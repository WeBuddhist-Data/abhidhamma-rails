"""pi-6 Yamaka, G9 (Dhammayamaka 9-01, 9-02, 9-03): Russian RAILS builder.

Built on the frame-setters and the finished groups, imported read-only (importing this file writes nothing):
    G2  = build_rails_G2_ru  (paṇṇatti / pavatti frames, partial / pair answers, headings, colophons)
    G8  = build_rails_G8_ru  (moment phrases, via G45)
    G45 = build_rails_G45_ru (intro_ru(): long person / time / place intros; place answers; pjparse / PJ)
    G6  = build_rails_G6_ru  (unlabeled questions)
    G3  = build_rails_G3_ru  (editorial-note strings; the Dhammayamaka has no editorial notes)
    S   = build_rails_sample_ru (labels, book strings, per-line checks)
New here (later groups may import them): the three classes and «явления» as nouns (kusalā dhammā …; kusalā, kusalaṃ,
kusalaṃ dhammaṃ), the moment subjects of the Dhammayamaka (kusalānaṃ, kusalavippayuttacittassa …, added to
G45.MOM_GEN), the multi-word paṇṇatti frames (pn_question / pn_answer), the bhāvanā frame (bv_question) and the
plural pavatti verbs (uppajjanti … as G2.VERB aliases).

Run: python -I -X utf8 -B build_rails_G9_ru.py             (writes 9-01 / 9-02 / 9-03 and notes-rails-G9.md)
     python -I -X utf8 -B build_rails_G9_ru.py --probe <ch>  (prints sentences without a formula; writes nothing)

Termbase (locked): AI_translation/russian/pi-6-pali-russian-termbase-plain.md + pi-6-ru/termbase/APPROVED.md.
"""
import importlib
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru\rails")
import build_rails_sample_ru as S  # noqa: E402

G2 = importlib.import_module("build_rails_G2_ru")
G8 = importlib.import_module("build_rails_G8_ru")
G3 = importlib.import_module("build_rails_G3_ru")
G45 = importlib.import_module("build_rails_G45_ru")
G6 = importlib.import_module("build_rails_G6_ru")

ROOT, PALI, OUT = S.ROOT, S.PALI, S.OUT
CHAPTERS = ["9-01-dhammayamaka.md", "9-02-dhammayamaka.md", "9-03-dhammayamaka.md"]
cap = S.cap
T = G2.TERMS
SLIPS = []
_CUR = {"id": None}


def slip(note):
    SLIPS.append((_CUR["id"], note))


# =========================================================================== nouns (termbase)
# kusalā dhammā «благие явления», Akusalā dhammā «неблагие явления», Abyākatā dhammā «этически неопределённые
# явления» (termbase; pi-1); kusalā / akusalā / abyākatā alone «благой / неблагой / этически неопределённый» (pl.
# substantive «благие»); kusalaṃ (sg. substantive) «благое»; kusalaṃ dhammaṃ «благое явление»; dhammā «явления».
CLASSES = ["kusal", "akusal", "abyākat"]
for _c in CLASSES:
    _pl, _plg, _pli = S.A(_c, "pl_nom"), S.A(_c, "pl_gen"), S.A(_c, "pl_ins")
    _n, _ng, _ni = S.A(_c, "n_nom"), S.A(_c, "mn_gen"), S.A(_c, "mn_ins")
    G2.register_term(f"{_c}ā", _pl, _plg, _pli, "pl")
    G2.register_term(f"{_c}ā dhammā", f"{_pl} явления", f"{_plg} явлений", f"{_pli} явлениями", "pl")
    G2.register_term(f"{_c}aṃ", _n, _ng, _ni, "n", forms=[f"{_c}añca"])
    G2.register_term(f"{_c}aṃ dhammaṃ", f"{_n} явление", f"{_ng} явления", f"{_ni} явлением", "n")
G2.register_term("dhammā", "явления", "явлений", "явлениями", "pl", forms=["dhamme"])   # dhamma «явление» (pi-1)
CLASS_KEYS = [f"{c}ā dhammā" for c in CLASSES]

# =========================================================================== verbs (plural Pāli forms)
# uppajjanti / nirujjhanti … (termbase: «возникать», «прекращаться», «возникнуть», «прекратиться») are the plural
# forms of G2's verbs; the Russian agrees with the plural noun (возникают / возникали / возникнут / прекращаются …).
for _pl, _base in (("uppajjanti", "uppajjati"), ("uppajjissanti", "uppajjissati"),
                   ("nirujjhanti", "nirujjhati"), ("nirujjhissanti", "nirujjhissati")):
    G2.VERB[_pl] = G2.VERB[_base]


def nca(s):
    """«kusalā ca dhammā» (ca inside the noun phrase) -> «kusalā dhammā ca», so G2.parse_pair sees «X ca V»."""
    return re.sub(r"(?<!\w)(akusalā|kusalā|abyākatā) ca dhammā(?!\w)", r"\1 dhammā ca", s, flags=re.I)


# =========================================================================== moments (G45 intro_ru)
# termbase: kusalānaṃ uppādakkhaṇe «момент возникновения благих явлений»; kusalavippayuttacittassa uppādakkhaṇe
# «момент возникновения ума не связанного с благим» (pi-1 «не связанные с …»; participle phrase between commas as
# G45 «ума, не связанного с жаждой,»); kusalākusalānaṃ «благие и неблагие явления».
G45.MOM_GEN.update({
    "kusalānaṃ": ("благих явлений", False),
    "akusalānaṃ": ("неблагих явлений", False),
    "kusalākusalānaṃ": ("благих и неблагих явлений", False),
    "kusalavippayuttacittassa": ("ума, не связанного с благим", True),
    "akusalavippayuttacittassa": ("ума, не связанного с неблагим", True),
    "kusalavippayuttaakusalavippayuttacittassa": ("ума, не связанного с благим и не связанного с неблагим", True),
    "akusalavippayuttakusalavippayuttacittassa": ("ума, не связанного с неблагим и не связанного с благим", True),
})
G45._MG = "(?P<g>" + "|".join(sorted(map(re.escape, G45.MOM_GEN), key=len, reverse=True)) + ")"
G45.UNITS = None


def person_answer(s):
    """INTRO tesaṃ (tattha) <partial | pair> (G45.intro_ru + G2 partial / pair)."""
    body = G45.norm(nca(s[:-1]))
    if ", asaññasattānaṃ" in body:
        slip("comma before «asaññasattānaṃ» inside the person list; the Russian has a comma there anyway")
    for m in re.finditer(r" tesaṃ(?P<t> tattha)? ", body):
        intro = G45.intro_ru(body[:m.start()])
        if not intro:
            continue
        r = G45.clause(body[m.end():].split(), intro, " там" if m.group("t") else "")
        if r:
            return r + "."
    return None


def place_answer(s):
    return G45.place_answer(nca(s))


# =========================================================================== paṇṇatti (naming), multi-word terms
COP = G2.COP              # «является / являются»
WHAT_NOT = G2.WHAT_NOT    # «То, что не является»
EXCEPT, REST = G2.EXCEPT, G2.REST   # «Кроме», «остальные»


def split2(toks):
    """['dhammā', 'kusalā', 'dhammā'] -> (key1, key2): the one split into two registered terms."""
    for k in range(1, len(toks)):
        a, b = G2.term(" ".join(toks[:k])), G2.term(" ".join(toks[k:]))
        if a and b:
            return a, b
    return None


def unquote(tok):
    return tok[:-2] if tok.endswith("ti") and not G2.term(tok) else tok


def pn_question(s):
    """(Ka) kusalā kusalā dhammā? = (а) Благие являются благими явлениями?
    (Kha) na dhammā na akusalā dhammāti? = (б) То, что не является явлениями, не является неблагими явлениями?"""
    m = re.match(r"^(?P<lab>\((?:Ka|Kha)\)) (?P<b>[^?]+)\?$", s)
    if not m:
        return None
    toks = m.group("b").split()
    toks[-1] = unquote(toks[-1])
    lab = S.LABEL[m.group("lab")]
    if toks[0] == "na":
        if "na" not in toks[1:]:
            return None
        j = toks.index("na", 1)
        a, b = G2.term(" ".join(toks[1:j])), G2.term(" ".join(toks[j + 1:]))
        if not (a and b):
            return None
        return f"{lab} {WHAT_NOT} {T[a]['ins']}, не является {T[b]['ins']}?"
    p = split2(toks)
    if not p:
        return None
    a, b = p
    return f"{lab} {cap(T[a]['nom'])} {COP[G2.num(a)]} {T[b]['ins']}?"


def pn_answer(s):
    # A B ceva C ca. = «A и является B, и является C.» (G2 frame)
    m = re.match(r"^(?P<l>.+) ceva (?P<c>.+) ca\.$", s)
    if m:
        p, c = split2(m.group("l").split()), G2.term(m.group("c"))
        if p and c:
            cp = COP[G2.num(p[0])]
            return f"{cap(T[p[0]]['nom'])} и {cp} {T[p[1]]['ins']}, и {cp} {T[c]['ins']}."
    # Avasesā dhammā na C. = «Остальные явления не являются C.» (G2 «Остальные совокупности не являются …»)
    m = re.match(r"^Avasesā dhammā na (?P<c>.+)\.$", s)
    if m and G2.term(m.group("c")):
        return f"{cap(REST)} {T['dhammā']['nom']} не {COP['pl']} {T[G2.term(m.group('c'))]['ins']}."
    # X ṭhapetvā avasesā dhammā na B, C. = «Кроме X, остальные явления не являются B, но являются C.» (G2)
    m = re.match(r"^(?P<x>\S+) ṭhapetvā avasesā dhammā na (?P<b>\S+), (?P<c>\S+)\.$", s)
    if m and all(G2.term(m.group(k)) for k in "xbc"):
        x, b, c = (G2.term(m.group(k)) for k in "xbc")
        return (f"{EXCEPT} {T[x]['gen']}, {REST} {T['dhammā']['nom']} не {COP['pl']} {T[b]['ins']}, "
                f"но {COP['pl']} {T[c]['ins']}.")
    # Xñca Y ca ṭhapetvā avasesā na ceva B na ca C. = «Кроме X и Y, остальные не являются ни B, ни C.» (G2)
    m = re.match(r"^(?P<x>\S+) (?P<y>\S+) ca ṭhapetvā avasesā na ceva (?P<b>\S+) na ca (?P<c>\S+)\.$", s)
    if m and all(G2.term(m.group(k)) for k in "xybc"):
        x, y, b, c = (G2.term(m.group(k)) for k in "xybc")
        return (f"{EXCEPT} {T[x]['gen']} и {T[y]['gen']}, {REST} не {COP['pl']} ни {T[b]['ins']}, "
                f"ни {T[c]['ins']}.")
    return None


# =========================================================================== bhāvanā (developing / abandoning)
# termbase: bhāveti «развивать», pajahati «устранять» (G45 / pi-5 «устраняет»); nappajahati «не устранять»;
# kusalaṃ dhammaṃ / akusalaṃ dhammaṃ «благое / неблагое явление» (accusative). Frame as G2 / G45 «Кто …, тот …?».
G45.PJ["bhāveti"] = ("развивает", "развивают", "не развивает", "не развивают", "sg")


def bv_question(s):
    """(Ka) yo kusalaṃ dhammaṃ bhāveti so akusalaṃ dhammaṃ pajahatīti? = (а) Кто развивает благое явление, тот
    устраняет неблагое явление?"""
    m = re.match(r"^(?P<lab>\((?:Ka|Kha)\)) yo(?P<vp> vā pana)? (?P<x>\S+ dhammaṃ) (?P<v1>(?:na )?\S+) so "
                 r"(?P<y>\S+ dhammaṃ) (?P<v2>(?:na )?\S+)\?$", s)
    if not m:
        return None
    x, y = G2.term(m.group("x")), G2.term(m.group("y"))
    v1, v2 = G45.pjparse(m.group("v1")), G45.pjparse(m.group("v2"))
    if not (x and y and v1 and v2):
        return None
    lead = "А кто" if m.group("vp") else "Кто"
    return (f"{S.LABEL[m.group('lab')]} {lead} {G45.pjru(v1, 'sg')} {T[x]['acc']}, "
            f"тот {G45.pjru(v2, 'sg')} {T[y]['acc']}?")


# =========================================================================== headings, label lines, closing lines
G2.HEAD.update({k.lower(): v for k, v in {   # termbase
    "Suddhadhammavāro": "раздел о явлениях как таковых",
    "Suddhadhammamūlacakkavāro": "круговой раздел на основе явлений как таковых",
    "Bhāvanāvāro": "раздел о развитии",
}.items()})
G2.COLO["bhāvanāvāro"] = cap("раздел о развитии")   # Bhāvanāvāro. (closing label, as G2's «<X>vāro.»)


def heading(text):
    """'#### 3 Suddhadhammavāro' -> '#### 3 Раздел о явлениях как таковых' (the bare number is kept as written)."""
    m = re.match(r"^(#+) (\d+) (.+)$", text)
    if m:
        return f"{m.group(1)} {m.group(2)} " + G2.heading(f"{m.group(1)} {m.group(3)}").split(" ", 1)[1]
    return G2.heading(text)


def label_line(s):
    """A heading standing as a plain line, e.g. «(Kha) niddeso», «(Ca) paccanīkapuggalokāsā» = «(е) Отрицательная
    форма по личности и месту» (as G6's «(Kha) paccanīkaṃ»)."""
    m = re.match(r"^(\([^)]+\)) (\S+)$", s)
    if m and m.group(1) in S.LABEL and m.group(2).lower() in G2.HEAD:
        return f"{S.LABEL[m.group(1)]} {cap(G2.HEAD[m.group(2).lower()])}"
    return None


FIXED_S = {
    "Dhammayamakaṃ niṭṭhitaṃ.": S.yamaka_done("Dhammayamakaṃ"),   # «Парные вопросы о явлениях завершены.»
    "Namo tassa bhagavato arahato sammāsambuddhassa": S.NAMO,       # pi-1
    "Abhidhammapiṭake": S.PITAKA,                                   # pi-1 «В корзине Абхидхаммы»
}

# =========================================================================== sentence / line translator
RULES = [pn_question, pn_answer, bv_question, G6.pv_question, person_answer, place_answer]


def translate_sentence(s):
    s = s.strip()
    if s in FIXED_S:
        return FIXED_S[s]
    m = re.match(r"^(.+\?)…[Pp]e…\.?$", s)   # «…?…Pe….» = «…?…» (G6)
    if m:
        return translate_sentence(m.group(1)) + "…"
    for fn in RULES:
        r = fn(s)
        if r:
            return r
    return G2.translate_sentence(s)


def split_sentences(pali):
    return re.split(r"(?<=[.?])\s+", pali.strip())


def translate_line(pali):
    """One Pāli line (without its ^id) -> Russian."""
    if pali.startswith("#"):
        return heading(pali)
    if pali in FIXED_S:
        return FIXED_S[pali]
    r = label_line(pali)
    if r:
        return r
    return " ".join(translate_sentence(x) for x in split_sentences(pali))


# =========================================================================== source checks (reported, not changed)
_CLS_RX = re.compile(r"(?<!\w)(akusalā|kusalā|abyākatā)(?: ca)? dhammā", re.I)
_LAST_Q = {"keys": None}


def check_answer_terms(line):
    """A partial / pair answer must name the classes of the question just before it; a mismatch is a source slip
    (translated as written)."""
    if "?" in line:
        q = line.split("?", 1)[0]
        _LAST_Q["keys"] = {k.lower() for k in _CLS_RX.findall(q)}
        rest = line.split("?", 1)[1]
        if not rest.strip() or rest.strip().startswith(("Āmantā", "No.", "Natthi")):
            return
        line = rest
    elif line.startswith(("#", "(")) or _LAST_Q["keys"] is None:
        return
    got = {k.lower() for k in _CLS_RX.findall(line)}
    if got and _LAST_Q["keys"] and not got <= _LAST_Q["keys"]:
        slip(f"answer names {sorted(got - _LAST_Q['keys'])}, the question asks about {sorted(_LAST_Q['keys'])}; "
             f"translated as written")


# =========================================================================== build + checks
def _set_id(sid):
    _CUR["id"] = sid
    G2._CUR["id"] = sid
    G45._CUR["id"] = sid


def render(pali_text):
    blocks, problems = [], []
    for sid, plines in S.segs(pali_text):
        _set_id(sid)
        ru = []
        for i, pl in enumerate(plines):
            body = (S.ID.sub("", pl) if i == len(plines) - 1 else pl).strip()
            check_answer_terms(body)
            r = translate_line(body)
            problems += S.check_line(sid, body, r)
            ru.append(r)
        ru[-1] = f"{ru[-1]} ^{sid}"
        blocks.append("\n".join(ru))
    return "\n\n".join(blocks) + "\n", problems


def probe(ch):
    bad = 0
    for sid, plines in S.segs((PALI / ch).read_text(encoding="utf-8")):
        _set_id(sid)
        for i, pl in enumerate(plines):
            body = (S.ID.sub("", pl) if i == len(plines) - 1 else pl).strip()
            try:
                translate_line(body)
            except (ValueError, KeyError, AssertionError, TypeError) as e:
                bad += 1
                print(sid, "|", e)
    print(ch, "lines without a formula:", bad)


# strings reused unchanged from approved earlier Russian rails (asserted in main)
PI1_STRINGS = ["Благие явления", "Неблагие явления", "Этически неопределённые явления", "не связанные с",
               S.NAMO, S.PITAKA]
PI5_STRINGS = ["развивается", "устраняются", "существ без восприятия"]

# =========================================================================== notes (new recurring formulas)
NOTE_EXAMPLES = [
    "#### 3 Suddhadhammavāro", "#### 4 Suddhadhammamūlacakkavāro", "#### Bhāvanāvāro", "(Kha) niddeso",
    "(Ca) paccanīkapuggalokāsā",
    "(Ka) kusalā kusalā dhammā?", "(Kha) kusalā dhammā kusalā?", "(Kha) dhammā akusalā dhammā?",
    "(Ka) na kusalā na kusalā dhammā?", "(Kha) na dhammā na abyākatā dhammā?", "(Ka) kusalā dhammā?",
    "(Kha) dhammā kusalā?", "(Ka) na kusalā na dhammā?", "(Kha) dhammā kusalā dhammāti?",
    "Akusalā dhammā dhammā ceva akusalā dhammā ca.", "Avasesā dhammā na akusalā dhammā.",
    "Kusalaṃ ṭhapetvā avasesā dhammā na kusalā, dhammā.",
    "Kusalañca dhamme ca ṭhapetvā avasesā na ceva kusalā na ca dhammā.",
    "(Ka) yassa kusalā dhammā uppajjanti tassa abyākatā dhammā uppajjantīti?",
    "(Kha) yassa vā pana yattha akusalā dhammā nirujjhittha tassa tattha kusalā dhammā uppajjantīti?",
    "Yattha kusalā dhammā uppajjanti tattha akusalā dhammā uppajjitthāti?…Pe….",
    "Uppajjanti.", "Nirujjhissanti.", "Uppajjittha.",
    "Arūpe kusalānaṃ uppādakkhaṇe tesaṃ kusalā dhammā uppajjanti, no ca tesaṃ abyākatā dhammā uppajjanti.",
    "Pañcavokāre kusalānaṃ uppādakkhaṇe tesaṃ kusalā ca dhammā uppajjanti abyākatā ca dhammā uppajjanti.",
    "Sabbesaṃ upapajjantānaṃ pavatte kusalavippayuttacittassa uppādakkhaṇe tesaṃ abyākatā dhammā uppajjanti, no ca "
    "tesaṃ kusalā dhammā uppajjanti.",
    "Akusalānaṃ uppādakkhaṇe tesaṃ kusalā dhammā na uppajjanti, no ca tesaṃ akusalā dhammā na uppajjanti.",
    "Sabbesaṃ cittassa bhaṅgakkhaṇe kusalavippayuttaakusalavippayuttacittassa uppādakkhaṇe nirodhasamāpannānaṃ "
    "asaññasattānaṃ tesaṃ kusalā ca dhammā na uppajjanti akusalā ca dhammā na uppajjanti.",
    "Sabbesaṃ cavantānaṃ pavatte cittassa bhaṅgakkhaṇe arūpe akusalānaṃ uppādakkhaṇe tesaṃ kusalā ca dhammā na "
    "uppajjanti abyākatā ca dhammā na uppajjanti.",
    "Asaññasatte tattha abyākatā dhammā uppajjanti, no ca tattha kusalā dhammā uppajjanti.",
    "Catuvokāre pañcavokāre tattha abyākatā ca dhammā uppajjanti kusalā ca dhammā uppajjanti.",
    "Suddhāvāsānaṃ dutiye akusale citte vattamāne tesaṃ tattha akusalā dhammā uppajjittha, no ca tesaṃ tattha kusalā "
    "dhammā uppajjittha.",
    "Suddhāvāsānaṃ dutiye citte vattamāne asaññasattānaṃ tesaṃ tattha kusalā ca dhammā na uppajjittha akusalā ca "
    "dhammā na uppajjittha.",
    "Yassa cittassa anantarā aggamaggaṃ paṭilabhissanti tesaṃ kusalā dhammā uppajjissanti, no ca tesaṃ akusalā dhammā "
    "uppajjissanti.",
    "Aggamaggasamaṅgīnaṃ arahantānaṃ tesaṃ abyākatā dhammā uppajjissanti, no ca tesaṃ kusalā dhammā uppajjissanti.",
    "Pacchimacittasamaṅgīnaṃ tesaṃ kusalā ca dhammā na uppajjissanti abyākatā ca dhammā na uppajjissanti.",
    "Aggamaggassa uppādakkhaṇe yassa cittassa anantarā aggamaggaṃ paṭilabhissanti tassa cittassa uppādakkhaṇe tesaṃ "
    "kusalā dhammā uppajjanti, no ca tesaṃ akusalā dhammā uppajjissanti.",
    "Itaresaṃ kusalānaṃ uppādakkhaṇe tesaṃ kusalā ca dhammā uppajjanti akusalā ca dhammā uppajjissanti.",
    "Aggamaggassa bhaṅgakkhaṇe arahantānaṃ yassa cittassa anantarā aggamaggaṃ paṭilabhissanti tassa cittassa "
    "bhaṅgakkhaṇe asaññasattānaṃ tesaṃ tattha kusalā ca dhammā na uppajjanti akusalā ca dhammā na uppajjissanti.",
    "Sabbesaṃ upapajjantānaṃ pavatte kusalavippayuttacittassa uppādakkhaṇe arūpe kusalākusalānaṃ bhaṅgakkhaṇe tesaṃ "
    "kusalā ca dhammā na uppajjanti abyākatā ca dhammā na nirujjhanti.",
    "Pacchimacittassa bhaṅgakkhaṇe tesaṃ kusalā dhammā uppajjittha, no ca tesaṃ abyākatā dhammā nirujjhissanti.",
    "(Ka) yo kusalaṃ dhammaṃ bhāveti so akusalaṃ dhammaṃ pajahatīti?",
    "(Kha) yo vā pana akusalaṃ dhammaṃ nappajahati so kusalaṃ dhammaṃ na bhāvetīti?",
    "Āmantā…pe….", "Bhāvanāvāro.", "Dhammayamakaṃ niṭṭhitaṃ.", "Abhidhammapiṭake",
]


def notes_md():
    L = ["# notes-rails-G9: Dhammayamaka frames (9-01, 9-02, 9-03)", "",
         "Format: Pāli = Russian, one per line. Builder: build_rails_G9_ru.py (importlib; importing writes nothing).",
         "Built on G2 (paṇṇatti / pavatti frames, partial / pair, headings), G45 (intro_ru, place answers, pjparse),",
         "G6 (unlabeled questions), G8 (moment phrases). New here: the class nouns, the Dhammayamaka moment subjects,",
         "multi-word paṇṇatti frames, the bhāvanā frame, plural pavatti verbs. No editorial notes in this yamaka.", "",
         "## Terms (termbase)", ""]
    for c in CLASSES:
        for k in (f"{c}ā dhammā", f"{c}ā", f"{c}aṃ", f"{c}aṃ dhammaṃ"):
            L.append(f"{k} = {T[k]['nom']} (gen. {T[k]['gen']}, ins. {T[k]['ins']})")
    L += ["dhammā / dhamme = явления (gen. явлений, ins. явлениями)",
          "X ca dhammā (ca inside the noun phrase) = read as «X dhammā ca»: «и возникают X явления, и …»",
          "uppajjanti / uppajjissanti / nirujjhanti / nirujjhissanti = возникают / возникнут / прекращаются / "
          "прекратятся (plural forms of G2's verbs; past возникали / прекращались)",
          "moments (G45.MOM_GEN): " + "; ".join(f"{k} = {v[0]}" for k, v in G45.MOM_GEN.items()
                                                 if "kusal" in k),
          "  (X-vippayutta-cittassa closes with a comma, as G45; «в момент возникновения / распада» + genitive)",
          "bhāveti = развивает (termbase «развивать»; pi-5 «путь развивается»); pajahati / nappajahati = устраняет / "
          "не устраняет (G45, pi-5)", "", "## Lines", ""]
    for p in NOTE_EXAMPLES:
        _LAST_Q["keys"] = None
        L.append(f"{p} = {translate_line(p)}")
    return "\n".join(L) + "\n"


def main():
    if len(sys.argv) > 2 and sys.argv[1] == "--probe":
        for ch in sys.argv[2:]:
            probe(ch)
        return
    for fn, lst in (("pi-1-russian-plain.md", PI1_STRINGS), ("pi-5-russian-plain.md", PI5_STRINGS)):
        txt = (S.RU / fn).read_text(encoding="utf-8")
        miss = [x for x in lst if x not in txt]
        assert not miss, f"{fn}: strings not found: {miss}"
    problems = []
    for ch in CHAPTERS:
        pt = (PALI / ch).read_text(encoding="utf-8")
        _LAST_Q["keys"] = None
        ru, pr = render(pt)
        problems += pr
        e, n = S.check_file(pt, ru)
        problems += [f"{ch}: {x}" for x in e]
        (OUT / ch).write_text(ru, encoding="utf-8", newline="\n")
        print(f"wrote {ch}: {n} segments")
    slips = list(SLIPS) + list(G2.SLIPS) + list(G45.SLIPS)
    (S.RAILS / "notes-rails-G9.md").write_text(notes_md(), encoding="utf-8", newline="\n")
    print("wrote notes-rails-G9.md")
    for sid, note in dict.fromkeys(slips):
        print("slip", sid, note)
    print("per-line problems:", len(problems))
    for p in problems:
        print("  ", p)
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
