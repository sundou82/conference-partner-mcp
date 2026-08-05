#!/usr/bin/env python3
"""List conference submission deadlines coming up in the next N days.

No API key needed — search is part of the anonymous tier.

    python upcoming_deadlines.py --days 90 --field ai --ccf A
    python upcoming_deadlines.py --days 30 --query neural --json
"""

import argparse
import datetime as dt
import json
import sys

import huiban


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--days", type=int, default=90, help="window size (default 90)")
    parser.add_argument("--field", choices=huiban.FIELDS, help="research field")
    parser.add_argument("--ccf", choices=["A", "B", "C"], help="CCF rank")
    parser.add_argument("--core", choices=["A*", "A", "B", "C"], help="CORE rank")
    parser.add_argument("--query", help="keyword")
    parser.add_argument("--json", action="store_true", help="print raw rows as JSON")
    args = parser.parse_args()

    today = dt.date.today()
    params = {
        "query": args.query,
        "field": args.field,
        "ccf_rank": args.ccf,
        "core_rank": args.core,
        "submission_date_start": today.isoformat(),
        "submission_date_end": (today + dt.timedelta(days=args.days)).isoformat(),
    }

    try:
        rows = list(huiban.paginate("/api/conferences", params, "conferences"))
    except huiban.ApiError as error:
        sys.exit(str(error))

    rows.sort(key=lambda c: c["submission_date"] or "")

    if args.json:
        print(json.dumps(rows, indent=2, ensure_ascii=False))
        return

    if not rows:
        print(f"Nothing due in the next {args.days} days for that filter.")
        return

    print(f"{len(rows)} deadlines in the next {args.days} days\n")
    for row in rows:
        days_left = (dt.date.fromisoformat(row["submission_date"]) - today).days
        ranks = "/".join(r for r in (row["ccf_rank"], row["core_rank"]) if r) or "-"
        extended = "  (extended)" if row["is_extended"] else ""
        print(f"{row['submission_date']}  {days_left:>4}d  {row['short_name']:<14} "
              f"{ranks:<8} {row['full_name'][:56]}{extended}")

    if huiban.quota_remaining:
        print(f"\nQuota remaining today: {huiban.quota_remaining}")


if __name__ == "__main__":
    main()
