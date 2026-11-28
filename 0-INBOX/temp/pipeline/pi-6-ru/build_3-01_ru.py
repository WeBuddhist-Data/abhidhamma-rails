"""Russian plain zero-shot of pi-6 (Yamaka): chapter 3-01-ayatanayamaka.md.

Families A (paṇṇattivāra) and B (pavattivāra) come from build_2-01_ru (frames imported, never retyped); the
person / place shape from build_7-01_ru (via build_2-01_ru.C). This module adds the twelve sense bases and the
Āyatana person descriptors (sacakkhuka / acakkhuka …), place lists and the abbreviated cycle lines.

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_3-01_ru.py
Import: A = importlib.import_module("build_3-01_ru")   (importing never writes any file)

Exposed for 3-02 … 3-06
  Members      AY_ORDER, AY_STEM, AY_PALI (cakkhāyatanaṃ …), AY_X (bare words), AY_K (bases), AY_G_SG / AY_G_PL,
               AY_LEX, AY_QUAL, AY_QUAL_PUN, AY_PV_SUBJ, AY_UDDESA
  Persons      AY_HAVE (sa-X-ka / a-X-ka descriptors), have_desc(), ay_person_units(), ay_person_intro()
  Places       AY_PLANES (2-01 PLANES + kāmāvacara / rūpāvacara / arūpāvacara), ay_place_intro()
  Sentences    ay_pv_sentence(), ay_question(), q_chain(), ay_answers(), ay_sentence()
  Closings     AY_MULAKA ("(Cakkhāyatanamūlakaṃ)"), SAMKHITTAM, CAKKAM_BANDHITABBAM, YASSAKA_TAIL, AY_HEADINGS
  Driver       AY_CFG (fixed lines, variant anchors), tr_line(text, cfg), translate_text(src, cfg)
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

D = importlib.import_module("build_2-01_ru")     # families A + B
C = D.C                                          # build_7-01_ru: person / place shape
CHAPTER = "3-01-ayatanayamaka.md"
cap, lower1, N = B.cap, C.lower1, D.N

# =============================================================================================
# Members: the twelve sense bases (names from pi-2 Āyatanavibhaṅga / pi-1, asserted below)
# =============================================================================================
AY_ORDER = ["cakkhu", "sota", "ghāna", "jivhā", "kāya", "rūpa", "sadda", "gandha", "rasa", "phoṭṭhabba",
            "mana", "dhamma"]
AY_STEM = {"cakkhu": "cakkh", "sota": "sot", "ghāna": "ghān", "jivhā": "jivh", "kāya": "kāy", "rūpa": "rūp",
           "sadda": "sadd", "gandha": "gandh", "rasa": "ras", "phoṭṭhabba": "phoṭṭhabb", "mana": "man",
           "dhamma": "dhamm"}
AY_PALI = {m: AY_STEM[m] + "āyatanaṃ" for m in AY_ORDER}           # cakkhāyatanaṃ …
AY_K_GEN = {"cakkhu": "глаза", "sota": "уха", "ghāna": "носа", "jivhā": "языка", "kāya": "тела",
            "rūpa": "видимых форм", "sadda": "звуков", "gandha": "запахов", "rasa": "вкусов",
            "phoṭṭhabba": "осязаемого", "mana": "ума", "dhamma": "объектов ума"}
AY_K = {m: N("сфера " + g, "сферой " + g, "сферы " + g, "f") for m, g in AY_K_GEN.items()}
AY_G_SG = N("сфера восприятия", "сферой восприятия", "сферы восприятия", "f")      # āyatanaṃ
AY_G_PL = N("сферы восприятия", "сферами восприятия", "сфер восприятия", "pl")     # āyatanā
# Bare words of the paṇṇattivāra. rūpa = «форма» as in 2-01 (aṭṭhakathā ^6-73: avasesaṃ rūpaṃ = all other
# matter and piyarūpa); dhamma = «явление» (aṭṭhakathā: avaseso dhammo = pariyattidhamma etc.).
AY_X = {
    "cakkhu": N("глаз", "глазом", "глаза", "m"),
    "sota": N("ухо", "ухом", "уха", "n"),
    "ghāna": N("нос", "носом", "носа", "m"),
    "jivhā": N("язык", "языком", "языка", "m"),
    "kāya": N("тело", "телом", "тела", "n"),
    "rūpa": D.KH_X["rūpa"],
    "sadda": N("звук", "звуком", "звука", "m"),
    "gandha": N("запах", "запахом", "запаха", "m"),
    "rasa": N("вкус", "вкусом", "вкуса", "m"),
    "phoṭṭhabba": N("осязаемое", "осязаемым", "осязаемого", "n"),
    "mana": N("ум", "умом", "ума", "m"),
    "dhamma": N("явление", "явлением", "явления", "n"),
}
AY_X_FORMS = {"cakkhu": ["cakkhu", "cakkhū", "cakkhuṃ"], "sota": ["sotaṃ"], "ghāna": ["ghānaṃ"],
              "jivhā": ["jivhā", "jivhaṃ"], "kāya": ["kāyo", "kāyaṃ"], "rūpa": ["rūpaṃ"],
              "sadda": ["saddo", "saddaṃ"], "gandha": ["gandho", "gandhaṃ"], "rasa": ["raso", "rasaṃ"],
              "phoṭṭhabba": ["phoṭṭhabbo", "phoṭṭhabbaṃ"], "mana": ["mano", "manaṃ"], "dhamma": ["dhammo", "dhammaṃ"]}
AY_LEX = {"āyatanaṃ": AY_G_SG, "āyatanā": AY_G_PL}
for _m, _forms in AY_X_FORMS.items():
    for _f in _forms:
        AY_LEX[_f] = AY_X[_m]
    AY_LEX[AY_PALI[_m]] = AY_K[_m]
AY_PV_SUBJ = {AY_PALI[m]: AY_K[m] for m in AY_ORDER}

# Dvādasāyatanāni – … (pi-2 ^2-155 names; this order: the Pāli of 3-01; «и» before the last as pi-2)
AY_UDDESA = ("Двенадцать сфер восприятия – " + ", ".join(AY_K[m]["nom"] for m in AY_ORDER[:-1])
             + " и " + AY_K[AY_ORDER[-1]]["nom"] + ".")

# Qualifiers of the paṇṇatti niddesa (lower-case Pāli -> (Russian, agreement)). Two or three listed things take
# the plural verb («являются»); "X-āyatanaṃ ṭhapetvā avaseso / avasesaṃ" = D.APART «Кроме …, остальное».
AY_QUAL = {
    "dibbacakkhu paññācakkhu": ("Божественный глаз, глаз мудрости", "pl"),                  # pi-5
    "dibbasotaṃ taṇhāsotaṃ": ("Божественное ухо, поток жажды", "pl"),                      # pi-5; sota = поток
    "sīlagandho samādhigandho paññāgandho": ("Запах нравственности, запах сосредоточения, запах мудрости", "pl"),
    "attharaso dhammaraso vimuttiraso": ("Вкус смысла, вкус Учения, вкус освобождения", "pl"),
}
for _m in AY_ORDER:
    for _end in ("avaseso", "avasesaṃ"):
        AY_QUAL[f"{AY_PALI[_m]} ṭhapetvā {_end}"] = (D.APART.format(a_gen=AY_K[_m]["gen"]), "n")
# sota = "ear" and "stream": the pun is marked with quotes on the bare word in these sentences only.
AY_QUAL_PUN = {"dibbasotaṃ taṇhāsotaṃ": (AY_X["sota"]["instr"], "«" + AY_X["sota"]["instr"] + "»")}

# =============================================================================================
# Family B: persons and places of the Āyatanayamaka
# =============================================================================================
AY_PLANES = dict(D.PLANES)
AY_PLANES.update({
    "kāmāvacar": {"in": C.LOCI["kāmadhātuyā"], "beings": "существ мира чувственных желаний"},
    "rūpāvacar": {"in": C.LOCI["rūpadhātuyā"], "beings": "существ мира форм"},
    "arūpāvacar": {"in": C.LOCI["arūpadhātuyā"], "beings": D.PLANES["arūp"]["beings"]},
})
# sa-X-kānaṃ / a-X-kānaṃ: «с глазом» / «без глаза» (pi-2 acittakā = «без ума»). stem -> (instr, gen)
AY_HAVE = {"cakkhuk": ("глазом", "глаза"), "sotak": ("ухом", "уха"), "ghānak": ("носом", "носа"),
           "rūpak": ("видимой формой", "видимой формы"), "cittak": ("умом", "ума")}
HAVE_JOIN = " и "                         # "sacakkhukānaṃ asotakānaṃ" = «с глазом и без уха»
ALL_DYING = next(ru for rx, ru, _ in D.PERSON_UNITS if rx == r"sabbesaṃ cavantānaṃ")          # всех, кто умирает
REBORN = next(ru for rx, ru, _ in D.PERSON_UNITS if rx == r"{P}aṃ upapajjantānaṃ").replace("{in1}", "{desc}")


def s_prep(w):
    return ("со " if re.match(r"[сзшжщ][бвгджзклмнпрстфхцчшщ]|мн", w) else "с ") + w


def have_desc(tok, have=None):
    have = AY_HAVE if have is None else have
    m = re.fullmatch(r"(sa|a)(" + "|".join(sorted(have, key=len, reverse=True)) + r")ānaṃ", tok)
    if not m:
        return None
    ins, gen = have[m.group(2)]
    return s_prep(ins) if m.group(1) == "sa" else "без " + gen


def ru_and(items):
    return items[0] if len(items) == 1 else ", ".join(items[:-1]) + " и " + items[-1]


def ay_person_units(intro, planes=None, have=None):
    planes = AY_PLANES if planes is None else planes
    toks = lower1(intro).split()
    pre = D._plane_re(planes)
    units, i = [], 0
    while i < len(toks):
        if toks[i:i + 2] == ["sabbesaṃ", "cavantānaṃ"]:
            units.append([ALL_DYING, True])
            i += 2
            continue
        descs = []
        while i < len(toks) and have_desc(toks[i], have):
            descs.append(have_desc(toks[i], have))
            i += 1
        if descs:
            if i >= len(toks) or toks[i] != "upapajjantānaṃ":
                raise ValueError(f"person intro not parsed: {intro!r}")
            units.append([REBORN.format(desc=HAVE_JOIN.join(descs)), True])
            i += 1
            continue
        beings = []
        while i < len(toks) and re.fullmatch(pre + "ānaṃ", toks[i]):
            beings.append(planes[re.fullmatch(pre + "ānaṃ", toks[i]).group(1)]["beings"])
            i += 1
        if beings:
            units.append([ru_and(beings), False])
            continue
        raise ValueError(f"person intro not parsed at {toks[i]!r} in {intro!r}")
    return units


def ay_person_intro(intro, planes=None, have=None):
    """Joined as build_2-01_ru.person_intro: «У A, и у B, …» (comma after a relative clause)."""
    units = ay_person_units(intro, planes, have)
    s = "У " + units[0][0]
    for i in range(1, len(units)):
        last = i == len(units) - 1
        sep = ((", и " if units[i - 1][1] else " и ") if last else ", ")
        s += sep + "у " + units[i][0]
    return s + ("," if units[-1][1] else "") + " "


def ay_place_intro(intro, planes=None):
    """'Asaññasatte arūpe' -> «Среди существ без восприятия, в мире без форм: там » (C.LOCI_SEP, no conjunction)."""
    planes = AY_PLANES if planes is None else planes
    rx = re.compile(D._plane_re(planes) + "e")
    locs = []
    for t in lower1(intro).split():
        m = rx.fullmatch(t)
        if not m:
            raise ValueError(f"place intro not parsed: {intro!r}")
        locs.append(planes[m.group(1)]["in"])
    return C.ANSWER_INTRO_PLACE.format(loci=cap(C.LOCI_SEP.join(locs)), res=C.RES["tattha"])


def ay_pv_sentence(s, subj=None, planes=None, y_ctx=None, have=None):
    """One Pāli pavatti answer sentence (final '.' removed) -> Russian (with '.'): build_2-01_ru.pv_sentence with
    the Āyatana person / place intros."""
    subj = AY_PV_SUBJ if subj is None else subj
    s = D._norm(s)
    if s in D.PV_SHORT:
        return D.PV_SHORT[s]
    lv = lower1(s)
    if lv in D.PV_VERBS or lv in D.PV_VERB_SLIPS:
        return cap(D.verb(lv, y_ctx["g"] if y_ctx else "sg")) + "."
    for rx, kind in ((D.PV_S1_RE, 1), (D.PV_S2_RE, 2)):
        m = rx.fullmatch(s)
        if not m:
            continue
        if m.group("t1").startswith("tesaṃ"):
            head = ay_person_intro(m.group("intro"), planes, have) + (D.PV_TAM if "tattha" in m.group("t1") else "")
        else:
            head = ay_place_intro(m.group("intro"), planes)
        x, y = subj[m.group("x")], subj[m.group("y")]
        p1 = D.PV_PRED.format(v=D.verb(m.group("v1"), x["g"], bool(m.group("n1"))), x=x["nom"])
        if kind == 1:
            res = C.RES[m.group("t2")]
            v2 = D.verb(m.group("v2"), y["g"], not m.group("n2"))
            tail = (D.PV_NO_CA_POS_FRAME if m.group("n2") else C.NO_CA_FRAME).format(
                res=res, **{("pred" if m.group("n2") else "neg_pred"): D.PV_PRED.format(v=v2, x=y["nom"])})
            return cap(head + p1 + tail) + "."
        if m.group("n1") and m.group("n2"):
            f1, f2 = D.verb(m.group("v1"), x["g"]), D.verb(m.group("v2"), y["g"])
            if f1 == f2:
                both = D.PV_NEITHER_FRAME.format(v=f1, x=x["nom"], y=y["nom"])
            else:
                both = D.PV_NEG_MIXED_FRAME.format(v1=f1, x=x["nom"], v2=f2, y=y["nom"])
            return cap(head + both) + "."
        p2 = D.PV_PRED.format(v=D.verb(m.group("v2"), y["g"], bool(m.group("n2"))), x=y["nom"])
        return cap(head + C.BOTH_FRAME.format(p1=p1, p2=p2)) + "."
    raise ValueError(f"pavatti answer not parsed: {s!r}")


# =============================================================================================
# Questions and answers
# =============================================================================================
SLIPS = {   # plain spelling slips, rendered as meant (reported)
    "sotāyananti": "sotāyatananti",                       # ^6-3-13
    "uppajjittharūpāyatanañca": "uppajjittha rūpāyatanañca",   # ^6-3-43 (missing space)
}
SLIP_LOG = D.SLIP_LOG


def preprocess(text):
    for a, b in SLIPS.items():
        if a in text:
            SLIP_LOG.append(f"{a} rendered as {b}")
            text = text.replace(a, b)
    return text


def _na(body):
    """nāyatanā / nāyatanaṃ / nāyatananti -> na āyatanā … (the pada_question parser wants 'na X na Y')."""
    return re.sub(r"\bnāyatan", "na āyatan", body)


def ay_question(body, cfg=None):
    """One Pāli question body (no label, no '?') -> (Russian question with '?', y noun or None)."""
    cfg = AY_CFG if cfg is None else cfg
    lb = lower1(body.strip())
    if lb.startswith(("yassa", "yattha")):
        return D.pv_question(lb, cfg["pv_subj"])
    return D.pada_question(_na(lb), cfg["lex"]), None


def q_chain(body, cfg=None):
    """'A…pe… B' (questions asked in turn) -> «QA… qB?» (only the last keeps '?')."""
    parts = [ay_question(p, cfg)[0] for p in body.split("…pe… ")]
    out = parts[0][:-1]
    for p in parts[1:]:
        out += "… " + lower1(p[:-1])
    return out + "?"


def ay_sentence(body, cfg=None, y_ctx=None):
    """One Pāli answer sentence (final '.' removed) -> Russian sentence."""
    cfg = AY_CFG if cfg is None else cfg
    lv = lower1(body)
    if body in D.PV_SHORT or lv in D.PV_VERBS or lv in D.PV_VERB_SLIPS \
            or " tesaṃ " in body or " tattha " in body or body.startswith("Sabbesaṃ"):
        return ay_pv_sentence(body, cfg["pv_subj"], cfg["planes"], y_ctx, cfg.get("have"))
    b2 = re.sub(r"\bavases(?:aṃ|o) na ceva\b", "avasesā na ceva", body)   # Russian «остальное» for every number
    ru = D.pannatti_sentence(b2, cfg["lex"], cfg["qual"])
    for q, (a, b) in cfg.get("pun", {}).items():
        if lv.startswith(q):
            assert a in ru, (a, ru)
            ru = re.sub(rf"(?<=являются ){a}\b", b, ru)
    return ru


def ay_answers(text, cfg=None, y_ctx=None):
    cfg = AY_CFG if cfg is None else cfg
    variants = D.VARIANT_RE.findall(text)
    plain = D.VARIANT_RE.sub("", text)
    out = []
    for s in re.split(r"(?<=\.) (?=\S)", plain.strip()):
        assert s.endswith("."), s
        out.append(ay_sentence(s[:-1], cfg, y_ctx))
    ru = " ".join(out)
    for v in variants:
        anchor = cfg["variant_anchors"][v]
        assert anchor in ru, (anchor, ru)
        ru = ru.replace(anchor, anchor + " " + D.variant_ru(v, cfg.get("variant_kind", {}).get(v, D.VARIANT_KIND_DEFAULT)), 1)
    return ru


# =============================================================================================
# Headings, closings, tails
# =============================================================================================
AY_EXTRA_HEADINGS = {   # not in build_sample_ru.SECTION_HEADINGS (new here; shaped like Suddhakhandha…)
    "Suddhāyatanavāro": "Раздел о сферах восприятия как таковых",
    "Suddhāyatanamūlacakkavāro": "Круговой раздел на основе сфер восприятия как таковых",
}
AY_HEADINGS = dict(B.SECTION_HEADINGS, **AY_EXTRA_HEADINGS)
HEAD_RE = re.compile(r"(#+) (?:\((\w+)\) )?(.+)")


def heading(text):
    hashes, lab, body = HEAD_RE.fullmatch(text).groups()
    ru = B.YAMAKA_TITLES[body] if body in B.YAMAKA_TITLES else C.heading_case(AY_HEADINGS[body])
    if lab:
        ru = f"({lab if lab.isdigit() else B.LETTERS[lab]}) " + ru
    return f"{hashes} {ru}"


AY_MULAKA_FRAME = "На основе {gen}"         # (Cakkhāyatanamūlakaṃ) = (На основе сферы глаза); 7-01 «На основе одного»
AY_MULAKA = {cap(AY_PALI[m][:-1] + "mūlakaṃ"): AY_MULAKA_FRAME.format(gen=AY_K[m]["gen"]) for m in AY_ORDER}
SAMKHITTAM = "Сокращено"                    # (Saṃkhittaṃ)
TAILS = dict(AY_MULAKA, **{"Saṃkhittaṃ": SAMKHITTAM})
TAIL_RE = re.compile(r"(.*?) ?\((" + "|".join(TAILS) + r")\)(\.?)")
CAKKAM_BANDHITABBAM = "(Круг следует замкнуть)"                                       # (Cakkaṃ bandhitabbaṃ)
EKEKAPADA_CAKKAM = "(Круг на основе каждого отдельного слова следует замкнуть, не допуская путаницы)."
CAKKAM_AMANTA = "(Замыкая круг, везде следует отвечать «" + B.AMANTA[:-1] + "»)."      # sabbattha = везде (pi-5)
# "(saṃkhittaṃ yassakasadisaṃ [ … ] )." at the end of an answer line
YASSAKA_PALI = " (saṃkhittaṃ yassakasadisaṃ [yassakampi sadisaṃ (sī.), yassekasadisaṃ (syā.)] )."
# yatthaka = «раздел с «где»» (2-02: "(yatthakaṃ paripuṇṇaṃ kātabbaṃ)"); yassaka = «раздел с «у кого»»
YATTHAKA = "раздел с «где»"
YASSAKA = "раздел с «у кого»"
YASSAKA_TAIL = (" (" + lower1(SAMKHITTAM) + ", так же как " + YASSAKA.replace("раздел", "в разделе", 1)
                + " [вариант чтения (Sī.): yassakampi sadisaṃ; (Syā.): yassekasadisaṃ]).")
ELL_RE = re.compile(r"(.*?)(…[Pp]e…\.?|…\.)")
LABEL_RE = re.compile(r"\((\w+)\) (.*)")


def tr_line(text, cfg=None):
    """Translate one Pāli line (block ID removed)."""
    cfg = AY_CFG if cfg is None else cfg
    if not text.strip():
        return ""
    if text in cfg["fixed"]:
        return cfg["fixed"][text]
    if text in B.FIXED:
        return B.FIXED[text]
    if text.startswith("#"):
        return heading(text)
    text = preprocess(text)
    if text.endswith(YASSAKA_PALI):
        out = tr_line(text[: -len(YASSAKA_PALI)] + ".", cfg)
        assert out.endswith(".")
        return out[:-1] + YASSAKA_TAIL
    m = TAIL_RE.fullmatch(text)
    if m:
        return tr_line(m.group(1), cfg) + f" ({TAILS[m.group(2)]}){m.group(3)}"
    m = ELL_RE.fullmatch(text)
    if m:
        rest = m.group(1)
        if rest.endswith((".", "?")):
            return tr_line(rest, cfg) + "…"
        out = tr_line(rest + ".", cfg)
        assert out.endswith(".")
        return out[:-1] + "…"
    label = ""
    m = LABEL_RE.fullmatch(text)
    if m and m.group(1) in B.LETTERS:
        label, text = f"({B.LETTERS[m.group(1)]}) ", m.group(2)
        if m.group(1) == "Ka" and " vā pana " in text:
            SLIP_LOG.append(f"label (Ka) on a 'vā pana' question (kept as written): {text[:60]}")
    if "?" in text:
        q, _, a = text.partition("?")
        if "…pe… " in q:
            out, y = q_chain(q, cfg), None
        else:
            out, y = ay_question(q, cfg)
        out = label + out
        return out + (" " + ay_answers(a, cfg, y) if a.strip() else "")
    return label + ay_answers(text, cfg)


def translate_text(src, cfg=None):
    out = []
    for line in src.split("\n"):
        body, bid = B.ID_RE.match(line).groups()
        out.append(tr_line(body, cfg) + (bid or ""))
    return unicodedata.normalize("NFC", "\n".join(out))


# =============================================================================================
# Fixed lines of 3-01 (abbreviated cycle lines; composed from the frames, never retyped)
# =============================================================================================
def _q(body):
    return ay_question(body, {"lex": AY_LEX, "pv_subj": AY_PV_SUBJ})[0]


def _apart_series(ms):
    """'Sotaṃ ṭhapetvā…pe… ghānaṃ ṭhapetvā…pe… … na ca āyatanā.' -> «Кроме уха… кроме носа… ни сферами восприятия.»"""
    krome = D.APART.split(" ")[0]
    parts = [f"{krome} {AY_X[m]['gen']}" for m in ms]
    return "… ".join([parts[0]] + [lower1(p) for p in parts[1:]]) + "… ни " + AY_G_PL["instr"] + "."


def _neg_k(m):
    """'na cakkhāyatanaṃ' (end of «Avasesā āyatanā na …») -> «не являются сферой глаза»."""
    return f"не {AY_G_PL['cop']} {AY_K[m]['instr']}"


def _rest_not(m):
    return D.ANS_REST_NOT.format(g_nom=AY_G_PL["nom"], g_cop=AY_G_PL["cop"], k_instr=AY_K[m]["instr"])


def _pv(v, m, neg=False):
    return D.PV_PRED.format(v=D.verb(v, AY_K[m]["g"], neg), x=AY_K[m]["nom"])


A_ = B.AMANTA
Q_PLACE_HEAD = C.Q_PLACE.split(",")[0]                     # «Где {p1}»
VERB_PAST = D.verb("uppajjittha", "f")                     # возникала

AY_FIXED = {
    ("Dvādasāyatanāni – cakkhāyatanaṃ, sotāyatanaṃ ghānāyatanaṃ, jivhāyatanaṃ, kāyāyatanaṃ, rūpāyatanaṃ, "
     "saddāyatanaṃ, gandhāyatanaṃ, rasāyatanaṃ, phoṭṭhabbāyatanaṃ, manāyatanaṃ, dhammāyatanaṃ."): AY_UDDESA,
    "(Cakkaṃ bandhitabbaṃ)": CAKKAM_BANDHITABBAM,
    "Paṇṇattiuddesavāro.": D.PANNATTI_UDDESAVARO,
    "Paṇṇattiniddesavāro.": D.PANNATTI_NIDDESAVARO,
    "(Ekekapadamūlakaṃ cakkaṃ bandhitabbaṃ asammohantena).": EKEKAPADA_CAKKAM,
    "(Cakkaṃ bandhantena sabbattha āmantāti kātabbaṃ).": CAKKAM_AMANTA,
    "Sotaṃ sotāyatananti?…Pe… avasesā āyatanā na dhammāyatanaṃ…pe….":
        f"{_q('sotaṃ sotāyatananti')}… {lower1(_rest_not('dhamma'))[:-1]}…",
    ("Āmantā.…Pe… ghānaṃ… jivhā… kāyo… rūpaṃ… saddo… gandho… raso… phoṭṭhabbo… mano… dhammo "
     "āyatananti?"):
        f"{A_}… " + "… ".join(AY_X[m]["nom"] for m in AY_ORDER[2:11]) + "… " + lower1(_q("dhammo āyatananti")),
    "Sotaṃ ṭhapetvā…pe… ghānaṃ ṭhapetvā…pe… jivhaṃ ṭhapetvā…pe… na ca āyatanā.":
        _apart_series(["sota", "ghāna", "jivhā"]),
    ("Rūpaṃ ṭhapetvā…pe… saddaṃ ṭhapetvā…pe… gandhaṃ ṭhapetvā…pe… rasaṃ ṭhapetvā…pe… phoṭṭhabbaṃ ṭhapetvā…pe… "
     "na ca āyatanā. Nāyatanā na phoṭṭhabbāyatananti? Āmantā."):
        _apart_series(["rūpa", "sadda", "gandha", "rasa", "phoṭṭhabba"]) + " "
        + _q("nāyatanā na phoṭṭhabbāyatananti") + " " + A_,
    "Āyatanā cakkhāyatananti?…Pe… na cakkhāyatanaṃ…pe…. Āyatanā dhammāyatananti?…Pe… na dhammāyatanaṃ.":
        (f"{_q('āyatanā cakkhāyatananti')}… {_neg_k('cakkhu')}… {_q('āyatanā dhammāyatananti')}… "
         f"{_neg_k('dhamma')}."),
    "Āyatanā cakkhāyatananti?…Pe… āyatanā dhammāyatananti? …Pe… na dhammāyatanaṃ…pe….":
        f"{_q('āyatanā cakkhāyatananti')}… {lower1(_q('āyatanā dhammāyatananti'))} … {_neg_k('dhamma')}…",
    ("Sotaṃ ṭhapetvā…pe… ghānaṃ ṭhapetvā…pe… jivhaṃ ṭhapetvā…pe… na ca āyatanā. Nāyatanā na "
     "dhammāyatananti? Āmantā."):
        _apart_series(["sota", "ghāna", "jivhā"]) + " " + _q("nāyatanā na dhammāyatananti") + " " + A_,
    "Nāyatanā na cakkhāyatananti? Āmantā.…Pe…. Nāyatanā na dhammāyatananti? Āmantā.…Pe….":
        f"{_q('nāyatanā na cakkhāyatananti')} {A_}… {_q('nāyatanā na dhammāyatananti')} {A_}…",
    ("(Yattha ghānāyatanaṃ uppajjati tattha manāyatanaṃ dhammāyatanañca ekasadisaṃ, nānaṃ natthi, upari pana "
     "vārasaṅkhepo [uparivāre saṅkhepo (syā.), uparivāre saṅkhepaṃ (sī. ka.)] tīti jānitabbaṃ.)"):
        (f"({Q_PLACE_HEAD.format(p1=_pv('uppajjati', 'ghāna'))}, там {AY_K['mana']['nom']} и "
         f"{AY_K['dhamma']['nom']} одинаковы, различия нет, а дальше разделы даются сокращённо "
         "[вариант чтения (Syā.): uparivāre saṅkhepo; (Sī., Ka.): uparivāre saṅkhepaṃ], так следует понимать.)"),
    ("Yassa cakkhāyatanaṃ uppajjittha tassa ghānāyatanaṃ…pe… rūpāyatanaṃ… manāyatanaṃ… dhammāyatanaṃ "
     "uppajjitthāti? Āmantā."):
        C.Q_PERSON.format(p1=_pv("uppajjittha", "cakkhu"),
                          p2=VERB_PAST + " " + "… ".join(AY_K[m]["nom"] for m in ("ghāna", "rūpa", "mana", "dhamma")))
        + " " + A_,
    ("Yassa ghānāyatanaṃ…pe… rūpāyatanaṃ… manāyatanaṃ uppajjittha tassa dhammāyatanaṃ uppajjitthāti? "
     "Āmantā."):
        C.Q_PERSON.format(p1=VERB_PAST + " " + "… ".join(AY_K[m]["nom"] for m in ("ghāna", "rūpa", "mana")),
                          p2=_pv("uppajjittha", "dhamma")) + " " + A_,
    ("(Ka) yattha cakkhāyatanaṃ uppajjittha…pe… (yatthakaṃ paccuppannepi atītepi anāgatepi paccuppannātītepi "
     "paccuppannānāgatepi atītānāgatepi sabbattha sadisaṃ, uppajjati uppajjitthāti nāmaṃ atirekaṃ kātabbaṃ)."):
        (f"({B.LETTERS['Ka']}) {Q_PLACE_HEAD.format(p1=_pv('uppajjittha', 'cakkhu'))}… ({YATTHAKA} везде "
         "одинаков: в настоящем, в прошлом, в будущем, в настоящем и прошлом, в настоящем и будущем, в прошлом "
         f"и будущем; следует добавить слова «{D.verb('uppajjati', 'sg')}», «{VERB_PAST}»)."),
    "Yattha cakkhāyatanaṃ nuppajjittha…pe….": Q_PLACE_HEAD.format(p1=_pv("uppajjittha", "cakkhu", True)) + "…",
}

AY_CFG = {
    "lex": AY_LEX,
    "qual": AY_QUAL,
    "pun": AY_QUAL_PUN,
    "pv_subj": AY_PV_SUBJ,
    "planes": AY_PLANES,
    "have": AY_HAVE,
    "fixed": AY_FIXED,
    "variant_anchors": {
        "avasesā (syā. pī.)": f"Кроме {AY_X['cakkhu']['gen']} и {AY_K['cakkhu']['gen']}, остальное",
        "avaseso (syā.)": f"Кроме {AY_X['kāya']['gen']} и {AY_K['kāya']['gen']}, остальное",
        "avasesā (syā.)": f"Кроме {AY_X['gandha']['gen']} и {AY_K['gandha']['gen']}, остальное",
    },
}

# =============================================================================================
# Checks
# =============================================================================================
CROSSBOOK = [   # strings taken from the approved pi-1 … pi-5 Russian rails (book, exact substring)
    ("2", "Двенадцать сфер восприятия – сфера глаза, сфера уха, сфера носа, сфера языка, сфера тела, сфера ума, "
          "сфера видимых форм, сфера звуков, сфера запахов, сфера вкусов, сфера осязаемого и сфера объектов ума."),
    ("1", "сфера осязаемого"), ("1", "сфера объектов ума"),
    ("5", "божественный глаз"), ("5", "глаз мудрости"), ("5", "божественное ухо"),
    ("2", "без ума"), ("1", "в мире чувственных желаний"), ("1", "в мире форм"), ("1", "в мире без форм"),
    ("5", "нравственность"), ("2", "освобождение"), ("2", "смысл"), ("1", "жажда"), ("5", "в поток"),
    ("1", "сосредоточение"), ("1", "мудрость"), ("2", "Учение"), ("2", "перерождаются"), ("5", "везде"),
    ("1", "глаз"), ("1", "ухо"), ("1", "нос"), ("1", "язык"), ("1", "тело"), ("1", "звук"), ("1", "запах"),
    ("1", "вкус"), ("1", "осязаемое"), ("1", "видимая форма"),
]


def main():
    B.check_crossbook()
    D.check_crossbook()
    D.check_crossbook(CROSSBOOK)
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    ru = translate_text(src)
    B.check_pair(src, ru, CHAPTER)
    pairs = [((B.PALI_DIR / n).read_text(encoding="utf-8"), (B.OUT_DIR / n).read_text(encoding="utf-8"))
             for n in B.SAMPLE_FILES + ["2-01-khandhayamaka.md", "7-01-anusayayamaka.md"]]
    D.consistency(pairs + [(src, ru)])
    with open(B.OUT_DIR / CHAPTER, "w", encoding="utf-8", newline="\n") as f:
        f.write(ru)
    print("written", B.OUT_DIR / CHAPTER, "lines", len(ru.split("\n")))
    for s in dict.fromkeys(SLIP_LOG):
        print("slip:", s)
    print("cross-book asserts OK; per-line checks OK; consistency OK")


if __name__ == "__main__":
    main()
