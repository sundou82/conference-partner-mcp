# Conference Partner — MCP server & REST API

Academic **conference and journal** data for AI agents and scripts: CFP deadlines,
CCF / CORE / QUALIS rankings, acceptance-rate history, edition history, journal impact
factors and special issues — served by [Conference Partner](https://www.myhuiban.com)
(会伴), a conference tracker that has been maintained since 2013.

Two surfaces over one dataset:

| | Endpoint | For |
|---|---|---|
| **MCP** | `https://www.myhuiban.com/mcp` (Streamable HTTP) | Claude, ChatGPT, Cursor, VS Code, any MCP client |
| **REST** | `https://www.myhuiban.com/api/*` | scripts, backends, OpenAPI codegen |

Both are backed by the same services and return **identical payloads** — the only
difference is the protocol envelope.

**Search, ranking lists and site statistics need no credentials at all.** Point a client
at the URL and the first call works.

```bash
curl "https://www.myhuiban.com/api/conferences?ccf_rank=A&field=ai&submission_date_start=2026-08-05"
```

---

## Add it to your MCP client

<details open>
<summary><b>Claude Code</b></summary>

```bash
claude mcp add --transport http conference-partner https://www.myhuiban.com/mcp
```
</details>

<details>
<summary><b>Claude.ai / Claude Desktop</b> (Settings → Connectors → Add custom connector)</summary>

Remote MCP server URL:

```
https://www.myhuiban.com/mcp
```

To unlock the detail tools, add a static request header in the connector's advanced
settings: `Authorization: Bearer hb_xxx` (see [Credentials](#credentials)).
</details>

<details>
<summary><b>Cursor</b> — <code>~/.cursor/mcp.json</code> or <code>.cursor/mcp.json</code></summary>

```json
{
  "mcpServers": {
    "conference-partner": {
      "url": "https://www.myhuiban.com/mcp"
    }
  }
}
```
</details>

<details>
<summary><b>VS Code</b> — <code>.vscode/mcp.json</code></summary>

```json
{
  "servers": {
    "conference-partner": {
      "type": "http",
      "url": "https://www.myhuiban.com/mcp"
    }
  }
}
```
</details>

<details>
<summary><b>ChatGPT</b> (Settings → Connectors → Create)</summary>

MCP server URL `https://www.myhuiban.com/mcp`, authentication **No authentication**
(or *API key* with your `hb_` key to enable the detail tools).
</details>

Ready-to-copy files for each client live in [`examples/mcp-config/`](examples/mcp-config/),
and the per-client walkthrough — including how to attach a key — is in
[`docs/mcp-clients.md`](docs/mcp-clients.md).

Also listed on [Smithery](https://smithery.ai/server/sundou82/conference-partner),
[Glama](https://glama.ai/mcp/connectors/com.myhuiban.www/conference-partner) and the
[official MCP registry](https://registry.modelcontextprotocol.io) as
`com.myhuiban.www/conference-partner`.

---

## Tools

Eight read-only tools, each with a REST twin returning the same payload.

| Tool | REST twin | Credentials |
|---|---|---|
| `search_conferences` | `GET /api/conferences` | — |
| `search_journals` | `GET /api/journals` | — |
| `list_conferences` | `GET /api/conferences/rankings/{ranking}` | — |
| `list_journals` | `GET /api/journals/rankings/{ranking}` | — |
| `get_statistics` | `GET /api/statistics` | — |
| `get_conference` | `GET /api/conferences/{id}` | free account |
| `get_journal` | `GET /api/journals/{id}` | free account |
| `get_researcher` | `GET /api/researchers/{id}` | free account |

Search accepts any combination of keyword, `ccf_rank` (A/B/C), `core_rank` (A\*/A/B/C),
`qualis_rank`, `field` (14 CS areas), submission/conference date ranges and
`updated_since` for incremental sync. **Every parameter is optional** — filter-only
queries such as "AI conferences with a deadline in the next 90 days" are the point.

Ranking lists cover open CFPs, the three tier lists, popularity, lowest acceptance rate,
trending, upcoming/past — and for journals, special-issue CFPs and highest impact factor.

Full machine-readable definitions, refreshed from production by CI:
[`spec/openapi.json`](spec/openapi.json) and [`spec/mcp-tools.json`](spec/mcp-tools.json).

---

## Credentials

| Tier | How | Limit |
|---|---|---|
| **Anonymous** | send nothing | 50 requests/day per source IP |
| **Free account** | `Authorization: Bearer hb_xxx` | 200 requests/day, shared across REST + MCP |
| Paid | — | *planned, not available yet* |

Create a key at [myhuiban.com/account/api-keys](https://www.myhuiban.com/account/api-keys)
— it never expires and can be revoked individually, which is what you want for a client
that only lets you pin a fixed request header. A JWT from `POST /api/login` works too and
draws on the same pool.

Every response carries `X-Quota-Limit` and `X-Quota-Remaining`. CORS is open, so browser
JavaScript works.

`401` = this endpoint needs a credential, or the one you sent is invalid. An unusable
credential is **never** silently downgraded to the anonymous tier.
`402` = account quota exhausted. `429` = anonymous per-IP quota exhausted.

---

## Examples

Runnable, no API key required:

```bash
# upcoming CCF-A deadlines in AI, next 90 days
python examples/python/upcoming_deadlines.py --field ai --ccf A --days 90

# same thing in Node
node examples/node/upcoming-deadlines.mjs --field ai --ccf A --days 90

# build your own deadline snapshot (JSON + CSV + Markdown table)
python examples/python/export_deadlines.py --out ./snapshot

# incremental sync — only what changed since your last checkpoint
python examples/python/incremental_sync.py --since 2026-07-01

# shell one-liners
bash examples/curl/quickstart.sh
```

See [`examples/README.md`](examples/README.md).

---

## Download the data

[**`data/`**](data/) carries a snapshot refreshed daily by CI, as JSON and CSV:

| | |
|---|---|
| [`upcoming-deadlines`](data/upcoming-deadlines.csv) | every conference whose deadline has not passed |
| [`ccf-conferences`](data/ccf-conferences.csv) · [`core-conferences`](data/core-conferences.csv) | the tier catalogues — all three ranks are columns on every row |
| [`open-calls-by-rank`](data/open-calls-by-rank.csv) | the ranked venues you can still submit to today |
| [`ccf-journals`](data/ccf-journals.csv) · [`top-impact-factor-journals`](data/top-impact-factor-journals.csv) | journals by tier and by impact factor |
| [`journal-special-issues`](data/journal-special-issues.csv) | journals with an open special-issue call |

[`data/README.md`](data/README.md) renders the next 90 days as a table you can read in
the browser.

The snapshot covers exactly what the **anonymous tier already serves** — nothing in it is
gated. Per-venue detail (CFP full text, acceptance-rate history, edition history, ratings)
stays behind the API, where a free key reaches it.

A file is stale the moment a deadline is extended, which in submission season is daily.
Use it to browse, diff or bulk-load; call the API when it has to be right.

---

## Why this dataset

Deadline lists are easy to find. These are the parts that are hard to reproduce:

- **Three ranking systems in one row** — CCF, CORE and QUALIS on the same venue, so
  "CCF-A that is also CORE-A\*" is one query rather than a join across three sources.
- **Acceptance-rate history** and **edition history** — how a venue's selectivity and
  location moved across editions, back to 2013.
- **Journals as first-class entities** — impact factor, publisher, ISSN, and
  special-issue CFPs, which conference-only lists do not carry.
- **Incremental sync** — `updated_since` with an `updated_at` watermark on every row, so
  a mirror is a diff rather than a re-crawl.
- Human-curated, not scraped: dates are entered and corrected by maintainers and by the
  organisers themselves through a venue-claim process.

Methodology, coverage and known limits: [myhuiban.com/methodology](https://www.myhuiban.com/methodology).

---

## About this repository

This repo is the distribution entry point for the API and MCP server: client
configuration, examples, and CI-synced specs. **The server itself is not open source** —
it is a hosted service; nothing here needs to be installed or run to use it.

- [`docs/mcp-clients.md`](docs/mcp-clients.md) — per-client setup, with and without a key
- [`docs/rest-api.md`](docs/rest-api.md) — endpoints, parameters, errors, incremental sync
- [`docs/data.md`](docs/data.md) — what is in the dataset, attribution, terms
- [`examples/`](examples/) — runnable Python, Node and curl clients; MCP config files
- [`spec/`](spec/) — OpenAPI 3 document, MCP tool definitions and server card, re-fetched
  from production daily by [CI](.github/workflows/sync-spec.yml) so they cannot go stale

Authoritative reference: **[myhuiban.com/developers](https://www.myhuiban.com/developers)**.
Where this repo and that page ever disagree, the page is right — it ships with the API.

Issues and PRs about the client-side material here are welcome. For data corrections use
the "report" link on the venue page, and for anything else email `admin@myhuiban.com`.

## License

[MIT](LICENSE) for the code and configuration in this repository.

The **data served by the API is not covered by that license**. It is free to use,
including commercially, with attribution: cite the canonical venue URL and
"Conference Partner (myhuiban.com)". If your claim is about a ranking value itself, cite
the ranking body — Conference Partner reproduces those lists, it does not define them.
Bulk use should start from `data/` rather than a crawl of your own, and dataset licensing
or model training needs a conversation first. See [`docs/data.md`](docs/data.md) and the
[terms on the site](https://www.myhuiban.com/developers).
