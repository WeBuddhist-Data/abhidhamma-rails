# -*- coding: utf-8 -*-
"""Extra checks for chapters 8 and 18: Latin-script words outside variant brackets, CR, double blank lines,
'—', ':-', the words 'seed'/'unseeded', and identical Pāli lines -> identical Hindi lines.

usage: python -I -X utf8 extra_checks_ch8_ch18.py <chapter>.md
"""
import os, re, sys
from collections import defaultdict

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
P = os.path.join(ROOT, r"AI_translation\pali\pi-2_split_chapters", sys.argv[1])
H = os.path.join(ROOT, r"AI_translation\hindi\pi-2-hindi-plain-zeroshot_split_chapters", sys.argv[1])
raw = open(H, encoding="utf-8", newline="").read()
errs = []
if "\r" in raw:
    errs.append("CR")
if "\n\n\n" in raw:
    errs.append("double blank line")
if "—" in raw or ":-" in raw:
    errs.append("em dash or ':-'")
if re.search(r"(?i)\b(un)?seeded?\b", raw):
    errs.append("'seed' word")
ID = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")
for i, line in enumerate(raw.splitlines(), 1):
    t = ID.sub("", line)
    t = re.sub(r"\[[^\]]*\]", "", t)
    lat = re.findall(r"[A-Za-zĀāĪīŪūṄṅÑñṬṭḌḍṆṇḶḷṂṃ]+", t)
    if lat:
        errs.append(f"line {i}: Latin {lat[:5]}")
# identical Pāli -> identical Hindi (non-empty lines, IDs removed)
pl = [ID.sub("", l) for l in open(P, encoding="utf-8-sig").read().splitlines() if l.strip()]
hl = [ID.sub("", l) for l in raw.splitlines() if l.strip()]
m = defaultdict(set)
for a, b in zip(pl, hl):
    m[a].add(b)
for a, bs in m.items():
    if len(bs) > 1:
        errs.append(f"identical Pāli, different Hindi: {a[:60]}…")
print(sys.argv[1], "extra checks", "OK" if not errs else "ERRORS")
for e in errs[:30]:
    print("  ", e)
sys.exit(1 if errs else 0)
