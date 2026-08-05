# Examples

Everything here runs against the live API with **no API key** — search, ranking lists and
statistics are on the anonymous tier (50 requests/day per IP).

Set `HUIBAN_API_KEY` to draw on an account quota instead (200/day) and to reach the detail
endpoints. Create one at
[myhuiban.com/account/api-keys](https://www.myhuiban.com/account/api-keys).

```bash
export HUIBAN_API_KEY=hb_xxxxxxxxxxxx    # optional
```

## Python

Standard library only — no `pip install`, Python 3.9+.
[`huiban.py`](python/huiban.py) is the shared 60-line client the three scripts use.

```bash
cd examples/python

# deadlines in the next 90 days, filtered
python upcoming_deadlines.py --days 90 --field ai --ccf A
python upcoming_deadlines.py --days 30 --query neural --json

# generate your own snapshot: JSON + CSV + Markdown table
python export_deadlines.py --out ./snapshot --days 180 --ranked-only

# keep a local mirror in step, day by day
python incremental_sync.py --state ./state.json
python incremental_sync.py --state ./state.json     # second run fetches only changes
```

## Node

No dependencies, Node 18+ (uses built-in `fetch`).

```bash
cd examples/node
node upcoming-deadlines.mjs --days 90 --field ai --ccf A
```

## curl

[`curl/quickstart.sh`](curl/quickstart.sh) walks the whole surface in a dozen calls —
search, filters, ranking lists, statistics, incremental sync, quota headers, both MCP
calls, and the 401 you get on a detail endpoint without a credential. Pipes through `jq`
if you have it.

```bash
bash examples/curl/quickstart.sh
```

## MCP client configs

[`mcp-config/`](mcp-config/) has ready-to-copy files for Claude Code, Cursor and VS Code,
each in an anonymous and a with-key variant. Walkthrough:
[`../docs/mcp-clients.md`](../docs/mcp-clients.md).

## Notes for anything you build on top

- **Search and ranking lists paginate differently.** Search returns `total_pages`;
  ranking lists return `has_more` and no total. The clients here handle both.
- **`id` is an integer**, in list rows and detail alike.
- Absent dates are `null`; absent ranks are `""`; an unrecorded `impact_factor` is
  `null` (unknown), never `0`.
- **Send a real `User-Agent`.** The stock `Python-urllib/3.x` is turned away at the edge.
- Errors are JSON, and the `message` on a 401 / 402 / 429 says what to do next — surface
  it rather than swallowing it.
- Every page costs one request against your daily quota. `paginate()` in both clients
  stops at 20 pages by default so a too-wide filter cannot spend the whole day's budget
  in one go.
