"""Shortest final pi-1/2/3 lines whose Pāli matches each regex (read only). usage: short.py N REGEX [REGEX ...]"""
import pathlib, re, sys, unicodedata
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
ID = re.compile(r" (\^[0-9A-Za-z-]+)\s*$")
def blocks(t):
    r, c = {}, []
    for l in t.splitlines():
        if not l.strip(): continue
        c.append(l); m = ID.search(l)
        if m: r[m.group(1)] = c; c = []
    return r
ALL = []
for b in "123":
    for f in sorted((ROOT / f"AI_translation/pali/pi-{b}_split_chapters").glob("*.md")):
        bf = ROOT / f"AI_translation/burmese/pi-{b}-burmese-plain-rails_split_chapters" / f.name
        if not bf.exists(): continue
        pb = blocks(f.read_text(encoding="utf-8-sig")); bb = blocks(unicodedata.normalize("NFC", bf.read_text(encoding="utf-8-sig")))
        for k, pl in pb.items():
            for i, p in enumerate(pl):
                ALL.append((b, k, p, bb[k][i]))
N = int(sys.argv[1])
for rx in sys.argv[2:]:
    r = re.compile(rx)
    hits = sorted((x for x in ALL if r.search(x[2])), key=lambda x: len(x[2]))
    print(f"##### {rx}  ({len(hits)} lines)")
    for b, k, p, m in hits[:N]:
        print(f"  pi-{b} {k}\n  P: {p[:400]}\n  M: {m[:400]}")
