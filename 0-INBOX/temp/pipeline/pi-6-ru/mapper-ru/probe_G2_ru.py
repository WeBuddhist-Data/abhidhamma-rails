"""G2 helper: print keywords, Pāli and Russian of segments.  usage: probe_G2_ru.py PART id [id ...] | PART from-to (indexes)"""
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_pi6_ru import read_keywords, read_pali, read_russian  # noqa: E402

part = sys.argv[1]
kw = read_keywords(part)
pa, ru = read_pali(part), read_russian(part)
ids = sys.argv[2:]
if len(ids) == 1 and ":" in ids[0]:
    a, b = ids[0].split(":")
    ids = [k for k, _ in kw[int(a):int(b)]]
kd = dict(kw)
for i in ids:
    print("=" * 20, i)
    print("KW:", ", ".join(kd.get(i, [])))
    print("PI:", pa.get(i, "").strip())
    print("RU:", ru.get(i, "").strip())
