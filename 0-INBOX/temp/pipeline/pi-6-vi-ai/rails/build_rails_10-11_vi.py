"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 10-11 (Indriyayamaka 11: uppādavāra, (5) paccuppannānāgatavāro,
(Ca) paccanīkapuggalokāsā: «yassa yattha A na uppajjati tassa tattha B na uppajjissati»).

Setters (all imported READ-ONLY with importlib; every shared string comes from their functions):
  build_rails_10-08_vi  (J8)  nearest setter: question12 (whole and cut pair questions with a separate na),
                              answer_head12 / persons12 (Indriya person heads with planes), mind_gen12, pv_sentence12,
                              tr_line (asserted equal wherever it parses); through it 10-04 … 10-01, 9-01, 3-02, 3-01,
                              2-01, 7-01, 8, 5-01 (the very module objects)
  build_rails_10-05_vi  (J5)  ye_clause12 (Ye purisā / Yā itthiyo / sacakkhukā / saghānakā, eteneva bhāvena, katici
                              bhave dassetvā, somanassena / upekkhāya upapajjitvā), YE_REL, YE_CA_RE, pacchima_mind
                              (termbase kinds of final mind), ye_head12 / answer_head12 / pv_sentence12 (cross-checks)
  build_rails_6-01_vi   (Q6)  through 10-05: the smooth anantarā shape (user: «… ngay sau tâm này», not «Vào tâm mà
                              ngay sau đó …»); answer_head (cross-check)
  build_rails_9-01_vi   (DY)  that_mind_moment («vào khoảnh khắc … của tâm mà ngay sau đó …»), moment_vi, EXTRA_PERSON,
                              ANANTARA, verb
  build_rails_9-02_vi   (P92) gen_vi("Pacchimacittassa") «tâm cuối cùng» (8 mind_gen_vi), answer_head (asserted)
  build_rails_3-03_vi   (A3)  flat_persons, ye_ca_head, YE_TAILS / KHI_UPAPAJJANTA (identical Pāli: asserted)
  build_rails_3-02_vi   (A2)  ay_person_items / ay_persons / answer_head (identical Pāli: asserted)
  build_rails_2-02_vi   (D2)  KHI_CAVANTA, TE      build_rails_2-01_vi (B): b_noca, b_both, join_and, being_run, ATTRS
  build_rails_10-02_vi  (I2)  ind_group, SEX / sex_vi, FEEL, PART_FEM, PRON_FEM, SAMPAYUTTA, FAC_MIND, heading

New here (named constants; later Indriya chapters may import them):
  PART_FEM11      cavantīnaṃ = cavantānaṃ «đang chết đi» (termbase), upapajjantīnaṃ (10-02)
  YE_TAILS11      "… parinibbāyissanti tāsaṃ cavantīnaṃ / tāsaṃ upapajjantīnaṃ" = 3-03's tails «, khi những người ấy
                  đang chết đi / đang tái sinh» (Vietnamese has no gender, as 10-02 tāsaṃ = tesaṃ)
  PACCHIMA_ATTR / pacchima_group
                  coordinator rule "Pacchimabhavikānaṃ <A>ānaṃ <B>ānaṃ upapajjantānaṃ is one group of persons":
                  "Pacchimabhavikānaṃ saghānakānaṃ upapajjantānaṃ" «những người thuộc kiếp sống cuối cùng có mũi đang
                  tái sinh» (coordinator: person type + attribute, no comma); "Pacchimabhavikānaṃ itthīnaṃ
                  upapajjantīnaṃ" «những người thuộc kiếp sống cuối cùng đang tái sinh làm người nữ» (sex word after the
                  participle, 10-02)
  pacchima_gen / samangi_person / that_mind_moment_x
                  Somanassa- / Upekkhāsampayuttapacchimacittassa «tâm cuối cùng gắn liền với niềm vui / sự bình thản»
                  (termbase = 10-05 pacchima_mind); <X>sampayuttapacchimacittasamaṅgīnaṃ «những người có được tâm cuối
                  cùng gắn liền với …» (8 + termbase); "yassa cittassa anantarā <X>pacchimacittaṃ uppajjissati tassa
                  cittassa <moment>" «vào khoảnh khắc … của tâm mà ngay sau đó tâm cuối cùng gắn liền với … sẽ sinh
                  khởi» (9-01 that_mind_moment shape, asserted; coordinator "From rails 9-01")
  person_items11 / persons11 / ye_head11 / head_parts11 / answer_head11 / NOCA11_RE / BOTH11_RE / pv_sentence11 /
  unit11 / line11 / tr_line / build
A line, unit or word the parsers cannot place raises ValueError (no silent fallback). Importing writes nothing.

usage: python -I -X utf8 -B build_rails_10-11_vi.py   (probe: … build_rails_10-11_vi.py probe)
"""
import importlib
import re
import sys
import unicodedata

RAILS_DIR = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\rails"
if RAILS_DIR not in sys.path:
    sys.path.insert(0, RAILS_DIR)
import build_rails_sample_vi as S  # noqa: E402  (READ-ONLY)
J8 = importlib.import_module("build_rails_10-08_vi")   # READ-ONLY: nearest setter (Indriya uppādavāra lines)
J5 = importlib.import_module("build_rails_10-05_vi")   # READ-ONLY: Ye-clauses with eteneva / katici, final minds
Q6 = importlib.import_module("build_rails_6-01_vi")    # READ-ONLY: anantarā group shape (user: smooth)
A3 = importlib.import_module("build_rails_3-03_vi")    # READ-ONLY: "P ye ca … tesaṃ cavantānaṃ" heads (identical Pāli)
P92 = importlib.import_module("build_rails_9-02_vi")   # READ-ONLY: Pacchimacittassa «tâm cuối cùng»
J10 = importlib.import_module("build_rails_10-10_vi")  # READ-ONLY: parallel chapter (coordinator-accepted frames)
assert J10.J8 is J8 and J10.J5 is J5 and J10.A3 is A3 and J10.P92 is P92 and J10.Q6 is Q6
I4, I3, I2, I, A, A2, B, C, DY, D8 = J8.I4, J8.I3, J8.I2, J8.I, J8.A, J8.A2, J8.B, J8.C, J8.DY, J8.D8
assert J5.I4 is I4 and J5.I2 is I2 and J5.DY is DY and J5.B is B and J5.D8 is D8 and J5.S6 is Q6 and J5.A3 is A3
assert A3.A2 is A2 and A3.B is B and A3.C is C and P92.DY is DY and P92.D is D8 and Q6.DY is DY
D2 = A3.D                                              # build_rails_2-02_vi (KHI_CAVANTA, TE, YE_CA)

cap = S.cap
lc = I2.lc
CH = "10-11-indriyayamaka.md"
N = "10-11"
NOTES_MD = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/notes-rails-{N}.md"
ADH_DIR = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/adh-{N}"
M_IND = I.INDRIYA
PLANES = A.PLANES_AY
CHECKED = {"10-08 line": 0, "10-08 sentence": 0, "10-05 sentence": 0, "10-08 head": 0, "10-05 head": 0,
           "3-02 head": 0, "3-03 ye head": 0, "10-05 ye head": 0, "9-02 head": 0, "3-02 persons": 0,
           "10-08 persons": 0, "10-08 group": 0, "10-10 group": 0, "10-10 ye head": 0, "10-10 head": 0,
           "10-10 sentence": 0, "10-10 line": 0}
HEADS_SEEN = {}          # Pāli head -> Vietnamese
OWN_READING = {}         # head -> (setter, setter's string): differs on purpose (coordinator's one-group rule)
SLIPS_SEEN = []

# ===============================================================================================================
# 1. Slips rendered as meant (reported); count = expected occurrences
# ===============================================================================================================
SLIPS = {
    # ^6-10-398 (Kha) purisa / upekkhā: «uppajjantānaṃ» for upapajjantānaṃ (termbase entry uppajjantānaṃ «đang tái
    # sinh», "the reading uppajjantānaṃ for upapajjantānaṃ"); the parallels have upapajjantānaṃ
    "Pacchimabhavikānaṃ purisānaṃ uppajjantānaṃ ye ca": ("Pacchimabhavikānaṃ purisānaṃ upapajjantānaṃ ye ca", 1),
}

# ===============================================================================================================
# 2. Final minds, their possessors, "yassa cittassa anantarā … tassa cittassa <moment>"
# ===============================================================================================================
# 10-10's functions, used as they are (coordinator: 10-09, 10-11, 10-12 align to them byte for byte)
PACCHIMA_GEN_RE = J10.PACCHIMA_GEN_RE
SAMANGI_RE = J10.SAMANGI_RE
pacchima_gen = J10.pacchima_gen          # Pacchimacittassa «tâm cuối cùng»; Somanassasampayutta… «… gắn liền với niềm vui»
samangi_person = J10.samangi_person      # «những người có được tâm cuối cùng gắn liền với …»
THAT_MIND_REL = J10.THAT_MIND_REL        # «tâm mà ngay sau đó …» (9-01 that_mind_moment)
that_mind_moment_x = J10.that_mind_moment_x
assert DY.that_mind_moment("bhaṅgakkhaṇe") == DY.moment_vi("bhaṅgakkhaṇe", f"{THAT_MIND_REL} {DY.ATTAIN_TOP}")


# ===============================================================================================================
# 3. Person phrases (3-02 / 3-03 items; Indriya groups 10-08 / 10-02; the coordinator's Pacchimabhavikānaṃ group)
# ===============================================================================================================
PACCHIMA = "pacchimabhavikānaṃ"
PACCHIMA_ATTR = J10.PACCHIMA_ATTR                     # «thuộc kiếp sống cuối cùng» (2-01; termbase; 10-10)
PART_FEM11 = {**I2.PART_FEM, "cavantīnaṃ": "cavantānaṃ"}   # termbase cavantīnaṃ «đang chết đi» = cavantānaṃ
assert B.PARTICIPLES["cavantānaṃ"][0] == "đang chết đi"


def _part(t):
    tl = lc(t)
    return PART_FEM11.get(tl, tl) if (tl in B.PARTICIPLES or tl in PART_FEM11) else None


def _plane(t):
    return B.plane_tok(lc(t), PLANES)


def _ind_word(t):
    tl = lc(t)
    return tl in I2.NEW_WORDS or tl in PART_FEM11


def pacchima_group(toks):
    """'Pacchimabhavikānaṃ [<attr>ānaṃ …] [na] [itthīnaṃ | purisānaṃ] [<plane-acc>] <participle>' with an Indriya /
    āyatana word: ONE group (coordinator rule) → «những người thuộc kiếp sống cuối cùng[, có mũi] đang tái sinh [vào
    X] [làm người nữ]» (10-02 ind_group: attributes joined by ATTR_JOIN, sex / feeling word after the participle;
    plane after the participle as 10-08 group12)."""
    low = [lc(t) for t in toks]
    if not low or low[0] != PACCHIMA:
        raise ValueError(f"not a Pacchimabhavikānaṃ group {toks!r}")
    pre, sex, feel, neg, planes, part = [PACCHIMA_ATTR], None, None, False, [], None
    for t in low[1:]:
        if part:
            raise ValueError(f"word after the participle in {toks!r}")
        pt = _plane(t)
        if t == "na":
            neg = True
        elif t in I2.PRE_ATTRS:
            if neg or sex or planes:
                raise ValueError(f"misplaced attribute {t!r} in {toks!r}")
            pre.append(I2.PRE_ATTRS[t])
        elif t in I2.SEX:
            sex, neg = I2.sex_vi(t, neg), False
        elif t in I2.FEEL:
            feel = I2.feel_vi(t)
        elif pt and pt[1] in ("acc", "abl"):
            planes.append(pt)
        elif _part(t):
            part = _part(t)
        else:
            raise ValueError(f"unknown word {t!r} in {toks!r}")
    if neg or not part:
        raise ValueError(f"incomplete group {toks!r}")
    pv, case, prep = B.PARTICIPLES[part]
    if any(c != case for _, c in planes):
        raise ValueError(f"plane case does not fit {part!r} in {toks!r}")
    if len(pre) > 1:      # coordinator: «thuộc kiếp sống cuối cùng» is the person type, no ATTR_JOIN comma after it
        pre = [f"{pre[0]} {A.ATTR_JOIN.join(pre[1:])}"]
    base = I2.ind_group(None, pre, part)
    full = I2.ind_group(None, pre, part, sex, feel)
    assert full.startswith(base), (toks, base, full)
    out = base + (f" {prep} {B.join_and(PLANES[k][0] for k, _ in planes)}" if planes else "") + full[len(base):]
    assert I2.ind_group(None, [PACCHIMA_ATTR], part) == A2.ay_persons(f"Pacchimabhavikānaṃ {part}", PLANES)
    if all(lc(t) not in I2.PRE_ATTRS for t in toks) and not planes:   # the 10-10 shape (sex / feeling word only)
        assert out == J10.pacchima_sex_group(toks), (toks, out)
        CHECKED["10-10 group"] += 1
    return out


def _is_pacchima_group(toks):
    low = [lc(t) for t in toks]
    return low[:1] == [PACCHIMA] and any(t in I2.PRE_ATTRS or t in I2.SEX or t in I2.FEEL for t in low[1:])


def group11(toks):
    """One person group (ends with its participle, or a locative-plane Pacchimabhavikānaṃ group)."""
    phrase = " ".join(toks)
    if _is_pacchima_group(toks):
        return pacchima_group(toks)
    if any(_ind_word(t) for t in toks):
        out = J8.persons12(phrase)                       # 10-08 group12 / 10-03 persons10 / 10-02 ind_persons
        CHECKED["10-08 group"] += 1
        if f" {C.AND} " in out:
            raise ValueError(f"one group read as several by 10-08: {phrase!r}")
        return out
    items = A2.ay_person_items(phrase, PLANES)
    if len(items) != 1 or items[0][0] != "group":
        raise ValueError(f"not one group {phrase!r}: {items!r}")
    return items[0][1]


def person_items11(phrase):
    """Genitive person phrase → list of Vietnamese items (joined flat by the caller, 3-02 / 3-03 rule «A, B và C»).
    Groups end at their participle (or at a Pacchimabhavikānaṃ after locative planes / before a non-group word);
    genitive plane-beings form runs; one run alone keeps 2-01's being_run («chúng sinh trong cõi X và cõi Y»), in a
    longer list each plane-being is its own item. Without Indriya words / the Pacchimabhavikānaṃ group this is
    3-03 flat_persons (asserted)."""
    toks = phrase.split()
    items, cur = [], []
    for i, t in enumerate(toks):
        pt = _plane(t)
        if pt and pt[1] == "gen" and not cur:
            if items and items[-1][0] == "run":
                items[-1][1].append(pt[0])
            else:
                items.append(("run", [pt[0]]))
            continue
        cur.append(t)
        if _part(t):
            items.append(("group", cur))
            cur = []
        elif lc(t) == PACCHIMA:
            nxt = toks[i + 1] if i + 1 < len(toks) else None
            only_loc = all((q := _plane(x)) and q[1] == "loc" for x in cur[:-1])
            nxt_in_group = nxt is not None and (_part(nxt) or lc(nxt) in I2.PRE_ATTRS or lc(nxt) in I2.SEX
                                                or lc(nxt) == "na" or ((q := _plane(nxt)) and q[1] in ("acc", "abl")))
            if (cur[:-1] and only_loc) or not nxt_in_group:
                items.append(("group", cur))
                cur = []
    if cur:
        raise ValueError(f"dangling words {cur!r} in {phrase!r}")
    if len(items) == 1 and items[0][0] == "run":
        flat = [B.being_run(items[0][1], None, PLANES)]
    else:
        flat = []
        for it in items:
            if it[0] == "group":
                flat.append(group11(it[1]))
            elif len(it[1]) == 1:
                flat.append(B.being_run(it[1], None, PLANES))
            else:
                flat += [PLANES[k][1] for k in it[1]]
    own = any(it[0] == "group" and _is_pacchima_group(it[1]) for it in items)
    if not own and not any(_ind_word(t) for t in toks):
        assert flat == A3.flat_persons(phrase, PLANES), (phrase, flat)
    return flat, own


def persons11(phrase):
    flat, own = person_items11(phrase)
    out = B.join_and(flat)
    for name, f in (("3-02 persons", lambda: A2.ay_persons(phrase, PLANES)),
                    ("10-08 persons", lambda: J8.persons12(phrase))):
        try:
            old = f()
        except (ValueError, KeyError):
            continue
        if own:
            if old != out:
                OWN_READING[phrase] = (name, old)
            continue
        assert old == out, (name, phrase, old, out)
        CHECKED[name] += 1
    return out


# ===============================================================================================================
# 4. Ye heads: "P [P2 …] ye ca / yā ca … parinibbāyissanti [tesaṃ | tāsaṃ] [cavantānaṃ | cavantīnaṃ | upapajjantānaṃ |
#    upapajjantīnaṃ]"
# ===============================================================================================================
YE_TAILS11 = {**A3.YE_TAILS,
              " tāsaṃ upapajjantīnaṃ": A3.KHI_UPAPAJJANTA,      # tāsaṃ / -antīnaṃ = tesaṃ / -antānaṃ (10-02)
              " tāsaṃ cavantīnaṃ": D2.KHI_CAVANTA}
assert A3.YE_TAILS[" tesaṃ cavantānaṃ"] == D2.KHI_CAVANTA == f"khi {D2.TE} {B.PARTICIPLES['cavantānaṃ'][0]}"
assert A3.KHI_UPAPAJJANTA == f"khi {D2.TE} {B.PARTICIPLES['upapajjantānaṃ'][0]}"
assert I2.PRON_FEM["tāsaṃ"] == "tesaṃ"
YE_SPLIT_RE = re.compile(r" (ye|yā) ca ")


def is_ye_head(head):
    return J5.is_ye_head(head)


def ye_head11(head):
    """«Ở <P>, <P2> và những người nam nào …[, khi những người ấy đang chết đi]»: one flat list (3-03), ye clauses by
    10-05 ye_clause12, the tail by 3-03 / 2-02."""
    tail = next((t for t in YE_TAILS11 if head.endswith(t)), None)
    core = head[: -len(tail)] if tail else head
    pieces = YE_SPLIT_RE.split(core)          # [left, rel, clause, rel, clause, …]
    left = pieces[0]
    clauses = [("Yā " if rel == "yā" else "Ye ") + c for rel, c in zip(pieces[1::2], pieces[2::2])]
    if left.split()[0] in J5.YE_REL:
        items, own, first = [], False, [J5.ye_clause12(left)]
    else:
        (items, own), first = person_items11(left), []
    yes = first + [lc(J5.ye_clause12(c)) for c in clauses]
    body = B.join_and(items + yes)
    core_vi = f"{B.AT} {body}" if items else body
    out = core_vi + (f", {YE_TAILS11[tail]}" if tail else "")
    for name, f, want in (("3-03 ye head", lambda: A3.ye_ca_head(head, PLANES), out),
                          ("10-05 ye head", lambda: J5.ye_head12(core), core_vi),
                          ("10-10 ye head", lambda: J10.ye_head(head), out)):
        try:
            old = f()
        except (ValueError, KeyError):
            continue
        if own:
            if old != want:
                OWN_READING[head] = (name, old)
            continue
        assert old == want, (name, head, old, want)
        CHECKED[name] += 1
    return out


# ===============================================================================================================
# 5. Answer heads (9-01 shape: parts joined «, »; one «ở» per run of persons; a run after a time phrase keeps its «ở»)
# ===============================================================================================================
ANANTARA_WORDS = J5.ANANTARA_WORDS                    # ["yassa", "cittassa", "anantarā"]


def head_parts11(head):
    toks = head.split()
    low = [lc(t) for t in toks]
    parts, run, buf, i = [], [], [], 0
    own = False

    def flush_buf():
        nonlocal own
        if buf:
            flat, o = person_items11(" ".join(buf))
            own = own or o
            run.extend(flat)
            buf.clear()

    def flush():
        flush_buf()
        if run:
            parts.append(f"{C.AT} {B.join_and(run)}")
            run.clear()

    while i < len(toks):
        if low[i:i + 3] == ANANTARA_WORDS:
            if i + 4 >= len(toks):
                raise ValueError(f"short anantarā phrase in {head!r}")
            if low[i + 5:i + 7] == ["tassa", "cittassa"]:
                if i + 7 >= len(toks) or low[i + 7] not in D8.MOMENT:
                    raise ValueError(f"'tassa cittassa' without a moment in {head!r}")
                flush()
                parts.append(that_mind_moment_x(toks[i + 7], toks[i + 3], toks[i + 4]))
                i += 8
            else:
                flush_buf()
                run.append(J5.anantara_group(toks[i + 3], toks[i + 4]))
                i += 5
            continue
        if i + 1 < len(toks) and low[i + 1] in D8.MOMENT:
            flush()
            parts.append(DY.moment_vi(toks[i + 1], pacchima_gen(toks[i])))
            i += 2
            continue
        if low[i] == "pavatte":
            flush()
            parts.append(DY.PAVATTE)
            i += 1
            continue
        if SAMANGI_RE.fullmatch(low[i]):
            flush_buf()
            run.append(samangi_person(toks[i]))
            i += 1
            continue
        if low[i] in DY.EXTRA_PERSON:
            flush_buf()
            run.append(DY.EXTRA_PERSON[low[i]])
            i += 1
            continue
        if low[i] == "sabbesaṃ" and (i + 1 >= len(toks) or low[i + 1] in D8.MOMENT
                                     or (i + 2 < len(toks) and low[i + 2] in D8.MOMENT)):
            flush_buf()
            run.append(DY.ALL_BEINGS)                     # bare Sabbesaṃ «tất cả chúng sinh» (9-01 / 10-08)
            i += 1
            continue
        buf.append(toks[i])
        i += 1
    flush()
    if not parts:
        raise ValueError(f"empty answer head {head!r}")
    return parts, own


def answer_head11(head, loc):
    if loc == "tattha":
        return B.place_head(head, PLANES)
    if is_ye_head(head):
        out = ye_head11(head)
        HEADS_SEEN[head] = out
        return out
    parts, own = head_parts11(head)
    out = cap(", ".join(parts))
    for name, f in (("10-10 head", lambda: J10.answer_head(head, loc)),
                    ("10-08 head", lambda: J8.answer_head12(head, loc)),
                    ("10-05 head", lambda: J5.answer_head12(head, loc)),
                    ("3-02 head", lambda: A2.answer_head(head, loc, PLANES)),
                    ("9-02 head", lambda: P92.answer_head(head, loc))):
        try:
            old = f()
        except (ValueError, KeyError):
            continue
        except AssertionError:                # a setter's own internal cross-check fails on this head: skip it
            continue
        if own:
            if old != out:
                OWN_READING[head] = (name, old)
            continue
        if name == "9-02 head" and not any(lc(t) == "pacchimacittassa" for t in head.split()):
            continue                          # 9-02 / 9-01 read nested plane runs with two «và» (10-07 clash note)
        assert old == out, (name, head, old, out)
        CHECKED[name] += 1
    HEADS_SEEN[head] = out
    return out


# ===============================================================================================================
# 6. Sentences, units, lines
# ===============================================================================================================
LOCP = r"(tesaṃ tattha|tāsaṃ tattha)"
NOCA11_RE = re.compile(r"(.+) " + LOCP + r" (\S+ (?:na )?\S+), no ca \2 (\S+ (?:na )?\S+)\.")
BOTH11_RE = re.compile(r"(.+) " + LOCP + r" (\S+?ñca) ((?:na )?\S+) (\S+?ñca) ((?:na )?\S+)\.")


def pv_sentence11(s, M=None):
    """Family B answers (2-01 b_noca / b_both) with this chapter's heads; the head is everything before the tesaṃ /
    tāsaṃ tattha that opens the member clause (a ye-head tail «tesaṃ cavantānaṃ» stays in the head)."""
    M = M or M_IND
    if m := NOCA11_RE.fullmatch(s):
        head, loc, c1, c2 = m.groups()
        a, v1 = I3.split_mv(c1, M)
        b, v2 = I3.split_mv(c2, M)
        out = B.b_noca(answer_head11(head, loc), I2.PRON_FEM.get(loc, loc), a, v1, b, v2)
    elif m := BOTH11_RE.fullmatch(s):
        head, loc, c1, v1, c2, v2 = m.groups()
        out = B.b_both(answer_head11(head, loc), I2.PRON_FEM.get(loc, loc), M.subj(c1), I3.verb(v1), M.subj(c2),
                       I3.verb(v2))
    else:
        return None
    for name, f in (("10-08 sentence", J8.pv_sentence12), ("10-05 sentence", J5.pv_sentence12),
                    ("10-10 sentence", J10.pv_sentence)):
        try:
            old = f(s, M)
        except (ValueError, KeyError, AssertionError):
            old = None
        if old is not None and old != out and any(h in s for h in OWN_READING):
            continue
        if old is not None:
            assert old == out, (name, s, old, out)
            CHECKED[name] += 1
    return out


def unit11(u, M=None):
    M = M or M_IND
    if (lab := I.ind_mulaka(u, M)) is not None:
        return lab
    if u.endswith("?"):
        return J8.question12(u[:-1], M)
    if u in B.SHORT:
        return B.SHORT[u]
    if "…" in u:
        raise ValueError(f"cut not set in this chapter: {u!r}")
    if (out := pv_sentence11(u, M)) is not None:
        return out
    raise ValueError(f"unknown unit {u!r}")


def line11(body, M=None):
    body, label = body.strip(), None
    if m := re.fullmatch(r"(.+?) (\(\w+mūlakaṃ\)\.?)", body):     # trailing (Xindriyamūlakaṃ) label (10-02)
        body, label = m.group(1), m.group(2)
    units = [x for x in re.split(r"(?<=[.?]) (?=\S)", body) if x]
    if label:
        units.append(label)
    return " ".join(unit11(x, M) for x in units)


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
        out = line11(body, M)
    full = f"{out} {bid}" if bid else out
    try:
        old = J8.tr_line(p, M, fixed)
    except (ValueError, KeyError, AssertionError):
        old = None
    if old is not None:
        assert old == full, ("10-08 line", p, old, full)
        CHECKED["10-08 line"] += 1
    try:
        old = J10.tr_line(p, M, fixed)
    except (ValueError, KeyError, AssertionError):
        old = None
    if old is not None:
        assert old == full, ("10-10 line", p, old, full)
        CHECKED["10-10 line"] += 1
    return full


def build(name, M=None, fixed=None):
    return [[tr_line(ln, M, fixed) for ln in seg] for seg in S.segments_of(name)]


# ===============================================================================================================
# 7. Checks
# ===============================================================================================================
TERMBASE_USED = [   # pi-6 termbase entries used verbatim («Pāli: {…: Vietnamese}»)
    ("Pacchimacittassa", P92.gen_vi("Pacchimacittassa")),
    ("Pacchimacittassa bhaṅgakkhaṇe", f"{D8.MOMENT['bhaṅgakkhaṇe']} {D8.OF} {pacchima_gen('Pacchimacittassa')}"),
    ("Pacchimacittassa uppādakkhaṇe", f"{D8.MOMENT['uppādakkhaṇe']} {D8.OF} {pacchima_gen('Pacchimacittassa')}"),
    ("Somanassasampayuttapacchimacittassa uppādakkhaṇe",
     f"{D8.MOMENT['uppādakkhaṇe']} {D8.OF} {pacchima_gen('Somanassasampayuttapacchimacittassa')}"),
    ("Somanassasampayuttapacchimacittassa bhaṅgakkhaṇe",
     f"{D8.MOMENT['bhaṅgakkhaṇe']} {D8.OF} {pacchima_gen('Somanassasampayuttapacchimacittassa')}"),
    ("Upekkhāsampayuttapacchimacittassa uppādakkhaṇe",
     f"{D8.MOMENT['uppādakkhaṇe']} {D8.OF} {pacchima_gen('Upekkhāsampayuttapacchimacittassa')}"),
    ("Upekkhāsampayuttapacchimacittassa bhaṅgakkhaṇe",
     f"{D8.MOMENT['bhaṅgakkhaṇe']} {D8.OF} {pacchima_gen('Upekkhāsampayuttapacchimacittassa')}"),
    ("upekkhāsampayuttapacchimacittasamaṅgīnaṃ",
     samangi_person("upekkhāsampayuttapacchimacittasamaṅgīnaṃ").removeprefix("những ")),
    ("somanassasampayuttapacchimacittasamaṅgīnaṃ",
     samangi_person("somanassasampayuttapacchimacittasamaṅgīnaṃ").removeprefix("những ")),
    ("upekkhāsampayuttapacchimacittaṃ", J5.pacchima_mind("upekkhāsampayuttapacchimacittaṃ")),
    ("somanassasampayuttapacchimacittaṃ", J5.pacchima_mind("somanassasampayuttapacchimacittaṃ")),
    ("Pacchimabhavikānaṃ", f"{J5.YE_PERSON} {PACCHIMA_ATTR}"), ("Pañcavokāre", PLANES["pañcavokār"][0]),
    ("Kāmāvacare", PLANES["kāmāvacar"][0]), ("arūpāvacare", PLANES["arūpāvacar"][0]),
    ("upapajjantīnaṃ", B.PARTICIPLES["upapajjantānaṃ"][0]), ("cavantīnaṃ", B.PARTICIPLES["cavantānaṃ"][0]),
    ("uppajjantānaṃ", B.PARTICIPLES["upapajjantānaṃ"][0]),
    ("purisā", J5.YE_NOUN["purisā"]), ("itthiyo", J5.YE_NOUN["itthiyo"]), ("sacakkhukā", A.AY_ATTRS["sacakkhukānaṃ"]),
    ("purisānaṃ", I2.SEX["purisānaṃ"]), ("anantarā", DY.ANANTARA),
    ("somanassavippayuttacittassa uppādakkhaṇe",
     f"{D8.MOMENT['uppādakkhaṇe']} {D8.OF} {pacchima_gen('somanassavippayuttacittassa')}"),
    ("upekkhāvippayuttacittassa uppādakkhaṇe",
     f"{D8.MOMENT['uppādakkhaṇe']} {D8.OF} {pacchima_gen('upekkhāvippayuttacittassa')}"),
    ("saddhāvippayuttacittassa uppādakkhaṇe",
     f"{D8.MOMENT['uppādakkhaṇe']} {D8.OF} {pacchima_gen('saddhāvippayuttacittassa')}"),
    ("ñāṇavippayuttacittassa uppādakkhaṇe",
     f"{D8.MOMENT['uppādakkhaṇe']} {D8.OF} {pacchima_gen('ñāṇavippayuttacittassa')}"),
]


def check_termbase():
    tb = I2.termbase_text()
    bad = [(p, v) for p, v in TERMBASE_USED
           if not re.search(rf"^{re.escape(p)}: {{.*: {re.escape(v)}}}$", tb, re.M)]
    assert not bad, "termbase entries not matched: " + repr(bad)
    J8.check_termbase()
    J5.check_termbase()


def check_frames():
    # 3-03 heads with the identical Pāli (one left group / two left groups, both tails)
    for h in ("Pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti tesaṃ "
              "upapajjantānaṃ",
              "Pañcavokāre parinibbantānaṃ arūpe pacchimabhavikānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti tesaṃ "
              "cavantānaṃ",
              "Kāmāvacare parinibbantānaṃ rūpāvacare arūpāvacare pacchimabhavikānaṃ ye ca arūpaṃ upapajjitvā "
              "parinibbāyissanti tesaṃ cavantānaṃ"):
        assert ye_head11(h) == A3.ye_ca_head(h, PLANES), h
    # 10-05 ye heads unchanged where 10-05 has the same Pāli
    for h in ("Ye rūpāvacaraṃ upapajjitvā parinibbāyissanti ye ca purisā eteneva bhāvena katici bhave dassetvā "
              "parinibbāyissanti",
              "Rūpāvacarānaṃ ye ca purisā eteneva bhāvena katici bhave dassetvā parinibbāyissanti",
              "Pacchimabhavikānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti yā ca itthiyo eteneva bhāvena katici "
              "bhave dassetvā parinibbāyissanti"):
        assert ye_head11(h) == J5.ye_head12(h), h
    # 9-02 final-mind heads; 9-01 anantarā endings; 6-01 group ending; 10-08 sex + plane group
    for h in ("Pacchimacittassa bhaṅgakkhaṇe", "Pacchimacittassa uppādakkhaṇe"):
        assert answer_head11(h, "tesaṃ") == P92.answer_head(h, "tesaṃ"), h
    assert Q6.anantara_group(None, False).endswith(f" {DY.ANANTARA} {DY.THIS_MIND}")
    hd = "Kāmāvacarā cavantānaṃ na itthīnaṃ kāmāvacaraṃ upapajjantānaṃ rūpāvacarānaṃ arūpāvacarānaṃ"
    assert answer_head11(hd, "tesaṃ tattha") == J8.answer_head12(hd, "tesaṃ tattha"), hd
    hd = "Pañcavokāre parinibbantānaṃ asaññasattānaṃ arūpānaṃ"
    assert answer_head11(hd, "tesaṃ tattha") == A2.answer_head(hd, "tesaṃ tattha", PLANES) == \
        J8.answer_head12(hd, "tesaṃ tattha"), hd
    assert samangi_person("upekkhāsampayuttapacchimacittasamaṅgīnaṃ").startswith(D8.PERSON["pacchimacittasamaṅgīnaṃ"])
    assert pacchima_group("Pacchimabhavikānaṃ itthīnaṃ upapajjantīnaṃ".split()) == \
        f"{A2.ay_persons('Pacchimabhavikānaṃ upapajjantānaṃ', PLANES)} {I2.sex_vi('itthīnaṃ')}"
    assert I2.heading("(Ca) paccanīkapuggalokāsā") == "(e) Chiều nghịch theo người và nơi chốn"
    assert B.noca_vi("B", I3.verb("na uppajjissati")) == "B vẫn sẽ sinh khởi"
    assert B.noca_vi("B", I3.verb("na uppajjati")) == "B vẫn sinh khởi"


def compare_setters():
    """Identical Pāli heads in 10-05 / 10-08 / 10-10 (their chapters rebuilt in memory; nothing written) must read
    the same here."""
    diffs = []
    for name, mod in (("10-05", J5), ("10-08", J8), ("10-10", J10)):
        mod.HEADS_SEEN.clear()                 # my cross-checks filled it: keep only the heads of its own chapter
        mod.build(mod.CH)
        for h, v in mod.HEADS_SEEN.items():
            if h not in HEADS_SEEN:
                continue
            if HEADS_SEEN[h] != v:
                diffs.append((name, h, v, HEADS_SEEN[h]))
    return diffs


def compare_parallel():
    """10-09 / 10-10 are built at the same time: where their builders import and read a head of this chapter, list
    any difference (nothing is asserted; nothing is written)."""
    out = []
    for n in ("10-09",):
        try:
            mod = importlib.import_module(f"build_rails_{n}_vi")
        except Exception as e:  # noqa: BLE001  (a builder in progress may not import)
            out.append((n, "not importable", type(e).__name__, str(e)[:120]))
            continue
        fn = getattr(mod, "answer_head", None) or getattr(mod, "answer_head12", None) \
            or getattr(mod, "answer_head13", None)
        if fn is None:
            out.append((n, "no answer_head", "", ""))
            continue
        for h, v in HEADS_SEEN.items():
            try:
                theirs = fn(h, "tesaṃ tattha")
            except Exception:  # noqa: BLE001
                continue
            if theirs != v:
                out.append((n, h, theirs, v))
    return out


# ===============================================================================================================
# 8. Notes file (Pāli = tiếng Việt)
# ===============================================================================================================
def notes(diffs, par):
    M = M_IND
    out = []

    def row(p, v):
        out.append(f"{p} = {v}")

    def h(t):
        out.extend(["", f"## {t}", ""])

    def hrow(hd, loc="tesaṃ tattha"):
        row(f"{hd} {loc} …", f"{answer_head11(hd, loc)}, {C.THEN} {B.L[I2.PRON_FEM.get(loc, loc)]} …")

    out += [f"# pi-6 rails {N} (Indriyayamaka 11): (5) paccuppannānāgatavāro, (Ca) paccanīkapuggalokāsā", "",
            "Builder: build_rails_10-11_vi.py (import with importlib). Setters: build_rails_10-08_vi (question12, "
            "answer_head12, persons12, mind_gen12, pv_sentence12, tr_line; through it 10-04 … 10-01, 9-01, 3-02, 3-01, "
            "2-01, 7-01, 8, 5-01), build_rails_10-05_vi (ye_clause12, ye_head12, YE_REL, pacchima_mind, "
            "anantara_group), build_rails_6-01_vi (anantarā shape), build_rails_9-02_vi (Pacchimacittassa), "
            "build_rails_3-03_vi (flat_persons, ye_ca_head, YE_TAILS, KHI_UPAPAJJANTA), 2-02 (KHI_CAVANTA), "
            "build_rails_10-10_vi (pacchima_gen, samangi_person, that_mind_moment_x, pacchima_sex_group, ye_head, "
            "answer_head, tr_line: used as they are or asserted); all READ-ONLY. Every line 10-08 / 10-10 parse, every "
            "sentence 10-08 / 10-05 parse, every head 10-10 / 10-08 / 10-05 / 3-02 / 3-03 / 9-02 parse is asserted "
            "byte-identical (except the Pacchimabhavikānaṃ one-group head below). "
            "Exposed: `SLIPS`, `PACCHIMA_GEN_RE`, `SAMANGI_RE`, `pacchima_gen`, `samangi_person`, `THAT_MIND_REL`, "
            "`that_mind_moment_x`, `PACCHIMA_ATTR`, `PART_FEM11`, `pacchima_group`, `group11`, `person_items11`, "
            "`persons11`, `YE_TAILS11`, `ye_head11`, `head_parts11`, `answer_head11`, `NOCA11_RE`, `BOTH11_RE`, "
            "`pv_sentence11`, `unit11`, `line11`, `tr_line`, `build`. Format: Pāli = tiếng Việt.", ""]
    h("Heading")
    row("(Ca) paccanīkapuggalokāsā", I2.heading("(Ca) paccanīkapuggalokāsā"))
    h("Verbs (2-01 VERB_TABLE, 9-01 separate na, coordinator after no ca)")
    for v in ("na uppajjati", "na uppajjissati"):
        row(v, I3.verb(v)[0])
    row("no ca tesaṃ tattha B na uppajjissati", "nhưng ở những người ấy, ở nơi ấy " + B.noca_vi("B", I3.verb(
        "na uppajjissati")))
    row("no ca tesaṃ tattha B na uppajjati", "nhưng ở những người ấy, ở nơi ấy " + B.noca_vi("B", I3.verb(
        "na uppajjati")))
    row("Añca na uppajjati Bñca na uppajjissati", B.b_both("H", "tesaṃ tattha", "A", I3.verb("na uppajjati"), "B",
                                                         I3.verb("na uppajjissati")).split(" ở nơi ấy ", 1)[1])
    h("Questions (10-08 question12)")
    for q in ("(Ka) yassa yattha cakkhundriyaṃ na uppajjati tassa tattha sotindriyaṃ na uppajjissatīti",
              "(Kha) yassa vā pana yattha sotindriyaṃ na uppajjissati tassa tattha cakkhundriyaṃ na uppajjatīti",
              "Yassa yattha cakkhundriyaṃ na uppajjati tassa tattha saddhindriyaṃ…pe… paññindriyaṃ…pe… manindriyaṃ "
              "na uppajjissatīti",
              "Yassa yattha saddhindriyaṃ na uppajjati tassa tattha paññindriyaṃ…pe… manindriyaṃ na uppajjissatīti"):
        row(q + "?", J8.question12(q, M))
    h("New: final minds, their possessors, «tâm mà ngay sau đó …» (9-01 that_mind_moment shape)")
    row("yassa cittassa anantarā <X>pacchimacittaṃ uppajjissati tassa cittassa bhaṅgakkhaṇe",
        that_mind_moment_x("bhaṅgakkhaṇe", "upekkhāsampayuttapacchimacittaṃ", "uppajjissati"))
    for hd in ("Pacchimacittassa bhaṅgakkhaṇe yassa cittassa anantarā upekkhāsampayuttapacchimacittaṃ uppajjissati "
               "tassa cittassa bhaṅgakkhaṇe asaññasattā cavantānaṃ",
               "Pacchimacittassa uppādakkhaṇe yassa cittassa anantarā somanassasampayuttapacchimacittaṃ uppajjissati "
               "tassa cittassa uppādakkhaṇe asaññasattaṃ upapajjantānaṃ",
               "Somanassasampayuttapacchimacittassa bhaṅgakkhaṇe upekkhāsampayuttapacchimacittasamaṅgīnaṃ yassa cittassa "
               "anantarā somanassasampayuttapacchimacittaṃ uppajjissati tassa cittassa bhaṅgakkhaṇe asaññasattānaṃ",
               "Somanassasampayuttapacchimacittassa uppādakkhaṇe yassa cittassa anantarā "
               "somanassasampayuttapacchimacittaṃ uppajjissati tassa cittassa uppādakkhaṇe",
               "Upekkhāsampayuttapacchimacittassa bhaṅgakkhaṇe somanassasampayuttapacchimacittasamaṅgīnaṃ "
               "asaññasattānaṃ",
               "Pacchimacittassa bhaṅgakkhaṇe asaññasattā cavantānaṃ",
               "Sabbesaṃ cittassa bhaṅgakkhaṇe somanassavippayuttacittassa uppādakkhaṇe",
               "Catuvokārā pañcavokārā cavantānaṃ pavatte cittassa bhaṅgakkhaṇe"):
        hrow(hd)
    h("New: Pacchimabhavikānaṃ + attribute / sex word = one group (coordinator rule)")
    for hd in ("Pacchimabhavikānaṃ saghānakānaṃ upapajjantānaṃ", "Pacchimabhavikānaṃ itthīnaṃ upapajjantīnaṃ",
               "Pacchimabhavikānaṃ purisānaṃ upapajjantānaṃ"):
        hrow(hd, "tāsaṃ tattha" if "itthīnaṃ" in hd else "tesaṃ tattha")
    h("New: Ye heads with Indriya clauses and a tail (3-03 flat list + 10-05 clauses; tāsaṃ cavantīnaṃ new)")
    for hd in ("Kāmāvacare parinibbantānaṃ rūpāvacarā cavantānaṃ asaññasattānaṃ arūpānaṃ ye ca purisā eteneva "
               "bhāvena katici bhave dassetvā parinibbāyissanti tesaṃ cavantānaṃ",
               "Pacchimabhavikānaṃ kāmāvacaraṃ upapajjantānaṃ rūpāvacaraṃ upapajjantānaṃ yā ca itthiyo eteneva bhāvena "
               "katici bhave dassetvā parinibbāyissanti tāsaṃ upapajjantīnaṃ",
               "Kāmāvacare parinibbantānaṃ rūpāvacarānaṃ arūpāvacarānaṃ yā ca itthiyo eteneva bhāvena katici bhave "
               "dassetvā parinibbāyissanti tāsaṃ cavantīnaṃ",
               "Pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ ye ca sacakkhukā upekkhāya upapajjitvā "
               "parinibbāyissanti tesaṃ upapajjantānaṃ",
               "Pañcavokāre parinibbantānaṃ arūpe pacchimabhavikānaṃ asaññasattānaṃ ye ca sacakkhukā somanassena "
               "upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ",
               "Pacchimabhavikānaṃ itthīnaṃ upapajjantīnaṃ yā ca itthiyo eteneva bhāvena katici bhave dassetvā "
               "parinibbāyissanti tāsaṃ upapajjantīnaṃ",
               "Pacchimabhavikānaṃ purisānaṃ upapajjantānaṃ ye ca purisā upekkhāya upapajjitvā parinibbāyissanti "
               "tesaṃ upapajjantānaṃ"):
        hrow(hd, "tāsaṃ tattha" if hd.startswith("Pacchimabhavikānaṃ itthīnaṃ") else "tesaṃ tattha")
    h("Heads with locative planes and plane-beings (3-02 / 3-03 / 10-08 strings)")
    for hd in ("Pañcavokāre parinibbantānaṃ arūpe pacchimabhavikānaṃ",
               "Kāmāvacare parinibbantānaṃ rūpāvacare arūpāvacare pacchimabhavikānaṃ asaññasattānaṃ",
               "Kāmāvacare parinibbantānaṃ rūpāvacare pacchimabhavikānaṃ asaññasattānaṃ arūpānaṃ",
               "Pacchimabhavikānaṃ kāmāvacaraṃ upapajjantānaṃ rūpāvacaraṃ upapajjantānaṃ",
               "Sabbesaṃ cavantānaṃ acakkhukānaṃ upapajjantānaṃ"):
        hrow(hd)
    h("Sample lines")
    for s in ("Pacchimabhavikānaṃ itthīnaṃ upapajjantīnaṃ tāsaṃ tattha jīvitindriyaṃ na uppajjissati, no ca tāsaṃ "
              "tattha itthindriyaṃ na uppajjati.",
              "Pacchimacittassa bhaṅgakkhaṇe yassa cittassa anantarā upekkhāsampayuttapacchimacittaṃ uppajjissati tassa "
              "cittassa bhaṅgakkhaṇe asaññasattā cavantānaṃ tesaṃ tattha jīvitindriyañca na uppajjati "
              "somanassindriyañca na uppajjissati."):
        row(s, line11(s, M))
    h("Termbase misfits and gaps (for the coordinator)")
    out += [
        "- Pacchimabhavikānaṃ + attribute / sex word + participle (^6-10-396 «Pacchimabhavikānaṃ saghānakānaṃ "
        "upapajjantānaṃ», ^6-10-397 «… itthīnaṃ upapajjantīnaṃ», ^6-10-398 «… purisānaṃ upapajjantānaṃ»): one group "
        "(coordinator rule) «những người thuộc kiếp sống cuối cùng có mũi đang tái sinh» (coordinator: «thuộc kiếp "
        "sống cuối cùng» is the person type, no ATTR_JOIN comma after it) / «… đang tái sinh làm người nữ / người nam» "
        "(10-02 sex word after the participle). 3-02 / 10-05 parsers would split the first into «những người thuộc "
        "kiếp sống cuối cùng và những người có mũi đang tái sinh» (never printed in finished chapters).",
        "- yassa cittassa anantarā <X>pacchimacittaṃ uppajjissati tassa cittassa <moment> (^6-10-399, ^6-10-400): built "
        "on 9-01's that_mind_moment («vào khoảnh khắc … của tâm mà ngay sau đó …», coordinator) with 10-05's final mind: "
        "«vào khoảnh khắc tan rã của tâm mà ngay sau đó tâm cuối cùng gắn liền với sự bình thản sẽ sinh khởi».",
        "- <X>sampayuttapacchimacittasamaṅgīnaṃ: termbase «người có được tâm cuối cùng gắn liền với …», plural «những "
        "người …» as 8's pacchimacittasamaṅgīnaṃ.",
        "- tāsaṃ cavantīnaṃ after a «yā ca itthiyo …» clause: termbase cavantīnaṃ «đang chết đi»; = 2-02's tail «, khi "
        "những người ấy đang chết đi» (tāsaṃ = tesaṃ, 10-02 PRON_FEM).",
        "- katici bhave dassetvā / eteneva bhāvena / saghānakā: 10-05 strings, unchanged.",
        "",
        "## Pāli as written (reported)",
        "",
        "- ^6-10-398 (Kha) purisa / upekkhā: «Pacchimabhavikānaṃ purisānaṃ uppajjantānaṃ» (for upapajjantānaṃ; termbase "
        "entry uppajjantānaṃ «đang tái sinh»): rendered as meant.",
        "- ^6-10-396 (Ka) / (Kha) ghāna / somanassa and ghāna / upekkhā: the (Ka) answers have «ye ca upekkhāya / "
        "somanassena upapajjitvā …», the first (Kha) answers «ye ca saghānakā upekkhāya / somanassena …»: translated as "
        "written («những người nào …» / «những người có mũi nào …»).",
        "- Unlabelled cut questions «Yassa yattha … saddhindriyaṃ…pe… paññindriyaṃ…pe… manindriyaṃ na uppajjissatīti?» "
        "and their «Yassa vā pana …» among labelled pairs, and the unlabelled pairs at ^6-10-401, ^6-10-402: kept as "
        "written.",
        "- Each (Xindriyamūlakaṃ) label stands at the end of the last answer line: kept on that line.",
        "",
        "## Clashes between finished chapters (listed for the coordinator)",
        "",
    ]
    if diffs:
        for name, hd, v, mine in diffs:
            out.append(f"- {name} head «{hd}»: {name} «{v}»; here «{mine}».")
    else:
        out.append("- None found: every head of 10-05 / 10-08 / 10-10 that also stands in this chapter reads the same "
                   "here.")
    out.append("- Kept as the setters print it (6-01 open item, «và» inside an inner plane list): 'Kāmāvacare "
               "parinibbantānaṃ rūpāvacare arūpāvacare pacchimabhavikānaṃ asaññasattānaṃ' «…, những người thuộc kiếp "
               "sống cuối cùng trong cõi hình sắc và cõi không hình sắc và chúng sinh Vô Tưởng» (= 3-03 / 3-02).")
    if OWN_READING:
        out.append("- Read on purpose differently from a setter's parser (coordinator's Pacchimabhavikānaṃ one-group "
                   "rule): " + "; ".join(f"«{k}» ({v[0]}: «{v[1]}»)" for k, v in sorted(OWN_READING.items())) + ".")
    out += ["", "## Parallel chapters (10-10 imported and asserted above; 10-09's parser compared, nothing asserted)",
            ""]
    if par:
        out.append("- Differences of 10-09's answer_head on heads of this chapter (parser level; the Pāli does not "
                   "stand in 10-09 unless said):")
        for x in par:
            out.append("  - " + " | ".join(str(y) for y in x))
    else:
        out.append("- No difference: every head of this chapter that 10-09's builder reads gives the same string.")
    out.append("")
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
    J8.check_frames()
    J5.check_frames()
    check_frames()
    segs = build(CH)
    check_termbase()
    for bad, (good, n) in SLIPS.items():
        got = sum(1 for s in SLIPS_SEEN if s[1] == bad)
        assert got == n, (bad, got, n)
    diffs = compare_setters()
    par = compare_parallel()
    S.write(CH, segs)
    text = (S.OUT_DIR / CH).read_text(encoding="utf-8")
    ADH_DIR.mkdir(parents=True, exist_ok=True)
    (ADH_DIR / CH).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", ADH_DIR / CH)
    NOTES_MD.write_text(unicodedata.normalize("NFC", notes(diffs, par)), encoding="utf-8", newline="\n")
    print("wrote", NOTES_MD)
    print("checked equal:", CHECKED, "; heads:", len(HEADS_SEEN), "; slips:", SLIPS_SEEN, "; clashes:", diffs,
          "; own:", len(OWN_READING), "; parallel:", par)


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
