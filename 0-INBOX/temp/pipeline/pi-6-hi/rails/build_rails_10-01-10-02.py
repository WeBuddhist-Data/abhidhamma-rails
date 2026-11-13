"""pi-6 Indriyayamaka 10-01 / 10-02, Pāli -> Hindi plain RAILS.

Imports build_rails_sample.py read-only (formulas, headings, verbs, places). Writes only
AI_translation\\hindi\\pi-6-hindi-plain-rails_split_chapters\\10-01-indriyayamaka.md and 10-02-indriyayamaka.md.
Every Pāli line must match a formula; an unknown line raises ValueError.
usage: python -I -X utf8 build_rails_10-01-10-02.py
"""
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\rails")
import build_rails_sample as S  # noqa: E402

FILES = ["10-01-indriyayamaka.md", "10-02-indriyayamaka.md"]

# ---------------------------------------------------------------------------------------------
# Words: faculties and bare words (termbase)
# ---------------------------------------------------------------------------------------------
Q_ANN = "“जो अब तक नहीं जाना उसे मैं जान लूँगा”"
FACULTY = {
    "cakkhundriyaṃ": "आँख की क्षमता", "sotindriyaṃ": "कान की क्षमता", "ghānindriyaṃ": "नाक की क्षमता",
    "jivhindriyaṃ": "जीभ की क्षमता", "kāyindriyaṃ": "शरीर की क्षमता", "manindriyaṃ": "मन की क्षमता",
    "itthindriyaṃ": "स्त्रीत्व की क्षमता", "purisindriyaṃ": "पुरुषत्व की क्षमता", "jīvitindriyaṃ": "जीवन-क्षमता",
    "sukhindriyaṃ": "सुख की क्षमता", "dukkhindriyaṃ": "दुःख की क्षमता", "somanassindriyaṃ": "प्रसन्नता की क्षमता",
    "domanassindriyaṃ": "उदासी की क्षमता", "upekkhindriyaṃ": "समभाव की क्षमता", "saddhindriyaṃ": "श्रद्धा की क्षमता",
    "vīriyindriyaṃ": "उत्साह की क्षमता", "satindriyaṃ": "सजगता की क्षमता", "samādhindriyaṃ": "एकाग्रता की क्षमता",
    "paññindriyaṃ": "प्रज्ञा की क्षमता", "anaññātaññassāmītindriyaṃ": Q_ANN + " की क्षमता",
    "aññindriyaṃ": "पूर्ण ज्ञान की क्षमता", "aññātāvindriyaṃ": "पूर्ण ज्ञान पा चुके की क्षमता",
}
# key (nominative) -> (direct, oblique, number)
WORDS = {k: (v, v, "sg") for k, v in FACULTY.items()}
WORDS.update({
    "cakkhu": ("आँख", "आँख", "sg"), "sotaṃ": ("कान", "कान", "sg"), "ghānaṃ": ("नाक", "नाक", "sg"),
    "jivhā": ("जीभ", "जीभ", "sg"), "kāyo": ("शरीर", "शरीर", "sg"), "mano": ("मन", "मन", "sg"),
    "itthī": ("स्त्री", "स्त्री", "sg"), "puriso": ("पुरुष", "पुरुष", "sg"), "jīvitaṃ": ("जीवन", "जीवन", "sg"),
    "sukhaṃ": ("सुख", "सुख", "sg"), "dukkhaṃ": ("दुःख", "दुःख", "sg"), "somanassaṃ": ("प्रसन्नता", "प्रसन्नता", "sg"),
    "domanassaṃ": ("उदासी", "उदासी", "sg"), "upekkhā": ("समभाव", "समभाव", "sg"), "saddhā": ("श्रद्धा", "श्रद्धा", "sg"),
    "vīriyaṃ": ("उत्साह", "उत्साह", "sg"), "sati": ("सजगता", "सजगता", "sg"), "samādhi": ("एकाग्रता", "एकाग्रता", "sg"),
    "paññā": ("प्रज्ञा", "प्रज्ञा", "sg"), "anaññātaññassāmīti": (Q_ANN, Q_ANN, "sg"),
    "anaññātaññāssāmīti": (Q_ANN, Q_ANN, "sg"),    # spelling variant in 10-01 line 98
    "aññaṃ": ("पूर्ण ज्ञान", "पूर्ण ज्ञान", "sg"),
    "aññātāvī": ("पूर्ण ज्ञान पा चुका व्यक्ति", "पूर्ण ज्ञान पा चुके व्यक्ति", "sg"),
    "indriyaṃ": ("क्षमता", "क्षमता", "sg"), "indriyā": ("क्षमताएँ", "क्षमताओं", "pl"),
})
# accusative forms (also before -ñca / ca) -> key
ACC = {
    "cakkhuṃ": "cakkhu", "sotaṃ": "sotaṃ", "ghānaṃ": "ghānaṃ", "jivhaṃ": "jivhā", "kāyaṃ": "kāyo", "manaṃ": "mano",
    "itthiṃ": "itthī", "purisaṃ": "puriso", "jīvitaṃ": "jīvitaṃ", "sukhaṃ": "sukhaṃ", "dukkhaṃ": "dukkhaṃ",
    "somanassaṃ": "somanassaṃ", "domanassaṃ": "domanassaṃ", "upekkhaṃ": "upekkhā", "saddhaṃ": "saddhā",
    "vīriyaṃ": "vīriyaṃ", "satiṃ": "sati", "samādhiṃ": "samādhi", "paññaṃ": "paññā",
    "anaññātaññassāmītiṃ": "anaññātaññassāmīti", "aññaṃ": "aññaṃ", "aññātāviṃ": "aññātāvī", "indriye": "indriyā",
    "indriyaṃ": "indriyaṃ",
}
ACC.update({k: k for k in FACULTY})
COP = {"sg": "है", "pl": "हैं"}
PRON = {"sg": "वह", "pl": "वे"}
SPECIAL_SUBJ = {
    "dibbacakkhu paññācakkhu": ("दिव्य आँख और प्रज्ञा की आँख", "pl"),
    "dibbasotaṃ taṇhāsotaṃ": ("दिव्य कान और तृष्णा की धारा", "pl"),
}


def low(w):
    return w[0].lower() + w[1:]


def strip_ti(word):
    """Remove the quotative -ti (cakkhūti, sotanti, satīti, indriyanti, uppajjatīti …)."""
    w = low(word)
    vocab = set(WORDS) | {"uppajjati"}
    if w in vocab:
        return w
    if w in ACC:          # 10-01 ^6-10-2 "(Kha) cakkhundriyaṃ cakkhuṃ?" (accusative form in the source)
        return ACC[w]
    for cand in (w[:-2], w[:-3] + "ṃ", w[:-3] + "i", w[:-3] + "u", w[:-3] + "a", w[:-3] + "ā"):
        if cand in vocab:
            return cand
    raise ValueError(f"unknown word with -ti: {word}")


def acc_key(w):
    """'Cakkhuñca' / 'Kāyañca' / 'indriye' (before ' ca') / 'Cakkhuṃ' -> key."""
    w = low(w)
    if w.endswith("ñca"):
        w = w[:-3] + "ṃ"
    return ACC[w]


def word(w):
    return WORDS[low(w)]


# ---------------------------------------------------------------------------------------------
# Paṇṇattivāra
# ---------------------------------------------------------------------------------------------
def pannatti_question(s):
    """'(Ka) cakkhu cakkhundriyaṃ?' / '(Kha) na indriyā na sotindriyanti?' / 'Sotaṃ sotindriyaṃ?' (no label)."""
    m = re.fullmatch(r"(?:\((Ka|Kha)\) )?(na |Na )?(\S+) (na )?(\S+)\?", s)
    if not m or bool(m.group(2)) != bool(m.group(4)):
        return None
    a = low(m.group(3))
    if a not in WORDS:
        return None
    b = strip_ti(m.group(5))
    if b not in WORDS:
        return None
    lab = (S.LABELS[f"({m.group(1)})"] + " ") if m.group(1) else ""
    (ad, _, an), (bd, _, bn) = WORDS[a], WORDS[b]
    n2 = "pl" if "pl" in (an, bn) else "sg"
    if m.group(2):
        return f"{lab}जो {ad} नहीं {COP[an]}, क्या {PRON[an]} {bd} नहीं {COP[n2]}?"
    return f"{lab}क्या {ad}, {bd} {COP[n2]}?"


def subject(s):
    """Subject of the A-B-C answers -> (Hindi, number or None = take the predicate's number)."""
    sl = low(s)
    if sl in SPECIAL_SUBJ:
        return SPECIAL_SUBJ[sl]
    m = re.fullmatch(r"(\S+) ṭhapetvā (avaseso|avasesā)( indriyā)?", s)
    if m:
        x = WORDS[acc_key(m.group(1))][1]
        if m.group(3):
            return f"{x} को छोड़कर शेष क्षमताएँ", "pl"
        return f"{x} को छोड़कर शेष", None
    if sl in WORDS:
        return WORDS[sl][0], WORDS[sl][2]
    raise ValueError(f"subject: {s}")


def pannatti_sentence(s):
    m = re.fullmatch(r"(.+?) (\S+), na (\S+)\.", s)                       # A B, na C.
    if not m:
        m = re.fullmatch(r"(.+? ṭhapetvā avaseso) (\S+) na (\S+)\.", s)  # same without the comma (^6-10-100)
    if m and low(m.group(2)) in WORDS and low(m.group(3)) in WORDS:
        a, n = subject(m.group(1))
        n = n or word(m.group(2))[2]
        return f"{a}, {word(m.group(2))[0]} {COP[n]}, पर {word(m.group(3))[0]} नहीं {COP[n]}।"
    m = re.fullmatch(r"(.+?) na (\S+), (\S+)\.", s)                       # A na C, B.
    if m and low(m.group(2)) in WORDS and low(m.group(3)) in WORDS:
        a, n = subject(m.group(1))
        n = n or word(m.group(3))[2]
        return f"{a}, {word(m.group(2))[0]} नहीं {COP[n]}, पर {word(m.group(3))[0]} {COP[n]}।"
    m = re.fullmatch(r"(\S+) (\S+?)(?:ñceva| ceva) (\S+?)(?:ñca| ca)\.", s)   # C B ceva C ca.
    if m:
        c = WORDS[low(m.group(1))]
        braw = m.group(2)
        b = WORDS.get(low(braw)) or WORDS[acc_key(braw + "ñca")]
        if WORDS[low(m.group(1))] != WORDS[acc_key(m.group(3) + "ñca")]:
            raise ValueError(f"C B ceva C: {s}")
        n = "pl" if "pl" in (b[2], c[2]) else "sg"
        return f"{c[0]}, {b[0]} भी {COP[n]} और {c[0]} भी।"
    m = re.fullmatch(r"(\S+?)(ñca| ca) (\S+?)(ñca| ca) ṭhapetvā (avasesā|avaseso) na ceva (\S+) na ca (\S+)\.", s)
    if m:
        b = WORDS[acc_key(m.group(1) + ("ñca" if m.group(2) == "ñca" else ""))]
        c = WORDS[acc_key(m.group(3) + ("ñca" if m.group(4) == "ñca" else ""))]
        cop = "हैं" if m.group(5) == "avasesā" else "है"
        return f"{b[1]} और {c[1]} को छोड़कर शेष न तो {word(m.group(6))[0]} {cop}, न {word(m.group(7))[0]}।"
    m = re.fullmatch(r"Avasesā indriyā na (\S+)\.", s)
    if m:
        return f"शेष क्षमताएँ, {word(m.group(1))[0]} नहीं हैं।"
    m = re.fullmatch(r"(?:Yaṃ|Yo|Yā) (\S+) indriyaṃ (?:taṃ|so|sā) (\S+?)(?:ñceva| ceva) indriyañca\.", s)
    if m:
        x = word(m.group(1))[0]
        if (WORDS.get(low(m.group(2))) or WORDS[acc_key(m.group(2) + "ñca")])[0] != x:
            raise ValueError(f"Yaṃ X indriyaṃ taṃ X: {s}")
        return f"जो {x}, क्षमता है, वह {x} भी है और क्षमता भी।"
    m = re.fullmatch(r"(?:Avasesaṃ|Avaseso|Avasesā) (\S+) na (?:indriyaṃ|indriyā)\.", s)
    if m:
        return f"शेष {word(m.group(1))[0]}, क्षमता नहीं है।"
    return None


FIXED_SENTENCES = {
    "Kāyindriyaṃ ṭhapetvā avaseso kāyo [avasesā kāyo (sī. syā. ka.)], na kāyindriyaṃ.":
        "शरीर की क्षमता को छोड़कर शेष, शरीर है [वर्तनी-भेद (Sī., Syā., Ka.): avasesā kāyo], पर शरीर की क्षमता नहीं है।",
}
FIXED_LINES = {
    "Bāvīsatindriyāni – cakkhundriyaṃ, sotindriyaṃ, ghānindriyaṃ, jivhindriyaṃ, kāyindriyaṃ, manindriyaṃ, "
    "itthindriyaṃ, purisindriyaṃ, jīvitindriyaṃ, sukhindriyaṃ, dukkhindriyaṃ, somanassindriyaṃ, domanassindriyaṃ, "
    "upekkhindriyaṃ, saddhindriyaṃ, vīriyindriyaṃ [viriyindiyaṃ (sī. syā.)], satindriyaṃ, samādhindriyaṃ, "
    "paññindriyaṃ, anaññātaññassāmītindriyaṃ, aññindriyaṃ, aññātāvindriyaṃ.":
        "बाईस क्षमताएँ – आँख की क्षमता, कान की क्षमता, नाक की क्षमता, जीभ की क्षमता, शरीर की क्षमता, मन की क्षमता, "
        "स्त्रीत्व की क्षमता, पुरुषत्व की क्षमता, जीवन-क्षमता, सुख की क्षमता, दुःख की क्षमता, प्रसन्नता की क्षमता, "
        "उदासी की क्षमता, समभाव की क्षमता, श्रद्धा की क्षमता, उत्साह की क्षमता [वर्तनी-भेद (Sī., Syā.): viriyindiyaṃ], "
        "सजगता की क्षमता, एकाग्रता की क्षमता, प्रज्ञा की क्षमता, " + Q_ANN + " की क्षमता, पूर्ण ज्ञान की क्षमता, "
        "पूर्ण ज्ञान पा चुके की क्षमता।",
}

# ---------------------------------------------------------------------------------------------
# Pavattivāra
# ---------------------------------------------------------------------------------------------
G = "f"   # every faculty is feminine (क्षमता)
FAC_FORMS = {}
for k in FACULTY:
    FAC_FORMS[k] = k
    FAC_FORMS[k[:-1] + "ñca"] = k            # cakkhundriyañca
REL_HI = {"yassa": ("जिस व्यक्ति में", "उसमें"), "yassa vā pana": ("और जिस व्यक्ति में", "उसमें"),
          "yattha": ("जिस स्थान पर", "वहाँ"), "yattha vā pana": ("और जिस स्थान पर", "वहाँ")}
assert REL_HI["yassa"] == S.REL_FRAMES[("yassa", "tassa")] and REL_HI["yattha"] == S.REL_FRAMES[("yattha", "tattha")]


def fac_chain(s):
    """'itthindriyaṃ…pe… purisindriyaṃ' -> «स्त्रीत्व की क्षमता… पुरुषत्व की क्षमता»."""
    parts = s.split("…pe… ")
    return "… ".join(FACULTY[p] for p in parts)


def vhi(tok, flip=False):
    return S.verb_hi(tok, G, flip)


def pavatti_question(s):
    m = re.fullmatch(r"(?:\((Ka|Kha)\) )?(yassa vā pana|yassa|yattha vā pana|yattha|Yattha vā pana|Yattha) "
                     r"(\S+) (uppajjati) (tassa|tattha) (.+) (uppajjatīti)\?", s)
    if not m:
        return None
    lab, rel, k1, v1, cor, k2, v2 = m.groups()
    rel_hi, cor_hi = REL_HI[low(rel)]
    lab_hi = (S.LABELS[f"({lab})"] + " ") if lab else ""
    return (f"{lab_hi}{rel_hi} {FACULTY[k1]} {vhi(v1)}, क्या {cor_hi} {fac_chain(k2)} "
            f"{vhi(strip_ti(v2))}?")


# being chunks
ADJ = {  # genitive pl. modifier -> (masc., fem.)
    "sacakkhukānaṃ": ("आँख वाले", "आँख वाली"), "acakkhukānaṃ": ("आँख से रहित", "आँख से रहित"),
    "sasotakānaṃ": ("कान वाले", "कान वाली"), "asotakānaṃ": ("कान से रहित", "कान से रहित"),
    "saghānakānaṃ": ("नाक वाले", "नाक वाली"), "aghānakānaṃ": ("नाक से रहित", "नाक से रहित"),
    "sahetukānaṃ": ("मूल वाले", "मूल वाली"), "ahetukānaṃ": ("मूल से रहित", "मूल से रहित"),
    "ñāṇasampayuttānaṃ": ("ज्ञान से जुड़े", "ज्ञान से जुड़ी"), "ñāṇavippayuttānaṃ": ("ज्ञान से अलग", "ज्ञान से अलग"),
    "sacittakānaṃ": ("मन वाले", "मन वाली"), "acittakānaṃ": ("मन से रहित", "मन से रहित"),
    "na itthīnaṃ": ("स्त्रियों से भिन्न", "स्त्रियों से भिन्न"), "na purisānaṃ": ("पुरुषों से भिन्न", "पुरुषों से भिन्न"),
}
ADV = {"somanassena": "प्रसन्नता के साथ", "vinā somanassena": "प्रसन्नता के बिना",
       "upekkhāya": "समभाव के साथ", "vinā upekkhāya": "समभाव के बिना"}
MOM_MEMBER = {"somanassa": "प्रसन्नता", "upekkhā": "समभाव", "saddhā": "श्रद्धा", "ñāṇa": "ज्ञान"}
PAVATTE = "जीवन के दौरान"


def moment(tok):
    """'somanassasampayuttasaddhāvippayuttacittassa' -> «प्रसन्नता से जुड़े और श्रद्धा से अलग मन के»."""
    assert tok.endswith("cittassa"), tok
    body = tok[: -len("cittassa")]
    mods = []
    while body:
        m = re.match(r"(somanassa|upekkhā|saddhā|ñāṇa)(sampayutta|vippayutta)", body)
        if not m:
            raise ValueError(f"moment: {tok}")
        mods.append(f"{MOM_MEMBER[m.group(1)]} से {'जुड़े' if m.group(2) == 'sampayutta' else 'अलग'}")
        body = body[m.end():]
    return (" और ".join(mods) + " " if mods else "") + "मन के उत्पन्न होने के क्षण में"


def who(s):
    """Being chain before tesaṃ / tāsaṃ -> Hindi; chunks end with «में», last joined with « और »."""
    toks = low(s).split(" ")
    chunks, adj, adv, fem, head, i = [], [], [], False, None, 0
    while i < len(toks):
        w = toks[i]
        two = " ".join(toks[i:i + 2])
        if two in ADJ:
            adj.append(two); i += 2; continue
        if two in ADV:
            adv.append(ADV[two]); i += 2; continue
        if w in ADJ:
            adj.append(w)
        elif w in ADV:
            adv.append(ADV[w])
        elif w == "itthīnaṃ":
            head = "itthī"
        elif w == "purisānaṃ":
            head = "purisa"
        elif w in ("upapajjantānaṃ", "upapajjantīnaṃ"):
            fem = (w == "upapajjantīnaṃ")
            if fem and head != "itthī":
                raise ValueError(f"who: upapajjantīnaṃ without itthīnaṃ: {s}")
            mods = [ADJ[a][1 if fem else 0] for a in adj] + adv
            pre = (" और ".join(mods) + " ") if mods else ""
            tail = {"itthī": "जन्म लेने वाली स्त्रियों में", "purisa": "जन्म लेने वाले पुरुषों में",
                    None: "जन्म लेने वालों में"}[head]
            chunks.append(pre + tail)
            adj, adv, head = [], [], None
        elif w == "pavatte" and i + 2 < len(toks) and toks[i + 2] == "uppādakkhaṇe":
            chunks.append(f"{PAVATTE} {moment(toks[i + 1])}")
            i += 3; continue
        else:
            raise ValueError(f"who: unknown token {w!r} in {s!r}")
        i += 1
    if adj or adv or head:
        raise ValueError(f"who: dangling tokens in {s!r}")
    if len(chunks) == 1:
        return chunks[0]
    return S.JOIN.join(chunks[:-1]) + S.JOIN_LAST + chunks[-1]


def pavatti_sentence(s):
    m = re.fullmatch(r"(.+?) (tesaṃ|tāsaṃ|tattha) (\S+) (uppajjati), no ca (?:tesaṃ|tāsaṃ|tattha) (\S+) (uppajjati)\.", s)
    if m:
        wh, t, k1, v1, k2, v2 = m.groups()
        k1h, k2h = FACULTY[k1], FACULTY[k2]
        if t == "tattha":
            return S.BUT_PLACE.format(place=S.place(wh), k1=k1h, v1=vhi(v1), k2=k2h, v2=vhi(v2, flip=True))
        return S.BUT_BEINGS.format(who=who(wh), k1=k1h, v1=vhi(v1), k2=k2h, v2=vhi(v2, flip=True))
    m = re.fullmatch(r"(.+?) (tesaṃ|tāsaṃ|tattha) (\S+) (uppajjati) (\S+) (uppajjati)\.", s)
    if m and m.group(3) in FAC_FORMS and m.group(3).endswith("ñca") and m.group(5).endswith("ñca"):
        wh, t, k1, v1, k2, v2 = m.groups()
        k1h, k2h = FACULTY[FAC_FORMS[k1]], FACULTY[FAC_FORMS[k2]]
        if t == "tattha":
            return S.BOTH_PLACE.format(place=S.place(wh), k1=k1h, v1=vhi(v1), k2=k2h, v2=vhi(v2))
        return S.BOTH_BEINGS.format(who=who(wh), k1=k1h, v1=vhi(v1), k2=k2h, v2=vhi(v2))
    return None


# ---------------------------------------------------------------------------------------------
# driver
# ---------------------------------------------------------------------------------------------
LABEL_RE = re.compile(r" \((\S+?)mūlakaṃ\)$")
HEADINGS = dict(S.HEADINGS)
HEADINGS.update({"Pavattivāro": "प्रक्रिया का खंड"})
SPLIT = re.compile(r"(?<=[.?]) (?=[A-ZĀĪŪṬḌṆÑṄ(])")


def sentence(s):
    if s in FIXED_SENTENCES:
        return FIXED_SENTENCES[s]
    if s in S.CLOSINGS:
        return S.CLOSINGS[s]
    # abbreviation tails
    # an abbreviated question list ending "…pe…." ends «…?» (formulas §0); spacing differs in the source only
    for tail, hi in (("?…Pe….", "…?"), ("? …Pe….", "…?")):
        if s.endswith(tail):
            return sentence(s[: -len(tail)] + "?")[:-1] + hi
    m = re.fullmatch(r"(.+?) ?…pe…\.", s)
    if m:
        return sentence(m.group(1) + ("" if m.group(1).endswith(".") else "."))[:-1] + "…।"
    if " …Pe… " in s:          # '(Kha) na indriyā na cakkhundriyaṃ? …Pe… na indriyā na aññātāvindriyaṃ?'
        a, b = s.split(" …Pe… ")
        return sentence(a) + " … " + sentence(b)
    for fn in (pannatti_question, pavatti_question, pannatti_sentence, pavatti_sentence):
        r = fn(s)
        if r:
            return r
    raise ValueError(f"no formula for: {s}")


def text_line(line):
    if line in FIXED_LINES:
        return FIXED_LINES[line]
    label = ""
    m = LABEL_RE.search(line)
    if m:
        key = m.group(1)[0].lower() + m.group(1)[1:] + "ṃ"
        label = f" ({FACULTY[key]} पर आधारित)"
        line = line[: m.start()]
    return " ".join(sentence(s) for s in SPLIT.split(line)) + label


def translate_line(line):
    bid = ""
    m = S.ID_RE.search(line)
    if m:
        bid = " " + m.group(1)
        line = line[: m.start()]
    if line.startswith("#"):
        hashes, text = line.split(" ", 1)
        if text not in HEADINGS:
            raise ValueError(f"unknown heading: {text}")
        return f"{hashes} {HEADINGS[text]}{bid}"
    return text_line(line.strip()) + bid


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


def main():
    for f in FILES:
        pali = (S.PALI_DIR / f).read_text(encoding="utf-8")
        (S.HI_DIR / f).write_text(translate_text(pali), encoding="utf-8", newline="\n")
        print("built", f)


if __name__ == "__main__":
    main()
