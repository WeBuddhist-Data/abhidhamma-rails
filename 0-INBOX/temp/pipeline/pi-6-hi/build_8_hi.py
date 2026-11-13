r"""pi-6 Yamaka, Hindi plain zero-shot: Cittayamaka (8-cittayamaka.md).

usage: python -I -X utf8 build_8_hi.py
Frames: person (yassa … tassa), mind (yaṃ … taṃ), person+mind (yassa yaṃ … tassa taṃ);
predicates are verb/participle chains composed from PRED; qualifier chains come from
build_5_hi.who(). An unknown line raises an error.
"""
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi")
import build_sample_hi as S  # noqa: E402
import build_5_hi as B  # noqa: E402

FNAME = "8-cittayamaka.md"
CITTA = "मन"

# predicates of the mind: (positive, negative); masc. sg.
PRED = dict(S.VERBS_M)
PRED.update({
    "uppannaṃ": ("उत्पन्न हो चुका है", "उत्पन्न हो चुका नहीं है"),        # uppanna (terms)
    "uppajjamānaṃ": ("उत्पन्न होता हुआ है", "उत्पन्न होता हुआ नहीं है"),  # uppajjamāna (terms)
    "nirujjhamānaṃ": ("समाप्त होता हुआ है", "समाप्त होता हुआ नहीं है"),   # nirujjhamāna (terms)
    "niruddhaṃ": ("समाप्त हो चुका है", "समाप्त हो चुका नहीं है"),        # niruddha (terms)
})
KNOWN = set(PRED) | {"cittaṃ"}

# kinds of mind (pi-2 Hindi ch. 7 and pi-1/pi-2 termbases)
ADJ = {
    "sarāgaṃ": "राग-युक्त", "vītarāgaṃ": "राग से मुक्त", "sadosaṃ": "द्वेष-युक्त", "vītadosaṃ": "द्वेष से मुक्त",
    "samohaṃ": "मोह-युक्त", "vītamohaṃ": "मोह से मुक्त", "saṃkhittaṃ": "सिमटा हुआ", "vikkhittaṃ": "बिखरा हुआ",
    "mahaggataṃ": "उन्नत", "amahaggataṃ": "उन्नत न होने वाला", "sauttaraṃ": "सर्वोच्च न होने वाला",
    "anuttaraṃ": "सर्वोच्च", "samāhitaṃ": "एकाग्र", "asamāhitaṃ": "एकाग्रता से रहित", "vimuttaṃ": "मुक्त",
    "avimuttaṃ": "अमुक्त", "kusalaṃ": "हितकर", "akusalaṃ": "हानिकर", "abyākataṃ": "नैतिक रूप से अनिर्धारित",
    "sukhāya vedanāya sampayuttaṃ": "सुखद अनुभूति से जुड़ा", "araṇaṃ": "संघर्ष से रहित",
}


def adj(a):
    a = a.strip()
    return (ADJ[a] + " ") if a else ""


def pred(text, flip=False):
    """'uppajjati na nirujjhati' -> 'उत्पन्न होता है और समाप्त नहीं होता'."""
    toks, out = text.split(" "), []
    i = 0
    while i < len(toks):
        neg = toks[i] == "na"
        if neg:
            i += 1
        w = toks[i]
        if w.startswith("nu") and w[1:] in PRED:
            neg, w = True, w[1:]
        out.append(PRED[w][int(neg != flip)])
        i += 1
    return " और ".join(out)


def both(h):
    """insert भी after the first word: 'उत्पन्न होता है' -> 'उत्पन्न भी होता है'."""
    a, b = h.split(" ", 1)
    return f"{a} भी {b}"


def norm(w):
    """uppannañceva / uppannañca / uppajjamānañca -> uppannaṃ / uppajjamānaṃ."""
    w = re.sub(r"(ñceva|ñca)$", "ṃ", w)
    return w


# ---------------------------------------------------------------- headings
HEADINGS = dict(B.HEADINGS)
_CHANGE = "उत्पन्न होते हुए होने और समाप्त न होने का खंड"
HEADINGS.update({
    "Suddhacittasāmaññaṃ": "सामान्य रूप से केवल मन",
    "Suddhacittasāmañña": "सामान्य रूप से केवल मन",
    "Puggalavāro": "व्यक्ति का खंड",
    "Dhammavāro": "परिघटना का खंड",
    "Puggaladhammavāro": "व्यक्ति और परिघटना का खंड",
    "(1) Uppādanirodhakālasambhedavāro": "(1) उत्पन्न होने और समाप्त होने के समयों के मेल का खंड",
    "(2) Uppāduppannavāro": "(2) उत्पन्न होने और उत्पन्न हो चुके होने का खंड",
    "(3) Nirodhuppannavāro": "(3) समाप्त होने और उत्पन्न हो चुके होने का खंड",
    "(4) Uppādavāro": "(4) उत्पन्न होने का खंड",
    "(5) Nirodhavāro": "(5) समाप्त होने का खंड",
    "(6) Uppādanirodhavāro": "(6) उत्पन्न होने और समाप्त होने का खंड",
    "(7) Uppajjamāna-nanirodhavāro": "(7) " + _CHANGE,
    "(7) Uppajjamānananirodhavāro": "(7) " + _CHANGE,
    "(8) Uppajjamānuppannavāro": "(8) उत्पन्न होते हुए होने और उत्पन्न हो चुके होने का खंड",
    "(9) Nirujjhamānuppannavāro": "(9) समाप्त होते हुए होने और उत्पन्न हो चुके होने का खंड",
    "(10) Uppannuppādavāro": "(10) उत्पन्न हो चुके होने और उत्पन्न होने का खंड",
    "(11) Atītānāgatavāro": "(11) अतीत और भविष्य का खंड",
    "(12) Uppannuppajjamānavāro": "(12) उत्पन्न हो चुके होने और उत्पन्न होते हुए होने का खंड",
    "(13) Niruddhanirujjhamānavāro": "(13) समाप्त हो चुके होने और समाप्त होते हुए होने का खंड",
    "(14) Atikkantakālavāro": "(14) समय बीत चुकने का खंड",
    "Suttantacittamissakaviseso": "सुत्तों के मन के प्रकारों से मिला विशेष रूप",
    "Abhidhammacittamissakaviseso": "अभिधम्म के मन के प्रकारों से मिला विशेष रूप",
})

# ---------------------------------------------------------------- questions
REL = {"yassa": "जिस व्यक्ति में", "yaṃ": "जो", "yassa yaṃ": "जिस व्यक्ति में जो"}
COR = {"tassa": "उसमें", "taṃ": "वह", "tassa taṃ": "उसमें वह"}


def untie(w):
    if w in KNOWN:
        return w
    for cand in (w[:-2], w[:-3] + "ṃ", w[:-3] + "i", w[:-3] + "a"):
        if cand in KNOWN:
            return cand
    return w


def _subject(rel, a):
    """rel: yassa / yaṃ / yassa yaṃ; the mind with its kind."""
    if rel == "yassa":
        return f"{REL[rel]} {adj(a)}{CITTA}"
    return f"{REL[rel]} {CITTA}"


def _cor_subject(cor, a):
    if cor == "tassa":
        return f"उसमें {adj(a)}{CITTA}"
    return f"{COR[cor]} {CITTA}"


PROG = {"uppajjamānaṃ": "उत्पन्न होते हुए", "nirujjhamānaṃ": "समाप्त होते हुए"}
PASSED = ("{P} क्षण-क्षण आगे निकल चुका है, जिसका समय बीत चुका है",
          "{P} क्षण-क्षण आगे नहीं निकला है, जिसका समय नहीं बीता है")
_ATI = " khaṇaṃ khaṇaṃ vītikkantaṃ atikkantakālaṃ"


def tr_question(q):
    """q without label, with '?' and the quotative -ti."""
    words = q[:-1].split(" ")
    words[-1] = untie(words[-1])
    q = " ".join(words)
    q = q[0].lower() + q[1:]
    # (14) atikkantakāla
    m = re.fullmatch(rf"(yassa|yaṃ)( vā pana)?( yaṃ)? cittaṃ (na )?(\S+){_ATI}, (na )?(\S+){_ATI} (tassa taṃ|tassa|taṃ) cittaṃ", q)
    if m:
        rel, vp, rel2, n1, p1, n2, p2, cor = m.groups()
        a = PASSED[bool(n1)].format(P=PROG[p1])
        b = PASSED[bool(n2)].format(P=PROG[p2])
        return f"{S.VA_PANA if vp else ''}{_subject(rel + (rel2 or ''), '')} {a}, और {b}, {COR[cor]} {CITTA} कौन-सा है?"
    # (12)/(13): bare participles
    m = re.fullmatch(r"((?:na )?\S+) ((?:na )?\S+)", q)
    if m and all(t.replace("na ", "") in PRED for t in m.groups()):
        return f"जो {pred(m.group(1))}, क्या वह {pred(m.group(2))}?"
    m = re.fullmatch(r"(yassa|yaṃ)( vā pana)?( yaṃ)? (.*?)cittaṃ (.+?)"
                     r"(?: no ca (tassa taṃ|tassa|taṃ) (.*?)cittaṃ (.+?),)? (tassa taṃ|tassa|taṃ) (.*?)cittaṃ (.+)", q)
    if not m:
        raise ValueError("untranslated question: " + q)
    rel, vp, rel2, a1, p1, ncor, a2, p2, cor, a3, p3 = m.groups()
    rel = rel + (rel2 or "")
    out = f"{S.VA_PANA if vp else ''}{_subject(rel, a1)} {pred(p1)}"
    if ncor:
        out += f", पर {_cor_subject(ncor, a2)} {pred(p2, flip=True)}"
    return out + f", क्या {_cor_subject(cor, a3)} {pred(p3)}?"


# ---------------------------------------------------------------- answers
SUBJ = {
    "Bhaṅgakkhaṇe anāgatañca cittaṃ": "भंग होने के क्षण का और भविष्य का मन",
    "Uppādakkhaṇe anāgatañca cittaṃ": "उत्पन्न होने के क्षण का और भविष्य का मन",
    "Bhaṅgakkhaṇe atītañca cittaṃ": "भंग होने के क्षण का और अतीत का मन",
    "Uppādakkhaṇe anāgataṃ cittaṃ": "उत्पन्न होने के क्षण का, भविष्य का मन",
    "Bhaṅgakkhaṇe cittaṃ": "भंग होने के क्षण का मन",
    "Uppādakkhaṇe cittaṃ": "उत्पन्न होने के क्षण का मन",
    "Atītānāgataṃ cittaṃ": "अतीत और भविष्य का मन",
    "Atītaṃ cittaṃ": "अतीत का मन",
    "Anāgataṃ cittaṃ": "भविष्य का मन",
    "Paccuppannaṃ cittaṃ": "वर्तमान मन",
    "Bhaṅgakkhaṇe": "भंग होने के क्षण में",       # (12)/(13), without a subject
    "Uppādakkhaṇe": "उत्पन्न होने के क्षण में",
}
_SUBJ_KEYS = sorted(SUBJ, key=len, reverse=True)
NOCA = {"tesaṃ cittaṃ": "उनमें " + CITTA, "taṃ cittaṃ": "वह " + CITTA, "tassa taṃ cittaṃ": "उसमें वह " + CITTA, "": ""}


def tr_rest(rest, noca_who=None):
    """the predicate part of an answer: 'P1, no ca … P2' / 'A ceva B ca' / 'na ceva A na ca B' / 'P1, P2'."""
    m = re.fullmatch(r"(.+?),? no ca (?:(tesaṃ cittaṃ|tassa taṃ cittaṃ|taṃ cittaṃ) )?(.+)", rest)
    if m:
        p1, who_, p2 = m.groups()
        cor = NOCA[who_ or ""]
        return f"{pred(p1)}, पर {cor + ' ' if cor else ''}{pred(p2, flip=True)}"
    m = re.fullmatch(r"na ceva (\S+) na ca (\S+)", rest)
    if m:
        return f"न तो {pred(m.group(1))}, न {pred(m.group(2))}"
    m = re.fullmatch(r"(.+?), (.+)", rest)
    if m:
        return f"{tr_rest(m.group(1))}, {tr_rest(m.group(2))}"
    m = re.fullmatch(r"(.+?)(?:ñceva| ceva) (.+?)(?:ñca| ca)", rest)
    if m:
        a, b = norm(m.group(1) + "ñca"), norm(m.group(2) + "ñca")
        a = a if a in PRED else m.group(1)
        b = b if b in PRED else m.group(2)
        return f"{both(pred(a))} और {both(pred(b))}"
    return pred(rest)


def tr_sentence(s):
    """one answer sentence without its final period."""
    m = re.fullmatch(r"(.+?) tesaṃ…pe…", s)
    if m:
        return B.who(m.group(1)) + "…"
    m = re.fullmatch(r"(.+?) tesaṃ ((?:\S+ )*?)cittaṃ (.+)", s)
    if m:
        w, a, rest = m.groups()
        return f"{B.who(w)} {adj(a)}{CITTA} {tr_rest(rest)}"
    for k in _SUBJ_KEYS:
        if s.startswith(k + " ") or s.startswith(k + ","):
            return f"{SUBJ[k]} {tr_rest(s[len(k):].lstrip(', ').strip())}"
    raise ValueError("untranslated sentence: " + s)


# ---------------------------------------------------------------- listing lines (uddesa abridgements)
def _listing(t):
    def rep(m):
        rel, a, tail = m.groups()
        return f"{REL[rel.lower()]} {adj(a)}{CITTA} {pred('uppajjati' + (tail or ''))}"
    t = re.sub(r"([Yy]assa) ((?:\S+ )*?)cittaṃ uppajjati( na nirujjhati)?", rep, t)
    return t.replace("…pe….", "…।").replace("…pe…", "…")


FIXED = {
    "(Etena upāyena yāva saraṇaaraṇā uddharitabbā.)":
        "(इसी तरीके से “संघर्ष वाला” और “संघर्ष से रहित” तक निकालकर बताना चाहिए।)",
    "(14) Atikkantakālavāro": HEADINGS["(14) Atikkantakālavāro"],
    "Bhaṅgakkhaṇe cittaṃ uppādakkhaṇaṃ vītakkantaṃ bhaṅgakkhaṇaṃ avītikkantaṃ, atītaṃ cittaṃ uppādakkhaṇañca vītikkantaṃ bhaṅgakkhaṇañca vītikkantaṃ.":
        None,  # filled below (source slip vītakkantaṃ = vītikkantaṃ)
    "Bhaṅgakkhaṇe cittaṃ uppādakkhaṇaṃ vītikkantaṃ bhaṅgakkhaṇaṃ avītikkantaṃ, atītaṃ cittaṃ uppādakkhaṇañca vītikkantaṃ bhaṅgakkhaṇañca vītikkantaṃ.":
        "भंग होने के क्षण का मन उत्पन्न होने के क्षण से आगे निकल चुका है, भंग होने के क्षण से आगे नहीं निकला है, "
        "अतीत का मन उत्पन्न होने के क्षण से भी आगे निकल चुका है और भंग होने के क्षण से भी आगे निकल चुका है।",
    "Atītaṃ cittaṃ.": "अतीत का मन।",
    "Uppādakkhaṇe anāgataṃ cittaṃ.": SUBJ["Uppādakkhaṇe anāgataṃ cittaṃ"] + "।",
    "Bhaṅgakkhaṇe cittaṃ bhaṅgakkhaṇaṃ avītikkantaṃ no ca uppādakkhaṇaṃ avītikkantaṃ, uppādakkhaṇe anāgatañca cittaṃ bhaṅgakkhaṇañca avītikkantaṃ uppādakkhaṇañca avītikkantaṃ.":
        "भंग होने के क्षण का मन भंग होने के क्षण से आगे नहीं निकला है, पर उत्पन्न होने के क्षण से आगे निकल चुका है, "
        "उत्पन्न होने के क्षण का और भविष्य का मन भंग होने के क्षण से भी आगे नहीं निकला है और उत्पन्न होने के क्षण से भी आगे नहीं निकला है।",
    "(Yassa cittake sakabhāvena niddiṭṭhe, yaṃ cittake ca yassa yaṃ cittake ca ekattena niddiṭṭhe.)":
        "(“जिस व्यक्ति में मन” वाला भाग अपने ही रूप में बताया गया है, “जो मन” वाला भाग और "
        "“जिस व्यक्ति में जो मन” वाला भाग एक साथ बताए गए हैं।)",
    "Yassa vā pana…pe…? Āmantā …pe….": "और जिस व्यक्ति में…? हाँ …।",
    "(Mūlayamakaṃ cittayamakaṃ dhammayamakanti tīṇi yamakāni yāva saraṇaaraṇā gacchanti.)":
        f"(“{S.CHAPTER_TITLES['Mūlayamakaṃ']}”, “{S.CHAPTER_TITLES['Cittayamakaṃ']}” और "
        f"“{S.CHAPTER_TITLES['Dhammayamakaṃ']}”, ये तीनों भाग “संघर्ष वाला” और “संघर्ष से रहित” तक जाते हैं।)",
    "Cittayamakaṃ niṭṭhitaṃ.": S.CHAPTER_END.format(title=S.CHAPTER_TITLES["Cittayamakaṃ"]),
}
FIXED["Bhaṅgakkhaṇe cittaṃ uppādakkhaṇaṃ vītakkantaṃ bhaṅgakkhaṇaṃ avītikkantaṃ, atītaṃ cittaṃ uppādakkhaṇañca vītikkantaṃ bhaṅgakkhaṇañca vītikkantaṃ."] = \
    FIXED["Bhaṅgakkhaṇe cittaṃ uppādakkhaṇaṃ vītikkantaṃ bhaṅgakkhaṇaṃ avītikkantaṃ, atītaṃ cittaṃ uppādakkhaṇañca vītikkantaṃ bhaṅgakkhaṇañca vītikkantaṃ."]

SHORT = dict(B.SHORT)
SHORT.update({"Uppannaṃ.": PRED["uppannaṃ"][0] + "।"})


def tr_text(t):
    if t in FIXED:
        return FIXED[t]
    if t in SHORT:
        return SHORT[t]
    if "…" in t and "cittaṃ uppajjati" in t and not t.startswith("("):
        r = _listing(t)
        if not re.search(r"[a-zāīūṃṅñṭḍṇ]{3,}", r):
            return r
    outs = []
    for part in re.split(r"(?<=[?.]) ", t):
        if part.endswith("?"):
            m = B.LABEL_RE.match(part)
            if m:
                outs.append(S.LABELS[m.group(1)] + " " + tr_question(m.group(2)))
            else:
                outs.append(tr_question(part))
        elif part in SHORT:
            outs.append(SHORT[part])
        elif part.endswith("."):
            outs.append(tr_sentence(part[:-1]) + "।")
        else:
            raise ValueError("untranslated part: " + part)
    return " ".join(outs)


def tr_line(line):
    if not line.strip():
        return ""
    m = S.ID_RE.search(line)
    bid = m.group(1) if m else None
    text = S.ID_RE.sub("", line) if m else line
    if text.startswith("#"):
        level = len(text) - len(text.lstrip("#"))
        h = text[level:].strip()
        if h not in HEADINGS:
            raise ValueError("untranslated heading: " + h)
        out = "#" * level + " " + HEADINGS[h]
    else:
        out = tr_text(text)
    return out + (" " + bid if bid else "")


def build():
    raw = (S.PALI_DIR / FNAME).read_text(encoding="utf-8").splitlines()
    out = [tr_line(l) for l in raw]
    (S.HI_DIR / FNAME).write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
    print(FNAME, len([l for l in raw if l.strip()]), "lines")


if __name__ == "__main__":
    build()
