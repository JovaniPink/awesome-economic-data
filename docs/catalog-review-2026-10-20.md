# Catalog review - October 20, 2026

This is an automated transport audit plus targeted public-source content review. It is
not a catalog-wide human review, dataset-quality qualification, or license grant. Existing
catalog-wide review dates and schema 1.1 uncertainty defaults remain unchanged.

## Review basis

- Baseline: `7593d4eea3575a369ab3de07b26653cefe93eb26`.
- Original contributor commits preserved with `git cherry-pick -x`:
  - [PR #16](https://github.com/JovaniPink/awesome-economic-data/pull/16), @estevecastells,
    `f33cf52f80240e1620c962bf8a3f9c0f2c87f656` (Invokely).
  - [PR #17](https://github.com/JovaniPink/awesome-economic-data/pull/17), @yumaheymans,
    `9ef671927f9fb5be99c68c3097c4c82d3c4846a4` (CareJobs.Now).
  - [PR #18](https://github.com/JovaniPink/awesome-economic-data/pull/18), submitted by
    @Busineessfree and authored by Fliar BI,
    `ad05b46fddb7ab67d0b386b794b5c743135b7904` (Fliar salary sample).
- PRs #17/#18 passed all three canonical checks at their original heads. PR #16 failed
  projection validation and its corresponding unit test. No hosted checks were exposed
  for these contributor PRs. Integration regenerated the index from the combined README.
- The labor-section conflict retained both new resources; generated JSON was rebuilt
  instead of combining conflict fragments.

## Contributor evidence

| Source | October 20 evidence | Treatment and limitation |
| --- | --- | --- |
| [Invokely pricing](https://invokely.ai/pricing) and [documentation](https://invokely.ai/docs) | Free MCP allowance is 500 calls/month; REST is on paid plans or credits. Current pricing does not support the PR's 60-point history limit. | Corrected the entry and projection. It is an aggregator with publisher-specific schedules and terms; authenticated behavior is unqualified. |
| [CareJobs.Now data](https://carejobs.now/data) and [pay JSON](https://carejobs.now/pay.json) | Unauthenticated JSON included an October 20 update timestamp and CC BY 4.0 metadata. Limitations include omitted salaries/non-dollar currencies and missing adjustments for location, experience, differentials, and bonuses. | Included as a narrow healthcare advertised-pay source. Employer selection and observed offers do not measure representative earnings received. |
| [Fliar dataset card](https://huggingface.co/datasets/HarshitKZ/skill-salary-percentiles-global/blob/main/README.md) | Publisher identifies a fixed 100,060-row company-selected sample from 620,752 postings, with fixed currency conversion and CC BY-NC 4.0. | Included as a one-time advertised-pay snapshot. Card assertions were reviewed; full-file row counts, accuracy, and collection rights were not independently established. |

## Public finance, procurement, and institutions

Six entries now sit together in the new section. Treasury Fiscal Data already existed
in Portals, so its existing URL, identity, creation date, and description were preserved
and moved rather than adding a duplicate API-documentation listing.

| Publisher source | Reviewed capability | Important boundary |
| --- | --- | --- |
| [Treasury Fiscal Data API documentation](https://fiscaldata.treasury.gov/api-documentation/) | Public machine-readable federal fiscal datasets, metadata, and queries. Direct retrieval succeeded even though the web-search reader returned 403. | Preserve dataset cadence, accounting basis, units, revisions, and coverage. |
| [USAspending API](https://api.usaspending.gov/) | Official federal award and account-level spending access. | Obligations, outlays, ceilings, amendments, recipient address, and place of performance are not interchangeable. |
| [FEC bulk data](https://www.fec.gov/data/browse-data/?tab=bulk-data) and [use restrictions](https://www.fec.gov/updates/use-of-contributor-information/) | Reported campaign-finance records and bulk files. | Preserve amendments and refunds. Individual-contributor use restrictions apply; public access is not unrestricted reuse permission. |
| [Congressional lobbying API](https://lda.gov/api/) | Official registration, quarterly activity, and LD-203 records; registration for an API key. The older Senate hostname redirects here. | A filing records a reported activity or relationship, not causal influence or wrongdoing. |
| [Open Contracting Data Registry](https://data.open-contracting.org/) | Bulk JSON, Excel, and CSV with publisher coverage and quality notes. | Compiled releases retain the latest field values; publisher-specific coverage and terms control. |
| [Worldwide Governance Indicators](https://www.worldbank.org/en/publication/worldwide-governance-indicators) | Annual perception-based composite estimates, survey/expert inputs, methodology, and revised historical series. | Retain release vintage and uncertainty; these are not counts of misconduct or definitive ratings. |
| [Procurement red-flags guide](https://www.open-contracting.org/resources/red-flags-in-public-procurement-a-guide-to-using-data-to-detect-and-mitigate-risks/) | Publisher methodology and formulas mapped to OCDS. | Listed in Learning & Methods. Risk flags prioritize inquiry; they do not establish a finding. |

These are public publisher descriptions written for this catalog. No private research
records, individual dossiers, case allegations, scoring rules, or restricted data were
copied into this integration. Dataset intake and application use remain separate decisions.

## Other source corrections

- Replaced the obsolete St. Louis Fed directory, which redirected to the generic bank
  homepage, with [FRASER](https://fraser.stlouisfed.org/) and a specific archive description.
- Updated [Freightos](https://www.freightos.com/enterprise/terminal/freightos-baltic-index-global-container-pricing-index/)
  to the verified destination.
- [ISM](https://www.ismworld.org/supply-management-news-and-reports/reports/ism-pmi-reports/)
  redirected an automated request to sign-in. The listing now describes access dependence.
- USDA Market News and OpenTable repeatedly timed out in the initial audit. Retain them
  as unresolved access observations; do not call them discontinued. See the final report
  for any later successful transport observations.

[License issue #1](https://github.com/JovaniPink/awesome-economic-data/issues/1) remains open.
[Renovate #15](https://github.com/JovaniPink/awesome-economic-data/pull/15) remains separate;
its existing hosted Python 3.11/3.14 checks passed at review time.

## Validation and boundaries

Run the canonical commands from the repository root:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/validate_readme.py README.md
python3 scripts/build_resource_index.py --check
python3 scripts/audit_links.py --output /tmp/catalog-link-audit.json
```

The offline suite includes controlled-response tests for redirects to unrelated HTTP 200
pages, HEAD rejection and false 404 responses, blocked requests, rate limits, missing
responses, transient errors, redirect loops, bounded GET bodies, and catalog preservation.
The live audit is deliberately outside CI. Its JSON records each request and observation;
HTTP success alone does not verify content, freshness, rights, or current data coverage.

Existing resource identifiers and creation dates were compared with the baseline. All
surviving identities retain their dates. Replacement URLs get new identities with explicit
October 20 inclusion dates; older URL dates remain in configuration as historical metadata.
Contributor-supplied identity dates remain attached to their original commits.

Original contributor PRs, Renovate onboarding, and open issues are unchanged. No merge,
contributor feedback, license change, paid API access, or dataset import is part of this
integration. Source descriptions based on public documentation do not establish
independently tested authenticated behavior. Hosted CI on these local integration commits
has not run.

## Final integration check

- Offline unit suite: 50 tests passed; README validation, generated-index check, and whitespace check passed.
- Final automated scan: 122 entries; blocked/authentication-required: 14, reachable: 92, redirected: 1, server-error: 4, transport-error: 11.
- Observation interval: `2026-10-20T19:31:14+00:00` through `2026-10-20T19:33:46+00:00`.
- [Full link-audit JSON](link-audits/2026-10-20.json) includes the matching catalog SHA-256 and per-request evidence.
- No final missing-link classifications were recorded. EIA endpoints returned server errors; several FRED/FRASER requests and the USDA/OpenTable pages timed out. These are unresolved access observations, not evidence of discontinued resources. Earlier successful publisher reads and later transport failures remain distinct observations.
