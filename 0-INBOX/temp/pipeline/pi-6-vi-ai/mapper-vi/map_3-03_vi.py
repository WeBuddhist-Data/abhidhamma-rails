"""Pāli->Vietnamese keyword map, pi-6 (Yamaka) chapter 3-03-ayatanayamaka (Āyatanayamaka, pavatti: future /
present, future / past; last heading of the uppādavāra and first heading of the nirodhavāra).

usage: python -I -X utf8 -B map_3-03_vi.py                (writes 3-03-ayatanayamaka.mapped.md and verifies it)
       python -I -X utf8 -B map_3-03_vi.py dump [miss]     (every distinct keyword=value; writes nothing)
       python -I -X utf8 -B map_3-03_vi.py show lo hi [pi] (segments lo..hi with their pairs; writes nothing)
       python -I -X utf8 -B map_3-03_vi.py diff            (where 3-02 value302, the 2-01 frames and 3-01 value3 differ)

Importing this module builds nothing. Frame-setters: map_3-02_vi (value302: T3_02 accusative / ablative planes,
beings_value position rule), map_3-01_vi (A3: the Āyatana members, ATTR, PLANE_LOC, BEINGS_GEN, value3) and
map_2-01_vi (K: frames201 = verbs and tenses through verb_value, planes, beings, persons).
Resolver: OVERRIDES -> T3_03 (this chapter) -> map_3-02_vi.value302.
Conventions: pi-1 … pi-5 vi-map-conventions*.md + notes, pi-5 map-coordinator-rules.md, vi-map-conventions-pi6.md,
pi-6 map-coordinator-rules.md, notes-map-3-01.md, notes-map-3-02.md, notes-map-3-03.md.
"""
import importlib
import pathlib
import sys
from collections import Counter

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
from map_common_vi import (NDE, build_part, en, lc, present, read_keywords, read_pali,  # noqa: E402
                           read_vietnamese, verify)

A3 = importlib.import_module("map_3-01_vi")
A32 = importlib.import_module("map_3-02_vi")
K = importlib.import_module("map_2-01_vi")

PART = "3-03-ayatanayamaka"

# ---------------------------------------------------------------------------- this chapter's own values
T3_03 = {}

# per-segment choices (read from the segments)
OVERRIDES = {}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def value303(kw, kws, vi, pi):
    k = lc(kw).lower()
    if k in T3_03:
        return T3_03[k]
    # «Itaresaṃ pañcavokārānaṃ» «những chúng sinh khác trong cõi gồm năm khối»: the head «chúng sinh» goes to
    # Itaresaṃ, the plane-being takes «cõi X» (2-01 rule, K._after_itaresam; 3-02's beings_value has no Itaresaṃ case)
    if k in A3.BEINGS_GEN and len(A3.BEINGS_GEN[k]) == 2 and K._after_itaresam(kw, pi):
        return A3.BEINGS_GEN[k][1]
    return A32.value302(kw, kws, vi, pi)


def resolver_for(part=PART):
    vi, pi = read_vietnamese(part), read_pali(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value303(kw, kws, vi.get(bid, ""), pi.get(bid, ""))
    return resolve


def dump(part=PART, only_miss=False):
    res = resolver_for(part)
    vi = read_vietnamese(part)
    c, miss, where = Counter(), Counter(), {}
    for bid, kws in read_keywords(part):
        for kw in kws:
            v = res(bid, kw, kws)
            c[(kw, v)] += 1
            where.setdefault((kw, v), []).append(bid)
            if v != NDE and not present(v, vi.get(bid, "")):
                miss[(kw, v)] += 1
    for (kw, v), n in sorted(c.items()):
        m = miss.get((kw, v), 0)
        if only_miss and not m:
            continue
        e = en(where[(kw, v)][0]).get(kw)
        print(f"{kw}={v}  [{n}] {where[(kw, v)][:4]}" + (f"  en:{e}" if e else "") + (f"  MISS {m}" if m else ""))
    print("distinct", len(c), "miss-pairs", len(miss), "miss-total", sum(miss.values()))


def show(lo, hi, with_pali=False, part=PART):
    res = resolver_for(part)
    vi, pi = read_vietnamese(part), read_pali(part)
    for i, (bid, kws) in enumerate(read_keywords(part)):
        if lo <= i < hi:
            print(f"== {i} [{bid}]")
            if with_pali:
                print(f"-- PI {pi.get(bid, '')}")
            print(f"-- VI {vi.get(bid, '')}")
            out = []
            for kw in kws:
                v = res(bid, kw, kws)
                flag = "" if v == NDE or present(v, vi.get(bid, "")) else " <<MISS"
                out.append(f"{kw}={v}{flag}")
            print("   " + " | ".join(out))


def diff(part=PART):
    """Keywords where this resolver, the 2-01 frames and 3-01 value3 do not all agree (review aid)."""
    res = resolver_for(part)
    vi, pi = read_vietnamese(part), read_pali(part)
    c = Counter()
    for bid, kws in read_keywords(part):
        for kw in kws:
            mine = res(bid, kw, kws)
            f = K.frames201(kw, kws, vi.get(bid, ""), pi.get(bid, ""), members={})
            try:
                a = A3.value3(kw, kws, None, vi.get(bid, ""))
            except KeyError:
                a = None
            if (f is not None and f != mine) or a != mine:
                c[(bid, kw, mine, f, a)] += 1
    for (bid, kw, mine, f, a), n in sorted(c.items()):
        print(f"[{bid}] {kw}: mine={mine} | 2-01={f} | 3-01={a}")
    print("differences", len(c))


if __name__ == "__main__":
    if sys.argv[1:2] == ["dump"]:
        dump(PART, sys.argv[2:3] == ["miss"])
    elif sys.argv[1:2] == ["show"]:
        show(int(sys.argv[2]), int(sys.argv[3]), "pi" in sys.argv[4:])
    elif sys.argv[1:2] == ["diff"]:
        diff(PART)
    else:
        build_part(PART, resolver_for(PART))
        verify(PART, ALLOWED)
