# Adopting the template

Complete this review before committing your team's setup. These are repository settings, not new interview questions or language rules. Do not assign owners, remove notices, or publish automatically.

- [ ] Confirm repository visibility and the agent/model provider's data practices. Use only authorized, repository-safe material; see [Safety](../SAFETY.md).
- [ ] Replace or deliberately retain `CODEOWNERS`. Its current owner routes upstream Chalkline reviews, not your team's language decisions.
- [ ] Review `GOVERNANCE.md` and `CONTRIBUTING.md`. Replace upstream processes and links with your own approved ownership and contribution decisions.
- [ ] Review `.github/` issue forms, PR template, workflows, permissions, and environments. In particular, disable or replace the Pages workflow unless you deliberately intend to publish its static site. Check upstream issue labels and contact links.
- [ ] Remove or adapt `website/` if you do not need the upstream explainer. Review upstream GitHub links before using it as your own site.
- [ ] Preserve applicable license and copyright notices. Do not assume a template adoption changes their requirements.
- [ ] Review the generated reference diff, provenance, exact-wording scope, and any separately approved calibration pair. Record unresolved ownership decisions instead of inventing an approver.
- [ ] Decide separately whether to approve references, commit changes, and publish or push the repository.

For use in another repository, follow [PINNING.md](../PINNING.md). A source pin or search index is not a validated snapshot; drafting agents must not fetch upstream instruction files.

This checklist does not verify authority, provider privacy, repository permissions, or that an agent followed the protocol. The adopting owner reviews those decisions.
