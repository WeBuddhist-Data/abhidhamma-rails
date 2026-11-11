"""Look up Pāli lemmas in the Hindi pi-3/4/5 termbases (head-word match, case-insensitive).

usage: python -I -X utf8 tb_4-02_4-03.py <regex> [<regex> ...]
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
HI = ROOT / "AI_translation" / "hindi"
files = [HI / f"pi-{n}-pali-hindi-termbase-plain.md" for n in (3, 4, 5)]
lines = {f.name[:4]: f.read_text(encoding="utf-8").splitlines() for f in files}
for pat in sys.argv[1:]:
    rx = re.compile(r"^(?:" + pat + r")[^:]*:", re.I)
    print("####", pat)
    n = 0
    for book, ls in lines.items():
        for l in ls:
            if rx.match(l):
                print(" ", book, l[:260])
                n += 1
                if n > 6:
                    break
