# Learning without self-governance

Chalkline can improve from the work it helps produce without turning output into policy or people into telemetry.

```text
Use -> notice -> propose -> decide -> change -> calibrate -> distribute -> observe
```

Each step produces a different kind of record:

1. **Use:** an agent consults a reviewed repository-local language snapshot or local writing system for a real task.
2. **Notice:** a person or agent reports a missing rule, conflict, retrieval failure, factual boundary, or calibration drift.
3. **Propose:** someone writes the smallest candidate change and links the public-safe evidence that motivated it.
4. **Decide:** the responsible person approves, edits, rejects, or routes the proposal elsewhere. An approved draft is not automatically a rule.
5. **Change:** approved language guidance changes by visible diff. Existing calibration pairs remain history unless privacy, legal, copyright, or factual-correction needs require removal.
6. **Calibrate:** re-run an applicable pair with one changed factor. Add a pair only for newly approved direction or genuinely new coverage.
7. **Distribute:** consuming owners deliberately update their validated source record and reviewed local snapshot. No consumer or drafting agent silently inherits the newest upstream revision.
8. **Observe:** check the next comparable task. Did the gap disappear without creating a new conflict, factual error, or review burden?

## A small learning record

Keep evidence in the place that owns it — an issue, pull request, review thread, or calibration pair. Do not add a database or log every interaction. A useful public-safe record answers:

```text
Observed: what happened, in which task and harness?
Expected: what should have happened?
Candidate: the smallest rule, example, routing, or protocol change.
Decision: approved / edited / rejected / routed elsewhere — by which role, for what scope, representing whom?
Affected groups and dissent: who is constrained, who was heard, and what valid variation remains?
Check: which held-out reproduction tests the change, with what control and failure criterion?
Rollout: which known consumers need a deliberate pin decision, and what is the previous known-good pin?
Result: across the predeclared comparable samples, did the original problem or a new regression occur?
Record boundary: who may see this record, when is it deleted, and can it be linked to a worker?
```

A rejected candidate is still useful evidence: it can show that the request was a product fact, a one-off judgment, outside the writing system's scope, or not worth the added complexity.

## Keep four approvals separate

One person may hold more than one role, but one decision never implies the next. For cross-team guidance, `must` rules, exact wording, or changes that constrain a group, do not let an owner self-certify representation: name the affected groups, the decision role and its mandate, preserved dissent or valid variants, and an appeal, local-exception, or rollback route.

1. **Approve this artifact for use.**
2. **Approve this artifact as reusable calibration direction** for a stated channel, audience, and purpose.
3. **Approve a normative reference change.**
4. **Approve deployment to a consuming repository** by updating its validated source record and reviewed local snapshot.

Before a source or snapshot change, follow [PINNING.md](PINNING.md): a human reviewer or trusted integration independently resolves the canonical source and full revision, rejects operational directives, and projects only declarative language data into a reviewed local snapshot. Drafting agents never interpret the external instruction repository. Test the candidate snapshot in the actual consuming harness on a held-out comparable sample; run an unchanged control; predeclare the failure criterion; and keep the previous known-good source and snapshot. Never use the agent's usage report as verification. Do not deploy if the candidate is unreadable, changes factual strength, misses applicable calibration, creates an unresolved conflict, or cannot be rolled back. The guidance owner approves the change; the consuming owner approves deployment.

## What is worth learning

Prefer changes that make the system:

- **more used:** a consumer can actually find and read its reviewed local guidance;
- **more effective:** an applicable calibration direction steers the output;
- **more honest:** missing facts, unavailable sources, conflicts, and human boundaries stay visible;
- **less burdensome:** one shared agreement replaces repeated prompt-writing, correction, or review;
- **more maintainable:** a rule has a responsible owner, understandable scope, and evidence that still applies.

The cheapest useful measures are task-level, not person-level:

- Was the reviewed local snapshot present with its required source record?
- Was an applicable calibration pair available?
- Did the output preserve supplied facts and non-negotiable wording?
- Did the same gap recur across the comparable samples selected before rollout?
- Did the change remove the target correction without adding factual, representational, accessibility, localization, or review-burden regressions?

These are diagnostic questions, not a compliance score. Predeclare what counts as comparable, the observation window, denominator, primary failure, and burden/regression checks. Keep an unchanged control; record known model, harness, settings, task input, and resolved revision. A single favorable or author-selected next task is anecdotal, not evidence that the diff worked. Report missing and negative observations; do not turn silence or unknown coverage into a pass.

## What must not become recursive

- Do not promote frequently used words, accepted drafts, reactions, or model outputs into guidance automatically.
- Do not infer team policy from one person's edit or approval of one artifact.
- Do not rank, score, profile, or make employment decisions about individual writers.
- Do not require people to submit learning or usage reports. Reports are purpose-limited and writer-controlled by default; do not aggregate them, join them to identity or performance systems, or retain task identifiers when a synthetic reproduction will do.
- Do not copy private usage reports or work artifacts into a public Chalkline repository. A technically public-safe report may still identify a person or confidential event through rare context; check for re-identification before publishing.
- Do not let a language system approve its own changes or bump its own consumers.
- Do not treat lack of reported gaps as proof that coverage is complete.

The recursive unit is **a reviewed diff with a reproduction**, not an agent memory, an engagement metric, or an accepted sentence.

## Upstream and local learning

A team's language repository learns about that team's language. The upstream Chalkline project learns about the setup and operating protocol.

- Send **local language gaps** to the people responsible for that language system.
- Send **repeatable protocol failures** upstream using the setup-experience issue form, with fictional or redacted evidence.
- Keep product facts, approvals, delivery state, and outcomes in the systems that own them; link them when appropriate rather than copying them into language guidance.

Upstream should change only when a public-safe reproduction shows a repeatable failure, an independent implementation proves a useful convention, or designated maintainers accept a documented evidence exception for a consequential failure that cannot be reproduced safely. An exception must still produce the smallest synthetic regression possible and may not disclose the reporter or source material. One surprising output is a case to investigate, not a standard to ship.
