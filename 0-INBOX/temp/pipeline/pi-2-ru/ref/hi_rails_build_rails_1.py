"""Builder for the Hindi rails translation of pi-2 chapter 1 (Khandhavibhaṅga), plain audience.

The output starts with sample-1/1-sample.md byte for byte (through ^2-33) and continues from
"##### Vedanākkhandho ^2-1-2-2-0" to the end of the chapter (Abhidhammabhājanīya for the four
mental aggregates, then the Pañhāpucchaka).

Constants come from build_rails_sample.py (imported read-only). The Abhidhammabhājanīya lines are
translated by a rule-based formula translator (identical Pāli -> identical Hindi); the
Pañhāpucchaka lines are composed from the same item table with the pi-1 rails frames
(«कभी … होता है», «… को नहीं कहा जा सकता – न “…”, न “…”»).

usage: python -I -X utf8 build_rails_1.py
"""
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-hi\rails")
import build_rails_sample as S  # noqa: E402  (read-only import)

SRC = S.PALI / "1-khandhavibhango.md"
TARGET = S.OUT / "1-khandhavibhango.md"
SAMPLE_HI = S.SAMPLE / "1-sample.md"

KH = S.KH
KHP = {"rūpakkhandho": "rupa", "vedanākkhandho": "vedana", "saññākkhandho": "sanna",
       "saṅkhārakkhandho": "sankhara", "viññāṇakkhandho": "vinnana"}
SENSE = {"cakkhu": "आँख", "sota": "कान", "ghāna": "नाक", "jivhā": "जीभ", "kāya": "शरीर", "mano": "मन"}
NUMW = {"eka": 1, "du": 2, "ti": 3, "catub": 4, "pañca": 5, "chab": 6, "satta": 7, "aṭṭha": 8,
        "nava": 9, "dasa": 10, "ekādasa": 11, "catuvīsati": 24, "tiṃsa": 30, "tiṃsati": 30, "bahu": "bahu"}
APARO = "दूसरी तरह से भी"  # Aparopi (no termbase entry)
SLIPS = []  # source slips noticed while translating (printed at the end)

# =========================================================================== item table (masc. sg.)
ITEMS = {
    # predicates used without atthi
    "phassasampayutto": "संपर्क से जुड़ा", "cittasampayutto": "मन से जुड़ा",
    # kusala triad and spheres
    "kusalo": "हितकर", "akusalo": "हानिकर", "abyākato": "नैतिक रूप से अनिर्धारित",
    "kāmāvacaro": "इंद्रिय-सुखों के लोक से संबंधित", "rūpāvacaro": "सूक्ष्म भौतिक लोक से संबंधित",
    "arūpāvacaro": "अभौतिक लोक से संबंधित",
    "na kāmāvacaro": "इंद्रिय-सुखों के लोक से संबंधित न होने वाला",
    "na rūpāvacaro": "सूक्ष्म भौतिक लोक से संबंधित न होने वाला",
    "na arūpāvacaro": "अभौतिक लोक से संबंधित न होने वाला",
    "pariyāpanno": "अस्तित्व के लोकों में समाया हुआ", "apariyāpanno": "अस्तित्व के लोकों में न समाया हुआ",
    # faculties
    "sukhindriyaṃ": "सुख की क्षमता", "dukkhindriyaṃ": "दुःख की क्षमता", "somanassindriyaṃ": "प्रसन्नता की क्षमता",
    "domanassindriyaṃ": "उदासी की क्षमता", "upekkhindriyaṃ": "समभाव की क्षमता",
    "sukhindriyasampayutto": "सुख की क्षमता से जुड़ा", "dukkhindriyasampayutto": "दुःख की क्षमता से जुड़ा",
    "somanassindriyasampayutto": "प्रसन्नता की क्षमता से जुड़ा",
    "domanassindriyasampayutto": "उदासी की क्षमता से जुड़ा", "upekkhindriyasampayutto": "समभाव की क्षमता से जुड़ा",
    # said of feminine / neuter nouns after a list
    "sukhā": "सुखद", "dukkhā": "दुःखद", "kusalā": "हितकर", "akusalā": "हानिकर", "abyākatā": "नैतिक रूप से अनिर्धारित",
    "kusalaṃ": "हितकर", "akusalaṃ": "हानिकर", "abyākataṃ": "नैतिक रूप से अनिर्धारित",
    "sukhasahagatā": "सुख के साथ होने वाला", "dukkhasahagatā": "दुःख के साथ होने वाला",
    "sukhasahagataṃ": "सुख के साथ होने वाला", "dukkhasahagataṃ": "दुःख के साथ होने वाला",
    # triads
    "sukhāya vedanāya sampayutto": "सुखद अनुभूति से जुड़ा", "dukkhāya vedanāya sampayutto": "दुःखद अनुभूति से जुड़ा",
    "adukkhamasukhāya vedanāya sampayutto": "न दुःखद, न सुखद अनुभूति से जुड़ा",
    "vipāko": "कर्म-फल रूपी", "vipākadhammadhammo": "कर्म-फल उत्पन्न करने वाला",
    "nevavipākanavipākadhammadhammo": "न कर्म-फल रूपी, न कर्म-फल उत्पन्न करने वाला",
    "upādinnupādāniyo": S.UPADINNA_UPA, "anupādinnupādāniyo": S.ANUPADINNA_UPA,
    "anupādinnaanupādāniyo": "न कर्म से उत्पन्न, न आसक्ति का विषय बनने वाला",
    "saṃkiliṭṭhasaṃkilesiko": "क्लेशों से मलिन और क्लेशों का विषय बनने वाला",
    "asaṃkiliṭṭhasaṃkilesiko": "क्लेशों से मलिन न होने वाला, पर क्लेशों का विषय बनने वाला",
    "asaṃkiliṭṭhaasaṃkilesiko": "क्लेशों से मलिन न होने वाला और क्लेशों का विषय न बनने वाला",
    "savitakkasavicāro": "आरंभिक विचार और सतत विचार वाला",
    "avitakkavicāramatto": "आरंभिक विचार से रहित, केवल सतत विचार वाला",
    "avitakkaavicāro": "आरंभिक विचार और सतत विचार दोनों से रहित",
    "pītisahagato": "उल्लास के साथ होने वाला", "sukhasahagato": "सुख के साथ होने वाला",
    "upekkhāsahagato": "समभाव के साथ होने वाला",
    "na pītisahagato": "उल्लास के साथ न होने वाला", "na sukhasahagato": "सुख के साथ न होने वाला",
    "na upekkhāsahagato": "समभाव के साथ न होने वाला",
    "dassanena pahātabbo": "सत्य-दर्शन से छोड़ा जाने वाला", "bhāvanāya pahātabbo": "मानसिक अभ्यास से छोड़ा जाने वाला",
    "neva dassanena na bhāvanāya pahātabbo": "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़ा जाने वाला",
    "dassanena pahātabbahetuko": "सत्य-दर्शन से छोड़े जाने वाले मूलों वाला",
    "bhāvanāya pahātabbahetuko": "मानसिक अभ्यास से छोड़े जाने वाले मूलों वाला",
    "neva dassanena na bhāvanāya pahātabbahetuko": "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़े जाने वाले मूलों वाला",
    "na dassanena pahātabbo": "सत्य-दर्शन से न छोड़ा जाने वाला", "na bhāvanāya pahātabbo": "मानसिक अभ्यास से न छोड़ा जाने वाला",
    "na dassanena pahātabbahetuko": "सत्य-दर्शन से छोड़े जाने वाले मूलों से रहित",
    "na bhāvanāya pahātabbahetuko": "मानसिक अभ्यास से छोड़े जाने वाले मूलों से रहित",
    "ācayagāmī": "संचय की ओर ले जाने वाला", "apacayagāmī": "संचय घटाने की ओर ले जाने वाला",
    "nevācayagāmināpacayagāmī": "न संचय की ओर, न संचय घटाने की ओर ले जाने वाला",
    "sekkho": "सीखने के चरण का", "asekkho": "सीखना पूरा होने के चरण का",
    "nevasekkhanāsekkho": "न सीखने के चरण का, न सीखना पूरा होने के चरण का",
    "paritto": "सीमित", "mahaggato": "उन्नत", "appamāṇo": "अपरिमित",
    "parittārammaṇo": "सीमित विषय वाला", "mahaggatārammaṇo": "उन्नत विषय वाला", "appamāṇārammaṇo": "अपरिमित विषय वाला",
    "hīno": "हीन", "majjhimo": "मध्यम", "paṇīto": "उत्तम",
    "micchattaniyato": "ग़लत दिशा में निश्चित", "sammattaniyato": "सही दिशा में निश्चित", "aniyato": "अनिश्चित",
    "niyato": "निश्चित",
    "maggārammaṇo": "मार्ग को विषय बनाने वाला", "maggahetuko": "मार्ग को मूल बनाने वाला",
    "maggādhipati": "मार्ग की प्रधानता वाला",
    "uppanno": "उत्पन्न हो चुका", "anuppanno": "उत्पन्न न हुआ", "uppādī": "उत्पन्न होने वाला",
    "atīto": "अतीत का", "anāgato": "भविष्य का", "paccuppanno": "वर्तमान का",
    "atītārammaṇo": "अतीत के विषय वाला", "anāgatārammaṇo": "भविष्य के विषय वाला",
    "paccuppannārammaṇo": "वर्तमान के विषय वाला",
    "ajjhatto": "स्वयं से संबंधित", "bahiddho": "दूसरों से संबंधित",
    "ajjhattabahiddho": "स्वयं और दूसरों दोनों से संबंधित",
    "ajjhattārammaṇo": "स्वयं से संबंधित विषय वाला", "bahiddhārammaṇo": "दूसरों से संबंधित विषय वाला",
    "ajjhattabahiddhārammaṇo": "स्वयं और दूसरों दोनों से संबंधित विषय वाला",
    "sanidassanasappaṭigho": "दिखाई देने वाला और टकराव वाला",
    "anidassanasappaṭigho": "दिखाई न देने वाला, पर टकराव वाला",
    "anidassanaappaṭigho": "दिखाई न देने वाला और टकराव से रहित",
    # dyads
    "hetu": "मूल रूपी", "na hetu": "मूल रूपी नहीं",
    "sahetuko": "मूल वाला", "ahetuko": "मूल से रहित",
    "hetusampayutto": "मूलों से जुड़ा", "hetuvippayutto": "मूलों से अलग",
    "hetu ceva sahetuko ca": "मूल रूपी भी और मूल वाला भी",
    "sahetuko ceva na ca hetu": "मूल वाला, पर स्वयं मूल रूपी न होने वाला",
    "hetu ceva hetusampayutto ca": "मूल रूपी भी और मूलों से जुड़ा भी",
    "hetusampayutto ceva na ca hetu": "मूलों से जुड़ा, पर स्वयं मूल रूपी न होने वाला",
    "na hetu sahetuko": "मूल रूपी न होने वाला, पर मूल वाला",
    "na hetu ahetuko": "मूल रूपी न होने वाला और मूल से रहित",
    "sappaccayo": "कारणों पर निर्भर रहने वाला", "saṅkhato": "निर्मित",
    "sanidassano": "दिखाई देने वाला", "anidassano": "दिखाई न देने वाला",
    "sappaṭigho": "टकराव वाला", "appaṭigho": "टकराव से रहित",
    "rūpaṃ": "भौतिक", "arūpo": "अभौतिक",
    "lokiyo": "लौकिक", "lokuttaro": "लोकोत्तर",
    "kenaci viññeyyo": "किसी एक प्रकार की चेतना से जाना जा सकने वाला",
    "kenaci na viññeyyo": "किसी एक प्रकार की चेतना से न जाना जा सकने वाला",
    "saṃkiliṭṭho": "क्लेशों से मलिन", "asaṃkiliṭṭho": "क्लेशों से मलिन न होने वाला",
    "savitakko": "आरंभिक विचार वाला", "avitakko": "आरंभिक विचार से रहित",
    "savicāro": "सतत विचार वाला", "avicāro": "सतत विचार से रहित",
    "sappītiko": "उल्लास वाला", "appītiko": "उल्लास से रहित",
    "niyyāniko": "मुक्ति की ओर ले जाने वाला", "aniyyāniko": "मुक्ति की ओर न ले जाने वाला",
    "sauttaro": "सर्वोच्च न होने वाला", "anuttaro": "सर्वोच्च",
    "saraṇo": "संघर्ष वाला", "araṇo": "संघर्ष से रहित",
    "upādinno": "कर्म से उत्पन्न", "anupādinno": "कर्म से उत्पन्न नहीं",
    "upādā": "व्युत्पन्न", "no upādā": "व्युत्पन्न नहीं",
    "sārammaṇo": "विषय वाला", "anārammaṇo": "विषय से रहित",
    "cittaṃ": "मन रूपी", "no cittaṃ": "मन रूपी नहीं",
    "cetasiko": "मन का सहचर", "acetasiko": "मन का सहचर न होने वाला",
    "cittavippayutto": "मन से अलग",
    "cittasaṃsaṭṭho": "मन से घुला-मिला", "cittavisaṃsaṭṭho": "मन से घुला-मिला न होने वाला",
    "cittasamuṭṭhāno": "मन से उत्पन्न", "no cittasamuṭṭhāno": "मन से उत्पन्न नहीं",
    "cittasahabhū": "मन के साथ-साथ होने वाला", "no cittasahabhū": "मन के साथ-साथ न होने वाला",
    "cittānuparivatti": "मन का अनुसरण करने वाला", "no cittānuparivatti": "मन का अनुसरण न करने वाला",
    "cittasaṃsaṭṭhasamuṭṭhāno": "मन से घुला-मिला और मन से उत्पन्न",
    "no cittasaṃsaṭṭhasamuṭṭhāno": "मन से घुला-मिला और मन से उत्पन्न नहीं",
    "cittasaṃsaṭṭhasamuṭṭhānasahabhū": "मन से घुला-मिला, मन से उत्पन्न और मन के साथ-साथ होने वाला",
    "no cittasaṃsaṭṭhasamuṭṭhānasahabhū": "मन से घुला-मिला, मन से उत्पन्न और मन के साथ-साथ होने वाला नहीं",
    "cittasaṃsaṭṭhasamuṭṭhānānuparivatti": "मन से घुला-मिला, मन से उत्पन्न और मन का अनुसरण करने वाला",
    "no cittasaṃsaṭṭhasamuṭṭhānānuparivatti": "मन से घुला-मिला, मन से उत्पन्न और मन का अनुसरण करने वाला नहीं",
    "ajjhattiko": "आंतरिक", "bāhiro": "बाह्य",
}
ALIAS = {"na hetusahetuko": "na hetu sahetuko", "na hetuahetuko": "na hetu ahetuko",
         "āsavippayuttaanāsavo": "āsavavippayuttaanāsavo"}

# the clusters of the matrix: (Pāli noun, Pāli object adj. stem pair, Hindi noun, Hindi oblique, «उनका/उसका»)
CLUSTERS = {
    "āsava": dict(noun="āsavo", obj="sāsavo", aobj="anāsavo", st="āsava", hn="मन के मैल", ho="मन के मैलों", pr="उनका"),
    "saṃyojana": dict(noun="saṃyojanaṃ", obj="saṃyojaniyo", aobj="asaṃyojaniyo", st="saṃyojana",
                      hn="बंधन", ho="बंधनों", pr="उनका"),
    "gantha": dict(noun="gantho", obj="ganthaniyo", aobj="aganthaniyo", st="gantha", hn="गाँठ", ho="गाँठों", pr="उनका"),
    "ogha": dict(noun="ogho", obj="oghaniyo", aobj="anoghaniyo", st="ogha", hn="बाढ़", ho="बाढ़ों", pr="उनका"),
    "yoga": dict(noun="yogo", obj="yoganiyo", aobj="ayoganiyo", st="yoga", hn="जकड़न", ho="जकड़नों", pr="उनका"),
    "nīvaraṇa": dict(noun="nīvaraṇaṃ", obj="nīvaraṇiyo", aobj="anīvaraṇiyo", st="nīvaraṇa",
                     hn="बाधा", ho="बाधाओं", pr="उनका"),
    "parāmāsa": dict(noun="parāmāso", obj="parāmaṭṭho", aobj="aparāmaṭṭho", st="parāmāsa",
                     hn="ग़लत धारणा", ho="ग़लत धारणा", pr="उसका"),
    "upādāna": dict(noun="upādānaṃ", obj="upādāniyo", aobj="anupādāniyo", st="upādāna",
                    hn="आसक्ति", ho="आसक्ति", pr="उसका"),
    "kilesa": dict(noun="kileso", obj="saṃkilesiko", aobj="asaṃkilesiko", st="kilesa",
                   hn="मन के क्लेश", ho="क्लेशों", pr="क्लेशों का"),
}
for c in CLUSTERS.values():
    n, o, ao, st = c["noun"], c["obj"], c["aobj"], c["st"]
    rupi = f"{c['hn']} रूपी"
    hobj = f"{c['ho']} का विषय बनने वाला"
    haobj = f"{c['ho']} का विषय न बनने वाला"
    ce = "ñceva" if n.endswith("ṃ") else " ceva"
    n_ce = n[:-1] + ce if n.endswith("ṃ") else n + ce
    ITEMS[n] = rupi
    ITEMS[f"no {n}"] = f"{rupi} नहीं"
    ITEMS[o] = hobj
    ITEMS[ao] = haobj
    ITEMS[f"{st}sampayutto"] = f"{c['ho']} से जुड़ा"
    ITEMS[f"{st}vippayutto"] = f"{c['ho']} से अलग"
    ITEMS[f"{n_ce} {o} ca"] = f"{rupi} भी और {hobj} भी"
    ITEMS[f"{o} ceva no ca {n}"] = f"{hobj}, पर स्वयं {rupi} न होने वाला"
    ITEMS[f"{n_ce} {st}sampayutto ca"] = f"{rupi} भी और {c['ho']} से जुड़ा भी"
    ITEMS[f"{st}sampayutto ceva no ca {n}"] = f"{c['ho']} से जुड़ा, पर स्वयं {rupi} न होने वाला"
    ITEMS[f"{st}vippayutta{o}"] = f"{c['ho']} से अलग, पर {c['pr']} विषय बनने वाला"
    ITEMS[f"{st}vippayutta{'a' if not ao.startswith('a') else ''}{ao}"] = f"{c['ho']} से अलग और {c['pr']} विषय न बनने वाला"
# kilesa extras (saṃkiliṭṭha pair)
ITEMS["kileso ceva saṃkiliṭṭho ca"] = "मन के क्लेश रूपी भी और क्लेशों से मलिन भी"
ITEMS["saṃkiliṭṭho ceva no ca kileso"] = "क्लेशों से मलिन, पर स्वयं मन के क्लेश रूपी न होने वाला"


def item(key):
    key = ALIAS.get(key, key)
    if key not in ITEMS:
        raise KeyError(key)
    return ITEMS[key]


def fem(h):
    return h.replace("वाला", "वाली").replace("जुड़ा", "जुड़ी")


def pl(h):
    for a, b in [("वाला", "वाले"), ("जुड़ा", "जुड़े"), ("समाया हुआ", "समाए हुए"), ("न हुआ", "न हुए"),
                 ("हो चुका", "हो चुके"), ("छोड़ा जाने", "छोड़े जाने"), ("जाना जा सकने", "जाने जा सकने"),
                 ("घुला-मिला", "घुले-मिले"), ("मन का सहचर", "मन के सहचर")]:
        h = h.replace(a, b)
    return re.sub(r"का(,|$)", r"के\1", h)


# =========================================================================== Abhidhammabhājanīya formula translator
NP_PACC = re.compile(r"^(cakkhu|sota|ghāna|jivhā|kāya|mano)samphassapaccayā(?: (\S+kkhandho))?$")
NP_JA = re.compile(r"^(cakkhu|sota|ghāna|jivhā|kāya|manoviññāṇadhātu|manodhātu|mano)samphassajā (vedanā|saññā|cetanā)$")
NP_VIN = re.compile(r"^(cakkhu|sota|ghāna|jivhā|kāya|mano)viññāṇaṃ$")
XN = {"vedanā": ("अनुभूति", "f"), "saññā": ("पहचान", "f"), "cetanā": ("इरादा", "m")}


def np_(t):
    """Pāli noun phrase -> (Hindi, gender) or None"""
    t = t[:1].lower() + t[1:]
    m = NP_PACC.match(t)
    if m:
        h = f"{SENSE[m.group(1)]} के संपर्क के कारण"
        if m.group(2):
            h += f" {KH[KHP[m.group(2)]]}"
        return h, "m"
    m = NP_JA.match(t)
    if m:
        x, g = XN[m.group(2)]
        src = {"manodhātu": "मन के तत्व", "manoviññāṇadhātu": "मन की चेतना के तत्व"}.get(m.group(1))
        src = src or SENSE[m.group(1)]
        return f"{src} के संपर्क से उत्पन्न {x}", g
    m = NP_VIN.match(t)
    if m:
        return f"{SENSE[m.group(1)]} की चेतना", "f"
    if t == "manodhātu":
        return "मन का तत्व", "m"
    if t == "manoviññāṇadhātu":
        return "मन की चेतना का तत्व", "m"
    return None


DELIM = {",": ",", ";": ";", ".": "।", "…pe…": "…"}


def chain(body):
    """Translate an Abhidhammabhājanīya body (after the dash) into Hindi."""
    parts = re.split(r"(…pe…|[,;.])", body)
    E = []  # elements: [type, text, extra]
    g = "m"  # gender of the last noun phrase (atthi items agree with it)
    for i, p in enumerate(parts):
        if i % 2 == 1:
            E.append(["sep", p, None])
            continue
        if not p.strip():
            if p:
                E.append(["sp", p, None])
            continue
        lead = p[:len(p) - len(p.lstrip())]
        if lead:
            E.append(["sp", lead, None])
        t = p.strip()
        pieces = re.split(r"\s+(?=atthi\s)", t)
        first = pieces[0]
        rest = pieces[1:]
        if re.match(r"^[Aa]tthi\s", first):
            rest = pieces
        else:
            r = np_(first)
            if r:
                E.append(["np", r[0], r[1]])
                g = r[1]
            else:
                E.append(["pred", item(first) + " है", None])
            if rest:
                E.append(["jis", None, None])
        for j, a in enumerate(rest):
            if j > 0:
                SLIPS.append(f"missing comma before '{a}'")
                E.append(["sep", ",", None])
                E.append(["sp", " ", None])
            key = re.sub(r"^[Aa]tthi\s+", "", a)
            h = item(key)
            if g == "f":
                h = fem(h)
            E.append(["at", f"कुछ {h} है", None])
    # «और» before the last member of a closing run of noun phrases
    idx = [i for i, e in enumerate(E) if e[0] != "sp"]
    k = 0
    while k < len(idx):
        if E[idx[k]][0] != "np":
            k += 1
            continue
        run = [k]
        while k + 2 < len(idx) and E[idx[k + 1]][0] == "sep" and E[idx[k + 1]][1] == "," and E[idx[k + 2]][0] == "np":
            k += 2
            run.append(k)
        j = k + 1
        if j < len(idx) and E[idx[j]][0] == "jis":
            j += 1
            while j < len(idx) and (E[idx[j]][0] == "at" or (E[idx[j]][0] == "sep" and E[idx[j]][1] == ","
                                                              and j + 1 < len(idx) and E[idx[j + 1]][0] == "at")):
                j += 1
        closing = j >= len(idx) or (E[idx[j]][0] == "sep" and E[idx[j]][1] in ".;")
        if len(run) >= 2 and closing:
            E[idx[run[-1] - 1]][0] = "and"
        k += 1
    out = []
    for i, e in enumerate(E):
        if e[0] == "sp":
            # drop a space before «…» (Pāli "x …pe…")
            if i + 1 < len(E) and E[i + 1][0] == "sep" and E[i + 1][1] == "…pe…":
                continue
            out.append(e[1])
        elif e[0] == "sep":
            out.append(DELIM[e[1]])
        elif e[0] == "and":
            out.append(" और")
        elif e[0] == "jis":
            out.append(", जिसमें ")
        else:
            out.append(e[1])
    return "".join(out)


HEAD = re.compile(r"^(Tattha katamo (\S+)\? )?(Aparopi )?(\S+?)[vb]idhena (\S+kkhandho)( – | |…pe…)(.*)$")
END = re.compile(r"^(.*?)\s*\b([Ee])vaṃ (\S+?)[vb]idhena (\S+kkhandho)\.$")
FIXED = {
    "Dukamūlakaṃ.": "दो-दो के वर्गीकरणों पर आधारित क्रम।",
    "Tikamūlakaṃ.": "तीन-तीन के वर्गीकरणों पर आधारित क्रम।",
    "Ubhatovaḍḍhakaṃ.": "दोनों ओर से बढ़ने वाला क्रम।",
    "Abhidhammabhājanīyaṃ.": f"{S.ABHI_BH}।",
    "(Yathā kusalattike vitthāro, evaṃ sabbepi tikā vitthāretabbā.)":
        "(जैसे हितकर वाले तीन-तीन के वर्गीकरण में विस्तार किया गया है, उसी तरह सभी तीन-तीन के वर्गीकरणों का विस्तार करना चाहिए।)",
}


def num(w):
    return NUMW[w.lower()]


def abhi_line(p):
    if p in FIXED:
        return FIXED[p]
    m = re.match(r"^Ayaṃ vuccati (\S+kkhandho)\.$", p)
    if m:
        return f"यह {KH[KHP[m.group(1)]]} कहा जाता है।"
    if p.startswith("Atthi "):  # continuation line of a long dyad list
        return chain(p)
    m = HEAD.match(p)
    assert m, p
    q, _, aparo, nw, kh, sep, body = m.groups()
    k = KHP[kh]
    out = ""
    if q:
        out += f"यहाँ {KH[k]} क्या है? "
    hd = S.vidha(num(nw), k)  # "<N> प्रकार से <KH> –"
    if aparo:
        hd = f"{APARO} {hd}"
    if sep == " – ":
        out += hd + " "
    elif sep == " ":
        SLIPS.append(f"no dash after '{nw}vidhena {kh}'")
        out += hd[:-2]
        out += " " if body.startswith(("phassa", "citta")) else ", "
    else:  # "…pe…" directly after the aggregate
        out += hd[:-2] + "…"
        body = body.lstrip()
        if body:
            out += " "
    tail = ""
    me = END.match(body)
    if me:
        body = me.group(1)
        assert KHP[me.group(4)] == k
        tail = S.vidha_end(num(me.group(3)), k)
    h = chain(body) if body else ""
    if tail:
        h = (h + " " + tail) if h else tail
    return out + h


# =========================================================================== Pañhāpucchaka
R, V, SA, SK, VI = (KH[x] for x in ("rupa", "vedana", "sanna", "sankhara", "vinnana"))
C4, T3, D2 = "चार समूह", "तीन समूह", "दो समूह"
OBL = {R: "भौतिक रूप के समूह को", V: "अनुभूति के समूह को", SK: "मानसिक रचनाओं के समूह को",
       VI: "चेतना के समूह को", C4: "चार समूहों को", T3: "तीन समूहों को", D2: "दो समूहों को"}
PL = {C4, T3, D2}


def num_(subj):
    return "p" if subj in PL else "s"


def P(key, n):
    h = item(key)
    return pl(h) if n == "p" else h


def is_(subj, key):
    n = num_(subj)
    return f"{subj} {P(key, n)} {'हैं' if n == 'p' else 'है'}।"


def kabhi(keys, n):
    out = []
    for key in keys:
        h = P(key, n)
        if h.endswith(" नहीं"):
            out.append(f"कभी {h} {'होते' if n == 'p' else 'होता'}")
        else:
            out.append(f"कभी {h} {'होते हैं' if n == 'p' else 'होता है'}")
    return ", ".join(out)


def siya(subj, keys):
    return f"{subj} {kabhi(keys, num_(subj))}"


def quoted(keys, n):
    q = [f"“{P(k, n)}”" for k in keys]
    return q[0] if len(q) == 1 else "न " + ", न ".join(q)


def na_vatt(subj, keys):
    return f"{OBL[subj]} नहीं कहा जा सकता – {quoted(keys, num_(subj))}"


def siya_nv(keys, n):
    return f"कभी {'उन्हें' if n == 'p' else 'उसे'} नहीं कहा जा सकता – {quoted(keys, n)}"


def siya_plus_nv(subj, keys, nv_keys=None):
    """X siyā A, siyā B, …, siyā na vattabbo/ā – "A"tipi, "B"tipi …"""
    n = num_(subj)
    return f"{siya(subj, keys)}, {siya_nv(nv_keys or keys, n)}।"


def j(*sents):
    return " ".join(sents)


# shorthand for the triads (masculine sg. keys)
FEEL = ["sukhāya vedanāya sampayutto", "dukkhāya vedanāya sampayutto", "adukkhamasukhāya vedanāya sampayutto"]
KUS = ["kusalo", "akusalo", "abyākato"]
VIP = ["vipāko", "vipākadhammadhammo", "nevavipākanavipākadhammadhammo"]
UPA = ["upādinnupādāniyo", "anupādinnupādāniyo", "anupādinnaanupādāniyo"]
SAMK = ["saṃkiliṭṭhasaṃkilesiko", "asaṃkiliṭṭhasaṃkilesiko", "asaṃkiliṭṭhaasaṃkilesiko"]
VIT = ["savitakkasavicāro", "avitakkavicāramatto", "avitakkaavicāro"]
PIT = ["pītisahagato", "sukhasahagato", "upekkhāsahagato"]
DAS = ["dassanena pahātabbo", "bhāvanāya pahātabbo", "neva dassanena na bhāvanāya pahātabbo"]
DASH = ["dassanena pahātabbahetuko", "bhāvanāya pahātabbahetuko", "neva dassanena na bhāvanāya pahātabbahetuko"]
ACA = ["ācayagāmī", "apacayagāmī", "nevācayagāmināpacayagāmī"]
SEK = ["sekkho", "asekkho", "nevasekkhanāsekkho"]
PAR = ["paritto", "mahaggato", "appamāṇo"]
PARA = ["parittārammaṇo", "mahaggatārammaṇo", "appamāṇārammaṇo"]
HIN = ["hīno", "majjhimo", "paṇīto"]
MIC = ["micchattaniyato", "sammattaniyato", "aniyato"]
MAG = ["maggārammaṇo", "maggahetuko", "maggādhipati"]
UPP = ["uppanno", "anuppanno", "uppādī"]
ATI = ["atīto", "anāgato", "paccuppanno"]
ATIA = ["atītārammaṇo", "anāgatārammaṇo", "paccuppannārammaṇo"]
AJJ = ["ajjhatto", "bahiddho", "ajjhattabahiddho"]
AJJA = ["ajjhattārammaṇo", "bahiddhārammaṇo", "ajjhattabahiddhārammaṇo"]
SAN = ["sanidassanasappaṭigho", "anidassanasappaṭigho", "anidassanaappaṭigho"]


def ce(n):
    return n[:-1] + "ñceva" if n.endswith("ṃ") else n + " ceva"


def cluster_keys(c):
    n, o, ao, st = c["noun"], c["obj"], c["aobj"], c["st"]
    return dict(both1=f"{ce(n)} {o} ca", but1=f"{o} ceva no ca {n}",
                both2=f"{ce(n)} {st}sampayutto ca", but2=f"{st}sampayutto ceva no ca {n}",
                vo=f"{st}vippayutta{o}", vao=f"{st}vippayutta{'a' if not ao.startswith('a') else ''}{ao}")


def rupa_nv(both, but, mode):
    """Rūpakkhandho na vattabbo – "both"ti(pi), …  mode: 'plain' (but stated), 'quoted' (but stated in quotes),
    'both' (both negated: "…"tipi, "…"tipi)"""
    if mode == "both":
        return na_vatt(R, [both, but]) + "।"
    head = f"{OBL[R]} नहीं कहा जा सकता – “{P(both, 's')}”"
    if mode == "quoted":
        return f"{head}; वह “{P(but, 's')}” है।"
    return f"{head}; वह {P(but, 's')} है।"


def tayo_nv(both, but):
    """Tayo khandhā na vattabbā – "both"ti, siyā but, siyā na vattabbā – "but"ti."""
    return (f"{OBL[T3]} नहीं कहा जा सकता – “{P(both, 'p')}”; वे {kabhi([but], 'p')}, "
            f"{siya_nv([but], 'p')}।")


def sankhara_both(both, but):
    """Saṅkhārakkhandho siyā both, siyā but, siyā na vattabbo – "both"tipi, "but"tipi."""
    return siya_plus_nv(SK, [both, but])


def cluster_line(name, rupa_modes=("plain", "both"), sk_assoc=False):
    c = CLUSTERS[name]
    k = cluster_keys(c)
    n, o, ao, st = c["noun"], c["obj"], c["aobj"], c["st"]
    s = [f"चार समूह {pl(item(n))} नहीं हैं।", siya(SK, [n, f"no {n}"]) + "।",
         is_(R, o), siya(C4, [o, ao]) + "।", is_(R, f"{st}vippayutto")]
    if sk_assoc:  # parāmāsa: Tayo khandhā siyā sampayuttā, siyā vippayuttā; Saṅkhārakkhandho … siyā na vattabbo
        s += [siya(T3, [f"{st}sampayutto", f"{st}vippayutto"]) + "।",
              siya_plus_nv(SK, [f"{st}sampayutto", f"{st}vippayutto"])]
    else:
        s += [siya(C4, [f"{st}sampayutto", f"{st}vippayutto"]) + "।"]
    s += [rupa_nv(k["both1"], k["but1"], rupa_modes[0]), tayo_nv(k["both1"], k["but1"]),
          sankhara_both(k["both1"], k["but1"])]
    if rupa_modes[1]:
        s += [rupa_nv(k["both2"], k["but2"], rupa_modes[1]), tayo_nv(k["both2"], k["but2"]),
              sankhara_both(k["both2"], k["but2"])]
    s += [is_(R, k["vo"]), siya_plus_nv(C4, [k["vo"], k["vao"]], [k["vo"], k["vao"]])]
    return j(*s)


def build_panha():
    h = {}
    h["2-1-3-0"] = [f"#### {S.PANHA}"]
    h["2-150"] = [S.FIVE]
    h["2-151"] = ["पाँच समूहों में से कितने हितकर हैं, कितने हानिकर हैं, कितने नैतिक रूप से अनिर्धारित हैं… "
                  "कितने संघर्ष वाले हैं, कितने संघर्ष से रहित हैं?"]
    h["2-1-3-1-0"] = ["##### तीन-तीन के वर्गीकरण"]
    l1 = j(is_(R, "abyākato"), siya(C4, KUS) + "।", na_vatt(D2, FEEL) + "।", siya(T3, FEEL) + "।",
           is_(R, VIP[2]), siya(C4, VIP) + "।", siya(R, UPA[:2]) + "।", siya(C4, UPA) + "।")
    l2 = j(is_(R, SAMK[1]), siya(C4, SAMK) + "।", is_(R, VIT[2]), siya(T3, VIT) + "।",
           siya_plus_nv(SK, VIT), na_vatt(R, PIT) + "।",
           f"{V} {kabhi(['pītisahagato'], 's')}, पर न {item('sukhasahagato')}, न {item('upekkhāsahagato')}; "
           f"{siya_nv(['pītisahagato'], 's')}।",
           siya_plus_nv(T3, PIT))
    l3 = j(is_(R, DAS[2]), siya(C4, DAS) + "।", is_(R, DASH[2]), siya(C4, DASH) + "।",
           is_(R, ACA[2]), siya(C4, ACA) + "।", is_(R, SEK[2]), siya(C4, SEK) + "।",
           is_(R, "paritto"), siya(C4, PAR) + "।", is_(R, "anārammaṇo"), siya_plus_nv(C4, PARA),
           is_(R, "majjhimo"), siya(C4, HIN) + "।", is_(R, "aniyato"), siya(C4, MIC) + "।")
    l4 = j(is_(R, "anārammaṇo"),
           f"{C4} {kabhi(MAG, 'p')}, {siya_nv(MAG, 'p')}; वे {kabhi(UPP, 'p')}; {kabhi(ATI, 'p')}।",
           is_(R, "anārammaṇo"),
           f"{C4} {kabhi(ATIA, 'p')}, {siya_nv(ATIA, 'p')}; वे {kabhi(AJJ, 'p')}।",
           is_(R, "anārammaṇo"), siya_plus_nv(C4, AJJA), is_(C4, SAN[2]), siya(R, SAN) + "।")
    h["2-152"] = [l1, l2, l3, l4]
    h["2-1-3-2-0"] = ["##### दो-दो के वर्गीकरण"]
    d1 = j(f"चार समूह {pl(item('hetu'))} नहीं हैं।", siya(SK, ["hetu", "na hetu"]) + "।",
           is_(R, "ahetuko"), siya(C4, ["sahetuko", "ahetuko"]) + "।",
           is_(R, "hetuvippayutto"), siya(C4, ["hetusampayutto", "hetuvippayutto"]) + "।",
           rupa_nv("hetu ceva sahetuko ca", "sahetuko ceva na ca hetu", "both"),
           tayo_nv("hetu ceva sahetuko ca", "sahetuko ceva na ca hetu"),
           sankhara_both("hetu ceva sahetuko ca", "sahetuko ceva na ca hetu"),
           rupa_nv("hetu ceva hetusampayutto ca", "hetusampayutto ceva na ca hetu", "both"),
           tayo_nv("hetu ceva hetusampayutto ca", "hetusampayutto ceva na ca hetu"),
           sankhara_both("hetu ceva hetusampayutto ca", "hetusampayutto ceva na ca hetu"),
           is_(R, "na hetu ahetuko"), siya(T3, ["na hetu sahetuko", "na hetu ahetuko"]) + "।",
           siya_plus_nv(SK, ["na hetu sahetuko", "na hetu ahetuko"]))
    d2 = f"पाँचों समूह {pl(item('sappaccayo'))} हैं, {item('saṅkhato')} हैं।"
    d3 = j(is_(C4, "anidassano"), siya(R, ["sanidassano", "anidassano"]) + "।",
           is_(C4, "appaṭigho"), siya(R, ["sappaṭigho", "appaṭigho"]) + "।",
           is_(R, "rūpaṃ"), is_(C4, "arūpo"), is_(R, "lokiyo"),
           f"{siya(C4, ['lokiyo', 'lokuttaro'])}; वे {pl(item('kenaci viññeyyo'))} हैं और "
           f"{pl(item('kenaci na viññeyyo'))} भी हैं।")
    d4 = cluster_line("āsava", ("plain", "both"))
    d5 = cluster_line("saṃyojana", ("quoted", "both"))
    d6 = cluster_line("gantha", ("quoted", "both"))
    og, yo, nv = (pl(item(CLUSTERS[x]["noun"])) for x in ("ogha", "yoga", "nīvaraṇa"))
    d7_head = f"चार समूह {og} नहीं हैं… {yo} नहीं हैं… {nv} नहीं हैं।"
    d7 = cluster_line("nīvaraṇa", ("quoted", "both"))
    d7 = d7_head + d7[d7.index("।") + 1:]
    d8 = cluster_line("parāmāsa", ("quoted", None), sk_assoc=True)
    d9 = j(is_(R, "anārammaṇo"), is_(C4, "sārammaṇo"), is_(VI, "cittaṃ"), f"चार समूह {item('cittaṃ')} नहीं हैं।",
           is_(T3, "cetasiko"), is_(D2, "acetasiko"), is_(T3, "cittasampayutto"), is_(R, "cittavippayutto"),
           f"{OBL[VI]} नहीं कहा जा सकता – न “{item('cittasampayutto')}”, न “{item('cittavippayutto')}”।",
           is_(T3, "cittasaṃsaṭṭho"), is_(R, "cittavisaṃsaṭṭho"),
           f"{OBL[VI]} नहीं कहा जा सकता – न “{item('cittasaṃsaṭṭho')}”, न “{item('cittavisaṃsaṭṭho')}”।",
           is_(T3, "cittasamuṭṭhāno"), is_(VI, "no cittasamuṭṭhāno"),
           siya(R, ["cittasamuṭṭhāno", "no cittasamuṭṭhāno"]) + "।",
           is_(T3, "cittasahabhū"), is_(VI, "no cittasahabhū"), siya(R, ["cittasahabhū", "no cittasahabhū"]) + "।",
           is_(T3, "cittānuparivatti"), is_(VI, "no cittānuparivatti"),
           siya(R, ["cittānuparivatti", "no cittānuparivatti"]) + "।",
           is_(T3, "cittasaṃsaṭṭhasamuṭṭhāno"), is_(D2, "no cittasaṃsaṭṭhasamuṭṭhāno"),
           is_(T3, "cittasaṃsaṭṭhasamuṭṭhānasahabhū"), is_(D2, "no cittasaṃsaṭṭhasamuṭṭhānasahabhū"),
           is_(T3, "cittasaṃsaṭṭhasamuṭṭhānānuparivatti"), is_(D2, "no cittasaṃsaṭṭhasamuṭṭhānānuparivatti"))
    up = cluster_line("upādāna", ("quoted", "both"))
    d10 = j(is_(VI, "ajjhattiko"), is_(T3, "bāhiro"), siya(R, ["ajjhattiko", "bāhiro"]) + "।",
            f"चार समूह {item('upādā')} नहीं हैं।",
            siya(R, ["upādā", "no upādā", "upādinno", "anupādinno"]) + "।", up)
    kc = CLUSTERS["kilesa"]
    kk = cluster_keys(kc)
    d11 = j("चार समूह मन के क्लेश रूपी नहीं हैं।", siya(SK, ["kileso", "no kileso"]) + "।",
            is_(R, "saṃkilesiko"), siya(C4, ["saṃkilesiko", "asaṃkilesiko"]) + "।",
            is_(R, "asaṃkiliṭṭho"), siya(C4, ["saṃkiliṭṭho", "asaṃkiliṭṭho"]) + "।",
            is_(R, "kilesavippayutto"), siya(C4, ["kilesasampayutto", "kilesavippayutto"]) + "।",
            rupa_nv(kk["both1"], kk["but1"], "quoted"), tayo_nv(kk["both1"], kk["but1"]),
            sankhara_both(kk["both1"], kk["but1"]),
            rupa_nv("kileso ceva saṃkiliṭṭho ca", "saṃkiliṭṭho ceva no ca kileso", "both"),
            tayo_nv("kileso ceva saṃkiliṭṭho ca", "saṃkiliṭṭho ceva no ca kileso"),
            sankhara_both("kileso ceva saṃkiliṭṭho ca", "saṃkiliṭṭho ceva no ca kileso"))
    d12 = j(rupa_nv(kk["both2"], kk["but2"], "both"), tayo_nv(kk["both2"], kk["but2"]),
            sankhara_both(kk["both2"], kk["but2"]),
            is_(R, kk["vo"]), siya_plus_nv(C4, [kk["vo"], kk["vao"]]))
    pairs13 = [("dassanena pahātabbo", "na dassanena pahātabbo"), ("bhāvanāya pahātabbo", "na bhāvanāya pahātabbo"),
               ("dassanena pahātabbahetuko", "na dassanena pahātabbahetuko"),
               ("bhāvanāya pahātabbahetuko", "na bhāvanāya pahātabbahetuko"),
               ("savitakko", "avitakko"), ("savicāro", "avicāro")]
    d13 = []
    for a, b in pairs13:
        d13 += [is_(R, b), siya(C4, [a, b]) + "।"]
    d13 += [f"{R} {item('appītiko')} है, {siya(C4, ['sappītiko', 'appītiko'])}।",
            is_(R, "na pītisahagato"), siya(C4, ["pītisahagato", "na pītisahagato"]) + "।",
            is_(D2, "na sukhasahagato"), siya(T3, ["sukhasahagato", "na sukhasahagato"]) + "।",
            is_(D2, "na upekkhāsahagato"), siya(T3, ["upekkhāsahagato", "na upekkhāsahagato"]) + "।"]
    d14 = []
    for a, b, r in [("kāmāvacaro", "na kāmāvacaro", "kāmāvacaro"), ("rūpāvacaro", "na rūpāvacaro", "na rūpāvacaro"),
                    ("arūpāvacaro", "na arūpāvacaro", "na arūpāvacaro"),
                    ("pariyāpanno", "apariyāpanno", "pariyāpanno"), ("niyyāniko", "aniyyāniko", "aniyyāniko"),
                    ("niyato", "aniyato", "aniyato"), ("sauttaro", "anuttaro", "sauttaro"),
                    ("saraṇo", "araṇo", "araṇo")]:
        d14 += [is_(R, r), siya(C4, [a, b]) + "।"]
    h["2-153"] = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, j(*d13), j(*d14),
                  f"{S.PANHA}।", f"{S.CH_TITLE[1]} {S.DONE}।"]
    return h


# =========================================================================== assemble
def segs_after_sample(src_lines):
    n = 0
    for i, line in enumerate(src_lines):
        if line.strip():
            n += 1
            if n > S.SAMPLE_LINES:
                assert line.startswith("##### Vedanākkhandho ^2-1-2-2-0"), line
                return src_lines[i:]
    raise AssertionError("sample boundary not found")


HEADINGS = {"##### Vedanākkhandho": f"##### {KH['vedana']}", "##### Saññākkhandho": f"##### {KH['sanna']}",
            "##### Saṅkhārakkhandho": f"##### {KH['sankhara']}", "##### Viññāṇakkhandho": f"##### {KH['vinnana']}"}


def build():
    src = SRC.read_text(encoding="utf-8").splitlines()
    rest = segs_after_sample(src)
    segs = S.segs_of_lines(rest)
    panha = build_panha()
    out = {}
    for sid, plines in segs:
        if sid in panha:
            out[sid] = panha[sid]
            continue
        hl = []
        for p in plines:
            p = S.ID.sub("", p).rstrip()
            if p.startswith("#####"):
                hl.append(HEADINGS[p])
            elif p.startswith("Pañcakkhandhā"):
                hl.append(S.FIVE)
            else:
                hl.append(abhi_line(p))
        out[sid] = hl
    # checks and blocks (same checks as build_rails_sample.emit)
    blocks = []
    for sid, plines in segs:
        hlines = list(out[sid])
        assert len(plines) == len(hlines), (sid, len(plines), len(hlines))
        for a, b in zip(plines, hlines):
            assert len(a) - len(a.lstrip("#")) == len(b) - len(b.lstrip("#")), sid
            assert a.count("–") + a.count("—") == b.count("–"), (sid, "dash", a.count("–"), b.count("–"), b[:120])
            assert a.count("[") == b.count("["), (sid, "bracket")
            assert not re.search(r"[A-Za-zāīūṃṅñṭḍṇḷ]", b), (sid, "latin", b[:120])
            assert "  " not in b, (sid, "double space", b)
        hlines[-1] = f"{hlines[-1]} ^{sid}"
        blocks.append("\n".join(hlines))
    sample = SAMPLE_HI.read_bytes()
    text = sample.decode("utf-8") + "\n" + "\n\n".join(blocks) + "\n"
    TARGET.write_text(text, encoding="utf-8", newline="\n")
    assert TARGET.read_bytes().startswith(sample)
    print("wrote", TARGET, len(blocks), "new segments")
    for s in sorted(set(SLIPS)):
        print("slip:", s)


if __name__ == "__main__":
    build()
