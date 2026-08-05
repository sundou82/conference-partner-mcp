#!/usr/bin/env python3
"""Render the deadline table the action posts into an issue.

Standalone on purpose: this file is the most-read thing in the repository for
anyone deciding whether to trust the API, so it depends on nothing but the
standard library and reads top to bottom.

Writes deadline-watch-body.md in the working directory and sets the action
outputs. Configured entirely through environment variables, which is what the
composite action passes in.
"""

import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

BASE = os.environ.get("HUIBAN_BASE_URL", "https://www.myhuiban.com")
UA = "conference-deadline-watch/1.0 (+https://github.com/sundou82/conference-partner-mcp)"

FIELD_NAMES = {
    "ai": "AI & Machine Learning", "vision": "Computer Vision", "nlp": "NLP & Speech",
    "data": "Data Mining & Databases", "network": "Networks", "security": "Security & Privacy",
    "se": "Software Engineering", "systems": "Systems & Architecture",
    "theory": "Theory & Algorithms", "hci": "Human-Computer Interaction",
    "graphics": "Graphics & Multimedia", "bio": "Bioinformatics & Health",
    "robotics": "Robotics & Control", "web": "Information Systems & Web",
}


def get(params):
    query = urllib.parse.urlencode({k: v for k, v in params.items() if v not in (None, "")})
    request = urllib.request.Request(f"{BASE}/api/conferences?{query}")
    request.add_header("Accept", "application/json")
    request.add_header("User-Agent", UA)

    key = os.environ.get("HUIBAN_API_KEY", "").strip()
    if key:
        request.add_header("Authorization", f"Bearer {key}")

    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.loads(response.read())["data"]
    except urllib.error.HTTPError as error:
        payload = json.loads(error.read() or b"{}")
        # 429 here means the anonymous per-IP budget is gone. Say what to do about it
        # rather than failing with a bare status code.
        hint = ""
        if error.code == 429:
            hint = ("\nThe anonymous daily limit is per source IP and GitHub runners are shared. "
                    "Pass a free api-key input to use an account quota instead: "
                    "https://www.myhuiban.com/account/api-keys")
        sys.exit(f"Conference Partner API returned {error.code}: "
                 f"{payload.get('message', error.reason)}{hint}")


def collect(field, days):
    today = dt.date.today()
    window = {
        "field": field,
        "submission_date_start": today.isoformat(),
        "submission_date_end": (today + dt.timedelta(days=days)).isoformat(),
        "per_page": 100,
    }

    rows, page = [], 1
    while page <= 10:                       # guard: each page costs one request
        data = get({**window, "page": page})
        rows.extend(data["conferences"])
        if page >= data["pagination"]["total_pages"]:
            break
        page += 1
    return rows


def main():
    field = os.environ.get("HUIBAN_FIELD", "").strip()
    ccf = os.environ.get("HUIBAN_CCF", "").strip().upper()
    core = os.environ.get("HUIBAN_CORE", "").strip().upper()
    days = int(os.environ.get("HUIBAN_DAYS", "90") or 90)
    ranked_only = os.environ.get("HUIBAN_RANKED_ONLY", "false").lower() == "true"

    if field and field not in FIELD_NAMES:
        sys.exit(f"Unknown field '{field}'. Valid: {', '.join(FIELD_NAMES)}")

    rows = collect(field, days)
    before_ranks = len(rows)

    # Rank filters are applied here rather than in the query so that one fetch
    # covers both, and so "CCF A or CORE A*" stays possible for callers later.
    if ccf:
        rows = [r for r in rows if (r.get("ccf_rank") or "").upper() == ccf]
    if core:
        rows = [r for r in rows if (r.get("core_rank") or "").upper() == core]
    if ranked_only:
        rows = [r for r in rows if r.get("ccf_rank") or r.get("core_rank") or r.get("qualis_rank")]

    rows.sort(key=lambda r: (r.get("submission_date") or "", r.get("short_name") or ""))

    today = dt.date.today()
    scope = FIELD_NAMES.get(field, "all fields")
    tiers = " · ".join(x for x in (f"CCF {ccf}" if ccf else "", f"CORE {core}" if core else "") if x)

    filters = " · ".join(x for x in (scope, tiers, "ranked only" if ranked_only else "") if x)
    lines = [
        f"**{len(rows)}** submission deadlines in the next **{days}** days — {filters}",
        "",
    ]
    if rows:
        # QUALIS gets its own column rather than being implied: `ranked-only` keeps
        # QUALIS-only venues, and showing them with "-" under both CCF and CORE made
        # the filter look broken. Carrying all three side by side is also the thing
        # this dataset does that deadline lists generally do not.
        lines += ["| Deadline | Left | Conference | CCF | CORE | QUALIS | Held | Location |",
                  "|---|---|---|---|---|---|---|---|"]
        for r in rows:
            deadline = dt.date.fromisoformat(r["submission_date"])
            left = (deadline - today).days
            extended = " *(extended)*" if r.get("is_extended") else ""
            name = r.get("short_name") or r["full_name"][:34]
            lines.append(
                f"| {r['submission_date']}{extended} | {left}d "
                f"| [{name}]({r['detail_page']}) | {r.get('ccf_rank') or '-'} "
                f"| {r.get('core_rank') or '-'} | {r.get('qualis_rank') or '-'} "
                f"| {r.get('conference_date') or '-'} "
                f"| {(r.get('location') or '-').strip()} |")
    elif before_ranks:
        # Distinguish "no data" from "your filter removed it all" — the obvious
        # first config (field: ai + ccf: A) really does return nothing, because
        # the big ranked AI venues have no open call right now. An empty table
        # with no explanation reads as a broken action.
        lines.append(
            f"_The window holds **{before_ranks}** deadlines, but none match the rank filter"
            + (f" ({tiers})" if tiers else "")
            + ". Ranked venues open their calls in bursts, so this is normal between cycles — "
              "widen `days`, or drop `ccf` / `core` to see everything._")
    else:
        lines.append("_Nothing due in this window. Try a longer `days`, or a different `field`._")

    lines += [
        "",
        "---",
        f"<sub>Updated {dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M} UTC by "
        "[conference-deadline-watch](https://github.com/sundou82/conference-partner-mcp/tree/main/actions/deadline-watch). "
        "Data: [Conference Partner](https://www.myhuiban.com). Rankings are reproduced from "
        "CCF / CORE / QUALIS. Deadlines move — check the venue page before relying on one.</sub>",
    ]

    with open("deadline-watch-body.md", "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")

    output = os.environ.get("GITHUB_OUTPUT")
    if output:
        with open(output, "a", encoding="utf-8") as fh:
            fh.write(f"count={len(rows)}\n")
            fh.write(f"soonest={rows[0]['submission_date'] if rows else ''}\n")

    print(f"{len(rows)} deadlines, soonest {rows[0]['submission_date'] if rows else 'n/a'}")


if __name__ == "__main__":
    main()
