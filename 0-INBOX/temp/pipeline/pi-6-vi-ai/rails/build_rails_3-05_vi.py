"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 3-05 (Āyatanayamaka, part 5: nirodhavāra present-future and
past-future, uppādanirodhavāra present and past).

Everything comes from the Āyatana chain build_rails_3-04_vi → build_rails_3-03_vi → build_rails_3-02_vi →
build_rails_3-01_vi → build_rails_2-01_vi / build_rails_7-01_vi (+ build_rails_2-02_vi, build_rails_4_vi,
build_rails_5-01_vi for the note wording), all imported READ-ONLY. This file adds, for 3-06:

  CUTQD_RE / cut_q_dot        a pair question cut by …pe… with no verb and no «?» ("(Kha) yassa vā pana [yattha]
                              A…pe…."): 3-04 cut_q0 without «không?», ending «…» (coordinator: a cut line ending
                              "…pe…." without "?" ends «…»)
  FRAG_RE / loc_fragment      an answer cut after "<persons> tesaṃ [tattha]" («Ở <persons>, thì ở những người ấy[, ở
                              nơi ấy]…»; = rails 8 / 5-02 «…, thì ở những người ấy…»), asserted to be the head of
                              the full family-B answer
  frag_line                   a line of such fragments, optionally after a question
  NOTES_3_05                  this chapter's editorial notes (yathā … tividhaṃ …, yatthakaṃ noti …, Yassakampi
                              yassayatthakampi sadisaṃ, Atītā pucchā …)
  sentence_vi / unit_vi / line_vi / tr_line / build   3-04's chain with the pieces above
A line, unit or word the parsers cannot place raises ValueError (no silent fallback). Importing writes nothing.

    A5 = importlib.import_module("build_rails_3-05_vi"); segs = A5.build("3-06-ayatanayamaka.md", fixed=…)

usage: python -I -X utf8 -B build_rails_3-05_vi.py   (probe: … build_rails_3-05_vi.py probe)
"""
import importlib
import re
import sys
import unicodedata

RAILS_DIR = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\rails"
if RAILS_DIR not in sys.path:
    sys.path.insert(0, RAILS_DIR)
import build_rails_sample_vi as S  # noqa: E402  (READ-ONLY)
A4 = importlib.import_module("build_rails_3-04_vi")  # READ-ONLY: nirodhavāra frames, cut questions, notes
A3 = A4.A3                                            # build_rails_3-03_vi (READ-ONLY)
A2 = A4.A2                                            # build_rails_3-02_vi (READ-ONLY)
A = A4.A                                              # build_rails_3-01_vi (READ-ONLY)
B = A4.B                                              # build_rails_2-01_vi (READ-ONLY)
C = A4.C                                              # build_rails_7-01_vi (READ-ONLY)
D = A4.D                                              # build_rails_2-02_vi (READ-ONLY)
G = A4.G                                              # build_rails_4_vi (READ-ONLY)
E = importlib.import_module("build_rails_5-01_vi")   # READ-ONLY: Yassakampi yassayatthakampi note, sadisaṃ kātabbaṃ

cap = S.cap
CH = "3-05-ayatanayamaka.md"
N = "3-05"
NOTES_MD = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/notes-rails-{N}.md"
ADH_DIR = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/adh-{N}"
SLIPS_SEEN = []
PLANES = A.PLANES_AY
LAB = A.LAB

# ===============================================================================================================
# 1. Pair questions cut by …pe… with no verb and no «?»
# ===============================================================================================================
CUTQD_RE = re.compile(r"((?:" + LAB + r" )?[Yy]assa(?: vā pana)?(?: yattha)?(?: \S+)?)…pe…")


def cut_q_dot(q, M=None):
    """'(Kha) yassa vā pana [yattha] [A]…pe…' (the line's «.» already cut off) → 3-04 cut_q0 without «không?»:
    «(b) Còn ở người nào[, ở nơi nào] mà lĩnh vực mũi…»."""
    M = M or A.AYATANA
    if not CUTQD_RE.fullmatch(q):
        return None
    full = A4.cut_q0(q + "?", M)
    assert full is not None and full.endswith(S.PE + " không?"), (q, full)
    return full[: -len(" không?")]


# ===============================================================================================================
# 2. Answers cut after their person head and its tesaṃ [tattha]
# ===============================================================================================================
FRAG_RE = re.compile(r"(.+?) " + A.LOC)


def loc_fragment(piece, planes=None):
    """'<persons> tesaṃ [tattha]' → «Ở <persons>, thì ở những người ấy[, ở nơi ấy]» (3-02 answer_head, 7-01 THEN,
    2-01 L). The result is asserted to be the head of the full family-B answer with the same persons."""
    m = FRAG_RE.fullmatch(piece)
    if not m:
        return None
    head, loc = m.groups()
    try:
        A2.ay_person_items(head, planes or PLANES)
    except ValueError:
        return None
    out = f"{A2.answer_head(head, loc, planes)}, {C.THEN} {B.L[loc]}"
    probe = f"{head} {loc} cakkhāyatanaṃ nirujjhati, no ca {loc} sotāyatanaṃ nirujjhissati."
    assert A4.sentence_vi(probe).startswith(out + " "), (piece, out)
    return out


def frag_line(body, M=None, planes=None):
    """'[<question>? ]<persons> tesaṃ [tattha]…pe…[ <persons> tesaṃ [tattha]…pe…].' → «[<question> ]<fragment>…
    [<fragment>…]» (the cut's «.» absorbed; a lower-case Pāli head keeps a lower-case «ở»). None if not this shape."""
    M = M or A.AYATANA
    if not body.endswith("…pe…."):
        return None
    q, rest = "", body[:-1]
    if "? " in rest:
        q, rest = rest.split("? ", 1)
        q += "?"
        if "?" in rest:
            return None
    pieces = rest.split("…pe…")
    if pieces[-1].strip() or len(pieces) < 2:
        return None
    outs = []
    for p in pieces[:-1]:
        p = p.strip()
        lower = p[:1].islower()
        f = loc_fragment(cap(p) if lower else p, planes)
        if f is None:
            return None
        outs.append((f[:1].lower() + f[1:] if lower else f) + S.PE)
    vi = " ".join(outs)
    return f"{A4.unit_vi(q, M, planes)} {vi}" if q else vi


# ===============================================================================================================
# 3. Editorial notes of this chapter
# ===============================================================================================================
P_PERSON, P_PLACE, P_PERSON_PLACE = A4.P_PERSON, A4.P_PLACE, A4.P_PERSON_PLACE
assert (P_PERSON, P_PLACE, P_PERSON_PLACE) == (E.P_PERSON, E.P_PLACE, E.P_PERSON_PLACE)
VITTHARITA = A4.VITTHARITA                       # vitthāritaṃ «đã được trình bày chi tiết» (3-04)
THREEFOLD = "theo ba cách"                       # tividhaṃ (no entry; reported)
THIS_PART = "phần này"                           # idampi (+ G.DETAILED's «cũng»)
NO_WORD = f"“{C.ANS_NO[:-1]}”"                  # noti: the answer No. «Không.» (7-01) quoted as a word
NOT_TO_MAKE = f"không {A.SHOULD} trả lời là"     # X-ti na kātabbaṃ (3-01 "āmantāti kātabbaṃ" «nên trả lời là “Đúng vậy”»)
SADISAM_KATABBAM = E.SADISAM_KATABBAM            # X-sadisaṃ kātabbaṃ «nên được làm cho giống như» (5-01)
OTHER_PLACE_PARTS = f"các {P_PLACE} khác"         # itaresaṃ yatthakānaṃ
ALL_THREE_VARAS = "ở cả ba mục"                  # tīsupi vāresu (vāra «mục»)
NOTE_YASSAKA_SADISA = E.NOTE_YASSAKA.replace(f" {E.VITTHARETABBAM} ", " ")   # = 5-01's note minus vitthāretabbaṃ
assert NOTE_YASSAKA_SADISA == f"(Cả {P_PERSON} lẫn {P_PERSON_PLACE} đều giống nhau)."
_AT_ALL = ", ".join(f"{C.AT} {x}" for x in (A4.UPPADE, A4.NIRODHE, A4.UPPADANIRODHE))
NOTES_3_05 = {
    "(yathā paccuppannātītepi tividhaṃ vitthāritaṃ evaṃ idampi vitthāretabbaṃ).":
        (f"(như {C.AT} {B.TIME['Paccuppannātīta']} {C.ALSO} {VITTHARITA} {THREEFOLD}, {THIS_PART} "
         f"{G.DETAILED})."),
    "(yatthakaṃ noti na kātabbaṃ, yatthakaṃ itaresaṃ yatthakānaṃ sadisaṃ kātabbaṃ, yatthakaṃ tīsupi vāresu "
    "sadisaṃ).":
        (f"({C.AT} {P_PLACE} {NOT_TO_MAKE} {NO_WORD}, {P_PLACE} {SADISAM_KATABBAM} {OTHER_PLACE_PARTS}, "
         f"{P_PLACE} {ALL_THREE_VARAS} đều {A2.SADISA})."),
    "(Yassakampi yassayatthakampi sadisaṃ).": NOTE_YASSAKA_SADISA,
    "(Atītā pucchā uppādepi nirodhepi uppādanirodhepi anulomampi paccanīkampi sadisaṃ).":
        (f"({cap(A4.PUCCHA)} về {B.TIME['Atīta']} {_AT_ALL}, theo {A4.ANULOMA} và {A4.PACCANIKA} "
         f"đều {A2.SADISA})."),
}
CLOSING = {"Nirodhavāro.": D.NIRODHAVARO_CLOSE}   # «Mục về sự chấm dứt.» (2-02)

SLIPS = dict(A4.SLIPS)
SLIPS.update({   # plain slips and punctuation, rendered as meant (reported)
    "parinibbāntānaṃ": "parinibbantānaṃ",                                         # ^6-3-172 long ā
    "manāyatana…pe…": "manāyatanaṃ…pe…",                                          # ^6-3-186 ṃ missing
    "manāyatanañca na nirujjhissati, cakkhāyatanañca na nirujjhittha.":
        "manāyatanañca na nirujjhissati cakkhāyatanañca na nirujjhittha.",       # ^6-3-195 comma (= «, … cũng …»)
})


# ===============================================================================================================
# 4. Units and lines (3-04's chain)
# ===============================================================================================================
NOTE_TAIL_RE = re.compile(r"(.*?) (\([^()]*\)\.)")


def sentence_vi(s, M=None, planes=None):
    M = M or A.AYATANA
    if s in NOTES_3_05:
        return NOTES_3_05[s]
    if s in CLOSING:
        return CLOSING[s]
    return A4.sentence_vi(s, M, planes)


def unit_vi(u, M=None, planes=None):
    M = M or A.AYATANA
    if u in NOTES_3_05:
        return NOTES_3_05[u]
    if u in CLOSING:
        return CLOSING[u]
    return A4.unit_vi(u, M, planes)


def line_vi(body, M=None, planes=None):
    M = M or A.AYATANA
    if body in NOTES_3_05 or body in CLOSING:
        return unit_vi(body, M, planes)
    if (m := NOTE_TAIL_RE.fullmatch(body)) and m.group(2) in NOTES_3_05:   # '<line> (note).'
        head, note = m.groups()
        if (q := cut_q_dot(head, M)) is not None:
            return f"{q} {NOTES_3_05[note]}"
        return f"{line_vi(head, M, planes)} {NOTES_3_05[note]}"
    if body.endswith("…pe…") and (q := cut_q_dot(body, M)) is not None:   # a line ending in the bare cut
        return q
    if body.endswith("…pe….") and (q := cut_q_dot(body[:-1], M)) is not None:
        return q
    if (out := frag_line(body, M, planes)) is not None:
        return out
    return A4.line_vi(body, M, planes)


def tr_line(p, M=None, fixed=None, variant_kind=None, planes=None, yamaka=A.YAMAKA):
    M = M or A.AYATANA
    m = re.search(r" (\^\S+)$", p)
    bid = m.group(1) if m else None
    body = p[:m.start()] if m else p
    fixed = fixed or {}
    variant_kind = {**A4.VARIANTS_3_04, **(variant_kind or {})}
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
# 5. Checks
# ===============================================================================================================
def check_frames():
    M = A.AYATANA
    # the dot-cut question = 3-04's cut question without «không?»
    for q in ("(Kha) yassa vā pana ghānāyatanaṃ…pe…", "(Kha) yassa vā pana yattha manāyatanaṃ…pe…",
              "Yassa vā pana dhammāyatanaṃ…pe…"):
        assert cut_q_dot(q, M) + " không?" == A4.cut_q0(q + "?", M), q
    # the fragment = the head of the full answer (asserted inside loc_fragment) and rails 8's «…, thì ở những người ấy…»
    f = loc_fragment("Sacakkhukānaṃ cavantānaṃ tesaṃ")
    assert f.endswith(f", {C.THEN} {B.L['tesaṃ']}") and B.L["tesaṃ"] == "ở những người ấy", f
    # the dropped comma (^6-3-195) gives the both-frame's own comma
    s = ("Suddhāvāse parinibbantānaṃ arūpe parinibbantānaṃ asaññasattānaṃ tesaṃ tattha manāyatanañca na "
         "nirujjhissati cakkhāyatanañca na nirujjhittha.")
    assert ", lĩnh vực mắt cũng chưa từng chấm dứt." in A4.sentence_vi(s, M), A4.sentence_vi(s, M)
    assert D.NIRODHAVARO_CLOSE == cap(B.NIRODHAVARO) + "."
    assert NO_WORD == "“Không”", NO_WORD


# ===============================================================================================================
# 6. Notes file (Pāli = tiếng Việt)
# ===============================================================================================================
def notes():
    M = A.AYATANA
    out = []

    def row(p, v):
        out.append(f"{p} = {v}")

    def h(t):
        out.extend(["", f"## {t}", ""])

    out += [f"# pi-6 rails {N} (Āyatanayamaka 5): nirodhavāra (present-future, past-future) and uppādanirodhavāra "
            "(present, past) on the 3-04 Āyatana chain", "",
            "Builder: build_rails_3-05_vi.py (import with importlib). Members, attributes, heads, labels, verbs and "
            "all answer frames are 3-04's / 3-03's / 3-02's / 3-01's (on 2-01 / 7-01 / 2-02); the mixed "
            "uppajjati / nirujjhati answers are 2-01's VERB_TABLE in 3-04's frames («lĩnh vực mắt không sinh khởi, "
            "nhưng ở những người ấy lĩnh vực tai vẫn chấm dứt»). New here, exposed for 3-06: `CUTQD_RE`, "
            "`cut_q_dot`, `FRAG_RE`, `loc_fragment`, `frag_line`, `NOTES_3_05` (pieces `THREEFOLD`, `THIS_PART`, "
            "`NO_WORD`, `NOT_TO_MAKE`, `OTHER_PLACE_PARTS`, `ALL_THREE_VARAS`, `NOTE_YASSAKA_SADISA`), `CLOSING`, "
            "`SLIPS`, `sentence_vi`, `unit_vi`, `line_vi`, `tr_line`, `build`. Format: Pāli = tiếng Việt.", ""]
    h("Pair questions cut by …pe… with no verb and no «?» (new; 3-04 cut_q0 without «không?»)")
    for q in ("(Kha) yassa vā pana ghānāyatanaṃ…pe….", "(Kha) yassa vā pana yattha manāyatanaṃ…pe….",
              "Yassa vā pana dhammāyatanaṃ…pe…."):
        row(q, line_vi(q, M))
    h("Answers cut after '<persons> tesaṃ [tattha]' (new; = rails 8 «…, thì ở những người ấy…»)")
    for ln in ("Sabbesaṃ upapajjantānaṃ acakkhukānaṃ cavantānaṃ tesaṃ…pe… sacakkhukānaṃ cavantānaṃ tesaṃ…pe….",
               "Kāmāvacaraṃ upapajjantānaṃ aghānakānaṃ kāmāvacarā cavantānaṃ rūpāvacarānaṃ tesaṃ tattha…pe…."):
        row(ln, line_vi(ln, M))
    h("Mixed uppāda / nirodha answers (all 3-04 / 3-03 frames)")
    for s in ("Sasotakānaṃ cavantānaṃ tesaṃ cakkhāyatanaṃ nuppajjati, no ca tesaṃ sotāyatanaṃ na nirujjhati.",
              "Acakkhukānaṃ upapajjantānaṃ asotakānaṃ cavantānaṃ tesaṃ cakkhāyatanañca nuppajjati sotāyatanañca na "
              "nirujjhati.",
              "Sacakkhukānaṃ upapajjantānaṃ tesaṃ sotāyatanaṃ na nirujjhati, no ca tesaṃ cakkhāyatanaṃ nuppajjati."):
        row(s, sentence_vi(s, M))
    h("Other answer shapes of this chapter (3-04 / 3-03 / 3-02)")
    for s in ("Pañcavokāre parinibbantānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ tesaṃ "
              "cakkhāyatanaṃ nirujjhati, no ca tesaṃ sotāyatanaṃ nirujjhissati.",
              "Pacchimabhavikānaṃ rūpāvacaraṃ upapajjantānaṃ arūpe pacchimabhavikānaṃ tesaṃ cakkhāyatanañca na "
              "nirujjhati ghānāyatanañca na nirujjhissati.",
              "Suddhāvāsaṃ upapajjantānaṃ tesaṃ tattha sotāyatanaṃ nirujjhissati, no ca tesaṃ tattha "
              "cakkhāyatanaṃ nirujjhittha."):
        row(s, sentence_vi(s, M))
    for q in ("(Ka) yassa manāyatanaṃ na nirujjhati tassa dhammāyatanaṃ na nirujjhissatīti? Nirujjhissati.",
              "(Kha) yassa vā pana dhammāyatanaṃ na nirujjhissati tassa manāyatanaṃ na nirujjhatīti? Nirujjhati."):
        row(q, line_vi(q, M))
    h("Closing line and editorial notes (new)")
    for p, v in CLOSING.items():
        row(p, v)
    for p, v in NOTES_3_05.items():
        row(p, v)
    row("tividhaṃ / idampi / noti / na kātabbaṃ / itaresaṃ yatthakānaṃ / tīsupi vāresu",
        f"{THREEFOLD} / {THIS_PART} (+ «cũng») / {NO_WORD} / {NOT_TO_MAKE} / {OTHER_PLACE_PARTS} / "
        f"{ALL_THREE_VARAS}")
    h("Termbase misfits and gaps (for the coordinator)")
    out += [
        "- No new member, person, plane or verb words: all from 3-01 … 3-04 / 2-01.",
        f"- tividhaṃ (no entry): «{THREEFOLD}»; idampi «{THIS_PART} … cũng»; paccuppannātītepi «ở hiện tại và quá "
        "khứ cũng» (3-01 note wording, no «mục về»: the Pāli has no vāra).",
        f"- yatthakaṃ noti na kātabbaṃ: «{C.AT} {P_PLACE} {NOT_TO_MAKE} {NO_WORD}» (3-01's «… nên trả lời là "
        "“Đúng vậy”» for āmantāti kātabbaṃ, negated; the answer No. «Không.» (7-01) quoted as a word; «ở» added "
        "since a section does not answer); sadisaṃ kātabbaṃ with a genitive «nên được làm cho "
        "giống như» (5-01); tīsupi vāresu «ở cả ba mục».",
        f"- (Yassakampi yassayatthakampi sadisaṃ): 5-01's «{E.NOTE_YASSAKA}» minus vitthāretabbaṃ.",
        "- Atītā pucchā … anulomampi paccanīkampi sadisaṃ: 3-04's pieces in the Pāli's order.",
        "",
        "## Slips and unsure Pāli (rendered as meant or kept; reported)",
        "",
        "- ^6-3-172 «parinibbāntānaṃ»: read «parinibbantānaṃ».",
        "- ^6-3-186 «manāyatana…pe…»: «ṃ» missing; read «manāyatanaṃ».",
        "- ^6-3-195 «… manāyatanañca na nirujjhissati, cakkhāyatanañca na nirujjhittha.»: the comma inside the "
        "both-frame stands where the Vietnamese frame has its comma anyway (as 3-03 ^6-3-89).",
        "- ^6-3-172 the (Kha) question about rūpa / ghāna has a cut answer «Kāmāvacare parinibbantānaṃ tesaṃ "
        "tattha…pe….» on the question line and «Kāmāvacaraṃ upapajjantānaṃ aghānakānaṃ kāmāvacarā cavantānaṃ "
        "rūpāvacarānaṃ tesaṃ tattha…pe….» on the next: translated as written (the first head looks like the one "
        "of the (Ka) answer; not emended).",
        "- ^6-3-166, 167, 172 and the (Kha) lines of ^6-3-171 / 173 «(Kha) yassa vā pana [yattha] X…pe….»: cut "
        "before the verb, no «?»; rendered «(b) Còn ở người nào[, ở nơi nào] mà X…».",
        "- ^6-3-194 «Yassa cakkhāyatanaṃ na nirujjhittha…pe….» heads the paccanīkaokāsa (place) section with "
        "«Yassa» (person): translated as written («Ở người nào mà …»).",
        "- ^6-3-170, 179, 188, 201, 208 «Yattha … …pe….»: place sections cut; «Ở nơi nào mà …» (3-01).",
        "- ^6-3-198 «Nirodhavāro.» closes the nirodhavāra: «Mục về sự chấm dứt.» (2-02).",
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
                print("FAIL", ln[:200], "\n    ", type(e).__name__, str(e)[:300])


if __name__ == "__main__":
    if sys.argv[1:] == ["probe"]:
        probe()
    else:
        main()
