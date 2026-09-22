# JSON receipt format (version 1)

Plain-text receipts remain the default user interface. This optional JSON representation supports local integrations with `python3 tools/receipt.py FILE.json`. The [traceability contract](../docs/traceability.md) governs meaning; the checker validates structure and arithmetic only.

All fields below are required except `sha256` and `overall`. Unknown fields are rejected. Strings must be nonempty; lists may be empty where there is nothing to report. An empty list is an explicit claim of absence, not a way to hide unknowns.

| Field | Shape and meaning |
|---|---|
| `schema_version` | Integer `1` |
| `scope` | Task, assessed artifact/version, audience/channel, and exclusions in one string |
| `sources` | List of `{id, locator, revision, sha256?}`. Exact consulted source paths/headings; revision may explicitly be `unknown` or `uncommitted`. Label supplied vs verified identities in the revision text. Optional SHA-256 is 64 lowercase hex digits over the identified file bytes, only if actually computed. |
| `evidence` | List of `{id, locator, description}`. Task evidence and recorded checks; distinguish supplied facts from independent confirmation. Locators are labels, never fetched by the checker. |
| `claims` | List of `{id, statement, source_ids, evidence_ids}`. Keep language-rule links separate from factual/check evidence. Either link list may be empty for a one-sided basis. If both are empty, explicitly call the finding unsupported in its statement. |
| `gaps` | String list: missing evidence/checks, required or optional, and effect |
| `blockers` | String list: unresolved necessary facts, applicable musts, conflicts, or required sources/checks. Any entry forces overall 0. |
| `unresolved` | String list: remaining facts, questions, and decisions. Any blocking item must also appear in `blockers`. |
| `review_required` | String list: responsible role, needed decision, unknown owner if applicable. |
| `reviewer_approval` | Separate string: `not recorded`, or an actual supplied decision with scope and source. Never inferred from confidence. |
| `dimensions` | Exactly `guidance`, `facts`, `verification`; each is `{score, reason, evidence_ids}` |
| Dimension `score` | Integer 0–3, or `null` for justified N/A. Verification cannot be N/A. |
| Dimension `reason` | Concrete reason tied to the rubric, including rationale for N/A |
| Dimension `evidence_ids` | Links to recorded evidence. Scores 2 or 3 require at least one link; a link alone does not justify that score. |
| `overall` | Optional integer. If supplied it must equal the minimum applicable score, or 0 when blockers exist. The checker includes the computed value in output. |

Record IDs are unique within each list. Duplicate JSON keys and duplicate or dangling references are errors. Nothing in this format authorizes keeping receipts, sharing private evidence, or scoring people. Omitted blockers and dishonest judgments cannot be detected mechanically.

## Fictional limited-support example

This example illustrates the format, not an executed review or verified provenance. Its overall score is 1. No hash or approval is invented.

```json
{
  "schema_version": 1,
  "scope": "Review fictional error draft v1 for a payment UI; excludes publication approval.",
  "sources": [
    {"id": "s1", "locator": "references/terminology.md#Payment errors", "revision": "uncommitted; fictional example"}
  ],
  "evidence": [
    {"id": "e1", "locator": "supplied-message:fictional-task", "description": "The supplied task says the payment failed; not independently confirmed."}
  ],
  "claims": [
    {"id": "c1", "statement": "Preserve the stated payment failure.", "source_ids": [], "evidence_ids": ["e1"]}
  ],
  "gaps": ["Optional calibration coverage missing."],
  "blockers": [],
  "unresolved": [],
  "reviewer_approval": "not recorded",
  "review_required": ["Content reviewer must check wording and supporting evidence.", "Reviewer approval: not recorded."],
  "dimensions": {
    "guidance": {"score": 1, "reason": "Required terminology is available; optional calibration coverage is missing.", "evidence_ids": []},
    "facts": {"score": 1, "reason": "The supplied task supports the claim, but authority is unconfirmed.", "evidence_ids": ["e1"]},
    "verification": {"score": 1, "reason": "Only an informal reread is reported; no required check is missing.", "evidence_ids": []}
  }
}
```

Unknown nonblocking questions belong in `gaps`; necessary unresolved facts or requirements belong in `blockers`. The JSON checker cannot classify prose into those categories. It requires a separate approval-status field but cannot verify its truth; the reviewer checks that semantic requirement. Structural validity and process exit status must never be displayed as confidence in the draft.
