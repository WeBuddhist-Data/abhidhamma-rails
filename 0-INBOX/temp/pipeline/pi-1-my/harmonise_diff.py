"""usage: harmonise_diff.py [chapter-prefix ...] [-v N]: lines changed per chapter vs harmonise-backup/chapters-before/;
-v N prints N changed line pairs per chapter (words that differ shown)."""
import difflib, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
NOW = HERE.parents[3] / "AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters"
BEFORE = HERE / "harmonise-backup/chapters-before"
args = [a for a in sys.argv[1:] if not a.startswith("-v")]
V = int(next((a[2:] or "3" for a in sys.argv[1:] if a.startswith("-v")), "0") or 0)
tot = 0
for b in sorted(BEFORE.glob("*.md")):
    if args and not any(b.name.startswith(a) for a in args):
        continue
    x, y = b.read_text(encoding="utf-8").splitlines(), (NOW / b.name).read_text(encoding="utf-8").splitlines()
    ch = [(i, p, q) for i, (p, q) in enumerate(zip(x, y), 1) if p != q]
    tot += len(ch)
    print(f"{b.name}: {len(ch)} lines changed" + ("" if len(x) == len(y) else f" (LINE COUNT {len(x)} -> {len(y)})"))
    for i, p, q in ch[:V]:
        pw, qw = p.split(" "), q.split(" ")
        sm = difflib.SequenceMatcher(None, pw, qw)
        for op, a1, a2, b1, b2 in sm.get_opcodes():
            if op != "equal":
                print(f"   {i}: «{' '.join(pw[a1:a2])}» -> «{' '.join(qw[b1:b2])}»")
print("total lines changed:", tot)
