"""Russian plain zero-shot of pi-6 (Yamaka): 7-03-anusayayamaka.md (Sānusayavāra, anuloma: person / place /
person and place).

Family C frames come from build_7-01_ru (imported, never edited); "…pe…" endings from build_7-02_ru.
New here (listed in notes-7-03.md), exposed for 7-04 … 7-11:
  - Transitive answers (sānusaya, and the same machinery for pajahati / parijānāti): person in the nominative
    (C.PERSON_NOM), "so tato / te tato / tato" resumptives, "no ca [so tato] B sānusayo" -> «, но [он там] не имеет B».
  - Negated «иметь» takes the GENITIVE object (NEG_OBJ_CASE): «не имеет скрытой склонности к X»,
    «не имеет ни скрытой склонности к X, ни скрытой склонности к Y».
  - Place questions WITHOUT a person, yato … tato … (Q_YATO): the Pāli has no subject ("one"), Russian uses the
    indefinite-personal 3rd person plural (GENERIC_3PL): «Где имеют скрытую склонность к X, там имеют скрытую
    склонность к Y?»; place answers «<места>: там имеют …, но там не имеют …» (C.ANSWER_INTRO_PLACE).
  - A bare answer "Mānānusayena sānusayo." = «Имеют скрытую склонность к самомнению.» in a place section
    (generic subject), «Имеет …» in a person / person-and-place section (subject = the person asked about).
  - "Sānusayavāre anulomaṃ." = «Утвердительная форма в разделе об имеющих скрытые склонности.»

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_7-03_ru.py
Import: importlib.import_module("build_7-03_ru")   (importing never writes any file)
Reuse:  t_pred(), t_clause(), t_answer_sentence(s, generic), t_answers(a, generic), question(q), Q_YATO,
        GENERIC_3PL, NEG_OBJ_CASE, NO_CA_BARE_FRAME, VARE_FRAME, tr_line(body, mode)
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

CHAPTER = "7-03-anusayayamaka.md"
cap = B.cap

# ---------------------------------------------------------------------------------------------
# New frames (7-03)
# ---------------------------------------------------------------------------------------------
# yato … tato … with no person: generic subject "one" = Russian indefinite-personal 3rd person plural
GENERIC_3PL = {
    "имеет": "имеют", "имеют": "имеют",                               # sānusayo / sānusayā (niranusayo)
    "устраняет": "устраняют",                                         # pajahati (proposal for 7-04)
    "полностью понимает": "полностью понимают",                       # parijānāti (proposal for 7-05)
}
NEG_OBJ_CASE = {"имеет": "gen", "имеют": "gen"}   # negated «иметь» + genitive; other transitive verbs keep acc
Q_YATO = C.Q_PLACE                                 # "yato X tato Y?" = «Где {p1}, там {p2}?» (p in GENERIC_3PL)
Q_YATO_RE = re.compile(rf"yato( vā pana)? (.+?) ({C.TV}) tato (.+) ({C.TV})")
NO_CA_BARE_FRAME = ", но {neg_pred}"              # "…, no ca B sānusayo" (no resumptive in the Pāli)
RES_T = {k: 0 for k in ("so tato", "te tato", "tato")}
VARE_FRAME = "{form} в разделе об имеющих скрытые склонности."    # Sānusayavāre anulomaṃ.
SANUSAYAVARE = B.SECTION_HEADINGS["Sānusayavāra"]
assert VARE_FRAME.endswith(SANUSAYAVARE.replace("Раздел ", "") + ".")

FIXED = dict(D.FIXED)
FIXED["Sānusayavāre anulomaṃ."] = VARE_FRAME.format(form=cap(B.SECTION_HEADINGS["anulomaṃ"]))


# ---------------------------------------------------------------------------------------------
# Transitive predicates (the person is the subject, the anusaya the object)
# ---------------------------------------------------------------------------------------------
def t_pred(verb, parsed, generic=False, neg_extra=False):
    """sānusayo -> «имеет скрытую склонность к X»; negated -> «не имеет скрытой склонности к X» / «… ни …, ни …»;
    generic (yato … tato … without a person) -> «имеют …»."""
    ru, neg = C.TRANSITIVE[verb]
    neg = neg != neg_extra
    case = NEG_OBJ_CASE.get(ru, "acc") if neg else "acc"
    if generic:
        ru = GENERIC_3PL[ru]
    return f"{'не ' if neg else ''}{ru} {C.ru_list(parsed, case, neg)}"


def t_clause(s, generic=False):
    """One predicate, or the both-form «и P1, и P2» (C.BOTH_FRAME)."""
    segs = C.split_clause(s, C.TRANSITIVE)
    if len(segs) == 1:
        lst, v = segs[0]
        return t_pred(v, C.parse_list(lst), generic)
    if len(segs) == 2 and all(l.endswith(" ca") for l, _ in segs):
        if any(C.TRANSITIVE[v][1] for _, v in segs):
            raise ValueError(f"negated both-form not prepared: {s!r}")
        p = [t_pred(v, C.parse_list(l[:-3]), generic) for l, v in segs]
        return C.BOTH_FRAME.format(p1=p[0], p2=p[1])
    raise ValueError(f"clause shape not parsed: {s!r}")


# ---------------------------------------------------------------------------------------------
# Questions
# ---------------------------------------------------------------------------------------------
def question(q):
    words = C.lower1(q.strip()).split(" ")
    words[-1] = C.unti(words[-1])
    t = " ".join(words)
    m = Q_YATO_RE.fullmatch(t)
    if m:
        vapana, l1, v1, l2, v2 = m.groups()
        out = Q_YATO.format(p1=t_pred(v1, C.parse_list(l1), True), p2=t_pred(v2, C.parse_list(l2), True))
        return C.KHA_PREFIX + C.lower1(out) if vapana else out
    return C.question(q)          # yo … so … / yo yato … so tato … (C.Q_WHO, C.Q_WHO_PLACE)


# ---------------------------------------------------------------------------------------------
# Answers
# ---------------------------------------------------------------------------------------------
def _t_answer(s, generic_bare):
    if s in C.SIMPLE_ANSWERS:
        return C.SIMPLE_ANSWERS[s]
    assert s.endswith("."), s
    body = C.lower1(s[:-1])
    person, body = C._take(body, C.PERSON_NOM)
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

    generic = not person and (bool(loci) or generic_bare)
    if person and loci:
        assert res in ("so tato", "te tato"), s
        head = C.ANSWER_INTRO_PERSON_PLACE.format(person=cap(C.PERSON_NOM[person]),
                                                  loci=C.LOCI_SEP.join(C.LOCI[x] for x in loci), res=res_ru(res))
    elif loci:
        assert res == "tato", s
        head = C.ANSWER_INTRO_PLACE.format(loci=C.LOCI_SEP.join(C.LOCI[x] for x in loci), res=C.RES[res])
    elif person:
        assert res is None, s
        head = C.ANSWER_INTRO_PERSON.format(person=cap(C.PERSON_NOM[person]))
    else:                                  # "Mānānusayena sānusayo." (subject from the question)
        assert res is None and not neg, s
        head = ""
    out = head + t_clause(main, generic)
    if neg:
        nres, neg = C._take(neg, RES_T)
        assert nres == res, s
        segs = C.split_clause(neg, C.TRANSITIVE)
        assert len(segs) == 1, s
        lst, v = segs[0]
        np = t_pred(v, C.parse_list(lst), generic, neg_extra=True)
        out += (C.NO_CA_FRAME.format(res=res_ru(nres), neg_pred=np) if nres else NO_CA_BARE_FRAME.format(neg_pred=np))
    return cap(out) + "."


def t_answer_sentence(s, generic_bare=False):
    pe = s.endswith(D.PE + ".")
    if pe:
        s = s[:-len(D.PE + ".")] + "."
    out = _t_answer(s, generic_bare)
    if pe:
        assert out.endswith("."), out
        out = out[:-1] + D.PE_END
    return out


def t_answers(a, generic_bare=False):
    sents = re.split(r"(?<=\.) (?=\S)", a.strip())
    return " ".join(t_answer_sentence(x, generic_bare) for x in sents)


# ---------------------------------------------------------------------------------------------
# Lines; mode = "okasa" inside an "…okāso" section (bare answers take the generic subject)
# ---------------------------------------------------------------------------------------------
def mode_of(heading_body):
    t = heading_body.split()[-1]
    if t.endswith("okāso"):
        return "okasa"
    return "puggala"


def tr_line(body, mode="puggala"):
    if not body.strip():
        return ""
    if body in FIXED:
        return FIXED[body]
    if body.startswith("#"):
        return C.heading(body)
    text = C.preprocess(body)
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
            out += " " + t_answers(a, mode == "okasa")
    else:
        out = label + t_answers(text, mode == "okasa")
    return out + tail


def translate_file(src_text):
    out, mode = [], "puggala"
    for line in src_text.split("\n"):
        body, bid = B.ID_RE.match(line).groups()
        if body.startswith("#"):
            mode = mode_of(body)
        out.append(tr_line(body, mode) + (bid or ""))
    return "\n".join(out)


# ---------------------------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------------------------
CROSSBOOK_03 = [
    ("5", "обычный человек"),        # puthujjano (PERSON_NOM; pi-5 10-dutiyavaggo)
]
FINISHED = ["1-mulayamaka.md", "7-01-anusayayamaka.md", "7-02-anusayayamaka.md"]


def check_crossbook_03():
    cache, missing = {}, []
    for b, s in CROSSBOOK_03:
        if b not in cache:
            cache[b] = "\n".join(p.read_text(encoding="utf-8") for p in sorted(B.RAILS[b].glob("*.md")))
        if s not in cache[b]:
            missing.append((b, s))
    if missing:
        raise AssertionError(f"cross-book strings not found in the pi-1..5 rails: {missing}")
    return True


def check_local(ru):
    assert "но не так, что" not in ru
    assert not re.search(r"не имеют? (ни )?скрытую", ru), "negated «иметь» must take the genitive"
    assert not re.search(r"\bли\b", ru)
    assert not re.search(r"[A-Za-zĀ-ſḀ-ỿ]", re.sub(r"\^[0-9A-Za-z-]+", "", ru)), "Latin left"
    assert "\n\n\n" not in ru and "\r" not in ru


def main():
    B.check_crossbook()
    C.check_crossbook_c()
    D.check_crossbook_02()
    check_crossbook_03()
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    ru = unicodedata.normalize("NFC", translate_file(src))
    check_local(ru)
    C.check_consistency(src, ru, _seen())
    B.check_pair(src, ru, CHAPTER)
    with open(B.OUT_DIR / CHAPTER, "w", encoding="utf-8", newline="\n") as f:
        f.write(ru)
    print("written", B.OUT_DIR / CHAPTER, "lines", len(ru.split("\n")))
    print("cross-book asserts OK; consistency OK; per-line checks OK")


def _seen():
    seen = {}
    for name in FINISHED:
        p, r = B.PALI_DIR / name, B.OUT_DIR / name
        if r.exists():
            C.check_consistency(p.read_text(encoding="utf-8"), r.read_text(encoding="utf-8"), seen)
    return seen


if __name__ == "__main__":
    main()
