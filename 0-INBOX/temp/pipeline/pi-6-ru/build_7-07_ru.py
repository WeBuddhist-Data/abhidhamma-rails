"""Russian plain zero-shot of pi-6 (Yamaka): 7-07-anusayayamaka.md (Pariññāvāra: anuloma person / place /
person and place; paṭiloma person / place).

Family C frames come from build_7-01_ru … build_7-06_ru (imported, never edited); family E (pariññā) from
build_2-02_ru (PJ_FORMS, PJ_RU, pj_pred: «полностью понимает», negated «не понимает полностью», never
«не полностью понимает»). Every frame not listed in notes-7-07.md is theirs. New or first used here:
  - parijānāti / parijānanti and "na parijānāti" / "na parijānanti" in the family C shapes (PJ_VERBS, pj_t_pred()):
    person «полностью понимает», generic yato … tato … «полностью понимают» (7-03 Q_YATO, GENERIC_3PL), group
    «Кроме …, остальные личности не понимают полностью ни A, ни B» (7-05 apart_persons(), coordinator "Negatives").
  - tadekaṭṭha with pariññā (7-05 frames, verb and participle of pariññā): bare «Полностью понимает то, что
    пребывает вместе с полностью понимаемым.»; pair «полностью понимает A и полностью понимает B, пребывающую
    вместе с полностью понимаемой»; with a Pāli comma «…A, полностью понимает B, …»; with "ca … ca" the both-form
    «и полностью понимает A, и полностью понимает B, пребывающую …».
  - "Pariññāvāre anulomaṃ." = «Утвердительная форма в разделе о полном понимании.»; prepared for 7-08:
    "Pariññāvāre paṭilomaṃ.", "Pariññāvāro." (FIXED); heading "Pariññāvāra" = "Pariññāvāro".

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_7-07_ru.py
Import: importlib.import_module("build_7-07_ru")   (importing never writes any file)
Reuse (7-08): PJ_VERBS, pj_t_pred(), pj_both_neg(), pj_clause(), answers7(a, generic_bare), question7(q),
        tr_line(body, mode), translate_file(src), preprocess(), FIXED, check_local7(), check_consistency7()
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
H = importlib.import_module("build_7-06_ru")
P = importlib.import_module("build_2-02_ru")

CHAPTER = "7-07-anusayayamaka.md"
cap = B.cap

# ---------------------------------------------------------------------------------------------
# Verbs. "na parijānāti" is joined to one token "na_parijānāti" for parsing only (preprocess()).
# value = (2-02 PJ_FORMS key, negated?)
# ---------------------------------------------------------------------------------------------
NEG_JOIN = "na_"
PJ_VERBS = {
    "parijānāti": ("parijānāti", False), "parijānanti": ("parijānanti", False),
    "na_parijānāti": ("parijānāti", True), "na_parijānanti": ("parijānanti", True),
}
assert C.TRANSITIVE["parijānāti"][0] == P.PJ_RU[("parijānāti", "pres", "sg")][0]   # 7-01 proposal = 2-02
assert E.GENERIC_3PL["полностью понимает"] == P.PJ_RU[("parijānāti", "pres", "pl")][0]
TV7 = "|".join(re.escape(k) for k in sorted(PJ_VERBS, key=len, reverse=True))


def _num(form, generic):
    """Russian number: generic subject (yato … tato …) = 3rd person plural; else the Pāli verb's number."""
    return "pl" if generic else P.PJ_FORMS[form][2]


def pj_t_pred(verb, parsed, generic=False, neg_extra=False):
    """parijānāti -> «полностью понимает A»; na parijānāti -> «не понимает полностью A» / «… ни A, ни B»
    (accusative kept, as 7-05 / 7-06 «устраняет»); generic -> «полностью понимают / не понимают полностью»."""
    form, neg = PJ_VERBS[verb]
    neg = neg != neg_extra
    return P.pj_pred(form, C.ru_list(parsed, "acc", neg), _num(form, generic), neg)


def pj_both_neg(segs, generic):
    """"A ca na parijānāti B ca C ca na parijānāti" -> «не понимает полностью ни A, ни B, ни C»
    (C.BOTH_NEG_FRAME, verb once; number of the Pāli verb; generic «не понимают полностью»)."""
    forms = {PJ_VERBS[v][0] for _, v in segs}
    assert len(forms) == 1 and all(PJ_VERBS[v][1] for _, v in segs), segs
    form = forms.pop()
    verb = P.pj_forms(form, _num(form, generic))[1]
    assert verb.startswith("не "), verb
    items = []
    for lst, _ in segs:
        t = C.ru_list(C.parse_list(lst), "acc", True)
        items.append(t if t.startswith("ни ") else "ни " + t)
    return C.BOTH_NEG_FRAME.format(verb=verb[3:], items=", ".join(items))


# ---------------------------------------------------------------------------------------------
# tadekaṭṭha (7-05 frames; pariññā verb and participle)
# ---------------------------------------------------------------------------------------------
TADEKATTHA = G.TADEKATTHA
PJ_PASSIVE_WITH = {"sg": "вместе с полностью понимаемой", "pl": "вместе с полностью понимаемыми"}   # cf. 7-05 «устраняемой»
TADEKATTHA_BARE_07 = "полностью понимает то, что пребывает вместе с полностью понимаемым"           # cf. 7-05 TADEKATTHA_BARE
assert G.TADEKATTHA_BARE.replace("устраняет", "полностью понимает").replace(
    "устраняемым", "полностью понимаемым") == TADEKATTHA_BARE_07
TADEKATTHA_PAIR_COMMA = "{p1}, {p2}"     # "A parijānāti, B tadekaṭṭhaṃ parijānāti" (the Pāli comma kept)


def _lnum(parsed):
    return "pl" if len(parsed[0]) > 1 else "sg"


def pj_tadekattha(v1, l1, v2, l2, generic=False, join="pair"):
    """join: "pair" -> 7-05 «P1 и P2»; "comma" -> «P1, P2»; "both" (A ca … B ca tadekaṭṭhaṃ …) -> «и P1, и P2»."""
    pa, pb = C.parse_list(l1), C.parse_list(l2)
    p1 = pj_t_pred(v1, pa, generic)
    form, neg = PJ_VERBS[v2]
    assert not neg, (v2, l2)
    verb = P.pj_forms(form, _num(form, generic))[0]
    p2 = G.TADEKATTHA_OBJ.format(verb=verb, obj=C.ru_list(pb, "acc"), part=G.TADEKATTHA_PART[_lnum(pb)],
                                 with_=PJ_PASSIVE_WITH[_lnum(pa)])
    frame = {"pair": G.TADEKATTHA_PAIR, "comma": TADEKATTHA_PAIR_COMMA, "both": C.BOTH_FRAME}[join]
    return frame.format(p1=p1, p2=p2)


def pj_clause(s, generic=False):
    """One predicate; bare tadekaṭṭha; the tadekaṭṭha pair (plain / comma / both-form); the both-form
    «и P1, и P2»; the negated both-form «не понимает полностью ни A, ни B»."""
    comma = False
    if ", " in s:
        left, right = s.split(", ", 1)
        segs = C.split_clause(left, PJ_VERBS) + C.split_clause(right, PJ_VERBS)
        comma = True
    else:
        segs = C.split_clause(s, PJ_VERBS)
    if len(segs) == 1 and not comma:
        lst, v = segs[0]
        if lst == TADEKATTHA:
            form, neg = PJ_VERBS[v]
            assert not neg and not generic and form == "parijānāti", s
            return TADEKATTHA_BARE_07
        return pj_t_pred(v, C.parse_list(lst), generic)
    if len(segs) != 2:
        raise ValueError(f"clause shape not parsed: {s!r}")
    (l1, v1), (l2, v2) = segs
    if l2.endswith(" " + TADEKATTHA):
        l2 = l2[:-len(TADEKATTHA) - 1]
        if comma:
            return pj_tadekattha(v1, l1, v2, l2, generic, "comma")
        if l1.endswith(" ca") and l2.endswith(" ca"):
            return pj_tadekattha(v1, l1[:-3], v2, l2[:-3], generic, "both")
        assert not l1.endswith(" ca"), s
        return pj_tadekattha(v1, l1, v2, l2, generic, "pair")
    assert not comma and l1.endswith(" ca") and l2.endswith(" ca"), s
    segs = [(l1[:-3], v1), (l2[:-3], v2)]
    if all(PJ_VERBS[v][1] for _, v in segs):
        return pj_both_neg(segs, generic)
    if not any(PJ_VERBS[v][1] for _, v in segs):
        p = [pj_t_pred(v, C.parse_list(l), generic) for l, v in segs]
        return C.BOTH_FRAME.format(p1=p[0], p2=p[1])
    raise ValueError(f"mixed both-form not prepared: {s!r}")


# ---------------------------------------------------------------------------------------------
# Questions: yo … so … (C.Q_WHO), yo yato … so tato … (C.Q_WHO_PLACE), yato … tato … (7-03 Q_YATO, generic)
# ---------------------------------------------------------------------------------------------
Q_YO7 = re.compile(rf"yo( vā pana)?( yato)? (.+?) ({TV7}) (so tato|so) (.+) ({TV7})")
Q_YATO7 = re.compile(rf"yato( vā pana)? (.+?) ({TV7}) tato (.+) ({TV7})")


def unti7(w):
    """parijānātīti -> parijānāti; na_parijānātīti -> na_parijānāti."""
    if w.endswith("īti") and w[:-3] + "i" in PJ_VERBS:
        return w[:-3] + "i"
    return w


def question7(q):
    words = C.lower1(q.strip()).split(" ")
    words[-1] = unti7(words[-1])
    t = " ".join(words)
    m = Q_YO7.fullmatch(t)
    if m:
        vapana, yato, l1, v1, res2, l2, v2 = m.groups()
        assert bool(yato) == (res2 == "so tato"), q
        out = (C.Q_WHO_PLACE if yato else C.Q_WHO).format(p1=pj_t_pred(v1, C.parse_list(l1)),
                                                         p2=pj_t_pred(v2, C.parse_list(l2)))
        return C.KHA_PREFIX + C.lower1(out) if vapana else out
    m = Q_YATO7.fullmatch(t)
    if m:
        vapana, l1, v1, l2, v2 = m.groups()
        out = E.Q_YATO.format(p1=pj_t_pred(v1, C.parse_list(l1), True), p2=pj_t_pred(v2, C.parse_list(l2), True))
        return C.KHA_PREFIX + C.lower1(out) if vapana else out
    raise ValueError(f"question not parsed: {q!r}")


# ---------------------------------------------------------------------------------------------
# Answers (7-06 _answer shape: group «Кроме …», sabbattha, person / places / both; 7-05 bare answers)
# ---------------------------------------------------------------------------------------------
PERSON_NOM = G.PERSON_NOM_05
PERSON_FEM = G.PERSON_FEM_05
RES_T = H.RES_T                      # so tato / te tato / tato / so
APART_HEAD_RE = H.APART_HEAD_RE


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
    else:                                  # "Mānānusayaṃ parijānāti." / "Tadekaṭṭhaṃ parijānāti." (subject implied)
        assert res is None and not neg, s
        head = ""
    out = head + pj_clause(main, generic)
    if neg:
        nres, neg = C._take(neg, RES_T)
        exp = "so" if (person and not loci) else res
        assert nres == exp, s
        segs = C.split_clause(neg, PJ_VERBS)
        assert len(segs) == 1, s
        lst, v = segs[0]
        # "no" negates the verb that follows: no ca … parijānāti = «не понимает полностью»;
        # no ca … na parijānāti = «полностью понимает» (coordinator "Negatives")
        np = pj_t_pred(v, C.parse_list(lst), generic, neg_extra=True)
        pos = PJ_VERBS[v][1]
        if nres:
            out += (C.NO_CA_POS_FRAME if pos else C.NO_CA_FRAME).format(res=res_ru(nres), pos_pred=np, neg_pred=np)
        else:
            out += E.NO_CA_BARE_FRAME.format(neg_pred=np)
    return cap(out) + "."


def answer_sentence7(s, generic_bare=False):
    pe = s.endswith(D.PE + ".")
    if pe:
        s = s[:-len(D.PE + ".")] + "."
    out = _answer(s, generic_bare)
    if pe:
        assert out.endswith("."), out
        out = out[:-1] + D.PE_END
    return out


def answers7(a, generic_bare=False):
    """Sentences split at ". "; a "; " inside a sentence is kept (7-06 answers6), the clause after it in lower case."""
    out = []
    for sent in re.split(r"(?<=\.) (?=\S)", a.strip()):
        parts = sent.split(H.SEMI)
        ru = [answer_sentence7(p + ("." if i < len(parts) - 1 else ""), generic_bare) for i, p in enumerate(parts)]
        for i in range(len(ru) - 1):
            assert ru[i].endswith("."), ru[i]
            ru[i] = ru[i][:-1]
            ru[i + 1] = C.lower1(ru[i + 1])
        out.append(H.SEMI.join(ru))
    return " ".join(out)


# ---------------------------------------------------------------------------------------------
# Fixed lines and headings
# ---------------------------------------------------------------------------------------------
PARINNAVARO = B.SECTION_HEADINGS["Pariññāvāro"]                         # «Раздел о полном понимании»
PARINNAVARE_FRAME = "{form} в разделе о полном понимании."               # Pariññāvāre anulomaṃ / paṭilomaṃ.
assert PARINNAVARE_FRAME.endswith(PARINNAVARO.replace("Раздел ", "") + ".")
FIXED = dict(H.FIXED)
FIXED["Pariññāvāre anulomaṃ."] = PARINNAVARE_FRAME.format(form=cap(B.SECTION_HEADINGS["anulomaṃ"]))
FIXED["Pariññāvāre paṭilomaṃ."] = PARINNAVARE_FRAME.format(form=cap(B.SECTION_HEADINGS["paccanīkaṃ"]))   # 7-08
FIXED["Pariññāvāro."] = C.VARO_CLOSING.format(heading=PARINNAVARO)                                    # 7-08 (= 2-02)
HEADING_ALIAS = {"Pariññāvāra": "Pariññāvāro"}     # as the sample's Pajahanavāra / Sānusayavāra pairs


def heading7(body):
    m = C.HEAD_RE.fullmatch(body)
    hashes, lab, text = m.groups()
    if text in HEADING_ALIAS:
        body = body[: m.start(3)] + HEADING_ALIAS[text]
    return C.heading(body)


# ---------------------------------------------------------------------------------------------
# Lines; mode = "okasa" inside an "…okāso" section (bare answers take the generic subject)
# ---------------------------------------------------------------------------------------------
NA_RE = re.compile(r"(?<!\S)na (parijān)")


def preprocess(body):
    text = C.preprocess(body)                         # " …pe…" spacing
    text = text.replace("ānusayañca", "ānusayaṃ ca")  # accusative sandhi in lists (7-05)
    return NA_RE.sub(NEG_JOIN + r"\1", text)          # "na parijānāti" -> one token (parsing only)


def tr_line(body, mode="puggala"):
    if not body.strip():
        return ""
    if body in FIXED:
        return FIXED[body]
    if body.startswith("#"):
        return heading7(body)
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
        if ". " in q:                         # answers, then the next question on the same line (7-06)
            assert not label, body
            k = q.rindex(". ") + 1
            lead, q = answers7(q[:k], gb) + " ", q[k + 1:]
        out = label + lead + question7(q)
        if a.strip():
            out += " " + answers7(a, gb)
    else:
        out = label + answers7(text, gb)
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
CROSSBOOK_07 = [
    ("5", "полностью понимает страдание"), ("5", "не понимает полностью страдание"),   # parijānāti (as 2-02)
    ("1", "пребывающие вместе с ними"),                                                 # tadekaṭṭha
]
FINISHED = H.FINISHED + ["7-06-anusayayamaka.md"]


def check_crossbook_07():
    cache, missing = {}, []
    for b, s in CROSSBOOK_07:
        if b not in cache:
            cache[b] = "\n".join(p.read_text(encoding="utf-8") for p in sorted(B.RAILS[b].glob("*.md")))
        if s not in cache[b]:
            missing.append((b, s))
    if missing:
        raise AssertionError(f"cross-book strings not found in the pi-1..5 rails: {missing}")
    return True


def check_local7(ru, src):
    E.check_local(ru)                                       # no «ли», no Latin, no «но не так, что»
    assert "\n\n\n" not in ru and "\r" not in ru
    assert "не полностью" not in ru, "negated parijānāti = «не понимает полностью» (2-02)"
    assert "не понимает полностью ни скрытой" not in ru and "не понимают полностью ни скрытой" not in ru
    assert not re.search(r"(?<!\w)и не понима", ru), "negated pairs must be «не понимает полностью ни A, ни B»"
    for p, r in zip(src.split("\n"), ru.split("\n")):
        if "parijān" in p:
            assert "понима" in r, r
        if re.search(r"(?<!\S)na parijān", p):
            assert "не понимает полностью" in r or "не понимают полностью" in r, r
        if "no ca" in p:
            assert p.count("no ca") == r.count(", но "), r
        if "ṭhapetvā avasesā puggalā" in p:
            assert p.count("ṭhapetvā") == r.count("Кроме "), r
        if "sabbattha" in p:
            assert p.count("sabbattha") == r.count(" " + D.SABBATTHA + " "), r
        if "tadekaṭṭh" in p.lower():
            assert p.lower().count("tadekaṭṭh") == r.count("пребыва"), r
        assert p.count("?") == r.count("?"), r


def check_consistency7(src, ru, finished=None):
    """Identical Pāli line -> identical Russian line, across the finished anusaya chapters (7-05's bare answers
    are section-dependent and skipped, as 7-06 does) and within this chapter per mode."""
    seen, ambiguous = {}, set()
    for name in (finished or FINISHED):
        p, r = B.PALI_DIR / name, B.OUT_DIR / name
        if not r.exists():
            continue
        for pl, rl in zip(p.read_text(encoding="utf-8").split("\n"), r.read_text(encoding="utf-8").split("\n")):
            pb, rb = B.ID_ANY.sub("", pl).strip(), B.ID_ANY.sub("", rl).strip()
            if pb in seen and seen[pb] != rb:
                assert name == "7-05-anusayayamaka.md", (name, pb)
                ambiguous.add(pb)
            seen.setdefault(pb, rb)
    for pb in ambiguous:
        del seen[pb]
    local, mode, shared = {}, "puggala", 0
    for p, r in zip(src.split("\n"), ru.split("\n")):
        if p.startswith("#"):
            mode = E.mode_of(B.ID_RE.match(p).group(1))
        pb, rb = B.ID_ANY.sub("", p).strip(), B.ID_ANY.sub("", r).strip()
        if pb in seen:
            assert seen[pb] == rb, f"inconsistent with a finished chapter: {pb!r}"
            shared += bool(pb)
        key = (mode == "okasa", pb)
        if key in local:
            assert local[key] == rb, f"inconsistent: {pb!r}"
        local[key] = rb
    return shared


def main():
    B.check_crossbook()
    C.check_crossbook_c()
    D.check_crossbook_02()
    E.check_crossbook_03()
    G.check_crossbook_05()
    check_crossbook_07()
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    ru = unicodedata.normalize("NFC", translate_file(src))
    check_local7(ru, src)
    shared = check_consistency7(src, ru)
    B.check_pair(src, ru, CHAPTER)
    with open(B.OUT_DIR / CHAPTER, "w", encoding="utf-8", newline="\n") as f:
        f.write(ru)
    print("written", B.OUT_DIR / CHAPTER, "lines", len(ru.split("\n")), "| lines shared with finished chapters:",
          shared)
    print("cross-book asserts OK; consistency OK; per-line checks OK")


if __name__ == "__main__":
    main()
