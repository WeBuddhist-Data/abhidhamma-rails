# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 10-09-indriyayamaka.md (Indriyayamaka, pavattivāra, uppādavāra
(5) paccuppannānāgatavāra: (Ka) anulomapuggalo, (Kha) anulomaokāso, (Ga) anulomapuggalokāsā).

Frames, imported and used VERBATIM:
  build_10-08_vi  (H8): translate_sentence() for every question (yassa / yattha / yassa yattha, «…pe…» runs, the
                  «?…Pe….» line), the mūlaka notes, Āmantā (through build_10-04_vi / build_10-02_vi); head8() for every
                  present-tense person / time head (attribute beings, planes, «Sabbesaṃ cavantānaṃ …», moments,
                  pavatte, nirodhasamāpannānaṃ, asaññasattānaṃ); split10, heading;
  build_10-04_vi  (R): P4_NOT / P4_BOTH (person-and-place answers);
  build_10-02_vi  (P): fm(), ATTR10, PARTICIPLE10, P_NOT / P_BOTH;
  build_10-05_vi  (Y5): YE_FRAME, ye_bhava(), ye_attr(), last_citta(), YE_NOUN, SAHA, UPA_ATTR (the future «ye …»
                  clauses: «eteneva bhāvena katici bhave dassetvā», «ye sacakkhukā upekkhāya upapajjitvā …»);
  build_3-03_vi   (A33): YE_CA_UPAPAJJANTA («ye ca <P>ṃ upapajjitvā parinibbāyissanti tesaṃ upapajjantānaṃ» = «và những
                  người đang tái sinh mà sau khi tái sinh vào <P> sẽ nhập Niết-bàn trọn vẹn»), who33 (checked);
  build_6-01_vi   (X6): ANANTARA «… mà ngay sau đó {c} sẽ sinh khởi»;
  build_8_vi      (C8): AT / OF / MOMENT, citta(last=True), P_SUBJ («Pacchimacittassa uppādakkhaṇe», checked);
  build_2-01_vi   (F) / build_2-02_vi (E): b_not / b_both, who(), WHO_HEAD, LIST_SEP, HEAD, PARTICIPLE, YE_CA_JOIN;
  build_3-01_vi   (A3): ATTR_GROUP / ATTR_JOIN;  labels from build_sample_vi.LABEL.
New here (notes-10-09.md): the «tesaṃ upapajjantānaṃ / tāsaṃ upapajjantīnaṃ» resumptive over several «ye ca» clauses
(the 3-03 rule extended to the 10-05 clauses), «Pacchimabhavikānaṃ <attr> upapajjantānaṃ» as one group,
«Itarāsaṃ», «yassa cittassa anantarā … pacchimacittaṃ uppajjissati tassa cittassa uppādakkhaṇe», «(Sadisaṃ )».

Importing writes nothing; run  python -I -X utf8 -B build_10-09_vi.py  to rebuild the chapter.
"""
import importlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as S  # noqa: E402

H8 = importlib.import_module("build_10-08_vi")    # present heads (head8), sentences (questions, places, notes)
R = H8.R                                          # build_10-04_vi
P = H8.P                                          # build_10-02_vi
F = H8.F                                          # build_2-01_vi
I = H8.I                                          # build_10-01_vi
A3 = H8.A3                                        # build_3-01_vi
C8 = H8.C8                                        # build_8_vi
E = importlib.import_module("build_2-02_vi")      # «ye ca …» join
Y5 = importlib.import_module("build_10-05_vi")    # future «ye …» clauses
A33 = importlib.import_module("build_3-03_vi")    # «ye ca … parinibbāyissanti tesaṃ upapajjantānaṃ»
X6 = importlib.import_module("build_6-01_vi")     # ANANTARA

NAME = "10-09-indriyayamaka.md"
cap, low = S.cap, S.low
LABEL = S.LABEL
SLIPS = []
OI = F.WHO_HEAD.format(g="")                      # «ở »
assert OI == H8.OI

# ================================================================ the future «ye …» clauses (10-05 / 2-01 / 3-03)
NAO = " nào sau khi "                             # inside Y5.YE_FRAME «những {n} nào sau khi {what} sẽ …»
assert NAO in Y5.YE_FRAME
UPA = F.PARTICIPLE["upapajjantānaṃ"][0]           # «đang tái sinh» (2-01)
NAO_UPA = f" {UPA} mà sau khi "                   # «… tesaṃ upapajjantānaṃ» (3-03 YE_CA_UPAPAJJANTA)
assert Y5.YE_FRAME.replace(NAO, NAO_UPA).format(n="người", what="tái sinh vào {p}") == A33.YE_CA_UPAPAJJANTA
AWITH = r"(?:upekkhāya|somanassena)"
ACCP = r"(?:rūpāvacaraṃ|arūpāvacaraṃ|arūpaṃ|kāmāvacaraṃ)"


def _planes(s):
    out = []
    for w in s.split():
        case, stem = F._plane_case(w)
        assert case == "acc", s
        out.append(F.PLANE[stem])
    return F.LIST_SEP.join(out)                   # 2-01 LIST_SEP (3-02 / 3-03)


def _ye_noun(n):
    return Y5.YE_NOUN[n] if n else "người"


def _clause(mm):
    """One «ye ca / yā ca …» clause -> Vietnamese «những … nào sau khi … sẽ nhập Niết-bàn trọn vẹn»."""
    g = mm.groupdict()
    if g.get("n") is not None:
        assert mm["rel"].startswith("yā") == (g["n"] == "itthiyo"), mm[0]
    if g.get("bh"):                                                       # eteneva bhāvena … (10-05)
        return Y5.ye_bhava(g["n"], g.get("a"))
    if g.get("h"):                                                        # ye sacakkhukā upekkhāya … (10-05)
        return Y5.ye_attr(g["h"], g["a"])
    if g.get("pl"):                                                       # ye ca <planes> upapajjitvā … (2-01 / 3-03)
        out = Y5.YE_FRAME.format(n=_ye_noun(g.get("n")), what="tái sinh vào " + _planes(g["pl"]))
        if not g.get("n"):
            assert out == F.YE_UPAPAJJITVA.format(p=_planes(g["pl"]))
        return out
    # ye ca purisā / yā ca itthiyo upekkhāya upapajjitvā … (new: 10-05 UPA_ATTR with the noun of ye_bhava)
    return Y5.YE_FRAME.format(n=_ye_noun(g["n"]), what=Y5.UPA_ATTR.format(a=Y5.SAHA[g["a"]]))


REL = r"(?P<rel>ye ca|yā ca)"
CLAUSES = [re.compile(p + r"(?= |$)") for p in (
    rf"{REL} (?P<n>purisā|itthiyo) (?P<bh>eteneva bhāvena katici bhave dassetvā) (?:(?P<a>{AWITH}) upapajjitvā )?"
    r"parinibbāyissanti",
    rf"{REL} (?P<h>sacakkhukā|saghānakā) (?P<a>{AWITH}) upapajjitvā parinibbāyissanti",
    rf"{REL} (?:(?P<n>purisā|itthiyo) )?(?P<pl>(?:{ACCP} )*{ACCP}) upapajjitvā parinibbāyissanti",
    rf"{REL} (?P<n>purisā|itthiyo) (?P<a>{AWITH}) upapajjitvā parinibbāyissanti",
)]
TAIL_RE = re.compile(r"(?P<r>tesaṃ|tāsaṃ) (?P<p>upapajjantānaṃ|upapajjantīnaṃ)$")


def ye_run(s, ctx=""):
    """«ye ca …[ ye ca …] [tesaṃ upapajjantānaṃ]» -> list of Vietnamese clauses. With the resumptive participle
    every clause reads «những … đang tái sinh mà sau khi …» (3-03 YE_CA_UPAPAJJANTA, applied to each clause)."""
    out, i = [], 0
    while i < len(s):
        tm = TAIL_RE.match(s, i)
        if tm and tm.end() == len(s):
            assert out, s
            if (tm["r"] == "tāsaṃ") != (tm["p"] == "upapajjantīnaṃ"):
                raise ValueError(s)
            out = [c.replace(NAO, NAO_UPA, 1) for c in out]
            assert all(NAO_UPA in c for c in out), out
            return out
        for rx in CLAUSES:
            mm = rx.match(s, i)
            if mm:
                out.append(_clause(mm))
                i = mm.end() + 1
                break
        else:
            raise ValueError(f"unparsed ye clause {s!r} at {s[i:]!r}")
    return out


# ================================================================ time phrases at the head's start
def _last(kind):
    """'' -> «tâm cuối cùng» (8); 'upekkhāsampayutta' -> «tâm cuối cùng gắn liền với sự bình thản» (10-05)."""
    return C8.citta(last=True) if not kind else Y5.last_citta(kind)


def _at(mo, c):
    return C8.AT.format(x=C8.OF.format(x=C8.MOMENT[mo], c=c))      # vào khoảnh khắc sinh khởi của <c> (8)


ANANTARA_REL = X6.ANANTARA[len("vào "):]                          # «tâm mà ngay sau đó {c} sẽ sinh khởi» (6-01)
assert X6.ANANTARA == "vào " + ANANTARA_REL and ANANTARA_REL.startswith(C8.citta() + " mà ")
TIMES = [
    (re.compile(r"(?P<k>\S*?)pacchimacittassa (?P<mo>uppāda|bhaṅga)kkhaṇe(?= |$)"),
     lambda m: _at(m["mo"], _last(m["k"]))),
    # yassa cittassa anantarā K-pacchimacittaṃ uppajjissati tassa cittassa uppādakkhaṇe (new): «vào khoảnh khắc sinh
    # khởi của tâm mà ngay sau đó <K> sẽ sinh khởi» (the 6-01 relative clause under the 8 moment)
    (re.compile(r"yassa cittassa anantarā (?P<k>\S*?)pacchimacittaṃ uppajjissati tassa cittassa "
                r"(?P<mo>uppāda|bhaṅga)kkhaṇe(?= |$)"),
     lambda m: _at(m["mo"], ANANTARA_REL.format(c=_last(m["k"])))),
]


# ================================================================ person heads
def _persons(s, ctx=""):
    """Present-tense person words -> «Ở …» (head8), with two additions: «Pacchimabhavikānaṃ <attr> upapajjantānaṃ»
    is one group (as «Pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ», 2-01 who), and «Itarāsaṃ» (feminine) =
    «Itaresaṃ» (10-02 PARTICIPLE10: the feminine has the same Vietnamese)."""
    w = s.split()
    if w and w[0] == "itarāsaṃ":
        w[0] = "itaresaṃ"
    if w and w[0] == "pacchimabhavikānaṃ" and len(w) >= 3 and w[1] in P.ATTR10 and w[-1] in P.PARTICIPLE10:
        h = F.who("pacchimabhavikānaṃ")[len(OI):]                     # «những người thuộc kiếp sống cuối cùng»
        tail = P.attr_group(w[1:])                                      # «những người đang tái sinh là người nam»
        head = F.HEAD[None] + " "
        assert tail.startswith(head), tail
        return cap(OI + h + " " + tail[len(head):])
    return H8.head8(" ".join(w), ctx)


def head9(g, ctx=""):
    """Pāli answer head (before tesaṃ / tāsaṃ [tattha]) -> Vietnamese head, capitalised.
    Time phrases stand alone; the persons take one «ở» (head8); «ye ca …» clauses join the persons with « và »
    (2-02 / 3-03); all joined «, » (2-01 LIST_SEP)."""
    s, pieces = low(g), []
    while True:
        for rx, fn in TIMES:
            mm = rx.match(s)
            if mm:
                pieces.append(fn(mm))
                s = s[mm.end():].lstrip()
                break
        else:
            break
    if s:
        mm = re.search(r"(?:^| )(?=(?:ye|yā) ca )", s)
        left, right = (s[:mm.start()], s[mm.end():]) if mm else (s, "")
        assert left, g
        per = low(_persons(left, ctx))
        if right:
            per += "".join(E.YE_CA_JOIN + c for c in ye_run(right, ctx))
        pieces.append(per)
    return cap(F.LIST_SEP.join(pieces))


# ================================================================ sentences
EXACT = {"(Sadisaṃ )": "(Giống nhau)"}           # sadisaṃ = «giống nhau» (3-02 «… sadisaṃ» = «… giống nhau»)
SLIP_FIX = [   # (Pāli as written, as read, report)
    ("somanassindriyaṃ uppajjissati, tassa purisindriyaṃ", "somanassindriyaṃ uppajjissati tassa purisindriyaṃ",
     "^6-10-369: comma inside the question «… uppajjissati, tassa …»; the Vietnamese question frame has its comma anyway"),
    ("tesaṃ tattha manindriyaṃ uppajjissati cakkhundriyañca uppajjati.",
     "tesaṃ tattha manindriyañca uppajjissati cakkhundriyañca uppajjati.",
     "^6-10-376: «manindriyaṃ uppajjissati cakkhundriyañca uppajjati»: first «ca» missing; rendered with the "
     "both-frame (as 3-03 ^6-3-100)"),
]
SLIP_USED = {}


def translate_sentence(s, ctx=""):
    s = s.strip()
    if s in EXACT:
        SLIPS.append((ctx, "«(Sadisaṃ )»: space before «)»; written without it"))
        return EXACT[s]
    if s.endswith(".") and (" tesaṃ " in s or " tāsaṃ " in s):
        body = s[:-1]
        for rx, both, res in ((R.P4_NOT, False, "tesaṃ tattha"), (R.P4_BOTH, True, "tesaṃ tattha"),
                              (P.P_NOT, False, "tesaṃ"), (P.P_BOTH, True, "tesaṃ")):
            mm = rx.fullmatch(body)
            if not mm:
                continue
            if not both:
                assert mm["r"] == mm["r2"], s
            if mm["r"] == "tāsaṃ":
                assert "upapajjantīnaṃ" in mm["g"], s
            f = F.b_both if both else F.b_not
            return f(res, head9(mm["g"], ctx), P.fm(mm["x"]), F.vparse(mm["v1"], ctx), P.fm(mm["y"]),
                     F.vparse(mm["v2"], ctx))
        raise ValueError(f"unmatched person answer: {s!r} ({ctx})")
    return H8.translate_sentence(s, ctx)          # questions, «?…Pe….», mūlaka notes (10-08 / 10-04 / 10-02)


def translate_line(line, ctx=""):
    mm = re.match(r"^(?P<h>#+ )?(?P<t>.*?)(?P<id> \^[0-9A-Za-z-]+)?$", line)
    h, t, sid = mm["h"] or "", mm["t"], mm["id"] or ""
    if h:
        return h + P.heading(t) + sid
    for a, b, why in SLIP_FIX:
        if a in t:
            SLIP_USED[why] = SLIP_USED.get(why, 0) + 1
            t = t.replace(a, b)
    return " ".join(translate_sentence(x, ctx) for x in P.split10(t) if x.strip()) + sid


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
    ("người nam", 2), ("người nữ", 2), ("có mắt", 4), ("sau khi tái sinh", 4), ("nhập Niết-bàn trọn vẹn", 5),
    ("gắn liền với sự bình thản", 1), ("gắn liền với niềm vui", 2), ("chúng sinh Vô Tưởng", 5),
    ("cõi dục lạc", 1), ("cõi hình sắc", 1), ("cõi không hình sắc", 5), ("khoảnh khắc tan rã", 5),
    ("thành tựu thiền chấm dứt", 5), ("ngay sau", 5), ("một số", 2), ("đời sống", 1),
]


def check_cross_book():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in S.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts (10-09): {len(CROSS_BOOK)} strings found in pi-1..5 rails")


def check_frames():
    """Frames shared with the frame-setters stay byte-identical."""
    g = "Pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti tesaṃ upapajjantānaṃ"
    assert head9(g) == cap(A33.who33(g)), (head9(g), A33.who33(g))                          # 3-03
    g = ("Pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ ye ca rūpāvacaraṃ arūpāvacaraṃ upapajjitvā "
         "parinibbāyissanti tesaṃ upapajjantānaṃ")
    assert head9(g) == cap(A33.who33(g)), (head9(g), A33.who33(g))                          # 3-03
    assert head9("Pacchimacittassa uppādakkhaṇe") == cap(C8.P_SUBJ["Pacchimacittassa uppādakkhaṇe"])   # 8 / 6-02
    assert _last("upekkhāsampayutta") == "tâm cuối cùng gắn liền với sự bình thản"                  # 10-05 / 10-06
    for g in ("Pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ", "Sabbesaṃ cavantānaṃ acakkhukānaṃ upapajjantānaṃ",
              "Itaresaṃ purisānaṃ upapajjantānaṃ", "Itthīnaṃ upapajjantīnaṃ"):
        assert head9(g) == H8.head8(g), g                                                    # 10-08
    assert head9("Itarāsaṃ itthīnaṃ upapajjantīnaṃ") == H8.head8("Itaresaṃ itthīnaṃ upapajjantīnaṃ")
    assert head9("Pacchimabhavikānaṃ purisānaṃ upapajjantānaṃ") == \
        "Ở những người thuộc kiếp sống cuối cùng đang tái sinh là người nam"
    assert P.ATTR10["purisānaṃ"] == "là người nam" and F.PACCHIMA == "thuộc kiếp sống cuối cùng"
    assert E.YE_CA_JOIN == " và " and S.LABEL["Ka"] == "(a)" and S.LABEL["Kha"] == "(b)" and S.LABEL["Ga"] == "(c)"


HEAD_DIFF_OK = {
    # head8 would make two groups («những người thuộc kiếp sống cuối cùng, những người đang tái sinh là người nam»);
    # the Pāli is one group, as «Pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ» (2-01 who): one group here
    "head8:pacchimabhavikānaṃ+attr",
}


def check_parallel(pali):
    """Every sentence the 10-08 / 10-04 / 10-02 / 10-05 / 10-06 / 10-07 parsers translate, and every head that
    head8 / who33 / head5 / head6 / head7 translate, comes out byte-identical here."""
    mods = [("10-08", H8), ("10-04", R), ("10-02", P), ("10-05", Y5)]
    heads = [("head8", H8.head8), ("who33", lambda x: cap(A33.who33(x))), ("head5", Y5.head5)]
    for nm, fn in (("build_10-06_vi", "head6"), ("build_10-07_vi", "head7")):
        try:
            m = importlib.import_module(nm)
            mods.append((nm[6:11], m))
            heads.append((fn, getattr(m, fn)))
        except Exception as e:                                         # noqa: BLE001 (parallel agents)
            print(f"note: {nm} not importable:", e)
    probs, n = [], {}
    for ln in pali.splitlines():
        if not ln.strip() or ln.startswith("#"):
            continue
        t = re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", ln)
        for a, b, _ in SLIP_FIX:
            t = t.replace(a, b)
        for s in P.split10(t):
            s = s.strip()
            if not s or s in EXACT:
                continue
            mine = translate_sentence(s, "check")
            w0 = low(s).split()
            one_group = w0[0] == "pacchimabhavikānaṃ" and w0[1] in P.ATTR10                   # HEAD_DIFF_OK
            for tag, mod in mods:
                try:
                    theirs = mod.translate_sentence(s, "check")
                except (AssertionError, ValueError, KeyError, TypeError, IndexError, AttributeError):
                    continue
                n[tag] = n.get(tag, 0) + 1
                if one_group and tag == "10-08":
                    assert theirs.split(", thì ", 1)[1] == mine.split(", thì ", 1)[1], s          # same clause
                    continue
                if theirs != mine:
                    probs.append(f"differs from {tag}: {s[:70]} | {theirs} | {mine}")
            mm = (R.P4_NOT.fullmatch(s[:-1]) or R.P4_BOTH.fullmatch(s[:-1]) or P.P_NOT.fullmatch(s[:-1])
                  or P.P_BOTH.fullmatch(s[:-1])) if s.endswith(".") else None
            if not mm:
                continue
            g, h = mm["g"], head9(mm["g"], "check")
            w = low(g).split()
            for tag, fn in heads:
                try:
                    o = cap(fn(g))
                except (AssertionError, ValueError, KeyError, TypeError, IndexError, AttributeError):
                    continue
                n[tag] = n.get(tag, 0) + 1
                if tag == "head8" and w[0] == "pacchimabhavikānaṃ" and len(w) > 1 and w[1] in P.ATTR10:
                    n["head8 one-group"] = n.get("head8 one-group", 0) + 1       # HEAD_DIFF_OK
                    continue
                if o != h:
                    probs.append(f"head differs from {tag}: {g} | {o} | {h}")
    for _, mod in mods:
        if hasattr(mod, "SLIPS"):
            del mod.SLIPS[:]
    for mod in (P, R, F, H8):
        del mod.SLIPS[:]
    del SLIPS[:]
    print("parallel checks:", ", ".join(f"{k} {v}" for k, v in n.items()))
    return probs


def check_same_as_other(text, pali):
    """Every Pāli line of this chapter that also occurs in a written Indriya chapter has the same Vietnamese."""
    strip = lambda x: re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", x)          # noqa: E731
    probs = []
    for k in range(1, 14):
        nm = f"10-{k:02d}-indriyayamaka.md"
        vp = S.OUT_DIR / nm
        if nm == NAME or not vp.exists():
            continue
        p1 = (S.PALI_DIR / nm).read_text(encoding="utf-8").splitlines()
        v1 = vp.read_text(encoding="utf-8").splitlines()
        if len(p1) != len(v1):
            print(f"note: {nm} line count differs from its Pāli; not compared")
            continue
        ref = {strip(p): strip(v) for p, v in zip(p1, v1) if p.strip() and not p.startswith("#")}
        c = 0
        for p, v in zip(pali.splitlines(), text.splitlines()):
            if p.strip() and strip(p) in ref:
                c += 1
                if ref[strip(p)] != strip(v):
                    probs.append(f"differs from {nm}: {p[:70]}")
        print(f"lines shared with {nm} checked: {c}")
    return probs


def main():
    S.check_cross_book()
    F.check_cross_book()
    I.check_cross_book()
    P.check_cross_book()
    check_cross_book()
    check_frames()
    pali = (S.PALI_DIR / NAME).read_text(encoding="utf-8")
    pprobs = check_parallel(pali)
    SLIP_USED.clear()
    text = unicodedata.normalize("NFC", translate_file())
    probs = (S.check_lines(pali, text, NAME) + I.check_extra(text, pali) + check_same_as_other(text, pali)
             + pprobs)
    for a, b, why in SLIP_FIX:
        if SLIP_USED.get(why) != 1:
            probs.append(f"slip fix used {SLIP_USED.get(why)} times: {why}")
    for i, ln in enumerate(text.splitlines(), 1):
        body = re.sub(r" ?\[[^\]]*\]", "", re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", ln))
        for bad in ("uppajj", "upapajj", "tesaṃ", "tāsaṃ", "tattha", "mūlakaṃ", "kkhaṇe", "thì thì", "bhāv",
                    "là không phải", "ndriya", "ānaṃ", "īnaṃ", "Āmantā", "….", "  ", "là là", "ye ca", "yā ca",
                    "itthiyo", "purisā", "pacchima", "anantarā", "parinibb", "cittassa", "Sadis", "itarā", "ṃ",
                    "sẽ sẽ", "và và", "Pe…"):
            if bad in body:
                probs.append(f"line {i}: «{bad}»")
    with open(S.OUT_DIR / NAME, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    segs = len(re.findall(r"\^[0-9A-Za-z-]+\s*$", text, flags=re.M))
    print(f"wrote {NAME}: {len([x for x in text.splitlines() if x.strip()])} lines, {segs} segments")
    seen = set()
    for why in SLIP_USED:
        print("SLIP", why)
    for c, w in SLIPS + H8.SLIPS + R.SLIPS + P.SLIPS + F.SLIPS:
        if (c, w) not in seen:
            seen.add((c, w))
            print("SLIP", c, "|", w)
    for p in probs[:80]:
        print("PROBLEM", p)
    print("line checks:", "OK" if not probs else f"{len(probs)} problems")
    sys.exit(1 if probs else 0)


if __name__ == "__main__":
    main()
