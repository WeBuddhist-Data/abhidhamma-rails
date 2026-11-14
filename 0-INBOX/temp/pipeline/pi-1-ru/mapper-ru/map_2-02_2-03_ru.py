"""Pāli->Russian keyword maps for pi-1 parts 2-02-cittuppadakandam and 2-03-cittuppadakandam.

usage: python -I -X utf8 map_2-02_2-03_ru.py          (writes the two <part>.mapped.md and verifies them)

Resolution order per keyword: OVERRIDES[bid][kw] -> context rules (context()) -> T (= CH2 + this script's
additions) via ch2_value. Conventions: ru-map-conventions.md; new decisions: notes-map-2-02_2-03.md.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_ru import CH2, GAP, NDE, build_part, ch2_value, lc, verify  # noqa: E402

PARTS = ["2-02-cittuppadakandam", "2-03-cittuppadakandam"]

ADD = {
    # user decision 2026-11-14 (fragment whose positive part is not a Russian word)
    "nikkhitta": NDE,
    # ---------------------------------------------------------------- headings and colophons
    "rūpāvacara": "относящийся к миру форм", "arūpāvacara": "относящийся к миру без форм",
    "catukka": "четверичный", "catukkanayo": "четверичный метод",
    "pañcaka": "пятеричный", "pañcakanayo": "пятеричный метод", "nayo": "метод",
    "paṭipadā": "способ практики", "ārammaṇāni": "виды объектов",
    "soḷasakkhattukaṃ": "шестнадцатикратный разбор", "soḷasakkhattukāni": "шестнадцатикратный разбор",
    "aṭṭhakkhattukaṃ": "восьмикратный разбор",
    "abhibhāyatanāni": "сферы преодоления", "abhibhu": "преодоление",
    "vimokkhāni": "освобождения", "vihāra": "обитель", "brahma": "божественный",
    "jhānāni": "медитативные погружения", "asubha": "непривлекательное",
    "bhūmaka": "мир",
    # ---------------------------------------------------------------- the absorption formulas
    "upapattiyā": "рождение", "maggaṃ": "путь", "upapattiyā maggaṃ": "путь к рождению",
    "bhāveti": "развивать", "maggaṃ bhāveti": "развивать путь",
    "upasampajja": "входить", "viharati": "пребывать", "upasampajja viharati": "входить" + GAP + "пребывать",
    "kasiṇaṃ": "всеохватный объект", "pathavī": "земля", "āpo": "вода", "tejo": "огонь",
    "vāyo": "воздух", "nīla": "синий", "pīta": "жёлтый", "lohita": "красный", "odāta": "белый",
    "vivicceva": "полностью уединиться", "kāmehi": "чувственные удовольствия",
    "vivicceva kāmehi": "полностью уединиться от чувственных удовольствий",
    "akusalehi": "неблагой", "akusalehi dhammehi": "неблагие явления",
    "vitakkaṃ": "направленная мысль", "vicāraṃ": "удержание мысли", "vitakka": "направленная мысль",
    "vicāra": "удержание мысли", "vicārānaṃ": "удержание мысли",
    "vivekajaṃ": "рождённый уединением", "samādhijaṃ": "рождённый сосредоточением",
    "vūpasamā": "затихание", "ajjhattaṃ": "внутренний", "sampasādanaṃ": "ясность",
    "ekodibhāvaṃ": "единение",
    "tivaṅgikaṃ": "трёхчастный", "duvaṅgikaṃ": "двухчастный",
    "duvaṅgikaṃ jhānaṃ": "двухчастное медитативное погружение",
    "pītiyā": "восторг", "virāgā": "угасание", "upekkhako": "невозмутимый",
    "upekkhako ca viharati": "пребывать невозмутимым", "sato": "осознанный",
    "sampajāno": "ясно понимающий", "sukhañca": "счастье", "kāyena": "тело",
    "paṭisaṃvedeti": "испытывать", "ariyā": "благородный", "ācikkhanti": "говорить",
    "pahānā": "устранение", "sukhassa": "приятное", "sukhassa ca pahānā": "устранение приятного",
    "dukkhassa": "болезненное", "dukkha": "болезненный", "atthaṅgamā": "исчезновение",
    "domanassānaṃ": "уныние", "pārisuddhiṃ": "чистота",
    "catutthaṃ jhānaṃ": "четвёртое медитативное погружение",
    # ways of practice and objects
    "paṭipadaṃ": "способ практики", "dukkhapaṭipadaṃ": "трудный способ практики",
    "sukha": "лёгкий", "sukhapaṭipadaṃ": "лёгкий способ практики",
    "abhiññaṃ": "высшее знание", "dandha": "медленный", "dandhābhiññaṃ": "медленное высшее знание",
    "khippa": "быстрый", "khippābhiññaṃ": "быстрое высшее знание",
    "paṭipadaṃ dandha": "способ практики" + GAP + "медленный",
    "paṭipadaṃ khippa": "способ практики" + GAP + "быстрый",
    "parittaṃ": "ограниченный", "paritta": "ограниченный", "parittāni": "ограниченный",
    "parittārammaṇaṃ": "с ограниченным объектом",
    "appamāṇaṃ": "безмерный", "appamāṇa": "безмерный", "appamāṇāni": "безмерный",
    "appamāṇārammaṇaṃ": "с безмерным объектом",
    # spheres of mastery, liberations
    "ajjhattaṃ arūpa": "не" + GAP + "материальная форма внутри себя",
    "rūpāni": "видимые формы", "saññī": "воспринимать", "rūpasaññī": "воспринимать материальную форму",
    "bahiddhā": "вовне", "abhibhuyya": "преодолеть", "jānāmi": "знать", "passāmīti": "видеть",
    "suvaṇṇa": "красивый", "dubbaṇṇāni": "некрасивый",
    "nīlāni": "синий", "pītāni": "жёлтый", "lohitakāni": "красный", "odātāni": "белый",
    "vaṇṇāni": "цвет", "nidassanāni": "вид", "nibhāsāni": "сияние",
    "rūpī": "обладать материальной формой", "subhanti": "прекрасно",
    # divine abidings, foulness
    "mettāsahagataṃ": "сопровождаемый доброжелательностью", "mettā": "доброжелательность",
    "karuṇā": "сострадание", "muditā": "сорадование",
    "uddhumātaka": "вздувшийся труп", "vinīlaka": "посиневший труп", "vipubbaka": "гноящийся труп",
    "vicchiddaka": "разрубленный труп", "vikkhāyitaka": "объеденный труп",
    "vikkhittaka": "разбросанный труп", "hata": "изрубленный", "lohitaka": "кровоточащий труп",
    "puḷavaka": "кишащий червями труп", "aṭṭhika": "скелет",
    # immaterial absorptions
    "arūpa": "мир без форм", "sabbaso": "полностью", "samatikkamā": "преодолеть",
    "samatikkamma": "преодолеть", "saññānaṃ": "восприятия", "nānatta": "разнообразие",
    "manasikārā": "внимание", "ākāsa": "пространство", "ānañca": "бесконечный",
    "ānañcāyatana": "сфера бесконечного", "ānañcāyatanaṃ": "сфера бесконечного",
    "viññāṇañca": "бесконечное сознание", "viññāṇañcāyatanaṃ": "сфера бесконечного сознания",
    "ākiñcañña": "отсутствие чего-либо", "nāsaññā": "ни невосприятие",
    # three planes
    "chanda": "желание", "adhipateyyaṃ": "преобладание", "vīmaṃsā": "пытливость",
    "hīnaṃ": "низший", "majjhimaṃ": "средний", "paṇītaṃ": "высший",
    # ================================================================ 2-03 (supramundane)
    "lokuttara": "надмирский", "lokuttarakusalaṃ": "надмирский благой ум",
    "suddhika": "простой", "suddhikapaṭipadā": "простой способ практики",
    "suññataṃ": "пустой", "mūlaka": "основанный", "mūlakapaṭipadā": "способ практики основанный на",
    "appaṇihitaṃ": "свободный от устремлений", "appaṇihita": "свобода от устремлений",
    "vīsati": "двадцать", "nayā": "методы", "adhipati": "преобладание",
    "lokuttaraṃ": "надмирский", "lokuttaraṃ jhānaṃ": "надмирское медитативное погружение",
    "lokuttaraṃ jhānaṃ bhāveti": "развивать надмирское медитативное погружение",
    "niyyānikaṃ": "ведущий к освобождению", "gāmiṃ": "ведущий", "apacaya": "убывание",
    "caya": NDE,                                            # fragment of apacaya: «убыванию» only
    "niyyānikaṃ apacayagāmiṃ": "ведущий к освобождению и ведущий к убыванию",
    "diṭṭhigatānaṃ": "приверженность воззрениям", "pahānāya": "устранение",
    "diṭṭhigatānaṃ pahānāya": "устранение приверженности воззрениям",
    "bhūmiyā": "ступень", "pattiyā": "достижение",
    "anaññātaññassāmītindriyaṃ": "способность познания непознанного", "aññāta": "познанный",
    "vācā": "речь", "ājīvo": "образ жизни",
    "eva": "полностью", "vivicca": "уединиться",               # vivicceva = «полностью уединившись»
    "magga": "путь", "aṅgaṃ": "фактор", "maggaṅgaṃ": "фактор пути",
    "sambojjhaṅgo": "фактор пробуждения", "samādhisambojjhaṅgo": "фактор пробуждения сосредоточения",
    "vīriyasambojjhaṅgo": "фактор пробуждения усердия",
    "vicayasambojjhaṅgo": "фактор пробуждения исследования",
    "viditānaṃ": "узнанный", "sacchikatānaṃ": "постигнутый непосредственно",
    "sacchikiriyāya": "непосредственное постижение", "ñātānaṃ": "познанный",
    "ārati": "отстранение", "virati": "воздержание", "paṭivirati": "полное воздержание",
    "veramaṇī": "уклонение", "kiriyā": "делание", "karaṇaṃ": "совершение",
    "ajjhāpatti": "впадение в проступок", "velā": "граница", "atikkamo": "переступание",
    "setu": "мост", "ghāto": "разрушение", "duccaritehi": "дурное поведение", "vacī": "речь",
    "samaye": "в это время", "micchā": "неправильный", "aṭṭhaṅgiko": "восьмичастный",
    # the twenty great methods (lokuttaraṃ X bhāveti)
    "khandhaṃ": "совокупность", "bojjhaṅgaṃ": "фактор пробуждения", "samathaṃ": "успокоение",
    "phassaṃ": "контакт", "dhātuṃ": "элемент", "vedanaṃ": "чувство", "paṭṭhānaṃ": "основа",
    "cetanaṃ": "намерение", "āhāraṃ": "питание", "saññaṃ": "восприятие", "iddhi": "сверхспособность",
    "āyatanaṃ": "сфера восприятия", "padhānaṃ": "усилие", "saccaṃ": "истина",
    "lokuttaraṃ maggaṃ": "надмирский путь", "lokuttaraṃ khandhaṃ": "надмирская совокупность",
    "lokuttaraṃ bojjhaṅgaṃ": "надмирский фактор пробуждения",
    "lokuttaraṃ iddhipādaṃ": "надмирская основа сверхспособностей",
    "lokuttaraṃ samathaṃ": "надмирское успокоение", "lokuttaraṃ phassaṃ": "надмирский контакт",
    "lokuttaraṃ dhātuṃ": "надмирский элемент", "lokuttaraṃ indriyaṃ": "надмирская способность",
    "lokuttaraṃ vedanaṃ": "надмирское чувство",
    "lokuttaraṃ satipaṭṭhānaṃ": "надмирская основа осознанности",
    "lokuttaraṃ cetanaṃ": "надмирское намерение", "lokuttaraṃ cittaṃ": "надмирский ум",
    "lokuttaraṃ āhāraṃ": "надмирское питание", "lokuttaraṃ saññaṃ": "надмирское восприятие",
    "lokuttaraṃ balaṃ": "надмирская сила", "lokuttaraṃ āyatanaṃ": "надмирская сфера восприятия",
    "lokuttaraṃ dhammaṃ": "надмирское явление", "lokuttaraṃ saccaṃ": "надмирская истина",
    "lokuttaraṃ maggaṃ bhāveti": "развивать надмирский путь",
    "lokuttaraṃ samathaṃ bhāveti": "развивать надмирское успокоение",
    "lokuttaraṃ phassaṃ bhāveti": "развивать надмирский контакт",
    "lokuttaraṃ vedanaṃ bhāveti": "развивать надмирское чувство",
    "lokuttaraṃ cetanaṃ bhāveti": "развивать надмирское намерение",
    "lokuttaraṃ saññaṃ bhāveti": "развивать надмирское восприятие",
    "ādhipateyyaṃ": "преобладание",
    # the higher paths
    "aññindriyaṃ": "способность окончательного знания", "aññā": "окончательное знание",
    "rāga": "страсть", "kāmarāga": "чувственная страсть", "byāpādānaṃ": "недоброжелательность",
    "tanubhāvāya": "ослабление",
    "avasesa": NDE,                                         # fragment of anavasesa-: «полного» only
    "māna": "самомнение", "uddhacca": "беспокойство", "avijjāya": "неведение",
}
T = {**CH2, **ADD}

OVERRIDES = {
    # ---- 2-02
    "1-165": {"sukhaṃ": "приятный"},        # sukhaṃ of adukkhamasukhaṃ: «ни болезненно, ни приятно»
    # ākāsānañcāyatana…saññāsahagataṃ = «с восприятием сферы …» (no upekkhāsahagataṃ in these)
    "1-273": {"sahagataṃ": "с"}, "1-274": {"sahagataṃ": "с"},
    "1-275": {"sahagataṃ": "с"}, "1-276": {"sahagataṃ": "с"},
    # ---- 2-03
    "1-300": {"kāya": "тело"},                # tīhi kāyaduccaritehi = «трёх видов дурного поведения телом»
    "1-301": {"samaye micchāājīvā ārati":     # «в это время есть отстранение от неправильного образа жизни»
              "в это время" + GAP + "отстранение от неправильного образа жизни"},
}


def context(bid, k, s):
    """Context rules (k: lower-cased keyword, s: lower-cased keyword set). None = no rule."""
    if k == "rūpa":
        if bid.startswith("1-1-"):                         # heading Rūpāvacarakusalaṃ
            return "форма"
        if "rāga" in s:                                    # rūparāga = «страсть к миру форм» (1-363)
            return "мир форм"
        if "arūpa" in s:                                   # rūpasaññānaṃ in the arūpa formula
            return "материальная форма"
        if "upapattiyā" in s:                              # rūpūpapattiyā
            return "мир форм"
    if k == "kāma" and "kāmarāga" in s:                    # kāmarāga = «чувственная страсть»
        return "чувственный"
    if k == "arūpa" and "arūpāvacara" in s:                # heading Arūpāvacarakusalaṃ
        return "без форм"
    if k == "ajjhattaṃ" and "ajjhattaṃ arūpa" in s:        # ajjhattaṃ arūpasaññī
        return "внутри себя"
    if k == "dukkha" and "dukkhapaṭipadaṃ" in s:
        return "трудный"
    if k == "āyatanāni" and "abhibhāyatanāni" in s:
        return "сферы"
    return None


def resolver_for(part):
    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        s = set(lc(x) for x in kws)
        v = context(bid, lc(kw), s)
        if v is not None:
            return v
        return ch2_value(kw, kws, T)
    return resolve


if __name__ == "__main__":
    for p in (sys.argv[1:] or PARTS):
        build_part(p, resolver_for(p))
        verify(p)
