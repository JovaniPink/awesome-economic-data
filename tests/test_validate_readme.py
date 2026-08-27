from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from typing import Final, TypeAlias, TypedDict

from scripts.validate_readme import (
    RESOURCE_ENTRY_RE,
    github_anchor,
    validate_document,
)

CatalogEntry: TypeAlias = tuple[str, str, str]


class ReleaseSourceContract(TypedDict):
    name: str
    url: str
    section: str
    required_phrases: tuple[str, ...]
    forbidden_phrases: tuple[str, ...]


VALID_README = """# Awesome Test [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A focused catalog.

Catalog structure reviewed: August 2026.

## Contents

- [Observed & Modeled Data](#observed--modeled-data)

## Observed & Modeled Data

- [Example](https://example.com/) - Example primary source.

## Contributing

See the contribution guide.
"""

PUBLISHABLE_TEXT_FILES: Final[tuple[str, ...]] = (
    ".github/workflows/validate.yml",
    "AGENTS.md",
    "LICENSE",
    "README.md",
    "code-of-conduct.md",
    "contributing.md",
    "scripts/validate_readme.py",
    "tests/test_validate_readme.py",
)

RELEASE_SOURCE_CONTRACTS: Final[tuple[ReleaseSourceContract, ...]] = (
    {
        "name": "BEA Data API",
        "url": "https://apps.bea.gov/api/signup/",
        "section": "Portals",
        "required_phrases": (
            "registered, API-key access",
            "subset of published",
            "terms acceptance is required",
        ),
        "forbidden_phrases": ("all BEA statistics",),
    },
    {
        "name": "Census Economic Indicators API",
        "url": (
            "https://www.census.gov/data/developers/data-sets/"
            "economic-indicators.html"
        ),
        "section": "Portals",
        "required_phrases": (
            "every query requires an API key",
            "Census attribution",
            "originating-program attribution",
            "preservation of published precision",
        ),
        "forbidden_phrases": ("queries do not require an API key",),
    },
    {
        "name": "FRED and ALFRED API",
        "url": "https://fred.stlouisfed.org/docs/api/fred/overview.html",
        "section": "Portals",
        "required_phrases": (
            "Requires a registered API key",
            "current and vintage series",
            "aggregation layer",
            "original-source definitions, revisions, and terms remain controlling",
        ),
        "forbidden_phrases": ("FRED is the original source",),
    },
    {
        "name": "U.S. Treasury Fiscal Data",
        "url": "https://fiscaldata.treasury.gov/",
        "section": "Portals",
        "required_phrases": (
            "machine-readable debt, revenue, spending, deficit",
            "dataset-specific cadences, units, accounting definitions",
        ),
        "forbidden_phrases": ("one shared accounting definition",),
    },
    {
        "name": "DBnomics Web API",
        "url": "https://docs.db.nomics.world/web-api/",
        "section": "Portals",
        "required_phrases": (
            "many economic providers",
            "original sources remain authoritative",
            "focused queries rather than indiscriminate bulk downloads",
        ),
        "forbidden_phrases": ("DBnomics is the source authority",),
    },
    {
        "name": "Atlanta Fed GDPNow",
        "url": "https://www.atlantafed.org/research-and-data/data/gdpnow",
        "section": "Composite Trackers",
        "required_phrases": (
            "model-based running estimate",
            "not an official Atlanta Fed forecast",
            "no subjective adjustment",
            "substantial error",
        ),
        "forbidden_phrases": ("it is an official Atlanta Fed forecast",),
    },
    {
        "name": "Dallas Fed Weekly Economic Index",
        "url": "https://www.dallasfed.org/research/wei",
        "section": "Composite Trackers",
        "required_phrases": (
            "Models the common component",
            "ten daily and weekly series",
            "scales the result to four-quarter GDP growth",
            "past values may be revised",
        ),
        "forbidden_phrases": ("directly observed weekly GDP",),
    },
    {
        "name": "Philadelphia Fed ADS Index",
        "url": (
            "https://www.philadelphiafed.org/surveys-and-data/"
            "real-time-data-research/ads"
        ),
        "section": "Composite Trackers",
        "required_phrases": (
            "model-based daily business-conditions estimate",
            "real-time vintages",
            "mixed frequencies",
            "not a directly observed daily measure",
        ),
        "forbidden_phrases": ("is a directly observed daily measure",),
    },
)


def _catalog_entries_by_url(text: str) -> dict[str, CatalogEntry]:
    entries: dict[str, CatalogEntry] = {}
    section = ""
    for line in text.splitlines():
        if line.startswith("## "):
            section = line.removeprefix("## ")
            continue
        match = RESOURCE_ENTRY_RE.fullmatch(line)
        if match and match.group(3):
            entries[match.group(2)] = (match.group(1), section, match.group(3))
    return entries


def _release_source_contract_errors(text: str) -> tuple[str, ...]:
    errors: list[str] = []
    entries = _catalog_entries_by_url(text)
    for contract in RELEASE_SOURCE_CONTRACTS:
        url = contract["url"]
        entry = entries.get(url)
        if entry is None:
            errors.append(f"missing release source URL: {url}")
            continue
        name, section, description = entry
        if name != contract["name"]:
            errors.append(f"unexpected README name for {url}: {name}")
        if section != contract["section"]:
            errors.append(f"unexpected README section for {url}: {section}")
        for phrase in contract["required_phrases"]:
            if phrase not in description:
                errors.append(f"missing README phrase for {url}: {phrase}")
        for phrase in contract["forbidden_phrases"]:
            if phrase in description:
                errors.append(f"forbidden README phrase for {url}: {phrase}")
    return tuple(errors)


class GithubAnchorTests(unittest.TestCase):
    def test_matches_github_heading_style(self) -> None:
        self.assertEqual(github_anchor("Observed & Modeled Data"), "observed--modeled-data")


class DocumentValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_directory.name)
        for filename in ("LICENSE", "code-of-conduct.md", "contributing.md"):
            (self.root / filename).touch()

    def tearDown(self) -> None:
        self.temp_directory.cleanup()

    def test_accepts_the_catalog_contract(self) -> None:
        result = validate_document(VALID_README, self.root)

        self.assertEqual(result.errors, ())
        self.assertEqual(result.resource_count, 1)
        self.assertEqual(result.contents_count, 1)

    def test_reports_contents_and_resource_format_errors(self) -> None:
        invalid = VALID_README.replace(
            "- [Observed & Modeled Data](#observed--modeled-data)",
            "- [Contributing](#contributing)",
        ).replace(
            "- [Example](https://example.com/) - Example primary source.",
            "- [Example](http://example.com/) - lowercase description",
        )

        result = validate_document(invalid, self.root)

        self.assertTrue(any("Contents entries must match" in error for error in result.errors))
        self.assertTrue(any("must use HTTPS" in error for error in result.errors))
        self.assertTrue(any("start uppercase" in error for error in result.errors))
        self.assertTrue(any("end with a period" in error for error in result.errors))

    def test_reports_malformed_and_duplicate_resources(self) -> None:
        invalid = VALID_README.replace(
            "- [Example](https://example.com/) - Example primary source.",
            "- [Example](https://example.com/) - Example primary source.\n"
            "- [Malformed](https://malformed.example/) / "
            "[Second](https://second.example/) - Combined entry.\n"
            "- [Duplicate](https://example.com/) - Duplicate source.",
        )

        result = validate_document(invalid, self.root)

        self.assertTrue(any("must match" in error for error in result.errors))
        self.assertTrue(any("duplicate resource URL" in error for error in result.errors))

    def test_reports_missing_relative_links(self) -> None:
        invalid = VALID_README + "\n[Missing](docs/missing.md)\n"

        result = validate_document(invalid, self.root)

        self.assertIn(
            "relative link for 'Missing' points to missing file: docs/missing.md",
            result.errors,
        )

    def test_reports_non_ascii_characters(self) -> None:
        invalid = VALID_README.replace("focused", f"foc{chr(0x016B)}sed")

        result = validate_document(invalid, self.root)

        self.assertIn(
            "line 3: document must use ASCII characters; found U+016B",
            result.errors,
        )

    def test_empty_document_reports_errors_instead_of_crashing(self) -> None:
        result = validate_document("", self.root)

        self.assertTrue(result.errors)
        self.assertEqual(result.resource_count, 0)


class ReleaseSourceContractTests(unittest.TestCase):
    def setUp(self) -> None:
        repository_root = Path(__file__).resolve().parents[1]
        self.readme = (repository_root / "README.md").read_text(encoding="utf-8")

    def test_release_sources_match_reviewed_evidence(self) -> None:
        self.assertEqual(_release_source_contract_errors(self.readme), ())

    def test_release_source_contract_rejects_boundary_mutations(self) -> None:
        census_mutation = self.readme.replace(
            "every query requires an API key",
            "queries do not require an API key",
        )
        gdpnow_mutation = self.readme.replace(
            "not an official Atlanta Fed forecast",
            "an official Atlanta Fed forecast",
        )

        census_errors = _release_source_contract_errors(census_mutation)
        gdpnow_errors = _release_source_contract_errors(gdpnow_mutation)

        self.assertTrue(
            any("forbidden README phrase" in error for error in census_errors)
        )
        self.assertTrue(
            any("forbidden README phrase" in error for error in gdpnow_errors)
        )


class RepositoryTextContractTests(unittest.TestCase):
    def test_publishable_text_files_are_ascii(self) -> None:
        repository_root = Path(__file__).resolve().parents[1]

        for relative_path in PUBLISHABLE_TEXT_FILES:
            with self.subTest(path=relative_path):
                contents = (repository_root / relative_path).read_bytes()
                self.assertTrue(
                    contents.isascii(), f"{relative_path} must contain only ASCII"
                )


if __name__ == "__main__":
    unittest.main()
