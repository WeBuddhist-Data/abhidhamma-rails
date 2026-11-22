"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 9-03 (Dhammayamaka 3: the rest of the uppādanirodhavāra, the
bhāvanāvāra and the closing lines of the Dhammayamaka).

Everything in the pavattivāra comes from build_rails_9-02_vi (its line translator, unchanged) and, through it,
build_rails_9-01_vi (members, verbs, questions, answer heads), 2-01 (families A, B), 7-01 (answer shapes) and 8
(moments, kinds of mind). The bhāvanāvāra uses family E's shell from build_rails_2-02_vi (yo_q, make_verbs,
rows_na, rows_fused, e_verb, YO_RE, pe_tail). All imported READ-ONLY. New here:
  BHAVETI / PAJAHATI            bhāveti «tu tập» / pajahati «dứt bỏ» (termbase; kept distinct, asserted)
  BHAVANA_VERBS / PAJAHANA_VERBS / BV_VERBS   their tense tables (family E rule: «V / không V», «đã V / chưa từng V»,
                                «sẽ V / sẽ không V»)
  BV_OBJECTS / bv_slot() / bv_question() / bv_answers()   "yo kusalaṃ dhammaṃ bhāveti so akusalaṃ dhammaṃ
                                pajahatīti?" = «Người nào mà tu tập hiện tượng thiện, thì người ấy có phải dứt bỏ hiện
                                tượng bất thiện không?»
  BHAVANAVARO / FIXED / HEADINGS   Bhāvanāvāro «Mục về sự tu tập», the Dhammayamaka closing, homage, Abhidhammapiṭake
  LINE_SLIPS / tr_line() / build()   the line translator (9-02's for everything else)
A line the parsers cannot place raises ValueError: there is no silent fallback.

Import READ-ONLY (importing writes nothing):
    sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai\\rails")
    import importlib; DY3 = importlib.import_module("build_rails_9-03_vi")

usage: python -I -X utf8 -B build_rails_9-03_vi.py [--probe]
"""
import importlib
import pathlib
import re
import sys
import unicodedata

RAILS_DIR = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\rails")
if str(RAILS_DIR) not in sys.path:
    sys.path.insert(0, str(RAILS_DIR))
import build_rails_sample_vi as S  # noqa: E402  (READ-ONLY)
DY2 = importlib.import_module("build_rails_9-02_vi")   # Dhammayamaka 2 translator (READ-ONLY)
DY = DY2.DY                                            # build_rails_9-01_vi (READ-ONLY)
B, C, D = DY.B, DY.C, DY.D                             # 2-01, 7-01, 8 (READ-ONLY)
E = importlib.import_module("build_rails_2-02_vi")     # family E: pariññāvāra shell (READ-ONLY)

CHAPTER = "9-03-dhammayamaka.md"
N = "9-03"
NOTES_MD = RAILS_DIR / f"notes-rails-{N}.md"
ADH_DIR = RAILS_DIR / f"adh-{N}"
TERMBASE = S.ROOT / "AI_translation/vietnamese/pi-6-pali-vietnamese-termbase-plain.md"
cap = S.cap
PE = S.PE
SLIPS_SEEN = []


# ===============================================================================================================
# 1. Bhāvanāvāra: verbs (family E tense rule; bhāveti and pajahati kept distinct)
# ===============================================================================================================
BHAVETI = "tu tập"                        # bhāveti / bhāvetīti (termbase; pi-1 «tu tập hiện tượng …», pi-5 «tu tập con đường»)
PAJAHATI = C.FAMILY_TERMS["pajahati"]     # pajahati «dứt bỏ» (termbase; = 7-01 FAMILY_TERMS, 7-05 … 7-07)
BHAVANA_VERBS = E.make_verbs(BHAVETI, E.rows_na("bhāveti", "bhāventi", "bhāvittha", "bhāvessati", "bhāvessanti"))
PAJAHANA_VERBS = E.make_verbs(PAJAHATI, E.rows_fused(
    ("pajahati", "pajahanti", "pajahittha", "pajahissati", "pajahissanti"),
    ("nappajahati", "nappajahanti", "nappajahittha", "nappajahissati", "nappajahissanti")))
BV_VERBS = {**BHAVANA_VERBS, **PAJAHANA_VERBS}
assert len(BV_VERBS) == len(BHAVANA_VERBS) + len(PAJAHANA_VERBS)

# objects (accusative sg.): termbase kusalaṃ dhammaṃ «hiện tượng thiện», akusalaṃ dhammaṃ «hiện tượng bất thiện»
# (= 9-01 DHAMMA "Kusalaṃ" / "Akusalaṃ" subject, the sample SUBJ)
BV_OBJECTS = {
    "kusalaṃ dhammaṃ": DY.DHAMMA.subj("kusalaṃ"),
    "akusalaṃ dhammaṃ": DY.DHAMMA.subj("akusalaṃ"),
}


def bv_slot(text):
    """'kusalaṃ dhammaṃ [na] bhāveti' / 'akusalaṃ dhammaṃ nappajahatīti' → «[không] tu tập hiện tượng thiện» /
    «không dứt bỏ hiện tượng bất thiện» (family E order: verb before the object, = E.ov)."""
    w = text.split()
    for k in (2, 1):
        if len(w) > k and E.is_e_verb(" ".join(w[-k:]), BV_VERBS):
            obj = " ".join(w[:-k])
            if obj not in BV_OBJECTS:
                raise ValueError(f"unknown bhāvanāvāra object {obj!r} in {text!r}")
            return f"{E.e_verb(' '.join(w[-k:]), BV_VERBS).vi} {BV_OBJECTS[obj]}"
    raise ValueError(f"no bhāvanāvāra verb in {text!r}")


def _exact(s):
    if s not in C.EXACT:
        raise ValueError(f"unknown bhāvanāvāra answer {s!r}")
    return C.EXACT[s]


def bv_answers(text):
    """'Āmantā.' / 'Āmantā…pe….' → «Đúng vậy.» / «Đúng vậy…» (C.EXACT; E.pe_tail: «.» before …pe… absorbed)."""
    out = []
    for x in [x for x in re.split(r"(?<=\.) ", text.strip()) if x]:
        if x in C.EXACT:
            out.append(C.EXACT[x])
        elif (t := E.pe_tail(x, _exact)) is not None:
            out.append(t)
        else:
            raise ValueError(f"unknown bhāvanāvāra answer {x!r}")
    return " ".join(out)


def bv_question(body):
    """(Ka) yo A V1 so B V2ti? = «(a) Người nào mà V1 A, thì người ấy có phải V2 B không?» (E.yo_q);
    (Kha) yo vā pana … = «(b) Còn người nào mà …». None if the line is not a yo … so … question."""
    m = E.YO_RE.fullmatch(body)
    if not m:
        return None
    label, y, vapana, a, b, rest = m.groups()
    if bool(label) != (y == "y"):
        raise ValueError(f"label / capital mismatch: {body!r}")
    if label in ("Ka", "Kha") and (label == "Kha") != bool(vapana):
        raise ValueError(f"label {label} with vā pana={bool(vapana)}: {body!r}")
    out = E.yo_q(bv_slot(a), bv_slot(b), label, bool(vapana))
    return out + (" " + bv_answers(rest) if rest else "")


# ===============================================================================================================
# 2. Headings and fixed lines
# ===============================================================================================================
BHAVANAVARO = f"Mục về sự {BHAVETI}"      # Bhāvanāvāro (termbase «mục về sự tu tập»; = «Mục về sự hiểu biết trọn vẹn»)
ABHI_LINE = S.H_ABHI[2:]                  # Abhidhammapiṭake as a plain line (pi-1 «# Tạng Vi Diệu Pháp» without «# »)
HEADINGS = {"Bhāvanāvāro": BHAVANAVARO}
FIXED = {
    "Bhāvanāvāro.": BHAVANAVARO + ".",                   # closing (= 2-02 «Pariññāvāro.» «Mục về sự hiểu biết trọn vẹn.»)
    "Dhammayamakaṃ niṭṭhitaṃ.": S.yamaka_end("Dhamma"),  # «Phần các cặp câu hỏi về các hiện tượng đã hoàn tất.» (= 4, 8)
    "Namo tassa bhagavato arahato sammāsambuddhassa": S.HOMAGE,
    "Abhidhammapiṭake": ABHI_LINE,
}

# ^6-9-192: a comma after "paṭilabhissanti" inside a person run; the parallel ^6-9-198 has none. Absorbed: the
# Vietnamese list already separates the groups (= the comma-less head, identical Vietnamese; as 2-02 absorbs a
# comma inside the both-frame). Reported.
LINE_SLIPS = {
    "aggamaggaṃ paṭilabhissanti, asaññasattānaṃ": "aggamaggaṃ paṭilabhissanti asaññasattānaṃ",
}


# ===============================================================================================================
# 3. Line translator (9-02's for the pavattivāra)
# ===============================================================================================================
def tr_line(p):
    m = re.search(r" (\^\S+)$", p)
    bid = m.group(1) if m else None
    body = p[:m.start()] if m else p
    for k, v in LINE_SLIPS.items():
        if k in body:
            SLIPS_SEEN.append((bid, k))
            body = body.replace(k, v)
    if body.startswith("#"):
        hashes, text = body.split(" ", 1)
        out = f"{hashes} {HEADINGS[text]}" if text in HEADINGS else DY2.tr_line(body)
    elif body in FIXED:
        out = FIXED[body]
    elif (q := bv_question(body)) is not None:
        out = q
    else:
        out = DY2.tr_line(body)
    return f"{out} {bid}" if bid else out


def build(name=CHAPTER):
    segs = []
    for seg in S.segments_of(name):
        out = []
        for ln in seg:
            try:
                out.append(tr_line(ln))
            except ValueError as e:
                raise ValueError(f"{name}: cannot place line {ln[:140]!r}: {e}") from None
        segs.append(out)
    return segs


def probe(name=CHAPTER):
    bad = 0
    for seg in S.segments_of(name):
        for ln in seg:
            try:
                tr_line(ln)
            except ValueError as e:
                bad += 1
                print("FAIL:", e, "\n   ", ln[:160])
    print("failing lines:", bad)


# ===============================================================================================================
# 4. Assertions: termbase, pi-N rails, shared strings
# ===============================================================================================================
TERMBASE_USED = [
    ("bhāveti", BHAVETI), ("bhāvetīti", BHAVETI), ("pajahati", PAJAHATI), ("pajahatīti", PAJAHATI),
    ("nappajahati", "không " + PAJAHATI), ("nappajahatīti", "không " + PAJAHATI),
    ("kusalaṃ dhammaṃ", BV_OBJECTS["kusalaṃ dhammaṃ"]), ("akusalaṃ dhammaṃ", BV_OBJECTS["akusalaṃ dhammaṃ"]),
    ("Bhāvanāvāro", "mục về sự " + BHAVETI), ("Dhammayamakaṃ", "Các cặp câu hỏi về các hiện tượng"),
    ("Abhidhammapiṭake", ABHI_LINE), ("Namo", "Kính lễ"),
]
REUSED = [   # (Pāli, Vietnamese, book): asserted to occur in that book's Vietnamese rails
    ("lokuttaraṃ dhammaṃ bhāveti (pi-1 2-03-cittuppadakandam)", f"{BHAVETI} hiện tượng", "1"),
    ("samudayaṃ pajahati … maggaṃ bhāveti (pi-5 12-catutthavaggo)", f"{PAJAHATI} sự phát sinh", "5"),
    ("maggaṃ bhāveti (pi-5 12-catutthavaggo)", f"{BHAVETI} con đường", "5"),
]


def check_reused():
    tb = TERMBASE.read_text(encoding="utf-8")
    bad = [(p, v) for p, v in TERMBASE_USED
           if not re.search(r"^" + re.escape(p) + r": \{[^\n]*: " + re.escape(v) + r"[};]", tb, re.M | re.I)]
    assert not bad, "termbase strings not found: " + repr(bad)
    texts = {b: unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md"))))
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED if unicodedata.normalize("NFC", v).lower() not in texts[b].lower()]
    assert not bad, "reused strings not found in their rails: " + repr(bad)


def check_shared():
    """Strings that must equal the setters' byte for byte."""
    assert DY2.DY is DY and E.B is B and E.C is C
    # bhāveti / pajahati distinct; family E tense rule (= 2-02 / family B)
    assert BHAVETI != PAJAHATI and not set(BHAVANA_VERBS) & set(PAJAHANA_VERBS)
    assert BV_VERBS["bhāveti"].vi == BHAVETI and BV_VERBS["na bhāveti"].vi == "không " + BHAVETI
    assert BV_VERBS["bhāvittha"].vi == "đã " + BHAVETI and BV_VERBS["na bhāvittha"].vi == "chưa từng " + BHAVETI
    assert BV_VERBS["nappajahati"].vi == C.FAMILY_TERMS["nappajahati"]
    assert BV_VERBS["nappajahissanti"].vi == C.FAMILY_TERMS["nappajahissanti"]
    for f, v in BV_VERBS.items():
        base = BHAVETI if f in BHAVANA_VERBS else PAJAHATI
        assert (v.pos_vi, v.neg_vi) == E.tense_vi(base, v.tense), f
    assert BV_OBJECTS["kusalaṃ dhammaṃ"] == S.SUBJ["kusala"] and BV_OBJECTS["akusalaṃ dhammaṃ"] == S.SUBJ["akusala"]
    # the question shell is family E's (2-02 yo_q = 7-03 wording)
    assert bv_question("(Ka) yo kusalaṃ dhammaṃ bhāveti so akusalaṃ dhammaṃ pajahatīti?") == \
        E.yo_q(f"{BHAVETI} {S.SUBJ['kusala']}", f"{PAJAHATI} {S.SUBJ['akusala']}", "Ka")
    assert BHAVANAVARO + "." == E.PARINNAVARO_CLOSE.replace("hiểu biết trọn vẹn", BHAVETI)
    assert FIXED["Dhammayamakaṃ niṭṭhitaṃ."] == f"Phần {S.yamaka_title('Dhamma')[0].lower()}" \
        f"{S.yamaka_title('Dhamma')[1:]} {S.NITTHITO}."
    # the comma slip gives the same Vietnamese as the comma-less parallel (^6-9-198 head)
    h = "Aggamaggasamaṅgīnaṃ arahantānaṃ yassa cittassa anantarā aggamaggaṃ paṭilabhissanti asaññasattānaṃ"
    s = f"{h} tesaṃ tattha abyākatā dhammā nirujjhissanti, no ca tesaṃ tattha kusalā dhammā uppajjissanti."
    assert tr_line(s.replace("paṭilabhissanti ", "paṭilabhissanti, ")) == DY2.sentence(s)
    # this translator reproduces the 9-02 and 9-01 chapters byte for byte (identical Pāli = identical Vietnamese)
    for ch in (DY2.CHAPTER, DY.CHAPTER):
        vi = (S.OUT_DIR / ch).read_text(encoding="utf-8")
        assert "\n\n".join("\n".join(tr_line(x) for x in seg) for seg in S.segments_of(ch)) + "\n" == vi, ch
    SLIPS_SEEN.clear()


# ===============================================================================================================
# 5. Notes file (Pāli = tiếng Việt)
# ===============================================================================================================
def notes():
    out = [f"# pi-6 rails {N} (Dhammayamaka 3): end of the uppādanirodhavāra, the bhāvanāvāra, the closing lines", "",
           "Builder: build_rails_9-03_vi.py. Imports build_rails_9-02_vi READ-ONLY (its translator, unchanged, for the "
           "whole pavattivāra; through it 9-01, 2-01, 7-01, 8) and build_rails_2-02_vi (family E: `yo_q`, `make_verbs`, "
           "`rows_na`, `rows_fused`, `e_verb`, `YO_RE`, `pe_tail`). New named constants: `BHAVETI`, `PAJAHATI`, "
           "`BHAVANA_VERBS`, `PAJAHANA_VERBS`, `BV_VERBS`, `BV_OBJECTS`, `bv_slot`, `bv_question`, `bv_answers`, "
           "`BHAVANAVARO`, `ABHI_LINE`, `HEADINGS`, `FIXED`, `LINE_SLIPS`, `tr_line`, `build`. The builder asserts that "
           "its translator reproduces the 9-01 and 9-02 chapters byte for byte. Format: Pāli = tiếng Việt.", ""]

    def h(t):
        out.extend(["", f"## {t}", ""])

    def row(p, v):
        out.append(f"{p} = {v}")

    h("Bhāvanāvāra: verbs (family E tense rule, 2-02; bhāveti and pajahati distinct)")
    for f, v in BV_VERBS.items():
        row(f, v.vi)
    row("after no ca (not met here)", "negative denied «vẫn V / đã từng V / vẫn sẽ V», positive «không V …» (2-02)")
    h("Bhāvanāvāra: objects and questions (family E shell, 2-02 yo_q)")
    for k, v in BV_OBJECTS.items():
        row(k, v)
    for q in ("(Ka) yo kusalaṃ dhammaṃ bhāveti so akusalaṃ dhammaṃ pajahatīti? Āmantā.",
              "(Kha) yo vā pana akusalaṃ dhammaṃ pajahati so kusalaṃ dhammaṃ bhāvetīti? Āmantā.",
              "(Ka) yo kusalaṃ dhammaṃ na bhāveti so akusalaṃ dhammaṃ nappajahatīti? Āmantā.",
              "(Kha) yo vā pana akusalaṃ dhammaṃ nappajahati so kusalaṃ dhammaṃ na bhāvetīti? Āmantā…pe…."):
        row(q, tr_line(q))
    h("Headings and closing lines")
    row("Bhāvanāvāro (heading)", BHAVANAVARO)
    for k, v in FIXED.items():
        row(k, v)
    for p in ("(3) Anāgatavāro", "(4) Paccuppannātītavāro", "(5) Paccuppannānāgatavāro", "(6) Atītānāgatavāro"):
        row(p, DY.heading(p))
    for p in ("Uppādanirodhavāro.", "Pavattivāro niṭṭhito."):
        row(p, DY.sentence(p))
    h("Sample pavattivāra lines as built (9-02 / 9-01 strings)")
    for s in ("Aggamaggasamaṅgīnaṃ arahantānaṃ tesaṃ abyākatā dhammā nirujjhissanti, no ca tesaṃ kusalā dhammā "
              "uppajjissanti.",
              "Yassa cittassa anantarā aggamaggaṃ paṭilabhissanti tesaṃ akusalā dhammā na nirujjhissanti, no ca tesaṃ "
              "kusalā dhammā na uppajjissanti.",
              "Aggamaggassa bhaṅgakkhaṇe arahantānaṃ yassa cittassa anantarā aggamaggaṃ paṭilabhissanti tassa cittassa "
              "bhaṅgakkhaṇe tesaṃ akusalā ca dhammā na nirujjhissanti kusalā ca dhammā na uppajjanti.",
              "(Kha) yassa vā pana yattha abyākatā dhammā na nirujjhissanti tassa tattha kusalā dhammā na "
              "uppajjitthāti? Uppajjittha.",
              "Yattha kusalā dhammā na uppajjittha tattha akusalā dhammā na nirujjhissantīti?…Pe…."):
        row(s, tr_line(s))
    h("Termbase misfits and gaps (for the coordinator)")
    out += [
        "- bhāveti «tu tập», pajahati «dứt bỏ», kusalaṃ / akusalaṃ dhammaṃ «hiện tượng thiện / bất thiện», "
        "Bhāvanāvāro «mục về sự tu tập»: termbase, no misfit. The negative forms (na bhāveti «không tu tập», "
        "nappajahati «không dứt bỏ») follow the family E / B rule; the other tenses (bhāvittha, bhāvessati …, "
        "pajahittha …) are in the tables for later chapters, not met here.",
        "- Abhidhammapiṭake as a plain last line (no #): «Tạng Vi Diệu Pháp» (termbase; pi-1 heading wording without "
        "the #).",
        "",
        "## Pāli as written (reported)",
        "",
        "- ^6-9-192: «… aggamaggaṃ paṭilabhissanti, asaññasattānaṃ tesaṃ tattha …»: a comma inside the person run (the "
        "parallel ^6-9-198 has none); absorbed, the head is the comma-less one: «Ở những người có được con đường tối "
        "thượng, các bậc A-la-hán, những người sẽ đạt được con đường tối thượng ngay sau tâm này và chúng sinh Vô "
        "Tưởng, …».",
        "- ^6-9-192 (suspected slip): the question asks about akusalā, the 'no ca' part reads «no ca tesaṃ tattha "
        "kusalā dhammā uppajjissanti» (the parallel ^6-9-188 and the Itaresaṃ sentence have akusalā): translated as "
        "written, «… không có các hiện tượng thiện sẽ sinh khởi», for review.",
        "- ^6-9-229: «Āmantā…pe….» = «Đúng vậy…»; the segment also holds «Bhāvanāvāro.», «Dhammayamakaṃ niṭṭhitaṃ.», "
        "the homage and «Abhidhammapiṭake» as lines (8 lines kept).",
        "- ^6-9-228: «Uppādanirodhavāro.» (no niṭṭhito) then «Pavattivāro niṭṭhito.» (9-01 / 2-01 closings).",
        "- ^6-9-201, ^6-9-206, ^6-9-211, ^6-9-216, ^6-9-221, ^6-9-226: unlabelled «Yattha …ti?…Pe….» = «… không?…» (9-01).",
        "",
    ]
    return "\n".join(out)


def main():
    if "--probe" in sys.argv:
        probe()
        return
    S.check_reused()
    B.check_reused()
    DY.check_reused()
    DY.check_shared()
    DY2.check_reused()
    DY2.check_shared()
    check_reused()
    check_shared()
    segs = build()
    S.write(CHAPTER, segs)
    ADH_DIR.mkdir(exist_ok=True)
    (ADH_DIR / CHAPTER).write_bytes((S.OUT_DIR / CHAPTER).read_bytes())
    print("wrote", ADH_DIR / CHAPTER)
    NOTES_MD.write_text(unicodedata.normalize("NFC", notes()), encoding="utf-8", newline="\n")
    print("wrote", NOTES_MD)
    for bid, k in SLIPS_SEEN:
        print("slip:", bid, "|", k)


if __name__ == "__main__":
    main()
