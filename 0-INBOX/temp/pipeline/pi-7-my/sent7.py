"""Align differences in full (read-only): the same sentence units as pi-1-my/align_check_my.py, each differing Pāli
sentence with every Burmese rendering (full) and the changed spans against the most frequent one.
usage: sent7.py [substring-of-Pāli]"""
import re, sys, pathlib, collections, difflib
HERE = pathlib.Path(__file__).resolve().parent; R = HERE.parents[3]
pd = R / "AI_translation/pali/pi-7_split_chapters"; md = R / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters"
ID = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")
f = lambda p: [ID.sub("", l) for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
seen = collections.defaultdict(lambda: collections.defaultdict(list))
for p in sorted(pd.glob("*.md")):
    for i, (x, y) in enumerate(zip(f(p), f(md / p.name)), 1):
        xs, ys = re.split(r"(?<=[.?])\s+", x.strip()), re.split(r"(?<=[။])\s+", y.strip())
        if len(xs) != len(ys):
            xs, ys = [x.strip()], [y.strip()]
        for s, t in zip(xs, ys):
            if len(s) > 25:
                seen[s][t].append(f"{p.name[:4]}:{i}")
q = sys.argv[1] if len(sys.argv) > 1 else ""
for s, v in seen.items():
    if len(v) < 2 or q not in s:
        continue
    print("\nPĀLI:", s)
    vs = sorted(v.items(), key=lambda kv: -len(kv[1]))
    base = vs[0][0]
    for t, locs in vs:
        print(f"  [{len(locs)}] {locs[:8]}")
        if t is base:
            print("     ", t[:600])
        else:
            sm = difflib.SequenceMatcher(None, base, t, autojunk=False)
            print("      ", " | ".join(f"«{base[max(0,a1-25):a2+10]}» -> «{t[max(0,b1-25):b2+10]}»"
                                     for op, a1, a2, b1, b2 in sm.get_opcodes() if op != "equal")[:1200])
