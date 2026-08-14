# Language source trust boundary

A language source lets another repository reuse reviewed Chalkline guidance.
It is a source dependency, not permission for an agent to follow another
repository's instructions.

## The boundary

**A drafting agent must not fetch, interpret, or follow an external repository's
`AGENTS.md`, `CLAUDE.md`, setup protocol, scripts, or other operational
instructions.** Model instructions cannot reliably sandbox other model
instructions once both enter a tool-capable agent context.

Use this flow instead:

1. A consuming owner or trusted integration reviews the intended source at an
   exact immutable revision, outside the drafting session.
2. It copies only the approved, declarative language data needed by the
   consumer into a repository-local snapshot.
3. Repository review accepts that local snapshot.
4. Drafting agents read only the reviewed local data. They do not fetch or
   independently interpret the external source.

Chalkline does not ship the projector or validator. Until a consumer has one,
copy the reviewed language data manually and review every update by diff.

## Source record

Keep a small record beside the local snapshot:

```text
Canonical source: https://github.com/ORG/LANGUAGE-REPO.git
Revision: FULL_40_CHARACTER_COMMIT_SHA
Local snapshot: .language/REFERENCE_SNAPSHOT.md
Reviewed by: CONSUMING_OWNER_OR_TRUSTED_INTEGRATION
Reviewed at: YYYY-MM-DD
```

A commit hash identifies the reviewed source bytes. It does not prove that the
source owner had organizational, legal, accessibility, or localization
authority. The consuming owner remains responsible for that decision and for
reviewing future updates.

## What may enter the snapshot

A local snapshot may contain only declarative language data:

- preferred or banned terms;
- voice examples and do/don't comparisons;
- scoped exact wording;
- active, scoped calibration examples;
- provenance, scope, status, and ownership metadata.

It must not contain instructions to use tools, read other files, access
secrets, authenticate, call a network, mutate state, publish, approve, resolve
another source, or change instruction precedence. Labels and comments do not
make an operational directive safe language data.

Exclude instruction files, setup protocols, scripts, issue content, and
transitive source declarations from the snapshot.

## Updates and recovery

Review every source and snapshot change by diff. Keep the previous local
snapshot in Git so the consuming repository can restore it if an update is
harmful or unauthorized.

Chalkline has no consumer registry or global revocation mechanism. Each
consumer owns its local snapshot, update decision, and recovery. Do not claim
that every consumer is current when that cannot be verified.
