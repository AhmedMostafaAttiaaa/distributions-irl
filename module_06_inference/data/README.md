# Data for Module 06

Lessons 06_01 to 06_06 use no external data: every example is a small table in the notebook or random numbers from a seeded generator (`numpy.random.default_rng(42)`).

## Lesson 06_07: Cookie Cats A/B test

| Item | Value |
|---|---|
| File | `cookie_cats.csv` (90,189 rows, 5 columns, 2.7 MB) |
| What it is | A real mobile-game A/B test: when the first progression gate of the puzzle game *Cookie Cats* (Tactile Games) was moved from level 30 to level 40, did players come back? |
| Original source | Tactile Games / DataCamp (also circulated on Kaggle as "Mobile Games A/B Testing - Cookie Cats") |
| Copy downloaded from | https://raw.githubusercontent.com/ryanschaub/Mobile-Games-A-B-Testing-with-Cookie-Cats/master/cookie_cats.csv |
| Download date | 2026-11-22 |
| License | No license is stated in the GitHub copy. The data is public and widely used for teaching; it is included here unmodified for educational use only. Re-download with `download_data.py` rather than redistributing it elsewhere. |

Columns:

| Column | Meaning |
|---|---|
| `userid` | unique player id (anonymised) |
| `version` | `gate_30` (control) or `gate_40` (treatment), assigned at random at installation |
| `sum_gamerounds` | rounds played in the first 14 days after installation |
| `retention_1` | `True` if the player came back one day after installation |
| `retention_7` | `True` if the player came back seven days after installation |

Checks used in the lesson: 44,700 players in `gate_30` and 45,489 in `gate_40`; user ids are unique; one outlier player has 49,854 rounds.

To re-download: `python module_06_inference/data/download_data.py`.
