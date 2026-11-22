"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 3-02 (Āyatanayamaka, part 2: future, present+past tenses).

Everything comes from the Āyatana module build_rails_3-01_vi (members, attributes, cuts, labels, notes), which is
built on families A / B (build_rails_2-01_vi) and the shared shapes (build_rails_7-01_vi); the "P ye ca … " head is
2-02's (build_rails_2-02_vi). All imported READ-ONLY. This file adds, for 3-02 … 3-06:

  ay_person_items / ay_persons   person heads that mix āyatana attributes WITH planes
                                 ("Pañcavokārā cavantānaṃ acakkhukānaṃ kāmāvacaraṃ upapajjantānaṃ"), and a run of
                                 groups in which a run of plane-beings is nested is joined flat «A, B và C»
                                 (never «A và B và C»; 7-01 list rule)
  answer_head                    + "Ye … upapajjitvā parinibbāyissanti" (2-01 ye_clause) and
                                 "P ye ca … parinibbāyissanti" (2-02 b_head) with the Āyatana person parser
  SADISA_NOTE / sadisa_note      "Yassa A V (tassa B-ñca C-ñca sadisaṃ, ime dve sadisāyeva honti)."
  b_sentence / sentence_vi / unit_vi / line_vi / tr_line / build   3-01's chain with the heads above
A line, unit or word the parsers cannot place raises ValueError (no silent fallback). Importing writes nothing.

    A2 = importlib.import_module("build_rails_3-02_vi"); segs = A2.build("3-03-ayatanayamaka.md", fixed=…, …)

usage: python -I -X utf8 -B build_rails_3-02_vi.py
"""
import importlib
import re
import sys
import unicodedata

RAILS_DIR = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\rails"
if RAILS_DIR not in sys.path:
    sys.path.insert(0, RAILS_DIR)
import build_rails_sample_vi as S  # noqa: E402  (READ-ONLY)
A = importlib.import_module("build_rails_3-01_vi")   # READ-ONLY: the Āyatana module (setter of 3-02 … 3-06)
B = importlib.import_module("build_rails_2-01_vi")   # READ-ONLY: families A / B (setter)
C = importlib.import_module("build_rails_7-01_vi")   # READ-ONLY: shared shell and answer shapes
D = importlib.import_module("build_rails_2-02_vi")   # READ-ONLY: the "P ye ca …" head (B additions)

cap = S.cap
CH = "3-02-ayatanayamaka.md"
N = "3-02"
NOTES_MD = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/notes-rails-{N}.md"
ADH_DIR = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/adh-{N}"
SLIPS_SEEN = []
HEADS_SEEN = []          # (head, Vietnamese) of every person head built (checked against the setters' parsers)
FLATTENED = set()        # heads joined flat because a run of plane-beings is nested in them (differ from 2-01)

# ===============================================================================================================
# 1. Person heads: āyatana attributes together with planes; flat lists
# ===============================================================================================================
PLANES = A.PLANES_AY


def ay_group(quant, attrs, part, plane_keys, planes=None):
    """One person group. = B.person_group (pacchimabhavika-type attributes, planes) and A.ay_group (āyatana
    attributes joined by A.ATTR_JOIN), in one: «những người không có mắt đang tái sinh vào cõi dục lạc»."""
    planes = planes or PLANES
    ay = [a for a in attrs if a in A.AY_ATTRS]
    other = [a for a in attrs if a not in A.AY_ATTRS]
    if ay and other:
        raise ValueError(f"mixed attribute kinds {attrs!r}")
    words = []
    if quant == "sabbesaṃ":
        words.append(B.QUANT[quant])
    words.append(B.PERSON)
    if quant == "itaresaṃ":
        words.append(B.QUANT[quant])
    if ay:
        words.append(A.ATTR_JOIN.join(A.AY_ATTRS[a] for a in ay))
    words += [B.ATTRS[a] for a in other]
    if part:
        pv, case, prep = B.PARTICIPLES[part]
        words.append(pv)
        if plane_keys:
            words.append(f"{prep} {B.join_and(planes[k][0] for k in plane_keys)}")
    elif plane_keys:
        words.append(f"{B.LOC_PREP} {B.join_and(planes[k][0] for k in plane_keys)}")
    return " ".join(words)


def ay_person_items(head, planes=None):
    """Genitive person phrase → list of items: ('group', vi) or ('run', keys, quant). Same grammar as B.persons,
    plus āyatana attributes (A.AY_ATTRS) before a participle with or without planes."""
    planes = planes or PLANES
    toks = head.split()
    items, quant, attrs, pl, i = [], None, [], [], 0

    def dangling():
        if quant or attrs or pl:
            raise ValueError(f"dangling words in person phrase {head!r}")

    while i < len(toks):
        t = toks[i].lower()
        nxt = toks[i + 1].lower() if i + 1 < len(toks) else None
        pt = B.plane_tok(t, planes)
        if t in B.QUANT:
            dangling()
            quant = t
            if nxt is None:                                  # Itaresaṃ alone «những người khác»
                if t != "itaresaṃ":
                    raise ValueError(f"bare {t!r} in {head!r}")
                items.append(("group", ay_group(quant, [], None, [], planes)))
                quant = None
        elif t in A.AY_ATTRS:
            if pl:
                raise ValueError(f"plane before an āyatana attribute in {head!r}")
            attrs.append(t)
        elif t in B.ATTRS:                                   # = B.persons
            np_ = B.plane_tok(nxt, planes) if nxt else None
            if pl and all(c == "loc" for _, c in pl):        # Pañcavokāre pacchimabhavikānaṃ «… trong cõi X»
                items.append(("group", ay_group(quant, attrs + [t], None, [k for k, _ in pl], planes)))
                quant, attrs, pl = None, [], []
            elif pl:
                raise ValueError(f"plane case before attribute in {head!r}")
            elif nxt in B.PARTICIPLES or (np_ and np_[1] in ("acc", "abl")):
                attrs.append(t)
            else:
                items.append(("group", ay_group(quant, attrs + [t], None, [], planes)))
                quant, attrs = None, []
        elif t in B.PARTICIPLES:
            case = B.PARTICIPLES[t][1]
            if any(c != case for _, c in pl):
                raise ValueError(f"plane case does not fit {t!r} in {head!r}")
            items.append(("group", ay_group(quant, attrs, t, [k for k, _ in pl], planes)))
            quant, attrs, pl = None, [], []
        elif pt and pt[1] == "gen":
            if attrs or pl:
                raise ValueError(f"plane-being after modifiers in {head!r}")
            run = [pt[0]]
            while i + 1 < len(toks) and (q := B.plane_tok(toks[i + 1], planes)) and q[1] == "gen":
                run.append(q[0])
                i += 1
            items.append(("run", run, quant))
            quant = None
        elif pt:
            pl.append(pt)
        else:
            raise ValueError(f"unknown word {toks[i]!r} in person phrase {head!r}")
        i += 1
    dangling()
    return items


def ay_persons(head, planes=None):
    """Person phrase → Vietnamese without «Ở». A head that is one run of plane-beings keeps 2-01's being_run
    («chúng sinh trong cõi Tịnh Cư và cõi Vô Tưởng»); in a run of several groups every plane-being is its own
    item and the whole list is joined once («A, B và C»: 7-01 list rule; never «A và B và C»)."""
    planes = planes or PLANES
    items = ay_person_items(head, planes)
    if len(items) == 1 and items[0][0] == "run":
        out = B.being_run(items[0][1], items[0][2], planes)
    else:
        flat = []
        for it in items:
            if it[0] == "group":
                flat.append(it[1])
            elif len(it[1]) == 1:
                flat.append(B.being_run(it[1], it[2], planes))
            elif it[2]:
                raise ValueError(f"{it[2]!r} before a nested run of planes in {head!r}")
            else:
                flat += [planes[k][1] for k in it[1]]
        out = B.join_and(flat)
        if len(items) > 1 and any(it[0] == "run" and len(it[1]) > 1 for it in items):
            FLATTENED.add(out)
    HEADS_SEEN.append((head, out))
    return out


def ye_ca_head(head, planes=None):
    """'P ye ca <plane> upapajjitvā parinibbāyissanti [tesaṃ cavantānaṃ]' = 2-02 b_head with this person parser."""
    left, right = head.split(f" {D.YE_CA} ", 1)
    cav = right.endswith(" tesaṃ cavantānaṃ")
    if cav:
        right = right[: -len(" tesaṃ cavantānaṃ")]
    ye = B.ye_clause("Ye " + right, planes or PLANES)
    ye = ye[0].lower() + ye[1:]
    return f"{B.AT} {ay_persons(left, planes)} {D.AND} {ye}" + (f", {D.KHI_CAVANTA}" if cav else "")


def answer_head(head, loc, planes=None):
    planes = planes or PLANES
    var = ""
    if m := re.fullmatch(r"(.+) (⟦\d+⟧)", head):
        head, var = m.group(1), " " + m.group(2)
    if loc == "tattha":
        return B.place_head(head, planes) + var
    if f" {D.YE_CA} " in head:
        return ye_ca_head(head, planes) + var
    if head.startswith("Ye "):
        return B.ye_clause(head, planes) + var                    # «Những người nào sau khi tái sinh vào …»
    return f"{B.AT} {ay_persons(head, planes)}" + var


# ===============================================================================================================
# 2. Editorial note of this chapter
# ===============================================================================================================
SADISA = "giống nhau"                 # sadisaṃ (3-01 note «… đều giống nhau»; termbase -sadisaṃ «giống như …»)
IME_DVE = "hai điều này"              # ime dve
SADISAYEVA_HONTI = f"đúng là {SADISA}"   # sadisā eva honti (eva: «đúng là»)
SADISA_NOTE = re.compile(r"(Yassa|Yattha) (.+?) \((tassa|tattha) (\S+?)ñca (\S+?)ñca sadisaṃ, "
                         r"ime dve sadisāyeva honti\)\.")


def sadisa_note(s, M=None):
    """'Yassa A V (tassa B-ñca C-ñca sadisaṃ, ime dve sadisāyeva honti).' → «Ở người nào mà A V (thì ở người ấy B
    và C giống nhau, hai điều này đúng là giống nhau).» The first half = 2-02 b_cut's shell half."""
    M = M or A.AYATANA
    m = SADISA_NOTE.fullmatch(s)
    if not m:
        return None
    w1, c1, then, m1, m2 = m.groups()
    who = w1.lower()
    if C.Q_COR[who] != then:
        raise ValueError(f"relative {who!r} with correlative {then!r}")
    a, v = A.split_mv(c1, M)
    first = D.b_cut(f"{w1} {c1}…pe….", M)[:-len(S.PE)]
    assert first == f"{cap(C.AT)} {C.Q_REL[who][0]} mà {a} {v[0]}", first
    pair = B.join_and([M.subj(m1 + "ñca"), M.subj(m2 + "ñca")])
    return f"{first} ({C.THEN} {B.L[then]} {pair} {SADISA}, {IME_DVE} {SADISAYEVA_HONTI})."


# ===============================================================================================================
# 3. Sentences, units, lines (3-01's chain; only the family-B answer heads differ)
# ===============================================================================================================
LOC = A.LOC
SLIPS = dict(A.SLIPS)
SLIPS.update({
    "rūpāyatanañca ca uppajjittha": "rūpāyatanañca uppajjittha",   # ^6-3-75: «ca» written twice
})


def b_sentence(s, M=None, planes=None):
    """3-01's two family-B regexes (B.b_noca / B.b_both) with this file's answer_head."""
    M = M or A.AYATANA
    if m := re.fullmatch(r"(.+?) " + LOC + r" (.+?), no ca \2 (.+?)\.", s):
        head, loc, c1, c2 = m.groups()
        a, v1 = A.split_mv(c1, M)
        b, v2 = A.split_mv(c2, M)
        return B.b_noca(answer_head(head, loc, planes), loc, a, v1, b, v2)
    if m := re.fullmatch(r"(.+?) " + LOC + r" (\S+?ñca) (\S+) (\S+?ñca) (\S+)\.", s):
        head, loc, c1, v1, c2, v2 = m.groups()
        return B.b_both(answer_head(head, loc, planes), loc, M.subj(c1), B.verb(v1), M.subj(c2), B.verb(v2))
    return None


def sentence_vi(s, M=None, planes=None):
    M = M or A.AYATANA
    if (out := sadisa_note(s, M)) is not None:
        return out
    if (out := b_sentence(s, M, planes)) is not None:
        try:                                     # where 3-01 can build it, it must be byte-identical
            old = A.sentence_vi(s, M, planes)
        except ValueError:
            old = None
        if old is not None and old != out and not any(f in out for f in FLATTENED):
            raise AssertionError(f"3-01 differs:\n{old}\n{out}")
        return out
    return A.sentence_vi(s, M, planes)


def unit_vi(u, M=None, planes=None):
    M = M or A.AYATANA
    if u[:1].isupper() and u.endswith(".") and not u.startswith("("):
        try:
            return sentence_vi(u, M, planes)
        except ValueError:
            pass
    return A.unit_vi(u, M, planes)


def units_vi(piece, M=None, planes=None):
    units = [x for x in re.split(r"(?<=[.?]) (?=\S)", piece.strip()) if x]
    return " ".join(unit_vi(x, M, planes) for x in units)


def line_vi(body, M=None, planes=None):
    M = M or A.AYATANA
    if "…" in body or SADISA_NOTE.fullmatch(body):
        if SADISA_NOTE.fullmatch(body):
            return sadisa_note(body, M)
        return A.line_vi(body, M, planes)        # cut lines: 3-01 (no person heads inside a cut in 3-02)
    return units_vi(body, M, planes)


def tr_line(p, M=None, fixed=None, variant_kind=None, planes=None, yamaka=A.YAMAKA):
    M = M or A.AYATANA
    m = re.search(r" (\^\S+)$", p)
    bid = m.group(1) if m else None
    body = p[:m.start()] if m else p
    fixed = fixed or {}
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
            if br not in (variant_kind or {}):
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
# 4. Checks: the setters' strings where their parsers reach
# ===============================================================================================================
def nested_run(head):
    items = ay_person_items(head)
    return len(items) > 1 and any(it[0] == "run" and len(it[1]) > 1 for it in items)


def check_frames():
    """Every head built: = B.persons where 2-01 parses it (no āyatana attribute, no nested run of planes);
    = A.ay_persons where 3-01 parses it (attributes, no planes)."""
    n_b = n_a = 0
    for head, out in HEADS_SEEN:
        has_attr = any(t.lower() in A.AY_ATTRS for t in head.split())
        if not has_attr and not nested_run(head):
            assert out == B.persons(head, PLANES), (head, out, B.persons(head, PLANES))
            n_b += 1
        if has_attr:
            try:
                old = A.ay_persons(head)
            except ValueError:
                continue
            assert out == old, (head, out, old)
            n_a += 1
    assert ye_ca_head("Pacchimabhavikānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti") == \
        D.b_head("Pacchimabhavikānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti", "tesaṃ", PLANES)
    assert answer_head("Ye arūpaṃ upapajjitvā parinibbāyissanti", "tesaṃ") == \
        B.answer_head("Ye arūpaṃ upapajjitvā parinibbāyissanti", "tesaṃ", PLANES)
    print(f"heads checked against 2-01: {n_b}, against 3-01: {n_a}")


# ===============================================================================================================
# 5. Notes file (Pāli = tiếng Việt)
# ===============================================================================================================
def notes():
    M = A.AYATANA
    out = []

    def row(p, v):
        out.append(f"{p} = {v}")

    def h(t):
        out.extend(["", f"## {t}", ""])

    out += [f"# pi-6 rails {N} (Āyatanayamaka 2): future and present-past tenses on the 3-01 Āyatana module", "",
            "Builder: build_rails_3-02_vi.py (import with importlib). Members, attributes, labels, notes, cuts and all "
            "frames are 3-01's (build_rails_3-01_vi, on 2-01 / 7-01); the 'P ye ca …' head is 2-02's. New here, "
            "exposed for 3-03 … 3-06: `ay_group`, `ay_person_items`, `ay_persons`, `ye_ca_head`, `answer_head`, "
            "`SADISA`, `IME_DVE`, `SADISAYEVA_HONTI`, `SADISA_NOTE`, `sadisa_note`, `SLIPS`, `b_sentence`, "
            "`sentence_vi`, `unit_vi`, `line_vi`, `tr_line`, `build`. Where 2-01 / 3-01 can parse a head, the "
            "builder asserts the string is theirs byte for byte. Format: Pāli = tiếng Việt.", ""]
    h("Person heads: āyatana attributes with planes (new shape)")
    for hd in ("Sacakkhukānaṃ kāmāvacaraṃ upapajjantānaṃ",
               "Pañcavokārā cavantānaṃ acakkhukānaṃ kāmāvacaraṃ upapajjantānaṃ",
               "Kāmāvacarā cavantānaṃ aghānakānaṃ kāmāvacaraṃ upapajjantānaṃ rūpāvacarānaṃ",
               "Pañcavokārā cavantānaṃ acakkhukānaṃ kāmāvacaraṃ upapajjantānaṃ asaññasattānaṃ"):
        row(hd, ay_persons(hd))
    h("Person heads: a nested run of plane-beings is joined flat (new rule; 7-01 «A, B và C»)")
    for hd in ("Kāmāvacarā cavantānaṃ aghānakānaṃ kāmāvacaraṃ upapajjantānaṃ rūpāvacarānaṃ arūpāvacarānaṃ",
               "Pañcavokāre pacchimabhavikānaṃ asaññasattānaṃ arūpānaṃ",
               "Suddhāvāse parinibbantānaṃ asaññasattānaṃ arūpānaṃ",
               "Rūpāvacarā cavantānaṃ asaññasattānaṃ arūpānaṃ"):
        row(hd, ay_persons(hd))
    out.append("(2-01's persons() would give «… và chúng sinh Vô Tưởng và chúng sinh trong cõi không hình sắc»; a head "
               "that is only a run keeps 2-01's being_run:)")
    for hd in ("Suddhāvāsānaṃ asaññasattānaṃ", "Suddhāvāsānaṃ arūpānaṃ", "Rūpāvacarānaṃ arūpāvacarānaṃ",
               "Asaññasattānaṃ arūpānaṃ", "Catuvokārānaṃ pañcavokārānaṃ", "Pañcavokārānaṃ asaññasattānaṃ"):
        row(hd, ay_persons(hd))
    h("Ye-clause heads in the Āyatana chapters (2-01 ye_clause, 2-02 b_head)")
    for hd in ("Ye rūpāvacaraṃ upapajjitvā parinibbāyissanti", "Ye rūpāvacaraṃ arūpāvacaraṃ upapajjitvā parinibbāyissanti",
               "Ye arūpaṃ upapajjitvā parinibbāyissanti"):
        row(hd + " tesaṃ …", answer_head(hd, "tesaṃ") + f", {C.THEN} {B.L['tesaṃ']} …")
    row("Pacchimabhavikānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti tesaṃ …",
        answer_head("Pacchimabhavikānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti", "tesaṃ") +
        f", {C.THEN} {B.L['tesaṃ']} …")
    row("Itaresaṃ tesaṃ …", answer_head("Itaresaṃ", "tesaṃ") + f", {C.THEN} {B.L['tesaṃ']} …")
    h("Sample sentences")
    for s in ("Ye rūpāvacaraṃ upapajjitvā parinibbāyissanti tesaṃ cakkhāyatanaṃ uppajjissati, no ca tesaṃ "
              "ghānāyatanaṃ uppajjissati.",
              "Pacchimabhavikānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti tesaṃ ghānāyatanañca nuppajjissati "
              "cakkhāyatanañca nuppajjissati.",
              "Pañcavokārā cavantānaṃ acakkhukānaṃ kāmāvacaraṃ upapajjantānaṃ tesaṃ tattha cakkhāyatanaṃ nuppajjati, "
              "no ca tesaṃ tattha sotāyatanaṃ nuppajjittha.",
              "Suddhāvāse parinibbantānaṃ asaññasattānaṃ arūpānaṃ tesaṃ tattha cakkhāyatanañca nuppajjati "
              "sotāyatanañca nuppajjittha."):
        row(s, sentence_vi(s, M))
    h("Editorial note")
    row("Yassa cakkhāyatanaṃ uppajjissati (tassa manāyatanañca dhammāyatanañca sadisaṃ, ime dve sadisāyeva honti).",
        sadisa_note("Yassa cakkhāyatanaṃ uppajjissati (tassa manāyatanañca dhammāyatanañca sadisaṃ, ime dve "
                    "sadisāyeva honti).", M))
    row("sadisaṃ / ime dve / sadisāyeva honti", f"{SADISA} / {IME_DVE} / {SADISAYEVA_HONTI}")
    h("Termbase misfits and gaps (for the coordinator)")
    out += [
        "- sadisaṃ, ime dve, sadisāyeva honti: no entries; sadisaṃ «giống nhau» as 3-01's note («… đều giống nhau»; "
        "termbase -sadisaṃ «giống như …»); ime dve «hai điều này» (masculine plural in the Pāli: not narrowed to "
        "«hai lĩnh vực này»); eva «đúng là».",
        "- Nested plane-being runs inside a longer head: joined flat («A, B và C»); 2-01 persons() would join the run "
        "inside the list («A và B và C»). No finished chapter has such a head. Please align (10-07 has the same "
        "Pāli 'Pañcavokāre pacchimabhavikānaṃ asaññasattānaṃ arūpānaṃ').",
        "",
        "## Slips (rendered as meant or kept; reported)",
        "",
        "- ^6-3-75 «rūpāyatanañca ca uppajjittha»: «ca» written twice; rendered as the both-frame («…, lĩnh vực hình "
        "sắc cũng đã sinh khởi»).",
        "- ^6-3-54 «(Rūpāyatanamūlakaṃ).» has a final «.» (the other labels do not): kept «(Phần dựa trên lĩnh vực "
        "hình sắc).».",
        "- ^6-3-74 «Āmantā.…Pe….»: the periods on both sides of the cut are absorbed (3-01).",
        "- ^6-3-80 «Yassa ghānāyatanaṃ…pe… rūpāyatanaṃ… manāyatanaṃ nuppajjati tassa dhammāyatanaṃ …»: the cut list "
        "stands in the first clause; rendered in place «… lĩnh vực mũi… lĩnh vực hình sắc… lĩnh vực ý không sinh khởi …».",
        "- Questions cut by …pe… and answered «Āmantā.» (^6-3-53, 54, 58, 61 …) keep their «?» (3-01 list question).",
        "",
    ]
    return "\n".join(out)


def main():
    S.check_reused()
    B.check_reused()
    A.check_reused()
    A.check_frames()
    segs = build(CH)
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


if __name__ == "__main__":
    main()
