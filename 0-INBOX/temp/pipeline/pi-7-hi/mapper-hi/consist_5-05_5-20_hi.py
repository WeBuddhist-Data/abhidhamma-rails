"""Compare the 5-05..5-20 values with the other pi-7 mapped files (same keyword, lower-case first letter).
Prints keywords whose value sets do not overlap. Writes nothing.
usage: python -I -B -X utf8 consist_5-05_5-20_hi.py
"""
import collections, pathlib
HERE = pathlib.Path(__file__).resolve().parent
MINE = {f"5-{n:02d}" for n in range(5, 21)}
mine, other = collections.defaultdict(collections.Counter), collections.defaultdict(collections.Counter)
for p in HERE.glob("*.mapped.md"):
    tgt = mine if p.name[:4] in MINE else other
    for line in p.read_text(encoding="utf-8").splitlines():
        if "] " not in line:
            continue
        for pair in line.split("] ", 1)[1].split(", "):
            if "=" in pair:
                k, v = pair.split("=", 1)
                tgt[k[:1].lower() + k[1:]][v] += 1
for k in sorted(mine):
    if k in other and not set(mine[k]) & set(other[k]):
        print(k, "| mine:", dict(mine[k]), "| other:", dict(other[k].most_common(3)))
