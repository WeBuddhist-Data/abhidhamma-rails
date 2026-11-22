"""Pāli->Vietnamese keyword map of pi-6 7-10-anusayayamaka (Pahīnavāra paṭiloma «chưa được dứt bỏ» / «Không nên nói là
“đã được dứt bỏ” hay “chưa được dứt bỏ”», Uppajjanavāra «sinh khởi» / «không sinh khởi», Dhātupucchāvāra «Ở người chết
ở cõi … rồi tái sinh vào cõi …, bao nhiêu khuynh hướng tiềm ẩn nằm sẵn … phải phân chia?»).

usage: python -I -X utf8 -B map_7-10_vi.py                  (writes 7-10-anusayayamaka.mapped.md and verifies it)
       python -I -X utf8 -B map_7-10_vi.py dump [miss]      (every distinct keyword=value; writes nothing)
       python -I -X utf8 -B map_7-10_vi.py show lo hi [pi]  (segments lo..hi with their pairs; writes nothing)

Importing this module builds nothing. Frame-setters: map_7-08_vi.py (chains 7-06 … 7-01 and 2-02: value701, TENDENCY,
VERBS appahīno / appahīnā «chưa được dứt bỏ» (first rendering: every Pahīnavāra segment opens with the question),
PERSONS, PLANES, FEELINGS, HEADINGS (round labels, kati), vare_value, 7-05 tendency_ca, T706 / T708), map_2-01_vi.py
(verb_value: uppajjati / nuppajjati and their -ti forms from the polarity of the verb's first occurrence in the Pāli),
map_7-09_vi.py (pahina_value: pahīno / appahīno and their -ti / -ā forms, polarity from the first Pāli occurrence of
the keyword's own stem; coordinator rule), loaded with importlib. Resolution: OVERRIDES[bid][kw] -> value710() = 2-01
verb_value(kw, pali) -> 7-05 tendency_ca -> 7-09 pahina_value(kw, pali) -> A.value701(kw, kws, T710, text) = T710
(T708 + own) -> 7-01 T701 -> tendency_value -> vare_value -> verb_value -> map_sample_vi.value6.
pahīno / pahīnā here occur only inside «na vattabbo "pahīno"ti vā "appahīno"ti vā» = «“đã được dứt bỏ”»; appahīno /
appahīnā first in the question = «chưa được dứt bỏ» (the 7-01 VERBS probe is not used for them).
Conventions: vi-map-conventions-pi6.md, map-coordinator-rules.md, notes-map-7-01.md … notes-map-7-08.md.
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
from map_common_vi import (NDE, build_part, en, present, read_keywords, read_pali,  # noqa: E402
                           read_vietnamese, verify)


def _load(name, fname):
    spec = importlib.util.spec_from_file_location(name, HERE / fname)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


H = _load("map_7_08_vi", "map_7-08_vi.py")          # chains 7-06 … 7-01, 2-02
A, E = H.A, H.E                                      # 7-01 (value701), 7-05 (tendency_ca)
M = importlib.import_module("map_2-01_vi")          # verb_value (uppajjati / nirujjhati and tenses)
N = _load("map_7_09_vi", "map_7-09_vi.py")          # pahina_value (pahīno / appahīno, coordinator rule)

PART = "7-10-anusayayamaka"

_NOT = "nơi không phải là "                          # «tái sinh vào nơi không phải là cõi dục lạc» (fused Na-)
_ALSO_NOT = " cũng không phải là "
_KAMA, _RUPA, _ARUPA = "cõi dục lạc", "cõi hình sắc", "cõi không hình sắc"
_BASED = "phần dựa trên "                            # round labels «(Phần dựa trên …)» (7-01 HEADINGS, 3-01)

# Own table (lower-case keys) on top of 7-08 T708 (= 7-06 T706 + the placeholder).
T710 = {
    **H.T708,
    "pahīnavāre": "mục về những gì đã được dứt bỏ",  # closer «Chiều ngược trong mục về những gì đã được dứt bỏ.»
    "pahīnavāro": "mục về những gì đã được dứt bỏ",  # «Mục về những gì đã được dứt bỏ.» (FORMULAS)
    "uppajjanavāro": "mục về sự sinh khởi",          # heading / closer «Mục về sự sinh khởi» (FORMULAS uppādavāro)
    "dhātupucchāvāro": "mục hỏi theo các yếu tố",    # «(a) Mục hỏi theo các yếu tố» (inner «các» kept; cf.
                                                     # dhātuvisajjanāvāro «mục trả lời theo các yếu tố»)
    "bhaṅgā": "phải phân chia",                      # «bao nhiêu khuynh hướng tiềm ẩn phải phân chia?»
    "upapajjantassa": "tái sinh",                    # «Ở người chết ở cõi … rồi tái sinh vào cõi …» («vào» = case frame;
                                                     # «người» belongs to cutassa, not a keyword)
    "anusayā": "khuynh hướng tiềm ẩn",               # «bao nhiêu khuynh hướng tiềm ẩn» (kati = bao nhiêu, not a keyword)
    "kāmadhātumūlakaṃ": _BASED + _KAMA,
    "rūpadhātumūlakaṃ": _BASED + _RUPA,
    "arūpadhātumūlakaṃ": _BASED + _ARUPA,
    "nakāmadhātumūlakaṃ": _BASED + _NOT + _KAMA,
    "narūpadhātumūlakaṃ": _BASED + _NOT + _RUPA,
    "naarūpadhātumūlakaṃ": _BASED + _NOT + _ARUPA,
    "nakāmanaarūpadhātumūlakaṃ": _BASED + _NOT + _KAMA + _ALSO_NOT + _ARUPA,
    "narūpanaarūpadhātumūlakaṃ": _BASED + _NOT + _RUPA + _ALSO_NOT + _ARUPA,
    "nakāmanarūpadhātumūlakaṃ": _BASED + _NOT + _KAMA + _ALSO_NOT + _RUPA,
}

# per-segment choices
OVERRIDES = {}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def value710(kw, kws, text, pali):
    v = M.verb_value(kw, pali)
    if v is not None:
        return v
    v = E.tendency_ca(kw)
    if v is not None:
        return v
    v = N.pahina_value(kw, pali)
    if v is not None:
        return v
    return A.value701(kw, kws, T710, text)


def resolver():
    vi, pi = read_vietnamese(PART), read_pali(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value710(kw, kws, vi.get(bid, ""), pi.get(bid, ""))
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
