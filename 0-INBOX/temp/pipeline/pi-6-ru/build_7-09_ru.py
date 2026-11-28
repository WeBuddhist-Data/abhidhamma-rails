"""Russian plain zero-shot of pi-6 (Yamaka): 7-09-anusayayamaka.md (Pahīnavāra: anuloma person / place /
person and place; paṭiloma person).

Family C frames come from build_7-01_ru … build_7-08_ru (imported, never edited): pahīno / pahīnā = «устранена /
устранены», appahīno / appahīnā = «не устранена / не устранены» (7-01 VERB, pi-5 «у архата страсть устранена»),
the person / place question shape, partial answers (C.no_ca), both-forms (C.BOTH_FRAME, C.both_neg), the "; "
clause join (7-06 SEMI), "…pe…." -> «…» (7-02), headings (7-01 heading(), 7-07 alias pattern). New here (all listed
in notes-7-09.md):
  - NA_VATTABBA: '[X] na vattabbo "pahīno"ti vā "appahīno"ti vā' = «[о X] не следует говорить «устранена» или
    «не устранена»» (pi-5 "na vattabbaṃ soti vā aññoti vā" = «не следует говорить «тот же или другой»»); plural
    vattabbā / pahīnā = «устранены» / «не устранены»; X in the prepositional case «о A и B».
  - bare answer clause without person / place ("Mānānusayo pahīno; …") = «Устранена скрытая склонность к …; …».
  - "Pahīnavāre anulomaṃ." = «Утвердительная форма в разделе об устранённом.»; prepared for 7-10:
    "Pahīnavāre paṭilomaṃ.", "Pahīnavāro." (FIXED); heading "Pahīnavāra" = "Pahīnavāro" (sample «Раздел об
    устранённом»).
  - variant note ^6-7-270 "[pahīno (sī. ka.) anusayavārena pana na sameti]" = «[вариант чтения (Sī., Ka.): pahīno,
    что не согласуется с разделом о скрытых склонностях]» (pi-4 «…, что согласуется с подкомментарием …»).
  - stray punctuation kept (user rule): ^6-7-306 "Puthujjanassa avijjānusayo ca appahīno; kāmarāgānusayo ca …
    appahīnā." = «У обычного человека не устранены ни A; ни B, …»; ^6-7-307 the same with "," (the Russian already
    has a comma there, as 7-08 STRAY_COMMA).

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_7-09_ru.py [--dry]
Import: importlib.import_module("build_7-09_ru")   (importing never writes any file)
Reuse (7-10 / 7-11): na_vattabba(), answer_sentence9(), answers9(), tr_line9(body), translate_file(src),
        FIXED, HEADING_ALIAS, STRAY_09 / stray_fix(), check_local9(), FINISHED
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
H = importlib.import_module("build_7-06_ru")
M = importlib.import_module("build_7-07_ru")
N8 = importlib.import_module("build_7-08_ru")

CHAPTER = "7-09-anusayayamaka.md"
cap = B.cap

# ---------------------------------------------------------------------------------------------
# pahīna (7-01 VERB; pi-5 «устранена»)
# ---------------------------------------------------------------------------------------------
PAHINA_RU = {"o": C.VERB["pahīno"][0], "ā": C.VERB["pahīnā"][0]}           # устранена / устранены
APPAHINA_RU = {"o": "не " + C.VERB["appahīno"][0], "ā": "не " + C.VERB["appahīnā"][0]}
assert PAHINA_RU == {"o": "устранена", "ā": "устранены"}
assert C.VERB["appahīno"][1] and C.VERB["appahīnā"][1]

# ---------------------------------------------------------------------------------------------
# na vattabbo "pahīno"ti vā "appahīno"ti vā (pi-5 «не следует говорить «тот же или другой»»)
# ---------------------------------------------------------------------------------------------
NA_VATTABBA_RE = re.compile(r'(?:(.+) )?na vattabb(o|ā) "pahīn(o|ā)"ti vā "appahīn(o|ā)"ti vā')
NA_VATTABBA_FRAME = "не следует говорить «{pos}» или «{neg}»"
NA_VATTABBA_ABOUT = "о {x} "                                                   # X in the prepositional case


def na_vattabba(m):
    """'kāmarāgānusayo ca paṭighānusayo ca na vattabbā "pahīnā"ti vā "appahīnā"ti vā' ->
    «о скрытой склонности к чувственной страсти и скрытой склонности к неприязни не следует говорить «устранены»
    или «не устранены»»; without a subject: «не следует говорить «устранена» или «не устранена»»."""
    subj, num, n1, n2 = m.groups()
    assert num == n1 == n2, m.group(0)
    about = NA_VATTABBA_ABOUT.format(x=C.ru_list(C.parse_list(subj), "prep")) if subj else ""
    return about + NA_VATTABBA_FRAME.format(pos=PAHINA_RU[num], neg=APPAHINA_RU[num])


# ---------------------------------------------------------------------------------------------
# Answers (7-02 _answer: person / places / person and places; + bare clause; + na vattabbo; "; " as 7-06)
# ---------------------------------------------------------------------------------------------
def _answer9(s):
    if s in C.SIMPLE_ANSWERS:
        return C.SIMPLE_ANSWERS[s]
    assert s.endswith("."), s
    body = C.lower1(s[:-1])
    m = NA_VATTABBA_RE.fullmatch(body)
    if m:
        return cap(na_vattabba(m)) + "."
    person, body = C._take(body, C.PERSON_GEN)
    loci = []
    while True:
        loc, body = C._take(body, C.LOCI)
        if not loc:
            break
        loci.append(loc)
    res, body = C._take(body, D.RES_HEAD)
    main, _, neg = body.partition(", no ca ")

    def res_ru(k):
        r = C.RES[k]
        return C.RES_FEM.get(r, r) if person in C.PERSON_FEM else r

    if person and loci:
        assert res in ("tassa tattha", "tesaṃ tattha"), s
        head = C.ANSWER_INTRO_PERSON_PLACE.format(person=C.PERSON_GEN[person],
                                                  loci=C.LOCI_SEP.join(C.LOCI[x] for x in loci), res=res_ru(res))
    elif loci:
        assert res in ("ettha", "tattha"), s
        head = C.ANSWER_INTRO_PLACE.format(loci=C.LOCI_SEP.join(C.LOCI[x] for x in loci), res=C.RES[res])
    elif person:
        assert res is None, s
        head = C.ANSWER_INTRO_PERSON.format(person=C.PERSON_GEN[person])
    else:                                  # "Mānānusayo pahīno; …" (no person, no place in the Pāli)
        assert res is None and not neg, s
        head = ""
    out = head + C.clause(main)
    if neg:
        nres, neg = C._take(neg, D.RES_NEG)
        exp = {(True, True): ("tassa tattha", "tesaṃ tattha"), (False, True): ("tattha",),
               (True, False): ("tassa", "tesaṃ")}[(bool(person), bool(loci))]
        assert nres in exp, s
        segs = C.split_clause(neg, C.VERB)
        assert len(segs) == 1, s
        lst, v = segs[0]
        # "no" negates the verb that follows: no ca … pahīno = «не устранена»; no ca … appahīno = «устранена»
        out += C.no_ca(v, C.parse_list(lst), res_ru(nres))
    return cap(out) + "."


def answer_sentence9(s):
    pe = s.endswith(D.PE + ".")
    if pe:
        s = s[:-len(D.PE + ".")] + "."
    out = _answer9(s)
    if pe:
        assert out.endswith("."), out
        out = out[:-1] + D.PE_END
    return out


def answers9(a):
    """Sentences split at ". "; a "; " inside a sentence is kept (7-06 / 7-07), the clause after it in lower case."""
    out = []
    for sent in re.split(r"(?<=\.) (?=\S)", a.strip()):
        parts = sent.split(H.SEMI)
        ru = [answer_sentence9(p + ("." if i < len(parts) - 1 else "")) for i, p in enumerate(parts)]
        for i in range(len(ru) - 1):
            assert ru[i].endswith("."), ru[i]
            ru[i] = ru[i][:-1]
            ru[i + 1] = C.lower1(ru[i + 1])
        out.append(H.SEMI.join(ru))
    return " ".join(out)


# ---------------------------------------------------------------------------------------------
# Variant note and stray punctuation (the Pāli file is untouched)
# ---------------------------------------------------------------------------------------------
ANUSAYAVARA_INSTR = "разделом " + B.SECTION_HEADINGS["Anusayavāra"][len("Раздел "):]   # разделом о скрытых склонностях
VARIANTS_09 = {   # Pāli bracket -> (Russian word it follows, Russian bracket)
    " [pahīno (sī. ka.) anusayavārena pana na sameti]":
        (PAHINA_RU["ā"], f"[вариант чтения (Sī., Ka.): pahīno, что не согласуется с {ANUSAYAVARA_INSTR}]"),   # ^6-7-270
}
# Stray punctuation inside a negated both-form (user rule: it stays as written).
# Pāli key -> (text parsed, Russian prefix before the mark, the mark)
PUTHU_NEG = (C.ANSWER_INTRO_PERSON.format(person=cap(C.PERSON_GEN["puthujjanassa"])) + "не "
             + C.RU_PLURAL[C.VERB["appahīno"][0]] + " ни " + C.anusaya("avijjā"))
STRAY_09 = {
    "Puthujjanassa avijjānusayo ca appahīno; kāmarāgānusayo": (
        "Puthujjanassa avijjānusayo ca appahīno kāmarāgānusayo", PUTHU_NEG, ";"),           # ^6-7-306
    "Puthujjanassa avijjānusayo ca appahīno, kāmarāgānusayo": (
        "Puthujjanassa avijjānusayo ca appahīno kāmarāgānusayo", PUTHU_NEG, ","),           # ^6-7-307
}


def stray_fix(body):
    """-> (body to parse, [(Russian prefix, mark)])."""
    marks = []
    for k, (rep, prefix, mark) in STRAY_09.items():
        if k in body:
            body = body.replace(k, rep)
            marks.append((prefix, mark))
    return body, marks


def stray_apply(out, marks):
    for prefix, mark in marks:
        assert out.count(prefix + ", ни ") == 1, out
        out = out.replace(prefix + ", ни ", prefix + mark + " ни ")
    return out


# ---------------------------------------------------------------------------------------------
# Fixed lines and headings
# ---------------------------------------------------------------------------------------------
PAHINAVARO = B.SECTION_HEADINGS["Pahīnavāro"]                      # «Раздел об устранённом»
PAHINAVARE_FRAME = "{form} в разделе об устранённом."             # Pahīnavāre anulomaṃ / paṭilomaṃ.
assert PAHINAVARE_FRAME.endswith(PAHINAVARO.replace("Раздел ", "") + ".")
FIXED = dict(M.FIXED)
FIXED["Pahīnavāre anulomaṃ."] = PAHINAVARE_FRAME.format(form=cap(B.SECTION_HEADINGS["anulomaṃ"]))
FIXED["Pahīnavāre paṭilomaṃ."] = PAHINAVARE_FRAME.format(form=cap(B.SECTION_HEADINGS["paccanīkaṃ"]))   # 7-10
FIXED["Pahīnavāro."] = C.VARO_CLOSING.format(heading=PAHINAVARO)                                     # 7-10
HEADING_ALIAS = dict(M.HEADING_ALIAS, **{"Pahīnavāra": "Pahīnavāro"})


def heading9(body):
    m = C.HEAD_RE.fullmatch(body)
    if m.group(3) in HEADING_ALIAS:
        body = body[: m.start(3)] + HEADING_ALIAS[m.group(3)]
    return C.heading(body)


# ---------------------------------------------------------------------------------------------
# Lines
# ---------------------------------------------------------------------------------------------
def tr_line9(body):
    if not body.strip():
        return ""
    if body in FIXED:
        return FIXED[body]
    if body.startswith("#"):
        return heading9(body)
    variants = [v for k, v in VARIANTS_09.items() if k in body]
    for k in VARIANTS_09:
        body = body.replace(k, "")
    body, marks = stray_fix(body)
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
        lead = ""
        if ". " in q:                         # answers, then the next question on the same line (7-06)
            assert not label, body
            k = q.rindex(". ") + 1
            lead, q = answers9(q[:k]) + " ", q[k + 1:]
        out = label + lead + D.question(q)
        if a.strip():
            out += " " + answers9(a)
    else:
        out = label + answers9(text)
    out += tail
    for word, ru in variants:
        assert word + " " in out, out
        out = out.replace(word + " ", word + " " + ru + " ", 1)
    return stray_apply(out, marks)


def translate_file(src_text):
    out = []
    for line in src_text.split("\n"):
        body, bid = B.ID_RE.match(line).groups()
        out.append(tr_line9(body) + (bid or ""))
    return "\n".join(out)


# ---------------------------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------------------------
CROSSBOOK_09 = [
    ("5", "не следует говорить «тот же или другой»"),        # na vattabbaṃ … ti vā … ti vā
    ("4", ", что согласуется с подкомментарием"),             # "… pana sameti" in a variant note
    ("1", "[вариант чтения (Sī., Ka.): "),                   # variant label
    ("5", "у архата страсть устранена"),                     # pahīna (7-01)
]
FINISHED = N8.FINISHED + ["7-08-anusayayamaka.md"]


def check_crossbook_09():
    cache, missing = {}, []
    for b, s in CROSSBOOK_09:
        if b not in cache:
            cache[b] = "\n".join(p.read_text(encoding="utf-8") for p in sorted(B.RAILS[b].glob("*.md")))
        if s not in cache[b]:
            missing.append((b, s))
    if missing:
        raise AssertionError(f"cross-book strings not found in the pi-1..5 rails: {missing}")
    return True


def check_local9(ru, src):
    E.check_local(re.sub(r"\[[^\]]*\]", "", ru))          # no «ли», no Latin outside variant brackets
    assert "\n\n\n" not in ru and "\r" not in ru
    assert not re.search(r"(?<!\w)и не устранен", ru), "negated pairs must be «не устранена ни A, ни B»"
    assert "ни скрытой" not in ru and "ни скрытую" not in ru
    for p, r in zip(src.split("\n"), ru.split("\n")):
        if p.startswith("#"):
            continue
        if "pahīn" in p and not p.startswith("Pahīnavāre"):
            assert "устранен" in r, r
        if "appahīn" in p.replace('"appahīn', ""):
            assert "не устранен" in r, r
        assert p.count("no ca") == r.count(", но "), r
        assert p.count("vattabb") == r.lower().count("не следует говорить «"), r
        assert p.count("?") == r.count("?"), r
        assert p.count('"') == 2 * r.count("«") == 2 * r.count("»"), r
        assert p.count("; ") == r.count("; "), r


def dry():
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    for i, r in enumerate(translate_file(src).split("\n"), 1):
        print(i, r)


def main():
    B.check_crossbook()
    C.check_crossbook_c()
    D.check_crossbook_02()
    E.check_crossbook_03()
    M.G.check_crossbook_05()
    M.check_crossbook_07()
    check_crossbook_09()
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    ru = unicodedata.normalize("NFC", translate_file(src))
    check_local9(ru, src)
    shared = M.check_consistency7(src, ru, FINISHED)
    B.check_pair(src, ru, CHAPTER)
    with open(B.OUT_DIR / CHAPTER, "w", encoding="utf-8", newline="\n") as f:
        f.write(ru)
    print("written", B.OUT_DIR / CHAPTER, "lines", len(ru.split("\n")), "| lines shared with finished chapters:",
          shared)
    print("cross-book asserts OK; consistency OK; per-line checks OK")


if __name__ == "__main__":
    if "--dry" in sys.argv:
        dry()
    else:
        main()
