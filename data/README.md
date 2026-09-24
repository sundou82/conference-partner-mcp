# Data snapshot

Generated **2026-09-24T10:28:28+00:00** from the [Conference Partner API](https://www.myhuiban.com/developers). Refreshed daily by [CI](../.github/workflows/snapshot.yml).

Every file here comes from the API's **anonymous tier** — the same rows anyone can fetch without credentials. Per-venue detail (CFP full text, acceptance-rate history, edition history, ratings, the organiser's own website URL) is not included; it needs a free credential and lives behind the API. See [../docs/data.md](../docs/data.md).

## Files

| Dataset | Rows | JSON | CSV |
|---|---|---|---|
| **Upcoming submission deadlines**<br><sub>Every conference whose submission deadline has not passed, soonest first.</sub> | 821 | [upcoming-deadlines.json](upcoming-deadlines.json) | [upcoming-deadlines.csv](upcoming-deadlines.csv) |
| **CCF-ranked conferences**<br><sub>Every conference carrying a CCF rank, whether or not a call is open. CORE and QUALIS ranks are on the same row where the venue has them.</sub> | 388 | [ccf-conferences.json](ccf-conferences.json) | [ccf-conferences.csv](ccf-conferences.csv) |
| **CORE-ranked conferences**<br><sub>Every conference carrying a CORE rank, whether or not a call is open.</sub> | 734 | [core-conferences.json](core-conferences.json) | [core-conferences.csv](core-conferences.csv) |
| **QUALIS-ranked conferences**<br><sub>Every conference carrying a QUALIS rank (A1 through B5), whether or not a call is open.</sub> | 705 | [qualis-conferences.json](qualis-conferences.json) | [qualis-conferences.csv](qualis-conferences.csv) |
| **Ranked conferences with a call open now**<br><sub>The subset of the catalogues you can still submit to today — CCF, CORE and QUALIS lists merged.</sub> | 143 | [open-calls-by-rank.json](open-calls-by-rank.json) | [open-calls-by-rank.csv](open-calls-by-rank.csv) |
| **CCF-ranked journals**<br><sub>Journals in the CCF catalogue, with impact factor, publisher and ISSN.</sub> | 292 | [ccf-journals.json](ccf-journals.json) | [ccf-journals.csv](ccf-journals.csv) |
| **Journals with an open special-issue call**<br><sub>Journals currently carrying a special-issue call for papers.</sub> | 91 | [journal-special-issues.json](journal-special-issues.json) | [journal-special-issues.csv](journal-special-issues.csv) |
| **Top journals by impact factor**<br><sub>The 300 highest reported impact factors. Figures are as published by the journal and may lag the latest JCR.</sub> | 296 | [top-impact-factor-journals.json](top-impact-factor-journals.json) | [top-impact-factor-journals.csv](top-impact-factor-journals.csv) |

Site totals on the day of generation: **5821** conferences, **1218** journals.

## Prefer live data

A snapshot is stale the moment a deadline is extended, which happens daily in submission season. For anything that has to be right, call the API — it needs no key for exactly the data in this directory:

```bash
curl "https://www.myhuiban.com/api/conferences?field=ai&submission_date_start=$(date +%F)"
```

Or mirror it incrementally with `updated_since` — see [../docs/rest-api.md](../docs/rest-api.md#incremental-sync).

## Deadlines in the next 90 days (512)

| Deadline | Conference | CCF | CORE | QUALIS | Held | Location |
|---|---|---|---|---|---|---|
| 2026-09-25 *(extended)* | [AsiaEdu](https://www.myhuiban.com/conference/5731) | - | - | - | 2026-11-28 | Niigata, Japan |
| 2026-09-25 | [BioMRH](https://www.myhuiban.com/conference/5047) | - | - | - | 2026-10-20 | Glasgow, UK |
| 2026-09-25 | [CMICA](https://www.myhuiban.com/conference/5865) | - | - | - | 2026-11-27 | Harbin, China |
| 2026-09-25 | [CSNT](https://www.myhuiban.com/conference/2166) | - | - | - | 2027-03-12 | Khajuraho, Gwalior, India |
| 2026-09-25 | [Eurographics](https://www.myhuiban.com/conference/271) | B | - | A2 | 2027-05-10 | Lucca, Italy |
| 2026-09-25 | [ICBMC](https://www.myhuiban.com/conference/5228) | - | - | - | 2027-02-18 | Hong Kong, China |
| 2026-09-25 *(extended)* | [ICBTA](https://www.myhuiban.com/conference/3222) | - | - | - | 2026-12-11 | Seoul, South Korea |
| 2026-09-25 | [ICCAID](https://www.myhuiban.com/conference/4507) | - | - | - | 2026-10-11 | Nanchang, China |
| 2026-09-25 | [ICCDE'](https://www.myhuiban.com/conference/2332) | - | - | - | 2027-02-17 | Phuket, Thailand |
| 2026-09-25 *(extended)* | [ICEEL](https://www.myhuiban.com/conference/3201) | - | - | - | 2026-11-27 | Tokyo, Japan |
| 2026-09-25 | [ICMLC](https://www.myhuiban.com/conference/1375) | - | - | B4 | 2027-02-26 | Shenzhen, China |
| 2026-09-25 | [ICPEE'](https://www.myhuiban.com/conference/3751) | - | - | - | 2026-12-26 | Chengdu, China |
| 2026-09-25 | [ICRAIC](https://www.myhuiban.com/conference/4200) | - | - | - | 2026-11-27 | Xi an, China |
| 2026-09-25 *(extended)* | [ICRCV](https://www.myhuiban.com/conference/4847) | - | - | - | 2026-11-06 | Jiangyin, China |
| 2026-09-25 | [ICRIC](https://www.myhuiban.com/conference/5565) | - | - | - | 2027-02-17 | Milan, Italy |
| 2026-09-25 *(extended)* | [ICSSIP](https://www.myhuiban.com/conference/5514) | - | - | - | 2026-11-27 | Lanzhou, China |
| 2026-09-25 *(extended)* | [ICSTTE](https://www.myhuiban.com/conference/2097) | - | - | - | 2026-10-30 | Weihai, China |
| 2026-09-25 *(extended)* | [ICoCTA](https://www.myhuiban.com/conference/3382) | - | - | - | 2026-10-23 | Qingdao, China |
| 2026-09-25 *(extended)* | [INCC](https://www.myhuiban.com/conference/4861) | - | - | - | 2026-11-28 | Niigata, Japan |
| 2026-09-25 | [ISEC](https://www.myhuiban.com/conference/2884) | - | - | - | 2027-02-18 | Mumbai, India |
| 2026-09-25 | [MEAE](https://www.myhuiban.com/conference/5864) | - | - | - | 2026-11-27 | Xi an, China |
| 2026-09-25 | [PEEE](https://www.myhuiban.com/conference/4375) | - | - | - | 2027-01-18 | Milan, Italy |
| 2026-09-26 *(extended)* | [ACITY](https://www.myhuiban.com/conference/1363) | - | - | - | 2026-11-27 | Zurich, Switzerland |
| 2026-09-26 *(extended)* | [AI'](https://www.myhuiban.com/conference/3462) | - | - | - | 2026-12-26 | Dubai, UAE |
| 2026-09-26 *(extended)* | [CAIML](https://www.myhuiban.com/conference/3548) | - | - | - | 2026-10-24 | Vienna, Austria |
| 2026-09-26 *(extended)* | [CCSIT](https://www.myhuiban.com/conference/1108) | - | - | - | 2026-11-21 | London, UK |
| 2026-09-26 | [CITCE](https://www.myhuiban.com/conference/4447) | - | - | - | 2026-12-11 | Suzhou, China |
| 2026-09-26 *(extended)* | [CLSB](https://www.myhuiban.com/conference/3861) | - | - | - | 2026-10-17 | Sydney, Australia |
| 2026-09-26 *(extended)* | [CSEA'](https://www.myhuiban.com/conference/3872) | - | - | - | 2026-12-19 | Sydney, Australia |
| 2026-09-26 | [DTMN](https://www.myhuiban.com/conference/2720) | - | - | - | 2026-10-17 | Sydney, Australia |
| 2026-09-26 *(extended)* | [ICAIT'](https://www.myhuiban.com/conference/3550) | - | - | - | 2026-10-24 | Vienna, Austria |
| 2026-09-26 | [ICNGN](https://www.myhuiban.com/conference/4459) | - | - | - | 2026-12-12 | Hong Kong, China |
| 2026-09-26 | [ICSE''](https://www.myhuiban.com/conference/4903) | - | - | - | 2026-12-11 | Shenzhen, China |
| 2026-09-26 | [IRAC](https://www.myhuiban.com/conference/5121) | - | - | - | 2026-12-11 | Hangzhou, China |
| 2026-09-26 *(extended)* | [ITCSE](https://www.myhuiban.com/conference/3149) | - | - | - | 2026-10-24 | Vienna, Austria |
| 2026-09-26 *(extended)* | [IWMEN](https://www.myhuiban.com/conference/5858) | - | - | - | 2026-11-21 | London, UK |
| 2026-09-26 *(extended)* | [IoTE](https://www.myhuiban.com/conference/3883) | - | - | - | 2026-11-27 | Zurich, Switzerland |
| 2026-09-26 *(extended)* | [MLTEC](https://www.myhuiban.com/conference/4070) | - | - | - | 2026-12-19 | Sydney, Australia |
| 2026-09-26 *(extended)* | [NLAICSE](https://www.myhuiban.com/conference/5874) | - | - | - | 2026-12-30 | Online |
| 2026-09-26 *(extended)* | [NLAII](https://www.myhuiban.com/conference/5859) | - | - | - | 2026-10-30 | Online |
| 2026-09-26 *(extended)* | [NLCA](https://www.myhuiban.com/conference/3947) | - | - | - | 2026-10-24 | Vienna, Austria |
| 2026-09-28 | [BDMLIC](https://www.myhuiban.com/conference/5546) | - | - | - | 2026-09-30 | Shenzhen, China |
| 2026-09-28 | [EMO](https://www.myhuiban.com/conference/5714) | - | - | - | 2027-04-05 | Exeter, UK |
| 2026-09-28 | [ICBCTIS](https://www.myhuiban.com/conference/4038) | - | - | - | 2026-12-04 | Zhengzhou, China |
| 2026-09-28 | [ICMMPM](https://www.myhuiban.com/conference/3128) | - | - | - | 2026-11-16 | Seoul, South Korea |
| 2026-09-29 | [AISTATS](https://www.myhuiban.com/conference/1853) | C | A | - | 2027-05-03 | Montreal, Quebec, Canada |
| 2026-09-30 | [ACIIDS](https://www.myhuiban.com/conference/5616) | - | B | - | 2027-04-05 | Bali, Indonesia |
| 2026-09-30 *(extended)* | [AI2A](https://www.myhuiban.com/conference/3995) | - | - | - | 2026-10-23 | Wuxi, China |
| 2026-09-30 *(extended)* | [AIAM](https://www.myhuiban.com/conference/3669) | - | - | - | 2026-10-29 | Frankfurt, Germany |
| 2026-09-30 | [AIEI](https://www.myhuiban.com/conference/5785) | - | - | - | 2027-01-21 | Bengaluru, India |
| 2026-09-30 *(extended)* | [AMEM](https://www.myhuiban.com/conference/5574) | - | - | - | 2026-12-11 | Wuhan, China |
| 2026-09-30 *(extended)* | [ASIG](https://www.myhuiban.com/conference/4883) | - | - | - | 2026-12-04 | Kyoto, Japan |
| 2026-09-30 | [BDCC](https://www.myhuiban.com/conference/2803) | - | - | - | 2026-12-03 | Coimbatore, India |
| 2026-09-30 *(extended)* | [BDCIA](https://www.myhuiban.com/conference/5572) | - | - | - | 2026-11-06 | Huanggang, China |
| 2026-09-30 | [BigComp](https://www.myhuiban.com/conference/1407) | - | - | - | 2027-01-25 | Fukuoka, Japan |
| 2026-09-30 *(extended)* | [CAVI](https://www.myhuiban.com/conference/5846) | - | - | - | 2026-10-30 | Guiyang, China |
| 2026-09-30 *(extended)* | [CCNML](https://www.myhuiban.com/conference/4338) | - | - | - | 2026-10-23 | Wuxi, China |
| 2026-09-30 | [CESPE](https://www.myhuiban.com/conference/5893) | - | - | - | 2026-12-04 | Chengdu, China |
| 2026-09-30 | [EAI WiCON](https://www.myhuiban.com/conference/105) | - | - | B3 | 2026-12-02 | Bratislava, Slovakia |
| 2026-09-30 *(extended)* | [ICAIT](https://www.myhuiban.com/conference/3089) | - | - | - | 2026-11-23 | Auckland, New Zealand |
| 2026-09-30 | [ICCMB](https://www.myhuiban.com/conference/3534) | - | - | - | 2027-02-18 | Basel, Switzerland |
| 2026-09-30 | [ICCRD](https://www.myhuiban.com/conference/4888) | - | - | - | 2027-01-15 | Singapore |
| 2026-09-30 | [ICCSNT](https://www.myhuiban.com/conference/763) | - | - | - | 2026-12-29 | Harbin, China |
| 2026-09-30 | [ICETCS](https://www.myhuiban.com/conference/5805) | - | - | - | 2027-02-11 | Bengaluru, India |
| 2026-09-30 | [ICICF](https://www.myhuiban.com/conference/5787) | - | - | - | 2027-01-21 | Bengaluru, India |
| 2026-09-30 | [ICIIT](https://www.myhuiban.com/conference/2349) | - | - | - | 2027-03-04 | Ho Chi Minh City, Vietnam |
| 2026-09-30 | [ICMLSC](https://www.myhuiban.com/conference/2975) | - | - | - | 2027-01-29 | Tokyo, Japan |
| 2026-09-30 | [ICNSC](https://www.myhuiban.com/conference/2033) | - | - | - | 2026-11-27 | Chongqing, China |
| 2026-09-30 | [ICSCM](https://www.myhuiban.com/conference/5204) | - | - | - | 2027-02-18 | Basel, Switzerland |
| 2026-09-30 | [ICSUMMIT](https://www.myhuiban.com/conference/5873) | - | - | - | 2027-01-08 | Vadodara, Gujarat, India |
| 2026-09-30 | [ICTACS](https://www.myhuiban.com/conference/5765) | - | - | - | 2026-12-03 | Tashkent, Uzbekistan |
| 2026-09-30 | [IEEA](https://www.myhuiban.com/conference/3493) | - | - | - | 2027-02-24 | Tokyo, Japan |
| 2026-09-30 | [IEEE Satellite](https://www.myhuiban.com/conference/4366) | - | - | - | 2026-11-14 | Hainan, China |
| 2026-09-30 | [IITCEE](https://www.myhuiban.com/conference/4966) | - | - | - | 2027-01-21 | Bengaluru, India |
| 2026-09-30 *(extended)* | [IMDH](https://www.myhuiban.com/conference/5856) | - | - | - | 2026-11-10 | Leukerbad, Switzerland |
| 2026-09-30 | [ISAS](https://www.myhuiban.com/conference/4901) | - | - | - | 2026-12-04 | Ankara, Turkiye |
| 2026-09-30 | [ISCIPT](https://www.myhuiban.com/conference/5023) | - | - | - | 2026-11-13 | Fushun, China |
| 2026-09-30 | [ISPA](https://www.myhuiban.com/conference/190) | C | C | B3 | 2026-12-27 | Kuala Lumpur, Malaysia |
| 2026-09-30 | [MLCC](https://www.myhuiban.com/conference/5564) | - | - | - | 2027-03-19 | Chongqing, China |
| 2026-09-30 *(extended)* | [MLPR](https://www.myhuiban.com/conference/4998) | - | - | - | 2026-12-04 | Kyoto, Japan |
| 2026-09-30 | [NPSPE](https://www.myhuiban.com/conference/5575) | - | - | - | 2026-12-25 | Harbin, China |
| 2026-09-30 | [NQComp](https://www.myhuiban.com/conference/5789) | - | - | - | 2027-01-21 | Bengaluru, India |
| 2026-09-30 | [PCCNT](https://www.myhuiban.com/conference/4557) | - | - | - | 2026-10-30 | Wuhan, China |
| 2026-09-30 *(extended)* | [PEPSC](https://www.myhuiban.com/conference/4528) | - | - | - | 2026-11-02 | Cairo, Egypt |
| 2026-09-30 | [PElS](https://www.myhuiban.com/conference/5892) | - | - | - | 2026-11-06 | Nanjing, China |
| 2026-09-30 | [SCA''](https://www.myhuiban.com/conference/4963) | - | - | - | 2027-03-01 | Singapore |
| 2026-09-30 *(extended)* | [TOCS](https://www.myhuiban.com/conference/4952) | - | - | - | 2026-11-20 | Nanyang, China |
| 2026-09-30 *(extended)* | [VSIP](https://www.myhuiban.com/conference/3057) | - | - | - | 2026-11-06 | Zhenjiang, China |
| 2026-09-30 | [WcAISR](https://www.myhuiban.com/conference/5786) | - | - | - | 2027-01-21 | Mohali, Punjab, India |
| 2026-10-01 | [AAMAS](https://www.myhuiban.com/conference/412) | B | A | A1 | 2027-05-03 | Hanoi, Vietnam |
| 2026-10-01 | [ArtInHCI](https://www.myhuiban.com/conference/4625) | - | - | - | 2026-10-16 | Wuhan, China |
| 2026-10-01 | [FPGA](https://www.myhuiban.com/conference/336) | B | A | A2 | 2027-03-14 | Seaside, California, USA |
| 2026-10-01 | [ICACT](https://www.myhuiban.com/conference/1682) | - | - | - | 2027-01-24 | Phoenix Park, PyeongChang, Korea |
| 2026-10-01 | [ICAIIC](https://www.myhuiban.com/conference/2925) | - | - | - | 2027-02-22 | Osaka, Japan |
| 2026-10-01 | [ICARA](https://www.myhuiban.com/conference/1587) | - | - | - | 2027-02-25 | Paris, France |
| 2026-10-01 | [ICICIP](https://www.myhuiban.com/conference/827) | - | - | - | 2027-02-08 | Vientiane and Luang Prabang, Laos |
| 2026-10-01 *(extended)* | [ICICM](https://www.myhuiban.com/conference/1978) | - | - | - | 2026-11-11 | Jakarta, Indonesia |
| 2026-10-01 | [ICIMPACT](https://www.myhuiban.com/conference/5803) | - | - | - | 2027-02-03 | Bandung, Indonesia |
| 2026-10-01 | [ICIPS](https://www.myhuiban.com/conference/5140) | - | - | - | 2026-10-24 | Dalian, China |
| 2026-10-01 | [IPDPS](https://www.myhuiban.com/conference/334) | B | A | A1 | 2027-06-01 | Seattle, Washington, USA |
| 2026-10-01 | [MJIC](https://www.myhuiban.com/conference/4941) | - | - | - | 2027-03-28 | Batu Ferringhi, Pulau Pinang, Malaysia |
| 2026-10-01 | [PDeS](https://www.myhuiban.com/conference/2527) | - | - | - | 2027-05-19 | Ostrava, Czech Republic |
| 2026-10-01 | [SMC-IoT](https://www.myhuiban.com/conference/4702) | - | - | - | 2026-12-04 | Jiaozuo, China |
| 2026-10-01 | [SPCT](https://www.myhuiban.com/conference/4461) | - | - | - | 2026-12-18 | Shenzhen, China |
| 2026-10-01 | [iEECON](https://www.myhuiban.com/conference/5817) | - | - | - | 2027-03-03 | Rayong, Thailand |
| 2026-10-02 *(extended)* | [ACC](https://www.myhuiban.com/conference/2880) | - | - | - | 2027-07-07 | Philadelphia, Pennsylvania, USA |
| 2026-10-02 | [ASIM](https://www.myhuiban.com/conference/5097) | - | - | - | 2026-12-04 | Chongqing, China |
| 2026-10-02 | [DCC](https://www.myhuiban.com/conference/617) | B | B | A2 | 2027-03-23 | Snowbird, Utah, USA |
| 2026-10-02 *(extended)* | [DFRWS EU](https://www.myhuiban.com/conference/3436) | C | - | - | 2027-03-30 | Edinburgh, Scotland |
| 2026-10-02 | [EDCC](https://www.myhuiban.com/conference/1404) | - | - | B2 | 2027-04-06 | Trondheim, Norway |
| 2026-10-02 | [FSE](https://www.myhuiban.com/conference/87) | A | A* | A1 | 2027-07-12 | Shenzhen, China |
| 2026-10-02 | [FTTE](https://www.myhuiban.com/conference/5157) | - | - | - | 2026-10-16 | Xiangyang, China |
| 2026-10-02 | [ICC](https://www.myhuiban.com/conference/318) | C | - | A2 | 2027-05-30 | Washington DC, USA |
| 2026-10-02 | [ICN'](https://www.myhuiban.com/conference/4624) | - | - | - | 2026-10-16 | Changzhou, China |
| 2026-10-02 *(extended)* | [ISSTC](https://www.myhuiban.com/conference/4916) | - | - | - | 2026-10-16 | Qingdao, China |
| 2026-10-02 | [SAC'](https://www.myhuiban.com/conference/218) | - | - | A1 | 2027-04-05 | Gwangju, South Korea |
| 2026-10-02 | [WONS](https://www.myhuiban.com/conference/932) | - | - | B4 | 2027-01-25 | Cortina d'Ampezzo, Italy |
| 2026-10-03 | [AIBDF](https://www.myhuiban.com/conference/4391) | - | - | - | 2026-12-18 | Chengdu, China |
| 2026-10-03 | [CEPGT](https://www.myhuiban.com/conference/5152) | - | - | - | 2026-12-18 | Chengdu, China |
| 2026-10-03 | [ICHBC](https://www.myhuiban.com/conference/4450) | - | - | - | 2026-12-18 | Nanchang, China |
| 2026-10-03 | [ICISE-IE](https://www.myhuiban.com/conference/4720) | - | - | - | 2026-12-18 | Guangzhou, China |
| 2026-10-03 | [ISNEET](https://www.myhuiban.com/conference/5169) | - | - | - | 2026-12-18 | Weihai, China |
| 2026-10-03 | [MEMAT](https://www.myhuiban.com/conference/5189) | - | - | - | 2026-12-18 | Foshan, China |
| 2026-10-04 | [AISEE](https://www.myhuiban.com/conference/5790) | - | - | - | 2027-01-22 | Mangaluru, India |
| 2026-10-05 *(extended)* | [ADMIT](https://www.myhuiban.com/conference/4378) | - | - | - | 2026-10-16 | Wuhan, China |
| 2026-10-05 *(extended)* | [AMA21](https://www.myhuiban.com/conference/3560) | - | - | - | 2026-12-16 | Online |
| 2026-10-05 *(extended)* | [CCBDIoT](https://www.myhuiban.com/conference/4379) | - | - | - | 2026-10-16 | Wuhan, China |
| 2026-10-05 | [CSP](https://www.myhuiban.com/conference/3334) | - | - | - | 2027-03-27 | Nagoya, Japan |
| 2026-10-05 | [ICAEM](https://www.myhuiban.com/conference/4483) | - | - | - | 2027-01-23 | Phuket, Thailand |
| 2026-10-05 *(extended)* | [ICBBE](https://www.myhuiban.com/conference/4077) | - | - | - | 2026-12-25 | Hokkaido, Japan |
| 2026-10-05 | [ICCSMT](https://www.myhuiban.com/conference/3964) | - | - | - | 2026-12-25 | Chengdu, China |
| 2026-10-05 | [ICINT](https://www.myhuiban.com/conference/2388) | - | - | - | 2027-03-05 | Melbourne, Australia |
| 2026-10-05 | [ICMEA'](https://www.myhuiban.com/conference/4711) | - | - | - | 2027-01-12 | Tokyo, Japan |
| 2026-10-05 | [ICMIP](https://www.myhuiban.com/conference/3335) | - | - | - | 2027-03-27 | Nagoya, Japan |
| 2026-10-05 *(extended)* | [ICMRA](https://www.myhuiban.com/conference/3697) | - | - | - | 2026-11-13 | Suzhou, China |
| 2026-10-05 *(extended)* | [ICRAE](https://www.myhuiban.com/conference/1779) | - | - | - | 2026-11-20 | Nagoya, Japan |
| 2026-10-05 *(extended)* | [ICoAC](https://www.myhuiban.com/conference/2391) | - | - | - | 2026-12-17 | Chennai, India |
| 2026-10-05 | [MLCIPR](https://www.myhuiban.com/conference/5147) | - | - | - | 2026-12-25 | Nanjing, China |
| 2026-10-05 *(extended)* | [PESA](https://www.myhuiban.com/conference/5730) | - | - | - | 2026-11-13 | Singapore |
| 2026-10-06 | [EPSEE](https://www.myhuiban.com/conference/4307) | - | - | - | 2026-11-06 | Hohhot, China |
| 2026-10-07 | [EDBT](https://www.myhuiban.com/conference/139) | B | B | A2 | 2027-04-06 | Lille, France |
| 2026-10-08 *(extended)* | [CFEEE](https://www.myhuiban.com/conference/3424) | - | - | - | 2026-11-06 | Shanghai, China |
| 2026-10-08 | [CHIIR](https://www.myhuiban.com/conference/1827) | - | B | - | 2027-03-07 | Berlin, Germany |
| 2026-10-08 | [DLNN](https://www.myhuiban.com/conference/5199) | - | - | - | 2026-12-11 | Wuhan, China |
| 2026-10-08 | [ICAUC](https://www.myhuiban.com/conference/5781) | - | - | - | 2027-01-18 | Pathum Thani, Thailand |
| 2026-10-08 *(extended)* | [JCRAI](https://www.myhuiban.com/conference/2514) | - | - | - | 2026-11-06 | Beijing, China |
| 2026-10-09 | [EIRIS](https://www.myhuiban.com/conference/5551) | - | - | - | 2026-10-23 | Wenzhou, China |
| 2026-10-09 | [ETRA](https://www.myhuiban.com/conference/3722) | - | B | - | 2027-06-07 | Pamplona, Spain |
| 2026-10-09 | [FG](https://www.myhuiban.com/conference/515) | C | B | A1 | 2027-04-26 | Marrakesh, Morocco |
| 2026-10-09 | [HotMobile](https://www.myhuiban.com/conference/608) | - | - | B2 | 2027-02-24 | Tucson, Arizona |
| 2026-10-09 | [ICEduTech](https://www.myhuiban.com/conference/3558) | - | - | - | 2027-03-13 | Porto, Portugal |
| 2026-10-09 | [IS'](https://www.myhuiban.com/conference/2964) | - | - | - | 2027-03-13 | Porto, Portugal |
| 2026-10-09 | [ISEAE](https://www.myhuiban.com/conference/4047) | - | - | - | 2027-04-23 | Harbin, China |
| 2026-10-09 | [IWIPP](https://www.myhuiban.com/conference/5813) | - | - | - | 2027-02-28 | Kitakyushu, Japan |
| 2026-10-09 | [MHV](https://www.myhuiban.com/conference/4230) | - | - | - | 2027-02-23 | Denver, Colorado, USA |
| 2026-10-09 | [ML](https://www.myhuiban.com/conference/2972) | - | - | - | 2027-03-13 | Porto, Portugal |
| 2026-10-09 | [e-Society](https://www.myhuiban.com/conference/2963) | - | - | - | 2027-03-13 | Porto, Portugal |
| 2026-10-10 | [AAIML](https://www.myhuiban.com/conference/5829) | - | - | - | 2027-03-29 | Tokyo, Japan |
| 2026-10-10 *(extended)* | [AICCC](https://www.myhuiban.com/conference/2864) | - | - | - | 2026-12-18 | Tokyo, Japan |
| 2026-10-10 *(extended)* | [AIES'](https://www.myhuiban.com/conference/5881) | - | - | - | 2026-12-18 | Kunming, China |
| 2026-10-10 | [AIPE](https://www.myhuiban.com/conference/4759) | - | - | - | 2027-02-26 | Nanjing, China |
| 2026-10-10 | [AIxDKE](https://www.myhuiban.com/conference/2770) | - | - | - | 2027-02-01 | Laguna Hills, California, USA |
| 2026-10-10 | [BDAMEA](https://www.myhuiban.com/conference/5118) | - | - | - | 2026-12-25 | Suzhou, China |
| 2026-10-10 *(extended)* | [CECCC](https://www.myhuiban.com/conference/4848) | - | - | - | 2026-11-18 | Barcelona, Spain |
| 2026-10-10 | [CTIEET](https://www.myhuiban.com/conference/4617) | - | - | - | 2026-12-25 | Harbin, China |
| 2026-10-10 | [EESE](https://www.myhuiban.com/conference/4920) | - | - | - | 2026-12-11 | Changsha, China |
| 2026-10-10 | [EMET](https://www.myhuiban.com/conference/3613) | - | - | - | 2026-11-10 | Nanchang, China |
| 2026-10-10 *(extended)* | [ICAIRS](https://www.myhuiban.com/conference/5558) | - | - | - | 2026-10-23 | Tianjin, China |
| 2026-10-10 *(extended)* | [ICCBN](https://www.myhuiban.com/conference/2041) | - | - | - | 2026-11-27 | Chengdu, China |
| 2026-10-10 *(extended)* | [ICETC](https://www.myhuiban.com/conference/1574) | - | - | B4 | 2026-12-14 | Porto, Portugal |
| 2026-10-10 | [ICGEA](https://www.myhuiban.com/conference/4203) | - | - | - | 2027-03-18 | Singapore |
| 2026-10-10 | [ICIBE](https://www.myhuiban.com/conference/4873) | - | - | - | 2027-03-19 | Hong Kong, China |
| 2026-10-10 *(extended)* | [ICICSE'](https://www.myhuiban.com/conference/4014) | - | - | - | 2026-12-27 | Chongqing, China |
| 2026-10-10 | [ICMSS](https://www.myhuiban.com/conference/3394) | - | - | - | 2027-03-19 | Hong Kong, China |
| 2026-10-10 *(extended)* | [ICRAI](https://www.myhuiban.com/conference/1975) | - | - | - | 2026-12-18 | Songdo, Incheon, Korea |
| 2026-10-10 | [ICSC](https://www.myhuiban.com/conference/230) | - | - | B2 | 2027-02-01 | Laguna Hills, California, USA |
| 2026-10-10 | [IFIP WG 11.9](https://www.myhuiban.com/conference/1497) | C | - | - | 2027-01-07 | New Delhi, India |
| 2026-10-10 *(extended)* | [ISCMI](https://www.myhuiban.com/conference/2634) | - | - | - | 2026-11-18 | Vienna, Austria |
| 2026-10-10 | [MLAIA](https://www.myhuiban.com/conference/5201) | - | - | - | 2026-12-18 | Nanning, China |
| 2026-10-10 | [NEFES](https://www.myhuiban.com/conference/3787) | - | - | - | 2027-08-17 | Osaka, Japan |
| 2026-10-10 *(extended)* | [NLPIR](https://www.myhuiban.com/conference/3024) | - | - | - | 2026-12-11 | Nara, Japan |
| 2026-10-10 *(extended)* | [RAAI](https://www.myhuiban.com/conference/4874) | - | - | - | 2026-12-18 | Singapore |
| 2026-10-10 | [RoboticCC](https://www.myhuiban.com/conference/2074) | - | - | - | 2027-02-01 | Laguna Hills, California, USA |
| 2026-10-10 | [SICE ISCS](https://www.myhuiban.com/conference/5815) | - | - | - | 2027-03-02 | Tokyo, Japan |
| 2026-10-10 | [SIGMOD](https://www.myhuiban.com/conference/133) | A | A* | A1 | 2027-06-13 | Huntington Beach, California, USA |
| 2026-10-10 | [SPRA](https://www.myhuiban.com/conference/5246) | - | - | - | 2027-03-03 | Tokyo, Japan |
| 2026-10-11 | [NESEE](https://www.myhuiban.com/conference/5168) | - | - | - | 2026-12-18 | Guangzhou, China |
| 2026-10-11 | [STACS](https://www.myhuiban.com/conference/389) | C | A | A2 | 2027-03-08 | Gottingen, Germany |
| 2026-10-12 | [ALT](https://www.myhuiban.com/conference/419) | C | B | B1 | 2027-03-09 | Leiden, the Netherlands |
| 2026-10-12 *(extended)* | [CIoTSC](https://www.myhuiban.com/conference/4691) | - | - | - | 2026-11-06 | Mianyang, China |
| 2026-10-12 | [COLING](https://www.myhuiban.com/conference/170) | B | B | A1 | 2027-05-09 | Macau, China |
| 2026-10-12 | [ICIT](https://www.myhuiban.com/conference/743) | - | - | B3 | 2027-03-15 | Florianopolis, Brazil |
| 2026-10-12 | [ITAM](https://www.myhuiban.com/conference/5198) | - | - | - | 2026-12-18 | Foshan, China |
| 2026-10-12 | [NAACL](https://www.myhuiban.com/conference/426) | B | A | A1 | 2027-06-01 | San Francisco, California, USA |
| 2026-10-12 *(extended)* | [NCIC](https://www.myhuiban.com/conference/4881) | - | - | - | 2026-10-16 | Baotou, China |
| 2026-10-13 | [IC-EISIT](https://www.myhuiban.com/conference/5471) | - | - | - | 2026-10-23 | Guangzhou, China |
| 2026-10-13 | [ISCAS](https://www.myhuiban.com/conference/340) | B | C | A1 | 2027-06-06 | Bordeaux, France |
| 2026-10-15 *(extended)* | [CCORE](https://www.myhuiban.com/conference/4790) | - | - | - | 2026-11-06 | Online |
| 2026-10-15 *(extended)* | [CESST](https://www.myhuiban.com/conference/5577) | - | - | - | 2026-12-18 | Zhengzhou, China |
| 2026-10-15 *(extended)* | [CEVVE](https://www.myhuiban.com/conference/4028) | - | - | - | 2026-10-16 | Fuzhou, China |
| 2026-10-15 | [EMC²](https://www.myhuiban.com/conference/5737) | - | - | - | 2027-01-08 | Shenzhen, China |
| 2026-10-15 | [ESOP](https://www.myhuiban.com/conference/200) | - | A | A2 | 2027-04-10 | Copenhagen, Denmark |
| 2026-10-15 | [ETAPS](https://www.myhuiban.com/conference/768) | B | - | - | 2027-04-10 | Copenhagen, Denmark |
| 2026-10-15 | [FoSSaCS](https://www.myhuiban.com/conference/202) | - | B | A2 | 2027-04-10 | Copenhagen, Denmark |
| 2026-10-15 | [IC'](https://www.myhuiban.com/conference/5882) | - | - | - | 2027-01-17 | Okinawa, Japan |
| 2026-10-15 *(extended)* | [ICACS](https://www.myhuiban.com/conference/2491) | - | - | - | 2026-12-18 | Phuket, Thailand |
| 2026-10-15 *(extended)* | [ICCDA'](https://www.myhuiban.com/conference/2897) | - | - | - | 2026-12-18 | Phuket, Thailand |
| 2026-10-15 | [ICCIDS](https://www.myhuiban.com/conference/2934) | - | - | - | 2027-01-06 | Chennai, India |
| 2026-10-15 | [ICCR'](https://www.myhuiban.com/conference/5751) | - | - | - | 2026-12-06 | Irbid, Jordan |
| 2026-10-15 | [ICCSCT](https://www.myhuiban.com/conference/1934) | - | - | - | 2026-12-12 | Hong Kong, China |
| 2026-10-15 | [ICCVIT](https://www.myhuiban.com/conference/4909) | - | - | - | 2026-12-18 | Beijing, China |
| 2026-10-15 | [ICECC](https://www.myhuiban.com/conference/679) | - | - | - | 2027-03-18 | Tokyo, Japan |
| 2026-10-15 | [ICEDS](https://www.myhuiban.com/conference/5400) | - | - | - | 2027-04-15 | Glasgow, UK |
| 2026-10-15 | [ICFST](https://www.myhuiban.com/conference/3232) | - | - | - | 2027-03-18 | Tokyo, Japan |
| 2026-10-15 *(extended)* | [ICMSC](https://www.myhuiban.com/conference/4676) | - | - | - | 2026-11-22 | Toyama, Japan |
| 2026-10-15 | [MAIC](https://www.myhuiban.com/conference/4914) | - | - | - | 2026-12-11 | Liuzhou, China |
| 2026-10-15 *(extended)* | [MMAL](https://www.myhuiban.com/conference/5847) | - | - | - | 2027-01-15 | Singapore |
| 2026-10-15 | [TACAS](https://www.myhuiban.com/conference/203) | - | A | A1 | 2027-04-10 | Copenhagen, Denmark |
| 2026-10-15 | [iFS](https://www.myhuiban.com/conference/5527) | - | - | - | 2027-04-10 | Copenhagen, Denmark |
| 2026-10-16 | [ICDM''](https://www.myhuiban.com/conference/5132) | - | - | - | 2026-10-30 | Changchun, China |
| 2026-10-16 | [ICFTIC](https://www.myhuiban.com/conference/3312) | - | - | - | 2026-10-30 | Qingdao, China |
| 2026-10-16 | [ICHIH](https://www.myhuiban.com/conference/4679) | - | - | - | 2026-12-25 | Hangzhou, China |
| 2026-10-16 | [MMLDS](https://www.myhuiban.com/conference/5507) | - | - | - | 2026-10-30 | Zhengzhou, China |
| 2026-10-16 *(extended)* | [SHWID](https://www.myhuiban.com/conference/5151) | - | - | - | 2026-10-30 | Kuala Lumpur, Malaysia |
| 2026-10-17 | [SCIBT](https://www.myhuiban.com/conference/5823) | - | - | - | 2027-03-17 | Muscat, Oman |
| 2026-10-18 | [ICIMCIS](https://www.myhuiban.com/conference/5770) | - | - | - | 2026-12-02 | Jakarta, Indonesia |
| 2026-10-18 | [The Web Conference](https://www.myhuiban.com/conference/137) | A | A* | A1 | 2027-05-10 | Dublin, Ireland |
| 2026-10-19 | [FSEN](https://www.myhuiban.com/conference/1976) | - | - | - | 2027-05-24 | Enschede, Netherlands |
| 2026-10-19 | [TechDebt](https://www.myhuiban.com/conference/5211) | - | B | - | 2027-04-25 | Dublin, Ireland |
| 2026-10-20 *(extended)* | [AAMLDS](https://www.myhuiban.com/conference/5579) | - | - | - | 2026-12-04 | Xiamen, China |
| 2026-10-20 *(extended)* | [ACEPE](https://www.myhuiban.com/conference/4822) | - | - | - | 2026-11-20 | Sanya, China |
| 2026-10-20 *(extended)* | [AIBDCC](https://www.myhuiban.com/conference/5505) | - | - | - | 2026-10-30 | Chengdu, China |
| 2026-10-20 | [AIIPCC](https://www.myhuiban.com/conference/3360) | - | - | - | 2026-12-11 | Sanya, China |
| 2026-10-20 | [BDEE](https://www.myhuiban.com/conference/3983) | - | - | - | 2027-04-16 | Zhengzhou, China |
| 2026-10-20 | [CCISP](https://www.myhuiban.com/conference/2586) | - | - | - | 2026-11-19 | Hefei, China |
| 2026-10-20 *(extended)* | [CDICS](https://www.myhuiban.com/conference/4563) | - | - | - | 2026-11-27 | Singapore |
| 2026-10-20 | [CEAC](https://www.myhuiban.com/conference/4485) | - | - | - | 2027-03-10 | Hanoi, Vietnam |
| 2026-10-20 | [DASIP](https://www.myhuiban.com/conference/1722) | - | - | - | 2027-01-18 | Glasgow, Scotland, UK |
| 2026-10-20 *(extended)* | [DSIS](https://www.myhuiban.com/conference/2987) | - | - | - | 2026-11-20 | Hangzhou, China |
| 2026-10-20 *(extended)* | [DSIT](https://www.myhuiban.com/conference/2620) | - | - | - | 2026-11-27 | Taicang, China |
| 2026-10-20 | [IC4E](https://www.myhuiban.com/conference/3398) | - | - | - | 2027-03-26 | Fukuoka, Japan |
| 2026-10-20 | [ICBCB](https://www.myhuiban.com/conference/4943) | - | - | - | 2027-03-26 | Xi an, China |
| 2026-10-20 *(extended)* | [ICBDAA](https://www.myhuiban.com/conference/4637) | - | - | - | 2026-11-27 | Singapore |
| 2026-10-20 | [ICBEA](https://www.myhuiban.com/conference/5244) | - | - | - | 2027-03-26 | Xi an, China |
| 2026-10-20 | [ICCAE](https://www.myhuiban.com/conference/1127) | - | - | - | 2027-03-12 | Melbourne, Australia |
| 2026-10-20 | [ICCCS'''](https://www.myhuiban.com/conference/3442) | - | - | - | 2027-04-16 | Shenzhen, China |
| 2026-10-20 | [ICMFM](https://www.myhuiban.com/conference/5205) | - | - | - | 2027-03-01 | Da Nang, Vietnam |
| 2026-10-20 | [ICMMT](https://www.myhuiban.com/conference/4712) | - | - | - | 2027-03-26 | Fukuoka, Japan |
| 2026-10-20 | [ICQH](https://www.myhuiban.com/conference/5532) | - | - | - | 2026-11-19 | Tashkent, Uzbekistan |
| 2026-10-20 *(extended)* | [ICRAIE](https://www.myhuiban.com/conference/4147) | - | - | - | 2026-12-11 | Nanjing, China |
| 2026-10-20 | [IEEE APSCON](https://www.myhuiban.com/conference/4663) | - | - | - | 2027-03-15 | Hyderabad, India |
| 2026-10-20 | [ITEC'](https://www.myhuiban.com/conference/5533) | - | - | - | 2026-11-19 | Tashkent, Uzbekistan |
| 2026-10-20 *(extended)* | [MLNLP](https://www.myhuiban.com/conference/2852) | - | - | - | 2026-12-04 | Xiamen, China |
| 2026-10-20 | [MSIEID](https://www.myhuiban.com/conference/5197) | - | - | - | 2026-12-01 | Kunming, China |
| 2026-10-20 | [MSR](https://www.myhuiban.com/conference/572) | C | A | B1 | 2027-04-26 | Dublin, Ireland |
| 2026-10-20 *(extended)* | [PEESE](https://www.myhuiban.com/conference/5506) | - | - | - | 2026-10-31 | Chengdu, China |
| 2026-10-20 *(extended)* | [PSETC](https://www.myhuiban.com/conference/5024) | - | - | - | 2026-11-13 | Singapore |
| 2026-10-20 *(extended)* | [SGGEA](https://www.myhuiban.com/conference/4823) | - | - | - | 2026-11-20 | Sanya, China |
| 2026-10-21 | [CVNN](https://www.myhuiban.com/conference/5420) | - | - | - | 2027-01-29 | Harbin, China |
| 2026-10-21 | [SEAMS](https://www.myhuiban.com/conference/186) | - | A | B3 | 2027-04-26 | Dublin, Ireland |
| 2026-10-22 *(extended)* | [CFIMA](https://www.myhuiban.com/conference/3380) | - | - | - | 2026-11-20 | Xiamen, China |
| 2026-10-22 *(extended)* | [FCSIT](https://www.myhuiban.com/conference/3261) | - | - | - | 2026-11-20 | Kunming, China |
| 2026-10-22 | [ISCID](https://www.myhuiban.com/conference/2278) | - | - | - | 2026-12-19 | Hangzhou, China |
| 2026-10-22 *(extended)* | [JCCME](https://www.myhuiban.com/conference/2340) | - | - | - | 2026-11-20 | Yantai, China |
| 2026-10-22 | [PRIA](https://www.myhuiban.com/conference/5889) | - | - | - | 2026-11-06 | Zhengzhou, China |
| 2026-10-23 | [3EAI](https://www.myhuiban.com/conference/5852) | - | - | - | 2026-11-06 | Tumxuk, China |
| 2026-10-23 *(extended)* | [AIGC](https://www.myhuiban.com/conference/4601) | - | - | - | 2026-12-26 | Guangzhou, China |
| 2026-10-23 | [CHASE'](https://www.myhuiban.com/conference/4316) | - | B | - | 2027-04-26 | Dublin, Ireland |
| 2026-10-23 | [CVM](https://www.myhuiban.com/conference/2906) | C | - | - | 2027-04-09 | Singapore |
| 2026-10-23 | [DILSCM](https://www.myhuiban.com/conference/5885) | - | - | - | 2026-11-06 | Jiangmen, China |
| 2026-10-24 | [TRUST](https://www.myhuiban.com/conference/5744) | - | - | - | 2027-03-07 | Washington DC, USA |
| 2026-10-25 | [CTCNet](https://www.myhuiban.com/conference/4788) | - | - | - | 2026-12-25 | Xiamen, China |
| 2026-10-25 | [FORGE](https://www.myhuiban.com/conference/5210) | - | - | - | 2027-04-26 | Dublin, Ireland |
| 2026-10-25 *(extended)* | [ICCNS](https://www.myhuiban.com/conference/1093) | - | - | - | 2026-12-19 | Harbin, China |
| 2026-10-25 *(extended)* | [ICCR](https://www.myhuiban.com/conference/4872) | - | - | - | 2026-12-11 | Tokyo, Japan |
| 2026-10-25 *(extended)* | [ICVIP](https://www.myhuiban.com/conference/2756) | - | - | - | 2026-12-11 | Shanghai, China |
| 2026-10-26 | [ISBI](https://www.myhuiban.com/conference/479) | - | - | B1 | 2027-05-25 | Lausanne, Switzerland |
| 2026-10-28 | [AROB](https://www.myhuiban.com/conference/5718) | - | C | - | 2027-01-19 | Beppu, Japan |
| 2026-10-28 | [RECOMB](https://www.myhuiban.com/conference/477) | B | B | A2 | 2027-05-17 | Toronto, Ontario, Canada |
| 2026-10-29 | [ICIPCN](https://www.myhuiban.com/conference/5784) | - | - | - | 2027-01-21 | Tamil Nadu, India |
| 2026-10-29 | [ICPECA](https://www.myhuiban.com/conference/5798) | - | - | - | 2027-01-29 | Shenyang, China |
| 2026-10-29 | [IDCIoT](https://www.myhuiban.com/conference/4974) | - | - | - | 2027-01-21 | Ottapalam, Kerala, India |
| 2026-10-30 | [AEEES](https://www.myhuiban.com/conference/3920) | - | - | - | 2027-03-19 | Chengdu, China |
| 2026-10-30 *(extended)* | [AIAT](https://www.myhuiban.com/conference/4951) | - | - | - | 2026-12-11 | Tokyo, Japan |
| 2026-10-30 | [AISNS](https://www.myhuiban.com/conference/5135) | - | - | - | 2026-11-13 | Chongqing, China |
| 2026-10-30 | [AST](https://www.myhuiban.com/conference/5208) | - | C | - | 2027-04-26 | Dublin, Ireland |
| 2026-10-30 | [CAIN](https://www.myhuiban.com/conference/5209) | - | B | - | 2027-04-25 | Dublin, Ireland |
| 2026-10-30 | [EECT'](https://www.myhuiban.com/conference/3939) | - | - | - | 2027-03-27 | Shanghai, China |
| 2026-10-30 | [FormaliSE](https://www.myhuiban.com/conference/3047) | - | - | - | 2027-04-26 | Dublin, Ireland |
| 2026-10-30 | [ICAIRC](https://www.myhuiban.com/conference/4460) | - | - | - | 2026-11-13 | Xiamen, China |
| 2026-10-30 | [ICCECE'](https://www.myhuiban.com/conference/3965) | - | - | - | 2027-01-15 | Xiangtan, China |
| 2026-10-30 | [ICESD](https://www.myhuiban.com/conference/3440) | - | - | - | 2027-03-28 | Tokyo, Japan |
| 2026-10-30 | [ICICT''](https://www.myhuiban.com/conference/2785) | - | - | - | 2027-03-10 | Honolulu, Hawaii, USA |
| 2026-10-30 | [ICIM](https://www.myhuiban.com/conference/2376) | - | - | - | 2027-03-19 | Cambridge, UK |
| 2026-10-30 | [ICIN](https://www.myhuiban.com/conference/1578) | - | - | - | 2027-03-15 | Pisa, Italy |
| 2026-10-30 *(extended)* | [ICIT''](https://www.myhuiban.com/conference/2996) | - | - | - | 2026-12-11 | Shanghai, China |
| 2026-10-30 | [ICLIST](https://www.myhuiban.com/conference/5825) | - | - | - | 2027-03-18 | Bangkok, Thailand |
| 2026-10-30 *(extended)* | [ICNCC](https://www.myhuiban.com/conference/2949) | - | - | - | 2026-12-10 | Kuala Lumper, Malaysia |
| 2026-10-30 | [ICSA](https://www.myhuiban.com/conference/176) | C | A | B1 | 2027-03-08 | Sydney, Australia |
| 2026-10-30 | [IDIM](https://www.myhuiban.com/conference/5799) | - | - | - | 2027-01-30 | Bali, Indonesia |
| 2026-10-30 | [IWEG](https://www.myhuiban.com/conference/3168) | - | - | - | 2026-11-22 | Shanghai, China |
| 2026-10-31 | [ADNTIIC](https://www.myhuiban.com/conference/1810) | - | - | - | 2026-11-17 | Montevideo, Uruguay |
| 2026-10-31 | [AICARE](https://www.myhuiban.com/conference/5820) | - | - | - | 2027-03-06 | Kolkata, India |
| 2026-10-31 | [ESIHISE](https://www.myhuiban.com/conference/1940) | - | - | - | 2026-11-19 | Montevideo, Uruguay |
| 2026-10-31 | [HCITISI](https://www.myhuiban.com/conference/1809) | - | - | - | 2026-11-26 | Cordoba, Argentina |
| 2026-10-31 | [L&T](https://www.myhuiban.com/conference/4965) | - | - | - | 2027-02-01 | Jeddah, Saudi Arabia |
| 2026-10-31 | [RadarConf](https://www.myhuiban.com/conference/2080) | - | - | - | 2027-05-01 | Bangalore, India |
| 2026-10-31 | [SAFEPROCESS](https://www.myhuiban.com/conference/5628) | - | C | - | 2027-06-29 | Delft, the Netherlands |
| 2026-10-31 | [SIROCCO](https://www.myhuiban.com/conference/996) | - | B | B2 | 2027-06-02 | Larnaca, Cyprus |
| 2026-11-01 | [CEES](https://www.myhuiban.com/conference/2576) | - | - | - | 2027-04-28 | Osaka, Japan |
| 2026-11-01 | [EuroGP](https://www.myhuiban.com/conference/1598) | - | B | B1 | 2027-07-31 | Mainz, Germany |
| 2026-11-01 | [EvoApplications](https://www.myhuiban.com/conference/5202) | - | B | - | 2027-03-31 | Mainz, Germany |
| 2026-11-01 | [EvoCOP](https://www.myhuiban.com/conference/1349) | - | B | B2 | 2027-03-31 | Mainz, Germany |
| 2026-11-01 | [EvoLearn](https://www.myhuiban.com/conference/5853) | - | - | - | 2027-03-31 | Mainz, Germany |
| 2026-11-01 | [EvoMUSART](https://www.myhuiban.com/conference/3416) | - | C | - | 2027-03-31 | Mainz, Germany |
| 2026-11-01 | [HOST](https://www.myhuiban.com/conference/2370) | - | - | - | 2027-05-03 | Washington DC, USA |
| 2026-11-01 | [ICMET](https://www.myhuiban.com/conference/2577) | - | - | - | 2027-04-28 | Osaka, Japan |
| 2026-11-01 | [ICMTS](https://www.myhuiban.com/conference/5831) | - | - | - | 2027-04-05 | Udine, Italy |
| 2026-11-01 | [ICRMV](https://www.myhuiban.com/conference/2565) | - | - | - | 2027-03-19 | Haining, China |
| 2026-11-01 | [IMA](https://www.myhuiban.com/conference/3249) | - | - | - | 2027-01-15 | Sanya, China |
| 2026-11-01 | [ISCAIT](https://www.myhuiban.com/conference/5148) | - | - | - | 2027-01-15 | Chengdu, China |
| 2026-11-02 | [ACE](https://www.myhuiban.com/conference/503) | - | B | B2 | 2027-02-01 | Canberra, Australia |
| 2026-11-02 | [ICST](https://www.myhuiban.com/conference/934) | C | A | B2 | 2027-05-17 | San Sebastian, Spain |
| 2026-11-02 | [STOC](https://www.myhuiban.com/conference/359) | A | A* | A1 | 2027-06-06 | Atlanta, Georgia, USA |
| 2026-11-03 | [HNNDL](https://www.myhuiban.com/conference/5216) | - | - | - | 2027-01-22 | Qingdao, China |
| 2026-11-04 | [ISoIRS](https://www.myhuiban.com/conference/3387) | - | - | - | 2027-04-16 | Shenzhen, China |
| 2026-11-05 | [AITC'](https://www.myhuiban.com/conference/4890) | - | - | - | 2026-11-20 | Hangzhou, China |
| 2026-11-05 *(extended)* | [CCAT](https://www.myhuiban.com/conference/4879) | - | - | - | 2026-12-18 | Fukuoka, Japan |
| 2026-11-05 | [CSTE](https://www.myhuiban.com/conference/4933) | - | - | - | 2027-04-09 | Wuhan, China |
| 2026-11-05 *(extended)* | [GBSCE](https://www.myhuiban.com/conference/5528) | - | - | - | 2026-12-06 | Sydney, Australia |
| 2026-11-05 | [ICBCT](https://www.myhuiban.com/conference/3576) | - | - | - | 2027-03-27 | Sapporo, Japan |
| 2026-11-05 | [ICCGV](https://www.myhuiban.com/conference/4906) | - | - | - | 2027-03-27 | Sapporo, Japan |
| 2026-11-05 | [ICEIT](https://www.myhuiban.com/conference/1391) | - | - | B5 | 2027-03-26 | Chongqing, China |
| 2026-11-05 | [ICFEE](https://www.myhuiban.com/conference/3397) | - | - | - | 2027-03-26 | Kyoto, Japan |
| 2026-11-05 | [ICPC](https://www.myhuiban.com/conference/573) | B | A | A2 | 2027-04-25 | Dublin, Ireland |
| 2026-11-05 | [IS-AII](https://www.myhuiban.com/conference/4994) | - | - | - | 2027-01-09 | to be updated |
| 2026-11-05 | [REFSQ](https://www.myhuiban.com/conference/1850) | C | B | - | 2027-04-12 | Basel, Switzerland |
| 2026-11-05 | [RTAS](https://www.myhuiban.com/conference/349) | B | A | A2 | 2027-05-11 | New York City, New York, USA |
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
| 2026-11-09 | [NOMS](https://www.myhuiban.com/conference/312) | - | B | A2 | 2027-05-10 | Montreal, Quebec, Canada |
| 2026-11-10 | [AAME](https://www.myhuiban.com/conference/2483) | - | - | - | 2027-03-26 | Ningbo, China |
| 2026-11-10 *(extended)* | [CSAI](https://www.myhuiban.com/conference/1972) | - | - | - | 2026-12-18 | Beijing, China |
| 2026-11-10 | [FICMSS](https://www.myhuiban.com/conference/4701) | - | - | - | 2027-01-08 | Xi an, China |
| 2026-11-10 | [ICAMAM](https://www.myhuiban.com/conference/5153) | - | - | - | 2027-01-22 | Tai an, China |
| 2026-11-10 | [ICAPM](https://www.myhuiban.com/conference/3400) | - | - | - | 2027-04-16 | Kyoto, Japan |
| 2026-11-10 | [ICCAI'](https://www.myhuiban.com/conference/3606) | - | - | - | 2027-04-23 | Seoul, South Korea |
| 2026-11-10 | [ICCCV](https://www.myhuiban.com/conference/4008) | - | - | - | 2027-04-02 | Tianjin, China |
| 2026-11-10 | [ICDIP](https://www.myhuiban.com/conference/2082) | - | - | - | 2027-04-16 | Beijing, China |
| 2026-11-10 | [ICIET](https://www.myhuiban.com/conference/3544) | - | - | - | 2027-04-09 | Osaka, Japan |
| 2026-11-10 | [ICMENS](https://www.myhuiban.com/conference/5227) | - | - | - | 2027-03-28 | Osaka, Japan |
| 2026-11-10 *(extended)* | [ICMSR](https://www.myhuiban.com/conference/2901) | - | - | - | 2026-12-18 | Singapore |
| 2026-11-10 | [ICRCA](https://www.myhuiban.com/conference/4886) | - | - | - | 2027-03-26 | Aizuwakamatsu, Japan |
| 2026-11-10 | [IMIP](https://www.myhuiban.com/conference/5237) | - | - | - | 2027-04-23 | Seoul, South Korea |
| 2026-11-10 | [IPAS](https://www.myhuiban.com/conference/5711) | - | C | - | 2027-04-06 | Castellon de la Plana, Spain |
| 2026-11-10 | [IVEC](https://www.myhuiban.com/conference/5350) | - | - | - | 2027-03-15 | Bengaluru, India |
| 2026-11-10 | [RAITS](https://www.myhuiban.com/conference/5224) | - | - | - | 2027-01-22 | Xi an, China |
| 2026-11-10 | [S&P](https://www.myhuiban.com/conference/289) | A | A* | - | 2027-05-18 | Montreal, Canada |
| 2026-11-11 | [ICDE](https://www.myhuiban.com/conference/135) | A | A* | A1 | 2027-05-17 | Copenhagen, Denmark |
| 2026-11-12 | [ICRFCS](https://www.myhuiban.com/conference/5804) | - | - | - | 2027-02-04 | Bengaluru, India |
| 2026-11-12 | [PLDI](https://www.myhuiban.com/conference/164) | A | A* | A1 | 2027-06-05 | Atlanta, Georgia, USA |
| 2026-11-13 | [ACC'](https://www.myhuiban.com/conference/5589) | - | C | - | 2026-12-07 | Melbourne, Australia |
| 2026-11-13 | [CogSIMA](https://www.myhuiban.com/conference/2462) | - | - | - | 2027-06-01 | Veszprém, Hungary |
| 2026-11-13 | [VTS](https://www.myhuiban.com/conference/1489) | C | - | A2 | 2027-04-26 | Napa, California, USA |
| 2026-11-14 | [ACMSE](https://www.myhuiban.com/conference/1412) | - | - | - | 2027-04-15 | Cape Girardeau, Missouri, USA |
| 2026-11-14 | [ECETES](https://www.myhuiban.com/conference/5819) | - | - | - | 2027-03-05 | Berlin, Germany |
| 2026-11-14 | [NNICE](https://www.myhuiban.com/conference/4515) | - | - | - | 2027-01-29 | Dongguan, China |
| 2026-11-15 | [AISC](https://www.myhuiban.com/conference/5586) | - | C | - | 2027-02-01 | Canberra, Australia |
| 2026-11-15 | [AusPDC](https://www.myhuiban.com/conference/5585) | - | C | - | 2027-02-01 | Canberra, Australia |
| 2026-11-15 | [CoMEA](https://www.myhuiban.com/conference/4758) | - | - | - | 2027-05-21 | Beijing, China |
| 2026-11-15 | [ICRITO](https://www.myhuiban.com/conference/1929) | - | - | - | 2027-02-11 | Noida, India |
| 2026-11-15 | [ICSGPS](https://www.myhuiban.com/conference/4697) | - | - | - | 2027-01-15 | Gold Coast, Australia |
| 2026-11-15 | [ITCSREC](https://www.myhuiban.com/conference/5588) | - | - | - | 2027-02-01 | Canberra, Australia |
| 2026-11-15 | [PEED](https://www.myhuiban.com/conference/5576) | - | - | - | 2027-02-27 | Nanjing, China |
| 2026-11-15 | [Pan Pac](https://www.myhuiban.com/conference/5794) | - | - | - | 2027-01-25 | Maui, Hawaii, USA |
| 2026-11-15 | [WCCCT](https://www.myhuiban.com/conference/3451) | - | - | - | 2027-04-16 | Chengdu, China |
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
| 2026-11-20 *(extended)* | [ACAI](https://www.myhuiban.com/conference/2855) | - | - | - | 2026-12-18 | Hangzhou, China |
| 2026-11-20 | [AIRC](https://www.myhuiban.com/conference/4929) | - | - | - | 2027-04-06 | Tempe, Arizona, USA |
| 2026-11-20 | [AISRA](https://www.myhuiban.com/conference/5746) | - | - | - | 2026-12-04 | Chengdu, China |
| 2026-11-20 | [ALIS](https://www.myhuiban.com/conference/5587) | - | - | - | 2027-02-01 | Canberra, Australia |
| 2026-11-20 | [CESEE](https://www.myhuiban.com/conference/4474) | - | - | - | 2027-06-17 | Milan, Italy |
| 2026-11-20 | [ETLTC](https://www.myhuiban.com/conference/4946) | - | - | - | 2027-01-25 | Aizuwakamatsu, Japan |
| 2026-11-20 | [IAEAC](https://www.myhuiban.com/conference/1764) | - | - | - | 2027-03-12 | Chongqing, China |
| 2026-11-20 | [ICETM'](https://www.myhuiban.com/conference/4947) | - | - | - | 2027-01-25 | Aizuwakamatsu, Japan |
| 2026-11-20 | [ICGDA](https://www.myhuiban.com/conference/2348) | - | - | - | 2027-04-05 | Paris, France |
| 2026-11-20 | [ICMDA](https://www.myhuiban.com/conference/4930) | - | - | - | 2027-04-08 | Hiroshima, Japan |
| 2026-11-20 | [ICOCE](https://www.myhuiban.com/conference/5229) | - | - | - | 2027-04-07 | Singapore |
| 2026-11-20 | [ICPEGE](https://www.myhuiban.com/conference/5090) | - | - | - | 2027-01-28 | Shenyang, China |
| 2026-11-20 | [ICoSSE](https://www.myhuiban.com/conference/4928) | - | - | - | 2027-04-05 | Paris, France |
| 2026-11-20 | [ISDEA](https://www.myhuiban.com/conference/1061) | - | - | - | 2027-04-24 | Okinawa, Japan |
| 2026-11-20 | [ITEC](https://www.myhuiban.com/conference/3125) | - | - | - | 2027-06-16 | Novi, Michigan, USA |
| 2026-11-20 *(extended)* | [MLBDM](https://www.myhuiban.com/conference/4434) | - | - | - | 2026-12-18 | Hangzhou, China |
| 2026-11-20 | [MLCI](https://www.myhuiban.com/conference/5200) | - | - | - | 2027-04-24 | Okinawa, Japan |
| 2026-11-20 | [PAKDD](https://www.myhuiban.com/conference/157) | C | B | - | 2027-06-29 | Wellington, New Zealand |
| 2026-11-20 | [PIERS](https://www.myhuiban.com/conference/2084) | - | - | - | 2027-05-09 | Daejeon, South Korea |
| 2026-11-20 *(extended)* | [PRDM](https://www.myhuiban.com/conference/3781) | - | - | - | 2026-12-18 | Hangzhou, China |
| 2026-11-22 | [DASFAA](https://www.myhuiban.com/conference/158) | B | B | B1 | 2027-05-28 | Shenyang, China |
| 2026-11-22 | [WorldCist](https://www.myhuiban.com/conference/5636) | - | C | - | 2027-03-23 | Cape Town, South Africa |
| 2026-11-25 | [CVAI](https://www.myhuiban.com/conference/4993) | - | - | - | 2027-03-25 | Hong Kong, China |
| 2026-11-25 | [DSN](https://www.myhuiban.com/conference/187) | B | A | A1 | 2027-06-22 | Berlin, Germany |
| 2026-11-25 | [FCCE](https://www.myhuiban.com/conference/5563) | - | - | - | 2027-04-16 | Hefei, China |
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
| 2026-11-30 | [CROS](https://www.myhuiban.com/conference/5367) | - | - | - | 2027-04-27 | Sao Paulo, Brazil |
| 2026-11-30 *(extended)* | [DSSE](https://www.myhuiban.com/conference/5469) | - | - | - | 2026-12-25 | Shanghai, China |
| 2026-11-30 | [EPEMR](https://www.myhuiban.com/conference/5442) | - | - | - | 2027-05-28 | Guilin, China |
| 2026-11-30 | [FAIML](https://www.myhuiban.com/conference/3031) | - | - | - | 2027-05-07 | China |
| 2026-11-30 | [HPSR](https://www.myhuiban.com/conference/908) | - | C | - | 2027-06-15 | Paris, France |
| 2026-11-30 | [ICAIBD](https://www.myhuiban.com/conference/2926) | - | - | - | 2027-05-28 | Chengdu, China |
| 2026-11-30 | [ICBBT](https://www.myhuiban.com/conference/4511) | - | - | - | 2027-05-21 | Qingdao, China |
| 2026-11-30 | [ICITSC](https://www.myhuiban.com/conference/5848) | - | - | - | 2027-03-05 | Chengdu, China |
| 2026-11-30 | [ICNLP](https://www.myhuiban.com/conference/3366) | - | - | - | 2027-04-16 | Zhenjiang, China |
| 2026-11-30 | [ICRCICN](https://www.myhuiban.com/conference/1780) | - | - | - | 2027-02-27 | Kalyani, West Bengal, India |
| 2026-11-30 | [IEAI](https://www.myhuiban.com/conference/3597) | - | - | - | 2027-04-28 | Seoul, South Korea |
| 2026-11-30 *(extended)* | [ISSE'](https://www.myhuiban.com/conference/5468) | - | - | - | 2026-12-25 | Shanghai, China |
| 2026-11-30 | [MSIE](https://www.myhuiban.com/conference/2968) | - | - | - | 2027-04-28 | Seoul, South Korea |
| 2026-11-30 | [SECON](https://www.myhuiban.com/conference/311) | B | B | B1 | 2027-05-05 | Lisbon, Portugal |
| 2026-12-01 | [CETA](https://www.myhuiban.com/conference/4931) | - | - | - | 2027-04-16 | Ankara, Turkey |
| 2026-12-01 | [CPAIOR](https://www.myhuiban.com/conference/2409) | - | B | - | 2027-06-01 | Toulouse, France |
| 2026-12-01 | [FSE'](https://www.myhuiban.com/conference/585) | B | B | A2 | 2027-05-24 | Maastricht, the Netherlands |
| 2026-12-01 | [ICEEE'](https://www.myhuiban.com/conference/2393) | - | - | - | 2027-04-16 | Ankara, Turkey |
| 2026-12-01 | [MOST](https://www.myhuiban.com/conference/4683) | - | - | - | 2027-04-04 | Pomona, California, USA |
| 2026-12-01 | [OSDI](https://www.myhuiban.com/conference/358) | A | A* | A1 | 2027-07-07 | Baltimore, Maryland, USA |
| 2026-12-01 | [RSSM](https://www.myhuiban.com/conference/5387) | - | - | - | 2027-01-15 | Chongqing, China |
| 2026-12-01 | [WoWMoM](https://www.myhuiban.com/conference/652) | C | C | B3 | 2027-06-21 | Irvine, California, USA |
| 2026-12-03 | [GAIIS](https://www.myhuiban.com/conference/5149) | - | - | - | 2027-03-26 | Guangzhou, China |
| 2026-12-03 | [PODS](https://www.myhuiban.com/conference/138) | B | A* | A1 | 2027-06-13 | Huntington Beach, California, USA |
| 2026-12-04 | [AIVRV](https://www.myhuiban.com/conference/4446) | - | - | - | 2026-12-18 | Wuhan, China |
| 2026-12-04 | [Confluence](https://www.myhuiban.com/conference/5783) | - | - | - | 2027-01-21 | Noida, India |
| 2026-12-05 | [AITC](https://www.myhuiban.com/conference/3372) | - | - | - | 2027-05-07 | Lianyungang, China |
| 2026-12-05 | [ICCCBDA](https://www.myhuiban.com/conference/3371) | - | - | - | 2027-04-23 | Chengdu, China |
| 2026-12-05 | [ICKECS](https://www.myhuiban.com/conference/5362) | - | - | - | 2027-04-23 | Chickballapur, India |
| 2026-12-05 | [ISAI'](https://www.myhuiban.com/conference/4935) | - | - | - | 2027-04-23 | Chengdu, China |
| 2026-12-05 | [NISS'](https://www.myhuiban.com/conference/2979) | - | - | - | 2027-04-27 | Casablanca, Morocco |
| 2026-12-07 | [ICAPS](https://www.myhuiban.com/conference/417) | B | A* | A2 | 2027-06-27 | Columbia, South Carolina, USA |
| 2026-12-07 | [IPMI](https://www.myhuiban.com/conference/465) | - | - | - | 2027-06-27 | Lake Stukely, Quebec, Canada |
| 2026-12-08 | [CCGRID](https://www.myhuiban.com/conference/342) | C | B | A1 | 2027-05-17 | Dallas-Fort Worth, Texas, USA |
| 2026-12-08 | [ETS](https://www.myhuiban.com/conference/1485) | C | B | B2 | 2027-05-24 | London, UK |
| 2026-12-09 | [ICOECA](https://www.myhuiban.com/conference/5822) | - | - | - | 2027-03-11 | Bengaluru, Karnataka, India |
| 2026-12-09 | [WISTP](https://www.myhuiban.com/conference/785) | - | C | - | 2027-03-19 | Djerba, Tunisia |
| 2026-12-10 | [EECR](https://www.myhuiban.com/conference/2857) | - | - | - | 2027-04-23 | Shenzhen, China |
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
| 2026-12-12 | [ICTMIM](https://www.myhuiban.com/conference/5824) | - | - | - | 2027-03-18 | Kanyakumari, India |
| 2026-12-14 | [ARCS](https://www.myhuiban.com/conference/210) | - | - | B2 | 2027-03-09 | Magdeburg, Germany |
| 2026-12-15 | [AISCN](https://www.myhuiban.com/conference/5832) | - | - | - | 2027-04-09 | Taichung, Taiwan |
| 2026-12-15 | [CI2A](https://www.myhuiban.com/conference/5826) | - | - | - | 2027-03-19 | Yogyakarta, Indonesia |
| 2026-12-15 | [ICDF2C](https://www.myhuiban.com/conference/1851) | C | - | - | 2027-06-25 | New York City, New York, USA |
| 2026-12-15 | [ICMI'](https://www.myhuiban.com/conference/5733) | - | - | - | 2027-05-01 | Mt. Pleasant, Michigan, USA |
| 2026-12-15 | [IEEE CONECCT](https://www.myhuiban.com/conference/4809) | - | - | - | 2027-03-13 | Bangalore, India |
| 2026-12-15 | [ITET](https://www.myhuiban.com/conference/4291) | - | - | - | 2027-05-28 | Okayama, Japan |
| 2026-12-15 | [UNet](https://www.myhuiban.com/conference/1687) | - | - | - | 2027-05-25 | Montreal, Quebec, Canada |
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
| 2026-12-21 | [GAIIP](https://www.myhuiban.com/conference/5421) | - | - | - | 2027-03-05 | Guangzhou, China |
| 2026-12-23 | [ISDS](https://www.myhuiban.com/conference/5414) | - | - | - | 2027-03-12 | Tianjin, China |

---

Data: **Conference Partner (myhuiban.com)**, free to use with attribution. Ranking values are reproduced from CCF / CORE / QUALIS — cite those bodies for the rankings themselves. The repository's MIT licence covers its code, not this data.
