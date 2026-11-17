# -*- coding: utf-8 -*-
"""pi-2 Vibhaṅga, Russian plain zero-shot: chapter 6 (Paṭiccasamuppādavibhaṅga).

usage: python -I -X utf8 build_6_ru.py
Writes AI_translation\\russian\\pi-2-russian-plain-zeroshot_split_chapters\\6-paticcasamuppadavibhango.md.
Reuses build_ch1_sample_ru (S: frames, headings, write), build_2_3_ru (T: pi-1 lookup, citta synonyms, feelings)
and build_4_5_ru (F: Suttanta strings for birth, ageing, death, sorrow …, lokuttara wisdom body).
The dependent-origination chain follows pi-1 ^1-1343 («Неведением обусловлены формирующие факторы, …»); mind-type
openings, jhāna openings and the definitions (moho, cetanā, citta, phassa, vedanā, rāga, diṭṭhi, dosa, vicikicchā,
uddhacca, alobha, adosa, amoha, saddhā …) are pi-1 strings, asserted byte for byte. Each link is generated from
fixed noun tables, so every repeat is identical. Unknown Pāli raises KeyError. Importing writes nothing.
"""
import os, re, sys

HERE = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru"
sys.path.insert(0, HERE)
import build_ch1_sample_ru as S  # noqa: E402
import build_2_3_ru as T  # noqa: E402
import build_4_5_ru as F  # noqa: E402

DASH = S.DASH
cap = S.cap
PI1 = T.PI1
PI1_ALL = F.PI1_ALL
in_pi1 = F.in_pi1
edit = F.edit
FN = "6-paticcasamuppadavibhango.md"

# ================================================================ 1. nouns of the links: nom, ins, acc, gender (m f n pl)
N = {
    "avijjā": ("неведение", "неведением", "неведение", "n"),
    "saṅkhāro": ("формирующий фактор", "формирующим фактором", "формирующий фактор", "m"),
    "saṅkhārā": ("формирующие факторы", "формирующими факторами", "формирующие факторы", "pl"),
    "viññāṇaṃ": ("сознание", "сознанием", "сознание", "n"),
    "nāmaṃ": ("умственное", "умственным", "умственное", "n"),                       # pi-1 nāma
    "rūpaṃ": ("материальная форма", "материальной формой", "материальную форму", "f"),
    "nāmarūpaṃ": ("умственное и материальная форма", "умственным и материальной формой",
                  "умственное и материальную форму", "pl"),                         # pi-1 ^1-1343
    "chaṭṭhāyatanaṃ": ("шестая сфера восприятия", "шестой сферой восприятия", "шестую сферу восприятия", "f"),
    "saḷāyatanaṃ": ("шесть сфер восприятия", "шестью сферами восприятия", "шесть сфер восприятия", "pl"),  # pi-1
    "phasso": ("контакт", "контактом", "контакт", "m"),
    "vedanā": ("чувство", "чувством", "чувство", "n"),
    "taṇhā": ("жажда", "жаждой", "жажду", "f"),
    "upādānaṃ": ("цепляние", "цеплянием", "цепляние", "n"),
    "bhavo": ("существование", "существованием", "существование", "n"),
    "jāti": ("рождение", "рождением", "рождение", "n"),
    "jarāmaraṇaṃ": ("старение и смерть", "старением и смертью", "старение и смерть", "pl"),
    "adhimokkho": ("решимость", "решимостью", "решимость", "f"),                   # core adhimokkha
    "paṭighaṃ": ("неприязнь", "неприязнью", "неприязнь", "f"),                     # pi-1
    "vicikicchā": ("колебание", "колебанием", "колебание", "n"),                   # core
    "uddhaccaṃ": ("беспокойство", "беспокойством", "беспокойство", "n"),           # core
    "pasādo": ("ясная вера", "ясной верой", "ясную веру", "f"),                    # new
}
STEM = {"avijjā": "avijjā", "saṅkhāra": "saṅkhāro", "viññāṇa": "viññāṇaṃ", "nāma": "nāmaṃ", "nāmarūpa": "nāmarūpaṃ",
        "chaṭṭhāyatana": "chaṭṭhāyatanaṃ", "saḷāyatana": "saḷāyatanaṃ", "phassa": "phasso", "vedanā": "vedanā",
        "taṇhā": "taṇhā", "upādāna": "upādānaṃ", "bhava": "bhavo", "jāti": "jāti", "adhimokkha": "adhimokkho",
        "paṭigha": "paṭighaṃ", "vicikicchā": "vicikicchā", "uddhacca": "uddhaccaṃ", "pasāda": "pasādo"}
COND_EXTRA = {"kusalamūla": "благими корнями", "akusalamūla": "неблагими корнями"}
SUTTA = {"on": False}   # Suttantabhājanīya: saṅkhāra- as condition is plural (pi-1 «формирующими факторами»)

OBUS = {"short": dict(m="обусловлен", f="обусловлена", n="обусловлено", pl="обусловлены"),
        "nom": dict(m="обусловленный", f="обусловленная", n="обусловленное", pl="обусловленные"),
        "ins": dict(m="обусловленным", f="обусловленной", n="обусловленным", pl="обусловленными")}
SVYAZ = {"short": dict(m="связан", f="связана", n="связано", pl="связаны"),
         "nom": dict(m="связанный", f="связанная", n="связанное", pl="связанные"),
         "ins": dict(m="связанным", f="связанной", n="связанным", pl="связанными")}
IMEYU = {"nom": dict(m="имеющий", f="имеющая", n="имеющее", pl="имеющие"),
         "ins": dict(m="имеющим", f="имеющей", n="имеющим", pl="имеющими")}
CAUSE = "причиной"   # Xhetuka = «имеющий причиной X» [pi-1 ^1-666 cittahetukaṃ «имеющей причиной ум»]
in_pi1("имеющей причиной ум")


def cond_ins(stem):
    if stem in COND_EXTRA:
        return COND_EXTRA[stem]
    if stem == "saṅkhāra" and SUTTA["on"]:
        return N["saṅkhārā"][1]
    return N[STEM[stem]][1]


LINK = re.compile(r"^(\w+?)paccayā(pi)? (\w+)(?: (\w+?)(hetuk|sampayutt)(?:o|aṃ|ā))?(?: (nāmaṃ|chaṭṭhāyatanaṃ))?$")
GRIEF_LINK = "jātipaccayā jarāmaraṇaṃ sokaparidevadukkhadomanassupāyāsā sambhavanti"
GRIEF_LINK_RU = "рождением обусловлены и возникают старение и смерть, " + F.GRIEF5     # pi-1 ^1-1343


def link(s, mode):
    """mode: chain («неведением обусловлен формирующий фактор»), nom / ins (noun phrase of the question / answer)."""
    if s == GRIEF_LINK and mode == "chain":
        return GRIEF_LINK_RU
    m = LINK.match(s)
    if not m:
        raise KeyError("link: " + s)
    stem, pi, res, qstem, qkind, apo = m.groups()
    nom, ins, acc, g = N[res]
    c = cond_ins(stem)
    also = "тоже " if pi else ""
    if mode == "chain":
        out = f"{'и ' if pi else ''}{c} {also}{OBUS['short'][g]} {nom}"
    elif mode == "nom":
        out = f"{nom}, {also}{OBUS['nom'][g]} {c}"
    else:
        out = f"{ins}, {also}{OBUS['ins'][g]} {c}"
    if qkind and apo:   # "nāmarūpaṃ viññāṇasampayuttaṃ nāmaṃ": the nāma of it is associated with consciousness
        a = N[apo]
        out += f", из которых {a[0]} {SVYAZ['short'][a[3]]} с {N[STEM[qstem]][1]}"
    elif qkind:
        z = N[STEM[qstem]]
        if mode == "chain":
            out += (f", {IMEYU['nom'][g]} {CAUSE} {z[2]}" if qkind == "hetuk" else f", {SVYAZ['nom'][g]} с {z[1]}")
        else:
            case = "nom" if mode == "nom" else "ins"
            out += (f" и {IMEYU[case][g]} {CAUSE} {z[2]}" if qkind == "hetuk" else f" и {SVYAZ[case][g]} с {z[1]}")
    return out


def chain(s):
    """links separated by ', ' / '; ' / '…pe… ' (Pāli punctuation kept)."""
    parts = re.split(r"(, |; |…pe… )", s[:1].lower() + s[1:])
    out = []
    for p in parts:
        if p in (", ", "; "):
            out.append(p)
        elif p == "…pe… ":
            out.append("… ")
        else:
            out.append(link(p, "chain"))
    return "".join(out)


SUTTA_CHAIN_RU = None   # checked against pi-1 ^1-1343 in main()

# ================================================================ 2. fixed sentences
EVAM = "Так происходит возникновение всей этой совокупности страдания."            # pi-1 ^1-1343
EVAM_LOW = "так происходит возникновение всей этой совокупности страдания"
in_pi1(EVAM_LOW)
EVAM_D = "Так происходит возникновение этих явлений."                               # Evametesaṃ dhammānaṃ samudayo hoti.
EVAM_D_LOW = "так происходит возникновение этих явлений"
MEANS = ("так происходит сочетание всей этой совокупности страдания, происходит её схождение, происходит её соединение, "
         "происходит её проявление")                                               # saṅgati, samāgamo, samodhānaṃ, pātubhāvo
MEANS_D = "так происходит сочетание этих явлений, происходит их схождение, происходит их соединение, происходит их проявление"
TENA = "поэтому и говорится:"                                                      # tena vuccati "…"ti

SENT = {
    "Evametassa kevalassa dukkhakkhandhassa samudayo hoti.": EVAM,
    "Evametesaṃ dhammānaṃ samudayo hoti.": EVAM_D,
    "Evametassa kevalassa dukkhakkhandhassa samudayo hotīti, evametassa kevalassa dukkhakkhandhassa saṅgati hoti, "
    "samāgamo hoti, samodhānaṃ hoti, pātubhāvo hoti.": f"«{cap(EVAM_LOW)}» означает, что {MEANS}.",
    "Evametassa kevalassa dukkhakkhandhassa samudayo hotīti.": f"«{cap(EVAM_LOW)}».",
    "Evametassa kevalassa dukkhakkhandhassa saṅgati hoti, samāgamo hoti, samodhānaṃ hoti, pātubhāvo hoti.":
        f"Это означает, что {MEANS}.",
    "Evametesaṃ dhammānaṃ samudayo hotīti.": f"«{cap(EVAM_D_LOW)}».",
    "Evametesaṃ dhammānaṃ saṅgati hoti, samāgamo hoti, samodhānaṃ hoti, pātubhāvo hoti.": f"Это означает, что {MEANS_D}.",
    'Tena vuccati "evametassa kevalassa dukkhakkhandhassa samudayo hotī"ti.': f"{cap(TENA)} «{EVAM_LOW}».",
    'Tena vuccati "evametesaṃ dhammānaṃ samudayo hotī"ti.': f"{cap(TENA)} «{EVAM_D_LOW}».",
    "Atthi nāmaṃ, atthi rūpaṃ.": "Есть умственное, есть материальная форма.",
    "Atthi jarā, atthi maraṇaṃ.": "Есть старение, есть смерть.",
    "Iti idañca nāmaṃ, idañca rūpaṃ.": "Таким образом, есть и это умственное, и эта материальная форма.",
    "Iti ayañca jarā, idañca maraṇaṃ.": "Таким образом, есть и это старение, и эта смерть.",
    "Iti ayañca kammabhavo, ayañca upapattibhavo.":
        "Таким образом, есть и это существование как действие, и это существование как перерождение.",
    "Bhavo duvidhena – atthi kammabhavo, atthi upapattibhavo.":
        f"Классификация существования на два вида {DASH} есть существование как действие, есть существование как перерождение.",
    "Sabbampi bhavagāmikammaṃ kammabhavo.": "И всякое действие, ведущее к существованию, является существованием как действием.",
    "Kāyasañcetanā kāyasaṅkhāro, vacīsañcetanā vacīsaṅkhāro, manosañcetanā cittasaṅkhāro.":
        ("Телесное намерение является телесным формирующим фактором, речевое намерение является речевым формирующим "
         "фактором, умственное намерение является умственным формирующим фактором."),
    "Puññābhisaṅkhāro, apuññābhisaṅkhāro, āneñjābhisaṅkhāro, kāyasaṅkhāro, vacīsaṅkhāro, cittasaṅkhāro.":
        ("Волевое действие, приносящее заслугу, волевое действие, не приносящее заслуги, волевое действие, ведущее к "
         "непоколебимому, телесный формирующий фактор, речевой формирующий фактор, умственный формирующий фактор."),
    "Alobho, adoso, amoho.": "Отсутствие жадности, отсутствие злобы, отсутствие заблуждения.",
    "Alobho, adoso.": "Отсутствие жадности, отсутствие злобы.",
    "Katame dhammā akusalā?": "Что такое неблагие явления?",
    "Katame dhammā kusalā?": "Что такое благие явления?",
    "Katame dhammā abyākatā?": "Что такое этически неопределённые явления?",
    "Tattha katamo alobho…pe… adoso…pe… amoho?":
        "Что такое здесь отсутствие жадности… отсутствие злобы… отсутствие заблуждения?",
}
in_pi1("Что такое неблагие явления?", "Что такое благие явления?", "Что такое этически неопределённые явления?")
PI5_DIR = os.path.join(S.ROOT, r"AI_translation\russian\pi-5-russian-plain-rails_split_chapters")
PI5_ALL = "\n".join(open(os.path.join(PI5_DIR, f), encoding="utf-8").read() for f in sorted(os.listdir(PI5_DIR))
                    if f.endswith(".md"))


def in_pi5(*parts):
    for p in parts:
        assert p in PI5_ALL, "not in pi-5: " + p[:90]


in_pi5("речевой формирующий фактор", "телесный формирующий фактор", "умственный формирующий фактор",
       "волевое действие, приносящее заслугу", "волевое действие, ведущее к непоколебимому",
       "существование из пяти составляющих", "возникновение в зависимости от условий")

# simple terms of the questions / answers: nom, ins
TERM = {
    "puññābhisaṅkhāro": ("волевое действие, приносящее заслугу", "волевым действием, приносящим заслугу"),   # pi-5
    "apuññābhisaṅkhāro": ("волевое действие, не приносящее заслуги", "волевым действием, не приносящим заслуги"),
    "āneñjābhisaṅkhāro": ("волевое действие, ведущее к непоколебимому", "волевым действием, ведущим к непоколебимому"),
    "kāyasaṅkhāro": ("телесный формирующий фактор", "телесным формирующим фактором"),                       # pi-5
    "kammabhavo": ("существование как действие", "существованием как действием"),
    "upapattibhavo": ("существование как перерождение", "существованием как перерождением"),
    "jarā": ("старение", "старением"), "maraṇaṃ": ("смерть", "смертью"),
    "soko": ("печаль", "печалью"), "paridevo": ("стенания", "стенаниями"), "dukkhaṃ": ("боль", "болью"),
    "domanassaṃ": ("уныние", "унынием"), "upāyāso": ("отчаяние", "отчаянием"),
    "kusalamūlā": ("благие корни", "благими корнями"),
    "alobho": ("отсутствие жадности", "отсутствием жадности"), "adoso": ("отсутствие злобы", "отсутствием злобы"),
    "amoho": ("отсутствие заблуждения", "отсутствием заблуждения"),
}
for _k in ("avijjā", "saṅkhāro", "nāmaṃ", "rūpaṃ", "nāmarūpaṃ"):
    TERM[_k] = N[_k][:2]


def term(t, case):
    i = 0 if case == "nom" else 1
    if t in TERM:
        return TERM[t][i]
    return link(t, case)


# ================================================================ 3. definitions (answer bodies): Pāli -> (Russian, comma before the dash)
MOHA_PI1 = T.MOHA                                    # pi-1 ^1-390 (without «в это время»)
assert MOHA_PI1.startswith("незнание, отсутствие видения,")
MOHA_HEAD, MOHA_TAIL = "незнание, отсутствие видения", "засов неведения, заблуждение как неблагой корень"
assert MOHA_PI1.endswith(MOHA_TAIL)
CETANA = "намерение, проявление намерения, состояние намеренности"                 # pi-1 ^1-5
assert CETANA in PI1["^1-5"]
CITTA = T.CITTA_SYN                                                                  # pi-1 ^1-6
PHASSA = "контакт, касание, соприкосновение, состояние соприкосновения"            # pi-1 ^1-2
assert PHASSA in PI1["^1-2"]
RAGA = "страсть, пристрастие, расположенность, потакание, наслаждение, страсть к наслаждению, пристрастие ума"
in_pi1(RAGA)                                                                         # pi-1 lobho (4-01)
DITTHI = edit(edit(PI1["^1-381"], " [вариант чтения (Sī., Syā.): paṭiggāho]", ""),
              " [вариант написания (Ka.): vipariyesagāho]", "")
DITTHI = DITTHI[DITTHI.index("воззрение, приверженность"):DITTHI.index(", – это ложное")]
assert DITTHI.endswith("сфера сектантских учений, превратная хватка")
DOSA_HEAD, DOSA_TAIL = "досада ума", "свирепость, грубость, недовольство ума"       # pi-1 ^1-1066
assert DOSA_HEAD in PI1["^1-1066"] and DOSA_TAIL in PI1["^1-1066"]
VICI = PI1_ALL[PI1_ALL.index("То, что в это время есть сомнение, "):]
VICI = VICI[len("То, что в это время есть "):VICI.index(", – это колебание в это время")]
assert VICI.endswith("оцепенелость ума, терзание ума")                             # pi-1 vicikicchā (2-04)
UDDH = "беспокойство ума, отсутствие затихания, отвлечение ума, взбудораженность ума"
in_pi1("есть " + UDDH + ", – это беспокойство")
ALOBHA = T.pi1_body("^1-32", ", – это отсутствие")[len("То, что в это время есть "):]
ADOSA = T.pi1_body("^1-33", ", – это отсутствие")[len("То, что в это время есть "):]
ADOSA = edit(ADOSA, " [вариант чтения (Syā.): adūsanā adūsitattaṃ]", "")
AMOHA_HEAD = "мудрость, понимание"
AMOHA_TAIL = "отсутствие заблуждения, исследование явлений, правильное воззрение"
assert AMOHA_TAIL in PI1["^1-34"]
SADDHA = "вера, доверие, уверенность, глубокая убеждённость"                       # pi-1 / ch. 5
in_pi1(SADDHA)
ADHIMOKKHA = "решимость ума, проявление решимости, состояние решимости в отношении этого"   # new
FEEL = T.FEEL
TO = "То, что есть "
TO_D = "То, что у тех или иных явлений есть "
JATI_D = TO_D + "рождение, зарождение, образование, появление, проявление"
JARA_D = TO_D + "старение, одряхление, сокращение срока жизни"
MARANA_D = TO_D + "уничтожение, угасание, распад, полный распад, непостоянство, исчезновение"   # pi-1 ^1-644 words
in_pi1("уничтожение, угасание, распад, полный распад, непостоянство, исчезновение")
AGG3 = "Совокупность чувств, совокупность восприятия, совокупность формирующих факторов"
AGG4 = "совокупность чувств, совокупность восприятия, совокупность формирующих факторов, совокупность сознания"
UPACAYA = ("Рост сферы глаза, рост сферы уха, рост сферы носа, рост сферы языка, рост сферы тела, или же какая бы "
           "другая материальная форма ни была рождённой умом, имеющей причиной ум, порождённой умом")
in_pi1("рост материальной формы", "или же какая бы другая материальная форма ни была рождённой умом, имеющей причиной ум, порождённой умом")
NISSAYA = "Материальная форма, в зависимости от которой действует элемент умственного сознания"
NISSAYA4 = ("И четыре великих элемента, и та материальная форма, в зависимости от которой действует элемент "
            "умственного сознания")
VAR_CETAYI = " [вариант чтения (Sī., Ka.): cetayitattaṃ]"
VAR_VIPARIYESA = " [вариант написания (во многих изданиях): vipariyesaggāho]"       # pi-1 «(во многих изданиях)»
in_pi1("(во многих изданиях)")
TAJJA = {"manoviññāṇa": "умственного сознания", "cakkhuviññāṇa": "зрительного сознания",
         "kāyaviññāṇa": "осязательного сознания"}


def tajja(k):
    return "соответствующий элемент ума" if k == "mano" else f"соответствующий элемент {TAJJA[k]}"


BODY = {
    # --- Suttantabhājanīya
    "Dukkhe aññāṇaṃ, dukkhasamudaye aññāṇaṃ, dukkhanirodhe aññāṇaṃ, dukkhanirodhagāminiyā paṭipadāya aññāṇaṃ":
        ("Незнание страдания, незнание возникновения страдания, незнание прекращения страдания, незнание способа "
         "практики, ведущего к прекращению страдания", True),
    "Kusalā cetanā kāmāvacarā rūpāvacarā dānamayā sīlamayā bhāvanāmayā":
        ("Благое намерение, относящееся к миру чувственных желаний, относящееся к миру форм, основанное на даянии, "
         "основанное на нравственности, основанное на развитии ума", True),
    "Akusalā cetanā kāmāvacarā": ("Неблагое намерение, относящееся к миру чувственных желаний", True),
    "Kusalā cetanā arūpāvacarā": ("Благое намерение, относящееся к миру без форм", True),
    "Cakkhuviññāṇaṃ, sotaviññāṇaṃ, ghānaviññāṇaṃ, jivhāviññāṇaṃ, kāyaviññāṇaṃ, manoviññāṇaṃ":
        ("Зрительное сознание, слуховое сознание, обонятельное сознание, вкусовое сознание, осязательное сознание, "
         "умственное сознание", False),
    "Vedanākkhandho, saññākkhandho, saṅkhārakkhandho": (AGG3, False),
    "Cattāro mahābhūtā, catunnañca mahābhūtānaṃ upādāya rūpaṃ":
        ("Четыре великих элемента и материальная форма, производная от четырёх великих элементов", True),
    "Cakkhāyatanaṃ, sotāyatanaṃ, ghānāyatanaṃ, jivhāyatanaṃ, kāyāyatanaṃ, manāyatanaṃ":
        ("Сфера глаза, сфера уха, сфера носа, сфера языка, сфера тела, сфера ума", False),
    "Cakkhusamphasso sotasamphasso ghānasamphasso jivhāsamphasso kāyasamphasso manosamphasso":
        ("Контакт глаза, контакт уха, контакт носа, контакт языка, контакт тела, контакт ума", False),
    "Cakkhusamphassajā vedanā, sotasamphassajā vedanā, ghānasamphassajā vedanā, jivhāsamphassajā vedanā, "
    "kāyasamphassajā vedanā, manosamphassajā vedanā":
        (cap(", ".join(f"рождённое контактом {d} чувство" for d in S.SIX_DOORS)), False),
    "Rūpataṇhā, saddataṇhā, gandhataṇhā, rasataṇhā, phoṭṭhabbataṇhā, dhammataṇhā":
        ("Жажда видимых форм, жажда звуков, жажда запахов, жажда вкусов, жажда осязаемого, жажда объектов ума", False),
    "Kāmupādānaṃ, diṭṭhupādānaṃ, sīlabbatupādānaṃ, attavādupādānaṃ":
        ("Цепляние за чувственные удовольствия, цепляние за воззрения, цепляние за обряды и обеты, цепляние за учение "
         "о самости", False),
    "Puññābhisaṅkhāro, apuññābhisaṅkhāro, āneñjābhisaṅkhāro":
        ("Волевое действие, приносящее заслугу, волевое действие, не приносящее заслуги, волевое действие, ведущее к "
         "непоколебимому", True),
    "Kāmabhavo, rūpabhavo, arūpabhavo, saññābhavo, asaññābhavo, nevasaññānāsaññābhavo, ekavokārabhavo, "
    "catuvokārabhavo, pañcavokārabhavo":
        ("Существование в мире чувственных желаний, существование в мире форм, существование в мире без форм, "
         "существование с восприятием, существование без восприятия, существование ни с восприятием, ни без "
         "восприятия, существование из одной составляющей, существование из четырёх составляющих, существование из "
         "пяти составляющих", False),
    "Yā tesaṃ tesaṃ sattānaṃ tamhi tamhi sattanikāye jāti sañjāti okkanti abhinibbatti, khandhānaṃ pātubhāvo, "
    "āyatanānaṃ paṭilābho": (F.JATI_L, True),
    "Yā tesaṃ tesaṃ sattānaṃ tamhi tamhi sattanikāye jarā jīraṇatā khaṇḍiccaṃ pāliccaṃ valittacatā āyuno saṃhāni "
    "indriyānaṃ paripāko": (F.JARA_L, True),
    "Yā tesaṃ tesaṃ sattānaṃ tamhā tamhā sattanikāyā cuti cavanatā bhedo antaradhānaṃ maccu maraṇaṃ kālakiriyā "
    "[kālaṃkiriyā (ka.)] khandhānaṃ bhedo kaḷevarassa nikkhepo jīvitindriyassupacchedo":
        (edit(F.MARANA_L, "кончина,", "кончина [вариант написания (Ka.): kālaṃkiriyā],"), True),
    "Ñātibyasanena vā phuṭṭhassa, bhogabyasanena vā phuṭṭhassa, rogabyasanena vā phuṭṭhassa, sīlabyasanena vā "
    "phuṭṭhassa, diṭṭhibyasanena vā phuṭṭhassa, aññataraññatarena byasanena samannāgatassa, aññataraññatarena "
    "dukkhadhammena phuṭṭhassa soko socanā socitattaṃ antosoko antoparisoko cetaso parijjhāyanā domanassaṃ sokasallaṃ":
        (F.SOKA_L, True),
    "Ñātibyasanena vā phuṭṭhassa, bhogabyasanena vā phuṭṭhassa, rogabyasanena vā phuṭṭhassa, sīlabyasanena vā "
    "phuṭṭhassa, diṭṭhibyasanena vā phuṭṭhassa, aññataraññatarena byasanena samannāgatassa, aññataraññatarena "
    "dukkhadhammena phuṭṭhassa ādevo paridevo ādevanā paridevanā ādevitattaṃ paridevitattaṃ vācā palāpo vippalāpo "
    "lālappo lālappanā lālappitattaṃ":
        (edit(F.PARIDEVA_L, " [вариант написания (Syā.): lālapo lālapanā lālapitattaṃ]", ""), True),
    "Yaṃ kāyikaṃ asātaṃ kāyikaṃ dukkhaṃ kāyasamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ kāyasamphassajā asātā dukkhā vedanā":
        (TO + FEEL["dukkha"], True),
    "Yaṃ cetasikaṃ asātaṃ, cetasikaṃ dukkhaṃ, cetosamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ, cetosamphassajā asātā dukkhā vedanā":
        (TO + FEEL["domanassa"], True),
    "Ñātibyasanena vā phuṭṭhassa, bhogabyasanena vā phuṭṭhassa, rogabyasanena vā phuṭṭhassa, sīlabyasanena vā "
    "phuṭṭhassa, diṭṭhibyasanena vā phuṭṭhassa, aññataraññatarena byasanena samannāgatassa, aññataraññatarena "
    "dukkhadhammena phuṭṭhassa āyāso upāyāso āyāsitattaṃ upāyāsitattaṃ": (F.UPAYASA_L, True),
    # --- Abhidhammabhājanīya
    "Yaṃ aññāṇaṃ adassanaṃ…pe… avijjālaṅgī moho akusalamūlaṃ": (f"{TO}{MOHA_HEAD}… {MOHA_TAIL}", True),
    "Yā cetanā sañcetanā sañcetayitattaṃ [cetayitattaṃ (sī. ka.)]": (TO + CETANA + VAR_CETAYI, True),
    "Yā cetanā sañcetanā sañcetayitattaṃ": (TO + CETANA, True),
    "Yaṃ cittaṃ mano mānasaṃ hadayaṃ paṇḍaraṃ mano manāyatanaṃ manindriyaṃ viññāṇaṃ viññāṇakkhandho "
    "tajjāmanoviññāṇadhātu": (f"{TO}{CITTA}, {tajja('manoviññāṇa')}", True),
    "Ṭhapetvā upādānaṃ, vedanākkhandho saññākkhandho saṅkhārakkhandho viññāṇakkhandho": ("Кроме цепляния, " + AGG4, False),
    "Ṭhapetvā phassaṃ, vedanākkhandho saññākkhandho saṅkhārakkhandho viññāṇakkhandho": ("Кроме контакта, " + AGG4, False),
    "Ṭhapetvā adhimokkhaṃ, vedanākkhandho saññākkhandho saṅkhārakkhandho viññāṇakkhandho": ("Кроме решимости, " + AGG4, False),
    "Ṭhapetvā adhimokkhaṃ, vedanākkhandho saññākkhandho saṅkhārakkhandho, viññāṇakkhandho": ("Кроме решимости, " + AGG4, False),
    "Ṭhapetvā vicikicchaṃ, vedanākkhandho saññākkhandho saṅkhārakkhandho viññāṇakkhandho": ("Кроме колебания, " + AGG4, False),
    "Ṭhapetvā vedanaṃ, saññākkhandho saṅkhārakkhandho viññāṇakkhandho":
        ("Кроме чувства, совокупность восприятия, совокупность формирующих факторов, совокупность сознания", False),
    "Vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho": (cap(AGG4), False),
    "Yo phasso phusanā samphusanā samphusitattaṃ": (TO + PHASSA, True),
    "Yaṃ cetasikaṃ sātaṃ cetasikaṃ sukhaṃ cetosamphassajaṃ sātaṃ sukhaṃ vedayitaṃ cetosamphassajā sātā sukhā vedanā":
        (TO + FEEL["somanassa"], True),
    "Yaṃ cetasikaṃ asātaṃ cetasikaṃ dukkhaṃ cetosamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ cetosamphassajā asātā dukkhā vedanā":
        (TO + FEEL["domanassa"], True),
    "Yaṃ cetasikaṃ neva sātaṃ nāsātaṃ cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ cetosamphassajā adukkhamasukhā vedanā":
        (TO + FEEL["upekkhā"], True),
    "Yaṃ cetasikaṃ neva sātaṃ nāsātaṃ cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ, cetosamphassajā adukkhamasukhā vedanā":
        (TO + FEEL["upekkhā"], True),
    "Yaṃ kāyikaṃ sātaṃ kāyikaṃ sukhaṃ kāyasamphassajaṃ sātaṃ sukhaṃ vedayitaṃ kāyasamphassajā sātā sukhā vedanā":
        (TO + FEEL["sukha"], True),
    "Yo rāgo sārāgo anunayo anurodho nandī nandirāgo cittassa sārāgo": (TO + RAGA, True),
    "Yo rāgo sārāgo…pe… cittassa sārāgo": (TO + "страсть, пристрастие… пристрастие ума", True),
    "Yo rāgo…pe… cittassa sārāgo": (TO + "страсть… пристрастие ума", True),
    "Yā diṭṭhi diṭṭhigataṃ diṭṭhigahanaṃ diṭṭhikantāro diṭṭhivisūkāyikaṃ diṭṭhivipphanditaṃ diṭṭhisaṃyojanaṃ gāho "
    "patiṭṭhāho abhiniveso parāmāso kummaggo micchāpatho micchattaṃ titthāyatanaṃ vipariyāsaggāho "
    "[vipariyesaggāho (bahūsu)]": (TO + DITTHI + VAR_VIPARIYESA, True),
    "Yā diṭṭhi diṭṭhigataṃ…pe… titthāyatanaṃ vipariyāsaggāho":
        (TO + "воззрение, приверженность воззрениям… сфера сектантских учений, превратная хватка", True),
    "Yā tesaṃ tesaṃ dhammānaṃ jāti sañjāti nibbatti abhinibbatti pātubhāvo": (JATI_D, True),
    "Yā tesaṃ tesaṃ dhammānaṃ jarā jīraṇatā āyuno saṃhāni": (JARA_D, True),
    "Yo tesaṃ tesaṃ dhammānaṃ khayo vayo bhedo paribhedo aniccatā antaradhānaṃ": (MARANA_D, True),
    "Cakkhāyatanassa upacayo, sotāyatanassa upacayo, ghānāyatanassa upacayo, jivhāyatanassa upacayo, "
    "kāyāyatanassa upacayo, yaṃ vā panaññampi atthi rūpaṃ cittajaṃ cittahetukaṃ cittasamuṭṭhānaṃ": (UPACAYA, True),
    "Yaṃ rūpaṃ nissāya manoviññāṇadhātu vattati": (NISSAYA, True),
    "Cattāro ca mahābhūtā, yañca rūpaṃ nissāya manoviññāṇadhātu vattati": (NISSAYA4, True),
    "Yo cittassa adhimokkho adhimuccanā tadadhimuttatā": (TO + ADHIMOKKHA, True),
    "Yo cittassa āghāto…pe… caṇḍikkaṃ asuropo [asulopo (syā.)] anattamanatā cittassa":
        (f"{TO}{DOSA_HEAD}… {edit(DOSA_TAIL, 'грубость,', 'грубость [вариант написания (Syā.): asulopo],')}", True),
    "Yā kaṅkhā kaṅkhāyanā kaṅkhāyitattaṃ vimati vicikicchā dveḷhakaṃ dvidhāpatho [dvedhāpatho (sī. syā.)] saṃsayo "
    "anekaṃsaggāho āsappanā parisappanā apariyogāhaṇā [apariyogāhanā (sī. syā. ka.)] chambhitattaṃ cittassa manovilekho":
        (TO + edit(edit(VICI, "распутье,", "распутье [вариант написания (Sī., Syā.): dvedhāpatho],"),
                   "отсутствие углубления,", "отсутствие углубления [вариант написания (Sī., Syā., Ka.): apariyogāhanā],"),
         True),
    "Yaṃ cittassa uddhaccaṃ avūpasamo cetaso vikkhepo bhantattaṃ cittassa": (TO + UDDH, True),
    "Yo alobho alubbhanā alubbhitattaṃ asārāgo asārajjanā asārajjitattaṃ anabhijjhā alobho kusalamūlaṃ": (TO + ALOBHA, True),
    "Yo adoso adussanā adussitattaṃ abyāpādo abyāpajjo adoso kusalamūlaṃ": (TO + ADOSA, True),
    "Yā paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi": (f"{TO}{AMOHA_HEAD}… {AMOHA_TAIL}", True),
    "Yā paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi dhammavicayasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ":
        (F.FACTOR_BODY["Yā paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi dhammavicayasambojjhaṅgo maggaṅgaṃ "
                       "maggapariyāpannaṃ"], True),
    "Yā saddhā saddahanā okappanā abhippasādo": (TO + SADDHA, True),
    "Alobho, adoso, amoho": ("Отсутствие жадности, отсутствие злобы, отсутствие заблуждения", False),
    "Alobho, adoso": ("Отсутствие жадности, отсутствие злобы", False),
}
for _k, _v in (("mano", "manodhātu"), ("manoviññāṇa", "manoviññāṇadhātu"), ("cakkhuviññāṇa", "cakkhuviññāṇadhātu"),
               ("kāyaviññāṇa", "kāyaviññāṇadhātu")):
    BODY[f"Yaṃ cittaṃ mano mānasaṃ…pe… tajjā{_v}"] = (f"{TO}{T.CITTA_SHORT}… {tajja(_k)}", True)
assert ALOBHA.startswith("отсутствие жадности,") and ADOSA.startswith("отсутствие злобы,")
in_pi1(VICI, FEEL["upekkhā"], "соответствующий элемент зрительного сознания",
       "соответствующий элемент осязательного сознания", "соответствующий элемент ума")
in_pi1("Цепляние за чувственные удовольствия, цепляние за воззрения, цепляние за обряды и обеты, цепляние за учение о самости".lower()[:40])
in_pi1("жажда видимых форм, жажда звуков, жажда запахов, жажда вкусов, жажда осязаемого, жажда объектов ума")
in_pi1("Четыре великих элемента и материальная форма, производная от четырёх великих элементов, – это")
in_pi1("контакт глаза", "рождённое контактом глаза чувство", "незнание способа практики, ведущего к прекращению страдания")

# ================================================================ 4. mind-type openings (Yasmiṃ samaye … , tasmiṃ samaye)
G2 = {"m": 0, "n": 1}
SAHA = {"somanassa": "радостью", "upekkhā": "невозмутимостью", "domanassa": "унынием", "sukha": "удовольствием",
        "dukkha": "болью"}
SAMP = {"diṭṭhigata": "с приверженностью воззрениям", "paṭigha": "с неприязнью", "vicikicchā": "с колебанием",
        "uddhacca": "с беспокойством", "ñāṇa": "со знанием"}
OBJ = {"rūp": "видимую форму", "sadd": "звук", "gandh": "запах", "ras": "вкус", "phoṭṭhabb": "осязаемое",
       "dhamm": "объект ума"}
A = r"(?:aṃ|ā)"
FULL6 = "".join(f"{s}ārammaṇ{A} vā " for s in ("rūp", "sadd", "gandh", "ras", "phoṭṭhabb", "dhamm")) + "yaṃ yaṃ vā panārabbha"
FULL5 = "".join(f"{s}ārammaṇ{A} vā " for s in ("rūp", "sadd", "gandh", "ras", "phoṭṭhabb")) + "yaṃ yaṃ vā panārabbha"
VIP_K = ("вследствие совершённого и накопленного благого действия, относящегося к миру чувственных желаний,", " ")
VIP_A = ("вследствие совершённого и накопленного неблагого действия", " ")
KIRIYA = "функциональный, ни благой, ни неблагой и не являющийся результатом действий"
VINN = {"cakkhu": "зрительное", "sota": "слуховое", "ghāna": "обонятельное", "jivhā": "вкусовое", "kāya": "осязательное"}


def _has(g, m, f):
    return "имеющий объектом " if g == "m" else "имеющее объектом "


TOKENS = [   # (regex, function(match, gender) -> (Russian, new gender or None, joiner to the next token or None))
    (r"kāmāvacarassa kusalassa kammassa katattā upacitattā", lambda m, g: (VIP_K[0], g, VIP_K[1])),
    (r"akusalassa kammassa katattā upacitattā", lambda m, g: (VIP_A[0], g, VIP_A[1])),
    (r"kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti",
     lambda m, g: ("возникает благой ум, относящийся к миру чувственных желаний", "m", None)),
    (r"akusalaṃ cittaṃ uppannaṃ hoti", lambda m, g: ("возникает неблагой ум", "m", None)),
    (r"vipākaṃ (cakkhu|sota|ghāna|jivhā|kāya)viññāṇaṃ uppannaṃ hoti",
     lambda m, g: (f"возникает {VINN[m.group(1)]} сознание, являющееся результатом", "n", None)),
    (r"(cakkhu|sota|ghāna|jivhā|kāya)viññāṇaṃ uppannaṃ hoti",
     lambda m, g: (f"возникает {VINN[m.group(1)]} сознание", "n", None)),
    (r"vipākā manodhātu uppannā hoti", lambda m, g: ("возникает элемент ума, являющийся результатом", "m", None)),
    (r"vipākā manoviññāṇadhātu uppannā hoti",
     lambda m, g: ("возникает элемент умственного сознания, являющийся результатом", "m", None)),
    (r"manodhātu uppannā hoti kiriyā neva kusalā nākusalā na ca kammavipākā",
     lambda m, g: (f"возникает элемент ума, {KIRIYA}", "m", None)),
    (r"manoviññāṇadhātu uppannā hoti kiriyā neva kusalā nākusalā na ca kammavipākā",
     lambda m, g: (f"возникает элемент умственного сознания, {KIRIYA}", "m", None)),
    (r"manodhātu uppannā hoti", lambda m, g: ("возникает элемент ума", "m", None)),
    (r"manoviññāṇadhātu uppannā hoti", lambda m, g: ("возникает элемент умственного сознания", "m", None)),
    (r"(somanassa|upekkhā|domanassa|sukha|dukkha)sahagat" + A,
     lambda m, g: (("сопровождаемый ", "сопровождаемое ")[G2[g]] + SAHA[m.group(1)], g, None)),
    (r"(diṭṭhigata|paṭigha|vicikicchā|uddhacca|ñāṇa)(sam|vip)payutt" + A,
     lambda m, g: (("" if m.group(2) == "sam" else "не ") + ("связанный ", "связанное ")[G2[g]] + SAMP[m.group(1)], g, None)),
    (r"sasaṅkhārena", lambda m, g: ("с побуждением", g, None)),
    (FULL6, lambda m, g: (_has(g, 0, 0) + "видимую форму, или звук, или запах, или вкус, или осязаемое, или объект ума, "
                          "или что бы то ни было", g, None)),
    (FULL5, lambda m, g: (_has(g, 0, 0) + "видимую форму, или звук, или запах, или вкус, или осязаемое, "
                          "или что бы то ни было", g, None)),
    (r"rūpārammaṇ" + A + r" vā…pe… (dhamm|phoṭṭhabb)ārammaṇ" + A + r" vā yaṃ yaṃ vā panārabbha",
     lambda m, g: (_has(g, 0, 0) + f"видимую форму… или {OBJ[m.group(1)]}, или что бы то ни было", g, None)),
    (r"rūpārammaṇ" + A + r" vā…pe… (dhamm|phoṭṭhabb)ārammaṇ" + A + r" vā(?=…pe…)",
     lambda m, g: (_has(g, 0, 0) + f"видимую форму… или {OBJ[m.group(1)]}", g, None)),
    (r"rūpārammaṇ" + A + r" vā(?=…pe…)", lambda m, g: (_has(g, 0, 0) + "видимую форму", g, None)),
    (r"(rūp|sadd|gandh|ras|phoṭṭhabb)ārammaṇaṃ", lambda m, g: (_has(g, 0, 0) + OBJ[m.group(1)], g, None)),
]
TOKENS = [(re.compile(p), f) for p, f in TOKENS]


def desc(s):
    """kāma-sphere mind-type descriptions -> «возникает неблагой ум, сопровождаемый радостью, …»."""
    out, g, rest, join = [], "m", s, None
    while rest:
        for rx, fn in TOKENS:
            m = rx.match(rest)
            if m:
                ru, g2, j = fn(m, g)
                if out:
                    out.append(join)
                out.append(ru)
                g = g2 or g
                rest = rest[m.end():]
                break
        else:
            raise KeyError("desc: " + rest[:80])
        if not rest:
            break
        if rest.startswith("…pe… "):
            rest, join = rest[len("…pe… "):], "… "
        elif rest.startswith(" "):
            rest, join = rest[1:], (j if j else ", ")
        else:
            raise KeyError("desc sep: " + rest[:80])
    return "".join(out)


# jhāna / supramundane openings and their results [pi-1 ^1-499, ^1-505, ^1-577, 2-04 and 2-05 lines]
def _between(line, a, b, nth=0):
    i = -1
    for _ in range(nth + 1):
        i = line.index(a, i + 1)
    return line[i:line.index(b, i)]


_R499, _R505, _R577 = PI1["^1-499"], PI1["^1-505"], PI1["^1-577"]
RUPA_K = _between(_R499, "кто-либо развивает путь", ", в это время есть контакт")
RUPA_V = _between(_R499, "Вследствие того же", ", в это время есть контакт")
LOK_K = _between(_R505, "кто-либо развивает надмирское", ", в это время есть контакт")
LOK_V_SUNNA = _between(_R505, "Вследствие того же", ", в это время есть контакт")
LOK_V = edit(LOK_V_SUNNA, ", пустое,", ",")
RUPA_F = _between(_R577, "кто-либо развивает медитативное", ", в это время есть контакт")
ARUPA_K = ("кто-либо развивает путь к рождению в мире без форм и, полностью преодолев сферу отсутствия чего-либо, "
           "в сопровождении восприятия сферы ни восприятия, ни невосприятия, с устранением приятного… входит в "
           "четвёртое медитативное погружение и пребывает в нём")
ARUPA_V = ("Вследствие того же совершённого и накопленного благого действия, относящегося к миру без форм, в качестве "
           "его результата, когда кто-либо, полностью преодолев сферу отсутствия чего-либо, в сопровождении восприятия "
           "сферы ни восприятия, ни невосприятия, с устранением приятного… входит в четвёртое медитативное погружение "
           "и пребывает в нём")
ARUPA_F = ("кто-либо развивает медитативное погружение, относящееся к миру без форм, функциональное, ни благое, ни "
           "неблагое и не являющееся результатом действий, для пребывания в счастье в этой жизни и, полностью преодолев "
           "сферу отсутствия чего-либо, в сопровождении восприятия сферы ни восприятия, ни невосприятия, с устранением "
           "приятного… входит в четвёртое медитативное погружение и пребывает в нём")
in_pi1(ARUPA_K, ARUPA_V, ARUPA_F)
VAR_PATHAVI = " [вариант написания (Sī., Syā.): paṭhavīkasiṇaṃ]"
EARTH = "со всеохватным объектом земли"

P_RUPA = "rūpūpapattiyā maggaṃ bhāveti vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja viharati pathavīkasiṇaṃ"
P_ARUPA = ("arūpūpapattiyā maggaṃ bhāveti sabbaso ākiñcaññāyatanaṃ samatikkamma nevasaññānāsaññāyatanasaññāsahagataṃ "
           "sukhassa ca pahānā…pe… catutthaṃ jhānaṃ upasampajja viharati")
P_LOK = ("lokuttaraṃ jhānaṃ bhāveti niyyānikaṃ apacayagāmiṃ diṭṭhigatānaṃ pahānāya paṭhamāya bhūmiyā pattiyā vivicceva "
         "kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja viharati dukkhapaṭipadaṃ dandhābhiññaṃ")
JHANA = {   # Pāli between "Yasmiṃ samaye " and ", tasmiṃ samaye" -> Russian after «В то время, когда »
    P_RUPA: RUPA_K,
    P_RUPA.replace("pathavīkasiṇaṃ", "pathavīkasiṇaṃ [paṭhavīkasiṇaṃ (sī. syā.)]"): edit(RUPA_K, EARTH, EARTH + VAR_PATHAVI),
    P_ARUPA: ARUPA_K,
    P_LOK: LOK_K,
    "rūpāvacaraṃ jhānaṃ bhāveti kiriyaṃ neva kusalaṃ nākusalaṃ na ca kammavipākaṃ diṭṭhadhammasukhavihāraṃ vivicceva "
    "kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja viharati pathavīkasiṇaṃ": RUPA_F,
    "arūpāvacaraṃ jhānaṃ bhāveti kiriyaṃ neva kusalaṃ nākusalaṃ na ca kammavipākaṃ diṭṭhadhammasukhavihāraṃ " + P_ARUPA[
        len("arūpūpapattiyā maggaṃ bhāveti "):]: ARUPA_F,
}
TASSEVA = {   # Pāli between "Tasseva " and ", tasmiṃ samaye" -> Russian (whole clause)
    "rūpāvacarassa kusalassa kammassa katattā upacitattā vipākaṃ vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja "
    "viharati pathavīkasiṇaṃ": RUPA_V,
    "arūpāvacarassa kusalassa kammassa katattā upacitattā vipākaṃ " + P_ARUPA[len("arūpūpapattiyā maggaṃ bhāveti "):]: ARUPA_V,
    "lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja "
    "viharati dukkhapaṭipadaṃ dandhābhiññaṃ": LOK_V,
    "lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja "
    "viharati dukkhapaṭipadaṃ dandhābhiññaṃ suññataṃ": LOK_V_SUNNA,
}
PHASSA_PE = "phasso hoti…pe… avikkhepo hoti – ime dhammā kusalā"
PHASSA_PE_RU = f"есть контакт… есть отсутствие отвлечения {DASH} это благие явления"
in_pi1("есть контакт… есть отсутствие отвлечения… это благие явления")


def when(d):
    if d in JHANA:
        return "В то время, когда " + JHANA[d]
    return "В то время, когда " + desc(d)


def tasmim(rest):
    if rest == PHASSA_PE:
        return "в это время " + PHASSA_PE_RU
    return "в это время " + chain(rest)


# ================================================================ 5. sentences and lines
FIXES = [   # (Pāli as written, as meant) – punctuation / spelling slips, all reported
    ('ayaṃ vuccati paridevo".', 'ayaṃ vuccati "paridevo".'),                                  # ^2-238 opening quote
    ("saṅkhārahetukaṃ viññāṇapaccayā", "saṅkhārahetukaṃ, viññāṇapaccayā"),                     # ^2-262 comma
    ('"taṇhāpaccayā upādānaṃ taṇhāsampayuttaṃ" …pe…', '"taṇhāpaccayā upādānaṃ taṇhāsampayuttaṃ"…pe…'),   # ^2-265 space
    ("mānasaṃ …pe…", "mānasaṃ…pe…"),                                                           # ^2-269 space
    ("akusamūlaṃ", "akusalamūlaṃ"),                                                            # ^2-277 spelling
    ('ayaṃ vuccati "avijjāpaccayā saṅkhāro.', 'ayaṃ vuccati "avijjāpaccayā saṅkhāro".'),         # ^2-277 closing quote
    ("abhinibbati pātubhāvo", "abhinibbatti pātubhāvo"),                                       # ^2-273 spelling
    ("kāmehi …pe…", "kāmehi…pe…"),                                                             # ^2-340 space
    ('Tena vuccati evametassa', 'Tena vuccati "evametassa'),                                   # ^2-354 opening quote
]
HEAD = {
    "Paccayacatukkaṃ": "Четвёрка условий", "Hetucatukkaṃ": "Четвёрка причин",
    "Sampayuttacatukkaṃ": "Четвёрка связанности", "Aññamaññacatukkaṃ": "Четвёрка взаимной обусловленности",
    "Mātikā": "Матрица",                                                                       # pi-1 Mātikā
    "Akusalaniddeso": "Разъяснение неблагого", "Kusalaniddeso": "Разъяснение благого",          # pi-1 niddeso
    "Abyākataniddeso": "Разъяснение этически неопределённого",
    "Avijjāmūlakakusalaniddeso": "Разъяснение благого на основе неведения",
    "Kusalamūlakavipākaniddeso": "Разъяснение результатов на основе благих корней",
    "Akusalamūlakavipākaniddeso": "Разъяснение результатов на основе неблагих корней",
}
SEC = S.SECTION_TITLES
SPLIT = re.compile(r'(?<=[.?])\s+(?=[A-ZĀĪŪṬḌÑṆṄ])')
Q = re.compile(r"^Tattha katam(?:o|ā|aṃ|e) (.+)\?$")
ANS = re.compile(r'^(.*?)(,?) – (?:ayaṃ|idaṃ|ime) (?:vuccati|vuccanti)( –)? ("?)([^"…]+?)("?)((?:…pe….*)?\.)$')
PE_TAIL = re.compile(r'^…pe… (?:(tena) vuccati "(.+)"ti|(?:ayaṃ|idaṃ) vuccati( –)? "(.+)")\.$')
LEMMA = re.compile(r"^(\S+paccayā(?:pi)? .+?)(nti|ti)\.$")
TAIL_EVAM = {"evametassa kevalassa dukkhakkhandhassa samudayo hotī": EVAM_LOW,
             "evametassa kevalassa dukkhakkhandhassa samudayo hoti": EVAM_LOW,       # ^2-257 short i
             "evametesaṃ dhammānaṃ samudayo hotī": EVAM_D_LOW}


def called(t, quoted=True, dash=False):
    ins = term(t, "ins")
    d = f" {DASH}" if dash else ""
    return f"{S.VUCCATI}{d} «{ins}»" if quoted else f"{S.VUCCATI}{d} {ins}"


def pe_tail(r):
    """the text after the answer term: '.', '…pe….', '…pe… tena vuccati "…"ti.', '…pe… ayaṃ vuccati "X".'"""
    if r == ".":
        return "."
    if r == "…pe….":
        return "…."
    m = PE_TAIL.match(r)
    if not m:
        raise KeyError("tail: " + r)
    if m.group(1):
        return f"… {TENA} «{TAIL_EVAM[m.group(2)]}»."
    return f"… {called(m.group(4), dash=bool(m.group(3)))}."


def answer(s):
    m = ANS.match(s)
    if not m:
        raise KeyError("answer: " + s[:100])
    body, _c, d, q1, t, q2, rest = m.groups()
    assert q1 == q2, s
    if body:
        ru, comma = BODY[body]
        out = f"{ru}{',' if comma else ''} {DASH} {called(t, bool(q1), bool(d))}"
    else:
        raise KeyError("answer without body: " + s[:80])
    return out + pe_tail(rest)


def sentence(s):
    if s in SENT:
        return SENT[s]
    m = Q.match(s)
    if m:
        return f"{S.TATTHA} {term(m.group(1), 'nom')}?"
    m = re.match(r"^(?:Idaṃ|Ayaṃ) vuccati \"(.+)\"\.$|^Ime vuccanti \"(.+)\"\.$", s)
    if m:
        return cap(called(m.group(1) or m.group(2))) + "."
    m = re.match(r"^Yasmiṃ samaye (.+?), tasmiṃ samaye (.+)\.$", s)
    if m:
        return f"{when(m.group(1))}, {tasmim(m.group(2))}."
    m = re.match(r"^Tasseva (.+?), tasmiṃ samaye (.+)\.$", s)
    if m:
        return f"{TASSEVA[m.group(1)]}, {tasmim(m.group(2))}."
    m = re.match(r"^Tasmiṃ samaye (.+)\.$", s)
    if m:
        return f"В это время {chain(m.group(1))}."
    if re.match(r"^(Avijjāpaccayā|Saṅkhārapaccayā avijjā)", s):
        return cap(chain(s[:-1])) + "."
    m = LEMMA.match(s)
    if m:
        lk = m.group(1) + ("ṃ" if m.group(2) == "nti" else "")
        lk = lk[:1].lower() + lk[1:]
        r = link(lk, "chain")
        r = r[2:] if r.startswith("и ") else r   # "Nāmarūpapaccayāpi viññāṇanti" stands alone: no leading «и»
        return f"«{cap(r)}»."
    if " – " in s:
        return answer(s)
    raise KeyError("sentence: " + s[:100])


SPECIAL = {   # whole Pāli lines that do not split into the usual sentences
    'Tattha katamā avijjā…pe… tena vuccati "evametassa kevalassa dukkhakkhandhassa samudayo hotī"ti.':
        f"{S.TATTHA} {N['avijjā'][0]}… {TENA} «{EVAM_LOW}».",
}


def special_349(t):
    """Tattha katamaṃ saṅkhārapaccayā viññāṇaṃ…pe… viññāṇapaccayā nāmaṃ…pe… … ayaṃ vuccati "phassapaccayā vedanā"."""
    m = re.match(r'^Tattha katamaṃ (.+)…pe… ayaṃ vuccati "(.+)"\.$', t)
    if not m or "?" in t:
        return None
    links = m.group(1).split("…pe… ")
    return f"{S.TATTHA} " + "… ".join(link(x, "nom") for x in links) + f"… {called(m.group(2))}."


def line(t):
    for a, b in FIXES:
        if a in t:
            t = t.replace(a, b)
    if t in SPECIAL:
        return SPECIAL[t]
    r = special_349(t)
    if r:
        return r
    # pi-2 ^2-286: "…pe… ayaṃ vuccati "X"." directly after an answer is handled by pe_tail
    sents = SPLIT.split(t)
    return " ".join(sentence(s) for s in sents)


def build_ch6(pali):
    out = []
    for t in pali:
        if t == "### Paṭiccasamuppādavibhaṅgo":
            out.append("### " + S.CHAPTER_TITLES[6])
        elif t.startswith("#### "):
            SUTTA["on"] = t[5:] == "Suttantabhājanīyaṃ"
            out.append("#### " + SEC[t[5:]])
        elif t.startswith("##### "):
            out.append("##### " + HEAD[t[6:]])
        elif t.rstrip(".") in HEAD and t.endswith("."):
            out.append(HEAD[t[:-1]] + ".")
        elif t.rstrip(".") in SEC and t.endswith("."):
            out.append(SEC[t[:-1]] + ".")
        elif t == "Paṭiccasamuppādavibhaṅgo [paccayākāravibhaṅgo (sī. syā.)] niṭṭhito.":
            out.append(S.CHAPTER_TITLES[6] + " [вариант чтения (Sī., Syā.): paccayākāravibhaṅgo] завершён.")
        else:
            out.append(line(t))
    return out


def main():
    # the Suttanta chain must equal pi-1 ^1-1343 word for word (its ';' is a '.' in pi-2)
    SUTTA["on"] = True
    p = ("Avijjāpaccayā saṅkhārā, saṅkhārapaccayā viññāṇaṃ, viññāṇapaccayā nāmarūpaṃ, nāmarūpapaccayā saḷāyatanaṃ, "
         "saḷāyatanapaccayā phasso, phassapaccayā vedanā, vedanāpaccayā taṇhā, taṇhāpaccayā upādānaṃ, upādānapaccayā "
         "bhavo, bhavapaccayā jāti, " + GRIEF_LINK)
    assert "«" + cap(chain(p)) + "; " + EVAM_LOW + "»" in PI1["^1-1343"], cap(chain(p))
    SUTTA["on"] = False
    # mind-type openings identical to pi-1 (^1-365, ^1-1, ^1-431, ^1-455)
    for d in ("akusalaṃ cittaṃ uppannaṃ hoti somanassasahagataṃ diṭṭhigatasampayuttaṃ " + FULL6.replace(A, "aṃ"),
              "kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti somanassasahagataṃ ñāṇasampayuttaṃ " + FULL6.replace(A, "aṃ"),
              "kāmāvacarassa kusalassa kammassa katattā upacitattā vipākaṃ cakkhuviññāṇaṃ uppannaṃ hoti "
              "upekkhāsahagataṃ rūpārammaṇaṃ",
              "kāmāvacarassa kusalassa kammassa katattā upacitattā vipākā manodhātu uppannā hoti upekkhāsahagatā "
              "rūpārammaṇā vā…pe… phoṭṭhabbārammaṇā vā yaṃ yaṃ vā panārabbha"):
        assert "В то время, когда " + desc(d) + ", в это время есть" in PI1_ALL, desc(d)
    pali = open(os.path.join(S.PALI_DIR, FN), encoding="utf-8").read().rstrip("\n").split("\n")
    nonempty = [S.ID.sub("", l).rstrip() for l in pali if l.strip()]
    ru = build_ch6(nonempty)
    assert len(ru) == len(nonempty), (len(ru), len(nonempty))
    for pl, r in zip(nonempty, ru):
        assert pl.count(DASH) + pl.count("—") == r.count(DASH), ("dash count", pl[:70], r[:70])
        assert "—" not in r and "\x01" not in r, r[:80]
        assert pl.startswith("#") == r.startswith("#")
    lines = S.attach_ids(pali, ru)
    S.write(os.path.join(S.RU_DIR, FN), lines)
    print("OK:", FN, "|", len(ru), "non-empty lines")


if __name__ == "__main__":
    main()
