"""Russian plain zero-shot of pi-6 (Yamaka): chapter 10-02-indriyayamaka.md (Indriyayamaka: suddhindriya-
mūlacakka of the paṇṇattivāra, then the pavattivāra, uppādavāra, present tense, persons and places).

Members, family A frames and the line driver come from build_10-01_ru (imported, never edited); the Āyatana
person descriptors (sacakkhuka / acakkhuka …), REBORN and the place intro from build_3-01_ru; the joining of
person / time intros, «в течение жизни», the moments and «не связанного с» from build_5-01_ru (moments of
build_8_ru); the person / place shape from build_7-01_ru; family B (verbs, PV_S1_RE / PV_S2_RE, PV_PRED, the
negative frames) from build_2-01_ru.

NEW here (listed in notes-10-02.md) and exposed for 10-03 … 10-13:
  IN_ATTR          person attributes of the Indriya pavattivāra (itthīnaṃ «женщиной», na itthīnaṃ «не женщиной»,
                   somanassena «с радостью», vinā upekkhāya «без невозмутимости», sahetukānaṃ «с корнями»,
                   ñāṇasampayuttānaṃ «со знанием» …); IN_ATTR_FRONT (the gender ones, said first)
  IN_HAVE2         IN_HAVE + jivhak / kāyak (sa-X-ka / a-X-ka)
  IN_ASSOC         members of the -sampayutta / -vippayutta minds (somanassa «радостью», upekkhā, saddhā, ñāṇa)
  IN_PERSON_VERB   upapajjantānaṃ / cavantānaṃ -> «тех, кто перерождается / умирает {desc}»
  in_units(), in_intro(), in_pv_sentence(), chain_question(), segments(), tr_line(), translate_text(), IN2_CFG

Run:    python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_10-02_ru.py
Probe:  python -I -X utf8 -B 0-INBOX\\temp\\pipeline\\pi-6-ru\\build_10-02_ru.py --probe 10-03-indriyayamaka.md
Import: J = importlib.import_module("build_10-02_ru")   (importing never writes any file)
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

I = importlib.import_module("build_10-01_ru")    # Indriya members, family A additions, line driver
S = importlib.import_module("build_5-01_ru")     # intro joining, pavatte, moments, «не связанного с»
A, D, C = I.A, I.D, I.C                          # build_3-01_ru, build_2-01_ru, build_7-01_ru
CHAPTER = "10-02-indriyayamaka.md"
cap, lower1 = B.cap, C.lower1
SLIP_LOG = []

# =============================================================================================
# Persons of the Indriya pavattivāra
# =============================================================================================
IN_HAVE2 = dict(I.IN_HAVE)
IN_HAVE2.update({"jivhak": ("языком", "языка"), "kāyak": ("телом", "тела")})

# Members of the associated minds (instrumental after «связанного с / не связанного с»; pi-1 «связанный со
# знанием», «сопровождаемый радостью / невозмутимостью»; saddhā «вера» pi-1)
IN_ASSOC = {"somanassa": "радостью", "upekkhā": "невозмутимостью", "saddhā": "верой", "ñāṇa": "знанием"}
assert S.VIPPAYUTTA == "не связанного с"
VIPP = S.VIPPAYUTTA[:-2]                   # «не связанного»
SAMP = VIPP[len("не "):]                   # «связанного»
WITHOUT = "без "                           # as 3-01 have_desc («без глаза»)

# Person attributes (Pāli token(s) -> Russian descriptor after «тех, кто перерождается»). Prepositional ones
# keep the Pāli order and are joined by A.HAVE_JOIN « и » (3-01). itthīnaṃ / purisānaṃ («перерождается
# женщиной», instrumental) are said first, so that «с глазом и женщиной» (= "with an eye and a woman") never occurs.
IN_ATTR = {
    "itthīnaṃ": "женщиной", "na itthīnaṃ": "не женщиной",
    "purisānaṃ": "мужчиной", "na purisānaṃ": "не мужчиной",
    "somanassena": A.s_prep(IN_ASSOC["somanassa"]), "vinā somanassena": WITHOUT + "радости",
    "upekkhāya": A.s_prep(IN_ASSOC["upekkhā"]), "vinā upekkhāya": WITHOUT + "невозмутимости",
    "sahetukānaṃ": A.s_prep("корнями"), "ahetukānaṃ": WITHOUT + "корней",            # pi-1 «имеющие корни»
    "ñāṇasampayuttānaṃ": A.s_prep(IN_ASSOC["ñāṇa"]), "ñāṇavippayuttānaṃ": WITHOUT + "знания",
}
IN_ATTR_FRONT = {"itthīnaṃ", "na itthīnaṃ", "purisānaṃ", "na purisānaṃ"}
IN_PERSON_VERB = {
    "upapajjantānaṃ": A.REBORN,                                         # «тех, кто перерождается {desc}»
    "cavantānaṃ": A.REBORN.replace("перерождается", "умирает"),        # 3-04 «тех, кто умирает с глазом …»
}
FEM = {"upapajjantīnaṃ": "upapajjantānaṃ", "cavantīnaṃ": "cavantānaṃ", "tāsaṃ": "tesaṃ", "Tāsaṃ": "Tesaṃ"}

MOMENT_RE = re.compile(r"((?:(?:" + "|".join(IN_ASSOC) + r")(?:sampayutta|vippayutta))*)(pacchima)?cittassa")
ASSOC_RE = re.compile(r"(" + "|".join(IN_ASSOC) + r")(sampayutta|vippayutta)")
KHANA = {"uppādakkhaṇe": S.UPPADA, "bhaṅgakkhaṇe": S.BHANGA}
PACCHIMA_G = "последнего "                 # pacchimacitta «последний ум» (8, 6-01)


def moment(word, khana):
    """'somanassasampayuttasaddhāvippayuttacittassa' + 'uppādakkhaṇe' -> (Russian, kind)."""
    m = MOMENT_RE.fullmatch(word)
    if not m:
        return None
    mind = (PACCHIMA_G if m.group(2) else "") + S.CITTA_G
    assoc = [(SAMP if k == "sampayutta" else VIPP) + " " + A.s_prep(IN_ASSOC[a])
             for a, k in ASSOC_RE.findall(m.group(1))]
    if not assoc:
        return f"{KHANA[khana]} {mind}", "adv"
    return f"{KHANA[khana]} {mind}, " + " и ".join(assoc), "advc"


def _attr_at(toks, i):
    for n in (2, 1):
        key = " ".join(toks[i:i + n])
        if len(toks[i:i + n]) == n and key in IN_ATTR:
            return IN_ATTR[key], key in IN_ATTR_FRONT, n
    d = A.have_desc(toks[i], IN_HAVE2)
    if d:
        return d, False, 1
    return None


def in_units(intro):
    """'Sacakkhukānaṃ na itthīnaṃ upapajjantānaṃ' / '… pavatte …cittassa uppādakkhaṇe' -> [[russian, kind]]."""
    toks = lower1(intro).split()
    units, i = [], 0
    while i < len(toks):
        if toks[i] == "pavatte":
            units.append([S.PAVATTE, "loc"])
            i += 1
            continue
        if i + 1 < len(toks) and toks[i + 1] in KHANA:
            mo = moment(toks[i], toks[i + 1])
            if mo:
                units.append(list(mo))
                i += 2
                continue
        front, rest = [], []
        while i < len(toks):
            a = _attr_at(toks, i)
            if not a:
                break
            (front if a[1] else rest).append(a[0])
            i += a[2]
        if (front or rest) and i < len(toks) and toks[i] in IN_PERSON_VERB:
            units.append([IN_PERSON_VERB[toks[i]].format(desc=A.HAVE_JOIN.join(front + rest)), "rel"])
            i += 1
            continue
        raise ValueError(f"intro not parsed at {toks[i:]!r} in {intro!r}")
    return units


def in_intro(intro, tattha=False):
    """Joined exactly as build_5-01_ru.pv_intro (same kinds, same separators), with the Indriya units."""
    items, prev = [], None
    for ru, kind in in_units(intro):
        if kind in S.PERSON_KINDS:
            ru = "у " + ru
        attach = prev is not None and prev in ("noun", "loc") and kind not in S.PERSON_KINDS
        if attach and items:
            items[-1].append((ru, kind))
        else:
            items.append([(ru, kind)])
        prev = kind
    persons = any(k in S.PERSON_KINDS for it in items for _, k in it)

    def render(item):
        s = item[0][0]
        for (_, pk), (ru, k) in zip(item, item[1:]):
            s += (", " if (pk in S.CLOSES or k in S.OPENS) else " ") + ru
        return s

    out = render(items[0])
    for i in range(1, len(items)):
        pc = items[i - 1][-1][1] in S.CLOSES
        out += ((", и " if pc else " и ") if i == len(items) - 1 else ", ") + render(items[i])
    if items[-1][-1][1] in S.CLOSES:
        out += ","
    if not persons:
        out += " " + S.WHO_TESAM
    if tattha:
        out += " " + S.TAM
    return cap(out) + " "


def fem_norm(s):
    for a, b in FEM.items():
        s = re.sub(rf"\b{a}\b", b, s)
    return s


def in_pv_sentence(s, subj=None):
    """One Pāli pavatti answer sentence (no final '.') -> Russian with '.' (tail frames as build_5-01_ru)."""
    subj = I.IN_PV_SUBJ if subj is None else subj
    s = fem_norm(D._norm(s))
    for rx, kind in ((D.PV_S1_RE, 1), (D.PV_S2_RE, 2)):
        m = rx.fullmatch(s)
        if not m:
            continue
        if m.group("t1").startswith("tesaṃ"):
            head = in_intro(m.group("intro"), "tattha" in m.group("t1"))
        else:
            head = A.ay_place_intro(m.group("intro"), I.IN_PLANES)
        x, y = subj[m.group("x")], subj[m.group("y")]
        p1 = D.PV_PRED.format(v=D.verb(m.group("v1"), x["g"], bool(m.group("n1"))), x=x["nom"])
        if kind == 1:
            res = C.RES[m.group("t2")]
            v2 = D.verb(m.group("v2"), y["g"], not m.group("n2"))
            tail = (D.PV_NO_CA_POS_FRAME if m.group("n2") else C.NO_CA_FRAME).format(
                res=res, **{("pred" if m.group("n2") else "neg_pred"): D.PV_PRED.format(v=v2, x=y["nom"])})
            return cap(head + p1 + tail) + "."
        if m.group("n1") and m.group("n2"):
            f1, f2 = D.verb(m.group("v1"), x["g"]), D.verb(m.group("v2"), y["g"])
            both = (D.PV_NEITHER_FRAME.format(v=f1, x=x["nom"], y=y["nom"]) if f1 == f2
                    else D.PV_NEG_MIXED_FRAME.format(v1=f1, x=x["nom"], v2=f2, y=y["nom"]))
            return cap(head + both) + "."
        p2 = D.PV_PRED.format(v=D.verb(m.group("v2"), y["g"], bool(m.group("n2"))), x=y["nom"])
        return cap(head + C.BOTH_FRAME.format(p1=p1, p2=p2)) + "."
    raise ValueError(f"pavatti answer not parsed: {s!r}")


# =============================================================================================
# Questions asked in turn: "Yattha X uppajjati tattha Y…pe… Z…pe… W uppajjatīti?"
# (as 3-01: «Где возникает X, там возникает Y… Z… W?»; the verb once, before the first member)
# =============================================================================================
CHAIN_RE = re.compile(r"(?P<rel>[Yy]assa vā pana|[Yy]assa|[Yy]attha vā pana|[Yy]attha) (?P<x>\S+) (?P<n1>na |n)?"
                      r"(?P<v1>" + D.V_RE + r") (?P<cor>tassa|tattha) (?P<ys>(?:\S+…pe… )+\S+) (?P<n2>na |n)?"
                      r"(?P<v2>" + D.VTI_RE + r")\?")


def chain_question(m, subj=None):
    subj = I.IN_PV_SUBJ if subj is None else subj
    rel = m.group("rel").lower()
    kind = "yassa" if rel.startswith("yassa") else "yattha"
    x = subj[m.group("x")]
    ys = [subj[w] for w in m.group("ys").split("…pe… ")]
    p1 = D.PV_PRED.format(v=D.verb(m.group("v1"), x["g"], bool(m.group("n1"))), x=x["nom"])
    p2 = D.PV_PRED.format(v=D.verb(D.PV_VERB_TI[m.group("v2")], ys[0]["g"], bool(m.group("n2"))),
                          x="… ".join(y["nom"] for y in ys))
    q = D.PV_Q[kind].format(p1=p1, p2=p2)
    return (D.PV_KHA + lower1(q)) if "vā pana" in rel else q


# =============================================================================================
# Line segments (as build_10-01_ru.segments, plus chain questions and the pavatti answers)
# =============================================================================================
SEG_RE = I.SEG_RE
ELL_TOK = I.ELL_TOK
CHAIN_TOK = re.compile(r"(\s*)(" + CHAIN_RE.pattern + r")")
PV_MARK = re.compile(r" (?:tesaṃ|tāsaṃ|tattha) ")


def sentence(body, cfg, y):
    if PV_MARK.search(body):
        return in_pv_sentence(body, cfg["pv_subj"])
    return I.in_sentence(body, cfg, y)


def segments(plain, cfg=None):
    cfg = IN2_CFG if cfg is None else cfg
    out, pos, y, first = [], 0, None, True
    while pos < len(plain):
        mc = CHAIN_TOK.match(plain, pos)
        if mc:
            sep = mc.group(1)
            ru = chain_question(CHAIN_RE.fullmatch(mc.group(2)), cfg["pv_subj"])
            pos, y = mc.end(), None
            out.append(sep + (cap(ru) if (first or mc.group(2)[0].isupper()) else lower1(ru)))
            first = False
            continue
        m = SEG_RE.match(plain, pos)
        if not m or m.end() == pos:
            raise ValueError(f"line not segmented at {plain[pos:]!r}")
        sep, tok = m.groups()
        pos = m.end()
        if ELL_TOK.fullmatch(tok):
            ru = "…"
        else:
            if tok.endswith("?"):
                ru, y = I.in_question(tok[:-1], cfg)
            elif tok.endswith("."):
                ru = sentence(tok[:-1], cfg, y)
            else:
                ru = sentence(tok, cfg, y)
                assert ru.endswith("."), ru
                ru = ru[:-1]
            ru = cap(ru) if (first or tok[0].isupper()) else lower1(ru)
        out.append(sep + ru)
        first = False
    return "".join(out)


def tr_line(text, cfg=None):
    """Translate one Pāli line (block ID removed): build_10-01_ru.tr_line with this module's segments."""
    cfg = IN2_CFG if cfg is None else cfg
    if not text.strip():
        return ""
    if text in cfg["fixed"]:
        return cfg["fixed"][text]
    if text in B.FIXED:
        return B.FIXED[text]
    if text.startswith("#"):
        return I.heading(text, cfg.get("headings"))
    text = I.preprocess(text)
    m = I.TAIL_RE.fullmatch(text)
    if m:
        return tr_line(m.group(1), cfg) + f" ({I.TAILS[m.group(2)]}){m.group(3)}"
    label = ""
    m = I.LABEL_RE.fullmatch(text)
    if m and m.group(1) in B.LETTERS:
        label, text = f"({B.LETTERS[m.group(1)]}) ", m.group(2)
        if m.group(1) == "Ka" and " vā pana " in text:
            SLIP_LOG.append(f"label (Ka) on a 'vā pana' question (kept as written): {text[:60]}")
    if re.match(r"indriyaṃ \S+indriyanti\?", text):
        SLIP_LOG.append(f"singular 'indriyaṃ' in a (Kha) suddhindriya question (kept as written): {text}")
    variants = D.VARIANT_RE.findall(text)
    ru = segments(D.VARIANT_RE.sub("", text), cfg)
    for v in variants:
        anchor = cfg["variant_anchors"][v]
        assert anchor in ru, (anchor, ru)
        kind = cfg.get("variant_kind", {}).get(v, D.VARIANT_KIND_DEFAULT)
        ru = ru.replace(anchor, anchor + " " + D.variant_ru(v, kind), 1)
    return label + ru


def translate_text(src, cfg=None):
    out = []
    for line in src.split("\n"):
        body, bid = B.ID_RE.match(line).groups()
        out.append(tr_line(body, cfg) + (bid or ""))
    return unicodedata.normalize("NFC", "\n".join(out))


IN2_CFG = dict(I.IN_CFG)
IN2_CFG.update({"have": IN_HAVE2, "fixed": dict(I.IN_CFG["fixed"]), "variant_anchors": dict(I.IN_CFG["variant_anchors"])})

# =============================================================================================
# Checks
# =============================================================================================
CROSSBOOK = [   # strings taken from the approved pi-1 … pi-5 Russian rails (book, exact substring)
    ("1", "связанный со знанием"), ("1", "не связанный со знанием"), ("1", "сопровождаемый радостью"),
    ("1", "сопровождаемый невозмутимостью"), ("1", "имеющие корни"), ("1", "не имеющие корней"),
    ("1", "без корней"), ("1", "с корнями"), ("1", "со знанием"), ("2", "с радостью"), ("1", "знание"),
    ("1", "вера"), ("1", "радость"), ("1", "невозмутимость"), ("2", "перерождаются"), ("1", "в мире форм"),
    ("1", "в мире чувственных желаний"), ("1", "в мире без форм"), ("5", "женщиной"), ("4", "мужчиной"),
]


def check_against_finished(src, ru):
    """Identical Pāli line = identical Russian line, against every other finished pi-6 chapter (and the sample)."""
    mine = {}
    for p, r in zip(src.split("\n"), ru.split("\n")):
        pb, rb = B.ID_ANY.sub("", p).strip(), B.ID_ANY.sub("", r).strip()
        if pb in mine:
            assert mine[pb] == rb, f"inconsistent within {CHAPTER}: {pb!r}"
        mine[pb] = rb
    shared = 0
    for f in sorted(B.OUT_DIR.glob("*.md")):
        if f.name == CHAPTER or not (B.PALI_DIR / f.name).exists():
            continue
        for p, r in zip((B.PALI_DIR / f.name).read_text(encoding="utf-8").split("\n"),
                        f.read_text(encoding="utf-8").split("\n")):
            pb, rb = B.ID_ANY.sub("", p).strip(), B.ID_ANY.sub("", r).strip()
            if pb and pb in mine:
                assert mine[pb] == rb, f"differs from {f.name}: {pb!r}\n  {rb!r}\n  {mine[pb]!r}"
                shared += 1
    return shared


def probe(name):
    src = (B.PALI_DIR / name).read_text(encoding="utf-8")
    ok = bad = 0
    for line in src.split("\n"):
        body, _ = B.ID_RE.match(line).groups()
        try:
            tr_line(body)
            ok += 1
        except Exception as e:   # noqa: BLE001
            bad += 1
            print("-- ", type(e).__name__, str(e)[:200])
    print(f"{name}: {ok} lines translated, {bad} not covered")


def main():
    B.check_crossbook()
    D.check_crossbook()
    D.check_crossbook(A.CROSSBOOK)
    D.check_crossbook(I.CROSSBOOK)
    D.check_crossbook(CROSSBOOK)
    I.check_members()
    src = (B.PALI_DIR / CHAPTER).read_text(encoding="utf-8")
    ru = translate_text(src)
    B.check_pair(src, ru, CHAPTER)
    shared = check_against_finished(src, ru)
    with open(B.OUT_DIR / CHAPTER, "w", encoding="utf-8", newline="\n") as f:
        f.write(ru)
    print("written", B.OUT_DIR / CHAPTER, "lines", len(ru.split("\n")), "| lines shared with finished chapters:", shared)
    for s in dict.fromkeys(SLIP_LOG + I.SLIP_LOG):
        print("slip:", s)
    print("cross-book asserts OK; member asserts OK; per-line checks OK; consistency OK")


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "--probe":
        probe(sys.argv[2])
    else:
        main()
