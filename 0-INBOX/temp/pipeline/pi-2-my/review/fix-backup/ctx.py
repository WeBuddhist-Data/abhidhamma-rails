"""Inspection helper (pi-2): for adherence misses of the given keywords (all when none given), print the keyword map's
Burmese value (the zero-shot's own form, pi-2-keywords-by-reference-pali-burmese-plain.md), the Pāli around the
keyword and the Burmese of the same line around the proportional position (zero-shot, or rails with --rails).
usage: ctx.py [--rails] [--first] [--skip kw,kw] adherence.txt [keyword ...]"""
import pathlib, re, sys, unicodedata
ROOT = pathlib.Path(__file__).resolve().parents[5]
N = lambda s: unicodedata.normalize("NFC", s)
a = sys.argv[1:]
rails = "--rails" in a; first = "--first" in a; a = [x for x in a if x not in ("--rails", "--first")]
seen = set()
skip = set()
if a[0] == "--skip": skip = set(a[1].split(",")); a = a[2:]
P = ROOT / "AI_translation/pali/pi-2_split_chapters"
M = ROOT / ("AI_translation/burmese/pi-2-burmese-plain-rails_split_chapters" if rails
            else "AI_translation/burmese/pi-2-burmese-plain-zeroshot_split_chapters")
KM = ROOT / "AI_translation/burmese/pi-2-keywords-by-reference-pali-burmese-plain.md"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
def segs(d):
    out = {}
    for p in sorted(d.glob("*.md")):
        buf = []
        for l in N(p.read_text(encoding="utf-8")).splitlines():
            if not l.strip(): continue
            buf.append(l); m = ID.search(l)
            if m: out[m.group(1)] = (p.name.split("-")[0], buf); buf = []
    return out
KV = {}
for l in open(KM, encoding="utf-8"):
    m = re.match(r"^\[([^\]]+)\] (.*)$", N(l.strip()))
    if m:
        for kv in m.group(2).split(", "):
            if "=" in kv:
                k, v = kv.split("=", 1); KV[(m.group(1), k)] = v
A, B = segs(P), segs(M)
W = "āīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶ"
for l in open(a[0], encoding="utf-8"):
    f = N(l).strip().split("\t")
    if len(f) < 3 or (a[1:] and f[1] not in a[1:]) or f[1] in skip: continue
    i = f[0]; ch, pl = A[i]; ml = B[i][1]
    if first:
        g = (f[1], KV.get((i, f[1])))
        if g in seen: continue
        seen.add(g)
    rx = re.compile(rf"(?<![\w{W}]){re.escape(f[1])}(?![\w{W}])")
    hit = None
    for x, y in zip(pl, ml):
        m = rx.search(x)
        if m: hit = (x, y, m); break
    if not hit:
        for x, y in zip(pl, ml):
            m = re.search(re.escape(f[1]), x, re.I)
            if m: hit = (x, y, m); break
    print(f"{i} [{ch}] {f[1]} = {f[2]}   MAP: {KV.get((i, f[1]), '-')}")
    if not hit:
        print("  P: (not found)", " ".join(pl)[:200]); continue
    x, y, m = hit
    print("  P:", x[max(0, m.start() - 70): m.end() + 70])
    c = int(m.start() / max(1, len(x)) * len(y))
    print("  M:", y[max(0, c - 120): c + 160])
