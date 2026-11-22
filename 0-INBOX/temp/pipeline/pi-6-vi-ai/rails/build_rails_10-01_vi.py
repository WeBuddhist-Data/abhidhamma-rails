"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 10-01 (Indriyayamaka, part 1: paṇṇattivāra) and the INDRIYA module.

Family A (paṇṇattivāra) comes from build_rails_2-01_vi; the «hiểu theo nghĩa …» subjects, the cut handling (…pe…)
and the variant brackets from build_rails_3-01_vi (both imported READ-ONLY; every shared string is produced by their
functions). This file adds what the Indriya chapters need on top of those frames:

  TWENTY_TWO / IND_NAME / IND_CLASS   the twenty-two members (termbase; pi-2 ^2-221 names) and «năng lực»
  INDRIYA (Members)                   2-01 Members for every written form (-ṃ / -ñca / -ti / accusatives)
  IND_SPECIAL                         = 3-01 AY_SPECIAL (Dibbacakkhu paññācakkhu …, Dibbasotaṃ taṇhāsotaṃ)
  UDDESA_PALI / UDDESA_VI             Bāvīsatindriyāni – … «Hai mươi hai năng lực – …» (pi-2)
  yam_both / part_rest_not            Yaṃ sotaṃ indriyaṃ taṃ sotañceva indriyañca. / Avasesaṃ sotaṃ na indriyaṃ.
  self_not                            Itthindriyaṃ na itthī, itthindriyaṃ. (2-01 special_not with a member subject)
  except_is_nc                        M ṭhapetvā avaseso X na Y. (2-01 except_is, no comma where the Pāli has none)
  ind_mulaka                          (Cakkhundriyamūlakaṃ) «(Phần dựa trên năng lực mắt)» (3-01 mulaka_label)
  heading / unit_vi / line_vi / tr_line / build   the line translator (M, fixed, variants, planes are parameters)

Later Indriya chapters (10-02 … 10-13):
    import importlib, sys
    sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai\\rails")
    I = importlib.import_module("build_rails_10-01_vi")
    segs = I.build("10-02-indriyayamaka.md", fixed={...}, variant_kind={...})
A line, unit or word the parsers cannot place raises ValueError (no silent fallback). Importing writes nothing.

usage: python -I -X utf8 -B build_rails_10-01_vi.py
"""
import importlib
import re
import sys
import unicodedata

RAILS_DIR = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\rails"
if RAILS_DIR not in sys.path:
    sys.path.insert(0, RAILS_DIR)
import build_rails_sample_vi as S  # noqa: E402  (READ-ONLY)
B = importlib.import_module("build_rails_2-01_vi")   # READ-ONLY: family A frames (setter)
A = importlib.import_module("build_rails_3-01_vi")   # READ-ONLY: «hiểu theo nghĩa …» subjects, cuts, variants
C = importlib.import_module("build_rails_7-01_vi")   # READ-ONLY: shared connectors (thì …)

cap = S.cap
LABEL = S.LABEL
CH = "10-01-indriyayamaka.md"
N = "10-01"
YAMAKA = "Indriya"
NOTES_MD = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/notes-rails-{N}.md"
ADH_DIR = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/adh-{N}"
SLIPS_SEEN = []

# ===============================================================================================================
# 1. Members (termbase; = pi-2 5-indriyavibhango ^2-221 «Hai mươi hai năng lực – năng lực mắt, …»)
# ===============================================================================================================
IND_CLASS = "năng lực"                    # indriyaṃ / indriyā / indriye (termbase «năng lực»)
# (key, simple word Vietnamese, Pāli forms of the simple word, X-indriya Pāli, X-indriya Vietnamese); uddesa order
TWENTY_TWO = [
    ("cakkhu", "mắt", ["cakkhu", "cakkhuṃ"], "cakkhundriyaṃ", "năng lực mắt"),
    ("sota", "tai", ["sotaṃ"], "sotindriyaṃ", "năng lực tai"),
    ("ghāna", "mũi", ["ghānaṃ"], "ghānindriyaṃ", "năng lực mũi"),
    ("jivhā", "lưỡi", ["jivhā", "jivhaṃ"], "jivhindriyaṃ", "năng lực lưỡi"),
    ("kāya", "thân", ["kāyo", "kāyaṃ"], "kāyindriyaṃ", "năng lực thân"),
    ("mana", "ý", ["mano", "manaṃ"], "manindriyaṃ", "năng lực ý"),
    ("itthī", "người nữ", ["itthī", "itthiṃ"], "itthindriyaṃ", "năng lực nữ tính"),
    ("purisa", "người nam", ["puriso", "purisaṃ"], "purisindriyaṃ", "năng lực nam tính"),
    ("jīvita", "sự sống", ["jīvitaṃ"], "jīvitindriyaṃ", "năng lực sống"),
    ("sukha", "sự dễ chịu", ["sukhaṃ"], "sukhindriyaṃ", "năng lực dễ chịu"),
    # bare dukkhaṃ in the Indriyayamaka = the faculty's sense «sự khó chịu» (user decision; Saccayamaka «khổ đau»)
    ("dukkha", "sự khó chịu", ["dukkhaṃ"], "dukkhindriyaṃ", "năng lực khó chịu"),
    ("somanassa", "niềm vui", ["somanassaṃ"], "somanassindriyaṃ", "năng lực niềm vui"),
    ("domanassa", "nỗi buồn", ["domanassaṃ"], "domanassindriyaṃ", "năng lực nỗi buồn"),
    ("upekkhā", "sự bình thản", ["upekkhā", "upekkhaṃ"], "upekkhindriyaṃ", "năng lực bình thản"),
    ("saddhā", "niềm tin", ["saddhā", "saddhaṃ"], "saddhindriyaṃ", "năng lực niềm tin"),
    # vīriyaṃ: no pi-6 headword; pi-1 ^1-13 «sự tinh tấn» (sibling vīriyindriyaṃ «năng lực tinh tấn»)
    ("vīriya", "sự tinh tấn", ["vīriyaṃ"], "vīriyindriyaṃ", "năng lực tinh tấn"),
    ("sati", "sự tỉnh thức", ["sati", "satiṃ"], "satindriyaṃ", "năng lực tỉnh thức"),
    ("samādhi", "định tâm", ["samādhi", "samādhiṃ"], "samādhindriyaṃ", "năng lực định tâm"),
    ("paññā", "trí tuệ", ["paññā", "paññaṃ"], "paññindriyaṃ", "năng lực trí tuệ"),
    # anaññātaññāssāmīti: the termbase's variant spelling (^6-10-3), same sense
    ("anaññātaññassāmīti", "sự biết được điều chưa từng biết",
     ["anaññātaññassāmīti", "anaññātaññāssāmīti", "anaññātaññassāmītiṃ"],
     "anaññātaññassāmītindriyaṃ", "năng lực biết được điều chưa từng biết"),
    ("añña", "sự hiểu biết trọn vẹn", ["aññaṃ"], "aññindriyaṃ", "năng lực hiểu biết trọn vẹn"),
    ("aññātāvī", "người đã hiểu biết trọn vẹn", ["aññātāvī", "aññātāviṃ"], "aññātāvindriyaṃ",
     "năng lực của người đã hiểu biết trọn vẹn"),
]
IND_NAME = {k: v for k, _, _, _, v in TWENTY_TWO}          # key -> «năng lực X»
IND_PALI = {k: p for k, _, _, p, _ in TWENTY_TWO}          # key -> X-indriyaṃ
IND_SPECIAL = dict(A.AY_SPECIAL)                          # the «hiểu theo nghĩa …» subjects (3-01 / termbase)
CLASS_KEYS = ("indriya", "indriyā")                       # the class words (not a single member)


def _table():
    t = {}
    for key, vi, forms, ip, iv in TWENTY_TWO:
        t[key] = (vi, vi, forms)
        t[key + "-indriya"] = (iv, iv, [ip])
    t["indriya"] = (IND_CLASS, IND_CLASS, ["indriyaṃ"])
    t["indriyā"] = (f"các {IND_CLASS}", IND_CLASS, ["indriyā", "indriye"])   # indriye ca ṭhapetvā (= khandhe ca)
    return t


INDRIYA = B.Members(_table(), special=IND_SPECIAL)
IND_FORMS = set(INDRIYA.form)

# Bāvīsatindriyāni – … (pi-2 ^2-219 / ^2-221 «Hai mươi hai năng lực –»; this book's order)
UDDESA_HEAD = "Hai mươi hai năng lực –"
UDDESA_PALI = ("Bāvīsatindriyāni – " + ", ".join(p if k != "vīriya" else p + " ⟦0⟧" for k, p in IND_PALI.items())
               + ".")
UDDESA_VI_PLAIN = f"{UDDESA_HEAD} " + ", ".join(IND_NAME.values()) + "."   # = pi-2 ^2-221 (asserted)
UDDESA_VI = f"{UDDESA_HEAD} " + ", ".join(v if k != "vīriya" else v + " ⟦0⟧" for k, v in IND_NAME.items()) + "."

# ===============================================================================================================
# 2. Frames new in this yamaka (built from 2-01 / 3-01 strings)
# ===============================================================================================================
PART = "Phần"                             # Avasesaṃ sotaṃ «Phần tai còn lại» (user decision 2026-11-22)
REST_WORD = "còn lại"                     # avasesa- (termbase «còn lại»; = 2-01 rest_not_is)
WHICH, THAT = "nào", "ấy"                 # Yaṃ … taṃ (relative / correlative, as 8 «Tâm nào …, thì … tâm ấy»)


# Members that are body parts take «Phần …» in the Avasesa- / Yaṃ … taṃ frames (user decision for tai, «Phần tai còn
# lại»: a bare «Tai còn lại» reads as "the other ear"; coordinator: likewise thân; not for sự bình thản …).
PART_KEYS = frozenset({"cakkhu", "sota", "ghāna", "jivhā", "kāya"})


def is_part(key):
    """True if the member (INDRIYA key) is a body part, i.e. takes the «Phần …» prefix."""
    return key in PART_KEYS


def part_rest_not(x, y, part=True):
    """Avasesaṃ sotaṃ na indriyaṃ. / Avaseso kāyo na indriyā. → «Phần tai còn lại không phải là năng lực.»
    (a single member, not the class word: the class keeps 2-01 rest_not_is «Các năng lực còn lại …»).
    part=False (not a body part, e.g. upekkhā): plain 2-01 rest_not_is «Sự bình thản còn lại không phải là năng lực.»
    (coordinator 2026-11-22)."""
    if not part:
        return B.rest_not_is(x, y)
    s = B.rest_not_is(f"{PART.lower()} {x}", y)
    assert s.startswith(f"{PART} {x} {REST_WORD} không phải là "), s
    return s


def yam_both(x, y, part=True):
    """Yaṃ sotaṃ indriyaṃ taṃ sotañceva indriyañca. → «Phần tai nào là năng lực, thì phần tai ấy vừa là tai vừa là
    năng lực.» (the part named as in «Phần tai còn lại»; tail = 2-01 both_is). part=False: «Sự bình thản nào là năng
    lực, thì sự bình thản ấy vừa là sự bình thản vừa là năng lực.»"""
    head = f"{PART.lower()} {x}" if part else x
    tail = B.both_is(f"{head} {THAT}", x, y)
    assert tail.startswith(f"{cap(head)} {THAT} vừa là "), tail
    return f"{cap(head)} {WHICH} là {y}, {C.THEN} {head}{tail[len(head):]}"


def self_not(m, y):
    """Itthindriyaṃ na itthī, itthindriyaṃ. → «Năng lực nữ tính thì không phải là người nữ, mà là năng lực nữ tính.»
    (2-01 special_not with the member itself as subject)."""
    return B.special_not(m, y, m)


def except_is_nc(m, x, y):
    """M ṭhapetvā avaseso X na Y. (no comma in the Pāli, ^6-10-100) = 2-01 except_is without its comma."""
    s = B.except_is(m, x, y)
    k = f"{x}, nhưng "
    assert s.count(k) == 1, s
    return s.replace(k, f"{x} nhưng ")


def ind_mulaka(text, M=None):
    """(Cakkhundriyamūlakaṃ)(.) → «(Phần dựa trên năng lực mắt)(.)» (3-01 mulaka_label; termbase); None if not one."""
    M = M or INDRIYA
    m = re.fullmatch(r"\((\w+?)mūlakaṃ\)(\.?)", text)
    if not m or not m.group(1).endswith("ndriya"):
        return None
    return A.mulaka_label(M.subj(m.group(1).lower() + "ṃ"), m.group(2))


YAM_RE = re.compile(r"(Yaṃ|Yo|Yā) (\S+) (\S+) (taṃ|so|sā) (\S+?)(ñceva| ceva) (\S+?)(ñca| ca)\.")
PART_RE = re.compile(r"(Avasesaṃ|Avaseso|Avasesā) (\S+) na (\S+)\.")
SELF_RE = re.compile(r"(\S+) na (\S+), (\S+)\.")
EXC_NC_RE = re.compile(r"([^\s,]+) ṭhapetvā (?:avaseso|avasesā|avasesaṃ) ([^\s,]+) na ([^\s,]+)\.")


def ind_sentence(s, M):
    """This yamaka's own sentence frames; None if the sentence is not one of them (then 3-01 / 2-01 apply)."""
    if m := YAM_RE.fullmatch(s):
        x1, y1, x2 = m.group(2), m.group(3), m.group(5) + ("ñceva" if m.group(6) == "ñceva" else "")
        y2 = m.group(7) + ("ñca" if m.group(8) == "ñca" else "")
        if not (M.key(x1) == M.key(x2) and M.key(y1) == M.key(y2)):
            raise ValueError(f"Yaṃ … taṃ with different members {s!r}")
        return yam_both(M.subj(x1), M.pred(y1), is_part(M.key(x1)))
    if (m := PART_RE.fullmatch(s)) and M.key(m.group(2)) not in CLASS_KEYS:
        return part_rest_not(M.subj(m.group(2)), M.pred(m.group(3)), is_part(M.key(m.group(2))))
    if (m := SELF_RE.fullmatch(s)) and m.group(1).lower() in M.form and m.group(3).lower() in M.form:
        if M.key(m.group(1)) != M.key(m.group(3)):
            raise ValueError(f"X na Y, Z with Z ≠ X {s!r}")
        return self_not(M.subj(m.group(1)), M.pred(m.group(2)))
    if (m := EXC_NC_RE.fullmatch(s)) and M.key(m.group(2)) not in CLASS_KEYS:
        return except_is_nc(M.subj(m.group(1)), M.pred(m.group(2)), M.pred(m.group(3)))
    return None


# ===============================================================================================================
# 3. Units and lines (3-01 unit_vi / line_vi with this yamaka's frames tried first)
# ===============================================================================================================
def unit_vi(u, M=None, planes=None):
    M = M or INDRIYA
    lower = u[:1].islower()
    p = cap(u) if lower else u
    out = None
    if (lab := ind_mulaka(p, M)) is not None:
        out = lab
    elif p.endswith("."):
        out = ind_sentence(p, M)
    if out is None:
        return A.unit_vi(u, M, planes)
    if lower and not out.startswith("("):
        out = out[:1].lower() + out[1:]
    return out


def units_vi(piece, M=None, planes=None):
    units = [x for x in re.split(r"(?<=[.?]) (?=\S)", piece.strip()) if x]
    return " ".join(unit_vi(x, M, planes) for x in units)


def line_vi(body, M=None, planes=None):
    """3-01 line_vi (pieces between …pe… cuts; the «.» on both sides of a cut is absorbed) over this file's units."""
    out, pos = "", 0
    for m in A.CUT_RE.finditer(body):
        piece = body[pos:m.start()]
        if piece.strip():
            if out:
                out += " " if piece.startswith(" ") else ""
            out += units_vi(piece, M, planes)
        if out.endswith("."):
            out = out[:-1]
        out += (" " if m.group(1) else "") + "…"
        pos = m.end()
    piece = body[pos:]
    if piece.strip():
        if out:
            out += " " if piece.startswith(" ") else ""
        out += units_vi(piece, M, planes)
    return out


def heading(text, yamaka=YAMAKA):
    """2-01 heading(); Suddhindriya… (sandhi Suddha + indriya, which 2-01's 'Suddha<X>' pattern does not see) goes to
    2-01's suddha_varo / suddha_mulacakka_varo (termbase Suddhindriyavāro «mục về các năng lực thuần túy»)."""
    if text == "Suddhindriyavāro":
        return B.suddha_varo(IND_CLASS)
    if text == "Suddhindriyamūlacakkavāro":
        return B.suddha_mulacakka_varo(IND_CLASS)
    return B.heading(text, IND_CLASS, yamaka)


SLIPS = {}   # plain slips rendered as meant: none needed here (the long-ā spelling is a termbase form)


def tr_line(p, M=None, fixed=None, variant_kind=None, planes=None, yamaka=YAMAKA):
    M = M or INDRIYA
    m = re.search(r" (\^\S+)$", p)
    bid = m.group(1) if m else None
    body = p[:m.start()] if m else p
    fixed = fixed or {}
    brs = re.findall(r"\[[^\]]*\]", body)
    for k, br in enumerate(brs):
        body = body.replace(br, f"⟦{k}⟧", 1)
    if body.startswith("#"):
        hashes, text = body.split(" ", 1)
        out = f"{hashes} {heading(text, yamaka)}"
    elif body in fixed:
        out = fixed[body]
    else:
        for bad, good in SLIPS.items():
            if bad in body:
                SLIPS_SEEN.append((bid, bad, good))
                body = body.replace(bad, good)
        out = line_vi(body, M, planes)
    for k, br in enumerate(brs):
        if br not in (variant_kind or {}):
            raise ValueError(f"undeclared variant {br!r}")
        if f"⟦{k}⟧" not in out:
            raise ValueError(f"variant {br!r} lost in {p!r}")
        out = out.replace(f"⟦{k}⟧", A.var_vi(br, variant_kind[br]))
    if "⟦" in out:
        raise ValueError(f"unplaced variant in {p!r}")
    return f"{out} {bid}" if bid else out


def build(name, M=None, fixed=None, variant_kind=None, planes=None, yamaka=YAMAKA):
    return [[tr_line(ln, M, fixed, variant_kind, planes, yamaka) for ln in seg] for seg in S.segments_of(name)]


# ===============================================================================================================
# 4. This chapter
# ===============================================================================================================
FIXED_10_01 = {UDDESA_PALI: UDDESA_VI}
VARIANTS_10_01 = {
    "[viriyindiyaṃ (sī. syā.)]": "spelling",      # pi-2 ^2-219 [viriyindriyaṃ (sī. syā.)] «khác chính tả»
    "[avasesā kāyo (sī. syā. ka.)]": "form",      # avaseso / avasesā (3-01 [avaseso (syā.)] «dị bản»)
}

REUSED = [   # (Pāli, Vietnamese, book): asserted to occur in that book's Vietnamese rails
    ("Bāvīsatindriyāni – cakkhundriyaṃ, … aññātāvindriyaṃ. (^2-2)", UDDESA_VI_PLAIN, "2"),
    ("vīriyindriyaṃ [viriyindriyaṃ (sī. syā.)] (^2-219)", "năng lực tinh tấn [khác chính tả (Sī., Syā.): viriyindriyaṃ]",
     "2"),
    ("vīriyaṃ (^1-13)", "sự tinh tấn", "1"),
    ("dibbacakkhu", "thiên nhãn", "5"), ("paññācakkhu", "mắt trí tuệ", "5"), ("dibbasotaṃ", "thiên nhĩ", "5"),
]


def check_reused():
    texts = {b: unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md"))))
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED if unicodedata.normalize("NFC", v).lower() not in texts[b].lower()]
    assert not bad, "reused strings not found in their rails: " + repr(bad)


def check_frames():
    """Shared strings must be the setters': the new frames are built from 2-01 functions; cut handling = 3-01."""
    assert yam_both("tai", "năng lực").endswith(B.both_is("phần tai ấy", "tai", "năng lực")[1:])
    assert yam_both("tai", "năng lực") == "Phần tai nào là năng lực, thì phần tai ấy vừa là tai vừa là năng lực."
    assert part_rest_not("sự bình thản", "năng lực", False) == "Sự bình thản còn lại không phải là năng lực."
    assert part_rest_not("x", "y", False) == B.rest_not_is("x", "y")
    assert (yam_both("sự bình thản", "năng lực", False) ==
            "Sự bình thản nào là năng lực, thì sự bình thản ấy vừa là sự bình thản vừa là năng lực.")
    assert is_part("sota") and is_part("kāya") and not is_part("upekkhā")
    assert part_rest_not("tai", "năng lực") == "Phần tai còn lại không phải là năng lực."   # user decision, verbatim
    assert self_not("năng lực nữ tính", "người nữ") == B.special_not("năng lực nữ tính", "người nữ", "năng lực nữ tính")
    assert except_is_nc("a", "x", "y").replace("x nhưng", "x, nhưng") == B.except_is("a", "x", "y")
    for t in ("Āyatanā ghānāyatananti…pe… āyatanā dhammāyatananti?",
              "Yattha cakkhāyatanaṃ nuppajjittha…pe….",
              "Cakkhāyatanaṃ cakkhu ceva cakkhāyatanañca…pe…."):
        assert line_vi(t, A.AYATANA) == A.line_vi(t, A.AYATANA), t       # same cut handling as 3-01
    assert heading("Indriyayamakaṃ") == S.yamaka_title("Indriya")
    assert ind_mulaka("(Cakkhundriyamūlakaṃ)") == "(Phần dựa trên năng lực mắt)"


# ===============================================================================================================
# 5. Notes file (Pāli = tiếng Việt)
# ===============================================================================================================
def notes():
    M = INDRIYA
    out = []

    def row(p, v):
        out.append(f"{p} = {v}")

    def h(t):
        out.extend(["", f"## {t}", ""])

    out += [f"# pi-6 rails {N} (Indriyayamaka 1): the Indriya module on top of family A (rails 2-01, 3-01)", "",
            "Builder: build_rails_10-01_vi.py (import with importlib). Family A strings come from build_rails_2-01_vi "
            "(name_q, name_q_neg, both_is, rest_not_is, special_is / special_not, except_*, heading, CLOSING, SHORT); "
            "the «hiểu theo nghĩa …» subjects, the …pe… cuts and the variant brackets from build_rails_3-01_vi "
            "(AY_SPECIAL, unit_vi, line_vi logic, var_vi). Exposed for 10-02 … 10-13: `TWENTY_TWO`, `IND_NAME`, "
            "`IND_PALI`, `IND_CLASS`, `IND_SPECIAL`, `INDRIYA` (Members), `IND_FORMS`, `UDDESA_PALI`, `UDDESA_VI`, "
            "`PART`, `PART_KEYS`, `is_part`, `part_rest_not`, `yam_both`, `self_not`, `except_is_nc`, `ind_mulaka`, `ind_sentence`, "
            "`unit_vi`, `units_vi`, `line_vi`, `heading`, `tr_line`, `build`. Family B (pavattivāra) for 10-02 …: "
            "2-01 b_q / b_noca / b_both with M=INDRIYA (3-01 answer_head for attribute heads). Format: Pāli = tiếng Việt.",
            ""]
    h("Members (termbase; pi-2 ^2-221 names)")
    for k, vi, forms, ip, iv in TWENTY_TWO:
        row(f"{' / '.join(forms)} ; {ip}", f"{vi} ; {iv}")
    row("indriyaṃ ; indriyā / indriye", f"{IND_CLASS} ; các {IND_CLASS} (predicate: {IND_CLASS})")
    row("Bāvīsatindriyāni – … (uddesa, ^6-10-1)", UDDESA_VI.replace("⟦0⟧", "[khác chính tả (Sī., Syā.): viriyindiyaṃ]"))
    h("Headings")
    for t in ("Indriyayamakaṃ", "Suddhindriyavāro", "Suddhindriyamūlacakkavāro"):
        row(t, heading(t))
    h("Family A in this yamaka (2-01 frames)")
    for s in ("(Ka) cakkhu cakkhundriyaṃ?", "(Kha) indriyā sotindriyaṃ?", "(Ka) na cakkhu na cakkhundriyaṃ?",
              "(Kha) na indriyā na sotindriyaṃ?", "(Ka) cakkhu indriyaṃ?", "(Kha) indriyā cakkhu?",
              "(Ka) dukkhaṃ dukkhindriyaṃ?", "(Ka) itthī itthindriyanti?",
              "(Ka) anaññātaññassāmīti anaññātaññassāmītindriyaṃ?", "(Kha) aññātāvindriyaṃ aññātāvī?",
              "Anaññātaññassāmīti anaññātaññassāmītindriyaṃ?"):
        row(s, unit_vi(s))
    for s in ("Dibbacakkhu paññācakkhu cakkhu, na cakkhundriyaṃ.", "Cakkhundriyaṃ cakkhu ceva cakkhundriyañca.",
              "Dibbasotaṃ taṇhāsotaṃ sotaṃ, na sotindriyaṃ.", "Sotindriyaṃ sotañceva sotindriyañca.",
              "Kāyindriyaṃ ṭhapetvā avaseso kāyo ⟦0⟧, na kāyindriyaṃ.",
              "Upekkhindriyaṃ ṭhapetvā avasesā upekkhā, na upekkhindriyaṃ.",
              "Upekkhindriyaṃ upekkhā ceva upekkhindriyañca.",
              "Dibbacakkhu paññācakkhu na cakkhundriyaṃ, cakkhu.",
              "Cakkhuñca cakkhundriyañca ṭhapetvā avasesā na ceva cakkhu na ca cakkhundriyaṃ.",
              "Kāyindriyaṃ ṭhapetvā avaseso na kāyindriyaṃ, kāyo.",
              "Kāyañca kāyindriyañca ṭhapetvā avaseso na ceva kāyo na ca kāyindriyaṃ.",
              "Sotindriyaṃ indriyañceva sotindriyañca.", "Avasesā indriyā na sotindriyaṃ.",
              "Cakkhuṃ ṭhapetvā avasesā indriyā na cakkhu, indriyā.",
              "Cakkhuñca indriye ca ṭhapetvā avasesā na ceva cakkhu na ca indriyā."):
        row(s.replace("⟦0⟧", "[v]"), unit_vi(s).replace("⟦0⟧", "[v]"))
    h("New frames (this yamaka; built from 2-01 strings)")
    for s in ("Itthindriyaṃ na itthī, itthindriyaṃ.", "Itthī na itthindriyaṃ, itthī.",
              "Purisindriyaṃ na puriso, purisindriyaṃ.",
              "Yaṃ sotaṃ indriyaṃ taṃ sotañceva indriyañca.", "Avasesaṃ sotaṃ na indriyaṃ.",
              "Yo kāyo indriyaṃ so kāyo ceva indriyañca.", "Avaseso kāyo na indriyā.",
              "Yā upekkhā indriyaṃ sā upekkhā ceva indriyañca.", "Avasesā upekkhā na indriyaṃ.",
              "Kāyindriyaṃ ṭhapetvā avaseso kāyo na kāyindriyaṃ."):
        row(s, unit_vi(s))
    row("X na Y, X. (member subject)", self_not("<X>", "<Y>"))
    row("Yaṃ / Yo / Yā X Y taṃ / so / sā Xñceva Yñca.", yam_both("<X>", "<Y>"))
    row("Avasesaṃ / Avaseso / Avasesā X na Y. (X a body part: PART_KEYS cakkhu, sota, ghāna, jivhā, kāya)",
        part_rest_not("<X>", "<Y>") + "  (X not a body part: " + part_rest_not("<X>", "<Y>", False) +
        "; X the class word indriyā: 2-01 «Các năng lực còn lại không phải là Y.»)")
    row("Yaṃ / Yo / Yā X Y taṃ … (X not a body part)", yam_both("<X>", "<Y>", False))
    row("(Xindriyamūlakaṃ) (for 10-02 …)", ind_mulaka("(Cakkhundriyamūlakaṃ)"))
    h("Cuts (3-01 handling)")
    for t in ("Sotaṃ sotindriyaṃ? Indriyā cakkhundriyaṃ?…Pe….",
              "Puriso purisindriyaṃ? Indriyā cakkhundriyaṃ? …Pe….",
              "(Kha) na indriyā na cakkhundriyaṃ? …Pe… na indriyā na aññātāvindriyaṃ?",
              "(Kha) indriyā cakkhu? …Pe… indriyā aññātāvī?",
              "Cakkhundriyaṃ indriyañceva cakkhundriyañca. Avasesā indriyā na cakkhundriyaṃ…pe….",
              "Sukhaṃ sukhindriyanti? Āmantā …pe….",
              "(Kha) na indriyā na cakkhundriyanti? Āmantā …pe…."):
        row(t, line_vi(t))
    h("Termbase misfits and gaps (for the coordinator)")
    out += [
        "- vīriyaṃ (bare word): no pi-6 headword; pi-1 ^1-13 «sự tinh tấn» (sibling vīriyindriyaṃ «năng lực tinh tấn»).",
        "- dukkhaṃ / dukkhanti / Dukkhaṃ (ṭhapetvā) / Dukkhañca: the termbase's second sense «sự khó chịu» (the faculty; "
        "user decision: bare dukkhaṃ follows its yamaka).",
        "- Avasesaṃ sotaṃ «Phần tai còn lại» (user decision), likewise Avaseso kāyo «Phần thân còn lại»: «Phần» is a "
        "property of the member (PART_KEYS / is_part: body parts only; coordinator 2026-11-22). Not a body part: "
        "Avasesā upekkhā na indriyaṃ «Sự bình thản còn lại không phải là năng lực.», Yā upekkhā … «Sự bình thản nào là "
        "năng lực, thì sự bình thản ấy vừa là sự bình thản vừa là năng lực.».",
        "- Yaṃ sotaṃ indriyaṃ taṃ … (no termbase entry): «Phần tai nào là năng lực, thì phần tai ấy vừa là tai vừa là năng "
        "lực.»: «Phần» added to match the approved «Phần tai còn lại» of the next sentence (a bare «Tai nào …» invites the "
        "same 'which ear' reading the user avoided); «nào … ấy» as 8's «Tâm nào …, thì … tâm ấy». Please confirm.",
        "- Itthindriyaṃ na itthī, itthindriyaṃ. (member subject in 2-01's special_not frame): «Năng lực nữ tính thì "
        "không phải là người nữ, mà là năng lực nữ tính.».",
        "- indriye (ca ṭhapetvā) «các năng lực» (= 2-01 khandhe ca «các khối»); indriyā as predicate «năng lực».",
        "",
        "## Slips and unsure Pāli (translated as written or as plainly meant)",
        "",
        "- ^6-10-1 variant «[viriyindiyaṃ (sī. syā.)]» (pi-2 ^2-219 has viriyindriyaṃ): kept as written, a spelling "
        "variant «[khác chính tả (Sī., Syā.): viriyindiyaṃ]».",
        "- ^6-10-3 «na anaññātaññāssāmīti» (long ā; the termbase's variant spelling): same Vietnamese.",
        "- ^6-10-100 «Kāyindriyaṃ ṭhapetvā avaseso kāyo na kāyindriyaṃ.» (no comma; the repeat in the same segment has "
        "one): no comma in the Vietnamese either (sample rule «no comma where the Pāli has none»).",
        "- ^6-10-140 the second question «(Ka) indriyā domanassindriyanti?» is labelled «(Ka)» (for «(Kha)»): label kept "
        "«(a)» (as 2-01 ^6-2-61, 3-01 ^6-3-50).",
        "- ^6-10-140 «Avaseso kāyo na indriyā.» (plural indriyā, the parallels have indriyaṃ): same Vietnamese «năng lực».",
        "- ^6-10-140 «(Ka) cakkhu indriyanti? Āmantā.» while sotaṃ / kāyo / upekkhā get partial answers: as written.",
        "- «… ? …Pe….» / «… ? …Pe….» with and without the space before the cut: the space is kept («không? …» / «không?…»).",
        "",
    ]
    return "\n".join(out)


def main():
    S.check_reused()
    B.check_reused()
    A.check_reused()
    check_reused()
    check_frames()
    segs = build(CH, fixed=FIXED_10_01, variant_kind=VARIANTS_10_01)
    S.write(CH, segs)
    text = (S.OUT_DIR / CH).read_text(encoding="utf-8")
    ADH_DIR.mkdir(parents=True, exist_ok=True)
    (ADH_DIR / CH).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", ADH_DIR / CH)
    NOTES_MD.write_text(unicodedata.normalize("NFC", notes()), encoding="utf-8", newline="\n")
    print("wrote", NOTES_MD)
    for s in SLIPS_SEEN:
        print("slip:", s)


if __name__ == "__main__":
    main()
