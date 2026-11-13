"""Builder for pi-6 Hindi plain RAILS, Anusayayamaka 7-01 and 7-02 (anusayavāra, anuloma + paṭiloma).

usage: python -I -X utf8 build_7-01_7-02.py [7-01-anusayayamaka.md ...]
Imports build_rails_sample.py read-only (labels, short answers, question frame, relative frames, joins).
Every unknown sentence raises ValueError, so nothing is passed through untranslated.
"""
import re
import sys
import pathlib

RAILS = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\rails")
sys.path.insert(0, str(RAILS))
import build_rails_sample as S  # noqa: E402  (read-only)

PALI_DIR = S.PALI_DIR
HI_DIR = S.HI_DIR
FILES = ["7-01-anusayayamaka.md", "7-02-anusayayamaka.md"]

# ---------------------------------------------------------------------------------------------------
# Words (termbase, inflected)
# ---------------------------------------------------------------------------------------------------
ANUSAYA = {
    "kāmarāgānusayo": "इंद्रिय-सुखों के राग की सुप्त प्रवृत्ति",
    "kāmārāgānusayo": "इंद्रिय-सुखों के राग की सुप्त प्रवृत्ति",   # source spelling slip (termbase variant)
    "paṭighānusayo": "चिढ़ की सुप्त प्रवृत्ति",
    "mānānusayo": "अहंकार की सुप्त प्रवृत्ति",
    "diṭṭhānusayo": "दृष्टि की सुप्त प्रवृत्ति",
    "vicikicchānusayo": "संशय की सुप्त प्रवृत्ति",
    "bhavarāgānusayo": "अस्तित्व के राग की सुप्त प्रवृत्ति",
    "avijjānusayo": "अज्ञान की सुप्त प्रवृत्ति",
}
# verb token -> (negative?, plural?)
VERB = {
    "anuseti": (False, False), "anusenti": (False, True), "anusanti": (False, True),  # anusanti: source slip
    "nānuseti": (True, False), "nānusenti": (True, True),
}
VERB_TI = {"anusetīti": "anuseti", "anusentīti": "anusenti", "nānusetīti": "nānuseti", "nānusentīti": "nānusenti"}
# anuseti = सोई रहती है (termbase सोया रहना, fem. सुप्त प्रवृत्ति)
HV = {(False, False): "सोई रहती है", (True, False): "सोई नहीं रहती",
      (False, True): "सोई रहती हैं", (True, True): "सोई नहीं रहतीं"}

# places where a tendency lies latent (each chunk keeps «में»)
PLACES = [
    ("kāmadhātuyā dvīsu vedanāsu", "इंद्रिय-सुखों के लोक की दो अनुभूतियों में"),
    ("kāmadhātuyā tīsu vedanāsu", "इंद्रिय-सुखों के लोक की तीन अनुभूतियों में"),
    ("dukkhāya vedanāya", "दुःखद अनुभूति में"),
    ("rūpadhātuyā", "सूक्ष्म भौतिक लोक में"),
    ("arūpadhātuyā", "अभौतिक लोक में"),
    ("apariyāpanne", "अस्तित्व के लोकों में न समाई हुई परिघटनाओं में"),            # pi-1 apariyāpanna
    ("sabbasakkāyapariyāpannesu dhammesu", "व्यक्तित्व में समाई हुई सभी परिघटनाओं में"),
]
SABBATTHA = "सभी स्थानों पर"

# persons (genitive) -> (Hindi chunk, plural?)
WHO = [
    ("anāgāmissa", "फिर न लौटने वाले में", False),
    ("arahato", "अर्हत् में", False),
    ("puthujjanassa", "साधारण व्यक्ति में", False),
    ("tasseva puggalassa", "उसी व्यक्ति में", False),
    ("tiṇṇaṃ puggalānaṃ", "तीन व्यक्तियों में", True),
    ("dvinnaṃ puggalānaṃ", "दो व्यक्तियों में", True),
    ("catunnaṃ puggalānaṃ", "चार व्यक्तियों में", True),
    ("tesaññeva puggalānaṃ", "उन्हीं व्यक्तियों में", True),
]
CORR = {"tassa": "उसमें", "tesaṃ": "उनमें", "tattha": "वहाँ",
        "tassa tattha": "उसमें वहाँ", "tesaṃ tattha": "उनमें वहाँ"}

CYCLE = {"ekamūlakaṃ": "एक पर आधारित", "dukamūlakaṃ": "दो पर आधारित", "tikamūlakaṃ": "तीन पर आधारित",
         "catukkamūlakaṃ": "चार पर आधारित", "pañcakamūlakaṃ": "पाँच पर आधारित", "chakkamūlakaṃ": "छह पर आधारित"}

HEAD = {
    "Anusayayamakaṃ": S.CHAPTER_TITLES["Anusayayamakaṃ"],
    "Uppattiṭṭhānavāro": "उत्पन्न होने के स्थान का खंड",
    "Mahāvāro 1. anusayavāro": "बड़ा खंड 1. सुप्त प्रवृत्तियों का खंड",
    "Anusayavāra": "सुप्त प्रवृत्तियों का खंड",
    "(Ka) anulomapuggalo": S.HEADINGS["(Ka) anulomapuggalo"],
    "(Kha) anulomaokāso": S.HEADINGS["(Kha) anulomaokāso"],
    "(Ga) anulomapuggalokāsā": S.HEADINGS["(Ga) anulomapuggalokāsā"],
    "(Gha) paṭilomapuggalo": "(घ) विपरीत: व्यक्ति",
    "(Ṅa) paṭilomaokāso": "(ङ) विपरीत: स्थान",
    "(Ca) paṭilomapuggalokāsā": "(च) विपरीत: व्यक्ति और स्थान",
}
FIXED = {
    "Sattānusayā – kāmarāgānusayo, paṭighānusayo, mānānusayo, diṭṭhānusayo, vicikicchānusayo, "
    "bhavarāgānusayo, avijjānusayo.":
        "सात सुप्त प्रवृत्तियाँ – " + ", ".join(ANUSAYA[k] for k in (
            "kāmarāgānusayo", "paṭighānusayo", "mānānusayo", "diṭṭhānusayo", "vicikicchānusayo",
            "bhavarāgānusayo", "avijjānusayo")) + "।",
    "Uppattiṭṭhānavāro.": "उत्पन्न होने के स्थान का खंड।",
    "Anusayavāre anulomaṃ.": "सुप्त प्रवृत्तियों के खंड में सकारात्मक।",
    "Anusayavāre paṭilomaṃ.": "सुप्त प्रवृत्तियों के खंड में विपरीत।",
    "Anusayavāro.": "सुप्त प्रवृत्तियों का खंड।",
    "Āmantā.": S.AMANTA,
    "No.": S.NO,
    "Natthi.": S.NATTHI,
    "Āmantā …pe….": "हाँ …।",
    "(Kha) yattha vā pana…pe…?": "(ख) और जिस स्थान पर…?",
}

PE = "…pe…"


# ---------------------------------------------------------------------------------------------------
def group_hi(items, conj):
    """items: anusaya names, with 'PE' markers; conj: the names are joined by ca (one subject group)."""
    out = []
    for it in items:
        if it == "PE":
            out[-1] += "…"
        else:
            out.append(ANUSAYA[it])
    if not conj:          # alternatives in an abbreviated question: «X… Y»
        return " ".join(out)
    if len(out) == 1:
        return out[0]
    return ", ".join(out[:-1]) + " और " + out[-1]


def clause_segments(text):
    """'X ca Y ca anusenti Z ca anuseti' -> [(items, conj, verb), ...]"""
    toks = text.replace(PE, " " + PE + " ").split()
    segs, items, conj = [], [], False
    for t in toks:
        tl = t.lower()
        if tl in VERB_TI:
            tl = VERB_TI[tl]
        if t == PE:
            items.append("PE")
        elif tl == "ca":
            conj = True
        elif tl in ANUSAYA:
            items.append(tl)
        elif tl in VERB:
            if not items:
                raise ValueError(f"verb without subject: {text!r}")
            segs.append((items, conj, tl))
            items, conj = [], False
        else:
            raise ValueError(f"unknown token {t!r} in {text!r}")
    if items:
        raise ValueError(f"subject without verb: {text!r}")
    return segs


def verb_hi(tok, flip=False):
    neg, pl = VERB[tok]
    return HV[(neg != flip, pl)]


def clause_hi(text, flip=False):
    segs = clause_segments(text)
    if len(segs) == 1:
        items, conj, v = segs[0]
        return f"{group_hi(items, conj)} {verb_hi(v, flip)}"
    if len(segs) == 2 and not flip:
        (i1, c1, v1), (i2, c2, v2) = segs
        return f"{group_hi(i1, c1)} भी {verb_hi(v1)} और {group_hi(i2, c2)} भी {verb_hi(v2)}"
    raise ValueError(f"clause shape: {text!r}")


def take_places(s):
    chunks = []
    while True:
        for p, h in PLACES:
            if s.lower().startswith(p + " "):
                chunks.append(h)
                s = s[len(p) + 1:]
                break
        else:
            return chunks, s


def join_chain(chunks):
    if len(chunks) == 1:
        return chunks[0]
    return S.JOIN.join(chunks[:-1]) + S.JOIN_LAST + chunks[-1]


def answer_hi(s):
    """Statement: [who] [places] [tassa/tesaṃ tattha | ettha | sabbattha] clause[, no ca <corr> clause]."""
    body = s[:-1] if s.endswith(".") else s
    tail = ""
    if body.endswith(PE):
        body = body[: -len(PE)]
        tail = " …" if body.endswith(" ") else "…"
        body = body.rstrip()
    parts = body.split(", no ca ")
    if len(parts) > 2:
        raise ValueError(f"two 'no ca' in {s!r}")
    first = parts[0]
    pre = []
    for w, h, _pl in WHO:
        if first.lower().startswith(w + " ") or first.lower() == w:
            pre.append(h)
            first = first[len(w) + 1:]
            break
    places, first = take_places(first)
    if places:
        pre.append(join_chain(places))
    for r in ("tassa tattha ", "tesaṃ tattha ", "ettha "):
        if first.startswith(r):
            if not places:
                raise ValueError(f"resumptive without place: {s!r}")
            first = first[len(r):]
            break
    if first.startswith("sabbattha"):
        pre.append(SABBATTHA)
        first = first[len("sabbattha"):].strip()
    if not first:                       # "Dvinnaṃ puggalānaṃ sabbattha…pe…."
        return " ".join(pre) + tail + "।"
    hi = " ".join(pre + [clause_hi(first)])
    if len(parts) == 2:
        second = parts[1]
        for c in ("tassa tattha", "tesaṃ tattha", "tassa", "tesaṃ", "tattha"):
            if second.startswith(c + " "):
                hi += f", पर {CORR[c]} {clause_hi(second[len(c) + 1:], flip=True)}"
                break
        else:
            raise ValueError(f"no correlative in {s!r}")
    return hi + tail + "।"


_REL = r"(yassa vā pana yattha|yassa yattha|yassa vā pana|yassa|yattha vā pana|yattha)"
_Q = re.compile(r"^(?:\((Ka|Kha)\) )?" + _REL + r" (.+? (?:nānusenti|nānuseti|anusenti|anuseti)) "
                r"(tassa tattha|tassa|tattha) (.+)\?$", re.I)


def question_hi(s):
    m = _Q.match(s)
    if not m:
        raise ValueError(f"question? {s!r}")
    lab, rel, c1, cor, c2 = m.groups()
    rel, cor = rel.lower(), cor.lower()
    rel_hi, cor_hi = S.REL_FRAMES[(rel, cor)]
    label = S.LABELS[f"({lab})"] + " " if lab else ""
    return f"{label}{rel_hi} {clause_hi(c1)}, क्या {cor_hi} {clause_hi(c2)}?"


_KATTHA = re.compile(r"^Kattha (\S+) anuseti\?$")


def sentence_hi(s):
    s = s.strip()
    if s in FIXED:
        return FIXED[s]
    m = re.fullmatch(r"\((\w+) ?\)", s)
    if m and m.group(1).lower() in CYCLE:
        return f"({CYCLE[m.group(1).lower()]})"
    m = _KATTHA.match(s)
    if m:
        return f"{ANUSAYA[m.group(1)]} कहाँ सोई रहती है?"
    if s.endswith("?"):
        return question_hi(s)
    return answer_hi(s)


_SPLIT = re.compile(r"(?<=[.?]) (?=[A-ZĀĪŪṬḌṆÑṄ(])")


def line_hi(line):
    m = S.ID_RE.search(line)
    bid = ""
    if m:
        bid = " " + m.group(1)
        line = line[: m.start()]
    line = line.strip()
    h = re.match(r"^(#+) (.+)$", line)
    if h:
        return f"{h.group(1)} {HEAD[h.group(2)]}{bid}"
    if line in FIXED:
        return FIXED[line] + bid
    sents = _SPLIT.split(line)
    return " ".join(sentence_hi(x) for x in sents) + bid


def build(name):
    src = (PALI_DIR / name).read_text(encoding="utf-8").replace("\r\n", "\n")
    out = []
    for line in src.split("\n"):
        out.append(line_hi(line) if line.strip() else "")
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text).strip("\n") + "\n"
    (HI_DIR / name).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", name, len([x for x in out if x]), "lines")


if __name__ == "__main__":
    for f in (sys.argv[1:] or FILES):
        build(f)
