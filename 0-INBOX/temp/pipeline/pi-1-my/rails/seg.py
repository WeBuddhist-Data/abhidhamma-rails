"""Inspection helper: print the Pāli and the Burmese of segments.
usage: seg.py [--rails] id [id ...]   (Burmese = zero-shot, or the rails with --rails)"""
import pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[5]
P = ROOT / "AI_translation/pali/pi-1_split_chapters"
args = sys.argv[1:]
M = ROOT / ("AI_translation/burmese/pi-1-burmese-plain-rails_split_chapters" if "--rails" in args
            else "AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters")
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
def segs(d):
    out = {}
    for p in sorted(d.glob("*.md")):
        buf = []
        for l in p.read_text(encoding="utf-8").splitlines():
            if not l.strip(): continue
            buf.append(l); m = ID.search(l)
            if m: out[m.group(1)] = (p.name[:-3], buf); buf = []
    return out
a, b = segs(P), segs(M)
for i in [x for x in args if not x.startswith("--")]:
    print(f"== {i} ({a[i][0]})")
    for x, y in zip(a[i][1], b[i][1]):
        print("P:", x); print("M:", y)
