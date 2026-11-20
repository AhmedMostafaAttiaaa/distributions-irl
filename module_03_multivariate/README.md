# Module 03: Multivariate distributions

Distributions of several variables together: the multivariate Normal, the Dirichlet, Gaussian mixtures and copulas.

## Lessons

| Lesson | Notebook | Interactive page | Status |
|---|---|---|---|
| 03_01 The Multivariate Normal | [notebook](notebooks/03_01_multivariate_normal.ipynb) | [page](html/03_01_multivariate_normal.html) | done |
| 03_02 The Dirichlet and Dirichlet-Multinomial | [notebook](notebooks/03_02_dirichlet_multinomial.ipynb) | [page](html/03_02_dirichlet_multinomial.html) | done |
| 03_03 Gaussian Mixtures and the EM Algorithm | [notebook](notebooks/03_03_gaussian_mixtures.ipynb) | [page](html/03_03_gaussian_mixtures.html) | done |
| 03_04 Copulas: Dependence Separate from the Marginals | [notebook](notebooks/03_04_copulas.ipynb) | [page](html/03_04_copulas.html) | done |

## How to open

- Notebooks: open in VS Code or JupyterLab (run from the `notebooks/` folder; they import `common/style.py` from the repo root).
- Pages: double-click the HTML file (internet needed for KaTeX and 3D).

## Decisions

- **Deepened on 2026-11-20:** every lesson now has three worked examples (the main one plus two more, each solved by hand, in code with asserts, by simulation and with a plain-language decision), an "In plain words" cell after the derivations, extra exercises with solutions, and a panel of two editable extra examples on its page.
- The HTML pages use a continuous engine: PDF and CDF lines, area shading, density histogram of samples, a quantile calculator, and special functions (incomplete gamma and beta) written in plain JavaScript so everything works from `file://`.
- Data are synthetic except the Old Faithful geyser data in 03_03 (`data/download_data.py`).
