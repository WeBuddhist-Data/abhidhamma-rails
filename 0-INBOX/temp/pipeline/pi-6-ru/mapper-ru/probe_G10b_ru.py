"""G10b probe (writes nothing).
  python -I -X utf8 -B probe_G10b_ru.py seg PART id [id ...]     Pāli + Russian (+ keywords) of segments
  python -I -X utf8 -B probe_G10b_ru.py kw PART kw [kw ...]      every segment of PART listing the keyword(s)
  python -I -X utf8 -B probe_G10b_ru.py unmapped                 keywords of 10-05 … 10-13 the G10a table cannot resolve
PART may be the short form 10-05."""
import collections
import importlib
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_pi6_ru import read_keywords, read_pali, read_russian  # noqa: E402

PARTS = [f"10-{i:02d}-indriyayamaka" for i in range(5, 14)]


def full(p):
    return p if p.endswith("yamaka") else p + "-indriyayamaka"


mode = sys.argv[1]
if mode == "seg":
    part = full(sys.argv[2])
    pa, ru, kws = read_pali(part), read_russian(part), dict(read_keywords(part))
    for i in sys.argv[3:]:
        print("=" * 30, i)
        print("KW:", ", ".join(kws.get(i, [])))
        print("PA:", pa.get(i, "<none>"))
        print("RU:", ru.get(i, "<none>"))
elif mode == "kw":
    part = full(sys.argv[2])
    pa, ru = read_pali(part), read_russian(part)
    want = set(sys.argv[3:])
    for bid, kws in read_keywords(part):
        if want & set(kws):
            print("=" * 30, bid)
            print("KW:", ", ".join(kws))
            print("PA:", pa.get(bid, "<none>"))
            print("RU:", ru.get(bid, "<none>"))
elif mode == "unmapped":
    g = importlib.import_module("map_G10b_ru") if len(sys.argv) > 2 else importlib.import_module("map_G10a_ru")
    cnt, where = collections.Counter(), collections.defaultdict(list)
    for part in PARTS:
        res = g.resolver_for(part)
        for bid, kws in read_keywords(part):
            for kw in kws:
                try:
                    res(bid, kw, kws)
                except KeyError:
                    cnt[kw] += 1
                    where[kw].append(bid)
    for kw, n in cnt.most_common():
        print(n, kw, where[kw][:4])
