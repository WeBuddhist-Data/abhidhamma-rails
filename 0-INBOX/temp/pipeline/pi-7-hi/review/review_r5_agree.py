import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from review_r5_common import *

bad = []
for fn in FILES:
    P, H = pairs(fn)
    for i, (a, b) in enumerate(zip(P, H), 1):
        if not a.strip() or a.startswith("#"):
            continue
        ph = a.split(" – ")[0]; hh = b.split(" – ")[0]
        if re.search(r"dhammā uppajjanti", ph):
            if "परिघटनाएँ" not in hh or "होती हैं" not in hh:
                bad.append((fn[:4], i, "pl-uppajj", hh[-60:]))
        elif re.search(r"dhammo uppajjati", ph):
            if re.search(r"होती हैं", hh):
                bad.append((fn[:4], i, "sg-uppajj", hh[-60:]))
        m = re.match(r"^(.+?) dhamm(o|ā) .+? dhammassa \S+paccayena paccayo", ph)
        if m:
            pl = m.group(2) == "ā"
            hm = re.search(r"कारण होती(?P<h> हैं)?", hh)
            if not hm:
                bad.append((fn[:4], i, "noverb", hh[-60:]))
            elif bool(hm.group("h")) != pl:
                bad.append((fn[:4], i, "panha-num", hh[-60:]))
for x in bad:
    print(x)
print(len(bad))
