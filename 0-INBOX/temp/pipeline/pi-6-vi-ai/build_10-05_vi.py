# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 10-05-indriyayamaka.md (Indriyayamaka, pavattivāra, uppādavāra
(2) atītavāra, all six sections, and (3) anāgatavāra, (Ka) anulomapuggalo).

Frames, imported and used VERBATIM:
  build_10-02_vi  (P): faculty names fm(), ATTR10 (somanassena / upekkhāya), citta_kind(), split10(), heading(),
                  MULAKA_RE, run_vi() (asserted equal for «…pe…» runs), translate_sentence() for every place answer
                  (3-01 where3) and «Āmantā …pe….»;
  build_2-01_vi   (F): family B (b_q, b_not, b_both, b_short, vparse, Q_FRAME / REL_VI / DEM_VI / VA_PANA, who(),
                  WHO_HEAD, LIST_SEP, BEINGS_OF, PLANE, PARTICIPLE, YE_UPAPAJJITVA, NATTHI);
  build_2-02_vi   (E): YE_CA_JOIN («… và …»), pe_end() («Natthi …pe….» = «Không có…»);
  build_3-01_vi   (A3): ATTR (sacakkhukā / saghānakā), ATTR_JOIN, MULAKA;
  build_3-02_vi   (A32): _ye_planes() («Ye rūpāvacaraṃ arūpāvacaraṃ upapajjitvā parinibbāyissanti»);
  build_5-01_vi   (T5): VATTAMANA / CITTA_KIND («dutiye citte vattamāne», «upapatticittassa uppādakkhaṇe»), the
                  head rule of head_vi (asserted equal);
  build_6-01_vi   (A6): ANANTARA («yassa cittassa anantarā … pacchimacittaṃ uppajjissati», asserted with head());
  build_8_vi      (C8): citta(last=True) «tâm cuối cùng»;
  labels from build_sample_vi.LABEL.
New here (notes-10-05.md): the future heads «Ye sacakkhukā upekkhāya upapajjitvā parinibbāyissanti», «Ye purisā /
Yā itthiyo eteneva bhāvena katici bhave dassetvā [upekkhāya / somanassena upapajjitvā] parinibbāyissanti»,
«upekkhāsampayuttapacchimacittaṃ», runs in the first slot of a question.

Importing writes nothing; run  python -I -X utf8 -B build_10-05_vi.py  to rebuild the chapter.
"""
import importlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as S  # noqa: E402

F = importlib.import_module("build_2-01_vi")     # families A / B
E = importlib.import_module("build_2-02_vi")     # ye ca join, pe_end
I = importlib.import_module("build_10-01_vi")    # faculty table, check_extra
P = importlib.import_module("build_10-02_vi")    # Indriya pavatti frames
Q = importlib.import_module("build_10-03_vi")    # Indriya puggalokāsa frames (checks)
A3 = importlib.import_module("build_3-01_vi")    # attribute beings, mūlaka notes
A32 = importlib.import_module("build_3-02_vi")   # Ye <P1>ṃ <P2>ṃ upapajjitvā …
T5 = importlib.import_module("build_5-01_vi")    # dutiye citte vattamāne, upapatticitta, head_vi
A6 = importlib.import_module("build_6-01_vi")    # yassa cittassa anantarā … pacchimacittaṃ uppajjissati
C8 = importlib.import_module("build_8_vi")       # tâm cuối cùng

NAME = "10-05-indriyayamaka.md"
cap, low = S.cap, S.low
LABEL = S.LABEL
SLIPS = []

# ================================================================ future heads (new)
YE_FRAME = "những {n} nào sau khi {what} sẽ nhập Niết-bàn trọn vẹn"      # = 2-01 YE_UPAPAJJITVA (asserted)
assert YE_FRAME.format(n="người", what="tái sinh vào {p}") == F.YE_UPAPAJJITVA
UPA_ATTR = "tái sinh {a}"                       # <attr> upapajjitvā (10-02 / 3-01 attribute order: «tái sinh có mắt …»)
BHAVA = "trải qua một số kiếp sống trong chính trạng thái ấy"
# eteneva bhāvena katici bhave dassetvā: aṭṭhakathā ^6-183 «etena purisabhāveneva … katici paṭisandhiyo gahetvā»;
# bhāva «trạng thái» (pi-1 itthibhāva / purisabhāva «trạng thái nữ / nam tính»), bhava «kiếp sống» (2-01 pacchimabhavika)
BHAVA_AND = "{b} và {u}"                         # … dassetvā upekkhāya upapajjitvā … (two absolutives)
YE_NOUN = {"purisā": I.BARE_VI["puriso"], "itthiyo": I.BARE_VI["itthī"]}  # người nam / người nữ (10-01, pi-2)
YE_ATTR = {"sacakkhukā": A3.ATTR["sacakkhukānaṃ"], "saghānakā": A3.ATTR["saghānakānaṃ"]}   # có mắt / có mũi (3-01)
SAHA = {"upekkhāya": P.ATTR10["upekkhāya"], "somanassena": P.ATTR10["somanassena"]}     # có … đi kèm (10-02)
PACCHIMA_KIND = "{c}{rest}"                      # <kind>pacchimacittaṃ = tâm cuối cùng <kind> (6-01 «cuối cùng» first)


def ye_attr(attr, saha):
    """Ye sacakkhukā upekkhāya upapajjitvā parinibbāyissanti."""
    return YE_FRAME.format(n="người", what=UPA_ATTR.format(a=A3.ATTR_JOIN.join([YE_ATTR[attr], SAHA[saha]])))


def ye_bhava(noun, saha=None):
    """Ye purisā / Yā itthiyo eteneva bhāvena katici bhave dassetvā [upekkhāya upapajjitvā] parinibbāyissanti."""
    what = BHAVA if not saha else BHAVA_AND.format(b=BHAVA, u=UPA_ATTR.format(a=SAHA[saha]))
    return YE_FRAME.format(n=YE_NOUN[noun], what=what)


def last_citta(kind):
    """upekkhāsampayutta -> «tâm cuối cùng gắn liền với sự bình thản»."""
    k = P.citta_kind(kind)
    assert k.startswith(P.CITTA + " "), k
    return PACCHIMA_KIND.format(c=C8.citta(last=True), rest=k[len(P.CITTA):])


# ================================================================ answer heads (head5)
GEN = r"(?:rūpāvacar|arūpāvacar|kāmāvacar|asaññasatt|arūp|pañcavokār|catuvokār|suddhāvās)ānaṃ"
ACC = r"(?:rūpāvacar|arūpāvacar|kāmāvacar|arūp)aṃ"
SADDHA_UPA = F.BEINGS_OF.format(p=F.PLANE["suddhāvāsa"]) + " " + F.PARTICIPLE["upapajjantānaṃ"][0]
# Suddhāvāsānaṃ upapajjantānaṃ (^6-10-277, as written: genitive; elsewhere «Suddhāvāsaṃ upapajjantānaṃ»)


def _ye_planes(m):
    r = A32._ye_planes(m[0])
    return r if r else F.who(m[0])                      # single plane: 2-01 who() (no «ở»)


def _who_run(m):
    w = F.who(m[0])
    assert w.startswith(F.WHO_HEAD.format(g="")), w
    return w[len(F.WHO_HEAD.format(g="")):]


def _saddha_upa(m):
    SLIPS.append(("^6-10-277", "«Suddhāvāsānaṃ upapajjantānaṃ» (genitive; the parallels have «Suddhāvāsaṃ "
                               "upapajjantānaṃ»): translated as written «chúng sinh trong cõi Tịnh Cư đang tái sinh»"))
    return SADDHA_UPA


ELEMENTS = [   # (regex at the current position, kind, function); kinds as 5-01 head_vi: R relative (start only),
    #           J «ye ca» (joined «và»), P person (one «ở» over a run), T time phrase (alone)
    (rf"ye (?:{ACC} )+upapajjitvā parinibbāyissanti", "R", _ye_planes),
    (r"ye (?P<a>sacakkhukā|saghānakā) (?P<s>upekkhāya|somanassena) upapajjitvā parinibbāyissanti", "R",
     lambda m: ye_attr(m["a"], m["s"])),
    (r"(?P<ca>ye ca|yā ca|ye|yā) (?P<n>purisā|itthiyo) eteneva bhāvena katici bhave dassetvā "
     r"(?:(?P<s>upekkhāya|somanassena) upapajjitvā )?parinibbāyissanti", None,
     lambda m: ye_bhava(m["n"], m["s"])),
    (r"yassa cittassa anantarā (?P<k>\S+?)pacchimacittaṃ uppajjissati", "T",
     lambda m: A6.ANANTARA.format(c=last_citta(m["k"]))),
    (r"suddhāvāsānaṃ upapajjantānaṃ", "P", _saddha_upa),
    (rf"(?:itaresaṃ )?(?:{GEN} )*{GEN}", "P", _who_run),
    (r"itaresaṃ", "P", lambda m: F.HEAD["itaresaṃ"]),
    (r"dutiye citte vattamāne", "T", lambda m: T5.VATTAMANA.format(c=T5.CITTA_KIND["dutiye"])),
    (r"upapatticittassa (?P<mo>uppāda|bhaṅga)kkhaṇe", "T", lambda m: T5._moment(m["mo"], T5.CITTA_KIND["upapatti"])),
]
ELEMENTS = [(re.compile(p + r"(?= |$)"), k, f) for p, k, f in ELEMENTS]


def head5(g):
    """Pāli answer head (before tesaṃ / tāsaṃ [tattha]) -> Vietnamese head, capitalised (5-01 head_vi rule)."""
    s, pos, items = low(g), 0, []
    while pos < len(s):
        for rx, kind, f in ELEMENTS:
            mm = rx.match(s, pos)
            if mm:
                k = kind or ("J" if mm["ca"].endswith(" ca") else "R")
                items.append((k, f(mm)))
                pos = mm.end() + 1
                break
        else:
            raise ValueError(f"unparsed head {g!r} at {s[pos:]!r}")
    chunks = []
    for kind, text in items:
        last = chunks[-1] if chunks else None
        if kind == "R":
            assert not chunks, g
            chunks.append(["R", text])
        elif kind == "J":
            assert last and last[0] in ("R", "P"), g
            last[1] += E.YE_CA_JOIN + text
        elif kind == "P" and last and last[0] == "P":
            last[1] += F.LIST_SEP + text
        elif kind == "P":
            chunks.append(["P", F.WHO_HEAD.format(g=text)])
        else:
            chunks.append(["T", text])
    return cap(F.LIST_SEP.join(c[1] for c in chunks))


# ================================================================ sentences
V = P.V
FAC_W = P.FAC_W
SEP = r"(?: ?…pe…| ?…) "
RUNX = rf"{FAC_W}(?:{SEP}{FAC_W})*"
SEP_SPLIT = re.compile(r" ?…(?:pe…)? ")
Q5_RE = re.compile(rf"(?:\((?P<l>Ka|Kha)\) )?(?P<w1>[Yy]assa vā pana yattha|[Yy]assa yattha|[Yy]assa vā pana|"
                   rf"[Yy]attha vā pana|[Yy]assa|[Yy]attha) (?P<x>{RUNX}) (?P<v1>{V}) "
                   rf"(?P<w2>tassa tattha|tassa|tattha) (?P<y>{RUNX}) (?P<v2>{V})")
RES5 = r"(?P<r>tesaṃ|tāsaṃ)(?P<t> tattha)?"
N_NOT = re.compile(rf"(?P<g>.+?) {RES5} (?P<x>{FAC_W}) (?P<v1>{V}), no ca (?P<r2>tesaṃ|tāsaṃ)(?P<t2> tattha)? "
                   rf"(?P<y>{FAC_W}) (?P<v2>{V})")
N_BOTH = re.compile(rf"(?P<g>.+?) {RES5} (?P<x>\S+ndriyañca|\S+ndriyaṃ ca) (?P<v1>{V}) (?P<y>\S+ndriyañca) "
                    rf"(?P<v2>{V})")
SHORT_RE = re.compile(r"(?P<b>Uppajj|Nirujjh)(?P<t>ati|ittha|issati)\.")
NATTHI_PE = "Natthi …pe…."


def run5(ys, ctx):
    """A run «X…pe… Y… Z» in either slot -> «X… Y… Z» (10-02 run_vi; a run with bare «…» joins the same way)."""
    if " …" in ys:
        SLIPS.append((ctx, "space before «…» inside a run; «…» written without it (as 10-02 / 8)"))
    return "… ".join(P.fm(y) for y in SEP_SPLIT.split(ys))


def q5(kind, w2, x, v1, y, v2, kha, label):
    """F.b_q, with the demonstrative as the Pāli writes it (one «yassa … tattha» slip)."""
    q = F.Q_FRAME.format(rel=F.REL_VI[kind], a=x, pa=F.verb(*v1), dem=F.DEM_VI[w2], b=y, pb=F.verb(*v2))
    q = cap(F.VA_PANA + q if kha else q)
    out = f"{LABEL[label]} {q}" if label else q
    if F.DEM_OF[kind] == w2:
        assert out == F.b_q(kind, x, v1, y, v2, kha=kha, label=label)
    return out


def translate_sentence(s, ctx=""):
    s = s.strip()
    if s == NATTHI_PE:
        return E.pe_end(F.NATTHI)                                      # «Không có…» (7-04 / 2-02 rule)
    if s == "Natthi.":
        return F.NATTHI
    mm = SHORT_RE.fullmatch(s)
    if mm:                                                             # Uppajjittha. = Đã sinh khởi. (2-01)
        return F.b_short(F.VERB_BASE[low(mm["b"])], F.TENSE_OF[mm["t"]])
    if s in ("Āmantā.", P.AMANTA_PE) or P.MULAKA_RE.fullmatch(s):
        return P.translate_sentence(s, ctx)
    punct, body = s[-1], s[:-1]
    assert punct in ".?", s
    if punct == "?":
        mm = Q5_RE.fullmatch(body)
        assert mm, (s, ctx)
        kind = low(mm["w1"]).replace(" vā pana", "")
        if F.DEM_OF[kind] != mm["w2"]:
            SLIPS.append((ctx, f"«{mm['w1']} … {mm['w2']} …»: «{mm['w2']}» where the pattern has "
                               f"«{F.DEM_OF[kind]}»; translated as written"))
        kha = "vā pana" in mm["w1"]
        if mm["l"] and kha != (mm["l"] == "Kha"):
            SLIPS.append((ctx, f"label ({mm['l']}) on a «{'vā pana' if kha else 'no vā pana'}» question; kept"))
        x = run5(mm["x"], ctx) if "…" in mm["x"] else P.fm(mm["x"])
        y = run5(mm["y"], ctx) if "…" in mm["y"] else P.fm(mm["y"])
        out = q5(kind, low(mm["w2"]), x, F.vparse(mm["v1"], ctx), y, F.vparse(mm["v2"], ctx), kha, mm["l"])
        if not mm["l"] and body[:1].islower():
            out = low(out)
        return out
    for rx, both in ((N_NOT, False), (N_BOTH, True)):
        mm = rx.fullmatch(body)
        if not mm:
            continue
        if not both:
            assert mm["r"] == mm["r2"] and bool(mm["t"]) == bool(mm["t2"]), s
        if mm["r"] == "tāsaṃ":
            assert low(mm["g"]).startswith("yā itthiyo"), s
        xw = mm["x"]
        if xw.endswith(" ca"):
            SLIPS.append((ctx, f"«{xw}» written apart (= «{xw[:-4]}ñca»); same Vietnamese"))
            xw = xw[:-3]
        res = "tesaṃ tattha" if mm["t"] else "tesaṃ"
        f = F.b_both if both else F.b_not
        return f(res, head5(mm["g"]), P.fm(xw), F.vparse(mm["v1"], ctx), P.fm(mm["y"]), F.vparse(mm["v2"], ctx))
    if " tesaṃ " not in s and " tāsaṃ " not in s:
        return P.translate_sentence(s, ctx)                            # place answers (3-01 where3)
    raise ValueError(f"unmatched sentence: {s!r} ({ctx})")


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
    ("trạng thái nam tính", 1), ("trạng thái nữ tính", 1), ("kiếp", 2), ("một số", 2), ("tái sinh", 2),
    ("nhập Niết-bàn trọn vẹn", 5), ("đang diễn ra", 5), ("ngay sau", 5), ("sự bình thản", 1), ("niềm vui", 2),
    ("cõi hình sắc", 1), ("cõi dục lạc", 1), ("Không có.", 3), ("Đúng vậy.", 5),
]


def check_cross_book():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in S.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts (10-05): {len(CROSS_BOOK)} strings found in pi-1..5 rails")


def _sentences(pali):
    for ln in pali.splitlines():
        if not ln.strip() or ln.startswith("#"):
            continue
        t = re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", ln)
        for s in P.split10(t):
            if s.strip():
                yield s.strip()


HEAD_DIFF_OK = {
    # 5-01 head_vi has no rule for the genitive «suddhāvāsānaṃ upapajjantānaṃ» and splits it into two groups
    # («chúng sinh trong cõi Tịnh Cư, những người đang tái sinh»); here it is one group, as written
    ("5-01", "Suddhāvāsānaṃ upapajjantānaṃ asaññasattānaṃ"),
}


def check_frames(pali):
    """Every sentence / head a frame-setter's own parser can translate comes out byte-identical here."""
    probs, n = [], {"10-02": 0, "10-03": 0, "10-04": 0, "5-01": 0, "6-01": 0, "run": 0}
    try:
        R4 = importlib.import_module("build_10-04_vi")
    except Exception as e:                                             # noqa: BLE001 (10-04 runs in parallel)
        print("note: build_10-04_vi not importable:", e)
        R4 = None
    others = [("10-02", P.translate_sentence), ("10-03", Q.translate_sentence)]
    if R4:
        others.append(("10-04", R4.translate_sentence))
    for s in _sentences(pali):
        mine = translate_sentence(s, "check")
        for tag, fn in others:
            try:
                theirs = fn(s, "check")
            except (AssertionError, ValueError, KeyError, TypeError, AttributeError):
                continue
            n[tag] += 1
            if theirs != mine:
                probs.append(f"differs from {tag}: {s[:70]} | {theirs[:60]} | {mine[:60]}")
        mm = (N_NOT.fullmatch(s[:-1]) or N_BOTH.fullmatch(s[:-1])) if s.endswith(".") else None
        if mm:
            g = mm["g"]
            for tag, fn in (("5-01", T5.head_vi), ("6-01", lambda x: cap(A6.head(x)))):
                try:
                    o = fn(g)
                except (AssertionError, ValueError, KeyError, TypeError, AttributeError):
                    continue
                n[tag] += 1
                if (tag, g) in HEAD_DIFF_OK:
                    continue
                if o != head5(g):
                    probs.append(f"head differs from {tag}: {g} | {o} | {head5(g)}")
        mq = Q5_RE.fullmatch(s[:-1]) if s.endswith("?") else None
        if mq and "…pe…" in mq["y"] and "…" not in mq["y"].replace("…pe…", ""):
            n["run"] += 1
            assert run5(mq["y"], "check") == P.run_vi(mq["y"])
    for tag in (P, Q):
        del tag.SLIPS[:]
    if R4:
        del R4.SLIPS[:]
    del F.SLIPS[:]
    print("frame checks:", ", ".join(f"{k} {v}" for k, v in n.items()))
    # fixed points
    assert head5("Itaresaṃ") == cap(F.who("Itaresaṃ"))
    assert head5("Ye rūpāvacaraṃ arūpāvacaraṃ upapajjitvā parinibbāyissanti") == \
        cap(A32._ye_planes("Ye rūpāvacaraṃ arūpāvacaraṃ upapajjitvā parinibbāyissanti"))
    assert head5("Suddhāvāsānaṃ dutiye citte vattamāne asaññasattānaṃ") == \
        T5.head_vi("Suddhāvāsānaṃ dutiye citte vattamāne asaññasattānaṃ")
    assert head5("Itaresaṃ catuvokārānaṃ pañcavokārānaṃ") == \
        T5.head_vi("Itaresaṃ catuvokārānaṃ pañcavokārānaṃ")
    assert head5("Rūpāvacarānaṃ arūpāvacarānaṃ") == cap(A6.head("Rūpāvacarānaṃ arūpāvacarānaṃ"))
    g = "Yassa cittassa anantarā kāmāvacarānaṃ pacchimacittaṃ uppajjissati"          # 6-01 ANANTARA frame
    assert cap(A6.head(g)) == cap(A6.ANANTARA.format(c=A6.ANANTARA_K["kāmāvacarānaṃ"]))
    assert T5.VATTAMANA.format(c=T5.CITTA_KIND["dutiye"]) == A6.VATTAMANE
    assert S.LABEL["Ka"] == "(a)" and S.LABEL["Kha"] == "(b)" and S.LABEL["Ca"] == "(e)" and S.LABEL["Ṅa"] == "(đ)"
    del SLIPS[:]
    return probs


def check_same_as_other(text, pali):
    """Every Pāli line of this chapter that also occurs in a finished Indriya chapter has the same Vietnamese."""
    strip = lambda x: re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", x)          # noqa: E731
    probs = []
    for nm in ("10-01-indriyayamaka.md", "10-02-indriyayamaka.md", "10-03-indriyayamaka.md",
               "10-04-indriyayamaka.md"):
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
    pali = (S.PALI_DIR / NAME).read_text(encoding="utf-8")
    fprobs = check_frames(pali)
    del SLIPS[:]
    del P.SLIPS[:]
    del F.SLIPS[:]
    text = unicodedata.normalize("NFC", translate_file())
    probs = S.check_lines(pali, text, NAME) + I.check_extra(text, pali) + check_same_as_other(text, pali) + fprobs
    for i, ln in enumerate(text.splitlines(), 1):
        body = re.sub(r" ?\[[^\]]*\]", "", re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", ln))
        for bad in ("uppajj", "upapajj", "tesaṃ", "tāsaṃ", "tattha", "mūlakaṃ", "kkhaṇe", "thì thì", "là không phải",
                    "ndriy", "sabbesaṃ", "ānaṃ", "….", "  ", "là là", "pe…", "bhāv", "anantarā", "itthiyo", "purisā",
                    "ṃ", "ā "):
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
