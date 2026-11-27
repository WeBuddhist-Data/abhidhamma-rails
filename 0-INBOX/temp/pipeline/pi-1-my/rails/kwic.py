"""Inspection helper: for adherence misses of the given keywords, print the Pāli around the keyword and every
Burmese match of a regex (with context) in the same segment.
usage: kwic.py [--rails] adherence.txt '<burmese regex>' keyword [keyword ...]"""
import pathlib, re, sys, unicodedata
ROOT = pathlib.Path(__file__).resolve().parents[5]
a = sys.argv[1:]
rails = "--rails" in a; a = [x for x in a if x != "--rails"]
P = ROOT / "AI_translation/pali/pi-1_split_chapters"
M = ROOT / ("AI_translation/burmese/pi-1-burmese-plain-rails_split_chapters" if rails
            else "AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters")
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
def segs(d):
    out = {}
    for p in sorted(d.glob("*.md")):
        buf = []
        for l in unicodedata.normalize("NFC", p.read_text(encoding="utf-8")).splitlines():
            if not l.strip(): continue
            buf.append(l); m = ID.search(l)
            if m: out[m.group(1)] = (p.name[:4], " ".join(buf)); buf = []
    return out
A, B = segs(P), segs(M)
adh, brx, kws = a[0], re.compile(a[1]), set(a[2:])
W = "āīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶ"
for l in open(adh, encoding="utf-8"):
    f = unicodedata.normalize("NFC", l).strip().split("\t")
    if len(f) < 3 or (kws and f[1] not in kws): continue
    i = f[0]; ch, pt = A[i]; mt = B[i][1]
    rx = re.compile(rf"(?<![\w{W}]){re.escape(f[1])}(?![\w{W}])", re.I)
    pm = [pt[max(0, m.start() - 45): m.end() + 45] for m in rx.finditer(pt)][:2]
    bm = [mt[max(0, m.start() - 30): m.end() + 30] for m in brx.finditer(mt)][:3]
    print(f"{i} [{ch}] {f[1]}\n  P: {' ¦ '.join(pm) or '(not as word)'}\n  M: {' ¦ '.join(bm) or '(no match)'}")
