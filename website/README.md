# Chalkline explainer site

Static public-site proposal. No build, dependencies, accounts, uploads, remote assets, analytics, or live model. This PR does not configure hosting or deploy the site.

From the repository root, preview with:

```sh
python3 -m http.server 8000 --bind 127.0.0.1 --directory website
```

Open http://127.0.0.1:8000. Python is optional; any static server works.

`index.html` contains the explanation and demo structure, `styles.css` the responsive styles, and `script.js` the fixed fictional examples. No repository files are automatically published. These four files and the local test are the entire site source; team references, receipts, local reports, and reviewer fixtures are excluded.

## Demo boundaries

Harbor and its tasks are fictional. The demo does not run AI, verify facts, consult external references, or record reviewer approval. Its confidence assessment is illustrative and defaults to limited support. Removing a required source withholds the candidate and sets overall confidence to zero. Restoring it shows the candidate again, without implying approval. The site labels receipt functionality as proposed in PR #18 while that work is unmerged.

## Checks

```sh
node --check website/script.js
node website/test.cjs
```

Node is needed only for these optional developer checks. The test exercises the actual script using a small DOM stub: both tasks, source removal/restoration, minimum scoring, and approval separation. It does not replace browser or accessibility review.

Browser checks on the local prototype covered desktop and 390px mobile layout, missing-source behavior, restoration, and absence of off-origin resources. No full accessibility audit, screen-reader test, live-model evaluation, or publication review is claimed. Recheck links and PR status before publication. Keep the site explanation aligned with canonical repository contracts; illustrative scores and process exit status never authorize publication.
