"""Cross-chapter alignment: identical Pāli sentences must have identical Burmese (Burmese copy of
pi-4-mr/align_check.py). Changes against the Marathi script: the Burmese sentence end is «။» (the Pāli still splits
on «.» / «?»), and locations name the chapter file («2-03:12», not «2:12», since 2-01 … 2-05 share the «2»).
Sentences are compared only on lines where Pāli and Burmese split into the same number of sentences.
usage: align_check_my.py <pali_dir> <my_dir> [--all]"""
import re, sys, pathlib, collections
pd, md = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
ID = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")
SPLIT_PI = re.compile(r"(?<=[.?])\s+")
SPLIT_MY = re.compile(r"(?<=[။])\s+")
f = lambda p: [ID.sub("", l) for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
loc = lambda p: p.name[:4] if p.name[1] == "-" and p.name[2].isdigit() else p.name.split("-")[0].split(".")[0]
seen = collections.defaultdict(lambda: collections.defaultdict(list))
skipped = 0
for p in sorted(pd.glob("*.md")):
    a, b = f(p), f(md / p.name)
    for i, (x, y) in enumerate(zip(a, b), 1):
        xs, ys = SPLIT_PI.split(x.strip()), SPLIT_MY.split(y.strip())
        if len(xs) != len(ys):
            skipped += 1
            xs, ys = [x.strip()], [y.strip()]
        for s, t in zip(xs, ys):
            if len(s) > 25:
                seen[s][t].append(f"{loc(p)}:{i}")
bad = {s: v for s, v in seen.items() if len(v) > 1}
print(f"repeated Pāli sentences: {sum(1 for v in seen.values() if sum(map(len, v.values())) > 1)}; "
      f"with differing Burmese: {len(bad)}; lines compared whole: {skipped}")
for s, v in list(bad.items())[: (10**6 if '--all' in sys.argv else 15)]:
    print("\nPĀLI:", s[:150])
    for t, locs in v.items():
        print("  ", locs[:6], t[:150])
