import re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from review_r1_common import *
from collections import OrderedDict

f = sys.argv[1] if len(sys.argv) > 1 else "1-01-kusalattika.md"
pr = pairs(f)
seen = OrderedDict()
for n, sid, p, h in pr:
    if p.startswith("#") or (len(p) < 60 and not p.startswith("(")):
        pk = re.sub(r"\s*\^[\w-]+\s*$", "", p)
        hk = re.sub(r"\s*\^[\w-]+\s*$", "", h)
        key = (pk, hk)
        seen.setdefault(key, []).append(n)
# group by pali key to find inconsistent renderings
byp = {}
for (pk, hk), ns in seen.items():
    byp.setdefault(re.sub(r"^#+\s*", "", pk), {}).setdefault(re.sub(r"^#+\s*", "", hk), []).extend(ns)
with open(os.path.join(OUT, "review_r1_heads_out.txt"), "w", encoding="utf-8") as fh:
    for pk, d in byp.items():
        flag = "  <<INCONSISTENT" if len(d) > 1 else ""
        for hk, ns in d.items():
            fh.write(f"{pk} | {hk} | n={len(ns)} first={ns[:4]}{flag}\n")
print(len(byp))
