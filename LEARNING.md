# Learning without self-governance

Chalkline can improve from the work it helps produce without turning output into policy or people into telemetry.

```text
Use -> notice -> propose -> decide -> change -> calibrate -> distribute -> observe
```

Each step produces a different kind of record:

1. **Use:** an agent consults a pinned writing system for a real task.
2. **Notice:** a person or agent reports a missing rule, conflict, retrieval failure, factual boundary, or calibration drift.
3. **Propose:** someone writes the smallest candidate change and links the public-safe evidence that motivated it.
4. **Decide:** the responsible person approves, edits, rejects, or routes the proposal elsewhere. An approved draft is not automatically a rule.
5. **Change:** approved language guidance changes by visible diff. Existing calibration pairs remain history unless privacy, legal, copyright, or factual-correction needs require removal.
6. **Calibrate:** re-run an applicable pair with one changed factor. Add a pair only for newly approved direction or genuinely new coverage.
7. **Distribute:** consuming repositories deliberately bump their language pins. No consumer silently inherits the newest revision.
8. **Observe:** check the next comparable task. Did the gap disappear without creating a new conflict, factual error, or review burden?

## A small learning record

Keep evidence in the place that owns it — an issue, pull request, review thread, or calibration pair. Do not add a database or log every interaction. A useful public-safe record answers:

```text
Observed: what happened, in which task and harness?
Expected: what should have happened?
Candidate: the smallest rule, example, routing, or protocol change.
Decision: approved / edited / rejected / routed elsewhere — by whom?
Check: which calibration pair or reproduction tests the change?
Rollout: which language pins need a deliberate bump?
Result: on the next comparable task, did the original problem recur?
```

A rejected candidate is still useful evidence: it can show that the request was a product fact, a one-off judgment, outside the writing system's scope, or not worth the added complexity.

## Keep four approvals separate

These decisions may belong to the same person, but one never implies the next:

1. **Approve this artifact for use.**
2. **Approve this artifact as reusable calibration direction** for a stated channel, audience, and purpose.
3. **Approve a normative reference change.**
4. **Approve deployment to a consuming repository** by bumping its language pin.

Before a pin bump, test the candidate revision in the consuming repo with its actual harness: rerun an applicable calibration pair, verify the usage report names the candidate revision, and compare it with the old pin while keeping the task facts fixed. Do not bump if the candidate is unreadable, changes factual strength, misses applicable calibration, or creates an unresolved conflict. The guidance owner approves the change; the consuming owner approves deployment.

## What is worth learning

Prefer changes that make the system:

- **more used:** a consumer can actually find and read the pinned guidance;
- **more effective:** an applicable calibration direction steers the output;
- **more honest:** missing facts, unavailable sources, conflicts, and human boundaries stay visible;
- **less burdensome:** one shared agreement replaces repeated prompt-writing, correction, or review;
- **more maintainable:** a rule has a responsible owner, understandable scope, and evidence that still applies.

The cheapest useful measures are task-level, not person-level:

- Was the pinned revision readable?
- Was an applicable calibration pair available?
- Did the output preserve supplied facts and non-negotiable wording?
- Did the same gap recur on the next comparable task?
- Did the change remove repeated instructions or review comments?

These are diagnostic questions, not a compliance score. Report absence honestly; do not turn unknown coverage into a pass.

## What must not become recursive

- Do not promote frequently used words, accepted drafts, reactions, or model outputs into guidance automatically.
- Do not infer team policy from one person's edit or approval of one artifact.
- Do not rank, score, or profile individual writers.
- Do not copy private usage reports or work artifacts into a public Chalkline repository.
- Do not let a language system approve its own changes or bump its own consumers.
- Do not treat lack of reported gaps as proof that coverage is complete.

The recursive unit is **a reviewed diff with a reproduction**, not an agent memory, an engagement metric, or an accepted sentence.

## Upstream and local learning

A team's language repository learns about that team's language. The upstream Chalkline project learns about the setup and operating protocol.

- Send **local language gaps** to the people responsible for that language system.
- Send **repeatable protocol failures** upstream using the setup-experience issue form, with fictional or redacted evidence.
- Keep product facts, approvals, delivery state, and outcomes in the systems that own them; link them when appropriate rather than copying them into language guidance.

Upstream should change only when a public-safe reproduction shows a repeatable failure or an independent implementation proves a useful convention. One surprising output is a case to investigate, not a standard to ship.
