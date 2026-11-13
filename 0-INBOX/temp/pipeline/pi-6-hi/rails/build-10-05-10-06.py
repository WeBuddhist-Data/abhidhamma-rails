"""pi-6 Indriyayamaka 10-05 / 10-06 (Atīta (Ga..Ca), Anāgata) Pāli -> Hindi plain RAILS.

Imports build_rails_sample.py read-only (constants and helpers); adds the faculty table and the being
phrases of these two files (see notes-10-05-10-06.md). Every sentence must match a formula, otherwise
ValueError. Writes only AI_translation\\hindi\\pi-6-hindi-plain-rails_split_chapters\\10-05 / 10-06.
usage: python -I -X utf8 build-10-05-10-06.py [--dry]
"""
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\rails")
import build_rails_sample as S  # noqa: E402  (read-only)

FILES = ["10-05-indriyayamaka.md", "10-06-indriyayamaka.md"]

# ---------------------------------------------------------------------------------------------------
# Faculties (termbase; indriya = «क्षमता», feminine)
# ---------------------------------------------------------------------------------------------------
FACULTY = {
    "cakkhundriya": "आँख की क्षमता",
    "sotindriya": "कान की क्षमता",
    "ghānindriya": "नाक की क्षमता",
    "jivhindriya": "जीभ की क्षमता",
    "kāyindriya": "शरीर की क्षमता",
    "manindriya": "मन की क्षमता",
    "itthindriya": "स्त्रीत्व की क्षमता",
    "purisindriya": "पुरुषत्व की क्षमता",
    "jīvitindriya": "जीवन-क्षमता",
    "sukhindriya": "सुख की क्षमता",
    "dukkhindriya": "दुःख की क्षमता",
    "somanassindriya": "प्रसन्नता की क्षमता",
    "domanassindriya": "उदासी की क्षमता",
    "upekkhindriya": "समभाव की क्षमता",
    "saddhindriya": "श्रद्धा की क्षमता",
    "vīriyindriya": "उत्साह की क्षमता",
    "satindriya": "सजगता की क्षमता",
    "samādhindriya": "एकाग्रता की क्षमता",
    "paññindriya": "प्रज्ञा की क्षमता",
}
G = "f"
_F = "|".join(sorted(FACULTY, key=len, reverse=True))
_FCI = "|".join(sorted({k[0].upper() + k[1:] for k in FACULTY} | set(FACULTY), key=len, reverse=True))

# label closing a cycle: (Cakkhundriyamūlakaṃ) = (आँख की क्षमता पर आधारित)  [termbase]
MULAKA = "({f} पर आधारित)"

# ---------------------------------------------------------------------------------------------------
# Being phrases new in these files (notes-10-05-10-06.md)
# ---------------------------------------------------------------------------------------------------
SEX = {"purisā": ("जो पुरुष", "इसी लिंग में", "पाएँगे"),           # eteneva bhāvena (as 10-12)
       "itthiyo": ("जो स्त्रियाँ", "इसी लिंग में", "पाएँगी")}
KATICI = "कुछ जन्म बिताकर"                       # katici bhave dassetvā
WITH_FEELING = {"upekkhāya": "समभाव के साथ", "somanassena": "प्रसन्नता के साथ"}
ORGAN_HAVING = {"sacakkhukā": "आँख वाले", "saghānakā": "नाक वाले"}   # harmonise I1
UPAPAJJITVA = "जन्म लेकर"
PARINIBBAYISSANTI_M = "पूर्ण निर्वाण पाएँगे"
ANANTARA = "जिनमें इस मन के ठीक बाद {x} उत्पन्न होगा, उनमें"       # harmonise B6
PACCHIMACITTA = {"upekkhā": "समभाव से जुड़ा अंतिम मन", "somanassa": "प्रसन्नता से जुड़ा अंतिम मन"}
SUDDHAVASA_DUTIYE = "शुद्ध निवास लोक के प्राणियों में दूसरे मन के चलते समय"   # harmonise B4
SUDDHAVASA_UPAPATTI = "शुद्ध निवास लोक के प्राणियों में जन्म के मन के उत्पन्न होने के क्षण में"
SUDDHAVASA_UPAPAJJ = "शुद्ध निवास लोक में जन्म लेने वालों में"
CATUPANCA_BEINGS = "चार या पाँच समूहों वाले अस्तित्व के प्राणियों में"        # harmonise I3
PACCHIMACITTASAMANGI = "अंतिम मन से युक्त लोगों में"
OR = " या "   # several accusative places of rebirth in one relative clause


def _ye_place(feeling, places):
    """Ye [somanassena] X [Y] upapajjitvā parinibbāyissanti tesaṃ."""
    names = [S.PLACE_NOUN[S.PLACE_FORMS[p][0]] for p in places]
    if [S.PLACE_FORMS[p][0] for p in places] == ["catuvokāra", "pañcavokāra"]:
        names = [S.PLACE_NOUN["catupañcavokāra"]]
    pl = OR.join(names)
    if feeling:
        return f"जो {WITH_FEELING[feeling]} {pl} में {UPAPAJJITVA} {PARINIBBAYISSANTI_M}, उनमें"
    return S.YE_PARINIBBAYISSANTI.format(place=pl)


def _ye_sex(sex, feeling):
    rel, bhava, verb = SEX[sex]
    mid = f" फिर {WITH_FEELING[feeling]} {UPAPAJJITVA}" if feeling else ""
    return f"{rel} {bhava} {KATICI}{mid} पूर्ण निर्वाण {verb}, उनमें"


def _ye_organ(organ, feeling):
    return f"जो {ORGAN_HAVING[organ]} {WITH_FEELING[feeling]} {UPAPAJJITVA} {PARINIBBAYISSANTI_M}, उनमें"


_PLACE_ACC = "|".join(k for k, (_, c) in S.PLACE_FORMS.items() if c == "acc")
PHRASES = [
    (re.compile(r"(?:ye|yā)(?: ca)? (purisā|itthiyo) eteneva bhāvena katici bhave dassetvā "
                r"(?:(upekkhāya|somanassena) upapajjitvā )?parinibbāyissanti"),
     lambda m: _ye_sex(m.group(1), m.group(2))),
    (re.compile(r"ye(?: ca)? (sacakkhukā|saghānakā) (upekkhāya|somanassena) upapajjitvā parinibbāyissanti"),
     lambda m: _ye_organ(m.group(1), m.group(2))),
    (re.compile(rf"ye(?: ca)? (?:(somanassena|upekkhāya) )?((?:(?:{_PLACE_ACC}) )+)upapajjitvā parinibbāyissanti"),
     lambda m: _ye_place(m.group(1), m.group(2).split())),
    (re.compile(r"yassa cittassa anantarā (upekkhā|somanassa)sampayuttapacchimacittaṃ uppajjissati"),
     lambda m: ANANTARA.format(x=PACCHIMACITTA[m.group(1)])),
    (re.compile(r"suddhāvāsānaṃ dutiye citte vattamāne"), lambda m: SUDDHAVASA_DUTIYE),
    (re.compile(r"suddhāvāsānaṃ upapatticittassa uppādakkhaṇe"), lambda m: SUDDHAVASA_UPAPATTI),
    (re.compile(r"suddhāvāsānaṃ upapajjantānaṃ"), lambda m: SUDDHAVASA_UPAPAJJ),
    (re.compile(r"catuvokārānaṃ pañcavokārānaṃ"), lambda m: CATUPANCA_BEINGS),
    (re.compile(r"pacchimacittasamaṅgīnaṃ?"), lambda m: PACCHIMACITTASAMANGI),
]


def who(s):
    """Being chain before tesaṃ / tāsaṃ -> Hindi; every chunk ends in «में», last joined with « और »."""
    s = s[0].lower() + s[1:]
    if s == "itaresaṃ":
        return S.ITARESAM_ALONE
    chunks_hi = {}

    def put(txt):
        tok = f"§{len(chunks_hi)}"
        chunks_hi[tok] = txt
        return tok
    for rx, fn in PHRASES:
        s = rx.sub(lambda m: put(fn(m)), s)
    chunks, pre = [], []
    for w in s.split():
        if w in chunks_hi:
            chunks.append(" ".join(pre + [chunks_hi[w]]))
            pre = []
        elif w == "itaresaṃ":
            pre.append(S.ITARESAM)
        elif w in S.BEINGS:
            chunks.append(" ".join(pre + [S.BEINGS[w]]))
            pre = []
        elif w == "pacchimabhavikānaṃ":
            chunks.append(" ".join(pre + [S.PARTICIPLES[w]]))
            pre = []
        else:
            raise ValueError(f"who: unknown token {w!r} in {s!r}")
    if pre or not chunks:
        raise ValueError(f"who: dangling in {s!r}")
    # relative clauses («जो …, उनमें») at the end of a chain share the one correlative (one tesaṃ in the
    # Pāli): «A में, जो X … पाएँगे और जो Y … पाएँगे, उनमें» (as 10-09 / 10-12)
    tail = ", उनमें"
    n_rel = 0
    while n_rel < len(chunks) and chunks[-1 - n_rel].startswith("जो ") and chunks[-1 - n_rel].endswith(tail):
        n_rel += 1
    if n_rel > 1:
        chunks = chunks[:-n_rel] + [c[: -len(tail)] for c in chunks[-n_rel:]]
    if len(chunks) == 1:
        out = chunks[0]
    else:
        out = S.JOIN.join(chunks[:-1]) + S.JOIN_LAST + chunks[-1]
    return out + tail if n_rel > 1 else out


# ---------------------------------------------------------------------------------------------------
# Sentences
# ---------------------------------------------------------------------------------------------------
VERB_TOK = {"uppajjittha": "uppajjittha", "uppajjissati": "uppajjissati",
            "upapajjissati": "uppajjissati"}   # 10-06 ^6-10-309: «na upapajjissati», source slip
SLIPS = []


def verb(tok, flip=False):
    neg = tok.startswith("na ")
    w = tok[3:] if neg else tok
    if w not in VERB_TOK:
        raise ValueError(f"verb {tok}")
    if VERB_TOK[w] != w:
        SLIPS.append(tok)
    pos, negs = S.VERBS[(VERB_TOK[w], G)]
    return negs if (neg != flip) else pos


def fac(w):
    m = re.fullmatch(rf"({_FCI})(?:ṃ|ñca|ṃ ca)", w)
    if not m:
        raise ValueError(f"faculty {w}")
    k = m.group(1)
    return FACULTY[k[0].lower() + k[1:]]


def fac_list(s):
    """'saddhindriyaṃ…pe… paññindriyaṃ…pe… manindriyaṃ' -> Hindi, keeping the «…» and spaces."""
    parts = re.split(r"(…pe…|…)", s)
    out = []
    for p in parts:
        if p in ("…pe…", "…"):
            out.append("…")
        elif p.strip():
            lead = " " if p.startswith(" ") else ""
            trail = " " if p.endswith(" ") else ""
            out.append(lead + fac(p.strip()) + trail)
        else:
            out.append(p)
    return "".join(out)


_V = r"((?:na )?(?:uppajjittha|uppajjissati|upapajjissati))"
_FL = rf"((?:{_FCI})ṃ(?:(?:…pe…| ?…) ?(?:{_FCI})ṃ)*)"
Q_RE = re.compile(rf"(?:\((Ka|Kha)\) )?(yassa vā pana yattha|yassa yattha|yassa vā pana|yassa|yattha vā pana|yattha) "
                  rf"{_FL} {_V} (tassa tattha|tassa|tattha) {_FL} ((?:na )?(?:uppajjitth|uppajjissat))(?:āti|īti)\?", re.I)
REL_FIX = {("yassa vā pana", "tattha"): "tassa"}   # 10-05 ^6-10-240 line 6: «yassa vā pana … tattha», source slip


def question(s):
    m = Q_RE.fullmatch(s)
    if not m:
        return None
    lab, rel, f1, v1, cor, f2, v2 = m.groups()
    v2 += "a" if v2.endswith("h") else "i"   # uppajjitthāti -> uppajjittha, uppajjissatīti -> uppajjissati
    rel_l = rel.lower()
    if (rel_l, cor) in REL_FIX:
        SLIPS.append(s)
        cor = REL_FIX[(rel_l, cor)]
    rel_hi, cor_hi = S.REL_FRAMES[(rel_l, cor)]
    label = (S.LABELS[f"({lab})"] + " ") if lab else ""
    return f"{label}{rel_hi} {fac_list(f1)} {verb(v1)}, क्या {cor_hi} {fac_list(f2)} {verb(v2)}?"


_COR = r"(tesaṃ tattha|tāsaṃ tattha|tesaṃ|tāsaṃ|tattha)"
_FW = rf"((?:{_FCI})ṃ)"
_FCA = rf"((?:{_FCI})(?:ñca|ṃ ca))"
BUT_RE = re.compile(rf"(.+?) {_COR} {_FW} {_V},? no ca {_COR} {_FW} {_V}\.")
BOTH_RE = re.compile(rf"(.+?) {_COR} {_FCA} {_V} {_FCA} {_V}\.")


def frames(cor):
    if cor == "tattha":
        return "place"
    return "beings_t" if cor.endswith("tattha") else "beings"


def answer(s):
    m = BUT_RE.fullmatch(s)
    if m:
        wh, c1, f1, v1, c2, f2, v2 = m.groups()
        kw = dict(k1=fac(f1), v1=verb(v1), k2=fac(f2), v2=verb(v2, flip=True))
        fr = frames(c1)
        if fr == "place":
            return S.BUT_PLACE.format(place=S.place(wh), **kw)
        return (S.BUT_BEINGS_T if fr == "beings_t" else S.BUT_BEINGS).format(who=who(wh), **kw)
    m = BOTH_RE.fullmatch(s)
    if m:
        wh, c1, f1, v1, f2, v2 = m.groups()
        kw = dict(k1=fac(f1), v1=verb(v1), k2=fac(f2), v2=verb(v2))
        fr = frames(c1)
        if fr == "place":
            return S.BOTH_PLACE.format(place=S.place(wh), **kw)
        return (S.BOTH_BEINGS_T if fr == "beings_t" else S.BOTH_BEINGS).format(who=who(wh), **kw)
    return None


SHORT = {
    "Āmantā.": S.AMANTA,
    "Natthi.": S.NATTHI,
    "No.": S.NO,
    "Āmantā …pe….": "हाँ …।",
    "Natthi …pe….": "ऐसा कोई नहीं है …।",
    "Uppajjittha.": S.VERBS[("uppajjittha", G)][0] + "।",
    "Uppajjissati.": S.VERBS[("uppajjissati", G)][0] + "।",
}


def sentence(s):
    if s in SHORT:
        return SHORT[s]
    m = re.fullmatch(rf"\(({_FCI})mūlakaṃ\)", s)
    if m:
        k = m.group(1)
        return MULAKA.format(f=FACULTY[k[0].lower() + k[1:]])
    r = question(s) or answer(s)
    if r:
        return r
    raise ValueError(f"no formula for: {s}")


# source slip 10-06 ^6-10-301: a full stop inside the «both» clause («…uppajjissati. Somanassindriyañca …»)
LINE_FIX = {"itthindriyañca uppajjissati. Somanassindriyañca uppajjissati.":
            "itthindriyañca uppajjissati somanassindriyañca uppajjissati."}
_SPLIT = re.compile(r"(?<=[.?]) (?=[A-ZĀĪŪṬḌṆÑṄ(])")


def text_line(line):
    for a, b in LINE_FIX.items():
        if a in line:
            SLIPS.append(a)
            line = line.replace(a, b)
    return " ".join(sentence(s) for s in _SPLIT.split(line))


def translate_line(line):
    bid = ""
    m = S.ID_RE.search(line)
    if m:
        bid = " " + m.group(1)
        line = line[: m.start()]
    if line.startswith("#"):
        hashes, text = line.split(" ", 1)
        return f"{hashes} {S.HEADINGS[text.strip()]}{bid}"
    return text_line(line.strip()) + bid


def translate_text(text):
    out, prev_blank = [], True
    for line in text.splitlines():
        if not line.strip():
            if not prev_blank:
                out.append("")
            prev_blank = True
            continue
        out.append(translate_line(line))
        prev_blank = False
    while out and out[-1] == "":
        out.pop()
    return "\n".join(out) + "\n"


def main():
    dry = "--dry" in sys.argv
    for f in FILES:
        src = (S.PALI_DIR / f).read_text(encoding="utf-8")
        hi = translate_text(src)
        if not dry:
            (S.HI_DIR / f).write_text(hi, encoding="utf-8", newline="\n")
        print(f, "lines", len([l for l in hi.splitlines() if l.strip()]))
    print("slips:", *sorted(set(SLIPS)), sep="\n  ")


if __name__ == "__main__":
    main()
