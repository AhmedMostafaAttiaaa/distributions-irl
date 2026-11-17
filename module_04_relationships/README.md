# Module 04: Relationships between distributions

How the distributions of Modules 01 to 03 are built from each other (sums, transformations, limits, special cases, mixtures, conditioning) and how well the limits approximate them.

## Lessons

| Lesson | Notebook | Interactive page | Status |
|---|---|---|---|
| 04_01 The Family Tree of Distributions | [notebook](notebooks/04_01_relationship_map.ipynb) | [page](html/04_01_relationship_map.html) | done |
| 04_02 Limits and approximations | [notebook](notebooks/04_02_limits_and_approximations.ipynb) | [page](html/04_02_limits_and_approximations.html) | done |

## How to open

- Notebooks: open in VS Code or JupyterLab (run from the `notebooks/` folder; they import `common/style.py` from the repo root).
- Pages: double-click the HTML file (internet needed for KaTeX and 3D).

## Decisions

- Only two lessons, so each is explained in depth: "In plain words" cells after each derivation, three worked examples per lesson, every relationship verified by simulation.
- The HTML pages use a continuous engine: PDF and CDF lines, area shading, density histogram of samples, a quantile calculator, and special functions (incomplete gamma and beta) written in plain JavaScript so everything works from `file://`.
- All data are synthetic.
