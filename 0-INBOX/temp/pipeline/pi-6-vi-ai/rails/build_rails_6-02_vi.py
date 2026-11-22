"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 6-02 (Saṅkhārayamaka 2: the rest of the nirodhavāra, the
uppādanirodhavāra and the pariññāvāra; the end of the Saṅkhārayamaka).

Everything comes from the Saṅkhāra module build_rails_6-01_vi (members, verbs, questions, answer heads, answer frames,
cut lines, headings) and, through it, 2-01 (families A, B), 7-01 (answer shapes), 8 (moments, persons), 9-01 / 9-02
(answer heads), 3-02 / 3-03 (person items, the ye-ca head), 2-02 (KHI_CAVANTA, cuts), 5-01 (note pieces, cut
questions). 9-02 gives Pacchimacittassa «tâm cuối cùng»; 5-02 / 5-03 the editorial-note pieces; 2-02 family E
(pariññāvāra). All imported READ-ONLY: nothing in them is changed.

6-01's head parser has no entry for the bare genitive pacchimacittassa (only savitakkasavicāra- / avitakkaavicāra-
pacchimacittassa): this file loads a PRIVATE second instance of build_rails_6-01_vi (`PSK`, its own module object;
the shared module `SK` and its dicts stay untouched) and gives that instance's own GEN the one extra genitive
pacchimacittassa «tâm cuối cùng» (= 9-02 gen_vi = 8 mind_gen_vi). The builder asserts that the private instance
still reproduces the 6-01 chapter byte for byte, so every string shared with 6-01 is 6-01's.

Exposed (for later chapters): `PSK`, `FINAL_MIND`, `NOTES`, `INLINE_NOTES`, `FIXED`, `frag`, `cut_with_note`,
`heading`, `line_vi`, `tr_line`, `build`. A line the parsers cannot place raises ValueError (no silent fallback).

usage: python -I -X utf8 -B build_rails_6-02_vi.py [--probe] [--show]
"""
import importlib
import importlib.util
import pathlib
import re
import sys
import unicodedata

RAILS_DIR = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\rails")
if str(RAILS_DIR) not in sys.path:
    sys.path.insert(0, str(RAILS_DIR))
import build_rails_sample_vi as S  # noqa: E402  (READ-ONLY)
SK = importlib.import_module("build_rails_6-01_vi")    # Saṅkhāra module, the family setter (READ-ONLY, shared)
B, C, D, E, DY, DY2, T5 = SK.B, SK.C, SK.D, SK.E, SK.DY, SK.DY2, SK.T5   # 2-01, 7-01, 8, 2-02, 9-01, 9-02, 5-01
P2 = importlib.import_module("build_rails_5-02_vi")   # READ-ONLY: note pieces (VIBHATTA, ANU_PACC, …)
P3 = importlib.import_module("build_rails_5-03_vi")   # READ-ONLY: ATITANAGATA_PUCCHA
A1 = importlib.import_module("build_rails_3-01_vi")   # READ-ONLY: ASAMMOHANTENA
A5 = importlib.import_module("build_rails_3-05_vi")   # READ-ONLY: OTHER_PLACE_PARTS (itaresaṃ yatthakānaṃ)


def _private_6_01():
    """A second, private instance of build_rails_6-01_vi (own module object, own dicts)."""
    spec = importlib.util.spec_from_file_location("build_rails_6_01_private_for_6_02",
                                                  RAILS_DIR / "build_rails_6-01_vi.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


PSK = _private_6_01()
assert PSK is not SK
FINAL_MIND = DY2.gen_vi("Pacchimacittassa")             # «tâm cuối cùng» (9-02; = 8 mind_gen_vi; termbase)
assert FINAL_MIND == D.mind_gen_vi("Pacchimacittassa") == SK.FINAL_MIND
PSK.GEN = {**PSK.GEN, "pacchimacittassa": FINAL_MIND}    # the private instance only
assert "pacchimacittassa" not in SK.GEN

CHAPTER = "6-02-sankharayamaka.md"
N = "6-02"
NOTES_MD = RAILS_DIR / f"notes-rails-{N}.md"
ADH_DIR = RAILS_DIR / f"adh-{N}"
TERMBASE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\vietnamese\pi-6-pali-vietnamese-termbase-plain.md")
cap = S.cap
PE = S.PE
M = PSK.M                                                 # SANKHARA (6-01)
SLIPS = []


def _decap(s):
    return s[:1].lower() + s[1:]


# ===============================================================================================================
# 1. Editorial notes (5-02 pieces: VIBHATTA «như đã được phân tích trong», VIBHAJITABBA «cũng nên phân tích như vậy»,
#    ANU_PACC «cả chiều thuận lẫn chiều nghịch», ATITA_PUCCHA / PACC_ATITA_PUCCHA «Các câu hỏi về …», SADISA
#    «giống nhau», NATTHI_NANA «không có sự khác biệt»; 5-03 ATITANAGATA_PUCCHA; 5-01 VITTHARETABBAM; 6-01
#    BOTH_SECTIONS / IN_YY / NIRODHA_Q; 3-01 ASAMMOHANTENA «mà không mê lầm» after the verb (= 5-03); 3-05
#    OTHER_PLACE_PARTS «các phần về nơi chốn khác»; termbase: uppādavāranirodhavārepi «mục về sự sinh khởi và sự
#    chấm dứt», nirodhavārena «mục về sự chấm dứt», khandhayamake / saṅkhārayamakepi (titles in “…”, as 4),
#    pariññāvāraṃ «mục về sự hiểu biết trọn vẹn»)
# ===============================================================================================================
ASAMMOHANTENA = A1.ASAMMOHANTENA
assert ASAMMOHANTENA == P2.ASAMMOHANTENA == "mà không mê lầm"
SADISA = P2.SADISA
SADISA_AS = f"{SADISA.split()[0]} như"                   # X-ena sadisaṃ «giống như X» (3-04 «giống như vậy»; 4)
assert SADISA_AS == "giống như"
OTHER_PLACE_PARTS = A5.OTHER_PLACE_PARTS                 # itaresaṃ yatthakānaṃ «các phần về nơi chốn khác» (3-05)
BOTH_YY = f"{SK.BOTH_SECTIONS} đều {SADISA}"              # Yassakampi yassayatthakampi sadisaṃ
assert SK.NOTE_SADISA == f"({BOTH_YY}.)"
assert f"({BOTH_YY})." == A5.NOTE_YASSAKA_SADISA         # = 3-05 / 5-02 "(Yassakampi yassayatthakampi sadisaṃ)."
T_KHANDHA = f"“{S.yamaka_title('Khandha')}”"             # khandhayamake (title in “…”, as 4)
T_SANKHARA = f"“{S.yamaka_title(SK.YAMAKA)}”"            # saṅkhārayamakepi
PARINNA = _decap(E.PARINNAVARO)                           # pariññāvāraṃ «mục về sự hiểu biết trọn vẹn»
_AT_3 = ", ".join(f"{C.AT} {x}" for x in (B.UPPADAVARO, B.NIRODHAVARO, B.UPPADANIRODHAVARO))

NOTES = {   # whole-line notes (Pāli → Vietnamese)
    "(Yassakampi yassayatthakampi sadisaṃ, yassayatthake nirodhasamāpannānanti na labbhati).":
        f"({BOTH_YY}, {SK.IN_YY} không có {SK.NIRODHA_Q}).",
    "(Atītā pucchā uppādavārepi nirodhavārepi uppādanirodhavārepi sadisaṃ vitthāretabbā).":
        f"({P2.ATITA_PUCCHA} {_AT_3} đều {T5.VITTHARETABBAM} {SADISA}).",
    "(Yathā uppādavāre paccuppannātītā pucchā anulomampi paccanīkampi vibhattā evaṃ uppādavāranirodhavārepi "
    "paccuppannātītā pucchā anulomampi paccanīkampi vibhajitabbā.)":
        f"({P2.PACC_ATITA_PUCCHA}, {P2.ANU_PACC}, {P2.VIBHATTA} {B.UPPADAVARO}, {C.AT} {B.UPPADANIRODHAVARO}, "
        f"{_decap(P2.PACC_ATITA_PUCCHA)}, {P2.ANU_PACC}, {P2.VIBHAJITABBA}.)",
    "(Yathā nirodhavāre atītānāgatā pucchā anulomampi paccanīkampi evaṃ uppādanirodhavārepi atītānāgatā pucchā "
    "anulomampi paccanīkampi vibhajitabbaṃ asammohantena nirodhavārena sadisaṃ, natthi nānākaraṇaṃ.)":
        f"({P3.ATITANAGATA_PUCCHA}, {P2.ANU_PACC}, như {C.AT} {B.NIRODHAVARO}, {C.AT} {B.UPPADANIRODHAVARO}, "
        f"{_decap(P3.ATITANAGATA_PUCCHA)}, {P2.ANU_PACC}, {P2.VIBHAJITABBA} {ASAMMOHANTENA}, {SADISA_AS} "
        f"{B.NIRODHAVARO}, {P2.NATTHI_NANA}.)",
    "(Yathā khandhayamake pariññāvāraṃ vibhattaṃ evaṃ saṅkhārayamakepi pariññāvāraṃ vibhajitabbaṃ.)":
        f"({cap(PARINNA)} {P2.VIBHATTA} {T_KHANDHA}, {C.AT} {T_SANKHARA}, {PARINNA} {P2.VIBHAJITABBA}.)",
}
INLINE_NOTES = {   # a note after a cut line (lower case in the Pāli)
    "(itaresaṃ yatthakānaṃ sadisaṃ).": f"({SADISA_AS} {OTHER_PLACE_PARTS}).",
    "(yassakampi yassayatthakampi sadisaṃ).": f"({_decap(BOTH_YY)}).",
}
FIXED = {
    "Pariññāvāro.": E.PARINNAVARO_CLOSE,                  # «Mục về sự hiểu biết trọn vẹn.» (2-02)
    "Saṅkhārayamakaṃ niṭṭhitaṃ.": S.yamaka_end(SK.YAMAKA),   # «Phần các cặp câu hỏi về các tạo tác đã hoàn tất.»
    "Namo tassa bhagavato arahato sammāsambuddhassa": S.HOMAGE,   # (pi-1; = 2-02, 4, 9-03)
}
assert FIXED["Saṅkhārayamakaṃ niṭṭhitaṃ."] == "Phần các cặp câu hỏi về các tạo tác đã hoàn tất."   # formulas file

# ===============================================================================================================
# 2. Cut lines with an inline note; an answer cut after its place head (^6-6-130)
# ===============================================================================================================
FRAG_RE = re.compile(r"(.+?) " + PSK.LOC + r"…pe…")


def frag(piece):
    """'<head> tesaṃ / tattha / tesaṃ tattha…pe…' → «<Head>, thì ở ……» (3-05 loc_fragment's shape with 6-01's head
    parser). Asserted to be the start of the full 6-01 answer with the same head."""
    m = FRAG_RE.fullmatch(piece)
    if not m:
        return None
    head, loc = m.groups()
    out = f"{PSK.answer_head(head)}, {C.THEN} {B.L[loc]}"
    probe_s = f"{head} {loc} kāyasaṅkhāro uppajjati, no ca {loc} vacīsaṅkhāro nirujjhati."
    assert PSK.b_sentence(probe_s).startswith(out + " "), (piece, out)
    return out + PE


CUT_NOTE_RE = re.compile(r"(.+?…pe…) (\([^()]*\)\.)")


def cut_with_note(body):
    """'Yassa yattha A V…pe… (note).' / '<head> tattha…pe… (note).' → the cut line + « (note).»."""
    m = CUT_NOTE_RE.fullmatch(body)
    if not m:
        return None
    left, note = m.groups()
    if note not in INLINE_NOTES:
        raise ValueError(f"unknown inline note {note!r}")
    c = PSK.cut_half(left)
    if c is None:
        c = frag(left)
    if c is None:
        raise ValueError(f"cut before a note not placed: {left!r}")
    return f"{c} {INLINE_NOTES[note]}"


# ^6-6-121 (Ka) answer, 2nd sentence: "H tesaṃ tattha A na V1 B ca V2." (no «ca» after A, a separate «na»; the
# parallel lines have "A ca V1 B ca V2"): translated as written, not as the both-frame (whose «cũng» would pair a
# denied verb with an affirmed one): «H, thì ở … A <na V1>, và B <V2>.» Reported as a possible slip.
HALF_CA_RE = re.compile(r"(.+?) " + PSK.LOC + r" (" + SK.MEMBER_SUBJ_RE + r") (na \S+) (" + SK.MEMBER_SUBJ_RE +
                        r") ca (\S+)\.")


def half_ca_sentence(s):
    m = HALF_CA_RE.fullmatch(s)
    if not m:
        return None
    head, loc, a, v1, b, v2 = m.groups()
    SLIPS.append(("«A na V1 B ca V2» (no «ca» after A; parallel lines have «A ca V1 B ca V2»): translated as written "
                  "with «và», possible slip for «ca»", s[:90]))
    return (f"{PSK.answer_head(head)}, {C.THEN} {B.L[loc]} {M.subj(a)} {B.verb(v1)[0]}, {C.AND} {M.subj(b)} "
            f"{B.verb(v2)[0]}.")


def answers(body):
    """A run of answer sentences where one is the half-ca shape (each other sentence: 6-01's sentence())."""
    out, rest = [], body.strip()
    while rest:
        m = re.match(r"(.+?\.)(?= |$)", rest)
        if not m:
            raise ValueError(f"no sentence end in {rest!r}")
        s = m.group(1)
        out.append(half_ca_sentence(s) or PSK.sentence(s))
        rest = rest[m.end():].strip()
    return " ".join(out)


# ===============================================================================================================
# 3. Headings (6-01's; 2-02's Pariññāvāro; termbase Paccuppannavārādi «mục về hiện tại và các mục khác», numbered as
#    the formulas file's «2-10. Mục về nguyên nhân và các mục khác»)
# ===============================================================================================================
PACC_ADI = "mục về hiện tại và các mục khác"              # Paccuppannavārādi (termbase)


def heading(text):
    if text in E.HEADINGS:
        return E.HEADINGS[text]
    if m := re.fullmatch(r"(\d+-\d+)\. Paccuppannavārādi", text):
        return f"{m.group(1)}. {cap(PACC_ADI)}"
    return PSK.heading(text)


# ===============================================================================================================
# 4. Line translator
# ===============================================================================================================
def line_vi(body):
    if body in NOTES:
        return NOTES[body]
    if body in FIXED:
        return FIXED[body]
    if (q := E.e_question(body, M, E.E_VERBS)) is not None:   # pariññāvāra (family E, 2-02)
        return q
    if (c := cut_with_note(body)) is not None:
        return c
    if any(HALF_CA_RE.fullmatch(x) for x in re.findall(r"(?:^|(?<=\. ))(.+?\.)(?= |$)", body)):
        return answers(body)
    return PSK.line_vi(body)


def tr_line(p):
    m = re.search(r" (\^\S+)$", p)
    bid = m.group(1) if m else None
    body = p[:m.start()] if m else p
    if body.startswith("#"):
        hashes, text = body.split(" ", 1)
        out = f"{hashes} {heading(text)}"
    else:
        if "[" in body:
            raise ValueError(f"variant bracket not declared for 6-02: {p!r}")
        out = line_vi(body)
    return f"{out} {bid}" if bid else out


def build(name=CHAPTER):
    segs = []
    for seg in S.segments_of(name):
        out = []
        for ln in seg:
            try:
                out.append(tr_line(ln))
            except (ValueError, KeyError, IndexError) as e:
                raise ValueError(f"{name}: cannot place line {ln[:160]!r}: {e!r}") from None
        segs.append(out)
    return segs


def probe(name=CHAPTER):
    bad = 0
    for seg in S.segments_of(name):
        for ln in seg:
            try:
                v = tr_line(ln)
                if "--show" in sys.argv:
                    print("PI:", ln, "\nVI:", v, "\n")
            except Exception as e:  # noqa: BLE001
                bad += 1
                print("FAIL:", type(e).__name__, str(e)[:300], "\n   ", ln[:200])
    print("failing lines:", bad)


# ===============================================================================================================
# 5. Assertions
# ===============================================================================================================
TB_USED = [("Paccuppannavārādi", PACC_ADI), ("uppādavāranirodhavārepi", B.UPPADANIRODHAVARO),
           ("nirodhavārena", B.NIRODHAVARO), ("khandhayamake", "các cặp câu hỏi về các khối"),
           ("saṅkhārayamakepi", "các cặp câu hỏi về các tạo tác"), ("pariññāvāraṃ", PARINNA),
           ("Pariññāvāro", PARINNA), ("Saṅkhārayamakaṃ", S.yamaka_title(SK.YAMAKA)), ("pucchā", "câu hỏi"),
           ("yatthakānaṃ", T5.P_PLACE)]


def check_termbase():
    entries = {}
    for ln in TERMBASE.read_text(encoding="utf-8").splitlines():
        if m := re.match(r"(.+?): \{(.*)\}$", ln):
            entries[m.group(1)] = m.group(2)
    bad = [(p, v, entries.get(p)) for p, v in TB_USED
           if entries.get(p) is None or not re.search(r": " + re.escape(v) + r"(?:[;}]|$)", entries[p])]
    assert not bad, "termbase mismatch: " + repr(bad)
    assert S.yamaka_title("Khandha").lower() == "các cặp câu hỏi về các khối"


def check_shared():
    # the private 6-01 instance still reproduces the 6-01 chapter byte for byte
    mine = "\n\n".join("\n".join(seg) for seg in PSK.build(SK.CHAPTER))
    have = (S.OUT_DIR / SK.CHAPTER).read_text(encoding="utf-8").rstrip("\n")
    assert unicodedata.normalize("NFC", mine) == have, "private 6-01 instance no longer reproduces 6-01"
    # Pacchimacittassa bhaṅgakkhaṇe = 9-02's head byte for byte
    assert PSK.answer_head("Pacchimacittassa bhaṅgakkhaṇe") == DY2.answer_head("Pacchimacittassa bhaṅgakkhaṇe",
                                                                                   "tesaṃ")
    # 2-02 closings / 5-02 «Mục về sự chấm dứt.»
    assert PSK.sentence("Nirodhavāro.") == E.NIRODHAVARO_CLOSE == P2.NIRODHAVARO_CLOSE
    assert PSK.sentence("Uppādanirodhavāro.") == E.UPPADANIRODHAVARO_CLOSE
    # short answers (9-02 «Đã chấm dứt.»; 7-01 «Không có.»)
    assert PSK.sentence("Nirujjhittha.") == "Đã chấm dứt." and PSK.sentence("Natthi.") == C.ANS_NATTHI
    # cut questions = 5-01 b_cut_question
    for q in ("(Kha) yassa vā pana…pe…? Āmantā.", "(Kha) yassa vā pana yattha…pe…? Āmantā."):
        assert PSK.cut_question(q) == T5.b_cut_question(q, M), q
    # 5-03's «… cũng nên phân tích như vậy mà không mê lầm»
    assert f"{P2.VIBHAJITABBA} {ASAMMOHANTENA}" in P3.NOTES[next(iter(P3.NOTES))]


# ===============================================================================================================
# 6. Notes file (Pāli = tiếng Việt)
# ===============================================================================================================
SAMPLE_HEADS = (
    "Kāmāvacarānaṃ pacchimacittassa uppādakkhaṇe yassa cittassa anantarā kāmāvacarānaṃ pacchimacittaṃ uppajjissati "
    "rūpāvacare arūpāvacare pacchimabhavikānaṃ ye ca rūpāvacaraṃ arūpāvacaraṃ upapajjitvā parinibbāyissanti tesaṃ "
    "cavantānaṃ",
    "Kāmāvacarānaṃ pacchimacittassa uppādakkhaṇe yassa cittassa anantarā kāmāvacarānaṃ pacchimacittaṃ uppajjissati "
    "catutthajjhānaṃ samāpannānaṃ rūpāvacarānaṃ arūpāvacarānaṃ",
    "Avitakkaavicārapacchimacittassa uppādakkhaṇe yassa cittassa anantarā avitakkaavicāraṃ pacchimacittaṃ "
    "uppajjissati",
    "Pacchimacittassa uppādakkhaṇe yassa cittassa anantarā avitakkaavicāraṃ pacchimacittaṃ uppajjissati",
    "Pacchimacittassa bhaṅgakkhaṇe asaññasattānaṃ",
    "Kāmāvacare pacchimacittassa bhaṅgakkhaṇe dutiyajjhānaṃ tatiyajjhānaṃ samāpannānaṃ",
    "Savitakkasavicārabhūmiyaṃ pacchimacittassa bhaṅgakkhaṇe",
    "Avitakkaavicārabhūmiyaṃ pacchimacittassa bhaṅgakkhaṇe asaññasattānaṃ",
    "Rūpāvacare arūpāvacare savitakkasavicārapacchimacittassa bhaṅgakkhaṇe avitakkaavicārapacchimacittasamaṅgīnaṃ "
    "yassa cittassa anantarā avitakkaavicāraṃ pacchimacittaṃ uppajjissati catutthajjhānaṃ samāpannānaṃ "
    "asaññasattānaṃ",
    "Rūpāvacare arūpāvacare pacchimacittassa bhaṅgakkhaṇe asaññasattānaṃ",
    "Sabbesaṃ cittassa uppādakkhaṇe vinā assāsapassāsehi cittassa bhaṅgakkhaṇe nirodhasamāpannānaṃ asaññasattānaṃ",
    "Vinā assāsapassāsehi cittassa uppādakkhaṇe vinā vitakkavicārehi cittassa bhaṅgakkhaṇe nirodhasamāpannānaṃ "
    "asaññasattānaṃ",
    "Dutiyajjhānaṃ tatiyajjhānaṃ samāpannānaṃ assāsapassāsānaṃ uppādakkhaṇe tesaṃyeva vinā assāsapassāsehi cittassa "
    "bhaṅgakkhaṇe catutthajjhānaṃ samāpannānaṃ suddhāvāsānaṃ dutiye citte vattamāne asaññasattānaṃ",
)
SAMPLE_LINES = (
    "(Ka) yassa kāyasaṅkhāro na nirujjhati tassa vacīsaṅkhāro na nirujjhitthāti? Nirujjhittha.",
    "(Kha) yassa vā pana vacīsaṅkhāro na nirujjhittha tassa kāyasaṅkhāro na nirujjhatīti? Natthi.",
    "Paṭhamajjhānaṃ samāpannānaṃ itaresaṃ kāmāvacarānaṃ tesaṃ tattha kāyasaṅkhāro na nirujjhittha vacīsaṅkhāro ca "
    "nirujjhissati.",
    "Yattha kāyasaṅkhāro uppajjati tattha vacīsaṅkhāro nirujjhatīti?",
    "Dutiyajjhāne tatiyajjhāne tattha…pe… (itaresaṃ yatthakānaṃ sadisaṃ).",
    "Yassa yattha kāyasaṅkhāro uppajjati…pe… (yassakampi yassayatthakampi sadisaṃ).",
    "Yassa yattha kāyasaṅkhāro nuppajjati…pe….",
    "Yassa kāyasaṅkhāro uppajjittha tassa vacīsaṅkhāro nirujjhitthāti? Āmantā.",
    "(Kha) yassa vā pana yattha…pe…? Āmantā.",
    "(Ka) yo kāyasaṅkhāraṃ parijānāti so vacīsaṅkhāraṃ parijānātīti? Āmantā.",
    "(Kha) yo vā pana vacīsaṅkhāraṃ parijānāti so kāyasaṅkhāraṃ parijānātīti? Āmantā.",
)


def notes():
    out = [f"# pi-6 rails {N} (Saṅkhārayamaka 2): nirodhavāra (end), uppādanirodhavāra, pariññāvāra", "",
           "Builder: build_rails_6-02_vi.py. Imports build_rails_6-01_vi READ-ONLY (and through it 2-01, 7-01, 8, 9-01, "
           "9-02, 3-02, 3-03, 2-02, 5-01, 10-01), 5-02 / 5-03 (note pieces), 3-01 (asammohantena), 3-05 (itaresaṃ "
           "yatthakānaṃ), 2-02 (family E). 6-01's parsers run in a private second instance whose own GEN adds "
           "pacchimacittassa «tâm cuối cùng» (= 9-02 / 8); the builder asserts that instance still reproduces the 6-01 "
           "chapter byte for byte. Exposed: `PSK`, `FINAL_MIND`, `NOTES`, `INLINE_NOTES`, `FIXED`, `frag`, "
           "`cut_with_note`, `heading`, `line_vi`, `tr_line`, `build`. Format: Pāli = tiếng Việt.", ""]

    def h(t):
        out.extend(["", f"## {t}", ""])

    def row(p, v):
        out.append(f"{p} = {v}")

    h("New strings set here")
    row("pacchimacittassa (genitive before a moment)", FINAL_MIND + "  (= 9-02 gen_vi)")
    row("Pariññāvāro (heading)", heading("Pariññāvāro"))
    row("1-6. Paccuppannavārādi", heading("1-6. Paccuppannavārādi"))
    for p, v in FIXED.items():
        row(p, v)
    for p, v in NOTES.items():
        row(p, v)
    for p, v in INLINE_NOTES.items():
        row(p + " (after a cut)", v)
    h("Answer heads as built (… tesaṃ / tesaṃ tattha / tattha …)")
    for hd in SAMPLE_HEADS:
        row(hd, PSK.answer_head(hd) + ", …")
    h("Sample lines as built")
    for ln in SAMPLE_LINES:
        row(ln, line_vi(ln))
    h("Termbase misfits and gaps (for the coordinator)")
    out += [
        "- Kāmāvacarānaṃ pacchimacittassa uppādakkhaṇe: no finished chapter has it. Read by 6-01's head parser as a "
        "person group followed by a moment, as 9-01's «Sabbesaṃ cittassa bhaṅgakkhaṇe» «Ở tất cả chúng sinh, vào "
        "khoảnh khắc tan rã của tâm»: «Ở chúng sinh trong cõi dục lạc, vào khoảnh khắc sinh khởi của tâm cuối cùng, ở "
        "chúng sinh trong cõi dục lạc mà tâm cuối cùng sẽ sinh khởi ngay sau tâm này, …» (meaning = «the final mind of "
        "beings in the sense sphere»; a «tâm cuối cùng của chúng sinh trong cõi dục lạc» shape would need a new "
        "frame). Please confirm.",
        "- Kāmāvacare / Rūpāvacare arūpāvacare / Savitakkasavicārabhūmiyaṃ / Avitakkaavicārabhūmiyaṃ before "
        "pacchimacittassa: places with their own «ở», then the moment (6-01 head_parts).",
        "- Notes: no termbase entries for vibhattā / vibhajitabbā(ṃ), sadisaṃ, labbhati, asammohantena, nānākaraṇaṃ: "
        "the 5-02 / 5-03 / 6-01 / 3-01 pieces; X-ena sadisaṃ «giống như X» (3-04 «giống như vậy»); "
        "itaresaṃ yatthakānaṃ sadisaṃ «giống như các phần về nơi chốn khác» (3-05 piece); "
        "Yathā nirodhavāre … (no vibhattā) «như ở mục về sự chấm dứt».",
        "- Clash between finished chapters (followed 5-02, which the coordinator lists): atītā pucchā «Các câu hỏi về "
        "quá khứ» and anulomampi paccanīkampi «cả chiều thuận lẫn chiều nghịch» (5-02 / 5-03) vs 3-05 «Câu hỏi về quá "
        "khứ …, theo chiều thuận và chiều nghịch»; vibhajitabbaṃ «cũng nên phân tích như vậy» (2-02 / 5-02 / 5-03) vs 4 "
        "«cũng nên được phân tích như vậy».",
        "- Yamaka titles inside a note in “…” with the heading form (4): khandhayamake «“Các cặp câu hỏi về các khối”», "
        "saṅkhārayamakepi «“Các cặp câu hỏi về các tạo tác”» (termbase lower case «các cặp câu hỏi về …»).",
        "",
        "## Pāli as written (reported)",
        "",
        "- ^6-6-121: «Paṭhamajjhānaṃ samāpannānaṃ itaresaṃ kāmāvacarānaṃ tesaṃ tattha kāyasaṅkhāro na nirujjhittha "
        "vacīsaṅkhāro ca nirujjhissati.» (Ka answer, second sentence): «na nirujjhittha» without «ca» after the first "
        "member; the parallel lines (^6-6-121 citta pair, ^6-6-122) have «A ca V1 B ca V2». Translated as written, "
        "not as the both-frame (its «cũng» would pair a denied verb with an affirmed one): «Ở những người đang nhập "
        "tầng thiền thứ nhất và chúng sinh khác trong cõi dục lạc, thì ở những người ấy, ở nơi ấy sự tạo tác bằng thân "
        "chưa từng chấm dứt, và sự tạo tác bằng lời nói sẽ chấm dứt.» Possible slip for «kāyasaṅkhāro ca "
        "nirujjhittha»; please check.",
        "- ^6-6-147: uppādavāranirodhavārepi (termbase «mục về sự sinh khởi và sự chấm dứt»); the repeated "
        "«paccuppannātītā pucchā anulomampi paccanīkampi» is kept twice. ^6-6-158: the repeated «atītānāgatā pucchā "
        "anulomampi paccanīkampi» kept twice.",
        "- ^6-6-135 / ^6-6-136 notes end «).»; ^6-6-147, ^6-6-158, the pariññāvāra note end «.)»: kept.",
        "- ^6-6-136 «Yassa kāyasaṅkhāro uppajjittha …ti? Āmantā.» has no label: kept unlabelled (6-01's pq_question).",
        "- ^6-6-130: «Dutiyajjhāne tatiyajjhāne tattha…pe…» an answer cut after «tattha»: «Ở tầng thiền thứ hai, ở "
        "tầng thiền thứ ba, thì ở nơi ấy…» (3-05 fragment shape).",
        "- ^6-6-159: the segment holds «Pariññāvāro.», «Saṅkhārayamakaṃ niṭṭhitaṃ.» and the homage of the next "
        "yamaka: kept as lines.",
        "",
    ]
    for what, where in dict.fromkeys(SLIPS + PSK.SLIPS_SEEN):
        out.append(f"- {what}: {where}")
    return "\n".join(out) + "\n"


def main():
    if "--probe" in sys.argv:
        probe()
        return
    S.check_reused()
    B.check_reused()
    DY.check_reused()
    SK.check_reused()
    SK.check_shared()
    check_termbase()
    check_shared()
    PSK.SLIPS_SEEN.clear()
    segs = build()
    S.write(CHAPTER, segs)
    ADH_DIR.mkdir(exist_ok=True)
    (ADH_DIR / CHAPTER).write_bytes((S.OUT_DIR / CHAPTER).read_bytes())
    print("wrote", ADH_DIR / CHAPTER)
    NOTES_MD.write_text(unicodedata.normalize("NFC", notes()), encoding="utf-8", newline="\n")
    print("wrote", NOTES_MD)
    for s in dict.fromkeys(SLIPS + PSK.SLIPS_SEEN):
        print("note:", s)


if __name__ == "__main__":
    main()
