# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 9-03-dhammayamaka.md (Dhammayamaka part 3: the time sections
(3)-(6) of the uppādanirodhavāra, the bhāvanāvāra and the close of the Dhammayamaka).

Frames come from build_9-02_vi (who9 with the 9-02 elements, b_answer, plain heading lines) and through it from
build_9-01_vi (members, B questions, short answers, «?…Pe….», and the bhāvanāvāra frames it settled ahead for this
chapter: BH_VERB, bh_q, BHAVANAVARO), build_2-01_vi (families A / B), build_2-02_vi, build_8_vi and build_7-01_vi.

Added here (listed in notes-9-03.md):
  - the answer head of ^6-9-192 that the Pāli prints with a comma inside the person list
    («… paṭilabhissanti, asaññasattānaṃ»): the comma is a list comma, the Vietnamese list is already comma-joined,
    so it is rendered exactly as the same head without the comma (^6-9-198);
  - the bhāvanāvāra question parser (bh_question) on 9-01's bh_q;
  - «Āmantā…pe….» = «Đúng vậy…» (build_8_vi ^6-8-115 form);
  - Bhāvanāvāro. / Dhammayamakaṃ niṭṭhitaṃ. / Namo … / Abhidhammapiṭake (sample constants).

Importing writes nothing; run  python -I -X utf8 -B build_9-03_vi.py  to build the chapter.
"""
import importlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as S  # noqa: E402

G = importlib.import_module("build_9-02_vi")     # Dhammayamaka part 2 (who9 with 9-02 elements)
D = G.D                                          # build_9-01_vi (Dhammayamaka frame-setter)
F = D.F                                          # build_2-01_vi (families A / B)
E = D.E                                          # build_2-02_vi
C8 = D.C8                                        # build_8_vi
A7 = D.A7                                        # build_7-01_vi

NAME = "9-03-dhammayamaka.md"
cap, low = S.cap, S.low
SLIPS = []

# ================================================================ closing lines and headings
AMANTA_PE = S.AMANTA[:-1] + A7.PE                 # Āmantā…pe…. = «Đúng vậy…» (build_8_vi ^6-8-115)
EXACT = {
    "Bhāvanāvāro.": D.BHAVANAVARO + ".",                          # = «Uppādavāro.» pattern (9-01)
    "Dhammayamakaṃ niṭṭhitaṃ.": S.yamaka_end("Dhammayamakaṃ"),    # = 6-02 «Saṅkhārayamakaṃ niṭṭhitaṃ.»
    "Namo tassa bhagavato arahato sammāsambuddhassa": S.HOMAGE,
    "Abhidhammapiṭake": S.PITAKA,                                 # plain line here (preamble: # heading)
    "Āmantā…pe….": AMANTA_PE,
}
HEAD = {"Bhāvanāvāro": D.BHAVANAVARO}


def heading(t):
    return HEAD.get(t) or D.heading(t)


# ================================================================ answer heads
def who9(phrase):
    """= build_9-02_vi.who9; a list comma inside the Pāli person list (^6-9-192) is the Vietnamese LIST_SEP anyway."""
    return G.who9(phrase.replace(", ", " "))


def b_answer(s):
    """= build_9-02_vi.b_answer, using who9 above."""
    for rx, both in ((D.B_NOT9, False), (D.B_BOTH9, True)):
        m = rx.fullmatch(s)
        if not m:
            continue
        if not both:
            assert m["r"] == m["r2"], s
        res = m["r"]
        head = D.where9(m["g"]) if res == "tattha" else who9(m["g"])
        f = F.b_both if both else F.b_not
        return f(res, head, D.member(m["x"]), D.vparse9(m["v1"]), D.member(m["y"]), D.vparse9(m["v2"]))
    return None


# ================================================================ bhāvanāvāra (9-01 BH_VERB / bh_q)
BH_STEM = "akusala|kusala"
BH_V = "na bhāveti|bhāveti|nappajahati|pajahati"
# second verb carries the quotative: «pajahatīti?» / «bhāvetīti?» -> stem + «tīti?», mapped back to the BH_VERB key
BH_Q = re.compile(rf"\((?P<l>Ka|Kha)\) yo (?P<vp>vā pana )?(?P<x>{BH_STEM})ṃ dhammaṃ (?P<v1>{BH_V}) so "
                  rf"(?P<y>{BH_STEM})ṃ dhammaṃ (?P<v2>na bhāve|bhāve|nappajaha|pajaha)tīti\?")


def bh_question(s):
    m = BH_Q.fullmatch(s)
    if not m:
        return None
    vapana = bool(m["vp"])
    if vapana != (m["l"] == "Kha"):
        SLIPS.append(f"label ({m['l']}) on a {'vā pana' if vapana else 'non-vā pana'} question: {s[:60]}")
    return D.bh_q(m["x"], m["v1"], m["y"], m["v2"] + "ti", label=m["l"], vapana=vapana)


# ================================================================ sentence / line translation
def translate_sentence(s, ctx=""):
    if s in EXACT:
        return EXACT[s]
    if s.endswith(D.PE_Q):
        return translate_sentence(s[:-len(D.PE_Q) + 1], ctx) + " " + A7.PE
    for fn in (bh_question, b_answer):
        r = fn(s)
        if r:
            return r
    return G.translate_sentence(s, ctx)


def translate_line(line, ctx=""):
    m = re.match(r"^(?P<h>#+ )?(?P<t>.*?)(?P<id> \^[0-9A-Za-z-]+)?$", line)
    h, t, sid = m["h"] or "", m["t"], m["id"] or ""
    if h:
        return h + heading(t) + sid
    if t in G.PLAIN_HEADINGS:
        return D.heading(t) + sid
    if t in EXACT:
        return EXACT[t] + sid
    if t in D.EXACT:
        return D.EXACT[t] + sid
    return " ".join(translate_sentence(x, ctx) for x in F.split_sentences(t)) + sid


def translate_file(name=NAME):
    src = (S.PALI_DIR / name).read_text(encoding="utf-8")
    out, seg = [], "start"
    for ln in src.splitlines():
        out.append(translate_line(ln, f"segment after ^{seg}") if ln.strip() else "")
        mid = re.search(r"\^([0-9A-Za-z-]+)\s*$", ln)
        if mid:
            seg = mid.group(1)
    text = "\n".join(out).rstrip("\n") + "\n"
    return re.sub(r"\n{3,}", "\n\n", text)


# ================================================================ checks
CROSS_BOOK = [
    (S.HOMAGE, 1), (S.PITAKA, 1), ("sự tu tập", 1), ("tu tập", 1), ("dứt bỏ", 1), ("đã hoàn tất", 1),
]


def check_cross_book():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in S.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts (9-03): {len(CROSS_BOOK)} strings found in pi-1..5 rails")


def _sentences(text):
    for p in text.splitlines():
        if not p.strip() or p.startswith("#"):
            continue
        p = re.sub(r"\s*\^[\w-]+$", "", p)
        if p in EXACT or p in D.EXACT or p in G.PLAIN_HEADINGS:
            continue
        yield from F.split_sentences(p)


def check_repeats(pali):
    """Identical Pāli sentence -> identical Vietnamese within 9-03, and against 9-01 / 9-02 / 2-01 / 2-02 / 8."""
    seen, bad = {}, 0
    for s in _sentences(pali):
        t = translate_sentence(s)
        if seen.setdefault(s, t) != t:
            bad += 1
    shared = 0
    for mod in (G, D, F, E):
        other = (S.PALI_DIR / mod.NAME).read_text(encoding="utf-8")
        for s in set(_sentences(other)) & set(seen):
            shared += 1
            if mod.translate_sentence(s, "") != seen[s]:
                print(f"DIFFERS FROM {mod.NAME}:", s)
                bad += 1
    print(f"repeat check: {len(seen)} distinct sentences, {shared} shared with 9-02 / 9-01 / 2-01 / 2-02")
    return bad


def check_frames():
    assert D.bh_q("kusala", "bhāveti", "akusala", "pajahati") == \
        "(a) Người nào tu tập hiện tượng thiện, thì có phải người ấy dứt bỏ hiện tượng bất thiện không?"
    assert translate_sentence("(Ka) yo kusalaṃ dhammaṃ bhāveti so akusalaṃ dhammaṃ pajahatīti?") == \
        D.bh_q("kusala", "bhāveti", "akusala", "pajahati")
    assert who9("Aggamaggasamaṅgīnaṃ arahantānaṃ yassa cittassa anantarā aggamaggaṃ paṭilabhissanti, "
                "asaññasattānaṃ") == G.who9("Aggamaggasamaṅgīnaṃ arahantānaṃ yassa cittassa anantarā aggamaggaṃ "
                                            "paṭilabhissanti asaññasattānaṃ")
    assert AMANTA_PE == "Đúng vậy" + "…"
    assert EXACT["Dhammayamakaṃ niṭṭhitaṃ."] == "Phần các cặp câu hỏi về các hiện tượng đã hoàn tất."
    assert heading("Bhāvanāvāro") == "Mục về sự tu tập"
    # the Uppādanirodhavāra lines shared with 9-02 come out byte-identical
    for s in ("Uppādanirodhavāro.", "Pavattivāro niṭṭhito.", "Natthi.", "Āmantā."):
        assert translate_sentence(s) == G.translate_sentence(s)


def main():
    S.check_cross_book()
    F.check_cross_book()
    D.check_cross_book()
    G.check_cross_book()
    check_cross_book()
    check_frames()
    D.SLIPS.clear()
    SLIPS.clear()
    text = unicodedata.normalize("NFC", translate_file())
    pali = (S.PALI_DIR / NAME).read_text(encoding="utf-8")
    probs = S.check_lines(pali, text, NAME)
    for bad in ("….", ".…", "?…", ",…", "  ", "là là", "—", ":-"):
        assert bad not in text, bad
    assert check_repeats(pali) == 0, "identical Pāli rendered differently"
    with open(S.OUT_DIR / NAME, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    segs = len(re.findall(r"\^[0-9A-Za-z-]+\s*$", text, flags=re.M))
    print(f"wrote {NAME}: {len([x for x in text.splitlines() if x.strip()])} lines, {segs} segments")
    for w in D.SLIPS + SLIPS:
        print("SLIP", w)
    for p in probs[:80]:
        print("PROBLEM", p)
    print("line checks:", "OK" if not probs else f"{len(probs)} problems")
    sys.exit(1 if probs else 0)


if __name__ == "__main__":
    main()
