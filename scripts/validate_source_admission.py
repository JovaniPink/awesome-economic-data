"""Validate the bounded regional source-admission contract and QCEW evidence bundle.

The validator checks repository-local structure and deliberately does not fetch,
authenticate, hash, or otherwise validate a publisher's external artifacts.
"""

from __future__ import annotations

from typing import Any


BUNDLE_PATH = "catalog/evidence/qcew-2019-2024-release-timing.v1.json"
QCEW_CATALOG_ID = "awesome-economic-data:source:r-9c05fea3c3e0cde9"

BASELINE_URLS = {
    "qcew": "https://www.bls.gov/cew/downloadable-data-files.htm",
    "qcew-industry": "https://www.bls.gov/cew/downloadable-data-files.htm",
    "bea-regional": "https://www.bea.gov/data/economic-accounts/regional",
    "fhfa-hpi": "https://www.fhfa.gov/house-price-index?tab=HPI+Datasets",
    "census-bfs": "https://www.census.gov/econ/bfs/data.html",
    "census-building-permits": "https://www.census.gov/construction/bps/statemonthly.html",
    "treasury-yield-curve": "https://home.treasury.gov/policy-issues/financing-the-government/interest-rate-statistics",
}

ADMISSION_PRIORITIES = {
    "qcew": "core",
    "qcew-industry": "pilot",
    "bea-regional": "core",
    "fhfa-hpi": "core",
    "census-bfs": "pilot",
    "census-building-permits": "pilot",
    "treasury-yield-curve": "gate_context",
}

PENDING_FEASIBILITY = {
    "qcew-industry": "requires-archive-proof",
    "bea-regional": "designed",
    "fhfa-hpi": "designed",
    "census-bfs": "requires-archive-proof",
    "census-building-permits": "requires-archive-proof",
    "treasury-yield-curve": "designed",
}

STATE_AREA_FIPS = (
    "01000", "02000", "04000", "05000", "06000", "08000", "09000",
    "10000", "11000", "12000", "13000", "15000", "16000", "17000",
    "18000", "19000", "20000", "21000", "22000", "23000", "24000",
    "25000", "26000", "27000", "28000", "29000", "30000", "31000",
    "32000", "33000", "34000", "35000", "36000", "37000", "38000",
    "39000", "40000", "41000", "42000", "44000", "45000", "46000",
    "47000", "48000", "49000", "50000", "51000", "53000", "54000",
    "55000", "56000",
)

FULL_DATA_DATES = {
    2019: ("2019-09-04", "2019-12-04", "2020-03-04", "2020-06-03"),
    2020: ("2020-09-02", "2020-12-02", "2021-03-09", "2021-06-02"),
    2021: ("2021-09-01", "2021-12-01", "2022-03-09", "2022-06-08"),
    2022: ("2022-09-07", "2022-12-06", "2023-03-08", "2023-06-07"),
    2023: ("2023-09-06", "2023-12-07", "2024-03-06", "2024-06-05"),
    2024: ("2024-09-04", "2024-12-05", "2025-03-05", "2025-06-04"),
}

FINAL_OUTCOME_DATES = {
    2019: "2020-09-02",
    2020: "2021-09-01",
    2021: "2022-09-07",
    2022: "2023-09-06",
    2023: "2024-09-04",
    2024: "2025-09-09",
}

PENDING_EVIDENCE_FIELDS = {
    "release": {
        "releaseId",
        "publicationDate",
        "publicationDateEvidence",
        "referencePeriod",
        "publicationDelay",
    },
    "vintage": {
        "vintageId",
        "archiveUrl",
        "retrievedAt",
        "sha256",
        "exactValueBinding",
        "revisionPolicy",
        "firstUsablePeriod",
        "releaseCutoffAudit",
    },
    "measures": {"variableIds", "units", "seasonalAdjustment", "measurementType"},
    "geography": {"geographyCodes", "coverageAudit", "classificationBasis"},
    "access": {"format", "credentials", "retrievalProcedure"},
    "terms": {
        "termsUrl",
        "reviewedAt",
        "modelingPermission",
        "redistributionPermission",
        "attributionRequirements",
    },
}

PENDING_SOURCE_FIELDS = {
    "qcew-industry": {
        "recordSelection",
        "classificationBreaks",
        "historicalReleaseByteBinding",
        "disclosureAudit",
        "coverageAudit",
    },
    "bea-regional": {
        "tableAndLineCodes",
        "unitMultipliersAndPriceBasis",
        "archivedTableBinding",
    },
    "fhfa-hpi": {
        "purchaseOnlyVariant",
        "indexBase",
        "archivedReportBinding",
        "pdfPageAndLayoutEvidence",
        "manualExtractionReview",
    },
    "census-bfs": {
        "seriesCodes",
        "frequencyTransition",
        "seasonalAdjustmentPolicy",
        "projectedFormationExclusion",
    },
    "census-building-permits": {
        "measureColumns",
        "methodologyBreak",
        "monthlyRevisionPolicy",
        "workbookLayoutEvidence",
    },
    "treasury-yield-curve": {
        "maturities",
        "methodologyBreak",
        "tradingDayPolicy",
        "archiveBinding",
    },
}


def _is_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _expect_fields(value: Any, expected: set[str], label: str, errors: list[str]) -> bool:
    if not isinstance(value, dict):
        errors.append(f"{label} must be an object.")
        return False
    if set(value) != expected:
        errors.append(f"{label} fields are missing or unknown.")
        return False
    return True


def _validate_pending_group(
    value: Any,
    fields: set[str],
    label: str,
    errors: list[str],
) -> None:
    if not _expect_fields(value, fields | {"status", "requirement"}, label, errors):
        return
    if value["status"] != "pending" or any(value[field] is not None for field in fields):
        errors.append(f"{label} must remain explicitly pending with null values.")
    if not _is_text(value["requirement"]):
        errors.append(f"{label} must explain the required evidence.")


def validate_bundle(bundle: Any) -> list[str]:
    """Return structural errors for the checked-in QCEW timing evidence bundle."""
    errors: list[str] = []
    expected_top = {
        "schemaVersion",
        "bundleId",
        "catalogId",
        "canonicalUrl",
        "publisher",
        "retrievedAt",
        "purpose",
        "claimBoundary",
        "sources",
        "dataSelection",
        "releaseYears",
        "unresolved",
    }
    if not _expect_fields(bundle, expected_top, "QCEW evidence bundle", errors):
        return errors
    if bundle["schemaVersion"] != "1.0":
        errors.append("QCEW evidence bundle has an unsupported schemaVersion.")
    if bundle["bundleId"] != "qcew-final-outcome-timing-2019-2024":
        errors.append("QCEW evidence bundle has an unexpected bundleId.")
    if bundle["catalogId"] != QCEW_CATALOG_ID:
        errors.append("QCEW evidence bundle must use the stable QCEW catalogId.")
    if bundle["canonicalUrl"] != BASELINE_URLS["qcew"]:
        errors.append("QCEW evidence bundle must use the QCEW catalog URL.")
    if bundle["publisher"] != "U.S. Bureau of Labor Statistics":
        errors.append("QCEW evidence bundle must identify BLS as publisher.")
    if bundle["retrievedAt"] != "2026-09-05":
        errors.append("QCEW evidence bundle must retain its research date.")
    if not _is_text(bundle["purpose"]):
        errors.append("QCEW evidence bundle purpose must be nonempty text.")

    claim_boundary = bundle["claimBoundary"]
    if _expect_fields(
        claim_boundary,
        {"admission", "doesNotEstablish", "cutoffPolicy"},
        "QCEW evidence bundle claimBoundary",
        errors,
    ):
        if not all(_is_text(claim_boundary[field]) for field in ("admission", "cutoffPolicy")):
            errors.append("QCEW evidence bundle claimBoundary text must be nonempty.")
        if not isinstance(claim_boundary["doesNotEstablish"], list) or len(claim_boundary["doesNotEstablish"]) < 4:
            errors.append("QCEW evidence bundle must preserve its unsupported-claim boundary.")

    sources = bundle["sources"]
    source_ids: set[str] = set()
    expected_source_ids = {
        "release-calendar",
        "technical-note",
        "revisions",
        "data-files-guide",
        "quarterly-layout",
        "aggregation-levels",
        "ownership-codes",
        "industry-codes",
        "area-codes",
        "size-codes",
        "one-data-release-notice",
    }
    if not isinstance(sources, list):
        errors.append("QCEW evidence bundle sources must be a list.")
    else:
        for source in sources:
            if not _expect_fields(source, {"id", "url", "supports", "retrievedAt"}, "QCEW source", errors):
                continue
            if not _is_text(source["id"]):
                errors.append("QCEW source id must be nonempty text.")
                continue
            source_ids.add(source["id"])
            if not isinstance(source["url"], str) or not source["url"].startswith("https://www.bls.gov/"):
                errors.append(f"{source['id']}: source URL must be an official HTTPS BLS URL.")
            if not _is_text(source["supports"]):
                errors.append(f"{source['id']}: source support description must be nonempty.")
            if source["retrievedAt"] != bundle["retrievedAt"]:
                errors.append(f"{source['id']}: source research date must match the bundle.")
    if source_ids != expected_source_ids:
        errors.append("QCEW evidence bundle must contain the fixed BLS source set exactly once.")

    selection = bundle["dataSelection"]
    expected_selection = {
        "fileFamily",
        "field",
        "fieldDefinition",
        "recordFilter",
        "transformation",
        "classificationBasis",
    }
    if _expect_fields(selection, expected_selection, "QCEW dataSelection", errors):
        if selection["fileFamily"] != "NAICS-based quarterly CSV":
            errors.append("QCEW dataSelection must use the NAICS quarterly CSV family.")
        if selection["field"] != "month3_emplvl":
            errors.append("QCEW dataSelection must select month3_emplvl.")
        if not _is_text(selection["fieldDefinition"]):
            errors.append("QCEW dataSelection must retain the BLS field definition.")
        record_filter = selection["recordFilter"]
        if _expect_fields(
            record_filter,
            {"stateAreaFips", "ownCode", "industryCode", "aggregationLevelCode", "sizeCode"},
            "QCEW dataSelection recordFilter",
            errors,
        ):
            if record_filter["stateAreaFips"] != list(STATE_AREA_FIPS):
                errors.append("QCEW dataSelection must retain exactly the 50 states and DC area codes.")
            if {
                "ownCode": record_filter["ownCode"],
                "industryCode": record_filter["industryCode"],
                "aggregationLevelCode": record_filter["aggregationLevelCode"],
                "sizeCode": record_filter["sizeCode"],
            } != {
                "ownCode": "0",
                "industryCode": "10",
                "aggregationLevelCode": "50",
                "sizeCode": "0",
            }:
                errors.append("QCEW dataSelection must retain the bounded statewide total selection.")
        transformation = selection["transformation"]
        if _expect_fields(
            transformation,
            {"name", "formula", "positiveLevelRequirement"},
            "QCEW dataSelection transformation",
            errors,
        ):
            if transformation["name"] != "year-over-year log growth":
                errors.append("QCEW dataSelection must preserve the target transformation name.")
            if transformation["formula"] != "log(month3_emplvl[t]) - log(month3_emplvl[t-4])":
                errors.append("QCEW dataSelection must preserve the target transformation formula.")
            if not _is_text(transformation["positiveLevelRequirement"]):
                errors.append("QCEW dataSelection must retain the positive-level requirement.")
        if selection["classificationBasis"] != [
            {"referenceYears": "2019-2021", "naicsVersion": "2017"},
            {"referenceYears": "2022-2024", "naicsVersion": "2022"},
        ]:
            errors.append("QCEW dataSelection must preserve the documented NAICS change.")

    release_years = bundle["releaseYears"]
    if not isinstance(release_years, list):
        errors.append("QCEW evidence bundle releaseYears must be a list.")
    else:
        seen_years: set[int] = set()
        for release_year in release_years:
            expected_release_year = {
                "referenceYear",
                "fullDataReleaseRecords",
                "finalOutcomeAvailability",
                "historicalDataArchiveUrl",
                "historicalDataSha256",
                "limitation",
            }
            if not _expect_fields(release_year, expected_release_year, "QCEW release year", errors):
                continue
            year = release_year["referenceYear"]
            if year not in FULL_DATA_DATES:
                errors.append("QCEW evidence bundle includes an unsupported reference year.")
                continue
            seen_years.add(year)
            if release_year["historicalDataArchiveUrl"] is not None or release_year["historicalDataSha256"] is not None:
                errors.append(f"{year}: release timing cannot masquerade as a retained historical byte artifact.")
            if not _is_text(release_year["limitation"]):
                errors.append(f"{year}: release timing limitation must be nonempty.")
            records = release_year["fullDataReleaseRecords"]
            if not isinstance(records, list) or len(records) != 4:
                errors.append(f"{year}: exactly four full-data release records are required.")
            else:
                expected_dates = FULL_DATA_DATES[year]
                for position, record in enumerate(records, start=1):
                    if not _expect_fields(
                        record,
                        {"referenceQuarter", "fullDataAvailableOn", "releaseTimeLocal", "timeZone", "evidenceSourceId"},
                        f"{year}: full-data release record",
                        errors,
                    ):
                        continue
                    if record["referenceQuarter"] != f"{year}-Q{position}":
                        errors.append(f"{year}: quarter identity must preserve the reference quarter.")
                    if record["fullDataAvailableOn"] != expected_dates[position - 1]:
                        errors.append(f"{year}: full-data availability date does not match the BLS release record.")
                    if record["releaseTimeLocal"] != "10:00" or record["timeZone"] != "America/New_York":
                        errors.append(f"{year}: full-data timing must retain the BLS local release time.")
                    if record["evidenceSourceId"] != "release-calendar":
                        errors.append(f"{year}: full-data release must be linked to the BLS release calendar.")
            final_availability = release_year["finalOutcomeAvailability"]
            if _expect_fields(
                final_availability,
                {"finalizationReferencePeriod", "notBeforeDate", "releaseTimeLocal", "timeZone", "evidenceSourceIds"},
                f"{year}: final outcome availability",
                errors,
            ):
                if final_availability["finalizationReferencePeriod"] != f"{year + 1}-Q1":
                    errors.append(f"{year}: finalization must remain tied to the following first-quarter release.")
                if final_availability["notBeforeDate"] != FINAL_OUTCOME_DATES[year]:
                    errors.append(f"{year}: final outcome availability date does not match the BLS release record.")
                if final_availability["releaseTimeLocal"] != "10:00" or final_availability["timeZone"] != "America/New_York":
                    errors.append(f"{year}: final outcome timing must retain the BLS local release time.")
                evidence_ids = final_availability["evidenceSourceIds"]
                if not isinstance(evidence_ids, list) or "release-calendar" not in evidence_ids:
                    errors.append(f"{year}: final outcome availability must cite the BLS release calendar.")
                if year == 2024 and (not isinstance(evidence_ids, list) or "one-data-release-notice" not in evidence_ids):
                    errors.append("2024: final outcome availability must cite the one-data-release notice.")
        if seen_years != set(FULL_DATA_DATES):
            errors.append("QCEW evidence bundle must cover each 2019-2024 reference year exactly once.")

    unresolved = bundle["unresolved"]
    if _expect_fields(
        unresolved,
        {"historicalDataBytes", "historicalPreliminaryVintages", "terms", "runReceiptRequirement"},
        "QCEW evidence bundle unresolved",
        errors,
    ):
        if unresolved["historicalDataBytes"] != "not-retained":
            errors.append("QCEW evidence bundle must not claim retained historical data bytes.")
        if unresolved["historicalPreliminaryVintages"] != "not-established":
            errors.append("QCEW evidence bundle must not claim historical preliminary vintages.")
        if unresolved["terms"] != "not-reviewed":
            errors.append("QCEW evidence bundle must leave source terms unreviewed.")
        if not _is_text(unresolved["runReceiptRequirement"]):
            errors.append("QCEW evidence bundle must retain the run-receipt requirement.")
    return errors


def _validate_qcew_evidence(evidence: Any, bundle: Any, errors: list[str]) -> None:
    groups = {"release", "vintage", "measures", "geography", "access", "terms", "sourceSpecific"}
    if not isinstance(evidence, dict) or set(evidence) != groups:
        errors.append("qcew: required evidence groups are missing or unknown.")
        return
    release = evidence["release"]
    if _expect_fields(
        release,
        {"status", "requirement", "bundlePath", "referencePeriodCoverage", "cutoffPolicy", "sourceIds"},
        "qcew.release",
        errors,
    ):
        if release["status"] != "supported":
            errors.append("qcew.release must be supported by the BLS release-timing bundle.")
        if release["bundlePath"] != BUNDLE_PATH:
            errors.append("qcew.release must link to the QCEW evidence bundle.")
        if release["referencePeriodCoverage"] != "2019-Q1 through 2024-Q4":
            errors.append("qcew.release must retain the 2019-2024 coverage boundary.")
        if not _is_text(release["requirement"]) or not _is_text(release["cutoffPolicy"]):
            errors.append("qcew.release must retain its usage boundary.")
        if not isinstance(release["sourceIds"], list) or not {"release-calendar", "technical-note", "revisions", "one-data-release-notice"}.issubset(release["sourceIds"]):
            errors.append("qcew.release must cite its required BLS sources.")
    _validate_pending_group(evidence["vintage"], PENDING_EVIDENCE_FIELDS["vintage"], "qcew.vintage", errors)
    measures = evidence["measures"]
    if _expect_fields(
        measures,
        {"status", "requirement", "bundlePath", "variableIds", "units", "seasonalAdjustment", "measurementType"},
        "qcew.measures",
        errors,
    ):
        if measures["status"] != "supported" or measures["bundlePath"] != BUNDLE_PATH:
            errors.append("qcew.measures must be supported by the QCEW evidence bundle.")
        if measures["variableIds"] != ["month3_emplvl"]:
            errors.append("qcew.measures must select only month3_emplvl.")
        if not all(_is_text(measures[field]) for field in ("requirement", "units", "seasonalAdjustment", "measurementType")):
            errors.append("qcew.measures must retain its documented measure boundary.")
    geography = evidence["geography"]
    if _expect_fields(
        geography,
        {"status", "requirement", "bundlePath", "geographyCodes", "coverageBasis", "rowLevelCoverageAudit", "classificationBasis"},
        "qcew.geography",
        errors,
    ):
        if geography["status"] != "bounded" or geography["bundlePath"] != BUNDLE_PATH:
            errors.append("qcew.geography must remain a bounded source selection.")
        if geography["geographyCodes"] != list(STATE_AREA_FIPS):
            errors.append("qcew.geography must retain exactly the 50 states and DC codes.")
        if geography["rowLevelCoverageAudit"] is not None:
            errors.append("qcew.geography must not claim a row-level coverage audit.")
        if not all(_is_text(geography[field]) for field in ("requirement", "coverageBasis", "classificationBasis")):
            errors.append("qcew.geography must retain its selection and classification boundary.")
    _validate_pending_group(evidence["access"], PENDING_EVIDENCE_FIELDS["access"], "qcew.access", errors)
    _validate_pending_group(evidence["terms"], PENDING_EVIDENCE_FIELDS["terms"], "qcew.terms", errors)
    source_specific = evidence["sourceSpecific"]
    if _expect_fields(
        source_specific,
        {"status", "requirement", "bundlePath", "recordSelection", "classificationBreaks", "disclosureHandling", "positiveLevelGrowthAudit"},
        "qcew.sourceSpecific",
        errors,
    ):
        if source_specific["status"] != "bounded" or source_specific["bundlePath"] != BUNDLE_PATH:
            errors.append("qcew.sourceSpecific must remain bounded by the QCEW evidence bundle.")
        if source_specific["recordSelection"] != {
            "ownCode": "0",
            "industryCode": "10",
            "aggregationLevelCode": "50",
            "sizeCode": "0",
        }:
            errors.append("qcew.sourceSpecific must retain the statewide total record selection.")
        if source_specific["positiveLevelGrowthAudit"] is not None:
            errors.append("qcew.sourceSpecific must not claim a completed positive-level audit.")
        if not all(_is_text(source_specific[field]) for field in ("requirement", "classificationBreaks", "disclosureHandling")):
            errors.append("qcew.sourceSpecific must retain its data-quality boundary.")
    if isinstance(bundle, dict) and bundle.get("bundleId") != "qcew-final-outcome-timing-2019-2024":
        errors.append("qcew must map to the checked QCEW evidence bundle.")


def _validate_pending_record(record: dict[str, Any], key: str, errors: list[str]) -> None:
    if (
        record.get("admissionScope") != "none"
        or record.get("admissionStatus") != "pending"
        or record.get("pointInTimeFeasibility") != PENDING_FEASIBILITY[key]
    ):
        errors.append(f"{key}: admission scope, status, and feasibility must remain pending.")
    evidence = record.get("evidence")
    groups = {**PENDING_EVIDENCE_FIELDS, "sourceSpecific": PENDING_SOURCE_FIELDS[key]}
    if not isinstance(evidence, dict) or set(evidence) != set(groups):
        errors.append(f"{key}: required evidence groups are missing or unknown.")
        return
    for group, fields in groups.items():
        _validate_pending_group(evidence[group], fields, f"{key}.{group}", errors)


def validate_manifest(manifest: Any, index: Any, bundle: Any) -> list[str]:
    """Return local-contract errors for source admission; do not validate the web."""
    errors = validate_bundle(bundle)
    expected_top = {"schemaVersion", "projectId", "baselineDocument", "admissionStatus", "target", "records"}
    if not _expect_fields(manifest, expected_top, "Manifest", errors):
        return errors
    if manifest["schemaVersion"] != "1.1":
        errors.append("Unsupported schemaVersion.")
    if not isinstance(index, dict) or manifest["projectId"] != index.get("projectId"):
        errors.append("projectId must match the catalog.")
    if manifest["baselineDocument"] != "docs/regional-economic-modeling-data.md":
        errors.append("baselineDocument must reference the regional data map.")
    if manifest["admissionStatus"] != "partial":
        errors.append("Admission status must remain partial while required sources are pending.")
    if manifest["target"] != {
        "measure": "Next-quarter final QCEW third-month employment year-over-year log growth",
        "geography": "50 states and Washington, DC",
        "frequency": "quarterly",
    }:
        errors.append("Target must preserve the regional baseline contract.")
    records = manifest["records"]
    if not isinstance(records, list):
        return errors + ["records must be a list."]
    resources = {
        resource.get("id"): resource
        for resource in index.get("resources", [])
        if isinstance(resource, dict) and isinstance(resource.get("id"), str)
    } if isinstance(index, dict) else {}
    expected_record_fields = {
        "key",
        "catalogId",
        "canonicalUrl",
        "publisher",
        "expertRole",
        "intendedUse",
        "materialLimitation",
        "admissionPriority",
        "admissionScope",
        "admissionStatus",
        "pointInTimeFeasibility",
        "evidence",
    }
    seen: list[str] = []
    for record in records:
        if not isinstance(record, dict):
            errors.append("Each record must be an object.")
            continue
        key = record.get("key")
        if key not in BASELINE_URLS:
            errors.append("Unknown baseline record key.")
            continue
        seen.append(key)
        if set(record) != expected_record_fields:
            errors.append(f"{key}: record fields are missing or unknown.")
        resource = resources.get(record.get("catalogId"))
        if not isinstance(resource, dict) or resource.get("source", {}).get("canonicalUrl") != BASELINE_URLS[key]:
            errors.append(f"{key}: catalogId must resolve to its canonical baseline source.")
        if record.get("canonicalUrl") != BASELINE_URLS[key]:
            errors.append(f"{key}: canonicalUrl must match its catalog source.")
        if record.get("admissionPriority") != ADMISSION_PRIORITIES[key]:
            errors.append(
                f"{key}: admissionPriority must remain {ADMISSION_PRIORITIES[key]}."
            )
        for field in ("publisher", "expertRole", "intendedUse", "materialLimitation"):
            if not _is_text(record.get(field)):
                errors.append(f"{key}: {field} must be nonempty text.")
        if key == "qcew":
            if record.get("admissionScope") != "final-qcew-outcome-timing":
                errors.append("qcew: admission scope must remain final-qcew-outcome-timing.")
            if record.get("admissionStatus") != "admitted":
                errors.append("qcew: admission status must remain admitted only for the bounded scope.")
            if record.get("pointInTimeFeasibility") != "final-outcome-timing-only":
                errors.append("qcew: point-in-time feasibility must remain final-outcome-timing-only.")
            _validate_qcew_evidence(record.get("evidence"), bundle, errors)
        else:
            _validate_pending_record(record, key, errors)
    if sorted(seen) != sorted(BASELINE_URLS):
        errors.append("Exactly one record for each of the seven regional v2 sources is required.")
    return errors
