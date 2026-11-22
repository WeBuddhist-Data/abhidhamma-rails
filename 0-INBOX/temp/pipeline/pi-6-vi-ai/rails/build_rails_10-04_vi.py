"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 10-04 (Indriyayamaka 4: uppādavāra, paccuppanna,
(Ṅa) paccanīkaokāso and (Ca) paccanīkapuggalokāsā).

Setters (all imported READ-ONLY with importlib; every shared string comes from their functions):
  build_rails_10-03_vi  (I3)  separate-na verbs (verb / split_mv), persons10 / answer_head10, question10,
                              pv_sentence10 (b_noca / b_both with na), unit10 / line10 / tr_line
  build_rails_10-02_vi  (I2)  Indriya person heads, heading, the cut answer «Āmantā …pe….» (pv_unit)
  build_rails_10-01_vi  (I)   INDRIYA members, ind_mulaka
  build_rails_9-01_vi   (DY)  verb() with a separate "na"
  build_rails_3-01_vi   (A)   BQ_RE, question_vi / split_mv (cut member lists «A… B… C»), PLANES_AY
  build_rails_2-01_vi   (B)   b_q, place_head, SHORT     build_rails_7-01_vi (C): shell connectors
  (all reached through I3 / I2, i.e. the very module objects 10-03 and 10-02 use)

New here (named constants; later Indriya chapters import them):
  split_mv_cut / CUT_SPLIT       a member list cut by …pe… with a SEPARATE "na" verb ("itthindriyaṃ…pe…
                                 purisindriyaṃ na uppajjatīti") = 3-01's cut list «năng lực nữ tính… năng lực nam
                                 tính» + 10-03's «không sinh khởi»
  question11                     pair questions (cut or whole) with separate-na verbs; a cut question is asserted
                                 equal to 3-01's positive question with «sinh khởi» → «không sinh khởi»; a whole one
                                 = 10-03 question10
  unit11 / line11 / tr_line / build   the line translator; every line 10-03 can parse is asserted byte-identical
A line, unit or word the parsers cannot place raises ValueError (no silent fallback). Importing writes nothing.

usage: python -I -X utf8 -B build_rails_10-04_vi.py   (probe: … build_rails_10-04_vi.py probe)
"""
import importlib
import re
import sys
import unicodedata

RAILS_DIR = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\rails"
if RAILS_DIR not in sys.path:
    sys.path.insert(0, RAILS_DIR)
import build_rails_sample_vi as S  # noqa: E402  (READ-ONLY)
I3 = importlib.import_module("build_rails_10-03_vi")   # READ-ONLY: separate-na Indriya lines (setter)
I2 = importlib.import_module("build_rails_10-02_vi")   # READ-ONLY: Indriya person heads (setter)
I, A, B, C, DY = I3.I, I3.A, I3.B, I3.C, I3.DY          # the same module objects 10-03 / 10-02 use
assert I2 is I3.I2 and A is I2.A and B is I2.B and DY is I2.DY

cap = S.cap
lc = I2.lc
CH = "10-04-indriyayamaka.md"
N = "10-04"
NOTES_MD = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/notes-rails-{N}.md"
ADH_DIR = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/adh-{N}"
M_IND = I.INDRIYA
CHECKED = {"10-03 line": 0, "10-03 question": 0, "3-01 cut question": 0}
CUTS_SEEN = []


# ===============================================================================================================
# 1. Pair questions with a separate "na", whole or with a member list cut by …pe…
# ===============================================================================================================
CUT_SPLIT = re.compile(r"…(?:pe…)?\s*")     # 3-01 split_mv: "A…pe… B…pe… C" → «A… B… C»
CUT_JOIN = S.PE + " "


def split_mv_cut(chunk, M=None):
    """'saddhindriyaṃ…pe… paññindriyaṃ…pe… manindriyaṃ na uppajjatīti' → («năng lực niềm tin… năng lực trí tuệ…
    năng lực ý», 9-01 verb tuple). Without a cut: 10-03 split_mv."""
    M = M or M_IND
    if "…" not in chunk:
        return I3.split_mv(chunk, M)
    w = chunk.split()
    for k in (2, 1):
        if len(w) > k and DY.is_verb(" ".join(w[-k:])):
            mem = " ".join(w[:-k])
            names = [M.subj(x) for x in CUT_SPLIT.split(mem) if x]
            if len(names) < 2:
                raise ValueError(f"cut list with one member in {chunk!r}")
            return CUT_JOIN.join(names), DY.verb(" ".join(w[-k:]))
    raise ValueError(f"no member list + verb in {chunk!r}")


def question11(q, M=None):
    """(Ka) yattha / yassa yattha A [na] V tattha / tassa tattha B[…pe… C] [na] Vti (without «?») → 2-01 b_q."""
    M = M or M_IND
    if "…" not in q:
        out = I3.question10(q, M)
        CHECKED["10-03 question"] += 1
        return out
    m = A.BQ_RE.fullmatch(q)
    if not m:
        raise ValueError(f"unknown cut question {q!r}")
    label, w1, vapana, w2, c1, then, c2 = m.groups()
    if label is None and w1[0] != w1[0].upper():
        raise ValueError(f"unlabelled lower-case question {q!r}")
    a, v1 = split_mv_cut(c1, M)
    b, v2 = split_mv_cut(c2, M)
    out = B.b_q(label, lc(w1) + (w2 or ""), then, a, v1[0], b, v2[0], other=bool(vapana))
    # the same question with positive verbs is 3-01's (10-02's) string; only the verbs differ
    pos_q = q.replace(" na uppajjati ", " uppajjati ").replace(" na uppajjatīti", " uppajjatīti")
    if pos_q != q:
        pos = A.question_vi(pos_q, M)
        neg_v, pos_v = DY.verb("na uppajjati")[0], DY.verb("uppajjati")[0]
        assert (v1[0], v2[0]) == (neg_v, neg_v), q
        assert out == pos.replace(f" {pos_v}", f" {neg_v}"), (q, pos, out)
        CHECKED["3-01 cut question"] += 1
    CUTS_SEEN.append((q, out))
    return out


# ===============================================================================================================
# 2. Units and lines
# ===============================================================================================================
def unit11(u, M=None):
    M = M or M_IND
    if (lab := I.ind_mulaka(u, M)) is not None:
        return lab
    if u.endswith("?"):
        return question11(u[:-1], M)
    if u in B.SHORT:
        return B.SHORT[u]
    if (m := I2.CUT_ANS_RE.fullmatch(u)) and m.group(1) + "." in B.SHORT:   # Āmantā …pe…. «Đúng vậy …» (10-02)
        return I2.pv_unit(u, M)
    if "…" in u:
        raise ValueError(f"cut not set in this chapter: {u!r}")
    if (out := I3.pv_sentence10(u, M)) is not None:
        return out
    raise ValueError(f"unknown unit {u!r}")


def line11(body, M=None):
    body, label = body.strip(), None
    if m := re.fullmatch(r"(.+?) (\(\w+mūlakaṃ\)\.?)", body):     # trailing (Xindriyamūlakaṃ) label (10-02)
        body, label = m.group(1), m.group(2)
    units = [x for x in re.split(r"(?<=[.?]) (?=\S)", body) if x]
    if label:
        units.append(label)
    return " ".join(unit11(x, M) for x in units)


def tr_line(p, M=None, fixed=None):
    M = M or M_IND
    m = re.search(r" (\^\S+)$", p)
    bid = m.group(1) if m else None
    body = p[:m.start()] if m else p
    if "[" in body:
        raise ValueError(f"variant bracket not handled: {p!r}")
    if body.startswith("#"):
        hashes, text = body.split(" ", 1)
        out = f"{hashes} {I2.heading(text)}"
    elif fixed and body in fixed:
        out = fixed[body]
    else:
        out = line11(body, M)
    full = f"{out} {bid}" if bid else out
    try:
        old = I3.tr_line(p, M, fixed)
    except (ValueError, KeyError):
        old = None
    if old is not None:
        assert old == full, ("10-03 line", p, old, full)
        CHECKED["10-03 line"] += 1
    return full


def build(name, M=None, fixed=None):
    return [[tr_line(ln, M, fixed) for ln in seg] for seg in S.segments_of(name)]


# ===============================================================================================================
# 3. Checks
# ===============================================================================================================
def check_frames():
    M = M_IND
    q = "Yattha cakkhundriyaṃ uppajjati tattha saddhindriyaṃ…pe… paññindriyaṃ…pe… manindriyaṃ uppajjatīti"
    assert B.b_q(None, "yattha", "tattha", M.subj("cakkhundriyaṃ"), DY.verb("uppajjati")[0],
                 *split_mv_cut("saddhindriyaṃ…pe… paññindriyaṃ…pe… manindriyaṃ uppajjatīti", M)[:1],
                 DY.verb("uppajjati")[0]) == A.question_vi(q, M)
    assert I2.heading("(Ṅa) paccanīkaokāso").endswith("Chiều nghịch theo nơi chốn")
    assert I2.heading("(Ca) paccanīkapuggalokāsā").endswith("Chiều nghịch theo người và nơi chốn")
    assert S.LABEL["Ṅa"] == "(đ)" and S.LABEL["Ca"] == "(e)"


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

    out += [f"# pi-6 rails {N} (Indriyayamaka 4): (Ṅa) paccanīkaokāso, (Ca) paccanīkapuggalokāsā", "",
            "Builder: build_rails_10-04_vi.py (import with importlib). Setters: build_rails_10-03_vi (verb / split_mv "
            "with a separate na, question10, pv_sentence10, persons10, answer_head10, tr_line) and build_rails_10-02_vi "
            "(heading, ind_persons, faculty_mind_gen, the cut answer «Āmantā …pe….»); through them 10-01 (INDRIYA, "
            "ind_mulaka), 9-01 (verb), 3-01 (BQ_RE, question_vi, PLANES_AY), 2-01 (b_q, place_head, b_noca, b_both, "
            "SHORT), 7-01; all READ-ONLY. Every line 10-03 can parse is asserted byte-identical to 10-03's; every cut "
            "question is asserted equal to 3-01's positive question with «sinh khởi» → «không sinh khởi». Exposed: "
            "`CUT_SPLIT`, `CUT_JOIN`, `split_mv_cut`, `question11`, `unit11`, `line11`, `tr_line`, `build`. Format: "
            "Pāli = tiếng Việt.", ""]
    h("Headings")
    for t in ("(Ṅa) paccanīkaokāso", "(Ca) paccanīkapuggalokāsā"):
        row(t, I2.heading(t))
    h("Questions with a separate na (new: member lists cut by …pe…)")
    for q in ("Yattha cakkhundriyaṃ na uppajjati tattha itthindriyaṃ…pe… purisindriyaṃ na uppajjatīti",
              "Yattha cakkhundriyaṃ na uppajjati tattha saddhindriyaṃ…pe… paññindriyaṃ…pe… manindriyaṃ na uppajjatīti",
              "(Ka) yattha cakkhundriyaṃ na uppajjati tattha sotindriyaṃ na uppajjatīti",
              "(Kha) yattha vā pana ghānindriyaṃ na uppajjati tattha cakkhundriyaṃ na uppajjatīti",
              "Yattha vā pana manindriyaṃ na uppajjati tattha cakkhundriyaṃ na uppajjatīti",
              "(Ka) yassa yattha cakkhundriyaṃ na uppajjati tassa tattha sotindriyaṃ na uppajjatīti",
              "(Kha) yassa vā pana yattha sotindriyaṃ na uppajjati tassa tattha cakkhundriyaṃ na uppajjatīti"):
        row(q + "?", question11(q, M))
    h("Place answers (10-03 / 2-01 frames with PLANES_AY)")
    for s in ("Rūpāvacare tattha ghānindriyaṃ na uppajjati, no ca tattha cakkhundriyaṃ na uppajjati.",
              "Asaññasatte arūpe tattha ghānindriyañca na uppajjati cakkhundriyañca na uppajjati.",
              "Rūpāvacare arūpāvacare tattha ghānindriyaṃ na uppajjati, no ca tattha upekkhindriyaṃ na uppajjati.",
              "Asaññasatte tattha cakkhundriyañca na uppajjati upekkhindriyañca na uppajjati."):
        row(s, line11(s, M))
    for s in ("Uppajjati.", "Natthi.", "Āmantā …pe…."):
        row(s, unit11(s, M))
    h("Person-and-place answers (10-03 frames with tesaṃ / tāsaṃ tattha)")
    for s in ("Acakkhukānaṃ itthīnaṃ upapajjantīnaṃ tāsaṃ tattha cakkhundriyaṃ na uppajjati, no ca tāsaṃ tattha "
              "itthindriyaṃ na uppajjati.",
              "Sabbesaṃ cavantānaṃ tesaṃ tattha cakkhundriyañca na uppajjati jīvitindriyañca na uppajjati.",
              "Sabbesaṃ cavantānaṃ vinā somanassena na itthīnaṃ upapajjantānaṃ tesaṃ tattha somanassindriyañca na "
              "uppajjati itthindriyañca na uppajjati.",
              "Vinā somanassena upapajjantānaṃ pavatte somanassavippayuttacittassa uppādakkhaṇe tesaṃ tattha "
              "somanassindriyaṃ na uppajjati, no ca tesaṃ tattha jīvitindriyaṃ na uppajjati.",
              "Sabbesaṃ cavantānaṃ pavatte cittassa bhaṅgakkhaṇe tesaṃ tattha somanassindriyañca na uppajjati "
              "jīvitindriyañca na uppajjati.",
              "Sabbesaṃ cittassa bhaṅgakkhaṇe somanassavippayuttaupekkhāvippayuttacittassa uppādakkhaṇe "
              "asaññasattānaṃ tesaṃ tattha somanassindriyañca na uppajjati upekkhindriyañca na uppajjati.",
              "Sabbesaṃ cittassa bhaṅgakkhaṇe asaññasattānaṃ tesaṃ tattha somanassindriyañca na uppajjati "
              "manindriyañca na uppajjati.",
              "Pavatte saddhāvippayuttasomanassasampayuttacittassa uppādakkhaṇe tesaṃ tattha saddhindriyaṃ na "
              "uppajjati, no ca tesaṃ tattha somanassindriyaṃ na uppajjati."):
        row(s, line11(s, M))
    h("Termbase misfits and gaps (for the coordinator)")
    out += [
        "- No new member, person, plane, mind or verb words: all from 10-01 … 10-03 / 9-01 / 3-01 / 2-01.",
        "- Sex / feeling words with cavantānaṃ itself or with a plane: not met in this chapter. Every sex / feeling "
        "word after «Sabbesaṃ cavantānaṃ» belongs to the next upapajjantānaṃ group (10-03 shape), e.g. «Sabbesaṃ "
        "cavantānaṃ vinā somanassena na itthīnaṃ upapajjantānaṃ» «tất cả những người đang chết đi và những người đang "
        "tái sinh không làm người nữ, không có niềm vui đi kèm». The builder still raises on the open shapes.",
        "- Cut member lists with a separate na (new here, (Ṅa)): 3-01's «A… B… C» + 10-03's «không sinh khởi», e.g. "
        "«… thì ở nơi ấy có phải năng lực nữ tính… năng lực nam tính không sinh khởi không?».",
        "",
        "## Pāli as written (reported)",
        "",
        "- ^6-10-222, ^6-10-223, ^6-10-225: an answer and the next (unlabelled) question, and at ^6-10-223 / "
        "^6-10-225 also the last question with its answer, stand on one line: kept on one line.",
        "- (Ṅa) unlabelled questions «Yattha …» / «Yattha vā pana …» among labelled ones: kept unlabelled.",
        "- ^6-10-224 «(Kha) … Āmantā …pe….» (space before the cut) = «Đúng vậy …» (10-01 / 10-02).",
        "- ^6-10-231 / ^6-10-232 / ^6-10-233 / ^6-10-234 «Sabbesaṃ cavantānaṃ acittakānaṃ upapajjantānaṃ …» (no "
        "acakkhukānaṃ / aghānakānaṃ / sex word in the manindriya answers): as written (as 10-03).",
        "- ^6-10-236 … ^6-10-239 «Sabbesaṃ cittassa bhaṅgakkhaṇe … asaññasattānaṃ …» (no nirodhasamāpannānaṃ, unlike "
        "the person-only 10-03 answers; fits the place reading): as written, «…, ở chúng sinh Vô Tưởng, thì ở những "
        "người ấy, ở nơi ấy …».",
        "- ^6-10-236 «Pavatte saddhāvippayuttasomanassasampayuttacittassa uppādakkhaṇe tesaṃ tattha …» (a head with "
        "no person group): «Trong đời sống, vào khoảnh khắc …, thì ở những người ấy, ở nơi ấy …» (10-02 shape).",
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
    check_frames()
    segs = build(CH)
    I3.check_termbase()
    S.write(CH, segs)
    text = (S.OUT_DIR / CH).read_text(encoding="utf-8")
    ADH_DIR.mkdir(parents=True, exist_ok=True)
    (ADH_DIR / CH).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", ADH_DIR / CH)
    NOTES_MD.write_text(unicodedata.normalize("NFC", notes()), encoding="utf-8", newline="\n")
    print("wrote", NOTES_MD)
    print("checked equal:", CHECKED, "; 10-03:", I3.CHECKED, "; cut questions:", len(CUTS_SEEN))


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
