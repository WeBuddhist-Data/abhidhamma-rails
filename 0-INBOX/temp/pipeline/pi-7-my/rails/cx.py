"""Inspection helper (read only): context of a Pāli / Burmese regex on one line or all lines (max 6 hits each).
usage: cx.py <ch-prefix:line | all> <pāli regex> <burmese regex> [--rails] [--w N]"""
import pathlib, re, sys, unicodedata
HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parents[4]
N = lambda s: unicodedata.normalize("NFC", s)
PD = ROOT / "AI_translation/pali/pi-7_split_chapters"
BD = (ROOT / "AI_translation/burmese/pi-7-burmese-plain-rails_split_chapters") if "--rails" in sys.argv else \
    (HERE / "dev-out" if "--dev" in sys.argv else HERE.parent / "review/fix-backup/rails-text")
w = int(sys.argv[sys.argv.index("--w") + 1]) if "--w" in sys.argv else 120
where, prx, brx = sys.argv[1], re.compile(N(sys.argv[2])), re.compile(N(sys.argv[3]))
n = 0
for p in sorted(PD.glob("*.md")):
    if where != "all" and not p.name.startswith(where.split(":")[0]):
        continue
    pl = N(p.read_text(encoding="utf-8-sig")).split("\n"); bl = N((BD / p.name).read_text(encoding="utf-8")).split("\n")
    for k, (a, b) in enumerate(zip(pl, bl), 1):
        if where != "all" and ":" in where and k != int(where.split(":")[1]):
            continue
        pm = [m for m in prx.finditer(a) if m.group(0)]
        if not pm:
            continue
        n += 1
        if n > 12:
            continue
        for m in pm[:3]:
            print(f"{p.name[:4]}:{k} P: {a[max(0, m.start() - w):m.end() + w]}")
        for m in [m for m in brx.finditer(b) if m.group(0)][:3]:
            print(f"{p.name[:4]}:{k} B: {b[max(0, m.start() - w):m.end() + w]}")
print("lines:", n)
