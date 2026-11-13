import re, sys, os
from collections import OrderedDict
sys.path.insert(0, os.path.dirname(__file__))
from review_r1_common import *

f = sys.argv[1] if len(sys.argv) > 1 else "1-01-kusalattika.md"
seen = OrderedDict()
for n, sid, p, h in pairs(f):
    pn = re.findall(r"\(([^()]*[a-zāīū]{4,}[^()]*)\)", p)
    hn = re.findall(r"\(([^()]*[ऀ-ॿ]{2,}[^()]*)\)", h)
    pn = [x for x in pn if not re.fullmatch(r"\s*(sa|a)vipākaṃ – \d+\s*", x, re.I)]
    hn = [x for x in hn if not re.search(r"कर्म-फल-कारण (सहित|रहित) – \d+", x)]
    if len(pn) != len(hn):
        print(f"COUNT n={n} {sid} P{len(pn)} H{len(hn)}")
    for a, b in zip(pn, hn):
        seen.setdefault(a.strip(), OrderedDict()).setdefault(b.strip(), []).append(n)
for a, d in seen.items():
    for b, ns in d.items():
        print(f"n={ns[:3]}x{len(ns)} | {a} | {b}")
