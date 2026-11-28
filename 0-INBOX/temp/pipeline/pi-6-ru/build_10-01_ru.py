"""Russian plain zero-shot of pi-6 (Yamaka): chapter 10-01-indriyayamaka.md (Indriyayamaka, paṇṇattivāra).

Family A (paṇṇattivāra) comes from build_2-01_ru (frames imported, never retyped); the Āyatana helpers
(qualifiers «Божественный глаз, глаз мудрости», the sota pun, ay_sentence, pavatti persons / places) from
build_3-01_ru; the person / place shape from build_7-01_ru (via build_2-01_ru.C). This module SETS THE INDRIYA
MEMBERS for 10-01 … 10-13: the 22 faculty names are taken from the pi-2 Indriyavibhaṅga Russian and asserted.

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_10-01_ru.py
Import: I = importlib.import_module("build_10-01_ru")   (importing never writes any file)

Exposed for 10-02 … 10-13
  Members      IN_ORDER (22 keys, Pāli order), IN_PALI (cakkhundriyaṃ …), IN_K (faculties, D.N dicts),
               IN_X (bare words), IN_X_FORMS, IN_G_SG / IN_G_PL (indriyaṃ / indriyā), IN_LEX, IN_QUAL, IN_PUN,
               IN_PV_SUBJ (pavattivāra subjects: Pāli faculty -> N), IN_UDDESA / IN_UDDESA_VAR (the 22-list),
               in_list(members) «A, B и C», IN_GEN_PL (itthī / purisa, proposal)
  Persons      IN_HAVE (sa-X-ka / a-X-ka from build_3-01_ru.AY_HAVE), IN_PLANES (= build_3-01_ru.AY_PLANES)
  Frames       IN_YAM_BOTH («То ухо, которое является способностью, является и ухом, и способностью.»),
               IN_REST_X_NOT («Остальное ухо не является способностью.»), DEM_REL, REST_ADJ
  Headings     IN_HEADINGS (sample + Suddhindriyavāro, Pavattivāro), heading()
  Closings     IN_MULAKA ("(Cakkhundriyamūlakaṃ)" = «(На основе способности глаза)»), TAILS
  Driver       IN_CFG, in_question(), in_sentence(), segments(), tr_line(text, cfg), translate_text(src, cfg)
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

D = importlib.import_module("build_2-01_ru")     # family A (+ B)
A = importlib.import_module("build_3-01_ru")     # Āyatana qualifiers, pun, ay_sentence, persons / places
C = D.C                                          # build_7-01_ru: person / place shape, NO, NATTHI, heading_case
CHAPTER = "10-01-indriyayamaka.md"
cap, lower1, N = B.cap, C.lower1, D.N
SLIP_LOG = []

# =============================================================================================
# Members: the 22 faculties (names from pi-2 Indriyavibhaṅga ^2-221 / ^2-1 Russian, asserted below)
# =============================================================================================
IN_ORDER = ["cakkhu", "sota", "ghāna", "jivhā", "kāya", "mana", "itthī", "purisa", "jīvita", "sukha", "dukkha",
            "somanassa", "domanassa", "upekkhā", "saddhā", "vīriya", "sati", "samādhi", "paññā",
            "anaññātaññassāmīti", "añña", "aññātāvī"]
IN_PALI = dict(zip(IN_ORDER, [
    "cakkhundriyaṃ", "sotindriyaṃ", "ghānindriyaṃ", "jivhindriyaṃ", "kāyindriyaṃ", "manindriyaṃ",
    "itthindriyaṃ", "purisindriyaṃ", "jīvitindriyaṃ", "sukhindriyaṃ", "dukkhindriyaṃ", "somanassindriyaṃ",
    "domanassindriyaṃ", "upekkhindriyaṃ", "saddhindriyaṃ", "vīriyindriyaṃ", "satindriyaṃ", "samādhindriyaṃ",
    "paññindriyaṃ", "anaññātaññassāmītindriyaṃ", "aññindriyaṃ", "aññātāvindriyaṃ"]))
IN_K_GEN = {   # «способность + genitive» (pi-2); jīvitindriya is the adjective form «жизненная способность»
    "cakkhu": "глаза", "sota": "уха", "ghāna": "носа", "jivhā": "языка", "kāya": "тела", "mana": "ума",
    "itthī": "женственности", "purisa": "мужественности", "sukha": "удовольствия", "dukkha": "боли",
    "somanassa": "радости", "domanassa": "уныния", "upekkhā": "невозмутимости", "saddhā": "веры",
    "vīriya": "усердия", "sati": "осознанности", "samādhi": "сосредоточения", "paññā": "мудрости",
    "anaññātaññassāmīti": "познания непознанного", "añña": "окончательного знания",
    "aññātāvī": "обладателя окончательного знания",
}
IN_K = {m: N("способность " + g, "способностью " + g, "способности " + g, "f") for m, g in IN_K_GEN.items()}
IN_K["jīvita"] = N("жизненная способность", "жизненной способностью", "жизненной способности", "f")
IN_K = {m: IN_K[m] for m in IN_ORDER}
IN_G_SG = N("способность", "способностью", "способности", "f")         # indriyaṃ
IN_G_PL = N("способности", "способностями", "способностей", "pl")      # indriyā / indriye

# Bare words of the paṇṇattivāra. The six sense words are the Āyatana bare words of build_3-01_ru; the others
# are the noun inside the pi-2 faculty name (sukha = «удовольствие» as in «способность удовольствия», so that
# "Sukhaṃ sukhindriyaṃ? Āmantā." reads as a plain yes; aññaṃ = «окончательное знание» pi-1;
# aññātāvī = «обладатель окончательного знания» pi-1/pi-2; anaññātaññassāmīti = «познание непознанного»).
IN_X = {m: A.AY_X[m] for m in ("cakkhu", "sota", "ghāna", "jivhā", "kāya", "mana")}
IN_X.update({
    "itthī": N("женщина", "женщиной", "женщины", "f"),
    "purisa": N("мужчина", "мужчиной", "мужчины", "m"),
    "jīvita": N("жизнь", "жизнью", "жизни", "f"),
    "sukha": N("удовольствие", "удовольствием", "удовольствия", "n"),
    "dukkha": N("боль", "болью", "боли", "f"),
    "somanassa": N("радость", "радостью", "радости", "f"),
    "domanassa": N("уныние", "унынием", "уныния", "n"),
    "upekkhā": N("невозмутимость", "невозмутимостью", "невозмутимости", "f"),
    "saddhā": N("вера", "верой", "веры", "f"),
    "vīriya": N("усердие", "усердием", "усердия", "n"),
    "sati": N("осознанность", "осознанностью", "осознанности", "f"),
    "samādhi": N("сосредоточение", "сосредоточением", "сосредоточения", "n"),
    "paññā": N("мудрость", "мудростью", "мудрости", "f"),
    "anaññātaññassāmīti": N("познание непознанного", "познанием непознанного", "познания непознанного", "n"),
    "añña": N("окончательное знание", "окончательным знанием", "окончательного знания", "n"),
    "aññātāvī": N("обладатель окончательного знания", "обладателем окончательного знания",
                  "обладателя окончательного знания", "m"),
})
IN_X = {m: IN_X[m] for m in IN_ORDER}
IN_GEN_PL = {"itthī": "женщин", "purisa": "мужчин"}     # proposal for the pavatti persons (itthīnaṃ / purisānaṃ)
IN_X_FORMS = {
    "cakkhu": ["cakkhu", "cakkhū", "cakkhuṃ"], "sota": ["sotaṃ"], "ghāna": ["ghānaṃ"], "jivhā": ["jivhā", "jivhaṃ"],
    "kāya": ["kāyo", "kāyaṃ"], "mana": ["mano", "manaṃ"], "itthī": ["itthī", "itthiṃ"], "purisa": ["puriso", "purisaṃ"],
    "jīvita": ["jīvitaṃ"], "sukha": ["sukhaṃ"], "dukkha": ["dukkhaṃ"], "somanassa": ["somanassaṃ"],
    "domanassa": ["domanassaṃ"], "upekkhā": ["upekkhā", "upekkhaṃ"], "saddhā": ["saddhā", "saddhaṃ"],
    "vīriya": ["vīriyaṃ"], "sati": ["sati", "satī", "satiṃ"], "samādhi": ["samādhi", "samādhī", "samādhiṃ"],
    "paññā": ["paññā", "paññaṃ"], "anaññātaññassāmīti": ["anaññātaññassāmīti", "anaññātaññassāmītiṃ"],
    "añña": ["aññaṃ"], "aññātāvī": ["aññātāvī", "aññātāviṃ"],
}
IN_LEX = {"indriyaṃ": IN_G_SG, "indriyā": IN_G_PL, "indriye": IN_G_PL}
for _m, _forms in IN_X_FORMS.items():
    for _f in _forms:
        IN_LEX[_f] = IN_X[_m]
    IN_LEX[IN_PALI[_m]] = IN_K[_m]
IN_PV_SUBJ = {IN_PALI[m]: IN_K[m] for m in IN_ORDER}
GROUPS = (IN_G_SG, IN_G_PL)


def in_list(members, key="nom"):
    """['cakkhu', 'sota', 'ghāna'] -> «способность глаза, способность уха и способность носа»."""
    return A.ru_and([IN_K[m][key] for m in members])


# Bāvīsatindriyāni – … (pi-2 ^2-221 verbatim; with the variant of 10-01 ^6-10-1 after «способность усердия»)
IN_UDDESA = "Двадцать две способности – " + in_list(IN_ORDER) + "."
IN_VAR_VIRIYA = D.variant_ru("viriyindiyaṃ (sī. syā.)", "написания")     # spelling-only variant (pi-2 kind)
IN_UDDESA_VAR = IN_UDDESA.replace(IN_K["vīriya"]["nom"] + ",", IN_K["vīriya"]["nom"] + " " + IN_VAR_VIRIYA + ",", 1)
IN_UDDESA_PALI = "Bāvīsatindriyāni – " + ", ".join(IN_PALI[m] for m in IN_ORDER) + "."
IN_UDDESA_PALI_VAR = IN_UDDESA_PALI.replace("vīriyindriyaṃ,", "vīriyindriyaṃ [viriyindiyaṃ (sī. syā.)],", 1)

# =============================================================================================
# Family A additions (qualifiers, new frames)
# =============================================================================================
IN_QUAL = {q: A.AY_QUAL[q] for q in ("dibbacakkhu paññācakkhu", "dibbasotaṃ taṇhāsotaṃ")}   # 3-01 (pi-5)
for _w, _n in IN_LEX.items():                       # a bare member as the subject: «Способность женственности не …»
    if _n not in GROUPS:
        IN_QUAL[_w] = (cap(_n["nom"]), _n["g"])
for _m in IN_ORDER:                                 # "X-indriyaṃ ṭhapetvā avaseso" = D.APART «Кроме …, остальное»
    IN_QUAL[f"{IN_PALI[_m]} ṭhapetvā avaseso"] = (D.APART.format(a_gen=IN_K[_m]["gen"]), "n")
IN_PUN = dict(A.AY_QUAL_PUN)                        # «Божественное ухо, поток жажды являются «ухом»» (3-01)

# "Yaṃ sotaṃ indriyaṃ taṃ sotañceva indriyañca." / "Avasesaṃ sotaṃ na indriyaṃ." (Russian gender of the member)
DEM_REL = {"m": ("Тот", "который"), "f": ("Та", "которая"), "n": ("То", "которое"), "pl": ("Те", "которые")}
REST_ADJ = {"m": "Остальной", "f": "Остальная", "n": "Остальное", "pl": "Остальные"}
IN_YAM_BOTH = "{dem} {x_nom}, {rel} {x_cop} {k_instr}, {x_cop} и {x_instr}, и {k2_instr}."
IN_REST_X_NOT = "{rest} {x_nom} не {x_cop} {k_instr}."
YAM_RE = re.compile(r"(?:Yaṃ|Yo|Yā) (\S+) (\S+) (?:taṃ|so|sā) (\S+) ceva (\S+) ca")
REST_X_RE = re.compile(r"[Aa]vases(?:aṃ|o|ā) (\S+) na (\S+)")
SHORT = {"Āmantā": B.AMANTA, "No": C.NO, "Natthi": C.NATTHI}

# =============================================================================================
# Persons / places for the pavattivāra (10-02 …): Āyatana descriptors and planes of build_3-01_ru
# =============================================================================================
IN_HAVE = {k: A.AY_HAVE[k] for k in ("cakkhuk", "sotak", "ghānak", "cittak")}
IN_PLANES = A.AY_PLANES

# =============================================================================================
# Headings and closings
# =============================================================================================
IN_EXTRA_HEADINGS = {   # not in build_sample_ru.SECTION_HEADINGS (shaped like Suddhakhandhavāro / 3-01)
    "Suddhindriyavāro": "Раздел о способностях как таковых",
    "Pavattivāro": "Раздел о протекании",                       # coordinator rules (Pavattivāro «Раздел о протекании»)
}
IN_HEADINGS = dict(B.SECTION_HEADINGS, **IN_EXTRA_HEADINGS)
HEAD_RE = A.HEAD_RE


def heading(text, heads=None):
    heads = IN_HEADINGS if heads is None else heads
    hashes, lab, body = HEAD_RE.fullmatch(text).groups()
    ru = B.YAMAKA_TITLES[body] if body in B.YAMAKA_TITLES else C.heading_case(heads[body])
    if lab:
        ru = f"({lab if lab.isdigit() else B.LETTERS[lab]}) " + ru
    return f"{hashes} {ru}"


IN_MULAKA = {cap(IN_PALI[m][:-1] + "mūlakaṃ"): A.AY_MULAKA_FRAME.format(gen=IN_K[m]["gen"]) for m in IN_ORDER}
TAILS = dict(IN_MULAKA, **{"Saṃkhittaṃ": A.SAMKHITTAM})
TAIL_RE = re.compile(r"(.*?) ?\((" + "|".join(TAILS) + r")\)(\.?)")

# =============================================================================================
# Questions, sentences, line segments
# =============================================================================================
SLIPS = {   # plain spelling slips / missing punctuation, rendered as meant (reported)
    "anaññātaññāssāmīti": "anaññātaññassāmīti",                                   # ^6-10-3 (ā for a)
    "ṭhapetvā avaseso kāyo na kāyindriyaṃ.": "ṭhapetvā avaseso kāyo, na kāyindriyaṃ.",   # ^6-10-100 missing comma
}


def preprocess(text):
    for a, b in SLIPS.items():
        if a in text:
            SLIP_LOG.append(f"{a!r} rendered as {b!r}")
            text = text.replace(a, b)
    return text


def in_question(body, cfg=None):
    """Pāli question body (no label, no '?') -> (Russian question with '?', y noun or None)."""
    cfg = IN_CFG if cfg is None else cfg
    lb = lower1(body.strip())
    if lb.startswith(("yassa", "yattha")):
        return D.pv_question(lb, cfg["pv_subj"])
    return D.pada_question(lb, cfg["lex"]), None


def in_sentence(body, cfg=None, y_ctx=None):
    """One Pāli answer sentence (final '.' removed) -> Russian sentence with '.'."""
    cfg = IN_CFG if cfg is None else cfg
    if body in SHORT:
        return SHORT[body]
    s = D._norm(body)
    m = YAM_RE.fullmatch(s)
    if m:
        x, k, x2, k2 = (D.lex_get(m.group(i), cfg["lex"]) for i in range(1, 5))
        assert x is x2 and k is k2, body
        dem, rel = DEM_REL[x["g"]]
        return IN_YAM_BOTH.format(dem=dem, x_nom=x["nom"], rel=rel, x_cop=x["cop"], k_instr=k["instr"],
                                  x_instr=x["instr"], k2_instr=k2["instr"])
    m = REST_X_RE.fullmatch(s)
    if m:
        x, k = D.lex_get(m.group(1), cfg["lex"]), D.lex_get(m.group(2), cfg["lex"])
        if x not in GROUPS:
            return IN_REST_X_NOT.format(rest=REST_ADJ[x["g"]], x_nom=x["nom"], x_cop=x["cop"], k_instr=k["instr"])
    return A.ay_sentence(body, cfg, y_ctx)


ELL_TOK = re.compile(r"…[Pp]e…\.?")
SEG_RE = re.compile(r"(\s*)(…[Pp]e…\.?|[^?.…]+?(?:[?.]|(?=\s*…)))")


def segments(plain, cfg=None):
    """A line (label and variants removed) cut into questions, sentences and "…pe…" markers; the spacing between
    them is kept as in the Pāli. A sentence that runs straight into "…pe…" keeps no full stop (as written)."""
    cfg = IN_CFG if cfg is None else cfg
    out, pos, y, first = [], 0, None, True
    while pos < len(plain):
        m = SEG_RE.match(plain, pos)
        if not m or m.end() == pos:
            raise ValueError(f"line not segmented at {plain[pos:]!r}")
        sep, tok = m.groups()
        pos = m.end()
        if ELL_TOK.fullmatch(tok):
            ru = "…"
        else:
            if tok.endswith("?"):
                ru, y = in_question(tok[:-1], cfg)
            elif tok.endswith("."):
                ru = in_sentence(tok[:-1], cfg, y)
            else:
                ru = in_sentence(tok, cfg, y)
                assert ru.endswith("."), ru
                ru = ru[:-1]
            ru = cap(ru) if (first or tok[0].isupper()) else lower1(ru)
        out.append(sep + ru)
        first = False
    return "".join(out)


LABEL_RE = re.compile(r"\((\w+)\) (.*)")


def tr_line(text, cfg=None):
    """Translate one Pāli line (block ID removed)."""
    cfg = IN_CFG if cfg is None else cfg
    if not text.strip():
        return ""
    if text in cfg["fixed"]:
        return cfg["fixed"][text]
    if text in B.FIXED:
        return B.FIXED[text]
    if text.startswith("#"):
        return heading(text, cfg.get("headings"))
    text = preprocess(text)
    m = TAIL_RE.fullmatch(text)
    if m:
        return tr_line(m.group(1), cfg) + f" ({TAILS[m.group(2)]}){m.group(3)}"
    label = ""
    m = LABEL_RE.fullmatch(text)
    if m and m.group(1) in B.LETTERS:
        label, text = f"({B.LETTERS[m.group(1)]}) ", m.group(2)
        if m.group(1) == "Ka" and (" vā pana " in text or text.startswith(("indriyā ", "na indriyā "))):
            SLIP_LOG.append(f"label (Ka) on a (Kha) question (kept as written): {text[:60]}")
    variants = D.VARIANT_RE.findall(text)
    ru = segments(D.VARIANT_RE.sub("", text), cfg)
    for v in variants:
        anchor = cfg["variant_anchors"][v]
        assert anchor in ru, (anchor, ru)
        kind = cfg.get("variant_kind", {}).get(v, D.VARIANT_KIND_DEFAULT)
        ru = ru.replace(anchor, anchor + " " + D.variant_ru(v, kind), 1)
    return label + ru


def translate_text(src, cfg=None):
    out = []
    for line in src.split("\n"):
        body, bid = B.ID_RE.match(line).groups()
        out.append(tr_line(body, cfg) + (bid or ""))
    return unicodedata.normalize("NFC", "\n".join(out))


IN_CFG = {
    "lex": IN_LEX,
    "qual": IN_QUAL,
    "pun": IN_PUN,
    "pv_subj": IN_PV_SUBJ,
    "planes": IN_PLANES,
    "have": IN_HAVE,
    "headings": IN_HEADINGS,
    "fixed": {
        IN_UDDESA_PALI_VAR: IN_UDDESA_VAR,
        IN_UDDESA_PALI: IN_UDDESA,
        "Paṇṇattiuddesavāro.": D.PANNATTI_UDDESAVARO,
        "Paṇṇattiniddesavāro.": D.PANNATTI_NIDDESAVARO,
    },
    "variant_anchors": {
        "avasesā kāyo (sī. syā. ka.)": D.APART.format(a_gen=IN_K["kāya"]["gen"]),   # «Кроме способности тела, остальное»
    },
}

# =============================================================================================
# Checks
# =============================================================================================
CROSSBOOK = [   # strings taken from the approved pi-1 … pi-5 Russian rails (book, exact substring)
    ("2", IN_UDDESA), ("2", "способность усердия [вариант написания (Sī., Syā.): viriyindriyaṃ]"),
    ("1", "жизненная способность"), ("2", "способностями"), ("1", "способностей"),
    ("2", "женщина"), ("2", "мужчина"), ("1", "жизнь"), ("1", "удовольствие"), ("1", "боль"), ("1", "радость"),
    ("1", "уныние"), ("1", "невозмутимость"), ("1", "вера"), ("1", "усердие"), ("1", "осознанность"),
    ("1", "сосредоточение"), ("1", "мудрость"), ("1", "окончательное знание"),
    ("1", "обладающих окончательным знанием"), ("2", "познания непознанного"),
    ("5", "божественный глаз"), ("5", "глаз мудрости"), ("5", "божественное ухо"), ("1", "жажда"),
    ("1", "глаз"), ("1", "ухо"), ("1", "нос"), ("1", "язык"), ("1", "тело"), ("1", "ум"),
]


def check_members():
    """The 22 names, in order, are exactly the pi-2 Indriyavibhaṅga list (both of its lines)."""
    ru2 = (B.RAILS["2"] / "5-indriyavibhango.md").read_text(encoding="utf-8")
    lists = [ln for ln in ru2.split("\n") if ln.startswith("Двадцать две способности – ")]
    plain = [B.ID_ANY.sub("", ln).strip() for ln in lists if "[" not in ln]
    var = [B.ID_ANY.sub("", ln).strip() for ln in lists if "[" in ln]
    assert IN_UDDESA in plain, (IN_UDDESA, plain)
    assert IN_UDDESA_VAR.replace("viriyindiyaṃ", "viriyindriyaṃ") in var, (IN_UDDESA_VAR, var)
    names = IN_UDDESA[len("Двадцать две способности – "):-1].replace(" и способность обладателя", ", способность обладателя")
    assert names.split(", ") == [IN_K[m]["nom"] for m in IN_ORDER] and len(IN_ORDER) == 22
    return True


def main():
    B.check_crossbook()
    D.check_crossbook()
    D.check_crossbook(A.CROSSBOOK)
    D.check_crossbook(CROSSBOOK)
    check_members()
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    ru = translate_text(src)
    B.check_pair(src, ru, CHAPTER)
    pairs = [((B.PALI_DIR / n).read_text(encoding="utf-8"), (B.OUT_DIR / n).read_text(encoding="utf-8"))
             for n in B.SAMPLE_FILES + ["2-01-khandhayamaka.md", "3-01-ayatanayamaka.md"]]
    D.consistency(pairs + [(src, ru)])
    with open(B.OUT_DIR / CHAPTER, "w", encoding="utf-8", newline="\n") as f:
        f.write(ru)
    print("written", B.OUT_DIR / CHAPTER, "lines", len(ru.split("\n")))
    for s in dict.fromkeys(SLIP_LOG):
        print("slip:", s)
    print("cross-book asserts OK; member asserts OK; per-line checks OK; consistency OK")


if __name__ == "__main__":
    main()
