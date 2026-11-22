# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 10-03-indriyayamaka.md (Indriyayamaka, pavattivāra, uppādavāra
(1) paccuppannavāra: (Ga) anulomapuggalokāsā, (Gha) paccanīkapuggalo).

Frames, imported and used VERBATIM:
  build_10-02_vi  (P): the faculty names (fm), the attribute beings (ATTR10, attr_group: «những người đang tái sinh có
                  mắt và là người nữ»), the citta kinds and moments (citta_kind, moment), pavatte, head10 (checked),
                  split10, heading;
  build_2-01_vi   (F): family B (b_q, b_not, b_both, vparse, who, WHO_HEAD, LIST_SEP, NO, BEINGS);
  build_3-01_vi   (A3): MULAKA «(Phần dựa trên …)», who3 (checked: «Ở tất cả những người đang chết đi, những người
                  đang tái sinh không có mắt và không có tai»);
  build_5-01_vi   (T5): SABBESAM_ALONE «tất cả chúng sinh», PAVATTE / PAVATTE_JOIN, head_vi (checked);
  build_8_vi      (C8): NIRODHA_PERSONS, the bhaṅga moment «khoảnh khắc tan rã»;
  labels from build_sample_vi.LABEL.
New here (notes-10-03.md): the person-and-place answers «… tesaṃ / tāsaṃ tattha …» with the attribute beings, and
the answer heads that combine «Sabbesaṃ cavantānaṃ» / «Sabbesaṃ» with attribute beings, moments,
nirodhasamāpannānaṃ and asaññasattānaṃ (head13).

Later Indriya chapters:
    import sys, importlib; sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai")
    Q = importlib.import_module("build_10-03_vi")
    Q.head13() / Q.translate_sentence() / Q.translate_line()

Importing writes nothing; run  python -I -X utf8 -B build_10-03_vi.py  to rebuild the chapter.
"""
import importlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as S  # noqa: E402

F = importlib.import_module("build_2-01_vi")     # family B
P = importlib.import_module("build_10-02_vi")    # Indriya pavattivāra frames
A3 = importlib.import_module("build_3-01_vi")    # mūlaka notes, who3
T5 = importlib.import_module("build_5-01_vi")    # bare Sabbesaṃ, pavatte, head_vi
C8 = importlib.import_module("build_8_vi")       # nirodhasamāpanna, moments

NAME = "10-03-indriyayamaka.md"
cap, low = S.cap, S.low
LABEL = S.LABEL
SLIPS = []

# ================================================================ answer heads
PART = ("upapajjantānaṃ", "upapajjantīnaṃ")
PART_SLIP = {"uppajjantīnaṃ": "upapajjantīnaṃ"}      # ^6-10-206 «Itthīnaṃ ñāṇasampayuttānaṃ uppajjantīnaṃ» (spelling)
SABBE_CAVANTA = F.who("sabbesaṃ cavantānaṃ")[len(F.WHO_HEAD.format(g="")):]   # tất cả những người đang chết đi
SABBESAM = T5.SABBESAM_ALONE                         # bare Sabbesaṃ = tất cả chúng sinh (coordinator)
NIRODHA = C8.NIRODHA_PERSONS                         # nirodhasamāpannānaṃ = những người nhập thành tựu thiền chấm dứt
ASANNA = F.BEINGS["asaññasatta"]                     # asaññasattānaṃ = chúng sinh Vô Tưởng
KHANE = re.compile(r"(?P<mo>uppāda|bhaṅga)kkhaṇe")


def _moment(tok, mo_tok):
    assert tok.endswith("cittassa"), tok
    mm = KHANE.fullmatch(mo_tok)
    assert mm, mo_tok
    return P.moment(tok[:-len("cittassa")], mm["mo"])


def head13(g, ctx=""):
    """Pāli answer head (before the resumptive tesaṃ / tāsaṃ) -> Vietnamese head, capitalised.
    Person groups in a row stand under one «ở» (2-01 WHO_HEAD / LIST_SEP, 5-01 head_vi); a moment (with or without
    pavatte) is its own group; groups are joined with «, »."""
    w = [low(x) for x in g.split()]
    groups, i, n = [], 0, len(w)
    while i < n:
        x = w[i]
        if x == "sabbesaṃ" and i + 1 < n and w[i + 1] == "cavantānaṃ":
            groups.append(("P", SABBE_CAVANTA)); i += 2
        elif x == "sabbesaṃ":
            groups.append(("P", SABBESAM)); i += 1
        elif x == "pavatte":
            assert i + 2 < n, g
            groups.append(("T", P.PAVATTE_JOIN.format(a=P.PAVATTE, b=_moment(w[i + 1], w[i + 2])))); i += 3
        elif x.endswith("cittassa"):
            groups.append(("T", _moment(x, w[i + 1]))); i += 2
        elif x == "nirodhasamāpannānaṃ":
            groups.append(("P", NIRODHA)); i += 1
        elif x == "asaññasattānaṃ":
            groups.append(("P", ASANNA)); i += 1
        else:
            j = i
            while j < n and w[j] not in PART and w[j] not in PART_SLIP:
                j += 1
            assert j < n, (g, ctx)
            toks = w[i:j + 1]
            if toks[-1] in PART_SLIP:
                SLIPS.append((ctx, f"«{toks[-1]}» read as «{PART_SLIP[toks[-1]]}» (spelling)"))
                toks[-1] = PART_SLIP[toks[-1]]
            groups.append(("P", P.attr_group(toks))); i = j + 1
    chunks = []
    for kind, text in groups:
        if kind == "P" and chunks and chunks[-1][0] == "P":
            chunks[-1][1] += F.LIST_SEP + text
        elif kind == "P":
            chunks.append(["P", F.WHO_HEAD.format(g=text)])
        else:
            chunks.append(["T", text])
    return cap(F.LIST_SEP.join(c[1] for c in chunks))


# ================================================================ sentences
FAC_W = P.FAC_W
V = P.V
Q_RE = re.compile(rf"\((?P<l>Ka|Kha)\) (?P<w1>yassa vā pana yattha|yassa yattha|yassa vā pana|yassa) (?P<x>{FAC_W}) "
                  rf"(?P<v1>{V}) (?P<w2>tassa tattha|tassa) (?P<y>{FAC_W}) (?P<v2>{V})")
RES = r"(?P<r>tesaṃ|tāsaṃ)(?P<t> tattha)?"
B_NOT = re.compile(rf"(?P<g>.+?) {RES} (?P<x>{FAC_W}) (?P<v1>{V}), no ca (?P<r2>tesaṃ|tāsaṃ)(?P<t2> tattha)? "
                   rf"(?P<y>{FAC_W}) (?P<v2>{V})")
B_BOTH = re.compile(rf"(?P<g>.+?) {RES} (?P<x>\S+ndriyañca) (?P<v1>{V}) (?P<y>\S+ndriyañca) (?P<v2>{V})")


def translate_sentence(s, ctx=""):
    s = s.strip()
    if s == "Āmantā.":
        return S.AMANTA
    if s == "No.":
        return F.NO
    mm = P.MULAKA_RE.fullmatch(s)
    if mm:
        return A3.MULAKA.format(x=P.FAC[low(mm["s"])])
    punct, body = s[-1], s[:-1]
    assert punct in ".?", s
    if punct == "?":
        mm = Q_RE.fullmatch(body)
        assert mm, (s, ctx)
        kind = mm["w1"].replace(" vā pana", "")
        assert F.DEM_OF[kind] == mm["w2"], s
        kha = "vā pana" in mm["w1"]
        if kha != (mm["l"] == "Kha"):
            SLIPS.append((ctx, f"label ({mm['l']}) on a «{'vā pana' if kha else 'no vā pana'}» question; kept"))
        return F.b_q(kind, P.fm(mm["x"]), F.vparse(mm["v1"], ctx), P.fm(mm["y"]), F.vparse(mm["v2"], ctx),
                     kha=kha, label=mm["l"])
    for rx, both in ((B_NOT, False), (B_BOTH, True)):
        mm = rx.fullmatch(body)
        if not mm:
            continue
        if not both:
            assert mm["r"] == mm["r2"] and bool(mm["t"]) == bool(mm["t2"]), s
        if mm["r"] == "tāsaṃ":
            assert re.search(r"(?:upapajjantīnaṃ|uppajjantīnaṃ)$", mm["g"]), s
        res = "tesaṃ tattha" if mm["t"] else "tesaṃ"
        f = F.b_both if both else F.b_not
        return f(res, head13(mm["g"], ctx), P.fm(mm["x"]), F.vparse(mm["v1"], ctx), P.fm(mm["y"]),
                 F.vparse(mm["v2"], ctx))
    raise ValueError(f"unmatched sentence: {s!r} ({ctx})")


def translate_line(line, ctx=""):
    mm = re.match(r"^(?P<h>#+ )?(?P<t>.*?)(?P<id> \^[0-9A-Za-z-]+)?$", line)
    h, t, sid = mm["h"] or "", mm["t"], mm["id"] or ""
    if h:
        return h + P.heading(t) + sid
    return " ".join(translate_sentence(s, ctx) for s in P.split10(t) if s.strip()) + sid


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
    ("chết đi", 2), ("khoảnh khắc tan rã", 5), ("thành tựu thiền chấm dứt", 5), ("chúng sinh Vô Tưởng", 5),
    ("tất cả chúng sinh", 2), ("người nữ", 2), ("người nam", 2), ("có niềm vui đi kèm", 1),
    ("gắn liền với hiểu biết", 1), ("không có gốc rễ", 1),
]


def check_cross_book():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in S.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts (10-03): {len(CROSS_BOOK)} strings found in pi-1..5 rails")


def check_frames(pali):
    """Every sentence / head that a frame-setter's own parser can translate comes out byte-identical here."""
    n_s = n_h10 = n_t5 = n_a3 = 0
    probs = []
    for ln in pali.splitlines():
        if not ln.strip() or ln.startswith("#"):
            continue
        t = re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", ln)
        for s in P.split10(t):
            s = s.strip()
            if not s:
                continue
            mine = translate_sentence(s, "check")
            try:
                theirs = P.translate_sentence(s, "check")
            except (AssertionError, ValueError, KeyError):
                theirs = None
            if theirs is not None:
                n_s += 1
                if theirs != mine:
                    probs.append(f"differs from 10-02 parser: {s[:70]}")
            mm = B_NOT.fullmatch(s[:-1]) or B_BOTH.fullmatch(s[:-1])
            if not mm:
                continue
            g = mm["g"]
            h = head13(g, "check")
            for fn, tag in ((P.head10, "h10"), (T5.head_vi, "t5"), (A3.who3, "a3")):
                try:
                    o = fn(g)
                except (AssertionError, ValueError, KeyError):
                    continue
                o = cap(o)
                if tag == "h10":
                    n_h10 += 1
                elif tag == "t5":
                    n_t5 += 1
                else:
                    if not any(x in A3.ATTR for x in [low(y) for y in g.split()]):
                        continue
                    n_a3 += 1
                if o != h:
                    probs.append(f"head differs from {tag}: {g} | {o} | {h}")
    del P.SLIPS[:]
    print(f"frame checks: {n_s} sentences vs 10-02 parser, heads vs head10 {n_h10}, vs 5-01 head_vi {n_t5}, "
          f"vs 3-01 who3 {n_a3}")
    assert S.LABEL["Ka"] == "(a)" and S.LABEL["Kha"] == "(b)"
    assert head13("Sabbesaṃ cittassa bhaṅgakkhaṇe nirodhasamāpannānaṃ asaññasattānaṃ") == \
        cap(T5.head_vi("Sabbesaṃ cittassa bhaṅgakkhaṇe nirodhasamāpannānaṃ asaññasattānaṃ"))
    return probs


def main():
    S.check_cross_book()
    F.check_cross_book()
    P.check_cross_book()
    check_cross_book()
    del SLIPS[:]
    pali = (S.PALI_DIR / NAME).read_text(encoding="utf-8")
    fprobs = check_frames(pali)
    del SLIPS[:]
    text = unicodedata.normalize("NFC", translate_file())
    probs = S.check_lines(pali, text, NAME) + fprobs
    for i, ln in enumerate(text.splitlines(), 1):
        body = re.sub(r" ?\[[^\]]*\]", "", re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", ln))
        for bad in ("uppajj", "upapajj", "tesaṃ", "tāsaṃ", "tattha", "mūlakaṃ", "vinā", "kkhaṇe", "thì thì",
                    "là không phải", "là là", "  ", "ndriy", "sabbesaṃ", "Sabbesaṃ", "ānaṃ"):
            if bad in body:
                probs.append(f"line {i}: «{bad}»")
    with open(S.OUT_DIR / NAME, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    segs = len(re.findall(r"\^[0-9A-Za-z-]+\s*$", text, flags=re.M))
    print(f"wrote {NAME}: {len([x for x in text.splitlines() if x.strip()])} lines, {segs} segments")
    seen = set()
    for c, w in SLIPS + F.SLIPS:
        if (c, w) not in seen:
            seen.add((c, w))
            print("SLIP", c, "|", w)
    for p in probs[:80]:
        print("PROBLEM", p)
    print("line checks:", "OK" if not probs else f"{len(probs)} problems")
    sys.exit(1 if probs else 0)


if __name__ == "__main__":
    main()
