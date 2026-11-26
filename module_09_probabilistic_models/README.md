# Module 09: Probabilistic modelling

How the distributions of Modules 01-08 become working models: losses as likelihoods, generalised linear models, naive Bayes on real text, density estimation and mixtures, anomaly detection, the randomness of neural networks, LLM sampling, VAEs, diffusion, Gaussian processes, reinforcement-learning policies, priors as regularisers, the bias-variance trade-off and uncertainty with conformal prediction.

## Lessons

| Lesson | Notebook | Interactive page | Status |
|---|---|---|---|
| 09_01 Loss functions as likelihoods | [notebook](notebooks/09_01_losses_as_likelihoods.ipynb) | [page](html/09_01_losses_as_likelihoods.html) | done |
| 09_02 Generalised linear models | [notebook](notebooks/09_02_glms.ipynb) | [page](html/09_02_glms.html) | done |

## Contents of the folders

- `notebooks/`: the lessons (executed, with outputs).
- `html/`: the interactive pages (calculators, simulators, 3D views).
- `figures/`: PNG exports of every notebook figure, in notebook order.
- `data/`: see its README.

## How to open

- Notebooks: open in VS Code or JupyterLab (run from the `notebooks/` folder; they import `common/style.py` from the repo root).
- Pages: double-click the HTML file (internet needed for KaTeX and 3D).

## Decisions

- Every model is written from scratch in NumPy (no scikit-learn or deep-learning framework needed), so each formula can be followed line by line and checked against the theory.
- Each lesson has several worked examples with numbers, many figures (2D and 3D), an "In plain words" cell after each derivation and an interactive page.
- Prerequisites: Modules 02 (continuous), 03 (multivariate), 06 (likelihood) and 08 (entropy, KL).
