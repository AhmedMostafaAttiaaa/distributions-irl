# Module 10: Model evaluation and the confusion matrix

How to judge a classifier or a regression model honestly: the two overlapping score distributions behind every confusion matrix, precision, recall, F1 and MCC, ROC and precision-recall curves with AUC as a probability, cost-sensitive thresholds, the base-rate fallacy, calibration, multiclass confusion matrices and residual diagnostics.

## Lessons

| Lesson | Notebook | Interactive page | Status |
|---|---|---|---|
| 10_01 The confusion matrix from two score distributions | [notebook](notebooks/10_01_confusion_matrix_from_distributions.ipynb) | [page](html/10_01_confusion_matrix_from_distributions.html) | done |
| 10_02 Classification metrics | [notebook](notebooks/10_02_classification_metrics.ipynb) | [page](html/10_02_classification_metrics.html) | done |

## Contents of the folders

- `notebooks/`: the lessons (executed, with outputs).
- `html/`: the interactive pages (calculators, simulators, 3D views).
- `figures/`: PNG exports of every notebook figure, in notebook order.
- `data/`: see its README.

## How to open

- Notebooks: open in VS Code or JupyterLab (run from the `notebooks/` folder; they import `common/style.py` from the repo root).
- Pages: double-click the HTML file (internet needed for KaTeX and 3D).

## Decisions

- The central picture is two overlapping score distributions (positives and negatives) with a movable threshold: confusion matrix, metrics and ROC point all follow from it.
- Every model and metric is written from scratch in NumPy, each lesson has several worked examples with numbers, 2D and 3D figures and an interactive page.
- Prerequisites: Modules 02 (normal and beta distributions), 06 (tests and errors), 08 (log loss) and 09 (naive Bayes, GLMs).
