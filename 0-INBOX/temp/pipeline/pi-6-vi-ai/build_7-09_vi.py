# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 7-09-anusayayamaka.md (Pahīnavāro: anuloma pahīno, paṭiloma appahīno).

Every frame comes VERBATIM from the family-C frame-setter build_7-01_vi (imported, nothing redefined): question()
(yassa / yattha / yassa yattha), statement(), tl(), VERB["pahīno" / "pahīnā" / "appahīno" / "appahīnā"]
(«đã được dứt bỏ» / «chưa được dứt bỏ», no ca … = the denial), NA_VATTABBO, PERSON_VI, PLACE_VI, RES_VI, BUT_C,
BOTH_C, SIMPLE_C, headings, MULAKA, VARE_DIR. «Āmantā …pe….» and «<statement> …pe….» as in 7-02 / 7-04.
New here (listed in notes-7-09.md):

    X na vattabbo "pahīno"ti vā "appahīno"ti vā   = X không nên nói là “đã được dứt bỏ” hay “chưa được dứt bỏ”   (7-01 proposal)
    X ca Y ca na vattabbā "pahīnā"ti vā "appahīnā"ti vā = same frame with the tl() list
    Na vattabbo / Na vattabbā "…"ti vā "…"ti vā.  = Không nên nói là “đã được dứt bỏ” hay “chưa được dứt bỏ”.
    <head> <clause 1>; <clause 2>; …               = <head>, thì <res> <clause 1>; <clause 2>; ….   (semicolons kept)
    A ca V; B ca V (^6-7-306)                       = A V; đồng thời B cũng V   (BOTH_C with the Pāli semicolon)
    A ca V, B ca V (^6-7-307)                       = A V, đồng thời B cũng V   (= BOTH_C)
    [pahīno (sī. ka.) anusayavārena pana na sameti] = [dị bản (Sī., Ka.): pahīno; nhưng không phù hợp với mục về
                                                      khuynh hướng tiềm ẩn]   (pi-4 «pana sameti» = «nhưng phù hợp với»)

DASH RULE: no dash in the Pāli of this chapter; the frames add none. Quotes: the Pāli "pahīno"ti -> “…” (outer).
Importing writes nothing; run  python -I -X utf8 -B build_7-09_vi.py  to rebuild the chapter file.
"""
import importlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as B  # noqa: E402

A = importlib.import_module("build_7-01_vi")   # family C frames (7-01)
P2 = importlib.import_module("build_7-02_vi")  # «…pe…» shortenings (7-02), cross-check only + AMANTA_PE

CH = "7-09-anusayayamaka.md"
cap, low, tl = B.cap, B.low, A.tl
PE = A.PE                                       # …pe… = …
SLIPS = []

# ================================================================ na vattabbo (7-01 proposal NA_VATTABBO, used verbatim)
NA_VATTABBO = A.NA_VATTABBO                     # "{a} không nên nói là “đã được dứt bỏ” hay “chưa được dứt bỏ”"
NA_BARE = cap(NA_VATTABBO.format(a="").lstrip())   # Na vattabbo "pahīno"ti vā "appahīno"ti vā (no subject)
NA_RE = re.compile(r'(?:(?P<a>.+?) )?(?P<n>[Nn]a) vattabb(?P<e1>[oā]) "pahīn(?P<e2>[oā])"ti vā "appahīn(?P<e3>[oā])"ti vā')

# ================================================================ the variant bracket of ^6-7-270
VAR_PALI = "[pahīno (sī. ka.) anusayavārena pana na sameti]"
VAR_VI = f"[{B.VAR} (Sī., Ka.): pahīno; nhưng không phù hợp với {low(A.SECTION['Anusayavāra'])}]"
# pi-4 «[patigaṇhāti (sī.) rūpasiddhiṭīkāya pana sameti]» = «[khác chính tả (Sī.): patigaṇhāti; nhưng phù hợp với …]»
# pi-2 «[āsavā (sī.) dhātuvibhaṅge pana …]» = «[dị bản (Sī.): āsavā; nhưng trong …]»; pahīno / pahīnā is a form
# (number) variant, so «dị bản» (sample rule for -ā / -aṃ).

# ================================================================ «A ca V; B ca V» / «A ca V, B ca V»
BOTH_SEMI_RE = re.compile(rf"(?P<a>.+? ca) (?P<va>{A.V_RE}); (?P<b>.+? ca) (?P<vb>{A.V_RE})")
BOTH_COMMA_RE = re.compile(rf"(?P<a>.+? ca) (?P<va>{A.V_RE}), (?P<b>.+? ca) (?P<vb>{A.V_RE})")
BOTH_SEMI_C = A.BOTH_C.replace(", đồng thời", "; đồng thời")   # BOTH_C with the Pāli semicolon at the joint
assert BOTH_SEMI_C != A.BOTH_C


def both(m):
    return A.BOTH_C.format(a=tl(m["a"]), p=A.verb(m["va"])["p"], b=tl(m["b"]), p2=A.verb(m["vb"])["p"])


def clause(body, s):
    """One clause of a statement (no subject head): na vattabbo, or 7-01's BUT / BOTH / SIMPLE clause."""
    m = NA_RE.fullmatch(body)
    if m:
        assert m["a"] and m["n"] == "na", s
        assert m["e1"] == m["e2"] == m["e3"], s            # vattabbo / pahīno, vattabbā / pahīnā agree
        if m["e1"] == "ā":
            assert " ca" in m["a"], s                          # plural only with a «ca» list
        return NA_VATTABBO.format(a=tl(m["a"]))
    for rx, kind in ((A.BUT_RE, "but"), (A.BOTH_RE, "both"), (A.SIMPLE_RE, "simple")):
        b = rx.fullmatch(body)
        if b:
            break
    else:
        raise ValueError(f"unparsed clause {body!r} in {s!r}")
    if kind == "but":
        return A.BUT_C.format(a=tl(b["a"]), p=A.verb(b["va"])["p"], dem=A.NO_CA_VI[b["dem"]], b=tl(b["b"]),
                              no=A.verb(b["vb"])["no"])
    if kind == "both":
        return both(b)
    return A.SIMPLE_C.format(a=tl(b["a"]), p=A.verb(b["va"])["p"])


def parse_statement(s):
    """7-01 parse_statement, extended: clauses joined by «; », na vattabbo clauses, «A ca V; / , B ca V»."""
    assert s.endswith(".") and not s.endswith(".."), s
    m = NA_RE.fullmatch(s[:-1])
    if m and not m["a"]:
        assert m["n"] == "Na" and m["e1"] == m["e2"] == m["e3"], s
        return NA_BARE + "."
    m = A.SUBJ_RE.fullmatch(s.rstrip("."))
    per = m["per"]
    if per:
        per = next(k for k in A.PERSON_VI if k.lower() == per.lower())
    pl_txt = (m["pl"] or "").strip()
    places = []
    while pl_txt:
        hit = re.match(rf"({A.PLACE_RE})(?: |$)", A.lower1(pl_txt))
        if not hit:
            raise ValueError(f"unparsed places in {s!r}")
        places.append(hit.group(1))
        pl_txt = pl_txt[hit.end():].strip()
    body = m["body"]
    if not (per or places or m["res"]):
        body = A.lower1(body)                            # «Mānānusayo pahīno; …» (no subject head)
    simple_body = "no ca" not in body and "vattabb" not in body
    b = BOTH_SEMI_RE.fullmatch(body) if simple_body else None
    if b:
        SLIPS.append("semicolon inside «A ca … B ca …» (kept): " + s[:70])
        cl = BOTH_SEMI_C.format(a=tl(b["a"]), p=A.verb(b["va"])["p"], b=tl(b["b"]), p2=A.verb(b["vb"])["p"])
    else:
        b = BOTH_COMMA_RE.fullmatch(body) if simple_body else None
        if b:
            SLIPS.append("comma inside «A ca … B ca …» (= the usual frame): " + s[:70])
            cl = both(b)
        else:
            cl = "; ".join(clause(c, s) for c in body.split("; "))
    return A.statement(per, places, m["res"], cl)


# ================================================================ sentences and lines
PE_END_RE = re.compile(r"(?P<base>.+?) ?…pe…\.")      # «<statement> …pe….» (7-02 / 7-04 rule)


def translate_sentence(s):
    if s == "Āmantā …pe….":
        return P2.AMANTA_PE                              # Đúng vậy… (7-02 / 7-04)
    m = PE_END_RE.fullmatch(s)
    if m:
        v = parse_statement(m["base"] + ".")
        assert v.endswith("."), v
        return v[:-1] + PE                               # «….» is never written
    if A.Q_RE.fullmatch(s) or s in ("Āmantā.", "Natthi.", "No.") or A.MULAKA_RE.fullmatch(s) \
            or re.fullmatch(r"\w+vāre (?:anulomaṃ|paṭilomaṃ)\.", s):
        return A.translate_sentence(s)                   # questions, short answers, (…mūlakaṃ), <X>vāre anulomaṃ.
    return parse_statement(s)


def translate_line(line):
    m = re.match(r"^(?P<h>#+ )?(?P<t>.*?)(?P<id> \^[0-9A-Za-z-]+)?$", line)
    h, t, sid = m["h"] or "", m["t"], m["id"] or ""
    if h:
        return h + A.heading(t) + sid
    var = VAR_PALI in t
    if var:                                              # the bracket holds «sī. ka.»: take it out before splitting
        t = t.replace(" " + VAR_PALI, "")
    sents = A.SPLIT_RE.split(t)
    out = [translate_sentence(s) for s in sents]
    if var:
        # the bracket follows the first verb of the (Ka) question: «… pahīnā [ … ] tassa …»
        assert sents[0].startswith("(Ka) yassa kāmarāgānusayo ca paṭighānusayo ca pahīnā tassa"), sents[0]
        assert out[0].count(", thì ") == 1, out[0]
        out[0] = out[0].replace(", thì ", f" {VAR_VI}, thì ")
    return " ".join(out) + sid


def translate_file(name):
    src = (B.PALI_DIR / name).read_text(encoding="utf-8")
    out = [translate_line(line) if line.strip() else "" for line in src.splitlines()]
    text = "\n".join(out).rstrip("\n") + "\n"
    return re.sub(r"\n{3,}", "\n\n", text)


# ================================================================ checks
CROSS_BOOK = [
    ("không nên nói", 1), ("không nên nói", 2), ("nhưng phù hợp với", 4), ("phù hợp với", 4),
    ("đã được dứt bỏ", 5), ("chưa được dứt bỏ", 5), ("bậc A-la-hán", 5), ("bậc không trở lại", 4),
    ("người phàm phu", 4), ("hai hạng người", 4), ("ba hạng người", 4), ("nơi cảm giác khó chịu", 5),
    ("trong cõi dục lạc", 2), ("trong cõi hình sắc", 2), ("trong cõi không hình sắc", 2),
    ("Không có.", 3), ("Đúng vậy.", 5), ("dị bản", 1),
]


def check_cross_book():
    A.check_cross_book()
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in B.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts (7-09): {len(CROSS_BOOK)} strings found in pi-1..5 rails")


def sentences(pali):
    for p in pali.splitlines():
        if not p.strip() or p.startswith("#"):
            continue
        p = re.sub(r"\s*\^[\w-]+$", "", p).replace(" " + VAR_PALI, "")
        yield from A.SPLIT_RE.split(p)


def check_repeats(pali):
    """Identical Pāli sentence -> identical Vietnamese sentence (within the chapter)."""
    seen, bad = {}, 0
    for s in sentences(pali):
        t = translate_sentence(s)
        if seen.setdefault(s, t) != t:
            print("REPEAT MISMATCH", s)
            bad += 1
    return bad


def check_vs_7_02_parser(pali):
    """Where the 7-02 parser (7-01 frames + its …pe… rules) also handles a sentence, the Vietnamese is identical."""
    same = 0
    for s in set(sentences(pali)):
        try:
            v2 = P2.translate_sentence(s)
        except Exception:            # na vattabbo / semicolon sentences: not covered by 7-01 / 7-02
            continue
        assert v2 == translate_sentence(s), f"differs from the 7-02 parser: {s!r}"
        same += 1
    return same


def check_vs_finished(pali_lines, vi_lines):
    """Identical Pāli lines in the finished anusaya chapters 7-01 … 7-06 -> identical Vietnamese lines."""
    strip = lambda ln: re.sub(r"\s*\^[\w-]+$", "", ln)      # noqa: E731
    known = {}
    for n in range(1, 7):
        ch = f"7-0{n}-anusayayamaka.md"
        pl = [ln for ln in (B.PALI_DIR / ch).read_text(encoding="utf-8").splitlines() if ln.strip()]
        vl = [ln for ln in (B.OUT_DIR / ch).read_text(encoding="utf-8").splitlines() if ln.strip()]
        assert len(pl) == len(vl), ch
        for p, v in zip(pl, vl):
            known.setdefault(strip(p), set()).add(strip(v))
    hits = 0
    for p, v in zip(pali_lines, vi_lines):
        k = strip(p)
        if k in known:
            assert known[k] == {strip(v)}, f"differs from a finished chapter: {p!r}"
            hits += 1
    return hits


def main():
    check_cross_book()
    SLIPS.clear()
    A.SLIPS.clear()
    text = unicodedata.normalize("NFC", translate_file(CH))
    pali = (B.PALI_DIR / CH).read_text(encoding="utf-8")
    probs = B.check_lines(pali, text, CH)
    assert check_repeats(pali) == 0, "identical Pāli rendered differently"
    n2 = check_vs_7_02_parser(pali)
    pl = [ln for ln in pali.splitlines() if ln.strip()]
    vl = [ln for ln in text.splitlines() if ln.strip()]
    nf = check_vs_finished(pl, vl)
    for bad in ("….", ".…", "?…", ",…", "  ", "là là", '"', "—", "–"):
        assert bad not in text, bad
    assert text.count("“") == text.count("”") and "‘" not in text
    with open(B.OUT_DIR / CH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    segs = len(re.findall(r"\^[0-9A-Za-z-]+\s*$", text, flags=re.M))
    print(f"wrote {CH}: {len(vl)} lines, {segs} segments")
    print(f"sentences identical with the 7-02 parser: {n2}; lines identical with finished 7-01 … 7-06: {nf}")
    print("source notes:")
    for s in sorted(set(SLIPS + A.SLIPS)):
        print("  ", s)
    for p in probs[:80]:
        print("PROBLEM", p)
    print("line checks:", "OK" if not probs else f"{len(probs)} problems")
    sys.exit(1 if probs else 0)


if __name__ == "__main__":
    main()
