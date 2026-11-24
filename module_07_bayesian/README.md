# Module 07: Bayesian thinking

Probability as a degree of belief, and how data update it: priors and posteriors, conjugate families (Beta-Binomial, Gamma-Poisson, Normal-Normal), credible intervals and predictions, MCMC sampling for posteriors without a formula, and Thompson sampling for choosing between options while learning.

## Lessons

| Lesson | Notebook | Interactive page | Status |
|---|---|---|---|

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
- Prerequisites: Module 02 (Beta, Gamma, Normal), Module 06 (likelihood, confidence intervals, A/B testing).
- The Bayesian A/B analysis in 07_02 reuses the Cookie Cats data downloaded for Module 06 (see `../module_06_inference/data/README.md`); everything else is synthetic.
