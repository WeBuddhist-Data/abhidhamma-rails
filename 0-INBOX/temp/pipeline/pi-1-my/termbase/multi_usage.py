"""For every multi-candidate sense (or the given headwords): counts of each Burmese value in the keyword-by-reference file, with sample ids."""
import re, collections, pathlib, sys
B = pathlib.Path(__file__).resolve().parents[5]
S = B / "AI_translation/burmese/pi-1-pali-word-burmese-senses-plain.md"
M = B / "AI_translation/burmese/pi-1-keywords-by-reference-pali-burmese-plain.md"
idx = collections.defaultdict(lambda: collections.defaultdict(list))
for l in M.read_text(encoding="utf-8").splitlines():
    m = re.match(r"\[([^\]]+)\] (.*)", l)
    if not m: continue
    for p in m.group(2).split(", "):
        k, _, v = p.partition("=")
        idx[k][v].append(m.group(1))
only = set(sys.argv[1:])
for line in S.read_text(encoding="utf-8").splitlines():
    hw, body = line.split(": {", 1)
    if only and hw not in only: continue
    for i, s in enumerate(body[:-1].split("; ")):
        tag, c = s.rsplit(": ", 1)
        if " / " not in c and not only: continue
        print(f"{hw}|{i}  [{tag[:110]}]  cands: {c}")
        for v, ids in sorted(idx[hw].items(), key=lambda x: -len(x[1])):
            print(f"     {len(ids):4d}  {v}   {' '.join(ids[:8])}")
