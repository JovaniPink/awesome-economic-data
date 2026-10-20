# Contribution Guidelines

Welcome! This is a community-maintained catalog for economic data and research, stewarded by
Jovani Pink with support from The Measured Studios. You do not need to be a programmer
or an expert to help. Useful corrections and carefully described sources matter more
than a large submission.

Please follow our [Code of Conduct](code-of-conduct.md). We welcome students, researchers,
practitioners, educators, and curious newcomers.

## Start with an issue or a pull request

- [Suggest a resource](https://github.com/JovaniPink/awesome-economic-data/issues/new?template=suggest-resource.md): include the canonical URL, what it provides, and why it helps. No coding or local setup is required.
- [Report a correction or broken link](https://github.com/JovaniPink/awesome-economic-data/issues/new?template=correction.md): explain what you observed and when. A login block or timeout may be temporary.
- Improve a description, explain a limitation, clarify documentation, or contribute a focused tooling fix.
- If you are ready to edit files, open a pull request. If validation is unfamiliar, explain that in the PR and ask for help.

Disclose if you own, work for, or are paid by a suggested resource. Affiliation does not
bar a useful submission; undisclosed promotion, referral links, paid placement, and
unsupported claims do. Maintainers make independent inclusion decisions and may edit,
defer, or decline a suggestion. Inclusion does not endorse a provider.

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

## Make a catalog pull request

1. Fork the repository and create a branch for one focused change.
2. Edit `README.md` in the most appropriate existing category. Use an original concise description and a canonical HTTPS URL; do not copy publisher marketing text.
3. For a new canonical URL, add an ISO date (`YYYY-MM-DD`) under `creationDates` in `catalog/resource-index.config.json`. Use the date you first add the entry in your contribution. Do not backdate it, alter existing dates, or advance catalog-wide review dates. A changed canonical URL is a new identity; keep the old date mapping as history.
4. Regenerate the resource index with `python3 scripts/build_resource_index.py`. Do not hand-edit generated records.
5. Commit the README, date metadata, regenerated index, and any related documentation together. Open a PR using the template.

## Validate your change

From the repository root, use Python 3.11 or newer. No third-party packages are required:

```sh
python3 scripts/build_resource_index.py
python3 -m unittest discover -s tests -v
python3 scripts/validate_readme.py README.md
python3 scripts/build_resource_index.py --check
git diff --check
```

For a tooling-only change, regeneration should leave the index unchanged. Review the diff
before committing; do not include downloaded datasets, private research, credentials,
API keys, personal records, or unrelated generated files.

These checks verify repository structure and consistency. Separately inspect the public
publisher page and provide the URLs and date supporting your description, access terms,
update claims, and limitations. Do not bypass access controls or buy access for a submission.
Disclose material AI assistance and verify every claim yourself; generated text is not evidence.

## Updating your pull request

If maintainers request changes, update the existing pull request rather than opening a replacement. If you are unsure how, see this [guide to amending a commit](https://github.com/RichardLitt/knowledge/blob/master/github/amending-a-commit-guide.md).

## Rights and credit

Content contributions use CC BY 4.0; code contributions use MIT. You retain ownership.
Submit original work or material you have permission to contribute under the applicable
terms. Identify third-party text and required attribution. Earlier contributions keep
their existing grants; see [LICENSING.md](LICENSING.md) and [NOTICE.md](NOTICE.md).

We credit contributions in commit history and PR records. If a contribution is included
through a separate integration PR, we link back to the original submission and preserve
attribution. You may suggest the public name or handle to use; avoid adding private contact
information. Clear evidence, courteous review, and small follow-up corrections are welcome.

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
