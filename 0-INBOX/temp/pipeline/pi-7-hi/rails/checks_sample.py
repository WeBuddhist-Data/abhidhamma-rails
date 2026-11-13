"""Run every brief check on the sample outputs (no files written).
usage (repo root): python -I -B -X utf8 0-INBOX\\temp\\pipeline\\pi-7-hi\\rails\\checks_sample.py"""
import collections
import pathlib
import re
import subprocess
import sys

R = pathlib.Path("0-INBOX/temp/pipeline/pi-7-hi/rails")
PALI = pathlib.Path("AI_translation/pali/pi-7_split_chapters")
OUT = pathlib.Path("AI_translation/hindi/pi-7-hindi-plain-rails_split_chapters")
PAIRS = [(PALI / "preamble.md", OUT / "preamble.md"), (PALI / "1-00-paccaya.md", OUT / "1-00-paccaya.md"),
         (R / "sample-1/1-01-a-pali-sample.md", R / "sample-1/1-01-a-sample.md"),
         (R / "sample-1/1-01-b-pali-sample.md", R / "sample-1/1-01-b-sample.md")]
PY = [sys.executable, "-I", "-X", "utf8"]


def run(args):
    r = subprocess.run(PY + args, capture_output=True, text=True, encoding="utf-8")
    print(r.stdout.strip() or r.stderr.strip())


print("== check_chapter_ids")
run(["0-INBOX/temp/pipeline/check_chapter_ids.py", str(PALI), str(OUT), "preamble.md", "1-00-paccaya.md"])
for p, h in PAIRS:
    print(f"== {h.name}")
    run(["0-INBOX/temp/pipeline/pi-1-en/dashcheck.py", str(p), str(h)])
    run(["0-INBOX/temp/pipeline/pi-1-hi/verify_hi.py", str(p), str(h)])
    t = h.read_text(encoding="utf-8")
    print("double blank:", "\n\n\n" in t, "| CR:", "\r" in t, "| em/en dash total:", t.count("—"), t.count("–"),
          "pali:", p.read_text(encoding="utf-8").count("–") + p.read_text(encoding="utf-8").count("—"))
    nob = re.sub(r"\[[^\]]*\]", "", t)
    latin = [w for w in re.findall(r"[A-Za-zĀāĪīŪūṂṃṄṅÑñṬṭḌḍṆṇḶḷ]{2,}", nob)]
    print("latin outside brackets:", collections.Counter(latin).most_common(10))
    print("':-' :", ":-" in t, "| …pe… :", "pe…" in t, "| ascii quotes:", '"' in t)
