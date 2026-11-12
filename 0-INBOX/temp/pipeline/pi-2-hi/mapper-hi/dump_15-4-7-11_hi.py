"""Dump segments of a pi-2 chapter with the default value of every keyword (for chapters 15, 4, 7, 11).

usage: python -I -X utf8 dump_15-4-7-11_hi.py <chapter> [id ...] [--miss]
  --miss  only print keywords whose default is missing (KeyError) or absent from the segment's Hindi
The default comes from the chapter script's TABLE/OVR if map_<chapter>_hi.py exists, else PI2.
"""
import importlib.util
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from map_sample_hi import PI2, pi2_value, read_keywords, read_hindi, read_pali, present, prior  # noqa: E402

args = sys.argv[1:]
only_miss = "--miss" in args
only_hi = "--hi" in args
args = [a for a in args if a not in ("--miss", "--hi")]
if only_hi:
    _h = read_hindi(args[0])
    for _i in args[1:]:
        print(f"=== {_i}\n{_h.get(_i)}\n")
    sys.exit()
ch, ids = args[0], set(args[1:])
resolver = None
p = HERE / f"map_{ch}_hi.py"
if p.exists():
    spec = importlib.util.spec_from_file_location("chmod", p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    resolver = m.resolver
hi, pi = read_hindi(ch), read_pali(ch)
for bid, kws in read_keywords(ch):
    if ids and bid not in ids:
        continue
    rows = []
    for kw in kws:
        try:
            v = resolver(bid, kw, kws) if resolver else pi2_value(kw, kws, PI2, bid, hi.get(bid))
            ok = present(v, hi.get(bid, ""))
        except KeyError:
            v, ok = "??? " + str({n: dict(c.most_common(3)) for n, c in prior(kw).items()}), False
        if not only_miss or not ok:
            rows.append(f"   {'  ' if ok else '!!'} {kw} = {v}")
    if rows or not only_miss:
        print(f"=== {bid}")
        if not only_miss:
            print("PI:", pi.get(bid))
            print("HI:", hi.get(bid))
        print("\n".join(rows))
