"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 5-03 (Saccayamaka, part 3: the end of the uppādanirodhavāra
(paccuppannānāgata, atītānāgata) and the pariññāvāra).

Pavattivāra lines: build_rails_5-02_vi (and through it 5-01, 2-01, 7-01, 8, 2-02, 9-01, 9-02, 3-01), unchanged.
This file loads a PRIVATE second instance of build_rails_5-02_vi (`Q`, its own module object, its own private
5-01 instance `Q.TP`); the shared modules (P2 = build_rails_5-02_vi, T = build_rails_5-01_vi) and their dicts stay
untouched. The private head parser gets ONE extra genitive owner before a moment: aggaphalassa «thành quả tối
thượng» (termbase), in the same slot as 5-01's maggassa / phalassa / aggamaggassa. The private 5-02's cut_answer
gets one extra cut shape: an answer cut by …pe… right after the member («…, thì ở những người ấy, ở nơi ấy
<member>…»). The builder asserts that its translator reproduces the 5-01 and 5-02 chapters byte for byte.

Pariññāvāra lines: family E from build_rails_2-02_vi (setter), unchanged: E.e_question / E.e_sentence with the
four truths as objects, parijānāti (E.E_VERBS) and pajahati (E.make_verbs + E.rows_fused, the same tense rule),
E.PERSONS. One addition: "…, no ca te B V" (the Pāli's own pronoun after no ca) = «…, nhưng những người ấy …»
(E.TE; as 7-07's «nhưng người ấy …» for "no ca so").

Exposed: `Q`, `PAJ_VERBS`, `E_VERBS_5`, `M_E`, `e_sentence5`, `e_line5`, `yo_cut`, `NOTES`, `VARIANTS`,
`line_vi`, `tr_line`, `build`. A line the parsers cannot place raises ValueError (no silent fallback).

usage: python -I -X utf8 -B build_rails_5-03_vi.py [--probe]
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
P2 = importlib.import_module("build_rails_5-02_vi")   # READ-ONLY (shared): Saccayamaka 2
T = importlib.import_module("build_rails_5-01_vi")    # READ-ONLY (shared): Saccayamaka module
E = importlib.import_module("build_rails_2-02_vi")    # READ-ONLY (shared): family E setter
B, C, D = T.B, T.C, T.D                                 # 2-01, 7-01, 8 (READ-ONLY, the same objects)


def _private_5_02():
    """A second, private instance of build_rails_5-02_vi (own module object, own private 5-01 instance)."""
    spec = importlib.util.spec_from_file_location("build_rails_5_02_private_for_5_03",
                                                  RAILS_DIR / "build_rails_5-02_vi.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


Q = _private_5_02()
assert Q.TP is not P2.TP and Q.TP is not T

CH = "5-03-saccayamaka.md"
N = "5-03"
NOTES_MD = RAILS_DIR / f"notes-rails-{N}.md"
ADH_DIR = RAILS_DIR / f"adh-{N}"
cap = S.cap
LABEL = S.LABEL
PE = S.PE
SLIPS = []   # (what, where)

# ===============================================================================================================
# 1. Pavattivāra additions (private instances only)
# ===============================================================================================================
AGGAPHALA = "thành quả tối thượng"                       # aggaphalassa (termbase «thành quả tối thượng»)
Q.TP.OWNER = {**Q.TP.OWNER, "aggaphalassa": AGGAPHALA}   # the private 5-01 instance only (its lambdas read OWNER)
_OWNER_RE = re.compile(r"(taṇhāya|maggassa|phalassa|aggamaggassa|aggaphalassa) " + Q.TP.MOMENT_W)
_old = Q.TP.T_PATTERNS[3]
assert _old[0].pattern == r"(taṇhāya|maggassa|phalassa|aggamaggassa) " + Q.TP.MOMENT_W
Q.TP.T_PATTERNS = Q.TP.T_PATTERNS[:3] + [(_OWNER_RE, _old[1])] + Q.TP.T_PATTERNS[4:]
assert "aggaphalassa" not in T.OWNER and "aggaphalassa" not in P2.TP.OWNER

_cut_answer_5_02 = Q.cut_answer


def cut_answer(core):
    """5-02's cut_answer, plus: '<head> <res> A' (cut right after the member) → «<Head>, thì <res> A»
    (the first half of 2-01's b_noca without the verb)."""
    w = core.split()
    if len(w) > 2 and Q._member_at(w) == len(w) - 1:
        i = len(w) - 1
        if " ".join(w[i - 2:i]) == "tesaṃ tattha":
            loc, h = "tesaṃ tattha", i - 2
        elif w[i - 1] == "tesaṃ":
            loc, h = "tesaṃ", i - 1
        else:
            raise ValueError(f"no resumptive before the cut member: {core!r}")
        out = f"{Q.TP.head_vi(w[:h])}, {C.THEN} {B.L[loc]} {Q.M.subj(w[i])}"
        SLIPS.append(("answer cut by …pe… right after the member (cut at the same spot)", core[:70]))
        return Q._decap(out) if core[:1].islower() else out
    return _cut_answer_5_02(core)


Q.cut_answer = cut_answer                                  # the private 5-02 instance only
assert P2.cut_answer is not cut_answer

# editorial note (5-02's strings: VIBHATTA, VIBHAJITABBA, ANU_PACC, ASAMMOHANTENA; 2-01 TIME, mục về …)
ATITANAGATA_PUCCHA = f"Các câu hỏi về {B.TIME['Atītānāgata']}"   # atītānāgatā pucchā (= 5-02 PACC_ATITA_PUCCHA shape)
assert Q.PACC_ATITA_PUCCHA == f"Các câu hỏi về {B.TIME['Paccuppannātīta']}"
NOTES = {
    "(Yathā nirodhavāre atītānāgatā ⟦0⟧ pucchā anulomampi paccanīkampi vibhattā evaṃ uppādanirodhavārepi "
    "asammohantena vibhajitabbaṃ).":
        f"({ATITANAGATA_PUCCHA} ⟦0⟧, {Q.ANU_PACC}, {Q.VIBHATTA} {B.NIRODHAVARO}, ở {B.UPPADANIRODHAVARO} "
        f"{Q.VIBHAJITABBA} {Q.ASAMMOHANTENA}).",
}
VARIANTS = dict(Q.VARIANTS) | {
    "[atītenānāgatā (syā.)]": B.parse_variant("[atītenānāgatā (syā.)]", "form"),
    "[apāyā asaññasattā (syā.)]": B.parse_variant("[apāyā asaññasattā (syā.)]", "form"),
    "[apāyaṃ asaññasattaṃ (syā.)]": B.parse_variant("[apāyaṃ asaññasattaṃ (syā.)]", "form"),
}
FIXED = {
    "Uppādanirodhavāro.": E.UPPADANIRODHAVARO_CLOSE,       # «Mục về sự sinh khởi và sự chấm dứt.» (2-02)
    "Pariññāvāro.": E.PARINNAVARO_CLOSE,                   # «Mục về sự hiểu biết trọn vẹn.» (2-02)
    "Saccayamakaṃ niṭṭhitaṃ.": S.yamaka_end(T.YAMAKA),     # = 4 «Dhātuyamakaṃ niṭṭhitaṃ.», 8 «Cittayamakaṃ …»
}

# ===============================================================================================================
# 2. Family E in the Saccayamaka (2-02's functions; objects = the four truths, verbs parijānāti + pajahati)
# ===============================================================================================================
M_E = Q.M                                                  # 5-01 SACCA_B (dukkhasaccaṃ / -ñca …)
PAJAHATI = "dứt bỏ"                                        # pajahati (termbase; = 7-05 / 7-07 PAJ)
PAJ_VERBS = E.make_verbs(PAJAHATI, E.rows_fused(
    ("pajahati", "pajahanti", "pajahittha", "pajahissati", "pajahissanti"),
    ("nappajahati", "nappajahanti", "nappajahittha", "nappajahissati", "nappajahissanti")))
E_VERBS_5 = {**E.E_VERBS, **PAJ_VERBS}
NOCA_TE = ", no ca te "


def e_sentence5(s):
    """E.e_sentence; "…, no ca te B V." (pronoun after no ca) = «…, nhưng những người ấy <no-ca part>.»."""
    if NOCA_TE in s:
        if s.count(NOCA_TE) != 1:
            raise ValueError(f"two 'no ca te' in {s!r}")
        r = E.e_sentence(s.replace(NOCA_TE, ", no ca "), M_E, E_VERBS_5)
        if r is None or r.count(f", {E.BUT} ") != 1:
            raise ValueError(f"'no ca te' sentence not placed: {s!r}")
        return r.replace(f", {E.BUT} ", f", {E.BUT} {E.TE} ")
    return E.e_sentence(s, M_E, E_VERBS_5)


YO_CUT_RE = re.compile(r"\((Kha)\) yo vā pana…pe…\?(?: (.+))?")


def yo_cut(body):
    """'(Kha) yo vā pana…pe…? Āmantā.' → «(b) Còn người nào mà… không? Đúng vậy.» (E.yo_q's opening; coordinator:
    a question cut by …pe… ending in '?' = «… không?»)."""
    m = YO_CUT_RE.fullmatch(body)
    if not m:
        return None
    s = f"{LABEL[m.group(1)]} {cap(E.OTHER)} {E.WHO} mà{PE} không?"
    assert E.yo_q("X", "Y", "Kha", True).startswith(f"{LABEL['Kha']} {cap(E.OTHER)} {E.WHO} mà X, ")
    return s + (" " + e_answers5(m.group(2)) if m.group(2) else "")


def e_answers5(text):
    out = []
    for x in [x for x in re.split(r"(?<=\.) ", text.strip()) if x]:
        if x in C.EXACT:
            out.append(C.EXACT[x])
        elif (r := e_sentence5(x)) is not None:
            out.append(r)
        else:
            raise ValueError(f"unknown family-E answer {x!r}")
    return " ".join(out)


def _has_e_verb(p):
    return any(E.is_e_verb(w, E_VERBS_5) for w in p.replace(",", "").split())


def e_line5(body):
    """A pariññāvāra line body: a question (+ answers), a cut question, or a run of answers; None if not family E."""
    if (c := yo_cut(body)) is not None:
        return c
    if (q := E.e_question(body, M_E, E_VERBS_5)) is not None:
        if NOCA_TE in body:
            raise ValueError(f"'no ca te' on a question line: {body!r}")
        return q
    parts = [x for x in re.split(r"(?<=\.) ", body.strip()) if x]
    if parts and all(p in C.EXACT or _has_e_verb(p) for p in parts) and any(p not in C.EXACT for p in parts):
        return e_answers5(body)
    return None


# ===============================================================================================================
# 3. Line translator
# ===============================================================================================================
def heading(text):
    if text in E.HEADINGS:                                 # Pariññāvāro, Paccuppannavāro, … (2-02)
        return E.HEADINGS[text]
    return Q.TP.heading(text)


def line_vi(body):
    if body in NOTES:
        return NOTES[body]
    if body in FIXED:
        return FIXED[body]
    if (r := e_line5(body)) is not None:
        return r
    return Q.line_vi(body)


def tr_line(p):
    m = re.search(r" (\^\S+)$", p)
    bid = m.group(1) if m else None
    body = p[:m.start()] if m else p
    if body.startswith("#"):
        hashes, text = body.split(" ", 1)
        out = f"{hashes} {heading(text)}"
    else:
        for bad, good in Q.VERB_SLIPS.items():             # 5-02's slip rule (none in 5-03; kept for 5-02)
            if bad in body:
                SLIPS.append((f"«{bad.strip()}» (termbase variant spelling of «{good.strip()}»)", bid or body[:40]))
                body = body.replace(bad, good)
        brs = Q.TP.VAR_RE.findall(body)
        for k, br in enumerate(brs):
            body = body.replace(br, f"⟦{k}⟧", 1)
        out = line_vi(body)
        for k, br in enumerate(brs):
            if br not in VARIANTS:
                raise ValueError(f"undeclared variant {br!r}")
            if out.count(f"⟦{k}⟧") != 1:
                raise ValueError(f"variant {br!r} lost in {p!r}")
            out = out.replace(f"⟦{k}⟧", VARIANTS[br])
        if "⟦" in out or Q.TP.KC_TOKEN in out:
            raise ValueError(f"unplaced token in {p!r}")
    return f"{out} {bid}" if bid else out


def build(name=CH):
    segs = []
    for seg in S.segments_of(name):
        out = []
        for ln in seg:
            try:
                out.append(tr_line(ln))
            except (ValueError, KeyError) as e:
                raise ValueError(f"{name}: cannot place line {ln[:160]!r}: {e!r}") from None
        segs.append(out)
    return segs


def probe(name=CH):
    bad = 0
    for seg in S.segments_of(name):
        for ln in seg:
            try:
                v = tr_line(ln)
                if "--show" in sys.argv:
                    print("PI:", ln, "\nVI:", v, "\n")
            except (ValueError, KeyError, AssertionError) as e:
                bad += 1
                print("FAIL:", repr(e)[:400], "\n   ", ln[:220])
    print("failing lines:", bad)


# ===============================================================================================================
# 4. Assertions
# ===============================================================================================================
TERMBASE_USED = [
    ("aggaphalassa", AGGAPHALA), ("pajahati", PAJAHATI), ("pajahatīti", PAJAHATI), ("nappajahatīti", "không dứt bỏ"),
    ("pajahitthāti", "đã dứt bỏ"), ("nappajahitthāti", "chưa từng dứt bỏ"), ("pajahittha", "đã dứt bỏ"),
    ("nappajahittha", "chưa từng dứt bỏ"), ("pajahissatīti", "sẽ dứt bỏ"), ("nappajahissatīti", "sẽ không dứt bỏ"),
    ("pajahissati", "sẽ dứt bỏ"), ("nappajahissati", "sẽ không dứt bỏ"), ("nappajahissanti", "sẽ không dứt bỏ"),
    ("parijānāti", E.PARIJANATI), ("parijānittha", "đã " + E.PARIJANATI), ("parijānissati", "sẽ " + E.PARIJANATI),
    ("parijānanti", E.PARIJANATI), ("Saccayamakaṃ", "các cặp câu hỏi về các sự thật"),
    ("asaññasattā", "cõi Vô Tưởng"), ("Apāye", "cõi khổ"), ("atītānāgatepi", B.TIME["Atītānāgata"]),
]


def _rebuild(name):
    return "\n\n".join("\n".join(tr_line(x) for x in seg) for seg in S.segments_of(name)) + "\n"


def check_assertions():
    tb = T.TERMBASE.read_text(encoding="utf-8")
    bad = [(p, v) for p, v in TERMBASE_USED
           if not re.search(r"^" + re.escape(p) + r": \{[^\n]*: " + re.escape(v) + r"[};]", tb, re.M | re.I)]
    assert not bad, "termbase strings not found: " + repr(bad)
    # family E: the pajahati table follows the termbase rows and the denied forms of the coordinator
    for f, v in (("nappajahati", "không dứt bỏ"), ("nappajahittha", "chưa từng dứt bỏ"),
                 ("nappajahissati", "sẽ không dứt bỏ"), ("pajahittha", "đã dứt bỏ"), ("pajahissanti", "sẽ dứt bỏ")):
        assert PAJ_VERBS[f].vi == v, (f, PAJ_VERBS[f].vi)
    assert E.denied(PAJ_VERBS["nappajahittha"]) == "đã từng dứt bỏ"
    assert E.denied(PAJ_VERBS["nappajahissanti"]) == "vẫn sẽ dứt bỏ"
    assert E.denied(E.E_VERBS["na parijānāti"]) == "vẫn hiểu biết trọn vẹn"      # user / coordinator
    assert E.denied(E.E_VERBS["na parijānittha"]) == "đã từng hiểu biết trọn vẹn"
    # 7-07's parameterised verb agrees (pajahati / parijānāti)
    V7 = importlib.import_module("build_rails_7-07_vi")
    assert V7.PAJ.pos == PAJAHATI and V7.PAJ.still == "vẫn dứt bỏ" and V7.PARIJ.pos == E.PARIJANATI
    # the 5-01 and 5-02 chapters re-translate identically with this file's translator
    for ch in (T.CH, P2.CH):
        vi = (S.OUT_DIR / ch).read_text(encoding="utf-8")
        assert unicodedata.normalize("NFC", _rebuild(ch)) == vi, f"{ch} not reproduced"
    del SLIPS[:]
    del Q.SLIPS[:]
    del Q.TP.SLIPS_SEEN[:]
    # the new owner slot: «vào khoảnh khắc sinh khởi của thành quả tối thượng»
    assert Q.TP.head_vi("arūpe aggaphalassa uppādakkhaṇe".split()) == \
        f"{cap(C.AT)} {Q.TP.PLANES['arūp'][0]}, {Q.TP.moment('uppādakkhaṇe', AGGAPHALA)}"
    # parsers still raise on unknown words / shapes
    for bad_s in ("Brahmānaṃ tesaṃ dukkhasaccaṃ", "Arūpe tattha dukkhasaccaṃ"):
        try:
            cut_answer(bad_s)
        except ValueError:
            continue
        raise AssertionError(f"no error on {bad_s!r}")
    for bad_s in ("Anāgāmī dukkhasaccaṃ na parijānāti, no ca te samudayasaccaṃ nappajahittha.",
                  "Arahā dukkhasaccaṃ na parijānanti."):
        try:
            e_sentence5(bad_s)
        except ValueError:
            continue
        raise AssertionError(f"no error on {bad_s!r}")


# ===============================================================================================================
# 5. Notes file (Pāli = tiếng Việt)
# ===============================================================================================================
def notes(slips):
    out = [f"# pi-6 rails {N} (Saccayamaka 3): end of the uppādanirodhavāra; pariññāvāra", "",
           "Builder: build_rails_5-03_vi.py. Imports build_rails_5-02_vi (a private second instance `Q`, with its own "
           "private 5-01 instance), build_rails_5-01_vi and build_rails_2-02_vi READ-ONLY (and through them 2-01, "
           "7-01, 8, 9-01, 9-02, 3-01; 7-07 for an agreement check). The private head parser adds one genitive owner "
           "(aggaphalassa); the private cut_answer adds one cut shape. The builder asserts that its translator "
           "reproduces the 5-01 and 5-02 chapters byte for byte. Format: Pāli = tiếng Việt.", ""]

    def h(t):
        out.extend(["", f"## {t}", ""])

    def row(p, v):
        out.append(f"{p} = {v}")

    h("New strings set here")
    row("aggaphalassa uppādakkhaṇe (head item)", Q.TP.head_vi("aggaphalassa uppādakkhaṇe".split()))
    row("arūpe aggaphalassa uppādakkhaṇe", Q.TP.head_vi("arūpe aggaphalassa uppādakkhaṇe".split()))
    row("<head> tesaṃ tattha A…pe… (cut right after the member)",
        cut_answer("Asaññasattaṃ upapajjantānaṃ tesaṃ tattha dukkhasaccaṃ") + PE)
    for p, v in NOTES.items():
        row(p, v)
    for p, v in VARIANTS.items():
        if p not in Q.VARIANTS:
            row(p, v)
    for p, v in FIXED.items():
        row(p, v)
    h("Family E in the Saccayamaka (2-02 frames; objects = the four truths)")
    for f, v in PAJ_VERBS.items():
        row(f, v.vi)
    row("after no ca: nappajahati / nappajahittha / nappajahissati (denied)",
        " / ".join(E.denied(PAJ_VERBS[f]) for f in ("nappajahati", "nappajahittha", "nappajahissati")))
    row("after no ca: na parijānāti / na parijānittha / na parijānissati (denied)",
        " / ".join(E.denied(E.E_VERBS[f]) for f in ("na parijānāti", "na parijānittha", "na parijānissati")))
    row("…, no ca te B V. (pronoun after no ca)", f"…, {E.BUT} {E.TE} …")
    row("(Kha) yo vā pana…pe…? Āmantā.", yo_cut("(Kha) yo vā pana…pe…? Āmantā."))
    for s in ("(Ka) yo dukkhasaccaṃ parijānāti so samudayasaccaṃ pajahatīti? Āmantā.",
              "(Kha) yo vā pana samudayasaccaṃ nappajahittha so dukkhasaccaṃ na parijānātīti?",
              "Arahā dukkhasaccaṃ na parijānāti, no ca samudayasaccaṃ nappajahittha.",
              "Aggamaggasamaṅgī samudayasaccaṃ nappajahittha, no ca dukkhasaccaṃ na parijānāti.",
              "Ye maggaṃ paṭilabhissanti te dukkhasaccaṃ na parijānittha, no ca te samudayasaccaṃ nappajahissanti.",
              "Arahā ye ca puthujjanā maggaṃ na paṭilabhissanti te dukkhasaccañca na parijānanti samudayasaccañca "
              "nappajahissanti."):
        row(s, line_vi(s))
    h("Termbase misfits and gaps (for the coordinator)")
    out += [
        "- nappajahanti, pajahanti: termbase rows exist; not met here (in the table for later chapters).",
        "- atītānāgatā pucchā «các câu hỏi về quá khứ và tương lai» (5-02 «các câu hỏi về …» shape; 2-01 TIME); "
        "vibhattā / vibhajitabbaṃ = 5-02 / pi-2 «như đã được phân tích trong …, … cũng nên phân tích như vậy»; "
        "asammohantena «mà không mê lầm» (3-01) after «phân tích như vậy».",
        "- «no ca te …» (^6-5-170, the Pāli's own te after no ca; 2-02 has none): «, nhưng những người ấy vẫn sẽ dứt "
        "bỏ …» (E.TE; = 7-07's «nhưng người ấy …» for so).",
        "",
        "## Pāli as written (reported)",
        "",
        "- ^6-5-157 first (Ka) answer: «… tesaṃ tattha dukkhasaccaṃ…pe… itaresaṃ … tesaṃ tattha dukkhasaccaṃ…pe….»: "
        "both halves cut right after the member; the Vietnamese is cut at the same spots.",
        "- ^6-5-165 … ^6-5-167: «(Kha) yo vā pana…pe…? Āmantā.» = «(b) Còn người nào mà… không? Đúng vậy.».",
        "- ^6-5-164: «(Yathā …)» note: the variant [atītenānāgatā (syā.)] follows «Các câu hỏi về quá khứ và tương "
        "lai» (5-02's placement for [paccuppannenātītā (syā.)]).",
        "- ^6-5-162: variants [apāyā asaññasattā (syā.)] / [apāyaṃ asaññasattaṃ (syā.)] inside the heads go after the "
        "person group they follow (5-01's placement rule).",
        "- ^6-5-168 / ^6-5-169: «Arahā … na parijānāti, no ca …» etc. kept as written; ^6-5-169 «Ye maggaṃ "
        "paṭilabhissanti te dukkhasaccaṃ na parijānanti, no ca samudayasaccaṃ …» (no te) and ^6-5-170 «…, no ca te "
        "…» (with te) differ in the Pāli and stay different in the Vietnamese.",
        "- Termbase adherence (adh-5-03): 292 keyword occurrences, 0 misses.",
    ]
    out += [f"- {p}: {v}" for p, v in slips]
    return out


def main():
    if "--probe" in sys.argv:
        probe()
        return
    S.check_reused()
    B.check_reused()
    check_assertions()
    segs = build(CH)
    C.write(CH, segs, extra_dirs=(ADH_DIR,))
    slips = sorted(set(SLIPS) | set(Q.SLIPS) | set(Q.TP.SLIPS_SEEN))
    lines = notes(slips) + [""]
    NOTES_MD.write_text(unicodedata.normalize("NFC", "\n".join(lines)), encoding="utf-8", newline="\n")
    print("wrote", NOTES_MD)
    for p, v in slips:
        print("slip:", p, "|", v)


if __name__ == "__main__":
    main()
