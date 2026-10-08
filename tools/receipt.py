#!/usr/bin/env python3
"""Validate a local, author-scored receipt; emit JSON to stdout without writing files.

Checks structure, references, and score arithmetic only. Does not read source or
evidence locators, verify hashes, judge evidence adequacy, or establish probability,
compliance, or approval. Python 3.9+ standard library only.
"""

import argparse
import copy
import json
from pathlib import Path
import re
import sys


class ReceiptError(ValueError):
    """Invalid receipt input."""


def object_fields(value, required, optional=()):
    if not isinstance(value, dict):
        raise ReceiptError("expected an object")
    missing = set(required) - value.keys()
    extra = value.keys() - set(required) - set(optional)
    if missing or extra:
        raise ReceiptError("invalid fields: missing=%s unknown=%s" %
                           (sorted(missing), sorted(extra)))


def text(value):
    if not isinstance(value, str) or not value.strip():
        raise ReceiptError("expected a nonempty string")
    if any(0xD800 <= ord(c) <= 0xDFFF for c in value):
        raise ReceiptError("unpaired Unicode surrogate")


def array(value):
    if not isinstance(value, list):
        raise ReceiptError("expected an array")


def strings(value):
    array(value)
    for item in value:
        text(item)


def references(value, known):
    strings(value)
    if len(value) != len(set(value)):
        raise ReceiptError("duplicate reference ID")
    if set(value) - known:
        raise ReceiptError("dangling reference IDs: %s" % sorted(set(value) - known))


def records(value, required, optional=()):
    array(value)
    ids = set()
    for record in value:
        object_fields(record, required, optional)
        text(record["id"])
        if record["id"] in ids:
            raise ReceiptError("duplicate record ID: " + record["id"])
        ids.add(record["id"])
    return ids


def validate(receipt):
    """Return a copy with computed overall. No semantic validation is performed."""
    object_fields(receipt, {"schema_version", "scope", "sources", "evidence", "claims",
                            "gaps", "blockers", "unresolved", "review_required", "reviewer_approval", "dimensions"},
                  {"overall"})
    if type(receipt["schema_version"]) is not int or receipt["schema_version"] != 1:
        raise ReceiptError("schema_version must be integer 1")
    text(receipt["scope"])
    text(receipt["reviewer_approval"])
    source_ids = records(receipt["sources"], {"id", "locator", "revision"}, {"sha256"})
    for source in receipt["sources"]:
        text(source["locator"])
        text(source["revision"])  # 'unknown' and 'uncommitted' are explicit valid values.
        if "sha256" in source:
            digest = source["sha256"]
            if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
                raise ReceiptError("sha256 must be a lowercase 64-digit hexadecimal digest")
    evidence_ids = records(receipt["evidence"], {"id", "locator", "description"})
    for evidence in receipt["evidence"]:
        text(evidence["locator"])
        text(evidence["description"])
    records(receipt["claims"], {"id", "statement", "source_ids", "evidence_ids"})
    for claim in receipt["claims"]:
        text(claim["statement"])
        references(claim["source_ids"], source_ids)
        references(claim["evidence_ids"], evidence_ids)
    for key in ("gaps", "blockers", "unresolved", "review_required"):
        strings(receipt[key])
    object_fields(receipt["dimensions"], {"guidance", "facts", "verification"})
    scores = []
    for name, dimension in receipt["dimensions"].items():
        object_fields(dimension, {"score", "reason", "evidence_ids"})
        text(dimension["reason"])
        references(dimension["evidence_ids"], evidence_ids)
        score = dimension["score"]
        if score is None:
            if name == "verification":
                raise ReceiptError("verification cannot be N/A")
        elif type(score) is not int or not 0 <= score <= 3:
            raise ReceiptError("score must be an integer 0..3 or null")
        else:
            if score >= 2 and not dimension["evidence_ids"]:
                raise ReceiptError("scores >=2 require evidence IDs")
            scores.append(score)
    if not scores:
        raise ReceiptError("at least one applicable dimension is required")
    overall = 0 if receipt["blockers"] else min(scores)
    if "overall" in receipt:
        if type(receipt["overall"]) is not int or receipt["overall"] != overall:
            raise ReceiptError("supplied overall does not match computed overall")
    result = copy.deepcopy(receipt)
    result["overall"] = overall
    return result


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ReceiptError("duplicate JSON key: " + key)
        result[key] = value
    return result


def reject_constant(value):
    raise ReceiptError("non-JSON numeric constant: " + value)


def loads(raw):
    return validate(json.loads(raw, object_pairs_hook=unique_object,
                               parse_constant=reject_constant))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="local UTF-8 JSON receipt (never overwritten)")
    args = parser.parse_args(argv)
    try:
        result = loads(args.path.read_text(encoding="utf-8"))
    except (OSError, ValueError, RecursionError) as exc:
        print("receipt: " + str(exc), file=sys.stderr)
        return 1
    print("receipt: structure and arithmetic valid; evidence and approval unverified; "
          "exit 0 is not artifact approval", file=sys.stderr)
    print(json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True, allow_nan=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
