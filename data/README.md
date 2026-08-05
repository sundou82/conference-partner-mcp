# Data snapshot

Generated **2026-08-05T07:17:33+00:00** from the [Conference Partner API](https://www.myhuiban.com/developers). Refreshed daily by [CI](../.github/workflows/snapshot.yml).

Every file here comes from the API's **anonymous tier** — the same rows anyone can fetch without credentials. Per-venue detail (CFP full text, acceptance-rate history, edition history, ratings, the organiser's own website URL) is not included; it needs a free credential and lives behind the API. See [../docs/data.md](../docs/data.md).

## Files

| Dataset | Rows | JSON | CSV |
|---|---|---|---|
| **Upcoming submission deadlines**<br><sub>Conferences whose submission deadline has not passed, soonest first.</sub> | 705 | [upcoming-deadlines.json](upcoming-deadlines.json) | [upcoming-deadlines.csv](upcoming-deadlines.csv) |
| **CCF-ranked conferences**<br><sub>The CCF catalogue as carried on the site, with CORE and QUALIS alongside.</sub> | 68 | [ccf-conferences.json](ccf-conferences.json) | [ccf-conferences.csv](ccf-conferences.csv) |
| **CORE-ranked conferences**<br><sub>The CORE catalogue as carried on the site.</sub> | 105 | [core-conferences.json](core-conferences.json) | [core-conferences.csv](core-conferences.csv) |
| **QUALIS-ranked conferences**<br><sub>The QUALIS catalogue as carried on the site.</sub> | 86 | [qualis-conferences.json](qualis-conferences.json) | [qualis-conferences.csv](qualis-conferences.csv) |
| **CCF-ranked journals**<br><sub>Journals in the CCF catalogue, with impact factor and publisher.</sub> | 292 | [ccf-journals.json](ccf-journals.json) | [ccf-journals.csv](ccf-journals.csv) |
| **Journals with an open special-issue call**<br><sub>Journals currently carrying a special-issue call for papers.</sub> | 181 | [journal-special-issues.json](journal-special-issues.json) | [journal-special-issues.csv](journal-special-issues.csv) |
| **Journals by impact factor**<br><sub>Highest reported impact factor first. Figures are as published by the journal and may lag the latest JCR.</sub> | 300 ⚠️ partial | [top-impact-factor-journals.json](top-impact-factor-journals.json) | [top-impact-factor-journals.csv](top-impact-factor-journals.csv) |

Site totals on the day of generation: **5788** conferences, **1212** journals.

## Prefer live data

A snapshot is stale the moment a deadline is extended, which happens daily in submission season. For anything that has to be right, call the API — it needs no key for exactly the data in this directory:

```bash
curl "https://www.myhuiban.com/api/conferences?field=ai&submission_date_start=$(date +%F)"
```

Or mirror it incrementally with `updated_since` — see [../docs/rest-api.md](../docs/rest-api.md#incremental-sync).

## Deadlines in the next 90 days (506)

| Deadline | Conference | CCF | CORE | QUALIS | Held | Location |
|---|---|---|---|---|---|---|
| 2026-08-05 | [APCT](https://www.myhuiban.com/conference/4235) | - | - | - | 2027-01-15 | Jakarta, Indonesia |
| 2026-08-05 | [APIET](https://www.myhuiban.com/conference/5183) | - | - | - | 2027-01-15 | Jakarta, Indonesia |
| 2026-08-05 *(extended)* | [CSEE'](https://www.myhuiban.com/conference/4911) | - | - | - | 2026-09-16 | Barcelona, Spain |
| 2026-08-05 *(extended)* | [ICAISG](https://www.myhuiban.com/conference/5512) | - | - | - | 2026-11-20 | Hangzhou, China |
| 2026-08-05 | [ICBBB](https://www.myhuiban.com/conference/3399) | - | - | - | 2027-01-29 | Osaka, Japan |
| 2026-08-05 *(extended)* | [ICCIP](https://www.myhuiban.com/conference/2259) | - | - | - | 2026-11-13 | Lingshui, China |
| 2026-08-05 *(extended)* | [ICDLE](https://www.myhuiban.com/conference/3766) | - | - | - | 2026-09-16 | Barcelona, Spain |
| 2026-08-05 | [ICGIP](https://www.myhuiban.com/conference/1397) | - | - | - | 2026-11-06 | Wuxi, China |
| 2026-08-05 | [ICMEAS](https://www.myhuiban.com/conference/2613) | - | - | - | 2026-12-10 | Kuala Lumpur, Malaysia |
| 2026-08-05 *(extended)* | [ICMIS](https://www.myhuiban.com/conference/5522) | - | - | - | 2026-09-26 | Sapporo, Japan |
| 2026-08-05 | [ICPRE](https://www.myhuiban.com/conference/2273) | - | - | - | 2026-09-18 | Shanghai, China |
| 2026-08-05 | [LMAGI](https://www.myhuiban.com/conference/5542) | - | - | - | 2026-10-30 | Zhangjiajie, China |
| 2026-08-05 | [PESA](https://www.myhuiban.com/conference/5730) | - | - | - | 2026-11-13 | Singapore |
| 2026-08-05 | [PSRE](https://www.myhuiban.com/conference/5012) | - | - | - | 2026-12-02 | Sydney, Australia |
| 2026-08-05 | [REPE](https://www.myhuiban.com/conference/4346) | - | - | - | 2026-09-26 | Beijing, China |
| 2026-08-05 | [WECE](https://www.myhuiban.com/conference/5088) | - | - | - | 2026-10-23 | Chengdu, China |
| 2026-08-06 *(extended)* | [AEMDS](https://www.myhuiban.com/conference/4756) | - | - | - | 2026-10-19 | Glasgow, UK |
| 2026-08-06 *(extended)* | [EEPE-TIA](https://www.myhuiban.com/conference/4027) | - | - | - | 2026-08-07 | Hohhot, China |
| 2026-08-07 | [IPCCC](https://www.myhuiban.com/conference/912) | C | C | B1 | 2026-11-21 | Austin, Texas, USA |
| 2026-08-07 | [ISPEC](https://www.myhuiban.com/conference/1418) | - | C | - | 2026-11-06 | Xi an, China |
| 2026-08-07 | [MIG](https://www.myhuiban.com/conference/3718) | - | C | - | 2026-12-11 | Charleston, South Carolina, USA |
| 2026-08-07 | [SII](https://www.myhuiban.com/conference/5742) | - | - | - | 2027-01-11 | Kobe, Japan |
| 2026-08-07 | [VRISP](https://www.myhuiban.com/conference/5115) | - | - | - | 2026-08-23 | Changchun, China |
| 2026-08-08 *(extended)* | [BMLI](https://www.myhuiban.com/conference/3914) | - | - | - | 2026-09-26 | Toronto, Ontario, Canada |
| 2026-08-08 *(extended)* | [CAIML](https://www.myhuiban.com/conference/3548) | - | - | - | 2026-10-24 | Vienna, Austria |
| 2026-08-08 *(extended)* | [CSEN](https://www.myhuiban.com/conference/3925) | - | - | - | 2026-08-22 | Dubai, UAE |
| 2026-08-08 | [CSITY](https://www.myhuiban.com/conference/2718) | - | - | - | 2026-10-17 | Sydney, Australia |
| 2026-08-08 | [IBCOM](https://www.myhuiban.com/conference/3911) | - | - | - | 2026-09-19 | Copenhagen, Denmark |
| 2026-08-08 *(extended)* | [ICAIT'](https://www.myhuiban.com/conference/3550) | - | - | - | 2026-10-24 | Vienna, Austria |
| 2026-08-08 | [InWeS'](https://www.myhuiban.com/conference/1433) | - | - | - | 2026-09-26 | Toronto, Ontario, Canada |
| 2026-08-08 | [MLBDBI](https://www.myhuiban.com/conference/4451) | - | - | - | 2026-10-23 | Hangzhou, China |
| 2026-08-08 *(extended)* | [NLCA](https://www.myhuiban.com/conference/3947) | - | - | - | 2026-10-24 | Vienna, Austria |
| 2026-08-08 *(extended)* | [NLPSIG](https://www.myhuiban.com/conference/4634) | - | - | - | 2026-09-29 | Online |
| 2026-08-08 | [SPPR](https://www.myhuiban.com/conference/3487) | - | - | - | 2026-09-19 | Copenhagen, Denmark |
| 2026-08-09 *(extended)* | [CSEITT](https://www.myhuiban.com/conference/5835) | - | - | - | 2026-08-27 | Online |
| 2026-08-09 | [ISPDS](https://www.myhuiban.com/conference/3689) | - | - | - | 2026-10-23 | Shanghai, China |
| 2026-08-09 | [MATE](https://www.myhuiban.com/conference/4098) | - | - | - | 2026-09-29 | Online |
| 2026-08-09 | [MVSCIT](https://www.myhuiban.com/conference/4639) | - | - | - | 2026-09-29 | Online |
| 2026-08-09 | [UEMCON](https://www.myhuiban.com/conference/1979) | - | - | - | 2026-10-07 | New York City, USA |
| 2026-08-10 | [ACDSA](https://www.myhuiban.com/conference/4689) | - | - | - | 2027-02-02 | Rio de Janeiro, Brazil |
| 2026-08-10 | [AIS2C](https://www.myhuiban.com/conference/5796) | - | - | - | 2027-01-29 | Bhubaneswar, India |
| 2026-08-10 | [APIT](https://www.myhuiban.com/conference/2881) | - | - | - | 2027-01-22 | Osaka, Japan |
| 2026-08-10 | [CIRCT](https://www.myhuiban.com/conference/5415) | - | - | - | 2026-09-11 | Wuxi, China |
| 2026-08-10 *(extended)* | [CLNLP](https://www.myhuiban.com/conference/3508) | - | - | - | 2026-09-18 | Kunming, China |
| 2026-08-10 *(extended)* | [CRC](https://www.myhuiban.com/conference/4156) | - | - | - | 2026-09-18 | Hefei, China |
| 2026-08-10 | [CVCI](https://www.myhuiban.com/conference/3401) | - | - | - | 2027-01-22 | Osaka, Japan |
| 2026-08-10 | [HASP](https://www.myhuiban.com/conference/5723) | - | - | - | 2026-10-31 | Athens, Greece |
| 2026-08-10 *(extended)* | [ICCT'](https://www.myhuiban.com/conference/808) | - | - | - | 2026-10-16 | Zhuhai, China |
| 2026-08-10 | [ICICM](https://www.myhuiban.com/conference/1978) | - | - | - | 2026-11-11 | Jakarta, Indonesia |
| 2026-08-10 | [ICICyTA](https://www.myhuiban.com/conference/5773) | - | - | - | 2026-12-01 | Bali, Indonesia |
| 2026-08-10 | [ICIGP](https://www.myhuiban.com/conference/3485) | - | - | - | 2027-01-15 | Shenzhen, China |
| 2026-08-10 *(extended)* | [ICITES](https://www.myhuiban.com/conference/4662) | - | - | - | 2026-09-18 | Hangzhou, China |
| 2026-08-10 *(extended)* | [ICRAE](https://www.myhuiban.com/conference/1779) | - | - | - | 2026-11-20 | Nagoya, Japan |
| 2026-08-10 *(extended)* | [ICRAI](https://www.myhuiban.com/conference/1975) | - | - | - | 2026-12-18 | Songdo, Incheon, Korea |
| 2026-08-10 | [IEEE SSCI](https://www.myhuiban.com/conference/1060) | - | - | - | 2027-02-14 | Queensland, Australia |
| 2026-08-10 *(extended)* | [IMIC](https://www.myhuiban.com/conference/5504) | - | - | - | 2026-08-21 | Chengdu, China |
| 2026-08-10 | [NCIC](https://www.myhuiban.com/conference/4881) | - | - | - | 2026-09-18 | Baotou, China |
| 2026-08-10 *(extended)* | [NLPIR](https://www.myhuiban.com/conference/3024) | - | - | - | 2026-12-11 | Nara, Japan |
| 2026-08-10 | [RSEIT](https://www.myhuiban.com/conference/5541) | - | - | - | 2026-10-16 | Zhangjiajie, China |
| 2026-08-10 | [SETTA](https://www.myhuiban.com/conference/1875) | C | - | - | 2026-12-02 | Singapore |
| 2026-08-10 | [STAIM](https://www.myhuiban.com/conference/5416) | - | - | - | 2026-09-11 | Wuxi, China |
| 2026-08-10 | [WCSP](https://www.myhuiban.com/conference/1946) | - | - | - | 2026-11-12 | Shenzhen, China |
| 2026-08-13 | [AIAC](https://www.myhuiban.com/conference/5002) | - | - | - | 2026-10-28 | Shenzhen, China |
| 2026-08-13 *(extended)* | [ISCSIC](https://www.myhuiban.com/conference/2113) | - | - | - | 2026-09-11 | Nanjing, China |
| 2026-08-13 | [IUI](https://www.myhuiban.com/conference/1409) | B | A | A1 | 2027-02-08 | Helsinki, Finland |
| 2026-08-14 | [AI'](https://www.myhuiban.com/conference/3462) | - | - | - | 2026-12-26 | Dubai, UAE |
| 2026-08-14 | [AIMLNET](https://www.myhuiban.com/conference/4250) | - | - | - | 2026-12-26 | Dubai, UAE |
| 2026-08-14 | [BINLP](https://www.myhuiban.com/conference/4251) | - | - | - | 2026-12-26 | Dubai, UAE |
| 2026-08-14 | [CSTY](https://www.myhuiban.com/conference/3948) | - | - | - | 2026-12-26 | Dubai, UAE |
| 2026-08-14 | [ICCISS](https://www.myhuiban.com/conference/5738) | - | - | - | 2027-01-08 | Uttar Pradesh, India |
| 2026-08-14 | [ICOIP](https://www.myhuiban.com/conference/5674) | - | - | - | 2026-08-28 | Nanjing, China |
| 2026-08-14 | [ITFT](https://www.myhuiban.com/conference/5837) | - | - | - | 2026-10-20 | Glasgow, UK |
| 2026-08-14 | [NATL](https://www.myhuiban.com/conference/2715) | - | - | - | 2026-12-19 | Sydney, Australia |
| 2026-08-15 | [ACINT](https://www.myhuiban.com/conference/5850) | - | - | - | 2026-11-14 | Melbourne, Australia |
| 2026-08-15 *(extended)* | [AIBT](https://www.myhuiban.com/conference/3656) | - | - | - | 2026-11-27 | Shanghai, China |
| 2026-08-15 | [APORS](https://www.myhuiban.com/conference/5717) | - | C | - | 2026-11-20 | Singapore |
| 2026-08-15 | [ASIANComNet](https://www.myhuiban.com/conference/4846) | - | - | - | 2026-10-11 | Hanoi, Vietnam |
| 2026-08-15 | [C2I6](https://www.myhuiban.com/conference/5253) | - | - | - | 2026-12-11 | Bangalore, India |
| 2026-08-15 *(extended)* | [CCCI](https://www.myhuiban.com/conference/3775) | - | - | - | 2026-10-16 | Shanghai, China |
| 2026-08-15 | [CESST](https://www.myhuiban.com/conference/5577) | - | - | - | 2026-12-18 | Zhengzhou, China |
| 2026-08-15 | [COMSAP](https://www.myhuiban.com/conference/5851) | - | - | - | 2026-11-14 | Melbourne, Australia |
| 2026-08-15 *(extended)* | [CRET](https://www.myhuiban.com/conference/4078) | - | - | - | 2026-09-24 | Kristiansand, Norway |
| 2026-08-15 | [CSITAI](https://www.myhuiban.com/conference/5841) | - | - | - | 2026-11-14 | Melbourne, Australia |
| 2026-08-15 *(extended)* | [ComComAp](https://www.myhuiban.com/conference/3111) | - | - | - | 2026-12-14 | Paphos, Cyprus |
| 2026-08-15 *(extended)* | [EDUNINE](https://www.myhuiban.com/conference/5812) | - | - | - | 2027-02-28 | Cochabamba, Bolivia |
| 2026-08-15 | [ESCI](https://www.myhuiban.com/conference/5816) | - | - | - | 2027-03-03 | Pune, India |
| 2026-08-15 *(extended)* | [ICAIP](https://www.myhuiban.com/conference/2494) | - | - | - | 2026-11-27 | Shanghai, China |
| 2026-08-15 | [ICEBE](https://www.myhuiban.com/conference/48) | - | - | B2 | 2026-11-11 |  Wuhan, China |
| 2026-08-15 | [ICEEL](https://www.myhuiban.com/conference/3201) | - | - | - | 2026-11-27 | Tokyo, Japan |
| 2026-08-15 *(extended)* | [ICMME'](https://www.myhuiban.com/conference/5571) | - | - | - | 2026-10-16 | Dalian, China |
| 2026-08-15 | [ICMSC](https://www.myhuiban.com/conference/4676) | - | - | - | 2026-11-22 | Toyama, Japan |
| 2026-08-15 | [ICNC](https://www.myhuiban.com/conference/725) | - | - | - | 2027-02-15 | Honolulu, Hawaii, USA |
| 2026-08-15 | [ICSPS](https://www.myhuiban.com/conference/688) | - | - | - | 2026-10-23 | Xiamen, China |
| 2026-08-15 | [ICVRV](https://www.myhuiban.com/conference/1347) | - | - | - | 2026-12-18 | Valparaiso, Chile |
| 2026-08-15 | [IEEE CIC](https://www.myhuiban.com/conference/1778) | - | - | - | 2026-11-04 | San Jose, California, USA |
| 2026-08-15 | [IEEE CogMI](https://www.myhuiban.com/conference/3916) | - | - | - | 2026-11-04 | San Jose, California, USA |
| 2026-08-15 | [IEEE HONET](https://www.myhuiban.com/conference/2198) | - | - | - | 2026-12-01 | Gazimagusa, Turkiye |
| 2026-08-15 | [IEEE ICCE](https://www.myhuiban.com/conference/1921) | - | - | - | 2027-01-08 | Las Vegas, Nevada, USA |
| 2026-08-15 | [IEEE MedAI](https://www.myhuiban.com/conference/4559) | - | - | - | 2026-11-20 | Zhengzhou, China |
| 2026-08-15 | [IEEE RISC](https://www.myhuiban.com/conference/5559) | - | - | - | 2026-11-04 | San Jose, California, USA |
| 2026-08-15 | [IEEE TPS](https://www.myhuiban.com/conference/3361) | - | - | - | 2026-11-04 | San Jose, California, USA |
| 2026-08-15 | [IRSES](https://www.myhuiban.com/conference/5808) | - | - | - | 2027-02-19 | Gandhinagar, Gujarat, India |
| 2026-08-15 | [ISTECH](https://www.myhuiban.com/conference/5849) | - | - | - | 2026-11-14 | Melbourne, Australia |
| 2026-08-15 | [ITCAU](https://www.myhuiban.com/conference/5838) | - | - | - | 2026-11-14 | Melbourne, Australia |
| 2026-08-15 | [ITEORY](https://www.myhuiban.com/conference/5839) | - | - | - | 2026-11-14 | Melbourne, Australia |
| 2026-08-15 | [Indocrypt](https://www.myhuiban.com/conference/3373) | - | - | - | 2026-12-13 | Bangalore, India |
| 2026-08-15 | [OPTIMA](https://www.myhuiban.com/conference/5755) | - | - | - | 2026-12-04 | Tashkent, Uzbekistan |
| 2026-08-15 | [PES IM](https://www.myhuiban.com/conference/5743) | - | - | - | 2027-01-10 | Beijing, China |
| 2026-08-15 | [iSAI-NLP](https://www.myhuiban.com/conference/2851) | - | - | - | 2026-11-19 | Bangkok, Thailand |
| 2026-08-16 | [ACITY](https://www.myhuiban.com/conference/1363) | - | - | - | 2026-11-27 | Zurich, Switzerland |
| 2026-08-16 | [AIAA](https://www.myhuiban.com/conference/1431) | - | - | - | 2026-11-27 | Zurich, Switzerland |
| 2026-08-16 | [CNDC](https://www.myhuiban.com/conference/2447) | - | - | - | 2026-11-27 | Zurich, Switzerland |
| 2026-08-16 | [DPPR](https://www.myhuiban.com/conference/1432) | - | - | - | 2026-11-27 | Zurich, Switzerland |
| 2026-08-16 | [DSA'](https://www.myhuiban.com/conference/3876) | - | - | - | 2026-11-27 | Zurich, Switzerland |
| 2026-08-16 | [ICSS'](https://www.myhuiban.com/conference/2448) | - | - | - | 2026-11-27 | Zurich, Switzerland |
| 2026-08-16 | [IoTE](https://www.myhuiban.com/conference/3883) | - | - | - | 2026-11-27 | Zurich, Switzerland |
| 2026-08-16 | [MMM](https://www.myhuiban.com/conference/620) | C | B | B1 | 2027-01-05 | Siem Reap, Cambodia |
| 2026-08-16 | [NLPTA](https://www.myhuiban.com/conference/4193) | - | - | - | 2026-11-27 | Zurich, Switzerland |
| 2026-08-16 | [P2PTM](https://www.myhuiban.com/conference/2449) | - | - | - | 2026-11-27 | Zurich, Switzerland |
| 2026-08-16 | [PKC](https://www.myhuiban.com/conference/300) | B | B | A2 | 2027-03-01 | Taipei, Taiwan |
| 2026-08-16 | [VLSI](https://www.myhuiban.com/conference/2451) | - | - | - | 2026-11-27 | Zurich, Switzerland |
| 2026-08-16 | [WeST](https://www.myhuiban.com/conference/2446) | - | - | - | 2026-11-27 | Zurich, Switzerland |
| 2026-08-17 | [WSDM](https://www.myhuiban.com/conference/527) | B | A | B1 | 2027-02-15 | Hong Kong, China |
| 2026-08-18 | [ICCGIV](https://www.myhuiban.com/conference/4436) | - | - | - | 2026-09-18 | Zhenjiang, China |
| 2026-08-18 | [ICoADI](https://www.myhuiban.com/conference/5697) | - | - | - | 2026-10-30 | Zhangjiajie, China |
| 2026-08-19 | [BDCAT](https://www.myhuiban.com/conference/1996) | - | C | - | 2026-12-01 | Florianopolis, Brazil |
| 2026-08-19 | [NDSS](https://www.myhuiban.com/conference/293) | A | A* | A1 | 2027-03-22 | Seoul, South Korea |
| 2026-08-19 | [UCC](https://www.myhuiban.com/conference/443) | - | - | - | 2026-12-01 | Florianopolis, Brazil |
| 2026-08-20 *(extended)* | [ASIG](https://www.myhuiban.com/conference/4883) | - | - | - | 2026-12-04 | Kyoto, Japan |
| 2026-08-20 *(extended)* | [CCISC](https://www.myhuiban.com/conference/5480) | - | - | - | 2026-09-18 | Wuxi, China |
| 2026-08-20 | [CEECT](https://www.myhuiban.com/conference/2816) | - | - | - | 2026-12-17 | Bangkok, Thailand |
| 2026-08-20 | [CSAE](https://www.myhuiban.com/conference/2231) | - | - | - | 2026-10-17 | Shanghai, China |
| 2026-08-20 | [CSAIA](https://www.myhuiban.com/conference/5064) | - | - | - | 2026-12-07 | Online |
| 2026-08-20 | [ICCEA](https://www.myhuiban.com/conference/4648) | - | - | - | 2026-12-26 | Bangkok, Thailand |
| 2026-08-20 | [ICCMME](https://www.myhuiban.com/conference/5191) | - | - | - | 2027-01-08 | Sapporo, Japan |
| 2026-08-20 | [ICMRE](https://www.myhuiban.com/conference/4942) | - | - | - | 2027-03-03 | Grimstad, Norway |
| 2026-08-20 | [ICSGSC](https://www.myhuiban.com/conference/3022) | - | - | - | 2026-12-04 | Guangzhou, China |
| 2026-08-20 | [ICSIE](https://www.myhuiban.com/conference/2458) | - | - | - | 2027-01-15 | Tokyo, Japan |
| 2026-08-20 | [ICSIE'](https://www.myhuiban.com/conference/5380) | - | - | - | 2026-10-07 | Irbid, Jordan |
| 2026-08-20 | [IEIM](https://www.myhuiban.com/conference/5190) | - | - | - | 2027-01-13 | Porto, Portugal |
| 2026-08-20 *(extended)* | [ISCAI](https://www.myhuiban.com/conference/3259) | - | - | - | 2026-10-30 | Zhengzhou, China |
| 2026-08-20 *(extended)* | [MLPR](https://www.myhuiban.com/conference/4998) | - | - | - | 2026-12-04 | Kyoto, Japan |
| 2026-08-20 | [MSN](https://www.myhuiban.com/conference/1769) | C | - | - | 2026-12-18 | Ningbo, China |
| 2026-08-20 *(extended)* | [NAOME](https://www.myhuiban.com/conference/2341) | - | - | - | 2026-09-18 | Guangzhou, China |
| 2026-08-21 | [IEEE BigData](https://www.myhuiban.com/conference/3582) | C | B | - | 2026-12-14 | Phoenix, Arizona, USA |
| 2026-08-21 | [IWCEAA](https://www.myhuiban.com/conference/5120) | - | - | - | 2026-11-06 | Xi an, China |
| 2026-08-22 | [ACOIT](https://www.myhuiban.com/conference/4857) | - | - | - | 2027-01-07 | Karnataka, India |
| 2026-08-22 | [BIBE](https://www.myhuiban.com/conference/485) | - | C | B1 | 2026-11-27 | Shanghai, China |
| 2026-08-22 | [ICCTIT](https://www.myhuiban.com/conference/4902) | - | - | - | 2026-11-06 | Beijing, China |
| 2026-08-22 | [PDCTA](https://www.myhuiban.com/conference/1364) | - | - | - | 2026-11-21 | London, UK |
| 2026-08-22 | [SIPP](https://www.myhuiban.com/conference/1324) | - | - | - | 2026-11-21 | London, UK |
| 2026-08-22 | [SOEN](https://www.myhuiban.com/conference/2995) | - | - | - | 2026-11-21 | London, UK |
| 2026-08-23 *(extended)* | [ICFMCE](https://www.myhuiban.com/conference/2116) | - | - | - | 2026-09-20 | Antalya, Turkiye |
| 2026-08-24 | [VR](https://www.myhuiban.com/conference/550) | A | A* | A2 | 2027-02-27 | Melbourne, Australia |
| 2026-08-25 | [AIAT](https://www.myhuiban.com/conference/4951) | - | - | - | 2026-12-11 | Tokyo, Japan |
| 2026-08-25 *(extended)* | [CEESD](https://www.myhuiban.com/conference/2587) | - | - | - | 2026-10-30 | Tokyo, Japan |
| 2026-08-25 *(extended)* | [IC2UHI](https://www.myhuiban.com/conference/5099) | - | - | - | 2026-09-22 | Nanjing, China |
| 2026-08-25 | [ICCR](https://www.myhuiban.com/conference/4872) | - | - | - | 2026-12-03 | Tokyo, Japan |
| 2026-08-25 *(extended)* | [ICIT''](https://www.myhuiban.com/conference/2996) | - | - | - | 2026-12-11 | Shanghai, China |
| 2026-08-25 | [ICPE'](https://www.myhuiban.com/conference/4646) | - | - | - | 2026-11-20 | Jilin, China |
| 2026-08-25 *(extended)* | [ICVIP](https://www.myhuiban.com/conference/2756) | - | - | - | 2026-12-11 | Shanghai, China |
| 2026-08-25 *(extended)* | [MICAD](https://www.myhuiban.com/conference/3554) | - | - | - | 2026-10-22 | Edinburgh, UK |
| 2026-08-26 | [APSci](https://www.myhuiban.com/conference/5842) | - | - | - | 2026-10-30 | Zhangjiajie, China |
| 2026-08-26 | [ISCTech](https://www.myhuiban.com/conference/4580) | - | - | - | 2026-10-23 | Jiaxing, China |
| 2026-08-26 | [Interdiscipline](https://www.myhuiban.com/conference/5696) | - | - | - | 2026-10-30 | Zhangjiajie, China |
| 2026-08-26 | [MobiCom](https://www.myhuiban.com/conference/104) | A | A* | A1 | 2027-10-18 | to be updated |
| 2026-08-28 | [3DV](https://www.myhuiban.com/conference/1438) | C | - | - | 2027-04-06 | Vancouver, British Columbia, Canada |
| 2026-08-28 | [BDNNDL](https://www.myhuiban.com/conference/5129) | - | - | - | 2026-09-11 | Changji, China |
| 2026-08-28 | [ICISC](https://www.myhuiban.com/conference/714) | - | - | - | 2026-11-18 | Seoul, Korea |
| 2026-08-28 | [ITSSC](https://www.myhuiban.com/conference/5544) | - | - | - | 2026-08-30 | Chongqing, China |
| 2026-08-28 | [WACV](https://www.myhuiban.com/conference/517) | - | A | B1 | 2027-01-04 | Buena Vista, Florida, USA |
| 2026-08-30 | [ACIE](https://www.myhuiban.com/conference/4182) | - | - | - | 2027-01-08 | Osaka, Japan |
| 2026-08-30 | [AEIT](https://www.myhuiban.com/conference/4198) | - | - | - | 2027-01-22 | Osaka, Japan |
| 2026-08-30 | [AIAIS](https://www.myhuiban.com/conference/5791) | - | - | - | 2027-01-22 | Hong Kong, China |
| 2026-08-30 *(extended)* | [AICSP](https://www.myhuiban.com/conference/5540) | - | - | - | 2026-09-18 | Guangzhou, China |
| 2026-08-30 | [AIDL-HCSY](https://www.myhuiban.com/conference/5780) | - | - | - | 2027-01-18 | TIET, Patiala, India |
| 2026-08-30 | [AIHC](https://www.myhuiban.com/conference/5793) | - | - | - | 2027-01-23 | Hyderabad, Telangana, India |
| 2026-08-30 | [APET](https://www.myhuiban.com/conference/5134) | - | - | - | 2026-12-18 | Fuzhou, China |
| 2026-08-30 *(extended)* | [CDSSC](https://www.myhuiban.com/conference/5539) | - | - | - | 2026-09-18 | Guangzhou, China |
| 2026-08-30 *(extended)* | [ICETC](https://www.myhuiban.com/conference/1574) | - | - | B4 | 2026-12-14 | Porto, Portugal |
| 2026-08-30 | [ICNDEMAC](https://www.myhuiban.com/conference/5811) | - | - | - | 2027-02-26 | Nandyal, Andhra Pradesh, India |
| 2026-08-30 | [ICNMS](https://www.myhuiban.com/conference/5192) | - | - | - | 2027-01-20 | Kuala Lumpur, Malaysia |
| 2026-08-30 | [ISCBI](https://www.myhuiban.com/conference/1807) | - | - | - | 2027-02-26 | Macau, China |
| 2026-08-30 | [NICE-TEAS ASIA](https://www.myhuiban.com/conference/5762) | - | - | - | 2026-12-02 | Hanoi, Vietnam |
| 2026-08-30 | [RoEduNet](https://www.myhuiban.com/conference/40) | - | - | - | 2026-11-19 | Iasi, Romania |
| 2026-08-31 | [AMEM](https://www.myhuiban.com/conference/5574) | - | - | - | 2026-12-11 | Wuhan, China |
| 2026-08-31 | [CISES](https://www.myhuiban.com/conference/5764) | - | - | - | 2026-12-03 | Greater Noida, India |
| 2026-08-31 | [COMNETSAT](https://www.myhuiban.com/conference/2004) | - | - | - | 2026-12-03 | Manado, Indonesia |
| 2026-08-31 | [COMSNETS](https://www.myhuiban.com/conference/903) | - | - | - | 2027-01-05 | Bengaluru, India |
| 2026-08-31 | [ICDLT'](https://www.myhuiban.com/conference/5041) | - | - | - | 2026-12-03 | Alcobaca, Portugal |
| 2026-08-31 | [ICEPG](https://www.myhuiban.com/conference/4678) | - | - | - | 2026-12-11 | Xiamen, China |
| 2026-08-31 | [IEEE CRESS](https://www.myhuiban.com/conference/5187) | - | - | - | 2026-10-29 | Nanjing, China |
| 2026-08-31 | [MMAL](https://www.myhuiban.com/conference/5847) | - | - | - | 2027-01-15 | Singapore |
| 2026-08-31 *(extended)* | [RIVF](https://www.myhuiban.com/conference/4479) | - | - | - | 2026-12-18 | Hanoi, Vietnam |
| 2026-09-01 | [APUAVD](https://www.myhuiban.com/conference/5274) | - | - | - | 2026-10-20 | Kyiv, Ukraine |
| 2026-09-01 | [EAAI](https://www.myhuiban.com/conference/5554) | - | - | - | 2027-02-21 | Montreal, Quebec, Canada |
| 2026-09-01 | [IC2NC](https://www.myhuiban.com/conference/5767) | - | - | - | 2026-12-02 | Erode, India |
| 2026-09-01 | [ICCTA](https://www.myhuiban.com/conference/1025) | - | - | B3 | 2026-12-06 | Alexandria, Egypt |
| 2026-09-01 | [ICDSEC](https://www.myhuiban.com/conference/5759) | - | - | - | 2026-12-04 | Ningbo, China |
| 2026-09-01 | [ICIMITAI](https://www.myhuiban.com/conference/5218) | - | - | - | 2026-10-23 | New York City, New York, USA |
| 2026-09-01 | [ICTBIG](https://www.myhuiban.com/conference/5769) | - | - | - | 2026-12-02 | Pradesh, India |
| 2026-09-01 | [ISM](https://www.myhuiban.com/conference/653) | - | C | B2 | 2026-12-07 | Laguna Hills, California, USA |
| 2026-09-01 | [LASCAS](https://www.myhuiban.com/conference/1618) | - | - | B5 | 2027-02-23 | Panama City, Panama |
| 2026-09-02 | [Complex Networks](https://www.myhuiban.com/conference/1057) | - | - | - | 2026-12-02 | Granada, Spain |
| 2026-09-02 | [ITCS](https://www.myhuiban.com/conference/2737) | - | A | - | 2027-01-12 | Berkeley, California, USA |
| 2026-09-03 | [CPP](https://www.myhuiban.com/conference/2298) | - | B | - | 2027-01-10 | Mexico City, Mexico |
| 2026-09-03 | [ICACRS](https://www.myhuiban.com/conference/5768) | - | - | - | 2026-12-02 | Pudukkottai, India |
| 2026-09-03 | [ICDT](https://www.myhuiban.com/conference/140) | B | A | B1 | 2027-04-06 | Lille, France |
| 2026-09-04 *(extended)* | [AC](https://www.myhuiban.com/conference/3724) | - | C | - | 2026-10-24 | Lisbon, Portugal |
| 2026-09-04 | [AICSS](https://www.myhuiban.com/conference/5109) | - | - | - | 2026-09-18 | Beijing, China |
| 2026-09-04 *(extended)* | [AMA21](https://www.myhuiban.com/conference/3560) | - | - | - | 2026-12-16 | Online |
| 2026-09-04 *(extended)* | [CELDA](https://www.myhuiban.com/conference/3725) | - | - | - | 2026-10-24 | Lisbon, Portugal |
| 2026-09-04 | [CFPR](https://www.myhuiban.com/conference/5827) | - | - | - | 2027-03-22 | College Station, Texas, USA |
| 2026-09-04 *(extended)* | [DSDI](https://www.myhuiban.com/conference/5543) | - | - | - | 2026-10-24 | Lisbon, Portugal |
| 2026-09-04 | [ICAHN'](https://www.myhuiban.com/conference/5393) | - | - | - | 2026-09-18 | Haikou, China |
| 2026-09-04 | [ICAISD'](https://www.myhuiban.com/conference/5760) | - | - | - | 2026-12-03 | Bekasi, Indonesia |
| 2026-09-04 | [ICPM](https://www.myhuiban.com/conference/4020) | - | B | - | 2027-02-08 | Rende, Italy |
| 2026-09-04 *(extended)* | [ICWI](https://www.myhuiban.com/conference/3726) | - | - | - | 2026-10-24 | Lisbon, Portugal |
| 2026-09-04 | [PerCom](https://www.myhuiban.com/conference/214) | B | A* | A2 | 2027-03-08 | Goa, India |
| 2026-09-05 | [CIoTSC](https://www.myhuiban.com/conference/4691) | - | - | - | 2026-11-06 | Mianyang, China |
| 2026-09-05 | [ERSGIT](https://www.myhuiban.com/conference/4917) | - | - | - | 2026-09-19 | Nanjing, China |
| 2026-09-05 | [GIRST](https://www.myhuiban.com/conference/4979) | - | - | - | 2026-11-20 | Nanjing, China |
| 2026-09-05 | [ICAMR](https://www.myhuiban.com/conference/3396) | - | - | - | 2027-01-23 | Phuket, Thailand |
| 2026-09-05 *(extended)* | [ICCDA'](https://www.myhuiban.com/conference/2897) | - | - | - | 2026-12-18 | Phuket, Thailand |
| 2026-09-05 | [IPMF](https://www.myhuiban.com/conference/5840) | - | - | - | 2026-11-20 | Xi an, China |
| 2026-09-05 | [JURIX](https://www.myhuiban.com/conference/5694) | - | C | - | 2026-12-08 | Toulouse, France |
| 2026-09-05 | [NGDN](https://www.myhuiban.com/conference/4770) | - | - | - | 2026-11-20 | Shenyang, China |
| 2026-09-06 | [AEEGE](https://www.myhuiban.com/conference/4306) | - | - | - | 2026-11-06 | Hohhot, China |
| 2026-09-06 | [ICCESC](https://www.myhuiban.com/conference/5114) | - | - | - | 2026-11-06 | Nanning, China |
| 2026-09-07 | [DATE](https://www.myhuiban.com/conference/216) | B | A | A1 | 2027-03-22 | Dresden, Germany |
| 2026-09-07 | [FRUCT](https://www.myhuiban.com/conference/3653) | - | - | - | 2026-11-04 | Helsinki, Finland |
| 2026-09-07 | [ICBAIE](https://www.myhuiban.com/conference/5119) | - | - | - | 2026-11-20 | Xi an, China |
| 2026-09-09 | [ASPLOS](https://www.myhuiban.com/conference/322) | A | A* | A1 | 2027-04-11 | Heraklion, Crete, Greece |
| 2026-09-09 | [ISSCC](https://www.myhuiban.com/conference/713) | - | - | B1 | 2027-02-14 | San Francisco, California, USA |
| 2026-09-10 *(extended)* | [ADMIT](https://www.myhuiban.com/conference/4378) | - | - | - | 2026-10-16 | Wuhan, China |
| 2026-09-10 | [AISSA](https://www.myhuiban.com/conference/5845) | - | - | - | 2026-12-08 | San Antonio, Texas, USA |
| 2026-09-10 *(extended)* | [BDIOT'](https://www.myhuiban.com/conference/3602) | - | - | - | 2026-10-23 | Shanghai, China |
| 2026-09-10 *(extended)* | [CCBDIoT](https://www.myhuiban.com/conference/4379) | - | - | - | 2026-10-16 | Wuhan, China |
| 2026-09-10 | [CGO](https://www.myhuiban.com/conference/345) | B | A | A2 | 2027-01-31 | Salt Lake City, Utah, USA |
| 2026-09-10 | [CHI](https://www.myhuiban.com/conference/961) | A | A* | A1 | 2027-05-10 | Pittsburgh, Pennsylvania, USA |
| 2026-09-10 | [DRAS](https://www.myhuiban.com/conference/5843) | - | - | - | 2026-12-08 | San Antonio, Texas, USA |
| 2026-09-10 | [FICN](https://www.myhuiban.com/conference/5844) | - | - | - | 2026-12-08 | San Antonio, Texas, USA |
| 2026-09-10 *(extended)* | [ICACR](https://www.myhuiban.com/conference/2330) | - | - | - | 2026-10-16 | Nanjing, China |
| 2026-09-10 | [ICKEM](https://www.myhuiban.com/conference/2907) | - | - | - | 2027-03-09 | Naples, Italy |
| 2026-09-10 | [ICSCA](https://www.myhuiban.com/conference/2809) | - | - | - | 2027-01-22 | Putrajaya, Malaysia |
| 2026-09-10 | [ISDDC'](https://www.myhuiban.com/conference/5260) | - | - | - | 2026-11-20 | Lucknow, India |
| 2026-09-10 | [ITAIC](https://www.myhuiban.com/conference/67) | - | - | - | 2026-12-04 | Chongqing, China |
| 2026-09-10 | [KST](https://www.myhuiban.com/conference/2034) | - | - | - | 2027-03-17 | Tokyo, Japan |
| 2026-09-10 | [Mechatronika](https://www.myhuiban.com/conference/5256) | - | - | - | 2026-12-02 | Prague, Czech Republic |
| 2026-09-10 | [NSDI](https://www.myhuiban.com/conference/303) | A | - | A1 | 2027-05-11 | Providence, Rhode Island, USA |
| 2026-09-11 | [ADC](https://www.myhuiban.com/conference/4556) | - | B | - | 2026-12-15 | Brisbane, Australia |
| 2026-09-11 | [AHPCAI](https://www.myhuiban.com/conference/4607) | - | - | - | 2026-11-20 | Zhengzhou, China |
| 2026-09-11 | [AIHI](https://www.myhuiban.com/conference/5758) | - | - | - | 2026-12-04 | Changchun, China |
| 2026-09-11 | [ALTA](https://www.myhuiban.com/conference/5592) | - | C | - | 2026-11-30 | Melbourne, Australia |
| 2026-09-11 | [EECCT](https://www.myhuiban.com/conference/5545) | - | - | - | 2026-09-13 | Yibin, China |
| 2026-09-11 *(extended)* | [SLT](https://www.myhuiban.com/conference/5581) | C | - | - | 2026-12-13 | Palermo, Sicily, Italy |
| 2026-09-11 | [SeHAS](https://www.myhuiban.com/conference/5724) | - | - | - | 2027-01-18 | Glasgow, Scotland, UK |
| 2026-09-12 | [ICACAR](https://www.myhuiban.com/conference/2343) | - | - | - | 2027-03-19 | Jinan, China |
| 2026-09-12 | [ISCEIC](https://www.myhuiban.com/conference/4397) | - | - | - | 2026-11-27 | Chongqing, China |
| 2026-09-13 | [CEII](https://www.myhuiban.com/conference/4636) | - | - | - | 2026-12-11 | Shenzhen, China |
| 2026-09-13 | [ENTER](https://www.myhuiban.com/conference/5654) | - | C | - | 2027-01-12 | Madrid, Spain |
| 2026-09-15 *(extended)* | [ACFPE](https://www.myhuiban.com/conference/4249) | - | - | - | 2026-10-22 | Chengdu, China |
| 2026-09-15 | [BIODEVICES](https://www.myhuiban.com/conference/2859) | - | - | - | 2027-02-19 | Valletta, Malta |
| 2026-09-15 | [BIOIMAGING](https://www.myhuiban.com/conference/2891) | - | - | - | 2027-02-19 | Valletta, Malta |
| 2026-09-15 | [BIOINFORMATICS](https://www.myhuiban.com/conference/2892) | - | - | - | 2027-02-19 | Valletta, Malta |
| 2026-09-15 | [BIOSIGNALS](https://www.myhuiban.com/conference/2893) | - | - | - | 2027-02-19 | Valletta, Malta |
| 2026-09-15 | [BIOSTEC](https://www.myhuiban.com/conference/3349) | - | - | - | 2027-02-19 | Valletta, Malta |
| 2026-09-15 | [FAST](https://www.myhuiban.com/conference/323) | A | A | A1 | 2027-02-23 | Renton, Washington, USA |
| 2026-09-15 | [GRIVAPP](https://www.myhuiban.com/conference/5451) | - | - | - | 2027-02-26 | Valletta, Malta |
| 2026-09-15 | [HEALTHINF](https://www.myhuiban.com/conference/3350) | - | - | - | 2027-02-19 | Valletta, Malta |
| 2026-09-15 *(extended)* | [IARCE](https://www.myhuiban.com/conference/2115) | - | - | - | 2026-11-13 | Hangzhou, China |
| 2026-09-15 | [ICAART](https://www.myhuiban.com/conference/371) | - | B | B4 | 2027-02-23 | Valletta, Malta |
| 2026-09-15 | [ICAMEM](https://www.myhuiban.com/conference/2566) | - | - | - | 2026-12-18 | Singapore |
| 2026-09-15 | [ICCT-Pacific](https://www.myhuiban.com/conference/5828) | - | - | - | 2027-03-27 | Okayama, Japan |
| 2026-09-15 | [ICICAIEECE](https://www.myhuiban.com/conference/5788) | - | - | - | 2027-01-21 | KOLLAM, India |
| 2026-09-15 | [ICISCC](https://www.myhuiban.com/conference/5615) | - | - | - | 2026-11-20 | Changsha, China |
| 2026-09-15 | [ICISSP](https://www.myhuiban.com/conference/1772) | - | C | - | 2027-02-22 | Valletta, Malta |
| 2026-09-15 | [ICORES](https://www.myhuiban.com/conference/2849) | - | C | - | 2027-02-20 | Valletta, Malta |
| 2026-09-15 | [ICPRAM](https://www.myhuiban.com/conference/2853) | - | C | - | 2027-02-20 | Valletta, Malta |
| 2026-09-15 | [ISCC'](https://www.myhuiban.com/conference/2405) | - | - | - | 2026-11-20 | Guangzhou, China |
| 2026-09-15 | [JHICON](https://www.myhuiban.com/conference/5802) | - | - | - | 2027-02-02 | Jharkhand, India |
| 2026-09-15 | [MODELSWARD](https://www.myhuiban.com/conference/2889) | - | C | - | 2027-02-19 | Valletta, Malta |
| 2026-09-15 | [PHOTOPTICS](https://www.myhuiban.com/conference/5630) | - | - | - | 2027-02-25 | Valletta, Malta |
| 2026-09-15 | [ROBOVIS](https://www.myhuiban.com/conference/4877) | - | - | - | 2027-02-27 | Valletta, Malta |
| 2026-09-15 | [SOFSEM](https://www.myhuiban.com/conference/997) | - | B | B1 | 2027-02-02 | Ioannina, Greece |
| 2026-09-15 | [VISAPP](https://www.myhuiban.com/conference/657) | - | - | B3 | 2027-02-26 | Valletta, Malta |
| 2026-09-15 | [WCNC](https://www.myhuiban.com/conference/316) | C | B | A2 | 2027-04-05 | Panama City, Panama |
| 2026-09-16 | [ICASSP](https://www.myhuiban.com/conference/429) | B | - | A1 | 2027-05-16 | Toronto, Ontario, Canada |
| 2026-09-16 | [IMCOM](https://www.myhuiban.com/conference/1553) | - | - | - | 2027-01-04 | Taipei, Taiwan |
| 2026-09-16 | [VMCAI](https://www.myhuiban.com/conference/217) | B | B | A2 | 2027-01-11 | Mexico City, Mexico |
| 2026-09-17 | [AIxVR](https://www.myhuiban.com/conference/2790) | - | - | - | 2027-01-25 | Vancouver, British Columbia, Canada |
| 2026-09-17 | [BDDM](https://www.myhuiban.com/conference/4959) | - | - | - | 2026-11-27 | Changsha, China |
| 2026-09-17 | [EuroSys](https://www.myhuiban.com/conference/199) | A | A | A2 | 2027-04-19 | Rabat, Morocco |
| 2026-09-17 | [Eurocrypt](https://www.myhuiban.com/conference/294) | A | A* | A1 | 2027-04-11 | Eindhoven, the Netherlands |
| 2026-09-17 | [FC](https://www.myhuiban.com/conference/966) | C | A | B1 | 2027-02-08 | Barbados |
| 2026-09-17 | [ISQED](https://www.myhuiban.com/conference/558) | - | - | B1 | 2027-04-14 | San Francisco, California, USA |
| 2026-09-18 | [CCPCDL](https://www.myhuiban.com/conference/4196) | - | - | - | 2026-09-28 | Nantong, China |
| 2026-09-18 *(extended)* | [CEVVE](https://www.myhuiban.com/conference/4028) | - | - | - | 2026-10-16 | Fuzhou, China |
| 2026-09-18 | [HRI](https://www.myhuiban.com/conference/472) | - | A* | A2 | 2027-03-08 | Santa Clara, California, USA |
| 2026-09-18 *(extended)* | [ICAUAS](https://www.myhuiban.com/conference/4757) | - | - | - | 2026-10-16 | Shanghai, China |
| 2026-09-18 | [ICBSR](https://www.myhuiban.com/conference/5647) | - | - | - | 2026-12-25 | Xiamen, China |
| 2026-09-18 | [ICCBD+AI](https://www.myhuiban.com/conference/4989) | - | - | - | 2026-11-20 | Fuzhou, China |
| 2026-09-18 | [ICCBD+AI](https://www.myhuiban.com/conference/4989) | - | - | - | 2026-11-20 | Fuzhou, China |
| 2026-09-18 | [ICOIN](https://www.myhuiban.com/conference/718) | - | - | B1 | 2027-01-13 | Nha Trang, Vietnam |
| 2026-09-18 | [IPOR](https://www.myhuiban.com/conference/5126) | - | - | - | 2026-11-27 | Kuala Lumpur, Malaysia |
| 2026-09-18 | [UT](https://www.myhuiban.com/conference/4988) | - | - | - | 2027-02-28 | Tokyo, Japan |
| 2026-09-19 | [EEICE](https://www.myhuiban.com/conference/5757) | - | - | - | 2026-12-04 | Xinxiang, China |
| 2026-09-19 | [ISPCT](https://www.myhuiban.com/conference/5753) | - | - | - | 2026-12-04 | Dongguan, China |
| 2026-09-20 | [ACRA](https://www.myhuiban.com/conference/5590) | - | C | - | 2026-11-30 | Canberra, Australia |
| 2026-09-20 | [AIGC](https://www.myhuiban.com/conference/4601) | - | - | - | 2026-12-26 | Guangzhou, China |
| 2026-09-20 | [AIHCIR](https://www.myhuiban.com/conference/4695) | - | - | - | 2026-11-20 | Urumqi, China |
| 2026-09-20 | [CCEAI](https://www.myhuiban.com/conference/2629) | - | - | - | 2027-01-21 | Shanghai, China |
| 2026-09-20 *(extended)* | [ICCFI](https://www.myhuiban.com/conference/2487) | - | - | - | 2026-10-29 | Paris, France |
| 2026-09-20 | [ICEEICT](https://www.myhuiban.com/conference/5795) | - | - | - | 2027-01-28 | Dhaka, Bangladesh |
| 2026-09-20 | [ICMWIA](https://www.myhuiban.com/conference/5801) | - | - | - | 2027-02-02 | Lisbon, Portugal |
| 2026-09-20 *(extended)* | [ICRSA](https://www.myhuiban.com/conference/3084) | - | - | - | 2026-10-30 | Huizhou, China |
| 2026-09-20 *(extended)* | [ICVRT](https://www.myhuiban.com/conference/3056) | - | - | - | 2026-12-25 | Harbin, China |
| 2026-09-20 | [IVSP](https://www.myhuiban.com/conference/2971) | - | - | - | 2027-03-03 | Sapporo, Japan |
| 2026-09-20 *(extended)* | [MCVR](https://www.myhuiban.com/conference/4884) | - | - | - | 2026-12-25 | Harbin, China |
| 2026-09-20 | [MLHMI](https://www.myhuiban.com/conference/3578) | - | - | - | 2027-03-03 | Sapporo, Japan |
| 2026-09-20 | [RDINIDR](https://www.myhuiban.com/conference/1811) | - | - | - | 2026-10-13 | Madrid, Spain |
| 2026-09-21 | [ECIR](https://www.myhuiban.com/conference/159) | C | A | A2 | 2027-03-21 | Southampton, UK |
| 2026-09-21 | [GARFIIELD](https://www.myhuiban.com/conference/5102) | - | - | - | 2026-10-15 | Madrid, Spain |
| 2026-09-21 | [ISPD](https://www.myhuiban.com/conference/557) | C | - | A2 | 2027-03-31 | Taipei, Taiwan |
| 2026-09-21 | [SANER](https://www.myhuiban.com/conference/1922) | B | A | - | 2027-03-09 | Richmond, Virginia, USA |
| 2026-09-23 *(extended)* | [ICVISP](https://www.myhuiban.com/conference/2111) | - | - | - | 2026-12-11 | Haikou, China |
| 2026-09-25 | [CSNT](https://www.myhuiban.com/conference/2166) | - | - | - | 2027-03-12 | Khajuraho, Gwalior, India |
| 2026-09-25 | [Eurographics](https://www.myhuiban.com/conference/271) | B | - | A2 | 2027-05-10 | Lucca, Italy |
| 2026-09-25 | [ICCAID](https://www.myhuiban.com/conference/4507) | - | - | - | 2026-10-11 | Nanchang, China |
| 2026-09-25 | [ICCDE'](https://www.myhuiban.com/conference/2332) | - | - | - | 2027-02-17 | Phuket, Thailand |
| 2026-09-25 | [ICMLC](https://www.myhuiban.com/conference/1375) | - | - | B4 | 2027-02-26 | Shenzhen, China |
| 2026-09-25 | [ICRAIC](https://www.myhuiban.com/conference/4200) | - | - | - | 2026-11-27 | Xi an, China |
| 2026-09-25 *(extended)* | [ICRCV](https://www.myhuiban.com/conference/4847) | - | - | - | 2026-11-06 | Jiangyin, China |
| 2026-09-25 | [ICRIC](https://www.myhuiban.com/conference/5565) | - | - | - | 2027-02-17 | Milan, Italy |
| 2026-09-25 *(extended)* | [ICSTTE](https://www.myhuiban.com/conference/2097) | - | - | - | 2026-10-30 | Weihai, China |
| 2026-09-25 *(extended)* | [ICoCTA](https://www.myhuiban.com/conference/3382) | - | - | - | 2026-10-23 | Qingdao, China |
| 2026-09-25 | [ISEC](https://www.myhuiban.com/conference/2884) | - | - | - | 2027-02-18 | Mumbai, India |
| 2026-09-26 | [CITCE](https://www.myhuiban.com/conference/4447) | - | - | - | 2026-12-11 | Suzhou, China |
| 2026-09-26 | [ICNGN](https://www.myhuiban.com/conference/4459) | - | - | - | 2026-12-12 | Hong Kong, China |
| 2026-09-26 | [ICSE''](https://www.myhuiban.com/conference/4903) | - | - | - | 2026-12-11 | Shenzhen, China |
| 2026-09-26 | [IRAC](https://www.myhuiban.com/conference/5121) | - | - | - | 2026-12-11 | Hangzhou, China |
| 2026-09-28 | [BDMLIC](https://www.myhuiban.com/conference/5546) | - | - | - | 2026-09-30 | Shenzhen, China |
| 2026-09-28 | [EMO](https://www.myhuiban.com/conference/5714) | - | - | - | 2027-04-05 | Exeter, UK |
| 2026-09-28 | [ICBCTIS](https://www.myhuiban.com/conference/4038) | - | - | - | 2026-12-04 | Zhengzhou, China |
| 2026-09-30 | [ACIIDS](https://www.myhuiban.com/conference/5616) | - | B | - | 2027-04-05 | Bali, Indonesia |
| 2026-09-30 *(extended)* | [AI2A](https://www.myhuiban.com/conference/3995) | - | - | - | 2026-10-23 | Wuxi, China |
| 2026-09-30 *(extended)* | [AIBDCC](https://www.myhuiban.com/conference/5505) | - | - | - | 2026-10-30 | Chengdu, China |
| 2026-09-30 | [AIEI](https://www.myhuiban.com/conference/5785) | - | - | - | 2027-01-21 | Bengaluru, India |
| 2026-09-30 | [BigComp](https://www.myhuiban.com/conference/1407) | - | - | - | 2027-01-25 | Fukuoka, Japan |
| 2026-09-30 *(extended)* | [CCNML](https://www.myhuiban.com/conference/4338) | - | - | - | 2026-10-23 | Wuxi, China |
| 2026-09-30 *(extended)* | [ICAIRS](https://www.myhuiban.com/conference/5558) | - | - | - | 2026-10-23 | Tianjin, China |
| 2026-09-30 | [ICCMB](https://www.myhuiban.com/conference/3534) | - | - | - | 2027-02-18 | Basel, Switzerland |
| 2026-09-30 | [ICCRD](https://www.myhuiban.com/conference/4888) | - | - | - | 2027-01-15 | Singapore |
| 2026-09-30 | [ICETCS](https://www.myhuiban.com/conference/5805) | - | - | - | 2027-02-11 | Bengaluru, India |
| 2026-09-30 | [ICICF](https://www.myhuiban.com/conference/5787) | - | - | - | 2027-01-21 | Bengaluru, India |
| 2026-09-30 | [ICIIT](https://www.myhuiban.com/conference/2349) | - | - | - | 2027-03-04 | Ho Chi Minh City, Vietnam |
| 2026-09-30 | [ICMLSC](https://www.myhuiban.com/conference/2975) | - | - | - | 2027-01-29 | Tokyo, Japan |
| 2026-09-30 | [ICSCM](https://www.myhuiban.com/conference/5204) | - | - | - | 2027-02-18 | Basel, Switzerland |
| 2026-09-30 | [ICTACS](https://www.myhuiban.com/conference/5765) | - | - | - | 2026-12-03 | Tashkent, Uzbekistan |
| 2026-09-30 | [IEEE Satellite](https://www.myhuiban.com/conference/4366) | - | - | - | 2026-11-14 | Hainan, China |
| 2026-09-30 | [IITCEE](https://www.myhuiban.com/conference/4966) | - | - | - | 2027-01-21 | Bengaluru, India |
| 2026-09-30 | [ISAS](https://www.myhuiban.com/conference/4901) | - | - | - | 2026-12-04 | Ankara, Turkiye |
| 2026-09-30 | [ISCIPT](https://www.myhuiban.com/conference/5023) | - | - | - | 2026-11-13 | Fushun, China |
| 2026-09-30 | [MLCC](https://www.myhuiban.com/conference/5564) | - | - | - | 2027-03-19 | Chongqing, China |
| 2026-09-30 | [NPSPE](https://www.myhuiban.com/conference/5575) | - | - | - | 2026-12-25 | Harbin, China |
| 2026-09-30 | [NQComp](https://www.myhuiban.com/conference/5789) | - | - | - | 2027-01-21 | Bengaluru, India |
| 2026-09-30 *(extended)* | [PEESE](https://www.myhuiban.com/conference/5506) | - | - | - | 2026-10-31 | Chengdu, China |
| 2026-09-30 *(extended)* | [PEPSC](https://www.myhuiban.com/conference/4528) | - | - | - | 2026-11-02 | Cairo, Egypt |
| 2026-09-30 | [WcAISR](https://www.myhuiban.com/conference/5786) | - | - | - | 2027-01-21 | Mohali, Punjab, India |
| 2026-10-01 | [ArtInHCI](https://www.myhuiban.com/conference/4625) | - | - | - | 2026-10-16 | Wuhan, China |
| 2026-10-01 | [ICACT](https://www.myhuiban.com/conference/1682) | - | - | - | 2027-01-24 | Phoenix Park, PyeongChang, Korea |
| 2026-10-01 | [ICAIIC](https://www.myhuiban.com/conference/2925) | - | - | - | 2027-02-22 | Osaka, Japan |
| 2026-10-01 | [ICARA](https://www.myhuiban.com/conference/1587) | - | - | - | 2027-02-25 | Paris, France |
| 2026-10-01 | [ICICIP](https://www.myhuiban.com/conference/827) | - | - | - | 2027-02-08 | Vientiane and Luang Prabang, Laos |
| 2026-10-01 | [ICIMPACT](https://www.myhuiban.com/conference/5803) | - | - | - | 2027-02-03 | Bandung, Indonesia |
| 2026-10-01 | [SMC-IoT](https://www.myhuiban.com/conference/4702) | - | - | - | 2026-12-04 | Jiaozuo, China |
| 2026-10-01 | [SPCT](https://www.myhuiban.com/conference/4461) | - | - | - | 2026-12-18 | Shenzhen, China |
| 2026-10-01 | [iEECON](https://www.myhuiban.com/conference/5817) | - | - | - | 2027-03-03 | Rayong, Thailand |
| 2026-10-02 | [ASIM](https://www.myhuiban.com/conference/5097) | - | - | - | 2026-12-04 | Chongqing, China |
| 2026-10-02 | [DCC](https://www.myhuiban.com/conference/617) | B | B | A2 | 2027-03-23 | Snowbird, Utah, USA |
| 2026-10-02 | [EDCC](https://www.myhuiban.com/conference/1404) | - | - | B2 | 2027-04-06 | Trondheim, Norway |
| 2026-10-02 | [FSE](https://www.myhuiban.com/conference/87) | A | A* | A1 | 2027-07-12 | Shenzhen, China |
| 2026-10-02 | [FTTE](https://www.myhuiban.com/conference/5157) | - | - | - | 2026-10-16 | Xiangyang, China |
| 2026-10-02 | [ICC](https://www.myhuiban.com/conference/318) | C | - | A2 | 2027-05-30 | Washington DC, USA |
| 2026-10-02 | [ICN'](https://www.myhuiban.com/conference/4624) | - | - | - | 2026-10-16 | Changzhou, China |
| 2026-10-02 | [SAC'](https://www.myhuiban.com/conference/218) | - | - | A1 | 2027-04-05 | Gwangju, South Korea |
| 2026-10-03 | [ICHBC](https://www.myhuiban.com/conference/4450) | - | - | - | 2026-12-18 | Nanchang, China |
| 2026-10-03 | [ISNEET](https://www.myhuiban.com/conference/5169) | - | - | - | 2026-12-18 | Weihai, China |
| 2026-10-04 | [AISEE](https://www.myhuiban.com/conference/5790) | - | - | - | 2027-01-22 | Mangaluru, India |
| 2026-10-05 | [CSP](https://www.myhuiban.com/conference/3334) | - | - | - | 2027-03-27 | Nagoya, Japan |
| 2026-10-05 | [ICCSMT](https://www.myhuiban.com/conference/3964) | - | - | - | 2026-12-25 | Chengdu, China |
| 2026-10-05 | [ICINT](https://www.myhuiban.com/conference/2388) | - | - | - | 2027-03-05 | Melbourne, Australia |
| 2026-10-05 | [ICMIP](https://www.myhuiban.com/conference/3335) | - | - | - | 2027-03-27 | Nagoya, Japan |
| 2026-10-05 *(extended)* | [ICMRA](https://www.myhuiban.com/conference/3697) | - | - | - | 2026-11-13 | Suzhou, China |
| 2026-10-05 | [MLCIPR](https://www.myhuiban.com/conference/5147) | - | - | - | 2026-12-25 | Nanjing, China |
| 2026-10-06 | [EPSEE](https://www.myhuiban.com/conference/4307) | - | - | - | 2026-11-06 | Hohhot, China |
| 2026-10-07 | [EDBT](https://www.myhuiban.com/conference/139) | B | B | A2 | 2027-04-06 | Lille, France |
| 2026-10-08 *(extended)* | [CFEEE](https://www.myhuiban.com/conference/3424) | - | - | - | 2026-11-06 | Shanghai, China |
| 2026-10-08 | [CHIIR](https://www.myhuiban.com/conference/1827) | - | B | - | 2027-03-07 | Berlin, Germany |
| 2026-10-08 | [ICAUC](https://www.myhuiban.com/conference/5781) | - | - | - | 2027-01-18 | Pathum Thani, Thailand |
| 2026-10-08 *(extended)* | [JCRAI](https://www.myhuiban.com/conference/2514) | - | - | - | 2026-11-06 | Beijing, China |
| 2026-10-09 | [EIRIS](https://www.myhuiban.com/conference/5551) | - | - | - | 2026-10-23 | Wenzhou, China |
| 2026-10-09 | [HotMobile](https://www.myhuiban.com/conference/608) | - | - | B2 | 2027-02-24 | Tucson, Arizona |
| 2026-10-09 | [ISEAE](https://www.myhuiban.com/conference/4047) | - | - | - | 2027-04-23 | Harbin, China |
| 2026-10-09 | [IWIPP](https://www.myhuiban.com/conference/5813) | - | - | - | 2027-02-28 | Kitakyushu, Japan |
| 2026-10-09 | [MHV](https://www.myhuiban.com/conference/4230) | - | - | - | 2027-02-23 | Denver, Colorado, USA |
| 2026-10-10 | [AAIML](https://www.myhuiban.com/conference/5829) | - | - | - | 2027-03-29 | Tokyo, Japan |
| 2026-10-10 | [AIxDKE](https://www.myhuiban.com/conference/2770) | - | - | - | 2027-02-01 | Laguna Hills, California, USA |
| 2026-10-10 | [BDAMEA](https://www.myhuiban.com/conference/5118) | - | - | - | 2026-12-25 | Suzhou, China |
| 2026-10-10 | [CTIEET](https://www.myhuiban.com/conference/4617) | - | - | - | 2026-12-25 | Harbin, China |
| 2026-10-10 | [EIECC](https://www.myhuiban.com/conference/5225) | - | - | - | 2026-12-25 | Guangzhou, China |
| 2026-10-10 | [ICIBE](https://www.myhuiban.com/conference/4873) | - | - | - | 2027-03-19 | Hong Kong, China |
| 2026-10-10 | [ICMSS](https://www.myhuiban.com/conference/3394) | - | - | - | 2027-03-19 | Hong Kong, China |
| 2026-10-10 | [ICSC](https://www.myhuiban.com/conference/230) | - | - | B2 | 2027-02-01 | Laguna Hills, California, USA |
| 2026-10-10 | [IFIP WG 11.9](https://www.myhuiban.com/conference/1497) | C | - | - | 2027-01-07 | New Delhi, India |
| 2026-10-10 *(extended)* | [ISCMI](https://www.myhuiban.com/conference/2634) | - | - | - | 2026-11-18 | Vienna, Austria |
| 2026-10-10 | [MLAIA](https://www.myhuiban.com/conference/5201) | - | - | - | 2026-12-18 | Nanning, China |
| 2026-10-10 | [SICE ISCS](https://www.myhuiban.com/conference/5815) | - | - | - | 2027-03-02 | Tokyo, Japan |
| 2026-10-10 | [SIGMOD](https://www.myhuiban.com/conference/133) | A | A* | A1 | 2027-06-13 | Huntington Beach, California, USA |
| 2026-10-10 | [SPRA](https://www.myhuiban.com/conference/5246) | - | - | - | 2027-03-03 | Tokyo, Japan |
| 2026-10-11 | [STACS](https://www.myhuiban.com/conference/389) | C | A | A2 | 2027-03-08 | Gottingen, Germany |
| 2026-10-11 | [The Web Conference](https://www.myhuiban.com/conference/137) | A | A* | A1 | 2027-05-10 | Dublin, Ireland |
| 2026-10-12 | [ICIT](https://www.myhuiban.com/conference/743) | - | - | B3 | 2027-03-15 | Florianopolis, Brazil |
| 2026-10-12 | [NAACL](https://www.myhuiban.com/conference/426) | B | A | A1 | 2027-06-01 | San Francisco, California, USA |
| 2026-10-13 | [IC-EISIT](https://www.myhuiban.com/conference/5471) | - | - | - | 2026-10-23 | Guangzhou, China |
| 2026-10-13 | [ISCAS](https://www.myhuiban.com/conference/340) | B | C | A1 | 2027-06-06 | Bordeaux, France |
| 2026-10-13 *(extended)* | [PSETC](https://www.myhuiban.com/conference/5024) | - | - | - | 2026-11-13 | Singapore |
| 2026-10-15 | [EMC²](https://www.myhuiban.com/conference/5737) | - | - | - | 2027-01-08 | Shenzhen, China |
| 2026-10-15 | [ESOP](https://www.myhuiban.com/conference/200) | - | A | A2 | 2027-04-10 | Copenhagen, Denmark |
| 2026-10-15 | [ETAPS](https://www.myhuiban.com/conference/768) | B | - | - | 2027-04-10 | Copenhagen, Denmark |
| 2026-10-15 | [FoSSaCS](https://www.myhuiban.com/conference/202) | - | B | A2 | 2027-04-10 | Copenhagen, Denmark |
| 2026-10-15 | [ICCR'](https://www.myhuiban.com/conference/5751) | - | - | - | 2026-12-06 | Irbid, Jordan |
| 2026-10-15 | [ICCVIT](https://www.myhuiban.com/conference/4909) | - | - | - | 2026-12-18 | Beijing, China |
| 2026-10-15 | [ICECC](https://www.myhuiban.com/conference/679) | - | - | - | 2027-03-18 | Tokyo, Japan |
| 2026-10-15 | [ICEDS](https://www.myhuiban.com/conference/5400) | - | - | - | 2027-04-15 | Glasgow, UK |
| 2026-10-15 | [ICFST](https://www.myhuiban.com/conference/3232) | - | - | - | 2027-03-18 | Tokyo, Japan |
| 2026-10-15 | [TACAS](https://www.myhuiban.com/conference/203) | - | A | A1 | 2027-04-10 | Copenhagen, Denmark |
| 2026-10-15 | [iFS](https://www.myhuiban.com/conference/5527) | - | - | - | 2027-04-10 | Copenhagen, Denmark |
| 2026-10-16 | [ICDM''](https://www.myhuiban.com/conference/5132) | - | - | - | 2026-10-30 | Changchun, China |
| 2026-10-16 | [ICFTIC](https://www.myhuiban.com/conference/3312) | - | - | - | 2026-10-30 | Qingdao, China |
| 2026-10-16 | [ICHIH](https://www.myhuiban.com/conference/4679) | - | - | - | 2026-12-25 | Hangzhou, China |
| 2026-10-16 | [MMLDS](https://www.myhuiban.com/conference/5507) | - | - | - | 2026-10-30 | Zhengzhou, China |
| 2026-10-17 | [SCIBT](https://www.myhuiban.com/conference/5823) | - | - | - | 2027-03-17 | Muscat, Oman |
| 2026-10-18 | [ICIMCIS](https://www.myhuiban.com/conference/5770) | - | - | - | 2026-12-02 | Jakarta, Indonesia |
| 2026-10-19 | [FSEN](https://www.myhuiban.com/conference/1976) | - | - | - | 2027-05-24 | Enschede, Netherlands |
| 2026-10-20 *(extended)* | [ACEPE](https://www.myhuiban.com/conference/4822) | - | - | - | 2026-11-20 | Sanya, China |
| 2026-10-20 | [CCISP](https://www.myhuiban.com/conference/2586) | - | - | - | 2026-11-19 | Hefei, China |
| 2026-10-20 *(extended)* | [CDICS](https://www.myhuiban.com/conference/4563) | - | - | - | 2026-11-27 | Singapore |
| 2026-10-20 | [CEAC](https://www.myhuiban.com/conference/4485) | - | - | - | 2027-03-10 | Hanoi, Vietnam |
| 2026-10-20 | [DASIP](https://www.myhuiban.com/conference/1722) | - | - | - | 2027-01-18 | Glasgow, Scotland, UK |
| 2026-10-20 *(extended)* | [DSIS](https://www.myhuiban.com/conference/2987) | - | - | - | 2026-11-20 | Hangzhou, China |
| 2026-10-20 | [IC4E](https://www.myhuiban.com/conference/3398) | - | - | - | 2027-03-26 | Fukuoka, Japan |
| 2026-10-20 | [ICBCB](https://www.myhuiban.com/conference/4943) | - | - | - | 2027-03-26 | Xi an, China |
| 2026-10-20 *(extended)* | [ICBDAA](https://www.myhuiban.com/conference/4637) | - | - | - | 2026-11-27 | Singapore |
| 2026-10-20 | [ICBEA](https://www.myhuiban.com/conference/5244) | - | - | - | 2027-03-26 | Xi an, China |
| 2026-10-20 | [ICCAE](https://www.myhuiban.com/conference/1127) | - | - | - | 2027-03-12 | Melbourne, Australia |
| 2026-10-20 *(extended)* | [ICCBN](https://www.myhuiban.com/conference/2041) | - | - | - | 2026-11-27 | Chengdu, China |
| 2026-10-20 | [ICCCS'''](https://www.myhuiban.com/conference/3442) | - | - | - | 2027-04-16 | Shenzhen, China |
| 2026-10-20 | [ICMFM](https://www.myhuiban.com/conference/5205) | - | - | - | 2027-03-01 | Da Nang, Vietnam |
| 2026-10-20 | [ICMMT](https://www.myhuiban.com/conference/4712) | - | - | - | 2027-03-26 | Fukuoka, Japan |
| 2026-10-20 | [ICQH](https://www.myhuiban.com/conference/5532) | - | - | - | 2026-11-19 | Tashkent, Uzbekistan |
| 2026-10-20 | [IEEE APSCON](https://www.myhuiban.com/conference/4663) | - | - | - | 2027-03-15 | Hyderabad, India |
| 2026-10-20 | [ITEC'](https://www.myhuiban.com/conference/5533) | - | - | - | 2026-11-19 | Tashkent, Uzbekistan |
| 2026-10-20 | [MSR](https://www.myhuiban.com/conference/572) | C | A | B1 | 2027-04-26 | Dublin, Ireland |
| 2026-10-20 *(extended)* | [SGGEA](https://www.myhuiban.com/conference/4823) | - | - | - | 2026-11-20 | Sanya, China |
| 2026-10-21 | [SEAMS](https://www.myhuiban.com/conference/186) | - | A | B3 | 2027-04-26 | Dublin, Ireland |
| 2026-10-22 *(extended)* | [CFIMA](https://www.myhuiban.com/conference/3380) | - | - | - | 2026-11-20 | Xiamen, China |
| 2026-10-22 *(extended)* | [FCSIT](https://www.myhuiban.com/conference/3261) | - | - | - | 2026-11-20 | Kunming, China |
| 2026-10-22 *(extended)* | [JCCME](https://www.myhuiban.com/conference/2340) | - | - | - | 2026-11-20 | Yantai, China |
| 2026-10-23 | [3EAI](https://www.myhuiban.com/conference/5852) | - | - | - | 2026-11-06 | Tumxuk, China |
| 2026-10-23 | [CHASE'](https://www.myhuiban.com/conference/4316) | - | B | - | 2027-04-26 | Dublin, Ireland |
| 2026-10-24 | [TRUST](https://www.myhuiban.com/conference/5744) | - | - | - | 2027-03-07 | Washington DC, USA |
| 2026-10-27 *(extended)* | [DSIT](https://www.myhuiban.com/conference/2620) | - | - | - | 2026-11-27 | Taicang, China |
| 2026-10-28 | [AROB](https://www.myhuiban.com/conference/5718) | - | C | - | 2027-01-19 | Beppu, Japan |
| 2026-10-29 | [ICIPCN](https://www.myhuiban.com/conference/5784) | - | - | - | 2027-01-21 | Tamil Nadu, India |
| 2026-10-29 | [ICPECA](https://www.myhuiban.com/conference/5798) | - | - | - | 2027-01-29 | Shenyang, China |
| 2026-10-29 | [IDCIoT](https://www.myhuiban.com/conference/4974) | - | - | - | 2027-01-21 | Ottapalam, Kerala, India |
| 2026-10-30 | [AISNS](https://www.myhuiban.com/conference/5135) | - | - | - | 2026-11-13 | Chongqing, China |
| 2026-10-30 | [EECT'](https://www.myhuiban.com/conference/3939) | - | - | - | 2027-03-27 | Shanghai, China |
| 2026-10-30 | [ICAIRC](https://www.myhuiban.com/conference/4460) | - | - | - | 2026-11-13 | Xiamen, China |
| 2026-10-30 | [ICCECE'](https://www.myhuiban.com/conference/3965) | - | - | - | 2027-01-15 | Xiangtan, China |
| 2026-10-30 | [ICICT''](https://www.myhuiban.com/conference/2785) | - | - | - | 2027-03-10 | Honolulu, Hawaii, USA |
| 2026-10-30 | [ICIM](https://www.myhuiban.com/conference/2376) | - | - | - | 2027-03-19 | Cambridge, UK |
| 2026-10-30 | [ICIN](https://www.myhuiban.com/conference/1578) | - | - | - | 2027-03-15 | Pisa, Italy |
| 2026-10-30 | [ICLIST](https://www.myhuiban.com/conference/5825) | - | - | - | 2027-03-18 | Bangkok, Thailand |
| 2026-10-30 | [ICSA](https://www.myhuiban.com/conference/176) | C | A | B1 | 2027-03-08 | Sydney, Australia |
| 2026-10-30 | [IDIM](https://www.myhuiban.com/conference/5799) | - | - | - | 2027-01-30 | Bali, Indonesia |
| 2026-10-31 | [ADNTIIC](https://www.myhuiban.com/conference/1810) | - | - | - | 2026-11-17 | Montevideo, Uruguay |
| 2026-10-31 | [AICARE](https://www.myhuiban.com/conference/5820) | - | - | - | 2027-03-06 | Kolkata, India |
| 2026-10-31 | [ESIHISE](https://www.myhuiban.com/conference/1940) | - | - | - | 2026-11-19 | Montevideo, Uruguay |
| 2026-10-31 | [HCITISI](https://www.myhuiban.com/conference/1809) | - | - | - | 2026-11-26 | Cordoba, Argentina |
| 2026-10-31 | [RadarConf](https://www.myhuiban.com/conference/2080) | - | - | - | 2027-05-01 | Bangalore, India |
| 2026-10-31 | [SAFEPROCESS](https://www.myhuiban.com/conference/5628) | - | C | - | 2027-06-29 | Delft, the Netherlands |
| 2026-11-01 | [EIEDP](https://www.myhuiban.com/conference/4322) | - | - | - | 2027-01-15 | Quanzhou, China |
| 2026-11-01 | [EuroGP](https://www.myhuiban.com/conference/1598) | - | B | B1 | 2027-07-31 | Mainz, Germany |
| 2026-11-01 | [EvoApplications](https://www.myhuiban.com/conference/5202) | - | B | - | 2027-03-31 | Mainz, Germany |
| 2026-11-01 | [EvoCOP](https://www.myhuiban.com/conference/1349) | - | B | B2 | 2027-03-31 | Mainz, Germany |
| 2026-11-01 | [EvoLearn](https://www.myhuiban.com/conference/5853) | - | - | - | 2027-03-31 | Mainz, Germany |
| 2026-11-01 | [EvoMUSART](https://www.myhuiban.com/conference/3416) | - | C | - | 2027-03-31 | Mainz, Germany |
| 2026-11-01 | [HOST](https://www.myhuiban.com/conference/2370) | - | - | - | 2027-05-03 | Washington DC, USA |
| 2026-11-01 | [ICMTS](https://www.myhuiban.com/conference/5831) | - | - | - | 2027-04-05 | Udine, Italy |
| 2026-11-01 | [ICRMV](https://www.myhuiban.com/conference/2565) | - | - | - | 2027-03-19 | Haining, China |
| 2026-11-01 | [ISCAIT](https://www.myhuiban.com/conference/5148) | - | - | - | 2027-01-15 | Chengdu, China |
| 2026-11-01 | [PETGS](https://www.myhuiban.com/conference/5226) | - | - | - | 2027-01-15 | Quanzhou, China |
| 2026-11-02 | [ICST](https://www.myhuiban.com/conference/934) | C | A | B2 | 2027-05-17 | San Sebastian, Spain |
| 2026-11-03 | [HNNDL](https://www.myhuiban.com/conference/5216) | - | - | - | 2027-01-22 | Qingdao, China |

---

Data: **Conference Partner (myhuiban.com)**, free to use with attribution. Ranking values are reproduced from CCF / CORE / QUALIS — cite those bodies for the rankings themselves. The repository's MIT licence covers its code, not this data.
