"""Builder for pi-6 Hindi plain RAILS: 7-09, 7-10, 7-11 (Anusayayamaka: Pahīnavāra, Uppajjanavāra,
Dhātupucchā- and Dhātuvisajjanāvāra, chapter end).

usage: python -I -X utf8 build_7-09_7-11.py [--dry]
Imports build_rails_sample.py read-only for the shared constants. Raises on any sentence it has no formula for.
New recurring formulas are listed in notes-7-09-7-11.md.
"""
import re, sys, pathlib

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\rails")
import build_rails_sample as S  # noqa: E402  (read-only)

FILES = ["7-09-anusayayamaka.md", "7-10-anusayayamaka.md", "7-11-anusayayamaka.md"]

# ------------------------------------------------------------------------------------------------
# Terms (termbase)
# ------------------------------------------------------------------------------------------------
ANUSAYA = {
    "kāmarāgānusayo": "इंद्रिय-सुखों के राग की सुप्त प्रवृत्ति",
    "paṭighānusayo": "चिढ़ की सुप्त प्रवृत्ति",
    "mānānusayo": "अहंकार की सुप्त प्रवृत्ति",
    "diṭṭhānusayo": "दृष्टि की सुप्त प्रवृत्ति",
    "vicikicchānusayo": "संशय की सुप्त प्रवृत्ति",
    "bhavarāgānusayo": "अस्तित्व के राग की सुप्त प्रवृत्ति",
    "avijjānusayo": "अज्ञान की सुप्त प्रवृत्ति",
}
# verb token -> (stem, negative?) ; anusaya is feminine
VTOK = {
    "pahīno": ("pahīna", False), "pahīnā": ("pahīna", False),
    "appahīno": ("pahīna", True), "appahīnā": ("pahīna", True),
    "uppajjati": ("uppajjati", False), "nuppajjati": ("uppajjati", True),
}
VTI = {"pahīnoti": "pahīno", "pahīnāti": "pahīnā", "appahīnoti": "appahīno", "appahīnāti": "appahīnā",
       "uppajjatīti": "uppajjati", "nuppajjatīti": "nuppajjati"}
# (stem, number) -> (positive, negative)
VHI = {
    ("pahīna", "sg"): ("छोड़ी जा चुकी है", "छोड़ी नहीं गई है"),
    ("pahīna", "pl"): ("छोड़ी जा चुकी हैं", "छोड़ी नहीं गई हैं"),
    ("uppajjati", "sg"): ("उत्पन्न होती है", "उत्पन्न नहीं होती"),
    ("uppajjati", "pl"): ("उत्पन्न होती हैं", "उत्पन्न नहीं होतीं"),
}
# Na vattabbo "pahīno"ti vā "appahīno"ti vā
NV_QUOTES = {"vattabbo": ("छोड़ी जा चुकी", "छोड़ी नहीं गई"), "vattabbā": ("छोड़ी जा चुकीं", "छोड़ी नहीं गईं")}
NV_FRAME = "{x} को न “{a}” कहा जा सकता है, न “{b}”"
NV_FRAME_BARE = "{x} न “{a}” कहा जा सकता है, न “{b}”"   # bare Na vattabbo/ā …
NV_BARE = {"vattabbo": "उसे", "vattabbā": "उन्हें"}

PERSONS = {   # Pāli -> (Hindi with «में», number of the correlative)
    "anāgāmissa": ("फिर न लौटने वाले में", "sg"),
    "arahato": ("अर्हत् में", "sg"),
    "puthujjanassa": ("साधारण व्यक्ति में", "sg"),
    "dvinnaṃ puggalānaṃ": ("दो व्यक्तियों में", "pl"),
    "tiṇṇaṃ puggalānaṃ": ("तीन व्यक्तियों में", "pl"),
    "catunnaṃ puggalānaṃ": ("चार व्यक्तियों में", "pl"),
    "tasseva puggalassa": ("उसी व्यक्ति में", "sg"),
    "tesaññeva puggalānaṃ": ("उन्हीं व्यक्तियों में", "pl"),
}
PLACES = {    # anusaya places (locative) -> Hindi chunk with «में»
    "kāmadhātuyā dvīsu vedanāsu": "इंद्रिय-सुखों के लोक की दो अनुभूतियों में",
    "kāmadhātuyā tīsu vedanāsu": "इंद्रिय-सुखों के लोक की तीन अनुभूतियों में",
    "dukkhāya vedanāya": "दुःखद अनुभूति में",
    "rūpadhātuyā": "सूक्ष्म भौतिक लोक में",
    "arūpadhātuyā": "अभौतिक लोक में",
}
CORR = {"tassa": "उसमें", "tesaṃ": "उनमें", "tassa tattha": "उसमें वहाँ", "tesaṃ tattha": "उनमें वहाँ",
        "tattha": "वहाँ"}
REL = [("yassa vā pana yattha", "और जिस व्यक्ति में जिस स्थान पर"), ("yassa yattha", "जिस व्यक्ति में जिस स्थान पर"),
       ("yassa vā pana", "और जिस व्यक्ति में"), ("yassa", "जिस व्यक्ति में"),
       ("yattha vā pana", "और जिस स्थान पर"), ("yattha", "जिस स्थान पर")]
assert dict(REL)["yassa"] == S.REL_FRAMES[("yassa", "tassa")][0]
assert dict(REL)["yattha vā pana"] == S.REL_FRAMES[("yattha vā pana", "tattha")][0]
QCORR = {"tassa": "उसमें", "tattha": "वहाँ", "tassa tattha": "उसमें वहाँ"}

MULAKA = {  # cycle labels
    # as notes-7-03-7-04 / notes-7-05-7-06 (termbase ekamūlakaṃ is the Mūlayamaka sense)
    "(Ekamūlakaṃ)": "(एक मूल पर आधारित)", "(Dukamūlakaṃ)": "(दो मूलों पर आधारित)",
    "(Tikamūlakaṃ)": "(तीन मूलों पर आधारित)", "(Catukkamūlakaṃ)": "(चार मूलों पर आधारित)",
    "(Pañcakamūlakaṃ)": "(पाँच मूलों पर आधारित)", "(Chakkamūlakaṃ)": "(छह मूलों पर आधारित)",
    # termbase
    "(Kāmadhātumūlakaṃ)": "(इंद्रिय-सुखों के लोक पर आधारित)",
    "(Rūpadhātumūlakaṃ)": "(सूक्ष्म भौतिक लोक पर आधारित)",
    "(Arūpadhātumūlakaṃ)": "(अभौतिक लोक पर आधारित)",
    "(Nakāmadhātumūlakaṃ)": "(इंद्रिय-सुखों के लोक से भिन्न लोक पर आधारित)",
    "(Narūpadhātumūlakaṃ)": "(सूक्ष्म भौतिक लोक से भिन्न लोक पर आधारित)",
    "(Naarūpadhātumūlakaṃ)": "(अभौतिक लोक से भिन्न लोक पर आधारित)",
    "(Nakāmanaarūpadhātumūlakaṃ)": "(इंद्रिय-सुखों के लोक और अभौतिक लोक से भिन्न लोक पर आधारित)",
    "(Narūpanaarūpadhātumūlakaṃ)": "(सूक्ष्म भौतिक लोक और अभौतिक लोक से भिन्न लोक पर आधारित)",
    "(Nakāmanarūpadhātumūlakaṃ)": "(इंद्रिय-सुखों के लोक और सूक्ष्म भौतिक लोक से भिन्न लोक पर आधारित)",
}
VITTHAR = "इसी प्रकार विस्तार करना चाहिए"   # bare (vitthāretabbaṃ), harmonise N-notes

HEADINGS = dict(S.HEADINGS)
HEADINGS.update({
    "Pahīnavāra": S.HEADINGS["Pahīnavāro"],
    "(Gha) paṭilomapuggalo": "(घ) विपरीत: व्यक्ति",
    "(Ṅa) paṭilomaokāso": "(ङ) विपरीत: स्थान",
    "(Ca) paṭilomapuggalokāsā": "(च) विपरीत: व्यक्ति और स्थान",
    "Uppajjanavāro": "उत्पन्न होने का खंड",
    "(Ka) dhātupucchāvāro": "(क) लोकों के बारे में प्रश्नों का खंड",
    "(Kha) dhātuvisajjanāvāro": "(ख) लोकों के बारे में उत्तरों का खंड",
})
CLOSINGS = {
    "Āmantā.": S.AMANTA, "Natthi.": S.NATTHI, "No.": S.NO,
    "Āmantā …pe….": "हाँ …।",
    "Pahīnavāre anulomaṃ.": "छोड़ा जा चुका होने के खंड में सकारात्मक।",
    "Pahīnavāre paṭilomaṃ.": "छोड़ा जा चुका होने के खंड में विपरीत।",
    "Pahīnavāro.": "छोड़ा जा चुका होने का खंड।",
    "Uppajjanavāro.": "उत्पन्न होने का खंड।",
    "Dhātupucchāvāro.": "लोकों के बारे में प्रश्नों का खंड।",
    "Dhātuvisajjavāro.": "लोकों के बारे में उत्तरों का खंड।",
    "Anusayayamakaṃ niṭṭhitaṃ.": S.CHAPTER_END.format(title=S.CHAPTER_TITLES["Anusayayamakaṃ"]),
    "Namo tassa bhagavato arahato sammāsambuddhassa": S.NAMO,
    "(Vitthāretabbaṃ).": f"({VITTHAR})।",
    "9": "9",   # 7-10 ^6-7-311: a stray numeral line in the source, kept as it is
}

# Variant bracket (7-09 ^6-7-270)
VARIANTS = {
    "[pahīno (sī. ka.) anusayavārena pana na sameti]":
        "[वर्तनी-भेद (Sī., Ka.): pahīno; पर यह सुप्त प्रवृत्तियों के खंड से मेल नहीं खाता]",
}

# ------------------------------------------------------------------------------------------------
# Dhātu sections (7-10 ^6-7-332 … 7-11 ^6-7-348)
# ------------------------------------------------------------------------------------------------
DHATU = {"kāma": "इंद्रिय-सुखों के लोक", "rūpa": "सूक्ष्म भौतिक लोक", "arūpa": "अभौतिक लोक"}
NUM = {"satta": "सात", "pañca": "पाँच", "tayo": "तीन"}
BHANGA_NATTHI = "भंग हो चुकी कोई सुप्त प्रवृत्ति नहीं है"          # anusayā bhaṅgā natthi
KATI_Q = ("कितनी सुप्त प्रवृत्तियाँ सोई रहती हैं, कितनी सुप्त प्रवृत्तियाँ सोई नहीं रहतीं, "
          "कितनी सुप्त प्रवृत्तियाँ भंग हो चुकी हैं")                # kati anusayā anusenti, … nānusenti, … bhaṅgā
SATTEVA = "सातों ही सुप्त प्रवृत्तियाँ सोई रहती हैं"                 # satteva anusayā anusenti
KASSACI = "किसी व्यक्ति में {n} सुप्त प्रवृत्तियाँ सोई रहती हैं"       # first kassaci N anusayā anusenti
KASSACI_N = "किसी में {n} सुप्त प्रवृत्तियाँ सोई रहती हैं"             # further kassaci
UPAPATTI_NATTHI = "{place} में जन्म नाम की कोई चीज़ नहीं है"         # X upapatti nāma natthi
HETTHA = "नीचे जन्म लेता हुआ व्यक्ति इंद्रिय-सुखों के लोक में ही जन्म लेता है"  # heṭṭhā upapajjamāno kāmadhātuṃyeva upapajjati
USME_SATTEVA = "उसमें " + SATTEVA


def dhatu_set(words, case):
    """words like ['na','kāmadhātuyā','na','arūpadhātuyā'] or ['rūpadhātuṃ'] -> Hindi place (oblique)."""
    neg = words[0].lower() == "na"
    names = [w for w in words if w.lower() != "na"]
    keys = []
    for w in names:
        m = re.fullmatch(r"(kāma|rūpa|arūpa)dhātu(yā|ṃ)", w.lower())
        assert m and (m.group(2) == ("yā" if case == "abl" else "ṃ") or case == "loc"), (w, case)
        keys.append(DHATU[m.group(1)])
    if neg:
        assert all(words[i].lower() == "na" for i in range(0, len(words), 2)), words
        return " और ".join(keys) + " से भिन्न लोक"
    assert len(keys) == 1
    return keys[0]


DHATU_W = r"(?:[Nn]a )?(?:kāma|rūpa|arūpa|Kāma|Rūpa|Arūpa)dhātu(?:yā|ṃ)(?: na (?:kāma|rūpa|arūpa)dhātu(?:yā|ṃ))?"


def dhatu_sentence(s):
    m = re.fullmatch(rf"({DHATU_W}) cutassa ({DHATU_W}) upapajjantassa (.*)", s)
    if m:
        frm = dhatu_set(m.group(1).split(), "abl") + " से मरकर"
        to = dhatu_set(m.group(2).split(), "acc") + " में जन्म लेने वाले"
        rest = m.group(3)
        if rest == "kati anusayā anusenti, kati anusayā nānusenti, kati anusayā bhaṅgā?":
            return f"{frm} {to} में {KATI_Q}?"
        if rest == "kati anusayā anusenti, kati anusayā nānusenti, kati anusayā bhaṅgā.":   # source slip "." (^6-7-335)
            return f"{frm} {to} में {KATI_Q}?"
        if rest == "satteva anusayā anusenti; anusayā bhaṅgā natthi.":
            return f"{frm} {to} में {SATTEVA}; {BHANGA_NATTHI}।"
        m2 = re.fullmatch(r"((?:kassaci \S+ anusayā anusenti, )*kassaci \S+ anusayā anusenti); anusayā bhaṅgā natthi\.",
                          rest)
        if m2:
            parts = m2.group(1).split(", ")
            hi = []
            for i, p in enumerate(parts):
                n = re.fullmatch(r"kassaci (\S+) anusayā anusenti", p).group(1)
                hi.append((KASSACI if i == 0 else KASSACI_N).format(n=NUM[n]))
            return f"{frm} {to} " + ", ".join(hi) + f"; {BHANGA_NATTHI}।"
        raise ValueError("dhatu rest: " + rest)
    m = re.fullmatch(rf"({DHATU_W}) cutassa ({DHATU_W}) upapatti ?nāma natthi, heṭṭhā upapajjamāno kāmadhātuṃyeva "
                     r"upapajjati, satteva anusayā anusenti; anusayā bhaṅgā natthi\.", s)
    if m:
        frm = dhatu_set(m.group(1).split(), "abl") + " से मरकर"
        place = dhatu_set(m.group(2).split(), "loc")
        return f"{frm} {UPAPATTI_NATTHI.format(place=place)}, {HETTHA}, {USME_SATTEVA}; {BHANGA_NATTHI}।"
    return None


# ------------------------------------------------------------------------------------------------
# Pahīna / Uppajjana sections
# ------------------------------------------------------------------------------------------------
def lc(s):
    return s[:1].lower() + s[1:]


def list_hi(tokens):
    """['kāmarāgānusayo','ca','paṭighānusayo','ca'] -> (Hindi, number). '…pe…' abbreviates (number sg)."""
    items, pe = [], False
    for t in tokens:
        t = lc(t)
        if t == "ca":
            continue
        if t == "…pe…":
            pe = True
            items[-1] = items[-1] + "…"
            continue
        assert t in ANUSAYA, ("not an anusaya: " + t, tokens)
        items.append(ANUSAYA[t])
    assert items, tokens
    if pe:
        assert len(items) == 2, tokens
        return items[0] + " " + items[1], "sg"
    if len(items) == 1:
        return items[0], "sg"
    return ", ".join(items[:-1]) + " और " + items[-1], "pl"


def verb_hi(tok, number, flip=False):
    stem, neg = VTOK[tok]
    pos, negf = VHI[(stem, number)]
    if flip:
        neg = not neg
    pal_num = "pl" if tok.endswith("ā") else "sg"
    if stem == "pahīna" and pal_num != number:
        SLIPS.append(f"number: {tok} with {number} subject")
    return negf if neg else pos


SLIPS = []


def tokens(s):
    s = s.replace("…pe…", " …pe… ")
    return s.split()


def question(s):
    m = re.fullmatch(r"(?:\((Ka|Kha)\) )?(.*)\?", s)
    label = S.LABELS[f"({m.group(1)})"] + " " if m.group(1) else ""
    body = lc(m.group(2))
    for p, hi in REL:
        if body.startswith(p + " "):
            rel, rel_hi, body = p, hi, body[len(p) + 1:]
            break
    else:
        raise ValueError("rel: " + s)
    if rel.startswith("yassa vā pana"):
        rel_hi = rel_hi if label else rel_hi   # same either way
    toks = tokens(body)
    # V1
    i = next(k for k, t in enumerate(toks) if t in VTOK)
    subj1, v1 = toks[:i], toks[i]
    j = i + 1
    variant = ""
    if j < len(toks) and toks[j].startswith("@VAR"):
        variant = " " + VARIANTS_BY_KEY[toks[j]]
        j += 1
    corr_n = 2 if toks[j + 1] == "tattha" and toks[j] == "tassa" else 1
    corr = " ".join(toks[j:j + corr_n])
    rest = toks[j + corr_n:]
    v2 = VTI[rest[-1]]
    subj2 = rest[:-1]
    l1, n1 = list_hi(subj1)
    l2, n2 = list_hi(subj2)
    return (f"{label}{rel_hi} {l1} {verb_hi(v1, n1)}{variant}, क्या {QCORR[corr]} {l2} {verb_hi(v2, n2)}?")


def clause_hi(toks, flip=False):
    """'A ca V1 B ca V2' (both) or 'LIST V'."""
    groups, cur = [], []
    for t in toks:
        if t in VTOK:
            groups.append((cur, t))
            cur = []
        else:
            cur.append(t)
    assert not cur and groups, toks
    if len(groups) == 1:
        lst, n = list_hi(groups[0][0])
        return f"{lst} {verb_hi(groups[0][1], n, flip)}"
    assert len(groups) == 2 and not flip, toks
    (a, va), (b, vb) = groups
    la, na = list_hi(a)
    lb, nb = list_hi(b)
    return f"{la} भी {verb_hi(va, na)} और {lb} भी {verb_hi(vb, nb)}"


def nv_hi(toks):
    k = toks.index("vattabbo") if "vattabbo" in toks else toks.index("vattabbā")
    vt = toks[k]
    assert toks[k - 1].lower() == "na", toks
    tail = " ".join(toks[k + 1:])
    exp = {"vattabbo": '"pahīno"ti vā "appahīno"ti vā', "vattabbā": '"pahīnā"ti vā "appahīnā"ti vā'}[vt]
    assert tail == exp, (tail, exp)
    subj = toks[:k - 1]
    a, b = NV_QUOTES[vt]
    if not subj:
        return NV_FRAME_BARE.format(x=NV_BARE[vt], a=a, b=b)
    x, n = list_hi(subj)
    if (n == "pl") != (vt == "vattabbā"):
        SLIPS.append(f"nv number: {toks}")
    return NV_FRAME.format(x=x, a=a, b=b)


def prefix(toks):
    """person, places, marker -> (hindi prefix, rest tokens, person number)."""
    hi, num = [], None
    low = [t.lower() for t in toks]
    for k in (2, 1):
        key = " ".join(low[:k])
        if key in PERSONS:
            hi.append(PERSONS[key][0])
            num = PERSONS[key][1]
            toks, low = toks[k:], low[k:]
            break
    places = []
    while True:
        for k in (3, 2, 1):
            key = " ".join(low[:k])
            if key in PLACES:
                places.append(PLACES[key])
                toks, low = toks[k:], low[k:]
                break
        else:
            break
    if places:
        hi.append(places[0] if len(places) == 1 else ", ".join(places[:-1]) + " और " + places[-1])
    marker = None
    for k in (2, 1):
        key = " ".join(low[:k])
        if key in ("tassa tattha", "tesaṃ tattha", "ettha", "tassa", "tesaṃ"):
            marker = key
            toks, low = toks[k:], low[k:]
            break
    if marker and "tattha" in marker or marker == "ettha":
        assert places, ("marker without place", toks)
    if marker in ("tassa", "tesaṃ", "tassa tattha", "tesaṃ tattha"):
        assert num == ("sg" if marker.startswith("tassa") else "pl"), (marker, num)
    return " ".join(hi), toks, num


def answer(s):
    tail = ""
    if s.endswith(" (vitthāretabbaṃ)."):
        s = s[: -len(" (vitthāretabbaṃ).")] + "."
        tail = f" ({VITTHAR})"
    ell = False
    if s.endswith(" …pe…."):
        s, ell = s[: -len(" …pe….")], True
    else:
        assert s.endswith("."), s
        s = s[:-1]
    parts = s.split("; ")
    # a «;» or «,» inside a both-clause is a source slip (^6-7-306, ^6-7-307): read as one clause
    first = parts[0]
    extra = []
    for p in parts[1:]:
        if "vattabb" in p:
            extra.append(p)
        else:
            assert not extra
            SLIPS.append("semicolon inside a both-clause: " + s[:60])
            first = first + " " + p
    if ", " in first and ", no ca " not in first:
        SLIPS.append("comma inside a both-clause: " + s[:60])
        first = first.replace(", ", " ")
    if ", no ca " in first:
        c1, c2 = first.split(", no ca ")
    else:
        c1, c2 = first, None
    pre_hi, rest, num = prefix(tokens(c1))
    if "vattabbo" in rest or "vattabbā" in rest:
        assert c2 is None
        body = nv_hi(rest)
    else:
        body = clause_hi(rest)
    out = (pre_hi + " " if pre_hi else "") + body
    if c2 is not None:
        t2 = tokens(c2)
        corr = None
        for k in (2, 1):
            key = " ".join(t2[:k])
            if key in CORR:
                corr, t2 = key, t2[k:]
                break
        assert corr, c2
        out += f", पर {CORR[corr]} {clause_hi(t2, flip=True)}"
    for p in extra:
        out += "; " + nv_hi(tokens(p))
    out = out[:1] + out[1:]
    return out + tail + (" …।" if ell else "।")


SENT_SPLIT = re.compile(r"(?<=[.?])\s+")
VARIANTS_BY_KEY = {}


def translate_sentence(s):
    if s in CLOSINGS:
        return CLOSINGS[s]
    if s in MULAKA:
        return MULAKA[s]
    d = dhatu_sentence(s)
    if d:
        return d
    if s.endswith("?"):
        return question(s)
    return answer(s)


def translate_text_line(line):
    for k, (pv, hv) in enumerate(VARIANTS.items()):
        key = f"@VAR{k}"
        VARIANTS_BY_KEY[key] = hv
        line = line.replace(" " + pv, " " + key)
    sents = SENT_SPLIT.split(line.strip())
    return " ".join(translate_sentence(x) for x in sents)


ID_RE = re.compile(r"\s(\^[0-9A-Za-z-]+)\s*$")


def translate_line(line):
    m = ID_RE.search(line)
    bid = m.group(1) if m else None
    text = line[: m.start()] if m else line
    if text.startswith("#"):
        hashes, h = re.match(r"(#+) (.*)", text).groups()
        hi = f"{hashes} {HEADINGS[h.strip()]}"
    else:
        hi = translate_text_line(text)
    return hi + (f" {bid}" if bid else "")


def translate_text(pali):
    out = []
    for line in pali.splitlines():
        if not line.strip():
            if out and out[-1] != "":
                out.append("")
            continue
        out.append(translate_line(line))
    while out and out[-1] == "":
        out.pop()
    return "\n".join(out) + "\n"


def main():
    dry = "--dry" in sys.argv
    for f in FILES:
        pali = (S.PALI_DIR / f).read_bytes().decode("utf-8").replace("\r\n", "\n")
        hi = translate_text(pali)
        if not dry:
            (S.HI_DIR / f).write_text(hi, encoding="utf-8", newline="\n")
        print(f, "lines", len([l for l in hi.splitlines() if l.strip()]))
    for x in sorted(set(SLIPS)):
        print("SLIP:", x)


if __name__ == "__main__":
    main()
