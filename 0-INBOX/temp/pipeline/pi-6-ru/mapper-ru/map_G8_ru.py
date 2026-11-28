"""G8 citta: Pāli->Russian keyword map for pi-6 8-cittayamaka (frame-setter for the cittayamaka frames).

usage: python -I -X utf8 -B map_G8_ru.py        (writes 8-cittayamaka.mapped.md and verifies it)

Importing writes nothing. Later groups import the tables:
    import importlib, sys; sys.path.insert(0, r"...\\pi-6-ru\\mapper-ru"); g8 = importlib.import_module("map_G8_ru")
    g8.CITTA_TABLE (the whole table), g8.TENSE (uppajjati / nirujjhati in every tense and participle),
    g8.TIME (moments, past / future / present), g8.PERSONS, g8.MIXTURES, g8.HEADINGS, g8.base_kw(kw)

Resolution order per keyword: OVERRIDES[bid][kw] -> CITTA_TABLE (with base_kw folding -ti / -nti / -ñca / -ñceva)
-> value() of map_common_pi6_ru (YM -> pi-2 KH -> pi-1 CH2 / MATRIX).
Every segment of 8-cittayamaka was read against its Russian; the chapter is formulaic (build_8_ru.py fixed phrase
tables), so identical Pāli has identical Russian and the table covers it.
"""
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_pi6_ru import (EXCEPTIONS, NDE, YM, lc, present, read_keywords, read_russian,  # noqa: E402
                               build_part, value, verify)

PARTS = ["8-cittayamaka"]

# -- uppajjati / nirujjhati: tenses and participles (verbs infinitive in the aspect the text uses;
#    participles nominative masculine singular; pi-1 uppajjati возникать, uppajjissati возникнуть, uppannaṃ возникший;
#    pi-2 nirujjhati прекращаться, niruddhaṃ прекратившийся)
TENSE = {
    "uppajjati": "возникать",            # «возникает»
    "uppajjittha": "возникать",          # «возникал» (past of the imperfective verb)
    "uppajjissati": "возникнуть",        # «возникнет» (perfective future)
    "nirujjhati": "прекращаться",        # «прекращается»
    "nirujjhittha": "прекращаться",      # «прекращался»
    "nirujjhissati": "прекратиться",     # «прекратится»
    "uppannaṃ": "возникший",             # «является возникшим»; bare (12) «Возникшее»
    "uppajjamānaṃ": "возникающий",       # «является возникающим»; bare «Возникающее»
    "uppajjamāna": "возникающий",        # heading member «о возникающем»
    "nirujjhamānaṃ": "прекращающийся",   # «является прекращающимся»
    "niruddhaṃ": "прекратившийся",       # «является прекратившимся»; bare «Прекратившееся»
}

# -- moments and times (locative time phrases -> nominative noun phrase, no «в»; government kept)
TIME = {
    "khaṇaṃ": "момент",                                   # (14) «миновал момент …, миновал этот момент»
    "uppādakkhaṇe": "момент возникновения", "bhaṅgakkhaṇe": "момент распада",
    "uppādakkhaṇaṃ": "момент возникновения", "bhaṅgakkhaṇaṃ": "момент распада",
    "cittassa uppādakkhaṇe": "момент возникновения ума", "cittassa bhaṅgakkhaṇe": "момент распада ума",
    "pacchimacittassa uppādakkhaṇe": "момент возникновения последнего ума",
    "pacchimacittassa bhaṅgakkhaṇe": "момент распада последнего ума",
    "pacchimacittassa": "последний ум",                   # split keyword «последнего ума»
    "sarāgapacchimacittassa uppādakkhaṇe": "момент возникновения последнего ума охваченного страстью",
    "sarāgacittassa uppādakkhaṇe": "момент возникновения ума охваченного страстью",
    "pacchimakusalacittassa": "последний благой ум", "kusalacittassa": "благой ум",
    "atītaṃ": "прошлый", "anāgataṃ": "будущий", "paccuppannaṃ": "настоящий",
    "atītānāgataṃ": "прошлый и будущий",                 # «Прошлый и будущий ум»
}

# -- persons (participles / adjectives masculine singular as pi-1 avasesā = остальной; nouns plural)
PERSONS = {
    "itaresaṃ": "остальной",                                       # «У остальных»
    "nirodhasamāpannānaṃ": "вошедший в медитативное достижение прекращения",
    "asaññasattānaṃ": "существа без восприятия",                   # pi-5 «существ без восприятия»
    "cittasamaṅgīnaṃ": "обладающий умом",
    "pacchimacittasamaṅgīnaṃ": "обладающий последним умом",
}

# -- suttanta / abhidhamma mixtures (the qualified minds)
MIXTURES = {
    "sarāgaṃ": "охваченный страстью", "vītarāgaṃ": "свободный от страсти",
    "sadosaṃ": "охваченный злобой", "samohaṃ": "охваченный заблуждением",
    "saṃkhittaṃ": "сжатый", "vikkhittaṃ": "рассеянный",
    "mahaggataṃ": "возвышенный", "amahaggataṃ": "невозвышенный",
    "sauttaraṃ": "имеющий над собой высшее", "anuttaraṃ": "не имеющий над собой высшего",
    "samāhitaṃ": "сосредоточенный", "asamāhitaṃ": "несосредоточенный",
    "vimuttaṃ": "освобождённый", "avimuttaṃ": "неосвобождённый",
    "kusalaṃ cittaṃ": "благой ум", "akusalaṃ cittaṃ": "неблагой ум",
    "abyākataṃ cittaṃ": "этически неопределённый ум",
    "sampayuttaṃ": "связанный", "vedanāya": "чувство",
    "saraṇaaraṇā": "сопряжённый с борьбой и свободный от борьбы", "araṇaṃ": "свободный от борьбы",
}

# -- headings and colophons (heading phrase, label / number dropped, lower-case first letter)
HEADINGS = {
    "cittayamakaṃ": "парные вопросы об уме", "mūlayamakaṃ": "парные вопросы о корнях",
    "dhammayamakaṃ": "парные вопросы о явлениях", "yamakāni": "части",   # «Три части, …»
    "suddhacittasāmaññaṃ": "ум вообще", "suddhacittasāmañña": "ум вообще",
    "puggalavāro": "раздел о личности", "dhammavāro": "раздел о явлениях",
    "puggaladhammavāro": "раздел о личности и явлениях",
    "uppādanirodhakālasambhedavāro": "раздел о смешении времени возникновения и прекращения",
    "uppāduppannavāro": "раздел о возникновении и возникшем",
    "nirodhuppannavāro": "раздел о прекращении и возникшем",
    "uppādavāro": "раздел о возникновении", "nirodhavāro": "раздел о прекращении",
    "uppādanirodhavāro": "раздел о возникновении и прекращении",
    "nanirodhavāro": "раздел о … непрекращающемся",          # «(7) Uppajjamāna-nanirodhavāro», 2nd keyword
    "uppajjamānananirodhavāro": "раздел о возникающем и непрекращающемся",
    "uppajjamānuppannavāro": "раздел о возникающем и возникшем",
    "nirujjhamānuppannavāro": "раздел о прекращающемся и возникшем",
    "uppannuppādavāro": "раздел о возникшем и возникновении",
    "atītānāgatavāro": "раздел о прошлом и будущем",
    "uppannuppajjamānavāro": "раздел о возникшем и возникающем",
    "niruddhanirujjhamānavāro": "раздел о прекратившемся и прекращающемся",
    "atikkantakālavāro": "раздел о прошедшем времени",
    "suttantacittamissakaviseso": "особенность ума из наставлений в смешении",
    "abhidhammacittamissakaviseso": "особенность ума из Абхидхаммы в смешении",
    "cittake": "раздел",       # ^6-8-113 «(Раздел «у кого ум» …, а раздел «какой ум» …)»
}

FRAME = {
    "cittaṃ": "ум",
    "natthi": "такого нет",    # «Такого нет.» (conventions-pi6 §7; YM still says нет)
    "āmantā": "да", "no": "нет",
    NDE: NDE,                  # the keyword list itself carries «(no direct equivalent)» (^6-8-7-15-0 …)
}

CITTA_TABLE = {**YM, **FRAME, **TENSE, **TIME, **PERSONS, **MIXTURES, **HEADINGS}

# per-segment readings: {block id: {keyword exactly as listed: Russian}}
# (14) Atikkantakālavāro: «uppajjamānaṃ / nirujjhamānaṃ khaṇaṃ … vītikkantaṃ» = «миновал момент возникновения /
# прекращения» (aṭṭhakathā: uppādakkhaṇaṃ / nirodhakkhaṇaṃ); the participle is carried by the noun of «момент …».
ATK = {"uppajjamānaṃ": "возникновение", "nirujjhamānaṃ": "прекращение"}
OVERRIDES = {bid: dict(ATK) for bid in ("6-8-20", "6-8-40", "6-8-60", "6-8-83", "6-8-104")}


def base_kw(kw):
    """Lower-case first letter; fold the quotation -ti (-āti / -īti / -nti) and -ñca / -ñceva to the base form."""
    k = lc(kw)
    for end, rep in (("ñceva", "ṃ"), ("ñca", "ṃ"), ("nti", "ṃ"), ("āti", "a"), ("īti", "i")):
        if k.endswith(end) and k[: -len(end)] + rep in CITTA_TABLE:
            return k[: -len(end)] + rep
    if k.endswith("anti") and k[:-4] + "aṃ" in CITTA_TABLE:     # cittanti -> cittaṃ
        return k[:-4] + "aṃ"
    return k


def resolve(bid, kw, kws):
    ov = OVERRIDES.get(bid, {})
    if kw in ov:
        return ov[kw]
    k = base_kw(kw)
    if k in CITTA_TABLE:
        return CITTA_TABLE[k]
    return value(kw, kws, CITTA_TABLE)


def presence_exceptions(part):
    """(bid, kw) -> reason, only where present() misses a correct value (listed in the report)."""
    ru, out = read_russian(part), {}
    for bid, kws in read_keywords(part):
        for kw in kws:
            v = resolve(bid, kw, kws)
            if v == NDE or present(v, ru.get(bid, "")):
                continue
            if base_kw(kw) == "uppajjissati":
                out[(bid, kw)] = "infinitive возникнуть vs text «возникнет» (stem возникну- not matched)"
    return out


if __name__ == "__main__":
    for p in PARTS:
        build_part(p, resolve)
        verify(p, show=200, allowed=presence_exceptions(p))
