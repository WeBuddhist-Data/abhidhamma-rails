"""Inspection helper (read only; model pi-5-my/rails/seg.py): windows of one or more segments around a Pāli regex and a
Burmese regex.  usage: seg.py <id[,id…]> <pāli regex> <burmese regex> [--rails] [--w N]"""
import pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(HERE)); sys.dont_write_bytecode = True
import adherence_my as A  # noqa: E402
w = int(sys.argv[sys.argv.index("--w") + 1]) if "--w" in sys.argv else 60
P = A.segments(ROOT / "AI_translation/pali/pi-7_split_chapters")
B = A.segments(ROOT / ("AI_translation/burmese/pi-7-burmese-plain-rails_split_chapters" if "--rails" in sys.argv else
                       "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters"))
for i in sys.argv[1].split(","):
    print(f"[{i}]")
    for m in list(re.finditer(sys.argv[2], P[i]))[:4]:
        print("   P: …" + P[i][max(0, m.start() - w):m.end() + w] + "…")
    for m in list(re.finditer(sys.argv[3], B[i]))[:6]:
        print("   B: …" + B[i][max(0, m.start() - w):m.end() + w] + "…")
