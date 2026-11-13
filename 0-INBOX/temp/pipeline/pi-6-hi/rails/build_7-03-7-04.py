"""pi-6 Anusayayamaka, Sānusayavāra (7-03 anuloma, 7-04 paṭiloma): Pāli -> Hindi plain RAILS.

usage: python -I -X utf8 build_7-03-7-04.py [7-03-anusayayamaka.md 7-04-anusayayamaka.md] [--dry]
Imports build_rails_sample read-only (shared labels, short answers, headings, sentence splitter).
Every sentence must match a formula below; an unknown sentence raises ValueError.
"""
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\rails")
import build_rails_sample as S  # noqa: E402

# ---------------------------------------------------------------- terms (locked termbase / pi-2 ^2-… names)
NAMES = {  # instrumental -> Hindi (fem. सुप्त प्रवृत्ति; «वाला» agrees with the person)
    "kāmarāgānusayena": "इंद्रिय-सुखों के राग की सुप्त प्रवृत्ति",
    "paṭighānusayena": "चिढ़ की सुप्त प्रवृत्ति",
    "mānānusayena": "अहंकार की सुप्त प्रवृत्ति",
    "diṭṭhānusayena": "दृष्टि की सुप्त प्रवृत्ति",
    "vicikicchānusayena": "संशय की सुप्त प्रवृत्ति",
    "bhavarāgānusayena": "अस्तित्व के राग की सुप्त प्रवृत्ति",
    "avijjānusayena": "अज्ञान की सुप्त प्रवृत्ति",
}
# predicate word -> (kind, number); sānusayo = सुप्त प्रवृत्ति वाला, niranusayo = सुप्त प्रवृत्ति से मुक्त
PREDS = {"sānusayo": ("sa", "sg"), "sānusayā": ("sa", "pl"),
         "niranusayo": ("nir", "sg"), "niranusayā": ("nir", "pl")}
VALA = {"sg": "वाला", "pl": "वाले"}
COP = {"sg": "है", "pl": "हैं"}
PRON = {"sg": "वह", "pl": "वे"}

SUBJECTS = {  # sentence-initial persons -> (Hindi, number)
    "Anāgāmī": ("फिर न लौटने वाला", "sg"),
    "Arahā": ("अर्हत्", "sg"),
    "Puthujjano": ("साधारण व्यक्ति", "sg"),
    "Sveva puggalo": ("वही व्यक्ति", "sg"),
    "Teva puggalā": ("वही व्यक्ति", "pl"),
    "Dve puggalā": ("दो प्रकार के व्यक्ति", "pl"),
    "Tayo puggalā": ("तीन प्रकार के व्यक्ति", "pl"),
    "Cattāro puggalā": ("चार प्रकार के व्यक्ति", "pl"),
}
APARIYAPANNA = "अस्तित्व के लोकों में न समाई हुई परिघटनाओं में"   # pi-1 ^1-M2-96 (not in the pi-6 termbase)
PLACES = [  # (Pāli token sequence, Hindi chunk) ; longest first
    (("kāmadhātuyā", "dvīsu", "vedanāsu"), "इंद्रिय-सुखों के लोक की दो अनुभूतियों में"),
    (("kāmadhātuyā", "tīsu", "vedanāsu"), "इंद्रिय-सुखों के लोक की तीन अनुभूतियों में"),
    (("dukkhāya", "vedanāya"), "दुःखद अनुभूति में"),
    (("rūpadhātuyā",), "सूक्ष्म भौतिक लोक में"),
    (("arūpadhātuyā",), "अभौतिक लोक में"),
    (("apariyāpanne",), APARIYAPANNA),
    (("ariyāpanne",), APARIYAPANNA),   # 7-04 ^6-7-130 line 256: source slip for apariyāpanne
]
SABBATTHA = "सब जगह"

MULAKA_LABELS = {
    "(Ekamūlakaṃ)": "(एक मूल पर आधारित)",
    "(Dukamūlakaṃ)": "(दो मूलों पर आधारित)",
    "(Tikamūlakaṃ)": "(तीन मूलों पर आधारित)",
    "(Catukkamūlakaṃ)": "(चार मूलों पर आधारित)",
    "(Pañcakamūlakaṃ)": "(पाँच मूलों पर आधारित)",
    "(Chakkamūlakaṃ)": "(छह मूलों पर आधारित)",
}
VARA = "सुप्त प्रवृत्ति वाला होने का खंड"          # Sānusayavāro (termbase)
VARA_OBL = "सुप्त प्रवृत्ति वाला होने के खंड"
CLOSINGS = {
    "Sānusayavāre anulomaṃ.": f"{VARA_OBL} में सकारात्मक।",
    "Sānusayavāre paṭilomaṃ.": f"{VARA_OBL} में विपरीत।",
    "Sānusayavāro.": f"{VARA}।",
    "Āmantā.": S.AMANTA, "No.": S.NO, "Natthi.": S.NATTHI,
}
HEADINGS = {
    "Sānusayavāro": VARA, "Sānusayavāra": VARA,
    "(Ka) anulomapuggalo": S.HEADINGS["(Ka) anulomapuggalo"],
    "(Kha) anulomaokāso": S.HEADINGS["(Kha) anulomaokāso"],
    "(Ga) anulomapuggalokāsā": S.HEADINGS["(Ga) anulomapuggalokāsā"],
    "(Gha) paṭilomapuggalo": "(घ) विपरीत: व्यक्ति",
    "(Ṅa) paṭilomaokāso": "(ङ) विपरीत: स्थान",
    "(Ca) paṭilomapuggalokāsā": "(च) विपरीत: व्यक्ति और स्थान",
}


# ---------------------------------------------------------------- helpers
def join_list(xs, last=" और "):
    return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + last + xs[-1]


def group_hi(g):
    """'kāmarāgānusayena ca paṭighānusayena ca' -> «A और B»; 'diṭṭhānusayena…pe… vicikicchānusayena' -> «A… B»."""
    g = g.strip()
    m = re.fullmatch(r"(\S+?)( ?)…pe… (\S+)", g)
    if m:
        return f"{NAMES[m.group(1)]}… {NAMES[m.group(3)]}"   # a space before …pe… is dropped
    items = [t for t in g.split(" ") if t != "ca"]
    return join_list([NAMES[t] for t in items])


def pred_hi(kind, num, neg=False, bhi=False):
    """Predicate after the tendency names: «वाला है» / «से मुक्त नहीं हैं» / «वाले भी हैं»."""
    head = VALA[num] if kind == "sa" else "से मुक्त"
    return f"{head}{' भी' if bhi else ''} {'नहीं ' if neg else ''}{COP[num]}"


def clause_groups(c):
    """'X ca sānusayā Y ca Z ca sānusayā' -> [(group-str, kind, num), ...]."""
    out, cur = [], []
    for t in c.strip().split(" "):
        if t in PREDS:
            if not cur:
                raise ValueError(f"predicate without names: {c}")
            out.append((" ".join(cur), *PREDS[t]))
            cur = []
        else:
            cur.append(t)
    if cur:
        raise ValueError(f"dangling names: {c}")
    return out


def clause_hi(c, neg=False):
    gs = clause_groups(c)
    if len(gs) == 1:
        g, k, n = gs[0]
        return f"{group_hi(g)} {pred_hi(k, n, neg)}", n
    if neg:
        raise ValueError(f"negated 'both' clause: {c}")
    parts = [f"{group_hi(g)} {pred_hi(k, n, bhi=True)}" for g, k, n in gs]
    return " और ".join(parts), gs[0][2]


# ---------------------------------------------------------------- questions
Q_RE = re.compile(r"(?:\((Ka|Kha)\) )?(Yo|yo|Yato|yato)( vā pana)?( yato)? (.+?) (sānusayo|niranusayo) "
                  r"(so tato|so|tato) (.+?) (sānusayo|niranusayo)ti\?")


def question(s):
    m = Q_RE.fullmatch(s)
    if not m:
        return None
    lab, rel, vp, yato2, g1, p1, cor, g2, p2 = m.groups()
    lab = (S.LABELS[f"({lab})"] + " ") if lab else ""
    aur = "और " if vp else ""
    a = f"{group_hi(g1)} {pred_hi(*PREDS[p1])}"
    b = f"{group_hi(g2)} {pred_hi(*PREDS[p2])}"
    rel = rel.lower()
    if rel == "yo" and not yato2 and cor == "so":           # person
        return f"{lab}{aur}जो व्यक्ति {a}, क्या वह {b}?"
    if rel == "yo" and yato2 and cor == "so tato":          # person and place
        return f"{lab}{aur}जो व्यक्ति जिस स्थान पर {a}, क्या वह वहाँ {b}?"
    if rel == "yato" and not yato2 and cor == "tato":       # place
        return f"{lab}{aur}जिस स्थान पर कोई {a}, क्या वहाँ वह {b}?"
    raise ValueError(f"question frame: {s}")


# ---------------------------------------------------------------- answers
def places_prefix(toks):
    """Consume place tokens from the front -> (Hindi chunk list, remaining tokens)."""
    chunks = []
    i = 0
    while i < len(toks):
        for seq, hi in PLACES:
            if tuple(t.lower() if i + j == 0 else t for j, t in enumerate(toks[i:i + len(seq)])) == seq:
                chunks.append(hi)
                i += len(seq)
                break
        else:
            break
    return chunks, toks[i:]


def answer(s):
    if not s.endswith("."):
        return None
    body = s[:-1]
    subj, num_s = None, None
    for k, (hi, n) in SUBJECTS.items():
        if body.startswith(k + " "):
            subj, num_s = hi, n
            body = body[len(k) + 1:]
            break
    toks = body.split(" ")
    places, toks = places_prefix(toks)
    marker = None
    rest = " ".join(toks)
    for mk in ("so tato ", "te tato ", "tato ", "sabbattha "):
        if rest.startswith(mk):
            marker, rest = mk.strip(), rest[len(mk):]
            break
    if not subj and not places and not marker:
        rest = rest[0].lower() + rest[1:]
    m = re.fullmatch(r"(.+?),? no ca (?:(so tato|te tato|tato) )?(.+)", rest)
    c1, c2, mk2 = (m.group(1), m.group(3), m.group(2)) if m else (rest, None, None)
    if c1.split(" ")[0] not in NAMES:
        return None
    h1, n1 = clause_hi(c1)
    h2 = clause_hi(c2, neg=True)[0] if c2 else None
    place_hi = S.JOIN.join(places[:-1]) + S.JOIN_LAST + places[-1] if len(places) > 1 else (places[0] if places else "")

    if subj and not places and not marker:                       # person: «A X है, पर Y नहीं है।»
        if mk2:
            raise ValueError(f"person answer with tato: {s}")
        return f"{subj} {h1}" + (f", पर {h2}" if h2 else "") + "।"
    if not subj and places and marker == "tato":                 # place: «P में कोई X है, पर वहाँ वह Y नहीं है।»
        if c2 and mk2 != "tato":
            raise ValueError(f"place answer: {s}")
        return f"{place_hi} कोई {h1}" + (f", पर वहाँ वह {h2}" if h2 else "") + "।"
    if subj and places and marker in ("so tato", "te tato"):     # person and place
        if c2 and mk2 != marker:
            raise ValueError(f"person-place answer: {s}")
        return f"{subj} {place_hi} {h1}" + (f", पर {PRON[num_s]} वहाँ {h2}" if h2 else "") + "।"
    if subj and not places and marker == "sabbattha" and not c2:  # «… सब जगह X भी है और Y भी है।»
        return f"{subj} {SABBATTHA} {h1}।"
    if not subj and not places and not marker and not c2:       # short answer «X वाला है।»
        return f"{h1}।"
    raise ValueError(f"answer frame: {s}")


# ---------------------------------------------------------------- driver
def translate_sentence(s):
    if s in CLOSINGS:
        return CLOSINGS[s]
    if s in MULAKA_LABELS:
        return MULAKA_LABELS[s]
    m = re.fullmatch(r"(.*?)( ?)…pe…\.", s)                     # abbreviated end: «…।»
    if m:
        inner = translate_sentence(m.group(1) + ".")
        return inner[:-1] + "…।"      # "Āmantā …pe…." and "Āmantā…pe…." alike: «हाँ…।»
    s2 = s[0].upper() + s[1:] if s.startswith("yo") else s
    for fn in (question, answer):
        r = fn(s) or (fn(s2) if s2 != s else None)
        if r:
            return r
    raise ValueError(f"no formula for: {s}")


def translate_line(line):
    bid = ""
    m = S.ID_RE.search(line)
    if m:
        bid = " " + m.group(1)
        line = line[: m.start()]
    if line.startswith("#"):
        hashes, text = line.split(" ", 1)
        return f"{hashes} {HEADINGS[text.strip()]}{bid}"
    sents = S._split_sentences(line.strip())
    return " ".join(translate_sentence(x) for x in sents) + bid


def translate_text(txt):
    out, prev_blank = [], True
    for line in txt.splitlines():
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
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry" in sys.argv
    files = args or ["7-03-anusayayamaka.md", "7-04-anusayayamaka.md"]
    for f in files:
        hi = translate_text((S.PALI_DIR / f).read_text(encoding="utf-8"))
        if dry:
            print(hi)
        else:
            (S.HI_DIR / f).write_text(hi, encoding="utf-8", newline="\n")
            print("written", f)


if __name__ == "__main__":
    main()
