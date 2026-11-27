"""Inspection helper (read only): aligned Pāli / Burmese rails lines of segments, with chapter line numbers.
usage: show_seg.py <id[,id…]> [--grep REGEX]   (REGEX filters lines on Pāli or Burmese)"""
import pathlib, re, sys, unicodedata
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PALI = ROOT / "AI_translation/pali/pi-5_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-5-burmese-plain-rails_split_chapters"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
N = lambda s: unicodedata.normalize("NFC", s)
g = re.compile(sys.argv[sys.argv.index("--grep") + 1]) if "--grep" in sys.argv else None
want = sys.argv[1].split(",")
for p in sorted(PALI.glob("*.md")):
    pl = N(p.read_text(encoding="utf-8-sig")).split("\n")
    ml = N((OUT / p.name).read_text(encoding="utf-8")).split("\n")
    buf = []
    for k, l in enumerate(pl):
        if not l.strip():
            continue
        buf.append(k)
        m = ID.search(l)
        if m:
            if m.group(1) in want or "all" in want:
                for j in buf:
                    if g and not (g.search(pl[j]) or g.search(ml[j])):
                        continue
                    print(f"{p.name[:-3]}:{j+1} P: {pl[j]}")
                    print(f"{p.name[:-3]}:{j+1} B: {ml[j]}")
                print()
            buf = []
