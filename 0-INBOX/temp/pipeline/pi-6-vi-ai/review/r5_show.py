import sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\review")
from r5_lib import *
# usage: r5_show.py 04:32 05:17-20 ...
want = []
for a in sys.argv[1:]:
    f, r = a.split(":")
    if "-" in r:
        x, y = r.split("-"); rng = range(int(x), int(y) + 1)
    else:
        rng = [int(r)]
    want.append(("10-%s-indriyayamaka.md" % f, set(rng)))
idx = {}
for fn, ln, sid, P, V in pairs([w[0] for w in want]):
    idx[(fn, ln)] = (sid, P, V)
for fn, rng in want:
    for ln in sorted(rng):
        if (fn, ln) in idx:
            sid, P, V = idx[(fn, ln)]
            print("== %s:%d %s\nP: %s\nV: %s" % (fn[:5], ln, sid, P, V))
