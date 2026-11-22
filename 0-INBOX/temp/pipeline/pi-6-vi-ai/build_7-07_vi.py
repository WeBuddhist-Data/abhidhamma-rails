# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 7-07-anusayayamaka.md (Pariññāvāro: parijānāti, anuloma + paṭiloma).

Family C frames come VERBATIM from the frame-setter build_7-01_vi: tendencies tl(), the yo / so, yato / tato,
yo yato / so tato question frame (question_yo, YO_Q_FRAME, YO_REL_VI, YO_DEM_VI), YO_VERB["parijānāti"] =
«hiểu biết trọn vẹn {t}» / «không hiểu biết trọn vẹn {t}», YO_VERB["na parijānāti"] = «không hiểu biết trọn vẹn {t}» /
«vẫn hiểu biết trọn vẹn {t}», TADEKATTHA «những gì cùng hiện diện với nó», places PLACE_VI, headings, mūlaka
labels, «Pariññāvāre anulomaṃ.». The answer demonstratives and answer frames come from build_7-04_vi (RES_VI,
BUT_C, BOTH_C, STATEMENT_*) and the subject-less answer from build_7-03_vi (STATEMENT_BARE). The frames shared with
the parallel pajahana chapters come from build_7-05_vi (TADEK_ATTR «X vốn cùng hiện diện với nó», TADEK_C
«{pa}, {pb}») and build_7-06_vi (the path persons Aṭṭhamako, Aggamaggasamaṅgī, Anāgāmimaggasamaṅgī, the
«… ṭhapetvā avasesā puggalā» subjects, DEM_VI with «no ca so»), asserted against the values used here.
New here (notes-7-07.md): the parijānāti answer shapes and the mixed-polarity question of ^6-7-243 (as written).

DASH RULE: no dash in this chapter, the frames add none. No quotes.
Importing writes nothing; run  python -I -X utf8 -B build_7-07_vi.py  to rebuild the chapter file.
"""
import importlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as B  # noqa: E402

A = importlib.import_module("build_7-01_vi")
N3 = importlib.import_module("build_7-03_vi")
N4 = importlib.import_module("build_7-04_vi")

CH = "7-07-anusayayamaka.md"
cap, low = B.cap, B.low
SLIPS = []

# ================================================================ verbs (7-01 YO_VERB verbatim)
POS = A.YO_VERB["parijānāti"]            # p = «hiểu biết trọn vẹn {t}», no = «không hiểu biết trọn vẹn {t}»
NEG = A.YO_VERB["na parijānāti"]         # p = «không hiểu biết trọn vẹn {t}», no = «vẫn hiểu biết trọn vẹn {t}»
VERB_KEY = {"parijānāti": "parijānāti", "parijānanti": "parijānāti",          # plural = same Vietnamese
            "na parijānāti": "na parijānāti", "na parijānanti": "na parijānāti"}
VERB_WORDS = {"parijānāti", "parijānanti"}

# ================================================================ tadekaṭṭhaṃ (7-01 TADEKATTHA; 7-05 TADEK_ATTR / TADEK_C)
# The parallel chapters 7-05 (pajahati) / 7-06 (nappajahati) ran at the same time; identical frames are taken from
# their builders (identical Pāli = identical Vietnamese) and asserted against the values this chapter was built with.
N5 = importlib.import_module("build_7-05_vi")
N6 = importlib.import_module("build_7-06_vi")
TADEKATTHA = A.TADEKATTHA                                   # Tadekaṭṭhaṃ parijānāti. -> «những gì cùng hiện diện với nó»
TADEKATTHA_ADJ = N5.TADEK_ATTR                              # X tadekaṭṭhaṃ parijānāti -> «X vốn cùng hiện diện với nó»
assert TADEKATTHA_ADJ == "{t} vốn cùng hiện diện với nó", TADEKATTHA_ADJ
# pi-1 «tadekaṭṭhā ca kilesā» = «các phiền não cùng hiện diện với chúng»; aṭṭhakathā «pahānekaṭṭhataṃ sandhāya»

# ================================================================ persons as subjects (nominative; = 7-05 / 7-06)
PERSON_EXPECTED = {
    "Sveva puggalo": "Chính hạng người ấy",                 # 7-04
    "Aṭṭhamako": "Người thứ tám",                           # pi-5 aṭṭhamaka puggala «người thứ tám»
    "Aggamaggasamaṅgī": "Người có được con đường tối thượng",   # pi-5 maggasamaṅgī «người có được con đường»; 7-05 agga
    "Anāgāmimaggasamaṅgī": "Người có được con đường không trở lại",   # pi-5 anāgāmimagga «con đường không trở lại»
    "Dvinnaṃ maggasamaṅgīnaṃ ṭhapetvā avasesā puggalā":
        "Ngoại trừ hai người có được con đường, những hạng người còn lại",   # pi-1 ṭhapetvā «Ngoại trừ», avasesā «còn lại»
    "Anāgāmimaggasamaṅgiñca aṭṭhamakañca ṭhapetvā avasesā puggalā":
        "Ngoại trừ người có được con đường không trở lại và người thứ tám, những hạng người còn lại",
    "Aggamaggasamaṅgiñca aṭṭhamakañca ṭhapetvā avasesā puggalā":
        "Ngoại trừ người có được con đường tối thượng và người thứ tám, những hạng người còn lại",
    "Dvinnaṃ maggasamaṅgīnañca aṭṭhamakañca ṭhapetvā avasesā puggalā":
        "Ngoại trừ hai người có được con đường và người thứ tám, những hạng người còn lại",
}
PERSON_NOM_VI = {k: N6.PERSON_NOM_VI[k] for k in PERSON_EXPECTED}     # 7-06 verbatim
assert PERSON_NOM_VI == PERSON_EXPECTED, "7-06 person subjects changed"
assert N5.PERSON_NOM_VI["Aggamaggasamaṅgī"] == PERSON_EXPECTED["Aggamaggasamaṅgī"]
PERSONS = sorted(PERSON_NOM_VI, key=len, reverse=True)

# ================================================================ places (7-01 PLACE_VI verbatim)
PLACE_VI = dict(A.PLACE_VI)
PLACES = sorted(PLACE_VI, key=len, reverse=True)

# ================================================================ demonstratives and answer frames (7-04 / 7-03 verbatim)
RES_VI = dict(N4.RES_VI)                                    # tato / so tato / te tato
DEM_VI = dict(RES_VI, so=A.YO_DEM_VI["so"])                 # NEW: «no ca so …» = «nhưng người ấy …» (7-01 YO_DEM_VI)
BUT_C = N4.BUT_C                                            # «{pa}, nhưng {dem}{no}»
BOTH_C = N4.BOTH_C                                          # «{pa}, đồng thời cũng {pb}»
SEQ_C = N5.TADEK_C                                          # «{pa}, {pb}»: A parijānāti(,) B tadekaṭṭhaṃ parijānāti (no «ca»)
assert SEQ_C == "{pa}, {pb}" and DEM_VI == N6.DEM_VI
STATEMENT_RES = N4.STATEMENT_RES                            # «{head}, thì {res} {clause}.»
STATEMENT_PLACE = N4.STATEMENT_PLACE                        # «{head}, {clause}.»
STATEMENT_PERSON = N4.STATEMENT_PERSON                      # «{head} {clause}.»
STATEMENT_BARE = N3.STATEMENT_BARE                          # «{clause}.» (Mānānusayaṃ parijānāti.)


def lower1(s):
    return s[:1].lower() + s[1:]


def split_ca(phrase):
    """«mānānusayañca» -> «mānānusayaṃ ca» (accusative sandhi), so that 7-01 tl() reads the list."""
    return re.sub(r"ñca(?=\s|$)", "ṃ ca", phrase)


def obj_vi(words):
    """Object of parijānāti: a tendency list, optionally followed by «tadekaṭṭhaṃ», or «tadekaṭṭhaṃ» alone."""
    td = bool(words) and words[-1] == "tadekaṭṭhaṃ"
    if td:
        words = words[:-1]
    if not words:
        assert td
        return TADEKATTHA
    t = A.tl(split_ca(" ".join(words)))
    return TADEKATTHA_ADJ.format(t=t) if td else t


def vgroups(text):
    """Split «A [na] parijānāti[,] B [na] parijānāti» into (object words, verb key, comma after)."""
    out, cur = [], []
    for w in text.split():
        bare = w.rstrip(",")
        if bare in VERB_WORDS:
            neg = bool(cur) and cur[-1] == "na"
            if neg:
                cur = cur[:-1]
            out.append((cur, VERB_KEY[("na " if neg else "") + bare], w.endswith(",")))
            cur = []
        else:
            cur.append(w)
    assert not cur, f"words after the last verb: {text!r}"
    return out


def is_ca(words):
    return bool(words) and split_ca(words[-1 if words[-1] != "tadekaṭṭhaṃ" else -2]).endswith(" ca")


def pred(group, form="p"):
    words, key, _ = group
    return A.YO_VERB[key][form].format(t=obj_vi(words))


def clause_of(body, s):
    left, sep, right = body.partition(", no ca ")
    gs = vgroups(left)
    assert 1 <= len(gs) <= 2, s
    if len(gs) == 1:
        lv = pred(gs[0])
    elif gs[1][0] and gs[1][0][-1] == "tadekaṭṭhaṃ":
        assert "tadekaṭṭhaṃ" not in gs[0][0], s
        lv = SEQ_C.format(pa=pred(gs[0]), pb=pred(gs[1]))            # A [ca] V(,) B [ca] tadekaṭṭhaṃ V (= 7-05)
    else:
        assert is_ca(gs[0][0]) and is_ca(gs[1][0]) and not gs[0][2], s
        lv = BOTH_C.format(pa=pred(gs[0]), pb=pred(gs[1]))           # A ca V B ca V
    if not sep:
        return lv
    dem = next((d for d in ("so tato", "te tato", "tato", "so") if right.startswith(d + " ")), None)
    if dem:
        right = right[len(dem) + 1:]
    rg = vgroups(right)
    assert len(rg) == 1, s
    return BUT_C.format(pa=lv, dem=DEM_VI[dem] + " " if dem else "", no=pred(rg[0], "no"))


def parse_statement(s):
    assert s.endswith(".") and not s.endswith(".."), s
    t = s[:-1]
    per = next((k for k in PERSONS if t.startswith(k + " ")), None)
    if per:
        t = t[len(per) + 1:]
    places = []
    while True:
        hit = next((p for p in PLACES if lower1(t).startswith(p + " ")), None)
        if not hit:
            break
        places.append(hit)
        t = t[len(hit) + 1:]
    res = next((r for r in ("so tato", "te tato", "tato") if t.startswith(r + " ")), None)
    if res:
        t = t[len(res) + 1:]
    if not per and not places and not res:
        t = lower1(t)                                           # «Mānānusayaṃ parijānāti.», «Tadekaṭṭhaṃ parijānāti.»
    clause = clause_of(t, s)
    head = ", ".join(([PERSON_NOM_VI[per]] if per else []) + [PLACE_VI[p] for p in places])
    if res:
        assert head, s
        return cap(STATEMENT_RES.format(head=head, res=RES_VI[res], clause=clause))
    if places:
        return cap(STATEMENT_PLACE.format(head=head, clause=clause))
    if per:
        return cap(STATEMENT_PERSON.format(head=head, clause=clause))
    return cap(STATEMENT_BARE.format(clause=clause))


# ================================================================ questions (7-01 question_yo / YO_Q_FRAME verbatim)
Q_RE = re.compile(r"(?:\((?P<l>Ka|Kha)\) )?(?P<y1>[Yy]o|[Yy]ato)(?P<vp> vā pana)?(?P<y2> yato)? "
                  r"(?P<a>.+?) (?P<va>na parijānāti|parijānāti) (?P<d>so tato|so|tato) "
                  r"(?P<b>.+?) ?(?P<vb>na parijānātīti|parijānātīti)\?")


def question(m, s):
    rel = "yo yato" if m["y2"] else m["y1"].lower()
    exp = {"yo": "so", "yato": "tato", "yo yato": "so tato"}[rel]
    assert m["d"] == exp, s
    va, vb = m["va"], m["vb"][:-3] + "i"                      # parijānātīti -> parijānāti
    a, b = split_ca(m["a"]), split_ca(m["b"])
    if va == vb:
        return A.question_yo(rel, m["d"], a, b, va, m["l"], bool(m["vp"]))
    # ^6-7-243 «yato paṭighānusayaṃ na parijānāti tato mānānusayaṃ parijānātīti?»: mixed polarity, as written
    SLIPS.append("mixed polarity question (translated as written): " + s[:90])
    q = A.YO_Q_FRAME.format(rel=A.YO_REL_VI[rel], pa=A.YO_VERB[va]["p"].format(t=A.tl(a)),
                            dem=A.YO_DEM_VI[m["d"]], pb=A.YO_VERB[vb]["p"].format(t=A.tl(b)))
    if m["vp"]:
        q = A.VA_PANA + low(q)
    return f"{B.LABEL[m['l']]} {cap(q)}" if m["l"] else cap(q)


# ================================================================ «…pe….» endings (= 7-03 / 7-04)
PE_END_RE = re.compile(r"(?P<s>.*?) ?…pe…\.")
PE = A.PE


def translate_sentence(s):
    m = PE_END_RE.fullmatch(s)
    if m:
        out = translate_sentence(m["s"] + ".")
        assert out.endswith("."), out
        return out[:-1] + PE                                    # «….» is never written
    m = Q_RE.fullmatch(s)
    if m:
        return question(m, s)
    if "parijān" in s:
        return parse_statement(s)
    return A.translate_sentence(s)          # Āmantā., No., Natthi., (…mūlakaṃ), Pariññāvāre anulomaṃ.


def translate_line(line):
    m = re.match(r"^(?P<h>#+ )?(?P<t>.*?)(?P<id> \^[0-9A-Za-z-]+)?$", line)
    h, t, sid = m["h"] or "", m["t"], m["id"] or ""
    if h:
        return h + A.heading(t) + sid
    return " ".join(translate_sentence(s) for s in A.SPLIT_RE.split(t)) + sid


def translate_file(name):
    src = (B.PALI_DIR / name).read_text(encoding="utf-8")
    out = [translate_line(line) if line.strip() else "" for line in src.splitlines()]
    text = "\n".join(out).rstrip("\n") + "\n"
    return re.sub(r"\n{3,}", "\n\n", text)


# ================================================================ checks
CROSS_BOOK = [
    ("người thứ tám", 5), ("người có được con đường", 5), ("con đường không trở lại", 5), ("Ngoại trừ", 1),
    ("còn lại", 1), ("cùng hiện diện với chúng", 1), ("hiểu biết trọn vẹn", 2), ("hạng người", 4),
    ("không nằm trong các cõi tồn tại", 1), ("nơi cảm giác khó chịu", 5), ("trong cõi hình sắc", 2),
    ("trong cõi không hình sắc", 2), ("trong cõi dục lạc", 2), ("Đúng vậy.", 5), ("Không có.", 3),
    ("tối thượng", 5),
]


def check_cross_book():
    A.check_cross_book()
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in B.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts (7-07): {len(CROSS_BOOK)} strings found in pi-1..5 rails")


def check_repeats(pali):
    """Identical Pāli sentence -> identical Vietnamese sentence (within the chapter)."""
    seen, bad = {}, 0
    for p in pali.splitlines():
        if not p.strip() or p.startswith("#"):
            continue
        p = re.sub(r"\s*\^[\w-]+$", "", p)
        for s in A.SPLIT_RE.split(p):
            t = translate_sentence(s)
            if seen.setdefault(s, t) != t:
                bad += 1
    return bad


def main():
    check_cross_book()
    SLIPS.clear()
    A.SLIPS.clear()
    text = unicodedata.normalize("NFC", translate_file(CH))
    pali = (B.PALI_DIR / CH).read_text(encoding="utf-8")
    probs = B.check_lines(pali, text, CH)
    assert check_repeats(pali) == 0, "identical Pāli rendered differently"
    for bad in ("….", ".…", "?…", "  ", "là là", "parijān", "puggal", "tadekaṭṭh", "maggasam"):
        assert bad not in text, bad
    with open(B.OUT_DIR / CH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    segs = len(re.findall(r"\^[0-9A-Za-z-]+\s*$", text, flags=re.M))
    print(f"wrote {CH}: {len([ln for ln in text.splitlines() if ln.strip()])} lines, {segs} segments")
    print("source notes:")
    for s in sorted(set(SLIPS + A.SLIPS)):
        print("  ", s)
    for p in probs[:80]:
        print("PROBLEM", p)
    print("line checks:", "OK" if not probs else f"{len(probs)} problems")
    sys.exit(1 if probs else 0)


if __name__ == "__main__":
    main()
