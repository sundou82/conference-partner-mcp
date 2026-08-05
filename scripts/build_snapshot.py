#!/usr/bin/env python3
"""Build the downloadable snapshot in data/ from the live API.

Run by .github/workflows/snapshot.yml. Locally:

    python scripts/build_snapshot.py            # anonymous, 50 requests/day
    HUIBAN_API_KEY=hb_xxx python scripts/build_snapshot.py

**Scope is deliberate and must stay this way**: every dataset here comes from an
endpoint the anonymous tier already serves — deadline searches and ranking lists,
the same rows anyone can fetch without credentials, and the same rows the website
and sitemap publish. Per-venue detail (CFP full text, acceptance-rate history,
edition history, ratings, the organiser's own website URL) is NOT exported and
must not be added: it needs credentials by design and is the upgrade path the API
exists to sell.

Adding a dataset means adding it to DATASETS below, and only from a path listed in
`AnonymousAccess::OPEN_REST_OPS` on the server.
"""

import argparse
import csv
import datetime as dt
import json
import os
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

# Reuse the published example client rather than keeping a second copy of it.
sys.path.insert(0, str(ROOT / "examples" / "python"))
import huiban  # noqa: E402

TODAY = dt.date.today()

#: Total request budget. The anonymous tier allows 50/day per IP; with
#: HUIBAN_API_KEY set the account tier allows 200. Staying under the smaller
#: number keeps the job runnable without a secret.
BUDGET = 200 if os.environ.get("HUIBAN_API_KEY") else 45

DATASETS = [
    {
        "slug": "upcoming-deadlines",
        "title": "Upcoming submission deadlines",
        "note": "Conferences whose submission deadline has not passed, soonest first.",
        "path": "/api/conferences",
        "params": {"submission_date_start": TODAY.isoformat()},
        "key": "conferences",
        "sort": lambda r: (r.get("submission_date") or "", r.get("short_name") or ""),
        "max_pages": 10,
    },
    {
        "slug": "ccf-conferences",
        "title": "CCF-ranked conferences",
        "note": "The CCF catalogue as carried on the site, with CORE and QUALIS alongside.",
        "path": "/api/conferences/rankings/ccf",
        "params": {},
        "key": "conferences",
        "max_pages": 7,
    },
    {
        "slug": "core-conferences",
        "title": "CORE-ranked conferences",
        "note": "The CORE catalogue as carried on the site.",
        "path": "/api/conferences/rankings/core",
        "params": {},
        "key": "conferences",
        "max_pages": 7,
    },
    {
        "slug": "qualis-conferences",
        "title": "QUALIS-ranked conferences",
        "note": "The QUALIS catalogue as carried on the site.",
        "path": "/api/conferences/rankings/qualis",
        "params": {},
        "key": "conferences",
        "max_pages": 7,
    },
    {
        "slug": "ccf-journals",
        "title": "CCF-ranked journals",
        "note": "Journals in the CCF catalogue, with impact factor and publisher.",
        "path": "/api/journals/rankings/ccf",
        "params": {},
        "key": "journals",
        "max_pages": 4,
    },
    {
        "slug": "journal-special-issues",
        "title": "Journals with an open special-issue call",
        "note": "Journals currently carrying a special-issue call for papers.",
        "path": "/api/journals/rankings/cfp",
        "params": {},
        "key": "journals",
        "max_pages": 3,
    },
    {
        "slug": "top-impact-factor-journals",
        "title": "Journals by impact factor",
        "note": "Highest reported impact factor first. Figures are as published by the "
                "journal and may lag the latest JCR.",
        "path": "/api/journals/rankings/highest_if",
        "params": {},
        "key": "journals",
        "max_pages": 3,
    },
]

CONFERENCE_COLUMNS = ["id", "short_name", "full_name", "submission_date",
                      "notification_date", "conference_date", "location",
                      "ccf_rank", "core_rank", "qualis_rank", "is_extended",
                      "acceptance_rate", "years", "clicked", "updated_at", "detail_page"]
JOURNAL_COLUMNS = ["id", "short_name", "full_name", "impact_factor", "publisher",
                   "issn", "ccf_rank", "clicked", "updated_at", "detail_page"]


class Budget:
    """Hard cap on requests, so a wide filter cannot spend the whole day's quota."""

    def __init__(self, total):
        self.total = total
        self.used = 0
        self.truncated = []

    def spend(self):
        if self.used >= self.total:
            return False
        self.used += 1
        return True


def fetch(dataset, budget):
    """Page through one dataset. Returns (rows, complete)."""
    rows = []
    for page in range(1, dataset["max_pages"] + 1):
        if not budget.spend():
            return rows, False

        data = huiban.get(dataset["path"],
                          {**dataset["params"], "page": page, "per_page": 100})
        rows.extend(data[dataset["key"]])

        pagination = data["pagination"]
        if "total_pages" in pagination:
            if page >= pagination["total_pages"]:
                return rows, True
        elif not pagination.get("has_more"):
            return rows, True

    return rows, False


def write_dataset(dataset, rows, generated_at):
    slug, key = dataset["slug"], dataset["key"]
    columns = CONFERENCE_COLUMNS if key == "conferences" else JOURNAL_COLUMNS
    present = [c for c in columns if any(c in row for row in rows)]

    payload = {
        "title": dataset["title"],
        "note": dataset["note"],
        "source": f"https://www.myhuiban.com{dataset['path']}",
        "generated_at": generated_at,
        "count": len(rows),
        "attribution": "Conference Partner (myhuiban.com). Ranking values are reproduced "
                       "from CCF / CORE / QUALIS; cite those bodies for the rankings.",
        key: rows,
    }
    (DATA / f"{slug}.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    with (DATA / f"{slug}.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=present, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({c: row.get(c, "") for c in present})


def deadline_table(rows, days):
    """Markdown table of the next `days` days — the part worth reading in a browser."""
    horizon = (TODAY + dt.timedelta(days=days)).isoformat()
    upcoming = [r for r in rows if r.get("submission_date")
                and TODAY.isoformat() <= r["submission_date"] <= horizon]

    lines = ["| Deadline | Conference | CCF | CORE | QUALIS | Held | Location |",
             "|---|---|---|---|---|---|---|"]
    for row in upcoming:
        extended = " *(extended)*" if row.get("is_extended") else ""
        lines.append(
            f"| {row['submission_date']}{extended} "
            f"| [{row.get('short_name') or row['full_name'][:30]}]({row['detail_page']}) "
            f"| {row.get('ccf_rank') or '-'} | {row.get('core_rank') or '-'} "
            f"| {row.get('qualis_rank') or '-'} | {row.get('conference_date') or '-'} "
            f"| {row.get('location') or '-'} |")
    return upcoming, "\n".join(lines)


def write_index(results, budget, generated_at, stats):
    deadlines = results["upcoming-deadlines"]
    shown, table = deadline_table(deadlines, 90)

    lines = [
        "# Data snapshot",
        "",
        f"Generated **{generated_at}** from the "
        "[Conference Partner API](https://www.myhuiban.com/developers). Refreshed daily by "
        "[CI](../.github/workflows/snapshot.yml).",
        "",
        "Every file here comes from the API's **anonymous tier** — the same rows anyone can "
        "fetch without credentials. Per-venue detail (CFP full text, acceptance-rate history, "
        "edition history, ratings, the organiser's own website URL) is not included; it needs "
        "a free credential and lives behind the API. See [../docs/data.md](../docs/data.md).",
        "",
        "## Files",
        "",
        "| Dataset | Rows | JSON | CSV |",
        "|---|---|---|---|",
    ]
    for dataset in DATASETS:
        slug = dataset["slug"]
        rows = results[slug]
        partial = " ⚠️ partial" if slug in budget.truncated else ""
        lines.append(f"| **{dataset['title']}**<br><sub>{dataset['note']}</sub> "
                     f"| {len(rows)}{partial} | [{slug}.json]({slug}.json) "
                     f"| [{slug}.csv]({slug}.csv) |")

    lines += [
        "",
        f"Site totals on the day of generation: **{stats['conferences_total']}** conferences, "
        f"**{stats['journals_total']}** journals.",
        "",
        "## Prefer live data",
        "",
        "A snapshot is stale the moment a deadline is extended, which happens daily in "
        "submission season. For anything that has to be right, call the API — it needs no "
        "key for exactly the data in this directory:",
        "",
        "```bash",
        "curl \"https://www.myhuiban.com/api/conferences?field=ai&submission_date_start=$(date +%F)\"",
        "```",
        "",
        "Or mirror it incrementally with `updated_since` — see "
        "[../docs/rest-api.md](../docs/rest-api.md#incremental-sync).",
        "",
        f"## Deadlines in the next 90 days ({len(shown)})",
        "",
        table,
        "",
        "---",
        "",
        "Data: **Conference Partner (myhuiban.com)**, free to use with attribution. Ranking "
        "values are reproduced from CCF / CORE / QUALIS — cite those bodies for the rankings "
        "themselves. The repository's MIT licence covers its code, not this data.",
    ]
    (DATA / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Rebuild data/ from the live API.")
    parser.add_argument("--budget", type=int, default=BUDGET,
                        help=f"request cap (default {BUDGET}); lower it to smoke-test "
                             "without spending the day's quota")
    args = parser.parse_args()

    DATA.mkdir(exist_ok=True)
    generated_at = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    budget = Budget(args.budget)

    try:
        budget.spend()
        stats = huiban.get("/api/statistics")

        results = {}
        for dataset in DATASETS:
            rows, complete = fetch(dataset, budget)
            if not complete:
                # Never let a cap pass silently as full coverage.
                budget.truncated.append(dataset["slug"])
                print(f"  ! {dataset['slug']}: truncated at {len(rows)} rows "
                      f"(page cap {dataset['max_pages']} or request budget)")
            if dataset.get("sort"):
                rows.sort(key=dataset["sort"])
            results[dataset["slug"]] = rows
            write_dataset(dataset, rows, generated_at)
            print(f"  {dataset['slug']:<28} {len(rows):>5} rows")
    except huiban.ApiError as error:
        sys.exit(f"aborting, data/ left untouched: {error}")

    write_index(results, budget, generated_at, stats)

    print(f"\n{budget.used}/{budget.total} requests used; "
          f"quota remaining today: {huiban.quota_remaining}")
    if budget.truncated:
        print(f"partial datasets: {', '.join(budget.truncated)}")


if __name__ == "__main__":
    main()
