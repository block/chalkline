# chalkline

**Snap a line before your agents build.**

Your team runs on language now: it's how you brief agents, how agents write to your customers, and what your product's words are supposed to mean. chalkline turns the part of that your team can actually agree on — voice, terminology, vocabulary, channel rules — into a small writing system agents consult instead of guess at. A chalk line is the first tool on a build site: snap it once, and every cut after lands straight. This is that, for your team's language.

## The problem

Your agents write now — support replies, product copy, lifecycle email, release notes. What they know about *your* voice is whatever happened to be in the prompt — and every new prompt, agent file, and skill restates that voice from memory, drifting a little each time. Style guides live in PDFs and wikis that no tool consults. Teams that skip setup blame the tools for output that was never given the chance to be right.

## What this is

A template repository plus a conversational setup protocol. Open your copy in any capable agent (goose, Codex, Claude Code, or another agent that reads repo instruction files) and say:

> **"Set up my writing system."**

The agent interviews you, optionally learns from material you already have (style guides, past campaigns, app strings), and generates a small set of reference files — **your** voice, **your** terms, **your** rules — that any agent can consult from then on. Setup ends with a visible comparison: your own copy rewritten with and without the system. If you separately approve that direction as reusable for a stated scope, the pair becomes your first few-shot example; it is not a held-out effectiveness test.

No CLI to install. No schema to learn. No rules to hand-write unless you want to.

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

Before pasting style guides, customer copy, or other source material, read [Safety and privacy](SAFETY.md). Git history can preserve content after you delete it.

## After setup

- Agents that follow `AGENTS.md` consult your references before writing — and ask instead of guessing when your rules don't cover something.
- Fixed wording sits under scoped **"Exact wording"** headings with its owner, locale/jurisdiction, audience/context, and required review. Agents reproduce it byte-for-byte only when that scope matches; shared wording never overrides applicable legal, accessibility, or localization authority.
- Switched models or harnesses? Run a held-out calibration check: hide the target pair's approved rewrite from the tested agent and add an unseen comparable sample before claiming broader improvement. Drift may reveal a reference gap, target leakage, or a model or harness difference.
- See [Operability](OPERABILITY.md) for the loop that keeps the language system useful and the short usage report agents can hand a reviewer. [Learning without self-governance](LEARNING.md) shows how evidence becomes a reviewed change, calibration check, deliberate pin update, and observation — never automatic policy.
- You can point a compatible writing server or skill at `references/` for retrieval across tools.
- Re-run setup any time to revise. Approved rules only change when you change them; calibration pairs are append-only.

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

[ai-rules](https://github.com/block/ai-rules) **distributes** rules that already exist — one source of coding guidelines fanned out to eleven agents' file formats. chalkline **elicits** rules that don't exist yet — a conversation that produces your first references. They share the same conventions (markdown rules, light frontmatter, AGENTS.md routing) and compose naturally: ai-rules can distribute what chalkline generates, and an MCP writing server can serve it.

## What this is not

- Not a style guide — it ships no opinions about how *you* should sound.
- Not a tool for correcting how teammates speak.
- Not a grammar checker or writing model.
- Not a complete language governance system. Company-scale use still needs representation, locale/accessibility ownership, confidential objections, appeals, risk-tiered review, discovery, and revocation outside Chalkline.
- Not a compliance, authority, or performance-management tool. It records scoped participant decisions; it does not establish mandate, organizational representation, or verified adherence.

## Contributing

The protocol improves through setup experiences: where people stalled, what questions confused, what the generated files missed. See [CONTRIBUTING.md](CONTRIBUTING.md).

Licensed under [Apache-2.0](LICENSE) · Governance: [GOVERNANCE.md](GOVERNANCE.md)
