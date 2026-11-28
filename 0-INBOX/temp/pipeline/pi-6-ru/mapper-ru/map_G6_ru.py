"""G6 saṅkhāra: Pāli->Russian keyword maps for pi-6 6-01-sankharayamaka and 6-02-sankharayamaka.

usage:  python -I -X utf8 -B map_G6_ru.py          (writes the two <part>.mapped.md and verifies them)
import: importing writes nothing. Later groups:

    import importlib, sys; sys.path.insert(0, r"...\\pi-6-ru\\mapper-ru"); G6 = importlib.import_module("map_G6_ru")
    G6.G6_TABLE        whole table (YM + G2_FRAME + G8 TIME / PERSONS + G6 values)
    G6.SK_MEMBERS      the three saṅkhāras, kāya / vacī / citta, breath and thought words (chapter-specific)
    G6.SK_FRAME        jhāna persons / places, planes in -e / -aṃ / -ānaṃ, the «yassa cittassa anantarā» frame,
                       avitakka / savitakka moments and levels, note words (yassakampi … pucchā, -vārepi)

Imports (not retyped): map_G2_ru G2_FRAME / frame_value() / frame_exceptions() / _fold_ti (pavatti and pariññā
verbs, answers, planes, persons, vāra headings); map_G8_ru TIME and PERSONS (moments, last mind, nirodhasamāpanna,
asaññasatta). G2_KHANDHA is NOT imported.
Resolution per keyword: OVERRIDES[bid][kw] -> CORE for the Namo line -> G2.frame_value() (denied negative, pariññā
word order, pacchimabhavika) -> G6_TABLE (-ti / -ñca / -ñceva folded) -> value() (pi-2 KH, pi-1 CH2 / MATRIX).
See notes-map-G6.md.
"""
import importlib
import pathlib
import re
import sys

sys.dont_write_bytecode = True
_HERE = pathlib.Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))
from map_common_pi6_ru import (CORE, NDE, YM, build_part, lc, present, read_russian,  # noqa: E402
                               value, verify)

G2 = importlib.import_module("map_G2_ru")
G8 = importlib.import_module("map_G8_ru")

PARTS = ["6-01-sankharayamaka", "6-02-sankharayamaka"]

# =============================================================================================== members
# notes-6-01 (pi-2 ^2-226): телесный / речевой формирующий фактор, формирующий фактор ума; saṅkhāra pi-2 / G2
SK_MEMBERS = {
    "saṅkhārayamakaṃ": "парные вопросы о формирующих факторах",
    "saṅkhārayamake": "парные вопросы о формирующих факторах",        # «в парных вопросах о формирующих факторах»
    "saṅkhārayamakepi": "парные вопросы о формирующих факторах",
    "khandhayamake": "парные вопросы о совокупностях",                # «в парных вопросах о совокупностях»
    "suddhasaṅkhāravāro": "раздел о формирующих факторах как таковых",
    "kāyasaṅkhāro": "телесный формирующий фактор", "kāyasaṅkhāraṃ": "телесный формирующий фактор",
    "vacīsaṅkhāro": "речевой формирующий фактор", "vacīsaṅkhāraṃ": "речевой формирующий фактор",
    "cittasaṅkhāro": "формирующий фактор ума", "cittasaṅkhāraṃ": "формирующий фактор ума",
    "saṅkhāro": "формирующий фактор", "saṅkhāraṃ": "формирующий фактор",   # «является и формирующим фактором»
    "saṅkhārā": "формирующие факторы",                                 # «Три формирующих фактора», «Остальные …»
    "kāyo": "тело", "kāyaṃ": "тело",                                   # Kāyañca -> kāyaṃ
    "vacī": "речь", "vaciṃ": "речь",                                   # Vaciñca -> vaciṃ
    "cittaṃ": "ум", "citte": "ум",                                     # «когда присутствует второй ум»
    "cittassa": "ум",                                                  # «сразу после данного ума»
    "assāsapassāsā": "вдохи и выдохи", "assāsapassāsānaṃ": "вдохи и выдохи",
    "assāsapassāsehi": "вдохи и выдохи",                              # vinā … «без вдохов и выдохов»
    "vitakkavicārā": "направленная мысль и удержание мысли", "vitakkavicāre": "направленная мысль и удержание мысли",
    "vitakkavicārehi": "направленная мысль и удержание мысли",
    "vitakkavicārānaṃ": "направленная мысль и удержание мысли",       # pi-2
    "saññā": "восприятие", "vedanā": "чувство",
    "cittasampayuttakā": "связанный с умом",                           # «все явления, связанные с умом» (pi-1)
    "ṭhapetvā": "кроме", "avasesā": "остальной",
}

# =============================================================================================== pavatti frame
_NO_VT = "без направленной мысли и без удержания мысли"
_WITH_VT = "с направленной мыслью и удержанием мысли"
SK_FRAME = {
    # persons and places (jhāna as place: «В четвёртом медитативном погружении»; person: «вошедших в …»)
    "samāpannānaṃ": "вошедший",                                        # pi-5 samāpanna = вошедший
    "catutthajjhāne": "четвёртое медитативное погружение",
    "catutthajjhānaṃ": "четвёртое медитативное погружение",
    # planes: -e / -aṃ = the plane, -ānaṃ = its beings (coordinator rule; pi-1 kāmāvacare)
    "kāmāvacare": "мир чувственных желаний", "kāmāvacaraṃ": "мир чувственных желаний",
    "rūpāvacare": "мир форм", "rūpāvacaraṃ": "мир форм",
    "arūpāvacare": "мир без форм", "arūpāvacaraṃ": "мир без форм",
    "kāmāvacarānaṃ": "существа мира чувственных желаний",
    "rūpāvacarānaṃ": "существа мира форм", "arūpāvacarānaṃ": "существа мира без форм",
    # «у существ Чистых обителей, когда присутствует второй ум»
    "vattamāne": "присутствовать",                                     # pi-5
    # «у которых сразу после данного ума возникнет последний ум»
    "anantarā": "сразу после",                                         # pi-5
    "pacchimacittaṃ": "последний ум",
    "tesaṃyeva": "они же",                                             # «у них же» (presence exception)
    # with / without vitakka-vicāra (pi-1 avitakkaavicāra, savitakkasavicāra)
    "avitakkaavicāraṃ": _NO_VT,                                        # «последний ум без …»
    "avitakkaavicārapacchimacittassa": "последний ум " + _NO_VT,
    "savitakkasavicārapacchimacittassa": "последний ум " + _WITH_VT,
    "avitakkaavicārapacchimacittasamaṅgīnaṃ": "обладающий последним умом " + _NO_VT,
    "avitakkaavicāracittassa uppādakkhaṇe": "момент возникновения ума " + _NO_VT,
    "avitakkaavicāracittassa bhaṅgakkhaṇe": "момент распада ума " + _NO_VT,
    "savitakkasavicārapacchimacittassa uppādakkhaṇe": "момент возникновения последнего ума " + _WITH_VT,
    "savitakkasavicārapacchimacittassa bhaṅgakkhaṇe": "момент распада последнего ума " + _WITH_VT,
    "avitakkaavicārapacchimacittassa bhaṅgakkhaṇe": "момент распада последнего ума " + _NO_VT,
    "savitakkasavicārabhūmiyaṃ": "уровень " + _WITH_VT,                # «на уровне с …» (pi-1 bhūmi = уровень)
    "avitakkaavicārabhūmiyaṃ": "уровень " + _NO_VT,
    # abbreviation notes («(И раздел с «у кого», и раздел с «у кого где» одинаковы.)»; G2 yatthakaṃ)
    "yassa yattha": "у кого где",                                      # «У кого где возникает …»
    "yassakampi": "раздел с «у кого»",
    "yassayatthakampi": "раздел с «у кого где»", "yassayatthake": "раздел с «у кого где»",
    "yatthakampi": "раздел с «где»",
    "yatthakānaṃ": "разделы с «где»",                                  # «остальные разделы с «где»» (plural)
    "pucchā": "вопросы",                                               # «разобраны вопросы о прошлом»
    "uppādavāre": "раздел о возникновении", "uppādavārepi": "раздел о возникновении",
    "nirodhavāre": "раздел о прекращении", "nirodhavārepi": "раздел о прекращении",
    "nirodhavārena": "раздел о прекращении",                           # «одинаково с разделом о прекращении»
    "uppādanirodhavārepi": "раздел о возникновении и прекращении",
    "uppādavāranirodhavārepi": "раздел о возникновении и прекращении",  # ^6-6-147 (notes-6-02: read as meant)
    # «и в утвердительной, и в отрицательной форме»: the noun is shared, so anulomampi is discontinuous (pi-1 " … ")
    "anulomampi": "утвердительная … форма", "paccanīkampi": "отрицательная форма",
    "paccanīkaokāsā": "отрицательная форма по месту",                 # ^6-6-16-5-0 slip for paccanīkaokāso
    "paccuppannavārādi": "раздел о настоящем и другие",
    "pariññāvāraṃ": "раздел о полном понимании",
}

G6_TABLE = {**YM, **G2.G2_FRAME, **G8.TIME, **G8.PERSONS, **SK_MEMBERS, **SK_FRAME}

# the Namo line (^6-6-159): CORE values (Почтение Благословенному, Достойному, Полностью Пробуждённому Будде)
CORE_FIRST = {"namo", "bhagavato", "arahato", "sammāsambuddhassa"}

# per-segment readings {block id: {keyword exactly as listed: Russian}} (none needed: the chapter is formulaic)
OVERRIDES = {}


def resolver_for(part, table=None):
    t = G6_TABLE if table is None else table
    pa, ru = G2.read_pali(part), read_russian(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        k = lc(kw)
        if k in CORE_FIRST:
            return CORE[k]
        v = G2.frame_value(kw, pa.get(bid, ""), ru.get(bid, ""))
        if v is not None:
            return v
        for f in G2._fold_ti(k):
            if f in t:
                return t[f]
        return value(kw, kws, t)
    return resolve


# =============================================================================================== presence exceptions
# Own self-checking exceptions: accepted only if the stated Russian form is in the segment.
G6_EXC_RU = {
    "tesaṃyeva": (r"у них же", "они же ~ «у них же» (pronoun in the genitive after «у»)"),
    # fleeting «е» of уровень ~ «на уровне» is outside present()'s tolerance
    "savitakkasavicārabhūmiyaṃ": (r"на уровне с направленной мыслью и удержанием мысли", "уровень ~ «на уровне»"),
    "avitakkaavicārabhūmiyaṃ": (r"на уровне без направленной мысли и без удержания мысли", "уровень ~ «на уровне»"),
}


def exceptions_for(part):
    allowed = dict(G2.frame_exceptions(part))
    ru = read_russian(part)
    for line in (_HERE / f"{part}.mapped.md").read_text(encoding="utf-8").splitlines():
        bid, rest = line.split("] ", 1)
        bid = bid[1:]
        text = ru.get(bid, "")
        for pair in rest.split(", "):
            kw, v = pair.split("=", 1)
            k = lc(kw)
            if v == NDE or present(v, text) or (bid, kw) in allowed:
                continue
            if k in G6_EXC_RU and re.search(G6_EXC_RU[k][0], text.lower()):
                allowed[(bid, kw)] = G6_EXC_RU[k][1]
    return allowed


if __name__ == "__main__":
    for p in (sys.argv[1:] or PARTS):
        build_part(p, resolver_for(p))
        verify(p, show=200, allowed=exceptions_for(p))
