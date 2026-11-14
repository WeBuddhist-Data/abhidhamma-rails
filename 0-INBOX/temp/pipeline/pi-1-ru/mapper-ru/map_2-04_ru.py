"""Build the Pāli->Russian keyword map for pi-1 part 2-04-cittuppadakandam
(twelve unwholesome minds; results of the wholesome).

usage: python -I -X utf8 map_2-04_ru.py      (writes 2-04-cittuppadakandam.mapped.md and verifies it)

Resolution order per keyword: OVERRIDES[bid][kw] -> context rules (rule_value) -> TABLE (CH2 + T204)
via ch2_value. Decisions are listed in notes-map-2-04.md; the shared conventions are in
ru-map-conventions.md. Read-only use of map_common_ru.py.
"""
import pathlib
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-ru\mapper-ru")
from map_common_ru import CH2, GAP, NDE, build_part, ch2_value, lc, verify  # noqa: E402

PART = "2-04-cittuppadakandam"

T204 = {
    # ---- frame: unwholesome / indeterminate
    "akusalā": "неблагой", "akusala": "неблагой", "akusalāni": "неблагой",
    "akusalaṃ cittaṃ": "неблагой ум", "dhammā akusalā": "неблагие явления",
    "akusalacittāni": "виды неблагого ума", "dvādasa": "двенадцать",
    "abyākata": "этически неопределённый", "abyākatā": "этически неопределённый",
    "dhammā abyākatā": "этически неопределённые явления",
    "abyākatamūlaṃ": "этически неопределённый корень", "akusalamūlaṃ": "неблагой корень",
    "cittaṃ uppannaṃ": "возникать" + GAP + "ум",                 # «возникает неблагой ум»
    "uppannā": "возникать", "dhātu uppannā": "возникать элемент",  # «возникает элемент ума»
    "dhammārammaṇaṃ": "объект ума", "dhammārammaṇā": "объект ума", "ārammaṇā": "объект",
    "diṭṭhigata": "приверженность воззрениям",
    "diṭṭhigatavippayuttaṃ": "не связанный с приверженностью воззрениям",
    "domanassa": "уныние", "domanassasahagataṃ": "сопровождаемый унынием", "paṭigha": "неприязнь",
    "sahagatā": "сопровождаемый", "somanassasahagatā": "сопровождаемый радостью",
    "upekkhāsahagatā": "сопровождаемый невозмутимостью", "sukhasahagataṃ": "сопровождаемый счастьем",
    "sampayuttā": "связанный", "vippayuttā": "не связанный", "ñāṇavippayuttā": "не связанный со знанием",
    "vicikicchā": "колебание", "uddhacca": "беспокойство", "uddhaccaṃ": "беспокойство",
    "tivaṅgiko": "трёхчастный", "duvaṅgiko": "двухчастный", "hetu": "корень",
    # ---- unwholesome factor names
    "micchā": "ложный", "micchādiṭṭhi": "ложное воззрение", "micchāsaṅkappo": "ложный помысел",
    "micchāvāyāmo": "ложное усилие", "micchāsamādhi": "ложное сосредоточение",
    "ahirika": "бессовестность", "ahirikaṃ": "бессовестность", "ahirikabalaṃ": "сила бессовестности",
    "anottappa": "отсутствие страха перед дурным", "anottappaṃ": "отсутствие страха перед дурным",
    "anottappabalaṃ": "сила отсутствия страха перед дурным",
    "lobho": "жадность", "moho": "заблуждение", "abhijjhā": "алчность", "doso": "злоба",
    "byāpādo": "недоброжелательность", "dukkhaṃ": "боль",
    # ---- nikkhitta: user decision 2026-11-14 (cut «не-» leaves a non-word)
    "nikkhitta": NDE,
    # ---- hiri / ottappa frames
    "ottappitabbena": "следует бояться",                          # «того, чего следует бояться»
    # ---- lobha string
    "sārāgo": "страсть",
    # ---- moha string (pi-4 ^4-60; fragments = the positive part)
    "aññāṇaṃ": "незнание", "ñāṇaṃ": "знание", "dassanaṃ": "видение",
    "anabhisamayo": "отсутствие постижения", "anubodho": "понимание", "sambodho": "пробуждённость",
    "appaṭivedho": "отсутствие проникновения", "asaṃgāhanā": "неохватывание",
    "pariyogāhanā": "углубление", "samapekkhanā": "рассмотрение", "paccavekkhanā": "обдумывание",
    "paccakkhakammaṃ": "видеть воочию", "dummejjhaṃ": "тупость", "bālyaṃ": "глупость",
    "pamoho": "сильное заблуждение", "sammoho": "полное заблуждение", "avijjā": "неведение",
    "ogho": "поток", "yogo": "ярмо", "anusayo": "скрытая склонность", "pariyuṭṭhānaṃ": "одержимость",
    "laṅgī": "засов",
    # ---- diṭṭhi string
    "diṭṭhigataṃ": "приверженность воззрениям", "gahanaṃ": "дебри", "kantāro": "пустыня",
    "visūkāyikaṃ": "извращённость", "vipphanditaṃ": "метания", "saṃyojanaṃ": "оковы",
    "diṭṭhisaṃyojanaṃ": "оковы воззрений", "gāho": "хватка", "patiṭṭhāho": "закрепление",
    "abhiniveso": "приверженность", "parāmāso": "искажение", "kummaggo": "кривая дорога",
    "patho": "путь", "micchāpatho": "ложный путь", "micchattaṃ": "ложность",
    "tittha": "сектантские учения", "vipariyāsa": "превратный", "vipariyāsaggāho": "превратная хватка",
    # ---- dosa string (pi-4 ^4-45)
    "byāpatti": "недоброжелательность", "byāpajjanā": "проявление недоброжелательности",
    "dussitattaṃ": "состояние злобы", "virodho": "вражда", "paṭivirodho": "противодействие",
    "caṇḍikkaṃ": "свирепость", "asuropo": "грубость", "anattamanatā": "недовольство",
    # ---- painful feeling string
    "cetasikaṃ dukkhaṃ": "душевная боль", "dukkhā vedanā": "болезненное чувство",
    # ---- vicikicchā string
    "kaṅkhā": "сомнение", "kaṅkhāyanā": "проявление сомнения", "vimati": "неуверенность",
    "dveḷhakaṃ": "раздвоенность", "dvedhā": "распутье", "saṃsayo": "нерешительность",
    "anekaṃsaggāho": "неспособность прийти к определённости", "ekaṃsa": "определённость",
    "āsappanā": "блуждание", "parisappanā": "беспорядочное блуждание",
    "thambhitattaṃ": "оцепенелость", "vilekho": "терзание",
    # ---- uddhacca string
    "avūpasamo": "отсутствие затихания", "vikkhepo": "отвлечение", "bhantattaṃ": "взбудораженность",
    # ---- results of the wholesome
    "kusalassa": "благой", "kusalassa kammassa": "благое действие",
    "kāmāvacarassa": "относящийся к миру чувственных желаний", "avacarassa": "относящийся к миру",
    "rūpāvacarassa": "относящийся к миру форм", "arūpāvacarassa": "относящийся к миру без форм",
    "katattā": "совершённый", "upacitattā": "накопленный",
    "cakkhuviññāṇaṃ": "зрительное сознание", "sotaviññāṇaṃ": "слуховое сознание",
    "ghānaviññāṇaṃ": "обонятельное сознание", "jivhāviññāṇaṃ": "вкусовое сознание",
    "kāyaviññāṇaṃ": "осязательное сознание",
    "cakkhuviññāṇa": "зрительное сознание", "cakkhuviññāṇadhātu": "элемент зрительного сознания",
    "kāyaviññāṇa": "осязательное сознание", "kāyaviññāṇadhātu": "элемент осязательного сознания",
    "manodhātu": "элемент ума", "sukha": "счастье",
    "kāyikaṃ": "телесный", "kāyasamphassajaṃ": "рождённый контактом тела",
    "kāyasamphassajā": "рождённый контактом тела",
    # vipāka: stem = noun; inflected (adjectival) forms = «являющийся результатом»
    "vipāka": "результат", "kusalavipāka": "результат благих действий",
    "vipākā": "являющийся результатом", "vipākāni": "являющийся результатом",
    "kusalavipākā": "являющийся результатом благих действий",
    "kusalavipākāni": "являющийся результатом благих действий",
    "abyākatavipāko": "этически неопределённый результат действий",
    "mahāvipākā": "великие результаты действий", "viññāṇāni": "виды сознания",
    "vipākapañcaviññāṇāni": "пять видов сознания являющихся результатом",
    "vipākāni pañcaviññāṇāni": "пять видов сознания являющихся результатом",
    "vipākamanodhātu": "элемент ума являющийся результатом",
    "vipākā manodhātu": "элемент ума являющийся результатом",
    "vipākamanoviññāṇadhātu": "элемент умственного сознания являющийся результатом",
    "vipākā manoviññāṇadhātu": "элемент умственного сознания являющийся результатом",
    "vipākā upekkhāsahagatā manoviññāṇadhātu":
        "элемент умственного сознания являющийся результатом" + GAP + "сопровождаемый невозмутимостью",
    "rūpāvacara": "относящийся к миру форм", "arūpāvacara": "относящийся к миру без форм",
    "arūpa": "без форм",
    # ---- fine-material / immaterial results (absorption phrases)
    "bhāveti": "развивать", "maggaṃ": "путь", "maggaṃ bhāveti": "развивать путь",
    "upapattiyā": "рождение", "upapattiyā maggaṃ": "путь к рождению",
    "vivicca": "уединившись", "eva": "полностью", "kāmehi": "чувственные удовольствия",
    "vivicceva kāmehi": "полностью уединившись от чувственных удовольствий",
    "upasampajja": "входить", "viharati": "пребывать", "upasampajja viharati": "входить" + GAP + "пребывать",
    "pathavī": "земля", "kasiṇaṃ": "всеохватный объект",
    "kusalā": "благой", "dhammā kusalā": "благие явления",
    "pahānā": "устранение", "sukhassa": "приятное", "sukhassa ca pahānā": "устранение приятного",
    "vitakka": "направленная мысль", "vicārānaṃ": "удержание мысли", "vūpasamā": "затихание",
    "catutthaṃ jhānaṃ": "четвёртое медитативное погружение",
    "sabbaso": "полностью", "samatikkamā": "преодолев", "samatikkamma": "преодолев",
    "saññānaṃ": "восприятия", "atthaṅgamā": "исчезновение", "nānatta": "разнообразие",
    "manasikārā": "внимание",
    "ākāsa": "пространство", "ānañca": "бесконечный", "ānañcāyatana": "сфера бесконечного",
    "ānañcāyatanaṃ": "сфера бесконечного", "viññāṇañca": "бесконечное сознание",
    "viññāṇañcāyatanaṃ": "сфера бесконечного сознания", "ākiñcañña": "отсутствие чего-либо",
    "asaññā": "невосприятие",
}
TABLE = {**CH2, **T204}

# Per-segment readings found when comparing each segment's Russian.
OVERRIDES = {
    # kāyikaṃ sukhaṃ = «телесное удовольствие» in the feeling / sukhindriya answers
    "1-445": {"sukhaṃ": "удовольствие"},
    "1-452": {"sukhaṃ": "удовольствие", "sukha": "удовольствие"},   # «способность удовольствия»
    # 1-449 asks for sukhaṃ (= «счастье», the factor); kept at the default счастье.
    # vicikicchā string: «терзание ума» (manovilekho), «распутье» (dvedhāpatho, one Russian word)
    "1-425": {"mano": "ум", "patho": "распутье"},
    # closing line «Двенадцать видов неблагого ума»
    "1-430": {"cittāni": "виды" + GAP + "ума"},
}


def rule_value(bid, kw, kws):
    k = lc(kw)
    s = set(lc(x) for x in kws)
    if k == "mano" and "manodhātu" in s and "hadayaṃ" not in s:   # «элемент ума»
        return "ум"
    if k == "rūpa":
        if "saññānaṃ" in s:                                         # rūpasaññānaṃ: «восприятия материальной формы»
            return "материальная форма"
        if s & {"rūpāvacarassa", "rūpāvacara"}:                     # «мир форм»
            return "форма"
    if k == "sahagataṃ" and s & {"samatikkamā", "samatikkamma"}:   # X-saññāsahagataṃ: «с восприятием X»
        return "с"
    return None


def resolve(bid, kw, kws):
    ov = OVERRIDES.get(bid, {})
    if kw in ov:
        return ov[kw]
    v = rule_value(bid, kw, kws)
    if v is not None:
        return v
    return ch2_value(kw, kws, TABLE)


if __name__ == "__main__":
    build_part(PART, resolve)
    verify(PART)
