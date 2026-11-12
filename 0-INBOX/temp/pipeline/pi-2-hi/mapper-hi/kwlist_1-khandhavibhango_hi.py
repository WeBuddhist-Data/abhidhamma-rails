"""List the unique keywords of a pi-2 chapter with counts and the pi-1/3/4/5 Hindi map values.

usage: python -I -X utf8 kwlist_1-khandhavibhango_hi.py <chapter>
"""
import collections
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
MAPS = [ROOT / "AI_translation" / "hindi" / f"pi-{n}-keywords-by-reference-pali-hindi-plain.md" for n in (1, 3, 4, 5)]


def lc(k):
    return k[:1].lower() + k[1:]


def load_maps():
    out = collections.defaultdict(collections.Counter)
    for i, p in enumerate(MAPS):
        for line in p.read_text(encoding="utf-8").splitlines():
            if "] " not in line:
                continue
            for pair in line.split("] ", 1)[1].split(", "):
                if "=" in pair:
                    k, v = pair.split("=", 1)
                    out[(i, lc(k.strip()))][v] += 1
    return out


if __name__ == "__main__":
    ch = sys.argv[1]
    cnt = collections.Counter()
    for line in (HERE / f"{ch}.keywords.md").read_text(encoding="utf-8").splitlines():
        if line.strip():
            for k in line.split("] ", 1)[1].split(", "):
                cnt[lc(k.strip())] += 1
    m = load_maps()
    for k, c in sorted(cnt.items()):
        vals = []
        for i, n in enumerate((1, 3, 4, 5)):
            if (i, k) in m:
                vals.append(f"pi{n}: " + " | ".join(f"{v}({x})" for v, x in m[(i, k)].most_common(3)))
        print(f"{c:4d} {k} :: " + " ;; ".join(vals))
