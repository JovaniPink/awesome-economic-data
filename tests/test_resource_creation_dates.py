from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


class ResourceCreationDateTests(unittest.TestCase):
    def build(self, entries, dates):
        spec = importlib.util.spec_from_file_location("resource_dates", ROOT / "scripts/build_resource_index.py")
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            readme = root / "README.md"
            config = root / "config.json"
            readme.write_text("## Data\n" + "\n".join(entries) + "\n")
            config.write_text(json.dumps({"projectId": "fixture", "domains": ["data"],
                                         "projectionDate": "2026-08-30", "creationDates": dates}))
            with patch.multiple(module, README_PATH=readme, CONFIG_PATH=config):
                return module.build_projection()

    def test_newly_admitted_identity_dates(self):
        config = json.loads((ROOT / "catalog/resource-index.config.json").read_text())
        for url in ['https://reboot-hub.com/pages/reboot-hub-data', 'https://thepergolakit.com/pergola-price-index/']:
            self.assertEqual(config["creationDates"][url], "2026-10-01")

    def test_missing_creation_date_is_not_backdated(self):
        with self.assertRaisesRegex(ValueError, "Missing explicit catalog creation date"):
            self.build(["- [New](https://example.com/new) - Synthetic source."], {})

    def test_identity_dates_survive_reordering_and_removal(self):
        first = "- [First](https://example.com/first) - Synthetic source."
        second = "- [Second](https://example.com/second) - Synthetic source."
        dates = {"https://example.com/first": "2026-08-30", "https://example.com/second": "2026-10-01"}
        original = self.build([first, second], dates)
        reversed_records = self.build([second, first], dates)
        values = lambda result: {row["id"]: row["dates"]["createdAt"] for row in result["resources"]}
        self.assertEqual(values(original), values(reversed_records))
        remaining = self.build([second], dates)
        self.assertEqual(remaining["resources"][0]["dates"]["createdAt"], "2026-10-01")
        self.assertEqual(remaining["projectionDate"], "2026-08-30")

    def test_invalid_calendar_date_is_rejected(self):
        with self.assertRaises(ValueError):
            self.build(["- [New](https://example.com/new) - Synthetic source."],
                       {"https://example.com/new": "2026-02-30"})


if __name__ == "__main__":
    unittest.main()
