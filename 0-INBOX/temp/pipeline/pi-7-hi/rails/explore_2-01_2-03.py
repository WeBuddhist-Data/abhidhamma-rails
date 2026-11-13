"""Explore helper for 2-01..2-03: print distinct clauses (items masked) with counts."""
import re
import sys
from collections import Counter

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
f = sys.argv[1]
mode = sys.argv[2] if len(sys.argv) > 2 else "clauses"
txt = open(rf"{ROOT}\AI_translation\pali\pi-7_split_chapters\{f}", encoding="utf-8").read()
ITEMS = [
    ("savitakkasavicār", "SV"), ("avitakkavicāramatt", "VM"), ("avitakkaavicār", "AV"),
    ("pītisahagat", "PI"), ("sukhasahagat", "SU"), ("upekkhāsahagat", "UP"),
    ("nevadassanena nabhāvanāya pahātabb", "NN"), ("neva dassanena na bhāvanāya pahātabb", "NN"),
    ("dassanena pahātabb", "DA"), ("bhāvanāya pahātabb", "BH"),
]
c = Counter()
for ln in txt.split("\n"):
    ln = re.sub(r" \^[\w-]+$", "", ln.strip())
    if not ln or ln.startswith("#"):
        if ln and mode == "heads":
            c[ln] += 1
        continue
    if mode == "heads":
        continue
    s = ln
    for a, b in ITEMS:
        s = re.sub(a, b, s, flags=re.I)
    for piece in re.split(r" – |; |, |\. |…pe…|…|\.$| \(\d+\)", s):
        piece = piece.strip(" .")
        if piece:
            c[piece] += 1
for k, v in sorted(c.items(), key=lambda kv: kv[0]):
    print(v, k)
