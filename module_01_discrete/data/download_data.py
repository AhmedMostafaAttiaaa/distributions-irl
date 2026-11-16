"""Download the datasets used in Module 01.

Run from anywhere:  python module_01_discrete/data/download_data.py
Files are saved next to this script. Existing files are kept.
"""
import pathlib
import urllib.request

DATA_DIR = pathlib.Path(__file__).resolve().parent

FILES = {
    # Lesson 01_03: English Premier League 2023/24 match results
    "E0_2324.csv": "https://www.football-data.co.uk/mmz4281/2324/E0.csv",
}


def download(name, url):
    target = DATA_DIR / name
    if target.exists():
        print(f"{name}: already present, skipping")
        return
    print(f"{name}: downloading from {url}")
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=60) as response:
        target.write_bytes(response.read())
    print(f"{name}: saved {target.stat().st_size / 1024:.0f} KB")


if __name__ == "__main__":
    for file_name, file_url in FILES.items():
        download(file_name, file_url)
