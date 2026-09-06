from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from scripts.validate_source_admission import validate_bundle, validate_manifest


ROOT = Path(__file__).resolve().parents[1]
BUNDLE_PATH = ROOT / "catalog/evidence/qcew-2019-2024-release-timing.v1.json"
MANIFEST_PATH = ROOT / "catalog/source-admission.v1.json"
INDEX_PATH = ROOT / "catalog/resources.v1.json"


class SourceAdmissionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.bundle = json.loads(BUNDLE_PATH.read_text(encoding="utf-8"))
        self.manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        self.index = json.loads(INDEX_PATH.read_text(encoding="utf-8"))

    def assert_manifest_invalid(self, manifest: object, message: str) -> None:
        errors = validate_manifest(manifest, self.index, self.bundle)
        self.assertTrue(any(message in error for error in errors), errors)

    def assert_bundle_invalid(self, bundle: object, message: str) -> None:
        errors = validate_bundle(bundle)
        self.assertTrue(any(message in error for error in errors), errors)

    def test_committed_bundle_and_manifest_are_valid(self) -> None:
        self.assertEqual(validate_bundle(self.bundle), [])
        self.assertEqual(validate_manifest(self.manifest, self.index, self.bundle), [])

    def test_bundle_covers_each_2019_to_2024_reference_year(self) -> None:
        years = self.bundle["releaseYears"]
        self.assertEqual([year["referenceYear"] for year in years], list(range(2019, 2025)))
        self.assertTrue(all(len(year["fullDataReleaseRecords"]) == 4 for year in years))
        self.assertEqual(
            [year["finalOutcomeAvailability"]["notBeforeDate"] for year in years],
            ["2020-09-02", "2021-09-01", "2022-09-07", "2023-09-06", "2024-09-04", "2025-09-09"],
        )

    def test_qcew_admission_cannot_broaden_beyond_final_outcome_timing(self) -> None:
        candidate = copy.deepcopy(self.manifest)
        candidate["records"][0]["admissionScope"] = "all-qcew-data"
        self.assert_manifest_invalid(candidate, "admission scope")
        candidate = copy.deepcopy(self.manifest)
        candidate["records"][0]["pointInTimeFeasibility"] = "historical-vintages"
        self.assert_manifest_invalid(candidate, "point-in-time feasibility")

    def test_qcew_terms_and_historical_byte_evidence_remain_unclaimed(self) -> None:
        candidate = copy.deepcopy(self.manifest)
        candidate["records"][0]["evidence"]["terms"]["modelingPermission"] = "allowed"
        self.assert_manifest_invalid(candidate, "qcew.terms")
        candidate_bundle = copy.deepcopy(self.bundle)
        candidate_bundle["releaseYears"][0]["historicalDataSha256"] = "a" * 64
        self.assert_bundle_invalid(candidate_bundle, "historical byte artifact")

    def test_qcew_release_calendar_values_are_not_mutable(self) -> None:
        candidate = copy.deepcopy(self.bundle)
        candidate["releaseYears"][3]["fullDataReleaseRecords"][2]["fullDataAvailableOn"] = "2023-03-09"
        self.assert_bundle_invalid(candidate, "full-data availability date")
        candidate = copy.deepcopy(self.bundle)
        candidate["releaseYears"][5]["finalOutcomeAvailability"]["notBeforeDate"] = "2025-09-08"
        self.assert_bundle_invalid(candidate, "final outcome availability date")

    def test_qcew_geography_and_selection_cannot_drift(self) -> None:
        candidate = copy.deepcopy(self.bundle)
        candidate["dataSelection"]["recordFilter"]["stateAreaFips"] = candidate["dataSelection"]["recordFilter"]["stateAreaFips"][:-1]
        self.assert_bundle_invalid(candidate, "50 states and DC")
        candidate = copy.deepcopy(self.manifest)
        candidate["records"][0]["evidence"]["sourceSpecific"]["recordSelection"]["industryCode"] = "31_33"
        self.assert_manifest_invalid(candidate, "statewide total record selection")

    def test_bundle_requires_official_bls_sources(self) -> None:
        candidate = copy.deepcopy(self.bundle)
        candidate["sources"][0]["url"] = "https://example.com/qcew"
        self.assert_bundle_invalid(candidate, "official HTTPS BLS URL")

    def test_all_unadmitted_sources_remain_pending(self) -> None:
        positions = {
            record["key"]: position
            for position, record in enumerate(self.manifest["records"])
        }
        for source in (
            "qcew-industry",
            "bea-regional",
            "fhfa-hpi",
            "census-bfs",
            "census-building-permits",
            "treasury-yield-curve",
        ):
            with self.subTest(source=source):
                candidate = copy.deepcopy(self.manifest)
                candidate["records"][positions[source]]["admissionStatus"] = "admitted"
                self.assert_manifest_invalid(candidate, f"{source}: admission scope")

    def test_manifest_identity_and_seven_source_contract_are_preserved(self) -> None:
        candidate = copy.deepcopy(self.manifest)
        candidate["records"][0]["catalogId"] = candidate["records"][1]["catalogId"]
        self.assert_manifest_invalid(candidate, "catalogId must resolve")
        candidate = copy.deepcopy(self.manifest)
        candidate["records"] = candidate["records"][:-1]
        self.assert_manifest_invalid(candidate, "Exactly one record")

    def test_qcew_industry_remains_blocked_on_original_release_bytes(self) -> None:
        record = next(
            record for record in self.manifest["records"] if record["key"] == "qcew-industry"
        )
        self.assertEqual(record["pointInTimeFeasibility"], "requires-archive-proof")
        self.assertEqual(record["evidence"]["vintage"]["status"], "pending")
        self.assertIsNone(record["evidence"]["vintage"]["archiveUrl"])
        self.assertIn("original", record["evidence"]["vintage"]["requirement"].lower())

    def test_release_evidence_must_reference_the_checked_bundle(self) -> None:
        candidate = copy.deepcopy(self.manifest)
        candidate["records"][0]["evidence"]["release"]["bundlePath"] = "catalog/evidence/other.json"
        self.assert_manifest_invalid(candidate, "qcew.release must link")


if __name__ == "__main__":
    unittest.main()
