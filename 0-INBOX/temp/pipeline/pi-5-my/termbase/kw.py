"""Keyword-in-context for pi-5: for each segment id, print the Pāli window around a Pāli substring and the Burmese window around
a Burmese substring. usage: kw.py PALI_SUB MY_SUB id [id ...]"""
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
ps, ms = sys.argv[1], sys.argv[2]
W = 90
for sid in sys.argv[3:]:
    sid = sid.lstrip("^")
    pt = " ".join(P.get(sid, [])); mt = " ".join(R.get(sid, []))
    out = []
    for t, s in ((pt, ps), (mt, ms)):
        i = t.lower().find(s.lower())
        out.append(t[max(0, i - W): i + len(s) + W] if i >= 0 else f"<{s} not found>")
    print(f"[{sid}] P: …{out[0]}…\n[{sid}] M: …{out[1]}…")
