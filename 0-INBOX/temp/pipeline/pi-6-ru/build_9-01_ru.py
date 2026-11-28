"""Russian plain zero-shot of pi-6 (Yamaka): chapter 9-01-dhammayamaka.md (Dhammayamaka: paṇṇattivāra and the
uppādavāra of the pavattivāra).

Families A and B come from build_2-01_ru (frames unchanged), pv_abbr() / extra_units() / PAVATTIVARO from
build_2-02_ru, the person / place shape from build_7-01_ru, the moments and persons of build_8_ru, and the mixed
person / moment intros (pv_intro, SC_UNITS, place_intro) of build_5-01_ru (+ the bhaṅgakkhaṇe units of
build_5-02_ru, for 9-02). None of those files is edited: the units added here are applied only inside units_9().
NEW here (listed in notes-9-01.md): the Dhamma members (kusalā / akusalā / abyākatā dhammā = pi-1 «благие /
неблагие / этически неопределённые явления»), the bare adjectives of the paṇṇattivāra, the moments
"kusalānaṃ uppādakkhaṇe" and "kusalavippayuttacittassa uppādakkhaṇe", two Suddhadhamma headings.

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_9-01_ru.py
Probe:  python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_9-01_ru.py --probe 9-02-dhammayamaka.md
Import: M = importlib.import_module("build_9-01_ru")   (importing never writes any file; only __main__ builds)

Exposed for 9-02 / 9-03
  Members     DH_MEMBERS, DH_PL, DH_X (bare kusalā), DH_X_SG (kusalaṃ), DH_K (kusalā dhammā), DHAMMA, DH_LEX,
              DH_PV_SUBJ, DH_GENDER, DH_CFG
  Paṇṇatti    pada_question(body, lex), pn_sentence(s, cfg), pn_line(text, cfg)
  Pavatti     pv_norm(text) (joins "kusalā dhammā" / "kusalā ca dhammā", plural verbs -> the 2-01 verb keys),
              UNITS_9, units_9() (context manager), pv_sentence(s, cfg), pv_answers(text, cfg), pv_line(text, cfg)
  Lines       heading(text), tr(text, cfg, mode), translate_text(src, cfg, mode="pn"|"pv"), HEADS, FIXED_9
  Checks      CROSSBOOK, check_against_finished(src, ru)
"""
import contextlib
import importlib
import pathlib
import re
import sys
import unicodedata

HERE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru")
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import build_sample_ru as B  # noqa: E402

A = importlib.import_module("build_2-01_ru")    # families A + B
E = importlib.import_module("build_2-02_ru")    # pv_abbr, extra_units, PAVATTIVARO
C = importlib.import_module("build_7-01_ru")    # person / place shape, answers
D = importlib.import_module("build_8_ru")       # moments, «у них»
S = importlib.import_module("build_5-01_ru")    # pv_intro, SC_UNITS, place_intro, notes
S2 = importlib.import_module("build_5-02_ru")   # bhaṅgakkhaṇe units (for 9-02)

CHAPTER = "9-01-dhammayamaka.md"
cap, lower1 = B.cap, C.lower1
SLIP_LOG = []

# =============================================================================================
# Members: pi-1 «благие / неблагие / этически неопределённые явления» (sample ADJ; asserted by the sample)
# =============================================================================================
DH_MEMBERS = ("kusala", "akusala", "abyākata")
DH_PL ={"kusala": "kusalā", "akusala": "akusalā", "abyākata": "abyākatā"}
DHAMMA_NOUN = ("явления", "явлениями", "явлений")            # dhammā (pi-1 dhamma = явление)


def _bare(x):
    """Bare 'kusalā' (pl., implied dhammā): «благие», instr. «благими»."""
    a = B.ADJ[x]
    return A.N(a["nom_pl"], a["instr_pl"], a["gen_pl"], "pl")


def _bare_sg(x):
    """Bare 'kusalaṃ' (sg. n.): «благое», «благим», gen. «благого» («Кроме благого», «не связанного с благим»)."""
    a = B.ADJ[x]
    return A.N(a["n_nom"], a["n_instr"], a["m_gen"], "n")


def _member(x):
    a = B.ADJ[x]
    return A.N(f"{a['nom_pl']} {DHAMMA_NOUN[0]}", f"{a['instr_pl']} {DHAMMA_NOUN[1]}",
               f"{a['gen_pl']} {DHAMMA_NOUN[2]}", "pl")


DH_X = {x: _bare(x) for x in DH_MEMBERS}
DH_X_SG = {x: _bare_sg(x) for x in DH_MEMBERS}
DH_K = {x: _member(x) for x in DH_MEMBERS}
DHAMMA = A.N(*DHAMMA_NOUN, "pl")
DH_LEX = {}
for _x, _p in DH_PL.items():
    DH_LEX[_p] = DH_X[_x]                       # kusalā
    DH_LEX[_x + "ṃ"] = DH_X_SG[_x]              # kusalaṃ
    DH_LEX[_p + " dhammā"] = DH_K[_x]           # kusalā dhammā (questions)
    DH_LEX[_p + "_dhammā"] = DH_K[_x]           # joined token (answers, pavattivāra)
DH_LEX.update({"dhammā": DHAMMA, "dhamme": DHAMMA})
DH_PV_SUBJ = {_p + "_dhammā": DH_K[_x] for _x, _p in DH_PL.items()}
DH_GENDER = "pl"                                 # bare verb answers: «Возникают.» / «Возникали.» / «Возникнут.»
assert DH_K["kusala"]["nom"] == "благие явления" and DH_K["abyākata"]["nom"] == "этически неопределённые явления"
assert ("1", f"(б) {cap(DH_K['akusala']['nom'])}.") in B.CROSSBOOK        # pi-1 «(б) Неблагие явления.»

# =============================================================================================
# Paṇṇattivāra (family A frames of 2-01)
# =============================================================================================
def _strip_ti(w, lex):
    if w in lex:
        return w
    if w.endswith("ti") and w[:-2] in lex:
        return w[:-2]
    raise KeyError(f"not in lexicon: {w!r}")


def pada_question(body, lex):
    """'kusalā kusalā dhammā(ti)' / 'dhammā kusalā' / 'na kusalā dhammā na kusalā(ti)' -> Russian question."""
    t = lower1(body).split()
    t[-1] = _strip_ti(t[-1], lex) if t[-1] not in lex else t[-1]
    if t[0] == "na":
        i = t.index("na", 1)
        a, b = lex[" ".join(t[1:i])], lex[" ".join(t[i + 1:])]
        return A.PADA_NEG.format(a_instr=a["instr"], b_instr=b["instr"])
    if len(t) == 2:
        a, b = t
    elif len(t) == 3 and t[2] == "dhammā":
        a, b = t[0], " ".join(t[1:])
    elif len(t) == 3 and t[1] == "dhammā":
        a, b = " ".join(t[:2]), t[2]
    else:
        raise ValueError(f"paṇṇatti question not parsed: {body!r}")
    a, b = lex[a], lex[b]
    return A.PADA_POS.format(a_nom=cap(a["nom"]), a_cop=a["cop"], b_instr=b["instr"])


JOIN_RE = re.compile(r"\b((?:[Kk]usal|[Aa]kusal|[Aa]byākat)ā) dhammā\b")
JOIN_CA_RE = re.compile(r"\b((?:[Kk]usal|[Aa]kusal|[Aa]byākat)ā) ca dhammā\b")


def pn_sentence(s, cfg):
    """One Pāli paṇṇatti answer sentence (no final '.') -> Russian with '.'."""
    if s + "." in C.SIMPLE_ANSWERS:
        return C.SIMPLE_ANSWERS[s + "."]
    return A.pannatti_sentence(JOIN_RE.sub(r"\1_dhammā", s), cfg["lex"], cfg["qual"])


def _sentences(text):
    out = []
    for s in re.split(r"(?<=\.) (?=\S)", text.strip()):
        assert s.endswith("."), s
        out.append(s[:-1])
    return out


def pn_line(text, cfg):
    """Paṇṇattivāra line (label removed): 'Q?' / 'Q? Āmantā.' / answer sentences."""
    if "?" in text:
        q, _, rest = text.partition("?")
        out = pada_question(q, cfg["lex"])
        rest = rest.strip()
        return out + (" " + " ".join(pn_sentence(s, cfg) for s in _sentences(rest)) if rest else "")
    return " ".join(pn_sentence(s, cfg) for s in _sentences(text))


# =============================================================================================
# Pavattivāra: intros (5-01 pv_intro + the Dhamma moments)
# =============================================================================================
# kusalānaṃ uppādakkhaṇe = «в момент возникновения благих явлений» (pi-2 «возникших благих явлений»);
# kusalavippayuttacittassa uppādakkhaṇe = «в момент возникновения ума, не связанного с благим» (5-01 taṇhāvippayutta
# frame «ума, не связанного с жаждой»; the bare compound member = 'what is wholesome', sg. n. «благое»);
# two members: «…, не связанного с благим и не связанного с неблагим» (5-01 two-member frame).
UNITS_9 = []
for _kh, _mo in (("uppādakkhaṇe", S.UPPADA), ("bhaṅgakkhaṇe", S.BHANGA)):
    for _x1 in DH_MEMBERS:
        for _x2 in DH_MEMBERS:
            if _x1 != _x2:
                UNITS_9.append((rf"{_x1}vippayutta{_x2}vippayuttacittassa {_kh}",
                                f"{_mo} {S.CITTA_G}, {S.VIPPAYUTTA} {DH_X_SG[_x1]['instr']} и {S.VIPPAYUTTA} "
                                f"{DH_X_SG[_x2]['instr']}", "advc", False))
    for _x in DH_MEMBERS:
        UNITS_9.append((rf"{_x}vippayuttacittassa {_kh}",
                        f"{_mo} {S.CITTA_G}, {S.VIPPAYUTTA} {DH_X_SG[_x]['instr']}", "advc", False))
        UNITS_9.append((rf"{_x[:-1]}ānaṃ {_kh}", f"{_mo} {DH_K[_x]['gen']}", "adv", False))


@contextlib.contextmanager
def units_9():
    """Prepend UNITS_9 (and 5-02's bhaṅgakkhaṇe units) to build_5-01_ru.ALL_UNITS for the block only."""
    old = list(S.ALL_UNITS)
    S.ALL_UNITS[:0] = [u for u in UNITS_9 + S2.UNITS_5_02 if u not in S.ALL_UNITS]
    try:
        with E.extra_units():
            yield
    finally:
        S.ALL_UNITS[:] = old


# =============================================================================================
# Pavattivāra: sentences, questions, lines
# =============================================================================================
VERB_PL_RE = re.compile(r"\b(n?)([Uu]ppajj|[Nn]irujjh)(issa|a)nt(i|īti)\b")


def pv_norm(text):
    """'kusalā ca dhammā' -> 'kusalā_dhammā ca'; 'kusalā dhammā' -> 'kusalā_dhammā'; uppajjanti -> uppajjati
    (number comes from the Russian subject, as in 2-01)."""
    text = JOIN_CA_RE.sub(r"\1_dhammā ca", text)
    text = JOIN_RE.sub(r"\1_dhammā", text)
    return VERB_PL_RE.sub(lambda m: m.group(1) + m.group(2) + m.group(3) + "t" + m.group(4), text)


_RX_CACHE = {}


def _rx(subj):
    key = tuple(sorted(subj))
    if key not in _RX_CACHE:
        names = "(?:" + "|".join(re.escape(k) for k in sorted(subj, key=len, reverse=True)) + ")"
        s1 = re.compile(r"(?P<intro>.+?) " + S._T.format(n="t1") + rf" (?P<x>{names}) (?P<n1>na |n)?(?P<v1>"
                        + A.V_RE + r"), no ca " + S._T.format(n="t2") + rf" (?P<y>{names}) (?P<n2>na |n)?(?P<v2>"
                        + A.V_RE + r")")
        s2 = re.compile(r"(?P<intro>.+?) " + S._T.format(n="t1") + rf" (?P<x>{names}) ca (?P<n1>na |n)?(?P<v1>"
                        + A.V_RE + rf") (?P<y>{names}) ca (?P<n2>na |n)?(?P<v2>" + A.V_RE + r")")
        single = re.compile(r"(?P<intro>.+?) (?P<t>tesaṃ tattha|tesaṃ|tattha) " + rf"(?P<x>{names}) (?P<n>na |n)?"
                            r"(?P<v>" + A.V_RE + r")")
        _RX_CACHE[key] = (s1, s2, single)
    return _RX_CACHE[key]


def _pred(v, x, neg):
    return A.PV_PRED.format(v=A.verb(v, x["g"], bool(neg)), x=x["nom"])


def _head(intro, t):
    if t.startswith("tesaṃ"):
        return S.pv_intro(intro, "tattha" in t)
    return S.place_intro(intro)


def pv_sentence(s, cfg):
    """One normalised Pāli pavatti answer sentence (no final '.') -> Russian with '.' (5-01 frames)."""
    if s + "." in C.SIMPLE_ANSWERS:
        return C.SIMPLE_ANSWERS[s + "."]
    lv = lower1(s)
    if lv in A.PV_VERBS:                                       # Uppajjanti. / Uppajjittha. …
        return cap(A.verb(lv, cfg.get("gender", DH_GENDER))) + "."
    pe = s.endswith("…pe…")
    core = s[: -len("…pe…")] if pe else s
    subj = cfg["pv_subj"]
    s1, s2, single = _rx(subj)
    ru = None
    m = s1.fullmatch(core)
    if m:
        x, y = subj[m.group("x")], subj[m.group("y")]
        p1 = _pred(m.group("v1"), x, m.group("n1"))
        v2 = A.verb(m.group("v2"), y["g"], not m.group("n2"))   # "no ca": the predicate is denied for Y
        tail = (A.PV_NO_CA_POS_FRAME if m.group("n2") else C.NO_CA_FRAME).format(
            res=C.RES[m.group("t2")], **{("pred" if m.group("n2") else "neg_pred"): A.PV_PRED.format(v=v2, x=y["nom"])})
        ru = _head(m.group("intro"), m.group("t1")) + p1 + tail + "."
    if ru is None:
        m = s2.fullmatch(core)
        if m:
            x, y = subj[m.group("x")], subj[m.group("y")]
            head = _head(m.group("intro"), m.group("t1"))
            if m.group("n1") and m.group("n2"):
                f1, f2 = A.verb(m.group("v1"), x["g"]), A.verb(m.group("v2"), y["g"])
                both = (A.PV_NEITHER_FRAME.format(v=f1, x=x["nom"], y=y["nom"]) if f1 == f2
                        else A.PV_NEG_MIXED_FRAME.format(v1=f1, x=x["nom"], v2=f2, y=y["nom"]))
            else:
                both = C.BOTH_FRAME.format(p1=_pred(m.group("v1"), x, m.group("n1")),
                                           p2=_pred(m.group("v2"), y, m.group("n2")))
            ru = head + both + "."
    if ru is None:
        m = single.fullmatch(core)
        if m and ", no ca " not in core:
            ru = _head(m.group("intro"), m.group("t")) + _pred(m.group("v"), subj[m.group("x")], m.group("n")) + "."
    if ru is None:
        raise ValueError(f"pavatti answer not parsed: {s!r}")
    return ru[:-1] + "…" if pe else ru


def pv_answers(text, cfg):
    return " ".join(pv_sentence(s, cfg) for s in _sentences(text))


def pv_line(text, cfg):
    """Normalised pavattivāra line (label removed)."""
    r = E.pv_abbr(text, cfg["pv_subj"])
    if r is not None:
        return r
    if "?" in text:
        q, _, rest = text.partition("?")
        out = S.pv_question_any(q, cfg)
        rest = rest.strip()
        if rest in ("…Pe….", "…pe…."):
            return out + "…"
        return out + (" " + pv_answers(rest, cfg) if rest else "")
    return pv_answers(text, cfg)


# =============================================================================================
# Headings, fixed lines, line driver
# =============================================================================================
_SK, _SKM = B.SECTION_HEADINGS["Suddhakhandhavāro"], B.SECTION_HEADINGS["Suddhakhandhamūlacakkavāro"]
assert "о совокупностях" in _SK and "совокупностей" in _SKM
SECTION_EXTRA_9 = {
    "Suddhadhammavāro": _SK.replace("о совокупностях", "о явлениях"),          # Раздел о явлениях как таковых
    "Suddhadhammamūlacakkavāro": _SKM.replace("совокупностей", "явлений"),     # Круговой раздел на основе явлений …
    "Pavattivāro": E.PAVATTIVARO,                                               # Раздел о протекании (2-02)
}
HEADS = dict(B.SECTION_HEADINGS, **S.SECTION_EXTRA, **SECTION_EXTRA_9)
HEAD_RE = re.compile(r"(#+) (?:\((\w+)\) |(\d+) )?(.+)")
LABEL_RE = re.compile(r"\((Ka|Kha)\) (.*)")


def heading(text):
    hashes, lab, num, body = HEAD_RE.fullmatch(text).groups()
    if body in B.YAMAKA_TITLES:
        ru = B.YAMAKA_TITLES[body]
    else:
        ru = C.heading_case(HEADS[body])
    pre = f"({lab if lab.isdigit() else B.LETTERS[lab]}) " if lab else (f"{num} " if num else "")
    return f"{hashes} {pre}{ru}"


FIXED_9 = {
    "(Kha) niddeso": f"({B.LETTERS['Kha']}) {B.NIDDESO}",       # plain line in the source (^6-9-16)
    "Paṇṇattiuddesavāro.": A.PANNATTI_UDDESAVARO,
    "Paṇṇattiniddesavāro.": A.PANNATTI_NIDDESAVARO,
    "Uppādavāro.": C.VARO_CLOSING.format(heading=B.SECTION_HEADINGS["Uppādavāro"]),
    "Nirodhavāro.": C.VARO_CLOSING.format(heading=B.SECTION_HEADINGS["Nirodhavāro"]),
    "Uppādanirodhavāro.": C.VARO_CLOSING.format(heading=B.SECTION_HEADINGS["Uppādanirodhavāro"]),
    "Pariññāvāro.": C.VARO_CLOSING.format(heading=B.SECTION_HEADINGS["Pariññāvāro"]),
    "Pavattivāro niṭṭhito.": f"{E.PAVATTIVARO} {B.NITTHITO}.",
    "Dhammayamakaṃ niṭṭhitaṃ.": B.YAMAKA_CLOSING_FRAME.format(title=B.YAMAKA_TITLES["Dhammayamakaṃ"]),
}

DH_CFG = {
    "lex": DH_LEX,
    "qual": {},
    "pv_subj": DH_PV_SUBJ,
    "gender": DH_GENDER,
    "slips": [],
    "fixed": FIXED_9,
    "variant_anchors": {},
}


def tr(text, cfg, mode):
    """Translate one Pāli line (block ID removed). mode: "pn" (paṇṇattivāra) or "pv" (pavattivāra)."""
    if not text.strip():
        return ""
    if text in cfg["fixed"]:
        return cfg["fixed"][text]
    if text in B.FIXED:
        return B.FIXED[text]
    if text.startswith("#"):
        return heading(text)
    variants, text = S._variants(text, cfg)
    for old, new, note in cfg.get("slips", []):
        if old in text:
            text = text.replace(old, new)
            SLIP_LOG.append(note)
    label = ""
    m = LABEL_RE.fullmatch(text)
    if m:
        label, text = f"({B.LETTERS[m.group(1)]}) ", m.group(2)
    ru = pn_line(text, cfg) if mode == "pn" else pv_line(pv_norm(text), cfg)
    return S._insert_variants(label + ru, variants, cfg)


def translate_text(src, cfg=None, mode="pn"):
    cfg = cfg or DH_CFG
    out = []
    with units_9():
        for line in src.split("\n"):
            body, bid = B.ID_RE.match(line).groups()
            if body.startswith("#") and "Pavatti" in body:
                mode = "pv"
            out.append(tr(body, cfg, mode) + (bid or ""))
    return unicodedata.normalize("NFC", "\n".join(out))


# =============================================================================================
# Checks
# =============================================================================================
CROSSBOOK = [   # strings taken from the approved pi-1 … pi-5 Russian rails (book, exact substring)
    ("1", "Благие явления"), ("1", "Неблагие явления"), ("1", "Этически неопределённые явления"),
    ("2", "благих явлений"), ("1", "не связанный с"), ("5", "момент возникновения"), ("5", "момент распада"),
    ("5", "медитативное достижение прекращения"), ("2", "Существа без восприятия"), ("5", "архат"),
]


def check_against_finished(src, ru):
    """Identical Pāli line = identical Russian line, against every finished pi-6 chapter (others are not
    re-checked among themselves)."""
    seen = {}
    names = [p.name for p in sorted(B.OUT_DIR.glob("*.md")) if p.name != CHAPTER and (B.PALI_DIR / p.name).exists()]
    for n in names:
        p = (B.PALI_DIR / n).read_text(encoding="utf-8").split("\n")
        r = (B.OUT_DIR / n).read_text(encoding="utf-8").split("\n")
        if len(p) != len(r):
            continue
        for a, b in zip(p, r):
            pb, rb = B.ID_ANY.sub("", a).strip(), B.ID_ANY.sub("", b).strip()
            seen.setdefault(pb, {}).setdefault(rb, n)
    bad, shared = [], 0
    mine = {}
    for a, b in zip(src.split("\n"), ru.split("\n")):
        pb, rb = B.ID_ANY.sub("", a).strip(), B.ID_ANY.sub("", b).strip()
        if pb in mine:
            assert mine[pb] == rb, f"inconsistent inside the chapter: {pb!r}"
        mine[pb] = rb
        if pb.strip() and pb in seen:
            shared += 1
            if rb not in seen[pb]:
                bad.append((pb, rb, seen[pb]))
    if bad:
        raise AssertionError("differs from finished chapters: " + repr(bad[:5]))
    return shared, names


def probe(name):
    src = (B.PALI_DIR / name).read_text(encoding="utf-8")
    ok = bad = 0
    mode = "pn" if name == CHAPTER else "pv"     # 9-02 / 9-03 continue the pavattivāra
    with units_9():
        for line in src.split("\n"):
            body, _ = B.ID_RE.match(line).groups()
            if body.startswith("#") and "Pavatti" in body:
                mode = "pv"
            try:
                tr(body, DH_CFG, mode)
                ok += 1
            except Exception as e:   # noqa: BLE001
                bad += 1
                print("-- ", type(e).__name__, str(e)[:200])
    print(f"{name}: {ok} lines translated, {bad} not covered")


def main():
    B.check_crossbook()
    A.check_crossbook()
    A.check_crossbook(S.CROSSBOOK)
    A.check_crossbook(CROSSBOOK)
    C.check_crossbook_c()
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    ru = translate_text(src)
    B.check_pair(src, ru, CHAPTER)
    shared, names = check_against_finished(src, ru)
    with open(B.OUT_DIR / CHAPTER, "w", encoding="utf-8", newline="\n") as f:
        f.write(ru)
    print("written", B.OUT_DIR / CHAPTER, "lines", len(ru.split("\n")))
    for s in SLIP_LOG + S.SLIP_LOG + A.SLIP_LOG:
        print("slip:", s)
    print(f"cross-book asserts OK; per-line checks OK; {shared} lines shared with {len(names)} finished chapters agree")


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "--probe":
        probe(sys.argv[2])
    else:
        main()
