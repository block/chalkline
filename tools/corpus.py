#!/usr/bin/env python3
"""Optional local reference discovery. Python 3 standard library only."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import sys

DOMAINS = ("shared", "product", "marketing", "support")
ENFORCEMENTS = ("must", "should", "may")
REQUIRED = {"title", "brand", "domain", "enforcement"}
ALLOWED = REQUIRED | {"teaching"}

# Fixed ingestion limits, not CLI options. Bytes refer to original file contents.
MAX_REFERENCE_FILES = 1000
MAX_REFERENCE_BYTES = 1024 * 1024
MAX_TOTAL_REFERENCE_BYTES = 16 * 1024 * 1024
MAX_DIRECTORY_DEPTH = 16
MAX_FILESYSTEM_ENTRIES = 10000


class CorpusError(ValueError):
    """Invalid corpus input."""


def scalar(value):
    """Parse the deliberately small scalar subset described in --help."""
    if value.startswith('"'):
        try:
            result, end = json.JSONDecoder().raw_decode(value)
        except ValueError as exc:
            raise CorpusError("invalid double-quoted string") from exc
        tail = value[end:].strip()
        if not isinstance(result, str) or (tail and not tail.startswith("#")):
            raise CorpusError("expected a string followed only by an optional comment")
    elif value.startswith("'"):
        match = re.fullmatch(r"'((?:[^']|'')*)'\s*(?:#.*)?", value)
        if not match:
            raise CorpusError("invalid single-quoted string")
        result = match.group(1).replace("''", "'")
    else:
        result = re.split(r"\s+#", value, maxsplit=1)[0].strip()
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9 _./-]*", result):
            raise CorpusError("unsupported bare scalar; quote the value")
        if result.lower() in {"null", "true", "false", "~"} or result.isdigit():
            raise CorpusError("ambiguous scalar; quote the value")
    if any(0xD800 <= ord(c) <= 0xDFFF for c in result):
        raise CorpusError("metadata contains an unpaired Unicode surrogate")
    if not result.strip() or any(ord(c) < 32 for c in result):
        raise CorpusError("metadata must be nonempty, single-line strings")
    return result


def parse(raw, path):
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise CorpusError("expected UTF-8") from exc
    if "\x00" in text:
        raise CorpusError("NUL bytes are unsupported")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise CorpusError("missing opening frontmatter delimiter")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise CorpusError("missing closing frontmatter delimiter") from exc
    metadata = {}
    for number, line in enumerate(lines[1:end], 2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = re.fullmatch(r"([a-z]+):[ \t]*(.*)", line)
        if not match:
            raise CorpusError("line %d: expected an unindented key: scalar" % number)
        key, value = match.groups()
        if key not in ALLOWED:
            raise CorpusError("line %d: unsupported key %r" % (number, key))
        if key in metadata:
            raise CorpusError("line %d: duplicate key %r" % (number, key))
        try:
            metadata[key] = scalar(value)
        except CorpusError as exc:
            raise CorpusError("line %d: %s" % (number, exc)) from exc
    missing = REQUIRED - metadata.keys()
    if missing:
        raise CorpusError("missing fields: " + ", ".join(sorted(missing)))
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", metadata["brand"]):
        raise CorpusError("brand must be a lowercase hyphen-separated slug")
    if metadata["domain"] not in DOMAINS:
        raise CorpusError("domain must be one of: " + ", ".join(DOMAINS))
    if metadata["enforcement"] not in ENFORCEMENTS:
        raise CorpusError("enforcement must be one of: " + ", ".join(ENFORCEMENTS))
    vocabulary = Path(path).name.lower() == "vocabulary.md"
    if vocabulary and metadata["enforcement"] != "may":
        raise CorpusError("vocabulary.md must use enforcement: may")
    if "teaching" in metadata:
        if not vocabulary or metadata["teaching"] not in ("on", "off"):
            raise CorpusError("teaching is only supported on vocabulary.md, with on or off")
    if not any(line.strip() for line in lines[end + 1:]):
        raise CorpusError("reference body is empty")
    return metadata, lines[end + 1:], end + 2


def load_corpus(root):
    root = Path(root).absolute()
    # Refuse symlinks in the supplied root, including its parent components.
    for component in (root,) + tuple(root.parents):
        if component.is_symlink():
            raise CorpusError("root path contains a symlink: %s" % component)
    root = root.resolve(strict=True)
    references = root / "references"
    if not references.exists() and not references.is_symlink():
        raise CorpusError("references/ does not exist under the selected root")
    records = []
    entry_count = 0
    reference_count = 0
    total_bytes = 0

    def walk(directory, depth=0):
        nonlocal entry_count, reference_count, total_bytes
        if depth > MAX_DIRECTORY_DEPTH:
            raise CorpusError("directory depth limit exceeded (%d): %s" %
                              (MAX_DIRECTORY_DEPTH, directory.relative_to(root).as_posix()))
        mode = directory.lstat().st_mode
        if stat.S_ISLNK(mode):
            raise CorpusError("symlink not allowed: " + directory.relative_to(root).as_posix())
        if not stat.S_ISDIR(mode):
            raise CorpusError("expected directory: " + directory.relative_to(root).as_posix())
        # Bound enumeration before sorting; ignored files also consume the budget.
        children = []
        with os.scandir(directory) as entries:
            for entry in entries:
                entry_count += 1
                if entry_count > MAX_FILESYSTEM_ENTRIES:
                    raise CorpusError("filesystem entry limit exceeded (%d) under references/" %
                                      MAX_FILESYSTEM_ENTRIES)
                children.append(directory / entry.name)
        for child in sorted(children, key=lambda item: item.name):
            path = child.relative_to(root).as_posix()
            mode = child.lstat().st_mode
            if stat.S_ISLNK(mode):
                raise CorpusError("symlink not allowed: " + path)
            if stat.S_ISDIR(mode):
                walk(child, depth + 1)
            elif not stat.S_ISREG(mode):
                raise CorpusError("special file not allowed: " + path)
            elif child.suffix.lower() == ".md" and child.name.lower() != "readme.md":
                reference_count += 1
                if reference_count > MAX_REFERENCE_FILES:
                    raise CorpusError("reference file count limit exceeded (%d): %s" %
                                      (MAX_REFERENCE_FILES, path))
                with child.open("rb") as stream:
                    raw = stream.read(MAX_REFERENCE_BYTES + 1)
                if len(raw) > MAX_REFERENCE_BYTES:
                    raise CorpusError("reference byte limit exceeded (%d): %s" %
                                      (MAX_REFERENCE_BYTES, path))
                total_bytes += len(raw)
                if total_bytes > MAX_TOTAL_REFERENCE_BYTES:
                    raise CorpusError("total reference byte limit exceeded (%d): %s" %
                                      (MAX_TOTAL_REFERENCE_BYTES, path))
                try:
                    metadata, body, first_line = parse(raw, path)
                except CorpusError as exc:
                    raise CorpusError(path + ": " + str(exc)) from exc
                records.append({"path": path, "metadata": metadata,
                                "sha256": hashlib.sha256(raw).hexdigest(),
                                "bytes": len(raw), "body": body, "first_line": first_line})
    walk(references)
    return sorted(records, key=lambda record: record["path"])


def public_record(record):
    return {key: record[key] for key in ("path", "metadata", "sha256", "bytes")}


def search(records, query, filters):
    terms = query.casefold().split()
    results = []
    for record in records:
        if any(record["metadata"].get(key) != value for key, value in filters.items()):
            continue
        haystack = (record["metadata"]["title"] + "\n" + "\n".join(record["body"])).casefold()
        if not all(term in haystack for term in terms):
            continue
        result = public_record(record)
        result["matches"] = [
            {"line": record["first_line"] + offset, "text": line}
            for offset, line in enumerate(record["body"])
            if terms and any(term in line.casefold() for term in terms)
        ]
        results.append(result)
    return results


HELP = """Scope and format:
  --root is a repository (or example) directory containing references/.
  Reads flat and nested references/**/*.md; ignores README.md (any case)
  and non-Markdown regular files. Calibration and other directories are excluded.
  All symlinks within references/ and in the supplied root path are rejected,
  including internal links; special files are rejected. Do not run against a
  directory being modified concurrently: this is not a filesystem sandbox.

  UTF-8 Markdown must start with a --- line and close frontmatter with ---.
  Required scalar keys: title, brand, domain, enforcement. Optional teaching
  is allowed only on vocabulary.md (on|off; omission leaves it unspecified).
  Vocabulary must use enforcement may. Brand is a lowercase hyphenated slug.
  Domain: shared|product|marketing|support. Enforcement: must|should|may.
  Strings may use JSON double quotes, single quotes (escape ' as ''), or simple
  bare words containing letters, digits, spaces, _, ., /, and -. Inline #
  comments require whitespace after bare values. Blank/comment lines are OK.
  Empty values/body, duplicate/unknown keys, lists, mappings, multiline scalars,
  YAML aliases/tags, BOM, and other YAML features are unsupported and rejected.

Output and limits:
  Fixed ingestion caps: 1000 reference Markdown files; 1 MiB (1048576 bytes)
  per reference; 16 MiB (16777216 bytes) total reference contents; 16 directory
  levels below references/ (which is level 0); 10000 filesystem entries below
  references/, including directories, README placeholders, and non-Markdown files.
  Ignored files do not count toward reference file/byte caps. Reads are bounded
  to the per-file cap plus one byte. Exceeding any cap fails before JSON output
  or output-file creation; no partial results. Limits are not a sandbox and do
  not make concurrent corpus modification safe.
  JSON schema_version 1; paths relative to root, sorted by path, no timestamps
  or absolute paths. SHA-256 covers original file bytes, including frontmatter.
  Index is a manifest, not a database; search always rereads and validates files.
  Search uses case-insensitive literal whitespace-separated terms (AND) across
  title and body, with exact, case-sensitive metadata filters (AND). No fuzzy
  matching, stemming, ranking, implicit shared-domain fallback, or rule evaluation.
  Matches list body lines containing any term; title-only matches have no lines.
  Empty query lists all records satisfying filters. Empty corpus is valid.
  No network, model, content execution, link following, or default disk writes.
  --output explicitly creates a NEW file (never overwrites; parents must exist).
  Check validates structure only, not writing quality or authority of the rules.
  Exit 0: success (including no matches); 1: input/output error; 2: CLI misuse.

Examples:
  python3 tools/corpus.py check --root .
  python3 tools/corpus.py index --root examples/meridian
  python3 tools/corpus.py search payment --root examples/meridian --domain shared
  python3 tools/corpus.py index --root . --output /tmp/chalkline-index.json
"""


def parser():
    cli = argparse.ArgumentParser(description=__doc__, epilog=HELP,
                                  formatter_class=argparse.RawDescriptionHelpFormatter)
    commands = cli.add_subparsers(dest="command", required=True)
    for name in ("check", "index", "search"):
        sub = commands.add_parser(name, epilog=HELP,
                                  formatter_class=argparse.RawDescriptionHelpFormatter)
        sub.add_argument("--root", default=".", help="directory containing references/ (default: .)")
        sub.add_argument("--output", metavar="NEW_FILE", help="create JSON file instead of stdout; never overwrite")
        if name == "search":
            sub.add_argument("query", nargs="?", default="", help="literal terms; AND matching; empty lists all")
            sub.add_argument("--brand", help="exact brand slug filter")
            sub.add_argument("--domain", choices=DOMAINS, help="exact domain filter")
            sub.add_argument("--enforcement", choices=ENFORCEMENTS, help="exact file-default enforcement filter")
    return cli


def main(argv=None):
    args = parser().parse_args(argv)
    try:
        records = load_corpus(args.root)
        result = {"schema_version": 1}
        if args.command == "check":
            result.update({"valid": True, "count": len(records)})
        elif args.command == "index":
            result["records"] = [public_record(record) for record in records]
        else:
            filters = {key: getattr(args, key) for key in ("brand", "domain", "enforcement")
                       if getattr(args, key) is not None}
            result.update({"query": args.query, "filters": filters,
                           "results": search(records, args.query, filters)})
        output = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
        if args.output:
            with open(args.output, "x", encoding="utf-8", newline="\n") as stream:
                stream.write(output)
        else:
            sys.stdout.write(output)
        return 0
    except (CorpusError, OSError, RuntimeError) as exc:
        print("corpus: " + str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
