"""Read-only: print Pāli, Burmese and the current mapping of segments (any chapter).
usage: python3 -I -X utf8 harmonise_show.py [-k keyword] ID ...   (-k: print only that keyword's pair)"""
import sys, re, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
MY = ROOT / "AI_translation/burmese/pi-3-burmese-plain-zeroshot_split_chapters"
PI = ROOT / "AI_translation/pali/pi-3_split_chapters"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")


def segments(path):
    out, buf = {}, []
    for l in path.read_text(encoding="utf-8-sig").splitlines():
        if not l.strip():
            continue
        buf.append(l)
        m = ID.search(l)
        if m:
            out[m.group(1)] = " ".join(buf)
            buf = []
    return out


args = sys.argv[1:]
kw = None
if args and args[0] == "-k":
    kw, args = args[1], args[2:]
for f in sorted(HERE.glob("*.mapped.md")):
    ch = f.name.split(".")[0]
    rows = dict(l.split("] ", 1) for l in f.read_text(encoding="utf-8").splitlines())
    rows = {k[1:]: v for k, v in rows.items()}
    hit = [s for s in args if s in rows]
    if not hit:
        continue
    my, pa = segments(MY / f"{ch}.md"), segments(PI / f"{ch}.md")
    for s in hit:
        print(f"== {s} ({ch})")
        print("PI:", pa.get(s))
        print("MY:", my.get(s))
        pairs = rows[s].split(", ")
        if kw:
            pairs = [p for p in pairs if p.split("=", 1)[0] == kw]
        print("MAP:", " | ".join(pairs))
