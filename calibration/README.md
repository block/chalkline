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

- **Original** — the user's real copy, as provided
- **Without the system** — the agent's rewrite with no references
- **With the system** — the rewrite consulting `references/`
- **What drove the difference** — the specific rules, by file
- **Approved** — date the user said "yes, that sounds like us"

## What these are for

1. **Regression checks.** Switched models or harnesses? Re-run a pair: give any agent the original plus `references/` and compare its rewrite against the approved one. Drift means your references need attention — you find out here, not in production.
2. **Few-shot examples.** Approved rewrites show your voice *applied*, not just described. Agents consulting this repo read the most recent pair alongside the references.

## Rules

- Pairs are **append-only**. Never rewrite an approved pair — add a new one.
- Every pair was human-approved at creation. If your voice changes, old pairs stay as history; the newest pair wins for calibration.
