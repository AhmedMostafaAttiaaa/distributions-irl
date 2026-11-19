# Module 0A: Basics layer

A from-zero start before Module 00: sets and events, counting, the rules of probability, conditional probability and independence, probability trees, and a first look at random variables. No earlier knowledge is assumed beyond school arithmetic. Module 00 (random variables, expectation, joint distributions, transformations, Bayes) follows directly after this layer.

## Lessons

| Lesson | Notebook | Interactive page | Status |
|---|---|---|---|
| 0a_01 Outcomes, events and the sample space | [notebook](notebooks/0a_01_sets_events_sample_space.ipynb) | [page](html/0a_01_sets_events_sample_space.html) | done |

## Contents of the folders

- `notebooks/`: the lessons (executed, with outputs).
- `html/`: the interactive pages (calculators, simulators, 3D views).
- `figures/`: PNG exports of every notebook figure, in notebook order.
- `data/`: see its README.

## How to open

- Notebooks: open in VS Code or JupyterLab (run from the `notebooks/` folder; they import `common/style.py` from the repo root).
- Pages: double-click the HTML file (internet needed for KaTeX and 3D).

## Decisions

- This module is a layer in front of Module 00; Module 00 files and names are unchanged. The folder is named `module_0a_basics` and lessons `0a_01` to `0a_06` so nothing is renumbered.
- Lessons use many small, concrete examples (dice, cards, passwords, lotteries, quality control, spam filters). One main example per lesson is solved by hand, in code with asserts and by simulation; the others are shorter.
- Pages are single self-contained files (vanilla JS and SVG) with calculators and simulators.
- Data are synthetic.
