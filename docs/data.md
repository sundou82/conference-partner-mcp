# The dataset

## What is in it

**Conferences** — short and full name, submission / notification / conference dates,
location, CCF / CORE / QUALIS ranks, whether the deadline has been extended, acceptance
rate history, edition history, CFP text, community ratings and comments, related venues.

**Journals** — name, ISSN, publisher, impact factor, CCF rank, special-issue calls for
papers, ratings, comments, related venues.

**Researchers** — public profiles only, by id: name, institution, an auto-generated
research-interest summary, CV, tracked and attended venues. Never contact details, and
there is deliberately no search or enumeration over researchers.

Coverage is strongest in computer science, where the three ranking systems apply. Venues
outside CS are present but carry no ranks.

The full account of where each field comes from, how conflicts are resolved and what is
known to be incomplete is at
[myhuiban.com/methodology](https://www.myhuiban.com/methodology). It is worth reading
before you build anything that depends on a date being right.

## How it is maintained

Dates are entered and corrected by maintainers, and increasingly by organisers themselves
through a venue-claim process on the site. Automated scans flag venues whose next edition
appears to have opened, but nothing is written from a scrape without review. Rankings are
reproduced from CCF, CORE and QUALIS — Conference Partner is not the authority for those
values and does not compute a ranking of its own.

## Why there is no dataset file in this repository

The obvious thing to put in a repo like this is a `deadlines.json` refreshed nightly by
CI. It is deliberately absent.

A committed snapshot is stale between commits and silently wrong at the moment it matters
most — deadline season, when extensions land daily. Worse, it teaches consumers to depend
on a file that is a copy of the thing that is actually maintained, and every bug report
then starts with "which commit was your data from".

So instead of shipping a snapshot,
[`../examples/python/export_deadlines.py`](../examples/python/export_deadlines.py)
*generates* one for you from the live API, in JSON, CSV and Markdown. Run it in your own
CI on whatever cadence you need; what you get is current as of the run. Anonymous access
covers it — no key required.

If you want a continuously-updated mirror rather than periodic snapshots, use
`updated_since` — see [Incremental sync](rest-api.md#incremental-sync).

## Using the data

Free to use, including commercially, with attribution.

Attribute as: the canonical venue URL (`https://www.myhuiban.com/conference/<id>`, which
is what every API response returns as `detail_page`) plus the name
**Conference Partner (myhuiban.com)**.

If the claim you are making is about a *ranking value itself* — "X is CCF-A" — cite CCF,
CORE or QUALIS. Conference Partner reproduces those lists; it does not define them.

The MIT license on this repository covers the code and configuration in it, not the data
served by the API.

## Corrections

Wrong date, dead link, missing venue: use the report link on the venue's page, or email
`admin@myhuiban.com`. Corrections to the data are not accepted as pull requests here —
this repository holds no data to correct.

Organisers can claim a venue from its page and then edit deadlines and CFP text directly.
