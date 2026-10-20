# Browser source review — October 20, 2026

This targeted browser and publisher-documentation review follows the hardened link
audit. Automated 403 responses and transport timeouts are access observations, not
proof that a resource is dead. This review does not advance a catalog-wide human
review date or qualify any dataset for an application.

## Priority access checks

| Resource | Browser observation | Catalog action |
| --- | --- | --- |
| [USDA Market News report 3324](https://mymarketnews.ams.usda.gov/viewReport/3324) | The specialty-crop retail report page showed the October 10–16 reporting period, published October 16, 2026, with PDF, data, and previous-release navigation. | Retain the canonical URL. Earlier timeouts do not establish discontinuation. |
| [OpenTable](https://www.opentable.com/c/state-of-industry/) | The dashboard and methodology loaded. Since June 2024, the measure covers online-reservation seated diners. It compares matching weekdays/weeks, with no adjustments for holidays or other listed external factors. | Retain the URL and correct the coverage description. It is a platform-specific signal, not all restaurant activity. |
| [ISM PMI](https://www.ismworld.org/supply-management-news-and-reports/reports/ism-pmi-reports/) | Public manufacturing/services report links and September 2026 PDF links were visible without logging in. Earlier automated requests redirected to sign-in and failed. | Retain the URL. Distinguish public reports from other data access and automated-request behavior. |
| [Baltic Exchange indices](https://www.balticexchange.com/en/data-services/market-information0/indices.html) | The homepage and this specific indices page loaded real publisher content. The page explains dry-bulk, tanker, gas, and other benchmarks. Earlier HTTP 200 responses could contain a challenge page. | Replace the generic homepage with the indices page; disclose commercial data/access terms and distinguish freight assessments from volumes. |

## Other previously blocked entries

The browser displayed the expected public content at CME copper, SEC financial
statement datasets, SEC N-PORT datasets, FirstCash investor relations, EZCORP investor
relations, S&P Global PMI releases, BLS QCEW downloads, BLS State and Area Employment,
BLS LAU, BLS state JOLTS, BLS API documentation, and FEMA disaster-declaration data.
Their canonical URLs are retained. Landing-page access does not verify every
download, API request, or authenticated service.

The Economist's Big Mac interactive displayed its page but also a registration
prompt and incomplete values. The ScienceDirect lipstick paper displayed an abstract
and purchase/institutional-access options. Neither observation establishes free
access to the complete underlying material.

## Three additions and their limits

| New source | Distinct research value | Evidence and limitation |
| --- | --- | --- |
| [USDA ERS Food Price Outlook](https://www.ers.usda.gov/data-products/food-price-outlook) | Food CPI/PPI observations, monthly forecasts, CSV/XLSX history, and originally published forecast archives. | The publisher page was updated September 25, 2026. Forecast methods changed in 2023. Earlier values in the Historical Data file are reconstructions using current methods; the separate Archived Data files preserve forecasts published under the former method. Do not combine the two as one comparable series. |
| [IMF PortWatch data and methodology](https://portwatch.imf.org/pages/data-and-methodology) | Daily port/chokepoint activity, estimated shipment volumes, download links, and API access. | The JavaScript page initially rendered blank, then loaded its documentation and download/API links. Its revision log reports AIS coverage changes, backfills, and spoofing checks. AIS-derived volume estimates differ from customs statistics and freight prices. See also the [IMF methodology paper](https://www.imf.org/en/publications/wp/issues/2026/05/19/nowcasting-country-level-trade-estimates-using-imf-portwatch-576176) and publisher-linked [usage terms](https://www.imf.org/external/terms.htm). |
| [Chicago Fed NFCI / ANFCI](https://www.chicagofed.org/research/data/nfci/current-data) | Weekly financial-conditions composites with a macroeconomically adjusted alternative. | The publisher explains 105 inputs, indicator weights, and historical revisions. Text loaded, but some embedded charts remained in a configuring state during this check; no claim of successful bulk-file retrieval is made. Preserve the release vintage and consult the [methodology](https://www.chicagofed.org/research/data/nfci/about). |

These entries identify public research resources. No API authentication, full dataset
ingestion, forecasting performance assessment, or broad reuse-rights approval was
performed. Preserve publisher-specific terms, revisions, and provenance when using data.

## Publisher-hosted archives

- USDA Market News exposes previous releases on the existing report page.
- Food Price Outlook adds an official archive with explicit methodology boundaries.
- The already-listed [Big Mac data repository](https://github.com/TheEconomist/big-mac-data)
  provides CSV/Excel releases and calculation code. Its README says adjusted history
  can change when IMF GDP history changes, and links previous releases. The catalog
  description now recommends retaining the chosen release.

Prefer these publisher-controlled references over an unidentified mirror. An archive
is historical evidence, not proof of current availability, unchanged definitions, or
unrestricted rights. No downloaded dataset or private research record is committed.

## Validation and metadata

The catalog increases from 122 to 125 resources. Baltic's replacement URL and the
three additions have explicit 2026-10-20 creation dates and new URL-derived identities.
Existing creation dates, old URL date mappings, and the projection date are retained.
The generated index was rebuilt; the 74-test suite, README validation, index check,
and whitespace check passed. The link checker and its security policy are unchanged.

A targeted hardened-checker rerun reached the four new canonical URLs without
redirects. OpenTable and ISM still returned transport errors, with ISM redirecting
to its sign-in host. Their successful browser observations are separate evidence;
the automated failures have not been relabeled as successes.
