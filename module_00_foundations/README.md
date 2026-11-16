# Module 00: Foundations

The vocabulary every later module uses: random variables, expectation and moments, joint and conditional distributions, transformations, and Bayes' theorem.

## Lessons

| Lesson | Notebook | Interactive page | Status |
|---|---|---|---|
| 00_01 Random Variables: PMF, PDF, CDF and Quantiles | [notebook](notebooks/00_01_random_variables.ipynb) | [page](html/00_01_random_variables.html) | done |
| 00_02 Expectation, Variance, Moments and the MGF | [notebook](notebooks/00_02_expectation_moments.ipynb) | [page](html/00_02_expectation_moments.html) | done |
| 00_03 Joint, Marginal and Conditional Distributions | [notebook](notebooks/00_03_joint_conditional.ipynb) | [page](html/00_03_joint_conditional.html) | done |
| 00_04 Transformations of Random Variables | [notebook](notebooks/00_04_transformations.ipynb) | [page](html/00_04_transformations.html) | done |

## How to open

- Notebooks: open in VS Code or JupyterLab (run from the `notebooks/` folder; they import `common/style.py` from the repo root).
- Pages: double-click the HTML file (internet needed for KaTeX and 3D).

## Decisions

- To keep these lessons short, each has one main worked example (hand, code plus assert, simulation, plots, decision) and one shorter extra example; derivations are compact with "In plain words" cells.
- The HTML pages use a continuous engine: PDF and CDF lines, area shading, density histogram of samples, a quantile calculator, and special functions (incomplete gamma and beta) written in plain JavaScript so everything works from `file://`.
- All data are synthetic.
