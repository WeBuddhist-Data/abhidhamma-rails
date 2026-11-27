"""Inspection helper: print the Pāli and Burmese lines of segments (zero-shot, or rails with --rails); with -g REGEX
only the line pairs whose Pāli matches, cut around the match.
usage: seg.py [--rails] [-g REGEX] id [id ...]"""
import pathlib, re, sys, unicodedata
ROOT = pathlib.Path(__file__).resolve().parents[5]
N = lambda s: unicodedata.normalize("NFC", s)
a = sys.argv[1:]
rails = "--rails" in a; a = [x for x in a if x != "--rails"]
g = None
if a and a[0] == "-g": g = re.compile(a[1]); a = a[2:]
P = ROOT / "AI_translation/pali/pi-2_split_chapters"
M = ROOT / ("AI_translation/burmese/pi-2-burmese-plain-rails_split_chapters" if rails
            else "AI_translation/burmese/pi-2-burmese-plain-zeroshot_split_chapters")
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
def segs(d):
    out = {}
    for p in sorted(d.glob("*.md")):
        buf = []
        for l in N(p.read_text(encoding="utf-8")).splitlines():
            if not l.strip(): continue
            buf.append(l); m = ID.search(l)
            if m: out[m.group(1)] = buf; buf = []
    return out
A, B = segs(P), segs(M)
for i in a:
    print(f"=== {i}")
    for x, y in zip(A[i], B[i]):
        if g:
            m = g.search(x)
            if not m: continue
            c = int(m.start() / max(1, len(x)) * len(y))
            print("P:", x[max(0, m.start() - 150): m.end() + 250]); print("M:", y[max(0, c - 250): c + 450])
        else:
            print("P:", x); print("M:", y)
