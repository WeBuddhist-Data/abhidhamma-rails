"""Termbase entries for every distinct Pāli word in files 2-04..2-08 (first-seen order) -> lookup_2-04_2-08.txt.
usage (repo root): python -I -B -X utf8 0-INBOX\\temp\\pipeline\\pi-7-hi\\rails\\lookup_2-04_2-08.py"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lookup_sample as L  # noqa: E402

ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", ".."))
PALI = os.path.join(ROOT, "AI_translation", "pali", "pi-7_split_chapters")
TB = os.path.join(ROOT, "AI_translation", "hindi", "pi-7-pali-hindi-termbase-plain.md")
FILES = ["2-04-dassanenapahatabbahetukattika.md", "2-05-acayagamittika.md", "2-06-sekkhattika.md",
         "2-07-parittattika.md", "2-08-parittarammanattika.md"]
# words already fixed by the sample builder / formulas file: skip them to keep the list short
SKIP = set()

tb = L.load(TB)
ci = {k.lower(): v for k, v in tb.items()}
seen = []
for f in FILES:
    text = open(os.path.join(PALI, f), encoding="utf-8").read()
    text = re.sub(r"\^[0-9A-Za-z-]+", " ", text)
    for t in L.TOK.findall(text):
        if t not in seen:
            seen.append(t)
out = []
for t in seen:
    e = tb.get(t) or ci.get(t.lower())
    out.append(f"{t}: {e}" if e else f"{t}: -")
open(os.path.join(HERE, "lookup_2-04_2-08.txt"), "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
print(len(seen), "words;", sum(1 for o in out if o.endswith(": -")), "missing")
