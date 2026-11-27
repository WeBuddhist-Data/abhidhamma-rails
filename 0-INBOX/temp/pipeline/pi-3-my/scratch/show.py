"""show.py <chapter-prefix> <line# ...> : nonblank line i (1-based) of Pāli and Burmese (as align_check counts)."""
import pathlib, sys, re
R = pathlib.Path(__file__).resolve().parents[5]
P = R / "AI_translation/pali/pi-3_split_chapters"; M = R / "AI_translation/burmese/pi-3-burmese-plain-zeroshot_split_chapters"
pre = sys.argv[1]
f = [p for p in sorted(P.glob("*.md")) if p.name.split("-")[0].split(".")[0] == pre][0]
a = [l for l in f.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
b = [l for l in (M / f.name).read_text(encoding="utf-8-sig").splitlines() if l.strip()]
for n in sys.argv[2:]:
    i = int(n) - 1
    print(f"--{f.name}:{n}\nP: {a[i]}\nM: {b[i]}")
