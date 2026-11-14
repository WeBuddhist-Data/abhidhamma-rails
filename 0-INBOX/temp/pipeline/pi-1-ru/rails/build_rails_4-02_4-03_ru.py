"""Builder for the Russian rails translation of pi-1 (Dhammasaṅgaṇī, plain audience), chapters 4-02 and 4-03
(Nikkhepakaṇḍaṃ: the flood, yoke, hindrance, misapprehension, clinging and defilement groups, the great
intermediate and the closing pairs ^1-1156 … ^1-1302; the suttanta pairs ^1-1303 … ^1-1383).

Writes (only when run as a script):
  AI_translation/russian/pi-1-russian-plain-rails_split_chapters/4-02-nikkhepakandam.md
  AI_translation/russian/pi-1-russian-plain-rails_split_chapters/4-03-nikkhepakandam.md
  0-INBOX/temp/pipeline/pi-1-ru/rails/notes-4-02_4-03.md

Every line is built from fixed strings. The earlier rails builders are imported, never edited:
build_rails_4-01_ru.py (F: the question / answer frames, «Что такое здесь X?», «это называется X», «Кроме этих
явлений, остальные», «Те явления, которые по отношению к этим явлениям …», «Те самые … и есть …», the craving,
hatred, delusion, doubt, view, conceit and fetter strings, the ten views, the counted names), and through F:
build_rails_sample_ru.py (S: matrix names, synonym strings), build_rails_2-04_ru.py (D), build_rails_3-01_ru.py (T).
Wherever a Pāli line of 4-02 / 4-03 is identical to a line of 4-01, the Russian is checked to be identical to the
4-01 Russian; identical Pāli lines inside 4-02 / 4-03 are checked to give identical Russian.
Punctuation before the Pāli dash (coordinator 2026-11-14): «X – это …» after a plain noun or list; «…, – это …»
only where the dash closes a participial phrase or a subordinate clause.
Terms follow the locked termbase AI_translation/russian/pi-1-pali-russian-termbase-plain.md.

usage: python -I -X utf8 build_rails_4-02_4-03_ru.py
"""
import importlib.util
import pathlib
import re
import sys

HERE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-ru\rails")
sys.path.insert(0, str(HERE))
import build_rails_sample_ru as S  # noqa: E402  (importing writes nothing)


def _load(name, fn):
    spec = importlib.util.spec_from_file_location(name, HERE / fn)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)       # importing writes nothing
    return mod


F = _load("build_rails_4_01_ru", "build_rails_4-01_ru.py")
D, T = F.D, F.T

PARTS = ["4-02-nikkhepakandam.md", "4-03-nikkhepakandam.md"]
cap, low = S.cap, S.low
PE, ELL = "…pe…", "…"
N, Q, A, ans, qa = F.N, F.Q, F.A, F.ans, F.qa
TATTHA, CALLED = F.TATTHA, F.CALLED
NOTES = []          # (pali, russian) new recurring formulas, written to notes-4-02_4-03.md


def note(p, r):
    NOTES.append((p, r))
    return r


def lst(items):
    """a, b, c и d"""
    return items[0] if len(items) == 1 else ", ".join(items[:-1]) + " и " + items[-1]


def cut(s, tail):
    assert s.endswith(tail), (s[-60:], tail)
    return s[:-len(tail)]


def once(s, a, b):
    assert s.count(a) == 1, (a, s.count(a))
    return s.replace(a, b)


# =========================================================================================
# 1. Pieces shared with 4-01
# =========================================================================================
AGG4, AGG4_PE, AGG3, AGG5_PE = F.AGG4, F.AGG4_PE, F.AGG3, F.AGG5_PE
SPH4, SPH3, RES, KIR, SABBA, ASANKH = F.SPH4, F.SPH3, F.RES, F.KIR, F.SABBA, F.ASANKH
TAMSAMP, KILESA, KAMMA3, LDM = F.TAMSAMP, F.KILESA, F.KAMMA3, F.LDM
LOKUTTARA, FOUR_PATHS, KA, KABY, KAA, SAS = F.LOKUTTARA, F.FOUR_PATHS, F.KA, F.KABY, F.KAA, F.SAS
EXC4, THOSE, AMONG, REL, AMONG_REST, DISS_SAS = F.EXC4, F.THOSE, F.AMONG, F.REL, F.AMONG_REST, F.DISS_SAS
locs = F.locs
RUPA = T.RUPA                                                # материальная форма
RUPAKKH_ETC = f"{cap(SAS)} {KAA}, {SPH3}: {AGG5_PE}"         # Sāsavā kusalākusalābyākatā … rūpakkhandho…pe…
ASSOC = f"{THOSE.format('связаны с этими явлениями')} {AGG4_PE}"
DISSOC = THOSE.format("не связаны с этими явлениями") + f" {AGG4_PE}" + "{}" + SABBA   # "; " or ", "
AMONG_ASSOC = f"{AMONG.format('связаны с этими явлениями')}: {AGG4_PE}"
DISS_SAS_KABY = once(DISS_SAS, "благими, неблагими и этически неопределёнными", "благими и этически неопределёнными")
note("Tehi dhammehi ye dhammā vippayuttā sāsavā kusalābyākatā dhammā kāmāvacarā, rūpāvacarā, arūpāvacarā; "
     "rūpakkhandho…pe… viññāṇakkhandho", DISS_SAS_KABY)

# the doctrinal strings (4-01 F, 2-04 D, sample S)
DIITHI = D.S_DIITHI                                          # … хватка, закрепление, … (patiṭṭhāho)
assert F.DIITHI_TAT == DIITHI
DIITHI_PE = "воззрение, приверженность воззрениям" + ELL + " превратная хватка"
assert DIITHI.startswith("воззрение, приверженность воззрениям, ") and DIITHI.endswith(", превратная хватка")
note("diṭṭhi diṭṭhigataṃ…pe… vipariyāsaggāho", DIITHI_PE)
MOHA_PE = "незнание, отсутствие видения" + ELL + " засов неведения, заблуждение как неблагой корень"
assert D.S_MOHA.startswith("незнание, отсутствие видения, ") and D.S_MOHA.endswith(MOHA_PE.split(ELL + " ")[1])
note("aññāṇaṃ adassanaṃ…pe… avijjālaṅgī moho akusalamūlaṃ", MOHA_PE)
PANNA_PE = "мудрость, понимание" + ELL + " отсутствие заблуждения, исследование явлений, правильное воззрение"
assert S.S_PANNA.startswith("мудрость, понимание, ") and S.S_PANNA.endswith(PANNA_PE.split(ELL + " ")[1])
note("paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi", PANNA_PE)
SAMADHI_PE = "устойчивость ума" + ELL + " правильное сосредоточение"
assert S.S_SAMADHI.startswith("устойчивость ума, ") and S.S_SAMADHI.endswith(", правильное сосредоточение")
note("cittassa ṭhiti…pe… sammāsamādhi", SAMADHI_PE)
VIRIYA_PE = "душевное приложение усердия" + ELL + " правильное усилие"
assert S.S_VIRIYA.startswith("душевное приложение усердия, ") and S.S_VIRIYA.endswith(", правильное усилие")
note("cetasiko vīriyārambho…pe… sammāvāyāmo", VIRIYA_PE)
DOUBT_PE = "Сомневаются и колеблются в отношении Учителя" + ELL + " оцепенелость ума, терзание ума"
assert F.DOUBT.startswith(DOUBT_PE.split(ELL)[0] + ", ") and D.S_VICIKICCHA.endswith(", оцепенелость ума, терзание ума")
note("Satthari kaṅkhati vicikicchati…pe… thambhitattaṃ cittassa manovilekho", DOUBT_PE)
BHAVA_PE = f"То, что есть в отношении существования {F.BHAVA_ITEMS[0]}{ELL} {F.BHAVA_ITEMS[-1]}"
note("Yo bhavesu bhavachando…pe… bhavajjhosānaṃ", BHAVA_PE)

MOHA_SEMI = F.MOHA                                           # «…aññāṇaṃः yaṃ evarūpaṃ» (visarga = «;»)
MOHA_DOT = once(MOHA_SEMI, "; то, что есть такое", ". То, что есть такое")     # «…aññāṇaṃ. Yaṃ evarūpaṃ»
VICIK_DOT = f"{F.DOUBT}. {F.VICIK}"                         # «…vicikicchati. Yā evarūpā …»
VICIK_SEMI = f"{F.DOUBT}; {low(F.VICIK)}"                   # «…vicikicchatiः yā evarūpā …»
# ^1-1160 has «;» after the second and the third ground of annoyance; ^1-1237 has commas (= 4-01)
_ag = F.AGHATA.split(", при мысли")
assert len(_ag) == 5
AGHATA_SEMI = _ag[0] + ", при мысли" + _ag[1] + "; при мысли" + _ag[2] + "; при мысли" + _ag[3] + ", при мысли" + _ag[4]
DOSA_SEMI = once(F.DOSA, F.AGHATA, AGHATA_SEMI)
# ^1-1239: «hīnohamasmīti māno; yo evarūpo …» and no variant bracket (4-01 ^1-1121: «. Yo …» [uṇṇati uṇṇāmo])
MANA_SEMI = once(once(F.MANA, " " + S.spell("Syā.", "uṇṇati uṇṇāmo"), ""), "«я хуже». То, что", "«я хуже»; то, что")
# sīlabbata: the Pāli of 4-02 has a dash after «…suddhīti» (4-01: no dash, «;»)
SILA_DASH = once(F.SILABBATA_HEAD, "»; то, что есть такое ", "» – то, что есть такое ")
note("Ito bahiddhā samaṇabrāhmaṇānaṃ sīlena suddhi, vatena suddhi, sīlabbatena suddhīti – yā evarūpā diṭṭhi …",
     SILA_DASH + "воззрение, …")
# sakkāyadiṭṭhi with «Vedanaṃ…pe… saññaṃ…pe… saṅkhāre…pe… viññāṇaṃ attato samanupassati, …»
_last = F.regards(*F.KH5[4])
SAKKAYA_PE = (F.SAKKAYA_HEAD + F.regards(*F.KH5[0]) + " Считает чувство" + ELL + " восприятие" + ELL
              + " формирующие факторы" + ELL + " " + _last[len("считает "):])
assert _last.startswith("считает сознание самостью")
note("… rūpasmiṃ vā attānaṃ. Vedanaṃ…pe… saññaṃ…pe… saṅkhāre…pe… viññāṇaṃ attato samanupassati, … viññāṇasmiṃ "
     "vā attānaṃ.", "… " + SAKKAYA_PE[len(F.SAKKAYA_HEAD):])

# hirī / ottappa without «tasmiṃ samaye»
HIRI = once(S.HIRI_BODY, f" {S.TS}", "")
OTTAPPA = once(S.OTTAPPA_BODY, f" {S.TS}", "")
AHIRI = once(list(D.BODIES.values())[0], f" {S.TS}", "")
ANOTTAPPA = once(list(D.BODIES.values())[1], f" {S.TS}", "")
for _p, _r in [("Yaṃ hirīyati hiriyitabbena, hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā", HIRI),
               ("Yaṃ ottappati ottappitabbena, ottappati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā", OTTAPPA),
               ("Yaṃ na hirīyati hiriyitabbena, na hirīyati …", AHIRI),
               ("Yaṃ na ottappati ottappitabbena, na ottappati …", ANOTTAPPA)]:
    note(_p, _r)

# =========================================================================================
# 2. New strings: hindrances
# =========================================================================================
S_THINA = ("неготовность ума, неработоспособность, оседание, полное оседание, косность, проявление косности, "
           "состояние косности, вялость, проявление вялости, состояние вялости ума")
S_MIDDHA = ("неготовность умственного тела, неработоспособность, окутанность, полная окутанность, внутренняя "
            "скованность, сонливость, дремота, клевание носом, дремота, засыпание, состояние сна")
KUKKUCCA_HEAD = ("Восприятие недопустимого как допустимого, восприятие допустимого как недопустимого, восприятие "
                 "безупречного как предосудительного, восприятие предосудительного как безупречного")
S_KUKKUCCA = "угрызения, мучение угрызениями, состояние мучения угрызениями, раскаяние ума, терзание ума"
note("Yā cittassa akallatā akammaññatā olīyanā sallīyanā līnaṃ līyanā līyitattaṃ thinaṃ thiyanā thiyitattaṃ cittassa",
     f"То, что есть {S_THINA}")
note("Yā kāyassa akallatā akammaññatā onāho pariyonāho antosamorodho middhaṃ soppaṃ pacalāyikā soppaṃ supanā "
     "supitattaṃ", f"То, что есть {S_MIDDHA}")
note("Akappiye kappiyasaññitā, kappiye akappiyasaññitā, avajje vajjasaññitā, vajje avajjasaññitā", KUKKUCCA_HEAD)
note("Yaṃ evarūpaṃ kukkuccaṃ kukkuccāyanā kukkuccāyitattaṃ cetaso vippaṭisāro manovilekho",
     f"То, что есть такие {S_KUKKUCCA}")
THUS = "Итак, {} и {} – это называется {}."                 # Iti idañca X, idañca Y – idaṃ vuccati Z.
note("Iti idañca X, idañca Y – idaṃ vuccati Z.", THUS.format("эта X", "эта Y", "Z (instrumental)"))

# names: hindrances, clingings (nominative, instrumental, dative)
NIV_G = {"kāmacchanda": "чувственного желания", "byāpāda": "недоброжелательности",
         "thinamiddha": "вялости и сонливости", "uddhaccakukkucca": "беспокойства и угрызений",
         "vicikicchā": "колебания", "avijjā": "неведения", "uddhacca": "беспокойства", "kukkucca": "угрызений"}
NIV = {k: (f"помеха {g}", f"помехой {g}", f"помехе {g}") for k, g in NIV_G.items()}
UPA_G = {"kām": "за чувственные удовольствия", "diṭṭh": "за воззрения", "sīlabbat": "за обряды и обеты",
         "attavād": "за учение о самости"}
UPA = {k: (f"цепляние {g}", f"цеплянием {g}", f"цеплянию {g}") for k, g in UPA_G.items()}
for _k, _v in NIV.items():
    note(f"{_k}nīvaraṇaṃ", _v[0])
for _k, _v in UPA.items():
    note(f"{_k}upādānaṃ", _v[0])
PARAMASA = ("искажение из-за воззрения", "искажением из-за воззрения")       # Diṭṭhiparāmāso (termbase)

# =========================================================================================
# 3. New strings: wrong and right view of the «natthi dinnaṃ» kind (model: pi-4 ^4-62 / ^4-82)
# =========================================================================================


def natthi(neg, var=""):
    if neg:
        no, none, beings, rec = "ничего не значит", "нет", "нет рождающихся самопроизвольно существ", \
            "нет в мире отшельников и брахманов, идущих верным путём{}, правильно практикующих"
    else:
        no, none, beings, rec = "имеет значение", "есть", "есть рождающиеся самопроизвольно существа", \
            "есть в мире отшельники и брахманы, идущие верным путём{}, правильно практикующие"
    return (f"«Подаяние {no}, жертвоприношение {no}, подношение {no}, у хорошо и дурно совершённых поступков "
            f"{none} плода, {none} результата, этот мир {no}, иной мир {no}, мать {no}, отец {no}, {beings}, "
            + rec.format(var) + ", которые, сами постигнув высшим знанием и осуществив этот мир и иной мир, "
            "возвещают о них»").replace("есть плода, есть результата", "есть плод, есть результат")


NATTHI = natthi(True)
NATTHI_VAR = natthi(True, " " + S.reading("Ka.", "samaggatā"))
ATTHI = natthi(False)
note("Natthi dinnaṃ, natthi yiṭṭhaṃ, … sacchikatvā pavedentīti", NATTHI)
note("Atthi dinnaṃ, atthi yiṭṭhaṃ, … sacchikatvā pavedentīti", ATTHI)

# =========================================================================================
# 4. New strings: suttanta definitions
# =========================================================================================
SUT = {}     # matrix name -> (nominative, instrumental), from S.SUTTA_ITEMS
_INS = {"Умственное": "умственным", "Материальная форма": "материальной формой", "Неведение": "неведением",
        "Жажда": "жаждой", "Воззрение": "воззрением", "Бессовестность": "бессовестностью",
        "Отсутствие": "отсутствием", "Совестливость": "совестливостью", "Страх": "страхом",
        "Неспособность": "неспособностью", "Дружба": "дружбой", "Готовность": "готовностью", "Умение": "умением",
        "Прямодушие": "прямодушием", "Мягкость": "мягкостью", "Терпение": "терпением", "Кротость": "кротостью",
        "Приветливость": "приветливостью", "Радушие": "радушием", "Неохранение": "неохранением",
        "Незнание": "незнанием", "Охранение": "охранением", "Знание": "знанием", "Утрата": "утратой",
        "Осознанность": "осознанностью", "Ясное понимание": "ясным пониманием", "Сила": "силой",
        "Успокоение": "успокоением", "Прозрение": "прозрением", "Признак": "признаком",
        "Напряжение": "напряжением", "Испорченность": "испорченностью", "Безупречность": "безупречностью",
        "Чистота": "чистотой"}
for _sid, _pair in S.SUTTA_ITEMS.items():
    for _p, _r in _pair:
        _r = _r.split(" [")[0]
        _p = _p[:-3] if _p.endswith(" ca") else (_p[:-3] + "ṃ" if _p.endswith("ñca") else _p)
        for _h in sorted(_INS, key=len, reverse=True):
            if _r == _h or _r.startswith(_h + " "):
                SUT.setdefault(_p, (low(_r), _INS[_h] + _r[len(_h):]))
                break
for _k in ("nāmaṃ", "rūpaṃ", "avijjā", "bhavataṇhā", "bhavadiṭṭhi", "aparantānudiṭṭhi", "ahirikaṃ", "anottappaṃ",
           "hirī", "ottappaṃ", "dovacassatā", "kalyāṇamittatā", "āpattikusalatā", "aṭṭhānakusalatā", "ajjavo",
           "soraccaṃ", "paṭisanthāro", "indriyesu aguttadvāratā", "bhojane mattaññutā", "muṭṭhasaccaṃ",
           "sampajaññaṃ", "bhāvanābalaṃ", "paggāhanimittaṃ", "avikkhepo", "diṭṭhivipatti", "diṭṭhivisuddhi"):
    assert _k in SUT, (_k, sorted(SUT)[:80])
assert SUT["indriyesu aguttadvāratā"] == ("неохранение врат чувств", "неохранением врат чувств")
assert SUT["sampajaññaṃ"] == ("ясное понимание", "ясным пониманием")


def tq(key):
    return TATTHA.format(SUT[key][0])


def called(key):
    return CALLED.format(SUT[key][1])


def define(key, body, comma=True):
    """Tattha katamo/ā/aṃ X? <body> – ayaṃ/idaṃ vuccati X."""
    return f"{tq(key)} {body}{', – ' if comma else ' – '}{called(key)}"


# views about the self and the world
SELF_WORLD = {"bhavadiṭṭhi": "«Самость и мир будут существовать»",
              "vibhavadiṭṭhi": "«Самость и мир не будут существовать»",
              "sassatadiṭṭhi": "«Самость и мир вечны»",
              "ucchedadiṭṭhi": "«Самость и мир будут уничтожены»",
              "antavā diṭṭhi": "«Самость и мир конечны»",
              "anantavā diṭṭhi": "«Самость и мир бесконечны»"}
for _k, _v in SELF_WORLD.items():
    note(f"… attā ca loko cāti ({_k})", _v)
ARABBHA = {"pubbantānudiṭṭhi": "прошлого", "aparantānudiṭṭhi": "будущего"}
VIEW_ARISES = "То, что в отношении {} возникает {}"           # X ārabbha yā uppajjati diṭṭhi …
note("Pubbantaṃ / Aparantaṃ ārabbha yā uppajjati diṭṭhi diṭṭhigataṃ…pe… vipariyāsaggāho",
     VIEW_ARISES.format("прошлого / будущего", DIITHI_PE))

DOVACASSA = ("Когда человеку делают замечание в согласии с Учением, а он проявляет неподатливость, упрямство, "
             "неспособность принимать наставления, склонность воспринимать всё наоборот, удовольствие от "
             "противоречия, непочтительность, непочтительное отношение, неуважение, непослушание")
SOVACASSA = ("Когда человеку делают замечание в согласии с Учением, а он проявляет податливость, сговорчивость, "
             "готовность принимать наставления, отсутствие склонности воспринимать всё наоборот, отсутствие "
             "удовольствия от противоречия, уважение, почтительность, почтительное отношение, послушание")
COMPANY = ("общение с ними, частое общение, тесное общение, сближение, тесное сближение, преданность, "
           "привязанность, склонность к ним")
PAPAMITTA = f"Те люди, которые лишены веры, безнравственны, мало слышали, скупы, лишены мудрости: {COMPANY}"
KALYANAMITTA = f"Те люди, которые обладают верой, нравственны, много слышали, щедры, мудры: {COMPANY}"
note("Sahadhammike vuccamāne dovacassāyaṃ … appaṭissavatā", DOVACASSA)
note("Sahadhammike vuccamāne sovacassāyaṃ … sappaṭissavatā", SOVACASSA)
note("Ye te puggalā assaddhā … duppaññā, yā tesaṃ sevanā … taṃsampavaṅkatā", PAPAMITTA)
note("Ye te puggalā saddhā … paññavanto, yā tesaṃ sevanā … taṃsampavaṅkatā", KALYANAMITTA)

SKILL = "То, что есть умение разбираться {}, " + PANNA_PE    # Yā tāsaṃ X-kusalatā paññā pajānanā…pe…
TATTHA_PANNA = "То, что здесь есть " + PANNA_PE              # yā tattha paññā pajānanā…pe…
note("Yā tāsaṃ X-ānaṃ X-kusalatā paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi", SKILL.format("в этих X"))
note("yā tattha paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi", TATTHA_PANNA)

ELEMENTS18 = []
for _st, _ob, _vi in [("глаза", "видимых форм", "зрительного"), ("уха", "звуков", "слухового"),
                      ("носа", "запахов", "обонятельного"), ("языка", "вкусов", "вкусового"),
                      ("тела", "осязаемого", "осязательного"), ("ума", "объектов ума", "умственного")]:
    ELEMENTS18.append(f"элемент {_st}, элемент {_ob}, элемент {_vi} сознания")
for _p, _r in (("cakkhudhātu", "элемент глаза"), ("rūpadhātu", "элемент видимых форм"),
               ("manodhātu", "элемент ума"), ("dhammadhātu", "элемент объектов ума")):
    assert _r in ELEMENTS18[0] + ELEMENTS18[5], _r
SPHERES12 = ["сфера глаза", "сфера видимых форм", "сфера уха", "сфера звуков", "сфера носа", "сфера запахов",
             "сфера языка", "сфера вкусов", "сфера тела", "сфера осязаемого", "сфера ума", "сфера объектов ума"]
assert all(x in T.AYATANAS_R + ", сфера ума, сфера объектов ума" for x in SPHERES12)

PS_CHAIN = ("«Неведением обусловлены формирующие факторы, формирующими факторами обусловлено сознание, сознанием "
            "обусловлены умственное и материальная форма, умственным и материальной формой обусловлены шесть сфер "
            "восприятия, шестью сферами восприятия обусловлен контакт, контактом обусловлено чувство, чувством "
            "обусловлена жажда, жаждой обусловлено цепляние, цеплянием обусловлено существование, существованием "
            "обусловлено рождение, рождением обусловлены и возникают старение и смерть, печаль, стенания, боль, "
            "уныние и отчаяние; так происходит возникновение всей этой совокупности страдания»")
note("Avijjāpaccayā saṅkhārā, … evametassa kevalassa dukkhakkhandhassa samudayo hotīti", PS_CHAIN)

TTHANA = ("Если какие-либо явления являются причинами и условиями для возникновения "
          + S.reading("Sī., Ka.", "upādāya") + " каких-либо явлений, то каждое такое является возможным")
ATTHANA = ("Если какие-либо явления не являются ни причинами, ни условиями для возникновения каких-либо явлений, "
           "то каждое такое является невозможным")
note("Ye ye dhammā yesaṃ yesaṃ dhammānaṃ hetū paccayā uppādāya taṃ taṃ ṭhānanti",
     TTHANA.replace(" " + S.reading("Sī., Ka.", "upādāya"), ""))
note("Ye ye dhammā yesaṃ yesaṃ dhammānaṃ na hetū na paccayā uppādāya taṃ taṃ aṭṭhānanti", ATTHANA)

AJJAVA = "То, что есть прямодушие, отсутствие кривизны, отсутствие изогнутости, отсутствие извилистости"
assert AJJAVA.endswith(S.S_UJUKATA.split(", ", 2)[2])
MADDAVA = f"То, что есть {S.S_MUDUTA}, смиренность ума"
KHANTI = ("То, что есть терпение, терпимость, выносливость, отсутствие свирепости, отсутствие грубости, "
          "довольство ума")
NONTRANS = "отсутствие нарушений телом, отсутствие нарушений речью, отсутствие нарушений телом и речью"
TRANS = "нарушение телом, нарушение речью, нарушение телом и речью"
note("Yo kāyiko avītikkamo, vācasiko avītikkamo, kāyikavācasiko avītikkamo", f"То, что есть {NONTRANS}")
note("Yo kāyiko vītikkamo, vācasiko vītikkamo, kāyikavācasiko vītikkamo", f"То, что есть {TRANS}")
ALL_RESTRAINT = "Всякая нравственная сдержанность является {}."   # Sabbopi sīlasaṃvaro X.
note("Sabbopi sīlasaṃvaro X.", ALL_RESTRAINT.format("X (instrumental)"))
SAKHALYA = ("Человек, отказавшись от такой речи, которая резка, жёстка, язвительна для других, оскорбительна для "
            "других, граничит с гневом, не ведёт к сосредоточению, говорит такой речью, которая безупречна, "
            "приятна для слуха, располагает к себе, трогает сердце, вежлива, мила многим людям, приятна многим "
            "людям; то, что здесь есть мягкость речи, приветливость речи, отсутствие резкости речи")
PATISANTHARA = ("Два вида радушия – радушие с помощью материальных вещей и радушие с помощью Учения. Вот человек "
                "радушен, проявляя радушие с помощью материальных вещей или радушие с помощью Учения")

SENSES = [("увидев глазом видимую форму", "её", "глаза"), ("услышав ухом звук", None, None),
          ("понюхав носом запах", None, None), ("попробовав языком вкус", None, None),
          ("коснувшись телом осязаемого", None, None), ("познав умом объект ума", "его", "ума")]


def doors(guard):
    ne = "" if guard else "не "
    grab = "не цепляется за {0} общий облик, не цепляется за {0} детали" if guard else \
        "цепляется за {0} общий облик, цепляется за {0} детали"

    def restraint(fac):
        sv = "сдержанность" if guard else "сдержанности"
        return (f"Поскольку, если он пребывает с необузданной способностью {fac}, в него могли бы проникнуть "
                f"алчность и уныние, дурные неблагие явления, он {ne}старается её обуздать, {ne}охраняет "
                f"способность {fac}, {ne}соблюдает {sv} в отношении способности {fac}.")

    eye = f"Вот человек, {SENSES[0][0]}, {grab.format('её')}. {restraint('глаза')}"
    rest = cap(f"{ELL} ".join(s[0] for s in SENSES[1:])) + f", {grab.format('его')}. {restraint('ума')}"
    six = ("охрана, защита, присмотр, сдержанность" if guard
           else "отсутствие охраны, отсутствие защиты, отсутствие присмотра, несдержанность")
    return f"{eye} {rest} То, что есть {six} этих шести способностей"


DOORS_NOT, DOORS = doors(False), doors(True)
note("Idhekacco cakkhunā rūpaṃ disvā nimittaggāhī hoti anubyañjanaggāhī. … agutti agopanā anārakkho asaṃvaro",
     DOORS_NOT)
FOOD_NOT = ("Вот человек принимает пищу без размышления, неразумно, ради забавы, ради упоения, ради "
            "привлекательности, ради украшения тела. То, что здесь есть отсутствие довольства, незнание меры, "
            "отсутствие размышления в еде")
FOOD = ("Вот человек принимает пищу с размышлением, вдумчиво – «ни ради забавы, ни ради упоения, ни ради "
        "привлекательности, ни ради украшения тела, а только для сохранения и поддержания этого тела, для прекращения "
        "мучений, для поддержки духовной жизни; так я устраню прежнее чувство и не вызову нового чувства, и жизнь моя "
        "будет продолжаться безупречно, и я буду жить спокойно». То, что здесь есть довольство, знание меры, "
        "размышление в еде")
MUTTHASACCA = ("То, что есть неосознанность, отсутствие припоминания, отсутствие воспоминания, неосознанность, "
               "неспособность помнить, неспособность удерживать в памяти, поверхностность, забывчивость")
assert S.S_SATI.startswith("осознанность, припоминание, воспоминание, осознанность, способность помнить, "
                           "способность удерживать в памяти, отсутствие поверхностности, отсутствие забывчивости")
BHAVANA = "То, что есть практика, развитие, многократное повторение благих явлений"
STRIVE = "порождает желание, прилагает усилие, пробуждает усердие, напрягает ум, прилагает старания"
note("chandaṃ janeti vāyamati vīriyaṃ ārabhati cittaṃ paggaṇhāti padahati", STRIVE)
note("kusalānaṃ dhammānaṃ āsevanā bhāvanā bahulīkammaṃ", "практика, развитие, многократное повторение благих явлений")


def kho(sid_item, i):
    """the quoted matrix item of 1-M2-138 … 1-M2-142 («X»)"""
    return "«" + S.SUTTA_ITEMS[sid_item][i][1] + "»"


# =========================================================================================
# 5. Headings and fixed lines
# =========================================================================================
EXACT = {
    "##### Oghagocchakaṃ": "##### " + S.CLUSTERS["ogha"]["heading"],
    "##### Yogagocchakaṃ": "##### " + S.CLUSTERS["yoga"]["heading"],
    "##### Nīvaraṇagocchakaṃ": "##### " + S.CLUSTERS["nivarana"]["heading"],
    "##### Parāmāsagocchakaṃ": "##### " + S.CLUSTERS["paramasa"]["heading"],
    "##### Mahantaradukaṃ": "##### " + S.MAHANTARA,
    "##### Upādānagocchakaṃ": "##### " + S.CLUSTERS["upadana"]["heading"],
    "##### Kilesagocchakaṃ": "##### Группа омрачений",
    "##### Piṭṭhidukaṃ": "##### " + S.PITTHI,
    "#### Suttantikadukanikkhepaṃ": "#### Сводка пар из наставлений",
    "Ime dhammā nīvaraṇā.": "Это " + N["nīvaraṇā"] + ".",
    "Ime dhammā parāmāsā.": "Это " + N["parāmāsā"] + ".",
    "Ime dhammā upādānā.": "Это " + N["upādānā"] + ".",
    "Ime dhammā kilesā.": "Это " + N["kilesā"] + ".",
    "Nikkhepakaṇḍe dutiyabhāṇavāro.": once(F.EXACT["Nikkhepakaṇḍe paṭhamabhāṇavāro."], "Первый", "Второй"),
    "Abhidhammadukaṃ.": "Пары Абхидхаммы.",
    "Nikkhepakaṇḍaṃ niṭṭhitaṃ.": f"{S.CH_HEADINGS['Nikkhepakaṇḍaṃ']} завершён.",
}
assert S.MATRIX_HEADINGS["1-M-2-12-0"] == "##### Группа омрачений"
for _p, _r in EXACT.items():
    note(_p, _r)

# =========================================================================================
# 6. The segments
# =========================================================================================
R = {}


def seg(sid, *lines):
    assert sid not in R, sid
    R[sid] = list(lines)


def rest_among(verb):
    return AMONG_REST.format(AMONG.format(f"{REL} {verb}"))


def same_as(name, plural):
    """Tāneva X-āni / Teva X-ā X-ā ceva Y-ā ca."""
    return f"{Q(name)} Те самые {plural} и есть {N[name]}."


# ---------------------------------------------------------------- floods, yokes
seg("1-1156", f"{Q('oghā')} Четыре потока{ELL} {A('oghavippayuttā oghaniyā')}")
seg("1-1157", f"{Q('yogā')} Четыре ярма{ELL} {A('yogavippayuttā yoganiyā')}")

# ---------------------------------------------------------------- hindrances
NIV6 = ["kāmacchanda", "byāpāda", "thinamiddha", "uddhaccakukkucca", "vicikicchā", "avijjā"]
seg("1-1158", f"{Q('nīvaraṇā')} Шесть помех {S.reading('Syā.', 'nīvaraṇāni')} – "
              f"{', '.join(NIV[k][0] for k in NIV6)}.")


def tq_niv(k):
    return TATTHA.format(NIV[k][0])


def called_niv(k):
    return CALLED.format(NIV[k][1])


seg("1-1159", f"{tq_niv('kāmacchanda')} {F.KAMA_BODY}, – {called_niv('kāmacchanda')}")
seg("1-1160", f"{tq_niv('byāpāda')} {DOSA_SEMI}, – {called_niv('byāpāda')}")
seg("1-1161", f"{tq_niv('thinamiddha')} Есть вялость, есть сонливость.")
seg("1-1162", f"{TATTHA.format('вялость')} То, что есть {S_THINA}, – {CALLED.format('вялостью')}")
seg("1-1163", f"{TATTHA.format('сонливость')} То, что есть {S_MIDDHA}, – {CALLED.format('сонливостью')} "
              + THUS.format("эта вялость", "эта сонливость", NIV["thinamiddha"][1]))
seg("1-1164", f"{tq_niv('uddhaccakukkucca')} Есть беспокойство, есть угрызения.")
seg("1-1165", f"{TATTHA.format('беспокойство')} То, что есть {D.S_UDDHACCA}, – {CALLED.format('беспокойством')}")
seg("1-1166", f"{TATTHA.format('угрызения')} {KUKKUCCA_HEAD}. То, что есть такие {S_KUKKUCCA}, – "
              f"{CALLED.format('угрызениями')} "
              + THUS.format("это беспокойство", "эти угрызения", NIV["uddhaccakukkucca"][1]))
seg("1-1167", f"{tq_niv('vicikicchā')} {VICIK_DOT}, – {called_niv('vicikicchā')}")
seg("1-1168", f"{tq_niv('avijjā')} {MOHA_SEMI}, – {called_niv('avijjā')}", EXACT["Ime dhammā nīvaraṇā."])
seg("1-1169", qa("no nīvaraṇā", f"{EXC4}: {AGG4_PE}; {SABBA}", False))
seg("1-1170", qa("nīvaraṇiyā", RUPAKKH_ETC, False))
seg("1-1171", qa("anīvaraṇiyā", LOKUTTARA, False))
seg("1-1172", qa("nīvaraṇasampayuttā", ASSOC, False))
seg("1-1173", qa("nīvaraṇavippayuttā", DISSOC.format("; "), False))
seg("1-1174", same_as("nīvaraṇā ceva nīvaraṇiyā ca", "помехи"))
seg("1-1175", qa("nīvaraṇiyā ceva no ca nīvaraṇā", rest_among("подвержены помехам"), False))

GEND = {"жадность": "а", "злоба": "а", "заблуждение": "о", "самомнение": "о", "воззрение": "о", "колебание": "о",
        "вялость": "а", "беспокойство": "о", "бессовестность": "а", "отсутствие страха перед дурным": "о"}


def pairs_line(pali_line, item_re, nom, dat, pred, closing):
    body = pali_line.split("? ", 1)[1].rsplit(" – ", 1)[0]
    found = re.findall(item_re, body)
    rebuilt = ", ".join(" ".join(x) for x in found)
    assert re.sub(item_re, lambda m: m.group(1) + " " + m.group(2), body) == rebuilt, "items lost"
    return qa(closing, cap(F.rel_pairs([(nom[a], dat[b]) for a, b in found], pred)), False), len(found)


def pali_of(sid):
    for part in PARTS:
        for s, pl in S.segments(S.PALI / part):
            if s == sid:
                return [re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", x) for x in pl]
    raise KeyError(sid)


_niv_nom = {f"{k}nīvaraṇaṃ": v[0] for k, v in NIV.items()}
_niv_nom.update({cap(k): v for k, v in _niv_nom.items()})
_niv_dat = {f"{k}nīvaraṇena": v[2] for k, v in NIV.items()}
_l, _n = pairs_line(pali_of("1-1176")[0],
                    r"(\w+nīvaraṇaṃ) (\w+nīvaraṇena) nīvaraṇañceva nīvaraṇasampayuttañca",
                    _niv_nom, _niv_dat, lambda n: "является помехой и связана с помехами",
                    "nīvaraṇā ceva nīvaraṇasampayuttā ca")
assert _n == 24, _n
seg("1-1176", _l)
note("X-nīvaraṇaṃ Y-nīvaraṇena nīvaraṇañceva nīvaraṇasampayuttañca",
     "помеха X по отношению к помехе Y является помехой и связана с помехами")
seg("1-1177", qa("nīvaraṇasampayuttā ceva no ca nīvaraṇā", AMONG_ASSOC, False))
seg("1-1178", qa("nīvaraṇavippayuttā nīvaraṇiyā", DISS_SAS_KABY, False))
seg("1-1179", qa("nīvaraṇavippayuttā anīvaraṇiyā", LOKUTTARA, False))

# ---------------------------------------------------------------- misapprehension
seg("1-1180", f"{Q('parāmāsā')} {cap(PARAMASA[0])}.")
seg("1-1181", f"{TATTHA.format(PARAMASA[0])} {F.TEN_VIEWS}; то, что есть такое {DIITHI}, – {CALLED.format(PARAMASA[1])} "
              f"{cap(F.ALL_WRONG.format(PARAMASA[1]))}.", EXACT["Ime dhammā parāmāsā."])
seg("1-1182", qa("no parāmāsā", f"{EXC4}: {AGG4_PE}; {SABBA}", False))
seg("1-1183", qa("parāmaṭṭhā", RUPAKKH_ETC, False))
seg("1-1184", qa("aparāmaṭṭhā", LOKUTTARA, False))
seg("1-1185", qa("parāmāsasampayuttā", ASSOC, False))
seg("1-1186", qa("parāmāsavippayuttā", DISSOC.format("; "), False))
PARAMASA_SAME = "То самое искажение и есть явление, являющееся искажением и затронутое искажениями."
note("Sveva parāmāso parāmāso ceva parāmaṭṭho ca.", PARAMASA_SAME)
seg("1-1187", f"{Q('parāmāsā ceva parāmaṭṭhā ca')} {PARAMASA_SAME}")
seg("1-1188", qa("parāmaṭṭhā ceva no ca parāmāsā", rest_among("затронуты искажениями"), False))
seg("1-1189", qa("parāmāsavippayuttā parāmaṭṭhā", DISS_SAS, False))
seg("1-1190", qa("parāmāsavippayuttā aparāmaṭṭhā", LOKUTTARA, False))

# ---------------------------------------------------------------- great intermediate pairs
CET3_ITEMS = ["совокупность чувств", "совокупность восприятия", "совокупность формирующих факторов"]
CET3 = lst(CET3_ITEMS)
assert AGG4 == ", ".join(CET3_ITEMS) + " и совокупность сознания"
CET3_SABBA = cap(", ".join(CET3_ITEMS)) + ", " + SABBA
CITTA_SABBA = f"И ум, {SABBA}"                              # Cittañca, sabbañca rūpaṃ, asaṅkhatā ca dhātu
CITTA_REST = f"И ум, и остальная {RUPA}, и {ASANKH}"         # Cittañca, avasesañca rūpaṃ, asaṅkhatā ca dhātu
VINNATTI2 = "телесное внешнее выражение, речевое внешнее выражение"
assert VINNATTI2 == f"{T.NOUN['kāyaviññatti'][0]}, {T.NOUN['vacīviññatti'][0]}"
CET3_VINN = cap(", ".join(CET3_ITEMS)) + ", " + VINNATTI2.replace(", ", " и ")
NOT_SAY = "Ум нельзя определить – ни как {0} с умом, ни как не {0} с умом."   # Cittaṃ na vattabbaṃ – …ntipi
note("Cittaṃ na vattabbaṃ – cittena sampayuttantipi, cittena vippayuttantipi.", NOT_SAY.format("связанный"))
note("Cittañca, sabbañca rūpaṃ, asaṅkhatā ca dhātu", CITTA_SABBA)
note("Cittañca, avasesañca rūpaṃ, asaṅkhatā ca dhātu", CITTA_REST)
CITTAJA_CLAUSE = f"или же какая бы другая {RUPA} ни была рождённой умом, имеющей причиной ум, порождённой умом"
CITTAJA_ITEMS = ("сфера видимых форм, сфера звуков, сфера запахов, сфера вкусов, сфера осязаемого, элемент "
                 "пространства, элемент воды, лёгкость материальной формы, мягкость материальной формы, "
                 "работоспособность материальной формы, рост материальной формы, непрерывность материальной формы, "
                 "съедаемая пища")
_r303 = (S.OUT / "3-03-rupakandam.md").read_text(encoding="utf-8")
assert f"{cap(VINNATTI2)}, {CITTAJA_CLAUSE}: {CITTAJA_ITEMS}, –" in _r303      # 3-03 ^1-769, same Pāli list
seg("1-1191", qa("sārammaṇā", cap(AGG4), False))
seg("1-1192", qa("anārammaṇā", cap(SABBA), False))
seg("1-1193", qa("cittā", "Зрительное сознание, слуховое сознание, обонятельное сознание, вкусовое сознание, "
                          "осязательное сознание, элемент ума и элемент умственного сознания", False))
seg("1-1194", qa("no cittā", CET3_SABBA, False))
seg("1-1195", qa("cetasikā", cap(CET3), False))
seg("1-1196", qa("acetasikā", CITTA_SABBA, False))
seg("1-1197", qa("cittasampayuttā", cap(CET3), False))
seg("1-1198", f"{qa('cittavippayuttā', cap(SABBA), False)} {NOT_SAY.format('связанный')}")
seg("1-1199", qa("cittasaṃsaṭṭhā", cap(CET3), False))
seg("1-1200", f"{qa('cittavisaṃsaṭṭhā', cap(SABBA), False)} {NOT_SAY.format('соединённый')}")
seg("1-1201", qa("cittasamuṭṭhānā", f"{cap(CET3)}; {VINNATTI2}; {CITTAJA_CLAUSE}: {CITTAJA_ITEMS}", False))
seg("1-1202", qa("no cittasamuṭṭhānā", CITTA_REST, False))
seg("1-1203", qa("cittasahabhuno", CET3_VINN, False))
seg("1-1204", qa("no cittasahabhuno", CITTA_REST, False))
seg("1-1205", qa("cittānuparivattino", CET3_VINN, False))
seg("1-1206", qa("no cittānuparivattino", CITTA_REST, False))
seg("1-1207", qa("cittasaṃsaṭṭhasamuṭṭhānā", cap(CET3), False))
seg("1-1208", qa("no cittasaṃsaṭṭhasamuṭṭhānā", CITTA_SABBA, False))
seg("1-1209", qa("cittasaṃsaṭṭhasamuṭṭhānasahabhuno", cap(CET3), False))
seg("1-1210", qa("no cittasaṃsaṭṭhasamuṭṭhānasahabhuno", CITTA_SABBA, False))
seg("1-1211", qa("cittasaṃsaṭṭhasamuṭṭhānānuparivattino", cap(CET3), False))
seg("1-1212", qa("no cittasaṃsaṭṭhasamuṭṭhānānuparivattino", CITTA_SABBA, False))
seg("1-1213", qa("ajjhattikā", f"{cap(T.NOUN['cakkhāyatanaṃ'][0])}{ELL} сфера ума", False))
seg("1-1214", qa("bāhirā", f"{cap(T.NOUN['rūpāyatanaṃ'][0])}{ELL} сфера объектов ума", False))
seg("1-1215", qa("upādā", f"{cap(T.NOUN['cakkhāyatanaṃ'][0])}{ELL} {T.NOUN['kabaḷīkāro āhāro'][0]}", False))
seg("1-1216", qa("no upādā", f"{cap(AGG4.replace(' и совокупность сознания', ', совокупность сознания'))}, "
                             f"и четыре великих элемента, и {ASANKH}", False))
seg("1-1217", qa("upādiṇṇā", f"{cap(AGG4_PE)}, {RES}, {SAS} и {SPH3}, {F.YANCA_KAMMA}", True))   # = 4-01 ^1-994
seg("1-1218", qa("anupādiṇṇā", f"{cap(SAS)} {KA}, {SPH3}: {AGG4_PE}; {KIR}; {F.YANCA_NA_KAMMA}; {low(LOKUTTARA)}",
                 False))

# ---------------------------------------------------------------- clinging
UPA4 = ["kām", "diṭṭh", "sīlabbat", "attavād"]
seg("1-1219", f"{Q('upādānā')} Четыре цепляния – {', '.join(UPA[k][0] for k in UPA4)} "
              f"{S.spell('Sī.', 'kāmūpādānaṃ diṭṭhūpādānaṃ sīlabbatūpādānaṃ attavādūpādānaṃ')}.")
seg("1-1220", f"{TATTHA.format(UPA['kām'][0])} {F.KAMA_BODY}, – {CALLED.format(UPA['kām'][1])}")
seg("1-1221", f"{TATTHA.format(UPA['diṭṭh'][0])} {NATTHI_VAR} – то, что есть такое {DIITHI}, – "
              f"{CALLED.format(UPA['diṭṭh'][1])} Кроме {UPA['sīlabbat'][1].replace('цеплянием', 'цепляния')} и "
              f"{UPA['attavād'][1].replace('цеплянием', 'цепляния')}, {F.ALL_WRONG.format(UPA['diṭṭh'][1])}.")
seg("1-1222", f"{TATTHA.format(UPA['sīlabbat'][0])} {SILA_DASH}{DIITHI}, – {CALLED.format(UPA['sīlabbat'][1])}")
seg("1-1223", f"{TATTHA.format(UPA['attavād'][0])} {SAKKAYA_PE} То, что есть такое {DIITHI}, – "
              f"{CALLED.format(UPA['attavād'][1])}", EXACT["Ime dhammā upādānā."])
seg("1-1224", qa("no upādānā", f"{EXC4}: {AGG4_PE}; {SABBA}", False))
seg("1-1225", qa("upādāniyā", RUPAKKH_ETC, False))
seg("1-1226", qa("anupādāniyā", LOKUTTARA, False))
seg("1-1227", qa("upādānasampayuttā", ASSOC, False))
seg("1-1228", qa("upādānavippayuttā", DISSOC.format("; "), False))
seg("1-1229", same_as("upādānā ceva upādāniyā ca", "цепляния"))
seg("1-1230", qa("upādāniyā ceva no ca upādānā", rest_among("служат объектом цепляния"), False))
_upa_nom = {f"{k}upādānaṃ": v[0] for k, v in UPA.items()}
_upa_nom.update({cap(k): v for k, v in _upa_nom.items()})
_upa_dat = {f"{k}upādānena": v[2] for k, v in UPA.items()}
_l, _n = pairs_line(pali_of("1-1231")[0], r"(\w+upādānaṃ) (\w+upādānena) upādānañceva upādānasampayuttañca",
                    _upa_nom, _upa_dat, lambda n: "является цеплянием и связано с цепляниями",
                    "upādānā ceva upādānasampayuttā ca")
assert _n == 6, _n
seg("1-1231", _l)
note("X-upādānaṃ Y-upādānena upādānañceva upādānasampayuttañca",
     "цепляние X по отношению к цеплянию Y является цеплянием и связано с цепляниями")
seg("1-1232", qa("upādānasampayuttā ceva no ca upādānā", AMONG_ASSOC, False))
seg("1-1233", qa("upādānavippayuttā upādāniyā", DISS_SAS, False))
seg("1-1234", qa("upādānavippayuttā anupādāniyā", LOKUTTARA, False), EXACT["Nikkhepakaṇḍe dutiyabhāṇavāro."])

# ---------------------------------------------------------------- defilements
KIL10 = ["жадность", "злоба", "заблуждение", "самомнение", "воззрение", "колебание", "вялость", "беспокойство",
         "бессовестность", "отсутствие страха перед дурным"]
seg("1-1235", f"{Q('kilesā')} Десять основ омрачений – {', '.join(KIL10)}.")
_lobha_p = pali_of("1-1236")[0]
assert _lobha_p == f"Tattha katamo lobho? Yo {F.LOBHA_P_PLAIN} – ayaṃ vuccati lobho.", "lobha list differs"
seg("1-1236", f"{TATTHA.format('жадность')} То, что есть {F.lobha(False)}, – {CALLED.format('жадностью')}")
seg("1-1237", f"{TATTHA.format('злоба')} {F.DOSA}, – {CALLED.format('злобой')}")
seg("1-1238", f"{TATTHA.format('заблуждение')} {MOHA_DOT}, – {CALLED.format('заблуждением')}")
seg("1-1239", f"{TATTHA.format('самомнение')} {MANA_SEMI}, – {CALLED.format('самомнением')}")
seg("1-1240", f"{TATTHA.format('воззрение')} {F.TEN_VIEWS}; то, что есть такое {DIITHI}, – {CALLED.format('воззрением')} "
              f"{cap(F.ALL_WRONG.format('воззрением'))}.")
seg("1-1241", f"{TATTHA.format('колебание')} {VICIK_SEMI}, – {CALLED.format('колебанием')}")
seg("1-1242", f"{TATTHA.format('вялость')} То, что есть {S_THINA}, – {CALLED.format('вялостью')}")
seg("1-1243", f"{TATTHA.format('беспокойство')} То, что есть {D.S_UDDHACCA}, – {CALLED.format('беспокойством')}")
seg("1-1244", define("ahirikaṃ", AHIRI))
seg("1-1245", define("anottappaṃ", ANOTTAPPA), EXACT["Ime dhammā kilesā."])
seg("1-1246", qa("no kilesā", f"{EXC4}: {AGG4_PE}; {SABBA}", False))
seg("1-1247", qa("saṃkilesikā", RUPAKKH_ETC, False))
seg("1-1248", qa("asaṃkilesikā", LOKUTTARA, False))
seg("1-1249", qa("saṃkiliṭṭhā", f"{F.ROOTS_A}; {KILESA}; {TAMSAMP} {AGG4_PE}; {KAMMA3}", False))   # = 4-01 ^1-997
seg("1-1250", qa("asaṃkiliṭṭhā", f"{cap(KABY)}, {SPH4}: {AGG4_PE}; {SABBA}", False))
seg("1-1251", qa("kilesasampayuttā", ASSOC, False))
seg("1-1252", qa("kilesavippayuttā", DISSOC.format("; "), False))
seg("1-1253", same_as("kilesā ceva saṃkilesikā ca", "омрачения"))
seg("1-1254", qa("saṃkilesikā ceva no ca kilesā", rest_among("подвержены омрачению"), False))
seg("1-1255", same_as("kilesā ceva saṃkiliṭṭhā ca", "омрачения"))
seg("1-1256", qa("saṃkiliṭṭhā ceva no ca kilesā", f"{AMONG.format('омрачены этими явлениями')}: {AGG4_PE}", False))
note("Tehi dhammehi ye dhammā saṃkiliṭṭhā, te dhamme ṭhapetvā", AMONG.format("омрачены этими явлениями"))
KIL_NOM = dict(zip(["lobho", "doso", "moho", "māno", "diṭṭhi", "vicikicchā", "thinaṃ", "uddhaccaṃ", "ahirikaṃ",
                    "anottappaṃ"], KIL10))
KIL_DAT = dict(zip(["lobhena", "dosena", "mohena", "mānena", "diṭṭhiyā", "vicikicchāya", "thinena", "uddhaccena",
                    "ahirikena", "anottappena"],
                   ["жадности", "злобе", "заблуждению", "самомнению", "воззрению", "колебанию", "вялости",
                    "беспокойству", "бессовестности", "отсутствию страха перед дурным"]))
KIL_NOM.update({cap(k): v for k, v in KIL_NOM.items()})
_l, _n = pairs_line(pali_of("1-1257")[0], r"(\w+) (\w+) kileso ceva kilesasampayutt(?:o ca|ā ca|añca)",
                    KIL_NOM, KIL_DAT, lambda n: f"является омрачением и связан{GEND[n]} с омрачениями",
                    "kilesā ceva kilesasampayuttā ca")
assert _n == 72, _n
seg("1-1257", _l)
note("X Y-ena kileso ceva kilesasampayutto ca", "X по отношению к Y является омрачением и связан(а/о) с омрачениями")
seg("1-1258", qa("kilesasampayuttā ceva no ca kilesā", AMONG_ASSOC, False))
seg("1-1259", qa("kilesavippayuttā saṃkilesikā", DISS_SAS_KABY, False))
seg("1-1260", qa("kilesavippayuttā asaṃkilesikā", LOKUTTARA, False))

# ---------------------------------------------------------------- closing pairs
SAKK, VICI, SILA = F.SAKK, F.VICI, F.SILA
SAKK_I, VICI_I, SILA_I = F.SAKK_I, F.VICI_I, F.SILA_I
SAKK_PE = f"{TATTHA.format(SAKK)} {SAKKAYA_PE} То, что есть такое {DIITHI_PE}, – {CALLED.format(SAKK_I)}"
VICI_PE = f"{TATTHA.format(VICI)} {DOUBT_PE}, – {CALLED.format(VICI_I)}"
SILA_PE = f"{TATTHA.format(SILA)} {SILA_DASH}{DIITHI_PE}, – {CALLED.format(SILA_I)}"
seg("1-1261", f"{Q('dassanena pahātabbā')} {F.SAMYOJ3}.")
seg("1-1262", SAKK_PE)
seg("1-1263", VICI_PE)
seg("1-1264", f"{SILA_PE} {ans(F.DASS_BODY, 'dassanena pahātabbā', False)}")
seg("1-1265", qa("na dassanena pahātabbā", f"{EXC4}: {AGG4_PE}, {SABBA}", False))
seg("1-1266", qa("bhāvanāya pahātabbā", f"Остальные {LDM}; {KILESA}; {TAMSAMP} {AGG4_PE}; {KAMMA3}", False))
seg("1-1267", qa("na bhāvanāya pahātabbā", f"{EXC4}: {AGG4_PE}; {SABBA}", False))
seg("1-1268", f"{Q('dassanena pahātabbahetukā')} {F.SAMYOJ3}.")
seg("1-1269", SAKK_PE)
seg("1-1270", VICI_PE)
seg("1-1271", f"{SILA_PE} {ans(F.DASS_BODY, 'dassanena pahātabbahetukā', False)} "
              f"{ans(F.SAMYOJ3, 'dassanena pahātabbā', False)} Пребывающие вместе с ними {LDM} – {F.ROOTS_D} "
              f"{ans(F.TAIL_KB, 'dassanena pahātabbahetukā', False)}")
assert R["1-1271"][0].endswith(" " + F.R["1-1017"][0])        # tail = 4-01 ^1-1017
seg("1-1272", qa("na dassanena pahātabbahetukā", f"{EXC4}: {AGG4_PE}; {SABBA}", False))
seg("1-1273", f"{Q('bhāvanāya pahātabbahetukā')} Остальные {LDM} – {F.ROOTS_B} "
              f"{ans(F.TAIL_KB, 'bhāvanāya pahātabbahetukā', False)}")
seg("1-1274", qa("na bhāvanāya pahātabbahetukā", f"{EXC4}: {AGG4_PE}; {SABBA}", False))
LVL = {"vitakka": ("с направленной мыслью", "без направленной мысли", "направленной мысли", "ней",
                   "и направленная мысль"),
       "vicāra": ("с удержанием мысли", "без удержания мысли", "удержания мысли", "ним", "и удержание мысли"),
       "pīti": ("с восторгом", "без восторга", "восторга", "ним", "и восторг")}
seg("1-1275", qa("savitakkā", f"На уровне {LVL['vitakka'][0]} {locs('krp')}, кроме {LVL['vitakka'][2]}, связанные с "
                              f"{LVL['vitakka'][3]} {AGG4_PE}", False))
seg("1-1276", qa("avitakkā", f"На уровне {LVL['vitakka'][1]} {locs('krap')}: {AGG4_PE}; {LVL['vitakka'][4]}, {SABBA}",
                 False))
seg("1-1277", qa("savicārā", f"На уровне {LVL['vicāra'][0]} {locs('krp')}, кроме {LVL['vicāra'][2]}, связанные с "
                             f"{LVL['vicāra'][3]} {AGG4}", False))
seg("1-1278", qa("avicārā", f"На уровне {LVL['vicāra'][1]} {locs('krap')}: {AGG4_PE}; {LVL['vicāra'][4]}, {SABBA}",
                 False))
seg("1-1279", qa("sappītikā", f"На уровне {LVL['pīti'][0]} {locs('krp')}, кроме {LVL['pīti'][2]}, связанные с "
                              f"{LVL['pīti'][3]} {AGG4_PE}", False))
seg("1-1280", qa("appītikā", f"На уровне {LVL['pīti'][1]} {locs('krap')}: {AGG4_PE}; {LVL['pīti'][4]}, {SABBA}",
                 False))
seg("1-1281", qa("pītisahagatā", f"На уровне восторга {locs('krp')}, кроме восторга, связанные с ним {AGG4_PE}",
                 False))                                                                           # = 4-01 ^1-1003
seg("1-1282", qa("na pītisahagatā", f"Не на уровне восторга {locs('krap')}: {AGG4_PE}; и восторг, {SABBA}", False))
seg("1-1283", qa("sukhasahagatā", f"На уровне счастья {locs('krp')}, кроме счастья, связанные с ним {AGG3}", False))
seg("1-1284", qa("na sukhasahagatā", f"Не на уровне счастья {locs('krap')}: {AGG4_PE}; и счастье, {SABBA}", False))
seg("1-1285", qa("upekkhāsahagatā", f"На уровне невозмутимости {locs('krap')}, кроме невозмутимости, связанные с ней "
                                    f"{AGG3}", False))
seg("1-1286", qa("na upekkhāsahagatā", f"Не на уровне невозмутимости {locs('krp')}: {AGG4_PE}; и невозмутимость, "
                                       f"{SABBA}", False))
note("Na pītibhūmiyaṃ / Na sukhabhūmiyaṃ / Na upekkhābhūmiyaṃ", "Не на уровне восторга / счастья / невозмутимости")
note("Sappītikabhūmiyaṃ / Appītikabhūmiyaṃ (Pītibhūmiyaṃ = «На уровне восторга», 4-01)",
     "На уровне с восторгом / На уровне без восторга")
WITHIN = "то всё, что в этих пределах относится к этому миру и принадлежит к нему:"
note("yaṃ etasmiṃ antare etthāvacarā ettha pariyāpannā", WITHIN)
LIMITS = "Если взять снизу за границу {}, а сверху включить в эти пределы {}, "   # Heṭṭhato X pariyantaṃ karitvā, …
note("Heṭṭhato X pariyantaṃ karitvā, uparito Y anto karitvā,", LIMITS.format("X", "Y"))
PERSONS = ("ум и сопутствующие уму явления того, кто вошёл в медитативное достижение, или того, кто переродился, "
           "или того, кто пребывает в счастье в этой жизни")
note("samāpannassa vā upapannassa vā diṭṭhadhammasukhavihārissa vā cittacetasikā dhammā", PERSONS)
seg("1-1287", qa("kāmāvacarā",
                 LIMITS.format("ад Авичи", "богов, властвующих над творениями других "
                               + S.spell("Sī., Ka.", "paranimmitavasavattideve"))
                 + WITHIN + f" совокупности, элементы и сферы восприятия; {RUPA}, чувство, восприятие, формирующие "
                            f"факторы, сознание", False))
OTHER3 = "Явления, относящиеся к {} и к {}, и явления, не принадлежащие к кругам существования"
seg("1-1288", qa("na kāmāvacarā", OTHER3.format("миру форм", "миру без форм"), True))
seg("1-1289", qa("rūpāvacarā",
                 LIMITS.format("мир Брахмы", "богов Аканиттха " + S.spell("Sī., Ka.", "akaniṭṭhadeve")) + WITHIN
                 + " " + PERSONS.replace("в этой жизни", "в этой жизни " + S.spell("Ka.", "diṭṭhadhammasukhavihārassa")),
                 True))
seg("1-1290", qa("na rūpāvacarā", OTHER3.format("миру чувственных желаний", "миру без форм"), True))
seg("1-1291", qa("arūpāvacarā",
                 LIMITS.format("богов, рождённых в сфере бесконечного пространства",
                               "богов, рождённых в сфере ни восприятия, ни невосприятия") + WITHIN + " " + PERSONS,
                 True))
seg("1-1292", qa("na arūpāvacarā", OTHER3.format("миру чувственных желаний", "миру форм"), True))
seg("1-1293", qa("pariyāpannā", RUPAKKH_ETC, False))
seg("1-1294", qa("apariyāpannā", f"Пути, плоды путей и {ASANKH}", False))
seg("1-1295", qa("niyyānikā", FOUR_PATHS, True))
seg("1-1296", qa("aniyyānikā", f"{EXC4}: {AGG4_PE}, {SABBA}", False))
seg("1-1297", qa("niyatā", "Пять действий с немедленным воздаянием, и то ложное воззрение, которое предопределено, "
                           f"и {low(FOUR_PATHS)}", True))
seg("1-1298", qa("aniyatā", f"{EXC4}: {AGG4_PE}, {SABBA}", False))
seg("1-1299", qa("sauttarā", RUPAKKH_ETC, False))
seg("1-1300", qa("anuttarā", LOKUTTARA, False))
seg("1-1301", qa("saraṇā", f"{F.ROOTS_A.replace(' – ', ': ')}; {KILESA}; {TAMSAMP} {AGG4_PE}; {KAMMA3}", False))
seg("1-1302", qa("araṇā", f"{cap(KABY)}, {SPH4}: {AGG4_PE}, {SABBA}", False), EXACT["Abhidhammadukaṃ."])

# ---------------------------------------------------------------- 4-03: suttanta pairs
seg("1-1303", qa("vijjābhāgino", "Явления, связанные с истинным знанием", True))
seg("1-1304", qa("avijjābhāgino", "Явления, связанные с неведением", True))
seg("1-1305", qa("vijjūpamā", "Мудрость на трёх низших благородных путях", False))
seg("1-1306", qa("vajirūpamā", "Мудрость на высшем пути состояния архата", False))
ALL_ARE = "Все {} явления {}."                                # Sabbepi kusalā/akusalā dhammā X.
note("Sabbepi akusalā / kusalā dhammā X.", ALL_ARE.format("неблагие / благие", "X (predicate)"))
H_O = ("Совестливость и страх перед дурным", "Бессовестность и отсутствие страха перед дурным")
seg("1-1307", f"{qa('bālā', H_O[1], False)} {ALL_ARE.format('неблагие', 'свойственны глупцам')}")
seg("1-1308", f"{qa('paṇḍitā', H_O[0], False)} {ALL_ARE.format('благие', 'свойственны мудрым')}")
seg("1-1309", f"{qa('kaṇhā', H_O[1], False)} {ALL_ARE.format('неблагие', 'являются тёмными')}")
seg("1-1310", f"{Q('sukkā')} {H_O[0]} – {A('sukkā')[:-1]}? {ALL_ARE.format('благие', 'являются светлыми')}")
seg("1-1311", f"{qa('tapanīyā', 'Дурное поведение телом, дурное поведение речью, дурное поведение умом', False)} "
              f"{ALL_ARE.format('неблагие', 'причиняют мучения')}")
seg("1-1312", f"{qa('atapanīyā', 'Благое поведение телом, благое поведение речью, благое поведение умом', False)} "
              f"{ALL_ARE.format('благие', 'не причиняют мучений')}")
NAMING = ("То, что есть исчисление, общепринятое название, обозначение, обиходное слово, имя, наречение, название, "
          "выражение, словесная форма, высказывание тех или иных явлений")
note("Yā tesaṃ tesaṃ dhammānaṃ saṅkhā samaññā paññatti vohāro nāmaṃ nāmakammaṃ nāmadheyyaṃ nirutti byañjanaṃ "
     "abhilāpo", NAMING)
ALL_PH = "Все явления являются {}."                           # Sabbeva dhammā X-pathā.
for _sid, _a, _b in (("1-1313", "adhivacanā", "adhivacanapathā"), ("1-1314", "nirutti", "niruttipathā"),
                     ("1-1315", "paññatti", "paññattipathā")):
    _path = once(N[_b], "явления, являющиеся ", "")
    seg(_sid, f"{qa(_a, NAMING, True)} {ALL_PH.format(_path)}")
seg("1-1316", define("nāmaṃ", f"{cap(AGG4.replace(' и совокупность сознания', ', совокупность сознания'))} и {ASANKH}",
                     False))
seg("1-1317", define("rūpaṃ", F.FOUR_GREAT))
assert R["1-1317"][0].split("? ", 1)[1].split(", – ")[0] + ", – " in T.EKAKA_Q_R
seg("1-1318", define("avijjā", f"То, что есть {MOHA_PE}"))
seg("1-1319", define("bhavataṇhā", BHAVA_PE))
for _sid, _k in (("1-1320", "bhavadiṭṭhi"), ("1-1321", "vibhavadiṭṭhi"), ("1-1322", "sassatadiṭṭhi"),
                 ("1-1323", "ucchedadiṭṭhi"), ("1-1324", "antavā diṭṭhi"), ("1-1325", "anantavā diṭṭhi")):
    seg(_sid, define(_k, f"{SELF_WORLD[_k]}; то, что есть такое {DIITHI_PE}"))
for _sid, _k in (("1-1326", "pubbantānudiṭṭhi"), ("1-1327", "aparantānudiṭṭhi")):
    seg(_sid, define(_k, VIEW_ARISES.format(ARABBHA[_k], DIITHI_PE)))
seg("1-1328", define("ahirikaṃ", AHIRI))
seg("1-1329", define("anottappaṃ", ANOTTAPPA))
seg("1-1330", define("hirī", HIRI))
seg("1-1331", define("ottappaṃ", OTTAPPA))
seg("1-1332", define("dovacassatā", DOVACASSA))
seg("1-1333", define("pāpamittatā", PAPAMITTA, False))
seg("1-1334", define("sovacassatā", SOVACASSA))
seg("1-1335", define("kalyāṇamittatā", KALYANAMITTA, False))
seg("1-1336", define("āpattikusalatā", "И пять классов проступков являются проступками, и семь классов проступков "
                                       "являются проступками. " + SKILL.format("в этих проступках")))
seg("1-1337", define("āpattivuṭṭhānakusalatā", SKILL.format("в избавлении от этих проступков")))
seg("1-1338", define("samāpattikusalatā", "Есть медитативное достижение с направленной мыслью и удержанием мысли, "
                                          "есть медитативное достижение без направленной мысли, только с удержанием "
                                          "мысли, есть медитативное достижение без направленной мысли и без удержания "
                                          "мысли. " + SKILL.format("в этих медитативных достижениях")))
seg("1-1339", define("samāpattivuṭṭhānakusalatā", SKILL.format("в выходе из этих медитативных достижений")))
seg("1-1340", define("dhātukusalatā", f"Восемнадцать элементов: {'; '.join(ELEMENTS18)}. "
                                      + SKILL.format("в этих элементах")))
seg("1-1341", define("manasikārakusalatā", SKILL.format("во внимании к этим элементам")))
seg("1-1342", define("āyatanakusalatā", f"Двенадцать сфер восприятия – {', '.join(SPHERES12)}. "
                                        + SKILL.format("в этих сферах восприятия")))
seg("1-1343", define("paṭiccasamuppādakusalatā", f"{PS_CHAIN}. {TATTHA_PANNA}"))
seg("1-1344", define("ṭhānakusalatā", f"{TTHANA}; {low(TATTHA_PANNA)}"))
seg("1-1345", define("aṭṭhānakusalatā", f"{ATTHANA}; {low(TATTHA_PANNA)}"))
seg("1-1346", define("ajjavo", AJJAVA))
seg("1-1347", define("maddavo", MADDAVA))
seg("1-1348", define("khanti", KHANTI))
seg("1-1349", f"{define('soraccaṃ', f'То, что есть {NONTRANS}')} {ALL_RESTRAINT.format(SUT['soraccaṃ'][1])}")
seg("1-1350", define("sākhalyaṃ", SAKHALYA))
seg("1-1351", define("paṭisanthāro", PATISANTHARA))
seg("1-1352", define("indriyesu aguttadvāratā", DOORS_NOT))
seg("1-1353", define("bhojane amattaññutā", FOOD_NOT))
seg("1-1354", define("indriyesu guttadvāratā", DOORS))
seg("1-1355", define("bhojane mattaññutā", FOOD))
seg("1-1356", define("muṭṭhasaccaṃ", MUTTHASACCA))
seg("1-1357", define("asampajaññaṃ", f"То, что есть {MOHA_PE}"))
seg("1-1358", define("sati", f"То, что есть {S.S_SATI}"))
seg("1-1359", define("sampajaññaṃ", f"То, что есть {PANNA_PE}"))
seg("1-1360", define("paṭisaṅkhānabalaṃ", f"То, что есть {PANNA_PE}"))
seg("1-1361", f"{define('bhāvanābalaṃ', BHAVANA)} Семь факторов пробуждения также являются "
              f"{SUT['bhāvanābalaṃ'][1]}.")
seg("1-1362", define("samatho", f"То, что есть {SAMADHI_PE}"))
seg("1-1363", define("vipassanā", f"То, что есть {PANNA_PE}"))
seg("1-1364", define("samathanimittaṃ", f"То, что есть {SAMADHI_PE}"))
seg("1-1365", define("paggāhanimittaṃ", f"То, что есть {VIRIYA_PE}"))
seg("1-1366", define("paggāho", f"То, что есть {VIRIYA_PE}"))
seg("1-1367", define("avikkhepo", f"То, что есть {SAMADHI_PE}"))
seg("1-1368", f"{define('sīlavipatti', f'То, что есть {TRANS}')} Всякая безнравственность является "
              f"{SUT['sīlavipatti'][1]}.")
seg("1-1369", f"{define('diṭṭhivipatti', f'{NATTHI}; то, что есть такое {DIITHI_PE}')} "
              f"{cap(F.ALL_WRONG.format(SUT['diṭṭhivipatti'][1]))}.")
seg("1-1370", f"{define('sīlasampadā', f'То, что есть {NONTRANS}')} {ALL_RESTRAINT.format(SUT['sīlasampadā'][1])}")
seg("1-1371", f"{define('diṭṭhisampadā', f'{ATTHI}; то, что есть такая {PANNA_PE}')} Всякое правильное воззрение "
              f"является {SUT['diṭṭhisampadā'][1]}.")
seg("1-1372", f"{define('sīlavisuddhi', f'То, что есть {NONTRANS}')} {ALL_RESTRAINT.format(SUT['sīlavisuddhi'][1])}")
seg("1-1373", f"{tq('diṭṭhivisuddhi')} Знание того, что действия являются собственностью существа, знание, "
              f"согласующееся с истинами, знание обладающего путём, знание обладающего плодом.")
seg("1-1374", f"{kho('1-M2-138', 0)} – то, что есть {PANNA_PE}.")
seg("1-1375", f"{kho('1-M2-138', 1)} – то, что есть {VIRIYA_PE}.")
seg("1-1376", f"«Потрясённость» – страх рождения, страх старения, страх болезни, страх смерти. «Обстоятельство, "
              f"которое должно потрясать» {S.spell('Sī.', 'saṃvejanīyaṃ')} – рождение, старение, болезнь, смерть.")
assert S.SUTTA_ITEMS["1-M2-139"][0][1].startswith("Потрясённость в обстоятельствах, которые должны потрясать")
seg("1-1377", f"{kho('1-M2-139', 1)} – вот монах ради невозникновения невозникших дурных неблагих явлений {STRIVE}; "
              f"ради устранения возникших дурных неблагих явлений {STRIVE}; ради возникновения невозникших благих "
              f"явлений {STRIVE}; ради сохранения, неутраты, умножения, обширности, развития и завершённости возникших "
              f"благих явлений {STRIVE}.")
seg("1-1378", f"{kho('1-M2-140', 0)} – то, что есть желание большего у того, кто не доволен развитием благих явлений.")
seg("1-1379", f"{kho('1-M2-140', 1)} – то, что есть в развитии благих явлений тщательность действий, постоянство "
              f"действий, безостановочность действий, неослабевающая деятельность, неотступное желание, неотступное "
              f"несение бремени, практика, развитие, многократное повторение.")
assert "неотступное желание, неотступное несение бремени" in S.S_VIRIYA
seg("1-1380", f"{kho('1-M2-141', 0)} – три истинных знания – знание припоминания прежних жизней является истинным "
              f"знанием, знание о смерти и новом рождении существ является истинным знанием, знание об уничтожении "
              f"влечений является истинным знанием.")
seg("1-1381", f"{kho('1-M2-141', 1)} – два вида освобождения – освобождённость ума "
              f"{S.reading('Sī., Syā.', 'cittassa ca')} и нирвана.")
seg("1-1382", f"{kho('1-M2-142', 0)} – знание обладающего путём.")
seg("1-1383", f"{kho('1-M2-142', 1)} – знание обладающего плодом.", EXACT["Nikkhepakaṇḍaṃ niṭṭhitaṃ."])

# =========================================================================================
# 7. Line dispatch, checks, build
# =========================================================================================
Q_RE = re.compile(r"^Katame dhammā (.+?)\? ")
A_RE = re.compile(r"ime dhammā ([^–?]+?)\.$")
LATIN = re.compile(r"[A-Za-zĀāĪīŪūṂṃṄṅÑñṬṭḌḍṆṇḶḷ]")


def check_line(sid, p, r):
    assert p.count("–") + p.count("—") == r.count("–") and "—" not in r, ("dash", sid, p.count("–"), r.count("–"))
    assert p.count(PE) == r.count(ELL), ("pe", sid, p.count(PE), r.count(ELL))
    assert p.count("?") == r.count("?"), ("question", sid, p.count("?"), r.count("?"))
    assert p.endswith("?") == r.endswith("?"), ("end", sid)
    assert p.startswith("#") == r.startswith("#"), ("heading", sid)
    assert "  " not in r and " ," not in r and ",," not in r and " ." not in r and ";;" not in r, ("spacing", sid, r)
    assert ", –" not in r.replace(", – ", "") and ":-" not in r, ("dash spacing", sid)
    assert not re.search(r"(?<![А-Яа-яЁё])ли(?![А-Яа-яЁё])", r), ("li", sid)
    stripped = re.sub(r"\[[^\]]*\]", "", r)
    assert not LATIN.search(stripped), ("latin", sid, LATIN.search(stripped).group(0))
    m = Q_RE.match(p)
    if m:
        assert r.startswith(Q(m.group(1)) + " "), ("q-frame", sid, m.group(1))
    m = A_RE.search(p)
    if m and m.group(1) in N:
        assert r.endswith(A(m.group(1))), ("a-frame", sid, m.group(1), r[-80:])


def strip_id(lines):
    return [re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", x) for x in lines]


def build(part):
    segs = S.segments(S.PALI / part)
    ru = {}
    for sid, plines in segs:
        plines = strip_id(plines)
        if sid in R:
            rlines = R[sid]
        else:
            assert len(plines) == 1 and plines[0] in EXACT, (sid, plines[0][:80])
            rlines = [EXACT[plines[0]]]
        assert len(rlines) == len(plines), (sid, len(plines), len(rlines))
        for p, r in zip(plines, rlines):
            check_line(sid, p, r)
        ru[sid] = rlines
    return ru, segs


def consistency(all_segs, all_ru):
    """identical Pāli lines -> identical Russian, inside 4-02/4-03 and against 4-01"""
    seen = {}
    for sid, plines in S.segments(S.PALI / "4-01-nikkhepakandam.md"):
        if sid in F.R:
            for p, r in zip(strip_id(plines), F.R[sid]):
                seen.setdefault(p, (r, "4-01 ^" + sid))
    n_401 = 0
    for sid, plines in all_segs:
        for p, r in zip(strip_id(plines), all_ru[sid]):
            if p in seen:
                assert seen[p][0] == r, ("inconsistent", sid, seen[p][1], p[:60])
                n_401 += seen[p][1].startswith("4-01")
            else:
                seen[p] = (r, "^" + sid)
    return n_401


def main():
    all_segs, all_ru = [], {}
    for part in PARTS:
        ru, segs = build(part)
        all_segs += segs
        all_ru.update(ru)
    unused = set(R) - set(all_ru)
    assert not unused, unused
    n = consistency(all_segs, all_ru)
    for part in PARTS:
        segs = S.segments(S.PALI / part)
        S.emit(S.PALI / part, {s: all_ru[s] for s, _ in segs}, S.OUT / part)
    print("lines identical to 4-01 Pāli, checked identical Russian:", n)
    notes()


def notes():
    L = ["# pi-1 Russian rails: new formulas of 4-02 and 4-03", "",
         "Generated by build_rails_4-02_4-03_ru.py from its fixed strings; import that file instead of retyping. "
         "Strings already in ru-rails-formulas.md or the notes of chapters 2, 3 and 4-01 are not repeated "
         "(the frames, the craving, hatred, delusion, doubt, view, conceit strings and the ten views come from "
         "build_rails_4-01_ru.py). Matrix names in the question and answer frames come verbatim from "
         "build_rails_sample_ru.py.", "",
         "Punctuation before the Pāli dash: «X – это …» after a plain noun or list; «…, – это …» only where the dash "
         "closes a participial phrase or a subordinate clause (coordinator 2026-11-14).", "",
         "The devanāgarī visarga «ः» used as a punctuation mark (^1-1168, 1181, 1240, 1241, 1369, 1371) = «;»; where "
         "the Pāli has a full stop instead (^1-1167, 1238), the Russian has one too.", "",
         "## Formulas (Pāli = Russian)", ""]
    for p, r in NOTES:
        L.append(f"{p} = {r}")
    L += ["", "## Decisions and termbase misfits (reported)", "",
          "Natthi (termbase «ничего не значить», nihilist view): «ничего не значит» for dinnaṃ, yiṭṭhaṃ, hutaṃ, loko, "
          "mātā, pitā; «нет» where existence is denied (phalaṃ vipāko, sattā opapātikā, samaṇabrāhmaṇā), as pi-4 "
          "^4-62; atthi = «имеет значение» / «есть» (pi-4 ^4-82).",
          "vipāko (natthi … phalaṃ vipāko) = «результат»: the termbase has only «результат действий» "
          "(compound member) and «являющийся результатом».",
          "nāmaṃ in the naming list (^1-1313 … 1315) = «имя»: the termbase has only «умственное» (nāmarūpa).",
          "byañjanaṃ (^1-1313 … 1315) = «словесная форма», assaddhā «лишены веры», appassutā «мало слышали», "
          "sambhatti «привязанность», ajjavatā «прямодушие», pariyonāho «полная "
          "окутанность», līyitattaṃ «состояние косности», kukkuccāyitattaṃ «состояние мучения угрызениями», "
          "anubyañjana «детали», aṭṭhitakiriyatā «безостановочность действий», anolīnavuttitā «неослабевающая "
          "деятельность», sucarita «благое поведение»: not in the termbase (pi-4 models where it has them).",
          "paccayā in ṭhāna / aṭṭhāna (^1-1344, 1345) = «условия» (noun); the termbase has only «обусловленный» "
          "(dependent origination, used in ^1-1343).",
          "yāpanāya (^1-1355) = «поддержание»: the termbase «сохранение» is given to ṭhitiyā in the same phrase.",
          "upaga (ākāsānañcāyatanupage / nevasaññānāsaññāyatanupage deve, ^1-1291) = «рождённых в сфере …».",
          "X Y-ena … ceva …-sampayutto ca (^1-1176, 1231, 1257): the frame of 4-01 «X по отношению к Y является … и "
          "связан(а/о) с …» is kept for consistency; the termbase entries for some of these pairs (e.g. uddhaccaṃ "
          "ahirikena «беспокойство вместе с бессовестностью», kāmupādānaṃ diṭṭhupādānena) have «вместе с».",
          "paranimmitavasavattī deve (^1-1287) = «богов, властвующих над творениями других» (termbase nimmita "
          "«творения», vasavattī «властвующий»; pi-4 had «созданным другими»); brahmaloka «мир Брахмы» and "
          "akaniṭṭhā devā «боги Аканиттха» as pi-5 (not in the termbase).",
          "kāyassa in the torpor definition (^1-1163) = «умственного тела» (termbase sense 2).",
          "Cittaṃ na vattabbaṃ (^1-1198, 1200) = «Ум нельзя определить – ни как …, ни как не …» (termbase vattabbaṃ "
          "«определить»).",
          "hotīti in the dependent-origination formula (^1-1343): «так происходит возникновение …» (the plain «есть» "
          "does not read as Russian here).",
          "Source slips kept as written: ^1-1310 «ime dhammā sukkā?» ends with «?»; ^1-1301 has no dash after "
          "«Tīṇi akusalamūlāni» (colon in the Russian); ^1-1189 lacks a comma in «rūpāvacarā arūpāvacarā» "
          "(standard Russian frame); ^1-1285 / 1286 list the spheres the other way round from the sibling pairs "
          "(arūpāvacara in the positive, not in the negative); ^1-1283 / 1285 start the associated aggregates "
          "from saññākkhandho; ^1-1160 punctuates the grounds of annoyance with «;» (mirrored); ^1-1178 and 1259 "
          "have «kusalābyākatā» where the sibling pairs have «kusalākusalābyākatā» (rendered as written).",
          "Variant labels: nīvaraṇāni (Syā.), samaggatā (Ka.), upādāya (Sī., Ka.), cittassa ca (Sī., Syā.) = "
          "«вариант чтения»; kāmūpādānaṃ … (Sī.), paranimmitavasavattideve, akaniṭṭhadeve (Sī., Ka.), "
          "diṭṭhadhammasukhavihārassa (Ka.), saṃvejanīyaṃ (Sī.) = «вариант написания».",
          "Headings: «#### Suttantikadukanikkhepaṃ» = «Сводка пар из наставлений» (4-01: «Сводка пар»); "
          "«Abhidhammadukaṃ.» = «Пары Абхидхаммы.» (4-01: «Tikaṃ.» = «Тройки.»)."]
    (HERE / "notes-4-02_4-03.md").write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")
    print("wrote", HERE / "notes-4-02_4-03.md")


if __name__ == "__main__":
    main()
