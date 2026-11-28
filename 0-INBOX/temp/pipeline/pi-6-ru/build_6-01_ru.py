"""Russian plain zero-shot of pi-6 (Yamaka): chapter 6-01-sankharayamaka.md (Saṅkhārayamaka, part 1).

Families A and B come from build_2-01_ru (imported, never edited); E.pv_abbr from build_2-02_ru; the person / place
shape from build_7-01_ru; the moments, «у них», persons of the citta yamaka from build_8_ru; the joining of mixed
person / time intros from build_5-01_ru (the same rules, re-implemented here for the Saṅkhāra units); the
Āyatana planes (kāmāvacara / rūpāvacara / arūpāvacara) from build_3-01_ru; the notes' words from build_5-02_ru.
NEW here (listed in notes-6-01.md): the Saṅkhāra members, the breath / thought moments, the jhāna persons and
places, "yassa cittassa anantarā … pacchimacittaṃ uppajjissati", the "bhūmi" places, and this chapter's notes.

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_6-01_ru.py
Probe:  python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_6-01_ru.py --probe 6-02-sankharayamaka.md
        (prints only: which lines of another chapter these frames already translate)
Import: K = importlib.import_module("build_6-01_ru")   (importing never writes any file; only __main__ builds)

Exposed for 6-02
  Members     SK_X, SK_K, SK_LEX, SK_QUAL, SK_SUBJ, SK_PJ_OBJ, SK_CFG, TAYO_SANKHARA_LINE
  Intros      SK_UNITS, sk_units(intro), sk_intro(intro, tattha), sk_place_intro(intro), jhana_acc(), jhana_loc()
  Sentences   pv_sentence(s, cfg), pv_answers(text, cfg), pv_question(q, cfg), pv_line(text, cfg)
  Paṇṇatti    pn_line(text, cfg)
  Lines       tr(text, cfg, mode), translate_text(src, cfg, mode="pn")   (mode "pv" from the "Pavatti…" heading)
  Notes       NOTES (whole-line editorial notes), HEADS (headings incl. Suddhasaṅkhāravāro)
"""
import importlib
import pathlib
import re
import sys
import unicodedata

HERE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru")
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import build_sample_ru as B  # noqa: E402

A = importlib.import_module("build_2-01_ru")    # families A + B (frame-setter)
E = importlib.import_module("build_2-02_ru")    # pv_abbr, PERSON_UNITS_2_02, family E
C = importlib.import_module("build_7-01_ru")    # person / place shape
D = importlib.import_module("build_8_ru")       # moments, «у них», persons of the citta yamaka
S = importlib.import_module("build_5-01_ru")    # mixed person / time intros (joining rules), notes words
S2 = importlib.import_module("build_5-02_ru")   # notes words (yassayatthaka …), "(Kha) yassa vā pana…pe…. Āmantā."
AY = importlib.import_module("build_3-01_ru")   # Āyatana planes (kāmāvacara / rūpāvacara / arūpāvacara)

CHAPTER = "6-01-sankharayamaka.md"
cap, lower1, N = B.cap, C.lower1, A.N
SLIP_LOG = []

# =============================================================================================
# Members (pi-2 Paṭiccasamuppādavibhaṅga ^2-226 Russian, asserted below)
# =============================================================================================
# kāyasaṅkhāro / vacīsaṅkhāro / cittasaṅkhāro = «телесный формирующий фактор / речевой формирующий фактор /
# формирующий фактор ума» (pi-2; pi-5 has «умственный формирующий фактор» for cittasaṅkhāro: not used, the
# coordinator brief names pi-2). Bare words of the paṇṇattivāra: kāyo «тело», vacī «речь», cittaṃ «ум» (pi-1 … 5).
SK_X = {
    "kāya": N("тело", "телом", "тела", "n"),
    "vacī": N("речь", "речью", "речи", "f"),
    "citta": N("ум", "умом", "ума", "m"),
}
SK_K = {
    "kāya": N("телесный формирующий фактор", "телесным формирующим фактором", "телесного формирующего фактора", "m"),
    "vacī": N("речевой формирующий фактор", "речевым формирующим фактором", "речевого формирующего фактора", "m"),
    "citta": N("формирующий фактор ума", "формирующим фактором ума", "формирующего фактора ума", "m"),
}
SK_G_SG = N("формирующий фактор", "формирующим фактором", "формирующего фактора", "m")   # saṅkhāro
SK_G_PL = A.KH_X["saṅkhāra"]                                                          # saṅkhārā (2-01)
assert SK_G_PL["nom"] == "формирующие факторы"
SK_X_FORMS = {"kāya": ["kāyo", "kāyaṃ"], "vacī": ["vacī", "vaciṃ"], "citta": ["cittaṃ"]}
SK_LEX = {}
for _m, _forms in SK_X_FORMS.items():
    for _f in _forms:
        SK_LEX[_f] = SK_X[_m]
    SK_LEX[_m + "saṅkhāro"] = SK_K[_m]
    SK_LEX[_m + "saṅkhāraṃ"] = SK_K[_m]
SK_LEX.update({"saṅkhāro": SK_G_SG, "saṅkhāraṃ": SK_G_SG, "saṅkhārā": SK_G_PL})
SK_SUBJ = {_m + "saṅkhāro": SK_K[_m] for _m in SK_K}                 # pavattivāra subjects (all masculine)
SK_GENDER = "m"                                                      # bare verb answers «Возникал.»
SK_PJ_OBJ = {_m + "saṅkhāraṃ": SK_K[_m]["nom"] for _m in SK_K}       # pariññāvāra objects (acc = nom), for 6-02
# Paṇṇatti qualifiers ("Q na K, X."): the Russian subject with its agreement class
SK_QUAL = {}
for _m in SK_K:
    SK_QUAL[SK_X_FORMS[_m][0]] = (cap(SK_X[_m]["nom"]), SK_X[_m]["g"])
    SK_QUAL[_m + "saṅkhāro"] = (cap(SK_K[_m]["nom"]), SK_K[_m]["g"])

# Uddesa (^6-6-1)
ASSASA = {"nom": "вдохи и выдохи", "gen": "вдохов и выдохов"}                              # pi-5
VITAKKA = {"nom": "направленная мысль и удержание мысли", "gen": "направленной мысли и удержания мысли"}   # pi-1/pi-5
SANNA_VEDANA = "восприятие и чувство"                                                     # saññā ca vedanā ca (pi-5)
CITTASAMPAYUTTA = "явления, связанные с умом"                                             # pi-1 cittasampayuttā dhammā
SK_LIST = f"{SK_K['kāya']['nom']}, {SK_K['vacī']['nom']} и {SK_K['citta']['nom']}"
TAYO_SANKHARA_LINE = (
    f"Три формирующих фактора – {SK_LIST}. "
    f"{cap(ASSASA['nom'])} являются {SK_K['kāya']['instr']}, {VITAKKA['nom']} являются {SK_K['vacī']['instr']}, "
    f"{SANNA_VEDANA} являются {SK_K['citta']['instr']}. "
    f"Кроме {VITAKKA['gen']}, все {CITTASAMPAYUTTA}, являются {SK_K['citta']['instr']}.")

# =============================================================================================
# Pavattivāra intros: persons, moments, jhānas and planes
# =============================================================================================
PLANES = AY.AY_PLANES                         # 2-01 PLANES + kāmāvacara / rūpāvacara / arūpāvacara (3-01)
PLANE_RX = A._plane_re(PLANES)                # capturing: "(asaññasatt|…)"
PLANE_ALT = "(?:" + PLANE_RX[1:]              # non-capturing, for the "({P})" slots of SK_UNITS
UPPADA, BHANGA = S.UPPADA, S.BHANGA           # «в момент возникновения / распада» (8, 5-01)
MOMENT = {"uppādakkhaṇe": UPPADA, "bhaṅgakkhaṇe": BHANGA}
# genitive after the moment
MOMENT_GEN = {
    "assāsapassāsānaṃ": ASSASA["gen"],                                          # вдохов и выдохов
    "vitakkavicārānaṃ": VITAKKA["gen"],                                         # направленной мысли и удержания мысли
    "cittassa": "ума",                                                          # 8
    "pacchimacittassa": "последнего ума",                                       # 8
    "avitakkaavicāracittassa": "ума без направленной мысли и без удержания мысли",   # pi-1 avitakkaavicāra
    "savitakkasavicārapacchimacittassa": "последнего ума с направленной мыслью и удержанием мысли",   # pi-1
    "avitakkaavicārapacchimacittassa": "последнего ума без направленной мысли и без удержания мысли",  # 6-02
}
VINA = {"assāsapassāsehi": "без " + ASSASA["gen"], "vitakkavicārehi": "без " + VITAKKA["gen"]}   # vinā …ehi
# jhānas (pi-1 «первое медитативное погружение»): ordinal (acc, prep)
JHANA_ORD = {"paṭhama": ("первое", "первом"), "dutiya": ("второе", "втором"), "tatiya": ("третье", "третьем"),
             "catuttha": ("четвёртое", "четвёртом")}
JHANA_ACC, JHANA_PREP = "медитативное погружение", "медитативном погружении"
JH_RX = r"(?:paṭhama|dutiya|tatiya|catuttha)jjhān"
BHUMI = {   # pi-1 "Savitakkasavicārabhūmiyaṃ" = «На уровне с направленной мыслью и удержанием мысли»
    "savitakkasavicārabhūmiyaṃ": "на уровне с направленной мыслью и удержанием мысли",
    "avitakkaavicārabhūmiyaṃ": "на уровне без направленной мысли и без удержания мысли",
}
LAST_MIND_HOLDERS = dict((u[0], u[1]) for u in S.SC_UNITS)["pacchimacittasamaṅgīnaṃ"]   # обладающих последним умом
NIRODHA_HOLDERS = dict((u[0], u[1]) for u in S.SC_UNITS)["nirodhasamāpannānaṃ"]
ANANTARA = "сразу после данного ума"                                             # 5-01 (yassa cittassa anantarā)
LAST_MIND_ARISES = f"{ANANTARA} возникнет последний ум"
SAMAPANNA = "вошедших"                                                          # samāpanna (pi-5 «у вошедшего в»)
TESAMYEVA = "них же"                                                            # tesaṃyeva (with «у»: «у них же»)
ALL = "всех"                                                                    # sabbesaṃ (5-01)


def ru_and(items):
    return items[0] if len(items) == 1 else ", ".join(items[:-1]) + " и " + items[-1]


def _v(s):
    return ("во " if re.match(r"вт", s) else "в ") + s


def jhana_acc(ords):
    """['dutiya', 'tatiya'] -> «во второе и третье медитативное погружение»."""
    return _v(ru_and([JHANA_ORD[o][0] for o in ords]) + " " + JHANA_ACC)


def jhana_loc(ords):
    """['paṭhama', 'dutiya'] -> «в первом и втором медитативном погружении»."""
    return _v(ru_and([JHANA_ORD[o][1] for o in ords]) + " " + JHANA_PREP)


def _ords(s, end):
    return [w[: -len("jjhān" + end)] for w in s.split()]


def _unit_ru(rx, s, pos):
    m = re.compile(rx.replace("{P}", PLANE_ALT).replace("{JH}", JH_RX)).match(s, pos)
    if m and (m.end() == len(s) or s[m.end()] == " "):
        return m
    return None


def _in(p):
    return PLANES[p]["in"]


def _beings(p):
    return PLANES[p]["beings"]


_REL_LAST_LIFE = next(ru for rx, ru, _ in A.PERSON_UNITS if rx == r"{P}e pacchimabhavikānaṃ")
_REL_REBORN = next(ru for rx, ru, _ in A.PERSON_UNITS if rx == r"{P}aṃ upapajjantānaṃ")
_REL_YE_CA = next(ru for rx, ru, _ in E.PERSON_UNITS_2_02 if rx.endswith("tesaṃ cavantānaṃ"))
_TWO = "{in1} и {in2}"                          # two planes (3-02, 3-03: «в мире форм и в мире без форм»)

# (pattern, builder(match) -> Russian, kind). kinds as build_5-01_ru: noun (person, genitive after «у»), rel
# (person clause, closing comma), adv (time phrase), advcl («когда …», commas both sides), loc (place: joins the
# next phrase), pair (two plane-beings «A и B»: split into two persons when the intro names other persons).
SK_UNITS = [
    (r"vinā (assāsapassāsehi|vitakkavicārehi) (\S+) (uppādakkhaṇe|bhaṅgakkhaṇe)",
     lambda m: f"{VINA[m.group(1)]} {MOMENT[m.group(3)]} {MOMENT_GEN[m.group(2)]}", "adv"),
    (r"(" + "|".join(sorted(MOMENT_GEN, key=len, reverse=True)) + r") (uppādakkhaṇe|bhaṅgakkhaṇe)",
     lambda m: f"{MOMENT[m.group(2)]} {MOMENT_GEN[m.group(1)]}", "adv"),
    (r"yassa cittassa anantarā ({P})ānaṃ pacchimacittaṃ uppajjissati",
     lambda m: f"{_beings(m.group(1))}, у которых {LAST_MIND_ARISES}", "rel"),
    (r"yassa cittassa anantarā avitakkaavicāraṃ pacchimacittaṃ uppajjissati",
     lambda m: f"тех, у кого {LAST_MIND_ARISES} без направленной мысли и без удержания мысли", "rel"),
    (r"((?:{JH}aṃ )+)samāpannānaṃ", lambda m: f"{SAMAPANNA} {jhana_acc(_ords(m.group(1), 'aṃ'))}", "noun"),
    (r"({P})e ({P})e pacchimacittasamaṅgīnaṃ",
     lambda m: f"{LAST_MIND_HOLDERS} {_in(m.group(1))} и {_in(m.group(2))}", "noun"),
    (r"({P})e pacchimacittasamaṅgīnaṃ", lambda m: f"{LAST_MIND_HOLDERS} {_in(m.group(1))}", "noun"),
    (r"(savitakkasavicārabhūmiyaṃ|avitakkaavicārabhūmiyaṃ) pacchimacittasamaṅgīnaṃ",
     lambda m: f"{LAST_MIND_HOLDERS} {BHUMI[m.group(1)]}", "noun"),
    (r"avitakkaavicārapacchimacittasamaṅgīnaṃ",
     lambda m: f"{LAST_MIND_HOLDERS} без направленной мысли и без удержания мысли", "noun"),
    (r"pacchimacittasamaṅgīnaṃ", lambda m: LAST_MIND_HOLDERS, "noun"),
    (r"nirodhasamāpannānaṃ", lambda m: NIRODHA_HOLDERS, "noun"),
    (r"tesaṃyeva", lambda m: TESAMYEVA, "noun"),
    (r"sabbesaṃ", lambda m: ALL, "noun"),
    (r"itaresaṃ", lambda m: A.ITARESAM, "noun"),
    (r"dutiye citte vattamāne", lambda m: "когда присутствует второй ум", "advcl"),            # 5-01
    (r"ye ca ({P})aṃ ({P})aṃ upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ",
     lambda m: _REL_YE_CA.replace("{in1}", _TWO).format(in1=_in(m.group(1)), in2=_in(m.group(2))), "rel"),
    (r"({P})e ({P})e pacchimabhavikānaṃ",
     lambda m: _REL_LAST_LIFE.replace("{in1}", _TWO).format(in1=_in(m.group(1)), in2=_in(m.group(2))), "rel"),
    (r"({P})aṃ upapajjantānaṃ", lambda m: _REL_REBORN.format(in1=_in(m.group(1))), "rel"),
    (r"({P})ānaṃ ({P})ānaṃ", lambda m: f"{_beings(m.group(1))} и {_beings(m.group(2))}", "pair"),
    (r"({P})ānaṃ", lambda m: _beings(m.group(1)), "noun"),
    (r"(savitakkasavicārabhūmiyaṃ|avitakkaavicārabhūmiyaṃ)", lambda m: BHUMI[m.group(1)], "loc"),
    (r"({P})e", lambda m: _in(m.group(1)), "loc"),          # a plane before a moment (6-02: "Kāmāvacare pacchimacittassa …")
]
PERSON_KINDS = ("noun", "rel")
CLOSES = ("rel", "advcl")
OPENS = ("advcl",)


def sk_units(intro):
    """Pāli intro -> [[russian, kind], …]: itaresaṃ merged as in 2-01 / 5-01; a plane pair stays «A и B» when
    it is the only person (3-01) or follows itaresaṃ, else it splits into two persons («у A и у B»)."""
    s = lower1(intro)
    units, pos = [], 0
    while pos < len(s):
        for rx, fn, kind in SK_UNITS:
            m = _unit_ru(rx, s, pos)
            if m:
                units.append([fn(m), kind, m])
                pos = m.end() + 1
                break
        else:
            raise ValueError(f"intro not parsed at {s[pos:]!r} in {intro!r}")
    out = []
    for ru, kind, m in units:
        prev = out[-1] if out else None
        if prev and prev[0] == A.ITARESAM and prev[1] == "noun":
            if kind in ("noun", "pair"):
                prev[:] = [f"{A.ITARESAM} {ru}", "noun", None]
                continue
            if kind == "rel" and ru.startswith("тех, кто"):
                prev[:] = [A.ITARESAM + ru[3:], "rel", None]
                continue
        out.append([ru, kind, m])
    n_persons = sum(1 for _, k, _ in out if k in PERSON_KINDS + ("pair",))
    final = []
    for ru, kind, m in out:
        if kind == "pair":
            if n_persons > 1:
                final += [[_beings(m.group(1)), "noun"], [_beings(m.group(2)), "noun"]]
            else:
                final.append([ru, "noun"])
        else:
            final.append([ru, kind])
    return final


def sk_intro(intro, tattha=False):
    """Person / time intro of an answer (+ «у них» when no person is named, + «там» for tattha), ending with a
    space. Joining as build_5-01_ru.pv_intro: a time phrase or place joins a preceding person noun; items «A, B и C»
    («, и» after a clause); a closing comma after a clause."""
    items, prev = [], None
    for ru, kind in sk_units(intro):
        if kind in PERSON_KINDS:
            ru = "у " + ru
        attach = prev in ("noun", "loc") and kind not in PERSON_KINDS
        if attach and items:
            items[-1].append((ru, kind))
        else:
            items.append([(ru, kind)])
        prev = kind
    persons = any(k in PERSON_KINDS for it in items for _, k in it)

    def render(item):
        out = item[0][0]
        for (_, pk), (ru, k) in zip(item, item[1:]):
            out += (", " if (pk in CLOSES or k in OPENS) else " ") + ru
        return out

    out = render(items[0])
    for i in range(1, len(items)):
        pc = items[i - 1][-1][1] in CLOSES
        out += ((", и " if pc else " и ") if i == len(items) - 1 else ", ") + render(items[i])
    if items[-1][-1][1] in CLOSES:
        out += ","
    if not persons:
        out += " " + S.WHO_TESAM
    if tattha:
        out += " " + S.TAM
    return cap(out) + " "


def sk_place_intro(intro):
    """'Paṭhamajjhāne kāmāvacare' -> «В первом медитативном погружении, в мире чувственных желаний: там »
    (7-01 colon form, places joined by C.LOCI_SEP; consecutive jhānas share one noun: «во втором и третьем …»)."""
    toks = lower1(intro).split()
    loci, jh = [], []
    for t in toks + [None]:
        if t is not None and re.fullmatch(JH_RX + "e", t):
            jh.append(t[: -len("jjhāne")])
            continue
        if jh:
            loci.append(jhana_loc(jh))
            jh = []
        if t is None:
            break
        m = re.fullmatch(PLANE_RX + "e", t)
        if not m:
            raise ValueError(f"place intro not parsed: {intro!r}")
        loci.append(_in(m.group(1)))
    return C.ANSWER_INTRO_PLACE.format(loci=cap(C.LOCI_SEP.join(loci)), res=C.RES["tattha"])


# =============================================================================================
# Pavattivāra sentences and questions (frames of build_2-01_ru / build_5-01_ru)
# =============================================================================================
_T = r"(?P<{n}>tesaṃ tattha|tesaṃ|tattha)"
SK_NAMES = "(?:" + "|".join(sorted(SK_SUBJ, key=len, reverse=True)) + ")"
PV_S1_RE = re.compile(r"(?P<intro>.+?) " + _T.format(n="t1") + rf" (?P<x>{SK_NAMES}) (?P<n1>na |n)?(?P<v1>"
                      + A.V_RE + r"), no ca " + _T.format(n="t2") + rf" (?P<y>{SK_NAMES}) (?P<n2>na |n)?(?P<v2>"
                      + A.V_RE + r")")
PV_S2_RE = re.compile(r"(?P<intro>.+?) " + _T.format(n="t1") + rf" (?P<x>{SK_NAMES}) ca (?P<n1>na |n)?(?P<v1>"
                      + A.V_RE + rf") (?P<y>{SK_NAMES}) ca (?P<n2>na |n)?(?P<v2>" + A.V_RE + r")")


def pred(v, x, neg):
    return A.PV_PRED.format(v=A.verb(v, x["g"], bool(neg)), x=x["nom"])


def pv_sentence(s, cfg):
    """One Pāli pavatti answer sentence (no final '.') -> Russian sentence with '.'."""
    if s + "." in C.SIMPLE_ANSWERS:
        return C.SIMPLE_ANSWERS[s + "."]
    lv = lower1(s)
    if lv in A.PV_VERBS:                                   # Uppajjittha. -> «Возникал.»
        return cap(A.verb(lv, cfg.get("gender", SK_GENDER))) + "."
    s = re.sub(r"ñca\b", "ṃ ca", s)
    subj = cfg["pv_subj"]
    for rx, kind in ((PV_S1_RE, 1), (PV_S2_RE, 2)):
        m = rx.fullmatch(s)
        if not m:
            continue
        if m.group("t1").startswith("tesaṃ"):
            head = cfg.get("intro", sk_intro)(m.group("intro"), "tattha" in m.group("t1"))
        else:
            head = cfg.get("place_intro", sk_place_intro)(m.group("intro"))
        x, y = subj[m.group("x")], subj[m.group("y")]
        p1 = pred(m.group("v1"), x, m.group("n1"))
        if kind == 1:   # "no ca": the predicate is denied for Y (coordinator "Negatives")
            res = C.RES[m.group("t2")]
            p2 = pred(m.group("v2"), y, not m.group("n2"))
            tail = (A.PV_NO_CA_POS_FRAME.format(res=res, pred=p2) if m.group("n2")
                    else C.NO_CA_FRAME.format(res=res, neg_pred=p2))
            return head + p1 + tail + "."
        if m.group("n1") and m.group("n2"):
            f1, f2 = A.verb(m.group("v1"), x["g"]), A.verb(m.group("v2"), y["g"])
            both = (A.PV_NEITHER_FRAME.format(v=f1, x=x["nom"], y=y["nom"]) if f1 == f2
                    else A.PV_NEG_MIXED_FRAME.format(v1=f1, x=x["nom"], v2=f2, y=y["nom"]))
            return head + both + "."
        return head + C.BOTH_FRAME.format(p1=p1, p2=pred(m.group("v2"), y, m.group("n2"))) + "."
    raise ValueError(f"pavatti answer not parsed: {s!r}")


def pv_answers(text, cfg):
    out = []
    for s in re.split(r"(?<=\.) (?=\S)", text.strip()):
        assert s.endswith("."), s
        out.append(pv_sentence(s[:-1], cfg))
    return " ".join(out)


# "yassa vā pana cittasaṅkhāro…pe…" (subject named, verb left out) = «А у кого формирующий фактор ума…»
PV_ABBR_X_RE = re.compile(rf"yassa vā pana (?P<x>{SK_NAMES})…pe…")


def pv_question(q, cfg):
    """Pāli question (no '?') -> Russian question with '?'."""
    m = PV_ABBR_X_RE.fullmatch(lower1(q))
    if m:
        return f"{S.PV_ABBR_HEAD['yassa vā pana']} {cfg['pv_subj'][m.group('x')]['nom']}…?"
    return S.pv_question_any(lower1(q), cfg)


# Abbreviated lines ("…pe…" in place of the rest)
ABBR_HEADS = {                                     # first clause of the question frames (7-01 / 2-02 / 5-01 / 5-02)
    "Yattha": E.PV_ABBR_HEAD,                      # «Где {p1}»
    "Yassa yattha": S2.ABBR_YY_HEAD,               # «У кого где {p1}»
    "Yassa vā pana yattha": S.PV_ABBR_HEAD["yassa vā pana yattha"] + " {p1}",   # «А у кого где {p1}»
}
PV_ABBR_RE = re.compile(r"(?P<rel>Yassa vā pana yattha|Yassa yattha|Yattha) (?P<x>" + SK_NAMES + r") (?P<n>na |n)?"
                        r"(?P<v>" + A.V_RE + r")…pe…(?P<dot>\.?)")


def pv_abbr(text, cfg):
    """'Yattha X V…pe….' / 'Yattha X V…pe…' / 'Yassa yattha X V…pe….' / 'Yassa vā pana yattha X na V…pe….'"""
    m = PV_ABBR_RE.fullmatch(text)
    if not m:
        return None
    return ABBR_HEADS[m.group("rel")].format(p1=pred(m.group("v"), cfg["pv_subj"][m.group("x")], m.group("n"))) + "…"


def pv_line(text, cfg):
    r = pv_abbr(text, cfg)
    if r is not None:
        return r
    if "?" in text:
        q, _, rest = text.partition("?")
        out = pv_question(q, cfg)
        rest = rest.strip()
        m = re.fullmatch(r"…[Pp]e…\.(?: (.+))?", rest)
        if m:                                       # "…?…Pe…." (+ a note)
            return out + "…" + (" " + cfg["notes"][m.group(1)] if m.group(1) else "")
        return out + (" " + pv_answers(rest, cfg) if rest else "")
    return pv_answers(text, cfg)


# =============================================================================================
# Paṇṇattivāra lines (family A of build_2-01_ru)
# =============================================================================================
def pn_answers(text, cfg):
    out = []
    for s in re.split(r"(?<=\.) (?=\S)", text.strip()):
        assert s.endswith("."), s
        out.append(C.SIMPLE_ANSWERS[s] if s in C.SIMPLE_ANSWERS
                   else A.pannatti_sentence(s[:-1], cfg["lex"], cfg["qual"]))
    return " ".join(out)


def pn_line(text, cfg):
    """'kāyo kāyasaṅkhāroti? No.' / 'na kāyo na kāyasaṅkhāroti?' / answer sentences (label removed)."""
    if "?" in text:
        q, _, rest = text.partition("?")
        out = A.pada_question(lower1(q), cfg["lex"])
        rest = rest.strip()
        return out + (" " + pn_answers(rest, cfg) if rest else "")
    return pn_answers(text, cfg)


# =============================================================================================
# Headings, closings, notes
# =============================================================================================
HEADS = dict(B.SECTION_HEADINGS)
HEADS.update({
    "Suddhasaṅkhāravāro": "Раздел о формирующих факторах как таковых",   # = Suddhakhandhavāro frame (sample)
    "paccanīkaokāsā": B.SECTION_HEADINGS["paccanīkaokāso"],               # ^6-6-16-5-0 "-okāsā" for "-okāso"
})
HEAD_RE = re.compile(r"(#+) (?:\((\w+)\) )?(.+)")
PLAIN_HEAD_RE = re.compile(r"(?:(\d+) )?\((\w+)\) (\w+)")             # "(Kha) paccanīkaṃ" / "4 (Ṅa) paccanīkaokāso"
LABEL_RE = re.compile(r"\((Ka|Kha)\) (.*)")


def heading(text):
    hashes, lab, body = HEAD_RE.fullmatch(text).groups()
    ru = B.YAMAKA_TITLES[body] if body in B.YAMAKA_TITLES else C.heading_case(HEADS[body])
    if body == "paccanīkaokāsā":
        SLIP_LOG.append("^6-6-16-5-0 heading 'paccanīkaokāsā' = paccanīkaokāso (spelling), rendered as meant")
    return f"{hashes} " + (f"({lab if lab.isdigit() else B.LETTERS[lab]}) " if lab else "") + ru


def plain_heading(text):
    m = PLAIN_HEAD_RE.fullmatch(text)
    if not m or m.group(3) not in HEADS:
        return None
    num, lab, word = m.groups()
    return (f"{num} " if num else "") + f"({B.LETTERS[lab]}) " + C.heading_case(HEADS[word])


# Notes (whole lines). Words from 5-01 / 5-02: «раздел с «у кого»», «раздел с «у кого где»», «следует развернуть»,
# «не следует указывать «у вошедших …»», «вопросы о прошлом», «различия нет».
SAME_YY = S2.SAME_YY                                               # И раздел с «у кого», и раздел с «у кого где» одинаковы
YY_VITTHARA = f"И {S.YASSAKA}, и {S.YASSAYATTHAKA} {C.VITTHARETABBAM} одинаково"
assert f"({YY_VITTHARA})." == S.NOTE_YASSAKA
NIRODHA_Q = f"«{S2.NIRODHASAMAPANNANAM}»"                         # «у вошедших в медитативное достижение прекращения»
NOTES = {
    "(Yassakampi yassayatthakampi sadisaṃ.)": f"({SAME_YY}.)",
    # ekasadisaṃ = «совершенно одинаков» (5-01: "Yatthakampi sabbattha sadisaṃ" = «… тоже везде одинаков»)
    "(Yatthakampi sabbattha ekasadisaṃ).": f"({cap(S.YATTHAKA)} тоже везде совершенно одинаков).",
    "(Yassakampi yassayatthakampi sadisaṃ vitthāretabbaṃ, yassayatthake nirodhasamāpannānanti na labbhati.)":
        f"({YY_VITTHARA}, но {S2.IN_YY} не встречается {NIRODHA_Q}.)",
    "(Yassakampi yassayatthakampi sadisaṃ vitthāretabbaṃ, yassayatthake nirodhasamāpannānanti na kātabbaṃ.)":
        f"({YY_VITTHARA}, но {S2.IN_YY} не следует указывать {NIRODHA_Q}.)",
    ("(Yathā uppādavāre atītā pucchā yassakampi yassayatthakampi anulomampi paccanīkampi vibhattaṃ evaṃ "
     "nirodhavārepi vibhajitabbaṃ, natthi nānākaraṇaṃ.)"):
        (f"(Как {S2.IN_UPPADA} разобраны {S2.ATITA_PUCCHA} и {S2._in(S.YASSAKA)}, и {S2._in(S.YASSAYATTHAKA)}, "
         f"{S2.ANULOMA_PACCANIKA}, так же следует разбирать и {S2.IN_NIRODHA}, {S2.NATTHI_NANAKARANAM}.)"),
}
assert S2.ANULOMA_PACCANIKA.startswith("и ")

FIXED = {
    ("Tayo saṅkhārā – kāyasaṅkhāro, vacīsaṅkhāro, cittasaṅkhāroti. Assāsapassāsā kāyasaṅkhāro, vitakkavicārā "
     "vacīsaṅkhāro, saññā ca vedanā ca cittasaṅkhāro. Ṭhapetvā vitakkavicāre sabbepi cittasampayuttakā dhammā "
     "cittasaṅkhāro."): TAYO_SANKHARA_LINE,
    "Paṇṇattiuddesavāro.": A.PANNATTI_UDDESAVARO,
    "Paṇṇattiniddesavāro.": A.PANNATTI_NIDDESAVARO,
    "Paṇṇattivāro.": C.VARO_CLOSING.format(heading=B.SECTION_HEADINGS["Paṇṇattivāro"]),
    "Uppādavāro.": C.VARO_CLOSING.format(heading=B.SECTION_HEADINGS["Uppādavāro"]),
    "Nirodhavāro.": C.VARO_CLOSING.format(heading=B.SECTION_HEADINGS["Nirodhavāro"]),
    "Uppādanirodhavāro.": C.VARO_CLOSING.format(heading=B.SECTION_HEADINGS["Uppādanirodhavāro"]),
    "Pariññāvāro.": C.VARO_CLOSING.format(heading=B.SECTION_HEADINGS["Pariññāvāro"]),
    # "." in place of "?" (as written; 5-02 ^6-5-97 renders the identical Pāli line)
    "(Kha) yassa vā pana…pe…. Āmantā.": S2.FIXED_5_02["(Kha) yassa vā pana…pe…. Āmantā."],
}

SK_CFG = {
    "lex": SK_LEX,
    "qual": SK_QUAL,
    "pv_subj": SK_SUBJ,
    "pj_obj": SK_PJ_OBJ,
    "gender": SK_GENDER,
    "fixed": FIXED,
    "notes": NOTES,
    "slips": [],
    "variant_anchors": {
        "avasesā saṅkhārā saṅkhārā (sī. syā. kaṃ.)": f"Остальные {SK_G_PL['nom']}",
    },
}


# =============================================================================================
# Lines
# =============================================================================================
def tr(text, cfg, mode):
    """Translate one Pāli line (block ID removed). mode: "pn" (paṇṇattivāra) or "pv" (pavattivāra)."""
    if not text.strip():
        return ""
    if text in cfg["fixed"]:
        return cfg["fixed"][text]
    if text in cfg["notes"]:
        return cfg["notes"][text]
    if text in B.FIXED:
        return B.FIXED[text]
    if text.startswith("#"):
        return heading(text)
    ph = plain_heading(text)
    if ph is not None:
        return ph
    variants, t = S._variants(text, cfg)
    for old, new, note in cfg.get("slips", []):
        if old in t:
            t = t.replace(old, new)
            SLIP_LOG.append(note)
    label = ""
    m = LABEL_RE.fullmatch(t)
    if m:
        label, t = f"({B.LETTERS[m.group(1)]}) ", m.group(2)
    if mode == "pv" and re.search(r"\bparijān", t):
        ru = E.pj_line(f"({m.group(1)}) {t}" if m else t, cfg)            # family E (6-02); label inside
        return S._insert_variants(ru, variants, cfg)
    ru = pn_line(t, cfg) if mode == "pn" else pv_line(t, cfg)
    return S._insert_variants(label + ru, variants, cfg)


def translate_text(src, cfg=None, mode="pn"):
    cfg = cfg or SK_CFG
    out = []
    for line in src.split("\n"):
        body, bid = B.ID_RE.match(line).groups()
        if body.startswith("#") and "Pavatti" in body:
            mode = "pv"
        out.append(tr(body, cfg, mode) + (bid or ""))
    return unicodedata.normalize("NFC", "\n".join(out))


# =============================================================================================
# Checks
# =============================================================================================
CROSSBOOK = [   # strings taken from the approved pi-1 … pi-5 Russian rails (book, exact substring)
    ("2", "телесный формирующий фактор; речевой формирующий фактор и формирующий фактор ума"),   # ^2-226 area
    ("2", "телесным формирующим фактором"), ("2", "речевым формирующим фактором"),
    ("2", "формирующим фактором ума"),
    ("5", "вдохи и выдохи"), ("5", "направленную мысль и удержание мысли"), ("5", "восприятие и чувство"),
    ("1", "есть направленная мысль, есть удержание мысли"),
    ("1", "Явления, связанные с умом"), ("1", "Явления с направленной мыслью и удержанием мысли"),
    ("1", "Явления без направленной мысли и без удержания мысли"),
    ("1", "На уровне с направленной мыслью и удержанием мысли"),
    ("1", "в первое медитативное погружение"), ("1", "во второе медитативное погружение"),
    ("2", "четвёртое медитативное погружение"), ("5", "у вошедшего в первое погружение"),
    ("1", "в мире чувственных желаний"), ("1", "в мире форм"), ("2", "сразу после"),
    ("5", "медитативное достижение прекращения"), ("2", "тело"), ("1", "речь"), ("1", "ум"),
]
OTHER_RU = {   # strings this builder composes that the finished pi-6 chapters already print
    "3-03-ayatanayamaka.md": [
        "у тех, кто живёт последней жизнью в мире форм и в мире без форм,",
        "у тех, кто, переродившись в мире форм и в мире без форм, достигнет окончательного угасания, когда они умирают,",
    ],
    "3-01-ayatanayamaka.md": ["В мире форм, в мире без форм: там "],
    "5-01-saccayamaka.md": ["У существ Чистых обителей, когда присутствует второй ум, и у существ без восприятия там "],
}


def check_other_ru():
    for name, strings in OTHER_RU.items():
        txt = (B.OUT_DIR / name).read_text(encoding="utf-8")
        for s in strings:
            assert s in txt, (name, s)
    # the same strings come out of this builder's units
    assert sk_intro("Rūpāvacare arūpāvacare pacchimabhavikānaṃ ye ca rūpāvacaraṃ arūpāvacaraṃ upapajjitvā "
                    "parinibbāyissanti tesaṃ cavantānaṃ") == (
        "У тех, кто живёт последней жизнью в мире форм и в мире без форм, и у тех, кто, переродившись в мире форм и "
        "в мире без форм, достигнет окончательного угасания, когда они умирают, ")
    assert sk_place_intro("Rūpāvacare arūpāvacare") == OTHER_RU["3-01-ayatanayamaka.md"][0]
    assert sk_intro("Suddhāvāsānaṃ dutiye citte vattamāne asaññasattānaṃ", True) == OTHER_RU["5-01-saccayamaka.md"][0]
    return True


def consistency_all(src, ru):
    """Identical Pāli line -> identical Russian line: within this chapter and with every finished pi-6 chapter."""
    seen = {}
    for p, r in zip(src.split("\n"), ru.split("\n")):
        pb, rb = B.ID_ANY.sub("", p).strip(), B.ID_ANY.sub("", r).strip()
        if pb:
            assert seen.setdefault(pb, rb) == rb, f"inconsistent within chapter: {pb!r}"
    bad, shared = [], 0
    for f in sorted(B.OUT_DIR.glob("*.md")):
        if f.name == CHAPTER or not (B.PALI_DIR / f.name).exists():
            continue
        for p, r in zip((B.PALI_DIR / f.name).read_text(encoding="utf-8").split("\n"),
                        f.read_text(encoding="utf-8").split("\n")):
            pb, rb = B.ID_ANY.sub("", p).strip(), B.ID_ANY.sub("", r).strip()
            if pb in seen:
                shared += 1
                if seen[pb] != rb:
                    bad.append((f.name, pb, seen[pb], rb))
    if bad:
        raise AssertionError("inconsistent with finished chapters:\n" + "\n".join(map(repr, bad[:10])))
    return shared


def probe(name, mode=None):
    """6-02 has no paṇṇattivāra: it is probed (and should be translated) with mode "pv"."""
    mode = mode or ("pn" if name == CHAPTER else "pv")
    src = (B.PALI_DIR / name).read_text(encoding="utf-8")
    ok = bad = 0
    for line in src.split("\n"):
        body, _ = B.ID_RE.match(line).groups()
        if body.startswith("#") and "Pavatti" in body:
            mode = "pv"
        try:
            tr(body, SK_CFG, mode)
            ok += 1
        except Exception as e:   # noqa: BLE001
            bad += 1
            print("-- ", type(e).__name__, str(e)[:200])
    print(f"{name}: {ok} lines translated, {bad} not covered")


def main():
    B.check_crossbook()
    A.check_crossbook()
    A.check_crossbook(CROSSBOOK)
    C.check_crossbook_c()
    check_other_ru()
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    SLIP_LOG.clear()
    ru = translate_text(src)
    B.check_pair(src, ru, CHAPTER)
    shared = consistency_all(src, ru)
    with open(B.OUT_DIR / CHAPTER, "w", encoding="utf-8", newline="\n") as f:
        f.write(ru)
    print("written", B.OUT_DIR / CHAPTER, "lines", len(ru.split("\n")))
    for s in sorted(set(SLIP_LOG)):
        print("slip:", s)
    print(f"cross-book asserts OK; per-line checks OK; consistency OK ({shared} identical Pāli lines in other chapters)")


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "--probe":
        probe(sys.argv[2])
    else:
        main()
