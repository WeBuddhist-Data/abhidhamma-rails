"""Inspection helper: for adherence misses of the given keywords (all when none given), print the Pāli around the
keyword and the Burmese of the same line around the proportional position (zero-shot, or rails with --rails).
usage: ctx.py [--rails] [--skip kw,kw] adherence.txt [keyword ...]"""
import pathlib, re, sys, unicodedata
ROOT = pathlib.Path(__file__).resolve().parents[5]
N = lambda s: unicodedata.normalize("NFC", s)
a = sys.argv[1:]
rails = "--rails" in a; a = [x for x in a if x != "--rails"]
skip = set()
if a[0] == "--skip": skip = set(a[1].split(",")); a = a[2:]
P = ROOT / "AI_translation/pali/pi-1_split_chapters"
M = ROOT / ("AI_translation/burmese/pi-1-burmese-plain-rails_split_chapters" if rails
            else "AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters")
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
def segs(d):
    out = {}
    for p in sorted(d.glob("*.md")):
        buf = []
        for l in N(p.read_text(encoding="utf-8")).splitlines():
            if not l.strip(): continue
            buf.append(l); m = ID.search(l)
            if m: out[m.group(1)] = (p.name[:4], buf); buf = []
    return out
A, B = segs(P), segs(M)
W = "āīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶ"
for l in open(a[0], encoding="utf-8"):
    f = N(l).strip().split("\t")
    if len(f) < 3 or (a[1:] and f[1] not in a[1:]) or f[1] in skip: continue
    i = f[0]; ch, pl = A[i]; ml = B[i][1]
    rx = re.compile(rf"(?<![\w{W}]){re.escape(f[1])}(?![\w{W}])")
    hit = None
    for x, y in zip(pl, ml):
        m = rx.search(x)
        if m: hit = (x, y, m); break
    if not hit:
        for x, y in zip(pl, ml):
            m = re.search(re.escape(f[1]), x, re.I)
            if m: hit = (x, y, m); break
    print(f"{i} [{ch}] {f[1]} = {f[2]}")
    if not hit:
        print("  P: (not found)", " ".join(pl)[:200]); continue
    x, y, m = hit
    print("  P:", x[max(0, m.start() - 60): m.end() + 60])
    c = int(m.start() / max(1, len(x)) * len(y))
    print("  M:", y[max(0, c - 110): c + 150])
