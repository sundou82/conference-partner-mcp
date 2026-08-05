#!/usr/bin/env python3
"""Keep a local mirror in step with the API using `updated_since`.

    python incremental_sync.py --state ./state.json          # first run: full pass
    python incremental_sync.py --state ./state.json          # later runs: only changes

State is a JSON file holding the checkpoint date and the mirrored rows, so this
is runnable as-is and easy to swap for a real database.

Two boundaries the API documents and this script respects:

  * Day resolution. Two edits on the same day are indistinguishable, so the next
    checkpoint is set to the highest `updated_at` seen and that whole day is
    re-fetched next time. Overlap by one day, never skip one.
  * Venues that have never been edited carry no `updated_at` and never appear in
    the incremental stream (~5% of the corpus). The first run therefore has to be
    a full pass without the parameter — which is what `--state` on a fresh file does.
"""

import argparse
import json
import pathlib
import sys

import huiban

ENTITIES = [("conferences", "/api/conferences"), ("journals", "/api/journals")]


def load(path):
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {"checkpoint": None, "conferences": {}, "journals": {}}


def sync(state, key, path):
    """Fetch the delta (or everything on a cold start) and merge it into state."""
    since = state["checkpoint"]
    params = {"updated_since": since} if since else {}

    mirror = state[key]
    seen, newest = 0, since

    for row in huiban.paginate(path, params, key):
        mirror[str(row["id"])] = row
        seen += 1
        if row.get("updated_at") and (newest is None or row["updated_at"] > newest):
            newest = row["updated_at"]

    mode = f"changes since {since}" if since else "full pass"
    print(f"{key:<12} {seen:>5} rows ({mode}), mirror now holds {len(mirror)}")
    return newest


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--state", default="./state.json", help="state file path")
    parser.add_argument("--since", help="override the stored checkpoint (YYYY-MM-DD)")
    args = parser.parse_args()

    path = pathlib.Path(args.state)
    state = load(path)
    if args.since:
        state["checkpoint"] = args.since

    try:
        watermarks = [sync(state, key, endpoint) for key, endpoint in ENTITIES]
    except huiban.ApiError as error:
        sys.exit(str(error))

    # Advance to the newest change actually observed — not to today. If nothing
    # changed, the checkpoint stays put and the next run re-asks the same question.
    watermarks = [w for w in watermarks if w]
    if watermarks:
        state["checkpoint"] = max(watermarks)

    path.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\ncheckpoint -> {state['checkpoint']}  (state in {path})")


if __name__ == "__main__":
    main()
