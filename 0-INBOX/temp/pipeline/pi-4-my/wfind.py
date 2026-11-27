"""Find a witness segment: usage wfind.py 'pali substring' 'burmese substring' [...pairs]; prints first 3 bids where both occur."""
import pathlib, re, sys, unicodedata
ROOT = pathlib.Path(__file__).resolve().parents[4]
ID = re.compile(r" (\^[0-9A-Za-z-]+)\s*$")
def blocks(t):
    r, c = {}, []
    for l in t.splitlines():
        if not l.strip(): continue
        c.append(l); m = ID.search(l)
        if m: r[m.group(1)] = c; c = []
    return r
SEG = []
for b in "123":
    for f in sorted((ROOT / f"AI_translation/pali/pi-{b}_split_chapters").glob("*.md")):
        bf = ROOT / f"AI_translation/burmese/pi-{b}-burmese-plain-rails_split_chapters" / f.name
        if not bf.exists(): continue
        pb = blocks(f.read_text(encoding="utf-8-sig")); bb = blocks(unicodedata.normalize("NFC", bf.read_text(encoding="utf-8-sig")))
        for k, pl in pb.items():
            SEG.append((b, k, " ".join(pl), " ".join(bb[k])))
a = sys.argv[1:]
for p, m in zip(a[::2], a[1::2]):
    hits = [(b, k) for b, k, P, M in SEG if p.lower() in P.lower() and m in M]
    print(f"{p!r} / {m!r}: {len(hits)} {hits[:3]}")
