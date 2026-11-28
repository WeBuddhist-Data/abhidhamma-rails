"""G45 dhātu + sacca: Pāli->Russian keyword maps for pi-6 4-dhatuyamaka, 5-01 … 5-03-saccayamaka.

usage:  python -I -X utf8 -B map_G45_ru.py [PART ...]     (writes <part>.mapped.md for the G45 parts and verifies them)
import: importing writes nothing. Later groups:
    import importlib, sys; sys.path.insert(0, r"...\\pi-6-ru\\mapper-ru"); G45 = importlib.import_module("map_G45_ru")
    G45.DHATU (the Dhātuyamaka members), G45.SACCA (the Saccayamaka members), G45.MOMENTS (the sacca time / person
    units: taṇhā / magga / phala moments, vippayutta minds, abhisametāvī, āpāyika, arahantānaṃ …),
    G45.PJ3_FRAME / G45.pj3_value() (pajahati in all tenses), G45.NOTES_KW (yassaka / yatthaka / vāra notes),
    G45.G45_TABLE = YM + G2_FRAME + G8 (TENSE, TIME, PERSONS) + all of the above.

Resolution per keyword: OVERRIDES[bid][kw] -> G2.frame_value() (denied negative of uppajjati, pariññā word order,
pacchimabhavika) -> pj3_value() (pajahati denied negative) -> G45_TABLE (with the -ti / -ñca / -ñceva / -pi / -mpi
folds) -> CORE (the Namo line) -> value() (pi-2 KH, pi-1 CH2 / MATRIX).
Frame values are imported from map_G2_ru (G2_FRAME, frame_value, frame_exceptions) and map_G8_ru (TENSE, TIME,
PERSONS); G2_KHANDHA is NOT imported (its rūpaṃ = «форма» is set here per chapter: the Dhātuyamaka bare word is
«форма» too, by its own text). Every segment of the four parts was read against its Russian (builders build_4_ru.py,
build_5-0N_ru.py; notes-4.md, notes-5-0N.md). Decisions: notes-map-G45.md.
"""
import importlib
import pathlib
import re
import sys

sys.dont_write_bytecode = True
_HERE = pathlib.Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))
from map_common_pi6_ru import (CORE, NDE, YM, build_part, lc, present, read_pali,  # noqa: E402,F401
                               read_russian, value, verify)

G2 = importlib.import_module("map_G2_ru")
G8 = importlib.import_module("map_G8_ru")

PARTS = ["4-dhatuyamaka", "5-01-saccayamaka", "5-02-saccayamaka", "5-03-saccayamaka"]

# =============================================================================================== Dhātuyamaka
# bare words (Russian «Глаз является элементом глаза?»; pi-2 / 3-01 terms, build_4_ru DH_X): every case form and the
# -ti / -ñca / -ñceva / -pi forms take the nominative
BARE = {
    "cakkhu": "глаз", "sota": "ухо", "ghāna": "нос", "jivhā": "язык", "kāya": "тело", "rūpa": "форма",
    "sadda": "звук", "gandha": "запах", "rasa": "вкус", "phoṭṭhabba": "осязаемое",
    "cakkhuviññāṇa": "зрительное сознание", "sotaviññāṇa": "слуховое сознание",
    "ghānaviññāṇa": "обонятельное сознание", "jivhāviññāṇa": "вкусовое сознание",
    "kāyaviññāṇa": "осязательное сознание", "mana": "ум", "manoviññāṇa": "умственное сознание",
    "dhamma": "явление",
}
# the eighteen elements (pi-2 ^2-183; «элемент глаза … элемент объектов ума»)
DHATU_NAME = {
    "cakkhu": "элемент глаза", "sota": "элемент уха", "ghāna": "элемент носа", "jivhā": "элемент языка",
    "kāya": "элемент тела", "rūpa": "элемент видимых форм", "sadda": "элемент звуков",
    "gandha": "элемент запахов", "rasa": "элемент вкусов", "phoṭṭhabba": "элемент осязаемого",
    "cakkhuviññāṇa": "элемент зрительного сознания", "sotaviññāṇa": "элемент слухового сознания",
    "ghānaviññāṇa": "элемент обонятельного сознания", "jivhāviññāṇa": "элемент вкусового сознания",
    "kāyaviññāṇa": "элемент осязательного сознания", "mano": "элемент ума",
    "manoviññāṇa": "элемент умственного сознания", "dhamma": "элемент объектов ума",
}

DHATU = {}
for _s, _v in BARE.items():
    if _s.endswith("u"):                                     # cakkhu
        forms = [_s, _s + "ṃ", _s + "ñca", _s[:-1] + "ūti"]
    elif _s.endswith("ā"):                                   # jivhā
        forms = [_s, _s + "ti", _s[:-1] + "a", _s[:-1] + "aṃ"]
    elif _s in ("kāya", "sadda", "gandha", "rasa", "phoṭṭhabba", "dhamma"):   # masculine -o
        forms = [_s[:-1] + e for e in ("o", "oti", "aṃ", "añca", "añceva")]
    elif _s == "mana":                                       # mano / manaṃ (Manañca)
        forms = ["mano", "manoti", "manaṃ", "manañca"]
    else:                                                    # neuter -aṃ (sotaṃ, rūpaṃ, …viññāṇaṃ)
        forms = [_s[:-1] + e for e in ("aṃ", "anti", "añca", "añceva")]
    for _f in forms:
        DHATU[_f] = _v
for _s, _v in DHATU_NAME.items():
    for _e in ("dhātu", "dhātū", "dhātūti", "dhātuṃ", "dhātuñca"):
        DHATU[_s + _e] = _v
DHATU.update({
    "dhātu": "элемент", "dhātūti": "элемент",                # «является элементом» (quoted singular dhātu+iti)
    "dhātuñca": "элемент", "dhātuṃ": "элемент",
    "dhātū": "элементы", "dhātuyo": "элементы",               # «Элементы являются …», «Восемнадцать элементов»
    "dibbacakkhu": "божественный глаз", "paññācakkhu": "глаз мудрости",
    "dibbasotaṃ": "божественное ухо", "taṇhāsotaṃ": "поток жажды",
    "sīlagandho": "запах нравственности", "samādhigandho": "запах сосредоточения", "paññāgandho": "запах мудрости",
    "attharaso": "вкус смысла", "dhammaraso": "вкус Учения", "vimuttiraso": "вкус освобождения",
    "ghānasadiso": "такой же как нос",                       # «(Звук такой же, как нос)»
    "ghānadhātusadisā": "такой же как элемент носа",         # «(Язык тоже такой же, как элемент носа)»
    "jivha": "язык",                                         # ^6-4-15 «jivha ṭhapetvā» slip (rendered as meant)
    "cakkaṃ": "круг",                                        # «круг следует замкнуть»
    "paṇṇatti": "обозначения",                               # «Как обозначения в парных вопросах …» (text plural)
    "dhātuyamakaṃ": "парные вопросы об элементах", "dhātuyamake": "парные вопросы об элементах",
    "dhātuyamakassa": "парные вопросы об элементах",
    "āyatanayamakaṃ": "парные вопросы о сферах восприятия", "āyatanayamake": "парные вопросы о сферах восприятия",
    "āyatanayamakassa": "парные вопросы о сферах восприятия",
    "suddhadhātuvāro": "раздел об элементах как таковых",
    "suddhadhātumūlacakkavāro": "круговой раздел на основе элементов как таковых",
    # person units of the pavatti frame («перерождается с глазом и без уха»): the prepositional phrase the text uses
    "sacakkhukānaṃ": "с глазом", "acakkhukānaṃ": "без глаза",
    "sasotakānaṃ": "с ухом", "asotakānaṃ": "без уха",
})

# =============================================================================================== Saccayamaka
TRUTH = {"dukkha": "страдании", "samudaya": "возникновении", "nirodha": "прекращении", "magga": "пути"}
SACCA = {}
for _s, _g in TRUTH.items():
    for _e in ("saccaṃ", "saccanti", "saccañca", "saccañceva"):
        SACCA[_s + _e] = "истина о " + _g
SACCA.update({
    "saccaṃ": "истина", "saccanti": "истина", "saccañca": "истина", "saccañceva": "истина",
    "saccā": "истины", "saccāni": "истины",                  # «Истины являются …», «Четыре истины»
    # bare words (pi-2 truth names; «Страдание является истиной?»)
    "dukkhaṃ": "страдание", "dukkhanti": "страдание", "dukkhañca": "страдание", "dukkhañceva": "страдание",
    "samudayo": "возникновение", "samudayoti": "возникновение", "samudayaṃ": "возникновение",
    "samudayañca": "возникновение",
    "nirodho": "прекращение", "nirodhoti": "прекращение", "nirodhaṃ": "прекращение", "nirodhañca": "прекращение",
    "maggo": "путь", "maggoti": "путь", "maggaṃ": "путь", "maggañca": "путь",
    "kāyikaṃ dukkhaṃ": "телесное страдание", "cetasikaṃ dukkhaṃ": "душевное страдание",
    "avasesaṃ": "остальной", "avaseso": "остальной", "avasesā": "остальной", "avasese": "остальной",
    "ṭhapetvā": "кроме",
    "saccayamakaṃ": "парные вопросы об истинах",
    "suddhasaccavāro": "раздел об истинах как таковых",
    "suddhasaccamūlacakkavāro": "круговой раздел на основе истин как таковых",
    "paṇṇattivāra": "раздел об обозначениях",
})

# -- pavatti units of the Saccayamaka (locative time phrases -> nominative noun phrase without «в», as G8 TIME;
#    the comma of «ума, не связанного с жаждой» dropped, as G8 «ума охваченного страстью»)
VIPP = {"taṇhāvippayutta": "не связанного с жаждой", "maggavippayutta": "не связанного с путём",
        "taṇhāvippayuttamaggavippayutta": "не связанного с жаждой и не связанного с путём",
        "maggavippayuttataṇhāvippayutta": "не связанного с путём и не связанного с жаждой"}
MOMENTS = {}
for _s, _g in VIPP.items():
    MOMENTS[_s + "cittassa uppādakkhaṇe"] = "момент возникновения ума " + _g
    MOMENTS[_s + "cittassa bhaṅgakkhaṇe"] = "момент распада ума " + _g
    MOMENTS[_s + "cittassa"] = "ум " + _g.replace("связанного", "связанный")
    MOMENTS[_s + "citte"] = "ум " + _g.replace("связанного", "связанный")   # «когда присутствует ум, не связанный …»
MOMENTS.update({
    "taṇhāya uppādakkhaṇe": "момент возникновения жажды", "taṇhāya bhaṅgakkhaṇe": "момент распада жажды",
    "upapatticittassa uppādakkhaṇe": "момент возникновения ума перерождения",
    "upapatticittassa bhaṅgakkhaṇe": "момент распада ума перерождения",
    "pavatte": "течение жизни",                               # «в течение жизни»
    "citte": "ум", "akusale citte": "неблагой ум",           # «когда присутствует второй (неблагой) ум»
    "vattamāne": "присутствовать",                            # «когда присутствует»
    "cittassa": "ум",                                         # «сразу после данного ума», «этого ума»
    "anantarā": "сразу после",
    "maggassa": "путь", "phalassa": "плод",                  # «в момент возникновения пути и плода»
    "aggamaggassa": "высший путь", "aggaphalassa": "высший плод",
    "aggamaggaṃ paṭilabhissanti": "обрести высший путь",     # «кто обретёт высший путь»
    "aggamaggaṃ paṭilabhissānti": "обрести высший путь",     # ^6-5-74 slip (rendered as meant)
    "aggamaggasamaṅgīnaṃ": "обладающий высшим путём",        # G2 aggamaggasamaṅgī
    "arahantānaṃ": "архаты",                                  # «у архатов» (Pāli and Russian plural)
    "abhisametāvīnaṃ": "постигший истины", "anabhisametāvīnaṃ": "не постигший истины",
    "āpāyikānaṃ": "существа низших миров",                    # «у существ низших миров»
    "apāye": "низшие миры",                                   # «В низших мирах»
    "caññe": "другой",                                        # «у других, кто обретёт путь» (ca = и, no word)
    "asaññattā": "существа без восприятия",                   # ^6-5-76 slip for asaññasattā (rendered as meant)
    "nirujjhiti": "прекращаться",                             # ^6-5-125 slip for nirujjhati (rendered as meant)
    "yassa yattha": "у кого где",                             # «У кого где …»
})

# -- editorial notes: vāra and yassaka / yatthaka words (-pi / -mpi = «и … и» / «тоже», no word of its own)
NOTES_KW = {
    "yatthakaṃ": "раздел с «где»", "yatthakā": "разделы с «где»",
    "yassakaṃ": "раздел с «у кого»", "yassayatthakaṃ": "раздел с «у кого где»",
    "yassayatthake": "раздел с «у кого где»",                # «в разделе с «у кого где»»
    "yatthakasadisaṃ": "такой же как в разделе с «где»",      # «такое же, как в разделе с «где» выше»
    "yassayatthakasadisaṃ": "так же как раздел с «у кого где»",   # «изложить так же, как раздел с «у кого где»»
    "uppāde": "раздел о возникновении", "nirodhe": "раздел о прекращении",          # harmonise_apply edit 3
    "uppādanirodhe": "раздел о возникновении и прекращении",
    "uppādavāre": "раздел о возникновении", "nirodhavāre": "раздел о прекращении",
    "uppādanirodhavāre": "раздел о возникновении и прекращении",
    "anulomaṃ": "утвердительная форма", "paccanīkaṃ": "отрицательная форма",
    "anulomampi": "утвердительная … форма",                   # «и в утвердительной, и в отрицательной форме»
    "pucchā": "вопросы",                                      # «вопросы о прошлом» (harmonise_apply edit 2)
    "nirodhasamāpannānaṃ": "вошедший в медитативное достижение прекращения",   # also the quoted -nti form
}

# =============================================================================================== pajahati (5-03)
# 7-01 / G7: pajahati = устранять. New tenses (notes-5-03): pajahittha «устранил» and pajahissati «устранит» =
# устранить (perfective). Glued n-: «не V» where that tense is negated in the segment's Russian, else the positive
# verb the text has (denied negative «no ca Y nappajahittha» = «но устранил Y»; coordinator "Negatives").
PJ3_VERB = {"pajahati": "устранять", "pajahanti": "устранять", "pajahittha": "устранить",
            "pajahissati": "устранить", "pajahissanti": "устранить"}
PJ3_NEG_RU = {"pajahati": r"не\s+устраня(ет|ют)", "pajahanti": r"не\s+устраня(ет|ют)",
              "pajahittha": r"не\s+устранил", "pajahissati": r"не\s+устран(ит|ят)",
              "pajahissanti": r"не\s+устран(ит|ят)"}
PJ3_FRAME = {}
for _f, _v in PJ3_VERB.items():
    PJ3_FRAME[_f] = PJ3_FRAME[G2._ti(_f)] = _v
    PJ3_FRAME["nap" + _f] = PJ3_FRAME[G2._ti("nap" + _f)] = "не " + _v   # nappajahati …


def pj3_value(kw, ru):
    k = lc(kw)
    for base in PJ3_VERB:
        neg = "nap" + base
        if k in (neg, G2._ti(neg)):
            return "не " + PJ3_VERB[base] if re.search(PJ3_NEG_RU[base], ru.lower()) else PJ3_VERB[base]
    return None


# =============================================================================================== the table
G45_TABLE = {**YM, **G2.G2_FRAME, **G8.TENSE, **G8.TIME, **G8.PERSONS,
             **DHATU, **SACCA, **MOMENTS, **NOTES_KW, **PJ3_FRAME}
G45_TABLE.update({
    "natthi": "такого нет",                  # G2 / G8 (YM still has нет)
    "rūpaṃ": "форма",                        # Dhātuyamaka bare word «Форма является элементом?» (not материальная)
})

# per-segment readings {block id: {keyword exactly as listed: Russian}}
OVERRIDES = {
    # «В остальном существовании с четырьмя составляющими и с пятью составляющими» (the noun is said once)
    "6-5-30": {"pañcavokāre": "существование … с пятью составляющими"},
}


def _folds(k):
    """-ti / -nti / -oti / -āti / -īti / -ūti, -ñca / -ñceva, -pi / -mpi: candidate base keys."""
    out = [k]
    for end, rep in (("ñceva", "ṃ"), ("ñca", "ṃ"), ("mpi", "ṃ"), ("nti", "ṃ")):
        if k.endswith(end):
            out.append(k[: -len(end)] + rep)
    if k.endswith("pi") and not k.endswith("mpi"):
        out.append(k[:-2])
    if k.endswith(("oti", "āti", "īti", "ūti")):
        out.append(k[:-2])
    return out


def resolver_for(part, table=None):
    t = G45_TABLE if table is None else table
    pa, ru = read_pali(part), read_russian(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        text = ru.get(bid, "")
        v = G2.frame_value(kw, pa.get(bid, ""), text)
        if v is not None:
            return v
        v = pj3_value(kw, text)
        if v is not None:
            return v
        k = lc(kw)
        if k == "arahato" and "Достойн" in text:
            return CORE["arahato"]                              # the Namo line (^6-4-19)
        for b in _folds(k):
            if b in t:
                return t[b]
        if k in CORE:
            return CORE[k]
        return value(kw, kws, t)
    return resolve


# =============================================================================================== presence exceptions
# Perfective infinitive vs the future / past form in the text (stem change outside present()'s tolerance); each is
# accepted only if the stated Russian form is in the segment (self-checking, as G2.FRAME_EXC_RU).
G45_EXC_RU = {
    "aggamaggaṃ paṭilabhissanti": (r"обрет(ёт|ут) высший путь", "обрести высший путь ~ обретёт высший путь"),
    "aggamaggaṃ paṭilabhissānti": (r"обрет(ёт|ут) высший путь", "обрести высший путь ~ обретёт высший путь"),
}
for _b in ("pajahissati", "pajahissanti", "pajahittha"):
    _re = r"устранил" if _b.endswith("ttha") else r"устран(ит|ят)"
    for _k in (_b, "nap" + _b):
        G45_EXC_RU[_k] = G45_EXC_RU[G2._ti(_k)] = (_re, "устранить ~ " + ("устранил" if _re == r"устранил"
                                                                         else "устранит/устранят"))


def exceptions_for(part):
    return G2.frame_exceptions(part, exc={**G2.FRAME_EXC_RU, **G45_EXC_RU})


if __name__ == "__main__":
    for p in (sys.argv[1:] or PARTS):
        build_part(p, resolver_for(p))
        verify(p, show=300, allowed=exceptions_for(p))
