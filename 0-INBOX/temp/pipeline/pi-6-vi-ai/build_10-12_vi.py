# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 10-12-indriyayamaka.md (Indriyayamaka, pavattivāra, uppādavāra
(6) atītānāgatavāra: anulomapuggalo … paccanīkapuggalokāsā; «Pavattivāro niṭṭhito.»; the heading Pariññāvāro).

Frames, imported and used VERBATIM:
  build_10-04_vi  (R): translate_sentence() for the questions (yassa / yattha / yassa yattha, «…pe…» runs in the
                  second slot), Āmantā, Natthi, the short answers (Uppajjittha. / Uppajjissati.), the mūlaka notes;
  build_10-05_vi  (Y5): translate_sentence() for a question with a run in the FIRST slot (^6-10-424), ye_bhava(),
                  ye_attr(), last_citta(), YE_FRAME / UPA_ATTR / SAHA / YE_NOUN (head5 checked);
  build_10-06_vi  (Y6): S_NOT / S_BOTH (answer regexes), _planes(), the «ye ca <plane> upapajjitvā …» clause
                  (head6 checked);
  build_10-07_vi  (Y7): head rule «persons in a row share one «ở»» (head7 checked where it parses);
  build_10-08_vi  (Y8): «…? …Pe….» = «… không? …» (translate_sentence checked);
  build_10-02_vi  (P): fm(), split10, heading, mūlaka notes;
  build_2-01_vi   (F): family B (b_not / b_both, vparse, who(), WHO_HEAD, LIST_SEP, YE_UPAPAJJITVA);
  build_2-02_vi   (E): YE_CA_JOIN «… và …», EXACT «Pavattivāro niṭṭhito.», pe_end rule (who2 checked);
  build_5-01_vi   (T5): VATTAMANA / CITTA_KIND «khi tâm thứ hai đang diễn ra» (head_vi checked);
  build_6-01_vi   (X6): ANANTARA «vào tâm mà ngay sau đó … sẽ sinh khởi» (head checked);
  build_8_vi      (C8): SAMANGI / citta(last=True) «những người có được tâm cuối cùng»;
  labels from build_sample_vi.LABEL.
New here (notes-10-12.md): «ye ca upekkhāya / somanassena upapajjitvā parinibbāyissanti» and «ye ca purisā / yā ca
itthiyo upekkhāya / somanassena upapajjitvā parinibbāyissanti» (10-05 YE_FRAME + UPA_ATTR), the mūlaka note followed
by «…pe….», and head12() (the 10-07 / 5-01 rule over the heads of this chapter).

Importing writes nothing; run  python -I -X utf8 -B build_10-12_vi.py  to rebuild the chapter.
"""
import importlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as S  # noqa: E402

F = importlib.import_module("build_2-01_vi")     # family B
E = importlib.import_module("build_2-02_vi")     # «ye ca …» join, closing lines
I = importlib.import_module("build_10-01_vi")    # faculty table, check_extra
P = importlib.import_module("build_10-02_vi")    # Indriya pavatti frames
R = importlib.import_module("build_10-04_vi")    # questions, short answers
Y5 = importlib.import_module("build_10-05_vi")   # ye_bhava / ye_attr / last_citta, first-slot runs
Y6 = importlib.import_module("build_10-06_vi")   # answer regexes, «ye ca <plane> …»
T5 = importlib.import_module("build_5-01_vi")    # dutiye citte vattamāne
X6 = importlib.import_module("build_6-01_vi")    # ANANTARA
C8 = importlib.import_module("build_8_vi")       # samaṅgī, last citta

NAME = "10-12-indriyayamaka.md"
cap, low = S.cap, S.low
LABEL = S.LABEL
SLIPS = []
OI = F.WHO_HEAD.format(g="")                      # «ở »
assert OI == Y6.OI


def _strip_o(s):
    assert s.startswith(OI), s
    return s[len(OI):]


# ================================================================ the nominative «ye …» clauses
assert Y5.YE_FRAME.format(n="người", what="tái sinh vào {p}") == F.YE_UPAPAJJITVA


def ye_saha(saha, noun=None):
    """NEW: «ye (ca) upekkhāya upapajjitvā parinibbāyissanti» = «những người nào sau khi tái sinh có sự bình thản đi
    kèm sẽ nhập Niết-bàn trọn vẹn»; with «purisā / itthiyo» = «những người nam / nữ nào …» (10-05 YE_FRAME, UPA_ATTR,
    SAHA, YE_NOUN; the same pieces as ye_bhava() / ye_attr())."""
    n = Y5.YE_NOUN[noun] if noun else "người"
    return Y5.YE_FRAME.format(n=n, what=Y5.UPA_ATTR.format(a=Y5.SAHA[saha]))


AWITH = r"(?:upekkhāya|somanassena)"
ACCP = r"(?:rūpāvacaraṃ|arūpāvacaraṃ|arūpaṃ)"
REL = r"(?P<rel>ye ca|yā ca|ye|yā)"
STOP = {"ye", "yā", "yassa", "dutiye", "pacchimacittasamaṅgīnaṃ"}

ELEMENTS = [   # (regex at the current position, kind, function); kinds: T time (alone), Y «ye …» clause,
    #           S pacchimacittasamaṅgī (a person piece)
    (r"yassa cittassa anantarā (?P<k>\S+?)pacchimacittaṃ uppajjissati", "T",
     lambda m: X6.ANANTARA.format(c=Y5.last_citta(m["k"]))),                              # 6-01 / 10-05 / 10-06
    (r"dutiye citte vattamāne", "T", lambda m: T5.VATTAMANA.format(c=T5.CITTA_KIND["dutiye"])),   # 5-01
    (rf"{REL} (?P<n>purisā|itthiyo) eteneva bhāvena katici bhave dassetvā (?:(?P<a>{AWITH}) upapajjitvā )?"
     r"parinibbāyissanti", "Y", lambda m: Y5.ye_bhava(m["n"], m["a"])),                    # 10-05
    (rf"{REL} (?P<n>purisā|itthiyo) (?P<a>{AWITH}) upapajjitvā parinibbāyissanti", "Y",
     lambda m: ye_saha(m["a"], m["n"])),                                                    # new
    (rf"{REL} (?P<h>sacakkhukā|saghānakā) (?P<a>{AWITH}) upapajjitvā parinibbāyissanti", "Y",
     lambda m: Y5.ye_attr(m["h"], m["a"])),                                                 # 10-05
    (rf"{REL} (?P<a>{AWITH}) upapajjitvā parinibbāyissanti", "Y", lambda m: ye_saha(m["a"])),   # new
    (rf"{REL} (?P<pl>(?:{ACCP} )*{ACCP}) upapajjitvā parinibbāyissanti", "Y",
     lambda m: F.YE_UPAPAJJITVA.format(p=Y6._planes(m["pl"]))),                            # 2-01 / 10-06
    (r"pacchimacittasamaṅgīnaṃ", "S", lambda m: C8.SAMANGI.format(c=C8.citta(last=True))),   # 8 / 10-06
]
ELEMENTS = [(re.compile(p + r"(?= |$)"), k, f) for p, k, f in ELEMENTS]


def head12(g, ctx=""):
    """Pāli answer head (before tesaṃ / tāsaṃ (tattha)) -> Vietnamese head, capitalised.
    Persons in a row share one «ở» (2-01 who() over the whole run of plane / being words; 5-01 head_vi, 10-07 head7);
    a time phrase stands alone; «ye ca / yā ca …» joins the persons before it with « và » (2-02 who2); a «ye …» clause
    at the start has no «ở» (2-01); all pieces joined «, »."""
    p, i, pieces = low(g), 0, []            # pieces: [kind, [texts]]
    while i < len(p):
        for rx, kind, fn in ELEMENTS:
            mm = rx.match(p, i)
            if mm:
                break
        else:
            mm, kind = None, "P"
        if mm:
            vi, i2 = fn(mm), mm.end() + 1
        else:                                # a run of plane / being words: 2-01 who()
            toks, j = [], i
            rest = p[i:].split(" ")
            for t in rest:
                if t in STOP:
                    break
                toks.append(t)
            assert toks, (g, p[i:])
            vi = _strip_o(F.who(" ".join(toks)))
            i2 = i + len(" ".join(toks)) + 1
        if kind in ("P", "S"):
            if pieces and pieces[-1][0] == "P":
                pieces[-1][1].append(vi)
            else:
                pieces.append(["P", [vi]])
        elif kind == "Y":
            if mm["rel"].endswith(" ca"):
                assert pieces and pieces[-1][0] == "P", g
                pieces[-1][1][-1] += E.YE_CA_JOIN + vi
            else:
                assert not pieces, g
                pieces.append(["N", [vi]])
        else:
            pieces.append(["T", [vi]])
        i = i2
    out = [OI + F.LIST_SEP.join(v) if k == "P" else v[0] for k, v in pieces]
    return cap(F.LIST_SEP.join(out))


# ================================================================ sentences
PE_Q_END = "…Pe…."                                 # «…tattha Y uppajjissatīti?…Pe….» (10-08: «? …»)
MULAKA_PE = re.compile(r"(?P<n>\([A-ZĀĪŪ]\S+mūlakaṃ\))…pe…\.")   # «(Paññindriyamūlakaṃ)…pe….» (new: note + «…»)
FIRST_RUN = re.compile(r"(?:\((?:Ka|Kha)\) )?[Yy]assa (?:vā pana )?(?:yattha )?\S+…")


def translate_sentence(s, ctx=""):
    s = s.strip()
    if s == "Pavattivāro niṭṭhito.":
        return E.EXACT[s]                                              # 2-02
    if s.endswith("?" + PE_Q_END):
        return translate_sentence(s[:-len(PE_Q_END)], ctx) + " …"      # 10-08
    mm = MULAKA_PE.fullmatch(s)
    if mm:
        return P.translate_sentence(mm["n"], ctx) + E.PE              # «(Phần dựa trên …)…»
    if s.endswith(".") and (" tesaṃ " in s or " tāsaṃ " in s):
        body = s[:-1]
        for rx, both in ((Y6.S_NOT, False), (Y6.S_BOTH, True)):
            mm = rx.fullmatch(body)
            if not mm:
                continue
            if not both:
                assert mm["r"] == mm["r2"] and bool(mm["t"]) == bool(mm["t2"]), s
            if mm["r"] == "tāsaṃ":
                assert "itthiyo" in mm["g"], s
            res = "tesaṃ tattha" if mm["t"] else "tesaṃ"
            f = F.b_both if both else F.b_not
            return f(res, head12(mm["g"], ctx), P.fm(mm["x"]), F.vparse(mm["v1"], ctx), P.fm(mm["y"]),
                     F.vparse(mm["v2"], ctx))
        raise ValueError(f"unmatched person answer: {s!r} ({ctx})")
    if s.endswith("?") and FIRST_RUN.match(s):
        return Y5.translate_sentence(s, ctx)                           # run in the first slot (10-05)
    return R.translate_sentence(s, ctx)                                # questions, short answers, notes (10-04)


def translate_line(line, ctx=""):
    mm = re.match(r"^(?P<h>#+ )?(?P<t>.*?)(?P<id> \^[0-9A-Za-z-]+)?$", line)
    h, t, sid = mm["h"] or "", mm["t"], mm["id"] or ""
    if h:
        return h + P.heading(t) + sid
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
    ("nhập Niết-bàn trọn vẹn", 5), ("tái sinh", 2), ("sự bình thản", 1), ("niềm vui", 2), ("chúng sinh Vô Tưởng", 5),
    ("cõi dục lạc", 1), ("cõi hình sắc", 1), ("gồm năm khối", 2), ("gồm bốn khối", 2), ("đang diễn ra", 5),
    ("ngay sau", 5), ("người nam", 2), ("người nữ", 2), ("Không có.", 3), ("Đúng vậy.", 5),
]


def check_cross_book():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in S.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts (10-12): {len(CROSS_BOOK)} strings found in pi-1..5 rails")


def check_frames():
    """Fixed frames shared with the frame-setters stay byte-identical."""
    g = "Pacchimabhavikānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti"
    assert head12(g) == cap(E.who2(g)), (head12(g), E.who2(g))                         # 2-02
    for g in ("Itaresaṃ", "Pacchimabhavikānaṃ", "Pañcavokāre pacchimabhavikānaṃ", "Itaresaṃ pañcavokārānaṃ",
              "Kāmāvacare pacchimabhavikānaṃ rūpāvacarānaṃ", "Suddhāvāsaṃ upapajjantānaṃ", "Arūpānaṃ",
              "Suddhāvāsānaṃ arūpe pacchimabhavikānaṃ asaññasattānaṃ", "Rūpāvacarānaṃ arūpāvacarānaṃ",
              "Itaresaṃ catuvokārānaṃ pañcavokārānaṃ", "Rūpāvacare arūpāvacare pacchimabhavikānaṃ asaññasattānaṃ"):
        assert head12(g) == cap(F.who(g)), (head12(g), F.who(g))                       # 2-01
    assert head12("Pacchimacittasamaṅgīnaṃ asaññasattānaṃ") == \
        T5.head_vi("Pacchimacittasamaṅgīnaṃ asaññasattānaṃ") == \
        "Ở những người có được tâm cuối cùng, chúng sinh Vô Tưởng"                     # 5-01 / 6-01
    assert head12("Suddhāvāsānaṃ dutiye citte vattamāne") == T5.head_vi("Suddhāvāsānaṃ dutiye citte vattamāne")
    assert ye_saha("upekkhāya") == "những người nào sau khi tái sinh có sự bình thản đi kèm sẽ nhập Niết-bàn trọn vẹn"
    assert ye_saha("somanassena", "itthiyo") == \
        "những người nữ nào sau khi tái sinh có niềm vui đi kèm sẽ nhập Niết-bàn trọn vẹn"
    assert Y5.ye_attr("sacakkhukā", "upekkhāya").endswith(ye_saha("upekkhāya")[len("những người nào sau khi tái sinh"):])
    assert E.EXACT["Pavattivāro niṭṭhito."] == "Mục về sự diễn tiến đã hoàn tất."
    assert S.LABEL["Ka"] == "(a)" and S.LABEL["Kha"] == "(b)" and S.LABEL["Ṅa"] == "(đ)" and S.LABEL["Ca"] == "(e)"


# 10-06 head6 gives every genitive group its own «ở»; 5-01 / 6-01 / 10-07 (and head12) let persons in a row share one
HEAD_DIFF_OK = {("head6", "Pacchimacittasamaṅgīnaṃ asaññasattānaṃ")}


def check_parallel(pali):
    """Every sentence / head a frame-setter's own parser can translate comes out byte-identical here."""
    mods = [("10-04", R), ("10-05", Y5), ("10-06", Y6), ("10-02", P)]
    for tag, nm in (("10-03", "build_10-03_vi"), ("10-07", "build_10-07_vi"), ("10-08", "build_10-08_vi")):
        try:
            mods.append((tag, importlib.import_module(nm)))
        except Exception as e:                            # noqa: BLE001 (parallel agents)
            print(f"note: {nm} not importable:", e)
    heads = [("head5", Y5.head5), ("head6", Y6.head6), ("head_vi", T5.head_vi), ("6-01", lambda x: cap(X6.head(x))),
             ("who", lambda x: cap(F.who(x))), ("who2", lambda x: cap(E.who2(x)))]
    for tag, mod in mods:
        if tag == "10-07" and hasattr(mod, "head7"):
            heads.append(("head7", mod.head7))
        if tag == "10-08" and hasattr(mod, "head8"):
            heads.append(("head8", mod.head8))
    probs, n = [], {}
    for ln in pali.splitlines():
        if not ln.strip() or ln.startswith("#"):
            continue
        t = re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", ln)
        for s in P.split10(t):
            s = s.strip()
            if not s:
                continue
            mine = translate_sentence(s, "check")
            mm = (Y6.S_NOT.fullmatch(s[:-1]) or Y6.S_BOTH.fullmatch(s[:-1])) if s.endswith(".") else None
            for tag, mod in mods:
                try:
                    theirs = mod.translate_sentence(s, "check")
                except (AssertionError, ValueError, KeyError, TypeError, IndexError, AttributeError):
                    continue
                n[tag] = n.get(tag, 0) + 1
                if mm and tag == "10-06" and ("head6", mm["g"]) in HEAD_DIFF_OK:
                    n["10-06 known head difference"] = n.get("10-06 known head difference", 0) + 1
                    continue
                if theirs != mine:
                    probs.append(f"differs from {tag}: {s[:70]} | {theirs} | {mine}")
            if not mm:
                continue
            g, h = mm["g"], head12(mm["g"])
            for tag, fn in heads:
                try:
                    o = fn(g)
                except (AssertionError, ValueError, KeyError, TypeError, IndexError, AttributeError):
                    continue
                n[tag] = n.get(tag, 0) + 1
                if o != h and (tag, g) not in HEAD_DIFF_OK:
                    probs.append(f"head differs from {tag}: {g} | {o} | {h}")
    for _, mod in mods:
        if hasattr(mod, "SLIPS"):
            del mod.SLIPS[:]
    del F.SLIPS[:]
    del SLIPS[:]
    print("parallel checks:", ", ".join(f"{k} {v}" for k, v in n.items()))
    return probs


def check_same_as_other(text, pali):
    """Every Pāli line of this chapter that also occurs in a finished Indriya chapter has the same Vietnamese."""
    strip = lambda x: re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", x)          # noqa: E731
    probs = []
    for k in range(1, 12):
        nm = f"10-{k:02d}-indriyayamaka.md"
        vp = S.OUT_DIR / nm
        if not vp.exists():
            print(f"note: {nm} not written yet; not compared")
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
                    probs.append(f"differs from {nm}: {p[:70]} | {ref[strip(p)][:80]} | {strip(v)[:80]}")
        print(f"lines shared with {nm} checked: {c}")
    return probs


def main():
    S.check_cross_book()
    F.check_cross_book()
    I.check_cross_book()
    P.check_cross_book()
    R.check_cross_book()
    Y5.check_cross_book()
    Y6.check_cross_book()
    check_cross_book()
    check_frames()
    pali = (S.PALI_DIR / NAME).read_text(encoding="utf-8")
    pprobs = check_parallel(pali)
    for mod in (R, P, F, Y5, Y6):
        del mod.SLIPS[:]
    del SLIPS[:]
    text = unicodedata.normalize("NFC", translate_file())
    probs = (S.check_lines(pali, text, NAME) + I.check_extra(text, pali) + check_same_as_other(text, pali)
             + pprobs)
    for i, ln in enumerate(text.splitlines(), 1):
        body = re.sub(r" ?\[[^\]]*\]", "", re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", ln))
        for bad in ("uppajj", "upapajj", "tesaṃ", "tāsaṃ", "tattha", "mūlakaṃ", "kkhaṇe", "thì thì",
                    "là không phải", "ndriy", "….", "  ", "là là", "ānaṃ", "Āmantā", "eteneva", "bhāv", "anantarā",
                    "pacchima", "parinibb", " ye ", " yā ", "itthiyo", "purisā", "sẽ sẽ", "và và", "Natthi", "pe…",
                    "Pe…", "niṭṭhit", "ṃ", "ā ", ", ở chúng sinh trong cõi Tịnh Cư đang"):
            if bad in body:
                probs.append(f"line {i}: «{bad}»")
    with open(S.OUT_DIR / NAME, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    segs = len(re.findall(r"\^[0-9A-Za-z-]+\s*$", text, flags=re.M))
    print(f"wrote {NAME}: {len([x for x in text.splitlines() if x.strip()])} lines, {segs} segments")
    seen = set()
    for c, w in SLIPS + R.SLIPS + P.SLIPS + F.SLIPS + Y5.SLIPS + Y6.SLIPS:
        if (c, w) not in seen:
            seen.add((c, w))
            print("SLIP", c, "|", w)
    for p in probs[:80]:
        print("PROBLEM", p)
    print("line checks:", "OK" if not probs else f"{len(probs)} problems")
    sys.exit(1 if probs else 0)


if __name__ == "__main__":
    main()
