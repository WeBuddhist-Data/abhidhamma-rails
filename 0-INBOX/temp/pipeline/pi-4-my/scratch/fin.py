"""fin.py REGEX [width]: lines of pi-1/2/3 Pāli matching REGEX, with their FINAL (rails) Burmese line."""
import pathlib, re, sys
R = pathlib.Path(__file__).resolve().parents[5]
rx = re.compile(sys.argv[1]); w = int(sys.argv[2]) if len(sys.argv) > 2 else 1500
for b in "123":
    P = R / f"AI_translation/pali/pi-{b}_split_chapters"; M = R / f"AI_translation/burmese/pi-{b}-burmese-plain-rails_split_chapters"
    for p in sorted(P.glob("*.md")):
        x = p.read_text(encoding="utf-8-sig").split("\n"); y = (M / p.name).read_text(encoding="utf-8").split("\n")
        for i, (s, t) in enumerate(zip(x, y), 1):
            if rx.search(s):
                j = rx.search(s).start()
                print(f"pi-{b} {p.name}:{i}\n  P: {s[max(0,j-200):j+w]}\n  M: {t[:w*3]}")
