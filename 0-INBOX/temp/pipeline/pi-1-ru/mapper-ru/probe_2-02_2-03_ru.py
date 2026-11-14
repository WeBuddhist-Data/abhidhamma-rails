"""Review helper for map_2-02_2-03_ru.py (writes nothing).

usage:
  python -I -X utf8 probe_2-02_2-03_ru.py missing PART       unique keywords not in CH2, with count + first id
  python -I -X utf8 probe_2-02_2-03_ru.py seg PART ID [ID..]  Pāli, Russian and the current mapping of segments
  python -I -X utf8 probe_2-02_2-03_ru.py miss PART            current mapping's presence misses (all)
"""
import collections
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from map_common_ru import CH2, lc, present, read_keywords, read_pali, read_russian  # noqa: E402

cmd, part = sys.argv[1], sys.argv[2]
kw = read_keywords(part)
if cmd == "missing":
    c, first = collections.Counter(), {}
    for bid, kws in kw:
        for k in kws:
            if lc(k) not in CH2 and not lc(k).startswith("samaye "):
                c[k] += 1
                first.setdefault(k, bid)
    for k, n in sorted(c.items(), key=lambda x: first[x[0]]):
        print(n, k, first[k])
    print(len(c), "unique")
else:
    import importlib.util
    spec = importlib.util.spec_from_file_location("m", HERE / "map_2-02_2-03_ru.py")
    M = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(M)
    ru, pi = read_russian(part), read_pali(part)
    res = M.resolver_for(part)
    ids = sys.argv[3:]
    for bid, kws in kw:
        if cmd == "seg" and bid not in ids:
            continue
        out = []
        for k in kws:
            try:
                v = res(bid, k, kws)
            except KeyError:
                v = "???"
            ok = present(v, ru.get(bid, "")) if v != "???" else False
            if cmd == "seg" or not ok:
                out.append(f"{'' if ok else '!! '}{k}={v}")
        if cmd == "seg":
            print("=" * 20, bid)
            print("PI:", pi.get(bid))
            print("RU:", ru.get(bid))
            print("  " + " | ".join(out))
        elif out:
            print(bid, " | ".join(out))
