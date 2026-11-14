"""Shared helpers and tables for the pi-1 Pāli->Russian keyword maps (mapper-ru/).

Importing this module has no side effects (no file is written, nothing printed).

    import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    from map_common_ru import *

Main pieces
- read_keywords(part)              -> [(id, [kw, ...]), ...]   from <part>.keywords.md
- read_russian(part) / read_pali(part) -> {id: segment text}   (segments end with ^id)
- present(value, text)             -> True if a Russian value occurs (regular inflection allowed) in text
- CORE                             -> cross-book core terms (preamble / frame)
- CH2 + ch2_value(kw, kws)         -> default table for the cittuppāda chapters (2-01 ... 2-05) with context rules
- MATRIX                           -> matrix item names as settled in 1-matika (default per keyword)
- build_part(part, resolver)       -> writes <part>.mapped.md; resolver(id, kw, kws) returns the Russian
- verify(part)                     -> the brief's structural check + the presence check; prints a report
"""
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
RU_DIR = ROOT / "AI_translation" / "russian" / "pi-1-russian-plain-zeroshot_split_chapters"
PI_DIR = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
NDE = "(no direct equivalent)"
GAP = " … "  # discontinuous Russian (e.g. samaye X = «в это время … X»)


# ---------------------------------------------------------------------------- reading
def read_keywords(part):
    out = []
    for line in (HERE / f"{part}.keywords.md").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        bid, rest = line.split("] ", 1)
        out.append((bid[1:], [k.strip() for k in rest.split(", ")]))
    return out


def _segments(path):
    segs = {}
    for block in re.split(r"\n\s*\n", path.read_text(encoding="utf-8")):
        block = block.strip()
        if not block:
            continue
        m = re.search(r"\^([0-9A-Za-z-]+)\s*$", block)
        if m:
            segs[m.group(1)] = block[: m.start()].strip()
    return segs


def read_russian(part):
    return _segments(RU_DIR / f"{part}.md")


def read_pali(part):
    return _segments(PI_DIR / f"{part}.md")


# ---------------------------------------------------------------------------- presence check
# A value is "present" when each of its parts (split on " … " and " / ") occurs in the segment's
# Russian with regular inflection: endings are stripped to a stem (ё = е), «нн» may be «н»
# (связанный ~ связаны), a participle stem in -ащ/-ящ/-ущ/-ющ matches the finite verb
# (служащий ~ служат), -овать matches -ует (следовать ~ следует), a glued «не» prefix is
# allowed (отступный ~ неотступное, проявление ~ непроявление), and a separate «не» may sit
# between two words. Commas, dashes, quotes and variant brackets are ignored.
CYR = "а-яa-z0-9"
ENDINGS = sorted(["иями", "ями", "ами", "ого", "его", "ому", "ему", "ыми", "ими", "ться", "тся",
                  "ая", "яя", "ое", "ее", "ые", "ие", "ый", "ий", "ой", "ую", "юю", "ых", "их",
                  "ым", "им", "ам", "ям", "ах", "ях", "ом", "ем", "ей", "ов", "ев", "ия", "ию", "ии",
                  "ть", "а", "я", "о", "е", "ы", "и", "у", "ю", "ь", "й"], key=len, reverse=True)
ALT = {
    "ум": "ум(?:а|у|ом|е|ы|ов)?", "то": "(?:то|того|тому|тем|том)", "в": "(?:в|во)", "с": "(?:с|со)",
    "к": "(?:к|ко)", "о": "(?:о|об|обо)", "корень": "кор(?:е)?н[а-я]*", "бояться": "бо(?:я|и)[а-я]*",
    "его": "его", "им": "им", "ним": "ним",
}
EXACT = {"и", "но", "ни", "не", "за", "от", "без", "над", "из", "до", "по", "на", "что", "бы", "или",
         "же", "ли"}


def _norm(t):
    t = re.sub(r"\s*\[[^\]]*\]", "", t)          # variant brackets
    t = t.lower().replace("ё", "е")
    t = re.sub(r"[,;:–—…«»„“”\"?!.()]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def _token(w):
    if w in ALT:
        return ALT[w]
    if w in EXACT or len(w) <= 2:
        return re.escape(w) + f"(?![{CYR}])"
    core = w[:-2] if len(w) > 4 and w.endswith(("ся", "сь")) else w   # reflexive: относящийся ~ относящиеся
    stem = core
    for e in ENDINGS:
        if core.endswith(e) and len(core) - len(e) >= 2:
            stem = core[: -len(e)]
            break
    if stem == core:                                                    # fleeting vowel: проступок ~ проступках
        m = re.search(r"[^аеиоуыэюя]([ое])([кцн])$", stem)
        if m:
            stem = stem[: m.start(1)] + f"(?:{m.group(1)})?" + m.group(2)
            return f"(?:не)?{re.escape(stem[:stem.index('(?:')])}{stem[stem.index('(?:'):]}[{CYR}]*"
    if re.search(r"[аяую]щ$", stem):              # participle -ащ/-ящ/-ущ/-ющ ~ finite verb
        stem = stem[:-2]
    tail = ""
    if stem.endswith("ова") or stem.endswith("ева"):  # следовать ~ следует
        stem, tail = stem[:-3], "(?:ова|ева|у|ю)"
    pat = re.escape(stem).replace("нн", "нн?") + tail
    return f"(?:не)?{pat}[{CYR}]*"


def _pattern(phrase):
    toks = _norm(phrase).split()
    body = r"\s+(?:не\s+)?".join(_token(t) for t in toks)   # a separate «не» may intervene
    return re.compile(f"(?<![{CYR}]){body}")


def present(value, text):
    if value == NDE:
        return True
    t = _norm(text)
    for part in re.split(r" … | / ", value):
        if part.strip() and not _pattern(part).search(t):
            return False
    return True


# ---------------------------------------------------------------------------- core / frame terms
CORE = {
    "abhidhamma": "Абхидхамма", "abhidhammapiṭake": "корзина Абхидхаммы",
    "saṅgaṇī": "перечисление", "dhammasaṅgaṇī": "Перечисление явлений", "dhamma": "явление",
    "namo": "почтение", "bhagavato": "Благословенный", "arahato": "Достойный", "sammā": "полностью",
    "sambuddhassa": "Будда", "sammāsambuddhassa": "Полностью Пробуждённый Будда",
}

# ---------------------------------------------------------------------------- CH2 default table
# Pāli keyword (as the keyword files spell it, lower-case first letter) -> Russian dictionary form.
CH2 = {
    # frame / opening of each type of mind
    "kusalā": "благой", "kusalaṃ": "благой", "kusala": "благой",
    "kusalaṃ cittaṃ": "благой ум", "dhammā kusalā": "благие явления",
    "akusalānaṃ": "неблагой", "akusalānaṃ dhammānaṃ": "неблагие явления",
    "kāma": "чувственные желания", "kāmāvacaraṃ": "относящийся к миру чувственных желаний",
    "kāmāvacara": "относящийся к миру чувственных желаний",
    "avacaraṃ": "относящийся к миру", "avacara": "относящийся к миру",
    "cittaṃ": "ум", "citta": "ум", "cittassa": "ум", "cittāni": "виды ума",
    "uppannaṃ": "возникать", "uppāda": "возникновение", "cittuppāda": "возникновение ума",
    "kaṇḍaṃ": "раздел",
    "sahagataṃ": "сопровождаемый", "somanassasahagataṃ": "сопровождаемый радостью",
    "upekkhāsahagataṃ": "сопровождаемый невозмутимостью", "somanassa": "радость",
    "upekkhā": "невозмутимость",
    "somanassindriyaṃ": "способность радости", "upekkhindriyaṃ": "способность невозмутимости",
    "ñāṇa": "знание", "sampayuttaṃ": "связанный", "vippayuttaṃ": "не связанный",
    "ñāṇavippayuttaṃ": "не связанный со знанием", "saṅkhārena": "побуждение",
    "rūpa": "видимая форма", "sadda": "звук", "gandha": "запах", "rasa": "вкус",
    "phoṭṭhabba": "осязаемое",
    "ārammaṇaṃ": "объект", "ārabbha": "имеющий объектом", "yaṃ yaṃ": "что бы то ни было",
    "samuppannā": "возникший", "samuppannā arūpino": "нематериальный … возникший",
    "samuppannā arūpino dhammā": "нематериальные явления возникшие",
    "paṭicca": "в зависимости от условий",
    "paṭiccasamuppannā": "возникший в зависимости от условий",
    "paṭiccasamuppannā arūpino": "нематериальный … возникший в зависимости от условий",
    "arūpino": "нематериальный", "arūpino dhammā": "нематериальные явления",
    "arūpīnaṃ": "нематериальный", "arūpīnaṃ dhammānaṃ": "нематериальные явления",
    "yo": "то что", "yā": "то что", "yaṃ": "то что", "ye": "какой",
    "ṭhapetvā": "кроме",
    # contact, feeling, perception, intention, mind
    "phasso": "контакт", "phassa": "контакт", "phusanā": "касание", "saṃphusanā": "соприкосновение",
    "vedanā": "чувство", "vedayitaṃ": "переживание",
    "saññā": "восприятие", "sañjānanā": "узнавание", "sañjānitattaṃ": "состояние узнавания",
    "cetanā": "намерение", "sañcetanā": "проявление намерения",
    "cetayitattaṃ": "состояние намеренности",
    "manosañcetanā": "умственное намерение", "mano": "разум", "āhāro": "питание",
    "āhārā": "виды питания",
    "mānasaṃ": "умственная деятельность", "hadayaṃ": "сердце", "paṇḍaraṃ": "чистота",
    "mana": "ум", "manāyatanaṃ": "сфера ума", "manindriyaṃ": "способность ума",
    "viññāṇaṃ": "сознание", "viññāṇa": "сознание",
    "khandho": "совокупность", "khandhā": "совокупности", "khandhassa": "совокупность",
    "viññāṇakkhandho": "совокупность сознания", "viññāṇakkhandhaṃ": "совокупность сознания",
    "viññāṇakkhandhassa": "совокупность сознания",
    "vedanākkhandho": "совокупность чувств", "vedanākkhandhaṃ": "совокупность чувств",
    "vedanākkhandhassa": "совокупность чувств",
    "saññākkhandho": "совокупность восприятия", "saññākkhandhaṃ": "совокупность восприятия",
    "saññākkhandhassa": "совокупность восприятия",
    "saṅkhārakkhandho": "совокупность формирующих факторов",
    "saṅkhārakkhandhaṃ": "совокупность формирующих факторов",
    "saṅkhārakkhandhassa": "совокупность формирующих факторов",
    "saṅkhāra": "формирующие факторы",
    "tajjā": "соответствующий", "dhātu": "элемент", "dhātuyo": "элементы",
    "manoviññāṇa": "умственное сознание", "manoviññāṇadhātu": "элемент умственного сознания",
    "dhammāyatanaṃ": "сфера объектов ума", "dhammadhātu": "элемент объектов ума",
    "āyatanāni": "сферы восприятия", "indriyaṃ": "способность", "indriyāni": "способности",
    # feeling string
    "samphassajaṃ": "рождённый контактом", "samphassajā": "рождённый контактом",
    "cetosamphassajaṃ": "рождённый контактом ума", "cetosamphassajā": "рождённый контактом ума",
    "cetasikaṃ": "душевный", "sātaṃ": "отрадный", "asātaṃ": "безотрадный",
    "cetasikaṃ sātaṃ": "душевная отрада", "cetasikaṃ sukhaṃ": "душевное счастье",
    "sukhaṃ": "счастье", "sukhā": "приятный", "sukhaṃ vedayitaṃ": "приятное переживание",
    "sukhā vedanā": "приятное чувство",
    "adukkhamasukhaṃ": "ни болезненный ни приятный",
    "cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ":
        "рождённое контактом ума переживание которое ни болезненно ни приятно",
    "cetosamphassajā adukkhamasukhā vedanā":
        "рождённое контактом ума чувство которое ни болезненно ни приятно",
    # vitakka / vicāra / pīti strings
    "vitakko": "направленная мысль", "takko": "мышление", "saṅkappo": "помысел",
    "appanā": "прикрепление мысли", "cetaso": "ум", "abhiniropanā": "направление … на объект",
    "vicāro": "удержание мысли", "cāro": "движение мысли",
    "anusandhānatā": "непрерывная связь … с объектом",
    "anupekkhanatā": "неотрывное наблюдение за объектом",
    "pīti": "восторг", "pāmojjaṃ": "ликование", "āmodanā": "веселье", "pamodanā": "оживление",
    "hāso": "весёлость", "pahāso": "бурная весёлость", "vitti": "удовлетворённость",
    "odagyaṃ": "воодушевление", "attamanatā": "довольство",
    # samādhi string
    "ekaggatā": "однонаправленность", "cittassekaggatā": "однонаправленность ума",
    "ṭhiti": "устойчивость", "cittassa ṭhiti": "устойчивость ума", "saṇṭhiti": "собранность",
    "avaṭṭhiti": "стабильность", "avisāhāro": "отсутствие рассеяния",
    "avikkhepo": "отсутствие отвлечения", "avisāhaṭa": "нерассеянность",
    "avisāhaṭamānasatā": "нерассеянность ума", "mānasatā": "ум",
    "samatho": "успокоение", "samādhi": "сосредоточение",
    "samādhindriyaṃ": "способность сосредоточения", "samādhibalaṃ": "сила сосредоточения",
    "balaṃ": "сила", "balāni": "силы", "sammā": "правильный",
    # saddhā string
    "saddhā": "вера", "saddahanā": "доверие", "okappanā": "уверенность",
    "abhippasādo": "глубокая убеждённость", "saddhindriyaṃ": "способность веры",
    "saddhābalaṃ": "сила веры",
    # vīriya string
    "cetasiko": "душевный", "cetasiko vīriyārambho": "душевное приложение усердия",
    "ārambho": "приложение", "nikkamo": "порыв", "parakkamo": "напор", "uyyāmo": "старание",
    "vāyāmo": "усилие", "ussāho": "рвение", "ussoḷhī": "упорство", "thāmo": "стойкость",
    "dhiti": "твёрдость", "asithila": "неослабевающий", "nikkhitta": "(no direct equivalent)",  # user 2026-11-14
    "chandatā": "желание", "dhuratā": "несение бремени", "sampaggāho": "крепкое удержание",
    "vīriyindriyaṃ": "способность усердия", "vīriyabalaṃ": "сила усердия",
    "paggāho": "напряжение сил",
    # sati string
    "sati": "осознанность", "anussati": "припоминание", "paṭissati": "воспоминание",
    "saraṇatā": "способность помнить", "dhāraṇatā": "способность удерживать в памяти",
    "pilāpanatā": "поверхностность", "sammussanatā": "забывчивость",
    "satindriyaṃ": "способность осознанности", "satibalaṃ": "сила осознанности",
    # paññā string
    "paññā": "мудрость", "pajānanā": "понимание", "vicayo": "исследование",
    "pavicayo": "тщательное исследование", "dhammavicayo": "исследование явлений",
    "sallakkhaṇā": "различение", "upalakkhaṇā": "распознавание",
    "paccupalakkhaṇā": "точное распознавание", "paṇḍiccaṃ": "учёность", "kosallaṃ": "умелость",
    "nepuññaṃ": "тонкость", "vebhabyā": "ясность суждения", "cintā": "размышление",
    "upaparikkhā": "проверка", "bhūrī": "широта ума", "medhā": "разумность",
    "pariṇāyikā": "руководящая сила", "vipassanā": "прозрение", "sampajaññaṃ": "ясное понимание",
    "patodo": "стрекало", "paññindriyaṃ": "способность мудрости", "paññābalaṃ": "сила мудрости",
    "satthaṃ": "меч", "paññāsatthaṃ": "меч мудрости", "pāsādo": "башня",
    "paññāpāsādo": "башня мудрости", "āloko": "свет", "paññāāloko": "свет мудрости",
    "obhāso": "сияние", "paññāobhāso": "сияние мудрости", "pajjoto": "светоч",
    "paññāpajjoto": "светоч мудрости", "ratanaṃ": "сокровище", "paññāratanaṃ": "сокровище мудрости",
    "amoho": "отсутствие заблуждения", "diṭṭhi": "воззрение",
    # jīvita string
    "jīvita": "жизненный", "jīvitindriyaṃ": "жизненная способность", "āyu": "срок жизни",
    "yapanā": "поддержание", "yāpanā": "продление", "iriyanā": "движение", "vattanā": "течение",
    "pālanā": "сбережение",
    # hiri / ottappa strings
    "hirīyati": "стыдиться", "hiri": "совестливость", "hirī": "совестливость",
    "hiribalaṃ": "сила совестливости",
    "ottappati": "бояться", "ottappa": "страх перед дурным", "ottappaṃ": "страх перед дурным",
    "ottappabalaṃ": "сила страха перед дурным", "pāpakānaṃ": "дурной",
    "samāpattiyā": "допускать в себе",
    # roots
    "alobho": "отсутствие жадности", "lubbhanā": "проявление жадности",
    "asārāgo": "отсутствие страсти", "sārajjanā": "проявление страсти",
    "anabhijjhā": "отсутствие алчности", "mūlaṃ": "корень", "kusalamūlaṃ": "благой корень",
    "adoso": "отсутствие злобы", "dussanā": "проявление злобы",
    "abyāpādo": "отсутствие недоброжелательности", "abyāpajjo": "отсутствие неприязни",
    "byāpajjo": "неприязнь", "hetū": "корни",
    # the six pairs (kāya = the mental body = the three mental aggregates)
    "kāya": "умственное тело",
    "passaddhi": "безмятежность", "cittapassaddhi": "безмятежность ума", "passambhanā": "утихание",
    "passambhitattaṃ": "состояние … утихания",
    "paṭipassambhitattaṃ": "состояние полного утихания",
    "lahutā": "лёгкость", "cittalahutā": "лёгкость ума", "lahu": "быстрота",
    "adandhanatā": "отсутствие медлительности", "dandhanatā": "медлительность",
    "vitthanatā": "скованность",
    "mudutā": "мягкость", "cittamudutā": "мягкость ума", "maddavatā": "гибкость",
    "akakkhaḷatā": "отсутствие грубости", "kakkhaḷatā": "грубость", "kathinatā": "жёсткость",
    "kammaññatā": "работоспособность", "cittakammaññatā": "работоспособность ума",
    "kammaññattaṃ": "состояние работоспособности", "bhāvo": "свойство",
    "pāguññatā": "натренированность", "cittapāguññatā": "натренированность ума",
    "paguṇattaṃ": "состояние натренированности",
    "ujutā": "прямота", "ujukatā": "прямота", "cittujukatā": "прямота ума",
    "ajimhatā": "отсутствие кривизны", "jimhatā": "кривизна", "vaṅkatā": "изогнутость",
    "kuṭilatā": "извилистость",
    # summaries (koṭṭhāsavāra / suññatavāra)
    "jhānaṃ": "медитативное погружение", "maggo": "путь", "pañcaṅgikaṃ": "пятичастный",
    "pañcaṅgiko": "пятичастный", "caturaṅgikaṃ": "четырёхчастный", "caturaṅgiko": "четырёхчастный",
    "caturaṅgiko maggo": "четырёхчастный путь",
    # headings and colophons
    "bhājanī": "разбор", "bhājanīyaṃ": "разбор", "bhāṇa": "чтение вслух", "vāro": "раздел",
    "koṭṭhāsa": "составные части", "suññata": "пустота",
    "pañcamaṃ": "пятый", "chaṭṭhaṃ": "шестой", "sattamaṃ": "седьмой", "aṭṭhamaṃ": "восьмой",
}


def lc(kw):
    return kw[:1].lower() + kw[1:]


def ch2_value(kw, kws, table=CH2):
    """Default value with the context rules settled for the cittuppāda chapters."""
    k = lc(kw)
    s = set(lc(x) for x in kws)
    if k.startswith("samaye "):                       # Yo/Yā/Yaṃ tasmiṃ samaye X ...
        return "в это время" + GAP + ch2_value(k[len("samaye "):], kws, table)
    if k == "dhamma":                                  # stem of dhammārammaṇa / dhammāyatana / dhammadhātu
        return "объекты ума" if s & {"dhammāyatanaṃ", "dhammadhātu"} else "объект ума"
    if k == "ṭhiti" and "āyu" in s:                    # jīvitindriya string
        return "сохранение"
    if k == "jīvita" and "āyu" in s:                   # jīvitaṃ inside the jīvitindriya string
        return "жизнь"
    if k == "mano" and "manosañcetanā" in s:           # manosañcetanāhāro
        return "умственный"
    if k == "sañcetanā" and "cetayitattaṃ" not in s:   # only inside manosañcetanā
        return "намерение"
    if k == "cetasikaṃ" and "adukkhamasukhaṃ" in s:    # cetasikaṃ neva sātaṃ nāsātaṃ
        return "душевное состояние"
    if k == "ujukatā" and "ujutā" in s:                # ujutā ujukatā … string: «прямота, прямизна»
        return "прямизна"
    return table[k]


# ---------------------------------------------------------------------------- MATRIX (1-matika)
# Default per keyword; segment-specific readings are overrides in map_sample_ru.py (OVERRIDES).
MATRIX = {
    "mātikā": "матрица", "duka": "пары", "dukaṃ": "пары", "antara": "промежуточный",
    "antaradukaṃ": "промежуточные пары", "piṭṭhi": "заключительный", "suttantika": "наставления",
    "abhidhamma": "Абхидхамма",
    # cluster names (stem = singular core term; plural form = plural)
    "hetu": "корень", "hetū": "корни", "āsava": "влечение", "āsavā": "влечения",
    "saṃyojana": "оковы", "saṃyojanā": "оковы", "gantha": "узы", "ganthā": "узы",
    "ogha": "поток", "oghā": "потоки", "yoga": "ярмо", "yogā": "ярма",
    "nīvaraṇa": "помеха", "nīvaraṇā": "помехи", "parāmāsa": "искажение", "parāmāsā": "искажения",
    "upādāna": "цепляние", "upādānā": "цепляния", "kilesa": "омрачение", "kilesā": "омрачения",
    # triads
    "dhammā": "явления",
    "kusalā": "благой", "kusalā dhammā": "благие явления", "akusalā": "неблагой",
    "akusalā dhammā": "неблагие явления", "abyākatā": "этически неопределённый",
    "abyākatā dhammā": "этически неопределённые явления",
    "sampayuttā": "связанный", "vippayuttā": "не связанный", "vippayuttā dhammā": "явления не связанные",
    "vedanāya": "чувство", "dukkhāya": "болезненный", "dukkhāya vedanāya": "болезненное чувство",
    "sukhāya": "приятный", "sukhāya vedanāya": "приятное чувство",
    "adukkhamasukhāya": "ни болезненный ни приятный",
    "vipākadhamma": "способный приносить результаты",
    "vipākadhammadhammā": "явления способные приносить результаты",
    "upādiṇṇa": "охваченный цеплянием", "upādiṇṇā": "охваченный цеплянием",
    "upādiṇṇā dhammā": "явления охваченные цеплянием",
    "anupādiṇṇā dhammā": "явления не охваченные цеплянием",
    "upādāniyā": "служащий объектом цепляния",
    "upādāniyā dhammā": "явления служащие объектом цепляния",
    "anupādāniyā dhammā": "явления не служащие объектом цепляния",
    "upādiṇṇupādāniyā": "охваченный цеплянием и служащий его объектом",
    "anupādiṇṇupādāniyā": "не охваченный цеплянием но служащий его объектом",
    "upādiṇṇupādāniyā dhammā": "явления охваченные цеплянием и служащие его объектом",
    "anupādiṇṇupādāniyā dhammā": "явления не охваченные цеплянием но служащие его объектом",
    "anupādiṇṇaanupādāniyā dhammā": "явления не охваченные цеплянием и не служащие его объектом",
    "saṃkiliṭṭha": "омрачённый", "saṃkiliṭṭhā": "омрачённый", "asaṃkiliṭṭha": "неомрачённый",
    "asaṃkiliṭṭhā": "неомрачённый", "saṃkiliṭṭhā dhammā": "омрачённые явления",
    "asaṃkiliṭṭhā dhammā": "неомрачённые явления",
    "saṃkilesikā": "подверженный омрачению", "saṃkilesikā dhammā": "явления подверженные омрачению",
    "asaṃkilesikā dhammā": "явления не подверженные омрачению",
    "vitakka": "направленная мысль", "vitakkā": "направленная мысль", "vicāra": "удержание мысли",
    "vicārā": "удержание мысли",
    "savitakkasavicārā dhammā": "явления с направленной мыслью и удержанием мысли",
    "avitakkavicāramattā dhammā": "явления без направленной мысли только с удержанием мысли",
    "savitakkā dhammā": "явления с направленной мыслью", "avitakkā dhammā": "явления без направленной мысли",
    "savicārā dhammā": "явления с удержанием мысли", "avicārā dhammā": "явления без удержания мысли",
    "sahagatā": "сопровождаемый", "sahagatā dhammā": "явления сопровождаемые",
    "pītisahagatā": "сопровождаемый восторгом", "sukhasahagatā": "сопровождаемый счастьем",
    "upekkhāsahagatā": "сопровождаемый невозмутимостью",
    "na pītisahagatā dhammā": "явления не сопровождаемые восторгом",
    "na sukhasahagatā dhammā": "явления не сопровождаемые счастьем",
    "na upekkhāsahagatā dhammā": "явления не сопровождаемые невозмутимостью",
    "pīti": "восторг", "sukha": "счастье", "upekkhā": "невозмутимость",
    "pītikā": "с восторгом", "sappītikā dhammā": "явления с восторгом",
    "appītikā dhammā": "явления без восторга",
    "pahātabbā": "устраняемый", "bhāvanāya pahātabbā": "устраняемый развитием ума",
    "pahātabba": "устраняться", "bhāvanāya pahātabba": "устраняться развитием ума",
    "dassanena": "видение истины", "hetukā": "чьи корни", "hetukā dhammā": "явления чьи корни",
    "ācaya": "накопление", "apacaya": "убывание", "gāmino dhammā": "явления ведущие",
    "sekkhā": "относящийся к обучающимся", "asekkhā": "относящийся к завершившим обучение",
    "parittā": "ограниченный", "parittā dhammā": "ограниченные явления", "paritta": "ограниченный",
    "mahaggatā": "возвышенный", "mahaggatā dhammā": "возвышенные явления", "mahaggata": "возвышенный",
    "appamāṇā": "безмерный", "appamāṇā dhammā": "безмерные явления", "appamāṇa": "безмерный",
    "ārammaṇā": "с … объектом", "parittārammaṇā": "с ограниченным объектом",
    "mahaggatārammaṇā": "с возвышенным объектом", "appamāṇārammaṇā": "с безмерным объектом",
    "hīnā": "низший", "hīnā dhammā": "низшие явления", "majjhimā": "средний",
    "majjhimā dhammā": "средние явления", "paṇītā": "высший", "paṇītā dhammā": "высшие явления",
    "micchatta": "ложное", "sammatta": "правильное", "niyatā": "предопределённый",
    "niyatā dhammā": "предопределённые явления",
    "magga": "путь", "adhipatino": "находящийся под главенством",
    "uppannā": "возникший", "uppannā dhammā": "возникшие явления", "uppādino": "возникнуть",
    "atītā dhammā": "прошлые явления", "anāgatā dhammā": "будущие явления",
    "paccuppannā dhammā": "настоящие явления",
    "atītārammaṇā": "с прошлым объектом", "anāgatārammaṇā": "с будущим объектом",
    "paccuppannārammaṇā": "с настоящим объектом",
    "bahiddhā": "внешний", "bahiddhā dhammā": "внешние явления",
    "sanidassana": "видимый", "anidassana": "невидимый", "sappaṭighā": "способный к соударению",
    # intermediate pairs
    "sahetukā dhammā": "явления имеющие корни", "ahetukā dhammā": "явления не имеющие корней",
    "appaccayā dhammā": "явления не имеющие условий",
    "saṅkhatā": "обусловленный", "saṅkhatā dhammā": "обусловленные явления",
    "asaṅkhatā": "необусловленный", "asaṅkhatā dhammā": "необусловленные явления",
    "sanidassanā": "видимый", "sanidassanā dhammā": "видимые явления",
    "anidassanā": "невидимый", "anidassanā dhammā": "невидимые явления",
    "sappaṭighā dhammā": "явления способные к соударению",
    "rūpino": "материальный", "rūpino dhammā": "материальные явления",
    "arūpino": "нематериальный", "arūpino dhammā": "нематериальные явления",
    "lokiyā": "мирской", "lokiyā dhammā": "мирские явления", "uttarā": "надмирский",
    "lokuttarā dhammā": "надмирские явления", "na": "не", "viññeyyā": "познаваемый",
    # gocchaka adjectives
    "sāsavā": "подверженный влечениям", "sāsavā dhammā": "явления подверженные влечениям",
    "anāsavā": "свободный от влечений", "anāsavā dhammā": "явления свободные от влечений",
    "āsavavippayuttā": "не связанный с влечениями",
    "saṃyojaniyā": "подверженный оковам", "saṃyojaniyā dhammā": "явления подверженные оковам",
    "asaṃyojaniyā dhammā": "явления не подверженные оковам",
    "saṃyojanavippayuttā": "не связанный с оковами",
    "ganthaniyā": "подверженный узам", "ganthaniyā dhammā": "явления подверженные узам",
    "aganthaniyā dhammā": "явления не подверженные узам", "ganthavippayuttā": "не связанный с узами",
    "oghaniyā": "подверженный потокам", "oghaniyā dhammā": "явления подверженные потокам",
    "anoghaniyā dhammā": "явления не подверженные потокам",
    "yoganiyā": "подверженный ярмам", "yoganiyā dhammā": "явления подверженные ярмам",
    "ayoganiyā dhammā": "явления не подверженные ярмам",
    "nīvaraṇiyā": "подверженный помехам", "nīvaraṇiyā dhammā": "явления подверженные помехам",
    "anīvaraṇiyā dhammā": "явления не подверженные помехам",
    "nīvaraṇavippayuttā": "не связанный с помехами",
    "parāmaṭṭhā": "затронутый искажениями", "parāmaṭṭhā dhammā": "явления затронутые искажениями",
    "parāmāsavippayuttā": "не связанный с искажениями",
    "upādānavippayuttā": "не связанный с цепляниями",
    "kilesavippayuttā": "не связанный с омрачениями",
    # great intermediate pairs
    "cittā": "ум", "cetasikā": "сопутствующий уму", "citta": "ум",
    "cittavippayuttā": "не связанный с умом",
    "saṃsaṭṭhā": "соединённый", "cittasaṃsaṭṭhā": "соединённый с умом", "saṃsaṭṭha": "соединённый",
    "saṃsaṭṭhā dhammā": "явления соединённые", "visaṃsaṭṭhā dhammā": "явления не соединённые",
    "samuṭṭhānā": "порождённый", "samuṭṭhāna": "порождённый", "cittasamuṭṭhānā": "порождённый умом",
    "samuṭṭhānā dhammā": "явления порождённые", "no cittasamuṭṭhānā dhammā": "явления не порождённые умом",
    "sahabhuno": "сосуществующий", "cittasahabhuno": "сосуществующий с умом",
    "cittasahabhuno dhammā": "явления сосуществующие с умом",
    "no cittasahabhuno dhammā": "явления не сосуществующие с умом",
    "anuparivattino": "следующий за", "cittānuparivattino": "следующий за умом",
    "anuparivattino dhammā": "явления следующие за",
    "cittānuparivattino dhammā": "явления следующие за умом",
    "no cittānuparivattino dhammā": "явления не следующие за умом",
    "cittasaṃsaṭṭhasamuṭṭhānā": "соединённый с умом и порождённый им",
    "saṃsaṭṭhasamuṭṭhānā dhammā": "явления соединённые … и порождённые им",
    "no cittasaṃsaṭṭhasamuṭṭhānā dhammā":
        "явления не являющиеся соединёнными с умом и порождёнными им",
    "saṃsaṭṭhasamuṭṭhānasahabhuno dhammā":
        "явления соединённые … порождённые им и сосуществующие с ним",
    "no cittasaṃsaṭṭhasamuṭṭhānasahabhuno dhammā":
        "явления не являющиеся соединёнными с умом порождёнными им и сосуществующими с ним",
    "cittasaṃsaṭṭhasamuṭṭhānānuparivattino": "соединённый с умом порождённый им и следующий за ним",
    "saṃsaṭṭhasamuṭṭhānānuparivattino dhammā":
        "явления соединённые … порождённые им и следующие за ним",
    "no cittasaṃsaṭṭhasamuṭṭhānānuparivattino dhammā":
        "явления не являющиеся соединёнными с умом порождёнными им и следующими за ним",
    "ajjhattikā": "относящийся к внутреннему", "ajjhattikā dhammā": "явления относящиеся к внутреннему",
    "bāhirā": "относящийся к внешнему", "bāhirā dhammā": "явления относящиеся к внешнему",
    "upādā": "производный", "upādā dhammā": "производные явления",
    # closing pairs
    "kāma": "чувственные желания", "kāmāvacarā": "относящийся к миру чувственных желаний",
    "avacarā": "относящийся к миру", "rūpa": "форма", "rūpāvacarā": "относящийся к миру форм",
    "arūpa": "без форм", "arūpāvacarā": "относящийся к миру без форм",
    "pariyāpannā dhammā": "явления принадлежащие к кругам существования",
    "apariyāpannā dhammā": "явления не принадлежащие к кругам существования",
    "niyyānikā": "ведущий к освобождению", "niyyānikā dhammā": "явления ведущие к освобождению",
    "sauttarā": "над которым есть высшее", "sauttarā dhammā": "явления над которыми есть высшее",
    "anuttarā": "над которым нет высшего", "anuttarā dhammā": "явления над которыми нет высшего",
    "raṇā": "борьба", "saraṇā dhammā": "явления сопряжённые с борьбой",
    "araṇā dhammā": "явления свободные от борьбы",
    # suttanta pairs
    "vijjā": "истинное знание", "avijjā": "неведение", "bhāgino dhammā": "явления причастные к",
    "vijju": "молния", "vajira": "алмаз", "upamā": "подобный", "vijjūpamā dhammā": "явления подобные молнии",
    "bālā": "свойственный глупцам", "bālā dhammā": "явления свойственные глупцам",
    "paṇḍitā": "свойственный мудрым", "paṇḍitā dhammā": "явления свойственные мудрым",
    "kaṇhā": "тёмный", "kaṇhā dhammā": "тёмные явления", "sukkā": "светлый",
    "sukkā dhammā": "светлые явления", "tapanīyā": "причиняющий мучения",
    "adhivacanā": "наименование", "nirutti": "выражение", "paññatti": "обозначение", "pathā": "путь",
    "nāmañca": "умственное", "rūpañca": "материальная форма",
    "bhava": "существование", "vibhava": "несуществование", "taṇhā": "жажда", "diṭṭhi": "воззрение",
    "sassata": "вечность", "sassatadiṭṭhi": "воззрение о вечности", "uccheda": "уничтожение",
    "ucchedadiṭṭhi": "воззрение об уничтожении", "anudiṭṭhi": "воззрение о",
    "ahirikañca": "бессовестность", "anottappañca": "отсутствие страха перед дурным",
    "hirī": "совестливость", "ottappañca": "страх перед дурным",
    "dovacassatā": "неспособность принимать наставления", "vacassatā": "принимать наставления",
    "sovacassatā": "готовность принимать наставления", "pāpa": "дурной", "mittatā": "дружба",
    "kusalatā": "умение разбираться", "āpatti": "проступок", "samāpatti": "медитативное достижение",
    "dhātu": "элемент", "manasikāra": "внимание", "manasikārakusalatā": "умение разбираться во внимании",
    "āyatana": "сфера восприятия", "paṭicca": "в зависимости от условий", "samuppāda": "возникновение",
    "aṭṭhāna": "невозможное",
    "ajjavo": "прямодушие", "maddavo": "мягкость", "khanti": "терпение", "soraccañca": "кротость",
    "sākhalyañca": "приветливость", "paṭisanthāro": "радушие",
    "indriyesu": "чувства", "gutta": "охранение", "dvāratā": "врата", "bhojane": "еда",
    "mattaññutā": "знание меры",
    "muṭṭhasaccañca": "утрата осознанности", "asampajaññañca": "отсутствие ясного понимания",
    "sampajaññañca": "ясное понимание", "sati": "осознанность",
    "paṭisaṅkhāna": "размышление", "balañca": "сила",
    "samatho": "успокоение", "samatha": "успокоение", "vipassanā": "прозрение",
    "paggāha": "напряжение сил", "paggāho": "напряжение сил", "nimittañca": "признак",
    "avikkhepo": "отсутствие отвлечения",
    "sīla": "нравственность", "vipatti": "испорченность", "sampadā": "безупречность",
    "visuddhi": "чистота", "yathā": "следовать", "padhānaṃ": "усилие",
    "saṃvego": "потрясённость", "saṃvejaniyesu": "должный потрясать", "ṭhānesu": "(no direct equivalent)",  # user 2026-11-14
    "saṃviggassa": "потрясённый", "yoniso": "вдумчивый",
    "santuṭṭhitā": "(no direct equivalent)","kusalesu": "благой", "kusalesu dhammesu": "благие явления",
    "padhānasmiṃ": "усилие",
    "vimutti": "освобождение", "khaye": "уничтожение", "ñāṇaṃ": "знание",
    "anuppāde": "невозникновение", "niṭṭhitā": "завершённый",
}


# ---------------------------------------------------------------------------- build and verify
def build_part(part, resolver):
    """resolver(bid, kw, kws) -> Russian value. Raises KeyError for an unmapped keyword."""
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
        raise SystemExit(f"{part}: unmapped keywords: {missing}")
    (HERE / f"{part}.mapped.md").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return len(lines)


def verify(part, show=50):
    a = [l.split("] ", 1) for l in (HERE / f"{part}.keywords.md").read_text(encoding="utf-8").splitlines()]
    b = [l.split("] ", 1) for l in (HERE / f"{part}.mapped.md").read_text(encoding="utf-8").splitlines()]
    assert [x[0] for x in a] == [x[0] for x in b]
    bad = [i for (i, x), (_, y) in zip(a, b)
           if [k.strip() for k in x.split(", ")] != [k.split("=", 1)[0] for k in y.split(", ")]]
    ru = read_russian(part)
    nde, miss = 0, []
    for bid, rest in b:
        bid = bid[1:]
        text = ru.get(bid)
        for pair in rest.split(", "):
            kw, v = pair.split("=", 1)
            if v == NDE:
                nde += 1
            elif text is None or not present(v, text):
                miss.append((bid, kw, v))
    print(part, "lines", len(a), "bad", bad, "| no-direct-equivalent", nde, "| presence misses", len(miss))
    for m in miss[:show]:
        print("   MISS", *m)
    return bad, nde, miss
