# chalkline

**Snap a line before your agents build.**

chalkline sets up a writing system your agents can actually use — in one conversation. A chalk line is the first tool on a build site: snap it once, and every cut after lands straight. This is that, for your team's language.

## The problem

Your agents write now — support replies, product copy, lifecycle email, release notes. What they know about *your* voice is whatever happened to be in the prompt. Style guides live in PDFs and wikis that no tool consults. Teams that skip setup blame the tools for output that was never given the chance to be right.

## What this is

A template repository plus a conversational setup protocol. Open your copy in any capable agent (goose, Claude Code, Codex, or another AGENTS.md-aware harness) and say:

> **"Set up my writing system."**

The agent interviews you, optionally learns from material you already have (style guides, past campaigns, app strings), and generates a small set of reference files — **your** voice, **your** terms, **your** rules — that any agent can consult from then on. Setup ends with proof: your own copy rewritten with and without the system, and the approved pair saved as your first calibration check.

No CLI to install. No schema to learn. No rules to hand-write unless you want to.

## What you get

```text
your-repo/
├── AGENTS.md              # how agents consult your writing system
├── references/
│   ├── voice.md           # how you sound, with real examples
│   ├── terminology.md     # words you use, words you ban
│   └── channels.md        # per-channel rules (only if you need them)
└── calibration/
    └── 001-….md           # approved before/after pairs: regression checks + few-shot examples
```

Two to four small files plus a calibration pair, not a hundred. You own the repo. Every rule in it was approved by you — and every file says so, with a provenance line stamped by setup. Grow it when reality demands, not before.

## Quick start

1. **Use this template** (GitHub → "Use this template") or clone it.
2. Open the repo in your agent.
3. Say **"set up my writing system."**
4. Answer the questions. Paste in anything useful when asked. Approve what the agent extracts.
5. Watch the before/after demo on your own copy — approve it, and it becomes your first calibration pair.
6. Commit.

Designed to finish in one sitting. (We're measuring real setup times now — field reports welcome in the [setup-experience issues](https://github.com/block/chalkline/issues?q=label%3Asetup-experience).)

## After setup

- Any agent that opens the repo consults your references before writing — and asks instead of guessing when your rules don't cover something.
- Legally fixed wording sits under **"Exact wording"** headings that agents reproduce byte-for-byte, never paraphrase.
- Switched models or harnesses? Re-run a calibration pair. If the rewrite drifts from what you approved, your references need attention — and you find out before your customers do.
- Point an MCP writing server or skill at `references/` for retrieval across tools.
- Re-run setup any time to revise. Approved rules only change when you change them; calibration pairs are append-only.

## Design principles

1. **Minimal by default.** A few small files beat an empire of guidelines. Complexity is added by users, when they need it — never shipped.
2. **Your rules, your words.** The agent drafts; you approve. Nothing enters your system unreviewed — and every file carries its provenance.
3. **Prove it immediately.** Setup ends with your own copy rewritten with and without your system. The approved pair stays as a standing regression check.
4. **Honest agents.** No invented rules, no silently resolved conflicts, no paraphrased legal wording. When the system doesn't know, it says so and asks.
5. **Plain files, no lock-in.** Markdown with light frontmatter. Readable by humans, consumable by any tool, portable forever.

## An experiment, in the open

chalkline is more than a onboarding convenience — it's an experiment in **how language spreads into organizational infrastructure**. The conventions this template ships (authority frontmatter, consult-order routing, exact-wording preservation, calibration pairs, provenance footers) are small, adoptable versions of ideas that larger language-governance systems need. We're testing whether they spread the way markdown and robots.txt did: by being copied, not by being specified.

Two commitments, stated plainly:

- **This stays open source.** Apache-2.0 with DCO sign-off means contributors keep their copyright — the license on what you've contributed and copied can't be pulled out from under you.
- **Openness doesn't depend on our roadmap.** If Block's investment here ever ends, an archived template keeps working for everyone who used it. Your repo is yours; nothing phones home.

See [ROADMAP.md](ROADMAP.md) for what we're testing next and what evidence gates each step.

## Related projects

[ai-rules](https://github.com/block/ai-rules) **distributes** rules that already exist — one source of coding guidelines fanned out to eleven agents' file formats. chalkline **elicits** rules that don't exist yet — a conversation that produces your first references. They share the same conventions (markdown rules, light frontmatter, AGENTS.md routing) and compose naturally: ai-rules can distribute what chalkline generates, and an MCP writing server can serve it.

## What this is not

- Not a style guide — it ships no opinions about how *you* should sound.
- Not a grammar checker or writing model.
- Not a compliance tool. It records your judgment; it doesn't supply it.

## Contributing

The protocol improves through setup experiences: where people stalled, what questions confused, what the generated files missed. See [CONTRIBUTING.md](CONTRIBUTING.md).

Licensed under [Apache-2.0](LICENSE) · Governance: [GOVERNANCE.md](GOVERNANCE.md)
