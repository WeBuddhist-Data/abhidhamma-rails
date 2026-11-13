"""Builder for pi-6 Hindi plain RAILS: 7-05-anusayayamaka.md and 7-06-anusayayamaka.md (Pajahanavāra).

usage: python -I -X utf8 build_7-05-7-06.py [7-05-anusayayamaka.md 7-06-anusayayamaka.md]
Imports build_rails_sample read-only (short answers, labels). Unknown Pāli raises ValueError.
"""
import re
import sys
import pathlib

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\rails")
import build_rails_sample as S  # noqa: E402  (read-only)

PALI_DIR = S.PALI_DIR
HI_DIR = S.HI_DIR

# ------------------------------------------------------------------ terms (termbase)
TEND = {
    "kāmarāg": "इंद्रिय-सुखों के राग की सुप्त प्रवृत्ति",
    "paṭigh": "चिढ़ की सुप्त प्रवृत्ति",
    "mān": "अहंकार की सुप्त प्रवृत्ति",
    "diṭṭh": "दृष्टि की सुप्त प्रवृत्ति",
    "vicikicch": "संशय की सुप्त प्रवृत्ति",
    "bhavarāg": "अस्तित्व के राग की सुप्त प्रवृत्ति",
    "avijj": "अज्ञान की सुप्त प्रवृत्ति",
}
TEND_RE = re.compile(r"^(kāmarāg|paṭigh|mān|diṭṭh|vicikicch|bhavarāg|avijj)ānusay(aṃ|añca)$", re.I)

# places, as the source of abandoning (Pāli locative + tato) -> Hindi oblique + «से»
PLACES = [
    ("kāmadhātuyā dvīsu vedanāsu", "इंद्रिय-सुखों के लोक की दो अनुभूतियों"),
    ("kāmadhātuyā tīsu vedanāsu", "इंद्रिय-सुखों के लोक की तीन अनुभूतियों"),
    ("dukkhāya vedanāya", "दुःखद अनुभूति"),
    ("rūpadhātuyā", "सूक्ष्म भौतिक लोक"),
    ("arūpadhātuyā", "अभौतिक लोक"),
    ("apariyāpanne", "अस्तित्व के लोकों में न समाई हुई परिघटनाओं"),
]
PLACE_POST = "से"

SUBJECTS = {
    "Aggamaggasamaṅgī": "सर्वोच्च मार्ग से युक्त व्यक्ति",
    "Anāgāmimaggasamaṅgī": "फिर न लौटने के मार्ग से युक्त व्यक्ति",
    "Aṭṭhamako": "आठवें स्तर का व्यक्ति",
    "Sveva puggalo": "वही व्यक्ति",
}
EXCL = {  # members of "<X> ṭhapetvā" (oblique)
    "dvinnaṃ maggasamaṅgīnaṃ": "मार्ग से युक्त दो व्यक्तियों",
    "dvinnaṃ maggasamaṅgīnañca": "मार्ग से युक्त दो व्यक्तियों",
    "aggamaggasamaṅgiñca": "सर्वोच्च मार्ग से युक्त व्यक्ति",
    "aggamaggasamaṅgiṃ": "सर्वोच्च मार्ग से युक्त व्यक्ति",
    "anāgāmimaggasamaṅgiñca": "फिर न लौटने के मार्ग से युक्त व्यक्ति",
    "anāgāmimaggasamaṅgiṃ": "फिर न लौटने के मार्ग से युक्त व्यक्ति",
    "aṭṭhamakañca": "आठवें स्तर के व्यक्ति",
}
EXCL_TAIL = "को छोड़कर शेष व्यक्ति"      # <X> ṭhapetvā avasesā puggalā
SABBATTHA = "सभी स्थानों से"             # sabbattha (in the abandoning frame)
TAD = "{pro} साथ रहने वाली"              # tadekaṭṭhaṃ
TAD_BARE = "{pro} साथ रहने वाली {noun} को {v}"   # Tadekaṭṭhaṃ pajahati.

# verbs: (positive, negative)
V_ACT = ("छोड़ता है", "नहीं छोड़ता")          # pajahati / nappajahati (person)
V_ACT_PL = ("छोड़ते हैं", "नहीं छोड़ते")       # pajahanti / nappajahanti
V_PASS = ("छोड़ा जाता है", "नहीं छोड़ा जाता")   # place frame, no person: impersonal passive
VERB_TOK = {"pajahati": (False, False), "nappajahati": (True, False),
            "pajahanti": (False, True), "nappajahanti": (True, True)}

# question frames: rel -> (Hindi relative, Hindi correlative, mode)
Q_REL = {
    "yo": ("जो व्यक्ति", "क्या वह", "act"),
    "yo vā pana": ("और जो व्यक्ति", "क्या वह", "act"),
    "yo yato": ("जो व्यक्ति जिस स्थान से", "क्या वह वहाँ से", "act"),
    "yo vā pana yato": ("और जो व्यक्ति जिस स्थान से", "क्या वह वहाँ से", "act"),
    "yato": ("जिस स्थान से", "क्या वहाँ से", "pass"),
    "yato vā pana": ("और जिस स्थान से", "क्या वहाँ से", "pass"),
}
Q_CORR = {"yo": "so", "yo vā pana": "so", "yo yato": "so tato", "yo vā pana yato": "so tato",
          "yato": "tato", "yato vā pana": "tato"}
Q_RE = re.compile(
    r"^(?:(?P<lab>\((?:Ka|Kha)\)) )?(?P<rel>[Yy]o vā pana yato|[Yy]o yato|[Yy]o vā pana|[Yy]o|[Yy]ato vā pana|[Yy]ato) "
    r"(?P<o1>.+?) (?P<v1>nappajahati|pajahati) (?P<corr>so tato|so|tato) (?P<o2>.+?) "
    r"(?P<v2>nappajahatīti|pajahatīti)\?$")

CYCLE = {
    "Ekamūlakaṃ": "एक मूल पर आधारित", "Dukamūlakaṃ": "दो मूलों पर आधारित",
    "Tikamūlakaṃ": "तीन मूलों पर आधारित", "Catukkamūlakaṃ": "चार मूलों पर आधारित",
    "Pañcakamūlakaṃ": "पाँच मूलों पर आधारित", "Chakkamūlakaṃ": "छह मूलों पर आधारित",
}
HEAD = {
    "Pajahanavāro": "छोड़ने का खंड",
    "Pajahanavāra": "छोड़ने का खंड",
    "(Ka) anulomapuggalo": "(क) सकारात्मक: व्यक्ति",
    "(Kha) anulomaokāso": "(ख) सकारात्मक: स्थान",
    "(Ga) anulomapuggalokāsā": "(ग) सकारात्मक: व्यक्ति और स्थान",
    "(Gha) paṭilomapuggalo": "(घ) विपरीत: व्यक्ति",
    "(Ṅa) paṭilomaokāso": "(ङ) विपरीत: स्थान",
    "(Ca) paṭilomapuggalokāsā": "(च) विपरीत: व्यक्ति और स्थान",
}
HEAD_MODE = {"puggalo": "person", "okāso": "place", "puggalokāsā": "pp"}
CLOSING = {
    "Pajahanavāre anulomaṃ.": "छोड़ने के खंड में सकारात्मक।",
    "Pajahanāvāre paṭilomaṃ.": "छोड़ने के खंड में विपरीत।",
    "Pajahanavāro.": "छोड़ने का खंड।",
}
SHORT = {"Āmantā": S.AMANTA[:-1], "No": S.NO[:-1], "Natthi": S.NATTHI[:-1]}

SLIPS = []


def join_list(items, last=" और "):
    if len(items) == 1:
        return items[0]
    return ", ".join(items[:-1]) + last + items[-1]


def objs_of(text):
    """'kāmarāgānusayañca paṭighānusayañca' -> list of Hindi names; '…pe…' ranges kept."""
    out = []
    for tok in text.split():
        m = TEND_RE.match(tok)
        if not m:
            raise ValueError(f"object token: {tok!r} in {text!r}")
        out.append(TEND[m.group(1).lower()])
    return out


def q_obj(text):
    """question object, possibly 'diṭṭhānusayaṃ…pe… vicikicchānusayaṃ'."""
    if "…pe…" in text:
        a, b = text.split("…pe…")
        return objs_of(a.strip())[0] + "… " + join_list(objs_of(b.strip())), 1
    lst = objs_of(text)
    return join_list(lst), len(lst)


class Ctx:
    mode = "person"
    last_q = (1, 1)


def question(s, ctx):
    m = Q_RE.match(s)
    if not m:
        return None
    rel = m.group("rel")
    rel_l = rel[0].lower() + rel[1:]
    if Q_CORR[rel_l] != m.group("corr"):
        raise ValueError(f"correlative mismatch: {s}")
    hrel, hcorr, kind = Q_REL[rel_l]
    vm = V_ACT if kind == "act" else V_PASS
    o1, n1 = q_obj(m.group("o1"))
    o2, n2 = q_obj(m.group("o2"))
    v1 = vm[1] if m.group("v1").startswith("napp") else vm[0]
    v2 = vm[1] if m.group("v2").startswith("napp") else vm[0]
    ctx.last_q = (n1, n2)
    lab = (S.LABELS[m.group("lab")] + " ") if m.group("lab") else ""
    return f"{lab}{hrel} {o1} को {v1}, {hcorr} {o2} को {v2}?"


def parse_vps(text):
    """'Xañca pajahati Yañca pajahati' -> [(objs, tad, neg, plural)]"""
    vps, objs, tad = [], [], False
    for tok in text.replace(",", " , ").split():
        if tok == ",":
            SLIPS.append(text)
            continue
        if tok in VERB_TOK:
            neg, pl = VERB_TOK[tok]
            vps.append((objs, tad, neg, pl))
            objs, tad = [], False
        elif tok == "tadekaṭṭhaṃ" or tok == "Tadekaṭṭhaṃ":
            tad = True
        else:
            objs.extend(objs_of(tok))
    if objs or tad:
        raise ValueError(f"dangling objects: {text}")
    return vps


def verb(neg, pl, passive, flip=False):
    vm = V_PASS if passive else (V_ACT_PL if pl else V_ACT)
    n = (not neg) if flip else neg
    return vm[1] if n else vm[0]


def clause(vps, passive, ctx, flip=False):
    if len(vps) == 1:
        objs, tad, neg, pl = vps[0]
        v = verb(neg, pl, passive, flip)
        if tad and not objs:
            n1, n2 = ctx.last_q
            pro = "उसके" if n1 == 1 else "उनके"
            noun = "सुप्त प्रवृत्ति" if n2 == 1 else "सुप्त प्रवृत्तियों"
            return TAD_BARE.format(pro=pro, noun=noun, v=v)
        if tad:
            raise ValueError("tadekaṭṭhaṃ with objects in a single VP")
        return f"{join_list(objs)} को {v}"
    if len(vps) == 2:
        (o1, t1, n1, p1), (o2, t2, n2, p2) = vps
        v1, v2 = verb(n1, p1, passive, flip), verb(n2, p2, passive, flip)
        if t1:
            raise ValueError("tadekaṭṭhaṃ in first VP")
        if t2:
            pro = "उसके" if len(o1) == 1 else "उनके"
            return f"{join_list(o1)} को {v1} और {TAD.format(pro=pro)} {join_list(o2)} को {v2}"
        return f"{join_list(o1)} को भी {v1} और {join_list(o2)} को भी {v2}"
    raise ValueError(f"{len(vps)} VPs")


def statement(s, ctx):
    """one answer sentence without its final punctuation."""
    rest = s
    subj, plural = None, False
    for k, v in SUBJECTS.items():
        if rest.startswith(k + " "):
            subj, rest = v, rest[len(k) + 1:]
            break
    if subj is None:
        m = re.match(r"^(?P<ex>.+?) ṭhapetvā avasesā puggalā (?P<sab>sabbattha )?", rest)
        if m:
            ex = m.group("ex")
            parts = []
            toks = ex.split()
            i = 0
            while i < len(toks):
                two = " ".join(toks[i:i + 2]).lower()
                if two in EXCL:
                    parts.append(EXCL[two]); i += 2
                elif toks[i].lower() in EXCL:
                    parts.append(EXCL[toks[i].lower()]); i += 1
                else:
                    raise ValueError(f"exclusion: {ex}")
            subj = f"{join_list(parts)} {EXCL_TAIL}" + (f" {SABBATTHA}" if m.group("sab") else "")
            plural = True
            rest = rest[m.end():]
    places = []
    while True:
        low = rest.lower()
        for p, h in PLACES:
            if low.startswith(p + " "):
                places.append(f"{h} {PLACE_POST}")
                rest = rest[len(p) + 1:]
                break
        else:
            break
    for lead in ("so tato ", "tato "):
        if rest.startswith(lead):
            rest = rest[len(lead):]
            break
    passive = (ctx.mode == "place") and subj is None
    m = re.search(r",? no ca (?P<pro>so tato|so|tato) ", rest)
    neg_part = None
    if m:
        if not rest[m.start():].startswith(","):
            SLIPS.append(s)
        pos_part, neg_part, npro = rest[:m.start()], rest[m.end():], m.group("pro")
    else:
        pos_part = rest
    out = []
    if subj:
        out.append(subj)
    if places:
        out.append(join_list(places))
    out.append(clause(parse_vps(pos_part), passive, ctx))
    hi = " ".join(out)
    if neg_part is not None:
        hpro = {"so tato": "वह वहाँ से", "so": "वह", "tato": "वहाँ से"}[npro]
        hi += f", पर {hpro} {clause(parse_vps(neg_part), passive, ctx, flip=True)}"
    return hi


def sentence(s, ctx):
    end = s[-1]
    body = s[:-1]
    pe = ""
    mpe = re.search(r"( ?)…pe…$", body)
    if mpe:
        pe = mpe.group(1) + "…"
        body = body[:mpe.start()]
    if end == "?":
        q = question(s, ctx)
        if q is None:
            raise ValueError(f"question: {s}")
        return q
    if body in SHORT:
        hi = SHORT[body]
    else:
        hi = statement(body, ctx)
    hend = {".": "।", ";": ";"}[end]
    return hi + pe + hend


def translate_line(line, ctx):
    bid = ""
    m = re.search(r" (\^[0-9a-z-]+)$", line)
    if m:
        bid, line = " " + m.group(1), line[:m.start()]
    hm = re.match(r"^(#+) (.+)$", line)
    if hm:
        txt = hm.group(2)
        for k, mode in HEAD_MODE.items():
            if txt.endswith(k):
                ctx.mode = mode
        return f"{hm.group(1)} {HEAD[txt]}{bid}"
    if line in CLOSING:
        return CLOSING[line] + bid
    lab = ""
    m = re.search(r" \((\w+)\)$", line)
    if m and m.group(1) in CYCLE:
        lab, line = f" ({CYCLE[m.group(1)]})", line[:m.start()]
    sents = re.split(r"(?<=[.?;])\s+", line.strip())
    return " ".join(sentence(x, ctx) for x in sents) + lab + bid


def build(name):
    src = (PALI_DIR / name).read_text(encoding="utf-8").replace("\r", "")
    ctx = Ctx()
    out, blank = [], False
    for line in src.split("\n"):
        if not line.strip():
            if out and not blank:
                out.append("")
            blank = True
            continue
        blank = False
        out.append(translate_line(line.rstrip(), ctx))
    while out and out[-1] == "":
        out.pop()
    (HI_DIR / name).write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
    print(name, "lines", len([o for o in out if o]), "slips", len(SLIPS))


if __name__ == "__main__":
    for n in (sys.argv[1:] or ["7-05-anusayayamaka.md", "7-06-anusayayamaka.md"]):
        SLIPS.clear()
        build(n)
        for s in SLIPS:
            print("  slip:", s[:160])
