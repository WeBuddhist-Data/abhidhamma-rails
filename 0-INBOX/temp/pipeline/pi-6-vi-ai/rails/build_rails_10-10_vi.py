"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 10-10 (Indriyayamaka 10: uppādavāra, (5) paccuppannānāgatavāro,
(Gha) paccanīkapuggalo and the cut (Ṅa) paccanīkaokāso).

Setters (all imported READ-ONLY with importlib; every shared string comes from their functions):
  build_rails_10-08_vi  (J8)  question12 (whole and cut pair questions, separate na), unit12 cuts, answer_head12 /
                              persons12 (Indriya heads), mind_gen12, pv_sentence12, tr_line (asserted equal where it
                              parses); through it 10-04 … 10-01, 9-01, 3-02, 3-01, 2-01, 7-01, 8, 5-01
  build_rails_10-05_vi  (J5)  ye_clause12 (Ye purisā / Yā itthiyo / sacakkhukā / saghānakā, eteneva bhāvena, katici
                              bhave dassetvā, somanassena / upekkhāya upapajjitvā), YE_CA_RE, YE_REL, pacchima_mind,
                              anantara_group, PACCHIMA_MIND
  build_rails_3-03_vi   (A3)  ye_ca_head / flat_persons / YE_TAILS / KHI_UPAPAJJANTA («…, khi những người ấy đang tái
                              sinh / đang chết đi»; several groups before "ye ca" joined flat «A, B và những người nào …»)
  build_rails_9-02_vi   (P92) gen_vi("Pacchimacittassa") «tâm cuối cùng», answer_head (asserted equal)
  build_rails_6-01_vi   (Q6)  anantara_group shape (cross-check of the «… ngay sau tâm này» ending)

New here (named constants; 10-09 and later Indriya chapters may import them):
  pacchima_gen               Somanassa- / Upekkhāsampayuttapacchimacittassa «tâm cuối cùng gắn liền với niềm vui / sự
                             bình thản» (termbase); Pacchimacittassa = 9-02 «tâm cuối cùng»
  SAMANGI_RE / samangi_person  upekkhāsampayuttapacchimacittasamaṅgīnaṃ «những người có được tâm cuối cùng gắn liền
                             với sự bình thản» (8 pacchimacittasamaṅgīnaṃ + termbase)
  that_mind_moment_x         yassa cittassa anantarā <X>pacchimacittaṃ uppajjissati tassa cittassa <moment>
                             «vào khoảnh khắc … của tâm mà ngay sau đó tâm cuối cùng gắn liền với … sẽ sinh khởi»
                             (9-01 that_mind_moment shape, asserted)
  PACCHIMA_ATTR / pacchima_sex_group   "Pacchimabhavikānaṃ itthīnaṃ upapajjantīnaṃ" «những người thuộc kiếp sống
                             cuối cùng đang tái sinh làm người nữ» (2-01 attribute, 10-02 sex word after the participle)
  YE_TAILS_X / ye_head       "P [P2] ye ca … [ye ca / yā ca …] tesaṃ cavantānaṃ / tesaṃ upapajjantānaṃ / tāsaṃ
                             upapajjantīnaṃ": one flat list (3-03), Indriya ye clauses (10-05), the tail (3-03)
  person_items / persons / head_parts / answer_head   heads (asserted equal to 10-08 / 3-02 / 3-03 / 9-02 where they
                             parse them)
  NOCA_X_RE / BOTH_X_RE / pv_sentence / unit / line / tr_line / build
A line, unit or word the parsers cannot place raises ValueError (no silent fallback). Importing writes nothing.

usage: python -I -X utf8 -B build_rails_10-10_vi.py   (probe: … build_rails_10-10_vi.py probe)
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
J5 = importlib.import_module("build_rails_10-05_vi")   # READ-ONLY: Ye-clauses with eteneva / katici, pacchima minds
A3 = importlib.import_module("build_rails_3-03_vi")    # READ-ONLY: "P ye ca … tesaṃ cavantānaṃ" heads (identical Pāli)
P92 = importlib.import_module("build_rails_9-02_vi")   # READ-ONLY: Pacchimacittassa «tâm cuối cùng»
Q6 = importlib.import_module("build_rails_6-01_vi")    # READ-ONLY: anantarā group shape (cross-check)
I4, I3, I2, I, A, A2, B, C, DY, D8 = J8.I4, J8.I3, J8.I2, J8.I, J8.A, J8.A2, J8.B, J8.C, J8.DY, J8.D8
assert J5.I4 is I4 and J5.I2 is I2 and J5.DY is DY and J5.B is B and J5.D8 is D8
assert A3.A2 is A2 and A3.B is B and A3.C is C and P92.DY is DY and P92.D is D8
D2 = A3.D                                              # build_rails_2-02_vi (KHI_CAVANTA, TE, YE_CA)

cap = S.cap
lc = I2.lc
CH = "10-10-indriyayamaka.md"
N = "10-10"
NOTES_MD = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/notes-rails-{N}.md"
ADH_DIR = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/adh-{N}"
M_IND = I.INDRIYA
PLANES = A.PLANES_AY
CHECKED = {"10-08 line": 0, "10-08 sentence": 0, "10-08 head": 0, "10-05 sentence": 0, "3-02 head": 0,
           "3-03 ye head": 0, "9-02 head": 0, "3-02 persons": 0}
HEADS_SEEN = {}
SLIPS_SEEN = []

# ===============================================================================================================
# 1. Slips and missing punctuation, rendered as meant (reported)
# ===============================================================================================================
SLIPS = {   # Pāli as printed → as parsed; count = expected occurrences
    "tesaṃ itthindriyaṃ na uppajjati no ca tesaṃ upekkhindriyaṃ":
        ("tesaṃ itthindriyaṃ na uppajjati, no ca tesaṃ upekkhindriyaṃ", 1),        # ^6-10-387 comma before no ca
    "manindriyaṃ na uppajjissati pacchimacittassa bhaṅgakkhaṇe":
        ("manindriyaṃ na uppajjissati. Pacchimacittassa bhaṅgakkhaṇe", 1),          # ^6-10-393 full stop missing
}
PLURAL_SLIP = "itthindriyaṃ na uppajjissanti"     # ^6-10-385 plural verb with a singular member: same Vietnamese


# ===============================================================================================================
# 2. Final minds, people possessed of them, "yassa cittassa anantarā … tassa cittassa <moment>"
# ===============================================================================================================
PACCHIMA_GEN_RE = re.compile(r"(somanassa|upekkhā)sampayuttapacchimacittassa")
SAMANGI_RE = re.compile(r"(somanassa|upekkhā)sampayuttapacchimacittasamaṅgīnaṃ")


def pacchima_gen(word):
    """Pacchimacittassa «tâm cuối cùng» (9-02); Somanassasampayuttapacchimacittassa «tâm cuối cùng gắn liền với niềm
    vui» (10-05 pacchima_mind = termbase); else 10-08 mind_gen12."""
    w = lc(word)
    if w == "pacchimacittassa":
        return P92.gen_vi(word)
    if PACCHIMA_GEN_RE.fullmatch(w):
        return J5.pacchima_mind(w[:-len("cittassa")] + "cittaṃ")
    return J8.mind_gen12(word)


def samangi_person(word):
    """upekkhāsampayuttapacchimacittasamaṅgīnaṃ «những người có được tâm cuối cùng gắn liền với sự bình thản»."""
    m = SAMANGI_RE.fullmatch(lc(word))
    if not m:
        raise ValueError(f"unknown samaṅgī word {word!r}")
    return f"{D8.PERSON['pacchimacittasamaṅgīnaṃ']} {I2.SAMPAYUTTA} {I2.FAC_MIND[m.group(1)]}"


THAT_MIND_REL = f"{D8.MIND} mà {DY.ANANTARA} đó"      # «tâm mà ngay sau đó …» (9-01 that_mind_moment)


def that_mind_moment_x(moment_loc, mind_word, verb_word):
    """yassa cittassa anantarā <X>pacchimacittaṃ uppajjissati tassa cittassa <moment> →
    «vào khoảnh khắc … của tâm mà ngay sau đó tâm cuối cùng gắn liền với … sẽ sinh khởi»."""
    return DY.moment_vi(moment_loc, f"{THAT_MIND_REL} {J5.pacchima_mind(mind_word)} {DY.verb(verb_word)[0]}")


assert DY.that_mind_moment("bhaṅgakkhaṇe") == DY.moment_vi("bhaṅgakkhaṇe", f"{THAT_MIND_REL} {DY.ATTAIN_TOP}")


# ===============================================================================================================
# 3. Person phrases
# ===============================================================================================================
PACCHIMA_ATTR = B.ATTRS["pacchimabhavikānaṃ"]         # «thuộc kiếp sống cuối cùng» (2-01; termbase)


def pacchima_sex_group(toks):
    """'Pacchimabhavikānaṃ itthīnaṃ upapajjantīnaṃ' → «những người thuộc kiếp sống cuối cùng đang tái sinh làm người
    nữ» (2-01 attribute before the participle, 10-02 sex / feeling word after it); None if not this shape."""
    low = [I2.PART_FEM.get(lc(t), lc(t)) for t in toks]
    if not low or low[0] != "pacchimabhavikānaṃ" or not any(t in I2.SEX or t in I2.FEEL for t in low):
        return None
    sex, feel, neg, part = None, None, False, None
    for t in low[1:]:
        if part:
            raise ValueError(f"word after the participle in {toks!r}")
        if t == "na":
            neg = True
        elif t in I2.SEX:
            sex, neg = I2.sex_vi(t, neg), False
        elif t in I2.FEEL:
            feel = I2.feel_vi(t)
        elif t in B.PARTICIPLES:
            part = t
        else:
            raise ValueError(f"unknown word {t!r} in {toks!r}")
    if neg or not part:
        raise ValueError(f"incomplete group {toks!r}")
    out = I2.ind_group(None, [PACCHIMA_ATTR], part, sex, feel)
    base = I2.ind_group(None, [PACCHIMA_ATTR], part)
    assert base == A2.ay_persons(f"Pacchimabhavikānaṃ {part}", PLANES), base     # 3-02 / 2-01 base group
    return out


def person_items(phrase):
    """Person phrase → list of Vietnamese items (joined flat by the caller). Without Indriya words: 3-03 flat_persons
    (= 3-02 ay_persons items); with them: one item per participle group (pacchima_sex_group, else 10-08 persons12)."""
    toks = phrase.split()
    if not any(lc(t) in I2.NEW_WORDS for t in toks):
        return A3.flat_persons(phrase, PLANES)
    items, cur = [], []
    for t in toks:
        cur.append(t)
        tl = lc(t)
        if tl in B.PARTICIPLES or tl in I2.PART_FEM:
            items.append(pacchima_sex_group(cur) or J8.persons12(" ".join(cur)))
            cur = []
    if cur:
        raise ValueError(f"dangling words {cur!r} in {phrase!r}")
    return items


def persons(phrase):
    out = B.join_and(person_items(phrase))
    try:
        old = A2.ay_persons(phrase, PLANES)
    except (ValueError, KeyError):
        old = None
    if old is not None:
        assert old == out, (phrase, old, out)
        CHECKED["3-02 persons"] += 1
    return out


# ===============================================================================================================
# 4. Ye heads: "P [P2] ye ca … [ye ca / yā ca …] [tesaṃ cavantānaṃ | tesaṃ upapajjantānaṃ | tāsaṃ upapajjantīnaṃ]"
# ===============================================================================================================
YE_TAILS_X = {**A3.YE_TAILS, " tāsaṃ upapajjantīnaṃ": A3.KHI_UPAPAJJANTA}   # tāsaṃ / -antīnaṃ = tesaṃ / -antānaṃ
assert I2.PRON_FEM["tāsaṃ"] == "tesaṃ" and I2.PART_FEM["upapajjantīnaṃ"] == "upapajjantānaṃ"
YE_SPLIT_RE = re.compile(r" (ye|yā) ca ")


def is_ye_head(head):
    return J5.is_ye_head(head)


def ye_head(head):
    """«Ở <P>, <P2>, những người nào … và những người nam nào …[, khi những người ấy đang chết đi]»: one flat list
    (3-03 / 3-02 list rule «A, B và C»), ye clauses by 10-05 ye_clause12, the tail by 3-03."""
    tail = next((t for t in YE_TAILS_X if head.endswith(t)), None)
    core = head[: -len(tail)] if tail else head
    pieces = YE_SPLIT_RE.split(core)          # [left, rel, clause, rel, clause, …]
    left = pieces[0]
    clauses = [("Yā " if rel == "yā" else "Ye ") + c for rel, c in zip(pieces[1::2], pieces[2::2])]
    if left.split()[0] in J5.YE_REL:
        items, first = [], [J5.ye_clause12(left)]
    else:
        items, first = person_items(left), []
    yes = first + [lc(J5.ye_clause12(c)) for c in clauses]
    body = B.join_and(items + yes)
    out = (f"{B.AT} {body}" if items else body) + (f", {YE_TAILS_X[tail]}" if tail else "")
    try:
        old = A3.ye_ca_head(head, PLANES)
    except (ValueError, KeyError):
        old = None
    if old is not None:
        assert old == out, ("3-03 ye head", head, old, out)
        CHECKED["3-03 ye head"] += 1
    return out


# ===============================================================================================================
# 5. Answer heads
# ===============================================================================================================
ANANTARA_WORDS = J5.ANANTARA_WORDS


def _special(toks):
    low = [lc(t) for t in toks]
    return any(t == "anantarā" or SAMANGI_RE.fullmatch(t) or t == "pacchimacittassa" or PACCHIMA_GEN_RE.fullmatch(t)
               for t in low)


def head_parts(head):
    """Heads with final minds / samaṅgī persons / anantarā phrases → parts joined «, » (9-01 shape; a person run after a
    time phrase keeps its own «ở»)."""
    toks = head.split()
    low = [lc(t) for t in toks]
    parts, run, buf, i = [], [], [], 0

    def flush_buf():
        if buf:
            run.extend(person_items(" ".join(buf)))
            buf.clear()

    def flush():
        flush_buf()
        if run:
            if len(run) > 1 and any(f" {C.AND} " in g for g in run):
                raise ValueError(f"«và» inside a group of a longer person run: {head!r}")
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
        buf.append(toks[i])
        i += 1
    flush()
    if not parts:
        raise ValueError(f"empty answer head {head!r}")
    return parts


def answer_head(head, loc):
    if loc in ("tattha",):
        return B.place_head(head, PLANES)
    if is_ye_head(head):
        out = ye_head(head)
    elif _special(head.split()):
        out = cap(", ".join(head_parts(head)))
        try:
            old = P92.answer_head(head, loc)
        except (ValueError, KeyError):
            old = None
        if old is not None:
            assert old == out, ("9-02 head", head, old, out)
            CHECKED["9-02 head"] += 1
    else:
        try:
            out = J8.answer_head12(head, loc)
            CHECKED["10-08 head"] += 1
        except ValueError:
            out = cap(f"{C.AT} {persons(head)}")
            try:
                old = A2.answer_head(head, loc, PLANES)
            except (ValueError, KeyError):
                old = None
            if old is not None:
                assert old == out, ("3-02 head", head, old, out)
                CHECKED["3-02 head"] += 1
    HEADS_SEEN[head] = out
    return out


# ===============================================================================================================
# 6. Sentences, units, lines
# ===============================================================================================================
LOCP = r"(tesaṃ|tāsaṃ)"
NOCA_X_RE = re.compile(r"(.+) " + LOCP + r" (\S+ (?:na )?\S+), no ca \2 (\S+ (?:na )?\S+)\.")
BOTH_X_RE = re.compile(r"(.+) " + LOCP + r" (\S+?ñca) ((?:na )?\S+) (\S+?ñca) ((?:na )?\S+)\.")


def pv_sentence(s, M=None):
    """Family B answers (2-01 b_noca / b_both) with this chapter's heads; the head is everything before the tesaṃ /
    tāsaṃ that opens the member clause (a ye-head tail «tesaṃ cavantānaṃ» stays in the head)."""
    M = M or M_IND
    if m := NOCA_X_RE.fullmatch(s):
        head, loc, c1, c2 = m.groups()
        a, v1 = I3.split_mv(c1, M)
        b, v2 = I3.split_mv(c2, M)
        out = B.b_noca(answer_head(head, loc), I2.PRON_FEM.get(loc, loc), a, v1, b, v2)
    elif m := BOTH_X_RE.fullmatch(s):
        head, loc, c1, v1, c2, v2 = m.groups()
        out = B.b_both(answer_head(head, loc), I2.PRON_FEM.get(loc, loc), M.subj(c1), I3.verb(v1), M.subj(c2),
                       I3.verb(v2))
    else:
        return None
    for name, f in (("10-08 sentence", J8.pv_sentence12), ("10-05 sentence", J5.pv_sentence12)):
        try:
            old = f(s, M)
        except (ValueError, KeyError, AssertionError):
            old = None
        if old is not None:
            assert old == out, (name, s, old, out)
            CHECKED[name] += 1
    return out


def unit(u, M=None):
    M = M or M_IND
    if (lab := I.ind_mulaka(u, M)) is not None:
        return lab
    if u.endswith(J8.CUT_AFTER_Q):
        return J8.question12(u[:-len(J8.CUT_AFTER_Q)], M) + S.PE
    if u.endswith("?"):
        return J8.question12(u[:-1], M)
    if u in B.SHORT:
        return B.SHORT[u]
    if "…" in u:
        raise ValueError(f"cut not set in this chapter: {u!r}")
    if (out := pv_sentence(u, M)) is not None:
        return out
    raise ValueError(f"unknown unit {u!r}")


def line(body, M=None):
    body, label = body.strip(), None
    if m := re.fullmatch(r"(.+?) (\(\w+mūlakaṃ\)\.?)", body):     # trailing (Xindriyamūlakaṃ) label (10-02)
        body, label = m.group(1), m.group(2)
    units = [x for x in re.split(r"(?<=[.?]) (?=\S)", body) if x]
    if label:
        units.append(label)
    return " ".join(unit(x, M) for x in units)


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
        if PLURAL_SLIP in body:
            SLIPS_SEEN.append((bid, PLURAL_SLIP, "(plural verb: «sẽ không sinh khởi» as the singular)"))
        out = line(body, M)
    full = f"{out} {bid}" if bid else out
    try:
        old = J8.tr_line(p, M, fixed)
    except (ValueError, KeyError, AssertionError):
        old = None
    if old is not None:
        assert old == full, ("10-08 line", p, old, full)
        CHECKED["10-08 line"] += 1
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
    ("Pacchimabhavikānaṃ", f"{B.PERSON.removeprefix('những ')} {PACCHIMA_ATTR}"), ("Pañcavokāre", PLANES["pañcavokār"][0]),
    ("Kāmāvacare", PLANES["kāmāvacar"][0]), ("arūpāvacare", PLANES["arūpāvacar"][0]),
    ("upapajjantīnaṃ", B.PARTICIPLES["upapajjantānaṃ"][0]), ("uppajjissanti", B.VERB["uppajjissati"][0]),
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
              "cavantānaṃ"):
        assert ye_head(h) == A3.ye_ca_head(h, PLANES), h
    # 10-05 ye clauses / heads unchanged where 10-05 has the same Pāli
    h = "Ye rūpāvacaraṃ upapajjitvā parinibbāyissanti ye ca purisā eteneva bhāvena katici bhave dassetvā parinibbāyissanti"
    assert ye_head(h) == J5.ye_head12(h), h
    h = "Rūpāvacarānaṃ ye ca purisā eteneva bhāvena katici bhave dassetvā parinibbāyissanti"
    assert ye_head(h) == J5.ye_head12(h), h
    # 9-02 final-mind heads; 9-01 anantarā endings; 6-01 group ending
    for h in ("Pacchimacittassa bhaṅgakkhaṇe", "Pacchimacittassa uppādakkhaṇe"):
        assert answer_head(h, "tesaṃ") == P92.answer_head(h, "tesaṃ"), h
    assert Q6.anantara_group(None, False).endswith(f" {DY.ANANTARA} {DY.THIS_MIND}")
    assert J5.anantara_group("upekkhāsampayuttapacchimacittaṃ", "uppajjissati").endswith(
        f" {DY.ANANTARA} {DY.THIS_MIND}")
    assert samangi_person("upekkhāsampayuttapacchimacittasamaṅgīnaṃ").startswith(D8.PERSON["pacchimacittasamaṅgīnaṃ"])
    assert I2.heading("(Gha) paccanīkapuggalo") == "(d) Chiều nghịch theo người"
    assert J8.CUT_AFTER_Q == "?…Pe…."


def compare_setters():
    """Identical Pāli heads in 10-05 / 10-08 (built in memory; nothing written) must read the same here."""
    diffs, seen, checked = [], dict(HEADS_SEEN), dict(CHECKED)
    for name, mod in (("10-05", J5), ("10-08", J8)):
        if not mod.HEADS_SEEN:
            mod.build(mod.CH)
        for h, v in list(mod.HEADS_SEEN.items()):
            try:
                mine = answer_head(h, "tesaṃ")
            except (ValueError, KeyError, AssertionError):
                continue
            if mine != v:
                diffs.append((name, h, v, mine))
    HEADS_SEEN.clear()
    HEADS_SEEN.update(seen)
    CHECKED.update(checked)
    return diffs


# ===============================================================================================================
# 8. Notes file (Pāli = tiếng Việt)
# ===============================================================================================================
def notes(diffs):
    M = M_IND
    out = []

    def row(p, v):
        out.append(f"{p} = {v}")

    def h(t):
        out.extend(["", f"## {t}", ""])

    out += [f"# pi-6 rails {N} (Indriyayamaka 10): (5) paccuppannānāgatavāro, (Gha) paccanīkapuggalo, (Ṅa) cut", "",
            "Builder: build_rails_10-10_vi.py (import with importlib). Setters: build_rails_10-08_vi (question12, "
            "answer_head12, persons12, mind_gen12, pv_sentence12, CUT_AFTER_Q, tr_line; through it 10-04 … 10-01, 9-01, "
            "3-02, 3-01, 2-01, 7-01, 8, 5-01), build_rails_10-05_vi (ye_clause12, YE_REL, pacchima_mind, "
            "anantara_group), build_rails_3-03_vi (ye_ca_head, flat_persons, YE_TAILS, KHI_UPAPAJJANTA), "
            "build_rails_9-02_vi (Pacchimacittassa), build_rails_6-01_vi (anantarā ending); all READ-ONLY. Every line "
            "10-08 parses, every sentence 10-08 / 10-05 parse, every head 10-08 / 3-02 / 3-03 / 9-02 parse is asserted "
            "byte-identical. Exposed: `SLIPS`, `PACCHIMA_GEN_RE`, `SAMANGI_RE`, `pacchima_gen`, `samangi_person`, "
            "`THAT_MIND_REL`, `that_mind_moment_x`, `PACCHIMA_ATTR`, `pacchima_sex_group`, `person_items`, `persons`, "
            "`YE_TAILS_X`, `ye_head`, `head_parts`, `answer_head`, `NOCA_X_RE`, `BOTH_X_RE`, `pv_sentence`, `unit`, "
            "`line`, `tr_line`, `build`. Format: Pāli = tiếng Việt.", ""]
    h("Headings")
    for t in ("(Gha) paccanīkapuggalo", "(Ṅa) paccanīkaokāso"):
        row(t, I2.heading(t))
    h("Verbs (2-01 VERB_TABLE, 9-01 separate na, coordinator after no ca)")
    for v in ("na uppajjati", "na uppajjissati", "na uppajjissanti"):
        row(v, I3.verb(v)[0])
    row("no ca tesaṃ B na uppajjissati", "nhưng ở những người ấy " + B.noca_vi("B", I3.verb("na uppajjissati")))
    row("no ca tesaṃ B na uppajjati", "nhưng ở những người ấy " + B.noca_vi("B", I3.verb("na uppajjati")))
    h("Questions (10-08 question12)")
    for q in ("(Ka) yassa cakkhundriyaṃ na uppajjati tassa sotindriyaṃ na uppajjissatīti",
              "(Kha) yassa vā pana sotindriyaṃ na uppajjissati tassa cakkhundriyaṃ na uppajjatīti",
              "Yassa cakkhundriyaṃ na uppajjati tassa saddhindriyaṃ…pe… paññindriyaṃ…pe… manindriyaṃ na uppajjissatīti",
              "Yassa saddhindriyaṃ na uppajjati tassa paññindriyaṃ…pe… manindriyaṃ na uppajjissatīti"):
        row(q + "?", J8.question12(q, M))
    row("Yattha cakkhundriyaṃ na uppajjati tattha sotindriyaṃ na uppajjissatīti?…Pe….",
        unit("Yattha cakkhundriyaṃ na uppajjati tattha sotindriyaṃ na uppajjissatīti?…Pe….", M))
    h("New: final minds, their possessors, «tâm mà ngay sau đó …» (9-01 that_mind_moment shape)")
    for hd in ("Pacchimacittassa bhaṅgakkhaṇe yassa cittassa anantarā upekkhāsampayuttapacchimacittaṃ uppajjissati "
               "tassa cittassa bhaṅgakkhaṇe",
               "Pacchimacittassa uppādakkhaṇe yassa cittassa anantarā somanassasampayuttapacchimacittaṃ uppajjissati "
               "tassa cittassa uppādakkhaṇe",
               "Somanassasampayuttapacchimacittassa bhaṅgakkhaṇe upekkhāsampayuttapacchimacittasamaṅgīnaṃ yassa cittassa "
               "anantarā somanassasampayuttapacchimacittaṃ uppajjissati tassa cittassa bhaṅgakkhaṇe",
               "Somanassasampayuttapacchimacittassa uppādakkhaṇe",
               "Upekkhāsampayuttapacchimacittassa bhaṅgakkhaṇe somanassasampayuttapacchimacittasamaṅgīnaṃ"):
        row(f"{hd} tesaṃ …", f"{answer_head(hd, 'tesaṃ')}, {C.THEN} {B.L['tesaṃ']} …")
    row("yassa cittassa anantarā <X>pacchimacittaṃ uppajjissati tassa cittassa <moment>",
        that_mind_moment_x("bhaṅgakkhaṇe", "upekkhāsampayuttapacchimacittaṃ", "uppajjissati"))
    h("New: Ye heads with Indriya clauses and a tail (3-03 flat list + 10-05 clauses)")
    for hd in ("Pañcavokāre parinibbantānaṃ arūpe pacchimabhavikānaṃ ye ca rūpāvacaraṃ arūpāvacaraṃ upapajjitvā "
               "parinibbāyissanti ye ca purisā eteneva bhāvena katici bhave dassetvā parinibbāyissanti tesaṃ cavantānaṃ",
               "Pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ ye ca sacakkhukā upekkhāya upapajjitvā parinibbāyissanti "
               "tesaṃ upapajjantānaṃ",
               "Kāmāvacare parinibbantānaṃ rūpāvacare arūpāvacare pacchimabhavikānaṃ ye ca somanassena upapajjitvā "
               "parinibbāyissanti tesaṃ cavantānaṃ",
               "Pacchimabhavikānaṃ itthīnaṃ upapajjantīnaṃ yā ca itthiyo rūpāvacaraṃ arūpāvacaraṃ upapajjitvā "
               "parinibbāyissanti yā ca itthiyo eteneva bhāvena katici bhave dassetvā parinibbāyissanti tāsaṃ "
               "upapajjantīnaṃ",
               "Pacchimabhavikānaṃ purisānaṃ upapajjantānaṃ ye ca purisā upekkhāya upapajjitvā parinibbāyissanti tesaṃ "
               "upapajjantānaṃ"):
        row(f"{hd} tesaṃ …", f"{answer_head(hd, 'tesaṃ')}, {C.THEN} {B.L['tesaṃ']} …")
    h("New: Pacchimabhavikānaṃ + sex word (2-01 attribute, 10-02 sex word after the participle)")
    for hd in ("Pacchimabhavikānaṃ itthīnaṃ upapajjantīnaṃ", "Pacchimabhavikānaṃ purisānaṃ upapajjantānaṃ"):
        row(f"{hd} tesaṃ …", f"{answer_head(hd, 'tesaṃ')}, {C.THEN} {B.L['tesaṃ']} …")
    h("Heads with locative planes (3-02 / 2-01 strings)")
    for hd in ("Pañcavokāre parinibbantānaṃ arūpe pacchimabhavikānaṃ",
               "Kāmāvacare parinibbantānaṃ rūpāvacare arūpāvacare pacchimabhavikānaṃ",
               "Pacchimabhavikānaṃ kāmāvacaraṃ upapajjantānaṃ"):
        row(f"{hd} tesaṃ …", f"{answer_head(hd, 'tesaṃ')}, {C.THEN} {B.L['tesaṃ']} …")
    h("Sample lines")
    for s in ("Sabbesaṃ cavantānaṃ acakkhukānaṃ upapajjantānaṃ tesaṃ cakkhundriyaṃ na uppajjati, no ca tesaṃ "
              "sotindriyaṃ na uppajjissati.",
              "Pacchimabhavikānaṃ itthīnaṃ upapajjantīnaṃ tāsaṃ jīvitindriyaṃ na uppajjissati, no ca tāsaṃ "
              "itthindriyaṃ na uppajjati.",
              "Pacchimacittassa bhaṅgakkhaṇe yassa cittassa anantarā upekkhāsampayuttapacchimacittaṃ uppajjissati tassa "
              "cittassa bhaṅgakkhaṇe tesaṃ jīvitindriyañca na uppajjati somanassindriyañca na uppajjissati."):
        row(s, line(s, M))
    h("Termbase misfits and gaps (for the coordinator)")
    out += [
        "- yassa cittassa anantarā <X>pacchimacittaṃ uppajjissati tassa cittassa <moment> (^6-10-389 … 391): not set "
        "before for a final mind; built on 9-01's that_mind_moment («vào khoảnh khắc … của tâm mà ngay sau đó sẽ đạt "
        "được con đường tối thượng») with 10-05's mind: «vào khoảnh khắc tan rã của tâm mà ngay sau đó tâm cuối cùng "
        "gắn liền với sự bình thản sẽ sinh khởi». Please confirm (10-06 / 10-07 / 10-12 may meet it).",
        "- <X>sampayuttapacchimacittasamaṅgīnaṃ: termbase «người có được tâm cuối cùng gắn liền với …», plural «những "
        "người …» as 8's pacchimacittasamaṅgīnaṃ.",
        "- Pacchimabhavikānaṃ itthīnaṃ upapajjantīnaṃ / purisānaṃ upapajjantānaṃ: «những người thuộc kiếp sống cuối "
        "cùng đang tái sinh làm người nữ / người nam» (attribute before the participle as 2-01 / 3-02, sex word after "
        "it as 10-02). New combination; please confirm.",
        "- Ye heads with several items (left groups + ye clauses): one flat list «A, B, những người nào … và những người "
        "nam nào …» (3-02 / 3-03 rule «A, B và C»; 10-05's ye_head12 would join a left part and two clauses with two "
        "«và»: see the clash list).",
        "- katici bhave dassetvā / eteneva bhāvena: 10-05 strings, unchanged.",
        "",
        "## Pāli as written (reported)",
        "",
        "- ^6-10-387 «… itthindriyaṃ na uppajjati no ca tesaṃ upekkhindriyaṃ …»: comma before «no ca» missing; added "
        "(7-05 rule).",
        "- ^6-10-393 «… manindriyaṃ na uppajjissati pacchimacittassa bhaṅgakkhaṇe …»: full stop missing between the two "
        "answers; rendered as two sentences.",
        "- ^6-10-385 «tesaṃ itthindriyaṃ na uppajjissanti» (plural verb with a singular member; the parallels have "
        "uppajjissati): Vietnamese has no number, «sẽ không sinh khởi».",
        "- ^6-10-388 the (Kha) somanassa answer runs over two Pāli lines: kept as two lines.",
        "- Unlabelled cut questions «Yassa … …pe… manindriyaṃ na uppajjissatīti?» among labelled ones: kept as written.",
        "- ^6-10-394 «Yattha …ti?…Pe….» = «… không?…» (9-01 / 10-08).",
        "",
        "## Clashes between finished chapters (listed for the coordinator)",
        "",
    ]
    if diffs:
        for name, hd, v, mine in diffs:
            out.append(f"- {name} head «{hd}»: {name} «{v}»; here «{mine}».")
    else:
        out.append("- None found: every head of 10-05 / 10-08 that this parser reads gives the same string.")
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
    S.write(CH, segs)
    text = (S.OUT_DIR / CH).read_text(encoding="utf-8")
    ADH_DIR.mkdir(parents=True, exist_ok=True)
    (ADH_DIR / CH).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", ADH_DIR / CH)
    NOTES_MD.write_text(unicodedata.normalize("NFC", notes(diffs)), encoding="utf-8", newline="\n")
    print("wrote", NOTES_MD)
    print("checked equal:", CHECKED, "; heads:", len(HEADS_SEEN), "; slips:", SLIPS_SEEN, "; clashes:", diffs)


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
