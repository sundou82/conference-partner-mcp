#!/usr/bin/env python3
"""Normalise the fetched spec files into spec/ and refuse to write a broken one.

Run by .github/workflows/sync-spec.yml after curl has saved the raw responses.
Locally:

    curl -sSf -o raw-openapi.json https://www.myhuiban.com/api/openapi.json
    curl -sSf -o raw-tools.json -H 'Content-Type: application/json' \
      -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}' https://www.myhuiban.com/mcp
    curl -sSf -o raw-card.json https://www.myhuiban.com/.well-known/mcp/server-card.json
    python scripts/sync_spec.py

Explicit UTF-8 on both ends: the specs contain em dashes, and letting the
interpreter pick the platform default mangles them on Windows.
"""

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SPEC = ROOT / "spec"


def read(name):
    return json.loads((ROOT / name).read_bytes().decode("utf-8"))


def write(name, payload):
    path = SPEC / name
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
                    encoding="utf-8")
    return path


def main():
    SPEC.mkdir(exist_ok=True)

    openapi = read("raw-openapi.json")
    tools = read("raw-tools.json")["result"]
    card = read("raw-card.json")

    # A truncated or error response must never be committed over a good spec.
    problems = []
    if not openapi.get("info", {}).get("title"):
        problems.append("openapi: no info.title")
    if len(openapi.get("paths", {})) < 8:
        problems.append(f"openapi: only {len(openapi.get('paths', {}))} paths")
    if len(tools.get("tools", [])) < 8:
        problems.append(f"mcp: only {len(tools.get('tools', []))} tools")
    if not card.get("name"):
        problems.append("server-card: no name")
    if problems:
        sys.exit("refusing to write:\n  " + "\n  ".join(problems))

    write("openapi.json", openapi)
    write("mcp-tools.json", tools)
    write("server-card.json", card)

    print(f"openapi {openapi['info']['version']} — {len(openapi['paths'])} paths, "
          f"{len(tools['tools'])} MCP tools, server-card {card.get('version', '?')}")


if __name__ == "__main__":
    main()
