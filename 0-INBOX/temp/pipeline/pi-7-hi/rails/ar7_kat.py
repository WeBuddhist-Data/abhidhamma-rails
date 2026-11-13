"""List kātabba- renderings that are not «करना चाहिए» (exploration for the alignment pass)."""
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ar7_common as C

if "--bak" in sys.argv:
    C.CUR["hdir"] = C.BAK
c = collections.Counter()
ex = collections.defaultdict(list)
RX = re.compile(r"((?:[^\s(]+ ){0,4})(तैयार कर|शामिल कर|बना|से शुरू कर)(ना|ने|नी) चाहिए")
for part in C.PARTS:
    for i, (p, h) in enumerate(C.pairs(part)):
        if "kātabb" not in p:
            continue
        for m in RX.finditer(h):
            k = m.group(0)
            c[k] += 1
            ex[k].append(f"{part[:4]}:{i+1}")
for k, v in c.most_common():
    print(v, " ".join(ex[k][:3]), "|", k)
