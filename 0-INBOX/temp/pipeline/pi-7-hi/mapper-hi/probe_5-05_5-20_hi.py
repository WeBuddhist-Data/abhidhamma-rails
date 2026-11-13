"""Probe for 5-05..5-20: unmapped keywords, presence misses (tolerant and strict), fallback sources.
Writes nothing. usage: python -I -B -X utf8 probe_5-05_5-20_hi.py [unm|fb|miss|strict|neg|all] [file-substring …]
"""
import sys, pathlib, collections, re, importlib.util
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from map_sample_hi import read_keywords, read_hindi, present, NDE, lc, DEV
from map_common_hi import _norm, _token

_spec = importlib.util.spec_from_file_location("m520", HERE / "map_5-05_5-20_hi.py")
_m = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_m)


def strict(value, text):
    """pi-1 presence without the «a dropped negative may intervene» tolerance."""
    if value == NDE:
        return True
    t = _norm(text or "")
    for part in re.split(r" … | / ", value):
        toks = _norm(part).split()
        if not toks:
            continue
        pat = re.compile(f"(?<![{DEV}])" + r"\s+".join(_token(x) for x in toks) + f"(?![{DEV}])")
        if not pat.search(t):
            return False
    return True


mode = sys.argv[1] if len(sys.argv) > 1 else "all"
sel = sys.argv[2:]
unm = collections.defaultdict(list); miss = collections.defaultdict(list); smiss = collections.defaultdict(list)
log_all = collections.defaultdict(collections.Counter)
for f in _m.FILES:
    if sel and not any(s in f for s in sel):
        continue
    hi = read_hindi(f)
    log = {}
    res = _m.make_resolver520(f, None, _m.OVR[f], log)
    for bid, kws in read_keywords(f):
        for kw in kws:
            try:
                v = res(bid, kw, kws)
            except KeyError:
                unm[kw].append((f, bid)); continue
            if v != NDE and not present(v, hi.get(bid)) and (bid, kw) not in _m.ALLOWED[f]:
                miss[(kw, v)].append((f, bid))
            elif v != NDE and not strict(v, hi.get(bid)):
                smiss[(kw, v)].append((f, bid))
    for (kw, v), c in log.items():
        for s, n in c.items():
            log_all[(kw, v)][s] += n
if mode in ("unm", "all"):
    print("UNMAPPED:", len(unm))
    for k, l in sorted(unm.items(), key=lambda x: -len(x[1])):
        print("  ", k, len(l), l[0])
if mode in ("fb", "all"):
    print("FALLBACKS:")
    for (kw, v), c in sorted(log_all.items(), key=lambda x: lc(x[0][0])):
        if set(c) - {"table", "heading", "override", "neg"}:
            print("  ", kw, "->", v, dict(c))
if mode in ("neg",):
    for (kw, v), c in sorted(log_all.items(), key=lambda x: lc(x[0][0])):
        if "neg" in c:
            print("  ", kw, "->", v, dict(c))
if mode in ("miss", "all"):
    print("PRESENCE MISSES:", sum(len(l) for l in miss.values()))
    for k, l in miss.items():
        print("  ", k[0], "=", k[1], len(l), l[:3])
if mode in ("strict", "all"):
    print("STRICT-ONLY MISSES:", sum(len(l) for l in smiss.values()))
    for k, l in smiss.items():
        print("  ", k[0], "=", k[1], len(l), l[:3])
