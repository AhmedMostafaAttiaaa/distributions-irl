# Module 01: Discrete distributions

How the common discrete distributions are generated, their full math, how to compute with them, and where they appear in statistics, data science and ML.

## Lessons

| Lesson | Notebook | Interactive page | Status |
|---|---|---|---|
| 01_01 Bernoulli and Binomial | [notebook](notebooks/01_01_bernoulli_binomial.ipynb) | [page](html/01_01_bernoulli_binomial.html) | done |

## How to open

- Notebooks: open in VS Code or JupyterLab (run from the `notebooks/` folder; they import `common/style.py` from the repo root).
- Pages: double-click the HTML file (internet needed for KaTeX and 3D).

## Decisions

- Where hand arithmetic over many PMF terms is impractical, the "by hand" step is the exact formula written as an explicit sum with `math.comb`, preceded by a normal-approximation calculation done on paper.
