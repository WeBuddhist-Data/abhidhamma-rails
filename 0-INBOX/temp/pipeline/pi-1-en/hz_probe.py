"""Probe: for lines whose Pāli matches P, tally English matches of E (group 0 or 1) per part.
usage: hz_probe.py "<pali regex>" "<english regex>" [show-misses]"""
import re, sys, collections
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-en")
from hz_show import PARTS, pairs

rp, re_ = re.compile(sys.argv[1]), re.compile(sys.argv[2])
show = len(sys.argv) > 3
tally = collections.defaultdict(collections.Counter)
miss = []
for part in PARTS:
    for i, (p, e) in enumerate(pairs(part)):
        np_ = len(rp.findall(p))
        if not np_:
            continue
        ms = [m.group(1) if m.groups() else m.group(0) for m in re_.finditer(e)]
        for m in ms:
            tally[m][part[:4]] += 1
        if len(ms) < np_:
            miss.append(f"{part[:4]}:{i} pali={np_} en={len(ms)}")
for k, v in sorted(tally.items(), key=lambda kv: -sum(kv[1].values())):
    print(f"[{sum(v.values())}] {k!r} :: {dict(v)}")
print("lines with fewer EN matches than PALI:", len(miss))
if show:
    print("\n".join(miss[:40]))
