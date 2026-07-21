# AGENTS.md — chalkline

This repository holds (or will hold) this team's writing system: voice, terminology, and channel rules that agents consult before writing anything on the team's behalf.

## If `references/` has content: consult before writing

1. Read `references/terminology.md` for banned and preferred terms — these are non-negotiable when marked `enforcement: must`.
2. Read `references/voice.md` for tone, register, and calibrating examples.
3. Read `references/vocabulary.md` (if present) to understand requests in the user's own words — it maps how people naturally speak to the team's canonical terms.
4. Read `references/channels.md` (if present) for the channel you're writing for.
5. Read the most recent pair in `calibration/` (if present) — approved rewrites show the voice applied, not just described.
6. Match the examples, not just the adjectives. When rules conflict, more specific beats more general; `must` beats `should`.
7. If precedence doesn't settle a conflict, surface it to the user instead of picking silently — conflicts are bugs in the system, not choices for the agent.
8. If the references don't cover something, say so and ask — never infer a rule that isn't written.
9. Never present output as "on brand" if you could not read the references.

## The reply that teaches

This repo doesn't just constrain writing — it teaches the team's language back to whoever is asking. Two behaviors, both gentle:

- **Teach-back.** When a request used an everyday word that `vocabulary.md` maps to a canonical term, fulfill the request exactly as asked, and name the canonical term **once**, in passing, inside the reply (the table shows the register). Never open by renaming what the person said. Never say they used the "wrong" word — there are no wrong words, only house words worth knowing. One teach-back per reply, maximum; skip it entirely if the person already used the canonical term or has been taught it in this conversation.
- **Plain explanation on request.** If someone asks what this writing system is, how it works, or "explain this to a new teammate," explain it in plain language from the actual files — what each reference does, with one real example from each, and where the rules came from (the provenance footers). No jargon, no schema talk. The system should be able to introduce itself.

What teaching must never become:

- Correcting or grading how a person speaks or writes in conversation.
- Logging, reporting, or tracking anyone's word choices.
- Withholding the requested work until the person adopts the house term.
- More than one lesson per reply. Teaching that interrupts stops being teaching.

## Exact wording blocks

Text under an **"Exact wording"** heading is reproduced byte-for-byte — never paraphrased, truncated, reformatted, or improved, including during structural edits. Changing exact text is a human decision made in the owning source, not an edit here. When the canonical text lives elsewhere (legal, compliance, a disclosures repo), reference it by link rather than pasting a copy that can go stale.

## If the user asks to "set up my writing system" (or `references/` is empty): run the setup protocol

Follow `setup/PROTOCOL.md` exactly. Summary of the contract:

- **Interview first** — short questions, one at a time. No jargon ("enforcement taxonomy" is not a question a person should meet during setup).
- **Ingest what exists** — offer to extract candidate rules from style guides, past copy, campaign examples, or app strings the user provides. Every extracted rule is shown to the user and only kept if approved.
- **Generate minimally** — 2–4 small files. Do not create a file the interview didn't justify. Do not invent rules the user didn't state or approve. Every generated file ends with a one-line provenance footer.
- **Prove it** — finish with a before/after rewrite of the user's own sample copy, with and without the new references. Show the diff, then save it as the first pair in `calibration/`.
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
- Don't modify text inside "Exact wording" blocks — byte-for-byte reproduction only.
- Don't rewrite approved calibration pairs — append new ones.
- Don't copy rules in from other companies' style guides unless the user pastes them in themselves.
- Don't treat this repo as a compliance authority. It records the team's judgment; escalation for legal/regulatory language goes to humans.
