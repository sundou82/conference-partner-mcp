# Data snapshot

Generated **2026-10-23T10:28:03+00:00** from the [Conference Partner API](https://www.myhuiban.com/developers). Refreshed daily by [CI](../.github/workflows/snapshot.yml).

Every file here comes from the API's **anonymous tier** — the same rows anyone can fetch without credentials. Per-venue detail (CFP full text, acceptance-rate history, edition history, ratings, the organiser's own website URL) is not included; it needs a free credential and lives behind the API. See [../docs/data.md](../docs/data.md).

## Files

| Dataset | Rows | JSON | CSV |
|---|---|---|---|
| **Upcoming submission deadlines**<br><sub>Every conference whose submission deadline has not passed, soonest first.</sub> | 912 | [upcoming-deadlines.json](upcoming-deadlines.json) | [upcoming-deadlines.csv](upcoming-deadlines.csv) |
| **CCF-ranked conferences**<br><sub>Every conference carrying a CCF rank, whether or not a call is open. CORE and QUALIS ranks are on the same row where the venue has them.</sub> | 388 | [ccf-conferences.json](ccf-conferences.json) | [ccf-conferences.csv](ccf-conferences.csv) |
| **CORE-ranked conferences**<br><sub>Every conference carrying a CORE rank, whether or not a call is open.</sub> | 733 | [core-conferences.json](core-conferences.json) | [core-conferences.csv](core-conferences.csv) |
| **QUALIS-ranked conferences**<br><sub>Every conference carrying a QUALIS rank (A1 through B5), whether or not a call is open.</sub> | 705 | [qualis-conferences.json](qualis-conferences.json) | [qualis-conferences.csv](qualis-conferences.csv) |
| **Ranked conferences with a call open now**<br><sub>The subset of the catalogues you can still submit to today — CCF, CORE and QUALIS lists merged.</sub> | 177 | [open-calls-by-rank.json](open-calls-by-rank.json) | [open-calls-by-rank.csv](open-calls-by-rank.csv) |
| **CCF-ranked journals**<br><sub>Journals in the CCF catalogue, with impact factor, publisher and ISSN.</sub> | 292 | [ccf-journals.json](ccf-journals.json) | [ccf-journals.csv](ccf-journals.csv) |
| **Journals with an open special-issue call**<br><sub>Journals currently carrying a special-issue call for papers.</sub> | 76 | [journal-special-issues.json](journal-special-issues.json) | [journal-special-issues.csv](journal-special-issues.csv) |
| **Top journals by impact factor**<br><sub>The 300 highest reported impact factors. Figures are as published by the journal and may lag the latest JCR.</sub> | 296 | [top-impact-factor-journals.json](top-impact-factor-journals.json) | [top-impact-factor-journals.csv](top-impact-factor-journals.csv) |

Site totals on the day of generation: **5896** conferences, **1218** journals.

## Prefer live data

A snapshot is stale the moment a deadline is extended, which happens daily in submission season. For anything that has to be right, call the API — it needs no key for exactly the data in this directory:

```bash
curl "https://www.myhuiban.com/api/conferences?field=ai&submission_date_start=$(date +%F)"
```

Or mirror it incrementally with `updated_since` — see [../docs/rest-api.md](../docs/rest-api.md#incremental-sync).

## Deadlines in the next 90 days (487)

| Deadline | Conference | CCF | CORE | QUALIS | Held | Location |
|---|---|---|---|---|---|---|
| 2026-10-23 | [3EAI](https://www.myhuiban.com/conference/5852) | - | - | - | 2026-11-06 | Tumxuk, China |
| 2026-10-23 *(extended)* | [AIGC](https://www.myhuiban.com/conference/4601) | - | - | - | 2026-12-26 | Guangzhou, China |
| 2026-10-23 | [CHASE'](https://www.myhuiban.com/conference/4316) | - | B | - | 2027-04-26 | Dublin, Ireland |
| 2026-10-23 | [CVM](https://www.myhuiban.com/conference/2906) | C | - | - | 2027-04-09 | Singapore |
| 2026-10-23 | [DILSCM](https://www.myhuiban.com/conference/5885) | - | - | - | 2026-11-06 | Jiangmen, China |
| 2026-10-23 *(extended)* | [FG](https://www.myhuiban.com/conference/515) | C | B | A1 | 2027-04-26 | Marrakesh, Morocco |
| 2026-10-24 *(extended)* | [ACITY](https://www.myhuiban.com/conference/1363) | - | - | - | 2026-11-27 | Zurich, Switzerland |
| 2026-10-24 *(extended)* | [AI'](https://www.myhuiban.com/conference/3462) | - | - | - | 2026-12-26 | Dubai, UAE |
| 2026-10-24 | [ARIN](https://www.myhuiban.com/conference/3619) | - | - | - | 2027-01-30 | Copenhagen, Denmark |
| 2026-10-24 *(extended)* | [CCSIT](https://www.myhuiban.com/conference/1108) | - | - | - | 2026-11-21 | London, UK |
| 2026-10-24 | [CONEDU](https://www.myhuiban.com/conference/4052) | - | - | - | 2027-01-30 | Copenhagen, Denmark |
| 2026-10-24 *(extended)* | [CSEA'](https://www.myhuiban.com/conference/3872) | - | - | - | 2026-12-19 | Sydney, Australia |
| 2026-10-24 | [CSITA](https://www.myhuiban.com/conference/3621) | - | - | - | 2027-01-30 | Copenhagen, Denmark |
| 2026-10-24 | [DMAP](https://www.myhuiban.com/conference/3623) | - | - | - | 2027-01-30 | Copenhagen, Denmark |
| 2026-10-24 | [ISPR'](https://www.myhuiban.com/conference/3622) | - | - | - | 2027-01-30 | Copenhagen, Denmark |
| 2026-10-24 *(extended)* | [IWMEN](https://www.myhuiban.com/conference/5858) | - | - | - | 2026-11-21 | London, UK |
| 2026-10-24 *(extended)* | [IoTE](https://www.myhuiban.com/conference/3883) | - | - | - | 2026-11-27 | Zurich, Switzerland |
| 2026-10-24 | [MLCL](https://www.myhuiban.com/conference/3627) | - | - | - | 2027-01-30 | Copenhagen, Denmark |
| 2026-10-24 *(extended)* | [MLTEC](https://www.myhuiban.com/conference/4070) | - | - | - | 2026-12-19 | Sydney, Australia |
| 2026-10-24 | [NATAP](https://www.myhuiban.com/conference/3749) | - | - | - | 2027-01-30 | Copenhagen, Denmark |
| 2026-10-24 | [NBIoT](https://www.myhuiban.com/conference/3626) | - | - | - | 2027-01-30 | Copenhagen, Denmark |
| 2026-10-24 *(extended)* | [NLAICSE](https://www.myhuiban.com/conference/5874) | - | - | - | 2026-12-30 | Online |
| 2026-10-24 *(extended)* | [NLAII](https://www.myhuiban.com/conference/5859) | - | - | - | 2026-10-30 | Online |
| 2026-10-24 | [NMCO](https://www.myhuiban.com/conference/3617) | - | - | - | 2027-01-30 | Copenhagen, Denmark |
| 2026-10-24 | [SOFTPA](https://www.myhuiban.com/conference/4258) | - | - | - | 2027-01-30 | Copenhagen, Denmark |
| 2026-10-24 | [TRUST](https://www.myhuiban.com/conference/5744) | - | - | - | 2027-03-07 | Washington DC, USA |
| 2026-10-25 | [ARC](https://www.myhuiban.com/conference/1803) | - | - | - | 2027-03-31 | Berlin, Germany |
| 2026-10-25 *(extended)* | [BLKCA](https://www.myhuiban.com/conference/5903) | - | - | - | 2026-12-29 | Online |
| 2026-10-25 | [CTCNet](https://www.myhuiban.com/conference/4788) | - | - | - | 2026-12-25 | Xiamen, China |
| 2026-10-25 | [FORGE](https://www.myhuiban.com/conference/5210) | - | - | - | 2027-04-26 | Dublin, Ireland |
| 2026-10-25 *(extended)* | [ICCNS](https://www.myhuiban.com/conference/1093) | - | - | - | 2026-12-19 | Harbin, China |
| 2026-10-25 *(extended)* | [ICCR](https://www.myhuiban.com/conference/4872) | - | - | - | 2026-12-11 | Tokyo, Japan |
| 2026-10-25 *(extended)* | [ICMLC](https://www.myhuiban.com/conference/1375) | - | - | B4 | 2027-02-26 | Shenzhen, China |
| 2026-10-25 | [ICPRS](https://www.myhuiban.com/conference/1821) | - | - | - | 2027-03-08 | Talence, France |
| 2026-10-25 *(extended)* | [ICVIP](https://www.myhuiban.com/conference/2756) | - | - | - | 2026-12-11 | Shanghai, China |
| 2026-10-25 *(extended)* | [ICVRT](https://www.myhuiban.com/conference/3056) | - | - | - | 2026-12-25 | Harbin, China |
| 2026-10-25 *(extended)* | [MCVR](https://www.myhuiban.com/conference/4884) | - | - | - | 2026-12-25 | Harbin, China |
| 2026-10-26 | [EIC'](https://www.myhuiban.com/conference/5968) | - | - | - | 2027-06-06 | Kitchener, Ontario, Canada |
| 2026-10-26 | [EuroSimE](https://www.myhuiban.com/conference/5904) | - | - | - | 2027-04-11 | Regensburg, Germany |
| 2026-10-26 *(extended)* | [ICIT](https://www.myhuiban.com/conference/743) | - | - | B3 | 2027-03-17 | Florianopolis, Brazil |
| 2026-10-26 | [ISBI](https://www.myhuiban.com/conference/479) | - | - | B1 | 2027-05-25 | Lausanne, Switzerland |
| 2026-10-27 | [FAT*](https://www.myhuiban.com/conference/2367) | - | - | - | 2027-06-21 | Porto, Portugal |
| 2026-10-27 | [FAccT](https://www.myhuiban.com/conference/5000) | - | - | - | 2027-06-21 | Porto, Portugal |
| 2026-10-28 | [AROB](https://www.myhuiban.com/conference/5718) | - | C | - | 2027-01-19 | Beppu, Japan |
| 2026-10-28 | [RECOMB](https://www.myhuiban.com/conference/477) | B | B | A2 | 2027-05-17 | Toronto, Ontario, Canada |
| 2026-10-29 | [HSCC+ICCPS](https://www.myhuiban.com/conference/5895) | - | - | - | 2027-05-17 | Boulder, Colorado, USA |
| 2026-10-29 | [ICIPCN](https://www.myhuiban.com/conference/5784) | - | - | - | 2027-01-21 | Tamil Nadu, India |
| 2026-10-29 | [ICPECA](https://www.myhuiban.com/conference/5798) | - | - | - | 2027-01-29 | Shenyang, China |
| 2026-10-29 | [IDCIoT](https://www.myhuiban.com/conference/4974) | - | - | - | 2027-01-21 | Ottapalam, Kerala, India |
| 2026-10-29 | [SenSys](https://www.myhuiban.com/conference/61) | B | - | A1 | 2027-05-17 | Boulder, Colorado, USA |
| 2026-10-30 | [AEEES](https://www.myhuiban.com/conference/3920) | - | - | - | 2027-03-19 | Chengdu, China |
| 2026-10-30 *(extended)* | [AIAT](https://www.myhuiban.com/conference/4951) | - | - | - | 2026-12-11 | Tokyo, Japan |
| 2026-10-30 *(extended)* | [AIBDCC](https://www.myhuiban.com/conference/5505) | - | - | - | 2026-10-30 | Chengdu, China |
| 2026-10-30 *(extended)* | [AIBT](https://www.myhuiban.com/conference/3656) | - | - | - | 2026-11-27 | Shanghai, China |
| 2026-10-30 | [AISNS](https://www.myhuiban.com/conference/5135) | - | - | - | 2026-11-13 | Chongqing, China |
| 2026-10-30 *(extended)* | [AMEM](https://www.myhuiban.com/conference/5574) | - | - | - | 2026-12-11 | Wuhan, China |
| 2026-10-30 *(extended)* | [ASIG](https://www.myhuiban.com/conference/4883) | - | - | - | 2026-12-04 | Kyoto, Japan |
| 2026-10-30 | [AST](https://www.myhuiban.com/conference/5208) | - | C | - | 2027-04-26 | Dublin, Ireland |
| 2026-10-30 | [CAIN](https://www.myhuiban.com/conference/5209) | - | B | - | 2027-04-25 | Dublin, Ireland |
| 2026-10-30 | [FormaliSE](https://www.myhuiban.com/conference/3047) | - | - | - | 2027-04-26 | Dublin, Ireland |
| 2026-10-30 *(extended)* | [ICAIP](https://www.myhuiban.com/conference/2494) | - | - | - | 2026-11-27 | Shanghai, China |
| 2026-10-30 | [ICAIRC](https://www.myhuiban.com/conference/4460) | - | - | - | 2026-11-13 | Xiamen, China |
| 2026-10-30 *(extended)* | [ICBBE](https://www.myhuiban.com/conference/4077) | - | - | - | 2026-12-25 | Hokkaido, Japan |
| 2026-10-30 | [ICCECE'](https://www.myhuiban.com/conference/3965) | - | - | - | 2027-01-15 | Xiangtan, China |
| 2026-10-30 | [ICESD](https://www.myhuiban.com/conference/3440) | - | - | - | 2027-03-28 | Tokyo, Japan |
| 2026-10-30 *(extended)* | [ICETC](https://www.myhuiban.com/conference/1574) | - | - | B4 | 2026-12-14 | Porto, Portugal |
| 2026-10-30 | [ICICT''](https://www.myhuiban.com/conference/2785) | - | - | - | 2027-03-10 | Honolulu, Hawaii, USA |
| 2026-10-30 | [ICIM](https://www.myhuiban.com/conference/2376) | - | - | - | 2027-03-19 | Cambridge, UK |
| 2026-10-30 | [ICIN](https://www.myhuiban.com/conference/1578) | - | - | - | 2027-03-15 | Pisa, Italy |
| 2026-10-30 *(extended)* | [ICIT''](https://www.myhuiban.com/conference/2996) | - | - | - | 2026-12-11 | Shanghai, China |
| 2026-10-30 | [ICLIST](https://www.myhuiban.com/conference/5825) | - | - | - | 2027-03-18 | Bangkok, Thailand |
| 2026-10-30 *(extended)* | [ICNCC](https://www.myhuiban.com/conference/2949) | - | - | - | 2026-12-10 | Kuala Lumper, Malaysia |
| 2026-10-30 | [ICSA](https://www.myhuiban.com/conference/176) | C | A | B1 | 2027-03-08 | Sydney, Australia |
| 2026-10-30 | [IDIM](https://www.myhuiban.com/conference/5799) | - | - | - | 2027-01-30 | Bali, Indonesia |
| 2026-10-30 | [IQIM](https://www.myhuiban.com/conference/5915) | - | - | - | 2027-10-04 | Taichung, Taiwan |
| 2026-10-30 | [ISRAI](https://www.myhuiban.com/conference/5184) | - | - | - | 2026-12-18 | Changchun, China |
| 2026-10-30 | [ITNG](https://www.myhuiban.com/conference/1654) | - | - | - | 2027-04-11 | Las Vegas, Nevada, USA |
| 2026-10-30 | [IWEG](https://www.myhuiban.com/conference/3168) | - | - | - | 2026-11-22 | Shanghai, China |
| 2026-10-30 *(extended)* | [MLPR](https://www.myhuiban.com/conference/4998) | - | - | - | 2026-12-04 | Kyoto, Japan |
| 2026-10-30 *(extended)* | [NLPIR](https://www.myhuiban.com/conference/3024) | - | - | - | 2026-12-11 | Nara, Japan |
| 2026-10-30 | [PAM](https://www.myhuiban.com/conference/925) | C | B | A2 | 2027-03-22 | Online |
| 2026-10-30 *(extended)* | [PEESE](https://www.myhuiban.com/conference/5506) | - | - | - | 2026-10-31 | Chengdu, China |
| 2026-10-31 | [ADNTIIC](https://www.myhuiban.com/conference/1810) | - | - | - | 2026-11-17 | Montevideo, Uruguay |
| 2026-10-31 *(extended)* | [AI3T](https://www.myhuiban.com/conference/5896) | - | - | - | 2026-12-13 | Hefei, China |
| 2026-10-31 | [AICARE](https://www.myhuiban.com/conference/5820) | - | - | - | 2027-03-06 | Kolkata, India |
| 2026-10-31 | [AISCA](https://www.myhuiban.com/conference/3800) | - | - | - | 2027-01-23 | Zurich, Switzerland |
| 2026-10-31 *(extended)* | [AISS''](https://www.myhuiban.com/conference/5898) | - | - | - | 2026-12-13 | Hefei, China |
| 2026-10-31 | [CCDC](https://www.myhuiban.com/conference/5906) | - | - | - | 2027-05-14 | Changsha, China |
| 2026-10-31 *(extended)* | [CCEI](https://www.myhuiban.com/conference/5900) | - | - | - | 2026-12-13 | Hefei, China |
| 2026-10-31 *(extended)* | [COAC](https://www.myhuiban.com/conference/5899) | - | - | - | 2026-12-13 | Hefei, China |
| 2026-10-31 | [ECC](https://www.myhuiban.com/conference/3409) | - | - | - | 2027-07-13 | Brussels, Belgium |
| 2026-10-31 | [ESIHISE](https://www.myhuiban.com/conference/1940) | - | - | - | 2026-11-19 | Montevideo, Uruguay |
| 2026-10-31 | [HCITISI](https://www.myhuiban.com/conference/1809) | - | - | - | 2026-11-26 | Cordoba, Argentina |
| 2026-10-31 *(extended)* | [IEEE CRESS](https://www.myhuiban.com/conference/5187) | - | - | - | 2026-12-04 | Nanjing, China |
| 2026-10-31 | [L&T](https://www.myhuiban.com/conference/4965) | - | - | - | 2027-02-01 | Jeddah, Saudi Arabia |
| 2026-10-31 | [MLIOB](https://www.myhuiban.com/conference/3887) | - | - | - | 2027-01-23 | Zurich, Switzerland |
| 2026-10-31 *(extended)* | [NPSPE](https://www.myhuiban.com/conference/5575) | - | - | - | 2026-12-25 | Harbin, China |
| 2026-10-31 | [RadarConf](https://www.myhuiban.com/conference/2080) | - | - | - | 2027-05-01 | Bangalore, India |
| 2026-10-31 | [SAFEPROCESS](https://www.myhuiban.com/conference/5628) | - | C | - | 2027-06-29 | Delft, the Netherlands |
| 2026-10-31 | [SIPO](https://www.myhuiban.com/conference/3797) | - | - | - | 2027-01-23 | Zurich, Switzerland |
| 2026-10-31 | [SIROCCO](https://www.myhuiban.com/conference/996) | - | B | B2 | 2027-06-02 | Larnaca, Cyprus |
| 2026-11-01 | [CEES](https://www.myhuiban.com/conference/2576) | - | - | - | 2027-04-28 | Osaka, Japan |
| 2026-11-01 | [CSPA](https://www.myhuiban.com/conference/2070) | - | - | - | 2027-04-16 | Kuala Lumpur, Malaysia |
| 2026-11-01 | [EuroGP](https://www.myhuiban.com/conference/1598) | - | B | B1 | 2027-07-31 | Mainz, Germany |
| 2026-11-01 | [EvoApplications](https://www.myhuiban.com/conference/5202) | - | B | - | 2027-03-31 | Mainz, Germany |
| 2026-11-01 | [EvoCOP](https://www.myhuiban.com/conference/1349) | - | B | B2 | 2027-03-31 | Mainz, Germany |
| 2026-11-01 | [EvoLearn](https://www.myhuiban.com/conference/5853) | - | - | - | 2027-03-31 | Mainz, Germany |
| 2026-11-01 | [EvoMUSART](https://www.myhuiban.com/conference/3416) | - | C | - | 2027-03-31 | Mainz, Germany |
| 2026-11-01 | [HOST](https://www.myhuiban.com/conference/2370) | - | - | - | 2027-05-03 | Washington DC, USA |
| 2026-11-01 *(extended)* | [ICACT](https://www.myhuiban.com/conference/1682) | - | - | - | 2027-01-24 | Phoenix Park, PyeongChang, Korea |
| 2026-11-01 | [ICMET](https://www.myhuiban.com/conference/2577) | - | - | - | 2027-04-28 | Osaka, Japan |
| 2026-11-01 | [ICMTS](https://www.myhuiban.com/conference/5831) | - | - | - | 2027-04-05 | Udine, Italy |
| 2026-11-01 | [ICRMV](https://www.myhuiban.com/conference/2565) | - | - | - | 2027-03-19 | Haining, China |
| 2026-11-01 | [IMA](https://www.myhuiban.com/conference/3249) | - | - | - | 2027-01-15 | Sanya, China |
| 2026-11-01 | [ISCAIT](https://www.myhuiban.com/conference/5148) | - | - | - | 2027-01-15 | Chengdu, China |
| 2026-11-01 | [PMAE](https://www.myhuiban.com/conference/4798) | - | - | - | 2026-12-18 | Singapore |
| 2026-11-02 | [ACE](https://www.myhuiban.com/conference/503) | - | B | B2 | 2027-02-01 | Canberra, Australia |
| 2026-11-02 *(extended)* | [AMA21](https://www.myhuiban.com/conference/3560) | - | - | - | 2026-12-16 | Online |
| 2026-11-02 | [ICM](https://www.myhuiban.com/conference/467) | - | - | - | 2027-03-07 | Yokohama, Japan |
| 2026-11-02 | [ICST](https://www.myhuiban.com/conference/934) | C | A | B2 | 2027-05-17 | San Sebastian, Spain |
| 2026-11-02 | [STOC](https://www.myhuiban.com/conference/359) | A | A* | A1 | 2027-06-06 | Atlanta, Georgia, USA |
| 2026-11-03 | [HNNDL](https://www.myhuiban.com/conference/5216) | - | - | - | 2027-01-22 | Qingdao, China |
| 2026-11-04 | [CAiSE](https://www.myhuiban.com/conference/191) | B | A | A2 | 2027-06-07 | Seville, Spain |
| 2026-11-04 | [ISoIRS](https://www.myhuiban.com/conference/3387) | - | - | - | 2027-04-16 | Shenzhen, China |
| 2026-11-05 *(extended)* | [AIES'](https://www.myhuiban.com/conference/5881) | - | - | - | 2026-12-18 | Kunming, China |
| 2026-11-05 | [AITC'](https://www.myhuiban.com/conference/4890) | - | - | - | 2026-11-20 | Hangzhou, China |
| 2026-11-05 *(extended)* | [CCAT](https://www.myhuiban.com/conference/4879) | - | - | - | 2026-12-18 | Fukuoka, Japan |
| 2026-11-05 | [CSTE](https://www.myhuiban.com/conference/4933) | - | - | - | 2027-04-09 | Wuhan, China |
| 2026-11-05 *(extended)* | [GBSCE](https://www.myhuiban.com/conference/5528) | - | - | - | 2026-12-06 | Sydney, Australia |
| 2026-11-05 *(extended)* | [ICAITE](https://www.myhuiban.com/conference/4860) | - | - | - | 2026-12-06 | Nagasaki, Japan |
| 2026-11-05 | [ICBCT](https://www.myhuiban.com/conference/3576) | - | - | - | 2027-03-27 | Sapporo, Japan |
| 2026-11-05 | [ICCGV](https://www.myhuiban.com/conference/4906) | - | - | - | 2027-03-27 | Sapporo, Japan |
| 2026-11-05 | [ICEIT](https://www.myhuiban.com/conference/1391) | - | - | B5 | 2027-03-26 | Chongqing, China |
| 2026-11-05 | [ICFEE](https://www.myhuiban.com/conference/3397) | - | - | - | 2027-03-26 | Kyoto, Japan |
| 2026-11-05 | [ICPC](https://www.myhuiban.com/conference/573) | B | A | A2 | 2027-04-25 | Dublin, Ireland |
| 2026-11-05 *(extended)* | [ICRAI](https://www.myhuiban.com/conference/1975) | - | - | - | 2026-12-18 | Songdo, Incheon, Korea |
| 2026-11-05 | [IS-AII](https://www.myhuiban.com/conference/4994) | - | - | - | 2027-01-09 | to be updated |
| 2026-11-05 | [ISPR](https://www.myhuiban.com/conference/3561) | - | - | - | 2026-12-20 | Istanbul, Turkey |
| 2026-11-05 | [REFSQ](https://www.myhuiban.com/conference/1850) | C | B | - | 2027-04-12 | Basel, Switzerland |
| 2026-11-05 | [RTAS](https://www.myhuiban.com/conference/349) | B | A | A2 | 2027-05-11 | New York City, New York, USA |
| 2026-11-06 *(extended)* | [AHPCAI](https://www.myhuiban.com/conference/4607) | - | - | - | 2026-11-20 | Zhengzhou, China |
| 2026-11-06 | [BDICN](https://www.myhuiban.com/conference/4254) | - | - | - | 2027-01-15 | Beijing, China |
| 2026-11-06 | [CCWC](https://www.myhuiban.com/conference/2511) | - | - | - | 2027-01-04 | Las Vegas, Nevada, USA |
| 2026-11-06 | [ICGHIT](https://www.myhuiban.com/conference/3037) | - | - | - | 2027-01-20 | Jakarta, Indonesia |
| 2026-11-06 | [ICMLCA](https://www.myhuiban.com/conference/3786) | - | - | - | 2026-11-20 | Hangzhou, China |
| 2026-11-06 | [ICPHDS](https://www.myhuiban.com/conference/3847) | - | - | - | 2026-11-20 | Dalian, China |
| 2026-11-06 | [SMAP](https://www.myhuiban.com/conference/5782) | - | - | - | 2027-01-20 | Jakarta, Indonesia |
| 2026-11-07 | [AMNA](https://www.myhuiban.com/conference/4285) | - | - | - | 2027-01-22 | Tianjin, China |
| 2026-11-07 *(extended)* | [ICAPE](https://www.myhuiban.com/conference/5068) | - | - | - | 2026-12-04 | Xi an, China |
| 2026-11-08 | [ICTEC](https://www.myhuiban.com/conference/5250) | - | - | - | 2027-01-15 | Nanjing, China |
| 2026-11-08 | [JCICE](https://www.myhuiban.com/conference/2445) | - | - | - | 2027-05-14 | Chengdu, China |
| 2026-11-08 | [PacificVis](https://www.myhuiban.com/conference/286) | C | B | B3 | 2027-04-19 | Busan, South Korea |
| 2026-11-08 | [RPIC](https://www.myhuiban.com/conference/5792) | - | - | - | 2027-01-22 | Tokyo, Japan |
| 2026-11-09 | [ICAAIC](https://www.myhuiban.com/conference/5800) | - | - | - | 2027-02-01 | Salem, Tamil Nadu, India |
| 2026-11-09 | [ICEARS](https://www.myhuiban.com/conference/5809) | - | - | - | 2027-02-22 | Tuticorin, India |
| 2026-11-09 | [ICPE](https://www.myhuiban.com/conference/1537) | - | B | - | 2027-05-24 | Gothenburg, Sweden |
| 2026-11-09 | [ISCA](https://www.myhuiban.com/conference/319) | A | A* | A1 | 2027-06-05 | Atlanta, Georgia, USA |
| 2026-11-09 | [NOMS](https://www.myhuiban.com/conference/312) | - | B | A2 | 2027-05-10 | Montreal, Quebec, Canada |
| 2026-11-10 | [AAME](https://www.myhuiban.com/conference/2483) | - | - | - | 2027-03-26 | Ningbo, China |
| 2026-11-10 *(extended)* | [CSAI](https://www.myhuiban.com/conference/1972) | - | - | - | 2026-12-18 | Beijing, China |
| 2026-11-10 | [CVPR](https://www.myhuiban.com/conference/407) | A | A* | A1 | 2027-06-20 | Seattle, Washington, USA |
| 2026-11-10 *(extended)* | [DSIS](https://www.myhuiban.com/conference/2987) | - | - | - | 2026-11-20 | Hangzhou, China |
| 2026-11-10 | [FICMSS](https://www.myhuiban.com/conference/4701) | - | - | - | 2027-01-08 | Xi an, China |
| 2026-11-10 *(extended)* | [ICACS](https://www.myhuiban.com/conference/2491) | - | - | - | 2026-12-18 | Phuket, Thailand |
| 2026-11-10 | [ICAMAM](https://www.myhuiban.com/conference/5153) | - | - | - | 2027-01-22 | Tai an, China |
| 2026-11-10 | [ICAPM](https://www.myhuiban.com/conference/3400) | - | - | - | 2027-04-16 | Kyoto, Japan |
| 2026-11-10 | [ICCAI'](https://www.myhuiban.com/conference/3606) | - | - | - | 2027-04-23 | Seoul, South Korea |
| 2026-11-10 | [ICCCV](https://www.myhuiban.com/conference/4008) | - | - | - | 2027-04-02 | Tianjin, China |
| 2026-11-10 *(extended)* | [ICCDA'](https://www.myhuiban.com/conference/2897) | - | - | - | 2026-12-18 | Phuket, Thailand |
| 2026-11-10 | [ICDIP](https://www.myhuiban.com/conference/2082) | - | - | - | 2027-04-16 | Beijing, China |
| 2026-11-10 | [ICIET](https://www.myhuiban.com/conference/3544) | - | - | - | 2027-04-09 | Osaka, Japan |
| 2026-11-10 | [ICMENS](https://www.myhuiban.com/conference/5227) | - | - | - | 2027-03-28 | Osaka, Japan |
| 2026-11-10 *(extended)* | [ICMSR](https://www.myhuiban.com/conference/2901) | - | - | - | 2026-12-18 | Singapore |
| 2026-11-10 | [ICRCA](https://www.myhuiban.com/conference/4886) | - | - | - | 2027-03-26 | Aizuwakamatsu, Japan |
| 2026-11-10 | [IMIP](https://www.myhuiban.com/conference/5237) | - | - | - | 2027-04-23 | Seoul, South Korea |
| 2026-11-10 | [IPAS](https://www.myhuiban.com/conference/5711) | - | C | - | 2027-04-06 | Castellon de la Plana, Spain |
| 2026-11-10 | [IVEC](https://www.myhuiban.com/conference/5350) | - | - | - | 2027-03-15 | Bengaluru, India |
| 2026-11-10 | [PES GM](https://www.myhuiban.com/conference/5935) | - | - | - | 2027-07-25 | San Francisco, California, USA |
| 2026-11-10 *(extended)* | [PSETC](https://www.myhuiban.com/conference/5024) | - | - | - | 2026-11-13 | Singapore |
| 2026-11-10 | [RAITS](https://www.myhuiban.com/conference/5224) | - | - | - | 2027-01-22 | Xi an, China |
| 2026-11-10 | [S&P](https://www.myhuiban.com/conference/289) | A | A* | - | 2027-05-18 | Montreal, Canada |
| 2026-11-11 | [DAC](https://www.myhuiban.com/conference/549) | - | A* | A1 | 2027-07-11 | San Jose, California, USA |
| 2026-11-11 | [ICDE](https://www.myhuiban.com/conference/135) | A | A* | A1 | 2027-05-17 | Copenhagen, Denmark |
| 2026-11-12 | [DFDS](https://www.myhuiban.com/conference/5465) | - | - | - | 2027-03-30 | Edinburgh, UK |
| 2026-11-12 | [ICRFCS](https://www.myhuiban.com/conference/5804) | - | - | - | 2027-02-04 | Bengaluru, India |
| 2026-11-12 | [PLDI](https://www.myhuiban.com/conference/164) | A | A* | A1 | 2027-06-05 | Atlanta, Georgia, USA |
| 2026-11-13 | [ACC'](https://www.myhuiban.com/conference/5589) | - | C | - | 2026-12-07 | Melbourne, Australia |
| 2026-11-13 | [AGENT](https://www.myhuiban.com/conference/5212) | - | - | - | 2027-04-25 | Dublin, Ireland |
| 2026-11-13 | [CogSIMA](https://www.myhuiban.com/conference/2462) | - | - | - | 2027-06-01 | Veszprém, Hungary |
| 2026-11-13 *(extended)* | [ICEduTech](https://www.myhuiban.com/conference/3558) | - | - | - | 2027-03-13 | Porto, Portugal |
| 2026-11-13 | [ICM'''](https://www.myhuiban.com/conference/5945) | - | - | - | 2027-06-14 | San Juan, Puerto Rico, USA |
| 2026-11-13 *(extended)* | [IS'](https://www.myhuiban.com/conference/2964) | - | - | - | 2027-03-13 | Porto, Portugal |
| 2026-11-13 *(extended)* | [ML](https://www.myhuiban.com/conference/2972) | - | - | - | 2027-03-13 | Porto, Portugal |
| 2026-11-13 | [VTS](https://www.myhuiban.com/conference/1489) | C | - | A2 | 2027-04-26 | Napa, California, USA |
| 2026-11-13 *(extended)* | [e-Society](https://www.myhuiban.com/conference/2963) | - | - | - | 2027-03-13 | Porto, Portugal |
| 2026-11-14 | [ACMSE](https://www.myhuiban.com/conference/1412) | - | - | - | 2027-04-15 | Cape Girardeau, Missouri, USA |
| 2026-11-14 | [ECETES](https://www.myhuiban.com/conference/5819) | - | - | - | 2027-03-05 | Berlin, Germany |
| 2026-11-14 | [NNICE](https://www.myhuiban.com/conference/4515) | - | - | - | 2027-01-29 | Dongguan, China |
| 2026-11-15 | [AISC](https://www.myhuiban.com/conference/5586) | - | C | - | 2027-02-01 | Canberra, Australia |
| 2026-11-15 | [AusPDC](https://www.myhuiban.com/conference/5585) | - | C | - | 2027-02-01 | Canberra, Australia |
| 2026-11-15 | [CoMEA](https://www.myhuiban.com/conference/4758) | - | - | - | 2027-05-21 | Beijing, China |
| 2026-11-15 | [ICAISC](https://www.myhuiban.com/conference/3880) | - | - | - | 2027-06-20 | Zakopane, Poland |
| 2026-11-15 *(extended)* | [ICICSE'](https://www.myhuiban.com/conference/4014) | - | - | - | 2026-12-27 | Chongqing, China |
| 2026-11-15 | [ICMEN](https://www.myhuiban.com/conference/3085) | - | - | - | 2027-04-02 | Kyoto, Japan |
| 2026-11-15 | [ICRITO](https://www.myhuiban.com/conference/1929) | - | - | - | 2027-02-11 | Noida, India |
| 2026-11-15 | [ICSGPS](https://www.myhuiban.com/conference/4697) | - | - | - | 2027-01-15 | Gold Coast, Australia |
| 2026-11-15 | [IDEAS](https://www.myhuiban.com/conference/1666) | - | C | - | 2027-01-25 | Fukuoka, Japan |
| 2026-11-15 | [IEEE IV](https://www.myhuiban.com/conference/2135) | - | B | - | 2027-06-15 | Perth, Australia |
| 2026-11-15 | [ISNN](https://www.myhuiban.com/conference/2062) | - | C | - | 2027-05-09 | Hangzhou, China |
| 2026-11-15 | [ITCSREC](https://www.myhuiban.com/conference/5588) | - | - | - | 2027-02-01 | Canberra, Australia |
| 2026-11-15 | [PEED](https://www.myhuiban.com/conference/5576) | - | - | - | 2027-02-27 | Nanjing, China |
| 2026-11-15 | [Pan Pac](https://www.myhuiban.com/conference/5794) | - | - | - | 2027-01-25 | Maui, Hawaii, USA |
| 2026-11-15 | [TPEC](https://www.myhuiban.com/conference/4978) | - | - | - | 2027-02-07 | College Station, Texas, USA |
| 2026-11-15 | [WCCCT](https://www.myhuiban.com/conference/3451) | - | - | - | 2027-04-16 | Chengdu, China |
| 2026-11-16 | [CICC](https://www.myhuiban.com/conference/849) | - | - | B2 | 2027-04-18 | San Diego, California, USA |
| 2026-11-16 | [CODASPY](https://www.myhuiban.com/conference/1319) | C | - | B4 | 2027-06-14 | Fort Collins, Colorado, USA |
| 2026-11-16 *(extended)* | [ICOIP](https://www.myhuiban.com/conference/5674) | - | - | - | 2026-12-10 | Suzhou, China |
| 2026-11-17 | [CLOSER](https://www.myhuiban.com/conference/2911) | - | C | - | 2027-04-17 | Rome, Italy |
| 2026-11-17 | [CSEDU](https://www.myhuiban.com/conference/5600) | - | B | - | 2027-04-16 | Rome, Italy |
| 2026-11-17 | [ENASE](https://www.myhuiban.com/conference/254) | - | B | B4 | 2027-04-20 | Rome, Italy |
| 2026-11-17 | [FEMIB](https://www.myhuiban.com/conference/5614) | - | - | - | 2027-04-21 | Rome, Italy |
| 2026-11-17 | [GISTAM](https://www.myhuiban.com/conference/1570) | - | - | - | 2027-04-20 | Rome, Italy |
| 2026-11-17 | [ICEIS](https://www.myhuiban.com/conference/182) | - | - | B1 | 2027-04-20 | Rome, Italy |
| 2026-11-17 | [ICT4AWE](https://www.myhuiban.com/conference/1796) | - | C | - | 2027-04-19 | Rome, Italy |
| 2026-11-17 | [IMPROVE](https://www.myhuiban.com/conference/5613) | - | - | - | 2027-04-18 | Rome, Italy |
| 2026-11-17 | [IoTBDS](https://www.myhuiban.com/conference/5612) | - | C | - | 2027-04-18 | Rome, Italy |
| 2026-11-17 | [SMARTGREENS](https://www.myhuiban.com/conference/5602) | - | - | - | 2027-04-16 | Rome, Italy |
| 2026-11-17 | [VEHITS](https://www.myhuiban.com/conference/5601) | - | C | - | 2027-04-16 | Rome, Italy |
| 2026-11-18 | [ESANN](https://www.myhuiban.com/conference/2358) | - | B | - | 2027-04-21 | Bruges, Belgium |
| 2026-11-19 | [MMSys](https://www.myhuiban.com/conference/897) | - | A | B3 | 2027-03-30 | Ghent, Belgium |
| 2026-11-20 *(extended)* | [AAMLDS](https://www.myhuiban.com/conference/5579) | - | - | - | 2026-12-04 | Xiamen, China |
| 2026-11-20 *(extended)* | [ACAI](https://www.myhuiban.com/conference/2855) | - | - | - | 2026-12-18 | Hangzhou, China |
| 2026-11-20 | [AIRC](https://www.myhuiban.com/conference/4929) | - | - | - | 2027-04-06 | Tempe, Arizona, USA |
| 2026-11-20 | [AISRA](https://www.myhuiban.com/conference/5746) | - | - | - | 2026-12-04 | Chengdu, China |
| 2026-11-20 | [ALIS](https://www.myhuiban.com/conference/5587) | - | - | - | 2027-02-01 | Canberra, Australia |
| 2026-11-20 | [CESEE](https://www.myhuiban.com/conference/4474) | - | - | - | 2027-06-17 | Milan, Italy |
| 2026-11-20 *(extended)* | [DSIT](https://www.myhuiban.com/conference/2620) | - | - | - | 2026-11-27 | Taicang, China |
| 2026-11-20 | [ETLTC](https://www.myhuiban.com/conference/4946) | - | - | - | 2027-01-25 | Aizuwakamatsu, Japan |
| 2026-11-20 | [IAEAC](https://www.myhuiban.com/conference/1764) | - | - | - | 2027-03-12 | Chongqing, China |
| 2026-11-20 *(extended)* | [ICAMEM](https://www.myhuiban.com/conference/2566) | - | - | - | 2026-12-18 | Singapore |
| 2026-11-20 | [ICETM'](https://www.myhuiban.com/conference/4947) | - | - | - | 2027-01-25 | Aizuwakamatsu, Japan |
| 2026-11-20 | [ICGDA](https://www.myhuiban.com/conference/2348) | - | - | - | 2027-04-05 | Paris, France |
| 2026-11-20 | [ICMDA](https://www.myhuiban.com/conference/4930) | - | - | - | 2027-04-08 | Hiroshima, Japan |
| 2026-11-20 | [ICOCE](https://www.myhuiban.com/conference/5229) | - | - | - | 2027-04-07 | Singapore |
| 2026-11-20 | [ICPEGE](https://www.myhuiban.com/conference/5090) | - | - | - | 2027-01-28 | Shenyang, China |
| 2026-11-20 *(extended)* | [ICRAIE](https://www.myhuiban.com/conference/4147) | - | - | - | 2026-12-11 | Nanjing, China |
| 2026-11-20 | [ICoSSE](https://www.myhuiban.com/conference/4928) | - | - | - | 2027-04-05 | Paris, France |
| 2026-11-20 | [ISDEA](https://www.myhuiban.com/conference/1061) | - | - | - | 2027-04-24 | Okinawa, Japan |
| 2026-11-20 | [ITEC](https://www.myhuiban.com/conference/3125) | - | - | - | 2027-06-16 | Novi, Michigan, USA |
| 2026-11-20 *(extended)* | [MLBDM](https://www.myhuiban.com/conference/4434) | - | - | - | 2026-12-18 | Hangzhou, China |
| 2026-11-20 | [MLCI](https://www.myhuiban.com/conference/5200) | - | - | - | 2027-04-24 | Okinawa, Japan |
| 2026-11-20 *(extended)* | [MLNLP](https://www.myhuiban.com/conference/2852) | - | - | - | 2026-12-04 | Xiamen, China |
| 2026-11-20 | [PAKDD](https://www.myhuiban.com/conference/157) | C | B | - | 2027-06-29 | Wellington, New Zealand |
| 2026-11-20 | [PIERS](https://www.myhuiban.com/conference/2084) | - | - | - | 2027-05-09 | Daejeon, South Korea |
| 2026-11-20 *(extended)* | [PRDM](https://www.myhuiban.com/conference/3781) | - | - | - | 2026-12-18 | Hangzhou, China |
| 2026-11-21 | [ICCCT](https://www.myhuiban.com/conference/5901) | - | - | - | 2027-01-30 | Goa, India |
| 2026-11-22 | [WorldCist](https://www.myhuiban.com/conference/5636) | - | C | - | 2027-03-23 | Cape Town, South Africa |
| 2026-11-24 | [CCGRID](https://www.myhuiban.com/conference/342) | C | B | A1 | 2027-05-24 | Dallas-Fort Worth, Texas, USA |
| 2026-11-25 | [CVAI](https://www.myhuiban.com/conference/4993) | - | - | - | 2027-03-25 | Hong Kong, China |
| 2026-11-25 | [DASFAA](https://www.myhuiban.com/conference/158) | B | B | B1 | 2027-05-27 | Shenyang, China |
| 2026-11-25 | [DSN](https://www.myhuiban.com/conference/187) | B | A | A1 | 2027-06-22 | Berlin, Germany |
| 2026-11-25 | [EuroS&P](https://www.myhuiban.com/conference/2920) | C | A | - | 2027-07-05 | Madrid, Spain |
| 2026-11-25 | [FCCE](https://www.myhuiban.com/conference/5563) | - | - | - | 2027-04-16 | Hefei, China |
| 2026-11-25 | [ICARC](https://www.myhuiban.com/conference/4201) | - | - | - | 2027-02-16 | Online |
| 2026-11-25 | [ICIEA'](https://www.myhuiban.com/conference/3446) | - | - | - | 2027-04-18 | Bangkok, Thailand |
| 2026-11-25 | [IECA](https://www.myhuiban.com/conference/4991) | - | - | - | 2027-01-15 | Kunming, China |
| 2026-11-25 | [ISMSI](https://www.myhuiban.com/conference/2909) | - | - | - | 2027-04-23 | Ho Chi Minh City, Vietnam |
| 2026-11-26 | [ICMLAS](https://www.myhuiban.com/conference/5810) | - | - | - | 2027-02-25 | Bangkok, Thailand |
| 2026-11-27 | [AIFC](https://www.myhuiban.com/conference/5552) | - | - | - | 2026-12-11 | Guangzhou, China |
| 2026-11-27 | [BDAIEM](https://www.myhuiban.com/conference/5734) | - | - | - | 2026-12-11 | Ningbo, China |
| 2026-11-27 *(extended)* | [CMAAE](https://www.myhuiban.com/conference/3265) | - | - | - | 2026-12-25 | Shanghai, China |
| 2026-11-27 | [ECCST](https://www.myhuiban.com/conference/4680) | - | - | - | 2026-12-11 | Xi an, China |
| 2026-11-27 | [Mobisys](https://www.myhuiban.com/conference/357) | B | A | A1 | 2027-06-21 | Ho Chi Minh City, Vietnam |
| 2026-11-29 | [ICIACS](https://www.myhuiban.com/conference/5814) | - | - | - | 2027-03-01 | Kangeyam, India |
| 2026-11-29 | [IISEC](https://www.myhuiban.com/conference/5732) | - | - | - | 2027-01-28 | Ankara, Turkiye |
| 2026-11-30 | [AAIEE](https://www.myhuiban.com/conference/4936) | - | - | - | 2027-04-23 | Guangzhou, China |
| 2026-11-30 | [CEEPE](https://www.myhuiban.com/conference/3023) | - | - | - | 2027-04-16 | Tianjin, China |
| 2026-11-30 | [CROS](https://www.myhuiban.com/conference/5367) | - | - | - | 2027-04-27 | Sao Paulo, Brazil |
| 2026-11-30 *(extended)* | [DSSE](https://www.myhuiban.com/conference/5469) | - | - | - | 2026-12-25 | Shanghai, China |
| 2026-11-30 | [EPEMR](https://www.myhuiban.com/conference/5442) | - | - | - | 2027-05-28 | Guilin, China |
| 2026-11-30 | [FAIML](https://www.myhuiban.com/conference/3031) | - | - | - | 2027-05-07 | China |
| 2026-11-30 | [ICAIBD](https://www.myhuiban.com/conference/2926) | - | - | - | 2027-05-28 | Chengdu, China |
| 2026-11-30 | [ICBBT](https://www.myhuiban.com/conference/4511) | - | - | - | 2027-05-21 | Qingdao, China |
| 2026-11-30 *(extended)* | [ICCRD](https://www.myhuiban.com/conference/4888) | - | - | - | 2027-01-15 | Singapore |
| 2026-11-30 | [ICITSC](https://www.myhuiban.com/conference/5848) | - | - | - | 2027-03-05 | Chengdu, China |
| 2026-11-30 | [ICNLP](https://www.myhuiban.com/conference/3366) | - | - | - | 2027-04-16 | Zhenjiang, China |
| 2026-11-30 | [ICRCICN](https://www.myhuiban.com/conference/1780) | - | - | - | 2027-02-27 | Kalyani, West Bengal, India |
| 2026-11-30 | [IEAI](https://www.myhuiban.com/conference/3597) | - | - | - | 2027-04-28 | Seoul, South Korea |
| 2026-11-30 | [IEEE HPSR](https://www.myhuiban.com/conference/908) | - | C | - | 2027-06-15 | Paris, France |
| 2026-11-30 *(extended)* | [ISSE'](https://www.myhuiban.com/conference/5468) | - | - | - | 2026-12-25 | Shanghai, China |
| 2026-11-30 | [MSIE](https://www.myhuiban.com/conference/2968) | - | - | - | 2027-04-28 | Seoul, South Korea |
| 2026-11-30 | [SECON](https://www.myhuiban.com/conference/311) | B | B | B1 | 2027-05-05 | Lisbon, Portugal |
| 2026-11-30 | [icABCD](https://www.myhuiban.com/conference/5941) | - | - | - | 2027-07-22 | Port Louis, Mauritius |
| 2026-12-01 | [CETA](https://www.myhuiban.com/conference/4931) | - | - | - | 2027-04-16 | Ankara, Turkey |
| 2026-12-01 | [CPAIOR](https://www.myhuiban.com/conference/2409) | - | B | - | 2027-06-01 | Toulouse, France |
| 2026-12-01 | [FSE'](https://www.myhuiban.com/conference/585) | B | B | A2 | 2027-05-24 | Maastricht, the Netherlands |
| 2026-12-01 | [GOODTECHS](https://www.myhuiban.com/conference/2903) | - | - | - | 2027-04-22 | Heraklion, Crete, Greece |
| 2026-12-01 | [ICEEE'](https://www.myhuiban.com/conference/2393) | - | - | - | 2027-04-16 | Ankara, Turkey |
| 2026-12-01 | [IE'](https://www.myhuiban.com/conference/5599) | - | B | - | 2027-06-21 | Skopje, North Macedonia |
| 2026-12-01 | [IntelliSys](https://www.myhuiban.com/conference/1671) | - | - | - | 2027-09-02 | Amsterdam, the Netherlands |
| 2026-12-01 | [MOST](https://www.myhuiban.com/conference/4683) | - | - | - | 2027-04-04 | Pomona, California, USA |
| 2026-12-01 | [OSDI](https://www.myhuiban.com/conference/358) | A | A* | A1 | 2027-07-07 | Baltimore, Maryland, USA |
| 2026-12-01 | [RSSM](https://www.myhuiban.com/conference/5387) | - | - | - | 2027-01-15 | Chongqing, China |
| 2026-12-01 | [SAI](https://www.myhuiban.com/conference/1330) | - | - | - | 2027-07-08 | London, UK |
| 2026-12-01 | [WoWMoM](https://www.myhuiban.com/conference/652) | C | C | B3 | 2027-06-21 | Irvine, California, USA |
| 2026-12-03 | [GAIIS](https://www.myhuiban.com/conference/5149) | - | - | - | 2027-03-26 | Guangzhou, China |
| 2026-12-03 | [ICBC](https://www.myhuiban.com/conference/2955) | - | C | - | 2027-05-31 | Toronto, Ontario, Canada |
| 2026-12-03 | [PODS](https://www.myhuiban.com/conference/138) | B | A* | A1 | 2027-06-13 | Huntington Beach, California, USA |
| 2026-12-03 | [TFP](https://www.myhuiban.com/conference/3202) | - | - | - | 2027-03-12 | Kyoto, Japan |
| 2026-12-04 | [AIVRV](https://www.myhuiban.com/conference/4446) | - | - | - | 2026-12-18 | Wuhan, China |
| 2026-12-04 | [Confluence](https://www.myhuiban.com/conference/5783) | - | - | - | 2027-01-21 | Noida, India |
| 2026-12-04 | [RSS](https://www.myhuiban.com/conference/471) | - | - | - | 2027-07-06 | Athens, Greece |
| 2026-12-05 | [AITC](https://www.myhuiban.com/conference/3372) | - | - | - | 2027-05-07 | Lianyungang, China |
| 2026-12-05 | [ICCCBDA](https://www.myhuiban.com/conference/3371) | - | - | - | 2027-04-23 | Chengdu, China |
| 2026-12-05 | [ICKECS](https://www.myhuiban.com/conference/5362) | - | - | - | 2027-04-23 | Chickballapur, India |
| 2026-12-05 *(extended)* | [ICSIM](https://www.myhuiban.com/conference/2808) | - | - | - | 2027-01-20 | Tokyo, Japan |
| 2026-12-05 | [ISAI'](https://www.myhuiban.com/conference/4935) | - | - | - | 2027-04-23 | Chengdu, China |
| 2026-12-05 | [NISS'](https://www.myhuiban.com/conference/2979) | - | - | - | 2027-04-27 | Casablanca, Morocco |
| 2026-12-07 | [IAS'](https://www.myhuiban.com/conference/5283) | - | - | - | 2027-06-27 | Rome, Italy |
| 2026-12-07 | [ICAPS](https://www.myhuiban.com/conference/417) | B | A* | A2 | 2027-06-27 | Columbia, South Carolina, USA |
| 2026-12-07 | [IPMI](https://www.myhuiban.com/conference/465) | - | - | - | 2027-06-27 | Lake Stukely, Quebec, Canada |
| 2026-12-08 | [ETS](https://www.myhuiban.com/conference/1485) | C | B | B2 | 2027-05-24 | London, UK |
| 2026-12-08 | [IMS](https://www.myhuiban.com/conference/4964) | - | - | - | 2027-05-23 | San Antonio, Texas, USA |
| 2026-12-08 | [Transducers](https://www.myhuiban.com/conference/5960) | - | - | - | 2027-06-20 | Stockholm, Sweden |
| 2026-12-09 | [ICOECA](https://www.myhuiban.com/conference/5822) | - | - | - | 2027-03-11 | Bengaluru, Karnataka, India |
| 2026-12-09 | [WISTP](https://www.myhuiban.com/conference/785) | - | C | - | 2027-03-19 | Djerba, Tunisia |
| 2026-12-10 | [EECR](https://www.myhuiban.com/conference/2857) | - | - | - | 2027-04-23 | Shenzhen, China |
| 2026-12-10 | [ESWC](https://www.myhuiban.com/conference/542) | C | B | A1 | 2027-05-23 | Limassol, Cyprus |
| 2026-12-10 | [ICBDA](https://www.myhuiban.com/conference/2289) | - | - | - | 2027-04-26 | Bangkok, Thailand |
| 2026-12-10 | [ICCIIA](https://www.myhuiban.com/conference/5207) | - | - | - | 2027-02-26 | Wuhan, China |
| 2026-12-10 | [ICCMS'](https://www.myhuiban.com/conference/3481) | - | - | - | 2027-05-14 | Beijing, China |
| 2026-12-10 | [ICCTech](https://www.myhuiban.com/conference/4940) | - | - | - | 2027-05-14 | Beijing, China |
| 2026-12-10 | [ICIAI](https://www.myhuiban.com/conference/3831) | - | - | - | 2027-04-26 | Bangkok, Thailand |
| 2026-12-10 | [ICMERR](https://www.myhuiban.com/conference/4945) | - | - | - | 2027-05-10 | Paris, France |
| 2026-12-10 | [ICMHI](https://www.myhuiban.com/conference/3352) | - | - | - | 2027-05-28 | Kyoto, Japan |
| 2026-12-10 | [ICMIMT](https://www.myhuiban.com/conference/4700) | - | - | - | 2027-05-13 | Cape Town, South Africa |
| 2026-12-10 | [ICMLT](https://www.myhuiban.com/conference/2456) | - | - | - | 2027-05-21 | Stockholm, Sweden |
| 2026-12-10 | [ITFM](https://www.myhuiban.com/conference/5445) | - | - | - | 2027-03-19 | Hohhot, China |
| 2026-12-11 | [ACM ASIACCS](https://www.myhuiban.com/conference/367) | C | A | B1 | 2027-07-12 | Macau, China |
| 2026-12-11 | [ADIST](https://www.myhuiban.com/conference/5466) | - | - | - | 2027-02-26 | Harbin, China |
| 2026-12-11 | [CIR](https://www.myhuiban.com/conference/5133) | - | - | - | 2026-12-25 | Haikou, China |
| 2026-12-11 | [EIECC](https://www.myhuiban.com/conference/5225) | - | - | - | 2026-12-25 | Guangzhou, China |
| 2026-12-11 | [ICMLS](https://www.myhuiban.com/conference/5735) | - | - | - | 2026-12-25 | Changsha, China |
| 2026-12-11 | [ISPASS](https://www.myhuiban.com/conference/1408) | C | B | B1 | 2027-05-09 | New York City, New York, USA |
| 2026-12-12 | [ICTMIM](https://www.myhuiban.com/conference/5824) | - | - | - | 2027-03-18 | Kanyakumari, India |
| 2026-12-14 | [ARCS](https://www.myhuiban.com/conference/210) | - | - | B2 | 2027-03-09 | Magdeburg, Germany |
| 2026-12-14 | [GMP](https://www.myhuiban.com/conference/380) | C | C | B2 | 2027-06-21 | Singapore |
| 2026-12-14 | [ISC''](https://www.myhuiban.com/conference/779) | - | - | - | 2027-06-07 | Hamburg, Germany |
| 2026-12-15 | [AISCN](https://www.myhuiban.com/conference/5832) | - | - | - | 2027-04-09 | Taichung, Taiwan |
| 2026-12-15 | [CI2A](https://www.myhuiban.com/conference/5826) | - | - | - | 2027-03-19 | Yogyakarta, Indonesia |
| 2026-12-15 | [ICCEE](https://www.myhuiban.com/conference/1114) | - | - | - | 2027-06-23 | Canberra, Australia |
| 2026-12-15 | [ICDF2C](https://www.myhuiban.com/conference/1851) | C | - | - | 2027-06-25 | New York City, New York, USA |
| 2026-12-15 | [ICMI'](https://www.myhuiban.com/conference/5733) | - | - | - | 2027-05-01 | Mt. Pleasant, Michigan, USA |
| 2026-12-15 *(extended)* | [ICMLSC](https://www.myhuiban.com/conference/2975) | - | - | - | 2027-01-29 | Tokyo, Japan |
| 2026-12-15 | [IEA/AIE](https://www.myhuiban.com/conference/3682) | - | C | - | 2027-07-20 | Naples, Italy |
| 2026-12-15 | [IEEE CONECCT](https://www.myhuiban.com/conference/4809) | - | - | - | 2027-03-13 | Bangalore, India |
| 2026-12-15 | [IFIP SEC](https://www.myhuiban.com/conference/3976) | C | B | - | 2027-06-14 | Linkoping, Sweden |
| 2026-12-15 | [ITET](https://www.myhuiban.com/conference/4291) | - | - | - | 2027-05-28 | Okayama, Japan |
| 2026-12-15 | [UNet](https://www.myhuiban.com/conference/1687) | - | - | - | 2027-05-25 | Montreal, Quebec, Canada |
| 2026-12-15 | [WCE](https://www.myhuiban.com/conference/5905) | - | - | - | 2027-08-23 | Cambridge, UK |
| 2026-12-15 | [WISM](https://www.myhuiban.com/conference/5969) | - | - | - | 2027-06-14 | Linkoping, Sweden |
| 2026-12-16 | [ISPSD](https://www.myhuiban.com/conference/4733) | - | - | - | 2027-06-13 | Taipei, Taiwan |
| 2026-12-18 | [AETCSE](https://www.myhuiban.com/conference/5440) | - | - | - | 2027-03-19 | Nanjing, China |
| 2026-12-18 | [BNNIO](https://www.myhuiban.com/conference/5390) | - | - | - | 2027-02-26 | Sanya, China |
| 2026-12-18 | [ISEAIC](https://www.myhuiban.com/conference/5163) | - | - | - | 2027-02-26 | Sanya, China |
| 2026-12-18 | [OLA](https://www.myhuiban.com/conference/5883) | - | - | - | 2027-05-05 | Krakow, Poland |
| 2026-12-20 | [AICCONF](https://www.myhuiban.com/conference/4900) | - | - | - | 2027-03-25 | Dubai, UAE |
| 2026-12-20 | [CIPCV](https://www.myhuiban.com/conference/4489) | - | - | - | 2027-08-20 | Shanghai, China |
| 2026-12-20 | [EMC+SIPI](https://www.myhuiban.com/conference/5321) | - | - | - | 2027-07-12 | Portland, Oregon, USA |
| 2026-12-20 | [ICCRE](https://www.myhuiban.com/conference/4925) | - | - | - | 2027-05-07 | Hong Kong, China |
| 2026-12-20 | [ICPST](https://www.myhuiban.com/conference/4961) | - | - | - | 2027-05-14 | Zhengzhou, China |
| 2026-12-20 | [MSME](https://www.myhuiban.com/conference/2614) | - | - | - | 2027-04-22 | Tianjin, China |
| 2026-12-20 | [RCVE](https://www.myhuiban.com/conference/4513) | - | - | - | 2027-06-21 | Paris, France |
| 2026-12-20 | [SSVM](https://www.myhuiban.com/conference/521) | - | - | - | 2027-06-06 | Veldhoven, the Netherlands |
| 2026-12-21 | [GAIIP](https://www.myhuiban.com/conference/5421) | - | - | - | 2027-03-05 | Guangzhou, China |
| 2026-12-23 | [ISDS](https://www.myhuiban.com/conference/5414) | - | - | - | 2027-03-12 | Tianjin, China |
| 2026-12-24 | [ICGEE](https://www.myhuiban.com/conference/4453) | - | - | - | 2027-03-25 | Jeju Island, South Korea |
| 2026-12-25 *(extended)* | [AIACT](https://www.myhuiban.com/conference/2601) | - | - | - | 2027-02-26 | Nanjing, China |
| 2026-12-25 | [ICAIE'](https://www.myhuiban.com/conference/4180) | - | - | - | 2027-05-28 | Bangkok, Thailand |
| 2026-12-25 | [ICCAR](https://www.myhuiban.com/conference/1774) | - | - | - | 2027-04-23 | Nanchang, China |
| 2026-12-25 | [ICETT](https://www.myhuiban.com/conference/4510) | - | - | - | 2027-05-21 | Seoul, South Korea |
| 2026-12-25 | [ICISN](https://www.myhuiban.com/conference/4152) | - | - | - | 2027-03-20 | Hai Phong, Vietnam |
| 2026-12-26 | [CTADS](https://www.myhuiban.com/conference/5408) | - | - | - | 2027-03-12 | Nanjing, China |
| 2026-12-26 | [ICICCS](https://www.myhuiban.com/conference/3405) | - | - | - | 2027-03-22 | Machangolhi, Maldives |
| 2026-12-28 | [ISBDAS](https://www.myhuiban.com/conference/2910) | - | - | - | 2027-03-12 | Nanjing, China |
| 2026-12-28 | [i-Society](https://www.myhuiban.com/conference/628) | - | - | - | 2027-08-23 | Cambridge, UK |
| 2026-12-29 | [CSAIDE](https://www.myhuiban.com/conference/4339) | - | - | - | 2027-03-19 | Hangzhou, China |
| 2026-12-30 | [ICAIC](https://www.myhuiban.com/conference/5818) | - | - | - | 2027-03-03 | Houston, Texas, USA |
| 2026-12-30 | [ICTC'](https://www.myhuiban.com/conference/3531) | - | - | - | 2027-05-21 | Nanjing, China |
| 2026-12-31 | [ICISCN](https://www.myhuiban.com/conference/4971) | - | - | - | 2027-04-24 | Gornalli, India |
| 2026-12-31 | [IDAA](https://www.myhuiban.com/conference/5884) | - | - | - | 2027-06-11 | Dhaka, Bangladesh |
| 2026-12-31 | [WAMS](https://www.myhuiban.com/conference/5954) | - | - | - | 2027-07-01 | Tadepalligudem, India |
| 2027-01-01 | [EIEDP](https://www.myhuiban.com/conference/4322) | - | - | - | 2027-01-15 | Quanzhou, China |
| 2027-01-01 | [ICCCAS](https://www.myhuiban.com/conference/4242) | - | - | - | 2027-05-21 | Chengdu, China |
| 2027-01-01 | [ICCCR](https://www.myhuiban.com/conference/4169) | - | - | - | 2027-05-14 | Chengdu, China |
| 2027-01-01 | [IMNM](https://www.myhuiban.com/conference/5388) | - | - | - | 2027-03-19 | Wuhan, China |
| 2027-01-03 | [PETGS](https://www.myhuiban.com/conference/5226) | - | - | - | 2027-01-15 | Quanzhou, China |
| 2027-01-04 | [ACL](https://www.myhuiban.com/conference/411) | A | A* | A1 | 2027-08-17 | Japan |
| 2027-01-04 | [CIISC](https://www.myhuiban.com/conference/5955) | - | - | - | 2027-06-21 | Hefei, China |
| 2027-01-04 | [IJCAI](https://www.myhuiban.com/conference/405) | B | A* | A1 | 2027-08-07 | Kyoto, Japan |
| 2027-01-04 | [NFM](https://www.myhuiban.com/conference/1830) | - | - | - | 2027-05-11 | Houston, Texas, USA |
| 2027-01-05 | [ECCS](https://www.myhuiban.com/conference/4926) | - | - | - | 2027-06-02 | Vienna, Austria |
| 2027-01-05 | [ICCTA''](https://www.myhuiban.com/conference/4108) | - | - | - | 2027-06-02 | Vienna, Austria |
| 2027-01-05 *(extended)* | [ICRIC](https://www.myhuiban.com/conference/5565) | - | - | - | 2027-02-17 | Milan, Italy |
| 2027-01-05 | [ICSGGE](https://www.myhuiban.com/conference/4990) | - | - | - | 2027-03-19 | Hong Kong, China |
| 2027-01-05 | [ICSREE](https://www.myhuiban.com/conference/4241) | - | - | - | 2027-05-25 | Madrid, Spain |
| 2027-01-05 | [KALINGACONF](https://www.myhuiban.com/conference/5334) | - | - | - | 2027-06-01 | Naya Raipur, India |
| 2027-01-05 | [SRSE](https://www.myhuiban.com/conference/4850) | - | - | - | 2027-05-28 | Shanghai, China |
| 2027-01-06 | [BIC](https://www.myhuiban.com/conference/5409) | - | - | - | 2027-04-09 | Shenzhen, China |
| 2027-01-06 | [CyCon](https://www.myhuiban.com/conference/1370) | - | - | - | 2027-05-25 | Tallinn, Estonia |
| 2027-01-06 | [RFIC](https://www.myhuiban.com/conference/4749) | - | - | - | 2027-05-23 | San Antonio, Texas, USA |
| 2027-01-08 | [CAIC'](https://www.myhuiban.com/conference/5160) | - | - | - | 2027-01-22 | Sanya, China |
| 2027-01-08 | [ISSTA](https://www.myhuiban.com/conference/177) | A | A | A2 | 2027-09-07 | Singapore |
| 2027-01-09 | [CSECS](https://www.myhuiban.com/conference/4610) | - | - | - | 2027-04-09 | Hangzhou, China |
| 2027-01-09 | [I&CPS](https://www.myhuiban.com/conference/5376) | - | - | - | 2027-05-17 | Ottawa, Ontario, Canada |
| 2027-01-09 | [ICISS'''](https://www.myhuiban.com/conference/5830) | - | - | - | 2027-04-01 | Tirunelveli, India |
| 2027-01-09 | [IPDL](https://www.myhuiban.com/conference/4995) | - | - | - | 2027-04-23 | Xi an, China |
| 2027-01-10 | [APDSP](https://www.myhuiban.com/conference/5161) | - | - | - | 2027-05-28 | Xining, China |
| 2027-01-10 | [CCAI](https://www.myhuiban.com/conference/3908) | - | - | - | 2027-05-21 | Shanghai, China |
| 2027-01-10 | [CCGIV](https://www.myhuiban.com/conference/2617) | - | - | - | 2027-04-09 | Hangzhou, China |
| 2027-01-10 | [CVIPPR](https://www.myhuiban.com/conference/4499) | - | - | - | 2027-04-16 | Xi an, China |
| 2027-01-10 | [FCCM](https://www.myhuiban.com/conference/351) | C | - | A2 | 2027-05-09 | Provo, Utah, USA |
| 2027-01-10 | [ICAIM](https://www.myhuiban.com/conference/5004) | - | - | - | 2027-03-12 | Changsha, China |
| 2027-01-10 | [ICBDT](https://www.myhuiban.com/conference/2432) | - | - | - | 2027-05-21 | Chengdu, China |
| 2027-01-10 | [ICMDRSE](https://www.myhuiban.com/conference/5946) | - | - | - | 2027-07-08 | Pune, India |
| 2027-01-10 | [ICMVA](https://www.myhuiban.com/conference/2434) | - | - | - | 2027-06-03 | Singapore |
| 2027-01-10 | [ICOWC](https://www.myhuiban.com/conference/1860) | - | - | - | 2027-05-21 | Shenzhen, China |
| 2027-01-10 | [MDTS](https://www.myhuiban.com/conference/4072) | - | - | - | 2027-05-17 | Albany, New York, USA |
| 2027-01-10 | [SEAI](https://www.myhuiban.com/conference/4774) | - | - | - | 2027-06-18 | Quanzhou, China |
| 2027-01-10 | [SECA](https://www.myhuiban.com/conference/5392) | - | - | - | 2027-03-26 | Changsha, China |
| 2027-01-11 | [CISCE](https://www.myhuiban.com/conference/4054) | - | - | - | 2027-03-26 | Guangzhou, China |
| 2027-01-11 | [CIbSE](https://www.myhuiban.com/conference/2958) | - | - | - | 2027-05-10 | Vina del Mar, Chile |
| 2027-01-11 | [CSW'](https://www.myhuiban.com/conference/5966) | - | - | - | 2027-06-15 | Venice, Italy |
| 2027-01-11 | [DIPCA](https://www.myhuiban.com/conference/5030) | - | - | - | 2027-03-26 | Urumqi, China |
| 2027-01-11 | [DIS](https://www.myhuiban.com/conference/1413) | C | A | A2 | 2027-06-28 | Stockholm, Sweden |
| 2027-01-11 | [ETHICS](https://www.myhuiban.com/conference/5953) | - | - | - | 2027-06-25 | Durham, North Carolina, USA |
| 2027-01-11 | [IC-EpsMsO](https://www.myhuiban.com/conference/5888) | - | - | - | 2027-07-07 | Loutraki, Greece |
| 2027-01-11 | [ICMPME](https://www.myhuiban.com/conference/2309) | - | - | - | 2027-03-26 | Shenyang, China |
| 2027-01-11 | [IGARSS](https://www.myhuiban.com/conference/5319) | - | C | - | 2027-07-11 | Reykjavík, Iceland |
| 2027-01-11 | [NEMD](https://www.myhuiban.com/conference/5444) | - | - | - | 2027-03-26 | Shenyang, China |
| 2027-01-11 | [NOSSDAV](https://www.myhuiban.com/conference/315) | B | B | A2 | 2027-04-02 | Ghent, Belgium |
| 2027-01-11 | [SIGMETRICS](https://www.myhuiban.com/conference/327) | B | A* | A1 | 2027-06-07 | Atlanta, Georgia, USA |
| 2027-01-12 | [CIBDA](https://www.myhuiban.com/conference/4765) | - | - | - | 2027-03-19 | Wuhan, China |
| 2027-01-12 | [ICAACE](https://www.myhuiban.com/conference/4497) | - | - | - | 2027-03-26 | Hangzhou, China |
| 2027-01-12 | [ICECET](https://www.myhuiban.com/conference/4103) | - | - | - | 2027-07-09 | Seoul, South Korea |
| 2027-01-12 | [ICICT'](https://www.myhuiban.com/conference/2265) | - | - | - | 2027-04-19 | Lalitpur, Nepal |
| 2027-01-12 | [INDIN](https://www.myhuiban.com/conference/112) | - | C | B3 | 2027-05-10 | Lisbon, Portugal |
| 2027-01-12 | [MEMA](https://www.myhuiban.com/conference/3313) | - | - | - | 2027-03-26 | Beijing, China |
| 2027-01-14 | [IEEE RFID](https://www.myhuiban.com/conference/4735) | - | - | - | 2027-06-14 | Memphis, Tennessee, USA |
| 2027-01-14 | [MVA](https://www.myhuiban.com/conference/5886) | - | - | - | 2027-05-12 | Fukuoka, Japan |
| 2027-01-14 | [SIGIR](https://www.myhuiban.com/conference/141) | A | A* | A1 | 2027-07-18 | San Jose, California, USA |
| 2027-01-15 | [ASENS](https://www.myhuiban.com/conference/5031) | - | - | - | 2027-03-26 | Xi an, China |
| 2027-01-15 | [BMSB](https://www.myhuiban.com/conference/1197) | - | - | - | 2027-07-07 | Sydney, Australia |
| 2027-01-15 | [DSDE](https://www.myhuiban.com/conference/79) | - | - | B4 | 2027-07-09 | Tokyo, Japan |
| 2027-01-15 | [FIST](https://www.myhuiban.com/conference/5923) | - | - | - | 2027-08-27 | New Delhi, India |
| 2027-01-15 | [FUZZ-IEEE](https://www.myhuiban.com/conference/435) | - | B | A2 | 2027-07-10 | Sydney, Australia |
| 2027-01-15 | [ICALT](https://www.myhuiban.com/conference/494) | - | B | B1 | 2027-07-19 | Dortmund, Germany |
| 2027-01-15 | [ICCCM](https://www.myhuiban.com/conference/4045) | - | - | - | 2027-07-09 | Tokyo, Japan |
| 2027-01-15 | [ICCSS](https://www.myhuiban.com/conference/2553) | - | - | - | 2027-06-25 | Da Nang, Vietnam |
| 2027-01-15 | [ICGCET](https://www.myhuiban.com/conference/2426) | - | - | - | 2027-04-28 | Kathmandu, Nepal |
| 2027-01-15 | [ICWSM](https://www.myhuiban.com/conference/526) | B | A | B1 | 2027-05-27 | Edinburgh, UK |
| 2027-01-15 | [IMI](https://www.myhuiban.com/conference/5894) | - | - | - | 2027-01-29 | Xiamen, China |
| 2027-01-15 | [IT'](https://www.myhuiban.com/conference/4983) | - | - | - | 2027-02-24 | Zabljak, Montenegro |
| 2027-01-15 | [IWBBIO](https://www.myhuiban.com/conference/5430) | - | - | - | 2027-07-14 | Gran Canaria, Spain |
| 2027-01-15 | [IWCMC](https://www.myhuiban.com/conference/913) | - | B | B1 | 2027-06-13 | Barcelona, Spain |
| 2027-01-15 | [LSSC](https://www.myhuiban.com/conference/2066) | - | - | - | 2027-06-14 | Sozopol, Bulgaria |
| 2027-01-15 | [NetSoft](https://www.myhuiban.com/conference/1633) | - | B | - | 2027-06-28 | Seoul, South Korea |
| 2027-01-15 | [RobCE](https://www.myhuiban.com/conference/3738) | - | - | - | 2027-05-20 | Shenzhen, China |
| 2027-01-15 | [SSIP](https://www.myhuiban.com/conference/2755) | - | - | - | 2027-06-09 | Ostrava, Czech Republic |
| 2027-01-15 | [SeGAH](https://www.myhuiban.com/conference/1791) | - | - | - | 2027-06-23 | Osaka, Japan |
| 2027-01-15 | [WPTCE](https://www.myhuiban.com/conference/5959) | - | - | - | 2027-07-02 | Chongqing, China |
| 2027-01-15 | [WSES](https://www.myhuiban.com/conference/3849) | - | - | - | 2027-06-11 | Nanjing, China |
| 2027-01-16 | [SVCC](https://www.myhuiban.com/conference/4760) | - | - | - | 2027-06-21 | San Jose, California, USA |
| 2027-01-19 | [USENIX Security](https://www.myhuiban.com/conference/292) | A | A* | A1 | 2027-08-11 | Denver, Colorado, USA |
| 2027-01-20 | [AAIP](https://www.myhuiban.com/conference/5046) | - | - | - | 2027-06-25 | Shanghai, China |
| 2027-01-20 | [CAV](https://www.myhuiban.com/conference/243) | A | A* | A1 | 2027-07-19 | Amsterdam, the Netherlands |
| 2027-01-20 | [CBMS](https://www.myhuiban.com/conference/483) | - | B | B1 | 2027-06-23 | Rome, Italy |
| 2027-01-20 | [CEEGE](https://www.myhuiban.com/conference/2551) | - | - | - | 2027-05-07 | Suzhou, China |
| 2027-01-20 | [CMLDS](https://www.myhuiban.com/conference/4716) | - | - | - | 2027-04-16 | Chengdu, China |
| 2027-01-20 | [DCOSS-IoT](https://www.myhuiban.com/conference/4477) | - | - | - | 2027-06-21 | Montreal, Quebec, Canada |
| 2027-01-20 | [ICCSM](https://www.myhuiban.com/conference/1106) | - | - | - | 2027-07-01 | Paris, France |
| 2027-01-20 | [ICEDL](https://www.myhuiban.com/conference/5411) | - | - | - | 2027-07-01 | Paris, France |
| 2027-01-20 | [ICKEA](https://www.myhuiban.com/conference/2454) | - | - | - | 2027-06-09 | London, UK |
| 2027-01-20 | [IFSP](https://www.myhuiban.com/conference/4907) | - | - | - | 2027-07-09 | Chengdu, China |
| 2027-01-20 | [MLANN](https://www.myhuiban.com/conference/4500) | - | - | - | 2027-04-16 | Xi an, China |
| 2027-01-20 | [SACI](https://www.myhuiban.com/conference/3118) | - | - | - | 2027-05-24 | Visegrad, Hungary and Timisoara, Romania |
| 2027-01-21 | [ACNS](https://www.myhuiban.com/conference/360) | C | B | B1 | 2027-06-28 | Egham, UK |

---

Data: **Conference Partner (myhuiban.com)**, free to use with attribution. Ranking values are reproduced from CCF / CORE / QUALIS — cite those bodies for the rankings themselves. The repository's MIT licence covers its code, not this data.
