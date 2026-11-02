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
- Use the [source-review template](docs/source-review-template.md) to organize the evidence for a new source or a material change. Initial suggestions can provide what is known and ask for help with unresolved fields.
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

## Record a source review

For a catalog addition or a material change to a source's description, methodology,
access, or terms, copy the [source-review template](docs/source-review-template.md)
into a dated Markdown review under `docs/` and link the completed record in your PR.
Use one record per canonical URL; related sources may share a file. The
[Indeed, Gusto, and Square reviews](docs/alternative-labor-review-2026-11-02.md)
show how to document tested exports alongside unresolved checks. Pure formatting,
tooling, and unrelated documentation changes do not require a new source review.

Identify the exact population, series, units, adjustment, and smoothing. Separate
reference, collection, publication, and retrieval dates, and record definition breaks
and revision behavior. Link the publisher evidence with its check date. Distinguish
observed results, publisher-documented behavior, and unverified claims. When reusing
earlier evidence, retain its dates and say that access was not retested.

Record the download route, selected variant, returned coverage and columns, and any
snapshot identifier or file hash captured. A visible download link is not a tested
export; one successful export does not verify every series or API. Write `Unknown`
or `Not tested` with the consequence and next check, rather than inventing evidence.
Use `Not applicable` with a reason when a field does not fit the resource.

Public access does not imply unrestricted reuse. Record explicit license grants,
attribution requirements, general terms, and unresolved rights separately. Review
records do not change the catalog schema, stable IDs, recorded creation dates, or
the generated index's conservative evidence/access fields. An unresolved field may
require a narrower description or deferral; completing the form is not approval,
source admission to a model, or proof of catalog-wide freshness.

## Make a catalog pull request

1. Fork the repository and create a branch for one focused change.
2. Edit `README.md` in the most appropriate existing category. Use an original concise description and a canonical HTTPS URL; do not copy publisher marketing text.
3. For a new canonical URL, add an ISO date (`YYYY-MM-DD`) under `creationDates` in `catalog/resource-index.config.json`. Use the date you first add the entry in your contribution. Do not backdate it, alter existing dates, or advance catalog-wide review dates. A changed canonical URL is a new identity; keep the old date mapping as history.
4. Regenerate the resource index with `python3 scripts/build_resource_index.py`. Do not hand-edit generated records.
5. Include a completed source review for additions or material source changes, following the instructions above. Commit the README, applicable date metadata, regenerated index, and related documentation together. Open a PR using the template.

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
workers. Each resource gets one 20-second overall budget, including interpreter startup,
DNS, connect, TLS, redirects, headers/body reads, retry backoff, and HEAD-to-GET
fallback. Socket timeouts also remain 20 seconds. The checker retries a transient
failure once per resource,
and falls back from unsupported, blocked, or missing HEAD responses, HEAD timeouts,
and any HEAD 5xx server response to GET (at most 64 KiB). Transient HEAD failures use
at most one retry before fallback; the retry budget is shared with GET and never resets
when changing methods. This permits at most three attempts per resource, excluding
redirect hops. A recovered HEAD does not trigger GET. Other transport failures (such
as DNS or certificate errors), rate limits, and security-policy refusals do not trigger
GET fallback. Timeout attempts carry `timedOut: true`, and all failed HEAD attempts
remain in the report even when GET succeeds.
Redirects are limited to five hops. Initial requests, redirects, retries, and GET
fallbacks allow only credential-free HTTPS on port 443 and public IP destinations.

The version 1.2 JSON report includes the input catalog hash, timestamps, resource IDs,
HTTP statuses, redirect chains, final URLs, errors, and all request attempts. A readable
summary is also printed. `reachable` means HTTP success only: the command does not
verify page content, data accuracy, rights, freshness, or completeness. Inspect redirects,
especially changes of host, for unrelated landing pages. Authentication blocks, rate
limits, missing responses, server failures, and transport errors remain separate results.
A 403 or timeout is not evidence that a resource is dead. `security-blocked` means
local policy refused the destination before sending HTTP to it; it is not a publisher
HTTP response. Version 1.1 adds this classification and the destination policy setting;
historical version 1.0 and 1.1 reports remain unchanged. Version 1.2 adds the
`resourceDeadlineSeconds` and `deadlineScope` settings, `deadline-exceeded` and
`worker-error` classifications, and an incomplete terminal attempt when work is stopped.
Completed attempt evidence is retained, including earlier redirects and failures. An
interrupted request has no invented HTTP status or final redirect target; its terminal
record uses the canonical URL and marks its phase and `incomplete: true`. A deadline
result ends processing for that resource: it never resets the budget, retries or falls
back to GET. Neither new classification means the source is dead.

The connector checks every resolved IPv4/IPv6 address and rejects the entire DNS answer
if any address is non-public. It connects directly to a validated numeric address to
avoid a second DNS lookup, retaining the original hostname for Host, TLS SNI, and
certificate verification. Private, loopback, link-local/metadata, shared, multicast,
reserved, and IPv6 transition/translation destinations are refused. Environment and
system proxies are disabled; there is no insecure bypass option.

The parent runs each resource in a separate isolated Python process with a fixed
command and JSON input, and kills and reaps it when its monotonic budget expires.
This stops blocked DNS and slow-drip reads without leaving background work behind;
returning from a timed-out thread alone would not do that. Four supervisors limit
concurrent resource processes to four. The deadline is counted before process launch,
but operating-system process creation and termination/scheduling overhead may add
time beyond the budget; this is not a hard real-time guarantee. No signal alarm or
fork from the thread pool is used. Process failure is reported, never retried through
an unprotected in-process path. The internal worker mode and HTTP engine are private
implementation/test seams, not standalone audit entry points.

This policy intentionally refuses nonstandard ports and some special-purpose ranges.
It is an application-level restriction, not network isolation: DNS still uses the system
resolver, and local routing/firewalls remain outside the tool's control. Run audits in
a restricted environment when processing untrusted catalogs. The tool does not execute
page content or qualify the security of third-party services.

Exit status 0 means a report was written, even if resources need review; status 1 means
invalid input or a failed audit/report write. Supply an existing output directory. This
command never rewrites catalog entries or review dates. It is manual and stays outside
normal CI; its controlled-response tests run offline with the regular unit suite.

See [the October 20 review receipt](docs/catalog-review-2026-10-20.md) for the bounded
content review, contributor attribution, and unresolved source access observations.
