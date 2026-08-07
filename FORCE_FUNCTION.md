# Language as a force function

A force function is a constraint that produces an outcome regardless of anyone's memory or good intentions. A car that won't move until the seatbelt clicks is a force function. This page explains the sense in which chalkline makes a team's language one, and — just as important — the sense in which it deliberately does not.

The distinction matters most at organization scale, where dozens of agents and hundreds of people write on a company's behalf. Unaligned language stops being a style problem there and becomes a structural one: contradictory product terms, brand drift at machine speed, and legal wording quietly paraphrased in a rewrite nobody reviewed.

## The force is the consult contract, not the content

chalkline aligns *how* a team binds its language. It never dictates *what* the language is.

**Uniform — the mechanism a whole organization can share:**

- Agents consult the references before writing, and say so instead of guessing (`AGENTS.md`).
- `must` beats `should`; more specific beats more general. Precedence is declared, not improvised.
- Text under an **"Exact wording"** heading survives every rewrite byte-for-byte.
- Conflicts and gaps surface to a person; they are never resolved silently.
- An agent may not present output as "on brand" if it could not read the references.
- Every rule carries a provenance line: who approved it, from what, and when.
- Calibration pairs turn the approved voice into a regression check, so drift is caught in review rather than discovered by a customer.

**Local — the content each team keeps sovereign:**

- The voice, the terms, the banned words, the channel rules. chalkline ships none of these and holds no opinion about them.
- Each team fills the same substrate with its own language. A support team and a legal team in the same company can run identical mechanics over entirely different words.

So an organization can standardize *the way language is bound* without standardizing *the language itself*. That is the whole point: alignment of the mechanism, sovereignty over the content.

## Why this is not a one-size-fits-all plan

The tempting mistake at enterprise scale is to answer "align our language" with a mandated agent, a central voice, an enforcement platform, or a taxonomy everyone must adopt. That is the opposite of what works, and chalkline refuses it on purpose:

- **No shipped voice.** The tool never tells you how to sound. If it did, it would be one company's style guide wearing a template's clothes.
- **No mandated agent or runtime.** The contract is plain markdown routed by `AGENTS.md`. Any AGENTS.md-aware tool can honor it; none is required. The mechanism spreads by being small and copyable — the way markdown and robots.txt spread — not by decree.
- **No central authority over people or teams.** chalkline records a team's own approved judgment. It does not grant permissions, prove an agent complied, or override the humans who own the words. See [Operability](OPERABILITY.md) for what it explicitly does not own.
- **No speculative machinery.** Cross-repository precedence, multi-brand configuration, and evaluation runners are not shipped. They are earned by field evidence from real teams, or not built. See [Contributing](CONTRIBUTING.md).

The force function is strong precisely because it is narrow: a shared, inspectable, portable way to make approved language bind — with the words left entirely to the team that has to stand behind them.

## Where this fits

- **[README](README.md)** — what chalkline is and how to set one up.
- **[Operability](OPERABILITY.md)** — the loop that keeps a system useful after setup, and the boundaries of what chalkline owns.
- **This page** — why the result behaves as a force function without becoming a mandate.
