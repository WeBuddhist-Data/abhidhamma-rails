"""Pañhāpucchaka (question-and-answer) sentence translator for the pi-2 Hindi rails, chapters 2 and 4.

Item names follow the approved pi-1 rails mātikā (1-matika.md), inflected for masculine subjects
(इंद्रिय-क्षेत्र, सत्य); frames follow pi-1 rails ^1-1406/^1-1430/^1-1448:
  siyā X, siyā Y            = कभी X होता है, कभी Y होता है
  S na vattabbā – "A"tipi … = S को नहीं कहा जा सकता – न “A”, न “B”
  siyā na vattabbaṃ – …     = कभी ऐसा होता है कि उसे नहीं कहा जा सकता – न “A”, न “B”
Imported read-only by build_rails_2.py and build_rails_4.py.
"""
import re

# --------------------------------------------------------------------------- predicates (masculine singular)
P = {
    "kusala": "हितकर", "akusala": "हानिकर", "abyākata": "नैतिक रूप से अनिर्धारित",
    "sukhāya vedanāya sampayutta": "सुखद अनुभूति से जुड़ा",
    "dukkhāya vedanāya sampayutta": "दुःखद अनुभूति से जुड़ा",
    "adukkhamasukhāya vedanāya sampayutta": "न दुःखद, न सुखद अनुभूति से जुड़ा",
    "vipāka": "कर्म-फल रूपी", "vipākadhammadhamma": "कर्म-फल उत्पन्न करने वाला",
    "nevavipākanavipākadhammadhamma": "न कर्म-फल रूपी, न कर्म-फल उत्पन्न करने वाला",
    "upādinnupādāniya": "कर्म से उत्पन्न और आसक्ति का विषय बनने वाला",
    "anupādinnupādāniya": "कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाला",
    "anupādinnaanupādāniya": "न कर्म से उत्पन्न, न आसक्ति का विषय बनने वाला",
    "saṃkiliṭṭhasaṃkilesika": "क्लेशों से मलिन और क्लेशों का विषय बनने वाला",
    "asaṃkiliṭṭhasaṃkilesika": "क्लेशों से मलिन न होने वाला, पर क्लेशों का विषय बनने वाला",
    "asaṃkiliṭṭhaasaṃkilesika": "क्लेशों से मलिन न होने वाला और क्लेशों का विषय न बनने वाला",
    "savitakkasavicāra": "आरंभिक विचार और सतत विचार वाला",
    "avitakkavicāramatta": "आरंभिक विचार से रहित, केवल सतत विचार वाला",
    "avitakkaavicāra": "आरंभिक विचार और सतत विचार दोनों से रहित",
    "pītisahagata": "उल्लास के साथ होने वाला", "sukhasahagata": "सुख के साथ होने वाला",
    "upekkhāsahagata": "समभाव के साथ होने वाला",
    "na pītisahagata": "उल्लास के साथ न होने वाला", "na sukhasahagata": "सुख के साथ न होने वाला",
    "na upekkhāsahagata": "समभाव के साथ न होने वाला",
    "dassanena pahātabba": "सत्य-दर्शन से छोड़ा जाने वाला",
    "bhāvanāya pahātabba": "मानसिक अभ्यास से छोड़ा जाने वाला",
    "neva dassanena na bhāvanāya pahātabba": "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़ा जाने वाला",
    "na dassanena pahātabba": "सत्य-दर्शन से न छोड़ा जाने वाला",
    "na bhāvanāya pahātabba": "मानसिक अभ्यास से न छोड़ा जाने वाला",
    "dassanena pahātabbahetuka": "सत्य-दर्शन से छोड़े जाने वाले मूलों वाला",
    "bhāvanāya pahātabbahetuka": "मानसिक अभ्यास से छोड़े जाने वाले मूलों वाला",
    "neva dassanena na bhāvanāya pahātabbahetuka": "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़े जाने वाले मूलों वाला",
    "na dassanena pahātabbahetuka": "सत्य-दर्शन से छोड़े जाने वाले मूलों से रहित",
    "na bhāvanāya pahātabbahetuka": "मानसिक अभ्यास से छोड़े जाने वाले मूलों से रहित",
    "ācayagāmi": "संचय की ओर ले जाने वाला", "apacayagāmi": "संचय घटाने की ओर ले जाने वाला",
    "nevācayagāmināpacayagāmi": "न संचय की ओर, न संचय घटाने की ओर ले जाने वाला",
    "sekkha": "सीखने के चरण का", "asekkha": "सीखना पूरा होने के चरण का",
    "nevasekkhanāsekkha": "न सीखने के चरण का, न सीखना पूरा होने के चरण का",
    "paritta": "सीमित", "mahaggata": "उन्नत", "appamāṇa": "अपरिमित",
    "parittārammaṇa": "सीमित विषय वाला", "mahaggatārammaṇa": "उन्नत विषय वाला",
    "appamāṇārammaṇa": "अपरिमित विषय वाला",
    "hīna": "हीन", "majjhima": "मध्यम", "paṇīta": "उत्तम",
    "micchattaniyata": "ग़लत दिशा में निश्चित", "sammattaniyata": "सही दिशा में निश्चित",
    "niyata": "निश्चित", "aniyata": "अनिश्चित",
    "maggārammaṇa": "मार्ग को विषय बनाने वाला", "maggahetuka": "मार्ग को मूल बनाने वाला",
    "maggādhipati": "मार्ग की प्रधानता वाला",
    "uppanna": "उत्पन्न हो चुका", "anuppanna": "उत्पन्न न हुआ", "uppādi": "उत्पन्न होने वाला",
    "atīta": "अतीत का", "anāgata": "भविष्य का", "paccuppanna": "वर्तमान का",
    "atītārammaṇa": "अतीत के विषय वाला", "anāgatārammaṇa": "भविष्य के विषय वाला",
    "paccuppannārammaṇa": "वर्तमान के विषय वाला",
    "ajjhatta": "स्वयं से संबंधित", "bahiddha": "दूसरों से संबंधित",
    "ajjhattabahiddha": "स्वयं और दूसरों दोनों से संबंधित",
    "ajjhattārammaṇa": "स्वयं से संबंधित विषय वाला", "bahiddhārammaṇa": "दूसरों से संबंधित विषय वाला",
    "ajjhattabahiddhārammaṇa": "स्वयं और दूसरों दोनों से संबंधित विषय वाला",
    "sanidassanasappaṭigha": "दिखाई देने वाला और टकराव वाला",
    "anidassanasappaṭigha": "दिखाई न देने वाला, पर टकराव वाला",
    "anidassanaappaṭigha": "दिखाई न देने वाला और टकराव से रहित",
    # dyads
    "hetu": "मूल रूपी", "na hetu": "मूल रूपी न होने वाला",
    "sahetuka": "मूल वाला", "ahetuka": "मूल से रहित",
    "hetusampayutta": "मूलों से जुड़ा", "hetuvippayutta": "मूलों से अलग",
    "hetu ceva sahetuka ca": "मूल रूपी भी और मूल वाला भी",
    "sahetuka ceva na ca hetu": "मूल वाला, पर स्वयं मूल रूपी न होने वाला",
    "hetu ceva hetusampayutta ca": "मूल रूपी भी और मूलों से जुड़ा भी",
    "hetusampayutta ceva na ca hetu": "मूलों से जुड़ा, पर स्वयं मूल रूपी न होने वाला",
    "na hetusahetuka": "मूल रूपी न होने वाला, पर मूल वाला",
    "na hetuahetuka": "मूल रूपी न होने वाला और मूल से रहित",
    "na hetūahetuka": "मूल रूपी न होने वाला और मूल से रहित",
    "sappaccaya": "कारणों पर निर्भर रहने वाला", "appaccaya": "कारणों पर निर्भर न रहने वाला",
    "saṅkhata": "निर्मित", "asaṅkhata": "अनिर्मित",
    "sanidassana": "दिखाई देने वाला", "anidassana": "दिखाई न देने वाला",
    "sappaṭigha": "टकराव वाला", "appaṭigha": "टकराव से रहित",
    "rūpa": "भौतिक", "arūpa": "अभौतिक", "lokiya": "लौकिक", "lokuttara": "लोकोत्तर",
    "kilesa": "मन के क्लेश रूपी", "na kilesa": "मन के क्लेश रूपी न होने वाला",
    "saṃkilesika": "क्लेशों का विषय बनने वाला", "asaṃkilesika": "क्लेशों का विषय न बनने वाला",
    "saṃkiliṭṭha": "क्लेशों से मलिन", "asaṃkiliṭṭha": "क्लेशों से मलिन न होने वाला",
    "kilesasampayutta": "क्लेशों से जुड़ा", "kilesavippayutta": "क्लेशों से अलग",
    "kilesa ceva saṃkilesika ca": "मन के क्लेश रूपी भी और क्लेशों का विषय बनने वाला भी",
    "saṃkilesika ceva na ca kilesa": "क्लेशों का विषय बनने वाला, पर स्वयं मन के क्लेश रूपी न होने वाला",
    "kilesa ceva saṃkiliṭṭha ca": "मन के क्लेश रूपी भी और क्लेशों से मलिन भी",
    "saṃkiliṭṭha ceva na ca kilesa": "क्लेशों से मलिन, पर स्वयं मन के क्लेश रूपी न होने वाला",
    "kilesa ceva kilesasampayutta ca": "मन के क्लेश रूपी भी और क्लेशों से जुड़ा भी",
    "kilesasampayutta ceva na ca kilesa": "क्लेशों से जुड़ा, पर स्वयं मन के क्लेश रूपी न होने वाला",
    "kilesasampayutta ceva na ca na kilesa": "क्लेशों से जुड़ा, पर स्वयं मन के क्लेश रूपी न होने वाला",  # source slip "no ca na"
    "kilesavippayuttasaṃkilesika": "क्लेशों से अलग, पर क्लेशों का विषय बनने वाला",
    "kilesavippayuttaasaṃkilesika": "क्लेशों से अलग और क्लेशों का विषय न बनने वाला",
    "sārammaṇa": "विषय वाला", "anārammaṇa": "विषय से रहित",
    "citta": "मन रूपी", "na citta": "मन रूपी न होने वाला",
    "cetasika": "मन का सहचर", "acetasika": "मन का सहचर न होने वाला",
    "cittasampayutta": "मन से जुड़ा", "cittavippayutta": "मन से अलग",
    "cittena sampayutta": "मन से जुड़ा", "cittena vippayutta": "मन से अलग",
    "cittasaṃsaṭṭha": "मन से घुला-मिला", "cittavisaṃsaṭṭha": "मन से घुला-मिला न होने वाला",
    "cittena saṃsaṭṭha": "मन से घुला-मिला", "cittena visaṃsaṭṭha": "मन से घुला-मिला न होने वाला",
    "cittasamuṭṭhāna": "मन से उत्पन्न", "na cittasamuṭṭhāna": "मन से उत्पन्न न होने वाला",
    "cittasahabhu": "मन के साथ-साथ होने वाला", "na cittasahabhu": "मन के साथ-साथ न होने वाला",
    "cittānuparivatti": "मन का अनुसरण करने वाला", "na cittānuparivatti": "मन का अनुसरण न करने वाला",
    "cittasaṃsaṭṭhasamuṭṭhāna": "मन से घुला-मिला और मन से उत्पन्न",
    "cittasaṃsaṭṭhasamuṭṭhānasahabhu": "मन से घुला-मिला, मन से उत्पन्न और मन के साथ-साथ होने वाला",
    "cittasaṃsaṭṭhasamuṭṭhānānuparivatti": "मन से घुला-मिला, मन से उत्पन्न और मन का अनुसरण करने वाला",
    "ajjhattika": "आंतरिक", "bāhira": "बाह्य",
    "upāda": "व्युत्पन्न", "na upāda": "व्युत्पन्न न होने वाला",
    "upādinna": "कर्म से उत्पन्न", "anupādinna": "कर्म से उत्पन्न न होने वाला",
    "savitakka": "आरंभिक विचार वाला", "avitakka": "आरंभिक विचार से रहित",
    "savicāra": "सतत विचार वाला", "avicāra": "सतत विचार से रहित",
    "sappītika": "उल्लास वाला", "appītika": "उल्लास से रहित",
    "kāmāvacara": "इंद्रिय-सुखों के लोक से संबंधित",
    "na kāmāvacara": "इंद्रिय-सुखों के लोक से संबंधित न होने वाला",
    "rūpāvacara": "सूक्ष्म भौतिक लोक से संबंधित", "na rūpāvacara": "सूक्ष्म भौतिक लोक से संबंधित न होने वाला",
    "arūpāvacara": "अभौतिक लोक से संबंधित", "na arūpāvacara": "अभौतिक लोक से संबंधित न होने वाला",
    "pariyāpanna": "अस्तित्व के लोकों में समाया हुआ", "apariyāpanna": "अस्तित्व के लोकों में न समाया हुआ",
    "niyyānika": "मुक्ति की ओर ले जाने वाला", "aniyyānika": "मुक्ति की ओर न ले जाने वाला",
    "sauttara": "सर्वोच्च न होने वाला", "anuttara": "सर्वोच्च",
    "saraṇa": "संघर्ष वाला", "araṇa": "संघर्ष से रहित",
    # source slips in chapter 2 (^2-171), rendered as written
    "upādānasampayuttaupādāniya": "आसक्ति से जुड़ा और उसका विषय बनने वाला",
    "upādāniya ceva upādānasampayutta ca": "आसक्ति का विषय बनने वाला भी और आसक्ति से जुड़ा भी",
}
# the five "cluster" groups (pi-1 mātikā ^1-M2-14 … ^1-M2-74)
GROUPS = [  # stem, object-adjective stem, Hindi noun, Hindi oblique plural, pronoun for "its object"
    ("āsava", "sāsava", "anāsava", "मन के मैल", "मन के मैलों", "उनका"),
    ("saṃyojana", "saṃyojaniya", "asaṃyojaniya", "बंधन", "बंधनों", "उनका"),
    ("gantha", "ganthaniya", "aganthaniya", "गाँठ", "गाँठों", "उनका"),
    ("ogha", "oghaniya", "anoghaniya", "बाढ़", "बाढ़ों", "उनका"),
    ("yoga", "yoganiya", "ayoganiya", "जकड़न", "जकड़नों", "उनका"),
    ("nīvaraṇa", "nīvaraṇiya", "anīvaraṇiya", "बाधा", "बाधाओं", "उनका"),
    ("parāmāsa", "parāmaṭṭha", "aparāmaṭṭha", "ग़लत धारणा", "ग़लत धारणा", "उसका"),
    ("upādāna", "upādāniya", "anupādāniya", "आसक्ति", "आसक्ति", "उसका"),
]
for g, o, ao, X, Xo, pr in GROUPS:
    P.setdefault(g, f"{X} रूपी")
    P.setdefault(f"na {g}", f"{X} रूपी न होने वाला")
    P.setdefault(o, f"{Xo} का विषय बनने वाला")
    P.setdefault(ao, f"{Xo} का विषय न बनने वाला")
    P.setdefault(f"{g}sampayutta", f"{Xo} से जुड़ा")
    P.setdefault(f"{g}vippayutta", f"{Xo} से अलग")
    P.setdefault(f"{g} ceva {o} ca", f"{X} रूपी भी और {Xo} का विषय बनने वाला भी")
    P.setdefault(f"{o} ceva na ca {g}", f"{Xo} का विषय बनने वाला, पर स्वयं {X} रूपी न होने वाला")
    P.setdefault(f"{g} ceva {g}sampayutta ca", f"{X} रूपी भी और {Xo} से जुड़ा भी")
    P.setdefault(f"{g}sampayutta ceva na ca {g}", f"{Xo} से जुड़ा, पर स्वयं {X} रूपी न होने वाला")
    P.setdefault(f"{g}vippayutta{o}", f"{Xo} से अलग, पर {pr} विषय बनने वाला")
    P.setdefault(f"{g}vippayutta{ao}", f"{Xo} से अलग और {pr} विषय न बनने वाला")
    P.setdefault(f"{g}vippayutta{'a' + o}", f"{Xo} से अलग और {pr} विषय न बनने वाला")
P["anupādāniya"] = "आसक्ति का विषय न बनने वाला"
P["upādānavippayuttaanupādāniya"] = "आसक्ति से अलग और उसका विषय न बनने वाला"

# "ऐसा … जो … नहीं" items (pi-1 ^1-M2-63 … ^1-M2-65 shape)
NEG = {"na cittasaṃsaṭṭhasamuṭṭhāna": "cittasaṃsaṭṭhasamuṭṭhāna",
       "na cittasaṃsaṭṭhasamuṭṭhānasahabhu": "cittasaṃsaṭṭhasamuṭṭhānasahabhu",
       "na cittasaṃsaṭṭhasamuṭṭhānānuparivatti": "cittasaṃsaṭṭhasamuṭṭhānānuparivatti"}

PL_WORD = {"वाला": "वाले", "जुड़ा": "जुड़े", "छोड़ा": "छोड़े", "हुआ": "हुए", "समाया": "समाए",
           "घुला-मिला": "घुले-मिले", "चुका": "चुके"}
PL_OVR = {"cetasika": "मन के सहचर", "acetasika": "मन के सहचर न होने वाले"}


def plural(h):
    out = []
    toks = h.split(" ")
    for i, t in enumerate(toks):
        core, tail = (t[:-1], ",") if t.endswith(",") else (t, "")
        if core in PL_WORD:
            core = PL_WORD[core]
        elif core == "का" and (tail or i == len(toks) - 1):
            core = "के"
        out.append(core + tail)
    return " ".join(out)


def canon(s):
    s = s.replace("ñcā", "ṃ cā").replace("ñceva", "ṃ ceva").replace("ñca", "ṃ ca")
    words = []
    for w in s.split():
        if w.endswith("ṃ"):
            w = w[:-1]
        done = False
        for a, b in (("uno", "u"), ("ino", "i"), ("āni", "a")):
            if w.endswith(a) and len(w) > 4:
                w, done = w[:-len(a)] + b, True
                break
        if not done and w:
            if w[-1] in "āo":
                w = w[:-1] + "a"
            elif w[-1] == "ī":
                w = w[:-1] + "i"
            elif w[-1] == "ū":
                w = w[:-1] + "u"
        words.append(w)
    s = " ".join(words)
    return s


def pred(key, num):
    if key not in P and key + " ca" in P:  # "…ñceva X"ntipi without the closing "ca" (source variation)
        key = key + " ca"
    if key not in P:
        raise KeyError(f"unknown predicate: {key!r}")
    if num == "p":
        return PL_OVR.get(key) or plural(P[key])
    return P[key]


def hai(n):
    return "हैं" if n == "p" else "है"


def hota(n):
    return "होते हैं" if n == "p" else "होता है"


def pron(n):
    return "उन्हें" if n == "p" else "उसे"


def vah(n):
    return "वे" if n == "p" else "वह"


QUOTE = re.compile(r'^"([^"]+)"\s?(n?ti(?:pi)?)?$')


def qlist(quotes, n):
    items = [f"“{pred(canon(c), n)}”" for c, _ in quotes]
    if any((sfx or "").endswith("pi") for _, sfx in quotes) or len(items) > 1:
        return ", ".join(f"न {x}" for x in items)
    return items[0]


def plain(key, n, siya):
    if key in NEG:
        k = NEG[key]
        if siya:
            return (f"कभी ऐसे होते हैं जो {pred(k, 'p')} नहीं हैं" if n == "p"
                    else f"कभी ऐसा होता है जो {pred(k, 's')} नहीं है")
        return (f"ऐसे हैं जो {pred(k, 'p')} नहीं हैं" if n == "p" else f"ऐसा है जो {pred(k, 's')} नहीं है")
    if siya:
        return f"कभी {pred(key, n)} {hota(n)}"
    return f"{pred(key, n)} {hai(n)}"


def tokens(rest):
    """split the predicate part on ', ' into clauses; quoted items join their 'na vattabba' clause."""
    out = []
    for t in rest.split(", "):
        t = t.strip()
        m = re.match(r"^(siyā )?na vattabb(?:ā|aṃ|o) – (.*)$", t)
        if m:
            out.append(["nv", bool(m.group(1)), [], True])
            t = m.group(2)
        q = QUOTE.match(t)
        if q and out and out[-1][0] == "nv" and out[-1][3]:
            out[-1][2].append((q.group(1), q.group(2)))
            out[-1][3] = (q.group(2) or "").endswith("pi")
            continue
        if q:  # quoted positive assertion after a closed 'na vattabba' ("…"ti, "Y")
            out.append(["posq", q.group(1)])
            continue
        if out and out[-1][0] == "nv":
            out[-1][3] = False
        if t.startswith("siyā "):
            out.append(["siya", t[5:]])
        else:
            out.append(["pos", t])
    return out


def render_clauses(subj, rest, special=None):
    d, obl, n = subj
    parts = []
    first = True
    after_nv = False
    for tok in tokens(rest):
        kind = tok[0]
        if special and kind in ("siya", "pos"):
            raw = ("siyā " if kind == "siya" else "") + tok[1]
            if canon(raw) in special:
                h = special[canon(raw)]
                parts.append((f"{d} " if first else "") + h)
                first, after_nv = False, False
                continue
        if kind == "nv":
            body = f"नहीं कहा जा सकता – {qlist(tok[2], n)}"
            if tok[1]:
                h = f"कभी ऐसा होता है कि {pron(n)} {body}"
                h = (f"{d} " if first else "") + h
            elif first:
                h = f"{obl} को {body}"
            else:
                h = f"{pron(n)} {body}"
            parts.append(h)
            first, after_nv = False, not tok[1]
            continue
        if kind == "posq":
            parts.append(f"{vah(n)} “{pred(canon(tok[1]), n)}” {hai(n)}")
            first, after_nv = False, False
            continue
        key = canon(tok[1])
        if kind == "pos" and "…pe… " in tok[1]:
            subs = [plain(canon(x), n, False) for x in tok[1].split("…pe… ")]
            h = "… ".join(subs)
        else:
            h = plain(key, n, kind == "siya")
        if first:
            h = f"{d} {h}"
        elif after_nv:
            h = f"{vah(n)} {h}"
        parts.append(h)
        first, after_nv = False, False
    return ", ".join(parts)


def sentence(s, SUBJ, special=None, semi_subject=None):
    s = s.strip()
    assert s.endswith("."), s
    s = s[:-1]
    if s.endswith("araṇāti"):
        s = s[:-2]
    elif s.endswith("araṇanti"):
        s = s[:-3] + "ṃ"
    subj = None
    for k in sorted(SUBJ, key=len, reverse=True):
        if s.startswith(k + " "):
            subj, rest = SUBJ[k], s[len(k) + 1:]
            break
    if subj is None:
        raise ValueError(f"no subject: {s[:60]}")
    if "; " in rest:
        a, b = rest.split("; ", 1)
        h = render_clauses(subj, a, special)
        if b.startswith("siyā "):  # subject-less continuation (^2-170): all the sense bases
            h2 = render_clauses(semi_subject, b, special)
        else:
            h2 = special[canon(b)]
        return f"{h}; {h2}।"
    return render_clauses(subj, rest, special) + "।"


def line(pali, SUBJ, special=None, semi_subject=None, pre=None):
    if pre:
        for a, b in pre:
            pali = pali.replace(a, b)
    sents = re.split(r"(?<=\.)\s+", pali.strip())
    return " ".join(sentence(x, SUBJ, special, semi_subject) for x in sents)
