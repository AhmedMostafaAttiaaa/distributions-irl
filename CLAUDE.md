# CLAUDE.md — Probability Distributions Study Book

Standing instructions for Claude Code. Read this file and `plan.md` fully at the start of every session, on every device.

---

## 1. Project goal

A self-study course on **probability distributions and how they are used in statistics, data science, ML and AI**, built module by module.

Each lesson produces:
1. A **Jupyter notebook** with full-depth theory, 2D and 3D plots, simulations, and a real-world worked example with concrete numbers and its own plots.
2. A **lightweight interactive HTML page** for the same lesson.

At the end, all HTML pages are linked into one **HTML book** with an index (table of contents) and a glossary.

- Language: **English**
- Depth: **full**. Intuition first, then formal definitions and complete derivations.
- Audience: a learner who will read the code and explain it aloud, so **readability beats cleverness everywhere**.

---

## 2. Session start protocol (every session, every device)

Repository: https://github.com/AhmedMostafaAttiaaa/distributions-irl (branch `main`)

Several devices may work on this repo at the same time, **each on a different module**. `plan.md` is the coordination point.

0. **Check the git identity** before any commit (see §11, Authorship). If `git config user.email` is not `ahmed.mostafa.attiaaa@gmail.com`, set it for this repo first.
1. `git pull --rebase`
2. Read `plan.md`. Find the module you were asked to work on.
3. If its status is 🟨 and claimed by **another** device, **stop and tell the user**. Do not work on it.
4. **Claim it**: set the status to 🟨, add your device name and today's date in the progress table, then commit `plan: claim module XX (<device>)` and push **immediately**.
5. If the module's lesson list is marked `(draft)`, refine it first: confirm the lesson split, examples and datasets, update `plan.md`, then commit and push.
6. If **Phase 0 (repo scaffold)** is not ✅, do it before any module.

---

## 3. Repository layout

```
prob-distributions/
├── CLAUDE.md                  # these rules
├── plan.md                    # shared to-do / progress tracker
├── .claude/settings.json      # Claude Code project settings (attribution off)
├── README.md                  # project overview + how to run
├── requirements.txt           # base Python deps
├── .gitignore
├── index.html                 # book table of contents (updated after every module)
├── glossary.html              # built in the final phase
├── common/
│   └── style.py               # tiny: palette + matplotlib rcParams only
├── templates/
│   ├── lesson_template.ipynb  # notebook skeleton (section headers from §4)
│   └── lesson_template.html   # HTML skeleton (layout, CSS, nav, chart helpers)
└── module_XX_slug/
    ├── README.md              # module overview, lesson list, how to open
    ├── glossary.md            # term | definition | lesson link
    ├── notebooks/
    │   └── XX_YY_slug.ipynb
    ├── html/
    │   └── XX_YY_slug.html
    ├── data/
    │   ├── README.md          # source URL, license, download date, description
    │   └── download_data.py   # only if data is downloaded
    └── figures/               # optional: 1 preview PNG per lesson for the README
```

Naming:
- Module folder: `module_01_discrete`, two-digit number plus a short slug.
- Lesson files: `XX_YY_slug`, where XX is the module and YY the lesson. The notebook and HTML **share the same base name**.
- If a module is large, split it into several lessons (one per family or sub-topic) rather than one giant notebook.

---

## 4. Lesson notebook template (sections in this order)

1. **Title + learning objectives + prerequisites** (link to earlier lessons)
2. **Prerequisite recap**: 3–6 lines restating any foundation concepts used (needed while Module 00 may not exist yet)
3. **Intuition / story**: the real-world process that generates this distribution
4. **Formal definition** (LaTeX): support, parameters and their meaning, PMF/PDF, CDF
5. **Derivations (full)**: show the steps for normalization, mean, variance and MGF/PGF where tractable, plus mode, skewness and kurtosis (derived or stated with a reference)
6. **Properties & relationships**: memorylessness, additivity, limits, links to other distributions
7. **2D visuals**: PMF/PDF, CDF, parameter sweeps (several parameter values on one axis), effect of each parameter
8. **3D visual**: PMF/PDF as a surface or 3D bars over (x, parameter), or a joint distribution
   - static `matplotlib` mplot3d version (renders on GitHub)
   - interactive Plotly version (renders in VS Code/Jupyter)
9. **Simulation vs theory**: sample with `numpy`, compare the histogram to the theoretical PMF/PDF, and show the running mean converging
10. **`scipy.stats` cheat sheet**: `pmf/pdf`, `cdf`, `sf`, `ppf`, `rvs`, `mean`, `var`, `interval`, `fit` where relevant
11. **Real-world worked example** (see §5) with its own plots
12. **Where it's used**: separate short subsections for Statistics / Data Science / ML & AI, with concrete cases
13. **Common pitfalls & misconceptions**
14. **Exercises** (4–8, increasing difficulty) with **solutions** at the end of the notebook
15. **Summary table**: parameters, support, mean, variance, when to use, `scipy` name

---

## 5. Real-world worked example rules (mandatory for every lesson)

- A **realistic scenario with concrete numbers**: an e-commerce store, call center, factory, hospital, sports, text, etc. If the numbers are illustrative, say so, and keep them plausible.
- Pose 2–4 concrete questions (e.g. "What is the probability of more than 20 calls in an hour?").
- **Solve by hand first**: write the formula, substitute the numbers in LaTeX, and show the arithmetic.
- **Then solve in code**, and add an `assert np.isclose(hand_result, code_result)` cell.
- **Then verify by simulation**: Monte Carlo estimate vs the exact answer.
- **Give the example its own plots**: shade the region being asked about (e.g. P(X ≥ 40)), mark the mean, and annotate the answer on the plot.
- End with a **plain-language interpretation and decision**, e.g. "the manager should staff 3 agents because…".
- Optional: a second, shorter example from a different domain.

---

## 6. Code style: readable and easy to explain

- **One idea per code cell**, ideally ≤ 15 lines.
- **A markdown cell before every code cell** explaining *what* it does and *why*.
- Descriptive names: `n_visitors`, `p_conversion`, `calls_per_hour`. Math-standard short names (`n`, `p`, `k`) are fine when the cell explains them. Use `lam` for λ, with a comment.
- No code golf: avoid long chained comprehensions, nested lambdas and clever one-liners. Explicit loops are fine when clearer.
- All imports in the first code cell. Reproducibility: `rng = np.random.default_rng(42)`.
- Prefer frozen `scipy.stats` objects: `dist = stats.binom(n=n_visitors, p=p_conversion)`.
- Every plot needs a title, axis labels (with units), a legend when there is more than one series, and readable font sizes.
- Define a helper function only if it is used ≥ 3 times in that notebook, inside the notebook, with a docstring. `common/style.py` holds **only** the color palette and rcParams. Teaching code never hides in external modules.
- Notebooks are **saved with outputs** and must run clean top to bottom (see §10).

---

## 7. Plotting

- 2D: `matplotlib` + `seaborn`.
- 3D: `matplotlib` mplot3d (static) **and** `plotly` (interactive).
- Use the palette from `common/style.py` everywhere so the book looks consistent. Apply colorblind-safe colors.

---

## 8. Interactive HTML rules (light as possible)

- **One HTML file per lesson**, self-contained single file (inline CSS + JS), started from `templates/lesson_template.html`.
- **2D charts: vanilla JS + SVG or Canvas, zero dependencies.**
- **3D charts: Plotly.js `gl3d` partial bundle from a CDN**, loaded **only** on pages that have a 3D view.
- **Formulas: KaTeX from a CDN** (auto-render).
- Size target: **< 150 KB per file**, excluding CDN libraries.
- Must work by **double-clicking the file** (`file://`): no local server, no `fetch()` of local files. Embed any small data as JSON inside the page.
- Responsive layout, plus light/dark mode via `prefers-color-scheme`.

Each lesson page contains:
1. Header with navigation: Book index (`../../index.html`), ← previous lesson, next lesson →
2. A short concept summary and key formulas
3. **Parameter sliders** with a live PMF/PDF chart and a live CDF chart
4. Live readouts: mean, variance, std, skewness, plus a **probability calculator** for P(a ≤ X ≤ b) that highlights the region
5. A **"Draw N samples" button**: histogram of the samples overlaid on the theoretical curve
6. A **worked example panel**: the notebook's real example with editable inputs, a live answer and the shaded plot
7. **"Where it's used" cards**: Statistics / Data Science / ML & AI
8. A **3D view** where relevant
9. A footer linking to the matching notebook file

Verify each page: open it with a headless browser if one is available (e.g. Playwright) and check for **zero console errors**. Otherwise review the JS carefully.

---

## 9. Data rules

- Decide per module. Small modules use synthetic data or tiny embedded tables. Use real datasets only where they add value.
- Save data in `module_XX/data/`. Every dataset must be documented in `data/README.md` with: **source URL, license, download date, size, column description**.
- Downloaded data comes with a `download_data.py` script so another device can reproduce it.
- Files **> 25 MB** go in `.gitignore`. The notebook must tell the reader to run `download_data.py` first.
- Extra dependencies for one module (e.g. `torch`) go in `module_XX/requirements.txt`, not the base file.

---

## 10. Definition of done (per lesson)

- [ ] Notebook follows §4 and runs clean: `jupyter nbconvert --to notebook --execute --inplace <nb>` with no errors
- [ ] Worked example follows §5, and its asserts pass
- [ ] 2D and 3D plots present and labeled
- [ ] HTML page follows §8, has zero console errors and is under the size target
- [ ] Glossary terms added to `module_XX/glossary.md`
- [ ] Module `README.md` lesson list updated
- [ ] `plan.md` checkboxes ticked for this lesson
- [ ] **Committed and pushed** (see §11)

Per module, when all lessons are done:
- [ ] Module `README.md` complete, with optional preview images
- [ ] Root `index.html` updated with links to this module's lesson pages
- [ ] Prev/next links between lessons verified
- [ ] `plan.md` status set to ✅ with date, committed and pushed

---

## 11. Git workflow

### Authorship (strict)
The **only** author and contributor of this repo is the owner's account:
- `user.name`: `AhmedMostafaAttiaaa`
- `user.email`: `ahmed.mostafa.attiaaa@gmail.com`

Rules:
- Set the identity **locally for this repo** on every device (don't change global config):
  ```bash
  git config user.name  "AhmedMostafaAttiaaa"
  git config user.email "ahmed.mostafa.attiaaa@gmail.com"
  ```
- **No AI attribution anywhere.** Never add `Co-Authored-By:` trailers, "Generated with Claude Code" lines, Claude session links, or any other Claude/Anthropic attribution to commit messages, PR descriptions, tags, README files, notebooks or HTML pages.
- Never use `--author` with any other identity. Never commit as a bot or another account.
- `.claude/settings.json` in this repo sets `attribution.commit` and `attribution.pr` to empty strings so Claude Code's default trailer is switched off. Don't remove it.
- Before each push, verify the authors with `git log -5 --format='%an <%ae>%n%b'`. Every author must be the owner's account, and no message body may contain a `Co-Authored-By` line. If one does, amend it **before pushing** (never rewrite pushed history).

### Routine
- **Commit and push after every lesson** (notebook + HTML + data + glossary + plan.md updates).
- Commit message format: `module XX lesson YY: <slug> — notebook, html, example`
- Always `git pull --rebase` before pushing. Only `plan.md` and `index.html` should ever conflict, since modules live in separate folders. Resolve by **keeping both sides' changes**.
- Never commit `.venv/`, `.ipynb_checkpoints/`, `__pycache__/` or large data files.
- Never rewrite history (`push --force`) on the shared branch.

---

## 12. Environment

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Base `requirements.txt`: `numpy`, `scipy`, `pandas`, `matplotlib`, `seaborn`, `plotly`, `jupyter`, `nbformat`, `nbconvert`, `ipykernel`, `kaleido` (optional, for static Plotly export).

---

## 13. When unsure

- A lesson is getting too big: split it, and update `plan.md`.
- A scope or design decision is needed that this file doesn't cover: choose the option that keeps code readable and HTML light, note the decision in the module `README.md`, and mention it in your final summary to the user.
