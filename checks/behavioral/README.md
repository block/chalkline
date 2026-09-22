# Manual synthetic behavioral fixtures

Four portable cases for a human-run check of Chalkline's drafting contract. These
are new synthetic inputs, not receipts from executed model runs, a benchmark,
automatic enforcement, or a reproduction of every historical red-team condition.
They require no external service, source checkout, credentials, or network access.
Use a locally available model/harness if an entirely offline run is required.

| Case | Drafter task | Reviewer material |
| --- | --- | --- |
| Fact strength | `drafter-input/01-fact-strength.md` | `reviewer-only/01-fact-strength.md` |
| Enforcement and specificity | `drafter-input/02-rule-precedence.md` | `reviewer-only/02-rule-precedence.md` |
| Missing attestation | `drafter-input/03-missing-attestation/TASK.md` plus its two local data files | `reviewer-only/03-missing-attestation.md` |
| Missing coverage | `drafter-input/04-missing-coverage.md` | `reviewer-only/04-missing-coverage.md` |

## Prepare before running

1. A human selects the exact baseline and candidate protocol revisions. Copy the
   relevant local drafting contract from that revision's `AGENTS.md` into the
   harness's instruction surface, including factual boundaries, rule precedence,
   coverage, and consumer snapshot requirements. Preserve the exact supplied text
   and its source revision. If using an excerpt rather than the entire file,
   record the excerpt and selection; results apply to that excerpt, not repository
   auto-discovery. Do not let an empty-template setup interview replace the task.
   For a repository-discovery test, instead stage the revision's instructions and
   needed local files and capture their full inventory; report this as a different
   harness condition. Never load external instruction graphs.
2. Predeclare cases, number of repetitions, order, unchanged control, primary
   failures, and regression checks. Reviewer criteria define failures, not exact
   answer strings. Use the same case inputs for baseline and candidate; change only
   the intended protocol factor. Run a repeated unchanged baseline control under
   the same settings to expose ordinary output variation. If there is no candidate
   change, label the work baseline-only; do not infer improvement.
3. Create a fresh scratch directory **outside this checkout** for each run. Stage
   only the selected protocol and one case's drafter input. For case 03, copy the
   directory contents including hidden `.language/` while preserving relative
   paths; it is a synthetic consumer, not a real source integration. For the other
   cases the references and calibration inventory are embedded in the input.
4. Keep this README, `reviewer-only/`, other cases, prior outputs, review notes,
   approved target answers, and red-team outcomes outside the tested agent's
   context and readable filesystem. A prompt saying “do not read” is insufficient
   isolation for a tool-capable agent. Use a sandbox allowlist, or a text-only
   harness with no filesystem tools. In text-only mode supply case 03's exact data
   bytes with their relative path labels; record that packaging difference.
5. Start a clean context per case, arm, and repetition: no previous conversation,
   remembered project rules, cached review material, or prior answer. Disable
   unrelated integrations and network access. Capture unavoidable global/system
   instructions and limitations, redacting secrets; unknown instructions or model
   settings are limitations, not inferred defaults. Do not fetch the fictional
   source identifiers or replace the deliberately incomplete consumer record.

## Run and capture

Submit the exact task and staged guidance without reviewer criteria or expected
answers. Do not coach or retry selectively after a failure. Preserve every
predeclared run, including errors and refusals. Follow-up turns, if allowed, must
be predeclared and captured. Keep run artifacts outside this fixture directory;
no runner, score generator, or results are shipped here.

A run record should include:

```text
Case / arm (baseline, candidate, unchanged control) / repetition:
UTC time and predeclared sample count/order:
Protocol source revision and exact staged instructions (or attached bytes):
Fixture revision and exact input bytes / relative file paths / hashes:
Intended changed factor; unchanged-control definition:
Model provider, exact model ID/version (not just “default”):
Harness name/version; OS/runtime where relevant:
Settings: temperature, top-p, seed, token limits, reasoning mode, other flags:
Unavailable settings or hidden instructions:
Tools, permissions, network state, sandbox and memory configuration:
Exact messages in order, role labels, invocation/configuration:
Raw output, tool calls/results, errors, termination and truncation:
Reviewer, criteria revision, quoted evidence and per-criterion judgment:
Outcome: pass / fail / inconclusive / not run:
Missing evidence, regression observations, and review effort:
```

Store the actual bytes/transcript, not only hashes or the agent's usage summary.
Exact settings improve reproducibility but cannot guarantee deterministic output.

## Review separately

After generation, give a separate reviewer the matching reviewer-only file, raw
output, task, protocol, and available trace. Never feed that material back into
an arm being tested. Review factual strength, precedence, missing coverage, and
access behavior directly; the tested agent's claim that it followed guidance is
not proof. Without a trace, mark unobservable tool behavior unknown. Incomplete,
truncated, contaminated, or mismatched runs are inconclusive, not passes.

Report baseline, candidate, and control results with the predeclared denominator,
negative results, missing observations, and limitations. These four cases do not
establish reliability rates, cross-model parity, organizational approval, security
isolation, or deployment safety. No outputs automatically become language rules,
calibration pairs, source attestations, or deployment approvals. Human owners make
those decisions separately. Real consumer changes still need held-out comparable
work in the actual consuming harness and independently reviewed source records;
this fictional local consumer cannot establish upstream source verification.

The historical receipt in `../RED-TEAM-2026-07-30.md` describes its own past runs.
Adding these files makes no new executed-model claim. Static file or repository
checks are not behavioral evidence.
