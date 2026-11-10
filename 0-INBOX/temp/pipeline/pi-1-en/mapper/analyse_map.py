"""Analyse a pāli=english keyword map: value lengths, " / " joins, suspected non-word fragments.

usage: python -I -X utf8 analyse_map.py <map.md> [--list N]
"""
import collections, re, sys

path = sys.argv[1]
show = int(sys.argv[sys.argv.index("--list") + 1]) if "--list" in sys.argv else 0
pairs = []
for line in open(path, encoding="utf-8-sig"):
    if not line.strip():
        continue
    i, body = line.rstrip("\n").split("] ", 1)
    for p in body.split(", "):
        pali, en = p.rsplit("=", 1) if "=" in p else (p, "")
        pairs.append((i[1:], pali.strip(), en))
nde = sum(1 for _, p, _ in pairs if p == "(no direct equivalent)")
vals = [(i, p, e) for i, p, e in pairs if p != "(no direct equivalent)"]
joins = [(i, p, e) for i, p, e in vals if " / " in p]
words = collections.Counter()
for i, p, e in vals:
    for part in p.split(" / "):
        words[min(len(part.split()), 6)] += 1
long_ = [(i, p, e) for i, p, e in vals if any(len(part.split()) >= 4 for part in p.split(" / "))]
FRAG = re.compile(r"^(ññ|bb|tt|kk|cc|pp|mm|ṃ|ss[aā]|ṭṭ|dd|jj|gg|ll|yy|vv|nn)|^(bhuno|ñutā|ññutā|tā|ttaṃ|ñassāmi|ssāmi|tta)$")
frags = collections.Counter(part for _, p, _ in vals for part in p.split(" / ") for part in [part] if FRAG.search(part.split()[0] if part.split() else part))
print(f"{path}\n pairs {len(pairs)}  no-equivalent {nde}  joins {len(joins)}")
print(" words per Pāli part:", dict(sorted(words.items())), "(6 = 6+)")
print(" parts with >=4 words:", len(long_))
print(" suspected fragments:", frags.most_common(40))
if show:
    for i, p, e in sorted(long_, key=lambda x: -max(len(q.split()) for q in x[1].split(" / ")))[:show]:
        print(f"  [{i}] {p} = {e}")
