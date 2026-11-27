"""Show Pāli and Burmese lines of the segments where a headword occurs. usage: show.py hw [max_segments] [value-filter]"""
import re, sys, pathlib, collections
B = pathlib.Path(__file__).resolve().parents[5]
M = B / "AI_translation/burmese/pi-1-keywords-by-reference-pali-burmese-plain.md"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
def segs(d):
    out = {}
    for p in sorted(d.glob("*.md")):
        buf = []
        for line in p.read_text(encoding="utf-8").splitlines():
            if line.strip() and not line.startswith("---"): buf.append(line)
            m = ID.search(line)
            if m: out[m.group(1)] = buf; buf = []
    return out
P = segs(B / "AI_translation/pali/pi-1_split_chapters")
R = segs(B / "AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters")
hw = sys.argv[1]; mx = int(sys.argv[2]) if len(sys.argv) > 2 else 4; vf = sys.argv[3] if len(sys.argv) > 3 else None
d = collections.defaultdict(list)
for l in M.read_text(encoding="utf-8").splitlines():
    m = re.match(r"\[([^\]]+)\] (.*)", l)
    if not m: continue
    for p in m.group(2).split(", "):
        k, _, v = p.partition("=")
        if k == hw: d[v].append(m.group(1))
pat = re.compile(r"(?<![^\W\d_])" + re.escape(hw) + r"(?![^\W\d_])", re.I)
for v, ids in d.items():
    if vf and v != vf: continue
    print(f"=== {hw} = {v} ({len(ids)})")
    for i in ids[:mx]:
        pl, ml = P.get(i, []), R.get(i, [])
        for k, line in enumerate(pl):
            if pat.search(line) or hw.lower() in line.lower():
                print(f"  [{i}:{k}] P: {line[:260]}")
                if k < len(ml): print(f"  [{i}:{k}] M: {ml[k][:300]}")
                break
