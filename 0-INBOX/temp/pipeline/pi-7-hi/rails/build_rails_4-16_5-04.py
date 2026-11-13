"""pi-7 Hindi plain RAILS builder for 4-16 .. 4-21 (tika-duka) and 5-01 .. 5-04 (tika-tika, duka-duka, paccanīya).
Imports the approved sample constants read-only (build_rails_sample as R).
usage: python -I -B -X utf8 build_rails_4-16_5-04.py [file ...]"""
import os
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\rails")
import build_rails_sample as R  # noqa: E402  (read-only)

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PALI_DIR = os.path.join(ROOT, "AI_translation", "pali", "pi-7_split_chapters")
OUT_DIR = os.path.join(ROOT, "AI_translation", "hindi", "pi-7-hindi-plain-rails_split_chapters")
FILES = ["4-16-tikaduka-sappaccayaduka.md", "4-17-tikaduka-asavaduka.md", "4-18-tikaduka-sarammanaduka.md",
         "4-19-tikaduka-kilesaduka.md", "4-20-tikaduka-dassanenapahatabbaduka.md", "4-21-tikaduka-sauttaraduka.md",
         "5-01-anuloma-tikatika.md", "5-02-anuloma-dukaduka.md", "5-03-paccaniya-tika.md", "5-04-paccaniya-duka.md"]

# ---------------------------------------------------------------- numbers

NUM = dict(R.NUM)
NUM.update({"dasa": "दस", "ekādasa": "ग्यारह", "terasa": "तेरह", "pannarasa": "पंद्रह", "soḷasa": "सोलह",
            "sattarasa": "सत्रह", "aṭṭhārasa": "अठारह", "ekavīsa": "इक्कीस", "tevīsa": "तेईस", "catuvīsa": "चौबीस",
            "pañcavīsa": "पच्चीस", "ekūnatiṃsa": "उनतीस", "tiṃsa": "तीस", "catuttiṃsa": "चौंतीस", "pañcatiṃsa": "पैंतीस",
            "chattiṃsa": "छत्तीस", "sattatiṃsa": "सैंतीस"})

# ---------------------------------------------------------------- items (feminine, before «परिघटना»)
# pi-1 1-matika.md wording (singular), termbase words; the comma inside pi-1 items is kept (termbase format rule only).

LEX = {
    # kusalattika
    "kusala": "हितकर", "akusala": "हानिकर", "abyākata": "नैतिक रूप से अनिर्धारित",
    # vedanāttika
    "sukhāya vedanāya sampayutta": "सुखद अनुभूति से जुड़ी",
    "dukkhāya vedanāya sampayutta": "दुःखद अनुभूति से जुड़ी",
    "adukkhamasukhāya vedanāya sampayutta": "न दुःखद, न सुखद अनुभूति से जुड़ी",
    # vipākattika
    "vipāka": "कर्म-फल रूपी", "vipākadhamma": "कर्म-फल उत्पन्न करने वाली",
    "vipākadhammadhamma": "कर्म-फल उत्पन्न करने वाली",
    "nevavipākanavipākadhamma": "न कर्म-फल रूपी, न कर्म-फल उत्पन्न करने वाली",
    "nevavipākanavipākadhammadhamma": "न कर्म-फल रूपी, न कर्म-फल उत्पन्न करने वाली",
    # upādinnattika
    "upādinnupādāniya": "कर्म से उत्पन्न और आसक्ति का विषय बनने वाली",
    "anupādinnupādāniya": "कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाली",
    "anupādinnaanupādāniya": "न कर्म से उत्पन्न, न आसक्ति का विषय बनने वाली",
    # saṃkiliṭṭhattika
    "saṃkiliṭṭhasaṃkilesika": "क्लेशों से मलिन और क्लेशों का विषय बनने वाली",
    "asaṃkiliṭṭhasaṃkilesika": "क्लेशों से मलिन न होने वाली, पर क्लेशों का विषय बनने वाली",
    "asaṃkiliṭṭhaasaṃkilesika": "क्लेशों से मलिन न होने वाली और क्लेशों का विषय न बनने वाली",
    # vitakkattika
    "savitakkasavicāra": "आरंभिक विचार और सतत विचार वाली",
    "avitakkavicāramatta": "आरंभिक विचार से रहित, केवल सतत विचार वाली",
    "avitakkaavicāra": "आरंभिक विचार और सतत विचार दोनों से रहित",
    # pītittika
    "pītisahagata": "उल्लास के साथ होने वाली", "sukhasahagata": "सुख के साथ होने वाली",
    "upekkhāsahagata": "समभाव के साथ होने वाली",
    "napītisahagata": "उल्लास के साथ न होने वाली", "nasukhasahagata": "सुख के साथ न होने वाली",
    "naupekkhāsahagata": "समभाव के साथ न होने वाली",
    # dassanattika, dassanahetuttika
    "dassanena pahātabba": "सत्य-दर्शन से छोड़ी जाने वाली",
    "bhāvanāya pahātabba": "मानसिक अभ्यास से छोड़ी जाने वाली",
    "nevadassanena nabhāvanāya pahātabba": "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़ी जाने वाली",
    "dassanena pahātabbahetuka": "सत्य-दर्शन से छोड़े जाने वाले मूलों वाली",
    "bhāvanāya pahātabbahetuka": "मानसिक अभ्यास से छोड़े जाने वाले मूलों वाली",
    "nevadassanena nabhāvanāya pahātabbahetuka": "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़े जाने वाले मूलों वाली",
    "nadassanena pahātabba": "सत्य-दर्शन से न छोड़ी जाने वाली",
    "nabhāvanāya pahātabba": "मानसिक अभ्यास से न छोड़ी जाने वाली",
    "nadassanena pahātabbahetuka": "सत्य-दर्शन से छोड़े जाने वाले मूलों से रहित",
    "nabhāvanāya pahātabbahetuka": "मानसिक अभ्यास से छोड़े जाने वाले मूलों से रहित",
    # ācayagāmittika
    "ācayagāmi": "संचय की ओर ले जाने वाली", "apacayagāmi": "संचय घटाने की ओर ले जाने वाली",
    "nevācayagāmināpacayagāmi": "न संचय की ओर, न संचय घटाने की ओर ले जाने वाली",
    # sekkhattika
    "sekkha": "सीखने के चरण की", "asekkha": "सीखना पूरा होने के चरण की",
    "nevasekkhanāsekkha": "न सीखने के चरण की, न सीखना पूरा होने के चरण की",
    # parittattika, parittārammaṇattika
    "paritta": "सीमित", "mahaggata": "उन्नत", "appamāṇa": "अपरिमित",
    "parittārammaṇa": "सीमित विषय वाली", "mahaggatārammaṇa": "उन्नत विषय वाली",
    "appamāṇārammaṇa": "अपरिमित विषय वाली",
    # hīnattika, micchattattika, maggārammaṇattika
    "hīna": "हीन", "majjhima": "मध्यम", "paṇīta": "उत्तम",
    "micchattaniyata": "ग़लत दिशा में निश्चित", "sammattaniyata": "सही दिशा में निश्चित", "aniyata": "अनिश्चित",
    "maggārammaṇa": "मार्ग को विषय बनाने वाली", "maggahetuka": "मार्ग को मूल बनाने वाली",
    "maggādhipati": "मार्ग की प्रधानता वाली",
    # uppannattika, atītattika, atītārammaṇattika
    "uppanna": "उत्पन्न हो चुकी", "anuppanna": "उत्पन्न न हुई", "uppādi": "उत्पन्न होने वाली",
    "atīta": "अतीत की", "anāgata": "भविष्य की", "paccuppanna": "वर्तमान की",
    "atītārammaṇa": "अतीत के विषय वाली", "anāgatārammaṇa": "भविष्य के विषय वाली",
    "paccuppannārammaṇa": "वर्तमान के विषय वाली",
    # ajjhattattika, ajjhattārammaṇattika
    "ajjhatta": "स्वयं से संबंधित", "bahiddhā": "दूसरों से संबंधित",
    "ajjhattārammaṇa": "स्वयं से संबंधित विषय वाली", "bahiddhārammaṇa": "दूसरों से संबंधित विषय वाली",
    # sanidassanattika
    "sanidassanasappaṭigha": "दिखाई देने वाली और टकराव वाली",
    "anidassanasappaṭigha": "दिखाई न देने वाली, पर टकराव वाली",
    "anidassanaappaṭigha": "दिखाई न देने वाली और टकराव से रहित",
    # hetugocchaka
    "hetu": "मूल रूपी", "nahetu": "मूल रूपी न होने वाली",
    "sahetuka": "मूल वाली", "ahetuka": "मूल से रहित",
    "hetusampayutta": "मूलों से जुड़ी", "hetuvippayutta": "मूलों से अलग",
    "nahetusahetuka": "मूल रूपी न होने वाली, पर मूल वाली",
    # cūḷantaraduka
    "sappaccaya": "कारणों पर निर्भर रहने वाली", "appaccaya": "कारणों पर निर्भर न रहने वाली",
    "saṅkhata": "निर्मित", "asaṅkhata": "अनिर्मित",
    "sanidassana": "दिखाई देने वाली", "anidassana": "दिखाई न देने वाली",
    "sappaṭigha": "टकराव वाली", "appaṭigha": "टकराव से रहित",
    "rūpi": "भौतिक", "arūpi": "अभौतिक", "lokiya": "लौकिक", "lokuttara": "लोकोत्तर",
    "kenaci viññeyya": "किसी एक प्रकार की चेतना से जानी जा सकने वाली",
    "nakenaci viññeyya": "किसी एक प्रकार की चेतना से न जानी जा सकने वाली",
    "kenaci naviññeyya": "किसी एक प्रकार की चेतना से न जानी जा सकने वाली",
    # āsavagocchaka
    "āsava": "मन के मैल रूपी", "sāsava": "मन के मैलों का विषय बनने वाली",
    "anāsava": "मन के मैलों का विषय न बनने वाली",
    "āsavasampayutta": "मन के मैलों से जुड़ी", "āsavavippayutta": "मन के मैलों से अलग",
    "āsavavippayutta sāsava": "मन के मैलों से अलग, पर उनका विषय बनने वाली",
    "āsavavippayutta anāsava": "मन के मैलों से अलग और उनका विषय न बनने वाली",
    # other gocchakas (pi-1)
    "saññojana": "बंधन रूपी", "saññojaniya": "बंधनों का विषय बनने वाली",
    "asaññojaniya": "बंधनों का विषय न बनने वाली",
    "saññojanasampayutta": "बंधनों से जुड़ी", "saññojanavippayutta": "बंधनों से अलग",
    "saññojanavippayutta saññojaniya": "बंधनों से अलग, पर उनका विषय बनने वाली",
    "saññojanavippayutta asaññojaniya": "बंधनों से अलग और उनका विषय न बनने वाली",
    "gantha": "गाँठ रूपी", "ganthaniya": "गाँठों का विषय बनने वाली", "aganthaniya": "गाँठों का विषय न बनने वाली",
    "ganthasampayutta": "गाँठों से जुड़ी", "ganthavippayutta": "गाँठों से अलग",
    "ganthavippayutta ganthaniya": "गाँठों से अलग, पर उनका विषय बनने वाली",
    "ganthavippayutta aganthaniya": "गाँठों से अलग और उनका विषय न बनने वाली",
    "ogha": "बाढ़ रूपी", "yoga": "जकड़न रूपी", "nīvaraṇa": "बाधा रूपी",
    "parāmāsa": "ग़लत धारणा रूपी", "parāmaṭṭha": "ग़लत धारणा का विषय बनने वाली",
    "aparāmaṭṭha": "ग़लत धारणा का विषय न बनने वाली",
    "parāmāsasampayutta": "ग़लत धारणा से जुड़ी", "parāmāsavippayutta": "ग़लत धारणा से अलग",
    "parāmāsavippayutta parāmaṭṭha": "ग़लत धारणा से अलग, पर उसका विषय बनने वाली",
    "parāmāsavippayutta aparāmaṭṭha": "ग़लत धारणा से अलग और उसका विषय न बनने वाली",
    # mahantaraduka
    "sārammaṇa": "विषय वाली", "anārammaṇa": "विषय से रहित",
    "citta": "मन रूपी", "cetasika": "मन की सहचर", "acetasika": "मन की सहचर न होने वाली",
    "cittasampayutta": "मन से जुड़ी", "cittavippayutta": "मन से अलग",
    "cittasaṃsaṭṭha": "मन से घुली-मिली", "cittavisaṃsaṭṭha": "मन से घुली-मिली न होने वाली",
    "cittasamuṭṭhāna": "मन से उत्पन्न", "cittasahabhu": "मन के साथ-साथ होने वाली",
    "cittānuparivatti": "मन का अनुसरण करने वाली",
    "nocittasahabhu": "मन के साथ-साथ न होने वाली", "nocittānuparivatti": "मन का अनुसरण न करने वाली",
    "cittasaṃsaṭṭhasamuṭṭhāna": "मन से घुली-मिली और मन से उत्पन्न",
    "cittasaṃsaṭṭhasamuṭṭhānasahabhu": "मन से घुली-मिली, मन से उत्पन्न और मन के साथ-साथ होने वाली",
    "cittasaṃsaṭṭhasamuṭṭhānānuparivatti": "मन से घुली-मिली, मन से उत्पन्न और मन का अनुसरण करने वाली",
    "nocittasaṃsaṭṭhasamuṭṭhānasahabhu": "मन से घुली-मिली, मन से उत्पन्न और मन के साथ-साथ न होने वाली",
    "nocittasaṃsaṭṭhasamuṭṭhānānuparivatti": "मन से घुली-मिली, मन से उत्पन्न और मन का अनुसरण न करने वाली",
    "ajjhattika": "आंतरिक", "bāhira": "बाह्य",
    "upādā": "व्युत्पन्न", "upādinna": "कर्म से उत्पन्न", "anupādinna": "कर्म से उत्पन्न न होने वाली",
    "upādāna": "आसक्ति रूपी",
    # kilesagocchaka
    "kilesa": "मन के क्लेश रूपी", "saṃkilesika": "क्लेशों का विषय बनने वाली",
    "asaṃkilesika": "क्लेशों का विषय न बनने वाली",
    "saṃkiliṭṭha": "क्लेशों से मलिन", "asaṃkiliṭṭha": "क्लेशों से मलिन न होने वाली",
    "kilesasampayutta": "क्लेशों से जुड़ी", "kilesavippayutta": "क्लेशों से अलग",
    "kilesavippayutta saṃkilesika": "क्लेशों से अलग, पर क्लेशों का विषय बनने वाली",
    "kilesavippayutta asaṃkilesika": "क्लेशों से अलग और क्लेशों का विषय न बनने वाली",
    # piṭṭhiduka
    "savitakka": "आरंभिक विचार वाली", "avitakka": "आरंभिक विचार से रहित",
    "savicāra": "सतत विचार वाली", "avicāra": "सतत विचार से रहित",
    "sappītika": "उल्लास वाली", "appītika": "उल्लास से रहित",
    "kāmāvacara": "इंद्रिय-सुखों के लोक से संबंधित", "rūpāvacara": "सूक्ष्म भौतिक लोक से संबंधित",
    "arūpāvacara": "अभौतिक लोक से संबंधित",
    "pariyāpanna": "अस्तित्व के लोकों में समाई हुई", "apariyāpanna": "अस्तित्व के लोकों में न समाई हुई",
    "niyyānika": "मुक्ति की ओर ले जाने वाली", "aniyyānika": "मुक्ति की ओर न ले जाने वाली",
    "niyata": "निश्चित", "sauttara": "सर्वोच्च न होने वाली", "anuttara": "सर्वोच्च",
    "saraṇa": "संघर्ष वाली", "araṇa": "संघर्ष से रहित",
}
# two-word pi-1 items (Xvippayutta + the second member), also with the paccanīya negation of the second member
MULTI = {}
for _a, _bs in [("āsavavippayutta", ["sāsava", "anāsava"]),
                ("saññojanavippayutta", ["saññojaniya", "asaññojaniya"]),
                ("ganthavippayutta", ["ganthaniya", "aganthaniya"]),
                ("parāmāsavippayutta", ["parāmaṭṭha", "aparāmaṭṭha"]),
                ("kilesavippayutta", ["saṃkilesika", "asaṃkilesika"])]:
    for _b in _bs:
        MULTI[(_a, _b)] = _a + " " + _b
        MULTI[(_a, "na" + _b)] = "na:" + _a + " " + _b     # paccanīya: the whole item negated
INVARIANT_PREFIX = {"sukhāya", "dukkhāya", "adukkhamasukhāya", "nasukhāya", "nadukkhāya", "naadukkhamasukhāya",
                    "vedanāya", "dassanena", "nadassanena", "nanadassanena", "bhāvanāya", "nabhāvanāya",
                    "nanabhāvanāya", "nevadassanena", "nanevadassanena", "kenaci", "nakenaci", "nanakenaci"}
INVARIANT_ITEM = {"upādā", "noupādā", "naupādā", "nanoupādā", "bahiddhā", "nabahiddhā"}
NEG = " न होने वाली"


def hi_item(lem):
    if lem.startswith("na:"):
        return hi_item(lem[3:]) + NEG
    if lem in LEX:
        return LEX[lem]
    for p in ("nano", "na", "no"):
        if lem.startswith(p) and len(lem) > len(p) + 2:
            rest = lem[len(p):]
            try:
                base = hi_item(rest)
            except KeyError:
                continue
            return base + NEG + (NEG if p == "nano" else "")
    raise KeyError(f"item: {lem!r}")


ENDINGS = [("añceva", "a", "ceva"), ("iñceva", "i", "ceva"), ("uñceva", "u", "ceva"),
           ("añca", "a", "ca"), ("iñca", "i", "ca"), ("uñca", "u", "ca"),
           ("assa", "a", ""), ("issa", "i", ""), ("ussa", "u", ""),
           ("aṃ", "a", ""), ("iṃ", "i", ""), ("uṃ", "u", ""), ("o", "a", ""), ("ī", "i", ""), ("ū", "u", "")]


def norm(tok):
    """surface form -> (lemma, clitic)"""
    if tok in INVARIANT_ITEM:
        return tok, ""
    for suf, rep, cl in ENDINGS:
        if tok.endswith(suf) and len(tok) > len(suf) + 1:
            return tok[: -len(suf)] + rep, cl
    return tok, ""


class Atom:
    def __init__(self, lem, neg=""):
        self.lem, self.neg, self.ceva, self.ca = lem, neg, False, False


TOKEN_SLIPS = {"nanoasaññojano": "nanosaññojano"}  # ^7-58-37: spelling slip, rendered as meant


def atoms_of(phrase):
    toks = [TOKEN_SLIPS.get(t, t) for t in phrase.split()]
    atoms = []
    prefix = []
    i = 0
    while i < len(toks):
        t = toks[i]
        nxt = toks[i + 1] if i + 1 < len(toks) else None
        if t in ("no", "na", "nano") and nxt == "ca":
            lem, cl = norm(toks[i + 2])
            a = Atom(lem, neg=t)
            a.ca = cl == "ca"
            atoms.append(a)
            i += 3
            continue
        if t in ("no", "na") and nxt not in (None, "ca"):
            toks[i + 1] = t + nxt
            i += 1
            continue
        if t == "ca":
            atoms[-1].ca = True
        elif t == "ceva":
            atoms[-1].ceva = True
        elif t in INVARIANT_PREFIX:
            prefix.append(t)
        else:
            lem, cl = norm(t)
            if prefix:
                lem = " ".join(prefix) + " " + lem
                prefix = []
            a = Atom(lem)
            if cl == "ca":
                a.ca = True
            elif cl == "ceva":
                a.ceva = True
            atoms.append(a)
        i += 1
    if prefix:
        raise KeyError(f"dangling prefix in {phrase!r}")
    # merge two-word items
    out = []
    for a in atoms:
        if out and (out[-1].lem, a.lem) in MULTI and not out[-1].ca and not out[-1].ceva and not a.neg:
            out[-1].lem = MULTI[(out[-1].lem, a.lem)]
            out[-1].ca, out[-1].ceva = a.ca, a.ceva
        else:
            out.append(a)
    return out


class Unit:
    def __init__(self, hi, comp=False, outer=False):
        self.hi, self.comp, self.outer = hi, comp, outer


def units_of(phrase):
    atoms = atoms_of(phrase)
    units = []
    i = 0
    while i < len(atoms):
        a = atoms[i]
        if a.ceva:
            b = atoms[i + 1]
            if b.neg:
                hi = f"{hi_item(a.lem)}, पर स्वयं {hi_item(b.neg + b.lem)}"
                units.append(Unit(hi, True, b.ca))
            else:
                units.append(Unit(f"{hi_item(a.lem)} भी और {hi_item(b.lem)} भी", True, False))
            i += 2
        else:
            if a.neg:
                raise KeyError(f"neg without ceva in {phrase!r}")
            units.append(Unit(hi_item(a.lem), False, a.ca))
            i += 1
    groups, cur = [], []
    for u in units:
        cur.append(u)
        if u.outer:
            groups.append(cur)
            cur = []
    if cur:
        groups.append(cur)
    out = []
    for g in groups:
        if len(g) >= 2 and all(u.comp for u in g):
            out.extend([[u] for u in g])
        else:
            out.append(g)
    return [", ".join(u.hi for u in g) for g in out], out


N = "परिघटना"


def join_list(xs):
    return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " और " + xs[-1]


def acc(phrase):
    gs, _ = units_of(phrase)
    return join_list([f"{g} {N}" for g in gs])


def dat(phrase):
    return acc(phrase) + " के लिए"


def nom(phrase, plural):
    gs, groups = units_of(phrase)
    if not plural:
        if len(gs) != 1:
            raise KeyError(f"singular with {len(gs)} members: {phrase!r}")
        return f"{gs[0]} {N}", "s"
    simple = all(len(g) == 1 and not g[0].comp for g in groups) and not any(("," in g or " और " in g) for g in gs)
    if simple:
        return join_list(gs) + " परिघटनाएँ", "p"
    return join_list([f"{g} {N}" for g in gs]), "p"


# ---------------------------------------------------------------- sentence pieces

def lower_initials(s):
    return R.lower_initials(s)


SLIPS = {"āmammaṇe": "ārammaṇe"}
CHAIN_FULL = re.compile(rf"^{R.CHAIN_RE}$")


def count_hi(text):
    toks = [t for t in re.split(r"(…pe…|…|, |; | )", text) if t]
    out = []
    for i, t in enumerate(toks):
        if t == " ":
            prev = toks[i - 1]
            out.append(", " if prev in R.P_ABL or prev in R.P_NABL else " ")
        elif t == "…pe…":
            out.append("…")
        elif t in ("…", ", ", "; "):
            out.append(t)
        else:
            t = SLIPS.get(t, t)
            for d in (R.P_ABL, R.P_NABL, R.P_LOC, R.P_NLOC, NUM):
                if t in d:
                    out.append(d[t])
                    break
            else:
                raise KeyError(t)
    return "".join(out)


def is_count(text):
    toks = [t for t in re.split(r"(…pe…|…|, |; | )", text) if t and t not in ("…pe…", "…", ", ", "; ", " ")]
    words = set(R.P_ABL) | set(R.P_NABL) | set(R.P_LOC) | set(R.P_NLOC) | set(NUM) | set(SLIPS)
    return bool(toks) and all(t in words for t in toks) and any(t in NUM for t in toks)


ARISES = {"s": "उत्पन्न होती है", "p": "उत्पन्न होती हैं"}
NOUN = r"(?:dhammaṃ|dhammo|dhammā|dhammassa)"
RE_PATICCA = re.compile(r"^(?P<acc>.+?) ?dhammaṃ paṭicca (?P<nom>.+?) ?(?P<v>dhammo uppajjati|dhammā uppajjanti)"
                        r"(?: (?P<chain>.+))?$")
RE_PATICCA_ONLY = re.compile(r"^(?P<acc>.+?) ?dhammaṃ paṭicca$")
RE_ACC_ONLY = re.compile(r"^(?P<acc>.+?) ?dhammaṃ$")
RE_PANHA = re.compile(r"^(?P<nom>.+?) ?(?P<n>dhammo|dhammā) (?P<dat>.+?) ?dhammassa (?P<k>\w+?)paccayena paccayo$")
RE_INS = re.compile(r"^(?P<k>\w+?)paccayena paccayo$")

STATE = {"g": "fs"}


def frame_chain(chain):
    """'hetupaccayā' or 'hetupaccayā ekaṃ' -> (ablative chain Hindi, trailing count Hindi or '')"""
    m = re.fullmatch(r"(.+?) (\w+)", chain)
    if CHAIN_FULL.match(chain):
        return R.CH(chain), ""
    if m and m.group(2) in NUM and CHAIN_FULL.match(m.group(1)):
        return R.CH(m.group(1)), NUM[m.group(2)]
    raise KeyError(f"chain: {chain!r}")


def segment(seg):
    s = seg.strip()
    if not s:
        return seg
    lead = seg[: len(seg) - len(seg.lstrip())]
    trail = seg[len(seg.rstrip()):]
    return lead + segment_core(s) + trail


def strict(rx):
    """the same regex with the noun as a separate word (tried first; fused …dhammadhammo is the fallback)"""
    return re.compile(rx.pattern.replace(" ?", " "))


RE_PATICCA_S, RE_PANHA_S = strict(RE_PATICCA), strict(RE_PANHA)


def segment_core(s):
    if s in SEG_HAND:
        return SEG_HAND[s]
    for rx in (RE_PATICCA_S, RE_PANHA_S):
        m = rx.match(s)
        if m:
            try:
                return segment_frame(s, rx, m)
            except KeyError:
                pass
    m = RE_PATICCA.match(s)
    if m:
        return segment_frame(s, RE_PATICCA, m)
    return segment_rest(s)


def segment_frame(s, rx, m):
    if "paṭicca" in rx.pattern:
        y, n = nom(m.group("nom"), m.group("v").startswith("dhammā"))
        h = f"{acc(m.group('acc'))} {R.PATICCA} {y}"
        tail = ""
        if m.group("chain"):
            ch, tail = frame_chain(m.group("chain"))
            h += " " + ch
        h += " " + ARISES[n]
        return h + (", " + tail if tail else "")
    y, n = nom(m.group("nom"), m.group("n") == "dhammā")
    STATE["g"] = "fp" if n == "p" else "fs"
    return f"{y}, {dat(m.group('dat'))} {R.INS(m.group('k'), STATE['g'])}"


def segment_rest(s):
    m = RE_PATICCA_ONLY.match(s)
    if m:
        return f"{acc(m.group('acc'))} {R.PATICCA}"
    m = RE_PANHA.match(s)
    if m:
        return segment_frame(s, RE_PANHA, m)
    m = RE_INS.match(s)
    if m:
        return R.INS(m.group("k"), STATE["g"])
    m = RE_ACC_ONLY.match(s)
    if m:
        return acc(m.group("acc"))
    if CHAIN_FULL.match(s):
        return R.CH(s)
    if s in NUM:
        return NUM[s]
    if is_count(s):
        return count_hi(s)
    if s in CLOSING:
        return CLOSING[s]
    raise KeyError(f"segment: {s!r}")


SEP_RE = re.compile(r"( …pe… |…pe… | …pe…|…pe…| … |… | …|…)")


def sentence(core):
    """a sentence without its final '.', possibly with ellipses"""
    core = lower_initials(core)
    if core in SENT_HAND:
        return SENT_HAND[core]
    STATE["g"] = "fs"
    out = []
    for part in SEP_RE.split(core):
        if SEP_RE.fullmatch(part):
            out.append(part.replace("…pe…", "…"))
        else:
            out.append(segment(part))
    return "".join(out)


def text_chunk(chunk):
    """text outside parentheses: one or more sentences, '.' -> '।'"""
    out = []
    for part in re.split(r"(\.(?= |$))", chunk):
        if part == ".":
            out.append("।")
        elif part.strip():
            lead = part[: len(part) - len(part.lstrip())]
            trail = part[len(part.rstrip()):]
            out.append(lead + sentence(part.strip()) + trail)
        else:
            out.append(part)
    return "".join(out)


# ---------------------------------------------------------------- notes

VARA = {"sahajāta": "सह-उत्पत्ति", "paccaya": "कारण", "nissaya": "आश्रय", "saṃsaṭṭha": "घुले-मिले होने",
        "sampayutta": "जुड़ाव", "pañhā": "प्रश्नों", "paṭicca": "निर्भरता"}
VSEP = r"(…pe… | …pe… | )"


def vara_list(text, suffix):
    """'sahajātavārampi…pe… sampayuttavārampi' -> parts; suffix 'vārampi' or 'vārepi'"""
    parts = re.split(VSEP, text)
    names, seps = [], []
    for p in parts:
        if re.fullmatch(VSEP, p):
            seps.append(p)
        else:
            m = re.fullmatch(rf"(\w+?){suffix}", p)
            if not m or m.group(1) not in VARA:
                raise KeyError(f"vāra: {p!r}")
            names.append(VARA[m.group(1)])
    return names, seps


def vara_join(names, seps, form):
    """form: 'nom' «X का खंड भी», 'gen' «X के खंड का भी», 'loc' «X के खंड में भी»"""
    word = {"nom": "{} का खंड भी", "gen": "{} के खंड का भी", "loc": "{} के खंड में भी"}[form]
    items = [word.format(n) for n in names]
    out = items[0]
    space_idx = [i for i, s in enumerate(seps) if s == " "]
    for i, s in enumerate(seps):
        if s == " ":
            out += (" और " if i == space_idx[-1] and i == len(seps) - 1 else ", ") + items[i + 1]
        else:
            out += s.replace("…pe…", "…") + items[i + 1]
    return out


SIMILAR = {  # Xsadisaṃ in notes
    "paṭiccavārasadisaṃ": "निर्भरता के खंड के समान",
    "sappaccayadukasadisaṃ": "कारणों पर निर्भर रहने वाली परिघटनाओं वाले दो के वर्गीकरण के समान",
    "kenaciviññeyyasadisaṃ": "किसी एक प्रकार की चेतना से जानी जा सकने वाली परिघटनाओं वाले दो के वर्गीकरण के समान",
    "saṃkiliṭṭhadukasadisaṃ": "क्लेशों से मलिन परिघटनाओं वाले दो के वर्गीकरण के समान",
    "kusalasavitakkasadisaṃ": "हितकर वाले तीन के वर्गीकरण और आरंभिक विचार वाले दो के वर्गीकरण के समान",
    "rūpāvacaradukasadisaṃ": "सूक्ष्म भौतिक लोक वाले दो के वर्गीकरण के समान",
    "āsavagocchakasadisaṃ": "मन के मैलों के वर्ग के समान",
}
NOTE_SENT = {
    "saṃkhittaṃ": "संक्षिप्त",
    "sabbattha vitthāro": "हर जगह विस्तार",
    "sabbattha vitthāretabbaṃ": "हर जगह विस्तार करना चाहिए",
    "vipākaṃ natthi": f"{R.NAME['vipāka']} नहीं है",
    "yāva mahābhūtā": "महाभूतों तक",
    "upādānagocchakaṃ vitthāretabbaṃ": "आसक्ति के वर्ग का विस्तार करना चाहिए",
    "sabbattha gocchakaṃ vitthāretabbaṃ": "हर जगह वर्ग का विस्तार करना चाहिए",
    "yathā kusalattike pañhāvāraṃ, evaṃ vitthāretabbaṃ":
        "जैसे हितकर वाले तीन के वर्गीकरण में प्रश्नों का खंड है, वैसे ही विस्तार करना चाहिए",
    "yathā kusalattike pañhāvāraṃ evaṃ vitthāretabbaṃ":
        "जैसे हितकर वाले तीन के वर्गीकरण में प्रश्नों का खंड है, वैसे ही विस्तार करना चाहिए",
    "pañhāvārampi evaṃ vitthāretabbaṃ": "प्रश्नों के खंड का भी इसी तरह विस्तार करना चाहिए",
    "yathā kusalattike pañhāvārassa anulomampi paccanīyampi anulomapaccanīyampi paccanīyānulomampi gaṇitaṃ "
    "evaṃ gaṇetabbaṃ":
        "जैसे हितकर वाले तीन के वर्गीकरण में प्रश्नों के खंड का सकारात्मक क्रम भी, नकारात्मक क्रम भी, "
        "सकारात्मक-नकारात्मक क्रम भी और नकारात्मक-सकारात्मक क्रम भी गिना गया है, वैसे ही गिनना चाहिए",
    "yathā kusalattike sahajātavārampi paccayavārampi nissayavārampi saṃsaṭṭhavārampi sampayuttavārampi "
    "pañhāvārampi gaṇitaṃ evaṃ gaṇetabbaṃ":
        "जैसे हितकर वाले तीन के वर्गीकरण में सह-उत्पत्ति का खंड भी, कारण का खंड भी, आश्रय का खंड भी, "
        "घुले-मिले होने का खंड भी, जुड़ाव का खंड भी और प्रश्नों का खंड भी गिना गया है, वैसे ही गिनना चाहिए",
    "oghagocchakayogagocchakesu āmasanaṃ āsavagocchake āmasanasadisaṃ":
        "बाढ़ों के वर्ग और जकड़नों के वर्ग में उल्लेख मन के मैलों के वर्ग के उल्लेख के समान है",
    "nīvaraṇagocchake āmasanaṃ saññojanagocchake āmasanasadisaṃ":
        "बाधाओं के वर्ग में उल्लेख बंधनों के वर्ग के उल्लेख के समान है",
    "paccanīyadukamattāni na vattabbaṃ dhammaṃ pūretuṃ nava nava pañhāni karotu":
        "केवल नकारात्मक क्रम के दो-दो के वर्गीकरणों में “कहने योग्य नहीं” परिघटना को पूरा करने के लिए "
        "नौ-नौ प्रश्न बनाएँ",
}


def note_sentence(s):
    s = lower_initials(s.strip())
    if s in NOTE_SENT:
        return NOTE_SENT[s]
    if s in SIMILAR:
        return SIMILAR[s]
    m = re.fullmatch(r"sabbattha (\w+)", s)
    if m and m.group(1) in NUM:
        return f"हर जगह {NUM[m.group(1)]}"
    if s in NUM:
        return NUM[s]
    m = re.fullmatch(r"(.+?vārampi)( paṭiccavārasadisaṃ| paṭiccavārasadisaṃ,? evaṃ vitthāretabbaṃ|"
                     r" paṭiccavārasadisaṃ vitthāretabbaṃ| vitthāretabbaṃ| evaṃ vitthāretabbaṃ|"
                     r" sabbattha vitthāretabbaṃ| sabbattha vitthāro)", s)
    if m:
        names, seps = vara_list(m.group(1), "vārampi")
        tail = m.group(2).strip()
        if tail == "paṭiccavārasadisaṃ":
            return vara_join(names, seps, "nom") + " निर्भरता के खंड के समान है"
        if re.fullmatch(r"paṭiccavārasadisaṃ,? evaṃ vitthāretabbaṃ", tail):
            return vara_join(names, seps, "nom") + " निर्भरता के खंड के समान है, इसी तरह विस्तार करना चाहिए"
        if tail == "paṭiccavārasadisaṃ vitthāretabbaṃ":
            return vara_join(names, seps, "gen") + " निर्भरता के खंड के समान विस्तार करना चाहिए"
        if tail == "vitthāretabbaṃ":
            return vara_join(names, seps, "gen") + " विस्तार करना चाहिए"
        if tail == "evaṃ vitthāretabbaṃ":
            return vara_join(names, seps, "gen") + " इसी तरह विस्तार करना चाहिए"
        if tail == "sabbattha vitthāretabbaṃ":
            return vara_join(names, seps, "gen") + " हर जगह विस्तार करना चाहिए"
        if tail == "sabbattha vitthāro":
            return vara_join(names, seps, "gen") + " हर जगह विस्तार"
    m = re.fullmatch(r"(.+?vārepi) (sabbattha ekaṃ|sabbattha vitthāro|sabbattha vitthāretabbaṃ|vitthāretabbaṃ|"
                     r"tattakāva pañhā)", s)
    if m:
        names, seps = vara_list(m.group(1), "vārepi")
        tail = {"sabbattha ekaṃ": "हर जगह एक", "sabbattha vitthāro": "हर जगह विस्तार",
                "sabbattha vitthāretabbaṃ": "हर जगह विस्तार करना चाहिए", "vitthāretabbaṃ": "विस्तार करना चाहिए",
                "tattakāva pañhā": "उतने ही प्रश्न हैं"}[m.group(2)]
        return vara_join(names, seps, "loc") + " " + tail
    raise KeyError(f"note: {s!r}")


def note_hi(inner):
    """inside of (...) -> Hindi inside"""
    if re.fullmatch(r"\d+", inner):
        return inner
    out = []
    # sentences end with '.'; ', ' before a new clause (sabbattha / sahajāta / saṃkhittaṃ) is kept
    for part in re.split(r"(\. |\.$|, (?=[sS]abbattha|[sS]ahajāta|[sS]aṃkhittaṃ|vipākaṃ)|…pe… (?=sahajāta))", inner):
        if part in (". ", "."):
            out.append(part.replace(".", "।"))
        elif part.startswith(", ") or part.startswith("…pe… "):
            out.append(part.replace("…pe…", "…"))
        elif part:
            out.append(note_sentence(part))
    return "".join(out)


# ---------------------------------------------------------------- headings, closings

TIKA = {
    "kusala": "हितकर वाला तीन का वर्गीकरण", "vedanā": "अनुभूति वाला तीन का वर्गीकरण",
    "vipāka": "कर्म-फल वाला तीन का वर्गीकरण",
    "upādinna": "कर्म से उत्पन्न परिघटनाओं वाला तीन का वर्गीकरण",
    "saṃkiliṭṭha": "क्लेशों से मलिन परिघटनाओं वाला तीन का वर्गीकरण",
    "vitakka": "आरंभिक विचार वाला तीन का वर्गीकरण", "pīti": "उल्लास वाला तीन का वर्गीकरण",
    "dassana": "सत्य-दर्शन से छोड़ी जाने वाली परिघटनाओं वाला तीन का वर्गीकरण",
    "dassanahetu": "सत्य-दर्शन से छोड़े जाने वाले मूलों वाला तीन का वर्गीकरण",
    "dassanahetuka": "सत्य-दर्शन से छोड़े जाने वाले मूलों वाला तीन का वर्गीकरण",
    "ācayagāmi": "संचय की ओर ले जाने वाला तीन का वर्गीकरण", "sekkha": "सीखने के चरण वाला तीन का वर्गीकरण",
    "paritta": "सीमित वाला तीन का वर्गीकरण", "parittārammaṇa": "सीमित विषय वाला तीन का वर्गीकरण",
    "hīna": "हीन वाला तीन का वर्गीकरण",
    "micchattaniyata": "ग़लत दिशा में निश्चित परिघटनाओं वाला तीन का वर्गीकरण",
    "micchatta": "ग़लत दिशा में निश्चित परिघटनाओं वाला तीन का वर्गीकरण",
    "maggārammaṇa": "मार्ग को विषय बनाने वाला तीन का वर्गीकरण", "uppanna": "उत्पन्न वाला तीन का वर्गीकरण",
    "atīta": "अतीत वाला तीन का वर्गीकरण", "atītārammaṇa": "अतीत के विषय वाला तीन का वर्गीकरण",
    "ajjhatta": "स्वयं से संबंधित परिघटनाओं वाला तीन का वर्गीकरण",
    "ajjhattārammaṇa": "स्वयं से संबंधित विषय वाला तीन का वर्गीकरण",
    "sanidassana": "दिखाई देने वाला और टकराव वाला तीन का वर्गीकरण",
}
_D = "वाला दो का वर्गीकरण"
DUKA = {
    "hetu": f"मूल {_D}", "sahetuka": f"मूल वाली परिघटनाओं {_D}", "hetusampayutta": f"मूलों से जुड़ी परिघटनाओं {_D}",
    "hetusahetuka": f"मूल रूपी भी और मूल वाली भी परिघटनाओं {_D}",
    "hetuhetusampayutta": f"मूल रूपी भी और मूलों से जुड़ी भी परिघटनाओं {_D}",
    "nahetusahetuka": f"मूल रूपी न होने वाली, पर मूल वाली परिघटनाओं {_D}",
    "sappaccaya": f"कारणों पर निर्भर रहने वाली परिघटनाओं {_D}", "saṅkhata": f"निर्मित परिघटनाओं {_D}",
    "sanidassana": f"दिखाई देने वाली परिघटनाओं {_D}", "sappaṭigha": f"टकराव वाली परिघटनाओं {_D}",
    "rūpī": f"भौतिक परिघटनाओं {_D}", "lokiya": f"लौकिक परिघटनाओं {_D}",
    "kenaciviññeyya": f"किसी एक प्रकार की चेतना से जानी जा सकने वाली परिघटनाओं {_D}",
    "āsava": f"मन के मैल {_D}", "sāsava": f"मन के मैलों के विषय {_D}", "āsavasampayutta": f"मन के मैलों से जुड़ाव {_D}",
    "āsavasāsava": f"मन के मैल और मन के मैलों के विषय {_D}",
    "āsavaāsavasampayutta": f"मन के मैल और मन के मैलों से जुड़ाव {_D}",
    "āsavavippayuttasāsava": f"मन के मैलों से अलगाव और मन के मैलों के विषय {_D}",
    "saññojana": f"बंधन {_D}", "saññojaniya": f"बंधनों के विषय {_D}", "saññojanasampayutta": f"बंधनों से जुड़ाव {_D}",
    "saññojanasaññojaniya": f"बंधन और बंधनों के विषय {_D}",
    "saññojanasaññojanasampayutta": f"बंधन और बंधनों से जुड़ाव {_D}",
    "saññojanavippayuttasaññojaniya": f"बंधनों से अलगाव और बंधनों के विषय {_D}",
    "gantha": f"गाँठ {_D}", "ganthaniya": f"गाँठों के विषय {_D}", "ganthasampayutta": f"गाँठों से जुड़ाव {_D}",
    "ganthaganthaniya": f"गाँठ और गाँठों के विषय {_D}", "ganthaganthasampayutta": f"गाँठ और गाँठों से जुड़ाव {_D}",
    "ganthavippayuttaganthaniya": f"गाँठों से अलगाव और गाँठों के विषय {_D}",
    "sārammaṇa": f"विषय वाली परिघटनाओं {_D}", "citta": f"मन रूपी परिघटनाओं {_D}",
    "cetasika": f"मन की सहचर परिघटनाओं {_D}", "cittasampayutta": f"मन से जुड़ी परिघटनाओं {_D}",
    "cittasaṃsaṭṭha": f"मन से घुली-मिली परिघटनाओं {_D}", "cittasamuṭṭhāna": f"मन से उत्पन्न परिघटनाओं {_D}",
    "cittasahabhū": f"मन के साथ-साथ होने वाली परिघटनाओं {_D}",
    "cittānuparivatti": f"मन का अनुसरण करने वाली परिघटनाओं {_D}",
    "cittasaṃsaṭṭhasamuṭṭhāna": f"मन से घुली-मिली और मन से उत्पन्न परिघटनाओं {_D}",
    "cittasaṃsaṭṭhasamuṭṭhānasahabhū": f"मन से घुली-मिली, मन से उत्पन्न और मन के साथ-साथ होने वाली परिघटनाओं {_D}",
    "cittasaṃsaṭṭhasamuṭṭhānānuparivatti": f"मन से घुली-मिली, मन से उत्पन्न और मन का अनुसरण करने वाली परिघटनाओं {_D}",
    "ajjhattika": f"आंतरिक परिघटनाओं {_D}", "upādā": f"व्युत्पन्न परिघटनाओं {_D}",
    "upādinna": f"कर्म से उत्पन्न परिघटनाओं {_D}",
    "kilesa": f"मन के क्लेश {_D}", "saṃkilesika": f"क्लेशों का विषय बनने {_D}",
    "saṃkiliṭṭha": f"क्लेशों से मलिन परिघटनाओं {_D}", "kilesasampayutta": f"क्लेशों से जुड़ाव {_D}",
    "kilesasaṃkilesika": f"मन के क्लेश और क्लेशों का विषय बनने {_D}",
    "kilesasaṃkiliṭṭha": f"मन के क्लेश और क्लेशों से मलिन परिघटनाओं {_D}",
    "kilesakilesasampayutta": f"मन के क्लेश और क्लेशों से जुड़ाव {_D}",
    "kilesavippayuttasaṃkilesika": f"क्लेशों से अलगाव और क्लेशों का विषय बनने {_D}",
    "dassanenapahātabba": f"सत्य-दर्शन से छोड़े जाने {_D}", "bhāvanāyapahātabba": f"मानसिक अभ्यास से छोड़े जाने {_D}",
    "dassanenapahātabbahetuka": f"सत्य-दर्शन से छोड़े जाने वाले मूलों {_D}",
    "bhāvanāyapahātabbahetuka": f"मानसिक अभ्यास से छोड़े जाने वाले मूलों {_D}",
    "savitakka": f"आरंभिक विचार {_D}", "savicāra": f"सतत विचार {_D}", "sappītika": f"उल्लास {_D}",
    "pītisahagata": f"उल्लास के साथ होने {_D}", "sukhasahagata": f"सुख के साथ होने {_D}",
    "upekkhāsahagata": f"समभाव के साथ होने {_D}",
    "kāmāvacara": f"इंद्रिय-सुखों के लोक {_D}", "rūpāvacara": f"सूक्ष्म भौतिक लोक {_D}",
    "arūpāvacara": f"अभौतिक लोक {_D}",
    "pariyāpanna": f"अस्तित्व के लोकों में समाए होने {_D}", "niyyānika": f"मुक्ति की ओर ले जाने {_D}",
    "niyata": f"निश्चित {_D}", "sauttara": f"सर्वोच्च न होने {_D}", "saraṇa": f"संघर्ष {_D}",
    "cūḷantara": "बीच के छोटे दो-दो के वर्गीकरण", "mahantara": "बीच के बड़े दो-दो के वर्गीकरण",
    "piṭṭhi": "अंतिम दो-दो के वर्गीकरण",
}
GOC = {"hetu": "मूलों का वर्ग", "āsava": "मन के मैलों का वर्ग", "saññojana": "बंधनों का वर्ग",
       "gantha": "गाँठों का वर्ग", "nīvaraṇa": "बाधाओं का वर्ग", "parāmāsa": "ग़लत धारणा का वर्ग",
       "upādāna": "आसक्ति का वर्ग", "kilesa": "मन के क्लेशों का वर्ग"}
_A = "आदि वाले दो-दो के वर्गीकरण"
ADI = {"saññojana": f"बंधन {_A}", "cittasampayutta": f"मन से जुड़ी परिघटनाओं {_A}", "upādāna": f"आसक्ति {_A}",
       "pītisahagata": f"उल्लास के साथ होने {_A}", "ogha": f"बाढ़ {_A}", "parāmāsa": f"ग़लत धारणा {_A}"}


def name_part(p):
    p = p[0].lower() + p[1:]
    for suf, d in (("ādidukāni", ADI), ("ādiduka", ADI), ("gocchakaṃ", GOC), ("gocchaka", GOC),
                   ("ttikaṃ", TIKA), ("ttika", TIKA), ("dukaṃ", DUKA), ("duka", DUKA)):
        if p.endswith(suf):
            stem = p[: -len(suf)]
            if stem in d:
                return d[stem]
            if suf.startswith("ā") and stem + "a" in d:
                return d[stem + "a"]
    raise KeyError(f"name: {p!r}")


def name(s):
    return " और ".join(name_part(p) for p in s.split("-"))


PADA = {
    "Lokuttarapadaṃ": "लोकोत्तर पद", "Anāsavapadaṃ": "मन के मैलों का विषय न बनने वाला पद",
    "Avitakkapadaṃ": "आरंभिक विचार से रहित पद", "Appītikapadaṃ": "उल्लास से रहित पद",
    "Nakāmāvacarapadaṃ": "इंद्रिय-सुखों के लोक से संबंधित न होने वाला पद",
    "Apariyāpannapadaṃ": "अस्तित्व के लोकों में न समाया हुआ पद", "Anuttarapadaṃ": "सर्वोच्च पद",
    "Araṇapadaṃ": "संघर्ष से रहित पद", "Sukhāyavedanāyasampayuttapadaṃ": "सुखद अनुभूति से जुड़ा पद",
    "Dukkhāyavedanāyasampayuttapadaṃ": "दुःखद अनुभूति से जुड़ा पद",
    "Adukkhamasukhavedanāyasampayuttapadaṃ": "न दुःखद, न सुखद अनुभूति से जुड़ा पद",
    "Mahaggatādipadāni": "उन्नत आदि पद", "Paṇītapadaṃ": "उत्तम पद",
    "Anāgatārammaṇapadaṃ": "भविष्य के विषय वाला पद", "Paccuppannārammaṇapadaṃ": "वर्तमान के विषय वाला पद",
    "Bahiddhāpadaṃ": "दूसरों से संबंधित पद", "Sahetukapadaṃ": "मूल वाला पद", "Ahetukapadaṃ": "मूल से रहित पद",
}
HEAD = dict(R.HEAD)
HEAD.update(PADA)
HEAD.update({
    "Paccayacatukkaṃ": "कारणों के चार क्रम", "Paccanīyaṃ": "नकारात्मक क्रम",
    "Paccanīyaṃ –nahetupaccayo": "नकारात्मक क्रम –" + R.NNAME["hetu"],
    "Paṭiccavārādi": "निर्भरता का खंड आदि",
    "Hetu-ārammaṇapaccayā": f"{R.NAME['hetu']} और {R.NAME['ārammaṇa']}",
    "Hetuārammaṇapaccayādi": f"{R.NAME['hetu']} और {R.NAME['ārammaṇa']} आदि",
    "Hetusahajātapaccayādi": f"{R.NAME['hetu']} और {R.NAME['sahajāta']} आदि",
    "(Pañcamo bhāgo)": "(पाँचवाँ भाग)",
    "Hetudukaṃ": DUKA["hetu"],  # dyad title here (5-04), not the counting heading of R.HEAD (harmonise-notes §3)
    "Dhammānulome tikatikapaṭṭhānaṃ": "परिघटनाओं का सकारात्मक क्रम: तीन-तीन और तीन-तीन के वर्गीकरणों के कारण-संबंध",
    "Dhammānulome dukadukapaṭṭhānaṃ": "परिघटनाओं का सकारात्मक क्रम: दो-दो और दो-दो के वर्गीकरणों के कारण-संबंध",
    "Dhammapaccanīye tikapaṭṭhānaṃ": "परिघटनाओं का नकारात्मक क्रम: तीन-तीन के वर्गीकरणों के कारण-संबंध",
    "Dhammapaccanīye dukapaṭṭhānaṃ": "परिघटनाओं का नकारात्मक क्रम: दो-दो के वर्गीकरणों के कारण-संबंध",
})


def heading(line):
    m = re.fullmatch(r"(#+) (\*?)(\d+ ?-?[\d-]*\. )?(.*?)(\*?)", line)
    hashes, st, num, body, en = m.groups()
    h = HEAD[body] if body in HEAD else name(body)
    return f"{hashes} {st}{num or ''}{h}{en}"


S = "समाप्त"
CLOSING = {
    "kusalattikacūḷantaradukaṃ niṭṭhitaṃ": f"{TIKA['kusala']} और {DUKA['cūḷantara']} {S}",
    "kusalattikaāsavagocchakaṃ niṭṭhitaṃ": f"{TIKA['kusala']} और {GOC['āsava']} {S}",
    "kusalattike cha gocchakaṃ niṭṭhitaṃ": f"हितकर वाले तीन के वर्गीकरण में छह वर्ग {S}",
    "kusalattikamahantaradukaṃ niṭṭhitaṃ": f"{TIKA['kusala']} और {DUKA['mahantara']} {S}",
    "kusalattikaupādānagocchakaṃ niṭṭhitaṃ": f"{TIKA['kusala']} और {GOC['upādāna']} {S}",
    "kusalattikakilesagocchakaṃ niṭṭhitaṃ": f"{TIKA['kusala']} और {GOC['kilesa']} {S}",
    "kusalattikapiṭṭhidukaṃ niṭṭhitaṃ": f"{TIKA['kusala']} और {DUKA['piṭṭhi']} {S}",
    "sanidassanattikasaraṇadukaṃ niṭṭhitaṃ": f"{TIKA['sanidassana']} और {DUKA['saraṇa']} {S}",
    "dhammānulome tikadukapaṭṭhānaṃ niṭṭhitaṃ":
        f"परिघटनाओं का सकारात्मक क्रम: तीन-तीन और दो-दो के वर्गीकरणों के कारण-संबंध {S}",
    "catuttho bhāgo niṭṭhito": f"चौथा भाग {S}",
    "kusalattikasanidassanattikaṃ niṭṭhitaṃ": f"{TIKA['kusala']} और {TIKA['sanidassana']} {S}",
    "dhammānulome tikatikapaṭṭhānaṃ niṭṭhitaṃ":
        f"परिघटनाओं का सकारात्मक क्रम: तीन-तीन और तीन-तीन के वर्गीकरणों के कारण-संबंध {S}",
    "hetugocchakaṃ niṭṭhitaṃ": f"{GOC['hetu']} {S}",
    "cūḷantaradukaṃ niṭṭhitaṃ": f"{DUKA['cūḷantara']} {S}",
    "hetudukaāsavagocchakaṃ niṭṭhitaṃ": f"{DUKA['hetu']} और {GOC['āsava']} {S}",
    "hetudukaparāmāsagocchakaṃ niṭṭhitaṃ": f"{DUKA['hetu']} और {GOC['parāmāsa']} {S}",
    "hetudukamahantaradukaṃ niṭṭhitaṃ": f"{DUKA['hetu']} और {DUKA['mahantara']} {S}",
    "hetudukapiṭṭhidukaṃ niṭṭhitaṃ": f"{DUKA['hetu']} और {DUKA['piṭṭhi']} {S}",
    "dhammānulome dukadukapaṭṭhānaṃ niṭṭhitaṃ":
        f"परिघटनाओं का सकारात्मक क्रम: दो-दो और दो-दो के वर्गीकरणों के कारण-संबंध {S}",
    "anulomapaṭṭhānaṃ niṭṭhitaṃ": f"सकारात्मक क्रम के कारण-संबंध {S}",
    "dhammapaccanīye tikapaṭṭhānaṃ niṭṭhitaṃ":
        f"परिघटनाओं का नकारात्मक क्रम: तीन-तीन के वर्गीकरणों के कारण-संबंध {S}",
    "āsavagocchakaṃ niṭṭhitaṃ": f"{GOC['āsava']} {S}",
    "saññojanagocchakaṃ niṭṭhitaṃ": f"{GOC['saññojana']} {S}",
    "ganthagocchakaṃ niṭṭhitaṃ": f"{GOC['gantha']} {S}",
    "nīvaraṇagocchakaṃ niṭṭhitaṃ": f"{GOC['nīvaraṇa']} {S}",
    "parāmāsagocchakaṃ niṭṭhitaṃ": f"{GOC['parāmāsa']} {S}",
    "mahantaradukaṃ niṭṭhitaṃ": f"{DUKA['mahantara']} {S}",
    "piṭṭhidukaṃ niṭṭhitaṃ": f"{DUKA['piṭṭhi']} {S}",
    "dhammapaccanīye dukapaṭṭhānaṃ niṭṭhitaṃ":
        f"परिघटनाओं का नकारात्मक क्रम: दो-दो के वर्गीकरणों के कारण-संबंध {S}",
}

# ---------------------------------------------------------------- hand pieces

SEG_HAND = {
    # 4-17 ^7-51-34
    "akusalaṃ ganthaṃ": "हानिकर, गाँठ रूपी", "oghaṃ": "बाढ़ रूपी", "yogaṃ": "जकड़न रूपी",
    "nīvaraṇaṃ": "बाधा रूपी",
    "diṭṭhiṃ paṭicca diṭṭhi na uppajjati": "दृष्टि पर निर्भर होकर दृष्टि उत्पन्न नहीं होती",
    # 4-21 ^7-54-104
    "hetupaccayā": R.ABL["hetu"],
    # 5-02 ^7-56-85 (no dhammaṃ after the elision)
}
SENT_HAND = {}
_KH = "मन से उत्पन्न भौतिक रूप"
# bodies after « – » (paṭicca examples)
BODY = {
    # 5-03 ^7-57-1
    "akusalaṃ abyākataṃ ekaṃ khandhaṃ paṭicca akusalā abyākatā tayo khandhā cittasamuṭṭhānañca rūpaṃ…pe… dve "
    "khandhe paṭicca dve khandhā cittasamuṭṭhānañca rūpaṃ":
        f"एक हानिकर या नैतिक रूप से अनिर्धारित समूह पर निर्भर होकर हानिकर और नैतिक रूप से अनिर्धारित तीन समूह "
        f"और {_KH}… दो समूहों पर निर्भर होकर दो समूह और {_KH}",
    # 5-04 ^7-58-1
    "nahetuṃ ekaṃ khandhaṃ paṭicca tayo khandhā cittasamuṭṭhānañca rūpaṃ…pe… dve khandhe paṭicca dve khandhā "
    "cittasamuṭṭhānañca rūpaṃ; paṭisandhikkhaṇe…pe…":
        f"मूल रूपी न होने वाले एक समूह पर निर्भर होकर तीन समूह और {_KH}… दो समूहों पर निर्भर होकर दो समूह "
        f"और {_KH}; पुनर्जन्म के क्षण में…",
    "nahetū khandhe paṭicca hetū; paṭisandhikkhaṇe…pe…":
        "मूल रूपी न होने वाले समूहों पर निर्भर होकर मूल; पुनर्जन्म के क्षण में…",
    # 5-04 ^7-58-5
    "vicikicchāsahagataṃ uddhaccasahagataṃ mohaṃ paṭicca cittasamuṭṭhānaṃ rūpaṃ, ekaṃ mahābhūtaṃ paṭicca tayo "
    "mahābhūtā…pe… dve mahābhūte paṭicca dve mahābhūtā, mahābhūte paṭicca cittasamuṭṭhānaṃ rūpaṃ kaṭattārūpaṃ "
    "upādārūpaṃ":
        f"संशय के साथ होने वाले या बेचैनी के साथ होने वाले मोह पर निर्भर होकर {_KH}, एक महाभूत पर निर्भर होकर "
        f"तीन महाभूत… दो महाभूतों पर निर्भर होकर दो महाभूत, महाभूतों पर निर्भर होकर {_KH}, "
        f"{R.RUPA_KATATTA} और {R.RUPA_UPADA}",
    "vicikicchāsahagataṃ uddhaccasahagataṃ mohaṃ paṭicca sampayuttakā khandhā; paṭisandhikkhaṇe vatthuṃ paṭicca "
    "sahetukā khandhā":
        "संशय के साथ होने वाले या बेचैनी के साथ होने वाले मोह पर निर्भर होकर जुड़े हुए समूह; पुनर्जन्म के क्षण में "
        "आधार पर निर्भर होकर मूल वाले समूह",
    # 5-04 ^7-58-13
    "ekaṃ mahābhūtaṃ paṭicca tayo mahābhūtā…pe…": "एक महाभूत पर निर्भर होकर तीन महाभूत…",
    "paṭisandhikkhaṇe vatthuṃ paṭicca nahetusahetukā khandhā":
        "पुनर्जन्म के क्षण में आधार पर निर्भर होकर मूल रूपी न होने वाले, पर मूल वाले समूह",
    # 5-04 ^7-58-56
    "cittaṃ paṭicca cittasamuṭṭhānaṃ rūpaṃ": f"मन पर निर्भर होकर {_KH}",
    "cittaṃ paṭicca cittasampayuttakā khandhā": "मन पर निर्भर होकर मन से जुड़े हुए समूह",
    # 5-04 ^7-58-64
    "paṭisandhikkhaṇe cittaṃ paṭicca ajjhattikaṃ kaṭattārūpaṃ":
        "पुनर्जन्म के क्षण में मन पर निर्भर होकर किए गए कर्म से उत्पन्न आंतरिक भौतिक रूप",
}


def translate_line(line):
    if line.startswith("#"):
        return heading(line)
    line = line.replace("(yāva mahābhūtā)", "\x01")
    # bodies after « – »: translate the frame before and the body after separately
    out = []
    pieces = re.split(r"( ?\([^()]*\))", line)
    for p in pieces:
        if not p:
            continue
        m = re.fullmatch(r"( ?)\(([^()]*)\)", p)
        if m:
            out.append(m.group(1) + "(" + note_hi(m.group(2)) + ")")
        else:
            out.append(chunk_with_body(p))
    hi = "".join(out)
    hi = hi.replace("\x01", "(" + note_hi("yāva mahābhūtā") + ")")
    return hi


def chunk_with_body(chunk):
    """handles '<frame> – <body>. <frame> – <body>. …' inside a text chunk"""
    if " – " not in chunk:
        return text_chunk(chunk)
    out = []
    # split into sentences on '. ' and keep bodies
    for sent_ in re.split(r"(\.(?= |$))", chunk):
        if sent_ == ".":
            out.append("।")
            continue
        if " – " in sent_:
            lead = sent_[: len(sent_) - len(sent_.lstrip())]
            frame, body = sent_.strip().split(" – ", 1)
            b = lower_initials(body)
            bt = b.rstrip()
            # a body may end with the placeholder for «(yāva mahābhūtā)»
            ph = ""
            if bt.endswith("\x01"):
                bt, ph = bt[:-1].rstrip(), " \x01"
            # bodies may also run on into '…pe… <next frame>'
            if bt in BODY:
                out.append(lead + sentence(frame) + " – " + BODY[bt] + ph)
            else:
                m = re.fullmatch(r"(.+?…pe…) (.+)", bt)
                if m and m.group(1) in BODY:
                    out.append(lead + sentence(frame) + " – " + BODY[m.group(1)] + " " + sentence(m.group(2)) + ph)
                else:
                    raise KeyError(f"body: {bt!r}")
        else:
            out.append(text_chunk(sent_) if sent_.strip() else sent_)
    return "".join(out)


# ---------------------------------------------------------------- build

def build_file(name_):
    src = os.path.join(PALI_DIR, name_)
    dst = os.path.join(OUT_DIR, name_)
    lines = open(src, encoding="utf-8").read().split("\n")
    out = []
    for ln in lines:
        if not ln.strip():
            if out and out[-1] != "":
                out.append("")
            continue
        m = R.ID_RE.search(ln)
        body = ln[: m.start()] if m else ln.rstrip()
        try:
            hi = translate_line(body)
        except KeyError as e:
            raise SystemExit(f"{name_}: {e}\n  line: {body}")
        out.append(hi + (f" ^{m.group(1)}" if m else ""))
    while out and out[-1] == "":
        out.pop()
    with open(dst, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out) + "\n")


if __name__ == "__main__":
    names = sys.argv[1:] or FILES
    for n_ in names:
        build_file(n_)
        print("built", n_)
