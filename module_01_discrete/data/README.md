# Module 01 data

All files can be recreated with `python download_data.py` (run from this folder or anywhere).

## E0_2324.csv: English Premier League 2023/24 results (lesson 01_03)

| Item | Value |
|---|---|
| Source | https://www.football-data.co.uk/mmz4281/2324/E0.csv (site: https://www.football-data.co.uk/englandm.php) |
| License | No formal license is published. The site offers the results for free use; this repo uses it for personal study only. |
| Download date | 2026-11-16 |
| Size | about 170 KB, 380 matches (one row per match) |

Columns used in the lesson: `HomeTeam`, `AwayTeam`, `FTHG` (full-time home goals), `FTAG` (full-time away goals). The file has many more columns (shots, cards, betting odds); see https://www.football-data.co.uk/notes.txt for the description of each.

## pride_and_prejudice.txt: Pride and Prejudice by Jane Austen (lesson 01_06)

| Item | Value |
|---|---|
| Source | Project Gutenberg ebook 1342, https://www.gutenberg.org/ebooks/1342 (downloaded from the official mirror https://gutenberg.pglaf.org/1/3/4/1342/1342-0.txt because www.gutenberg.org was down for maintenance) |
| License | Public domain in the United States; distributed under the Project Gutenberg License (https://www.gutenberg.org/policy/license.html). The header and footer in the file contain the license text. |
| Download date | 2026-11-16 |
| Size | about 720 KB, plain UTF-8 text, about 14,500 lines |

Plain text of the novel. The lesson removes everything before the line `*** START OF` and after `*** END OF`, lowercases the text, and extracts words with a regular expression. Result: 128,565 word tokens and 6,729 distinct words.
