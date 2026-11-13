"""Compare my keyword values with the other pi-7 mapped files in this folder (shared keywords whose value sets differ).
usage: python -I -B -X utf8 cmp_3-02_3-06_hi.py
"""
import collections, pathlib
HERE = pathlib.Path(__file__).resolve().parent
MINE = {"3-02-culantaraduka", "3-03-asavagocchaka", "3-04-sannojanagocchaka", "3-05-ganthagocchaka",
        "3-06-oghayogagocchaka"}


def load(files):
    by = collections.defaultdict(collections.Counter)
    for p in files:
        for line in p.read_text(encoding="utf-8").splitlines():
            if "] " in line:
                for pair in line.split("] ", 1)[1].split(", "):
                    if "=" in pair:
                        k, v = pair.split("=", 1)
                        by[k[:1].lower() + k[1:]][v] += 1
    return by


allf = sorted(HERE.glob("*.mapped.md"))
mine = load([p for p in allf if p.name[:-len(".mapped.md")] in MINE])
other = load([p for p in allf if p.name[:-len(".mapped.md")] not in MINE])
print("other files:", len([p for p in allf if p.name[:-len(".mapped.md")] not in MINE]))
for k in sorted(mine):
    if k in other and set(mine[k]) != set(other[k]):
        print(k, "| mine:", dict(mine[k]), "| other:", dict(other[k].most_common(4)))
