"""Classify negated Pañhāpucchaka items (na X / no X / siyā na X / siyā no X) by Hindi shape, per chapter.
Pairs comma/dash/period items of lines whose item counts match (as find_divergences_hi.scan_items).

usage: python -I -X utf8 neg_items_pi2.py [--show]
"""
import collections, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import hz_common
from hz_common import PARTS, pairs, norm, short

hz_common.CUR["hdir"] = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-2-hindi-plain-rails_split_chapters"
SP = re.compile(r"(?<=[?.;:,])\s+|\s+[–—]\s+")
SH = re.compile(r"(?<=[?।;:,])\s+|\s+[–—]\s+")
NEG = re.compile(r"^(Siyā |siyā )?(na|no|Na|No) (?!vattabb)(\w+)[.,;]?$")
cnt = collections.defaultdict(collections.Counter)
ex = collections.defaultdict(list)
for part in PARTS:
    for p, h in pairs(part):
        if p.startswith("#"):
            continue
        cp = [c for c in SP.split(norm(p)) if c]
        ch = [c for c in SH.split(norm(h)) if c]
        if len(cp) != len(ch):
            continue
        for a, b in zip(cp, ch):
            m = NEG.match(a.strip())
            if not m:
                continue
            kind = ("siyā " if m.group(1) else "") + m.group(2).lower()
            if "नहीं" in b:
                shape = "pred-neg (नहीं)"
            elif re.search(r"(^| )न ", b) or "रहित" in b:
                shape = "item-name (न/रहित)"
            else:
                shape = "other"
            cnt[(kind, shape)][short(part)] += 1
            if len(ex[(kind, shape, short(part))]) < 2:
                ex[(kind, shape, short(part))].append(f"{a} :: {b}")
for k in sorted(cnt):
    print(k, dict(cnt[k]))
if "--show" in sys.argv:
    for k in sorted(ex):
        for e in ex[k]:
            print(k, e)
