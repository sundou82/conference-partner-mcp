#!/usr/bin/env python3
"""Build your own conference-deadline snapshot from the live API.

Writes JSON, CSV and a Markdown table. Run it in your own CI on whatever cadence
you need — the output is current as of the run, which is the point of generating
it rather than committing one.

    python export_deadlines.py --out ./snapshot
    python export_deadlines.py --out ./snapshot --days 180 --ranked-only
    python export_deadlines.py --out ./snapshot --field ai --field security

Anonymous access is enough. Each page costs one request against the daily quota
(50/day per IP, or 200/day with HUIBAN_API_KEY set), so a wide window over every
field can need a key.
"""

import argparse
import csv
import datetime as dt
import json
import pathlib
import sys

import huiban

COLUMNS = ["short_name", "full_name", "submission_date", "notification_date",
           "conference_date", "location", "ccf_rank", "core_rank", "qualis_rank",
           "is_extended", "updated_at", "detail_page"]


def collect(days, fields, ranked_only):
    """Fetch every conference with a deadline inside the window, de-duplicated by id."""
    today = dt.date.today()
    window = {
        "submission_date_start": today.isoformat(),
        "submission_date_end": (today + dt.timedelta(days=days)).isoformat(),
    }

    by_id = {}
    for field in (fields or [None]):
        params = {**window, "field": field}
        for row in huiban.paginate("/api/conferences", params, "conferences"):
            if ranked_only and not (row["ccf_rank"] or row["core_rank"] or row["qualis_rank"]):
                continue
            by_id[row["id"]] = row

    return sorted(by_id.values(), key=lambda c: (c["submission_date"] or "", c["short_name"]))


def write_json(path, rows, meta):
    path.write_text(json.dumps({**meta, "conferences": rows}, indent=2, ensure_ascii=False),
                    encoding="utf-8")


def write_csv(path, rows):
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=COLUMNS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(path, rows, meta):
    lines = [
        f"# Upcoming conference deadlines ({meta['window_start']} → {meta['window_end']})",
        "",
        f"{len(rows)} venue{'s' if len(rows) != 1 else ''}. "
        f"Generated {meta['generated_at']} from the "
        "[Conference Partner API](https://www.myhuiban.com/developers).",
        "",
        "| Deadline | Conference | CCF | CORE | QUALIS | Held | Location |",
        "|---|---|---|---|---|---|---|",
    ]
    for row in rows:
        extended = " *(extended)*" if row["is_extended"] else ""
        name = f"[{row['short_name']}]({row['detail_page']})"
        lines.append(
            f"| {row['submission_date']}{extended} | {name} | {row['ccf_rank'] or '-'} | "
            f"{row['core_rank'] or '-'} | {row['qualis_rank'] or '-'} | "
            f"{row['conference_date'] or '-'} | {row['location'] or '-'} |"
        )
    lines += ["", "Data: Conference Partner (myhuiban.com). Ranking values are reproduced "
              "from CCF / CORE / QUALIS — cite those bodies for the rankings themselves."]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", default="./snapshot", help="output directory")
    parser.add_argument("--days", type=int, default=180, help="window size (default 180)")
    parser.add_argument("--field", action="append", choices=huiban.FIELDS,
                        help="restrict to a research field; repeatable")
    parser.add_argument("--ranked-only", action="store_true",
                        help="keep only venues carrying at least one ranking")
    args = parser.parse_args()

    try:
        rows = collect(args.days, args.field, args.ranked_only)
    except huiban.ApiError as error:
        sys.exit(str(error))

    today = dt.date.today()
    meta = {
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "source": "https://www.myhuiban.com/developers",
        "window_start": today.isoformat(),
        "window_end": (today + dt.timedelta(days=args.days)).isoformat(),
        "fields": args.field or "all",
        "count": len(rows),
    }

    out = pathlib.Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "deadlines.json", rows, meta)
    write_csv(out / "deadlines.csv", rows)
    write_markdown(out / "deadlines.md", rows, meta)

    print(f"{len(rows)} conferences -> {out}/deadlines.{{json,csv,md}}")
    if huiban.quota_remaining:
        print(f"Quota remaining today: {huiban.quota_remaining}")


if __name__ == "__main__":
    main()
