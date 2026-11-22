"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 10-06 (Indriyayamaka 6: uppādavāra, (3) Anāgatavāro
(Kha) anulomaokāso, (Ga) anulomapuggalokāsā, (Gha) paccanīkapuggalo, (Ṅa) paccanīkaokāso).

Setter: build_rails_10-05_vi (R5), imported READ-ONLY with importlib; through it the very module objects of
10-04 (I4), 10-03 (I3), 10-02 (I2), 10-01 (I), 9-01 (DY), 8 (D8), 6-01 (S6), 5-01 (P5), 3-03 (A3), 3-02 (A2),
3-01 (A), 2-02 (D2), 2-01 (B), 7-01 (C). Every line R5.tr_line parses is asserted byte-identical (and R5 itself
asserts against 10-04 and the head parsers of 9-01 / 10-02 / 10-03 / 5-01 / 6-01 / 3-03 / 2-01).

New here (named constants; later chapters may import them):
  PLANE_ATTR_REL / FEEL_PLANE_RE / ye_clause13 / ye_head13
        "ye ca somanassena rūpāvacaraṃ upapajjitvā parinibbāyissanti" (feeling word BEFORE the plane):
        coordinator rule "plane before attribute" «những người nào sau khi tái sinh vào cõi hình sắc mà có niềm vui
        đi kèm sẽ nhập Niết-bàn trọn vẹn» (= R5.ye_clause12 of the clause without the feeling word, with
        «mà <feeling>» after the plane: asserted)
  answer_head13 / pv_sentence13 / unit13 / line13 / tr_line13 / build13
        R5's chain with answer_head13; a both-frame cut by a stray "." (^6-10-301) is translated as the both-frame
        and split at the same spot («… sẽ sinh khởi. Năng lực niềm vui cũng sẽ sinh khởi.»), never merged.
  SLIPS13 / PUNCT13   Pāli as printed → as parsed (spelling slip / missing comma before "no ca"), reported.
A line, unit or word the parsers cannot place raises ValueError (no silent fallback). Importing writes nothing.

usage: python -I -X utf8 -B build_rails_10-06_vi.py   (probe: … build_rails_10-06_vi.py probe)
"""
import importlib
import re
import sys
import unicodedata

RAILS_DIR = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\rails"
if RAILS_DIR not in sys.path:
    sys.path.insert(0, RAILS_DIR)
import build_rails_sample_vi as S  # noqa: E402  (READ-ONLY)
R5 = importlib.import_module("build_rails_10-05_vi")    # READ-ONLY: the nearest setter
I4, I3, I2, I, A, B, C, DY = R5.I4, R5.I3, R5.I2, R5.I, R5.A, R5.B, R5.C, R5.DY
A2, A3, D2, D8, P5, S6 = R5.A2, R5.A3, R5.D2, R5.D8, R5.P5, R5.S6
I8 = importlib.import_module("build_rails_10-08_vi")    # READ-ONLY: only checked for the same module objects
assert I8.S is S

cap, lc = S.cap, R5.lc
CH = "10-06-indriyayamaka.md"
N = "10-06"
NOTES_MD = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/notes-rails-{N}.md"
ADH_DIR = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/adh-{N}"
M_IND = I.INDRIYA
PLANES = A.PLANES_AY
CHECKED = {"10-05 line": 0, "10-05 ye (feeling dropped)": 0}
OWN_LINES = []          # (block id, Pāli) of lines R5 cannot parse, built here
SLIPS_SEEN = []

# ===============================================================================================================
# 1. A feeling word before the plane: plane first, then «mà <feeling>» (coordinator: plane before attribute)
# ===============================================================================================================
PLANE_ATTR_REL = "mà"
FEEL_PLANE_RE = re.compile(r"\b(" + "|".join(I2.FEEL) + r") (\S+) upapajjitvā")


def ye_clause13(text):
    """Ye … <feeling> <plane-acc …> upapajjitvā … «Những người nào sau khi tái sinh vào cõi X mà <feeling> …»;
    any other Ye-clause = R5.ye_clause12."""
    toks = text.split()
    for i, t in enumerate(toks):
        if t not in I2.FEEL or i + 1 >= len(toks):
            continue
        j, planes = i + 1, []
        while j < len(toks) and (pt := B.plane_tok(toks[j], PLANES)) and pt[1] == "acc":
            planes.append(pt[0])
            j += 1
        if not planes:
            continue
        if j >= len(toks) or toks[j] != "upapajjitvā":
            raise ValueError(f"feeling + plane not followed by upapajjitvā in {text!r}")
        base = R5.ye_clause12(" ".join(toks[:i] + toks[i + 1:]))
        anchor = f"{B.UPAPAJJITVA} vào {B.join_and(PLANES[k][0] for k in planes)}"
        if base.count(anchor) != 1:
            raise ValueError(f"plane phrase not found once in {base!r}")
        out = base.replace(anchor, f"{anchor} {PLANE_ATTR_REL} {I2.feel_vi(t)}")
        CHECKED["10-05 ye (feeling dropped)"] += 1
        return out
    return R5.ye_clause12(text)


def ye_head13(head):
    """R5.ye_head12 with ye_clause13 (same joins: «A và b»; 'P ye ca …' «Ở P và những … nào …»)."""
    if not FEEL_PLANE_RE.search(head):
        return R5.ye_head12(head)
    parts = R5.YE_CA_RE.split(head)
    clauses = [ye_clause13(("Yā " if m.group(0).strip().startswith("yā") else "Ye ") + p)
               for m, p in zip(R5.YE_CA_RE.finditer(head), parts[1:])]
    if head.split()[0] in R5.YE_REL:
        out = f" {D2.AND} ".join([ye_clause13(parts[0])] + [lc(c) for c in clauses])
    else:
        try:
            flat = A3.flat_persons(parts[0], PLANES)
        except ValueError:
            flat = [R5.persons12(parts[0])]
            if f" {C.AND} " in flat[0]:
                raise ValueError(f"«và» inside the persons before 'ye ca': {head!r}")
        out = f"{B.AT} {B.join_and(flat + [lc(c) for c in clauses])}"
    # the same head without its feeling words = R5's head, with «mà <feeling>» removed
    plain = FEEL_PLANE_RE.sub(lambda m: f"{m.group(2)} upapajjitvā", head)
    stripped = out
    for f in I2.FEEL:
        stripped = stripped.replace(f" {PLANE_ATTR_REL} {I2.feel_vi(f)}", "")
    assert stripped == R5.ye_head12(plain), (head, stripped, R5.ye_head12(plain))
    return out


def answer_head13(head, loc):
    if loc != "tattha" and FEEL_PLANE_RE.search(head):
        return ye_head13(head)
    return R5.answer_head12(head, loc)


# ===============================================================================================================
# 2. Sentences, units, lines (R5's chain with answer_head13)
# ===============================================================================================================
SLIPS13 = {   # Pāli as printed → as parsed (plain spelling slip); count = expected occurrences
    "Pacchimacittasamaṅgīna tesaṃ": ("Pacchimacittasamaṅgīnaṃ tesaṃ", 1),
}
PUNCT13 = {   # missing comma before "no ca" (7-05: added); count = expected occurrences
    "na uppajjissati no ca tattha": ("na uppajjissati, no ca tattha", 1),
}
STRAY_RE = re.compile(r"(\S+ñca) (\S+(?: \S+)?)\.")        # "Somanassindriyañca uppajjissati." after a stray "."


def pv_sentence13(s, M=None):
    M = M or M_IND
    if m := I2.NOCA_RE.fullmatch(s):
        head, loc, c1, c2 = m.groups()
        a, v1 = I3.split_mv(c1, M)
        b, v2 = I3.split_mv(c2, M)
        return B.b_noca(answer_head13(head, loc), I2.PRON_FEM.get(loc, loc), a, v1, b, v2)
    if m := I3.NEG_BOTH_RE.fullmatch(s):
        head, loc, c1, v1, c2, v2 = m.groups()
        return B.b_both(answer_head13(head, loc), I2.PRON_FEM.get(loc, loc), M.subj(c1), I3.verb(v1), M.subj(c2),
                        I3.verb(v2))
    return None


def unit13(u, M=None):
    M = M or M_IND
    if (lab := I.ind_mulaka(u, M)) is not None:
        return lab
    if u.endswith("?"):
        return R5.question12(u[:-1], M)
    if u in B.SHORT:
        return B.SHORT[u]
    if (m := I2.CUT_ANS_RE.fullmatch(u)) and m.group(1) + "." in B.SHORT:
        return I2.pv_unit(u, M)
    if "…" in u:
        raise ValueError(f"cut not set in this chapter: {u!r}")
    if (out := pv_sentence13(u, M)) is not None:
        return out
    raise ValueError(f"unknown unit {u!r}")


def stray_pair(u1, u2, M=None):
    """'<head> <loc> Añca V.' + 'Bñca V.' (a both-frame cut by a stray '.'): the both-frame, split at that spot."""
    M = M or M_IND
    m = STRAY_RE.fullmatch(u2)
    if not m or not u2[:1].isupper():
        raise ValueError(f"not the tail of a both-frame {u2!r}")
    joined = pv_sentence13(f"{u1[:-1]} {lc(u2)}", M)
    if joined is None:
        raise ValueError(f"not a both-frame: {u1!r} {u2!r}")
    subj2 = M.subj(lc(m.group(1)))
    cut = f", {subj2} "
    if joined.count(cut) != 1:
        raise ValueError(f"cannot split {joined!r}")
    return joined.replace(cut, f". {cap(subj2)} ")


def line13(body, M=None):
    body, label = body.strip(), None
    if m := re.fullmatch(r"(.+?) (\(\w+mūlakaṃ\)\.?)", body):
        body, label = m.group(1), m.group(2)
    units = [x for x in re.split(r"(?<=[.?]) (?=\S)", body) if x]
    out, i = [], 0
    while i < len(units):
        u = units[i]
        if i + 1 < len(units) and STRAY_RE.fullmatch(units[i + 1]) and units[i + 1][:1].isupper() \
                and not I2.NOCA_RE.fullmatch(units[i + 1]):
            out.append(stray_pair(u, units[i + 1], M))
            SLIPS_SEEN.append(("stray .", units[i + 1]))
            i += 2
            continue
        out.append(unit13(u, M))
        i += 1
    if label:
        out.append(unit13(label, M))
    return " ".join(out)


def tr_line13(p, M=None):
    M = M or M_IND
    m = re.search(r" (\^\S+)$", p)
    bid = m.group(1) if m else None
    body = p[:m.start()] if m else p
    if "[" in body:
        raise ValueError(f"variant bracket not handled: {p!r}")
    if body.startswith("#"):
        hashes, text = body.split(" ", 1)
        out = f"{hashes} {I2.heading(text)}"
    else:
        for table, kind in ((SLIPS13, "slip"), (PUNCT13, "comma")):
            for bad, (good, _) in table.items():
                if bad in body:
                    SLIPS_SEEN.append((kind, bid, bad, good))
                    body = body.replace(bad, good)
        out = line13(body, M)
    full = f"{out} {bid}" if bid else out
    try:
        old = R5.tr_line(p, M)
    except (ValueError, KeyError):
        old = None
        OWN_LINES.append((bid, p))
    if old is not None:
        assert old == full, ("10-05 line", p, old, full)
        CHECKED["10-05 line"] += 1
    return full


def build13(name=CH, M=None):
    return [[tr_line13(ln, M) for ln in seg] for seg in S.segments_of(name)]


# ===============================================================================================================
# 3. Checks
# ===============================================================================================================
def check_frames():
    h = "Pacchimabhavikānaṃ ye ca somanassena rūpāvacaraṃ upapajjitvā parinibbāyissanti"
    want = ("Ở những người thuộc kiếp sống cuối cùng và những người nào sau khi tái sinh vào cõi hình sắc mà có niềm "
            "vui đi kèm sẽ nhập Niết-bàn trọn vẹn")
    assert answer_head13(h, "tesaṃ") == want, answer_head13(h, "tesaṃ")
    assert R5.answer_head12(h.replace("somanassena ", ""), "tesaṃ") == want.replace(" mà có niềm vui đi kèm", "")
    assert answer_head13("Pacchimabhavikānaṃ", "tesaṃ") == R5.answer_head12("Pacchimabhavikānaṃ", "tesaṃ")
    assert S.LABEL["Ṅa"] == "(đ)" and S.LABEL["Gha"] == "(d)" and S.LABEL["Kha"] == "(b)"


# ===============================================================================================================
# 4. Notes file (Pāli = tiếng Việt)
# ===============================================================================================================
def notes():
    M = M_IND
    out = []

    def row(p, v):
        out.append(f"{p} = {v}")

    def h(t):
        out.extend(["", f"## {t}", ""])

    out += [f"# pi-6 rails {N} (Indriyayamaka 6): (3) Anāgatavāro (Kha) anulomaokāso … (Ṅa) paccanīkaokāso", "",
            "Builder: build_rails_10-06_vi.py (import with importlib). Setter: build_rails_10-05_vi (R5; READ-ONLY), "
            "and through it 10-04, 10-03, 10-02, 10-01, 9-01, 8, 6-01, 5-01, 3-03, 3-02, 3-01, 2-02, 2-01, 7-01 "
            "(the same module objects). Every line R5.tr_line parses is asserted byte-identical "
            f"({CHECKED['10-05 line']} lines); the {len(OWN_LINES)} lines it cannot parse are built here from R5's "
            "functions. Exposed: `PLANE_ATTR_REL`, `FEEL_PLANE_RE`, `ye_clause13`, `ye_head13`, `answer_head13`, "
            "`pv_sentence13`, `unit13`, `stray_pair`, `line13`, `tr_line13`, `build13`, `SLIPS13`, `PUNCT13`. "
            "Format: Pāli = tiếng Việt.", ""]
    h("Headings")
    for t in ("(Kha) anulomaokāso", "(Ga) anulomapuggalokāsā", "(Gha) paccanīkapuggalo", "(Ṅa) paccanīkaokāso"):
        row(t, I2.heading(t))
    h("New: a feeling word before the plane (coordinator rule: plane before attribute, «mà»)")
    for hd in ("Pacchimabhavikānaṃ ye ca somanassena rūpāvacaraṃ upapajjitvā parinibbāyissanti",):
        row(f"{hd} tesaṃ …", f"{answer_head13(hd, 'tesaṃ')}, {C.THEN} {B.L['tesaṃ']} …")
    row("ye ca somanassena rūpāvacaraṃ upapajjitvā parinibbāyissanti",
        lc(ye_clause13("Ye somanassena rūpāvacaraṃ upapajjitvā parinibbāyissanti")))
    h("Heads new in this chapter (all from R5 / its setters)")
    for hd, loc in (("Yassa cittassa anantarā upekkhāsampayuttapacchimacittaṃ uppajjissati asaññasattānaṃ", "tesaṃ tattha"),
                    ("Yassa cittassa anantarā somanassasampayuttapacchimacittaṃ uppajjissati", "tesaṃ tattha"),
                    ("Itaresaṃ kāmāvacarānaṃ", "tesaṃ tattha"), ("Itaresaṃ pañcavokārānaṃ", "tesaṃ tattha"),
                    ("Asaññasattānaṃ arūpānaṃ", "tesaṃ tattha"), ("Pañcavokārānaṃ", "tesaṃ tattha"),
                    ("Rūpāvacarānaṃ yā ca itthiyo eteneva bhāvena katici bhave dassetvā somanassena upapajjitvā "
                     "parinibbāyissanti", "tesaṃ tattha"),
                    ("Rūpāvacarānaṃ arūpāvacarānaṃ ye ca purisā eteneva bhāvena katici bhave dassetvā "
                     "parinibbāyissanti", "tesaṃ tattha"),
                    ("Ye rūpāvacaraṃ upapajjitvā parinibbāyissanti ye ca purisā eteneva bhāvena katici bhave dassetvā "
                     "somanassena upapajjitvā parinibbāyissanti", "tesaṃ"),
                    ("Pacchimabhavikānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti ye ca purisā eteneva bhāvena katici "
                     "bhave dassetvā upekkhāya upapajjitvā parinibbāyissanti", "tesaṃ"),
                    ("Pacchimabhavikānaṃ ye ca rūpāvacaraṃ arūpāvacaraṃ upapajjitvā parinibbāyissanti", "tesaṃ"),
                    ("Pacchimacittasamaṅgīnaṃ", "tesaṃ"),
                    ("Asaññasatte arūpe", "tattha"), ("Catuvokāre pañcavokāre", "tattha"),
                    ("Rūpāvacare arūpāvacare", "tattha")):
        row(f"{hd} {loc} …", f"{answer_head13(hd, loc)}, {C.THEN} {B.L[loc]} …")
    h("Sample lines")
    for s in ("(Ka) yattha cakkhundriyaṃ uppajjissati tattha sotindriyaṃ uppajjissatīti? Āmantā.",
              "Yattha cakkhundriyaṃ uppajjissati tattha itthindriyaṃ…pe… purisindriyaṃ uppajjissatīti?",
              "(Ka) yassa cakkhundriyaṃ na uppajjissati tassa sotindriyaṃ na uppajjissatīti? Āmantā.",
              "(Ka) yattha cakkhundriyaṃ na uppajjissati tattha jīvitindriyaṃ na uppajjissatīti? Uppajjissati.",
              "(Kha) yattha vā pana jīvitindriyaṃ na uppajjissati tattha cakkhundriyaṃ na uppajjissatīti? Natthi.",
              "Ye rūpāvacaraṃ upapajjitvā parinibbāyissanti tesaṃ ghānindriyaṃ na uppajjissati, no ca tesaṃ "
              "cakkhundriyaṃ na uppajjissati.",
              "Pacchimacittasamaṅgīnaṃ tesaṃ somanassindriyañca na uppajjissati jīvitindriyañca na uppajjissati.",
              "Itaresaṃ kāmāvacarānaṃ tesaṃ tattha itthindriyañca uppajjissati. Somanassindriyañca uppajjissati.",
              "Rūpāvacare arūpāvacare tattha ghānindriyaṃ na uppajjissati, no ca tattha upekkhindriyaṃ na "
              "uppajjissati."):
        row(s, line13(s, M))
    h("Termbase misfits and gaps (for the coordinator)")
    out += [
        "- No new terms. somanassena / upekkhāya «có niềm vui / có sự bình thản đi kèm» (termbase, 10-02); with a plane "
        "AFTER it in the Pāli (^6-10-309 «ye ca somanassena rūpāvacaraṃ upapajjitvā …», twice) the plane comes first "
        "and the feeling follows with «mà» (coordinator rule «sau khi tái sinh vào cõi X mà <attribute> …»): "
        "«những người nào sau khi tái sinh vào cõi hình sắc mà có niềm vui đi kèm sẽ nhập Niết-bàn trọn vẹn». First "
        "use of this shape in the rails: please confirm. (10-05's ye_clause12 order plane + feeling, without «mà», "
        "never occurs in 10-05 / 10-06.)",
        "- Termbase adherence: 12 misses, all setter forms (Itaresaṃ kāmāvacarānaṃ / pañcavokārānaṃ «chúng sinh khác "
        "trong cõi …», 10-05; catuvokārānaṃ pañcavokārānaṃ «chúng sinh trong cõi gồm bốn khối và cõi gồm năm khối», "
        "one «chúng sinh» per run, 3-02 / 10-02): not changed.",
        "",
        "## Open item kept as the setters print it (for the consistency pass)",
        "",
        "- «Rūpāvacarānaṃ arūpāvacarānaṃ ye ca purisā / yā ca itthiyo …» = «Ở chúng sinh trong cõi hình sắc và cõi "
        "không hình sắc và những người nam / nữ nào …» (two «và»: 3-03 flat_persons keeps a one-run plane list whole; "
        "the 6-01 open item; 10-05 / 3-03 … 3-06 / 6-0x print it the same; R5 asserts it equal to 3-03): ^6-10-301, "
        "^6-10-302 (six lines).",
        "",
        "## Pāli as written (reported)",
        "",
        "- ^6-10-301 «… tesaṃ tattha itthindriyañca uppajjissati. Somanassindriyañca uppajjissati.» (a stray "
        "full stop inside the both-frame): translated as the both-frame and split at the same spot, «…, thì ở những "
        "người ấy, ở nơi ấy năng lực nữ tính sẽ sinh khởi. Năng lực niềm vui cũng sẽ sinh khởi.» (two sentences kept).",
        "- ^6-10-314 «Pacchimacittasamaṅgīna tesaṃ» (for Pacchimacittasamaṅgīnaṃ): spelling slip, rendered as meant "
        "«Ở những người có được tâm cuối cùng».",
        "- ^6-10-318 «… ghānindriyaṃ na uppajjissati no ca tattha …» (no comma before no ca): comma added (7-05).",
        "- ^6-10-309 «somanassindriyaṃ na upapajjissati» (for uppajjissati; coordinator: «sẽ sinh khởi»): after no ca "
        "«vẫn sẽ sinh khởi», as R5 / 10-03's verb table gives it.",
        "- ^6-10-293 «(Kha) yattha purisindriyaṃ uppajjissati tattha upekkhindriyaṃ uppajjissatīti?» is labelled (Kha) "
        "for (Ka); the next line is (Kha) too: both kept «(b)» as written.",
        "- ^6-10-292, ^6-10-319 «Āmantā …pe….» = «Đúng vậy …» (10-02 pv_unit).",
        "- Unlabelled pairs and pairs whose (Kha) stands without a (Ka) (^6-10-308 / 309 / 310 …) are kept as written.",
        "",
    ]
    return "\n".join(out)


def main():
    S.check_reused()
    B.check_reused()
    A.check_reused()
    I.check_reused()
    I.check_frames()
    I2.check_reused()
    I2.check_frames()
    I3.check_frames()
    I4.check_frames()
    R5.check_frames()
    R5.check_termbase()
    check_frames()
    segs = build13(CH)
    for table, kind in ((SLIPS13, "slip"), (PUNCT13, "comma")):
        for bad, (_, n) in table.items():
            got = sum(1 for s in SLIPS_SEEN if s[0] == kind and s[2] == bad)
            assert got == n, (bad, got, n)
    assert sum(1 for s in SLIPS_SEEN if s[0] == "stray .") == 1, SLIPS_SEEN
    S.write(CH, segs)
    text = (S.OUT_DIR / CH).read_text(encoding="utf-8")
    ADH_DIR.mkdir(parents=True, exist_ok=True)
    (ADH_DIR / CH).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", ADH_DIR / CH)
    NOTES_MD.write_text(unicodedata.normalize("NFC", notes()), encoding="utf-8", newline="\n")
    print("wrote", NOTES_MD)
    print("checked equal:", CHECKED, "; own lines:", [b for b, _ in OWN_LINES], "; slips:", SLIPS_SEEN)


def probe(name=CH):
    for seg in S.segments_of(name):
        for ln in seg:
            try:
                print("OK  ", tr_line13(ln))
            except Exception as e:  # noqa: BLE001
                print("FAIL", ln[:220], "\n    ", type(e).__name__, str(e)[:300])


if __name__ == "__main__":
    if sys.argv[1:] == ["probe"]:
        probe()
    else:
        main()
