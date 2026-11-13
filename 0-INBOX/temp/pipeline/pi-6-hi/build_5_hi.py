r"""pi-6 Yamaka, Hindi plain zero-shot: Saccayamaka (5-01, 5-02, 5-03).

usage: python -I -X utf8 build_5_hi.py
Every line is composed from fixed frames (imported from build_sample_hi) and the tables below;
an unknown line raises an error. The 'who/when' qualifier phrases of the answers are built by a
small chunk translator (WHO_TOKENS + who()), shared with build_8_hi.py.
"""
import pathlib
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi")
import build_sample_hi as S  # noqa: E402

PALI_DIR, HI_DIR = S.PALI_DIR, S.HI_DIR

# ---------------------------------------------------------------- truths (pi-2 Hindi ch. 4 headings)
SACCA = {
    "dukkhasaccaṃ": "दुःख का सत्य",
    "samudayasaccaṃ": "उत्पत्ति का सत्य",
    "nirodhasaccaṃ": "अंत का सत्य",
    "maggasaccaṃ": "मार्ग का सत्य",
}
SACCA_OBL = {k: v.replace(" का सत्य", " के सत्य") for k, v in SACCA.items()}
# bare words of the word-checking pairs: Hindi, plural?
BARE = {
    "dukkhaṃ": ("दुःख", False), "samudayo": ("उत्पत्ति", False), "nirodho": ("अंत", False),
    "maggo": ("मार्ग", False), "saccaṃ": ("सत्य", False), "saccā": ("सत्य", True),
}


def noun(w):
    """Any case form of a truth word -> (Hindi, Hindi oblique, plural?)."""
    w = w[0].lower() + w[1:]
    w = re.sub(r"(ñceva|ñca)$", "ṃ", w)
    stem = re.sub(r"(ṃ|o|ā)$", "", w)
    for k in SACCA:
        if k[:-1] == stem:
            return SACCA[k], SACCA_OBL[k], False
    m = {"dukkha": "दुःख", "samuday": "उत्पत्ति", "samudaya": "उत्पत्ति", "nirodh": "अंत",
         "nirodha": "अंत", "magg": "मार्ग", "magga": "मार्ग", "sacc": "सत्य", "sacca": "सत्य"}
    if stem in m:
        return m[stem], m[stem], w.endswith("ā")
    raise KeyError(w)


# ---------------------------------------------------------------- headings and fixed lines
HEADINGS = dict(S.HEADINGS)
HEADINGS.update({
    "Paṇṇattivāra": "शब्दावली का खंड",
    "Suddhasaccavāro": "केवल सत्यों का खंड",
    "Suddhasaccamūlacakkavāro": "केवल सत्यों पर आधारित चक्र का खंड",
    "Pariññāvāro": "पूरी तरह समझने का खंड",
    "Paccuppannavāro": "वर्तमान का खंड",
    "Atītavāro": "अतीत का खंड",
    "Anāgatavāro": "भविष्य का खंड",
    "Paccuppannātītavāro": "वर्तमान और अतीत का खंड",
    "Paccuppannānāgatavāro": "वर्तमान और भविष्य का खंड",
    "Atītānāgatavāro": "अतीत और भविष्य का खंड",
})

NO = "नहीं।"                          # No.
NATTHI = "ऐसा कोई नहीं है।"           # Natthi.
SHORT = dict(S.SHORT_ANSWERS)
SHORT.update({"No.": NO, "Natthi.": NATTHI})
ANSWER_WORDS = {"Āmantā": "हाँ"}        # Āmantā without its period (before …pe…)

# names of the sub-sections used in the editorial notes
YASSAKA = "“जिस व्यक्ति में” वाला खंड"
YATTHAKA = "“जिस स्थान पर” वाला खंड"
YASSAYATTHAKA = "“जिस व्यक्ति में जिस स्थान पर” वाला खंड"


def obl(s):
    return s.replace("वाला खंड", "वाले खंड")


def var(label, sigla, pali, note=None):
    return f"[{label} ({sigla}): {pali}" + (f"; {note}" if note else "") + "]"


# variant brackets: Pāli bracket -> (Hindi bracket, Hindi anchor after which it goes, n-th occurrence)
VARIANTS = {
    "[avasesaṃ dukkhasaccaṃ dukkhasaccaṃ (syā.) evamuparipi]":
        (var(S.VAR_READ, "Syā.", "avasesaṃ dukkhasaccaṃ dukkhasaccaṃ", "आगे भी इसी तरह"), "शेष दुःख का सत्य", 1),
    "[avasesaṃ dukkhasaccaṃ na dukkhaṃ (sī. syā. ka.) evaṃ avasesesu tīsu saccesu]":
        (var(S.VAR_READ, "Sī., Syā., Ka.", "avasesaṃ dukkhasaccaṃ na dukkhaṃ", "बाकी तीन सत्यों में भी इसी तरह"),
         "दुःख नहीं है", 1),
    "[avasesā saccā saccā (syā.)]":
        (var(S.VAR_READ, "Syā.", "avasesā saccā saccā"), "शेष सत्य", 1),
    "[taṇhāvippayuttamaggavippayuttacittassa (sī.) evaṃ puggalokāsepi nirodhavārepi]":
        (var(S.VAR_READ, "Sī.", "taṇhāvippayuttamaggavippayuttacittassa",
             "व्यक्ति और स्थान वाले खंड में और समाप्त होने के खंड में भी इसी तरह"), "तृष्णा से अलग मन", 1),
    "[uppatticittassa (syā.)]":
        (var(S.VAR_SPELL, "Syā.", "uppatticittassa"), "जन्म के मन", 1),
    "[paṭilabhissanti tassa cittassa uppādakkhaṇe ye (sī. syā.) puggalokāsavārepi]":
        (var(S.VAR_READ, "Sī., Syā.", "paṭilabhissanti tassa cittassa uppādakkhaṇe ye",
             "व्यक्ति और स्थान वाले खंड में भी"), "सर्वोच्च मार्ग प्राप्त करेंगे", 1),
    "[paṭilabhissanti tassa cittassa uppādakkhaṇe (sī. syā.) uppādavāre pana pāṭhantaraṃ natthi]":
        (var(S.VAR_READ, "Sī., Syā.", "paṭilabhissanti tassa cittassa uppādakkhaṇe",
             "पर उत्पन्न होने के खंड में पाठभेद नहीं है"), "सर्वोच्च मार्ग प्राप्त करेंगे", 1),
    "[vattamāne, nirodhasamāpannānaṃ asaññasattānaṃ (sī. syā.)]":
        (var(S.VAR_READ, "Sī., Syā.", "vattamāne, nirodhasamāpannānaṃ asaññasattānaṃ"),
         "तृष्णा से अलग मन के चलते समय", 1),
    "[apāyā asaññasattā (syā.)]":
        (var(S.VAR_READ, "Syā.", "apāyā asaññasattā"), "पहचान-रहित प्राणियों के लोक से", 1),
    "[apāyaṃ asaññasattaṃ (syā.)]":
        (var(S.VAR_READ, "Syā.", "apāyaṃ asaññasattaṃ"), "पहचान-रहित प्राणियों के लोक में", 1),
}

# ---------------------------------------------------------------- who / when (answer qualifiers)
# kinds: P person group, S 'sabbesaṃ' alone, L place, T mid 'tesaṃ', TP mid 'tesaṃ <beings>',
# R relative clause, TM 'tassa cittassa <moment>', M moment, PV 'pavatte', V '… vattamāne'
CATUPANCA = "चार समूहों वाले और पाँच समूहों वाले अस्तित्व"
REBORN = "जन्म लेने वालों में"           # upapajjantānaṃ (terms)
DYING = "मरने वालों में"                  # cavantānaṃ (terms)
ABHI = "सत्यों का बोध पा चुके"            # abhisametāvī
ANABHI = "सत्यों का बोध न पाए"            # anabhisametāvī
OTHERS = "बाकी"                     # itaresaṃ + beings
NIRODHASAMAPANNA = "समाप्ति की ध्यान-अवस्था में लीन लोगों में"   # pi-5 nirodhasamāpatti + pi-2 samāpanna
ASANNA_FROM = "पहचान-रहित प्राणियों के लोक से " + DYING        # asaññasattā cavantānaṃ

# genitives before uppādakkhaṇe / bhaṅgakkhaṇe
GEN = {
    "cittassa": "मन", "taṇhāya": "तृष्णा", "maggassa": "मार्ग", "aggamaggassa": "सर्वोच्च मार्ग",
    "phalassa": "फल", "aggaphalassa": "सर्वोच्च फल",
    "maggassa ca phalassa ca": "मार्ग और फल", "aggamaggassa ca phalassa ca": "सर्वोच्च मार्ग और फल",
    "taṇhāvippayuttacittassa": "तृष्णा से अलग मन", "maggavippayuttacittassa": "मार्ग से अलग मन",
    "taṇhāvippayuttamaggavippayuttacittassa": "तृष्णा से अलग और मार्ग से अलग मन",
    "maggavippayuttataṇhāvippayuttacittassa": "मार्ग से अलग और तृष्णा से अलग मन",
    "upapatticittassa": "जन्म के मन", "pacchimacittassa": "अंतिम मन",
    "sarāgapacchimacittassa": "राग-युक्त अंतिम मन", "sarāgacittassa": "राग-युक्त मन",
    "pacchimakusalacittassa": "अंतिम हितकर मन", "kusalacittassa": "हितकर मन",
}
MOMENT = {"uppādakkhaṇe": "{G} के उत्पन्न होने के क्षण में", "bhaṅgakkhaṇe": "{G} के भंग होने के क्षण में"}
R_YASSA = "जो इस मन के ठीक बाद सर्वोच्च मार्ग प्राप्त करेंगे"   # yassa cittassa anantarā aggamaggaṃ paṭilabhissanti

WHO_TOKENS = {
    "sabbesaṃ upapajjantānaṃ": ("P", "सभी " + REBORN),
    "sabbesaṃ cavantānaṃ": ("P", "सभी " + DYING),
    "sabbesaṃ": ("S", "सभी में"),
    "abhisametāvīnaṃ upapajjantānaṃ": ("P", ABHI + " " + REBORN),
    "abhisametāvīnaṃ cavantānaṃ": ("P", ABHI + " " + DYING),
    "abhisametāvīnaṃ": ("P", ABHI + " लोगों में"),
    "anabhisametāvīnaṃ upapajjantānaṃ": ("P", ANABHI + " " + REBORN),
    "anabhisametāvīnaṃ cavantānaṃ": ("P", ANABHI + " " + DYING),
    "anabhisametāvīnaṃ": ("P", ANABHI + " लोगों में"),
    "itaresaṃ upapajjantānaṃ": ("P", OTHERS + " " + REBORN),
    "itaresaṃ cavantānaṃ": ("P", OTHERS + " " + DYING),
    "itaresaṃ catuvokārānaṃ pañcavokārānaṃ": ("P", OTHERS + " " + CATUPANCA + " के प्राणियों में"),
    "itaresaṃ catuvokāraṃ pañcavokāraṃ upapajjantānaṃ": ("P", OTHERS + " " + CATUPANCA + " में " + REBORN),
    "itaresaṃ catuvokārā pañcavokārā cavantānaṃ": ("P", OTHERS + " " + CATUPANCA + " से " + DYING),
    "itaresaṃ cittasamaṅgīnaṃ": ("P", OTHERS + " मन से युक्त लोगों में"),
    "itaresaṃ": ("P", "बाकी सबमें"),
    "catuvokāraṃ pañcavokāraṃ upapajjantānaṃ": ("P", CATUPANCA + " में " + REBORN),
    "catuvokārā pañcavokārā cavantānaṃ": ("P", CATUPANCA + " से " + DYING),
    "asaññasattaṃ upapajjantānaṃ": ("P", S.WHO["Asaññasattaṃ upapajjantānaṃ"]),
    "asaññasattā cavantānaṃ": ("P", ASANNA_FROM),
    "asaññattā cavantānaṃ": ("P", ASANNA_FROM),          # source slip for asaññasattā
    "asaññasattānaṃ": ("P", "पहचान-रहित प्राणियों में"),
    "nirodhasamāpannānaṃ": ("P", NIRODHASAMAPANNA),
    "suddhāvāsaṃ upapajjantānaṃ": ("P", "शुद्ध निवास लोक में " + REBORN),
    "suddhāvāsānaṃ": ("P", "शुद्ध निवास लोक के प्राणियों में"),
    "āpāyikānaṃ": ("P", "दुर्गति के प्राणियों में"),
    "pacchimacittasamaṅgīnaṃ": ("P", "अंतिम मन से युक्त लोगों में"),
    "cittasamaṅgīnaṃ": ("P", "मन से युक्त लोगों में"),
    "aggamaggasamaṅgīnaṃ": ("P", "सर्वोच्च मार्ग से युक्त लोगों में"),
    "arahantānaṃ": ("P", "अर्हतों में"),
    "avasese catuvokāre pañcavokāre": ("L", "बाकी " + CATUPANCA + " में"),
    "catuvokāre pañcavokāre": ("L", CATUPANCA + " में"),
    "asaññasatte": ("L", S.WHERE["Asaññasatte"]),
    "pañcavokāre": ("L", S.WHERE["Pañcavokāre"]),
    "arūpe": ("L", S.WHERE["Arūpe"]),
    "apāye": ("L", "दुर्गति के लोकों में"),
    "tesaṃ upapajjantānaṃ": ("TP", "उनमें से " + REBORN),
    "tesaṃ cavantānaṃ": ("TP", "उनमें से " + DYING),
    "tesaṃ": ("T", "उनमें"),
    "ye maggaṃ paṭilabhissanti": ("R", "जो मार्ग प्राप्त करेंगे"),
    "ye puthujjanā maggaṃ na paṭilabhissanti": ("R", "जो साधारण व्यक्ति मार्ग प्राप्त नहीं करेंगे"),
    "ye ca puthujjanā maggaṃ na paṭilabhissanti": ("R", "और जो साधारण व्यक्ति मार्ग प्राप्त नहीं करेंगे"),
    "ye caññe maggaṃ paṭilabhissanti": ("R", "और जो दूसरे लोग मार्ग प्राप्त करेंगे"),
    "yassa cittassa anantarā aggamaggaṃ paṭilabhissanti": ("R", R_YASSA),
    "yassa cittassa anantarā aggamaggaṃ paṭilabhissānti": ("R", R_YASSA),   # source slip
    "tassa cittassa uppādakkhaṇe": ("TM", "उस मन के उत्पन्न होने के क्षण में"),
    "tassa cittassa bhaṅgakkhaṇe": ("TM", "उस मन के भंग होने के क्षण में"),
    "pavatte": ("PV", "जीवन के दौरान"),
    "dutiye citte vattamāne": ("V", "दूसरे मन के चलते समय"),
    "dutiye akusale citte vattamāne": ("V", "दूसरे हानिकर मन के चलते समय"),
    "taṇhāvippayuttacitte vattamāne": ("V", "तृष्णा से अलग मन के चलते समय"),
}
for _g, _h in GEN.items():
    for _k, _f in MOMENT.items():
        WHO_TOKENS[f"{_g} {_k}"] = ("M", _f.format(G=_h))
_WHO_KEYS = sorted(WHO_TOKENS, key=len, reverse=True)


def _sep(a, b):
    if a == "PV":
        return " "
    if b in ("M", "V") and a in ("P", "L", "S", "T"):
        return " "
    if a == "R":
        if b in ("R", "T", "TP"):
            return ", "
        return ", उनमें " if b == "TM" else ", उनमें, "
    return ", "


def who(text):
    """Pāli qualifier chain (before the final tesaṃ/tattha) -> Hindi."""
    rest = text.replace(",", "").strip()
    rest = rest[0].lower() + rest[1:]
    items = []
    while rest:
        for k in _WHO_KEYS:
            if rest == k or rest.startswith(k + " "):
                items.append(WHO_TOKENS[k])
                rest = rest[len(k):].strip()
                break
        else:
            raise KeyError("who: " + rest)
    out = items[0][1]
    for (a, _), (b, h) in zip(items, items[1:]):
        out += _sep(a, b) + h
    if items[-1][0] == "R":
        out += ", उनमें"
    return out


# ---------------------------------------------------------------- pavatti answers
_LOC = "tesaṃ tattha|tesaṃ|tattha"
_V = r"(?:na )?\S+"
_X = r"\S+sacca"


def _subj(w):
    return SACCA[re.sub(r"ñca$", "ṃ", w)]


def tr_pavatti_answer(s):
    """One answer sentence without its final period."""
    suffix = ""
    if s.endswith("…pe…"):
        s, suffix = s[:-len("…pe…")], "…"
    m = re.fullmatch(rf"(.+?) ({_LOC}) ({_X}ṃ) ({_V}), no ca ({_LOC}) ({_X}ṃ) ({_V})", s)
    if m:
        w, l1, x, v1, l2, y, v2 = m.groups()
        return S.ANS_BUT.format(WHO=who(w), L1=S.LOC1[l1], X=_subj(x), V1=S.verb(v1)[0],
                                L2=S.LOC2[l2], Y=_subj(y), V2=S.verb_flip(v2)) [:-1] + suffix + "।"
    m = re.fullmatch(rf"(.+?) ({_LOC}) ({_X}ñca) ({_V}) ({_X}ñca) ({_V})", s)
    if m:
        w, l1, x, v1, y, v2 = m.groups()
        return S.ANS_BOTH.format(WHO=who(w), L1=S.LOC1[l1], X=_subj(x), V1=S.verb(v1)[0],
                                 Y=_subj(y), V2=S.verb(v2)[0])[:-1] + suffix + "।"
    m = re.fullmatch(rf"(.+?) ({_LOC}) ({_X}ṃ) ({_V})", s)
    if m and suffix:
        w, l1, x, v1 = m.groups()
        return f"{who(w)}{S.LOC1[l1]} {_subj(x)} {S.verb(v1)[0]}{suffix}।"
    return None


# ---------------------------------------------------------------- questions
_KNOWN = set(SACCA) | set(BARE) | set(S.VERBS_M) | {"n" + v for v in S.VERBS_M if v.startswith("u")}


def untie(word):
    """Remove the quotative -ti: uppajjatīti -> uppajjati, dukkhasaccanti -> dukkhasaccaṃ."""
    if word in _KNOWN:
        return word
    for cand in (word[:-2], word[:-3] + "ṃ", word[:-3] + "i", word[:-3] + "a", word[:-3] + "ā"):
        if cand in _KNOWN:
            return cand
    return word


def tr_pavatti_question(body):
    m = re.fullmatch(rf"(yassa|yattha)( vā pana)?( yattha)? (\S+) ({_V}) (tassa tattha|tassa|tattha) (\S+) ({_V})\?", body)
    if not m:
        return None
    rel, vp, rel2, x, v1, cor, y, v2 = m.groups()
    return S.PAVATTI_Q.format(AND=S.VA_PANA if vp else "", REL=S.Q_REL[rel + (rel2 or "")], X=SACCA[x],
                              V1=S.verb(v1)[0], COR=S.Q_COR[cor], Y=SACCA[y], V2=S.verb(v2)[0])


def tr_pannatti_question(body):
    m = re.fullmatch(r"(na )?(\S+) (na )?(\S+)\?", body)
    if not m or bool(m.group(1)) != bool(m.group(3)):
        return None
    n1, x, _, y = m.groups()
    xh, _, pl = noun(x)
    yh = noun(y)[0]
    v = "हैं" if pl else "है"
    if n1:
        return S.PANNATTI_Q_PACC.format(X=xh, Y=yh, V=v, P="वे" if pl else "वह")
    return S.PANNATTI_Q_ANU.format(X=xh, Y=yh, V=v)


# pariññā: verbs (positive, negative); past forms take the ergative relative जिसने / उसने
PARI = {
    "parijānāti": ("पूरी तरह समझता है", "पूरी तरह नहीं समझता"),
    "parijānittha": ("पूरी तरह समझा था", "पूरी तरह नहीं समझा था"),
    "parijānissati": ("पूरी तरह समझेगा", "पूरी तरह नहीं समझेगा"),
    "parijānanti": ("पूरी तरह समझते हैं", "पूरी तरह नहीं समझते"),
    "pajahati": ("छोड़ता है", "नहीं छोड़ता"),
    "pajahittha": ("छोड़ा था", "नहीं छोड़ा था"),
    "pajahissati": ("छोड़ेगा", "नहीं छोड़ेगा"),
    "pajahissanti": ("छोड़ेंगे", "नहीं छोड़ेंगे"),
}


_KNOWN |= set(PARI) | {"nap" + v for v in PARI if v.startswith("pa")}


def pverb(tok):
    if tok.startswith("na "):
        return PARI[tok[3:]][1]
    if tok.startswith("napp"):
        return PARI[tok[3:]][1]
    return PARI[tok][0]


def tr_parinna_question(body):
    m = re.fullmatch(r"yo( vā pana)? (\S+) ((?:na )?\S+) so (\S+) ((?:na )?\S+)\?", body)
    if not m:
        return None
    vp, x, v1, y, v2 = m.groups()
    past1, past2 = v1.endswith("ittha"), v2.endswith("ittha")
    rel = "जिसने" if past1 else "जो"
    cor = "उसने" if past2 else "वह"
    return f"{S.VA_PANA if vp else ''}{rel} {SACCA_OBL[x]} को {pverb(v1)}, क्या {cor} {SACCA_OBL[y]} को {pverb(v2)}?"


def tr_question(q):
    """q: a question with its '?', no label; the quotative -ti still on the last word."""
    words = q[:-1].split(" ")
    words[-1] = untie(words[-1])
    q2 = " ".join(words) + "?"
    q2 = q2[0].lower() + q2[1:]
    for f in (tr_pavatti_question, tr_pannatti_question, tr_parinna_question):
        try:
            r = f(q2)
        except KeyError:
            r = None
        if r:
            return r
    raise ValueError("untranslated question: " + q)


# ---------------------------------------------------------------- paṇṇatti answers
KAYIKA = "Kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ"
KAYIKA_HI = "शारीरिक दुःख और मानसिक दुःख"           # pi-1 kāyika / cetasika dukkha


def _obj(p):
    """object of ṭhapetvā -> Hindi (oblique)."""
    p = p[0].upper() + p[1:]
    if p == KAYIKA:
        return KAYIKA_HI
    parts = re.fullmatch(r"(\S+)ñca (\S+)ñca|(\S+) ca (\S+)ñca", p)
    if parts:
        a, b = [g for g in parts.groups() if g]
        return f"{noun(a)[1]} और {noun(b)[1]}"
    return noun(p)[1]


def tr_pannatti_answer(s):
    """one answer sentence without its final period."""
    s = s[0].upper() + s[1:]
    av = r"avases(o|aṃ|ā)"
    m = re.fullmatch(rf"(.+?) ṭhapetvā {av} ([^\s,]+),? na (\S+)", s)
    if m and not s.split(" ṭhapetvā ")[1].split(" ")[1] == "na":
        o, n, x, y = m.groups()
        v = "हैं" if n == "ā" else "है"
        return f"{_obj(o)} को छोड़कर {S.AVASESA} {noun(x)[0]}, {noun(y)[0]} नहीं {v}"
    m = re.fullmatch(rf"(.+?) ṭhapetvā {av} na ceva (\S+) na ca (\S+)", s)
    if m:
        o, n, b, c = m.groups()
        v = "हैं" if n == "ā" else "है"
        return f"{_obj(o)} को छोड़कर {S.AVASESA} न तो {noun(b)[0]} {v}, न {noun(c)[0]}"
    m = re.fullmatch(rf"(.+?) ṭhapetvā avasesā saccā na (\S+), saccā", s)
    if m:
        o, y = m.groups()
        return f"{_obj(o)} को छोड़कर {S.AVASESA} सत्य, {noun(y)[0]} नहीं हैं, पर सत्य हैं"
    m = re.fullmatch(rf"(.+?) ṭhapetvā {av} na (\S+?),? (\S+)", s)
    if m:
        o, n, y, x = m.groups()
        v = "हैं" if n == "ā" else "है"
        return f"{_obj(o)} को छोड़कर {S.AVASESA}, {noun(y)[0]} नहीं {v}, पर {noun(x)[0]} {v}"
    m = re.fullmatch(r"(.+) (\S+?)(?:ñceva| ceva) (\S+?ñca)", s)
    if m:
        subj, x, z = m.groups()
        sh = KAYIKA_HI if subj == KAYIKA else noun(subj)[0]
        v = "हैं" if subj == KAYIKA else "है"
        return f"{sh}, {noun(x)[0]} भी {v} और {noun(z)[0]} भी"
    m = re.fullmatch(r"Avasesā saccā na (\S+)", s)
    if m:
        return f"{S.AVASESA} सत्य, {noun(m.group(1))[0]} नहीं हैं"
    m = re.fullmatch(r"(\S+) ṭhapetvā", s)
    if m:
        return f"{_obj(m.group(1))} को छोड़कर"
    return None


# ---------------------------------------------------------------- fragments with …pe…
def tr_fragment(t):
    """'(Kha) yassa vā pana…pe… uppajjitthāti? Āmantā.', 'Yattha dukkhasaccaṃ uppajjittha…pe….' …"""
    m = re.fullmatch(rf"(\((?:Ka|Kha)\) )?([Yy]assa|[Yy]attha|yo)( vā pana)?( yattha)?(?: ({_X}ṃ) ({_V}))?…pe…(?: (\S+?))?([?.])(?: (.*))?", t)
    if not m:
        return None
    lab, rel, vp, rel2, x, v1, v2, punct, ans = m.groups()
    out = (S.LABELS[lab.strip()] + " " if lab else "") + (S.VA_PANA if vp else "")
    out += {"yo": "जो"}.get(rel) or S.Q_REL[rel.lower() + (rel2 or "")]
    if x:
        out += f" {SACCA[x]} {S.verb(v1)[0]}"
    out += "…"
    if v2:
        out += " " + S.verb(untie(v2))[0]
    out += "?" if punct == "?" else "।"
    if ans:
        out += " " + SHORT[ans]
    return out


# ---------------------------------------------------------------- line translation
LABEL_RE = re.compile(r"^(\((?:Ka|Kha)\)) (.*)$")


def tr_sentence(s):
    """One statement; with its final '.' (-> «।») or open (before …pe…)."""
    if s in SHORT:
        return SHORT[s]
    if s in ANSWER_WORDS:
        return ANSWER_WORDS[s]
    closed = s.endswith(".")
    core = s[:-1] if closed else s
    r = tr_pavatti_answer(core) if closed else None
    if r is None:
        r = tr_pannatti_answer(core)
        if r is not None and closed:
            r += "।"
    if r is None:
        raise ValueError("untranslated sentence: " + s)
    return r


def tr_unit(u):
    """Questions (with or without label) and statements, in sequence."""
    outs = []
    for part in re.split(r"(?<=[?.]) ", u):
        if part == "":
            outs.append("")
            continue
        if part.endswith("?"):
            m = LABEL_RE.match(part)
            if m:
                outs.append(S.LABELS[m.group(1)] + " " + tr_question(m.group(2)))
            else:
                outs.append(tr_question(part))
        else:
            outs.append(tr_sentence(part))
    return " ".join(outs)


_PE = re.compile(r"…[Pp]e…")


def tr_text(t):
    if t in FIXED:
        return FIXED[t]
    if t in SHORT:
        return SHORT[t]
    r = tr_fragment(t)
    if r:
        return r
    if "?" not in t:
        try:
            return tr_unit(t)
        except (ValueError, KeyError):
            if not _PE.search(t):
                raise
    if _PE.search(t):
        outs = []
        for p in _PE.split(t):
            lead = " " if p.startswith(" ") else ""
            trail = " " if p.endswith(" ") and p.strip() else ""
            p = p.strip()
            if p == "":
                outs.append(lead)
            elif p == ".":
                outs.append("।")
            elif p.startswith(". "):
                outs.append("। " + tr_unit(p[2:]) + trail)
            else:
                outs.append(lead + tr_unit(p) + trail)
        return "…".join(outs)
    return tr_unit(t)


# source slips corrected before translation (reported in the notes)
SLIPS = [
    ("tassa tattha samudayasaccaṃ nirujjhitthāti.", "tassa tattha samudayasaccaṃ nirujjhitthāti?"),
    ("samudayasaccañca na nirujjhiti", "samudayasaccañca na nirujjhati"),
]


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
    elif text in FIXED:
        out = FIXED[text]
    else:
        brackets = re.findall(r" ?(\[[^\]]*\])", text)
        clean = re.sub(r" ?\[[^\]]*\]", "", text)
        for a, b in SLIPS:
            clean = clean.replace(a, b)
        out = tr_text(clean)
        for b in brackets:
            hb, anchor, nth = VARIANTS[b]
            idx = -1
            for _ in range(nth):
                idx = out.index(anchor, idx + 1)
            pos = idx + len(anchor)
            out = out[:pos] + " " + hb + out[pos:]
    return out + (" " + bid if bid else "")


# ---------------------------------------------------------------- fixed lines (editorial notes, uddesa, pariññā answers)
def _both_q(who_pali, l1, x, v1, y, v2):
    return S.ANS_BOTH.format(WHO=who(who_pali), L1=S.LOC1[l1], X=SACCA[x], V1=S.verb(v1)[0], Y=SACCA[y], V2=S.verb(v2)[0])


DUK, SAM = SACCA_OBL["dukkhasaccaṃ"], SACCA_OBL["samudayasaccaṃ"]
ARAHA = "अर्हत्"
AGGA_SAMANGI = "सर्वोच्च मार्ग से युक्त व्यक्ति"   # aggamaggasamaṅgī
PUTHU_REL = "जो साधारण व्यक्ति मार्ग प्राप्त नहीं करेंगे"
MAGGA_REL = "जो मार्ग प्राप्त करेंगे"

FIXED = dict(S.FIXED)
FIXED.update({
    "Cattāri saccāni – dukkhasaccaṃ, samudayasaccaṃ nirodhasaccaṃ, maggasaccaṃ.":
        "चार सत्य – " + ", ".join(SACCA.values()) + "।",
    "Uppādavāro.": "उत्पन्न होने का खंड।",
    "Nirodhavāro.": "समाप्त होने का खंड।",
    "Uppādanirodhavāro.": "उत्पन्न होने और समाप्त होने का खंड।",
    "Pavattivāro niṭṭhito.": "प्रक्रिया का खंड पूरा हुआ।",
    "Pariññāvāro.": "पूरी तरह समझने का खंड।",
    "Saccayamakaṃ niṭṭhitaṃ.": S.CHAPTER_END.format(title=S.CHAPTER_TITLES["Saccayamakaṃ"]),
    # editorial notes on the abridged sub-sections
    "(Yassakampi yassayatthakampi sadisaṃ vitthāretabbaṃ).":
        f"({obl(YASSAKA)} को भी और {obl(YASSAYATTHAKA)} को भी इसी तरह विस्तार से कहना चाहिए)।",
    "(Yatthakampi sabbattha sadisaṃ. Tantinānākaraṇaṃ heṭṭhā yatthakasadisaṃ).":
        f"({YATTHAKA} भी हर जगह एक जैसा है। पाठ का अंतर पहले वाले {obl(YATTHAKA)} जैसा है)।",
    "Yattha dukkhasaccaṃ uppajjati…pe… (yatthakā sadisā sabbe).":
        f"जिस स्थान पर {SACCA['dukkhasaccaṃ']} उत्पन्न होता है… (“जिस स्थान पर” वाले सभी खंड एक जैसे हैं)।",
    "Yattha dukkhasaccaṃ uppajjati…pe… (yatthakampi yassayatthakasadisaṃ kātabbaṃ).":
        f"जिस स्थान पर {SACCA['dukkhasaccaṃ']} उत्पन्न होता है… ({obl(YATTHAKA)} को भी {obl(YASSAYATTHAKA)} जैसा बनाना चाहिए)।",
    "(Yatthakaṃ uppādepi nirodhepi uppādanirodhepi sadisaṃ, natthi nānākaraṇaṃ).":
        f"({YATTHAKA} उत्पन्न होने में, समाप्त होने में और उत्पन्न होने और समाप्त होने में भी एक जैसा है, कोई अंतर नहीं है)।",
    "(Yassayatthakampi sadisaṃ vitthāretabbaṃ).":
        f"({obl(YASSAYATTHAKA)} को भी इसी तरह विस्तार से कहना चाहिए)।",
    "(Yassakampi [yassakampi yatthakampi (sī. syā.)] yassayatthakampi sadisaṃ, yassayatthakepi nirodhasamāpannānanti cetaṃ na kātabbaṃ).":
        f"({YASSAKA} {var(S.VAR_READ, 'Sī., Syā.', 'yassakampi yatthakampi')} और {YASSAYATTHAKA} भी एक जैसे हैं, "
        f"पर {obl(YASSAYATTHAKA)} में “{NIRODHASAMAPANNA}” यह नहीं जोड़ना चाहिए)।",
    "(Yathā uppādavāre atītā pucchā anulomampi paccanīkampi vibhattā evaṃ nirodhepi vibhajitabbā, natthi nānākaraṇaṃ).":
        "(जैसे उत्पन्न होने के खंड में अतीत के प्रश्न सकारात्मक और नकारात्मक दोनों रूपों में बाँटकर बताए गए हैं, "
        "वैसे ही समाप्त होने में भी बाँटकर बताने चाहिए, कोई अंतर नहीं है)।",
    "(Yassakampi yassayatthakampi sadisaṃ).":
        f"({YASSAKA} और {YASSAYATTHAKA} भी एक जैसे हैं)।",
    "(Yatthakaṃ uppādavārepi nirodhavārepi uppādanirodhavārepi sadisaṃ natthi nānākaraṇaṃ).":
        f"({YATTHAKA} उत्पन्न होने के खंड में, समाप्त होने के खंड में और उत्पन्न होने और समाप्त होने के खंड में भी एक जैसा है, कोई अंतर नहीं है)।",
    "(Yassakampi yassayatthakampi sadisaṃ, yassayatthakepi nirodhasamāpannānanti na kātabbaṃ).":
        f"({YASSAKA} और {YASSAYATTHAKA} भी एक जैसे हैं, पर {obl(YASSAYATTHAKA)} में “{NIRODHASAMAPANNA}” नहीं जोड़ना चाहिए)।",
    "(Atītā pucchā yathā uppādavāre vibhattā evaṃ uppādanirodhavārepi anulomampi paccanīkampi vibhajitabbaṃ).":
        "(अतीत के प्रश्न जैसे उत्पन्न होने के खंड में बाँटकर बताए गए हैं, वैसे ही उत्पन्न होने और समाप्त होने के खंड में भी "
        "सकारात्मक और नकारात्मक दोनों रूपों में बाँटकर बताने चाहिए)।",
    "(Yassakampi yassayatthakampi sadisaṃ, samudayasaccaṃ maggasaccaṃ nānākaraṇaṃ, aggamaggassa bhaṅgakkhaṇe, arahantānaṃ asaññasattānaṃ tesaṃ tattha maggasaccañca na nirujjhissati samudayasaccañca nuppajjissati).":
        f"({YASSAKA} और {YASSAYATTHAKA} भी एक जैसे हैं, उत्पत्ति के सत्य और मार्ग के सत्य में अंतर है, "
        + _both_q("aggamaggassa bhaṅgakkhaṇe arahantānaṃ asaññasattānaṃ", "tesaṃ tattha", "maggasaccaṃ",
                  "na nirujjhissati", "samudayasaccaṃ", "nuppajjissati")[:-1] + ")।",
    "(Paccuppannaatītā [paccuppannenātītā (syā.)] pucchā uppādavārepi uppādanirodhavārepi yassakampi yatthakampi yassayatthakampi anulomampi paccanīkampi sadisaṃ, asammohantena vibhajitabbā).":
        f"(वर्तमान और अतीत के प्रश्न {var(S.VAR_SPELL, 'Syā.', 'paccuppannenātītā')} उत्पन्न होने के खंड में भी और "
        f"उत्पन्न होने और समाप्त होने के खंड में भी, {obl(YASSAKA)} में, {obl(YATTHAKA)} में और {obl(YASSAYATTHAKA)} में, "
        "सकारात्मक और नकारात्मक दोनों रूपों में एक जैसे हैं, इन्हें बिना भ्रम के बाँटकर बताना चाहिए)।",
    "(Yathā nirodhavāre atītānāgatā [atītenānāgatā (syā.)] pucchā anulomampi paccanīkampi vibhattā evaṃ uppādanirodhavārepi asammohantena vibhajitabbaṃ).":
        f"(जैसे समाप्त होने के खंड में अतीत और भविष्य के प्रश्न {var(S.VAR_SPELL, 'Syā.', 'atītenānāgatā')} "
        "सकारात्मक और नकारात्मक दोनों रूपों में बाँटकर बताए गए हैं, वैसे ही उत्पन्न होने और समाप्त होने के खंड में भी "
        "बिना भ्रम के बाँटकर बताने चाहिए)।",
    # abridged answer lines
    "Aggamaggasamaṅgīnaṃ arahantānaṃ yassa cittassa anantarā aggamaggaṃ paṭilabhissanti asaññasattānaṃ tesaṃ tattha …pe… itaresaṃ catuvokārānaṃ pañcavokārānaṃ tesaṃ tattha…pe…. (Yassakampi yassayatthakampi sadisaṃ).":
        who("Aggamaggasamaṅgīnaṃ arahantānaṃ yassa cittassa anantarā aggamaggaṃ paṭilabhissanti asaññasattānaṃ")
        + " वहाँ … " + who("itaresaṃ catuvokārānaṃ pañcavokārānaṃ") + " वहाँ…। "
        + f"({YASSAKA} और {YASSAYATTHAKA} भी एक जैसे हैं)।",
    "Aggamaggassa uppādakkhaṇe arahantānaṃ cittassa uppādakkhaṇe yassa cittassa anantarā aggamaggaṃ paṭilabhissanti tassa cittassa uppādakkhaṇe asaññasattaṃ upapajjantānaṃ tesaṃ tattha dukkhasaccaṃ…pe… itaresaṃ catuvokāraṃ pañcavokāraṃ upapajjantānaṃ pavatte cittassa uppādakkhaṇe tesaṃ tattha dukkhasaccaṃ…pe….":
        who("Aggamaggassa uppādakkhaṇe arahantānaṃ cittassa uppādakkhaṇe yassa cittassa anantarā aggamaggaṃ paṭilabhissanti tassa cittassa uppādakkhaṇe asaññasattaṃ upapajjantānaṃ")
        + f" वहाँ {SACCA['dukkhasaccaṃ']}… "
        + who("itaresaṃ catuvokāraṃ pañcavokāraṃ upapajjantānaṃ pavatte cittassa uppādakkhaṇe")
        + f" वहाँ {SACCA['dukkhasaccaṃ']}…।",
    # pariññāvāra answers
    "Arahā dukkhasaccaṃ na parijānāti, no ca samudayasaccaṃ nappajahittha. Aggamaggasamaṅgiñca arahantañca ṭhapetvā avasesā puggalā dukkhasaccañca na parijānanti samudayasaccañca nappajahittha.":
        f"{ARAHA} {DUK} को पूरी तरह नहीं समझता, पर उसने {SAM} को छोड़ा था। "
        f"{AGGA_SAMANGI} और {ARAHA} को छोड़कर {S.AVASESA} व्यक्ति {DUK} को भी पूरी तरह नहीं समझते और उन्होंने {SAM} को भी नहीं छोड़ा था।",
    "Aggamaggasamaṅgī samudayasaccaṃ nappajahittha, no ca dukkhasaccaṃ na parijānāti. Aggamaggasamaṅgiñca arahantañca ṭhapetvā avasesā puggalā samudayasaccañca nappajahittha dukkhasaccañca na parijānanti.":
        f"{AGGA_SAMANGI} ने {SAM} को नहीं छोड़ा था, पर वह {DUK} को पूरी तरह समझता है। "
        f"{AGGA_SAMANGI} और {ARAHA} को छोड़कर {S.AVASESA} व्यक्तियों ने {SAM} को भी नहीं छोड़ा था और वे {DUK} को भी पूरी तरह नहीं समझते।",
    "Ye maggaṃ paṭilabhissanti te dukkhasaccaṃ na parijānanti, no ca samudayasaccaṃ nappajahissanti. Arahā ye ca puthujjanā maggaṃ na paṭilabhissanti te dukkhasaccañca na parijānanti samudayasaccañca nappajahissanti.":
        f"{MAGGA_REL}, वे {DUK} को पूरी तरह नहीं समझते, पर {SAM} को छोड़ेंगे। "
        f"{ARAHA} और {PUTHU_REL}, वे {DUK} को भी पूरी तरह नहीं समझते और {SAM} को भी नहीं छोड़ेंगे।",
    "Aggamaggasamaṅgī samudayasaccaṃ nappajahissati, no ca dukkhasaccaṃ na parijānāti. Arahā ye ca puthujjanā maggaṃ na paṭilabhissanti te samudayasaccañca nappajahissanti dukkhasaccañca na parijānanti.":
        f"{AGGA_SAMANGI} {SAM} को नहीं छोड़ेगा, पर {DUK} को पूरी तरह समझता है। "
        f"{ARAHA} और {PUTHU_REL}, वे {SAM} को भी नहीं छोड़ेंगे और {DUK} को भी पूरी तरह नहीं समझते।",
    "Ye maggaṃ paṭilabhissanti te dukkhasaccaṃ na parijānittha, no ca te samudayasaccaṃ nappajahissanti. Aggamaggasamaṅgī ye ca puthujjanā maggaṃ na paṭilabhissanti te dukkhasaccañca na parijānittha samudayasaccañca nappajahissanti.":
        f"{MAGGA_REL}, उन्होंने {DUK} को पूरी तरह नहीं समझा था, पर वे {SAM} को छोड़ेंगे। "
        f"{AGGA_SAMANGI} और {PUTHU_REL}, उन्होंने {DUK} को भी पूरी तरह नहीं समझा था और वे {SAM} को भी नहीं छोड़ेंगे।",
    "Arahā samudayasaccaṃ nappajahissati, no ca dukkhasaccaṃ na parijānittha. Aggamaggasamaṅgī ye ca puthujjanā maggaṃ na paṭilabhissanti te samudayasaccañca nappajahissanti dukkhasaccañca na parijānittha.":
        f"{ARAHA} {SAM} को नहीं छोड़ेगा, पर उसने {DUK} को पूरी तरह समझा था। "
        f"{AGGA_SAMANGI} और {PUTHU_REL}, वे {SAM} को भी नहीं छोड़ेंगे और उन्होंने {DUK} को भी पूरी तरह नहीं समझा था।",
})


# ---------------------------------------------------------------- build
FILES = ["5-01-saccayamaka.md", "5-02-saccayamaka.md", "5-03-saccayamaka.md"]


def build(fname):
    raw = (PALI_DIR / fname).read_text(encoding="utf-8").splitlines()
    out = [tr_line(l) for l in raw]
    (HI_DIR / fname).write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
    print(fname, len([l for l in raw if l.strip()]), "lines")


if __name__ == "__main__":
    for f in (sys.argv[1:] or FILES):
        build(f)
