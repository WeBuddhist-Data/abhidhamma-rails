"""Clause-level drift: split Pāli on , ; . ? – and Burmese on ၊ ။ – (lines with equal counts); report identical Pāli
clauses (> MIN chars, brackets removed) with different Burmese. usage: clause_scan.py [MIN]"""
import pathlib, re, sys, collections
R = pathlib.Path(__file__).resolve().parents[5]
P = R / "AI_translation/pali/pi-4_split_chapters"
M = R / "AI_translation/burmese/pi-4-burmese-plain-zeroshot_split_chapters"
MIN = int(sys.argv[1]) if len(sys.argv) > 1 else 12
ID = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")
BR = re.compile(r"\s*\[[^\]]*\]")
SP = re.compile(r"\s*(?:[,;.?!]|–)\s*(?=\S|$)")
SM = re.compile(r"\s*(?:[၊။]|–)\s*")
seen = collections.defaultdict(lambda: collections.defaultdict(list))
for p in sorted(P.glob("*.md")):
    for i, (x, y) in enumerate(zip(p.read_text(encoding="utf-8-sig").split("\n"), (M / p.name).read_text(encoding="utf-8").split("\n")), 1):
        if not x.strip() or x.startswith("#"):
            continue
        x, y = BR.sub("", ID.sub("", x)), BR.sub("", ID.sub("", y))
        x = re.sub(r"^\(\d+\) ", "", x); y = re.sub(r"^\(\d+\) ", "", y)
        xs = [s.strip(' "“”') for s in SP.split(x) if s.strip(' "')]
        ys = [s.strip(' “”') for s in SM.split(y) if s.strip()]
        if len(xs) != len(ys):
            continue
        for s, t in zip(xs, ys):
            s = s[0].lower() + s[1:] if s else s
            if len(s) >= MIN:
                seen[s][t].append(f"{p.name.split('-')[0]}:{i}")
n = 0
for s, v in sorted(seen.items()):
    if len(v) > 1:
        n += 1
        print("\nPĀLI:", s)
        for t, l in v.items():
            print("  ", l[:8], t)
print("\ndiffering clauses:", n)
