"""Inspection helper (read only): for the misses of one keyword, the Pāli window around the keyword and the Burmese
window around a regex. usage: kwin.py <adherence report> <keyword> <burmese regex> [--rails] [--w N] [--max N]"""
import pathlib, re, sys, unicodedata
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(HERE)); sys.dont_write_bytecode = True
import adherence_my as A  # noqa: E402
N = lambda s: unicodedata.normalize("NFC", s)
w = int(sys.argv[sys.argv.index("--w") + 1]) if "--w" in sys.argv else 50
mx = int(sys.argv[sys.argv.index("--max") + 1]) if "--max" in sys.argv else 99
P = A.segments(ROOT / "AI_translation/pali/pi-7_split_chapters")
B = A.segments(ROOT / ("AI_translation/burmese/pi-7-burmese-plain-rails_split_chapters" if "--rails" in sys.argv else
                       "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters"))
ids = [N(l).split("\t")[0].strip() for l in open(sys.argv[1], encoding="utf-8") if "\t" in l and N(l).split("\t")[1] == N(sys.argv[2])]
for i in ids[:mx]:
    print(f"[{i}]")
    for m in list(re.finditer(re.escape(N(sys.argv[2])), P[i]))[:3]:
        print("   P: …" + P[i][max(0, m.start() - w):m.end() + w] + "…")
    for m in list(re.finditer(N(sys.argv[3]), B[i]))[:4]:
        print("   B: …" + B[i][max(0, m.start() - w):m.end() + w] + "…")
