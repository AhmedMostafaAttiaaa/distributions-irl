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

## Contents of the folders

- `notebooks/`: the two lessons (executed, with outputs).
- `html/`: the interactive pages.
- `figures/`: PNG exports of every notebook figure (04_01_figNN.png, 04_02_figNN.png), in notebook order.
- `data/`: no external data; see its README.

## Suggested order

Read 04_01 first (the map and the six mechanisms), then 04_02 (how good each limit approximation is). Prerequisites: Modules 01 to 03, especially Poisson, Gamma, t and chi-square.

## Decisions

- Only two lessons, so each is explained in depth: "In plain words" cells after each derivation, three worked examples per lesson, every relationship verified by simulation.
- The HTML pages use a continuous engine: PDF and CDF lines, area shading, density histogram of samples, a quantile calculator, and special functions (incomplete gamma and beta) written in plain JavaScript so everything works from `file://`.
- All data are synthetic.
