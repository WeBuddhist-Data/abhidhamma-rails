# Builder for pi-6 Hindi plain RAILS: 7-07-anusayayamaka.md, 7-08-anusayayamaka.md (Pariññāvāra).
# Imports build_rails_sample.py read-only for the shared constants; new formulas are listed in notes-7-07-7-08.md.
# The frames mirror the Pajahanavāra builder (build_7-05-7-06.py), which has the same Pāli with pajahati, so that
# Pariññā and Pajahana differ only in the verb (and the place postposition, see the notes).
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\rails")
import build_rails_sample as S  # noqa: E402

FILES = ["7-07-anusayayamaka.md", "7-08-anusayayamaka.md"]

# ---------------- terms (termbase) ----------------
ANUSAYA = {  # stem -> Hindi (termbase, fem. sg.)
    "kāmarāgānusay": "इंद्रिय-सुखों के राग की सुप्त प्रवृत्ति",
    "paṭighānusay": "चिढ़ की सुप्त प्रवृत्ति",
    "mānānusay": "अहंकार की सुप्त प्रवृत्ति",
    "diṭṭhānusay": "दृष्टि की सुप्त प्रवृत्ति",
    "vicikicchānusay": "संशय की सुप्त प्रवृत्ति",
    "bhavarāgānusay": "अस्तित्व के राग की सुप्त प्रवृत्ति",
    "avijjānusay": "अज्ञान की सुप्त प्रवृत्ति",
}
# parijānāti: person sg. (formulas §11), plural, and the impersonal passive for the place frames (no person in the Pāli)
VERB = {
    "sg": S.PARIJANATI["parijānāti"],                       # पूरी तरह समझता है / पूरी तरह नहीं समझता
    "pl": ("पूरी तरह समझते हैं", "पूरी तरह नहीं समझते"),
    "pass": ("पूरी तरह समझा जाता है", "पूरी तरह नहीं समझा जाता"),
}
TAD = "{pro} साथ रहने वाली"                          # tadekaṭṭhaṃ (pi-1 tadekaṭṭhā = «उनके साथ रहने वाले»)
TAD_BARE = "{pro} साथ रहने वाली {noun} को {v}"        # Tadekaṭṭhaṃ parijānāti.

PERSONS = {  # nominative subjects
    "Sveva puggalo": "वही व्यक्ति",
    "Aggamaggasamaṅgī": "सर्वोच्च मार्ग से युक्त व्यक्ति",
    "Anāgāmimaggasamaṅgī": "फिर न लौटने के मार्ग से युक्त व्यक्ति",
    "Aṭṭhamako": "आठवें स्तर का व्यक्ति",
}
EXCEPT = {  # X ṭhapetvā avasesā puggalā -> «X को छोड़कर शेष व्यक्ति»
    "Dvinnaṃ maggasamaṅgīnaṃ": "मार्ग से युक्त दो व्यक्तियों",
    "Dvinnaṃ maggasamaṅgīnañca aṭṭhamakañca": "मार्ग से युक्त दो व्यक्तियों और आठवें स्तर के व्यक्ति",
    "Anāgāmimaggasamaṅgiñca aṭṭhamakañca": "फिर न लौटने के मार्ग से युक्त व्यक्ति और आठवें स्तर के व्यक्ति",
    "Aggamaggasamaṅgiñca aṭṭhamakañca": "सर्वोच्च मार्ग से युक्त व्यक्ति और आठवें स्तर के व्यक्ति",
    "Anāgāmimaggasamaṅgiṃ": "फिर न लौटने के मार्ग से युक्त व्यक्ति",
    "Aggamaggasamaṅgiṃ": "सर्वोच्च मार्ग से युक्त व्यक्ति",
}
AVASESA_PUGGALA = "को छोड़कर शेष व्यक्ति"
SABBATTHA = "सभी स्थानों पर"                          # sabbattha (= 7-01/7-02)

PLACES = [  # (Pāli chunk, lower case) -> Hindi chunk, every chunk ends in «में» (formulas §10)
    ("kāmadhātuyā dvīsu vedanāsu", "इंद्रिय-सुखों के लोक की दो अनुभूतियों में"),
    ("kāmadhātuyā tīsu vedanāsu", "इंद्रिय-सुखों के लोक की तीन अनुभूतियों में"),
    ("dukkhāya vedanāya", "दुःखद अनुभूति में"),
    ("rūpadhātuyā", "सूक्ष्म भौतिक लोक में"),
    ("arūpadhātuyā", "अभौतिक लोक में"),
    ("apariyāpanne", "अस्तित्व के लोकों में न समाई हुई परिघटनाओं में"),   # pi-1 ^1-M2-96
]

CYCLE = {  # closing labels of a cycle (= 7-03..7-06)
    "(Ekamūlakaṃ)": "(एक मूल पर आधारित)", "(Dukamūlakaṃ)": "(दो मूलों पर आधारित)",
    "(Tikamūlakaṃ)": "(तीन मूलों पर आधारित)", "(Catukkamūlakaṃ)": "(चार मूलों पर आधारित)",
    "(Pañcakamūlakaṃ)": "(पाँच मूलों पर आधारित)", "(Chakkamūlakaṃ)": "(छह मूलों पर आधारित)",
}
CLOSE = {
    "Pariññāvāre anulomaṃ.": "पूरी तरह समझने के खंड में सकारात्मक।",
    "Pariññāvāre paṭilomaṃ.": "पूरी तरह समझने के खंड में विपरीत।",
    "Pariññāvāro.": S.CLOSINGS["Pariññāvāro."],
}
SHORT = {"Āmantā": S.AMANTA[:-1], "No": S.NO[:-1], "Natthi": S.NATTHI[:-1]}
HEADINGS = dict(S.HEADINGS)
HEADINGS.update({
    "Pariññāvāra": "पूरी तरह समझने का खंड",
    "(Gha) paṭilomapuggalo": "(घ) विपरीत: व्यक्ति",
    "(Ṅa) paṭilomaokāso": "(ङ) विपरीत: स्थान",
    "(Ca) paṭilomapuggalokāsā": "(च) विपरीत: व्यक्ति और स्थान",
})
# source slips: read as intended (reported)
SLIPS = {
    # 7-07 ^6-7-243 line 1: "na" missing before the second verb of a paṭiloma question (the answer is negative)
    "(Ka) yato paṭighānusayaṃ na parijānāti tato mānānusayaṃ parijānātīti?":
        "(Ka) yato paṭighānusayaṃ na parijānāti tato mānānusayaṃ na parijānātīti?",
}


def join_list(items):
    if len(items) == 1:
        return items[0]
    return S.JOIN.join(items[:-1]) + S.JOIN_LAST + items[-1]


def term(tok):
    t = tok[0].lower() + tok[1:]
    for end in ("añca", "aṃ"):
        if t.endswith(end) and t[: -len(end)] in ANUSAYA:
            return ANUSAYA[t[: -len(end)]]
    raise ValueError(f"unknown term: {tok}")


def q_objs(o):
    """Question object phrase (without «को») and its count; 'A…pe… B' = «A… B», counted as one."""
    if "…pe…" in o:
        a, b = o.split("…pe… ")
        return f"{term(a)}… {term(b)}", 1
    names = [term(t) for t in o.split()]
    return join_list(names), len(names)


class Ctx:
    last_q = (1, 1)   # object counts of the last question (for the bare «Tadekaṭṭhaṃ parijānāti.»)


# ---------------- questions ----------------
Q_RE = re.compile(
    r"(?:\((Ka|Kha)\) )?(yo|Yo|yato|Yato)( vā pana)?( yato)? (.+?) (na )?parijānāti (so tato|so|tato) (.+?) (na )?parijānātīti\?")


def question(s):
    m = Q_RE.fullmatch(s)
    if not m:
        return None
    lab, rel, vp, yato2, o1, n1, cor, o2, n2 = m.groups()
    rel = rel.lower()
    label = (S.LABELS[f"({lab})"] + " ") if lab else ""
    vapana = "और " if vp else ""
    if rel == "yo" and yato2:
        assert cor == "so tato", s
        r, c, mode = "जो व्यक्ति जिस स्थान पर", "वह वहाँ", "sg"
    elif rel == "yo":
        assert cor == "so", s
        r, c, mode = "जो व्यक्ति", "वह", "sg"
    else:
        assert cor == "tato" and not yato2, s
        r, c, mode = "जिस स्थान पर", "वहाँ", "pass"
    h1, c1 = q_objs(o1)
    h2, c2 = q_objs(o2)
    Ctx.last_q = (c1, c2)
    return (f"{label}{vapana}{r} {h1} को {VERB[mode][1 if n1 else 0]}, "
            f"क्या {c} {h2} को {VERB[mode][1 if n2 else 0]}?")


# ---------------- answers ----------------
OBJ_RE = re.compile(r"\S+ānusay(?:aṃ|añca)")


def parse_vps(text):
    """'Xñca na parijānanti Yñca na parijānanti' -> [(objs, tad, neg)]; a stray comma is ignored."""
    vps, cur, tad, neg = [], [], False, False
    for t in text.replace(",", "").split():
        if OBJ_RE.fullmatch(t):
            cur.append(term(t))
        elif t in ("tadekaṭṭhaṃ", "Tadekaṭṭhaṃ"):
            tad = True
        elif t == "na":
            neg = True
        elif t in ("parijānāti", "parijānanti"):
            vps.append((cur, tad, neg))
            cur, tad, neg = [], False, False
        else:
            raise ValueError(f"unknown token {t!r} in: {text}")
    if cur or tad or neg:
        raise ValueError(f"dangling tokens in: {text}")
    return vps


def clause(text, mode, flip=False):
    vps = parse_vps(text)
    vb = lambda neg: VERB[mode][1 if (neg != flip) else 0]   # noqa: E731
    if len(vps) == 1:
        objs, tad, neg = vps[0]
        if tad and not objs:                                   # Tadekaṭṭhaṃ parijānāti.
            n1, n2 = Ctx.last_q
            return TAD_BARE.format(pro="उसके" if n1 == 1 else "उनके",
                                   noun="सुप्त प्रवृत्ति" if n2 == 1 else "सुप्त प्रवृत्तियों", v=vb(neg))
        assert not tad, text
        return f"{join_list(objs)} को {vb(neg)}"
    if len(vps) == 2:
        (o1, t1, n1), (o2, t2, n2) = vps
        assert not t1, text
        if t2:                                                 # A V (,) B tadekaṭṭhaṃ V
            pro = "उसके" if len(o1) == 1 else "उनके"
            return f"{join_list(o1)} को {vb(n1)} और {TAD.format(pro=pro)} {join_list(o2)} को {vb(n2)}"
        return f"{join_list(o1)} को भी {vb(n1)} और {join_list(o2)} को भी {vb(n2)}"
    raise ValueError(f"{len(vps)} verb phrases: {text}")


def places(rest):
    chunks = []
    while True:
        low = rest[0].lower() + rest[1:] if rest else rest
        for p, h in PLACES:
            if low.startswith(p + " ") or low.startswith(p + ", "):
                chunks.append(h)
                rest = rest[len(p):].lstrip(", ").lstrip()
                break
        else:
            return chunks, rest


def statement(body):
    subj, mode = None, None
    for k, v in PERSONS.items():
        if body.startswith(k + " "):
            subj, mode, body = v, "sg", body[len(k) + 1:]
            break
    else:
        m = re.match(r"(.+?) ṭhapetvā avasesā puggalā( sabbattha)? ", body)
        if m:
            subj = f"{EXCEPT[m.group(1)]} {AVASESA_PUGGALA}" + (f" {SABBATTHA}" if m.group(2) else "")
            mode, body = "pl", body[m.end():]
    pl, body = places(body)
    so = tato = False
    if body.startswith("so "):
        so, body = True, body[3:]
    if body.startswith("tato "):
        tato, body = True, body[5:]
    if pl and not subj:
        assert tato and not so, body
        mode = "pass"                                          # place answer, no person in the Pāli
    if mode is None:
        mode = "sg"                                            # bare answer in the person frame
    if ", no ca " in body:
        c1, c2 = body.split(", no ca ", 1)
    else:
        c1, c2 = body, None
    head = " ".join(x for x in [subj, join_list(pl) if pl else None] if x)
    hi = (head + " " if head else "") + clause(c1, mode)
    if c2 is not None:
        pre = []
        if c2.startswith("so "):
            pre.append("वह")
            c2 = c2[3:]
        if c2.startswith("tato "):
            pre.append("वहाँ")
            c2 = c2[5:]
        hi += ", पर " + " ".join(pre + [clause(c2, mode, flip=True)])
    return hi


def sentence(s):
    if s in CLOSE:
        return CLOSE[s]
    if s in CYCLE:
        return CYCLE[s]
    if s.endswith("?"):
        r = question(s)
        if r:
            return r
        raise ValueError(f"no question formula: {s}")
    assert s.endswith("."), s
    body, pe = s[:-1], ""
    m = re.search(r"( ?)…pe…$", body)
    if m:
        pe, body = m.group(1) + "…", body[: m.start()]
    hi = SHORT[body] if body in SHORT else statement(body)
    return hi + pe + "।"


def text_line(line):
    line = SLIPS.get(line, line)
    return " ".join(sentence(x) for x in S._split_sentences(line))


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
        hashes, t = line.split(" ", 1)
        return f"{hashes} {HEADINGS[t]}{bid}"
    return text_line(line) + bid


def translate_text(pali):
    out, prev_blank = [], True
    for line in pali.splitlines():
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


def build():
    for f in FILES:
        pali = (S.PALI_DIR / f).read_bytes().decode("utf-8")
        (S.HI_DIR / f).write_text(translate_text(pali), encoding="utf-8", newline="\n")
        print("built", f)


if __name__ == "__main__":
    build()
