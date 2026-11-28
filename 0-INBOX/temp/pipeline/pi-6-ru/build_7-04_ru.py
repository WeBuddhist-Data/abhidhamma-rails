"""Russian plain zero-shot of pi-6 (Yamaka): 7-04-anusayayamaka.md (Sānusayavāra, paṭiloma: person / place /
person and place; niranusaya).

Family C frames come from build_7-01_ru, build_7-02_ru and build_7-03_ru (imported, never edited).
New here (listed in notes-7-04.md):
  - niranusayo / niranusayā = «не имеет / не имеют скрытой склонности к X» (7-01 TRANSITIVE, genitive after the
    negated «иметь»: 7-03 NEG_OBJ_CASE), also in the yo … so … questions (Q_WHO / Q_WHO_PLACE with t_pred, so the
    object is in the genitive; 7-01's C.question would give the accusative).
  - Two negated predicates "A ca niranusayo B ca niranusayo" = «не имеет ни A, ни B» (coordinator "Negatives";
    t_both_neg(): verb once, number of the Pāli verb, generic «не имеют» in place answers).
  - Denied negative "…, no ca [so tato] B niranusayo" = «…, но [он там] имеет B» (C.NO_CA_POS_FRAME).
  - sabbattha after a nominative person: «Архат везде не имеет ни …» (7-02 SABBATTHA).
  - "Sānusayavāre paṭilomaṃ." = «Отрицательная форма в разделе об имеющих скрытые склонности.» (7-03 VARE_FRAME);
    "Sānusayavāro." = «Раздел об имеющих скрытые склонности.» (7-01 VARO_CLOSING).

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_7-04_ru.py
Import: importlib.import_module("build_7-04_ru")   (importing never writes any file)
Reuse:  t_both_neg(), t_clause(), question(), t_answers(), tr_line(body, mode)
"""
import importlib
import pathlib
import re
import sys
import unicodedata

PIPE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru")
if str(PIPE) not in sys.path:
    sys.path.insert(0, str(PIPE))
import build_sample_ru as B   # noqa: E402

C = importlib.import_module("build_7-01_ru")
D = importlib.import_module("build_7-02_ru")
E = importlib.import_module("build_7-03_ru")

CHAPTER = "7-04-anusayayamaka.md"
cap = B.cap

# ---------------------------------------------------------------------------------------------
# Fixed lines
# ---------------------------------------------------------------------------------------------
FIXED = dict(E.FIXED)
FIXED["Sānusayavāre paṭilomaṃ."] = E.VARE_FRAME.format(form=cap(B.SECTION_HEADINGS["paccanīkaṃ"]))
FIXED["Sānusayavāro."] = C.VARO_CLOSING.format(heading=B.SECTION_HEADINGS["Sānusayavāro"])

# Source slips rendered as meant (reported in notes-7-04.md); the Pāli file is not touched.
SLIPS_04 = {
    "Sveva puggalo dukkhāya vedanāya ariyāpanne ": "Sveva puggalo dukkhāya vedanāya apariyāpanne ",   # ^6-7-130
    "paṭighānusayena niranusayo no ca so tato": "paṭighānusayena niranusayo, no ca so tato",             # ^6-7-122
}
# ^6-7-127 "Arahā sabbattha bhavarāgānusayena niranusayo kāmarāgānusayena ca …": first "ca" missing; the two
# negated predicates are read as the usual "A ca niranusayo B ca niranusayo" (t_clause, MISSING_CA_OK).
MISSING_CA_OK = {"bhavarāgānusayena"}
RES_T = E.RES_T


# ---------------------------------------------------------------------------------------------
# Predicates
# ---------------------------------------------------------------------------------------------
def t_both_neg(segs, generic):
    """"A ca niranusayo B ca C ca niranusayo" -> «не имеет ни A(gen), ни B(gen), ни C(gen)» (C.BOTH_NEG_FRAME);
    the verb's number follows the Pāli verb; generic (no person) -> «не имеют»."""
    ru = C.TRANSITIVE[segs[0][1]][0]
    assert all(C.TRANSITIVE[v][0] == ru for _, v in segs), segs
    if generic:
        ru = E.GENERIC_3PL[ru]
    case = E.NEG_OBJ_CASE.get(ru, "acc")
    items = []
    for lst, _ in segs:
        t = C.ru_list(C.parse_list(lst), case, True)
        items.append(t if t.startswith("ни ") else "ни " + t)
    return C.BOTH_NEG_FRAME.format(verb=ru, items=", ".join(items))


def t_clause(s, generic=False):
    """One predicate, the both-form «и P1, и P2», or the negated both-form «не имеет ни A, ни B»."""
    segs = C.split_clause(s, C.TRANSITIVE)
    if len(segs) == 1:
        lst, v = segs[0]
        return E.t_pred(v, C.parse_list(lst), generic)
    if len(segs) == 2:
        (l1, v1), (l2, v2) = segs
        if not l1.endswith(" ca"):
            assert l1 in MISSING_CA_OK, s
            l1 += " ca"
        assert l2.endswith(" ca"), s
        segs = [(l1[:-3], v1), (l2[:-3], v2)]
        if all(C.TRANSITIVE[v][1] for _, v in segs):
            return t_both_neg(segs, generic)
        if not any(C.TRANSITIVE[v][1] for _, v in segs):
            p = [E.t_pred(v, C.parse_list(l), generic) for l, v in segs]
            return C.BOTH_FRAME.format(p1=p[0], p2=p[1])
    raise ValueError(f"clause shape not parsed: {s!r}")


# ---------------------------------------------------------------------------------------------
# Questions
# ---------------------------------------------------------------------------------------------
def question(q):
    words = C.lower1(q.strip()).split(" ")
    words[-1] = C.unti(words[-1])
    t = " ".join(words)
    m = C.Q_YO.fullmatch(t)
    if m:                                  # yo (yato) … so (tato) …: object case from t_pred (genitive if negated)
        _, vapana, yato, l1, v1, res2, l2, v2 = m.groups()
        assert bool(yato) == (res2 == "so tato"), q
        out = (C.Q_WHO_PLACE if yato else C.Q_WHO).format(p1=E.t_pred(v1, C.parse_list(l1)),
                                                         p2=E.t_pred(v2, C.parse_list(l2)))
        return C.KHA_PREFIX + C.lower1(out) if vapana else out
    m = E.Q_YATO_RE.fullmatch(t)
    if m:
        return E.question(q)
    raise ValueError(f"question not parsed: {q!r}")


# ---------------------------------------------------------------------------------------------
# Answers
# ---------------------------------------------------------------------------------------------
def _t_answer(s):
    if s in C.SIMPLE_ANSWERS:
        return C.SIMPLE_ANSWERS[s]
    assert s.endswith("."), s
    body = C.lower1(s[:-1])
    person, body = C._take(body, C.PERSON_NOM)
    sabb = False
    if body.startswith("sabbattha "):
        sabb, body = True, body[len("sabbattha "):]
    loci = []
    while True:
        loc, body = C._take(body, C.LOCI)
        if not loc:
            break
        loci.append(loc)
    res, body = C._take(body, RES_T)
    main, _, neg = body.partition(", no ca ")

    def res_ru(k):
        r = C.RES[k]
        return C.RES_FEM.get(r, r) if person in C.PERSON_FEM else r

    generic = not person
    if sabb:
        assert person and not loci and res is None and not neg, s
        head = f"{cap(C.PERSON_NOM[person])} {D.SABBATTHA} "
    elif person and loci:
        assert res in ("so tato", "te tato"), s
        head = C.ANSWER_INTRO_PERSON_PLACE.format(person=cap(C.PERSON_NOM[person]),
                                                  loci=C.LOCI_SEP.join(C.LOCI[x] for x in loci), res=res_ru(res))
    elif loci:
        assert res == "tato", s
        head = C.ANSWER_INTRO_PLACE.format(loci=C.LOCI_SEP.join(C.LOCI[x] for x in loci), res=C.RES[res])
    elif person:
        assert res is None, s
        head = C.ANSWER_INTRO_PERSON.format(person=cap(C.PERSON_NOM[person]))
    else:
        raise ValueError(f"answer intro not parsed: {s!r}")
    out = head + t_clause(main, generic)
    if neg:
        nres, neg = C._take(neg, RES_T)
        assert nres == res, s
        segs = C.split_clause(neg, C.TRANSITIVE)
        assert len(segs) == 1, s
        lst, v = segs[0]
        # "no" negates the verb that follows: no ca … niranusayo = «имеет» (C.NO_CA_POS_FRAME)
        np = E.t_pred(v, C.parse_list(lst), generic, neg_extra=True)
        pos = C.TRANSITIVE[v][1]
        if nres:
            out += (C.NO_CA_POS_FRAME if pos else C.NO_CA_FRAME).format(res=res_ru(nres), pos_pred=np, neg_pred=np)
        else:
            out += E.NO_CA_BARE_FRAME.format(neg_pred=np)
    return cap(out) + "."


def t_answer_sentence(s):
    pe = s.endswith(D.PE + ".")
    if pe:
        s = s[:-len(D.PE + ".")] + "."
    out = _t_answer(s)
    if pe:
        assert out.endswith("."), out
        out = out[:-1] + D.PE_END
    return out


def t_answers(a):
    sents = re.split(r"(?<=\.) (?=\S)", a.strip())
    return " ".join(t_answer_sentence(x) for x in sents)


# ---------------------------------------------------------------------------------------------
# Lines
# ---------------------------------------------------------------------------------------------
def preprocess(body):
    text = C.preprocess(body)
    for a, b in SLIPS_04.items():
        text = text.replace(a, b)
    return text


def tr_line(body):
    if not body.strip():
        return ""
    if body in FIXED:
        return FIXED[body]
    if body.startswith("#"):
        return C.heading(body)
    text = preprocess(body)
    tail = ""
    m = C.MULAKA_RE.fullmatch(text)
    if m:
        text, tail = m.group(1), f" ({C.MULAKA[m.group(2)]})"
    label = ""
    m = C.LABEL_RE.fullmatch(text)
    if m and m.group(1) in B.LETTERS:
        label, text = f"({B.LETTERS[m.group(1)]}) ", m.group(2)
    if "?" in text:
        q, _, a = text.partition("?")
        out = label + question(q)
        if a.strip():
            out += " " + t_answers(a)
    else:
        out = label + t_answers(text)
    return out + tail


def translate_file(src_text):
    out = []
    for line in src_text.split("\n"):
        body, bid = B.ID_RE.match(line).groups()
        out.append(tr_line(body) + (bid or ""))
    return "\n".join(out)


# ---------------------------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------------------------
FINISHED = ["1-mulayamaka.md", "7-01-anusayayamaka.md", "7-02-anusayayamaka.md", "7-03-anusayayamaka.md"]


def check_local(ru, src):
    E.check_local(ru)
    assert not re.search(r"не имеют? (ни )?скрытую", ru), "negated «иметь» must take the genitive"
    assert not re.search(r"(?<!\w)и не имеют?\b", ru), "negated pairs must be «не имеет ни A, ни B»"
    # every niranusaya line is negative in Russian
    for p, r in zip(src.split("\n"), ru.split("\n")):
        if "niranusay" in p:
            assert "не имеет" in r or "не имеют" in r, r


def seen_from_finished():
    seen = {}
    for name in FINISHED:
        p, r = B.PALI_DIR / name, B.OUT_DIR / name
        if r.exists():
            C.check_consistency(p.read_text(encoding="utf-8"), r.read_text(encoding="utf-8"), seen)
    return seen


def main():
    B.check_crossbook()
    C.check_crossbook_c()
    D.check_crossbook_02()
    E.check_crossbook_03()
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    ru = unicodedata.normalize("NFC", translate_file(src))
    check_local(ru, src)
    C.check_consistency(src, ru, seen_from_finished())
    B.check_pair(src, ru, CHAPTER)
    with open(B.OUT_DIR / CHAPTER, "w", encoding="utf-8", newline="\n") as f:
        f.write(ru)
    print("written", B.OUT_DIR / CHAPTER, "lines", len(ru.split("\n")))
    print("cross-book asserts OK; consistency OK; per-line checks OK")


if __name__ == "__main__":
    main()
