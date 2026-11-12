"""KWIC over the aligned pi-2 Pāli / Hindi rails lines.

usage: python -I -X utf8 kwic_rails_pi2.py <pali-regex> [hindi-regex] [--ch 4,6] [--full] [--max N] [--pi1]
  prints chapter:segment, then the Pāli line and the Hindi line (or, with a hindi-regex and without --full,
  only the Hindi matches with 60 chars of context). --pi1 searches the pi-1 rails instead.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import hz_common
from hz_common import PARTS, short, ID

RAILS = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-2-hindi-plain-rails_split_chapters"
PI1P = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-1_split_chapters"
PI1H = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters"

args = [a for a in sys.argv[1:]]
opts = {}
pos = []
i = 0
while i < len(args):
    a = args[i]
    if a in ("--ch", "--max"):
        opts[a] = args[i + 1]; i += 2; continue
    if a.startswith("--"):
        opts[a] = True; i += 1; continue
    pos.append(a); i += 1
prx = re.compile(pos[0])
hrx = re.compile(pos[1]) if len(pos) > 1 else None
chs = set(opts["--ch"].split(",")) if "--ch" in opts else None
mx = int(opts.get("--max", 10 ** 9))


def lines(p):
    return [l for l in open(p, encoding="utf-8-sig").read().splitlines() if l.strip()]


def iter_pairs():
    if "--pi1" in opts:
        for f in sorted(os.listdir(PI1P)):
            if f.endswith(".md") and os.path.exists(os.path.join(PI1H, f)):
                P, H = lines(os.path.join(PI1P, f)), lines(os.path.join(PI1H, f))
                yield f[:-3], P, H
        return
    for part in PARTS:
        P, H = lines(os.path.join(hz_common.PDIR, part + ".md")), lines(os.path.join(RAILS, part + ".md"))
        yield part, P, H


n = 0
for part, P, H in iter_pairs():
    tag = part if "--pi1" in opts else short(part)
    if chs and tag.replace("ch", "") not in chs:
        continue
    sid = "?"
    # segment id = id of the next line carrying one
    ids = [None] * len(P)
    nxt = "?"
    for k in range(len(P) - 1, -1, -1):
        m = ID.search(P[k])
        if m:
            nxt = m.group(1)
        ids[k] = nxt
    for k, (p, h) in enumerate(zip(P, H)):
        if not prx.search(p):
            continue
        if hrx and not hrx.search(h):
            continue
        n += 1
        if n > mx:
            break
        print(f"== {tag}:{ids[k]} (line {k + 1})")
        if hrx and "--full" not in opts:
            for m in hrx.finditer(h):
                print("  H…", h[max(0, m.start() - 60):m.end() + 60])
        else:
            print("  P:", p)
            print("  H:", h)
print("matches:", n)
