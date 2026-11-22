"""r3: headings, closing lines, (…mūlakaṃ) tags, answer-only lines and Tadekaṭṭha lines, side by side. Console only."""
import re, sys
from collections import Counter
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\review")
import r3_check as C

tags = Counter()
short = Counter()
for fn in C.FILES:
    P, V = C.lines(C.PI + fn), C.lines(C.VI + fn)
    for i, (p, v) in enumerate(zip(P, V)):
        if p.startswith("#") or (("vāre" in p or "vāro" in p) and "?" not in p):
            print(fn, i, "|", p, "||", v)
        for a, b in zip(re.findall(r"\((\w+mūlakaṃ)\)", p), re.findall(r"\((Phần[^)]*)\)", v)):
            tags[(a, b)] += 1
        if "?" not in p and len(p) < 60 and not p.startswith("#"):
            short[(C.ID_RE.sub("", p), C.ID_RE.sub("", v))] += 1
for k, n in sorted(tags.items()):
    print(n, k)
for k, n in sorted(short.items()):
    print(n, k)
