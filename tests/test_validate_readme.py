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
    "docs/ai-assisted-economic-research-writing.md",
    "docs/regional-economic-modeling-data.md",
    "scripts/validate_readme.py",
    "tests/test_validate_readme.py",
)

REGIONAL_EXPERT_ROLES: Final[tuple[str, ...]] = (
    "Aggregate labor momentum",
    "Industry momentum",
    "Business formation",
    "Construction pipeline",
    "State growth",
    "Housing",
    "Energy",
    "Labor flows",
    "Credit",
    "National context",
)

WRITING_GUIDE_CATEGORIES: Final[tuple[str, ...]] = (
    "Chinese Draft to English Economics Prose",
    "English Economics Prose to a Chinese Reading Copy",
    "Chinese Academic Rewriting",
    "Careful Condensation",
    "Evidence-Bounded Expansion",
    "English Economics Editing",
    "Chinese Economics Editing",
    "Logic and Identification Review",
    "Removing Formulaic AI Style from LaTeX Prose",
    "Removing Formulaic AI Style from Word Prose",
    "Research-Design Figures",
    "Empirical Chart Selection",
    "Figure Titles",
    "Table Titles",
    "Empirical-Results Analysis",
    "Reviewer Simulation",
    "Model and Tool Selection",
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

REGIONAL_SOURCE_CONTRACTS: Final[tuple[ReleaseSourceContract, ...]] = (
    {
        "name": "QCEW Data Files",
        "url": "https://www.bls.gov/cew/downloadable-data-files.htm",
        "section": "Regional Economic Modeling Data",
        "required_phrases": (
            "quarterly state employment, establishment, and wage data",
            "industry detail",
            "historical forecasts require publication vintages",
        ),
        "forbidden_phrases": ("unrevised historical data",),
    },
    {
        "name": "Census Business Formation Statistics",
        "url": "https://www.census.gov/econ/bfs/data.html",
        "section": "Regional Economic Modeling Data",
        "required_phrases": (
            "monthly state business applications",
            "projected formations",
            "methodology and seasonal revisions",
        ),
        "forbidden_phrases": ("unrevised business formations",),
    },
    {
        "name": "Building Permits by State",
        "url": "https://www.census.gov/construction/bps/statemonthly.html",
        "section": "Regional Economic Modeling Data",
        "required_phrases": (
            "monthly state residential permits",
            "late reports and corrections",
        ),
        "forbidden_phrases": ("final monthly values",),
    },
    {
        "name": "BEA Regional Economic Accounts",
        "url": "https://www.bea.gov/data/economic-accounts/regional",
        "section": "Regional Economic Modeling Data",
        "required_phrases": (
            "state GDP and personal income",
            "archived releases",
        ),
        "forbidden_phrases": ("current API history is point-in-time",),
    },
    {
        "name": "FHFA House Price Index Datasets",
        "url": "https://www.fhfa.gov/house-price-index?tab=HPI+Datasets",
        "section": "Regional Economic Modeling Data",
        "required_phrases": (
            "state purchase-only house-price indexes",
            "historical values are revised",
        ),
        "forbidden_phrases": ("all index variants are interchangeable",),
    },
    {
        "name": "EIA API v2",
        "url": "https://www.eia.gov/opendata/documentation.php",
        "section": "Regional Economic Modeling Data",
        "required_phrases": (
            "state and sector electricity",
            "API key, pagination, units, and prospective vintage capture",
        ),
        "forbidden_phrases": ("no API key",),
    },
    {
        "name": "Census Quarterly Workforce Indicators",
        "url": "https://www.census.gov/data/developers/data-sets/qwi.html",
        "section": "Regional Economic Modeling Data",
        "required_phrases": (
            "quarterly hires, separations, job creation, job destruction, and wages",
            "historical publication vintages",
        ),
        "forbidden_phrases": ("verified point-in-time history",),
    },
    {
        "name": "FDIC Data Downloads",
        "url": "https://www.fdic.gov/bank-data-guide/data-downloads",
        "section": "Regional Economic Modeling Data",
        "required_phrases": (
            "quarterly institution financials back to 1992",
            "mergers and borrower geography",
        ),
        "forbidden_phrases": ("branch location identifies every borrower",),
    },
    {
        "name": "Treasury Interest Rate Statistics",
        "url": (
            "https://home.treasury.gov/policy-issues/financing-the-government/"
            "interest-rate-statistics"
        ),
        "section": "Regional Economic Modeling Data",
        "required_phrases": (
            "national gate context",
            "indicative market quotations",
            "methodology changes",
        ),
        "forbidden_phrases": ("state-specific interest rates",),
    },
)

REGIONAL_EXTENSION_CONTRACTS: Final[tuple[ReleaseSourceContract, ...]] = (
    {
        "name": "BLS State and Area Employment",
        "url": "https://www.bls.gov/sae/",
        "section": "Regional Economic Modeling Data",
        "required_phrases": ("monthly state payroll", "monthly and benchmark revisions"),
        "forbidden_phrases": ("never revised",),
    },
    {
        "name": "BLS Local Area Unemployment Statistics",
        "url": "https://www.bls.gov/lau/",
        "section": "Regional Economic Modeling Data",
        "required_phrases": ("monthly state labor-force", "model-based"),
        "forbidden_phrases": ("direct census",),
    },
    {
        "name": "BLS State JOLTS",
        "url": "https://www.bls.gov/jlt/jlt_statedata.htm",
        "section": "Regional Economic Modeling Data",
        "required_phrases": ("job openings, hires, quits, and separations", "model-assisted"),
        "forbidden_phrases": ("directly observed state JOLTS",),
    },
    {
        "name": "Census County Business Patterns",
        "url": "https://www.census.gov/programs-surveys/cbp/data/datasets.html",
        "section": "Regional Economic Modeling Data",
        "required_phrases": ("annual establishment, employment, and payroll", "suppression"),
        "forbidden_phrases": ("quarterly leading indicator",),
    },
    {
        "name": "Census Business Dynamics Statistics",
        "url": "https://www.census.gov/programs-surveys/bds/data.API.html",
        "section": "Regional Economic Modeling Data",
        "required_phrases": ("annual job creation and destruction", "API key"),
        "forbidden_phrases": ("monthly business formation",),
    },
    {
        "name": "American Community Survey API",
        "url": "https://www.census.gov/programs-surveys/acs/data/data-via-api.html",
        "section": "Regional Economic Modeling Data",
        "required_phrases": ("annual demographic, economic, and housing", "sampling uncertainty"),
        "forbidden_phrases": ("monthly population counts",),
    },
    {
        "name": "IRS Migration Data",
        "url": "https://www.irs.gov/statistics/soi-tax-stats-migration-data",
        "section": "Regional Economic Modeling Data",
        "required_phrases": ("tax-return address changes", "methodology break"),
        "forbidden_phrases": ("complete population migration",),
    },
    {
        "name": "SBA 7(a) and 504 Public Data",
        "url": "https://data.sba.gov/dataset/7a-504-foia",
        "section": "Regional Economic Modeling Data",
        "required_phrases": (
            "quarterly loan-level approvals",
            "do not represent all small-business borrowing",
        ),
        "forbidden_phrases": ("all small-business credit",),
    },
    {
        "name": "USDA NASS Quick Stats",
        "url": "https://www.nass.usda.gov/Quick_Stats/",
        "section": "Regional Economic Modeling Data",
        "required_phrases": ("state agricultural production and prices", "suppression"),
        "forbidden_phrases": ("complete real-time farm economy",),
    },
    {
        "name": "NOAA Climate Data Online API",
        "url": "https://www.ncdc.noaa.gov/cdo-web/webservices/v2",
        "section": "Regional Economic Modeling Data",
        "required_phrases": ("weather and climate observations", "station coverage"),
        "forbidden_phrases": ("economic effect of weather",),
    },
    {
        "name": "OpenFEMA Disaster Declarations",
        "url": "https://www.fema.gov/about/openfema/disaster-declarations-summaries",
        "section": "Regional Economic Modeling Data",
        "required_phrases": ("federal disaster declarations", "historical entry errors"),
        "forbidden_phrases": ("official federal financial reporting",),
    },
)

METHOD_SOURCE_CONTRACTS: Final[tuple[ReleaseSourceContract, ...]] = (
    {
        "name": "Awesome Machine Learning in Economics and Finance",
        "url": "https://github.com/cwyalpha/Awesome-Machine-Learning-in-Economics-and-Finance",
        "section": "Machine Learning and Economic Simulation",
        "required_phrases": ("mixed-language discovery list", "not a reviewed source authority"),
        "forbidden_phrases": ("authoritative bibliography",),
    },
    {
        "name": "Awesome Economic World Models",
        "url": "https://github.com/FreedomIntelligence/Awesome-Economic-World-Models",
        "section": "Machine Learning and Economic Simulation",
        "required_phrases": ("research taxonomy", "not observed economic data"),
        "forbidden_phrases": ("proves policy outcomes",),
    },
    {
        "name": "Economic World Models Systems Blueprint",
        "url": "https://arxiv.org/abs/2608.06020",
        "section": "Machine Learning and Economic Simulation",
        "required_phrases": ("systems blueprint", "not empirical validation"),
        "forbidden_phrases": ("validated economic twin",),
    },
    {
        "name": "AI Research Writing for Economics",
        "url": (
            "https://github.com/uinue2010/"
            "awesome-ai-research-writing-economics"
        ),
        "section": "Learning & Methods",
        "required_phrases": (
            "Chinese-language prompts",
            "workflow inspiration",
            "no recognized license",
        ),
        "forbidden_phrases": ("English translation",),
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


def _source_contract_errors(
    text: str, contracts: tuple[ReleaseSourceContract, ...]
) -> tuple[str, ...]:
    errors: list[str] = []
    entries = _catalog_entries_by_url(text)
    for contract in contracts:
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


def _release_source_contract_errors(text: str) -> tuple[str, ...]:
    return _source_contract_errors(text, RELEASE_SOURCE_CONTRACTS)


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


class RegionalExpansionContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.repository_root = Path(__file__).resolve().parents[1]
        self.readme = (self.repository_root / "README.md").read_text(encoding="utf-8")

    def test_regional_sources_match_reviewed_evidence(self) -> None:
        self.assertEqual(
            _source_contract_errors(self.readme, REGIONAL_SOURCE_CONTRACTS), ()
        )

    def test_extension_and_method_sources_preserve_boundaries(self) -> None:
        contracts = REGIONAL_EXTENSION_CONTRACTS + METHOD_SOURCE_CONTRACTS
        self.assertEqual(_source_contract_errors(self.readme, contracts), ())

    def test_regional_source_contract_rejects_leakage_mutation(self) -> None:
        mutation = self.readme.replace(
            "historical publication vintages must be established",
            "verified point-in-time history is available",
        )

        errors = _source_contract_errors(mutation, REGIONAL_SOURCE_CONTRACTS)

        self.assertTrue(
            any("forbidden README phrase" in error for error in errors)
        )

    def test_method_source_contract_rejects_translation_claim(self) -> None:
        mutation = self.readme.replace(
            "use it as workflow inspiration",
            "use this English translation",
        )

        errors = _source_contract_errors(mutation, METHOD_SOURCE_CONTRACTS)

        self.assertTrue(
            any("forbidden README phrase" in error for error in errors)
        )

    def test_regional_data_map_covers_requested_experts(self) -> None:
        path = self.repository_root / "docs/regional-economic-modeling-data.md"
        text = path.read_text(encoding="utf-8")

        for role in REGIONAL_EXPERT_ROLES:
            with self.subTest(role=role):
                self.assertIn(f"| {role} |", text)

        for heading in (
            "Publisher and canonical URL",
            "Measures and units",
            "Revision and vintage availability",
            "Point-in-time feasibility",
        ):
            with self.subTest(heading=heading):
                self.assertIn(heading, text)

    def test_english_writing_guide_has_attribution_and_safeguards(self) -> None:
        path = self.repository_root / "docs/ai-assisted-economic-research-writing.md"
        text = path.read_text(encoding="utf-8")

        for category in WRITING_GUIDE_CATEGORIES:
            with self.subTest(category=category):
                self.assertIn(f"## {category}", text)

        for phrase in (
            "This is an original English guide, not a translation or republication.",
            "https://github.com/uinue2010/awesome-ai-research-writing-economics",
            "https://github.com/Leey21/awesome-ai-research-writing",
            "Do not invent citations, DOI values, BibTeX, data, coefficients, or significance.",
            "AI-assisted reviewer output is diagnostic feedback, not peer review.",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)


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
