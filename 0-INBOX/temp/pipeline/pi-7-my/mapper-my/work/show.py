"""show.py ch sid [sid …]: the keywords, the Pāli and the Burmese of a segment (read-only helper)."""
import sys, re, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[6]
D = pathlib.Path(__file__).resolve().parents[1]
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
def segs(p):
    out, buf = {}, []
    for l in pathlib.Path(p).read_text(encoding="utf-8-sig").splitlines():
        if not l.strip(): continue
        buf.append(l)
        m = ID.search(l)
        if m:
            out[m.group(1)] = "\n".join(buf); buf = []
    return out
ch = sys.argv[1]
kw = {l[1:].split("] ", 1)[0]: l.split("] ", 1)[1] for l in (D / f"{ch}.keywords.md").read_text(encoding="utf-8").splitlines()}
pa = segs(ROOT / f"AI_translation/pali/pi-7_split_chapters/{ch}.md")
my = segs(ROOT / f"AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters/{ch}.md")
mp = D / f"{ch}.mapped.md"
mm = {l[1:].split("] ", 1)[0]: l.split("] ", 1)[1] for l in mp.read_text(encoding="utf-8").splitlines()} if mp.exists() else {}
for sid in sys.argv[2:]:
    print("=====", sid)
    print("KW:", kw.get(sid))
    if sid in mm: print("MAP:", mm[sid])
    print("PI:", pa.get(sid))
    print("MY:", my.get(sid))
