#!/usr/bin/env bash
# Conference Partner in ten curl calls. Nothing here needs an API key except the
# last two, which show what happens without one and with one.
#
#   bash quickstart.sh
#   HUIBAN_API_KEY=hb_xxx bash quickstart.sh
#
# Requires curl. `jq` is optional — output is piped through it when present.

set -uo pipefail

BASE="${HUIBAN_BASE_URL:-https://www.myhuiban.com}"
KEY="${HUIBAN_API_KEY:-}"

pretty() { if command -v jq >/dev/null 2>&1; then jq "${1:-.}"; else cat; fi; }
step()   { printf '\n\033[1m== %s\033[0m\n' "$1"; }

step 'CCF-A conferences with an open deadline, soonest first'
curl -s "$BASE/api/conferences?ccf_rank=A&submission_date_start=$(date +%F)&per_page=5" \
  | pretty '.data.conferences[] | {short_name, submission_date, conference_date, location}'

step 'Security conferences due in the next 90 days (filter only, no keyword)'
curl -s "$BASE/api/conferences?field=security&submission_date_start=$(date +%F)&submission_date_end=$(date -d '+90 days' +%F 2>/dev/null || date -v+90d +%F)&per_page=5" \
  | pretty '.data.conferences[] | {short_name, submission_date, ccf_rank}'

step 'Keyword search across journals, CCF-A only'
curl -s "$BASE/api/journals?query=machine+learning&ccf_rank=A&per_page=5" \
  | pretty '.data.journals[] | {short_name, full_name, impact_factor}'

step 'Ranking list: open calls for papers'
curl -s "$BASE/api/conferences/rankings/cfp?per_page=5" \
  | pretty '.data.conferences[] | {short_name, submission_date}'

step 'Ranking list: lowest acceptance rate'
curl -s "$BASE/api/conferences/rankings/most_competitive?per_page=5" \
  | pretty '.data.conferences[] | {short_name, full_name}'

step 'Journals with the highest impact factor'
curl -s "$BASE/api/journals/rankings/highest_if?per_page=5" \
  | pretty '.data.journals[] | {short_name, impact_factor}'

step 'Site statistics'
curl -s "$BASE/api/statistics" | pretty '.data | keys'

step 'Incremental sync: what changed in the last week'
curl -s "$BASE/api/conferences?updated_since=$(date -d '-7 days' +%F 2>/dev/null || date -v-7d +%F)&per_page=5" \
  | pretty '.data | {changed: .pagination.total, sample: [.conferences[] | {short_name, updated_at}]}'

step 'Quota headroom (headers are on every response)'
curl -s -o /dev/null -D - "$BASE/api/statistics" | grep -i '^x-quota'

step 'MCP: list the tools'
curl -s "$BASE/mcp" -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}' \
  | pretty '.result.tools[] | .name'

step 'MCP: call one anonymously'
curl -s "$BASE/mcp" -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"search_conferences","arguments":{"ccf_rank":"A","field":"vision","per_page":3}}}' \
  | pretty '.result.structuredContent.conferences[] | {short_name, submission_date}'

step 'Detail endpoint WITHOUT a credential — 401 is the expected answer'
curl -s -w '\nHTTP %{http_code}\n' "$BASE/api/conferences/411" | pretty '.message // .'

if [ -n "$KEY" ]; then
  step 'Detail endpoint WITH a credential'
  curl -s "$BASE/api/conferences/411" -H "Authorization: Bearer $KEY" \
    | pretty '.data | {short_name, acceptance_rates, website}'
else
  printf '\nSet HUIBAN_API_KEY to see the detail endpoint succeed.\n'
  printf 'Create one at %s/account/api-keys\n' "$BASE"
fi
