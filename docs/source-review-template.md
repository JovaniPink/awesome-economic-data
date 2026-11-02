# Source-review template

Use this template for a new catalog source or a material change to a source's
description, methodology, access, or terms. Copy one record per canonical URL into
a dated review under `docs/`; related sources may share a review file. For a portal
with several series, identify exactly which series and exports were inspected.
See the [completed labor reviews](alternative-labor-review-2026-11-02.md).

Support claims with direct publisher links and a check date. Distinguish what was
observed from what the publisher documents and what remains unverified. Write
`Unknown` or `Not tested` with the consequence and next check; use `Not applicable`
with a reason for fields that do not fit the resource. Do not invent dates or file
receipts to complete the form. A review assembled from earlier evidence must retain
the original observation dates and state that access was not retested.

This is a Markdown review record, not a new catalog schema or admission manifest.
It does not change `schemaVersion`, URL-derived IDs, recorded creation dates,
`unreviewed` evidence status, or `unknown` access and authority fields in the
generated index. A review date is not a catalog creation date. Local validators do
not verify external availability, freshness, methodology, rights, or model fitness.

Copy the record below and replace every placeholder.

## Resource name

### Review scope and identity

| Field | Record |
| --- | --- |
| Review date and method | YYYY-MM-DD; reviewer or review method, including material AI assistance. |
| Publisher and canonical URL | Publisher name and canonical HTTPS link. |
| Existing catalog identity | Copy the existing ID and creation date, or state that this is a proposed new URL requiring an explicit creation date on admission. |
| Scope and evidence | Exact series, variants, geographies, and files inspected; link publisher documentation, methodology, data, and change notices with their check dates. |

### Measurement contract

| Field | Record |
| --- | --- |
| Measure and evidence type | What the series measures; identify observed records, modeled or weighted estimates, market prices, forecasts, self-reports, or anecdotal/company proxies as applicable. |
| Population and selection | Worker/business unit, geography, inclusion/exclusion rules, platform coverage, sampling, matching, and weighting dependencies. |
| Units and transformations | Currency, price basis, levels versus growth, scale, denominator, seasonal adjustment, and exact smoothing window; separate raw and transformed series. |
| Comparability and changes | Definition/question wording and method effective dates, known breaks, changing coverage, and limits on comparisons. State which history was checked. |

### Timing and vintage

| Field | Record |
| --- | --- |
| Reference period | When the measured activity occurred and what the date column means. |
| Collection period | When observations or responses were collected; distinguish this from the reference period. |
| Publication and vintage | Publisher release date, release/version ID, and revision policy; distinguish current history from originally published values. |
| Retrieval date and observed coverage | Actual retrieval/check date and the returned first/last periods for the tested subset. |
| Cadence and freshness limits | Publisher's stated schedule versus the release actually observed; discrepancies, delays, or unverified latest-release claims. |

### Access and artifact receipt

| Field | Record |
| --- | --- |
| Tested route and conditions | Landing page to file/API/control, selected filters/variant, authentication, payment, or registration requirements; record failures separately from successes. |
| Retrieved artifact | Filename or endpoint, format, schema/columns, row count, date coverage, and checks actually performed. |
| Snapshot identity | Immutable publisher revision/archive link, file byte count and SHA-256 when captured; say when only a mutable URL or decoded content was retained. |
| Untested access | Other series, variants, APIs, microdata, archives, or full-history claims not exercised. A visible button alone does not prove retrieval. |

### Terms and interpretation limits

| Field | Record |
| --- | --- |
| License and terms evidence | Direct dataset-specific license/terms links and check date; separate explicit grants from general service terms or unresolved rights. |
| Reuse and attribution | Documented conditions for analysis, redistribution, commercial use, and attribution; do not infer an open license from public downloads. |
| Interpretation limits | Selection, uncertainty, revisions, calibration dependencies, and claims the source cannot establish. |

### Catalog decision and follow-up

| Field | Record |
| --- | --- |
| Catalog action | Add, retain, clarify, defer, or remove, with the bounded reason; distinguish the recommendation from any action already taken. |
| Unresolved checks | Missing evidence, its practical consequence, and the specific next verification needed. |
| Recheck triggers | Publisher notices, new releases, changed terms/definitions, broken routes, or other events that invalidate this review. |

Keep downloaded datasets, credentials, personal records, and private research out of
the contribution. A receipt can identify inspected bytes without redistributing
them. Catalog inclusion grants no rights to underlying material and does not qualify
the source for a model or establish historical point-in-time fitness.
