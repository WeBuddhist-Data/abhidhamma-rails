import sys, re
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\review")
from r5_lib import *

PH = re.compile(r"^(.*?)\s+(?:tesaṃ|tāsaṃ|tattha|te|so|tassa)\s")
VH = re.compile(r"^(.*?),\s+thì\s")
files = FILES if len(sys.argv) < 2 else ["10-%s-indriyayamaka.md" % x for x in sys.argv[1].split(",")]
heads = defaultdict(Counter); hloc = {}
for fn, ln, sid, P, V in pairs(files):
    if P.startswith("#"): continue
    sp = sentences(P); sv = sentences(V)
    if len(sp) != len(sv): continue
    for a, b in zip(sp, sv):
        if a.startswith("(") or re.match(r"(Yassa|yassa|Yattha|yattha|Yo|yo)\b", a):
            continue
        if "?" in a: continue
        m = PH.match(a); n = VH.match(b)
        if not m:
            ph = "NOHEAD:" + a[:120]
        else:
            ph = m.group(1)
        vh = n.group(1) if n else "NOHEAD:" + b[:140]
        pn, _ = norm_p(ph); vn = norm_v(vh)
        o = order_of(pn)
        k = lettered(pn, o); v = lettered(vn, o)
        heads[k][v] += 1
        hloc.setdefault((k, v), "%s:%d/%s" % (fn[3:5], ln, sid))
print("distinct heads", len(heads))
for k, c in heads.items():
    for v, n in c.items():
        print("[%d] %s\n P: %s\n V: %s" % (n, hloc[(k, v)], k, v))
