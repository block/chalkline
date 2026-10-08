# Chalkline explainer site

Static public explainer. No build, dependencies, accounts, uploads, remote assets, analytics, or live model. GitHub Pages publishes the site after approved changes merge to `main`.

From the repository root, preview with:

```sh
python3 -m http.server 8000 --bind 127.0.0.1 --directory website
```

Open http://127.0.0.1:8000. Python is optional; any static server works.

`index.html` contains the explanation and demo structure, `styles.css` the responsive styles, and `script.js` the fixed fictional examples. The Pages workflow copies only `index.html`, `styles.css`, and `script.js` into the deployment artifact. Documentation, tests, team references, receipts, reports, and reviewer fixtures are excluded.

## Demo boundaries

Harbor and its tasks are fictional. The demo does not run AI, verify facts, consult external references, or record reviewer approval. Its confidence assessment is illustrative and defaults to limited support. Removing a required source withholds the candidate and sets overall confidence to zero. Restoring it shows the candidate again, without implying approval. The receipt contract and checker are part of the repository; the site illustrates them without running the checker or a model.

## Checks

```sh
node --check website/script.js
node website/test.cjs
```

Node is needed only for these optional developer checks. The test exercises the actual script using a small DOM stub: both tasks, source removal/restoration, minimum scoring, and approval separation. It does not replace browser or accessibility review.

Browser checks on the local prototype covered desktop and 390px mobile layout, missing-source behavior, restoration, and absence of off-origin resources. No full accessibility audit, screen-reader test, live-model evaluation, or publication review is claimed. Recheck links and browser behavior before publication. Keep the site explanation aligned with canonical repository contracts; illustrative scores and process exit status never authorize publication.

## Publishing

`.github/workflows/pages.yml` runs the JavaScript checks on site pull requests without publishing. After a site or workflow change merges to `main`, it reruns checks and deploys the three public files to https://block.github.io/chalkline/. Manual runs deploy only when run from `main`. Deployments use the `github-pages` environment and GitHub’s short-lived identity token, not a stored publishing secret.

The repository Pages source must be set to GitHub Actions. Environment approval rules, if configured, still apply. There is no hosted PR preview. The live site becomes available after the first successful deployment.
