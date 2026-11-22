"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 10-08 (Indriyayamaka 8: uppādavāra, (4) paccuppannātītavāro, all six
sections, and the heading of (5) paccuppannānāgatavāro).

Setters (all imported READ-ONLY with importlib; every shared string comes from their functions):
  build_rails_10-04_vi  (I4)  split_mv_cut (member lists cut by …pe…), question11, the line translator (cross-check)
  build_rails_10-03_vi  (I3)  verb / split_mv (separate na), persons10, head_parts10, answer_head10, question10,
                              NOCA_RE, NEG_BOTH_RE, pv_sentence10, PERSON_WORDS
  build_rails_10-02_vi  (I2)  Indriya person words (IND_ATTRS, SEX / sex_vi, FEEL / feel_vi), ind_group, ind_persons,
                              faculty_mind_gen, PRON_FEM, heading, CUT_ANS_RE / pv_unit («Natthi…pe….»)
  build_rails_10-01_vi  (I)   INDRIYA members, ind_mulaka
  build_rails_9-01_vi   (DY)  PAVATTE, ALL_BEINGS, EXTRA_PERSON, moment_vi, CUT_AFTER_Q («…ti?…Pe….» = «… không?…»)
  build_rails_3-02_vi   (A2)  ay_group / ay_persons (attributes with planes, flat runs «A, B và C»), answer_head
  build_rails_3-01_vi   (A)   BQ_RE, question_vi, PLANES_AY      build_rails_2-01_vi (B): b_q, b_noca, b_both,
  place_head, being_run, plane_tok, join_and, SHORT              build_rails_7-01_vi (C): connectors
  build_rails_5-01_vi   (T5)  MIND_KIND['upapatti'] «tâm tái sinh» and head_vi (cross-check of the identical heads)
  (all reached through I4 / I3 / I2, i.e. the very module objects 10-04 … 10-02 use)

New here (named constants; later Indriya chapters import them):
  mind_gen12                    upapatticittassa «tâm tái sinh» (5-01 / termbase), else 10-02 faculty_mind_gen
  group12 / persons12           a group with an Indriya word (sex / feeling / IND_ATTRS) AND a plane: the plane goes
                                with the participle, the sex / feeling word after it (10-02 order):
                                "Kāmāvacarā cavantānaṃ na itthīnaṃ kāmāvacaraṃ upapajjantānaṃ" «những người đang chết
                                đi khỏi cõi dục lạc và những người đang tái sinh vào cõi dục lạc không làm người nữ»;
                                runs of plane-beings in such a head are joined flat as 3-02
  head_parts12 / answer_head12  10-03 head parts + person spans with planes (3-02 ay_persons) + the rebirth-mind moments
                                (5-01: «Ở chúng sinh trong cõi Tịnh Cư, vào khoảnh khắc sinh khởi của tâm tái sinh, …»)
  question12                    pair questions, whole or cut, with mixed tenses and separate na
                                ("…pe… manindriyaṃ na uppajjitthāti")
  SLIPS                         (Ghānandriyamūlakaṃ), cavantāna (termbase variant entries): rendered as meant
  pv_sentence12 / unit12 / line12 / tr_line / build
Every head that 10-03, 10-02, 3-02 or 5-01 can parse, every sentence 10-03 can parse, every question 10-04 / 3-01 can
parse and every line 10-04 can parse is asserted byte-identical. A line, unit or word the parsers cannot place raises
ValueError (no silent fallback). Importing writes nothing.

usage: python -I -X utf8 -B build_rails_10-08_vi.py   (probe: … build_rails_10-08_vi.py probe)
"""
import importlib
import re
import sys
import unicodedata

RAILS_DIR = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\rails"
if RAILS_DIR not in sys.path:
    sys.path.insert(0, RAILS_DIR)
import build_rails_sample_vi as S  # noqa: E402  (READ-ONLY)
I4 = importlib.import_module("build_rails_10-04_vi")   # READ-ONLY: cut member lists, line translator (setter)
I3 = I4.I3                                             # READ-ONLY: separate-na Indriya lines (setter)
I2 = I3.I2                                             # READ-ONLY: Indriya person heads (setter)
I, A, B, C, DY = I3.I, I3.A, I3.B, I3.C, I3.DY
A2, D8 = I2.A2, I2.D8
T5 = importlib.import_module("build_rails_5-01_vi")    # READ-ONLY: «tâm tái sinh» heads (cross-check)
assert T5.B is B and T5.C is C and T5.T9 is DY

cap = S.cap
lc = I2.lc
CH = "10-08-indriyayamaka.md"
N = "10-08"
NOTES_MD = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/notes-rails-{N}.md"
ADH_DIR = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/adh-{N}"
M_IND = I.INDRIYA
PLANES = A.PLANES_AY
CHECKED = {"10-04 line": 0, "10-03 sentence": 0, "10-03 head": 0, "10-02 head": 0, "3-02 head": 0, "5-01 head": 0,
           "10-03 persons": 0, "3-02 persons": 0, "3-01 question": 0, "10-04 question": 0, "3-02 group": 0}
HEADS_SEEN = {}
NEW_GROUPS = {}          # sex / feeling word + plane groups built here (Pāli → Vietnamese)
SLIPS_SEEN = []
SETTER_CLASH = {}        # heads on which 10-03's own cross-check (head_parts10 vs 10-02 / 3-02) fails: 3-02 followed

# ===============================================================================================================
# 1. Slips rendered as meant (both are termbase entries: Ghānandriyamūlakaṃ «phần dựa trên năng lực mũi»,
#    cavantāna «đang chết đi»)
# ===============================================================================================================
SLIPS = {
    "(Ghānandriyamūlakaṃ)": "(Ghānindriyamūlakaṃ)",           # ^6-10-336: «a» for «i»
    "asaññasattā cavantāna tesaṃ": "asaññasattā cavantānaṃ tesaṃ",   # ^6-10-361: final «ṃ» missing
}


# ===============================================================================================================
# 2. Kinds of mind: the rebirth mind (5-01 MIND_KIND['upapatti'] = termbase upapatticittassa «tâm tái sinh»)
# ===============================================================================================================
UPAPATTI_MIND = T5.MIND_KIND["upapatti"]


def mind_gen12(word):
    if lc(word) == "upapatticittassa":
        return UPAPATTI_MIND
    return I2.faculty_mind_gen(word)


# ===============================================================================================================
# 3. Person groups and heads
# ===============================================================================================================
def _plane(t):
    return B.plane_tok(lc(t), PLANES)


def group12(toks):
    """One person group (ends with its participle). With an Indriya word AND a plane: 10-02 ind_group with the plane
    after the participle (3-02 ay_group order) and the sex / feeling word after the plane (10-02 order)."""
    head = " ".join(toks)
    has_ind = any(lc(t) in I2.NEW_WORDS for t in toks)
    has_plane = any(_plane(t) for t in toks)
    if not (has_ind and has_plane):
        return I3.persons10(head)
    quant, pre, pre_keys, sex, feel, neg, vina, planes, part = None, [], [], None, None, False, False, [], None
    for t in toks:
        tl = I2.QUANT_FEM.get(lc(t), lc(t))
        pt = _plane(t)
        if part:
            raise ValueError(f"word after the participle in {head!r}")
        if tl == "na":
            if neg:
                raise ValueError(f"double na in {head!r}")
            neg = True
        elif tl == "vinā":
            vina = True
        elif tl in B.QUANT:
            if quant or pre or sex or feel or planes:
                raise ValueError(f"misplaced {t!r} in {head!r}")
            quant = tl
        elif tl in I2.PRE_ATTRS:
            if neg or vina or planes:
                raise ValueError(f"misplaced attribute {t!r} in {head!r}")
            pre.append(I2.PRE_ATTRS[tl])
            pre_keys.append(tl)
        elif tl in I2.SEX:
            if sex or vina:
                raise ValueError(f"misplaced {t!r} in {head!r}")
            sex, neg = I2.sex_vi(tl, neg), False
        elif tl in I2.FEEL:
            if feel or neg:
                raise ValueError(f"misplaced {t!r} in {head!r}")
            feel, vina = I2.feel_vi(tl, vina), False
        elif pt and pt[1] in ("acc", "abl"):
            if neg or vina:
                raise ValueError(f"na / vinā before a plane in {head!r}")
            planes.append(pt)
        elif tl in B.PARTICIPLES or tl in I2.PART_FEM:
            if neg or vina:
                raise ValueError(f"dangling na / vinā in {head!r}")
            part = I2.PART_FEM.get(tl, tl)
        else:
            raise ValueError(f"unknown word {t!r} in person group {head!r}")
    if not part or not planes:
        raise ValueError(f"group without participle / plane {head!r}")
    pv, case, prep = B.PARTICIPLES[part]
    if any(c != case for _, c in planes):
        raise ValueError(f"plane case does not fit {part!r} in {head!r}")
    keys = [k for k, _ in planes]
    base = I2.ind_group(quant, pre, part)                       # «những người … đang tái sinh»
    full = I2.ind_group(quant, pre, part, sex, feel)            # «… đang tái sinh không làm người nữ» (10-02)
    assert full.startswith(base), (head, base, full)
    with_plane = f"{base} {prep} {B.join_and(PLANES[k][0] for k in keys)}"
    if all(k in A.AY_ATTRS for k in pre_keys):                  # = 3-02 ay_group (attributes + planes)
        assert with_plane == A2.ay_group(quant, pre_keys, part, keys, PLANES), (head, with_plane)
        CHECKED["3-02 group"] += 1
    out = with_plane + full[len(base):]
    NEW_GROUPS[head] = out
    return out


def persons12(head):
    """Genitive person phrase → Vietnamese (no «Ở»). Groups end at their participle; genitive plane-beings are items
    of their own; a phrase that is only one run of plane-beings = 2-01 being_run; otherwise the items are joined once,
    flat («A, B và C», 3-02). Asserted equal to 10-03 persons10 / 3-02 ay_persons wherever they parse the phrase."""
    toks = head.split()
    items, cur = [], []
    for t in toks:
        pt = _plane(t)
        if pt and pt[1] == "gen" and not cur:
            if items and items[-1][0] == "run":
                items[-1][1].append(pt[0])
            else:
                items.append(("run", [pt[0]]))
            continue
        cur.append(t)
        if lc(t) in B.PARTICIPLES or lc(t) in I2.PART_FEM:
            items.append(("group", cur))
            cur = []
    if cur:
        raise ValueError(f"dangling words {cur!r} in {head!r}")
    if len(items) == 1 and items[0][0] == "run":
        out = B.being_run(items[0][1], None, PLANES)
    else:
        flat = []
        for it in items:
            if it[0] == "group":
                flat.append(group12(it[1]))
            else:
                flat += [PLANES[k][1] for k in it[1]]
        out = B.join_and(flat)
    for name, f in (("10-03 persons", lambda: I3.persons10(head)),
                    ("3-02 persons", lambda: A2.ay_persons(head, PLANES))):
        try:
            old = f()
        except (ValueError, KeyError):
            continue
        assert old == out, (name, head, old, out)
        CHECKED[name] += 1
    return out


def _span_tok(t):
    return lc(t) in I3.PERSON_WORDS or bool(_plane(t))


def head_parts12(head):
    """Answer head (before tesaṃ / tāsaṃ [tattha]) → parts joined «, » (9-01 / 10-03 shape): person runs «ở …»,
    pavatte «trong đời sống», <mind> <moment> «vào khoảnh khắc … của tâm …», bare Sabbesaṃ before a moment «tất cả
    chúng sinh», nirodhasamāpannānaṃ (9-01 EXTRA_PERSON), person spans with planes (persons12)."""
    toks = head.split()
    parts, run, i = [], [], 0

    def flush():
        if run:
            if len(run) > 1 and any(f" {C.AND} " in g for g in run):
                raise ValueError(f"«và» inside a group of a longer person run: {head!r}")
            parts.append(f"{C.AT} {B.join_and(run)}")
            run.clear()

    def before_moment(j):
        return j + 1 < len(toks) and lc(toks[j + 1]) in D8.MOMENT

    while i < len(toks):
        t, lt = toks[i], lc(toks[i])
        if before_moment(i):
            flush()
            parts.append(DY.moment_vi(toks[i + 1], mind_gen12(t)))
            i += 2
        elif lt == "pavatte":
            flush()
            parts.append(DY.PAVATTE)
            i += 1
        elif lt in DY.EXTRA_PERSON:
            run.append(DY.EXTRA_PERSON[lt])
            i += 1
        elif lt == "sabbesaṃ" and not (i + 1 < len(toks) and _span_tok(toks[i + 1])):
            run.append(DY.ALL_BEINGS)
            i += 1
        elif _span_tok(t):
            j = i + 1
            while j < len(toks) and _span_tok(toks[j]) and not before_moment(j) and lc(toks[j]) not in DY.EXTRA_PERSON:
                j += 1
            run.append(persons12(" ".join(toks[i:j])))
            i = j
        else:
            raise ValueError(f"unknown word {t!r} in answer head {head!r}")
    flush()
    if not parts:
        raise ValueError(f"empty answer head {head!r}")
    return parts


def answer_head12(head, loc):
    if loc == "tattha":
        return B.place_head(head, PLANES)
    out = cap(", ".join(head_parts12(head)))
    has_loc = any((pt := _plane(t)) and pt[1] == "loc" for t in head.split())
    for name, f in (("10-03 head", lambda: I3.answer_head10(head, loc)),
                    ("10-02 head", lambda: I2.ind_answer_head(head, loc)),
                    ("3-02 head", lambda: A2.answer_head(head, loc, PLANES)),
                    ("5-01 head", lambda: T5.head_vi(head.split()))):
        if name == "5-01 head" and has_loc:
            continue      # 5-01 reads a locative plane as a place «Ở cõi X, ở …»; 2-01 / 3-02 «… trong cõi X» (person)
        try:
            old = f()
        except (ValueError, KeyError):
            continue
        except AssertionError as e:       # 10-03's own check: its head_parts10 differs from 10-02 / 3-02 here
            SETTER_CLASH[head] = (name, str(e)[:300])
            continue
        assert old == out, (name, head, old, out)
        CHECKED[name] += 1
    HEADS_SEEN[head] = out
    return out


# ===============================================================================================================
# 4. Questions, sentences, units, lines
# ===============================================================================================================
NA_RE = re.compile(r"\bna (uppajj)")
CUT_AFTER_Q = "?" + DY.CUT_AFTER_Q       # "…ti?…Pe…." = «… không?…» (9-01)


def _cut_q(q, M):
    m = A.BQ_RE.fullmatch(q)
    if not m:
        raise ValueError(f"unknown cut question {q!r}")
    label, w1, vapana, w2, c1, then, c2 = m.groups()
    if label is None and w1[0] != w1[0].upper():
        raise ValueError(f"unlabelled lower-case question {q!r}")
    a, v1 = I4.split_mv_cut(c1, M)
    b, v2 = I4.split_mv_cut(c2, M)
    return B.b_q(label, lc(w1) + (w2 or ""), then, a, v1[0], b, v2[0], other=bool(vapana))


def question12(q, M=None):
    """(Ka) yassa [yattha] A [na] V tassa [tattha] B[…pe… C] [na] V(ti) (without «?») → 2-01 b_q. A whole question =
    10-03 question10; a cut one = 10-04 split_mv_cut in the same shell; its positive twin is asserted = 3-01's."""
    M = M or M_IND
    if "…" not in q:
        return I3.question10(q, M)
    out = _cut_q(q, M)
    pos_q = NA_RE.sub(r"\1", q)
    try:
        old = A.question_vi(pos_q, M)
    except (ValueError, KeyError):
        old = None
    if old is not None:
        assert _cut_q(pos_q, M) == old, (pos_q, old)
        CHECKED["3-01 question"] += 1
    try:
        old = I4.question11(q, M)
    except (ValueError, KeyError):
        old = None
    if old is not None:
        assert old == out, (q, old, out)
        CHECKED["10-04 question"] += 1
    return out


def pv_sentence12(s, M=None):
    """Family B answers (2-01 b_noca / b_both) with this chapter's heads and separate-na / mixed-tense verbs."""
    M = M or M_IND
    out = None
    if m := I3.NOCA_RE.fullmatch(s):
        head, loc, c1, c2 = m.groups()
        a, v1 = I3.split_mv(c1, M)
        b, v2 = I3.split_mv(c2, M)
        out = B.b_noca(answer_head12(head, loc), I2.PRON_FEM.get(loc, loc), a, v1, b, v2)
    elif m := I3.NEG_BOTH_RE.fullmatch(s):
        head, loc, c1, v1, c2, v2 = m.groups()
        out = B.b_both(answer_head12(head, loc), I2.PRON_FEM.get(loc, loc), M.subj(c1), I3.verb(v1), M.subj(c2),
                       I3.verb(v2))
    if out is None:
        return None
    try:
        old = I3.pv_sentence10(s, M)
    except (ValueError, KeyError):
        old = None
    except AssertionError as e:           # 10-03's internal head check fails (SETTER_CLASH)
        SETTER_CLASH.setdefault(s[:80], ("10-03 sentence", str(e)[:300]))
        old = None
    if old is not None:
        assert old == out, (s, old, out)
        CHECKED["10-03 sentence"] += 1
    return out


def unit12(u, M=None):
    M = M or M_IND
    if (lab := I.ind_mulaka(u, M)) is not None:
        return lab
    if u.endswith(CUT_AFTER_Q):
        return question12(u[:-len(CUT_AFTER_Q)], M) + S.PE
    if u.endswith("?"):
        return question12(u[:-1], M)
    if u in B.SHORT:
        return B.SHORT[u]
    if (m := I2.CUT_ANS_RE.fullmatch(u)) and m.group(1) + "." in B.SHORT:   # Natthi…pe…. «Không có…» (10-02)
        return I2.pv_unit(u, M)
    if "…" in u:
        raise ValueError(f"cut not set in this chapter: {u!r}")
    if (out := pv_sentence12(u, M)) is not None:
        return out
    raise ValueError(f"unknown unit {u!r}")


def line12(body, M=None):
    body, label = body.strip(), None
    if m := re.fullmatch(r"(.+?) (\(\w+mūlakaṃ\)\.?)", body):     # trailing (Xindriyamūlakaṃ) label (10-02)
        body, label = m.group(1), m.group(2)
    units = [x for x in re.split(r"(?<=[.?]) (?=\S)", body) if x]
    if label:
        units.append(label)
    return " ".join(unit12(x, M) for x in units)


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
        for bad, good in SLIPS.items():
            if bad in body:
                SLIPS_SEEN.append((bid, bad, good))
                body = body.replace(bad, good)
        out = line12(body, M)
    full = f"{out} {bid}" if bid else out
    try:
        old = I4.tr_line(p, M, fixed)
    except (ValueError, KeyError):
        old = None
    except AssertionError as e:           # 10-03's internal head check fails (SETTER_CLASH)
        SETTER_CLASH.setdefault(p[:80], ("10-04 line", str(e)[:300]))
        old = None
    if old is not None:
        assert old == full, ("10-04 line", p, old, full)
        CHECKED["10-04 line"] += 1
    return full


def build(name, M=None, fixed=None):
    return [[tr_line(ln, M, fixed) for ln in seg] for seg in S.segments_of(name)]


# ===============================================================================================================
# 5. Checks
# ===============================================================================================================
TERMBASE_USED = [   # pi-6 termbase entries used verbatim («Pāli: {…: Vietnamese}»)
    ("upapatticittassa", UPAPATTI_MIND),
    ("upapatticittassa uppādakkhaṇe", f"{D8.MOMENT['uppādakkhaṇe']} {D8.OF} {UPAPATTI_MIND}"),
    ("upapatticittassa bhaṅgakkhaṇe", f"{D8.MOMENT['bhaṅgakkhaṇe']} {D8.OF} {UPAPATTI_MIND}"),
    ("Ghānandriyamūlakaṃ", "phần dựa trên năng lực mũi"), ("cavantāna", B.PARTICIPLES["cavantānaṃ"][0]),
    ("Suddhāvāsaṃ", PLANES["suddhāvās"][0]), ("Suddhāvāse", PLANES["suddhāvās"][0]),
    ("Suddhāvāsānaṃ", PLANES["suddhāvās"][1]), ("Arūpānaṃ", PLANES["arūp"][1]),
    ("Kāmāvacarā", PLANES["kāmāvacar"][0]), ("kāmāvacaraṃ", PLANES["kāmāvacar"][0]),
    ("Rūpāvacarā", PLANES["rūpāvacar"][0]), ("Rūpāvacarānaṃ", PLANES["rūpāvacar"][1]),
    ("Pañcavokārā", PLANES["pañcavokār"][0]), ("Pañcavokāraṃ", PLANES["pañcavokār"][0]),
    ("parinibbantānaṃ", B.PARTICIPLES["parinibbantānaṃ"][0]), ("Itaresaṃ", "người khác"),
]


def check_termbase():
    tb = I2.termbase_text()
    bad = [(p, v) for p, v in TERMBASE_USED
           if not re.search(rf"^{re.escape(p)}: {{.*: {re.escape(v)}}}$", tb, re.M)]
    assert not bad, "termbase entries not matched: " + repr(bad)
    assert I.ind_mulaka("(Ghānindriyamūlakaṃ)", M_IND) == "(" + cap("phần dựa trên năng lực mũi") + ")"
    I3.check_termbase()


def check_frames():
    assert mind_gen12("cittassa") == D8.MIND and mind_gen12("upekkhāsampayuttacittassa") == I2.faculty_mind_gen(
        "upekkhāsampayuttacittassa")
    hd = "Suddhāvāsānaṃ upapatticittassa uppādakkhaṇe asaññasattaṃ upapajjantānaṃ"
    assert answer_head12(hd, "tesaṃ") == T5.head_vi(hd.split())
    hd = "Pañcavokārā cavantānaṃ acakkhukānaṃ kāmāvacaraṃ upapajjantānaṃ arūpānaṃ"
    assert answer_head12(hd, "tesaṃ") == A2.answer_head(hd, "tesaṃ", PLANES)
    hd = "Sabbesaṃ cittassa bhaṅgakkhaṇe somanassavippayuttacittassa uppādakkhaṇe nirodhasamāpannānaṃ asaññasattānaṃ"
    assert answer_head12(hd, "tesaṃ") == I3.answer_head10(hd, "tesaṃ")
    g = group12("na itthīnaṃ kāmāvacaraṃ upapajjantānaṃ".split())
    assert g == f"{B.PERSON} {B.PARTICIPLES['upapajjantānaṃ'][0]} vào {PLANES['kāmāvacar'][0]} " \
                f"{I2.sex_vi('itthīnaṃ', True)}", g
    assert CUT_AFTER_Q == "?…Pe…."
    assert I2.heading("(4) Paccuppannātītavāro").startswith("(4) ")


# ===============================================================================================================
# 6. Notes file (Pāli = tiếng Việt)
# ===============================================================================================================
def notes():
    M = M_IND
    out = []

    def row(p, v):
        out.append(f"{p} = {v}")

    def h(t):
        out.extend(["", f"## {t}", ""])

    out += [f"# pi-6 rails {N} (Indriyayamaka 8): (4) paccuppannātītavāro (present + past)", "",
            "Builder: build_rails_10-08_vi.py (import with importlib). Setters: build_rails_10-04_vi (split_mv_cut, "
            "question11, tr_line), build_rails_10-03_vi (verb / split_mv with a separate na, persons10, head_parts10, "
            "answer_head10, question10, NOCA_RE, NEG_BOTH_RE, pv_sentence10), build_rails_10-02_vi (ind_group, "
            "ind_persons, sex_vi, feel_vi, faculty_mind_gen, PRON_FEM, heading, the cut answer), 10-01 (INDRIYA, "
            "ind_mulaka), 9-01 (PAVATTE, ALL_BEINGS, EXTRA_PERSON, moment_vi, CUT_AFTER_Q), 3-02 (ay_group, ay_persons, "
            "answer_head), 3-01 (BQ_RE, question_vi, PLANES_AY), 2-01 (b_q, b_noca, b_both, place_head, being_run, "
            "VERB_TABLE, SHORT), 7-01, and 5-01 (MIND_KIND['upapatti'], head_vi); all READ-ONLY. Every head 10-03 / "
            "10-02 / 3-02 / 5-01 parse, every sentence 10-03 parses, every question 10-04 / 3-01 parse and every line "
            "10-04 parses is asserted byte-identical. Exposed: `SLIPS`, `UPAPATTI_MIND`, `mind_gen12`, `group12`, "
            "`persons12`, `head_parts12`, `answer_head12`, `CUT_AFTER_Q`, `question12`, `pv_sentence12`, `unit12`, "
            "`line12`, `tr_line`, `build`. Format: Pāli = tiếng Việt.", ""]
    h("Headings")
    for t in ("(4) Paccuppannātītavāro", "(Ka) anulomapuggalo", "(Kha) anulomaokāso", "(Ga) anulomapuggalokāsā",
              "(Gha) paccanīkapuggalo", "(Ṅa) paccanīkaokāso", "(Ca) paccanīkapuggalokāsā",
              "(5) Paccuppannānāgatavāro"):
        row(t, I2.heading(t))
    h("Verbs (2-01 VERB_TABLE, 9-01 separate na, 7-01 / coordinator after no ca)")
    for v in ("uppajjati", "uppajjittha", "na uppajjati", "na uppajjittha"):
        row(v, I3.verb(v)[0])
    row("no ca tesaṃ B uppajjittha", "nhưng ở những người ấy " + B.noca_vi("B", I3.verb("uppajjittha")))
    row("no ca tesaṃ B na uppajjittha", "nhưng ở những người ấy " + B.noca_vi("B", I3.verb("na uppajjittha")))
    row("Uppajjittha.", B.SHORT["Uppajjittha."])
    h("Questions (mixed tenses; cut member lists with a separate na: new here)")
    for q in ("(Ka) yassa cakkhundriyaṃ uppajjati tassa sotindriyaṃ uppajjitthāti",
              "(Kha) yassa vā pana sotindriyaṃ uppajjittha tassa cakkhundriyaṃ uppajjatīti",
              "Yassa cakkhundriyaṃ uppajjati tassa saddhindriyaṃ…pe… paññindriyaṃ…pe… manindriyaṃ uppajjitthāti",
              "Yassa cakkhundriyaṃ na uppajjati tassa itthindriyaṃ…pe… purisindriyaṃ na uppajjitthāti",
              "Yassa yattha cakkhundriyaṃ na uppajjati tassa tattha saddhindriyaṃ…pe… paññindriyaṃ…pe… manindriyaṃ "
              "na uppajjitthāti",
              "(Kha) yassa vā pana yattha sotindriyaṃ na uppajjittha tassa tattha cakkhundriyaṃ na uppajjatīti"):
        row(q + "?", question12(q, M))
    for u in ("Yattha cakkhundriyaṃ uppajjati tattha sotindriyaṃ uppajjitthāti?…Pe….", "Natthi…pe…."):
        row(u, unit12(u, M))
    h("Person heads with planes (3-02 shapes) and the rebirth mind (5-01)")
    for hd in ("Suddhāvāsaṃ upapajjantānaṃ", "Itaresaṃ sacakkhukānaṃ upapajjantānaṃ",
               "Pañcavokārā cavantānaṃ acakkhukānaṃ kāmāvacaraṃ upapajjantānaṃ arūpānaṃ",
               "Kāmāvacarā cavantānaṃ aghānakānaṃ kāmāvacaraṃ upapajjantānaṃ rūpāvacarānaṃ arūpāvacarānaṃ",
               "Suddhāvāse parinibbantānaṃ asaññasattānaṃ arūpānaṃ", "Rūpāvacarānaṃ arūpāvacarānaṃ",
               "Suddhāvāsānaṃ asaññasattānaṃ arūpānaṃ", "Suddhāvāsaṃ upapajjantānaṃ asaññasattaṃ upapajjantānaṃ",
               "Suddhāvāsānaṃ upapatticittassa uppādakkhaṇe asaññasattaṃ upapajjantānaṃ",
               "Suddhāvāsānaṃ upapatticittassa bhaṅgakkhaṇe asaññasattā cavantānaṃ",
               "Itaresaṃ catuvokāraṃ pañcavokāraṃ upapajjantānaṃ pavatte cittassa uppādakkhaṇe",
               "Catuvokārā pañcavokārā cavantānaṃ pavatte cittassa bhaṅgakkhaṇe",
               "Itaresaṃ upekkhāya upapajjantānaṃ pavatte upekkhāsampayuttacittassa uppādakkhaṇe",
               "Itaresaṃ ñāṇasampayuttānaṃ upapajjantānaṃ pavatte ñāṇasampayuttacittassa uppādakkhaṇe"):
        row(f"{hd} tesaṃ tattha …", f"{answer_head12(hd, 'tesaṃ tattha')}, {C.THEN} {B.L['tesaṃ tattha']} …")
    h("Sex word + plane in one group (new here; please confirm)")
    for hd in ("Kāmāvacarā cavantānaṃ na itthīnaṃ kāmāvacaraṃ upapajjantānaṃ",
               "Kāmāvacarā cavantānaṃ na itthīnaṃ kāmāvacaraṃ upapajjantānaṃ rūpāvacarānaṃ arūpāvacarānaṃ",
               "Kāmāvacarā cavantānaṃ na purisānaṃ kāmāvacaraṃ upapajjantānaṃ rūpāvacarānaṃ"):
        row(hd, persons12(hd))
    h("Sample lines")
    for s in ("Suddhāvāsaṃ upapajjantānaṃ tesaṃ tattha cakkhundriyaṃ uppajjati, no ca tesaṃ tattha sotindriyaṃ "
              "uppajjittha. Itaresaṃ sacakkhukānaṃ upapajjantānaṃ tesaṃ tattha cakkhundriyañca uppajjati sotindriyañca "
              "uppajjittha.",
              "Pañcavokārā cavantānaṃ acakkhukānaṃ kāmāvacaraṃ upapajjantānaṃ tesaṃ tattha cakkhundriyaṃ na uppajjati, "
              "no ca tesaṃ tattha sotindriyaṃ na uppajjittha. Suddhāvāse parinibbantānaṃ asaññasattānaṃ arūpānaṃ tesaṃ "
              "tattha cakkhundriyañca na uppajjati sotindriyañca na uppajjittha.",
              "Kāmāvacarā cavantānaṃ na itthīnaṃ kāmāvacaraṃ upapajjantānaṃ tesaṃ tattha purisindriyaṃ uppajjittha, no "
              "ca tesaṃ tattha itthindriyaṃ uppajjati. Itthīnaṃ upapajjantīnaṃ tāsaṃ tattha purisindriyañca uppajjittha "
              "itthindriyañca uppajjati."):
        row(s, line12(s, M))
    h("Termbase misfits and gaps (for the coordinator)")
    out += [
        "- Sex word + plane in one group (^6-10-347, ^6-10-348, ^6-10-359, ^6-10-360: «Kāmāvacarā cavantānaṃ na itthīnaṃ "
        "/ na purisānaṃ kāmāvacaraṃ upapajjantānaṃ …»): not set before; set here as the plane after the participle "
        "(3-02 «đang tái sinh vào cõi dục lạc») and the sex word after it (10-02 «… không làm người nữ»): «những người "
        "đang tái sinh vào cõi dục lạc không làm người nữ». The sex word belongs to the upapajjantānaṃ group, not to "
        "«Kāmāvacarā cavantānaṃ» (10-03 rule). Please confirm.",
        "- upapatticittassa uppādakkhaṇe / bhaṅgakkhaṇe: termbase «khoảnh khắc sinh khởi / tan rã của tâm tái sinh» "
        "(5-01 wording; heads asserted = 5-01 head_vi). Not in 10-02's faculty minds; added as mind_gen12.",
        "- No new member, verb or plane words: all from 10-01 … 10-04, 3-01 / 3-02, 2-01, 9-01, 5-01.",
        "- Indriya anantarā / katici bhave lines: none in this chapter (nothing to align with 10-05).",
        "",
        "## Pāli as written (reported)",
        "",
        "- ^6-10-336 «(Ghānandriyamūlakaṃ)» (for Ghānindriya-): termbase entry «phần dựa trên năng lực mũi»; rendered "
        "as meant «(Phần dựa trên năng lực mũi)».",
        "- ^6-10-361 «asaññasattā cavantāna» (first answer of the jīvita / somanassa (Ka) pair; the parallels have "
        "cavantānaṃ): termbase entry cavantāna «đang chết đi»; rendered as meant.",
        "- ^6-10-357 (Ka) cakkhundriya / somanassindriya: the last answer has «… cakkhundriyañca na uppajjati "
        "sotindriyañca na uppajjittha» (sotindriya for somanassindriya, as in the sota pair above): translated as "
        "written («năng lực tai»). Please review.",
        "- ^6-10-361 (Kha) somanassindriyaṃ na uppajjittha … jīvitindriyaṃ na uppajjati: the first answer has the tenses "
        "the other way round («… somanassindriyaṃ na uppajjati, no ca … jīvitindriyaṃ na uppajjittha»): translated as "
        "written. Please review.",
        "- ^6-10-345 (Ga) cakkhu / itthi-purisa cut question «Yassa yattha cakkhundriyaṃ uppajjati tassa tattha "
        "itthindriyaṃ…pe… purisindriyaṃ uppajjitthāti?» and other (Ga) / (Ca) cut questions: unlabelled among labelled "
        "ones, as written; questions without an answer keep their «?».",
        "- ^6-10-346, ^6-10-358: an answer, the next question (and at ^6-10-358 its answer and the label) stand on one "
        "line: kept on one line.",
        "- ^6-10-344 / ^6-10-356 «Yattha …ti?…Pe….» = «… không?…» (9-01); ^6-10-354 «Natthi…pe….» = «Không có…» (10-02).",
        "",
        "## Clashes between finished setters (listed for the coordinator)",
        "",
        "- A head that is only a run of plane-beings ('Suddhāvāsānaṃ asaññasattānaṃ [arūpānaṃ]', 'Rūpāvacarānaṃ "
        "arūpāvacarānaṃ', ^6-10-358 … ^6-10-360): 10-03 head_parts10 would give «chúng sinh trong cõi Tịnh Cư và chúng "
        "sinh Vô Tưởng»; 10-02 ind_persons / 3-02 ay_persons (2-01 being_run) give «chúng sinh trong cõi Tịnh Cư và cõi "
        "Vô Tưởng». Followed 10-02 / 3-02 (family setter; 3-02 has the identical Pāli). 10-03's own cross-check fails on "
        "these heads, so its parser is skipped there. The termbase adherence check lists these 3 as asaññasattānaṃ "
        "misses (the 2-01 position variant «cõi Vô Tưởng»).",
        "- 'Suddhāvāse parinibbantānaṃ …': 5-01 head_vi would read Suddhāvāse as a place («Ở cõi Tịnh Cư, ở những người "
        "đang nhập Niết-bàn trọn vẹn»); 2-01 / 2-02 / 3-02 / 3-04 / 3-05 have «những người đang nhập Niết-bàn trọn vẹn "
        "trong cõi Tịnh Cư» (followed; 5-01 never printed the other form).",
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
    I3.check_frames()
    I4.check_frames()
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
    print("checked equal:", CHECKED, "; heads:", len(HEADS_SEEN), "; new groups:", len(NEW_GROUPS),
          "; slips:", SLIPS_SEEN)


def probe(name=CH):
    for seg in S.segments_of(name):
        for ln in seg:
            try:
                print("OK  ", tr_line(ln))
            except Exception as e:  # noqa: BLE001
                print("FAIL", ln[:200], "\n    ", type(e).__name__, str(e)[:400])


if __name__ == "__main__":
    if sys.argv[1:] == ["probe"]:
        probe()
    else:
        main()
