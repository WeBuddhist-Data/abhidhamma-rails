"""Shared helpers and tables for the pi-2 (Vibhaṅga) Pāli->Russian keyword maps (pi-2-ru/mapper-ru/).

Importing this module has no side effects (no file is written, nothing printed).

    import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    from map_common_pi2_ru import *

It re-uses the pi-1 tooling (pi-1-ru/mapper-ru/map_common_ru.py: present(), CORE, CH2, MATRIX, ch2_value)
unchanged and only swaps the paths to pi-2. Never edit the pi-1 module.

Main pieces
- read_keywords(part)              -> [(id, [kw, ...]), ...]   from <part>.keywords.md (this folder)
- read_russian(part) / read_pali(part) -> {id: segment text}   (segments end with ^id)
- present(value, text)             -> pi-1 presence check (regular inflection allowed)
- CORE, CH2, MATRIX, ch2_value, lc -> pi-1 tables (binding where pi-2 repeats pi-1 items)
- KH                               -> pi-2 table settled on the sample (preamble + 1-khandhavibhango)
- value(kw, kws, table)            -> KH-first default with the pi-2 context rules (see ru-map-conventions-pi2.md)
- build_part(part, resolver)       -> writes <part>.mapped.md here; resolver(id, kw, kws) returns the Russian
- verify(part)                     -> the brief's structural check + presence check + non-word / preposition check
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PI1_MAPPER = ROOT / "0-INBOX" / "temp" / "pipeline" / "pi-1-ru" / "mapper-ru"
if str(PI1_MAPPER) not in sys.path:
    sys.path.insert(0, str(PI1_MAPPER))
sys.dont_write_bytecode = True  # never write into the pi-1 folder
import map_common_ru as _pi1  # noqa: E402  (pi-1 tooling, read-only)
from map_common_ru import CH2, CORE, MATRIX, ch2_value, lc, present  # noqa: E402,F401

RU_DIR = ROOT / "AI_translation" / "russian" / "pi-2-russian-plain-zeroshot_split_chapters"
PI_DIR = ROOT / "AI_translation" / "pali" / "pi-2_split_chapters"
NDE = "(no direct equivalent)"
GAP = " … "


# ---------------------------------------------------------------------------- reading
def read_keywords(part):
    out = []
    for line in (HERE / f"{part}.keywords.md").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        bid, rest = line.split("] ", 1)
        out.append((bid[1:], [k.strip() for k in rest.split(", ")]))
    return out


def read_russian(part):
    return _pi1._segments(RU_DIR / f"{part}.md")


def read_pali(part):
    return _pi1._segments(PI_DIR / f"{part}.md")


# ---------------------------------------------------------------------------- pi-2 table (sample)
# Pāli keyword (lower-case first letter) -> Russian dictionary form. Settled on the sample; later
# parts extend it in their own script ({**KH, ...}). Values for the rūpa ekaka list follow pi-1 ^1-584.
_ORD = {"eka": "по одному", "du": "на два вида", "ti": "на три вида", "catub": "на четыре вида",
        "pañca": "на пять видов", "cha": "на шесть видов", "satta": "на семь видов",
        "aṭṭha": "на восемь видов", "nava": "на девять видов", "dasa": "на десять видов",
        "ekādasa": "на одиннадцать видов", "catuvīsati": "на двадцать четыре вида",
        "tiṃsa": "на тридцать видов", "tiṃsati": "на тридцать видов", "bahu": "на многие виды"}
FRAME = {f"{k}vidhena": "классификация" + GAP + v for k, v in _ORD.items()}
FRAME["chabbidhena"] = FRAME.pop("chavidhena")
FRAME["catubbidhena"] = FRAME.pop("catubvidhena")

# aggregates (genitive after «совокупность»)
AGG_GEN = {"rūpa": "материальной формы", "vedanā": "чувств", "saññā": "восприятия",
           "saṅkhāra": "формирующих факторов", "viññāṇa": "сознания"}
KH = {**FRAME, "vidhena": "вид"}
for _k, _g in AGG_GEN.items():
    _kk = {"rūpa": "rūpakkhandho", "vedanā": "vedanākkhandho", "saññā": "saññākkhandho",
           "saṅkhāra": "saṅkhārakkhandho", "viññāṇa": "viññāṇakkhandho"}[_k]
    KH[_kk] = f"совокупность {_g}"
    KH[f"vuccati {_kk}"] = f"называться совокупностью {_g}"
    KH[f"dasavidhena {_kk}"] = f"классификация совокупности {_g} на десять видов"
KH.update({
    # aggregates, frame
    "khandho": "совокупность", "khandhā": "совокупности", "khandhānaṃ": "совокупности",
    "khandha": "совокупность", "vibhaṅgo": "разбор", "bhājanīyaṃ": "разбор", "suttanta": "наставления",
    "abhidhamma": "Абхидхамма", "abhidhammapiṭake": "корзина Абхидхаммы",
    "vibhaṅga": "подробный разбор", "pāḷi": NDE, "vibhaṅgapāḷi": "подробный разбор",
    "pañhā": "вопрос", "pañhāpucchakaṃ": "раздел вопросов", "tikaṃ": "тройки", "dukaṃ": "пары",
    "tika": "тройки", "duka": "пары", "mūlakaṃ": "основа", "ubhato": "с обеих сторон",
    "vaḍḍhakaṃ": "наращивание", "tike": "тройка", "tikā": "тройки", "kusala": "благой",
    "vitthāro": "подробно изложенный", "niṭṭhito": "завершённый",
    "kaṇḍe": "раздел", "vibhattaṃ": "разобранный",
    "rūpa": "материальная форма", "vedanā": "чувство", "saññā": "восприятие",
    "saṅkhāra": "формирующие факторы", "viññāṇa": "сознание", "saṅkhārā": "формирующие факторы",
    "viññāṇaṃ": "сознание", "rūpaṃ": "материальная форма", "cetanā": "намерение",
    "tattha": "здесь", "yaṃ kiñci": "любой", "yā kāci": "любой", "ye keci": "любой",
    "tadekajjhaṃ": "весь вместе", "abhisaññūhitvā": "собранный воедино", "abhisaṅkhipitvā": "обобщённый",
    "vuccati": "называться", "vuccanti": "называться",
    "vuccati rūpaṃ": "называться материальной формой", "vuccati vedanā": "называться чувством",
    "vuccati saññā": "называться восприятием", "vuccati viññāṇaṃ": "называться сознанием",
    "vuccanti saṅkhārā": "называться формирующими факторами",
    "vuccati vedanā atītā": "называться прошлым чувством",
    # past / future / present strings (2-3, 2-9, 2-15, 2-21, 2-27)
    "atītaṃ": "прошлый", "atītā": "прошлый", "atīto": "прошлый",
    "anāgataṃ": "будущий", "anāgatā": "будущий", "anāgato": "будущий",
    "paccuppannaṃ": "настоящий", "paccuppannā": "настоящий", "paccuppanno": "настоящий",
    "niruddhaṃ": "прекратившийся", "niruddhā": "прекратившийся",
    "vigataṃ": "исчезнувший", "vigatā": "исчезнувший",
    "vipariṇataṃ": "изменившийся", "vipariṇatā": "изменившийся",
    "abbhatthaṅgataṃ": "полностью угасший", "abbhatthaṅgatā": "полностью угасший",
    "uppajjitvā": "после возникновения",
    "atītaṃsena": "категория прошлых", "saṅgahitaṃ": "включённый", "saṅgahitā": "включённый",
    "atītaṃsena saṅgahitaṃ": "включённый в категорию прошлых",
    "atītaṃsena saṅgahitā": "включённый в категорию прошлых",
    "jātaṃ": "рождённый", "jātā": "рождённый", "bhūtā": "элементы",
    "nibbattaṃ": "появившийся", "nibbattā": "появившийся",
    "abhinibbattaṃ": "полностью появившийся", "abhinibbattā": "полностью появившийся",
    "pātubhūtaṃ": "проявившийся", "pātubhūtā": "проявившийся",
    "uppannaṃ": "возникший", "uppannā": "возникший", "uppanno": "возникший",
    "uṭṭhitaṃ": "поднявшийся", "uṭṭhitā": "поднявшийся",
    "samuṭṭhitaṃ": "полностью поднявшийся", "samuṭṭhitā": "полностью поднявшийся",
    "mahābhūtā": "великие элементы", "upādāya": "производный",
    "upādāyarūpaṃ": "материальная форма производная",
    "rūpaṃ atītaṃ": "прошлая материальная форма", "rūpaṃ anāgataṃ": "будущая материальная форма",
    "rūpaṃ paccuppannaṃ": "настоящая материальная форма",
    "vedanā atītā": "прошлое чувство", "vedanā anāgatā": "будущее чувство",
    "vedanā paccuppannā": "настоящее чувство",
    "saññā atītā": "прошлое восприятие", "saññā anāgatā": "будущее восприятие",
    "saññā paccuppannā": "настоящее восприятие",
    "viññāṇaṃ atītaṃ": "прошлое сознание", "viññāṇaṃ anāgataṃ": "будущее сознание",
    "viññāṇaṃ paccuppannaṃ": "настоящее сознание",
    # internal / external
    "ajjhattaṃ": "внутри себя", "paccattaṃ": "собственный", "pāṭipuggalikaṃ": "индивидуальный",
    "pāṭipuggalikā": "индивидуальный", "parapuggalānaṃ": "другие личности",
    # gross / subtle, low / high, far / near
    "oḷārikaṃ": "грубый", "oḷārikā": "грубый", "sukhumaṃ": "тонкий", "sukhumā": "тонкий",
    "hīnaṃ": "низший", "hīnā": "низший", "hīno": "низший",
    "paṇītaṃ": "высший", "paṇītā": "высший", "paṇīto": "высший",
    "rūpaṃ oḷārikaṃ": "грубая материальная форма", "rūpaṃ sukhumaṃ": "тонкая материальная форма",
    "rūpaṃ hīnaṃ": "низшая материальная форма", "rūpaṃ paṇītaṃ": "высшая материальная форма",
    "vedanā oḷārikā": "грубое" + GAP + "чувство", "vedanā hīnā": "низшее" + GAP + "чувство",
    "vedanā paṇītā": "высшее" + GAP + "чувство",
    "saṅkhārā oḷārikā": "грубые" + GAP + "формирующие факторы",
    "viññāṇaṃ oḷārikaṃ": "грубое" + GAP + "сознание", "viññāṇaṃ sukhumaṃ": "тонкое" + GAP + "сознание",
    "cakkhāyatanaṃ": "сфера глаза", "phoṭṭhabbāyatanaṃ": "сфера осязаемого",
    "itthindriyaṃ": "способность женственности", "indriyaṃ": "способность", "kabaḷīkāro": "съедаемый",
    "āhāro": "пища", "āyatanaṃ": "сфера",
    "manāpaṃ": "приятный", "amanāpaṃ": "неприятный", "kantaṃ": "милый", "akantaṃ": "немилый",
    "iṭṭhaṃ": "желанный", "aniṭṭhaṃ": "нежеланный", "paribhūtaṃ": "униженный",
    "avaññātaṃ": "презренный", "uññātaṃ": "пренебрежённый", "hīḷitaṃ": "осмеянный",
    "cittīkataṃ": "уважаемый", "acittīkataṃ": "неуважаемый", "hīnamataṃ": "считающийся низшим",
    "rūpā": "видимые формы", "saddā": "звуки", "gandhā": "запахи", "rasā": "вкусы",
    "phoṭṭhabbā": "осязаемое", "upādāyupādāya": "в сравнении с",
    "daṭṭhabbaṃ": "следует рассматривать", "daṭṭhabbā": "следует рассматривать",
    "upakaṭṭhe": "поблизости", "yaṃ vā panaññampi": "а также любой другой",
    # feeling / perception qualifiers
    "sukhā": "приятный", "dukkhā": "болезненный", "adukkhamasukhā": "ни болезненный ни приятный",
    "sukhā vedanā": "приятное чувство", "dukkhā vedanā": "болезненное чувство",
    "sukhāya": "приятный", "dukkhāya": "болезненный", "adukkhamasukhāya": "ни болезненный ни приятный",
    "vedanāya": "чувство", "vedanāhi": "чувства", "sukhāya vedanāya": "приятное чувство",
    "dukkhāya vedanāya": "болезненное чувство", "dukkhāhi vedanāhi": "болезненные чувства",
    "sukhadukkhā": "приятные и болезненные", "sukhadukkhāhi": "приятные и болезненные",
    "vedanāya sampayuttā": "связанный с чувством", "vedanāya sampayutto": "связанный с чувством",
    "vedanāya sampayuttaṃ": "связанный с чувством",
    "dukkhāya vedanāya sampayuttā": "связанный с болезненным чувством",
    "dukkhāya vedanāya sampayutto": "связанный с болезненным чувством",
    "dukkhāya vedanāya sampayuttaṃ": "связанный с болезненным чувством",
    "sukhāya vedanāya sampayuttā": "связанный с приятным чувством",
    "sukhāya vedanāya sampayutto": "связанный с приятным чувством",
    "sukhāya vedanāya sampayuttaṃ": "связанный с приятным чувством",
    "samāpannassa": "войти в медитативное достижение",
    "kusalā": "благой", "kusalaṃ": "благой", "kusalo": "благой",
    "akusalā": "неблагой", "akusalaṃ": "неблагой", "akusalo": "неблагой",
    "abyākatā": "этически неопределённый", "abyākataṃ": "этически неопределённый",
    "abyākato": "этически неопределённый",
    "kusalābyākatā": "благие и этически неопределённые", "kusalākusalā": "благие и неблагие",
    "akusalābyākatāhi saññāhi": "неблагие и этически неопределённые восприятия",
    "ābyākatāhi saññāhi": "этически неопределённые восприятия",
    "ābyākatāhi vedanāhi": "этически неопределённые чувства",
    "saññāhi": "восприятия", "sampayuttāhi saññāhi": "восприятия связанные",
    "akusalā vedanā": "неблагое чувство", "kusalā vedanā": "благое чувство",
    "abyākatā vedanā": "этически неопределённое чувство",
    "akusalā saññā": "неблагое восприятие", "kusalā saññā": "благое восприятие",
    "abyākatā saññā": "этически неопределённое восприятие",
    "akusalā saṅkhārā": "неблагие формирующие факторы", "kusalā saṅkhārā": "благие формирующие факторы",
    "abyākatā saṅkhārā": "этически неопределённые формирующие факторы",
    "akusalaṃ viññāṇaṃ": "неблагое сознание", "kusalaṃ viññāṇaṃ": "благое сознание",
    "abyākataṃ viññāṇaṃ": "этически неопределённое сознание",
    "sāsavā": "подверженный влечениям", "sāsavaṃ": "подверженный влечениям", "sāsavo": "подверженный влечениям",
    "anāsavā": "свободный от влечений", "anāsavaṃ": "свободный от влечений", "anāsavo": "свободный от влечений",
    "āsavā": "влечения", "āsavaṃ": "влечение", "āsavo": "влечение", "āsava": "влечение",
    "sāsavā vedanā": "чувство подверженное влечениям", "anāsavā vedanā": "чувство свободное от влечений",
    "sāsavā saññā": "восприятие подверженное влечениям", "anāsavā saññā": "восприятие свободное от влечений",
    "sāsavā saṅkhārā": "формирующие факторы подверженные влечениям",
    "anāsavā saṅkhārā": "формирующие факторы свободные от влечений",
    "sāsavaṃ viññāṇaṃ": "сознание подверженное влечениям",
    "anāsavaṃ viññāṇaṃ": "сознание свободное от влечений",
    "sampayuttā": "связанный", "sampayutto": "связанный", "sampayuttaṃ": "связанный",
    "sampayuttā saññā": "восприятие связанное", "sampayuttā saṅkhārā": "формирующие факторы связанные",
    "sampayuttaṃ viññāṇaṃ": "сознание связанное",
    # contact-born
    "samphassajā": "рождённый контактом", "samphassa": "контакт", "samphassaṃ": "контакт",
    "phassa": "контакт", "phassasampayutto": "связанный с контактом",
    "cittasampayutto": "связанный с умом", "citta": "ум", "paccayā": "обусловленный",
    "paṭighasamphassa": "контакт соударения", "paṭighasamphassajā": "рождённый контактом соударения",
    "paṭighasamphassajā saññā": "рождённое контактом соударения восприятие",
    "adhivacanasamphassa": "контакт наименования",
    "adhivacanasamphassajā saññā": "рождённое контактом наименования восприятие",
    # classification predicates
    "hetu": "корень", "hetū": "корни", "hetuko": "имеющий корни", "hetukaṃ": "имеющий корни",
    "hetukā": "чьи корни", "sahetuko": "имеющий корни", "ahetuko": "не имеющий корней",
    "hetusampayutto": "связанный с корнями", "hetusampayuttā": "связанный с корнями",
    "hetuvippayutto": "не связанный с корнями",
    "vippayutto": "не связанный", "vippayutta": "не связанный", "vippayuttaṃ": "не связанный",
    "kāmāvacaro": "относящийся к миру чувственных желаний",
    "kāmāvacaraṃ": "относящийся к миру чувственных желаний",
    "na kāmāvacaro": "не относящийся к миру чувственных желаний",
    "rūpāvacaro": "относящийся к миру форм", "rūpāvacaraṃ": "относящийся к миру форм",
    "arūpāvacaro": "относящийся к миру без форм", "arūpāvacaraṃ": "относящийся к миру без форм",
    "āvacaro": "относящийся к миру", "āvacaraṃ": "относящийся к миру",
    "pariyāpanno": "принадлежащий к кругам существования",
    "apariyāpanno": "не принадлежащий к кругам существования",
    "apariyāpannā": "не принадлежащий к кругам существования",
    "apariyāpannaṃ": "не принадлежащий к кругам существования",
    "sukhindriyaṃ": "способность удовольствия", "sukhindriya": "способность удовольствия",
    "dukkhindriyaṃ": "способность боли", "dukkhindriya": "способность боли",
    "somanassindriyaṃ": "способность радости", "somanassindriya": "способность радости",
    "domanassindriyaṃ": "способность уныния", "domanassindriya": "способность уныния",
    "upekkhindriyaṃ": "способность невозмутимости", "upekkhindriya": "способность невозмутимости",
    "indriya": "способность", "sukhindriyasampayutto": "связанный со способностью удовольствия",
    "manodhātu": "элемент ума", "manoviññāṇa": "умственное сознание",
    "manoviññāṇadhātu": "элемент умственного сознания", "dhātu": "элемент",
    "viññāṇadhātu": "элемент" + GAP + "сознания", "mano": "ум",
    "viññāṇehi": "виды сознания",
    "cakkhuviññāṇaṃ": "зрительное сознание", "sotaviññāṇaṃ": "слуховое сознание",
    "ghānaviññāṇaṃ": "обонятельное сознание", "jivhāviññāṇaṃ": "вкусовое сознание",
    "kāyaviññāṇaṃ": "осязательное сознание", "manoviññāṇaṃ": "умственное сознание",
    "vipākadhammadhammo": "способный приносить результаты",
    "vipākadhammadhammā": "способный приносить результаты",
    "vipākadhammadhammaṃ": "способный приносить результаты",
    "saṃkiliṭṭha": "омрачённый", "saṃkiliṭṭho": "омрачённый", "saṃkiliṭṭhā": "омрачённый",
    "asaṃkiliṭṭha": "неомрачённый", "asaṃkiliṭṭho": "неомрачённый",
    "saṃkilesiko": "подверженный омрачению", "saṃkilesikaṃ": "подверженный омрачению",
    "asaṃkiliṭṭhasaṃkilesiko": "неомрачённый но подверженный омрачению",
    "asaṃkiliṭṭhaasaṃkilesiko": "неомрачённый и не подверженный омрачению",
    "vitakka": "направленная мысль", "vitakko": "направленная мысль", "avitakko": "без направленной мысли",
    "vicāro": "удержание мысли", "vicāraṃ": "удержание мысли", "savicāro": "с удержанием мысли",
    "avicāro": "без удержания мысли", "mattaṃ": "только",
    "savitakkasavicāro": "с направленной мыслью и удержанием мысли",
    "savitakkasavicāraṃ": "с направленной мыслью и удержанием мысли",
    "savitakkasavicārā": "с направленной мыслью и удержанием мысли",
    "avitakkavicāramatto": "без направленной мысли только с удержанием мысли",
    "dassanena": "видение истины", "bhāvanāya": "развитие ума",
    "pahātabbo": "устраняемый", "pahātabbaṃ": "устраняться", "pahātabba": "устраняться",
    "pahātabbahetuko": "относящийся к явлениям чьи корни устраняются",
    "ācaya": "накопление", "apacaya": "убывание", "āpacaya": "убывание",
    "ācayagāmī": "ведущий к накоплению", "apacayagāmī": "ведущий к убыванию", "gāmī": "ведущий",
    "sekkho": "относящийся к обучающимся", "asekkho": "относящийся к завершившим обучение",
    "sekkhā": "относящийся к обучающимся", "asekkhā": "относящийся к завершившим обучение",
    "sekkha": "обучающийся", "āsekkhaṃ": "завершивший обучение",
    "paritto": "ограниченный", "parittaṃ": "ограниченный", "mahaggato": "возвышенный",
    "mahaggatā": "возвышенный", "appamāṇo": "безмерный", "appamāṇā": "безмерный",
    "ārammaṇo": "объект",
    "parittārammaṇo": "с ограниченным объектом", "parittārammaṇā": "с ограниченным объектом",
    "mahaggatārammaṇo": "с возвышенным объектом", "mahaggatārammaṇā": "с возвышенным объектом",
    "appamāṇārammaṇo": "с безмерным объектом", "appamāṇārammaṇā": "с безмерным объектом",
    "majjhimo": "средний",
    "micchattaniyato": "предопределённо ведущий к ложному", "micchatta": "ложное",
    "sammatta": "правильное", "niyato": "предопределённый", "niyatā": "предопределённый",
    "aniyato": "непредопределённый", "aniyataṃ": "непредопределённый",
    "magga": "путь", "ādhipati": "находящийся под главенством",
    "ādhipatino": "находящийся под главенством",
    "uppādī": "возникнуть", "uppādino": "возникнуть",
    "atītārammaṇo": "с прошлым объектом", "atītārammaṇā": "с прошлым объектом",
    "anāgatārammaṇo": "с будущим объектом", "anāgatārammaṇā": "с будущим объектом",
    "paccuppannārammaṇo": "с настоящим объектом", "paccuppannārammaṇā": "с настоящим объектом",
    "ajjhatto": "внутренний", "ajjhattā": "внутренний", "bahiddho": "внешний", "bahiddhā": "внешний",
    "ajjhattabahiddho": "внутренний и внешний", "ajjhattabahiddhā": "внутренний и внешний",
    "ajjhattārammaṇo": "с внутренним объектом", "ajjhattārammaṇā": "с внутренним объектом",
    "bahiddhārammaṇo": "с внешним объектом", "bahiddhārammaṇā": "с внешним объектом",
    "ajjhattabahiddhārammaṇo": "с внутренним и внешним объектом",
    "ajjhattabahiddhārammaṇā": "с внутренним и внешним объектом",
    "lokiyo": "мирской", "lokiyaṃ": "мирской", "uttaro": "надмирский", "uttarā": "надмирский",
    "kenaci": "тот или иной",
    "kenaci viññeyyo": "познаваемый тем или иным видом сознания",
    "kenaci na viññeyyo": "не познаваемый тем или иным видом сознания",
    "viññeyyo": "познаваемый", "viññeyyā": "познаваться", "viññeyyaṃ": "познаваться",
    "āsavasampayutto": "связанный с влечениями", "āsavavippayutto": "не связанный с влечениями",
    "āsavavippayuttasāsavo": "не связанный с влечениями но подверженный влечениям",
    "saṃyojaniyo": "подверженный оковам", "saṃyojaniyā": "подверженный оковам",
    "saṃyojaniyaṃ": "подверженный оковам",
    "asaṃyojaniyo": "не подверженный оковам", "asaṃyojaniyā": "не подверженный оковам",
    "saṃyojanasampayutto": "связанный с оковами", "saṃyojanavippayutto": "не связанный с оковами",
    "saṃyojanavippayuttasaṃyojaniyo": "не связанный с оковами но подверженный оковам",
    "saṃyojana": "оковы", "saṃyojanaṃ": "оковы", "saṃyojanā": "оковы",
    "ganthaniyo": "подверженный узам", "ganthaniyaṃ": "подверженный узам",
    "aganthaniyo": "не подверженный узам",
    "ganthasampayutto": "связанный с узами", "ganthavippayutto": "не связанный с узами",
    "ganthavippayuttaganthaniyo": "не связанный с узами но подверженный узам",
    "gantha": "узы", "gantho": "узы", "ganthā": "узы",
    "oghaniyo": "подверженный потокам", "oghaniyaṃ": "подверженный потокам",
    "anoghaniyo": "не подверженный потокам",
    "oghasampayutto": "связанный с потоками", "oghavippayutto": "не связанный с потоками",
    "oghavippayuttaoghaniyo": "не связанный с потоками но подверженный потокам",
    "ogha": "поток", "oghā": "потоки",
    "yoganiyo": "подверженный ярмам", "yoganiyaṃ": "подверженный ярмам", "ayoganiyo": "не подверженный ярмам",
    "yogasampayutto": "связанный с ярмами", "yogavippayutto": "не связанный с ярмами",
    "yogavippayuttayoganiyo": "не связанный с ярмами но подверженный ярмам",
    "yoga": "ярмо", "yogā": "ярма",
    "nīvaraṇiyo": "подверженный помехам", "nīvaraṇiyaṃ": "подверженный помехам",
    "anīvaraṇiyo": "не подверженный помехам", "nīvaraṇa": "помеха", "nīvaraṇaṃ": "помеха",
    "nīvaraṇā": "помехи",
    "parāmaṭṭho": "затронутый искажениями", "parāmaṭṭhaṃ": "затронутый искажениями",
    "parāmāsavippayutto": "не связанный с искажениями", "parāmāsa": "искажение",
    "parāmāso": "искажение", "parāmāsā": "искажения",
    "upādāniyo": "служащий объектом цепляния", "upādāniyaṃ": "служащий объектом цепляния",
    "upādānasampayutto": "связанный с цепляниями", "upādānasampayuttā": "связанный с цепляниями",
    "upādānavippayutto": "не связанный с цепляниями", "upādāna": "цепляние", "upādānā": "цепляния",
    "kilesa": "омрачение", "kilesā": "омрачения",
    "kilesasampayutto": "связанный с омрачениями", "kilesavippayutto": "не связанный с омрачениями",
    "sahagato": "сопровождаемый", "sahagatā": "сопровождаемый", "sahagataṃ": "сопровождаемый",
    "pītisahagato": "сопровождаемый восторгом", "na pītisahagato": "не сопровождаемый восторгом",
    "sukhasahagato": "сопровождаемый счастьем", "sukhasahagatā": "сопровождаемый счастьем",
    "upekkhāsahagato": "сопровождаемый невозмутимостью",
    "upekkhāsahagatā": "сопровождаемый невозмутимостью",
    "pīti": "восторг", "sukha": "счастье", "dukkha": "болезненный", "upekkhā": "невозмутимость",
    "niyyāniko": "ведущий к освобождению", "sauttaro": "имеющий над собой высшее",
    "sauttarā": "имеющий над собой высшее", "anuttarā": "не имеющий над собой высшего",
    "saraṇo": "сопряжённый с борьбой", "saraṇā": "сопряжённый с борьбой",
    "araṇo": "свободный от борьбы", "araṇā": "свободный от борьбы",
    # rūpa (2-33; pi-1 ^1-584 and the rūpa matrix)
    "jarābhibhūtaṃ": "подвластный старению", "ābhibhūtaṃ": "подвластный",
    "pathavī": "земля", "pathavīdhātu": "элемент земли", "āpo": "вода", "āpodhātu": "элемент воды",
    "tejo": "огонь", "tejodhātu": "элемент огня", "vāyo": "ветер", "vāyodhātu": "элемент ветра",
    "ānuparivatti": "следующий за", "ānuparivattino": "следующий за",
    "sahabhu": "сосуществующий", "sahabhuno": "сосуществующий", "saha": NDE,
    "viññatti": "внешнее выражение", "upādā": "производный",
    "rūpaṃ upādā": "материальная форма производная",
    "rūpaṃ cittasamuṭṭhānaṃ": "материальная форма порождённая умом", "samuṭṭhānaṃ": "порождённый",
    "samuṭṭhānā": "порождённый",
    "viññeyyaṃ rūpaṃ": "материальная форма познаваемая",
    "cakkhuviññeyyaṃ": "познаваемый глазом", "sotaviññeyyaṃ": "познаваемый ухом",
    "ghānaviññeyyaṃ": "познаваемый носом", "jivhāviññeyyaṃ": "познаваемый языком",
    "kāyaviññeyyaṃ": "познаваемый телом",
    "cakkhundriyaṃ": "способность глаза", "sotindriyaṃ": "способность уха",
    "ghānindriyaṃ": "способность носа", "jivhindriyaṃ": "способность языка",
    "kāyindriyaṃ": "способность тела", "purisindriyaṃ": "способность мужественности",
    "jīvitindriyaṃ": "жизненная способность",
    "sotāyatanaṃ": "сфера уха", "ghānāyatanaṃ": "сфера носа", "jivhāyatanaṃ": "сфера языка",
    "kāyāyatanaṃ": "сфера тела", "rūpāyatanaṃ": "сфера видимых форм", "saddāyatanaṃ": "сфера звуков",
    "gandhāyatanaṃ": "сфера запахов", "rasāyatanaṃ": "сфера вкусов",
    "dhammāyatana": "сфера объектов ума",
    "sanidassanaṃ": "видимый", "sanidassano": "видимый", "sanidassana": "видимый",
    "anidassanaṃ": "невидимый", "anidassanā": "невидимый", "anidassana": "невидимый",
    "anidassanasappaṭigho": "невидимый но способный к соударению",
    "sappaṭighaṃ": "способный к соударению", "sappaṭigho": "способный к соударению",
    "sappaccayaṃ": "иметь условия", "saṅkhataṃ": "обусловленный", "saṅkhatā": "обусловленный",
    "anārammaṇaṃ": "не имеющий объекта", "anārammaṇo": "не имеющий объекта",
    "sārammaṇā": "имеющий объект",
    "acetasikaṃ": "не сопутствующий уму", "cetasikā": "сопутствующий уму",
    "aniccaṃ": "непостоянный", "ajjhattikaṃ": "относящийся к внутреннему",
    "ajjhattiko": "относящийся к внутреннему", "bāhiraṃ": "относящийся к внешнему",
    "bāhirā": "относящийся к внешнему",
    "sutaṃ": "услышанный", "mutaṃ": "ощущённый", "viññātaṃ": "познанный",
    "pītisahagataṃ": "сопровождаться восторгом", "sukhasahagataṃ": "сопровождаться счастьем",
    "upekkhāsahagataṃ": "сопровождаться невозмутимостью",
    # pañhāpucchaka (2-152, 2-153)
    "na": "не", "siyā": "иногда", "khandhā siyā": "совокупности" + GAP + "иногда",
    "vattabbo": "определить", "vattabbā": "определить",
    "cittaṃ": "ум", "saṃsaṭṭhā": "соединённый", "cittasaṃsaṭṭhā": "соединённый с умом",
    "khandhā cittasaṃsaṭṭhā": "совокупности соединённые с умом",
    "cittasampayuttā": "связанный с умом", "arūpā": "нематериальный",
    "rūpakkhandho hetuvippayutto": "совокупность материальной формы" + GAP + "не связанный с корнями",
    "hetu ceva hetusampayutto": "являющийся корнем и связанный с корнями",
    "hetū ceva hetusampayuttā": "являющийся корнями и связанный с корнями",
    "āsavo ceva āsavasampayutto": "являющийся влечением и связанный с влечениями",
    "āsavā ceva āsavasampayuttā": "являющийся влечениями и связанный с влечениями",
    "saṃyojanañceva saṃyojanasampayutto": "являющийся оковами и связанный с оковами",
    "saṃyojanā ceva saṃyojanasampayuttā": "являющийся оковами и связанный с оковами",
    "gantho ceva ganthasampayutto": "являющийся узами и связанный с узами",
    "ganthā ceva ganthasampayuttā": "являющийся узами и связанный с узами",
    "nīvaraṇañceva nīvaraṇasampayutto": "являющийся помехой и связанный с помехами",
    "nīvaraṇā ceva nīvaraṇasampayuttā": "являющийся помехами и связанный с помехами",
    "upādānā ceva upādānasampayuttā": "являющийся цепляниями и связанный с цепляниями",
    "kileso ceva kilesasampayutto": "являющийся омрачением и связанный с омрачениями",
    "kilesā ceva kilesasampayuttā": "являющийся омрачениями и связанный с омрачениями",
    "cakkhusamphassajā cetanā": "рождённое контактом глаза намерение",
    "cakkhusamphassajā saññā": "рождённое контактом глаза восприятие",
    "cakkhusamphassajā vedanā": "рождённое контактом глаза чувство",
})
for _p, _r in {"cakkhu": "глаза", "sota": "уха", "ghāna": "носа", "jivhā": "языка", "kāya": "тела",
               "mano": "ума"}.items():
    KH[f"{_p}samphassa"] = f"контакт {_r}"
    KH[f"{_p}samphassajā"] = f"рождённый контактом {_r}"


def hetuko_value(pali):
    """hetuko is a fragment: sa-/ahetuko «имеющий корни» (preferred), else pahātabbahetuko «чьи корни»,
    else maggahetuko «имеющий корнем» (pi-1 1-M1-16). pali = the segment's Pāli text."""
    words = set(re.findall(r"\w+", pali))
    if any(w.endswith(("sahetuko", "ahetuko")) and not w.endswith(("bbahetuko", "ggahetuko")) for w in words):
        return "имеющий корни"
    if any(w.endswith("pahātabbahetuko") for w in words):
        return "чьи корни"
    return "имеющий корнем"


# presence-check exceptions by keyword (value correct; inflection outside present()'s tolerance)
EXCEPTIONS = {
    "tadekajjhaṃ": "весь ~ вся / всё / все (suppletive pronoun)",
    "samāpannassa": "войти ~ вошёл (suppletive past stem), = pi-1 value",
    "kenaci": "тот или иной ~ тем или иным (pronoun declension)",
    "vāyo": "ветер ~ ветра (fleeting vowel before р)",
    "tejo": "огонь ~ огня (fleeting vowel)",
    "tika": "тройки ~ троек (fleeting vowel after й)",
    "viññeyyā": "познаваться ~ познаются (stem alternation), = pi-1 ^1-584 viññeyyaṃ",
}


def allowed_for(part, exceptions=None):
    exc = EXCEPTIONS if exceptions is None else exceptions
    return {(bid, kw): exc[lc(kw)] for bid, kws in read_keywords(part) for kw in kws if lc(kw) in exc}


def value(kw, kws, table=None):
    """Default: the given table (or KH), then the pi-1 CH2 / MATRIX tables."""
    k = lc(kw)
    t = KH if table is None else table
    if k in t:
        return t[k]
    if k in CH2:
        return ch2_value(kw, kws, CH2)
    return MATRIX[k]


# ---------------------------------------------------------------------------- build and verify
PREPOSITIONS = {"в", "во", "с", "со", "к", "ко", "о", "об", "по", "на", "за", "от", "из", "до", "без",
                "над", "под", "при", "для", "у", "через", "про"}


def build_part(part, resolver):
    """resolver(bid, kw, kws) -> Russian value. Stops on an unmapped keyword or ", " in a value."""
    lines, missing = [], []
    for bid, kws in read_keywords(part):
        pairs = []
        for kw in kws:
            try:
                v = resolver(bid, kw, kws)
            except KeyError:
                missing.append((bid, kw))
                v = "???"
            assert ", " not in v, (bid, kw, v)
            pairs.append(f"{kw}={v}")
        lines.append(f"[{bid}] " + ", ".join(pairs))
    if missing:
        raise SystemExit(f"{part}: unmapped keywords: {sorted(set(k for _, k in missing))}")
    (HERE / f"{part}.mapped.md").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return len(lines)


def verify(part, show=60, allowed=None):
    """allowed: {(bid, kw): reason} presence-check exceptions (listed in the report)."""
    allowed = allowed or {}
    a = [l.split("] ", 1) for l in (HERE / f"{part}.keywords.md").read_text(encoding="utf-8").splitlines()]
    b = [l.split("] ", 1) for l in (HERE / f"{part}.mapped.md").read_text(encoding="utf-8").splitlines()]
    assert [x[0] for x in a] == [x[0] for x in b]
    bad = [i for (i, x), (_, y) in zip(a, b)
           if [k.strip() for k in x.split(", ")] != [k.split("=", 1)[0] for k in y.split(", ")]]
    ru = read_russian(part)
    nde, miss, exc, prep = 0, [], [], []
    for bid, rest in b:
        bid = bid[1:]
        text = ru.get(bid)
        for pair in rest.split(", "):
            kw, v = pair.split("=", 1)
            if v == NDE:
                nde += 1
                continue
            if v.strip().lower() in PREPOSITIONS:
                prep.append((bid, kw, v))
            if (bid, kw) in allowed:
                exc.append((bid, kw, v, allowed[(bid, kw)]))
            elif text is None or not present(v, text):
                miss.append((bid, kw, v))
    print(part, "lines", len(a), "bad", bad, "| no-direct-equivalent", nde, "| presence misses", len(miss),
          "| listed exceptions", len(exc), "| bare prepositions", len(prep))
    for m in miss[:show]:
        print("   MISS", *m)
    for p in prep:
        print("   PREP", *p)
    return bad, nde, miss, exc
