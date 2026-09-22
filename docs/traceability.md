# Traceability and task confidence

Every drafting or review task using Chalkline must include a compact usage receipt, even when blocked. Put it after or alongside the deliverable, clearly separated from copy. A chat block is enough: no additional setup interview, compulsory per-task file, telemetry service, or new reference metadata is required.

The receipt is a self-report of consultation and checks, not independent attestation, proof of compliance, or evidence that an agent obeyed instructions. Its confidence score describes support for this task—not model probability, writing quality, a writer's ability, or permission to publish. No percentages or personal telemetry. Do not record or score anyone's vocabulary habits.

## Required receipt fields

Use short lines; write `none` or `unknown` explicitly rather than omitting a field.

- **Scope:** task, artifact or version assessed, audience/channel, and exclusions. Assess the delivered artifact; for blocked work, assess the requested task. Do not silently narrow scope to improve a score.
- **Sources:** source identity and revision when established, or explicitly `uncommitted` / `unknown`. A base commit does not identify modified working-tree content: label it as a base and mark uncommitted changes. List exact consulted local paths and relevant headings or rule IDs; identify non-file task evidence by its supplied message, document section, or stable locator. List unread or unavailable sources as missing, not consulted. Include a content hash only when actually computed, with algorithm and exact file or byte scope. Label supplied revision/digest records as supplied, not independently verified. Never invent a revision, digest, consultation, approval, or provenance.
- **Findings and basis:** link each material finding or recommendation to **factual evidence** and/or **language rules**, labeled separately. A language rule does not substantiate a product fact. If no basis exists, say `unsupported`; distinguish supplied claims from checked facts. Identify applicable exact wording and whether it was checked byte-for-byte, preserved without a check, or left untouched. Do not reproduce private evidence unnecessarily.
- **Missing evidence:** unavailable required sources, optional coverage gaps, or omitted checks, with their effect on the task.
- **Unresolved:** facts, applicable `must` requirements, conflicts, and questions still needing a decision. Do not silently choose a conflicting rule.
- **Confidence:** each dimension below with score or justified N/A and a concrete basis; the overall score and limiting reason.
- **Required review:** the responsible role and decision/input needed before proceeding or use; if the owner is unknown, say so. **Reviewer approval is separate:** default `not recorded`; record only an actual supplied decision with scope and source. A score never supplies approval or waives required review.

## Canonical ordinal rubric

Score each dimension by the highest level whose conditions are all supported by recorded evidence. Do not infer checks from a polished result. Apply blockers first.

| Level | Guidance coverage | Factual support | Verification |
|---|---|---|---|
| **0 — blocked** | An applicable `must` is unresolved, guidance conflicts remain unresolved, or required guidance cannot be read. | A required factual source is missing, a necessary fact remains unsupported, or factual sources conflict without resolution. | A check required to proceed is unavailable, incomplete, or failing. |
| **1 — limited** | Required guidance is available, but relevant nonblocking coverage is partial or missing (such as no applicable calibration pair). | Retained claims have identifiable supplied support, but its authority or applicability is not established; no required fact/source is missing. | Only an informal reread or incomplete non-required checks are recorded; no required check is missing or failing. |
| **2 — supported** | Applicable approved guidance covers the declared scope; its authority and applicability are identified, with no unresolved requirements or conflicts. | Every retained factual claim is traceable to an identified source authoritative for that claim and applicable to this task. | Explicit task-relevant checks were executed against the assessed artifact, with methods, results, and limits recorded; required checks pass. |
| **3 — corroborated** | Level 2 plus a separate recorded scope/coverage review or held-out check supports application to this task. | Level 2 plus independent corroboration or an authoritative owner's recorded confirmation of the retained facts for this task. | Level 2 plus an independent check or reviewer independently repeats the relevant checks on this artifact and records the result. |

**Aggregation and blockers:**

1. Any unresolved applicable `must`, unresolved conflict, or missing required source forces overall **0**, even if another dimension is N/A. Stop affected work and request resolution; label any safe partial artifact and its exclusions. A receipt may report a blocker without producing a draft.
2. Otherwise take the **minimum numeric score** of applicable dimensions. Never average, round up, add points, or infer corroboration from repeated self-report. Evidence for one dimension does not automatically support another.
3. **N/A requires a reason tied to scope**, such as factual support for a purely typographic task with no factual assertions or changes. Missing evidence or an unperformed check is not N/A. Exclude justified N/A from the minimum without substituting a 3; show it visibly so the narrower assessment is not mistaken for broader confidence. Verification applies to every draft/review; if all dimensions were marked N/A, the receipt is invalid and must be corrected before a score is issued.
4. A missing optional example can limit coverage to 1; it is not automatically a blocker. A missing required reference always blocks. Explicitly distinguish these cases.
5. Never alter a fact's original certainty to fit a score: “will” must not become “may” because support is limited. Ask, omit an unsupported claim with the omission disclosed, or stop; do not manufacture certainty either. After an authorized scope change or resolution, reassess the actual artifact and record what changed.

Approval is not a fourth dimension. An approval may supply evidence only for the check or factual confirmation it actually records; generic approval does not make every dimension 3. A 3 still does not establish legal, accessibility, localization, production, or publication approval.

## Compact receipt template

```text
Usage receipt (self-report; separate from copy)
Scope: [artifact/version, task, audience/channel; exclusions]
Sources: [identity, revision or uncommitted/unknown; exact consulted paths/locators]
Findings: [finding -> factual evidence: locator; language rule: path#heading]
Missing evidence: [none or source/check, required/optional, effect]
Unresolved: [none or facts/musts/conflicts/questions]
Confidence: guidance [0–3/N/A + basis]; facts [0–3/N/A + basis]; verification [0–3 + checks/results/limits]
Overall: [lowest score; limiting reason or blocker]
Required review: [role + decision/input; unknown owner if needed]
Reviewer approval: [not recorded, or supplied decision + scope + source]
```

Only add a hash line if a hash was actually computed. Do not paste this template into customer copy or imply its placeholders are real evidence.

## Cheap consistency checks

These are expected outcomes, not executed behavioral evidence. Use synthetic tasks in two harnesses with the same inputs; retain the receipts separately from copy and compare them against these criteria. Human review remains necessary to judge the evidence.

| Case | Required outcome |
|---|---|
| Required terminology file unread; other dimensions supported | Overall 0; missing source disclosed; no invented consultation. |
| Guidance 2, supplied but unconfirmed facts 1, verification 2 | Overall 1; factual certainty preserved; required review named. |
| Typographic task: guidance 2, facts N/A with scoped reason, verification 2 | Overall 2 with visible N/A; no claim of factual verification. |
| Guidance 3, facts 2, verification 1 | Overall 1; no average or percentage. |
| Applicable must or source conflict unresolved despite reviewer praise | Overall 0; praise does not resolve or waive the blocker. |
| Modified local files and a known base commit; no hashes computed | Uncommitted state and exact consulted paths; base labeled; no invented digest. |
| All dimensions 3 but publication approval absent | Overall 3; approval remains not recorded and required review remains visible. |

Failure means the receipt hides a gap, invents provenance, inflates confidence, changes factual certainty, or merges assessment with approval. Compare against an unchanged control before claiming this contract improves model behavior. The operating cost is a short receipt and three grounded judgments; do not add a service or maintained fields until a real integration or observed failure requires them.
