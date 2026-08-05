# MCP client setup

The server is **remote** — Streamable HTTP at `https://www.myhuiban.com/mcp`. There is
nothing to install, no `npx`, no local process. Any MCP client that can talk to a URL
works.

```
Endpoint      https://www.myhuiban.com/mcp
Transport     Streamable HTTP (POST; SSE framing if you send Accept: text/event-stream)
Protocol      2025-06-18
Auth          none for search / lists / statistics
              Authorization: Bearer <credential> for the three detail tools
```

## Two levels of access

**Without credentials** you get `search_conferences`, `search_journals`,
`list_conferences`, `list_journals` and `get_statistics`, at 50 calls/day per source IP.
That is enough to browse, filter and build deadline lists.

**With a credential** you additionally get `get_conference`, `get_journal` and
`get_researcher` — full CFP text, acceptance-rate history, edition history, ratings and
comments, related venues — at 200 calls/day.

Create a key at [myhuiban.com/account/api-keys](https://www.myhuiban.com/account/api-keys).
It starts with `hb_`, never expires, and is revocable on its own. Prefer it over a login
JWT for anything you configure once and forget: JWTs expire after six months and cannot be
revoked individually.

Start without a key. Add one when a client tells you a detail tool returned 401.

---

## Claude Code

```bash
claude mcp add --transport http conference-partner https://www.myhuiban.com/mcp
```

With a key:

```bash
claude mcp add --transport http conference-partner https://www.myhuiban.com/mcp \
  --header "Authorization: Bearer hb_YOUR_KEY"
```

Project-scoped, committed to the repo — `.mcp.json`:

```json
{
  "mcpServers": {
    "conference-partner": {
      "type": "http",
      "url": "https://www.myhuiban.com/mcp"
    }
  }
}
```

Verify with `claude mcp list` — it should report `✔ Connected`.

## Claude.ai and Claude Desktop

Settings → **Connectors** → *Add custom connector*, and paste
`https://www.myhuiban.com/mcp`.

To use the detail tools, open the connector's advanced settings and add a static request
header:

```
Authorization: Bearer hb_YOUR_KEY
```

## Cursor

`~/.cursor/mcp.json` for every project, or `.cursor/mcp.json` for one:

```json
{
  "mcpServers": {
    "conference-partner": {
      "url": "https://www.myhuiban.com/mcp",
      "headers": {
        "Authorization": "Bearer hb_YOUR_KEY"
      }
    }
  }
}
```

Drop the `headers` block for anonymous access.

## VS Code (GitHub Copilot)

`.vscode/mcp.json`. Use an input prompt rather than pasting the key into a file you might
commit:

```json
{
  "inputs": [
    {
      "type": "promptString",
      "id": "huiban-key",
      "description": "Conference Partner API key (hb_...)",
      "password": true
    }
  ],
  "servers": {
    "conference-partner": {
      "type": "http",
      "url": "https://www.myhuiban.com/mcp",
      "headers": {
        "Authorization": "Bearer ${input:huiban-key}"
      }
    }
  }
}
```

Anonymous is just the `servers` block with no `headers` and no `inputs`.

## ChatGPT

Settings → **Connectors** → *Create*. MCP server URL `https://www.myhuiban.com/mcp`.
Choose **No authentication**, or **API key** and paste your `hb_` key to enable the detail
tools.

## Smithery

Listed at [smithery.ai/server/sundou82/conference-partner](https://smithery.ai/server/sundou82/conference-partner).

Smithery proxies through its own gateway, so every Smithery user reaches the origin from
the same address and shares one anonymous per-IP bucket. If you use this route, fill in the
`apiKey` connection parameter with your `hb_` key — it is forwarded as your `Authorization`
header and puts you on your own account quota. Connecting directly to
`https://www.myhuiban.com/mcp` avoids the shared bucket entirely.

---

## Checking it by hand

List the tools:

```bash
curl -s https://www.myhuiban.com/mcp \
  -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'
```

Call one anonymously:

```bash
curl -s https://www.myhuiban.com/mcp \
  -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{
        "name":"search_conferences",
        "arguments":{"field":"ai","ccf_rank":"A","per_page":3}}}'
```

Results arrive as JSON text in `result.content[0].text` and, parsed, in
`result.structuredContent`.

A detail tool without a credential returns a JSON-RPC error carrying HTTP 401 — that is
the expected answer, not a misconfiguration.

## Troubleshooting

| Symptom | Cause |
|---|---|
| Client shows "needs authentication" immediately | Some clients probe a detail tool first. Search tools still work; add a key to silence it. |
| `401` on `get_conference` only | Working as intended — detail tools need a credential. |
| `401` on every tool | A credential *was* sent and is invalid, revoked or expired. Bad credentials are never downgraded to the anonymous tier — remove the header to fall back to it. |
| `429` | Anonymous daily quota (50/IP) is gone. Add a free key for 200/day. |
| `402` | Account daily quota is gone. Counters are per calendar day and reset overnight. |
| `405` on `GET /mcp` | Expected. The transport is POST; a plain GET is answered with `Allow: POST, OPTIONS, DELETE`. |

Anything else: `admin@myhuiban.com`.
