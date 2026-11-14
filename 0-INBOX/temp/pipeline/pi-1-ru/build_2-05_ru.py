"""Build the Russian plain zero-shot of pi-1 part 2-05 (^1-1-8-0 ... ^1-582, end of the chapter on the arising of mind).

usage: python -I -X utf8 build_2-05_ru.py
Mirrors the English/Hindi 2-05 builders: each Pāli line is split at '…pe…'; every chunk is translated by fixed
rules and fixed strings below (same Pāli chunk = same Russian), then the chunks are re-joined with '…'.
Shared constants come from the approved builders build_matika_ru.py (M) and build_ch2_01_sample_ru.py (C);
importing them does not rewrite their outputs.
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_matika_ru as M  # noqa: E402
import build_ch2_01_sample_ru as C  # noqa: E402

ROOT = HERE.parents[3]
PART = "2-05-cittuppadakandam.md"
PALI = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters" / PART
OUT = ROOT / "AI_translation" / "russian" / "pi-1-russian-plain-zeroshot_split_chapters" / PART

DASH = C.DASH
PE = "…"
KUSALA, ABYAKATA = C.KUSALA, C.ABYAKATA
TASMIM = C.TASMIM

# ---- headings (terms file, verbatim) and closing lines ---------------------------------
HEAD = {
    "Lokuttaravipāka-paṭhamamaggavipākā": "Надмирские результаты действий: результаты первого пути",
    "Suddhikapaṭipadā": "Простой способ практики",            # terms file, 2-03 list
    "Suddhikasuññataṃ": "Простая пустота",
    "Suññatapaṭipadā": "Способ практики с пустотой",
    "Suddhikaappaṇihitaṃ": "Простое свободное от устремлений",
    "Appaṇihitapaṭipadā": "Способ практики со свободой от устремлений",
    "Vīsati mahānayā": "Двадцать великих методов",             # terms file, 2-03 list
    "Chandādhipateyyasuddhikapaṭipadā": "Простой способ практики при преобладании желания",
    "Chandādhipateyyasuddhikasuññatā": "Простая пустота при преобладании желания",
    "Dutiyādimaggavipāko": "Результаты второго и последующих путей",
    "Akusalavipākaabyākataṃ": "Этически неопределённое, являющееся результатом неблагих действий",
    "Akusalavipākapañcaviññāṇāni": "Пять видов сознания, являющихся результатом неблагих действий",
    "Akusalavipākamanodhātu": "Элемент ума, являющийся результатом неблагих действий",
    "Akusalavipākamanoviññāṇadhātu": "Элемент умственного сознания, являющийся результатом неблагих действий",
    "Ahetukakiriyāabyākataṃ": "Этически неопределённое функциональное без корней",
    "Kiriyāmanodhātu": "Функциональный элемент ума",
    "Kiriyāmanoviññāṇadhātusomanassasahagatā": "Функциональный элемент умственного сознания, сопровождаемый радостью",
    "Kiriyāmanoviññāṇadhātuupekkhāsahagatā":
        "Функциональный элемент умственного сознания, сопровождаемый невозмутимостью",
    "Sahetukakāmāvacarakiriyā": "Функциональный ум с корнями, относящийся к миру чувственных желаний",
    "Rūpāvacarakiriyā": "Функциональный ум, относящийся к миру форм",
    "Arūpāvacarakiriyā": "Функциональный ум, относящийся к миру без форм",
}
H_ABY_VIPAKA = "Этически неопределённые результаты действий"  # terms file: #### Abyākatavipāko (2-04)
CLOSE = {
    "Suddhikapaṭipadā.": HEAD["Suddhikapaṭipadā"] + ".",
    "Suddhikasuññataṃ.": HEAD["Suddhikasuññataṃ"] + ".",
    "Suññatapaṭipadā.": HEAD["Suññatapaṭipadā"] + ".",
    "Suddhikaappaṇihitaṃ.": HEAD["Suddhikaappaṇihitaṃ"] + ".",
    "Appaṇihitapaṭipadā.": HEAD["Appaṇihitapaṭipadā"] + ".",
    "Vīsati mahānayā.": HEAD["Vīsati mahānayā"] + ".",
    "Chandādhipateyyasuddhikapaṭipadā.": HEAD["Chandādhipateyyasuddhikapaṭipadā"] + ".",
    "Chandādhipateyyasuddhikasuññatā.": HEAD["Chandādhipateyyasuddhikasuññatā"] + ".",
    "Paṭhamamaggavipāko.": "Результат первого пути.",
    "Dutiyādimaggavipāko.": HEAD["Dutiyādimaggavipāko"] + ".",
    "Lokuttaravipāko.": "Надмирский результат действий.",
    "Akusalavipākapañcaviññāṇāni.": HEAD["Akusalavipākapañcaviññāṇāni"] + ".",
    "Akusalavipākā manodhātu.": HEAD["Akusalavipākamanodhātu"] + ".",
    "Akusalavipākā manoviññāṇadhātu.": HEAD["Akusalavipākamanoviññāṇadhātu"] + ".",
    "Vipākā abyākatā.": H_ABY_VIPAKA + ".",
    "Kiriyā manodhātu.": HEAD["Kiriyāmanodhātu"] + ".",
    "Kiriyā manoviññāṇadhātu somanassasahagatā.": HEAD["Kiriyāmanoviññāṇadhātusomanassasahagatā"] + ".",
    "Kiriyā manoviññāṇadhātu upekkhāsahagatā.": HEAD["Kiriyāmanoviññāṇadhātuupekkhāsahagatā"] + ".",
    "Ahetukā kiriyā abyākatā.": HEAD["Ahetukakiriyāabyākataṃ"] + ".",
    "Sahetukā kāmāvacarakiriyā.": HEAD["Sahetukakāmāvacarakiriyā"] + ".",
    "Rūpāvacarakiriyā.": HEAD["Rūpāvacarakiriyā"] + ".",
    "Arūpāvacarakiriyā.": HEAD["Arūpāvacarakiriyā"] + ".",
    "Kiriyā abyākatā.": "Этически неопределённое функциональное.",
    "Cittuppādakaṇḍaṃ niṭṭhitaṃ.": "Раздел о возникновении ума завершён.",  # terms file (proposed form)
}

# ---- factor names: sample names + new ones (nominative, instrumental) -------------------
NAMES_C = dict(C.NAMES_C)
NAMES_C.update({
    "dukkhaṃ": ("боль", "болью"),
    "dukkhindriyaṃ": ("способность боли", "способностью боли"),
    "upekkhā": ("невозмутимость", "невозмутимостью"),
    "upekkhindriyaṃ": ("способность невозмутимости", "способностью невозмутимости"),
    "aññindriyaṃ": ("способность окончательного знания", "способностью окончательного знания"),
    "aññātāvindriyaṃ": ("способность обладателя окончательного знания",
                        "способностью обладателя окончательного знания"),
    "saṅkhārakkhandho": ("совокупность формирующих факторов", "совокупностью формирующих факторов"),
})
N = {k: v[0] for k, v in NAMES_C.items()}
INS = {k: v[1] for k, v in NAMES_C.items()}


def Q(key):
    """'Katamo/Katamā/Katamaṃ tasmiṃ samaye X hoti?' (template of C.Q)"""
    return f"Что {TASMIM} является {INS[key]}?"


def A(s, key, mid=""):
    """'Yo/Yā/Yaṃ tasmiṃ samaye [mid] S – ayaṃ/idaṃ tasmiṃ samaye X hoti.' (template of C.A)"""
    return f"То, что {TASMIM}{mid} есть {s}, {DASH} это и есть {N[key]} {TASMIM}."


assert Q("phasso") == C.Q("phasso") and A(C.S_PHASSA, "phasso") == C.A(C.S_PHASSA, "phasso")


def QA(key, s, mid=""):
    return Q(key) + " " + A(s, key, mid)


def strip_dot(s):
    assert s.endswith("."), s
    return s[:-1]


# ---- fixed formula strings -------------------------------------------------------------
Q_ABY = M.QUESTION(ABYAKATA)              # Какие явления являются этически неопределёнными?
ANS_ABY = M.ANSWER(ABYAKATA)              # это этически неопределённые явления.
ANS_KUS = M.ANSWER(KUSALA)                # это благие явления.
YEVA_ABY = C.YEVAPANA(ABYAKATA)           # любые другие … в это время, – это этически неопределённые явления.

# The world-transcending clause is shared with part 2-03; its strings are copied byte-for-byte from
# build_2-03_ru.py (LEADS, LEADS_M, STAGE, J1/J5 wording, IN_J, PP, EMPTY, DESIRELESS, ADHI, TWENTY_OBJ).
WHEN = "В то время, когда человек развивает"          # Yasmiṃ samaye … bhāveti
NIY_N = "ведущее к освобождению и ведущее к убыванию"  # niyyānikaṃ apacayagāmiṃ (with jhānaṃ) [2-03 LEADS]
NIY_M = "ведущий к освобождению и ведущий к убыванию"  # (with cittaṃ) [2-03 LEADS_M]
JHANA_LOK = "надмирское медитативное погружение"        # lokuttaraṃ jhānaṃ
STAGE = {  # [2-03 STAGE]
    1: "для устранения приверженности воззрениям, для достижения первой ступени",
    2: "для ослабления чувственной страсти и недоброжелательности, для достижения второй ступени",
    3: "для полного устранения чувственной страсти и недоброжелательности, для достижения третьей ступени",
    4: ("для полного устранения страсти к миру форм, страсти к миру без форм, самомнения, беспокойства "
        "и неведения, для достижения четвёртой ступени"),
}
VIV = "отстранившись от чувственных удовольствий"                    # vivicceva kāmehi [2-03 J1]
VUP = "с успокоением направленной мысли и удержания мысли"          # vitakkavicārānaṃ vūpasamā [2-03 J5]
LOK_KUS = f"{WHEN} {JHANA_LOK}, {NIY_N}"
VIPAKA_OPEN = ("когда в результате того, что было совершено и развито это же надмирское благое медитативное "
               "погружение, человек, " + VIV)
# word order of the 2-04 result frame («вследствие того, что было совершено и накоплено благое действие, …,
# возникает зрительное сознание как его результат, …»)
AKUS_KAMMA = "В то время, когда вследствие того, что было совершено и накоплено неблагое действие, возникает"
AS_RESULT = "как его результат"                    # vipākaṃ / vipākā (2-04)
KIRIYA_M = "функциональный, не являющийся ни благим, ни неблагим, ни результатом действий"
KIRIYA_N = "функциональное, не являющееся ни благим, ни неблагим, ни результатом действий"
DITTHA = "для приятного пребывания в этой жизни"                    # diṭṭhadhammasukhavihāraṃ
KIRIYA_JH = KIRIYA_N + ", " + DITTHA
OBJ_M = {  # with «элемент» (masculine)
    "rūpārammaṇā vā": "имеющий объектом видимую форму",
}
OR_TOUCH = "или осязаемое"                       # phoṭṭhabbārammaṇā vā (after …)
OR_DHAMMA = "или объект ума"                     # dhammārammaṇā vā (after …)
YAM_YAM = "или что бы то ни было"                # yaṃ yaṃ vā panārabbha (C.ARAMMANA)
assert C.ARAMMANA.endswith(f"{OR_TOUCH}, {OR_DHAMMA}, {YAM_YAM}")
THERE_CONTACT = f"{TASMIM} есть {N['phasso']}"  # tasmiṃ samaye phasso hoti

ORD = {"paṭhamaṃ": "первого", "dutiyaṃ": "второго", "tatiyaṃ": "третьего", "catutthaṃ": "четвёртого",
       "pañcamaṃ": "пятого"}
JH_GEN = "медитативного погружения"
ENTER = "и пребывает в нём"                      # upasampajja viharati (after «достигает … погружения»)
# path attributes (they qualify jhānaṃ), as in 2-03: after «… и пребывает в нём» comes «в погружении …»
# (prepositional case: «с …» / «на …» phrases, adjectives «пустом», «свободном от устремлений»);
# alone, suññataṃ is «в пустом погружении» (2-03 ^1-343). A run of chunks shares one «в погружении».
IN_J = "в погружении"                                   # [2-03 IN_J]
EMPTY = "пустом"                                        # [2-03 EMPTY]
PATIPADA = {  # [2-03 PP]
    "dukkhapaṭipadaṃ dandhābhiññaṃ": "с болезненным способом практики и медленным высшим знанием",
    "dukkhapaṭipadaṃ khippābhiññaṃ": "с болезненным способом практики и быстрым высшим знанием",
    "sukhapaṭipadaṃ dandhābhiññaṃ": "с приятным способом практики и медленным высшим знанием",
    "sukhapaṭipadaṃ khippābhiññaṃ": "с приятным способом практики и быстрым высшим знанием",
}
ATTR1 = {
    "suññataṃ": EMPTY,
    "animittaṃ": "не имеющем признаков",                 # new (2-03 has no animitta)
    "appaṇihitaṃ": "свободном от устремлений",           # [2-03 DESIRELESS]
    "chandādhipateyyaṃ": "при преобладании желания",     # [2-03 ADHI]
    "vīriyādhipateyyaṃ": "при преобладании усердия",
    "cittādhipateyyaṃ": "при преобладании ума",
    "vīmaṃsādhipateyyaṃ": "при преобладании исследования",
    "pathavīkasiṇaṃ": "на всеохватном объекте земли",    # kasiṇa = всеохватный объект (terms file, 2-02 heading)
}
LABEL = {"kusalaṃ": " (благое)", "vipāko": " (результат)"}
TWENTY = {  # lokuttaraṃ X bhāveti
    "maggaṃ": "надмирский путь",
    "satipaṭṭhānaṃ": "надмирскую основу осознанности",
    "sammappadhānaṃ": "надмирское правильное усилие",
    "iddhipādaṃ": "надмирскую основу сверхспособностей",
    "indriyaṃ": "надмирскую способность",
    "balaṃ": "надмирскую силу",
    "bojjhaṅgaṃ": "надмирский фактор пробуждения",
    "saccaṃ": "надмирскую истину",
    "samathaṃ": "надмирское успокоение",
    "dhammaṃ": "надмирское явление",
    "khandhaṃ": "надмирскую совокупность",
    "āyatanaṃ": "надмирскую сферу восприятия",
    "dhātuṃ": "надмирский элемент",
    "āhāraṃ": "надмирское питание",
    "phassaṃ": "надмирский контакт",
    "vedanaṃ": "надмирское чувство",
    "saññaṃ": "надмирское восприятие",
    "cetanaṃ": "надмирское намерение",
    "cittaṃ": "надмирский ум",
}
# immaterial-sphere pieces: the wording of the 2-01/2-02 builder (build_2-01_2-02_ru.py) for the same Pāli
ARUPA = {
    "sabbaso rūpasaññānaṃ samatikkamā paṭighasaññānaṃ atthaṅgamā nānattasaññānaṃ amanasikārā ākāsānañcāyatanasaññāsahagataṃ":
        "полностью преодолев восприятия материальной формы, с исчезновением восприятий соударения, "
        "не уделяя внимания восприятиям разнообразия, с восприятием сферы бесконечного пространства",
    "sabbaso ākāsānañcāyatanaṃ samatikkamma viññāṇañcāyatanasaññāsahagataṃ":
        "полностью преодолев сферу бесконечного пространства, с восприятием сферы бесконечного сознания",
    "sabbaso viññāṇañcāyatanaṃ samatikkamma ākiñcaññāyatanasaññāsahagataṃ":
        "полностью преодолев сферу бесконечного сознания, с восприятием сферы отсутствия чего-либо",
    "sabbaso ākiñcaññāyatanaṃ samatikkamma nevasaññānāsaññāyatanasaññāsahagataṃ":
        "полностью преодолев сферу отсутствия чего-либо, с восприятием сферы ни восприятия, ни невосприятия",
}
SUKHA_PAHANA = "и с устранением приятного"        # (ca) sukhassa ca pahānā (2-02: «с устранением приятного»)
CITTA_KIND = {  # sahetuka kiriyā (with «элемент», masculine)
    "somanassasahagatā ñāṇasampayuttā": "сопровождаемый радостью и связанный со знанием",
    "somanassasahagatā ñāṇasampayuttā sasaṅkhārena": "сопровождаемый радостью и связанный со знанием, с побуждением",
    "somanassasahagatā ñāṇavippayuttā": "сопровождаемый радостью и не связанный со знанием",
    "somanassasahagatā ñāṇavippayuttā sasaṅkhārena":
        "сопровождаемый радостью и не связанный со знанием, с побуждением",
    "upekkhāsahagatā ñāṇasampayuttā": "сопровождаемый невозмутимостью и связанный со знанием",
    "upekkhāsahagatā ñāṇasampayuttā sasaṅkhārena":
        "сопровождаемый невозмутимостью и связанный со знанием, с побуждением",
    "upekkhāsahagatā ñāṇavippayuttā": "сопровождаемый невозмутимостью и не связанный со знанием",
    "upekkhāsahagatā ñāṇavippayuttā sasaṅkhārena":
        "сопровождаемый невозмутимостью и не связанный со знанием, с побуждением",
}
# the masculine form of the sample's ACC_SOMA_NANA (neuter «ум» is masculine too: identical)
assert CITTA_KIND["somanassasahagatā ñāṇasampayuttā"] == C.ACC_SOMA_NANA

# body-pain string: the painful counterpart of the sample's sāta/sukha string
P_KAYA_DUKKHA = ("kāyikaṃ asātaṃ kāyikaṃ dukkhaṃ kāyasamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ "
                 "kāyasamphassajā asātā dukkhā vedanā")
S_KAYA_DUKKHA = ("телесная безотрадность, телесная боль, рождённое контактом тела безотрадное и болезненное "
                 "переживание, рождённое контактом тела безотрадное и болезненное чувство")
TAJJA_KAYA = "рождённое контактом соответствующего элемента осязательного сознания"
# shortened strings (functional mind: without the path factor at the end)
SAM_TAIL, VIR_TAIL = ", " + C.N["sammāsamādhi"], ", " + C.N["sammāvāyāmo"]
assert C.S_SAMADHI.endswith(SAM_TAIL) and C.S_VIRIYA.endswith(VIR_TAIL)
S_SAMADHI_SHORT = C.S_SAMADHI[: -len(SAM_TAIL)]
S_VIRIYA_SHORT = C.S_VIRIYA[: -len(VIR_TAIL)]
P_SAMADHI_SHORT = ("cittassa ṭhiti saṇṭhiti avaṭṭhiti avisāhāro avikkhepo avisāhaṭamānasatā samatho "
                   "samādhindriyaṃ samādhibalaṃ")
P_VIRIYA_SHORT = ("cetasiko vīriyārambho nikkamo parakkamo uyyāmo vāyāmo ussāho ussoḷhī thāmo dhiti "
                  "asithilaparakkamatā anikkhittachandatā anikkhittadhuratā dhurasampaggāho vīriyaṃ "
                  "vīriyindriyaṃ vīriyabalaṃ")
assert P_SAMADHI_SHORT + " sammāsamādhi" in C.STRINGS and P_VIRIYA_SHORT + " sammāvāyāmo" in C.STRINGS
P_PANNA = [k for k in C.STRINGS if k.startswith("paññā ")][0]
P_PATH_TAIL = "dhammavicayasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ"
PATH_TAIL = "фактор пробуждения исследования явлений, фактор пути, принадлежащее к пути"
ANNA = "окончательное знание"                                        # aññā (before the paññā string)
G_ANNATAVI = "у этих явлений, обладающих окончательным знанием"     # tesaṃ aññātāvīnaṃ dhammānaṃ
APART = "кроме совокупности чувств, кроме совокупности восприятия, кроме совокупности сознания"
KOT_AGGR = (f"И {TASMIM} есть четыре совокупности, есть две сферы восприятия, есть два элемента, "
            "есть три вида питания, есть {n}, есть один контакт")
KOT_N = {"tīṇindriyāni": "три способности", "pañcindriyāni": "пять способностей"}
KOT_TAIL = "есть один {e}, есть одна сфера объектов ума, есть один элемент объектов ума; или же "
ELEM = {"kāyaviññāṇadhātu": "элемент осязательного сознания", "manodhātu": "элемент ума",
        "manoviññāṇadhātu": "элемент умственного сознания"}
YEVA_P = ("ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā – ime dhammā abyākatā")


def stage_open(n, after):
    return f"{Q_ABY} {LOK_KUS}, {STAGE[n]} {after}"


EXACT = {
    ".": ".",
    "avikkhepo hoti": "есть " + N["avikkhepo"],
    "aññindriyaṃ hoti": "есть " + N["aññindriyaṃ"],
    "aññātāvindriyaṃ hoti": "есть " + N["aññātāvindriyaṃ"],
    "ime dhammā kusalā": strip_dot(ANS_KUS),
    "ime dhammā abyākatā.": ANS_ABY,
    "ime dhammā abyākatā": strip_dot(ANS_ABY),
    YEVA_P + ".": "или же " + YEVA_ABY,
    "alobho abyākatamūlaṃ": N["alobho"] + ", этически неопределённый корень",
    "adoso abyākatamūlaṃ": N["adoso"] + ", этически неопределённый корень",
    "amoho abyākatamūlaṃ": N["amoho"] + ", этически неопределённый корень",
    # world-transcending openers
    "Katame dhammā abyākatā? Yasmiṃ samaye lokuttaraṃ jhānaṃ bhāveti niyyānikaṃ apacayagāmiṃ diṭṭhigatānaṃ "
    "pahānāya paṭhamāya bhūmiyā pattiyā vivicceva kāmehi": stage_open(1, "и, " + VIV),
    "Katame dhammā abyākatā? Yasmiṃ samaye lokuttaraṃ jhānaṃ bhāveti niyyānikaṃ apacayagāmiṃ diṭṭhigatānaṃ "
    "pahānāya paṭhamāya bhūmiyā pattiyā vitakkavicārānaṃ vūpasamā": stage_open(1, "и " + VUP),
    # (stage_open: no comma before «и», as in 2-03 CL)
    "ime dhammā kusalā. Tasseva lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ vivicceva kāmehi":
        ANS_KUS + " " + VIPAKA_OPEN[0].upper() + VIPAKA_OPEN[1:],
    # ^1-528: the Pāli has no full stop after kusalā (translated as written: semicolon)
    "ime dhammā kusalā tasseva lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ vivicceva kāmehi":
        strip_dot(ANS_KUS) + "; " + VIPAKA_OPEN,
    "Katame dhammā abyākatā? Yasmiṃ samaye lokuttaraṃ maggaṃ bhāveti":
        f"{Q_ABY} {WHEN} {TWENTY['maggaṃ']}",
    "lokuttaraṃ cittaṃ bhāveti niyyānikaṃ apacayagāmiṃ diṭṭhigatānaṃ pahānāya paṭhamāya bhūmiyā pattiyā "
    "vivicceva kāmehi":
        f"развивает {TWENTY['cittaṃ']}, {NIY_M}, {STAGE[1]} и, {VIV}",
    "Katame dhammā abyākatā? Yasmiṃ samaye lokuttaraṃ jhānaṃ bhāveti niyyānikaṃ apacayagāmiṃ "
    "kāmarāgabyāpādānaṃ tanubhāvāya dutiyāya bhūmiyā pattiyā":
        f"{Q_ABY} {LOK_KUS}, {STAGE[2]}",
    # "kāmarā gabyāpādānaṃ": broken word in the source, read as kāmarāgabyāpādānaṃ (plain spelling slip)
    "kāmarā gabyāpādānaṃ anavasesappahānāya tatiyāya bhūmiyā pattiyā": STAGE[3],
    "rūparāgaarūparāgamānauddhaccaavijjāya anavasesappahānāya catutthāya bhūmiyā pattiyā vivicceva kāmehi":
        f"{STAGE[4]} и, {VIV}",
    # Q/A
    "Katamo tasmiṃ samaye phasso hoti? Yo tasmiṃ samaye phasso phusanā saṃphusanā saṃphusitattaṃ – "
    "ayaṃ tasmiṃ samaye phasso hoti": strip_dot(QA("phasso", C.S_PHASSA)),
    "Katamo tasmiṃ samaye phasso hoti? Yo tasmiṃ samaye phasso phusanā saṃphusanā saṃphusitattaṃ – "
    "ayaṃ tasmiṃ samaye phasso hoti.": QA("phasso", C.S_PHASSA),
    "Katamaṃ tasmiṃ samaye aññātāvindriyaṃ hoti? Yā tesaṃ aññātāvīnaṃ dhammānaṃ aññā " + P_PANNA + " "
    + P_PATH_TAIL + " – idaṃ tasmiṃ samaye aññātāvindriyaṃ hoti":
        Q("aññātāvindriyaṃ") + f" То, что {G_ANNATAVI}, есть {ANNA}, {C.S_PANNA}, {PATH_TAIL}, {DASH} "
        f"это и есть {N['aññātāvindriyaṃ']} {TASMIM}",
    # unwholesome results: the five kinds of consciousness
    "Katame dhammā abyākatā? Yasmiṃ samaye akusalassa kammassa katattā upacitattā vipākaṃ cakkhuviññāṇaṃ "
    "uppannaṃ hoti upekkhāsahagataṃ rūpārammaṇaṃ":
        f"{Q_ABY} {AKUS_KAMMA} зрительное сознание {AS_RESULT}, сопровождаемое невозмутимостью, "
        "имеющее объектом видимую форму",
    "sotaviññāṇaṃ uppannaṃ hoti upekkhāsahagataṃ saddārammaṇaṃ":
        "возникает слуховое сознание, сопровождаемое невозмутимостью, имеющее объектом звук",
    "ghānaviññāṇaṃ uppannaṃ hoti upekkhāsahagataṃ gandhārammaṇaṃ":
        "возникает обонятельное сознание, сопровождаемое невозмутимостью, имеющее объектом запах",
    "jivhāviññāṇaṃ uppannaṃ hoti upekkhāsahagataṃ rasārammaṇaṃ":
        "возникает вкусовое сознание, сопровождаемое невозмутимостью, имеющее объектом вкус",
    "Katamā tasmiṃ samaye vedanā hoti? Yaṃ tasmiṃ samaye tajjākāyaviññāṇadhātusamphassajaṃ " + P_KAYA_DUKKHA
    + " – ayaṃ tasmiṃ samaye vedanā hoti":
        strip_dot(QA("vedanā", S_KAYA_DUKKHA, ", " + TAJJA_KAYA + ",")),
    "Katamaṃ tasmiṃ samaye dukkhaṃ hoti? Yaṃ tasmiṃ samaye " + P_KAYA_DUKKHA + " – idaṃ tasmiṃ samaye dukkhaṃ hoti":
        strip_dot(QA("dukkhaṃ", S_KAYA_DUKKHA)),
    "Katamaṃ tasmiṃ samaye dukkhindriyaṃ hoti? Yaṃ tasmiṃ samaye " + P_KAYA_DUKKHA
    + " – idaṃ tasmiṃ samaye dukkhindriyaṃ hoti":
        strip_dot(QA("dukkhindriyaṃ", S_KAYA_DUKKHA)),
    "Tasmiṃ kho pana samaye cattāro khandhā honti, dvāyatanāni honti, dve dhātuyo honti, tayo āhārā honti, "
    "tīṇindriyāni honti, eko phasso hoti": KOT_AGGR.format(n=KOT_N["tīṇindriyāni"]),
    "Tasmiṃ kho pana samaye cattāro khandhā honti, dvāyatanāni honti, dve dhātuyo honti, tayo āhārā honti, "
    "pañcindriyāni honti, eko phasso hoti": KOT_AGGR.format(n=KOT_N["pañcindriyāni"]),
    # unwholesome results: mind element, mind-consciousness element
    "Katame dhammā abyākatā? Yasmiṃ samaye akusalassa kammassa katattā upacitattā vipākā manodhātu uppannā "
    "hoti upekkhāsahagatā rūpārammaṇā vā":
        f"{Q_ABY} {AKUS_KAMMA} {ELEM['manodhātu']} {AS_RESULT}, сопровождаемый невозмутимостью, "
        + OBJ_M["rūpārammaṇā vā"],
    "Katame dhammā abyākatā? Yasmiṃ samaye akusalassa kammassa katattā upacitattā vipākā manoviññāṇadhātu "
    "uppannā hoti upekkhāsahagatā rūpārammaṇā vā":
        f"{Q_ABY} {AKUS_KAMMA} {ELEM['manoviññāṇadhātu']} {AS_RESULT}, сопровождаемый "
        "невозмутимостью, " + OBJ_M["rūpārammaṇā vā"],
    # functional
    "Katame dhammā abyākatā? Yasmiṃ samaye manodhātu uppannā hoti kiriyā neva kusalā nākusalā na ca "
    "kammavipākā upekkhāsahagatā rūpārammaṇā vā":
        f"{Q_ABY} В то время, когда возникает {ELEM['manodhātu']}, {KIRIYA_M}, сопровождаемый невозмутимостью, "
        + OBJ_M["rūpārammaṇā vā"],
    "Katame dhammā abyākatā? Yasmiṃ samaye manoviññāṇadhātu uppannā hoti kiriyā neva kusalā nākusalā na ca "
    "kammavipākā somanassasahagatā rūpārammaṇā vā":
        f"{Q_ABY} В то время, когда возникает {ELEM['manoviññāṇadhātu']}, {KIRIYA_M}, сопровождаемый радостью, "
        + OBJ_M["rūpārammaṇā vā"],
    "Katame dhammā abyākatā? Yasmiṃ samaye manoviññāṇadhātu uppannā hoti kiriyā neva kusalā nākusalā na ca "
    "kammavipākā upekkhāsahagatā rūpārammaṇā vā":
        f"{Q_ABY} В то время, когда возникает {ELEM['manoviññāṇadhātu']}, {KIRIYA_M}, сопровождаемый "
        "невозмутимостью, " + OBJ_M["rūpārammaṇā vā"],
    "Katamā tasmiṃ samaye cittassekaggatā hoti? Yā tasmiṃ samaye " + P_SAMADHI_SHORT
    + " – ayaṃ tasmiṃ samaye cittassekaggatā hoti.": QA("cittassekaggatā", S_SAMADHI_SHORT),
    "Katamaṃ tasmiṃ samaye vīriyindriyaṃ hoti? Yo tasmiṃ samaye " + P_VIRIYA_SHORT
    + " – idaṃ tasmiṃ samaye vīriyindriyaṃ hoti.": QA("vīriyindriyaṃ", S_VIRIYA_SHORT),
    "Katamaṃ tasmiṃ samaye samādhindriyaṃ hoti? Yā tasmiṃ samaye " + P_SAMADHI_SHORT
    + " – idaṃ tasmiṃ samaye samādhindriyaṃ hoti": strip_dot(QA("samādhindriyaṃ", S_SAMADHI_SHORT)),
    "Katame dhammā abyākatā? Yasmiṃ samaye manoviññāṇadhātu uppannā hoti kiriyā neva kusalā nākusalā na ca "
    "kammavipākā somanassasahagatā ñāṇasampayuttā":
        f"{Q_ABY} В то время, когда возникает {ELEM['manoviññāṇadhātu']}, {KIRIYA_M}, "
        + CITTA_KIND["somanassasahagatā ñāṇasampayuttā"],
    "upekkhāsahagatā ñāṇavippayuttā sasaṅkhārena rūpārammaṇā vā":
        CITTA_KIND["upekkhāsahagatā ñāṇavippayuttā sasaṅkhārena"] + ", " + OBJ_M["rūpārammaṇā vā"],
    "dhammārammaṇā vā yaṃ yaṃ vā panārabbha, tasmiṃ samaye phasso hoti":
        f"{OR_DHAMMA}, {YAM_YAM}, {THERE_CONTACT}",
    # fine-material and immaterial functional absorption
    "Katame dhammā abyākatā? Yasmiṃ samaye rūpāvacaraṃ jhānaṃ bhāveti kiriyaṃ neva kusalaṃ nākusalaṃ na ca "
    "kammavipākaṃ diṭṭhadhammasukhavihāraṃ vivicceva kāmehi":
        f"{Q_ABY} {WHEN} медитативное погружение, относящееся к миру форм, {KIRIYA_JH} и, {VIV}",
    "Katame dhammā abyākatā? Yasmiṃ samaye rūpāvacaraṃ jhānaṃ bhāveti kiriyaṃ neva kusalaṃ nākusalaṃ na ca "
    "kammavipākaṃ diṭṭhadhammasukhavihāraṃ vitakkavicārānaṃ vūpasamā":
        f"{Q_ABY} {WHEN} медитативное погружение, относящееся к миру форм, {KIRIYA_JH} и {VUP}",
}
for k, v in CITTA_KIND.items():
    EXACT.setdefault(k, v)
for k, v in TWENTY.items():
    EXACT.setdefault(f"lokuttaraṃ {k} bhāveti", "развивает " + v)
for k, v in ARUPA.items():
    EXACT["Katame dhammā abyākatā? Yasmiṃ samaye arūpāvacaraṃ jhānaṃ bhāveti kiriyaṃ neva kusalaṃ nākusalaṃ "
          "na ca kammavipākaṃ diṭṭhadhammasukhavihāraṃ " + k + " sukhassa ca pahānā"] = \
        f"{Q_ABY} {WHEN} медитативное погружение, относящееся к миру без форм, {KIRIYA_JH}, {v}, {SUKHA_PAHANA}"

RE_PATH = re.compile(r"^(?:(?P<ord>paṭhamaṃ|dutiyaṃ|tatiyaṃ|catutthaṃ|pañcamaṃ) jhānaṃ"
                     r"(?P<enter> upasampajja viharati)?,?)?\s*(?P<attrs>.*?)"
                     r"(?P<tail>,? ?tasmiṃ samaye phasso hoti)?$")
RE_LIST = re.compile(r"^(?P<pre>.*?), tasmiṃ samaye (?P<list>(?:\S+ hoti,? ?)+); ye vā pana tasmiṃ samaye aññepi "
                     r"atthi paṭiccasamuppannā arūpino dhammā – ime dhammā abyākatā(?P<dot>\.?)$")
RE_SANKHARA = re.compile(r"^Katamo tasmiṃ samaye saṅkhārakkhandho hoti\? (?P<list>[^;]+); ye vā pana tasmiṃ samaye "
                         r"aññepi atthi paṭiccasamuppannā arūpino dhammā ṭhapetvā vedanākkhandhaṃ ṭhapetvā "
                         r"saññākkhandhaṃ ṭhapetvā viññāṇakkhandhaṃ – ayaṃ tasmiṃ samaye saṅkhārakkhandho hoti$")
RE_KOT_TAIL = re.compile(r"^ekā (?P<e>\S+) hoti, ekaṃ dhammāyatanaṃ hoti, ekā dhammadhātu hoti; " + re.escape(YEVA_P) + "$")
PRE = {
    "kāyaviññāṇaṃ uppannaṃ hoti dukkhasahagataṃ phoṭṭhabbārammaṇaṃ":
        "возникает осязательное сознание, сопровождаемое болью, имеющее объектом осязаемое",
    "phoṭṭhabbārammaṇā vā yaṃ yaṃ vā panārabbha": f"{OR_TOUCH}, {YAM_YAM}",
    "dhammārammaṇā vā yaṃ yaṃ vā panārabbha": f"{OR_DHAMMA}, {YAM_YAM}",
}


def attrs_ru(s):
    """Path attributes, e.g. 'dukkhapaṭipadaṃ dandhābhiññaṃ suññataṃ' -> list of Russian phrases."""
    words, out, i = s.split(), [], 0
    while i < len(words):
        two = " ".join(words[i:i + 2])
        if two in PATIPADA:
            out.append(PATIPADA[two]); i += 2
        elif words[i] in ATTR1:
            out.append(ATTR1[words[i]]); i += 1
        else:
            raise KeyError(f"attr? {words[i]!r} in {s!r}")
    return out


def path_chunk(m):
    attrs, label = m["attrs"].strip(), ""
    for lab in LABEL:
        if attrs.endswith("nti " + lab):
            attrs = attrs[: -len("nti " + lab)] + "ṃ"
            label = LABEL[lab]
    phrases = attrs_ru(attrs) if attrs else []
    if m["ord"]:
        out = f"{ORD[m['ord']]} {JH_GEN}"
        if m["enter"]:
            out = f"достигает {out} {ENTER}"
            if phrases:
                p0, rest = phrases[0], phrases[1:]
                if p0 == EMPTY:
                    q = f"в {EMPTY} погружении"                   # 2-03 ^1-343
                elif p0.startswith(("с ", "на ")):
                    q = f"{IN_J} {p0}"                            # 2-03 ^1-277
                else:
                    q = f"{IN_J}, {p0}"                           # 2-03 ^1-350
                out += ", " + q + "".join(", " + p for p in rest)
        else:
            assert not phrases, m.group(0)
    else:
        out = ", ".join(phrases)
    out += label
    if m["tail"]:
        out += ", " + THERE_CONTACT
    return out


def tr_chunk(c):
    if c in EXACT:
        return EXACT[c]
    m = RE_LIST.match(c)
    if m:
        names = [w for w in re.split(r"\s*hoti,?\s*", m["list"]) if w]
        return (PRE[m["pre"]] + f", {TASMIM} " + ", ".join("есть " + N[w] for w in names)
                + "; или же " + (YEVA_ABY if m["dot"] else strip_dot(YEVA_ABY)))
    m = RE_KOT_TAIL.match(c)
    if m:
        return KOT_TAIL.format(e=ELEM[m["e"]]) + strip_dot(YEVA_ABY)
    m = RE_SANKHARA.match(c)
    if m:
        names = ", ".join(N[w[0].lower() + w[1:]] for w in m["list"].split())
        return (Q("saṅkhārakkhandho") + " " + names[0].upper() + names[1:] + "; или же "
                + C.YEVAPANA_BODY + ", " + APART + f", {DASH} это и есть {N['saṅkhārakkhandho']} {TASMIM}")
    m = RE_PATH.match(c)
    if m and (m["ord"] or m["attrs"] or m["tail"]):
        return path_chunk(m)
    raise KeyError(f"no rule for chunk: {c!r}")


def tr_line(line):
    if line in CLOSE:
        return CLOSE[line]
    chunks = [c.strip() for c in line.split("…pe…")]
    ru = [tr_chunk(c) for c in chunks]
    out = ru[0]
    for r in ru[1:]:
        out += PE + ("" if r == "." else " ") + r
    return out[0].upper() + out[1:]


def build():
    out_lines = []
    for line in PALI.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            out_lines.append("")
            continue
        m = re.match(r"^(.*?)(\s*\^[0-9A-Za-z-]+)?$", line)
        body, bid = m.group(1), m.group(2) or ""
        bid = bid.strip()
        if body.startswith("#"):
            hashes, title = body.split(" ", 1)
            out_lines.append(f"{hashes} {HEAD[title]}" + (f" {bid}" if bid else ""))
        else:
            out_lines.append(tr_line(body) + (f" {bid}" if bid else ""))
    text = "\n".join(out_lines).rstrip("\n") + "\n"
    assert "—" not in text and ":-" not in text and "\n\n\n" not in text
    return text


if __name__ == "__main__":
    text = build()
    OUT.write_text(text, encoding="utf-8", newline="\n")
    print("wrote", OUT)
