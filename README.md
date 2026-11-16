# Probability Distributions Study Book

A self-study course on probability distributions and how they are used in statistics, data science, ML and AI.
Every lesson has a Jupyter notebook (theory, derivations, 2D and 3D plots, simulation, a worked real-world example)
and a lightweight interactive HTML page.

## Set up

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## How to open the lessons

- Notebooks: open `module_XX_slug/notebooks/*.ipynb` in VS Code or JupyterLab.
  Check that one runs top to bottom with `jupyter nbconvert --to notebook --execute --inplace <notebook>`.
- Interactive pages: double-click `module_XX_slug/html/*.html` (works from `file://`, internet needed for KaTeX and the 3D charts).
- Book index: open `index.html`.

## Layout

- `common/style.py`: color palette and plot settings only.
- `templates/`: skeletons for new lesson notebooks and HTML pages.
- `module_XX_slug/`: notebooks, html, data and a glossary per module.
- `plan.md`: progress tracker. `CLAUDE.md`: working rules for this project.
