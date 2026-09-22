"""Synthetic receipt regressions. Run: python3 -B -m unittest discover -s tests -v"""

import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

TOOL = Path(__file__).resolve().parents[1] / "tools" / "receipt.py"
sys.dont_write_bytecode = True
SPEC = importlib.util.spec_from_file_location("receipt", TOOL)
receipt = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(receipt)

# Fictional unchanged control; no claims of approval or semantic adequacy.
CONTROL = {
    "schema_version": 1,
    "scope": "Review a fictional payment error message.",
    "sources": [{"id": "s1", "locator": "references/terminology.md", "revision": "uncommitted"}],
    "evidence": [{"id": "e1", "locator": "fixture:payment-error", "description": "Synthetic source says the payment failed."}],
    "claims": [{"id": "c1", "statement": "The draft preserves the stated failure.", "source_ids": ["s1"], "evidence_ids": ["e1"]}],
    "gaps": [],
    "blockers": [],
    "unresolved": [],
    "reviewer_approval": "not recorded",
    "review_required": ["Content reviewer checks evidence and wording."],
    "dimensions": {
        "guidance": {"score": 2, "reason": "The author reports consulting the applicable rule.", "evidence_ids": ["e1"]},
        "facts": {"score": 2, "reason": "The author reports preserving the fixture fact.", "evidence_ids": ["e1"]},
        "verification": {"score": 1, "reason": "Only an author self-check is reported.", "evidence_ids": []},
    },
}


class ReceiptTests(unittest.TestCase):
    def setUp(self):
        self.value = copy.deepcopy(CONTROL)

    def invalid(self):
        with self.assertRaises(receipt.ReceiptError):
            receipt.validate(self.value)

    def test_unchanged_control_and_no_mutation(self):
        before = copy.deepcopy(self.value)
        result = receipt.validate(self.value)
        self.assertEqual(result["overall"], 1)
        self.assertEqual(self.value, before)
        result.pop("overall")
        self.assertEqual(result, CONTROL)

    def test_minimum_not_average_and_blocker_override(self):
        self.value["dimensions"]["guidance"]["score"] = 3
        self.value["dimensions"]["verification"]["score"] = 2
        self.value["dimensions"]["verification"]["evidence_ids"] = ["e1"]
        self.assertEqual(receipt.validate(self.value)["overall"], 2)
        self.value["blockers"] = ["Applicable must rule is unresolved."]
        self.assertEqual(receipt.validate(self.value)["overall"], 0)

    def test_na_requires_reason_and_verification_is_applicable(self):
        self.value["dimensions"]["facts"] = {"score": None, "reason": "No factual claims in this scope.", "evidence_ids": []}
        self.assertEqual(receipt.validate(self.value)["overall"], 1)
        self.value["dimensions"]["facts"]["reason"] = " "
        self.invalid()
        self.value = copy.deepcopy(CONTROL)
        self.value["dimensions"]["verification"]["score"] = None
        self.invalid()
        for dimension in self.value["dimensions"].values():
            dimension["score"] = None
        self.invalid()

    def test_bool_float_string_and_out_of_range_scores(self):
        for bad in (True, False, 2.0, "2", -1, 4, [], {}):
            with self.subTest(bad=bad):
                self.value["dimensions"]["guidance"]["score"] = bad
                self.invalid()

    def test_high_scores_require_evidence(self):
        for name in ("guidance", "facts", "verification"):
            for score in (2, 3):
                with self.subTest(name=name, score=score):
                    self.value = copy.deepcopy(CONTROL)
                    self.value["dimensions"][name]["score"] = score
                    self.value["dimensions"][name]["evidence_ids"] = []
                    self.invalid()

    def test_dangling_duplicate_and_empty_references(self):
        for owner, key in ((self.value["claims"][0], "source_ids"),
                           (self.value["claims"][0], "evidence_ids"),
                           (self.value["dimensions"]["guidance"], "evidence_ids")):
            original = owner[key]
            for bad in (["missing"], original * 2, "e1", [True]):
                with self.subTest(key=key, bad=bad):
                    owner[key] = bad
                    self.invalid()
            owner[key] = original

    def test_claims_can_separate_facts_from_language_only_findings(self):
        self.value["claims"][0]["source_ids"] = []
        self.assertEqual(receipt.validate(self.value)["overall"], 1)
        self.value["claims"][0]["evidence_ids"] = []
        self.value["claims"][0]["statement"] = "Unsupported: owner confirmation needed."
        self.assertEqual(receipt.validate(self.value)["overall"], 1)

    def test_duplicate_record_ids(self):
        for key in ("sources", "evidence", "claims"):
            self.value = copy.deepcopy(CONTROL)
            self.value[key].append(copy.deepcopy(self.value[key][0]))
            self.invalid()

    def test_missing_and_unknown_keys_at_every_object_level(self):
        for path in ((), ("sources", 0), ("evidence", 0), ("claims", 0),
                     ("dimensions",), ("dimensions", "guidance")):
            self.value = copy.deepcopy(CONTROL)
            owner = self.value
            for part in path:
                owner = owner[part]
            original = copy.deepcopy(owner)
            for key in original:
                with self.subTest(path=path, missing=key):
                    owner.pop(key)
                    self.invalid()
                    owner[key] = original[key]
            owner["approval"] = True
            self.invalid()

    def test_invalid_container_types(self):
        for key in ("sources", "evidence", "claims", "gaps", "blockers", "review_required", "dimensions"):
            for bad in (None, True, 1, "x"):
                self.value = copy.deepcopy(CONTROL)
                self.value[key] = bad
                self.invalid()
        for bad in ([], None, True, "receipt"):
            with self.assertRaises(receipt.ReceiptError):
                receipt.validate(bad)

    def test_strings_cannot_be_empty_or_nonstring(self):
        for path in (("scope",), ("sources", 0, "revision"),
                     ("sources", 0, "locator"), ("sources", 0, "id"),
                     ("evidence", 0, "description"), ("claims", 0, "statement"),
                     ("dimensions", "verification", "reason")):
            for bad in ("", "  ", None, True, 9, "\ud800"):
                self.value = copy.deepcopy(CONTROL)
                owner = self.value
                for part in path[:-1]:
                    owner = owner[part]
                owner[path[-1]] = bad
                self.invalid()
        for key in ("gaps", "blockers", "review_required"):
            self.value = copy.deepcopy(CONTROL)
            self.value[key] = [""]
            self.invalid()

    def test_hash_format_only_and_explicit_revision_states(self):
        import hashlib
        digest = hashlib.sha256(b"fictional fixture").hexdigest()
        for revision in ("unknown", "uncommitted", "abc123"):
            self.value["sources"][0]["revision"] = revision
            self.value["sources"][0]["sha256"] = digest
            self.assertEqual(receipt.validate(self.value)["overall"], 1)
        for bad in ("a" * 63, "g" * 64, "A" * 64, None, 12):
            self.value["sources"][0]["sha256"] = bad
            self.invalid()

    def test_overall_checked_and_round_trip(self):
        result = receipt.validate(self.value)
        self.assertEqual(receipt.loads(json.dumps(result)), result)
        for bad in (True, 1.0, "1", None, 0, 2, 3, 4):
            self.value["overall"] = bad
            self.invalid()
        self.value = copy.deepcopy(CONTROL)
        self.value["schema_version"] = True
        self.invalid()

    def test_duplicate_json_keys_and_nonstandard_constants(self):
        raw = json.dumps(CONTROL)
        for bad in (raw.replace('"score": 2', '"score": 2, "score": 3', 1),
                    raw.replace('"scope":', '"scope": "duplicate", "scope":', 1),
                    raw.replace('"score": 2', '"score": NaN', 1),
                    raw.replace('"score": 2', '"score": Infinity', 1),
                    raw.replace('"score": 2', '"score": -Infinity', 1)):
            with self.subTest(raw=bad), self.assertRaises(receipt.ReceiptError):
                receipt.loads(bad)

    def test_blocked_receipt_can_report_missing_sources(self):
        self.value.update(sources=[], evidence=[], claims=[], blockers=["Required source unavailable."])
        for dimension in self.value["dimensions"].values():
            dimension.update(score=0, reason="Required source unavailable.", evidence_ids=[])
        self.assertEqual(receipt.validate(self.value)["overall"], 0)

    def test_cli_control_and_negative_leave_all_files_unchanged(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "receipt.json"
            sentinel = root / "source.txt"
            sentinel.write_bytes(b"unchanged source")
            for valid in (True, False):
                value = copy.deepcopy(CONTROL)
                if not valid:
                    value["dimensions"]["guidance"]["evidence_ids"] = []
                path.write_text(json.dumps(value), encoding="utf-8")
                before = {p.name: p.read_bytes() for p in root.iterdir()}
                result = subprocess.run([sys.executable, "-B", str(TOOL), str(path)],
                                        capture_output=True, text=True, cwd=root)
                self.assertEqual(result.returncode, 0 if valid else 1, result.stderr)
                if valid:
                    self.assertEqual(json.loads(result.stdout)["overall"], 1)
                    self.assertEqual(result.stderr, "")
                else:
                    self.assertEqual(result.stdout, "")
                    self.assertIn("require evidence", result.stderr)
                self.assertEqual({p.name: p.read_bytes() for p in root.iterdir()}, before)

    def test_cli_invalid_json_encoding_and_missing_path(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "receipt.json"
            for raw in (b"{", b"\xff", None):
                if raw is None:
                    path.unlink()
                else:
                    path.write_bytes(raw)
                result = subprocess.run([sys.executable, "-B", str(TOOL), str(path)],
                                        capture_output=True, text=True)
                self.assertEqual(result.returncode, 1)
                self.assertEqual(result.stdout, "")
                self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
