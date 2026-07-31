# calibration/

Before/after pairs explicitly approved as reusable, scoped direction during setup or revision. This folder starts empty; artifact approval alone does not fill it.

Each pair is one file, numbered and append-only:

```text
calibration/
├── 001-support-reply.md
├── 002-trip-invite-email.md
└── …
```

Each file contains:

- **ID** — a stable identifier, usually the filename number and slug
- **Scope** — explicit channel, audience, and purpose; `any` is allowed only when the approver deliberately chose it
- **Status** — `active`, `superseded`, or `withdrawn`; active pairs may name the ID they supersede
- **Reference revision** — the commit used when the direction was approved, or `uncommitted setup` during setup
- **Original** — a redacted, synthetic, or otherwise repository-safe sample
- **Without the system** — a baseline produced in a clean session with no references
- **With the system** — the rewrite consulting `references/`
- **Baseline method** — how the no-system version was produced; if no clean session was available, say the comparison is informal
- **What drove the difference** — the specific rules, by file
- **What this teaches** — the one lesson a new teammate should take from the pair
- **Reusable-direction approval** — date, participant/role, and stated scope; artifact approval alone is insufficient

## What these are for

1. **Calibration checks.** Switched models or harnesses? Hold the target pair out from the tested agent: provide its original plus applicable references, but not that pair's approved rewrite, rationale, or lesson. The reviewer compares the output with the approved direction. A pair used as few-shot context cannot validate the same run; use an unseen comparable sample before claiming broader improvement.
2. **Few-shot examples.** Approved rewrites show your voice *applied*, not just described. For ordinary drafting, agents consult the active pair with the most specific matching scope. If more than one active pair has the same most-specific scope and neither explicitly supersedes the other, report a conflict instead of choosing by filename, date, or filesystem order. A pair never overrides a conflicting reference.
3. **Teaching artifacts.** A pair should make one lesson visible to a new teammate, not only to a model.

## Rules

- Preserve supplied facts — including their strength. Writing guidance must never invent causes, states, dates, deadlines, guarantees, names, amounts, eligibility, or required actions, and never soften or harden the ones supplied.
- Pairs are **append-only** for ordinary revisions. Privacy, legal, copyright, and factual-correction needs override that rule; remember that deleting a file does not remove it from Git history.
- Approval of an ordinary artifact does not approve it as a calibration pair. A person must explicitly approve the rewrite as reusable direction for its stated channel, audience, and purpose.
- A new pair records genuinely new coverage or a newly approved direction—not every accepted draft or different model output. If a pair suggests a general rule, propose that rule separately; an example never silently promotes itself into policy.
- Superseded and withdrawn pairs stay as history but are not drafting guidance. When direction changes, append a new active pair and mark the prior pair `superseded` with the new ID; do not infer precedence from filename or date. Privacy, legal, copyright, and factual-correction needs may still require removal.
