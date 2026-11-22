"""Build the book front matter from the module folders: index.html (table of contents with search) and glossary.html (all terms).

Run from the repository root:  python tools/build_book.py
Reads  module_*/html/*.html (lesson titles) and module_*/glossary.md (terms); writes index.html and glossary.html.
Both outputs are single self-contained files that work by double-clicking (no fetch of local files).
"""
import html
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent

# (id, folder or None for planned, title, one-line description)
MODULES = [
    ("0a", "module_0a_basics", "Basics layer (start here if probability is new)",
     "From zero: events and the sample space, counting, the rules of probability, conditional probability, trees and a first look at Bayes, and random variables."),
    ("00", "module_00_foundations", "Foundations",
     "Random variables (PMF, PDF, CDF), expectation and moments, joint and conditional distributions, transformations, Bayes' theorem."),
    ("01", "module_01_discrete", "Discrete distributions",
     "Bernoulli, Binomial, Geometric, Negative Binomial, Poisson, Hypergeometric, Multinomial, Zipf, and how to choose between them."),
    ("02", "module_02_continuous", "Continuous distributions",
     "Normal, Lognormal, Exponential and Gamma, Beta, Weibull, heavy tails, Laplace, Logistic, Gumbel, t, chi-square, F and von Mises."),
    ("03", "module_03_multivariate", "Multivariate distributions",
     "Multivariate Normal, Dirichlet, Gaussian mixtures with EM, and copulas."),
    ("04", "module_04_relationships", "Relationships between distributions",
     "The family tree of distributions, limits and approximations."),
    ("05", "module_05_sampling", "Sampling and limit theorems",
     "Law of large numbers, central limit theorem (and its role in AI), standard errors, bootstrap, concentration inequalities, delta method, extremes, sampling designs."),
    ("06", "module_06_inference", "Statistical inference",
     "Estimation (moments and maximum likelihood), confidence intervals, hypothesis tests, power, common tests; nonparametric tests, multiple testing and A/B testing."),
    ("07", None, "Bayesian thinking", "Planned."),
    ("08", None, "Information theory", "Planned."),
    ("09", None, "Distributions inside ML and AI", "Planned."),
    ("10", None, "Model evaluation and the confusion matrix", "Planned."),
    ("11", None, "Data science in practice", "Planned."),
    ("12", None, "Sampling algorithms", "Planned."),
    ("13", None, "Capstone projects", "Planned."),
]

IN_PROGRESS = set()   # modules shown with the badge "in progress" instead of "done"

CSS = """
:root { --bg:#fff; --panel:#f6f7f9; --text:#1b1f24; --muted:#5b636d; --border:#d8dce1; --main:#0072B2; --hit:#fff3cd; }
@media (prefers-color-scheme: dark) {
  :root { --bg:#14171a; --panel:#1d2126; --text:#e8eaed; --muted:#9aa3ad; --border:#343a41; --main:#56B4E9; --hit:#3a3320; }
}
* { box-sizing: border-box; }
body { margin:0; background:var(--bg); color:var(--text); font:16px/1.55 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif; }
main { max-width:960px; margin:0 auto; padding:24px 16px 48px; }
h1 { margin:0 0 4px; }
.muted { color:var(--muted); }
.module { background:var(--panel); border:1px solid var(--border); border-radius:10px; padding:12px 16px; margin:12px 0; }
.module h2 { font-size:1.1rem; margin:0 0 6px; }
.module p { margin:2px 0 6px; color:var(--muted); font-size:0.92rem; }
.module ul { margin:6px 0 0; padding-left:20px; }
.module a, a.link { color:var(--main); text-decoration:none; font-weight:600; }
.module a:hover, a.link:hover { text-decoration:underline; }
.module.todo { opacity:0.5; }
.badge { font-size:0.75rem; border:1px solid var(--border); border-radius:99px; padding:1px 8px; margin-left:8px; color:var(--muted); font-weight:400; }
.bar { display:flex; flex-wrap:wrap; gap:8px 12px; align-items:center; margin:12px 0; }
input[type=search], select { padding:8px 10px; background:var(--bg); color:var(--text); border:1px solid var(--border); border-radius:8px; font:inherit; }
input[type=search] { flex:1 1 260px; }
.card { background:var(--panel); border:1px solid var(--border); border-radius:10px; padding:10px 14px; margin:10px 0; }
.hit { background:var(--hit); border-radius:3px; }
.paths { display:grid; grid-template-columns:repeat(auto-fit,minmax(260px,1fr)); gap:10px; margin:12px 0; }
.paths .card { margin:0; }
#results { display:none; }
#results li { margin:2px 0; }
.letter { font-size:1.2rem; margin:18px 0 4px; border-bottom:1px solid var(--border); }
.entry { padding:6px 0; border-bottom:1px solid var(--border); }
.entry .term { font-weight:700; }
.entry .where { font-size:0.85rem; color:var(--muted); }
.entry:target { background:var(--hit); }
nav.top a { margin-right:14px; }
"""


def split_row(line):
    parts = re.split(r"(?<!\\)\|", line.strip())
    parts = [p.strip().replace("\\|", "|") for p in parts[1:-1]]
    return parts


def read_lessons(folder):
    out = []
    for page in sorted((ROOT / folder / "html").glob("*.html")):
        text = page.read_text(encoding="utf-8")
        m = re.search(r"<h1>(.*?)</h1>", text, re.S)
        title = html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip() if m else page.stem
        out.append({"id": page.stem[:5], "title": title, "url": f"{folder}/html/{page.name}"})
    return out


def read_terms(mod_id, folder):
    g = ROOT / folder / "glossary.md"
    terms = []
    if not g.exists():
        return terms
    for line in g.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or line.startswith("|---") or line.startswith("| Term"):
            continue
        cells = split_row(line)
        if len(cells) != 3:
            continue
        link = re.search(r"\[(.+?)\]\((.+?)\)", cells[2])
        lesson_id, url = (link.group(1), f"{folder}/{link.group(2)}") if link else ("", "")
        terms.append({"term": cells[0], "def": cells[1], "lesson": lesson_id, "url": url, "module": mod_id})
    return terms


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def build_index(modules_data, search_items):
    blocks = []
    for mid, folder, title, desc, lessons in modules_data:
        if folder and lessons:
            items = "\n".join(f'<li><a href="{l["url"]}">{html.escape(l["title"])}</a></li>' for l in lessons)
            blocks.append(f'<div class="module" id="module-{mid}"><h2>Module {mid.upper()}. {html.escape(title)} <span class="badge">{"in progress" if mid in IN_PROGRESS else "done"}</span></h2>\n<p>{html.escape(desc)}</p><ul>\n{items}\n</ul></div>')
        else:
            blocks.append(f'<div class="module todo"><h2>Module {mid}. {html.escape(title)} <span class="badge">planned</span></h2></div>')
    n_lessons = sum(len(m[4]) for m in modules_data)
    n_terms = len([s for s in search_items if s["kind"] == "term"])
    data = json.dumps(search_items, ensure_ascii=False, separators=(",", ":"))
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Probability Distributions Book</title>
<style>{CSS}</style>
</head>
<body>
<main>
<h1>Probability Distributions Book</h1>
<p class="muted">How distributions work, and how they are used in statistics, data science, ML and AI. Each lesson has a notebook and an interactive page. {n_lessons} lessons and {n_terms} glossary terms so far.</p>
<nav class="top"><a class="link" href="glossary.html">Glossary (all terms)</a></nav>

<div class="bar"><input type="search" id="q" placeholder="Search lessons and glossary terms (try: bayes, poisson, bootstrap, copula)" aria-label="Search"></div>
<div class="card" id="results"><strong id="count"></strong><ul id="list"></ul></div>

<div class="paths">
<div class="card"><strong>New to probability?</strong><br>Read in order: 0A, then 00, 01, 02, 03, 04, 05. Every lesson builds on the earlier ones.</div>
<div class="card"><strong>Know the basics?</strong><br>Start at Module 00, or jump to the choosers: <a class="link" href="module_01_discrete/html/01_07_discrete_summary_chooser.html">discrete</a>, <a class="link" href="module_02_continuous/html/02_10_continuous_summary_chooser.html">continuous</a> and the <a class="link" href="module_04_relationships/html/04_01_relationship_map.html">family tree</a>.</div>
<div class="card"><strong>Interested in AI?</strong><br>See the <a class="link" href="module_05_sampling/html/05_02_central_limit_theorem.html">CLT in machine learning</a>, <a class="link" href="module_03_multivariate/html/03_03_gaussian_mixtures.html">mixtures and EM</a> and <a class="link" href="module_0a_basics/html/0a_05_trees_total_probability.html">Bayes and precision</a>.</div>
</div>

<!-- Generated by tools/build_book.py from the module folders; edit the script, not this file. -->
{chr(10).join(blocks)}
</main>
<script>
"use strict";
const ITEMS = {data};
const q = document.getElementById("q"), box = document.getElementById("results"), list = document.getElementById("list"), count = document.getElementById("count");
function esc(s) {{ return s.replace(/[&<>]/g, c => ({{ "&": "&amp;", "<": "&lt;", ">": "&gt;" }}[c])); }}
function mark(s, words) {{ let t = esc(s); for (const w of words) t = t.replace(new RegExp("(" + w.replace(/[.*+?^${{}}()|[\\]\\\\]/g, "\\\\$&") + ")", "ig"), '<span class="hit">$1</span>'); return t; }}
function search() {{
  const words = q.value.toLowerCase().split(/\\s+/).filter(w => w);
  if (!words.length) {{ box.style.display = "none"; return; }}
  const hits = ITEMS.filter(it => words.every(w => it.text.toLowerCase().includes(w))).slice(0, 60);
  box.style.display = "block"; count.textContent = hits.length ? hits.length + (hits.length === 60 ? "+" : "") + " matches" : "No matches";
  list.innerHTML = hits.map(it => it.kind === "lesson"
    ? '<li>Lesson: <a class="link" href="' + it.url + '">' + mark(it.text, words) + "</a></li>"
    : '<li>Term: <a class="link" href="glossary.html#' + it.slug + '">' + mark(it.term, words) + '</a> <span class="muted">(' + esc(it.lesson) + ")</span></li>").join("");
}}
q.addEventListener("input", search);
</script>
</body>
</html>
"""


def build_glossary(all_terms, module_titles):
    all_terms = sorted(all_terms, key=lambda t: t["term"].lower())
    seen = {}
    entries, letters = [], {}
    for t in all_terms:
        s = slug(t["term"])
        seen[s] = seen.get(s, 0) + 1
        t["slug"] = s if seen[s] == 1 else f"{s}-{seen[s]}"
        first = t["term"][0].upper() if t["term"][0].isalpha() else "#"
        letters.setdefault(first, []).append(t)
    body = []
    for letter in sorted(letters):
        body.append(f'<h2 class="letter" id="letter-{letter}">{letter}</h2>')
        for t in letters[letter]:
            link = f'<a class="link" href="{t["url"]}">{html.escape(t["lesson"])}</a>' if t["url"] else ""
            body.append(f'<div class="entry" id="{t["slug"]}" data-module="{t["module"]}"><span class="term">{html.escape(t["term"])}</span>: {html.escape(t["def"])} '
                        f'<div class="where">Module {t["module"].upper()}, lesson {link}</div></div>')
    options = "".join(f'<option value="{m}">Module {m.upper()}: {html.escape(module_titles[m])}</option>' for m in module_titles)
    jump = " ".join(f'<a class="link" href="#letter-{l}">{l}</a>' for l in sorted(letters))
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Glossary | Probability Distributions Book</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>
<style>{CSS}</style>
</head>
<body>
<main>
<nav class="top"><a class="link" href="index.html">Book index</a></nav>
<h1>Glossary</h1>
<p class="muted">{len(all_terms)} terms from all modules. Each links to the lesson that introduces it.</p>
<div class="bar"><input type="search" id="q" placeholder="Filter terms and definitions" aria-label="Filter"><select id="mod"><option value="">All modules</option>{options}</select><span id="shown" class="muted"></span></div>
<p>{jump}</p>
{chr(10).join(body)}
</main>
<script>
"use strict";
const entries = Array.from(document.querySelectorAll(".entry")), letters = Array.from(document.querySelectorAll(".letter"));
const q = document.getElementById("q"), mod = document.getElementById("mod"), shown = document.getElementById("shown");
function apply() {{
  const words = q.value.toLowerCase().split(/\\s+/).filter(w => w); let n = 0;
  for (const e of entries) {{ const ok = (!mod.value || e.dataset.module === mod.value) && words.every(w => e.textContent.toLowerCase().includes(w)); e.style.display = ok ? "" : "none"; if (ok) n++; }}
  for (const h of letters) {{ let sib = h.nextElementSibling, any = false; while (sib && !sib.classList.contains("letter")) {{ if (sib.style.display !== "none") any = true; sib = sib.nextElementSibling; }} h.style.display = any ? "" : "none"; }}
  shown.textContent = n + " shown";
}}
q.addEventListener("input", apply); mod.addEventListener("change", apply); apply();
window.addEventListener("DOMContentLoaded", () => {{ if (window.renderMathInElement) renderMathInElement(document.body, {{ delimiters: [{{ left: "$$", right: "$$", display: true }}, {{ left: "$", right: "$", display: false }}] }}); }});
</script>
</body>
</html>
"""


def main():
    modules_data, search_items, all_terms, titles = [], [], [], {}
    for mid, folder, title, desc in MODULES:
        lessons = read_lessons(folder) if folder else []
        modules_data.append((mid, folder, title, desc, lessons))
        if folder:
            titles[mid] = title
            for l in lessons:
                search_items.append({"kind": "lesson", "text": l["title"], "url": l["url"]})
            all_terms.extend(read_terms(mid, folder))
    glossary = build_glossary(all_terms, titles)
    for t in all_terms:
        search_items.append({"kind": "term", "text": t["term"] + " " + t["def"], "term": t["term"], "slug": t["slug"], "lesson": t["lesson"]})
    (ROOT / "glossary.html").write_text(glossary, encoding="utf-8")
    (ROOT / "index.html").write_text(build_index(modules_data, search_items), encoding="utf-8")
    print(f"index.html: {sum(len(m[4]) for m in modules_data)} lessons; glossary.html: {len(all_terms)} terms")


if __name__ == "__main__":
    main()
