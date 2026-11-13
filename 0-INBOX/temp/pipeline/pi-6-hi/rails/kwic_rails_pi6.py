"""Show Pāli/Hindi line pairs whose Hindi (or, with -p, Pāli) matches a regex.

usage: python -I -X utf8 kwic_rails_pi6.py <regex> [per_file=2] [-p] [-f file-substring]
"""
import pathlib, re, sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
P = ROOT / "AI_translation/pali/pi-6_split_chapters"
H = ROOT / "AI_translation/hindi/pi-6-hindi-plain-rails_split_chapters"
args = sys.argv[1:]
pal = "-p" in args
fsub = None
if "-f" in args:
    fsub = args[args.index("-f") + 1]
    args = [a for i, a in enumerate(args) if a != "-f" and (i == 0 or args[i - 1] != "-f")]
args = [a for a in args if a != "-p"]
rx = re.compile(args[0])
per = int(args[1]) if len(args) > 1 else 2

def lines(f):
    return [l for l in f.read_text(encoding="utf-8-sig").splitlines() if l.strip()]

for pf in sorted(P.glob("*.md")):
    if fsub and fsub not in pf.name:
        continue
    pl, hl = lines(pf), lines(H / pf.name)
    n = 0
    for a, b in zip(pl, hl):
        if rx.search(a if pal else b):
            print(f"[{pf.stem}] P: {a}\n{'':{len(pf.stem)+3}}H: {b}")
            n += 1
            if n >= per:
                break
