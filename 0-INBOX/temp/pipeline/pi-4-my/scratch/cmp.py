"""cmp.py ch:line ch:line : the two Burmese lines (raw file line numbers) split at ၊ / ။, aligned by difflib."""
import pathlib, re, sys, difflib
R = pathlib.Path(__file__).resolve().parents[5]
P = R / "AI_translation/pali/pi-4_split_chapters"; M = R / "AI_translation/burmese/pi-4-burmese-plain-zeroshot_split_chapters"
def get(spec):
    ch, n = spec.split(":"); f = next(p for p in P.glob("*.md") if p.name.split("-")[0] == ch)
    return (f.read_text(encoding="utf-8-sig").split("\n")[int(n) - 1], (M / f.name).read_text(encoding="utf-8").split("\n")[int(n) - 1])
(pa, ma), (pb, mb) = get(sys.argv[1]), get(sys.argv[2])
sa = re.split(r"(?<=[၊။])\s+|\s+–\s+", ma); sb = re.split(r"(?<=[၊။])\s+|\s+–\s+", mb)
sm = difflib.SequenceMatcher(None, sa, sb, autojunk=False)
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op == "equal":
        print(f"= ({i2-i1} same) {sa[i1][:60]} … {sa[i2-1][-40:]}")
    else:
        for x in sa[i1:i2]: print("  A:", x)
        for x in sb[j1:j2]: print("  B:", x)
        print("  --")
if "-p" in sys.argv:
    print("PĀLI A:", pa); print("PĀLI B:", pb)
