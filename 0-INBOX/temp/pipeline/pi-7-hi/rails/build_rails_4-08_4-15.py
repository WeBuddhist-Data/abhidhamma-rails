"""pi-7 Paṭṭhāna, Hindi plain RAILS: builder for 4-08 .. 4-15 (dukatika nīvaraṇa .. saraṇa, tikaduka hetu).

Uses the approved sample constants read-only (build_rails_sample as S). New recurring formulas: notes-4-08_4-15.md.
usage: python -I -B -X utf8 build_rails_4-08_4-15.py [file.md ...]
"""
import os
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\rails")
import build_rails_sample as S  # noqa: E402  (read-only)

FILES = ["4-08-dukatika-nivaranaduka.md", "4-09-dukatika-paramasaduka.md", "4-10-dukatika-sarammanaduka.md",
         "4-11-dukatika-upadanaduka.md", "4-12-dukatika-kilesaduka.md", "4-13-dukatika-dassanenapahatabbaduka.md",
         "4-14-dukatika-saranaduka.md", "4-15-tikaduka-hetuduka.md"]

# ---------------------------------------------------------------- numbers

NUM = dict(S.NUM)
NUM.update({"dasa": "दस", "ekādasa": "ग्यारह", "dvādasa": "बारह", "terasa": "तेरह", "cuddasa": "चौदह",
            "pannarasa": "पंद्रह", "soḷasa": "सोलह", "sattarasa": "सत्रह", "aṭṭhārasa": "अठारह",
            "ekūnavīsati": "उन्नीस", "vīsati": "बीस", "vīsa": "बीस", "ekavīsa": "इक्कीस", "bāvīsa": "बाईस",
            "tevīsa": "तेईस", "catuvīsa": "चौबीस", "pañcavīsa": "पच्चीस", "chabbīsa": "छब्बीस", "sattavīsa": "सत्ताईस",
            "aṭṭhavīsa": "अट्ठाईस", "ekūnatiṃsa": "उनतीस", "tiṃsa": "तीस", "ekatiṃsa": "इकतीस", "dvattiṃsa": "बत्तीस",
            "tettiṃsa": "तैंतीस", "catuttiṃsa": "चौंतीस", "pañcatiṃsa": "पैंतीस", "chattiṃsa": "छत्तीस",
            "sattatiṃsa": "सैंतीस", "aṭṭhatiṃsa": "अड़तीस"})

# ---------------------------------------------------------------- items (feminine singular, agreeing with परिघटना)
# Inside a combined (duka-tika / tika-duka) item the commas of the pi-1 wording are dropped (as in the termbase),
# so that the only comma marks the boundary between the two classifications.

LEX = {}  # surface (lowercase) -> (Hindi, carries 'ca')


def add(hindi, *surfaces):
    for s in surfaces:
        LEX[s] = (hindi, False)
        LEX[(s[:-1] + "ñca") if s.endswith("ṃ") else (s + " ca")] = (hindi, True)


def A(stem, hindi):
    """a-stem adjective: stem 'kusala' -> kusalaṃ / kusalo / kusalassa (+ ñca / ca)."""
    add(hindi, stem + "ṃ", stem[:-1] + "o", stem + "ssa")


def ceva_ca(x, y, hindi):
    """'both X and Y' items: Xañceva Yañca / Xo ceva Yo ca / Xassa ceva Yassa ca (+ forms used in coordination)."""
    for s in (f"{x}ñceva {y}ñca", f"{x}ñceva {y}ṃ", f"{x[:-1]}o ceva {y[:-1]}o ca", f"{x[:-1]}o ca {y[:-1]}o ca",
              f"{x}ssa ceva {y}ssa ca"):
        LEX[s] = (hindi, False)


def ceva_noca(y, x, hindi, neg="no"):
    """'Y but not X' items: Yañceva no ca Xaṃ / Yo ceva no ca Xo / Yassa ceva no ca Xassa."""
    for s in (f"{y}ñceva {neg} ca {x}ṃ", f"{y[:-1]}o ceva {neg} ca {x[:-1]}o", f"{y}ssa ceva {neg} ca {x}ssa"):
        LEX[s] = (hindi, False)


def pair(x, y, hindi):
    """two-word items: Xaṃ Yaṃ / Xo Yo / Xassa Yassa."""
    add(hindi, f"{x}ṃ {y}ṃ", f"{x[:-1]}o {y[:-1]}o", f"{x}ssa {y}ssa")


# kusalattika and the other triads
for st, h in [
    ("kusala", "हितकर"), ("akusala", "हानिकर"), ("abyākata", "नैतिक रूप से अनिर्धारित"),
    ("sukhāya vedanāya sampayutta", "सुखद अनुभूति से जुड़ी"), ("dukkhāya vedanāya sampayutta", "दुःखद अनुभूति से जुड़ी"),
    ("adukkhamasukhāya vedanāya sampayutta", "न दुःखद, न सुखद अनुभूति से जुड़ी"),
    ("vipāka", "कर्म-फल रूपी"),
    ("upādinnupādāniya", "कर्म से उत्पन्न और आसक्ति का विषय बनने वाली"),
    ("anupādinnupādāniya", "कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाली"),
    ("anupādinnaanupādāniya", "न कर्म से उत्पन्न, न आसक्ति का विषय बनने वाली"),
    ("saṃkiliṭṭhasaṃkilesika", "क्लेशों से मलिन और क्लेशों का विषय बनने वाली"),
    ("asaṃkiliṭṭhasaṃkilesika", "क्लेशों से मलिन न होने वाली, पर क्लेशों का विषय बनने वाली"),
    ("asaṃkiliṭṭhaasaṃkilesika", "क्लेशों से मलिन न होने वाली और क्लेशों का विषय न बनने वाली"),
    ("savitakkasavicāra", "आरंभिक विचार और सतत विचार वाली"),
    ("avitakkavicāramatta", "आरंभिक विचार से रहित, केवल सतत विचार वाली"),
    ("avitakkaavicāra", "आरंभिक विचार और सतत विचार दोनों से रहित"),
    ("pītisahagata", "उल्लास के साथ होने वाली"), ("sukhasahagata", "सुख के साथ होने वाली"),
    ("upekkhāsahagata", "समभाव के साथ होने वाली"), ("naupekkhāsahagata", "समभाव के साथ न होने वाली"),
    ("dassanena pahātabba", "सत्य-दर्शन से छोड़ी जाने वाली"),
    ("nadassanena pahātabba", "सत्य-दर्शन से न छोड़ी जाने वाली"),
    ("bhāvanāya pahātabba", "मानसिक अभ्यास से छोड़ी जाने वाली"),
    ("nabhāvanāya pahātabba", "मानसिक अभ्यास से न छोड़ी जाने वाली"),
    ("nevadassanena nabhāvanāya pahātabba", "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़ी जाने वाली"),
    ("dassanena pahātabbahetuka", "सत्य-दर्शन से छोड़े जाने वाले मूलों वाली"),
    ("nadassanena pahātabbahetuka", "सत्य-दर्शन से छोड़े जाने वाले मूलों से रहित"),
    ("bhāvanāya pahātabbahetuka", "मानसिक अभ्यास से छोड़े जाने वाले मूलों वाली"),
    ("nabhāvanāya pahātabbahetuka", "मानसिक अभ्यास से छोड़े जाने वाले मूलों से रहित"),
    ("nevadassanena nabhāvanāya pahātabbahetuka", "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़े जाने वाले मूलों वाली"),
    ("sekkha", "सीखने के चरण की"), ("asekkha", "सीखना पूरा होने के चरण की"),
    ("nevasekkhanāsekkha", "न सीखने के चरण की, न सीखना पूरा होने के चरण की"),
    ("paritta", "सीमित"), ("mahaggata", "उन्नत"), ("appamāṇa", "अपरिमित"),
    ("parittārammaṇa", "सीमित विषय वाली"), ("mahaggatārammaṇa", "उन्नत विषय वाली"),
    ("appamāṇārammaṇa", "अपरिमित विषय वाली"),
    ("hīna", "हीन"), ("majjhima", "मध्यम"), ("paṇīta", "उत्तम"),
    ("micchattaniyata", "ग़लत दिशा में निश्चित"), ("sammattaniyata", "सही दिशा में निश्चित"), ("aniyata", "अनिश्चित"),
    ("maggārammaṇa", "मार्ग को विषय बनाने वाली"), ("maggahetuka", "मार्ग को मूल बनाने वाली"),
    ("uppanna", "उत्पन्न हो चुकी"), ("anuppanna", "उत्पन्न न हुई"),
    ("atīta", "अतीत की"), ("anāgata", "भविष्य की"), ("paccuppanna", "वर्तमान की"),
    ("atītārammaṇa", "अतीत के विषय वाली"), ("anāgatārammaṇa", "भविष्य के विषय वाली"),
    ("paccuppannārammaṇa", "वर्तमान के विषय वाली"),
    ("ajjhatta", "स्वयं से संबंधित"),
    ("ajjhattārammaṇa", "स्वयं से संबंधित विषय वाली"), ("bahiddhārammaṇa", "दूसरों से संबंधित विषय वाली"),
    ("ajjhattabahiddhārammaṇa", "स्वयं और दूसरों दोनों से संबंधित विषय वाली"),
    ("sanidassanasappaṭigha", "दिखाई देने वाली और टकराव वाली"),
    ("anidassanasappaṭigha", "दिखाई न देने वाली, पर टकराव वाली"),
    ("anidassanaappaṭigha", "दिखाई न देने वाली और टकराव से रहित"),
]:
    A(st, h)
A("vipākadhammadhamma", "कर्म-फल उत्पन्न करने वाली")
A("nevavipākanavipākadhammadhamma", "न कर्म-फल रूपी, न कर्म-फल उत्पन्न करने वाली")
# duka-tika: «saraṇaṃ vipākadhammadhammaṃ paṭicca» has no separate noun; FUSED splits it off before parsing
add("कर्म-फल उत्पन्न करने वाली", "vipākadhamma")
add("न कर्म-फल रूपी, न कर्म-फल उत्पन्न करने वाली", "nevavipākanavipākadhamma")
FUSED = re.compile(r"(?<![\w])((?:nevavipākana)?vipākadhamma)dhamm(aṃ|o|ā|assa)(?= (?:paṭicca|uppajj))")
for b, h in [("ācayagām", "संचय की ओर ले जाने वाली"), ("apacayagām", "संचय घटाने की ओर ले जाने वाली"),
             ("nevācayagāmināpacayagām", "न संचय की ओर, न संचय घटाने की ओर ले जाने वाली"),
             ("uppād", "उत्पन्न होने वाली")]:
    add(h, b + "iṃ", b + "ī", b + "issa", b + "ino")
add("मार्ग की प्रधानता वाली", "maggādhipatiṃ", "maggādhipati", "maggādhipatissa", "maggādhipatino")
add("दूसरों से संबंधित", "bahiddhā")
add("स्वयं और दूसरों दोनों से संबंधित", "ajjhattabahiddhā")

# dyads of 4-08 .. 4-13 (pi-1 matrix wording)
for st, h in [
    ("nīvaraṇa", "बाधा रूपी"), ("nonīvaraṇa", "बाधा रूपी न होने वाली"),
    ("nīvaraṇiya", "बाधाओं का विषय बनने वाली"), ("anīvaraṇiya", "बाधाओं का विषय न बनने वाली"),
    ("nīvaraṇasampayutta", "बाधाओं से जुड़ी"), ("nīvaraṇavippayutta", "बाधाओं से अलग"),
    ("parāmāsa", "ग़लत धारणा रूपी"), ("noparāmāsa", "ग़लत धारणा रूपी न होने वाली"),
    ("parāmaṭṭha", "ग़लत धारणा का विषय बनने वाली"), ("aparāmaṭṭha", "ग़लत धारणा का विषय न बनने वाली"),
    ("parāmāsasampayutta", "ग़लत धारणा से जुड़ी"), ("parāmāsavippayutta", "ग़लत धारणा से अलग"),
    ("sārammaṇa", "विषय वाली"), ("anārammaṇa", "विषय से रहित"),
    ("citta", "मन रूपी"), ("nocitta", "मन रूपी न होने वाली"),
    ("cetasika", "मन की सहचर"), ("acetasika", "मन की सहचर न होने वाली"),
    ("cittasampayutta", "मन से जुड़ी"), ("cittavippayutta", "मन से अलग"),
    ("cittasaṃsaṭṭha", "मन से घुली-मिली"), ("nocittasaṃsaṭṭha", "मन से घुली-मिली न होने वाली"),
    ("cittasamuṭṭhāna", "मन से उत्पन्न"), ("nocittasamuṭṭhāna", "मन से उत्पन्न न होने वाली"),
    ("cittasaṃsaṭṭhasamuṭṭhāna", "मन से घुली-मिली और मन से उत्पन्न"),
    ("nocittasaṃsaṭṭhasamuṭṭhāna", "मन से घुली-मिली और मन से उत्पन्न न होने वाली"),
    ("ajjhattika", "आंतरिक"), ("bāhira", "बाह्य"),
    ("upādinna", "कर्म से उत्पन्न"), ("anupādinna", "कर्म से उत्पन्न न होने वाली"),
    ("upādāna", "आसक्ति रूपी"), ("noupādāna", "आसक्ति रूपी न होने वाली"),
    ("upādāniya", "आसक्ति का विषय बनने वाली"), ("anupādāniya", "आसक्ति का विषय न बनने वाली"),
    ("upādānasampayutta", "आसक्ति से जुड़ी"), ("upādānavippayutta", "आसक्ति से अलग"),
    ("kilesa", "मन के क्लेश रूपी"), ("nokilesa", "मन के क्लेश रूपी न होने वाली"),
    ("saṃkilesika", "क्लेशों का विषय बनने वाली"), ("asaṃkilesika", "क्लेशों का विषय न बनने वाली"),
    ("saṃkiliṭṭha", "क्लेशों से मलिन"), ("asaṃkiliṭṭha", "क्लेशों से मलिन न होने वाली"),
    ("kilesasampayutta", "क्लेशों से जुड़ी"), ("kilesavippayutta", "क्लेशों से अलग"),
    ("savitakka", "आरंभिक विचार वाली"), ("avitakka", "आरंभिक विचार से रहित"),
    ("savicāra", "सतत विचार वाली"), ("avicāra", "सतत विचार से रहित"),
    ("sappītika", "उल्लास वाली"), ("appītika", "उल्लास से रहित"),
    ("kāmāvacara", "इंद्रिय-सुखों के लोक से संबंधित"),
    ("nakāmāvacara", "इंद्रिय-सुखों के लोक से संबंधित न होने वाली"),
    ("rūpāvacara", "सूक्ष्म भौतिक लोक से संबंधित"), ("narūpāvacara", "सूक्ष्म भौतिक लोक से संबंधित न होने वाली"),
    ("arūpāvacara", "अभौतिक लोक से संबंधित"), ("naarūpāvacara", "अभौतिक लोक से संबंधित न होने वाली"),
    ("pariyāpanna", "अस्तित्व के लोकों में समाई हुई"), ("apariyāpanna", "अस्तित्व के लोकों में न समाई हुई"),
    ("niyyānika", "मुक्ति की ओर ले जाने वाली"), ("aniyyānika", "मुक्ति की ओर न ले जाने वाली"),
    ("niyata", "निश्चित"),
    ("sauttara", "सर्वोच्च न होने वाली"), ("anuttara", "सर्वोच्च"),
    ("saraṇa", "संघर्ष वाली"), ("araṇa", "संघर्ष से रहित"),
    ("sahetuka", "मूल वाली"), ("ahetuka", "मूल से रहित"),
    ("hetusampayutta", "मूलों से जुड़ी"), ("hetuvippayutta", "मूलों से अलग"),
]:
    A(st, h)
for b, h in [("cittasahabh", "मन के साथ-साथ होने वाली"), ("nocittasahabh", "मन के साथ-साथ न होने वाली"),
             ("cittasaṃsaṭṭhasamuṭṭhānasahabh", "मन से घुली-मिली, मन से उत्पन्न और मन के साथ-साथ होने वाली"),
             ("nocittasaṃsaṭṭhasamuṭṭhānasahabh", "मन से घुली-मिली, मन से उत्पन्न और मन के साथ-साथ न होने वाली")]:
    add(h, b + "uṃ", b + "ū", b + "uno", b + "ussa")
for b, h in [("cittānuparivatt", "मन का अनुसरण करने वाली"), ("nocittānuparivatt", "मन का अनुसरण न करने वाली"),
             ("cittasaṃsaṭṭhasamuṭṭhānānuparivatt", "मन से घुली-मिली, मन से उत्पन्न और मन का अनुसरण करने वाली"),
             ("nocittasaṃsaṭṭhasamuṭṭhānānuparivatt", "मन से घुली-मिली, मन से उत्पन्न और मन का अनुसरण न करने वाली")]:
    add(h, b + "iṃ", b + "ī", b + "ino", b + "issa")
add("व्युत्पन्न", "upādā")
add("व्युत्पन्न न होने वाली", "noupādā")
add("मूल रूपी", "hetuṃ", "hetu", "hetussa")
add("मूल रूपी न होने वाली", "nahetuṃ", "nahetu", "nahetussa")

for x, y, ny, gx, gy, gyn, pron in [
    ("nīvaraṇa", "nīvaraṇiya", "anīvaraṇiya", "बाधा रूपी", "बाधाओं का विषय बनने वाली", "बाधाओं का विषय न बनने वाली", "उनका"),
    ("parāmāsa", "parāmaṭṭha", "aparāmaṭṭha", "ग़लत धारणा रूपी", "ग़लत धारणा का विषय बनने वाली",
     "ग़लत धारणा का विषय न बनने वाली", "उसका"),
    ("upādāna", "upādāniya", "anupādāniya", "आसक्ति रूपी", "आसक्ति का विषय बनने वाली", "आसक्ति का विषय न बनने वाली",
     "उसका"),
    ("kilesa", "saṃkilesika", "asaṃkilesika", "मन के क्लेश रूपी", "क्लेशों का विषय बनने वाली",
     "क्लेशों का विषय न बनने वाली", "क्लेशों का"),
]:
    neg = f"स्वयं {gx} न होने वाली"
    ceva_ca(x, y, f"{gx} भी और {gy} भी")
    ceva_noca(y, x, f"{gy}, पर {neg}")
    sx = {"nīvaraṇa": "बाधाओं", "parāmāsa": "ग़लत धारणा", "upādāna": "आसक्ति", "kilesa": "क्लेशों"}[x]
    vip = {"kilesa": "kilesavippayutta"}.get(x, x + "vippayutta")
    ceva_ca(x, x + "sampayutta" if x != "kilesa" else "kilesasampayutta", f"{gx} भी और {sx} से जुड़ी भी")
    ceva_noca(x + "sampayutta" if x != "kilesa" else "kilesasampayutta", x, f"{sx} से जुड़ी, पर {neg}")
    pair(vip, y, f"{sx} से अलग, पर {pron} विषय बनने वाली")
    pair(vip, ny, f"{sx} से अलग और {pron} विषय न बनने वाली")
ceva_ca("kilesa", "saṃkiliṭṭha", "मन के क्लेश रूपी भी और क्लेशों से मलिन भी")
ceva_noca("saṃkiliṭṭha", "kilesa", "क्लेशों से मलिन, पर स्वयं मन के क्लेश रूपी न होने वाली")
# kilesavippayutta saṃkilesika: the pi-1 wording repeats «क्लेशों का»
pair("kilesavippayutta", "saṃkilesika", "क्लेशों से अलग, पर क्लेशों का विषय बनने वाली")
pair("kilesavippayutta", "asaṃkilesika", "क्लेशों से अलग और क्लेशों का विषय न बनने वाली")

# hetu cluster (tikaduka)
for s in ("hetuñceva sahetukañca", "hetuñceva sahetukaṃ", "hetu ceva sahetuko ca", "hetussa ceva sahetukassa ca"):
    LEX[s] = ("मूल रूपी भी और मूल वाली भी", False)
for s in ("hetuñceva hetusampayuttañca", "hetuñceva hetusampayuttaṃ", "hetu ceva hetusampayutto ca",
          "hetussa ceva hetusampayuttassa ca"):
    LEX[s] = ("मूल रूपी भी और मूलों से जुड़ी भी", False)
for s in ("sahetukañceva na ca hetuṃ", "sahetuko ceva na ca hetu", "sahetukassa ceva na ca hetussa"):
    LEX[s] = ("मूल वाली, पर स्वयं मूल रूपी न होने वाली", False)
for s in ("hetusampayuttañceva na ca hetuṃ", "hetusampayutto ceva na ca hetu", "hetusampayuttassa ceva na ca hetussa"):
    LEX[s] = ("मूलों से जुड़ी, पर स्वयं मूल रूपी न होने वाली", False)
add("मूल रूपी न होने वाली, पर मूल वाली", "nahetuṃ sahetukaṃ", "nahetu sahetuko", "nahetussa sahetukassa")
add("मूल रूपी न होने वाली और मूल से रहित", "nahetuṃ ahetukaṃ", "nahetu ahetuko", "nahetussa ahetukassa")

LEX_KEYS = sorted(LEX, key=len, reverse=True)
LEX_ALT = "|".join(re.escape(k) for k in LEX_KEYS)


def tokenize(s):
    """Split an item sequence into lexicon items (longest first, with backtracking)."""
    s = s.strip()
    if not s:
        return []
    for k in LEX_KEYS:
        if s == k or s.startswith(k + " "):
            rest = tokenize(s[len(k):]) if s != k else []
            if rest is not None:
                return [LEX[k]] + rest
    return None


def join_and(parts, word="और"):
    return parts[0] if len(parts) == 1 else ", ".join(parts[:-1]) + f" {word} " + parts[-1]


def join_shared(parts):
    """members sharing one noun: «A और B»; «A तथा B» when a member already holds «और» (no ambiguity)."""
    return join_and(parts, "तथा" if any(" और " in p for p in parts) else "और")


def np_hi(items, noun):
    """items: Pāli item sequence; noun: acc | nom_sg | nom_pl | dat.  Returns Hindi noun phrase."""
    toks = tokenize(items)
    if toks is None:
        raise KeyError(f"items: {items!r}")
    conjs, cur = [], []
    for h, ca in toks:
        cur.append(h)
        if ca:
            conjs.append(cur)
            cur = []
    shared = cur
    n = "परिघटनाएँ" if noun == "nom_pl" else "परिघटना"
    if not conjs:
        out = ", ".join(shared) + " " + n
    elif shared:
        out = join_shared([", ".join(c) for c in conjs]) + ", " + ", ".join(shared) + " " + n
    elif noun == "nom_pl":
        out = join_shared([", ".join(c) for c in conjs]) + " " + n
    else:
        out = join_and([", ".join(c) + " परिघटना" for c in conjs])
    return out + (" के लिए" if noun == "dat" else "")


ITEMS = rf"(?:(?:{LEX_ALT}) )+"
INS_ALT = "|".join(re.escape(k) for k in sorted(S.KEYS, key=len, reverse=True))
PATICCA_RE = re.compile(rf"(?<![^\s…(])({ITEMS})dhammaṃ paṭicca ({ITEMS})(dhammo uppajjati|dhammā uppajjanti) ({S.CHAIN_RE})")
PATICCA_BARE_RE = re.compile(rf"(?<![^\s…(])({ITEMS})dhammaṃ paṭicca(?=…)")
PANHA_RE = re.compile(rf"(?<![^\s…(])({ITEMS})(dhammo|dhammā) ({ITEMS})dhammassa ({INS_ALT})paccayena paccayo"
                      rf"((?:(?:…pe…|…) ?(?:{INS_ALT})paccayena paccayo)*)")


def paticca_hi(m):
    acc, nom, verb, chain = m.groups()
    pl = verb.startswith("dhammā")
    return (f"{np_hi(acc, 'acc')} {S.PATICCA} {np_hi(nom, 'nom_pl' if pl else 'nom_sg')} {S.CH(chain)} "
            f"{S.ARISES['p' if pl else 's']}")


def panha_hi(m):
    nom, noun, dat, k, tail = m.groups()
    g = "fp" if noun == "dhammā" else "fs"
    out = f"{np_hi(nom, 'nom_pl' if g == 'fp' else 'nom_sg')}, {np_hi(dat, 'dat')} {S.INS(k, g)}"
    out += re.sub(rf"({INS_ALT})paccayena paccayo", lambda t: S.INS(t.group(1), g), tail).replace("…pe…", "…")
    return out


# a line of conditions only, continuing the subject of the line before (^7-49-205: «Uppanno hetu dhammo …»)
INS_CHAIN_RE = re.compile(rf"^(?:{INS_ALT})paccayena paccayo(?:(?:…pe…|…) ?(?:{INS_ALT})paccayena paccayo)*")


# ---------------------------------------------------------------- names (headings, closings, notes)

NAMES = {
    # triads
    "kusalattika": "हितकर वाला तीन का वर्गीकरण", "vedanāttika": "अनुभूति वाला तीन का वर्गीकरण",
    "vipākattika": "कर्म-फल वाला तीन का वर्गीकरण",
    "upādinnattika": "कर्म से उत्पन्न परिघटनाओं वाला तीन का वर्गीकरण",
    "saṃkiliṭṭhattika": "क्लेशों से मलिन परिघटनाओं वाला तीन का वर्गीकरण",
    "vitakkattika": "आरंभिक विचार वाला तीन का वर्गीकरण", "pītittika": "उल्लास वाला तीन का वर्गीकरण",
    "dassanenapahātabbattika": "सत्य-दर्शन से छोड़ी जाने वाली परिघटनाओं वाला तीन का वर्गीकरण",
    "dassanenapahātabbahetukattika": "सत्य-दर्शन से छोड़े जाने वाले मूलों वाला तीन का वर्गीकरण",
    "ācayagāmittika": "संचय की ओर ले जाने वाला तीन का वर्गीकरण",
    "sekkhattika": "सीखने के चरण वाला तीन का वर्गीकरण", "parittattika": "सीमित वाला तीन का वर्गीकरण",
    "parittārammaṇattika": "सीमित विषय वाला तीन का वर्गीकरण", "hīnattika": "हीन वाला तीन का वर्गीकरण",
    "micchattaniyatattika": "ग़लत दिशा में निश्चित परिघटनाओं वाला तीन का वर्गीकरण",
    "micchattattika": "ग़लत दिशा में निश्चित परिघटनाओं वाला तीन का वर्गीकरण",
    "maggārammaṇattika": "मार्ग को विषय बनाने वाला तीन का वर्गीकरण",
    "uppannattika": "उत्पन्न वाला तीन का वर्गीकरण", "atītattika": "अतीत वाला तीन का वर्गीकरण",
    "atītārammaṇattika": "अतीत के विषय वाला तीन का वर्गीकरण",
    "ajjhattattika": "स्वयं से संबंधित परिघटनाओं वाला तीन का वर्गीकरण",
    "ajjhattārammaṇattika": "स्वयं से संबंधित विषय वाला तीन का वर्गीकरण",
    "sanidassanasappaṭighattika": "दिखाई देने वाला और टकराव वाला तीन का वर्गीकरण",
    "sanidassanattika": "दिखाई देने वाला और टकराव वाला तीन का वर्गीकरण",
    # dyads
    "hetuduka": "मूल वाला दो का वर्गीकरण", "sahetukaduka": "मूल वाली परिघटनाओं वाला दो का वर्गीकरण",
    "hetusampayuttaduka": "मूलों से जुड़ी परिघटनाओं वाला दो का वर्गीकरण",
    "hetusahetukaduka": "मूल रूपी भी और मूल वाली भी परिघटनाओं वाला दो का वर्गीकरण",
    "hetuhetusampayuttaduka": "मूल रूपी भी और मूलों से जुड़ी भी परिघटनाओं वाला दो का वर्गीकरण",
    "nahetusahetukaduka": "मूल रूपी न होने वाली पर मूल वाली परिघटनाओं वाला दो का वर्गीकरण",
    "sappaccayaduka": "कारणों पर निर्भर रहने वाली परिघटनाओं वाला दो का वर्गीकरण",
    "lokiyaduka": "लौकिक परिघटनाओं वाला दो का वर्गीकरण",
    "lokiyalokuttaraduka": "लौकिक और लोकोत्तर परिघटनाओं वाला दो का वर्गीकरण",
    "nīvaraṇaduka": "बाधा वाला दो का वर्गीकरण", "nīvaraṇiyaduka": "बाधाओं के विषय वाला दो का वर्गीकरण",
    "nīvaraṇasampayuttaduka": "बाधाओं से जुड़ाव वाला दो का वर्गीकरण",
    "nīvaraṇanīvaraṇiyaduka": "बाधा और बाधाओं के विषय वाला दो का वर्गीकरण",
    "nīvaraṇanīvaraṇasampayuttaduka": "बाधा और बाधाओं से जुड़ाव वाला दो का वर्गीकरण",
    "nīvaraṇavippayuttanīvaraṇiyaduka": "बाधाओं से अलगाव और बाधाओं के विषय वाला दो का वर्गीकरण",
    "parāmāsaduka": "ग़लत धारणा वाला दो का वर्गीकरण",
    "parāmaṭṭhaduka": "ग़लत धारणा के विषय वाला दो का वर्गीकरण",
    "parāmāsasampayuttaduka": "ग़लत धारणा से जुड़ाव वाला दो का वर्गीकरण",
    "parāmāsaparāmaṭṭhaduka": "ग़लत धारणा और ग़लत धारणा के विषय वाला दो का वर्गीकरण",
    "parāmāsavippayuttaparāmaṭṭhaduka": "ग़लत धारणा से अलगाव और ग़लत धारणा के विषय वाला दो का वर्गीकरण",
    "sārammaṇaduka": "विषय वाली परिघटनाओं वाला दो का वर्गीकरण",
    "cittaduka": "मन रूपी परिघटनाओं वाला दो का वर्गीकरण",
    "cetasikaduka": "मन की सहचर परिघटनाओं वाला दो का वर्गीकरण",
    "cittasampayuttaduka": "मन से जुड़ी परिघटनाओं वाला दो का वर्गीकरण",
    "cittasaṃsaṭṭhaduka": "मन से घुली-मिली परिघटनाओं वाला दो का वर्गीकरण",
    "cittasamuṭṭhānaduka": "मन से उत्पन्न परिघटनाओं वाला दो का वर्गीकरण",
    "cittasahabhūduka": "मन के साथ-साथ होने वाली परिघटनाओं वाला दो का वर्गीकरण",
    "cittānuparivattiduka": "मन का अनुसरण करने वाली परिघटनाओं वाला दो का वर्गीकरण",
    "cittasaṃsaṭṭhasamuṭṭhānaduka": "मन से घुली-मिली और मन से उत्पन्न परिघटनाओं वाला दो का वर्गीकरण",
    "cittasaṃsaṭṭhasamuṭṭhānasahabhūduka":
        "मन से घुली-मिली मन से उत्पन्न और मन के साथ-साथ होने वाली परिघटनाओं वाला दो का वर्गीकरण",
    "cittasaṃsaṭṭhasamuṭṭhānānuparivattiduka":
        "मन से घुली-मिली मन से उत्पन्न और मन का अनुसरण करने वाली परिघटनाओं वाला दो का वर्गीकरण",
    "ajjhattikaduka": "आंतरिक परिघटनाओं वाला दो का वर्गीकरण",
    "upādāduka": "व्युत्पन्न परिघटनाओं वाला दो का वर्गीकरण",
    "upādinnaduka": "कर्म से उत्पन्न परिघटनाओं वाला दो का वर्गीकरण",
    "upādānaduka": "आसक्ति वाला दो का वर्गीकरण",
    "upādāniyaduka": "आसक्ति का विषय बनने वाली परिघटनाओं वाला दो का वर्गीकरण",
    "upādānasampayuttaduka": "आसक्ति से जुड़ी परिघटनाओं वाला दो का वर्गीकरण",
    "upādānaupādāniyaduka": "आसक्ति रूपी भी और आसक्ति का विषय बनने वाली भी परिघटनाओं वाला दो का वर्गीकरण",
    "upādānaupādānasampayuttaduka": "आसक्ति रूपी भी और आसक्ति से जुड़ी भी परिघटनाओं वाला दो का वर्गीकरण",
    "upādānavippayuttaupādāniyaduka": "आसक्ति से अलग पर उसका विषय बनने वाली परिघटनाओं वाला दो का वर्गीकरण",
    "kilesaduka": "मन के क्लेश वाला दो का वर्गीकरण",
    "saṃkilesikaduka": "क्लेशों का विषय बनने वाला दो का वर्गीकरण",
    "saṃkiliṭṭhaduka": "क्लेशों से मलिन परिघटनाओं वाला दो का वर्गीकरण",
    "kilesasampayuttaduka": "क्लेशों से जुड़ाव वाला दो का वर्गीकरण",
    # Saṃkilesasaṃkilesikaduka (heading 79-1) is the Kilesasaṃkilesika dyad; saṃkilesa = kilesa
    "saṃkilesasaṃkilesikaduka": "मन के क्लेश और क्लेशों का विषय बनने वाला दो का वर्गीकरण",
    "kilesasaṃkiliṭṭhaduka": "मन के क्लेश और क्लेशों से मलिन परिघटनाओं वाला दो का वर्गीकरण",
    "kilesakilesasampayuttaduka": "मन के क्लेश और क्लेशों से जुड़ाव वाला दो का वर्गीकरण",
    "kilesavippayuttasaṃkilesikaduka": "क्लेशों से अलगाव और क्लेशों का विषय बनने वाला दो का वर्गीकरण",
    "dassanenapahātabbaduka": "सत्य-दर्शन से छोड़े जाने वाला दो का वर्गीकरण",
    "bhāvanāyapahātabbaduka": "मानसिक अभ्यास से छोड़े जाने वाला दो का वर्गीकरण",
    "dassanenapahātabbahetukaduka": "सत्य-दर्शन से छोड़े जाने वाले मूलों वाला दो का वर्गीकरण",
    "bhāvanāyapahātabbahetukaduka": "मानसिक अभ्यास से छोड़े जाने वाले मूलों वाला दो का वर्गीकरण",
    "savitakkaduka": "आरंभिक विचार वाला दो का वर्गीकरण", "savicāraduka": "सतत विचार वाला दो का वर्गीकरण",
    "sappītikaduka": "उल्लास वाला दो का वर्गीकरण",
    "pītisahagatādiduka": "उल्लास के साथ होने वाला दो का वर्गीकरण आदि",
    "upekkhāsahagataduka": "समभाव के साथ होने वाला दो का वर्गीकरण",
    "kāmāvacaraduka": "इंद्रिय-सुखों के लोक वाला दो का वर्गीकरण",
    "rūpāvacaraduka": "सूक्ष्म भौतिक लोक वाला दो का वर्गीकरण",
    "arūpāvacaraduka": "अभौतिक लोक वाला दो का वर्गीकरण",
    "pariyāpannaduka": "अस्तित्व के लोकों में समाए होने वाला दो का वर्गीकरण",
    "niyyānikaduka": "मुक्ति की ओर ले जाने वाला दो का वर्गीकरण", "niyataduka": "निश्चित वाला दो का वर्गीकरण",
    "sauttaraduka": "सर्वोच्च न होने वाला दो का वर्गीकरण", "saraṇaduka": "संघर्ष वाला दो का वर्गीकरण",
    # clusters (pi-1)
    "hetugocchaka": "मूलों का वर्ग", "nīvaraṇagocchaka": "बाधाओं का वर्ग", "parāmāsagocchaka": "ग़लत धारणा का वर्ग",
    "upādānagocchaka": "आसक्ति का वर्ग", "kilesagocchaka": "मन के क्लेशों का वर्ग",
    "mahantaraduka": "बीच के बड़े दो-दो के वर्गीकरण", "piṭṭhiduka": "अंतिम दो-दो के वर्गीकरण",
}


def oblique(name):
    return name.replace("वाला दो का वर्गीकरण", "वाले दो के वर्गीकरण").replace(
        "वाला तीन का वर्गीकरण", "वाले तीन के वर्गीकरण").replace("दो-दो के वर्गीकरण", "दो-दो के वर्गीकरणों")


PADA = {"kusala": "हितकर", "akusala": "हानिकर", "abyākata": "नैतिक रूप से अनिर्धारित"}

# ---------------------------------------------------------------- headings

HEAD = dict(S.HEAD)
HEAD.update({
    "Paccayacatukkaṃ": "कारणों के चार क्रम",
    "Paṭiccavārādi": "निर्भरता का खंड आदि",
    "Paccanīyaṃ": "नकारात्मक क्रम",
    "Paccanīyuddhāro": "नकारात्मक क्रम के लिए कारणों की छँटाई",
    "Hetupadaṃ": "मूल रूपी पद",
    "Nahetupadaṃ": "मूल रूपी न होने वाला पद",
    "Ahetukapadaṃ": "मूल से रहित पद",
    "Hetuvippayuttapadaṃ": "मूलों से अलग पद",
    "Sahetukanahetupadaṃ": "मूल वाला पर मूल रूपी न होने वाला पद",
    "Hetusampayuttanahetupadaṃ": "मूलों से जुड़ा पर मूल रूपी न होने वाला पद",
    "Nahetuahetukapadaṃ": "मूल रूपी न होने वाला और मूल से रहित पद",
    "Nahetupadapaccayacatukkaṃ": "मूल रूपी न होने वाले पद के कारणों के चार क्रम",
    "Dhammānulome tikadukapaṭṭhānaṃ": "परिघटनाओं का सकारात्मक क्रम: तीन-तीन और दो-दो के वर्गीकरणों के कारण-संबंध",
})

COND_STEMS = sorted(S.KEYS, key=len, reverse=True)


def cond_list(s):
    """'Nahetunaārammaṇa' / 'hetu-ārammaṇa-adhipati' -> list of Hindi names (negated where na-/no-)."""
    out = []
    s = s.lower().replace("-", "")
    while s:
        # prefer a plain stem (natthi is a stem, not na + atthi); else a negated one
        k = next((k for k in COND_STEMS if s.startswith(k)), None)
        if k:
            out.append(S.NAME[k])
            s = s[len(k):]
            continue
        for neg in ("na", "no"):
            k = next((k for k in COND_STEMS if s.startswith(neg + k)), None)
            if k:
                out.append(S.NNAME[k])
                s = s[len(neg + k):]
                break
        else:
            raise KeyError(s)
    return out


def head_body(b):
    if b in HEAD:
        return HEAD[b]
    if b[:1].upper() + b[1:] in HEAD:
        return HEAD[b[:1].upper() + b[1:]]
    m = re.fullmatch(r"(.*?)( ?–)(.*)", b)
    if m:
        return head_body(m.group(1)) + m.group(2) + (" " if m.group(3).startswith(" ") else "") + head_body(m.group(3).strip())
    m = re.fullmatch(r"(.+?)paccay(ā|ādi|o)", b)
    if m:
        names = cond_list(m.group(1))
        return join_and(names) + (" आदि" if m.group(2) == "ādi" else "")
    if b.endswith("ṃ") and ("duka" in b or "ttika" in b):
        parts = b[:-1].lower().split("-")
        return " और ".join(NAMES[p] for p in parts)
    raise KeyError(f"heading: {b!r}")


def heading(line):
    m = re.fullmatch(r"(#+) (\*?)((?:\d+-)*\d+\. )?(.*?)(\*?)", line)
    hashes, st, num, body, en = m.groups()
    return f"{hashes} {st}{num or ''}{head_body(body)}{en}"


# ---------------------------------------------------------------- counting

P_CNT = {}
for d in (S.P_ABL, S.P_NABL, S.P_LOC, S.P_NLOC, NUM):
    P_CNT.update(d)
PH0 = 0xE000


def is_ph(t):
    return len(t) == 1 and PH0 <= ord(t) < PH0 + 4000


CNT_SPLIT = r"(…pe…|…|, |; |\. | |\.$)"


def is_count(text):
    toks = [t for t in re.split(CNT_SPLIT, text) if t and t not in ("…pe…", "…", ", ", "; ", " ", ". ", ".")]
    return bool(toks) and any(t in P_CNT for t in toks) and all(t in P_CNT or is_ph(t) for t in toks)


def count_hi(text):
    toks = [t for t in re.split(CNT_SPLIT, text) if t]
    out = []
    for i, t in enumerate(toks):
        if t == " ":
            prev = toks[i - 1] if i else ""
            out.append(", " if (prev in S.P_ABL or prev in S.P_NABL) else " ")
        elif t == "…pe…":
            out.append("…")
        elif t == ".":
            out.append("।")
        elif t == ". ":
            out.append("। ")
        elif t in ("…", ", ", "; ") or is_ph(t):
            out.append(t)
        else:
            out.append(P_CNT[t])
    return "".join(out)


# ---------------------------------------------------------------- notes

SEC = {"sahajāta": "सह-उत्पत्ति", "paccaya": "कारण", "nissaya": "आश्रय", "saṃsaṭṭha": "घुले-मिले होने",
       "sampayutta": "जुड़ाव", "pañhā": "प्रश्नों", "paṭicca": "निर्भरता"}
VARA_RE = re.compile(r"^((?:(?:sahajāta|paccaya|nissaya|saṃsaṭṭha|sampayutta|pañhā)vār(?:epi|ampi|opi)"
                     r"(?: ?…pe… | ?… | ))+)(.*)$")
VERB = "विस्तार करना चाहिए"
VIT = r"(?:vitthāretabb(?:aṃ|o|ā))"


def vara_hi(s):
    if s.startswith("sahajātavārādi "):
        tail = s[len("sahajātavārādi "):]
        if re.fullmatch(VIT, tail):
            return f"सह-उत्पत्ति के खंड आदि का {VERB}"
        raise KeyError(s)
    m = VARA_RE.match(s + " ")
    if not m:
        return None
    lst, tail = m.group(1), m.group(2).strip()
    toks = [t for t in re.split(r"( ?…pe… | ?… | )", lst) if t]
    names, seps = [], []
    for t in toks:
        mm = re.fullmatch(r"(\w+)vār(epi|ampi|opi)", t)
        if mm:
            names.append((SEC[mm.group(1)], mm.group(2)))
        else:
            seps.append(t)
    kinds = {k for _, k in names}
    sadisa_only = tail in ("paṭiccavārasadisaṃ",)
    if "epi" in kinds:
        form = "{x} के खंड में भी"
    elif sadisa_only:
        form = "{x} का खंड भी"
    elif tail == "kātabbaṃ":
        form = "{x} के खंड को भी"
    else:
        form = "{x} के खंड का भी"
    words = [form.format(x=x) for x, _ in names]
    # rebuild the list with the Pāli separators: «…pe…» / «…» keep their spacing, a plain space joins an
    # explicit list («A, B … और Z»)
    out = words[0]
    explicit = all(sp == " " for sp in seps[:-1]) and seps and seps[-1] == " "
    for i, w in enumerate(words[1:]):
        sp = seps[i]
        if sp == " ":
            out += (" और " if i == len(words) - 2 and explicit else ", ") + w
        else:
            out += sp.replace("…pe…", "…").rstrip() + " " + w
    if re.fullmatch(r"sabbattha (\w+)", tail) and tail.split()[1] in NUM:
        return f"{out} हर जगह {NUM[tail.split()[1]]}"
    if re.fullmatch(VIT, tail):
        return f"{out} {VERB}"
    if re.fullmatch(rf"sabbattha {VIT}", tail):
        return f"{out} हर जगह {VERB}"
    if re.fullmatch(rf"paṭiccavārasadis(?:aṃ|ā) {VIT}", tail):
        return f"{out} निर्भरता के खंड के समान {VERB}"
    if sadisa_only:
        return f"{out} निर्भरता के खंड के समान हैं"
    if tail == "kātabbaṃ":
        return f"{out} तैयार करना चाहिए"
    if tail == "ekaṃ sappaccayakusalasadisaṃ":
        return f"{out} एक, {sadisa_hi('sappaccayadukakusalasadisaṃ')}"
    if tail == "sabbattha vitthāretabbaṃ lokiyadukaabyākatasadisaṃ":
        return f"{out} हर जगह {sadisa_hi('lokiyadukaabyākatasadisaṃ')} {VERB}"
    if tail == "evaṃ vitthāretabbaṃ":   # in «Yathā …, evaṃ vitthāretabbaṃ»
        return out
    raise KeyError(f"vara tail: {tail!r}")


def sadisa_hi(s):
    s = s.replace(" ", "")
    m = re.fullmatch(r"(.+?(?:duka|ttika))(kusala|akusala|abyākata)?sadisa[ṃā]", s)
    if not m or m.group(1) not in NAMES:
        return None
    name = oblique(NAMES[m.group(1)])
    return name + (f" के {PADA[m.group(2)]} पद" if m.group(2) else "") + " के समान"


def loc_item(word):
    """an item in the locative inside notes («kāmāvacare ekaṃ», «upādinnamūlake dve»)."""
    w = word
    mul = w.endswith("mūlake") or w.endswith("mūle")
    w = re.sub(r"(mūlake|mūle)$", "", w)
    base = LOCITEM.get(w)
    if base is None:
        return None
    return f"{base} पद से शुरू होने वाली शृंखला में" if mul else f"{base} पद में"


LOCITEM = {"kāmāvacare": "इंद्रिय-सुखों के लोक से संबंधित", "nakāmāvacare": "इंद्रिय-सुखों के लोक से संबंधित न होने वाले",
           "rūpāvacare": "सूक्ष्म भौतिक लोक से संबंधित", "narūpāvacare": "सूक्ष्म भौतिक लोक से संबंधित न होने वाले",
           "arūpāvacara": "अभौतिक लोक से संबंधित", "naarūpāvacare": "अभौतिक लोक से संबंधित न होने वाले",
           "naarūpe": "अभौतिक लोक से संबंधित न होने वाले",
           "upādinna": "कर्म से उत्पन्न", "anupādinna": "कर्म से उत्पन्न न होने वाले",
           "noupādāna": "आसक्ति रूपी न होने वाले", "upādānasampayutta": "आसक्ति से जुड़े",
           "upādānavippayutte": "आसक्ति से अलग",
           "dassane": "सत्य-दर्शन से छोड़े जाने वाले", "nadassane": "सत्य-दर्शन से न छोड़े जाने वाले",
           "avitakke": "आरंभिक विचार से रहित", "niyate": "निश्चित"}

SENT = {
    "saṃkhittaṃ": "संक्षिप्त",
    "yathā kusalattike pañhāvāraṃ, evaṃ vitthāretabbaṃ":
        "जैसे हितकर वाले तीन के वर्गीकरण में प्रश्नों का खंड है, वैसे ही विस्तार करना चाहिए",
    "yathā kusalattike pañhāvāraṃ evaṃ vitthāretabbaṃ":
        "जैसे हितकर वाले तीन के वर्गीकरण में प्रश्नों का खंड है, वैसे ही विस्तार करना चाहिए",
    "yathā kusalattike pañhāvārassa anulomampi paccanīyampi anulomapaccanīyampi paccanīyānulomampi gaṇitaṃ, "
    "evaṃ gaṇetabbaṃ":
        "जैसे हितकर वाले तीन के वर्गीकरण में प्रश्नों के खंड का सकारात्मक क्रम भी, नकारात्मक क्रम भी, "
        "सकारात्मक-नकारात्मक क्रम भी और नकारात्मक-सकारात्मक क्रम भी गिना गया है, वैसे ही गिनना चाहिए",
    "sabbattha vitthāretabbaṃ": f"हर जगह {VERB}",
    "kusalasadisaṃ": "हितकर पद के समान",
    "evaṃ sabbattha akusalaṃ vitthāretabbaṃ": "इसी तरह हर जगह हानिकर पद का विस्तार करना चाहिए",
    "yathā kusalanayaṃ evaṃ nahetupaccayampi kātabbaṃ":
        "जैसे हितकर पद की विधि है, वैसे ही मूल-कारण के अभाव को भी तैयार करना चाहिए",
    "nahetuyāpi kattabbaṃ": "मूल-कारण के अभाव में भी तैयार करना चाहिए",
    "sabbe kātabbā": "सभी को शामिल करना चाहिए",
    "dve pañhā": "दो प्रश्न",
    "yathā sappaccayaṃ kusalaṃ, evaṃ vitthāretabbaṃ":
        "जैसे कारणों पर निर्भर रहने वाली, हितकर परिघटना का विस्तार किया गया है, वैसे ही विस्तार करना चाहिए",
    "yathā sappaccayaṃ akusalaṃ, evaṃ kātabbaṃ":
        "जैसे कारणों पर निर्भर रहने वाली, हानिकर परिघटना के लिए किया गया है, वैसे ही करना चाहिए",
    "aññamaññanissayapaccayā sahajātapaccayasadisā":
        f"{S.NAME['aññamañña']} और {S.NAME['nissaya']} {S.SADISA['sahajāta']} हैं",
    "kusalampi akusalampi abyākatampi sappītikadukasadisaṃ":
        "हितकर पद भी, हानिकर पद भी और नैतिक रूप से अनिर्धारित पद भी उल्लास वाले दो के वर्गीकरण के समान हैं",
    "yathā cittasampayuttadukaṃ abyākatasadisaṃ":
        "जैसे मन से जुड़ी परिघटनाओं वाले दो के वर्गीकरण में, नैतिक रूप से अनिर्धारित पद के समान",
    "yathā mahantaraduke cetasikadukakusalasadisaṃ, tattakā eva pañhā":
        "जैसे बीच के बड़े दो-दो के वर्गीकरणों में मन की सहचर परिघटनाओं वाले दो के वर्गीकरण के हितकर पद के समान, "
        "उतने ही प्रश्न",
    "yathā cetasikadukamūlā tīṇi gamanā, evaṃ imepi tīṇi gamanā kātabbā":
        "जैसे मन की सहचर परिघटनाओं वाले दो के वर्गीकरण पर आधारित तीन प्रसंग हैं, वैसे ही ये तीन प्रसंग भी "
        "तैयार करने चाहिए",
    "yathā kāmāvacaradukaabyākatasadisaṃ, ettakāyeva pañhā heṭṭhuparikaṃ parivattanti":
        "जैसे इंद्रिय-सुखों के लोक वाले दो के वर्गीकरण के नैतिक रूप से अनिर्धारित पद के समान, उतने ही प्रश्न हैं, "
        "केवल नीचे वाले और ऊपर वाले आपस में बदल जाते हैं",
    "imaṃ gamanaṃ upādānadukaakusalasadisaṃ":
        "यह प्रसंग आसक्ति वाले दो के वर्गीकरण के हानिकर पद के समान है",
    "idha pana hetupaccayā idaṃ nānaṃ": "लेकिन यहाँ मूल-कारण के मामले में यह अंतर है",
    "kusalattikasadisaṃ sahajātavārampi …pe… pañhāvārampi vitthāretabbaṃ":
        f"हितकर वाले तीन के वर्गीकरण के समान सह-उत्पत्ति के खंड का भी … प्रश्नों के खंड का भी {VERB}",
    "yathā sahajātavārampi… sampayuttavārampi evaṃ vitthāretabbaṃ":
        f"जैसे सह-उत्पत्ति का खंड भी… जुड़ाव का खंड भी है, वैसे ही {VERB}",
    "yathā saṃkiliṭṭhattikahetudukaṃ, evaṃ vitthāretabbaṃ":
        "जैसे क्लेशों से मलिन परिघटनाओं वाला तीन का वर्गीकरण और मूल वाला दो का वर्गीकरण है, वैसे ही विस्तार करना चाहिए",
    "upekkhāti nānāupekkhā abyākate":
        "“समभाव” का अर्थ नैतिक रूप से अनिर्धारित पद में अलग-अलग प्रकार का समभाव है",
    "akusalaṃ dhammaṃ paṭicca…pe… paccanīye nahetuyā ekaṃ":
        f"{S.ACC['akusalaṃ']} {S.PATICCA}… नकारात्मक क्रम में {S.NLOC['hetu']} एक",
    "abyākataṃ dhammaṃ paṭicca…pe… paccanīye nahetuyā nava…pe… najhāne cha":
        f"{S.ACC['abyākataṃ']} {S.PATICCA}… नकारात्मक क्रम में {S.NLOC['hetu']} नौ… {S.NLOC['jhāna']} छह",
    "kātabbā": "इस तरह करना चाहिए",
    "paccanīye pañhāvāre kusalākusale indriye jhāne cha":
        f"नकारात्मक क्रम में, प्रश्नों के खंड में, हितकर और हानिकर में {S.LOC['indriya']} {S.LOC['jhāna']} छह",
    "pañhāvāre abyākate nava": "प्रश्नों के खंड में नैतिक रूप से अनिर्धारित में नौ",
    "pañhāvāre kusalākusale indriye jhāne cha":
        f"प्रश्नों के खंड में हितकर और हानिकर में {S.LOC['indriya']} {S.LOC['jhāna']} छह",
    "abyākate nava": "नैतिक रूप से अनिर्धारित में नौ",
    "paccanīye nahetuyā nava": f"नकारात्मक क्रम में {S.NLOC['hetu']} नौ",
    # notes inside the counts
    "majjhime ca ante ca ārammaṇādhipati": "बीच वाले में और अंतिम में विषय रूपी प्रधानता",
    "majjhe tīṇi sahajātādhipati": "बीच में तीन सह-उत्पत्ति रूपी प्रधानता",
    "ettha chasu sahajātādhipati": "यहाँ छह में सह-उत्पत्ति रूपी प्रधानता",
    "ādimhi tīṇi": "शुरुआत में तीन",
    "majjhimesu tīsu majjhimānulomikāyeva pañhā": "बीच के तीनों में बीच वालों के अनुरूप ही प्रश्न",
    "cittasamuṭṭhānamūlaṃ nocittasamuṭṭhānassa kabaḷīkāro āhāro kātabbo":
        "मन से उत्पन्न पद से शुरू होने वाली शृंखला में, मन से उत्पन्न न होने वाली परिघटना के लिए कौर-कौर खाया जाने वाला "
        "भोजन शामिल करना चाहिए",
    "nocittasamuṭṭhāno cittasamuṭṭhānassa kabaḷīkāro āhāro ghaṭane majjhe kabaḷīkāro āhāro":
        "मन से उत्पन्न न होने वाली परिघटना, मन से उत्पन्न परिघटना के लिए कौर-कौर खाया जाने वाला भोजन, संयोजन में "
        "बीच में कौर-कौर खाया जाने वाला भोजन",
    "rūpajīvitindriyaṃ ekaṃ": "भौतिक जीवन-क्षमता एक",
    "ajjhattiko bāhirassa gamanakāle sahajātādhipati":
        "आंतरिक परिघटना के बाह्य परिघटना के लिए होने के प्रसंग में सह-उत्पत्ति रूपी प्रधानता",
    "majjhe tīsupi sahajātādhipati": "बीच के तीनों में भी सह-उत्पत्ति रूपी प्रधानता",
    "ārammaṇapurejātampi vatthupurejātampi": "विषय रूपी पूर्व-उत्पत्ति भी और आधार रूपी पूर्व-उत्पत्ति भी",
    "ārammaṇapurejātaṃyeva": "केवल विषय रूपी पूर्व-उत्पत्ति",
    "ghaṭanā dve": "संयोजन दो",
    "ghaṭane ekaṃ": "संयोजन में एक",
    "tiṇṇannaṃ kabaḷīkāro āhāro": "तीनों के लिए कौर-कौर खाया जाने वाला भोजन",
    "tiṇṇannaṃ rūpajīvitindriyaṃ": "तीनों के लिए भौतिक जीवन-क्षमता",
    "paṭhame dvepi adhipatī": "पहले में दोनों प्रधानताएँ",
    "dvīsu sahajātādhipati": "दो में सह-उत्पत्ति रूपी प्रधानता",
    "dassanena pahātabbamūlakaṃ ekaṃ": "सत्य-दर्शन से छोड़े जाने वाले पद से शुरू होने वाली शृंखला में एक",
    "dassanamūlakaṃ ekaṃ": "सत्य-दर्शन से छोड़े जाने वाले पद से शुरू होने वाली शृंखला में एक",
    "ekārammaṇādhipati": "एक विषय रूपी प्रधानता",
    "heṭṭhā tīsu sahajātādhipati": "पहले के तीनों में सह-उत्पत्ति रूपी प्रधानता",
    "cattāri sahajātādhipati": "चार सह-उत्पत्ति रूपी प्रधानता",
    "kāmāvacare sahajātādhipatiyeva": "इंद्रिय-सुखों के लोक से संबंधित पद में केवल सह-उत्पत्ति रूपी प्रधानता",
    "sahajātādhipatiyeva": "केवल सह-उत्पत्ति रूपी प्रधानता",
    "dutiye ārammaṇādhipati sahajātādhipati": "दूसरे में विषय रूपी प्रधानता और सह-उत्पत्ति रूपी प्रधानता",
    "niyate sahajātādhipati": "निश्चित पद में सह-उत्पत्ति रूपी प्रधानता",
    "noupādānamūlake": "आसक्ति रूपी न होने वाले पद से शुरू होने वाली शृंखला में",
    "sahajātādhipati": "सह-उत्पत्ति रूपी प्रधानता",
    "ārammaṇādhipati": "विषय रूपी प्रधानता",
}


def sent_hi(s):
    key = S.lower_initials(s.strip())
    if key in SENT:
        return SENT[key]
    v = vara_hi(key)
    if v:
        return v
    sd = sadisa_hi(key)
    if sd:
        return sd
    m = re.fullmatch(rf"(\S+sadisaṃ) {VIT}", key)
    if m and sadisa_hi(m.group(1)):
        return f"{sadisa_hi(m.group(1))} {VERB}"
    if is_count(key):
        return count_hi(key)
    m = re.fullmatch(r"sabbattha (\w+)", key)
    if m and m.group(1) in NUM:
        return f"हर जगह {NUM[m.group(1)]}"
    if key in NUM:
        return NUM[key]
    m = re.fullmatch(r"(\w+) (\w+)", key)
    if m and m.group(2) in NUM and loc_item(m.group(1)):
        return f"{loc_item(m.group(1))} {NUM[m.group(2)]}"
    if ", " in key:
        return ", ".join(sent_hi(p) for p in key.split(", "))
    raise KeyError(f"note sentence: {s!r}")


def note_hi(content):
    """content of a (…) note -> Hindi (without the parentheses)."""
    parts = re.split(r"(?<=\.) ", content)
    out = []
    for p in parts:
        end = ""
        if p.endswith("."):
            p, end = p[:-1], "।"
        trail = ""
        if p.endswith(","):
            p, trail = p[:-1], ","
        out.append(sent_hi(p) + trail + end)
    return " ".join(out)


# ---------------------------------------------------------------- dash clauses and residual words

DASH = {
    "vicikicchānīvaraṇaṃ uddhaccanīvaraṇaṃ paṭicca avijjānīvaraṇaṃ":
        "संशय की बाधा या बेचैनी की बाधा पर निर्भर होकर अज्ञान की बाधा",
    "vicikicchāsahagate uddhaccasahagate khandhe paṭicca avijjānīvaraṇaṃ":
        "संशय के साथ होने वाले और बेचैनी के साथ होने वाले समूहों पर निर्भर होकर अज्ञान की बाधा",
    "vicikicchānīvaraṇañca uddhaccanīvaraṇañca sampayuttake ca khandhe paṭicca avijjānīvaraṇaṃ":
        "संशय की बाधा, बेचैनी की बाधा और जुड़े हुए समूहों पर निर्भर होकर अज्ञान की बाधा",
    "vicikicchaṃ paṭicca vicikicchāsahagato moho, uddhaccaṃ paṭicca uddhaccasahagato moho":
        "संशय पर निर्भर होकर संशय के साथ होने वाला मोह, बेचैनी पर निर्भर होकर बेचैनी के साथ होने वाला मोह",
    "vicikicchāsahagate uddhaccasahagate khandhe paṭicca vicikicchāsahagato uddhaccasahagato moho":
        f"{S.SUBJ_P['vicikicchāsahagate uddhaccasahagate khandhe']} {S.PATICCA} "
        f"{S.OBJ_P['vicikicchāsahagato uddhaccasahagato moho']}",
    "vicikicchāsahagate khandhe ca vicikicchañca paṭicca vicikicchāsahagato moho, uddhaccasahagate khandhe ca "
    "uddhaccañca paṭicca uddhaccasahagato moho":
        "संशय के साथ होने वाले समूहों और संशय पर निर्भर होकर संशय के साथ होने वाला मोह, बेचैनी के साथ होने वाले "
        "समूहों और बेचैनी पर निर्भर होकर बेचैनी के साथ होने वाला मोह",
    "vicikicchāsahagate khandhe paṭicca vicikicchāsahagato moho":
        "संशय के साथ होने वाले समूहों पर निर्भर होकर संशय के साथ होने वाला मोह",
    "upādinne khandhe ca mahābhūte ca paṭicca cittasamuṭṭhānaṃ rūpaṃ":
        f"कर्म से उत्पन्न समूहों और महाभूतों पर निर्भर होकर {S.RUPA_CITTA}",
    "uppannā hetū sampayuttakānaṃ hetūnaṃ hetupaccayena paccayo":
        f"उत्पन्न हो चुके मूल जुड़े हुए मूलों के लिए {S.INS('hetu', 'mp')}",
    "anuppannā hetū cetopariyañāṇassa anāgataṃsañāṇassa ārammaṇapaccayena paccayo":
        f"उत्पन्न न हुए मूल दूसरों के मन को जानने के ज्ञान और भविष्य को जानने के ज्ञान के लिए "
        f"{S.INS('ārammaṇa', 'mp')}",
    "uppādī hetū cetopariyañāṇassa anāgataṃsañāṇassa ārammaṇapaccayena paccayo":
        f"उत्पन्न होने वाले मूल दूसरों के मन को जानने के ज्ञान और भविष्य को जानने के ज्ञान के लिए "
        f"{S.INS('ārammaṇa', 'mp')}",
    "ārammaṇapurejātaṃ, vatthupurejātaṃ": "विषय रूपी पूर्व-उत्पत्ति, आधार रूपी पूर्व-उत्पत्ति",
    "ārammaṇādhipati, sahajātādhipati": "विषय रूपी प्रधानता, सह-उत्पत्ति रूपी प्रधानता",
    "ārammaṇādhipati": "विषय रूपी प्रधानता",
    "sahajātādhipati": "सह-उत्पत्ति रूपी प्रधानता",
    "paṭisandhikkhaṇe": S.PREFIX["paṭisandhikkhaṇe"],
}
DASH_KEYS = sorted(DASH, key=len, reverse=True)

CLOSE = {
    "dhammānulome dukatikapaṭṭhānaṃ niṭṭhitaṃ.":
        "परिघटनाओं का सकारात्मक क्रम: दो-दो और तीन-तीन के वर्गीकरणों के कारण-संबंध समाप्त।",
    "hetugocchakaṃ niṭṭhitaṃ.": "मूलों का वर्ग समाप्त।",
}

SLIPS = {"dhamma paṭicca": "dhammaṃ paṭicca",       # ^7-47-11 (spelling)
         "nahetudhammo": "nahetu dhammo",           # ^7-49-? (word space)
         "vitthārebbaṃ": "vitthāretabbaṃ",          # ^7-49-141 (spelling)
         "…pe. …": "…pe…"}                          # «adhipatiyā pañca…pe. … avigate» (punctuation slip)


# ---------------------------------------------------------------- line translator

def translate_line(line):
    if line.startswith("#"):
        return heading(line)
    text = S.lower_initials(line)
    for a, b in SLIPS.items():
        text = text.replace(a, b)
    text = FUSED.sub(r"\1 dhamm\2", text)
    if text in CLOSE:
        return CLOSE[text]
    m = re.fullmatch(r"(\w+?)(kusalattika|vedanāttika|hetuduka)ṃ niṭṭhitaṃ\.", text)
    if m:
        pre = m.group(1)
        pre_hi = NAMES.get(pre) or NAMES[pre + "duka"]
        return f"{pre_hi} और {NAMES[m.group(2)]} समाप्त।"
    m = re.fullmatch(r"(\w+)\.", text)
    if m and m.group(1)[:1].upper() + m.group(1)[1:] in HEAD:     # «Nahetupadaṃ.» as a closing line
        return HEAD[m.group(1)[:1].upper() + m.group(1)[1:]] + "।"
    store = []

    def keep(h):
        store.append(h)
        return chr(PH0 + len(store) - 1)

    # notes
    text = re.sub(r"\(([^()]*[^\d()][^()]*)\)", lambda mm: keep("(" + note_hi(mm.group(1)) + ")"), text)
    # counting lines
    if is_count(text):
        return finish(count_hi(text), store)
    # dash clauses and fixed words
    for k in DASH_KEYS:
        if k in text:
            text = re.sub(rf"(?<![\w]){re.escape(k)}(?![\w])", lambda mm, k=k: keep(DASH[k]), text)
    # frames
    text = PATICCA_RE.sub(lambda mm: keep(paticca_hi(mm)), text)
    text = PATICCA_BARE_RE.sub(lambda mm: keep(f"{np_hi(mm.group(1), 'acc')} {S.PATICCA}"), text)
    text = PANHA_RE.sub(lambda mm: keep(panha_hi(mm)), text)
    text = INS_CHAIN_RE.sub(lambda mm: keep(re.sub(rf"({INS_ALT})paccayena paccayo", lambda t: S.INS(t.group(1), "fs"),
                                                   mm.group(0)).replace("…pe…", "…")), text)
    # residue
    text = text.replace(" nava pañhā", ", नौ प्रश्न")
    text = text.replace("…pe…", "…")
    text = re.sub(r"\.(?= |$)", "।", text)
    text = re.sub(r"(?<![\w])(\w+)(?![\w])", lambda mm: NUM.get(mm.group(1), mm.group(1)), text)
    out = finish(text, store)
    if re.search(r"[A-Za-zāīūṃṅñṭḍṇḷ]", out):
        raise KeyError(f"untranslated: {out!r}  <=  {line!r}")
    return out


def finish(s, store):
    for _ in range(3):
        s = re.sub(rf"[{chr(PH0)}-{chr(PH0 + 3999)}]", lambda m: store[ord(m.group(0)) - PH0], s)
    return s


# ---------------------------------------------------------------- file builder

ID_RE = re.compile(r" \^([0-9A-Za-z-]+)\s*$")


def build_file(src, dst):
    lines = open(src, encoding="utf-8").read().split("\n")
    out, errors = [], []
    for ln in lines:
        if not ln.strip():
            if out and out[-1] != "":
                out.append("")
            continue
        m = ID_RE.search(ln)
        body = ln[: m.start()] if m else ln.rstrip()
        try:
            hi = translate_line(body)
        except KeyError as e:
            errors.append(f"{e}")
            hi = "@@" + body
        out.append(hi + (f" ^{m.group(1)}" if m else ""))
    while out and out[-1] == "":
        out.pop()
    with open(dst, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out) + "\n")
    return errors


if __name__ == "__main__":
    names = sys.argv[1:] or FILES
    allerr = 0
    for n in names:
        errs = build_file(os.path.join(S.PALI_DIR, n), os.path.join(S.OUT_DIR, n))
        allerr += len(errs)
        print(f"{n}: {len(errs)} errors")
        for e in errs[:15]:
            print("   ", e)
    print("total errors:", allerr)
