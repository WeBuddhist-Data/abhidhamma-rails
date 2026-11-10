"""KWIC: for lines whose Pāli matches P, print distinct English snippets around matches of E with counts per part.
usage: hz_kwic.py "<pali regex>" "<english regex>" [before] [after] [parts-prefix-filter]"""
import re, sys, collections
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-en")
from hz_show import PARTS, pairs

rp, re_ = re.compile(sys.argv[1]), re.compile(sys.argv[2])
b = int(sys.argv[3]) if len(sys.argv) > 3 else 40
a = int(sys.argv[4]) if len(sys.argv) > 4 else 40
flt = sys.argv[5].split(",") if len(sys.argv) > 5 else None
t = collections.defaultdict(collections.Counter)
for part in PARTS:
    if flt and not any(part.startswith(f) for f in flt):
        continue
    for i, (p, e) in enumerate(pairs(part)):
        if not rp.search(p):
            continue
        for m in re_.finditer(e):
            t[e[max(0, m.start() - b):m.end() + a]][part[:4]] += 1
for k, v in sorted(t.items(), key=lambda kv: -sum(kv[1].values())):
    print(f"[{sum(v.values())}] {dict(v)} :: {k}")
