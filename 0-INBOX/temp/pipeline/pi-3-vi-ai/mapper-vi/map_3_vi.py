"""Build the Pāli->Vietnamese keyword map for pi-3 (Dhātukathā) part 3-dutiyanayo.

usage: python -I -X utf8 map_3_vi.py                     (writes 3-dutiyanayo.mapped.md and verifies it)
       python -I -X utf8 map_3_vi.py dump [miss]         (every distinct keyword=value; writes nothing)
       python -I -X utf8 map_3_vi.py show lo hi          (segments lo..hi with every pair; writes nothing)

Importing this module writes nothing (check_parts_vi.py imports it only for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> T3 (this script's table) -> map_common_vi.value()
(context3 -> KD -> alternatives / counts / «X saṅgahito» / «X dhammā» -> pi-2 chain -> pi-1 chain).
Conventions: pi-1 vi-map-conventions.md, pi-2 vi-map-conventions-pi2.md, pi-3 vi-map-conventions-pi3.md
(approved sample: map_sample_vi.py).
"""
import pathlib
import sys
from collections import Counter

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import (GAP, NDE, build_part, lc, pi1_map_values, pi2_map_values,  # noqa: E402
                           present, read_keywords, read_pali, read_vietnamese, value, verify)

PART = "3-dutiyanayo"

_DH = "theo cách gộp vào khối"

# part table (method 2: «Đối với X, những hiện tượng nào … được gộp vào theo cách gộp vào khối, không được gộp
# vào theo cách gộp vào lĩnh vực nhận biết …, thì những hiện tượng đó không được gộp vào …»)
T3 = {
    # the heading «Giải thích đề mục về điều không được gộp vào dựa trên điều được gộp vào»: noun (method term)
    "asaṅgahita": "điều không được gộp vào",
    # the reference «Đối với X» (X-ena / X-āya = X itself; «đối với» is the case frame)
    "cakkhudhātuyā": "yếu tố mắt", "phoṭṭhabbadhātuyā": "yếu tố vật xúc chạm",
    "phoṭṭhabbāyatanena": "lĩnh vực vật xúc chạm", "cakkhāyatanena": "lĩnh vực mắt",
    "cakkhuviññāṇadhātuyā": "yếu tố thức qua mắt", "sotaviññāṇadhātuyā": "yếu tố thức qua tai",
    "ghānaviññāṇadhātuyā": "yếu tố thức qua mũi", "jivhāviññāṇadhātuyā": "yếu tố thức qua lưỡi",
    "kāyaviññāṇadhātuyā": "yếu tố thức qua thân", "manodhātuyā": "yếu tố ý",
    "manoviññāṇadhātuyā": "yếu tố ý thức",
    "cakkhundriyena": "năng lực mắt", "indriyena": "năng lực",
    "bhavena": "sự hiện hữu", "paridevena": "sự than khóc", "paridevo": "sự than khóc",
    "sanidassanehi": "thấy được", "sanidassanehi dhammehi": "hiện tượng thấy được",
    "upādādhammehi": "hiện tượng phái sinh",
    # artefact pair «… dhammehi ye dhammā khandhasaṅgahena …» «các hiện tượng … theo cách gộp vào khối»
    "dhammehi khandhasaṅgahena": "hiện tượng" + GAP + _DH,
    # summary verse ^3-178: «Mười lĩnh vực nhận biết …», «Bảy năng lực», «Điều không thấy được»
    "dasāyatanā": "mười lĩnh vực nhận biết", "indriyā": "năng lực",
    "anidassanaṃ": "điều không thấy được",
}

# per-segment choices
OVERRIDES = {
    # Asaññābhavena «sự hiện hữu không có tri giác»: fragment saññā = the positive part (as ^3-70 asaññābhavo)
    "3-174": {"saññā": "có tri giác"},
}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value(kw, kws, T3, vi.get(bid, ""))
    return resolve


def dump(only_miss=False):
    res = resolver()
    vi = read_vietnamese(PART)
    c, miss, where = Counter(), Counter(), {}
    for bid, kws in read_keywords(PART):
        for kw in kws:
            try:
                v = res(bid, kw, kws)
            except KeyError:
                v = "???"
            c[(kw, v)] += 1
            where.setdefault((kw, v), []).append(bid)
            if v == "???" or (v != NDE and not present(v, vi.get(bid, ""))):
                miss[(kw, v)] += 1
    for (kw, v), n in sorted(c.items()):
        m = miss.get((kw, v), 0)
        if only_miss and not m:
            continue
        p1 = [x for x, _ in pi1_map_values(kw).most_common(2) if x != v]
        p2 = [x for x, _ in pi2_map_values(kw).most_common(2) if x != v]
        print(f"{kw}={v}  [{n}] {where[(kw, v)][:4]}" + (f"  pi1:{p1}" if p1 else "") + (f"  pi2:{p2}" if p2 else "")
              + (f"  MISS {m}" if m else ""))
    print("distinct", len(c), "miss-pairs", len(miss), "miss-total", sum(miss.values()))


def show(lo, hi):
    res = resolver()
    vi, pi = read_vietnamese(PART), read_pali(PART)
    for i, (bid, kws) in enumerate(read_keywords(PART)):
        if lo <= i < hi:
            print(f"== {i} [{bid}]\n-- PI {pi.get(bid, '')}\n-- VI {vi.get(bid, '')}")
            print("   " + " | ".join(f"{kw}={res(bid, kw, kws)}" for kw in kws))


if __name__ == "__main__":
    if sys.argv[1:2] == ["dump"]:
        dump(sys.argv[2:3] == ["miss"])
    elif sys.argv[1:2] == ["show"]:
        show(int(sys.argv[2]), int(sys.argv[3]))
    else:
        build_part(PART, resolver())
        verify(PART, ALLOWED)
