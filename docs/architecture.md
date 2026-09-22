# Architecture

Chalkline starts as approved Markdown references and examples read by an agent. A search service, database, hosted application, or integration is not required. This document explains optional growth; it does not add language rules or approval roles.

## Separate the responsibilities

```text
People approve scoped guidance
             |
             v
Canonical references + approved calibration pairs
             |
             v
Optional checks, indexes, search, and generated views
             |
             v
Local drafting or a reviewed consumer-local snapshot
             |
             v
Candidate copy + gaps + sources -> appropriate human review
```

| Layer | Responsibility | Does not establish |
| --- | --- | --- |
| References | Record approved terms, voice, scope, examples, and enforcement | Product facts or authority outside the approving person's scope |
| Calibration | Show reusable direction for an explicit task scope | A rule change or approval of a future artifact |
| Loading and retrieval | Find and return source material with its identity and context | Applicability, complete coverage, or permission to publish |
| Checks | Report the specific structural or behavioral properties tested | General language quality or compliance |
| Adapters | Carry task context and present results without changing their meaning | New rules, exceptions, or approval thresholds |
| Review | Decide within the reviewer's stated remit | Authority over unrelated teams, locales, or disciplines |

The existing contracts in [AGENTS.md](../AGENTS.md), [PINNING.md](../PINNING.md), and [LEARNING.md](../LEARNING.md) govern these boundaries.

## Canonical sources and generated views

Edit the owned reference, then regenerate its views. An index, extracted term list, or rendered site is a view of a particular source revision, not a second place to maintain rules. Preserve source paths, scope, enforcement, and enough surrounding text to interpret an excerpt. A document-level default must not erase an inline `must` rule.

A generated view should identify its inputs and generation method. A freshness check can rebuild it and compare the result with the stored view. Equality demonstrates reproducibility for those inputs; it does not prove that the sources are correct, authorized, or complete. Treat parse failures as visible errors, not permission to substitute weaker defaults.

Keep generated outputs distinguishable from authored references so a loader does not ingest them again as independent evidence. A reviewed consumer snapshot is also derived data, but updating it requires the separate verification and deployment decisions in [PINNING.md](../PINNING.md).

## Retrieval is not approval

Search ranking measures a match to a query. It does not resolve a conflict or turn a likely match into an applicable rule. Read the source and its scope. A top result can omit a relevant exception; an empty result can reflect missing coverage, a narrow filter, or a retrieval failure.

Report these states separately:

- applicable material found and read;
- no applicable coverage found;
- material unavailable or unreadable;
- unresolved conflict;
- a named check completed with no findings in its tested scope.

**No coverage is not a pass.** Neither a clean structural check nor an agent's usage report is approval of copy. Language guidance cannot supply missing product facts or change the strength of supplied facts.

## Ownership and conflicts

Nesting files makes them easier to locate; it grants no authority. Scope and the existing precedence contract govern applicability. Directory depth, search score, modification date, and generated IDs do not break ties. When precedence does not settle a conflict, stop and ask the responsible people.

Cross-team guidance needs named affected groups, an approving role with a stated mandate, preserved valid variation, and an exception or appeal route. Shared wording cannot override applicable legal, accessibility, or localization authority. Exact wording retains its source, locale, audience, and required owner review.

## Optional implementation

The Python 3 standard-library helper, `tools/corpus.py`, provides `check`, `index`, and `search`. Consult `python3 tools/corpus.py --help` for the supported interface. These are corpus utilities, not approval or deployment services.

See [Growing a writing system](growing-a-writing-system.md) for adoption choices and [Integrations](integrations.md) for adapter boundaries.
