# Roadmap

chalkline is an experiment, and this roadmap is part of the experiment: we're publishing what we're testing, what evidence would move us, and what would stop us. Steps unlock on evidence, not dates.

## What we're testing

The template ships five small conventions:

| Convention | The idea it carries |
|---|---|
| Frontmatter (`brand` / `domain` / `enforcement`) | Not all guidance has equal authority |
| AGENTS.md consult order + precedence | Agents follow rules they're routed to, in a declared order |
| **Exact wording** blocks | Some language must survive every rewrite byte-for-byte |
| Calibration pairs | An approved before/after is both a regression check and a teaching example |
| Provenance footers | Every rule says who approved it, from what, and when |

The hypothesis: these spread the way markdown and robots.txt spread — by being copied because they're small and immediately useful, not by being specified first.

## Now — prove the setup works

- Dry-run the protocol end to end ([#2](https://github.com/block/chalkline/issues/2))
- Same protocol, multiple harnesses — divergence reports drive protocol fixes ([#3](https://github.com/block/chalkline/issues/3))
- Find the practical limits of pasted-material ingestion ([#5](https://github.com/block/chalkline/issues/5))
- Real teams through setup, instrumented ([#6](https://github.com/block/chalkline/issues/6))

**Evidence that moves us on:** teams finish in one sitting and the before/after demo visibly improves their copy. If they can't, or it doesn't, the protocol is wrong and we fix it here before adding anything.

## Next — serve the references beyond the repo (if asked)

A small MCP server that reads any chalkline-shaped repo, so your references travel to every MCP-capable tool rather than only agents that open the repo directly.

**Gate:** field reports actually asking for cross-tool retrieval. If nobody asks, we don't build it.

## Later — formalize the conventions (if earned)

If independent repos adopt these conventions and start needing to interoperate — shared tooling, portable evaluations, cross-tool authority — the conventions may deserve a documented format with schemas and conformance cases.

**Gate:** multiple independent corpora and at least two independent implementations. Until then we call these *conventions*, not a protocol or standard, on purpose.

## What would stop us

Honest kill conditions, stated up front:

- If setup can't be made to work in one sitting, we stop adding and fix or fold.
- If no one wants their references outside the repo, the MCP server doesn't get built.
- If the conventions don't spread beyond us, they stay a good template and nothing more.

**What stopping does *not* mean:** this repo going away or closing up. It's a template under Apache-2.0 with DCO — every copy keeps working forever, archived or not. Kill conditions govern our investment, never your ownership.

## What we won't add

Risk-level taxonomies, multi-level enforcement enums, decision-receipt schemas, eval runners, multi-brand machinery, or config emission for specific tools. Some of these ideas may matter at larger scale — they'll be earned elsewhere first, not shipped here on speculation. The template stays small enough to read in one sitting, because that's the property that makes it copyable.
