# Household wealth and community data review

Reviewed 2026-09-08 for [Awesome Economic Data](https://github.com/JovaniPink/awesome-economic-data). Six sources are listed in the [catalog](../README.md), taking the local catalog from 105 to 111 resources and from 18 to 19 Contents entries. This focused review follows the Measuring Wealth research; it does not validate the podcast's claims or admit inputs to an analytical pipeline.

Publisher pages, documentation routes, and download listings were inspected. No bulk archives were acquired, records validated, or statistical claims replicated. Public access is not unrestricted redistribution permission. The generated index retains its existing conservative assessment fields, schema, and projection-date configuration.

## Federal Reserve Survey of Consumer Finances - listed

- Publisher and canonical URL: [Federal Reserve Board SCF](https://www.federalreserve.gov/econres/scfindex.htm). Reviewed 2026-09-08.
- Coverage and method: Triennial family balance-sheet survey; the inspected page lists 2022 as its most recent survey and comparable historical tables from 1989. Measures assets, liabilities, income, and family characteristics. Repeated cross-sections are not a panel following each family's entire life.
- Access evidence: Full SAS, Stata, and ASCII ZIP listings; CSV summary extracts; codebook, variable maps, replicate weights, and standard-error instructions on the canonical page. The summary extract expresses monetary values in 2022 dollars.
- Terms evidence: Publisher explicitly offers public datasets and separately identifies confidential-data access. No blanket license for all linked content or redistribution was established in this review.
- Dependencies and uncertainty: Survey weights, disclosure protection, five imputations, and the extract's inflation adjustment matter. Treating imputed records as independent families understates uncertainty. File integrity and exact release bytes remain acquisition checks.
- Research role: Compare wealth distributions and liquid resources at similar ages, rather than comparing unadjusted generational totals.

## Census Survey of Income and Program Participation - listed

- Publisher and canonical URL: [U.S. Census Bureau SIPP datasets](https://www.census.gov/programs-surveys/sipp/data/datasets.html). Reviewed 2026-09-08.
- Coverage and method: Annual files listed for 2018-2025 and historical panels/waves for 1984-2014. Income, benefits, assets, and household changes support analysis of resources and hardship transitions.
- Access evidence: The [2025 release page](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html) lists SAS, Stata, and pipe-delimited ZIPs, dictionaries, schemas, and replicate and longitudinal weights. The intervening year landing page showed a related-content component 404, but its release link resolved. The publisher identifies 2024 as the 2025 survey's reference year.
- Terms evidence: Public-use release offered by Census; no account or payment gate was observed on the inspected pages. This is not a claim about unrestricted access to confidential linked records or all third-party content.
- Dependencies and uncertainty: Survey design, imputation, attrition, and redesigned panels complicate comparisons; the 2025 release also warns of collection costs and low unit response. Distinguish ordinary public-use files from separately labeled synthetic SIPP products. Payload retrieval and variable-level harmonization remain unperformed.
- Research role: Follow changes in household economic resources and program participation, complementing the existing SHED hardship survey.

## Census Characteristics of New Housing - listed

- Publisher and canonical URL: [Census Bureau, with HUD support](https://www.census.gov/construction/chars/index.html). Reviewed 2026-09-08.
- Coverage and method: National annual characteristics of new privately owned residential structures, with regional detail for many measures. The page identifies 2025 characteristics released July 1, 2026.
- Access evidence: [Current tables](https://www.census.gov/construction/chars/current.html), annual SOC microdata, historical tables, definitions, and change summaries are linked from the canonical page. [SOC methodology](https://www.census.gov/construction/soc/methodology.html) documents collection.
- Terms evidence: Public agency table and microdata listings; no blanket rights claim for linked third-party content. No bulk file was downloaded.
- Dependencies and uncertainty: Sample estimates, construction stage, geographic coverage, and category changes matter. New-home size is not housing-stock size, and national prices do not establish access to jobs or neighborhood services.
- Research role: Test claims about smaller-home construction. Complements existing building permits, FHFA, Zillow, and Apartment List entries without duplicating their canonical URLs.

## BEA Household Production - listed

- Publisher and canonical URL: [Bureau of Economic Analysis](https://www.bea.gov/data/special-topics/household-production). Reviewed 2026-09-08.
- Coverage and method: Periodically updated annual estimates valuing unpaid household activities. The June 2026 expanded-indicator release covers 1965-2024; earlier workbooks have different coverage.
- Access evidence: Canonical page lists XLSX workbooks, the June 2026 working paper, earlier methodological articles, and valuation FAQs.
- Terms evidence: Public agency workbooks offered without an observed account or payment gate; no generalized license inferred for externally linked publications.
- Dependencies and uncertainty: Time-use observations, including ATUS, and valuation assumptions underpin estimates. Publication by BEA does not make BLS-related inputs independent. Replacement-cost valuation is not a price for affection or a comprehensive welfare measure. Workbook contents were not independently replicated.
- Research role: Examine unpaid care and household services alongside purchased substitutes; avoid double-counting when comparing with GDP or household budgets.

## NORC General Social Survey - listed with terms qualification

- Publisher and canonical URL: [NORC GSS](https://gss.norc.org/get-the-data.html). Reviewed 2026-09-08.
- Coverage and method: Repeated U.S. surveys since 1972, generally biennial since 1994. Attitudes, trust, participation, and demographic characteristics; questions and samples vary across releases.
- Access evidence: SAS, Stata, and SPSS listings and documentation are provided. The [SPSS listing](https://gss.norc.org/get-the-data/spss.html) identifies the 1972-2024 cumulative Release 3a, July 2026, and explains revised negative missing-value codes. Sensitive geography requires a separate application.
- Terms evidence: [Publisher terms](https://gss.norc.org/terms-and-conditions.html) specify citation, responsible use, and no warranty; the same page includes a broader copyright notice. List and describe the source in original prose; do not label it unrestricted open-license data or infer permission to mirror its files.
- Dependencies and uncertainty: Mode changes, weighting, question availability, disclosure-related revisions, and format-specific releases affect trends. Distribution mirrors may lag NORC and do not add independent observations.
- Research role: Test participation and trust differences across demographic groups. Responses do not establish that a particular institution or policy caused an outcome.

## Census Volunteering and Civic Life Supplement - listed

- Publisher and canonical URL: [Census Bureau CPS supplement](https://www.census.gov/data/datasets/2023/demo/cps/cps-volunteer.html), associated with AmeriCorps civic measurement. Reviewed 2026-09-08.
- Coverage and method: September 2023 survey supplement on volunteering, informal helping, and civic life. It is a periodic supplement, not a monthly civic-activity series.
- Access evidence: Canonical page lists the supplement documentation, compressed data, CSV, SAS input statements, and separate nonresponse and self-response replicate-weight files. Large CSV listings were inspected without downloading the payloads.
- Terms evidence: Public agency microdata and documentation listings; no account or payment gate observed. Confidential CPS records are not included in this public-access claim.
- Dependencies and uncertainty: Shared CPS sampling infrastructure, self-report, weights, response selection, and questionnaire compatibility matter. Independent publication or a different topic does not create an independent sample.
- Research role: Measure reported helping and volunteering alongside GSS attitudes; neither measure captures all neighborhood trust or informal care.

## Sources remaining outside this batch

PSID remains a strong registration-and-terms candidate. IMLS public-library data deserve follow-up after the latest automated retrieval returned 403; this is an access-check limitation, not evidence that the program is private. Childcare, HMDA, education, and other community resources still require source-specific qualification. PHDCN restricted records and National Zoning Atlas reuse conditions must not be presented as unrestricted downloads. Podcast recaps, essays, and individual interpretive studies remain research context rather than new dataset entries.

Existing ACS, SHED, New York Fed, financial accounts, and housing entries retain their URLs and descriptions. No new API, schema, network tests, source-admission changes, or license changes are part of this batch.

## Validation boundary

Repository tests, README validation, index synchronization, ASCII checks, and unchanged-existing-record comparisons assess the local change. They do not establish future source availability, successful payload retrieval, unrestricted reuse, or validity of a causal interpretation. Rollback removes these six listings and this note, restores the section introductions and Contents, and regenerates the index.
