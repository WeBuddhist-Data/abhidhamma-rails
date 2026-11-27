"""For each headword and each of its Burmese values: up to N segments with a Pāli window around the headword and a Burmese
window around the value. usage: cv.py [-n N] [-w W] hw [hw ...]"""
import re, sys, pathlib, collections
B = pathlib.Path(__file__).resolve().parents[5]
M = B / "AI_translation/burmese/pi-5-keywords-by-reference-pali-burmese-plain.md"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
def segs(d):
    out = {}
    for p in sorted(d.glob("*.md")):
        buf = []
        for line in p.read_text(encoding="utf-8").splitlines():
            if line.strip() and not line.startswith("---"): buf.append(line)
            m = ID.search(line)
            if m: out[m.group(1)] = " ".join(buf); buf = []
    return out
P = segs(B / "AI_translation/pali/pi-5_split_chapters")
R = segs(B / "AI_translation/burmese/pi-5-burmese-plain-zeroshot_split_chapters")
a = sys.argv[1:]; N = 2; W = 70
if "-n" in a: i = a.index("-n"); N = int(a[i+1]); del a[i:i+2]
if "-w" in a: i = a.index("-w"); W = int(a[i+1]); del a[i:i+2]
idx = collections.defaultdict(lambda: collections.defaultdict(list))
for l in M.read_text(encoding="utf-8").splitlines():
    m = re.match(r"\[([^\]]+)\] (.*)", l)
    if not m: continue
    for p in m.group(2).split(", "):
        k, _, v = p.partition("="); idx[k.lower()][v].append(m.group(1))
def win(t, s):
    i = t.lower().find(s.lower())
    if i < 0:
        s2 = s.split(" … ")[0].split("…")[0].strip()
        i = t.lower().find(s2.lower()); s = s2
    return t[max(0, i - W): i + len(s) + W] if i >= 0 else "<not found>"
for hw in a:
    for v, ids in idx[hw.lower()].items():
        print(f"## {hw} = {v} ({len(ids)}: {' '.join(ids[:8])})")
        for sid in ids[:N]:
            print(f"   [{sid}] P: {win(P.get(sid, ''), hw)}")
            print(f"   [{sid}] M: {win(R.get(sid, ''), v)}")
