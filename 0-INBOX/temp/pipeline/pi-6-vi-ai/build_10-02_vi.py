# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 10-02-indriyayamaka.md (Indriyayamaka: the rest of the paṇṇattivāra
niddesa, suddhindriyamūlacakka; pavattivāra, uppādavāra (1) paccuppannavāra, anulomapuggalo and anulomaokāso).

Frames, imported and used VERBATIM:
  build_10-01_vi  (I): the faculty table (FACULTY_VI, BARE_VI, m()), and translate_line() for every paṇṇatti line;
  build_2-01_vi   (F): family A / B (b_q, b_not, b_both, vparse, WHO_HEAD, LIST_SEP, PARTICIPLE, PLACE_IN, NO, …);
  build_3-01_vi   (A3): the attribute beings (ATTR, ATTR_JOIN, ATTR_GROUP: «những người đang tái sinh có mắt và
                  không có tai»), where3() (multi-plane place answers), _run() («…pe…» runs inside one question),
                  MULAKA «(Phần dựa trên …)»;
  build_8_vi      (C8): the moments (AT, OF, MOMENT: «vào khoảnh khắc sinh khởi của tâm»);
  build_5-01_vi   (T5): pavatte (PAVATTE, PAVATTE_JOIN: «trong quá trình diễn tiến vào khoảnh khắc …»);
  labels from build_sample_vi.LABEL.
New here (listed in notes-10-02.md): the faculty-specific attributes of the beings (itthīnaṃ / na itthīnaṃ,
purisānaṃ, somanassena / vinā somanassena, upekkhāya / vinā upekkhāya, sahetukānaṃ / ahetukānaṃ,
ñāṇasampayuttānaṃ / ñāṇavippayuttānaṃ), the feminine upapajjantīnaṃ / tāsaṃ, and the citta kinds
«somanassasampayuttasaddhāvippayuttacittassa …».

Later Indriya chapters:
    import sys, importlib; sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai")
    P = importlib.import_module("build_10-02_vi")
    P.ATTR10 / P.attr_group() / P.citta_kind() / P.head10() / P.translate_sentence() / P.translate_line()

Importing writes nothing; run  python -I -X utf8 -B build_10-02_vi.py  to rebuild the chapter.
"""
import importlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as S  # noqa: E402

F = importlib.import_module("build_2-01_vi")     # families A / B
I = importlib.import_module("build_10-01_vi")    # Indriya faculty table + paṇṇatti lines
A3 = importlib.import_module("build_3-01_vi")    # attribute beings, multi-plane places, «…pe…» runs, mūlaka notes
C8 = importlib.import_module("build_8_vi")       # moments
T5 = importlib.import_module("build_5-01_vi")    # pavatte

NAME = "10-02-indriyayamaka.md"
cap, low = S.cap, S.low
LABEL = S.LABEL
SLIPS = []

# ================================================================ members
FAC = I.FACULTY_VI                                # "cakkhundriya" -> "năng lực mắt"
BARE = I.BARE_VI                                  # "itthī" -> "người nữ" …


def fm(w):
    """cakkhundriyaṃ / cakkhundriyañca -> «năng lực mắt»."""
    w = low(w)
    if w.endswith("ñca"):
        w = w[:-3] + "ṃ"
    assert w.endswith("ndriyaṃ") and w[:-1] in FAC, w
    return FAC[w[:-1]]


# ================================================================ beings: attributes (3-01 ATTR + new)
SAHAGATA = "có {x} đi kèm"                        # somanassena / upekkhāya (pi-1 somanassasahagata «có niềm vui đi kèm»)
SAHAGATA_NEG = "không có {x} đi kèm"              # vinā somanassena / vinā upekkhāya (vinā «không có», 6-01 VINA)
SAMPAYUTTA = "gắn liền với {x}"                   # ñāṇasampayutta (pi-1 «gắn liền với hiểu biết»)
VIPPAYUTTA = "không gắn liền với {x}"             # ñāṇavippayutta (pi-1 «không gắn liền với hiểu biết»)
NANA = "hiểu biết"                                # ñāṇa in these compounds (pi-1)
ATTR10 = dict(A3.ATTR)
ATTR10.update({
    "itthīnaṃ": F.a_is(BARE["itthī"]), "na itthīnaṃ": F.a_not(BARE["itthī"]),        # là người nữ / không phải là …
    "purisānaṃ": F.a_is(BARE["puriso"]), "na purisānaṃ": F.a_not(BARE["puriso"]),   # là người nam / không phải là …
    "somanassena": SAHAGATA.format(x=BARE["somanassaṃ"]),
    "vinā somanassena": SAHAGATA_NEG.format(x=BARE["somanassaṃ"]),
    "upekkhāya": SAHAGATA.format(x=BARE["upekkhā"]),
    "vinā upekkhāya": SAHAGATA_NEG.format(x=BARE["upekkhā"]),
    "sahetukānaṃ": "có gốc rễ", "ahetukānaṃ": "không có gốc rễ",                     # coordinator; sample SAHETUKA
    "ñāṇasampayuttānaṃ": SAMPAYUTTA.format(x=NANA), "ñāṇavippayuttānaṃ": VIPPAYUTTA.format(x=NANA),
})
PARTICIPLE10 = {"upapajjantānaṃ": "upapajjantānaṃ", "upapajjantīnaṃ": "upapajjantānaṃ"}   # feminine = same Vietnamese


def attr_group(tokens):
    """[attr…, participle] -> «những người đang tái sinh có mắt và là người nữ» (3-01 ATTR_GROUP / ATTR_JOIN)."""
    attrs, i = [], 0
    while i < len(tokens) - 1:
        two = " ".join(tokens[i:i + 2])
        if two in ATTR10:
            attrs.append(ATTR10[two]); i += 2
        elif tokens[i] in ATTR10:
            attrs.append(ATTR10[tokens[i]]); i += 1
        else:
            raise ValueError(f"unknown attribute {tokens[i:]!r}")
    assert i == len(tokens) - 1 and tokens[i] in PARTICIPLE10, tokens
    vi = F.PARTICIPLE[PARTICIPLE10[tokens[i]]][0]
    assert attrs, tokens
    return A3.ATTR_GROUP.format(h=F.HEAD[None], p=vi, a=A3.ATTR_JOIN.join(attrs))


# ================================================================ citta kinds and moments
KIND_NOUN = {"somanassa": BARE["somanassaṃ"], "upekkhā": BARE["upekkhā"], "saddhā": BARE["saddhā"], "ñāṇa": NANA}
KIND_PART = re.compile(r"(somanassa|upekkhā|saddhā|ñāṇa)(sampayutta|vippayutta)")
CITTA = "tâm"                                     # citta (core)
KIND_JOIN = " và "                                # 5-01 «tâm không gắn liền với khao khát và không gắn liền với …»


def citta_kind(k):
    """somanassasampayuttasaddhāvippayutta -> «tâm gắn liền với niềm vui và không gắn liền với niềm tin»."""
    if not k:
        return CITTA
    parts = KIND_PART.findall(k)
    assert "".join(a + b for a, b in parts) == k, k
    return CITTA + " " + KIND_JOIN.join((SAMPAYUTTA if b == "sampayutta" else VIPPAYUTTA).format(x=KIND_NOUN[a])
                                        for a, b in parts)


def moment(kind, mo="uppāda"):
    return C8.AT.format(x=C8.OF.format(x=C8.MOMENT[mo], c=citta_kind(kind)))   # vào khoảnh khắc sinh khởi của <tâm>


PAVATTE = T5.PAVATTE                              # «trong quá trình diễn tiến» (5-01)
PAVATTE_JOIN = T5.PAVATTE_JOIN                    # pavatte + moment, no comma (5-01)
TIME_RE = re.compile(r"(?P<pv>[Pp]avatte )?(?P<k>\S*?)cittassa (?P<mo>uppāda|bhaṅga)kkhaṇe")


def head10(g):
    """Pāli answer head (before the resumptive tesaṃ / tāsaṃ) -> Vietnamese head, capitalised.
    Person groups: one «ở» (2-01 WHO_HEAD); the pavatte moment is its own group; groups joined with «, »."""
    mt = re.search(r"(?:^| )([Pp]avatte \S*cittassa (?:uppāda|bhaṅga)kkhaṇe)$", g)
    person = g[:mt.start(1)].strip() if mt else g
    chunks = []
    if person:
        chunks.append(F.WHO_HEAD.format(g=attr_group([low(x) for x in person.split()])))
    if mt:
        tm = TIME_RE.fullmatch(mt.group(1))
        assert tm and tm["pv"], g
        chunks.append(PAVATTE_JOIN.format(a=PAVATTE, b=moment(tm["k"], tm["mo"])))
    return cap(F.LIST_SEP.join(chunks))


# ================================================================ sentences of the pavattivāra
V = r"(?:na )?\S+"
FAC_W = r"\S+ndriyaṃ"                             # cakkhundriyaṃ has no «i» before «ndriya»
RUN = rf"(?:{FAC_W}…pe… )*{FAC_W}"
Q_RE = re.compile(rf"(?:\((?P<l>Ka|Kha)\) )?(?P<w1>[Yy]assa vā pana|[Yy]attha vā pana|[Yy]assa|[Yy]attha) (?P<x>{FAC_W}) "
                  rf"(?P<v1>{V}) (?P<w2>tassa|tattha) (?P<y>{RUN}) (?P<v2>{V})")
RES = r"(?P<r>tesaṃ|tāsaṃ)"
P_NOT = re.compile(rf"(?P<g>.+?) {RES} (?P<x>{FAC_W}) (?P<v1>{V}), no ca (?P<r2>tesaṃ|tāsaṃ) (?P<y>{FAC_W}) (?P<v2>{V})")
P_BOTH = re.compile(rf"(?P<g>.+?) {RES} (?P<x>\S+ndriyañca) (?P<v1>{V}) (?P<y>\S+ndriyañca) (?P<v2>{V})")
L_NOT = re.compile(rf"(?P<g>.+?) tattha (?P<x>{FAC_W}) (?P<v1>{V}), no ca tattha (?P<y>{FAC_W}) (?P<v2>{V})")
L_BOTH = re.compile(rf"(?P<g>.+?) tattha (?P<x>\S+ndriyañca) (?P<v1>{V}) (?P<y>\S+ndriyañca) (?P<v2>{V})")
MULAKA_RE = re.compile(r"\((?P<s>\S+ndriya)mūlakaṃ\)")
AMANTA_PE = "Āmantā …pe…."


def run_vi(ys):
    """itthindriyaṃ…pe… purisindriyaṃ -> «năng lực nữ tính… năng lực nam tính» (3-01 _run: «… »)."""
    return "… ".join(fm(y.strip()) for y in ys.split("…pe…"))


def translate_sentence(s, ctx=""):
    """One pavattivāra sentence (with its final «.» / «?», or a bare mūlaka note) -> Vietnamese."""
    s = s.strip()
    if s == AMANTA_PE:
        return S.AMANTA[:-1] + "…"                                      # 7-04 «Đúng vậy…»
    if s == "Āmantā.":
        return S.AMANTA
    if s == "No.":
        return F.NO
    mm = MULAKA_RE.fullmatch(s)
    if mm:
        return A3.MULAKA.format(x=FAC[low(mm["s"])])
    punct = s[-1]
    assert punct in ".?", s
    body = s[:-1]
    if punct == "?":
        mm = Q_RE.fullmatch(body)
        assert mm, (s, ctx)
        kind = low(mm["w1"]).replace(" vā pana", "")
        assert F.DEM_OF[kind] == mm["w2"], s
        kha = "vā pana" in mm["w1"]
        if mm["l"] and kha != (mm["l"] == "Kha"):
            SLIPS.append((ctx, f"label ({mm['l']}) on a «{'vā pana' if kha else 'no vā pana'}» question; kept"))
        y = run_vi(mm["y"]) if "…pe…" in mm["y"] else fm(mm["y"])
        out = F.b_q(kind, fm(mm["x"]), F.vparse(mm["v1"], ctx), y, F.vparse(mm["v2"], ctx), kha=kha, label=mm["l"])
        if not mm["l"] and body[:1].islower():
            out = low(out)
        return out
    for rx, both, place in ((P_NOT, False, False), (P_BOTH, True, False), (L_NOT, False, True),
                            (L_BOTH, True, True)):
        mm = rx.fullmatch(body)
        if not mm:
            continue
        if place:
            res, head = "tattha", A3.where3(mm["g"])
        else:
            if not both:
                assert mm["r"] == mm["r2"], s
            res, head = "tesaṃ", head10(mm["g"])
            if mm["r"] == "tāsaṃ":
                assert "upapajjantīnaṃ" in mm["g"], s
        f = F.b_both if both else F.b_not
        return f(res, head, fm(mm["x"]), F.vparse(mm["v1"], ctx), fm(mm["y"]), F.vparse(mm["v2"], ctx))
    raise ValueError(f"unmatched sentence: {s!r} ({ctx})")


def split10(t):
    """F.split_sentences, plus a bare «(Xmūlakaṃ)» note after the last sentence is its own piece."""
    out = []
    for s in F.split_sentences(t):
        mm = re.fullmatch(r"(?P<a>.+[.?]) (?P<n>\(\S+mūlakaṃ\))", s.strip())
        out.extend([mm["a"], mm["n"]] if mm else [s])
    return out


def translate_pavatti_line(t, ctx):
    return " ".join(translate_sentence(s, ctx) for s in split10(t) if s.strip())


# ================================================================ lines
EXACT_LINE = {"Paṇṇattiniddesavāro.": F.PANNATTI_NIDDESAVARO}
HEAD_EXTRA = {"Uppādavāro": cap(S.SECTION["uppādavāro"])}     # a heading of its own here (6-01 / 8 «Mục về sự sinh khởi»)


def heading(t):
    return HEAD_EXTRA.get(t) or I.heading(t)


def translate_line(line, ctx="", pavatti=False):
    mm = re.match(r"^(?P<h>#+ )?(?P<t>.*?)(?P<id> \^[0-9A-Za-z-]+)?$", line)
    h, t, sid = mm["h"] or "", mm["t"], mm["id"] or ""
    if h:
        return h + heading(t) + sid
    if t in EXACT_LINE:
        return EXACT_LINE[t] + sid
    if not pavatti:
        out = I.translate_line(t, ctx)
        if re.search(r"\w(?<!Āmantā) …pe…\.$", t):                      # «na cakkhundriyaṃ …pe….»: space before …pe… (8 rule:
            SLIPS.append((ctx, "space before «…pe…» after a statement; «…» written without it (as 8 ^6-8-61)"))
            out = re.sub(r"(\w) …$", r"\1…", out)           # «… uppajjati …» = «…» without the space)
        return out + sid
    return translate_pavatti_line(t, ctx) + sid


def translate_file(name=NAME):
    src = (S.PALI_DIR / name).read_text(encoding="utf-8")
    out, seg, pav = [], "start", False
    for ln in src.splitlines():
        if ln.startswith("#### Pavattivāro"):
            pav = True
        out.append(translate_line(ln, f"segment after ^{seg}", pav) if ln.strip() else "")
        mid = re.search(r"\^([0-9A-Za-z-]+)\s*$", ln)
        if mid:
            seg = mid.group(1)
    text = "\n".join(out).rstrip("\n") + "\n"
    return re.sub(r"\n{3,}", "\n\n", text)


# ================================================================ checks
CROSS_BOOK = [
    ("có niềm vui đi kèm", 1), ("có sự bình thản đi kèm", 1), ("gắn liền với hiểu biết", 1),
    ("không gắn liền với hiểu biết", 1), ("có gốc rễ", 1), ("không có gốc rễ", 1), ("người nữ", 2),
    ("người nam", 2), ("niềm tin", 2), ("khoảnh khắc sinh khởi", 5), ("cõi hình sắc", 1), ("cõi dục lạc", 1),
    ("tái sinh", 2), ("gắn liền với", 1), ("không gắn liền với", 1),
]


def check_cross_book():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in S.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts (10-02): {len(CROSS_BOOK)} strings found in pi-1..5 rails")


def check_frames():
    """Frames shared with the frame-setters stay byte-identical."""
    assert A3.who3("Sacakkhukānaṃ asotakānaṃ upapajjantānaṃ") == \
        F.WHO_HEAD.format(g=attr_group(["sacakkhukānaṃ", "asotakānaṃ", "upapajjantānaṃ"]))
    assert moment("") == "vào khoảnh khắc sinh khởi của tâm"
    assert citta_kind("ñāṇavippayutta") == "tâm không gắn liền với hiểu biết"
    assert T5.CITTA_KIND["taṇhāvippayuttamaggavippayutta"].startswith(CITTA + " " + VIPPAYUTTA.format(x="khao khát")
                                                                        + KIND_JOIN)
    assert S.LABEL["Ka"] == "(a)" and S.LABEL["Kha"] == "(b)"
    try:                                              # 9-01 (running in parallel) renders pavatte differently
        D9 = importlib.import_module("build_9-01_vi")
        if getattr(D9, "PAVATTE", PAVATTE) != PAVATTE:
            print(f"WARN: pavatte differs: 5-01 {PAVATTE!r} (used) vs 9-01 {D9.PAVATTE!r}")
    except Exception as e:                            # noqa: BLE001
        print("note: build_9-01_vi not importable for the pavatte check:", e)


def check_same_as_10_01(text, pali):
    """Every Pāli line of this chapter that also occurs in 10-01 has the same Vietnamese there."""
    p1 = (S.PALI_DIR / I.NAME).read_text(encoding="utf-8").splitlines()
    v1 = (S.OUT_DIR / I.NAME).read_text(encoding="utf-8").splitlines()
    strip = lambda x: re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", x)          # noqa: E731
    ref = {strip(p): strip(v) for p, v in zip(p1, v1) if p.strip() and not p.startswith("#")}
    probs, n = [], 0
    for p, v in zip(pali.splitlines(), text.splitlines()):
        if strip(p) in ref:
            n += 1
            if ref[strip(p)] != strip(v):
                probs.append(f"differs from 10-01: {p[:60]}")
    print(f"lines shared with 10-01 checked: {n}")
    return probs


def main():
    S.check_cross_book()
    F.check_cross_book()
    I.check_cross_book()
    check_cross_book()
    check_frames()
    del SLIPS[:]
    del I.SLIPS[:]
    text = unicodedata.normalize("NFC", translate_file())
    pali = (S.PALI_DIR / NAME).read_text(encoding="utf-8")
    probs = S.check_lines(pali, text, NAME) + I.check_extra(text, pali) + check_same_as_10_01(text, pali)
    for i, ln in enumerate(text.splitlines(), 1):
        body = re.sub(r" ?\[[^\]]*\]", "", re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", ln))
        for bad in ("uppajj", "upapajj", "tesaṃ", "tāsaṃ", "tattha", "mūlakaṃ", "vinā", "kkhaṇe", "thì thì",
                    "là không phải"):
            if bad in body:
                probs.append(f"line {i}: «{bad}»")
    with open(S.OUT_DIR / NAME, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    segs = len(re.findall(r"\^[0-9A-Za-z-]+\s*$", text, flags=re.M))
    print(f"wrote {NAME}: {len([x for x in text.splitlines() if x.strip()])} lines, {segs} segments")
    seen = set()
    for c, w in SLIPS + I.SLIPS:
        if (c, w) not in seen:
            seen.add((c, w))
            print("SLIP", c, "|", w)
    for p in probs[:80]:
        print("PROBLEM", p)
    print("line checks:", "OK" if not probs else f"{len(probs)} problems")
    sys.exit(1 if probs else 0)


if __name__ == "__main__":
    main()
