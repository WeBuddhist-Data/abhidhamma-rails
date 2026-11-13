import sys, os, re
from collections import defaultdict, Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from review_r5_common import *

# Pali head formulas
PV = r"(paṭicca|paccayā|nissāya|saṃsaṭṭho|saṃsaṭṭhā|sampayutto|sampayuttā)"
P1 = re.compile(r"^(?P<x>.+?) dhamm(?:aṃ|e) " + PV + r" (?P<y>.+?) dhamm(?:o|ā) uppajj")
P2 = re.compile(r"^(?P<x>.+?) dhamm(?:o|ā) (?P<y>.+?) dhammassa (?P<c>\S+?)paccayena paccayo")
# Hindi
H1 = re.compile(r"^(?P<x>.+?) परिघटना(?:ओं)? (?P<v>पर निर्भर होकर|के कारण|पर आश्रित होकर|से घुली-मिली|से घुली-मिलीं|से जुड़ी|से जुड़ीं|के साथ घुल-मिलकर|से जुड़कर|के सहारे|का आश्रय लेकर|\S+ \S+)\s+(?P<y>.+?) परिघटना(?:एँ)? ")
H2 = re.compile(r"^(?P<x>.+?) परिघटना(?:एँ)?, (?P<y>.+?) परिघटना के लिए (?P<c>.+?)-कारण के रूप में")

verbs = Counter()
tabX = defaultdict(Counter); tabY = defaultdict(Counter)
tab2X = defaultdict(Counter); tab2Y = defaultdict(Counter)
locs = defaultdict(list)
nomatch = []
for fn in FILES:
    P, H = pairs(fn)
    for i, (a, b) in enumerate(zip(P, H), 1):
        a2 = re.sub(r"^\*|\*$", "", a.strip()); b2 = b.strip()
        m = P1.match(a2)
        if m:
            v = m.group(2)
            hm = H1.match(b2)
            if not hm:
                nomatch.append((fn, i, "H1", a[:80], b[:120])); continue
            verbs[(v, hm.group("v"))] += 1
            kx = (v, m.group("x").lower()); ky = (v, m.group("y").lower())
            tabX[kx][hm.group("x")] += 1; tabY[ky][hm.group("y")] += 1
            locs[("X",) + kx + (hm.group("x"),)].append(f"{fn[:4]}:{i}")
            locs[("Y",) + ky + (hm.group("y"),)].append(f"{fn[:4]}:{i}")
            continue
        m = P2.match(a2)
        if m:
            hm = H2.match(b2)
            if not hm:
                nomatch.append((fn, i, "H2", a[:80], b[:120])); continue
            kx = m.group("x").lower(); ky = m.group("y").lower()
            tab2X[kx][hm.group("x")] += 1; tab2Y[ky][hm.group("y")] += 1
            locs[("2X", kx, hm.group("x"))].append(f"{fn[:4]}:{i}")
            locs[("2Y", ky, hm.group("y"))].append(f"{fn[:4]}:{i}")

print("VERBS")
for k, c in verbs.items():
    print(" ", k, c)
print("NOMATCH", len(nomatch))
for n in nomatch:
    print(" ", n)
for name, tab, tag in (("PATICCA-X", tabX, "X"), ("PATICCA-Y", tabY, "Y"), ("PANHA-X", tab2X, "2X"), ("PANHA-Y", tab2Y, "2Y")):
    print("=====", name)
    for k in sorted(tab, key=str):
        c = tab[k]
        flag = "  <<<VARIANTS" if len(c) > 1 else ""
        print(k, "=>", dict(c), flag)
        if len(c) > 1:
            for hv in c:
                key = (tag,) + (k if isinstance(k, tuple) else (k,)) + (hv,)
                print("     ", hv, locs[key][:12])
