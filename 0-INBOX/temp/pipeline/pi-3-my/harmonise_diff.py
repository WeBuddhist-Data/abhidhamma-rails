"""Lines changed per chapter: the chapter files now vs harmonise-backup/chapters/ (before the consistency pass).
usage: python3 -I -X utf8 harmonise_diff.py [-v [chapter-prefix]]   (-v: show the changed spans of each line)"""
import difflib, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
MD = ROOT / "AI_translation/burmese/pi-3-burmese-plain-zeroshot_split_chapters"
BK = HERE / "harmonise-backup/chapters"
v = "-v" in sys.argv
pref = [a for a in sys.argv[1:] if a != "-v"]
tot, per = 0, []
key = lambda p: (int(p.name.split("-")[0]) if p.name[0].isdigit() else 0)
for p in sorted(BK.glob("*.md"), key=key):
    a, b = p.read_text(encoding="utf-8").split("\n"), (MD / p.name).read_text(encoding="utf-8").split("\n")
    n = sum(1 for x, y in zip(a, b) if x != y) + abs(len(a) - len(b))
    tot += n
    per.append(f"{p.name.split('-')[0].split('.')[0]}: {n}")
    if v and n and (not pref or p.name.split("-")[0].split(".")[0] in pref):
        for i, (x, y) in enumerate(zip(a, b), 1):
            if x != y:
                sm = difflib.SequenceMatcher(None, x, y, autojunk=False)
                print(f"{p.name.split('-')[0]}:{i}", " | ".join(f"«{x[max(0,i1-12):i2+12]}» -> «{y[max(0,j1-12):j2+12]}»"
                      for op, i1, i2, j1, j2 in sm.get_opcodes() if op != "equal")[:900])
print(f"lines changed: {tot} ({', '.join(per)})")
