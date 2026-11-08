# ClockInToday No-Interview Jobs Dataset: source review (2026-11-08)

Affiliation: submitted by the publisher. Chris Crew runs ClockInToday. Prepared with
material AI assistance (Claude), working from the publisher's own build files and
published pages.

## ClockInToday No-Interview Jobs Dataset

### Review scope and identity

| Field | Record |
| --- | --- |
| Review date and method | 2026-11-08; publisher self-review with material AI assistance. Not an independent review. |
| Publisher and canonical URL | ClockInToday, <https://clockintoday.com/report/>. |
| Existing catalog identity | Proposed new URL; creation date 2026-11-08 added in `catalog/resource-index.config.json`. |
| Scope and evidence | The single CSV linked from the report page, its methodology page <https://clockintoday.com/how-we-check/>, the Zenodo archive (concept DOI <https://doi.org/10.5281/zenodo.24058617>) and the JSON API <https://clockintoday.com/developers/>. All checked 2026-11-08. |

### Measurement contract

| Field | Record |
| --- | --- |
| Measure and evidence type | Stated entry requirements and pay terms per platform: minimum age, whether a criminal background check is run, vehicle needed, payout schedule, reported pay, pay source and worker classification. Requirements are taken from each company's own published pages. Pay is company-advertised or third-party averages (for example Gridwise), labeled per row in `pay_source`. These are company-specific statements, not observed hiring or earnings. |
| Population and selection | 112 US platforms the publisher curates as startable without a job interview: driving and delivery, shift work, tasks and labor, pets and care, online and remote, surveys and rewards, plasma and paid studies. This is not a census of gig platforms. |
| Units and transformations | `reported_pay` is text in the units the source uses (per hour, per task, per donation). Age is text because some rules vary by state or role. No seasonal adjustment or smoothing. |
| Comparability and changes | Values are overwritten at each monthly recheck. Changes are logged on <https://clockintoday.com/updates/>. Only the current state is published in the CSV; earlier states are in the Zenodo version history from 2026-11-08 on. |

### Timing and vintage

| Field | Record |
| --- | --- |
| Reference period | The requirements in force when last checked. |
| Collection period | Monthly recheck of each company's pages; the report page shows the last check (November 2026 at review). |
| Publication and vintage | The site CSV and the GitHub repository <https://github.com/crewdog77/clockintoday-data> are updated in place. Zenodo versions carry their own version DOIs under the concept DOI. |
| Retrieval date and observed coverage | 2026-11-08: 112 rows, 11 columns. |
| Cadence and freshness limits | Stated as monthly. Only one Zenodo version exists so far, so cadence is not yet demonstrated in the archive. |

### Access and artifact receipt

| Field | Record |
| --- | --- |
| Tested route and conditions | Report page, then "Download the data (CSV)". No login or payment. The JSON API needs no key. |
| Retrieved artifact | `clockintoday-no-interview-jobs-data.csv`, 112 rows. Columns: platform, category, minimum_age, background_check, vehicle, payout, reported_pay, pay_source, worker_type, details_confirmed, page. |
| Snapshot identity | 19,439 bytes; SHA-256 `9e9c06694fc0e5c467152dc6cb6b90aebc43301d5e93ea7133e10fd7d8125a10`. Identical to GitHub commit `e493ad8663169336609f0ae89cc835acf87697db`. |
| Untested access | Kaggle and Hugging Face mirrors not byte-compared in this review. |

### Terms and interpretation limits

| Field | Record |
| --- | --- |
| License and terms evidence | CC BY 4.0, stated on the report page, the API docs and the Zenodo record (checked 2026-11-08). |
| Reuse and attribution | Commercial use allowed with credit to ClockInToday (clockintoday.com). |
| Interpretation limits | Curated selection, so shares (for example "62% list no background check") describe this list, not all gig work. Advertised pay is an offer or average, not earnings received; costs such as gas are excluded. Requirements can vary by city or state beyond what one row shows. |

### Catalog decision and follow-up

| Field | Record |
| --- | --- |
| Catalog action | Proposed: add to Labor & Hiring as a company-stated entry-requirements source, labeled as a curated list. |
| Unresolved checks | Independent review of the source pages behind individual rows; whether monthly cadence holds over time. |
| Recheck triggers | A missed monthly update, a license change, or a change in the CSV columns. |
