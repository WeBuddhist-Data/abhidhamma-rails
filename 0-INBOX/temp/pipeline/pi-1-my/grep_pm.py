"""Pāli regex -> the matching Pāli lines and their Burmese lines (non-empty line numbers).
usage: grep_pm.py REGEX [chapter-prefix ...] [-n MAX] [-w WIDTH] [-my REGEX2 (filter on the Burmese line)]"""
import pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PD = ROOT / "AI_translation/pali/pi-1_split_chapters"
MD = ROOT / "AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters"
a = sys.argv[1:]
rx = re.compile(a.pop(0))
opt = lambda k, d: (a.pop(a.index(k) + 1), a.remove(k))[0] if k in a else d
MAX, W, MY = int(opt("-n", "8")), int(opt("-w", "600")), opt("-my", None)
myrx = re.compile(MY) if MY else None
n = 0
for p in sorted(PD.glob("*.md")):
    if a and not any(p.name.startswith(x) for x in a):
        continue
    x = [l for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
    y = [l for l in (MD / p.name).read_text(encoding="utf-8").splitlines() if l.strip()]
    for i, (s, t) in enumerate(zip(x, y), 1):
        if rx.search(s) and (not myrx or myrx.search(t)):
            n += 1
            if n <= MAX:
                print(f"{p.name[:4]}:{i}\n  P: {s[:W]}\n  B: {t[:W]}")
print("matches:", n)
