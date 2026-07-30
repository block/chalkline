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
- **What this teaches** — the one lesson a new teammate should take from the pair
- **Approved** — date the user said "yes, that sounds like us"

## What these are for

1. **Calibration checks.** Switched models or harnesses? Re-run a pair: give an agent the original plus `references/` and compare its rewrite against the approved direction. Drift may reveal a reference gap or a model or harness difference.
2. **Few-shot examples.** Approved rewrites show your voice *applied*, not just described. Agents consulting this repo read the newest pair that applies to the task's channel, audience, and purpose alongside the references. If no pair applies, that is a coverage gap.
3. **Teaching artifacts.** A pair should make one lesson visible to a new teammate, not only to a model.

## Rules

- Preserve supplied facts — including their strength. Writing guidance must never invent causes, states, dates, deadlines, guarantees, names, amounts, eligibility, or required actions, and never soften or harden the ones supplied.
- Pairs are **append-only** for ordinary revisions. Privacy, legal, copyright, and factual-correction needs override that rule; remember that deleting a file does not remove it from Git history.
- Approval of an ordinary artifact does not approve it as a calibration pair. A person must explicitly approve the rewrite as reusable direction for its stated channel, audience, and purpose.
- A new pair records genuinely new coverage or a newly approved direction—not every accepted draft or different model output. If a pair suggests a general rule, propose that rule separately; an example never silently promotes itself into policy.
- Approved pairs stay as history. If your voice changes, the newest applicable pair wins for its channel, audience, and purpose.
