"""Probe a chapter (10/12/13/14 mapper): every unique keyword with its current default (PI2 + my tables),
the prior pi-1/3/4/5 values, and for which segments the default is absent from the Hindi.

usage: python -I -X utf8 probe_10_12_13_14_hi.py <chapter> [missing-only]
"""
import collections
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import PI2, CH2, pi2_value, prior, read_keywords, read_hindi, present, lc, NDE  # noqa
import common_10_12_13_14_hi as C  # noqa

ch = sys.argv[1]
only_missing = len(sys.argv) > 2
table = {**PI2, **C.T_ALL, **C.CHAPTER_T.get(ch, {})}
hi = read_hindi(ch)
info = collections.OrderedDict()
for bid, kws in read_keywords(ch):
    for kw in kws:
        k = lc(kw)
        d = info.setdefault(k, {"n": 0, "absent": [], "val": None})
        d["n"] += 1
        try:
            v = C.resolve(ch, bid, kw, kws, hi.get(bid))
        except KeyError:
            v = None
        d["val"] = v
        if v is not None and v != NDE and not present(v, hi.get(bid, "")):
            d["absent"].append((bid, v))
for k, d in sorted(info.items()):
    if only_missing and d["val"] is not None and not d["absent"]:
        continue
    pr = prior(k)
    ps = " ;; ".join(f"pi{n}: " + " | ".join(f"{v}({c})" for v, c in cnt.most_common(3)) for n, cnt in pr.items())
    ab = ""
    if d["absent"]:
        ab = " ABSENT " + " ".join(f"{b}[{v}]" for b, v in d["absent"][:6])
    print(f"{d['n']:3d} {k} = {d['val']}{ab} :: {ps}")
