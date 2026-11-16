"""Download the datasets used in Module 03. Run: python module_03_multivariate/data/download_data.py"""
import pathlib
import urllib.request

DATA_DIR = pathlib.Path(__file__).resolve().parent
FILES = {
    # Lesson 03_03: Old Faithful geyser eruptions (the "geyser" dataset shipped with seaborn)
    "geyser.csv": ["https://raw.githubusercontent.com/mwaskom/seaborn-data/master/geyser.csv"],
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
        print(f"{name}: saved {target.stat().st_size / 1024:.1f} KB")
        return
    raise RuntimeError(f"Could not download {name} from any source")


if __name__ == "__main__":
    for file_name, file_urls in FILES.items():
        download(file_name, file_urls)
