"""Lines changed per chapter, pi-4 rails against the zero-shot (non-empty lines compared in order). Model:
pi-2-my/rails/diff_count.py.
usage: diff_count.py [--show N]   (--show prints up to N changed line pairs per chapter, shortened)"""
import difflib
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[5]
Z = ROOT / "AI_translation/burmese/pi-4-burmese-plain-zeroshot_split_chapters"
R = ROOT / "AI_translation/burmese/pi-4-burmese-plain-rails_split_chapters"
show = int(sys.argv[sys.argv.index("--show") + 1]) if "--show" in sys.argv else 0
tot = n_all = 0
for p in sorted(Z.glob("*.md")):
    a = [l for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]
    b = [l for l in (R / p.name).read_text(encoding="utf-8").splitlines() if l.strip()]
    ch = [(x, y) for x, y in zip(a, b) if x != y] + [("", y) for y in b[len(a):]] + [(x, "") for x in a[len(b):]]
    tot += len(ch)
    n_all += len(a)
    print(f"{p.name[:-3]}\t{len(ch)} of {len(a)} lines changed")
    for x, y in ch[:show]:
        sm = difflib.SequenceMatcher(None, x, y)
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op != "equal":
                print(f"   - «{x[max(0, i1 - 15):i2 + 5]}»\n   + «{y[max(0, j1 - 15):j2 + 5]}»")
print(f"total\t{tot} of {n_all} lines changed")
