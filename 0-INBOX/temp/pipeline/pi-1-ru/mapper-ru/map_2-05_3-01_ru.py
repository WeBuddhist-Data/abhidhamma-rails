"""Pāli->Russian keyword maps for pi-1 parts 2-05-cittuppadakandam and 3-01-rupakandam.

usage: python -I -X utf8 map_2-05_3-01_ru.py      (writes the two <part>.mapped.md and verifies them)

Resolution order per keyword:
  2-05: OVERRIDES[bid][kw] -> context rules (rule_205) -> T205 (extends CH2) -> ch2_value
  3-01: OVERRIDES[bid][kw] -> «-meva» rule -> T301 (own table; CH2/MATRIX are not used blindly)
Conventions: ru-map-conventions.md; new decisions: notes-map-2-05_3-01.md.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_ru import CH2, GAP, NDE, build_part, ch2_value, lc, present, read_russian, verify  # noqa: E402

PARTS = ["2-05-cittuppadakandam", "3-01-rupakandam"]

# ============================================================================ 2-05
T205 = {
    # headings
    "lokuttara": "надмирский", "magga": "путь",
    "suddhika": "простой", "suddhikapaṭipadā": "простой способ практики", "paṭipadā": "способ практики",
    "suññata": "пустота", "suññatā": "пустота", "appaṇihita": "свобода от устремлений",
    "suddhikaappaṇihitaṃ": "простое свободное от устремлений",
    "nayā": "методы", "vīsati": "двадцать",
    "chanda": "желание", "adhipateyya": "преобладание", "adhipateyyaṃ": "преобладание",
    "adhipateyyanti": "преобладание", "vīmaṃsā": "пытливость",
    "abyākataṃ": "этически неопределённый", "akusala": "неблагой",
    "vipākaabyākataṃ": "этически неопределённое являющееся результатом",
    "vipāka": "результат", "vipākā": "результат", "viññāṇāni": "виды сознания",
    "vipākapañcaviññāṇāni": "пять видов сознания являющихся результатом",
    "manodhātu": "элемент ума", "vipākamanodhātu": "элемент ума являющийся результатом",
    "vipākā manodhātu": "элемент ума являющийся результатом",
    "vipākamanoviññāṇadhātu": "элемент умственного сознания являющийся результатом",
    "vipākā manoviññāṇadhātu": "элемент умственного сознания являющийся результатом",
    "vipākā abyākatā": "этически неопределённые результаты действий",
    "kiriyā": "функциональный", "kiriyaṃ": "функциональный",
    "kiriyāabyākataṃ": "этически неопределённое функциональное",
    "kiriyā abyākatā": "этически неопределённое функциональное",
    "hetuka": "корень", "hetukā": "корень",
    "kiriyāmanodhātu": "функциональный элемент ума", "kiriyā manodhātu": "функциональный элемент ума",
    "kiriyāmanoviññāṇa": "функциональный … умственное сознание",
    "kiriyā manoviññāṇa": "функциональный … умственное сознание",
    "kiriyāmanoviññāṇadhātu": "функциональный элемент умственного сознания",
    "kiriyā manoviññāṇadhātu": "функциональный элемент умственного сознания",
    "sahagatā": "сопровождаемый", "somanassasahagatā": "сопровождаемый радостью",
    "upekkhāsahagatā": "сопровождаемый невозмутимостью",
    "dhātusomanassasahagatā": "элемент … сопровождаемый радостью",
    "dhātu somanassasahagatā": "элемент … сопровождаемый радостью",
    "dhātuupekkhāsahagatā": "элемент … сопровождаемый невозмутимостью",
    "dhātu upekkhāsahagatā": "элемент … сопровождаемый невозмутимостью",
    "manoviññāṇadhātusomanassasahagatā": "элемент умственного сознания сопровождаемый радостью",
    "manoviññāṇadhātu somanassasahagatā": "элемент умственного сознания сопровождаемый радостью",
    "manoviññāṇadhātuupekkhāsahagatā": "элемент умственного сознания сопровождаемый невозмутимостью",
    "manoviññāṇadhātu upekkhāsahagatā": "элемент умственного сознания сопровождаемый невозмутимостью",
    "arūpa": "без форм", "arūpāvacara": "относящийся к миру без форм",
    "arūpāvacaraṃ": "относящийся к миру без форм",
    "rūpāvacara": "относящийся к миру форм", "rūpāvacaraṃ": "относящийся к миру форм",
    "mano": "ум",                                     # manodhātu «элемент ума», manindriyaṃ «способность ума»
    # world-transcending frame (^1-505 … ^1-553)
    "abyākatā": "этически неопределённый", "dhammā abyākatā": "этически неопределённые явления",
    "lokuttaraṃ": "надмирский", "jhānaṃ": "медитативное погружение",
    "lokuttaraṃ jhānaṃ": "надмирское медитативное погружение",
    "bhāveti": "развивать", "lokuttaraṃ jhānaṃ bhāveti": "развивать надмирское медитативное погружение",
    "jhānaṃ bhāveti": "развивать медитативное погружение",
    "niyyānikaṃ": "ведущий к освобождению", "gāmiṃ": "ведущий", "apacaya": "убывание",
    "caya": NDE,                                      # only «убыванию»: no word for the member caya
    "niyyānikaṃ apacayagāmiṃ": "ведущий к освобождению и ведущий к убыванию",
    "diṭṭhigatānaṃ": "приверженность воззрениям", "pahānāya": "устранение",
    "diṭṭhigatānaṃ pahānāya": "устранение приверженности воззрениям",
    "bhūmiyā": "ступень", "pattiyā": "достижение",
    "eva": "полностью",                               # vivicc'eva = «полностью уединившись»
    "vivicca": "уединиться", "kāmehi": "чувственные удовольствия",
    "vivicceva kāmehi": "полностью уединиться от чувственных удовольствий",
    "upasampajja": "входить", "viharati": "пребывать",
    "upasampajja viharati": "входить в … и пребывать в нём",
    "dukkha": "трудный", "dukkhapaṭipadaṃ": "трудный способ практики",
    "sukha": "лёгкий", "sukhapaṭipadaṃ": "лёгкий способ практики", "paṭipadaṃ": "способ практики",
    "paṭipadaṃ dandha": "способ практики и медленный", "paṭipadaṃ khippa": "способ практики и быстрый",
    "dandha": "медленный", "khippa": "быстрый",
    "abhiññaṃ": "высшее знание", "abhiññanti": "высшее знание",
    "dandhābhiññaṃ": "медленное высшее знание", "dandhābhiññanti": "медленное высшее знание",
    "khippābhiññaṃ": "быстрое высшее знание",
    "suññataṃ": "пустой", "suññatanti": "пустой",
    "animittaṃ": "не имеющий признаков", "animittanti": "не имеющий признаков",
    "appaṇihitaṃ": "свободный от устремлений", "appaṇihitanti": "свободный от устремлений",
    "vitakka": "направленная мысль", "vicārānaṃ": "удержание мысли", "vūpasamā": "затихание",
    "catutthaṃ jhānaṃ": "четвёртое медитативное погружение",
    "kusalassa jhānassa": "благое медитативное погружение",
    "lokuttarassa kusalassa": "надмирский благой",
    "lokuttarassa kusalassa jhānassa": "надмирское благое медитативное погружение",
    "katattā": "совершённый", "bhāvitattā": "развитый", "upacitattā": "накопленный",
    "aññindriyaṃ": "способность окончательного знания", "aññā": "окончательное знание",
    "aññātāvī": "обладатель окончательного знания",
    # twenty great methods (^1-528, ^1-552)
    "maggaṃ": "путь", "sati": "осознанность", "paṭṭhānaṃ": "основа", "padhānaṃ": "усилие",
    "iddhi": "сверхспособность", "bojjhaṅgaṃ": "фактор пробуждения", "saccaṃ": "истина",
    "samathaṃ": "успокоение", "khandhaṃ": "совокупность", "āyatanaṃ": "сфера восприятия",
    "dhātuṃ": "элемент", "āhāraṃ": "питание", "phassaṃ": "контакт", "vedanaṃ": "чувство",
    "saññaṃ": "восприятие", "cetanaṃ": "намерение",
    "lokuttaraṃ maggaṃ": "надмирский путь",
    "lokuttaraṃ satipaṭṭhānaṃ": "надмирская основа осознанности",
    "lokuttaraṃ satipaṭṭhānaṃ bhāveti": "развивать надмирскую основу осознанности",
    "lokuttaraṃ iddhipādaṃ": "надмирская основа сверхспособностей",
    "lokuttaraṃ indriyaṃ": "надмирская способность", "lokuttaraṃ balaṃ": "надмирская сила",
    "lokuttaraṃ bojjhaṅgaṃ": "надмирский фактор пробуждения", "lokuttaraṃ saccaṃ": "надмирская истина",
    "lokuttaraṃ samathaṃ": "надмирское успокоение", "lokuttaraṃ dhammaṃ": "надмирское явление",
    "lokuttaraṃ khandhaṃ": "надмирская совокупность",
    "lokuttaraṃ āyatanaṃ": "надмирская сфера восприятия", "lokuttaraṃ dhātuṃ": "надмирский элемент",
    "lokuttaraṃ āhāraṃ": "надмирское питание", "lokuttaraṃ phassaṃ": "надмирский контакт",
    "lokuttaraṃ vedanaṃ": "надмирское чувство", "lokuttaraṃ saññaṃ": "надмирское восприятие",
    "lokuttaraṃ cetanaṃ": "надмирское намерение", "lokuttaraṃ cittaṃ": "надмирский ум",
    # further paths (^1-553)
    "kāmarāga": "чувственная страсть", "rāga": "страсть", "byāpādānaṃ": "недоброжелательность",
    "tanubhāvāya": "ослабление", "avasesa": NDE,       # an-avasesa = «полного»: no word of its own
    "māna": "самомнение", "uddhacca": "беспокойство", "avijjāya": "неведение",
    # ^1-555
    "sambojjhaṅgo": "фактор пробуждения", "vicayasambojjhaṅgo": "фактор пробуждения исследования",
    "maggaṅgaṃ": "фактор пути",
    # unwholesome results (^1-556 …)
    "akusalassa": "неблагой", "akusalassa kammassa": "неблагое действие",
    "cakkhuviññāṇaṃ": "зрительное сознание", "sotaviññāṇaṃ": "слуховое сознание",
    "ghānaviññāṇaṃ": "обонятельное сознание", "jivhāviññāṇaṃ": "вкусовое сознание",
    "kāyaviññāṇaṃ": "осязательное сознание", "dukkhindriyaṃ": "способность боли",
    "kāyikaṃ": "телесный", "kāyaviññāṇa": "осязательное сознание",
    "kāyaviññāṇadhātu": "элемент осязательного сознания", "kāyasamphassa": "контакт тела",
    "kāyasamphassajaṃ": "рождённый контактом тела", "samphassa": "контакт",
    "dukkhaṃ": "боль", "dukkhā vedanā": "болезненное чувство",
    "uppannā": "возникать", "dhātu uppannā": "возникать элемент",
    "ārammaṇā": "объект",                              # as rūpārammaṇaṃ = объект in 2-01
    # functional minds (^1-566 …)
    "kammavipākā": "результат действий", "kammavipākaṃ": "результат действий",
    "akusalā": "неблагой", "akusalaṃ": "неблагой",
    "kusalā nākusalā": "ни благой ни неблагой", "kusalaṃ nākusalaṃ": "ни благой ни неблагой",
    "sampayuttā": "связанный", "vippayuttā": "не связанный", "ñāṇavippayuttā": "не связанный со знанием",
    "abyākatamūlaṃ": "этически неопределённый корень",
    "vihāraṃ": "пребывание", "kasiṇaṃ": "всеохватный объект", "pathavī": "земля",
    "sabbaso": "полностью", "samatikkamā": "преодолеть", "samatikkamma": "преодолеть",
    "atthaṅgamā": "исчезновение", "nānatta": "разнообразие",
    "manasikārā": "уделять внимание",                 # a-manasikārā «не уделяя внимания»
    "saññānaṃ": "восприятия", "ākāsa": "пространство", "ānañca": "бесконечный",
    "ānañcāyatana": "сфера бесконечного", "ānañcāyatanaṃ": "сфера бесконечного",
    "viññāṇañca": "бесконечное сознание", "viññāṇañcāyatanaṃ": "сфера бесконечного сознания",
    "ākiñcañña": "отсутствие чего-либо", "asaññā": "невосприятие",
    "pahānā": "устранение", "sukhassa": "приятное", "sukhassa ca pahānā": "устранение приятного",
    "niṭṭhitaṃ": "завершённый",
}
TABLE205 = {**CH2, **T205}
FUNCTIONAL_SEGS = {"1-577", "1-578", "1-579", "1-580", "1-581", "1-582"}


def rule_205(bid, k, s):
    """Context rules; return None when the table value applies."""
    if k == "nikkhitta":                                 # user decision 2026-11-14
        return NDE
    if k in ("kiriyāmano", "kiriyā mano"):              # «Функциональный элемент ума / умственного сознания»
        return "функциональный … " + ("умственный" if any("manoviññāṇa" in x for x in s) else "ум")
    if k == "sukha" and bid in FUNCTIONAL_SEGS:          # diṭṭhadhammasukhavihāraṃ «приятного пребывания»
        return "приятный"
    if k == "dukkha" and ({"dukkhindriyaṃ", "dukkhaṃ"} & s):   # dukkhasahagataṃ / dukkhindriyaṃ «боль»
        return "боль"
    if k == "sahagataṃ" and bid in FUNCTIONAL_SEGS:      # …saññāsahagataṃ «с восприятием»
        return "с"
    return None


OVERRIDES = {
    "1-1-8-2-0": {"suññataṃ": "пустота"},                       # heading «Простая пустота»
    "1-553": {"rūpa": "мир форм", "arūpa": "мир без форм",       # «страсти к миру форм, … к миру без форм»
              "kāma": "чувственный"},                            # «чувственной страсти»
    "1-1-10-5-0": {"Rūpa": "форма"},                            # «относящийся к миру форм»
    "1-577": {"rūpa": "форма"},
    "1-578": {"rūpa": "форма"},
    "1-579": {"rūpa": "материальная форма"},                    # «восприятия материальной формы»
}


def resolve_205(bid, kw, kws):
    ov = OVERRIDES.get(bid, {})
    if kw in ov:
        return ov[kw]
    s = set(lc(x) for x in kws)
    r = rule_205(bid, lc(kw), s)
    if r is not None:
        return r
    return ch2_value(kw, kws, TABLE205)


# ============================================================================ 3-01
T301 = {
    # headings and frame
    "kaṇḍaṃ": "раздел", "rūpa": "материальная форма", "uddeso": "перечень", "mātikā": "матрица",
    "dukaṃ": "классификация по два", "dasakaṃ": "классификация по десять",
    "ekādasakaṃ": "классификация по одиннадцать", "dasa": "десять", "ekādasa": "одиннадцать",
    "vibhatti": "классификация", "niddeso": "разъяснение", "saṅgaho": "классификация",
    "rūpasaṅgaho": "классификация материальной формы", "vidhena": "по",
    "catubbidhena": "по четыре", "chabbidhena": "по шесть", "tattha": "здесь",
    "rūpaṃ": "материальная форма", "eva": "несомненно",
    # uddeso ^1-583
    "khandho": "совокупность", "viññāṇakkhandho": "совокупность сознания",
    "vedanākkhandho": "совокупность чувств", "saṅkhārakkhandho": "совокупность формирующих факторов",
    "saññākkhandho": "совокупность восприятия", "viññāṇa": "сознание", "dhātu": "элемент",
    "vedanā": "чувство", "saññā": "восприятие", "saṅkhāra": "формирующие факторы",
    "kāma": "чувственные желания", "kāmāvacarā": "относящийся к миру чувственных желаний",
    "avacarā": "относящийся к миру", "rūpāvacarā": "относящийся … к миру форм",
    "arūpāvacarā": "относящийся … к миру без форм", "arūpa": "без форм",
    "kiriyā": "функциональный", "abyākatā": "этически неопределённый",
    "dhammā abyākatā": "этически неопределённые явления",
    "asaṅkhatā": "необусловленный", "asaṅkhatā ca dhātu": "необусловленный элемент",
    "akusalānaṃ": "неблагой", "akusalānaṃ dhammānaṃ": "неблагие явления", "kusala": "благой",
    "kusalā nākusalā": "ни благой ни неблагой",
    # ekaka ^1-584 / ^1-594 (finite verbs of the Russian -> infinitive; adjectives as in the matrix)
    "mahābhūtā": "великие элементы", "bhūtā": "элементы", "upādāya": "производный",
    "upādāya rūpaṃ": "материальная форма производная",
    "hetu": "корень", "hetukaṃ": "имеющий корни", "vippayuttaṃ": "не связанный",
    "saṅkhataṃ": "обусловленный", "lokiyaṃ": "мирской", "āsavaṃ": "влечение",
    "sāsavaṃ": "подверженный влечениям", "saṃyojaniyaṃ": "подверженный оковам",
    "ganthaniyaṃ": "подверженный узам", "oghaniyaṃ": "подверженный потокам",
    "yoganiyaṃ": "подверженный ярмам", "nīvaraṇiyaṃ": "подверженный помехам",
    "parāmaṭṭhaṃ": "затронутый искажениями", "upādāniyaṃ": "служащий объектом цепляния",
    "saṃkilesikaṃ": "подверженный омрачению", "abyākataṃ": "этически неопределённый",
    "ārammaṇaṃ": "объект", "cetasikaṃ": "сопутствующий уму", "citta": "ум",
    "cittavippayuttaṃ": "не связанный с умом", "vipākadhamma": "способный приносить результаты",
    "asaṃkiliṭṭha": "не омрачённый", "vitakka": "направленная мысль", "vicāra": "удержание мысли",
    "sahagataṃ": "сопровождаться", "pītisahagataṃ": "сопровождаться восторгом",
    "sukhasahagataṃ": "сопровождаться счастьем", "upekkhāsahagataṃ": "сопровождаться невозмутимостью",
    "pīti": "восторг", "sukha": "счастье", "upekkhā": "невозмутимость",
    "dassanena": "видение истины", "pahātabbaṃ": "устраняться",
    "ācaya": "накопление", "apacaya": "убывание", "gāmi": "ведущий",
    "sekkha": "обучающийся", "asekkhaṃ": "завершивший обучение",
    "parittaṃ": "ограниченный", "kāmāvacaraṃ": "относящийся к миру чувственных желаний",
    "avacaraṃ": "относящийся к миру", "rūpāvacaraṃ": "относящийся к миру форм",
    "arūpāvacaraṃ": "относящийся к миру без форм",
    "apariyāpannaṃ": "не принадлежащий к кругам существования",
    "niyataṃ": "предопределённый", "niyyānikaṃ": "ведущий к освобождению",
    "uppannaṃ": "возникший", "viññāṇehi": "виды сознания",
    "viññeyyaṃ": "познаваться",                        # «познаётся» (1-584); «познаваемая» in 1-588 …
    "aniccaṃ": "непостоянный", "jarā": "старение", "abhibhūtaṃ": "подвластный",
    # dyads / triads / tetrads (^1-U1, ^1-585, ^1-586)
    "upādā": "производный", "upādiṇṇaṃ": "охваченный цеплянием",
    "upādiṇṇupādāniyaṃ": "охваченный цеплянием и служащий его объектом",
    "anupādiṇṇupādāniyaṃ": "не охваченный цеплянием но служащий его объектом",
    "sanidassanaṃ": "видимый", "anidassanaṃ": "невидимый", "anidassana": "невидимый",
    "sappaṭighaṃ": "способный к соударению", "appaṭighaṃ": "не способный к соударению",
    "anidassanaappaṭighaṃ": "невидимый и не способный к соударению",
    "rūpaṃ sappaṭighaṃ": "материальная форма … способный к соударению",
    "indriyaṃ": "способность", "bhūtaṃ": "элемент", "mahābhūtaṃ": "великий элемент",
    "viññatti": "внешнее выражение", "kāyaviññatti": "телесное внешнее выражение",
    "vacī": "речевой", "vacīviññatti": "речевое внешнее выражение",
    "samuṭṭhānaṃ": "порождённый", "cittasamuṭṭhānaṃ": "порождённый умом",
    "cittasahabhu": "сосуществующий с умом", "anuparivatti": "следующий за",
    "cittānuparivatti": "следующий за умом",
    "rūpaṃ cittasamuṭṭhānaṃ": "материальная форма … порождённый умом",
    "rūpaṃ cittasahabhu": "материальная форма … сосуществующий с умом",
    "rūpaṃ cittānuparivatti": "материальная форма … следующий за умом",
    "ajjhattikaṃ": "относящийся к внутреннему", "bāhiraṃ": "относящийся к внешнему",
    "oḷārikaṃ": "грубый", "sukhumaṃ": "тонкий",
    "cakkhu": "глаз", "sota": "ухо", "ghāna": "нос", "jivhā": "язык", "kāya": "тело",
    "cakkhusamphassassa": "контакт глаза", "sotasamphassassa": "контакт уха",
    "ghānasamphassassa": "контакт носа", "jivhāsamphassassa": "контакт языка",
    "kāyasamphassassa": "контакт тела", "samphassajāya": "рождённый контактом",
    "kāyasamphassajāya": "рождённый контактом тела", "vedanāya": "чувство",
    "samphassajāya vedanāya": "чувство рождённое контактом", "saññāya": "восприятие",
    "cetanāya": "намерение", "cakkhuviññāṇassa": "зрительное сознание",
    "kāyaviññāṇassa": "осязательное сознание",
    "cakkhāyatanaṃ": "сфера глаза", "sotāyatanaṃ": "сфера уха", "ghānāyatanaṃ": "сфера носа",
    "jivhāyatanaṃ": "сфера языка", "kāyāyatanaṃ": "сфера тела", "rūpāyatanaṃ": "сфера видимых форм",
    "saddāyatanaṃ": "сфера звуков", "gandhāyatanaṃ": "сфера запахов", "rasāyatanaṃ": "сфера вкусов",
    "phoṭṭhabbāyatanaṃ": "сфера осязаемого",
    "cakkhudhātu": "элемент глаза", "sotadhātu": "элемент уха", "ghānadhātu": "элемент носа",
    "jivhādhātu": "элемент языка", "kāyadhātu": "элемент тела", "rūpadhātu": "элемент видимых форм",
    "saddadhātu": "элемент звуков", "gandhadhātu": "элемент запахов", "rasadhātu": "элемент вкусов",
    "phoṭṭhabbadhātu": "элемент осязаемого",
    "sadda": "звук", "gandha": "запах", "rasa": "вкус", "phoṭṭhabba": "осязаемое",
    "itthi": "женственность", "purisa": "мужественность", "jīvita": "жизненный",
    "itthindriyaṃ": "способность женственности", "purisindriyaṃ": "способность мужественности",
    "jīvitindriyaṃ": "жизненная способность",
    "ākāsa": "пространство", "ākāsadhātu": "элемент пространства",
    "āpo": "вода", "āpodhātu": "элемент воды",
    "lahutā": "лёгкость", "rūpassa lahutā": "лёгкость материальной формы",
    "mudutā": "мягкость", "rūpassa mudutā": "мягкость материальной формы",
    "kammaññatā": "работоспособность", "rūpassa kammaññatā": "работоспособность материальной формы",
    "rūpassa upacayo": "рост материальной формы",
    "santati": "непрерывность", "rūpassa santati": "непрерывность материальной формы",
    "jaratā": "старение", "rūpassa jaratā": "старение материальной формы",
    "aniccatā": "непостоянство", "rūpassa aniccatā": "непостоянство материальной формы",
    "kabaḷīkāro": "съедаемый", "āhāro": "пища", "kabaḷīkāro āhāro": "съедаемая пища",
    "viññātaṃ": "познанный", "sutaṃ": "услышанный", "mutaṃ": "ощущённый",
    # pentad … hendecad (^1-587 … ^1-593)
    "pathavī": "земля", "pathavīdhātu": "элемент земли", "tejo": "огонь", "tejodhātu": "элемент огня",
    "vāyo": "ветер", "vāyodhātu": "элемент ветра",
    "viññeyyaṃ rūpaṃ": "познаваемая … материальная форма", "mano": "ум",
    "manodhātu": "элемент ума", "manoviññāṇa": "умственное сознание",
    "manoviññāṇadhātu": "элемент умственного сознания",
    "dukkha": "болезненный", "samphassaṃ": "контакт",
    "dhamma": "объекты ума", "dhammāyatana": "сфера объектов ума",
}

OVERRIDES_301 = {
    "1-583": {"rūpa": "форма"},                        # rūpāvacarā «к миру форм» (rūpaṃ = материальная форма)
    "1-585": {"upādāniyaṃ": "служащий его объектом"},  # only inside (an)upādiṇṇupādāniyaṃ
    "1-586": {"upādāniyaṃ": "служащий его объектом"},
    "1-U1": {"upādāniyaṃ": "служащий его объектом"},
    "1-588": {"viññeyyaṃ": "познаваемый"},             # «Познаваемая глазом …»
    "1-589": {"viññeyyaṃ": "познаваемый"},
    "1-590": {"viññeyyaṃ": "познаваемый", "sukha": "приятный"},   # «приятная при контакте»
    "1-594": {"uppannaṃ": "возникнуть"},               # «познаётся, возникнув»
}

_RU301 = None


def resolve_301(bid, kw, kws):
    global _RU301
    if _RU301 is None:
        _RU301 = read_russian("3-01-rupakandam")
    ov = OVERRIDES_301.get(bid, {})
    if kw in ov:
        return ov[kw]
    k = lc(kw)
    if k.endswith("meva") and k != "eva":               # X-meva (^1-594) = «несомненно» + X
        base = k[:-4] + "ṃ"
        v = T301[base]
        joined = "несомненно " + v
        return joined if present(joined, _RU301[bid]) else "несомненно" + GAP + v
    return T301[k]


if __name__ == "__main__":
    build_part("2-05-cittuppadakandam", resolve_205)
    build_part("3-01-rupakandam", resolve_301)
    for p in PARTS:
        verify(p)
