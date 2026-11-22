"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 3-04 (Āyatanayamaka, part 4: the nirodhavāra in all tenses).

Everything comes from the Āyatana chain build_rails_3-03_vi → build_rails_3-02_vi → build_rails_3-01_vi →
build_rails_2-01_vi / build_rails_7-01_vi (+ build_rails_2-02_vi, build_rails_4_vi for the note wording), all
imported READ-ONLY. This file adds, for 3-05 / 3-06:

  BOTH_NA_RE / b_both_na     the both-frame with a SEPARATE negative verb ("A-ñca na nirujjhati B-ñca na
                             nirujjhati") = 2-01 b_both with 2-01's VERB_TABLE («A không chấm dứt, B cũng không
                             chấm dứt»), plain heads (3-02 answer_head) and ye-ca heads (3-03 ye_ca_head)
  CUTQ0_RE / cut_q0          a pair question cut by …pe… with no verb after the cut: "(Kha) yassa vā pana
                             yattha…pe…?" «(b) Còn ở người nào, ở nơi nào mà… không?» (= 3-03 cut_pair_q minus the verb)
  ti_cut                     a pair question cut after its -ti ("… nirujjhatīti…pe… [B… C… D V-ti?]"): the full
                             shell with «không», then «…» (a cut question without «?» keeps «không», 3-01 naming cuts)
  head_fragment              an answer cut after its person head ("Rūpāvacarānaṃ…pe… kāmāvacarānaṃ…pe….")
                             «Ở chúng sinh trong cõi hình sắc… ở chúng sinh trong cõi dục lạc…» (3-02 answer_head)
  comma_join                 two answers joined by the Pāli's comma (^6-3-148): kept «…, ở …»
  NOTES_3_04                 the editorial notes of this chapter (uppādepi nirodhepi …, Yassa yatthakampi …, Yathā …)
  sentence_vi / unit_vi / units_vi / cut_line / line_vi / tr_line / build   3-03's chain with the pieces above
A line, unit or word the parsers cannot place raises ValueError (no silent fallback). Importing writes nothing.

    A4 = importlib.import_module("build_rails_3-04_vi"); segs = A4.build("3-05-ayatanayamaka.md", fixed=…)

usage: python -I -X utf8 -B build_rails_3-04_vi.py   (probe: … build_rails_3-04_vi.py probe)
"""
import importlib
import re
import sys
import unicodedata

RAILS_DIR = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\rails"
if RAILS_DIR not in sys.path:
    sys.path.insert(0, RAILS_DIR)
import build_rails_sample_vi as S  # noqa: E402  (READ-ONLY)
A3 = importlib.import_module("build_rails_3-03_vi")  # READ-ONLY: Āyatana chain, ye-ca heads, cut pair questions
A2 = importlib.import_module("build_rails_3-02_vi")  # READ-ONLY: Āyatana heads with planes
A = importlib.import_module("build_rails_3-01_vi")   # READ-ONLY: the Āyatana module
B = importlib.import_module("build_rails_2-01_vi")   # READ-ONLY: families A / B
C = importlib.import_module("build_rails_7-01_vi")   # READ-ONLY: shared shell and answer shapes
D = importlib.import_module("build_rails_2-02_vi")   # READ-ONLY: "P ye ca …" head, closing lines
G = importlib.import_module("build_rails_4_vi")      # READ-ONLY: note wording (vitthāretabbā, Yathā … evaṃ …)

cap = S.cap
CH = "3-04-ayatanayamaka.md"
N = "3-04"
NOTES_MD = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/notes-rails-{N}.md"
ADH_DIR = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/adh-{N}"
SLIPS_SEEN = []
JOINS_SEEN = []
PLANES = A.PLANES_AY
LAB = A.LAB

# ===============================================================================================================
# 1. Both-frame with a separate "na" (nirodhavāra): 2-01 b_both, 2-01 VERB_TABLE
# ===============================================================================================================
BOTH_RE = re.compile(r"(\S+?ñca) ((?:na )?\S+) (\S+?ñca) ((?:na )?\S+)")
BOTH_NA_RE = re.compile(r"(.+?) " + A.LOC + r" (\S+?ñca (?:na )?\S+ \S+?ñca (?:na )?\S+)\.")


def b_both_na(s, M=None, planes=None, force=False):
    """'H tesaṃ [tattha] A-ñca [na] V B-ñca [na] W.' → B.b_both («H, thì ở những người ấy A V, B cũng W.»).
    Only sentences with a separate "na" (the 3-01 … 3-03 regexes take one-word verbs); force=True builds the
    positive ones too (for the check against 3-03)."""
    M = M or A.AYATANA
    if (m := A3.YE_HEAD_RE.fullmatch(s)) is not None:
        head, loc, rest = m.groups()
        head_vi = None
    elif (m := BOTH_NA_RE.fullmatch(s)) is not None:
        head, loc, rest = m.groups()
        head_vi = None
    else:
        return None
    mm = BOTH_RE.fullmatch(rest)
    if not mm or "," in head:                    # a comma in the head: two answers (comma_join)
        return None
    c1, v1, c2, v2 = mm.groups()
    if not force and not (v1.startswith("na ") or v2.startswith("na ")):
        return None
    head_vi = A3.ye_ca_head(head, planes) if f" {D.YE_CA} " in head else A2.answer_head(head, loc, planes)
    return B.b_both(head_vi, loc, M.subj(c1), B.verb(v1), M.subj(c2), B.verb(v2))


# ===============================================================================================================
# 2. Cut questions
# ===============================================================================================================
CUTQ0_RE = re.compile(r"(?:" + LAB + r" )?([Yy]assa)( vā pana)?( yattha)?((?: \S+)?)…pe…\?")


def cut_q0(u, M=None):
    """'(Kha) yassa vā pana yattha…pe…?' / '(Ka) yassa yattha manāyatanaṃ…pe…?' → the shell (B.b_q) up to «mà»
    [+ A], «…», «không?» (3-03 cut_pair_q with no verb; 7-02 «(b) Còn ở nơi nào mà… không?»)."""
    M = M or A.AYATANA
    m = CUTQ0_RE.fullmatch(u)
    if not m:
        return None
    label, w1, vapana, w2, mem = m.groups()
    who = w1.lower() + (w2 or "")
    full = B.b_q(label, who, C.Q_COR[who], "⟨A⟩", "⟨V⟩", "⟨B⟩", "⟨W⟩", other=bool(vapana))
    head, sep, _ = full.partition(" ⟨A⟩ ⟨V⟩")
    assert sep and full.endswith(" ⟨B⟩ ⟨W⟩ không?"), full
    first = head + (f" {M.subj(mem.strip())}" if mem.strip() else "")
    return f"{first}{S.PE} không?"


TI_CUT_RE = re.compile(r"(.+?ti)…pe…((?: .*)?)")


def ti_cut(body, M=None, planes=None):
    """'Yassa [yattha] A V tassa [tattha] B Vti…pe…[ C… D… E Vti?][ (note).]' → the full pair question with
    «không», «…», then the cut list «C… D… E V không?» and the notes. None if the line is not of this shape."""
    M = M or A.AYATANA
    m = TI_CUT_RE.fullmatch(body)
    if not m or not A.BQ_RE.fullmatch(m.group(1)):
        return None
    q, rest = m.groups()
    full = A.question_vi(q, M)
    assert full.endswith(" không?"), full
    out = full[:-1] + S.PE
    rest = rest.strip()
    if mm := re.fullmatch(r"(.+?\?)((?: .*)?)", rest):
        lst, tail = mm.group(1)[:-1], mm.group(2)
        names, v = A.split_mv(lst, M)
        if v != A.split_mv(A.BQ_RE.fullmatch(q).group(7), M)[1]:
            raise ValueError(f"cut list verb differs from the question's in {body!r}")
        out += f" {names} {v[0]} không?"
        rest = tail.strip()
    if rest:
        out += " " + units_vi(rest, M, planes)
    return out


# ===============================================================================================================
# 3. Answer fragments: a person head cut by …pe…; two answers joined by a comma
# ===============================================================================================================
def head_fragment(u, planes=None):
    """'Rūpāvacarānaṃ' / 'Asaññasattānaṃ arūpānaṃ' (an answer cut after its head) → 3-02 answer_head
    («Ở chúng sinh trong cõi hình sắc»); None if the words are not a person phrase."""
    try:
        A2.ay_person_items(u, planes or PLANES)
    except ValueError:
        return None
    return A2.answer_head(u, "tesaṃ", planes)


COMMA_JOIN_RE = re.compile(r", (?=[^\W\d_]\S*ānaṃ )")


def comma_join(s, M=None, planes=None):
    """'<answer 1>, <answer 2 with a lower-case head>.' (the Pāli's comma between two answers, ^6-3-148) →
    «<answer 1 without its «.»>, <answer 2 with a lower-case «ở»>.»: the comma is kept, nothing is added.
    Every ", <lower-case …ānaṃ>" is tried; both halves must be whole answers. None if no split works."""
    M = M or A.AYATANA
    if not s.endswith("."):
        return None
    for m in COMMA_JOIN_RE.finditer(s):
        if not s[m.end()].islower():
            continue
        first, second = s[:m.start()] + ".", cap(s[m.end():])
        try:
            v1, v2 = sentence_vi(first, M, planes), sentence_vi(second, M, planes)
        except ValueError:
            continue
        JOINS_SEEN.append(s)
        return f"{v1[:-1]}, {v2[:1].lower()}{v2[1:]}"
    return None


# ===============================================================================================================
# 4. Editorial notes of this chapter
# ===============================================================================================================
VITTHARETABBAM = "nên được trình bày chi tiết"   # vitthāretabbaṃ (pi-5; = 5-01 VITTHARETABBAM)
VITTHARITA = f"đã được {VITTHARETABBAM[len('nên được '):]}"   # vitthāritā «đã được trình bày chi tiết»
assert VITTHARETABBAM in G.DETAILED
LIKEWISE = "giống như vậy"               # sadisaṃ (with one subject: «giống như vậy»; 3-02 SADISA «giống nhau»)
PUCCHA = "câu hỏi"                       # pucchā (termbase)
P_PERSON = "phần về người"               # Yassakampi (termbase; = 5-01 P_PERSON)
P_PERSON_PLACE = "phần về người và nơi chốn"   # Yassa yatthakampi / yassa yatthake (termbase; = 5-01)
P_PLACE = "phần về nơi chốn"             # yatthakaṃ (termbase; = 3-01 / 5-01)
ALSO = C.ALSO                            # -pi «cũng»
UPPADE = "sự sinh khởi"                  # uppādepi (termbase)
NIRODHE = "sự chấm dứt"                  # nirodhepi (termbase)
UPPADANIRODHE = "sự sinh khởi và sự chấm dứt"   # uppādanirodhepi (termbase)
ANULOMA, PACCANIKA = B.ORDER["anuloma"].lower(), B.ORDER["paccanīka"].lower()   # anulomampi / paccanīkampi
VARAS = [B.UPPADAVARO, B.NIRODHAVARO, B.UPPADANIRODHAVARO]   # Uppādavārepi nirodhavārepi uppādanirodhavārepi
_AT_ALL = ", ".join(f"{C.AT} {x}" for x in (UPPADE, NIRODHE, UPPADANIRODHE))
NOTES_3_04 = {
    "(uppādepi nirodhepi uppādanirodhepi yatthakaṃ sabbattha sadisaṃ).":
        f"({_AT_ALL}, {P_PLACE} {A.SABBATTHA_CASES} đều {A2.SADISA}).",
    "(Yassa yatthakampi sadisaṃ vitthāretabbaṃ).":
        f"({cap(P_PERSON_PLACE)} {ALSO} {VITTHARETABBAM} {LIKEWISE}).",
    "(yassa yatthakampi yassakasadisaṃ).":
        f"({P_PERSON_PLACE} {ALSO} giống như {P_PERSON}).",       # yassakasadisaṃ (termbase; = 3-01)
    "(Uppādavārepi nirodhavārepi uppādanirodhavārepi atītā pucchā anulomampi paccanīkampi ⟦0⟧ sadisaṃ.)":
        (f"({cap(', '.join(f'{C.AT} {v}' for v in VARAS))}, {PUCCHA} về {B.TIME['Atīta']} theo {ANULOMA} và "
         f"{PACCANIKA} ⟦0⟧ đều {A2.SADISA}.)"),
    "(Yathā uppādavāre yassa yatthake anāgatā pucchā vitthāritā, evaṃ nirodhepi vitthāretabbā).":
        (f"(Như trong {B.UPPADAVARO}, {PUCCHA} về {B.TIME['Anāgata']} trong {P_PERSON_PLACE} {VITTHARITA}, "
         f"{C.AT} {NIRODHE} {G.DETAILED})."),
}
VARIANTS_3_04 = {"[paccaniyampi (sī. syā. ka.)]": "form"}

SLIPS = dict(A3.SLIPS)
SLIPS.update({   # plain slips and punctuation, rendered as meant (reported)
    "na nirujjhatī ti…pe…": "na nirujjhatīti…pe…",                # ^6-3-131 «ti» written apart
    "rūpāyatanaṃ …pe…": "rūpāyatanaṃ…pe…",                        # ^6-3-151 stray space before the cut
})

# ===============================================================================================================
# 5. Sentences, units, lines (3-03's chain)
# ===============================================================================================================


def sentence_vi(s, M=None, planes=None):
    M = M or A.AYATANA
    if s in NOTES_3_04:
        return NOTES_3_04[s]
    if (out := b_both_na(s, M, planes)) is not None:
        return out
    try:
        return A3.sentence_vi(s, M, planes)
    except ValueError:
        if (out := comma_join(s, M, planes)) is not None:
            return out
        raise


def unit_vi(u, M=None, planes=None):
    M = M or A.AYATANA
    if u in NOTES_3_04:
        return NOTES_3_04[u]
    if (out := cut_q0(u, M)) is not None:
        return out
    if (out := A3.cut_pair_q(u, M)) is not None:
        return out
    lower = u[:1].islower()
    p = cap(u) if lower else u
    out = None
    if p[:1].isupper() and p.endswith(".") and not p.startswith("(") and "…" not in p:
        try:
            out = sentence_vi(p, M, planes)
        except ValueError:
            out = None
    elif not p.endswith((".", "?", ")")) and not p.startswith("("):
        out = head_fragment(p, planes)
    if out is None:
        return A3.unit_vi(u, M, planes)
    if lower and not out.startswith("("):
        out = out[:1].lower() + out[1:]
    return out


def units_vi(piece, M=None, planes=None):
    units = [x for x in re.split(r"(?<=[.?]) (?=\S)", piece.strip()) if x]
    return " ".join(unit_vi(x, M, planes) for x in units)


def cut_line(body, M=None, planes=None):
    """3-01 line_vi's piece loop (A.CUT_RE: «.» before a cut absorbed, the cut's own «.» absorbed) on this file's
    units."""
    M = M or A.AYATANA
    out, pos = "", 0
    for m in A.CUT_RE.finditer(body):
        piece = body[pos:m.start()]
        if piece.strip():
            if out:
                out += " " if piece.startswith(" ") else ""
            out += units_vi(piece, M, planes)
        if out.endswith("."):
            out = out[:-1]
        out += (" " if m.group(1) else "") + S.PE
        pos = m.end()
    piece = body[pos:]
    if piece.strip():
        if out:
            out += " " if piece.startswith(" ") else ""
        out += units_vi(piece, M, planes)
    return out


def line_vi(body, M=None, planes=None):
    M = M or A.AYATANA
    if (out := ti_cut(body, M, planes)) is not None:
        return out
    units = [x for x in re.split(r"(?<=[.?]) (?=\S)", body.strip()) if x]
    if any(A3.CUTQ_RE.fullmatch(x) or CUTQ0_RE.fullmatch(x) for x in units):
        return " ".join(unit_vi(x, M, planes) for x in units)
    if "…" in body:
        if (lq := A.list_question(body, M)) is not None:
            return lq
        out = cut_line(body, M, planes)
        try:                                     # where 3-03 can build the line, it must be byte-identical
            old = A3.line_vi(body, M, planes)
        except ValueError:
            old = None
        if old is not None and old != out:
            raise AssertionError(f"3-03 differs:\n{old}\n{out}")
        return out
    return units_vi(body, M, planes)


def tr_line(p, M=None, fixed=None, variant_kind=None, planes=None, yamaka=A.YAMAKA):
    M = M or A.AYATANA
    m = re.search(r" (\^\S+)$", p)
    bid = m.group(1) if m else None
    body = p[:m.start()] if m else p
    fixed = fixed or {}
    variant_kind = {**VARIANTS_3_04, **(variant_kind or {})}
    if body.startswith("#"):
        hashes, text = body.split(" ", 1)
        out = f"{hashes} {A.heading(text, yamaka)}"
    elif body in fixed:
        out = fixed[body]
    else:
        for bad, good in SLIPS.items():
            if bad in body:
                SLIPS_SEEN.append((bid, bad, good))
                body = body.replace(bad, good)
        brs = re.findall(r"\[[^\]]*\]", body)
        for k, br in enumerate(brs):
            body = body.replace(br, f"⟦{k}⟧", 1)
        out = line_vi(body, M, planes)
        for k, br in enumerate(brs):
            if br not in variant_kind:
                raise ValueError(f"undeclared variant {br!r}")
            if f"⟦{k}⟧" not in out:
                raise ValueError(f"variant {br!r} lost in {p!r}")
            out = out.replace(f"⟦{k}⟧", A.var_vi(br, variant_kind[br]))
    if "⟦" in out:
        raise ValueError(f"unplaced variant in {p!r}")
    return f"{out} {bid}" if bid else out


def build(name, M=None, fixed=None, variant_kind=None, planes=None, yamaka=A.YAMAKA):
    return [[tr_line(ln, M, fixed, variant_kind, planes, yamaka) for ln in seg] for seg in S.segments_of(name)]


# ===============================================================================================================
# 6. Checks
# ===============================================================================================================
REUSED = [   # (Pāli, Vietnamese, book): asserted to occur in that book's Vietnamese rails
    ("vitthāretabbaṃ", VITTHARETABBAM, "5"),
    ("… vitthāretabbā (pi-2, via rails 4)", G.DETAILED, "2"),
]


def check_reused():
    texts = {b: unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md"))))
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED if unicodedata.normalize("NFC", v).lower() not in texts[b].lower()]
    assert not bad, "reused strings not found in their rails: " + repr(bad)


def check_frames():
    M = A.AYATANA
    # the both-frame: a positive sentence built here = 3-03's string
    for s in ("Sacakkhukānaṃ sasotakānaṃ cavantānaṃ tesaṃ cakkhāyatanañca nirujjhati sotāyatanañca nirujjhati.",
              "Itaresaṃ sacakkhukānaṃ cavantānaṃ tesaṃ tattha cakkhāyatanañca nirujjhati sotāyatanañca nirujjhittha.",
              "Pacchimabhavikānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ tesaṃ "
              "ghānāyatanañca nirujjhissati cakkhāyatanañca nirujjhissati."):
        assert b_both_na(s, M, force=True) == A3.sentence_vi(s, M), s
    # the negative both-frame = the positive one with 2-01's negative verbs
    pos = b_both_na("Parinibbantānaṃ tesaṃ cakkhāyatanañca nirujjhati dhammāyatanañca nirujjhati.", M, force=True)
    neg = b_both_na("Parinibbantānaṃ tesaṃ cakkhāyatanañca na nirujjhati dhammāyatanañca na nirujjhati.", M)
    assert neg == pos.replace(f" {B.VERB['nirujjhati'][0]}", f" {B.VERB['na nirujjhati'][0]}"), (pos, neg)
    # the verb-less cut question = 3-03's cut question without its verb
    full = A3.cut_pair_q("(Kha) yassa vā pana yattha…pe… nirujjhissatīti?", M)
    assert full == cut_q0("(Kha) yassa vā pana yattha…pe…?", M).replace(
        " không?", f" {B.VERB['nirujjhissati'][0]} không?"), full
    # a head fragment = 3-02 answer_head
    assert head_fragment("Rūpāvacarānaṃ arūpāvacarānaṃ") == A2.answer_head("Rūpāvacarānaṃ arūpāvacarānaṃ", "tesaṃ")
    print(f"comma-joined answers: {len(JOINS_SEEN)}")


# ===============================================================================================================
# 7. Notes file (Pāli = tiếng Việt)
# ===============================================================================================================
def notes():
    M = A.AYATANA
    out = []

    def row(p, v):
        out.append(f"{p} = {v}")

    def h(t):
        out.extend(["", f"## {t}", ""])

    out += [f"# pi-6 rails {N} (Āyatanayamaka 4): the nirodhavāra on the 3-03 Āyatana chain", "",
            "Builder: build_rails_3-04_vi.py (import with importlib). Members, attributes, heads, labels, verbs and "
            "all frames are 3-03's / 3-02's / 3-01's (on 2-01 / 7-01 / 2-02); 2-01's VERB_TABLE gives nirujjhati "
            "«chấm dứt», na nirujjhati «không chấm dứt», nirujjhittha «đã chấm dứt», na nirujjhittha «chưa từng chấm "
            "dứt», nirujjhissati «sẽ chấm dứt», na nirujjhissati «sẽ không chấm dứt»; after no ca «vẫn chấm dứt» / "
            "«đã từng chấm dứt» / «vẫn sẽ chấm dứt». New here, exposed for 3-05 / 3-06: `BOTH_RE`, `BOTH_NA_RE`, "
            "`b_both_na`, `CUTQ0_RE`, `cut_q0`, `TI_CUT_RE`, `ti_cut`, `head_fragment`, `comma_join`, `NOTES_3_04` "
            "(and its pieces `VITTHARETABBAM`, `VITTHARITA`, `LIKEWISE`, `PUCCHA`, `P_PERSON`, `P_PERSON_PLACE`, "
            "`P_PLACE`, `UPPADE`, `NIRODHE`, `UPPADANIRODHE`, `ANULOMA`, `PACCANIKA`, `VARAS`), `VARIANTS_3_04`, "
            "`SLIPS`, `sentence_vi`, `unit_vi`, `units_vi`, `cut_line`, `line_vi`, `tr_line`, `build`. Where 3-03 "
            "can build a string or a line, the builder asserts it is 3-03's byte for byte. Format: Pāli = tiếng Việt.",
            ""]
    h("Both-frame with a separate na (new; 2-01 b_both + VERB_TABLE)")
    for s in ("Sabbesaṃ upapajjantānaṃ acakkhukānaṃ asotakānaṃ cavantānaṃ tesaṃ cakkhāyatanañca na nirujjhati "
              "sotāyatanañca na nirujjhati.",
              "Parinibbantānaṃ tesaṃ cakkhāyatanañca na nirujjhissati dhammāyatanañca na nirujjhissati.",
              "Pañcavokāre parinibbantānaṃ arūpe pacchimabhavikānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti "
              "tesaṃ cavantānaṃ tesaṃ ghānāyatanañca na nirujjhissati cakkhāyatanañca na nirujjhissati.",
              "Suddhāvāsaṃ upapajjantānaṃ asaññasattānaṃ arūpānaṃ tesaṃ tattha cakkhāyatanañca na nirujjhati "
              "sotāyatanañca na nirujjhittha.",
              "Suddhāvāsaṃ upapajjantānaṃ asaññasattaṃ upapajjantānaṃ tesaṃ tattha rūpāyatanañca na nirujjhati "
              "manāyatanañca na nirujjhittha."):
        row(s, sentence_vi(s, M))
    h("Other answer shapes of this chapter (all 3-03 / 3-02)")
    for s in ("Acakkhukānaṃ sasotakānaṃ cavantānaṃ tesaṃ cakkhāyatanaṃ na nirujjhati, no ca tesaṃ sotāyatanaṃ na "
              "nirujjhati.",
              "Sabbesaṃ upapajjantānaṃ acakkhukānaṃ cavantānaṃ tesaṃ sotāyatanaṃ nirujjhittha, no ca tesaṃ "
              "cakkhāyatanaṃ nirujjhati.",
              "Pañcavokāraṃ upapajjantānaṃ acakkhukānaṃ kāmāvacarā cavantānaṃ tesaṃ tattha cakkhāyatanaṃ na "
              "nirujjhati, no ca tesaṃ tattha sotāyatanaṃ na nirujjhittha.",
              "Suddhāvāse parinibbantānaṃ asaññasattā cavantānaṃ tesaṃ tattha rūpāyatanaṃ nirujjhati, no ca tesaṃ "
              "tattha manāyatanaṃ nirujjhittha."):
        row(s, sentence_vi(s, M))
    h("Cut questions (new)")
    for q in ("(Kha) yassa vā pana yattha…pe…?", "(Ka) yassa yattha manāyatanaṃ…pe…?"):
        row(q, cut_q0(q, M))
    for q in ("Yassa yattha cakkhāyatanaṃ na nirujjhati tassa tattha sotāyatanaṃ na nirujjhatīti…pe…",
              "Yassa yattha cakkhāyatanaṃ nirujjhati tassa tattha sotāyatanaṃ nirujjhatīti…pe… ghānāyatanaṃ… "
              "rūpāyatanaṃ… manāyatanaṃ… dhammāyatanaṃ nirujjhatīti?"):
        row(q, ti_cut(q, M))
    out.append("(a pair question cut after its -ti without «?» keeps «không» and ends «…», as 3-01's cut naming "
               "questions «X có phải là Y không…»)")
    h("Answers cut after their person head (new)")
    for ln in ("Rūpāvacarānaṃ…pe… kāmāvacarānaṃ…pe….", "Asaññasattānaṃ arūpānaṃ…pe… pañcavokārānaṃ…pe….",
               "Arūpānaṃ…pe… pañcavokārānaṃ asaññasattānaṃ…pe…."):
        row(ln, line_vi(ln, M))
    h("Editorial notes (new)")
    for p, v in NOTES_3_04.items():
        row(p.replace("⟦0⟧", "[paccaniyampi (sī. syā. ka.)]"),
            v.replace("⟦0⟧", A.var_vi("[paccaniyampi (sī. syā. ka.)]", "form")))
    row("vitthāretabbaṃ / vitthāritā / … vitthāretabbā (Yathā …, evaṃ …)",
        f"{VITTHARETABBAM} (pi-5) / {VITTHARITA} / {G.DETAILED} (pi-2, rails 4)")
    row("sadisaṃ with one subject («the same way»)", LIKEWISE)
    row("pucchā / atītā pucchā / anāgatā pucchā", f"{PUCCHA} / {PUCCHA} về {B.TIME['Atīta']} / "
        f"{PUCCHA} về {B.TIME['Anāgata']}")
    row("uppāde / nirodhe / uppādanirodhe (+pi)", f"{C.AT} {UPPADE} / {C.AT} {NIRODHE} / {C.AT} {UPPADANIRODHE}")
    row("Uppādavārepi nirodhavārepi uppādanirodhavārepi", cap(", ".join(f"{C.AT} {v}" for v in VARAS)))
    row("anulomampi paccanīkampi", f"theo {ANULOMA} và {PACCANIKA}")
    h("Termbase misfits and gaps (for the coordinator)")
    out += [
        "- No new member, person, plane or verb words: all from 3-01 … 3-03 / 2-01 (2-01 VERB_TABLE has the "
        "nirujjhati forms with a separate na).",
        "- uppādepi / nirodhepi / uppādanirodhepi: termbase «sự sinh khởi» / «sự chấm dứt» / «sự sinh khởi và sự "
        "chấm dứt» (no «mục về»: the Pāli has no vāra here), each with «ở» as 3-01's «ở hiện tại, ở quá khứ, …»; "
        "the -pi … -pi runs as plain lists (3-01).",
        f"- sadisaṃ with one subject (Yassa yatthakampi sadisaṃ vitthāretabbaṃ): «{LIKEWISE}» (3-02 «giống nhau» "
        "needs two things compared).",
        "- vitthāritā «đã được trình bày chi tiết» (no entry; from pi-5 vitthāretabbaṃ); Yathā … evaṃ … "
        "vitthāretabbā = rails 4's «(Như …, … cũng nên được trình bày chi tiết như vậy)».",
        "- [paccaniyampi (sī. syā. ka.)]: treated as a form variant «[dị bản (Sī., Syā., Ka.): paccaniyampi]».",
        "",
        "## Slips (rendered as meant or kept; reported)",
        "",
        "- ^6-3-131 «… na nirujjhatī ti…pe…»: «ti» written apart; read «nirujjhatīti». The question has no «?»: it "
        "keeps «không» and ends «…».",
        "- ^6-3-151 «rūpāyatanaṃ …pe…»: stray space before the cut; dropped.",
        "- ^6-3-148 «… manāyatanaṃ na nirujjhissati, parinibbantānaṃ asaññasattānaṃ …»: the Pāli joins two answers "
        "with a comma (the parallels have «.»); the comma is kept and the second answer starts with «ở».",
        "- ^6-3-125 «… nirujjhatīti…pe… ghānāyatanaṃ… … dhammāyatanaṃ nirujjhatīti?»: the first question is cut "
        "after its -ti, then the list; rendered «… có phải lĩnh vực tai chấm dứt không… lĩnh vực mũi… … lĩnh vực "
        "đối tượng của ý chấm dứt không?».",
        "- ^6-3-124, 130, 137, 146, 155, 161 «Yattha … …pe….»: place sections cut; «Ở nơi nào mà …» (3-01).",
        "- ^6-3-132 the past section is one question with «Āmantā.» and a note for all three vāras: kept.",
        "- ^6-3-138 … ^6-3-141 cut answers give only person heads («Ở chúng sinh trong cõi hình sắc… ở chúng sinh "
        "trong cõi dục lạc…»); ^6-3-141 «(Ka) yassa yattha manāyatanaṃ…pe…?» is cut before its verb.",
        "- ^6-3-148 the (Kha) question ends a line and «Āmantā.» stands on the next line, as in the Pāli.",
        "",
    ]
    return "\n".join(out)


def main():
    S.check_reused()
    B.check_reused()
    A.check_reused()
    check_reused()
    A.check_frames()
    segs = build(CH)
    A2.check_frames()
    A3.check_frames()
    check_frames()
    S.write(CH, segs)
    text = (S.OUT_DIR / CH).read_text(encoding="utf-8")
    ADH_DIR.mkdir(parents=True, exist_ok=True)
    (ADH_DIR / CH).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", ADH_DIR / CH)
    NOTES_MD.write_text(unicodedata.normalize("NFC", notes()), encoding="utf-8", newline="\n")
    print("wrote", NOTES_MD)
    for s in SLIPS_SEEN:
        print("slip:", s)
    for s in JOINS_SEEN:
        print("comma join:", s[:120])


def probe(name=CH):
    for seg in S.segments_of(name):
        for ln in seg:
            try:
                print("OK  ", tr_line(ln))
            except Exception as e:  # noqa: BLE001
                print("FAIL", ln[:200], "\n    ", type(e).__name__, str(e)[:300])


if __name__ == "__main__":
    if sys.argv[1:] == ["probe"]:
        probe()
    else:
        main()
