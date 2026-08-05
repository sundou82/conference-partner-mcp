# Conference Deadline Watch

A GitHub Action that keeps one issue in your repo up to date with the paper
deadlines you can still submit to.

No API key, no account, nothing to host. It reads the endpoints
[Conference Partner](https://www.myhuiban.com) serves to anonymous callers.

## Use it

`.github/workflows/deadlines.yml`:

```yaml
name: Deadline watch
on:
  schedule:
    - cron: '0 7 * * 1'      # every Monday morning
  workflow_dispatch:

permissions:
  issues: write

jobs:
  watch:
    runs-on: ubuntu-latest
    steps:
      - uses: sundou82/conference-partner-mcp/actions/deadline-watch@main
        with:
          field: security
          days: 120
          issue-title: 'Upcoming deadlines — security'
```

The first run opens the issue. Every run after that **edits the same issue**, so
it stays a live board instead of turning into a notification feed.

## Inputs

| Input | Default | Notes |
|---|---|---|
| `field` | *(all)* | `ai` `vision` `nlp` `data` `network` `security` `se` `systems` `theory` `hci` `graphics` `bio` `robotics` `web` |
| `ccf` | — | keep only this CCF rank: `A` `B` `C` |
| `core` | — | keep only this CORE rank: `A*` `A` `B` `C` |
| `days` | `90` | how far ahead to look |
| `ranked-only` | `false` | drop venues with no ranking at all |
| `issue-title` | `Upcoming paper deadlines` | the issue kept in sync |
| `labels` | — | applied when the issue is first created |
| `api-key` | — | optional, see [Rate limits](#rate-limits) |

Outputs: `count` and `soonest`, so you can branch on them — post to Slack only
when something is close, for instance.

## A result worth expecting

Combining a field with a top rank often returns **nothing**, and that is usually
correct rather than broken. Ranked venues open their calls in bursts: at the time
of writing, 115 AI conferences have a deadline inside the next 180 days and
exactly one of them carries any CCF rank, because NeurIPS/ICML/AAAI are between
cycles.

The action says so explicitly instead of rendering a bare empty table. If you
want a board that is never empty, start without `ccf`/`core` and add
`ranked-only: true` if the noise bothers you.

## Rate limits

The anonymous tier allows 50 requests per day **per source IP**, and GitHub's
hosted runners share addresses with everyone else. One run costs one request per
100 results — a weekly schedule is comfortably inside the limit; hourly is not.

If you hit `429`, create a free key at
[myhuiban.com/account/api-keys](https://www.myhuiban.com/account/api-keys), add
it as a repository secret, and pass it:

```yaml
        with:
          api-key: ${{ secrets.HUIBAN_API_KEY }}
```

That moves you to an account quota of 200/day. The action tells you this in its
failure message too, so you do not have to come back here.

## Attribution

Data from Conference Partner (myhuiban.com); the rendered issue links every
venue to its page there. Ranking values are reproduced from CCF, CORE and
QUALIS — cite those bodies for the rankings themselves. Deadlines move; check
the venue page before relying on one.
