"""Russian plain zero-shot of pi-6 (Yamaka): 7-06-anusayayamaka.md (Pajahanavāra, paṭiloma: person / place /
person and place).

Family C frames come from build_7-01_ru … build_7-05_ru (imported, never edited); every frame not listed in
notes-7-06.md is theirs. New or first used here:
  - nappajahati / nappajahanti = «не устраняет / не устраняют» + accusative (7-05 TRANSITIVE_05; 7-03 NEG_OBJ_CASE
    is for «иметь» only); two negated predicates "A ca nappajahati B ca nappajahati" = «не устраняет ни A, ни B»
    (coordinator "Negatives"; 7-04 t_both_neg shape, verb once, number of the Pāli verb, generic «не устраняют»).
  - Denied negative "…, no ca so [tato] B nappajahati" = «…, но он / она [там] устраняет B» (C.NO_CA_POS_FRAME).
  - "X ṭhapetvā avasesā puggalā [sabbattha] …nappajahanti" = «Кроме X, остальные личности [везде] не устраняют ни …»
    (7-05 apart_persons(), 7-02 SABBATTHA).
  - A line holding answers and then the next question (^6-7-178, ^6-7-182): both rendered in order.
  - "…; apariyāpanne …" (^6-7-180): the semicolon is kept, the next clause starts in lower case.
  - "Pajahanavāre paṭilomaṃ." / "Pajahanavāro." from 7-05 FIXED.

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_7-06_ru.py
Import: importlib.import_module("build_7-06_ru")   (importing never writes any file)
Reuse:  t_pred6(), t_both_neg6(), t_clause6(), answers6(a, generic_bare), tr_line(body, mode)
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
G = importlib.import_module("build_7-05_ru")

CHAPTER = "7-06-anusayayamaka.md"
cap = B.cap

TRANSITIVE = G.TRANSITIVE_05                 # + pajahanti / nappajahanti = «устраняют»
PERSON_NOM = G.PERSON_NOM_05
PERSON_FEM = G.PERSON_FEM_05
RES_T = dict(E.RES_T, so=0)                  # "no ca so B nappajahati" (person section): «но он …»
APART_TAIL = " ṭhapetvā avasesā puggalā"
APART_HEAD_RE = re.compile(r"(.+?" + APART_TAIL + r") (.*)")

# ---------------------------------------------------------------------------------------------
# Source slips rendered as meant (reported in notes-7-06.md); the Pāli file is not touched.
# ---------------------------------------------------------------------------------------------
SLIPS_06 = {
    # ^6-7-193: stray comma inside the negated pair "A ca nappajahati B ca nappajahati"
    "paṭighānusayañca nappajahati, vicikicchānusayañca nappajahati.":
        "paṭighānusayañca nappajahati vicikicchānusayañca nappajahati.",
}

FIXED = dict(G.FIXED)
FIXED["Pajahanāvāre paṭilomaṃ."] = G.FIXED["Pajahanavāre paṭilomaṃ."]   # ^6-7-197 "Pajahanāvāre": spelling slip


# ---------------------------------------------------------------------------------------------
# Predicates (TRANSITIVE_05: singular and plural pajahati)
# ---------------------------------------------------------------------------------------------
def t_pred6(verb, parsed, generic=False, neg_extra=False):
    if verb in C.TRANSITIVE:
        return E.t_pred(verb, parsed, generic, neg_extra)
    ru, neg = TRANSITIVE[verb]
    assert not generic, verb
    neg = neg != neg_extra
    case = E.NEG_OBJ_CASE.get(ru, "acc") if neg else "acc"
    return f"{'не ' if neg else ''}{ru} {C.ru_list(parsed, case, neg)}"


def t_both_neg6(segs, generic):
    """"A ca nappajahati B ca C ca nappajahati" -> «не устраняет ни A, ни B, ни C» (7-04 t_both_neg with the plural
    verbs of TRANSITIVE_05); the verb's number follows the Pāli verb; generic (no person) -> «не устраняют»."""
    ru = TRANSITIVE[segs[0][1]][0]
    assert all(TRANSITIVE[v][0] == ru and TRANSITIVE[v][1] for _, v in segs), segs
    if generic:
        ru = E.GENERIC_3PL[ru]
    case = E.NEG_OBJ_CASE.get(ru, "acc")
    items = []
    for lst, _ in segs:
        t = C.ru_list(C.parse_list(lst), case, True)
        items.append(t if t.startswith("ни ") else "ни " + t)
    return C.BOTH_NEG_FRAME.format(verb=ru, items=", ".join(items))


def t_clause6(s, generic=False):
    segs = C.split_clause(s, TRANSITIVE)
    if len(segs) == 1:
        lst, v = segs[0]
        return t_pred6(v, C.parse_list(lst), generic)
    if len(segs) == 2 and all(l.endswith(" ca") for l, _ in segs):
        segs = [(l[:-3], v) for l, v in segs]
        if all(TRANSITIVE[v][1] for _, v in segs):
            return t_both_neg6(segs, generic)
    raise ValueError(f"clause shape not parsed: {s!r}")


# ---------------------------------------------------------------------------------------------
# Answers
# ---------------------------------------------------------------------------------------------
def _answer(s, generic_bare):
    if s in C.SIMPLE_ANSWERS:
        return C.SIMPLE_ANSWERS[s]
    assert s.endswith("."), s
    body = C.lower1(s[:-1])
    group = None
    m = APART_HEAD_RE.fullmatch(body)
    if m:
        group, body = m.group(1), m.group(2)
        person = None
    else:
        person, body = C._take(body, PERSON_NOM)
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
        return C.RES_FEM.get(r, r) if person in PERSON_FEM else r

    generic = not person and not group and (bool(loci) or generic_bare)
    if group:
        assert not loci and res is None and not neg, s
        head = G.apart_persons(group) + " " + (D.SABBATTHA + " " if sabb else "")
    elif sabb:
        raise ValueError(f"sabbattha without a group: {s!r}")
    elif person and loci:
        assert res in ("so tato", "te tato"), s
        head = C.ANSWER_INTRO_PERSON_PLACE.format(person=cap(PERSON_NOM[person]),
                                                  loci=C.LOCI_SEP.join(C.LOCI[x] for x in loci), res=res_ru(res))
    elif loci:
        assert res == "tato", s
        head = C.ANSWER_INTRO_PLACE.format(loci=C.LOCI_SEP.join(C.LOCI[x] for x in loci), res=C.RES[res])
    elif person:
        assert res is None, s
        head = C.ANSWER_INTRO_PERSON.format(person=cap(PERSON_NOM[person]))
    else:
        raise ValueError(f"answer intro not parsed: {s!r}")
    out = head + t_clause6(main, generic)
    if neg:
        nres, neg = C._take(neg, RES_T)
        exp = "so" if (person and not loci) else res
        assert nres == exp, s
        segs = C.split_clause(neg, TRANSITIVE)
        assert len(segs) == 1, s
        lst, v = segs[0]
        np = t_pred6(v, C.parse_list(lst), generic, neg_extra=True)
        pos = TRANSITIVE[v][1]
        out += (C.NO_CA_POS_FRAME if pos else C.NO_CA_FRAME).format(res=res_ru(nres), pos_pred=np, neg_pred=np)
    return cap(out) + "."


def answer_sentence6(s, generic_bare=False):
    pe = s.endswith(D.PE + ".")
    if pe:
        s = s[:-len(D.PE + ".")] + "."
    out = _answer(s, generic_bare)
    if pe:
        assert out.endswith("."), out
        out = out[:-1] + D.PE_END
    return out


SEMI = "; "


def answers6(a, generic_bare=False):
    """Sentences split at ". "; a "; " inside a sentence (^6-7-180) is kept, the clause after it in lower case."""
    out = []
    for sent in re.split(r"(?<=\.) (?=\S)", a.strip()):
        parts = sent.split(SEMI)
        ru = [answer_sentence6(p + ("." if i < len(parts) - 1 else ""), generic_bare) for i, p in enumerate(parts)]
        for i in range(len(ru) - 1):
            assert ru[i].endswith("."), ru[i]
            ru[i] = ru[i][:-1]
            ru[i + 1] = C.lower1(ru[i + 1])
        out.append(SEMI.join(ru))
    return " ".join(out)


# ---------------------------------------------------------------------------------------------
# Lines; mode = "okasa" inside an "…okāso" section
# ---------------------------------------------------------------------------------------------
def preprocess(body):
    for a, b in SLIPS_06.items():
        body = body.replace(a, b)
    return G.preprocess(body)                 # " …pe…" spacing, "-ānusayañca" -> "-ānusayaṃ ca"


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
    gb = mode == "okasa"
    if "?" in text:
        q, _, a = text.partition("?")
        lead = ""
        if ". " in q:                         # answers, then the next question on the same line (^6-7-178, -182)
            assert not label, body
            k = q.rindex(". ") + 1
            lead, q = answers6(q[:k], gb) + " ", q[k + 1:]
        out = label + lead + G.question(q)
        if a.strip():
            out += " " + answers6(a, gb)
    else:
        out = label + answers6(text, gb)
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
FINISHED = G.FINISHED + ["7-05-anusayayamaka.md"]


def check_local(ru, src):
    E.check_local(ru)
    assert "\n\n\n" not in ru and "\r" not in ru
    assert not re.search(r"(?<!\w)и не устраня", ru), "negated pairs must be «не устраняет ни A, ни B»"
    assert "не устраняет ни скрытой" not in ru and "не устраняют ни скрытой" not in ru, "accusative after «устранять»"
    for p, r in zip(src.split("\n"), ru.split("\n")):
        if "nappajah" in p:
            assert "не устраня" in r, r
        if "no ca" in p:
            assert ", но " in r and "но не так" not in r, r
            assert p.count("no ca") == r.count(", но "), r
        if "ṭhapetvā avasesā puggalā" in p:
            assert p.count("ṭhapetvā") == r.count("Кроме "), r
        if "sabbattha" in p:
            assert p.count("sabbattha") == r.count(" везде "), r
        assert p.count("?") == r.count("?"), r


def check_consistency_06(src, ru):
    """Identical Pāli line -> identical Russian line, across the finished chapters and within this one per mode."""
    seen, ambiguous = {}, set()
    for name in FINISHED:
        p, r = B.PALI_DIR / name, B.OUT_DIR / name
        if not r.exists():
            continue
        for pl, rl in zip(p.read_text(encoding="utf-8").split("\n"), r.read_text(encoding="utf-8").split("\n")):
            pb, rb = B.ID_ANY.sub("", pl).strip(), B.ID_ANY.sub("", rl).strip()
            if pb in seen and seen[pb] != rb:
                # 7-05 bare answers ("Mānānusayaṃ pajahati.") differ by section (implicit subject): skip them
                assert name == "7-05-anusayayamaka.md", (name, pb)
                ambiguous.add(pb)
            seen.setdefault(pb, rb)
    for pb in ambiguous:
        del seen[pb]
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
    G.check_crossbook_05()
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    ru = unicodedata.normalize("NFC", translate_file(src))
    check_local(ru, src)
    check_consistency_06(src, ru)
    B.check_pair(src, ru, CHAPTER)
    with open(B.OUT_DIR / CHAPTER, "w", encoding="utf-8", newline="\n") as f:
        f.write(ru)
    print("written", B.OUT_DIR / CHAPTER, "lines", len(ru.split("\n")))
    print("cross-book asserts OK; consistency OK; per-line checks OK")


if __name__ == "__main__":
    main()
