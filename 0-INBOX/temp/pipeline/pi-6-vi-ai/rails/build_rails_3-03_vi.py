"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 3-03 (Āyatanayamaka, part 3: present-future and past-future tenses,
end of the uppādavāra).

Everything comes from the Āyatana chain build_rails_3-02_vi → build_rails_3-01_vi → build_rails_2-01_vi /
build_rails_7-01_vi (and build_rails_2-02_vi for the "P ye ca …" head and the closing lines), all imported READ-ONLY.
This file adds, for 3-04 … 3-06:

  KHI_UPAPAJJANTA / ye_ca_head     "P ye ca … parinibbāyissanti tesaṃ upapajjantānaṃ" «…, khi những người ấy đang
                                   tái sinh» (= 2-02's "tesaṃ cavantānaṃ" «…, khi những người ấy đang chết đi»);
                                   a left part of several person groups is joined flat with the ye clause
                                   («A, B và những người nào …»; 3-02 / 7-01 list rule, never «A và B và …»)
  b_sentence                       the family-B answers with such a head (no-ca frame and both-frame, B's frames)
  CUTQ_RE / cut_pair_q             a pair question cut by …pe… after "yassa vā pana [yattha] [A]" and before the last
                                   verb: «(b) Còn ở người nào mà… đã sinh khởi không?» (= 7-02 / 8 cut shells)
  UPPADAVARO_CLOSE                 "Uppādavāro." «Mục về sự sinh khởi.» (= 2-02 «Nirodhavāro.»)
  SLIPS                            3-02's plus this chapter's
  sentence_vi / unit_vi / units_vi / line_vi / tr_line / build   3-02's chain with the pieces above
A line, unit or word the parsers cannot place raises ValueError (no silent fallback). Importing writes nothing.

    A3 = importlib.import_module("build_rails_3-03_vi"); segs = A3.build("3-04-ayatanayamaka.md", fixed=…)

usage: python -I -X utf8 -B build_rails_3-03_vi.py
"""
import importlib
import re
import sys
import unicodedata

RAILS_DIR = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\rails"
if RAILS_DIR not in sys.path:
    sys.path.insert(0, RAILS_DIR)
import build_rails_sample_vi as S  # noqa: E402  (READ-ONLY)
A2 = importlib.import_module("build_rails_3-02_vi")  # READ-ONLY: Āyatana heads with planes (3-03 … 3-06 setter)
A = importlib.import_module("build_rails_3-01_vi")   # READ-ONLY: the Āyatana module
B = importlib.import_module("build_rails_2-01_vi")   # READ-ONLY: families A / B
C = importlib.import_module("build_rails_7-01_vi")   # READ-ONLY: shared shell and answer shapes
D = importlib.import_module("build_rails_2-02_vi")   # READ-ONLY: "P ye ca …" head, closing lines

cap = S.cap
CH = "3-03-ayatanayamaka.md"
N = "3-03"
NOTES_MD = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/notes-rails-{N}.md"
ADH_DIR = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/adh-{N}"
SLIPS_SEEN = []
YE_FLAT = set()          # ye-ca heads whose left part has several groups (joined flat; no earlier chapter has them)
PLANES = A.PLANES_AY

# ===============================================================================================================
# 1. "P ye ca … parinibbāyissanti [tesaṃ upapajjantānaṃ / tesaṃ cavantānaṃ]" heads
# ===============================================================================================================
KHI_UPAPAJJANTA = f"khi {D.TE} {B.PARTICIPLES['upapajjantānaṃ'][0]}"   # «khi những người ấy đang tái sinh»
YE_TAILS = {" tesaṃ upapajjantānaṃ": KHI_UPAPAJJANTA, " tesaṃ cavantānaṃ": D.KHI_CAVANTA}


def flat_persons(head, planes=None):
    """3-02 ay_persons as a list of items (its join is B.join_and of this list; asserted)."""
    planes = planes or PLANES
    items = A2.ay_person_items(head, planes)
    if len(items) == 1 and items[0][0] == "run":
        flat = [B.being_run(items[0][1], items[0][2], planes)]
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
    assert B.join_and(flat) == A2.ay_persons(head, planes), head
    return flat


def ye_ca_head(head, planes=None):
    """'P ye ca <plane> upapajjitvā parinibbāyissanti [tesaṃ upapajjantānaṃ / cavantānaṃ]' →
    «Ở <P> và những người nào sau khi tái sinh vào … sẽ nhập Niết-bàn trọn vẹn[, khi những người ấy đang …]».
    One group in P: byte-identical to 3-02's ye_ca_head (asserted); several groups: one flat list «A, B và …»."""
    planes = planes or PLANES
    left, right = head.split(f" {D.YE_CA} ", 1)
    tail = next((t for t in YE_TAILS if right.endswith(t)), None)
    core = right[: -len(tail)] if tail else right
    ye = B.ye_clause("Ye " + core, planes)
    ye = ye[0].lower() + ye[1:]
    flat = flat_persons(left, planes)
    out = f"{B.AT} {B.join_and(flat + [ye])}" + (f", {YE_TAILS[tail]}" if tail else "")
    if len(flat) == 1:
        if tail == " tesaṃ upapajjantānaṃ":
            assert out == f"{A2.ye_ca_head(head[: -len(tail)], planes)}, {KHI_UPAPAJJANTA}", out
        else:
            assert out == A2.ye_ca_head(head, planes), out
    else:
        YE_FLAT.add(out)
    return out


YE_HEAD_RE = re.compile(r"(.+? " + D.YE_CA + r" .+? parinibbāyissanti(?: tesaṃ (?:upapajjantānaṃ|cavantānaṃ))?) "
                        + A.LOC + r" (.+)\.")


def b_sentence(s, M=None, planes=None):
    """Family-B answer with a 'P ye ca …' head (B.b_noca / B.b_both, unchanged); None for any other sentence."""
    M = M or A.AYATANA
    m = YE_HEAD_RE.fullmatch(s)
    if not m:
        return None
    head, loc, rest = m.groups()
    head_vi = ye_ca_head(head, planes)
    if f", no ca {loc} " in rest:
        c1, c2 = rest.split(f", no ca {loc} ")
        a, v1 = A.split_mv(c1, M)
        b, v2 = A.split_mv(c2, M)
        return B.b_noca(head_vi, loc, a, v1, b, v2)
    if mm := re.fullmatch(r"(\S+?ñca) (\S+) (\S+?ñca) (\S+)", rest):
        c1, v1, c2, v2 = mm.groups()
        return B.b_both(head_vi, loc, M.subj(c1), B.verb(v1), M.subj(c2), B.verb(v2))
    raise ValueError(f"unknown answer after a ye-ca head: {s!r}")


# ===============================================================================================================
# 2. Pair questions cut by …pe… between "yassa vā pana [yattha] [A]" and the last verb
# ===============================================================================================================
CUTQ_RE = re.compile(r"(?:" + A.LAB + r" )?([Yy]assa)( vā pana)( yattha)?((?: \S+)?)…pe… (\S+)\?")


def cut_pair_q(u, M=None):
    """'(Kha) yassa vā pana [yattha] [A]…pe… Vti?' → the shell (B.b_q) up to «mà» [+ A], «…», and the second
    half's verb with «không?»: «(b) Còn ở người nào mà… đã sinh khởi không?» (7-02 «(b) Còn ở nơi nào mà…
    không?», 8 «Còn ở người nào mà… không?»)."""
    M = M or A.AYATANA
    m = CUTQ_RE.fullmatch(u)
    if not m:
        return None
    label, w1, _vapana, w2, mem, vb = m.groups()
    who = w1.lower() + (w2 or "")
    full = B.b_q(label, who, C.Q_COR[who], "⟨A⟩", "⟨V⟩", "⟨B⟩", "⟨W⟩", other=True)
    head, sep, _ = full.partition(" ⟨A⟩ ⟨V⟩")
    assert sep and full.endswith(" ⟨B⟩ ⟨W⟩ không?"), full
    first = head + (f" {M.subj(mem.strip())}" if mem.strip() else "")
    return f"{first}{S.PE} {B.verb(vb)[0]} không?"


# ===============================================================================================================
# 3. Sentences, units, lines (3-02's chain)
# ===============================================================================================================
UPPADAVARO_CLOSE = cap(B.UPPADAVARO) + "."     # Uppādavāro. «Mục về sự sinh khởi.» (= 2-02 «Nirodhavāro.»)
CLOSING = {"Uppādavāro.": UPPADAVARO_CLOSE}

SLIPS = dict(A2.SLIPS)
SLIPS.update({   # plain slips and punctuation, rendered as meant (reported)
    "(Ka) yassa =93 yattha": "(Ka) yassa yattha",                                     # ^6-3-118 page-number debris
    "tesaṃ tattha manāyatanaṃ nuppajjissati cakkhāyatanañca nuppajjati.":
        "tesaṃ tattha manāyatanañca nuppajjissati cakkhāyatanañca nuppajjati.",      # ^6-3-100 -ñca missing
    "cakkhāyatanañca nuppajjittha dhammāyatanaṃ nuppajjissati.":
        "cakkhāyatanañca nuppajjittha dhammāyatanañca nuppajjissati.",               # ^6-3-116 -ñca missing
    "manāyatanañca uppajjati, dhammāyatanañca uppajjissati.":
        "manāyatanañca uppajjati dhammāyatanañca uppajjissati.",                     # ^6-3-89 comma (= «, … cũng …»)
})


def sentence_vi(s, M=None, planes=None):
    M = M or A.AYATANA
    if s in CLOSING:
        return CLOSING[s]
    if (out := b_sentence(s, M, planes)) is not None:
        try:                                     # where 3-02 can build it, it must be byte-identical
            old = A2.sentence_vi(s, M, planes)
        except ValueError:
            old = None
        if old is not None and old != out and not any(f in out for f in YE_FLAT):
            raise AssertionError(f"3-02 differs:\n{old}\n{out}")
        return out
    return A2.sentence_vi(s, M, planes)


def unit_vi(u, M=None, planes=None):
    M = M or A.AYATANA
    if (out := cut_pair_q(u, M)) is not None:
        return out
    if u in CLOSING or (u[:1].isupper() and u.endswith(".") and not u.startswith("(") and "…" not in u):
        try:
            return sentence_vi(u, M, planes)
        except ValueError:
            pass
    return A2.unit_vi(u, M, planes)


def units_vi(piece, M=None, planes=None):
    units = [x for x in re.split(r"(?<=[.?]) (?=\S)", piece.strip()) if x]
    return " ".join(unit_vi(x, M, planes) for x in units)


def line_vi(body, M=None, planes=None):
    """A line holding a cut pair question (CUTQ_RE) is split into units here; any other cut line goes to 3-02's
    line_vi (3-01's piece splitter); a line without cuts is a run of units."""
    M = M or A.AYATANA
    units = [x for x in re.split(r"(?<=[.?]) (?=\S)", body.strip()) if x]
    if any(CUTQ_RE.fullmatch(x) for x in units):
        return " ".join(unit_vi(x, M, planes) for x in units)
    if "…" in body:
        return A2.line_vi(body, M, planes)
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
# 4. Checks
# ===============================================================================================================
def check_frames():
    assert D.NIRODHAVARO_CLOSE == cap(B.NIRODHAVARO) + "."                 # same shape as UPPADAVARO_CLOSE
    assert KHI_UPAPAJJANTA.replace(B.PARTICIPLES["upapajjantānaṃ"][0], B.PARTICIPLES["cavantānaṃ"][0]) \
        == D.KHI_CAVANTA
    h = "Pacchimabhavikānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti"
    assert ye_ca_head(h) == A2.ye_ca_head(h) == D.b_head(h, "tesaṃ", PLANES)
    assert ye_ca_head(h + " tesaṃ cavantānaṃ") == A2.ye_ca_head(h + " tesaṃ cavantānaṃ")
    full = B.b_q("Kha", "yassa", "tassa", "A", "V", "B", "W", other=True)
    assert cut_pair_q("(Kha) yassa vā pana…pe… uppajjitthāti?") == \
        full.split(" A V")[0] + S.PE + " " + B.verb("uppajjittha")[0] + " không?"
    print(f"ye-ca heads joined flat: {len(YE_FLAT)}")


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

    out += [f"# pi-6 rails {N} (Āyatanayamaka 3): present-future and past-future tenses on the 3-02 Āyatana chain", "",
            "Builder: build_rails_3-03_vi.py (import with importlib). Members, attributes, heads, labels and all "
            "frames are 3-02's / 3-01's (on 2-01 / 7-01 / 2-02). New here, exposed for 3-04 … 3-06: "
            "`KHI_UPAPAJJANTA`, `YE_TAILS`, `flat_persons`, `ye_ca_head`, `b_sentence`, `CUTQ_RE`, `cut_pair_q`, "
            "`UPPADAVARO_CLOSE`, `CLOSING`, `SLIPS`, `sentence_vi`, `unit_vi`, `units_vi`, `line_vi`, `tr_line`, "
            "`build`. Where 3-02 can build a string, the builder asserts it is 3-02's byte for byte. "
            "Format: Pāli = tiếng Việt.", ""]
    h("'P ye ca … parinibbāyissanti tesaṃ upapajjantānaṃ' heads (new)")
    for hd in ("Pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti "
               "tesaṃ upapajjantānaṃ",
               "Pacchimabhavikānaṃ kāmāvacaraṃ upapajjantānaṃ ye ca rūpāvacaraṃ arūpāvacaraṃ upapajjitvā "
               "parinibbāyissanti tesaṃ upapajjantānaṃ"):
        row(hd + " tesaṃ …", ye_ca_head(hd) + f", {C.THEN} {B.L['tesaṃ']} …")
    row("tesaṃ upapajjantānaṃ (after a ye ca clause)", f"{KHI_UPAPAJJANTA} (= 2-02 tesaṃ cavantānaṃ «{D.KHI_CAVANTA}»)")
    h("'P1 P2 ye ca …' heads: several groups before the ye clause, one flat list (new; 3-02 / 7-01 list rule)")
    for hd in ("Pañcavokāre parinibbantānaṃ arūpe pacchimabhavikānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti "
               "tesaṃ cavantānaṃ",
               "Kāmāvacare parinibbantānaṃ rūpāvacare arūpāvacare pacchimabhavikānaṃ ye ca arūpaṃ upapajjitvā "
               "parinibbāyissanti tesaṃ cavantānaṃ"):
        row(hd + " tesaṃ …", ye_ca_head(hd) + f", {C.THEN} {B.L['tesaṃ']} …")
    out.append("(3-02's ye_ca_head would give «Ở A và B và những người nào …».)")
    h("Pair questions cut by …pe… before the last verb (new)")
    for q in ("(Kha) yassa vā pana…pe… uppajjitthāti?", "Yassa vā pana…pe… uppajjitthāti?",
              "Yassa vā pana dhammāyatanaṃ…pe… uppajjitthāti?", "(Kha) yassa vā pana yattha…pe… uppajjitthāti?"):
        row(q, cut_pair_q(q, M))
    h("Closing line")
    row("Uppādavāro.", UPPADAVARO_CLOSE)
    h("Sample sentences")
    for s in ("Pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti tesaṃ "
              "upapajjantānaṃ tesaṃ cakkhāyatanaṃ uppajjati, no ca tesaṃ sotāyatanaṃ uppajjissati.",
              "Pañcavokāre parinibbantānaṃ arūpe pacchimabhavikānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti "
              "tesaṃ cavantānaṃ tesaṃ cakkhāyatanañca nuppajjati sotāyatanañca nuppajjissati.",
              "Pacchimabhavikānaṃ kāmāvacaraṃ upapajjantānaṃ rūpāvacaraṃ upapajjantānaṃ tesaṃ tattha "
              "cakkhāyatanaṃ uppajjati, no ca tesaṃ tattha ghānāyatanaṃ uppajjissati.",
              "Pañcavokāre parinibbantānaṃ arūpe pacchimabhavikānaṃ asaññasattā cavantānaṃ tesaṃ tattha "
              "rūpāyatanañca nuppajjati manāyatanañca nuppajjissati.",
              "Itaresaṃ pañcavokārānaṃ asaññasattānaṃ tesaṃ tattha rūpāyatanañca uppajjittha dhammāyatanañca "
              "uppajjissati."):
        row(s, sentence_vi(s, M))
    h("Termbase misfits and gaps (for the coordinator)")
    out += [
        "- No new terms: every word of this chapter is in 3-01 / 3-02 / 2-01 / 2-02 (members, attributes, planes, "
        "tenses, short answers Āmantā / Natthi / Uppajjittha).",
        f"- tesaṃ upapajjantānaṃ after a ye-ca clause: built as 2-02's tesaṃ cavantānaṃ «{KHI_UPAPAJJANTA}».",
        "- Several groups before 'ye ca': joined flat with the ye clause («A, B và những người nào …»); 3-02's "
        "ye_ca_head (built for one group) would give «A và B và …». Please align (3-04 … 3-06 will import this).",
        "- Heads with planes joined inside one group plus a further item keep 3-02's string «những người thuộc "
        "kiếp sống cuối cùng trong cõi hình sắc và cõi không hình sắc và chúng sinh Vô Tưởng» (two «và» on two "
        "levels; identical Pāli in 3-02's parser).",
        "",
        "## Slips (rendered as meant or kept; reported)",
        "",
        "- ^6-3-118 «(Ka) yassa =93 yattha …»: «=93» is page-number debris; dropped.",
        "- ^6-3-100 «… tesaṃ tattha manāyatanaṃ nuppajjissati cakkhāyatanañca nuppajjati.» and ^6-3-116 "
        "«… cakkhāyatanañca nuppajjittha dhammāyatanaṃ nuppajjissati.»: «-ñca» missing on one member of the "
        "both-frame; rendered as the both-frame («…, … cũng …»).",
        "- ^6-3-89 «… manāyatanañca uppajjati, dhammāyatanañca uppajjissati.»: the Pāli's comma inside the "
        "both-frame stands where the Vietnamese frame has its comma anyway («…, … cũng sẽ sinh khởi»).",
        "- ^6-3-90, 99, 108, 115 «Yattha … …pe….»: the place sections are cut; «Ở nơi nào mà …» (3-01).",
        "- ^6-3-104 the second question («Yassa vā pana…pe… uppajjitthāti? Āmantā.») stands on the answer line, as "
        "in the Pāli; ^6-3-114 has both questions and both answers on one line: kept.",
        "- Cut lists in the first clause (^6-3-114 «Yassa ghānāyatanaṃ…pe… rūpāyatanaṃ… manāyatanaṃ nuppajjittha "
        "…») rendered in place, as 3-02 ^6-3-80.",
        "",
    ]
    return "\n".join(out)


def main():
    S.check_reused()
    B.check_reused()
    A.check_reused()
    A.check_frames()
    segs = build(CH)
    A2.check_frames()
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


def probe(name=CH):
    for seg in S.segments_of(name):
        for ln in seg:
            try:
                print("OK  ", tr_line(ln))
            except Exception as e:  # noqa: BLE001
                print("FAIL", ln[:160], "\n    ", type(e).__name__, str(e)[:300])


if __name__ == "__main__":
    if sys.argv[1:] == ["probe"]:
        probe()
    else:
        main()
