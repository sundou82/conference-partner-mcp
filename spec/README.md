# Machine-readable specs

**Generated files — do not edit.** `.github/workflows/sync-spec.yml` re-fetches them from
production every day and commits any change, so they cannot drift from the deployed API.
Fix anything wrong here in the server, not in this directory.

| File | Source |
|---|---|
| `openapi.json` | [`/api/openapi.json`](https://www.myhuiban.com/api/openapi.json) — OpenAPI 3.0.3 |
| `mcp-tools.json` | `tools/list` on [`/mcp`](https://www.myhuiban.com/mcp) |
| `server-card.json` | [`/.well-known/mcp/server-card.json`](https://www.myhuiban.com/.well-known/mcp/server-card.json) — SEP-1649 descriptor |

## Generating a client

```bash
npx @openapitools/openapi-generator-cli generate \
  -i spec/openapi.json -g python -o ./client
```

Two things a generated client will not know:

- Endpoints that need credentials answer `401` when called without them. That is the
  contract, not a bug — see [`../docs/rest-api.md`](../docs/rest-api.md).
- Search and ranking-list endpoints paginate with different response shapes.
