# RMM Pricing Transparency Dataset source review

This record applies the [source-review template](source-review-template.md) to a proposed addition under Behavioral & Company Proxies. The reviewer is affiliated with Nizlo, which publishes the dataset and is one of the 14 compared products.

## RMM Pricing Transparency Dataset

### Review scope and identity

| Field | Record |
| --- | --- |
| Review date and method | 2026-11-05; direct retrieval of the public landing page, CSV, JSON-LD and Data Package, programmatic CSV parsing and SHA-256 verification, with material AI assistance. Every claim below was checked against those retrieved artifacts; the 14 underlying vendor pages were not independently rechecked in this catalog review. |
| Publisher and canonical URL | Nizlo; [RMM Pricing Transparency Dataset](https://izikipizi.github.io/nizlo-msp-operations-resources/public-rmm-pricing-dataset.html). Nizlo's relationship to the dataset and its inclusion as one compared product are disclosed on the landing page. |
| Existing catalog identity | Proposed new URL requiring creation date `2026-11-05` on admission. |
| Scope and evidence | The inspected release covers 14 remote monitoring and management products and four normalized one-technician scenarios at 10, 50, 100 and 500 endpoints. Evidence inspected on 2026-11-05: the [landing page and method notes](https://izikipizi.github.io/nizlo-msp-operations-resources/public-rmm-pricing-dataset.html), [CSV](https://izikipizi.github.io/nizlo-msp-operations-resources/data/public-rmm-pricing-comparison-2026-11-02.csv), [JSON-LD/DCAT metadata](https://izikipizi.github.io/nizlo-msp-operations-resources/data/public-rmm-pricing-comparison-2026-11-02.jsonld) and [Data Package](https://izikipizi.github.io/nizlo-msp-operations-resources/datapackage.json). |

### Measurement contract

| Field | Record |
| --- | --- |
| Measure and evidence type | A manually normalized cross-section of vendors' public pricing and price-visibility disclosures. Numeric scenario cells are derived subscription-price arithmetic only where the linked vendor page supported exact calculation; blank cells mean no exact public rate was recorded. These are advertised subscription terms, not transactions, invoices, realized spending, product-quality scores or feature-equivalent offers. |
| Population and selection | Fourteen named RMM products selected by the publisher; the inspected artifacts do not document a sampling frame or claim exhaustive market coverage. The scenario is one technician in the United States, excluding tax and optional add-ons. Nizlo selected the comparison set, maintains the data and is one row. |
| Units and transformations | U.S. dollars per month at 10, 50, 100 and 500 endpoints. When annual and month-to-month public rates both exist, the scenario fields use the annual-billing monthly equivalent and retain a separate month-to-month field. A zero for source-available software denotes base-license cost only, not hosting, support, code-signing, operations or security-management cost. |
| Comparability and changes | Per-device, per-technician, flat, free-tier, source-available and package-based products can differ materially in included capabilities. Only the source-dated 2026-10-30 through 2026-11-02 cross-section was checked. No historical series, constant product specification or adjustment for taxes, discounts, add-ons or changing plan scope was established. |

### Timing and vintage

| Field | Record |
| --- | --- |
| Reference period | Each row's `fact_checked` date records when the linked public disclosure was checked, from 2026-10-30 through 2026-11-02. The monthly scenario columns describe terms visible on those dates rather than completed purchases during a measurement interval. |
| Collection period | Manual source checks recorded from 2026-10-30 through 2026-11-02. The current review did not independently reproduce all 14 source checks. |
| Publication and vintage | CSV filename and metadata version `2026-11-02`; landing page and provenance metadata updated 2026-11-05. The publisher states no fixed release cadence or formal revision policy. Git history provides version receipts, but the canonical landing page and default-branch downloads are mutable. |
| Retrieval date and observed coverage | Retrieved 2026-11-05. The CSV returned 14 data rows and 12 columns. Fact-check coverage ran from 2026-10-30 through 2026-11-02; visibility classes were six `numeric_public`, four `quote_only`, two `free_tier_only`, one `range_and_quote` and one `source_available`. |
| Cadence and freshness limits | No fixed refresh schedule was observed. Prices and public terms can change after the row-level fact-check date, so later analysis must recheck the vendor source URLs and preserve the version used. |

### Access and artifact receipt

| Field | Record |
| --- | --- |
| Tested route and conditions | The landing page linked directly to the CSV, JSON-LD and Data Package over HTTPS. Each retrieved without authentication, registration or payment on 2026-11-05. |
| Retrieved artifact | `public-rmm-pricing-comparison-2026-11-02.csv`; UTF-8 CSV, 14 data rows, 12 columns: product, pricing model, estimate billing term, visibility class, four endpoint-scenario prices, month-to-month alternative, source URL, fact-checked date and notes. Parsing succeeded and the row counts matched the landing-page summary. |
| Snapshot identity | The exact 4,273-byte CSV retrieved at commit [`73646370e0cf971b19326253064e459723972567`](https://github.com/izikipizi/nizlo-msp-operations-resources/blob/73646370e0cf971b19326253064e459723972567/docs/data/public-rmm-pricing-comparison-2026-11-02.csv) had SHA-256 `966cc69560e41681a3bf07894b5c485024d93e4793db6b112572db6608f5e06c`. The corrected JSON-LD and Data Package published the same byte count and hash. |
| Untested access | No API or microdata beyond the CSV was advertised. The current review did not independently re-request all 14 vendor URLs, test prior Git revisions as releases, or verify prices outside the four scenarios and one-technician assumption. |

### Terms and interpretation limits

| Field | Record |
| --- | --- |
| License and terms evidence | The landing page and JSON-LD identify [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) for the dataset; checked 2026-11-05. This grant applies to Nizlo's compilation, schema and verification metadata, not to third-party vendor pages or underlying trademarks. |
| Reuse and attribution | CC BY 4.0 permits sharing and adaptation, including commercial reuse, with attribution, a license link and an indication of changes. The landing page asks users to cite the fact-checked date because prices change. |
| Interpretation limits | This is a publisher-selected, company-maintained procurement snapshot, not a probability sample, transaction dataset, quality ranking, feature-equivalence study or representative software-price index. Public visibility can be absent even when a vendor offers competitive private pricing. Nizlo's commercial interest and inclusion as one product require explicit disclosure in downstream use. |

### Catalog decision and follow-up

| Field | Record |
| --- | --- |
| Catalog action | Add under Behavioral & Company Proxies as a narrow, source-dated SaaS pricing-transparency dataset with the maintainer relationship and non-representativeness stated in the catalog description. The recommendation is bounded to the inspected 2026-11-02 release. |
| Unresolved checks | The selection rule, refresh cadence and revision policy are not documented beyond the inspected artifacts, and the 14 underlying vendor claims were not independently rechecked during this review. These gaps prevent treating the file as an exhaustive market measure or current price source without row-level revalidation. |
| Recheck triggers | A new dataset version, altered product set or scenario assumptions, changed CC BY notice, changed publisher relationship, broken direct downloads, modified hash metadata, or vendor price changes should trigger re-review. |

Catalog inclusion would not endorse Nizlo or the compared products, establish the dataset as representative of the RMM market, or make the series fit for historical price-index analysis.
