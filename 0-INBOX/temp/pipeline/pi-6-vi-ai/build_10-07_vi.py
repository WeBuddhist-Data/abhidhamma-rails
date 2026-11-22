# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 10-07-indriyayamaka.md (Indriyayamaka, pavattivāra, uppādavāra,
anāgatavāra: (Ca) paccanīkapuggalokāsā, the future tense «na uppajjissati» person-and-place pairs).

Frames, imported and used VERBATIM:
  build_10-04_vi  (R): translate_sentence() for every «yassa yattha» question, Āmantā, mūlaka note (and through it
                  build_10-02_vi: fm, run_vi, split10, heading); the answer regexes P4_NOT / P4_BOTH;
  build_10-02_vi  (P): fm(), ATTR10 («có niềm vui đi kèm», «có sự bình thản đi kèm»), SAMPAYUTTA, KIND_NOUN, BARE;
  build_2-01_vi   (F): b_not / b_both (res «tesaṃ tattha»), vparse, who() (pacchimabhavikānaṃ, <P>e pacchimabhavikānaṃ,
                  rūpāvacarānaṃ arūpāvacarānaṃ, asaññasattānaṃ, arūpānaṃ), WHO_HEAD, LIST_SEP, YE_UPAPAJJITVA;
  build_2-02_vi   (E): YE_CA_JOIN («<beings> ye ca …» = «<beings> và …»);
  build_3-01_vi   (A3): ATTR («có mắt», «có mũi»);
  build_6-01_vi   (X6): ANANTARA «vào tâm mà ngay sau đó {c} sẽ sinh khởi» (yassa cittassa anantarā … pacchimacittaṃ
                  uppajjissati), «cuối cùng» before a long citta kind (LAST_AVITAKKA pattern);
  build_8_vi      (C8): SAMANGI / citta(last=True) / for_ (pacchimacittasamaṅgīnaṃ = những người có được tâm cuối cùng);
  build_9-01_vi   (D9): the element head rule (consecutive persons share one «ở», a time phrase stands alone);
  labels from build_sample_vi.LABEL.
New here (notes-10-07.md): «ye purisā / yā itthiyo eteneva bhāvena katici bhave dassetvā [M upapajjitvā]
parinibbāyissanti», «ye sacakkhukā / saghānakā M upapajjitvā parinibbāyissanti», the kinds
«upekkhā- / somanassasampayuttapacchimacittaṃ».

Importing writes nothing; run  python -I -X utf8 -B build_10-07_vi.py  to rebuild the chapter.
"""
import importlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as S  # noqa: E402

F = importlib.import_module("build_2-01_vi")     # family B
E = importlib.import_module("build_2-02_vi")     # «ye ca …» join
I = importlib.import_module("build_10-01_vi")    # faculty table, check_extra
P = importlib.import_module("build_10-02_vi")    # Indriya pavatti frames
R = importlib.import_module("build_10-04_vi")    # yassa yattha questions, answer regexes
A3 = importlib.import_module("build_3-01_vi")    # attribute words
X6 = importlib.import_module("build_6-01_vi")    # ANANTARA
C8 = importlib.import_module("build_8_vi")       # samaṅgī, last citta
D9 = importlib.import_module("build_9-01_vi")    # head rule

NAME = "10-07-indriyayamaka.md"
cap, low = S.cap, S.low
LABEL = S.LABEL
SLIPS = []
OI = D9.OI                                        # «ở » before a run of persons
assert F.WHO_HEAD.format(g="") == OI == C8.for_("")


def _strip_o(s):
    assert s.startswith(OI), s
    return s[len(OI):]


# ================================================================ the future «ye …» clauses: 10-05 (same Pāli, same
# run, finished first; also used by 10-06) settled them; imported and used verbatim.
Y5 = importlib.import_module("build_10-05_vi")    # ye_bhava(), ye_attr(), last_citta(), head5()
assert Y5.YE_FRAME.format(n="người", what="tái sinh vào {p}") == F.YE_UPAPAJJITVA
ye_bhava = Y5.ye_bhava      # ye purisā / yā itthiyo eteneva bhāvena katici bhave dassetvā [M upapajjitvā] parinibbāyissanti
ye_attr = Y5.ye_attr        # ye sacakkhukā / saghānakā M upapajjitvā parinibbāyissanti


def last_kind(k):
    """upekkhāsampayutta -> «tâm cuối cùng gắn liền với sự bình thản» (10-05 last_citta; 6-01 «cuối cùng» first)."""
    out = Y5.last_citta(k + "sampayutta")
    assert out == C8.citta(last=True) + " " + P.SAMPAYUTTA.format(x=P.KIND_NOUN[k]), out
    return out


# ================================================================ answer heads (head7)
_LOC = sorted(w for w, (c, _s) in F._FORMS.items() if c == "loc")
_GEN = sorted(w for w, (c, _s) in F._FORMS.items() if c == "gen")
WHO_TOK = "|".join(re.escape(w) for w in _LOC + _GEN + ["pacchimabhavikānaṃ"])
BHAVA_P = r"eteneva bhāvena katici bhave dassetvā (?:(?P<m>somanassena|upekkhāya) upapajjitvā )?parinibbāyissanti"
ELEMENTS = [
    (r"yassa cittassa anantarā (?P<k>somanassa|upekkhā)sampayuttapacchimacittaṃ uppajjissati", "T",
     lambda m: X6.ANANTARA.format(c=last_kind(m["k"]))),                                         # 6-01
    (rf"(?:ye ca (?P<p>purisā)|yā ca (?P<q>itthiyo)) {BHAVA_P}", "Y",
     lambda m: ye_bhava(m["p"] or m["q"], m["m"])),                                               # 10-05
    (rf"(?:ye (?P<p>purisā)|yā (?P<q>itthiyo)) {BHAVA_P}", "N",
     lambda m: ye_bhava(m["p"] or m["q"], m["m"])),                                               # 10-05
    (r"ye (?P<a>sacakkhukā|saghānakā) (?P<m>somanassena|upekkhāya) upapajjitvā parinibbāyissanti", "N",
     lambda m: ye_attr(m["a"], m["m"])),                                                          # 10-05
    (r"pacchimacittasamaṅgīnaṃ", "P", lambda m: C8.SAMANGI.format(c=C8.citta(last=True))),        # 8
    (rf"(?:{WHO_TOK})(?: (?:{WHO_TOK}))*", "P", lambda m: _strip_o(F.who(m[0]))),               # 2-01 who
]
ELEMENTS = [(re.compile(p + r"(?= |$)"), k, f) for p, k, f in ELEMENTS]


def head7(g):
    """Pāli answer head (before tesaṃ / tāsaṃ tattha) -> Vietnamese head, capitalised.
    Persons in a row share one «ở» (2-01 / 9-01), a time phrase stands alone, «ye ca …» joins the persons with
    « và » (2-02), a nominative «ye …» head has no «ở» (2-01 YE_UPAPAJJITVA); all joined «, »."""
    p, i, pieces = low(g), 0, []            # pieces: [kind, [texts]]
    while i < len(p):
        for rx, kind, fn in ELEMENTS:
            mm = rx.match(p, i)
            if mm:
                vi = fn(mm)
                if kind == "P" and pieces and pieces[-1][0] == "P":
                    pieces[-1][1].append(vi)
                elif kind == "Y":
                    assert pieces and pieces[-1][0] == "P", g
                    pieces[-1][1][-1] += E.YE_CA_JOIN + vi
                else:
                    pieces.append([kind, [vi]])
                i = mm.end() + 1
                break
        else:
            raise ValueError(f"unparsed head {g!r} at {p[i:]!r}")
    if any(k == "N" for k, _v in pieces):
        assert len(pieces) == 1, g
    out = [OI + F.LIST_SEP.join(v) if k == "P" else v[0] for k, v in pieces]
    return cap(F.LIST_SEP.join(out))


# ================================================================ sentences
def translate_sentence(s, ctx=""):
    s = s.strip()
    if s.endswith("."):
        body = s[:-1]
        for rx, both in ((R.P4_NOT, False), (R.P4_BOTH, True)):
            mm = rx.fullmatch(body)
            if not mm:
                continue
            if not both:
                assert mm["r"] == mm["r2"], s
            if mm["r"] == "tāsaṃ":                      # feminine resumptive = same Vietnamese (10-02)
                assert mm["g"].startswith("Yā itthiyo "), s
            f = F.b_both if both else F.b_not
            return f("tesaṃ tattha", head7(mm["g"]), P.fm(mm["x"]), F.vparse(mm["v1"], ctx), P.fm(mm["y"]),
                     F.vparse(mm["v2"], ctx))
    return R.translate_sentence(s, ctx)                  # questions, Āmantā, mūlaka notes (10-04 / 10-02)


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
    ("người nam", 2), ("người nữ", 2), ("có mắt", 4), ("sau khi tái sinh", 4), ("nhập Niết-bàn trọn vẹn", 5), ("gắn liền với sự bình thản", 1), ("gắn liền với niềm vui", 2),
    ("chúng sinh Vô Tưởng", 5), ("cõi dục lạc", 1), ("cõi hình sắc", 1), ("cõi không hình sắc", 5),
]


def check_cross_book():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in S.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts (10-07): {len(CROSS_BOOK)} strings found in pi-1..5 rails")


def check_frames():
    """Frames shared with the frame-setters stay byte-identical."""
    for g in ("Pacchimabhavikānaṃ", "Rūpāvacarānaṃ arūpāvacarānaṃ", "Pañcavokāre pacchimabhavikānaṃ asaññasattānaṃ arūpānaṃ",
              "Kāmāvacare pacchimabhavikānaṃ rūpāvacarānaṃ arūpāvacarānaṃ", "Asaññasattānaṃ arūpānaṃ"):
        assert head7(g) == cap(F.who(g)), (head7(g), F.who(g))
    assert head7("Asaññasattānaṃ") == R.head4("Asaññasattānaṃ")
    assert head7("Pacchimacittasamaṅgīnaṃ") == cap(C8.P_SUBJ["Pacchimacittasamaṅgīnaṃ"]) == \
        cap(D9.who9("Pacchimacittasamaṅgīnaṃ"))
    assert C8.citta(last=True) == "tâm cuối cùng" and X6.LAST_AVITAKKA.startswith(C8.citta(last=True) + " ")
    assert X6.ANANTARA == "vào tâm mà ngay sau đó {c} sẽ sinh khởi"
    assert E.YE_CA_JOIN == " và " == Y5.E.YE_CA_JOIN
    assert S.LABEL["Ka"] == "(a)" and S.LABEL["Kha"] == "(b)" and S.LABEL["Ca"] == "(e)"


def check_parallel(pali):
    """Every sentence the 10-02 / 10-04 / 10-05 / 10-06 parsers (same yamaka) can translate, and every answer head
    10-05 head5 / 10-06 head6 can translate, comes out byte-identical here."""
    try:
        Y6 = importlib.import_module("build_10-06_vi")
    except Exception as e:                            # noqa: BLE001
        print("note: build_10-06_vi not importable:", e)
        Y6 = None
    mods = [("10-04", R), ("10-02", P), ("10-05", Y5)] + ([("10-06", Y6)] if Y6 else [])
    heads = [("head5", Y5.head5)] + ([("head6", Y6.head6)] if Y6 and hasattr(Y6, "head6") else [])
    probs, n = [], {k: 0 for k, _m in mods + heads}
    for ln in pali.splitlines():
        if not ln.strip() or ln.startswith("#"):
            continue
        t = re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", ln)
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
                    _diff(tag, f"differs from {tag}: {s[:70]} | {theirs} | {mine}", theirs, mine, probs)
            mm = R.P4_NOT.fullmatch(s[:-1]) or R.P4_BOTH.fullmatch(s[:-1])
            if not mm:
                continue
            for tag, fn in heads:
                try:
                    o = fn(mm["g"])
                except (AssertionError, ValueError, KeyError, TypeError):
                    continue
                n[tag] += 1
                if o != head7(mm["g"]):
                    _diff(tag, f"head differs from {tag}: {mm['g']} | {o} | {head7(mm['g'])}", o, head7(mm["g"]),
                          probs)
    for _t, mod in mods:
        del mod.SLIPS[:]
    print("parallel checks:", ", ".join(f"{k} {v}" for k, v in n.items()))
    for w in sorted(WARNED):
        print("WARN", w)
    return probs


WARNED = set()


def _diff(tag, msg, theirs, mine, probs):
    """10-06 (running in parallel) writes «ở» before each person element after the first (head6); 2-01 who, 9-01,
    10-04 head4 and 10-05 head5 share one «ở» over a run of persons. That one difference is a warning, anything
    else a problem."""
    if tag in ("10-06", "head6") and theirs.replace(", ở ", ", ") == mine.replace(", ở ", ", "):
        WARNED.add(f"{tag} repeats «ở» inside a run of persons (one «ở» kept here, = 2-01 / 10-04 / 10-05)")
        return
    probs.append(msg)


def check_same_as_other(text, pali):
    """Every Pāli line of this chapter that also occurs in another written Indriya chapter has the same Vietnamese."""
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
        ref = {strip(p): strip(v) for p, v in zip(p1, v1) if p.strip()}
        n = 0
        for p, v in zip(pali.splitlines(), text.splitlines()):
            if p.strip() and strip(p) in ref:
                n += 1
                if ref[strip(p)] != strip(v):
                    probs.append(f"differs from {nm}: {p[:70]}")
        print(f"lines shared with {nm} checked: {n}")
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
    del SLIPS[:]
    del P.SLIPS[:]
    del R.SLIPS[:]
    del F.SLIPS[:]
    text = unicodedata.normalize("NFC", translate_file())
    probs = (S.check_lines(pali, text, NAME) + I.check_extra(text, pali) + check_same_as_other(text, pali)
             + pprobs)
    for i, ln in enumerate(text.splitlines(), 1):
        body = re.sub(r" ?\[[^\]]*\]", "", re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", ln))
        for bad in ("uppajj", "upapajj", "tesaṃ", "tāsaṃ", "tattha", "mūlakaṃ", "kkhaṇe", "thì thì", "bhāv",
                    "là không phải", "ndriya", "ānaṃ", "Āmantā", "….", "  ", "là là", "ye ca", "itthiyo", "purisā",
                    "pacchima", "anantarā", "parinibb"):
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
