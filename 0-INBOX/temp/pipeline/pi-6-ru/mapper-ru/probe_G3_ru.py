"""G3 helper (writes nothing).
usage:
  python -I -X utf8 -B probe_G3_ru.py kw [PART ...]          distinct keywords (lower-case first letter) with counts
  python -I -X utf8 -B probe_G3_ru.py seg PART id [id ...]   Pāli + Russian of segments
  python -I -X utf8 -B probe_G3_ru.py where PART kw          ids whose keyword list has kw (exact)
  python -I -X utf8 -B probe_G3_ru.py unmapped [PART ...]    keywords the G3 resolver cannot map yet
  python -I -X utf8 -B probe_G3_ru.py vals PART kw           distinct values of kw in PART with ids
"""
import collections
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_pi6_ru import lc, read_keywords, read_pali, read_russian  # noqa: E402

G3 = [f"3-0{i}-ayatanayamaka" for i in range(1, 7)]

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "kw":
        parts = sys.argv[2:] or G3
        c = collections.Counter()
        where = collections.defaultdict(set)
        for p in parts:
            for bid, kws in read_keywords(p):
                for k in kws:
                    c[lc(k)] += 1
                    where[lc(k)].add(p[:4])
        for k, n in sorted(c.items()):
            print(f"{k}\t{n}\t{','.join(sorted(where[k]))}")
    elif cmd == "seg":
        p = sys.argv[2]
        pa, ru = read_pali(p), read_russian(p)
        kw = dict(read_keywords(p))
        for bid in sys.argv[3:]:
            print("=====", bid, "KW:", ", ".join(kw.get(bid, [])))
            print(pa.get(bid))
            print("--")
            print(ru.get(bid))
    elif cmd == "where":
        p, k = sys.argv[2], sys.argv[3]
        print([bid for bid, kws in read_keywords(p) if k in kws])
    elif cmd == "unmapped":
        import map_G3_ru as g3
        parts = sys.argv[2:] or G3
        miss = collections.Counter()
        for p in parts:
            r = g3.resolver_for(p)
            for bid, kws in read_keywords(p):
                for k in kws:
                    try:
                        r(bid, k, kws)
                    except KeyError:
                        miss[k] += 1
        for k, n in sorted(miss.items()):
            print(f"{k}\t{n}")
    elif cmd == "dump":
        import map_G3_ru as g3
        parts = sys.argv[2:] or G3
        d = collections.defaultdict(collections.Counter)
        for p in parts:
            r = g3.resolver_for(p)
            for bid, kws in read_keywords(p):
                for k in kws:
                    d[k][r(bid, k, kws)] += 1
        for k in sorted(d, key=lc):
            print(k, "=>", dict(d[k]))
    elif cmd == "vals":
        import map_G3_ru as g3
        p, k = sys.argv[2], sys.argv[3]
        r = g3.resolver_for(p)
        d = collections.defaultdict(list)
        for bid, kws in read_keywords(p):
            if k in kws:
                d[r(bid, k, kws)].append(bid)
        for v, ids in d.items():
            print(v, ids)
