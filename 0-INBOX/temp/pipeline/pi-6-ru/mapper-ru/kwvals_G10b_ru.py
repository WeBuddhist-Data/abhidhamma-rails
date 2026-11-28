"""G10b review helper (writes nothing): every distinct keyword of the mapped 10-05 … 10-13 files with its values and
counts.  python -I -X utf8 -B kwvals_G10b_ru.py"""
import collections
import pathlib
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
d = collections.defaultdict(collections.Counter)
for i in range(5, 14):
    for line in (HERE / f"10-{i:02d}-indriyayamaka.mapped.md").read_text(encoding="utf-8").splitlines():
        for pair in line.split("] ", 1)[1].split(", "):
            k, v = pair.split("=", 1)
            d[k][v] += 1
for k in sorted(d, key=lambda x: x.lower()):
    print(k, "=", "; ".join(f"{v} ({n})" for v, n in d[k].most_common()))
