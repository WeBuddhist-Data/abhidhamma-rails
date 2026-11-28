"""Russian plain zero-shot of pi-6 (Yamaka), chapter 8-cittayamaka.md.

Frame-setter for family D (cittayamaka: puggalavāra, dhammavāra, puggaladhammavāra, the time
sections, uppajjamāna / nirujjhamāna, uppanna / niruddha, suttanta / abhidhamma mixtures).

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_8_ru.py
Import: sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-ru")
        import importlib; C = importlib.import_module("build_8_ru")   (importing never writes)

Imports build_7-01_ru (C7) for the general person shape: Q_PERSON, KHA_PREFIX, NO, NATTHI, RES,
NO_CA_FRAME; and build_7-02_ru NO_CA_POS_FRAME (coordinator "Negatives", 2026-11-27).

Exposed frames (all listed in notes-8.md):
  CITTA, VERB, COP, COPULA, SUBST, BUT, NO_CA_FRAME / NO_CA_NEG_FRAME (from 7-01), NO_CA_X,
  CEVA_CA / CEVA_CA_COP, NA_CEVA_NA_CA / NA_CEVA_NA_CA_COP, PERSON_Q / KHA_PREFIX (from 7-01), kha(),
  DHAMMA_Q, PD_Q, BARE_Q, ATK_STAGE / ATK_PART / ATK_PART_NEG / ATK_P2, ATK_ANSWERS, WHO, WHO_TESAM,
  DSUBJ, BARE_TIME, SHORT, CITTA_NP, ETENA_UPAYENA, FIXED; functions P(), no_ca(), clause(), sentence(),
  answer(), question(), mixture(), tr(), translate_file().
"""
import pathlib
import re
import sys
import unicodedata

HERE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru")
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import build_sample_ru as B  # noqa: E402
import importlib  # noqa: E402

C7 = importlib.import_module("build_7-01_ru")   # general person question shape, answers (7-01, coordinator)

CHAPTER = "8-cittayamaka.md"

# ---------------------------------------------------------------------------------------------
# Predicates (subject «ум», masc.). Index 0 = singular, 1 = plural.
# ---------------------------------------------------------------------------------------------
CITTA = "ум"                                   # citta (pi-1 … pi-5)
VERB = {
    "uppajjati": ("возникает", "возникают"),
    "nirujjhati": ("прекращается", "прекращаются"),
    "uppajjittha": ("возникал", "возникали"),          # past: "has (ever) arisen"
    "nirujjhittha": ("прекращался", "прекращались"),
    "uppajjissati": ("возникнет", "возникнут"),
    "nirujjhissati": ("прекратится", "прекратятся"),
}
COPULA = ("является", "являются")
COP = {                                        # predicate participles: «является возникшим»
    "uppannaṃ": ("возникшим", "возникшими"),
    "uppajjamānaṃ": ("возникающим", "возникающими"),
    "nirujjhamānaṃ": ("прекращающимся", "прекращающимися"),
    "niruddhaṃ": ("прекратившимся", "прекратившимися"),
}
SUBST = {                                      # bare questions (12) (13): subject, negated subject
    "uppannaṃ": ("возникшее", "невозникшее"),
    "uppajjamānaṃ": ("возникающее", "невозникающее"),
    "nirujjhamānaṃ": ("прекращающееся", "непрекращающееся"),
    "niruddhaṃ": ("прекратившееся", "непрекратившееся"),
}
BUT = ", но "          # "uppajjati na nirujjhati" = «возникает, но не прекращается»
# "P1, no ca X P2" = «P1, но X не P2» (7-01); "P1, no ca X na P2" = «P1, но X P2» (coordinator "Negatives",
# 7-02 NO_CA_POS_FRAME; never «но не так, что»)
NO_CA_FRAME = C7.NO_CA_FRAME                                            # ", но {res} {neg_pred}"
NO_CA_POS_FRAME = importlib.import_module("build_7-02_ru").NO_CA_POS_FRAME   # ", но {res} {pos_pred}"
CEVA_CA = "и {a}, и {b}"                       # "A ceva B ca"
CEVA_CA_COP = "{cop} и {a}, и {b}"             # both participles: «является и возникшим, и возникающим»
NA_CEVA_NA_CA = "{a} и {b}"                    # "na ceva A na ca B" = «не A и не B»
NA_CEVA_NA_CA_COP = "не {cop} ни {a}, ни {b}"  # both participles: «не является ни …, ни …»

# ---------------------------------------------------------------------------------------------
# Question frames. s = "<subject NP> <predicate>", e.g. «ум возникает».
# ---------------------------------------------------------------------------------------------
KHA_PREFIX = C7.KHA_PREFIX                     # "vā pana" = «А …» (7-01)
PERSON_Q = C7.Q_PERSON                         # yassa … tassa … = «У кого {p1}, у того {p2}?» (7-01)
DHAMMA_Q = "Какой {p1}, тот {p2}?"             # yaṃ cittaṃ P1 taṃ cittaṃ P2?
PD_Q = "У кого какой {p1}, у того тот {p2}?"   # yassa yaṃ cittaṃ P1 tassa taṃ cittaṃ P2? (cf. 7-01 «У кого где …»)
PERSON_KA, PERSON_KHA = PERSON_Q.split(" {")[0], KHA_PREFIX + PERSON_Q.split(" {")[0].lower()   # «У кого», «А у кого»


def kha(q, vp):
    """prefix «А » for vā pana (first letter lowered), as 7-01."""
    return KHA_PREFIX + q[0].lower() + q[1:] if vp else q
BARE_Q = "{subj} {pred}?"                      # uppannaṃ uppajjamānaṃ? = «Возникшее является возникающим?»
# (11) "yassa cittaṃ P1 no ca tassa cittaṃ P2, tassa cittaṃ P3?": s1 = «ум P1, но <P2 negated>»
# (14) Atikkantakālavāro ("uppajjamānaṃ khaṇaṃ" = uppādakkhaṇaṃ, aṭṭhakathā):
ATK_STAGE = {"uppajjamānaṃ": "возникновения", "nirujjhamānaṃ": "прекращения"}
ATK_PART = "миновал момент {stage}, миновал этот момент и его время прошло"
ATK_PART_NEG = "не миновал момент {stage}, не миновал этот момент и его время не прошло"
ATK_P2 = CITTA + " таков"      # "… tassa cittaṃ?" = «…, у того ум таков?»; dhamma «…, тот ум таков?»

# ---------------------------------------------------------------------------------------------
# Answers
# ---------------------------------------------------------------------------------------------
SHORT = {
    "Āmantā.": B.AMANTA,            # Да.
    "No.": C7.NO,                   # Нет. (7-01)
    "Natthi.": C7.NATTHI,           # Такого нет. (7-01)
    "Uppajjittha.": "Возникал.",
    "Nirujjhittha.": "Прекращался.",
    "Uppajjissati.": "Возникнет.",
    "Nirujjhissati.": "Прекратится.",
    "Nirujjhati.": "Прекращается.",
    "Uppannaṃ.": "Является возникшим.",
}
NIRODHA_ASANNA = "у вошедших в медитативное достижение прекращения, у существ без восприятия"
# Person answers: "<who> tesaṃ cittaṃ …". (Russian, add «у них»): «у них» renders tesaṃ when no
# person phrase precedes; after a person phrase tesaṃ merges into it («У остальных … ум …»).
WHO = {
    "Pacchimacittassa uppādakkhaṇe": ("В момент возникновения последнего ума", True),
    "Pacchimacittassa bhaṅgakkhaṇe": ("В момент распада последнего ума", True),
    "Itaresaṃ cittassa uppādakkhaṇe": ("У остальных в момент возникновения ума", False),
    "Itaresaṃ cittassa bhaṅgakkhaṇe": ("У остальных в момент распада ума", False),
    "Cittassa uppādakkhaṇe": ("В момент возникновения ума", True),
    "Cittassa bhaṅgakkhaṇe": ("В момент распада ума", True),
    "Nirodhasamāpannānaṃ asaññasattānaṃ": (B.cap(NIRODHA_ASANNA), False),
    "Cittassa bhaṅgakkhaṇe nirodhasamāpannānaṃ asaññasattānaṃ": ("В момент распада ума, " + NIRODHA_ASANNA, False),
    "Cittassa uppādakkhaṇe nirodhasamāpannānaṃ asaññasattānaṃ": ("В момент возникновения ума, " + NIRODHA_ASANNA, False),
    "Pacchimacittasamaṅgīnaṃ": ("У обладающих последним умом", False),
    "Itaresaṃ": ("У остальных", False),
    "Itaresaṃ cittasamaṅgīnaṃ": ("У остальных обладающих умом", False),
    "Cittasamaṅgīnaṃ": ("У обладающих умом", False),
}
WHO_TESAM = "у них"
NO_CA_X = {                     # the subject repeated after "no ca" (longest first); RES from 7-01
    "tassa taṃ cittaṃ ": C7.RES["tassa"] + " этот " + CITTA,    # «у него этот ум» (puggaladhammavāra)
    "tassa cittaṃ ": C7.RES["tassa"] + " " + CITTA,             # «у него ум» ((11) questions)
    "tesaṃ cittaṃ ": C7.RES["tesaṃ"] + " " + CITTA,             # «у них ум» (puggalavāra)
    "taṃ cittaṃ ": "этот " + CITTA,                             # «этот ум» (dhammavāra)
}
# Dhamma answers: "<subj> cittaṃ …" -> (Russian subject, number)
DSUBJ = {
    "Bhaṅgakkhaṇe": ("Ум в момент распада", 0),
    "Uppādakkhaṇe": ("Ум в момент возникновения", 0),
    "Atītānāgataṃ": ("Прошлый и будущий ум", 0),
    "Atītaṃ": ("Прошлый ум", 0),
    "Anāgataṃ": ("Будущий ум", 0),
    "Paccuppannaṃ": ("Настоящий ум", 0),
    "Bhaṅgakkhaṇe anāgatañca": ("Ум в момент распада и будущий ум", 1),
    "Bhaṅgakkhaṇe atītañca": ("Ум в момент распада и прошлый ум", 1),
    "Uppādakkhaṇe anāgatañca": ("Ум в момент возникновения и будущий ум", 1),
}
BARE_TIME = {"Bhaṅgakkhaṇe": "В момент распада", "Uppādakkhaṇe": "В момент возникновения"}

# (14) answers (fixed). "vītakkantaṃ" (^6-8-83) read as vītikkantaṃ (spelling slip).
ATK_ANSWERS = {
    ("Bhaṅgakkhaṇe cittaṃ uppādakkhaṇaṃ vītakkantaṃ bhaṅgakkhaṇaṃ avītikkantaṃ, atītaṃ cittaṃ "
     "uppādakkhaṇañca vītikkantaṃ bhaṅgakkhaṇañca vītikkantaṃ."):
        ("Ум в момент распада миновал момент возникновения, не миновал момент распада, прошлый ум "
         "и миновал момент возникновения, и миновал момент распада."),
    ("Bhaṅgakkhaṇe cittaṃ uppādakkhaṇaṃ vītikkantaṃ bhaṅgakkhaṇaṃ avītikkantaṃ, atītaṃ cittaṃ "
     "uppādakkhaṇañca vītikkantaṃ bhaṅgakkhaṇañca vītikkantaṃ."):
        ("Ум в момент распада миновал момент возникновения, не миновал момент распада, прошлый ум "
         "и миновал момент возникновения, и миновал момент распада."),
    "Atītaṃ cittaṃ.": "Прошлый ум.",
    "Uppādakkhaṇe anāgataṃ cittaṃ.": "Ум в момент возникновения, будущий ум.",
    ("Bhaṅgakkhaṇe cittaṃ bhaṅgakkhaṇaṃ avītikkantaṃ no ca uppādakkhaṇaṃ avītikkantaṃ, uppādakkhaṇe "
     "anāgatañca cittaṃ bhaṅgakkhaṇañca avītikkantaṃ uppādakkhaṇañca avītikkantaṃ."):
        ("Ум в момент распада не миновал момент распада, но миновал момент возникновения, ум в момент "
         "возникновения и будущий ум не миновали момент распада и не миновали момент возникновения."),
}

# ---------------------------------------------------------------------------------------------
# Suttanta / Abhidhamma mixtures: qualified mind NPs (pi-2 satipaṭṭhāna / ñāṇa vibhaṅga; pi-1).
# A postposed phrase carries its closing comma so that «У кого ум, охваченный страстью, возникает».
# ---------------------------------------------------------------------------------------------
CITTA_NP = {
    "": CITTA,
    "sarāgaṃ": "ум, охваченный страстью,",
    "vītarāgaṃ": "ум, свободный от страсти,",
    "sadosaṃ": "ум, охваченный злобой,",
    "vītadosaṃ": "ум, свободный от злобы,",
    "samohaṃ": "ум, охваченный заблуждением,",
    "vītamohaṃ": "ум, свободный от заблуждения,",
    "saṃkhittaṃ": "сжатый ум",
    "vikkhittaṃ": "рассеянный ум",
    "mahaggataṃ": "возвышенный ум",
    "amahaggataṃ": "невозвышенный ум",
    "sauttaraṃ": "ум, имеющий над собой высшее,",
    "anuttaraṃ": "ум, не имеющий над собой высшего,",
    "samāhitaṃ": "сосредоточенный ум",
    "asamāhitaṃ": "несосредоточенный ум",
    "vimuttaṃ": "освобождённый ум",
    "avimuttaṃ": "неосвобождённый ум",
    "kusalaṃ": B.ADJ["kusala"]["m_nom"] + " ум",
    "akusalaṃ": B.ADJ["akusala"]["m_nom"] + " ум",
    "abyākataṃ": B.ADJ["abyākata"]["m_nom"] + " ум",
    "sukhāya vedanāya sampayuttaṃ": "ум, связанный с приятным чувством,",
    "saraṇaṃ": "ум, сопряжённый с борьбой,",
    "araṇaṃ": "ум, свободный от борьбы,",
}
ETENA_UPAYENA = "(Этим способом следует развернуть вплоть до сопряжённого с борьбой и свободного от борьбы.)"


# ---------------------------------------------------------------------------------------------
# Predicate rendering
# ---------------------------------------------------------------------------------------------
def P(s, num=0):
    """'uppajjati na nirujjhati' -> «возникает, но не прекращается»; 'na uppannaṃ' -> «не является возникшим»."""
    items, neg = [], False
    for t in s.split():
        if t == "na":
            neg = True
            continue
        if t in VERB:
            w = VERB[t][num]
        elif t in COP:
            w = f"{COPULA[num]} {COP[t][num]}"
        else:
            raise ValueError(f"predicate not parsed: {s!r}")
        items.append(("не " if neg else "") + w)
        neg = False
    assert items and not neg, s
    return BUT.join(items)


def no_ca(s, res="", num=0):
    """the clause after 'no ca' (with its leading ', но'): 'P' -> «, но <res> не P» (7-01 NO_CA_FRAME);
    'na P' -> «, но <res> P» (the denied negative said plainly: NO_CA_POS_FRAME)."""
    assert len(s.split()) <= 2, s
    if s.startswith("na "):
        out = NO_CA_POS_FRAME.format(res=res, pos_pred=P(s[3:], num))
    else:
        out = NO_CA_FRAME.format(res=res, neg_pred=P("na " + s, num))
    return out.replace("  ", " ")      # no subject (bare answers): «, но не является …»


CEVA_RE = re.compile(r"(.+?)(ñceva| ceva) (.+?)(ñca| ca)")


def _ceva(rest, num):
    m = CEVA_RE.fullmatch(rest)
    a = m.group(1) + ("ṃ" if m.group(2) == "ñceva" else "")
    b = m.group(3) + ("ṃ" if m.group(4) == "ñca" else "")
    if a in COP and b in COP:
        return CEVA_CA_COP.format(cop=COPULA[num], a=COP[a][num], b=COP[b][num])
    return CEVA_CA.format(a=P(a, num), b=P(b, num))


def _neither(rest, num):
    m = re.fullmatch(r"na ceva (.+) na ca (.+)", rest)
    a, b = m.group(1), m.group(2)
    if a in COP and b in COP:
        return NA_CEVA_NA_CA_COP.format(cop=COPULA[num], a=COP[a][num], b=COP[b][num])
    return NA_CEVA_NA_CA.format(a=P("na " + a, num), b=P("na " + b, num))


def clause(rest, num=0):
    """Predicate part of an answer sentence ('P1, no ca X P2', 'A ceva B ca', 'na ceva A na ca B', 'P')."""
    if ", no ca " in rest:
        p1, p2 = rest.split(", no ca ")
        x = ""
        for pre, ru in NO_CA_X.items():
            if p2.startswith(pre):
                p2, x = p2[len(pre):], ru
                break
        return P(p1, num) + no_ca(p2, x, num)
    if ", " in rest:
        p1, p2 = rest.split(", ", 1)
        return f"{P(p1, num)}, {clause(p2, num)}"
    if rest.startswith("na ceva "):
        return _neither(rest, num)
    if CEVA_RE.fullmatch(rest):
        return _ceva(rest, num)
    return P(rest, num)


def sentence(s):
    """One answer sentence without its final '.'."""
    if " tesaṃ cittaṃ " in s:
        who, rest = s.split(" tesaṃ cittaṃ ", 1)
        who_ru, add = WHO[who]
        return f"{who_ru}{' ' + WHO_TESAM if add else ''} {CITTA} {clause(rest, 0)}"
    m = re.match(r"(.+?) cittaṃ (.+)", s)
    if m and m.group(1) in DSUBJ:
        subj, num = DSUBJ[m.group(1)]
        return f"{subj} {clause(m.group(2), num)}"
    first, rest = s.split(" ", 1)
    return f"{BARE_TIME[first]} {clause(rest, 0)}"


def answer(text):
    text = text.strip()
    if text in SHORT:
        return SHORT[text]
    if text in ATK_ANSWERS:
        return ATK_ANSWERS[text]
    out = []
    for s in re.split(r"(?<=\.) ", text):
        assert s.endswith("."), s
        out.append(sentence(s[:-1]) + ".")
    return " ".join(out)


# ---------------------------------------------------------------------------------------------
# Questions
# ---------------------------------------------------------------------------------------------
def strip_ti(body):
    """drop the quotation particle of the niddesa questions: …uppajjatīti / …uppannanti / …uppajjitthāti."""
    for end, rep in (("īti", "i"), ("nti", "ṃ"), ("āti", "a")):
        if body.endswith(end):
            return body[: -len(end)] + rep
    return body


PERSON_RE = re.compile(r"yassa (vā pana )?(yaṃ )?(\D*?)cittaṃ (.+?)"
                       r"(?: no ca tassa (?:taṃ )?cittaṃ (.+?),)? tassa (taṃ )?(\D*?)cittaṃ (.+)")
DHAMMA_RE = re.compile(r"yaṃ (vā pana )?cittaṃ (.+?)(?: no ca taṃ cittaṃ (.+?),)? taṃ cittaṃ (.+)")
BARE_RE = re.compile(r"(na )?(\w+) (na )?(\w+)")
ATK_RE = re.compile(r"(na )?(uppajjamānaṃ|nirujjhamānaṃ) khaṇaṃ khaṇaṃ vītikkantaṃ atikkantakālaṃ")


def _s(np, p1, p_noca=None, res=""):
    s = f"{np} {P(p1)}"
    if p_noca is not None:            # (11): "P1 no ca tassa cittaṃ P2" = «ум P1, но у него ум не P2»
        s += no_ca(p_noca, res)
    return s


def question(body):
    """body = the question text after the label, without '?' and without the ti particle."""
    vp = body.startswith(("yassa vā pana", "yaṃ vā pana"))
    if "khaṇaṃ khaṇaṃ" in body:
        parts = ATK_RE.findall(body)
        assert len(parts) == 2, body
        p1 = CITTA + " " + ", ".join((ATK_PART_NEG if n else ATK_PART).format(stage=ATK_STAGE[st]) for n, st in parts)
        if re.match(r"yassa (vā pana )?yaṃ ", body):
            assert body.endswith("tassa taṃ cittaṃ"), body
            return kha(PD_Q.format(p1=p1, p2=ATK_P2), vp)
        if body.startswith("yassa"):
            assert body.endswith("tassa cittaṃ"), body
            return kha(PERSON_Q.format(p1=p1, p2=ATK_P2), vp)
        assert body.startswith("yaṃ") and body.endswith("taṃ cittaṃ"), body
        return kha(DHAMMA_Q.format(p1=p1, p2=ATK_P2), vp)
    m = PERSON_RE.fullmatch(body)
    if m:
        _, yam, q1, p1, p2, tam, q2, p3 = m.groups()
        assert bool(yam) == bool(tam) and q1 == q2, body
        np = CITTA_NP[q1.strip()]
        if yam:
            res = NO_CA_X["tassa taṃ cittaṃ "]
            return kha(PD_Q.format(p1=_s(np, p1, p2, res), p2=_s(np, p3)), vp)
        res = NO_CA_X["tassa cittaṃ "]
        return kha(PERSON_Q.format(p1=_s(np, p1, p2, res), p2=_s(np, p3)), vp)
    m = DHAMMA_RE.fullmatch(body)
    if m:
        _, p1, p2, p3 = m.groups()
        res = NO_CA_X["taṃ cittaṃ "]
        return kha(DHAMMA_Q.format(p1=_s(CITTA, p1, p2, res), p2=_s(CITTA, p3)), vp)
    m = BARE_RE.fullmatch(body)
    if m and m.group(2) in SUBST and m.group(4) in COP:
        n1, w1, n2, w2 = m.groups()
        subj = SUBST[w1][1 if n1 else 0]
        return BARE_Q.format(subj=B.cap(subj), pred=P((n2 or "") + w2))
    raise ValueError(f"question not parsed: {body!r}")


MIX_RE = re.compile(r"[Yy]assa (.+?) cittaṃ uppajjati")


def mixture(text):
    """'Yassa sarāgaṃ cittaṃ uppajjati…pe… yassa vītarāgaṃ cittaṃ uppajjati… …?'"""
    items = MIX_RE.findall(text)
    rest = MIX_RE.sub("", text)
    assert re.fullmatch(r"(\s*…(pe…)?\s*)+\?", rest), rest     # only ellipses between the items
    ru = [f"у кого {CITTA_NP[q]} {VERB['uppajjati'][0]}" for q in items]
    return B.cap("… ".join(ru)) + "…?"


# ---------------------------------------------------------------------------------------------
# Fixed lines (composed from the frames above)
# ---------------------------------------------------------------------------------------------
_UNC = "uppajjati na nirujjhati, nirujjhissati na uppajjissati"
FIXED = {
    "(Etena upāyena yāva saraṇaaraṇā uddharitabbā.)": ETENA_UPAYENA,
    "(Yassa cittake sakabhāvena niddiṭṭhe, yaṃ cittake ca yassa yaṃ cittake ca ekattena niddiṭṭhe.)":
        "(Раздел «у кого ум» изложен в собственном виде, а раздел «какой ум» и раздел «у кого какой ум» "
        "изложены как одно целое.)",
    ("Sarāgapacchimacittassa uppādakkhaṇe tesaṃ sarāgaṃ cittaṃ uppajjati na nirujjhati, nirujjhissati na "
     "uppajjissati. Itaresaṃ sarāgacittassa uppādakkhaṇe tesaṃ…pe…."):
        (f"В момент возникновения последнего ума, охваченного страстью, {WHO_TESAM} {CITTA_NP['sarāgaṃ']} "
         f"{clause(_UNC)}. У остальных в момент возникновения ума, охваченного страстью…"),
    ("Pacchimakusalacittassa uppādakkhaṇe tesaṃ kusalaṃ cittaṃ uppajjati na nirujjhati, nirujjhissati na "
     "uppajjissati. Itaresaṃ kusalacittassa uppādakkhaṇe tesaṃ…pe…."):
        (f"В момент возникновения последнего {B.ADJ['kusala']['m_gen']} ума {WHO_TESAM} {CITTA_NP['kusalaṃ']} "
         f"{clause(_UNC)}. У остальных в момент возникновения {B.ADJ['kusala']['m_gen']} ума…"),
    "Yassa vā pana…pe…? Āmantā …pe….": f"{PERSON_KHA}…? {B.AMANTA[:-1]}…",
    ("Yassa akusalaṃ cittaṃ uppajjati na nirujjhati…pe…. Yassa abyākataṃ cittaṃ uppajjati na "
     "nirujjhati…pe…."):
        (f"{PERSON_KA} {CITTA_NP['akusalaṃ']} {P('uppajjati na nirujjhati')}… "
         f"{PERSON_KA} {CITTA_NP['abyākataṃ']} {P('uppajjati na nirujjhati')}…"),
    "(Mūlayamakaṃ cittayamakaṃ dhammayamakanti tīṇi yamakāni yāva saraṇaaraṇā gacchanti.)":
        (f"(Три части, «{B.YAMAKA_TITLES['Mūlayamakaṃ']}», «{B.YAMAKA_TITLES['Cittayamakaṃ']}» и "
         f"«{B.YAMAKA_TITLES['Dhammayamakaṃ']}», доходят вплоть до сопряжённого с борьбой и свободного от борьбы.)"),
    "Cittayamakaṃ niṭṭhitaṃ.": B.YAMAKA_CLOSING_FRAME.format(title=B.YAMAKA_TITLES["Cittayamakaṃ"]),
}


# ---------------------------------------------------------------------------------------------
# Lines
# ---------------------------------------------------------------------------------------------
HEAD_RE = re.compile(r"(#+) (?:\((Ka|Kha)\) |\((\d+)\) )?(.+)")
LABEL_Q_RE = re.compile(r"\((Ka|Kha)\) (.+?)\?(?: (.+))?")
PLAIN_HEAD_RE = re.compile(r"\((\d+)\) (\w+vāro)")


def heading_word(w):
    if w in B.YAMAKA_TITLES:
        return B.YAMAKA_TITLES[w]
    return B.SECTION_HEADINGS[w]


def tr(text):
    if not text.strip():
        return ""
    m = HEAD_RE.fullmatch(text)
    if m and text.startswith("#"):
        hashes, lab, num, word = m.groups()
        ru = heading_word(word)
        if lab:
            return f"{hashes} ({B.LETTERS[lab]}) {B.cap(ru)}"
        if num:
            return f"{hashes} ({num}) {B.cap(ru)}"
        return f"{hashes} {B.cap(ru)}"
    m = PLAIN_HEAD_RE.fullmatch(text)
    if m:
        return f"({m.group(1)}) {B.cap(heading_word(m.group(2)))}"
    if text in FIXED:
        return FIXED[text]
    if text.startswith("Yassa ") and "cittaṃ uppajjati…" in text:
        return mixture(text)
    m = LABEL_Q_RE.fullmatch(text)
    if m:
        lab, body, ans = m.groups()
        out = f"({B.LETTERS[lab]}) " + question(strip_ti(body))
        return out + (" " + answer(ans) if ans else "")
    if text.startswith("Yassa ") and text.endswith("?"):     # unlabeled question (mixture niddesa)
        return question(strip_ti("y" + text[1:-1]))
    return answer(text)


def translate_file(src_text):
    out = []
    for line in src_text.split("\n"):
        body, bid = B.ID_RE.match(line).groups()
        out.append(tr(body) + (bid or ""))
    return "\n".join(out)


# ---------------------------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------------------------
# Strings this builder takes from the approved pi-1 … pi-5 Russian rails (book, exact string).
CROSSBOOK = [
    ("2", "ум, охваченный страстью"), ("2", "ум, свободный от страсти"), ("2", "ум, охваченный злобой"),
    ("2", "ум, свободный от злобы"), ("2", "ум, охваченный заблуждением"), ("2", "ум, свободный от заблуждения"),
    ("2", "сжатый ум"), ("2", "рассеянный ум"), ("2", "возвышенный ум"), ("2", "невозвышенный ум"),
    ("2", "ум, имеющий над собой высшее"), ("2", "ум, не имеющий над собой высшего"),
    ("2", "сосредоточенный ум"), ("2", "несосредоточенный ум"), ("2", "освобождённый ум"),
    ("2", "неосвобождённый ум"),
    ("1", "Явления, сопряжённые с борьбой."), ("1", "Явления, свободные от борьбы."),
    ("1", "Явления, связанные с приятным чувством."), ("1", "благой ум"),
    ("5", "существ без восприятия"), ("5", "медитативное достижение прекращения"),
    ("5", "Момент возникновения"), ("5", "в момент распада"), ("2", "обладающий"),
    ("1", "прошлые явления"), ("1", "будущие явления"), ("1", "настоящие явления"),
]


def check_crossbook():
    B.check_crossbook()
    cache, missing = {}, []
    for b, s in CROSSBOOK:
        if b not in cache:
            cache[b] = "\n".join(p.read_text(encoding="utf-8") for p in sorted(B.RAILS[b].glob("*.md")))
        if s not in cache[b]:
            missing.append((b, s))
    if missing:
        raise AssertionError(f"cross-book strings not found in the pi-1..5 rails: {missing}")
    return True


def consistency(pairs):
    """identical Pāli line (without ID and ti particle differences) -> identical Russian line."""
    seen = {}
    for p, r in pairs:
        pb, rb = B.ID_ANY.sub("", p).strip(), B.ID_ANY.sub("", r).strip()
        if not pb:
            continue
        if pb in seen:
            assert seen[pb] == rb, f"inconsistent: {pb!r}\n  {seen[pb]!r}\n  {rb!r}"
        seen[pb] = rb
    return seen


def main():
    check_crossbook()
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    ru = unicodedata.normalize("NFC", translate_file(src))
    pairs = list(zip(src.split("\n"), ru.split("\n")))
    for name in B.SAMPLE_FILES:     # agree with the approved sample on identical Pāli lines
        sp = (B.PALI_DIR / name).read_text(encoding="utf-8").split("\n")
        sr = (B.OUT_DIR / name).read_text(encoding="utf-8").split("\n")
        pairs = list(zip(sp, sr)) + pairs
    consistency(pairs)
    B.check_pair(src, ru, CHAPTER)
    with open(B.OUT_DIR / CHAPTER, "w", encoding="utf-8", newline="\n") as f:
        f.write(ru)
    print("written", B.OUT_DIR / CHAPTER, "lines", len(ru.split("\n")))
    print("cross-book asserts OK; consistency OK; per-line checks OK")


if __name__ == "__main__":
    main()
