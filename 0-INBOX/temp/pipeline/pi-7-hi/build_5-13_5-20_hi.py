"""Builder for the pi-7 Hindi plain zero-shot, files 5-13 .. 5-20.

    python -I -B -X utf8 build_5-13_5-20_hi.py            # write all 8 files
    python -I -B -X utf8 build_5-13_5-20_hi.py --dry      # report unknown fragments only

Every line is composed from fixed frames (build_sample_hi) and the item tables below, so identical
Pāli always gives identical Hindi. Unknown words/fragments raise and are listed.
"""
import pathlib
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi")
import build_sample_hi as S  # noqa: E402

FILES = ["5-13-anulomapaccaniya-tikatika", "5-14-anulomapaccaniya-dukaduka",
         "5-15-paccaniyanuloma-tika", "5-16-paccaniyanuloma-duka",
         "5-17-paccaniyanuloma-dukatika", "5-18-paccaniyanuloma-tikaduka",
         "5-19-paccaniyanuloma-tikatika", "5-20-paccaniyanuloma-dukaduka"]

# extra number words used in these files (count_hi reads S.NUM)
S.NUM.update({
    "chabbīsati": "छब्बीस", "chabbīsa": "छब्बीस", "ekūnapaññāsa": "उनचास", "dvāvīsa": "बाईस",
    "dvāvīsati": "बाईस", "tevīsa": "तेईस", "ekavīsa": "इक्कीस", "aṭṭhavīsa": "अट्ठाईस",
    "pañcatiṃsa": "पैंतीस", "tīṇiyeva": "तीन ही", "tīṇimeva": "तीन ही", "ekameva": "एक ही",
    "pañceva": "पाँच ही", "catuvīsa": "चौबीस",
})

# =====================================================================================
# 1. Item lexicon (pi-1 1-matika.md item names, singular, agreeing with परिघटना)
# =====================================================================================
ITEMS = {
    # triads
    "kusala": "हितकर", "akusala": "हानिकर", "abyākata": "नैतिक रूप से अनिर्धारित",
    "sukhāya vedanāya sampayutta": "सुखद अनुभूति से जुड़ी",
    "dukkhāya vedanāya sampayutta": "दुःखद अनुभूति से जुड़ी",
    "adukkhamasukhāya vedanāya sampayutta": "न दुःखद, न सुखद अनुभूति से जुड़ी",
    "vipāka": "कर्म-फल रूपी", "vipākadhammadhamma": "कर्म-फल उत्पन्न करने वाली",
    "nevavipākanavipākadhammadhamma": "न कर्म-फल रूपी, न कर्म-फल उत्पन्न करने वाली",
    "upādinnupādāniya": "कर्म से उत्पन्न और आसक्ति का विषय बनने वाली",
    "anupādinnupādāniya": "कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाली",
    "anupādinnaanupādāniya": "न कर्म से उत्पन्न, न आसक्ति का विषय बनने वाली",
    "saṃkiliṭṭhasaṃkilesika": "क्लेशों से मलिन और क्लेशों का विषय बनने वाली",
    "asaṃkiliṭṭhasaṃkilesika": "क्लेशों से मलिन न होने वाली, पर क्लेशों का विषय बनने वाली",
    "asaṃkiliṭṭhaasaṃkilesika": "क्लेशों से मलिन न होने वाली और क्लेशों का विषय न बनने वाली",
    "savitakkasavicāra": "आरंभिक विचार और सतत विचार वाली",
    "avitakkavicāramatta": "आरंभिक विचार से रहित, केवल सतत विचार वाली",
    "avitakkaavicāra": "आरंभिक विचार और सतत विचार दोनों से रहित",
    "pītisahagata": "उल्लास के साथ होने वाली", "sukhasahagata": "सुख के साथ होने वाली",
    "upekkhāsahagata": "समभाव के साथ होने वाली",
    "napītisahagata": "उल्लास के साथ न होने वाली", "nasukhasahagata": "सुख के साथ न होने वाली",
    "naupekkhāsahagata": "समभाव के साथ न होने वाली",
    "dassanena pahātabba": "सत्य-दर्शन से छोड़ी जाने वाली",
    "bhāvanāya pahātabba": "मानसिक अभ्यास से छोड़ी जाने वाली",
    "nevadassanena nabhāvanāya pahātabba": "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़ी जाने वाली",
    "nadassanena pahātabba": "सत्य-दर्शन से न छोड़ी जाने वाली",
    "nabhāvanāya pahātabba": "मानसिक अभ्यास से न छोड़ी जाने वाली",
    "dassanena pahātabbahetuka": "सत्य-दर्शन से छोड़े जाने वाले मूलों वाली",
    "bhāvanāya pahātabbahetuka": "मानसिक अभ्यास से छोड़े जाने वाले मूलों वाली",
    "nevadassanena nabhāvanāya pahātabbahetuka": "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़े जाने वाले मूलों वाली",
    "nadassanena pahātabbahetuka": "सत्य-दर्शन से छोड़े जाने वाले मूलों से रहित",
    "nabhāvanāya pahātabbahetuka": "मानसिक अभ्यास से छोड़े जाने वाले मूलों से रहित",
    "ācayagāmī": "संचय की ओर ले जाने वाली", "apacayagāmī": "संचय घटाने की ओर ले जाने वाली",
    "nevācayagāmināpacayagāmī": "न संचय की ओर, न संचय घटाने की ओर ले जाने वाली",
    "sekkha": "सीखने के चरण की", "asekkha": "सीखना पूरा होने के चरण की",
    "nevasekkhanāsekkha": "न सीखने के चरण की, न सीखना पूरा होने के चरण की",
    "paritta": "सीमित", "mahaggata": "उन्नत", "appamāṇa": "अपरिमित",
    "parittārammaṇa": "सीमित विषय वाली", "mahaggatārammaṇa": "उन्नत विषय वाली",
    "appamāṇārammaṇa": "अपरिमित विषय वाली",
    "hīna": "हीन", "majjhima": "मध्यम", "paṇīta": "उत्तम",
    "micchattaniyata": "ग़लत दिशा में निश्चित", "sammattaniyata": "सही दिशा में निश्चित",
    "aniyata": "अनिश्चित", "niyata": "निश्चित",
    "maggārammaṇa": "मार्ग को विषय बनाने वाली", "maggahetuka": "मार्ग को मूल बनाने वाली",
    "maggādhipati": "मार्ग की प्रधानता वाली",
    "uppanna": "उत्पन्न हो चुकी", "anuppanna": "उत्पन्न न हुई", "uppādī": "उत्पन्न होने वाली",
    "atīta": "अतीत की", "anāgata": "भविष्य की", "paccuppanna": "वर्तमान की",
    "atītārammaṇa": "अतीत के विषय वाली", "anāgatārammaṇa": "भविष्य के विषय वाली",
    "paccuppannārammaṇa": "वर्तमान के विषय वाली",
    "ajjhatta": "स्वयं से संबंधित", "bahiddhā": "दूसरों से संबंधित",
    "ajjhattabahiddhā": "स्वयं और दूसरों दोनों से संबंधित",
    "ajjhattārammaṇa": "स्वयं से संबंधित विषय वाली", "bahiddhārammaṇa": "दूसरों से संबंधित विषय वाली",
    "sanidassanasappaṭigha": "दिखाई देने वाली और टकराव वाली",
    "anidassanasappaṭigha": "दिखाई न देने वाली, पर टकराव वाली",
    "anidassanaappaṭigha": "दिखाई न देने वाली और टकराव से रहित",
    # dyads
    "hetu": "मूल रूपी", "nahetu": "मूल रूपी न होने वाली",
    "sahetuka": "मूल वाली", "ahetuka": "मूल से रहित",
    "hetusampayutta": "मूलों से जुड़ी", "hetuvippayutta": "मूलों से अलग",
    "sappaccaya": "कारणों पर निर्भर रहने वाली", "appaccaya": "कारणों पर निर्भर न रहने वाली",
    "saṅkhata": "निर्मित", "asaṅkhata": "अनिर्मित",
    "sanidassana": "दिखाई देने वाली", "anidassana": "दिखाई न देने वाली",
    "sappaṭigha": "टकराव वाली", "appaṭigha": "टकराव से रहित",
    "rūpī": "भौतिक", "arūpī": "अभौतिक", "lokiya": "लौकिक", "lokuttara": "लोकोत्तर",
    "kenaci viññeyya": "किसी एक प्रकार की चेतना से जानी जा सकने वाली",
    "nakenaci viññeyya": "किसी एक प्रकार की चेतना से न जानी जा सकने वाली",
    "kenaci naviññeyya": "किसी एक प्रकार की चेतना से न जानी जा सकने वाली",
    "āsava": "मन के मैल रूपी", "noāsava": "मन के मैल रूपी न होने वाली",
    "sāsava": "मन के मैलों का विषय बनने वाली", "anāsava": "मन के मैलों का विषय न बनने वाली",
    "āsavasampayutta": "मन के मैलों से जुड़ी", "āsavavippayutta": "मन के मैलों से अलग",
    "saññojana": "बंधन रूपी", "gantha": "गाँठ रूपी", "ogha": "बाढ़ रूपी", "yoga": "जकड़न रूपी",
    "nīvaraṇa": "बाधा रूपी", "parāmāsa": "ग़लत धारणा रूपी",
    "sārammaṇa": "विषय वाली", "anārammaṇa": "विषय से रहित",
    "citta": "मन रूपी", "cetasika": "मन की सहचर", "acetasika": "मन की सहचर न होने वाली",
    "cittasampayutta": "मन से जुड़ी", "cittavippayutta": "मन से अलग",
    "cittasaṃsaṭṭha": "मन से घुली-मिली", "cittavisaṃsaṭṭha": "मन से घुली-मिली न होने वाली",
    "cittasamuṭṭhāna": "मन से उत्पन्न", "nocittasamuṭṭhāna": "मन से उत्पन्न न होने वाली",
    "cittasahabhū": "मन के साथ-साथ होने वाली", "nocittasahabhū": "मन के साथ-साथ न होने वाली",
    "cittānuparivattī": "मन का अनुसरण करने वाली", "nocittānuparivattī": "मन का अनुसरण न करने वाली",
    "cittasaṃsaṭṭhasamuṭṭhāna": "मन से घुली-मिली और मन से उत्पन्न",
    "cittasaṃsaṭṭhasamuṭṭhānasahabhū": "मन से घुली-मिली, मन से उत्पन्न और मन के साथ-साथ होने वाली",
    "cittasaṃsaṭṭhasamuṭṭhānānuparivattī": "मन से घुली-मिली, मन से उत्पन्न और मन का अनुसरण करने वाली",
    "ajjhattika": "आंतरिक", "bāhira": "बाह्य", "upādā": "व्युत्पन्न", "noupādā": "व्युत्पन्न न होने वाली",
    "upādinna": "कर्म से उत्पन्न", "anupādinna": "कर्म से उत्पन्न न होने वाली",
    "upādāna": "आसक्ति रूपी", "kilesa": "मन के क्लेश रूपी",
    "savitakka": "आरंभिक विचार वाली", "avitakka": "आरंभिक विचार से रहित",
    "savicāra": "सतत विचार वाली", "avicāra": "सतत विचार से रहित",
    "sappītika": "उल्लास वाली", "appītika": "उल्लास से रहित",
    "kāmāvacara": "इंद्रिय-सुखों के लोक से संबंधित", "rūpāvacara": "सूक्ष्म भौतिक लोक से संबंधित",
    "arūpāvacara": "अभौतिक लोक से संबंधित",
    "pariyāpanna": "अस्तित्व के लोकों में समाई हुई", "apariyāpanna": "अस्तित्व के लोकों में न समाई हुई",
    "niyyānika": "मुक्ति की ओर ले जाने वाली", "aniyyānika": "मुक्ति की ओर न ले जाने वाली",
    "sauttara": "सर्वोच्च न होने वाली", "anuttara": "सर्वोच्च",
    "saraṇa": "संघर्ष वाली", "araṇa": "संघर्ष से रहित",
}

CONJ_SUFFIX = [("ñceva", "ceva"), ("ñca", "ca")]
CASE_END = ["assa", "issa", "ussa", "ino", "uno", "ṃ"]


def stem(w):
    for e in CASE_END:
        if w.endswith(e) and len(w) > len(e) + 1:
            w = w[: -len(e)]
            break
    if w and w[-1] in "aāiīuūo":
        w = w[:-1]
    return w


def key_of(words):
    return tuple(words[:-1]) + (stem(words[-1]),)


LEX = {}
for _p, _h in ITEMS.items():
    LEX[key_of(_p.split())] = _h


def neg(p):
    """na/no + item: '<P> न होने वाली'; quote P when it already holds a comma or a 'न'."""
    if "," in p or " न " in f" {p} ":
        return f"“{p}” न होने वाली"
    return f"{p} न होने वाली"


class Unknown(Exception):
    pass


def lookup(ws):
    """ws: list of words (case endings on the last word). Returns Hindi or None."""
    first = ws[0]
    negs = 0
    while True:
        k = key_of([first] + ws[1:])
        if k in LEX:
            p = LEX[k]
            for _ in range(negs):
                p = neg(p)
            return p
        if first.startswith("na") and len(first) > 3:
            first = first[2:]
        elif first.startswith("no") and len(first) > 3:
            first = first[2:]
        else:
            return None
        negs += 1


def tokens(s):
    out = []
    for w in s.split():
        w = w[0].lower() + w[1:]
        for suf, mark in CONJ_SUFFIX:
            if w.endswith(suf) and len(w) > len(suf) + 1:
                out += [w[: -len(suf)] + "ṃ", mark]
                break
        else:
            out.append(w)
    return out


def item_at(t, i):
    for n in (3, 2, 1):
        if i + n <= len(t) and not any(x in ("ca", "ceva") for x in t[i:i + n]):
            h = lookup(t[i:i + n])
            if h is not None:
                return h, i + n
    raise Unknown(" ".join(t[i:]))


NACA = {"na": 0, "no": 0, "nana": 1, "nano": 1}


def members(s):
    """Parse an item group into members (list of Hindi strings)."""
    t = tokens(s)
    mems, units, i = [], [], 0
    while i < len(t):
        w = t[i]
        if w == "ca":
            mems.append(", ".join(units))
            units = []
            i += 1
            continue
        p1, i = item_at(t, i)
        if i < len(t) and t[i] == "ceva":
            i += 1
            if t[i] in NACA and i + 1 < len(t) and t[i + 1] == "ca":
                m = NACA[t[i]]
                px, i = item_at(t, i + 2)
                if m == 0:
                    p1 = f"{p1}, पर स्वयं {neg(px)}"
                else:
                    p1 = f"{p1} भी और {neg(neg(px))} भी"
            else:
                p2, i = item_at(t, i)
                p1 = f"{p1} भी और {p2} भी"
            if i < len(t) and t[i] == "ca":
                i += 1
        units.append(p1)
    if units:
        mems.append(", ".join(units))
    return mems


def join_and(xs):
    return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " और " + xs[-1]


def acc(s):
    return join_and([f"{m} {S.DHAMMA}" for m in members(s)])


def nom(s):
    ms = members(s)
    if len(ms) == 1:
        return f"{ms[0]} {S.DHAMMA}"
    return join_and(ms) + " " + S.DHAMMA_PL


def bare(s):
    return join_and(members(s))


def cond_abl(c):
    kind, k = S._classify(c)
    if kind == "abl":
        return S.ABL(k)
    if kind == "neg_abl":
        return S.NABL(k)
    raise Unknown(c)


def cond_ins(c):  # "ārammaṇapaccayena paccayo"
    m = re.match(r"^(na|no)?(\S+?)paccayena paccayo$", c)
    if not m or m.group(2) not in S.COND_BASE:
        raise Unknown(c)
    return S.INS(m.group(2))


DEP = {"paṭicca": S.DEP["paṭicca"], "paccayā": S.DEP["paccaya"]}

W = r"[^\s.…,;()]+"
G = rf"{W}(?: {W})*?"
OBJ = rf"(?:(?P<obj>{G}) dhammaṃ|(?P<objx>{G}dhammadhammaṃ))"
RX_PATICCA = re.compile(
    rf"{OBJ} (?P<dep>paṭicca|paccayā) "
    rf"(?:(?P<res>{G}) (?P<v>dhammo uppajjati|dhammā uppajjanti)|(?P<resx>{G}dhammadhammo) (?P<vx>uppajjati))"
    rf"(?: (?P<cond>{W}paccayā))?(?=[\s.…,;(]|$)")
RX_OBJDEPRES = re.compile(rf"{OBJ} (?P<dep>paṭicca|paccayā) (?P<res>{G})(?=…)")
RX_OBJDEP = re.compile(rf"{OBJ} (?P<dep>paṭicca|paccayā)(?=[….]|$)")
RX_PANHA = re.compile(
    rf"(?P<src>{G}) (?P<n>dhammo|dhammā) (?P<dst>{G}) dhammassa "
    rf"(?P<conds>{W}paccayena paccayo(?:, {W}paccayena paccayo)*)")


def tr_paticca(m):
    o = acc(m.group("obj") or m.group("objx"))
    r_src = m.group("res") or m.group("resx")
    r = nom(r_src)
    pl = m.group("v") == "dhammā uppajjanti"
    verb = "उत्पन्न होती हैं" if pl else "उत्पन्न होती है"
    c = m.group("cond")
    if c:
        return f"{o} {DEP[m.group('dep')]} {r} {cond_abl(c)} {verb}"
    return f"{o} {DEP[m.group('dep')]} {r} {verb}"


def tr_panha(m):
    src, dst = m.group("src"), m.group("dst")
    hoti = "होती है" if m.group("n") == "dhammo" else "होती हैं"
    conds = [cond_ins(c) for c in m.group("conds").split(", ")]
    return f"{nom(src)}, {acc(dst)} के लिए " + ", ".join(f"{c} {hoti}" for c in conds)


# =====================================================================================
# 2. Notes in parentheses and other fixed fragments
# =====================================================================================
NOTES = {}
FRAGS = {}

# ---- headings -------------------------------------------------------------------------
T, D, GO = S.TIKA, S.DUKA, S.GOCCHAKA
TN = {  # short triad names: "<X> वाला तीन का वर्गीकरण"
    "kusala": "हितकर", "vedanā": "अनुभूति", "vipāka": "कर्म-फल", "upādinna": "कर्म से उत्पन्न",
    "saṃkiliṭṭha": "क्लेशों से मलिन", "vitakka": "आरंभिक विचार", "pīti": "उल्लास",
    "dassana": "सत्य-दर्शन", "dassanahetu": "सत्य-दर्शन से छोड़े जाने वाले मूलों",
    "ācayagāmi": "संचय", "sekkha": "सीखने के चरण", "paritta": "सीमित",
    "parittārammaṇa": "सीमित विषय", "hīna": "हीन", "micchattaniyata": "ग़लत दिशा में निश्चित",
    "maggārammaṇa": "मार्ग को विषय बनाने", "uppanna": "उत्पन्न", "atīta": "अतीत",
    "atītārammaṇa": "अतीत के विषय", "ajjhatta": "स्वयं से संबंधित",
    "ajjhattārammaṇa": "स्वयं से संबंधित विषय", "sanidassana": "दिखाई देने",
}
DN = {  # dyad names: "<X> वाला दो का वर्गीकरण"
    "hetu": "मूल", "sahetuka": "मूल वाली परिघटनाओं", "hetusampayutta": "मूलों से जुड़ी परिघटनाओं",
    "hetusahetuka": "मूल रूपी और मूल वाली परिघटनाओं",
    "hetuhetusampayutta": "मूल रूपी और मूलों से जुड़ी परिघटनाओं",
    "nahetusahetuka": "मूल रूपी न होने वाली, पर मूल वाली परिघटनाओं",
    "sappaccaya": "कारणों पर निर्भर रहने वाली परिघटनाओं",
    "sanidassana": "दिखाई देने वाली परिघटनाओं", "sappaṭigha": "टकराव वाली परिघटनाओं",
    "rūpī": "भौतिक परिघटनाओं", "lokiya": "लौकिक परिघटनाओं",
    "kenaciviññeyya": "किसी एक प्रकार की चेतना से जानी जा सकने वाली परिघटनाओं",
    "āsava": "मन के मैल रूपी परिघटनाओं", "sāsava": "मन के मैलों का विषय बनने वाली परिघटनाओं",
    "āsavasampayutta": "मन के मैलों से जुड़ी परिघटनाओं",
    "āsavasāsava": "मन के मैल रूपी और मन के मैलों का विषय बनने वाली परिघटनाओं",
    "āsavaāsavasampayutta": "मन के मैल रूपी और मन के मैलों से जुड़ी परिघटनाओं",
    "āsavavippayuttasāsava": "मन के मैलों से अलग, पर उनका विषय बनने वाली परिघटनाओं",
    "saraṇa": "संघर्ष वाली परिघटनाओं", "dassanenapahātabba": "सत्य-दर्शन से छोड़ी जाने वाली परिघटनाओं",
    "kāmāvacara": "इंद्रिय-सुखों के लोक से संबंधित परिघटनाओं",
    "rūpāvacara": "सूक्ष्म भौतिक लोक से संबंधित परिघटनाओं",
    "arūpāvacara": "अभौतिक लोक से संबंधित परिघटनाओं",
    "pariyāpanna": "अस्तित्व के लोकों में समाई हुई परिघटनाओं",
    "niyyānika": "मुक्ति की ओर ले जाने वाली परिघटनाओं", "niyata": "निश्चित परिघटनाओं",
    "sauttara": "सर्वोच्च न होने वाली परिघटनाओं", "upādāna": "आसक्ति रूपी परिघटनाओं",
    "kilesa": "मन के क्लेश रूपी परिघटनाओं",
}
GN = {"hetu": "मूलों", "āsava": "मन के मैलों", "saññojana": "बंधनों", "upādāna": "आसक्ति",
      "kilesa": "मन के क्लेशों"}
CULA, MAHA, PITTHI = "बीच के छोटे दो-दो के वर्गीकरण", "बीच के बड़े दो-दो के वर्गीकरण", "अंतिम दो-दो के वर्गीकरण"
ADI = " आदि"
HEAD_PARTS = {}
for _k, _v in TN.items():
    HEAD_PARTS[f"{_k[0].upper()}{_k[1:]}ttikaṃ"] = T(_v)
    HEAD_PARTS[f"{_k}ttikaṃ"] = T(_v)
    HEAD_PARTS[f"{_k[0].upper()}{_k[1:]}ttika"] = T(_v)
    HEAD_PARTS[f"{_k}ttikādi"] = T(_v) + ADI
    HEAD_PARTS[f"{_k[0].upper()}{_k[1:]}ttikādi"] = T(_v) + ADI
    HEAD_PARTS[f"{_k[0].upper()}{_k[1:]}ādittikāni"] = T(_v) + ADI
for _k, _v in DN.items():
    for _cap in (_k, f"{_k[0].upper()}{_k[1:]}"):
        HEAD_PARTS[f"{_cap}dukaṃ"] = D(_v)
        HEAD_PARTS[f"{_cap}duka"] = D(_v)
        HEAD_PARTS[f"{_cap}dukādi"] = D(_v) + ADI
        HEAD_PARTS[f"{_cap}ādidukāni"] = D(_v) + ADI
for _k, _v in GN.items():
    for _cap in (_k, f"{_k[0].upper()}{_k[1:]}"):
        HEAD_PARTS[f"{_cap}gocchakaṃ"] = GO(_v)
        HEAD_PARTS[f"{_cap}gocchaka"] = GO(_v)
        HEAD_PARTS[f"{_cap}gocchakāni"] = GO(_v)
        HEAD_PARTS[f"{_cap}gocchakādi"] = GO(_v) + ADI
        HEAD_PARTS[f"{_cap}ādigocchakaṃ"] = GO(_v) + ADI
        HEAD_PARTS[f"{_cap}ādigocchakāni"] = GO(_v) + ADI
HEAD_PARTS.update({
    "Cūḷantaradukādi": CULA + ADI, "cūḷantaradukādi": CULA + ADI, "Cūḷantaradukāni": CULA,
    "cūḷantaradukāni": CULA, "cūḷantaradukaṃ": CULA, "Mahantaradukādi": MAHA + ADI,
    "mahantaradukādi": MAHA + ADI, "Mahantaradukāni": MAHA, "mahantaradukāni": MAHA,
    "mahantaradukaṃ": MAHA, "Mahantaraduka": MAHA, "Piṭṭhiduka": PITTHI, "Piṭṭhidukāni": PITTHI,
    "piṭṭhidukaṃ": PITTHI, "piṭṭhidukāni": PITTHI, "Piṭṭhidukādi": PITTHI + ADI,
    "Saññojanādichagocchakāni": "बंधनों का वर्ग आदि छह वर्ग",
    "saññojanādigocchakāni": GO("बंधनों") + ADI, "saññojanādigocchakaṃ": GO("बंधनों") + ADI,
    "Saññojanagocchakādi": GO("बंधनों") + ADI, "Upādānagocchakādi": GO("आसक्ति") + ADI,
    "upādānādidukāni": D("आसक्ति रूपी परिघटनाओं") + ADI, "Upādānadukādi": D("आसक्ति रूपी परिघटनाओं") + ADI,
    "kilesādidukāni": D("मन के क्लेश रूपी परिघटनाओं") + ADI,
    "Kilesadukādi": D("मन के क्लेश रूपी परिघटनाओं") + ADI,
    "Sappaccayadukādi": D("कारणों पर निर्भर रहने वाली परिघटनाओं") + ADI,
    "Kenaciviññeyyaduka": D(DN["kenaciviññeyya"]), "Rūpīduka": D(DN["rūpī"]),
    "Sahetukādidukāni": D(DN["sahetuka"]) + ADI, "hetusampayuttādidukāni": D(DN["hetusampayutta"]) + ADI,
    "hetusahetukādidukāni": D(DN["hetusahetuka"]) + ADI, "hetusahetukadukādi": D(DN["hetusahetuka"]) + ADI,
    "āsavādigocchakāni": GO("मन के मैलों") + ADI, "āsavagocchakādi": GO("मन के मैलों") + ADI,
    "Āsavagocchaka": GO("मन के मैलों"),
    "dassanenapahātabbadukādi": D(DN["dassanenapahātabba"]) + ADI,
    "Atītattikadvaya": "अतीत वाले दोनों तीन के वर्गीकरण",
    "Atītattikadvayaṃ": "अतीत वाले दोनों तीन के वर्गीकरण",
    "atītattikadvayaṃ": "अतीत वाले दोनों तीन के वर्गीकरण",
    "Ajjhattattikadvaya": "स्वयं से संबंधित वाले दोनों तीन के वर्गीकरण",
    "Ajjhattattikadvayaṃ": "स्वयं से संबंधित वाले दोनों तीन के वर्गीकरण",
    "ajjhattattikadvayaṃ": "स्वयं से संबंधित वाले दोनों तीन के वर्गीकरण",
    "Parittattikadvaya": "सीमित वाले दोनों तीन के वर्गीकरण",
    "Hīnādittikāni": T("हीन") + ADI, "Uppannādittikāni": T("उत्पन्न") + ADI,
    "Vitakkādittikāni": T("आरंभिक विचार") + ADI,
})
HEADINGS = {
    "Dhammānulomapaccanīye tikatikapaṭṭhānaṃ": f"{S.DHAMMANULOMAPACCANIYA}: {S.TIKATIKAPATTHANA}",
    "Dhammānulomapaccanīye dukadukapaṭṭhānaṃ": f"{S.DHAMMANULOMAPACCANIYA}: {S.DUKADUKAPATTHANA}",
    "Dhammapaccanīyānulome tikapaṭṭhānaṃ": f"{S.DHAMMAPACCANIYANULOMA}: {S.TIKAPATTHANA}",
    "Dhammapaccanīyānulome dukapaṭṭhānaṃ": f"{S.DHAMMAPACCANIYANULOMA}: {S.DUKAPATTHANA}",
    "Dhammapaccanīyānulome dukatikapaṭṭhānaṃ": f"{S.DHAMMAPACCANIYANULOMA}: {S.DUKATIKAPATTHANA}",
    "Dhammapaccanīyānulome tikadukapaṭṭhānaṃ": f"{S.DHAMMAPACCANIYANULOMA}: {S.TIKADUKAPATTHANA}",
    "Dhammapaccanīyānulome tikatikapaṭṭhānaṃ": f"{S.DHAMMAPACCANIYANULOMA}: {S.TIKATIKAPATTHANA}",
    "Dhammapaccanīyānulome dukadukapaṭṭhānaṃ": f"{S.DHAMMAPACCANIYANULOMA}: {S.DUKADUKAPATTHANA}",
    "Paccanīyaṃ": S.PACCANIYA, "Paccayacatukkaṃ": "कारणों के चार क्रम",
    "Hetu-ārammaṇapaccayā": f"{S.NAME('hetu')} और {S.NAME('ārammaṇa')}",
    "Hetu-anantarapaccayā": f"{S.NAME('hetu')} और {S.NAME('anantara')}",
    "Nahetu-naārammaṇapaccayā": f"{S.NNAME('hetu')} और {S.NNAME('ārammaṇa')}",
    "Nahetunaārammaṇapaccayādi": f"{S.NNAME('hetu')}, {S.NNAME('ārammaṇa')} आदि",
    "Hetuārammaṇapaccayādi": f"{S.NAME('hetu')}, {S.NAME('ārammaṇa')} आदि",
    "Hetupaccayo": S.NAME("hetu"), "Nahetupaccayo": S.NNAME("hetu"),
    "Ārammaṇapaccayo": S.NAME("ārammaṇa"),
    "Paccanīyuddhāro": "नकारात्मक क्रम के लिए चयन",
    "Pañhāvāro": S.VARA["pañhā"], "Paṭiccavārādi": S.VARA["paṭicca"] + ADI,
    "Paccayavārādi": S.VARA["paccaya"] + ADI,
    "Akusalapadaṃ": "हानिकर पद", "Abyākatapadaṃ": "नैतिक रूप से अनिर्धारित पद",
    "Anuttarapadaṃ": "सर्वोच्च पद",
    "Hetugocchakaṃ": GO("मूलों"), "Āsavagocchakaṃ": GO("मन के मैलों"),
    "Upādānagocchakaṃ": GO("आसक्ति"), "Kilesagocchakaṃ": GO("मन के क्लेशों"),
    "Piṭṭhidukaṃ": PITTHI, "Mahantaradukādi": MAHA + ADI, "Cūḷantaradukādi": CULA + ADI,
    "Saññojanādichagocchakāni": "बंधनों का वर्ग आदि छह वर्ग",
    "Parittattikādi": T("सीमित") + ADI,
}

# ---- notes in parentheses and fixed fragments -------------------------------------------
SKH = "संक्षिप्त"                       # saṃkhittaṃ
VIT = "का विस्तार करना चाहिए"            # vitthāretabbaṃ
SAMA = "के समान है"                     # -sadisaṃ
MULA = "वाले आरंभ-बिंदु"                 # -mūla (the starting item of a series)
GAN = "गणना के अनुसार"                   # gaṇitakena
PANHA_W = "प्रश्न"                        # pañhā


def VARA_OBL(k):  # "सह-उत्पत्ति का खंड" -> "सह-उत्पत्ति के खंड"
    return S.VARA[k].replace(" का खंड", " के खंड")


def mula(pali_items):  # "Nahetunaanidassanasappaṭigha-mūla" -> "<items> परिघटना वाले आरंभ-बिंदु"
    return f"{bare(pali_items)} {S.DHAMMA} {MULA}"


def dsadisa(k):  # "<X>dukasadisaṃ"
    return f"{D(DN[k]).replace('वाला दो का', 'वाले दो के')} {SAMA}"


SIX = ["sahajāta", "paccaya", "nissaya", "saṃsaṭṭha", "sampayutta"]
VARAMPI_SADISA = ", ".join(f"{S.VARA[k]} भी" for k in SIX) + f" {VARA_OBL('paṭicca')} {SAMA}"
VARAMPI_VIT = ", ".join(f"{VARA_OBL(k)} का भी" for k in SIX)
YATHA_KUSALATTIKE = (f"जैसे हितकर वाले तीन के वर्गीकरण में प्रश्नों के खंड का {S.ANULOMA} भी, {S.PACCANIYA} भी, "
                     f"{S.ANULOMAPACCANIYA} भी, {S.PACCANIYANULOMA} भी गिना गया है, वैसे ही गिनना चाहिए।")

NOTES.update({
    "Saṃkhittaṃ.": f"{SKH}।", "saṃkhittaṃ.": f"{SKH}।", "saṃkhittaṃ": SKH,
    "Sahajātavārampi paccayavārampi nissayavārampi saṃsaṭṭhavārampi sampayuttavārampi paṭiccavārasadisaṃ.":
        VARAMPI_SADISA + "।",
    "Sahajātavārampi…pe… sampayuttavārampi paṭiccavārasadisaṃ.":
        f"{S.VARA['sahajāta']} भी… {S.VARA['sampayutta']} भी {VARA_OBL('paṭicca')} {SAMA}।",
    "Sahajātavāro paṭiccavārasadiso": f"{S.VARA['sahajāta']} {VARA_OBL('paṭicca')} {SAMA}",
    "Pañhāvārampi vitthāretabbaṃ.": f"{VARA_OBL('pañhā')} का भी विस्तार करना चाहिए।",
    "Sahajātavārampi…pe… pañhāvārampi vitthāretabbaṃ.":
        f"{VARA_OBL('sahajāta')} का भी… {VARA_OBL('pañhā')} का भी विस्तार करना चाहिए।",
    "Pañhāvāraṃ vitthāretabbaṃ.": f"{VARA_OBL('pañhā')} {VIT}।",
    "Sahajātavārampi paccayavārampi nissayavārampi saṃsaṭṭhavārampi sampayuttavārampi vitthāretabbaṃ.":
        VARAMPI_VIT + " विस्तार करना चाहिए।",
    "Sahajātavārampi paccayavārampi nissayavārampi saṃsaṭṭhavārampi sampayuttavārampi pañhāvārampi vitthāretabbaṃ.":
        VARAMPI_VIT + f", {VARA_OBL('pañhā')} का भी विस्तार करना चाहिए।",
    "Sahajātavārampi paṭiccavārasadisaṃ vitthāretabbaṃ.":
        f"{VARA_OBL('sahajāta')} का भी {VARA_OBL('paṭicca')} के समान विस्तार करना चाहिए।",
    "Yathā kusalattike pañhāvārassa anulomampi paccanīyampi anulomapaccanīyampi paccanīyānulomampi gaṇitaṃ, evaṃ gaṇetabbaṃ.":
        YATHA_KUSALATTIKE,
    "Yathā kusalattike pañhāvāraṃ evaṃ vitthāretabbaṃ.":
        f"जैसे हितकर वाले तीन के वर्गीकरण में {S.VARA['pañhā']} है, वैसे ही विस्तार करना चाहिए।",
    "Kusale pañca, akusale pañca, abyākate tīṇi.":
        f"{S.T['k']} में पाँच, {S.T['a']} में पाँच, {S.T['ab']} में तीन।",
    "Dve mūlāni.": "दो आरंभ-बिंदु।",
    "Uppādī anuppannasadisaṃ.": f"{nom('uppādī')}, {nom('anuppanno')} {SAMA}।",
    "Anāgataṃ atītasadisaṃ.": f"{nom('anāgato')}, {nom('atīto')} {SAMA}।",
    "Tīṇi veditakaṃ kātabbaṃ.": "अनुभूति से संबंधित तीन बनाने चाहिए।",
    "Ekavīsati pañhā.": f"इक्कीस {PANHA_W}।",
    "Dukkhāya vedanāya sampayuttaabyākatamūlaṃ adukkhamasukhāya vedanāya sampayuttaabyākatamūlampi kātabbaṃ.":
        f"{mula('dukkhāya vedanāya sampayutta abyākata')} और "
        f"{mula('adukkhamasukhāya vedanāya sampayutta abyākata')} भी बनाने चाहिए।",
    "Vedanāttikasadisaṃ. Saṃkhittaṃ.": f"अनुभूति वाले तीन के वर्गीकरण {SAMA}। {SKH}।",
    "Sahetukasadisaṃ.": f"{nom('sahetuko')} {SAMA}।",
    "Ahetukasadisaṃ, saṃkhittaṃ.": f"{nom('ahetuko')} {SAMA}, {SKH}।",
    "Asaṅkhataṃ appaccayasadisaṃ.": f"{nom('asaṅkhato')}, {nom('appaccayo')} {SAMA}।",
    "Lokiyasadisaṃ.": f"{nom('lokiyo')} {SAMA}।",
    "saṃkhittaṃ. Nayavasena vitthāretabbaṃ": f"{SKH}। विधि के अनुसार विस्तार करना चाहिए",
    "Saṅkhataṃ sappaccayasadisaṃ": f"{nom('saṅkhato')}, {nom('sappaccayo')} {SAMA}",
    "Saṅkhataṃ sappaccayasadisaṃ.": f"{nom('saṅkhato')}, {nom('sappaccayo')} {SAMA}।",
    "sabbattha pañca.": "हर जगह पाँच।",
    "Lokiyadukasadisaṃ.": dsadisa("lokiya") + "।",
    "Sabbattha pañhe saṃkhittaṃ.": f"हर जगह {PANHA_W} {SKH} हैं।",
    "Sahetukadukasadisaṃ.": dsadisa("sahetuka") + "।",
    "Hetusahetukadukasadisaṃ.": dsadisa("hetusahetuka") + "।",
    "sappaccayadukasadisaṃ": dsadisa("sappaccaya"),
    "Etena upāyena sabbattha vitthāretabbaṃ.": "इसी उपाय से हर जगह विस्तार करना चाहिए।",
    "Sabbattha vitthāro": "हर जगह विस्तार",
    "Sabbattha nava pañhā.": f"हर जगह नौ {PANHA_W}।",
    "saṃkhittaṃ, nava pañhā": f"{SKH}, नौ {PANHA_W}",
    "Nava pañhā.": f"नौ {PANHA_W}।",
    "saṃkhittaṃ, nava pañhā kātabbā": f"{SKH}, नौ {PANHA_W} बनाने चाहिए",
    "Nava pañhā kātabbā.": f"नौ {PANHA_W} बनाने चाहिए।",
    "Nava pañhā kātabbā": f"नौ {PANHA_W} बनाने चाहिए",
    "Cha pañhā kātabbā.": f"छह {PANHA_W} बनाने चाहिए।",
    "Sabbattha nava.": "हर जगह नौ।",
    "gaṇitakena tīṇi.": f"{GAN} तीन।",
    "Sabbattha tīṇi.": "हर जगह तीन।",
    "Sabbattha saṃkhittaṃ.": f"हर जगह {SKH}।",
    "Dukamūlakaṃ ekaṃ.": "दो के वर्गीकरण वाले आरंभ-बिंदु से एक।",
    "Dukamūlaṃ ekaṃ saṃkhittaṃ, sabbattha tīṇi.": f"दो के वर्गीकरण वाला एक आरंभ-बिंदु {SKH} है, हर जगह तीन।",
    "Āsavaāsavasampayuttadukaṃ natthi.": f"{D(DN['āsavaāsavasampayutta'])} नहीं है।",
    "Āsavaāsavasampayuttaduke pañhā na labbhati.":
        f"{D(DN['āsavaāsavasampayutta']).replace('वाला दो का', 'वाले दो के')} में {PANHA_W} नहीं मिलते।",
    "Naakusale tīṇi. Naabyākate tīṇi. Saṃkhittaṃ.":
        f"{nom('naakusalo')} में तीन। {nom('naabyākato')} में तीन। {SKH}।",
    "Nava pañhā saṃkhittaṃ.": f"नौ {PANHA_W} {SKH}।",
    "Ajjhattattiko na labbhati paṭiccavārādīsu.":
        f"{VARA_OBL('paṭicca')} आदि में {T(TN['ajjhatta'])} नहीं मिलता।",
    "Ajjhattabahiddhārammaṇaṃ natthi.": "स्वयं और दूसरों दोनों से संबंधित विषय वाली परिघटना नहीं है।",
    "Nahetunaanidassanasappaṭighamūlepi tīṇiyeva.": f"{mula('nahetu naanidassanasappaṭigha')} में भी तीन ही।",
    "Nasahetukanaanidassanasappaṭighamūlepi tīṇiyeva.":
        f"{mula('nasahetuka naanidassanasappaṭigha')} में भी तीन ही।",
    "Nahetusampayuttaṃ nasanidassanasappaṭighaṃ sahetukadukasadisaṃ. Tīṇi pañhā. Hetusahetukaduke ca hetuhetusampayuttaduke ca pañhā no labbhati.":
        f"{nom('nahetusampayuttaṃ nasanidassanasappaṭighaṃ')} {dsadisa('sahetuka')}। तीन {PANHA_W}। "
        f"{D(DN['hetusahetuka']).replace('वाला दो का', 'वाले दो के')} में और "
        f"{D(DN['hetuhetusampayutta']).replace('वाला दो का', 'वाले दो के')} में {PANHA_W} नहीं मिलते।",
    "Naappaccayanaanidassanaappaṭighamūlepi ekameva.": f"{mula('naappaccaya naanidassanaappaṭigha')} में भी एक ही।",
    "Nasaṅkhataṃ nasappaccayasadisaṃ.": f"{nom('nasaṅkhato')}, {nom('nasappaccayo')} {SAMA}।",
    "Gaṇitakena gaṇetabbā tīṇi pañhā.": f"{GAN} तीन {PANHA_W} गिनने चाहिए।",
    "tīṇiyeva pañhā kātabbā": f"तीन ही {PANHA_W} बनाने चाहिए",
    "purimanayena tīṇi pañhā": f"पहले की विधि से तीन {PANHA_W}",
    "Nasāsavaṃ naanidassanasappaṭighamūlassa purimanayena tīṇi pañhā.":
        f"{mula('nasāsava naanidassanasappaṭigha')} के लिए पहले की विधि से तीन {PANHA_W}।",
    "Naāsavasampayuttanaanidassanasappaṭighamūle tīṇiyeva.":
        f"{mula('naāsavasampayutta naanidassanasappaṭigha')} में तीन ही।",
    "Naāsavañceva naanāsavaṃ naanidassanasappaṭighamūlepi purimanayena tīṇiyeva.":
        f"{mula('naāsavañceva naanāsavaṃ naanidassanasappaṭigha')} में भी पहले की विधि से तीन ही।",
    "Āsavavippayuttanasāsavanaanidassanasappaṭighamūlepi purimanayeneva tīṇi pañhā.":
        f"{mula('āsavavippayutta nasāsava naanidassanasappaṭigha')} में भी पहले की विधि से ही तीन {PANHA_W}।",
    "Tīṇi pañhā.": f"तीन {PANHA_W}।",
    "Anidassanasappaṭighe tīṇiyeva.": f"{nom('anidassanasappaṭigho')} में तीन ही।",
    "Cittasamuṭṭhānarūpeneva tīṇi, saṃkhittaṃ.": f"{S.CSR} के साथ ही तीन, {SKH}।",
    "Naakusale dve, naabyākate dve. Paṭhamaṃ gaṇitakena ekaṃ, dutiyaṃ gaṇitakena ekaṃ, tatiyaṃ gaṇitakena ekaṃ, sabbattha nava pañhā.":
        f"{nom('naakusalo')} में दो, {nom('naabyākato')} में दो। {GAN} पहले में एक, {GAN} दूसरे में एक, "
        f"{GAN} तीसरे में एक, हर जगह नौ {PANHA_W}।",
    "Gaṇitakena tīṇi pañhā.": f"{GAN} तीन {PANHA_W}।",
    "Akusalamūle dve, dukamūle dve.": f"{S.T['a']} {MULA} में दो, दो के वर्गीकरण {MULA} में दो।",
    "apariyāpannasadisaṃ cha pañhā": f"{nom('apariyāpanno')} के समान, छह {PANHA_W}",
    "dutiyaṃ gaṇitakena tīṇi": f"{GAN} दूसरे में तीन",
    "dve pañhāyeva": f"दो ही {PANHA_W}",
    "dveyeva. Paṭhamaṃ gaṇitakena ekaṃ, dutiyaṃ gaṇitakena ekaṃ, tatiyaṃ gaṇitakena ekaṃ kātabbaṃ.":
        f"दो ही। {GAN} पहले में एक, {GAN} दूसरे में एक, {GAN} तीसरे में एक बनाना चाहिए।",
    "Nahetu nanahetu ovattā, tīṇi mūlāni, ekavīsati pañhā kātabbā.":
        f"{bare('nahetu')} और {bare('nanahetu')} उलट दी गई हैं, तीन आरंभ-बिंदु, इक्कीस {PANHA_W} बनाने चाहिए।",
    "Akusalāneva tīṇi.": f"{S.T['a']} वाले ही तीन।",
    "Cattāri gaṇitakena dve dve pañhā kātabbā.": f"चार, {GAN} दो-दो {PANHA_W} बनाने चाहिए।",
    "Naakusalaṃ naabyākataṃ natthi.": f"{nom('naakusalaṃ naabyākataṃ')} नहीं है।",
    "Atītattikaṃ uppannattikasadisaṃ.": f"{T(TN['atīta'])} {T(TN['uppanna']).replace('वाला तीन का', 'वाले तीन के')} {SAMA}।",
    "Naanidassanasappaṭighanaabyākatamūlāni sattameva, dukamūlāni sattameva, sabbaṃ ekavīsatimeva.":
        f"{mula('naanidassanasappaṭigha naabyākata')} सात ही, दो के वर्गीकरण {MULA} सात ही, सब मिलाकर इक्कीस ही।",
    "Antimadukaṃ na labbhati.": "अंतिम दो का वर्गीकरण नहीं मिलता।",
    "Hetuhetusampayuttadukaṃ saṃkhittaṃ.": f"{D(DN['hetuhetusampayutta'])} {SKH} है।",
})

DH_AP = S.DHAMMANULOMAPACCANIYA
DH_PA = S.DHAMMAPACCANIYANULOMA
FRAGS.update({
    "Akusale tīṇi": f"{S.T['a']} में तीन",
    "Abyākataṃ anupādinnupādāniye tīṇiyeva": f"{bare('abyākata anupādinnupādāniya')} {S.DHAMMA} में तीन ही",
    "Saṃsaṭṭhavāre": VARA_OBL("saṃsaṭṭha") + " में",
    "Akusalaṃ ekaṃ khandhaṃ paṭicca tayo khandhā": S.KH13(S.KH_FIRST["a"]),
    "dve khandhe paṭicca dve khandhā": "दो समूहों पर निर्भर होकर दो समूह",
    "Vipākābyākataṃ kiriyābyākataṃ ekaṃ khandhaṃ paṭicca tayo khandhā cittasamuṭṭhānañca rūpaṃ":
        f"{S.KH13(S.KH_FIRST['vk'])} {S.AND_CSR}",
    "{hetuyā aṭṭha?}": "[पाठभेद: hetuyā aṭṭha?]",
    "Nahetu nadukkhāya vedanāya sampayuttamūlaṃ tīṇiyeva":
        f"{mula('nahetu nadukkhāya vedanāya sampayutta')} में तीन ही",
    "Gaṇitakena tīṇi pañhā": f"{GAN} तीन {PANHA_W}",
    "Gaṇitakena tīṇi": f"{GAN} तीन", "gaṇitakena tīṇi": f"{GAN} तीन",
    "pañhā": PANHA_W,
    "Nakenaci viññeyyaṃ naanidassanasappaṭighassa purimasadisaṃ navapañhaṃ kātabbaṃ":
        f"{acc('nakenaci viññeyyaṃ naanidassanasappaṭighaṃ')} के लिए पहले के समान नौ {PANHA_W} बनाने चाहिए",
    "Nakenaci viññeyyaṃ naanidassanaappaṭighamūlassa navapañhameva":
        f"{mula('nakenaci viññeyya naanidassanaappaṭigha')} के लिए नौ {PANHA_W} ही",
    "Dhammānulomapaccanīye tikatikapaṭṭhānaṃ niṭṭhitaṃ": f"{DH_AP}: {S.TIKATIKAPATTHANA} समाप्त",
    "Dhammānulomapaccanīye dukadukapaṭṭhānaṃ niṭṭhitaṃ": f"{DH_AP}: {S.DUKADUKAPATTHANA} समाप्त",
    "Anulomapaccanīyapaṭṭhānaṃ niṭṭhitaṃ": f"{S.ANULOMAPACCANIYA} के कारण-संबंध समाप्त",
    "Dhammapaccanīyānulome tikapaṭṭhānaṃ niṭṭhitaṃ": f"{DH_PA}: {S.TIKAPATTHANA} समाप्त",
    "Dhammapaccanīyānulome dukapaṭṭhānaṃ niṭṭhitaṃ": f"{DH_PA}: {S.DUKAPATTHANA} समाप्त",
    "Dhammapaccanīyānulome dukatikapaṭṭhānaṃ niṭṭhitaṃ": f"{DH_PA}: {S.DUKATIKAPATTHANA} समाप्त",
    "Dhammapaccanīyānulome tikadukapaṭṭhānaṃ niṭṭhitaṃ": f"{DH_PA}: {S.TIKADUKAPATTHANA} समाप्त",
    "Dhammapaccanīyānulome tikatikapaṭṭhānaṃ niṭṭhitaṃ": f"{DH_PA}: {S.TIKATIKAPATTHANA} समाप्त",
    "Dhammapaccanīyānulome dukadukapaṭṭhānaṃ niṭṭhitaṃ": f"{DH_PA}: {S.DUKADUKAPATTHANA} समाप्त",
    "Paccanīyānulomapaṭṭhānaṃ niṭṭhitaṃ": f"{S.PACCANIYANULOMA} के कारण-संबंध समाप्त",
    "Anulomadukatikapaṭṭhānato paṭṭhāya yāva pariyosānā tiṃsamattehi bhāṇavārehi paṭṭhānaṃ":
        f"{S.ANULOMA} में {S.DUKATIKAPATTHANA} से लेकर अंत तक, “{S.BOOK_TITLE}” लगभग तीस पाठ-खंडों का है",
    "Paṭṭhānapakaraṇaṃ niṭṭhitaṃ": f"“{S.BOOK_TITLE}” ग्रंथ समाप्त",
})
FRAG_KEYS = sorted(FRAGS, key=len, reverse=True)


def lc(s):
    return s[0].lower() + s[1:] if s else s


def count_run(text, p):
    """Longest counting run from p (ablatives, locatives, numbers, …pe…, commas, final '.')."""
    q, last = p, None
    while q < len(text):
        rest = text[q:]
        if rest.startswith(" "):
            q += 1
            continue
        if rest.startswith("…pe…"):
            q += len("…pe…")
            last = q
            continue
        if rest.startswith("…") or rest.startswith(","):
            q += 1
            last = q
            continue
        m = re.match(W, rest)
        if m and S._classify(m.group(0))[0] != "other":
            q += m.end()
            last = q
            continue
        break
    if last is None:
        return None
    seg = text[p:last]
    if not re.search(r"[^\s…,]", seg) or not any(
            S._classify(w)[0] != "other" for w in re.findall(W, seg)):
        return None
    if last < len(text) and text[last] == ".":
        last += 1
    return last


def tr_text(text):
    out, p = [], 0
    while p < len(text):
        rest = text[p:]
        if rest[0] == " ":
            out.append(" ")
            p += 1
            continue
        m = re.match(r"\((\d+)\)", rest)
        if m:
            out.append(m.group(0))
            p += m.end()
            continue
        m = re.match(r"\(([^()]*)\)", rest)
        if m:
            inner = m.group(1)
            if inner not in NOTES:
                raise Unknown("NOTE: " + inner)
            out.append(f"({NOTES[inner]})")
            p += m.end()
            continue
        if rest.startswith("…pe…"):
            out.append("…")
            p += len("…pe…")
            continue
        if rest[0] == "…":
            out.append("…")
            p += 1
            continue
        if rest[0] == ".":
            out.append("।")
            p += 1
            continue
        if rest[0] in ",;":
            out.append(rest[0])
            p += 1
            continue
        hit = next((k for k in FRAG_KEYS if rest.startswith(k)), None)
        if hit:
            out.append(FRAGS[hit])
            p += len(hit)
            continue
        low = lc(rest)
        m = RX_PATICCA.match(low)
        if m:
            out.append(tr_paticca(m))
            p += m.end()
            continue
        m = RX_PANHA.match(low)
        if m:
            out.append(tr_panha(m))
            p += m.end()
            continue
        m = RX_OBJDEPRES.match(low)
        if m:
            out.append(f"{acc(m.group('obj') or m.group('objx'))} {DEP[m.group('dep')]} {bare(m.group('res'))}")
            p += m.end()
            continue
        m = RX_OBJDEP.match(low)
        if m:
            out.append(f"{acc(m.group('obj') or m.group('objx'))} {DEP[m.group('dep')]}")
            p += m.end()
            continue
        m = re.match(rf"({W}paccayena paccayo)", low)
        if m:
            out.append(f"{cond_ins(m.group(1))} होती है")
            p += m.end()
            continue
        m = re.match(rf"(?P<src>{G}) (?P<n>dhammo|dhammā)(?=[….]|$)", low)
        if m:
            out.append(nom(m.group("src")))
            p += m.end()
            continue
        e = count_run(text, p)
        if e:
            out.append(S.count_hi(text[p:e]))
            p = e
            continue
        m = re.match(rf"{G}(?=[….]|$)", low)
        if m:
            try:
                out.append(bare(m.group(0)))
                p += m.end()
                continue
            except Unknown:
                pass
        raise Unknown(rest)
    s = "".join(out)
    return s


def tr_heading(line):
    hashes, body = re.match(r"^(#+) (.*)$", line).groups()
    if body in HEADINGS:
        return f"{hashes} {HEADINGS[body]}"
    m = re.match(r"^([\d-]+\.) (.+)$", body)
    num, name = (m.group(1) + " ", m.group(2)) if m else ("", body)
    if name in HEADINGS:
        return f"{hashes} {num}{HEADINGS[name]}"
    parts = name.split("-")
    hi = []
    for part in parts:
        if part not in HEAD_PARTS:
            raise Unknown("HEAD: " + part)
        hi.append(HEAD_PARTS[part])
    return f"{hashes} {num}" + " और ".join(hi)


def build(name, errors):
    pali_path = S.PALI_DIR / f"{name}.md"
    text = pali_path.read_text(encoding="utf-8")
    lines = []
    for line in S.nonempty(text):
        body = S.ID_RX.sub("", line)
        try:
            if body.startswith("#"):
                lines.append(tr_heading(body))
            else:
                lines.append(tr_text(body))
        except Unknown as e:
            errors.append(f"{name}: {e}")
            lines.append("# " * 0 + "XX" if not body.startswith("#") else body)
    return S.assemble(text, lines)


def main():
    dry = "--dry" in sys.argv
    errors = []
    outs = {n: build(n, errors) for n in FILES}
    seen = set()
    for e in errors:
        if e not in seen:
            print(e)
            seen.add(e)
    print("errors:", len(errors))
    if dry or errors:
        return
    for n, t in outs.items():
        (S.HI_DIR / f"{n}.md").write_text(t, encoding="utf-8", newline="\n")
        print("wrote", n)


if __name__ == "__main__":
    main()
