import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from review_r5_common import *

SKIP_P = {"cakkaṃ", "saṃkhittaṃ", "saṃkhittaṃ.", "syā.", "sī.", "pī.", "ka.", "ma."}


def groups(s):
    # top-level parenthesis groups
    out = []; depth = 0; cur = ""
    for ch in s:
        if ch == "(":
            if depth == 0:
                cur = ""
            else:
                cur += ch
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth == 0:
                out.append(cur)
            else:
                cur += ch
        elif depth > 0:
            cur += ch
    return [g for g in out if not re.fullmatch(r"\d+", g.strip())]

fsel = sys.argv[1] if len(sys.argv) > 1 else None
for fn in FILES:
    if fsel and not fn.startswith(fsel):
        continue
    P, H = pairs(fn)
    for i, (a, b) in enumerate(zip(P, H), 1):
        if a.startswith("#"):
            continue
        pg = groups(re.sub(r"\{[^}]*\}", "", a)); hg = groups(re.sub(r"\[[^\]]*\]", "", b))
        pg2 = [g for g in pg if g.strip() not in SKIP_P]
        hg2 = [g for g in hg if g.strip() not in ("चक्र", "संक्षिप्त")]
        if not pg2 and not hg2:
            continue
        if len(pg) != len(hg):
            print(f"!! {fn[:4]}:{i} group count {len(pg)} vs {len(hg)}")
        for k in range(max(len(pg2), len(hg2))):
            x = pg2[k] if k < len(pg2) else "-"; y = hg2[k] if k < len(hg2) else "-"
            print(f"{fn[:4]}:{i} | {x} || {y}")
