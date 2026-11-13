import re, sys, os
from collections import Counter
sys.path.insert(0, os.path.dirname(__file__))
from review_r1_common import *

def seq_p(p):
    q = p.lower()
    q = re.sub(r"\{[^}]*\}", "", q)
    q = re.sub(r"vipākābyākat\w*\s+kiriyābyākat\w*", "xbyak", q)
    toks = []
    for m in re.finditer(r"kusalākusal|(?<![a-zāīū])akusal|kusal|byākat|xbyak", q):
        t = m.group(0)
        if t == "kusalākusal":
            toks += ["K", "A"]
        elif t == "akusal":
            toks.append("A")
        elif t == "kusal":
            toks.append("K")
        else:
            toks.append("B")
    return toks

def seq_h(h):
    h = re.sub(r"\[[^\]]*\]", "", h)
    toks = []
    for m in re.finditer(r"हितकर|हानिकर|अनिर्धारित", h):
        toks.append({"हितकर": "K", "हानिकर": "A", "अनिर्धारित": "B"}[m.group(0)])
    return toks

out = []
for f in FILES[1:]:
    for n, sid, p, h in pairs(f):
        a, b = seq_p(p), seq_h(h)
        if a != b:
            k = 0
            while k < min(len(a), len(b)) and a[k] == b[k]:
                k += 1
            out.append(f"{f} n={n} {sid} P={''.join(a)} H={''.join(b)} at {k}")
print("\n".join(out))
print(len(out))

