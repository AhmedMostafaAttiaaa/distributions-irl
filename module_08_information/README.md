# Module 08: Information theory

How much surprise a distribution carries and how far apart two distributions are: entropy and cross-entropy (the classification loss), KL and Jensen-Shannon divergence, the Wasserstein distance, and mutual information for feature selection.

## Lessons

| Lesson | Notebook | Interactive page | Status |
|---|---|---|---|
| 08_01 Entropy and cross-entropy | [notebook](notebooks/08_01_entropy_cross_entropy.ipynb) | [page](html/08_01_entropy_cross_entropy.html) | done |
| 08_02 KL divergence and Jensen-Shannon divergence | [notebook](notebooks/08_02_kl_js_divergence.ipynb) | [page](html/08_02_kl_js_divergence.html) | done |

## Contents of the folders

- `notebooks/`: the lessons (executed, with outputs).
- `html/`: the interactive pages (calculators, simulators, 3D views).
- `figures/`: PNG exports of every notebook figure, in notebook order.
- `data/`: see its README.

## How to open

- Notebooks: open in VS Code or JupyterLab (run from the `notebooks/` folder; they import `common/style.py` from the repo root).
- Pages: double-click the HTML file (internet needed for KaTeX and 3D).

## Decisions

- Each lesson has three worked examples (the main one in full, two more), every claim checked by simulation, an "In plain words" cell after each derivation, 3D plots and an interactive page.
- Prerequisites: Module 01-02 (discrete and continuous distributions), Module 07 for the Bayesian link to KL divergence.
- All logarithms are natural (nats) unless a lesson says bits.
