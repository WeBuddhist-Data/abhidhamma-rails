"""Overview of the pi-7 multi-candidate senses: candidates with their use counts (exact headword, keyword map) and sample ids,
the matched locked term (pi123456-match.tsv). headwords case-insensitive (the senses file joins case variants). usage: multi_view.py [> multi-view.txt]"""
import re, pathlib, collections
B = pathlib.Path(__file__).resolve().parents[5]
S = B / "AI_translation/burmese/pi-7-pali-word-burmese-senses-plain.md"
M = B / "AI_translation/burmese/pi-7-keywords-by-reference-pali-burmese-plain.md"
idx = collections.defaultdict(lambda: collections.defaultdict(list))
for l in M.read_text(encoding="utf-8").splitlines():
    m = re.match(r"\[([^\]]+)\] (.*)", l)
    if not m: continue
    for p in m.group(2).split(", "):
        k, _, v = p.partition("="); idx[k.lower()][v].append(m.group(1))
match = {}
for r in pathlib.Path(__file__).with_name("pi123456-match.tsv").read_text(encoding="utf-8").splitlines():
    c = r.split("\t"); match[c[1]] = c
n = 0
for line in S.read_text(encoding="utf-8").splitlines():
    hw, body = line.split(": {", 1)
    ss = body[:-1].split("; ")
    for i, s in enumerate(ss):
        tag, cands = s.rsplit(": ", 1)
        cl = cands.split(" / ")
        if len(cl) < 2: continue
        n += 1
        mt = match.get(f"{hw}|{i}")
        lk = f"{mt[0]} L={mt[3]} ({mt[4]} {mt[5]})" if mt and mt[3] else (mt[0] if mt else "")
        print(f"#{n} {hw}|{i} [{len(ss)} senses] {lk}\n   tag: {tag[:200]}")
        for c in cl:
            ids = idx[hw.lower()].get(c, [])
            print(f"   {len(ids):4d} {c}   {' '.join(ids[:5])}")
