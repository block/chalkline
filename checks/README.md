# checks/

Conformance checks for the teaching-loop contract in AGENTS.md — dependency-free, no build step, honest about being heuristics.

```bash
node checks/check-transcripts.mjs                    # run all fixtures
node checks/check-transcripts.mjs my-transcript.md   # check one reply ad hoc
```

## What gets checked

Against **reply transcripts** (real fresh-context agent sessions, kept in `fixtures/`):

1. **copy-leak** — teach-back phrasing never appears inside quoted copy blocks (`>` lines, `**Title/Body/Subject**` lines). The worst violation: pedagogy shipping to someone's customer.
2. **cap** — at most one teach-back gloss per reply.
3. **citation** — a gloss must credit `vocabulary.md`, and must never be attributed to `terminology.md` on the same line.
4. **opening-rename** — the reply must not lead with a gloss (first ~40 characters); teaching comes in passing, after fulfillment.

Against **vocabulary files**: the boundary sentence ("governs conversation, not output"), the `teaching:` flag, a three-column table, a provenance footer, and a named approver.

## How fixtures work

`fixtures/expectations.json` declares intent per transcript: expected gloss count, plus `knownFindings` for **negative fixtures** — transcripts kept precisely because they violate the contract. The suite fails if a negative fixture *stops* tripping its check: that means the check lost its teeth, not that the fixture got better. (`pre-hardening-miscitation.md` is the reply that attributed a vocabulary mapping to `terminology.md` before the contract required citations — the bug that motivated the rule.)

## What this deliberately is not

A language parser. The patterns are grep-grade on purpose — cheap, portable, and aimed at the worst violations. A clever reply can fool them; a reviewed fixture set keeps them honest. Add a fixture with every contract change: the transcripts are the spec's test suite, the same way `calibration/` pairs are a voice's test suite.
