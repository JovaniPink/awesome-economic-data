# Alternative economic and financial data review

Review date: 2026-09-08. Scope: 19 candidates selected for the catalog expansion, using publisher documentation and download listings, schemas, or exposed samples. Seventeen are listed; M5 and dunnhumby are deferred. The resulting catalog has 105 resources and 18 Contents entries. This is a source-specific review, not a catalog-wide recency audit.

No bulk archives were acquired. A visible download listing establishes an offered route, not successful file retrieval, validated rows, unrestricted reuse, or point-in-time fitness. Public reports can qualify as explicitly labeled research resources without an open microdata export. Terms evidence below distinguishes explicit licenses from public-access statements and unresolved redistribution permission. These assessments do not change the index's conservative fields or the separate source-admission manifest.

## Labor and hiring

### Indeed Wage Tracker - listed

- Publisher and canonical URL: [Indeed Hiring Lab](https://github.com/hiring-lab/indeed-wage-tracker). Reviewed 2026-09-08.
- Coverage and method: Monthly country and occupation growth from advertised wages, matching job-title, region, and salary-type cells rather than people. Not seasonally adjusted. Exact usable first observation remains an export check.
- Access evidence: Repository lists country and sector CSVs; README documents country, month, sample count, annual growth, and three-month average fields.
- Terms evidence: Explicit CC BY 4.0 with Hiring Lab attribution.
- Dependencies and uncertainty: Proprietary job postings and changing salary disclosure; methodological similarity to a worker tracker does not make the observations worker pay. Do not compound overlapping annual growth rates.

### Gusto Real Time Economic Data - listed

- Publisher and canonical URL: [Gusto](https://gusto.com/resources/gusto-insights/real-time-economic-data). Reviewed 2026-09-08.
- Coverage and method: Monthly payroll indicators from businesses with 1-49 employees; August 2026 release observed. [Release methodology](https://gusto.com/resources/gusto-insights/aug-2026-smb-jobs-report) describes national calibration using QCEW.
- Access evidence: Dashboard promises CSV for every series; [earnings detail](https://gusto.com/resources/gusto-insights/average-hourly-earnings) provides series context. Export payload and earliest date were not validated.
- Terms evidence: Footer leads to [employer terms](https://gusto.com/legal/terms), not a verified dataset redistribution license. CSV availability grants no inferred open license.
- Dependencies and uncertainty: Census seasonal-adjustment method, QCEW weights, platform selection, and late payroll revisions; independent observations do not imply independent calibration.

### Square Payroll Index - listed as public charts

- Publisher and canonical URL: [Square](https://squareup.com/us/en/the-bottom-line/tools/square-payroll-index). Reviewed 2026-09-08.
- Coverage and method: Monthly retail and food-service employees; [methodology](https://squareup.com/us/en/press/square-payroll-index-methodology) separates base wages from pretax hourly earnings including tips and overtime, excluding bonuses and commissions. Growth matches employee-employer pairs twelve months apart.
- Access evidence: Embedded overall and growth charts and documented measures inspected; bulk CSV/API and historical endpoints remain unverified.
- Terms evidence: Public educational publication; no dataset reuse license established. The page's "Terms" section defines measures, not licensing rights.
- Dependencies and uncertainty: Geographic weighting, platform and tenure selection, no seasonal adjustment; inflation comparison uses CPI-U. This is not an open payroll microdata listing.

## Prices and electricity

### USDA Advertised Grocery Prices - listed

- Publisher and canonical URL: [USDA Agricultural Marketing Service, report 3324](https://mymarketnews.ams.usda.gov/viewReport/3324). Reviewed 2026-09-08.
- Coverage and method: Weekly specialty-crop features from retail grocery advertisements, with commodity and regional detail. Promotions measure offers, not completed purchases or all groceries.
- Access evidence: Publisher report listing and [Market News guidance](https://www.ams.usda.gov/market-news/fruits-vegetables) identify report access and archives. Structured API authentication and continuity back to 2020 remain untested; the listing promises reports rather than a verified API.
- Terms evidence: Public USDA report access observed; no additional dataset-specific license established here.
- Dependencies and uncertainty: Retailer advertising practices, product grade, package, and promotion mix. BLS-independent collection does not establish national representativeness.

### Open Prices - listed

- Publisher and canonical URL: [Open Food Facts on Hugging Face](https://huggingface.co/datasets/openfoodfacts/open-prices). Reviewed 2026-09-08.
- Coverage and method: Irregular community observations with international coverage; no representative U.S. sample or 2020 baseline established.
- Access evidence: Parquet listing and visible sample/schema include price, currency, date, discount, product code, proof type, receipt quantity, and location country. [Data guidance](https://openfoodfacts.github.io/open-prices/guides/data/) and [API documentation](https://github.com/openfoodfacts/open-prices/blob/main/API.md) identify further routes.
- Terms evidence: ODbL declared, with attribution/share-alike obligations; proof images require separate care rather than assuming identical rights.
- Dependencies and uncertainty: OpenStreetMap locations and product/proof matching; selection, duplicates, missing quantities, and changing packages require a coverage audit before any index.

### EIA Electricity Prices and Bills - listed

- Publisher and canonical URL: [U.S. Energy Information Administration](https://www.eia.gov/electricity/sales_revenue_price/). Reviewed 2026-09-08.
- Coverage and method: Annual utility sales, revenues, customers, average prices, and residential bills. Page offers 2024 tables and earlier archives; monthly household bill microdata are not implied.
- Access evidence: Spreadsheet listings include residential average bill and utility sales/revenue tables, with historical Excel and older PDF routes.
- Terms evidence: Public agency downloads; no claim about rights to unrelated third-party content.
- Dependencies and uncertainty: Utility reporting and aggregation; average revenue per kWh differs from a tariff. Separate price, consumption, and customer composition; electricity excludes gas, water, and other utilities.

## Household financial health

### Federal Reserve SHED - listed

- Publisher and canonical URL: [Federal Reserve Board](https://www.federalreserve.gov/consumerscommunities/shed_data.htm). Reviewed 2026-09-08.
- Coverage and method: Annual financial well-being survey, 2013-2025, with special supplements. Self-reports require survey weights and comparable questions.
- Access evidence: Year-specific CSV/Stata ZIP and codebook listings inspected. The 2025 data were revised July 7, 2026; codebook wording changed September 4, 2026. Earlier files also have revision notices.
- Terms evidence: Explicit public-use data designation and direct downloads; this does not grant access to identifiable respondent records.
- Dependencies and uncertainty: Survey selection, weighting, question changes, and revised identifiers. Preserve questionnaire and file versions; no population-wide household linkage was validated.

### New York Fed Consumer Data Bank - listed

- Publisher and canonical URL: [Federal Reserve Bank of New York](https://www.newyorkfed.org/microeconomics/databank). Reviewed 2026-09-08.
- Coverage and method: Quarterly credit balances/delinquency and separate Survey of Consumer Expectations products; dates and frequencies vary by workbook or survey module.
- Access evidence: Credit report underlying-data workbooks and SCE data/questionnaire listings inspected; core survey history reaches 2013, with 2026 releases shown.
- Terms evidence: Public aggregate downloads do not provide restricted Equifax Consumer Credit Panel microdata. No blanket redistribution license established for all products.
- Dependencies and uncertainty: Credit-file coverage differs from survey respondents; preserve third-party provenance and separate realized balances from expectations. Higher total debt alone does not establish distress.

### IRS ZIP-Code Income Data - listed

- Publisher and canonical URL: [IRS Statistics of Income](https://www.irs.gov/statistics/soi-tax-stats-individual-income-tax-statistics-zip-code-data-soi). Reviewed 2026-09-08.
- Coverage and method: Annual ZIP and income-bracket aggregates from tax returns, including wage/salary amounts. Retrieved listing includes 2020 and years through 2022; this is not a claim about every IRS publication's latest year.
- Access evidence: Annual CSV/Excel and documentation listings inspected.
- Terms evidence: Public statistical files, not confidential individual returns; no separate dataset license established here.
- Dependencies and uncertainty: Filing population, suppression, ZIP changes, migration, and publication lag. Returns are tax units rather than workers or households; aggregate wage growth is not a matched person's raise.

### EIA Utility Disconnections - listed

- Publisher and canonical URL: [U.S. Energy Information Administration](https://www.eia.gov/analysis/requests/residential/utility/). Reviewed 2026-09-08.
- Coverage and method: April 2026 publication of monthly calendar-2024 utility survey information on nonpayment notices, disconnections, and reconnections.
- Access evidence: Separate electric and natural-gas utility downloadable files listed alongside survey explanation.
- Terms evidence: Public agency release; not customer account microdata or permission to identify customers.
- Dependencies and uncertainty: Responding utilities, reporting definitions, repeated events, and local disconnection rules. This limited period cannot verify a 2020-onward trend; event counts cannot be interpreted as unique households.

## Corporate accounts

### SEC Financial Statement Data Sets - listed

- Publisher and canonical URL: [U.S. Securities and Exchange Commission](https://www.sec.gov/data-research/sec-markets-data/financial-statement-data-sets). Reviewed 2026-09-08.
- Coverage and method: As-filed financial-statement facts; quarterly download listings span 2009 Q1-2026 Q2. Filing quarter is not necessarily the observation's fiscal quarter.
- Access evidence: ZIP listing and [table definitions](https://www.sec.gov/files/financial-statement-data-sets.pdf) inspected; [EDGAR API documentation](https://www.sec.gov/search-filings/edgar-application-programming-interfaces) describes another route, not a separately cataloged source.
- Terms evidence: SEC explicitly offers files for public analysis and disclaims extraction accuracy; files do not substitute for filings.
- Dependencies and uncertainty: Registrant tags, restatements, acquisitions, units, and incomplete coverage of domestic businesses. December 2024 reprocessing added a NUM segments field; preserve versions before panel comparisons.

### Census Quarterly Financial Report - listed

- Publisher and canonical URL: [U.S. Census Bureau](https://www.census.gov/econ/qfr/historic.html). Reviewed 2026-09-08.
- Coverage and method: Quarterly industry financial estimates; [collection documentation](https://www.census.gov/econ/qfr/collection.html) describes survey collection, and [program overview](https://www.census.gov/econ/overview/mu1400.html) defines covered sectors and size thresholds.
- Access evidence: PDF publications from 1996, Excel financial/summary tables from 2006, and a longer historical database listing are distinct routes. Older database history does not imply unchanged industry coverage.
- Terms evidence: Public aggregate tables; underlying confidential business responses are not offered.
- Dependencies and uncertainty: Sampling, industry coverage, revisions, and national-accounts use. QFR informs BEA profit estimates, so agreement is not wholly independent corroboration.

### Federal Reserve Financial Accounts Z.1 - listed

- Publisher and canonical URL: [Federal Reserve Board](https://www.federalreserve.gov/releases/z1/). Reviewed 2026-09-08.
- Coverage and method: Quarterly sector transactions, financial asset/liability levels, and balance sheets; history varies by series. Current release reviewed covers 2026 Q1; separately labeled preview data are not silently substituted.
- Access evidence: Current-release CSV tables, XML files, explanatory material, and data-download route inspected.
- Terms evidence: Public statistical downloads; source-specific restrictions are not erased for underlying inputs.
- Dependencies and uncertainty: Multiple administrative, survey, and estimated inputs, sector definitions, and revisions. Household/nonprofit aggregates differ from individual households; stock changes include valuation effects and need not equal saving flows.

## Financial markets

### SEC Form N-PORT Data Sets - listed

- Publisher and canonical URL: [U.S. Securities and Exchange Commission](https://www.sec.gov/data-research/sec-markets-data/form-n-port-data-sets). Reviewed 2026-09-08.
- Coverage and method: Publicly disseminated fund portfolio disclosures, with archive listings from October 2019 through June 2026; not all funds or all reported positions are immediately public.
- Access evidence: Quarterly ZIP listings and linked [reporting form](https://www.sec.gov/files/formn-port.pdf) inspected; bulk archives were not downloaded.
- Terms evidence: SEC public dissemination and extraction disclaimers; no private filing access inferred.
- Dependencies and uncertainty: Fund-reported facts, amendments, identifiers, valuation dates, and disclosure delays. Keep reporting period separate from public availability; these are neither live holdings nor market transaction prices.

### New York Fed Reference Rates - listed

- Publisher and canonical URL: [Federal Reserve Bank of New York](https://www.newyorkfed.org/markets/reference-rates). Reviewed 2026-09-08.
- Coverage and method: Business-day overnight funding benchmarks including SOFR and federal funds rates; secured and unsecured markets differ. Start dates vary by rate.
- Access evidence: Publisher links rate-specific histories, calculation explanations, and API access. No service-level guarantee or complete historical payload validation performed.
- Terms evidence: Public benchmark distribution observed; no blanket license inferred for upstream transaction records or downstream benchmark use.
- Dependencies and uncertainty: Underlying transaction sources, filtering, business calendars, and revisions. Rates describe wholesale funding; household loan pricing includes other spreads and contractual terms.

### OFR Short-Term Funding Monitor API - listed

- Publisher and canonical URL: [Office of Financial Research](https://www.financialresearch.gov/short-term-funding-monitor/api/). Reviewed 2026-09-08.
- Coverage and method: Multiple funding series and derived indicators; period and cadence are series-specific rather than one uniform panel.
- Access evidence: Documentation provides HTTPS JSON endpoints, mnemonics, series metadata, searches, and request/response examples. API explicitly requires neither tokens nor registration; no production availability test performed.
- Terms evidence: Explicit public API invitation; upstream terms still require series-level review before redistribution.
- Dependencies and uncertainty: Mixed publishers, calculations, revisions, and missing periods. Retrieve source metadata with observations and avoid counting redistributed reference rates as new independent evidence.

### Kenneth French Data Library - listed

- Publisher and canonical URL: [Kenneth R. French, Dartmouth](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Reviewed 2026-09-08.
- Coverage and method: Constructed research factors and portfolios at daily, weekly, or monthly frequencies; starting dates differ by file.
- Access evidence: CSV/text download listings, portfolio descriptions, and historical archives inspected.
- Terms evidence: Public derived-return downloads; no inferred grant to redistribute underlying licensed CRSP security data. Dataset-specific reuse permission remains a separate check.
- Dependencies and uncertainty: CRSP inputs and construction choices; January 2025 transition from FIZ to CIZ changed monthly return construction. Record the release and methodology; backfilled histories are not contemporaneous tradable prices or investment performance guarantees.

## Deferred learning datasets

### M5 Forecasting Accuracy - deferred

- Publisher and canonical URL: [Kaggle M5 competition, Walmart benchmark](https://www.kaggle.com/competitions/m5-forecasting-accuracy/data). Reviewed 2026-09-08.
- Coverage and method: [Organizers' paper](https://doi.org/10.1016/j.ijforecast.2021.11.013) describes historical 2011-2016 product/store sales with selling prices; useful for price/quantity and forecasting methods, not current national inflation.
- Access and terms evidence: Repeated web extraction of data and [competition rules](https://www.kaggle.com/competitions/m5-forecasting-accuracy/rules) returned no readable content. Current access conditions and reuse rules were not verified; no competition acceptance or downloads attempted.
- Dependencies and next check: Limited Walmart panel and competition-specific rights. Inspect authenticated or browser-visible official rules and file listing before promotion; a paper or mirror cannot resolve current access terms.

### dunnhumby Source Files - deferred

- Publisher and canonical URL: [dunnhumby](https://www.dunnhumby.com/source-files/). Reviewed 2026-09-08.
- Coverage and method: Earlier discovery on this date described real-world-inspired, represented datasets, including two years for 2,500 Complete Journey households. This is a learning candidate, not verified raw current national transactions.
- Access and terms evidence: Implementation recheck repeatedly timed out through web retrieval. Earlier visible download buttons did not establish a verified file/terms route. No archive acquired; current dataset reuse conditions remain unresolved.
- Dependencies and next check: Representation process, calendar endpoints, and customer selection need documentation. Recheck publisher download, guide, and applicable terms before listing. Do not substitute a Kaggle mirror or silently relabel represented data as observed transactions.

## Exclusions and existing sources

The following remain outside this batch; none replaces a deferred candidate:

- [Synthetic employee salaries](https://www.kaggle.com/datasets/gmudit/employer-data): simulated records cannot support empirical wage claims.
- [BLS CPI mirror](https://www.kaggle.com/datasets/bls/consumer-price-index) and [FRED-derived wages/profits](https://www.kaggle.com/datasets/dennisbucklin/wages-vs-profits-cleaned): distribution and transformation are not independent observations; prefer original definitions and current publishers.
- [Estimated grocery histories](https://www.kaggle.com/datasets/waddahali/global-grocery-inflation-20252026): mixtures of forecasts and estimates are not an observed national price panel.
- [LinkedIn job postings](https://www.kaggle.com/datasets/arshkon/linkedin-job-postings/data): upstream redistribution rights remain unverified, and 2023-2024 offers lack a 2020 baseline.
- [FINRA TRACE data](https://www.finra.org/filing-reporting/trace/data): subscription-based feeds are outside this open-access batch; public information pages do not make the underlying feed free.

Existing README entries retain their canonical URLs, identities, sections, and descriptions. ADP provides another payroll perspective alongside Indeed offers, Gusto small firms, and Square service workers; it should not be counted as identical coverage. Zillow and Apartment List measure rental markets rather than each incumbent tenant's bill. FDIC institution financials complement SEC accounts and household credit outcomes, but bank location is not borrower location. Treasury yields describe a different maturity/risk context from overnight funding benchmarks. The existing EIA API is an access route related to the annual electricity publication, not another independent observation system.

## Proposed analysis and acquisition sequence

1. Qualify a small export from each selected downloadable source: record publisher, URL, retrieval time, release date, observation range, file hash, units, schema, terms evidence, and revisions. Keep observation origin, calibration, deflator, and distribution host separate. Report-only resources stay outside promises of reusable microdata.
2. Pilot hours of work needed to buy a fixed essentials basket. Match dates, geography, occupation, currency, and units; normalize package sizes. Where wage and shopping populations differ, label the result a scenario rather than a linked household finding. Do not compound annual growth observations as monthly changes.
3. Compare that scenario with SHED hardship, credit delinquency, and available utility payment events. Their different populations and time windows prevent treating agreement as a count of independent national estimates.
4. Examine stable-company profit margins alongside profit dollars, sales, and disclosed volume/mix; reconcile fiscal periods and acquisitions. Compare QFR industries and Z.1 sectors without equating public companies to all domestic corporate activity.

These are proposed analyses, not implemented results. The screenshot lacks a dated endpoint and exact definitions; this catalog expansion does not verify its percentages or infer policy intent. A current, open, nationally representative U.S. grocery transaction panel spanning 2020 onward remains an unresolved gap.

## Local acceptance and rollback

Required structural checks are the unit suite, README validator, resource-index synchronization check, and `git diff --check`. Also compare all 88 existing resource objects against main, confirm 17 added URLs have dated assessments, verify 18 Contents entries and ASCII text, and retain the shared projection date and schema. Passing these checks does not prove external availability, unrestricted reuse, historical vintages, or methodology fitness.

Validation on 2026-09-08: all 32 unit tests passed; README validation reported 105 resources and 18 Contents entries; the index synchronization and whitespace checks passed. A direct comparison against main confirmed all 88 existing resource objects unchanged, all 17 new canonical URLs present in this note, ASCII text, and unchanged projection metadata. No network tests were added.

This branch changes only the README, this review, and the generated index. It does not alter the license, source-admission status, schema, generator, or ingestion system. Work remains local; pushing, opening a pull request, and merging are separate actions. Roll back by reverting the expansion and regenerating the index.
