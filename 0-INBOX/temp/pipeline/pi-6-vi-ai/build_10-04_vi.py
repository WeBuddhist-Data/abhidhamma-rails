# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 10-04-indriyayamaka.md (Indriyayamaka, pavattivāra, uppādavāra (1)
paccuppannavāra: (Ṅa) paccanīkaokāso and (Ca) paccanīkapuggalokāsā).

Frames, imported and used VERBATIM:
  build_10-02_vi  (P): ATTR10 / attr_group() (the attribute beings itthīnaṃ / somanassena / sahetukānaṃ …),
                  citta_kind() / moment(), PAVATTE, fm(), run_vi(), split10(), translate_sentence() (every yattha
                  question and place answer, Āmantā, mūlaka notes, «Āmantā …pe….»), heading();
  build_2-01_vi   (F): family B (b_q with kind «yassa yattha», b_not / b_both with res «tesaṃ tattha», b_short,
                  vparse, who(), WHO_HEAD, LIST_SEP, NATTHI);
  build_3-01_vi   (A3): who3() (asserted equal for the 3-01 attribute heads);
  build_9-01_vi   (D9): SABBE «tất cả chúng sinh» (bare sabbesaṃ before cittassa …), the element-by-element
                  head rule (consecutive persons share one «ở», a time phrase stands alone, joined «, »);
  build_8_vi      (C8): when() for «cittassa bhaṅgakkhaṇe»;
  labels from build_sample_vi.LABEL.
New here (notes-10-04.md): the mixed heads of the puggalokāsa answers (head4()).

Importing writes nothing; run  python -I -X utf8 -B build_10-04_vi.py  to rebuild the chapter.
"""
import importlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as S  # noqa: E402

F = importlib.import_module("build_2-01_vi")     # families A / B
I = importlib.import_module("build_10-01_vi")    # Indriya faculty table
P = importlib.import_module("build_10-02_vi")    # Indriya pavatti frames (attributes, citta kinds, sentences)
A3 = importlib.import_module("build_3-01_vi")    # who3 (attribute heads)
D9 = importlib.import_module("build_9-01_vi")    # SABBE, element head rule
C8 = importlib.import_module("build_8_vi")       # moments

NAME = "10-04-indriyayamaka.md"
cap, low = S.cap, S.low
LABEL = S.LABEL
SLIPS = []
OI = D9.OI                                        # «ở » before a run of persons (2-01 WHO_HEAD)
assert F.WHO_HEAD.format(g="") == OI


def _strip_o(s):
    assert s.startswith(OI), s
    return s[len(OI):]


# ================================================================ answer heads (head4)
PART_RE = r"upapajjantānaṃ|upapajjantīnaṃ"
ATTR_KEYS = sorted(P.ATTR10, key=len, reverse=True)
ATTR_RE = "|".join(re.escape(k) for k in ATTR_KEYS)
ELEMENTS = [
    (rf"sabbesaṃ (?:upapajjantānaṃ|cavantānaṃ)", "P", lambda m: _strip_o(F.who(m[0]))),          # 2-01
    (rf"(?:(?:{ATTR_RE}) )+(?:{PART_RE})", "P", lambda m: P.attr_group(_tokens(m[0]))),        # 10-02
    (r"asaññasattānaṃ", "P", lambda m: _strip_o(F.who(m[0]))),                                  # 2-01 chúng sinh Vô Tưởng
    (r"sabbesaṃ", "P", lambda m: D9.SABBE),                                                     # 9-01 / coordinator
    (r"pavatte", "T", lambda m: P.PAVATTE),                                                     # coordinator / 9-01
    (r"(?P<k>\S*?)cittassa (?P<m>uppāda|bhaṅga)kkhaṇe", "T", lambda m: P.moment(m["k"], m["m"])),  # 10-02 / 8
]
ELEMENTS = [(re.compile(p + r"(?= |$)"), k, f) for p, k, f in ELEMENTS]


def _tokens(s):
    """«vinā somanassena sacakkhukānaṃ upapajjantānaṃ» -> attribute tokens as 10-02 attr_group takes them."""
    return s.split()


def head4(g):
    """Pāli answer head (before tesaṃ / tāsaṃ tattha) -> Vietnamese head, capitalised (9-01 who9 rule)."""
    p, i, out, prev_p = low(g), 0, [], False
    while i < len(p):
        for rx, kind, fn in ELEMENTS:
            mm = rx.match(p, i)
            if mm:
                vi = fn(mm)
                if kind == "P" and not prev_p:
                    vi = OI + vi
                out.append(vi)
                prev_p = kind == "P"
                i = mm.end() + 1
                break
        else:
            raise ValueError(f"unparsed head {g!r} at {p[i:]!r}")
    return cap(F.LIST_SEP.join(out))


# ================================================================ sentences
V = P.V
FAC_W = P.FAC_W
RUN = P.RUN
Q4_RE = re.compile(rf"(?:\((?P<l>Ka|Kha)\) )?(?P<w1>[Yy]assa vā pana yattha|[Yy]assa yattha) (?P<x>{FAC_W}) "
                   rf"(?P<v1>{V}) (?P<w2>tassa tattha) (?P<y>{RUN}) (?P<v2>{V})")
RES4 = r"(?P<r>tesaṃ|tāsaṃ) tattha"
P4_NOT = re.compile(rf"(?P<g>.+?) {RES4} (?P<x>{FAC_W}) (?P<v1>{V}), no ca (?P<r2>tesaṃ|tāsaṃ) tattha (?P<y>{FAC_W}) "
                    rf"(?P<v2>{V})")
P4_BOTH = re.compile(rf"(?P<g>.+?) {RES4} (?P<x>\S+ndriyañca) (?P<v1>{V}) (?P<y>\S+ndriyañca) (?P<v2>{V})")
SHORT_RE = re.compile(r"(?P<b>Uppajj|Nirujjh)(?P<t>ati|ittha|issati)\.")
EXACT_SENT = {"Natthi.": F.NATTHI}


def translate_sentence(s, ctx=""):
    s = s.strip()
    if s in EXACT_SENT:
        return EXACT_SENT[s]
    mm = SHORT_RE.fullmatch(s)
    if mm:                                                              # Uppajjati. = Có sinh khởi. (2-01)
        return F.b_short(F.VERB_BASE[low(mm["b"])], F.TENSE_OF[mm["t"]])
    punct, body = s[-1], s[:-1]
    if punct == "?":
        mm = Q4_RE.fullmatch(body)
        if mm:
            kind = low(mm["w1"]).replace(" vā pana", "")
            assert F.DEM_OF[kind] == mm["w2"], s
            kha = "vā pana" in mm["w1"]
            if mm["l"] and kha != (mm["l"] == "Kha"):
                SLIPS.append((ctx, f"label ({mm['l']}) on a «{'vā pana' if kha else 'no vā pana'}» question; kept"))
            y = P.run_vi(mm["y"]) if "…pe…" in mm["y"] else P.fm(mm["y"])
            out = F.b_q(kind, P.fm(mm["x"]), F.vparse(mm["v1"], ctx), y, F.vparse(mm["v2"], ctx), kha=kha,
                        label=mm["l"])
            if not mm["l"] and body[:1].islower():
                out = low(out)
            return out
    if punct == ".":
        for rx, both in ((P4_NOT, False), (P4_BOTH, True)):
            mm = rx.fullmatch(body)
            if not mm:
                continue
            if not both:
                assert mm["r"] == mm["r2"], s
            if mm["r"] == "tāsaṃ":
                assert "upapajjantīnaṃ" in mm["g"], s
            f = F.b_both if both else F.b_not
            return f("tesaṃ tattha", head4(mm["g"]), P.fm(mm["x"]), F.vparse(mm["v1"], ctx), P.fm(mm["y"]),
                     F.vparse(mm["v2"], ctx))
    return P.translate_sentence(s, ctx)                                 # yattha frames, Āmantā, mūlaka … (10-02)


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
    ("Không có.", 3), ("chết đi", 2), ("không có gốc rễ", 1), ("không gắn liền với hiểu biết", 1),
]


def check_cross_book():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in S.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts (10-04): {len(CROSS_BOOK)} strings found in pi-1..5 rails")


def check_frames():
    """Frames shared with the frame-setters stay byte-identical."""
    for g in ("Acakkhukānaṃ sasotakānaṃ upapajjantānaṃ", "Sabbesaṃ cavantānaṃ acakkhukānaṃ asotakānaṃ upapajjantānaṃ",
              "Sabbesaṃ cavantānaṃ acittakānaṃ upapajjantānaṃ", "Acittakānaṃ upapajjantānaṃ"):
        assert head4(g) == cap(A3.who3(g)), (head4(g), A3.who3(g))
    assert head4("Sabbesaṃ cavantānaṃ") == cap(F.who("Sabbesaṃ cavantānaṃ"))
    assert head4("Itthīnaṃ upapajjantīnaṃ") == P.head10("Itthīnaṃ upapajjantīnaṃ")
    g = "Vinā somanassena upapajjantānaṃ pavatte somanassavippayuttacittassa uppādakkhaṇe"
    assert head4(g) == P.head10(g), (head4(g), P.head10(g))
    g = "Pavatte saddhāvippayuttasomanassasampayuttacittassa uppādakkhaṇe"
    assert head4(g) == P.head10(g), (head4(g), P.head10(g))
    assert P.moment("", "bhaṅga") == C8.when("bhaṅga")
    assert D9.who9("Sabbesaṃ cittassa bhaṅgakkhaṇe asaññasattānaṃ") == \
        low(head4("Sabbesaṃ cittassa bhaṅgakkhaṇe asaññasattānaṃ"))
    assert D9.PAVATTE == P.PAVATTE
    assert S.LABEL["Ka"] == "(a)" and S.LABEL["Kha"] == "(b)" and S.LABEL["Ca"] == "(e)"


def check_parallel(pali):
    """Every sentence of this chapter that the 10-02 or 10-03 parser (same yamaka, same frames) can translate, and
    every answer head that 10-03 head13 / 10-02 head10 / 3-01 who3 can translate, comes out byte-identical here."""
    try:
        Q = importlib.import_module("build_10-03_vi")
    except Exception as e:                            # noqa: BLE001
        print("note: build_10-03_vi not importable:", e)
        Q = None
    probs, n = [], {"10-02": 0, "10-03": 0, "head13": 0, "head10": 0, "who3": 0}
    for ln in pali.splitlines():
        if not ln.strip() or ln.startswith("#"):
            continue
        t = re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", ln)
        for s in P.split10(t):
            s = s.strip()
            if not s:
                continue
            mine = translate_sentence(s, "check")
            for tag, mod in (("10-02", P), ("10-03", Q)):
                if mod is None:
                    continue
                try:
                    theirs = mod.translate_sentence(s, "check")
                except (AssertionError, ValueError, KeyError, TypeError):
                    continue
                n[tag] += 1
                if theirs != mine:
                    probs.append(f"differs from {tag}: {s[:70]} | {theirs} | {mine}")
            mm = P4_NOT.fullmatch(s[:-1]) or P4_BOTH.fullmatch(s[:-1])
            if not mm:
                continue
            g, h = mm["g"], head4(mm["g"])
            fns = [("head10", P.head10), ("who3", A3.who3)] + ([("head13", Q.head13)] if Q else [])
            for tag, fn in fns:
                try:
                    o = cap(fn(g))
                except (AssertionError, ValueError, KeyError, TypeError):
                    continue
                if tag == "who3" and not any(x in A3.ATTR for x in low(g).split()):
                    continue
                n[tag] += 1
                if o != h:
                    probs.append(f"head differs from {tag}: {g} | {o} | {h}")
    del P.SLIPS[:]
    if Q is not None:
        del Q.SLIPS[:]
    print("parallel checks:", ", ".join(f"{k} {v}" for k, v in n.items()))
    return probs


def check_same_as_other(text, pali):
    """Every Pāli line of this chapter that also occurs in a finished Indriya chapter has the same Vietnamese."""
    strip = lambda x: re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", x)          # noqa: E731
    probs, warn = [], []
    for nm in ("10-01-indriyayamaka.md", "10-02-indriyayamaka.md", "10-03-indriyayamaka.md"):
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
                    (warn if nm.startswith("10-03") else probs).append(f"differs from {nm}: {p[:70]}")
        print(f"lines shared with {nm} checked: {n}")
    for w in warn:
        print("WARN", w)
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
    del SLIPS[:]
    del P.SLIPS[:]
    del F.SLIPS[:]
    text = unicodedata.normalize("NFC", translate_file())
    probs = (S.check_lines(pali, text, NAME) + I.check_extra(text, pali) + check_same_as_other(text, pali)
             + pprobs)
    for i, ln in enumerate(text.splitlines(), 1):
        body = re.sub(r" ?\[[^\]]*\]", "", re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", ln))
        for bad in ("uppajj", "upapajj", "tesaṃ", "tāsaṃ", "tattha", "mūlakaṃ", "vinā", "kkhaṇe", "thì thì",
                    "là không phải", "ndriya", "sabbesaṃ", "Sabbesaṃ", "….", "  ", "là là", "ānaṃ", "Āmantā"):
            if bad in body:
                probs.append(f"line {i}: «{bad}»")
    with open(S.OUT_DIR / NAME, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    segs = len(re.findall(r"\^[0-9A-Za-z-]+\s*$", text, flags=re.M))
    print(f"wrote {NAME}: {len([x for x in text.splitlines() if x.strip()])} lines, {segs} segments")
    seen = set()
    for c, w in SLIPS + P.SLIPS + F.SLIPS:
        if (c, w) not in seen:
            seen.add((c, w))
            print("SLIP", c, "|", w)
    for p in probs[:80]:
        print("PROBLEM", p)
    print("line checks:", "OK" if not probs else f"{len(probs)} problems")
    sys.exit(1 if probs else 0)


if __name__ == "__main__":
    main()
