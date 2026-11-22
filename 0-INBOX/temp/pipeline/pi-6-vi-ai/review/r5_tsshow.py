import sys, re
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\review")
from r5_lib import *
# Console-only viewer: prints Pali / ours / reference for the given segment IDs. Writes nothing.
TS = os.path.join(ROOT, r"1-SOURCES\Translations\Vietnamese\vi-6-tinh_su.md")
with open(TS, encoding="utf-8") as f:
    tl = f.read().split("\n")
seg = defaultdict(list); cur = None
for l in tl:
    m = re.match(r"!\[\[.*#\^([0-9a-z-]+)\]\]", l.strip())
    if m:
        cur = m.group(1); continue
    if cur and l.strip():
        seg[cur].append(l)
P = defaultdict(list); V = defaultdict(list)
for fn, ln, sid, p, v in pairs():
    P[sid].append(p); V[sid].append(v)
what = sys.argv[2] if len(sys.argv) > 2 else "pvt"
for i in sys.argv[1].split(","):
    print("######", i)
    if "p" in what:
        for x in P[i]: print("P:", x)
    if "v" in what:
        for x in V[i]: print("V:", x)
    if "t" in what:
        for x in seg.get(i, ["(none)"]): print("T:", x)
