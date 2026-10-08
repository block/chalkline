# Sharing readiness

Chalkline is an experimental protocol and template for team-owned language guidance. Share it as a method to try, not a verified enforcement or compliance system.

## What has evidence

- Python regression tests cover the local corpus parser, filesystem restrictions, output behavior, and receipt structure/arithmetic.
- CI runs contract-text assertions and validates fictional corpora. Text assertions do not execute agent behavior.
- Website tests exercise fixed fictional tasks and blocked/restored states. The site has no live model, uploads, or telemetry.
- [The July red-team receipt](../checks/RED-TEAM-2026-07-30.md) records single-run observations in three harnesses. It is historical evidence under those conditions, not current setup parity or a reliability estimate.

## What remains unverified

| Work | Current boundary | Next evidence |
|---|---|---|
| Cross-harness setup | Portable instructions, not demonstrated current parity | Run the same synthetic interview in goose, Claude Code, and Codex; [issue #3](https://github.com/block/chalkline/issues/3) |
| Real-team adoption | The under-30-minute setup target is still a target | Recruit a consenting pilot; record task-level elapsed time, stalls, approval burden, and safe gaps; [issue #6](https://github.com/block/chalkline/issues/6) |
| Ingest quality | At most 10 candidate rules per artifact; no measured semantic input budget | Compare predeclared small/large synthetic inputs and unchanged controls; [issue #5](https://github.com/block/chalkline/issues/5) |
| Cross-repository consumption | Manual review and local snapshot contract; no bundled validator/projector | An independently reviewed projector and consuming-harness conformance tests before claiming automated enforcement |
| Website accessibility | DOM-stub tests and historical visual checks | Keyboard, mobile, and screen-reader review; no full accessibility audit is claimed |
| Semantic checking | No Jev integration or automatic fact-preservation check | Evaluate an optional adapter using the [semantic-check experiment](optional-semantic-checks.md) |

## Next execution plan

1. Ship sharing cleanup: current site claims, an adoption checklist, visible structure-only receipt validation, and bounded local corpus reads with synthetic regressions.
2. Run the synthetic setup across the actual target harnesses. Predeclare cases and repetitions, separate reviewer material, preserve unchanged controls, and report failures and unknown settings. Follow [the behavioral-fixture procedure](../checks/behavioral/README.md); do not treat existing unit tests as this evidence.
3. Run a small consenting-team pilot. Keep private artifacts and raw agent sessions out of this public repository. Publish only manually reviewed, sanitized findings or synthetic reproductions.
4. Evaluate optional semantic checks only after the pilot identifies a recurring problem. Keep ordinary setup and local tools dependency-free.
5. Build snapshot projection only if cross-repository use becomes a demonstrated need. Explicit file allowlists and code checks help, but cannot prove arbitrary prose harmless. Keep consuming-owner review and harness access controls.

No change in steps 2–5 is approved by this plan. Language approval, artifact approval, reusable calibration approval, and consumer deployment remain separate decisions. Upstream normative changes require the two maintainer roles in [Governance](../GOVERNANCE.md).
