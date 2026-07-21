# Contributing

This project improves through **setup experiences**, not style opinions.

## What we want

- **Field reports:** where the interview stalled, what question confused you, how long setup took, what the generated files missed. Open an issue with the `setup-experience` label.
- **Protocol improvements:** changes to `setup/PROTOCOL.md` that fix an observed failure. Link the experience that motivated it.
- **Harness reports:** does the protocol behave the same in goose, Claude Code, Codex, and other AGENTS.md-aware agents? Divergence reports are gold.
- **Example corpora:** fictional or explicitly publishable setups under `examples/` that show the output shape for a kind of team we don't cover.

## What we don't want

- Opinions about how companies *should* sound. This tool ships no voice.
- Rules copied from real companies' style guides without permission.
- Complexity. A change that adds a file, a required question, or a concept to the default path needs to point at a real failure it fixes. The first version of this idea died of complexity once; see the design principles in the README.

## Ground rules

- Every PR needs a one-line answer to: *what setup experience does this improve?*
- Protocol changes are reviewed by one content/design maintainer and one technical maintainer.
- Sign your commits (DCO): `git commit -s`.

## Governance

See [GOVERNANCE.md](GOVERNANCE.md).
