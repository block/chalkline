# calibration/

Approved before/after pairs from setup and revision runs. This folder starts empty; Phase 4 of the setup protocol fills it.

Each pair is one file, numbered and append-only:

```text
calibration/
├── 001-support-reply.md
├── 002-trip-invite-email.md
└── …
```

Each file contains:

- **Original** — a redacted, synthetic, or otherwise repository-safe sample
- **Without the system** — a baseline produced in a clean session with no references
- **With the system** — the rewrite consulting `references/`
- **Baseline method** — how the no-system version was produced; if no clean session was available, say the comparison is informal
- **What drove the difference** — the specific rules, by file
- **Approved** — date the user said "yes, that sounds like us"

## What these are for

1. **Calibration checks.** Switched models or harnesses? Re-run a pair: give an agent the original plus `references/` and compare its rewrite against the approved direction. Drift may reveal a reference gap or a model or harness difference.
2. **Few-shot examples.** Approved rewrites show your voice *applied*, not just described. Agents consulting this repo read the most recent pair alongside the references.

## Rules

- Preserve supplied facts. Writing guidance must never invent causes, states, dates, deadlines, guarantees, names, amounts, eligibility, or required actions.
- Pairs are **append-only** for ordinary revisions. Privacy, legal, copyright, and factual-correction needs override that rule; remember that deleting a file does not remove it from Git history.
- Every pair was human-approved at creation. If your voice changes, old pairs stay as history; the newest pair wins for calibration.
