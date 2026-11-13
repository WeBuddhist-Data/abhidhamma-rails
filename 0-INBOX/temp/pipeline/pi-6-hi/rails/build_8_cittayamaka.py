"""pi-6 Cittayamaka (8-cittayamaka.md) Pāli -> Hindi plain RAILS.

Imports build_rails_sample.py read-only (constants: LABELS, VERBS, HEADINGS, CHAPTER_TITLES, AMANTA, NO, NATTHI,
_split_sentences). New formulas of this chapter are listed in notes-8.md.
usage: python -I -X utf8 build_8_cittayamaka.py [--dry]
"""
import re
import sys
import pathlib

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\rails")
import build_rails_sample as S  # noqa: E402  (read-only)

SRC = S.PALI_DIR / "8-cittayamaka.md"
OUT = S.HI_DIR / "8-cittayamaka.md"

# ---------------------------------------------------------------------------------------------------
# Headings
# ---------------------------------------------------------------------------------------------------
HEADINGS = dict(S.HEADINGS)
HEADINGS.update({
    "Suddhacittasāmaññaṃ": "सामान्य रूप से केवल मन",
    "Suddhacittasāmañña": "सामान्य रूप से केवल मन",
    "(1) Uppādanirodhakālasambhedavāro": "(1) उत्पन्न होने और समाप्त होने के समयों के मेल का खंड",
    "(2) Uppāduppannavāro": "(2) उत्पन्न होने और उत्पन्न हो चुके होने का खंड",
    "(3) Nirodhuppannavāro": "(3) समाप्त होने और उत्पन्न हो चुके होने का खंड",
    "(4) Uppādavāro": "(4) उत्पन्न होने का खंड",
    "(5) Nirodhavāro": "(5) समाप्त होने का खंड",
    "(6) Uppādanirodhavāro": "(6) उत्पन्न होने और समाप्त होने का खंड",
    "(7) Uppajjamāna-nanirodhavāro": "(7) उत्पन्न होते हुए होने और समाप्त न होने का खंड",
    "(7) Uppajjamānananirodhavāro": "(7) उत्पन्न होते हुए होने और समाप्त न होने का खंड",
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

# ---------------------------------------------------------------------------------------------------
# Predicates of the mind (masculine singular मन). (positive, negative, positive with «भी» for ceva … ca)
# ---------------------------------------------------------------------------------------------------
PRED = {}
for stem in ("uppajjati", "uppajjittha", "uppajjissati", "nirujjhati", "nirujjhittha", "nirujjhissati"):
    pos, neg = S.VERBS[(stem, "m")]
    w = pos.split(" ", 1)
    PRED[stem] = (pos, neg, f"{w[0]} भी {w[1]}")
PRED.update({
    "uppannaṃ": ("उत्पन्न हो चुका है", "उत्पन्न हो चुका नहीं है", "उत्पन्न भी हो चुका है"),
    "uppajjamānaṃ": ("उत्पन्न होता हुआ है", "उत्पन्न होता हुआ नहीं है", "उत्पन्न होता हुआ भी है"),
    "nirujjhamānaṃ": ("समाप्त होता हुआ है", "समाप्त होता हुआ नहीं है", "समाप्त होता हुआ भी है"),
    "niruddhaṃ": ("समाप्त हो चुका है", "समाप्त हो चुका नहीं है", "समाप्त भी हो चुका है"),
})
NEG_BHI = {k: v[1].replace(" नहीं", " भी नहीं", 1) for k, v in PRED.items()}  # na V ceva … («समाप्त भी नहीं होता»)
# short answers
SHORT = {"Uppajjittha.": "उत्पन्न हुआ था।", "Uppajjissati.": "उत्पन्न होगा।", "Nirujjhittha.": "समाप्त हुआ था।",
         "Nirujjhissati.": "समाप्त होगा।", "Nirujjhati.": "समाप्त होता है।", "Uppannaṃ.": "उत्पन्न हो चुका है।",
         "Āmantā.": S.AMANTA, "No.": S.NO, "Natthi.": S.NATTHI}

# kinds of mind (termbase; vītadosa / vītamoha / sukhāya from pi-2 / pi-1 rails Hindi)
ADJ = {
    "sarāgaṃ": "राग-युक्त", "vītarāgaṃ": "राग से मुक्त", "sadosaṃ": "द्वेष-युक्त", "vītadosaṃ": "द्वेष से मुक्त",
    "samohaṃ": "मोह-युक्त", "vītamohaṃ": "मोह से मुक्त", "saṃkhittaṃ": "सिमटा हुआ", "vikkhittaṃ": "बिखरा हुआ",
    "mahaggataṃ": "उन्नत", "amahaggataṃ": "उन्नत न होने वाला", "sauttaraṃ": "सर्वोच्च न होने वाला",
    "anuttaraṃ": "सर्वोच्च", "samāhitaṃ": "एकाग्र", "asamāhitaṃ": "एकाग्रता से रहित", "vimuttaṃ": "मुक्त",
    "avimuttaṃ": "अमुक्त", "kusalaṃ": "हितकर", "akusalaṃ": "हानिकर", "abyākataṃ": "नैतिक रूप से अनिर्धारित",
    "sukhāya vedanāya sampayuttaṃ": "सुखद अनुभूति से जुड़ा", "araṇaṃ": "संघर्ष से रहित",
}
MIND = "मन"


def stem_of(w):
    return w


def vp_hi(vp, flip=False):
    """'uppajjati' / 'na uppajjati' / 'uppajjati na nirujjhati' / 'na uppajjati nirujjhati' -> Hindi."""
    toks = vp.split(" ")
    parts, neg = [], False
    for t in toks:
        if t == "na":
            neg = True
            continue
        n = neg != flip
        parts.append(PRED[t][1] if n else PRED[t][0])
        neg = False
    return " और ".join(parts)


def strip_ti(line):
    """Drop the quotative -ti of the word before '?'."""
    def rep(m):
        w = m.group(1)
        if w.endswith("īti"):
            w = w[:-3] + "i"
        elif w.endswith("āti"):
            w = w[:-3] + "a"
        elif w.endswith("nti"):
            w = w[:-3] + "ṃ"
        return w + "?"
    return re.sub(r"(\S+ti)\?", rep, line)


# ---------------------------------------------------------------------------------------------------
# Subjects of the answers
# ---------------------------------------------------------------------------------------------------
WHO = {  # before 'tesaṃ' (persons)
    "Pacchimacittassa uppādakkhaṇe": "अंतिम मन के उत्पन्न होने के क्षण में",
    "Pacchimacittassa bhaṅgakkhaṇe": "अंतिम मन के भंग होने के क्षण में",
    "Cittassa uppādakkhaṇe": "मन के उत्पन्न होने के क्षण में",
    "Cittassa bhaṅgakkhaṇe": "मन के भंग होने के क्षण में",
    "Itaresaṃ cittassa uppādakkhaṇe": "बाकी सबमें मन के उत्पन्न होने के क्षण में",
    "Itaresaṃ cittassa bhaṅgakkhaṇe": "बाकी सबमें मन के भंग होने के क्षण में",
    "Nirodhasamāpannānaṃ asaññasattānaṃ":
        "समाप्ति की ध्यान-अवस्था में लीन लोगों में और पहचान-रहित प्राणियों में",
    "Cittassa bhaṅgakkhaṇe nirodhasamāpannānaṃ asaññasattānaṃ":
        "मन के भंग होने के क्षण में, समाप्ति की ध्यान-अवस्था में लीन लोगों में और पहचान-रहित प्राणियों में",
    "Cittassa uppādakkhaṇe nirodhasamāpannānaṃ asaññasattānaṃ":
        "मन के उत्पन्न होने के क्षण में, समाप्ति की ध्यान-अवस्था में लीन लोगों में और पहचान-रहित प्राणियों में",
    "Pacchimacittasamaṅgīnaṃ": "अंतिम मन से युक्त लोगों में",
    "Cittasamaṅgīnaṃ": "मन से युक्त लोगों में",
    "Itaresaṃ cittasamaṅgīnaṃ": "बाकी मन से युक्त लोगों में",
    "Itaresaṃ": "बाकी सबमें",
    "Sarāgapacchimacittassa uppādakkhaṇe": "राग-युक्त अंतिम मन के उत्पन्न होने के क्षण में",
    "Itaresaṃ sarāgacittassa uppādakkhaṇe": "बाकी सबमें राग-युक्त मन के उत्पन्न होने के क्षण में",
    "Pacchimakusalacittassa uppādakkhaṇe": "अंतिम हितकर मन के उत्पन्न होने के क्षण में",
    "Itaresaṃ kusalacittassa uppādakkhaṇe": "बाकी सबमें हितकर मन के उत्पन्न होने के क्षण में",
}
MIND_SUBJ = {  # before 'cittaṃ' (the mind itself, Dhammavāra) -> modifier of «मन»
    "Bhaṅgakkhaṇe": "भंग होने के क्षण का",
    "Uppādakkhaṇe": "उत्पन्न होने के क्षण का",
    "Atītaṃ": "अतीत का",
    "Anāgataṃ": "भविष्य का",
    "Paccuppannaṃ": "वर्तमान",
    "Atītānāgataṃ": "अतीत और भविष्य का",
    "Bhaṅgakkhaṇe anāgatañca": "भंग होने के क्षण का और भविष्य का",
    "Uppādakkhaṇe anāgatañca": "उत्पन्न होने के क्षण का और भविष्य का",
    "Bhaṅgakkhaṇe atītañca": "भंग होने के क्षण का और अतीत का",
}
MOMENT = {"Bhaṅgakkhaṇe": "भंग होने के क्षण में", "Uppādakkhaṇe": "उत्पन्न होने के क्षण में"}  # no 'cittaṃ'
PRON = {"tesaṃ": "उनमें ", "taṃ": "वह ", "tassa taṃ": "उसमें वह ", None: ""}


def subject(subj, tesam, has_citta, adj):
    a = (ADJ[adj] + " ") if adj else ""
    if tesam:
        return f"{WHO[subj]} {a}{MIND}"
    if has_citta:
        return f"{MIND_SUBJ[subj]} {a}{MIND}"
    return MOMENT[subj]


_ADJ_RE = "(?:(" + "|".join(sorted((re.escape(k) for k in ADJ), key=len, reverse=True)) + ") )?"
_P = r"(?:uppajjati|uppajjittha|uppajjissati|nirujjhati|nirujjhittha|nirujjhissati|uppannaṃ|uppajjamānaṃ|nirujjhamānaṃ|niruddhaṃ)"
_VP = rf"((?:na )?{_P}(?: (?:na )?{_P})?)"


def answer_sentence(s):
    if s in SHORT:
        return SHORT[s]
    # ^6-8-63/114/115: <who> tesaṃ [adj] cittaṃ VPc, VPc.  |  …, V ceva V ca.
    m = re.fullmatch(rf"(.+?) tesaṃ {_ADJ_RE}cittaṃ {_VP}, (?:{_VP}|(\S+) ceva (\S+) ca)\.", s)
    if m and "no ca" not in s:
        subj, adj, vp1, vp2, b1, b2 = m.groups()
        sh = subject(subj, True, True, adj)
        tail = vp_hi(vp2) if vp2 else f"{PRED[b1][2]} और {PRED[b2][2]}"
        return f"{sh} {vp_hi(vp1)}, {tail}।"
    # <subj> [tesaṃ] [adj] [cittaṃ] VP1, no ca [pron] [cittaṃ] VP2.
    m = re.fullmatch(rf"(.+?)( tesaṃ)? {_ADJ_RE}(cittaṃ )?{_VP}, no ca (?:(tassa taṃ|tesaṃ|taṃ) )?({_ADJ_RE}cittaṃ )?{_VP}\.", s)
    if m:
        subj, tes, adj, cit, vp1, pron, cit2, adj2, vp2 = m.groups()
        sh = subject(subj, tes, cit, adj)
        mind2 = ((ADJ[adj2] + " ") if adj2 else "") + MIND + " " if cit2 else ""
        return f"{sh} {vp_hi(vp1)}, पर {PRON[pron]}{mind2}{vp_hi(vp2, flip=True)}।"
    # both: VP1 ceva VP2 ca  /  P1ñceva P2ñca  /  P1ñceva V2 ca
    m = re.fullmatch(rf"(.+?)( tesaṃ)? {_ADJ_RE}(cittaṃ )?(na )?(\S+?)(?:ñceva| ceva) (\S+?)(?:ñca| ca)\.", s)
    if m:
        subj, tes, adj, cit, neg1, p1, p2 = m.groups()
        p1 = p1 + "ṃ" if p1 + "ṃ" in PRED else p1
        p2 = p2 + "ṃ" if p2 + "ṃ" in PRED else p2
        sh = subject(subj, tes, cit, adj)
        h1 = NEG_BHI[p1] if neg1 else PRED[p1][2]
        return f"{sh} {h1} और {PRED[p2][2]}।"
    # neither: na ceva P1 na ca P2
    m = re.fullmatch(rf"(.+?)( tesaṃ)? {_ADJ_RE}(cittaṃ )?na ceva (\S+) na ca (\S+)\.", s)
    if m:
        subj, tes, adj, cit, p1, p2 = m.groups()
        sh = subject(subj, tes, cit, adj)
        return f"{sh} न तो {PRED[p1][0]}, न {PRED[p2][0]}।"
    # abbreviated: <who> tesaṃ…pe….
    m = re.fullmatch(r"(.+?) tesaṃ…pe…\.", s)
    if m:
        return f"{WHO[m.group(1)]}…।"
    raise ValueError(f"no answer formula: {s!r}")


# ---------------------------------------------------------------------------------------------------
# Questions
# ---------------------------------------------------------------------------------------------------
REL = {"yassa": ("जिस व्यक्ति में", "उसमें"), "yaṃ": ("जो", "वह"), "yassa yaṃ": ("जिस व्यक्ति में जो", "उसमें वह")}
COR = {"tassa": "yassa", "taṃ": "yaṃ", "tassa taṃ": "yassa yaṃ"}


def label(lab):
    return (S.LABELS[lab] + " ") if lab else ""


def question(q):
    q = strip_ti(q)
    m = re.fullmatch(
        rf"(\((?:Ka|Kha)\) )?(?:Y|y)(assa|aṃ)( vā pana)?( yaṃ)? {_ADJ_RE}cittaṃ {_VP}"
        rf"(?: no ca (tassa taṃ|tassa|taṃ) cittaṃ {_VP},)? (tassa taṃ|tassa|taṃ) {_ADJ_RE}cittaṃ {_VP}\?", q)
    if m:
        lab, rel1, vp_, yam, adj1, vp1, nc_pron, nc_vp, cor, adj2, vp2 = m.groups()
        rel = "y" + rel1 + (yam or "")
        rel_hi, cor_hi = REL[rel]
        a1 = (ADJ[adj1] + " ") if adj1 else ""
        a2 = (ADJ[adj2] + " ") if adj2 else ""
        mid = f", पर {cor_hi} {MIND} {vp_hi(nc_vp, flip=True)}" if nc_pron else ""
        return (f"{label(lab.strip() if lab else None)}{'और ' if vp_ else ''}{rel_hi} {a1}{MIND} {vp_hi(vp1)}{mid}, "
                f"क्या {cor_hi} {a2}{MIND} {vp_hi(vp2)}?")
    # (12)/(13): (Ka) [na ]P1 [na ]P2?
    m = re.fullmatch(r"\((Ka|Kha)\) (na )?(\S+) (na )?(\S+)\?", q)
    if m and m.group(3) in PRED and m.group(5) in PRED:
        lab = S.LABELS[f"({m.group(1)})"]
        if m.group(2):
            return f"{lab} जो {PRED[m.group(3)][1]}, क्या वह {PRED[m.group(5)][1]}?"
        return f"{lab} जो {PRED[m.group(3)][0]}, क्या वह {PRED[m.group(5)][0]}?"
    # (14)
    m = re.fullmatch(
        r"\((Ka|Kha)\) y(assa|aṃ)( vā pana)?( yaṃ)? cittaṃ (na )?(uppajjamānaṃ|nirujjhamānaṃ) khaṇaṃ khaṇaṃ vītikkantaṃ "
        r"atikkantakālaṃ, (na )?(uppajjamānaṃ|nirujjhamānaṃ) khaṇaṃ khaṇaṃ vītikkantaṃ atikkantakālaṃ "
        r"(tassa taṃ|tassa|taṃ) cittaṃ\?", q)
    if m:
        lab, rel1, vp_, yam, n1, p1, n2, p2, cor = m.groups()
        rel_hi, cor_hi = REL["y" + rel1 + (yam or "")]
        return (f"{S.LABELS['(' + lab + ')']} {'और ' if vp_ else ''}{rel_hi} {MIND} {atikkanta(p1, n1)}, "
                f"क्या {cor_hi} {MIND} {atikkanta(p2, n2)}?")
    return None


def atikkanta(p, neg):
    v = "उत्पन्न" if p == "uppajjamānaṃ" else "समाप्त"
    if neg:
        return f"{v} होते हुए क्षण-क्षण से आगे नहीं निकला है और उसका समय नहीं बीता है"
    return f"{v} होते हुए क्षण-क्षण से आगे निकल चुका है और उसका समय बीत चुका है"


# ---------------------------------------------------------------------------------------------------
# Fixed lines
# ---------------------------------------------------------------------------------------------------
SUTTANTA = ["sarāgaṃ", "vītarāgaṃ", "sadosaṃ", "vītadosaṃ", "samohaṃ", "vītamohaṃ", "saṃkhittaṃ", "vikkhittaṃ",
            "mahaggataṃ", "amahaggataṃ", "sauttaraṃ", "anuttaraṃ", "samāhitaṃ", "asamāhitaṃ", "vimuttaṃ",
            "avimuttaṃ"]
ABHI = ["kusalaṃ", "akusalaṃ", "abyākataṃ", "sukhāya vedanāya sampayuttaṃ"]


def abbr_list(adjs):
    return "… ".join(f"जिस व्यक्ति में {ADJ[a]} मन उत्पन्न होता है" for a in adjs) + "…?"


A14_1 = ("भंग होने के क्षण का मन उत्पन्न होने के क्षण से आगे निकल चुका है, पर भंग होने के क्षण से आगे नहीं निकला है। "
         "अतीत का मन उत्पन्न होने के क्षण से भी आगे निकल चुका है और भंग होने के क्षण से भी आगे निकल चुका है।")
A14_4 = ("भंग होने के क्षण का मन भंग होने के क्षण से आगे नहीं निकला है, पर उत्पन्न होने के क्षण से आगे निकल चुका है। "
         "उत्पन्न होने के क्षण का और भविष्य का मन भंग होने के क्षण से भी आगे नहीं निकला है और उत्पन्न होने के क्षण "
         "से भी आगे नहीं निकला है।")
FIXED = {
    # ^6-8-61, ^6-8-62 (abbreviated question lists)
    "Yassa sarāgaṃ cittaṃ uppajjati…pe… yassa vītarāgaṃ cittaṃ uppajjati… yassa sadosaṃ cittaṃ uppajjati… "
    "yassa vītadosaṃ cittaṃ uppajjati… yassa samohaṃ cittaṃ uppajjati… yassa vītamohaṃ cittaṃ uppajjati … "
    "yassa saṃkhittaṃ cittaṃ uppajjati… yassa vikkhittaṃ cittaṃ uppajjati… yassa mahaggataṃ cittaṃ uppajjati… "
    "yassa amahaggataṃ cittaṃ uppajjati… yassa sauttaraṃ cittaṃ uppajjati… yassa anuttaraṃ cittaṃ uppajjati… "
    "yassa samāhitaṃ cittaṃ uppajjati… yassa asamāhitaṃ cittaṃ uppajjati… yassa vimuttaṃ cittaṃ uppajjati… "
    "yassa avimuttaṃ cittaṃ uppajjati…?": abbr_list(SUTTANTA),
    "Yassa kusalaṃ cittaṃ uppajjati…pe… yassa akusalaṃ cittaṃ uppajjati… yassa abyākataṃ cittaṃ uppajjati… "
    "yassa sukhāya vedanāya sampayuttaṃ cittaṃ uppajjati…?": abbr_list(ABHI),
    "(Etena upāyena yāva saraṇaaraṇā uddharitabbā.)":
        "(इसी तरीके से “संघर्ष वाला और संघर्ष से रहित” तक प्रश्न निकाले जाने चाहिए।)",
    # (14) answers
    "Bhaṅgakkhaṇe cittaṃ uppādakkhaṇaṃ vītakkantaṃ bhaṅgakkhaṇaṃ avītikkantaṃ, atītaṃ cittaṃ uppādakkhaṇañca "
    "vītikkantaṃ bhaṅgakkhaṇañca vītikkantaṃ.": A14_1,   # source slip vītakkantaṃ (^6-8-83)
    "Bhaṅgakkhaṇe cittaṃ uppādakkhaṇaṃ vītikkantaṃ bhaṅgakkhaṇaṃ avītikkantaṃ, atītaṃ cittaṃ uppādakkhaṇañca "
    "vītikkantaṃ bhaṅgakkhaṇañca vītikkantaṃ.": A14_1,
    "Atītaṃ cittaṃ.": "अतीत का मन।",
    "Uppādakkhaṇe anāgataṃ cittaṃ.": "उत्पन्न होने के क्षण का और भविष्य का मन।",
    "Bhaṅgakkhaṇe cittaṃ bhaṅgakkhaṇaṃ avītikkantaṃ no ca uppādakkhaṇaṃ avītikkantaṃ, uppādakkhaṇe anāgatañca "
    "cittaṃ bhaṅgakkhaṇañca avītikkantaṃ uppādakkhaṇañca avītikkantaṃ.": A14_4,
    # ^6-8-82 (heading line inside the segment, source slip)
    "(14) Atikkantakālavāro": "(14) समय बीत चुकने का खंड",
    # ^6-8-113 note
    "(Yassa cittake sakabhāvena niddiṭṭhe, yaṃ cittake ca yassa yaṃ cittake ca ekattena niddiṭṭhe.)":
        "(“जिस व्यक्ति में मन” वाले भाग की व्याख्या अपने ही ढंग से की गई है, और “जो मन” वाले भाग की तथा "
        "“जिस व्यक्ति में जो मन” वाले भाग की व्याख्या एक ही रूप में की गई है।)",
    # ^6-8-115
    "Yassa vā pana…pe…? Āmantā …pe….": "और जिस व्यक्ति में…? हाँ…।",
    # ^6-8-116
    "Yassa akusalaṃ cittaṃ uppajjati na nirujjhati…pe…. Yassa abyākataṃ cittaṃ uppajjati na nirujjhati…pe….":
        "जिस व्यक्ति में हानिकर मन उत्पन्न होता है और समाप्त नहीं होता…। "
        "जिस व्यक्ति में नैतिक रूप से अनिर्धारित मन उत्पन्न होता है और समाप्त नहीं होता…।",
    "(Mūlayamakaṃ cittayamakaṃ dhammayamakanti tīṇi yamakāni yāva saraṇaaraṇā gacchanti.)":
        "(मूलों पर प्रश्नों के जोड़े, मन पर प्रश्नों के जोड़े और परिघटनाओं पर प्रश्नों के जोड़े, ये तीन भाग "
        "“संघर्ष वाला और संघर्ष से रहित” तक जाते हैं।)",
    "Cittayamakaṃ niṭṭhitaṃ.": S.CHAPTER_END.format(title=S.CHAPTER_TITLES["Cittayamakaṃ"]),
}


def text_line(line):
    if line in FIXED:
        return FIXED[line]
    out = []
    for s in S._split_sentences(line):
        if s.startswith(("(Ka)", "(Kha)", "Yassa ")) and "?" in s:
            qpart, _, rest = s.partition("?")
            q = question(qpart + "?")
            if q is None:
                raise ValueError(f"no question formula: {s!r}")
            out.append(q)
            rest = rest.strip()
            if rest:
                out.append(answer_sentence(rest))
        else:
            out.append(answer_sentence(s))
    return " ".join(out)


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
        hashes, text = line.split(" ", 1)
        return f"{hashes} {HEADINGS[text]}{bid}"
    return text_line(line) + bid


def main():
    pali = SRC.read_text(encoding="utf-8")
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
    text = "\n".join(out) + "\n"
    if "--dry" in sys.argv:
        sys.stdout.write(text)
        return
    OUT.write_text(text, encoding="utf-8", newline="\n")
    print("written", OUT)


if __name__ == "__main__":
    main()
