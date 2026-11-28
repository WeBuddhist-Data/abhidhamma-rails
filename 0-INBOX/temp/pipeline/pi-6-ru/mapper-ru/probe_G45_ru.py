"""G45 helper (writes nothing).
usage:
  python -I -X utf8 -B probe_G45_ru.py kw [PART ...]          distinct keywords (lower-case first letter) with counts
  python -I -X utf8 -B probe_G45_ru.py seg PART id [id ...]   Pāli + Russian of segments
  python -I -X utf8 -B probe_G45_ru.py where PART kw          ids whose keyword list has kw (exact)
"""
import collections
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_pi6_ru import lc, read_keywords, read_pali, read_russian  # noqa: E402

G45 = ["4-dhatuyamaka", "5-01-saccayamaka", "5-02-saccayamaka", "5-03-saccayamaka"]

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "kw":
        parts = sys.argv[2:] or G45
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
