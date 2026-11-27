"""Inspection helper (read only): Burmese lines matching B-regex whose Pāli line does NOT match P-regex (or with --both,
does), showing the windows. usage: pair2.py <burmese regex> <pāli regex> [--both] [--max N] [--w N] [--rails]"""
import pathlib, re, sys, unicodedata
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
N = lambda s: unicodedata.normalize("NFC", s)
PD = ROOT / "AI_translation/pali/pi-7_split_chapters"
BD = ROOT / ("AI_translation/burmese/pi-7-burmese-plain-rails_split_chapters" if "--rails" in sys.argv else
             "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters")
brx, prx = re.compile(N(sys.argv[1])), re.compile(N(sys.argv[2]))
mx = int(sys.argv[sys.argv.index("--max") + 1]) if "--max" in sys.argv else 30
w = int(sys.argv[sys.argv.index("--w") + 1]) if "--w" in sys.argv else 80
n = 0
for p in sorted(PD.glob("*.md")):
    pl = N(p.read_text(encoding="utf-8-sig")).splitlines(); bl = N((BD / p.name).read_text(encoding="utf-8")).splitlines()
    for k, (a, b) in enumerate(zip(pl, bl), 1):
        m = brx.search(b)
        if m and (bool(prx.search(a)) == ("--both" in sys.argv)):
            n += 1
            if n <= mx:
                print(f"{p.name[:5]}:{k}\n   B: …{b[max(0, m.start() - w):m.end() + w]}…\n   P: {a[:300]}")
print("lines", n)
