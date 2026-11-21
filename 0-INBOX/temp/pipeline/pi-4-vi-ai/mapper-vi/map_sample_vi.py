"""Build the SAMPLE Pāli->Vietnamese keyword maps for pi-4 (Puggalapaññatti): preamble, 1-matika, 2-ekakapuggalapannatti.

usage: python -I -X utf8 map_sample_vi.py                     (writes the three <part>.mapped.md and verifies them)
       python -I -X utf8 map_sample_vi.py dump PART [miss]    (every distinct keyword=value with count, first segments
                                                              and the pi-1 / pi-2 / pi-3 map values; writes nothing)
       python -I -X utf8 map_sample_vi.py show PART lo hi     (segments lo..hi: Pāli, Vietnamese, every pair with the
                                                              English / Russian value; writes nothing)

Importing this module builds nothing (check_parts_vi.py imports it only for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> CORE (preamble only) -> SAMPLE (this script's table)
-> map_common_vi.value(): context4 (segment rules) -> PG (pi-4 table) -> the pi-3 chain (T15 … -> context3 -> KD ->
pi-2 -> pi-1).
Conventions: pi-1 vi-map-conventions.md + notes-map-*.md, pi-2 vi-map-conventions-pi2.md + notes-map-*.md,
pi-3 vi-map-conventions-pi3.md + notes-map-*.md, vi-map-conventions-pi4.md.
"""
import pathlib
import sys
from collections import Counter

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import (CORE, GAP, NDE, build_part, en_ru, lc, pi1_map_values, pi2_map_values,  # noqa: E402
                           pi3_map_values, present, read_keywords, read_pali, read_vietnamese, value, verify)

PARTS = ["preamble", "1-matika", "2-ekakapuggalapannatti"]

# part-specific values (everything recurring lives in map_common_vi.PG)
SAMPLE = {}

# per-segment choices (read from the segments)
OVERRIDES = {
    # ---- 1-matika
    "4-M-9": {"puthu": "rộng lớn"},                           # puthupañño «người có trí tuệ rộng lớn»
    "4-M-10": {"ññū": "hiểu",                                 # ugghaṭitaññū «người hiểu ngay …» (4-M-8 mattaññū «biết»)
               "gāmī": "đi",                                  # anusota- / paṭisotagāmī «người đi xuôi / ngược dòng»
               "sota": "dòng",                                # «xuôi dòng», «ngược dòng» (elsewhere sota = tai)
               "ṭhita": "đứng vững",                          # ṭhitatto «người đứng vững» (ṭhitakappī «dừng lại»)
               "viharati": "sống"},                           # «ngay trong đời này sống không còn đói khát …»
    "4-M-13": {"ṭhito": "đứng yên"},                          # ummujjitvā ṭhito hoti «trồi lên rồi đứng yên»
    # ---- 2-ekakapuggalapannatti
    "4-9": {"pahīnāni": "được dứt bỏ"},                       # appahīnāni «chưa được dứt bỏ» (fragment, positive part)
    "4-6": {"parihānadhammo": "thể bị sa sút"},               # of aparihānadhammo «người không thể bị sa sút»: «không»
                                                              # = a-, «thể bị» = dhammo (as akuppa / kuppa, ^4-4)
    "4-16": {"hoti": "xảy ra"},                               # «… và sự kết thúc mạng sống xảy ra không trước không sau»
    "4-37": {"upahacca": "khi gần"},                          # upahacca vā kālakiriyaṃ «hoặc khi gần mạng chung»
    "4-44": {"rūpa": "cõi hình sắc", "arūpa": "cõi không hình sắc"},   # rūparāga / arūparāga (pi-1 «sự tham đắm cõi
                                                              # hình sắc»)
}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def resolver_for(part):
    vi = read_vietnamese(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        k = lc(kw)
        if part == "preamble" and k in CORE:      # the pi-1 preamble values (Namo … sammāsambuddhassa)
            return CORE[k]
        return value(kw, kws, SAMPLE, vi.get(bid, ""))
    return resolve


def dump(part, only_miss=False):
    res = resolver_for(part)
    vi = read_vietnamese(part)
    c, miss, where = Counter(), Counter(), {}
    for bid, kws in read_keywords(part):
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
        er = en_ru(where[(kw, v)][0]).get(kw)
        print(f"{kw}={v}  [{n}] {where[(kw, v)][:4]}" + ("  " + " ".join(ps) if ps else "")
              + (f"  en/ru:{er[0]}|{er[1]}" if er else "") + (f"  MISS {m}" if m else ""))
    print("distinct", len(c), "miss-pairs", len(miss), "miss-total", sum(miss.values()))


def show(part, lo, hi):
    res = resolver_for(part)
    vi, pi = read_vietnamese(part), read_pali(part)
    for i, (bid, kws) in enumerate(read_keywords(part)):
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


def look(kws):
    """the pi-1 / pi-2 / pi-3 map values of each keyword (exact keyword and lower-case first letter)."""
    for kw in kws:
        for k in dict.fromkeys((kw, lc(kw), kw[:1].upper() + kw[1:])):
            out = [f"pi{i}:{dict(f(k).most_common(4))}" for i, f in
                   ((1, pi1_map_values), (2, pi2_map_values), (3, pi3_map_values)) if f(k)]
            if out:
                print(k, " ".join(out))


if __name__ == "__main__":
    if sys.argv[1:2] == ["look"]:
        look(sys.argv[2:])
    elif sys.argv[1:2] == ["dump"]:
        dump(sys.argv[2], sys.argv[3:4] == ["miss"])
    elif sys.argv[1:2] == ["show"]:
        show(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
    else:
        for p in PARTS:
            build_part(p, resolver_for(p))
            verify(p, ALLOWED)
