"""Probe for 3-02..3-06: unmapped keywords (with counts and a sample id) and presence misses of the default table.
usage: python -I -B -X utf8 probe_3-02_3-06_hi.py [file ...]
"""
import sys, pathlib, collections; sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import *  # noqa
import importlib.util  # noqa
_sp = importlib.util.spec_from_file_location("m3", pathlib.Path(__file__).resolve().parent / "map_3-02_3-06_hi.py")
M = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(M)

FILES = sys.argv[1:] or ["3-02-culantaraduka", "3-03-asavagocchaka", "3-04-sannojanagocchaka",
                         "3-05-ganthagocchaka", "3-06-oghayogagocchaka"]
for f in FILES:
    hi, pa = read_hindi(f), read_pali(f)
    tab = {**PI7, **M.T}
    ovr = M.OVR.get(f, {})
    unm = collections.defaultdict(list)
    miss = collections.defaultdict(list)
    for bid, kws in read_keywords(f):
        for kw in kws:
            if kw in ovr.get(bid, {}):
                v = ovr[bid][kw]
            else:
                try:
                    v, src = pi7_value(kw, kws, tab, pa.get(bid), hi.get(bid))
                except KeyError:
                    unm[kw].append(bid)
                    continue
            if v != NDE and not present(v, hi.get(bid)):
                miss[(kw, v)].append(bid)
    print("=" * 10, f, "unmapped", len(unm), "miss", len(miss))
    for kw, ids in sorted(unm.items(), key=lambda x: -len(x[1])):
        print("  UNM", kw, len(ids), ids[:4])
    for (kw, v), ids in sorted(miss.items(), key=lambda x: -len(x[1])):
        print("  MISS", kw, "=", v, len(ids), ids[:4])
