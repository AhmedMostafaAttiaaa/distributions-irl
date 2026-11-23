# Module 06: Statistical inference

How to learn about a population from a sample: estimating parameters (method of moments, maximum likelihood), quantifying uncertainty with confidence intervals, and deciding between hypotheses with tests, p-values and power. Later lessons cover nonparametric tests, multiple testing and A/B testing.

## Lessons

| Lesson | Notebook | Interactive page | Status |
|---|---|---|---|
| 06_01 Estimation: method of moments and maximum likelihood | [notebook](notebooks/06_01_estimation_mle_mom.ipynb) | [page](html/06_01_estimation_mle_mom.html) | done |
| 06_02 Confidence intervals | [notebook](notebooks/06_02_confidence_intervals.ipynb) | [page](html/06_02_confidence_intervals.html) | done |
| 06_03 Hypothesis testing: the core ideas | [notebook](notebooks/06_03_hypothesis_testing_core.ipynb) | [page](html/06_03_hypothesis_testing_core.html) | done |
| 06_04 The common tests: t-tests, chi-square and ANOVA | [notebook](notebooks/06_04_common_tests.ipynb) | [page](html/06_04_common_tests.html) | done |
| 06_05 Nonparametric tests: ranks, permutations and KS | [notebook](notebooks/06_05_nonparametric_tests.ipynb) | [page](html/06_05_nonparametric_tests.html) | done |
| 06_06 Multiple testing: Bonferroni, Holm and Benjamini-Hochberg | [notebook](notebooks/06_06_multiple_testing.ipynb) | [page](html/06_06_multiple_testing.html) | done |
| 06_07 A/B testing end to end: the Cookie Cats experiment | [notebook](notebooks/06_07_ab_testing.ipynb) | [page](html/06_07_ab_testing.html) | done |
| 06_08 Risk, relative risk and odds ratio | [notebook](notebooks/06_08_risk_odds_ratio.ipynb) | [page](html/06_08_risk_odds_ratio.html) | done |
| 06_09 Variance reduction with CUPED | [notebook](notebooks/06_09_cuped_variance_reduction.ipynb) | [page](html/06_09_cuped_variance_reduction.html) | done |
| 06_10 Likelihood-ratio, Wald and score tests | [notebook](notebooks/06_10_likelihood_ratio_tests.ipynb) | [page](html/06_10_likelihood_ratio_tests.html) | done |

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
- Lessons 06_01 to 06_04 were built on 2026-11-21; 06_05 to 06_07 follow the next day.
- Data are synthetic unless a lesson says otherwise.
