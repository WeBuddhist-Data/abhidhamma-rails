"""Hindi builder for pi-7 4-02..4-07 (dukatika: hetu, sahetuka.., sappaccaya.., āsava, saññojana, gantha dyads
with the kusala / other triads). Composes every line from fixed frames (build_sample_hi) and item tables.

    python -I -B -X utf8 build_4-02_4-07_hi.py            # write all six files
    python -I -B -X utf8 build_4-02_4-07_hi.py --dry      # parse only, report problems
"""
import pathlib
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi")
import build_sample_hi as S  # noqa: E402

FILES = ["4-02-dukatika-hetuduka.md", "4-03-dukatika-sahetukaduka.md", "4-04-dukatika-sappaccayaduka.md",
         "4-05-dukatika-asavaduka.md", "4-06-dukatika-sannojanaduka.md", "4-07-dukatika-ganthaduka.md"]

DH, DH_PL = S.DHAMMA, S.DHAMMA_PL   # परिघटना / परिघटनाएँ

# =====================================================================================
# 1. Item labels (pi-1 1-matika.md, singular adjectival form before परिघटना)
# =====================================================================================
TIKA_ITEM = {
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
    "dassanena pahātabba": "सत्य-दर्शन से छोड़ी जाने वाली",
    "bhāvanāya pahātabba": "मानसिक अभ्यास से छोड़ी जाने वाली",
    "nevadassanena nabhāvanāya pahātabba": "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़ी जाने वाली",
    "dassanena pahātabbahetuka": "सत्य-दर्शन से छोड़े जाने वाले मूलों वाली",
    "bhāvanāya pahātabbahetuka": "मानसिक अभ्यास से छोड़े जाने वाले मूलों वाली",
    "nevadassanena nabhāvanāya pahātabbahetuka": "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़े जाने वाले मूलों वाली",
    "ācayagāmi": "संचय की ओर ले जाने वाली", "apacayagāmi": "संचय घटाने की ओर ले जाने वाली",
    "nevācayagāmināpacayagāmi": "न संचय की ओर, न संचय घटाने की ओर ले जाने वाली",
    "sekkha": "सीखने के चरण की", "asekkha": "सीखना पूरा होने के चरण की",
    "nevasekkhanāsekkha": "न सीखने के चरण की, न सीखना पूरा होने के चरण की",
    "paritta": "सीमित", "mahaggata": "उन्नत", "appamāṇa": "अपरिमित",
    "parittārammaṇa": "सीमित विषय वाली", "mahaggatārammaṇa": "उन्नत विषय वाली",
    "appamāṇārammaṇa": "अपरिमित विषय वाली",
    "hīna": "हीन", "majjhima": "मध्यम", "paṇīta": "उत्तम",
    "micchattaniyata": "ग़लत दिशा में निश्चित", "sammattaniyata": "सही दिशा में निश्चित", "aniyata": "अनिश्चित",
    "maggārammaṇa": "मार्ग को विषय बनाने वाली", "maggahetuka": "मार्ग को मूल बनाने वाली",
    "maggādhipati": "मार्ग की प्रधानता वाली",
    "uppanna": "उत्पन्न हो चुकी", "anuppanna": "उत्पन्न न हुई", "uppādi": "उत्पन्न होने वाली",
    "atīta": "अतीत की", "anāgata": "भविष्य की", "paccuppanna": "वर्तमान की",
    "atītārammaṇa": "अतीत के विषय वाली", "anāgatārammaṇa": "भविष्य के विषय वाली",
    "paccuppannārammaṇa": "वर्तमान के विषय वाली",
    "ajjhatta": "स्वयं से संबंधित", "bahiddhā": "दूसरों से संबंधित",
    "ajjhattārammaṇa": "स्वयं से संबंधित विषय वाली", "bahiddhārammaṇa": "दूसरों से संबंधित विषय वाली",
    "sanidassanasappaṭigha": "दिखाई देने वाली और टकराव वाली",
    "anidassanasappaṭigha": "दिखाई न देने वाली, पर टकराव वाली",
    "anidassanaappaṭigha": "दिखाई न देने वाली और टकराव से रहित",
}
TIKA_KEYS = sorted(TIKA_ITEM, key=lambda k: -len(k.split()))


def _gocchaka_dukas(base, noun, noun_pl, ya, a_ya, sampayutta_word, vippayutta_word, neg="no"):
    """Dyads of one gocchaka (āsava / saññojana / gantha), as in pi-1 1-matika.md."""
    rupi = f"{noun} रूपी"
    rupi_na = f"{noun} रूपी न होने वाली"
    visaya = f"{noun_pl} का विषय बनने वाली"
    visaya_na = f"{noun_pl} का विषय न बनने वाली"
    samp = f"{noun_pl} से जुड़ी"
    vipp = f"{noun_pl} से अलग"
    return {
        base: rupi, f"{neg}{base}": rupi_na,
        ya: visaya, a_ya: visaya_na,
        sampayutta_word: samp, vippayutta_word: vipp,
        f"{base} ceva {ya} ca": f"{rupi} भी और {visaya} भी",
        f"{base} ceva {ya}": f"{rupi} भी और {visaya} भी",        # source slip: "ca" missing
        f"{ya} ceva {neg} ca {base}": f"{visaya}, पर स्वयं {rupi_na}",
        f"{base} ceva {sampayutta_word} ca": f"{rupi} भी और {samp} भी",
        f"{base} ceva {sampayutta_word}": f"{rupi} भी और {samp} भी",  # source slip: "ca" missing
        f"{sampayutta_word} ceva {neg} ca {base}": f"{samp}, पर स्वयं {rupi_na}",
        f"{vippayutta_word} {ya}": f"{vipp}, पर उनका विषय बनने वाली",
        f"{vippayutta_word} {a_ya}": f"{vipp} और उनका विषय न बनने वाली",
    }


DUKA_ITEM = {
    "hetu": "मूल रूपी", "nahetu": "मूल रूपी न होने वाली",
    "sahetuka": "मूल वाली", "ahetuka": "मूल से रहित",
    "hetusampayutta": "मूलों से जुड़ी", "hetuvippayutta": "मूलों से अलग",
    "hetu ceva sahetuka ca": "मूल रूपी भी और मूल वाली भी",
    "sahetuka ceva na ca hetu": "मूल वाली, पर स्वयं मूल रूपी न होने वाली",
    "hetu ceva hetusampayutta ca": "मूल रूपी भी और मूलों से जुड़ी भी",
    "hetusampayutta ceva na ca hetu": "मूलों से जुड़ी, पर स्वयं मूल रूपी न होने वाली",
    "nahetu sahetuka": "मूल रूपी न होने वाली, पर मूल वाली",
    "nahetu ahetuka": "मूल रूपी न होने वाली और मूल से रहित",
    "sappaccaya": "कारणों पर निर्भर रहने वाली", "appaccaya": "कारणों पर निर्भर न रहने वाली",
    "saṅkhata": "निर्मित", "asaṅkhata": "अनिर्मित",
    "sanidassana": "दिखाई देने वाली", "anidassana": "दिखाई न देने वाली",
    "sappaṭigha": "टकराव वाली", "appaṭigha": "टकराव से रहित",
    "rūpi": "भौतिक", "arūpi": "अभौतिक", "lokiya": "लौकिक", "lokuttara": "लोकोत्तर",
    "kenaci viññeyya": "किसी एक प्रकार की चेतना से जानी जा सकने वाली",
    "kenaci na viññeyya": "किसी एक प्रकार की चेतना से न जानी जा सकने वाली",
}
DUKA_ITEM.update(_gocchaka_dukas("āsava", "मन के मैल", "मन के मैलों", "sāsava", "anāsava", "āsavasampayutta",
                                 "āsavavippayutta"))
DUKA_ITEM.update(_gocchaka_dukas("saññojana", "बंधन", "बंधनों", "saññojaniya", "asaññojaniya",
                                 "saññojanasampayutta", "saññojanavippayutta"))
DUKA_ITEM.update(_gocchaka_dukas("gantha", "गाँठ", "गाँठों", "ganthaniya", "aganthaniya", "ganthasampayutta",
                                 "ganthavippayutta"))
assert DUKA_ITEM["anāsava"] == "मन के मैलों का विषय न बनने वाली"
assert DUKA_ITEM["asaññojaniya"] == "बंधनों का विषय न बनने वाली"
assert DUKA_ITEM["aganthaniya"] == "गाँठों का विषय न बनने वाली"

KEEP = {"ca", "ceva", "na", "no", "kenaci", "sukhāya", "dukkhāya", "adukkhamasukhāya", "vedanāya", "dassanena",
        "bhāvanāya", "nevadassanena", "nabhāvanāya", "bahiddhā"}
LEMMAS = set()
for _k in list(TIKA_ITEM) + list(DUKA_ITEM) + ["dhamma"]:
    LEMMAS.update(w for w in _k.split() if w not in KEEP)
ENDINGS = [("assa", "a"), ("ssa", ""), ("aṃ", "a"), ("ṃ", ""), ("o", "a"), ("ī", "i"), ("ā", "a"), ("", "")]


def _lemma(w):
    if w in KEEP:
        return w
    for end, rep in ENDINGS:
        if w.endswith(end):
            stem = w[: len(w) - len(end)] + rep
            if stem in LEMMAS:
                return stem
    raise ValueError(f"unknown item word {w!r}")


def _tokens(phrase):
    p = phrase.strip()
    p = p[0].lower() + p[1:]
    p = p.replace("ñceva ", "ṃ ceva ").replace("ñca ", "ṃ ca ")
    p = re.sub(r"ñca$", "ṃ ca", p)
    p = p.replace("sāsavoca", "sāsavo ca")            # spelling: merged "ca" (4-05)
    p = p.replace("naviññeyyo", "na viññeyyo")
    out = []
    for w in p.split():
        out.append(_lemma(w))
    return out


def item_members(phrase):
    """-> (list of labels, plural_flag).  phrase = Pāli item phrase incl. the dhamm- word (or a slip without it)."""
    toks = _tokens(phrase)
    plural = False
    if toks and toks[-1] == "dhamma":
        plural = phrase.rstrip().endswith("dhammā")
        toks = toks[:-1]
    members, cur, i = [], [], 0
    while i < len(toks):
        for k in TIKA_KEYS:
            kw = k.split()
            if toks[i:i + len(kw)] == kw:
                duka = " ".join(cur)
                if duka and duka not in DUKA_ITEM:
                    raise ValueError(f"unknown duka {duka!r} in {phrase!r}")
                members.append((DUKA_ITEM[duka] + ", " if duka else "") + TIKA_ITEM[k])
                i += len(kw)
                if i < len(toks) and toks[i] == "ca":
                    i += 1
                cur = []
                break
        else:
            cur.append(toks[i])
            i += 1
    if cur:
        raise ValueError(f"dangling words {cur} in {phrase!r}")
    return members, plural


def ACC(phrase):
    m, _ = item_members(phrase)
    w = [f"{x} {DH}" for x in m]
    return w[0] if len(w) == 1 else ", ".join(w[:-1]) + " और " + w[-1]


def NOM(phrase):
    m, plural = item_members(phrase)
    if len(m) == 1 and not plural:
        return f"{m[0]} {DH}", False
    return ", ".join(m[:-1]) + " और " + m[-1] + " " + DH_PL, True


def DAT(phrase):
    return ACC(phrase) + " के लिए"


# =====================================================================================
# 2. Headings
# =====================================================================================
def DUKA_H(x):
    return S.DUKA(x)


def TIKA_H(x):
    return S.TIKA(x)


DUKA_NAME = {  # X in "<X> वाला दो का वर्गीकरण"
    "Hetu": "मूल", "Sahetuka": "मूल वाली परिघटनाओं", "Hetusampayutta": "मूलों से जुड़ी परिघटनाओं",
    "Hetusahetuka": "मूल रूपी और मूल वाली परिघटनाओं",
    "Hetuhetusampayutta": "मूल रूपी और मूलों से जुड़ी परिघटनाओं",
    "Nahetusahetuka": "मूल रूपी न होने वाली, पर मूल वाली परिघटनाओं",
    "Sappaccaya": "कारणों पर निर्भर रहने वाली परिघटनाओं", "Saṅkhata": "निर्मित परिघटनाओं",
    "Sanidassana": "दिखाई देने वाली परिघटनाओं", "Sappaṭigha": "टकराव वाली परिघटनाओं",
    "Rūpī": "भौतिक परिघटनाओं", "Lokiya": "लौकिक परिघटनाओं",
    "Kenaciviññeyya": "किसी एक प्रकार की चेतना से जानी जा सकने वाली परिघटनाओं",
}
for _b, _n, _npl, _ya in [("Āsava", "मन के मैल", "मन के मैलों", "Sāsava"),
                          ("Saññojana", "बंधन", "बंधनों", "Saññojaniya"),
                          ("Gantha", "गाँठ", "गाँठों", "Ganthaniya")]:
    _l = _b.lower()
    DUKA_NAME.update({
        _b: _n,
        _ya: f"{_npl} का विषय बनने वाली परिघटनाओं",
        f"{_b}sampayutta": f"{_npl} से जुड़ी परिघटनाओं",
        f"{_b}{_ya.lower()}": f"{_n} रूपी और {_npl} का विषय बनने वाली परिघटनाओं",
        f"{_b}{_l}sampayutta": f"{_n} रूपी और {_npl} से जुड़ी परिघटनाओं",
        f"{_b}vippayutta{_ya.lower()}": f"{_npl} से अलग, पर उनका विषय बनने वाली परिघटनाओं",
    })
TIKA_NAME = {  # X in "<X> वाला तीन का वर्गीकरण"
    "kusala": "हितकर", "vedanā": "अनुभूति", "vipāka": "कर्म-फल",
    "upādinna": "कर्म से उत्पन्न परिघटनाओं", "saṃkiliṭṭha": "क्लेशों से मलिन परिघटनाओं",
    "vitakka": "आरंभिक विचार", "pīti": "उल्लास",
    "dassanenapahātabba": "सत्य-दर्शन से छोड़ी जाने वाली परिघटनाओं",
    "dassanenapahātabbahetuka": "सत्य-दर्शन से छोड़े जाने वाले मूलों वाली परिघटनाओं",
    "ācayagāmi": "संचय की ओर ले जाने वाली परिघटनाओं", "sekkha": "सीखने के चरण की परिघटनाओं",
    "paritta": "सीमित परिघटनाओं", "parittārammaṇa": "सीमित विषय वाली परिघटनाओं",
    "hīna": "हीन परिघटनाओं", "micchattaniyata": "ग़लत दिशा में निश्चित परिघटनाओं",
    "maggārammaṇa": "मार्ग को विषय बनाने वाली परिघटनाओं", "uppanna": "उत्पन्न हो चुकी परिघटनाओं",
    "atīta": "अतीत की परिघटनाओं", "atītārammaṇa": "अतीत के विषय वाली परिघटनाओं",
    "ajjhatta": "स्वयं से संबंधित परिघटनाओं", "ajjhattārammaṇa": "स्वयं से संबंधित विषय वाली परिघटनाओं",
    "sanidassanasappaṭigha": "दिखाई देने वाली और टकराव वाली परिघटनाओं",
}


def DUKATIKA(duka, tika):
    return f"{DUKA_H(DUKA_NAME[duka])} और {TIKA_H(TIKA_NAME[tika])}"


def GOCCHAKA_TIKA(goc, tika):
    return f"{goc} और {TIKA_H(TIKA_NAME[tika])}"


PADA = {  # "<item> पद" (पद is masculine: वाली -> वाला etc.)
    "Kusala": "हितकर पद", "Akusala": "हानिकर पद", "Abyākata": "नैतिक रूप से अनिर्धारित पद",
    "Kusalākusala": "हितकर और हानिकर पद",
    "Sukhāyavedanāyasampayutta": "सुखद अनुभूति से जुड़ा पद",
    "Dukkhāyavedanāyasampayutta": "दुःखद अनुभूति से जुड़ा पद",
    "Adukkhamasukhāyavedanāyasampayutta": "न दुःखद, न सुखद अनुभूति से जुड़ा पद",
    "Vipāka": "कर्म-फल रूपी पद", "Vipākadhamma": "कर्म-फल उत्पन्न करने वाला पद",
    "Nevavipākanavipākadhamma": "न कर्म-फल रूपी, न कर्म-फल उत्पन्न करने वाला पद",
    "Upādinnupādāniya": "कर्म से उत्पन्न और आसक्ति का विषय बनने वाला पद",
    "Anupādinnupādāniya": "कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाला पद",
    "Anupādinnaanupādāniya": "न कर्म से उत्पन्न, न आसक्ति का विषय बनने वाला पद",
    "Saṃkiliṭṭhasaṃkilesika": "क्लेशों से मलिन और क्लेशों का विषय बनने वाला पद",
    "Asaṃkiliṭṭhasaṃkilesika": "क्लेशों से मलिन न होने वाला, पर क्लेशों का विषय बनने वाला पद",
    "Asaṃkiliṭṭhaasaṃkilesika": "क्लेशों से मलिन न होने वाला और क्लेशों का विषय न बनने वाला पद",
    "Savitakkasavicāra": "आरंभिक विचार और सतत विचार वाला पद",
    "Avitakkavicāramatta": "आरंभिक विचार से रहित, केवल सतत विचार वाला पद",
    "Avitakkaavicāra": "आरंभिक विचार और सतत विचार दोनों से रहित पद",
    "Pītisahagata": "उल्लास के साथ होने वाला पद", "Sukhasahagata": "सुख के साथ होने वाला पद",
    "Upekkhāsahagata": "समभाव के साथ होने वाला पद",
    "Dassanenapahātabba": "सत्य-दर्शन से छोड़ा जाने वाला पद",
    "Bhāvanāyapahātabba": "मानसिक अभ्यास से छोड़ा जाने वाला पद",
    "Nevadassanenanabhāvanāyapahātabba": "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़ा जाने वाला पद",
    "Dassanenapahātabbahetuka": "सत्य-दर्शन से छोड़े जाने वाले मूलों वाला पद",
    "Bhāvanāyapahātabbahetuka": "मानसिक अभ्यास से छोड़े जाने वाले मूलों वाला पद",
    "Nevadassanenanabhāvanāyapahātabbahetuka":
        "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़े जाने वाले मूलों वाला पद",
    "Ācayagāmi": "संचय की ओर ले जाने वाला पद", "Apacayagāmi": "संचय घटाने की ओर ले जाने वाला पद",
    "Nevācayagāmināpacayagāmi": "न संचय की ओर, न संचय घटाने की ओर ले जाने वाला पद",
    "Sekkha": "सीखने के चरण का पद", "Asekkha": "सीखना पूरा होने के चरण का पद",
    "Nevasekkhanāsekkha": "न सीखने के चरण का, न सीखना पूरा होने के चरण का पद",
    "Paritta": "सीमित पद", "Mahaggata": "उन्नत पद", "Appamāṇa": "अपरिमित पद",
    "Parittārammaṇa": "सीमित विषय वाला पद", "Mahaggatārammaṇa": "उन्नत विषय वाला पद",
    "Appamāṇārammaṇa": "अपरिमित विषय वाला पद",
    "Hīna": "हीन पद", "Majjhima": "मध्यम पद", "Paṇīta": "उत्तम पद",
    "Micchattaniyata": "ग़लत दिशा में निश्चित पद", "Sammattaniyata": "सही दिशा में निश्चित पद",
    "Aniyata": "अनिश्चित पद",
    "Maggārammaṇa": "मार्ग को विषय बनाने वाला पद", "Maggahetuka": "मार्ग को मूल बनाने वाला पद",
    "Maggādhipati": "मार्ग की प्रधानता वाला पद",
    "Uppanna": "उत्पन्न हो चुका पद", "Paccuppanna": "वर्तमान का पद",
    "Atītārammaṇa": "अतीत के विषय वाला पद", "Anāgatārammaṇa": "भविष्य के विषय वाला पद",
    "Paccuppannārammaṇa": "वर्तमान के विषय वाला पद",
    "Ajjhatta": "स्वयं से संबंधित पद", "Bahiddhā": "दूसरों से संबंधित पद",
    "Ajjhattārammaṇa": "स्वयं से संबंधित विषय वाला पद", "Bahiddhārammaṇa": "दूसरों से संबंधित विषय वाला पद",
    "Anidassanasappaṭigha": "दिखाई न देने वाला, पर टकराव वाला पद",
    "Anidassanaappaṭigha": "दिखाई न देने वाला और टकराव से रहित पद",
}
HEAD_FIXED = {
    "Dhammānulome dukatikapaṭṭhānaṃ": f"{S.DHAMMANULOMA}: {S.DUKATIKAPATTHANA}",
    "Paṭiccavārādi": "निर्भरता का खंड आदि",
    "Pañhāvāro": S.VARA["pañhā"],
    "Paccayacatukkaṃ": "कारणों के चार क्रम",
    "Paccanīyaṃ": S.PACCANIYA,
    "Paccanīyuddhāro": "नकारात्मक क्रम के लिए छँटाई",
    "Suddhaṃ": S.SUDDHA,
}
COND_STEM = {k.lower(): k for k in S.COND_KEYS}


def _cond_part(p):
    low = p[0].lower() + p[1:]
    if low in COND_STEM:
        return S.NAME(low)
    for pre in ("na", "no"):
        if low.startswith(pre) and low[len(pre):] in COND_STEM:
            return S.NNAME(low[len(pre):])
    raise ValueError(f"unknown condition heading part {p!r}")


def cond_heading(t):
    m = re.fullmatch(r"(.+?)paccay(o|ā|ādi)", t)
    if not m:
        return None
    body = m.group(1)
    body = body.replace("Nahetunaārammaṇa", "Nahetu-naārammaṇa")   # hyphen missing in one heading
    names = [_cond_part(p) for p in body.split("-")]
    out = " और ".join(names)
    return out + (" आदि" if m.group(2) == "ādi" else "")


def heading_hi(text):
    star = text.startswith("*") and text.endswith("*")
    t = text[1:-1] if star else text
    m = re.match(r"(\d+-\d+\.? )(.*)$", t)
    num, t = (m.group(1), m.group(2)) if m else ("", t)
    if t in HEAD_FIXED:
        h = HEAD_FIXED[t]
    elif t.endswith("padaṃ") and t[:-5] in PADA:
        h = PADA[t[:-5]]
    elif t.endswith("kusalattikaṃ") and "duka-" in t:
        h = DUKATIKA(t.split("duka-")[0], "kusala")
    elif t.startswith("Hetuduka-") and t.endswith("ttikaṃ"):
        h = DUKATIKA("Hetu", t[len("Hetuduka-"):-len("ttikaṃ")])
    else:
        h = cond_heading(t)
        if h is None:
            raise ValueError(f"unknown heading {text!r}")
    return f"*{num}{h}*" if star else f"{num}{h}"


# =====================================================================================
# 3. Editorial notes and whole-line formulas
# =====================================================================================
KUSALATTIKE = "हितकर वाले तीन के वर्गीकरण में"
YATHA_KUSALATTIKE = (f"जैसे {KUSALATTIKE} प्रश्नों के खंड का सकारात्मक क्रम भी, नकारात्मक क्रम भी, "
                     f"सकारात्मक-नकारात्मक क्रम भी और नकारात्मक-सकारात्मक क्रम भी गिना गया है")
GANETABBAM = "वैसे ही गिनना चाहिए।"
VARA_OBL = {  # "<X> के खंड"
    "sahajāta": "सह-उत्पत्ति", "paccaya": "कारण", "nissaya": "आश्रय", "saṃsaṭṭha": "घुले-मिले होने",
    "sampayutta": "जुड़ाव", "pañhā": "प्रश्नों", "paṭicca": "निर्भरता",
}


def V_GEN(k):      # sahajātavāropi … vitthāretabbā -> "सह-उत्पत्ति के खंड का भी"
    return f"{VARA_OBL[k]} के खंड का भी"


def V_LOC(k):      # sahajātavārepi -> "सह-उत्पत्ति के खंड में भी"
    return f"{VARA_OBL[k]} के खंड में भी"


def V_NOM(k):      # sahajātavāropi … sadisā -> "सह-उत्पत्ति का खंड भी"
    return f"{VARA_OBL[k]} का खंड भी"


PATICCA_SADISA = "निर्भरता के खंड के समान"
VITTHARETABBA = "विस्तार करना चाहिए"
FIVE_GEN = (f"{V_GEN('sahajāta')}, {V_GEN('paccaya')}, {V_GEN('nissaya')}, {V_GEN('saṃsaṭṭha')} और "
            f"{V_GEN('sampayutta')}")
LOKIYADUKA_OBL = f"{S.DUKA(DUKA_NAME['Lokiya'])}".replace("वाला दो का", "वाले दो के")
CULANTARADUKE = "बीच के छोटे दो-दो के वर्गीकरणों में"
SAPPACCAYA_OBL = S.DUKA(DUKA_NAME["Sappaccaya"]).replace("वाला दो का", "वाले दो के")
SABBATTHA = "हर जगह"
SAMKHITTA = "संक्षिप्त"
KENACI_K = f"{DUKA_ITEM['kenaci viññeyya']}, {TIKA_ITEM['kusala']} {DH}"

PAREN = {
    "(saṃkhittaṃ)": f"({SAMKHITTA})", "(Saṃkhittaṃ)": f"({SAMKHITTA})",
    "(Saṃkhittaṃ.)": f"({SAMKHITTA}।)", "(saṃkhittaṃ.)": f"({SAMKHITTA}।)",
    "(anulomaṃ)": f"({S.ANULOMA})", "(Anulomaṃ)": f"({S.ANULOMA})", "(paccanīyaṃ)": f"({S.PACCANIYA})",
    "(saṃkhittaṃ, anulomaṃ)": f"({SAMKHITTA}, {S.ANULOMA})",
    "(saṃkhittaṃ, paccanīyaṃ)": f"({SAMKHITTA}, {S.PACCANIYA})",
    "(saṃkhittaṃ, anulomapaccanīyaṃ)": f"({SAMKHITTA}, {S.ANULOMAPACCANIYA})",
    "(saṃkhittaṃ, anuloma paccanīyaṃ)": f"({SAMKHITTA}, {S.ANULOMAPACCANIYA})",
    "(saṃkhittaṃ, paccanīyānulomaṃ)": f"({SAMKHITTA}, {S.PACCANIYANULOMA})",
    "(sabbattha ekaṃ)": S.SABBATTHA_EKAM, "(sabbattha tīṇi)": f"({SABBATTHA} तीन)",
    "(sabbattha ekaṃ, saṃkhittaṃ)": f"({SABBATTHA} एक, {SAMKHITTA})",
    "(sabbattha nava, saṃkhittaṃ)": f"({SABBATTHA} नौ, {SAMKHITTA})",
    "(pañhāvārepi sabbattha ekaṃ)": f"({V_LOC('pañhā')} {SABBATTHA} एक)",
    "(pañhāvārepi sabbattha ekaṃ.)": f"({V_LOC('pañhā')} {SABBATTHA} एक।)",
    "(Sahajātavārepi…pe… pañhāvārepi sabbattha ekaṃ.)": f"({V_LOC('sahajāta')}… {V_LOC('pañhā')} {SABBATTHA} एक।)",
    "(Sahajātavārepi…pe… pañhāvārepi sabbattha ekaṃ)": f"({V_LOC('sahajāta')}… {V_LOC('pañhā')} {SABBATTHA} एक)",
    "(Sahajātavārepi …pe… pañhāvārepi sabbattha ekaṃ.)": f"({V_LOC('sahajāta')} … {V_LOC('pañhā')} {SABBATTHA} एक।)",
    "(Sahajātavārepi …pe… pañhāvārepi sabbattha ekaṃ)": f"({V_LOC('sahajāta')} … {V_LOC('pañhā')} {SABBATTHA} एक)",
    "(Sahajātavārepi… sampayuttavārepi sabbattha nava.)":
        f"({V_LOC('sahajāta')}… {V_LOC('sampayutta')} {SABBATTHA} नौ।)",
    "(Saṃkhittaṃ. Sahajātavārepi paccayavārepi…pe… pañhāvārepi sabbattha ekaṃ.)":
        f"({SAMKHITTA}। {V_LOC('sahajāta')}, {V_LOC('paccaya')}… {V_LOC('pañhā')} {SABBATTHA} एक।)",
    "(saṃkhittaṃ. Sahajātavārepi…pe… pañhāvārepi sabbattha ekaṃ)":
        f"({SAMKHITTA}। {V_LOC('sahajāta')}… {V_LOC('pañhā')} {SABBATTHA} एक)",
    "(saṃkhittaṃ. Sahajātavārepi…pe… sampayuttavārepi sabbattha ekaṃ)":
        f"({SAMKHITTA}। {V_LOC('sahajāta')}… {V_LOC('sampayutta')} {SABBATTHA} एक)",
    "(saṃkhittaṃ. Sahajātavārepi…pe… sampayuttavārepi sabbattha pañca.)":
        f"({SAMKHITTA}। {V_LOC('sahajāta')}… {V_LOC('sampayutta')} {SABBATTHA} पाँच।)",
    "(saṃkhittaṃ. Paccanīyaṃ. Sahajātavārepi…pe… sampayuttavārepi sabbattha dve)":
        f"({SAMKHITTA}। {S.PACCANIYA}। {V_LOC('sahajāta')}… {V_LOC('sampayutta')} {SABBATTHA} दो)",
    "(saṃkhittaṃ, sahajātavāropi…pe… pañhāvāropi sabbattha sadisā)":
        f"({SAMKHITTA}, {V_NOM('sahajāta')}… {V_NOM('pañhā')} {SABBATTHA} समान हैं)",
    "(saṃkhittaṃ. Sappaccayasadisaṃ vitthāretabbaṃ)":
        f"({SAMKHITTA}। {SAPPACCAYA_OBL} के समान {VITTHARETABBA})",
    "(saṃkhittaṃ, lokiyalokuttaragamanasadisaṃ)": f"({SAMKHITTA}, लौकिक और लोकोत्तर के क्रम के समान)",
    "(sabbe paccayā kātabbā)": "(सभी कारण लागू करने चाहिए)",
    "(sahajātakammameva, saṃkhittaṃ)": f"(केवल सह-उत्पत्ति रूपी कर्म, {SAMKHITTA})",
    "(sahajātādhipatiyeva labbhati, ārammaṇādhipati natthi)":
        f"({S.SAHAJATADHIPATI} ही लागू होती है, {S.ARAMMANADHIPATI} नहीं है)",
    "(majjhe tiṇṇaṃ sahajātādhipati labbhati)": f"(बीच के तीनों में {S.SAHAJATADHIPATI} लागू होती है)",
    "(itare dve anantarūpanissayo pakatūpanissayoyeva)":
        f"(बाकी दो में {S.ANANTARUPANISSAYA} और {S.PAKATUPANISSAYA} ही)",
    "(tadārammaṇāyeva labbhanti)": "(उसी विषय को लेकर उत्पन्न होने वाले ही लागू होते हैं)",
    "(ārammaṇādhipatiyeva)": f"({S.ARAMMANADHIPATI} ही)",
    # the "paṭicca-like" expansion notes
    "(Sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi paṭiccavārasadisā vitthāretabbā.)":
        f"({FIVE_GEN} {PATICCA_SADISA} {VITTHARETABBA}।)",
    "(Sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāro sampayuttavāropi paṭiccavārasadisā vitthāretabbā.)":
        f"({FIVE_GEN} {PATICCA_SADISA} {VITTHARETABBA}।)",
    "(Sahajātavārampi paccayavārampi nissayavārampi saṃsaṭṭhavārampi sampayuttavārampi paṭiccavārasadisā vitthāretabbā.)":
        f"({FIVE_GEN} {PATICCA_SADISA} {VITTHARETABBA}।)",
    "(Sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi vitthāretabbā.)":
        f"({FIVE_GEN} {VITTHARETABBA}।)",
    "(Sahajātavāropi… sampayuttavāropi paṭiccavārasadisā vitthāretabbā.)":
        f"({V_GEN('sahajāta')}… {V_GEN('sampayutta')} {PATICCA_SADISA} {VITTHARETABBA}।)",
    "(Sahajātavāropi…pe… sampayuttavāropi paṭiccavārasadisā vitthāretabbā.)":
        f"({V_GEN('sahajāta')}… {V_GEN('sampayutta')} {PATICCA_SADISA} {VITTHARETABBA}।)",
    "(Sahajātavārampi…pe… sampayuttavārampi paṭiccavārasadisaṃ vitthāretabbaṃ.)":
        f"({V_GEN('sahajāta')}… {V_GEN('sampayutta')} {PATICCA_SADISA} {VITTHARETABBA}।)",
    "(Sahajātavāropi…pe… sampayuttavāropi paṭiccavārasadisā.)":
        f"({V_NOM('sahajāta')}… {V_NOM('sampayutta')} {PATICCA_SADISA} हैं।)",
    "(Sahajātavārampi…pe… sampayuttavārampi paṭiccavārasadisaṃ.)":
        f"({V_NOM('sahajāta')}… {V_NOM('sampayutta')} {PATICCA_SADISA} हैं।)",
    "(Sahajātavāropi…pe… sampayuttavāropi vitthāretabbā.)":
        f"({V_GEN('sahajāta')}… {V_GEN('sampayutta')} {VITTHARETABBA}।)",
    "(Sahajātavāropi…pe… sampayuttavāropi sabbattha vitthāretabbo.)":
        f"({V_GEN('sahajāta')}… {V_GEN('sampayutta')} {SABBATTHA} {VITTHARETABBA}।)",
    "(Sahajātavāropi…pe… pañhāvāropi vitthāretabbā.)":
        f"({V_GEN('sahajāta')}… {V_GEN('pañhā')} {VITTHARETABBA}।)",
    "(Sahajātavāropi…pe… pañhāvāropi vitthāretabbo.)":
        f"({V_GEN('sahajāta')}… {V_GEN('pañhā')} {VITTHARETABBA}।)",
    "(Sahajātavāropi…pe… pañhāvāropi sabbattha vitthāretabbā.)":
        f"({V_GEN('sahajāta')}… {V_GEN('pañhā')} {SABBATTHA} {VITTHARETABBA}।)",
    # counting notes
    "(Yathā kusalattike pañhāvārassa anulomampi paccanīyampi anulomapaccanīyampi paccanīyānulomampi gaṇitaṃ, evaṃ gaṇetabbaṃ.)":
        f"({YATHA_KUSALATTIKE}, {GANETABBAM})",
    "(Yathā kusalattike pañhāvārassa anulomampi paccanīyampi anulomapaccanīyampi paccanīyānulomampi naṇitaṃ, evaṃ gaṇetabbaṃ.)":
        f"({YATHA_KUSALATTIKE}, {GANETABBAM})",   # naṇitaṃ: spelling slip for gaṇitaṃ
    "(Yathā kusalattike pañhāvārassa anulomampi paccanīyampi anulomapaccanīyampi paccanīyānulomampi gaṇitaṃ evaṃ gaṇetabbaṃ.)":
        f"({YATHA_KUSALATTIKE} {GANETABBAM})",
    "(Yathā kusalattike pañhāvārassa anulomampi paccanīyampi anulomapaccanīyampi paccanīyānulomampi gaṇitaṃ, evaṃ gaṇetabbaṃ. Ajjhattabahiddhā na labbhanti.)":
        f"({YATHA_KUSALATTIKE}, {GANETABBAM} स्वयं और दूसरों दोनों से संबंधित परिघटनाएँ लागू नहीं होतीं।)",
    "(Yathā kusalattike pañhāvārassa anulomampi paccanīyampi anulomapaccanīyampi paccanīyānulomampi gaṇitaṃ, evaṃ gaṇetabbaṃ. Imamhi dukatike paṭiccavārampi sahajātavārampi paccayavārampi nissayavārampi saṃsaṭṭhavārampi sampayuttavārampi anuppannampi uppādīpi natthi.)":
        f"({YATHA_KUSALATTIKE}, {GANETABBAM} इस दो और तीन के वर्गीकरण में {V_NOM('paṭicca')}, "
        f"{V_NOM('sahajāta')}, {V_NOM('paccaya')}, {V_NOM('nissaya')}, {V_NOM('saṃsaṭṭha')}, "
        f"{V_NOM('sampayutta')}, उत्पन्न न हुई परिघटनाएँ भी और उत्पन्न होने वाली परिघटनाएँ भी नहीं हैं।)",
    "(Yathā kusalattike pañhāvārassa anulomampi paccanīyampi anulomapaccanīyampi paccanīyānulomampi gaṇitaṃ, evaṃ gaṇetabbaṃ. Imamhi dukatike paṭiccavārampi sahajātavārampi paccayavārampi nissayavārampi saṃsaṭṭhavārampi sampayuttavārampi atītampi anāgatampi natthi.)":
        f"({YATHA_KUSALATTIKE}, {GANETABBAM} इस दो और तीन के वर्गीकरण में {V_NOM('paṭicca')}, "
        f"{V_NOM('sahajāta')}, {V_NOM('paccaya')}, {V_NOM('nissaya')}, {V_NOM('saṃsaṭṭha')}, "
        f"{V_NOM('sampayutta')}, अतीत की परिघटनाएँ भी और भविष्य की परिघटनाएँ भी नहीं हैं।)",
    "(Yathā kusalattike pañhāvārassa anulomampi paccanīyampi anulomapaccanīyampi paccanīyānulomampi gaṇitaṃ, evaṃ gaṇetabbaṃ. Kenaci viññeyyaṃ akusalampi kenaci viññeyyaṃ abyākatampi kenaci viññeyyakusalasadisaṃ vitthāretabbaṃ)":
        f"({YATHA_KUSALATTIKE}, {GANETABBAM} {DUKA_ITEM['kenaci viññeyya']}, {TIKA_ITEM['akusala']} {DH} का भी "
        f"और {DUKA_ITEM['kenaci viññeyya']}, {TIKA_ITEM['abyākata']} {DH} का भी {KENACI_K} के समान "
        f"{VITTHARETABBA})",
    "(Hetupaccayo natthi. Pañhāvārepi sabbattha ekaṃ, pañhāvārepi imesaṃ tiṇṇannaṃ hetupaccayo natthi.)":
        f"({S.NAME('hetu')} नहीं है। {V_LOC('pañhā')} {SABBATTHA} एक, {V_LOC('pañhā')} इन तीनों के लिए "
        f"{S.NAME('hetu')} नहीं है।)",
    "(Appaccayampi asaṅkhatampi sanidassanampi na labbhati.)":
        f"({DUKA_ITEM['appaccaya']} {DH} भी, {DUKA_ITEM['asaṅkhata']} {DH} भी और {DUKA_ITEM['sanidassana']} {DH} भी "
        f"लागू नहीं होती।)",
    "(Oghagocchakampi yogagocchakampi āsavagocchakakusalattikasadisaṃ.)":
        f"(बाढ़ों का वर्ग भी और जकड़नों का वर्ग भी मन के मैलों के वर्ग और {KUSALATTIKE.replace(' में', '')} "
        f"के समान हैं।)",
    "(Yathā cūḷantaraduke lokiyadukagamanaṃ, evaṃ imampi ñātabbaṃ. Sahajātavāropi…pe… pañhāvāropi vitthāretabbā.)":
        f"(जैसे {CULANTARADUKE} {LOKIYADUKA_OBL} का क्रम है, वैसे ही इसे भी समझना चाहिए। "
        f"{V_GEN('sahajāta')}… {V_GEN('pañhā')} {VITTHARETABBA}।)",
    "(Yathā cūḷantaraduke lokiyadukasadisaṃ. Sahajātavāropi…pe… pañhāvāropi sabbattha vitthāretabbā.)":
        f"(जैसे {CULANTARADUKE}, {LOKIYADUKA_OBL} के समान। "
        f"{V_GEN('sahajāta')}… {V_GEN('pañhā')} {SABBATTHA} {VITTHARETABBA}।)",
}
LINE_FIXED = {
    "Cūḷantaraduke lokiyadukasadisaṃ.": f"{CULANTARADUKE} {LOKIYADUKA_OBL} के समान।",
    "Hetugocchakaṃ niṭṭhitaṃ.": "मूलों का वर्ग पूरा हुआ।",
    "Cūḷantaradukaṃ niṭṭhitaṃ.": "बीच के छोटे दो-दो के वर्गीकरण पूरे हुए।",
    "Āsavagocchakaṃ niṭṭhitaṃ.": "मन के मैलों का वर्ग पूरा हुआ।",
    "Saññojanagocchakakusalattikaṃ niṭṭhitaṃ.": f"{GOCCHAKA_TIKA('बंधनों का वर्ग', 'kusala')} पूरा हुआ।",
    "Ganthagocchakakusalattikaṃ niṭṭhitaṃ.": f"{GOCCHAKA_TIKA('गाँठों का वर्ग', 'kusala')} पूरा हुआ।",
}


def niṭṭhita_line(t):
    m = re.fullmatch(r"(\w+?)duka(\w+?)ttikaṃ niṭṭhitaṃ\.", t)
    if not m:
        return None
    duka = m.group(1)
    tika = m.group(2)
    return f"{DUKATIKA(duka, tika)} पूरा हुआ।"


# =====================================================================================
# 4. Sentence parser
# =====================================================================================
SUBTYPE = {"ārammaṇādhipati": S.ARAMMANADHIPATI, "sahajātādhipati": S.SAHAJATADHIPATI,
           "ārammaṇūpanissayo": S.ARAMMANUPANISSAYA, "anantarūpanissayo": S.ANANTARUPANISSAYA,
           "pakatūpanissayo": S.PAKATUPANISSAYA, "Pakatūpanissayo": S.PAKATUPANISSAYA,
           "ārammaṇapurejātaṃ": S.ARAMMANAPUREJATA, "vatthupurejātaṃ": S.VATTHUPUREJATA}
PHRASE = {  # fixed content phrases
    "vicikicchāsahagate khandhe paṭicca vicikicchāsahagato moho":
        "संशय के साथ होने वाले समूहों पर निर्भर होकर संशय के साथ होने वाला मोह",
    "uddhaccasahagate khandhe paṭicca uddhaccasahagato moho":
        "बेचैनी के साथ होने वाले समूहों पर निर्भर होकर बेचैनी के साथ होने वाला मोह",
    "uppannaṃ utuṃ upanissāya jhānaṃ uppādeti, vipassanaṃ… maggaṃ… abhiññaṃ… samāpattiṃ uppādeti":
        "उत्पन्न हो चुके तापमान के प्रबल आश्रय से ध्यान उत्पन्न करता है, अंतर्दृष्टि… मार्ग… उच्च ज्ञान… "
        "ध्यान-अवस्था उत्पन्न करता है",
    "Cūḷantaraduke lokiyadukasadisaṃ": f"{CULANTARADUKE} {LOKIYADUKA_OBL} के समान",
}
NUMW = dict(S.NUM)
COND_RX = "|".join(sorted(S.COND_KEYS, key=len, reverse=True))
ITEM_CH = r"[^.…()–,;]"
RX_PATICCA = re.compile(rf"({ITEM_CH}+?) paṭicca ({ITEM_CH}+?) (uppajjati|uppajjanti)")
RX_PANHA = re.compile(rf"({ITEM_CH}+?) ((?:kenaci )?\S+ssa\b{ITEM_CH}*?dhammassa) ((?:na|no)?(?:{COND_RX}))paccayena paccayo")
RX_ABL = re.compile(rf"(na|no)?({COND_RX})paccayā", re.I)
RX_INS = re.compile(rf"({COND_RX})paccayena paccayo", re.I)
RX_NUM = re.compile(r"(" + "|".join(sorted(NUMW, key=len, reverse=True)) + r")(?![\wāīūṃṅñṭḍṇḷ])")
RX_PAREN = re.compile(r"\([^()]*\)")
RX_SUB = re.compile("|".join(sorted(SUBTYPE, key=len, reverse=True)))


def abl_hi(m):
    k = m.group(2).lower()
    return S.NABL(k) if m.group(1) else S.ABL(k)


def is_count_line(t):
    first = re.split(r"[\s,]", t, maxsplit=1)[0]
    if first in ("Hetuyā", "Nahetuyā") or re.fullmatch(r"(?:Na|No)?\w+(?:yā|e)", first) and \
            S._classify(first)[0] in ("loc", "neg_loc"):
        return True
    if S._classify(first)[0] in ("abl", "neg_abl") and "paṭicca" not in t:
        return True
    return False


def count_line(t):
    """Counting line with optional parenthetical notes inside or at the end."""
    out, pos = "", 0
    for m in RX_PAREN.finditer(t):
        seg = t[pos:m.start()]
        out += _count_seg(seg)
        p = m.group(0)
        if re.fullmatch(r"\(\d+\)", p):
            out += p
        else:
            if p not in PAREN:
                raise ValueError(f"unknown paren {p!r}")
            out += PAREN[p]
        pos = m.end()
    out += _count_seg(t[pos:])
    return out


def _count_seg(seg):
    if not seg.strip():
        return seg
    lead = seg[: len(seg) - len(seg.lstrip(" "))]
    trail = seg[len(seg.rstrip(" ")):]
    core = seg.strip()
    if re.fullmatch(r"[.,]", core):
        return lead + {".": "।", ",": ","}[core] + trail
    hi = S.count_hi(core)
    # "kamme āhāre indriye jhāne tīṇi": the Pāli lists several counted conditions without commas;
    # put a comma between them, as count_hi does after ablatives and numbers
    hi = re.sub(r"(में) (?=(?:पूर्ण |प्रबल )?\S+-कारण (?:में|के अभाव में))", r"\1, ", hi)
    return lead + hi + trail


class Ctx:
    plural = False   # number of the current pañhā subject


SPELLFIX = [  # pure spelling slips in the source, parsed as the word meant (listed in the notes)
    ("nahetu asakkho dhammo", "nahetu asekkho dhammo"),
    ("…pe… kamma nava,", "…pe… kamme nava,"),
    ("…pe… avigata nava", "…pe… avigate nava"),
]


def translate_line(t):
    for a, b in SPELLFIX:
        t = t.replace(a, b)
    if t in LINE_FIXED:
        return LINE_FIXED[t]
    n = niṭṭhita_line(t)
    if n:
        return n
    if t in PAREN:
        return PAREN[t]
    if is_count_line(t):
        return count_line(t)
    return clause_line(t)


def clause_line(t):
    out, i = [], 0
    ctx = Ctx()
    while i < len(t):
        rest = t[i:]
        if rest[0] == " ":
            out.append(" ")
            i += 1
            continue
        m = RX_PATICCA.match(rest)
        if m:
            acc, nom, verb = m.groups()
            j = m.end()
            conds = []
            # leading condition chain: " Xpaccayā", "… Xpaccayā"
            while True:
                mm = re.match(r"(?: |\s?…\s?)((?:na|no)?(?:" + COND_RX + r")paccayā)", t[i + j:])
                if not mm or (conds and "…" not in mm.group(0)[: mm.start(1)]):
                    break
                sep = "" if not conds else t[i + j: i + j + mm.start(1)]
                conds.append((sep, abl_hi(RX_ABL.fullmatch(mm.group(1)))))
                j += mm.end()
            if not conds:
                raise ValueError(f"paṭicca without condition: {rest[:80]!r}")
            nom_hi, _ = NOM(nom)
            ch = conds[0][1] + "".join(s.replace("…", "…") + c for s, c in conds[1:])
            vb = "उत्पन्न होती हैं" if verb == "uppajjanti" else "उत्पन्न होती है"
            out.append(f"{ACC(acc)} {S.DEP['paṭicca']} {nom_hi} {ch} {vb}")
            i += j
            continue
        m = RX_PANHA.match(rest)
        if m:
            nom, dat, k = m.groups()
            nom_hi, ctx.plural = NOM(nom)
            k = k[0].lower() + k[1:]
            out.append(f"{nom_hi}, {DAT(dat)} {S.INS(k)} {'होती हैं' if ctx.plural else 'होती है'}")
            i += m.end()
            continue
        m = RX_INS.match(rest)
        if m:
            k = m.group(1)[0].lower() + m.group(1)[1:]
            out.append(f"{S.INS(k)} {'होती हैं' if ctx.plural else 'होती है'}")
            i += m.end()
            continue
        hit = None
        for ph, hi in PHRASE.items():
            if rest.startswith(ph):
                hit = (ph, hi)
                break
        if hit:
            out.append(hit[1])
            i += len(hit[0])
            continue
        m = RX_ABL.match(rest)
        if m:
            out.append(abl_hi(m))
            i += m.end()
            continue
        m = RX_SUB.match(rest)
        if m:
            out.append(SUBTYPE[m.group(0)])
            i += m.end()
            continue
        m = RX_NUM.match(rest)
        if m:
            out.append(NUMW[m.group(1)])
            i += m.end()
            continue
        m = RX_PAREN.match(rest)
        if m:
            p = m.group(0)
            if re.fullmatch(r"\(\d+\)", p):
                out.append(p)
            elif p in PAREN:
                out.append(PAREN[p])
            else:
                raise ValueError(f"unknown paren {p!r}")
            i += m.end()
            continue
        if rest.startswith("…pe…"):
            out.append("…")
            i += 4
            continue
        ch = rest[0]
        if ch in " …,–":
            out.append(ch)
            i += 1
            continue
        if ch == ".":
            out.append("।")
            i += 1
            continue
        raise ValueError(f"cannot parse at: {rest[:90]!r}")
    return "".join(out)


# =====================================================================================
# 5. File assembly
# =====================================================================================
ID_RX = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")


def build_file(fname):
    src = (S.PALI_DIR / fname).read_text(encoding="utf-8")
    hindi, errors = [], []
    for ln, line in enumerate(src.splitlines(), 1):
        if not line.strip():
            continue
        body = ID_RX.sub("", line)
        try:
            if body.startswith("#"):
                hashes = body[: len(body) - len(body.lstrip("#"))]
                h = f"{hashes} {heading_hi(body.lstrip('#').strip())}"
            else:
                h = translate_line(body)
        except Exception as e:  # noqa: BLE001
            errors.append(f"{fname}:{ln}: {e}")
            h = "???"
        hindi.append(h)
    return src, hindi, errors


def main():
    dry = "--dry" in sys.argv
    allerr = []
    for f in FILES:
        src, hindi, errs = build_file(f)
        allerr += errs
        if not errs and not dry:
            text = S.assemble(src, hindi)
            (S.HI_DIR / f).write_text(text, encoding="utf-8", newline="\n")
            print("wrote", f, len(hindi), "lines")
    for e in allerr[:60]:
        print(e)
    print("errors:", len(allerr))


if __name__ == "__main__":
    main()
