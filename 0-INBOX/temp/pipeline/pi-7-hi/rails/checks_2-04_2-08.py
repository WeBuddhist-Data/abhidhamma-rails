"""Run the brief's checks on 2-04 .. 2-08 (no files written).
usage (repo root): python -I -B -X utf8 0-INBOX\\temp\\pipeline\\pi-7-hi\\rails\\checks_2-04_2-08.py"""
import collections
import pathlib
import re
import subprocess
import sys

PALI = pathlib.Path("AI_translation/pali/pi-7_split_chapters")
OUT = pathlib.Path("AI_translation/hindi/pi-7-hindi-plain-rails_split_chapters")
FILES = ["2-04-dassanenapahatabbahetukattika.md", "2-05-acayagamittika.md", "2-06-sekkhattika.md",
         "2-07-parittattika.md", "2-08-parittarammanattika.md"]
PY = [sys.executable, "-I", "-X", "utf8"]


def run(args):
    r = subprocess.run(PY + args, capture_output=True, text=True, encoding="utf-8")
    return (r.stdout.strip() or r.stderr.strip())


for f in FILES:
    p, h = PALI / f, OUT / f
    print(f"== {f}")
    print(run(["0-INBOX/temp/pipeline/check_chapter_ids.py", str(PALI), str(OUT), f])[-300:])
    print(run(["0-INBOX/temp/pipeline/pi-1-en/dashcheck.py", str(p), str(h)])[-300:])
    v = run(["0-INBOX/temp/pipeline/pi-1-hi/verify_hi.py", str(p), str(h)])
    print("verify_hi:", v[-1500:] if "-v" in sys.argv else v[-400:])
    t = h.read_text(encoding="utf-8")
    nob = re.sub(r"\[[^\]]*\]", "", t)
    latin = re.findall(r"[A-Za-zĀāĪīŪūṂṃṄṅÑñṬṭḌḍṆṇḶḷ]{2,}", re.sub(r"\^[0-9A-Za-z-]+", "", nob))
    print("double blank:", "\n\n\n" in t, "| CR:", "\r" in t, "| ⁇:", "⁇" in t, "| ':-':", ":-" in t,
          "| ascii quote:", '"' in t, "| latin:", collections.Counter(latin).most_common(8))
