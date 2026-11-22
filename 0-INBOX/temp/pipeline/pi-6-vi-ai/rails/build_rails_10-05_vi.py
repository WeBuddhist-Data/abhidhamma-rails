"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 10-05 (Indriyayamaka 5: uppādavāra, (2) Atītavāro all six
sections, (3) Anāgatavāro (Ka) anulomapuggalo).

Setters (all imported READ-ONLY with importlib; every shared string comes from their functions):
  build_rails_10-04_vi  (I4)  question11 (cut member lists, separate na), tr_line (asserted equal where it parses)
  build_rails_10-03_vi  (I3)  verb / split_mv (separate na), persons10, NEG_BOTH_RE, answer_head10
  build_rails_10-02_vi  (I2)  ind_persons, ind_answer_head, faculty_mind_gen, SEX, FEEL, PRON_FEM, NOCA_RE, heading,
                              pv_unit (the cut answer «Āmantā …pe….»)
  build_rails_10-01_vi  (I)   INDRIYA members, ind_mulaka
  build_rails_9-01_vi   (DY)  verb, moment_vi, PAVATTE, ORDINAL / WHILE / OCCURRING, ANANTARA, THIS_MIND,
                              EXTRA_PERSON, ALL_BEINGS, answer_head (asserted equal)
  build_rails_5-01_vi   (P5)  MIND_KIND['upapatti'] «tâm tái sinh», head_vi (asserted equal)
  build_rails_3-02_vi   (A2)  ay_persons (a head that is one run of plane-beings: «chúng sinh trong cõi X và cõi Y»)
  build_rails_3-01_vi   (A)   PLANES_AY, AY_ATTRS        build_rails_2-01_vi (B): b_q, b_noca, b_both, ye_clause,
  build_rails_2-02_vi   (D2)  AND / REL                   place_head, SHORT, YE, UPAPAJJITVA, YE_VERBS
  build_rails_7-01_vi   (C)   shell (pair_q, Q_REL, PRON), connectors       build_rails_8_vi (D8): MIND, PEOPLE, MOMENT

New here (named constants; 10-06, 10-07, 10-12 import them):
  ETENEVA / BHAVE / KATICI / DASSETVA / KATICI_BHAVE
        eteneva bhāvena «trong chính trạng thái ấy» (user), katici bhave dassetvā «sau khi trải qua một số kiếp sống»
        (bhava «kiếp sống», user)
  YE_NOUN / ye_clause12   Ye / Yā [purisā | itthiyo | sacakkhukā | saghānakā] [eteneva bhāvena] [katici bhave
        dassetvā] [<plane-acc>] [somanassena | upekkhāya] upapajjitvā parinibbāyissanti
        «Những người nam nào trong chính trạng thái ấy, sau khi trải qua một số kiếp sống, sau khi tái sinh có niềm
        vui đi kèm, sẽ nhập Niết-bàn trọn vẹn»; without eteneva = 2-01 ye_clause shape (asserted)
  ye_head12   "Ye … ye ca / yā ca …" «… và những người nam nào …»; "P ye ca …" «Ở P và những … nào …» (3-02 shape)
  PACCHIMA_MIND / pacchima_mind / ANANTARA_REL / anantara_group
        yassa cittassa anantarā <X>sampayuttapacchimacittaṃ uppajjissati (a person group):
        «những người mà tâm cuối cùng gắn liền với sự bình thản sẽ sinh khởi ngay sau tâm này» (9-01 «… ngay sau
        tâm này»; user: smooth, not «Vào tâm mà ngay sau đó …»)
  plane_being_part   "Suddhāvāsānaṃ upapajjantānaṃ" (plane-being + participle) «chúng sinh trong cõi Tịnh Cư đang tái sinh»
  mind_gen12 / head_parts12 / answer_head12   heads (9-01 shape), asserted equal to 9-01 / 10-02 / 10-03 / 5-01
        wherever those parse them (a head with a plane-being + participle group differs on purpose: listed)
  question12 / pv_sentence12 / unit12 / line12 / tr_line / build
A line, unit or word the parsers cannot place raises ValueError (no silent fallback). Importing writes nothing.

usage: python -I -X utf8 -B build_rails_10-05_vi.py   (probe: … build_rails_10-05_vi.py probe)
"""
import importlib
import re
import sys
import unicodedata

RAILS_DIR = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\rails"
if RAILS_DIR not in sys.path:
    sys.path.insert(0, RAILS_DIR)
import build_rails_sample_vi as S  # noqa: E402  (READ-ONLY)
I4 = importlib.import_module("build_rails_10-04_vi")   # READ-ONLY: Indriya lines with separate na, cut lists
I3, I2, I, A, B, C, DY = I4.I3, I4.I2, I4.I, I4.A, I4.B, I4.C, I4.DY   # the very module objects 10-04 uses
A2, D8 = I2.A2, I2.D8
D2 = A2.D                                               # build_rails_2-02_vi (AND, REL, YE_CA)
P5 = importlib.import_module("build_rails_5-01_vi")    # READ-ONLY: «tâm tái sinh», head_vi
S6 = importlib.import_module("build_rails_6-01_vi")    # READ-ONLY: the smooth anantarā group (anantara_group)
A3 = importlib.import_module("build_rails_3-03_vi")    # READ-ONLY: "P ye ca …" joined flat (flat_persons)
assert DY.D is D8 and I3.DY is DY and S6.DY is DY and A3.A2 is A2

cap = S.cap
lc = I2.lc
CH = "10-05-indriyayamaka.md"
N = "10-05"
NOTES_MD = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/notes-rails-{N}.md"
ADH_DIR = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/adh-{N}"
APPROVED = S.ROOT / "0-INBOX/temp/pipeline/pi-6-vi-ai/termbase/APPROVED.md"
M_IND = I.INDRIYA
PLANES = A.PLANES_AY
CHECKED = {"10-04 line": 0, "9-01 head": 0, "10-02 head": 0, "10-03 head": 0, "5-01 head": 0, "2-01 ye": 0,
           "3-03 ye ca": 0, "6-01 anantarā": 0, "6-01 head": 0}
HEADS_SEEN = {}        # Pāli head -> Vietnamese
OWN_READING = set()    # heads that differ on purpose from a setter's parse (plane-being + participle)
CLASH_10_03 = set()    # heads where 10-03's answer_head10 disagrees with 10-02 / 3-02 (10-02 / 3-02 followed)
SLIPS_SEEN = []

# ===============================================================================================================
# 1. Ye-clauses with eteneva bhāvena / katici bhave dassetvā (new) and with nominative subjects
# ===============================================================================================================
ETENEVA = "trong chính trạng thái ấy"         # eteneva bhāvena (user decision 2026-11-22)
BHAVE = "kiếp sống"                           # bhava (user: «kiếp sống», kept apart from kappa «kiếp»)
KATICI = "một số"                             # katici (no entry; «một số» = a few, some)
DASSETVA = "sau khi trải qua"                 # dassetvā (no entry; commentary: katici paṭisandhiyo gahetvā)
KATICI_BHAVE = f"{DASSETVA} {KATICI} {BHAVE}"  # katici bhave dassetvā «sau khi trải qua một số kiếp sống»
YE_REL = ("Ye", "Yā")                         # Yā itthiyo (feminine) = Ye «Những … nào»
YE_CA_RE = re.compile(r" (?:ye|yā) ca ")
YE_NOUN = {   # nominative subject of a Ye-clause → «Những <noun> nào»
    "purisā": I2.SEX["purisānaṃ"],                         # termbase purisā «người nam»
    "itthiyo": I2.SEX["itthīnaṃ"],                         # termbase itthiyo «người nữ»
    "sacakkhukā": f"người {A.AY_ATTRS['sacakkhukānaṃ']}",  # termbase sacakkhukā «có mắt»
    "saghānakā": f"người {A.AY_ATTRS['saghānakānaṃ']}",    # no entry: sibling Saghānakānaṃ «có mũi» (3-01)
}
YE_PERSON = "người"                           # B.YE = «Những người nào»
assert B.YE == f"Những {YE_PERSON} {D2.REL}"
ABS_JOIN = ", "                               # absolutives after eteneva bhāvena are set off by commas


def ye_clause12(text):
    """Ye / Yā … parinibbāyissanti → «Những <noun> nào …». Without eteneva / noun / feeling = 2-01 ye_clause."""
    toks = text.split()
    if toks[0] not in YE_REL:
        raise ValueError(f"not a Ye-clause {text!r}")
    i, noun = 1, None
    if i < len(toks) and toks[i] in YE_NOUN:
        noun = toks[i]
        i += 1
    eteneva, absol, pl, feel, verb_vi = False, [], [], None, None
    while i < len(toks):
        t = toks[i]
        if toks[i:i + 2] == ["eteneva", "bhāvena"]:
            if eteneva or absol or pl or feel:
                raise ValueError(f"misplaced eteneva bhāvena in {text!r}")
            eteneva = True
            i += 2
            continue
        if toks[i:i + 3] == ["katici", "bhave", "dassetvā"]:
            if pl or feel:
                raise ValueError(f"dangling words before katici in {text!r}")
            absol.append(KATICI_BHAVE)
            i += 3
            continue
        pt = B.plane_tok(t, PLANES)
        if pt and pt[1] == "acc":
            if feel:
                raise ValueError(f"plane after a feeling word in {text!r}")
            pl.append(pt[0])
        elif t in I2.FEEL:
            if feel:
                raise ValueError(f"two feeling words in {text!r}")
            feel = I2.feel_vi(t)
        elif t == "upapajjitvā":
            phrase = B.UPAPAJJITVA
            if pl:
                phrase += f" vào {B.join_and(PLANES[k][0] for k in pl)}"
            if feel:
                phrase += f" {feel}"
            absol.append(phrase)
            pl, feel = [], None
        elif t in B.YE_VERBS:
            if verb_vi or i != len(toks) - 1:
                raise ValueError(f"verb not at the end of {text!r}")
            verb_vi = B.YE_VERBS[t]
        else:
            raise ValueError(f"unknown word {t!r} in Ye-clause {text!r}")
        i += 1
    if pl or feel or not verb_vi:
        raise ValueError(f"incomplete Ye-clause {text!r}")
    subj = f"Những {YE_NOUN[noun] if noun else YE_PERSON} {D2.REL}"
    if eteneva:
        out = f"{subj} {ETENEVA}{ABS_JOIN}" + ABS_JOIN.join(absol) + f"{ABS_JOIN}{verb_vi}"
    else:
        out = " ".join([subj] + absol + [verb_vi])
    if not noun and not eteneva and "có " not in out and toks[0] == "Ye":
        assert out == B.ye_clause(text, PLANES), (text, out)
        CHECKED["2-01 ye"] += 1
    return out


def ye_head12(head):
    """'Ye … [ye ca / yā ca …]' «A và b»; 'P ye ca …' «Ở P và những … nào …» (3-02 ye_ca_head shape)."""
    parts = YE_CA_RE.split(head)
    clauses = [ye_clause12(("Yā " if m.group(0).strip().startswith("yā") else "Ye ") + p)
               for m, p in zip(YE_CA_RE.finditer(head), parts[1:])]
    if head.split()[0] in YE_REL:
        first = ye_clause12(parts[0])
        return f" {D2.AND} ".join([first] + [lc(c) for c in clauses])
    try:                                               # 3-03: groups before "ye ca" and the clauses, one flat list
        flat = A3.flat_persons(parts[0], PLANES)
    except ValueError:
        flat = [persons12(parts[0])]
        if f" {C.AND} " in flat[0]:
            raise ValueError(f"«và» inside the persons before 'ye ca': {head!r}")
    out = f"{B.AT} {B.join_and(flat + [lc(c) for c in clauses])}"
    # 3-03's ye_ca_head asserts itself equal to 3-02's where the left part is one group (3-03's flat rule otherwise)
    for name, f in (("3-03 ye ca", lambda: A3.ye_ca_head(head, PLANES)),):
        try:
            old = f()
        except (ValueError, KeyError):
            continue
        assert old == out, (name, head, old, out)
        CHECKED[name] += 1
    return out


def is_ye_head(head):
    return head.split()[0] in YE_REL or bool(YE_CA_RE.search(head))


# ===============================================================================================================
# 2. yassa cittassa anantarā <X>pacchimacittaṃ uppajjissati (a person group; new smooth shape)
# ===============================================================================================================
PACCHIMA_MIND = "tâm cuối cùng"               # pacchimacittaṃ (termbase; 8 «tâm cuối cùng»)
PACCHIMA_RE = re.compile(r"(somanassa|upekkhā)sampayuttapacchimacittaṃ")
ANANTARA_REL = "mà"                           # «những người mà <mind> <verb> ngay sau tâm này»
ANANTARA_WORDS = ["yassa", "cittassa", "anantarā"]


def pacchima_mind(word):
    """upekkhāsampayuttapacchimacittaṃ «tâm cuối cùng gắn liền với sự bình thản» (termbase)."""
    m = PACCHIMA_RE.fullmatch(lc(word))
    if not m:
        raise ValueError(f"unknown final mind {word!r}")
    return f"{PACCHIMA_MIND} {I2.SAMPAYUTTA} {I2.FAC_MIND[m.group(1)]}"


def anantara_group(mind_word, verb_word):
    """«những người mà tâm cuối cùng gắn liền với … sẽ sinh khởi ngay sau tâm này» = 6-01 anantara_group with the
    kind of final mind filled in (asserted); 9-01 PERSON_ATTAIN ending «… ngay sau tâm này»."""
    out = f"{D8.PEOPLE} {ANANTARA_REL} {pacchima_mind(mind_word)} {DY.verb(verb_word)[0]} {DY.ANANTARA} {DY.THIS_MIND}"
    if lc(verb_word) == "uppajjissati":
        s6 = S6.anantara_group(None, False)
        assert s6.count(S6.FINAL_MIND) == 1 and s6.replace(S6.FINAL_MIND, pacchima_mind(mind_word)) == out, (s6, out)
        CHECKED["6-01 anantarā"] += 1
    return out


assert DY.PERSON_ATTAIN.endswith(f" {DY.ANANTARA} {DY.THIS_MIND}") and S6.FINAL_MIND == PACCHIMA_MIND


# ===============================================================================================================
# 3. Answer heads (9-01 shape: parts joined «, »; one «ở» per run of persons)
# ===============================================================================================================
def plane_being_part(plane_tok, part):
    """'Suddhāvāsānaṃ upapajjantānaṃ' «chúng sinh trong cõi Tịnh Cư đang tái sinh» (plane-being + participle)."""
    pt = B.plane_tok(plane_tok, PLANES)
    if not pt or pt[1] != "gen" or lc(part) not in B.PARTICIPLES:
        raise ValueError(f"not a plane-being + participle {plane_tok!r} {part!r}")
    return f"{PLANES[pt[0]][1]} {B.PARTICIPLES[lc(part)][0]}"


def mind_gen12(word):
    """upapatticittassa «tâm tái sinh» (5-01, termbase); else 10-02 faculty_mind_gen."""
    if lc(word) == "upapatticittassa":
        return P5.MIND_KIND["upapatti"]
    return I2.faculty_mind_gen(word)


def persons12(phrase):
    """Person phrase → Vietnamese (no «Ở»): groups ending in a participle = 10-03 persons10; plane-beings /
    Itaresaṃ without a participle = 10-02 ind_persons (3-02 ay_persons: one run «chúng sinh trong cõi X và cõi Y»)."""
    if any(lc(t) in B.PARTICIPLES or lc(t) in I2.PART_FEM or lc(t) in I3.PART_READING for t in phrase.split()):
        return I3.persons10(phrase)
    return I2.ind_persons(phrase)


def head_parts12(head):
    toks = head.split()
    low = [lc(t) for t in toks]
    parts, run, buf = [], [], []
    special = False

    def flush_buf():
        if buf:
            run.append(persons12(" ".join(buf)))
            buf.clear()

    def flush():
        flush_buf()
        if run:
            if len(run) > 1 and any(f" {C.AND} " in g for g in run):
                raise ValueError(f"«và» inside a group of a longer person run: {head!r}")
            parts.append(f"{C.AT} {B.join_and(run)}")
            run.clear()

    i = 0
    while i < len(toks):
        if low[i:i + 3] == ANANTARA_WORDS:
            if i + 4 >= len(toks):
                raise ValueError(f"short anantarā phrase in {head!r}")
            flush_buf()
            run.append(anantara_group(toks[i + 3], toks[i + 4]))
            i += 5
            continue
        pt = B.plane_tok(low[i], PLANES)
        if pt and pt[1] == "gen" and i + 1 < len(toks) and low[i + 1] in B.PARTICIPLES:
            flush_buf()
            run.append(plane_being_part(toks[i], toks[i + 1]))
            special = True
            i += 2
            continue
        if i + 1 < len(toks) and low[i + 1] in D8.MOMENT:
            flush()
            parts.append(DY.moment_vi(toks[i + 1], mind_gen12(toks[i])))
            i += 2
            continue
        if low[i] == "pavatte":
            flush()
            parts.append(DY.PAVATTE)
            i += 1
            continue
        if low[i] in DY.ORDINAL:
            if toks[i + 1:i + 3] != ["citte", "vattamāne"]:
                raise ValueError(f"unknown time phrase in {head!r}")
            flush()
            parts.append(f"{DY.WHILE} {D8.MIND} {DY.ORDINAL[low[i]]} {DY.OCCURRING}")
            i += 3
            continue
        if low[i] in DY.EXTRA_PERSON:
            flush_buf()
            run.append(DY.EXTRA_PERSON[low[i]])
            i += 1
            continue
        buf.append(toks[i])
        i += 1
    flush()
    if not parts:
        raise ValueError(f"empty answer head {head!r}")
    return parts, special


def answer_head12(head, loc):
    if loc == "tattha":
        return B.place_head(head, PLANES)
    if is_ye_head(head):
        out = ye_head12(head)
        old = None
        if head.split()[0] in YE_REL:          # "P ye ca …" heads are checked against 3-03 in ye_head12
            try:
                old = I2.ind_answer_head(head, loc)
            except (ValueError, KeyError, AssertionError):
                old = None
        if old is not None:
            assert old == out, ("10-02 head", head, old, out)
            CHECKED["10-02 head"] += 1
        HEADS_SEEN[head] = out
        return out
    parts, special = head_parts12(head)
    out = cap(", ".join(parts))
    checks = (("9-01 head", lambda: DY.answer_head(head, loc)),
              ("10-02 head", lambda: I2.ind_answer_head(head, loc)),
              ("10-03 head", lambda: I3.answer_head10(head, loc)),
              ("5-01 head", lambda: P5.head_vi(head.split())),
              ("6-01 head", lambda: S6.answer_head(head)))
    for name, f in checks:
        try:
            old = f()
        except (ValueError, KeyError):
            continue
        except AssertionError:
            if name == "10-03 head":          # 10-03 head_parts10 vs 10-02 on a run of plane-beings
                CLASH_10_03.add(head)
                continue
            raise
        if special:
            if old != out:
                OWN_READING.add((head, name, old))
            continue
        assert old == out, (name, head, old, out)
        CHECKED[name] += 1
    HEADS_SEEN[head] = out
    return out


# ===============================================================================================================
# 4. Questions, sentences, units, lines
# ===============================================================================================================
SLIPS = {   # Pāli as printed → as parsed (reported in the notes); count = expected occurrences
    "jīvitindriyaṃ … somanassindriyaṃ": ("jīvitindriyaṃ… somanassindriyaṃ", 1),    # space before the cut
    "manindriyaṃ ca uppajjittha": ("manindriyañca uppajjittha", 1),                  # for manindriyañca
}
MISMATCH_Q = re.compile(r"(Yassa)( vā pana)? (\S+ \S+) (tattha) (\S+ \S+)")   # yassa … tattha (as written)


def question12(q, M=None):
    """10-04 question11; a question whose correlative does not fit its relative (yassa … tattha) is translated as
    written: the shell with «thì ở nơi ấy» (reported)."""
    M = M or M_IND
    m = MISMATCH_Q.fullmatch(q)
    if m:
        a, v1 = I3.split_mv(m.group(3), M)
        b, v2 = I3.split_mv(m.group(5), M)
        s = C.pair_q("yassa", f"{a} {v1[0]}", f"{b} {v2[0]}", None, bool(m.group(2)))
        that = f"{C.THEN} {C.AT} {C.Q_REL['yassa'][1]} "
        assert s.count(that) == 1, s
        SLIPS_SEEN.append(("yassa … tattha", q))
        return s.replace(that, f"{C.THEN} {C.AT} {C.PRON['tattha']} ")
    return I4.question11(q, M)


def pv_sentence12(s, M=None):
    """Family B answers (2-01 b_noca / b_both) with answer_head12 and separate-na verbs (10-03)."""
    M = M or M_IND
    if m := I2.NOCA_RE.fullmatch(s):
        head, loc, c1, c2 = m.groups()
        a, v1 = I3.split_mv(c1, M)
        b, v2 = I3.split_mv(c2, M)
        return B.b_noca(answer_head12(head, loc), I2.PRON_FEM.get(loc, loc), a, v1, b, v2)
    if m := I3.NEG_BOTH_RE.fullmatch(s):
        head, loc, c1, v1, c2, v2 = m.groups()
        return B.b_both(answer_head12(head, loc), I2.PRON_FEM.get(loc, loc), M.subj(c1), I3.verb(v1), M.subj(c2),
                        I3.verb(v2))
    return None


def unit12(u, M=None):
    M = M or M_IND
    if (lab := I.ind_mulaka(u, M)) is not None:
        return lab
    if u.endswith("?"):
        return question12(u[:-1], M)
    if u in B.SHORT:
        return B.SHORT[u]
    if (m := I2.CUT_ANS_RE.fullmatch(u)) and m.group(1) + "." in B.SHORT:   # Āmantā …pe…. «Đúng vậy …» (10-02)
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
        for bad, (good, _) in SLIPS.items():
            if bad in body:
                SLIPS_SEEN.append((bid, bad, good))
                body = body.replace(bad, good)
        out = line12(body, M)
    full = f"{out} {bid}" if bid else out
    try:
        old = I4.tr_line(p, M, fixed)
    except (ValueError, KeyError, AssertionError):
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
    ("upekkhāsampayuttapacchimacittaṃ", pacchima_mind("upekkhāsampayuttapacchimacittaṃ")),
    ("somanassasampayuttapacchimacittaṃ", pacchima_mind("somanassasampayuttapacchimacittaṃ")),
    ("pacchimacittaṃ", PACCHIMA_MIND), ("anantarā", DY.ANANTARA), ("purisā", YE_NOUN["purisā"]),
    ("itthiyo", YE_NOUN["itthiyo"]), ("sacakkhukā", A.AY_ATTRS["sacakkhukānaṃ"]), ("upapajjitvā", B.UPAPAJJITVA),
    ("parinibbāyissanti", B.YE_VERBS["parinibbāyissanti"]), ("upapatticittassa", P5.MIND_KIND["upapatti"]),
    ("upapatticittassa uppādakkhaṇe", f"{D8.MOMENT['uppādakkhaṇe']} {D8.OF} {P5.MIND_KIND['upapatti']}"),
    ("upekkhāya", I2.FEEL["upekkhāya"]), ("somanassena", I2.FEEL["somanassena"]), ("Itaresaṃ", "người khác"),
]
USER_DECISIONS = ["eteneva bhāvena «trong chính trạng thái ấy»", "bhava «kiếp sống»"]


def check_termbase():
    tb = I2.termbase_text()
    bad = [(p, v) for p, v in TERMBASE_USED
           if not re.search(rf"^{re.escape(p)}: {{.*: {re.escape(v)}}}$", tb, re.M)]
    assert not bad, "termbase entries not matched: " + repr(bad)
    ap = unicodedata.normalize("NFC", APPROVED.read_text(encoding="utf-8"))
    assert all(d in ap for d in USER_DECISIONS), "user decisions not found in APPROVED.md"
    assert f"«{ETENEVA}»" in USER_DECISIONS[0] and f"«{BHAVE}»" in USER_DECISIONS[1]
    I2.check_termbase()


def check_frames():
    assert ye_clause12("Ye rūpāvacaraṃ upapajjitvā parinibbāyissanti") == B.ye_clause(
        "Ye rūpāvacaraṃ upapajjitvā parinibbāyissanti", PLANES)
    assert answer_head12("Ye arūpaṃ upapajjitvā parinibbāyissanti", "tesaṃ") == A2.answer_head(
        "Ye arūpaṃ upapajjitvā parinibbāyissanti", "tesaṃ", PLANES)
    for hd in ("Rūpāvacarānaṃ arūpāvacarānaṃ", "Suddhāvāsānaṃ asaññasattānaṃ arūpānaṃ", "Catuvokārānaṃ pañcavokārānaṃ"):
        assert answer_head12(hd, "tesaṃ tattha") == I2.ind_answer_head(hd, "tesaṃ tattha") == \
            f"{B.AT} {A2.ay_persons(hd, PLANES)}", hd
    hd = "Suddhāvāsānaṃ dutiye citte vattamāne asaññasattānaṃ"
    assert answer_head12(hd, "tesaṃ tattha") == DY.answer_head(hd, "tesaṃ tattha")
    hd = "Suddhāvāsānaṃ upapatticittassa uppādakkhaṇe"
    assert answer_head12(hd, "tesaṃ tattha") == P5.head_vi(hd.split())
    for hd in ("Pacchimabhavikānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti",
               "Kāmāvacare parinibbantānaṃ rūpāvacare arūpāvacare pacchimabhavikānaṃ ye ca arūpaṃ upapajjitvā "
               "parinibbāyissanti"):
        assert answer_head12(hd, "tesaṃ") == A3.ye_ca_head(hd, PLANES), hd
    assert I2.PRON_FEM["tāsaṃ"] == "tesaṃ"
    assert S.LABEL["Ga"] == "(c)" and S.LABEL["Gha"] == "(d)"


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

    out += [f"# pi-6 rails {N} (Indriyayamaka 5): (2) Atītavāro, (3) Anāgatavāro (Ka) anulomapuggalo", "",
            "Builder: build_rails_10-05_vi.py (import with importlib). Setters: build_rails_10-04_vi (question11, "
            "tr_line), 10-03 (verb / split_mv, persons10, NEG_BOTH_RE), 10-02 (ind_persons, ind_answer_head, SEX, FEEL, "
            "faculty_mind_gen, PRON_FEM, NOCA_RE, heading, pv_unit), 10-01 (INDRIYA, ind_mulaka), 9-01 (verb, "
            "moment_vi, PAVATTE, ORDINAL, ANANTARA, THIS_MIND, EXTRA_PERSON), 5-01 (MIND_KIND['upapatti'], head_vi), "
            "3-02 (ay_persons, ye_ca_head), 3-01 (PLANES_AY, AY_ATTRS), 2-02 (AND, REL), 2-01 (b_q, b_noca, b_both, "
            "ye_clause, place_head, SHORT), 7-01 (pair_q), 8 (MIND, PEOPLE, MOMENT); all READ-ONLY. Every line 10-04 "
            "parses is asserted byte-identical; every head 9-01 / 10-02 / 10-03 / 5-01 parse, likewise (exceptions "
            "listed below). Exposed for 10-06, 10-07, 10-12: `ETENEVA`, `BHAVE`, `KATICI`, `DASSETVA`, "
            "`KATICI_BHAVE`, `YE_REL`, `YE_CA_RE`, `YE_NOUN`, `YE_PERSON`, `ABS_JOIN`, `ye_clause12`, `ye_head12`, "
            "`is_ye_head`, `PACCHIMA_MIND`, `PACCHIMA_RE`, `ANANTARA_REL`, `pacchima_mind`, `anantara_group`, "
            "`plane_being_part`, `mind_gen12`, `head_parts12`, `answer_head12`, `question12`, `pv_sentence12`, "
            "`unit12`, `line12`, `tr_line`, `build`. Format: Pāli = tiếng Việt.", ""]
    h("Headings")
    for t in ("(2) Atītavāro", "(3) Anāgatavāro", "(Ka) anulomapuggalo", "(Ga) anulomapuggalokāsā",
              "(Ca) paccanīkapuggalokāsā"):
        row(t, I2.heading(t))
    h("New: eteneva bhāvena / katici bhave dassetvā (Ye-clauses; user: eteneva bhāvena, bhava)")
    row("eteneva bhāvena", ETENEVA)
    row("katici bhave dassetvā", KATICI_BHAVE)
    row("katici / bhave / dassetvā", f"{KATICI} / {BHAVE} / {DASSETVA}")
    for hd in ("Ye purisā eteneva bhāvena katici bhave dassetvā parinibbāyissanti",
               "Yā itthiyo eteneva bhāvena katici bhave dassetvā parinibbāyissanti",
               "Yā itthiyo eteneva bhāvena katici bhave dassetvā upekkhāya upapajjitvā parinibbāyissanti",
               "Ye purisā eteneva bhāvena katici bhave dassetvā somanassena upapajjitvā parinibbāyissanti",
               "Ye sacakkhukā upekkhāya upapajjitvā parinibbāyissanti",
               "Ye saghānakā somanassena upapajjitvā parinibbāyissanti",
               "Ye rūpāvacaraṃ upapajjitvā parinibbāyissanti ye ca purisā eteneva bhāvena katici bhave dassetvā "
               "parinibbāyissanti",
               "Ye rūpāvacaraṃ arūpāvacaraṃ upapajjitvā parinibbāyissanti yā ca itthiyo eteneva bhāvena katici bhave "
               "dassetvā upekkhāya upapajjitvā parinibbāyissanti"):
        row(f"{hd} tesaṃ …", f"{answer_head12(hd, 'tesaṃ')}, {C.THEN} {B.L['tesaṃ']} …")
    out.append("(For 10-06 / 10-07 / 10-12: «P ye ca purisā …» = 3-02 / 3-03 «Ở P và những người nam nào …»; several "
               "groups and clauses form one flat list «Ở A, B và …» (3-03 flat_persons):)")
    for hd in ("Rūpāvacarānaṃ ye ca purisā eteneva bhāvena katici bhave dassetvā parinibbāyissanti",
               "Pacchimabhavikānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti yā ca itthiyo eteneva bhāvena katici "
               "bhave dassetvā parinibbāyissanti"):
        row(f"{hd} tesaṃ …", f"{answer_head12(hd, 'tesaṃ')}, {C.THEN} {B.L['tesaṃ']} …")
    h("New: anantarā heads (person group; user: smooth, meaning unchanged)")
    for w in ("upekkhāsampayuttapacchimacittaṃ", "somanassasampayuttapacchimacittaṃ"):
        hd = f"Yassa cittassa anantarā {w} uppajjissati"
        row(f"{hd} tesaṃ …", f"{answer_head12(hd, 'tesaṃ')}, {C.THEN} {B.L['tesaṃ']} …")
    hd = "Yassa cittassa anantarā somanassasampayuttapacchimacittaṃ uppajjissati asaññasattānaṃ"
    row(f"{hd} tesaṃ … (10-06 / 10-07)", f"{answer_head12(hd, 'tesaṃ')}, {C.THEN} {B.L['tesaṃ']} …")
    hd = "Pacchimacittasamaṅgīnaṃ yassa cittassa anantarā upekkhāsampayuttapacchimacittaṃ uppajjissati"
    row(f"{hd} tesaṃ … (10-12)", f"{answer_head12(hd, 'tesaṃ')}, {C.THEN} {B.L['tesaṃ']} …")
    h("Heads new in the Indriya chapters (9-01 / 5-01 / 3-02 strings)")
    for hd in ("Suddhāvāsānaṃ dutiye citte vattamāne asaññasattānaṃ", "Itaresaṃ catuvokārānaṃ pañcavokārānaṃ",
               "Suddhāvāsānaṃ upapatticittassa uppādakkhaṇe", "Suddhāvāsānaṃ upapajjantānaṃ asaññasattānaṃ",
               "Rūpāvacarānaṃ arūpāvacarānaṃ", "Suddhāvāsānaṃ asaññasattānaṃ arūpānaṃ", "Itaresaṃ"):
        row(f"{hd} tesaṃ tattha …", f"{answer_head12(hd, 'tesaṃ tattha')}, {C.THEN} {B.L['tesaṃ tattha']} …")
    h("Sample lines")
    for s in ("(Ka) yassa cakkhundriyaṃ uppajjittha tassa sotindriyaṃ uppajjitthāti? Āmantā.",
              "Rūpāvacare tattha cakkhundriyaṃ uppajjittha, no ca tattha ghānindriyaṃ uppajjittha.",
              "Asaññasatte arūpe tattha jīvitindriyaṃ uppajjittha, no ca tattha cakkhundriyaṃ uppajjittha.",
              "Rūpāvacare tattha ghānindriyaṃ na uppajjittha, no ca tattha cakkhundriyaṃ na uppajjittha.",
              "Asaññasatte tattha cakkhundriyañca na uppajjittha upekkhindriyañca na uppajjittha.",
              "(Ka) yattha cakkhundriyaṃ na uppajjittha tattha jīvitindriyaṃ na uppajjitthāti? Uppajjittha.",
              "Yassa cittassa anantarā upekkhāsampayuttapacchimacittaṃ uppajjissati tesaṃ jīvitindriyaṃ uppajjissati, "
              "no ca tesaṃ somanassindriyaṃ uppajjissati.",
              "Itaresaṃ tesaṃ jīvitindriyañca uppajjissati somanassindriyañca uppajjissati.",
              "Yā itthiyo eteneva bhāvena katici bhave dassetvā parinibbāyissanti tāsaṃ ghānindriyaṃ uppajjissati, no "
              "ca tāsaṃ purisindriyaṃ uppajjissati."):
        row(s, line12(s, M))
    h("Clashes between finished chapters (for the coordinator)")
    out += [
        "- A head that is only a run of plane-beings (Rūpāvacarānaṃ arūpāvacarānaṃ, Catuvokārānaṃ pañcavokārānaṃ, "
        "Suddhāvāsānaṃ asaññasattānaṃ [arūpānaṃ] … tesaṃ tattha): 10-02 ind_answer_head / 3-02 ay_persons / 2-01 / "
        "9-01 / 5-01 give «Ở chúng sinh trong cõi hình sắc và cõi không hình sắc» (used in 2-01, 3-02 … 3-04, 5-01, "
        "9-01); 10-03 head_parts10 would give «… và chúng sinh trong cõi không hình sắc» (never printed: 10-03 / "
        "10-04 have no such head). Followed 10-02 / 3-02 (the earlier, printed form). Heads: "
        + ", ".join(sorted(CLASH_10_03)) + ".",
        "",
        "## Termbase misfits and gaps (for the coordinator)",
        "",
        f"- katici «{KATICI}», dassetvā «{DASSETVA}» (no entries; commentary ^6-183: katici paṭisandhiyo gahetvā): "
        f"katici bhave dassetvā «{KATICI_BHAVE}». Please confirm.",
        "- Ye-clauses with eteneva bhāvena: the absolutives are set off by commas («Những người nam nào trong chính "
        "trạng thái ấy, sau khi trải qua một số kiếp sống, sẽ nhập Niết-bàn trọn vẹn»); without it 2-01's no-comma "
        "shape («Những người có mắt nào sau khi tái sinh có sự bình thản đi kèm sẽ nhập Niết-bàn trọn vẹn»).",
        "- Ye sacakkhukā / saghānakā «Những người có mắt / có mũi nào» (termbase sacakkhukā «có mắt»; saghānakā has no "
        "entry: sibling Saghānakānaṃ «có mũi», 3-01). Ye purisā / Yā itthiyo «Những người nam / nữ nào» (termbase).",
        "- somanassena / upekkhāya with upapajjitvā «sau khi tái sinh có niềm vui / có sự bình thản đi kèm» (10-02 "
        "feel_vi after the verb).",
        "- yassa cittassa anantarā <X>pacchimacittaṃ uppajjissati: «những người mà tâm cuối cùng gắn liền với … sẽ "
        "sinh khởi ngay sau tâm này» = 6-01's anantara_group with the termbase kind of final mind (asserted); 9-01's "
        "«… ngay sau tâm này».",
        "- Suddhāvāsānaṃ upapajjantānaṃ (genitive plane-being + participle; the English reads 'those being reborn in "
        "the Pure Abodes'): one group «chúng sinh trong cõi Tịnh Cư đang tái sinh» (9-01 / 10-02 parsers would split "
        "it into two groups «chúng sinh trong cõi Tịnh Cư, những người đang tái sinh …»): "
        + "; ".join(f"{h_} (differs from: " + ", ".join(sorted(n for hh, n, _ in OWN_READING if hh == h_)) + ")"
                    for h_ in sorted({x[0] for x in OWN_READING})) + ".",
        "",
        "## Pāli as written (reported)",
        "",
        "- ^6-10-240 «Yassa vā pana purisindriyaṃ uppajjittha tattha cakkhundriyaṃ uppajjitthāti?» (yassa … tattha; the "
        "parallels have tassa): translated as written «Còn ở người nào mà …, thì ở nơi ấy có phải … không?».",
        "- ^6-10-256 «manindriyaṃ ca uppajjittha» (for manindriyañca): rendered as the both-frame.",
        f"- ^6-10-261 «jīvitindriyaṃ … somanassindriyaṃ» (space before the cut): «{M.subj('jīvitindriyaṃ')}{S.PE} "
        f"{M.subj('somanassindriyaṃ')}».",
        "- ^6-10-243, ^6-10-263: an answer and the next (unlabelled) question with its answer stand on one line: kept.",
        "- ^6-10-244 / 253 / 265 / 274 «Āmantā …pe….» = «Đúng vậy …» (10-01 / 10-02); ^6-10-261 «Natthi …pe….» = "
        "«Không có …».",
        "- ^6-10-257 «(Ka) yassa yattha upekkhindriyaṃ … manindriyaṃ uppajjitthāti?» labelled (Ka), then an unlabelled "
        "«Yassa vā pana …»: kept as written.",
        "- ^6-10-276 «Suddhāvāsānaṃ upapatticittassa uppādakkhaṇe tesaṃ tattha …»: «Ở chúng sinh trong cõi Tịnh Cư, "
        "vào khoảnh khắc sinh khởi của tâm tái sinh, …» (5-01).",
        "- ^6-10-282, ^6-10-283 «Itaresaṃ tesaṃ …» after «Yā itthiyo … tāsaṃ»: «Ở những người khác, thì ở những người "
        "ấy …» (tāsaṃ = tesaṃ, 10-02).",
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
    for bad, (good, n) in SLIPS.items():
        got = sum(1 for s in SLIPS_SEEN if len(s) == 3 and s[1] == bad)
        assert got == n, (bad, got, n)
    S.write(CH, segs)
    text = (S.OUT_DIR / CH).read_text(encoding="utf-8")
    ADH_DIR.mkdir(parents=True, exist_ok=True)
    (ADH_DIR / CH).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", ADH_DIR / CH)
    NOTES_MD.write_text(unicodedata.normalize("NFC", notes()), encoding="utf-8", newline="\n")
    print("wrote", NOTES_MD)
    print("checked equal:", CHECKED, "; heads:", len(HEADS_SEEN), "; own reading:", len(OWN_READING),
          "; 10-03 clash:", len(CLASH_10_03), "; slips:", len(SLIPS_SEEN))


def probe(name=CH):
    for seg in S.segments_of(name):
        for ln in seg:
            try:
                print("OK  ", tr_line(ln))
            except Exception as e:  # noqa: BLE001
                print("FAIL", ln[:200], "\n    ", type(e).__name__, str(e)[:300])


if __name__ == "__main__":
    if sys.argv[1:] == ["probe"]:
        probe()
    else:
        main()
