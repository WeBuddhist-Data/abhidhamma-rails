"""Pāli and Burmese (pi-5 zero-shot) lines of segments. usage: ctx.py id [id ...] [--grep PALI_SUBSTRING] [--cut N]"""
import re, sys, pathlib
B = pathlib.Path(__file__).resolve().parents[5]
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
P = segs(B / "AI_translation/pali/pi-5_split_chapters")
R = segs(B / "AI_translation/burmese/pi-5-burmese-plain-zeroshot_split_chapters")
a = sys.argv[1:]; g = None; cut = 600
if "--grep" in a: i = a.index("--grep"); g = a[i+1]; del a[i:i+2]
if "--cut" in a: i = a.index("--cut"); cut = int(a[i+1]); del a[i:i+2]
for sid in a:
    sid = sid.lstrip("^")
    pl, ml = P.get(sid, []), R.get(sid, [])
    for k, line in enumerate(pl):
        if g and g.lower() not in line.lower(): continue
        print(f"[{sid}:{k}] P: {line[:cut]}")
        if k < len(ml): print(f"[{sid}:{k}] M: {ml[k][:cut]}")
