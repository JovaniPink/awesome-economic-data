# WorkinVirtual Remote Job Eligibility Index source review (2026-11-28)

Affiliation: WorkinVirtual Editorial & Research publishes the source and submits this
review. Prepared with material AI assistance and checked against the public report,
the exact aggregate download, and its registered archive metadata. The maintainer's
[November 25 receipt](https://github.com/JovaniPink/awesome-economic-data/issues/35#issuecomment-7169693095)
independently corroborates access and the file identity.

## WorkinVirtual Remote Job Eligibility Index

### Review scope and identity

| Field | Record |
| --- | --- |
| Review date and method | 2026-11-28. Publisher self-review. Retrieved the public canonical report and linked aggregate CSV without authentication. Parsed the CSV, counted data rows and columns, and hashed the bytes. Checked the DOI registry metadata separately. |
| Publisher and canonical URL | WorkinVirtual Editorial & Research. <https://workinvirtual.com/research/remote-job-eligibility-index-2026/>. |
| Existing catalog identity | Proposed new URL. The contribution first adds it on 2026-11-28, as recorded in the catalog configuration. |
| Scope and evidence | The report's August 13 snapshot and the exact linked [aggregate CSV](https://workinvirtual.com/research/remote-job-eligibility-index-2026.csv), checked 2026-11-28. Later dated directory observations are described separately on the report page and are outside this CSV. |

### Measurement contract

| Field | Record |
| --- | --- |
| Measure and evidence type | Counts and percentages of listings by advertised remote-scope labels and other recorded job fields. This review focuses on applicant geography. Advertised eligibility is a characteristic of the posting, distinct from the employer's location, a worker's actual location, and confirmed permission to work. |
| Population and selection | All 112 listings marked public on WorkinVirtual at the August 13, 2026 snapshot. The inventory spans U.S. and non-U.S. scopes. The U.S. nationwide label applies to 45 listings and the U.S. selected-states label to 24. The single-board inventory has its own coverage and curation and is unweighted. |
| Units and transformations | Each CSV row is an aggregate category count and a percentage of the 112-listing denominator, rounded to one decimal. Repeated listings across metric groups mean the 25 rows should not be summed as independent observations. No seasonal adjustment or smoothing. |
| Comparability and changes | The August classifications use the report's published fields and definitions. Later directory checks use their own population and method. They do not establish a comparable series. Individual employer policies and actual hire outcomes were not checked. |

### Timing and vintage

| Field | Record |
| --- | --- |
| Reference period | One inventory snapshot on 2026-08-13. The aggregate has no per-row date field. |
| Collection period | The publisher extracted fields for publicly listed records at the snapshot time. The snapshot does not describe how long each vacancy had been open or follow it over time. |
| Publication and vintage | The report is dated 2026-08-13. The [versioned archive](https://doi.org/10.5281/zenodo.24449475) identifies the August aggregate. The later observations appended to the report have separate dates and do not update the August CSV. |
| Retrieval date and observed coverage | Retrieved the publisher-hosted CSV on 2026-11-28. It covers the single August 13 snapshot. |
| Cadence and freshness limits | Treat this as a dated research example. The aggregate has one verified release. Check current vacancy information with the employer. |

### Access and artifact receipt

| Field | Record |
| --- | --- |
| Tested route and conditions | The canonical report and its direct CSV both returned HTTP 200 without sign-in, payment or an API key. [DataCite version metadata](https://api.datacite.org/dois/10.5281/zenodo.24449475) separately returned HTTP 200. |
| Retrieved artifact | `remote-job-eligibility-index-2026.csv`. 25 data rows and four columns: `metric_group`, `segment`, `listing_count`, and `percentage_of_snapshot`. The rows describe aggregate categories rather than individual job ads. |
| Snapshot identity | 1,359 bytes. SHA-256 `21f44edb203fc19280fd825301a60341dfbdf0c18203cba0a8e9ffb8e993e486` from the publisher's CSV, matching the maintainer's November 25 receipt. The version DOI provides the archive reference. |
| Untested access | The Zenodo record API returned HTTP 403 to this review client, so the archive bytes were not independently downloaded in this review. Listing-level data, an API history and other vintages were outside scope. |

### Terms and interpretation limits

| Field | Record |
| --- | --- |
| License and terms evidence | The versioned [DataCite record](https://api.datacite.org/dois/10.5281/zenodo.24449475) links the [WorkinVirtual Terms of Service](https://workinvirtual.com/terms-of-service/) and identifies the dataset as in copyright. Both were checked on 2026-11-28. The CSV has no separate open license evident in the checked material. |
| Reuse and attribution | WorkinVirtual offers no separate redistribution or commercial reuse permission through this proposal. For an ordinary report citation, credit WorkinVirtual Editorial & Research, the report title and August 13, 2026 snapshot date, and link the canonical report. The catalogue contribution adds original review text and a report link. The underlying dataset remains subject to the publisher's terms. |
| Interpretation limits | This is evidence about a single platform's published fields. The labels do not establish independently verified eligibility, a vacancy fill rate, labor-market coverage or the geography of remote workers. |

### Catalog decision and follow-up

| Field | Record |
| --- | --- |
| Catalog action | Propose one report-only Labor & Hiring listing. The example helps distinguish advertised applicant geography from whether a role is called remote. |
| Unresolved checks | No row-by-row eligibility audit, demonstrated recurring series, or verified redistribution license. Those would require separate evidence before expanding the entry or claiming broader reuse. |
| Recheck triggers | A changed source or DOI, new comparable releases, a file schema or hash change, or a publisher rights notice. |
