"""Print sentence pairs (Pāli '.'/'?' ↔ Hindi '।'/'?') of lines in given segments, flagging count mismatches.

usage: python -I -X utf8 sents_rails_pi2.py <chapter-file-prefix> <seg-id>[,<seg-id>…] [--grep REGEX]
"""
import os, re, sys
ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PDIR = ROOT + r"\AI_translation\pali\pi-2_split_chapters"
HDIR = ROOT + r"\AI_translation\hindi\pi-2-hindi-plain-rails_split_chapters"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
SP = re.compile(r"(?<=[.?])\s+")
SH = re.compile(r"(?<=[।?])\s+")


def lines(p):
    return [l for l in open(p, encoding="utf-8-sig").read().splitlines() if l.strip()]


pref, segs = sys.argv[1], set(sys.argv[2].split(","))
grep = re.compile(sys.argv[sys.argv.index("--grep") + 1]) if "--grep" in sys.argv else None
f = next(x for x in os.listdir(PDIR) if x.startswith(pref))
P, H = lines(os.path.join(PDIR, f)), lines(os.path.join(HDIR, f))
ids, nxt = [None] * len(P), "?"
for k in range(len(P) - 1, -1, -1):
    m = ID.search(P[k])
    if m:
        nxt = m.group(1)
    ids[k] = nxt
for k, (p, h) in enumerate(zip(P, H)):
    if ids[k] not in segs and "all" not in segs:
        continue
    sp, sh = SP.split(p), SH.split(h)
    print(f"## line {k + 1} ({ids[k]}) sentences P={len(sp)} H={len(sh)}")
    if len(sp) == len(sh):
        for a, b in zip(sp, sh):
            if grep and not (grep.search(a) or grep.search(b)):
                continue
            print("  P:", a)
            print("  H:", b)
    else:
        print("  P:", p)
        print("  H:", h)
