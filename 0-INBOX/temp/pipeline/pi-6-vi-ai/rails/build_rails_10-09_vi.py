"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 10-09 (Indriyayamaka 9: uppādavāra, (5) paccuppannānāgatavāro,
(Ka) anulomapuggalo, (Kha) anulomaokāso, (Ga) anulomapuggalokāsā).

Setters (all imported READ-ONLY with importlib; every shared string comes from their functions):
  build_rails_10-08_vi  (M8)  nearest setter: question12, persons12, head_parts12 pieces, answer_head12, pv_sentence12,
                              unit12 / line12 / tr_line (asserted equal wherever it parses a line, head or sentence)
  build_rails_10-05_vi  (M5)  Ye-clauses with eteneva bhāvena / katici bhave dassetvā (ye_clause12, ye_head12,
                              YE_CA_RE, YE_REL), PACCHIMA_MIND / pacchima_mind / ANANTARA_REL / anantara_group
  build_rails_10-04 … 10-01, 9-01, 5-01, 3-02, 3-01, 2-01, 7-01, 8 (through M8: I4, I3, I2, I, DY, T5, A2, A, B, C, D8)
  build_rails_3-03_vi   (A3)  "P ye ca … parinibbāyissanti tesaṃ upapajjantānaṃ" (KHI_UPAPAJJANTA, flat_persons,
                              ye_ca_head: asserted equal wherever it parses)
  build_rails_3-04_vi   (A4)  LIKEWISE «giống như vậy» (sadisaṃ)

New here (named constants; later Indriya chapters import them):
  YE_TAILS13 / ye_head13      "P ye ca … [ye ca / yā ca …] parinibbāyissanti tesaṃ upapajjantānaṃ / tāsaṃ
                              upapajjantīnaṃ": 10-05's clauses joined flat with P (3-03 / 10-05) + 3-03's
                              «, khi những người ấy đang tái sinh» (tāsaṃ upapajjantīnaṃ = the same: no gender)
  group13 / persons13         pacchimabhavikānaṃ + sex word: «những người thuộc kiếp sống cuối cùng đang tái sinh làm
                              người nữ» (2-01 ATTRS + 10-02 ind_group); anything else = 10-08 persons12 / 3-02 ay_persons
  PACCHIMA_GEN_RE / mind_gen13  Pacchimacittassa «tâm cuối cùng» (8); Somanassa- / Upekkhāsampayuttapacchimacittassa
                              «tâm cuối cùng gắn liền với niềm vui / sự bình thản» (termbase = 10-05 pacchima_mind)
  that_mind_moment13          yassa cittassa anantarā <X>pacchimacittaṃ uppajjissati tassa cittassa uppādakkhaṇe
                              «vào khoảnh khắc sinh khởi của tâm mà ngay sau đó tâm cuối cùng gắn liền với … sẽ sinh
                              khởi» (9-01 that_mind_moment with the 10-05 final mind in place of «sẽ đạt được con
                              đường tối thượng»)
  head_parts13 / answer_head13 / NOCA13_RE / BOTH13_RE / pv_sentence13 / SADISA_NOTE / unit13 / line13 / tr_line / build
A line, unit or word the parsers cannot place raises ValueError (no silent fallback). Importing writes nothing.

usage: python -I -X utf8 -B build_rails_10-09_vi.py   (probe: … build_rails_10-09_vi.py probe)
"""
import importlib
import re
import sys
import unicodedata

RAILS_DIR = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\rails"
if RAILS_DIR not in sys.path:
    sys.path.insert(0, RAILS_DIR)
import build_rails_sample_vi as S  # noqa: E402  (READ-ONLY)
M8 = importlib.import_module("build_rails_10-08_vi")   # READ-ONLY: nearest setter
M5 = importlib.import_module("build_rails_10-05_vi")   # READ-ONLY: Ye / eteneva / final-mind strings
A3 = importlib.import_module("build_rails_3-03_vi")    # READ-ONLY: "P ye ca … tesaṃ upapajjantānaṃ"
A4 = importlib.import_module("build_rails_3-04_vi")    # READ-ONLY: sadisaṃ «giống như vậy»
J10 = importlib.import_module("build_rails_10-10_vi")  # READ-ONLY: finished sibling (coordinator: align byte for byte)
I4, I3, I2, I, A, B, C, DY = M8.I4, M8.I3, M8.I2, M8.I, M8.A, M8.B, M8.C, M8.DY
A2, D8, T5 = M8.A2, M8.D8, M8.T5
assert M5.I4 is I4 and M5.A3 is A3 and A3.A2 is A2 and A3.B is B and M5.DY is DY and M5.D8 is D8
assert J10.J8 is M8 and J10.J5 is M5 and J10.A3 is A3

cap = S.cap
lc = I2.lc
CH = "10-09-indriyayamaka.md"
N = "10-09"
NOTES_MD = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/notes-rails-{N}.md"
ADH_DIR = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/adh-{N}"
M_IND = I.INDRIYA
PLANES = A.PLANES_AY
CHECKED = {"10-08 line": 0, "10-05 line": 0, "10-08 head": 0, "10-05 head": 0, "10-08 sentence": 0,
           "10-05 sentence": 0, "3-03 ye ca": 0, "10-05 ye": 0, "10-08 persons": 0, "3-02 persons": 0,
           "10-10 pieces": 0, "10-10 ye": 0, "10-10 head": 0, "10-10 line": 0}
HEADS_SEEN = {}
NEW_HEADS = {}           # heads none of the setters can parse (new shapes here)
SLIPS_SEEN = []
SETTER_FAIL = {}         # setter raised an AssertionError of its own on a line / head (listed)
CLASH = {}               # a setter parses a head / line differently (raises: never silent)

# ===============================================================================================================
# 1. Slips rendered as meant (reported in the notes); value: (as parsed, expected count)
# ===============================================================================================================
SLIPS = {
    "somanassindriyaṃ uppajjissati, tassa purisindriyaṃ": ("somanassindriyaṃ uppajjissati tassa purisindriyaṃ", 1),
    "tesaṃ tattha manindriyaṃ uppajjissati cakkhundriyañca uppajjati.":
        ("tesaṃ tattha manindriyañca uppajjissati cakkhundriyañca uppajjati.", 1),
}

# ===============================================================================================================
# 2. Kinds of mind: the final mind (8 «tâm cuối cùng»; termbase «tâm cuối cùng gắn liền với …» = 10-05)
# ===============================================================================================================
PACCHIMA_GEN_RE = re.compile(r"((?:somanassa|upekkhā)sampayutta)?pacchimacittassa")


def mind_gen13(word):
    m = PACCHIMA_GEN_RE.fullmatch(lc(word))
    if not m:
        return M8.mind_gen12(word)
    if not m.group(1):
        out = D8.mind_gen_vi(word)                               # Pacchimacittassa «tâm cuối cùng» (8 / 9-02)
    else:
        out = M5.pacchima_mind(m.group(1) + "pacchimacittaṃ")   # = termbase -sampayuttapacchimacittassa
    assert out == J10.pacchima_gen(word), (word, out)           # 10-10 pacchima_gen
    CHECKED["10-10 pieces"] += 1
    return out


def that_mind_moment13(moment_word, mind_word, verb_word):
    """yassa cittassa anantarā <X>pacchimacittaṃ <verb> tassa cittassa <moment> → 9-01 that_mind_moment with the
    final mind and its verb in place of «sẽ đạt được con đường tối thượng»."""
    base = DY.that_mind_moment(moment_word)
    assert base.count(DY.ATTAIN_TOP) == 1 and base.endswith(f"{D8.MIND} {M5.ANANTARA_REL} {DY.ANANTARA} đó "
                                                            f"{DY.ATTAIN_TOP}"), base
    out = base.replace(DY.ATTAIN_TOP, f"{M5.pacchima_mind(mind_word)} {DY.verb(verb_word)[0]}")
    assert out == J10.that_mind_moment_x(moment_word, mind_word, verb_word), out    # 10-10
    CHECKED["10-10 pieces"] += 1
    return out


# ===============================================================================================================
# 3. Person groups and heads
# ===============================================================================================================
PACCHIMABHAVIKA = "pacchimabhavikānaṃ"


def group13(toks):
    """pacchimabhavikānaṃ + sex / feeling word + participle (no plane) → 10-02 ind_group with 2-01's attribute
    «thuộc kiếp sống cuối cùng»: «những người thuộc kiếp sống cuối cùng đang tái sinh làm người nữ»."""
    head = " ".join(toks)
    pre, sex, feel, neg, part = [], None, None, False, None
    for t in toks:
        tl = lc(t)
        if part:
            raise ValueError(f"word after the participle in {head!r}")
        if tl == "na":
            neg = True
        elif tl in B.ATTRS:
            if pre or sex or neg:
                raise ValueError(f"misplaced attribute {t!r} in {head!r}")
            pre.append(B.ATTRS[tl])
        elif tl in I2.SEX:
            if sex:
                raise ValueError(f"two sex words in {head!r}")
            sex, neg = I2.sex_vi(tl, neg), False
        elif tl in I2.FEEL:
            if feel or neg:
                raise ValueError(f"misplaced {t!r} in {head!r}")
            feel = I2.feel_vi(tl)
        elif tl in B.PARTICIPLES or tl in I2.PART_FEM:
            if neg:
                raise ValueError(f"dangling na in {head!r}")
            part = I2.PART_FEM.get(tl, tl)
        else:
            raise ValueError(f"unknown word {t!r} in person group {head!r}")
    if not part or not pre:
        raise ValueError(f"not a pacchimabhavika group {head!r}")
    base = I2.ind_group(None, pre, part)
    assert base == A2.ay_persons(f"Pacchimabhavikānaṃ {part}", PLANES), (head, base)   # 3-02 «… đang tái sinh»
    out = I2.ind_group(None, pre, part, sex, feel)
    assert out == J10.pacchima_sex_group(toks), (head, out)     # 10-10 pacchima_sex_group
    CHECKED["10-10 pieces"] += 1
    NEW_HEADS.setdefault(head, out)
    return out


def persons13(phrase):
    """Genitive person phrase (no «Ở»): with pacchimabhavikānaṃ + an Indriya word = group13 per group, joined flat;
    else 10-08 persons12, else 3-02 ay_persons (the Āyatana shapes with pacchimabhavikānaṃ and planes)."""
    toks = phrase.split()
    low = [lc(t) for t in toks]
    if PACCHIMABHAVIKA in low and any(t in I2.NEW_WORDS for t in low):
        groups, cur = [], []
        for t in toks:
            cur.append(t)
            if lc(t) in B.PARTICIPLES or lc(t) in I2.PART_FEM:
                groups.append(group13(cur) if PACCHIMABHAVIKA in [lc(x) for x in cur] else M8.persons12(" ".join(cur)))
                cur = []
        if cur:
            raise ValueError(f"dangling words {cur!r} in {phrase!r}")
        return B.join_and(groups)
    try:
        out = M8.persons12(phrase)
        CHECKED["10-08 persons"] += 1
        return out
    except (ValueError, KeyError):
        pass
    out = A2.ay_persons(phrase, PLANES)
    CHECKED["3-02 persons"] += 1
    return out


def _span_tok(t):
    return M8._span_tok(t) or lc(t) == PACCHIMABHAVIKA


ANANTARA_WORDS = M5.ANANTARA_WORDS         # yassa cittassa anantarā


def head_parts13(head):
    """Answer head → parts joined «, » (9-01 / 10-08 shape) + the final-mind moments, the anantarā moment
    (that_mind_moment13) or person group (10-05 anantara_group), pacchimabhavikānaṃ person spans."""
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
        if [lc(x) for x in toks[i:i + 3]] == ANANTARA_WORDS:
            if i + 4 >= len(toks):
                raise ValueError(f"short anantarā phrase in {head!r}")
            mind_w, verb_w = toks[i + 3], toks[i + 4]
            if toks[i + 5:i + 7] == ["tassa", "cittassa"]:
                if i + 7 >= len(toks) or lc(toks[i + 7]) not in D8.MOMENT:
                    raise ValueError(f"'tassa cittassa' without a moment in {head!r}")
                flush()
                parts.append(that_mind_moment13(toks[i + 7], mind_w, verb_w))
                i += 8
            else:
                run.append(M5.anantara_group(mind_w, verb_w))
                i += 5
        elif before_moment(i):
            flush()
            parts.append(DY.moment_vi(toks[i + 1], mind_gen13(t)))
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
            run.append(persons13(" ".join(toks[i:j])))
            i = j
        else:
            raise ValueError(f"unknown word {t!r} in answer head {head!r}")
    flush()
    if not parts:
        raise ValueError(f"empty answer head {head!r}")
    return parts


# "P ye ca … parinibbāyissanti tesaṃ upapajjantānaṃ / tāsaṃ upapajjantīnaṃ" (3-03; tāsaṃ = tesaṃ, upapajjantīnaṃ =
# upapajjantānaṃ: Vietnamese has no gender, 10-02)
YE_TAILS13 = {" tesaṃ upapajjantānaṃ": A3.KHI_UPAPAJJANTA, " tāsaṃ upapajjantīnaṃ": A3.KHI_UPAPAJJANTA}
assert I2.PRON_FEM["tāsaṃ"] == "tesaṃ" and I2.PART_FEM["upapajjantīnaṃ"] == "upapajjantānaṃ"
assert set(A3.YE_TAILS) >= {" tesaṃ upapajjantānaṃ"}


def ye_head13(head):
    """'P ye ca … [ye ca / yā ca …] [tail]' → «Ở P, <clause> và <clause>[, khi những người ấy đang tái sinh]»:
    10-05 ye_head12 (clauses from ye_clause12, P joined flat as 3-03) + 3-03's tail; asserted equal to 10-05
    ye_head12 (without the tail) and 3-03 ye_ca_head (with it) wherever they parse the head."""
    tail = next((t for t in YE_TAILS13 if head.endswith(t)), None)
    core = head[:-len(tail)] if tail else head
    parts = M5.YE_CA_RE.split(core)
    clauses = [lc(M5.ye_clause12(("Yā " if mm.group(0).strip().startswith("yā") else "Ye ") + p))
               for mm, p in zip(M5.YE_CA_RE.finditer(core), parts[1:])]
    if core.split()[0] in M5.YE_REL:
        out = f" {C.AND} ".join([M5.ye_clause12(parts[0])] + clauses)
    else:
        try:
            flat = A3.flat_persons(parts[0], PLANES)
        except (ValueError, KeyError):
            flat = [persons13(parts[0])]
            if f" {C.AND} " in flat[0]:
                raise ValueError(f"«và» inside the persons before 'ye ca': {head!r}")
        out = f"{B.AT} {B.join_and(flat + clauses)}"
    try:
        old = M5.ye_head12(core)
    except (ValueError, KeyError):
        old = None
    if old is not None:
        assert old == out, ("10-05 ye", core, old, out)
        CHECKED["10-05 ye"] += 1
    if tail:
        out += f", {YE_TAILS13[tail]}"
    try:
        old = A3.ye_ca_head(head, PLANES)
    except (ValueError, KeyError):
        old = None
    if old is not None:
        assert old == out, ("3-03 ye ca", head, old, out)
        CHECKED["3-03 ye ca"] += 1
    assert out == J10.ye_head(head), ("10-10 ye", head, out)     # 10-10 ye_head (flat list + tail)
    CHECKED["10-10 ye"] += 1
    return out


def answer_head13(head, loc):
    if loc in ("tattha",):
        return B.place_head(head, PLANES)
    if M5.YE_CA_RE.search(head) or head.split()[0] in M5.YE_REL:
        out = ye_head13(head)
    else:
        out = cap(", ".join(head_parts13(head)))
    parsed = False
    for name, f in (("10-08 head", lambda: M8.answer_head12(head, loc)),
                    ("10-05 head", lambda: M5.answer_head12(head, loc)),
                    ("10-10 head", lambda: J10.answer_head(head, loc))):
        try:
            old = f()
        except (ValueError, KeyError):
            continue
        except AssertionError as e:          # the setter's own cross-check fails on this head
            SETTER_FAIL.setdefault(head, (name, str(e)[:300]))
            continue
        parsed = True
        if old != out:
            CLASH[head] = (name, old, out)
            raise AssertionError((name, head, old, out))
        CHECKED[name] += 1
    if not parsed:
        NEW_HEADS.setdefault(head, out)
    HEADS_SEEN[head] = out
    return out


# ===============================================================================================================
# 4. Sentences, units, lines
# ===============================================================================================================
# the head ends before the pronoun that is followed by a member word (a "tesaṃ upapajjantānaṃ" tail stays in the head)
_MEM = r"(?=\S+ndriya(?:ṃ|ñca) )"           # cakkhundriyaṃ, ghānindriyañca …
NOCA13_RE = re.compile(r"(.+?) " + I2.LOCP + " " + _MEM + r"(.+?), no ca \2 (.+?)\.")
BOTH13_RE = re.compile(r"(.+?) " + I2.LOCP + " " + _MEM + r"(\S+?ñca) ((?:na )?\S+) (\S+?ñca) ((?:na )?\S+)\.")


def pv_sentence13(s, M=None):
    """Family B answers (2-01 b_noca / b_both) with answer_head13 and 10-03's member / verb split."""
    M = M or M_IND
    if m := NOCA13_RE.fullmatch(s):
        head, loc, c1, c2 = m.groups()
        a, v1 = I3.split_mv(c1, M)
        b, v2 = I3.split_mv(c2, M)
        out = B.b_noca(answer_head13(head, loc), I2.PRON_FEM.get(loc, loc), a, v1, b, v2)
    elif m := BOTH13_RE.fullmatch(s):
        head, loc, c1, v1, c2, v2 = m.groups()
        out = B.b_both(answer_head13(head, loc), I2.PRON_FEM.get(loc, loc), M.subj(c1), I3.verb(v1), M.subj(c2),
                       I3.verb(v2))
    else:
        return None
    for name, f in (("10-08 sentence", lambda: M8.pv_sentence12(s, M)), ("10-05 sentence", lambda: M5.pv_sentence12(s, M))):
        try:
            old = f()
        except (ValueError, KeyError):
            continue
        except AssertionError as e:
            SETTER_FAIL.setdefault(s[:80], (name, str(e)[:300]))
            continue
        if old is None:
            continue
        assert old == out, (name, s, old, out)
        CHECKED[name] += 1
    return out


SADISA_PALI = "(Sadisaṃ )"
SADISA_NOTE = f"({cap(A4.LIKEWISE)})"       # (Sadisaṃ ) «(Giống như vậy)»: the same as the pair before (3-04)


def unit13(u, M=None):
    M = M or M_IND
    if u == SADISA_PALI:
        return SADISA_NOTE
    if (lab := I.ind_mulaka(u, M)) is not None:
        return lab
    if u.endswith(M8.CUT_AFTER_Q):
        return M8.question12(u[:-len(M8.CUT_AFTER_Q)], M) + S.PE
    if u.endswith("?"):
        return M8.question12(u[:-1], M)
    if u in B.SHORT:
        return B.SHORT[u]
    if "…" in u:
        raise ValueError(f"cut not set in this chapter: {u!r}")
    if (out := pv_sentence13(u, M)) is not None:
        return out
    raise ValueError(f"unknown unit {u!r}")


def line13(body, M=None):
    body, label = body.strip(), None
    if m := re.fullmatch(r"(.+?) (\(\w+mūlakaṃ\)\.?)", body):     # trailing (Xindriyamūlakaṃ) label (10-02)
        body, label = m.group(1), m.group(2)
    units = [x for x in re.split(r"(?<=[.?]) (?=\S)", body) if x]
    if label:
        units.append(label)
    return " ".join(unit13(x, M) for x in units)


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
        out = line13(body, M)
    full = f"{out} {bid}" if bid else out
    for name, f in (("10-08 line", lambda: M8.tr_line(p, M, fixed)), ("10-05 line", lambda: M5.tr_line(p, M, fixed)),
                    ("10-10 line", lambda: J10.tr_line(p, M, fixed))):
        try:
            old = f()
        except (ValueError, KeyError):
            continue
        except AssertionError as e:
            SETTER_FAIL.setdefault(p[:80], (name, str(e)[:300]))
            continue
        assert old == full, (name, p, old, full)
        CHECKED[name] += 1
    return full


def build(name, M=None, fixed=None):
    return [[tr_line(ln, M, fixed) for ln in seg] for seg in S.segments_of(name)]


# ===============================================================================================================
# 5. Checks
# ===============================================================================================================
TERMBASE_USED = [   # pi-6 termbase entries used verbatim («Pāli: {…: Vietnamese}»)
    ("Pacchimabhavikānaṃ", f"người {B.ATTRS[PACCHIMABHAVIKA]}"),
    ("Pacchimacittassa", mind_gen13("Pacchimacittassa")),
    ("Pacchimacittassa uppādakkhaṇe", f"{D8.MOMENT['uppādakkhaṇe']} {D8.OF} {mind_gen13('Pacchimacittassa')}"),
    ("Somanassasampayuttapacchimacittassa uppādakkhaṇe",
     f"{D8.MOMENT['uppādakkhaṇe']} {D8.OF} {mind_gen13('Somanassasampayuttapacchimacittassa')}"),
    ("Upekkhāsampayuttapacchimacittassa uppādakkhaṇe",
     f"{D8.MOMENT['uppādakkhaṇe']} {D8.OF} {mind_gen13('Upekkhāsampayuttapacchimacittassa')}"),
    ("upekkhāsampayuttapacchimacittaṃ", M5.pacchima_mind("upekkhāsampayuttapacchimacittaṃ")),
    ("somanassasampayuttapacchimacittaṃ", M5.pacchima_mind("somanassasampayuttapacchimacittaṃ")),
    ("uppajjissati", DY.verb("uppajjissati")[0]), ("Itarāsaṃ", "người khác"), ("itthiyo", M5.YE_NOUN["itthiyo"]),
    ("purisā", M5.YE_NOUN["purisā"]), ("upapajjantīnaṃ", B.PARTICIPLES["upapajjantānaṃ"][0]),
    ("saddhāsampayuttacittassa uppādakkhaṇe",
     f"{D8.MOMENT['uppādakkhaṇe']} {D8.OF} {mind_gen13('saddhāsampayuttacittassa')}"),
    ("saddhāvippayuttacittassa uppādakkhaṇe",
     f"{D8.MOMENT['uppādakkhaṇe']} {D8.OF} {mind_gen13('saddhāvippayuttacittassa')}"),
    ("upekkhāvippayuttacittassa uppādakkhaṇe",
     f"{D8.MOMENT['uppādakkhaṇe']} {D8.OF} {mind_gen13('upekkhāvippayuttacittassa')}"),
]


def check_termbase():
    tb = I2.termbase_text()
    bad = [(p, v) for p, v in TERMBASE_USED
           if not re.search(rf"^{re.escape(p)}: {{.*: {re.escape(v)}}}$", tb, re.M)]
    assert not bad, "termbase entries not matched: " + repr(bad)
    M8.check_termbase()


def check_frames():
    assert mind_gen13("Pacchimacittassa") == f"{D8.MIND} {D8.FINAL}" == M5.PACCHIMA_MIND
    assert mind_gen13("cittassa") == D8.MIND
    assert DY.that_mind_moment("uppādakkhaṇe").startswith(DY.moment_vi("uppādakkhaṇe", D8.MIND))
    hd = "Pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti tesaṃ upapajjantānaṃ"
    assert ye_head13(hd) == A3.ye_ca_head(hd, PLANES)
    hd = "Pacchimabhavikānaṃ kāmāvacaraṃ upapajjantānaṃ rūpāvacaraṃ upapajjantānaṃ"
    assert answer_head13(hd, "tesaṃ tattha") == f"{B.AT} {A2.ay_persons(hd, PLANES)}"
    assert A3.KHI_UPAPAJJANTA == f"khi {A3.D.TE} {B.PARTICIPLES['upapajjantānaṃ'][0]}"
    assert SADISA_NOTE == "(Giống như vậy)"


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

    out += [f"# pi-6 rails {N} (Indriyayamaka 9): (5) paccuppannānāgatavāro (present + future), (Ka) … (Ga)", "",
            "Builder: build_rails_10-09_vi.py (import with importlib). Setters: build_rails_10-08_vi (question12, "
            "persons12, answer_head12, pv_sentence12, tr_line; through it 10-04 … 10-01, 9-01, 5-01, 3-02, 3-01, 2-01, "
            "7-01, 8), build_rails_10-05_vi (ye_clause12, ye_head12, YE_CA_RE, pacchima_mind, ANANTARA_REL, "
            "anantara_group), build_rails_3-03_vi (KHI_UPAPAJJANTA, flat_persons, ye_ca_head), build_rails_3-04_vi "
            "(LIKEWISE), build_rails_10-10_vi (pacchima_gen, that_mind_moment_x, pacchima_sex_group, ye_head, "
            "answer_head, tr_line; coordinator: 10-09 aligns to 10-10); all READ-ONLY. Every line / head / sentence "
            "10-08, 10-05 or 10-10 parse and every head 3-03 parses is asserted byte-identical; mind_gen13, "
            "that_mind_moment13, group13 and ye_head13 are asserted equal to 10-10's pacchima_gen, that_mind_moment_x, "
            "pacchima_sex_group and ye_head on every call. Exposed: `SLIPS`, `PACCHIMA_GEN_RE`, `mind_gen13`, `that_mind_moment13`, "
            "`group13`, `persons13`, `head_parts13`, `YE_TAILS13`, `ye_head13`, `answer_head13`, `NOCA13_RE`, "
            "`BOTH13_RE`, `pv_sentence13`, `SADISA_PALI`, `SADISA_NOTE`, `unit13`, `line13`, `tr_line`, `build`. "
            "Format: Pāli = tiếng Việt.", ""]
    h("Headings")
    for t in ("(Ka) anulomapuggalo", "(Kha) anulomaokāso", "(Ga) anulomapuggalokāsā"):
        row(t, I2.heading(t))
    h("Verbs and questions (present + future)")
    for v in ("uppajjati", "uppajjissati"):
        row(v, I3.verb(v)[0])
    row("no ca tesaṃ B uppajjissati", "nhưng ở những người ấy " + B.noca_vi("B", I3.verb("uppajjissati")))
    for q in ("(Ka) yassa cakkhundriyaṃ uppajjati tassa sotindriyaṃ uppajjissatīti",
              "(Kha) yassa vā pana sotindriyaṃ uppajjissati tassa cakkhundriyaṃ uppajjatīti",
              "Yassa cakkhundriyaṃ uppajjati tassa saddhindriyaṃ…pe… paññindriyaṃ…pe… manindriyaṃ uppajjissatīti",
              "Yassa saddhindriyaṃ uppajjati tassa paññindriyaṃ…pe… manindriyaṃ uppajjissatīti",
              "(Ka) yassa yattha cakkhundriyaṃ uppajjati tassa tattha sotindriyaṃ uppajjissatīti"):
        row(q + "?", M8.question12(q, M))
    row("Yattha cakkhundriyaṃ uppajjati tattha sotindriyaṃ uppajjissatīti?…Pe….",
        unit13("Yattha cakkhundriyaṃ uppajjati tattha sotindriyaṃ uppajjissatīti?…Pe….", M))
    row(SADISA_PALI, SADISA_NOTE + f" (3-04 sadisaṃ with one subject «{A4.LIKEWISE}»)")
    h("New: 'P ye ca … parinibbāyissanti tesaṃ upapajjantānaṃ / tāsaṃ upapajjantīnaṃ' with 10-05's clauses")
    for hd in ("Pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti tesaṃ "
               "upapajjantānaṃ",
               "Pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ ye ca rūpāvacaraṃ arūpāvacaraṃ upapajjitvā "
               "parinibbāyissanti ye ca purisā eteneva bhāvena katici bhave dassetvā parinibbāyissanti tesaṃ "
               "upapajjantānaṃ",
               "Pacchimabhavikānaṃ kāmāvacaraṃ upapajjantānaṃ ye ca rūpāvacaraṃ arūpāvacaraṃ upapajjitvā "
               "parinibbāyissanti yā ca itthiyo eteneva bhāvena katici bhave dassetvā parinibbāyissanti tesaṃ "
               "upapajjantānaṃ",
               "Pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ ye ca sacakkhukā upekkhāya upapajjitvā "
               "parinibbāyissanti tesaṃ upapajjantānaṃ",
               "Pacchimabhavikānaṃ itthīnaṃ upapajjantīnaṃ yā ca itthiyo rūpāvacaraṃ arūpāvacaraṃ upapajjitvā "
               "parinibbāyissanti yā ca itthiyo eteneva bhāvena katici bhave dassetvā parinibbāyissanti tāsaṃ "
               "upapajjantīnaṃ",
               "Pacchimabhavikānaṃ purisānaṃ upapajjantānaṃ ye ca purisā somanassena upapajjitvā parinibbāyissanti "
               "tesaṃ upapajjantānaṃ",
               "Pacchimabhavikānaṃ kāmāvacaraṃ upapajjantānaṃ rūpāvacaraṃ upapajjantānaṃ yā ca itthiyo eteneva "
               "bhāvena katici bhave dassetvā parinibbāyissanti tāsaṃ upapajjantīnaṃ"):
        row(f"{hd} tesaṃ …", f"{answer_head13(hd, 'tesaṃ')}, {C.THEN} {B.L['tesaṃ']} …")
    h("New: pacchimabhavikānaṃ with a sex word (2-01 attribute + 10-02 sex word)")
    for hd in ("Pacchimabhavikānaṃ itthīnaṃ upapajjantīnaṃ", "Pacchimabhavikānaṃ purisānaṃ upapajjantānaṃ",
               "Pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ", "Pacchimabhavikānaṃ kāmāvacaraṃ upapajjantānaṃ"):
        row(f"{hd} tesaṃ …", f"{answer_head13(hd, 'tesaṃ')}, {C.THEN} {B.L['tesaṃ']} …")
    h("New: final-mind moments and the anantarā moment (9-01 that_mind_moment shape; 10-05 final minds)")
    for hd in ("Pacchimacittassa uppādakkhaṇe",
               "Somanassasampayuttapacchimacittassa uppādakkhaṇe", "Upekkhāsampayuttapacchimacittassa uppādakkhaṇe",
               "Pacchimacittassa uppādakkhaṇe yassa cittassa anantarā upekkhāsampayuttapacchimacittaṃ uppajjissati "
               "tassa cittassa uppādakkhaṇe",
               "Somanassasampayuttapacchimacittassa uppādakkhaṇe yassa cittassa anantarā "
               "somanassasampayuttapacchimacittaṃ uppajjissati tassa cittassa uppādakkhaṇe",
               "Pacchimacittassa uppādakkhaṇe yassa cittassa anantarā somanassasampayuttapacchimacittaṃ uppajjissati "
               "tassa cittassa uppādakkhaṇe asaññasattaṃ upapajjantānaṃ",
               "Pacchimacittassa uppādakkhaṇe asaññasattaṃ upapajjantānaṃ"):
        row(f"{hd} tesaṃ …", f"{answer_head13(hd, 'tesaṃ')}, {C.THEN} {B.L['tesaṃ']} …")
    h("Sample lines")
    for s in ("Pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti tesaṃ "
              "upapajjantānaṃ tesaṃ cakkhundriyaṃ uppajjati, no ca tesaṃ sotindriyaṃ uppajjissati. Itaresaṃ "
              "sacakkhukānaṃ upapajjantānaṃ tesaṃ cakkhundriyañca uppajjati sotindriyañca uppajjissati.",
              "Pacchimacittassa uppādakkhaṇe yassa cittassa anantarā upekkhāsampayuttapacchimacittaṃ uppajjissati "
              "tassa cittassa uppādakkhaṇe tesaṃ jīvitindriyaṃ uppajjati, no ca tesaṃ somanassindriyaṃ uppajjissati.",
              "Itarāsaṃ itthīnaṃ upapajjantīnaṃ tāsaṃ itthindriyañca uppajjati purisindriyañca uppajjissati.",
              "Yassa cakkhundriyaṃ uppajjati tassa purisindriyaṃ uppajjissatīti? (Sadisaṃ )"):
        row(s, line13(s, M))
    h("Termbase misfits and gaps (for the coordinator)")
    out += [
        "- 'P ye ca … ye ca … [eteneva bhāvena katici bhave dassetvā] parinibbāyissanti tesaṃ upapajjantānaṃ' "
        "(^6-10-366 … ^6-10-369, ^6-10-376 … ^6-10-379): = 10-10 ye_head (coordinator-accepted); built as "
        "10-05's ye_head12 (P and the clauses joined flat: «Ở P, những người nào … và những người nam nào …») plus "
        f"3-03's tail «, {A3.KHI_UPAPAJJANTA}». tāsaṃ upapajjantīnaṃ = the same tail (Vietnamese has no gender, 10-02).",
        "- Pacchimabhavikānaṃ itthīnaṃ upapajjantīnaṃ / purisānaṃ upapajjantānaṃ (not set before): 2-01's attribute "
        "and 10-02's sex word: «những người thuộc kiếp sống cuối cùng đang tái sinh làm người nữ / người nam» (the "
        "3-02 «những người thuộc kiếp sống cuối cùng đang tái sinh vào …» shape). Please confirm.",
        "- yassa cittassa anantarā <X>pacchimacittaṃ uppajjissati tassa cittassa uppādakkhaṇe (new with the moment): "
        "9-01's that_mind_moment with 10-05's final mind: «vào khoảnh khắc sinh khởi của tâm mà ngay sau đó tâm cuối "
        "cùng gắn liền với sự bình thản sẽ sinh khởi» (user: smooth, meaning unchanged). Please confirm.",
        "- Somanassa- / Upekkhāsampayuttapacchimacittassa uppādakkhaṇe: termbase «khoảnh khắc sinh khởi của tâm cuối "
        "cùng gắn liền với …» (= 10-05 pacchima_mind order; 8's Sarāgapacchimacittassa puts «cuối cùng» last: a "
        "different compound, kept as the termbase has it).",
        f"- (Sadisaṃ ) after an unanswered question (^6-10-366, puriso pair = the itthi pair): «{SADISA_NOTE}» "
        f"(3-04 LIKEWISE; no termbase entry for bare Sadisaṃ).",
        "- No new member, verb or plane words.",
        "",
        "## Pāli as written (reported)",
        "",
        "- ^6-10-369 «(Kha) yassa vā pana somanassindriyaṃ uppajjissati, tassa purisindriyaṃ uppajjatīti?»: a comma the "
        "parallels lack; the Vietnamese shell has its comma there anyway («…, thì ở người ấy …»).",
        "- ^6-10-376 last answer «Sacakkhukānaṃ upapajjantānaṃ tesaṃ tattha manindriyaṃ uppajjissati cakkhundriyañca "
        "uppajjati.»: «-ñca» missing on manindriyaṃ; rendered as the both-frame (3-03 precedent).",
        "- ^6-10-366 «(Sadisaṃ )»: a space before «)»; rendered «(Giống như vậy)».",
        "- Unlabelled pairs among labelled ones (the cut-list pairs «Yassa … saddhindriyaṃ…pe… paññindriyaṃ…pe… "
        "manindriyaṃ uppajjissatīti?» / «Yassa vā pana …», the whole upekkhā and saddhā sections ^6-10-372, ^6-10-373, "
        "^6-10-382, ^6-10-383; the questions start with a capital there): kept as written (no label).",
        "- ^6-10-375 «Yattha …ti?…Pe….» = «… không?…» (9-01 / 10-08).",
        "",
        "## Setter cross-checks",
        "",
        "- Asserted equal: " + ", ".join(f"{k} {v}" for k, v in CHECKED.items()) + ".",
        "- Heads no setter parses (built here): " + str(len(NEW_HEADS)) + ".",
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
    M8.check_frames()
    M5.check_frames()
    check_frames()
    segs = build(CH)
    check_termbase()
    for bad, (good, n) in SLIPS.items():
        got = sum(1 for s in SLIPS_SEEN if s[1] == bad)
        assert got == n, (bad, got, n)
    S.write(CH, segs)
    text = (S.OUT_DIR / CH).read_text(encoding="utf-8")
    ADH_DIR.mkdir(parents=True, exist_ok=True)
    (ADH_DIR / CH).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", ADH_DIR / CH)
    NOTES_MD.write_text(unicodedata.normalize("NFC", notes()), encoding="utf-8", newline="\n")
    print("wrote", NOTES_MD)
    print("checked equal:", CHECKED, "; heads:", len(HEADS_SEEN), "; new heads:", len(NEW_HEADS),
          "; setter self-check failures:", len(SETTER_FAIL), "; slips:", SLIPS_SEEN)
    for k, v in SETTER_FAIL.items():
        print("setter fail:", k, v[0])


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
