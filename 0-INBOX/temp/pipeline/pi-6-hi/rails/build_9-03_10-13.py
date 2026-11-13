"""pi-6 Yamaka, 9-03-dhammayamaka.md and 10-13-indriyayamaka.md: Pāli -> Hindi plain RAILS builder.

Imports read-only:
  build_rails_sample.py (S: headings, closings, frames, beings)
  build_9-01-9-02.py    (D: the Dhammayamaka process formulas of the sibling files 9-01 / 9-02, so that
                         identical Pāli gets identical Hindi across 9-01 … 9-03)
Adds: the Dhammayamaka bhāvanā questions, the closing lines of 9-03 / 10-13, and the Indriya pariññā /
pajahana / bhāvanā / sacchikiriyā questions and answers (notes-9-03-10-13.md).
Every Pāli line must match a formula; an unknown line raises ValueError.

usage: python -I -X utf8 build_9-03_10-13.py [--dry] [9-03-dhammayamaka.md 10-13-indriyayamaka.md]
"""
import importlib.util
import re
import sys

RAILS = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\rails"
sys.path.insert(0, RAILS)
import build_rails_sample as S  # noqa: E402  (read-only)

_spec = importlib.util.spec_from_file_location("build_9_01_9_02", RAILS + r"\build_9-01-9-02.py")
D = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(D)  # read-only: defines constants and functions only

# ------------------------------------------------------------------------------------------------
# Closings of the two files
# ------------------------------------------------------------------------------------------------
CLOSINGS = dict(D.CLOSINGS)
CLOSINGS.update({
    "Bhāvanāvāro.": "अभ्यास का खंड।",                                   # NEW (cf. Pariññāvāro. = … खंड।)
    "Dhammayamakaṃ niṭṭhitaṃ.": S.CHAPTER_END.format(title=S.CHAPTER_TITLES["Dhammayamakaṃ"]),
    "Indriyayamakaṃ niṭṭhitaṃ.": S.CHAPTER_END.format(title=S.CHAPTER_TITLES["Indriyayamakaṃ"]),
    "Yamakapakaraṇaṃ niṭṭhitaṃ.": S.BOOK_END,
    "Āmantā…pe….": "हाँ…।",
})
LINES = {"Abhidhammapiṭake": S.ABHIDHAMMA}  # whole line (no punctuation, as in the preamble heading)

# ------------------------------------------------------------------------------------------------
# Source slips, corrected before translation (the Pāli file is never touched); see notes
# ------------------------------------------------------------------------------------------------
SLIPS = [
    # 9-03 ^6-9-192: comma inside the being chain
    ("aggamaggaṃ paṭilabhissanti, asaññasattānaṃ", "aggamaggaṃ paṭilabhissanti asaññasattānaṃ"),
    # 10-13 ^6-10-452: missing comma, comma for full stop, bhavissanti for bhāvessanti
    ("Dve puggalā aññindriyaṃ bhāvessanti no ca domanassindriyaṃ pajahissanti, pañca puggalā aññindriyañca "
     "bhavissanti domanassindriyañca pajahissanti.",
     "Dve puggalā aññindriyaṃ bhāvessanti, no ca domanassindriyaṃ pajahissanti. Pañca puggalā aññindriyañca "
     "bhāvessanti domanassindriyañca pajahissanti."),
    # 10-13 ^6-10-455: question ending with "." instead of "?"
    ("anaññātaññassāmītindriyaṃ na bhāvessatīti. Āmantā.", "anaññātaññassāmītindriyaṃ na bhāvessatīti? Āmantā."),
    ("so cakkhundriyaṃ na parijānissatīti.", "so cakkhundriyaṃ na parijānissatīti?"),
    # 10-13 ^6-10-468: one sentence run together, plural verbs with a singular subject
    ("no ca domanassindriyaṃ pajahanti anāgāmimaggasamaṅgi aññindriyañca bhāvessanti, domanassindriyañca pajahanti.",
     "no ca domanassindriyaṃ pajahanti. Anāgāmimaggasamaṅgī aññindriyañca bhāvessati domanassindriyañca pajahati."),
    # 10-13 ^6-10-477: stray full stop inside the question, missing comma before no ca
    ("aññindriyaṃ bhāvessati. So anaññāt", "aññindriyaṃ bhāvessati so anaññāt"),
    ("Dve puggalā aññindriyaṃ bhāvessanti no ca", "Dve puggalā aññindriyaṃ bhāvessanti, no ca"),
    # 10-13 ^6-10-480: nappajjahittha
    ("nappajjahittha", "nappajahittha"),
]

# ------------------------------------------------------------------------------------------------
# Practice verbs (subject = a person). post = postposition of the object.
# forms: pres sg / pres pl / past (ergative, invariant) / fut sg / fut pl -> (positive, negative)
# ------------------------------------------------------------------------------------------------
PV = {
    "parijānāti": ("को", {
        "pres_sg": ("पूरी तरह समझता है", "पूरी तरह नहीं समझता"),
        "pres_pl": ("पूरी तरह समझते हैं", "पूरी तरह नहीं समझते"),
        "past": ("पूरी तरह समझा था", "पूरी तरह नहीं समझा था"),
        "fut_sg": ("पूरी तरह समझेगा", "पूरी तरह नहीं समझेगा"),
        "fut_pl": ("पूरी तरह समझेंगे", "पूरी तरह नहीं समझेंगे")}),
    "pajahati": ("को", {
        "pres_sg": ("छोड़ता है", "नहीं छोड़ता"),
        "pres_pl": ("छोड़ते हैं", "नहीं छोड़ते"),
        "past": ("छोड़ा था", "नहीं छोड़ा था"),
        "fut_sg": ("छोड़ेगा", "नहीं छोड़ेगा"),
        "fut_pl": ("छोड़ेंगे", "नहीं छोड़ेंगे")}),
    "bhāveti": ("का", {
        "pres_sg": ("अभ्यास करता है", "अभ्यास नहीं करता"),
        "pres_pl": ("अभ्यास करते हैं", "अभ्यास नहीं करते"),
        "past": ("अभ्यास किया था", "अभ्यास नहीं किया था"),
        "fut_sg": ("अभ्यास करेगा", "अभ्यास नहीं करेगा"),
        "fut_pl": ("अभ्यास करेंगे", "अभ्यास नहीं करेंगे")}),
    "sacchikaroti": ("का", {
        "pres_sg": ("साक्षात्कार करता है", "साक्षात्कार नहीं करता"),
        "pres_pl": ("साक्षात्कार करते हैं", "साक्षात्कार नहीं करते"),
        "past": ("साक्षात्कार किया था", "साक्षात्कार नहीं किया था"),
        "fut_sg": ("साक्षात्कार करेगा", "साक्षात्कार नहीं करेगा"),
        "fut_pl": ("साक्षात्कार करेंगे", "साक्षात्कार नहीं करेंगे")}),
}
# Pāli token -> (verb, tense); tense: pres | past | fut (number comes from the subject)
VTOK = {}
VTOK.update({
    "parijānāti": ("parijānāti", "pres"), "parijānanti": ("parijānāti", "pres"),
    "parijānittha": ("parijānāti", "past"),
    "parijānissati": ("parijānāti", "fut"), "parijānissanti": ("parijānāti", "fut"),
    "pajahati": ("pajahati", "pres"), "pajahanti": ("pajahati", "pres"), "pajahittha": ("pajahati", "past"),
    "pajahissati": ("pajahati", "fut"), "pajahissanti": ("pajahati", "fut"),
    "bhāveti": ("bhāveti", "pres"), "bhāventi": ("bhāveti", "pres"), "bhāvittha": ("bhāveti", "past"),
    "bhāvessati": ("bhāveti", "fut"), "bhāvessanti": ("bhāveti", "fut"),
    "sacchikaroti": ("sacchikaroti", "pres"), "sacchikaronti": ("sacchikaroti", "pres"),
    "sacchikarittha": ("sacchikaroti", "past"),
    "sacchikarissati": ("sacchikaroti", "fut"), "sacchikarissanti": ("sacchikaroti", "fut"),
})
_VTOK_ALL = set(VTOK) | {"napp" + k[1:] for k in VTOK if k.startswith("pajah")}


def _vparse(tok):
    """'na parijānāti' / 'nappajahati' / 'bhāvittha' -> (verb, tense, negative)."""
    neg = tok.startswith("na ")
    w = tok[3:] if neg else tok
    if w.startswith("nappajah"):
        neg, w = True, w[3:]
    verb, tense = VTOK[w]
    return verb, tense, neg


def vform(tok, num, flip=False):
    """Hindi verb phrase for the token; num = sg | pl (of the subject)."""
    verb, tense, neg = _vparse(tok)
    key = "past" if tense == "past" else f"{tense}_{num}"
    pos, negs = PV[verb][1][key]
    return (negs if neg != flip else pos), PV[verb][0], tense == "past"


# ------------------------------------------------------------------------------------------------
# Objects
# ------------------------------------------------------------------------------------------------
INDRIYA = {  # termbase
    "cakkhundriya": "आँख की क्षमता",
    "sotindriya": "कान की क्षमता",
    "domanassindriya": "उदासी की क्षमता",
    "anaññātaññassāmītindriya": "“जो अब तक नहीं जाना उसे मैं जान लूँगा” की क्षमता",
    "aññindriya": "पूर्ण ज्ञान की क्षमता",
    "aññātāvindriya": "पूर्ण ज्ञान पा चुके की क्षमता",
}
OBJ = {}
for _k, _v in INDRIYA.items():
    OBJ[_k + "ṃ"] = _v
    OBJ[_k + "ñca"] = _v
OBJ.update({"kusalaṃ dhammaṃ": "हितकर परिघटना", "akusalaṃ dhammaṃ": "हानिकर परिघटना"})
MULAKA = {k[0].upper() + k[1:] + "mūlakaṃ": f"({v} पर आधारित)" for k, v in INDRIYA.items()}
_OBJ_RE = "|".join(sorted(map(re.escape, OBJ), key=len, reverse=True))


def obj(o, post, verb, bhi=False):
    """«X को पूरी तरह समझता है» / «X का भी अभ्यास करता है»."""
    return f"{OBJ[o]} {post}{' भी' if bhi else ''} {verb}"


# ------------------------------------------------------------------------------------------------
# Questions: (Ka) yo [vā pana] O1 V1 so O2 V2ti?  (harmonise B10, formulas §11)
# ------------------------------------------------------------------------------------------------
def practice_question(s):
    m = re.fullmatch(rf"{S._LAB} yo( vā pana)? ({_OBJ_RE}) ((?:na )?\S+) so ({_OBJ_RE}) ((?:na )?\S+)\?", s)
    if not m:
        return None
    lab, vp, o1, v1, o2, v2 = m.groups()
    neg2 = v2.startswith("na ")
    v2 = ("na " if neg2 else "") + S.strip_ti(v2[3:] if neg2 else v2, _VTOK_ALL)
    h1, p1, past1 = vform(v1, "sg")
    h2, p2, past2 = vform(v2, "sg")
    rel = ("और " if vp else "") + ("जिस व्यक्ति ने" if past1 else "जो व्यक्ति")
    cor = "उसने" if past2 else "वह"
    return f"{S.LABELS[f'({lab})']} {rel} {obj(o1, p1, h1)}, क्या {cor} {obj(o2, p2, h2)}?"


def bhavana_question(s):
    """9-03: (Ka) yo kusalaṃ dhammaṃ bhāveti so akusalaṃ dhammaṃ pajahatīti?"""
    return practice_question(s)


# ------------------------------------------------------------------------------------------------
# Answers: subjects
# ------------------------------------------------------------------------------------------------
NUM = {"Dve": "दो", "Tayo": "तीन", "Cattāro": "चार", "Pañca": "पाँच", "Cha": "छह", "Satta": "सात", "Aṭṭha": "आठ"}
SIGLA = {"sī.": "Sī.", "syā.": "Syā.", "ka.": "Ka.", "pī.": "Pī."}


def variant(br):
    """'[satta (sī. syā. ka.)]' -> «[पाठभेद (Sī., Syā., Ka.): satta]» (words differ)."""
    m = re.fullmatch(r"\[(.+) \(([^)]+)\)\]", br)
    sig = ", ".join(SIGLA[x] for x in m.group(2).split(" "))
    return f"[पाठभेद ({sig}): {m.group(1)}]"


# singular persons: (direct, ergative)
PERSON_SG = {
    "Aggamaggasamaṅgī": ("सर्वोच्च मार्ग से युक्त व्यक्ति", "सर्वोच्च मार्ग से युक्त व्यक्ति ने"),
    "Anāgāmimaggasamaṅgī": ("फिर न लौटने के मार्ग से युक्त व्यक्ति", "फिर न लौटने के मार्ग से युक्त व्यक्ति ने"),
    "Aṭṭhamako": ("आठवें स्तर का व्यक्ति", "आठवें स्तर के व्यक्ति ने"),
    "Arahā": ("अर्हत्", "अर्हत् ने"),
    "Anāgāmī": ("फिर न लौटने वाला", "फिर न लौटने वाले ने"),
    "Yo aggaphalaṃ sacchikaroti so": ("जो व्यक्ति सर्वोच्च फल का साक्षात्कार करता है, वह",
                                      "जो व्यक्ति सर्वोच्च फल का साक्षात्कार करता है, उसने"),
    "Yo aggaphalaṃ sacchākāsi so": ("जिस व्यक्ति ने सर्वोच्च फल का साक्षात्कार कर लिया है, वह",
                                    "जिस व्यक्ति ने सर्वोच्च फल का साक्षात्कार कर लिया है, उसने"),
}
PERSON_PL = {
    "Ye puthujjanā maggaṃ paṭilabhissanti te": ("जो साधारण व्यक्ति मार्ग प्राप्त करेंगे, वे",
                                                "जो साधारण व्यक्ति मार्ग प्राप्त करेंगे, उन्होंने"),
    "Ye puthujjanā maggaṃ na paṭilabhissanti te": ("जो साधारण व्यक्ति मार्ग प्राप्त नहीं करेंगे, वे",
                                                   "जो साधारण व्यक्ति मार्ग प्राप्त नहीं करेंगे, उन्होंने"),
}
# excepted groups before «को छोड़कर» (oblique)
EXCEPT = {
    "Aggamaggasamaṅgiñca arahantañca": "सर्वोच्च मार्ग से युक्त व्यक्ति और अर्हत्",
    "Anāgāmimaggasamaṅgiñca arahantañca": "फिर न लौटने के मार्ग से युक्त व्यक्ति और अर्हत्",
    "Aṭṭhamakañca arahantañca": "आठवें स्तर के व्यक्ति और अर्हत्",
}


def _group(numw, br=None, obl=False):
    """'Tayo maggasamaṅgino' -> «मार्ग से युक्त तीन व्यक्ति / व्यक्तियों» (+ variant bracket)."""
    h = f"मार्ग से युक्त {NUM[numw]} {'व्यक्तियों' if obl else 'व्यक्ति'}"
    return h + (" " + variant(br) if br else "")


def subject(s, erg):
    """Pāli subject -> (Hindi, number). erg: the first verb is past (Hindi ergative «ने»)."""
    if s in PERSON_SG:
        return PERSON_SG[s][1 if erg else 0], "sg"
    if s in PERSON_PL:
        return PERSON_PL[s][1 if erg else 0], "pl"
    m = re.fullmatch(r"(\S+)( \[[^\]]+\])? puggalā", s)
    if m and m.group(1) in NUM:
        br = " " + variant(m.group(2).strip()) if m.group(2) else ""
        return f"{NUM[m.group(1)]}{br} {'व्यक्तियों ने' if erg else 'व्यक्ति'}", "pl"
    m = re.fullmatch(r"(\S+) maggasamaṅgino( \[[^\]]+\])?", s)
    if m and m.group(1) in NUM:
        g = _group(m.group(1), m.group(2).strip() if m.group(2) else None, obl=erg)
        return g + (" ने" if erg else ""), "pl"
    m = re.fullmatch(r"(.+?)( \[[^\]]+\])? ṭhapetvā avasesā puggalā", s)
    if m:
        x, br = m.group(1), (m.group(2).strip() if m.group(2) else None)
        if x in EXCEPT:
            ex = EXCEPT[x] + (" " + variant(br) if br else "")
        else:
            mm = re.fullmatch(r"(\S+) maggasamaṅgino( ca arahantañca)?", x)
            if not mm or mm.group(1) not in NUM:
                raise ValueError(f"except group: {x}")
            ex = _group(mm.group(1), br, obl=True) + (" और अर्हत्" if mm.group(2) else "")
        return f"{ex} को छोड़कर शेष {'व्यक्तियों ने' if erg else 'व्यक्ति'}", "pl"
    raise ValueError(f"subject: {s!r}")


PRON = {("sg", False): "वह", ("pl", False): "वे", ("sg", True): "उसने", ("pl", True): "उन्होंने"}


def practice_sentence(s):
    m = re.fullmatch(rf"(.+?) ({_OBJ_RE}) ((?:na )?\S+), no ca ({_OBJ_RE}) ((?:na )?\S+)\.", s)
    both = False
    if not m:
        m = re.fullmatch(rf"(.+?) ({_OBJ_RE}) ((?:na )?\S+) ({_OBJ_RE}) ((?:na )?\S+)\.", s)
        if not m or not (m.group(2).endswith("ñca") and m.group(4).endswith("ñca")):
            return None
        both = True
    sj, o1, v1, o2, v2 = m.groups()
    past1 = _vparse(v1)[1] == "past"
    past2 = _vparse(v2)[1] == "past"
    sh, num = subject(sj, past1)
    h1, p1, _ = vform(v1, num)
    h2, p2, _ = vform(v2, num, flip=not both)
    pron = (PRON[(num, past2)] + " ") if past1 != past2 else ""
    if both:
        return f"{sh} {obj(o1, p1, h1, bhi=True)} और {pron}{obj(o2, p2, h2, bhi=True)}।"
    return f"{sh} {obj(o1, p1, h1)}, पर {pron}{obj(o2, p2, h2)}।"


def mulaka_note(s):
    m = re.fullmatch(r"\((\S+)\)(\.?)", s)
    if m and m.group(1) in MULAKA:
        return MULAKA[m.group(1)] + ("।" if m.group(2) else "")
    return None


# ------------------------------------------------------------------------------------------------
# Driver
# ------------------------------------------------------------------------------------------------
def translate_sentence(s):
    if s in CLOSINGS:
        return CLOSINGS[s]
    for fn in (mulaka_note, practice_question, practice_sentence):
        r = fn(s)
        if r:
            return r
    return D.translate_sentence(s)


def translate_line(line):
    if not line.strip():
        return ""
    bid = ""
    m = S.ID_RE.search(line)
    if m:
        bid = " " + m.group(1)
        line = line[: m.start()]
    line = line.strip()
    if line.startswith("#"):
        return D.translate_line(line) + bid
    if line in LINES:
        return LINES[line] + bid
    for a, b in SLIPS:
        line = line.replace(a, b)
    out = [translate_sentence(x) for x in S._split_sentences(line)]
    return " ".join(out) + bid


def translate_text(pali_text):
    out, prev_blank = [], True
    for line in pali_text.splitlines():
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


def main(args):
    dry = "--dry" in args
    files = [a for a in args if a != "--dry"] or ["9-03-dhammayamaka.md", "10-13-indriyayamaka.md"]
    for f in files:
        pali = (S.PALI_DIR / f).read_text(encoding="utf-8")
        hi = translate_text(pali)
        if dry:
            print(f"dry ok {f}: {len(hi.splitlines())} lines")
        else:
            (S.HI_DIR / f).write_text(hi, encoding="utf-8", newline="\n")
            print("built", f)


if __name__ == "__main__":
    main(sys.argv[1:])
