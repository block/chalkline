# chalkline

**A writing system your team owns and your agents can consult.**

Chalkline helps a team turn its approved voice, terminology, vocabulary, and channel rules into plain reference files. Start with a short setup conversation. Add discovery, checks, and integrations only when the work needs them.

This open-source project shares reusable methods for maintaining language guidance, not a company's private style guide. It ships fictional examples, a setup protocol, and optional local tools. Your team supplies its own rules and decides who can approve them.

## Status

Experimental protocol and template. Local structural checks and synthetic regressions run in CI; they do not verify writing quality or model adherence. Cross-harness setup parity, real-team setup burden, and ingest limits still need field validation. Cross-repository snapshot projection is a manual review contract, not bundled enforcement. See [sharing readiness and the next experiments](docs/sharing-readiness.md).

## The problem

Your agents write now — support replies, product copy, lifecycle email, release notes. What they know about *your* voice is whatever happened to be in the prompt — and every new prompt, agent file, and skill restates that voice from memory, drifting a little each time. Style guides live in PDFs and wikis that no tool consults. Teams that skip setup blame the tools for output that was never given the chance to be right.

## What this is

A template repository plus a conversational setup protocol. Open your copy in any capable agent (goose, Codex, Claude Code, or another agent that reads repo instruction files) and say:

> **"Set up my writing system."**

The agent interviews you, optionally learns from material you already have (style guides, past campaigns, app strings), and generates a small set of reference files — **your** voice, **your** terms, **your** rules — that any agent can consult from then on. Setup ends with a visible comparison: your own copy rewritten with and without the system. If you separately approve that direction as reusable for a stated scope, the pair becomes your first few-shot example; it is not a held-out effectiveness test.

Setup needs no CLI installation or schema knowledge. Optional Python tools can check and search your files later; they do not generate rules or approve copy.

## What you get

```text
your-repo/
├── AGENTS.md              # how agents consult your writing system
├── CLAUDE.md              # one-line bridge for agents that read CLAUDE.md instead
├── references/
│   ├── voice.md           # how you sound, with real examples
│   ├── terminology.md     # words you use, words you ban
│   ├── vocabulary.md      # optional: how people ask for your terms in everyday language
│   └── channels.md        # per-channel rules (only if you need them)
└── calibration/
    └── 001-….md           # approved before/after pairs: calibration checks + few-shot examples
```

Two to four small files plus an optional calibration pair, not a hundred. You control the resulting repo and its visibility. Every rule records approval by the setup participant for the repository's stated scope; that provenance does not claim organization-wide authority. Grow it when reality demands, not before.

## Quick start

1. **Use this template** (GitHub → "Use this template") or clone it. Start with a private repository unless every input and output is safe to publish.
2. Open the repo in your agent.
3. Say **"set up my writing system."**
4. Answer the questions. Paste in material you have permission to use; approve what the agent extracts.
5. Watch the before/after demo on your own copy. Approve the artifact and, separately, decide whether its direction should become a reusable, scoped calibration pair.
6. Review the diff, then choose whether to commit it.

Target time: under 30 minutes. We're testing that target through real setup experiences.

The upstream `GOVERNANCE.md`, `CODEOWNERS`, `CONTRIBUTING.md`, and `.github/` settings govern contributions to Chalkline itself. When adopting the template, use the [adoption checklist](docs/adoption-checklist.md) to review or replace those settings for your own repository; preserve applicable license and copyright notices. Using Chalkline does not place your language decisions under Block governance or appoint Chalkline maintainers as your reviewers. Agents should propose these changes, never assign owners or remove notices silently.

Before pasting style guides, customer copy, or other source material, read [Safety and privacy](SAFETY.md). Git history can preserve content after you delete it.

## After setup

- Agents that follow `AGENTS.md` consult your references before writing — and ask instead of guessing when your rules don't cover something.
- Fixed wording sits under scoped **"Exact wording"** headings with its owner, locale/jurisdiction, audience/context, and required review. Agents reproduce it byte-for-byte only when that scope matches; shared wording never overrides applicable legal, accessibility, or localization authority.
- Switched models or harnesses? Run a held-out calibration check: hide the target pair's approved rewrite from the tested agent and add an unseen comparable sample before claiming broader improvement. Drift may reveal a reference gap, target leakage, or a model or harness difference.
- Every draft or review includes a separate compact [usage receipt and confidence assessment](docs/traceability.md): sources, evidence-linked findings, gaps, unresolved facts, and required review. Confidence is 0 blocked, 1 limited, 2 supported, or 3 corroborated—the lowest applicable dimension, not a probability, compliance claim, writer rating, or approval. No extra setup questions or per-task files are required. See [Operability](OPERABILITY.md) for the operating loop. [Learning without self-governance](LEARNING.md) shows how evidence becomes a reviewed change, calibration check, deliberate pin update, and observation — never automatic policy.
- For retrieval across tools, use an adapter that explicitly supports Chalkline’s reference format; see the [integration contract](docs/integrations.md). MCP alone does not guarantee file-format compatibility.
- Re-run setup any time to revise. Approved rules only change when you change them; calibration pairs are append-only.

## When your system grows

Keep the small setup until you have a specific need:

| Need | Next step |
|---|---|
| See a completed small setup | [Fictional Meridian example](examples/meridian/) |
| Several audiences or content types need different guidance | [Growth guide](docs/growing-a-writing-system.md) and [fictional Harbor example](examples/harbor/) |
| Check metadata or find references locally | [Local tools](tools/README.md) — Python 3, no packages, accounts, or API keys |
| Understand the source and generated views | [Architecture](docs/architecture.md) |
| Connect an editor, agent, search service, or docs site | [Integration contract](docs/integrations.md) |
| Propose a reference change from observed work | [Learning loop](LEARNING.md) |

The optional tools check file structure and retrieve candidates. They do not verify approval, resolve conflicting rules, evaluate prose, or establish compliance. An empty corpus or zero search results is a coverage gap, not a pass.

## Point other repos at your system

Your writing system is most useful when the repositories your team actually works in declare it. The [Language-pin trust contract](PINNING.md) records the exact canonical source and full immutable commit, but drafting agents **do not fetch or follow external instruction files**. A human reviewer or trusted integration validates the source and projects only declarative language data into a reviewed, repository-local snapshot.

This hard boundary follows an adversarial result: a tool-capable agent read a sentinel before deciding an upstream directive was out of scope. Prose cannot reliably sandbox other prose once both enter the same model context. Until a consumer has a validator, a human consuming owner copies reviewed language data into a local snapshot, records source/revision/digest/previous version plus their verification attestation, and reviews each update by diff. Drafting agents check that this local record exists; they never fetch upstream or pretend to verify it themselves.

## Design principles

1. **Minimal by default.** A few small files beat an empire of guidelines. Complexity is added by users, when they need it — never shipped.
2. **Your rules, your words.** The agent drafts; you approve. Nothing enters your system unreviewed — and every file carries its provenance.
3. **Make the preference visible immediately.** Setup ends with repository-safe copy rewritten with and without your system. If separately approved as reusable direction, the pair becomes a few-shot example; a held-out sample is required before claiming broader usefulness.
4. **Honest agents.** No invented rules, no silently resolved conflicts, no paraphrased legal wording. When the system doesn't know, it says so and asks.
5. **Plain files, no lock-in.** Markdown with light frontmatter. Readable by humans, consumable by any tool, portable forever.

## Related projects

[ai-rules](https://github.com/block/ai-rules) **distributes** rules that already exist — one source of coding guidelines fanned out to eleven agents' file formats. chalkline **elicits** rules that don't exist yet — a conversation that produces your first references. Both use plain files and agent routing. Distribution or MCP retrieval requires an adapter explicitly tested against Chalkline’s reference format and trust boundaries; no such adapter is bundled here.

## What this is not

- Not a style guide — it ships no opinions about how *you* should sound.
- Not a tool for correcting how teammates speak.
- Not a grammar checker or writing model.
- Not a complete language governance system. Company-scale use still needs representation, locale/accessibility ownership, confidential objections, appeals, risk-tiered review, discovery, and revocation outside Chalkline.
- Not a compliance, authority, or performance-management tool. It records scoped participant decisions; it does not establish mandate, organizational representation, or verified adherence.

## Contributing

The protocol improves through setup experiences: where people stalled, what questions confused, what the generated files missed. See [CONTRIBUTING.md](CONTRIBUTING.md).

Licensed under [Apache-2.0](LICENSE) · Governance: [GOVERNANCE.md](GOVERNANCE.md)
