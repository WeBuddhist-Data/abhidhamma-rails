"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 3-01 (Āyatanayamaka, part 1) and the ĀYATANA module.

Families A (paṇṇattivāra) and B (pavattivāra) come from build_rails_2-01_vi (imported READ-ONLY, every frame string
taken from its functions). This file adds what the Āyatana chapters need on top of those frames:

  AYATANA (Members)          the twelve āyatana members, X-āyatana, āyatana / āyatanā (termbase; pi-1 names)
  AY_SPECIAL                 the «hiểu theo nghĩa …» subjects (Dibbacakkhu paññācakkhu …)
  AY_ATTRS / ATTR_JOIN       person attributes sacakkhukānaṃ «có mắt» … and how a run of them is joined
  PLANES_AY                  2-01's PLANES + rūpāvacara / kāmāvacara / arūpāvacara
  ay_persons / answer_head   person heads with attribute runs (else 2-01's persons / place_head)
  mulaka_label               (Cakkhāyatanamūlakaṃ) «(Phần dựa trên lĩnh vực mắt)»
  NOTES_AY                   the editorial notes (Cakkaṃ bandhitabbaṃ …)
  cut handling               …pe… / … cuts inside a line (pieces → units → frames), fragments of the 2-01 frames
  tr_line / build            the line translator (M, planes, fixed, variants are parameters)

Later Āyatana chapters (3-02 … 3-06):
    import importlib, sys
    sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai\\rails")
    A = importlib.import_module("build_rails_3-01_vi")
    segs = A.build("3-02-ayatanayamaka.md", fixed={...}, variant_kind={...})
A line, unit or word the parsers cannot place raises ValueError (no silent fallback). Importing writes nothing.

usage: python -I -X utf8 -B build_rails_3-01_vi.py
"""
import importlib
import re
import sys
import unicodedata

RAILS_DIR = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\rails"
if RAILS_DIR not in sys.path:
    sys.path.insert(0, RAILS_DIR)
import build_rails_sample_vi as S  # noqa: E402  (READ-ONLY)
B = importlib.import_module("build_rails_2-01_vi")   # READ-ONLY: family A / B frames (setter)
C = importlib.import_module("build_rails_7-01_vi")   # READ-ONLY: the shared shell (via 2-01)

cap = S.cap
LABEL = S.LABEL
CH = "3-01-ayatanayamaka.md"
N = "3-01"
YAMAKA = "Āyatana"
NOTES_MD = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/notes-rails-{N}.md"
ADH_DIR = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/adh-{N}"
SLIPS_SEEN = []

# ===============================================================================================================
# 1. Members (termbase; = pi-1 / pi-2 names: «lĩnh vực mắt» … «lĩnh vực đối tượng của ý»)
# ===============================================================================================================
AY_CLASS = "lĩnh vực nhận biết"           # āyatanaṃ / āyatanā (termbase); x_pl for the Suddhāyatana headings
# key: (organ / object word, termbase Vietnamese, Pāli forms of the simple word); the order is the uddesa order
TWELVE = [
    ("cakkhu", "mắt", ["cakkhu", "cakkhuṃ"]),
    ("sota", "tai", ["sotaṃ"]),
    ("ghāna", "mũi", ["ghānaṃ"]),
    ("jivhā", "lưỡi", ["jivhā", "jivhaṃ"]),
    ("kāya", "thân", ["kāyo", "kāyaṃ"]),
    ("rūpa", "vật chất", ["rūpaṃ"]),             # termbase rūpaṃ «vật chất» (= 2-01); rūpāyatana «lĩnh vực hình sắc»
    ("sadda", "âm thanh", ["saddo", "saddaṃ"]),
    ("gandha", "mùi", ["gandho", "gandhaṃ"]),
    ("rasa", "vị", ["raso", "rasaṃ"]),
    ("phoṭṭhabba", "vật xúc chạm", ["phoṭṭhabbo", "phoṭṭhabbaṃ"]),
    ("mana", "ý", ["mano", "manaṃ"]),
    ("dhamma", "hiện tượng", ["dhammo", "dhammaṃ"]),   # no pi-6 entry for dhammo: pi-1 core term dhamma «hiện tượng»
]
AY_NAME = {   # X-āyatana (termbase / pi-1)
    "cakkhu": "lĩnh vực mắt", "sota": "lĩnh vực tai", "ghāna": "lĩnh vực mũi", "jivhā": "lĩnh vực lưỡi",
    "kāya": "lĩnh vực thân", "rūpa": "lĩnh vực hình sắc", "sadda": "lĩnh vực âm thanh", "gandha": "lĩnh vực mùi",
    "rasa": "lĩnh vực vị", "phoṭṭhabba": "lĩnh vực vật xúc chạm", "mana": "lĩnh vực ý",
    "dhamma": "lĩnh vực đối tượng của ý",
}
AY_STEM = {"cakkhu": "cakkh", "sota": "sot", "ghāna": "ghān", "jivhā": "jivh", "kāya": "kāy", "rūpa": "rūp",
           "sadda": "sadd", "gandha": "gandh", "rasa": "ras", "phoṭṭhabba": "phoṭṭhabb", "mana": "man",
           "dhamma": "dhamm"}   # stem + "āyatanaṃ"

AY_SPECIAL = {   # the «hiểu theo nghĩa …» frame (2-01 / coordinator); figurative senses from the termbase
    "Dibbacakkhu paññācakkhu": "mắt hiểu theo nghĩa thiên nhãn, mắt trí tuệ",
    "Dibbasotaṃ taṇhāsotaṃ": "tai hiểu theo nghĩa thiên nhĩ, dòng chảy của khao khát",
    "Sīlagandho samādhigandho paññāgandho": "mùi hiểu theo nghĩa hương của giới hạnh, hương của định tâm, hương của trí tuệ",
    "Attharaso dhammaraso vimuttiraso": "vị hiểu theo nghĩa vị của ý nghĩa, vị của Giáo Pháp, vị của sự giải thoát",
}


def _table():
    t = {}
    for key, vi, forms in TWELVE:
        t[key] = (vi, vi, forms)
        st = AY_STEM[key]
        t[key + "āyatana"] = (AY_NAME[key], AY_NAME[key], [f"{st}āyatanaṃ"])
    t["āyatana"] = (AY_CLASS, AY_CLASS, ["āyatanaṃ"])
    t["āyatanā"] = (f"các {AY_CLASS}", AY_CLASS, ["āyatanā"])
    return t


AYATANA = B.Members(_table(), special=AY_SPECIAL)

# Dvādasāyatanāni – … (pi-2 «Mười hai lĩnh vực nhận biết –»; this book's order)
UDDESA_PALI = ("Dvādasāyatanāni – cakkhāyatanaṃ, sotāyatanaṃ ghānāyatanaṃ, jivhāyatanaṃ, kāyāyatanaṃ, rūpāyatanaṃ, "
               "saddāyatanaṃ, gandhāyatanaṃ, rasāyatanaṃ, phoṭṭhabbāyatanaṃ, manāyatanaṃ, dhammāyatanaṃ.")
UDDESA_VI = "Mười hai lĩnh vực nhận biết – " + ", ".join(AY_NAME[k] for k, _, _ in TWELVE) + "."
# (the Pāli lacks the comma after sotāyatanaṃ: missing punctuation, rendered as meant)

# ===============================================================================================================
# 2. Persons and planes
# ===============================================================================================================
PLANES_AY = dict(B.PLANES)
PLANES_AY.update({   # termbase: Rūpāvacare «cõi hình sắc», Kāmāvacare «cõi dục lạc», arūpāvacare «cõi không hình sắc»;
    # genitive plural = the beings «chúng sinh trong cõi X» (coordinator; termbase Rūpāvacarānaṃ / Kāmāvacarānaṃ)
    "rūpāvacar": ("cõi hình sắc", "chúng sinh trong cõi hình sắc"),
    "kāmāvacar": ("cõi dục lạc", "chúng sinh trong cõi dục lạc"),
    "arūpāvacar": ("cõi không hình sắc", "chúng sinh trong cõi không hình sắc"),
})
HAVE, HAVE_NOT = "có", "không có"         # termbase Sacakkhukānaṃ «có mắt», acakkhukānaṃ «không có mắt»
_ATTR_OF = {"cakkhuk": "mắt", "sotak": "tai", "ghānak": "mũi", "rūpak": "vật chất", "cittak": "tâm"}
AY_ATTRS = {}
for _st, _vi in _ATTR_OF.items():
    AY_ATTRS[f"sa{_st}ānaṃ"] = f"{HAVE} {_vi}"
    AY_ATTRS[f"a{_st}ānaṃ"] = f"{HAVE_NOT} {_vi}"
ATTR_JOIN = ", "   # a run of attributes in one person group: «những người có mắt, không có tai đang tái sinh»


def ay_group(quant, attrs, part):
    words = []
    if quant == "sabbesaṃ":
        words.append(B.QUANT[quant])
    words.append(B.PERSON)
    if quant == "itaresaṃ":
        words.append(B.QUANT[quant])
    if attrs:
        words.append(ATTR_JOIN.join(AY_ATTRS[a] for a in attrs))
    words.append(B.PARTICIPLES[part][0])
    return " ".join(words)


def ay_persons(head, planes=None):
    """Genitive person phrase → Vietnamese groups. Without an āyatana attribute: 2-01's persons()."""
    toks = head.split()
    if not any(t.lower() in AY_ATTRS for t in toks):
        return B.persons(head, planes or PLANES_AY)
    groups, quant, attrs = [], None, []
    for t in toks:
        tl = t.lower()
        if tl in B.QUANT:
            if quant or attrs:
                raise ValueError(f"misplaced {t!r} in {head!r}")
            quant = tl
        elif tl in AY_ATTRS:
            attrs.append(tl)
        elif tl in B.PARTICIPLES:
            groups.append(ay_group(quant, attrs, tl))
            quant, attrs = None, []
        else:
            raise ValueError(f"unknown word {t!r} in person phrase {head!r}")
    if quant or attrs:
        raise ValueError(f"dangling words in person phrase {head!r}")
    return B.join_and(groups)


def answer_head(head, loc, planes=None):
    planes = planes or PLANES_AY
    if loc == "tattha":
        return B.place_head(head, planes)
    return f"{B.AT} {ay_persons(head, planes)}"


# ===============================================================================================================
# 3. Labels and editorial notes
# ===============================================================================================================
MULAKA_PART = "Phần dựa trên"            # Cakkhāyatanamūlakaṃ «phần dựa trên lĩnh vực mắt» (termbase)


def mulaka_label(member_vi, dot=""):     # (Xāyatanamūlakaṃ)(.)
    return f"({MULAKA_PART} {member_vi}){dot}"


CAKKA = "vòng luân chuyển"               # Cakkaṃ (termbase)
SHOULD = "nên"                           # the gerundive -tabbaṃ (2-02: paripuṇṇaṃ kātabbaṃ «nên được trình bày đầy đủ»,
#                                          vibhajitabbaṃ «nên phân tích», pi-2)
BANDHITABBA = f"{SHOULD} được nối kết"   # bandhitabbaṃ (no entry; English rails "should be linked up")
BANDHANTENA = "khi nối kết"              # bandhantena
ASAMMOHANTENA = "mà không mê lầm"        # asammohantena (coordinator; pi-1 sammoha «sự mê lầm»), right after the verb
EKEKAPADAMULAKA = "dựa trên từng thuật ngữ một"   # Ekekapadamūlakaṃ (pada «thuật ngữ», ekeka «từng … một», mūlaka «dựa trên»)
SABBATTHA_CASES = "ở mọi chỗ"            # sabbattha in an editorial note = every case (coordinator)
SAMKHITTA = "tóm lược"                   # saṃkhittaṃ (abridged; the termbase sense «co rút» is the mind's; sibling vārasaṅkhepo)
YES_WORD = S.YES[:-1]                    # «Đúng vậy» quoted inside a note
_V = {k: B.VERB[k][0] for k in ("uppajjati", "uppajjittha")}
_YATTHA, _TATTHA = C.Q_REL["yattha"]
NOTES_AY = {
    "(Cakkaṃ bandhitabbaṃ)": f"({cap(CAKKA)} {BANDHITABBA})",
    "(Ekekapadamūlakaṃ cakkaṃ bandhitabbaṃ asammohantena).":
        f"({cap(CAKKA)} {EKEKAPADAMULAKA} {BANDHITABBA} {ASAMMOHANTENA}).",
    "(Cakkaṃ bandhantena sabbattha āmantāti kātabbaṃ).":
        f"({cap(BANDHANTENA)} {CAKKA}, {SABBATTHA_CASES} {SHOULD} trả lời là “{YES_WORD}”).",
    "(Yattha ghānāyatanaṃ uppajjati tattha manāyatanaṃ dhammāyatanañca ekasadisaṃ, nānaṃ natthi, upari pana "
    "vārasaṅkhepo ⟦0⟧ tīti jānitabbaṃ.)":
        (f"({cap(C.AT)} {_YATTHA} mà {AY_NAME['ghāna']} {_V['uppajjati']}, {C.THEN} {C.AT} {_TATTHA} "
         f"{B.join_and([AY_NAME['mana'], AY_NAME['dhamma']])} giống hệt nhau, không có khác biệt, "
         f"{C.VA_PANA.lower()} ở phần sau thì có sự tóm lược các mục ⟦0⟧, {SHOULD} hiểu như vậy.)"),
    "(saṃkhittaṃ yassakasadisaṃ ⟦0⟧ )": f"({SAMKHITTA}, giống như phần về người ⟦0⟧)",   # yassakasadisaṃ (termbase)
    "(Saṃkhittaṃ).": f"({cap(SAMKHITTA)}).",
    "(yatthakaṃ paccuppannepi atītepi anāgatepi paccuppannātītepi paccuppannānāgatepi atītānāgatepi sabbattha "
    "sadisaṃ, uppajjati uppajjitthāti nāmaṃ atirekaṃ kātabbaṃ).":
        ("(phần về nơi chốn " + ", ".join(f"{C.AT} {B.TIME[t]}" for t in B.TIME) +
         f", {SABBATTHA_CASES} đều giống nhau, {SHOULD} thêm vào tên gọi “{_V['uppajjati']}”, “{_V['uppajjittha']}”)."),
}

# ===============================================================================================================
# 4. Fragments of the 2-01 frames (for …pe… cuts); derived from the frame functions, so they stay byte-identical
# ===============================================================================================================


def except_frag(m):                      # "X ṭhapetvā…pe…" = «Ngoại trừ X…»
    s = f"{B.EXCEPT} {m}"
    assert B.except_is(m, "X", "Y").startswith(s + ",")
    return s


def naca_tail(y):                        # "…pe… na ca Y." = «… cũng không phải là Y.» (tail of except2_neither)
    full = B.except2_neither("M1", "M2", "X", y)
    return full.split(", ")[-1][:-1]


def na_tail(y):                          # "…pe… na Y" = «… không phải là Y» (tail of rest_not_is)
    full = B.rest_not_is("R", y)
    return full.split(" còn lại ", 1)[1][:-1]


def nq(label, a, b, end="?", neg=False):
    """Naming question, labelled or not. end="" for a question cut by …pe… without «?» («… không…»)."""
    q = B.name_q_neg(label or "Ka", a, b, end) if neg else B.name_q(label or "Ka", a, b, end)
    return q if label else q[len(LABEL["Ka"]) + 1:]


def except2_var(m1, m2, x, y, var=""):  # 2-01 except2_neither, a variant after «những gì còn lại»
    s = B.except2_neither(m1, m2, x, y)
    if var:
        k = f", {B.REST} "
        assert s.count(k) == 1, s
        s = s.replace(k, f", {B.REST} {var} ")
    return s


# ===============================================================================================================
# 5. Units: questions, sentences, fragments
# ===============================================================================================================
LAB = r"\((Ka|Kha|Ga|Gha|Ṅa|Ca|Cha|Ja)\)"
PH = r"(?: (⟦\d+⟧))?"
NQ_RE = re.compile(r"(?:" + LAB + r" )?(na |Na )?(\S+) (na )?(\S+)")
BQ_RE = re.compile(r"(?:" + LAB + r" )?([Yy]assa|[Yy]attha)( vā pana)?( yattha)? (.+?) (tassa tattha|tassa|tattha) (.+)")
BF_RE = re.compile(r"(?:" + LAB + r" )?([Yy]assa|[Yy]attha)( vā pana)?( yattha)? (.+)")
AVA = r"(?:avasesā|avaseso|avasesaṃ)"
LOC = r"(tesaṃ tattha|tesaṃ|tattha)"


def norm_neg(s):
    """nāyatanaṃ / nāyatanā (fused na + āyatana) → 'na āyatana…' so the 2-01 naming frame applies."""
    return re.sub(r"(?<!\w)([Nn])āyatan", r"\1a āyatan", s)


def split_mv(chunk, M):
    """'<member(s)> <verb>' → (Vietnamese member or cut list «A… B… C», verb tuple of 2-01)."""
    w = chunk.split()
    for k in (2, 1):
        if len(w) > k and B.is_verb(" ".join(w[-k:])):
            mem = " ".join(w[:-k])
            if "…" in mem:
                names = [M.subj(x) for x in re.split(r"…(?:pe…)?\s*", mem) if x]
                return "… ".join(names), B.verb(" ".join(w[-k:]))
            return M.subj(mem), B.verb(" ".join(w[-k:]))
    raise ValueError(f"no member + verb in {chunk!r}")


def question_vi(q, M, end="?"):
    """A question without its final «?» (end = «?» or «» for a cut) → Vietnamese, or ValueError."""
    if m := BQ_RE.fullmatch(q):
        label, w1, vapana, w2, c1, then, c2 = m.groups()
        a, v1 = split_mv(c1, M)
        b, v2 = split_mv(c2, M)
        out = B.b_q(label, w1.lower() + (w2 or ""), then, a, v1[0], b, v2[0], other=bool(vapana))
        if end != "?":
            raise ValueError(f"cut pair question {q!r}")
        return out
    q = norm_neg(q)
    if m := NQ_RE.fullmatch(q):
        label, na1, a, na2, b = m.groups()
        if bool(na1) != bool(na2):
            raise ValueError(f"half-negated naming question {q!r}")
        if na1:
            return nq(label, M.pred(a), M.pred(b), end, neg=True)
        return nq(label, M.subj(a), M.pred(b), end)
    raise ValueError(f"unknown question {q!r}")


def tails(t, M):
    """'Na ca Y' / 'Na Y' (single member word) → the frame tails, without the final «.»; else None."""
    if m := re.fullmatch(r"Na ca (\S+)", t):
        return naca_tail(M.pred(m.group(1)))
    if (m := re.fullmatch(r"Na (\S+)", t)) and m.group(1).lower() in AY_FORMS:
        return na_tail(M.pred(m.group(1)))
    return None


def a_sentence(s, M):
    """Family A answers (2-01 frames) incl. the avaseso / avasesaṃ and fused -ñca forms of this yamaka."""
    if m := re.fullmatch(r"(\S+) (\S+?)(ñceva| ceva) (\S+?)(ñca| ca)\.", s):
        b = m.group(2) + ("ñceva" if m.group(3) == "ñceva" else "")
        c = m.group(4) + ("ñca" if m.group(5) == "ñca" else "")
        return B.both_is(M.subj(m.group(1)), M.pred(b), M.pred(c))
    if m := re.fullmatch(r"Avasesā (\S+)" + PH + r" na (\S+)\.", s):
        return B.rest_not_is(M.subj(m.group(1)), M.pred(m.group(3)), f" {m.group(2)}" if m.group(2) else "")
    if m := re.fullmatch(r"(\S+?)(ñca| ca) (\S+?)(ñca| ca) ṭhapetvā " + AVA + PH + r" na ceva (\S+) na ca (\S+)\.", s):
        a1 = m.group(1) + ("ñca" if m.group(2) == "ñca" else "")
        a2 = m.group(3) + ("ñca" if m.group(4) == "ñca" else "")
        return except2_var(M.subj(a1), M.subj(a2), M.pred(m.group(6)), M.pred(m.group(7)), m.group(5) or "")
    if m := re.fullmatch(r"(\S+) ṭhapetvā " + AVA + r" na (\S+), (\S+)\.", s):
        return B.except_not(M.subj(m.group(1)), M.pred(m.group(2)), M.pred(m.group(3)))
    if m := re.fullmatch(r"(\S+) ṭhapetvā avasesā (\S+) na (\S+), (\S+)\.", s):
        return B.except_rest_not(M.subj(m.group(1)), M.subj(m.group(2)), M.pred(m.group(3)), M.pred(m.group(4)))
    if m := re.fullmatch(r"(\S+) ṭhapetvā " + AVA + r" (\S+?)" + PH + r", na (\S+)\.", s):
        return B.except_is(M.subj(m.group(1)), M.pred(m.group(2)), M.pred(m.group(4)),
                           f" {m.group(3)}" if m.group(3) else "")
    if (m := re.fullmatch(r"(.+?) na (\S+), (\S+)\.", s)) and m.group(1).lower() in M.special:
        return B.special_not(M.sp(m.group(1)), M.pred(m.group(2)), M.pred(m.group(3)))
    if (m := re.fullmatch(r"(.+?) (\S+), na (\S+)\.", s)) and m.group(1).lower() in M.special:
        return B.special_is(M.sp(m.group(1)), M.pred(m.group(2)), M.pred(m.group(3)))
    return None


def b_sentence(s, M, planes=None):
    """Family B answers (2-01 b_noca / b_both) with this yamaka's heads."""
    if m := re.fullmatch(r"(.+?) " + LOC + r" (.+?), no ca \2 (.+?)\.", s):
        head, loc, c1, c2 = m.groups()
        a, v1 = split_mv(c1, M)
        b, v2 = split_mv(c2, M)
        return B.b_noca(answer_head(head, loc, planes), loc, a, v1, b, v2)
    if m := re.fullmatch(r"(.+?) " + LOC + r" (\S+?ñca) (\S+) (\S+?ñca) (\S+)\.", s):
        head, loc, c1, v1, c2, v2 = m.groups()
        return B.b_both(answer_head(head, loc, planes), loc, M.subj(c1), B.verb(v1), M.subj(c2), B.verb(v2))
    return None


def sentence_vi(s, M, planes=None):
    if s in B.SHORT:
        return B.SHORT[s]
    if s in B.CLOSING:
        return B.CLOSING[s]
    if (t := tails(s[:-1], M)) is not None:
        return t + "."
    for f in (a_sentence, b_sentence):
        out = f(s, M) if f is a_sentence else f(s, M, planes)
        if out is not None:
            return out
    # a sentence with a trailing editorial note: '… uppajjati (saṃkhittaṃ …).'
    if m := re.fullmatch(r"(.+) (\([^()]+\))\.", s):
        if m.group(2) in NOTES_AY:
            return sentence_vi(m.group(1) + ".", M, planes)[:-1] + " " + NOTES_AY[m.group(2)] + "."
    raise ValueError(f"unknown sentence {s!r}")


def fragment_vi(u, M, planes=None):
    """A unit with no final «.» / «?» (cut by …pe… / …)."""
    if (t := tails(u, M)) is not None:
        return t
    if m := re.fullmatch(r"(\S+) ṭhapetvā", u):
        return except_frag(M.subj(m.group(1)))
    if u.lower() in AY_FORMS:
        return M.subj(u)
    if (m := BF_RE.fullmatch(u)) and not BQ_RE.fullmatch(u):   # pair question cut after its first clause
        label, w1, vapana, w2, c1 = m.groups()
        who = w1.lower() + (w2 or "")
        a, v1 = split_mv(c1, M)
        full = B.b_q(label, who, C.Q_COR[who], a, v1[0], "B", "V", other=bool(vapana))
        return full.split(f", {C.THEN} ", 1)[0]
    try:
        return question_vi(u, M, end="")
    except ValueError:
        pass
    return sentence_vi(u + ".", M, planes)[:-1]


def unit_vi(u, M, planes=None):
    """One unit (a question, a sentence or a fragment). The Pāli case of the first letter is kept."""
    lower = u[:1].islower()
    p = cap(u) if lower else u
    m = re.fullmatch(r"\((\w+?)āyatanamūlakaṃ\)(\.?)", p)
    if p in NOTES_AY:
        out = NOTES_AY[p]
    elif m:
        out = mulaka_label(M.subj(m.group(1).lower() + "āyatanaṃ"), m.group(2))
    elif p in B.SHORT or p in B.CLOSING:
        out = sentence_vi(p, M, planes)
    elif p.endswith("?"):
        out = question_vi(p[:-1], M)
    elif p.endswith(".") or p.endswith(")"):
        out = sentence_vi(p, M, planes)
    else:
        out = fragment_vi(p, M, planes)
    if lower and not out.startswith("("):
        out = out[:1].lower() + out[1:]
    return out


# ===============================================================================================================
# 6. Lines: pieces between cuts → units
# ===============================================================================================================
CUT_RE = re.compile(r"( ?)…(?:[Pp]e…)?(\.?)")
SLIPS = {   # plain slips, rendered as meant (reported)
    "sotāyananti": "sotāyatananti",                                   # ^6-3-13
    "uppajjittharūpāyatanañca": "uppajjittha rūpāyatanañca",          # ^6-3-43 (two words run together)
}


def units_vi(piece, M, planes=None):
    units = [x for x in re.split(r"(?<=[.?]) (?=\S)", piece.strip()) if x]
    return " ".join(unit_vi(x, M, planes) for x in units)


def list_question(body, M):
    """Yassa A…pe… B… C V tassa D Vti? <answers> (member lists cut by …pe… / … inside the pair question)."""
    m = re.fullmatch(r"(.+?\?)((?: .*)?)", body)
    if not m:
        return None
    q, rest = m.group(1)[:-1], m.group(2)
    mm = BQ_RE.fullmatch(q)
    if not mm or "…" not in q:
        return None
    out = question_vi(q, M)
    if rest.strip():
        out += " " + units_vi(rest, M)
    return out


def line_vi(body, M, planes=None):
    if (lq := list_question(body, M)) is not None:
        return lq
    out, pos = "", 0
    for m in CUT_RE.finditer(body):
        piece = body[pos:m.start()]
        if piece.strip():
            if out:
                out += " " if piece.startswith(" ") else ""
            out += units_vi(piece, M, planes)
        if out.endswith("."):
            out = out[:-1]                                  # «.» before a cut is absorbed (never «.…»)
        out += (" " if m.group(1) else "") + "…"            # the cut's final «.» (m.group(2)) is absorbed
        pos = m.end()
    piece = body[pos:]
    if piece.strip():
        if out:
            out += " " if piece.startswith(" ") else ""
        out += units_vi(piece, M, planes)
    return out


def var_vi(br, kind):
    """One variant bracket: single (2-01 parse_variant) or double '[X (a.), Y (b.)]' = «[dị bản (A.): X; (B.): Y]» (pi-2)."""
    parts = re.findall(r"(.+?) \(([^()]+)\)(?:, |$)", br[1:-1])
    if len(parts) <= 1:
        return B.parse_variant(br, kind)
    if kind != "form":
        raise ValueError(f"double variant {br!r} kind {kind!r}")
    sig = [", ".join(cap(x.strip()) + "." for x in s.split(".") if x.strip()) for _, s in parts]
    return "[dị bản " + "; ".join(f"({g}): {w}" for (w, _), g in zip(parts, sig)) + "]"


def heading(text, yamaka=YAMAKA):
    """2-01 heading(); Suddhāyatana… (sandhi Suddha + āyatana, which 2-01's 'Suddha<X>' pattern does not see) goes
    to 2-01's suddha_varo / suddha_mulacakka_varo."""
    if text == "Suddhāyatanavāro":
        return B.suddha_varo(AY_CLASS)
    if text == "Suddhāyatanamūlacakkavāro":
        return B.suddha_mulacakka_varo(AY_CLASS)
    return B.heading(text, AY_CLASS, yamaka)


def tr_line(p, M=None, fixed=None, variant_kind=None, planes=None, yamaka=YAMAKA):
    M = M or AYATANA
    m = re.search(r" (\^\S+)$", p)
    bid = m.group(1) if m else None
    body = p[:m.start()] if m else p
    fixed = fixed or {}
    if body.startswith("#"):
        hashes, text = body.split(" ", 1)
        out = f"{hashes} {heading(text, yamaka)}"
    elif body in fixed:
        out = fixed[body]
    else:
        for bad, good in SLIPS.items():
            if bad in body:
                SLIPS_SEEN.append((bid, bad, good))
                body = body.replace(bad, good)
        brs = re.findall(r"\[[^\]]*\]", body)
        for k, br in enumerate(brs):
            body = body.replace(br, f"⟦{k}⟧", 1)
        out = line_vi(body, M, planes)
        for k, br in enumerate(brs):
            if br not in (variant_kind or {}):
                raise ValueError(f"undeclared variant {br!r}")
            if f"⟦{k}⟧" not in out:
                raise ValueError(f"variant {br!r} lost in {p!r}")
            out = out.replace(f"⟦{k}⟧", var_vi(br, variant_kind[br]))
    if "⟦" in out:
        raise ValueError(f"unplaced variant in {p!r}")
    return f"{out} {bid}" if bid else out


def build(name, M=None, fixed=None, variant_kind=None, planes=None, yamaka=YAMAKA):
    return [[tr_line(ln, M, fixed, variant_kind, planes, yamaka) for ln in seg] for seg in S.segments_of(name)]


AY_FORMS = set(AYATANA.form)              # every written member form (for single-word fragments)

# ===============================================================================================================
# 7. This chapter
# ===============================================================================================================
FIXED_3_01 = {UDDESA_PALI: UDDESA_VI}
VARIANTS_3_01 = {
    "[avasesā (syā. pī.)]": "form",
    "[avaseso (syā.)]": "form",
    "[avasesā (syā.)]": "form",
    "[uparivāre saṅkhepo (syā.), uparivāre saṅkhepaṃ (sī. ka.)]": "form",
    "[yassakampi sadisaṃ (sī.), yassekasadisaṃ (syā.)]": "form",
}

REUSED = [   # (Pāli, Vietnamese, book): asserted to occur in that book's Vietnamese rails
    ("Dvādasāyatanāni –", "Mười hai lĩnh vực nhận biết –", "2"),
    *[(f"{AY_STEM[k]}āyatanaṃ", AY_NAME[k], "1") for k in AY_NAME],
    ("lĩnh vực nhận biết (āyatana)", AY_CLASS, "1"),
    ("dibbacakkhu", "thiên nhãn", "5"), ("paññācakkhu", "mắt trí tuệ", "5"), ("dibbasotaṃ", "thiên nhĩ", "5"),
    ("sacittakassa / acittakassa", "người có tâm", "5"), ("acittakassa", "người không có tâm", "5"),
    ("sammoho", "sự mê lầm", "1"),
    ("[X (syā.), Y (ka.)] double variant", "[dị bản (Syā.): upariṭṭhime; (Ka.): upariṭṭhimaṃ]", "2"),
]


def check_reused():
    texts = {b: unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md"))))
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED if unicodedata.normalize("NFC", v).lower() not in texts[b].lower()]
    assert not bad, "reused strings not found in their rails: " + repr(bad)


def check_frames():
    """Shared strings must be the setter's: B's own persons() for attribute-free heads, the fragments as substrings."""
    assert ay_persons("Sabbesaṃ cavantānaṃ") == B.persons("Sabbesaṃ cavantānaṃ")
    assert ay_group("sabbesaṃ", [], "cavantānaṃ") == B.persons("Sabbesaṃ cavantānaṃ")
    assert naca_tail("Y") + "." in B.except2_neither("A", "B", "X", "Y")
    assert na_tail("Y") + "." in B.rest_not_is("R", "Y")
    assert nq(None, "a", "b") == B.name_q("Ka", "a", "b")[4:]
    assert B.Members.__name__ == "Members"


# ===============================================================================================================
# 8. Notes file (Pāli = tiếng Việt)
# ===============================================================================================================
def notes():
    M = AYATANA
    out = []

    def row(p, v):
        out.append(f"{p} = {v}")

    def h(t):
        out.extend(["", f"## {t}", ""])

    out += [f"# pi-6 rails {N} (Āyatanayamaka 1): the Āyatana module on top of families A / B (rails 2-01)", "",
            "Builder: build_rails_3-01_vi.py (import with importlib). Every frame string is produced by "
            "build_rails_2-01_vi functions (name_q, name_q_neg, both_is, rest_not_is, special_is / special_not, "
            "except_*, b_q, b_noca, b_both, persons, place_head, heading, SHORT, CLOSING); this file only plugs in "
            "the members and adds the pieces listed here. Exposed for 3-02 … 3-06: `AYATANA`, `TWELVE`, `AY_NAME`, "
            "`AY_SPECIAL`, `AY_ATTRS`, `ATTR_JOIN`, `PLANES_AY`, `ay_persons`, `answer_head`, `mulaka_label`, "
            "`NOTES_AY`, `except_frag`, `naca_tail`, `na_tail`, `nq`, `except2_var`, `question_vi`, `sentence_vi`, "
            "`unit_vi`, `line_vi`, `var_vi`, `tr_line`, `build`. Format: Pāli = tiếng Việt.", ""]
    h("Members (termbase; pi-1 names)")
    for k, vi, forms in TWELVE:
        row(f"{' / '.join(forms)} ; {AY_STEM[k]}āyatanaṃ", f"{vi} ; {AY_NAME[k]}")
    row("āyatanaṃ / āyatanā", f"{AY_CLASS} / các {AY_CLASS} (predicate: {AY_CLASS})")
    row("nāyatanaṃ / nāyatanā (fused na)", f"= na āyatana…: «{nq('Ka', 'mắt', AY_CLASS, neg=True)}»")
    row("Dvādasāyatanāni – … (uddesa, ^6-3-1)", UDDESA_VI)
    h("Headings")
    for t in ("Āyatanayamakaṃ", "Suddhāyatanavāro", "Suddhāyatanamūlacakkavāro"):
        row(t, heading(t))
    h("Family A in this yamaka (2-01 frames)")
    for s in ("(Ka) cakkhu cakkhāyatanaṃ?", "(Kha) āyatanā sotāyatanaṃ?", "(Ka) na cakkhu nāyatanaṃ?",
              "(Kha) nāyatanā na cakkhu?", "Cakkhu cakkhāyatananti?", "Na sotaṃ na sotāyatananti?"):
        row(s, unit_vi(s, M))
    for s in ("Dibbacakkhu paññācakkhu cakkhu, na cakkhāyatanaṃ.", "Dibbasotaṃ taṇhāsotaṃ sotaṃ, na sotāyatanaṃ.",
              "Sīlagandho samādhigandho paññāgandho gandho, na gandhāyatanaṃ.",
              "Attharaso dhammaraso vimuttiraso raso, na rasāyatanaṃ.",
              "Dibbacakkhu paññācakkhu na cakkhāyatanaṃ, cakkhu.",
              "Cakkhāyatanaṃ cakkhu ceva cakkhāyatanañca.", "Sotāyatanaṃ sotañceva sotāyatanañca.",
              "Sotāyatanaṃ āyatanañceva sotāyatanañca.", "Avasesā āyatanā na sotāyatanaṃ.",
              "Kāyāyatanaṃ ṭhapetvā avaseso kāyo, na kāyāyatanaṃ.", "Rūpāyatanaṃ ṭhapetvā avasesaṃ rūpaṃ, na rūpāyatanaṃ.",
              "Kāyāyatanaṃ ṭhapetvā avaseso na kāyāyatanaṃ, kāyo.",
              "Rūpañca rūpāyatanañca ṭhapetvā avasesaṃ na ceva rūpaṃ na ca rūpāyatanaṃ.",
              "Cakkhuṃ ṭhapetvā avasesā āyatanā na cakkhu, āyatanā.",
              "Cakkhuñca āyatanañca ṭhapetvā avasesā na ceva cakkhu na ca āyatanā."):
        row(s, sentence_vi(s, M))
    row("avaseso / avasesaṃ (= avasesā)", f"{B.REST}")
    row("Cakkhuñca cakkhāyatanañca ṭhapetvā avasesaṃ [v] na ceva …", except2_var("mắt", "lĩnh vực mắt", "mắt",
        "lĩnh vực mắt", "[v]"))
    h("Cuts (…pe… / …) inside a line")
    row("<question>?…pe… / <question>? …pe…", "<câu hỏi> không?… / <câu hỏi> không? …")
    row("<sentence>…pe…. / Āmantā.…Pe…. / Natthi.…Pe….", f"<câu>… / {S.YES[:-1]}… / {B.SHORT['Natthi.'][:-1]}…  "
        "(the «.» on both sides of the cut is absorbed: never «.…» / «….»)")
    row("<naming question>ti…pe… / <naming question>…pe… (no «?»)", f"«{nq(None, 'X', 'Y', end='')}…» "
        f"/ «{nq(None, 'X', 'Y', end='', neg=True)}…» (2-01 frame, end «»)")
    row("Āyatanā ghānāyatananti…pe… āyatanā dhammāyatananti?", line_vi("Āyatanā ghānāyatananti…pe… āyatanā dhammāyatananti?", M))
    row("X ṭhapetvā…pe…", f"{except_frag('X')}…")
    row("…pe… na ca Y.", f"… {naca_tail('Y')}.")
    row("…pe… na Y(.)", f"… {na_tail('Y')}(.)")
    row("ghānaṃ… jivhā… (member list)", f"{M.subj('ghānaṃ')}… {M.subj('jivhā')}…  (lower case as the Pāli)")
    row("Yassa A V tassa B…pe… C… D Vti?", line_vi("Yassa cakkhāyatanaṃ uppajjittha tassa ghānāyatanaṃ…pe… "
                                                    "rūpāyatanaṃ… manāyatanaṃ… dhammāyatanaṃ uppajjitthāti? Āmantā.", M))
    row("(Ka) yattha A V…pe… (pair question cut after its first clause)",
        line_vi("(Ka) yattha cakkhāyatanaṃ uppajjittha…pe…", M))
    row("Yattha A nuppajjittha…pe….", line_vi("Yattha cakkhāyatanaṃ nuppajjittha…pe….", M))
    row("a unit after a cut keeps the Pāli case", "«… các lĩnh vực nhận biết còn lại không phải là …»")
    h("Labels and editorial notes")
    for k in ("cakkhu", "ghāna", "rūpa", "mana"):
        row(f"({cap(AY_STEM[k])}āyatanamūlakaṃ)", mulaka_label(AY_NAME[k]))
    for p, v in NOTES_AY.items():
        row(p.replace("⟦0⟧", "[v]"), v.replace("⟦0⟧", "[v]"))
    row("[X (syā.), Y (sī. ka.)] (double variant)", var_vi("[X (syā.), Y (sī. ka.)]", "form") + " (pi-2 format)")
    h("Family B in this yamaka: person attributes and planes")
    for k, v in AY_ATTRS.items():
        row(k, f"{B.PERSON} {v} …")
    row("<attr> <attr> <participle> (one group)", f"{B.PERSON} <attr>{ATTR_JOIN}<attr> <participle>  (ATTR_JOIN «{ATTR_JOIN}»)")
    for hd in ("Sacakkhukānaṃ asotakānaṃ upapajjantānaṃ", "Sacakkhukānaṃ sasotakānaṃ upapajjantānaṃ",
               "Sacakkhukānaṃ upapajjantānaṃ", "Acittakānaṃ upapajjantānaṃ",
               "Sabbesaṃ cavantānaṃ acakkhukānaṃ asotakānaṃ upapajjantānaṃ",
               "Sabbesaṃ cavantānaṃ arūpakānaṃ upapajjantānaṃ", "Sabbesaṃ cavantānaṃ"):
        row(hd, ay_persons(hd))
    for k in ("rūpāvacar", "kāmāvacar", "arūpāvacar"):
        pv, bv = PLANES_AY[k]
        row(f"{k}e / {k}ānaṃ", f"{pv} / {bv}")
    for hd in ("Rūpāvacarānaṃ arūpāvacarānaṃ", "Suddhāvāsānaṃ asaññasattānaṃ arūpānaṃ", "Asaññasattānaṃ arūpānaṃ",
               "Pañcavokārānaṃ asaññasattānaṃ"):
        row(hd, ay_persons(hd))
    row("Rūpāvacare arūpāvacare tattha …", f"{B.place_head('Rūpāvacare arūpāvacare', PLANES_AY)}, {C.THEN} "
        f"{B.L['tattha']} …")
    for s in ("Sacakkhukānaṃ asotakānaṃ upapajjantānaṃ tesaṃ cakkhāyatanaṃ uppajjati, no ca tesaṃ sotāyatanaṃ uppajjati.",
              "Acakkhukānaṃ sasotakānaṃ upapajjantānaṃ tesaṃ cakkhāyatanaṃ nuppajjati, no ca tesaṃ sotāyatanaṃ nuppajjati.",
              "Sabbesaṃ cavantānaṃ tesaṃ cakkhāyatanañca nuppajjati dhammāyatanañca nuppajjati.",
              "Rūpāvacare tattha ghānāyatanaṃ nuppajjati, no ca tattha cakkhāyatanaṃ nuppajjati.",
              "Rūpāvacarānaṃ tesaṃ tattha cakkhāyatanaṃ uppajjittha, no ca tesaṃ tattha ghānāyatanaṃ uppajjittha."):
        row(s, sentence_vi(s, M))
    h("Termbase misfits and gaps (for the coordinator)")
    out += [
        "- dhammo / dhammaṃ (member word): no pi-6 entry; pi-1 core term dhamma «hiện tượng».",
        "- sarūpakānaṃ, saghānakānaṃ, aghānakānaṃ: no entry; built as their termbase siblings (arūpakānaṃ «không có "
        "vật chất», Sacakkhukānaṃ «có mắt», acakkhukānaṃ «không có mắt»): «có vật chất», «có mũi», «không có mũi».",
        "- Attribute runs (Sacakkhukānaṃ asotakānaṃ upapajjantānaṃ): one person group (as the coordinator's "
        f"Pacchimabhavikānaṃ <A> <B> rule), attributes joined by «{ATTR_JOIN}»: «những người có mắt, không có tai đang "
        "tái sinh». New shape: please align.",
        "- saṃkhittaṃ / Saṃkhittaṃ (abridged): the termbase sense «co rút» is the mind's (8); closest sibling "
        "vārasaṅkhepo «sự tóm lược các mục»: «tóm lược».",
        "- Cakkaṃ bandhitabbaṃ / bandhantena, Ekekapadamūlakaṃ, ekasadisaṃ, nānaṃ natthi, jānitabbaṃ, atirekaṃ "
        "kātabbaṃ: no entries; wording above (Cakkaṃ «vòng luân chuyển», pada «thuật ngữ», mūlaka «dựa trên», "
        "Natthi «không có», yatthakaṃ «phần về nơi chốn», yassakasadisaṃ «giống như phần về người»).",
        "- arūpāvacarānaṃ: termbase «cõi không hình sắc»; as the second plane of a beings run (Rūpāvacarānaṃ "
        "arūpāvacarānaṃ) 2-01's run gives «chúng sinh trong cõi hình sắc và cõi không hình sắc», which matches.",
        "",
        "## Slips (rendered as meant or kept; reported)",
        "",
        "- ^6-3-1 no comma after «sotāyatanaṃ»: comma supplied.",
        "- ^6-3-13 «sotāyananti» for sotāyatananti (termbase lists it as a misspelling): «lĩnh vực tai».",
        "- ^6-3-23 note «… vārasaṅkhepo [..] tīti jānitabbaṃ»: «tīti» read as «(hotī)ti»: «… thì có sự tóm lược các mục …, "
        "nên hiểu như vậy».",
        "- The gerundive -tabbaṃ (bandhitabbaṃ, kātabbaṃ, jānitabbaṃ) = «nên …», as 2-02 (paripuṇṇaṃ kātabbaṃ «nên được "
        "trình bày đầy đủ») and pi-2 (vibhajitabbaṃ «nên phân tích»).",
        "- ^6-3-26 «[…] )»: the stray space before «)» is dropped.",
        "- ^6-3-43 «uppajjittharūpāyatanañca» (two words run together): «đã sinh khởi, lĩnh vực hình sắc …».",
        "- ^6-3-50 the second question is labelled «(Ka)» (for «(Kha)»): label kept «(a)» (as 2-01 ^6-2-61).",
        "- «Āmantā.…Pe….», «Natthi.…Pe….», «…pe….»: the periods on both sides of the cut are absorbed.",
        "",
    ]
    return "\n".join(out)


def main():
    S.check_reused()
    B.check_reused()
    check_reused()
    check_frames()
    segs = build(CH, fixed=FIXED_3_01, variant_kind=VARIANTS_3_01)
    S.write(CH, segs)
    text = (S.OUT_DIR / CH).read_text(encoding="utf-8")
    ADH_DIR.mkdir(parents=True, exist_ok=True)
    (ADH_DIR / CH).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", ADH_DIR / CH)
    NOTES_MD.write_text(unicodedata.normalize("NFC", notes()), encoding="utf-8", newline="\n")
    print("wrote", NOTES_MD)
    for s in SLIPS_SEEN:
        print("slip:", s)


if __name__ == "__main__":
    main()
