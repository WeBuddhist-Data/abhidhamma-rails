# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 5-03-saccayamaka.md (Saccayamaka: uppādanirodhavāra (5)-(6), close of
the pavattivāra, pariññāvāra, close of the Saccayamaka).

Every frame comes VERBATIM from the frame-setters:
  build_5-02_vi (P): its translate_sentence() and the in-memory extensions of build_5-01_vi it makes on import
                     (pacchimacitta moment, variant bracket closing a head); import it FIRST;
  build_5-01_vi (T): sacca members m(), the answer-head parser head_vi(), variant(), family A / B sentences;
  build_2-01_vi (F): families A / B (verbs and tenses verb() / deny(), STATEMENT_RES, RES_VI …);
  build_2-02_vi (E): family E (pariññāvāra: e_q, e_pred, e_deny, e_subject, E_BUT_C, E_BOTH_C, E_TE, PARINNA_EXACT),
                     pe_end(), «Uppādanirodhavāro.», «Pavattivāro niṭṭhito.»;
  build_7-01_vi (A7): YO_VERB["pajahati"] / ["nappajahati"] «dứt bỏ» (= 7-05 / 7-06 / 9-03);
  build_8_vi (C8):   PE;
  build_sample_vi (S): LABEL, SECTION, yamaka_end().
Settled here (listed in notes-5-03.md): pajahati in its three tenses inside the family-E frames, «no ca te» in a
pariññā answer, the «(Kha) yo vā pana…pe…?» shortening, aggaphala, a variant bracket inside an
«asaññasattaṃ / asaññasattā» group, the two-head «…pe…» half-answers with a member, the editorial note of ^6-5-164.

Local extensions of build_5-01_vi (additive only, in memory; nothing T or P already translated changes): two
HEAD_RULES_C entries (aggaphalassa …kkhaṇe; asaññasattaṃ [var] upapajjantānaṃ / asaññasattā [var] cavantānaṃ).

Importing writes nothing; run  python -I -X utf8 -B build_5-03_vi.py  to rebuild the chapter.
"""
import importlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as S  # noqa: E402

P = importlib.import_module("build_5-02_vi")     # previous chapter of this yamaka (extends T on import)
T = importlib.import_module("build_5-01_vi")     # this yamaka's frame-setter
F = importlib.import_module("build_2-01_vi")     # families A / B
E = importlib.import_module("build_2-02_vi")     # family E
A7 = importlib.import_module("build_7-01_vi")    # YO_VERB pajahati
C8 = importlib.import_module("build_8_vi")       # PE
assert P.T is T and T.F is F and T.E is E and T.C8 is C8

NAME = "5-03-saccayamaka.md"
cap, low = S.cap, S.low
LABEL_VI = S.LABEL
PE = C8.PE                                        # …pe… = …
SLIPS = []

# ================================================================ local extensions of the 5-01 head parser
# aggaphalassa uppādakkhaṇe = vào khoảnh khắc sinh khởi của thành quả tối thượng (aggamagga «con đường tối thượng»,
# coordinator; phala «thành quả», 5-01)
AGGAPHALA = "thành quả tối thượng"
AGGAPHALA_RX = re.compile(r"(?:aggaphalassa (?P<mo>uppāda|bhaṅga)kkhaṇe)(?P<comma>,)?(?: |$)")
# asaññasattaṃ [apāyaṃ asaññasattaṃ (syā.)] upapajjantānaṃ / asaññasattā [apāyā asaññasattā (syā.)] cavantānaṃ:
# the variant replaces the plane word; in Vietnamese it follows the whole group (as 5-01 ^6-5-69)
ASANNA_VAR_RX = re.compile(r"(?:(?P<pl>asaññasatt(?:aṃ|ā)) (?P<v>\[[^\]]+\]) (?P<p>upapajjantānaṃ|cavantānaṃ))"
                           r"(?P<comma>,)?(?: |$)")


def _asanna_var(g):
    return T._who01(f"{g['pl']} {g['p']}") + " " + T.variant(g["v"])


for _rx, _kind, _fn in ((AGGAPHALA_RX, "T", lambda g: T._moment(g["mo"], AGGAPHALA)),
                        (ASANNA_VAR_RX, "P", _asanna_var)):
    if not any(rx.pattern == _rx.pattern for rx, _k, _f in T.HEAD_RULES_C):
        T.HEAD_RULES_C.append((_rx, _kind, _fn))

# ================================================================ family E with pajahati (2-02 frames)
# pajahati = dứt bỏ (7-01 YO_VERB, = 7-05 / 7-06 / 9-03); tenses / polarity / «no ca» denial = the 2-01 tables, as
# 2-02 does for parijānāti:
#   pajahati           = dứt bỏ          nappajahati   = không dứt bỏ          no ca … nappajahati   = vẫn dứt bỏ
#   pajahittha         = đã dứt bỏ       nappajahittha = chưa từng dứt bỏ      no ca … nappajahittha = đã từng dứt bỏ
#   pajahissati / -nti = sẽ dứt bỏ       nappajahissati = sẽ không dứt bỏ      no ca … nappajahissati = vẫn sẽ dứt bỏ
PAJAH_BASE = "dứt bỏ"
PAJAH_V = r"(?:nap)?pajah(?:atīti|ati|anti|itthāti|ittha|issatīti|issati|issanti)"
PAJAH_VFORM = re.compile(r"(?P<neg>nap)?pajah(?P<t>atīti|ati|anti|itthāti|ittha|issatīti|issati|issanti)")
PAJAH_TENSE = {"ati": "pres", "atīti": "pres", "anti": "pres", "ittha": "past", "itthāti": "past",
               "issati": "fut", "issatīti": "fut", "issanti": "fut"}
V_ALL = rf"(?:{E.E_V}|{PAJAH_V})"


def vparse(s):
    """parijānāti / pajahati form (any tense, number, polarity) -> (base, tense, neg) triple."""
    mm = PAJAH_VFORM.fullmatch(s)
    if mm:
        return (PAJAH_BASE, PAJAH_TENSE[mm["t"]], bool(mm["neg"]))
    return E.e_vparse(s)


E3_Q_RE = re.compile(rf"\((?P<l>Ka|Kha)\) yo(?P<vp> vā pana)? (?P<x>\S+) (?P<v1>{V_ALL}) so (?P<y>\S+) "
                     rf"(?P<v2>{V_ALL})\?")
E3_BUT_RE = re.compile(rf"(?P<s>.+?) (?P<x>\S+) (?P<v1>{V_ALL}), no ca (?P<te>te )?(?P<y>\S+) (?P<v2>{V_ALL})\.")
E3_BOTH_RE = re.compile(rf"(?P<s>.+?) (?P<x>\S+ñca) (?P<v1>{V_ALL}) (?P<y>\S+ñca) (?P<v2>{V_ALL})\.")
YO_PE_RE = re.compile(r"\((?P<l>Ka|Kha)\) yo vā pana…pe…\?")


def yo_pe_question(mm):
    """(Kha) yo vā pana…pe…? = (b) Còn người nào…?  (8 / 5-01 «(b) Còn ở người nào…?» with the yo / so subject)"""
    return f"{LABEL_VI[mm['l']]} {cap(E.E_VA_PANA + E.E_REL)}{PE}?"


def translate_e3(s):
    mm = E3_Q_RE.fullmatch(s)
    if mm:
        vp = bool(mm["vp"])
        if vp != (mm["l"] == "Kha"):
            SLIPS.append(f"label ({mm['l']}) on a {'vā pana' if vp else 'non-vā pana'} question: {s[:50]}")
        return E.e_q(T.m(mm["x"]), vparse(mm["v1"]), T.m(mm["y"]), vparse(mm["v2"]), label=mm["l"], vapana=vp)
    mm = YO_PE_RE.fullmatch(s)
    if mm:
        return yo_pe_question(mm)
    mm = E3_BUT_RE.fullmatch(s)
    if mm:
        dem = E.E_TE + " " if mm["te"] else ""     # no ca te = nhưng những người ấy (7-04 «no ca te tato»)
        clause = E.E_BUT_C.format(pa=E.e_pred(T.m(mm["x"]), vparse(mm["v1"])), dem=dem,
                                  no=E.e_deny(T.m(mm["y"]), vparse(mm["v2"])))
        return E._e_statement(mm["s"], clause)
    mm = E3_BOTH_RE.fullmatch(s)
    if mm:
        return E.e_both(mm["s"], T.m(mm["x"]), vparse(mm["v1"]), T.m(mm["y"]), vparse(mm["v2"]))
    return None


# ================================================================ editorial note and closing lines
ATITANAGATA_Q = "các câu hỏi về quá khứ và tương lai"     # atītānāgatā pucchā (5-02 ATITA_Q / PAC_ATITA_Q; SECTION)
YATHA_VIBHATTA_3 = "(Như {q} {var}, {ap}, đã được phân tích trong {v}, trong {w} cũng nên phân tích như vậy {asm})."
ASAMMOHA_ADV = "mà không mê lầm"                          # asammohantena (5-02 ASAMMOHA «nên phân tích mà không mê lầm»)
assert P.ASAMMOHA.endswith(ASAMMOHA_ADV)
EXACT_LINE = {
    "(Yathā nirodhavāre atītānāgatā [atītenānāgatā (syā.)] pucchā anulomampi paccanīkampi vibhattā evaṃ "
    "uppādanirodhavārepi asammohantena vibhajitabbaṃ).":
        YATHA_VIBHATTA_3.format(q=ATITANAGATA_Q, var=T.variant("[atītenānāgatā (syā.)]"), ap=P.ANU_PACC,
                                v=P.VARA["nirodhavāre"], w=P.VARA["uppādanirodhavāre"], asm=ASAMMOHA_ADV),
}
EXACT = {
    "Uppādanirodhavāro.": E.EXACT["Uppādanirodhavāro."],            # Mục về sự sinh khởi và sự chấm dứt. (2-02)
    "Pavattivāro niṭṭhito.": E.EXACT["Pavattivāro niṭṭhito."],      # Mục về sự diễn tiến đã hoàn tất. (2-02)
    "Saccayamakaṃ niṭṭhitaṃ.": S.yamaka_end("Saccayamakaṃ"),        # Phần các cặp câu hỏi về các sự thật đã hoàn tất.
    **E.PARINNA_EXACT,                                              # Pariññāvāro. = Mục về sự hiểu biết trọn vẹn.
}

# ================================================================ sentences
MEM = r"(?:dukkha|samudaya|nirodha|magga)saccaṃ"
PE_MID_X_RE = re.compile(rf"(?P<g1>.+?) tesaṃ tattha (?P<x>{MEM})…pe… (?P<g2>.+?) tesaṃ tattha (?P<y>{MEM})…pe…\.")
STATIC_NOTES = [
    "^6-5-157 (first answer): two heads cut by «…pe…»: «… tesaṃ tattha dukkhasaccaṃ…pe… itaresaṃ … tesaṃ tattha "
    "dukkhasaccaṃ…pe….» rendered with «…» after the member at both points (5-02 ^6-5-148 shape)",
    "^6-5-162: variant brackets «[apāyā asaññasattā (syā.)]» / «[apāyaṃ asaññasattaṃ (syā.)]» stand between the "
    "plane word and the participle; in Vietnamese they follow the whole group",
    "^6-5-169 vs ^6-5-170: «no ca samudayasaccaṃ nappajahissanti» / «no ca te samudayasaccaṃ nappajahissanti»; "
    "each rendered as written («nhưng vẫn sẽ …» / «nhưng những người ấy vẫn sẽ …»)",
    "^6-5-155 / ^6-5-158 / ^6-5-160 / ^6-5-163: «yassa cittassa anantarā aggamaggaṃ paṭilabhissanti ye caññe …» "
    "without «tassa cittassa …kkhaṇe» (^6-5-154 has it); translated as written",
]


def translate_sentence(s, ctx=""):
    if s in EXACT:
        return EXACT[s]
    r = translate_e3(s)
    if r:
        return r
    mm = PE_MID_X_RE.fullmatch(s)                # two heads, each cut after «tesaṃ tattha X»
    if mm:
        res = F.RES_VI["tesaṃ tattha"]
        a = cap(P.RES_HEAD.format(head=T.head_vi(mm["g1"]), res=res))
        b = P.RES_HEAD.format(head=low(T.head_vi(mm["g2"])), res=res)
        return f"{a} {T.m(mm['x'])}{PE} {b} {T.m(mm['y'])}{PE}"
    return P.translate_sentence(s, ctx)


def translate_line(line, ctx):
    mm = re.match(r"^(?P<h>#+ )?(?P<t>.*?)(?P<id> \^[0-9A-Za-z-]+)?$", line)
    h, t, sid = mm["h"] or "", mm["t"], mm["id"] or ""
    if h:
        return h + P.heading(t) + sid
    if t in EXACT_LINE:
        return EXACT_LINE[t] + sid
    return " ".join(translate_sentence(s, ctx) for s in F.split_sentences(t)) + sid


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
    ("dứt bỏ", 1), ("thành quả", 1), ("tối thượng", 2), ("mê lầm", 1), ("hiểu biết trọn vẹn", 2),
    ("quá khứ và tương lai", 1), ("dị bản", 2),
]   # new (no pi-1..5 string): «thành quả tối thượng» (aggaphala; parallel to «con đường tối thượng»)


def check_cross_book():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in S.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts (5-03): {len(CROSS_BOOK)} strings found in pi-1..5 rails")


def check_frames():
    """The imported frames still say what this chapter relies on (frame-setters / finished chapters)."""
    P.check_frames()
    o = "sự thật về sự phát sinh"
    yv = A7.YO_VERB
    assert E.e_pred(o, vparse("pajahati")) == yv["pajahati"]["p"].format(t=o)            # 7-01 dứt bỏ X
    assert E.e_deny(o, vparse("pajahati")) == yv["pajahati"]["no"].format(t=o)           # không dứt bỏ X
    assert E.e_pred(o, vparse("nappajahati")) == yv["nappajahati"]["p"].format(t=o)
    assert E.e_deny(o, vparse("nappajahati")) == yv["nappajahati"]["no"].format(t=o)     # vẫn dứt bỏ X
    assert vparse("parijānāti") == E.e_vparse("parijānāti")
    assert E.e_pred(o, vparse("nappajahittha")) == E.e_pred(o, ("dứt bỏ", "past", True))
    assert translate_e3("(Ka) yo dukkhasaccaṃ parijānāti so samudayasaccaṃ pajahatīti?") == \
        "(a) Người nào hiểu biết trọn vẹn sự thật về khổ đau, thì có phải người ấy dứt bỏ sự thật về sự phát sinh không?"
    assert yo_pe_question(YO_PE_RE.fullmatch("(Kha) yo vā pana…pe…?")) == \
        P.pe_question_dot(P.PE_Q_DOT_RE.fullmatch("(Kha) yassa vā pana…pe….")).replace("ở người nào", "người nào") + "?"
    assert E.e_subject("Arahā ye ca puthujjanā maggaṃ na paṭilabhissanti te")[1] == E.E_TE
    assert T.head_vi("Arūpe aggamaggassa ca phalassa ca uppādakkhaṇe").endswith("con đường tối thượng và thành quả")
    assert EXACT["Saccayamakaṃ niṭṭhitaṃ."] == "Phần các cặp câu hỏi về các sự thật đã hoàn tất."


def _sentences(text):
    for p in text.splitlines():
        if not p.strip() or p.startswith("#"):
            continue
        p = re.sub(r"\s*\^[\w-]+$", "", p)
        if p in EXACT_LINE:
            continue
        yield from F.split_sentences(p)


def check_repeats(pali):
    """Identical Pāli sentence -> identical Vietnamese, within 5-03 and against 5-01 / 5-02."""
    seen, bad = {}, 0
    for s in _sentences(pali):
        t = translate_sentence(s)
        if seen.setdefault(s, t) != t:
            bad += 1
    shared = 0
    for mod in (T, P):
        prev = (S.PALI_DIR / mod.NAME).read_text(encoding="utf-8")
        for s in set(mod._sentences(prev)) & set(seen):
            shared += 1
            if mod.translate_sentence(s) != seen[s]:
                print(f"DIFFERS FROM {mod.NAME}:", s)
                bad += 1
    print(f"repeat check: {len(seen)} distinct sentences, {shared} shared with 5-01 / 5-02")
    return bad


def main():
    S.check_cross_book()
    F.check_cross_book()
    T.check_cross_book()
    P.check_cross_book()
    check_cross_book()
    check_frames()
    SLIPS.clear(); P.SLIPS.clear(); T.SLIPS.clear(); F.SLIPS.clear(); E.SLIPS.clear()
    text = unicodedata.normalize("NFC", translate_file())
    pali = (S.PALI_DIR / NAME).read_text(encoding="utf-8")
    probs = S.check_lines(pali, text, NAME)
    for bad in ("….", ".…", "?…", ",…", "  ", "là là", "—", ":-", " ,", " ."):
        assert bad not in text, bad
    assert check_repeats(pali) == 0, "identical Pāli rendered differently"
    with open(S.OUT_DIR / NAME, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    segs = len(re.findall(r"\^[0-9A-Za-z-]+\s*$", text, flags=re.M))
    print(f"wrote {NAME}: {len([x for x in text.splitlines() if x.strip()])} lines, {segs} segments")
    for w in STATIC_NOTES + sorted(set(SLIPS + P.SLIPS + T.SLIPS + E.SLIPS)) + [f"{c} | {w}" for c, w in F.SLIPS]:
        print("NOTE", w)
    for p in probs[:80]:
        print("PROBLEM", p)
    print("line checks:", "OK" if not probs else f"{len(probs)} problems")
    sys.exit(1 if probs else 0)


if __name__ == "__main__":
    main()
