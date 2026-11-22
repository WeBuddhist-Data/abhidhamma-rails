# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 10-01-indriyayamaka.md (Indriyayamaka, paṇṇattivāra: uddesa and
niddesa), and the FACULTY TABLE for the later Indriya chapters 10-02 … 10-13.

Frames: family A from build_2-01_vi, imported and used VERBATIM (a_q, a_is, a_not, a_but_not, a_both, a_rest,
a_except, a_except_n, a_neither, a_and, a_sense, PANNATTI_UDDESAVARO, heading, variant, split_sentences); labels
from build_sample_vi.LABEL. The twenty-two faculties are the pi-2 Indriyavibhaṅga names (^2-219 / ^2-221).
Frames 2-01 / 2-02 did not cover (the «Yaṃ X indriyaṃ taṃ …» sentence, «Avasesaṃ / Avaseso X na …» with a member
subject, the bare words of the faculties, the «…pe…» joins) are settled here and listed in notes-10-01.md.

Later Indriya chapters use:

    import sys, importlib; sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai")
    I = importlib.import_module("build_10-01_vi")
    I.FACULTY        # the table: (Pāli stem, Vietnamese faculty name, bare Pāli forms, Vietnamese bare word), in order
    I.FACULTY_VI     # "cakkhundriya" -> "năng lực mắt" …   I.BARE_VI: "cakkhu" -> "mắt" …
    I.MEMBER / I.m() # every Pāli word form of this chapter -> Vietnamese noun phrase
    I.INDRIYA / I.INDRIYA_PL / I.TWENTYTWO / I.BAVISATI_VI
    I.translate_line(line, ctx) / I.translate_sentence(s, ctx)

Importing writes nothing; run  python -I -X utf8 -B build_10-01_vi.py  to rebuild the chapter.
"""
import importlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as S  # noqa: E402

F = importlib.import_module("build_2-01_vi")     # family A frame-setter (paṇṇattivāra)

NAME = "10-01-indriyayamaka.md"
cap, low = S.cap, S.low
LABEL = S.LABEL

# ================================================================ the faculty table (exposed for 10-02 … 10-13)
INDRIYA = "năng lực"                       # indriyaṃ (core, pi-1)
INDRIYA_PL = f"các {INDRIYA}"              # indriyā / indriye (2-01: the Pāli number is kept, khandhā = các khối)
TWENTYTWO = "Hai mươi hai năng lực"        # Bāvīsatindriyāni (pi-2 ^2-219 / ^2-221)
# (Pāli stem, Vietnamese faculty name [pi-2 ^2-221], bare Pāli word forms, Vietnamese bare word)
# bare words: pi-2 Indriyavibhaṅga / pi-1 core (mắt … ý as 3-01 BARE; người nữ / người nam, sự sống, sự dễ chịu …
# from the pi-2 definitions; anaññātaññassāmīti / aññā / aññātāvī from the inner part of the pi-2 faculty names)
FACULTY = [
    ("cakkhundriya", "năng lực mắt", ("cakkhu", "cakkhuṃ", "cakkhū"), "mắt"),
    ("sotindriya", "năng lực tai", ("sotaṃ",), "tai"),
    ("ghānindriya", "năng lực mũi", ("ghānaṃ",), "mũi"),
    ("jivhindriya", "năng lực lưỡi", ("jivhā", "jivhaṃ"), "lưỡi"),
    ("kāyindriya", "năng lực thân", ("kāyo", "kāyaṃ"), "thân"),
    ("manindriya", "năng lực ý", ("mano", "manaṃ"), "ý"),
    ("itthindriya", "năng lực nữ tính", ("itthī", "itthiṃ"), "người nữ"),
    ("purisindriya", "năng lực nam tính", ("puriso", "purisaṃ"), "người nam"),
    ("jīvitindriya", "năng lực sống", ("jīvitaṃ",), "sự sống"),
    ("sukhindriya", "năng lực dễ chịu", ("sukhaṃ",), "sự dễ chịu"),
    ("dukkhindriya", "năng lực khó chịu", ("dukkhaṃ",), "sự khó chịu"),
    ("somanassindriya", "năng lực niềm vui", ("somanassaṃ",), "niềm vui"),
    ("domanassindriya", "năng lực nỗi buồn", ("domanassaṃ",), "nỗi buồn"),
    ("upekkhindriya", "năng lực bình thản", ("upekkhā", "upekkhaṃ"), "sự bình thản"),
    ("saddhindriya", "năng lực niềm tin", ("saddhā", "saddhaṃ"), "niềm tin"),
    ("vīriyindriya", "năng lực tinh tấn", ("vīriyaṃ",), "sự tinh tấn"),
    ("satindriya", "năng lực tỉnh thức", ("sati", "satiṃ", "satī"), "sự tỉnh thức"),
    ("samādhindriya", "năng lực định tâm", ("samādhi", "samādhiṃ", "samādhī"), "định tâm"),
    ("paññindriya", "năng lực trí tuệ", ("paññā", "paññaṃ"), "trí tuệ"),
    ("anaññātaññassāmītindriya", "năng lực biết được điều chưa từng biết",
     ("anaññātaññassāmīti", "anaññātaññassāmī", "anaññātaññassāmītiṃ"), "sự biết được điều chưa từng biết"),
    ("aññindriya", "năng lực hiểu biết trọn vẹn", ("aññaṃ",), "sự hiểu biết trọn vẹn"),
    ("aññātāvindriya", "năng lực của người đã hiểu biết trọn vẹn", ("aññātāvī", "aññātāviṃ"),
     "người đã hiểu biết trọn vẹn"),
]
FACULTY_VI = {st: vi for st, vi, _, _ in FACULTY}
BARE_VI = {forms[0]: b for _, _, forms, b in FACULTY}
MEMBER = {"indriyaṃ": INDRIYA, "indriyā": INDRIYA_PL, "indriye": INDRIYA_PL}
for _st, _vi, _forms, _b in FACULTY:
    MEMBER[_st + "ṃ"] = _vi
    for _w in _forms:
        MEMBER[_w] = _b
BAVISATI_VI = f"{TWENTYTWO} – {', '.join(FACULTY_VI.values())}."   # = pi-2 ^2-221 (asserted)
# source spelling slips read as meant (each reported)
SLIP_ALIAS = {"anaññātaññāssāmīti": "anaññātaññassāmīti"}       # ^6-10-3
SLIPS = []


def m(w, ctx=""):
    """Pāli member word (any listed form, capitalised or not) -> Vietnamese noun phrase."""
    w = low(w)
    if w in SLIP_ALIAS:
        SLIPS.append((ctx, f"«{w}» read as «{SLIP_ALIAS[w]}» (spelling)"))
        w = SLIP_ALIAS[w]
    return MEMBER[w]


def is_member(w):
    return low(w) in MEMBER or low(w) in SLIP_ALIAS


def strip_ti(w):
    """cakkhundriyanti -> cakkhundriyaṃ; cakkhūti -> cakkhū; a listed member (sati, anaññātaññassāmīti) stays."""
    if is_member(w):
        return w
    if w.endswith("nti"):
        return w[:-3] + "ṃ"
    if w.endswith("ti"):
        return w[:-2]
    return w


def norm_ca(w):
    """Cakkhuñca -> cakkhuṃ; sotañceva -> sotaṃ (3-01 norm_ca)."""
    if w.endswith("ñceva"):
        return w[:-5] + "ṃ"
    if w.endswith("ñca"):
        return w[:-3] + "ṃ"
    return w


# ================================================================ word-sense subjects (2-01 A_SENSE; = build_3-01_vi SENSE)
SENSE = {
    "Dibbacakkhu paññācakkhu": F.a_sense("mắt", "thiên nhãn, mắt trí tuệ"),           # pi-5 «thiên nhãn, mắt trí tuệ»
    "Dibbasotaṃ taṇhāsotaṃ": F.a_sense("tai", "thiên nhĩ, dòng chảy của khao khát"),  # pi-5 «thiên nhĩ»; taṇhā pi-2
}
SENSE_RE = "|".join(re.escape(k) for k in SENSE)

# ================================================================ new frame: «Yaṃ X indriyaṃ taṃ Xñceva indriyañca.»
YA_SUBJ = "{x} nào {p}"                       # Yaṃ / Yo / Yā X Y  (relative subject: «tai nào là năng lực»)
YA_BOTH = "{s} thì {x} ấy vừa {a} vừa {b}."   # … taṃ / so / sā Xñceva Yñca. (S.BOTH «vừa … vừa …»)
YA_REL = {"Yaṃ": "taṃ", "Yo": "so", "Yā": "sā"}


def ya_both(x, y, a, b):
    """Yaṃ sotaṃ indriyaṃ taṃ sotañceva indriyañca. = «Tai nào là năng lực thì tai ấy vừa là tai vừa là năng lực.»"""
    return cap(YA_BOTH.format(s=YA_SUBJ.format(x=x, p=F.a_is(y)), x=x, a=F.a_is(a), b=F.a_is(b)))


# ================================================================ headings and exact lines
HEAD10 = {"Suddhindriyavāro": S.VARO.format(x=f"{INDRIYA_PL} thuần túy")}   # like Suddhakhandhavāro (sample SECTION)
assert S.SECTION["Suddhindriyamūlacakkavāro"] == S.VARO.format(x=f"vòng luân chuyển dựa trên {INDRIYA_PL} thuần túy")


def heading(t):
    return HEAD10.get(t) or F.heading(t)


V_VIRIYA = "[viriyindiyaṃ (sī. syā.)]"
EXACT_LINE = {
    ("Bāvīsatindriyāni – cakkhundriyaṃ, sotindriyaṃ, ghānindriyaṃ, jivhindriyaṃ, kāyindriyaṃ, manindriyaṃ, "
     "itthindriyaṃ, purisindriyaṃ, jīvitindriyaṃ, sukhindriyaṃ, dukkhindriyaṃ, somanassindriyaṃ, domanassindriyaṃ, "
     f"upekkhindriyaṃ, saddhindriyaṃ, vīriyindriyaṃ {V_VIRIYA}, satindriyaṃ, samādhindriyaṃ, paññindriyaṃ, "
     "anaññātaññassāmītindriyaṃ, aññindriyaṃ, aññātāvindriyaṃ."):
        BAVISATI_VI.replace(FACULTY_VI["vīriyindriya"] + ",",
                            f"{FACULTY_VI['vīriyindriya']} {F.variant(V_VIRIYA, S.SPELL)},"),
    # pi-2 ^2-219 has the same bracket as «[khác chính tả (Sī., Syā.): viriyindriyaṃ]»; this source spells it
    # «viriyindiyaṃ» (kept as written inside the bracket, reported)
}
EXACT_BODY = {                                 # sentence body (final punctuation split off) -> Vietnamese sentence
    "Āmantā": S.AMANTA,
    "No": F.NO,
    "Paṇṇattiuddesavāro": F.PANNATTI_UDDESAVARO,
}

# ================================================================ sentence parser
AV = r"(?:avaseso|avasesaṃ|avasesā)"
STATEMENTS = [
    # Dibbacakkhu paññācakkhu cakkhu, na cakkhundriyaṃ.
    (rf"(?P<s>{SENSE_RE}) (?P<a>\S+), na (?P<b>\S+)",
     lambda g, c: F.a_but_not(SENSE[g["s"]], F.a_is(m(g["a"], c)), F.a_not(m(g["b"], c)))),
    # Dibbacakkhu paññācakkhu na cakkhundriyaṃ, cakkhu.
    (rf"(?P<s>{SENSE_RE}) na (?P<b>\S+), (?P<a>\S+)",
     lambda g, c: F.a_but_not(SENSE[g["s"]], F.a_not(m(g["b"], c)), F.a_is(m(g["a"], c)))),
    # Cakkhuṃ ṭhapetvā avasesā indriyā na cakkhu, indriyā.
    (r"(?P<e>\S+) ṭhapetvā avasesā (?P<n>indriyā) na (?P<b>\S+), (?P<a>\S+)",
     lambda g, c: F.a_but_not(F.a_except_n(m(g["e"], c), m(g["n"], c)), F.a_not(m(g["b"], c)),
                              F.a_is(m(g["a"], c)))),
    # Kāyindriyaṃ ṭhapetvā avaseso na kāyindriyaṃ, kāyo.
    (rf"(?P<e>\S+) ṭhapetvā {AV} na (?P<b>\S+), (?P<a>\S+)",
     lambda g, c: F.a_but_not(F.a_except(m(g["e"], c)), F.a_not(m(g["b"], c)), F.a_is(m(g["a"], c)))),
    # Kāyindriyaṃ ṭhapetvā avaseso kāyo [var], na kāyindriyaṃ.  (^6-10-100: once without the comma)
    (rf"(?P<e>\S+) ṭhapetvā {AV} (?P<a>(?!na )[^\s,]+)(?P<v> \[[^\]]+\])?(?P<k>,?) na (?P<b>\S+)",
     lambda g, c: (_no_comma(g, c), F.a_but_not(F.a_except(m(g["e"], c)),
                                                F.a_is(m(g["a"], c)) + (" " + F.variant(g["v"].strip())
                                                                        if g["v"] else ""),
                                                F.a_not(m(g["b"], c))))[1]),
    # Cakkhuñca cakkhundriyañca ṭhapetvā avasesā na ceva cakkhu na ca cakkhundriyaṃ. / … indriye ca ṭhapetvā …
    (rf"(?P<a>\S+?)ñca (?P<b>\S+?)(?P<bk>ñca| ca) ṭhapetvā {AV} na ceva (?P<c>\S+) na ca (?P<d>\S+)",
     lambda g, c: F.a_neither(F.a_except(F.a_and(m(g["a"] + "ṃ", c),
                                                 m(g["b"] + ("ṃ" if g["bk"] == "ñca" else ""), c))),
                              m(g["c"], c), m(g["d"], c))),
    # Yaṃ sotaṃ indriyaṃ taṃ sotañceva indriyañca. / Yo kāyo … so kāyo ceva … / Yā upekkhā … sā upekkhā ceva …
    (r"(?P<r>Yaṃ|Yo|Yā) (?P<x>\S+) (?P<y>\S+) (?P<d>taṃ|so|sā) (?P<x2>\S+?)(?P<k>ñceva| ceva) (?P<b>\S+ñca)",
     lambda g, c: _ya(g, c)),
    # Cakkhundriyaṃ cakkhu ceva cakkhundriyañca. / Sotindriyaṃ indriyañceva sotindriyañca.
    (r"(?P<s>\S+) (?P<a>\S+?)(?P<k>ñceva| ceva) (?P<b>\S+ñca)",
     lambda g, c: F.a_both(m(g["s"], c), F.a_is(m(g["a"] + ("ṃ" if g["k"] == "ñceva" else ""), c)),
                           F.a_is(m(norm_ca(g["b"]), c)))),
    # Itthindriyaṃ na itthī, itthindriyaṃ. / Itthī na itthindriyaṃ, itthī.
    (r"(?P<s>\S+) na (?P<b>\S+), (?P<a>\S+)",
     lambda g, c: F.a_but_not(m(g["s"], c), F.a_not(m(g["b"], c)), F.a_is(m(g["a"], c)))),
    # Avasesā indriyā na sotindriyaṃ. / Avasesaṃ sotaṃ na indriyaṃ. / Avaseso kāyo na indriyā.
    (r"Avases(?:o|aṃ|ā) (?P<n>\S+) na (?P<b>\S+)",
     lambda g, c: (_rest_note(g, c), F.a_rest(m(g["n"], c), F.a_not(m(g["b"], c))))[1]),
]
STATEMENTS = [(re.compile(p), f) for p, f in STATEMENTS]


def _no_comma(g, c):
    if not g["k"]:
        SLIPS.append((c, "«… avaseso kāyo na kāyindriyaṃ»: comma missing before «na»; rendered as the comma form"))


def _rest_note(g, c):
    if g["n"] == "kāyo" and g["b"] == "indriyā":
        SLIPS.append((c, "«Avaseso kāyo na indriyā»: plural «indriyā» (elsewhere «na indriyaṃ»); translated as written"))


def _ya(g, c):
    assert YA_REL[g["r"]] == g["d"], g[0]
    x2 = g["x2"] + ("ṃ" if g["k"] == "ñceva" else "")
    assert low(x2) == low(g["x"]) and norm_ca(g["b"]) == g["y"], g[0]
    return ya_both(m(g["x"], c), m(g["y"], c), m(x2, c), m(norm_ca(g["b"]), c))


def _question(body, ctx):
    mm = re.fullmatch(r"(?:\((?P<l>Ka|Kha)\) )?(?P<b>.+)", body)
    lab, b = mm["l"], mm["b"]
    t = b.split()
    if len(t) == 4 and low(t[0]) == "na" and t[2] == "na":
        neg, x, y = True, t[1], t[3]
    elif len(t) == 2:
        neg, x, y = False, t[0], t[1]
    else:
        return None
    y = strip_ti(y)
    if not (is_member(x) and is_member(y)):
        return None
    return F.a_q(m(x, ctx), m(y, ctx), neg=neg, label=lab)


def translate_body(body, ctx):
    """One Pāli sentence body (no final punctuation) -> Vietnamese sentence with the frame's own final mark."""
    if body in EXACT_BODY:
        return EXACT_BODY[body]
    for rx, f in STATEMENTS:
        mm = rx.fullmatch(body)
        if mm:
            return f(mm, ctx)
    return None


def translate_sentence(s, ctx=""):
    """Pāli sentence (with or without its final «.» / «?») -> Vietnamese; the Pāli mark replaces the frame's."""
    s = s.strip()
    punct = s[-1] if s[-1:] in (".", "?") else ""
    body = s[:-1] if punct else s
    if punct == "?" or (not punct and _question(body, ctx)):
        out = _question(body, ctx)
        kind = "?"
    else:
        out = translate_body(body, ctx)
        kind = "."
    if out is None:
        raise ValueError(f"unmatched sentence: {s!r} ({ctx})")
    assert out[-1] == kind, (s, out)
    out = out[:-1] + punct
    if body[:1].islower():                    # a chunk after «…pe…» starts lowercase in the Pāli
        out = low(out)
    return out


def tr_sentences(text, ctx):
    return " ".join(translate_sentence(s, ctx) for s in F.split_sentences(text.strip()) if s.strip())


PE_RE = re.compile(r"…(?:pe|Pe)…")
PE = "…"


def tr_pe(text, ctx):
    """A line with «…pe…»: each piece is translated in place and the ellipsis stays at the same spot. A period before
    or after it gives way to it («….» is never written); «?…» is written «? …»; «Āmantā …pe….» = «Đúng vậy…» (7-04)."""
    pieces = []
    for chunk in PE_RE.split(text):
        lead = chunk[:len(chunk) - len(chunk.lstrip())]
        trail = chunk[len(chunk.rstrip()):]
        core = chunk.strip()
        pieces.append(lead + (tr_sentences(core, ctx) if core and core != "." else core) + trail)
    out = PE.join(pieces)
    prev = None
    while prev != out:
        prev = out
        out = out.replace(".…", "…").replace("….", "…").replace("?…", "? …")
    return out.replace(f"{S.AMANTA[:-1]} …", f"{S.AMANTA[:-1]}…")


def translate_line(line, ctx=""):
    mm = re.match(r"^(?P<h>#+ )?(?P<t>.*?)(?P<id> \^[0-9A-Za-z-]+)?$", line)
    h, t, sid = mm["h"] or "", mm["t"], mm["id"] or ""
    if h:
        return h + heading(t) + sid
    if t in EXACT_LINE:
        SLIPS.append((ctx, f"variant bracket {V_VIRIYA}: «viriyindiyaṃ» (pi-2: viriyindriyaṃ); kept as written"))
        return EXACT_LINE[t] + sid
    if PE_RE.search(t):
        return tr_pe(t, ctx) + sid
    return tr_sentences(t, ctx) + sid


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


def label_slips(pali):
    """Report a (Ka) / (Kha) label that breaks the Ka-Kha alternation (kept as written)."""
    labs = [(i, mm.group(1)) for i, ln in enumerate(pali.splitlines(), 1)
            for mm in [re.match(r"\((Ka|Kha)\) (?!uddeso|niddeso|anulomaṃ|paccanīkaṃ)", ln)] if mm]
    out = []
    for (i1, l1), (i2, l2) in zip(labs, labs[1:]):
        if l1 == l2 == "Ka" and "indriyā" in pali.splitlines()[i2 - 1]:
            out.append(f"source line {i2}: «{pali.splitlines()[i2 - 1]}» has (Ka) on the (Kha) question; kept (a)")
    return out


# ================================================================ checks
CROSS_BOOK = [
    (BAVISATI_VI, 2), (TWENTYTWO, 2), ("[khác chính tả (Sī., Syā.): viriyindriyaṃ]", 2), ("năng lực", 1),
    ("mắt", 2), ("tai", 2), ("mũi", 2), ("lưỡi", 2), ("thân", 2), ("ý", 2), ("người nữ", 2), ("người nam", 2),
    ("sự sống", 2), ("sự dễ chịu", 2), ("sự khó chịu", 2), ("niềm vui", 2), ("nỗi buồn", 2), ("sự bình thản", 2),
    ("niềm tin", 2), ("sự tinh tấn", 2), ("sự tỉnh thức", 2), ("định tâm", 2), ("trí tuệ", 2),
    ("biết được điều chưa từng biết", 2), ("sự hiểu biết trọn vẹn", 1), ("người đã hiểu biết trọn vẹn", 2),
    ("thiên nhãn", 5), ("mắt trí tuệ", 5), ("thiên nhĩ", 5), ("dòng chảy", 2), ("khao khát", 2),
    ("thuần túy", 5), ("vòng luân chuyển", 5), ("còn lại", 1), ("ngoại trừ", 2), ("vừa là", 1),
]


def check_cross_book():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in S.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts (10-01): {len(CROSS_BOOK)} strings found in pi-1..5 rails")


def check_frames():
    """The family-A frames used here are byte-identical with 2-01's output (same Pāli shape, Khandha members)."""
    assert F.a_q("vật chất", "khối vật chất") == "(a) Vật chất có phải là khối vật chất không?"
    assert F.a_q("các khối", "khối thức", neg=True, label="Kha") == \
        "(b) Những gì không phải là các khối thì không phải là khối thức, có đúng không?"
    assert F.PANNATTI_UDDESAVARO == "Mục nêu đề mục về sự định danh."
    assert S.LABEL["Ka"] == "(a)" and S.LABEL["Kha"] == "(b)"
    try:                                               # 3-01 (running in parallel) uses the same sense subjects
        A3 = importlib.import_module("build_3-01_vi")
        for k, v in SENSE.items():
            if A3.SENSE.get(k) != v:
                print(f"WARN: sense subject {k!r} differs from build_3-01_vi: {A3.SENSE.get(k)!r}")
    except Exception as e:                             # noqa: BLE001
        print("note: build_3-01_vi not importable for the sense check:", e)


def check_extra(text, pali):
    probs = []
    for i, ln in enumerate(text.splitlines(), 1):
        body = re.sub(r" ?\[[^\]]*\]", "", re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", ln))
        for bad in ("….", ".…", "?…", "  ", "là là", "thì thì", "indriy", "ṭhapetvā", " ca ", "cakkhu", "pe…", "Pe…",
                    ",,"):
            if bad in body:
                probs.append(f"line {i}: «{bad}»")
    # identical Pāli line -> identical Vietnamese line
    pl, vl = pali.splitlines(), text.splitlines()
    seen = {}
    for p, v in zip(pl, vl):
        p0, v0 = re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", p), re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", v)
        if p0.strip() and seen.setdefault(p0, v0) != v0:
            probs.append(f"identical Pāli rendered differently: {p0[:60]}")
    return probs


def main():
    S.check_cross_book()
    F.check_cross_book()
    check_cross_book()
    check_frames()
    del SLIPS[:]
    text = unicodedata.normalize("NFC", translate_file())
    pali = (S.PALI_DIR / NAME).read_text(encoding="utf-8")
    probs = S.check_lines(pali, text, NAME) + check_extra(text, pali)
    with open(S.OUT_DIR / NAME, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    segs = len(re.findall(r"\^[0-9A-Za-z-]+\s*$", text, flags=re.M))
    print(f"wrote {NAME}: {len([x for x in text.splitlines() if x.strip()])} lines, {segs} segments")
    seen = set()
    for c, w in SLIPS:
        if (c, w) not in seen:
            seen.add((c, w))
            print("SLIP", c, "|", w)
    for x in label_slips(pali):
        print("SLIP", x)
    for p in probs[:80]:
        print("PROBLEM", p)
    print("line checks:", "OK" if not probs else f"{len(probs)} problems")
    sys.exit(1 if probs else 0)


if __name__ == "__main__":
    main()
