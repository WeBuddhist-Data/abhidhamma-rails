"""Count Vietnamese phrase variants in the aligned lines whose Pali matches a regex.
usage: r4_count.py PALI_REGEX VI_REGEX[;VI_REGEX...] [files|all] [showN]"""
import sys, re, collections
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\review")
from r4_common import pairs
pre = re.compile(sys.argv[1], re.I)
vres = sys.argv[2].split(";")
files = None if len(sys.argv) < 4 or sys.argv[3] == "all" else sys.argv[3].split(",")
show = int(sys.argv[4]) if len(sys.argv) > 4 else 0
c = collections.Counter()
nomatch = []
for f, n, sid, p, v in pairs(files):
    k = len(pre.findall(p))
    if not k:
        continue
    c["pali_hits"] += k
    for vr in vres:
        c[vr] += len(re.findall(vr, v))
    if all(not re.search(vr, v) for vr in vres):
        nomatch.append((f, n, sid, p, v))
for k, x in c.items():
    print(x, k)
print("lines with none of the VI patterns:", len(nomatch))
for f, n, sid, p, v in nomatch[:show]:
    print(f"{f}:{n} {sid}\n  P: {p.strip()[:400]}\n  V: {v.strip()[:400]}")
