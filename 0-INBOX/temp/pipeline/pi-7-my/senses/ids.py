"""List every Burmese value of a Pāli headword with all its segment ids (pi-7 map). usage: ids.py hw [hw ...]
Adapted from pi-6-my/senses/ids.py (map read once)."""
import sys, re, collections, pathlib
M = pathlib.Path(__file__).resolve().parents[5] / "AI_translation/burmese/pi-7-keywords-by-reference-pali-burmese-plain.md"
want = {h.lower(): h for h in sys.argv[1:]}
d = {h: collections.defaultdict(list) for h in sys.argv[1:]}
for l in M.read_text(encoding="utf-8").splitlines():
    m = re.match(r"\[([^\]]+)\] (.*)", l)
    if not m: continue
    for p in m.group(2).split(", "):
        k, _, v = p.partition("=")
        h = want.get(k.lower())
        if h: d[h][v].append(m.group(1))
for hw in sys.argv[1:]:
    print(hw, {v: (len(ids), ids[:12]) for v, ids in d[hw].items()})
