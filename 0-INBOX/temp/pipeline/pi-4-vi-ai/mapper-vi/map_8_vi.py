"""Build the Pāli->Vietnamese keyword map for pi-4 part 8-sattakapuggalapannatti (chapter 8).

usage: python -I -X utf8 map_8_vi.py                     (writes 8-sattakapuggalapannatti.mapped.md and verifies it)
       python -I -X utf8 map_8_vi.py show lo hi          (segments lo..hi: Pāli, Vietnamese, pairs; writes nothing)
       python -I -X utf8 map_8_vi.py dump [miss]         (every distinct keyword=value; writes nothing)
       python -I -X utf8 map_8_vi.py look kw ...         (pi-1 / pi-2 / pi-3 map values; writes nothing)

Importing this module builds nothing (check_parts_vi.py imports it only for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> T8 (this script's table) -> map_common_vi.value():
context4 -> PG -> the pi-3 chain.
The seven water similes (^4-M-13) are one segment, ^4-203; ^4-204 … ^4-206 repeat the ekaka definitions ^4-24 … ^4-30.
"""
import pathlib
import sys
from collections import Counter

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import (GAP, NDE, build_part, en_ru, lc, pi1_map_values, pi2_map_values,  # noqa: E402
                           pi3_map_values, present, read_keywords, read_pali, read_vietnamese, value, verify)

PART = "8-sattakapuggalapannatti"

# part-specific values (^4-203, read from the segment)
T8 = {
    # ---- the water similes «Người như thế nào là người chìm một lần thì chìm hẳn / trồi lên rồi …?»
    "ummujjati": "trồi lên",                                  # «có người trồi lên với ý nghĩ …» (4-M-13 ummujjitvā)
    "puggalo nimuggo": "người chìm",                          # «là người chìm một lần thì chìm hẳn»
    "patigādha": "chỗ chân chạm đáy",                         # Pāli spelling of PG paṭigādha (4-M-13)
    "ekanta": "hoàn toàn", "kāḷakehi": "đen tối",             # ekantakāḷakehi «hoàn toàn đen tối»
    # ---- «sāhu / sādhu saddhā kusalesu dhammesu» «Tốt thay niềm tin trong các hiện tượng thiện»
    "sāhu dhammesu": "tốt thay" + GAP + "hiện tượng",
    "saddhā kusalesu": "niềm tin trong" + GAP + "thiện",     # locative «trong» kept, «các hiện tượng» (dhammesu) skipped
    "hirī kusalesu": "sự biết hổ thẹn trong" + GAP + "thiện",   # (as puggalānaṃ āsavā «ô nhiễm của … hạng người»)
    "ottappaṃ kusalesu": "sự biết ghê sợ tội lỗi trong" + GAP + "thiện",
    "vīriyaṃ kusalesu": "sự tinh tấn trong" + GAP + "thiện",  # the text writes «sự tinh tấn» here
    "paññā kusalesu": "trí tuệ trong" + GAP + "thiện",
    "hirī": "sự biết hổ thẹn", "ottappaṃ": "sự biết ghê sợ tội lỗi",   # pi-1 factor names
    # ---- «neva tiṭṭhati no vaḍḍhati hāyatiyeva» «không đứng yên, không tăng trưởng, mà chỉ suy giảm»
    "hāyati": "suy giảm", "vaḍḍhati": "tăng trưởng",
    "tiṭṭhati no vaḍḍhati": "đứng yên không tăng trưởng",    # comma dropped; «không» of neva not in the keyword
    "hāyati no vaḍḍhati": "suy giảm không tăng trưởng",
    # ---- the four fruits (as ^4-31 … ^4-35, map_4 arahatta formula, map_7 dukkhassanta)
    "dukkhassanta": "tận cùng của khổ đau",                   # dukkhassantakaro «người đi đến tận cùng của khổ đau»
    "abhiññā": "hiểu biết trực tiếp", "anāsavaṃ": "không còn ô nhiễm",
    "cetovimuttiṃ paññāvimuttiṃ": "sự giải thoát của tâm sự giải thoát nhờ trí tuệ",   # comma dropped (map_4)
    "tassa": "người ấy",                                     # Tassa sā saddhā «Niềm tin ấy của người ấy» (map_4 assa)
    "evaṃ": "như vậy",                                        # Evaṃ puggalo … «Như vậy là người …» (main text)
    # the variant bracket [sāhu (sī. syā.) evaṃ tīsu ṭhānesupi] «[khác chính tả (Sī., Syā.): sāhu, cũng vậy ở cả ba chỗ]»
    "ṭhānesu": "chỗ",                                         # the bracket's translated label (ALLOWED)
}

# per-segment choices (read from the segments)
OVERRIDES = {
    "4-203": {"samannāgato": "mang",                          # samannāgato hoti ekantakāḷakehi … «mang các hiện tượng
              "puggalo samannāgato": "người mang",             # bất thiện hoàn toàn đen tối»
              "patto": "đến được",                            # patigādhappatto «đến được chỗ chân chạm đáy»
              "ṭhito": "đứng yên"},                           # ummujjitvā ṭhito hoti «trồi lên rồi đứng yên» (4-M-13)
}

# presence-check exceptions: (id, keyword) -> reason
_BR = "the word is in the translated label of a variant bracket, which present() strips (pi-3 ^3-112 precedent)"
ALLOWED = {("4-203", "ṭhānesu"): _BR}


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value(kw, kws, T8, vi.get(bid, ""))
    return resolve


def show(lo, hi):
    res = resolver()
    vi, pi = read_vietnamese(PART), read_pali(PART)
    for i, (bid, kws) in enumerate(read_keywords(PART)):
        if lo <= i < hi:
            print(f"== {i} [{bid}]")
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
