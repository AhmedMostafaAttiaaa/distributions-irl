# Module 00: Foundations

The vocabulary every later module uses: random variables, expectation and moments, joint and conditional distributions, transformations, and Bayes' theorem.

## Lessons

| Lesson | Notebook | Interactive page | Status |
|---|---|---|---|
| 00_01 Random Variables: PMF, PDF, CDF and Quantiles | [notebook](notebooks/00_01_random_variables.ipynb) | [page](html/00_01_random_variables.html) | done |
| 00_02 Expectation, Variance, Moments and the MGF | [notebook](notebooks/00_02_expectation_moments.ipynb) | [page](html/00_02_expectation_moments.html) | done |
| 00_03 Joint, Marginal and Conditional Distributions | [notebook](notebooks/00_03_joint_conditional.ipynb) | [page](html/00_03_joint_conditional.html) | done |
| 00_04 Transformations of Random Variables | [notebook](notebooks/00_04_transformations.ipynb) | [page](html/00_04_transformations.html) | done |
| 00_05 Conditional Probability and Bayes Theorem | [notebook](notebooks/00_05_bayes_theorem.ipynb) | [page](html/00_05_bayes_theorem.html) | done |

## How to open

- Notebooks: open in VS Code or JupyterLab (run from the `notebooks/` folder; they import `common/style.py` from the repo root).
- Pages: double-click the HTML file (internet needed for KaTeX and 3D).

## Decisions

- **Deepened on 2026-11-20:** every lesson now has three worked examples (the main one plus two more, each solved by hand, in code with asserts, by simulation and with a plain-language decision), an "In plain words" cell after the derivations, extra exercises with solutions, and a panel of two editable extra examples on its page.
- The HTML pages use a continuous engine: PDF and CDF lines, area shading, density histogram of samples, a quantile calculator, and special functions (incomplete gamma and beta) written in plain JavaScript so everything works from `file://`.
- All data are synthetic.
