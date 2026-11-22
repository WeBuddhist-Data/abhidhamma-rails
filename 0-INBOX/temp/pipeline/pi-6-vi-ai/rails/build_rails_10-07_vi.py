"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 10-07 (Indriyayamaka 7: uppādavāra, (3) Anāgatavāro,
(Ca) paccanīkapuggalokāsā).

Setter: build_rails_10-05_vi (I5), imported READ-ONLY with importlib; through it the very module objects of
10-04 (I4), 10-03 (I3), 10-02 (I2), 10-01 (I), 9-01 (DY), 6-01 (S6), 5-01 (P5), 3-03 (A3), 3-02 (A2), 3-01 (A),
2-02 (D2), 2-01 (B), 7-01 (C) and 8 (D8). build_rails_10-08_vi (I8) is imported as a cross-check.
Every string comes from their functions: I5.ETENEVA / KATICI_BHAVE / ye_clause12 / ye_head12 / anantara_group /
head_parts12 / answer_head12, I4.question11, I3.split_mv, B.b_noca / b_both, I.ind_mulaka.

The one difference from 10-05's answer_head12: the head 'Pañcavokāre pacchimabhavikānaṃ asaññasattānaṃ arūpānaṃ'
(a person group followed by a run of plane-beings). 10-05 / 10-02 / 3-02 / 6-01 give the flat list
«những người thuộc kiếp sống cuối cùng trong cõi gồm năm khối, chúng sinh Vô Tưởng và chúng sinh trong cõi không
hình sắc»; 9-01's answer_head gives «… và chúng sinh Vô Tưởng và …», so 10-05's cross-check stops. Coordinator rule
(3-02 line): nested runs of beings are joined flat «A, B và C»; 10-07 has the same Pāli. Followed 3-02 (asserted
equal to A2.answer_head, I2.ind_answer_head and S6.answer_head) and listed the clash.

Exposed: FLAT_FOLLOWED, answer_head13, pv_sentence13, unit13, line13, tr_line, build.
A line, unit or head the parsers cannot place raises ValueError (no silent fallback). Importing writes nothing.

usage: python -I -X utf8 -B build_rails_10-07_vi.py   (probe: … build_rails_10-07_vi.py probe)
"""
import importlib
import re
import sys
import unicodedata

RAILS_DIR = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\rails"
if RAILS_DIR not in sys.path:
    sys.path.insert(0, RAILS_DIR)
import build_rails_sample_vi as S  # noqa: E402  (READ-ONLY)
I5 = importlib.import_module("build_rails_10-05_vi")   # READ-ONLY: nearest setter
I8 = importlib.import_module("build_rails_10-08_vi")   # READ-ONLY: cross-check (lines it parses)
I4, I3, I2, I, A, B, C, DY = I5.I4, I5.I3, I5.I2, I5.I, I5.A, I5.B, I5.C, I5.DY
A2, A3, S6, P5, D8 = I5.A2, I5.A3, I5.S6, I5.P5, I5.D8
assert I8.I4 is I4 and I8.S is S

cap = S.cap
CH = "10-07-indriyayamaka.md"
N = "10-07"
NOTES_MD = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/notes-rails-{N}.md"
ADH_DIR = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/adh-{N}"
M_IND = I.INDRIYA
PLANES = I5.PLANES
CHECKED = {"10-05 line": 0, "10-08 line": 0, "3-02 flat head": 0}
FLAT_FOLLOWED = {}     # Pāli head -> (followed 3-02 form, 9-01 form)
HEADS_SEEN = {}


# ===============================================================================================================
# 1. Answer heads: 10-05 answer_head12; a person group + plane-being run = 3-02 flat (9-01 clash listed)
# ===============================================================================================================
def answer_head13(head, loc):
    try:
        out = I5.answer_head12(head, loc)
    except AssertionError as e:
        info = e.args[0] if e.args else None
        if not (isinstance(info, tuple) and info[0] == "9-01 head" and info[1] == head):
            raise
        parts, special = I5.head_parts12(head)
        if special or len(parts) != 1:
            raise ValueError(f"9-01 clash on a head that is not one person run: {head!r}") from e
        out = cap(", ".join(parts))
        flat = (A2.answer_head(head, loc, PLANES), I2.ind_answer_head(head, loc), S6.answer_head(head))
        assert all(f == out for f in flat), (head, out, flat)
        assert out.count(f" {C.AND} ") == 1 and info[2].count(f" {C.AND} ") > 1, (out, info[2])
        FLAT_FOLLOWED[head] = (out, info[2])
        CHECKED["3-02 flat head"] += 1
    HEADS_SEEN[head] = out
    return out


# ===============================================================================================================
# 2. Sentences, units, lines (10-05 pv_sentence12 / unit12 / line12 / tr_line with answer_head13)
# ===============================================================================================================
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
        return I5.question12(u[:-1], M)
    if u in B.SHORT:
        return B.SHORT[u]
    if "…" in u:
        raise ValueError(f"cut not set in this chapter: {u!r}")
    if (out := pv_sentence13(u, M)) is not None:
        return out
    raise ValueError(f"unknown unit {u!r}")


def line13(body, M=None):
    body, label = body.strip(), None
    if m := re.fullmatch(r"(.+?) (\(\w+mūlakaṃ\)\.?)", body):     # trailing (Xindriyamūlakaṃ) label (10-02)
        body, label = m.group(1), m.group(2)
    units = [x for x in re.split(r"(?<=[.?]) (?=\S)", body) if x]
    if label:
        units.append(label)
    return " ".join(unit13(x, M) for x in units)


def tr_line(p, M=None):
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
        out = line13(body, M)
    full = f"{out} {bid}" if bid else out
    for name, mod in (("10-05 line", I5), ("10-08 line", I8)):
        try:
            old = mod.tr_line(p, M)
        except (ValueError, KeyError, AssertionError):
            continue
        assert old == full, (name, p, old, full)
        CHECKED[name] += 1
    return full


def build(name=CH, M=None):
    return [[tr_line(ln, M) for ln in seg] for seg in S.segments_of(name)]


# ===============================================================================================================
# 3. Notes file (Pāli = tiếng Việt)
# ===============================================================================================================
def notes():
    out = []

    def row(p, v):
        out.append(f"{p} = {v}")

    def h(t):
        out.extend(["", f"## {t}", ""])

    def head_row(hd, loc="tesaṃ tattha"):
        row(f"{hd} {loc} …", f"{answer_head13(hd, loc)}, {C.THEN} {B.L[I2.PRON_FEM.get(loc, loc)]} …")

    out += [f"# pi-6 rails {N} (Indriyayamaka 7): (3) Anāgatavāro, (Ca) paccanīkapuggalokāsā", "",
            "Builder: build_rails_10-07_vi.py (import with importlib). Setter: build_rails_10-05_vi (ETENEVA, "
            "KATICI_BHAVE, ye_clause12, ye_head12, anantara_group, head_parts12, answer_head12, question12, "
            "pv_sentence12 / unit12 / line12 / tr_line), and through it 10-04 (question11), 10-03 (split_mv, "
            "NEG_BOTH_RE), 10-02 (ind_answer_head, PRON_FEM, NOCA_RE, heading), 10-01 (INDRIYA, ind_mulaka), 9-01, "
            "6-01 (anantara_group), 5-01, 3-03 (flat_persons), 3-02 (answer_head), 3-01 (PLANES_AY, AY_ATTRS), 2-02, "
            "2-01 (b_noca, b_both, SHORT), 7-01 (pair_q), 8; all READ-ONLY. Every line 10-05 or 10-08 parses is "
            "asserted byte-identical (10-05: " + str(CHECKED["10-05 line"]) + " lines, 10-08: "
            + str(CHECKED["10-08 line"]) + " lines). No new frames: every string is a setter's. Exposed: "
            "`FLAT_FOLLOWED`, `answer_head13`, `pv_sentence13`, `unit13`, `line13`, `tr_line`, `build`. "
            "Format: Pāli = tiếng Việt.", ""]
    h("Headings")
    row("(Ca) paccanīkapuggalokāsā", I2.heading("(Ca) paccanīkapuggalokāsā"))
    h("Questions and verbs (future, separate na)")
    for s in ("(Ka) yassa yattha cakkhundriyaṃ na uppajjissati tassa tattha sotindriyaṃ na uppajjissatīti? Āmantā.",
              "Yassa yattha cakkhundriyaṃ na uppajjissati tassa tattha saddhindriyaṃ…pe… paññindriyaṃ…pe… "
              "manindriyaṃ na uppajjissatīti?",
              "Yassa yattha saddhindriyaṃ na uppajjissati tassa tattha paññindriyaṃ…pe… manindriyaṃ "
              "na uppajjissatīti? Āmantā."):
        row(s, line13(s))
    row("no ca tesaṃ tattha B na uppajjissati", "nhưng ở những người ấy, ở nơi ấy B vẫn sẽ sinh khởi")
    row("A-ñca na uppajjissati B-ñca na uppajjissati", "A sẽ không sinh khởi, B cũng sẽ không sinh khởi")
    h("Answer heads in this chapter (all from the setters)")
    for hd in ("Rūpāvacarānaṃ", "Pañcavokāre pacchimabhavikānaṃ asaññasattānaṃ arūpānaṃ",
               "Asaññasattānaṃ arūpānaṃ", "Pacchimabhavikānaṃ", "Pacchimabhavikānaṃ asaññasattānaṃ",
               "Rūpāvacarānaṃ arūpāvacarānaṃ", "Kāmāvacare pacchimabhavikānaṃ rūpāvacarānaṃ arūpāvacarānaṃ",
               "Ye sacakkhukā upekkhāya upapajjitvā parinibbāyissanti",
               "Ye saghānakā somanassena upapajjitvā parinibbāyissanti",
               "Ye purisā eteneva bhāvena katici bhave dassetvā parinibbāyissanti",
               "Rūpāvacarānaṃ ye ca purisā eteneva bhāvena katici bhave dassetvā parinibbāyissanti",
               "Rūpāvacarānaṃ arūpāvacarānaṃ yā ca itthiyo eteneva bhāvena katici bhave dassetvā upekkhāya "
               "upapajjitvā parinibbāyissanti",
               "Pañcavokāre pacchimabhavikānaṃ asaññasattānaṃ arūpānaṃ ye ca purisā eteneva bhāvena katici bhave "
               "dassetvā upekkhāya upapajjitvā parinibbāyissanti",
               "Pacchimabhavikānaṃ asaññasattānaṃ yā ca itthiyo eteneva bhāvena katici bhave dassetvā somanassena "
               "upapajjitvā parinibbāyissanti",
               "Yassa cittassa anantarā upekkhāsampayuttapacchimacittaṃ uppajjissati asaññasattānaṃ",
               "Yassa cittassa anantarā somanassasampayuttapacchimacittaṃ uppajjissati",
               "Pacchimacittasamaṅgīnaṃ", "Pacchimacittasamaṅgīnaṃ asaññasattānaṃ"):
        head_row(hd)
    head_row("Yā itthiyo eteneva bhāvena katici bhave dassetvā parinibbāyissanti", "tāsaṃ tattha")
    h("Sample lines")
    for s in ("Rūpāvacarānaṃ tesaṃ tattha ghānindriyaṃ na uppajjissati, no ca tesaṃ tattha cakkhundriyaṃ na "
              "uppajjissati. Pañcavokāre pacchimabhavikānaṃ asaññasattānaṃ arūpānaṃ tesaṃ tattha ghānindriyañca na "
              "uppajjissati cakkhundriyañca na uppajjissati.",
              "Yā itthiyo eteneva bhāvena katici bhave dassetvā parinibbāyissanti tāsaṃ tattha purisindriyaṃ na "
              "uppajjissati, no ca tāsaṃ tattha ghānindriyaṃ na uppajjissati.",
              "Yassa cittassa anantarā upekkhāsampayuttapacchimacittaṃ uppajjissati asaññasattānaṃ tesaṃ tattha "
              "somanassindriyaṃ na uppajjissati, no ca tesaṃ tattha jīvitindriyaṃ na uppajjissati."):
        row(s, line13(s))
    h("Clashes between finished chapters (for the coordinator)")
    out += [
        "- 'Pañcavokāre pacchimabhavikānaṃ asaññasattānaṃ arūpānaṃ tesaṃ tattha' (^6-10-326 four times, ^6-10-327 "
        "twice; before 'ye ca' at ^6-10-328 / ^6-10-329 10-05's ye_head12 already gives the flat list, asserted equal "
        "to 3-03): 9-01 answer_head gives «"
        + "; ".join(sorted({v[1] for v in FLAT_FOLLOWED.values()}))
        + "»; 10-05 head_parts12 / 10-02 ind_answer_head / 3-02 answer_head / 6-01 answer_head give the flat list «"
        + "; ".join(sorted({v[0] for v in FLAT_FOLLOWED.values()}))
        + "». Followed 3-02 (coordinator rule: nested runs of beings joined flat; 3-02 has the same Pāli). 10-05's "
        "own tr_line stops on these lines (its 9-01 cross-check), so they are built here with answer_head13.",
        "- Kept as the setters print it (rules-coordinator 6-01 open item, «và» inside an inner plane list): "
        "'Rūpāvacarānaṃ arūpāvacarānaṃ ye/yā ca …' «Ở chúng sinh trong cõi hình sắc và cõi không hình sắc và những "
        "người nam / nữ nào …» (= 3-03 'rūpāvacare arūpāvacare pacchimabhavikānaṃ ye ca …'; 10-05 ye_head12 asserted "
        "equal to 3-03 ye_ca_head).",
        "- After a person group, plane-beings each take «chúng sinh» ('Kāmāvacare pacchimabhavikānaṃ rūpāvacarānaṃ "
        "arūpāvacarānaṃ' «…, chúng sinh trong cõi hình sắc và chúng sinh trong cõi không hình sắc», 3-02 / 10-08); "
        "alone they share it ('Rūpāvacarānaṃ arūpāvacarānaṃ' «chúng sinh trong cõi hình sắc và cõi không hình sắc»). "
        "Both as the setters print them.",
        "",
        "## Termbase misfits and gaps (for the coordinator)",
        "",
        "- None new. Inherited: saghānakā «có mũi» (no entry; sibling Saghānakānaṃ, 3-01 / 10-05); katici bhave "
        "dassetvā «sau khi trải qua một số kiếp sống» (10-05, awaiting confirmation).",
        "",
        "## Pāli as written (reported)",
        "",
        "- Cut member-list questions (Yassa yattha X na uppajjissati tassa tattha saddhindriyaṃ…pe… paññindriyaṃ…pe… "
        "manindriyaṃ …ti?) and their (b) questions stand unlabelled among labelled ones (^6-10-326 … ^6-10-333): kept "
        "unlabelled; questions without an answer keep their «?».",
        "- ^6-10-332: the answer and the next (unlabelled) question with its answer and the label stand on one line: "
        "kept on one line.",
        "- ^6-10-333: both questions unlabelled (no (Ka) / (Kha)): kept as written.",
        "- ^6-10-328 / ^6-10-329 'tāsaṃ tattha' after 'Yā itthiyo …' and 'tesaṃ tattha' after 'Rūpāvacarānaṃ yā ca "
        "itthiyo …': both «thì ở những người ấy, ở nơi ấy» (10-02 PRON_FEM).",
        "- No spelling slips found.",
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
    I5.check_frames()
    segs = build(CH)
    I5.check_termbase()
    assert CHECKED["3-02 flat head"] > 0 and set(FLAT_FOLLOWED) == {
        "Pañcavokāre pacchimabhavikānaṃ asaññasattānaṃ arūpānaṃ"}, FLAT_FOLLOWED
    note_text = unicodedata.normalize("NFC", notes())
    S.write(CH, segs)
    text = (S.OUT_DIR / CH).read_text(encoding="utf-8")
    ADH_DIR.mkdir(parents=True, exist_ok=True)
    (ADH_DIR / CH).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", ADH_DIR / CH)
    NOTES_MD.write_text(note_text, encoding="utf-8", newline="\n")
    print("wrote", NOTES_MD)
    print("checked equal:", CHECKED, "; heads:", len(HEADS_SEEN), "; flat followed:", len(FLAT_FOLLOWED))


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
