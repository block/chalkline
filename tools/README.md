# Optional local corpus tools

Use Python 3.9 or newer. No installation, third-party packages, API keys, network calls, or model access are needed. These tools help maintain and find references; ordinary setup does not need them.

Run from the repository root:

```sh
# Validate reference metadata and file structure.
python3 tools/corpus.py check --root examples/meridian

# Emit a deterministic JSON manifest to stdout.
python3 tools/corpus.py index --root examples/harbor

# Find literal terms within a specific corpus.
python3 tools/corpus.py search reservation --root examples/harbor --domain product

# Inspect the full supported format and options.
python3 tools/corpus.py --help
```

`--root` selects a directory containing `references/`. To check your own system, use `--root .`. Flat and nested Markdown files are included; README placeholders, calibration pairs, and files outside `references/` are not. All symlinks and special files inside references are rejected, as are symlinks in the selected root path. Use a real directory path, not a symlink. Do not modify the corpus concurrently while checking it; this is not a filesystem sandbox.

## What the output means

- **Check:** structural validity and file count. A valid empty template reports `count: 0`; it contains no writing guidance.
- **Index:** relative source paths, metadata, byte counts, and SHA-256 hashes of original file bytes. No timestamps or absolute paths. Paths identify files in this corpus, not permanent rule IDs; renaming changes identity.
- **Search:** matching paths and source lines. Terms are case-insensitive literal substrings separated by whitespace; all terms must appear somewhere in the title or body. Results are path-sorted, not relevance-ranked. Metadata filters are exact and combined with AND. Empty query lists all matching files.

Search validates the entire selected corpus before returning results. Malformed files do not silently disappear or receive guessed metadata. A filter does not automatically include shared guidance: consult the local routing instructions and read all applicable shared sources separately.

`--enforcement` filters the **file default only**. A `should` file may contain an inline `must` rule. Read the full source, including scope, provenance, and exact-wording restrictions, before applying a result. Matching lines are not a complete policy bundle.

## Supported frontmatter

The helper intentionally accepts a small scalar subset, not general YAML:

```yaml
---
title: "Voice"
brand: "example"
domain: "shared"
enforcement: "should"
---
```

Required keys are `title`, `brand`, `domain`, and `enforcement`. Optional `teaching` is supported only on `vocabulary.md`; that file must use `enforcement: "may"`. Allowed domains are `shared`, `product`, `marketing`, and `support`; enforcement is `must`, `should`, or `may`. See `--help` for quoting and comment rules.

Unknown or duplicate keys, missing values, unsupported YAML features, invalid UTF-8, and empty bodies fail visibly. This restricted helper is not a universal reader for other writing repositories. Do not delete approved metadata merely to make another corpus fit it; use or build an explicitly compatible reader instead.

## Output and exit status

JSON goes to stdout by default. `--output NEW_FILE` creates a new file only; it refuses to overwrite an existing file and requires its parent directory to exist. Generated indexes belong outside `references/`, and should not be committed unless there is a specific consumer and freshness check.

Exit status `0` means the operation completed, including an empty corpus or no search matches. Status `1` means an input/output error; `2` means invalid CLI arguments. Consumers must inspect counts and results rather than treating status `0` as evidence of coverage.

Hashes identify bytes; they do not prove approval or trustworthy provenance. These tools do not evaluate prose, resolve conflicts, interpret inline enforcement, verify source-record attestations, or authorize publication. They do not implement the cross-repository snapshot validator described in [PINNING.md](../PINNING.md).

## Traceability receipt checker

Drafting and review now include a [traceability and confidence receipt](../docs/traceability.md) by default. Plain text is sufficient. For an integration that needs structured JSON, the optional checker validates the receipt's fields, internal evidence references, and score arithmetic:

```sh
python3 tools/receipt.py path/to/receipt.json
```

It reads one local JSON file and emits the validated receipt with its computed `overall` to stdout. It never writes back, follows source/evidence locators, verifies hashes, or calls a model. Exit 0 means the receipt is structurally valid—even when `overall` is 0 (blocked). Exit 1 means invalid input; 2 means CLI misuse. Do not use process success as artifact approval.

The author supplies evidence-backed dimension assessments. The checker computes the lowest applicable score, with any declared blocker forcing 0. It rejects invalid scores, duplicate keys and IDs within each record group, dangling links, missing reasons, and inconsistent supplied totals. It cannot detect invented evidence, omitted blockers, unjustified N/A, or misleading reasoning. Evidence adequacy still needs review.

See [the JSON receipt format](receipt-format.md) for fields and an example. No receipt storage, analytics, or person-level scoring is required or provided.

Run regression tests with `python3 -m unittest discover -s tests -v`. See [CONTRIBUTING.md](../CONTRIBUTING.md) for separate contract and behavioral checks.
