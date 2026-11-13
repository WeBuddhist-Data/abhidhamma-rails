import re, sys, os
from collections import Counter, OrderedDict
sys.path.insert(0, os.path.dirname(__file__))
from review_r1_common import *
src = open(os.path.join(os.path.dirname(__file__), "review_r1_check.py"), encoding="utf-8-sig").read().split("res = {")[0]
g = {"__file__": os.path.join(os.path.dirname(__file__), "review_r1_check.py")}
exec(src, g)
PRE0, HRE = g["PRE0"], g["HRE"]
PL = g["PL"]
NUMP = re.compile(r"(?<![" + PL + r"])(ekaṃ|eko|dve|tayo|tīṇi|cattāri|pañca|cha|satta|aṭṭha|nava|dasa|ekādasa|dvādasa|terasa|cuddasa|pannarasa|soḷasa|sattarasa|aṭṭhārasa)(?![" + PL + r"])")
NUMH = re.compile(r"(?<![ऀ-ॣ०-ॿ-])(एक|दो|तीन|चार|पाँच|छह|सात|आठ|नौ|दस|ग्यारह|बारह|तेरह|चौदह|पंद्रह|सोलह|सत्रह|अठारह)(?![ऀ-ॣ०-ॿ-])")

def np_(p):
    q = p.lower()
    q = re.sub(r"\s*\^[\w-]+\s*$", "", q)
    q = PRE0.sub("<C>", q)
    q = NUMP.sub("<N>", q)
    q = re.sub(r"\(\d+\)", "(#)", q)
    return q

def nh_(h):
    q = re.sub(r"\s*\^[\w-]+\s*$", "", h)
    q = HRE.sub("<C>", q)
    q = NUMH.sub("<N>", q)
    q = re.sub(r"\(\d+\)", "(#)", q)
    return q

f = "1-01-kusalattika.md"
groups = OrderedDict()
for n, sid, p, h in pairs(f):
    if p.startswith("#"):
        continue
    # split into sentences to get finer templates
    ps = [s for s in re.split(r"(?<=[.?])\s+", np_(p)) if s]
    hs = [s for s in re.split(r"(?<=[।?])\s+", nh_(h)) if s]
    if len(ps) != len(hs):
        groups.setdefault(("LINE", np_(p)), {}).setdefault(nh_(h), []).append(n)
        continue
    for a, b in zip(ps, hs):
        groups.setdefault(("S", a), {}).setdefault(b, []).append(n)
incons = [(k, v) for k, v in groups.items() if len(v) > 1]
with open(os.path.join(OUT, "review_r1_templ_out.txt"), "w", encoding="utf-8") as fh:
    for (t, k), v in incons:
        fh.write(f"=== [{t}] {k}\n")
        for hk, ns in v.items():
            fh.write(f"   n={ns[:6]} ({len(ns)}) :: {hk}\n")
with open(os.path.join(OUT, "review_r1_templ_uniq.txt"), "w", encoding="utf-8") as fh:
    for (t, k), v in groups.items():
        hk, ns = next(iter(v.items()))
        fh.write(f"[{t}] n={ns[0]} x{sum(len(x) for x in v.values())}\nP: {k}\nH: {hk}\n")
print("templates", len(groups), "inconsistent", len(incons))
