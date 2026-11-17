"""Builder for the Russian rails translation of pi-2 (Vibhaṅga, plain audience), chapter 16
(Ñāṇavibhaṅgo ^2-16-0 … ^2-831).

Writes (only when run as a script):
  AI_translation/russian/pi-2-russian-plain-rails_split_chapters/16-nanavibhango.md
  0-INBOX/temp/pipeline/pi-2-ru/rails/notes-16.md   (new recurring formulas, Pāli = Russian)

Every Russian string comes from the fixed tables and functions below, so identical Pāli gives identical Russian.
Imported read-only: the approved sample builder (S) and the builders of chapters 1 (K1), 2-3 (K23), 4-5 (K45),
6 (K6), 7-9 (K79), 10-12 (K10) and 13-15 (K1315). Nothing of theirs is changed.

Reused: the matrix item names of ch. 1 (pi-1 matrix wording, here said of «мудрость»), the wisdom list of ch. 4-5
(pi-1 ^1-1359), the mind list of ch. 7, the jhāna / formless formulas of ch. 10-12, the knowledge and analytical-
knowledge strings of ch. 15, the dependent-origination links of ch. 6 and the ten views of pi-1 ^1-1105.

usage: python -I -X utf8 build_rails_16_ru.py
"""
import pathlib
import re
import sys

RAILS = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru\rails")
sys.path.insert(0, str(RAILS))
import build_rails_sample_ru as S   # noqa: E402  (importing writes nothing)
import build_rails_1_ru as K1       # noqa: E402
import build_rails_2_3_ru as K23    # noqa: E402
import build_rails_4_5_ru as K45    # noqa: E402
import build_rails_6_ru as K6       # noqa: E402
import build_rails_7_9_ru as K79    # noqa: E402
import build_rails_10_12_ru as K10  # noqa: E402
import build_rails_13_15_ru as K1315  # noqa: E402

PART = "16-nanavibhango.md"
NOTES_PATH = RAILS / "notes-16.md"
PI1_RU = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\russian\pi-1-russian-plain.md")
cap, low, nlist = S.cap, K1.low, K45.nlist
SLIPS = []


def slip(msg):
    if msg not in SLIPS:
        SLIPS.append(msg)


# =========================================================================== frame strings
NV = "основа знания"                                    # ñāṇavatthu (termbase)
WIS = K45.WISDOM_SHORT                                  # paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi
YA_TATTHA = f"то, что здесь есть {WIS}"                 # yā tattha paññā … (pi-1 ^1-1344, ch. 12)
YA_EVARUPA = f"то, что есть такая {WIS}"               # yā evarūpā paññā …
ARISE = f"возникают {WIS}"                              # yā uppajjati paññā …
LETTER = {"ka": "а", "kha": "б", "ga": "в", "gha": "г"}
NUM_LOC = {"dvīsu": "двух", "tīsu": "трёх", "catūsu": "четырёх"}
TATH = "Татхагата"
FEATS = ("заявляет о своём положении вожака, издаёт львиный рык в собраниях, приводит в движение колесо "
         "Брахмы")                                      # āsabhaṃ ṭhānaṃ paṭijānāti, parisāsu sīhanādaṃ nadati, …
POWER_OF = "силой Татхагаты, присущей Татхагате"         # tathāgatassa tathāgatabalaṃ (instrumental)
POWERS10 = "десять сил Татхагаты, присущих Татхагате"  # dasa tathāgatassa tathāgatabalāni
YATHA = "как есть на самом деле"                        # yathābhūtaṃ (termbase)


def vidha_head(n):
    """<N>vidhena ñāṇavatthu – = Основа знания <N> –"""
    return f"{cap(NV)} {S.NUMW[n]} –"


def vidha_end(n):
    """Evaṃ <N>vidhena ñāṇavatthu. = Такова основа знания <N>."""
    return f"Такова {NV} {S.NUMW[n]}."


def close_label(n):
    """Ekakaṃ. / Dukaṃ. … (closing labels, termbase) = По одному. / На два вида. …"""
    return f"{cap(S.NUMW[n])}."


def called(ins):
    return f"это называется «{ins}»"


def lab(raw):
    """(1. Ka) / (Kha) / (Kha-gha) / (12-21) -> (1. а) / (б) / (б-г) / (12-21)"""
    m = re.match(r"^(\d+)\. (\w+)$", raw)
    if m:
        return f"({m.group(1)}. {LETTER[m.group(2).lower()]})"
    if re.match(r"^[\d-]+$", raw):
        return f"({raw})"
    return "(" + "-".join(LETTER[x.lower()] for x in raw.split("-")) + ")"


# =========================================================================== wisdom phrases (pi-1 matrix names)
PRE = {"внутренняя и внешняя", "этически неопределённая"}   # multi-word attributes that stay before the noun


def pk(w):
    """Pāli feminine attribute of paññā -> K1.ITEMS key"""
    w = w[0].lower() + w[1:]
    parts = w.split(" ")
    if len(parts) == 2 and parts[0].endswith("vippayuttā"):
        return parts[0][:-1] + "a" + pk(parts[1])
    last = parts[-1]
    if last == "maggādhipatinī":
        last = "maggādhipati"
    elif last.endswith("inī"):
        last = last[:-3] + "ī"
    elif last.endswith("ā"):
        last = last[:-1] + "o"
    return " ".join(parts[:-1] + [last])


PH = {   # paññā phrases without a matrix item: key -> (nominative, instrumental)
    "atthajāpiko": ("мудрость, производящая цель", "мудростью, производящей цель"),
    "jāpitattho": ("мудрость, цель которой произведена", "мудростью, цель которой произведена"),
    "cintāmayo": ("мудрость, основанная на размышлении", "мудростью, основанной на размышлении"),
    "sutamayo": ("мудрость, основанная на услышанном", "мудростью, основанной на услышанном"),
    "bhāvanāmayo": ("мудрость, основанная на развитии ума", "мудростью, основанной на развитии ума"),
    "dānamayo": ("мудрость, основанная на даянии", "мудростью, основанной на даянии"),
    "sīlamayo": ("мудрость, основанная на нравственности", "мудростью, основанной на нравственности"),
    "adhisīle": ("мудрость в высшей нравственности", "мудростью в высшей нравственности"),
    "adhicitte": ("мудрость в высшем уме", "мудростью в высшем уме"),
    "adhipaññāya": ("мудрость в высшей мудрости", "мудростью в высшей мудрости"),
    "hānabhāgī": ("мудрость, ведущая к упадку", "мудростью, ведущей к упадку"),
    "ṭhitibhāgī": ("мудрость, ведущая к устойчивости", "мудростью, ведущей к устойчивости"),
    "visesabhāgī": ("мудрость, ведущая к отличию", "мудростью, ведущей к отличию"),
    "nibbedhabhāgī": ("мудрость, ведущая к проникновению", "мудростью, ведущей к проникновению"),
}
for _k, _r in (("vitakka", "с направленной мыслью"), ("vicāra", "с удержанием мысли"), ("pīti", "с восторгом"),
               ("sukha", "со счастьем"), ("upekkhā", "с невозмутимостью"),
               ("vitakkavicāra", "с направленной мыслью и удержанием мысли")):
    PH[f"{_k}sampayutto"] = (f"мудрость, связанная {_r}", f"мудростью, связанной {_r}")
    PH[f"{_k}vippayutto"] = (f"мудрость, не связанная {_r}", f"мудростью, не связанной {_r}")
PH["vitakkavicāravippayutto"] = ("мудрость, не связанная ни с направленной мыслью, ни с удержанием мысли",
                                 "мудростью, не связанной ни с направленной мыслью, ни с удержанием мысли")
PH["vitakkavippayutta vicārasampayutto"] = (
    "мудрость, не связанная с направленной мыслью, но связанная с удержанием мысли",
    "мудростью, не связанной с направленной мыслью, но связанной с удержанием мысли")
for _p, _r in (("dukkha", "с трудным"), ("sukha", "с лёгким")):     # the four modes of progress (termbase phrases)
    for _q, _s in (("dandha", "медленным"), ("khippa", "быстрым")):
        PH[f"{_p}paṭipadā {_q[:-1]}ābhiñño"] =(f"мудрость {_r} способом практики и {_s} высшим знанием",
                                           f"мудростью {_r} способом практики и {_s} высшим знанием")
for _a, _ar in (("paritto", "ограниченная"), ("appamāṇo", "безмерная")):          # the four objects (termbase)
    for _b, _br in (("parittārammaṇo", "ограниченным"), ("appamāṇārammaṇo", "безмерным")):
        _ai = _ar[:-2] + "ой"
        PH[f"{_a} {_b}"] = (f"мудрость {_ar} и с {_br} объектом", f"мудростью {_ai} и с {_br} объектом")


def ph(key):
    """-> (nominative, instrumental) of «мудрость» with the attribute"""
    if key in PH:
        return PH[key]
    if key == "uppādī":
        return ("мудрость, которой предстоит возникнуть", "мудростью, которой предстоит возникнуть")
    f = K1.item(key)["f"]
    if f.startswith("явление "):
        t = f[len("явление "):]
        return (f"мудрость {t}", f"мудростью {t}")
    ins = K1._infl(f, K1._wins)
    if " " not in f or f in PRE:
        return (f"{f} мудрость", f"{ins} мудростью")
    return (f"мудрость, {f}", f"мудростью, {ins}")


def pkey_full(p):
    """«X paññā» / «paññā …» name -> PH / ITEMS key"""
    p = p[0].lower() + p[1:]
    if p.endswith(" paññā"):
        p = p[:-len(" paññā")]
    a = p.split(" ")
    if len(a) == 2 and a[0] in ("dukkhapaṭipadā", "sukhapaṭipadā"):
        return f"{a[0]} {a[1][:-1]}o"
    if len(a) == 2 and a[0] in ("parittā", "appamāṇā"):
        return f"{pk(a[0])} {pk(a[1])}"
    if p.endswith("bhāginī"):
        return p[:-3] + "ī"
    if p in ("adhisīle", "adhicitte", "adhipaññāya"):
        return p
    if p == "vitakkavippayuttā vicārasampayuttā":
        return "vitakkavippayutta vicārasampayutto"
    return pk(p)


def byv(key, pl=False):
    """«atthi X» = «бывает / бывают X(ins)»"""
    it = K1.item(key)
    f = it["f"]
    verb = "бывают" if pl else "бывает"
    if f.startswith("явление "):
        return f"{verb} {f[len('явление '):]}"
    # K1's plural instrumental turns the noun «обучение» into «обученими» (sekkha triad); the noun stays
    return f"{verb} {it['insp'].replace('обученими', 'обучение') if pl else it['ins']}"


def join_items(items):
    """a Pāli comma list of phrases: «; » when a member before the last has its own comma"""
    sep = "; " if any(", " in x for x in items[:-1]) else ", "
    return sep.join(items)


# =========================================================================== locations of wisdom (bhūmīsu …)
LOC_RX = re.compile(r"(tīsu|catūsu) bhūmīsu (kusalābyākate|kusale|vipāke|kiriyābyākate)|(catūsu|tīsu) (maggesu|phalesu)"
                    r"|(dvīsu|tīsu) jhānesu|rūpāvacarārūpāvacarakusalābyākate|rūpāvacarārūpāvacarakusale"
                    r"|kāmāvacarakusalābyākate|rūpāvacarakusalābyākate|arūpāvacarakusalābyākate|kāmāvacarakusale"
                    r"|upariṭṭhimā arahattaphale")
LOC_KIND = {"kusalābyākate": "в благом и этически неопределённом", "kusale": "в благом",
            "vipāke": "в результатах действий", "kiriyābyākate": "в функциональном этически неопределённом"}
SPHERE = {"kāmāvacara": "к миру чувственных желаний", "rūpāvacara": "к миру форм", "arūpāvacara": "к миру без форм",
          "rūpāvacarārūpāvacara": "к миру форм и к миру без форм"}


def loc_unit(u):
    m = re.match(r"^(tīsu|catūsu) bhūmīsu (\S+)$", u)
    if m:
        return f"{LOC_KIND[m.group(2)]} на {NUM_LOC[m.group(1)]} уровнях", False
    m = re.match(r"^(catūsu|tīsu) (maggesu|phalesu)$", u)
    if m:
        return f"в {NUM_LOC[m.group(1)]} {'путях' if m.group(2) == 'maggesu' else 'плодах'}", False
    m = re.match(r"^(dvīsu|tīsu) jhānesu$", u)
    if m:
        return f"в {NUM_LOC[m.group(1)]} медитативных погружениях", False
    if u == "upariṭṭhimā arahattaphale":
        return "в высшем плоде состояния архата", False
    m = re.match(r"^(\S+?)kusal(ābyākate|e)$", u)
    head = "в благом и этически неопределённом" if m.group(2) == "ābyākate" else "в благом"
    return f"{head}, относящемся {SPHERE[m.group(1)]}", True


def loc(s):
    """Pāli location string -> (Russian «в … », ends with a participial clause)"""
    s = s[0].lower() + s[1:]
    units = [m.group(0) for m in LOC_RX.finditer(s)]
    assert " ".join(units) == s, (s, units)
    rus = [loc_unit(u) for u in units]
    texts = [r[0] for r in rus]
    if len(texts) == 1:
        return texts[0], rus[0][1]
    return ", ".join(texts[:-1]) + " и " + texts[-1], rus[-1][1]


def subject(s):
    """the subject before «paññā X paññā»: a location (wisdom in …) or an attribute (wisdom conjoined with …)"""
    try:
        t, comma = loc(s)
        return f"мудрость {t}", comma
    except (AssertionError, AttributeError, KeyError):
        nom = ph(pkey_full(s))[0]
        return nom, ", " in nom


def is_clause(subj_s, pred_key):
    """«<subject> paññā <X> paññā» = «<subject> является <X(ins)>»"""
    subj, comma = subject(subj_s)
    return f"{subj}{',' if comma else ''} является {ph(pred_key)[1]}"


SENT_RX = re.compile(r"^(.+?) paññā (.+?) paññā$")


def is_sentence(body):
    """«A paññā X paññā, B paññā Y paññā» (no final stop) -> Russian halves joined by «; »"""
    out = []
    for half in body.split(", "):
        m = SENT_RX.match(half)
        assert m, half
        out.append(is_clause(m.group(1), pkey_full(m.group(2))))
    return "; ".join(out)


# =========================================================================== names (questions and «… vuccati "X"»)
KNOW = dict(K1315.KNOW)


def know(k):
    return f"знание {KNOW[k]}", f"знанием {KNOW[k]}"


NAMES = {
    "āyakosallaṃ": ("умелость в росте", "умелостью в росте"),
    "apāyakosallaṃ": ("умелость в упадке", "умелостью в упадке"),
    "upāyakosallaṃ": ("умелость в средствах", "умелостью в средствах"),
    "kammassakatañāṇaṃ": ("знание собственности действий", "знанием собственности действий"),
    "saccānulomikaṃ ñāṇaṃ": ("знание, согласующееся с истинами", "знанием, согласующимся с истинами"),
    "maggasamaṅgissa ñāṇaṃ": ("знание обладающего путём", "знанием обладающего путём"),
    "phalasamaṅgissa ñāṇaṃ": ("знание обладающего плодом", "знанием обладающего плодом"),
    "dhamme ñāṇaṃ": ("знание явлений", "знанием явлений"),
    "anvaye ñāṇaṃ": ("знание по выводу", "знанием по выводу"),
    "pariye ñāṇaṃ": ("знание охвата умов", "знанием охвата умов"),
    "sammutiñāṇaṃ": ("условное знание", "условным знанием"),
    "paññā ācayāya no apacayāya": ("мудрость, ведущая к накоплению, а не к убыванию",
                                   "мудростью, ведущей к накоплению, а не к убыванию"),
    "paññā apacayāya no ācayāya": ("мудрость, ведущая к убыванию, а не к накоплению",
                                   "мудростью, ведущей к убыванию, а не к накоплению"),
    "paññā ācayāya ceva apacayāya ca": ("мудрость, ведущая и к накоплению, и к убыванию",
                                        "мудростью, ведущей и к накоплению, и к убыванию"),
    "paññā nevācayāya no apacayāya": ("мудрость, не ведущая ни к накоплению, ни к убыванию",
                                      "мудростью, не ведущей ни к накоплению, ни к убыванию"),
    "paññā nibbidāya no paṭivedhāya": ("мудрость, ведущая к разочарованию, а не к проникновению",
                                       "мудростью, ведущей к разочарованию, а не к проникновению"),
    "paññā paṭivedhāya no nibbidāya": ("мудрость, ведущая к проникновению, а не к разочарованию",
                                       "мудростью, ведущей к проникновению, а не к разочарованию"),
    "paññā nibbidāya ceva paṭivedhāya ca": ("мудрость, ведущая и к разочарованию, и к проникновению",
                                            "мудростью, ведущей и к разочарованию, и к проникновению"),
    "paññā neva nibbidāya no paṭivedhāya": ("мудрость, не ведущая ни к разочарованию, ни к проникновению",
                                            "мудростью, не ведущей ни к разочарованию, ни к проникновению"),
    "catasso paṭisambhidā": (K1315.FOUR_PS[0].lower() + K1315.FOUR_PS[1:], None),
    "catasso paṭipadā": ("четыре способа практики", None),
    "cattāri ārammaṇāni": ("четыре объекта", None),
    "pañcaṅgiko sammāsamādhi": ("пятичастное правильное сосредоточение", "пятичастным правильным сосредоточением"),
    "pañcañāṇiko sammāsamādhi": ("правильное сосредоточение с пятью знаниями",
                                 "правильным сосредоточением с пятью знаниями"),
    "chasu abhiññāsu paññā": ("мудрость в шести высших знаниях", None),
    "sattasattati ñāṇavatthūni": ("семьдесят семь основ знания", None),
    "catūsu maggesu catūsu phalesu paññā": ("мудрость в четырёх путях и в четырёх плодах", None),
    "navasu anupubbavihārasamāpattīsu paññā": (
        "мудрость в девяти медитативных достижениях последовательного пребывания", None),
}
for _x in ("dukkha", "jarāmaraṇa"):
    NAMES[f"{_x[:-1]}e ñāṇaṃ"] = know(_x)
    NAMES[f"{_x}nirodhagāminiyā paṭipadāya ñāṇaṃ"] = know(f"{_x}nirodhagāminiyā paṭipadāya")
NAMES["saṅkhāresu ñāṇaṃ"] = know("saṅkhāra")
NAMES["saṅkhāranirodhagāminiyā paṭipadāya ñāṇaṃ"] = know("saṅkhāranirodhagāminiyā paṭipadāya")


def name(p):
    p = p[0].lower() + p[1:]
    if p in NAMES:
        return NAMES[p]
    return ph(pkey_full(p))


# conditions of «… yā uppajjati paññā …» (Russian ends with a comma where a clause closes)
COND = {
    "Ariyamaggaṃ ārabbha": "В отношении благородного пути",
    "Ariyamaggaṃ adhipatiṃ karitvā": "Когда благородный путь сделан главенствующим,",
    "Dānaṃ ārabbha dānādhigaccha": "В отношении даяния, при осуществлении даяния,",
    "Sīlaṃ ārabbha sīlādhigaccha": "В отношении нравственности, при осуществлении нравственности,",
    "Pātimokkhasaṃvaraṃ saṃvarantassa": "У того, кто сдерживает себя сдержанностью свода монашеских правил,",
    "Rūpāvacarārūpāvacarasamāpattiṃ samāpajjantassa":
        "У того, кто входит в медитативное достижение, относящееся к миру форм или к миру без форм,",
    "Dukkhaṃ ārabbha": f"В отношении {KNOW['dukkha']}",
    "Jarāmaraṇaṃ ārabbha": f"В отношении {KNOW['jarāmaraṇa']}",
    "Saṅkhāre ārabbha": f"В отношении {KNOW['saṅkhāra']}",
}
for _p, _r in (("Paritte", "ограниченных"), ("Mahaggate", "возвышенных"), ("Appamāṇe", "безмерных"),
               ("Atīte", "прошлых"), ("Anāgate", "будущих"), ("Paccuppanne", "настоящих"), ("Ajjhatte", "внутренних"),
               ("Bahiddhā", "внешних"), ("Ajjhattabahiddhā", "внутренних и внешних")):
    COND[f"{_p} dhamme ārabbha"] = f"В отношении {_r} явлений"
COND["Bahiddhādhamme ārabbha"] = COND["Bahiddhā dhamme ārabbha"]
for _p, _r in (("Kicchena kasirena", "с трудом и тяготами"), ("Akicchena akasirena", "без труда и без тягот")):
    for _q, _s in (("dandhaṃ", "медленно"), ("khippaṃ", "быстро")):
        COND[f"{_p} samādhiṃ uppādentassa {_q} taṇṭhānaṃ abhijānantassa"] = (
            f"У того, кто {_r} порождает сосредоточение и {_s} постигает высшим знанием это состояние,")
for _p, _r in (("Samādhissa na nikāmalābhissa", "не обретает сосредоточение по желанию"),
               ("Samādhissa nikāmalābhissa", "обретает сосредоточение по желанию")):
    for _q, _s in (("thokaṃ", "немного"), ("vipulaṃ", "обширно")):
        COND[f"{_p} ārammaṇaṃ {_q} pharantassa"] = f"У того, кто {_r} и распространяет объект {_s},"
PE_COND = {   # «Xsamudayaṃ ārabbha…pe… Xnirodhaṃ ārabbha…pe… Xnirodhagāminiṃ paṭipadaṃ ārabbha»
    x: (f"В отношении {KNOW[x + 'samudaya']}… в отношении {KNOW[x + 'nirodha']}… в отношении "
        f"{KNOW[x + 'nirodhagāminiyā paṭipadāya']},") for x in ("dukkha", "jarāmaraṇa", "saṅkhāra")}

ARISE_RX = re.compile(r'^(.+?) yā uppajjati paññā pajānanā ?…pe… amoho dhammavicayo sammādiṭṭhi – (?:ayaṃ|idaṃ) '
                      r'vuccati "(.+?)("?)\.(?: (.*))?$')


def arise_sentence(body):
    """«<cond> yā uppajjati paññā …sammādiṭṭhi – ayaṃ vuccati "X". [tail]»"""
    m = ARISE_RX.match(body)
    assert m, body
    cond_p, nm, q, tail = m.groups()
    if not q:
        slip(f'^{SID["sid"]} «vuccati "{nm}. Evaṃ …»: the closing quote mark is missing (rendered as meant)')
    if "ādhigaccha" in cond_p:
        slip("^2-769 «dānādhigaccha», «sīlādhigaccha»: an unusual form (the termbase has no entry); rendered «при "
             "осуществлении даяния / нравственности»")
    pe = re.match(r"^(\w+?)samudayaṃ ārabbha…pe… \1nirodhaṃ ārabbha…pe… \1nirodhagāminiṃ paṭipadaṃ ārabbha$",
                  cond_p[0].lower() + cond_p[1:])
    cond = PE_COND[pe.group(1)] if pe else COND[cond_p[0].upper() + cond_p[1:]]
    r = f"{cond} {ARISE} – {called(name(nm)[1])}."
    if tail:
        r += " " + tail_sentences(tail)
    return r


TAIL = {}   # short closing sentences, filled below


def tail_sentences(t):
    return " ".join(TAIL[s] for s in K45.split_sents(t))


# =========================================================================== chapter strings
VIN_NOM = K1.VINN                                            # cakkhu -> зрительное сознание …
VIN_GEN = {k: v.replace("ое сознание", "ого сознания") for k, v in VIN_NOM.items()}
FIVE_V = "пять видов сознания"                               # pañca viññāṇā
BY_FIVE = "Пятью видами сознания"                            # pañcahi viññāṇehi
AFTER_FIVE = "И сразу после пяти видов сознания"             # pañcannaṃ viññāṇānaṃ samanantarāpi
AFTER_FIVE_MD = "сразу после пяти видов сознания даже элементом ума"   # … samanantarā manodhātuyāpi
POSTURES = "ни хождения, ни стояния, ни сидения, ни лежания"  # gamanaṃ vā ṭhānaṃ vā nisajjaṃ vā seyyaṃ vā
REAL = "мудрость, проясняющая основу такой, какова она есть"   # yāthāvakavatthuvibhāvanā paññā
V_KINCI = "[вариант написания (Sī., Ka.): kiñci]"
ACTS = {   # the verb phrases of the onefold matrix (subject: indefinite «они»)
    "na kañci dhammaṃ paṭivijānāti": "не распознают никакого явления",
    "na kañci iriyāpathaṃ kappeti": "не принимают никакого положения тела",
    "na kāyakammaṃ na vacīkammaṃ paṭṭhapeti": "не совершают ни телесного действия, ни речевого действия",
    "na kusalākusalaṃ dhammaṃ samādiyati": "не принимают на себя благого или неблагого явления",
    "na samāpajjati na vuṭṭhāti": "не входят в медитативное достижение и не выходят из него",
    "na cavati na uppajjati": "не умирают и не рождаются",
    "na supati na paṭibujjhati na supinaṃ passati": "не засыпают, не просыпаются, не видят снов",
}
EKA = {   # the onefold matrix lines (3) … (13) and the base pairs: Pāli -> Russian
    "Uppannavatthukā uppannārammaṇā": "Имеют возникшую основу и возникший объект",
    "Purejātavatthukā purejātārammaṇā": "Имеют ранее возникшую основу и ранее возникший объект",
    "Ajjhattikavatthukā bāhirārammaṇā":
        "Имеют основу, относящуюся к внутреннему, и объект, относящийся к внешнему",
    "Asambhinnavatthukā asambhinnārammaṇā": "Имеют неразрушенную основу и неразрушенный объект",
    "Nānāvatthukā nānārammaṇā": "Имеют разные основы и разные объекты",
    "Na aññamaññassa gocaravisayaṃ paccanubhonti": "Не испытывают сферы действия друг друга",
    "Na asamannāhārā uppajjanti": "Не возникают без обращения внимания",
    "Na amanasikārā uppajjanti": "Не возникают без внимания",
    "Na abbokiṇṇā uppajjanti": "Не возникают непрерывной чередой",
    "Na apubbaṃ acarimaṃ uppajjanti": "Не возникают одновременно",
    "Na aññamaññassa samanantarā uppajjanti": "Не возникают сразу друг после друга",
    "Pañca viññāṇā anābhogā": "Пять видов сознания лишены вовлечённости",
}
for _a, _r in ACTS.items():
    EKA[f"Pañcahi viññāṇehi {_a}"] = f"{BY_FIVE} {_r}"
    EKA[f"Pañcannaṃ viññāṇānaṃ samanantarāpi {_a}"] = f"{AFTER_FIVE} {_r}"
EKA_GLOSS = {   # «X»ti … (the onefold exposition, ^2-762 … ^2-766): quoted Pāli -> (quote, explanation)
    "Pañca viññāṇā uppannavatthukā, uppannārammaṇā": (
        "Пять видов сознания имеют возникшую основу, возникший объект",
        "они возникают на возникшей основе и на возникшем объекте"),
    "Purejātavatthukā, purejātārammaṇā": (
        "Имеют ранее возникшую основу, ранее возникший объект",
        "они возникают на ранее возникшей основе и на ранее возникшем объекте"),
    "Ajjhattikavatthukā, bāhirārammaṇā": (
        "Имеют основу, относящуюся к внутреннему, объект, относящийся к внешнему",
        "основа пяти видов сознания относится к внутреннему, объекты относятся к внешнему"),
    "Asambhinnavatthukā, asambhinnārammaṇā": (
        "Имеют неразрушенную основу, неразрушенный объект",
        "они возникают на неразрушенной основе и на неразрушенном объекте"),
    "Nānāvatthukā, nānārammaṇā": (
        "Имеют разные основы, разные объекты",
        ", ".join(f"у {VIN_GEN[k]} другие основа и объект" for k in ("cakkhu", "sota", "ghāna", "jivhā", "kāya"))),
    "Na asamannāhārā uppajjanti": (EKA["Na asamannāhārā uppajjanti"], "они возникают у того, кто обращает внимание"),
    "Na amanasikārā uppajjanti": (EKA["Na amanasikārā uppajjanti"], "они возникают у того, кто уделяет внимание"),
    "Na abbokiṇṇā uppajjanti": (EKA["Na abbokiṇṇā uppajjanti"], "они не возникают одно за другим"),
    "Na apubbaṃ acarimaṃ uppajjanti": (EKA["Na apubbaṃ acarimaṃ uppajjanti"], "они не возникают в один момент"),
    "Pañca viññāṇā anābhogā": (EKA["Pañca viññāṇā anābhogā"],
                               "у пяти видов сознания нет ни поворота ума, ни вовлечённости, ни обращения внимания, "
                               "ни внимания"),
    "Aññatra abhinipātamattā": ("Кроме простого столкновения", "кроме простого попадания в поле восприятия"),
}
for _a, _r in ACTS.items():
    _q1, _q2 = EKA[f"Pañcahi viññāṇehi {_a}"], EKA[f"Pañcannaṃ viññāṇānaṃ samanantarāpi {_a}"]
    _post = f" – {POSTURES}" if "iriyāpathaṃ" in _a else ""
    EKA_GLOSS[f"Pañcahi viññāṇehi {_a}"] = (_q1, f"{low(BY_FIVE)} {_r}{_post}")
    EKA_GLOSS[f"Pañcannaṃ viññāṇānaṃ samanantarāpi {_a}"] = (_q2, f"{AFTER_FIVE_MD} {_r}{_post}")


def gloss(q, expl):
    return f"«{q}»: {expl}."


# the five kinds of consciousness: predicates (plural; ch. 1 matrix items, pi-1 wording)
VP_LOCAL = {"sappaccayo": "имеют условия", "saṅkhato": "являются обусловленными",
            "no apariyāpanno": "не относятся к явлениям, не принадлежащим к кругам существования"}


def vp(key):
    if key in VP_LOCAL:
        return VP_LOCAL[key]
    if key in K1.ITEMS:
        return K1.ITEMS[key]["vp"]
    assert key.startswith("na "), key
    return "не " + K1.ITEMS[key[3:]]["vp"]


def pl2key(w):
    if w == "na hetū":
        return "na hetu"
    if w.endswith("gāmino"):
        return w[:-len("gāmino")] + "gāmī"
    assert w.endswith("ā"), w
    return w[:-1] + "o"


def meva2key(w):
    b = w[:-len("meva")]
    if b.endswith("gāmi"):
        return b[:-1] + "ī"
    if b.endswith("hetu"):
        return b
    assert b.endswith("a"), w
    return b[:-1] + "o"


MEVA_TAIL = {"uppannaṃ manoviññāṇaviññeyyameva": "будучи возникшими, непременно познаются умственным сознанием",
             "aniccameva": "непременно являются непостоянными", "jarābhibhūtameva": "непременно подвластны старению"}
SURE = "непременно"                                       # emphatic eva (termbase)

# ten powers
POWERS = [   # (accusative after «понимает», prepositional after «знание Татхагаты»)
    ("возможное как возможное и невозможное как невозможное",
     "о возможном как возможном и о невозможном как невозможном"),
    ("результат прошлых, будущих и настоящих совершаемых действий по условиям и по причинам",
     "о результате прошлых, будущих и настоящих совершаемых действий по условиям и по причинам"),
    ("способ практики, ведущий повсюду", "о способе практики, ведущем повсюду"),
    ("мир многих элементов и разных элементов", "о мире многих элементов и разных элементов"),
    ("разные устремления существ", "о разных устремлениях существ"),
    ("высокую и низкую степень развития способностей других существ, других личностей",
     "о высокой и низкой степени развития способностей других существ, других личностей"),
    ("омрачение, очищение и выход в медитативных погружениях, освобождениях, сосредоточениях и медитативных "
     "достижениях",
     "об омрачении, очищении и выходе в медитативных погружениях, освобождениях, сосредоточениях и медитативных "
     "достижениях"),
    ("припоминание прежних жизней", "о припоминании прежних жизней"),
    ("смерть и новое рождение существ", "о смерти и новом рождении существ"),
    ("уничтожение влечений", "об уничтожении влечений"),
]
P7_Q = ("об омрачении и очищении в медитативных погружениях, освобождениях, сосредоточениях и медитативных "
        "достижениях")                                  # ^2-828 question: «saṃkilesaṃ vodānaṃ» (no vuṭṭhānaṃ)
V_LOKAM = "[вариант написания (Syā.): anekadhātuṃ nānādhātuṃ lokaṃ; ma. ni. 1.148]"


def tath_knowledge(prep):
    return f"знание {TATH[:-1]}ы {prep}, {YATHA}"


def power_q(n, prep):
    return f"({n}) Что такое здесь {tath_knowledge(prep)}?"


def power_end(prep):
    return f"{cap(YA_TATTHA)}, – это {tath_knowledge(prep)}."


IMP = "Невозможно и исключено, чтобы {x}, такой возможности нет"     # aṭṭhānametaṃ anavakāso yaṃ …, netaṃ ṭhānaṃ vijjati
POS = "Но возможно, чтобы {x}, такая возможность есть"               # ṭhānañca kho etaṃ vijjati yaṃ …, ṭhānametaṃ vijjati
DS = "человек, обладающий совершенным воззрением,"                  # diṭṭhisampanno puggalo
PJ = "обычный человек"                                             # puthujjano


def knows(x, first=False):
    return f"{'Здесь Татхагата понимает' if first else 'Понимает'}: «{x}»."


CONDUCT = {"kāya": "телесное", "vacī": "речевое", "mano": "умственное"}
CONDUCT_INS = {"kāya": "телесным", "vacī": "речевым", "mano": "умственным"}
GOOD_RES = "желанный, милый, приятный результат"                   # iṭṭho kanto manāpo vipāko
BAD_RES = "нежеланный, немилый, неприятный результат"
HAPPY = "в счастливом уделе, в небесном мире"                     # sugatiṃ saggaṃ lokaṃ
WOE = "в мире лишений, в дурном уделе, в мире падения, в аду"       # apāyaṃ duggatiṃ vinipātaṃ nirayaṃ
AFTER_DEATH = "по этой причине, по этому условию после распада тела, после смерти появился"   # tannidānaṃ tappaccayā …


def conduct(kind, good):
    return f"{'хорошее' if good else 'дурное'} {CONDUCT[kind]} поведение"


def owner(kind, good):
    return f"обладающий {'хорошим' if good else 'дурным'} {CONDUCT_INS[kind]} поведением"


# beings (power 5 and 6)
LOW_DISP = "существа с низшими устремлениями"
HIGH_DISP = "существа с высшими устремлениями"
LOW_DISP_I = "с существами с низшими устремлениями"
HIGH_DISP_I = "с существами с высшими устремлениями"
ASSOC = {"now": "общаются, водят дружбу и сближаются", "past": "общались, водили дружбу и сближались",
         "fut": "будут общаться, водить дружбу и сближаться"}


def disp_lines(quoted):
    o = "«" if quoted else ""
    l1 = (f"{o}Есть {LOW_DISP}, есть {HIGH_DISP}. {cap(LOW_DISP)} {ASSOC['now']} {LOW_DISP_I}. {cap(HIGH_DISP)} "
          f"{ASSOC['now']} {HIGH_DISP_I}.")
    sep2 = ", " if quoted else ". "
    l2 = (f"{o}И в прошлом времени {LOW_DISP} {ASSOC['past']} {LOW_DISP_I}{sep2}"
          f"{HIGH_DISP if quoted else cap(HIGH_DISP)} {ASSOC['past']} {HIGH_DISP_I}.")
    l3 = (f"{o}И в будущем времени {LOW_DISP} {ASSOC['fut']} {LOW_DISP_I}{sep2}"
          f"{HIGH_DISP if quoted else cap(HIGH_DISP)} {ASSOC['fut']} {HIGH_DISP_I}")
    return l1, l2, l3


TEN_VIEWS = ("«Мир вечен», или «мир не вечен», или «мир конечен», или «мир бесконечен», или «душа то же самое, что и "
             "плоть», или «душа одно, а плоть другое», или «Татхагата существует после смерти», или «Татхагата не "
             "существует после смерти», или «Татхагата и существует, и не существует после смерти», или «Татхагата не "
             "существует и не не существует после смерти»")          # pi-1 ^1-1105
RIGHT_VIEW = ("«Подаяние имеет значение, жертвоприношение имеет значение, подношение имеет значение, у хорошо и дурно "
              "совершённых поступков есть плод, есть результат, этот мир имеет значение, иной мир имеет значение, мать "
              "имеет значение, отец имеет значение, есть рождающиеся самопроизвольно существа, есть в мире отшельники и "
              "брахманы, идущие верным путём, правильно практикующие, которые, сами постигнув высшим знанием и "
              "осуществив этот мир и иной мир, возвещают о них»")   # atthi dinnaṃ … (pi-1 ^1-1221 wording, positive)
ACCEPT = ("такое согласующееся принятие, воззрение, предпочтение, одобрение, рассмотрение, принятие через обдумывание "
          "явлений")                                    # evarūpiṃ anulomikaṃ khantiṃ diṭṭhiṃ ruciṃ mudiṃ pekkhaṃ …
IMPERM = "«Материальная форма непостоянна», или чувство… восприятие… формирующие факторы… «Сознание непостоянно»"
YOGA = ("в видах работы, требующих умения, или в ремёслах, требующих умения, или в областях науки, требующих "
        "умения")                                       # yogavihitesu vā kammāyatanesu … vijjāṭṭhānesu

# dependent origination (ch. 6 links)
DO_LINK = {   # Xpaccayā Y -> Russian; asati X natthi Y -> Russian
    "jāti": ("рождением обусловлены старение и смерть", "когда нет рождения, нет старения и смерти"),
    "bhava": ("существованием обусловлено рождение", None), "upādāna": ("цеплянием обусловлено существование", None),
    "taṇhā": ("жаждой обусловлено цепляние", None), "vedanā": ("чувством обусловлена жажда", None),
    "phassa": ("контактом обусловлено чувство", None), "saḷāyatana": ("шестью сферами восприятия обусловлен контакт", None),
    "nāmarūpa": ("умственным и материальной формой обусловлены шесть сфер восприятия", None),
    "viññāṇa": ("сознанием обусловлены умственное и материальная форма", None),
    "saṅkhāra": ("формирующими факторами обусловлено сознание", None),
    "avijjā": ("неведением обусловлены формирующие факторы", "когда нет неведения, нет формирующих факторов"),
}
STEADY = ("и это его знание устойчивости явлений подвержено уничтожению, подвержено исчезновению, подвержено угасанию, "
          "подвержено прекращению")                     # yampissa taṃ dhammaṭṭhitiñāṇaṃ tampi khayadhammaṃ …


def that(x):
    return f"знание того, что {x}"


def do_run(k):
    a, b = DO_LINK[k]
    neg = f"знание того, что, {b}"
    return [that(a), neg, that(f"и в прошлом времени {a}"), neg, that(f"и в будущем времени {a}"), neg]


# path, fruit, attainments
PATHS = [("sotāpatti", "вступления в поток"), ("sakadāgāmi", "однократного возвращения"),
         ("anāgāmi", "невозвращения"), ("arahatta", "состояния архата")]
ATTAIN9 = [K10.UPA_GEN[k] for k in ("paṭhamassa jhānassa", "dutiyassa jhānassa", "tatiyassa jhānassa",
                                    "catutthassa jhānassa", "ākāsānañcāyatanassa", "viññāṇañcāyatanassa",
                                    "ākiñcaññāyatanassa", "nevasaññānāsaññāyatanassa")]
CESSATION = "прекращения восприятия и ощущаемого"         # saññāvedayitanirodha (gen.)

# decline … penetration (^2-799)
LABHI = {"Paṭhamassa jhānassa": "первое медитативное погружение", "Dutiyassa jhānassa": "второе медитативное погружение",
         "Tatiyassa jhānassa": "третье медитативное погружение", "Catutthassa jhānassa": "четвёртое медитативное погружение",
         "Ākāsānañcāyatanassa": K10.ATTAIN["ākāsānañcāyatanaṃ"], "Viññāṇañcāyatanassa": K10.ATTAIN["viññāṇañcāyatanaṃ"],
         "Ākiñcaññāyatanassa": K10.ATTAIN["ākiñcaññāyatanaṃ"]}
SAHA = {"kāma": "чувственными желаниями", "avitakka": "отсутствием направленной мысли", "nibbidā": "разочарованием",
        "vitakka": "направленной мыслью", "upekkhā": "невозмутимостью", "pītisukha": "восторгом и счастьем",
        "adukkhamasukha": "тем, что ни болезненно, ни приятно", "rūpa": "материальной формой",
        "ākāsānañcāyatana": "сферой бесконечного пространства", "viññāṇañcāyatana": "сферой бесконечного сознания",
        "ākiñcaññāyatana": "сферой отсутствия чего-либо",
        "nevasaññānāsaññāyatana": "сферой ни восприятия, ни невосприятия"}
PM = "восприятия и внимание"                                # saññāmanasikārā
STAND = f"Когда устойчива осознанность, соответствующая этому, это {PH['ṭhitibhāgī'][0]}."  # tadanudhammatā sati …


def assail(x, who=None):
    w = f"у того, кто обрёл {LABHI[who]}, " if who else ""
    return f"Когда {w}проявляются {PM}, сопровождаемые {SAHA[x]},"


def decline_sent(s):
    s = s.rstrip(".")
    if s == "Tadanudhammatā sati santiṭṭhati ṭhitibhāginī paññā" or s == "tadanudhammatā sati santiṭṭhati ṭhitibhāginī paññā":
        return STAND
    m = re.match(r"^(?:(\S+ssa(?: jhānassa)?) lābhiṃ )?(\S+?)sahagatā saññāmanasikārā samudācaranti "
                 r"(virāgūpasañhitā )?(\S+)bhāginī paññā$", s[0].upper() + s[1:] if not s.startswith(("tad",)) else s)
    assert m, s
    who, x, vir, kind = m.groups()
    x = x[0].lower() + x[1:]
    end = PH[f"{kind}bhāgī"][0]
    if vir:
        end = end.replace("мудрость, ", "мудрость, связанная с бесстрастием и ")
    return f"{assail(x, who)} это {end}."


# =========================================================================== segment builders
SID = {"sid": None}


def eka_matrix(lines):
    head = lines[0]
    m = re.match(r"^Ekavidhena ñāṇavatthu – pañca viññāṇā (.*),$", head)
    keys = [pl2key(w) for w in m.group(1).split(", ")]
    out = [f"{vidha_head(1)} {FIVE_V} " + "; ".join(vp(k) for k in keys) + ";"]
    assert lines[1] == "Uppannavatthukā uppannārammaṇā,", lines[1]
    out.append(EKA["Uppannavatthukā uppannārammaṇā"] + ";")
    for ln in lines[2:-1]:
        mm = re.match(r"^\((\d+)\) (.*)$", ln)
        n, body = mm.groups()
        if n == "14":
            assert body == ("Pañcahi viññāṇehi na kañci [kiñci (sī. ka.)] dhammaṃ paṭivijānāti aññatra "
                            "abhinipātamattā"), body
            out.append(f"({n}) {EKA['Pañcahi viññāṇehi na kañci dhammaṃ paṭivijānāti']} {V_KINCI}, "
                       f"{EKA_GLOSS['Aññatra abhinipātamattā'][0].lower()}")
            continue
        tail = ""
        if n == "27":
            body, t = body.split(", ")
            assert t == "yāthāvakavatthuvibhāvanā paññā", t
            tail = f"; {REAL}"
        out.append(f"({n}) {EKA[body]}{tail}")
    assert lines[-1] == "Evaṃ ekavidhena ñāṇavatthu."
    out.append(vidha_end(1))
    return out, keys


def eka_meva(lines, keys):
    ln = lines[0]
    assert ln.startswith("Pañca viññāṇā ") and ln.endswith("."), ln
    words = ln[len("Pañca viññāṇā "):-1].split(", ")
    mk = [meva2key(w) for w in words if w not in MEVA_TAIL]
    assert mk == keys, (mk, keys)
    parts = [f"{SURE} {vp(k)}" for k in mk] + [MEVA_TAIL[w] for w in words if w in MEVA_TAIL]
    return [f"{cap(FIVE_V)} " + "; ".join(parts) + "."]


def eka_gloss_line(ln):
    """the quoted part ends in «…ti» («anābhogāti») or «…īti» («uppajjantīti», «paṭivijānātīti»)"""
    for q in sorted(EKA_GLOSS, key=len, reverse=True):
        forms = [q + "ti "]
        if q.endswith("i"):
            forms.append(q[:-1] + "īti ")
        if any(ln.startswith(f) for f in forms):
            return EKA_GLOSS[q]
    raise KeyError(ln)


def eka_gloss(ln):
    q, expl = eka_gloss_line(ln)
    return gloss(q, expl)


def pairs_line(ln, kind):
    """^2-763 / ^2-765: «Na aññamaññassa …ti» + the cross pairs"""
    if kind == "gocara":
        q = EKA["Na aññamaññassa gocaravisayaṃ paccanubhonti"]
        one = "Сферы действия {a} {b} не испытывает, и сферы действия {c} {d} не испытывает."
    else:
        q = EKA["Na aññamaññassa samanantarā uppajjanti"]
        one = "Сразу после возникновения {a} {b} не возникает, и сразу после возникновения {c} {d} не возникает."
    sents = []
    for x, y in (("cakkhu", "sota"), ("cakkhu", "ghāna"), ("cakkhu", "jivhā"), ("cakkhu", "kāya")):
        sents.append(one.format(a=VIN_GEN[x], b=VIN_NOM[y], c=VIN_GEN[y], d=VIN_NOM[x]))
    pe = one.format(a=f"{VIN_GEN['sota']}… {VIN_GEN['ghāna']}… {VIN_GEN['jivhā']}… {VIN_GEN['kāya']}",
                    b=VIN_NOM["cakkhu"], c=VIN_GEN["cakkhu"], d=VIN_NOM["kāya"])
    sents.append(pe)
    for x, y in (("kāya", "sota"), ("kāya", "ghāna"), ("kāya", "jivhā")):
        sents.append(one.format(a=VIN_GEN[x], b=VIN_NOM[y], c=VIN_GEN[y], d=VIN_NOM[x]))
    first = sents[0]
    sents[0] = low(first)
    return f"«{q}»: " + " ".join(sents)


def matrix_line(ln):
    """(n) A paññā, B paññā[, C paññā] / Atthi … lines of the twofold and threefold matrices"""
    m = re.match(r"^\((\d+)\) (.*)$", ln)
    n, body = m.groups()
    return f"({n}) {matrix_body(body)}"


def matrix_body(body):
    if " atthi " in body or body.startswith("Atthi "):
        return atthi_body(body)
    names = body.split(", ")
    return cap(join_items([ph(pkey_full(x))[0] for x in names]))


ATTHI_SLIP = {"anuppādinnupādāniyā": ("anupādinnupādāniyā", "^2-753 (40) «anuppādinnupādāniyā, anuppādinnaanupādāniyā» "
                                                            "(-pp- for anupādinna-): rendered as meant"),
              "anuppādinnaanupādāniyā": ("anupādinnaanupādāniyā", None),
              "ajjhatā": ("ajjhattā", "^2-753 (62) «atthi ajjhatā» (for ajjhattā): rendered as meant «внутренней»")}
PLURAL_SUBJ = {"Pītisahagatā paññā sukhasahagatā paññā"}


def atthi_body(body):
    subj = ""
    rest = body
    mm = re.match(r"^(.+?) (atthi .*)$", body)
    if mm and not body.startswith("Atthi "):
        subj, rest = mm.groups()
    rest = rest[0].lower() + rest[1:]
    items = []
    for a in rest.split(", "):
        assert a.startswith("atthi "), a
        w = a[len("atthi "):]
        if w in ATTHI_SLIP:
            w2, note = ATTHI_SLIP[w]
            if note:
                slip(note)
            w = w2
        items.append(w)
    pl = subj in PLURAL_SUBJ
    if pl:
        ATTHI_STATE["pl"] = True
    elif subj:
        ATTHI_STATE["pl"] = False
    pl = ATTHI_STATE["pl"]
    preds = ", ".join(byv(pk(w), pl) for w in items)
    if not subj:
        return cap(preds)
    if subj in PLURAL_SUBJ:
        a, b = subj[:-len(" paññā")].split(" paññā ")
        s = f"{ph(pk(a))[0]}, и {ph(pk(b))[0]},"
    else:
        nom = ph(pk(subj[:-len(' paññā')]))[0]
        s = nom + ("," if ", " in nom else "")
    return f"{cap(s)} {preds}"


ATTHI_STATE = {"pl": False}


def duka_matrix(lines):
    out = [vidha_head(2)]
    assert lines[0] == "Duvidhena ñāṇavatthu –"
    for ln in lines[1:-1]:
        out.append(matrix_line(ln))
    out.append(vidha_end(2))
    return out


def tika_matrix(lines):
    assert lines[0] == "Tividhena ñāṇavatthu –"
    out = [vidha_head(3)]
    for ln in lines[1:-1]:
        m = re.match(r"^\((\d+)\) (.*)$", ln)
        n, body = m.groups()
        if n == "4":
            assert body == "Āyakosallaṃ, apāyakosallaṃ, upāyakosallaṃ"
            out.append(f"({n}) " + cap(", ".join(NAMES[x][0] for x in ("āyakosallaṃ", "apāyakosallaṃ",
                                                                       "upāyakosallaṃ"))))
            continue
        if n == "3":
            out.append(f"({n}) " + cap(join_items([PH[x][0] for x in ("adhisīle", "adhicitte", "adhipaññāya")])))
            continue
        out.append(f"({n}) {matrix_body(body)}")
    out.append(vidha_end(3))
    return out


V_PARICCE = "[вариант чтения (во всех изданиях): paricce; см. в Дигха-никае]"
V_SAMMATI = "[вариант написания (Syā.): sammatiñāṇaṃ; см. в Дигха-никае]"


def four(keys):
    return [know(k)[0] for k in keys]


def four_ins(keys):
    return [know(k)[1] for k in keys]


def truths(x):
    return [x, f"{x}samudaya", f"{x}nirodha", f"{x}nirodhagāminiyā paṭipadāya"]


DO_PE = ["jāti", "bhava", "upādāna", "taṇhā", "vedanā", "phassa", "saḷāyatana", "nāmarūpa", "viññāṇa"]


def catukka_matrix(lines):
    assert lines[0] == "Catubbidhena ñāṇavatthu –"
    out = [vidha_head(4)]
    exp = {
        "1": "Kammassakatañāṇaṃ, saccānulomikaṃ ñāṇaṃ, maggasamaṅgissa ñāṇaṃ, phalasamaṅgissa ñāṇaṃ",
        "2": "Dukkhe ñāṇaṃ, dukkhasamudaye ñāṇaṃ, dukkhanirodhe ñāṇaṃ, dukkhanirodhagāminiyā paṭipadāya ñāṇaṃ",
        "3": "Kāmāvacarā paññā, rūpāvacarā paññā, arūpāvacarā paññā, apariyāpannā paññā",
        "5": ("Atthi paññā ācayāya no apacayāya, atthi paññā apacayāya no ācayāya, atthi paññā ācayāya ceva apacayāya "
              "ca, atthi paññā nevācayāya no apacayāya"),
        "6": ("Atthi paññā nibbidāya no paṭivedhāya, atthi paññā paṭivedhāya no nibbidāya, atthi paññā nibbidāya ceva "
              "paṭivedhāya ca, atthi paññā neva nibbidāya no paṭivedhāya"),
        "7": "Hānabhāginī paññā, ṭhitibhāginī paññā, visesabhāginī paññā, nibbedhabhāginī paññā",
        "11": ("Jarāmaraṇe ñāṇaṃ, jarāmaraṇasamudaye ñāṇaṃ, jarāmaraṇanirodhe ñāṇaṃ, jarāmaraṇanirodhagāminiyā "
               "paṭipadāya ñāṇaṃ"),
    }
    for ln in lines[1:]:
        m = re.match(r"^\(([\d-]+)\) (.*)$", ln)
        n, body = m.groups()
        if n in exp:
            assert body == exp[n], (n, body)
        if n == "1":
            r = join_items([NAMES[k][0] for k in ("kammassakatañāṇaṃ", "saccānulomikaṃ ñāṇaṃ", "maggasamaṅgissa ñāṇaṃ",
                                                  "phalasamaṅgissa ñāṇaṃ")])
        elif n == "2":
            r = join_items(four(truths("dukkha")))
        elif n == "3":
            r = join_items([ph(pk(x))[0] for x in ("kāmāvacarā", "rūpāvacarā", "arūpāvacarā", "apariyāpannā")])
        elif n == "4":
            assert body == ("Dhamme ñāṇaṃ, anvaye ñāṇaṃ, pariye [paricce (sabbattha) passa dīghanikāye] ñāṇaṃ, "
                            "sammutiñāṇaṃ [sammatiñāṇaṃ (syā.) passa dīghanikāye]"), body
            r = (f"{NAMES['dhamme ñāṇaṃ'][0]}, {NAMES['anvaye ñāṇaṃ'][0]}, {NAMES['pariye ñāṇaṃ'][0]} {V_PARICCE}, "
                 f"{NAMES['sammutiñāṇaṃ'][0]} {V_SAMMATI}")
        elif n == "5":
            r = "; ".join(f"есть {NAMES[k][0]}" for k in ("paññā ācayāya no apacayāya", "paññā apacayāya no ācayāya",
                                                          "paññā ācayāya ceva apacayāya ca",
                                                          "paññā nevācayāya no apacayāya"))
        elif n == "6":
            r = "; ".join(f"есть {NAMES[k][0]}" for k in ("paññā nibbidāya no paṭivedhāya",
                                                          "paññā paṭivedhāya no nibbidāya",
                                                          "paññā nibbidāya ceva paṭivedhāya ca",
                                                          "paññā neva nibbidāya no paṭivedhāya"))
        elif n == "7":
            r = join_items([PH[k][0] for k in ("hānabhāgī", "ṭhitibhāgī", "visesabhāgī", "nibbedhabhāgī")])
        elif n in ("8", "9", "10"):
            r = NAMES[body[0].lower() + body[1:]][0]
        elif n == "11":
            r = join_items(four(truths("jarāmaraṇa")))
        else:
            assert n == "12-21", n
            p_pe = "…pe… ".join(f"{x} ñāṇaṃ" for x in ("Jātiyā", "bhave", "upādāne", "taṇhāya", "vedanāya", "phasse",
                                                        "saḷāyatane", "nāmarūpe", "viññāṇe"))
            assert body == (f"{p_pe}…pe… saṅkhāresu ñāṇaṃ, saṅkhārasamudaye ñāṇaṃ, saṅkhāranirodhe ñāṇaṃ, "
                            "saṅkhāranirodhagāminiyā paṭipadāya ñāṇaṃ. Evaṃ catubbidhena ñāṇavatthu."), body
            r = ("… ".join(know(x)[0] for x in DO_PE) + "… " + ", ".join(four(truths("saṅkhāra"))) + ". "
                 + vidha_end(4))
            out.append(f"({n}) {cap(r)}")
            continue
        out.append(f"({n}) {cap(r)}")
    return out


def small_matrix(lines, n, item_ru):
    return [vidha_head(n), item_ru, vidha_end(n)]


def dasa_matrix(lines):
    assert lines[0] == ("Dasavidhena ñāṇavatthu – dasa tathāgatassa tathāgatabalāni yehi balehi samannāgato "
                        "tathāgato āsabhaṃ ṭhānaṃ paṭijānāti, parisāsu sīhanādaṃ nadati, brahmacakkaṃ pavatteti. "
                        "Katamāni dasa?"), lines[0]
    out = [f"{vidha_head(10)} {POWERS10}, наделённый которыми {TATH} {FEATS}. Какие десять?"]
    for i, ln in enumerate(lines[1:11]):
        n = i + 1
        assert ln.startswith(f"({n}) "), ln
        acc = POWERS[i][0]
        acc1 = f"{acc} {V_LOKAM}" if n == 4 else acc
        intro = "Здесь" if n == 1 else "Кроме того,"
        r = (f"({n}) {intro} {TATH} понимает, {YATHA}, {acc1}. И то, что {TATH} понимает, {YATHA}, {acc}, тоже "
             f"является {POWER_OF}, опираясь на которую {TATH} {FEATS}.")
        if n == 10:
            assert ln.endswith("Imāni dasa tathāgatassa tathāgatabalāni, yehi balehi samannāgato tathāgato āsabhaṃ "
                               "ṭhānaṃ paṭijānāti, parisāsu sīhanādaṃ nadati, brahmacakkaṃ pavatteti."), ln
            r += f" Это {POWERS10}, наделённый которыми {TATH} {FEATS}."
        out.append(r)
    assert lines[11] == "Evaṃ dasavidhena ñāṇavatthu."
    out.append(vidha_end(10))
    return out


# ---- twofold exposition (^2-767)
def duka_nid(lines):
    out = []
    for ln in lines:
        m = re.match(r"^\((\d+)\) (.*)$", ln)
        if not m:
            if ln == "Tattha katamā atthajāpikā paññā?":
                out.append(f"Что такое здесь {PH['atthajāpiko'][0]}?")
            elif ln.startswith("Catūsu bhūmīsu kusale arahato abhiññaṃ"):
                assert ln == ("Catūsu bhūmīsu kusale arahato abhiññaṃ uppādentassa samāpattiṃ uppādentassa "
                              "kiriyābyākate paññā atthajāpikā paññā, catūsu bhūmīsu vipāke arahato uppannāya "
                              "abhiññāya uppannāya samāpattiyā kiriyābyākate paññā jāpitatthā paññā."), ln
                out.append(f"Мудрость {LOC_KIND['kusale']} на четырёх уровнях и {LOC_KIND['kiriyābyākate']} у "
                           "архата, порождающего высшее знание, порождающего медитативное достижение, является "
                           f"{PH['atthajāpiko'][1]}; мудрость {LOC_KIND['vipāke']} на четырёх уровнях и "
                           f"{LOC_KIND['kiriyābyākate']} у архата, у которого возникло высшее знание, возникло "
                           f"медитативное достижение, является {PH['jāpitattho'][1]}.")
            elif ln == "Evaṃ duvidhena ñāṇavatthu.":
                out.append(vidha_end(2))
            elif ln == "Dukaṃ.":
                out.append(close_label(2))
            else:
                raise KeyError(ln)
            continue
        n, body = m.groups()
        if body == "Tattha katamā atthajāpikā paññā?":
            out.append(f"({n}) Что такое здесь {PH['atthajāpiko'][0]}?")
            continue
        assert body.endswith("."), body
        b = body[:-1]
        if n == "2":
            assert b == "Sabbāva paññā kenaci viññeyyā, kenaci na viññeyyā"
            out.append(f"({n}) Всякая мудрость {K1.ITEMS['kenaci viññeyyo']['v']}, "
                       f"{K1.ITEMS['kenaci na viññeyyo']['v']}.")
            continue
        if n in ("28", "29", "30"):
            sph = {"28": "kāmāvacara", "29": "rūpāvacara", "30": "arūpāvacara"}[n]
            first, rest = b.split(", ", 1)
            mm = SENT_RX.match(first)
            r1 = is_clause(mm.group(1), pkey_full(mm.group(2)))
            mm2 = re.match(r"^(.+) na (\S+) paññā$", rest.replace(", ", " "))
            subs = [x for x in mm2.group(1).split(" paññā") if x.strip()]
            subs = [x.strip() for x in subs]
            subs_ru = [ph(pk(x))[0] for x in subs]
            assert mm2.group(2) == sph[:-1] + "ā", rest
            r2 = f"{nlist(subs_ru)}, являются {ph('na ' + sph[:-1] + 'o')[1]}"
            out.append(f"({n}) {cap(r1)}; {r2}.")
            continue
        out.append(f"({n}) {cap(is_sentence(b))}.")
    return out


# ---- generic exposition lines (threefold and fourfold sections)
Q_RX = re.compile(r"^(?:\(([^)]+)\) )?[Tt]attha katam(?:ā|aṃ|o|āni) (.+?)\?(?: (.*))?$")


V_UPARI = "[вариант написания (Syā.): upariṭṭhime, (Ka.): upariṭṭhimaṃ]"


def body_sentence(b):
    """one exposition body after the question / label"""
    if " [upariṭṭhime (syā.), upariṭṭhimaṃ (ka.)]" in b:
        slip("^2-777 «upariṭṭhimā arahattaphale» (nominative plural beside a locative; Syā. upariṭṭhime): rendered "
             "as meant «в высшем плоде состояния архата»")
        r = body_sentence(b.replace(" [upariṭṭhime (syā.), upariṭṭhimaṃ (ka.)]", ""))
        return r.replace("в высшем", f"в высшем {V_UPARI}", 1)
    if ARISE_RX.match(b):
        return arise_sentence(b)
    m = re.match(r'^(.+?) paññā – ayaṃ vuccati "(.+?)"\.$', b)
    if m:
        return f"Мудрость {loc(m.group(1))[0]} – {called(name(m.group(2))[1])}."
    m = re.match(r"^(.+?) paññā (.+?)\.$", b)
    if m and m.group(2) in NAMES and not b.startswith("sabbāpi "):
        t, comma = loc(m.group(1))
        return f"Мудрость {t}{',' if comma else ''} является {NAMES[m.group(2)][1]}."
    if b in TAIL:
        return TAIL[b]
    if b.startswith("sabbāpi samāpannassa paññā "):
        k = pkey_full(b[len("sabbāpi samāpannassa paññā "):-1])
        return f"Всякая мудрость того, кто вошёл в медитативное достижение, является {ph(k)[1]}."
    if b == "sabbāpi tatrupāyā paññā upāyakosallaṃ.":
        return f"Всякая мудрость, касающаяся средств в этом, является {NAMES['upāyakosallaṃ'][1]}."
    mm = re.match(r"^(.+?) paññā (.+?) paññā\.$", b[0].lower() + b[1:])
    if mm:
        return cap(is_clause(mm.group(1), pkey_full(mm.group(2)))) + "."
    raise KeyError(b)


def gen_line(ln):
    if ln in SIYA:
        return SIYA[ln]
    m = Q_RX.match(ln)
    if m:
        label, nm, rest = m.groups()
        q = f"Что такое здесь {name(nm)[0]}?"
        r = (f"{lab(label)} {q}" if label else q)
        return r + (f" {body_sentence(rest)}" if rest else "")
    m = re.match(r"^\(([^)]+)\) (.*)$", ln)
    if m:
        return f"{lab(m.group(1))} {body_sentence(m.group(2))}"
    return body_sentence(ln)


def tika_nid_special(sid, lines):
    if sid == "2-768":
        assert len(lines) == 4
        out = [gen_line(lines[0])]
        exp = ('Yogavihitesu vā kammāyatanesu yogavihitesu vā sippāyatanesu yogavihitesu vā vijjāṭṭhānesu kammassakataṃ '
               'vā saccānulomikaṃ vā rūpaṃ aniccanti vā vedanā…pe… saññā… saṅkhārā… viññāṇaṃ aniccanti vā, yaṃ '
               'evarūpiṃ anulomikaṃ khantiṃ diṭṭhiṃ ruciṃ mudiṃ pekkhaṃ dhammanijjhānakkhantiṃ parato {h} '
               'paṭilabhati – ayaṃ vuccati "{n}".')
        assert lines[1] == exp.format(h="assutvā", n="cintāmayā paññā"), lines[1]
        topics = f"касающееся {NAMES['kammassakatañāṇaṃ'][0][len('знание '):]}, или согласующееся с истинами, или такое, как {IMPERM}"
        out.append(f"Когда {YOGA}, человек, не услышав от другого, обретает {ACCEPT}, {topics}, – "
                   f"{called(PH['cintāmayo'][1])}.")
        q, rest = lines[2].split("? ", 1)
        assert rest == exp.format(h="sutvā", n="sutamayā paññā"), rest
        out.append(f"{gen_line(q + '?')} Когда {YOGA}, человек, услышав от другого, обретает {ACCEPT}, {topics}, – "
                   f"{called(PH['sutamayo'][1])}.")
        out.append(gen_line(lines[3]))
        return out
    if sid == "2-771":
        out = []
        for ln in lines[:2]:
            m = re.match(r'^\((.+?)\) tattha katamaṃ (\S+)\? "(.*)"ti – yā tattha paññā pajānanā…pe… amoho '
                         r'dhammavicayo sammādiṭṭhi – idaṃ vuccati "(\S+)"\.$', ln)
            label, nm, quote, nm2 = m.groups()
            assert nm == nm2
            out.append(f"{lab(label)} Что такое здесь {NAMES[nm][0]}? «{GAIN_LOSS[quote]}» – {YA_TATTHA}, – "
                       f"{called(NAMES[nm][1])}.")
        out.append(gen_line(lines[2]))
        return out
    raise KeyError(sid)


WHO_ATTENDS = "У того, кто уделяет внимание этим явлениям,"   # ime dhamme manasikaroto
OR_WHO = "Или же у того, кто уделяет внимание этим явлениям,"  # ime vā panime dhamme manasikaroto
GROW4 = "к умножению, обширности, развитию и завершённости"   # bhiyyobhāvāya vepullāya bhāvanāya pāripūriyā (ch. 8)
GROW2 = "к умножению и обширности"
GAIN_LOSS = {
    ("Ime dhamme manasikaroto anuppannā ceva akusalā dhammā na uppajjanti, uppannā ca akusalā dhammā pahīyanti. Ime "
     "vā panime dhamme manasikaroto anuppannā ceva kusalā dhammā uppajjanti, uppannā ca kusalā dhammā bhiyyobhāvāya "
     "vepullāya bhāvanāya pāripūriyā saṃvattantī"):
        (f"{WHO_ATTENDS} и невозникшие неблагие явления не возникают, и возникшие неблагие явления устраняются. "
         f"{OR_WHO} и невозникшие благие явления возникают, и возникшие благие явления ведут {GROW4}"),
    ("Ime dhamme manasikaroto anuppannā ceva kusalā dhammā na uppajjanti, uppannā ca kusalā dhammā nirujjhanti. Ime "
     "vā panime dhamme manasikaroto anuppannā ceva akusalā dhammā uppajjanti, uppannā ca akusalā dhammā "
     "bhiyyobhāvāya vepullāya saṃvattantī"):
        (f"{WHO_ATTENDS} и невозникшие благие явления не возникают, и возникшие благие явления прекращаются. "
         f"{OR_WHO} и невозникшие неблагие явления возникают, и возникшие неблагие явления ведут {GROW2}"),
}

TAIL.update({
    "Imā catasso paṭipadā.": "Это четыре способа практики.",
    "Imāni cattāri ārammaṇāni.": "Это четыре объекта.",
    "Evaṃ tividhena ñāṇavatthu.": vidha_end(3), "Tikaṃ.": close_label(3),
    "Evaṃ catubbidhena ñāṇavatthu.": vidha_end(4), "Catukkaṃ.": close_label(4),
})


def is_also(subject_ru, keys):
    """X ñāṇaṃ Ype etaṃ ñāṇaṃ, … = X является и знанием Y, и знанием …"""
    return f"{subject_ru} является " + ", ".join(f"и {k}" for k in keys)


def catukka_nid(sid, lines):
    if sid == "2-793":
        a = lines[0]
        assert a.startswith('(1. Ka) tattha katamaṃ kammassakatañāṇaṃ? "Atthi dinnaṃ, atthi yiṭṭhaṃ') and a.endswith(
            'pavedentī"ti – yā evarūpā paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi – idaṃ vuccati '
            '"kammassakatañāṇaṃ". Ṭhapetvā saccānulomikaṃ ñāṇaṃ, sabbāpi sāsavā kusalā paññā kammassakatañāṇaṃ.'), a
        n = NAMES["kammassakatañāṇaṃ"]
        l1 = (f"{lab('1. Ka')} Что такое здесь {n[0]}? {RIGHT_VIEW} – {YA_EVARUPA}, – {called(n[1])}. Кроме "
              f"{KNOW_SACCA_GEN}, всякая благая мудрость, подверженная влечениям, является {n[1]}.")
        b = lines[1]
        assert b == ('(Kha) tattha katamaṃ saccānulomikaṃ ñāṇaṃ? "Rūpaṃ anicca"nti vā vedanā…pe… saññā… saṅkhārā… '
                     '"viññāṇaṃ anicca"nti vā yā evarūpī anulomikā khanti diṭṭhi ruci mudi pekkhā '
                     'dhammanijjhānakkhanti – idaṃ vuccati "saccānulomikaṃ ñāṇaṃ".'), b
        s = NAMES["saccānulomikaṃ ñāṇaṃ"]
        l2 = f"{lab('Kha')} Что такое здесь {s[0]}? {cap(ACCEPT)}, как {IMPERM}, – {called(s[1])}."
        l3 = f"{lab('Ga')} Мудрость в четырёх путях является {NAMES['maggasamaṅgissa ñāṇaṃ'][1]}."
        l4 = f"{lab('Gha')} Мудрость в четырёх плодах является {NAMES['phalasamaṅgissa ñāṇaṃ'][1]}."
        assert lines[2:] == ["(Ga) catūsu maggesu paññā maggasamaṅgissa ñāṇaṃ.",
                             "(Gha) catūsu phalesu paññā phalasamaṅgissa ñāṇaṃ."], lines[2:]
        return [l1, l2, l3, l4]
    if sid in ("2-794", "2-802", "2-803"):
        out = []
        for ln in lines:
            if ln.startswith("(10) Tattha katamāni cattāri ārammaṇāni?"):
                assert ln == ("(10) Tattha katamāni cattāri ārammaṇāni? Parittā parittārammaṇā paññā, parittā "
                              "appamāṇārammaṇā paññā, appamāṇā parittārammaṇā paññā, appamāṇā appamāṇārammaṇā "
                              "paññā."), ln
                lst = ", ".join(PH[f"{a} {b}"][0] for a in ("paritto", "appamāṇo")
                                for b in ("parittārammaṇo", "appamāṇārammaṇo"))
                out.append(f"(10) Что такое здесь {NAMES['cattāri ārammaṇāni'][0]}? {cap(lst)}.")
                continue
            m = re.match(r"^\(([\d-]+)\) (Magga|Dhamma)samaṅgissa ñāṇaṃ (.*)\.$", ln)
            if m:
                n, who, rest = m.groups()
                if who == "Dhamma":
                    slip("^2-803 «Dhammasamaṅgissa ñāṇaṃ jātiyāpetaṃ ñāṇaṃ…» (^2-794 and ^2-802 have Maggasamaṅgissa): "
                         "translated as written «знание обладающего явлением»")
                subj = "Знание обладающего путём" if who == "Magga" else "Знание обладающего явлением"
                if n == "12-21":
                    pe = [f"и {know(x)[1]}" for x in DO_PE]
                    tail = ", ".join(f"и {x}" for x in four_ins(truths("saṅkhāra")))
                    out.append(f"({n}) {subj} является " + "… ".join(pe) + "… " + tail + ".")
                else:
                    x = "dukkha" if "dukkhepetaṃ" in rest else "jarāmaraṇa"
                    out.append(f"({n}) {is_also(subj, four_ins(truths(x)))}.")
                continue
            out.append(gen_line(ln))
        return out
    if sid == "2-795":
        ln = lines[0]
        m = re.match(r"^\(3\) (.*)\.$", ln)
        return [f"(3) {cap(is_sentence(m.group(1)))}."]
    if sid == "2-796":
        out = [gen_line(lines[0])]
        b = lines[1]
        assert b.startswith("(Kha) so iminā dhammena ñātena diṭṭhena pattena viditena pariyogāḷhena atītānāgatena "
                            'nayaṃ neti. "Ye hi keci atītamaddhānaṃ samaṇā vā brāhmaṇā vā dukkhaṃ abbhaññaṃsu '
                            '[abbhaññiṃsu (syā.) evamuparipi], dukkhasamudayaṃ abbhaññaṃsu,'), b
        assert b.endswith('abhijānissantī"ti – yā tattha paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi – idaṃ '
                          'vuccati "anvaye ñāṇaṃ".'), b
        acc = ["страдание", "возникновение страдания", "прекращение страдания",
               "способ практики, ведущий к прекращению страдания"]
        acc_this = ["именно это страдание", "именно это возникновение страдания", "именно это прекращение страдания",
                    "именно этот способ практики, ведущий к прекращению страдания"]
        v_abb = "[вариант написания (Syā.): abbhaññiṃsu; так же и далее]"
        past = (f"Все те отшельники или брахманы, которые в прошлом постигли страдание {v_abb}, "
                + ", ".join(f"постигли {x}" for x in acc[1:]) + ", "
                + ", ".join(f"постигли {x}" for x in acc_this) + ".")
        fut = ("Все те отшельники или брахманы, которые в будущем постигнут "
               + ", ".join(f"постигнут {x}" if i else x for i, x in enumerate(acc)) + ", "
               + ", ".join(f"постигнут {x}" for x in acc_this))
        an = NAMES["anvaye ñāṇaṃ"]
        out.append(f"{lab('Kha')} Посредством этого явления, познанного, увиденного, достигнутого, узнанного, глубоко "
                   f"постигнутого, он делает вывод о прошлом и будущем. «{past} {fut}» – {YA_TATTHA}, – "
                   f"{called(an[1])}.")
        c = lines[2]
        mm = re.match(r'^\(Ga\) tattha katamaṃ pariye ñāṇaṃ\? Idha bhikkhu parasattānaṃ parapuggalānaṃ cetasā ceto '
                      r'paricca pajānāti\. (.*) pajānātīti – yā tattha paññā pajānanā…pe… amoho dhammavicayo '
                      r'sammādiṭṭhi – idaṃ vuccati "pariye ñāṇaṃ"\.$', c)
        units = mm.group(1).split(" pajānāti, ")
        rus = []
        for u in units:
            m1 = re.match(r'^(\S+) vā cittaṃ "(\S+) citta"n(?:ti)?$', u)
            assert m1 and m1.group(1).lower() == m1.group(2), u
            attr, pred = K79.MIND[m1.group(2)]
            rus.append(f"понимает {K79.mind_attr(attr)}: «Ум {pred}»")
        pn = NAMES["pariye ñāṇaṃ"]
        out.append(f"{lab('Ga')} Что такое здесь {pn[0]}? Здесь монах, охватив своим умом ум других существ, других "
                   f"личностей, понимает его. Он " + "; ".join(rus) + f" – {YA_TATTHA}, – {called(pn[1])}.")
        d = lines[3]
        assert d == "(Gha) ṭhapetvā dhamme ñāṇaṃ anvaye ñāṇaṃ pariye ñāṇaṃ, avasesā paññā sammutiñāṇaṃ.", d
        out.append(f"{lab('Gha')} Кроме {KNOW_GEN['dhamme ñāṇaṃ']}, {KNOW_GEN['anvaye ñāṇaṃ']} и "
                   f"{KNOW_GEN['pariye ñāṇaṃ']}, остальная мудрость является {NAMES['sammutiñāṇaṃ'][1]}.")
        return out
    if sid in ("2-797", "2-798"):
        out = []
        for ln in lines:
            m = re.match(r"^\(([^)]+)\) (.*)$", ln)
            label, rest = m.groups()
            mq = re.match(r"^tattha katamā (paññā .+?)\? (.*)$", rest)
            pre = ""
            if mq:
                pre = f"Что такое здесь {NAMES[mq.group(1)][0]}? "
                rest = mq.group(2)
            out.append(f"{lab(label)} {pre}{ACAYA_BODY[rest]}")
        return out
    if sid == "2-799":
        out = []
        for ln in lines:
            m = re.match(r"^\(([^)]+)\) (?:tattha katamā hānabhāginī paññā\? )?(.*)$", ln)
            label, rest = m.groups()
            pre = f"Что такое здесь {PH['hānabhāgī'][0]}? " if "katamā" in ln else ""
            sents = [s.strip() for s in re.split(r"(?<=paññā\.) ", rest)]
            out.append(f"{lab(label)} {pre}" + " ".join(decline_sent(s) for s in sents))
        return out
    if sid == "2-800":
        ln = lines[0]
        assert ln == ("(8) Tattha katamā catasso paṭisambhidā? Atthapaṭisambhidā, dhammapaṭisambhidā, "
                      "niruttipaṭisambhidā, paṭibhānapaṭisambhidā. Atthe ñāṇaṃ atthapaṭisambhidā, dhamme ñāṇaṃ "
                      "dhammapaṭisambhidā, tatra dhammaniruttābhilāpe ñāṇaṃ niruttipaṭisambhidā, ñāṇesu ñāṇaṃ "
                      "paṭibhānapaṭisambhidā. Imā catasso paṭisambhidā."), ln
        ps = K1315.PS
        lst = cap(nlist([ps[k][0] for k in ("attha", "dhamma", "nirutti", "paṭibhāna")]))
        defs = (f"{cap(K1315.know(['attha'])[0])} {K1315.is_ps('attha')}, {K1315.know(['dhamma'])[0]} "
                f"{K1315.is_ps('dhamma')}, {K1315.NIRUTTI_CL}, {K1315.NANESU_CL}.")
        return [f"(8) Что такое здесь {NAMES['catasso paṭisambhidā'][0]}? {lst}. {defs} Это "
                f"{NAMES['catasso paṭisambhidā'][0]}."]
    if sid == "2-801":
        out = []
        ln = lines[0]
        assert ln == ("(9) Tattha katamā catasso paṭipadā? Dukkhapaṭipadā dandhābhiññā paññā, dukkhapaṭipadā "
                      "khippābhiññā paññā, sukhapaṭipadā dandhābhiññā paññā, sukhapaṭipadā khippābhiññā paññā."), ln
        lst = ", ".join(PH[f"{p}paṭipadā {q}ābhiñño"][0] for p in ("dukkha", "sukha") for q in ("dandh", "khipp"))
        out.append(f"(9) Что такое здесь {NAMES['catasso paṭipadā'][0]}? {cap(lst)}.")
        out += [gen_line(x) for x in lines[1:]]
        return out
    raise KeyError(sid)


_I = {k: K1.ITEMS[k]["ins"] for k in ("uppanno", "anuppanno", "uppādī", "atīto", "anāgato", "paccuppanno",
                                      "ajjhatto", "bahiddho", "ajjhattabahiddho")}
_F = {k: K1.ITEMS[k]["f"] for k in ("anuppanno", "uppādī")}
SIYA = {   # siyā … / na vattabbā …ti (no dash in the Pāli, so none in the Russian; ch. 15 wording)
    ("(14) Catūsu bhūmīsu vipāke paññā siyā uppannā, siyā uppādinī, na vattabbā anuppannāti. Catūsu bhūmīsu kusale "
     "tīsu bhūmīsu kiriyābyākate paññā siyā uppannā, siyā anuppannā, na vattabbā uppādinīti."):
        (f"(14) Мудрость {loc('catūsu bhūmīsu vipāke')[0]} иногда является {_I['uppanno']}, иногда {_I['uppādī']}, её "
         f"нельзя определить как «{_F['anuppanno']}». Мудрость "
         f"{loc('catūsu bhūmīsu kusale tīsu bhūmīsu kiriyābyākate')[0]} иногда является {_I['uppanno']}, иногда "
         f"{_I['anuppanno']}, её нельзя определить как «{_F['uppādī']}»."),
    "(15) Sabbāva paññā siyā atītā, siyā anāgatā, siyā paccuppannā.":
        f"(15) Всякая мудрость иногда является {_I['atīto']}, иногда {_I['anāgato']}, иногда {_I['paccuppanno']}.",
    "(17) Sabbāva paññā siyā ajjhattā, siyā bahiddhā, siyā ajjhattabahiddhā.":
        f"(17) Всякая мудрость иногда является {_I['ajjhatto']}, иногда {_I['bahiddho']}, иногда "
        f"{_I['ajjhattabahiddho']}.",
}
KNOW_SACCA_GEN = "знания, согласующегося с истинами"
KNOW_GEN = {"dhamme ñāṇaṃ": "знания явлений", "anvaye ñāṇaṃ": "знания по выводу", "pariye ñāṇaṃ": "знания охвата умов"}
ACAYA_BODY = {   # the bodies of ^2-797 / ^2-798 (after the label and question)
    "Kāmāvacarakusale paññā ācayāya no apacayāya.":
        f"Мудрость {loc('kāmāvacarakusale')[0]}, ведёт к накоплению, а не к убыванию.",
    "catūsu maggesu paññā apacayāya no ācayāya.": "Мудрость в четырёх путях ведёт к убыванию, а не к накоплению.",
    "rūpāvacarārūpāvacarakusale paññā ācayāya ceva apacayāya ca.":
        f"Мудрость {loc('rūpāvacarārūpāvacarakusale')[0]}, ведёт и к накоплению, и к убыванию.",
    "avasesā paññā neva ācayāya no apacayāya.": "Остальная мудрость не ведёт ни к накоплению, ни к убыванию.",
    ('Yāya paññāya kāmesu vītarāgo hoti, na ca abhiññāyo paṭivijjhati na ca saccāni – ayaṃ vuccati "paññā nibbidāya '
     'no paṭivedhāya".'):
        ("Мудрость, благодаря которой человек становится свободным от страсти к чувственным удовольствиям, но не "
         "проникает ни в высшие знания, ни в истины, – "
         f"{called(NAMES['paññā nibbidāya no paṭivedhāya'][1])}."),
    ('sveva paññāya kāmesu vītarāgo samāno abhiññāyo paṭivijjhati na ca saccāni – ayaṃ vuccati "paññā paṭivedhāya no '
     'nibbidāya".'):
        ("Тот же человек, будучи благодаря мудрости свободным от страсти к чувственным удовольствиям, проникает в "
         f"высшие знания, но не в истины, – {called(NAMES['paññā paṭivedhāya no nibbidāya'][1])}."),
    "catūsu maggesu paññā nibbidāya ceva paṭivedhāya ca.":
        "Мудрость в четырёх путях ведёт и к разочарованию, и к проникновению.",
    "avasesā paññā neva nibbidāya no paṭivedhāya.": "Остальная мудрость не ведёт ни к разочарованию, ни к проникновению.",
}


# ---- fivefold … ninefold expositions
def pancaka_nid(lines):
    a, b, c = lines
    assert a == ("(1) Tattha katamo pañcaṅgiko sammāsamādhi? Pītipharaṇatā, sukhapharaṇatā, cetopharaṇatā, "
                 "ālokapharaṇatā, paccavekkhaṇānimittaṃ. Dvīsu jhānesu paññā pītipharaṇatā. Tīsu jhānesu paññā "
                 "sukhapharaṇatā. Paracitte ñāṇaṃ cetopharaṇatā. Dibbacakkhu ālokapharaṇatā. Tamhā tamhā samādhimhā "
                 "vuṭṭhitassa paccavekkhaṇāñāṇaṃ paccavekkhaṇānimittaṃ. Ayaṃ vuccati pañcaṅgiko sammāsamādhi."), a
    PF = {"pīti": ("наполненность восторгом", "наполненностью восторгом"),
          "sukha": ("наполненность счастьем", "наполненностью счастьем"),
          "ceto": ("наполненность умом", "наполненностью умом"), "āloka": ("наполненность светом", "наполненностью светом"),
          "nimitta": ("признак рассмотрения", "признаком рассмотрения")}
    n5 = NAMES["pañcaṅgiko sammāsamādhi"]
    l1 = (f"(1) Что такое здесь {n5[0]}? " + cap(nlist([PF[k][0] for k in ("pīti", "sukha", "ceto", "āloka",
                                                                            "nimitta")])) + ". "
          f"Мудрость в двух медитативных погружениях является {PF['pīti'][1]}. Мудрость в трёх медитативных "
          f"погружениях является {PF['sukha'][1]}. Знание ума другого является {PF['ceto'][1]}. Божественный глаз "
          f"является {PF['āloka'][1]}. Знание рассмотрения у того, кто вышел из того или иного сосредоточения, "
          f"является {PF['nimitta'][1]}. Это называется {n5[1]}.")
    assert b.startswith("(2) Tattha katamo pañcañāṇiko sammāsamādhi? ") and b.endswith(
        '. So kho panāhaṃ imaṃ samādhiṃ sato samāpajjāmi sato vuṭṭhahāmī"ti paccattaññeva ñāṇaṃ uppajjati. Ayaṃ '
        "pañcañāṇiko sammāsamādhi. Evaṃ pañcavidhena ñāṇavatthu."), b
    slip('^2-804 «So kho panāhaṃ imaṃ samādhiṃ sato samāpajjāmi sato vuṭṭhahāmī"ti»: the opening quote mark is '
         "missing (rendered as meant)")
    k5 = ["Это сосредоточение приятно в настоящем и в будущем приносит приятный результат",
          "Это сосредоточение благородное и неплотское",
          "Это сосредоточение не практикуется низкими людьми",
          ("Это сосредоточение спокойное, высшее, обретённое успокоением, достигнутое через единение ума, не "
           "удерживаемое насильственным подавлением и сдерживанием"),
          "Я осознанно вхожу в это сосредоточение и осознанно выхожу из него"]
    n5b = NAMES["pañcañāṇiko sammāsamādhi"]
    l2 = (f"(2) Что такое здесь {n5b[0]}? " + " ".join(f"Лично возникает знание: «{x}»." for x in k5)
          + f" Это {n5b[0]}. {vidha_end(5)}")
    assert c == "Pañcakaṃ."
    return [l1, l2, close_label(5)]


def six_nid(lines):
    a, b = lines
    assert a == ("Tattha katamā chasu abhiññāsu paññā? Iddhividhe ñāṇaṃ, sotadhātuvisuddhiyā ñāṇaṃ, paracitte ñāṇaṃ, "
                 "pubbenivāsānussatiyā ñāṇaṃ, sattānaṃ cutūpapāte ñāṇaṃ, āsavānaṃ khaye ñāṇaṃ – imā chasu abhiññāsu "
                 "paññā. Evaṃ chabbidhena ñāṇavatthu."), a
    six = ["знание видов сверхспособностей", "знание очищения элемента уха", "знание ума другого",
           "знание припоминания прежних жизней", "знание смерти и нового рождения существ",
           "знание уничтожения влечений"]
    n = NAMES["chasu abhiññāsu paññā"][0]
    return [f"Что такое здесь {n}? {cap(', '.join(six))} – это {n}. {vidha_end(6)}", close_label(6)]


def seven_nid(lines):
    a, b = lines
    pe = "…pe… ".join(f"{x}ti ñāṇaṃ" for x in ("bhavapaccayā jātī", "upādānapaccayā bhavo", "taṇhāpaccayā upādānan",
                                               "vedanāpaccayā taṇhā", "phassapaccayā vedanā", "saḷāyatanapaccayā phasso",
                                               "nāmarūpapaccayā saḷāyatanan", "viññāṇapaccayā nāmarūpan",
                                               "saṅkhārapaccayā viññāṇan"))
    run = ("Jātipaccayā jarāmaraṇanti ñāṇaṃ, asati jātiyā natthi jarāmaraṇanti ñāṇaṃ, atītampi addhānaṃ jātipaccayā "
           "jarāmaraṇanti ñāṇaṃ, asati jātiyā natthi jarāmaraṇanti ñāṇaṃ, anāgatampi addhānaṃ jātipaccayā "
           "jarāmaraṇanti ñāṇaṃ, asati jātiyā natthi jarāmaraṇanti ñāṇaṃ.")
    steady = "Yampissa taṃ dhammaṭṭhitiñāṇaṃ tampi khayadhammaṃ vayadhammaṃ virāgadhammaṃ nirodhadhammanti ñāṇaṃ"
    run2 = ("avijjāpaccayā saṅkhārāti ñāṇaṃ, asati avijjāya natthi saṅkhārāti ñāṇaṃ, atītampi addhānaṃ avijjāpaccayā "
            "saṅkhārāti ñāṇaṃ, asati avijjāya natthi saṅkhārāti ñāṇaṃ, anāgatampi addhānaṃ avijjāpaccayā saṅkhārāti "
            "ñāṇaṃ, asati avijjāya natthi saṅkhārāti ñāṇaṃ.")
    exp = (f"Tattha katamāni sattasattati ñāṇavatthūni? {run} {steady}; {pe}…pe… {run2} {steady}. Imāni sattasattati "
           "ñāṇavatthūni. Evaṃ sattavidhena ñāṇavatthu.")
    assert a == exp, a
    nm = NAMES["sattasattati ñāṇavatthūni"][0]
    r1 = "; ".join(do_run("jāti"))
    r2 = "; ".join(do_run("avijjā"))
    mid = "… ".join(that(DO_LINK[k][0]) for k in ("bhava", "upādāna", "taṇhā", "vedanā", "phassa", "saḷāyatana",
                                                   "nāmarūpa", "viññāṇa", "saṅkhāra"))
    st = cap(that(STEADY))
    return [f"Что такое здесь {nm}? {cap(r1)}. {st}; {mid}… {r2}. {st}. Это {nm}. {vidha_end(7)}", close_label(7)]


def eight_nid(lines):
    a, b = lines
    pp = []
    for p, r in PATHS:
        pp += [f"мудрость на пути {r}", f"мудрость в плоде {r}"]
    n = NAMES["catūsu maggesu catūsu phalesu paññā"][0]
    exp = ("Tattha katamā catūsu maggesu catūsu phalesu paññā? " + cap(", ".join(
        f"{p}{w} paññā" for p, _ in PATHS for w in ("magge", "phale"))) + " – imā catūsu maggesu catūsu phalesu paññā. "
        "Evaṃ aṭṭhavidhena ñāṇavatthu.")
    assert a == exp and b == "Aṭṭhakaṃ.", (a, exp)
    return [f"Что такое здесь {n}? {cap(', '.join(pp))} – это {n}. {vidha_end(8)}", close_label(8)]


def nine_nid(lines):
    a, b = lines
    assert a.startswith("Tattha katamā navasu anupubbavihārasamāpattīsu paññā? Paṭhamajjhānasamāpattiyā paññā,") and \
        a.endswith("saññāvedayitanirodhasamāpattiyā vuṭṭhitassa paccavekkhaṇāñāṇaṃ – imā navasu "
                   "anupubbavihārasamāpattīsu paññā. Evaṃ navavidhena ñāṇavatthu."), a
    n = NAMES["navasu anupubbavihārasamāpattīsu paññā"][0]
    items = [f"мудрость в достижении {x}" for x in ATTAIN9]
    items.append(f"знание рассмотрения у того, кто вышел из достижения {CESSATION}")
    return [f"Что такое здесь {n}? {cap(', '.join(items))}, – это {n}. {vidha_end(9)}", close_label(9)]


# ---- tenfold exposition
def dasaka_1(lines):
    assert len(lines) == 8
    out = []
    x = [(f"{DS} принял какой-либо формирующий фактор за постоянный", f"{PJ} принял какой-либо формирующий фактор за "
          "постоянный"),
         (f"{DS} принял какой-либо формирующий фактор за счастье", f"{PJ} принял какой-либо формирующий фактор за счастье"),
         (f"{DS} принял какое-либо явление за самость", f"{PJ} принял какое-либо явление за самость"),
         (f"{DS} лишил жизни мать", f"{PJ} лишил жизни мать")]
    l1 = power_q(1, POWERS[0][1]) + " " + " ".join(
        knows(IMP.format(x=a), first=(i == 0)) + " " + knows(POS.format(x=b)) for i, (a, b) in enumerate(x))
    assert lines[0].startswith("(1) Tattha katamaṃ tathāgatassa ṭhānañca ṭhānato aṭṭhānañca aṭṭhānato yathābhūtaṃ "
                               'ñāṇaṃ? Idha tathāgato "aṭṭhānametaṃ anavakāso yaṃ diṭṭhisampanno puggalo kañci '
                               "saṅkhāraṃ niccato upagaccheyya"), lines[0]
    out.append(l1)
    assert lines[1].startswith("Aṭṭhānametaṃ anavakāso yaṃ diṭṭhisampanno puggalo pitaraṃ"), lines[1]
    slip('^2-809 line 2 «Aṭṭhānametaṃ anavakāso yaṃ diṭṭhisampanno puggalo pitaraṃ…»: the opening quote mark is '
         "missing (rendered as meant)")
    pe = "… ".join(["лишил жизни отца", "лишил жизни архата", "со злым умыслом пролил кровь Татхагаты",
                    "расколол Общину", "признал другого учителя", "породил восьмое существование"])
    out.append(knows(IMP.format(x=f"{DS} {pe}")) + " " + knows(POS.format(x=f"{PJ} породил восьмое существование")))
    v_cakka = "[вариант написания (Sī., Syā.): cakkavatti]"
    w = "в одной мировой системе"
    out.append(" ".join([
        knows(IMP.format(x=f"{w} одновременно появились два Достойных, Полностью Пробуждённых Будды")),
        knows(POS.format(x=f"{w} появился один Достойный, Полностью Пробуждённый Будда")),
        knows(IMP.format(x=f"{w} одновременно появились два царя, вращающих колесо {v_cakka}")),
        knows(POS.format(x=f"{w} появился один царь, вращающий колесо"))]))
    out.append(" ".join([
        knows(IMP.format(x="женщина была Достойным, Полностью Пробуждённым Буддой")),
        knows(POS.format(x="мужчина был Достойным, Полностью Пробуждённым Буддой")),
        knows(IMP.format(x="женщина была царём, вращающим колесо")),
        knows(POS.format(x="мужчина был царём, вращающим колесо")),
        knows(IMP.format(x="женщина заняла положение Сакки, заняла положение Мары, заняла положение Брахмы")),
        knows(POS.format(x="мужчина занял положение Сакки, занял положение Мары, занял положение Брахмы"))]))
    for good in (False, True):
        r1, r2 = (BAD_RES, GOOD_RES) if good else (GOOD_RES, BAD_RES)
        out.append(" ".join([
            knows(IMP.format(x=f"{conduct('kāya', good)} принесло {r1}")),
            knows(POS.format(x=f"{conduct('kāya', good)} принесло {r2}")),
            knows(IMP.format(x=f"{conduct('vacī', good)}… чтобы {conduct('mano', good)} принесло {r1}")),
            knows(POS.format(x=f"{conduct('vacī', good)}… чтобы {conduct('mano', good)} принесло {r2}"))]))
    for good in (False, True):
        d1, d2 = (WOE, HAPPY) if good else (HAPPY, WOE)
        out.append(" ".join([
            knows(IMP.format(x=f"{owner('kāya', good)} {AFTER_DEATH} {d1}")),
            knows(POS.format(x=f"{owner('kāya', good)} {AFTER_DEATH} {d2}")),
            knows(IMP.format(x=f"{owner('vacī', good)}… чтобы {owner('mano', good)} {AFTER_DEATH} {d1}")),
            knows(POS.format(x=f"{owner('vacī', good)}… чтобы {owner('mano', good)} {AFTER_DEATH} {d2}"))]))
    assert lines[7].endswith('"Ye ye dhammā yesaṃ yesaṃ dhammānaṃ hetū paccayā upādāya taṃ taṃ ṭhānaṃ, ye ye dhammā '
                             'yesaṃ yesaṃ dhammānaṃ na hetū appaccayā upādāya taṃ taṃ aṭṭhāna"nti. Yā tattha paññā '
                             "pajānanā…pe… amoho dhammavicayo sammādiṭṭhi – idaṃ tathāgatassa ṭhānañca ṭhānato "
                             "aṭṭhānañca aṭṭhānato yathābhūtaṃ ñāṇaṃ."), lines[7]
    out[-1] += (" «Те или иные явления, которые являются причинами и условиями тех или иных явлений, в силу этого в "
                "каждом таком случае являются возможным; те или иные явления, которые не являются ни причинами, ни "
                "условиями тех или иных явлений, в силу этого в каждом таком случае являются невозможным». "
                f"{power_end(POWERS[0][1])}")
    return out


GATI = [("gati", "удела"), ("upadhi", "облика"), ("kāla", "времени"), ("payoga", "усилия")]


def dasaka_2(lines):
    assert len(lines) == 4
    bad, good = "дурные совершаемые действия", "хорошие совершаемые действия"
    blocked = "Есть некоторые {k}, которые, будучи подавлены {s} {g}, не приносят результата."
    ripen = "Есть некоторые {k}, которые приносят результат, опираясь на {s} {g}."
    l = []
    l.append(" ".join(blocked.format(k=bad, s="благополучием", g=g) for _, g in GATI))
    l.append(" ".join(ripen.format(k=bad, s="неблагополучие", g=g) for _, g in GATI))
    l.append(" ".join(blocked.format(k=good, s="неблагополучием", g=g) for _, g in GATI))
    l.append(" ".join(ripen.format(k=good, s="благополучие", g=g) for _, g in GATI))
    l = ["«" + x for x in l]
    l[0] = f"{power_q(2, POWERS[1][1])} Здесь {TATH} понимает – {l[0]}"
    l[-1] = l[-1][:-1] + f"». {power_end(POWERS[1][1])}"
    assert lines[0].startswith("(2) Tattha katamaṃ tathāgatassa atītānāgatapaccuppannānaṃ") and lines[3].endswith(
        "ṭhānaso hetuso vipākaṃ yathābhūtaṃ ñāṇaṃ."), lines
    return l


GO = [("nirayagāmī", "ведёт в ад", " [вариант написания (Syā.): nirayagāminīti]"),
      ("tiracchānayonigāmī", "ведёт в мир животных",
       " [вариант чтения (Syā.): tiracchānagāminīti; так же и далее; следует свериться с комментарием]"),
      ("pettivisayagāmī", "ведёт в мир голодных духов", ""), ("manussalokagāmī", "ведёт в мир людей", ""),
      ("devalokagāmī", "ведёт в мир богов", ""), ("nibbānagāmī", "ведёт к нирване", "")]


def dasaka_3(lines):
    (ln,) = lines
    for p, _, _ in GO:
        assert f"ayaṃ maggo ayaṃ paṭipadā {p}" in ln, p
    units = [f"понимает: «Этот путь, этот способ практики {r}»{v}" for _, r, v in GO]
    return [f"{power_q(3, POWERS[2][1])} Здесь {TATH} " + "; ".join(units) + f". {power_end(POWERS[2][1])}"]


def dasaka_4(lines):
    (ln,) = lines
    assert "khandhanānattaṃ pajānāti, āyatananānattaṃ pajānāti, dhātunānattaṃ pajānāti, " \
           "anekadhātunānādhātulokanānattaṃ pajānātīti" in ln, ln
    div = ["разнообразие совокупностей", "разнообразие сфер восприятия", "разнообразие элементов",
           "разнообразие мира многих элементов и разных элементов"]
    return [f"{power_q(4, POWERS[3][1])} Здесь {TATH} " + ", ".join(f"понимает {d}" for d in div)
            + f". {power_end(POWERS[3][1])}"]


def dasaka_5(lines):
    l1, l2, l3 = disp_lines(quoted=True)
    return [f"{power_q(5, POWERS[4][1])} Здесь {TATH} понимает – {l1}", l2,
            f"{l3}». {power_end(POWERS[4][1])}"]


BEINGS6 = ("существ с малой пылью в глазах и с большой пылью в глазах, с острыми способностями и со слабыми "
           "способностями, с хорошими качествами и с плохими качествами, легко обучаемых и трудно обучаемых, способных "
           "и неспособных")


def who(desc, kind):
    return f"Кто такие {kind}?" if desc is None else desc


def dasaka_6(sid, lines):
    if sid == "2-814":
        return [f"{power_q(6, POWERS[5][1])} Здесь {TATH} понимает наклонность существ, понимает скрытую склонность, "
                f"понимает поведение, понимает устремление, понимает {BEINGS6}."]
    if sid == "2-815":
        (ln,) = lines
        assert ln.startswith('Katamo ca sattānaṃ āsayo? "Sassato loko"ti vā,') and ln.endswith(
            "Ete vā pana ubho ante anupagamma idappaccayatā paṭiccasamuppannesu dhammesu anulomikā khanti paṭiladdhā "
            "hoti yathābhūtaṃ ñāṇaṃ. Ayaṃ sattānaṃ āsayo."), ln
        slip('^2-815 «"hoti tathāgato paraṃ maraṇāti vā»: the closing quote mark is missing (rendered as meant)')
        return [f"А что такое наклонность существ? {TEN_VIEWS}; так существа опираются либо на воззрение о "
                "существовании, либо на воззрение о несуществовании. Или же, без приближения к этим двум крайностям, "
                "обретено согласующееся принятие в отношении явлений, возникших в зависимости от условий по закону "
                f"обусловленности, знание, {YATHA}. Это наклонность существ."]
    if sid == "2-816":
        an = ["чувственной страсти", "неприязни", "самомнению", "воззрениям", "колебанию", "страсти к существованию",
              "неведению"]
        return ["А что такое скрытая склонность существ? Семь скрытых склонностей – "
                + nlist([f"скрытая склонность к {a}" for a in an]) + ". Что в мире привлекательно и отрадно, в том у "
                "существ лежит скрытая склонность к страсти. Что в мире непривлекательно и неотрадно, в том у существ "
                "лежит скрытая склонность к неприязни. Так в этих двух явлениях сопутствует неведение. Самомнение, "
                "воззрение и колебание следует рассматривать как пребывающие вместе с ним. Это скрытая склонность "
                "существ."]
    if sid == "2-817":
        return ["А что такое поведение существ? Волевое действие, приносящее заслугу, волевое действие, не приносящее "
                "заслуги, и волевое действие, ведущее к непоколебимому, ограниченного уровня или великого уровня – это "
                "поведение существ."]
    if sid == "2-818":
        l1, l2, l3 = disp_lines(quoted=False)
        return [f"А что такое устремление существ? {l1}", l2, f"{l3}. Это устремление существ."]
    PRAC = {True: "практикуются, развиты, многократно повторяются и стали преобладающими",
            False: "не практикуются, не развиты, не повторяются многократно и не стали преобладающими"}
    if sid in ("2-819", "2-820"):
        big = sid == "2-819"
        kind = "существа с большой пылью в глазах" if big else "существа с малой пылью в глазах"
        lst = ("Десять основ омрачений – жадность, злоба, заблуждение, самомнение, воззрение, колебание, вялость, "
               "беспокойство, бессовестность и отсутствие страха перед дурным. ") if big else ""
        return [f"Кто такие {kind}? {lst}Существа, у которых эти десять основ омрачений {PRAC[big]}, и есть {kind}."]
    if sid in ("2-821", "2-822"):
        dull = sid == "2-821"
        kind = "существа со слабыми способностями" if dull else "существа с острыми способностями"
        lst = ("Пять способностей – способность веры, способность усердия, способность осознанности, способность "
               "сосредоточения и способность мудрости. ") if dull else ""
        return [f"Кто такие {kind}? {lst}Существа, у которых эти пять способностей {PRAC[not dull]}, и есть {kind}."]
    if sid == "2-823":
        return ["Кто такие существа с плохими качествами? Существа с дурными наклонностями, с дурными скрытыми "
                "склонностями, с дурным поведением, с дурными устремлениями, с большой пылью в глазах, со слабыми "
                "способностями и есть существа с плохими качествами."]
    if sid == "2-824":
        return ["Кто такие существа с хорошими качествами? Существа с хорошими наклонностями, с хорошим поведением, с "
                "хорошими устремлениями, с малой пылью в глазах, с острыми способностями и есть существа с хорошими "
                "качествами."]
    if sid == "2-825":
        return ["Кто такие трудно обучаемые существа? Существа с плохими качествами и есть трудно обучаемые существа. "
                "Существа с хорошими качествами и есть легко обучаемые существа."]
    OBST = ("наделённые препятствием в виде действий, наделённые препятствием в виде омрачений, наделённые "
            "препятствием в виде результатов действий")
    STEP = "вступить на предопределённый путь правильности в благих явлениях"
    if sid == "2-826":
        return [f"Кто такие неспособные существа? Существа, {OBST}, лишённые веры, лишённые стремления, лишённые "
                f"мудрости, неспособные {STEP}, и есть неспособные существа."]
    if sid == "2-827":
        neg = OBST.replace("наделённые", "не наделённые")
        return [f"Кто такие способные существа? Существа, {neg}, имеющие веру, обладающие стремлением, обладающие "
                f"мудростью, способные {STEP}, и есть способные существа. {power_end(POWERS[5][1])}"]
    raise KeyError(sid)


ORD = ["первое", "второе", "третье", "четвёртое", "пятое", "шестое", "седьмое", "восьмое"]


def dasaka_7(lines):
    assert len(lines) == 15
    out = []
    ss = ("Есть медитирующий, который считает {a} то, что на самом деле является {b}{v}")
    succ, fail = "успехом", "неудачей"
    m4 = cap("; ".join(low(x) for x in [ss.format(a=fail, b=succ, v=" [вариант написания (Ka.): sampattiyeva]"),
                                         ss.format(a=succ, b=fail, v=" [вариант написания (Ka.): vipattiyeva]"),
                                         ss.format(a=succ, b=succ, v=""), ss.format(a=fail, b=fail, v="")]))
    out.append(f"{power_q(7, P7_Q)} «Медитирующий». Четыре медитирующих. {m4} – это четыре медитирующих.")
    sp = "Есть медитирующий, который {a} входит в погружение и {b} выходит"
    out.append("Есть и другие четыре медитирующих. " + cap("; ".join(low(sp.format(a=a, b=b)) for a, b in (
        ("медленно", "быстро"), ("быстро", "медленно"), ("медленно", "медленно"), ("быстро", "быстро"))))
        + " – это четыре медитирующих.")
    sk = "искусен в сосредоточении в отношении сосредоточения"
    ak = "искусен в достижении в отношении сосредоточения"
    out.append("Есть и другие четыре медитирующих. " + "; ".join([
        f"Есть медитирующий, который {sk}, но не {ak}", f"есть медитирующий, который {ak}, но не {sk}",
        f"есть медитирующий, который и {sk}, и {ak}", f"есть медитирующий, который не {sk} и не {ak}"])
        + " – это четыре медитирующих.")
    out.append(f"«Медитативное погружение». {K10.FOUR_JH}")
    out.append(f"«Освобождение». Восемь освобождений. Будучи материальным, видит видимые формы – это {ORD[0]} "
               "освобождение.")
    out.append(f"Не воспринимая внутренней материальной формы, видит внешние видимые формы – это {ORD[1]} освобождение.")
    out.append(f"Он устремлён только к прекрасному – это {ORD[2]} освобождение.")
    for i, a in enumerate((K10.ARUPA1, K10.ARUPA2, K10.ARUPA3, K10.ARUPA4)):
        out.append(f"{cap(a)} – это {ORD[3 + i]} освобождение.")
    out.append(f"Полностью преодолев сферу ни восприятия, ни невосприятия, входит в прекращение восприятия и "
               f"ощущаемого и пребывает в нём – это {ORD[7]} освобождение.")
    out.append("«Сосредоточение». Три сосредоточения – " + nlist([
        "сосредоточение с направленной мыслью и удержанием мысли",
        "сосредоточение без направленной мысли, только с удержанием мысли",
        "сосредоточение без направленной мысли и без удержания мысли"]) + ".")
    out.append("«Медитативное достижение». Девять медитативных достижений последовательного пребывания – "
               + nlist([f"достижение {x}" for x in ATTAIN9] + [f"достижение {CESSATION}"]) + ".")
    out.append("«Омрачение»: явление, ведущее к упадку. «Очищение»: явление, ведущее к отличию. «Выход». И очищение "
               "является выходом, и выход из того или иного сосредоточения является выходом. "
               + power_end(POWERS[6][1]))
    exp_starts = ["(7) Tattha katamaṃ", "Aparepi cattāro jhāyī. Atthekacco jhāyī dandhaṃ",
                  "Aparepi cattāro jhāyī. Atthekacco jhāyī samādhismiṃ", '"Jhāna"nti.', '"Vimokkho"ti.',
                  "Ajjhattaṃ arūpasaññī", "Subhanteva", "Sabbaso rūpasaññānaṃ", "Sabbaso ākāsānañcāyatanaṃ",
                  "Sabbaso viññāṇañcāyatanaṃ", "Sabbaso ākiñcaññāyatanaṃ", "Sabbaso nevasaññānāsaññāyatanaṃ",
                  '"Samādhī"ti.', '"Samāpattī"ti.', '"Saṃkilesa"nti']
    for ln, st in zip(lines, exp_starts):
        assert ln.startswith(st), (ln, st)
    assert "jhānavimokkhasamādhisamāpattīnaṃ saṃkilesaṃ vodānaṃ yathābhūtaṃ ñāṇaṃ?" in lines[0]
    slip("^2-828 the question «… saṃkilesaṃ vodānaṃ yathābhūtaṃ ñāṇaṃ?» lacks «vuṭṭhānaṃ» (the matrix and the closing "
         "sentence have it): translated as written")
    return out


LIVES = ["одно рождение", "два рождения", "три рождения", "четыре рождения", "пять рождений", "десять рождений",
         "двадцать рождений", "тридцать рождений", "сорок рождений", "пятьдесят рождений", "сто рождений",
         "тысячу рождений", "сто тысяч рождений", "многие эпохи сжатия мира", "многие эпохи развёртывания мира",
         "многие эпохи сжатия и развёртывания мира"]
THERE = ("с таким-то именем, из такого-то рода, с таким-то обликом, такой была моя пища, такие удовольствия и боли я "
         "испытывал, таким был предел срока моей жизни")


def dasaka_8(lines):
    (ln,) = lines
    assert "seyyathidaṃ – ekampi jātiṃ" in ln and 'so tato cuto idhūpapanno"ti.' in ln, ln
    return [f"{power_q(8, POWERS[7][1])} Здесь {TATH} вспоминает многие прежние жизни, а именно – " + ", ".join(LIVES)
            + f": «Там я был {THERE}; уйдя оттуда, я появился там; и там я был {THERE}; уйдя оттуда, я появился "
            "здесь». Так он вспоминает многие прежние жизни со всеми их особенностями и подробностями. "
            + power_end(POWERS[7][1])]


SEES = ("божественным глазом, очищенным и превосходящим человеческий, видит существ умирающими и появляющимися, "
        "низшими и высшими, красивыми и безобразными, счастливыми и несчастными, понимает существ, идущих согласно "
        "своим действиям")


def dasaka_9(lines):
    (ln,) = lines
    assert 'yathākammūpage satte pajānāti – "ime vata bhonto sattā' in ln, ln
    bad = ("Эти почтенные существа были наделены дурным телесным поведением, наделены дурным речевым поведением, "
           "наделены дурным умственным поведением, хулили благородных, придерживались ложного воззрения, принимали на "
           f"себя действия, основанные на ложном воззрении. После распада тела, после смерти они появились {WOE}.")
    good = ("А эти почтенные существа были наделены хорошим телесным поведением, наделены хорошим речевым поведением, "
            "наделены хорошим умственным поведением, не хулили благородных, придерживались правильного воззрения, "
            f"принимали на себя действия, основанные на правильном воззрении. После распада тела, после смерти они появились "
            f"{HAPPY}.")
    return [f"{power_q(9, POWERS[8][1])} Здесь {TATH} {SEES}, – «{bad} {good[:-1]}». Так {SEES.replace('видит', 'он видит', 1)}. "
            + power_end(POWERS[8][1])]


def dasaka_10(lines):
    a, b, c = lines
    assert a.startswith("(10) Tattha katamaṃ tathāgatassa āsavānaṃ khayaṃ") and a.endswith("yathābhūtaṃ ñāṇanti."), a
    assert b == "Dasakaṃ." and c == "Ñāṇavibhaṅgo niṭṭhito."
    return [f"{power_q(10, POWERS[9][1])} Здесь {TATH} с уничтожением влечений уже в этой жизни, сам постигнув высшим "
            "знанием и осуществив свободное от влечений освобождение ума и освобождение мудростью, достигает их и "
            f"пребывает в них. {power_end(POWERS[9][1])}", close_label(10), f"{S.CH_TITLE[16][1]} {S.DONE}."]


# =========================================================================== headings
SPLIT_H = {"Ekaka": "единиц", "Duka": "пар", "Tika": "троек", "Catukka": "четвёрок", "Pañcaka": "пятёрок",
           "Chakka": "шестёрок", "Sattaka": "семёрок", "Aṭṭhaka": "восьмёрок", "Navaka": "девяток", "Dasaka": "десяток"}
NID_N = {"Ekaka": 1, "Duka": 2, "Tika": 3, "Catukka": 4, "Pañcaka": 5, "Chakka": 6, "Sattaka": 7, "Aṭṭhaka": 8,
         "Navaka": 9, "Dasaka": 10}


def heading(ln):
    lvl, text = ln.split(" ", 1)
    if text == S.CH_TITLE[16][0]:
        return f"{lvl} {S.CH_TITLE[16][1]}"
    if text == "Mātikā":
        return f"{lvl} Матрица"
    m = re.match(r"^(\w+?)mātikā$", text)
    if m:
        return f"{lvl} Матрица {SPLIT_H[m.group(1)]}"
    m = re.match(r"^(\w+?)niddeso$", text)
    return f"{lvl} Разъяснение {S.NUMW[NID_N[m.group(1)]]}"


# =========================================================================== build
SMALL = {"2-755": (5, "(1) Pañcaṅgiko sammāsamādhi (2) pañcañāṇiko sammāsamādhi",
                   f"(1) {cap(NAMES['pañcaṅgiko sammāsamādhi'][0])} (2) {NAMES['pañcañāṇiko sammāsamādhi'][0]}"),
         "2-756": (6, "(1) Chasu abhiññāsu paññā", f"(1) {cap(NAMES['chasu abhiññāsu paññā'][0])}"),
         "2-757": (7, "(1) Sattasattati ñāṇavatthūni", f"(1) {cap(NAMES['sattasattati ñāṇavatthūni'][0])}"),
         "2-758": (8, "(1) Catūsu maggesu, catūsu phalesu paññā", "(1) Мудрость в четырёх путях, в четырёх плодах"),
         "2-759": (9, "(1) Navasu anupubbavihārasamāpattīsu paññā",
                   f"(1) {cap(NAMES['navasu anupubbavihārasamāpattīsu paññā'][0])}")}
VIDHA_P = {2: "Duvidhena", 3: "Tividhena", 4: "Catubbidhena", 5: "Pañcavidhena", 6: "Chabbidhena", 7: "Sattavidhena",
           8: "Aṭṭhavidhena", 9: "Navavidhena", 10: "Dasavidhena"}


def seg(sid, lines, state):
    SID["sid"] = sid
    n = int(sid.split("-")[1]) if re.match(r"^2-\d+$", sid) else None
    if n == 751:
        out, keys = eka_matrix(lines)
        state["keys"] = keys
        return out
    if n == 752:
        return duka_matrix(lines)
    if n == 753:
        return tika_matrix(lines)
    if n == 754:
        return catukka_matrix(lines)
    if sid in SMALL:
        k, p, r = SMALL[sid]
        assert lines == [f"{VIDHA_P[k]} ñāṇavatthu –", p, f"Evaṃ {VIDHA_P[k].lower()} ñāṇavatthu."], lines
        return [vidha_head(k), r, vidha_end(k)]
    if n == 760:
        return dasa_matrix(lines)
    if n == 761:
        return eka_meva(lines, state["keys"])
    if n in (762, 764):
        return [eka_gloss(ln) for ln in lines]
    if n == 763:
        (ln,) = lines
        assert ln.startswith("Na aññamaññassa gocaravisayaṃ paccanubhontīti cakkhuviññāṇassa gocaravisayaṃ")
        return [pairs_line(ln, "gocara")]
    if n == 765:
        (ln,) = lines
        assert ln.startswith("Na aññamaññassa samanantarā uppajjantīti cakkhuviññāṇassa uppannasamanantarā")
        return [pairs_line(ln, "after")]
    if n == 766:
        out = []
        for ln in lines:
            if ln == "Evaṃ ekavidhena ñāṇavatthu.":
                out.append(vidha_end(1))
            elif ln == "Ekakaṃ.":
                out.append(close_label(1))
            elif ln.endswith("Evaṃ yāthāvakavatthuvibhāvanā paññā."):
                out.append(eka_gloss(ln[:-len(" Evaṃ yāthāvakavatthuvibhāvanā paññā.")]) + f" Такова {REAL}.")
            else:
                out.append(eka_gloss(ln))
        return out
    if n == 767:
        return duka_nid(lines)
    if sid in ("2-768", "2-771"):
        return tika_nid_special(sid, lines)
    if 769 <= n <= 792:
        return [gen_line(ln) for ln in lines]
    if 793 <= n <= 803:
        return catukka_nid(sid, lines)
    if n == 804:
        return pancaka_nid(lines)
    if n == 805:
        return six_nid(lines)
    if n == 806:
        return seven_nid(lines)
    if n == 807:
        return eight_nid(lines)
    if n == 808:
        return nine_nid(lines)
    if n == 809:
        return dasaka_1(lines)
    if n == 810:
        return dasaka_2(lines)
    if n == 811:
        return dasaka_3(lines)
    if n == 812:
        return dasaka_4(lines)
    if n == 813:
        return dasaka_5(lines)
    if 814 <= n <= 827:
        return dasaka_6(sid, lines)
    if n == 828:
        return dasaka_7(lines)
    if n == 829:
        return dasaka_8(lines)
    if n == 830:
        return dasaka_9(lines)
    if n == 831:
        return dasaka_10(lines)
    raise KeyError(sid)


def build():
    pali = (S.PALI / PART).read_text(encoding="utf-8")
    h, state = {}, {}
    for sid, lines in S.segs(pali):
        lines = [re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", ln) for ln in lines]
        if lines[0].startswith("#"):
            assert len(lines) == 1
            h[sid] = [heading(lines[0])]
            continue
        lines = [ln.replace(" …pe…", "…pe…") for ln in lines]
        h[sid] = seg(sid, lines, state)
        assert len(h[sid]) == len(lines), (sid, len(h[sid]), len(lines))
    return pali, h


# =========================================================================== checks against earlier Russian
def check():
    pi1 = PI1_RU.read_text(encoding="utf-8")
    assert TEN_VIEWS in pi1, "pi-1 ^1-1105 views"
    for s in ("у хорошо и дурно совершённых поступков", "рождающихся самопроизвольно существ", "идущих верным путём",
              "которые, сами постигнув высшим знанием и осуществив этот мир и иной мир, возвещают о них"):
        assert s in pi1, s
    ch = {f: (S.OUT / f).read_text(encoding="utf-8") for f in (
        "6-paticcasamuppadavibhango.md", "7-satipatthanavibhango.md", "8-sammappadhanavibhango.md",
        "12-jhanavibhango.md", "15-patisambhidavibhango.md")}
    for k, (a, _) in DO_LINK.items():
        assert a.split(" обусловлен")[0] + " обусловлен" in ch["6-paticcasamuppadavibhango.md"], a
    assert "умножения, обширности, развития и завершённости" in ch["8-sammappadhanavibhango.md"]
    assert "понимает ум, охваченный страстью: «Ум охвачен страстью»" in ch["7-satipatthanavibhango.md"]
    for a in (K10.ARUPA1, K10.ARUPA2, K10.ARUPA3, K10.ARUPA4):
        assert a in ch["12-jhanavibhango.md"], a
    assert K1315.NIRUTTI_CL in ch["15-patisambhidavibhango.md"]
    assert WIS in ch["7-satipatthanavibhango.md"]


# =========================================================================== notes
def notes_md():
    L = ["# pi-2 Russian rails: new formulas of chapter 16 (^2-751 … ^2-831)", "",
         "Generated by build_rails_16_ru.py; import it instead of retyping. Strings already in ru-rails-formulas.md "
         "(sample) or notes-1 … notes-13-15 are not repeated.", "",
         "## Headings, divisions, closing labels", ""]
    L += [f"#### {k}mātikā = #### Матрица {v}" for k, v in SPLIT_H.items()]
    L += ["#### Mātikā = #### Матрица"]
    L += [f"##### {k}niddeso = ##### Разъяснение {S.NUMW[v]}" for k, v in NID_N.items()]
    L += [f"<N>vidhena ñāṇavatthu – = {vidha_head(1).replace('по одному', '<N>')} (e.g. «{vidha_head(2)}»)",
          f"Evaṃ <N>vidhena ñāṇavatthu. = {vidha_end(1).replace('по одному', '<N>')} (e.g. «{vidha_end(10)}»)",
          "Ekakaṃ. / Dukaṃ. / Tikaṃ. / Catukkaṃ. … Dasakaṃ. = " + " / ".join(close_label(i) for i in range(1, 11)),
          "(Ka) / (Kha) / (Ga) / (Gha) / (Kha-gha) = (а) / (б) / (в) / (г) / (б-г); (1. Ka) = (1. а)",
          "", "## Wisdom phrases", "",
          "<X> paññā (matrix item X) = the ch. 1 matrix item said of «мудрость»: a one-word attribute before the noun "
          "(«мирская мудрость»), a phrase after it with a comma («мудрость, подверженная влечениям»), «с …» items "
          "without a comma («мудрость с направленной мыслью»); instrumental after «является»",
          "atthi X, atthi Y (of a wisdom) = бывает X(ins), бывает Y(ins); with the two subjects of ^2-753 (51) "
          "«Мудрость, сопровождаемая восторгом, и мудрость, сопровождаемая счастьем,» the plural «бывают …» (also in "
          "the following «Atthi …» lines (52)-(63))",
          f"<location> paññā X paññā = Мудрость <location> является X(ins); e.g. «{cap(is_sentence('Tīsu bhūmīsu kusalābyākate paññā lokiyā paññā, catūsu maggesu catūsu phalesu paññā lokuttarā paññā'))}.»",
          "locations: " + "; ".join(f"{k} = {v}" for k, v in LOC_KIND.items())
          + "; tīsu / catūsu bhūmīsu = на трёх / четырёх уровнях; catūsu maggesu catūsu phalesu = в четырёх путях и в "
            "четырёх плодах; Xāvacarakusalābyākate = в благом и этически неопределённом, относящемся к миру X",
          "Sabbāva paññā siyā X, siyā Y, siyā Z. = Всякая мудрость иногда является X, иногда Y, иногда Z.",
          "sabbāpi samāpannassa paññā X = Всякая мудрость того, кто вошёл в медитативное достижение, является X(ins)",
          "PH: " + "; ".join(f"{k} = {v[0]}" for k, v in PH.items()),
          "NAMES: " + "; ".join(f"{k} = {v[0]}" for k, v in NAMES.items()),
          "", "## Exposition frames", "",
          f"<cond> yā uppajjati paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi – ayaṃ/idaṃ vuccati \"X\". = <cond> "
          f"{ARISE} – это называется «X(ins)».",
          "conditions: " + "; ".join(f"{k} = {v}" for k, v in COND.items()),
          "Xsamudayaṃ ārabbha…pe… Xnirodhaṃ ārabbha…pe… Xnirodhagāminiṃ paṭipadaṃ ārabbha = " + PE_COND["dukkha"],
          f"– yā tattha paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi – idaṃ vuccati X = – {YA_TATTHA}, – это "
          "называется …",
          f"yā evarūpā paññā pajānanā…pe… = {YA_EVARUPA}",
          f"Yā tattha paññā …– idaṃ tathāgatassa X yathābhūtaṃ ñāṇaṃ. = {cap(YA_TATTHA)}, – это знание Татхагаты X, "
          f"{YATHA}.",
          "Maggasamaṅgissa ñāṇaṃ Xpetaṃ ñāṇaṃ, … = Знание обладающего путём является и знанием X, и …",
          f"evarūpiṃ anulomikaṃ khantiṃ diṭṭhiṃ ruciṃ mudiṃ pekkhaṃ dhammanijjhānakkhantiṃ = {ACCEPT}",
          f"rūpaṃ aniccanti vā vedanā…pe… saññā… saṅkhārā… viññāṇaṃ aniccanti vā = {IMPERM}",
          f"yogavihitesu vā kammāyatanesu … vijjāṭṭhānesu = {YOGA}",
          f"Atthi dinnaṃ, atthi yiṭṭhaṃ, … pavedentī = {RIGHT_VIEW} (pi-1 ^1-1221, put positively)",
          "", "## The onefold matrix (five kinds of consciousness)", "",
          "pañca viññāṇā na hetū, ahetukā, … = пять видов сознания не являются корнями; не имеют корней; … (ch. 1 "
          "plural predicates, «; » between them)",
          f"-meva (^2-761) = {SURE} + predicate; uppannaṃ manoviññāṇaviññeyyameva = {MEVA_TAIL['uppannaṃ manoviññāṇaviññeyyameva']}",
          ]
    L += [f"{k} = {v}" for k, v in EKA.items()]
    L += [f"\"{k}\"ti … = «{v[0]}»: {v[1]}." for k, v in EKA_GLOSS.items()]
    L += [f"yāthāvakavatthuvibhāvanā paññā = {REAL}",
          "Na aññamaññassa gocaravisayaṃ paccanubhontīti X-assa gocaravisayaṃ Y na paccanubhoti, … = «…»: сферы "
          "действия X(gen) Y не испытывает, и сферы действия Y(gen) X не испытывает. …",
          "X-assa uppannasamanantarā Y na uppajjati = Сразу после возникновения X(gen) Y не возникает",
          "", "## The ten powers", "",
          f"dasa tathāgatassa tathāgatabalāni = {POWERS10}; tathāgatabalaṃ = {POWER_OF}",
          f"āsabhaṃ ṭhānaṃ paṭijānāti, parisāsu sīhanādaṃ nadati, brahmacakkaṃ pavatteti = {FEATS}",
          "powers (acc. / prep.): " + "; ".join(f"{a} / {b}" for a, b in POWERS),
          f"aṭṭhānametaṃ anavakāso yaṃ …, netaṃ ṭhānaṃ vijjati = {IMP}",
          f"ṭhānañca kho etaṃ vijjati yaṃ …, ṭhānametaṃ vijjati = {POS}",
          f"diṭṭhisampanno puggalo = {DS[:-1]}; puthujjano = {PJ}",
          f"iṭṭho kanto manāpo vipāko = {GOOD_RES}; aniṭṭho akanto amanāpo = {BAD_RES}",
          f"X-samaṅgī tannidānaṃ tappaccayā kāyassa bhedā paraṃ maraṇā … upapajjeyya = обладающий X {AFTER_DEATH} …",
          f"sugatiṃ saggaṃ lokaṃ = {HAPPY}; apāyaṃ duggatiṃ vinipātaṃ nirayaṃ = {WOE}",
          "atthekaccāni pāpakāni kammasamādānāni X-sampattipaṭibāḷhāni na vipaccanti = Есть некоторые дурные совершаемые "
          "действия, которые, будучи подавлены благополучием X, не приносят результата; X-vipattiṃ āgamma vipaccanti = "
          "…, которые приносят результат, опираясь на неблагополучие X (gati / upadhi / kāla / payoga = удела / облика "
          "/ времени / усилия)",
          "ayaṃ maggo ayaṃ paṭipadā X-gāmī = Этот путь, этот способ практики ведёт X: " + "; ".join(
              f"{p} = {r}" for p, r, _ in GO),
          f"apparajakkhe mahārajakkhe … bhabbābhabbe satte = {BEINGS6}",
          "Katame te sattā X? … ime te sattā X. = Кто такие существа X? … и есть существа X.",
          ("Jhāyī / Jhāna / Vimokkho / Samādhī / Samāpattī (ti) = «Медитирующий» / «Медитативное погружение» / "
           "«Освобождение» / «Сосредоточение» / «Медитативное достижение»"),
          "Saṃkilesa / Vodāna / Vuṭṭhāna (ti) = «Омрачение» / «Очищение» / «Выход»; hānabhāgiyo / visesabhāgiyo dhammo "
          "= явление, ведущее к упадку / к отличию",
          ("Atthekacco jhāyī sampattiyeva samānaṃ vipattīti pacceti = есть медитирующий, который считает неудачей то, "
           "что на самом деле является успехом"),
          f"pubbenivāsa list = {', '.join(LIVES)}; amutrāsiṃ evaṃnāmo … = Там я был {THERE}",
          f"dibbena cakkhunā … yathākammūpage satte pajānāti = {SEES}",
          "", "## Dependent origination knowledge (^2-806)", "",
          "Xpaccayā Yti ñāṇaṃ = знание того, что X(ins) обусловлен(о/а/ы) Y; asati X natthi Yti ñāṇaṃ = знание того, "
          "что, когда нет X(gen), нет Y(gen); atītampi / anāgatampi addhānaṃ = и в прошлом / в будущем времени",
          f"Yampissa taṃ dhammaṭṭhitiñāṇaṃ tampi khayadhammaṃ vayadhammaṃ virāgadhammaṃ nirodhadhammanti ñāṇaṃ = "
          f"{that(STEADY)}",
          ]
    return "\n".join(L) + "\n"


def main():
    check()
    pali, h = build()
    (S.OUT / PART).write_text(K23.render(pali, h), encoding="utf-8", newline="\n")
    print(f"wrote {PART}: {len(S.segs(pali))} segments")
    NOTES_PATH.write_text(notes_md(), encoding="utf-8", newline="\n")
    for s in SLIPS + K1.SLIPS:
        print("slip:", s)


if __name__ == "__main__":
    main()
