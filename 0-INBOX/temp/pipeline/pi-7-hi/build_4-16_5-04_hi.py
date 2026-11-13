"""Hindi plain zero-shot builder for pi-7 (Paṭṭhāna) files 4-16 .. 4-21 and 5-01 .. 5-04.

Every line is composed from fixed frames (imported from build_sample_hi.py) and item tables, so
identical Pāli always gives identical Hindi.

    python -I -B -X utf8 build_4-16_5-04_hi.py            # build + write all ten files
    python -I -B -X utf8 build_4-16_5-04_hi.py 4-16 5-01  # only the files whose name starts so
    python -I -B -X utf8 build_4-16_5-04_hi.py --dry      # build, report errors, write nothing
"""
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi")
import build_sample_hi as S  # noqa: E402

FILES = ["4-16-tikaduka-sappaccayaduka.md", "4-17-tikaduka-asavaduka.md", "4-18-tikaduka-sarammanaduka.md",
         "4-19-tikaduka-kilesaduka.md", "4-20-tikaduka-dassanenapahatabbaduka.md", "4-21-tikaduka-sauttaraduka.md",
         "5-01-anuloma-tikatika.md", "5-02-anuloma-dukaduka.md", "5-03-paccaniya-tika.md", "5-04-paccaniya-duka.md"]
# number of components (triad / dyad items) that make up one item of a frame
NCOMP = {"4": 2, "5-01": 2, "5-02": 2, "5-03": 1, "5-04": 1}

# extra Pāli number words in these files (added to the importer's own table at run time only)
S.NUM.update({"ekūnatiṃsa": "उनतीस", "tiṃsa": "तीस", "catuvīsa": "चौबीस", "chattiṃsa": "छत्तीस",
              "pañcatiṃsa": "पैंतीस", "catuttiṃsa": "चौंतीस", "sattatiṃsa": "सैंतीस", "ekavīsa": "इक्कीस",
              "soḷasa": "सोलह", "sattarasa": "सत्रह", "aṭṭhārasa": "अठारह", "dvattiṃsa": "बत्तीस",
              "tettiṃsa": "तैंतीस", "ekatiṃsa": "इकतीस", "chabbīsa": "छब्बीस", "pañcavīsa": "पच्चीस",
              "sattavīsa": "सत्ताईस", "aṭṭhavīsa": "अट्ठाईस", "bāvīsa": "बाईस", "tevīsa": "तेईस"})

DH, DH_PL = S.DHAMMA, S.DHAMMA_PL       # परिघटना / परिघटनाएँ
NA = "न होने वाली"                      # generic negation of an item ("na" + item)

# =====================================================================================
# 1. Item lexicon (Pāli stem -> Hindi feminine adjective; pi-1 1-matika.md items)
# =====================================================================================
LEX = {
    # triads
    "kusala": "हितकर", "akusala": "हानिकर", "abyākata": "नैतिक रूप से अनिर्धारित",
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
    "ajjhattabahiddhā": "स्वयं और दूसरों दोनों से संबंधित",
    "ajjhattārammaṇa": "स्वयं से संबंधित विषय वाली", "bahiddhārammaṇa": "दूसरों से संबंधित विषय वाली",
    "ajjhattabahiddhārammaṇa": "स्वयं और दूसरों दोनों से संबंधित विषय वाली",
    "sanidassanasappaṭigha": "दिखाई देने वाली और टकराव वाली",
    "anidassanasappaṭigha": "दिखाई न देने वाली, पर टकराव वाली",
    "anidassanaappaṭigha": "दिखाई न देने वाली और टकराव से रहित",
    # dyads: roots cluster
    "hetu": "मूल रूपी", "nahetu": "मूल रूपी न होने वाली",
    "sahetuka": "मूल वाली", "ahetuka": "मूल से रहित",
    "hetusampayutta": "मूलों से जुड़ी", "hetuvippayutta": "मूलों से अलग",
    # small intermediate dyads
    "sappaccaya": "कारणों पर निर्भर रहने वाली", "appaccaya": "कारणों पर निर्भर न रहने वाली",
    "saṅkhata": "निर्मित", "asaṅkhata": "अनिर्मित",
    "sanidassana": "दिखाई देने वाली", "anidassana": "दिखाई न देने वाली",
    "sappaṭigha": "टकराव वाली", "appaṭigha": "टकराव से रहित",
    "rūpi": "भौतिक", "arūpi": "अभौतिक", "lokiya": "लौकिक", "lokuttara": "लोकोत्तर",
    # clusters (gocchaka)
    "āsava": "मन के मैल रूपी", "noāsava": "मन के मैल रूपी न होने वाली",
    "sāsava": "मन के मैलों का विषय बनने वाली", "anāsava": "मन के मैलों का विषय न बनने वाली",
    "āsavasampayutta": "मन के मैलों से जुड़ी", "āsavavippayutta": "मन के मैलों से अलग",
    "saññojana": "बंधन रूपी", "nosaññojana": "बंधन रूपी न होने वाली",
    "saññojaniya": "बंधनों का विषय बनने वाली", "asaññojaniya": "बंधनों का विषय न बनने वाली",
    "saññojanasampayutta": "बंधनों से जुड़ी", "saññojanavippayutta": "बंधनों से अलग",
    "gantha": "गाँठ रूपी", "nogantha": "गाँठ रूपी न होने वाली",
    "ganthaniya": "गाँठों का विषय बनने वाली", "aganthaniya": "गाँठों का विषय न बनने वाली",
    "ganthasampayutta": "गाँठों से जुड़ी", "ganthavippayutta": "गाँठों से अलग",
    "ogha": "बाढ़ रूपी", "noogha": "बाढ़ रूपी न होने वाली",
    "yoga": "जकड़न रूपी", "noyoga": "जकड़न रूपी न होने वाली",
    "nīvaraṇa": "बाधा रूपी", "nonīvaraṇa": "बाधा रूपी न होने वाली",
    "parāmāsa": "ग़लत धारणा रूपी", "noparāmāsa": "ग़लत धारणा रूपी न होने वाली",
    "parāmaṭṭha": "ग़लत धारणा का विषय बनने वाली", "aparāmaṭṭha": "ग़लत धारणा का विषय न बनने वाली",
    "parāmāsasampayutta": "ग़लत धारणा से जुड़ी", "parāmāsavippayutta": "ग़लत धारणा से अलग",
    "upādāna": "आसक्ति रूपी", "noupādāna": "आसक्ति रूपी न होने वाली",
    "upādāniya": "आसक्ति का विषय बनने वाली", "anupādāniya": "आसक्ति का विषय न बनने वाली",
    "upādānasampayutta": "आसक्ति से जुड़ी", "upādānavippayutta": "आसक्ति से अलग",
    "kilesa": "मन के क्लेश रूपी", "nokilesa": "मन के क्लेश रूपी न होने वाली",
    "saṃkilesika": "क्लेशों का विषय बनने वाली", "asaṃkilesika": "क्लेशों का विषय न बनने वाली",
    "saṃkiliṭṭha": "क्लेशों से मलिन", "asaṃkiliṭṭha": "क्लेशों से मलिन न होने वाली",
    "kilesasampayutta": "क्लेशों से जुड़ी", "kilesavippayutta": "क्लेशों से अलग",
    # large intermediate dyads
    "sārammaṇa": "विषय वाली", "anārammaṇa": "विषय से रहित",
    "citta": "मन रूपी", "nocitta": "मन रूपी न होने वाली",
    "cetasika": "मन की सहचर", "acetasika": "मन की सहचर न होने वाली",
    "cittasampayutta": "मन से जुड़ी", "cittavippayutta": "मन से अलग",
    "cittasaṃsaṭṭha": "मन से घुली-मिली", "cittavisaṃsaṭṭha": "मन से घुली-मिली न होने वाली",
    "cittasamuṭṭhāna": "मन से उत्पन्न", "nocittasamuṭṭhāna": "मन से उत्पन्न न होने वाली",
    "cittasahabhu": "मन के साथ-साथ होने वाली", "nocittasahabhu": "मन के साथ-साथ न होने वाली",
    "cittānuparivatti": "मन का अनुसरण करने वाली", "nocittānuparivatti": "मन का अनुसरण न करने वाली",
    "cittasaṃsaṭṭhasamuṭṭhāna": "मन से घुली-मिली और मन से उत्पन्न",
    "cittasaṃsaṭṭhasamuṭṭhānasahabhu": "मन से घुली-मिली, मन से उत्पन्न और मन के साथ-साथ होने वाली",
    "cittasaṃsaṭṭhasamuṭṭhānānuparivatti": "मन से घुली-मिली, मन से उत्पन्न और मन का अनुसरण करने वाली",
    "ajjhattika": "आंतरिक", "bāhira": "बाह्य",
    "upādā": "व्युत्पन्न", "noupādā": "व्युत्पन्न न होने वाली",
    "upādinna": "कर्म से उत्पन्न", "anupādinna": "कर्म से उत्पन्न न होने वाली",
    # final dyads
    "savitakka": "आरंभिक विचार वाली", "avitakka": "आरंभिक विचार से रहित",
    "savicāra": "सतत विचार वाली", "avicāra": "सतत विचार से रहित",
    "sappītika": "उल्लास वाली", "appītika": "उल्लास से रहित",
    "napītisahagata": "उल्लास के साथ न होने वाली", "nasukhasahagata": "सुख के साथ न होने वाली",
    "naupekkhāsahagata": "समभाव के साथ न होने वाली",
    "kāmāvacara": "इंद्रिय-सुखों के लोक से संबंधित",
    "nakāmāvacara": "इंद्रिय-सुखों के लोक से संबंधित न होने वाली",
    "rūpāvacara": "सूक्ष्म भौतिक लोक से संबंधित", "narūpāvacara": "सूक्ष्म भौतिक लोक से संबंधित न होने वाली",
    "arūpāvacara": "अभौतिक लोक से संबंधित", "naarūpāvacara": "अभौतिक लोक से संबंधित न होने वाली",
    "pariyāpanna": "अस्तित्व के लोकों में समाई हुई", "apariyāpanna": "अस्तित्व के लोकों में न समाई हुई",
    "niyyānika": "मुक्ति की ओर ले जाने वाली", "aniyyānika": "मुक्ति की ओर न ले जाने वाली",
    "niyata": "निश्चित",
    "sauttara": "सर्वोच्च न होने वाली", "anuttara": "सर्वोच्च",
    "saraṇa": "संघर्ष वाली", "araṇa": "संघर्ष से रहित",
}
LEX["nahetusahetuka"] = f"{LEX['nahetu']}, पर {LEX['sahetuka']}"     # fused "nahetusahetukaṃ" (5-02)
LEX["nahetuahetuka"] = f"{LEX['nahetu']} और {LEX['ahetuka']}"
LEX["asaññojana"] = f"{LEX['saññojana']} न होने वाली"                # "nanoasaññojano" (5-04, as written)
# items of more than one word
MW = {
    ("sukhāya", "vedanāya", "sampayutta"): "सुखद अनुभूति से जुड़ी",
    ("dukkhāya", "vedanāya", "sampayutta"): "दुःखद अनुभूति से जुड़ी",
    ("adukkhamasukhāya", "vedanāya", "sampayutta"): "न दुःखद, न सुखद अनुभूति से जुड़ी",
    ("dassanena", "pahātabba"): "सत्य-दर्शन से छोड़ी जाने वाली",
    ("bhāvanāya", "pahātabba"): "मानसिक अभ्यास से छोड़ी जाने वाली",
    ("nevadassanena", "nabhāvanāya", "pahātabba"): "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़ी जाने वाली",
    ("dassanena", "pahātabbahetuka"): "सत्य-दर्शन से छोड़े जाने वाले मूलों वाली",
    ("bhāvanāya", "pahātabbahetuka"): "मानसिक अभ्यास से छोड़े जाने वाले मूलों वाली",
    ("nevadassanena", "nabhāvanāya", "pahātabbahetuka"):
        "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़े जाने वाले मूलों वाली",
    ("nadassanena", "pahātabba"): "सत्य-दर्शन से न छोड़ी जाने वाली",
    ("nabhāvanāya", "pahātabba"): "मानसिक अभ्यास से न छोड़ी जाने वाली",
    ("nadassanena", "pahātabbahetuka"): "सत्य-दर्शन से छोड़े जाने वाले मूलों से रहित",
    ("nabhāvanāya", "pahātabbahetuka"): "मानसिक अभ्यास से छोड़े जाने वाले मूलों से रहित",
    ("kenaci", "viññeyya"): "किसी एक प्रकार की चेतना से जानी जा सकने वाली",
    ("nakenaci", "viññeyya"): "किसी एक प्रकार की चेतना से न जानी जा सकने वाली",
    ("kenaci", "naviññeyya"): "किसी एक प्रकार की चेतना से न जानी जा सकने वाली",
}
# two-word dyad items "<group>vippayutta <X>" (pi-1: "मन के मैलों से अलग, पर उनका विषय बनने वाली")
VIP_GROUP = {"āsava": "मन के मैलों", "saññojana": "बंधनों", "gantha": "गाँठों", "ogha": "बाढ़ों",
             "yoga": "जकड़नों", "nīvaraṇa": "बाधाओं", "parāmāsa": "ग़लत धारणा", "upādāna": "आसक्ति",
             "kilesa": "क्लेशों"}
VIP_SECOND = {  # second word: (Hindi, positive?)
    "sāsava": ("उनका विषय बनने वाली", True), "anāsava": ("उनका विषय न बनने वाली", False),
    "saññojaniya": ("उनका विषय बनने वाली", True), "asaññojaniya": ("उनका विषय न बनने वाली", False),
    "ganthaniya": ("उनका विषय बनने वाली", True), "aganthaniya": ("उनका विषय न बनने वाली", False),
    "oghaniya": ("उनका विषय बनने वाली", True), "anoghaniya": ("उनका विषय न बनने वाली", False),
    "yoganiya": ("उनका विषय बनने वाली", True), "ayoganiya": ("उनका विषय न बनने वाली", False),
    "nīvaraṇiya": ("उनका विषय बनने वाली", True), "anīvaraṇiya": ("उनका विषय न बनने वाली", False),
    "parāmaṭṭha": ("उसका विषय बनने वाली", True), "aparāmaṭṭha": ("उसका विषय न बनने वाली", False),
    "upādāniya": ("उसका विषय बनने वाली", True), "anupādāniya": ("उसका विषय न बनने वाली", False),
    "saṃkilesika": ("क्लेशों का विषय बनने वाली", True), "asaṃkilesika": ("क्लेशों का विषय न बनने वाली", False),
}
CTX = {"nahetu2": False}   # "nahetu sahetuka" read as ONE dyad item (only inside the nahetusahetuka dyad)


def NEG(h, k=1):
    for _ in range(k):
        h = f"{h} {NA}"
    return h


def strip_na(w):
    """'nanahetu' -> ('hetu', 2) only as far as needed; yields all (rest, count) splits."""
    out, k = [(w, 0)], 0
    while True:
        if w.startswith("na") and len(w) > 3:
            w, k = w[2:], k + 1
        elif w.startswith("no") and len(w) > 3 and k == 0 and False:
            w, k = w[2:], k + 1
        else:
            break
        out.append((w, k))
    return out


def stems(w):
    out = [w]
    for end, rep in (("assa", "a"), ("issa", "i"), ("ussa", "u"), ("aṃ", "a"), ("iṃ", "i"), ("uṃ", "u"),
                     ("ino", "i"), ("o", "a"), ("ī", "i"), ("ū", "u"), ("ā", "a")):
        if w.endswith(end):
            out.append(w[: -len(end)] + rep)
    return out


def word_hi(w):
    """Hindi for one surface word (any case), with generic 'na'/'no' negation. Returns (hindi, base) or None."""
    for st in stems(w):
        if st in LEX:
            return LEX[st], st
    for p in ("na", "no"):
        if w.startswith(p) and len(w) > len(p) + 2:
            r = word_hi(w[len(p):])
            if r:
                return NEG(r[0]), r[1]
    return None


def tokenize_item(p):
    """'Kusalaṃ sāsavañceva no ca āsavaṃ' -> [[word, marker], ...]; marker in (None, 'ca', 'ceva')."""
    toks = []
    for w in p.split():
        lw = w[0].lower() + w[1:]
        if lw in ("ca", "ceva"):
            if not toks:
                raise ValueError(f"leading {lw!r} in {p!r}")
            toks[-1][1] = lw
        elif lw.endswith("ñceva"):
            toks.append([lw[:-5] + "ṃ", "ceva"])
        elif lw.endswith("ñca"):
            toks.append([lw[:-3] + "ṃ", "ca"])
        else:
            toks.append([lw, None])
    # glue a separate "na" to the next word ("na nahetuṃ" -> "nanahetuṃ"), but not "na ca"
    out = []
    i = 0
    while i < len(toks):
        w, m = toks[i]
        if w in ("na", "no") and m is None and i + 1 < len(toks):
            toks[i + 1][0] = w + toks[i + 1][0]
            i += 1
            continue
        out.append(toks[i])
        i += 1
    return out


def atoms(toks, i):
    """Candidate atoms at position i, longest first: (hindi, end_index, positive_base_or_None)."""
    cands = []
    # multi-word items, allowing extra "na" on the first word
    for n in (3, 2):
        if i + n > len(toks) or any(toks[j][1] for j in range(i, i + n - 1)):
            continue
        rest = [stems(toks[j][0]) for j in range(i + 1, i + n)]
        for first, k in strip_na(toks[i][0]):
            hit = None
            for f in stems(first):
                for key, val in MW.items():
                    if len(key) == n and key[0] == f and all(key[j + 1] in rest[j] for j in range(n - 1)):
                        hit = val
            if hit:
                cands.append((NEG(hit, k), i + n, None))
                break
    # two-word dyad items
    if i + 2 <= len(toks) and not toks[i][1]:
        first = stems(toks[i][0])
        second = toks[i + 1][0]
        for g, gh in VIP_GROUP.items():
            if g + "vippayutta" in first:
                for rest, k in strip_na(second):
                    for st in stems(rest):
                        if st in VIP_SECOND:
                            h2, pos = VIP_SECOND[st]
                            j = ", पर " if pos else " और "
                            cands.append((f"{gh} से अलग{j}{NEG(h2, k)}", i + 2, None))
                            break
                    else:
                        continue
                    break
        if CTX["nahetu2"] and "nahetu" in first:
            for rest, k in strip_na(second):
                st = next((s for s in stems(rest) if s in ("sahetuka", "ahetuka")), None)
                if st:
                    j = ", पर " if st == "sahetuka" else " और "
                    cands.append((f"{LEX['nahetu']}{j}{NEG(LEX[st], k)}", i + 2, None))
                    break
    r = word_hi(toks[i][0])
    if r:
        cands.append((r[0], i + 1, r[1]))
    return cands


NEG_TOK = {"na": 0, "no": 0, "nano": 1}


def components(toks, i=0):
    """All parses of toks[i:] into components (generator, longest atoms first)."""
    if i == len(toks):
        yield []
        return
    for h1, j, _ in atoms(toks, i):
        m1 = toks[j - 1][1]
        if m1 == "ceva":
            # "A ceva no ca B" -> "A, पर स्वयं B न होने वाली";  "A ceva B ca" -> "A भी और B भी"
            if j < len(toks) and toks[j][0] in NEG_TOK and toks[j][1] == "ca":
                for h2, k, _ in atoms(toks, j + 1):
                    comp = f"{h1}, पर स्वयं {NEG(h2, 1 + NEG_TOK[toks[j][0]])}"
                    for rest in components(toks, k):
                        yield [comp] + rest
            else:
                for h2, k, _ in atoms(toks, j):
                    if toks[k - 1][1] != "ca" and k != len(toks):   # "hetu ceva sahetuko" (no "ca"): as "ca"
                        continue
                    comp = f"{h1} भी और {h2} भी"
                    for rest in components(toks, k):
                        yield [comp] + rest
        else:
            for rest in components(toks, j):
                yield [h1] + rest


def items(p, n):
    """Pāli item phrase -> list of Hindi items (each = n components joined with ', ')."""
    toks = tokenize_item(p.strip())
    for comps in components(toks):
        if comps and len(comps) % n == 0:
            return [", ".join(comps[i:i + n]) for i in range(0, len(comps), n)]
    raise ValueError(f"cannot parse item phrase {p!r}")


def join_and(xs):
    """'A और B' / 'A, B और C'; when an item has its own 'और' inside, the items are joined with ', तथा '."""
    if len(xs) == 1:
        return xs[0]
    j = ", तथा " if any(" और " in x for x in xs) else " और "
    return ", ".join(xs[:-1]) + j + xs[-1]


def ACC(p, n):        # kusalaṃ sappaccayaṃ dhammaṃ
    return join_and([f"{x} {DH}" for x in items(p, n)])


def NOM(p, n):        # kusalo sappaccayo dhammo / ... ca ... ca dhammā
    xs = items(p, n)
    return (f"{xs[0]} {DH}" if len(xs) == 1 else f"{join_and(xs)} {DH_PL}"), len(xs) > 1


def DAT(p, n):        # kusalassa sappaccayassa dhammassa
    return ACC(p, n) + " के लिए"


# =====================================================================================
# 2. Names of triads, dyads and clusters (headings)
# =====================================================================================
TIKA_LABEL = {  # "<label> वाला तीन का वर्गीकरण": terms fix हितकर / अनुभूति / कर्म-फल; the other
    # triads are named, like the dyads, by their first item: "<first item> परिघटनाओं वाला तीन का वर्गीकरण"
    "kusala": "हितकर", "vedanā": "अनुभूति", "vipāka": "कर्म-फल"}
TIKA_FIRST = {
    "upādinna": "upādinnupādāniya", "saṃkiliṭṭha": "saṃkiliṭṭhasaṃkilesika", "vitakka": "savitakkasavicāra",
    "pīti": "pītisahagata", "dassana": ("dassanena", "pahātabba"), "dassanahetu": ("dassanena", "pahātabbahetuka"),
    "dassanahetuka": ("dassanena", "pahātabbahetuka"), "ācayagāmi": "ācayagāmi", "sekkha": "sekkha",
    "paritta": "paritta", "parittārammaṇa": "parittārammaṇa", "hīna": "hīna", "micchatta": "micchattaniyata",
    "micchattaniyata": "micchattaniyata", "maggārammaṇa": "maggārammaṇa", "uppanna": "uppanna",
    "atīta": "atīta", "atītārammaṇa": "atītārammaṇa", "ajjhatta": "ajjhatta",
    "ajjhattārammaṇa": "ajjhattārammaṇa", "sanidassana": "sanidassanasappaṭigha"}
for _k, _v in TIKA_FIRST.items():
    TIKA_LABEL[_k] = (MW[_v] if isinstance(_v, tuple) else LEX[_v]) + " परिघटनाओं"
DUKA_KA = {  # dyad name = "<first item> परिघटनाओं वाला दो का वर्गीकरण" (Hetuduka: terms "मूल वाला")
    "sahetuka": LEX["sahetuka"], "hetusampayutta": LEX["hetusampayutta"],
    "hetusahetuka": f"{LEX['hetu']} भी और {LEX['sahetuka']} भी",
    "hetuhetusampayutta": f"{LEX['hetu']} भी और {LEX['hetusampayutta']} भी",
    "nahetusahetuka": f"{LEX['nahetu']}, पर {LEX['sahetuka']}",
    "sappaccaya": LEX["sappaccaya"], "saṅkhata": LEX["saṅkhata"], "sanidassana": LEX["sanidassana"],
    "sappaṭigha": LEX["sappaṭigha"], "rūpī": LEX["rūpi"], "lokiya": LEX["lokiya"],
    "kenaciviññeyya": MW[("kenaci", "viññeyya")], "sārammaṇa": LEX["sārammaṇa"], "citta": LEX["citta"],
    "cetasika": LEX["cetasika"], "cittasampayutta": LEX["cittasampayutta"],
    "cittasaṃsaṭṭha": LEX["cittasaṃsaṭṭha"], "cittasamuṭṭhāna": LEX["cittasamuṭṭhāna"],
    "cittasahabhū": LEX["cittasahabhu"], "cittānuparivatti": LEX["cittānuparivatti"],
    "cittasaṃsaṭṭhasamuṭṭhāna": LEX["cittasaṃsaṭṭhasamuṭṭhāna"],
    "cittasaṃsaṭṭhasamuṭṭhānasahabhū": LEX["cittasaṃsaṭṭhasamuṭṭhānasahabhu"],
    "cittasaṃsaṭṭhasamuṭṭhānānuparivatti": LEX["cittasaṃsaṭṭhasamuṭṭhānānuparivatti"],
    "ajjhattika": LEX["ajjhattika"], "upādā": LEX["upādā"], "upādinna": LEX["upādinna"],
    "dassanenapahātabba": MW[("dassanena", "pahātabba")], "bhāvanāyapahātabba": MW[("bhāvanāya", "pahātabba")],
    "dassanenapahātabbahetuka": MW[("dassanena", "pahātabbahetuka")],
    "bhāvanāyapahātabbahetuka": MW[("bhāvanāya", "pahātabbahetuka")],
    "savitakka": LEX["savitakka"], "savicāra": LEX["savicāra"], "sappītika": LEX["sappītika"],
    "pītisahagata": LEX["pītisahagata"], "sukhasahagata": LEX["sukhasahagata"],
    "upekkhāsahagata": LEX["upekkhāsahagata"], "kāmāvacara": LEX["kāmāvacara"],
    "rūpāvacara": LEX["rūpāvacara"], "arūpāvacara": LEX["arūpāvacara"], "pariyāpanna": LEX["pariyāpanna"],
    "niyyānika": LEX["niyyānika"], "niyata": LEX["niyata"], "sauttara": LEX["sauttara"], "saraṇa": LEX["saraṇa"],
}
GOCCHA = {"āsava": ("āsava", "sāsava", "āsavasampayutta", "मन के मैलों"),
          "saññojana": ("saññojana", "saññojaniya", "saññojanasampayutta", "बंधनों"),
          "gantha": ("gantha", "ganthaniya", "ganthasampayutta", "गाँठों"),
          "ogha": ("ogha", None, None, "बाढ़ों"), "yoga": ("yoga", None, None, "जकड़नों"),
          "nīvaraṇa": ("nīvaraṇa", None, None, "बाधाओं"),
          "parāmāsa": ("parāmāsa", "parāmaṭṭha", "parāmāsasampayutta", "ग़लत धारणा"),
          "upādāna": ("upādāna", "upādāniya", "upādānasampayutta", "आसक्ति"),
          "kilesa": ("kilesa", "saṃkilesika", "kilesasampayutta", "मन के क्लेशों")}
for g, (a, b, c, gh) in GOCCHA.items():
    DUKA_KA[g] = LEX[a]
    if b:
        DUKA_KA[b] = LEX[b]
        DUKA_KA[c] = LEX[c]
        DUKA_KA[g + b] = f"{LEX[a]} भी और {LEX[b]} भी"
        DUKA_KA[g + c] = f"{LEX[a]} भी और {LEX[c]} भी"
        DUKA_KA[g + g + "sampayutta"] = DUKA_KA[g + c]
        sec = {"āsava": "sāsava", "kilesa": "saṃkilesika"}.get(g, b)
        DUKA_KA[g + "vippayutta" + sec] = f"{gh} से अलग, पर {VIP_SECOND[sec][0]}"
DUKA_KA["kilesasaṃkiliṭṭha"] = f"{LEX['kilesa']} भी और {LEX['saṃkiliṭṭha']} भी"
DUKA_KA["saṃkiliṭṭha"] = LEX["saṃkiliṭṭha"]
DUKA_KA["kilesavippayuttasaṃkilesika"] = f"मन के क्लेशों से अलग, पर {VIP_SECOND['saṃkilesika'][0]}"
DUKA_KA["kilesavippayuttasaṃkilesika"] = f"क्लेशों से अलग, पर {VIP_SECOND['saṃkilesika'][0]}"
DUKA_KA["āsavavippayuttasāsava"] = f"मन के मैलों से अलग, पर {VIP_SECOND['sāsava'][0]}"

GROUP_NAME = {  # cluster / group headings (pi-1 1-matika.md)
    "hetugocchaka": "मूलों का वर्ग", "cūḷantaraduka": "बीच के छोटे दो-दो के वर्गीकरण",
    "āsavagocchaka": "मन के मैलों का वर्ग", "saññojanagocchaka": "बंधनों का वर्ग",
    "ganthagocchaka": "गाँठों का वर्ग", "oghagocchaka": "बाढ़ों का वर्ग", "yogagocchaka": "जकड़नों का वर्ग",
    "nīvaraṇagocchaka": "बाधाओं का वर्ग", "parāmāsagocchaka": "ग़लत धारणा का वर्ग",
    "mahantaraduka": "बीच के बड़े दो-दो के वर्गीकरण", "upādānagocchaka": "आसक्ति का वर्ग",
    "kilesagocchaka": "मन के क्लेशों का वर्ग", "piṭṭhiduka": "अंतिम दो-दो के वर्गीकरण",
}


def tika_name(stem):
    return S.TIKA(TIKA_LABEL[stem])


def duka_name(stem):
    if stem == "hetu":
        return S.DUKA("मूल")
    return f"{DUKA_KA[stem]} परिघटनाओं वाला दो का वर्गीकरण"


def unit_name(u):
    """Name of one unit given as a lower-case Pāli stem: 'kusalattika', 'hetuduka', 'kilesagocchaka',
    'saññojanādiduka' ..."""
    if u in GROUP_NAME:
        return GROUP_NAME[u]
    if u.endswith("ādiduka"):
        return duka_name(u[:-7] + "a") + " आदि"
    if u.endswith("ttika"):
        return tika_name(u[:-5])
    if u.endswith("duka"):
        return duka_name(u[:-4])
    raise KeyError(u)


def unit_from_heading_word(w):
    """'Kusalattikaṃ' / 'Sappaccayadukaṃ' / 'Oghādidukāni' / 'Upādānagocchakaṃ' -> unit stem."""
    w = w[0].lower() + w[1:]
    for end, rep in (("ādidukāni", "ādiduka"), ("dukāni", "duka"), ("ttikaṃ", "ttika"), ("dukaṃ", "duka"),
                     ("gocchakaṃ", "gocchaka")):
        if w.endswith(end):
            return w[: -len(end)] + rep
    return w


def OBL(name):
    """Oblique of a heading name: '… वाला दो का वर्गीकरण' -> '… वाले दो के वर्गीकरण'."""
    name = re.sub(r" वाला (दो|तीन) का वर्गीकरण", r" वाले \1 के वर्गीकरण", name)
    return re.sub(r" का वर्ग$", " के वर्ग", name)


PADA = {  # "<item> पद" (terms: Kusalapadaṃ = हितकर पद, Sahetukapadaṃ = मूल वाला पद)
    "Lokuttarapadaṃ": "लोकोत्तर पद", "Anāsavapadaṃ": "मन के मैलों का विषय न बनने वाला पद",
    "Avitakkapadaṃ": "आरंभिक विचार से रहित पद", "Appītikapadaṃ": "उल्लास से रहित पद",
    "Nakāmāvacarapadaṃ": "इंद्रिय-सुखों के लोक से संबंधित न होने वाला पद",
    "Apariyāpannapadaṃ": "अस्तित्व के लोकों में न समाया हुआ पद", "Anuttarapadaṃ": "सर्वोच्च पद",
    "Araṇapadaṃ": "संघर्ष से रहित पद", "Ahetukapadaṃ": "मूल से रहित पद", "Sahetukapadaṃ": "मूल वाला पद",
    "Bahiddhāpadaṃ": "दूसरों से संबंधित पद", "Paṇītapadaṃ": "उत्तम पद",
    "Anāgatārammaṇapadaṃ": "भविष्य के विषय वाला पद", "Paccuppannārammaṇapadaṃ": "वर्तमान के विषय वाला पद",
    "Mahaggatādipadāni": "उन्नत आदि पद", "Sukhāyavedanāyasampayuttapadaṃ": "सुखद अनुभूति से जुड़ा पद",
    "Dukkhāyavedanāyasampayuttapadaṃ": "दुःखद अनुभूति से जुड़ा पद",
    "Adukkhamasukhavedanāyasampayuttapadaṃ": "न दुःखद, न सुखद अनुभूति से जुड़ा पद",
}
HEAD = {
    "Paṭiccavārādi": "निर्भरता का खंड आदि", "Paccayacatukkaṃ": "कारणों के चार क्रम",
    "Paccanīyaṃ": S.PACCANIYA, "Paccanīyaṃ –nahetupaccayo": f"{S.PACCANIYA} – {S.NNAME('hetu')}",
    "Pañhāvāro": S.VARA["pañhā"], "Hetu-ārammaṇapaccayā": f"{S.NAME('hetu')} और {S.NAME('ārammaṇa')}",
    "Hetuārammaṇapaccayādi": f"{S.NAME('hetu')}, {S.NAME('ārammaṇa')} आदि",
    "Hetusahajātapaccayādi": f"{S.NAME('hetu')}, {S.NAME('sahajāta')} आदि",
    "(Pañcamo bhāgo)": S.BHAGA[5],
    "Dhammānulome tikatikapaṭṭhānaṃ": f"{S.DHAMMANULOMA}: {S.TIKATIKAPATTHANA}",
    "Dhammānulome dukadukapaṭṭhānaṃ": f"{S.DHAMMANULOMA}: {S.DUKADUKAPATTHANA}",
    "Dhammapaccanīye tikapaṭṭhānaṃ": f"{S.DHAMMAPACCANIYA}: {S.TIKAPATTHANA}",
    "Dhammapaccanīye dukapaṭṭhānaṃ": f"{S.DHAMMAPACCANIYA}: {S.DUKAPATTHANA}",
}
for _k in S.COND_KEYS:
    HEAD[_k[0].upper() + _k[1:] + "paccayo"] = S.NAME(_k)
    HEAD[S.NEG_PREFIX_PALI[_k].capitalize() + _k + "paccayo"] = S.NNAME(_k)


def heading_name(name):
    if name in HEAD:
        return HEAD[name]
    if name in PADA:
        return PADA[name]
    if "-" in name:
        a, b = name.split("-")
        return f"{unit_name(a[0].lower() + a[1:])} और {unit_name(unit_from_heading_word(b))}"
    return unit_name(unit_from_heading_word(name))


def heading(text):
    ital = text.startswith("*") and text.endswith("*")
    core = text.strip("*")
    m = re.match(r"^(\d+(?:\s?-\d+)*\.\s)?(.*)$", core)
    pre, name = m.group(1) or "", m.group(2)
    h = pre + heading_name(name)
    return f"*{h}*" if ital else h


# closing lines "<X> niṭṭhitaṃ."
END = {
    "Kusalattikacūḷantaradukaṃ": f"{tika_name('kusala')} और {GROUP_NAME['cūḷantaraduka']}",
    "Kusalattikaāsavagocchakaṃ": f"{tika_name('kusala')} और {GROUP_NAME['āsavagocchaka']}",
    "Kusalattikamahantaradukaṃ": f"{tika_name('kusala')} और {GROUP_NAME['mahantaraduka']}",
    "Kusalattikaupādānagocchakaṃ": f"{tika_name('kusala')} और {GROUP_NAME['upādānagocchaka']}",
    "Kusalattikakilesagocchakaṃ": f"{tika_name('kusala')} और {GROUP_NAME['kilesagocchaka']}",
    "Kusalattikapiṭṭhidukaṃ": f"{tika_name('kusala')} और {GROUP_NAME['piṭṭhiduka']}",
    "Sanidassanattikasaraṇadukaṃ": f"{tika_name('sanidassana')} और {duka_name('saraṇa')}",
    "Kusalattikasanidassanattikaṃ": f"{tika_name('kusala')} और {tika_name('sanidassana')}",
    "Hetudukaāsavagocchakaṃ": f"{duka_name('hetu')} और {GROUP_NAME['āsavagocchaka']}",
    "Hetudukaparāmāsagocchakaṃ": f"{duka_name('hetu')} और {GROUP_NAME['parāmāsagocchaka']}",
    "Hetudukamahantaradukaṃ": f"{duka_name('hetu')} और {GROUP_NAME['mahantaraduka']}",
    "Hetudukapiṭṭhidukaṃ": f"{duka_name('hetu')} और {GROUP_NAME['piṭṭhiduka']}",
    "Dhammānulome tikadukapaṭṭhānaṃ": f"{S.DHAMMANULOMA}: {S.TIKADUKAPATTHANA}",
    "Dhammānulome tikatikapaṭṭhānaṃ": f"{S.DHAMMANULOMA}: {S.TIKATIKAPATTHANA}",
    "Dhammānulome dukadukapaṭṭhānaṃ": f"{S.DHAMMANULOMA}: {S.DUKADUKAPATTHANA}",
    "Dhammapaccanīye tikapaṭṭhānaṃ": f"{S.DHAMMAPACCANIYA}: {S.TIKAPATTHANA}",
    "Dhammapaccanīye dukapaṭṭhānaṃ": f"{S.DHAMMAPACCANIYA}: {S.DUKAPATTHANA}",
    "Anulomapaṭṭhānaṃ": f"{S.ANULOMA} के कारण-संबंध",
}
for _g in ("hetu", "āsava", "saññojana", "gantha", "nīvaraṇa", "parāmāsa"):
    END[_g.capitalize() + "gocchakaṃ"] = GROUP_NAME[_g + "gocchaka"]
END["Āsavagocchakaṃ"] = GROUP_NAME["āsavagocchaka"]
END["Cūḷantaradukaṃ"] = GROUP_NAME["cūḷantaraduka"]
END["Mahantaradukaṃ"] = GROUP_NAME["mahantaraduka"]
END["Piṭṭhidukaṃ"] = GROUP_NAME["piṭṭhiduka"]

# =====================================================================================
# 3. Notes in brackets
# =====================================================================================
VARA_STEM = {"sahajāta": "सह-उत्पत्ति", "paccaya": "कारण", "nissaya": "आश्रय", "saṃsaṭṭha": "घुले-मिले होने",
             "sampayutta": "जुड़ाव", "pañhā": "प्रश्नों", "paṭicca": "निर्भरता"}
NUMWORDS = "|".join(sorted(S.NUM, key=len, reverse=True))
VLIST = (r"(?P<list>(?:[Ss]ahajāta|[Pp]accaya|[Nn]issaya|[Ss]aṃsaṭṭha|[Ss]ampayutta|[Pp]añhā|[Pp]aṭicca)"
         r"vār(?:am|e)pi(?:(?:\s*…pe…\s*|,?\s+)(?:sahajāta|paccaya|nissaya|saṃsaṭṭha|sampayutta|pañhā|paṭicca)"
         r"vār(?:am|e)pi)*)")
VPRED = (r"\s*(?P<pred>paṭiccavārasadisaṃ, evaṃ vitthāretabbaṃ|paṭiccavārasadisaṃ evaṃ vitthāretabbaṃ"
         r"|paṭiccavārasadisaṃ vitthāretabbaṃ|paṭiccavārasadisaṃ|sabbattha vitthāretabbaṃ|evaṃ vitthāretabbaṃ"
         r"|vitthāretabbaṃ|sabbattha vitthāro|tattakāva pañhā|sabbattha (?:" + NUMWORDS + r"))")
VARA_RX = re.compile(VLIST + VPRED)


def vara_clause(m):
    lst, pred = m.group("list"), m.group("pred")
    loc = "vārepi" in lst
    if pred.startswith("paṭiccavārasadisaṃ") and pred != "paṭiccavārasadisaṃ, evaṃ vitthāretabbaṃ" \
            and pred != "paṭiccavārasadisaṃ":
        form = "acc"
    elif "vitthāretabbaṃ" in pred and pred != "paṭiccavārasadisaṃ, evaṃ vitthāretabbaṃ":
        form = "loc" if loc else "acc"
    else:
        form = "loc" if loc else "nom"
    suffix = {"nom": "का खंड भी", "acc": "के खंड का भी", "loc": "के खंड में भी"}[form]
    parts = re.split(r"((?:\s*…pe…\s*|,?\s+))", lst)
    out = ""
    for p in parts:
        if not p:
            continue
        mm = re.fullmatch(r"(\w+?)vār(?:am|e)pi", p)
        if mm:
            st = mm.group(1)
            out += f"{VARA_STEM[st[0].lower() + st[1:]]} {suffix}"
        else:
            out += ", " if "…pe…" not in p else p.replace("…pe…", "…")
    P = {"paṭiccavārasadisaṃ, evaṃ vitthāretabbaṃ": "निर्भरता के खंड के समान है, इसी तरह विस्तार करना चाहिए",
         "paṭiccavārasadisaṃ evaṃ vitthāretabbaṃ": "निर्भरता के खंड के समान इसी तरह विस्तार करना चाहिए",
         "paṭiccavārasadisaṃ vitthāretabbaṃ": "निर्भरता के खंड के समान विस्तार करना चाहिए",
         "paṭiccavārasadisaṃ": "निर्भरता के खंड के समान है",
         "sabbattha vitthāretabbaṃ": "हर जगह विस्तार करना चाहिए", "evaṃ vitthāretabbaṃ": "इसी तरह विस्तार करना चाहिए",
         "vitthāretabbaṃ": "विस्तार करना चाहिए", "sabbattha vitthāro": "हर जगह विस्तार",
         "tattakāva pañhā": "उतने ही प्रश्न"}
    ph = P.get(pred) or f"हर जगह {S.NUM[pred.split()[1]]}"
    return f"{out} {ph}"


YATHA_K = f"जैसे {OBL(tika_name('kusala'))} में"
NOTE_LIT = [  # literal clauses (Pāli -> Hindi), longest first
    ("Yathā kusalattike pañhāvārassa anulomampi paccanīyampi anulomapaccanīyampi paccanīyānulomampi gaṇitaṃ "
     "evaṃ gaṇetabbaṃ",
     f"{YATHA_K} प्रश्नों के खंड के {S.ANULOMA} की भी, {S.PACCANIYA} की भी, {S.ANULOMAPACCANIYA} की भी और "
     f"{S.PACCANIYANULOMA} की भी गणना की गई है, वैसे ही गिनना चाहिए"),
    ("Yathā kusalattike sahajātavārampi paccayavārampi nissayavārampi saṃsaṭṭhavārampi sampayuttavārampi "
     "pañhāvārampi gaṇitaṃ evaṃ gaṇetabbaṃ",
     f"{YATHA_K} " + ", ".join(f"{VARA_STEM[v]} के खंड की भी" for v in
                               ("sahajāta", "paccaya", "nissaya", "saṃsaṭṭha", "sampayutta", "pañhā"))
     + " गणना की गई है, वैसे ही गिनना चाहिए"),
    ("Yathā kusalattike pañhāvāraṃ, evaṃ vitthāretabbaṃ",
     f"{YATHA_K} प्रश्नों के खंड का, वैसे ही विस्तार करना चाहिए"),
    ("Yathā kusalattike pañhāvāraṃ evaṃ vitthāretabbaṃ",
     f"{YATHA_K} प्रश्नों के खंड का, वैसे ही विस्तार करना चाहिए"),
    ("Pañhāvārampi evaṃ vitthāretabbaṃ", f"प्रश्नों के खंड का भी इसी तरह विस्तार करना चाहिए"),
    ("oghagocchakayogagocchakesu āmasanaṃ āsavagocchake āmasanasadisaṃ",
     f"{OBL(GROUP_NAME['oghagocchaka'])} और {OBL(GROUP_NAME['yogagocchaka'])} में उल्लेख "
     f"{OBL(GROUP_NAME['āsavagocchaka'])} में उल्लेख के समान है"),
    ("Nīvaraṇagocchake āmasanaṃ saññojanagocchake āmasanasadisaṃ",
     f"{OBL(GROUP_NAME['nīvaraṇagocchaka'])} में उल्लेख {OBL(GROUP_NAME['saññojanagocchaka'])} में उल्लेख "
     f"के समान है"),
    ("Paccanīyadukamattāni na vattabbaṃ dhammaṃ pūretuṃ nava nava pañhāni karotu",
     f"केवल {S.PACCANIYA} के {S.DUKA_PL}; न कहने योग्य परिघटना को पूरा करने के लिए नौ-नौ प्रश्न बनाए जाएँ"),
    ("upādānagocchakaṃ vitthāretabbaṃ", f"{OBL(GROUP_NAME['upādānagocchaka'])} का विस्तार करना चाहिए"),
    ("sabbattha gocchakaṃ vitthāretabbaṃ", "हर जगह वर्ग का विस्तार करना चाहिए"),
    ("yāva mahābhūtā", "महाभूतों तक"),
    ("vipākaṃ natthi", f"{S.NAME('vipāka')} नहीं है"),
    ("Pañcamo bhāgo", S.BHAGA[5].strip("()")),
]
SADISA_OF = {  # "<X>sadisaṃ" -> "<X> के समान"
    "sappaccayaduka": OBL(duka_name("sappaccaya")), "Sappaccayaduka": OBL(duka_name("sappaccaya")),
    "kenaciviññeyya": OBL(duka_name("kenaciviññeyya")),
    "kusalasavitakka": f"{LEX['kusala']}, {LEX['savitakka']} परिघटना",
    "rūpāvacaraduka": OBL(duka_name("rūpāvacara")), "saṃkiliṭṭhaduka": OBL(duka_name("saṃkiliṭṭha")),
    "Āsavagocchaka": OBL(GROUP_NAME["āsavagocchaka"]),
}
NOTE_RX = [
    (VARA_RX, vara_clause),
    (re.compile(r"[Ss]aṃkhittaṃ"), lambda m: "संक्षिप्त"),
    (re.compile(r"[Ss]abbattha vitthāretabbaṃ"), lambda m: "हर जगह विस्तार करना चाहिए"),
    (re.compile(r"[Ss]abbattha vitthāro"), lambda m: "हर जगह विस्तार"),
    (re.compile(r"[Ss]abbattha (" + NUMWORDS + r")"), lambda m: f"हर जगह {S.NUM[m.group(1)]}"),
    (re.compile(r"(\w+)sadisaṃ"), lambda m: f"{SADISA_OF[m.group(1)]} के समान"),
    (re.compile(r"(" + NUMWORDS + r")\b"), lambda m: S.NUM[m.group(1)]),
]


def note(c):
    out, pos = "", 0
    while pos < len(c):
        for lit, hi in NOTE_LIT:
            if c.startswith(lit, pos):
                out += hi
                pos += len(lit)
                break
        else:
            for rx, fn in NOTE_RX:
                m = rx.match(c, pos)
                if m:
                    out += fn(m)
                    pos = m.end()
                    break
            else:
                if c.startswith("…pe…", pos):
                    out, pos = out + "…", pos + 4
                elif c[pos] == ".":
                    out, pos = out + "।", pos + 1
                elif c[pos] in ", ":
                    out, pos = out + c[pos], pos + 1
                else:
                    raise ValueError(f"note: cannot read {c[pos:pos + 50]!r} in ({c})")
    return out


# =====================================================================================
# 4. Explanations after "–" (paccanīya files)
# =====================================================================================
AKU_ABY_SG = f"{S.T['a']} या {S.T['ab']} एक समूह"
MOHA_VU_OBL = S.MOHA_VU.replace("होने वाला", "होने वाले")   # "... mohaṃ paṭicca": oblique before "पर"
EXPL = {
    "akusalaṃ abyākataṃ ekaṃ khandhaṃ paṭicca akusalā abyākatā tayo khandhā cittasamuṭṭhānañca rūpaṃ…pe… "
    "dve khandhe paṭicca dve khandhā cittasamuṭṭhānañca rūpaṃ":
        f"{AKU_ABY_SG} पर निर्भर होकर {S.T['a']} और {S.T['ab']} तीन समूह {S.AND_CSR}… "
        f"दो समूहों पर निर्भर होकर दो समूह {S.AND_CSR}",
    "nahetuṃ ekaṃ khandhaṃ paṭicca tayo khandhā cittasamuṭṭhānañca rūpaṃ…pe… dve khandhe paṭicca dve khandhā "
    "cittasamuṭṭhānañca rūpaṃ; paṭisandhikkhaṇe…pe… (yāva mahābhūtā)":
        f"मूल रूपी न होने वाले एक समूह पर निर्भर होकर तीन समूह {S.AND_CSR}… दो समूहों पर निर्भर होकर दो समूह "
        f"{S.AND_CSR}; {S.PATISANDHI}… (महाभूतों तक)",
    "nahetū khandhe paṭicca hetū; paṭisandhikkhaṇe":
        f"मूल रूपी न होने वाले समूहों पर निर्भर होकर मूल; {S.PATISANDHI}",
    "vicikicchāsahagataṃ uddhaccasahagataṃ mohaṃ paṭicca cittasamuṭṭhānaṃ rūpaṃ, ekaṃ mahābhūtaṃ paṭicca tayo "
    "mahābhūtā…pe… dve mahābhūte paṭicca dve mahābhūtā, mahābhūte paṭicca cittasamuṭṭhānaṃ rūpaṃ kaṭattārūpaṃ "
    "upādārūpaṃ":
        f"{MOHA_VU_OBL} पर निर्भर होकर {S.CSR}, {S.MB13()}… दो महाभूतों पर निर्भर होकर दो महाभूत, "
        f"{S.MBE(S.CSR + ', ' + S.KTR + ', ' + S.UPR)}",
    "vicikicchāsahagataṃ uddhaccasahagataṃ mohaṃ paṭicca sampayuttakā khandhā; paṭisandhikkhaṇe vatthuṃ paṭicca "
    "sahetukā khandhā":
        f"{MOHA_VU_OBL} पर निर्भर होकर जुड़े हुए समूह; {S.PATISANDHI} आधार पर निर्भर होकर मूल वाले समूह",
    "ekaṃ mahābhūtaṃ paṭicca tayo mahābhūtā": S.MB13(),
    "paṭisandhikkhaṇe vatthuṃ paṭicca nahetusahetukā khandhā":
        f"{S.PATISANDHI} आधार पर निर्भर होकर मूल रूपी न होने वाले, पर मूल वाले समूह",
    "cittaṃ paṭicca cittasamuṭṭhānaṃ rūpaṃ": f"मन पर निर्भर होकर {S.CSR}",
    "cittaṃ paṭicca cittasampayuttakā khandhā": "मन पर निर्भर होकर मन से जुड़े हुए समूह",
    "paṭisandhikkhaṇe cittaṃ paṭicca ajjhattikaṃ kaṭattārūpaṃ":
        f"{S.PATISANDHI} मन पर निर्भर होकर किए गए कर्म से उत्पन्न आंतरिक भौतिक रूप",
}

# =====================================================================================
# 5. Line translator
# =====================================================================================
ITEM = r"[^\s.…–;()?,][^.…–;()?]*?"
CONDS = r"(?:(?:na|no)?(?:" + "|".join(sorted(S.COND_KEYS, key=len, reverse=True)) + r")paccayā)"
PAT_RX0 = re.compile(rf"(?P<acc>{ITEM}) dhammaṃ paṭicca (?P<nom>{ITEM}) (?:dhammo|dhammā) "
                     rf"(?P<v>uppajjati|uppajjanti) (?P<c>{CONDS}(?: {CONDS})*)")
PAN_RX0 = re.compile(rf"(?P<src>{ITEM}) (?:dhammo|dhammā) (?P<dst>{ITEM}) dhammassa "
                     rf"(?P<k>[a-zāīūñṭḍṇḷṃ]+?)paccayena paccayo")
# fallback: "vipākadhammadhammaṃ" carries its own "dhammaṃ" (no separate word)
PAT_RX = re.compile(rf"(?P<acc>{ITEM})(?: dhammaṃ|(?<=dhammadhammaṃ)) paṭicca "
                    rf"(?P<nom>{ITEM})(?: (?:dhammo|dhammā)|(?<=dhammadhammo)) "
                    rf"(?P<v>uppajjati|uppajjanti) (?P<c>{CONDS}(?: {CONDS})*)")
PAN_RX = re.compile(rf"(?P<src>{ITEM})(?: (?:dhammo|dhammā)|(?<=dhammadhammo)) "
                    rf"(?P<dst>{ITEM})(?: dhammassa|(?<=dhammadhammassa)) "
                    rf"(?P<k>[a-zāīūñṭḍṇḷṃ]+?)paccayena paccayo")
SLIPS = {"āmammaṇe": "ārammaṇe"}   # pure spelling slips, rendered as the word meant (listed in the notes)
CONT_RX = re.compile(r"(?P<k>[a-zāīūñṭḍṇḷṃ]+?)paccayena paccayo")
FRAG_PAT_RX = re.compile(rf"(?P<acc>{ITEM}) dhammaṃ paṭicca(?=…| …|\.|$)")
FRAG_ACC_RX = re.compile(rf"(?P<acc>{ITEM}) dhammaṃ(?=…)")
ABL_RX = re.compile(CONDS)
_LOCS = sorted(set(S.COND_LOC_PALI.values()), key=len, reverse=True)
CW = (r"(?:(?:[Nn]a|[Nn]o) ?)?(?:(?:" + "|".join(_LOCS) + r")|(?:" +
      "|".join(sorted(S.COND_KEYS, key=len, reverse=True)) + r")paccayā)")
CW = r"(?:" + CW + r"|(?:[A-ZĀ][a-zāīūñṭḍṇḷṃ]*?))"   # capitalised first word is checked by count_hi
NUMW = r"(?:" + "|".join(sorted(list(S.NUM) + [w.capitalize() for w in S.NUM], key=len, reverse=True)) + r")"
LOCW = r"(?:(?:[Nn]a|[Nn]o) ?)?(?:" + "|".join(_LOCS + [l.capitalize() for l in _LOCS]) + r")"
ABLW = (r"(?:(?:[Nn]a|[Nn]o)?(?:" + "|".join(sorted(S.COND_KEYS + [k.capitalize() for k in S.COND_KEYS],
                                                     key=len, reverse=True)) + r")paccayā)")
CWORD = rf"(?:{LOCW}|{ABLW}|{NUMW})(?![\wāīūñṭḍṇḷṃ])"
COUNT_RX = re.compile(rf"{CWORD}(?:(?:, | |…pe… ?|… ?){CWORD})*")
NUMONLY_RX = re.compile(rf"{NUMW}(?![\wāīūñṭḍṇḷṃ])")


def conds_hi(c):
    ks = []
    for t in c.split():
        neg = t.startswith(("na", "no")) and t[2:-7] in S.COND_KEYS
        k = t[2:-7] if neg else t[:-7]
        ks.append(("-" if neg else "") + k)
    return S.CH(*ks)


class Line:
    def __init__(self, n):
        self.n = n
        self.plural = False

    def pat(self, m):
        acc = ACC(m.group("acc"), self.n)
        nom, _ = NOM(m.group("nom"), self.n)
        verb = "उत्पन्न होती हैं" if m.group("v") == "uppajjanti" else "उत्पन्न होती है"
        return f"{acc} {S.DEP['paṭicca']} {nom} {conds_hi(m.group('c'))} {verb}"

    def pan(self, m):
        src, pl = NOM(m.group("src"), self.n)
        self.plural = pl
        dst = DAT(m.group("dst"), self.n)
        return f"{src}, {dst} {S.INS(m.group('k'))} {'होती हैं' if pl else 'होती है'}"

    def cont(self, m):
        return f"{S.INS(m.group('k'))} {'होती हैं' if self.plural else 'होती है'}"

    def tr(self, s):
        out, pos = "", 0
        while pos < len(s):
            ch = s[pos]
            m = PAT_RX0.match(s, pos) or PAT_RX.match(s, pos)
            if m:
                out += self.pat(m)
                pos = m.end()
                continue
            m = PAN_RX0.match(s, pos) or PAN_RX.match(s, pos)
            if m:
                out += self.pan(m)
                pos = m.end()
                continue
            m = CONT_RX.match(s, pos)
            if m and m.group("k") in S.COND_KEYS:
                out += self.cont(m)
                pos = m.end()
                continue
            m = FRAG_PAT_RX.match(s, pos)
            if m and not COUNT_RX.match(s, pos):
                out += f"{ACC(m.group('acc'), self.n)} {S.DEP['paṭicca']}"
                pos = m.end()
                continue
            m = FRAG_ACC_RX.match(s, pos)
            if m and not COUNT_RX.match(s, pos):
                out += ACC(m.group("acc"), self.n)
                pos = m.end()
                continue
            if s.startswith("– ", pos):
                for k in sorted(EXPL, key=len, reverse=True):
                    if s.startswith(k, pos + 2):
                        out += "– " + EXPL[k]
                        pos += 2 + len(k)
                        break
                else:
                    raise ValueError(f"explanation not in EXPL: {s[pos:pos + 120]!r}")
                continue
            if ch == "(":
                end = s.index(")", pos)
                c = s[pos + 1:end]
                out += "(" + (c if re.fullmatch(r"\d+", c) else note(c)) + ")"
                pos = end + 1
                continue
            m = COUNT_RX.match(s, pos)
            if m:
                run = m.group(0).rstrip()
                if ABL_RX.fullmatch(run[0].lower() + run[1:]):
                    out += S.ABL(run[0].lower() + run[1:-7])
                else:
                    out += S.count_hi(run)
                pos += len(run)
                continue
            if s.startswith("…pe…", pos):
                out, pos = out + "…", pos + 4
                continue
            if ch == ".":
                out, pos = out + "।", pos + 1
                continue
            if ch in " ,;…":
                out, pos = out + ch, pos + 1
                continue
            m = re.match(r"(.+?) niṭṭhit(?:aṃ|o)\.", s[pos:])
            if m and m.group(1) in END:
                out += f"{END[m.group(1)]} समाप्त।"
                pos += m.end()
                continue
            if s.startswith("Catuttho bhāgo niṭṭhito.", pos):
                out += "चौथा भाग समाप्त।"
                pos += len("Catuttho bhāgo niṭṭhito.")
                continue
            raise ValueError(f"cannot read at {s[pos:pos + 100]!r}")
        return out


# whole-line overrides (lines the frames cannot read; built from the same pieces)
def _items_list(*xs):
    return "… ".join(xs)


OVERRIDE = {
    "Akusalaṃ saññojanaṃ dhammaṃ paṭicca…pe… akusalaṃ ganthaṃ… oghaṃ… yogaṃ… nīvaraṇaṃ….":
        f"{S.T['a']}, {LEX['saññojana']} {DH} {S.DEP['paṭicca']}… {S.T['a']}, {LEX['gantha']}… "
        f"{LEX['ogha']}… {LEX['yoga']}… {LEX['nīvaraṇa']}…।",
    "Diṭṭhiṃ paṭicca diṭṭhi na uppajjati.": "दृष्टि पर निर्भर होकर दृष्टि उत्पन्न नहीं होती।",
    "Kusalattike cha gocchakaṃ niṭṭhitaṃ.": f"{OBL(tika_name('kusala'))} में छह वर्ग समाप्त।",
}


def tr_line(s, n):
    for a, b in SLIPS.items():
        s = s.replace(a, b)
    if s in OVERRIDE:
        return OVERRIDE[s]
    # a line may start with an override sentence followed by normal text
    for k, v in OVERRIDE.items():
        if s.endswith(" " + k):
            return Line(n).tr(s[: -len(k) - 1]) + " " + v
    return Line(n).tr(s)


# =====================================================================================
# 6. File assembly
# =====================================================================================
def ncomp(fname):
    for k, v in NCOMP.items():
        if fname.startswith(k):
            return v
    raise KeyError(fname)


def build(fname):
    pali = (S.PALI_DIR / fname).read_text(encoding="utf-8")
    n = ncomp(fname)
    H, errs = [], []
    for ln, line in enumerate(pali.splitlines(), 1):
        if not line.strip():
            continue
        body = S.ID_RX.sub("", line)
        try:
            if body.startswith("#"):
                hashes = body[: len(body) - len(body.lstrip("#"))]
                text = body[len(hashes):].strip()
                if "duka" in text.lower():
                    CTX["nahetu2"] = "nahetusahetuka" in text.lower()
                H.append(f"{hashes} {heading(text)}")
            else:
                H.append(tr_line(body, n))
        except (ValueError, KeyError, IndexError) as e:
            errs.append(f"{fname}:{ln}: {type(e).__name__}: {e}")
            H.append("??")
    return pali, H, errs


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry" in sys.argv
    files = [f for f in FILES if not args or any(f.startswith(a) for a in args)]
    total = 0
    for f in files:
        pali, H, errs = build(f)
        total += len(errs)
        for e in errs[:40]:
            print(e)
        if len(errs) > 40:
            print(f"... {len(errs) - 40} more")
        if not errs and not dry:
            text = S.assemble(pali, H)
            (S.HI_DIR / f).write_bytes(text.encode("utf-8"))
            print(f"wrote {f}")
        elif not errs:
            print(f"ok {f}")
    print("errors:", total)


if __name__ == "__main__":
    main()
