# Optional semantic-check experiment

No TypeSafe/Jev adapter is bundled. This is an experiment plan, not a supported API or an effectiveness claim. Markdown remains canonical; setup, structural checks, and receipt arithmetic need no network or API key.

## Start with fact preservation

Use synthetic supplied facts and candidate drafts. Code extracts bounded candidate spans such as amounts, dates, identifiers, negations, and modal words. An optional semantic model evaluates narrow questions about each fact, such as whether a stated possibility became a promise or a failed request became a confirmed reservation. A generative model still writes copy; the semantic model does not rewrite it.

For retrieval in a larger corpus, first retrieve and filter candidates in code, then evaluate semantic relevance against the supplied task, audience, channel, and locale. Keep no-coverage, unavailable-source, invalid-source, and conflict outcomes distinct. Ranking does not approve a rule or resolve precedence.

## Keep code and people in control

- Code owns parsing, exact comparisons, hashes, arithmetic, explicit scope/precedence, and result routing. Never use a model to sanitize upstream instruction repositories.
- People own authority and all four approval decisions. A semantic answer cannot create a human decision or promote output into guidance.
- Ask independent questions over the same small state together. Do not send the entire repository when only a fact and its surrounding draft are needed.
- Keep raw judgments separate from policy thresholds. TypeSafe Choice/Score confidence and Noul probability are not Chalkline's ordinal 0–3 evidence assessment.
- Expose uncertain answers, errors, timeouts, and skipped checks. Never display an unavailable semantic check as a pass. Requiring a check is an explicit adopting-owner decision.
- Keep credentials server-side or in the local caller's authorized environment. Review provider data practices; avoid body-level debug logging of private inputs. The static site stays offline.

## Acceptance experiment

Predeclare a synthetic suite containing preserved and changed facts, ambiguous dates, unsupported causes, added retry instructions, and irrelevant retrieved passages. Have a separate reviewer label cases without seeing model results. Split tuning and holdout cases; run a deterministic-only control alongside the optional adapter.

Report false negatives and false positives, uncertainty/escalation rate, service failures, cost, end-to-end latency, and review effort. Report the exact model, SDK, questions, candidate spans, and thresholds. Choose thresholds from the consequences and held-out evidence, not a cookbook number. Include adversarially framed source data and option-order checks; typed output does not guarantee truth or injection resistance.

Proceed only if the adapter catches the targeted mutations without unacceptable false alarms or burden on the holdout. It must not change supplied factual strength, suppress blockers, invent evidence, or approve publication. Keep the default tools and CI independent of SDK installation and paid calls.

Before implementation, read the current [TypeSafe docs](https://docs.typesafe.ai/llms.txt), [confidence guidance](https://docs.typesafe.ai/confidence), and [model limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13). Recheck the applicable model's limitations; Jev 1.13 documents injection susceptibility, context distraction, and option-order effects.
