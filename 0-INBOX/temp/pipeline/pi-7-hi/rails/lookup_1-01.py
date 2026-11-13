"""Termbase entries for 1-01 words.
usage: python -I -B -X utf8 lookup_1-01.py new        (distinct words of 1-01 not in the sample Pāli files)
       python -I -B -X utf8 lookup_1-01.py w1 w2 ...  (given words; prefix 're:' for a regex over headwords)"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..", "..", "..", "..")
TB = os.path.join(ROOT, "AI_translation", "hindi", "pi-7-pali-hindi-termbase-plain.md")
SRC = os.path.join(ROOT, "AI_translation", "pali", "pi-7_split_chapters", "1-01-kusalattika.md")
TOK = re.compile(r"[A-Za-zāīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶ]+")

tb = {}
for line in open(TB, encoding="utf-8").read().splitlines():
    if ": {" in line:
        w, body = line.split(": {", 1)
        tb[w] = body[:-1]
ci = {}
for k, v in tb.items():
    ci.setdefault(k.lower(), v)

args = sys.argv[1:]
if args == ["new"]:
    known = set()
    for f in ("1-01-a-pali-sample.md", "1-01-b-pali-sample.md"):
        known |= {t.lower() for t in TOK.findall(open(os.path.join(HERE, "sample-1", f), encoding="utf-8").read())}
    known |= {t.lower() for t in TOK.findall(open(os.path.join(ROOT, "AI_translation", "pali", "pi-7_split_chapters",
                                                              "1-00-paccaya.md"), encoding="utf-8").read())}
    text = re.sub(r"\^[0-9A-Za-z-]+", " ", open(SRC, encoding="utf-8").read())
    seen = []
    for t in TOK.findall(text):
        if t.lower() not in known and t.lower() not in [s.lower() for s in seen]:
            seen.append(t)
    words = seen
else:
    words = args
for t in words:
    if t.startswith("re:"):
        rx = re.compile(t[3:])
        for k, v in tb.items():
            if rx.search(k):
                print(f"{k}: {v}")
        continue
    e = tb.get(t) or ci.get(t.lower())
    print(f"{t}: {e if e else '-'}")
