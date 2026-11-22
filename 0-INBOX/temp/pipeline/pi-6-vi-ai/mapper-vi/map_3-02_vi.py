"""Pāli->Vietnamese keyword map, pi-6 (Yamaka) chapter 3-02-ayatanayamaka (Āyatanayamaka, pavatti: future,
present/past).

usage: python -I -X utf8 -B map_3-02_vi.py                (writes 3-02-ayatanayamaka.mapped.md and verifies it)
       python -I -X utf8 -B map_3-02_vi.py dump [miss]     (every distinct keyword=value; writes nothing)
       python -I -X utf8 -B map_3-02_vi.py show lo hi [pi] (segments lo..hi with their pairs; writes nothing)
       python -I -X utf8 -B map_3-02_vi.py diff            (where the 2-01 frames and 3-01 value3 differ; writes nothing)

Importing this module builds nothing. Frame-setters: map_3-01_vi (A3: the Āyatana members, ATTR, PLANE_LOC,
BEINGS_GEN, value3) and map_2-01_vi (K: frames201 = verbs and tenses from the first Pāli occurrence, planes, beings,
persons). Resolver: OVERRIDES -> T3_02 (this chapter) -> the 3-01 member tables -> the beings in the genitive (positional,
see beings_value) -> frames201 -> value3 (-> map_sample_vi.value6).
Later chapters may reuse:
    T3_02             the accusative / ablative planes of the pavatti answers (rūpāvacaraṃ «(tái sinh) vào cõi hình
                      sắc», Kāmāvacarā «(chết đi) khỏi cõi dục lạc»: «vào», «khỏi» are the case frame, 2-01)
    beings_value(kw, vi, pi)   an -ānaṃ being keyword: «chúng sinh trong cõi X»; «cõi X» where its first Pāli
                      occurrence follows another plane-being -ānaṃ («Rūpāvacarānaṃ arūpāvacarānaṃ» «Ở chúng sinh trong
                      cõi hình sắc, cõi không hình sắc»; asaññasattānaṃ «chúng sinh Vô Tưởng» does not count, the text
                      repeats «chúng sinh» after it)
Conventions: pi-1 … pi-5 vi-map-conventions*.md + notes, pi-5 map-coordinator-rules.md, vi-map-conventions-pi6.md,
pi-6 map-coordinator-rules.md, notes-map-3-01.md, notes-map-3-02.md.
"""
import importlib
import pathlib
import re
import sys
from collections import Counter

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
from map_common_vi import (NDE, build_part, en, lc, pick, present, read_keywords, read_pali,  # noqa: E402
                           read_vietnamese, verify)

A3 = importlib.import_module("map_3-01_vi")
K = importlib.import_module("map_2-01_vi")

PART = "3-02-ayatanayamaka"

# ---------------------------------------------------------------------------- planes in the accusative / ablative
# «Ye rūpāvacaraṃ upapajjitvā parinibbāyissanti» «Những người nào sau khi tái sinh vào cõi hình sắc sẽ nhập Niết-bàn
# trọn vẹn»; «Kāmāvacarā cavantānaṃ» «những người đang chết đi khỏi cõi dục lạc» («vào», «khỏi» = case frame, as
# 2-01 arūpaṃ / Pañcavokārā = cõi …)
T3_02 = {
    "rūpāvacaraṃ": "cõi hình sắc", "arūpāvacaraṃ": "cõi không hình sắc", "kāmāvacaraṃ": "cõi dục lạc",
    "rūpāvacarā": "cõi hình sắc", "arūpāvacarā": "cõi không hình sắc", "kāmāvacarā": "cõi dục lạc",
}

# ---------------------------------------------------------------------------- beings in the genitive (positional)
_BEING_KEYS = {k for k in A3.BEINGS_GEN if k != "asaññasattānaṃ"}


def _first(kw, pali):
    if not pali:
        return None
    m = re.search(r"(?<!\w)" + re.escape(kw) + r"(?!\w)", pali)
    return m or re.search(r"(?<!\w)" + re.escape(kw) + r"(?!\w)", pali, re.I)


def beings_value(kw, vi, pi):
    """«chúng sinh trong cõi X» / «cõi X» (second item of a list of beings, where the text has only «cõi X»)."""
    k = lc(kw).lower()
    if k not in A3.BEINGS_GEN:
        return None
    cands = A3.BEINGS_GEN[k]
    if len(cands) == 1:
        return cands[0]
    long_, short = cands
    m = _first(kw, pi)
    if m:
        words = re.split(r"[.?!\n]", pi[: m.start()])[-1].split()
        if words and lc(words[-1]).lower() in _BEING_KEYS:
            return pick(vi, short, long_) or short
    return pick(vi, long_, short) or long_


# per-segment choices (read from the segments): none needed
OVERRIDES = {}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def value302(kw, kws, vi, pi):
    k = lc(kw).lower()
    if k in T3_02:
        return T3_02[k]
    if k in A3.T3_01:                              # Āyatana members, attributes, locative planes, headings of 3-01
        return A3.T3_01[k]
    v = beings_value(kw, vi, pi)
    if v is not None:
        return v
    v = K.frames201(kw, kws, vi, pi, members={})   # verbs (first Pāli occurrence), planes, persons
    if v is not None:
        return v
    return A3.value3(kw, kws, None, vi)


def resolver_for(part=PART):
    vi, pi = read_vietnamese(part), read_pali(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value302(kw, kws, vi.get(bid, ""), pi.get(bid, ""))
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
