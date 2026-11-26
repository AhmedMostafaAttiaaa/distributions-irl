"""Download the SMS Spam Collection (UCI, CC BY 4.0) into this folder."""
import io, pathlib, urllib.request, zipfile
URL = "https://archive.ics.uci.edu/static/public/228/sms+spam+collection.zip"
out = pathlib.Path(__file__).parent / "SMSSpamCollection.tsv"
with urllib.request.urlopen(URL) as r:
    z = zipfile.ZipFile(io.BytesIO(r.read()))
out.write_bytes(z.read("SMSSpamCollection"))
print("wrote", out, out.stat().st_size, "bytes")
