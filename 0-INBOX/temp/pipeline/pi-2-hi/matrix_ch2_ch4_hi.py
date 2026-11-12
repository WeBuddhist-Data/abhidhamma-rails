# -*- coding: utf-8 -*-
"""pi-2 Vibhaṅga, Hindi: shared Pañhāpucchaka engine for chapters 2 (Āyatana) and 4 (Sacca).

Every matrix predicate is a fixed string taken from the pi-1 Hindi matrix (1-matika.md, fem. pl. there),
put into the masculine here (इंद्रिय-क्षेत्र and सत्य are masculine), so every repeat is byte-identical.
The Pāli sentences are parsed (subject + clauses: plain / siyā / na vattabbaṃ – "…"tipi) and assembled from
these strings; a sentence the parser cannot handle raises, so nothing is typed by hand.
"""
import re

DASH = "–"

# ---------------------------------------------------------------- masculine sg -> pl
_PL = {"वाला": "वाले", "हुआ": "हुए", "जुड़ा": "जुड़े", "समाया": "समाए", "छोड़ा": "छोड़े", "घुला-मिला": "घुले-मिले",
       "चुका": "चुके"}


def plural(sg):
    out = []
    for w in sg.split(" "):
        core, tail = (w[:-1], w[-1]) if w.endswith(",") else (w, "")
        out.append(_PL.get(core, core) + tail)
    return " ".join(out)


def E(sg, pl=None):
    return (sg, pl if pl is not None else plural(sg))


# ---------------------------------------------------------------- Pāli normalisation
FUNC = {"na", "no", "ca", "ceva", "neva", "kenaci"}
ALIAS = {"hetūahetuka": "hetuahetuka"}


def _word(w):
    if w in FUNC:
        return w
    for a, b in (("āni", "a"), ("ino", "i"), ("uno", "u"), ("aṃ", "a"), ("ā", "a"), ("o", "a"), ("ī", "i"), ("ū", "u")):
        if w.endswith(a) and len(w) > len(a) + 1:
            w = w[: -len(a)] + b
            break
    return ALIAS.get(w, w)


def norm(p):
    p = p.strip()
    p = re.sub(r"ñceva\b", "ṃ ceva", p)
    p = re.sub(r"ñc[aā]\b", "ṃ ca", p)
    p = re.sub(r"\bcā$", "ca", p)
    return " ".join(_word(w) for w in p.split())


# ---------------------------------------------------------------- the predicates (key = normalised Pāli)
P = {}


PRED_NEG = {}  # a-/an- words that read better as "X नहीं है" when they are the predicate (quotes keep the lexical form)


def add(key, sg, pl=None, pred_neg=None):
    key = norm(key)
    assert key not in P, key
    P[key] = E(sg, pl)
    if pred_neg:
        PRED_NEG[key] = pred_neg


# triads (pi-1 1-matika.md ^1-M1-1 … ^1-M1-22)
add("kusala", "हितकर")
add("akusala", "हानिकर")
add("abyākata", "नैतिक रूप से अनिर्धारित")
add("sukhāya vedanāya sampayutta", "सुखद अनुभूति से जुड़ा")
add("dukkhāya vedanāya sampayutta", "दुःखद अनुभूति से जुड़ा")
add("adukkhamasukhāya vedanāya sampayutta", "न दुःखद, न सुखद अनुभूति से जुड़ा")
add("vipāka", "कर्म-फल रूपी")
add("vipākadhammadhamma", "कर्म-फल उत्पन्न करने वाला")
add("nevavipākanavipākadhammadhamma", "न कर्म-फल रूपी, न कर्म-फल उत्पन्न करने वाला")
add("upādinnupādāniya", "कर्म से उत्पन्न और आसक्ति का विषय बनने वाला")
add("anupādinnupādāniya", "कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाला")
add("anupādinnaanupādāniya", "न कर्म से उत्पन्न, न आसक्ति का विषय बनने वाला")
add("saṃkiliṭṭhasaṃkilesika", "क्लेशों से मलिन और क्लेशों का विषय बनने वाला")
add("asaṃkiliṭṭhasaṃkilesika", "क्लेशों से मलिन न होने वाला, पर क्लेशों का विषय बनने वाला")
add("asaṃkiliṭṭhaasaṃkilesika", "क्लेशों से मलिन न होने वाला और क्लेशों का विषय न बनने वाला")
add("savitakkasavicāra", "आरंभिक विचार और सतत विचार वाला")
add("avitakkavicāramatta", "आरंभिक विचार से रहित, केवल सतत विचार वाला")
add("avitakkaavicāra", "आरंभिक विचार और सतत विचार दोनों से रहित")
add("pītisahagata", "उल्लास के साथ होने वाला")
add("sukhasahagata", "सुख के साथ होने वाला")
add("upekkhāsahagata", "समभाव के साथ होने वाला")
add("dassanena pahātabba", "सत्य-दर्शन से छोड़ा जाने वाला")
add("bhāvanāya pahātabba", "मानसिक अभ्यास से छोड़ा जाने वाला")
add("neva dassanena na bhāvanāya pahātabba", "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़ा जाने वाला")
add("dassanena pahātabbahetuka", "सत्य-दर्शन से छोड़े जाने वाले मूलों वाला")
add("bhāvanāya pahātabbahetuka", "मानसिक अभ्यास से छोड़े जाने वाले मूलों वाला")
add("neva dassanena na bhāvanāya pahātabbahetuka", "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़े जाने वाले मूलों वाला")
add("ācayagāmi", "संचय की ओर ले जाने वाला")
add("apacayagāmi", "संचय घटाने की ओर ले जाने वाला")
add("nevācayagāmināpacayagāmi", "न संचय की ओर, न संचय घटाने की ओर ले जाने वाला")
add("sekkha", "सीखने के चरण का", "सीखने के चरण के")
add("asekkha", "सीखना पूरा होने के चरण का", "सीखना पूरा होने के चरण के")
add("nevasekkhanāsekkha", "न सीखने के चरण का, न सीखना पूरा होने के चरण का",
    "न सीखने के चरण के, न सीखना पूरा होने के चरण के")
add("paritta", "सीमित")
add("mahaggata", "उन्नत")
add("appamāṇa", "अपरिमित")
add("parittārammaṇa", "सीमित विषय वाला")
add("mahaggatārammaṇa", "उन्नत विषय वाला")
add("appamāṇārammaṇa", "अपरिमित विषय वाला")
add("hīna", "हीन")
add("majjhima", "मध्यम")
add("paṇīta", "उत्तम")
add("micchattaniyata", "ग़लत दिशा में निश्चित")
add("sammattaniyata", "सही दिशा में निश्चित")
add("aniyata", "अनिश्चित")
add("maggārammaṇa", "मार्ग को विषय बनाने वाला")
add("maggahetuka", "मार्ग को मूल बनाने वाला")
add("maggādhipati", "मार्ग की प्रधानता वाला")
add("uppanna", "उत्पन्न हो चुका")
add("anuppanna", "उत्पन्न न हुआ")
add("uppādi", "उत्पन्न होने वाला")
add("atīta", "अतीत का", "अतीत के")
add("anāgata", "भविष्य का", "भविष्य के")
add("paccuppanna", "वर्तमान का", "वर्तमान के")
add("atītārammaṇa", "अतीत के विषय वाला")
add("anāgatārammaṇa", "भविष्य के विषय वाला")
add("paccuppannārammaṇa", "वर्तमान के विषय वाला")
add("ajjhatta", "स्वयं से संबंधित")
add("bahiddha", "दूसरों से संबंधित")
add("ajjhattabahiddha", "स्वयं और दूसरों दोनों से संबंधित")
add("ajjhattārammaṇa", "स्वयं से संबंधित विषय वाला")
add("bahiddhārammaṇa", "दूसरों से संबंधित विषय वाला")
add("ajjhattabahiddhārammaṇa", "स्वयं और दूसरों दोनों से संबंधित विषय वाला")
add("sanidassanasappaṭigha", "दिखाई देने वाला और टकराव वाला")
add("anidassanasappaṭigha", "दिखाई न देने वाला, पर टकराव वाला")
add("anidassanaappaṭigha", "दिखाई न देने वाला और टकराव से रहित")

# roots (^1-M2-1 … ^1-M2-6)
add("hetu", "मूल रूपी")
add("sahetuka", "मूल वाला")
add("ahetuka", "मूल से रहित")
add("hetusampayutta", "मूलों से जुड़ा")
add("hetuvippayutta", "मूलों से अलग")
add("hetu ceva sahetuka ca", "मूल रूपी भी और मूल वाला भी", "मूल रूपी भी और मूल वाले भी")
add("sahetuka ceva na ca hetu", "मूल वाला, पर स्वयं मूल रूपी न होने वाला")
add("hetu ceva hetusampayutta ca", "मूल रूपी भी और मूलों से जुड़ा भी", "मूल रूपी भी और मूलों से जुड़े भी")
add("hetusampayutta ceva na ca hetu", "मूलों से जुड़ा, पर स्वयं मूल रूपी न होने वाला")
add("na hetusahetuka", "मूल रूपी न होने वाला, पर मूल वाला")
add("na hetuahetuka", "मूल रूपी न होने वाला और मूल से रहित")
# small middle dyads (^1-M2-7 … ^1-M2-13)
add("sappaccaya", "कारणों पर निर्भर रहने वाला")
add("appaccaya", "कारणों पर निर्भर न रहने वाला")
add("saṅkhata", "निर्मित")
add("asaṅkhata", "अनिर्मित")
add("sanidassana", "दिखाई देने वाला")
add("anidassana", "दिखाई न देने वाला")
add("sappaṭigha", "टकराव वाला")
add("appaṭigha", "टकराव से रहित")
add("rūpa", "भौतिक")
add("arūpa", "अभौतिक")
add("lokiya", "लौकिक")
add("lokuttara", "लोकोत्तर")
add("kenaci viññeyya", "किसी एक प्रकार की चेतना से जाना जा सकने वाला", "किसी एक प्रकार की चेतना से जाने जा सकने वाले")
add("kenaci na viññeyya", "किसी एक प्रकार की चेतना से न जाना जा सकने वाला",
    "किसी एक प्रकार की चेतना से न जाने जा सकने वाले")


def cluster(stem, iya, aniya, rupi, obl, pron):
    """the dyads of a cluster: āsava / saṃyojana / gantha / ogha / yoga / nīvaraṇa / upādāna (pi-1 wording)."""
    vis = f"{obl} का विषय बनने वाला"
    add(stem, f"{rupi} रूपी")
    add(iya, vis)
    add(aniya, f"{obl} का विषय न बनने वाला")
    add(stem + "sampayutta", f"{obl} से जुड़ा")
    add(stem + "vippayutta", f"{obl} से अलग")
    add(f"{stem} ceva {iya} ca", f"{rupi} रूपी भी और {vis} भी", f"{rupi} रूपी भी और {plural(vis)} भी")
    add(f"{iya} ceva no ca {stem}", f"{vis}, पर स्वयं {rupi} रूपी न होने वाला")
    add(f"{stem} ceva {stem}sampayutta ca", f"{rupi} रूपी भी और {obl} से जुड़ा भी", f"{rupi} रूपी भी और {obl} से जुड़े भी")
    add(f"{stem}sampayutta ceva no ca {stem}", f"{obl} से जुड़ा, पर स्वयं {rupi} रूपी न होने वाला")
    add(f"{stem}vippayutta{iya}", f"{obl} से अलग, पर {pron} विषय बनने वाला")
    add(f"{stem}vippayutta{aniya}", f"{obl} से अलग और {pron} विषय न बनने वाला")


cluster("āsava", "sāsava", "anāsava", "मन के मैल", "मन के मैलों", "उनका")
cluster("saṃyojana", "saṃyojaniya", "asaṃyojaniya", "बंधन", "बंधनों", "उनका")
cluster("gantha", "ganthaniya", "aganthaniya", "गाँठ", "गाँठों", "उनका")
cluster("ogha", "oghaniya", "anoghaniya", "बाढ़", "बाढ़ों", "उनका")
cluster("yoga", "yoganiya", "ayoganiya", "जकड़न", "जकड़नों", "उनका")
cluster("nīvaraṇa", "nīvaraṇiya", "anīvaraṇiya", "बाधा", "बाधाओं", "उनका")
cluster("upādāna", "upādāniya", "anupādāniya", "आसक्ति", "आसक्ति", "उसका")
# parāmāsa (^1-M2-50 … ^1-M2-54)
add("parāmāsa", "ग़लत धारणा रूपी")
add("parāmaṭṭha", "ग़लत धारणा का विषय बनने वाला")
add("aparāmaṭṭha", "ग़लत धारणा का विषय न बनने वाला")
add("parāmāsasampayutta", "ग़लत धारणा से जुड़ा")
add("parāmāsavippayutta", "ग़लत धारणा से अलग")
add("parāmāsa ceva parāmaṭṭha ca", "ग़लत धारणा रूपी भी और ग़लत धारणा का विषय बनने वाला भी",
    "ग़लत धारणा रूपी भी और ग़लत धारणा का विषय बनने वाले भी")
add("parāmaṭṭha ceva no ca parāmāsa", "ग़लत धारणा का विषय बनने वाला, पर स्वयं ग़लत धारणा रूपी न होने वाला")
add("parāmāsavippayuttaparāmaṭṭha", "ग़लत धारणा से अलग, पर उसका विषय बनने वाला")
add("parāmāsavippayuttaaparāmaṭṭha", "ग़लत धारणा से अलग और उसका विषय न बनने वाला")
# big middle dyads (^1-M2-55 … ^1-M2-68)
add("sārammaṇa", "विषय वाला")
add("anārammaṇa", "विषय से रहित")
add("citta", "मन रूपी")
add("cetasika", "मन का सहचर", "मन के सहचर")
add("acetasika", "मन का सहचर न होने वाला", "मन के सहचर न होने वाले", pred_neg="cetasika")
add("cittasampayutta", "मन से जुड़ा")
add("cittavippayutta", "मन से अलग")
add("cittena sampayutta", "मन से जुड़ा")
add("cittena vippayutta", "मन से अलग")
add("cittasaṃsaṭṭha", "मन से घुला-मिला")
add("cittavisaṃsaṭṭha", "मन से घुला-मिला न होने वाला", pred_neg="cittasaṃsaṭṭha")
add("cittena saṃsaṭṭha", "मन से घुला-मिला")
add("cittena visaṃsaṭṭha", "मन से घुला-मिला न होने वाला")
add("cittasamuṭṭhāna", "मन से उत्पन्न")
add("cittasahabhu", "मन के साथ-साथ होने वाला")
add("cittānuparivatti", "मन का अनुसरण करने वाला")
add("cittasaṃsaṭṭhasamuṭṭhāna", "मन से घुला-मिला और मन से उत्पन्न", "मन से घुले-मिले और मन से उत्पन्न")
add("cittasaṃsaṭṭhasamuṭṭhānasahabhu", "मन से घुला-मिला, मन से उत्पन्न और मन के साथ-साथ होने वाला")
add("cittasaṃsaṭṭhasamuṭṭhānānuparivatti", "मन से घुला-मिला, मन से उत्पन्न और मन का अनुसरण करने वाला")
add("ajjhattika", "आंतरिक")
add("bāhira", "बाह्य")
add("upāda", "व्युत्पन्न")
add("upādinna", "कर्म से उत्पन्न")
add("anupādinna", "कर्म से उत्पन्न न होने वाला", pred_neg="upādinna")
# kilesa (^1-M2-75 … ^1-M2-82)
add("kilesa", "मन के क्लेश रूपी")
add("saṃkilesika", "क्लेशों का विषय बनने वाला")
add("asaṃkilesika", "क्लेशों का विषय न बनने वाला")
add("saṃkiliṭṭha", "क्लेशों से मलिन")
add("asaṃkiliṭṭha", "क्लेशों से मलिन न होने वाला")
add("kilesasampayutta", "क्लेशों से जुड़ा")
add("kilesavippayutta", "क्लेशों से अलग")
add("kilesa ceva saṃkilesika ca", "मन के क्लेश रूपी भी और क्लेशों का विषय बनने वाला भी",
    "मन के क्लेश रूपी भी और क्लेशों का विषय बनने वाले भी")
add("saṃkilesika ceva no ca kilesa", "क्लेशों का विषय बनने वाला, पर स्वयं मन के क्लेश रूपी न होने वाला")
add("kilesa ceva saṃkiliṭṭha ca", "मन के क्लेश रूपी भी और क्लेशों से मलिन भी")
add("saṃkiliṭṭha ceva no ca kilesa", "क्लेशों से मलिन, पर स्वयं मन के क्लेश रूपी न होने वाला")
add("kilesa ceva kilesasampayutta ca", "मन के क्लेश रूपी भी और क्लेशों से जुड़ा भी", "मन के क्लेश रूपी भी और क्लेशों से जुड़े भी")
add("kilesasampayutta ceva no ca kilesa", "क्लेशों से जुड़ा, पर स्वयं मन के क्लेश रूपी न होने वाला")
# ch2 ^2-170 "kilesasampayuttā ceva no ca na kilesā" (as written)
add("kilesasampayutta ceva no ca na kilesa", "क्लेशों से जुड़ा, पर स्वयं मन के क्लेश रूपी न होने वाला नहीं")
add("kilesavippayuttasaṃkilesika", "क्लेशों से अलग, पर क्लेशों का विषय बनने वाला")
add("kilesavippayuttaasaṃkilesika", "क्लेशों से अलग और क्लेशों का विषय न बनने वाला")
# ch2 ^2-170 "upādāniyañceva upādānasampayuttañcā", "upādānasampayuttaupādāniyā" (as written)
add("upādāniya ceva upādānasampayutta ca", "आसक्ति का विषय बनने वाला भी और आसक्ति से जुड़ा भी")
add("upādānasampayuttaupādāniya", "आसक्ति से जुड़ा और उसका विषय बनने वाला")
# last dyads (^1-M2-83 … ^1-M2-100)
add("savitakka", "आरंभिक विचार वाला")
add("avitakka", "आरंभिक विचार से रहित")
add("savicāra", "सतत विचार वाला")
add("avicāra", "सतत विचार से रहित")
add("sappītika", "उल्लास वाला")
add("appītika", "उल्लास से रहित")
add("kāmāvacara", "इंद्रिय-सुखों के लोक से संबंधित")
add("rūpāvacara", "सूक्ष्म भौतिक लोक से संबंधित")
add("arūpāvacara", "अभौतिक लोक से संबंधित")
add("pariyāpanna", "अस्तित्व के लोकों में समाया हुआ")
add("apariyāpanna", "अस्तित्व के लोकों में न समाया हुआ")
add("niyyānika", "मुक्ति की ओर ले जाने वाला")
add("aniyyānika", "मुक्ति की ओर न ले जाने वाला")
add("niyata", "निश्चित")
add("anuttara", "सर्वोच्च")
add("sauttara", "सर्वोच्च न होने वाला", pred_neg="anuttara")
# ch2 ^2-170 "saṃyojanañceva saṃyojaniya"ntipi (no "ca", as written)
add("saṃyojana ceva saṃyojaniya", *P[norm("saṃyojana ceva saṃyojaniya ca")])
add("saraṇa", "संघर्ष वाला")
add("araṇa", "संघर्ष से रहित")


def lookup(p, predicate=False):
    """-> (sg, pl, neg)"""
    k = norm(p)
    if predicate and k in PRED_NEG:
        return P[norm(PRED_NEG[k])] + (True,)
    if k in P:
        return P[k] + (False,)
    for n in ("na ", "no "):
        if k.startswith(n) and k[3:] in P:
            return P[k[3:]] + (True,)
    raise KeyError(f"no predicate for {p!r} (key {k!r})")


# ---------------------------------------------------------------- sentence parser and Hindi assembly
QITEM = re.compile(r'^"([^"]*)"\s*(n?)(ti)?(pi)?$')


class Subj:
    def __init__(self, direct, oblique, plural_):
        self.d, self.o, self.pl = direct, oblique, plural_


def _verb(pl, neg, habitual):
    if habitual:
        return ("नहीं होते" if pl else "नहीं होता") if neg else ("होते हैं" if pl else "होता है")
    return ("नहीं हैं" if pl else "नहीं है") if neg else ("हैं" if pl else "है")


def _form(entry, pl):
    return entry[1] if pl else entry[0]


def _split_top(s):
    """split a clause string on ', ' and '; ' outside quotes; keep the separator."""
    out, buf, q, i = [], "", False, 0
    while i < len(s):
        c = s[i]
        if c == '"':
            q = not q
        if not q and s[i:i + 2] in (", ", "; "):
            out.append((buf, s[i]))
            buf, i = "", i + 2
            continue
        buf += c
        i += 1
    out.append((buf, ""))
    return out


def quoted(items, pl):
    """items: list of raw Pāli items like '"sukhāya vedanāya sampayuttā"tipi' -> Hindi list."""
    parsed = []
    for it in items:
        m = QITEM.match(it.strip())
        if not m:
            raise ValueError(f"bad quoted item {it!r}")
        txt, n, ti, pi = m.groups()
        if n:
            txt += "ṃ"
        parsed.append((txt, bool(pi)))
    use_na = any(pi for _, pi in parsed)
    hs = []
    for txt, _ in parsed:
        sg, plf, neg = lookup(txt)
        if neg:
            raise KeyError(f"negated quoted item {txt!r}")
        h = "“" + (plf if pl else sg) + "”"
        hs.append(("न " + h) if use_na else h)
    return ", ".join(hs)


def sentence(subj, rest, end="।"):
    """rest = Pāli after the subject, without the final '.'"""
    parts = _split_top(rest)
    clauses = []  # (kind, payload, sep)
    i = 0
    while i < len(parts):
        txt, sep = parts[i]
        t = txt.strip()
        m = re.match(r"^(siyā )?na vattabb(?:ā|aṃ|o) – (.*)$", t)
        if m:
            items = [m.group(2)]
            while sep == "," and i + 1 < len(parts) and parts[i + 1][0].strip().startswith('"') \
                    and items[-1].rstrip().endswith("pi"):
                i += 1
                items.append(parts[i][0])
                sep = parts[i][1]
            clauses.append(("vatt", (bool(m.group(1)), items), sep))
        elif t.startswith("siyā "):
            clauses.append(("siya", t[5:], sep))
        else:
            clauses.append(("plain", t, sep))
        i += 1
    out, after_vatt, seen_siya = [], False, False
    pron = "वे" if subj.pl else "वह"
    obj = "उन्हें" if subj.pl else "उसे"
    for k, (kind, payload, sep) in enumerate(clauses):
        first = k == 0
        if kind == "vatt":
            siy, items = payload
            q = quoted(items, subj.pl)
            if first:
                h = f"{subj.o} को नहीं कहा जा सकता {DASH} {q}"
            elif siy:
                h = f"कभी {obj} नहीं कहा जा सकता {DASH} {q}"
            else:
                h = f"{obj} नहीं कहा जा सकता {DASH} {q}"
            after_vatt = True
        else:
            if kind == "plain" and payload.startswith('"'):   # a further quoted item after a "…"ti list (as written)
                sg, plf, neg = lookup(payload.strip('"'))
                h = "“" + (plf if subj.pl else sg) + "”"
                out.append(h + (sep and sep + " " or ""))
                continue
            sg, plf, neg = lookup(payload, predicate=True)
            form = plf if subj.pl else sg
            habitual = kind == "siya" or seen_siya
            v = _verb(subj.pl, neg, habitual)
            h = (f"कभी {form} {v}" if kind == "siya" else f"{form} {v}")
            if first:
                h = f"{subj.d} {h}"
            elif after_vatt:
                h = f"{pron} {h}"
                after_vatt = False
            if kind == "siya":
                seen_siya = True
        out.append(h + (sep and sep + " " or ""))
    return "".join(out).rstrip() + end


def split_sentences(line):
    """Pāli paragraph -> sentences (without the final '.'); keeps a trailing 'ti' marker off."""
    s = re.split(r'(?<=\.)\s+(?=[A-ZĀĪŪṬḌṆÑṄ"])|(?<=")\.\s+', line.strip())
    out = []
    for x in s:
        x = x.strip()
        if x.endswith("."):
            x = x[:-1]
        out.append(x)
    return out


# two predicates in one clause without a comma: parsed as two clauses (the Hindi gets the comma)
SPLIT_FIX = [("mahaggatārammaṇaṃ na appamāṇārammaṇaṃ", "mahaggatārammaṇaṃ, na appamāṇārammaṇaṃ"),
             ("na maggārammaṇaṃ maggahetukaṃ", "na maggārammaṇaṃ, maggahetukaṃ"),
             ("maggārammaṇaṃ na maggahetukaṃ", "maggārammaṇaṃ, na maggahetukaṃ")]


def paragraph(line, subjects, overrides):
    """subjects: [(pāli prefix, Subj)] longest first; overrides: {pāli sentence: hindi sentence}."""
    hs = []
    for s in split_sentences(line):
        for a, b in SPLIT_FIX:
            s = s.replace(a, b)
        if s in overrides:
            hs.append(overrides[s])
            continue
        for pref, subj in subjects:
            if s.startswith(pref + " "):
                rest = s[len(pref) + 1:]
                break
        else:
            raise ValueError(f"no subject: {s!r}")
        rest = re.sub(r"(araṇ(?:ā|a))(?:n)?ti$", lambda m: m.group(1) + ("ṃ" if m.group(0).endswith("nti") else ""), rest)
        kenaci = "; kenaci viññeyyā, kenaci na viññeyyā"
        if rest.endswith(kenaci):   # "…; kenaci viññeyyā, kenaci na viññeyyā" (same wording as chapter 1)
            a, b = P[norm("kenaci viññeyya")], P[norm("kenaci na viññeyya")]
            i = 1 if subj.pl else 0
            tail = f"; {'वे' if subj.pl else 'वह'} {a[i]} भी {'हैं' if subj.pl else 'है'}, {b[i]} भी {'हैं' if subj.pl else 'है'}।"
            hs.append(sentence(subj, rest[: -len(kenaci)], end="") + tail)
            continue
        hs.append(sentence(subj, rest))
    return " ".join(hs)
