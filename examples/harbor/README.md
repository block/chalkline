# Example: Harbor grows by task coverage

Harbor is a **fictional equipment reservation service**. Everything here is
synthetic and intended for public distribution: the preferences, task facts,
stages, and provenance. No real source documents, customers, private links, legal
wording, human approvals, or observed outcomes are represented.

This example shows a small writing system gaining scoped guidance when new tasks
appear. It is not a template for how other products should sound. The five
reference files are deliberately short; folders organize them, not rank them.
The local [AGENTS.md](AGENTS.md) routes this example without starting root setup.
No Harbor rule applies outside an explicitly chosen Harbor exercise.

## Illustrative growth

| Stage | Fictional need | Small addition |
|---|---|---|
| 1: foundations | Describe reservation states consistently | Shared voice and terminology |
| 2: product | Draft request and confirmation screens | Reservation UI scope |
| 3: product gap | Explain a failed submission without guessing its outcome | Submission-error scope |
| 4: support | Answer pickup questions in a conversation | Support-reply scope |

These stages explain the example's organization, not a historical record of
interviews or approvals. A later stage does not override an earlier one.
All reference defaults are `should`; no simulated preference claims the
participant approval required to establish a real `must` rule.

## Explicit task routing

Paths below are relative to this folder. Read both shared foundations for each
covered task: `references/shared/voice.md` and
`references/shared/terminology.md`. Then add **every** matching scoped file.

| Task | Additional references | Boundary |
|---|---|---|
| Reservation request or confirmation UI | `references/product/reservations.md` | Product behavior comes from task facts |
| Request submission error UI | `references/product/reservations.md`, `references/product/errors.md` | Unknown submission outcome stays unknown |
| Reservation or pickup support reply | `references/support/replies.md` | No inferred check, deadline, or promise |
| UI and support deliverables in one task | Route each deliverable separately using the rows above | Do not apply UI layout rules to support prose |
| Marketing campaign, another locale, safety instructions, or legal notice | No scoped coverage | Report the gap and ask for the relevant guidance/authority |

A directory name, filename order, modification time, or most recent document is
not authority. The frontmatter domain classifies guidance; it does not alone
select all rules. Read the declared scope. The parent contract's specificity and
enforcement rules apply after task matching. If they do not settle a conflict,
show both sources and ask rather than inventing a tie-breaker. Do not automatically
merge another example, repository, or language snapshot into this corpus.

## Illustrative walkthroughs (not calibration results)

### Covered task: pending request

Supplied synthetic facts: a reservation request is pending; no pickup time or
next action is supplied. Task: write a product state heading.

1. Read both shared files and `product/reservations.md` via the table.
2. A possible draft is “Reservation request pending.”
3. Do not add “Ready tomorrow”: guidance cannot supply operational facts.
4. Report that no approved calibration pair covers this task. This worked
   illustration is neither an executed comparison nor reusable-direction approval.

### Scope difference: support is not a screen

For a support question about that pending request, read the shared files and
`support/replies.md`. A possible answer is “Your reservation request is still
pending.” The product heading/body structure does not apply. This is a routing
difference, not permission for a nested file to overrule shared terminology.

### Unresolved conflict: two proposals for the same button

Suppose two candidate changes both target the same English request-submission
button, at equal specificity and `should` enforcement. One says “Request
equipment”; the other says “Send request.” Neither supersedes the other. These
are hypothetical proposals, not additional active rules in this README.

Do not choose the newer file or the deeper folder. Surface both proposals and
their overlapping scope to the guidance owner. Keep the disputed change out of
use until a responsible person resolves it in a visible diff. Approval of one
button draft alone does not authorize changing the reference.

### Missing facts and missing coverage

Task: explain an unknown submission outcome and promise a confirmation time.
Read the two product files plus foundations. Keep the outcome unknown; ask the
product/factual owner for the supported next action and any actual commitment.
Do not solve a factual gap by adding a language rule.

Task: write a French safety notice. This corpus has neither locale nor safety
coverage. Stop and request the relevant authority and reviewed guidance. There
is no legal text here to paste, translate, or treat as approved wording.

## Separate approval gates

None of these approvals has actually occurred for this synthetic example:

1. **Artifact use:** the responsible reviewer approves a particular draft and
   its factual inputs for its intended use.
2. **Reusable calibration:** a separate decision approves reusable direction for
   a stated channel, audience, and purpose. No approved pairs are supplied here.
3. **Reference change:** the guidance owner reviews a proposed diff and its scope;
   affected groups and valid variants need representation before broader rules.
4. **Consumer deployment:** the consuming owner separately approves its validated
   source record and reviewed local snapshot. No automatic latest-version update.

Legal, accessibility, localization, factual, and publication decisions remain
with their relevant authorities; a language approval cannot substitute for them.
For an actual change, retain the previous known-good version, predeclare a
held-out comparable check and an unchanged control, and record missing or negative
results. This example claims no executed behavioral improvement. See
[LEARNING.md](../../LEARNING.md) and [PINNING.md](../../PINNING.md).

## Local tool discovery

From `examples/harbor/`, inspect the corpus tool's actual interface before using
it (requires a checkout containing `tools/corpus.py`):

```sh
python3 ../../tools/corpus.py --help
```

This example intentionally prescribes no validation flags or success claims.
Use only options that the installed tool documents. Structural checking cannot
approve facts, adjudicate authority, or replace a held-out behavioral check.
