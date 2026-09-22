# Growing a writing system

Keep the smallest system that covers the work. The stages below are options, not maturity levels or a required migration plan.

## Start with a flat corpus

Use [setup](../setup/PROTOCOL.md) to agree on a few references and an explicitly approved, scoped calibration pair. Voice and terminology may be enough. Add channel guidance or a conversational vocabulary map only when the interview establishes a need.

Read these files directly. Try a real, repository-safe sample. Record missing facts and coverage rather than filling them with assumed rules. Approving a draft, approving reusable calibration direction, changing a reference, and deploying a consumer snapshot remain separate decisions.

## Add structure when a concrete problem needs it

| Observed problem | Small next step |
| --- | --- |
| People cannot find an existing rule | Improve a title, scope statement, or navigation before adding search |
| One file mixes distinct audiences or domains | Propose a scoped split with explicit ownership |
| Several surfaces duplicate the same reference text | Generate views from one canonical source |
| A consumer uses old or unverified guidance | Review its local snapshot and source record |
| A recurring correction is not covered | Propose a small reference change and held-out test |

Avoid creating empty folders, mandatory metadata, dashboards, or services for hypothetical future needs.

## Move to scoped nested references deliberately

A larger corpus might group references by team or brand, then by domain. This is an illustrative layout, not a new schema:

```text
references/
  voice.md
  terminology.md
  channels.md
  product/
    errors.md
  support/
    replies.md
```

Keep the entry references usable, and explicitly route readers to applicable scoped material. Moving a file should not silently broaden its scope or change its enforcement. Retain the base frontmatter contract in [AGENTS.md](../AGENTS.md); a folder name does not replace declared metadata. Record audience, purpose, ownership, and limits clearly in the prose where the existing format does not have a field.

For each split or move:

1. Name the discovery or ownership problem it fixes.
2. Identify which guidance remains shared and which genuinely differs.
3. Have the responsible people review the scope and any overlap.
4. Update local links, retrieval expectations, and generated views. Path-derived identifiers may change on a move; check consumers rather than assuming identity is preserved.
5. Test both the intended scope and a nearby scope that should remain unchanged.

Do not use nesting to bypass an applicable non-negotiable rule. Unresolved overlaps go back to their owners. If a new routing or metadata convention is needed, propose and approve it explicitly rather than treating this example as authorization.

## Add retrieval or integrations only when useful

Direct reading can remain the entire implementation. The optional `tools/corpus.py` helper offers `check`, `index`, and `search` using Python 3's standard library; use `--help` for its interface. A generated index improves discovery, not authority. A consumer still needs applicable sources and a visible gap when they are missing.

Before connecting another repository, follow [PINNING.md](../PINNING.md). A drafting agent reads the reviewed local snapshot, not a remote instruction repository. Each consumer owns its update and rollback decision.

## Learn through reviewed changes

Use the loop in [LEARNING.md](../LEARNING.md): observe a task-level gap, propose the smallest change, get a scoped decision, test, and deliberately distribute. Do not promote accepted drafts or repeated model outputs into rules automatically.

For a behavioral change, choose comparable samples and failure criteria before testing. Hold the target calibration pair's rewrite, rationale, and lesson out of the tested agent's context. Run an unchanged control and an unseen comparable sample before making a broader improvement claim. Record the reference revision, model, harness, inputs, missing observations, and regressions.

Check factual strength, scope, conflict handling, and review burden as well as the correction you intended. Keep the previous known-good revision and snapshot. A favorable example is useful evidence, but it cannot establish coverage across untested work.

Keep learning records public-safe and purpose-limited. They diagnose the system; they are not individual writer scores or employment telemetry. No one needs to log every interaction to maintain a useful writing system.
