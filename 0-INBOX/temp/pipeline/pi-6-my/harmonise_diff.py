"""Lines changed per chapter: the chapter files now vs harmonise-backup/chapters/ (before the consistency pass).
usage: python3 -I -X utf8 harmonise_diff.py [-v [chapter-prefix ...]]   (-v: show the changed spans of each line)
Model: pi-5-my/harmonise_diff.py (read only)."""
import difflib, pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
MD = ROOT / "AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters"
BK = HERE / "harmonise-backup/chapters"
v = "-v" in sys.argv
pref = [a for a in sys.argv[1:] if a != "-v"]
tot, per = 0, []
name = lambda p: p.name[:-3].rsplit("-", 1)[0] if p.name[0].isdigit() else p.name[:-3]
key = lambda p: [int(x) for x in re.findall(r"\d+", name(p))] or [0]
for p in sorted(BK.glob("*.md"), key=key):
    a, b = p.read_text(encoding="utf-8").split("\n"), (MD / p.name).read_text(encoding="utf-8").split("\n")
    n = sum(1 for x, y in zip(a, b) if x != y) + abs(len(a) - len(b))
    tot += n
    per.append(f"{name(p)}: {n}")
    if v and n and (not pref or any(name(p).startswith(x) for x in pref)):
        for i, (x, y) in enumerate(zip(a, b), 1):
            if x != y:
                sm = difflib.SequenceMatcher(None, x, y, autojunk=False)
                print(f"{name(p)}:{i}", " | ".join(f"«{x[max(0,i1-12):i2+12]}» -> «{y[max(0,j1-12):j2+12]}»"
                      for op, i1, i2, j1, j2 in sm.get_opcodes() if op != "equal")[:1500])
print(f"lines changed: {tot} ({', '.join(per)})")
