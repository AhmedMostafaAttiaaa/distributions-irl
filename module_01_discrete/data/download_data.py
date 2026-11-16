"""Download the datasets used in Module 01.

Run from anywhere:  python module_01_discrete/data/download_data.py
Files are saved next to this script. Existing files are kept.
"""
import pathlib
import urllib.request

DATA_DIR = pathlib.Path(__file__).resolve().parent

FILES = {
    # Lesson 01_03: English Premier League 2023/24 match results
    "E0_2324.csv": ["https://www.football-data.co.uk/mmz4281/2324/E0.csv"],
    # Lesson 01_06: Pride and Prejudice by Jane Austen (Project Gutenberg ebook 1342, public domain).
    # The www.gutenberg.org site is sometimes down for maintenance, so an official mirror is tried first.
    "pride_and_prejudice.txt": [
        "https://gutenberg.pglaf.org/1/3/4/1342/1342-0.txt",
        "https://www.gutenberg.org/cache/epub/1342/pg1342.txt",
    ],
}


def download(name, urls):
    """Try each URL in turn and save the first one that works."""
    target = DATA_DIR / name
    if target.exists():
        print(f"{name}: already present, skipping")
        return
    for url in urls:
        print(f"{name}: downloading from {url}")
        request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                target.write_bytes(response.read())
        except Exception as error:
            print(f"  failed: {error}")
            continue
        print(f"{name}: saved {target.stat().st_size / 1024:.0f} KB")
        return
    raise RuntimeError(f"Could not download {name} from any source")


if __name__ == "__main__":
    for file_name, file_urls in FILES.items():
        download(file_name, file_urls)
