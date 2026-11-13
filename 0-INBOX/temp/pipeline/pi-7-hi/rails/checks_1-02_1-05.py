"""Run the brief's checks on 1-02..1-05 (no files written).
usage (repo root): python -I -B -X utf8 0-INBOX\\temp\\pipeline\\pi-7-hi\\rails\\checks_1-02_1-05.py"""
import collections
import pathlib
import re
import subprocess
import sys

PALI = pathlib.Path("AI_translation/pali/pi-7_split_chapters")
OUT = pathlib.Path("AI_translation/hindi/pi-7-hindi-plain-rails_split_chapters")
FILES = ["1-02-vedanattika.md", "1-03-vipakattika.md", "1-04-upadinnattika.md", "1-05-sankilitthattika.md"]
PY = [sys.executable, "-I", "-X", "utf8"]


def run(args):
    r = subprocess.run(PY + args, capture_output=True, text=True, encoding="utf-8")
    out = (r.stdout.strip() or r.stderr.strip()).splitlines()
    print("\n".join(out[:25]) + (f"\n… ({len(out)} lines)" if len(out) > 25 else ""))


print("== check_chapter_ids")
run(["0-INBOX/temp/pipeline/check_chapter_ids.py", str(PALI), str(OUT)] + FILES)
for f in FILES:
    p, h = PALI / f, OUT / f
    print(f"== {f}")
    run(["0-INBOX/temp/pipeline/pi-1-en/dashcheck.py", str(p), str(h)])
    run(["0-INBOX/temp/pipeline/pi-1-hi/verify_hi.py", str(p), str(h)])
    t = h.read_text(encoding="utf-8")
    print("double blank:", "\n\n\n" in t, "| CR:", "\r" in t, "| control/markers:",
          len(re.findall("[\x00-\x08\x0b-\x1f@§‹›?]", t.replace("?", ""))), "| ??? :", t.count("???"))
    nob = re.sub(r"\[[^\]]*\]", "", t)
    nob = re.sub(r"\^[\w-]+", "", nob)
    latin = re.findall(r"[A-Za-zĀāĪīŪūṂṃṄṅÑñṬṭḌḍṆṇḶḷ]{2,}", nob)
    print("latin outside brackets:", collections.Counter(latin).most_common(10))
    print("':-' :", ":-" in t, "| pe… :", "pe…" in t, "| ascii quotes:", '"' in t, "| em dash:", t.count("—"))
