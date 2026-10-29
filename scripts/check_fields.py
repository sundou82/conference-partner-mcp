#!/usr/bin/env python3
"""Fail when a client-side research-field list disagrees with the API spec.

The example client and the deadline-watch action each keep a copy of the field
slugs (the action to print a friendly error, the examples for argparse choices).
Both once stayed at the original 14 computer-science fields for months after the
server grew to 21, quietly refusing every non-CS field. Run by sync-spec.yml right
after spec/ is refreshed, so the next drift turns that job red the day it happens.
"""

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples" / "python"))
sys.path.insert(0, str(ROOT / "actions" / "deadline-watch"))
import huiban  # noqa: E402
import deadline_watch  # noqa: E402


def spec_enums():
    spec = json.loads((ROOT / "spec" / "openapi.json").read_text(encoding="utf-8"))
    found = []
    for path, ops in spec["paths"].items():
        for op in ops.values():
            for param in op.get("parameters", []) if isinstance(op, dict) else []:
                if param.get("name") == "field" and "enum" in param.get("schema", {}):
                    found.append((path, param["schema"]["enum"]))
    return found


def main():
    enums = spec_enums()
    # Probe: an empty scan would let every comparison below pass vacuously.
    if not enums:
        sys.exit("no `field` enum found in spec/openapi.json - has the spec changed shape?")

    clients = {"examples/python/huiban.py FIELDS": list(huiban.FIELDS),
               "deadline_watch.py FIELD_NAMES": list(deadline_watch.FIELD_NAMES)}
    problems = []
    for path, enum in enums:
        for name, values in clients.items():
            missing, extra = set(enum) - set(values), set(values) - set(enum)
            if missing or extra:
                problems.append(f"{name} vs {path}: missing {sorted(missing)}, "
                                f"extra {sorted(extra)}")
    if problems:
        sys.exit("research-field lists drifted from the spec:\n  " + "\n  ".join(problems))
    print(f"field lists match the spec ({len(enums)} enums, {len(enums[0][1])} slugs)")


if __name__ == "__main__":
    main()
