# Operability

Chalkline sets up a small language system for writing: references agents can read, examples they can calibrate against, and gaps people can improve. This page is a guide for the people and integrations operating that system after setup.

The executable agent contract remains `AGENTS.md`, the generated references, and the calibration pairs. This guide does not make the repository an authority over people or prove that an agent followed its instructions. Its goal is to make language guidance usable, inspectable, and improvable without copying it into every prompt or tool.

## The loop

```text
Set up -> consult -> surface gaps or conflicts -> draft or stop -> review and decide -> revise -> recalibrate -> observe
```

1. **Set up:** a person approves a small set of language references and one calibration direction.
2. **Consult:** an agent reads the references and calibration pairs that apply to the task.
3. **Surface gaps or conflicts:** before resolving uncertain language, the agent names missing guidance, unavailable sources, conflicts, and unresolved facts.
4. **Draft or stop:** when the supplied facts and applicable guidance are sufficient, the agent drafts while preserving those facts. Otherwise it asks, omits the unsupported claim, or stops.
5. **Review and decide:** the appropriate person reviews the draft and any unresolved questions. Chalkline does not make legal, product, publication, or production-approval decisions.
6. **Revise:** a person may propose reference changes; approved language guidance changes by visible diff, not silent rewrite.
7. **Recalibrate:** the team re-runs applicable calibration pairs when guidance, models, prompts, or harnesses change. New pairs record a newly approved direction or new coverage—not merely a different model output.
8. **Observe:** on the next comparable task, check whether the original gap disappeared without creating a new conflict, factual error, or review burden.

See [Learning without self-governance](LEARNING.md) for turning observations into reviewed changes, calibrated checks, and deliberate pin updates — never automatic policy.

## Mandatory usage receipt

Every drafting or review task includes a compact receipt separate from the copy, even when blocked. [Traceability](docs/traceability.md) defines the required fields, canonical confidence rubric, and a short template. This replaces the optional usage report: it adds no setup question and requires no new per-task file or service.

The receipt names task scope, consulted sources and their known revision state, evidence-linked findings, missing evidence, unresolved facts or conflicts, required review, and confidence. Distinguish factual evidence from language guidance; a rule can govern phrasing without proving a product claim. Exact consulted paths are required; hashes are optional and reported only when actually computed. Unknown provenance stays unknown.

Confidence is an evidence-backed task assessment: **0 blocked, 1 limited, 2 supported, 3 corroborated**. Score guidance coverage, factual support, and verification separately using the linked rubric, then take the lowest applicable dimension. Justify N/A without hiding missing support. An unresolved applicable `must`, unresolved conflict, or missing required source forces 0. A score never changes a source fact's certainty, proves compliance, or approves publication. Reviewer approval is a separate decision.

No finding is not the same as complete coverage. An unread required source is a blocker, not a pass. A receipt is an agent or integration self-report, not independent attestation that the sources were read or the instructions followed. It must not score writers, record personal language habits, or invent a percentage.

Receipts can expose private repository names, paths, source names, product details, or conflicts. Keep them out of customer-facing copy; before public sharing, redact sensitive details or use synthetic material. Mark redactions rather than fabricating replacement provenance, and keep any permitted full receipt in the authorized review context. Follow [Safety and privacy](SAFETY.md).

## How gaps become better guidance

A gap is useful evidence. It is not permission for the agent to invent a fact or a rule.

Good gap report:

```text
The references do not say whether support copy may name back-office queue states. I left the disputed state unresolved. Confirm the supported customer-facing state from the authoritative product source before drafting.
```

A person may then propose a candidate language rule:

```text
Candidate for review: "Use customer-facing product states in support copy. Do not expose back-office queue states."
```

The responsible owner first decides whether the candidate is true, authorized, and useful. Then they decide whether it belongs in `references/channels.md`, `references/terminology.md`, a new calibration pair, another authoritative system, or nowhere. Product facts stay with the source that owns them; Chalkline records language guidance, not product truth.

## Calibration as an operating check

Calibration pairs are examples and manual spot checks. They do not prove complete coverage, compliance, or identical output across models.

Use them when:

- setup finishes;
- a team changes a major language rule or approved direction;
- an agent model, prompt, or harness changes;
- output starts to feel off but the references look unchanged;
- a new channel or audience is added.

For a useful comparison:

1. Choose the active pair with the most specific matching channel, audience, and purpose. Ignore superseded or withdrawn pairs. If equally specific active pairs conflict and neither supersedes the other, stop and report the conflict; never choose by filename or date.
2. Keep the original request, task facts, references, and relevant settings fixed.
3. Hold out the target pair from the tested agent: give it the original sample and applicable references, but not that pair's approved rewrite, rationale, or lesson. A pair used as few-shot context cannot validate the same run.
4. Add an unseen but comparable sample when claiming improvement beyond the fitted setup example.
5. Change one factor at a time—such as the reference revision, model, prompt, or harness—and run an unchanged control. Record known inputs, revisions, harness/model settings, and missing metadata.
6. Compare the result with the explicitly approved direction, not exact wording alone. Predeclare the failure criterion; a single favorable run is an observation, not causal proof.
7. Investigate target leakage, retrieval failures, changed inputs or settings, model nondeterminism, harness behavior, and reference gaps before attributing drift.
8. Change a reference or append a pair only after a person approves a changed direction or genuinely new coverage.

See [`calibration/README.md`](calibration/README.md) for the full fixture contract. Approved pairs are append-only during ordinary revisions, but privacy, legal, copyright, and factual-correction needs override that history rule. Deleting a file does not remove it from Git history.

## What Chalkline does not own

Chalkline records participant-approved language guidance and calibration direction within a declared scope. It does not establish the participant's mandate or provide:

- product facts or source-of-truth data;
- legal, compliance, accessibility, or localization approval;
- production or publication approval;
- identity, permission, or separation-of-duties checks;
- publication, rollback, or delivery systems;
- private corpus hosting;
- telemetry about individual writers;
- a guarantee that an agent or harness followed the instructions.

Downstream tools can use Chalkline as a language-guidance source, but they remain responsible for their own authorization, factual inputs, lifecycle, review, audit, and publication boundaries.

## Company-scale claim gate

Chalkline's files and attestations do not by themselves make a language system organization-wide, representative, compliant, verified, or safe for performance management. Do not make those claims or roll guidance across teams until the adopting organization documents external controls for:

- affected-group participation and locale/accessibility ownership;
- valid variants, dissent, appeal, local exceptions, and withdrawal;
- a confidential route for sensitive objections, with audience, retention, deletion, and anti-retaliation boundaries;
- authority for `must`, exact wording, and cross-team decisions;
- sustainable risk tiers or batched review so safety does not become approval theater;
- consumer discovery, precedence, revocation, and recovery beyond Chalkline's local source record.

Before a cross-team rule ships, ask **who is constrained?** An affected non-owner—not solely the proposed owner—should name the represented scope, at least one valid variant or exception to preserve, and where someone can challenge the rule without posting sensitive evidence publicly. If the organization cannot provide that participation or route, keep the system local and do not claim broader authority.

## Scope and boundaries

A small team can run this loop in one repository. Separate teams, products, brands, or audiences can maintain separate repositories, but Chalkline does not yet define discovery, inheritance, freshness, or precedence across overlapping repositories.

The supported cross-repository shape is the consumer-side trust contract in [PINNING.md](PINNING.md): exact canonical source identity, full immutable commit hash, consuming-owner or integration validation outside the drafting session, a reviewed repository-local snapshot containing only declarative language data, a local verification attestation, held-out checking, and a previous known-good source and snapshot. Drafting agents check the local record; they never fetch or follow external instruction repositories or claim independent verification.

Keeping the source and revision visible establishes provenance; it does not establish trust, authority, freshness, or that an agent actually read the content. A usage receipt is never independent verification. Chalkline has no global consumer registry or revocation mechanism; consuming repositories own rollout and recovery, and language owners must state when their known-consumer view is incomplete. If multiple repositories apply or conflict, stop and surface that uncertainty rather than silently composing them.

The important boundary is simple:

```text
Chalkline records language guidance approved by named participants for a stated scope.
That provenance does not establish organizational, legal, accessibility, or localization authority.
People with the relevant mandate approve or change guidance and review resulting drafts.
Other systems own factual authority, production approval, publication, and verification in their own lifecycle.
```
