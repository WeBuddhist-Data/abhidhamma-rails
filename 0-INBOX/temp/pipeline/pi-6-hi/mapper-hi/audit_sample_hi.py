"""Audit a pi-6 mapped file: every keyword (lower-case first letter) with the distinct values it got, where the
default value came from (PI6 / PI2 / CH2 / stripped -ti, -ñca), and its values in the pi-1..5 Hindi maps.
usage: python -I -X utf8 audit_sample_hi.py <file> [only-multi]"""
import collections
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import HERE, PI6, PI2, CH2, BARE, lc, prior, _strip_particles  # noqa: E402

f = sys.argv[1]
only_multi = len(sys.argv) > 2
vals = collections.defaultdict(collections.Counter)
for line in (HERE / f"{f}.mapped.md").read_text(encoding="utf-8").splitlines():
    if "] " in line:
        for pair in line.split("] ", 1)[1].split(", "):
            k, v = pair.split("=", 1)
            vals[lc(k)][v] += 1


def source(k):
    for cand in [k] + _strip_particles(k):
        for name, t in (("PI6", PI6), ("PI2", PI2), ("CH2", CH2)):
            if cand in t:
                return ("BARE-or-" if cand in BARE else "") + name + ("" if cand == k else f"({cand})")
    return "?"


for k in sorted(vals):
    if only_multi and len(vals[k]) < 2:
        continue
    pr = {n: dict(c.most_common(2)) for n, c in prior(k).items()}
    print(k, "|", source(k), "|", dict(vals[k]), "| prior", pr if pr else "-")
