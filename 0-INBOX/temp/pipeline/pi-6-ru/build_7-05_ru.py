"""Russian plain zero-shot of pi-6 (Yamaka): 7-05-anusayayamaka.md (Pajahanavāra, anuloma: person / place /
person and place).

Family C frames come from build_7-01_ru, build_7-02_ru, build_7-03_ru and build_7-04_ru (imported, never edited);
Aggamaggasamaṅgī from build_2-02_ru. New here (listed in notes-7-05.md), exposed for 7-06 (Pajahanavāra paṭiloma):
  - pajahati = «устраняет» (+ accusative, also when negated: NEG_OBJ_CASE covers «иметь» only); generic yato … tato …
    = «Где устраняют …, там устраняют …?» (7-03 Q_YATO, GENERIC_3PL).
  - Lists in the accusative with sandhi "-ānusayañca" = "-ānusayaṃ ca" (preprocess()).
  - tadekaṭṭhaṃ: bare "Tadekaṭṭhaṃ pajahati." = TADEKATTHA_BARE «Устраняет то, что пребывает вместе с устраняемым.»
    (number-neutral: the implied object and the antecedent are singular or plural by question);
    "A pajahati B tadekaṭṭhaṃ pajahati" = TADEKATTHA_PAIR «устраняет A и устраняет B, пребывающую вместе с
    устраняемой» (tadekaṭṭha pi-1 «пребывающие вместе с ними»; participle number = B, «устраняемой / устраняемыми»
    = number of A).
  - Persons: Aṭṭhamako «личность восьмой ступени» (pi-5; feminine: «она там»), Aggamaggasamaṅgī «обладающий высшим
    путём» (2-02), proposed Anāgāmimaggasamaṅgī «обладающий путём невозвращения» (pi-2 / pi-5 «путь невозвращения»),
    and the «Кроме …, остальные личности» genitives for 7-06 (APART_GEN_05, apart_persons()).
  - "Pajahanavāre anulomaṃ." = «Утвердительная форма в разделе об устранении.» (PAJAHANAVARE_FRAME; paṭilomaṃ and
    the closing "Pajahanavāro." prepared in FIXED).

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_7-05_ru.py
Import: importlib.import_module("build_7-05_ru")   (importing never writes any file)
Reuse:  PERSON_NOM_05, PERSON_FEM_05, APART_GEN_05, apart_persons(), TRANSITIVE_05, TADEKATTHA_*, tadekattha(),
        p_clause(), question(), p_answers(a, mode), tr_line(body, mode), translate_file(), preprocess()
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
F = importlib.import_module("build_7-04_ru")
P = importlib.import_module("build_2-02_ru")

CHAPTER = "7-05-anusayayamaka.md"
cap = B.cap

# ---------------------------------------------------------------------------------------------
# Persons (nominative answers; genitive after «Кроме»)
# ---------------------------------------------------------------------------------------------
AGG_NOM = next(ru for rx, ru, _, _ in P.PJ_SUBJ_UNITS if rx == "aggamaggasamaṅgī")   # «обладающий высшим путём»
AGG_GEN = P.PJ_GEN["aggamaggasamaṅgiṃ"]                                              # «обладающего высшим путём»
PERSON_NOM_05 = dict(C.PERSON_NOM)
PERSON_NOM_05.update({
    "aṭṭhamako": "личность восьмой ступени",          # pi-5 Aṭṭhamako puggalo = Личность восьмой ступени
    "aggamaggasamaṅgī": AGG_NOM,                      # 2-02
    "anāgāmimaggasamaṅgī": "обладающий путём невозвращения",   # proposal for 7-06 (pi-2/pi-5 «путь невозвращения»)
})
PERSON_FEM_05 = set(C.PERSON_FEM) | {"aṭṭhamako"}     # «личность» is feminine: so tato -> «она там»
APART_GEN_05 = {                                      # "X ṭhapetvā avasesā puggalā" (7-06), genitive after «Кроме»
    "aggamaggasamaṅgiṃ": AGG_GEN,
    "anāgāmimaggasamaṅgiṃ": "обладающего путём невозвращения",
    "aṭṭhamakaṃ": "личности восьмой ступени",         # pi-5 «У личности восьмой ступени»
    "dvinnaṃ maggasamaṅgīnaṃ": "двух обладающих путём",   # maggasamaṅgī pi-1/pi-2 «обладающий путём»
}
PUGGALA_PL = P.PUGGALA_PL                             # «личности»
APART_RE = re.compile(r"(.+?) ṭhapetvā avasesā puggalā")


def apart_persons(s):
    """'Anāgāmimaggasamaṅgiñca aṭṭhamakañca ṭhapetvā avasesā puggalā' ->
    «Кроме обладающего путём невозвращения и личности восьмой ступени, остальные личности» (2-01 APART_GROUP)."""
    m = APART_RE.fullmatch(C.lower1(s))
    if not m:
        raise ValueError(f"apart group not parsed: {s!r}")
    t = re.sub(r"ñca(?=\s|$)", "ṃ ca", m.group(1))          # "aṭṭhamakañca" -> "aṭṭhamakaṃ ca"
    parts = [x.strip() for x in re.split(r" ca(?=\s|$)", t) if x.strip()]
    names = [APART_GEN_05[x] for x in parts]
    a_gen = names[0] if len(names) == 1 else ", ".join(names[:-1]) + " и " + names[-1]
    return cap(P.A.APART_GROUP.format(a_gen=a_gen, g_nom=PUGGALA_PL))


# plural forms for 7-06 ("… avasesā puggalā … nappajahanti")
TRANSITIVE_05 = dict(C.TRANSITIVE, pajahanti=("устраняют", False), nappajahanti=("устраняют", True))

# ---------------------------------------------------------------------------------------------
# tadekaṭṭha (pi-1 tadekaṭṭha = «пребывающие вместе с ними»)
# ---------------------------------------------------------------------------------------------
TADEKATTHA_BARE = "устраняет то, что пребывает вместе с устраняемым"   # "Tadekaṭṭhaṃ pajahati." (object implied)
TADEKATTHA_PART = {"sg": "пребывающую", "pl": "пребывающие"}          # agrees with B («скрытая склонность», f.)
# antecedent A, named as "the one(s) being abandoned" as in TADEKATTHA_BARE: «с ней» would be ambiguous after
# «Личность восьмой ступени …: она там …» (personal pronoun of the person, feminine like «склонность»)
TADEKATTHA_WITH = {"sg": "вместе с устраняемой", "pl": "вместе с устраняемыми"}
TADEKATTHA_OBJ = "{verb} {obj}, {part} {with_}"                         # "B tadekaṭṭhaṃ pajahati"
TADEKATTHA_PAIR = "{p1} и {p2}"                                          # "A pajahati B tadekaṭṭhaṃ pajahati"
TADEKATTHA = "tadekaṭṭhaṃ"
assert C.TADEKATTHA_FRAME   # 7-01's proposal «{Verb} то, что пребывает вместе с ней.» is settled as TADEKATTHA_BARE


def _num(parsed):
    return "pl" if len(parsed[0]) > 1 else "sg"


def tadekattha(v1, l1, v2, l2, generic=False):
    """A pajahati B tadekaṭṭhaṃ pajahati -> «устраняет A и устраняет B, пребывающую вместе с устраняемой»."""
    pa, pb = C.parse_list(l1), C.parse_list(l2)
    p1 = E.t_pred(v1, pa, generic)
    ru, neg = C.TRANSITIVE[v2]
    assert not neg, (v2, l2)
    if generic:
        ru = E.GENERIC_3PL[ru]
    p2 = TADEKATTHA_OBJ.format(verb=ru, obj=C.ru_list(pb, "acc"), part=TADEKATTHA_PART[_num(pb)],
                               with_=TADEKATTHA_WITH[_num(pa)])
    return TADEKATTHA_PAIR.format(p1=p1, p2=p2)


def p_clause(s, generic=False):
    """One predicate, the both-form (7-04 t_clause), bare tadekaṭṭha, or the tadekaṭṭha pair."""
    segs = C.split_clause(s, C.TRANSITIVE)
    if len(segs) == 1 and segs[0][0] == TADEKATTHA:
        assert segs[0][1] == "pajahati" and not generic, s
        return TADEKATTHA_BARE
    if len(segs) == 2 and segs[1][0].endswith(" " + TADEKATTHA):
        (l1, v1), (l2, v2) = segs
        return tadekattha(v1, l1, v2, l2[:-len(TADEKATTHA) - 1], generic)
    return F.t_clause(s, generic)


# ---------------------------------------------------------------------------------------------
# Preprocessing (parsing only; the Pāli file is untouched)
# ---------------------------------------------------------------------------------------------
SLIPS_05 = {
    "tato avijjānusayaṃ pajahati no ca tato": "tato avijjānusayaṃ pajahati, no ca tato",   # ^6-7-148 comma missing
}


def preprocess(body):
    text = C.preprocess(body)                         # " …pe…" spacing
    for a, b in SLIPS_05.items():
        text = text.replace(a, b)
    return text.replace("ānusayañca", "ānusayaṃ ca")  # accusative sandhi in lists


# ---------------------------------------------------------------------------------------------
# Questions: yo … so … / yo yato … so tato … (C.Q_WHO / C.Q_WHO_PLACE), yato … tato … (7-03 Q_YATO, generic)
# ---------------------------------------------------------------------------------------------
def question(q):
    return F.question(q)


# ---------------------------------------------------------------------------------------------
# Answers
# ---------------------------------------------------------------------------------------------
def _p_answer(s, generic_bare):
    if s in C.SIMPLE_ANSWERS:
        return C.SIMPLE_ANSWERS[s]
    assert s.endswith("."), s
    body = C.lower1(s[:-1])
    person, body = C._take(body, PERSON_NOM_05)
    loci = []
    while True:
        loc, body = C._take(body, C.LOCI)
        if not loc:
            break
        loci.append(loc)
    res, body = C._take(body, E.RES_T)
    main, _, neg = body.partition(", no ca ")

    def res_ru(k):
        r = C.RES[k]
        return C.RES_FEM.get(r, r) if person in PERSON_FEM_05 else r

    generic = not person and (bool(loci) or generic_bare)
    if person and loci:
        assert res in ("so tato", "te tato"), s
        head = C.ANSWER_INTRO_PERSON_PLACE.format(person=cap(PERSON_NOM_05[person]),
                                                  loci=C.LOCI_SEP.join(C.LOCI[x] for x in loci), res=res_ru(res))
    elif loci:
        assert res == "tato", s
        head = C.ANSWER_INTRO_PLACE.format(loci=C.LOCI_SEP.join(C.LOCI[x] for x in loci), res=C.RES[res])
    elif person:
        assert res is None, s
        head = C.ANSWER_INTRO_PERSON.format(person=cap(PERSON_NOM_05[person]))
    else:                                  # "Mānānusayaṃ pajahati." / "Tadekaṭṭhaṃ pajahati." (subject from the question)
        assert res is None and not neg, s
        head = ""
    out = head + p_clause(main, generic)
    if neg:
        nres, neg = C._take(neg, E.RES_T)
        assert nres == res, s
        segs = C.split_clause(neg, C.TRANSITIVE)
        assert len(segs) == 1, s
        lst, v = segs[0]
        np = E.t_pred(v, C.parse_list(lst), generic, neg_extra=True)
        pos = C.TRANSITIVE[v][1]
        if nres:
            out += (C.NO_CA_POS_FRAME if pos else C.NO_CA_FRAME).format(res=res_ru(nres), pos_pred=np, neg_pred=np)
        else:
            out += E.NO_CA_BARE_FRAME.format(neg_pred=np)
    return cap(out) + "."


def p_answer_sentence(s, generic_bare=False):
    pe = s.endswith(D.PE + ".")
    if pe:
        s = s[:-len(D.PE + ".")] + "."
    out = _p_answer(s, generic_bare)
    if pe:
        assert out.endswith("."), out
        out = out[:-1] + D.PE_END
    return out


def p_answers(a, generic_bare=False):
    sents = re.split(r"(?<=\.) (?=\S)", a.strip())
    return " ".join(p_answer_sentence(x, generic_bare) for x in sents)


# ---------------------------------------------------------------------------------------------
# Fixed lines
# ---------------------------------------------------------------------------------------------
PAJAHANAVARO = B.SECTION_HEADINGS["Pajahanavāro"]                       # «Раздел об устранении»
PAJAHANAVARE_FRAME = "{form} в разделе об устранении."                   # Pajahanavāre anulomaṃ / paṭilomaṃ.
assert PAJAHANAVARE_FRAME.endswith(PAJAHANAVARO.replace("Раздел ", "") + ".")
FIXED = dict(F.FIXED)
FIXED["Pajahanavāre anulomaṃ."] = PAJAHANAVARE_FRAME.format(form=cap(B.SECTION_HEADINGS["anulomaṃ"]))
FIXED["Pajahanavāre paṭilomaṃ."] = PAJAHANAVARE_FRAME.format(form=cap(B.SECTION_HEADINGS["paccanīkaṃ"]))   # 7-06
FIXED["Pajahanavāro."] = C.VARO_CLOSING.format(heading=PAJAHANAVARO)                                     # 7-06


# ---------------------------------------------------------------------------------------------
# Lines; mode = "okasa" inside an "…okāso" section (bare answers take the generic subject)
# ---------------------------------------------------------------------------------------------
def tr_line(body, mode="puggala"):
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
            out += " " + p_answers(a, mode == "okasa")
    else:
        out = label + p_answers(text, mode == "okasa")
    return out + tail


def translate_file(src_text):
    out, mode = [], "puggala"
    for line in src_text.split("\n"):
        body, bid = B.ID_RE.match(line).groups()
        if body.startswith("#"):
            mode = E.mode_of(body)
        out.append(tr_line(body, mode) + (bid or ""))
    return "\n".join(out)


# ---------------------------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------------------------
CROSSBOOK_05 = [   # strings taken from the approved pi-1 … pi-5 Russian rails
    ("5", "он полностью понимает страдание, устраняет возникновение"),   # pajahati = устраняет
    ("5", "устраняют злобу"),                                            # generic subject = 3rd person plural
    ("5", "Личность восьмой ступени является"),                          # Aṭṭhamako (puggalo)
    ("5", "У личности восьмой ступени"),
    ("5", "путь невозвращения"),                                         # anāgāmimagga
    ("1", "пребывающие вместе с ними"),                                  # tadekaṭṭha
    ("2", "знание обладающего путём"),                                   # maggasamaṅgī
]
FINISHED = ["1-mulayamaka.md", "7-01-anusayayamaka.md", "7-02-anusayayamaka.md", "7-03-anusayayamaka.md",
            "7-04-anusayayamaka.md"]


def check_crossbook_05():
    cache, missing = {}, []
    for b, s in CROSSBOOK_05:
        if b not in cache:
            cache[b] = "\n".join(p.read_text(encoding="utf-8") for p in sorted(B.RAILS[b].glob("*.md")))
        if s not in cache[b]:
            missing.append((b, s))
    if missing:
        raise AssertionError(f"cross-book strings not found in the pi-1..5 rails: {missing}")
    return True


def check_local(ru, src):
    E.check_local(ru)
    assert "\n\n\n" not in ru and "\r" not in ru
    for p, r in zip(src.split("\n"), ru.split("\n")):
        if "pajahati" in p:
            assert "устраня" in r.lower(), r
        if "no ca" in p:
            assert ", но " in r, r
        if "tadekaṭṭh" in p.lower():
            assert "пребыва" in r, r
    # self-test of the 7-06 helpers (nothing of 7-06 is written)
    assert apart_persons("Anāgāmimaggasamaṅgiñca aṭṭhamakañca ṭhapetvā avasesā puggalā") == \
        "Кроме обладающего путём невозвращения и личности восьмой ступени, остальные личности"
    assert apart_persons("Dvinnaṃ maggasamaṅgīnaṃ ṭhapetvā avasesā puggalā") == \
        "Кроме двух обладающих путём, остальные личности"


def check_consistency_05(src, ru):
    """Identical Pāli line -> identical Russian line: across the finished chapters (Pāli key) and within this
    chapter per mode (a bare answer such as "Mānānusayaṃ pajahati." has the generic subject «Устраняют» in the
    place section and the person «Устраняет» in the person sections: the Pāli subject is implicit)."""
    seen = {}
    for name in FINISHED:
        p, r = B.PALI_DIR / name, B.OUT_DIR / name
        if r.exists():
            C.check_consistency(p.read_text(encoding="utf-8"), r.read_text(encoding="utf-8"), seen)
    local, mode = {}, "puggala"
    for p, r in zip(src.split("\n"), ru.split("\n")):
        if p.startswith("#"):
            mode = E.mode_of(B.ID_RE.match(p).group(1))
        pb, rb = B.ID_ANY.sub("", p).strip(), B.ID_ANY.sub("", r).strip()
        if pb in seen:
            assert seen[pb] == rb, f"inconsistent with a finished chapter: {pb!r}"
        key = (mode == "okasa", pb)
        if key in local:
            assert local[key] == rb, f"inconsistent: {pb!r}"
        local[key] = rb


def main():
    B.check_crossbook()
    C.check_crossbook_c()
    D.check_crossbook_02()
    E.check_crossbook_03()
    check_crossbook_05()
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    ru = unicodedata.normalize("NFC", translate_file(src))
    check_local(ru, src)
    check_consistency_05(src, ru)
    B.check_pair(src, ru, CHAPTER)
    with open(B.OUT_DIR / CHAPTER, "w", encoding="utf-8", newline="\n") as f:
        f.write(ru)
    print("written", B.OUT_DIR / CHAPTER, "lines", len(ru.split("\n")))
    print("cross-book asserts OK; consistency OK; per-line checks OK")


if __name__ == "__main__":
    main()
