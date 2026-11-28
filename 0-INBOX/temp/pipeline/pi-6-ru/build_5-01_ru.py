"""Russian plain zero-shot of pi-6 (Yamaka): chapter 5-01-saccayamaka.md.

Families A and B come from build_2-01_ru (imported, never edited), family-B additions and pv_abbr() from
build_2-02_ru, the person / place shape from build_7-01_ru, moment phrases and persons of build_8_ru.
NEW here (listed in notes-5-01.md): the Sacca members, and the answer intros of the Sacca pavattivāra that mix
persons, planes and moments (taṇhāvippayuttacittassa uppādakkhaṇe, maggassa uppādakkhaṇe, abhisametāvī,
yassa cittassa anantarā aggamaggaṃ paṭilabhissanti, Suddhāvāsānaṃ dutiye citte vattamāne …).

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_5-01_ru.py
Probe:  python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_5-01_ru.py --probe 5-02-saccayamaka.md
        (prints only: which lines of another chapter these frames already translate)
Import: S = importlib.import_module("build_5-01_ru")   (importing never writes any file; only __main__ builds)

Exposed for 5-02 / 5-03 (and later chapters with the same intros)
  Members     SACCA_LEX (paṇṇattivāra words), SACCA_QUAL, SACCA_SUBJ (pavattivāra subjects), SACCA_CFG,
              CATTARI_SACCANI, KAYIKA_CETASIKA
  Intros      SC_UNITS, sc_units(), pv_intro(intro, tattha), place_intro(intro)   («У всех, кто перерождается, и
              в течение жизни в момент возникновения ума, не связанного с жаждой, …»)
  Sentences   pv_sentence(s, cfg), pv_answers(text, cfg), pv_question_any(q, cfg), PV_ABBR_Q_RE
  Paṇṇatti    pn_sentence(s, cfg), pn_line(text, cfg)
  Lines       tr(text, cfg, mode), translate_text(src, cfg, mode="pn"|"pv")   (mode switches to "pv" at the
              "Pavatti…" heading)
  Notes       NOTE_* strings, VARIANT_TAILS, variant_ru()
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

A = importlib.import_module("build_2-01_ru")   # families A + B
E = importlib.import_module("build_2-02_ru")   # family-B additions, pv_abbr, family E
C = importlib.import_module("build_7-01_ru")   # person / place shape
D = importlib.import_module("build_8_ru")      # moments, persons of the citta yamaka

CHAPTER = "5-01-saccayamaka.md"
cap = B.cap
lower1 = C.lower1
N = A.N
SLIP_LOG = []

# =============================================================================================
# Members (pi-2 Saccavibhaṅga / Dhammahadayavibhaṅga Russian, asserted below)
# =============================================================================================
# Bare words of the paṇṇattivāra are the names of the truths in pi-2 ^2-… «страдание, возникновение страдания,
# прекращение страдания»: dukkha = страдание, samudaya = возникновение (russian-style), nirodha = прекращение,
# magga = путь. The bare dukkha keeps «страдание» also in "kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ" (pi-1 there:
# «телесная боль, душевная боль»): the paṇṇattivāra tests the WORD dukkha, so one Russian word throughout.
SACCA_X = {
    "dukkha": N("страдание", "страданием", "страдания", "n"),
    "samudaya": N("возникновение", "возникновением", "возникновения", "n"),
    "nirodha": N("прекращение", "прекращением", "прекращения", "n"),
    "magga": N("путь", "путём", "пути", "m"),
}
SACCA_GENMOD = {"dukkha": "о страдании", "samudaya": "о возникновении", "nirodha": "о прекращении",
                "magga": "о пути"}
SACCA_K = {m: N("истина " + g, "истиной " + g, "истины " + g, "f") for m, g in SACCA_GENMOD.items()}
SACCA_G_SG = N("истина", "истиной", "истины", "f")         # saccaṃ
SACCA_G_PL = N("истины", "истинами", "истин", "pl")         # saccā
SACCA_X_FORMS = {"dukkha": ["dukkhaṃ"], "samudaya": ["samudayo", "samudayaṃ"],
                 "nirodha": ["nirodho", "nirodhaṃ"], "magga": ["maggo", "maggaṃ"]}
SACCA_LEX = {}
for _m, _forms in SACCA_X_FORMS.items():
    for _f in _forms:
        SACCA_LEX[_f] = SACCA_X[_m]
    SACCA_LEX[_m + "saccaṃ"] = SACCA_K[_m]
SACCA_LEX.update({"saccaṃ": SACCA_G_SG, "saccā": SACCA_G_PL})
SACCA_SUBJ = {_m + "saccaṃ": SACCA_K[_m] for _m in SACCA_X}          # pavattivāra subjects (all feminine)
SACCA_GENDER = "f"                                                  # bare verb answers («Возникала.»)

# Cattāri saccāni – … (pi-2 ^2-982 lists the same four names: asserted)
SACCA_LIST = "истина о страдании, истина о возникновении, истина о прекращении и истина о пути"
CATTARI_SACCANI = "Четыре истины – " + SACCA_LIST + "."
KAYIKA_CETASIKA = {"nom": "телесное страдание и душевное страдание", "gen": "телесного страдания и душевного страдания"}

# Paṇṇatti qualifiers (sg "avasesaṃ" / "avaseso" = «остальное», as 2-01's APART)
SACCA_QUAL = {"kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ ṭhapetvā avasesaṃ":
              (A.APART.format(a_gen=KAYIKA_CETASIKA["gen"]), "n")}
for _m in ("samudaya", "nirodha", "magga"):
    SACCA_QUAL[_m + "saccaṃ ṭhapetvā avaseso"] = (A.APART.format(a_gen=SACCA_K[_m]["gen"]), "n")
APART_FRAG = "Кроме {a_gen}"     # "X ṭhapetvā…pe…" (fragment before …pe…)

# =============================================================================================
# Notes, closings, headings
# =============================================================================================
SECTION_EXTRA = {
    "Suddhasaccavāro": "Раздел об истинах как таковых",                       # = Suddhakhandhavāro frame
    "Suddhasaccamūlacakkavāro": "Круговой раздел на основе истин как таковых",
    "Paṇṇattivāra": B.SECTION_HEADINGS["Paṇṇattivāro"],                       # stem form, same heading
}
HEADS = dict(B.SECTION_HEADINGS, **SECTION_EXTRA)
YASSAKA = "раздел с «у кого»"                # yassaka (cf. 2-02 yatthaka «раздел с «где»»)
YATTHAKA = "раздел с «где»"                  # yatthaka (2-02)
YASSAYATTHAKA = "раздел с «у кого где»"      # yassayatthaka
assert E.YATTHAKAM_PARIPUNNAM.startswith(YATTHAKA)
NOTE_YASSAKA = f"(И {YASSAKA}, и {YASSAYATTHAKA} следует развернуть одинаково)."   # vitthāretabbaṃ (7-01)
assert C.VITTHARETABBAM in NOTE_YASSAKA
NOTE_YATTHAKA_SABBATTHA = (f"({cap(YATTHAKA)} тоже везде одинаков. Различие в тексте такое же, "
                           f"как в разделе с «где» выше).")
NOTE_YATTHAKA_SABBE = "(все разделы с «где» одинаковы)"
NOTE_YATTHAKA_KATABBAM = f"({YATTHAKA} тоже следует изложить так же, как {YASSAYATTHAKA})"

# Variants: tails after the sigla
VARIANT_TAILS = {
    "evamuparipi": "так же и далее",                                                    # 2-01
    "evaṃ avasesesu tīsu saccesu": "так же и в остальных трёх истинах",
    "evaṃ puggalokāsepi nirodhavārepi": "так же и в разделе о личности и месте, и в разделе о прекращении",
    "puggalokāsavārepi": "так же и в разделе о личности и месте",
}
VARIANT_RE = A.VARIANT_RE


def variant_ru(content, kind="чтения"):
    m = re.fullmatch(r"(.+?) \(([^)]+)\)(?: (.+))?", content)
    if not m:
        raise ValueError(f"variant not parsed: {content!r}")
    sig = ", ".join(cap(x.strip()) + "." for x in m.group(2).split(".") if x.strip())
    tail = (", " + VARIANT_TAILS[m.group(3)]) if m.group(3) else ""
    return f"[вариант {kind} ({sig}): {m.group(1)}{tail}]"


# =============================================================================================
# Pavattivāra answer intros: persons, planes and moments
# =============================================================================================
# kinds: noun (person, genitive after «у»), rel (person clause «у тех, кто …,»), adv (time phrase), advc (time
# phrase ending in a participial phrase: closing comma), advcl (clause «когда …»: commas both sides), loc (place /
# «в течение жизни»: joins the next phrase), attach (joins the previous unit), part (participle after a person:
# «когда они перерождаются»), tesam (resumptive tesaṃ after a person clause: dropped, joins the next unit).
PAVATTE = "в течение жизни"                                     # pavatte (as against rebirth and death)
UPPADA, BHANGA = "в момент возникновения", "в момент распада"   # uppādakkhaṇe / bhaṅgakkhaṇe (pi-5, 8)
VIPPAYUTTA = "не связанного с"                                   # -vippayutta (pi-1 «не связанный со знанием»)
TANHA, MAGGA_G = "жаждой", "путём"                                # taṇhā (pi-1) instr.; magga instr.
CITTA_G = "ума"
SC_UNITS = [
    # persons
    (r"yassa cittassa anantarā aggamaggaṃ paṭilabhissanti", "тех, кто обретёт высший путь сразу после данного ума",
     "rel"),
    (r"tassa cittassa uppādakkhaṇe", f"{UPPADA} этого ума", "attach"),
    (r"tassa cittassa bhaṅgakkhaṇe", f"{BHANGA} этого ума", "attach"),
    (r"ye ca puthujjanā maggaṃ na paṭilabhissanti", "тех обычных людей, которые не обретут путь", "rel"),
    (r"ye puthujjanā maggaṃ na paṭilabhissanti", "тех обычных людей, которые не обретут путь", "rel"),
    (r"ye caññe maggaṃ paṭilabhissanti", "других, кто обретёт путь", "rel"),
    (r"ye maggaṃ paṭilabhissanti", "тех, кто обретёт путь", "rel"),
    (r"aggamaggasamaṅgīnaṃ", "обладающих высшим путём", "noun"),          # 2-02 «обладающий высшим путём»
    (r"arahantānaṃ", "архатов", "noun"),                                   # 2-02 «архат»
    (r"pacchimacittasamaṅgīnaṃ", "обладающих последним умом", "noun"),     # 8
    (r"nirodhasamāpannānaṃ", "вошедших в медитативное достижение прекращения", "noun"),   # 8
    (r"anabhisametāvīnaṃ", "не постигших истины", "noun"),
    (r"abhisametāvīnaṃ", "постигших истины", "noun"),
    (r"āpāyikānaṃ", "существ низших миров", "noun"),                       # pi-5 āpāyika «в низших мирах»
    # time phrases (the -vippayutta minds: uppādakkhaṇe / bhaṅgakkhaṇe; the latter for 5-02)
    *[u for kh, mo in (("uppādakkhaṇe", UPPADA), ("bhaṅgakkhaṇe", BHANGA)) for u in (
        (rf"taṇhāvippayuttamaggavippayuttacittassa {kh}",
         f"{mo} {CITTA_G}, {VIPPAYUTTA} {TANHA} и {VIPPAYUTTA} {MAGGA_G}", "advc"),
        (rf"maggavippayuttataṇhāvippayuttacittassa {kh}",
         f"{mo} {CITTA_G}, {VIPPAYUTTA} {MAGGA_G} и {VIPPAYUTTA} {TANHA}", "advc"),
        (rf"taṇhāvippayuttacittassa {kh}", f"{mo} {CITTA_G}, {VIPPAYUTTA} {TANHA}", "advc"),
        (rf"maggavippayuttacittassa {kh}", f"{mo} {CITTA_G}, {VIPPAYUTTA} {MAGGA_G}", "advc"),
    )],
    (r"taṇhāvippayuttacitte vattamāne", f"когда присутствует ум, не связанный с {TANHA}", "advcl"),   # pi-5
    (r"dutiye akusale citte vattamāne", "когда присутствует второй неблагой ум", "advcl"),
    (r"dutiye citte vattamāne", "когда присутствует второй ум", "advcl"),
    (r"upapatticittassa uppādakkhaṇe", f"{UPPADA} ума перерождения", "adv"),
    (r"upapatticittassa bhaṅgakkhaṇe", f"{BHANGA} ума перерождения", "adv"),
    (r"cittassa uppādakkhaṇe", f"{UPPADA} ума", "adv"),                    # 8
    (r"cittassa bhaṅgakkhaṇe", f"{BHANGA} ума", "adv"),                    # 8
    (r"taṇhāya uppādakkhaṇe", f"{UPPADA} жажды", "adv"),
    (r"taṇhāya bhaṅgakkhaṇe", f"{BHANGA} жажды", "adv"),
    (r"aggamaggassa ca phalassa ca uppādakkhaṇe", f"{UPPADA} высшего пути и плода", "adv"),
    (r"maggassa ca phalassa ca uppādakkhaṇe", f"{UPPADA} пути и плода", "adv"),
    (r"aggamaggassa uppādakkhaṇe", f"{UPPADA} высшего пути", "adv"),
    (r"aggamaggassa bhaṅgakkhaṇe", f"{BHANGA} высшего пути", "adv"),
    (r"maggassa uppādakkhaṇe", f"{UPPADA} пути", "adv"),
    (r"maggassa bhaṅgakkhaṇe", f"{BHANGA} пути", "adv"),
    (r"phalassa uppādakkhaṇe", f"{UPPADA} плода", "adv"),
    (r"phalassa bhaṅgakkhaṇe", f"{BHANGA} плода", "adv"),
]
# tried after build_2-01_ru.PERSON_UNITS (which has "sabbesaṃ upapajjantānaṃ" … and "itaresaṃ")
SC_UNITS_LAST = [
    # places / course of existence (join the following time phrase)
    (r"pavatte", PAVATTE, "loc"),
    (r"arūpe", A.PLANES["arūp"]["in"], "loc"),
    (r"pañcavokāre", A.PLANES["pañcavokār"]["in"], "loc"),
    (r"sabbesaṃ", "всех", "noun"),
    (r"tesaṃ upapajjantānaṃ", ("когда они перерождаются", "кто перерождается"), "part"),
    (r"tesaṃ cavantānaṃ", ("когда они умирают", "кто умирает"), "part"),            # 2-02 «когда они умирают»
    (r"upapajjantānaṃ", ("когда они перерождаются", "кто перерождается"), "part"),
    (r"cavantānaṃ", ("когда они умирают", "кто умирает"), "part"),
    (r"tesaṃ", "", "tesam"),
]
PERSON_KINDS = ("noun", "rel")
CLOSES = ("rel", "advc", "advcl", "part")
OPENS = ("advcl", "part")
WHO_TESAM = D.WHO_TESAM                      # «у них» when no person is named (8)
TAM = C.RES["tattha"]                        # «там»


def _units():
    out = []
    for rx, ru, rel in E.PERSON_UNITS_2_02 + A.PERSON_UNITS:
        out.append((rx, ru, "rel" if rel else "noun", True))
    return ([(rx, ru, k, False) for rx, ru, k in SC_UNITS] + out
            + [(rx, ru, k, False) for rx, ru, k in SC_UNITS_LAST])


ALL_UNITS = _units()
PLANE_RX = A._plane_re(A.PLANES)


def sc_units(intro):
    """'Sabbesaṃ upapajjantānaṃ pavatte …' -> [[russian, kind], …] (itaresaṃ merged as in 2-01)."""
    s = lower1(intro).replace(",", "")
    units, pos = [], 0
    while pos < len(s):
        for rx, ru, kind, planes in ALL_UNITS:
            m = re.compile(rx.replace("{P}", PLANE_RX)).match(s, pos)
            if m and (m.end() == len(s) or s[m.end()] == " "):
                if planes:
                    g = [A.PLANES[x] for x in m.groups()] + [{"in": "", "beings": ""}] * 2
                    ru = ru.format(in1=g[0]["in"], in2=g[1]["in"], b1=g[0]["beings"], b2=g[1]["beings"])
                units.append([ru, kind])
                pos = m.end() + 1
                break
        else:
            raise ValueError(f"intro not parsed at {s[pos:]!r} in {intro!r}")
    out = []
    for ru, kind in units:
        prev = out[-1] if out else None
        if prev and prev[0] == A.ITARESAM and prev[1] == "noun":
            if kind == "rel" and ru.startswith("тех, кто"):
                prev[:] = [A.ITARESAM + ru[3:], "rel"]
                continue
            if kind == "noun":
                prev[:] = [f"{A.ITARESAM} {ru}", "noun"]
                continue
            if kind == "part":
                prev[:] = [f"{A.ITARESAM}, {ru[1]}", "rel"]
                continue
        out.append([ru, kind])
    return out


def pv_intro(intro, tattha=False):
    """Person / time intro of an answer (+ «у них» / «там») ending with a space."""
    items, pending, prev = [], False, None
    for ru, kind in sc_units(intro):
        if kind == "tesam":
            pending = True
            continue
        if kind == "part":
            ru = ru[0]
        if kind in PERSON_KINDS:
            ru = "у " + ru
        attach = (pending or kind == "attach" or (prev is not None and prev in ("noun", "loc") and kind not in
                  PERSON_KINDS) or (kind == "part" and prev in PERSON_KINDS))
        pending = False
        if attach and items:
            items[-1].append((ru, kind))
        else:
            items.append([(ru, kind)])
        prev = kind
    persons = any(k in PERSON_KINDS for it in items for _, k in it)

    def render(item):
        s = item[0][0]
        for (_, pk), (ru, k) in zip(item, item[1:]):
            s += (", " if (pk in CLOSES or k in OPENS) else " ") + ru
        return s

    out = render(items[0])
    for i in range(1, len(items)):
        pc = items[i - 1][-1][1] in CLOSES
        out += ((", и " if pc else " и ") if i == len(items) - 1 else ", ") + render(items[i])
    if items[-1][-1][1] in CLOSES:
        out += ","
    if not persons:
        out += " " + WHO_TESAM
    if tattha:
        out += " " + TAM
    return cap(out) + " "


# Places (yattha answers): "Asaññasatte" / "Catuvokāre pañcavokāre" / "Apāye asaññasatte" / "Avasese …"
PLACE_FIXED = {
    "apāye": "в низших мирах",                                                          # pi-5 āpāyika
    "avasese catuvokāre pañcavokāre": "в остальном существовании с четырьмя составляющими и с пятью составляющими",
}


def place_intro(intro):
    s = lower1(intro)
    if s in PLACE_FIXED and " " in s:
        loci = [PLACE_FIXED[s]]
    else:
        loci = []
        for w in s.split(" "):
            if w in PLACE_FIXED:
                loci.append(PLACE_FIXED[w])
                continue
            m = re.fullmatch(PLANE_RX + "e", w)
            if not m:
                raise ValueError(f"place intro not parsed: {intro!r}")
            loci.append(A.PLANES[m.group(1)]["in"])
    txt = loci[0] if len(loci) == 1 else ", ".join(loci[:-1]) + " и " + loci[-1]
    return C.ANSWER_INTRO_PLACE.format(loci=cap(txt), res=TAM)


# =============================================================================================
# Pavattivāra sentences and questions
# =============================================================================================
_T = r"(?P<{n}>tesaṃ tattha|tesaṃ|tattha)"
S_NAMES = "(?:" + "|".join(sorted(SACCA_SUBJ, key=len, reverse=True)) + ")"
PV_S1_RE = re.compile(r"(?P<intro>.+?) " + _T.format(n="t1") + rf" (?P<x>{S_NAMES}) (?P<n1>na |n)?(?P<v1>"
                      + A.V_RE + r"), no ca " + _T.format(n="t2") + rf" (?P<y>{S_NAMES}) (?P<n2>na |n)?(?P<v2>"
                      + A.V_RE + r")")
PV_S2_RE = re.compile(r"(?P<intro>.+?) " + _T.format(n="t1") + rf" (?P<x>{S_NAMES}) ca (?P<n1>na |n)?(?P<v1>"
                      + A.V_RE + rf") (?P<y>{S_NAMES}) ca (?P<n2>na |n)?(?P<v2>" + A.V_RE + r")")


def pv_sentence(s, cfg):
    """One Pāli pavatti answer sentence (no final '.') -> Russian sentence with '.'."""
    if s + "." in C.SIMPLE_ANSWERS:
        return C.SIMPLE_ANSWERS[s + "."]
    lv = lower1(s)
    if lv in A.PV_VERBS:                                   # Uppajjati. / Uppajjittha. …
        return cap(A.verb(lv, cfg.get("gender", SACCA_GENDER))) + "."
    s = re.sub(r"ñca\b", "ṃ ca", s)
    subj = cfg["pv_subj"]
    for rx, kind in ((PV_S1_RE, 1), (PV_S2_RE, 2)):
        m = rx.fullmatch(s)
        if not m:
            continue
        if m.group("t1").startswith("tesaṃ"):
            head = pv_intro(m.group("intro"), "tattha" in m.group("t1"))
        else:
            head = place_intro(m.group("intro"))
        x, y = subj[m.group("x")], subj[m.group("y")]
        p1 = A.PV_PRED.format(v=A.verb(m.group("v1"), x["g"], bool(m.group("n1"))), x=x["nom"])
        if kind == 1:
            res = C.RES[m.group("t2")]
            v2 = A.verb(m.group("v2"), y["g"], not m.group("n2"))   # "no ca": the predicate is denied for Y
            tail = (A.PV_NO_CA_POS_FRAME if m.group("n2") else C.NO_CA_FRAME).format(
                res=res, **{("pred" if m.group("n2") else "neg_pred"): A.PV_PRED.format(v=v2, x=y["nom"])})
            return head + p1 + tail + "."
        if m.group("n1") and m.group("n2"):
            f1, f2 = A.verb(m.group("v1"), x["g"]), A.verb(m.group("v2"), y["g"])
            both = (A.PV_NEITHER_FRAME.format(v=f1, x=x["nom"], y=y["nom"]) if f1 == f2
                    else A.PV_NEG_MIXED_FRAME.format(v1=f1, x=x["nom"], v2=f2, y=y["nom"]))
            return head + both + "."
        p2 = A.PV_PRED.format(v=A.verb(m.group("v2"), y["g"], bool(m.group("n2"))), x=y["nom"])
        return head + C.BOTH_FRAME.format(p1=p1, p2=p2) + "."
    raise ValueError(f"pavatti answer not parsed: {s!r}")


def pv_answers(text, cfg):
    out = []
    for s in re.split(r"(?<=\.) (?=\S)", text.strip()):
        assert s.endswith("."), s
        out.append(pv_sentence(s[:-1], cfg))
    return " ".join(out)


# Abbreviated questions: "yassa vā pana…pe… uppajjitthāti", "yattha vā pana…pe…", "yassa vā pana yattha X V…pe… Vti"
PV_ABBR_Q_RE = re.compile(r"(?P<rel>yassa vā pana yattha|yassa vā pana|yattha vā pana)(?: (?P<x>\S+) (?P<n1>na |n)?"
                          r"(?P<v1>" + A.V_RE + r"))?…pe…(?: (?P<n2>na |n)?(?P<v2>" + A.VTI_RE + r"))?")
PV_ABBR_HEAD = {
    "yassa vā pana": C.KHA_PREFIX + lower1(C.Q_PERSON.split(" {")[0]),          # «А у кого»
    "yassa vā pana yattha": C.KHA_PREFIX + lower1(C.Q_PERSON_PLACE.split(" {")[0]),   # «А у кого где»
    "yattha vā pana": C.KHA_PREFIX + lower1(C.Q_PLACE.split(" {")[0]),           # «А где»
}


def pv_question_any(q, cfg):
    """Pāli question (no '?') -> Russian question with '?'."""
    m = PV_ABBR_Q_RE.fullmatch(q)
    if m:
        out = PV_ABBR_HEAD[m.group("rel")]
        g = cfg.get("gender", SACCA_GENDER)
        if m.group("x"):
            x = cfg["pv_subj"][m.group("x")]
            out += " " + A.PV_PRED.format(v=A.verb(m.group("v1"), x["g"], bool(m.group("n1"))), x=x["nom"])
        out += "…"
        if m.group("v2"):
            out += " " + A.verb(A.PV_VERB_TI[m.group("v2")], g, bool(m.group("n2")))
        return out + "?"
    return A.pv_question(lower1(q), cfg["pv_subj"])[0]


# =============================================================================================
# Paṇṇattivāra sentences and lines
# =============================================================================================
def pn_sentence(s, cfg):
    """One Pāli paṇṇatti answer sentence (no final '.') -> Russian with '.'."""
    if s + "." in C.SIMPLE_ANSWERS:
        return C.SIMPLE_ANSWERS[s + "."]
    if s == "Kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ dukkhañceva dukkhasaccañca":
        x, k2 = SACCA_LEX["dukkhaṃ"], SACCA_LEX["dukkhasaccaṃ"]
        return A.ANS_K_BOTH.format(k_nom=cap(KAYIKA_CETASIKA["nom"]), k_cop="являются", x_instr=x["instr"],
                                   k2_instr=k2["instr"])
    s = re.sub(r"ṭhapetvā avases(?:aṃ|o) na ceva", "ṭhapetvā avasesā na ceva", s)   # «остальное» in every gender
    return A.pannatti_sentence(s, cfg["lex"], cfg["qual"])


PE_TOKEN = re.compile(r"…[Pp]e…\.?")
PN_TOKEN = re.compile(r"…[Pp]e…\.?|\s+|[^?.…]+[?.]|[^?.…]+(?=…)")


def pn_line(text, cfg):
    """Paṇṇattivāra line (variants already removed, label removed): questions, answers, …pe… and fragments."""
    out, first = [], True
    pos = 0
    while pos < len(text):
        m = PN_TOKEN.match(text, pos)
        if not m:
            raise ValueError(f"paṇṇatti line not tokenised at {text[pos:]!r}")
        t = m.group(0)
        pos = m.end()
        if PE_TOKEN.fullmatch(t):
            out.append("…")
        elif not t.strip():
            out.append(t)
        else:
            if t.endswith("?"):
                ru = A.pada_question(lower1(t[:-1]), cfg["lex"])
            elif t.endswith("."):
                ru = pn_sentence(t[:-1], cfg)
            else:
                fm = re.fullmatch(r"(\S+) ṭhapetvā", t)
                if fm:
                    ru = APART_FRAG.format(a_gen=A.lex_get(fm.group(1), cfg["lex"])["gen"])
                elif t + "." in C.SIMPLE_ANSWERS:
                    ru = C.SIMPLE_ANSWERS[t + "."][:-1]
                else:
                    raise ValueError(f"fragment not parsed: {t!r}")
            if not first and t[0].islower():
                ru = lower1(ru)
            out.append(ru)
            first = False
    return "".join(out)


# =============================================================================================
# Lines
# =============================================================================================
HEAD_RE = re.compile(r"(#+) (?:\((\w+)\) )?(.+)")
LABEL_RE = re.compile(r"\((Ka|Kha)\) (.*)")
SLIPS = [   # (old, new, note): plain slips rendered as meant (each must occur exactly once in 5-01)
    ("paṭilabhissānti", "paṭilabhissanti", "^6-5-74 'paṭilabhissānti' = paṭilabhissanti (spelling)"),
    ("asaññattā cavantānaṃ", "asaññasattā cavantānaṃ", "^6-5-76 'asaññattā' = asaññasattā (spelling)"),
    ("avasesaṃ na dukkhaṃ dukkhasaccaṃ.", "avasesaṃ na dukkhaṃ, dukkhasaccaṃ.",
     "^6-5-11 comma missing before 'dukkhasaccaṃ' (after the variant; ^6-5-16 has it)"),
]


def heading(text):
    hashes, lab, body = HEAD_RE.fullmatch(text).groups()
    if body in B.YAMAKA_TITLES:
        ru = B.YAMAKA_TITLES[body]
    else:
        ru = C.heading_case(HEADS[body])
    return f"{hashes} " + (f"({lab if lab.isdigit() else B.LETTERS[lab]}) " if lab else "") + ru


def _variants(text, cfg):
    return VARIANT_RE.findall(text), VARIANT_RE.sub("", text)


def _insert_variants(ru, variants, cfg):
    for v in variants:
        anchor = cfg["variant_anchors"][v]
        assert ru.count(anchor) >= 1, (anchor, ru)
        ru = ru.replace(anchor, anchor + " " + variant_ru(v, cfg.get("variant_kind", {}).get(v, "чтения")), 1)
    return ru


def _preprocess(text, cfg):
    for old, new, note in cfg.get("slips", []):
        if old in text:
            text = text.replace(old, new)
            SLIP_LOG.append(note)
    return text


def tr(text, cfg, mode):
    """Translate one Pāli line (block ID removed). mode: "pn" (paṇṇattivāra) or "pv" (pavattivāra)."""
    if not text.strip():
        return ""
    if text in cfg["fixed"]:
        return cfg["fixed"][text]
    if text in B.FIXED:
        return B.FIXED[text]
    if text.startswith("#"):
        return heading(text)
    variants, text = _variants(text, cfg)
    text = _preprocess(text, cfg)
    label = ""
    m = LABEL_RE.fullmatch(text)
    if m:
        label, text = f"({B.LETTERS[m.group(1)]}) ", m.group(2)
    if mode == "pn":
        ru = pn_line(text, cfg)
    else:
        ru = pv_line(text, cfg)
    return _insert_variants(label + ru, variants, cfg)


def pv_line(text, cfg):
    for tail, note in cfg.get("abbr_notes", {}).items():          # "Yattha X V…pe… (note)."
        if text.endswith(" " + tail):
            head = E.pv_abbr(text[: -len(tail) - 1] + ".", cfg["pv_subj"])
            assert head and head.endswith("…"), text
            return f"{head} {note}."
    r = E.pv_abbr(text, cfg["pv_subj"])
    if r is not None:
        return r
    if "?" in text:
        q, _, rest = text.partition("?")
        out = pv_question_any(q, cfg)
        rest = rest.strip()
        if rest in ("…Pe….", "…pe…."):
            return out + "…"
        return out + (" " + pv_answers(rest, cfg) if rest else "")
    return pv_answers(text, cfg)


def translate_text(src, cfg, mode="pn"):
    out = []
    with E.extra_units():
        for line in src.split("\n"):
            body, bid = B.ID_RE.match(line).groups()
            if body.startswith("#") and "Pavatti" in body:
                mode = "pv"
            out.append(tr(body, cfg, mode) + (bid or ""))
    return unicodedata.normalize("NFC", "\n".join(out))


SACCA_CFG = {
    "lex": SACCA_LEX,
    "qual": SACCA_QUAL,
    "pv_subj": SACCA_SUBJ,
    "gender": SACCA_GENDER,
    "slips": SLIPS,
    "fixed": {
        "Cattāri saccāni – dukkhasaccaṃ, samudayasaccaṃ nirodhasaccaṃ, maggasaccaṃ.": CATTARI_SACCANI,
        "Paṇṇattiuddesavāro.": A.PANNATTI_UDDESAVARO,
        "Paṇṇattiniddesavāro.": A.PANNATTI_NIDDESAVARO,
        "Uppādavāro.": C.VARO_CLOSING.format(heading=B.SECTION_HEADINGS["Uppādavāro"]),
        "Nirodhavāro.": C.VARO_CLOSING.format(heading=B.SECTION_HEADINGS["Nirodhavāro"]),
        "Uppādanirodhavāro.": C.VARO_CLOSING.format(heading=B.SECTION_HEADINGS["Uppādanirodhavāro"]),
        "Pariññāvāro.": C.VARO_CLOSING.format(heading=B.SECTION_HEADINGS["Pariññāvāro"]),
        "(Yassakampi yassayatthakampi sadisaṃ vitthāretabbaṃ).": NOTE_YASSAKA,
        "(Yatthakampi sabbattha sadisaṃ. Tantinānākaraṇaṃ heṭṭhā yatthakasadisaṃ).": NOTE_YATTHAKA_SABBATTHA,
    },
    "abbr_notes": {
        "(yatthakā sadisā sabbe).": NOTE_YATTHAKA_SABBE,
        "(yatthakampi yassayatthakasadisaṃ kātabbaṃ).": NOTE_YATTHAKA_KATABBAM,
    },
    "variant_anchors": {
        "avasesaṃ dukkhasaccaṃ dukkhasaccaṃ (syā.) evamuparipi": "остальное является истиной о страдании",
        "avasesaṃ dukkhasaccaṃ na dukkhaṃ (sī. syā. ka.) evaṃ avasesesu tīsu saccesu":
            "остальное не является страданием",
        "avasesā saccā saccā (syā.)": "Остальные истины",
        "taṇhāvippayuttamaggavippayuttacittassa (sī.) evaṃ puggalokāsepi nirodhavārepi":
            f"{VIPPAYUTTA} {MAGGA_G} и {VIPPAYUTTA} {TANHA}",
        "uppatticittassa (syā.)": f"{UPPADA} ума перерождения",
        "paṭilabhissanti tassa cittassa uppādakkhaṇe ye (sī. syā.) puggalokāsavārepi":
            "обретёт высший путь сразу после данного ума",
    },
}

# Strings taken from the approved pi-1 … pi-5 Russian rails (book, exact substring)
CROSSBOOK = [
    ("2", cap(SACCA_LIST)), ("2", "Четыре истины – "),
    ("2", "страдание, возникновение страдания, прекращение страдания"),
    ("1", "не связанный со знанием"),               # vippayutta
    ("1", "отсутствие постижения"),                 # abhisamaya (abhisametāvī «постигший»)
    ("5", "Страдание в низших мирах"),              # āpāyika / apāya
    ("5", "когда у него присутствует"),            # citte vattamāne
    ("2", "сразу после"),                           # (sam)anantarā
    ("1", "жажда"), ("1", "жаждой"), ("1", "плод"), ("1", "неблагой ум"),
    ("5", "момент возникновения"), ("5", "момент распада"),
    ("5", "медитативное достижение прекращения"), ("5", "обычными людьми"), ("5", "архат"),
    ("2", "Существа без восприятия"), ("2", "перерождаются"), ("2", "умирают"),
    ("1", "душевная боль"), ("1", "телесная боль"),   # kāyika / cetasika (adjectives reused)
]


def check_slips(src):
    plain = VARIANT_RE.sub("", src)            # slips are matched after the variants are removed
    for old, _, note in SLIPS:
        assert plain.count(old) == 1, f"slip pattern must occur once: {note}"


def probe(name, mode="pv"):
    src = (B.PALI_DIR / name).read_text(encoding="utf-8")
    ok = bad = 0
    with E.extra_units():
        for line in src.split("\n"):
            body, _ = B.ID_RE.match(line).groups()
            if body.startswith("#") and "Pavatti" in body:
                mode = "pv"
            try:
                tr(body, SACCA_CFG, mode)
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
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    check_slips(src)
    ru = translate_text(src, SACCA_CFG)
    B.check_pair(src, ru, CHAPTER)
    prev = [((B.PALI_DIR / n).read_text(encoding="utf-8"), (B.OUT_DIR / n).read_text(encoding="utf-8"))
            for n in B.SAMPLE_FILES + ["2-01-khandhayamaka.md", "2-02-khandhayamaka.md", "7-01-anusayayamaka.md",
                                       "8-cittayamaka.md"]]
    A.consistency(prev + [(src, ru)])
    with open(B.OUT_DIR / CHAPTER, "w", encoding="utf-8", newline="\n") as f:
        f.write(ru)
    print("written", B.OUT_DIR / CHAPTER, "lines", len(ru.split("\n")))
    for s in SLIP_LOG + A.SLIP_LOG:
        print("slip:", s)
    print("cross-book asserts OK; per-line checks OK; consistency OK (sample, 2-01, 2-02, 7-01, 8)")


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "--probe":
        probe(sys.argv[2])
    else:
        main()
