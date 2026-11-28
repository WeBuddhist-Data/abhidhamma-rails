"""Russian plain zero-shot of pi-6 (Yamaka): chapter 4-dhatuyamaka.md (the whole Dhātuyamaka).

Families A (paṇṇattivāra) and B (pavattivāra) come from build_2-01_ru through build_3-01_ru (the Āyatana driver
tr_line / ay_answers / ay_pv_sentence, imported, never edited), family E (pariññāvāra) from build_2-02_ru, the
person / place shape from build_7-01_ru. This module only adds the eighteen elements (pi-2 names), the bare
words of the consciousness elements, the abbreviated chain lines and the chapter's notes.

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_4_ru.py [--probe [--show] | --dry | --wide]
Import: importlib.import_module("build_4_ru")   (importing never writes any file)

Exposed
  Members   DH_ORDER, DH_PALI, DH_K_GEN, DH_K, DH_X, DH_G_SG, DH_G_PL, DH_LEX, DH_UDDESA, DH_PJ_OBJ
  Driver    DH_CFG, tr_line(text, cfg), translate_text(src, cfg), chain(text, mode)
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

A = importlib.import_module("build_3-01_ru")     # Āyatana driver and members (closest parallel)
D = A.D                                          # build_2-01_ru: families A + B
C = A.C                                          # build_7-01_ru: person / place shape
E = importlib.import_module("build_2-02_ru")     # family E (pariññāvāra)
CHAPTER = "4-dhatuyamaka.md"
cap, lower1, N = B.cap, C.lower1, D.N
SLIP_LOG = []

# =============================================================================================
# Members: the eighteen elements (names from pi-2 Dhātuvibhaṅga ^2-183, asserted below)
# =============================================================================================
DH_ORDER = ["cakkhu", "sota", "ghāna", "jivhā", "kāya", "rūpa", "sadda", "gandha", "rasa", "phoṭṭhabba",
            "cakkhuviññāṇa", "sotaviññāṇa", "ghānaviññāṇa", "jivhāviññāṇa", "kāyaviññāṇa", "mano", "manoviññāṇa",
            "dhamma"]                                     # order of the Pāli uddesa of this chapter
DH_PALI = {m: m + "dhātu" for m in DH_ORDER}             # cakkhudhātu …
DH_K_GEN = {"cakkhu": "глаза", "sota": "уха", "ghāna": "носа", "jivhā": "языка", "kāya": "тела",
            "rūpa": "видимых форм", "sadda": "звуков", "gandha": "запахов", "rasa": "вкусов",
            "phoṭṭhabba": "осязаемого", "cakkhuviññāṇa": "зрительного сознания",
            "sotaviññāṇa": "слухового сознания", "ghānaviññāṇa": "обонятельного сознания",
            "jivhāviññāṇa": "вкусового сознания", "kāyaviññāṇa": "осязательного сознания", "mano": "ума",
            "manoviññāṇa": "умственного сознания", "dhamma": "объектов ума"}
DH_K = {m: N("элемент " + g, "элементом " + g, "элемента " + g, "m") for m, g in DH_K_GEN.items()}
DH_G_SG = N("элемент", "элементом", "элемента", "m")           # dhātu
DH_G_PL = N("элементы", "элементами", "элементов", "pl")       # dhātū
# Bare words of the paṇṇattivāra: the twelve shared with the Āyatanayamaka are 3-01's (identical Russian);
# the five consciousnesses as pi-2 (1-khandhavibhango: зрительное сознание … умственное сознание).
_AY = {"mano": "mana"}
DH_X = {m: A.AY_X[_AY.get(m, m)] for m in DH_ORDER if _AY.get(m, m) in A.AY_X}
DH_X.update({
    "cakkhuviññāṇa": N("зрительное сознание", "зрительным сознанием", "зрительного сознания", "n"),
    "sotaviññāṇa": N("слуховое сознание", "слуховым сознанием", "слухового сознания", "n"),
    "ghānaviññāṇa": N("обонятельное сознание", "обонятельным сознанием", "обонятельного сознания", "n"),
    "jivhāviññāṇa": N("вкусовое сознание", "вкусовым сознанием", "вкусового сознания", "n"),
    "kāyaviññāṇa": N("осязательное сознание", "осязательным сознанием", "осязательного сознания", "n"),
    "manoviññāṇa": N("умственное сознание", "умственным сознанием", "умственного сознания", "n"),
})
assert set(DH_X) == set(DH_ORDER)
DH_X_FORMS = {m: A.AY_X_FORMS[_AY.get(m, m)] for m in DH_ORDER if _AY.get(m, m) in A.AY_X_FORMS}
DH_X_FORMS.update({m: [m + "ṃ"] for m in DH_ORDER if m.endswith("viññāṇa")})
DH_LEX = {"dhātu": DH_G_SG, "dhātuṃ": DH_G_SG, "dhātū": DH_G_PL,
          "dhātūti": DH_G_SG}     # "cakkhu dhātūti?" = dhātu + ti (singular, as 3-01's "āyatananti")
for _m, _forms in DH_X_FORMS.items():
    for _f in _forms:
        DH_LEX[_f] = DH_X[_m]
    for _end in ("dhātu", "dhātū", "dhātuṃ"):          # -dhātū only before -ti ("cakkhudhātūti")
        DH_LEX[_m + _end] = DH_K[_m]
DH_PV_SUBJ = {DH_PALI[m]: DH_K[m] for m in DH_ORDER}
DH_PJ_OBJ = {DH_PALI[m] + "ṃ": DH_K[m]["nom"] for m in DH_ORDER}   # accusative (masc. inanimate = nom.)

# Aṭṭhārasa dhātuyo – … (pi-2 ^2-183 shape and names; order of this chapter; «и» before the last as pi-2)
DH_UDDESA_PALI = "Aṭṭhārasa dhātuyo – " + ", ".join(DH_PALI[m] for m in DH_ORDER) + "."
DH_UDDESA = ("Восемнадцать элементов – " + ", ".join(DH_K[m]["nom"] for m in DH_ORDER[:-1])
             + " и " + DH_K[DH_ORDER[-1]]["nom"] + ".")

# Qualifiers of the paṇṇatti niddesa: 3-01's named ones (dibbacakkhu …) and "X-dhātuṃ ṭhapetvā avaseso".
DH_QUAL = {k: v for k, v in A.AY_QUAL.items() if "ṭhapetvā" not in k}
for _m in DH_ORDER:
    for _end in ("avaseso", "avasesaṃ"):
        DH_QUAL[f"{DH_PALI[_m]}ṃ ṭhapetvā {_end}"] = (D.APART.format(a_gen=DH_K[_m]["gen"]), "n")

# =============================================================================================
# Headings
# =============================================================================================
DH_EXTRA_HEADINGS = {   # shaped like Suddhakhandhavāro / Suddhāyatanavāro (sample, 3-01)
    "Suddhadhātuvāro": "Раздел об элементах как таковых",
    "Suddhadhātumūlacakkavāro": "Круговой раздел на основе элементов как таковых",
}
DH_HEADINGS = dict(B.SECTION_HEADINGS, **DH_EXTRA_HEADINGS)


def heading(text):
    hashes, lab, body = A.HEAD_RE.fullmatch(text).groups()
    ru = B.YAMAKA_TITLES[body] if body in B.YAMAKA_TITLES else C.heading_case(DH_HEADINGS[body])
    if lab:
        ru = f"({lab if lab.isdigit() else B.LETTERS[lab]}) " + ru
    return f"{hashes} {ru}"


# =============================================================================================
# Abbreviated chain lines: "A?…pe… b?… C?…" / "Sotaviññāṇaṃ…pe… ghānaviññāṇaṃ…." / "X ṭhapetvā…pe… y…"
# Every "…pe…" / "…" / final "…." -> «…»; each piece keeps the case of its Pāli first letter.
# =============================================================================================
SEP_RE = re.compile(r"(…(?:[Pp]e…)?\.?)")
KROME = D.APART.split(" ")[0]                      # «Кроме» (ṭhapetvā)


def _w(w):
    return D.lex_get(w, DH_LEX)


def piece(core, mode):
    """One piece between ellipses. mode "q": questions / bare nouns; "apart": "X ṭhapetvā" / "x"."""
    q = core.endswith("?")
    body = core[:-1] if q else core
    w = body.split()
    if mode == "apart":
        assert not q and (len(w) == 1 or (len(w) == 2 and w[1] == "ṭhapetvā")), core
        g = _w(w[0])["gen"]
        return f"{KROME} {g}" if len(w) == 2 else g
    if len(w) >= 3 or (len(w) == 2 and w[0].lower() != "na"):
        r = D.pada_question(lower1(body), DH_LEX)               # «X является Y?» / «То, что не является …?»
        return r if q else r[:-1]
    if len(w) == 2:                                             # "Na ghānaṃ?" = «Не нос?»
        return "не " + _w(w[1])["nom"] + ("?" if q else "")
    return _w(w[0])["nom"] + ("?" if q else "")                 # "Ghānaviññāṇaṃ?" = «Обонятельное сознание?»


def chain(text, mode="q"):
    amanta = text.endswith("? Āmantā.")
    if amanta:
        text = text[: -len(" Āmantā.")]
    parts = SEP_RE.split(text)
    out = []
    for i, p in enumerate(parts):
        if i % 2:
            out.append("…")
            continue
        if not p.strip():
            out.append(p)
            continue
        core = p.strip()
        lead, trail = p[: len(p) - len(p.lstrip())], p[len(p.rstrip()):]
        ru = piece(core, mode)
        out.append(lead + (cap(ru) if core[0].isupper() else lower1(ru)) + trail)
    return "".join(out) + (" " + B.AMANTA if amanta else "")


# =============================================================================================
# Notes of this chapter (composed from approved headings and earlier frames)
# =============================================================================================
AY_TITLE, DH_TITLE = B.YAMAKA_TITLES["Āyatanayamakaṃ"], B.YAMAKA_TITLES["Dhātuyamakaṃ"]
assert AY_TITLE.startswith("Парные вопросы ") and DH_TITLE.startswith("Парные вопросы ")
AY_PREP = AY_TITLE.replace("Парные вопросы", "парных вопросах", 1)     # āyatanayamake
DH_PREP = DH_TITLE.replace("Парные вопросы", "парных вопросах", 1)     # dhātuyamake
AY_GEN = AY_TITLE.replace("Парные вопросы", "парных вопросов", 1)      # āyatanayamakassa
DH_GEN = DH_TITLE.replace("Парные вопросы", "парных вопросов", 1)      # dhātuyamakassa
AY_ACC, DH_ACC = lower1(AY_TITLE), lower1(DH_TITLE)                    # āyatanayamakaṃ / dhātuyamakaṃ
CAKKAM = A.CAKKAM_BANDHITABBAM[1:-1]                                   # «Круг следует замкнуть»
PANNATTI = "обозначения"                                              # paṇṇatti (Paṇṇattivāro «… об обозначениях»)
AMANTA_Q = "«" + B.AMANTA[:-1] + "»"                                  # «Да» (as 3-01 CAKKAM_AMANTA)
UBHATO = "в обоих вопросах"                                           # ubhato (the (а) and (б) question)
VIBHATTA_PL = "разобраны"                                             # vibhattaṃ (2-02 «разобран», plural subject)
VIBHAJITABBA = "следует разбирать"                                    # vibhajitabbaṃ (2-02)
assert ("разобран {what}, так же " + VIBHAJITABBA) in E.VIBHAJITABBAM_FRAME
SADISA = "такой же, как"                                              # -sadisa (m.); n. «такое же, как»
assert A.CAKKAM_AMANTA.endswith(f"«{B.AMANTA[:-1]}»).")

SUFFIX_NOTES = {   # notes closing a line: Pāli suffix -> Russian suffix
    " (Cakkaṃ bandhitabbaṃ).": f" ({CAKKAM}).",
    " (Jivhāpi ghānadhātusadisā).": f" ({cap(DH_X['jivhā']['nom'])} тоже {SADISA} {DH_K['ghāna']['nom']}).",
    " (Saddo ghānasadiso).": f" ({cap(DH_X['sadda']['nom'])} {SADISA} {DH_X['ghāna']['nom']}).",
    " (Phoṭṭhabbo ghānasadiso).": (f" ({cap(DH_X['phoṭṭhabba']['nom'])} "
                                   f"{SADISA.replace('такой', 'такое')} {DH_X['ghāna']['nom']})."),
}

NOTE_49_PALI = "(Yathā āyatanayamake cakkaṃ bandhitaṃ evamidha cakkaṃ bandhitabbaṃ.)"
NOTE_49 = f"(Как в {AY_PREP} круг замкнут, так же и здесь {lower1(CAKKAM)}.)"
NOTE_179_PALI = "Na jivhā… (saṃkhittaṃ [yaṃ saṃkhittaṃ (syā.)], ubhato āmantā)."
NOTE_215_PALI = "(Yathā āyatanayamake paṇṇatti evaṃ dhātuyamakepi paṇṇatti. Cakkaṃ bandhitabbaṃ)."
NOTE_215 = f"(Как {PANNATTI} в {AY_PREP}, так же и {PANNATTI} в {DH_PREP}. {CAKKAM})."
NOTE_223_PALI = "(Cakkaṃ bandhitabbaṃ, sabbe āmantā ubhatopi sesepi)."
NOTE_223 = f"({CAKKAM}, все ответы {AMANTA_Q} и {UBHATO}, и в остальных)."
NOTE_283_PALI = "(Yathā āyatanayamakassa paṇṇatti evaṃ dhātuyamakassa paṇṇatti vitthāretabbā)"
NOTE_283 = f"(Как {PANNATTI} {AY_GEN}, так же {C.VITTHARETABBAM} {PANNATTI} {DH_GEN})"
NOTE_309_PALI = ("(Yathā āyatanayamakaṃ vibhattaṃ evaṃ dhātuyamakampi vibhajitabbaṃ, sadisaṃ kātabbaṃ).")
NOTE_309 = f"(Как {VIBHATTA_PL} {AY_ACC}, так же {VIBHAJITABBA} и {DH_ACC}, излагая одинаково)."
PEYYALA = f"({DH_ACC} полны, с сокращением)"                         # (dhātuyamakaṃ paripuṇṇaṃ peyyālena)

# =============================================================================================
# Slips (rendered as meant; each must occur exactly once)
# =============================================================================================
SLIPS = [
    ("jivha ṭhapetvā", "jivhaṃ ṭhapetvā", "^6-4-15: 'jivha ṭhapetvā' = jivhaṃ ṭhapetvā (spelling slip)"),
]


def preprocess(text):
    for old, new, note in SLIPS:
        if old in text:
            text = text.replace(old, new)
            SLIP_LOG.append(note)
    return text


# =============================================================================================
# Config and driver
# =============================================================================================
DH_CFG = {
    "lex": DH_LEX,
    "qual": DH_QUAL,
    "pun": A.AY_QUAL_PUN,            # sota = ear and stream: «являются «ухом»» (3-01)
    "pv_subj": DH_PV_SUBJ,
    "planes": A.AY_PLANES,
    "have": A.AY_HAVE,               # sacakkhuka «с глазом», acakkhuka «без глаза», sacittaka «с умом» … (3-01)
    "pj_obj": DH_PJ_OBJ,
    "fixed": {},                     # filled below
    "variant_anchors": {
        "avaseso kāyo kāyo (syā.)": f"{KROME} {DH_K['kāya']['gen']}, остальное",
        "avaseso kāyo (syā.)": f"{KROME} {DH_X['kāya']['gen']} и {DH_K['kāya']['gen']}, остальное",
        "avasesā dhātū dhātū (syā.)": f"Остальные {DH_G_PL['nom']}",
    },
}


def ans(text, cfg=None):
    """Complete Pāli answer sentences -> Russian (3-01's ay_answers with the Dhātu config)."""
    return A.ay_answers(text, DH_CFG if cfg is None else cfg)


def line(text, cfg=None):
    return A.tr_line(text, DH_CFG if cfg is None else cfg)


def _q(body):
    return D.pada_question(lower1(body), DH_LEX)


def _fixed():
    var_46 = "[вариант чтения (Sī., Ka.): dhātu; следует сверить с другими парными вопросами]"
    q46 = _q("dhātū sotadhātu")
    assert q46.startswith(cap(DH_G_PL["nom"]) + " ")
    pj_q = E.pj_question("yo cakkhudhātuṃ parijānāti so sotadhātuṃ parijānātīti", DH_PJ_OBJ)
    s213 = "Dibbacakkhu paññācakkhu cakkhu, na cakkhudhātu. Cakkhudhātu cakkhu ceva cakkhudhātu ca."
    s236 = ("Cakkhuviññāṇadhātu dhātu ceva cakkhuviññāṇadhātu ca. Avasesā dhātū na cakkhuviññāṇadhātu.")
    s278 = "Cakkhuṃ ṭhapetvā avasesā dhātū na cakkhu, dhātu. Cakkhu ca dhātuñca ṭhapetvā avasesā na ceva cakkhu na ca dhātu."
    q278 = "Na dhātū na ghānadhātu…pe… na dhātū na dhammadhātūti? Āmantā."
    # ^6-4-17 first sentence: "Cakkhuṃ ṭhapetvā avasesā dhātū na cakkhudhātu." (as written; no ", dhātu")
    s275 = (D.APART_GROUP.format(a_gen=DH_X["cakkhu"]["gen"], g_nom=DH_G_PL["nom"])
            + f" не {DH_G_PL['cop']} {DH_K['cakkhu']['instr']}.")
    return {
        DH_UDDESA_PALI: DH_UDDESA,
        "Paṇṇattiuddesavāro.": D.PANNATTI_UDDESAVARO,
        "Paṇṇattiniddesavāro.": D.PANNATTI_NIDDESAVARO,
        "(Kha) dhātū [dhātu (sī. ka.) aññehi yamakehi saṃsanditabbaṃ] sotadhātu?…Pe…":
            f"({B.LETTERS['Kha']}) {cap(DH_G_PL['nom'])} {var_46} {q46[len(DH_G_PL['nom']) + 1:]}…",
        NOTE_49_PALI: NOTE_49,
        NOTE_179_PALI: (f"{chain('Na jivhā…')} ({lower1(A.SAMKHITTAM)} "
                        f"{D.variant_ru('yaṃ saṃkhittaṃ (syā.)')}, {UBHATO} {AMANTA_Q})."),
        NOTE_215_PALI: NOTE_215,
        NOTE_223_PALI: NOTE_223,
        NOTE_283_PALI: NOTE_283,
        NOTE_309_PALI: NOTE_309,
        # chains
        ("Ghānaṃ dhātu?…Pe… jivhā dhātu?… Kāyo dhātu?… Rūpaṃ dhātu?… Saddo dhātu?… Gandho dhātu?… Raso dhātu?… "
         "Phoṭṭhabbo dhātu?…"): None,
        "… Ghānaviññāṇaṃ?…Pe… jivhāviññāṇaṃ?… Kāyaviññāṇaṃ?": None,
        "… Na ghānaṃ?… Na jivhā?… Na kāyo?… Na rūpaṃ? … Na saddo?… Na gandho?… Na raso?… Na phoṭṭhabbo?": None,
        "… Na sotaviññāṇaṃ?…Pe… na ghānaviññāṇaṃ?… Na jivhāviññāṇaṃ?": None,
        "Sotaviññāṇaṃ…pe… ghānaviññāṇaṃ… jivhāviññāṇaṃ… kāyaviññāṇaṃ….": None,
        "Na saddo…pe… na gandho na gandhadhātūti? Āmantā.": None,
        "Na phoṭṭhabbo…pe… na cakkhuviññāṇaṃ na cakkhuviññāṇadhātūti? Āmantā.": None,
        "Na sotaviññāṇaṃ…pe… na ghānaviññāṇaṃ… na jivhāviññāṇaṃ… na kāyaviññāṇaṃ….": None,
        "Ghānaṃ…pe… jivhā… kāyo… rūpaṃ… saddo… gandho… raso… phoṭṭhabbo….": None,
        "Sotaṃ ṭhapetvā…pe… ghānaṃ ṭhapetvā…pe… jivhaṃ ṭhapetvā…pe….": chain(
            "Sotaṃ ṭhapetvā…pe… ghānaṃ ṭhapetvā…pe… jivhaṃ ṭhapetvā…pe….", "apart"),
        ("Rūpaṃ ṭhapetvā…pe… saddaṃ… gandhaṃ… rasaṃ… phoṭṭhabbaṃ… cakkhuviññāṇaṃ…pe… manoviññāṇaṃ "
         "ṭhapetvā…pe…."): chain("Rūpaṃ ṭhapetvā…pe… saddaṃ… gandhaṃ… rasaṃ… phoṭṭhabbaṃ… cakkhuviññāṇaṃ…pe… "
                                 "manoviññāṇaṃ ṭhapetvā…pe….", "apart"),
        # answer sentences + abbreviated question
        s213 + " Dhātū ghānadhātu…pe… dhātū dhammadhātūti?":
            ans(s213) + " " + chain("Dhātū ghānadhātu…pe… dhātū dhammadhātūti?"),
        s236 + " Sotaviññāṇaṃ…pe… ghānaviññāṇaṃ… jivhāviññāṇaṃ… kāyaviññāṇaṃ….":
            ans(s236) + " " + chain("Sotaviññāṇaṃ…pe… ghānaviññāṇaṃ… jivhāviññāṇaṃ… kāyaviññāṇaṃ…."),
        s278 + " " + q278: ans(s278) + " " + line(q278),
        ("Cakkhuṃ ṭhapetvā avasesā dhātū na cakkhudhātu. Cakkhuñca dhātuñca ṭhapetvā avasesā na ceva cakkhu "
         "na ca dhātu."):
            s275 + " " + ans("Cakkhuñca dhātuñca ṭhapetvā avasesā na ceva cakkhu na ca dhātu."),
        # pariññāvāra (family E, 2-02)
        "Yo cakkhudhātuṃ parijānāti so sotadhātuṃ parijānātīti? Āmantā.…Pe… (dhātuyamakaṃ paripuṇṇaṃ peyyālena).":
            f"{pj_q} {B.AMANTA}… {PEYYALA}.",
        "Dhātuyamakaṃ niṭṭhitaṃ.": B.YAMAKA_CLOSING_FRAME.format(title=DH_TITLE),
    }


def _fill_fixed():
    fx = _fixed()
    for k, v in list(fx.items()):
        if v is None:
            fx[k] = chain(k)
    return fx


DH_CFG["fixed"] = _fill_fixed()
assert DH_CFG["fixed"]["Dhātuyamakaṃ niṭṭhitaṃ."] == "Парные вопросы об элементах завершены."


def tr_line(text, cfg=None):
    """Translate one Pāli line (block ID removed)."""
    cfg = DH_CFG if cfg is None else cfg
    if not text.strip():
        return ""
    text = preprocess(text)
    if text in cfg["fixed"]:
        return cfg["fixed"][text]
    if text in B.FIXED:
        return B.FIXED[text]
    if text.startswith("#"):
        return heading(text)
    for p, r in SUFFIX_NOTES.items():
        if text.endswith(p):
            return tr_line(text[: -len(p)], cfg) + r
    return A.tr_line(text, cfg)


def translate_text(src, cfg=None):
    out = []
    for ln in src.split("\n"):
        body, bid = B.ID_RE.match(ln).groups()
        out.append(tr_line(body, cfg) + (bid or ""))
    return unicodedata.normalize("NFC", "\n".join(out))


# =============================================================================================
# Checks
# =============================================================================================
CROSSBOOK = [   # strings taken from the approved pi-1 … pi-5 Russian rails (book, exact substring)
    ("2", "Восемнадцать элементов – элемент глаза, "),
    ("2", "элемент тела, элемент осязаемого, элемент осязательного сознания, элемент ума, элемент объектов ума "
          "и элемент умственного сознания."),
    ("2", "зрительное сознание, слуховое сознание, обонятельное сознание, вкусовое сознание, осязательное сознание "
          "и умственное сознание"),
    ("1", "элементом глаза"), ("1", "элементом уха"), ("1", "элементом носа"), ("1", "элементом языка"),
    ("1", "элементом тела"), ("4", "элемент глаза"), ("5", "полностью понимает"), ("5", "Да."),
    ("2", "так же следует разбирать и здесь.)"), ("5", "так следует развернуть всё"),
] + [("2", DH_K[m]["nom"]) for m in DH_ORDER]


def probe(show=False):
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    bad = 0
    for n, ln in enumerate(src.split("\n"), 1):
        body, _ = B.ID_RE.match(ln).groups()
        try:
            r = tr_line(body)
            if show:
                print(f"{n}: {r}")
        except Exception as ex:  # noqa: BLE001
            bad += 1
            print(f"{n}: {type(ex).__name__}: {str(ex)[:300]}")
    print("failing lines:", bad)


def main():
    if "--probe" in sys.argv:
        probe("--show" in sys.argv)
        return
    B.check_crossbook()
    D.check_crossbook()
    D.check_crossbook(A.CROSSBOOK)
    D.check_crossbook(CROSSBOOK)
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    for old, _, note in SLIPS:
        assert src.count(old) == 1, f"slip pattern must occur once: {note}"
    lines = set()
    for ln in src.split("\n"):
        body = B.ID_RE.match(ln).group(1)
        for old, new, _ in SLIPS:
            body = body.replace(old, new)
        lines.add(body)
    unused = [k for k in DH_CFG["fixed"] if k not in lines]
    assert not unused, f"fixed keys not in the source: {unused}"
    ru = translate_text(src)
    B.check_pair(src, ru, CHAPTER)
    others = B.SAMPLE_FILES + ["2-01-khandhayamaka.md", "2-02-khandhayamaka.md", "3-01-ayatanayamaka.md",
                               "7-01-anusayayamaka.md"]
    pairs = [((B.PALI_DIR / n).read_text(encoding="utf-8"), (B.OUT_DIR / n).read_text(encoding="utf-8"))
             for n in others]
    D.consistency(pairs + [(src, ru)])
    if "--wide" in sys.argv:            # informative: identical Pāli lines against every other finished chapter
        for p in sorted(B.OUT_DIR.glob("*.md")):
            if p.name in others + [CHAPTER]:
                continue
            try:
                D.consistency([((B.PALI_DIR / p.name).read_text(encoding="utf-8"), p.read_text(encoding="utf-8")),
                               (src, ru)])
            except AssertionError as ex:
                print("CHECK", p.name, str(ex)[:400])
        print("wide check done")
        return
    if "--dry" in sys.argv:
        print(ru)
        return
    with open(B.OUT_DIR / CHAPTER, "w", encoding="utf-8", newline="\n") as f:
        f.write(ru)
    print("written", B.OUT_DIR / CHAPTER, "lines", len(ru.split("\n")))
    for s in dict.fromkeys(SLIP_LOG + D.SLIP_LOG):
        print("slip:", s)
    print("cross-book asserts OK; per-line checks OK; consistency OK (sample, 2-01, 2-02, 3-01, 7-01)")


if __name__ == "__main__":
    main()
