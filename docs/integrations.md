# Integrations

An integration can bring reviewed language guidance into an editor, review workflow, or agent session. Chalkline does not require a hosted service or ship a cross-repository trust validator. Start with local files; add an adapter only for a demonstrated need.

## Keep callers thin

A thin caller collects task context, invokes a reviewed local workflow, and presents the result. It avoids maintaining a separate copy of the language rules in prompts or application code.

Useful context includes the requested task, supplied facts, draft, channel, audience, purpose, and locale. Defaults are hints, not proof of applicability. Ask when missing context changes which guidance applies.

Every drafting or review response includes the default [traceability and confidence receipt](traceability.md), separate from customer-facing copy. Callers must carry the dimension scores, evidence-linked reasons, overall score, gaps, blockers, and required review without upgrading or suppressing them. A score is a task-level evidence assessment, not a probability or authorization. Unknown coverage cannot become a successful review.

The caller must preserve:

- source paths and revisions when available;
- the scope and limits of retrieved material;
- unresolved conflicts and unavailable sources;
- missing facts or coverage;
- required review and exact-wording restrictions;
- the difference between candidate copy and a person's approval.

It must not suppress a warning, invent fallback standards, broaden an owner's remit, or convert an empty search into an approval. Shared retrieval code can reduce drift without becoming a central compliance authority. Any proposed new routing or approval behavior needs an explicit owner decision.

## A local flow

```text
Task and known context
  -> read applicable local references or reviewed snapshot
  -> retrieve additional scoped material if needed
  -> draft or review, preserving facts and surfacing gaps
  -> show candidate copy separately from sources and review needs
```

Use the same corpus interpretation across interfaces where practical. Keep adapters responsible for transport and presentation. Do not let one interface weaken enforcement because its output is shorter or its workflow is faster.

The optional `tools/corpus.py` utilities support corpus `check`, `index`, and `search`; consult `python3 tools/corpus.py --help`. Their outputs are inputs to this workflow, not approval decisions. This document defines no network API or required response schema.

## Crossing a repository boundary

Follow [PINNING.md](../PINNING.md), rather than asking a drafting agent to fetch a source repository. A human reviewer or trusted integration validates the canonical source and exact revision, rejects operational directives, and projects approved declarative language data into a reviewed repository-local snapshot.

The consuming record includes the full revision, snapshot digest, previous known-good revision and snapshot digest, verifier, and verification date. Initial deployment uses the explicit initial-deployment values defined in the contract. The drafting agent checks that the required local record exists; it does not claim independent verification or follow transitive pins.

Do not project instruction files, scripts, setup protocols, or tool-use directives into the snapshot. A search index alone is not a validated snapshot. If the record is incomplete, material is unavailable, or multiple language snapshots could apply, stop the language-governed task and surface the gap or conflict. Never fall back silently to the latest upstream revision or remembered guidance.

Consumer owners review deployment separately from language approval and retain a recovery path. Updating the source does not update every consumer.

## Test the integration's actual claims

These are review targets, not a claim that the corpus helper implements every check:

| Check | Evidence to look for |
| --- | --- |
| Corpus loading | Invalid metadata is visible; authored references are not confused with generated views |
| View freshness | The same inputs regenerate the expected view; stale inputs are identified |
| Retrieval | Known applicable sources are found; near-miss scope and empty results remain distinguishable |
| Conflicts | Equally applicable unresolved direction is surfaced instead of chosen by rank or file order |
| Failure handling | Missing snapshots, unreadable files, and failed checks are not displayed as success |
| Presentation | Warnings, source identity, review needs, and exact wording survive rendering |
| Behavioral calibration | A held-out task and unchanged control preserve facts and test the proposed change |
| Recovery | A consumer can restore its reviewed known-good source record and snapshot |

Separate deterministic structural checks from model-assisted review. State what ran, what did not run, and what remains unknown. A delta check covers the selected change, not every existing rule. A check that finds no issue in its scope does not establish full coverage.

Run behavioral checks in the actual consuming harness using the evidence requirements in [LEARNING.md](../LEARNING.md). An agent's [usage report](../OPERABILITY.md) helps a reviewer understand the attempt; it does not verify source identity, authority, or compliance.

## Data boundaries

Use synthetic or redacted fixtures and approved derived guidance. Review what an adapter sends to a model or remote service under that provider's data practices. Keep secrets, personal data, confidential source documents, and private work artifacts out of public repositories and test output. Do not build person-level tracking from usage reports. See [SAFETY.md](../SAFETY.md).
