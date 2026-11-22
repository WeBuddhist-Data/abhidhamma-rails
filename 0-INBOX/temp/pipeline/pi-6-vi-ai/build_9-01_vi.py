# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 9-01-dhammayamaka.md (Dhammayamaka part 1: paṇṇattivāra and the
uppādavāra of the pavattivāra), and FRAME-SETTER of the Dhammayamaka members and answer heads for 9-02 / 9-03.

Families A / B come VERBATIM from build_2-01_vi (question and answer frames, verbs, beings, planes); the person /
place shape there is the 7-01 one. The moment / person vocabulary of the answers (khoảnh khắc sinh khởi / tan rã,
nirodhasamāpanna, samaṅgī, itaresaṃ) comes from build_8_vi. Set here: the three members as subjects / predicates
of the naming questions, the Dhammayamaka answer heads (who9) and the Pāli plural verb forms.

9-02 / 9-03 use:

    import sys, importlib; sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai")
    D = importlib.import_module("build_9-01_vi")
    D.translate_sentence(s)       the whole sentence parser of this chapter (A naming questions / answers, B questions,
                                  B answers with who9 heads, short answers, «?…Pe….»)
    D.member(w) / D.a_subject(t) / D.a_pred(t)      kusalā dhammā = các hiện tượng thiện …
    D.vparse9("na nirujjhissanti")                  -> (base, tense, neg) (singular and plural Pāli forms)
    D.who9("Sabbesaṃ cittassa bhaṅgakkhaṇe …")      -> answer head (lowercase start)
    D.heading(t)                                    headings incl. Suddhadhammavāro …
    D.bh_q(...) / D.BH_VERB                         PROPOSED bhāvanāvāra frames (9-03)

Importing writes nothing; run  python -I -X utf8 -B build_9-01_vi.py  to rebuild the chapter.
"""
import importlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as S  # noqa: E402

F = importlib.import_module("build_2-01_vi")     # families A / B (frame-setter)
E = importlib.import_module("build_2-02_vi")     # PE handling conventions, family E
C8 = importlib.import_module("build_8_vi")       # moments, nirodhasamāpanna, samaṅgī, itaresaṃ (family D)
A7 = importlib.import_module("build_7-01_vi")    # yo / so frame, YO_VERB (pajahati)

NAME = "9-01-dhammayamaka.md"
cap, low = S.cap, S.low
LABEL_VI = S.LABEL
SLIPS = []

# ================================================================ members
# kusalā / akusalā / abyākatā dhammā = các hiện tượng thiện / bất thiện / không xác định về mặt đạo đức (sample CAT,
# pi-1 matrix); dhammā = các hiện tượng (2-01 rule: the Pāli number is kept, khandhā = các khối).
CATS = {"kusalā": "kusala", "akusalā": "akusala", "abyākatā": "abyākata"}
K_RE = "akusalā|kusalā|abyākatā"
DHAMMA_PL = "các hiện tượng"                     # dhammā / dhamme
WHAT_IS = "những gì {p}"                         # bare kusalā as subject: «những gì là thiện» (sample pred)


def member(w):
    """kusalā (dhammā) in the pavattivāra -> «các hiện tượng thiện» (sample CAT head, lowercase)."""
    return low(S.CAT[CATS[low(w)]]["head"])


def a_subject(t):
    """Naming-question subject: kusalā = những gì là thiện; kusalā dhammā = các hiện tượng thiện; dhammā = các hiện tượng."""
    t = low(t)
    if t in ("dhammā", "dhamme"):
        return DHAMMA_PL
    if t.endswith(" dhammā"):
        return member(t.split()[0])
    return WHAT_IS.format(p=S.CAT[CATS[t]]["pred"])


def a_pred(t):
    """Predicate after «là» / «không phải là»: kusalā = thiện; kusalā dhammā = các hiện tượng thiện; dhammā = các hiện tượng."""
    t = low(t)
    if t in ("dhammā", "dhamme"):
        return DHAMMA_PL
    if t.endswith(" dhammā"):
        return member(t.split()[0])
    return S.CAT[CATS[t]]["adj"]


def a_noun(stem):
    """Kusalaṃ / kusalañca (neuter collective) = hiện tượng thiện (sample CAT noun)."""
    return S.CAT[low(stem)]["noun"]


# ================================================================ headings
HEAD9 = {
    "Suddhadhammavāro": S.VARO.format(x=f"{DHAMMA_PL} thuần túy"),                       # = 3-01 Suddhāyatanavāro pattern
    "Suddhadhammamūlacakkavāro": S.VARO.format(x=f"vòng luân chuyển dựa trên {DHAMMA_PL} thuần túy"),
    "Uppādavāro": cap(S.SECTION["uppādavāro"]),                                         # Mục về sự sinh khởi
    "Nirodhavāro": cap(S.SECTION["nirodhavāro"]),                                       # Mục về sự chấm dứt
}


def heading(t):
    m = re.fullmatch(r"(?P<n>\d+) (?P<w>\S+)", t)          # «3 Suddhadhammavāro»: the digit stays
    if m and m["w"] in HEAD9:
        return f"{m['n']} {HEAD9[m['w']]}"
    return HEAD9.get(t) or F.heading(t)


EXACT = {
    "(Kha) niddeso": f"{S.LABEL['Kha']} {S.NIDDESO}",                  # plain line inside ^6-9-16
    "Paṇṇattiniddesavāro.": F.PANNATTI_NIDDESAVARO,                    # 2-01
    "Uppādavāro.": cap(S.SECTION["uppādavāro"]) + ".",                 # = 2-02 «Nirodhavāro.» pattern
    "Nirodhavāro.": E.EXACT["Nirodhavāro."],
    "Uppādanirodhavāro.": E.EXACT["Uppādanirodhavāro."],
    "Pavattivāro niṭṭhito.": E.EXACT["Pavattivāro niṭṭhito."],
    "Āmantā.": S.AMANTA,
    "Natthi.": F.NATTHI,
    "No.": A7.NO,
}

# ================================================================ family A: naming questions and answers
A_WORDS = {"kusalā", "akusalā", "abyākatā", "dhammā"}


def _unti(w):
    return w[:-2] if w.endswith("āti") else w


def a_question(s):
    """(Ka) kusalā kusalā dhammā? / (Kha) na dhammā na akusalā dhammāti? … -> Vietnamese, or None."""
    m = re.fullmatch(r"\((?P<l>Ka|Kha)\) (?P<b>[^?]+)\?", s)
    if not m:
        return None
    words = m["b"].split()
    words[-1] = _unti(words[-1])
    if not set(words) <= A_WORDS | {"na"}:
        return None
    body = " ".join(words)
    if body.startswith("na "):
        parts = body[3:].split(" na ")
        assert len(parts) == 2, s
        return F.a_q(a_pred(parts[0]), a_pred(parts[1]), neg=True, label=m["l"])
    assert "na" not in words, s
    if len(words) == 2:
        x, y = words
    else:
        assert len(words) == 3, s
        x, y = (words[0], " ".join(words[1:])) if words[2] == "dhammā" else (" ".join(words[:2]), words[2])
    return F.a_q(a_subject(x), a_pred(y), label=m["l"])


A_SENT = [
    # Akusalā dhammā dhammā ceva akusalā dhammā ca.
    (rf"(?P<s>\S+ dhammā) (?P<a>dhammā) ceva (?P<b>(?:{K_RE}) dhammā) ca\.",
     lambda g: F.a_both(a_subject(g["s"]), F.a_is(a_pred(g["a"])), F.a_is(a_pred(g["b"])))),
    # Avasesā dhammā na akusalā dhammā.
    (rf"Avasesā (?P<n>dhammā) na (?P<b>(?:{K_RE}) dhammā)\.",
     lambda g: F.a_rest(a_subject(g["n"]), F.a_not(a_pred(g["b"])))),
    # Kusalaṃ ṭhapetvā avasesā dhammā na kusalā, dhammā.
    (rf"(?P<e>Akusala|Kusala|Abyākata)ṃ ṭhapetvā avasesā (?P<n>dhammā) na (?P<b>{K_RE}), (?P<a>dhammā)\.",
     lambda g: F.a_but_not(F.a_except_n(a_noun(g["e"]), a_subject(g["n"])), F.a_not(a_pred(g["b"])),
                           F.a_is(a_pred(g["a"])))),
    # Kusalañca dhamme ca ṭhapetvā avasesā na ceva kusalā na ca dhammā.
    (rf"(?P<e>Akusala|Kusala|Abyākata)ñca (?P<d>dhamme) ca ṭhapetvā avasesā na ceva (?P<c>{K_RE}) na ca "
     rf"(?P<f>dhammā)\.",
     lambda g: F.a_neither(F.a_except(F.a_and(a_noun(g["e"]), a_subject(g["d"]))), a_pred(g["c"]), a_pred(g["f"]))),
]
A_SENT = [(re.compile(p), f) for p, f in A_SENT]

# ================================================================ family B: verbs (singular and plural Pāli forms)
VF = (r"(?:na |n)?(?:uppajj|nirujjh)(?:antīti|anti|atīti|ati|itthāti|ittha|issantīti|issanti|issatīti|issati)")
VFORM9 = re.compile(r"(?P<neg>na |n)?(?P<b>uppajj|nirujjh)(?P<t>antīti|anti|atīti|ati|itthāti|ittha|issantīti|"
                    r"issanti|issatīti|issati)")
TENSE9 = {"anti": "pres", "antīti": "pres", "ati": "pres", "atīti": "pres", "ittha": "past", "itthāti": "past",
          "issanti": "fut", "issantīti": "fut", "issati": "fut", "issatīti": "fut"}   # plural = singular


def vparse9(s):
    m = VFORM9.fullmatch(s)
    if not m:
        raise ValueError(f"unparsed verb {s!r}")
    return (F.VERB_BASE[m["b"]], TENSE9[m["t"]], bool(m["neg"]))


SHORT9 = re.compile(r"(?P<b>Uppajj|Nirujjh)(?P<t>anti|ati|ittha|issanti|issati)\.")   # Uppajjanti. / Uppajjittha. …

# ================================================================ family B: answer heads (who9)
# Each Pāli element of a head becomes one Vietnamese element; elements are joined with ", " (2-01 LIST_SEP).
# P = persons (genitive): consecutive persons share one «ở» (2-01 WHO_HEAD / 8 NIRODHA_ASANNA); T = time or place.
AGGAMAGGA = "con đường tối thượng"               # aggamagga (coordinator: Aggamaggasamaṅgī = Người có được con đường tối thượng)
ARAHANTA_PL = "các bậc A-la-hán"                 # arahantānaṃ (pi-5 «các bậc A-la-hán»; 7-04 Arahā = Bậc A-la-hán)
SABBE = "tất cả chúng sinh"                      # bare sabbesaṃ (before cittassa …; pi-2, 6-01, coordinator); with a participle 2-01 «tất cả những người …»
ANANTARA = f"những người sẽ đạt được {AGGAMAGGA} ngay sau tâm nào đó"
# yassa cittassa anantarā aggamaggaṃ paṭilabhissanti (aṭṭhakathā ^6-176: the gotrabhū citta); paṭilabhati «đạt được» (2-02)
THAT_CITTA = "tâm ấy"                            # tassa cittassa (… uppādakkhaṇe) = của tâm ấy
PAVATTE = "trong đời sống"                       # pavatte (as against the moments of rebirth and death; pi-5 «đời sống»)
VIPPAYUTTA = "tâm không gắn liền với {a}"        # Xvippayuttacitta (pi-1 «không gắn liền với»)
VIPPAYUTTA2 = "tâm vừa không gắn liền với {a} vừa không gắn liền với {b}"   # Xvippayutta-Yvippayuttacitta («vừa … vừa» pi-1)
DUTIYA = "khi tâm{k} thứ hai đang diễn ra"       # dutiye [akusale] citte vattamāne (pi-5 «khi tâm … đang diễn ra»)
CAT_STEM = {"kusal": "kusalā", "akusal": "akusalā", "abyākat": "abyākatā"}
CAT_LOC = {"kusale": "kusala", "akusale": "akusala", "abyākate": "abyākata"}


def _strip_o(s):
    assert s.startswith("ở "), s
    return s[2:]


def _at(moment, c):
    return C8.AT.format(x=C8.OF.format(x=C8.MOMENT[moment], c=c))      # vào khoảnh khắc sinh khởi của …


ELEMENTS = [
    (r"sabbesaṃ (?:upapajjantānaṃ|cavantānaṃ)", "P", lambda m: _strip_o(F.who(m[0]))),
    (r"suddhāvāsaṃ upapajjantānaṃ", "P", lambda m: _strip_o(F.who(m[0]))),
    (r"itaresaṃ catuvokārānaṃ pañcavokārānaṃ", "P", lambda m: _strip_o(F.who(m[0]))),
    (r"suddhāvāsānaṃ|asaññasattānaṃ", "P", lambda m: _strip_o(F.who(m[0]))),
    (r"nirodhasamāpannānaṃ", "P", lambda m: C8.NIRODHA_PERSONS),
    (r"aggamaggasamaṅgīnaṃ", "P", lambda m: C8.SAMANGI.format(c=AGGAMAGGA)),
    (r"arahantānaṃ", "P", lambda m: ARAHANTA_PL),
    (r"pacchimacittasamaṅgīnaṃ", "P", lambda m: _strip_o(C8.P_SUBJ["Pacchimacittasamaṅgīnaṃ"])),
    (r"yassa cittassa anantarā aggamaggaṃ paṭilabhissanti", "P", lambda m: ANANTARA),
    (r"itaresaṃ", "P", lambda m: C8.OTHERS),
    (r"sabbesaṃ", "P", lambda m: SABBE),
    (r"pavatte", "T", lambda m: PAVATTE),
    (r"arūpe|pañcavokāre|catuvokāre|asaññasatte", "T", lambda m: F.where(m[0])),
    (r"tassa cittassa (?P<m>uppāda|bhaṅga)kkhaṇe", "T", lambda m: _at(m["m"], THAT_CITTA)),
    (r"cittassa (?P<m>uppāda|bhaṅga)kkhaṇe", "T", lambda m: C8.when(m["m"])),
    (r"aggamaggassa (?P<m>uppāda|bhaṅga)kkhaṇe", "T", lambda m: _at(m["m"], AGGAMAGGA)),
    (r"(?P<c>akusal|kusal|abyākat)ānaṃ (?P<m>uppāda|bhaṅga)kkhaṇe", "T",
     lambda m: _at(m["m"], member(CAT_STEM[m["c"]]))),
    (r"(?P<c1>akusal|kusal|abyākat)avippayutta(?:(?P<c2>akusal|kusal|abyākat)avippayutta)?cittassa "
     r"(?P<m>uppāda|bhaṅga)kkhaṇe", "T",
     lambda m: _at(m["m"], VIPPAYUTTA2.format(a=member(CAT_STEM[m["c1"]]), b=member(CAT_STEM[m["c2"]]))
                   if m["c2"] else VIPPAYUTTA.format(a=member(CAT_STEM[m["c1"]])))),
    (r"dutiye (?:(?P<k>akusale|kusale|abyākate) )?citte vattamāne", "T",
     lambda m: DUTIYA.format(k=" " + S.CAT[CAT_LOC[m["k"]]]["adj"] if m["k"] else "")),
]
ELEMENTS = [(re.compile(p + r"(?= |$)"), k, f) for p, k, f in ELEMENTS]
OI = "ở "


def who9(phrase):
    """Pāli answer head (before tesaṃ / tesaṃ tattha) -> Vietnamese head, lowercase start."""
    p, i, out, prev_p = low(phrase), 0, [], False
    while i < len(p):
        for rx, kind, fn in ELEMENTS:
            m = rx.match(p, i)
            if m:
                vi = fn(m)
                if kind == "P" and not prev_p:
                    vi = OI + vi
                out.append(vi)
                prev_p = kind == "P"
                i = m.end() + 1
                break
        else:
            raise ValueError(f"unparsed head {phrase!r} at {p[i:]!r}")
    return F.LIST_SEP.join(out)


def where9(phrase):
    """Place head of a yattha answer: Asaññasatte / Catuvokāre pañcavokāre -> «trong cõi …, cõi …»."""
    ws = phrase.split()
    return F.LIST_SEP.join([F.where(ws[0])] + [F.where(w)[len("trong "):] for w in ws[1:]])


# ================================================================ family B: questions and answers
B_Q9 = re.compile(rf"(?:\((?P<l>Ka|Kha)\) )?(?P<w1>[Yy]assa vā pana yattha|[Yy]assa yattha|[Yy]assa vā pana|"
                  rf"[Yy]attha vā pana|[Yy]assa|[Yy]attha) (?P<x>{K_RE}) dhammā (?P<v1>{VF}) "
                  rf"(?P<w2>tassa tattha|tassa|tattha) (?P<y>{K_RE}) dhammā (?P<v2>{VF})\?")
RES = r"tesaṃ tattha|tesaṃ|tattha"
B_NOT9 = re.compile(rf"(?P<g>.+?) (?P<r>{RES}) (?P<x>{K_RE}) dhammā (?P<v1>{VF}), no ca (?P<r2>{RES}) "
                    rf"(?P<y>{K_RE}) dhammā (?P<v2>{VF})\.")
B_BOTH9 = re.compile(rf"(?P<g>.+?) (?P<r>{RES}) (?P<x>{K_RE}) ca dhammā (?P<v1>{VF}) (?P<y>{K_RE}) ca dhammā "
                     rf"(?P<v2>{VF})\.")
PE_Q = "?…Pe…."                                  # question + …pe…. : «? …» (3-01 rule; «….» is never written)


def b_question(s):
    m = B_Q9.fullmatch(s)
    if not m:
        return None
    kind = low(m["w1"]).replace(" vā pana", "")
    assert kind == {"tassa": "yassa", "tattha": "yattha", "tassa tattha": "yassa yattha"}[m["w2"]], s
    kha = "vā pana" in m["w1"]
    if m["l"] and kha != (m["l"] == "Kha"):
        SLIPS.append(f"label ({m['l']}) on a {'vā pana' if kha else 'non-vā pana'} question: {s[:60]}")
    return F.b_q(kind, member(m["x"]), vparse9(m["v1"]), member(m["y"]), vparse9(m["v2"]), kha=kha,
                 label=m["l"])


def b_answer(s):
    for rx, both in ((B_NOT9, False), (B_BOTH9, True)):
        m = rx.fullmatch(s)
        if not m:
            continue
        if not both:
            assert m["r"] == m["r2"], s
        res = m["r"]
        head = where9(m["g"]) if res == "tattha" else who9(m["g"])
        f = F.b_both if both else F.b_not
        return f(res, head, member(m["x"]), vparse9(m["v1"]), member(m["y"]), vparse9(m["v2"]))
    return None


def translate_sentence(s, ctx=""):
    if s in EXACT:
        return EXACT[s]
    if s.endswith(PE_Q):
        return translate_sentence(s[:-len(PE_Q) + 1], ctx) + " " + A7.PE
    for fn in (a_question, b_question, b_answer):
        r = fn(s)
        if r:
            return r
    m = SHORT9.fullmatch(s)
    if m:
        return F.b_short(F.VERB_BASE[low(m["b"])], TENSE9[m["t"]])
    for rx, f in A_SENT:
        m = rx.fullmatch(s)
        if m:
            return f(m)
    raise ValueError(f"unmatched sentence ({ctx}): {s!r}")


def translate_line(line, ctx=""):
    m = re.match(r"^(?P<h>#+ )?(?P<t>.*?)(?P<id> \^[0-9A-Za-z-]+)?$", line)
    h, t, sid = m["h"] or "", m["t"], m["id"] or ""
    if h:
        return h + heading(t) + sid
    if t in EXACT:
        return EXACT[t] + sid
    return " ".join(translate_sentence(x, ctx) for x in F.split_sentences(t)) + sid


def translate_file(name=NAME):
    src = (S.PALI_DIR / name).read_text(encoding="utf-8")
    out, seg = [], "start"
    for ln in src.splitlines():
        out.append(translate_line(ln, f"segment after ^{seg}") if ln.strip() else "")
        mid = re.search(r"\^([0-9A-Za-z-]+)\s*$", ln)
        if mid:
            seg = mid.group(1)
    text = "\n".join(out).rstrip("\n") + "\n"
    return re.sub(r"\n{3,}", "\n\n", text)


# ================================================================ PROPOSED for 9-03 (bhāvanāvāra; not used in 9-01)
# (Ka) yo kusalaṃ dhammaṃ bhāveti so akusalaṃ dhammaṃ pajahatīti?
#   = (a) Người nào tu tập hiện tượng thiện, thì có phải người ấy dứt bỏ hiện tượng bất thiện không?
# 7-01 YO_Q_FRAME / YO_REL_VI / YO_DEM_VI / VA_PANA; pajahati from 7-01 YO_VERB; bhāveti «tu tập» (pi-1 maggaṃ bhāveti);
# kusalaṃ dhammaṃ (singular) = hiện tượng thiện (sample CAT noun).
BH_VERB = {
    "bhāveti": dict(p="tu tập {t}", no="không tu tập {t}"),
    "na bhāveti": dict(p="không tu tập {t}", no="vẫn tu tập {t}"),
    "pajahati": A7.YO_VERB["pajahati"],
    "nappajahati": A7.YO_VERB["nappajahati"],
}
BHAVANAVARO = S.VARO.format(x="sự tu tập")       # Bhāvanāvāro (pi-1 bhāvanā «sự tu tập»)


def bh_q(x, v1, y, v2, label="Ka", vapana=False):
    """x, y: Pāli stems (kusala …); v1, v2: keys of BH_VERB (with the -ti stripped)."""
    s = A7.YO_Q_FRAME.format(rel=A7.YO_REL_VI["yo"], pa=BH_VERB[v1]["p"].format(t=S.CAT[x]["noun"]),
                             dem=A7.YO_DEM_VI["so"], pb=BH_VERB[v2]["p"].format(t=S.CAT[y]["noun"]))
    if vapana:
        s = A7.VA_PANA + low(s)
    return f"{LABEL_VI[label]} {cap(s)}" if label else cap(s)


# ================================================================ checks
CROSS_BOOK = [
    ("không gắn liền với", 1), ("khoảnh khắc sinh khởi", 5), ("khoảnh khắc tan rã", 5), ("đang diễn ra", 5),
    ("khi tâm thiện hoặc không xác định về mặt đạo đức đang diễn ra", 5), ("các bậc A-la-hán", 5),
    ("đời sống", 5), ("thành tựu thiền chấm dứt", 5), ("con đường", 4), ("tối thượng", 2), ("đạt được", 2),
    ("thuần túy", 5), ("tu tập", 1), ("sự tu tập", 1), ("dứt bỏ", 1), ("thứ hai", 1), ("ngay sau", 5),
    ("Các hiện tượng thiện", 1), ("không xác định về mặt đạo đức", 1), ("vừa", 1), ("nào đó", 2), ("tất cả chúng sinh", 2),
]


def check_cross_book():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in S.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts (9-01): {len(CROSS_BOOK)} strings found in pi-1..5 rails")


def _sentences(text):
    for p in text.splitlines():
        if not p.strip() or p.startswith("#"):
            continue
        p = re.sub(r"\s*\^[\w-]+$", "", p)
        if p in EXACT:
            yield p
            continue
        yield from F.split_sentences(p)


def check_repeats(pali):
    """Identical Pāli sentence -> identical Vietnamese within 9-01, and against 2-01 / 2-02 / 8 where shared."""
    seen, bad = {}, 0
    for s in _sentences(pali):
        t = translate_sentence(s)
        if seen.setdefault(s, t) != t:
            bad += 1
    shared = 0
    for mod in (F, E):
        other = (S.PALI_DIR / mod.NAME).read_text(encoding="utf-8")
        for s in set(_sentences(other)) & set(seen):
            shared += 1
            if mod.translate_sentence(s, "") != seen[s]:
                print(f"DIFFERS FROM {mod.NAME}:", s)
                bad += 1
    print(f"repeat check: {len(seen)} distinct sentences, {shared} shared with 2-01 / 2-02")
    return bad


def check_frames():
    """Spot checks that the imported frames are used byte for byte."""
    assert F.b_q("yassa", "x", ("sinh khởi", "pres", False), "y", ("sinh khởi", "pres", False)) == \
        "(a) Ở người nào mà x sinh khởi, thì ở người ấy có phải y sinh khởi không?"
    assert who9("Cittassa bhaṅgakkhaṇe nirodhasamāpannānaṃ asaññasattānaṃ") == \
        low(C8.P_SUBJ["Cittassa bhaṅgakkhaṇe nirodhasamāpannānaṃ asaññasattānaṃ"])
    assert who9("Itaresaṃ") == low(C8.P_SUBJ["Itaresaṃ"])
    assert who9("Pacchimacittasamaṅgīnaṃ") == low(C8.P_SUBJ["Pacchimacittasamaṅgīnaṃ"])
    assert who9("Itaresaṃ catuvokārānaṃ pañcavokārānaṃ") == F.who("Itaresaṃ catuvokārānaṃ pañcavokārānaṃ")
    assert who9("Sabbesaṃ upapajjantānaṃ") == F.who("Sabbesaṃ upapajjantānaṃ")
    assert member("kusalā") == "các hiện tượng thiện"
    assert bh_q("kusala", "bhāveti", "akusala", "pajahati") == \
        "(a) Người nào tu tập hiện tượng thiện, thì có phải người ấy dứt bỏ hiện tượng bất thiện không?"


def main():
    S.check_cross_book()
    F.check_cross_book()
    check_cross_book()
    check_frames()
    SLIPS.clear()
    text = unicodedata.normalize("NFC", translate_file())
    pali = (S.PALI_DIR / NAME).read_text(encoding="utf-8")
    probs = S.check_lines(pali, text, NAME)
    for bad in ("….", ".…", "?…", ",…", "  ", "là là", "—", ":-", "  "):
        assert bad not in text, bad
    assert check_repeats(pali) == 0, "identical Pāli rendered differently"
    with open(S.OUT_DIR / NAME, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    segs = len(re.findall(r"\^[0-9A-Za-z-]+\s*$", text, flags=re.M))
    print(f"wrote {NAME}: {len([x for x in text.splitlines() if x.strip()])} lines, {segs} segments")
    for w in SLIPS:
        print("SLIP", w)
    for p in probs[:80]:
        print("PROBLEM", p)
    print("line checks:", "OK" if not probs else f"{len(probs)} problems")
    sys.exit(1 if probs else 0)


if __name__ == "__main__":
    main()
