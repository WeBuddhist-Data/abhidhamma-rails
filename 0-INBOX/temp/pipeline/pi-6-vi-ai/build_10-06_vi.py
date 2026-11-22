# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 10-06-indriyayamaka.md (Indriyayamaka, pavattivāra, uppādavāra (3)
anāgatavāra: (Kha) anulomaokāso … (Ṅa) paccanīkaokāso).

Frames, imported and used VERBATIM:
  build_10-04_vi  (R): translate_sentence() for every question (yassa / yattha / yassa yattha, «…pe…» runs),
                  Āmantā, «Āmantā …pe….», Natthi, the short answers (Uppajjissati. = Sẽ sinh khởi.), the place
                  answers (via 10-02 / 3-01 where3) and the mūlaka notes; translate_line() frame, split10, heading;
  build_10-02_vi  (P): fm(), ATTR10 (upekkhāya / somanassena), citta_kind() pieces, BARE (người nam / người nữ);
  build_2-01_vi   (F): b_not / b_both / STATEMENT_RES, BOTH_C, vparse, who() (planes, beings, pacchimabhavikānaṃ,
                  itaresaṃ …), YE_UPAPAJJITVA, WHO_HEAD, LIST_SEP, RES_VI;
  build_2-02_vi   (E): YE_CA_JOIN «… và …» (asserted against who2);
  build_3-01_vi   (A3): ATTR (sacakkhukā = có mắt …);
  build_3-02_vi   (A32): ATTR_PLANE_GROUP «… vào <plane> mà <attr>»;
  build_6-01_vi   (X6): ANANTARA «Vào tâm mà ngay sau đó <tâm cuối cùng …> sẽ sinh khởi», «cuối cùng» before the kind;
  build_8_vi      (C8): citta(last=True) «tâm cuối cùng», SAMANGI «những người có được …»;
  build_10-05_vi  (Y5): ye_bhava() «những người nam / nữ nào sau khi trải qua một số kiếp sống trong chính trạng thái
                  ấy [và tái sinh có … đi kèm] sẽ nhập Niết-bàn trọn vẹn», ye_attr() «những người nào sau khi tái sinh
                  có mắt và có … đi kèm sẽ …», last_citta() (same Pāli, settled there in the same run; head5 checked);
  labels from build_sample_vi.LABEL.
New here (notes-10-06.md): «ye ca somanassena rūpāvacaraṃ upapajjitvā parinibbāyissanti», pacchimabhavikānaṃ /
pacchimacittasamaṅgīnaṃ in these heads, the stray-period both-answer, and the answer-head rule head6().

Importing writes nothing; run  python -I -X utf8 -B build_10-06_vi.py  to rebuild the chapter.
"""
import importlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as S  # noqa: E402

R = importlib.import_module("build_10-04_vi")    # Indriya pavatti sentences (questions, places, answers)
P = R.P                                           # build_10-02_vi
F = R.F                                           # build_2-01_vi
I = R.I                                           # build_10-01_vi
A3 = R.A3                                         # build_3-01_vi
C8 = R.C8                                         # build_8_vi
E = importlib.import_module("build_2-02_vi")      # «ye ca …» join
A32 = importlib.import_module("build_3-02_vi")    # attribute + plane group
X6 = importlib.import_module("build_6-01_vi")     # yassa cittassa anantarā … pacchimacittaṃ uppajjissati

NAME = "10-06-indriyayamaka.md"
cap, low = S.cap, S.low
LABEL = S.LABEL
SLIPS = []
OI = R.OI                                         # «ở »

# ================================================================ the nominative «ye …» clauses
assert F.YE_UPAPAJJITVA == "những người nào sau khi tái sinh vào {p} sẽ nhập Niết-bàn trọn vẹn"
REBORN = "sau khi tái sinh"                       # upapajjitvā (2-01 YE_UPAPAJJITVA)
PARI = "sẽ nhập Niết-bàn trọn vẹn"                # parinibbāyissanti (2-01 YE_UPAPAJJITVA; pi-5)
assert F.YE_UPAPAJJITVA == f"những người nào {REBORN} vào {{p}} {PARI}"
# The «ye purisā / yā itthiyo eteneva bhāvena katici bhave dassetvā …» and «ye sacakkhukā upekkhāya upapajjitvā …»
# clauses: 10-05 (same Pāli, same run) settled them first; its functions are imported and used verbatim.
Y5 = importlib.import_module("build_10-05_vi")    # ye_bhava(), ye_attr(), last_citta(), YE_FRAME
assert Y5.YE_FRAME.format(n="người", what="tái sinh vào {p}") == F.YE_UPAPAJJITVA
assert A32.ATTR_PLANE_GROUP == "{h} {p} {prep} {planes} mà {a}"
YE_ATTR_PLANE = "những người nào " + REBORN + " vào {p} mà {a} " + PARI        # ye somanassena rūpāvacaraṃ upapajjitvā …
# (new here: 2-01 YE_UPAPAJJITVA + the 3-02 ATTR_PLANE_GROUP order «… vào <plane> mà <attr>»)
AWITH = r"(?:upekkhāya|somanassena)"
ACCP = r"(?:rūpāvacaraṃ|arūpāvacaraṃ|arūpaṃ)"
GENP = r"(?:kāmāvacarānaṃ|rūpāvacarānaṃ|arūpāvacarānaṃ|arūpānaṃ|pañcavokārānaṃ|catuvokārānaṃ|asaññasattānaṃ)"


def _planes(s):
    out = []
    for w in s.split():
        case, stem = F._plane_case(w)
        assert case == "acc", s
        out.append(F.PLANE[stem])
    return F.LIST_SEP.join(out)


def _ye(mm):
    """One «ye / yā (ca) …» clause -> Vietnamese (no «ở»: a nominative relative, 2-01)."""
    g = mm.groupdict()
    if g.get("pl") is not None and g.get("a") is None:
        return F.YE_UPAPAJJITVA.format(p=_planes(g["pl"]))
    if g.get("n"):
        assert (mm["rel"].startswith("yā")) == (g["n"] == "itthiyo"), mm[0]
        return Y5.ye_bhava(g["n"], g.get("a"))                                       # 10-05
    if g.get("h"):
        assert not mm["rel"].endswith(" ca"), mm[0]
        return Y5.ye_attr(g["h"], g["a"])                                            # 10-05
    return YE_ATTR_PLANE.format(p=_planes(g["pl"]), a=P.ATTR10[g["a"]])


def _last_kind(k):
    """upekkhāsampayutta -> «tâm cuối cùng gắn liền với sự bình thản» (6-01 order; = 10-05 last_citta)."""
    kind = P.citta_kind(k)
    assert kind.startswith(P.CITTA + " "), kind
    out = C8.citta(last=True) + kind[len(P.CITTA):]
    assert out == Y5.last_citta(k), (out, Y5.last_citta(k))
    return out


def _strip_o(s):
    assert s.startswith(OI), s
    return s[len(OI):]


REL = r"(?P<rel>ye ca|yā ca|ye|yā)"
ELEMENTS = [
    (r"yassa cittassa anantarā (?P<k>\S+?)pacchimacittaṃ uppajjissati", "T",
     lambda m: X6.ANANTARA.format(c=_last_kind(m["k"]))),
    (rf"{REL} (?P<n>purisā|itthiyo) eteneva bhāvena katici bhave dassetvā (?:(?P<a>{AWITH}) upapajjitvā )?"
     r"parinibbāyissanti", "Y", _ye),
    (rf"{REL} (?P<h>sacakkhukā|saghānakā) (?P<a>{AWITH}) upapajjitvā parinibbāyissanti", "Y", _ye),
    (rf"{REL} (?P<a>{AWITH}) (?P<pl>{ACCP}) upapajjitvā parinibbāyissanti", "Y", _ye),
    (rf"{REL} (?P<pl>(?:{ACCP} )*{ACCP}) upapajjitvā parinibbāyissanti", "Y", _ye),
    (r"pacchimacittasamaṅgīn(?P<s>aṃ|a)", "P",
     lambda m: C8.SAMANGI.format(c=C8.citta(last=True))),                       # 8 / 5-01 / 9-01
    (r"pacchimabhavikānaṃ", "P", lambda m: _strip_o(F.who(m[0]))),            # 2-01
    (rf"(?:itaresaṃ )?(?:{GENP} )*{GENP}", "P", lambda m: _strip_o(F.who(m[0]))),   # 2-01
]
ELEMENTS = [(re.compile(p + r"(?= |$)"), k, f) for p, k, f in ELEMENTS]


def head6(g, ctx=""):
    """Pāli answer head (before tesaṃ / tāsaṃ (tattha)) -> Vietnamese head, capitalised.
    T (time) stands alone; P (genitive persons) take «ở» unless they follow other persons; a «ye …» clause at the
    start has no «ở» (2-01); «ye ca / yā ca …» joins the piece before it with « và » (2-02 who2); pieces «, »."""
    p, i, pieces = low(g), 0, []
    while i < len(p):
        for rx, kind, fn in ELEMENTS:
            mm = rx.match(p, i)
            if not mm:
                continue
            vi = fn(mm)
            if kind == "P" and "pacchimacittasamaṅgīna" in mm[0] and mm["s"] == "a":
                SLIPS.append((ctx, "«Pacchimacittasamaṅgīna» read as «Pacchimacittasamaṅgīnaṃ»"))
            if kind == "Y" and mm["rel"].endswith(" ca"):
                assert pieces, g
                pieces[-1] = (pieces[-1][0], pieces[-1][1] + E.YE_CA_JOIN + vi)
            else:
                assert kind != "Y" or not pieces, g
                if kind == "P":
                    vi = OI + vi
                pieces.append((kind, vi))
            i = mm.end() + 1
            break
        else:
            raise ValueError(f"unparsed head {g!r} at {p[i:]!r}")
    return cap(F.LIST_SEP.join(v for _, v in pieces))


# ================================================================ sentences
V = P.V
FAC_W = P.FAC_W
RES6 = r"(?P<r>tesaṃ|tāsaṃ)(?P<t> tattha)?"
S_NOT = re.compile(rf"(?P<g>.+?) {RES6} (?P<x>{FAC_W}) (?P<v1>{V}), no ca (?P<r2>tesaṃ|tāsaṃ)(?P<t2> tattha)? "
                   rf"(?P<y>{FAC_W}) (?P<v2>{V})")
S_BOTH = re.compile(rf"(?P<g>.+?) {RES6} (?P<x>\S+ndriyañca) (?P<v1>{V}) (?P<y>\S+ndriyañca) (?P<v2>{V})")
S_HALF = re.compile(rf"(?P<g>.+?) {RES6} (?P<x>\S+ndriyañca) (?P<v1>{V})")      # ^6-10-301 (stray period)
S_TAIL = re.compile(rf"(?P<y>[A-ZĀĪŪ]\S+ndriyañca) (?P<v2>{V})")                 # «Somanassindriyañca uppajjissati.»
BOTH_HEAD, BOTH_TAIL = F.BOTH_C.split(", ", 1)                                  # «{a} {p}» / «đồng thời {b} cũng {p2}»
assert F.BOTH_C == f"{BOTH_HEAD}, {BOTH_TAIL}"


def _res(mm):
    return "tesaṃ tattha" if mm["t"] else "tesaṃ"


def _check_fem(mm, s):
    if mm["r"] == "tāsaṃ":
        assert "itthiyo" in mm["g"], s


def translate_sentence(s, ctx=""):
    s = s.strip()
    if s.endswith(".") and (" tesaṃ " in s or " tāsaṃ " in s):
        body = s[:-1]
        mm = S_NOT.fullmatch(body)
        if mm:
            assert mm["r"] == mm["r2"] and bool(mm["t"]) == bool(mm["t2"]), s
            _check_fem(mm, s)
            return F.b_not(_res(mm), head6(mm["g"], ctx), P.fm(mm["x"]), F.vparse(mm["v1"], ctx), P.fm(mm["y"]),
                           F.vparse(mm["v2"], ctx))
        mm = S_BOTH.fullmatch(body)
        if mm:
            _check_fem(mm, s)
            return F.b_both(_res(mm), head6(mm["g"], ctx), P.fm(mm["x"]), F.vparse(mm["v1"], ctx), P.fm(mm["y"]),
                            F.vparse(mm["v2"], ctx))
        mm = S_HALF.fullmatch(body)
        if mm:                                                         # first half of a both-answer (stray period)
            SLIPS.append((ctx, "stray period inside a both-answer («… itthindriyañca uppajjissati. "
                               "Somanassindriyañca uppajjissati.»); kept as two sentences"))
            clause = BOTH_HEAD.format(a=P.fm(mm["x"]), p=F.verb(*F.vparse(mm["v1"], ctx)))
            return cap(F.STATEMENT_RES.format(head=head6(mm["g"], ctx), res=F.RES_VI[_res(mm)], clause=clause))
        raise ValueError(f"unmatched person answer: {s!r} ({ctx})")
    mm = S_TAIL.fullmatch(s[:-1]) if s.endswith(".") else None
    if mm:                                                             # second half: «Đồng thời Y cũng v.»
        return cap(BOTH_TAIL.format(b=P.fm(mm["y"]), p2=F.verb(*F.vparse(mm["v2"], ctx)))) + "."
    return R.translate_sentence(s, ctx)                                # questions, places, Āmantā, mūlaka (10-04)


SLIP_FIX = [   # (Pāli as written, as read, report)
    ("somanassindriyaṃ na upapajjissati.", "somanassindriyaṃ na uppajjissati.",
     "«na upapajjissati» (verb of a faculty) read as «na uppajjissati»"),
    ("ghānindriyaṃ na uppajjissati no ca tattha", "ghānindriyaṃ na uppajjissati, no ca tattha",
     "missing comma before «no ca»; written"),
]


def translate_line(line, ctx=""):
    mm = re.match(r"^(?P<h>#+ )?(?P<t>.*?)(?P<id> \^[0-9A-Za-z-]+)?$", line)
    h, t, sid = mm["h"] or "", mm["t"], mm["id"] or ""
    if h:
        return h + P.heading(t) + sid
    for a, b, why in SLIP_FIX:
        if a in t:
            SLIPS.append((ctx, why))
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
    ("trạng thái nam tính", 1), ("trạng thái nữ tính", 1), ("nhập Niết-bàn trọn vẹn", 5),
    ("ngay sau", 5), ("chúng sinh Vô Tưởng", 5), ("cõi dục lạc", 1), ("cõi hình sắc", 1), ("người nam", 2),
    ("người nữ", 2), ("một số", 2),
]
# «kiếp sống» is pi-6's own word for bhava here (2-01 PACCHIMA «thuộc kiếp sống cuối cùng»; pi-1..5 «kiếp» = aeon)
assert "kiếp sống" in F.PACCHIMA


def check_cross_book():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in S.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts (10-06): {len(CROSS_BOOK)} strings found in pi-1..5 rails")


def check_frames():
    """Frames shared with the frame-setters stay byte-identical."""
    g = "Pacchimabhavikānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti"
    assert head6(g) == cap(E.who2(g)), (head6(g), E.who2(g))                       # 2-02
    for g in ("Rūpāvacarānaṃ arūpāvacarānaṃ", "Asaññasattānaṃ arūpānaṃ", "Itaresaṃ catuvokārānaṃ pañcavokārānaṃ",
              "Itaresaṃ kāmāvacarānaṃ", "Pacchimabhavikānaṃ", "Asaññasattānaṃ"):
        assert head6(g) == cap(F.who(g)), (head6(g), F.who(g))                    # 2-01
    g = "Ye arūpaṃ upapajjitvā parinibbāyissanti"
    assert head6(g) == cap(F.who(g)), (head6(g), F.who(g))                        # 2-01 YE_UPAPAJJITVA
    assert head6("Pacchimacittasamaṅgīnaṃ") == cap(C8.P_SUBJ["Pacchimacittasamaṅgīnaṃ"]), \
        (head6("Pacchimacittasamaṅgīnaṃ"), C8.P_SUBJ["Pacchimacittasamaṅgīnaṃ"])       # 8
    assert X6.ANANTARA == "vào tâm mà ngay sau đó {c} sẽ sinh khởi"
    assert X6.ANANTARA_K["kāmāvacarānaṃ"].startswith(C8.citta(last=True) + " ")   # 6-01 «tâm cuối cùng …»
    assert X6.LAST_AVITAKKA.startswith(C8.citta(last=True) + " ")
    assert _last_kind("upekkhāsampayutta") == "tâm cuối cùng gắn liền với sự bình thản"
    assert P.ATTR10["upekkhāya"] == "có sự bình thản đi kèm" and P.ATTR10["somanassena"] == "có niềm vui đi kèm"
    assert S.LABEL["Ka"] == "(a)" and S.LABEL["Kha"] == "(b)" and S.LABEL["Ṅa"] == "(đ)"


def check_parallel(pali):
    """Every sentence that the 10-02 / 10-03 / 10-04 parsers (same yamaka, same frames) can translate comes out
    byte-identical here."""
    mods = [("10-04", R), ("10-02", P), ("10-05", Y5)]
    try:
        mods.append(("10-03", importlib.import_module("build_10-03_vi")))
    except Exception as e:                            # noqa: BLE001
        print("note: build_10-03_vi not importable:", e)
    probs, n = [], {k: 0 for k, _ in mods}
    n["head5"] = 0
    for ln in pali.splitlines():
        if not ln.strip() or ln.startswith("#"):
            continue
        t = re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", ln)
        for a, b, _ in SLIP_FIX:
            t = t.replace(a, b)
        for s in P.split10(t):
            s = s.strip()
            if not s:
                continue
            mine = translate_sentence(s, "check")
            for tag, mod in mods:
                try:
                    theirs = mod.translate_sentence(s, "check")
                except (AssertionError, ValueError, KeyError, TypeError):
                    continue
                n[tag] += 1
                if theirs != mine:
                    probs.append(f"differs from {tag}: {s[:70]} | {theirs} | {mine}")
            mm = (S_NOT.fullmatch(s[:-1]) or S_BOTH.fullmatch(s[:-1]) or S_HALF.fullmatch(s[:-1])) \
                if s.endswith(".") else None
            if mm:
                try:
                    h5 = Y5.head5(mm["g"])
                except (AssertionError, ValueError, KeyError, TypeError):
                    continue
                n["head5"] += 1
                if h5 != head6(mm["g"]):
                    probs.append(f"head differs from 10-05 head5: {mm['g'][:70]} | {h5} | {head6(mm['g'])}")
    for _, mod in mods:
        if hasattr(mod, "SLIPS"):
            del mod.SLIPS[:]
    print("parallel checks:", ", ".join(f"{k} {v}" for k, v in n.items()))
    return probs


def check_same_as_other(text, pali):
    """Every Pāli line of this chapter that also occurs in a finished Indriya chapter has the same Vietnamese."""
    strip = lambda x: re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", x)          # noqa: E731
    probs, warn = [], []
    for nm in ("10-01-indriyayamaka.md", "10-02-indriyayamaka.md", "10-03-indriyayamaka.md",
               "10-04-indriyayamaka.md", "10-05-indriyayamaka.md"):
        vp = S.OUT_DIR / nm
        if not vp.exists():
            print(f"note: {nm} not written yet; not compared")
            continue
        p1 = (S.PALI_DIR / nm).read_text(encoding="utf-8").splitlines()
        v1 = vp.read_text(encoding="utf-8").splitlines()
        if len(p1) != len(v1):
            print(f"note: {nm} line count differs from its Pāli; not compared")
            continue
        ref = {strip(p): strip(v) for p, v in zip(p1, v1) if p.strip()}
        n = 0
        for p, v in zip(pali.splitlines(), text.splitlines()):
            if p.strip() and strip(p) in ref:
                n += 1
                if ref[strip(p)] != strip(v):
                    (warn if nm.startswith("10-05") else probs).append(f"differs from {nm}: {p[:70]}")
        print(f"lines shared with {nm} checked: {n}")
    for w in warn:
        print("WARN", w)
    return probs


def main():
    S.check_cross_book()
    F.check_cross_book()
    I.check_cross_book()
    P.check_cross_book()
    R.check_cross_book()
    check_cross_book()
    check_frames()
    pali = (S.PALI_DIR / NAME).read_text(encoding="utf-8")
    pprobs = check_parallel(pali)
    for mod in (R, P, F):
        del mod.SLIPS[:]
    del SLIPS[:]
    text = unicodedata.normalize("NFC", translate_file())
    probs = (S.check_lines(pali, text, NAME) + I.check_extra(text, pali) + check_same_as_other(text, pali)
             + pprobs)
    for i, ln in enumerate(text.splitlines(), 1):
        body = re.sub(r" ?\[[^\]]*\]", "", re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", ln))
        for bad in ("uppajj", "upapajj", "tesaṃ", "tāsaṃ", "tattha", "mūlakaṃ", "kkhaṇe", "thì thì",
                    "là không phải", "ndriya", "….", "  ", "là là", "ānaṃ", "Āmantā", "eteneva", "bhāv", "anantarā",
                    "pacchima", "parinibb", " ye ", " yā ", "itthiyo", "purisā", "sẽ sẽ", "và và"):
            if bad in body:
                probs.append(f"line {i}: «{bad}»")
    with open(S.OUT_DIR / NAME, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    segs = len(re.findall(r"\^[0-9A-Za-z-]+\s*$", text, flags=re.M))
    print(f"wrote {NAME}: {len([x for x in text.splitlines() if x.strip()])} lines, {segs} segments")
    seen = set()
    for c, w in SLIPS + R.SLIPS + P.SLIPS + F.SLIPS:
        if (c, w) not in seen:
            seen.add((c, w))
            print("SLIP", c, "|", w)
    for p in probs[:80]:
        print("PROBLEM", p)
    print("line checks:", "OK" if not probs else f"{len(probs)} problems")
    sys.exit(1 if probs else 0)


if __name__ == "__main__":
    main()
