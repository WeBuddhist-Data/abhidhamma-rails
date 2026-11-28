"""Russian plain zero-shot of pi-6 (Yamaka): chapter 10-07-indriyayamaka.md (Indriyayamaka, pavattivāra,
uppādavāra anāgata: (Ca) paccanīkapuggalokāsā, "yassa yattha X na uppajjissati tassa tattha Y na uppajjissatīti?").

Every frame comes from the Indriya builders (imported, never edited):
  members, headings, mūlaka tails   build_10-01_ru (IN_PV_SUBJ, TAIL_RE, TAILS)
  person attributes                 build_10-02_ru (IN_ATTR «с радостью» / «с невозмутимостью», IN_HAVE2, IN_ASSOC,
                                    SAMP «связанного»), build_3-01_ru (have_desc «с глазом», HAVE_JOIN, AY_PLANES)
  intro joining, persons            build_10-03_ru (in_units, moments(), pv_norm, S1_RE / S2_RE) on build_5-01_ru
                                    (pv_intro: «A, B и C», «, и» after a clause, «у них» / «там»)
  family B frames                   build_2-01_ru (PV_Q, PV_PRED, verb(), PV_NO_CA_POS_FRAME, PV_NEITHER_FRAME)
  persons of the future             build_2-01_ru PERSON_UNITS («тех, кто живёт последней жизнью {in}»), build_2-02_ru
                                    («тех, кто, переродившись {in}, достигнет окончательного угасания»), build_6-01_ru
                                    («сразу после данного ума возникнет последний ум»)
New in this chapter (notes-10-07.md):
  "ye ca purisā eteneva bhāvena katici bhave dassetvā [somanassena / upekkhāya upapajjitvā] parinibbāyissanti"
      = «тех мужчин, которые, пройдя в этом же состоянии несколько существований[ и переродившись с радостью],
        достигнут окончательного угасания» (aṭṭhakathā ^6-183: etena purisabhāveneva …, katici paṭisandhiyo gahetvā)
  "ye sacakkhukā upekkhāya upapajjitvā parinibbāyissanti" = «тех, кто, переродившись с глазом и с невозмутимостью,
      достигнет окончательного угасания» (2-02 frame + 10-02 attributes)
  "yassa cittassa anantarā upekkhāsampayuttapacchimacittaṃ uppajjissati" = «тех, у кого сразу после данного ума
      возникнет последний ум, связанный с невозмутимостью» (6-01 frame + 10-02 «связанного с»)
  "Yassa yattha X na uppajjissati tassa tattha Y…pe… Z…pe… W na uppajjissatīti?" = «У кого где не возникнет X, у того
      там не возникнет Y… Z… W?» (10-02 chain question with the 7-01 person / place question)

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_10-07_ru.py [--probe]
Import: importlib.import_module("build_10-07_ru")   (importing never writes any file)
"""
import importlib
import pathlib
import re
import sys
import unicodedata

HERE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru")
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import build_sample_ru as B  # noqa: E402

I = importlib.import_module("build_10-01_ru")    # members, headings, mūlaka tails
P2 = importlib.import_module("build_10-02_ru")   # person attributes, associated minds, chain questions
P3 = importlib.import_module("build_10-03_ru")   # person / place driver: in_units, moments(), S1_RE / S2_RE
K = importlib.import_module("build_6-01_ru")     # «сразу после данного ума возникнет последний ум»
D = I.D                                          # build_2-01_ru: family B
A3 = I.A                                         # build_3-01_ru: Āyatana planes, have_desc
C = I.C                                          # build_7-01_ru: person / place shape
S = P3.S                                         # build_5-01_ru: pv_intro
E = S.E                                          # build_2-02_ru
CHAPTER = "10-07-indriyayamaka.md"
cap, lower1 = B.cap, C.lower1
SLIP_LOG = []

# =============================================================================================
# Persons of the future (uppādavāra anāgata)
# =============================================================================================
_LAST_LIFE = next(ru for rx, ru, _ in D.PERSON_UNITS if rx == r"{P}e pacchimabhavikānaṃ")   # тех, кто живёт последней жизнью {in1}
_YE_CA = next(ru for rx, ru, _ in E.PERSON_UNITS_2_02
              if rx == r"ye ca {P}aṃ upapajjitvā parinibbāyissanti")   # тех, кто, переродившись {in1}, достигнет …
assert _YE_CA == "тех, кто, переродившись {in1}, достигнет окончательного угасания", _YE_CA
_REBORN_ABS = "переродившись {desc}"             # upapajjitvā (2-02)
_PARINIB_SG = "достигнет окончательного угасания"
_PARINIB_PL = "достигнут окончательного угасания"   # plural after «которые» (2-02 verb, plural)
assert _PARINIB_SG in _YE_CA
# "eteneva bhāvena katici bhave dassetvā": aṭṭhakathā ^6-183 "etena purisabhāveneva … katici paṭisandhiyo gahetvā
# itthibhāvaṃ appatvāva parinibbāyissanti".
SAME_STATE = "пройдя в этом же состоянии несколько существований"
GENDER_NOUN = {"purisā": ("ye", "мужчин"), "itthiyo": ("yā", "женщин")}   # pi-4 «мужчина» / «женщина» (10-01)
GENDER_FRAME = "тех {noun}, которые, {same}, {parinib}"
GENDER_REBORN_FRAME = "тех {noun}, которые, {same} и {reborn}, {parinib}"
PL = A3.AY_PLANES


def _desc(*keys):
    """Pāli attribute keys (10-02 / 3-01) -> «с глазом и с невозмутимостью» (3-01 HAVE_JOIN, Pāli order)."""
    out = []
    for k in keys:
        out.append(P2.IN_ATTR[k] if k in P2.IN_ATTR else A3.have_desc(k, P2.IN_HAVE2))
    return A3.HAVE_JOIN.join(out)


MY_UNITS = []   # (regex on the lower-cased intro, Russian, kind as build_5-01_ru)
for _g, (_rel, _noun) in GENDER_NOUN.items():
    for _ca in ("ca ", ""):
        _head = rf"{_rel} {_ca}{_g} eteneva bhāvena katici bhave dassetvā "
        for _attr in ("somanassena", "upekkhāya"):
            MY_UNITS.append((_head + rf"{_attr} upapajjitvā parinibbāyissanti",
                             GENDER_REBORN_FRAME.format(noun=_noun, same=SAME_STATE, parinib=_PARINIB_PL,
                                                        reborn=_REBORN_ABS.format(desc=_desc(_attr))), "rel"))
        MY_UNITS.append((_head + "parinibbāyissanti",
                         GENDER_FRAME.format(noun=_noun, same=SAME_STATE, parinib=_PARINIB_PL), "rel"))
for _stem in P2.IN_HAVE2:                                  # "ye sacakkhukā upekkhāya upapajjitvā parinibbāyissanti"
    for _attr in ("somanassena", "upekkhāya"):
        MY_UNITS.append((rf"ye (?:ca )?sa{_stem}ā {_attr} upapajjitvā parinibbāyissanti",
                         _YE_CA.format(in1=_desc(f"sa{_stem}ānaṃ", _attr)), "rel"))
# «последний ум» is the subject (nominative): «связанный с …» (pi-1 «связанный со знанием»; 10-02 SAMP «связанного»
# is the genitive of the moments «в момент возникновения ума, связанного с …»)
assert P2.SAMP == "связанного"
SAMP_NOM = "связанный"
for _m, _instr in P2.IN_ASSOC.items():                     # "yassa cittassa anantarā Xsampayuttapacchimacittaṃ uppajjissati"
    MY_UNITS.append((rf"yassa cittassa anantarā {_m}sampayuttapacchimacittaṃ uppajjissati",
                     f"тех, у кого {K.LAST_MIND_ARISES}, {SAMP_NOM} {A3.s_prep(_instr)}", "rel"))
MY_UNITS += [
    (r"kāmāvacare pacchimabhavikānaṃ", _LAST_LIFE.format(in1=PL["kāmāvacar"]["in"]), "rel"),        # 3-03
    (r"rūpāvacarānaṃ arūpāvacarānaṃ",
     f'{PL["rūpāvacar"]["beings"]} и {PL["arūpāvacar"]["beings"]}', "noun"),                          # 3-01 / 3-02
    (r"rūpāvacarānaṃ", PL["rūpāvacar"]["beings"], "noun"),                                              # 3-01
    (r"arūpāvacarānaṃ", PL["arūpāvacar"]["beings"], "noun"),
]
_MY_RX = [(re.compile(rx), ru, kind) for rx, ru, kind in MY_UNITS]


def my_units(intro):
    """Intro -> 5-01 units: this chapter's units first; the stretches between them go through build_10-03_ru.in_units
    (Indriya attributes, then build_5-01_ru.sc_units)."""
    s = lower1(intro).replace(",", "")
    units, rest, pos = [], [], 0

    def flush():
        if rest:
            units.extend(P3.in_units(" ".join(rest)))
            rest.clear()

    while pos < len(s):
        for rx, ru, kind in _MY_RX:
            m = rx.match(s, pos)
            if m and (m.end() == len(s) or s[m.end()] == " "):
                flush()
                units.append([ru, kind])
                pos = m.end() + 1
                break
        else:
            j = s.find(" ", pos)
            rest.append(s[pos:] if j < 0 else s[pos:j])
            pos = len(s) if j < 0 else j + 1
    flush()
    return units


def my_intro(intro, tattha=False):
    """build_5-01_ru.pv_intro with build_10-03_ru's moments / attributes and this chapter's units."""
    with P3.moments():
        S.sc_units = my_units          # restored by moments() on exit
        return S.pv_intro(intro, tattha)


# =============================================================================================
# Sentences and questions (as build_10-03_ru.in_pv_sentence, with my_intro)
# =============================================================================================
SUBJ = I.IN_PV_SUBJ


def _pred(v, x, neg):
    return D.PV_PRED.format(v=D.verb(v, x["g"], bool(neg)), x=x["nom"])


def pv_sentence(s, subj=SUBJ):
    """One Pāli answer sentence (no final '.') -> Russian sentence with '.'."""
    if s + "." in C.SIMPLE_ANSWERS:
        return C.SIMPLE_ANSWERS[s + "."]
    s = P3.pv_norm(s)
    m = P3.S1_RE.fullmatch(s)
    if m:
        head = (my_intro(m.group("intro"), "tattha" in m.group("t1")) if m.group("t1").startswith("tesaṃ")
                else S.place_intro(m.group("intro")))
        x, y = subj[m.group("x")], subj[m.group("y")]
        v2 = D.verb(m.group("v2"), y["g"], not m.group("n2"))      # "no ca": the predicate is denied for Y
        tail = (D.PV_NO_CA_POS_FRAME if m.group("n2") else C.NO_CA_FRAME).format(
            res=C.RES[m.group("t2")], **{("pred" if m.group("n2") else "neg_pred"): D.PV_PRED.format(v=v2, x=y["nom"])})
        return head + _pred(m.group("v1"), x, m.group("n1")) + tail + "."
    m = P3.S2_RE.fullmatch(s)
    if m:
        head = (my_intro(m.group("intro"), "tattha" in m.group("t1")) if m.group("t1").startswith("tesaṃ")
                else S.place_intro(m.group("intro")))
        x, y = subj[m.group("x")], subj[m.group("y")]
        if m.group("n1") and m.group("n2"):
            f1, f2 = D.verb(m.group("v1"), x["g"]), D.verb(m.group("v2"), y["g"])
            both = (D.PV_NEITHER_FRAME.format(v=f1, x=x["nom"], y=y["nom"]) if f1 == f2
                    else D.PV_NEG_MIXED_FRAME.format(v1=f1, x=x["nom"], v2=f2, y=y["nom"]))
        else:
            both = C.BOTH_FRAME.format(p1=_pred(m.group("v1"), x, m.group("n1")),
                                       p2=_pred(m.group("v2"), y, m.group("n2")))
        return head + both + "."
    raise ValueError(f"pavatti answer not parsed: {s!r}")


# "Yassa yattha X na uppajjissati tassa tattha Y…pe… Z…pe… W na uppajjissatīti" (10-02 chain, verb once)
CHAIN_PP_RE = re.compile(r"(?P<rel>yassa vā pana yattha|yassa yattha) (?P<x>\S+) (?P<n1>na |n)?(?P<v1>" + D.V_RE
                         + r") tassa tattha (?P<ys>(?:\S+…pe… )+\S+) (?P<n2>na |n)?(?P<v2>" + D.VTI_RE + r")")


def question(q, subj=SUBJ):
    body = lower1(q.strip())
    m = CHAIN_PP_RE.fullmatch(body)
    if not m:
        return P3.in_pv_question(q, subj)
    x = subj[m.group("x")]
    ys = [subj[w] for w in m.group("ys").split("…pe… ")]
    p1 = _pred(m.group("v1"), x, m.group("n1"))
    p2 = D.PV_PRED.format(v=D.verb(D.PV_VERB_TI[m.group("v2")], ys[0]["g"], bool(m.group("n2"))),
                          x="… ".join(y["nom"] for y in ys))
    out = D.PV_Q["yassa yattha"].format(p1=p1, p2=p2)
    return (D.PV_KHA + lower1(out)) if "vā pana" in m.group("rel") else out


# =============================================================================================
# Lines
# =============================================================================================
SENT_RE = re.compile(r"\s*([^?.]+[?.])")


def tr_line(text, subj=SUBJ):
    """Translate one Pāli line (block ID removed): questions and answers in any order on the line."""
    if not text.strip():
        return ""
    if text.startswith("#"):
        return P2.tr_line(text, P2.IN2_CFG)
    m = I.TAIL_RE.fullmatch(text)
    if m:
        return tr_line(m.group(1), subj) + f" ({I.TAILS[m.group(2)]}){m.group(3)}"
    label = ""
    m = P3.LABEL_RE.fullmatch(text)
    if m:
        label, text = f"({B.LETTERS[m.group(1)]}) ", m.group(2)
    out, pos = [], 0
    while pos < len(text):
        ms = SENT_RE.match(text, pos)
        if not ms:
            raise ValueError(f"line not segmented at {text[pos:]!r}")
        seg = ms.group(1)
        pos = ms.end()
        out.append(question(seg[:-1], subj) if seg.endswith("?") else pv_sentence(seg[:-1], subj))
    return label + " ".join(out)


def translate_text(src, subj=SUBJ):
    out = []
    for line in src.split("\n"):
        body, bid = B.ID_RE.match(line).groups()
        out.append(tr_line(body, subj) + (bid or ""))
    return unicodedata.normalize("NFC", "\n".join(out))


# =============================================================================================
# Checks
# =============================================================================================
CROSSBOOK = [   # strings taken from the approved pi-1 … pi-5 Russian rails (book, exact substring)
    ("4", "мужчин"), ("4", "женщин"), ("2", "перерождаются"), ("1", "связанный со знанием"),
]


def check_with_10_03(src):
    """Every sentence / question that build_10-03_ru parses comes out byte-identical here."""
    same = 0
    for line in src.split("\n"):
        body, _ = B.ID_RE.match(line).groups()
        if not body.strip() or body.startswith("#"):
            continue
        m = I.TAIL_RE.fullmatch(body)
        body = m.group(1) if m else body
        m = P3.LABEL_RE.fullmatch(body)
        body = m.group(2) if m else body
        for seg in SENT_RE.findall(body):
            try:
                theirs = P3.in_pv_question(seg[:-1]) if seg.endswith("?") else P3.in_pv_sentence(seg[:-1])
            except (ValueError, KeyError):
                continue
            mine = question(seg[:-1]) if seg.endswith("?") else pv_sentence(seg[:-1])
            assert theirs == mine, (seg, theirs, mine)
            same += 1
    return same


def compare_lines(modname, src, ru, strict=True):
    """Lines that another Indriya builder (10-05 / 10-06, run in parallel) translates must come out the same."""
    try:
        M = importlib.import_module(modname)
    except ImportError:
        return None
    same, diff = 0, []
    for p, r in zip(src.split("\n"), ru.split("\n")):
        body, bid = B.ID_RE.match(p).groups()
        try:
            theirs = M.tr_line(body) + (bid or "")
        except Exception:  # noqa: BLE001  (their parser does not cover this line)
            continue
        if theirs == r:
            same += 1
        else:
            diff.append((p, r, theirs))
    if strict:
        assert not diff, "\n".join(f"{p}\n  mine:   {r}\n  theirs: {t}" for p, r, t in diff[:5])
    return same, diff


def check_against_finished(src, ru):
    """Identical Pāli line = identical Russian line, within the chapter and against every other finished pi-6
    chapter (and the sample)."""
    mine = {}
    for p, r in zip(src.split("\n"), ru.split("\n")):
        pb, rb = B.ID_ANY.sub("", p).strip(), B.ID_ANY.sub("", r).strip()
        if pb in mine:
            assert mine[pb] == rb, f"inconsistent within {CHAPTER}: {pb!r}"
        mine[pb] = rb
    shared, files = 0, set()
    for f in sorted(B.OUT_DIR.glob("*.md")):
        if f.name == CHAPTER or not (B.PALI_DIR / f.name).exists():
            continue
        for p, r in zip((B.PALI_DIR / f.name).read_text(encoding="utf-8").split("\n"),
                        f.read_text(encoding="utf-8").split("\n")):
            pb, rb = B.ID_ANY.sub("", p).strip(), B.ID_ANY.sub("", r).strip()
            if pb and pb in mine:
                assert mine[pb] == rb, f"differs from {f.name}: {pb!r}\n  {rb!r}\n  {mine[pb]!r}"
                shared += 1
                files.add(f.name)
    return shared, sorted(files)


def probe():
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    for n, line in enumerate(src.split("\n"), 1):
        body, bid = B.ID_RE.match(line).groups()
        try:
            print(n, tr_line(body) + (bid or ""))
        except Exception as e:  # noqa: BLE001
            print(n, "FAIL", type(e).__name__, str(e)[:300])


def main():
    B.check_crossbook()
    D.check_crossbook()
    D.check_crossbook(I.A.CROSSBOOK)
    D.check_crossbook(I.CROSSBOOK)
    D.check_crossbook(P2.CROSSBOOK)
    D.check_crossbook(P3.CROSSBOOK)
    D.check_crossbook(CROSSBOOK)
    I.check_members()
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    ru = translate_text(src)
    B.check_pair(src, ru, CHAPTER)
    same = check_with_10_03(src)
    shared, files = check_against_finished(src, ru)
    cmp = {mod: compare_lines(mod, src, ru) for mod in ("build_10-05_ru", "build_10-06_ru")}
    print("same lines as the parallel Indriya builders:",
          {k: (v[0] if v else "not found") for k, v in cmp.items()})
    with open(B.OUT_DIR / CHAPTER, "w", encoding="utf-8", newline="\n") as f:
        f.write(ru)
    print("written", B.OUT_DIR / CHAPTER, "lines", len(ru.split("\n")),
          f"| {same} segments identical with build_10-03_ru | lines shared with finished chapters: {shared}", files)
    for s in dict.fromkeys(SLIP_LOG + P3.SLIP_LOG + P2.SLIP_LOG + I.SLIP_LOG + D.SLIP_LOG):
        print("slip:", s)
    print("cross-book asserts OK; member asserts OK; per-line checks OK; consistency OK")


if __name__ == "__main__":
    if "--probe" in sys.argv:
        probe()
    elif "--compare" in sys.argv:
        _src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
        _ru = translate_text(_src)
        for _mod in ("build_10-05_ru", "build_10-06_ru"):
            _res = compare_lines(_mod, _src, _ru, strict=False)
            print(_mod, "not found" if _res is None else f"same {_res[0]}, differ {len(_res[1])}")
            for _p, _r, _t in (_res[1] if _res else []):
                print(" P", _p, "\n M", _r, "\n T", _t)
    else:
        main()
