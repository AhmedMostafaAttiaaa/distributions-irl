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

## How to open

- Notebooks: open in VS Code or JupyterLab (run from the `notebooks/` folder; they import `common/style.py` from the repo root).
- Pages: double-click the HTML file (internet needed for KaTeX and 3D).

## Decisions

- Each lesson is explained in depth: "In plain words" cells after each derivation, three worked examples (the main one solved by hand, in code and by simulation), every claim verified by simulation.
- Pages are single self-contained files (vanilla JS and SVG) with animations where they help.
- Data are synthetic unless a lesson says otherwise.
