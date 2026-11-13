r"""pi-6 Yamaka, Anusayayamaka 7-01 .. 7-05: Hindi plain zero-shot builder.

usage: python -I -X utf8 build_7a_hi.py [7-01-anusayayamaka.md ...]
Without arguments it builds all five files. Importing the module writes nothing.
Every line is composed from fixed frames (see notes-7a.md); an unknown line raises an error.
"""
import pathlib
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi")
import build_sample_hi as S  # noqa: E402  (import only)

PALI_DIR = S.PALI_DIR
HI_DIR = S.HI_DIR
FILES = [f"7-0{i}-anusayayamaka.md" for i in range(1, 6)]

# ---------------------------------------------------------------- anusayas (pi-2 ^2-949)
ANUSAYA = {
    "kāmarāg": "इंद्रिय-सुखों के राग की सुप्त प्रवृत्ति",
    "kāmārāg": "इंद्रिय-सुखों के राग की सुप्त प्रवृत्ति",   # source spelling slip
    "paṭigh": "चिढ़ की सुप्त प्रवृत्ति",
    "mān": "अहंकार की सुप्त प्रवृत्ति",
    "diṭṭh": "दृष्टि की सुप्त प्रवृत्ति",
    "vicikicch": "संशय की सुप्त प्रवृत्ति",
    "bhavarāg": "अस्तित्व के राग की सुप्त प्रवृत्ति",
    "avijj": "अज्ञान की सुप्त प्रवृत्ति",
}
ANUSAYA_RE = re.compile(r"(kāmarāg|kāmārāg|paṭigh|mān|diṭṭh|vicikicch|bhavarāg|avijj)ānusay(o|ena|aṃ|añca)")
SEVEN = "सात सुप्त प्रवृत्तियाँ"

# ---------------------------------------------------------------- headings
HEADINGS = dict(S.HEADINGS)
HEADINGS.update({
    "Uppattiṭṭhānavāro": "उत्पन्न होने के स्थान का खंड",
    "Mahāvāro 1. anusayavāro": "बड़ा खंड 1. सुप्त प्रवृत्तियों का खंड",
    "Anusayavāra": "सुप्त प्रवृत्तियों का खंड",
    "Sānusayavāro": "सुप्त प्रवृत्ति वाला होने का खंड",
    "Sānusayavāra": "सुप्त प्रवृत्ति वाला होने का खंड",
    "Pajahanavāro": "छोड़ने का खंड",
    "Pajahanavāra": "छोड़ने का खंड",
    "(Gha) paṭilomapuggalo": "(घ) " + S.PATILOMAM + ": " + S.PUGGALO,
    "(Ṅa) paṭilomaokāso": "(ङ) " + S.PATILOMAM + ": " + S.OKASO,
    "(Ca) paṭilomapuggalokāsā": "(च) " + S.PATILOMAM + ": " + S.PUGGALOKASA,
})
VARA = {  # section names, for closing lines and "<X>vāre anulomaṃ / paṭilomaṃ"
    "Anusaya": ("सुप्त प्रवृत्तियों का खंड", "सुप्त प्रवृत्तियों के खंड"),
    "Sānusaya": ("सुप्त प्रवृत्ति वाला होने का खंड", "सुप्त प्रवृत्ति वाला होने के खंड"),
    "Pajahana": ("छोड़ने का खंड", "छोड़ने के खंड"),
    "Pajahanā": ("छोड़ने का खंड", "छोड़ने के खंड"),
    "Uppattiṭṭhāna": ("उत्पन्न होने के स्थान का खंड", "उत्पन्न होने के स्थान के खंड"),
}
PART = {"anulomaṃ": S.ANULOMAM, "paṭilomaṃ": S.PATILOMAM}

FIXED = {
    "Sattānusayā – kāmarāgānusayo, paṭighānusayo, mānānusayo, diṭṭhānusayo, vicikicchānusayo, bhavarāgānusayo, avijjānusayo.":
        SEVEN + " – " + ", ".join(ANUSAYA[k] for k in ("kāmarāg", "paṭigh", "mān", "diṭṭh", "vicikicch", "bhavarāg", "avijj")) + "।",
}
for _p, (_nom, _obl) in VARA.items():
    FIXED[_p + "vāro."] = _nom + "।"
    for _pp, _ph in PART.items():
        FIXED[_p + "vāre " + _pp + "."] = _obl + " का " + _ph + " भाग।"

MULAKA = {"Ekamūlakaṃ": "एक", "Dukamūlakaṃ": "दो", "Tikamūlakaṃ": "तीन", "Catukkamūlakaṃ": "चार",
          "Pañcakamūlakaṃ": "पाँच", "Chakkamūlakaṃ": "छह"}
MULAKA_H = "({N} पर आधारित)"

# ---------------------------------------------------------------- short answers
SHORT = {"Āmantā": S.AMANTA[:-1], "No": "नहीं", "Natthi": "ऐसा नहीं होता"}
PE = "…"

# ---------------------------------------------------------------- persons and places
PERSONS = {  # lower-case Pāli phrase -> Hindi
    # genitive, with anuseti (" … में")
    "anāgāmissa": "फिर न लौटने वाले में",
    "arahato": "अर्हत् में",
    "puthujjanassa": "साधारण व्यक्ति में",
    "dvinnaṃ puggalānaṃ": "दो व्यक्तियों में",
    "tiṇṇaṃ puggalānaṃ": "तीन व्यक्तियों में",
    "catunnaṃ puggalānaṃ": "चार व्यक्तियों में",
    "tesaññeva puggalānaṃ": "उन्हीं व्यक्तियों में",
    "tasseva puggalassa": "उसी व्यक्ति में",
    # nominative
    "anāgāmī": "फिर न लौटने वाला",
    "arahā": "अर्हत्",
    "puthujjano": "साधारण व्यक्ति",
    "dve puggalā": "दो व्यक्ति",
    "tayo puggalā": "तीन व्यक्ति",
    "cattāro puggalā": "चार व्यक्ति",
    "teva puggalā": "वे ही व्यक्ति",
    "sveva puggalo": "वही व्यक्ति",
    "aṭṭhamako": "आठवें स्तर का व्यक्ति",
    "aggamaggasamaṅgī": "सर्वोच्च मार्ग से युक्त व्यक्ति",
}
PLACES = {  # oblique stems; one "में" follows the whole list
    "kāmadhātuyā dvīsu vedanāsu": "इंद्रिय-सुखों के लोक की दो अनुभूतियों",
    "kāmadhātuyā tīsu vedanāsu": "इंद्रिय-सुखों के लोक की तीन अनुभूतियों",
    "dukkhāya vedanāya": "दुःखद अनुभूति",
    "rūpadhātuyā": "सूक्ष्म भौतिक लोक",
    "arūpadhātuyā": "अभौतिक लोक",
    "apariyāpanne": "अस्तित्व के लोकों में न समाई हुई परिघटनाओं",
    "sabbasakkāyapariyāpannesu dhammesu": "व्यक्तिगत अस्तित्व में समाई हुई सभी परिघटनाओं",
}
PLACES["ariyāpanne"] = PLACES["apariyāpanne"]   # source slip in 7-04 for apariyāpanne
SABBATTHA = "सब जगह"
KOI = "कोई"
IN = "में"

# ---------------------------------------------------------------- verbs
# kind, plural?, negative?
VERBS = {
    "anuseti": ("anu", False, False), "nānuseti": ("anu", False, True),
    "anusenti": ("anu", True, False), "anusanti": ("anu", True, False), "nānusenti": ("anu", True, True),
    "sānusayo": ("sa", False, False), "sānusayā": ("sa", True, False),
    "niranusayo": ("nir", False, False), "niranusayā": ("nir", True, False),
    "pajahati": ("paj", False, False), "nappajahati": ("paj", False, True),
    "pajahanti": ("paj", True, False), "nappajahanti": ("paj", True, True),
}
QUOT = {"anusetīti": "anuseti", "anusentīti": "anusenti", "nānusetīti": "nānuseti", "nānusentīti": "nānusenti",
        "sānusayoti": "sānusayo", "niranusayoti": "niranusayo", "pajahatīti": "pajahati",
        "nappajahatīti": "nappajahati"}
NOMINATIVE_KINDS = {"sa", "nir", "paj"}
TADEKATTHA = "उसके साथ जुड़ी होने के कारण"


def pred_h(kind, pl, neg, lst, both=False, tad=False):
    """Hindi predicate: the anusaya list + the verb."""
    bhi = " भी" if both else ""
    if kind == "anu":
        v = ("सोई नहीं रहतीं" if neg else "सोई रहती हैं") if pl else ("सोई नहीं रहती" if neg else "सोई रहती है")
        return f"{lst}{bhi} {v}"
    if kind == "sa":
        adj = "वाले" if pl else "वाला"
        cop = "हैं" if pl else "है"
        return f"{lst} {adj}{bhi} {'नहीं ' if neg else ''}{cop}"
    if kind == "nir":
        cop = "हैं" if pl else "है"
        return f"{lst} से{bhi} मुक्त {'नहीं ' if neg else ''}{cop}"
    if kind == "paj":
        if neg:
            v = "नहीं छोड़ते" if pl else "नहीं छोड़ता"
        else:
            v = "छोड़ते हैं" if pl else "छोड़ता है"
        mid = f" {TADEKATTHA}" if tad else ""
        return f"{lst} को{bhi}{mid} {v}"
    raise KeyError(kind)


def join_list(names):
    """names: Hindi names and PE markers -> one Hindi list."""
    segs, cur = [], []
    for n in names:
        if n is PE:
            segs.append(cur)
            cur = []
        else:
            cur.append(n)
    segs.append(cur)
    out = []
    for seg in segs:
        if len(seg) == 1:
            out.append(seg[0])
        else:
            out.append(", ".join(seg[:-1]) + " और " + seg[-1])
    return (PE + " ").join(out)


# ---------------------------------------------------------------- tokenizer
def tokens(s):
    s = s.replace("…pe…", " PE ")
    return [t for t in s.split() if t]


def parse_preds(toks):
    """Tokens of anusayas / ca / PE / tadekaṭṭhaṃ / verbs -> list of predicates."""
    preds, items, tad = [], [], False
    for t in toks:
        m = ANUSAYA_RE.fullmatch(t[0].lower() + t[1:])
        if m:
            items.append([ANUSAYA[m.group(1)], m.group(2) == "añca"])
        elif t == "ca":
            if not items:
                raise ValueError("ca without item")
            items[-1][1] = True
        elif t == "PE":
            items.append(PE)
        elif t == "tadekaṭṭhaṃ":
            tad = True
        else:
            t = QUOT.get(t, t)
            if t not in VERBS:
                raise KeyError(t)
            kind, pl, neg = VERBS[t]
            preds.append(dict(items=items, kind=kind, pl=pl, neg=neg, tad=tad))
            items, tad = [], False
    if items or tad:
        raise ValueError("dangling items")
    return preds


def names(pred):
    return [it if it is PE else it[0] for it in pred["items"]]


def all_ca(pred):
    return all(it is PE or it[1] for it in pred["items"])


def render_preds(preds, flip=False):
    both = len(preds) > 1 and all(all_ca(p) for p in preds)
    outs = []
    for p in preds:
        neg = (not p["neg"]) if flip else p["neg"]
        outs.append(pred_h(p["kind"], p["pl"], neg, join_list(names(p)), both=both, tad=p["tad"]))
    return " और ".join(outs)


# ---------------------------------------------------------------- answers
COR_FIRST = {"tassa", "tesaṃ", "so", "te"}
COR_LOC = {"tattha", "ettha", "tato"}
NOCA_COR = {  # "no ca <cor> …"
    "": "", "tassa": "उसमें", "tesaṃ": "उनमें", "tattha": "वहाँ", "tassa tattha": "उसमें वहाँ",
    "tesaṃ tattha": "उनमें वहाँ", "tato": "वहाँ वह", "so tato": "वहाँ वह", "te tato": "वहाँ वे",
}


def take_phrase(toks, i, table):
    """Longest phrase of table at toks[i:] (case-insensitive first letter)."""
    for n in (4, 3, 2, 1):
        if i + n <= len(toks):
            ph = " ".join(toks[i:i + n])
            ph = ph[0].lower() + ph[1:]
            if ph in table:
                return table[ph], i + n
    return None, i


def tr_clause(s):
    toks = tokens(s)
    i = 0
    who, i = take_phrase(toks, i, PERSONS)
    places = []
    while True:
        p, j = take_phrase(toks, i, PLACES)
        if p is None:
            break
        places.append(p)
        i = j
    sab = False
    if i < len(toks) and toks[i] == "sabbattha":
        sab, i = True, i + 1
    while i < len(toks) and (toks[i] in COR_FIRST or toks[i] in COR_LOC):
        i += 1
    preds = parse_preds(toks[i:])
    parts = []
    if who:
        parts.append(who)
    if places:
        parts.append(join_list(places) + " " + IN)
    if sab:
        parts.append(SABBATTHA)
    if not who and (places or sab) and preds[0]["kind"] in NOMINATIVE_KINDS:
        parts.append(KOI)
    parts.append(render_preds(preds))
    return " ".join(parts)


def tr_noca(s):
    toks = tokens(s)
    i = 0
    cor = []
    while i < len(toks) and (toks[i] in COR_FIRST or toks[i] in COR_LOC):
        cor.append(toks[i])
        i += 1
    c = NOCA_COR[" ".join(cor)]
    preds = parse_preds(toks[i:])
    out = render_preds(preds, flip=True)
    return "पर " + (c + " " if c else "") + out


def tr_answer(s):
    """One answer sentence without its final period."""
    pe_tail = ""
    if s.endswith(" …pe…"):
        s, pe_tail = s[:-len(" …pe…")], " " + PE
    elif s.endswith("…pe…"):
        s, pe_tail = s[:-len("…pe…")], PE
    if s in SHORT:
        return SHORT[s] + pe_tail + "।"
    if s == "Tadekaṭṭhaṃ pajahati":
        return TADEKATTHA + " छोड़ता है" + pe_tail + "।"
    parts = re.split(r",? no ca ", s)   # one source line lacks the comma before "no ca"
    out = tr_clause(parts[0])
    for p in parts[1:]:
        out += ", " + tr_noca(p)
    return out + pe_tail + "।"


# ---------------------------------------------------------------- questions
Q_REL = {"yassa": "जिस व्यक्ति में", "yattha": "जिस स्थान पर", "yassa yattha": "जिस व्यक्ति में जिस स्थान पर",
         "yo": "जो व्यक्ति", "yato": "जिस स्थान के संबंध में " + KOI, "yo yato": "जो व्यक्ति जिस स्थान के संबंध में"}
Q_COR = {"tassa": "उसमें", "tattha": "वहाँ", "tassa tattha": "उसमें वहाँ",
         "so": "वह", "tato": "वहाँ वह", "so tato": "वह वहाँ"}
Q = "{AND}{REL} {P1}, क्या {COR} {P2}?"
KATTHA = "{X} कहाँ {V}?"


def tr_question(s):
    toks = tokens(s[:-1])
    if toks[0] == "Kattha":
        preds = parse_preds(toks[1:])
        assert len(preds) == 1
        p = preds[0]
        v = pred_h(p["kind"], p["pl"], p["neg"], "").strip()
        return KATTHA.format(X=join_list(names(p)), V=v)
    toks[0] = toks[0].lower()
    rel = [toks[0]]
    i = 1
    vp = False
    if toks[i:i + 2] == ["vā", "pana"]:
        vp, i = True, i + 2
    if toks[i] in ("yattha", "yato"):
        rel.append(toks[i])
        i += 1
    if toks[i:] == ["PE"]:   # abbreviated question: "yattha vā pana…pe…?"
        return (S.VA_PANA if vp else "") + Q_REL[" ".join(rel)] + PE + "?"
    # first predicate: up to the first verb
    j = i
    while QUOT.get(toks[j], toks[j]) not in VERBS:
        j += 1
    p1 = parse_preds(toks[i:j + 1])
    k = j + 1
    cor = []
    while toks[k] in ("tassa", "tattha", "so", "tato"):
        cor.append(toks[k])
        k += 1
    p2 = parse_preds(toks[k:])
    return Q.format(AND=S.VA_PANA if vp else "", REL=Q_REL[" ".join(rel)], P1=render_preds(p1),
                    COR=Q_COR[" ".join(cor)], P2=render_preds(p2))


# ---------------------------------------------------------------- lines
def tr_body(text):
    if text in FIXED:
        return FIXED[text]
    suffix = ""
    m = re.search(r"\s*\((\w+) ?\)$", text)
    if m and m.group(1) in MULAKA:
        suffix = " " + MULAKA_H.format(N=MULAKA[m.group(1)])
        text = text[:m.start()]
    label = ""
    m = re.match(r"^\((Ka|Kha)\) ", text)
    if m:
        label = S.LABELS["(" + m.group(1) + ")"] + " "
        text = text[m.end():]
    sents = re.split(r"(?<=[.?]) ", text)
    outs = []
    for s in sents:
        if s.endswith("?"):
            outs.append(tr_question(s))
        elif s.endswith("."):
            outs.append(tr_answer(s[:-1]))
        else:
            raise ValueError("sentence without end: " + s)
    return label + " ".join(outs) + suffix


def tr_line(line):
    if not line.strip():
        return ""
    m = S.ID_RE.search(line)
    bid = m.group(1) if m else None
    text = S.ID_RE.sub("", line) if m else line
    text = text.rstrip()
    if text.startswith("#"):
        level = len(text) - len(text.lstrip("#"))
        h = text[level:].strip()
        if h not in HEADINGS:
            raise ValueError("untranslated heading: " + h)
        out = "#" * level + " " + HEADINGS[h]
    else:
        try:
            out = tr_body(text)
        except (KeyError, ValueError, IndexError, AssertionError) as e:
            raise ValueError(f"untranslated line ({e!r}): {text}")
    return out + (" " + bid if bid else "")


def build(fname):
    lines = (PALI_DIR / fname).read_text(encoding="utf-8").splitlines()
    hi = [tr_line(l) for l in lines]
    (HI_DIR / fname).write_text("\n".join(hi) + "\n", encoding="utf-8", newline="\n")
    print(fname, len([l for l in lines if l.strip()]), "lines")


def main(argv):
    for f in argv or FILES:
        build(f)


if __name__ == "__main__":
    main(sys.argv[1:])
