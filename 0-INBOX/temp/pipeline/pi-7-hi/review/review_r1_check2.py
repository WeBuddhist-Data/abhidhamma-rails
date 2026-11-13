import re, sys, os
from collections import Counter
sys.path.insert(0, os.path.dirname(__file__))
from review_r1_common import *
import importlib.util
spec = importlib.util.spec_from_file_location("c1", os.path.join(os.path.dirname(__file__), "review_r1_check.py"))
# reuse definitions without running the main loop: exec only the top part
src = open(os.path.join(os.path.dirname(__file__), "review_r1_check.py"), encoding="utf-8-sig").read()
src = src.split("res = {")[0]
g = {"__file__": os.path.join(os.path.dirname(__file__), "review_r1_check.py")}
exec(src, g)
PRE, HRE, H2P, STEMS, PL = g["PRE"], g["HRE"], g["H2P"], g["STEMS"], g["PL"]
PNUM, HNUM, PNRE = g["PNUM"], g["HNUM"], g["PNRE"]
HNRE = re.compile(r"(?<![\u0900-\u0963\u0966-\u097F-])(" + "|".join(sorted(HNUM, key=len, reverse=True)) + r")(?![\u0900-\u0963\u0966-\u097F-])")

STEMS_L = sorted(STEMS, key=len, reverse=True)

def parse_compound(c):
    c = c.lower().replace("-", "").replace("hetādhipati", "hetuadhipati").replace("ādhipati", "aadhipati").replace("ūpanissaya", "aupanissaya")
    out = []
    i = 0
    while i < len(c):
        for s in STEMS_L:
            if c.startswith(s, i):
                out.append(s); i += len(s); break
        else:
            return None
    return out

def prep_p(p):
    def rep(m):
        st = parse_compound(m.group(1))
        if st is None:
            FAIL.append(m.group(0))
            return m.group(0)
        return " ".join(s + "paccayā" for s in st)
    p = re.sub(r"\((a|sa)vipākaṃ", "(vipākapaccayā", p, flags=re.I)
    p = re.sub(r" ?- ?", "-", p)
    p = re.sub(r"īti(?![a-zāīū])", "inti", p)
    p = re.sub(r"vippayuttaṃ-", "vippayutta-", p).replace("vipākaṃ-", "vipāka-")
    p = re.sub(r"(?<![a-zāīū])(na|no)?([A-Za-zĀāīūṃñṅṭḍṇḷ]+?)mūlak(aṃ|ā)", lambda m: (m.group(1) or "") + m.group(2) + "paccayā mūlakaṃ" if parse_compound(m.group(2)) else m.group(0), p)
    return re.sub(r"([A-Za-zĀāīūṃñṅṭḍṇḷ-]+?)nti(?![a-zāīū])", rep, p)
FAIL = []

def seq_p(p):
    return [(m.stem, "N" if m.neg else "P") for m in PRE.finditer(p.lower())]

def seq_h(h):
    return [(H2P[m.group(1)], "N" if m.group(2) else "P") for m in HRE.finditer(h)]

out = []
for f in FILES[1:]:
    for n, sid, p, h in pairs(f):
        if p.startswith("#"):
            continue
        pb = re.sub(r"\{[^}]*\}", "", p); hb = re.sub(r"\[[^\]]*\]", "", h)
        pb = re.sub(r"\^[\w-]+\s*$", "", pb); hb = re.sub(r"\^[\w-]+\s*$", "", hb)
        pp = prep_p(pb)
        a, b = seq_p(pp), seq_h(hb)
        if a != b:
            # find first divergence
            k = 0
            while k < min(len(a), len(b)) and a[k] == b[k]:
                k += 1
            out.append(f"COND {f} n={n} {sid} lenP={len(a)} lenH={len(b)} at {k}: P={a[k:k+3]} H={b[k:k+3]}")
        na = [PNUM[m.group(1)] for m in PNRE.finditer(pp.lower())]
        nb = [HNUM[m.group(1)] for m in HNRE.finditer(hb)]
        if na != nb:
            k = 0
            while k < min(len(na), len(nb)) and na[k] == nb[k]:
                k += 1
            out.append(f"NUM {f} n={n} {sid} lenP={len(na)} lenH={len(nb)} at {k}: P={na[k:k+4]} H={nb[k:k+4]}")
        da = re.findall(r"\d+", pb); db = re.findall(r"\d+", hb)
        if da != db:
            out.append(f"DIGIT {f} n={n} {sid} {da} {db}")
with open(os.path.join(OUT, "review_r1_check2_out.txt"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(out))
print(Counter(o.split()[0] for o in out))
print("FAIL", Counter(FAIL).most_common(40))

