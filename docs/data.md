# The dataset

## What is in it

**Conferences** — short and full name, submission / notification / conference dates,
location, CCF / CORE / QUALIS ranks, the Conference Partner Index (`cp_index`), whether
the deadline has been extended, acceptance
rate history, edition history, CFP text, community ratings and comments, related venues.

**Journals** — name, ISSN, publisher, impact factor, CCF rank, special-issue calls for
papers, ratings, comments, related venues.

**Researchers** — public profiles only, by id: name, institution, an auto-generated
research-interest summary, CV, tracked and attended venues. Never contact details, and
there is deliberately no search or enumeration over researchers.

Coverage is strongest in computer science, where the three ranking systems apply. Venues
outside CS are present but carry no CCF / CORE / QUALIS rank — `cp_index` is computed for
them all the same, which is most of why it exists.

The full account of where each field comes from, how conflicts are resolved and what is
known to be incomplete is at
[myhuiban.com/methodology](https://www.myhuiban.com/methodology). It is worth reading
before you build anything that depends on a date being right.

## How it is maintained

Dates are entered and corrected by maintainers, and increasingly by organisers themselves
through a venue-claim process on the site. Automated scans flag venues whose next edition
appears to have opened, but nothing is written from a scrape without review. CCF, CORE
and QUALIS values are reproduced as published — Conference Partner is not the authority
for them and does not adjust them.

One index is ours: the **Conference Partner Index** (`cp_index`), a 0–100 score
recomputed nightly from academic recognition, selectivity, longevity, community and how
much a venue publishes about itself. It exists because those three lists between them
cover about a fifth of the catalogue and say nothing at all about the rest. Every value
carries a `confidence` and the `algorithm` version that produced it, and a missing input
scores as a neutral 50 rather than a zero — so a middling score on a thinly documented
venue reflects what we do not know about it, not a verdict on it. The factors, weights
and their limits are at [myhuiban.com/ranking](https://www.myhuiban.com/ranking).

## The snapshot in `data/`

[`data/`](../data/) holds a downloadable copy, refreshed daily by CI: upcoming submission
deadlines, the CCF / CORE / QUALIS conference catalogues, CCF journals, open
special-issue calls, and journals by impact factor. Each dataset is published as JSON and
CSV, with a browsable Markdown index.

CI commits only when something changed, so `git log -- data/` is a deadline-change log and
[`data.atom`](https://github.com/sundou82/conference-partner-mcp/commits/main/data.atom)
is a feed of it.

**What is in it is exactly what the anonymous tier already serves** — deadline searches
and ranking lists, the same rows anyone can fetch without credentials and the same rows
the website and sitemap publish. Exporting them costs nothing that is not already public.

**What is not in it**, and should not be added: per-venue detail — CFP full text,
acceptance-rate history, edition history, ratings and comments, and the organiser's own
website URL. Those need a free credential by design. The scope rule lives in a comment at
the top of [`../scripts/build_snapshot.py`](../scripts/build_snapshot.py); a dataset may
only be added there if its endpoint is on the server's anonymous whitelist.

### Prefer the API when it has to be right

A snapshot is stale the moment a deadline is extended, which in submission season is
daily. The files in `data/` are a convenience for browsing, diffing and bulk loading —
not a substitute for asking. For anything time-sensitive, call the API; it needs no key
for exactly this data.

Two ways to stay current:

- [`../examples/python/export_deadlines.py`](../examples/python/export_deadlines.py)
  generates a snapshot in your own filters and cadence.
- `updated_since` gives you a diff instead of a re-crawl — see
  [Incremental sync](rest-api.md#incremental-sync).

## Using the data

Free to use, including commercially, with attribution.

Attribute as: the canonical venue URL (`https://www.myhuiban.com/conference/<id>`, which
is what every API response returns as `detail_page`) plus the name
**Conference Partner (myhuiban.com)**.

If the claim you are making is about a *ranking value itself* — "X is CCF-A" — cite CCF,
CORE or QUALIS. Conference Partner reproduces those lists; it does not define them.
`cp_index` is the exception, since it is computed here: cite
[myhuiban.com/ranking](https://www.myhuiban.com/ranking) and the `algorithm` version on
the row, and keep the score with its `rank` or `confidence` — a bare number out of 100
reads as more authoritative than the method supports.

Two limits, matching the
[terms on the site](https://www.myhuiban.com/developers): keep crawls to one request per
second or slower, and if you need the dataset in bulk take `data/` here rather than
scraping your own copy. For anything wider — dataset licensing, model training —
ask first at `admin@myhuiban.com`.

The MIT license on this repository covers the code and configuration in it, not the data
served by the API.

## Corrections

Wrong date, dead link, missing venue: use the report link on the venue's page, or email
`admin@myhuiban.com`. Corrections to the data are not accepted as pull requests here —
this repository holds no data to correct.

Organisers can claim a venue from its page and then edit deadlines and CFP text directly.
