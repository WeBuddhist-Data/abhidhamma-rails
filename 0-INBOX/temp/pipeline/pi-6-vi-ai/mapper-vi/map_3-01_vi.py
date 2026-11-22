"""Pāli->Vietnamese keyword map, pi-6 (Yamaka) chapter 3-01-ayatanayamaka (frame-setter of the Āyatanayamaka).

usage: python -I -X utf8 -B map_3-01_vi.py          (writes 3-01-ayatanayamaka.mapped.md and verifies it)

Importing this module builds nothing. Later Āyatanayamaka chapters (3-02 … 3-06) and 4-dhatuyamaka load it with
importlib and reuse the named tables:
    import importlib; A3 = importlib.import_module("map_3-01_vi")
    A3.BASES      the twelve bases, stem -> «lĩnh vực X» (cakkhāyatana = lĩnh vực mắt … dhammāyatana = lĩnh vực đối
                  tượng của ý)
    A3.BARE       the bare words, stem -> Vietnamese (cakkhu mắt … mano ý, rūpa vật chất, dhamma hiện tượng)
    A3.AYATANA    āyatana itself (āyatanaṃ / āyatanā = lĩnh vực nhận biết; nāyatanaṃ / nāyatanā = không phải là
                  (các) lĩnh vực nhận biết)
    A3.ATTR       the attributes of the beings (sacakkhukānaṃ = có mắt, acakkhukānaṃ = không có mắt, sasotaka-,
                  saghānaka-, sarūpaka-, sacittaka- …; «có» = having, kept)
    A3.SENSE      the non-base senses of 3-01 ^6-3-10 (Dibbacakkhu thiên nhãn, paññācakkhu mắt trí tuệ, …)
    A3.PLANE_LOC  the planes in the locative of the answers («Trong cõi X» -> cõi X; «Trong» is frame)
    A3.BEINGS_GEN the beings in the genitive («Ở chúng sinh trong cõi X» -> chúng sinh trong cõi X; the second item
                  of a list, where the text does not repeat «chúng sinh trong», -> cõi X)
    A3.HEADS      the section headings, notes and closers of 3-01
    A3.forms(stem_table)  every inflected keyword form of a stem table (-aṃ, -nti, -ñca, -ñceva, -ssa, -o / -oti …)
    A3.T3_01      all fixed values of this chapter (keys: lower-case first letter, as value6 looks them up)
    A3.value3(kw, kws, table=None, text=None)  = your table -> T3_01 -> BEINGS_GEN pick -> map_sample_vi.value6
Shared frames (verbs, beings, planes, relatives) are 2-01's (map_2-01_vi.py); where 2-01 and this file differ,
2-01 wins for the shared frames, this file for the Āyatana members.
Conventions: pi-1 … pi-5 vi-map-conventions*.md + notes, pi-5 map-coordinator-rules.md, vi-map-conventions-pi6.md,
pi-6 map-coordinator-rules.md; notes-map-3-01.md lists what this chapter adds.
"""
import pathlib
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import map_sample_vi as S  # noqa: E402
from map_common_vi import GAP, NDE, build_part, lc, pick, read_vietnamese, verify  # noqa: E402

PART = "3-01-ayatanayamaka"

# ---------------------------------------------------------------------------- the twelve bases (pi-2 ^2-155)
BASES = {
    "cakkhāyatana": "lĩnh vực mắt", "sotāyatana": "lĩnh vực tai", "ghānāyatana": "lĩnh vực mũi",
    "jivhāyatana": "lĩnh vực lưỡi", "kāyāyatana": "lĩnh vực thân", "rūpāyatana": "lĩnh vực hình sắc",
    "saddāyatana": "lĩnh vực âm thanh", "gandhāyatana": "lĩnh vực mùi", "rasāyatana": "lĩnh vực vị",
    "phoṭṭhabbāyatana": "lĩnh vực vật xúc chạm", "manāyatana": "lĩnh vực ý",
    "dhammāyatana": "lĩnh vực đối tượng của ý",
}

# ---------------------------------------------------------------------------- the bare words (subject of the pair)
# «Mắt có phải là lĩnh vực mắt không?», «Vật chất có phải là lĩnh vực hình sắc không?», «Hiện tượng có phải là lĩnh
# vực đối tượng của ý không?»; stem -> (Vietnamese, the stem's own nominative forms)
BARE = {
    "cakkhu": "mắt", "sota": "tai", "ghāna": "mũi", "jivhā": "lưỡi", "kāya": "thân", "rūpa": "vật chất",
    "sadda": "âm thanh", "gandha": "mùi", "rasa": "vị", "phoṭṭhabba": "vật xúc chạm", "mana": "ý",
    "dhamma": "hiện tượng",
}
_BARE_FORMS = {
    "cakkhu": ("cakkhu", "cakkhūti", "cakkhuṃ", "cakkhuñca", "cakkhuñceva"),
    "sota": ("sotaṃ", "sotanti", "sotañca", "sotañceva"),
    "ghāna": ("ghānaṃ", "ghānanti", "ghānañca", "ghānañceva"),
    "jivhā": ("jivhā", "jivhāti", "jivhaṃ", "jivhañca", "jivhā ceva"),
    "kāya": ("kāyo", "kāyoti", "kāyaṃ", "kāyañca", "kāyo ceva"),
    "rūpa": ("rūpaṃ", "rūpanti", "rūpañca", "rūpañceva"),
    "sadda": ("saddo", "saddoti", "saddaṃ", "saddañca", "saddo ceva"),
    "gandha": ("gandho", "gandhoti", "gandhaṃ", "gandhañca", "gandho ceva"),
    "rasa": ("raso", "rasoti", "rasaṃ", "rasañca", "raso ceva"),
    "phoṭṭhabba": ("phoṭṭhabbo", "phoṭṭhabboti", "phoṭṭhabbaṃ", "phoṭṭhabbañca", "phoṭṭhabbo ceva"),
    "mana": ("mano", "manoti", "manaṃ", "manañca", "mano ceva"),
    "dhamma": ("dhammo", "dhammoti", "dhammaṃ", "dhammañca", "dhammo ceva"),
}

# ---------------------------------------------------------------------------- āyatana itself
# leading «Các» dropped (pi-1 value form: khandhā = khối); the fused negative na-āyatana keeps «không phải là» (the
# keyword's own na, with the copula as the text writes it; inner «các» kept)
AYATANA = {
    "āyatanaṃ": "lĩnh vực nhận biết", "āyatananti": "lĩnh vực nhận biết", "āyatanañca": "lĩnh vực nhận biết",
    "āyatanañceva": "lĩnh vực nhận biết", "āyatanā": "lĩnh vực nhận biết", "āyatanāti": "lĩnh vực nhận biết",
    "āyatana": "lĩnh vực nhận biết", "āyatanāni": "lĩnh vực nhận biết",
    "nāyatanaṃ": "không phải là lĩnh vực nhận biết", "nāyatananti": "không phải là lĩnh vực nhận biết",
    "nāyatanā": "không phải là các lĩnh vực nhận biết", "nāyatanāti": "không phải là các lĩnh vực nhận biết",
}

# ---------------------------------------------------------------------------- attributes of the beings
# «Ở những người đang tái sinh có mắt và không có tai, …» («và» joins the attributes; «những người» belongs to
# upapajjantānaṃ / cavantānaṃ); «có» = having (pi-1 sa- / -ika), kept
ATTR = {
    "sacakkhukānaṃ": "có mắt", "acakkhukānaṃ": "không có mắt",
    "sasotakānaṃ": "có tai", "asotakānaṃ": "không có tai",
    "saghānakānaṃ": "có mũi", "aghānakānaṃ": "không có mũi",
    "sarūpakānaṃ": "có vật chất", "arūpakānaṃ": "không có vật chất",
    "sacittakānaṃ": "có tâm", "acittakānaṃ": "không có tâm",
}

# ---------------------------------------------------------------------------- non-base senses (^6-3-10 / ^6-3-11)
# «Mắt hiểu theo nghĩa thiên nhãn, mắt trí tuệ thì là mắt …» («Mắt hiểu theo nghĩa» is the frame of the predicate)
SENSE = {
    "dibbacakkhu": "thiên nhãn", "paññācakkhu": "mắt trí tuệ",
    "dibbasotaṃ": "thiên nhĩ", "taṇhāsotaṃ": "dòng chảy của khao khát",
    "sīlagandho": "hương của giới hạnh", "samādhigandho": "hương của định tâm", "paññāgandho": "hương của trí tuệ",
    "attharaso": "vị của ý nghĩa", "dhammaraso": "vị của Giáo Pháp", "vimuttiraso": "vị của sự giải thoát",
}

# ---------------------------------------------------------------------------- planes (locative) and beings (genitive)
# «Trong cõi hình sắc, thì ở nơi ấy …»: the locative «Trong» is frame (pi-6 conventions)
PLANE_LOC = {
    "kāmāvacare": "cõi dục lạc", "rūpāvacare": "cõi hình sắc", "arūpāvacare": "cõi không hình sắc",
    "arūpe": "cõi không hình sắc", "asaññasatte": "cõi Vô Tưởng", "suddhāvāse": "cõi Tịnh Cư",
    "pañcavokāre": "cõi gồm năm khối", "catuvokāre": "cõi gồm bốn khối", "ekavokāre": "cõi gồm một khối",
}
# «Ở chúng sinh trong cõi hình sắc, cõi không hình sắc, thì …»: the head noun «chúng sinh (trong)» is the keyword's
# own (as asaññasattānaṃ = chúng sinh Vô Tưởng, pi-4 names with their head noun); the second item of a list has
# only «cõi X» in the text. Candidates, best first (the caller keeps the first present).
_PLANES = {"kāmāvacarānaṃ": "cõi dục lạc", "rūpāvacarānaṃ": "cõi hình sắc", "arūpāvacarānaṃ": "cõi không hình sắc",
           "arūpānaṃ": "cõi không hình sắc", "suddhāvāsānaṃ": "cõi Tịnh Cư",
           "pañcavokārānaṃ": "cõi gồm năm khối", "catuvokārānaṃ": "cõi gồm bốn khối",
           "ekavokārānaṃ": "cõi gồm một khối"}
BEINGS_GEN = {k: ["chúng sinh trong " + v, v] for k, v in _PLANES.items()}
BEINGS_GEN["asaññasattānaṃ"] = ["chúng sinh Vô Tưởng"]

# ---------------------------------------------------------------------------- headings, notes, closers
HEADS = {
    "suddhāyatanavāro": "mục về các lĩnh vực nhận biết thuần túy",          # = Suddhakhandhavāro
    "suddhāyatanamūlacakkavāro": "mục về vòng luân chuyển dựa trên các lĩnh vực nhận biết thuần túy",
    "paṇṇattiuddesavāro": "mục nêu đề mục về sự định danh",                # closer «Mục nêu đề mục về sự định danh.»
    "paṇṇattiniddesavāro": "mục giải thích về sự định danh",               # closer «Mục giải thích về sự định danh.»
    "cakkaṃ": "vòng luân chuyển",          # (Cakkaṃ bandhitabbaṃ) «(Nên nối kết thành vòng luân chuyển)»
    "vārasaṅkhepo": "sự tóm lược các mục",  # «ở phần sau có sự tóm lược các mục» (inner «các» kept)
    "yassakasadisaṃ": "giống như phần về người",   # (saṃkhittaṃ yassakasadisaṃ) «(tóm lược, giống như phần về người)»
    "yassaka": "phần về người", "yatthakaṃ": "phần về nơi chốn", "yatthaka": "phần về nơi chốn",
    "sadisaṃ": "giống như",
    # (yatthakaṃ paccuppannepi atītepi …) «… ở hiện tại, ở quá khứ, …»: locative nouns, «ở» is frame (pi-5 Rūpasmiṃ);
    # -pi has no word of its own («đều» is the frame of the sentence)
    "paccuppannepi": "hiện tại", "atītepi": "quá khứ", "anāgatepi": "tương lai",
    "paccuppannātītepi": "hiện tại và quá khứ", "paccuppannānāgatepi": "hiện tại và tương lai",
    "atītānāgatepi": "quá khứ và tương lai",
    "avaseso": "còn lại", "avasesaṃ": "còn lại",   # «những gì còn lại» (avasesā = còn lại, pi-1 … pi-4)
    "sotāyananti": "lĩnh vực tai",          # ^6-3-13 spelling slip for sotāyatananti (translated as meant)
    # (no direct equivalent) is itself a keyword in the extraction (^6-3-12, ^6-3-23): no Pāli word to map
    "(no direct equivalent)": NDE,
}


def forms(stem_table):
    """Every inflected keyword form of a base stem -> value (lower case)."""
    out = {}
    for s, v in stem_table.items():
        for suf in ("ṃ", "nti", "ñca", "ñceva", "", "ssa", "ṃ ceva"):
            out[s + suf] = v
        out[s + "mūlakaṃ"] = "phần dựa trên " + v   # (Cakkhāyatanamūlakaṃ) «(Phần dựa trên lĩnh vực mắt)» (7-01)
    return out


T3_01 = {}
T3_01.update(forms(BASES))
for _stem, _fs in _BARE_FORMS.items():
    for _f in _fs:
        T3_01[_f] = BARE[_stem]
T3_01.update(AYATANA)
T3_01.update(ATTR)
T3_01.update(SENSE)
T3_01.update(PLANE_LOC)
T3_01.update(HEADS)


def value3(kw, kws, table=None, text=None):
    """your table -> T3_01 -> BEINGS_GEN (first candidate present) -> map_sample_vi.value6."""
    k = lc(kw)
    t = text or ""
    if table and k in table:
        return table[k]
    if k in T3_01:
        return T3_01[k]
    if k in BEINGS_GEN:
        v = pick(t, *BEINGS_GEN[k])
        if v:
            return v
        return BEINGS_GEN[k][0]
    if " " not in k and len(k) > 4 and k.endswith("ti") and k[-3] in _LONG and k[:-3] + _LONG[k[-3]] in _VERBS:
        # the question -ti of a verb (uppajjatīti, nuppajjitthāti): the verb's own value (context6 / FORMULAS)
        return value3(k[:-3] + _LONG[k[-3]], kws, table, t)
    return S.value6(kw, kws, table, t)


_LONG = {"ī": "i", "ā": "a", "ū": "u"}
_VERBS = {k for k in S.FORMULAS if k.endswith(("ti", "ttha"))}


# part-specific values (everything recurring lives in the tables above)
T3_01_PART = {
    # ^6-3-43 «…dhammāyatanañca uppajjittharūpāyatanañca uppajjittha» (space missing in the Pāli): «… đã sinh khởi,
    # đồng thời lĩnh vực hình sắc cũng đã sinh khởi» (Pāli order, not adjacent: « … »)
    "uppajjittharūpāyatanañca": "đã sinh khởi" + GAP + "lĩnh vực hình sắc",
}

OVERRIDES = {}

ALLOWED = {}


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value3(kw, kws, T3_01_PART, vi.get(bid, ""))
    return resolve


if __name__ == "__main__":
    build_part(PART, resolver())
    verify(PART, ALLOWED)
