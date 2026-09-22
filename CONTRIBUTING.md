# Contributing

This project improves through **setup experiences**, not style opinions.

## What we want

- **Field reports:** where the interview stalled, what question confused you, how long setup took, what the generated files missed. Open an issue with the `setup-experience` label.
- **Protocol improvements:** changes to `setup/PROTOCOL.md` that fix an observed failure. Link the experience that motivated it and name the reproduction or calibration check that would show the fix worked.
- **Harness reports:** does the protocol behave the same in goose, Claude Code, Codex, and other AGENTS.md-aware agents? Divergence reports are gold.
- **Example corpora:** fictional, redacted, or explicitly publishable setups under `examples/` that show the output shape for a kind of team we don't cover.

## What we don't want

- Opinions about how companies *should* sound. This tool ships no voice.
- Rules copied from real companies' style guides without permission.
- Complexity. A change that adds a file, a required question, or a concept to the default path needs to point at a real failure it fixes. The first version of this idea died of complexity once; see the design principles in the README.

## Ground rules

- This repository and its issues are public. Never submit private writing rules, raw source documents, customer or personal data, confidential material, secrets, or private links. Reproduce failures with fictional or redacted material.
- Submit only material you have permission to publish under this project's license.
- Every PR needs a one-line answer to: *what observed experience does this improve?* Behavior changes also need an executed held-out reproduction and unchanged control with exact versions and failure criteria. A future check is not verification; consequential private failures may use a maintainer-approved evidence exception and the smallest safe synthetic regression.
- Protocol changes are reviewed by one content/design maintainer and one technical maintainer.
- Sign your commits (DCO): `git commit -s`.

## Local development and verification

Ordinary setup still needs no installed tooling. To work on the optional developer tools, use Python 3.9 or newer; no third-party packages or API keys are required.

From the repository root:

```sh
bash checks/adversarial-contract.sh
python3 -m unittest discover -s tests -v
python3 tools/corpus.py --help
```

See [tools/README.md](tools/README.md) for corpus checks and retrieval examples. These checks validate file structure and implementation behavior, not the quality of writing, legitimate approval, or model adherence. The existing shell check only asserts that important contract text is present.

[Behavioral fixtures](checks/behavioral/README.md) provide synthetic inputs and separate reviewer criteria for manual agent tests. Keep reviewer-only material out of the tested session. Record unexecuted cases as unexecuted; unit tests do not substitute for held-out behavioral evidence.

For tooling contributions, include a failing synthetic input and a valid unchanged control, run both, and report exact commands and runtime versions. If a change also affects agent behavior, the held-out requirements above still apply. Do not add private corpora, deployment credentials, or real customer examples to make a test realistic.

## Governance

See [GOVERNANCE.md](GOVERNANCE.md).
