"""Russian plain zero-shot of pi-6 (Yamaka): chapter 2-02-khandhayamaka.md.

Families A and B come from build_2-01_ru (imported, never edited); the person / place shape from build_7-01_ru.
FRAME-SETTER for family E (pariññāvāra, parijānāti frames): every frame is listed in notes-2-02.md.

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_2-02_ru.py
Import: E = importlib.import_module("build_2-02_ru")   (importing never writes any file; only __main__ builds)

Exposed for reuse
  Family B additions
    PERSON_UNITS_2_02, extra_units()    "ye ca Xaṃ upapajjitvā parinibbāyissanti [tesaṃ cavantānaṃ]" person units;
                                        `with extra_units(): A.translate_text(...)` adds them to build_2-01_ru only
                                        for the duration of the block (2-01's own output is unchanged: asserted)
    PV_ABBR_RE, pv_abbr()               "Yattha X V…pe…." / "Yattha X V (yatthakaṃ paripuṇṇaṃ kātabbaṃ)."
    PAVATTIVARO, VIBHAJITABBAM_FRAME, YATTHAKAM_PARIPUNNAM
  Family E (pariññāvāra)
    PJ_FORMS, PJ_RU, pj_pred()          parijānāti / parijānanti / parijānittha / parijānissati / parijānissanti
    PJ_Q_RE, pj_question(body, obj)     "yo X parijānāti so Y parijānātīti" -> «Кто полностью понимает X, тот …?»
    PJ_SUBJ_UNITS, PJ_GEN, pj_subject() the persons of the answers (архат, обладающий высшим путём, …)
    PJ_S1_RE, PJ_S2_RE, pj_sentence()   partial answers (no ca …; X ca … Y ca …)
    pj_line(text, cfg)                  one pariññāvāra line (question + answers, or answers only)
  Generic
    SLIPS, preprocess()                 plain slips of this chapter, rendered as meant (logged)
    tr(text, cfg), translate_text(src, cfg)
"""
import contextlib
import importlib
import pathlib
import re
import sys
import unicodedata

HERE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru")
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import build_sample_ru as B  # noqa: E402

A = importlib.import_module("build_2-01_ru")   # families A + B (frame-setter)
C = importlib.import_module("build_7-01_ru")   # person / place shape, Q_WHO, NO, VARO_CLOSING

CHAPTER = "2-02-khandhayamaka.md"
PREV_CHAPTER = "2-01-khandhayamaka.md"
cap = B.cap
SLIP_LOG = []

# =============================================================================================
# Family B additions (pavattivāra)
# =============================================================================================
# "Pacchimabhavikānaṃ arūpaṃ upapajjantānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ tesaṃ …"
# The unit wording copies 2-01's "ye {P}aṃ upapajjitvā parinibbāyissanti"; "ca" is the «и» of the person list;
# "tesaṃ cavantānaṃ" (of them, dying) = «когда они умирают» (cavati = умирать, as 2-01).
PERSON_UNITS_2_02 = [
    (r"ye ca {P}aṃ upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ",
     "тех, кто, переродившись {in1}, достигнет окончательного угасания, когда они умирают", True),
    (r"ye ca {P}aṃ upapajjitvā parinibbāyissanti",
     "тех, кто, переродившись {in1}, достигнет окончательного угасания", True),
]


@contextlib.contextmanager
def extra_units(M=A, units=PERSON_UNITS_2_02):
    """Prepend the extra person units to build_2-01_ru.PERSON_UNITS for the duration of the block only."""
    old = list(M.PERSON_UNITS)
    M.PERSON_UNITS[:0] = [u for u in units if u not in M.PERSON_UNITS]
    try:
        yield
    finally:
        M.PERSON_UNITS[:] = old


# "Pavattivāro niṭṭhito." The approved heading «Раздел о протекании» is the head of "Pavattivāro 1. uppādavāro".
PAVATTIVARO = "Раздел о протекании"
assert B.SECTION_HEADINGS["Pavattivāro 1. uppādavāro"].startswith(PAVATTIVARO + " 1. ")

# Abbreviated place sections: "Yattha rūpakkhandho nirujjhati…pe…." / "… (yatthakaṃ paripuṇṇaṃ kātabbaṃ)."
PV_ABBR_HEAD = C.Q_PLACE.split(",")[0]                       # «Где {p1}» (first clause of the yattha question)
YATTHAKAM_PARIPUNNAM = "раздел с «где» следует изложить полностью"   # yatthakaṃ paripuṇṇaṃ kātabbaṃ
PV_ABBR_RE = re.compile(r"Yattha (?P<x>\S+) (?P<n>na |n)?(?P<v>" + A.V_RE + r")"
                        r"(?P<tail>…pe…\.| \(yatthakaṃ paripuṇṇaṃ kātabbaṃ\)\.)")


def pv_abbr(text, subj):
    m = PV_ABBR_RE.fullmatch(text)
    if not m:
        return None
    x = subj[m.group("x")]
    head = PV_ABBR_HEAD.format(p1=A.PV_PRED.format(v=A.verb(m.group("v"), x["g"], bool(m.group("n"))), x=x["nom"]))
    return head + ("…" if m.group("tail").startswith("…") else f" ({YATTHAKAM_PARIPUNNAM}).")


# "(Yathā uppādavāre paccuppannātītaṃ vibhattaṃ tathā idha vibhajitabbaṃ)." — pi-2 1-khandhavibhango
# "(Yathā rūpakaṇḍe vibhattaṃ, tathā idha vibhajitabbaṃ.)" = «(Как разобрано в разделе о материальной форме,
# так же следует разбирать и здесь.)»: same frame, the Pāli's ")." kept.
VIBHAJITABBAM_FRAME = "(Как {where} разобран {what}, так же следует разбирать и здесь)."
IN_UPPADAVARE = "в разделе о возникновении"                  # uppādavāre (Uppādavāro = Раздел о возникновении)
assert B.SECTION_HEADINGS["Uppādavāro"] == "Раздел о возникновении"

# =============================================================================================
# FAMILY E: pariññāvāra (parijānāti)
# =============================================================================================
# parijānāti = «полностью понимает» (pi-5 «полностью понимает страдание»); negated «не понимает полностью»
# (pi-5 «не понимает полностью страдание»: negation moves the adverb after the verb, so «не полностью» never
# reads as "partly"). Past parijānittha = perfective «полностью понял» (aṭṭhakathā: the task of full
# understanding is finished, niṭṭhitapariññākicco); future perfective «полностью поймёт» (as 2-01's «возникнет»).
PJ_FORMS = {   # Pāli form -> (lemma, tense, Pāli number or None when the form does not show it)
    "parijānāti": ("parijānāti", "pres", "sg"), "parijānanti": ("parijānāti", "pres", "pl"),
    "parijānittha": ("parijānāti", "past", None),
    "parijānissati": ("parijānāti", "fut", "sg"), "parijānissanti": ("parijānāti", "fut", "pl"),
}
PJ_RU = {      # (lemma, tense, Russian number) -> (positive, negative)
    ("parijānāti", "pres", "sg"): ("полностью понимает", "не понимает полностью"),
    ("parijānāti", "pres", "pl"): ("полностью понимают", "не понимают полностью"),
    ("parijānāti", "past", "sg"): ("полностью понял", "не понял полностью"),
    ("parijānāti", "past", "pl"): ("полностью поняли", "не поняли полностью"),
    ("parijānāti", "fut", "sg"): ("полностью поймёт", "не поймёт полностью"),
    ("parijānāti", "fut", "pl"): ("полностью поймут", "не поймут полностью"),
}
PJ_PRED = "{v} {obj}"                          # verb before the object (pi-5)
PJ_NO_CA_FRAME = ", но {pred}"                 # ", no ca Y parijānāti" (no resumptive pronoun in the Pāli)
PJ_NEITHER_FRAME = A.PV_NEITHER_FRAME          # "Xñca na parijānāti Yñca na parijānāti": «не {v} ни X, ни Y»
PJ_NEG_MIXED_FRAME = A.PV_NEG_MIXED_FRAME      # different tenses: «не {v1} X и не {v2} Y»
PJ_BOTH_FRAME = C.BOTH_FRAME                   # "Xñca parijānāti Yñca parijānāti": «и {p1}, и {p2}»


def _alt(keys):
    return "(?:" + "|".join(re.escape(k) for k in sorted(keys, key=len, reverse=True)) + ")"


PJ_V_RE = _alt(PJ_FORMS)


def pj_forms(v, num):
    lemma, tense, _ = PJ_FORMS[v]
    return PJ_RU[(lemma, tense, num)]


def pj_pred(v, obj_ru, num, neg):
    pos, negf = pj_forms(v, num)
    return PJ_PRED.format(v=negf if neg else pos, obj=obj_ru)


def unti(w):
    """parijānātīti -> parijānāti; parijānitthāti -> parijānittha; parijānissatīti -> parijānissati."""
    for suf, rep in (("īti", "i"), ("āti", "a")):
        if w.endswith(suf) and w[: -len(suf)] + rep in PJ_FORMS:
            return w[: -len(suf)] + rep
    return w


# Questions: yo X V so Y V-ti?  -> C.Q_WHO «Кто {p1}, тот {p2}?»; "vā pana" -> C.KHA_PREFIX «А кто …»
PJ_Q_RE = re.compile(r"yo(?P<vp> vā pana)? (?P<x>\S+) (?P<n1>na )?(?P<v1>" + PJ_V_RE + r") so (?P<y>\S+) "
                     r"(?P<n2>na )?(?P<v2>" + PJ_V_RE + r")")


def pj_question(body, obj):
    words = body.split(" ")
    words[-1] = unti(words[-1])
    m = PJ_Q_RE.fullmatch(" ".join(words))
    if not m:
        raise ValueError(f"pariññā question not parsed: {body!r}")
    p1 = pj_pred(m.group("v1"), obj[m.group("x")], "sg", bool(m.group("n1")))
    p2 = pj_pred(m.group("v2"), obj[m.group("y")], "sg", bool(m.group("n2")))
    q = C.Q_WHO.format(p1=p1, p2=p2)
    return C.KHA_PREFIX + C.lower1(q) if m.group("vp") else q


# Persons of the answers (nominative). (pattern, Russian, number, relative clause -> needs a closing comma)
PJ_GEN = {"aggamaggasamaṅgiṃ": "обладающего высшим путём", "arahantaṃ": "архата"}   # after «Кроме»
PJ_SUBJ_UNITS = [
    (r"(\S+) ca (\S+) ca ṭhapetvā avasesā puggalā", None, "pl", False),       # A.APART_GROUP «Кроме A и B, остальные личности»
    (r"ye ca puthujjanā maggaṃ na paṭilabhissanti te", "те обычные люди, которые не обретут путь", "pl", True),
    (r"ye maggaṃ paṭilabhissanti te", "те, кто обретёт путь", "pl", True),
    (r"aggamaggasamaṅgī", "обладающий высшим путём", "sg", False),
    (r"arahā", "архат", "sg", False),
]
PUGGALA_PL = "личности"                        # puggalā (pi-5 puggala = личность)


def pj_subject(s):
    """'arahā ye ca puthujjanā maggaṃ na paṭilabhissanti te' -> («Архат и те обычные люди, которые …,», 'pl')."""
    s = C.lower1(s)
    units, pos = [], 0
    while pos < len(s):
        for rx, ru, num, rel in PJ_SUBJ_UNITS:
            m = re.compile(rx).match(s, pos)
            if m and (m.end() == len(s) or s[m.end()] == " "):
                if ru is None:
                    ru = A.APART_GROUP.format(a_gen=f"{PJ_GEN[m.group(1)]} и {PJ_GEN[m.group(2)]}", g_nom=PUGGALA_PL)
                units.append((ru, num, rel))
                pos = m.end() + 1
                break
        else:
            raise ValueError(f"pariññā subject not parsed at {s[pos:]!r} in {s!r}")
    out = units[0][0]
    for i in range(1, len(units)):
        last = i == len(units) - 1
        out += ((", и " if units[i - 1][2] else " и ") if last else ", ") + units[i][0]
    num = "pl" if len(units) > 1 or units[0][1] == "pl" else "sg"
    return cap(out) + ("," if units[-1][2] else ""), num


PJ_S1_RE = re.compile(r"(?P<subj>.+?) (?P<x>\S+) (?P<n1>na )?(?P<v1>" + PJ_V_RE + r"), no ca (?P<y>\S+) "
                      r"(?P<n2>na )?(?P<v2>" + PJ_V_RE + r")")
PJ_S2_RE = re.compile(r"(?P<subj>.+?) (?P<x>\S+) ca (?P<n1>na )?(?P<v1>" + PJ_V_RE + r") (?P<y>\S+) ca "
                      r"(?P<n2>na )?(?P<v2>" + PJ_V_RE + r")")


def _check_num(v, num, s):
    pn = PJ_FORMS[v][2]
    assert pn is None or pn == num, f"verb number {v} vs subject {num}: {s!r}"


def pj_sentence(s, obj):
    """One Pāli pariññā answer sentence (final '.' removed) -> Russian sentence (with '.')."""
    if s + "." in C.SIMPLE_ANSWERS:
        return C.SIMPLE_ANSWERS[s + "."]
    s = A._norm(s)                                           # Xñca -> Xṃ ca
    for rx, kind in ((PJ_S1_RE, 1), (PJ_S2_RE, 2)):
        m = rx.fullmatch(s)
        if not m or m.group("x") not in obj or m.group("y") not in obj:
            continue
        subj, num = pj_subject(m.group("subj"))
        _check_num(m.group("v1"), num, s)
        _check_num(m.group("v2"), num, s)
        x, y = obj[m.group("x")], obj[m.group("y")]
        n1, n2 = bool(m.group("n1")), bool(m.group("n2"))
        p1 = pj_pred(m.group("v1"), x, num, n1)
        if kind == 1:   # "no ca": the question's predicate is denied for Y (coordinator "Negatives")
            return f"{subj} {p1}{PJ_NO_CA_FRAME.format(pred=pj_pred(m.group('v2'), y, num, not n2))}."
        if n1 and n2:
            f1, f2 = pj_forms(m.group("v1"), num)[1][3:], pj_forms(m.group("v2"), num)[1][3:]
            both = (PJ_NEITHER_FRAME.format(v=f1, x=x, y=y) if f1 == f2
                    else PJ_NEG_MIXED_FRAME.format(v1=f1, x=x, v2=f2, y=y))
            return f"{subj} {both}."
        return f"{subj} {PJ_BOTH_FRAME.format(p1=p1, p2=pj_pred(m.group('v2'), y, num, n2))}."
    raise ValueError(f"pariññā answer not parsed: {s!r}")


def pj_answers(text, obj):
    out = []
    for s in re.split(r"(?<=\.) (?=\S)", text.strip()):
        assert s.endswith("."), s
        out.append(pj_sentence(s[:-1], obj))
    return " ".join(out)


PJ_QA_RE = re.compile(r"\((Ka|Kha)\) (yo .+?)\?(?: (.+))?")


def pj_line(text, cfg):
    """A pariññāvāra line, or None when the line is not one."""
    m = PJ_QA_RE.fullmatch(text)
    if m:
        lab, body, ans = m.groups()
        out = f"({B.LETTERS[lab]}) {pj_question(body, cfg['pj_obj'])}"
        return out + (" " + pj_answers(ans, cfg["pj_obj"]) if ans else "")
    if re.search(r"\bparijān", text):
        return pj_answers(text, cfg["pj_obj"])
    return None


# =============================================================================================
# Khandha members for family E (accusative objects; «совокупность» acc = nom)
# =============================================================================================
KH_PJ_OBJ = {m + "kkhandhaṃ": A.KH_K[m]["nom"] for m in A.KH_X}
assert all(v.startswith("совокупность ") for v in KH_PJ_OBJ.values())

# =============================================================================================
# Slips of this chapter (rendered as meant; each must occur exactly once)
# =============================================================================================
SLIPS = [
    ("tassa vadanākkhandho nirujjhitthāti", "tassa vedanākkhandho nirujjhitthāti",
     "^6-2-185: 'vadanākkhandho' = vedanākkhandho (spelling slip)"),
    ("saññākkhandho ca nirujjhissati vedanākkhandho nirujjhati.",
     "saññākkhandho ca nirujjhissati vedanākkhandho ca nirujjhati.",
     "^6-2-134: second 'ca' missing in '… vedanākkhandho nirujjhati' (parallel lines have it)"),
    ("tesaṃ tattha rūpakkhandho nuppajjati vedanākkhandho ca na nirujjhati.",
     "tesaṃ tattha rūpakkhandho ca nuppajjati vedanākkhandho ca na nirujjhati.",
     "^6-2-163: first 'ca' missing in 'rūpakkhandho nuppajjati vedanākkhandho ca …' (^6-2-159 has it)"),
    ("rūpakkhandho ca na nirujjhittha, vedanākkhandho ca na nirujjhissati.",
     "rūpakkhandho ca na nirujjhittha vedanākkhandho ca na nirujjhissati.",
     "^6-2-151: stray comma inside the ca … ca pair"),
]


def preprocess(text):
    for old, new, note in SLIPS:
        if old in text:
            text = text.replace(old, new)
            SLIP_LOG.append(note)
    return text


# =============================================================================================
# Line / chapter translation
# =============================================================================================
PE_END = "…pe…."


def tr(text, cfg):
    """Translate one Pāli line (block ID removed)."""
    if not text.strip():
        return ""
    text = preprocess(text)
    if text in cfg["fixed"]:
        return cfg["fixed"][text]
    r = pv_abbr(text, cfg["pv_subj"])
    if r is not None:
        return r
    r = pj_line(text, cfg)
    if r is not None:
        return r
    m = re.fullmatch(r"(\((?:Ka|Kha)\) .+\?) No\.", text)            # "? No." (not in 2-01's PV_SHORT)
    if m:
        return A.tr(m.group(1), cfg) + " " + C.NO
    if text.endswith(PE_END):                                          # "… uppajjati…pe…." -> «… возникает…»
        ru = A.tr(text[: -len(PE_END)] + ".", cfg)
        assert ru.endswith(".")
        return ru[:-1] + "…"
    return A.tr(text, cfg)


def translate_text(src, cfg):
    out = []
    with extra_units():
        for line in src.split("\n"):
            body, bid = B.ID_RE.match(line).groups()
            out.append(tr(body, cfg) + (bid or ""))
    return unicodedata.normalize("NFC", "\n".join(out))


KH2_CFG = dict(A.KH_CFG)
KH2_CFG.update({
    "pj_obj": KH_PJ_OBJ,
    "fixed": dict(A.KH_CFG["fixed"], **{
        "Nirodhavāro.": C.VARO_CLOSING.format(heading=B.SECTION_HEADINGS["Nirodhavāro"]),
        "Uppādanirodhavāro.": C.VARO_CLOSING.format(heading=B.SECTION_HEADINGS["Uppādanirodhavāro"]),
        "Pariññāvāro.": C.VARO_CLOSING.format(heading=B.SECTION_HEADINGS["Pariññāvāro"]),
        "Pavattivāro niṭṭhito.": f"{PAVATTIVARO} {B.NITTHITO}.",
        "Khandhayamakapāḷi niṭṭhitā.": B.YAMAKA_CLOSING_FRAME.format(title=B.YAMAKA_TITLES["Khandhayamakaṃ"]),
        "(Yathā uppādavāre paccuppannātītaṃ vibhattaṃ tathā idha vibhajitabbaṃ).": VIBHAJITABBAM_FRAME.format(
            where=IN_UPPADAVARE, what=B.SECTION_HEADINGS["Paccuppannātītavāro"].lower()),
    }),
})

# Strings taken from the approved pi-1 … pi-5 Russian rails (book, exact substring)
CROSSBOOK = [
    ("5", "полностью понимает страдание"), ("5", "не понимает полностью страдание"),   # parijānāti
    ("5", "полностью понимая его"), ("5", "обретает"),                                  # paṭilabhati
    ("5", "у архата"), ("5", "архат"),                                                  # arahant
    ("2", "знание обладающего путём"), ("1", "У обладающего благородным путём"),       # maggasamaṅgī
    ("4", "а также те обычные люди, которые"), ("5", "обычными людьми"),               # ye ca puthujjanā
    ("2", "так же следует разбирать и здесь.)"), ("2", "(Как разобрано в разделе"),   # vibhajitabbaṃ
    ("2", "следует подробно излагать"), ("2", "умирают"), ("2", "достигают окончательного угасания"),
    ("5", "Личность"), ("5", "? Нет."),
]


def check_previous_unchanged():
    """The extra units must not change 2-01's own output (and 2-01 imports cleanly)."""
    src = (B.PALI_DIR / PREV_CHAPTER).read_text(encoding="utf-8")
    on_disk = (B.OUT_DIR / PREV_CHAPTER).read_text(encoding="utf-8")
    with extra_units():
        again = A.translate_text(src, A.KH_CFG)
    assert again == on_disk, "2-01 output would change with the 2-02 person units"
    return src, on_disk


def main():
    B.check_crossbook()
    A.check_crossbook()
    A.check_crossbook(CROSSBOOK)
    C.check_crossbook_c()
    prev = check_previous_unchanged()
    A.SLIP_LOG.clear()                                    # 2-01's own slips are reported in notes-2-01.md
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    ru = translate_text(src, KH2_CFG)
    for old, _, note in SLIPS:
        assert src.count(old) == 1, f"slip pattern must occur once: {note}"
    B.check_pair(src, ru, CHAPTER)
    sample = [((B.PALI_DIR / n).read_text(encoding="utf-8"), (B.OUT_DIR / n).read_text(encoding="utf-8"))
              for n in B.SAMPLE_FILES]
    A.consistency(sample + [prev, (src, ru)])
    with open(B.OUT_DIR / CHAPTER, "w", encoding="utf-8", newline="\n") as f:
        f.write(ru)
    print("written", B.OUT_DIR / CHAPTER, "lines", len(ru.split("\n")))
    for s in SLIP_LOG + A.SLIP_LOG:
        print("slip:", s)
    print("cross-book asserts OK; per-line checks OK; consistency OK (sample, 2-01, 2-02); 2-01 unchanged")


if __name__ == "__main__":
    main()
