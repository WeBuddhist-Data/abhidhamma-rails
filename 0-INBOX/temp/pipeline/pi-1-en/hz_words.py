"""Word-level scan of synonym strings: a Pāli clause of N space-separated words with no comma, whose English
clause splits into N comma items, is paired word by word. Groups by (Pāli word, previous word) and lists
English variants per part. Also pairs comma-separated Pāli lists with comma-separated English lists of the
same length. usage: hz_words.py out-file"""
import re, sys, collections
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-en")
from hz_show import PARTS, pairs
from hz_scan import clauses

STRIP_E = re.compile(r"^(whatever|or whatever|whatever is|is|and)\s+", re.I)
g = collections.defaultdict(lambda: collections.defaultdict(set))
for part in PARTS:
    for i, (p, e) in enumerate(pairs(part)):
        if p.startswith("#"):
            continue
        cp, ce = clauses(p), clauses(e)
        if len(cp) != len(ce):
            continue
        for a, b in zip(cp, ce):
            a = a.rstrip(".?;:")
            b = b.rstrip(".?;:")
            if "," in a:
                pa = [x.strip() for x in a.split(",")]
                pe = [x.strip() for x in b.split(",")]
                if len(pa) == len(pe) and len(pa) >= 3:
                    for j, (x, y) in enumerate(zip(pa, pe)):
                        if "…" in x:
                            continue
                        g[("L", x)][y.lower()].add(f"{part[:4]}")
                continue
            w = a.split()
            items = [x.strip() for x in b.split(",")]
            if len(items) >= 5 and len(w) >= len(items) and "…" not in a:
                k0 = len(w) - len(items) + 1
                for j, (x, y) in [(k0 + t, (w[k0 + t], items[1 + t])) for t in range(len(items) - 1)]:
                    prev = w[j - 1] if j else "^"
                    g[(prev, x)][y.lower()].add(f"{part[:4]}:{i}")
out = []
for k in sorted(g, key=lambda k: (k[1], k[0])):
    v = g[k]
    if len(v) > 1:
        out.append(f"### {k[0]} | {k[1]}")
        for y, locs in v.items():
            out.append(f"   {sorted(locs)[:6]}{'...' if len(locs) > 6 else ''} ({len(locs)}) :: {y}")
open(sys.argv[1], "w", encoding="utf-8").write("\n".join(out))
print("multi", sum(1 for l in out if l.startswith("###")))
