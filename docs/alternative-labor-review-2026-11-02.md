# Alternative labor indicators - November 2, 2026

These three records apply the [source-review template](source-review-template.md)
to evidence already collected on 2026-11-02. Applying the template does not represent
another publisher visit or export test. Observed results, publisher-documented
methods, and unresolved checks are distinguished below. No missing release dates,
collection dates, revision identifiers, or rights grants have been inferred.

The existing catalog descriptions were clarified without adding duplicate URLs.
Canonical URLs, resource IDs, recorded creation dates, schema version, and conservative
index fields are preserved. This review does not qualify model inputs or establish
catalog-wide source freshness. File receipts identify inspected bytes; the datasets
are not redistributed here, and hashes do not establish accuracy or reuse rights.

## Indeed Wage Tracker

### Review scope and identity

| Field | Record |
| --- | --- |
| Review date and method | 2026-11-02; AI-assisted inspection of publisher documentation and retrieved country CSV content. |
| Publisher and canonical URL | Indeed Hiring Lab; [data repository](https://github.com/hiring-lab/indeed-wage-tracker). |
| Existing catalog identity | `awesome-economic-data:source:r-2aaff649fe40d8c7`; created `2026-08-30`, unchanged. |
| Scope and evidence | Repository README methodology, schema, and license plus the [country CSV](https://github.com/hiring-lab/indeed-wage-tracker/blob/main/posted-wage-growth-by-country.csv), checked 2026-11-02. Country export inspected; sector export not tested. |

### Measurement contract

| Field | Record |
| --- | --- |
| Measure and evidence type | Publisher-documented year-over-year advertised wage growth derived from job postings. It measures offers, not actual payroll earnings or a wage level. |
| Population and selection | Job-title, region, and salary-type cells within each country. The publisher calculates median advertised pay in each cell, then the median annual change across cells; it follows categories rather than the same workers. Salary disclosure and platform coverage can change. |
| Units and transformations | Annual wage-growth rates, not currency levels. The publisher documents no seasonal adjustment. `posted_wage_growth_yoy` is separate from the headline trailing three-month average, `posted_wage_growth_yoy_3moavg`; raw numeric scaling was not independently qualified. |
| Comparability and changes | No historical definition-break audit was performed. The dynamic repository does not establish the method in force at every past release. Do not compound overlapping annual growth rates into an earnings index. |

### Timing and vintage

| Field | Record |
| --- | --- |
| Reference period | Publisher schema defines `month` as the month the job was first posted. The measure compares advertised wages with a year earlier. |
| Collection period | Unknown exact observation/extraction dates; a posting month does not establish the collection window. |
| Publication and vintage | Exact release timestamp, pinned commit SHA, and revision policy not recorded in this review. The retrieved history is not proof of originally published values. |
| Retrieval date and observed coverage | 2026-11-02; 1,012 country-file observations, including 92 U.S. monthly rows from January 2019 through August 2026. |
| Cadence and freshness limits | Publisher-documented monthly frequency. The tested U.S. history ends in August 2026; no November release or latest-available status was verified. |

### Access and artifact receipt

| Field | Record |
| --- | --- |
| Tested route and conditions | Public repository to `posted-wage-growth-by-country.csv`, retrieved through the GitHub connector. No publisher sign-in or purchase was required; this was not a separate unauthenticated HTTP test. |
| Retrieved artifact | Country CSV content parsed: 1,012 observations. Fields: `jobcountry`, `country`, `month`, `n_obs`, `posted_wage_growth_yoy`, `posted_wage_growth_yoy_3moavg`. The U.S. subset's count and endpoints were checked. |
| Snapshot identity | Mutable repository/file URLs only. No pinned revision, exact-byte SHA-256, or byte count was captured; a later retrieval may return different content. |
| Untested access | Sector CSV, underlying posting microdata, API access, historical release snapshots, and completeness of every country/period. |

### Terms and interpretation limits

| Field | Record |
| --- | --- |
| License and terms evidence | Repository README explicitly states CC BY 4.0 with Hiring Lab attribution; checked 2026-11-02 at the canonical source. |
| Reuse and attribution | The documented grant covers Hiring Lab's published data and files under CC BY 4.0, including attribution obligations. It does not establish access or rights to underlying posting microdata. |
| Interpretation limits | Offers differ from realized earnings. Changing salary disclosure and posting composition can affect the signal; category matching does not turn it into a worker pay tracker. |

### Catalog decision and follow-up

| Field | Record |
| --- | --- |
| Catalog action | Retained and clarified the existing entry: advertised wages, cell matching, no seasonal adjustment, and CC BY 4.0. Identity and creation date unchanged. |
| Unresolved checks | Before reproducible analysis, pin the repository revision and capture a file digest, verify rate encoding, and inspect revision/method notices. Test sector exports separately before claiming their retrieval. |
| Recheck triggers | New releases, methodology or license notices, changed salary coverage/schema, or a failed file route. |

## Gusto Real Time Economic Data

### Review scope and identity

| Field | Record |
| --- | --- |
| Review date and method | 2026-11-02; AI-assisted publisher-documentation review, browser export, and local CSV inspection. |
| Publisher and canonical URL | Gusto; [real-time data dashboard](https://gusto.com/resources/gusto-insights/real-time-economic-data). |
| Existing catalog identity | `awesome-economic-data:source:r-bcd694b1a75086a5`; created `2026-08-30`, unchanged. |
| Scope and evidence | Dashboard, [September release methodology](https://gusto.com/resources/gusto-insights/sep-2026-smb-jobs-report), [Average Hourly Earnings](https://gusto.com/resources/gusto-insights/average-hourly-earnings), and [footer terms](https://gusto.com/legal/terms), checked 2026-11-02. Only the earnings export was tested. |

### Measurement contract

| Field | Record |
| --- | --- |
| Measure and evidence type | Actual payroll records underlie monthly jobs, average hourly earnings, and new-hire pay indicators. The published aggregates use sampling, weighting, and adjustment; they are not vacancy offers or a census of U.S. workers. |
| Population and selection | Publisher describes roughly 100,000 sampled U.S. businesses with 1-49 employees from the larger platform population. QCEW calibrates industry, size, and region; Census Business Dynamics Statistics calibrates company ages. New hires and workers included in overall earnings are different populations. |
| Units and transformations | Earnings levels in dollars per hour, with `earnings_level` and `earnings_seasonally_adjusted` in the tested CSV. Publisher documents X-13ARIMA-SEATS adjustment, annual-change views, and a three-month rolling average for new-hire starting pay; the new-hire export was not tested. |
| Comparability and changes | Independent payroll collection still relies on official calibration and platform selection. No historical methodology-break audit or comprehensive pay-component audit was performed. |

### Timing and vintage

| Field | Record |
| --- | --- |
| Reference period | Monthly payroll-based indicators; `month` labels the exported period. Exact payroll cutoff rules were not established. |
| Collection period | Exact processing/settlement windows unknown; late payrolls can enter later revisions. |
| Publication and vintage | Publisher documents revisions as payrolls settle. No immutable release ID or originally published vintage was established; the file digest below identifies only the retrieved bytes. |
| Retrieval date and observed coverage | 2026-11-02; earnings CSV spans January 2019 through October 2026, with 2,632 rows across total, industry, firm-size, and region series. |
| Cadence and freshness limits | Publisher advertises monthly releases. The earnings page/export displayed October observations while the landing-page readback showed September and a November 3 next release. No coherent latest release across all pages was established. |

### Access and artifact receipt

| Field | Record |
| --- | --- |
| Tested route and conditions | Average Hourly Earnings page, Level and Seasonally adjusted view, then **Download CSV**; succeeded without sign-in or payment. The resulting CSV contained both unadjusted and adjusted columns. |
| Retrieved artifact | `gusto_average_hourly_earnings.csv`; 2,632 rows. Fields: `month`, `series`, `key`, `earnings_level`, `earnings_seasonally_adjusted`. Counts: Total 94, Industry 1,786, Firm size 376, Region 376. Coverage endpoints and series counts were checked. |
| Snapshot identity | 109326 bytes; SHA-256 `92e00a792ff9f42e41d6b33ae9bb5244c555d3f18c3de13a63f4458e46776d7b`. No immutable publisher archive or release ID was established. |
| Untested access | Jobs and new-hire exports, payroll microdata, API access, historical release archives, and row-by-row accuracy. |

### Terms and interpretation limits

| Field | Record |
| --- | --- |
| License and terms evidence | Footer leads to employer service terms, checked 2026-11-02. No dataset-specific open redistribution license was established. |
| Reuse and attribution | Public CSV retrieval does not establish redistribution, commercial-use, or other dataset permission. Applicable dataset rights and attribution conditions remain unresolved. |
| Interpretation limits | Small-business platform selection, official-data calibration, adjustment, and revisions limit national interpretation. New-hire pay is not earnings growth for the same workers. |

### Catalog decision and follow-up

| Field | Record |
| --- | --- |
| Catalog action | Retained and clarified the existing payroll-based entry, population, calibration, revisions, and unresolved redistribution rights. Identity and creation date unchanged. |
| Unresolved checks | Reconcile the page/export release discrepancy before calling a release current; establish dataset-specific terms before redistribution or assuming permission; test jobs/new-hire files and retain release snapshots before using them. |
| Recheck triggers | A new release, changed file/schema, revised weighting or methods, dataset terms, or a changed download route. |

## Square Payroll Index

### Review scope and identity

| Field | Record |
| --- | --- |
| Review date and method | 2026-11-02; AI-assisted publisher-methodology review, browser export, and local CSV inspection. |
| Publisher and canonical URL | Square; [Square Payroll Index](https://squareup.com/us/en/the-bottom-line/tools/square-payroll-index). |
| Existing catalog identity | `awesome-economic-data:source:r-4358c78294b33d08`; created `2026-08-30`, unchanged. |
| Scope and evidence | Canonical page, embedded [overall hourly-earnings chart](https://datawrapper.dwcdn.net/TZNea/61/), and [methodology](https://squareup.com/us/en/press/square-payroll-index-methodology), checked 2026-11-02. Only the overall earnings percentile export was tested. |

### Measurement contract

| Field | Record |
| --- | --- |
| Measure and evidence type | Payroll-derived hourly earnings for retail and food-and-drink workers. The tested export gives earnings percentiles; a separate growth tracker follows matched worker-employer pairs. |
| Population and selection | Square payroll workers in those industries. Publisher excludes bonuses, commissions, contractors, and stubs without hours; national series use geographic population weights. The matched growth sample favors workers with at least a year at the same employer. |
| Units and transformations | Earnings in dollars per hour: regular wages, overtime, and tips divided by hours; base wages contain regular wages only. No seasonal adjustment. The separate growth tracker smooths median twelve-month matched-pair changes over three months; it is not the downloaded percentile-level series. |
| Comparability and changes | Platform, industry, geographic-weighting, and tenure selection limit comparisons with all workers or other trackers. No historical definition-break audit was performed. |

### Timing and vintage

| Field | Record |
| --- | --- |
| Reference period | `pay_month` in the tested export; publisher method selects the last payroll run per employee/employer in a month. |
| Collection period | Exact processing/extraction windows unknown; the pay-month label alone does not establish them. |
| Publication and vintage | Chart version `/TZNea/61/` observed; exact publication date, revision policy, and immutability of the version URL not established. The file digest identifies the inspected bytes. |
| Retrieval date and observed coverage | 2026-11-02; 95 monthly rows from January 2017 through November 2024. |
| Cadence and freshness limits | Canonical page advertises monthly updates, but the tested export ends in November 2024. It verifies historical aggregate access, not current monthly coverage. |

### Access and artifact receipt

| Field | Record |
| --- | --- |
| Tested route and conditions | Canonical page to embedded overall hourly-earnings chart, then **Get the data**; succeeded without sign-in or payment. |
| Retrieved artifact | `data-TZNea.csv`; 95 rows. Fields: `pay_month`, `10th Percentile`, `Median`, `90th Percentile`. Row count and coverage endpoints were checked. |
| Snapshot identity | 4473 bytes; SHA-256 `262ca1b2b362ae1ba9411c64a183cfcc7f74cef5b01a06d9cb2651e6263166a7`. Chart version recorded above; no immutable publisher file archive established. |
| Untested access | Base-wage, sector, metro, and growth exports; API access, payroll microdata, historical release archives, and current coverage. |

### Terms and interpretation limits

| Field | Record |
| --- | --- |
| License and terms evidence | Public chart and methodology inspected 2026-11-02; no dataset-specific open reuse license or grant was established. The page's measure definitions are not licensing permission. |
| Reuse and attribution | Public historical export access does not establish redistribution or commercial-use rights. Dataset-specific permission and attribution conditions remain unresolved. |
| Interpretation limits | Narrow platform/industry coverage, geographic weights, no seasonal adjustment, and the historical cutoff limit interpretation. Percentile levels and matched-worker growth must remain distinct. |

### Catalog decision and follow-up

| Field | Record |
| --- | --- |
| Catalog action | Retained the pre-existing entry after satisfying the requested bulk-access and methodology condition for this historical aggregate series. Clarified the November 2024 cutoff; identity and creation date unchanged. |
| Unresolved checks | Obtain a newer export before claiming current coverage, establish dataset terms before reuse beyond verified permission, and test each additional chart variant before claiming its access. |
| Recheck triggers | New chart versions or data periods, changed download controls, publisher method/terms notices, or broken embedded links. |

## Refinements suggested by the linked discussion

The [shared chart-building conversation](https://chatgpt.com/share/6ae89e86-8658-83e8-85fd-c4ef2d4f3b89) and [Hacker News discussion](https://news.ycombinator.com/item?id=50336840) are discovery and interpretation sources. Publisher documents control the factual conclusions below. These lessons inform the review template; they do not change the schema or admit additional catalog sources.

- **Version the meaning as well as the file.** Census's [December 3, 2025 change notice](https://www.census.gov/hfp/btos/downloads/AI%20Question%20Wording%20Updates.pdf) documents the November 17 expansion from production-related AI use to any business function and starts a new time series after an observed level shift. Preserve effective question wording and break dates; do not join those segments as continuous adoption growth.
- **Separate historical instrument wording from current labels.** The browser-rendered [BTOS About the Data page](https://www.census.gov/hfp/btos/about), reviewed November 2, dates the later instrument update to the October 19, 2026 collection and now describes earlier AI observations with SI labels. Preserve reference, collection, release, and retrieval dates separately. A current label alone does not establish what historical respondents were asked.
- **Specify the transformation and population.** Six biweekly observations span roughly twelve weeks, not six. Keep raw and smoothed series separate, never smooth across a definition break, and show uncertainty when available. Census describes supplements as pooled six-panel snapshots; they cannot be treated as continuous biweekly histories. The same discipline separates Indeed's offers, Gusto's new hires, and Square's matched-worker growth.
- **Investigate response changes without inventing effects.** One HN commenter says they stopped responding. That is an anecdote, not evidence of population-wide nonresponse or its direction. Census acknowledges nonresponse-bias risk. Review response rates, sample composition, and any wording experiments before attributing a change in measured adoption to terminology or political trust.

The [source-review template](source-review-template.md) now records the exact series, population, units, adjustment, smoothing, method effective dates, tested export scope, and unresolved terms beside the retrieval evidence. The generated index remains conservative: this prose review does not change its `unreviewed` evidence status or `unknown` access and authority fields.

## Validation

All three canonical commands passed on the final candidate based on current main: 74 unit tests, README validation (126 resources, 20 Contents entries), and the resource-index synchronization check. Compared with that base, only the three labor summaries change in the generated records; all 126 existing IDs and creation dates are preserved. No new canonical URL is admitted by this change.

Each completed record was checked for all 23 template fields and its existing catalog identity. Local documentation links, ASCII text, and whitespace checks passed. The creation-date configuration, source-admission manifest, resource-index contract, schema version, and licensing files are unchanged from the base. The existing local Gusto and Square files still match their recorded SHA-256 digests; this is a repeat artifact check, not a fresh publisher retrieval. These local checks do not verify external source freshness or methodology.
