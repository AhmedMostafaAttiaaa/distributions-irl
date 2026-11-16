# Module 02: Continuous distributions

The continuous families used in statistics, data science and ML, with extra plain-language explanation and three worked examples per lesson.

## Lessons

| Lesson | Notebook | Interactive page | Status |
|---|---|---|---|
| 02_01 Uniform and Normal | [notebook](notebooks/02_01_uniform_normal.ipynb) | [page](html/02_01_uniform_normal.html) | done |
| 02_02 Lognormal | [notebook](notebooks/02_02_lognormal.ipynb) | [page](html/02_02_lognormal.html) | done |
| 02_03 Exponential, Gamma and Erlang | [notebook](notebooks/02_03_exponential_gamma_erlang.ipynb) | [page](html/02_03_exponential_gamma_erlang.html) | done |

## How to open

- Notebooks: open in VS Code or JupyterLab (run from the `notebooks/` folder; they import `common/style.py` from the repo root).
- Pages: double-click the HTML file (internet needed for KaTeX and 3D).

## Decisions

- To explain more, every derivation block is followed by an "In plain words" cell, and each lesson has three worked examples: a main example (3 to 4 questions with hand, code plus assert, simulation, shaded plots and a decision) and two shorter examples from other domains.
- The HTML pages use a continuous engine: PDF and CDF lines, area shading, density histogram of samples, a quantile calculator, and special functions (incomplete gamma and beta) written in plain JavaScript so everything works from `file://`.
- Lessons 02_01 and 02_02 use the real `tips` dataset (`data/download_data.py`).
