# Module 05: Sampling and limit theorems

What happens to averages and other statistics when we collect more data: the law of large numbers, the central limit theorem, standard errors and the bootstrap.

## Lessons

| Lesson | Notebook | Interactive page | Status |
|---|---|---|---|

## Contents of the folders

- `notebooks/`: the lessons (executed, with outputs).
- `html/`: the interactive pages (animations, calculators, 3D views).
- `figures/`: PNG exports of every notebook figure, in notebook order.
- `data/`: see its README.
| 05_01 The law of large numbers | [notebook](notebooks/05_01_law_of_large_numbers.ipynb) | [page](html/05_01_law_of_large_numbers.html) | done |
| 05_02 The central limit theorem | [notebook](notebooks/05_02_central_limit_theorem.ipynb) | [page](html/05_02_central_limit_theorem.html) | done |
| 05_03 Sampling distributions and the standard error | [notebook](notebooks/05_03_sampling_distributions_standard_error.ipynb) | [page](html/05_03_sampling_distributions_standard_error.html) | done |
| 05_04 The bootstrap and Monte Carlo | [notebook](notebooks/05_04_bootstrap_monte_carlo.ipynb) | [page](html/05_04_bootstrap_monte_carlo.html) | done |
| 05_05 Concentration inequalities | [notebook](notebooks/05_05_concentration_inequalities.ipynb) | [page](html/05_05_concentration_inequalities.html) | done |
| 05_06 Delta method and Slutsky | [notebook](notebooks/05_06_delta_method_slutsky.ipynb) | [page](html/05_06_delta_method_slutsky.html) | done |
| 05_07 Order statistics and extremes | [notebook](notebooks/05_07_order_statistics_extremes.ipynb) | [page](html/05_07_order_statistics_extremes.html) | done |
| 05_08 Sampling designs | [notebook](notebooks/05_08_sampling_designs.ipynb) | [page](html/05_08_sampling_designs.html) | done |

## How to open

- Notebooks: open in VS Code or JupyterLab (run from the `notebooks/` folder; they import `common/style.py` from the repo root).
- Pages: double-click the HTML file (internet needed for KaTeX and 3D).

## Decisions

- Each lesson is explained in depth: "In plain words" cells after each derivation, three worked examples (the main one solved by hand, in code and by simulation), every claim verified by simulation.
- Pages are single self-contained files (vanilla JS and SVG) with animations where they help.
- Data are synthetic unless a lesson says otherwise.
