# REST API

Base URL `https://www.myhuiban.com`. Read-only, JSON, CORS open.
OpenAPI 3 document: [`../spec/openapi.json`](../spec/openapi.json), served live at
[`/api/openapi.json`](https://www.myhuiban.com/api/openapi.json).

Every endpoint here has an MCP twin returning the same payload; see
[mcp-clients.md](mcp-clients.md).

## Envelope

```json
{
  "code": 200,
  "message": "Success",
  "data": { "...": "..." },
  "request_id": "req_..."
}
```

`code` mirrors the HTTP status for transport-level outcomes. Validation errors come back
as HTTP 200 with `code: 400` in the body; a missing entity is a real HTTP 404. Quote
`request_id` in any bug report.

## Endpoints

| Method | Path | Credentials |
|---|---|---|
| `GET` | `/api/conferences` | — |
| `GET` | `/api/conferences/rankings/{ranking}` | — |
| `GET` | `/api/journals` | — |
| `GET` | `/api/journals/rankings/{ranking}` | — |
| `GET` | `/api/statistics` | — |
| `GET` | `/api/conferences/{id}` | free account |
| `GET` | `/api/journals/{id}` | free account |
| `GET` | `/api/researchers/{id}` | free account |
| `POST` | `/api/login` | — (returns a JWT) |

### Search conferences — `GET /api/conferences`

All parameters optional; combine freely.

| Parameter | Values |
|---|---|
| `query` | keyword, matched against short and full name |
| `ccf_rank` | `A` `B` `C` |
| `core_rank` | `A*` `A` `B` `C` |
| `qualis_rank` | e.g. `A1` `A2` `B1` |
| `field` | one of the 14 slugs below |
| `submission_date_start` / `submission_date_end` | `YYYY-MM-DD` |
| `conference_date_start` / `conference_date_end` | `YYYY-MM-DD` |
| `updated_since` | `YYYY-MM-DD`, see [Incremental sync](#incremental-sync) |
| `page` / `per_page` | 1-based; `per_page` max 100, default 10 |

Filter-only queries are supported and are the most useful shape — "what is due in the
next 90 days in security" needs no keyword.

```bash
curl "https://www.myhuiban.com/api/conferences?field=security&submission_date_start=2026-08-05&submission_date_end=2026-11-03&per_page=50"
```

Research field slugs: `ai` `vision` `nlp` `data` `network` `security` `se` `systems`
`theory` `hci` `graphics` `bio` `robotics` `web`.

### Search journals — `GET /api/journals`

`query`, `ccf_rank`, `issn` (fuzzy), `field`, `updated_since`, `page`, `per_page`.

### Ranking lists — `GET /api/{conferences,journals}/rankings/{ranking}`

Conferences: `cfp` (open calls) · `past_cfp` · `ccf` · `core` · `qualis` ·
`most_viewed` · `most_tracked` · `most_attended` · `most_competitive` (lowest acceptance
rate) · `upcoming` · `past` · `trending` (most viewed in the last 30 days).

Journals: `cfp` (special-issue calls) · `ccf` · `highest_if` · `most_viewed` ·
`most_tracked` · `all`.

Paginated with `page` / `per_page` (default 20, max 100). An unknown ranking returns 400
with the valid values listed in the message.

Ranking rows carry a few extra fields — `years` (editions on record), `clicked` (page
views) and, for `most_competitive`, `acceptance_rate`.

> **Pagination differs between the two families.** Search endpoints return
> `{"total": n, "page": p, "per_page": s, "total_pages": t}`; ranking lists return
> `{"page": p, "per_page": s, "count": n, "has_more": bool}` with no total. Loop on
> `page < total_pages` for search and on `has_more` for rankings — the example clients
> handle both.

### Details — `GET /api/{conferences,journals,researchers}/{id}`

Requires `Authorization: Bearer <credential>`.

Conference detail adds CFP text, acceptance-rate history, edition history, structured
ratings, comments and related venues. Journal detail adds CFP text, special issues,
ratings, comments and related venues. Researcher detail is a public profile — name,
institution, auto-generated research-interest summary, CV, tracked/attended venues —
never contact details, and by id only: there is no researcher search or enumeration.

### Statistics — `GET /api/statistics`

Totals, upcoming deadlines by month, conference country distribution, journal impact
factor and publisher distributions.

## List rows

```json
{
  "id": 411,
  "short_name": "ACL",
  "full_name": "Annual Meeting of the Association for Computational Linguistics",
  "submission_date": null,
  "notification_date": null,
  "conference_date": "2027-08-17",
  "location": "Japan",
  "ccf_rank": "A",
  "core_rank": "A*",
  "qualis_rank": "A1",
  "is_extended": false,
  "updated_at": "2026-07-05",
  "detail_page": "https://www.myhuiban.com/conference/411"
}
```

Notes that bite if you assume otherwise:

- `id` is an **integer**, and matches the `id` the detail endpoints and MCP detail
  tools expect — the output of a search feeds straight into a lookup.
- Date fields are `null` when unannounced, and `""` is used for an absent rank.
- `impact_factor` is `null` when a journal has none on record — that is "unknown",
  not "zero". Do not coerce it to 0 before sorting or filtering.
- `is_extended` marks a deadline that has been pushed back at least once.
- Responses link to `detail_page` — the canonical Conference Partner page — and not to the
  venue's own website. Attribution therefore always resolves to a page that shows where
  the data came from. The official website URL is part of the planned paid tier.

## Authentication

Two credential types, one `Authorization: Bearer` header, one shared quota pool.

**API key** — create at
[/account/api-keys](https://www.myhuiban.com/account/api-keys). Starts with `hb_`, never
expires, revocable individually. Use this for anything configured once.

**JWT** — `POST /api/login` with your site credentials:

```bash
curl -X POST https://www.myhuiban.com/api/login \
  -H 'Content-Type: application/json' \
  -d '{"email":"you@example.com","password":"..."}'
```

Valid six months, not individually revocable.

```
Authorization: Bearer hb_xxxxxxxxxxxx
```

## Quotas

| Tier | Limit |
|---|---|
| Anonymous | 50 requests/day per source IP |
| Free account | 200 requests/day, REST and MCP together |
| Paid | *planned, not available yet* |

`X-Quota-Limit` and `X-Quota-Remaining` are on every response and are exposed via CORS.

| Status | Meaning |
|---|---|
| `401` | Endpoint needs a credential, or the one sent is invalid/revoked/expired. Invalid credentials are **never** silently downgraded to the anonymous tier — send no `Authorization` header at all to use that tier. |
| `402` | Account daily quota exhausted. |
| `429` | Anonymous per-IP daily quota exhausted. |

Errors are always JSON, including the ones raised before the endpoint runs.

Need more than 200/day, or a bulk export? Email `admin@myhuiban.com` and describe the use
case.

## Incremental sync

Pass `updated_since=YYYY-MM-DD` to either search endpoint to get only venues changed on or
after that date, and use the `updated_at` field of the rows you receive as the next
checkpoint.

```bash
curl "https://www.myhuiban.com/api/conferences?updated_since=2026-07-01&per_page=100"
```

Two boundaries worth knowing before you build a mirror on it:

- **Day resolution.** Two changes on the same day are indistinguishable; re-fetch the
  whole day rather than assuming ordering within it.
- **Never-edited venues do not appear in the incremental stream** (about 5% of the
  corpus). Do a full pass once without the parameter, then go incremental.

[`../examples/python/incremental_sync.py`](../examples/python/incremental_sync.py) is a
working checkpoint loop.

## Other machine-readable surfaces

Same data, no API key, no quota — useful when you want a feed rather than an API:

- [`/llms.txt`](https://www.myhuiban.com/llms.txt) — site description for LLM agents
- [`/llms-full.txt`](https://www.myhuiban.com/llms-full.txt) — with a live data sample
- [`/feed/upcoming-deadlines.xml`](https://www.myhuiban.com/feed/upcoming-deadlines.xml) — RSS, next 30 days
- [`/calendar/deadlines.ics`](https://www.myhuiban.com/calendar/deadlines.ics) — iCalendar subscription
- Any venue page with `Accept: text/markdown` returns Markdown instead of HTML
- [`/.well-known/api-catalog`](https://www.myhuiban.com/.well-known/api-catalog) — RFC 9727 discovery
