# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 10-08-indriyayamaka.md (Indriyayamaka, pavattivāra, uppādavāra
(4) paccuppannātītavāra: anulomapuggalo … paccanīkapuggalokāsā; the heading of (5) paccuppannānāgatavāra).

Frames, imported and used VERBATIM:
  build_10-04_vi  (R): translate_sentence() for every question (yassa / yattha / yassa yattha, with «…pe…» runs),
                  Āmantā, Natthi, the mūlaka notes (through build_10-02_vi), P4_NOT / P4_BOTH (person-and-place
                  answers), head4 (checked);
  build_10-02_vi  (P): fm, ATTR10 (attribute beings), PARTICIPLE10, citta_kind / moment, PAVATTE, P_NOT / P_BOTH,
                  head10 (checked), split10, heading;
  build_10-03_vi  (Q): head13 (checked), translate_sentence (checked);
  build_2-01_vi   (F): family B (b_not / b_both, vparse, who(), WHO_HEAD, LIST_SEP, HEAD, PARTICIPLE, NATTHI);
  build_3-01_vi   (A3): ATTR_GROUP / ATTR_JOIN, who3 (checked);
  build_3-02_vi   (A32): ATTR_PLANE_GROUP («những người đang tái sinh vào cõi dục lạc mà không có mắt»), who32 (checked);
  build_5-01_vi   (T5): SABBESAM_ALONE, CITTA_KIND["upapatti"] «tâm tái sinh», head_vi (checked);
  build_8_vi      (C8): NIRODHA_PERSONS, AT / OF / MOMENT;
  labels from build_sample_vi.LABEL.
New here (notes-10-08.md): head8() = the same element rule over the person groups of this chapter (attribute beings
of 10-02 together with a plane, after «itaresaṃ», and the genitive plane beings), the «?…Pe….» / «Natthi…pe….» lines.

Importing writes nothing; run  python -I -X utf8 -B build_10-08_vi.py  to rebuild the chapter.
"""
import importlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as S  # noqa: E402

F = importlib.import_module("build_2-01_vi")     # families A / B
I = importlib.import_module("build_10-01_vi")    # faculty table, extra checks
P = importlib.import_module("build_10-02_vi")    # Indriya pavatti frames
Q = importlib.import_module("build_10-03_vi")    # head13
R = importlib.import_module("build_10-04_vi")    # head4, person-and-place sentences
A3 = importlib.import_module("build_3-01_vi")    # attribute groups, who3
A32 = importlib.import_module("build_3-02_vi")   # attribute groups with a plane, who32
T5 = importlib.import_module("build_5-01_vi")    # bare sabbesaṃ, upapatticitta, head_vi
C8 = importlib.import_module("build_8_vi")       # moments, nirodhasamāpanna

NAME = "10-08-indriyayamaka.md"
cap, low = S.cap, S.low
LABEL = S.LABEL
SLIPS = []
OI = F.WHO_HEAD.format(g="")                      # «ở »

# ================================================================ answer heads (head8)
PARTS = {"upapajjantānaṃ", "upapajjantīnaṃ", "cavantānaṃ", "parinibbantānaṃ"}
PART_SLIP = {"cavantāna": "cavantānaṃ"}           # ^6-10-361 «asaññasattā cavantāna» (spelling; parallels cavantānaṃ)
KHANE = re.compile(r"(?P<mo>uppāda|bhaṅga)kkhaṇe")
SABBE = T5.SABBESAM_ALONE                         # bare Sabbesaṃ = tất cả chúng sinh (coordinator)
NIRODHA = C8.NIRODHA_PERSONS                      # những người nhập thành tựu thiền chấm dứt (8)


def _strip_o(s):
    assert s.startswith(OI), s
    return s[len(OI):]


def _attr_len(w, k):
    if k + 1 < len(w) and f"{w[k]} {w[k + 1]}" in P.ATTR10:
        return 2
    return 1 if k < len(w) and w[k] in P.ATTR10 else 0


def _moment(tok, mo_tok):
    mm = KHANE.fullmatch(mo_tok)
    assert tok.endswith("cittassa") and mm, (tok, mo_tok)
    kind = tok[:-len("cittassa")]
    if kind == "upapatti":                        # upapatticittassa = của tâm tái sinh (5-01)
        return C8.AT.format(x=C8.OF.format(x=C8.MOMENT[mm["mo"]], c=T5.CITTA_KIND["upapatti"]))
    return P.moment(kind, mm["mo"])


def _persons(w):
    """A run of person words -> list of Vietnamese groups (without «ở»). Attribute groups as 10-02 / 3-01 / 3-02;
    every other stretch through 2-01 who()."""
    groups, other, i, n = [], [], 0, len(w)

    def flush():
        if other:
            groups.append(_strip_o(F.who(" ".join(other))))
            other.clear()

    while i < n:
        k, mod = i, None
        if w[k] in ("sabbesaṃ", "itaresaṃ") and _attr_len(w, k + 1):
            mod, k = w[k], k + 1
        if not _attr_len(w, k):
            other.append(w[i]); i += 1
            continue
        flush()
        attrs = []
        while _attr_len(w, k):
            L = _attr_len(w, k)
            attrs.append(P.ATTR10[" ".join(w[k:k + L])]); k += L
        planes = []
        while k < n and F._plane_case(w[k])[0] == "acc":
            planes.append(F.PLANE[F._plane_case(w[k])[1]]); k += 1
        assert k < n and w[k] in PARTS, w
        vi, prep, _need = F.PARTICIPLE[P.PARTICIPLE10.get(w[k], w[k])]
        a = A3.ATTR_JOIN.join(attrs)
        if planes:
            assert w[k] in ("upapajjantānaṃ", "upapajjantīnaṃ"), w
            groups.append(A32.ATTR_PLANE_GROUP.format(h=F.HEAD[mod], p=vi, prep=prep, planes=F.LIST_SEP.join(planes),
                                                      a=a))
        else:
            groups.append(A3.ATTR_GROUP.format(h=F.HEAD[mod], p=vi, a=a))
        i = k + 1
    flush()
    return groups


def head8(g, ctx=""):
    """Pāli answer head (before tesaṃ / tāsaṃ tattha) -> Vietnamese head, capitalised. Persons in a row share one «ở»,
    a time phrase stands alone, all joined «, » (2-01 WHO_HEAD / LIST_SEP; = 10-03 head13, 10-04 head4, 5-01 head_vi)."""
    w = [low(x) for x in g.split()]
    for j, x in enumerate(w):
        if x in PART_SLIP:
            SLIPS.append((ctx, f"«{x}» read as «{PART_SLIP[x]}» (spelling)"))
            w[j] = PART_SLIP[x]
    els, i, n = [], 0, len(w)
    while i < n:
        x = w[i]
        if x == "pavatte":
            els.append(("T", P.PAVATTE)); i += 1
        elif x.endswith("cittassa"):
            els.append(("T", _moment(x, w[i + 1]))); i += 2
        elif x == "nirodhasamāpannānaṃ":
            els.append(("P", NIRODHA)); i += 1
        elif x == "sabbesaṃ" and (i + 1 == n or w[i + 1] == "pavatte" or w[i + 1].endswith("cittassa")):
            els.append(("P", SABBE)); i += 1
        else:
            j = i
            while j < n and w[j] != "pavatte" and not w[j].endswith("cittassa") and w[j] != "nirodhasamāpannānaṃ":
                j += 1
            els.extend(("P", t) for t in _persons(w[i:j]))
            i = j
    out, prev_p = [], False
    for kind, vi in els:
        if kind == "P" and not prev_p:
            vi = OI + vi
        out.append(vi)
        prev_p = kind == "P"
    return cap(F.LIST_SEP.join(out))


# ================================================================ sentences
MULAKA_SLIP = {"(Ghānandriyamūlakaṃ)": "(Ghānindriyamūlakaṃ)"}   # ^6-10-336 (spelling; = ^6-10-346)
PE_Q_END = "…Pe…."                                 # «…tattha Y uppajjitthāti?…Pe….» (10-01: «? …»)
NATTHI_PE = "Natthi…pe…."                          # 7-04 rule: «Không có…»


def translate_sentence(s, ctx=""):
    s = s.strip()
    if s in MULAKA_SLIP:
        SLIPS.append((ctx, f"«{s}» read as «{MULAKA_SLIP[s]}» (spelling)"))
        s = MULAKA_SLIP[s]
    if s == NATTHI_PE:
        return F.NATTHI[:-1] + "…"
    if s.endswith("?" + PE_Q_END):
        return translate_sentence(s[:-len(PE_Q_END)], ctx) + " …"
    if s[-1:] == ".":
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
            return f(res, head8(mm["g"], ctx), P.fm(mm["x"]), F.vparse(mm["v1"], ctx), P.fm(mm["y"]),
                     F.vparse(mm["v2"], ctx))
    return R.translate_sentence(s, ctx)


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
    ("tất cả chúng sinh", 2), ("đời sống", 1), ("khoảnh khắc tan rã", 5), ("chúng sinh Vô Tưởng", 5),
    ("Không có.", 3), ("chết đi", 2), ("cõi dục lạc", 1), ("cõi hình sắc", 1), ("tái sinh", 2),
    ("nhập Niết-bàn trọn vẹn", 5), ("thành tựu thiền chấm dứt", 5), ("gồm năm khối", 2), ("gồm bốn khối", 2),
]


def check_cross_book():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in S.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts (10-08): {len(CROSS_BOOK)} strings found in pi-1..5 rails")


def check_frames():
    """Fixed frames shared with the frame-setters stay byte-identical (heads taken from 3-02 / 5-01 output)."""
    assert head8("Pañcavokārā cavantānaṃ acakkhukānaṃ kāmāvacaraṃ upapajjantānaṃ") == \
        "Ở những người đang chết đi khỏi cõi gồm năm khối, những người đang tái sinh vào cõi dục lạc mà không có mắt"
    assert head8("Suddhāvāsānaṃ upapatticittassa uppādakkhaṇe asaññasattaṃ upapajjantānaṃ") == \
        ("Ở chúng sinh trong cõi Tịnh Cư, vào khoảnh khắc sinh khởi của tâm tái sinh, ở những người đang tái sinh "
         "vào cõi Vô Tưởng")
    assert head8("Itaresaṃ catuvokāraṃ pañcavokāraṃ upapajjantānaṃ pavatte cittassa uppādakkhaṇe") == \
        ("Ở những người khác đang tái sinh vào cõi gồm bốn khối, cõi gồm năm khối, trong đời sống, vào khoảnh khắc "
         "sinh khởi của tâm")
    assert head8("Itaresaṃ sacakkhukānaṃ upapajjantānaṃ") == cap(A3.who3("Itaresaṃ sacakkhukānaṃ upapajjantānaṃ"))
    assert P.PAVATTE == T5.PAVATTE and P.PAVATTE_JOIN == T5.PAVATTE_JOIN
    assert S.LABEL["Ka"] == "(a)" and S.LABEL["Kha"] == "(b)" and S.LABEL["Ca"] == "(e)"


def check_parallel(pali):
    """Every sentence the 10-02 / 10-03 / 10-04 parsers translate, and every head that head4 / head10 / head13 /
    who3 / who32 / 5-01 head_vi translate, comes out byte-identical here."""
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
            for tag, mod in (("10-02", P), ("10-03", Q), ("10-04", R)):
                try:
                    theirs = mod.translate_sentence(s, "check")
                except (AssertionError, ValueError, KeyError, TypeError, IndexError):
                    continue
                n[tag] = n.get(tag, 0) + 1
                if theirs != mine:
                    probs.append(f"differs from {tag}: {s[:70]} | {theirs} | {mine}")
            mm = R.P4_NOT.fullmatch(s[:-1]) or R.P4_BOTH.fullmatch(s[:-1]) or P.P_NOT.fullmatch(s[:-1]) or \
                P.P_BOTH.fullmatch(s[:-1])
            if not mm:
                continue
            g, h = mm["g"], head8(mm["g"], "check")
            for tag, fn in (("head4", R.head4), ("head10", P.head10), ("head13", Q.head13), ("who3", A3.who3),
                            ("who32", A32.who32), ("head_vi", T5.head_vi)):
                try:
                    o = cap(fn(g))
                except (AssertionError, ValueError, KeyError, TypeError, IndexError):
                    continue
                n[tag] = n.get(tag, 0) + 1
                if o != h:
                    probs.append(f"head differs from {tag}: {g} | {o} | {h}")
    for mod in (P, Q, R, F):
        del mod.SLIPS[:]
    del SLIPS[:]
    print("parallel checks:", ", ".join(f"{k} {v}" for k, v in n.items()))
    return probs


def check_same_as_other(text, pali):
    """Every Pāli line of this chapter that also occurs in a finished Indriya chapter has the same Vietnamese."""
    strip = lambda x: re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", x)          # noqa: E731
    probs = []
    for nm in ("10-01-indriyayamaka.md", "10-02-indriyayamaka.md", "10-03-indriyayamaka.md",
               "10-04-indriyayamaka.md", "10-05-indriyayamaka.md", "10-06-indriyayamaka.md",
               "10-07-indriyayamaka.md"):
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
        k = 0
        for p, v in zip(pali.splitlines(), text.splitlines()):
            if p.strip() and strip(p) in ref:
                k += 1
                if ref[strip(p)] != strip(v):
                    probs.append(f"differs from {nm}: {p[:70]}")
        print(f"lines shared with {nm} checked: {k}")
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
    text = unicodedata.normalize("NFC", translate_file())
    probs = (S.check_lines(pali, text, NAME) + I.check_extra(text, pali) + check_same_as_other(text, pali)
             + pprobs)
    for i, ln in enumerate(text.splitlines(), 1):
        body = re.sub(r" ?\[[^\]]*\]", "", re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", ln))
        for bad in ("uppajj", "upapajj", "tesaṃ", "tāsaṃ", "tattha", "mūlakaṃ", "vinā", "kkhaṇe", "thì thì",
                    "là không phải", "ndriya", "sabbesaṃ", "Sabbesaṃ", "….", "  ", "là là", "ānaṃ", "Āmantā",
                    "antāna", "Natthi", "Pe…", "cittassa"):
            if bad in body:
                probs.append(f"line {i}: «{bad}»")
    with open(S.OUT_DIR / NAME, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    segs = len(re.findall(r"\^[0-9A-Za-z-]+\s*$", text, flags=re.M))
    print(f"wrote {NAME}: {len([x for x in text.splitlines() if x.strip()])} lines, {segs} segments")
    seen = set()
    for c, w in SLIPS + P.SLIPS + R.SLIPS + F.SLIPS:
        if (c, w) not in seen:
            seen.add((c, w))
            print("SLIP", c, "|", w)
    for p in probs[:80]:
        print("PROBLEM", p)
    print("line checks:", "OK" if not probs else f"{len(probs)} problems")
    sys.exit(1 if probs else 0)


if __name__ == "__main__":
    main()
