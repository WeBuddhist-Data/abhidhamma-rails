"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 4 (Dhātuyamaka, the pairs on the eighteen elements).

Family setter: rails 2-01 (families A and B), imported READ-ONLY; the eighteen dhātu members (termbase, pi-1 / pi-2)
are plugged into its frames (B.name_q, B.name_q_neg, B.a_sentence, B.b_question, B.b_noca, B.b_both, B.heading …).
Family E (the one pariññā line) from rails 2-02 (E.e_question); the shared answer shapes from rails 7-01 (C).

New here (exposed for later chapters, e.g. Indriya / Āyatana with the same shapes):
  DHATU / PLAIN / DHATU_M     the members (Members table of 2-01's class)
  sense()                     the «<member> hiểu theo nghĩa <a>, <b>, …» frame of the special subjects (= 2-01)
  ATTR4 / head4()             answer heads "Sacakkhukānaṃ asotakānaṃ upapajjantānaṃ" (one group: attributes + participle)
  chain() / piece()           lines cut by …pe… / …: each piece a question, a sentence run or a fragment
  fragment()                  cut pieces: "Dhātū ghānadhātu", "Na jivhā", "Sotaṃ ṭhapetvā", "saddaṃ" …
  bare_q()                    bare cut questions "Ghānaviññāṇaṃ?" «… không?» / "Na ghānaṃ?" «…, có phải không?»
  NOTE_*                      the editorial notes (cakkaṃ bandhitabbaṃ, yathā āyatanayamake …)
A line, piece or word the parsers cannot place raises ValueError: there is no silent fallback.

usage: python -I -X utf8 -B build_rails_4_vi.py
"""
import importlib
import re
import sys
import unicodedata

RAILS_DIR = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\rails"
if RAILS_DIR not in sys.path:
    sys.path.insert(0, RAILS_DIR)
import build_rails_sample_vi as S  # noqa: E402  (read-only)
B = importlib.import_module("build_rails_2-01_vi")   # family A / B setter (read-only)
C = importlib.import_module("build_rails_7-01_vi")   # shared answer shapes (read-only)
E = importlib.import_module("build_rails_2-02_vi")   # family E setter (read-only)
A3 = importlib.import_module("build_rails_3-01_vi")  # Āyatana 1 (read-only): shared attribute beings, notes, cuts

LABEL = S.LABEL
cap = S.cap
CH = "4-dhatuyamaka.md"
N = "4"
NOTES_MD = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/notes-rails-{N}.md"
ADH_DIR = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/adh-{N}"
TERMBASE = S.ROOT / "AI_translation/vietnamese/pi-6-pali-vietnamese-termbase-plain.md"
YAMAKA = "Dhātu"
X_PL = "yếu tố"                          # Suddhadhātuvāro «Mục về các yếu tố thuần túy» (termbase)


# ===============================================================================================================
# 1. Members (termbase headwords; pi-2 ^2-183 for the eighteen dhātus)
# ===============================================================================================================
DHATU = [   # (Pāli stem of the -dhātu compound, Vietnamese), in the order of the uddesa ^6-4-1
    ("cakkhu", "yếu tố mắt"), ("sota", "yếu tố tai"), ("ghāna", "yếu tố mũi"), ("jivhā", "yếu tố lưỡi"),
    ("kāya", "yếu tố thân"), ("rūpa", "yếu tố hình sắc"), ("sadda", "yếu tố âm thanh"), ("gandha", "yếu tố mùi"),
    ("rasa", "yếu tố vị"), ("phoṭṭhabba", "yếu tố vật xúc chạm"),
    ("cakkhuviññāṇa", "yếu tố thức qua mắt"), ("sotaviññāṇa", "yếu tố thức qua tai"),
    ("ghānaviññāṇa", "yếu tố thức qua mũi"), ("jivhāviññāṇa", "yếu tố thức qua lưỡi"),
    ("kāyaviññāṇa", "yếu tố thức qua thân"), ("mano", "yếu tố ý"), ("manoviññāṇa", "yếu tố ý thức"),
    ("dhamma", "yếu tố đối tượng của ý"),
]
PLAIN = [   # the plain words of the padasodhana / suddha questions: (key, Vietnamese, Pāli forms)
    ("cakkhu", "mắt", ["cakkhu", "cakkhuṃ"]),
    ("sota", "tai", ["sotaṃ"]),
    ("ghāna", "mũi", ["ghānaṃ"]),
    ("jivhā", "lưỡi", ["jivhā", "jivhaṃ", "jivha"]),          # jivha: short spelling (termbase), ^6-4-15
    ("kāya", "thân", ["kāyo", "kāyaṃ"]),
    ("rūpa", "vật chất", ["rūpaṃ"]),                            # termbase rūpaṃ «vật chất» (= 2-01)
    ("sadda", "âm thanh", ["saddo", "saddaṃ"]),
    ("gandha", "mùi", ["gandho", "gandhaṃ"]),
    ("rasa", "vị", ["raso", "rasaṃ"]),
    ("phoṭṭhabba", "vật xúc chạm", ["phoṭṭhabbo", "phoṭṭhabbaṃ"]),
    ("cakkhuviññāṇa", "thức qua mắt", ["cakkhuviññāṇaṃ"]),
    ("sotaviññāṇa", "thức qua tai", ["sotaviññāṇaṃ"]),
    ("ghānaviññāṇa", "thức qua mũi", ["ghānaviññāṇaṃ"]),
    ("jivhāviññāṇa", "thức qua lưỡi", ["jivhāviññāṇaṃ"]),
    ("kāyaviññāṇa", "thức qua thân", ["kāyaviññāṇaṃ"]),
    ("mano", "ý", ["mano", "manaṃ"]),
    ("manoviññāṇa", "ý thức", ["manoviññāṇaṃ"]),
    ("dhamma", "hiện tượng", ["dhammo", "dhammaṃ"]),            # no termbase headword: core term dhamma «hiện tượng»
]
DHATU_SUBJ, DHATU_PRED = "các yếu tố", "yếu tố"                # dhātū / dhātu / dhātuñca (termbase «yếu tố»)

SENSE = "hiểu theo nghĩa"                # the approved frame (2-01 Piyarūpaṃ sātarūpaṃ, termbase Diṭṭhisaññā)


def sense(member, terms):
    """«<member> hiểu theo nghĩa <a>, <b>, …» (2-01: «vật chất hiểu theo nghĩa điều đáng yêu, điều khoan khoái»)."""
    return f"{member} {SENSE} {', '.join(terms)}"


SPECIAL = {   # Pāli (as written) -> (member Vietnamese, the termbase terms of the figurative senses)
    "Dibbacakkhu paññācakkhu": ("mắt", ["thiên nhãn", "mắt trí tuệ"]),
    "Dibbasotaṃ taṇhāsotaṃ": ("tai", ["thiên nhĩ", "dòng chảy của khao khát"]),
    "Sīlagandho samādhigandho paññāgandho": ("mùi", ["hương của giới hạnh", "hương của định tâm", "hương của trí tuệ"]),
    "Attharaso dhammaraso vimuttiraso": ("vị", ["vị của ý nghĩa", "vị của Giáo Pháp", "vị của sự giải thoát"]),
}

_table = {k: (vi, vi, forms) for k, vi, forms in PLAIN}
for _stem, _vi in DHATU:
    _table[_stem + "dhātu"] = (_vi, _vi, [_stem + "dhātu", _stem + "dhātuṃ"])
_table["dhātu"] = (DHATU_SUBJ, DHATU_PRED, ["dhātu", "dhātū", "dhātuṃ"])
DHATU_M = B.Members(_table, special={k: sense(m, t) for k, (m, t) in SPECIAL.items()})
M = DHATU_M

# termbase headwords this chapter takes its Vietnamese from (asserted against the locked termbase)
TB_USED = [(f"{s}dhātu", v) for s, v in DHATU] + [
    ("cakkhu", "mắt"), ("sotaṃ", "tai"), ("ghānaṃ", "mũi"), ("jivhā", "lưỡi"), ("jivha", "lưỡi"), ("kāyo", "thân"),
    ("rūpaṃ", "vật chất"), ("saddo", "âm thanh"), ("gandho", "mùi"), ("raso", "vị"), ("phoṭṭhabbo", "vật xúc chạm"),
    ("cakkhuviññāṇaṃ", "thức qua mắt"), ("sotaviññāṇaṃ", "thức qua tai"), ("Ghānaviññāṇaṃ", "thức qua mũi"),
    ("jivhāviññāṇaṃ", "thức qua lưỡi"), ("Kāyaviññāṇaṃ", "thức qua thân"), ("mano", "ý"),
    ("manoviññāṇaṃ", "ý thức"), ("dhātu", "yếu tố"), ("dhātū", "yếu tố"), ("dhātuyo", "yếu tố"),
    ("Dibbacakkhu", "thiên nhãn"), ("paññācakkhu", "mắt trí tuệ"), ("Dibbasotaṃ", "thiên nhĩ"),
    ("taṇhāsotaṃ", "dòng chảy của khao khát"), ("Sīlagandho", "hương của giới hạnh"),
    ("samādhigandho", "hương của định tâm"), ("paññāgandho", "hương của trí tuệ"), ("Attharaso", "vị của ý nghĩa"),
    ("dhammaraso", "vị của Giáo Pháp"), ("vimuttiraso", "vị của sự giải thoát"),
    ("Sacakkhukānaṃ", "có mắt"), ("acakkhukānaṃ", "không có mắt"), ("sasotakānaṃ", "có tai"),
    ("asotakānaṃ", "không có tai"), ("Sacittakānaṃ", "có tâm"), ("upapajjantānaṃ", "đang tái sinh"),
    ("Cakkaṃ", "vòng luân chuyển"), ("paṇṇatti", "sự định danh"), ("ghānasadiso", "giống như mũi"),
    ("ghānadhātusadisā", "giống như yếu tố mũi"), ("Jivhāpi", "lưỡi"), ("ṭhapetvā", "ngoại trừ"),
    ("avaseso", "còn lại"), ("avasesaṃ", "còn lại"), ("Avasesā", "còn lại"),
    ("Dhātuyamakaṃ", "Các cặp câu hỏi về các yếu tố"), ("Suddhadhātuvāro", "mục về các yếu tố thuần túy"),
    ("Suddhadhātumūlacakkavāro", "mục về vòng luân chuyển dựa trên các yếu tố thuần túy"),
    ("āyatanayamake", "các cặp câu hỏi về các lĩnh vực nhận biết"),
    ("āyatanayamakassa", "các cặp câu hỏi về các lĩnh vực nhận biết"),
    ("dhātuyamakepi", "các cặp câu hỏi về các yếu tố"), ("dhātuyamakassa", "các cặp câu hỏi về các yếu tố"),
    ("dhātuyamakampi", "các cặp câu hỏi về các yếu tố"), ("Pariññāvāro", "mục về sự hiểu biết trọn vẹn"),
    ("parijānāti", "hiểu biết trọn vẹn"), ("cakkhudhātuṃ", "yếu tố mắt"), ("sotadhātuṃ", "yếu tố tai"),
]


def check_termbase():
    entries = {}
    for ln in TERMBASE.read_text(encoding="utf-8").splitlines():
        if m := re.match(r"(.+?): \{(.*)\}$", ln):
            entries[m.group(1)] = m.group(2)
    bad = []
    for p, v in TB_USED:
        e = entries.get(p)
        if e is None or not re.search(r": " + re.escape(v) + r"(?:[;}]|$)", e):
            bad.append((p, v, e))
    assert not bad, "termbase mismatch: " + repr(bad)


# ===============================================================================================================
# 2. Headings, uddesa, closing lines
# ===============================================================================================================
LATER = dict(S.LATER_HEADINGS)
PARINNAVARO = LATER["Pariññāvāro"]       # Mục về sự hiểu biết trọn vẹn (approved; = 2-02)


def heading(text):
    if text == "Pariññāvāro":
        return PARINNAVARO
    return B.heading(text, X_PL, YAMAKA)


EIGHTEEN = "Mười tám yếu tố"             # Aṭṭhārasa dhātuyo (pi-2 ^2-183)


def uddesa(body):
    m = re.fullmatch(r"Aṭṭhārasa dhātuyo – (.+)\.", body)
    if not m:
        raise ValueError(f"not the uddesa: {body!r}")
    items = m.group(1).split(", ")
    if items != [s + "dhātu" for s, _ in DHATU]:
        raise ValueError(f"uddesa members differ from DHATU: {items!r}")
    return f"{EIGHTEEN} – {', '.join(M.subj(x) for x in items)}."


# ===============================================================================================================
# 3. Editorial notes (cross-references to the Āyatanayamaka; titles in “…” as rails 8)
# ===============================================================================================================
T_AYATANA = f"“{S.yamaka_title('Āyatana')}”"     # āyatanayamake / -assa / -aṃ
T_DHATU = f"“{S.yamaka_title('Dhātu')}”"         # dhātuyamakepi / -assa / -ampi / -aṃ
CYCLE = A3.CAKKA                         # Cakkaṃ «vòng luân chuyển» (termbase; = 3-01)
DESIG = "sự định danh"                   # paṇṇatti (termbase)
LINKED = A3.BANDHITABBA                  # bandhitabbaṃ «nên được nối kết» (= 3-01)
LINKED_PAST = "đã được nối kết"          # bandhitaṃ (3-01's word, past)
NOTE_CAKKAM = A3.NOTES_AY["(Cakkaṃ bandhitabbaṃ)"][1:-1]   # «Vòng luân chuyển nên được nối kết» (= 3-01)
DETAILED = "cũng nên được trình bày chi tiết như vậy"   # … vitthāretabbā (pi-2 1-khandhavibhango)
ANALYSED, TO_ANALYSE = "đã được phân tích", "cũng nên được phân tích như vậy"   # vibhattaṃ / vibhajitabbaṃ (pi-2)
YES_Q = f"“{A3.YES_WORD}”"               # āmantā (as a word in a note) «“Đúng vậy”» (= 3-01)
BOTH_WAYS = "ở cả hai chiều"             # ubhato / ubhatopi
ABRIDGED = A3.SAMKHITTA                  # saṃkhittaṃ «tóm lược» (abridged; = 3-01; termbase «co rút» is a mind's)
FULL = "đã đầy đủ"                       # paripuṇṇaṃ (2-02 «đầy đủ»)
BY_PEYYALA = "theo cách lược bớt"        # peyyālena
HARMONISE = "nên đối chiếu với các phần cặp câu hỏi khác"   # aññehi yamakehi saṃsanditabbaṃ

NOTE_LINES = {   # whole line bodies
    "(Yathā āyatanayamake cakkaṃ bandhitaṃ evamidha cakkaṃ bandhitabbaṃ.)":
        f"(Như {CYCLE} {LINKED_PAST} trong {T_AYATANA}, ở đây {CYCLE} cũng {LINKED} như vậy.)",
    "(Yathā āyatanayamake paṇṇatti evaṃ dhātuyamakepi paṇṇatti. Cakkaṃ bandhitabbaṃ).":
        f"(Như {DESIG} trong {T_AYATANA}, {DESIG} trong {T_DHATU} cũng như vậy. {NOTE_CAKKAM}).",
    "(Cakkaṃ bandhitabbaṃ, sabbe āmantā ubhatopi sesepi).":
        f"({NOTE_CAKKAM}, tất cả đều là {YES_Q}, {BOTH_WAYS} và cả ở các phần còn lại).",
    "(Yathā āyatanayamakassa paṇṇatti evaṃ dhātuyamakassa paṇṇatti vitthāretabbā)":
        f"(Như {DESIG} của {T_AYATANA}, {DESIG} của {T_DHATU} {DETAILED})",
    "(Yathā āyatanayamakaṃ vibhattaṃ evaṃ dhātuyamakampi vibhajitabbaṃ, sadisaṃ kātabbaṃ).":
        f"(Như {T_AYATANA} {ANALYSED}, {T_DHATU} {TO_ANALYSE}, nên được làm cho giống nhau).",
    "Namo tassa bhagavato arahato sammāsambuddhassa": S.HOMAGE,
}
NOTE_SENT = {    # sentences (inside a line); ⟦k⟧ = the line's protected variant bracket
    "(Cakkaṃ bandhitabbaṃ).": f"({NOTE_CAKKAM}).",
    "(Jivhāpi ghānadhātusadisā).": f"({cap(M.subj('jivhā'))} cũng giống như {M.subj('ghānadhātu')}).",
    "(Saddo ghānasadiso).": f"({cap(M.subj('saddo'))} giống như {M.subj('ghānaṃ')}).",
    "(Phoṭṭhabbo ghānasadiso).": f"({cap(M.subj('phoṭṭhabbo'))} giống như {M.subj('ghānaṃ')}).",
    "(saṃkhittaṃ ⟦0⟧, ubhato āmantā).": f"({ABRIDGED} ⟦0⟧, {BOTH_WAYS} đều là {YES_Q}).",
    "(dhātuyamakaṃ paripuṇṇaṃ peyyālena).": f"({T_DHATU} {FULL}, {BY_PEYYALA}).",
    "Dhātuyamakaṃ niṭṭhitaṃ.": S.yamaka_end(YAMAKA),     # = rails 8 «Cittayamakaṃ niṭṭhitaṃ.»
}

VARIANTS = {     # Pāli bracket -> Vietnamese (3-01 var_vi = 2-01 parse_variant where it fits)
    "[dhātu (sī. ka.) aññehi yamakehi saṃsanditabbaṃ]": S.var("Sī., Ka.", f"dhātu, {HARMONISE}"),
    **{br: A3.var_vi(br, "form") for br in ("[avaseso kāyo kāyo (syā.)]", "[yaṃ saṃkhittaṃ (syā.)]",
                                             "[avaseso kāyo (syā.)]", "[avasesā dhātū dhātū (syā.)]")},
}


# ===============================================================================================================
# 4. Questions: labeled (2-01), unlabeled, bare cut questions, fragments
# ===============================================================================================================
TAIL_POS = " không?"                     # end of B.name_q
TAIL_NEG = ", có phải không?"            # end of B.name_q_neg
_LAB = LABEL["Ka"] + " "
assert B.name_q("Ka", "a", "b").endswith(TAIL_POS) and B.name_q_neg("Ka", "a", "b").endswith(TAIL_NEG)


def case_as(pali, vi):
    """Keep the Pāli's initial case (a piece after …pe… may start lower case, as the sample)."""
    return cap(vi) if pali[:1].isupper() else vi[:1].lower() + vi[1:]


def unlabeled_q(na, a, b, end="?"):
    """'A B?' / 'na A na B?' without a label: 2-01's frame without «(a) » (= 3-01 nq); end="" for a clause cut by
    …pe… without «?» (3-01: «X có phải là Y không…»)."""
    if na:
        return A3.nq(None, M.pred(a), M.pred(b), end, neg=True)
    return A3.nq(None, M.subj(a), M.pred(b), end)


def bare_q(na, x):
    """A bare cut question 'X?' / 'Na X?' (the rest of the pair elided): the tail of its own frame
    (coordinator: a cut question ending in "?" = «… không?»): «X không?» / «Những gì không phải là X, có phải không?»."""
    return f"{B.NEG_SUBJ} {M.pred(x)}{TAIL_NEG}" if na else f"{cap(M.subj(x))}{TAIL_POS}"


def fragment(p):
    """A piece cut by …pe… without '?' or '.': a naming clause, a bare member, 'X ṭhapetvā'."""
    if m := re.fullmatch(r"([Nn]a) (\S+) na (\S+)", p):
        return case_as(p, unlabeled_q(True, m.group(2), m.group(3), end=""))
    if m := re.fullmatch(r"(\S+) ṭhapetvā", p):
        return case_as(p, A3.except_frag(M.subj(m.group(1))))
    if m := re.fullmatch(r"([Nn]a) (\S+)", p):
        return case_as(p, f"{B.NEG_SUBJ} {M.pred(m.group(2))}")
    if m := re.fullmatch(r"(\S+) (\S+)", p):
        return case_as(p, unlabeled_q(False, m.group(1), m.group(2), end=""))
    if re.fullmatch(r"\S+", p):
        return case_as(p, M.subj(p))
    raise ValueError(f"unknown fragment {p!r}")


def a_question_var(body):
    """'(Kha) dhātū ⟦0⟧ sotadhātu?' (a variant bracket after the subject) → 2-01's frame with the bracket after it."""
    m = re.fullmatch(B.LABEL_RE + r" (na )?(\S+) (⟦\d+⟧) (na )?(\S+?)\?((?: .*)?)", body)
    if not m:
        return None
    label, na1, a, ph, na2, b, rest = m.groups()
    if bool(na1) != bool(na2):
        raise ValueError(f"half-negated naming question {body!r}")
    if na1:
        q = B.name_q_neg(label, M.pred(a), M.pred(b))
        old = f"{LABEL[label]} {B.NEG_SUBJ} {M.pred(a)} "
    else:
        q = B.name_q(label, M.subj(a), M.pred(b))
        old = f"{LABEL[label]} {cap(M.subj(a))} "
    if not q.startswith(old):
        raise ValueError(f"cannot place {ph} in {body!r}")
    return old + ph + " " + q[len(old):], rest


# ===============================================================================================================
# 5. Answer sentences: family A (2-01) + the two shapes 2-01 lacks; family B with this chapter's person heads
# ===============================================================================================================
ATTR4 = A3.AY_ATTRS                      # sacakkhukānaṃ «có mắt» … (3-01; termbase / siblings)
ATTR_JOIN = A3.ATTR_JOIN                 # «, »: «những người có mắt, không có tai đang tái sinh» (3-01, one group)


def head4(head):
    """'Sacakkhukānaṃ asotakānaṃ upapajjantānaṃ' → «Ở những người có mắt, không có tai đang tái sinh» (3-01's
    ay_persons: one person group; one «Ở»). Only attribute heads occur in this chapter."""
    if not any(t.lower() in ATTR4 for t in head.split()):
        raise ValueError(f"unknown answer head {head!r}")
    return A3.answer_head(head, "tesaṃ")


def b_sentence4(s):
    """2-01's two family-B answer shapes (b_noca / b_both) with head4() as the head."""
    if m := re.fullmatch(r"(.+?) " + B.LOC_RE + r" (.+?), no ca \2 (.+?)\.", s):
        head, loc, c1, c2 = m.groups()
        a, v1 = B.split_mv(c1, M)
        b, v2 = B.split_mv(c2, M)
        return B.b_noca(head4(head), loc, a, v1, b, v2)
    if m := re.fullmatch(r"(.+?) " + B.LOC_RE + r" (.+?) ca (.+?) ca (.+?)\.", s):
        head, loc, c1, mid, c3 = m.groups()
        v1, b = B.split_vm(mid, M)
        return B.b_both(head4(head), loc, M.subj(c1), v1, b, B.verb(c3))
    return None


def except_rest_not_only(m, rest_subj, y):   # M ṭhapetvā avasesā X na Y. (no ", Z"): 2-01's words, no «mà là»
    return f"{B.EXCEPT} {m}, {rest_subj} còn lại không phải là {y}."


def _ca(word, conj):
    return word + ("ñca" if conj == "ñca" else "")


def sentence(s):
    if s in NOTE_SENT:
        return NOTE_SENT[s]
    if s in B.SHORT:
        return B.SHORT[s]
    if s in B.CLOSING:
        return B.CLOSING[s]
    s2 = re.sub(r" ṭhapetvā avases(?:o|aṃ) ", " ṭhapetvā avasesā ", s)   # gender of avasesa: same «những gì còn lại»
    if m := re.fullmatch(r"(\S+) ṭhapetvā avasesā ([^\s,]+) na ([^\s,]+)\.", s2):
        return except_rest_not_only(M.subj(m.group(1)), M.subj(m.group(2)), M.pred(m.group(3)))
    if m := re.fullmatch(r"(\S+?)(ñca| ca) (\S+?)(ñca| ca) ṭhapetvā avasesā (⟦\d+⟧) na ceva (\S+) na ca (\S+)\.", s2):
        return A3.except2_var(M.subj(_ca(m.group(1), m.group(2))), M.subj(_ca(m.group(3), m.group(4))),
                              M.pred(m.group(6)), M.pred(m.group(7)), m.group(5))
    if (r := B.a_sentence(s2, M)) is not None:
        return r
    if (r := b_sentence4(s)) is not None:
        return r
    raise ValueError(f"unknown sentence {s!r}")


def sentences(rest):
    return " ".join(sentence(x) for x in re.split(r"(?<=\.) ", rest.strip()) if x)


# ===============================================================================================================
# 6. Pieces and cut chains
# ===============================================================================================================
UQ_RE = re.compile(r"([Nn]a )?(\S+) (na )?(\S+?)\?((?: .*)?)")
BARE_RE = re.compile(r"([Nn]a )?(\S+)\?")


def piece(p):
    """One piece of a line between …pe… cuts (stripped)."""
    if p in NOTE_SENT:
        return NOTE_SENT[p]
    if re.match(B.LABEL_RE + " ", p):
        q = a_question_var(p) or B.a_question(p, M) or B.b_question(p, M)
        if not q:
            raise ValueError(f"unknown labeled question {p!r}")
        out, rest = q
        return out + (" " + sentences(rest) if rest.strip() else "")
    if (r := E.e_question(p, M)) is not None:
        return r
    if m := BARE_RE.fullmatch(p):
        return case_as(p, bare_q(bool(m.group(1)), m.group(2)))
    if m := UQ_RE.fullmatch(p):
        na1, a, na2, b, rest = m.groups()
        if bool(na1) != bool(na2):
            raise ValueError(f"half-negated naming question {p!r}")
        out = case_as(p, unlabeled_q(bool(na1), a, b))
        return out + (" " + sentences(rest) if rest.strip() else "")
    parts = [x for x in re.split(r"(?<=\.) ", p) if x]
    out = []
    for k, x in enumerate(parts):
        if x.endswith("."):
            out.append(sentence(x))
        elif k == len(parts) - 1:
            out.append(fragment(x))
        else:
            raise ValueError(f"cannot place {x!r} in {p!r}")
    return " ".join(out)


SEP = re.compile(r"(…[Pp]e…\.?|…\.?)")   # …pe… / …Pe… / … (a «.» right after it is absorbed: never «….»)


def chain(body):
    parts = SEP.split(body)
    out = []
    for i, x in enumerate(parts):
        if i % 2:
            out.append(S.PE)
            continue
        if not x.strip():
            out.append(x)
            continue
        lead, tail = x[:len(x) - len(x.lstrip())], x[len(x.rstrip()):]
        vi = piece(x.strip())
        if i + 1 < len(parts) and not tail and vi.endswith("."):
            vi = vi[:-1]                   # «Đúng vậy.…» → «Đúng vậy…» (never «.…»)
        out.append(lead + vi + tail)
    return "".join(out)


def tr_line(p):
    m = re.search(r" (\^\S+)$", p)
    bid = m.group(1) if m else None
    body = p[:m.start()] if m else p
    if body.startswith("#"):
        hashes, text = body.split(" ", 1)
        out = f"{hashes} {heading(text)}"
    elif body in NOTE_LINES:
        out = NOTE_LINES[body]
    elif body.startswith("Aṭṭhārasa dhātuyo"):
        out = uddesa(body)
    else:
        brs = re.findall(r"\[[^\]]*\]", body)
        for k, br in enumerate(brs):
            body = body.replace(br, f"⟦{k}⟧", 1)
        out = chain(body)
        for k, br in enumerate(brs):
            if br not in VARIANTS:
                raise ValueError(f"undeclared variant {br!r}")
            if out.count(f"⟦{k}⟧") != 1:
                raise ValueError(f"variant {br!r} lost in {p!r}")
            out = out.replace(f"⟦{k}⟧", VARIANTS[br])
    if "⟦" in out:
        raise ValueError(f"unplaced variant in {p!r}")
    return f"{out} {bid}" if bid else out


def build():
    return [[tr_line(ln) for ln in seg] for seg in S.segments_of(CH)]


# ===============================================================================================================
# 7. Checks: strings reused from pi-1 … pi-5 rails; frames shared with 2-01 / 2-02
# ===============================================================================================================
REUSED = [   # (Pāli, Vietnamese, book): asserted to occur in that book's Vietnamese rails
    ("Aṭṭhārasa dhātuyo – cakkhudhātu, … (pi-2 ^2-183)", f"{EIGHTEEN} – yếu tố mắt", "2"),
    ("cakkhuviññāṇadhātu (pi-2 ^2-183)", "yếu tố thức qua mắt", "2"),
    ("phoṭṭhabbadhātu (pi-2 ^2-183)", "yếu tố vật xúc chạm", "2"),
    ("dhammadhātu (pi-2 ^2-183)", "yếu tố đối tượng của ý", "2"),
    ("manoviññāṇadhātu (pi-2 ^2-183)", "yếu tố ý thức", "2"),
    ("rūpadhātu (eye object, pi-2 ^2-183)", "yếu tố hình sắc", "2"),
    ("dibbacakkhu (pi-5 Dibbacakkhukathā)", "thiên nhãn", "5"),
    ("(Yathā kusalattike vitthāro, evaṃ sabbepi tikā vitthāretabbā.) (pi-2)", DETAILED, "2"),
    ("(Yathā rūpakaṇḍe vibhattaṃ, tathā idha vibhajitabbaṃ.) (pi-2)", ANALYSED, "2"),
]


def check_reused():
    texts = {b: unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md"))))
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED if unicodedata.normalize("NFC", v).lower() not in texts[b].lower()]
    assert not bad, "reused strings not found in their rails: " + repr(bad)


def check_shared():
    # the «hiểu theo nghĩa» frame is 2-01's
    assert B.KHANDHA.sp("Piyarūpaṃ sātarūpaṃ") == sense("vật chất", ["điều đáng yêu", "điều khoan khoái"])
    assert B.KHANDHA.sp("Diṭṭhisaññā") == sense("tri giác", ["quan điểm"])
    # 2-01's suddha heading with this chapter's class word = the termbase heading
    assert B.suddha_varo(X_PL) == "Mục về các yếu tố thuần túy"
    # family E (2-02) heading
    assert PARINNAVARO == "Mục về sự hiểu biết trọn vẹn"
    # 3-01 (Āyatana): identical figurative-sense subjects and attribute beings, byte for byte
    assert A3.AY_SPECIAL == {k: M.sp(k) for k in A3.AY_SPECIAL} and set(A3.AY_SPECIAL) == set(SPECIAL)
    assert all(M.subj(k) == v for k, v in (("cakkhu", "mắt"), ("rūpaṃ", "vật chất"), ("dhammo", "hiện tượng")))
    for a in ("Sacakkhukānaṃ", "sasotakānaṃ", "asotakānaṃ", "acakkhukānaṃ", "Sacittakānaṃ"):
        assert ATTR4[a.lower()] in dict(TB_USED)[a], a
    assert head4("Sacakkhukānaṃ asotakānaṃ upapajjantānaṃ") == "Ở những người có mắt, không có tai đang tái sinh"


# ===============================================================================================================
# 8. Notes file (Pāli = tiếng Việt)
# ===============================================================================================================
def notes():
    out = []

    def row(p, v):
        out.append(f"{p} = {v}")

    def h(t):
        out.extend(["", f"## {t}", ""])

    out += [f"# pi-6 rails {N} (Dhātuyamaka): the eighteen elements in the family A / B frames of rails 2-01", "",
            "Builder: build_rails_4_vi.py (import with importlib). It imports build_rails_2-01_vi (families A / B, "
            "READ-ONLY), build_rails_7-01_vi (shared shapes) and build_rails_2-02_vi (family E, the one pariññā line) "
            "and adds: `DHATU`, `PLAIN`, `DHATU_M` (Members), `sense`, `SPECIAL`, `ATTR4`, `head4`, `b_sentence4`, "
            "`unlabeled_q`, `bare_q`, `fragment`, `piece`, `chain`, `NOTE_LINES`, `NOTE_SENT`, `VARIANTS`. "
            "Format: Pāli = tiếng Việt.", ""]
    h("Headings (2-01 heading() with the class word «yếu tố»)")
    for t in ("Dhātuyamakaṃ", "Paṇṇattivāro", "(Ka) uddeso", "(Kha) niddeso", "Padasodhanavāro",
              "Padasodhanamūlacakkavāro", "Suddhadhātuvāro", "Suddhadhātumūlacakkavāro", "(Ka) anulomaṃ",
              "(Kha) paccanīkaṃ", "Pavattivāro 1. uppādavāro", "(1) Paccuppannavāro", "(Ka) anulomapuggalo",
              "Pariññāvāro"):
        row(t, heading(t))
    for p in ("Paṇṇattiuddesavāro.", "Paṇṇattiniddesavāro.", "Dhātuyamakaṃ niṭṭhitaṃ."):
        row(p, sentence(p))
    h("Members (termbase; pi-2 ^2-183)")
    row("Aṭṭhārasa dhātuyo – …", f"{EIGHTEEN} – …  (pi-2)")
    for s, v in DHATU:
        row(f"{s}dhātu / {s}dhātuṃ / {s}dhātūti / {s}dhātuñca", v)
    for k, v, forms in PLAIN:
        row(" / ".join(forms), v)
    row("dhātū / dhātu / dhātuñca (subject) ; dhātu / dhātū (predicate)", f"{DHATU_SUBJ} ; {DHATU_PRED}")
    h("Special subjects in the «hiểu theo nghĩa …» frame (2-01; coordinator)")
    for k in SPECIAL:
        row(k, M.sp(k))
    h("Family A (2-01 frames) as built here")
    for p in ("(Ka) cakkhu cakkhudhātu?", "(Kha) dhātū sotadhātu?", "(Ka) cakkhu dhātu?", "(Kha) dhātū cakkhu?",
              "(Ka) na dhammo na dhammadhātu?", "(Kha) na dhātū na cakkhu?", "(Kha) rūpadhātu rūpanti? Āmantā."):
        row(p, piece(p))
    for s in ("Dibbacakkhu paññācakkhu cakkhu, na cakkhudhātu.", "Cakkhudhātu cakkhu ceva cakkhudhātu ca.",
              "Sotadhātu sotañceva sotadhātu ca.", "Rūpadhātuṃ ṭhapetvā avasesaṃ rūpaṃ, na rūpadhātu.",
              "Dibbasotaṃ taṇhāsotaṃ na sotadhātu, sotaṃ.",
              "Cakkhuñca cakkhudhātuñca ṭhapetvā avasesaṃ na ceva cakkhu na ca cakkhudhātu.",
              "Kāyadhātuṃ ṭhapetvā avaseso na kāyadhātu, kāyo.", "Sotadhātu dhātu ceva sotadhātu ca.",
              "Avasesā dhātū na sotadhātu.", "Cakkhuṃ ṭhapetvā avasesā dhātū na cakkhu, dhātu.",
              "Cakkhuñca dhātuñca ṭhapetvā avasesā na ceva cakkhu na ca dhātū."):
        row(s, sentence(s))
    row("avaseso / avasesaṃ / avasesā (after ṭhapetvā)", f"{B.REST} (one Vietnamese for every gender)")
    h("New shapes (not in 2-01)")
    row("Cakkhuṃ ṭhapetvā avasesā dhātū na cakkhudhātu. (no «, Z»)",
        sentence("Cakkhuṃ ṭhapetvā avasesā dhātū na cakkhudhātu."))
    row("Kāyañca kāyadhātuñca ṭhapetvā avaseso [var] na ceva kāyo na ca kāyadhātu.",
        sentence("Kāyañca kāyadhātuñca ṭhapetvā avaseso ⟦1⟧ na ceva kāyo na ca kāyadhātu.").replace("⟦1⟧", "[var]"))
    row("(Kha) dhātū [var] sotadhātu?", a_question_var("(Kha) dhātū ⟦0⟧ sotadhātu?")[0].replace("⟦0⟧", "[var]"))
    row("Ghānaṃ dhātu? / na gandho na gandhadhātūti? (no label)",
        f"{piece('Ghānaṃ dhātu?')} / {piece('na gandho na gandhadhātūti?')}  (2-01 frame without the label; "
        "the Pāli's initial case kept)")
    row("Ghānaviññāṇaṃ? (bare cut question)", piece("Ghānaviññāṇaṃ?"))
    row("Na ghānaṃ? (bare cut question)", piece("Na ghānaṃ?"))
    row("Dhātū ghānadhātu…pe… (cut naming clause)", fragment("Dhātū ghānadhātu") + S.PE)
    row("Na dhātū na sotadhātu…pe… (cut naming clause)", fragment("Na dhātū na sotadhātu") + S.PE)
    row("Sotaviññāṇaṃ…pe… / Na jivhā… / Sotaṃ ṭhapetvā…pe… / saddaṃ…",
        f"{fragment('Sotaviññāṇaṃ')}{S.PE} / {fragment('Na jivhā')}{S.PE} / {fragment('Sotaṃ ṭhapetvā')}{S.PE} / "
        f"{fragment('saddaṃ')}{S.PE}")
    row("Āmantā.…Pe… (a «.» before a cut)", f"{S.YES[:-1]}{S.PE}  (never «.…»)")
    row("…pe…. / …. (a «.» after a cut)", f"{S.PE}  (absorbed)")
    h("Family B (2-01 frames) with this chapter's heads")
    row("(Ka) yassa cakkhudhātu uppajjati tassa sotadhātu uppajjatīti?",
        piece("(Ka) yassa cakkhudhātu uppajjati tassa sotadhātu uppajjatīti?"))
    row("(Kha) yassa vā pana sotadhātu uppajjati tassa cakkhudhātu uppajjatīti?",
        piece("(Kha) yassa vā pana sotadhātu uppajjati tassa cakkhudhātu uppajjatīti?"))
    for k, v in ATTR4.items():
        row(k, v)
    row("<attr>ānaṃ <attr>ānaṃ upapajjantānaṃ (one group)", f"{B.AT} {B.PERSON} <attr>{ATTR_JOIN}<attr> "
        f"{B.PARTICIPLES['upapajjantānaṃ'][0]}")
    for s in ("Sacakkhukānaṃ asotakānaṃ upapajjantānaṃ tesaṃ cakkhudhātu uppajjati, no ca tesaṃ sotadhātu uppajjati.",
              "Sacakkhukānaṃ sasotakānaṃ upapajjantānaṃ tesaṃ cakkhudhātu ca uppajjati sotadhātu ca uppajjati.",
              "Sarūpakānaṃ acakkhukānaṃ upapajjantānaṃ tesaṃ rūpadhātu uppajjati, no ca tesaṃ cakkhudhātu uppajjati.",
              "Acakkhukānaṃ upapajjantānaṃ tesaṃ dhammadhātu uppajjati, no ca tesaṃ cakkhudhātu uppajjati."):
        row(s, sentence(s))
    h("Family E (2-02) as built here")
    p = "Yo cakkhudhātuṃ parijānāti so sotadhātuṃ parijānātīti? Āmantā."
    row(p, piece(p))
    h("Editorial notes")
    for k, v in NOTE_LINES.items():
        if k.startswith("("):
            row(k, v)
    for k, v in NOTE_SENT.items():
        if k.startswith("("):
            row(k, v)
    for k, v in VARIANTS.items():
        row(k, v)
    h("Termbase gaps and choices (for the coordinator)")
    out += [
        "- dhammo / dhammaṃ / Dhammañca: no termbase headword; the core term dhamma «hiện tượng» (= the Dhammayamaka "
        "title «các hiện tượng»). dhammadhātu stays the termbase «yếu tố đối tượng của ý».",
        "- rūpaṃ: the termbase has only «vật chất» (= 2-01); rūpadhātu is «yếu tố hình sắc». So «Vật chất có phải là "
        "yếu tố hình sắc không?» / «Ngoại trừ yếu tố hình sắc, những gì còn lại là vật chất …»: the meaning holds "
        "(the remaining rūpa is matter); 3-01 should take the same (rūpāyatana pair).",
        "- sarūpakānaṃ «có vật chất», saghānakānaṃ «có mũi», aghānakānaṃ «không có mũi»: no termbase headword; 3-01's "
        "AY_ATTRS (siblings sacakkhuka «có mắt» / acakkhuka «không có mắt», rūpaṃ «vật chất»).",
        "- Two attributes of one reborn group: 3-01's ATTR_JOIN «, »: «những người có mắt, không có tai đang tái sinh» "
        "(head = 3-01 answer_head / ay_persons).",
        "- saṃkhittaṃ «tóm lược» (= 3-01; the termbase sense «co rút» is the contracted mind).",
        "- Cakkaṃ bandhitabbaṃ «Vòng luân chuyển nên được nối kết» (= 3-01 NOTES_AY), bandhitaṃ «đã được nối kết»; "
        "aññehi yamakehi "
        "saṃsanditabbaṃ «nên đối chiếu với các phần cặp câu hỏi khác»; ubhato(pi) «ở cả hai chiều»; sesepi «cả ở các "
        "phần còn lại»; sadisaṃ kātabbaṃ «nên được làm cho giống nhau»; paripuṇṇaṃ peyyālena «đã đầy đủ, theo cách "
        "lược bớt» (2-02 paripuṇṇaṃ «đầy đủ»): no termbase entries.",
        "- vitthāretabbā «cũng nên được trình bày chi tiết như vậy», vibhattaṃ / vibhajitabbaṃ «đã được phân tích» / "
        "«cũng nên được phân tích như vậy»: pi-2 notes.",
        "- Yamaka titles inside notes in “…” with capitals (as rails 8's note); the termbase cross-reference forms "
        "(āyatanayamake «các cặp câu hỏi về các lĩnh vực nhận biết» …) are those titles.",
        "- Bare cut questions «Thức qua mũi không?» / «Những gì không phải là mũi, có phải không?»: the tail of their "
        "own frame (coordinator «… không?» for a cut question ending in «?»); for the coordinator to confirm.",
        "",
        "## Slips and unsure Pāli (translated as written or as plainly meant)",
        "",
        "- ^6-4-17 «Cakkhuṃ ṭhapetvā avasesā dhātū na cakkhudhātu.» (the parallel lines have «na cakkhu, dhātu»): "
        "translated as written «… không phải là yếu tố mắt.».",
        "- ^6-4-17 «Cakkhu ca dhātuñca» (for Cakkhuñca) and «na ca dhātu» / «na ca dhātū»: same Vietnamese.",
        "- ^6-4-15 «jivha ṭhapetvā» (short spelling, termbase jivha): «ngoại trừ lưỡi».",
        "- ^6-4-11 «Na gandhadhātu na gandhoti?», «Na cakkhuviññāṇadhātu …?» have no (Kha) label: kept unlabeled.",
        "- ^6-4-17 the note «(Yathā … vitthāretabbā)» has no final «.»: none added.",
        "- ^6-4-9 «?…Pe….» / ^6-4-10 «kāyaviññāṇaṃ….»: the «.» after the cut is absorbed («…»).",
        "- ^6-4-19 «Āmantā.…Pe…»: «Đúng vậy…».",
        "",
    ]
    return "\n".join(out)


def main():
    S.check_reused()
    B.check_reused()
    check_reused()
    check_termbase()
    check_shared()
    segs = build()
    S.write(CH, segs)
    text = (S.OUT_DIR / CH).read_text(encoding="utf-8")
    ADH_DIR.mkdir(parents=True, exist_ok=True)
    (ADH_DIR / CH).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", ADH_DIR / CH)
    NOTES_MD.write_text(unicodedata.normalize("NFC", notes()), encoding="utf-8", newline="\n")
    print("wrote", NOTES_MD)


if __name__ == "__main__":
    main()
