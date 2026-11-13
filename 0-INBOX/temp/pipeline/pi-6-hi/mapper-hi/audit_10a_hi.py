"""Audit the 10-01 .. 10-06 maps: every keyword (lower-case first letter) with its values, the table that gave the
default (T / IND / PI6 / PI2 / CH2, after -ti/-ñca stripping) and the pi-1..5 prior values.
usage: python -I -X utf8 audit_10a_hi.py [only-fallback]"""
import collections
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import HERE, PI6, PI2, CH2, lc, prior, _strip_particles  # noqa: E402
from map_10_common_hi import IND  # noqa: E402
from map_10a_hi import FILES, T  # noqa: E402

only_fb = len(sys.argv) > 1
vals = collections.defaultdict(collections.Counter)
for f in FILES:
    for line in (HERE / f"{f}.mapped.md").read_text(encoding="utf-8").splitlines():
        if "] " in line:
            for pair in line.split("] ", 1)[1].split(", "):
                k, v = pair.split("=", 1)
                vals[lc(k)][v] += 1


def source(k):
    for cand in [k] + _strip_particles(k):
        for name, t in (("T", T), ("IND", IND), ("PI6", PI6), ("PI2", PI2), ("CH2", CH2)):
            if cand in t:
                return name + ("" if cand == k else f"({cand})")
    return "?"


for k in sorted(vals):
    s = source(k)
    if only_fb and not (s.startswith("PI2") or s.startswith("CH2") or len(vals[k]) > 1):
        continue
    pr = {n: dict(c.most_common(2)) for n, c in prior(k).items()}
    print(k, "|", s, "|", dict(vals[k]), "| prior", pr if pr else "-")
