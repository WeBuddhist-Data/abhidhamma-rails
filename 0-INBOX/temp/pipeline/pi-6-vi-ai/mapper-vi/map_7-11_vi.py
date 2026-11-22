"""Pāli->Vietnamese keyword map of pi-6 7-11-anusayayamaka (Dhātuvisajjanāvāra «Ở người chết ở cõi … rồi tái sinh vào
cõi …, thì ở một số người, bảy khuynh hướng tiềm ẩn nằm sẵn …; không có khuynh hướng tiềm ẩn nào phải phân chia.», the
«không có cái gọi là sự tái sinh vào …, khi tái sinh xuống thấp hơn, người ấy chỉ tái sinh vào cõi dục lạc» answers,
and the Anusayayamaka closer).

usage: python -I -X utf8 -B map_7-11_vi.py                  (writes 7-11-anusayayamaka.mapped.md and verifies it)
       python -I -X utf8 -B map_7-11_vi.py dump [miss]      (every distinct keyword=value; writes nothing)
       python -I -X utf8 -B map_7-11_vi.py show lo hi [pi]  (segments lo..hi with their pairs; writes nothing)

Importing this module builds nothing. Frame-setters: map_7-08_vi.py (chains 7-06 … 7-01 and 2-02: value701, TENDENCY,
PERSONS, PLANES (kāmadhātuṃ / rūpadhātuṃ / arūpadhātuṃ «cõi …», the 7-01 proposal for 7-10 / 7-11), HEADINGS,
vare_value, 7-05 tendency_ca, T706 / T708), map_2-01_vi.py (verb_value), loaded with importlib. The dhātu frames
(bhaṅgā «phải phân chia», upapajjantassa «tái sinh», anusayā, the nine «(Phần dựa trên …)» round labels) carry the
same values as map_7-10_vi.py T710 (the Dhātupucchāvāra, mapped at the same time); they are copied here, not imported,
so that this chapter does not depend on 7-09 / 7-10 modules that were still being written.
Resolution: OVERRIDES[bid][kw] -> value711() = 2-01 verb_value(kw, pali) -> 7-05 tendency_ca -> 2-02 parinna_value ->
A.value701(kw, kws, T711, text) = T711 (T708 + own) -> 7-01 T701 -> tendency_value -> vare_value -> verb_value ->
map_sample_vi.value6.
Conventions: vi-map-conventions-pi6.md, map-coordinator-rules.md, notes-map-7-01.md … notes-map-7-08.md, pi-5
map-coordinator-rules.md (participles keep «khi»).
"""
import importlib
import importlib.util
import pathlib
import sys
from collections import Counter

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
from map_common_vi import (GAP, NDE, build_part, en, present, read_keywords, read_pali,  # noqa: E402
                           read_vietnamese, verify)


def _load(name, fname):
    spec = importlib.util.spec_from_file_location(name, HERE / fname)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


H = _load("map_7_08_vi", "map_7-08_vi.py")          # chains 7-06 … 7-01, 2-02
A, E, P = H.A, H.E, H.P                              # 7-01 (value701), 7-05 (tendency_ca), 2-02 (parinna_value)
M = importlib.import_module("map_2-01_vi")          # verb_value (uppajjati / nirujjhati and tenses)

PART = "7-11-anusayayamaka"

_NOT = "nơi không phải là "                          # «tái sinh vào nơi không phải là cõi dục lạc» (fused Na-)
_ALSO_NOT = " cũng không phải là "
_KAMA, _RUPA, _ARUPA = "cõi dục lạc", "cõi hình sắc", "cõi không hình sắc"
_BASED = "phần dựa trên "                            # round labels «(Phần dựa trên …)» (7-01 HEADINGS, 7-10)

# Own table (lower-case keys) on top of 7-08 T708 (= 7-06 T706 + the placeholder).
T711 = {
    **H.T708,
    # ---- the dhātu frames, as map_7-10_vi.py T710 (Dhātupucchāvāra)
    "bhaṅgā": "phải phân chia",                      # «không có khuynh hướng tiềm ẩn nào phải phân chia» (Natthi /
                                                     # «không có» and «nào» are frame: natthi is not a keyword here)
    "upapajjantassa": "tái sinh",                    # «Ở người chết ở cõi … rồi tái sinh vào cõi …» («vào» = case
                                                     # frame; «người» belongs to cutassa, not a keyword)
    "anusayā": "khuynh hướng tiềm ẩn",               # «bảy / năm / ba khuynh hướng tiềm ẩn nằm sẵn» (the numerals
                                                     # satta / pañca / tayo / satteva are not keywords)
    "kāmadhātumūlakaṃ": _BASED + _KAMA,
    "rūpadhātumūlakaṃ": _BASED + _RUPA,
    "arūpadhātumūlakaṃ": _BASED + _ARUPA,
    "nakāmadhātumūlakaṃ": _BASED + _NOT + _KAMA,
    "narūpadhātumūlakaṃ": _BASED + _NOT + _RUPA,
    "naarūpadhātumūlakaṃ": _BASED + _NOT + _ARUPA,
    "nakāmanaarūpadhātumūlakaṃ": _BASED + _NOT + _KAMA + _ALSO_NOT + _ARUPA,
    "narūpanaarūpadhātumūlakaṃ": _BASED + _NOT + _RUPA + _ALSO_NOT + _ARUPA,
    "nakāmanarūpadhātumūlakaṃ": _BASED + _NOT + _KAMA + _ALSO_NOT + _RUPA,
    # ---- headings of this chapter
    "dhātuvisajjanāvāro": "mục trả lời theo các yếu tố",   # «(b) Mục trả lời theo các yếu tố» (FORMULAS)
    "dhātuvisajjavāro": "mục trả lời theo các yếu tố",     # closer «Mục trả lời theo các yếu tố.» (Pāli spelling of
                                                           # the closer; same heading)
    # closer «Anusayayamakaṃ niṭṭhitaṃ.» «Phần các cặp câu hỏi về các khuynh hướng tiềm ẩn đã hoàn tất.» (lower case
    # as written, as 6-02 saṅkhārayamakaṃ, 9-03 dhammayamakaṃ, 3-06 āyatanayamakaṃ; «Phần» frame)
    "anusayayamakaṃ": "các cặp câu hỏi về các khuynh hướng tiềm ẩn",
    # ---- the «upapatti nāma natthi» answers (^6-7-343, ^6-7-349)
    # «thì không có cái gọi là sự tái sinh vào cõi hình sắc, khi tái sinh xuống thấp hơn, người ấy chỉ tái sinh vào
    # cõi dục lạc» (heṭṭhā «xuống thấp hơn», natthi, satteva: not keywords)
    "upapatti": "sự tái sinh",                       # the text's nominaliser kept (pi-1 / pi-2 «tái sinh» where bare)
    "upapattināma": "cái gọi là sự tái sinh",        # fused «upapattināma» (^6-7-349): nāma = «cái gọi là»
    "upapajjamāno": "khi tái sinh",                  # participle keeps «khi» (pi-5 coordinator; pi-4 / pi-5
                                                     # upapajjamāne «đang tái sinh» where the text has «đang»)
    "upapajjati": "tái sinh",                        # «người ấy chỉ tái sinh vào cõi dục lạc» (pi-2 / pi-5)
    "kāmadhātuṃyeva": "chỉ" + GAP + "cõi dục lạc",   # yeva = «chỉ» (FORMULAS eva), «tái sinh vào» between
}

# per-segment choices
OVERRIDES = {}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def value711(kw, kws, text, pali):
    v = M.verb_value(kw, pali)
    if v is not None:
        return v
    v = E.tendency_ca(kw)
    if v is not None:
        return v
    v = P.parinna_value(kw, pali)
    if v is not None:
        return v
    return A.value701(kw, kws, T711, text)


def resolver():
    vi, pi = read_vietnamese(PART), read_pali(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value711(kw, kws, vi.get(bid, ""), pi.get(bid, ""))
    return resolve


def dump(only_miss=False):
    res, vi = resolver(), read_vietnamese(PART)
    c, miss, where = Counter(), Counter(), {}
    for bid, kws in read_keywords(PART):
        for kw in kws:
            v = res(bid, kw, kws)
            c[(kw, v)] += 1
            where.setdefault((kw, v), []).append(bid)
            if v != NDE and not present(v, vi.get(bid, "")):
                miss[(kw, v)] += 1
    for (kw, v), n in sorted(c.items()):
        if only_miss and not miss.get((kw, v)):
            continue
        e = en(where[(kw, v)][0]).get(kw)
        print(f"{kw}={v}  [{n}] {where[(kw, v)][:4]}" + (f"  en:{e}" if e else "")
              + (f"  MISS {miss[(kw, v)]}" if miss.get((kw, v)) else ""))
    print("distinct", len(c), "miss-pairs", len(miss), "miss-total", sum(miss.values()))


def show(lo, hi, with_pali=False):
    res, vi, pi = resolver(), read_vietnamese(PART), read_pali(PART)
    for i, (bid, kws) in enumerate(read_keywords(PART)):
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


if __name__ == "__main__":
    if sys.argv[1:2] == ["dump"]:
        dump(sys.argv[2:3] == ["miss"])
    elif sys.argv[1:2] == ["show"]:
        show(int(sys.argv[2]), int(sys.argv[3]), "pi" in sys.argv[4:])
    else:
        build_part(PART, resolver())
        verify(PART, ALLOWED)
