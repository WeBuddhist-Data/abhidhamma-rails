"""Russian plain zero-shot of pi-6 (Yamaka): chapter 2-01-khandhayamaka.md.

FRAME-SETTER for family A (paṇṇattivāra) and family B (pavattivāra). Later chapters import this module
(importlib.import_module("build_2-01_ru")) and substitute their own members into the frames below.

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_2-01_ru.py
Import: importing never writes any file; only __main__ builds.

Exposed for reuse
  Family A (paṇṇattivāra)
    N(...)                      Russian noun phrase with nom / instr / gen and agreement class (m f n pl)
    PADA_POS, PADA_NEG          the "X Y?" / "na X na Y?" naming questions (padasodhana, mūlacakka, suddha)
    ANS_X_NOT_K, ANS_K_BOTH, ANS_NOT_K_BUT_X, ANS_APART_NEITHER, ANS_REST_NOT, APART, APART_GROUP
                                the answer sentences of the paṇṇatti niddesa
    PANNATTI_UDDESAVARO, PANNATTI_NIDDESAVARO   closing lines
    pada_question(body, lex), pannatti_sentence(s, lex, qual)
  Family B (pavattivāra)
    PV_VERBS, verb(...)         uppajjati / nirujjhati in present, past, future (+ agreement)
    PV_PRED, PV_Q, PV_KHA       predicate «возникает X» and the yassa / yattha / yassa yattha questions
                                (shape imported from build_7-01_ru: Q_PERSON, Q_PLACE, Q_PERSON_PLACE, KHA_PREFIX)
    PV_TAM, place_intro()       partial answers use C.ANSWER_INTRO_PLACE, C.NO_CA_FRAME, C.NO_CA_NEG_FRAME,
                                C.BOTH_FRAME, C.RES from build_7-01_ru
    PV_SHORT                    Āmantā / Natthi; bare verb answers via verb()
    PLANES, PERSON_UNITS, person_intro(), place_intro()   beings and planes in answers
    pv_question(body, subj), pv_sentence(s, subj, planes)
  Generic
    VARIANT_RE / variant_ru()   «[вариант чтения (Sī., Syā.): …, так же и далее]»
    translate_text(src, cfg)    whole-chapter translation driven by a config dict (see KH_CFG)
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

CHAPTER = "2-01-khandhayamaka.md"
cap = B.cap


def N(nom, instr, gen, g="f"):
    """Russian noun phrase. g = m / f / n / pl: agreement for the copula and for past-tense verbs."""
    return {"nom": nom, "instr": instr, "gen": gen, "g": g, "cop": "являются" if g == "pl" else "является"}


# =============================================================================================
# Members of the Khandhayamaka (names from pi-2 Khandhavibhaṅga Russian, asserted below)
# =============================================================================================
# Bare words in the paṇṇattivāra: rūpa here is "whatever is called rūpa" (aṭṭhakathā: yaṃkiñci rūpanti
# vuccati), incl. piyarūpa sātarūpa, so the bare word is «форма»; the aggregate keeps the pi-2 name.
KH_X = {
    "rūpa": N("форма", "формой", "формы", "f"),
    "vedanā": N("чувство", "чувством", "чувства", "n"),
    "saññā": N("восприятие", "восприятием", "восприятия", "n"),
    "saṅkhāra": N("формирующие факторы", "формирующими факторами", "формирующих факторов", "pl"),
    "viññāṇa": N("сознание", "сознанием", "сознания", "n"),
}
KH_GENMOD = {"rūpa": "материальной формы", "vedanā": "чувств", "saññā": "восприятия",
             "saṅkhāra": "формирующих факторов", "viññāṇa": "сознания"}
KH_K = {m: N("совокупность " + gm, "совокупностью " + gm, "совокупности " + gm, "f") for m, gm in KH_GENMOD.items()}
KH_G_SG = N("совокупность", "совокупностью", "совокупности", "f")          # khandho
KH_G_PL = N("совокупности", "совокупностями", "совокупностей", "pl")       # khandhā
KH_X_FORMS = {"rūpa": ["rūpaṃ"], "vedanā": ["vedanā", "vedanaṃ"], "saññā": ["saññā", "saññaṃ"],
              "saṅkhāra": ["saṅkhārā", "saṅkhāre"], "viññāṇa": ["viññāṇaṃ"]}

KH_LEX = {}
for _m, _forms in KH_X_FORMS.items():
    for _f in _forms:
        KH_LEX[_f] = KH_X[_m]
    KH_LEX[_m + "kkhandho"] = KH_K[_m]
    KH_LEX[_m + "kkhandhaṃ"] = KH_K[_m]
KH_LEX.update({"khandho": KH_G_SG, "khandhaṃ": KH_G_SG, "khandhā": KH_G_PL, "khandhe": KH_G_PL})
KH_PV_SUBJ = {_m + "kkhandho": KH_K[_m] for _m in KH_X}        # pavattivāra subjects

# Pañcakkhandhā – rūpakkhandho, … (identical Pāli in pi-2 2-1: copied verbatim, asserted)
KH_PANCAKKHANDHA = ("Пять совокупностей – совокупность материальной формы, совокупность чувств, совокупность "
                    "восприятия, совокупность формирующих факторов и совокупность сознания.")

# =============================================================================================
# FAMILY A: paṇṇattivāra
# =============================================================================================
# (Ka) rūpaṃ rūpakkhandho(ti)?  /  (Kha) khandhā vedanākkhandho?  /  (Ka) rūpaṃ khandho?
PADA_POS = "{a_nom} {a_cop} {b_instr}?"                      # «Форма является совокупностью материальной формы?»
# (Ka) na rūpaṃ na rūpakkhandho(ti)?
PADA_NEG = "То, что не является {a_instr}, не является {b_instr}?"
# Answers (one Pāli sentence -> one Russian sentence)
ANS_X_NOT_K = "{q} {q_cop} {x_instr}, но не {q_cop} {k_instr}."        # Q X, na K.
ANS_K_BOTH = "{k_nom} {k_cop} и {x_instr}, и {k2_instr}."              # K Xñceva K ca.
ANS_NOT_K_BUT_X = "{q} не {q_cop} {k_instr}, но {q_cop} {x_instr}."    # Q na K, X.
ANS_APART_NEITHER = "Кроме {a_gen} и {b_gen}, остальное не является ни {x_instr}, ни {y_instr}."
#                                   # Añca Bñca ṭhapetvā avasesā na ceva X na ca Y.
ANS_REST_NOT = "Остальные {g_nom} не {g_cop} {k_instr}."               # Avasesā khandhā na K.
APART = "Кроме {a_gen}, остальное"                                     # A ṭhapetvā avasesā (sg)
APART_GROUP = "Кроме {a_gen}, остальные {g_nom}"                       # A ṭhapetvā avasesā khandhā (pl)
PANNATTI_UDDESAVARO = "Раздел перечня обозначений."                    # Paṇṇattiuddesavāro.
PANNATTI_NIDDESAVARO = "Раздел разъяснения обозначений."               # Paṇṇattiniddesavāro.
# Chapter-specific qualifiers (Khandha): Q -> (Russian, agreement)
KH_QUAL = {
    "piyarūpaṃ sātarūpaṃ": ("Привлекательная форма, отрадная форма", "f"),
    "diṭṭhisaññā": ("Восприятие-воззрение", "n"),
}


def lex_get(w, lex):
    lw = w[0].lower() + w[1:]
    if lw in lex:
        return lex[lw]
    for suf, rep in (("nti", "ṃ"), ("ti", "")):           # quoting -ti
        if lw.endswith(suf) and lw[: -len(suf)] + rep in lex:
            return lex[lw[: -len(suf)] + rep]
    raise KeyError(f"not in lexicon: {w!r}")


def pada_question(body, lex):
    """'rūpaṃ rūpakkhandho(ti)' / 'na rūpaṃ na rūpakkhandho(ti)' -> Russian question (with '?')."""
    t = body.split()
    if len(t) == 2:
        a, b = lex_get(t[0], lex), lex_get(t[1], lex)
        return PADA_POS.format(a_nom=cap(a["nom"]), a_cop=a["cop"], b_instr=b["instr"])
    if len(t) == 4 and t[0] == "na" and t[2] == "na":
        a, b = lex_get(t[1], lex), lex_get(t[3], lex)
        return PADA_NEG.format(a_instr=a["instr"], b_instr=b["instr"])
    raise ValueError(f"paṇṇatti question not parsed: {body!r}")


def _norm(s):
    s = re.sub(r"ñceva\b", "ṃ ceva", s)
    return re.sub(r"ñca\b", "ṃ ca", s)


def qualifier(q, lex, qual):
    lq = q[0].lower() + q[1:]
    if lq in qual:
        return qual[lq]
    m = re.fullmatch(r"(\S+) ṭhapetvā avasesā (\S+)", lq)
    if m:
        g = lex_get(m.group(2), lex)
        return APART_GROUP.format(a_gen=lex_get(m.group(1), lex)["gen"], g_nom=g["nom"]), g["g"]
    m = re.fullmatch(r"(\S+) ṭhapetvā avasesā", lq)
    if m:
        return APART.format(a_gen=lex_get(m.group(1), lex)["gen"]), "n"
    raise KeyError(f"qualifier not parsed: {q!r}")


def _cop(g):
    return "являются" if g == "pl" else "является"


def pannatti_sentence(s, lex, qual):
    """One Pāli answer sentence of the paṇṇatti niddesa (final '.' removed) -> Russian sentence."""
    s = _norm(s)
    m = re.fullmatch(r"(\S+) ca (\S+) ca ṭhapetvā avasesā na ceva (\S+) na ca (\S+)", s)
    if m:
        a, b, x, y = (lex_get(m.group(i), lex) for i in range(1, 5))
        return ANS_APART_NEITHER.format(a_gen=a["gen"], b_gen=b["gen"], x_instr=x["instr"], y_instr=y["instr"])
    m = re.fullmatch(r"[Aa]vasesā (\S+) na (\S+)", s)
    if m:
        g, k = lex_get(m.group(1), lex), lex_get(m.group(2), lex)
        return ANS_REST_NOT.format(g_nom=g["nom"], g_cop=g["cop"], k_instr=k["instr"])
    m = re.fullmatch(r"(\S+) (\S+) ceva (\S+) ca", s)
    if m:
        k, x, k2 = (lex_get(m.group(i), lex) for i in range(1, 4))
        return ANS_K_BOTH.format(k_nom=cap(k["nom"]), k_cop=k["cop"], x_instr=x["instr"], k2_instr=k2["instr"])
    m = re.fullmatch(r"(.+) (\S+), na (\S+)", s)
    if m:
        q, g = qualifier(m.group(1), lex, qual)
        x, k = lex_get(m.group(2), lex), lex_get(m.group(3), lex)
        return ANS_X_NOT_K.format(q=q, q_cop=_cop(g), x_instr=x["instr"], k_instr=k["instr"])
    m = re.fullmatch(r"(.+) na (\S+), (\S+)", s)
    if m:
        q, g = qualifier(m.group(1), lex, qual)
        k, x = lex_get(m.group(2), lex), lex_get(m.group(3), lex)
        return ANS_NOT_K_BUT_X.format(q=q, q_cop=_cop(g), k_instr=k["instr"], x_instr=x["instr"])
    raise ValueError(f"paṇṇatti answer not parsed: {s!r}")


# =============================================================================================
# FAMILY B: pavattivāra
# =============================================================================================
# Tenses: present = present; past (-ittha) = imperfective past («возникала»: "has (ever) arisen");
# future (-issati) = perfective future («возникнет»). Agreement: present/future sg|pl, past m|f|n|pl.
PV_VERBS = {
    "uppajjati": {"sg": "возникает", "pl": "возникают"},
    "uppajjittha": {"m": "возникал", "f": "возникала", "n": "возникало", "pl": "возникали"},
    "uppajjissati": {"sg": "возникнет", "pl": "возникнут"},
    "nirujjhati": {"sg": "прекращается", "pl": "прекращаются"},
    "nirujjhittha": {"m": "прекращался", "f": "прекращалась", "n": "прекращалось", "pl": "прекращались"},
    "nirujjhissati": {"sg": "прекратится", "pl": "прекратятся"},
}
PV_VERB_SLIPS = {"nirujjhattha": "nirujjhittha"}   # plain spelling slips, rendered as meant (reported)
V_RE = "(?:" + "|".join(sorted(list(PV_VERBS) + list(PV_VERB_SLIPS), key=len, reverse=True)) + ")"
# quoted forms at the end of a question: uppajjatīti, uppajjitthāti, uppajjissatīti …
PV_VERB_TI = {}
for _v in PV_VERBS:
    PV_VERB_TI[(_v[:-1] + "īti") if _v.endswith("ti") else (_v[:-1] + "āti")] = _v
VTI_RE = "(?:" + "|".join(sorted(PV_VERB_TI, key=len, reverse=True)) + ")"


def verb(v, g, neg=False):
    """Pāli verb form (no negation) + agreement class of the subject -> Russian."""
    if v in PV_VERB_SLIPS:
        SLIP_LOG.append(f"verb slip {v} rendered as {PV_VERB_SLIPS[v]}")
    forms = PV_VERBS[PV_VERB_SLIPS.get(v, v)]
    f = forms.get(g) or forms["pl" if g == "pl" else "sg"]
    return ("не " if neg else "") + f


# Person / place shape: imported from the family-C setter (build_7-01_ru, coordinator rule 2026-11-27) so that
# families B and C agree byte for byte; this module only puts its verbs and subjects into the slots.
C = importlib.import_module("build_7-01_ru")
PV_PRED = "{v} {x}"                # predicate «возникает совокупность материальной формы» (verb first, as 7-01)
PV_Q = {"yassa": C.Q_PERSON, "yattha": C.Q_PLACE, "yassa yattha": C.Q_PERSON_PLACE}   # «У кого …, у того …?» …
PV_KHA = C.KHA_PREFIX              # vā pana: «А у кого …», «А где …»
PV_SHORT = {"Āmantā": C.AMANTA, "Natthi": C.NATTHI}   # Да. / Такого нет.
# Partial answers.
# S1 "<who> tesaṃ [tattha] X V1, no ca tesaṃ [tattha] Y V2."
#   person: «У тех, кто …, [там ]возникает X, но у них [там ]не возникает Y.»
#   place:  «Среди существ без восприятия: там возникает X, но там не возникает Y.»   (C.ANSWER_INTRO_PLACE)
#   "no ca … Y nuppajjati" (double negative): C.NO_CA_NEG_FRAME «, но не так, что у них не возникает Y»
# S2 "<who> tesaṃ [tattha] X ca V1 Y ca V2." -> intro + C.BOTH_FRAME «и возникает X, и возникает Y».
PV_TAM = C.RES["tattha"] + " "     # tattha after a person intro («там »); a place intro takes C.ANSWER_INTRO_PLACE
# Negatives (coordinator rule 2026-11-27, replaces 7-01's «, но не так, что …»):
PV_NO_CA_POS_FRAME = ", но {res} {pred}"          # "…, no ca tesaṃ Y nuppajjati" = «…, но у них возникает Y»
PV_NEITHER_FRAME = "не {v} ни {x}, ни {y}"        # "X ca nuppajjati Y ca nuppajjati" = «не возникает ни X, ни Y»
PV_NEG_MIXED_FRAME = "не {v1} {x} и не {v2} {y}"  # different tenses: "X ca nuppajjati Y ca nuppajjittha"

# Planes. "in": where one is reborn / dies / lives; "beings": genitive plural of the beings of that plane.
PLANES = {
    "asaññasatt": {"in": "среди существ без восприятия", "beings": "существ без восприятия"},
    "pañcavokār": {"in": "в существовании с пятью составляющими", "beings": "существ с пятью составляющими"},
    "catuvokār": {"in": "в существовании с четырьмя составляющими", "beings": "существ с четырьмя составляющими"},
    "ekavokār": {"in": "в существовании с одной составляющей", "beings": "существ с одной составляющей"},
    "arūp": {"in": "в мире без форм", "beings": "существ мира без форм"},
    "suddhāvās": {"in": "в Чистых обителях", "beings": "существ Чистых обителей"},
}
# Person units inside an answer intro (genitive after «у»). {P} = a plane stem; rel = relative clause
# (needs a closing comma). Order matters: longer patterns first.
PERSON_UNITS = [
    (r"ye {P}aṃ upapajjitvā parinibbāyissanti", "тех, кто, переродившись {in1}, достигнет окончательного угасания", True),
    (r"sabbesaṃ cavantānaṃ", "всех, кто умирает", True),
    (r"sabbesaṃ upapajjantānaṃ", "всех, кто перерождается", True),
    (r"pacchimabhavikānaṃ {P}aṃ upapajjantānaṃ", "тех, кто в последний раз перерождается {in1}", True),
    (r"pacchimabhavikānaṃ upapajjantānaṃ", "тех, кто перерождается в последний раз", True),
    (r"{P}e pacchimabhavikānaṃ", "тех, кто живёт последней жизнью {in1}", True),
    (r"pacchimabhavikānaṃ", "тех, кто живёт последней жизнью", True),
    (r"{P}e parinibbantānaṃ", "тех, кто достигает окончательного угасания {in1}", True),
    (r"parinibbantānaṃ", "тех, кто достигает окончательного угасания", True),
    (r"{P}ā {P}ā cavantānaṃ", "тех, кто умирает {in1} и {in2}", True),
    (r"{P}ā cavantānaṃ", "тех, кто умирает {in1}", True),
    (r"{P}aṃ {P}aṃ upapajjantānaṃ", "тех, кто перерождается {in1} и {in2}", True),
    (r"{P}aṃ upapajjantānaṃ", "тех, кто перерождается {in1}", True),
    (r"{P}ānaṃ {P}ānaṃ", "{b1} и {b2}", False),
    (r"{P}ānaṃ", "{b1}", False),
    (r"itaresaṃ", "остальных", False),       # merges with the next unit: «остальных, кто …» / «остальных существ …»
]
ITARESAM = "остальных"


def _plane_re(planes):
    return "(" + "|".join(sorted(planes, key=len, reverse=True)) + ")"


def person_units(intro, planes=PLANES):
    s = intro[0].lower() + intro[1:]
    pre = _plane_re(planes)
    units, pos = [], 0
    while pos < len(s):
        for rx, ru, rel in PERSON_UNITS:
            m = re.compile(rx.replace("{P}", pre)).match(s, pos)
            if m and (m.end() == len(s) or s[m.end()] == " "):
                g = [planes[x] for x in m.groups()] + [{"in": "", "beings": ""}] * 2
                units.append([ru.format(in1=g[0]["in"], in2=g[1]["in"], b1=g[0]["beings"], b2=g[1]["beings"]), rel])
                pos = m.end() + 1
                break
        else:
            raise ValueError(f"person intro not parsed at {s[pos:]!r} in {intro!r}")
    out = []
    i = 0
    while i < len(units):
        t, rel = units[i]
        if t == ITARESAM and i + 1 < len(units):
            nt, nrel = units[i + 1]
            t = ITARESAM + nt[3:] if nt.startswith("тех, кто") else f"{ITARESAM} {nt}"
            rel = nrel
            i += 1
        out.append([t, rel])
        i += 1
    return out


def person_intro(intro, planes=PLANES):
    """'Asaññasattaṃ upapajjantānaṃ' -> «У тех, кто перерождается среди существ без восприятия,» (+ space)."""
    units = person_units(intro, planes)
    s = "У " + units[0][0]
    for i in range(1, len(units)):
        last = i == len(units) - 1
        sep = ((", и " if units[i - 1][1] else " и ") if last else ", ")
        s += sep + "у " + units[i][0]
    return s + ("," if units[-1][1] else "") + " "


def place_intro(intro, planes=PLANES):
    """'Asaññasatte' (+ tattha) -> «Среди существ без восприятия: там » (C.ANSWER_INTRO_PLACE)."""
    m = re.fullmatch(_plane_re(planes) + "e", intro[0].lower() + intro[1:])
    if not m:
        raise ValueError(f"place intro not parsed: {intro!r}")
    return C.ANSWER_INTRO_PLACE.format(loci=cap(planes[m.group(1)]["in"]), res=C.RES["tattha"])


_T = r"(?P<{n}>tesaṃ tattha|tesaṃ|tattha)"
PV_S1_RE = re.compile(r"(?P<intro>.+?) " + _T.format(n="t1") + r" (?P<x>\S+) (?P<n1>na |n)?(?P<v1>" + V_RE
                      + r"), no ca " + _T.format(n="t2") + r" (?P<y>\S+) (?P<n2>na |n)?(?P<v2>" + V_RE + r")")
PV_S2_RE = re.compile(r"(?P<intro>.+?) " + _T.format(n="t1") + r" (?P<x>\S+) ca (?P<n1>na |n)?(?P<v1>" + V_RE
                      + r") (?P<y>\S+) ca (?P<n2>na |n)?(?P<v2>" + V_RE + r")")


def pv_sentence(s, subj, planes=PLANES, y_ctx=None):
    """One Pāli pavatti answer sentence (final '.' removed) -> Russian sentence (with '.')."""
    if s in PV_SHORT:
        return PV_SHORT[s]
    lv = s[0].lower() + s[1:]
    if lv in PV_VERBS or lv in PV_VERB_SLIPS:                       # Uppajjati. / Nirujjhittha. …
        return cap(verb(lv, y_ctx["g"] if y_ctx else "sg")) + "."
    for rx, kind in ((PV_S1_RE, 1), (PV_S2_RE, 2)):
        m = rx.fullmatch(s)
        if not m:
            continue
        person = m.group("t1").startswith("tesaṃ")
        if person:
            head = person_intro(m.group("intro"), planes) + (PV_TAM if "tattha" in m.group("t1") else "")
        else:
            head = place_intro(m.group("intro"), planes)
        x, y = subj[m.group("x")], subj[m.group("y")]
        p1 = PV_PRED.format(v=verb(m.group("v1"), x["g"], bool(m.group("n1"))), x=x["nom"])
        if kind == 1:
            res = C.RES[m.group("t2")]
            # "no ca": the question's predicate is denied for Y, so the negation flips (coordinator "Negatives")
            v2 = verb(m.group("v2"), y["g"], not m.group("n2"))
            tail = (PV_NO_CA_POS_FRAME if m.group("n2") else C.NO_CA_FRAME).format(
                res=res, **{("pred" if m.group("n2") else "neg_pred"): PV_PRED.format(v=v2, x=y["nom"])})
            return cap(head + p1 + tail) + "."
        if m.group("n1") and m.group("n2"):   # "X ca nuppajjati Y ca nuppajjati"
            f1, f2 = verb(m.group("v1"), x["g"]), verb(m.group("v2"), y["g"])
            if f1 == f2:
                both = PV_NEITHER_FRAME.format(v=f1, x=x["nom"], y=y["nom"])
            else:                             # mixed tenses: two verbs, no «ни … ни»
                both = PV_NEG_MIXED_FRAME.format(v1=f1, x=x["nom"], v2=f2, y=y["nom"])
            return cap(head + both) + "."
        p2 = PV_PRED.format(v=verb(m.group("v2"), y["g"], bool(m.group("n2"))), x=y["nom"])
        return cap(head + C.BOTH_FRAME.format(p1=p1, p2=p2)) + "."
    raise ValueError(f"pavatti answer not parsed: {s!r}")


PV_Q_RE = re.compile(r"(?P<rel>yassa vā pana yattha|yassa yattha|yassa vā pana|yassa|yattha vā pana|yattha) "
                     r"(?P<x>\S+) (?P<n1>na |n)?(?P<v1>" + V_RE + r") (?P<cor>tassa tattha|tassa|tattha) "
                     r"(?P<y>\S+) (?P<n2>na |n)?(?P<v2>" + VTI_RE + r")")


def pv_question(body, subj):
    """'yassa rūpakkhandho uppajjati tassa vedanākkhandho uppajjatīti' -> (Russian question, y noun)."""
    m = PV_Q_RE.fullmatch(body)
    if not m:
        raise ValueError(f"pavatti question not parsed: {body!r}")
    rel = m.group("rel")
    kind = "yassa yattha" if ("yassa" in rel and "yattha" in rel) else ("yassa" if "yassa" in rel else "yattha")
    x, y = subj[m.group("x")], subj[m.group("y")]
    p1 = PV_PRED.format(v=verb(m.group("v1"), x["g"], bool(m.group("n1"))), x=x["nom"])
    p2 = PV_PRED.format(v=verb(PV_VERB_TI[m.group("v2")], y["g"], bool(m.group("n2"))), x=y["nom"])
    q = PV_Q[kind].format(p1=p1, p2=p2)
    return (PV_KHA + C.lower1(q) if "vā pana" in rel else q), y


# =============================================================================================
# Variants
# =============================================================================================
VARIANT_RE = re.compile(r" \[([^\]]+)\]")
VARIANT_KIND_DEFAULT = "чтения"


def variant_ru(content, kind=VARIANT_KIND_DEFAULT):
    """'avasesā khandhā khandhā (syā.) evamuparipi' -> «[вариант чтения (Syā.): avasesā khandhā khandhā, так же и далее]»."""
    m = re.fullmatch(r"(.+?) \(([^)]+)\)( evamuparipi)?", content)
    if not m:
        raise ValueError(f"variant not parsed: {content!r}")
    sig = ", ".join(cap(x.strip()) + "." for x in m.group(2).split(".") if x.strip())
    return f"[вариант {kind} ({sig}): {m.group(1)}{', так же и далее' if m.group(3) else ''}]"


# =============================================================================================
# Line / chapter translation
# =============================================================================================
QA_RE = re.compile(r"\((Ka|Kha)\) (.+?)(\?|\.)(?: (.+))?")
HEAD_RE = re.compile(r"(#+) (.+)")
LABEL_RE = re.compile(r"\((\w+)\) (.+)")
VARO_NITTHITO_RE = re.compile(r"(\w+) niṭṭhito\.")
SLIP_LOG = []


def heading(text):
    m = HEAD_RE.fullmatch(text)
    hashes, body = m.groups()
    if body in B.YAMAKA_TITLES:
        return f"{hashes} {B.YAMAKA_TITLES[body]}"
    if body in B.SECTION_HEADINGS:
        return f"{hashes} {C.heading_case(B.SECTION_HEADINGS[body])}"
    m = LABEL_RE.fullmatch(body)
    if m:
        lab = m.group(1)
        lab_ru = lab if lab.isdigit() else B.LETTERS[lab]
        return f"{hashes} ({lab_ru}) {C.heading_case(B.SECTION_HEADINGS[m.group(2)])}"
    raise ValueError(f"heading not parsed: {text!r}")


def answer_sentences(text, cfg, y_ctx=None):
    variants = VARIANT_RE.findall(text)
    plain = VARIANT_RE.sub("", text)
    out = []
    for s in re.split(r"(?<=\.) (?=\S)", plain.strip()):
        assert s.endswith("."), s
        body = s[:-1]
        if body in PV_SHORT or body.startswith(("Ye ", "Sabbesaṃ")) or " tesaṃ " in body or " tattha " in body \
                or body[0].lower() + body[1:] in PV_VERBS or body[0].lower() + body[1:] in PV_VERB_SLIPS:
            out.append(pv_sentence(body, cfg["pv_subj"], cfg["planes"], y_ctx))
        else:
            out.append(pannatti_sentence(body, cfg["lex"], cfg["qual"]))
    ru = " ".join(out)
    for v in variants:
        anchor = cfg["variant_anchors"][v]
        assert anchor in ru, (anchor, ru)
        ru = ru.replace(anchor, anchor + " " + variant_ru(v, cfg.get("variant_kind", {}).get(v, VARIANT_KIND_DEFAULT)), 1)
    return ru


def tr(text, cfg):
    """Translate one Pāli line (block ID removed)."""
    if not text.strip():
        return ""
    if text in cfg["fixed"]:
        return cfg["fixed"][text]
    if text in B.FIXED:
        return B.FIXED[text]
    if text.startswith("#"):
        return heading(text)
    m = VARO_NITTHITO_RE.fullmatch(text)
    if m and m.group(1) in B.SECTION_HEADINGS:
        return f"{B.SECTION_HEADINGS[m.group(1)]} {B.NITTHITO}."
    m = QA_RE.fullmatch(text)
    if m:
        lab, body, punct, ans = m.groups()
        if punct == ".":
            SLIP_LOG.append(f"question ends with '.' (rendered '?'): {text}")
        if body.startswith(("yassa", "yattha")):
            q, y = pv_question(body, cfg["pv_subj"])
            if lab == "Ka" and " vā pana " in body:
                SLIP_LOG.append(f"label (Ka) on a 'vā pana' question (kept as written): {text}")
        else:
            q, y = pada_question(body, cfg["lex"]), None
        out = f"({B.LETTERS[lab]}) {q}"
        return out + (" " + answer_sentences(ans, cfg, y) if ans else "")
    return answer_sentences(text, cfg)


def translate_text(src, cfg):
    out = []
    for line in src.split("\n"):
        body, bid = B.ID_RE.match(line).groups()
        out.append(tr(body, cfg) + (bid or ""))
    return unicodedata.normalize("NFC", "\n".join(out))


KH_CFG = {
    "lex": KH_LEX,
    "qual": KH_QUAL,
    "pv_subj": KH_PV_SUBJ,
    "planes": PLANES,
    "fixed": {
        "Pañcakkhandhā – rūpakkhandho, vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho.":
            KH_PANCAKKHANDHA,
        "Paṇṇattiuddesavāro.": PANNATTI_UDDESAVARO,
        "Paṇṇattiniddesavāro.": PANNATTI_NIDDESAVARO,
    },
    "variant_anchors": {
        "avasesā saṅkhārā saṅkhārā (syā.)": "остальное является формирующими факторами",
        "avasesā khandhā khandhā (syā.) evamuparipi": "Остальные совокупности",
        "pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ (sī. syā.)": "У тех, кто перерождается в последний раз",
    },
}

# Strings taken from the approved pi-1 … pi-5 Russian rails (book, exact substring)
CROSSBOOK = [
    ("2", KH_PANCAKKHANDHA),
    ("2", "совокупность материальной формы"), ("2", "совокупность чувств"), ("2", "совокупность восприятия"),
    ("2", "совокупность формирующих факторов"), ("2", "совокупность сознания"),
    ("2", "существование с пятью составляющими"), ("2", "существование с четырьмя составляющими"),
    ("2", "существование с одной составляющей"), ("2", "существование в мире без форм"),
    ("2", "Существа без восприятия"), ("2", "достигают окончательного угасания"),
    ("4", "Достигающий окончательного угасания"), ("2", "не умирают"), ("2", "перерождаются"),
    ("2", "в момент перерождения"), ("2", "так же и далее"), ("2", "привлекательно и отрадно"),
    ("1", "воззрение"), ("2", "кроме"), ("1", "Остальные"), ("5", "Да."), ("1", "чувство"), ("1", "восприятие"),
    ("1", "сознание"), ("1", "форма"),
]


def check_crossbook(pairs=CROSSBOOK):
    cache, missing = {}, []
    for b, s in pairs:
        if b not in cache:
            cache[b] = "\n".join(p.read_text(encoding="utf-8") for p in sorted(B.RAILS[b].glob("*.md")))
        if s not in cache[b]:
            missing.append((b, s))
    if missing:
        raise AssertionError(f"cross-book strings not found in the pi-1..5 rails: {missing}")
    return True


def consistency(pairs, seen=None):
    """pairs: [(pali_text, russian_text)]; identical Pāli line -> identical Russian line."""
    seen = {} if seen is None else seen
    for src, ru in pairs:
        for p, r in zip(src.split("\n"), ru.split("\n")):
            pb, rb = B.ID_ANY.sub("", p).strip(), B.ID_ANY.sub("", r).strip()
            if pb in seen:
                assert seen[pb] == rb, f"inconsistent: {pb!r}\n  {seen[pb]!r}\n  {rb!r}"
            seen[pb] = rb
    return seen


def main():
    B.check_crossbook()
    check_crossbook()
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    ru = translate_text(src, KH_CFG)
    B.check_pair(src, ru, CHAPTER)
    sample = [((B.PALI_DIR / n).read_text(encoding="utf-8"), (B.OUT_DIR / n).read_text(encoding="utf-8"))
              for n in B.SAMPLE_FILES]
    consistency(sample + [(src, ru)])
    with open(B.OUT_DIR / CHAPTER, "w", encoding="utf-8", newline="\n") as f:
        f.write(ru)
    print("written", B.OUT_DIR / CHAPTER, "lines", len(ru.split("\n")))
    for s in SLIP_LOG:
        print("slip:", s)
    print("cross-book asserts OK; per-line checks OK; consistency OK")


if __name__ == "__main__":
    main()
