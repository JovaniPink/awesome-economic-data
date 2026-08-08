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
- Add one resource per pull request when practical, and explain why it improves the catalog.

## Quality bar

A listed resource should be at least one of the following:

- An authoritative recurring economic series or release.
- A maintained data portal, research index, API, library, or composite tracker.
- A distinctive alternative indicator with a transparent methodology and clearly stated limitations.
- A substantive learning resource for economics, statistics, or economic-data interpretation.

Company results and behavioral proxies must be labeled as narrow context. They must not be described as representative measures of the broader economy without supporting evidence.

## Validate your change

The catalog gate requires Python 3.11 or newer and has no third-party dependencies:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/validate_readme.py README.md
```

The validator checks structure and formatting only. Before adding or materially updating a resource, open its canonical source and verify its current maintenance status, update frequency, access level, relevant license or terms, and the specific claim made by the description. Include that evidence in the pull request.

## Updating your pull request

If maintainers request changes, update the existing pull request rather than opening a replacement. If you are unsure how, see this [guide to amending a commit](https://github.com/RichardLitt/knowledge/blob/master/github/amending-a-commit-guide.md).
