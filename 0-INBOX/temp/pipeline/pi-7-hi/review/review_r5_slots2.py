import sys, os, re
from collections import defaultdict, Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from review_r5_common import *

PV = r"(paṭicca|paccayā|nissāya|saṃsaṭṭho|saṃsaṭṭhā|sampayutto|sampayuttā)"
P1 = re.compile(r"^(?P<x>.+?) dhamm(?:aṃ|e) " + PV + r" (?P<y>.+?) dhamm(?:o|ā) uppajj")
P2 = re.compile(r"^(?P<x>.+?) dhamm(?:o|ā) (?P<y>.+?) dhammassa (?P<c>\S+?)paccayena paccayo")
HV = ["पर निर्भर होकर", "के कारण", "से घुल-मिलकर", "से जुड़कर", "पर आश्रित होकर", "के आश्रय से"]


def hnorm(s):
    s = re.sub(r"\s*परिघटना(एँ|ओं)?\b", "", s)
    s = s.replace(",", "")
    return re.sub(r"\s+", " ", s).strip()


def pnorm(s):
    return s.lower().strip()


tab = defaultdict(Counter)
locs = defaultdict(list)
bad = []
for fn in FILES:
    P, H = pairs(fn)
    for i, (a, b) in enumerate(zip(P, H), 1):
        a2 = re.sub(r"^\*|\*$", "", a.strip()); b2 = b.strip()
        m = P1.match(a2)
        if m:
            v = m.group(2)
            pos = [(b2.find(" " + hv + " "), hv) for hv in HV if b2.find(" " + hv + " ") >= 0]
            if not pos:
                bad.append((fn, i, "noverb", b2[:100])); continue
            p, hv = min(pos)
            hx = b2[:p]
            rest = b2[p + len(hv) + 2:]
            rest = rest.split(" – ")[0]
            my = re.match(r"(.+) परिघटना(?:एँ)? ", rest)
            if not my:
                bad.append((fn, i, "noY", rest[:100])); continue
            hy = my.group(1)
            for slot, pk, hk in (("X", m.group("x"), hx), ("Y", m.group("y"), hy)):
                k = (slot, v, pnorm(pk)); hv2 = hv + " | " + hnorm(hk)
                tab[k][hnorm(hk) + "  [" + hv + "]"] += 1
                locs[(k, hnorm(hk) + "  [" + hv + "]")].append(f"{fn[:4]}:{i}")
            continue
        m = P2.match(a2)
        if m:
            mm = re.match(r"^(?P<x>.+?) परिघटना(?:एँ)?, (?P<y>.+?) परिघटना के लिए (?P<c>.+?)-कारण के रूप में", b2)
            if not mm:
                bad.append((fn, i, "noH2", b2[:100])); continue
            for slot, pk, hk in (("2X", m.group("x"), mm.group("x")), ("2Y", m.group("y"), mm.group("y"))):
                k = (slot, "", pnorm(pk))
                tab[k][hnorm(hk)] += 1
                locs[(k, hnorm(hk))].append(f"{fn[:4]}:{i}")
print("BAD", bad)
for k in sorted(tab, key=str):
    c = tab[k]
    flag = "  <<<VARIANTS" if len(c) > 1 else ""
    print(k, "=>", dict(c), flag)
    if len(c) > 1:
        for hv in c:
            print("     ", hv, locs[(k, hv)][:15])
