# AGENTS.md — chalkline

This repository holds (or will hold) this team's writing system: voice, terminology, and channel rules that agents consult before writing anything on the team's behalf.

## If `references/` has content: consult before writing

1. Read `references/terminology.md` for banned and preferred terms — these are non-negotiable when marked `enforcement: must`.
2. Read `references/voice.md` for tone, register, and calibrating examples.
3. Read `references/channels.md` (if present) for the channel you're writing for.
4. Match the examples, not just the adjectives. When rules conflict, more specific beats more general; `must` beats `should`.
5. Never present output as "on brand" if you could not read the references.

## If the user asks to "set up my writing system" (or `references/` is empty): run the setup protocol

Follow `setup/PROTOCOL.md` exactly. Summary of the contract:

- **Interview first** — short questions, one at a time. No jargon ("enforcement taxonomy" is not a question a person should meet during setup).
- **Ingest what exists** — offer to extract candidate rules from style guides, past copy, campaign examples, or app strings the user provides. Every extracted rule is shown to the user and only kept if approved.
- **Generate minimally** — 2–4 small files. Do not create a file the interview didn't justify. Do not invent rules the user didn't state or approve.
- **Prove it** — finish with a before/after rewrite of the user's own sample copy, with and without the new references. Show the diff.
- **The user owns the result** — plain markdown, light frontmatter, no lock-in.

## Frontmatter contract for generated files

Every file in `references/` carries exactly this frontmatter:

```yaml
---
title: "Voice"            # human name for the file
brand: "acme"             # the user's brand slug, set once during setup
domain: "shared"          # shared | product | marketing | support
enforcement: "should"     # must (non-negotiable) | should (default) | may (suggestion)
---
```

Default everything to `should`. Only mark `must` when the user explicitly says a rule is non-negotiable (legal wording, banned terms, trademark usage). This keeps the files compatible with MCP writing servers and skills without asking the user to learn a schema.

## What agents must not do in this repo

- Don't add rules, files, or structure beyond what setup produced and the user approved.
- Don't rewrite the user's approved rules when regenerating — propose diffs.
- Don't copy rules in from other companies' style guides unless the user pastes them in themselves.
- Don't treat this repo as a compliance authority. It records the team's judgment; escalation for legal/regulatory language goes to humans.
