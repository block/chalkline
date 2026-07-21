# chalkline

**Snap a line before your agents build.**

chalkline sets up a writing system your agents can actually use — in one conversation. A chalk line is the first tool on a build site: snap it once, and every cut after lands straight. This is that, for your team's language.

Status: experimental · A [Builder Labs](https://github.com/block) project · Apache-2.0

## The problem

Your agents write now — support replies, product copy, lifecycle email, release notes. What they know about *your* voice is whatever happened to be in the prompt. Style guides live in PDFs and wikis that no tool consults. Teams that skip setup blame the tools for output that was never given the chance to be right.

## What this is

A template repository plus a conversational setup protocol. Open your copy in any capable agent (goose, Claude Code, Codex, or another AGENTS.md-aware harness) and say:

> **"Set up my writing system."**

The agent interviews you, optionally learns from material you already have (style guides, past campaigns, app strings), and generates a small set of reference files — **your** voice, **your** terms, **your** rules — that any agent can consult from then on.

No CLI to install. No schema to learn. No rules to hand-write unless you want to.

## What you get

```text
your-repo/
├── AGENTS.md              # how agents consult your writing system
└── references/
    ├── voice.md           # how you sound, with real examples
    ├── terminology.md     # words you use, words you ban
    └── channels.md        # per-channel rules (only if you need them)
```

Two to four small files, not a hundred. You own the repo. Every rule in it was approved by you. Grow it when reality demands, not before.

## Quick start

1. **Use this template** (GitHub → "Use this template") or clone it.
2. Open the repo in your agent.
3. Say **"set up my writing system."**
4. Answer the questions. Paste in anything useful when asked. Approve what the agent extracts.
5. Watch the before/after demo on your own copy.
6. Commit.

Typical time: under 30 minutes.

## After setup

- Any agent that opens the repo consults your references before writing.
- Point an MCP writing server or skill at `references/` for retrieval across tools.
- Re-run setup any time to revise; your approvals are preserved as history.

## Design principles

1. **Minimal by default.** A few small files beat an empire of guidelines. Complexity is added by users, when they need it — never shipped.
2. **Your rules, your words.** The agent drafts; you approve. Nothing enters your system unreviewed.
3. **Prove it immediately.** Setup ends with your own copy rewritten with and without your system, so you can see what it's for.
4. **Plain files, no lock-in.** Markdown with light frontmatter. Readable by humans, consumable by any tool, portable forever.

## What this is not

- Not a style guide — it ships no opinions about how *you* should sound.
- Not a grammar checker or writing model.
- Not a compliance tool. It records your judgment; it doesn't supply it.

## Contributing

The protocol improves through setup experiences: where people stalled, what questions confused, what the generated files missed. See [CONTRIBUTING.md](CONTRIBUTING.md).
