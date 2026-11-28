"""G3 āyatana: Pāli->Russian keyword maps for pi-6 3-01-ayatanayamaka … 3-06-ayatanayamaka.

usage:  python -I -X utf8 -B map_G3_ru.py [PART ...]   (writes <part>.mapped.md and verifies it; default: all six)
import: importing writes nothing. Later groups:

    import importlib, sys; sys.path.insert(0, r"...\\pi-6-ru\\mapper-ru"); G3 = importlib.import_module("map_G3_ru")
    G3.AY_MEMBERS (the twelve bases in every case form + bare paṇṇatti words), G3.AY_PLANES (kāma- / rūpa- /
    arūpāvacara in every plane form), G3.AY_HAVE (sa-X-ka / a-X-ka person descriptors), G3.AY_FRAME (section names,
    -pi forms, time words), G3.G3_TABLE (= YM + G2_FRAME + all of the above)

Frame values are imported from the frame-setter G2 (map_G2_ru: G2_FRAME, frame_value(), frame_exceptions()); G2_KHANDHA
is NOT imported (its rūpaṃ = «форма» is set here again for the Āyatana paṇṇattivāra, where the text says «форма» too).
map_G8_ru was checked: no citta-type moment / participle keyword occurs in 3-01 … 3-06, so nothing of it is needed.

Resolution per keyword: OVERRIDES[bid][kw] -> G2.frame_value() (denied negative, pariññā word order, pacchimabhavika)
-> G3_TABLE (-ti / -nti / -ñca / -ñceva folded) -> CORE -> value() (YM -> pi-2 KH -> pi-1 CH2 / MATRIX).
See notes-map-G3.md for every value.
"""
import importlib
import pathlib
import sys

sys.dont_write_bytecode = True
_HERE = pathlib.Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))
from map_common_pi6_ru import CORE, NDE, YM, build_part, lc, value, verify  # noqa: E402

G2 = importlib.import_module("map_G2_ru")

PARTS = [f"3-0{i}-ayatanayamaka" for i in range(1, 7)]

# =============================================================================================== members
# the twelve bases (pi-2 ^2-155, pi-1; build_3-01_ru AY_K): every case form takes the nominative
AY_BASE = {
    "cakkh": "сфера глаза", "sot": "сфера уха", "ghān": "сфера носа", "jivh": "сфера языка",
    "kāy": "сфера тела", "rūp": "сфера видимых форм", "sadd": "сфера звуков", "gandh": "сфера запахов",
    "ras": "сфера вкусов", "phoṭṭhabb": "сфера осязаемого", "man": "сфера ума", "dhamm": "сфера объектов ума",
}
AY_MEMBERS = {}
for _s, _v in AY_BASE.items():
    for _e in ("āyatanaṃ", "āyatana"):
        AY_MEMBERS[_s + _e] = _v
    # (Cakkhāyatanamūlakaṃ) = «(На основе сферы глаза)» (as G7 kāmadhātumūlakaṃ = на основе мира …)
    AY_MEMBERS[_s + "āyatanamūlakaṃ"] = "на основе " + _v.replace("сфера", "сферы", 1)
AY_MEMBERS.update({
    "sotāyanaṃ": "сфера уха",                       # ^6-3-13 slip sotāyananti = sotāyatananti (rendered as meant)
    "āyatanaṃ": "сфера восприятия", "āyatanā": "сферы восприятия",
    # glued negation na + āyatana: «То, что не является сферами восприятия / сферой восприятия» (" … ": the verb
    # «является» stands between; as G2 nuppajjati = не возникать keeps the glued negation)
    "nāyatanā": "не … сферы восприятия", "nāyatanaṃ": "не … сфера восприятия",
    # bare words of the paṇṇattivāra (build_3-01_ru AY_X / AY_LEX): «Глаз является сферой глаза?»
    "cakkhu": "глаз", "cakkhū": "глаз", "cakkhuṃ": "глаз", "sotaṃ": "ухо", "ghānaṃ": "нос",
    "jivhā": "язык", "jivhaṃ": "язык", "kāyo": "тело", "kāyaṃ": "тело",
    "rūpaṃ": "форма",                               # «Форма является сферой видимых форм?» (not материальная форма)
    "saddo": "звук", "saddaṃ": "звук", "gandho": "запах", "gandhaṃ": "запах", "raso": "вкус", "rasaṃ": "вкус",
    "phoṭṭhabbo": "осязаемое", "phoṭṭhabbaṃ": "осязаемое", "mano": "ум", "manaṃ": "ум",
    # family A qualifiers (6-3-10 … 6-3-12)
    "dibbacakkhu": "божественный глаз", "paññācakkhu": "глаз мудрости",
    "dibbasotaṃ": "божественное ухо", "taṇhāsotaṃ": "поток жажды",
    "sīlagandho": "запах нравственности", "samādhigandho": "запах сосредоточения", "paññāgandho": "запах мудрости",
    "attharaso": "вкус смысла", "dhammaraso": "вкус Учения", "vimuttiraso": "вкус освобождения",
    "ṭhapetvā": "кроме", "avasesā": "остальной", "avaseso": "остальной", "avasesaṃ": "остальной",
    "cakkaṃ": "круг",                               # «(Круг следует замкнуть)»
    # ^6-3-43 slip «uppajjittharūpāyatanañca» = uppajjittha rūpāyatanañca: «возникала сфера видимых форм»
    "uppajjittharūpāyatanaṃ": "возникать … сфера видимых форм",
})

# =============================================================================================== planes
# -aṃ («перерождается в …») / -e («В …: там») / -ā («умирает в …») = the plane; -ānaṃ = its beings (G2 rule)
AY_PLANES_RU = {
    "kāmāvacar": ("мир чувственных желаний", "существа мира чувственных желаний"),
    "rūpāvacar": ("мир форм", "существа мира форм"),
    "arūpāvacar": ("мир без форм", "существа мира без форм"),
    "catuvokār": ("существование с четырьмя составляющими", "существа с четырьмя составляющими"),
}
AY_PLANES = {}
for _s, (_in, _beings) in AY_PLANES_RU.items():
    for _e in ("aṃ", "e", "ā"):
        AY_PLANES[_s + _e] = _in
    AY_PLANES[_s + "ānaṃ"] = _beings

# =============================================================================================== persons
# sa-X-ka / a-X-ka (build_3-01_ru AY_HAVE): «перерождается с глазом и без уха»: the prepositional phrase is the
# word that carries sa- / a- (pi-2 asaññā = без восприятия)
AY_HAVE = {
    "sacakkhukānaṃ": "с глазом", "acakkhukānaṃ": "без глаза",
    "sasotakānaṃ": "с ухом", "asotakānaṃ": "без уха",
    "saghānakānaṃ": "с носом", "aghānakānaṃ": "без носа",
    "sarūpakānaṃ": "с видимой формой", "arūpakānaṃ": "без видимой формы",
    "sacittakānaṃ": "с умом", "acittakānaṃ": "без ума",
    "parinibbāntānaṃ": "достигать окончательного угасания",   # ^6-3-172 slip for parinibbantānaṃ
    "upapajjissati": "возникнуть",          # ^6-3-212 slip «ghānāyatanaṃ upapajjissati» = uppajjissati («не возникнет»)
    "nirujjhatī": "прекращаться",           # ^6-3-131 «na nirujjhatī ti» (separate ti)
}

# =============================================================================================== frame words
AY_FRAME = {
    "āyatanayamakaṃ": "парные вопросы о сферах восприятия",
    "suddhāyatanavāro": "раздел о сферах восприятия как таковых",
    "suddhāyatanamūlacakkavāro": "круговой раздел на основе сфер восприятия как таковых",
    # section names inside the closing notes (G2 yatthakaṃ = раздел с «где»)
    "yassa yattha": "у кого где",
    "yatthakampi": "раздел с «где»", "yatthakānaṃ": "разделы с «где»",
    "yassakampi": "раздел с «у кого»", "yassayatthakampi": "раздел с «у кого где»",
    "yassa yatthakampi": "раздел с «у кого где»", "yassa yatthake": "раздел с «у кого где»",
    "vāresu": "разделы",                    # «во всех трёх разделах»
    "pucchā": "вопросы",                    # «вопросы о прошлом / о будущем / о настоящем и прошлом»
    "vārasaṅkhepo": "разделы … сокращённо",  # ^6-3-23 «а дальше разделы даются сокращённо»
    # -pi forms (pi adds no word; «в разделе о возникновении», «и в утвердительной форме»)
    "uppādepi": "раздел о возникновении", "uppādavārepi": "раздел о возникновении",
    "nirodhepi": "раздел о прекращении", "nirodhavārepi": "раздел о прекращении",
    "nirodhavāre": "раздел о прекращении",
    "uppādanirodhepi": "раздел о возникновении и прекращении",
    "uppādanirodhavārepi": "раздел о возникновении и прекращении",
    # «и в утвердительной, и в отрицательной форме»: «форме» is shared, so anulomampi is discontinuous
    "anulomampi": "утвердительная … форма", "paccanīkampi": "отрицательная форма",
    # ^6-3-40 «в настоящем, в прошлом, …»: locative time words -> nominative, no «в» (G8 rule)
    "paccuppannepi": "настоящее", "atītepi": "прошлое", "anāgatepi": "будущее",
    "paccuppannātītepi": "настоящее и прошлое", "paccuppannānāgatepi": "настоящее и будущее",
    "atītānāgatepi": "прошлое и будущее",
    # Namo line (^6-3-254) as CORE
    "namo": CORE.get("namo", "почтение"), "bhagavato": CORE.get("bhagavato", "Благословенный"),
    "arahato": CORE.get("arahato", "Достойный"),
    "sammāsambuddhassa": CORE.get("sammāsambuddhassa", "Полностью Пробуждённый Будда"),
}

G3_TABLE = {**YM, **G2.G2_FRAME, **AY_MEMBERS, **AY_PLANES, **AY_HAVE, **AY_FRAME}

# per-segment readings {block id: {keyword exactly as listed: Russian}}
OVERRIDES = {
    "6-3-26": {"yassakasadisaṃ": "так же как в разделе с «у кого»"},   # «(сокращено, так же как в разделе с «у кого» …)»
    "6-3-131": {"yassakasadisaṃ": "такой же как раздел с «у кого»"},   # «раздел с «у кого где» тоже такой же, как …»
}


def _fold(k):
    out = [k]
    if k.endswith("ñceva"):
        out.append(k[:-5] + "ṃ")
    if k.endswith("ñca"):
        out.append(k[:-3] + "ṃ")
    if k.endswith("nti"):
        out.append(k[:-3] + "ṃ")
    if k.endswith(("oti", "āti", "īti", "ūti")):
        out.append(k[:-2])
    return out


def resolver_for(part, table=None):
    t = G3_TABLE if table is None else table
    pa, ru = G2.read_pali(part), G2.read_russian(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        v = G2.frame_value(kw, pa.get(bid, ""), ru.get(bid, ""))
        if v is not None:
            return v
        for k in _fold(lc(kw)):
            if k in t:
                return t[k]
        if lc(kw) in CORE:
            return CORE[lc(kw)]
        return value(kw, kws, t)
    return resolve


# presence-check exceptions: G2's self-checking frame-verb exceptions plus the ^6-3-212 slip
AY_EXC_RU = {**G2.FRAME_EXC_RU,
             "upapajjissati": (r"возникн(ет|ут)", "slip for uppajjissati: возникнуть ~ возникнет")}


def exceptions_for(part):
    return G2.frame_exceptions(part, exc=AY_EXC_RU)


if __name__ == "__main__":
    for p in (sys.argv[1:] or PARTS):
        build_part(p, resolver_for(p))
        verify(p, show=200, allowed=exceptions_for(p))
