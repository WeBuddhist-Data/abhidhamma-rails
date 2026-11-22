"""Identical Pali lines (ignoring IDs/labels) must have identical Vietnamese."""
import sys, re, collections
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\review")
from r4_common import pairs
show = int(sys.argv[1]) if len(sys.argv) > 1 else 10


def norm(s):
    s = re.sub(r"\s*\^[0-9a-z-]+\s*$", "", s.strip())
    s = re.sub(r"^\((Ka|Kha|a|b)\)\s*", "", s)
    s = re.sub(r"^(Còn )", "", s)
    s = s.replace("yassa vā pana", "yassa").replace("yattha vā pana", "yattha").replace("yaṃ vā pana", "yaṃ")
    return s.lower()


groups = collections.defaultdict(collections.Counter)
where = collections.defaultdict(list)
for f, n, sid, p, v in pairs():
    if p.startswith("#"):
        continue
    k = norm(p)
    vv = re.sub(r"\s*\^[0-9a-z-]+\s*$", "", v.strip())
    vv = re.sub(r"^\((a|b)\)\s*", "", vv)
    vv = re.sub(r"^Còn (ở|người|tâm|những|nơi|các)", lambda m: m.group(1).capitalize(), vv)
    groups[k][vv] += 1
    where[(k, vv)].append(f"{f}:{n}")
bad = [(k, c) for k, c in groups.items() if len(c) > 1]
print("groups", len(groups), "inconsistent", len(bad))
for k, c in bad[:show]:
    print("P:", k[:300])
    for vv, x in c.most_common():
        print(f"   {x}x {where[(k, vv)][:3]} V: {vv[:400]}")
