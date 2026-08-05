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

# A dataset may issue several queries whose results are merged and de-duplicated by
# id — the rank catalogues need one query per rank value, because search filters on a
# single rank at a time. `max_pages` is the cap across all of them.
#
# The /rankings/{ccf,core,qualis} endpoints are deliberately NOT used for the
# catalogues: they list only venues with a call currently open — 68 rows for CCF,
# when a search for ccf_rank=A alone returns 57. That is a useful list, but it is not
# "every CCF-ranked venue", so it is published separately as open-calls-by-rank.
DATASETS = [
    {
        "slug": "upcoming-deadlines",
        "title": "Upcoming submission deadlines",
        "note": "Every conference whose submission deadline has not passed, soonest first.",
        "path": "/api/conferences",
        "queries": [{"submission_date_start": TODAY.isoformat()}],
        "key": "conferences",
        "sort": lambda r: (r.get("submission_date") or "", r.get("short_name") or ""),
        "max_pages": 10,
    },
    {
        "slug": "ccf-conferences",
        "title": "CCF-ranked conferences",
        "note": "Every conference carrying a CCF rank, whether or not a call is open. "
                "CORE and QUALIS ranks are on the same row where the venue has them.",
        "path": "/api/conferences",
        "queries": [{"ccf_rank": rank} for rank in ("A", "B", "C")],
        "key": "conferences",
        "sort": lambda r: (r.get("ccf_rank") or "", r.get("short_name") or ""),
        "max_pages": 8,
    },
    {
        "slug": "core-conferences",
        "title": "CORE-ranked conferences",
        "note": "Every conference carrying a CORE rank, whether or not a call is open.",
        "path": "/api/conferences",
        "queries": [{"core_rank": rank} for rank in ("A*", "A", "B", "C")],
        "key": "conferences",
        "sort": lambda r: (r.get("core_rank") or "", r.get("short_name") or ""),
        "max_pages": 9,
    },
    {
        "slug": "open-calls-by-rank",
        "title": "Ranked conferences with a call open now",
        "note": "The subset of the catalogues you can still submit to today — CCF, CORE "
                "and QUALIS lists merged.",
        "path": "/api/conferences/rankings/ccf",
        "queries": [{}],
        "extra_paths": ["/api/conferences/rankings/core",
                        "/api/conferences/rankings/qualis"],
        "key": "conferences",
        "sort": lambda r: (r.get("submission_date") or "", r.get("short_name") or ""),
        "max_pages": 5,
    },
    {
        "slug": "ccf-journals",
        "title": "CCF-ranked journals",
        "note": "Journals in the CCF catalogue, with impact factor, publisher and ISSN.",
        "path": "/api/journals",
        "queries": [{"ccf_rank": rank} for rank in ("A", "B", "C")],
        "key": "journals",
        "sort": lambda r: (r.get("ccf_rank") or "", r.get("short_name") or ""),
        "max_pages": 5,
    },
    {
        "slug": "journal-special-issues",
        "title": "Journals with an open special-issue call",
        "note": "Journals currently carrying a special-issue call for papers.",
        "path": "/api/journals/rankings/cfp",
        "queries": [{}],
        "key": "journals",
        "max_pages": 3,
    },
    {
        "slug": "top-impact-factor-journals",
        "title": "Top journals by impact factor",
        "note": "The 300 highest reported impact factors. Figures are as published by the "
                "journal and may lag the latest JCR.",
        "path": "/api/journals/rankings/highest_if",
        "queries": [{}],
        "key": "journals",
        # Intentionally the top N rather than the whole table — not a truncation.
        "capped": True,
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
    """Run every query of a dataset, merge by id. Returns (rows, complete).

    complete is False when a page cap or the request budget cut a query short, so
    the caller can say so rather than presenting a partial list as the whole thing.
    """
    key = dataset["key"]
    paths = [dataset["path"]] + dataset.get("extra_paths", [])
    by_id, pages_left, complete = {}, dataset["max_pages"], True

    for path in paths:
        for query in dataset["queries"]:
            page = 1
            while True:
                if pages_left <= 0 or not budget.spend():
                    return list(by_id.values()), False
                pages_left -= 1

                data = huiban.get(path, {**query, "page": page, "per_page": 100})
                for row in data[key]:
                    by_id[row["id"]] = row

                pagination = data["pagination"]
                exhausted = (page >= pagination["total_pages"]
                             if "total_pages" in pagination
                             else not pagination.get("has_more"))
                if exhausted:
                    break
                page += 1

    return list(by_id.values()), complete


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
            if not complete and not dataset.get("capped"):
                # Never let an accidental cap pass silently as full coverage.
                # A dataset declared "capped" is a top-N by design, not a shortfall.
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
