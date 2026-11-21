"""Build the Pāli->Vietnamese keyword map for pi-4 part 11-dasakapuggalapannatti (chapter 11, the last; it ends with
the book colophon).

usage: python -I -X utf8 map_11_vi.py                     (writes 11-dasakapuggalapannatti.mapped.md and verifies it)
       python -I -X utf8 map_11_vi.py show lo hi          (segments lo..hi: Pāli, Vietnamese, pairs; writes nothing)
       python -I -X utf8 map_11_vi.py dump [miss]         (every distinct keyword=value; writes nothing)
       python -I -X utf8 map_11_vi.py look kw ...         (pi-1 / pi-2 / pi-3 map values; writes nothing)

Importing this module builds nothing (check_parts_vi.py imports it only for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> T11 (this script's table) -> map_common_vi.value():
context4 -> PG -> the pi-3 chain.
^4-209 = the ten persons of the matrix ^4-M-16 (the five «đạt đến đích ngay ở đây» / «sau khi rời khỏi nơi đây», names
as the ekaka definitions ^4-37 … ^4-42 write them, here in the genitive), the closer of the designation question
(^4-M-6 «Sự định danh về các hạng người bao quát đến mức ấy.»), the chapter closer and the book colophon.
"""
import pathlib
import sys
from collections import Counter

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import (GAP, NDE, build_part, en_ru, lc, pi1_map_values, pi2_map_values,  # noqa: E402
                           pi3_map_values, present, read_keywords, read_pali, read_vietnamese, value, verify)

PART = "11-dasakapuggalapannatti"

# part-specific values (^4-209, read from the segment)
T11 = {
    # ---- genitive forms of the names / members (as the nominatives in PG / NAMES, ^4-37 … ^4-42)
    "sakadāgāmissa": "bậc trở lại một lần",                  # name with its head noun (NAMES sakadāgāmī)
    "parinibbāyissa": "nhập Niết-bàn trọn vẹn",               # member of antarā- / upahacca- / (a)saṅkhāraparinibbāyissa
    "bījissa": "hạt giống",                                   # member of ekabījissa «người chỉ còn một hạt giống»
    "uddhaṃsotassa": "ngược dòng",                            # member (PG uddhaṃsoto)
    "gāmino": "đi đến",                                       # akaniṭṭhagāmino «đi đến cõi Sắc Cứu Cánh» (PG gāmī)
    # ---- diṭṭheva dhamme «ngay trong đời này» (map_4 ^4-131, notes-map-7)
    "dhamme": "đời",
    # ---- book colophon «Bộ “Định danh các hạng người” đã hoàn tất.»
    "pakaraṇaṃ": "Bộ",
    "niṭṭhitaṃ": "đã hoàn tất",
}

# per-segment choices (read from the segments)
OVERRIDES = {}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value(kw, kws, T11, vi.get(bid, ""))
    return resolve


def show(lo, hi):
    res = resolver()
    vi, pi = read_vietnamese(PART), read_pali(PART)
    for i, (bid, kws) in enumerate(read_keywords(PART)):
        if lo <= i < hi:
            print(f"== {i} [{bid}]\n-- PI {pi.get(bid, '')}\n-- VI {vi.get(bid, '')}")
            er = en_ru(bid)
            for kw in kws:
                try:
                    v = res(bid, kw, kws)
                except KeyError:
                    v = "???"
                flag = "" if v == NDE or present(v, vi.get(bid, "")) else "   <<MISS"
                e = er.get(kw, ["", ""])
                print(f"   {kw}={v}   [{e[0]} | {e[1]}]{flag}")


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
        ps = []
        for i, f in ((1, pi1_map_values), (2, pi2_map_values), (3, pi3_map_values)):
            p = [x for x, _ in f(kw).most_common(2) if x != v]
            if p:
                ps.append(f"pi{i}:{p}")
        print(f"{kw}={v}  [{n}] {where[(kw, v)][:4]}" + ("  " + " ".join(ps) if ps else "")
              + (f"  MISS {m}" if m else ""))
    print("distinct", len(c), "miss-pairs", len(miss), "miss-total", sum(miss.values()))


def look(kws):
    for kw in kws:
        for k in dict.fromkeys((kw, lc(kw), kw[:1].upper() + kw[1:])):
            out = [f"pi{i}:{dict(f(k).most_common(4))}" for i, f in
                   ((1, pi1_map_values), (2, pi2_map_values), (3, pi3_map_values)) if f(k)]
            if out:
                print(k, " ".join(out))


if __name__ == "__main__":
    if sys.argv[1:2] == ["show"]:
        show(int(sys.argv[2]), int(sys.argv[3]))
    elif sys.argv[1:2] == ["dump"]:
        dump(sys.argv[2:3] == ["miss"])
    elif sys.argv[1:2] == ["look"]:
        look(sys.argv[2:])
    else:
        build_part(PART, resolver())
        verify(PART, ALLOWED)
