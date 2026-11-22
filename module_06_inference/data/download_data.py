"""Download the Cookie Cats A/B test data used by lesson 06_07 (see README.md in this folder)."""
import pathlib
import urllib.request

URL = "https://raw.githubusercontent.com/ryanschaub/Mobile-Games-A-B-Testing-with-Cookie-Cats/master/cookie_cats.csv"
OUT = pathlib.Path(__file__).with_name("cookie_cats.csv")

if __name__ == "__main__":
    urllib.request.urlretrieve(URL, OUT)
    print(f"saved {OUT} ({OUT.stat().st_size:,} bytes)")
