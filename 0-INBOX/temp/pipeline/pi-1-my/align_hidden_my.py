"""For repeated Pāli sentences inside lines whose sentence counts differ: check that a Burmese rendering of the
sentence (taken from lines that do split evenly) occurs as a substring of the uneven line (Burmese copy of
pi-4-mr/rails/align_hidden.py: Burmese sentences end in «။»; the sentence end itself is not part of the substring,
since in the uneven line a «။» may be a «၊» or the sentence may run on; locations name the chapter file).
usage: align_hidden_my.py <pali_dir> <my_dir>"""
import re, sys, pathlib, collections
pd, md = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
ID = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")
SPLIT_PI = re.compile(r"(?<=[.?])\s+")
SPLIT_MY = re.compile(r"(?<=[။])\s+")
f = lambda p: [ID.sub("", l).strip() for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
loc = lambda p: p.name[:4] if p.name[1] == "-" and p.name[2].isdigit() else p.name.split("-")[0].split(".")[0]
known = collections.defaultdict(set); uneven = []
for p in sorted(pd.glob("*.md")):
    for i, (x, y) in enumerate(zip(f(p), f(md / p.name)), 1):
        xs, ys = SPLIT_PI.split(x), SPLIT_MY.split(y)
        if len(xs) == len(ys):
            for s, t in zip(xs, ys): known[s].add(t.rstrip("။"))
        else:
            uneven.append((loc(p), i, xs, y))
bad = 0
for ch, i, xs, y in uneven:
    for s in xs:
        if len(s) > 25 and s in known and not any(t in y for t in known[s]):
            bad += 1; print(f"{ch}:{i}  PĀLI: {s[:110]}\n      known: {sorted(known[s])[0][:110]}")
print("uneven lines", len(uneven), "| unmatched repeated sentences:", bad)
