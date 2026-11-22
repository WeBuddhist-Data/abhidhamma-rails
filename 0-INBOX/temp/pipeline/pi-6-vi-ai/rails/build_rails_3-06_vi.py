"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 3-06 (Āyatanayamaka, part 6: uppādanirodhavāra future, present-past,
present-future and past-future; the pariññāvāra; end of the Āyatanayamaka).

Everything comes from the Āyatana chain build_rails_3-05_vi → build_rails_3-04_vi → build_rails_3-03_vi →
build_rails_3-02_vi → build_rails_3-01_vi → build_rails_2-01_vi / build_rails_7-01_vi / build_rails_4_vi, and from
build_rails_2-02_vi (family E, pariññāvāra; headings and closing lines), all imported READ-ONLY. New here:

  YE_TAIL_RE / ye_tail_head / ye_tail_sentence
                              a bare "Ye … parinibbāyissanti tesaṃ cavantānaṃ [/ upapajjantānaṃ] tesaṃ …" head (no
                              person group before "ye"): 3-02's Ye head + 2-02 / 3-03's tail «Những người nào sau khi
                              tái sinh vào cõi hình sắc sẽ nhập Niết-bàn trọn vẹn, khi những người ấy đang chết đi, thì
                              ở những người ấy …» (2-01 b_noca / b_both unchanged)
  member_fragment             an answer cut right after its first member ("<persons> tesaṃ tattha manāyatanaṃ…pe…")
                              «Ở …, thì ở những người ấy, ở nơi ấy lĩnh vực ý…» (= 5-03 cut_answer shape)
  noca_cut                    an answer cut right after "no ca tesaṃ [tattha]" «…, nhưng ở những người ấy[, ở nơi ấy]…»
  mixed_line                  a line of such pieces and 3-05 loc_fragment pieces, optionally ending in a whole answer
                              with a lower-case head («… ở những người có mắt đang tái sinh, thì …»)
  NOTES_3_06                  the two editorial notes (Yathā uppādavāre paccuppannātītā …, Yathā nirodhavāre …)
  FIXED_3_06                  Uppādanirodhavāro. / Pariññāvāro. / Āyatanayamakaṃ niṭṭhitaṃ. / Namo tassa …
  heading / sentence_vi / unit_vi / line_vi / tr_line / build   3-05's chain + 2-02's family E (D.e_line)
A line, unit or word the parsers cannot place raises ValueError (no silent fallback). Importing writes nothing.

usage: python -I -X utf8 -B build_rails_3-06_vi.py   (probe: … build_rails_3-06_vi.py probe)
"""
import importlib
import re
import sys
import unicodedata

RAILS_DIR = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\rails"
if RAILS_DIR not in sys.path:
    sys.path.insert(0, RAILS_DIR)
import build_rails_sample_vi as S  # noqa: E402  (READ-ONLY)
A5 = importlib.import_module("build_rails_3-05_vi")  # READ-ONLY: 3-05 chain (cut questions, fragments, notes)
A4 = A5.A4                                            # build_rails_3-04_vi (READ-ONLY)
A3 = A5.A3                                            # build_rails_3-03_vi (READ-ONLY)
A2 = A5.A2                                            # build_rails_3-02_vi (READ-ONLY)
A = A5.A                                              # build_rails_3-01_vi (READ-ONLY)
B = A5.B                                              # build_rails_2-01_vi (READ-ONLY)
C = A5.C                                              # build_rails_7-01_vi (READ-ONLY)
G = A5.G                                              # build_rails_4_vi (READ-ONLY)
D = importlib.import_module("build_rails_2-02_vi")   # READ-ONLY: family E (pariññāvāra), headings, closings
assert D is A5.D

cap = S.cap
CH = "3-06-ayatanayamaka.md"
N = "3-06"
NOTES_MD = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/notes-rails-{N}.md"
ADH_DIR = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/adh-{N}"
SLIPS_SEEN = []
NEW_SEEN = {"ye_tail": [], "member_fragment": [], "noca_cut": [], "mixed": []}
PLANES = A.PLANES_AY
M_AY = A.AYATANA
PE = S.PE


def _decap(s):
    return s[:1].lower() + s[1:]


# ===============================================================================================================
# 1. A bare "Ye … parinibbāyissanti tesaṃ cavantānaṃ" head (3-02 Ye head + 3-03 / 2-02 tail)
# ===============================================================================================================
YE_TAIL_RE = re.compile(r"(Ye .+? parinibbāyissanti) tesaṃ (upapajjantānaṃ|cavantānaṃ) " + A.LOC + r" (.+)\.")


def ye_tail_head(core, tail, planes=None):
    """'Ye <plane> upapajjitvā parinibbāyissanti' + 'tesaṃ cavantānaṃ' → «Những người nào sau khi tái sinh vào … sẽ
    nhập Niết-bàn trọn vẹn, khi những người ấy đang chết đi» (= 3-02 answer_head of the Ye head + 3-03 YE_TAILS)."""
    planes = planes or PLANES
    out = f"{A2.answer_head(core, 'tesaṃ', planes)}, {A3.YE_TAILS[' tesaṃ ' + tail]}"
    assert out.startswith(B.ye_clause(core, planes) + ", khi "), out
    return out


def ye_tail_sentence(s, M=None, planes=None):
    """'Ye … parinibbāyissanti tesaṃ cavantānaṃ tesaṃ A V, no ca tesaṃ B W.' / '… tesaṃ A-ñca V B-ñca W.' →
    2-01 b_noca / b_both with ye_tail_head. None if not this head."""
    M = M or M_AY
    m = YE_TAIL_RE.fullmatch(s)
    if not m:
        return None
    core, tail, loc, rest = m.groups()
    head_vi = ye_tail_head(core, tail, planes)
    if f", no ca {loc} " in rest:
        c1, c2 = rest.split(f", no ca {loc} ")
        a, v1 = A.split_mv(c1, M)
        b, v2 = A.split_mv(c2, M)
        out = B.b_noca(head_vi, loc, a, v1, b, v2)
    elif mm := A4.BOTH_RE.fullmatch(rest):
        c1, v1, c2, v2 = mm.groups()
        out = B.b_both(head_vi, loc, M.subj(c1), B.verb(v1), M.subj(c2), B.verb(v2))
    else:
        raise ValueError(f"unknown answer after a Ye-tail head: {s!r}")
    NEW_SEEN["ye_tail"].append(s)
    return out


# ===============================================================================================================
# 2. Answers cut by …pe… after the first member, or after "no ca tesaṃ [tattha]"
# ===============================================================================================================
MEMBER_FRAG_RE = re.compile(r"(.+?) " + A.LOC + r" (\S+)")
NOCA_CUT_RE = re.compile(r"(.+), no ca " + A.LOC)


def member_fragment(piece, M=None, planes=None):
    """'<persons> tesaṃ [tattha] A' → «Ở <persons>, thì ở những người ấy[, ở nơi ấy] A» (3-05 loc_fragment + the
    member; = 5-03 cut_answer). Asserted to be the head of the full answer. None if not this shape."""
    M = M or M_AY
    m = MEMBER_FRAG_RE.fullmatch(piece)
    if not m:
        return None
    head, loc, mem = m.groups()
    try:
        M.subj(mem)
    except ValueError:
        return None
    lf = A5.loc_fragment(f"{head} {loc}", planes)
    if lf is None:
        return None
    out = f"{lf} {M.subj(mem)}"
    other = "dhammāyatanaṃ" if mem != "dhammāyatanaṃ" else "rūpāyatanaṃ"
    probe = f"{piece} nirujjhissati, no ca {loc} {other} uppajjati."
    assert A5.sentence_vi(probe, M, planes).startswith(out + " "), (piece, out)
    NEW_SEEN["member_fragment"].append(piece)
    return out


def noca_cut(piece, M=None, planes=None):
    """'<head> <loc> A V, no ca <loc>' → the whole 2-01 b_noca answer cut after its «, nhưng <loc>»:
    «Ở …, thì ở những người ấy, ở nơi ấy A V, nhưng ở những người ấy, ở nơi ấy». None if not this shape."""
    M = M or M_AY
    m = NOCA_CUT_RE.fullmatch(piece)
    if not m:
        return None
    first, loc = m.groups()
    other = "dhammāyatanaṃ" if "dhammāyatanaṃ" not in first else "rūpāyatanaṃ"
    probe = f"{piece} {other} nirujjhissati."
    try:
        full = A5.sentence_vi(probe, M, planes)
    except ValueError:
        return None
    mark = f", {C.BUT} {B.L[loc]} "
    if full.count(mark) != 1:
        raise ValueError(f"no single «{mark.strip()}» in {full!r}")
    NEW_SEEN["noca_cut"].append(piece)
    return full[: full.index(mark) + len(mark) - 1]


def piece_vi(p, M=None, planes=None):
    """One piece between …pe… cuts: a fragment (3-05 loc_fragment, member_fragment, noca_cut) or, as the last piece,
    a whole answer. A lower-case Pāli head keeps a lower-case «ở». Raises if nothing places it."""
    M = M or M_AY
    units = [x for x in re.split(r"(?<=[.?]) (?=\S)", p) if x]
    if len(units) > 1:                                       # '<answer>. (Ghānāyatanamūlakaṃ)': label units after it
        return " ".join([piece_vi(units[0], M, planes)] + [unit_vi(x, M, planes) for x in units[1:]])
    lower = p[:1].islower()
    q = cap(p) if lower else p
    if q.endswith("."):
        out = sentence_vi(q, M, planes)
    else:
        out = A5.loc_fragment(q, planes)
        if out is None:
            out = member_fragment(q, M, planes)
        if out is None:
            out = noca_cut(q, M, planes)
    if out is None:
        raise ValueError(f"cut piece not placed: {p!r}")
    return _decap(out) if lower else out


def mixed_line(body, M=None, planes=None):
    """'P1…pe… P2…pe…[.]' / 'P1…pe… <whole answer>.' → the pieces joined with «…» at the same spots (a final
    "…pe…." absorbs its «.»; the Pāli's space after each cut kept)."""
    M = M or M_AY
    parts = body.split("…pe…")
    if len(parts) < 2:
        return None
    out = ""
    for k, p in enumerate(parts):
        last = k == len(parts) - 1
        if last and p in ("", "."):
            break
        if p.startswith(" "):
            out += " "
        elif k:
            raise ValueError(f"no space after a cut in {body!r}")
        if p.strip() != p.lstrip() and not last:
            raise ValueError(f"space before a cut in {body!r}")
        out += piece_vi(p.strip(), M, planes)
        if not last:
            out += PE
    NEW_SEEN["mixed"].append(body)
    return out


# ===============================================================================================================
# 3. Editorial notes, closings, headings
# ===============================================================================================================
P_PERSON, P_PLACE, P_PERSON_PLACE = A4.P_PERSON, A4.P_PLACE, A4.P_PERSON_PLACE
PUCCHA = A4.PUCCHA                                    # pucchā «câu hỏi» (3-04)
ANU_PACC = f"theo {A4.ANULOMA} và {A4.PACCANIKA}"     # anulomampi paccanīkampi (3-04 / 3-05 notes)
VIBHATTA = "như đã được phân tích trong"             # yathā … vibhattā / vibhattaṃ (pi-2; 2-02 YATHA_IDHA)
VIBHAJITABBA = "cũng nên phân tích như vậy"          # evaṃ … vibhajitabbā (pi-2; 2-02 YATHA_IDHA)
assert f"{VIBHATTA} {B.UPPADAVARO}, ở đây {VIBHAJITABBA}" in D.YATHA_IDHA
THREE_PARTS = f"ở cả {P_PERSON}, {P_PLACE} lẫn {P_PERSON_PLACE}"   # yassakampi yatthakampi yassayatthakampi (5-02)
PACC_ATITA_PUCCHA = f"{PUCCHA} về {B.TIME['Paccuppannātīta']}"     # paccuppannātītā pucchā
ATITANAGATA_PUCCHA = f"{PUCCHA} về {B.TIME['Atītānāgata']}"        # atītānāgatā pucchā
AT_UPPADANIRODHE = f"{C.AT} {A4.UPPADANIRODHE}"                     # uppādanirodhepi «ở sự sinh khởi và sự chấm dứt»

NOTES_3_06 = {   # Pāli (variant brackets protected as ⟦k⟧) → Vietnamese
    "(Yathā uppādavāre paccuppannātītā pucchā vibhattā evaṃ uppādanirodhepi paccuppannātītā pucchā anulomampi "
    "paccanīkampi vibhajitabbā ⟦0⟧).":
        (f"({cap(PACC_ATITA_PUCCHA)} {VIBHATTA} {B.UPPADAVARO}, {AT_UPPADANIRODHE}, {PACC_ATITA_PUCCHA} "
         f"{ANU_PACC} {VIBHAJITABBA} ⟦0⟧)."),
    "(Yathā nirodhavāre atītānāgatā ⟦0⟧ pucchā yassakampi yatthakampi yassayatthakampi anulomampi paccanīkampi "
    "vibhattaṃ, evaṃ uppādanirodhepi atītānāgatā pucchā vibhajitabbā.)":
        (f"({cap(ATITANAGATA_PUCCHA)} ⟦0⟧ {THREE_PARTS}, {ANU_PACC}, {VIBHATTA} {B.NIRODHAVARO}, "
         f"{AT_UPPADANIRODHE}, {ATITANAGATA_PUCCHA} {VIBHAJITABBA}.)"),
}
VARIANTS_3_06 = {"[vibhajitabbaṃ (sī. syā. ka.)]": "form", "[atītenānāgatā (syā.)]": "form"}

FIXED_3_06 = {
    "Uppādanirodhavāro.": D.UPPADANIRODHAVARO_CLOSE,       # «Mục về sự sinh khởi và sự chấm dứt.» (2-02, 5-03)
    "Pariññāvāro.": D.PARINNAVARO_CLOSE,                   # «Mục về sự hiểu biết trọn vẹn.» (2-02, 5-03)
    "Āyatanayamakaṃ niṭṭhitaṃ.": S.yamaka_end(A.YAMAKA),   # = 4 / 5-03 / 7-11 / 8 / 9-03 «<X>yamakaṃ niṭṭhitaṃ.»
    "Namo tassa bhagavato arahato sammāsambuddhassa": S.HOMAGE,   # (pi-1; = 2-02, 4, 7-11, 9-03)
}

SLIPS = dict(A5.SLIPS)
SLIPS.update({   # plain slips and punctuation, rendered as meant (reported)
    "manāyatanaṃ …pe…": "manāyatanaṃ…pe…",                          # ^6-3-217 stray space before the cut (= 3-04)
    "arūpānaṃ tasaṃ tattha": "arūpānaṃ tesaṃ tattha",              # ^6-3-244 tasaṃ for tesaṃ
    "[vibhajitabbaṃ (sī syā. ka.)] ).": "[vibhajitabbaṃ (sī. syā. ka.)]).",   # ^6-3-229 «sī» dot; space before «)»
})
UPAPAJJISSATI_SEEN = []   # "upapajjissati" for uppajjissati (2-01 VERB_TABLE «sẽ sinh khởi», coordinator)


def heading(text, yamaka=A.YAMAKA):
    if text in D.HEADINGS:                                  # unnumbered pariññāvāra sections (2-02)
        return D.HEADINGS[text]
    return A.heading(text, yamaka)


# ===============================================================================================================
# 4. Sentences, units, lines (3-05's chain + family E)
# ===============================================================================================================
def sentence_vi(s, M=None, planes=None):
    M = M or M_AY
    if s in FIXED_3_06:
        return FIXED_3_06[s]
    if s in NOTES_3_06:
        return NOTES_3_06[s]
    if (out := ye_tail_sentence(s, M, planes)) is not None:
        return out
    return A5.sentence_vi(s, M, planes)


def unit_vi(u, M=None, planes=None):
    M = M or M_AY
    if u in FIXED_3_06 or u in NOTES_3_06 or YE_TAIL_RE.fullmatch(u):
        return sentence_vi(u, M, planes)
    return A5.unit_vi(u, M, planes)


def line_vi(body, M=None, planes=None):
    M = M or M_AY
    if body in FIXED_3_06 or body in NOTES_3_06:
        return sentence_vi(body, M, planes)
    if "parijān" in body:                                    # family E (2-02), nothing else
        out = D.e_line(body, M)
        if out is None:
            raise ValueError(f"family-E line not placed: {body!r}")
        return out
    units = [x for x in re.split(r"(?<=[.?]) (?=\S)", body.strip()) if x]
    if "…" not in body and any(YE_TAIL_RE.fullmatch(x) for x in units):
        return " ".join(unit_vi(x, M, planes) for x in units)
    try:
        return A5.line_vi(body, M, planes)
    except ValueError:
        if "…pe…" in body and (out := mixed_line(body, M, planes)) is not None:
            return out
        raise


def tr_line(p, M=None, variant_kind=None, planes=None, yamaka=A.YAMAKA):
    M = M or M_AY
    m = re.search(r" (\^\S+)$", p)
    bid = m.group(1) if m else None
    body = p[:m.start()] if m else p
    variant_kind = {**A4.VARIANTS_3_04, **VARIANTS_3_06, **(variant_kind or {})}
    if body.startswith("#"):
        hashes, text = body.split(" ", 1)
        out = f"{hashes} {heading(text, yamaka)}"
    else:
        for bad, good in SLIPS.items():
            if bad in body:
                SLIPS_SEEN.append((bid, bad, good))
                body = body.replace(bad, good)
        if "upapajjissati" in body:
            UPAPAJJISSATI_SEEN.append((bid, body[:90]))
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


def build(name=CH, M=None, variant_kind=None, planes=None, yamaka=A.YAMAKA):
    segs = []
    for seg in S.segments_of(name):
        out = []
        for ln in seg:
            try:
                out.append(tr_line(ln, M, variant_kind, planes, yamaka))
            except ValueError as e:
                raise ValueError(f"{name}: cannot place line {ln[:140]!r}: {e}") from None
        segs.append(out)
    return segs


# ===============================================================================================================
# 5. Checks
# ===============================================================================================================
VI_5_02 = S.OUT_DIR / "5-02-saccayamaka.md"


def check_frames():
    M = M_AY
    # the Ye-tail head = 3-02's Ye head + 3-03's tail; the same answer with a person group before "ye ca" = 3-03's
    core = "Ye rūpāvacaraṃ upapajjitvā parinibbāyissanti"
    assert ye_tail_head(core, "cavantānaṃ") == f"{B.ye_clause(core, PLANES)}, {D.KHI_CAVANTA}"
    s1 = (f"{core} tesaṃ cavantānaṃ tesaṃ cakkhāyatanaṃ uppajjissati, no ca tesaṃ ghānāyatanaṃ nirujjhissati.")
    s2 = ("Pacchimabhavikānaṃ ye ca rūpāvacaraṃ upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ tesaṃ cakkhāyatanaṃ "
          "uppajjissati, no ca tesaṃ ghānāyatanaṃ nirujjhissati.")
    v1, v2 = sentence_vi(s1, M), A5.sentence_vi(s2, M)
    tail1 = v1.split(f", {D.KHI_CAVANTA}, ", 1)[1]
    tail2 = v2.split(f", {D.KHI_CAVANTA}, ", 1)[1]
    assert tail1 == tail2, (v1, v2)
    # the member fragment = 5-03's «<Head>, thì <res> A» and the head of the full answer
    f = member_fragment("Sabbesaṃ cavantānaṃ aghānakānaṃ upapajjantānaṃ tesaṃ tattha dhammāyatanaṃ", M)
    assert f.endswith(f", {C.THEN} {B.L['tesaṃ tattha']} {M.subj('dhammāyatanaṃ')}"), f
    # the no-ca cut = the full 2-01 b_noca answer up to its «, nhưng <loc>»
    c = noca_cut("Asaññasattaṃ upapajjantānaṃ tesaṃ tattha rūpāyatanaṃ uppajjati, no ca tesaṃ tattha", M)
    assert c.endswith(f", {C.BUT} {B.L['tesaṃ tattha']}"), c
    # note pieces: 5-02's three-part list occurs in the 5-02 rails; 2-02's Yathā wording
    vi502 = unicodedata.normalize("NFC", VI_5_02.read_text(encoding="utf-8"))
    assert THREE_PARTS in vi502, THREE_PARTS
    assert D.HEADINGS["Paccuppannātītavāro"] == f"Mục về {B.TIME['Paccuppannātīta']}"
    assert FIXED_3_06["Āyatanayamakaṃ niṭṭhitaṃ."] == "Phần các cặp câu hỏi về các lĩnh vực nhận biết đã hoàn tất."
    # family E: identical to 2-02's frames with the Āyatana members
    assert D.e_line("(Ka) yo cakkhāyatanaṃ parijānāti so sotāyatanaṃ parijānātīti? Āmantā.", M) == \
        "(a) Người nào mà hiểu biết trọn vẹn lĩnh vực mắt, thì người ấy có phải hiểu biết trọn vẹn lĩnh vực tai " \
        "không? Đúng vậy."
    assert D.e_sentence("Arahā cakkhāyatanaṃ na parijānāti, no ca sotāyatanaṃ na parijānittha.", M) == \
        "Bậc A-la-hán không hiểu biết trọn vẹn lĩnh vực mắt, nhưng đã từng hiểu biết trọn vẹn lĩnh vực tai."
    assert D.e_sentence("Ye maggaṃ paṭilabhissanti te cakkhāyatanaṃ na parijānanti, no ca sotāyatanaṃ na "
                        "parijānissanti.", M).endswith("nhưng vẫn sẽ hiểu biết trọn vẹn lĩnh vực tai.")
    assert D.e_sentence("Aggamaggasamaṅgī sotāyatanaṃ na parijānittha, no ca cakkhāyatanaṃ na parijānāti.", M) \
        .endswith("nhưng vẫn hiểu biết trọn vẹn lĩnh vực mắt.")


# ===============================================================================================================
# 6. Notes file (Pāli = tiếng Việt)
# ===============================================================================================================
def notes():
    M = M_AY
    out = []

    def row(p, v):
        out.append(f"{p} = {v}")

    def h(t):
        out.extend(["", f"## {t}", ""])

    out += [f"# pi-6 rails {N} (Āyatanayamaka 6): uppādanirodhavāra (future, present-past, present-future, "
            "past-future), pariññāvāra, end of the Āyatanayamaka", "",
            "Builder: build_rails_3-06_vi.py (import with importlib). Members, attributes, heads, labels, verbs and "
            "all family-B answer frames are 3-05's / 3-04's / 3-03's / 3-02's / 3-01's (on 2-01 / 7-01); the "
            "pariññāvāra is 2-02's family E (D.e_line) with the Āyatana members; headings and closings 2-02's. New "
            "here: `YE_TAIL_RE`, `ye_tail_head`, `ye_tail_sentence`, `member_fragment`, `noca_cut`, `piece_vi`, "
            "`mixed_line`, `NOTES_3_06` (pieces `PUCCHA`, `ANU_PACC`, `VIBHATTA`, `VIBHAJITABBA`, `THREE_PARTS`, "
            "`PACC_ATITA_PUCCHA`, `ATITANAGATA_PUCCHA`, `AT_UPPADANIRODHE`), `VARIANTS_3_06`, `FIXED_3_06`, "
            "`SLIPS`, `heading`, `sentence_vi`, `unit_vi`, `line_vi`, `tr_line`, `build`. Format: Pāli = tiếng Việt.",
            ""]
    h("Bare Ye head with a 'tesaṃ cavantānaṃ' tail (new; 3-02 Ye head + 3-03 / 2-02 tail)")
    for s in ("Ye rūpāvacaraṃ upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ tesaṃ cakkhāyatanaṃ uppajjissati, no ca "
              "tesaṃ ghānāyatanaṃ nirujjhissati.",
              "Ye rūpāvacaraṃ upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ tesaṃ ghānāyatanaṃ na nirujjhissati, no "
              "ca tesaṃ cakkhāyatanaṃ nuppajjissati."):
        row(s, sentence_vi(s, M))
    h("Answers cut by …pe… after the first member or after 'no ca tesaṃ [tattha]' (new)")
    for ln in ("Sabbesaṃ cavantānaṃ acakkhukānaṃ upapajjantānaṃ tesaṃ…pe… sacakkhukānaṃ upapajjantānaṃ tesaṃ "
               "rūpāyatanañca nirujjhissati cakkhāyatanañca uppajjati.",
               "Sabbesaṃ cavantānaṃ aghānakānaṃ upapajjantānaṃ tesaṃ tattha dhammāyatanaṃ…pe… saghānakānaṃ "
               "upapajjantānaṃ tesaṃ tattha dhammāyatanañca nirujjhissati ghānāyatanañca uppajjati.",
               "Asaññasattaṃ upapajjantānaṃ tesaṃ tattha rūpāyatanaṃ uppajjati, no ca tesaṃ tattha…pe… "
               "pañcavokāraṃ upapajjantānaṃ tesaṃ tattha…pe….",
               "Pañcavokārā cavantānaṃ arūpānaṃ tesaṃ tattha…pe… pañcavokāraṃ upapajjantānaṃ tesaṃ tattha "
               "manāyatanañca nirujjhissati rūpāyatanañca uppajjati."):
        row(ln, line_vi(ln, M))
    h("Mixed uppāda / nirodha answers of this chapter (all 3-05 / 3-04 / 3-03 frames)")
    for s in ("Pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti tesaṃ "
              "upapajjantānaṃ tesaṃ sotāyatanaṃ nirujjhissati, no ca tesaṃ cakkhāyatanaṃ uppajjissati.",
              "Pañcavokāre parinibbantānaṃ arūpe pacchimabhavikānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti tesaṃ "
              "cavantānaṃ tesaṃ cakkhāyatanañca nuppajjissati sotāyatanañca na nirujjhissati.",
              "Pacchimabhavikānaṃ upapajjantānaṃ tesaṃ manāyatanaṃ nuppajjissati, no ca tesaṃ dhammāyatanaṃ na "
              "nirujjhissati.",
              "Sabbesaṃ cavantānaṃ acakkhukānaṃ upapajjantānaṃ tesaṃ sotāyatanaṃ nirujjhittha, no ca tesaṃ "
              "cakkhāyatanaṃ uppajjati.",
              "Kāmāvacarā cavantānaṃ acakkhukānaṃ kāmāvacaraṃ upapajjantānaṃ tesaṃ tattha cakkhāyatanaṃ nuppajjati, "
              "no ca tesaṃ tattha ghānāyatanaṃ na nirujjhissati.",
              "Pañcavokāre parinibbantānaṃ arūpe pacchimabhavikānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti tesaṃ "
              "cavantānaṃ tesaṃ cakkhāyatanaṃ uppajjittha, no ca tesaṃ sotāyatanaṃ nirujjhissati."):
        row(s, sentence_vi(s, M))
    h("Pariññāvāra (2-02 family E with the Āyatana members)")
    for q in ("(Ka) yo cakkhāyatanaṃ parijānittha so sotāyatanaṃ parijānissatīti? No.",
              "(Kha) yo vā pana sotāyatanaṃ na parijānittha so cakkhāyatanaṃ na parijānātīti?",
              "Arahā cakkhāyatanaṃ na parijānāti, no ca sotāyatanaṃ na parijānittha.",
              "Aggamaggasamaṅgiñca arahantañca ṭhapetvā avasesā puggalā cakkhāyatanañca na parijānanti sotāyatanañca "
              "na parijānittha.",
              "Ye maggaṃ paṭilabhissanti te cakkhāyatanaṃ na parijānanti, no ca sotāyatanaṃ na parijānissanti.",
              "Aggamaggasamaṅgī ye ca puthujjanā maggaṃ na paṭilabhissanti te cakkhāyatanañca na parijānittha "
              "sotāyatanañca na parijānissanti."):
        row(q, line_vi(q, M))
    h("Headings, closing lines and editorial notes")
    for t in ("Pariññāvāro", "Paccuppannavāro", "Paccuppannātītavāro", "Atītānāgatavāro"):
        row(t, heading(t))
    for p, v in FIXED_3_06.items():
        row(p, v)
    for p, v in NOTES_3_06.items():
        brs = {"⟦0⟧": "[vibhajitabbaṃ (sī. syā. ka.)]"} if "vibhajitabbā ⟦0⟧" in p else \
            {"⟦0⟧": "[atītenānāgatā (syā.)]"}
        row(p.replace("⟦0⟧", brs["⟦0⟧"]), v.replace("⟦0⟧", A.var_vi(brs["⟦0⟧"], "form")))
    row("paccuppannātītā pucchā / atītānāgatā pucchā", f"{PACC_ATITA_PUCCHA} / {ATITANAGATA_PUCCHA}")
    row("yassakampi yatthakampi yassayatthakampi", THREE_PARTS)
    row("anulomampi paccanīkampi", ANU_PACC)
    row("yathā … vibhattā / vibhattaṃ, evaṃ … vibhajitabbā", f"{VIBHATTA} … , … {VIBHAJITABBA}")
    h("Termbase misfits and gaps (for the coordinator)")
    out += [
        "- No new member, person, plane or verb words: all from 3-01 … 3-05 / 2-01 / 2-02 (termbase).",
        "- Two finished chapters word the note pieces differently: anulomampi paccanīkampi «theo chiều thuận và chiều "
        "nghịch» (3-04 / 3-05) vs «cả chiều thuận lẫn chiều nghịch» (5-02); pucchā «câu hỏi» (3-04 / 3-05) vs "
        "«các câu hỏi» (5-02); vibhajitabbā «cũng nên phân tích như vậy» (pi-2, 2-02, 5-02) vs «cũng nên được phân "
        "tích như vậy» (4). Followed pi-2 for vibhatta / vibhajitabba, then the Āyatana chain (earlier chapter) for "
        "the rest; 5-02's «ở cả phần về người, phần về nơi chốn lẫn phần về người và nơi chốn» for the three-part "
        "list (no Āyatana parallel).",
        "- The bare Ye head with «, khi những người ấy đang chết đi» (^6-3-211, ^6-3-220) is new: no earlier chapter "
        "has 'Ye … parinibbāyissanti tesaṃ cavantānaṃ' without a person group before it.",
        "",
        "## Slips and unsure Pāli (rendered as meant or kept; reported)",
        "",
        "- ^6-3-212 «… no ca tesaṃ ghānāyatanaṃ upapajjissati»: upapajjissati for uppajjissati; «sẽ sinh khởi» "
        "(coordinator rule, 2-01 VERB_TABLE).",
        "- ^6-3-217 «manāyatanaṃ …pe…»: stray space before the cut; dropped (as 3-04 ^6-3-151).",
        "- ^6-3-229 «vibhajitabbā [vibhajitabbaṃ (sī syā. ka.)] ).»: «sī» lacks its dot (read «sī.»), and the space "
        "before «)» is dropped.",
        "- ^6-3-244 «arūpānaṃ tasaṃ tattha»: tasaṃ for tesaṃ.",
        "- ^6-3-230, 236, 237 answers cut by …pe… after the head, after the first member or after «no ca tesaṃ "
        "tattha», some then giving the second answer whole: translated as cut, «…» at the same spots.",
        "- ^6-3-215, 224, 234, 243 «Yattha … …pe….»: place sections cut; «Ở nơi nào mà …» (3-01).",
        "- ^6-3-221, 222, 239 … «Yassa vā pana dhammāyatanaṃ…pe…? Āmantā.»: cut questions (3-04 cut_q0).",
        "- ^6-3-248 the past-future uppādanirodha section gives one pair and a note; «Uppādanirodhavāro.» and "
        "«Pavattivāro niṭṭhito.» close it (kept as separate lines).",
        "",
    ]
    return "\n".join(out)


def main():
    S.check_reused()
    B.check_reused()
    A.check_reused()
    A4.check_reused()
    A.check_frames()
    segs = build(CH)
    A2.check_frames()
    A3.check_frames()
    A4.check_frames()
    A5.check_frames()
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
    for s in UPAPAJJISSATI_SEEN:
        print("upapajjissati:", s)
    for k, v in NEW_SEEN.items():
        print(f"{k}: {len(v)}")


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
