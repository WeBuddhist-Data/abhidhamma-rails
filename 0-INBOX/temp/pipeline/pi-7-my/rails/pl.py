"""Inspection helper (read only): show aligned Pāli / Burmese lines.
usage: pl.py id <segid>... | pl.py grep <pāli regex> [--b <burmese regex>] [--max N] [--zs]"""
import pathlib, re, sys, unicodedata
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
N = lambda s: unicodedata.normalize("NFC", s)
PD = ROOT / "AI_translation/pali/pi-7_split_chapters"
BD = HERE.parent / "review/fix-backup/rails-text" if "--bk" in sys.argv else ROOT / ("AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters" if "--zs" in sys.argv else
             "AI_translation/burmese/pi-7-burmese-plain-rails_split_chapters")
a = sys.argv[1:]
mx = int(a[a.index("--max") + 1]) if "--max" in a else 30
brx = re.compile(N(a[a.index("--b") + 1])) if "--b" in a else None
n = 0
for p in sorted(PD.glob("*.md")):
    pl = N(p.read_text(encoding="utf-8-sig")).split("\n"); bl = N((BD / p.name).read_text(encoding="utf-8")).split("\n")
    for k, (x, y) in enumerate(zip(pl, bl), 1):
        if a[0] == "id":
            ok = any(x.rstrip().endswith("^" + i) for i in a[1:] if not i.startswith("--"))
        else:
            ok = re.search(N(a[1]), x) and (brx is None or brx.search(y))
        if ok:
            n += 1
            if n <= mx:
                print(f"{p.name[:4]}:{k}\n  P: {x}\n  B: {y}")
print("lines:", n)
