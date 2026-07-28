# Operability

Chalkline sets up a small language system for writing: references agents can read, examples they can calibrate against, and gaps people can improve. This page explains the operating loop after setup.

The goal is not to make the repository an authority over people. The goal is to make language guidance usable, inspectable, and improvable without copying it into every prompt or tool.

## The loop

```text
Set up -> consult -> apply -> report gaps -> revise -> recalibrate
```

1. **Set up:** the team approves a small set of references and one calibration pair.
2. **Consult:** an agent reads the applicable references before writing or reviewing.
3. **Apply:** the agent changes language while preserving supplied facts.
4. **Report gaps:** the agent names missing coverage, conflicts, or exact wording it cannot safely handle.
5. **Revise:** a person proposes reference changes; approved rules are changed by diff, not silently rewritten.
6. **Recalibrate:** the team adds or re-runs calibration pairs when voice, model behavior, or harness behavior changes.

## What an agent should report

When an agent uses a Chalkline repository for real work, it should be able to say:

- which repository and revision it used, if the revision is available;
- which reference files and calibration pair it read;
- which `must` rules applied;
- which exact wording blocks were preserved or left untouched;
- which facts came from the user's request rather than the writing system;
- which relevant guidance was missing, unavailable, or in conflict;
- what needs a person before the work is treated as approved.

Short version:

```text
Used: references/voice.md, references/terminology.md, calibration/002-...
Applied: 2 must rules, 4 should rules
Preserved: exact wording in terminology.md
Gaps: no support-channel rule for refunds
Human needed: approve whether "refund pending" is a supported product state
```

No finding is not the same as complete coverage. If an agent could not read a needed source, it should say so instead of treating silence as approval.

## How gaps become better rules

A gap is useful evidence. Treat it as a proposed improvement, not as permission for the agent to invent policy.

Good gap report:

```text
The references do not say whether support replies should name back-office queue states. I avoided that term and used the customer-visible state instead.
```

Good follow-up:

```text
Add a support-channel rule: "Use customer-visible states. Do not name back-office queue states unless support policy says to."
```

The person maintaining the Chalkline repo decides whether that rule belongs in `references/channels.md`, `references/terminology.md`, a new calibration pair, or nowhere.

## Calibration as an operating check

Calibration pairs are both examples and checks.

Use them when:

- setup finishes;
- a team changes a major rule;
- an agent model or harness changes;
- output starts to feel off but the references look unchanged;
- a new channel or audience is added.

The check is deliberately manual:

1. Give an agent the original sample and the current references.
2. Ask it to rewrite the sample.
3. Compare the result with the approved direction in the newest calibration pair.
4. If it drifts, decide whether the issue is the model, the harness, the prompt, or a missing rule.
5. Fix the reference gap or append a new calibration pair.

Do not rewrite approved calibration pairs during ordinary revisions. Append a new pair so the history stays visible.

## What Chalkline does not own

Chalkline records approved language guidance. It does not provide:

- legal, compliance, accessibility, or localization approval;
- identity, permission, or separation-of-duties checks;
- publication, rollback, or delivery systems;
- private corpus hosting;
- telemetry about individual writers;
- a guarantee that an agent or harness followed the instructions.

Downstream tools can use Chalkline as a policy source, but they remain responsible for their own authorization, lifecycle, audit, and human-review boundaries.

## Why this scales

Small teams can run the loop in one repository. Larger organizations can run many Chalkline language systems by team, product, brand, or audience, as long as consumers keep the source and revision visible.

The important boundary is simple:

```text
Chalkline records current language guidance for a scoped writing system.
People decide whether to approve, waive, publish, or change it.
Other systems apply and verify it in their own lifecycle.
```
