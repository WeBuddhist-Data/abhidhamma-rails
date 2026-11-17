"""Review helper for chapter 18: every distinct keyword with its resolved value(s), the segments where it occurs,
and a presence flag (!! = value not found in that segment's Russian and not a listed exception).
usage: python -I -X utf8 uniq_18.py [--miss]"""
import collections
import pathlib
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import map_18_ru as M  # noqa: E402
from map_common_pi2_ru import NDE, present, read_keywords, read_russian  # noqa: E402

ru, res, allowed = read_russian(M.PART), M.resolver(), M.allowed()
seen = collections.OrderedDict()
for bid, kws in read_keywords(M.PART):
    for kw in kws:
        try:
            v = res(bid, kw, kws)
        except KeyError:
            v = "???"
        ok = v != "???" and (v == NDE or present(v, ru.get(bid, "")) or (bid, kw) in allowed)
        seen.setdefault((kw, v), []).append(bid + ("" if ok else "!!"))
only_miss = "--miss" in sys.argv
for (kw, v), ids in sorted(seen.items(), key=lambda x: x[0][0].lower()):
    if only_miss and not any(i.endswith("!!") for i in ids):
        continue
    print(f"{kw}={v}\t[{len(ids)}] {' '.join(ids[:6])}{' …' if len(ids) > 6 else ''}")
