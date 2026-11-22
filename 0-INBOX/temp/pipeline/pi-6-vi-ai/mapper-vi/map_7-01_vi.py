"""Pāli->Vietnamese keyword map of pi-6 7-01-anusayayamaka (frame-setter of the Anusayayamaka, 7-01 … 7-11).

usage: python -I -X utf8 -B map_7-01_vi.py                  (writes 7-01-anusayayamaka.mapped.md and verifies it)
       python -I -X utf8 -B map_7-01_vi.py dump [miss]      (every distinct keyword=value; writes nothing)
       python -I -X utf8 -B map_7-01_vi.py show lo hi [pi]  (segments lo..hi with their pairs; writes nothing)

Importing this module builds nothing. The later Anusaya chapters load it with importlib:
    import importlib.util, pathlib, sys
    sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai\\mapper-vi")
    spec = importlib.util.spec_from_file_location("map_7_01_vi", pathlib.Path(sys.path[0]) / "map_7-01_vi.py")
    A = importlib.util.module_from_spec(spec); spec.loader.exec_module(A)
    value = A.value701(kw, kws, YOUR_TABLE, text)
Named tables (the Anusayayamaka frame; extend them only in your own table):
    TENDENCY / tendency_value()   the seven anusaya «khuynh hướng tiềm ẩn X» in every case form, Sattānusayā, bare anusaya
    VERBS / verb_value()          anuseti … (and the proposals nānuseti, sānusayo, niranusayo, pajahati, parijānāti,
                                  pahīno …): -ti of the question dropped; two renderings in a segment = the first
    PERSONS                       Anāgāmissa, Puthujjanassa, Arahato, puggalānaṃ / puggalassa «hạng người»
    PLANES, FEELINGS              kāma- / rūpa- / arūpadhātuyā «cõi …», dvīsu / tīsu vedanāsu «hai / ba loại cảm giác»,
                                  dukkhāya vedanāya «cảm giác khó chịu», apariyāpanne, sabbattha …
    HEADINGS / vare_value()       Anusayavāre (and every <X>vāre of the paṭiloma closers) = the <X>vāro heading
    T701                          all of the above merged (one dict, lower-case keys)
Resolution: OVERRIDES[bid][kw] -> value701(): your table -> T701 -> tendency_value -> verb_value -> vare_value ->
map_sample_vi.value6 (context6 -> FORMULAS -> YM -> composition -> the pi-5 chain).
Conventions: vi-map-conventions-pi6.md, map-coordinator-rules.md, notes-map-7-01.md.
"""
import importlib.util
import pathlib
import re
import sys
import unicodedata
from collections import Counter

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import map_sample_vi as S  # noqa: E402
from map_common_vi import (NDE, build_part, en, lc, present, read_keywords, read_pali,  # noqa: E402
                           read_vietnamese, verify)
from map_sample_vi import FORMULAS, value6  # noqa: E402

PART = "7-01-anusayayamaka"

# ---------------------------------------------------------------------------- the seven tendencies
ANUSAYA = "khuynh hướng tiềm ẩn"                   # pi-2 anusaya (approved)
TENDENCY = {                                       # member stems (pi-2 ^2-816; notes-7-01.md TENDENCY_VI)
    "kāmarāga": "tham đắm dục lạc",
    "paṭigha": "ác cảm",
    "māna": "kiêu mạn",
    "diṭṭhi": "quan điểm",
    "vicikicchā": "hoài nghi",
    "bhavarāga": "tham đắm hiện hữu",
    "avijjā": "vô minh",
}
TENDENCY_SLIPS = {"kāmārāga": "kāmarāga"}           # kāmārāgānusayo (^6-7-21, ^6-7-25) = kāmarāgānusayo
NUMERAL_STEMS = {"satt": "bảy"}                     # Sattānusayā «Bảy khuynh hướng tiềm ẩn» (numeral in the keyword: kept)
_ANUSAYA_END = ("o", "ā", "aṃ", "ena", "assa", "ānaṃ", "e", "ehi", "a", "āni")


def _sandhi_stems():
    out = {}
    for name, v in TENDENCY.items():
        out[name[:-1]] = v                         # kāmarāga + anusayo = kāmarāgānusayo (final vowel absorbed)
    for slip, name in TENDENCY_SLIPS.items():
        out[slip[:-1]] = TENDENCY[name]
    return out


_STEMS = _sandhi_stems()


def tendency_value(kw):
    """X-ānusayo / -ānusayā / -ānusayaṃ / -ānusayena … = «khuynh hướng tiềm ẩn X» (the case is carried by the verb
    frame); Sattānusayā = «bảy khuynh hướng tiềm ẩn»; anusayo / anusayā / anusayaṃ … = «khuynh hướng tiềm ẩn».
    The tendency member alone (kāmarāga …) = its Vietnamese. None if the keyword is not one."""
    k = lc(kw).lower()
    if k in TENDENCY:
        return TENDENCY[k]
    m = re.fullmatch(r"(.*?)(ā|a)nusay(\w*?)(?:ti)?", k)
    if not m:
        return None
    pre, end = m.group(1), m.group(3)
    if end not in _ANUSAYA_END:
        return None
    if pre == "" and m.group(2) == "a":
        return ANUSAYA
    if pre in _STEMS:
        return ANUSAYA + " " + _STEMS[pre]
    if pre in NUMERAL_STEMS:
        return NUMERAL_STEMS[pre] + " " + ANUSAYA
    return None


# ---------------------------------------------------------------------------- verbs and their polarity
# value -> list of (value, probe) candidates; the value whose probe stands first in the segment wins (coordinator rule:
# one keyword with two renderings in a segment = the first). The probe only locates the rendering («không có khuynh
# hướng» for niranusayo, so that a «Không có.» answer is not taken for it).
_K = "khuynh hướng"
VERBS = {
    # 7-01 (used)
    "anuseti": [("nằm sẵn", "nằm sẵn")], "anusenti": [("nằm sẵn", "nằm sẵn")],
    # proposals (7-02 …): after «no ca» the double negative is said plainly («nhưng ở nơi ấy … vẫn nằm sẵn», 7-02)
    "nānuseti": [("không nằm sẵn", "không nằm sẵn"), ("vẫn nằm sẵn", "vẫn nằm sẵn")],
    "nānusenti": [("không nằm sẵn", "không nằm sẵn"), ("vẫn nằm sẵn", "vẫn nằm sẵn")],
    # 7-03 / 7-04 «Bậc không trở lại không có khuynh hướng tiềm ẩn …, nhưng vẫn có khuynh hướng tiềm ẩn …»:
    # Xena sānusayo = «có X» (sānusayo = có, X = the tendency keyword), niranusayo = không có / after no ca «vẫn có»
    "sānusayo": [("có", "có " + _K)], "sānusayā": [("có", "có " + _K)],
    "niranusayo": [("không có", "không có " + _K), ("vẫn có", "vẫn có " + _K)],
    "niranusayā": [("không có", "không có " + _K), ("vẫn có", "vẫn có " + _K)],
    # 7-05 / 7-06 pajahati, 7-07 / 7-08 parijānāti, 7-09 / 7-10 pahīno (check against your segments)
    "pajahati": [("dứt bỏ", "dứt bỏ")], "pajahanti": [("dứt bỏ", "dứt bỏ")],
    "nappajahati": [("không dứt bỏ", "không dứt bỏ"), ("vẫn dứt bỏ", "vẫn dứt bỏ")],
    "nappajahanti": [("không dứt bỏ", "không dứt bỏ"), ("vẫn dứt bỏ", "vẫn dứt bỏ")],
    "parijānāti": [("hiểu biết trọn vẹn", "hiểu biết trọn vẹn")],
    "parijānanti": [("hiểu biết trọn vẹn", "hiểu biết trọn vẹn")],
    "pahīno": [("đã được dứt bỏ", "đã được dứt bỏ"), ("được dứt bỏ", "được dứt bỏ")],
    "pahīnā": [("đã được dứt bỏ", "đã được dứt bỏ"), ("được dứt bỏ", "được dứt bỏ")],
    "appahīno": [("chưa được dứt bỏ", "chưa được dứt bỏ"), ("đã được dứt bỏ", "đã được dứt bỏ")],
    "appahīnā": [("chưa được dứt bỏ", "chưa được dứt bỏ"), ("đã được dứt bỏ", "đã được dứt bỏ")],
    "uppajjati": [("sinh khởi", "sinh khởi")],
    "nuppajjati": [("không sinh khởi", "không sinh khởi"), ("vẫn sinh khởi", "vẫn sinh khởi")],
}


def _norm(t):
    return unicodedata.normalize("NFC", t).lower()


def first_in_text(text, cands):
    """The candidate value whose probe starts first in the text (word-bounded); None if no probe is there."""
    t = _norm(text)
    best = None
    for v, probe in cands:
        m = re.search(r"(?<!\w)" + re.escape(_norm(probe)) + r"(?!\w)", t)
        if m and (best is None or m.start() < best[0]):
            best = (m.start(), v)
    return best[1] if best else None


def _question_base(k):
    """-ti of the question dropped: anusetīti -> anuseti, anusentīti -> anusenti, pahīnoti -> pahīno."""
    for a, b in (("īti", "i"), ("oti", "o"), ("āti", "ā")):
        if k.endswith(a) and len(k) > 4:
            return k[: -len(a)] + b
    return k


def verb_value(kw, text):
    k = lc(kw).lower()
    if k not in VERBS:
        k = _question_base(k)
    if k not in VERBS:
        return None
    return first_in_text(text, VERBS[k]) or VERBS[k][0][0]


# ---------------------------------------------------------------------------- persons, planes, feelings
PERSONS = {
    "anāgāmissa": "bậc không trở lại", "anāgāmī": "bậc không trở lại", "anāgāmino": "bậc không trở lại",  # pi-4
    "puthujjanassa": "người phàm phu", "puthujjano": "người phàm phu",                                   # pi-1 / pi-4
    "arahato": "bậc A-la-hán", "arahā": "bậc A-la-hán",                                                  # pi-1 / pi-5
    # «Ở hai / ba / bốn hạng người», «Ở chính hạng người ấy» (Tasseva puggalassa), «Ở chính những hạng người ấy»
    # (Tesaññeva puggalānaṃ): the text writes «hạng người» for both (pi-4 puggalā / puggalānaṃ)
    "puggalānaṃ": "hạng người", "puggalassa": "hạng người", "puggalā": "hạng người",
}
PLANES = {
    "kāmadhātuyā": "cõi dục lạc", "rūpadhātuyā": "cõi hình sắc", "arūpadhātuyā": "cõi không hình sắc",   # pi-2
    "kāmadhātu": "cõi dục lạc", "rūpadhātu": "cõi hình sắc", "arūpadhātu": "cõi không hình sắc",
    "kāmadhātuṃ": "cõi dục lạc", "rūpadhātuṃ": "cõi hình sắc", "arūpadhātuṃ": "cõi không hình sắc",   # 7-10 (proposal)
    # proposals 7-02 …: «nơi những gì không nằm trong các cõi tồn tại» («nơi» = the locative frame, as «trong» of
    # «trong cõi hình sắc»; «những gì» kept: it is the substantive pronoun, not a plural marker; pi-1 apariyāpanna)
    "apariyāpanne": "những gì không nằm trong các cõi tồn tại",
    "sabbattha": "ở mọi nơi",                                                                            # pi-5
    # «Nơi tất cả các hiện tượng nằm trong tự ngã» (not a keyword in 7-01; proposal)
    "sabbasakkāyapariyāpannesu dhammesu": "tất cả các hiện tượng nằm trong tự ngã",
    "sabbasakkāyapariyāpannesu": "tất cả các hiện tượng nằm trong tự ngã",
}
FEELINGS = {
    "dvīsu vedanāsu": "hai loại cảm giác",           # «Nơi hai loại cảm giác trong cõi dục lạc» (numeral kept, pi-3)
    "tīsu vedanāsu": "ba loại cảm giác",
    "dukkhāya vedanāya": "cảm giác khó chịu",        # pi-2 / pi-5
    "dvīsu": "hai", "tīsu": "ba", "vedanāsu": "loại cảm giác",
    "sukhāya vedanāya": "cảm giác dễ chịu",          # proposal (pi-2)
    "adukkhamasukhāya vedanāya": "cảm giác không khó chịu cũng không dễ chịu",   # proposal (pi-1 / pi-2)
}
HEADINGS = {
    "sattānusayā": "bảy khuynh hướng tiềm ẩn",      # «Bảy khuynh hướng tiềm ẩn –» (keyword with its numeral)
    "(no direct equivalent)": NDE,                  # keyword-file placeholder (English «place»): no Pāli word
    "ekamūlakaṃ": "phần dựa trên một mục", "dukamūlakaṃ": "phần dựa trên bộ đôi",
    "tikamūlakaṃ": "phần dựa trên bộ ba", "catukkamūlakaṃ": "phần dựa trên bộ bốn",
    "pañcakamūlakaṃ": "phần dựa trên bộ năm", "chakkamūlakaṃ": "phần dựa trên bộ sáu",
    "kati": "bao nhiêu",                             # proposal 7-10 «bao nhiêu khuynh hướng tiềm ẩn …»
}


def vare_value(kw):
    """<X>vāre (locative of the closers «Chiều thuận trong mục về khuynh hướng tiềm ẩn.») = the <X>vāro heading
    («trong» = the locative frame); <X>vāra = the same."""
    k = lc(kw).lower()
    for end in ("vāre", "vāra"):
        if k.endswith(end) and k[: -len(end)] + "vāro" in FORMULAS:
            return FORMULAS[k[: -len(end)] + "vāro"]
    return None


T701 = {**PERSONS, **PLANES, **FEELINGS, **HEADINGS}


def value701(kw, kws, table=None, text=None):
    """table -> T701 -> tendency_value -> verb_value -> vare_value -> map_sample_vi.value6."""
    t = text or ""
    k = lc(kw).lower()
    if table:
        if kw in table:
            return table[kw]
        if lc(kw) in table:
            return table[lc(kw)]
    if k in T701:
        return T701[k]
    for fn in (tendency_value, vare_value):
        v = fn(kw)
        if v is not None:
            return v
    v = verb_value(kw, t)
    if v is not None:
        return v
    return value6(kw, kws, table, t)


# per-segment choices
OVERRIDES = {}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value701(kw, kws, None, vi.get(bid, ""))
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
