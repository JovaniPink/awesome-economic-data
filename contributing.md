# Contribution Guidelines

Please note that this project is released with a [Contributor Code of Conduct](code-of-conduct.md).
By participating, you agree to abide by its terms.

## Suggesting a resource

- Search the README first to avoid duplicates.
- Prefer official publishers, primary datasets, documented methodologies, and stable canonical URLs.
- Confirm that the source is maintained and materially useful for economic analysis, data discovery, or learning.
- Describe what the source measures, its update frequency, its access level, and a meaningful limitation in one concise sentence.
- Identify observed data, modeled estimates, market prices, forecasts, and anecdotal or company-specific proxies accurately.
- Link to the recurring dataset or methodology page, not a one-time news story or generic press hub.
- Do not submit affiliate, referral, pay-to-rank, or promotional links.
- Do not copy, translate, or republish text from a repository that lacks a compatible license or documented permission; write an original attributed summary instead.
- Add one resource per pull request when practical, and explain why it improves the catalog.

## Quality bar

A listed resource should be at least one of the following:

- An authoritative recurring economic series or release.
- A maintained data portal, research index, API, library, or composite tracker.
- A distinctive alternative indicator with a transparent methodology and clearly stated limitations.
- A substantive learning resource for economics, statistics, or economic-data interpretation.

Company results and behavioral proxies must be labeled as narrow context. They must not be described as representative measures of the broader economy without supporting evidence.

A source listed in a modeling roadmap is not automatically model-ready. Point-in-time use requires verified release dates, historical vintages or prospective capture, stable units and geography, documented terms, and leakage-resistant validation.

## Validate your change

The catalog gate requires Python 3.11 or newer and has no third-party dependencies:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/validate_readme.py README.md
```

The validator checks structure and formatting only. Before adding or materially updating a resource, open its canonical source and verify its current maintenance status, update frequency, access level, relevant license or terms, and the specific claim made by the description. Include that evidence in the pull request.

## Updating your pull request

If maintainers request changes, update the existing pull request rather than opening a replacement. If you are unsure how, see this [guide to amending a commit](https://github.com/RichardLitt/knowledge/blob/master/github/amending-a-commit-guide.md).

## Manual external-link audit

Run `python3 scripts/audit_links.py --output /tmp/catalog-link-audit.json` from the
repository root. This standard-library command reads the generated catalog, uses four
workers with 20-second socket timeouts, retries a transient failure once per resource,
and falls back from unsupported, blocked, or missing HEAD responses to GET (at most 64 KiB).
Redirects are limited to five hops and HTTPS destinations without credentials.

The version 1.0 JSON report includes the input catalog hash, timestamps, resource IDs,
HTTP statuses, redirect chains, final URLs, errors, and all request attempts. A readable
summary is also printed. `reachable` means HTTP success only: the command does not
verify page content, data accuracy, rights, freshness, or completeness. Inspect redirects,
especially changes of host, for unrelated landing pages. Authentication blocks, rate
limits, missing responses, server failures, and transport errors remain separate results.
A 403 or timeout is not evidence that a resource is dead.

Exit status 0 means a report was written, even if resources need review; status 1 means
invalid input or a failed audit/report write. Supply an existing output directory. This
command never rewrites catalog entries or review dates. It is manual and stays outside
normal CI; its controlled-response tests run offline with the regular unit suite.

See [the October 20 review receipt](docs/catalog-review-2026-10-20.md) for the bounded
content review, contributor attribution, and unresolved source access observations.
