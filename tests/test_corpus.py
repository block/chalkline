"""Run: python3 -B -m unittest discover -s tests -v"""

import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

TOOL = Path(__file__).resolve().parents[1] / "tools" / "corpus.py"
# Avoid importlib's bytecode cache: the tool and tests need no disk caches.
sys.dont_write_bytecode = True
SPEC = importlib.util.spec_from_file_location("corpus", TOOL)
corpus = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(corpus)
BASE = ('---\ntitle: "Sample"\nbrand: "fictional"\ndomain: "shared"\n'
        'enforcement: "should"\n---\n\n# Sample\nA payment failed.\n')


class CorpusTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        (self.root / "references").mkdir()

    def put(self, name="voice.md", text=BASE):
        path = self.root / "references" / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def cli(self, *args):
        return subprocess.run([sys.executable, "-B", str(TOOL), *args,
                               "--root", str(self.root)], capture_output=True, text=True)

    def test_empty_template_and_readme_placeholders(self):
        self.put("README.md", "# placeholder")
        self.put("nested/readme.MD", "# placeholder")
        self.put("notes.txt", "not Markdown")
        self.assertEqual(corpus.load_corpus(self.root), [])
        result = self.cli("check")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), {"schema_version": 1, "valid": True, "count": 0})
        self.assertEqual(json.loads(self.cli("search", "absent").stdout)["results"], [])

    def test_examples_contract(self):
        records = corpus.load_corpus(TOOL.parents[1] / "examples" / "meridian")
        self.assertEqual(len(records), 4)
        self.assertTrue(all(record["metadata"]["brand"] == "meridian" for record in records))

    def test_nested_hashes_and_determinism(self):
        self.put("z/voice.md")
        first = self.put("a.md", BASE.replace("Sample", "Alpha"))
        self.put("ignored.txt", "ignored")
        (self.root / "calibration").mkdir()
        (self.root / "calibration" / "pair.md").write_text("not a reference")
        before = self.cli("index")
        self.assertEqual(before.returncode, 0, before.stderr)
        os.utime(first, (123, 456))
        self.assertEqual(before.stdout, self.cli("index").stdout)
        records = json.loads(before.stdout)["records"]
        self.assertEqual([r["path"] for r in records], ["references/a.md", "references/z/voice.md"])
        self.assertEqual(records[0]["sha256"], hashlib.sha256(first.read_bytes()).hexdigest())
        self.assertNotIn(str(self.root), before.stdout)
        first.write_bytes(first.read_bytes() + b"\n")
        self.assertNotEqual(before.stdout, self.cli("index").stdout)

    def test_search_and_exact_filters(self):
        self.put("a.md")
        self.put("b.md", BASE.replace('"shared"', '"support"').replace('"should"', '"must"'))
        records = corpus.load_corpus(self.root)
        results = corpus.search(records, "PAYMENT failed", {"domain": "shared"})
        self.assertEqual([r["path"] for r in results], ["references/a.md"])
        self.assertEqual(results[0]["matches"], [{"line": 9, "text": "A payment failed."}])
        self.assertEqual(corpus.search(records, "payment missing", {}), [])
        self.assertEqual(corpus.search(records, "payment", {"brand": "Fictional"}), [])
        self.assertEqual(len(corpus.search(records, "", {"enforcement": "must"})), 1)
        self.assertEqual(corpus.search(records, "", {"domain": "product"}), [])
        result = self.cli("search", "PAYMENT", "--domain", "support", "--enforcement", "must", "--brand", "fictional")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(len(json.loads(result.stdout)["results"]), 1)

    def test_title_only_match_and_literal_search(self):
        self.put(text=BASE.replace('title: "Sample"', 'title: "Rare [token]"'))
        records = corpus.load_corpus(self.root)
        self.assertEqual(corpus.search(records, "[token]", {})[0]["matches"], [])
        self.assertEqual(corpus.search(records, ".*", {}), [])

    def test_supported_scalar_comments_and_quotes(self):
        text = BASE.replace('title: "Sample"', "title: 'Writer''s guide' # comment")
        text = text.replace('brand: "fictional"', 'brand: fictional # comment')
        text = text.replace('domain: "shared"', '# comment\n\ndomain: "shared" # comment')
        self.put(text=text)
        self.assertEqual(corpus.load_corpus(self.root)[0]["metadata"]["title"], "Writer's guide")

    def test_malformed_frontmatter(self):
        cases = [
            "# no frontmatter", BASE.replace("---\n", "", 1),
            BASE.replace("---\n\n#", "\n#"),
            BASE.replace('title: "Sample"', 'title: "unterminated'),
            BASE.replace('title: "Sample"', 'title: "Sample" extra'),
            BASE.replace('title: "Sample"', 'title: ""'),
            BASE.replace('title: "Sample"', 'title: |\n  multiline'),
            BASE.replace('title: "Sample"', 'title: [list]'),
            BASE.replace('title: "Sample"', 'title: &anchor value'),
            BASE.replace('title: "Sample"', 'title: *alias'),
            BASE.replace('title: "Sample"', 'title: true'),
            BASE.replace('title: "Sample"', 'title: 123'),
            BASE.replace('title: "Sample"', 'title: "Sample"\ntitle: "Duplicate"'),
            BASE.replace('title: "Sample"\n', ''),
            BASE.replace('title: "Sample"', 'unknown: "Sample"'),
            BASE.replace('domain: "shared"', 'domain: "unknown"'),
            BASE.replace('enforcement: "should"', 'enforcement: "context"'),
            BASE.replace('brand: "fictional"', 'brand: "Not a slug"'),
            BASE.replace('title: "Sample"', ' title: "Sample"'),
            BASE.replace('title: "Sample"', 'title: "line\\nbreak"'),
            BASE.split('---\n\n')[0] + '---\n',
            '\ufeff' + BASE, BASE + '\x00',
        ]
        for text in cases:
            with self.subTest(text=text):
                self.put(text=text)
                with self.assertRaises(corpus.CorpusError):
                    corpus.load_corpus(self.root)

    def test_invalid_utf8(self):
        self.put().write_bytes(b"\xff")
        with self.assertRaisesRegex(corpus.CorpusError, "UTF-8"):
            corpus.load_corpus(self.root)

    def test_vocabulary_contract(self):
        self.put("vocabulary.md", BASE.replace('"should"', '"may"').replace('---\n\n', 'teaching: "off"\n---\n\n'))
        self.assertEqual(corpus.load_corpus(self.root)[0]["metadata"]["teaching"], "off")
        for text in (BASE, BASE.replace('"should"', '"may"').replace('---\n\n', 'teaching: "yes"\n---\n\n')):
            self.put("vocabulary.md", text)
            with self.assertRaises(corpus.CorpusError):
                corpus.load_corpus(self.root)
        (self.root / "references" / "vocabulary.md").unlink()
        self.put(text=BASE.replace('---\n\n', 'teaching: "off"\n---\n\n'))
        with self.assertRaises(corpus.CorpusError):
            corpus.load_corpus(self.root)

    def test_symlinks_rejected_even_placeholder_or_non_markdown(self):
        target = self.put()
        for name, destination in [("escape.md", self.root.parent), ("internal.md", target),
                                  ("README.md", target), ("ignored.txt", target),
                                  ("broken.md", self.root / "missing"),
                                  ("loop", self.root / "references")]:
            with self.subTest(name=name):
                link = self.root / "references" / name
                link.symlink_to(destination)
                with self.assertRaisesRegex(corpus.CorpusError, "symlink"):
                    corpus.load_corpus(self.root)
                link.unlink()

    def test_symlinked_root_and_references(self):
        alias = self.root / "alias"
        alias.symlink_to(self.root, target_is_directory=True)
        with self.assertRaisesRegex(corpus.CorpusError, "symlink"):
            corpus.load_corpus(alias)
        refs = self.root / "references"
        refs.rmdir()
        refs.symlink_to(self.root, target_is_directory=True)
        with self.assertRaisesRegex(corpus.CorpusError, "symlink"):
            corpus.load_corpus(self.root)

    @unittest.skipUnless(hasattr(os, "mkfifo"), "FIFO not supported")
    def test_special_file_rejected_without_read(self):
        os.mkfifo(self.root / "references" / "pipe.md")
        with self.assertRaisesRegex(corpus.CorpusError, "special file"):
            corpus.load_corpus(self.root)

    def test_missing_references_fails_not_empty(self):
        (self.root / "references").rmdir()
        result = self.cli("check")
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout, "")
        self.assertIn("references/", result.stderr)

    def test_errors_fail_closed_before_search_or_output(self):
        self.put()
        self.put("broken.md", "invalid")
        output = self.root / "result.json"
        result = self.cli("search", "payment", "--brand", "other", "--output", str(output))
        self.assertEqual(result.returncode, 1)
        self.assertFalse(output.exists())
        self.assertEqual(result.stdout, "")
        self.assertIn("references/broken.md", result.stderr)

    def test_surrogates_rejected_before_output_and_unicode_control(self):
        output = self.root / "result.json"
        for escaped in (r'\ud800', r'\udfff'):
            self.put(text=BASE.replace('title: "Sample"', 'title: "' + escaped + '"'))
            for command in ("check", "index", "search"):
                result = self.cli(command, "--output", str(output))
                self.assertEqual(result.returncode, 1, result.stderr)
                self.assertIn("unpaired Unicode surrogate", result.stderr)
                self.assertNotIn("Traceback", result.stderr)
                self.assertFalse(output.exists())
        self.put(text=BASE.replace('title: "Sample"', r'title: "Caf\u00e9 \ud83d\ude80"'))
        result = self.cli("index")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["records"][0]["metadata"]["title"], "Café 🚀")

    def test_stdout_default_and_explicit_output_no_overwrite(self):
        self.put()
        before = sorted(str(p) for p in self.root.rglob("*"))
        result = self.cli("index")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(before, sorted(str(p) for p in self.root.rglob("*")))
        output = self.root / "result.json"
        written = self.cli("index", "--output", str(output))
        self.assertEqual(written.returncode, 0, written.stderr)
        self.assertEqual(written.stdout, "")
        self.assertEqual(output.read_text(), result.stdout)
        output.write_text("do not overwrite")
        self.assertEqual(self.cli("index", "--output", str(output)).returncode, 1)
        self.assertEqual(output.read_text(), "do not overwrite")
        self.assertEqual(self.cli("index", "--output", str(self.root / "missing" / "file")).returncode, 1)

    def test_cli_help_and_bad_filter(self):
        result = subprocess.run([sys.executable, "-B", str(TOOL), "--help"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn("No network", result.stdout)
        self.assertEqual(self.cli("search", "--domain", "unknown").returncode, 2)


if __name__ == "__main__":
    unittest.main()
