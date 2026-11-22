"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 10-03 (Indriyayamaka 3: pavattivāra, uppādavāra, paccuppanna,
(Ga) anulomapuggalokāsā and (Gha) paccanīkapuggalo).

Setters (all imported READ-ONLY with importlib; every shared string comes from their functions):
  build_rails_10-02_vi  (I2)  Indriya person heads: IND_ATTRS, SEX / sex_vi, FEEL / feel_vi, ind_group, ind_persons,
                              faculty_mind_gen, ind_answer_head, PRON_FEM, pv_sentence / pv_line / tr_line, heading
  build_rails_10-01_vi  (I)   INDRIYA members, ind_mulaka
  build_rails_9-01_vi   (DY)  verb() with a separate "na", PAVATTE, moment_vi, ALL_BEINGS, EXTRA_PERSON, answer_head
  build_rails_3-01_vi / 3-02 (A / A2), build_rails_2-01_vi (B), build_rails_7-01_vi (C), build_rails_8_vi (D8)
  (all reached through I2, i.e. the very module objects 10-02 uses)

New here (named constants; later Indriya chapters import them):
  verb / split_mv              B.VERB_TABLE + a separate "na" (9-01 verb): na uppajjati «không sinh khởi»
  NEG_BOTH_RE / pv_sentence10  "A-ñca na V B-ñca na V" «A không V, B cũng không V» (2-01 b_both, 7-02 negative both)
  SEX_ALSO / sex_list_vi       two sex words in one group: na itthīnaṃ na purisānaṃ upapajjantānaṃ «… đang tái sinh
                               không làm người nữ, cũng không làm người nam» (7-01 / 7-04 neither shape)
  PART_READING                 uppajjantīnaṃ = upapajjantīnaṃ (termbase reading «đang tái sinh»)
  persons10 / head_parts10 / answer_head10   heads with Sabbesaṃ cavantānaṃ + Indriya words, Sabbesaṃ cittassa
                               bhaṅgakkhaṇe + faculty minds + nirodhasamāpannānaṃ asaññasattānaṃ (9-01 shape)
  question10 / unit10 / line10 / tr_line / build
Every line 10-02 can parse is asserted byte-identical to 10-02; every head 9-01 or 10-02 can parse, to theirs;
every question 3-01 can parse, to 3-01's. A line, unit or word the parsers cannot place raises ValueError.
Importing writes nothing.

usage: python -I -X utf8 -B build_rails_10-03_vi.py
"""
import importlib
import re
import sys
import unicodedata

RAILS_DIR = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\rails"
if RAILS_DIR not in sys.path:
    sys.path.insert(0, RAILS_DIR)
import build_rails_sample_vi as S  # noqa: E402  (READ-ONLY)
I2 = importlib.import_module("build_rails_10-02_vi")   # READ-ONLY: Indriya person heads (setter)
I = importlib.import_module("build_rails_10-01_vi")    # READ-ONLY: Indriya members
DY = importlib.import_module("build_rails_9-01_vi")    # READ-ONLY: separate-na verbs, moment heads
A, A2, B, C, D8 = I2.A, I2.A2, I2.B, I2.C, I2.D8       # the same module objects 10-02 uses

cap = S.cap
lc = I2.lc
CH = "10-03-indriyayamaka.md"
N = "10-03"
NOTES_MD = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/notes-rails-{N}.md"
ADH_DIR = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/adh-{N}"
M_IND = I.INDRIYA
PLANES = A.PLANES_AY
CHECKED = {"10-02 line": 0, "10-02 head": 0, "9-01 head": 0, "3-01 question": 0, "10-02 persons": 0}
SLIPS_SEEN = []
HEADS_SEEN = {}


# ===============================================================================================================
# 1. Verbs: a separate "na" (9-01 verb = coordinator: a separate na negates the positive term)
# ===============================================================================================================
verb = DY.verb


def split_mv(chunk, M=None):
    """'cakkhundriyaṃ na uppajjati' → («năng lực mắt», verb tuple). Verb = last two words, else the last."""
    M = M or M_IND
    w = chunk.split()
    for k in (2, 1):
        if len(w) > k and DY.is_verb(" ".join(w[-k:])):
            return M.subj(" ".join(w[:-k])), verb(" ".join(w[-k:]))
    raise ValueError(f"no member + verb in {chunk!r}")


# ===============================================================================================================
# 2. Person phrases
# ===============================================================================================================
PART_READING = {"uppajjantīnaṃ": "upapajjantīnaṃ"}   # termbase: the reading uppajjantīnaṃ «đang tái sinh»
SEX_ALSO = ", cũng "                                # na itthīnaṃ na purisānaṃ: «không làm người nữ, cũng không làm
#                                                     người nam» (7-01 / 7-04 neither: «không A, cũng không B»)
PERSON_WORDS = (set(I2.NEW_WORDS) | set(B.QUANT) | set(B.PARTICIPLES) | set(I2.PRE_ATTRS) | set(I2.PART_FEM)
                | set(I2.QUANT_FEM) | set(PART_READING))


def sex_list_vi(keys_neg):
    """[(key, neg)] → «không làm người nữ, cũng không làm người nam» (one sex word: 10-02 sex_vi)."""
    if len(keys_neg) == 1:
        return I2.sex_vi(*keys_neg[0])
    if not all(n for _, n in keys_neg):
        raise ValueError(f"positive sex word in a list {keys_neg!r}")
    return SEX_ALSO.join(I2.sex_vi(k, n) for k, n in keys_neg)


def _groups(toks):
    """Split a person phrase at its participles: one token list per group."""
    out, cur = [], []
    for t in toks:
        cur.append(t)
        tl = lc(t)
        if tl in B.PARTICIPLES or tl in I2.PART_FEM:
            out.append(cur)
            cur = []
    if cur:
        raise ValueError(f"dangling words {cur!r}")
    return out


def _double_sex_group(toks):
    """One group with two sex words (na itthīnaṃ na purisānaṃ …) → Vietnamese, else None."""
    sexes = [lc(t) for t in toks if lc(t) in I2.SEX]
    if len(sexes) < 2:
        return None
    quant, pre, sex, neg, part = None, [], [], False, None
    for t in toks:
        tl = lc(t)
        if tl == "na":
            if neg:
                raise ValueError(f"double na in {toks!r}")
            neg = True
        elif tl in B.QUANT:
            quant = tl
        elif tl in I2.PRE_ATTRS:
            pre.append(I2.PRE_ATTRS[tl])
        elif tl in I2.SEX:
            sex.append((tl, neg))
            neg = False
        elif tl in B.PARTICIPLES or tl in I2.PART_FEM:
            part = I2.PART_FEM.get(tl, tl)
        else:
            raise ValueError(f"word {t!r} not set beside two sex words in {toks!r}")
    if neg:
        raise ValueError(f"dangling na in {toks!r}")
    return I2.ind_group(quant, pre, part, sex_list_vi(sex), None)


def persons10(head):
    """Genitive person phrase → Vietnamese groups (no «Ở»): 10-02 ind_persons, plus groups with two sex words and the
    termbase reading uppajjantīnaṃ. Asserted equal to 10-02 wherever 10-02 parses the phrase."""
    toks = []
    for t in head.split():
        if lc(t) in PART_READING:
            SLIPS_SEEN.append((t, PART_READING[lc(t)]))
            t = PART_READING[lc(t)]
        toks.append(t)
    fixed = " ".join(toks)
    groups = _groups(toks)
    if not any(_double_sex_group(g) for g in groups):
        out = I2.ind_persons(fixed)
    else:
        out = B.join_and(_double_sex_group(g) or I2.ind_persons(" ".join(g)) for g in groups)
    try:
        old = I2.ind_persons(head)
    except ValueError:
        old = None
    if old is not None:
        assert old == out, (head, old, out)
        CHECKED["10-02 persons"] += 1
    return out


def _is_person_tok(t):
    tl = lc(t)
    return tl in PERSON_WORDS


def head_parts10(head):
    """Answer head (before tesaṃ / tāsaṃ [tattha]) → parts joined «, » (9-01 head_parts shape): person runs «ở …»,
    pavatte «trong đời sống», <mind> <moment> «vào khoảnh khắc … của tâm …» (10-02 faculty_mind_gen), bare Sabbesaṃ
    before a moment «tất cả chúng sinh» (9-01), nirodhasamāpannānaṃ (8 / 9-01), plane-beings (2-01)."""
    toks = head.split()
    parts, run, i = [], [], 0

    def flush():
        if run:
            if len(run) > 1 and any(f" {C.AND} " in g for g in run):
                raise ValueError(f"«và» inside a group of a longer person run: {head!r}")
            parts.append(f"{C.AT} {B.join_and(run)}")
            run.clear()

    while i < len(toks):
        t, lt = toks[i], lc(toks[i])
        if i + 1 < len(toks) and lc(toks[i + 1]) in D8.MOMENT:
            flush()
            parts.append(DY.moment_vi(toks[i + 1], I2.faculty_mind_gen(t)))
            i += 2
        elif lt == "pavatte":
            flush()
            parts.append(DY.PAVATTE)
            i += 1
        elif lt in DY.EXTRA_PERSON:
            run.append(DY.EXTRA_PERSON[lt])
            i += 1
        elif lt == "sabbesaṃ" and not (i + 1 < len(toks) and _is_person_tok(toks[i + 1])):
            run.append(DY.ALL_BEINGS)
            i += 1
        elif (pt := B.plane_tok(lt, PLANES)) and pt[1] == "gen":
            run.append(B.persons(t, PLANES))
            i += 1
        elif _is_person_tok(t):
            j = i + 1
            while j < len(toks) and _is_person_tok(toks[j]) and not (
                    j + 1 < len(toks) and lc(toks[j + 1]) in D8.MOMENT):
                j += 1
            run.append(persons10(" ".join(toks[i:j])))
            i = j
        else:
            raise ValueError(f"unknown word {t!r} in answer head {head!r}")
    flush()
    if not parts:
        raise ValueError(f"empty answer head {head!r}")
    return parts


def answer_head10(head, loc):
    if loc == "tattha":
        return B.place_head(head, PLANES)
    out = cap(", ".join(head_parts10(head)))
    for name, f in (("10-02 head", lambda: I2.ind_answer_head(head, loc)),
                    ("9-01 head", lambda: DY.answer_head(head, loc))):
        try:
            old = f()
        except (ValueError, KeyError):
            continue
        assert old == out, (name, head, old, out)
        CHECKED[name] += 1
    HEADS_SEEN[head] = out
    return out


# ===============================================================================================================
# 3. Questions, sentences, units, lines
# ===============================================================================================================
def question10(q, M=None):
    """(Ka) yassa [yattha] A [na] V tassa [tattha] B [na] Vti (without «?») → 2-01 b_q (coordinator shell)."""
    M = M or M_IND
    m = A.BQ_RE.fullmatch(q)
    if not m:
        raise ValueError(f"unknown question {q!r}")
    label, w1, vapana, w2, c1, then, c2 = m.groups()
    if label is None and w1[0] != w1[0].upper():
        raise ValueError(f"unlabelled lower-case question {q!r}")
    a, v1 = split_mv(c1, M)
    b, v2 = split_mv(c2, M)
    out = B.b_q(label, lc(w1) + (w2 or ""), then, a, v1[0], b, v2[0], other=bool(vapana))
    try:
        old = A.question_vi(q, M)
    except (ValueError, KeyError):
        old = None
    if old is not None:
        assert old == out, (q, old, out)
        CHECKED["3-01 question"] += 1
    return out


LOCP = I2.LOCP
NOCA_RE = I2.NOCA_RE
NEG_BOTH_RE = re.compile(r"(.+?) " + LOCP + r" (\S+?ñca) ((?:na )?\S+) (\S+?ñca) ((?:na )?\S+)\.")


def pv_sentence10(s, M=None):
    """Family B answers (2-01 b_noca / b_both) with this chapter's heads and separate-na verbs."""
    M = M or M_IND
    if m := NOCA_RE.fullmatch(s):
        head, loc, c1, c2 = m.groups()
        a, v1 = split_mv(c1, M)
        b, v2 = split_mv(c2, M)
        return B.b_noca(answer_head10(head, loc), I2.PRON_FEM.get(loc, loc), a, v1, b, v2)
    if m := NEG_BOTH_RE.fullmatch(s):
        head, loc, c1, v1, c2, v2 = m.groups()
        return B.b_both(answer_head10(head, loc), I2.PRON_FEM.get(loc, loc), M.subj(c1), verb(v1), M.subj(c2),
                        verb(v2))
    return None


def unit10(u, M=None):
    M = M or M_IND
    if (lab := I.ind_mulaka(u, M)) is not None:
        return lab
    if u.endswith("?"):
        return question10(u[:-1], M)
    if u in B.SHORT:
        return B.SHORT[u]
    if (out := pv_sentence10(u, M)) is not None:
        return out
    raise ValueError(f"unknown unit {u!r}")


def line10(body, M=None):
    body, label = body.strip(), None
    if "…" in body:
        raise ValueError(f"cut not set in this chapter: {body!r}")
    if m := re.fullmatch(r"(.+?) (\(\w+mūlakaṃ\)\.?)", body):     # trailing (Xindriyamūlakaṃ) label (10-02)
        body, label = m.group(1), m.group(2)
    units = [x for x in re.split(r"(?<=[.?]) (?=\S)", body) if x]
    if label:
        units.append(label)
    return " ".join(unit10(x, M) for x in units)


def tr_line(p, M=None, fixed=None):
    M = M or M_IND
    m = re.search(r" (\^\S+)$", p)
    bid = m.group(1) if m else None
    body = p[:m.start()] if m else p
    if "[" in body:
        raise ValueError(f"variant bracket not handled: {p!r}")
    if body.startswith("#"):
        hashes, text = body.split(" ", 1)
        out = f"{hashes} {I2.heading(text)}"
    elif fixed and body in fixed:
        out = fixed[body]
    else:
        out = line10(body, M)
    try:
        old = I2.tr_line(p, True, M, fixed)
    except (ValueError, KeyError):
        old = None
    full = f"{out} {bid}" if bid else out
    if old is not None:
        assert old == full, ("10-02 line", p, old, full)
        CHECKED["10-02 line"] += 1
    return full


def build(name, M=None, fixed=None):
    return [[tr_line(ln, M, fixed) for ln in seg] for seg in S.segments_of(name)]


# ===============================================================================================================
# 4. Checks
# ===============================================================================================================
TERMBASE_USED = [   # pi-6 termbase entries used verbatim («Pāli: {…: Vietnamese}»)
    ("uppajjantīnaṃ", B.PARTICIPLES["upapajjantānaṃ"][0]), ("cavantānaṃ", B.PARTICIPLES["cavantānaṃ"][0]),
    ("nirodhasamāpannānaṃ", "người nhập thành tựu thiền chấm dứt"), ("itthīnaṃ", I2.SEX["itthīnaṃ"]),
    ("purisānaṃ", I2.SEX["purisānaṃ"]), ("cittassa bhaṅgakkhaṇe", "khoảnh khắc tan rã của tâm"),
]


def check_termbase():
    tb = I2.termbase_text()
    bad = [(p, v) for p, v in TERMBASE_USED
           if not re.search(rf"^{re.escape(p)}: {{.*: {re.escape(v)}}}$", tb, re.M)]
    assert not bad, "termbase entries not matched: " + repr(bad)
    assert DY.EXTRA_PERSON["nirodhasamāpannānaṃ"].endswith("người nhập thành tựu thiền chấm dứt")
    I2.check_termbase()                  # every faculty kind of mind built here (I2.MINDS_SEEN) = its termbase entry


def check_frames():
    assert verb("na uppajjati")[0] == B.VERB["nuppajjati"][0]        # separate na = fused negative «không sinh khởi»
    assert sex_list_vi([("itthīnaṃ", True)]) == I2.sex_vi("itthīnaṃ", True)
    for hd in ("Sabbesaṃ cavantānaṃ acakkhukānaṃ asotakānaṃ upapajjantānaṃ", "Sacakkhukānaṃ na itthīnaṃ upapajjantānaṃ",
               "Sabbesaṃ cavantānaṃ acakkhukānaṃ na itthīnaṃ upapajjantānaṃ"):
        assert persons10(hd) == I2.ind_persons(hd), hd
    hd = "Sabbesaṃ cittassa bhaṅgakkhaṇe nirodhasamāpannānaṃ asaññasattānaṃ"
    assert answer_head10(hd, "tesaṃ") == DY.answer_head(hd, "tesaṃ")
    hd = "Sabbesaṃ cavantānaṃ pavatte cittassa bhaṅgakkhaṇe"
    assert answer_head10(hd, "tesaṃ") == DY.answer_head(hd, "tesaṃ")


# ===============================================================================================================
# 5. Notes file (Pāli = tiếng Việt)
# ===============================================================================================================
def notes():
    M = M_IND
    out = []

    def row(p, v):
        out.append(f"{p} = {v}")

    def h(t):
        out.extend(["", f"## {t}", ""])

    out += [f"# pi-6 rails {N} (Indriyayamaka 3): (Ga) anulomapuggalokāsā, (Gha) paccanīkapuggalo", "",
            "Builder: build_rails_10-03_vi.py (import with importlib). Setter: build_rails_10-02_vi (ind_persons, "
            "ind_group, sex_vi, feel_vi, faculty_mind_gen, ind_answer_head, PRON_FEM, heading); 9-01 verb (separate "
            "na), PAVATTE, moment_vi, ALL_BEINGS, EXTRA_PERSON; 2-01 b_q / b_noca / b_both; 3-01 BQ_RE; 10-01 "
            "INDRIYA / ind_mulaka; all READ-ONLY. Every line 10-02 parses, every head 9-01 / 10-02 parse and every "
            "question 3-01 parses is asserted byte-identical. Exposed: `verb`, `split_mv`, `PART_READING`, "
            "`SEX_ALSO`, `sex_list_vi`, `persons10`, `head_parts10`, `answer_head10`, `question10`, `NEG_BOTH_RE`, "
            "`pv_sentence10`, `unit10`, `line10`, `tr_line`, `build`. Format: Pāli = tiếng Việt.", ""]
    h("Headings")
    for t in ("(Ga) anulomapuggalokāsā", "(Gha) paccanīkapuggalo"):
        row(t, I2.heading(t))
    h("Verbs and questions (separate na)")
    row("na uppajjati", verb("na uppajjati")[0])
    row("no ca tesaṃ B na uppajjati", "nhưng ở những người ấy B " + B.denied_vi(verb("na uppajjati")[2]))
    for q in ("(Ka) yassa cakkhundriyaṃ na uppajjati tassa sotindriyaṃ na uppajjatīti",
              "(Kha) yassa vā pana sotindriyaṃ na uppajjati tassa cakkhundriyaṃ na uppajjatīti",
              "(Ka) yassa yattha cakkhundriyaṃ uppajjati tassa tattha sotindriyaṃ uppajjatīti"):
        row(q + "?", question10(q, M))
    h("Person words and heads new here")
    row("na itthīnaṃ na purisānaṃ upapajjantānaṃ (two sex words, set here)",
        I2.ind_group(None, [], "upapajjantānaṃ", sex_list_vi([("itthīnaṃ", True), ("purisānaṃ", True)])))
    row("uppajjantīnaṃ (termbase: the reading for upapajjantīnaṃ)", B.PARTICIPLES["upapajjantānaṃ"][0])
    for hd in ("Sabbesaṃ cavantānaṃ acakkhukānaṃ asotakānaṃ upapajjantānaṃ",
               "Sabbesaṃ cavantānaṃ acakkhukānaṃ na itthīnaṃ upapajjantānaṃ",
               "Sabbesaṃ cavantānaṃ na itthīnaṃ acakkhukānaṃ upapajjantānaṃ",
               "Sabbesaṃ cavantānaṃ vinā somanassena acakkhukānaṃ upapajjantānaṃ",
               "Sabbesaṃ cavantānaṃ acakkhukānaṃ vinā upekkhāya upapajjantānaṃ",
               "Sabbesaṃ cavantānaṃ vinā somanassena na itthīnaṃ upapajjantānaṃ",
               "Sabbesaṃ cavantānaṃ na itthīnaṃ vinā somanassena upapajjantānaṃ",
               "Sabbesaṃ cavantānaṃ na itthīnaṃ na purisānaṃ upapajjantānaṃ",
               "Itthīnaṃ ñāṇasampayuttānaṃ uppajjantīnaṃ"):
        row(hd, persons10(hd))
    for hd in ("Sabbesaṃ cavantānaṃ pavatte cittassa bhaṅgakkhaṇe",
               "Sabbesaṃ cittassa bhaṅgakkhaṇe somanassavippayuttaupekkhāvippayuttacittassa uppādakkhaṇe "
               "nirodhasamāpannānaṃ asaññasattānaṃ",
               "Sabbesaṃ cittassa bhaṅgakkhaṇe nirodhasamāpannānaṃ asaññasattānaṃ",
               "Pavatte saddhāvippayuttasomanassasampayuttacittassa uppādakkhaṇe"):
        row(f"{hd} tesaṃ …", f"{answer_head10(hd, 'tesaṃ')}, {C.THEN} {B.L['tesaṃ']} …")
    h("Sample lines")
    for s in ("Acakkhukānaṃ sasotakānaṃ upapajjantānaṃ tesaṃ cakkhundriyaṃ na uppajjati, no ca tesaṃ sotindriyaṃ na "
              "uppajjati. Sabbesaṃ cavantānaṃ acakkhukānaṃ asotakānaṃ upapajjantānaṃ tesaṃ cakkhundriyañca na uppajjati "
              "sotindriyañca na uppajjati.",
              "Purisānaṃ upapajjantānaṃ tesaṃ itthindriyaṃ na uppajjati, no ca tesaṃ purisindriyaṃ na uppajjati. "
              "Sabbesaṃ cavantānaṃ na itthīnaṃ na purisānaṃ upapajjantānaṃ tesaṃ itthindriyañca na uppajjati "
              "purisindriyañca na uppajjati.",
              "Upekkhāya upapajjantānaṃ pavatte upekkhāsampayuttacittassa uppādakkhaṇe tesaṃ somanassindriyaṃ na "
              "uppajjati, no ca tesaṃ upekkhindriyaṃ na uppajjati. Sabbesaṃ cittassa bhaṅgakkhaṇe "
              "somanassavippayuttaupekkhāvippayuttacittassa uppādakkhaṇe nirodhasamāpannānaṃ asaññasattānaṃ tesaṃ "
              "somanassindriyañca na uppajjati upekkhindriyañca na uppajjati.",
              "Sacakkhukānaṃ itthīnaṃ upapajjantīnaṃ tāsaṃ tattha cakkhundriyañca uppajjati itthindriyañca uppajjati."):
        row(s, line10(s, M))
    h("Termbase misfits and gaps (for the coordinator)")
    out += [
        "- Sex / feeling words beside cavantānaṃ: in this chapter they always belong to the following upapajjantānaṃ "
        "group («Sabbesaṃ cavantānaṃ na itthīnaṃ acakkhukānaṃ upapajjantānaṃ» beside «… acakkhukānaṃ na itthīnaṃ "
        "upapajjantānaṃ»), so 10-02's shape applies unchanged: «tất cả những người đang chết đi và những người không "
        "có mắt đang tái sinh không làm người nữ». No sex / feeling word goes with cavantānaṃ itself, and none with a "
        "plane (still not set; the builder raises).",
        "- Two sex words in one group (na itthīnaṃ na purisānaṃ upapajjantānaṃ, ^6-10-215 block, both (Ka) and (Kha)): set "
        "here as «những người đang tái sinh không làm người nữ, cũng không làm người nam» (7-01 / 7-04 neither shape "
        "«không A, cũng không B»). Please confirm.",
        "- na uppajjati (separate na, all of (Gha)): 9-01 verb «không sinh khởi»; after no ca «vẫn sinh khởi» (7-01); "
        "both-frame «A không sinh khởi, B cũng không sinh khởi» (2-01 b_both, 7-02).",
        "- Sabbesaṃ before cittassa bhaṅgakkhaṇe: 9-01 «Ở tất cả chúng sinh, vào khoảnh khắc tan rã của tâm, …»; "
        "nirodhasamāpannānaṃ asaññasattānaṃ after the moments keep their own «ở» (coordinator).",
        "",
        "## Pāli as written (reported)",
        "",
        "- ^6-10-206 block (Ka) itthindriyaṃ … paññindriyaṃ: «Itthīnaṃ ñāṇasampayuttānaṃ uppajjantīnaṃ» (for "
        "upapajjantīnaṃ): the termbase reading entry uppajjantīnaṃ «đang tái sinh» is used (rendered as meant).",
        "- ^6-10-204 last answer «Sacakkhukānaṃ upapajjantānaṃ …» (no sacittakānaṃ; the ghāna parallel ^6-10-205 has "
        "«Saghānakānaṃ upapajjantānaṃ …»): as written.",
        "- ^6-10-213 … ^6-10-216 «Sabbesaṃ cavantānaṃ acittakānaṃ upapajjantānaṃ …» (manindriya): as written.",
        "- ^6-10-218 / ^6-10-219 / ^6-10-220 / ^6-10-221 «Sabbesaṃ cittassa bhaṅgakkhaṇe nirodhasamāpannānaṃ "
        "asaññasattānaṃ …» (no mind kind before the second group where manindriya is named): as written.",
        "",
    ]
    return "\n".join(out)


def main():
    S.check_reused()
    B.check_reused()
    A.check_reused()
    I.check_reused()
    I.check_frames()
    I2.check_reused()
    I2.check_frames()
    check_frames()
    segs = build(CH)
    check_termbase()
    S.write(CH, segs)
    text = (S.OUT_DIR / CH).read_text(encoding="utf-8")
    ADH_DIR.mkdir(parents=True, exist_ok=True)
    (ADH_DIR / CH).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", ADH_DIR / CH)
    NOTES_MD.write_text(unicodedata.normalize("NFC", notes()), encoding="utf-8", newline="\n")
    print("wrote", NOTES_MD)
    print("checked equal:", CHECKED, "; heads:", len(HEADS_SEEN), "; slips:", sorted(set(SLIPS_SEEN)))


if __name__ == "__main__":
    main()
