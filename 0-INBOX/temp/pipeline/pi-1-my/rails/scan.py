"""Inspection helper: Pāli lines matching a regex, with the Burmese matches of a second regex on the same line.
usage: scan.py [--rails] '<pāli regex>' '<burmese regex>' [max]"""
import pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[5]
a = sys.argv[1:]; rails = "--rails" in a; a = [x for x in a if x != "--rails"]
P = ROOT / "AI_translation/pali/pi-1_split_chapters"
M = ROOT / ("AI_translation/burmese/pi-1-burmese-plain-rails_split_chapters" if rails
            else "AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters")
px, mx = re.compile(a[0]), re.compile(a[1]); mxn = int(a[2]) if len(a) > 2 else 10**6
k = 0
for p in sorted(P.glob("*.md")):
    A = [l for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]
    B = [l for l in (M / p.name).read_text(encoding="utf-8").splitlines() if l.strip()]
    for i, (x, y) in enumerate(zip(A, B), 1):
        pm = [x[max(0, m.start() - 25): m.end() + 25] for m in px.finditer(x)]
        if not pm: continue
        k += 1
        if k > mxn: continue
        bm = [y[max(0, m.start() - 20): m.end() + 20] for m in mx.finditer(y)]
        print(f"{p.name[:4]}:{i} P×{len(pm)} M×{len(bm)} | {pm[0]} | {' ¦ '.join(bm[:3])}")
print("lines:", k)
