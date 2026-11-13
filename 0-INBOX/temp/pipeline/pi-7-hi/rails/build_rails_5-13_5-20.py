"""pi-7 Paṭṭhāna, Hindi plain RAILS: builder for 5-13 .. 5-20 (anulomapaccanīya / paccanīyānuloma, all six methods).

Imports the approved sample constants read-only (build_rails_sample as R) and adds:
  - an item lexicon for every triad / dyad item (pi-1 1-matika.md Hindi, singular adjective), with the
    negation rule  na-/no- + item = «<item> न होने वाली»  (pi-1 wording where pi-1 has the na-item itself);
  - the paṭicca / paccayā frames and the pañhā frame over item phrases;
  - counts with number words beyond nine; headings; the editorial notes of these files.
Run:  python -I -B -X utf8 build_rails_5-13_5-20.py [--report]
"""
import os
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\rails")
import build_rails_sample as R  # noqa: E402

FILES = ["5-13-anulomapaccaniya-tikatika.md", "5-14-anulomapaccaniya-dukaduka.md", "5-15-paccaniyanuloma-tika.md",
         "5-16-paccaniyanuloma-duka.md", "5-17-paccaniyanuloma-dukatika.md", "5-18-paccaniyanuloma-tikaduka.md",
         "5-19-paccaniyanuloma-tikatika.md", "5-20-paccaniyanuloma-dukaduka.md"]

# ---------------------------------------------------------------- 1. item lexicon

POS = {}    # Pāli surface (lowercase) -> item id
HI = {}     # item id -> Hindi adjective (feminine singular, no noun)
NEG1 = {}   # item id -> pi-1 wording of the na-item (overrides «<item> न होने वाली»)


def a(stem):
    return [stem + "aṃ", stem + "o", stem + "assa"]


def i_(stem):
    return [stem + "iṃ", stem + "ī", stem + "ino"]


def reg(iid, hindi, forms, neg=None):
    HI[iid] = hindi
    for f in forms:
        POS[f] = iid
    if neg:
        NEG1[iid] = neg


# triads (pi-1 1-matika.md)
reg("kusala", "हितकर", a("kusal"))
reg("akusala", "हानिकर", a("akusal"))
reg("abyākata", "नैतिक रूप से अनिर्धारित", a("abyākat"))
reg("sukha-v", "सुखद अनुभूति से जुड़ी", a("sukhāya vedanāya sampayutt"))
reg("dukkha-v", "दुःखद अनुभूति से जुड़ी", a("dukkhāya vedanāya sampayutt"))
reg("adm-v", "न दुःखद, न सुखद अनुभूति से जुड़ी", a("adukkhamasukhāya vedanāya sampayutt"))
reg("vipāka", "कर्म-फल रूपी", a("vipāk"))
# «vipākadhammadhammaṃ» fuses the item with «dhammaṃ»; piece() splits it before paṭicca / paccayā / uppajj- / paccayena
reg("vipākadhamma", "कर्म-फल उत्पन्न करने वाली", a("vipākadhammadhamm") + ["vipākadhamma"])
reg("nevavipāka", "न कर्म-फल रूपी, न कर्म-फल उत्पन्न करने वाली",
    a("nevavipākanavipākadhammadhamm") + ["nevavipākanavipākadhamma"])
reg("upādinnupādāniya", "कर्म से उत्पन्न और आसक्ति का विषय बनने वाली", a("upādinnupādāniy"))
reg("anupādinnupādāniya", "कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाली", a("anupādinnupādāniy"))
reg("anupādinnaanupādāniya", "न कर्म से उत्पन्न, न आसक्ति का विषय बनने वाली", a("anupādinnaanupādāniy"))
reg("saṃkiliṭṭhasaṃkilesika", "क्लेशों से मलिन और क्लेशों का विषय बनने वाली", a("saṃkiliṭṭhasaṃkilesik"))
reg("asaṃkiliṭṭhasaṃkilesika", "क्लेशों से मलिन न होने वाली, पर क्लेशों का विषय बनने वाली", a("asaṃkiliṭṭhasaṃkilesik"))
reg("asaṃkiliṭṭhaasaṃkilesika", "क्लेशों से मलिन न होने वाली और क्लेशों का विषय न बनने वाली",
    a("asaṃkiliṭṭhaasaṃkilesik"))
reg("savitakkasavicāra", "आरंभिक विचार और सतत विचार वाली", a("savitakkasavicār"))
reg("avitakkavicāramatta", "आरंभिक विचार से रहित, केवल सतत विचार वाली", a("avitakkavicāramatt"))
reg("avitakkaavicāra", "आरंभिक विचार और सतत विचार दोनों से रहित", a("avitakkaavicār"))
reg("pītisahagata", "उल्लास के साथ होने वाली", a("pītisahagat"), neg="उल्लास के साथ न होने वाली")
reg("sukhasahagata", "सुख के साथ होने वाली", a("sukhasahagat"), neg="सुख के साथ न होने वाली")
reg("upekkhāsahagata", "समभाव के साथ होने वाली", a("upekkhāsahagat"), neg="समभाव के साथ न होने वाली")
reg("dassana", "सत्य-दर्शन से छोड़ी जाने वाली", a("dassanena pahātabb"), neg="सत्य-दर्शन से न छोड़ी जाने वाली")
reg("bhāvanā", "मानसिक अभ्यास से छोड़ी जाने वाली", a("bhāvanāya pahātabb"), neg="मानसिक अभ्यास से न छोड़ी जाने वाली")
reg("nevadassana", "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़ी जाने वाली", a("nevadassanena nabhāvanāya pahātabb"))
reg("dassanahetu", "सत्य-दर्शन से छोड़े जाने वाले मूलों वाली", a("dassanena pahātabbahetuk"),
    neg="सत्य-दर्शन से छोड़े जाने वाले मूलों से रहित")
reg("bhāvanāhetu", "मानसिक अभ्यास से छोड़े जाने वाले मूलों वाली", a("bhāvanāya pahātabbahetuk"),
    neg="मानसिक अभ्यास से छोड़े जाने वाले मूलों से रहित")
reg("nevadassanahetu", "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़े जाने वाले मूलों वाली",
    a("nevadassanena nabhāvanāya pahātabbahetuk"))
reg("ācayagāmī", "संचय की ओर ले जाने वाली", i_("ācayagām"))
reg("apacayagāmī", "संचय घटाने की ओर ले जाने वाली", i_("apacayagām"))
reg("nevācayagāmī", "न संचय की ओर, न संचय घटाने की ओर ले जाने वाली", i_("nevācayagāmināpacayagām"))
reg("sekkha", "सीखने के चरण की", a("sekkh"))
reg("asekkha", "सीखना पूरा होने के चरण की", a("asekkh"))
reg("nevasekkha", "न सीखने के चरण की, न सीखना पूरा होने के चरण की", a("nevasekkhanāsekkh"))
reg("paritta", "सीमित", a("paritt"))
reg("mahaggata", "उन्नत", a("mahaggat"))
reg("appamāṇa", "अपरिमित", a("appamāṇ"))
reg("parittārammaṇa", "सीमित विषय वाली", a("parittārammaṇ"))
reg("mahaggatārammaṇa", "उन्नत विषय वाली", a("mahaggatārammaṇ"))
reg("appamāṇārammaṇa", "अपरिमित विषय वाली", a("appamāṇārammaṇ"))
reg("hīna", "हीन", a("hīn"))
reg("majjhima", "मध्यम", a("majjhim"))
reg("paṇīta", "उत्तम", a("paṇīt"))
reg("micchattaniyata", "ग़लत दिशा में निश्चित", a("micchattaniyat"))
reg("sammattaniyata", "सही दिशा में निश्चित", a("sammattaniyat"))
reg("aniyata", "अनिश्चित", a("aniyat"))
reg("maggārammaṇa", "मार्ग को विषय बनाने वाली", a("maggārammaṇ"))
reg("maggahetuka", "मार्ग को मूल बनाने वाली", a("maggahetuk"))
reg("maggādhipati", "मार्ग की प्रधानता वाली", ["maggādhipatiṃ", "maggādhipati", "maggādhipatino"])
reg("uppanna", "उत्पन्न हो चुकी", a("uppann"))
reg("anuppanna", "उत्पन्न न हुई", a("anuppann"))
reg("uppādī", "उत्पन्न होने वाली", i_("uppād"))
reg("atīta", "अतीत की", a("atīt"))
reg("anāgata", "भविष्य की", a("anāgat"))
reg("paccuppanna", "वर्तमान की", a("paccuppann"))
reg("atītārammaṇa", "अतीत के विषय वाली", a("atītārammaṇ"))
reg("anāgatārammaṇa", "भविष्य के विषय वाली", a("anāgatārammaṇ"))
reg("paccuppannārammaṇa", "वर्तमान के विषय वाली", a("paccuppannārammaṇ"))
reg("ajjhatta", "स्वयं से संबंधित", a("ajjhatt"))
reg("bahiddhā", "दूसरों से संबंधित", ["bahiddhā"])
reg("ajjhattārammaṇa", "स्वयं से संबंधित विषय वाली", a("ajjhattārammaṇ"))
reg("bahiddhārammaṇa", "दूसरों से संबंधित विषय वाली", a("bahiddhārammaṇ"))
reg("sanidassanasappaṭigha", "दिखाई देने वाली और टकराव वाली", a("sanidassanasappaṭigh"))
reg("anidassanasappaṭigha", "दिखाई न देने वाली, पर टकराव वाली", a("anidassanasappaṭigh"))
reg("anidassanaappaṭigha", "दिखाई न देने वाली और टकराव से रहित", a("anidassanaappaṭigh"))
# dyads (pi-1 1-matika.md)
reg("hetu", "मूल रूपी", ["hetuṃ", "hetu", "hetussa"])
reg("sahetuka", "मूल वाली", a("sahetuk"))
reg("ahetuka", "मूल से रहित", a("ahetuk"))
reg("hetusampayutta", "मूलों से जुड़ी", a("hetusampayutt"))
reg("hetuvippayutta", "मूलों से अलग", a("hetuvippayutt"))
reg("sappaccaya", "कारणों पर निर्भर रहने वाली", a("sappaccay"))
reg("appaccaya", "कारणों पर निर्भर न रहने वाली", a("appaccay"))
reg("saṅkhata", "निर्मित", a("saṅkhat"))
reg("asaṅkhata", "अनिर्मित", a("asaṅkhat"))
reg("sanidassana", "दिखाई देने वाली", a("sanidassan"))
reg("anidassana", "दिखाई न देने वाली", a("anidassan"))
reg("sappaṭigha", "टकराव वाली", a("sappaṭigh"))
reg("appaṭigha", "टकराव से रहित", a("appaṭigh"))
reg("rūpī", "भौतिक", i_("rūp"))
reg("arūpī", "अभौतिक", i_("arūp"))
reg("lokiya", "लौकिक", a("lokiy"))
reg("lokuttara", "लोकोत्तर", a("lokuttar"))
reg("kenaci", "किसी एक प्रकार की चेतना से जानी जा सकने वाली", a("kenaci viññeyy"),
    neg="किसी एक प्रकार की चेतना से न जानी जा सकने वाली")
# «kenaci naviññeyya» is the same item as «nakenaci viññeyya» (pi-1 (ख))
reg("kenaci-na", "किसी एक प्रकार की चेतना से न जानी जा सकने वाली", a("kenaci naviññeyy"))
reg("āsava", "मन के मैल रूपी", a("āsav"))
reg("sāsava", "मन के मैलों का विषय बनने वाली", a("sāsav"))   # pi-1 (ख) is anāsava, not na-sāsava
reg("anāsava", "मन के मैलों का विषय न बनने वाली", a("anāsav"))
reg("āsavasampayutta", "मन के मैलों से जुड़ी", a("āsavasampayutt"))
reg("āsavavippayutta", "मन के मैलों से अलग", a("āsavavippayutt"))
reg("saññojana", "बंधन रूपी", a("saññojan"))
reg("gantha", "गाँठ रूपी", a("ganth"))
reg("ogha", "बाढ़ रूपी", a("ogh"))
reg("yoga", "जकड़न रूपी", a("yog"))
reg("nīvaraṇa", "बाधा रूपी", a("nīvaraṇ"))
reg("parāmāsa", "ग़लत धारणा रूपी", a("parāmās"))
reg("sārammaṇa", "विषय वाली", a("sārammaṇ"))
reg("anārammaṇa", "विषय से रहित", a("anārammaṇ"))
reg("citta", "मन रूपी", a("citt"))
reg("cetasika", "मन की सहचर", a("cetasik"))
reg("acetasika", "मन की सहचर न होने वाली", a("acetasik"))
reg("cittasampayutta", "मन से जुड़ी", a("cittasampayutt"))
reg("cittavippayutta", "मन से अलग", a("cittavippayutt"))
reg("cittasaṃsaṭṭha", "मन से घुली-मिली", a("cittasaṃsaṭṭh"))
reg("cittavisaṃsaṭṭha", "मन से घुली-मिली न होने वाली", a("cittavisaṃsaṭṭh"))
reg("cittasamuṭṭhāna", "मन से उत्पन्न", a("cittasamuṭṭhān"))
# termbase: «no-» (the pi-1 (ख) item) = pi-1 wording, «na-» (the Paṭṭhāna negation) = «… होने वाली न होने वाली»
reg("cittasahabhū", "मन के साथ-साथ होने वाली", ["cittasahabhuṃ", "cittasahabhū", "cittasahabhuno"],
    neg="मन के साथ-साथ न होने वाली")
reg("cittānuparivattī", "मन का अनुसरण करने वाली", i_("cittānuparivatt"), neg="मन का अनुसरण न करने वाली")
NO_ONLY = {"cittasahabhū", "cittānuparivattī"}
reg("cssamuṭṭhāna", "मन से घुली-मिली और मन से उत्पन्न", a("cittasaṃsaṭṭhasamuṭṭhān"))
reg("cssahabhū", "मन से घुली-मिली, मन से उत्पन्न और मन के साथ-साथ होने वाली",
    ["cittasaṃsaṭṭhasamuṭṭhānasahabhuṃ", "cittasaṃsaṭṭhasamuṭṭhānasahabhū", "cittasaṃsaṭṭhasamuṭṭhānasahabhuno"])
reg("csanuparivattī", "मन से घुली-मिली, मन से उत्पन्न और मन का अनुसरण करने वाली",
    i_("cittasaṃsaṭṭhasamuṭṭhānānuparivatt"))
reg("ajjhattika", "आंतरिक", a("ajjhattik"))
reg("bāhira", "बाह्य", a("bāhir"))
reg("upādā", "व्युत्पन्न", ["upādā"])
reg("upādinna", "कर्म से उत्पन्न", a("upādinn"))
reg("anupādinna", "कर्म से उत्पन्न न होने वाली", a("anupādinn"))
reg("upādāna", "आसक्ति रूपी", a("upādān"))
reg("kilesa", "मन के क्लेश रूपी", a("kiles"))
reg("savitakka", "आरंभिक विचार वाली", a("savitakk"))
reg("avitakka", "आरंभिक विचार से रहित", a("avitakk"))
reg("savicāra", "सतत विचार वाली", a("savicār"))
reg("avicāra", "सतत विचार से रहित", a("avicār"))
reg("sappītika", "उल्लास वाली", a("sappītik"))
reg("appītika", "उल्लास से रहित", a("appītik"))
reg("kāmāvacara", "इंद्रिय-सुखों के लोक से संबंधित", a("kāmāvacar"))
reg("rūpāvacara", "सूक्ष्म भौतिक लोक से संबंधित", a("rūpāvacar"))
reg("arūpāvacara", "अभौतिक लोक से संबंधित", a("arūpāvacar"))
reg("pariyāpanna", "अस्तित्व के लोकों में समाई हुई", a("pariyāpann"))
reg("apariyāpanna", "अस्तित्व के लोकों में न समाई हुई", a("apariyāpann"))
reg("niyyānika", "मुक्ति की ओर ले जाने वाली", a("niyyānik"))
reg("aniyyānika", "मुक्ति की ओर न ले जाने वाली", a("aniyyānik"))
reg("niyata", "निश्चित", a("niyat"))
reg("sauttara", "सर्वोच्च न होने वाली", a("sauttar"))
reg("anuttara", "सर्वोच्च", a("anuttar"))
reg("saraṇa", "संघर्ष वाली", a("saraṇ"))
reg("araṇa", "संघर्ष से रहित", a("araṇ"))

NEG = " न होने वाली"


def item(s):
    """Hindi for one item surface (possibly multiword), with any number of na-/no- prefixes; None if unknown."""
    if s in POS:
        return HI[POS[s]]
    for p in ("na", "no"):
        if s.startswith(p) and len(s) > 2:
            rest = s[2:]
            if rest in POS and POS[rest] in NEG1 and (p == "no" or POS[rest] not in NO_ONLY):
                return NEG1[POS[rest]]
            h = item(rest)
            if h is not None:
                return h + NEG
    return None


CA, CEVA = "\x01CA", "\x01CEVA"


def tokens(text):
    out = []
    for w in text.split(" "):
        if w == "ca":
            out.append(CA)
        elif w == "ceva":
            out.append(CEVA)
        elif w.endswith("ñceva"):
            out += [w[:-5] + "ṃ", CEVA]
        elif w.endswith("ñca"):
            out += [w[:-3] + "ṃ", CA]
        else:
            out.append(w)
    return out


def _item_at(toks, i):
    for n in (4, 3, 2, 1):
        if i + n <= len(toks) and all(not t.startswith("\x01") for t in toks[i:i + n]):
            h = item(" ".join(toks[i:i + n]))
            if h is not None:
                return h, i + n
    raise KeyError("item: " + " ".join(t for t in toks[i:i + 4]))


def phrase(text):
    """Item phrase before dhammaṃ / dhammo / dhammā / dhammassa -> list of conjuncts (each a list of unit strings)."""
    toks = tokens(text)
    conj, cur, i = [], [], 0
    while i < len(toks):
        t = toks[i]
        if t == CA:
            conj.append(cur)
            cur = []
            i += 1
            continue
        h, i = _item_at(toks, i)
        if i < len(toks) and toks[i] == CEVA:
            i += 1
            negw = None
            if i + 1 < len(toks) and toks[i] in ("na", "no", "nana", "nano") and toks[i + 1] == CA:
                negw = toks[i]
                i += 2
            h2, i = _item_at(toks, i)
            if negw in ("na", "no"):
                h = f"{h}, पर स्वयं {h2}{NEG}"              # X ceva na ca Y (pi-1)
            elif negw:
                h = f"{h} भी और {h2}{NEG}{NEG} भी"          # X ceva nana ca Y
            else:
                if i < len(toks) and toks[i] == CA:
                    i += 1
                h = f"{h} भी और {h2} भी"                    # X ceva Y ca (pi-1)
        cur.append(h)
    if cur:
        conj.append(cur)
    return [", ".join(c) for c in conj]


def join_and(xs):
    return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " और " + xs[-1]


def np_sg(text):
    """... dhammaṃ / dhammo / dhammassa (one noun per conjunct)."""
    cs = phrase(text)
    return join_and([c + " परिघटना" for c in cs])


def np_pl(text):
    """... ca … ca dhammā."""
    return join_and(phrase(text)) + " परिघटनाएँ"


# ---------------------------------------------------------------- 2. numbers and counts

NUM = dict(R.NUM)
NUM.update({"dasa": "दस", "terasa": "तेरह", "cuddasa": "चौदह", "pannarasa": "पंद्रह", "sattarasa": "सत्रह",
            "aṭṭhārasa": "अठारह", "ekavīsati": "इक्कीस", "ekavīsa": "इक्कीस", "dvāvīsa": "बाईस", "tevīsa": "तेईस",
            "chabbīsati": "छब्बीस", "chabbīsa": "छब्बीस", "aṭṭhavīsa": "अट्ठाईस", "pañcatiṃsa": "पैंतीस",
            "ekūnapaññāsa": "उनचास", "ekādasa": "ग्यारह", "dvādasa": "बारह", "soḷasa": "सोलह", "catuvīsa": "चौबीस",
            "tīṇiyeva": "तीन ही", "tīṇimeva": "तीन ही", "ekameva": "एक ही", "dveyeva": "दो ही"})
CWORDS = {}
for _d in (R.P_ABL, R.P_NABL, R.P_LOC, R.P_NLOC, NUM):
    CWORDS.update(_d)
ABLS = set(R.P_ABL) | set(R.P_NABL)


def is_count(core):
    ws = core.split(" ")
    return bool(core) and all(w in CWORDS for w in ws)


def count(core):
    ws = core.split(" ")
    out = []
    for j, w in enumerate(ws):
        if j:
            out.append(", " if ws[j - 1] in ABLS else " ")
        out.append(CWORDS[w])
    return "".join(out)


# ---------------------------------------------------------------- 3. headings

TIKA = {  # triad stem in headings -> Hindi base before «वाला» (harmonise-notes §1)
    "kusala": "हितकर", "vedanā": "अनुभूति", "vipāka": "कर्म-फल", "upādinna": "कर्म से उत्पन्न परिघटनाओं",
    "saṃkiliṭṭha": "क्लेशों से मलिन परिघटनाओं", "vitakka": "आरंभिक विचार", "pīti": "उल्लास",
    "dassana": "सत्य-दर्शन से छोड़ी जाने वाली परिघटनाओं", "dassanahetu": "सत्य-दर्शन से छोड़े जाने वाले मूलों",
    "ācayagāmi": "संचय की ओर ले जाने", "sekkha": "सीखने के चरण", "paritta": "सीमित", "parittārammaṇa": "सीमित विषय",
    "hīna": "हीन", "micchattaniyata": "ग़लत दिशा में निश्चित परिघटनाओं", "maggārammaṇa": "मार्ग को विषय बनाने",
    "uppanna": "उत्पन्न", "atīta": "अतीत", "atītārammaṇa": "अतीत के विषय",
    "ajjhatta": "स्वयं से संबंधित परिघटनाओं", "ajjhattārammaṇa": "स्वयं से संबंधित विषय",
    "sanidassana": "दिखाई देने वाला और टकराव",
}
DUKA = {
    "hetu": "मूल", "sahetuka": "मूल वाली परिघटनाओं", "hetusampayutta": "मूलों से जुड़ी परिघटनाओं",
    "hetusahetuka": "मूल रूपी भी और मूल वाली भी परिघटनाओं",
    "hetuhetusampayutta": "मूल रूपी भी और मूलों से जुड़ी भी परिघटनाओं",
    "nahetusahetuka": "मूल रूपी न होने वाली, पर मूल वाली परिघटनाओं",
    "sappaccaya": "कारणों पर निर्भर रहने वाली परिघटनाओं", "sanidassana": "दिखाई देने वाली परिघटनाओं",
    "sappaṭigha": "टकराव वाली परिघटनाओं", "rūpī": "भौतिक परिघटनाओं", "lokiya": "लौकिक परिघटनाओं",
    "kenaciviññeyya": "किसी एक प्रकार की चेतना से जानी जा सकने वाली परिघटनाओं",
    "āsava": "मन के मैल", "sāsava": "मन के मैलों के विषय", "āsavasampayutta": "मन के मैलों से जुड़ाव",
    "āsavasāsava": "मन के मैल और मन के मैलों के विषय",
    "āsavaāsavasampayutta": "मन के मैल और मन के मैलों से जुड़ाव",
    "āsavavippayuttasāsava": "मन के मैलों से अलगाव और मन के मैलों के विषय",
    "upādāna": "आसक्ति", "kilesa": "मन के क्लेश", "saraṇa": "संघर्ष",
    "dassanenapahātabba": "सत्य-दर्शन से छोड़े जाने",
    "kāmāvacara": "इंद्रिय-सुखों के लोक", "rūpāvacara": "सूक्ष्म भौतिक लोक", "arūpāvacara": "अभौतिक लोक",
    "pariyāpanna": "अस्तित्व के लोकों में समाए होने", "niyyānika": "मुक्ति की ओर ले जाने", "niyata": "निश्चित",
    "sauttara": "सर्वोच्च न होने",
}
CLUSTER = {  # pi-1 cluster names
    "hetugocchaka": "मूलों का वर्ग", "āsavagocchaka": "मन के मैलों का वर्ग",
    "saññojanagocchaka": "बंधनों का वर्ग", "upādānagocchaka": "आसक्ति का वर्ग",
    "kilesagocchaka": "मन के क्लेशों का वर्ग",
    "cūḷantaraduka": "बीच के छोटे दो-दो के वर्गीकरण", "mahantaraduka": "बीच के बड़े दो-दो के वर्गीकरण",
    "piṭṭhiduka": "अंतिम दो-दो के वर्गीकरण",
}
CLUSTER_PL = {  # «X-ādi-gocchakāni» / «X-gocchakāni»: base of «X आदि के वर्ग»
    "saññojana": "बंधनों", "āsava": "मन के मैलों",
}


def name_part(p):
    """One member of a (combined) triad / dyad / cluster heading, Pāli stem with its suffix."""
    p = p.lower()
    for suf, kind in (("ttikadvayaṃ", "dvaya"), ("ttikadvaya", "dvaya"), ("ādittikāni", "ādi-pl"),
                      ("ttikādi", "ādi"), ("ttikaṃ", "sg"), ("ttika", "sg")):
        st = p[: -len(suf)] + ("a" if suf.startswith("ā") else "")
        if p.endswith(suf) and st in TIKA:
            b = TIKA[st]
            return {"sg": f"{b} वाला तीन का वर्गीकरण", "ādi": f"{b} वाला तीन का वर्गीकरण आदि",
                    "ādi-pl": f"{b} आदि वाले तीन-तीन के वर्गीकरण", "dvaya": f"{b} वाले दोनों तीन के वर्गीकरण"}[kind]
    for suf, kind in (("ādichagocchakāni", "cha"), ("ādigocchakāni", "ādi-gpl"), ("gocchakāni", "gpl"),
                      ("ādigocchakaṃ", "ādi-g"), ("gocchakādi", "g-ādi"), ("gocchakaṃ", "g"), ("gocchaka", "g")):
        if p.endswith(suf):
            s = p[: -len(suf)]
            if kind == "cha":
                return f"{CLUSTER_PL[s + 'a']} आदि के छह वर्ग"
            if kind == "ādi-gpl":
                return f"{CLUSTER_PL[s + 'a']} आदि के वर्ग"
            if kind == "gpl":
                return f"{CLUSTER[s + 'gocchaka']} के दो-दो के वर्गीकरण"
            if kind == "ādi-g":
                return f"{CLUSTER[s + 'agocchaka']} आदि"
            if kind == "g-ādi":
                return f"{CLUSTER[s + 'gocchaka']} आदि"
            return CLUSTER[s + "gocchaka"]
    for suf, kind in (("dukāni", "pl"), ("dukādi", "ādi"), ("dukaṃ", "sg"), ("duka", "sg")):
        if p.endswith(suf):
            s = p[: -len(suf)]
            if s + "duka" in CLUSTER:
                return CLUSTER[s + "duka"] + (" आदि" if kind == "ādi" else "")
            if s.endswith("ādi") and kind == "pl":
                return f"{DUKA[s[:-3] + 'a']} आदि वाले दो-दो के वर्गीकरण"
            if s in DUKA:
                b = DUKA[s]
                return {"sg": f"{b} वाला दो का वर्गीकरण", "ādi": f"{b} वाला दो का वर्गीकरण आदि",
                        "pl": f"{b} वाले दो-दो के वर्गीकरण"}[kind]
    raise KeyError("name part: " + p)


HEAD = {
    "Dhammānulomapaccanīye tikatikapaṭṭhānaṃ":
        "परिघटनाओं का सकारात्मक-नकारात्मक क्रम: तीन-तीन और तीन-तीन के वर्गीकरणों के कारण-संबंध",
    "Dhammānulomapaccanīye dukadukapaṭṭhānaṃ":
        "परिघटनाओं का सकारात्मक-नकारात्मक क्रम: दो-दो और दो-दो के वर्गीकरणों के कारण-संबंध",
    "Dhammapaccanīyānulome tikapaṭṭhānaṃ": "परिघटनाओं का नकारात्मक-सकारात्मक क्रम: तीन-तीन के वर्गीकरणों के कारण-संबंध",
    "Dhammapaccanīyānulome dukapaṭṭhānaṃ": "परिघटनाओं का नकारात्मक-सकारात्मक क्रम: दो-दो के वर्गीकरणों के कारण-संबंध",
    "Dhammapaccanīyānulome dukatikapaṭṭhānaṃ":
        "परिघटनाओं का नकारात्मक-सकारात्मक क्रम: दो-दो और तीन-तीन के वर्गीकरणों के कारण-संबंध",
    "Dhammapaccanīyānulome tikadukapaṭṭhānaṃ":
        "परिघटनाओं का नकारात्मक-सकारात्मक क्रम: तीन-तीन और दो-दो के वर्गीकरणों के कारण-संबंध",
    "Dhammapaccanīyānulome tikatikapaṭṭhānaṃ":
        "परिघटनाओं का नकारात्मक-सकारात्मक क्रम: तीन-तीन और तीन-तीन के वर्गीकरणों के कारण-संबंध",
    "Dhammapaccanīyānulome dukadukapaṭṭhānaṃ":
        "परिघटनाओं का नकारात्मक-सकारात्मक क्रम: दो-दो और दो-दो के वर्गीकरणों के कारण-संबंध",
    "Paccanīyaṃ": "नकारात्मक क्रम",
    "Nahetunaārammaṇapaccayādi": f"{R.NNAME['hetu']} और {R.NNAME['ārammaṇa']} आदि",
    "Nahetu-naārammaṇapaccayā": f"{R.NNAME['hetu']} और {R.NNAME['ārammaṇa']}",
    "Hetu-ārammaṇapaccayā": f"{R.NAME['hetu']} और {R.NAME['ārammaṇa']}",
    "Hetuārammaṇapaccayādi": f"{R.NAME['hetu']} और {R.NAME['ārammaṇa']} आदि",
    "Hetu-anantarapaccayā": f"{R.NAME['hetu']} और {R.NAME['anantara']}",
    "Paṭiccavārādi": "निर्भरता का खंड आदि",
    "Paccayavārādi": "कारण का खंड आदि",
    "Paccayacatukkaṃ": "कारणों के चार क्रम",
    "Paccanīyuddhāro": "नकारात्मक क्रम के लिए कारणों की छँटाई",
    "Anuttarapadaṃ": "सर्वोच्च पद",
}


def head_body(b):
    if b in HEAD:
        return HEAD[b]
    if b in R.HEAD:
        return R.HEAD[b]
    parts = b.split("-")
    return " और ".join(name_part(p) for p in parts)


def heading(line):
    m = re.fullmatch(r"(#+) (\*?)((?:\d+-)*\d+\.? )?(.*?)(\*?)", line)
    hashes, st, num, body, en = m.groups()
    return f"{hashes} {st}{num or ''}{head_body(body)}{en}"


# ---------------------------------------------------------------- 4. notes and hand sentences

SAMPAYUTTAVARA = "सह-उत्पत्ति का खंड, कारण का खंड, आश्रय का खंड, घुले-मिले होने का खंड और जुड़ाव का खंड"
SAMPAYUTTAVARA_OBL = "सह-उत्पत्ति के खंड, कारण के खंड, आश्रय के खंड, घुले-मिले होने के खंड और जुड़ाव के खंड"
GANITAKENA = "गणना की विधि से"
MULA = "मूल वाक्य"
DUKAMULA = "दो पदों वाला मूल वाक्य"
SAMKHITTAM = "संक्षिप्त"


def P(text):
    """Item phrase without noun (for notes)."""
    return join_and(phrase(text))


NOTE = {
    "saṃkhittaṃ.": f"{SAMKHITTAM}।",
    "saṃkhittaṃ": SAMKHITTAM,
    "sahajātavārampi paccayavārampi nissayavārampi saṃsaṭṭhavārampi sampayuttavārampi paṭiccavārasadisaṃ.":
        f"{SAMPAYUTTAVARA} भी निर्भरता के खंड के समान हैं।",
    "pañhāvārampi vitthāretabbaṃ.": "प्रश्नों के खंड का भी विस्तार करना चाहिए।",
    "sahajātavārampi…pe… pañhāvārampi vitthāretabbaṃ.":
        "सह-उत्पत्ति के खंड का भी… प्रश्नों के खंड का भी विस्तार करना चाहिए।",
    "sahajātavārampi…pe… sampayuttavārampi paṭiccavārasadisaṃ.":
        "सह-उत्पत्ति का खंड भी… जुड़ाव का खंड भी निर्भरता के खंड के समान है।",
    "sabbattha vitthāro": "हर जगह विस्तार",
    "kusale pañca, akusale pañca, abyākate tīṇi.":
        "हितकर परिघटना में पाँच, हानिकर परिघटना में पाँच, नैतिक रूप से अनिर्धारित परिघटना में तीन।",
    "dve mūlāni.": f"दो {MULA}।",
    "uppādī anuppannasadisaṃ.": f"{P('uppādī')} परिघटना, {P('anuppanno')} परिघटना के समान है।",
    "anāgataṃ atītasadisaṃ.": f"{P('anāgataṃ')} परिघटना, {P('atīto')} परिघटना के समान है।",
    # «veditakaṃ» is unclear (perhaps veditabbaṃ); rendered as «known»
    "tīṇi veditakaṃ kātabbaṃ.": "तीन को जानकर तैयार करना चाहिए।",
    "ekavīsati pañhā.": "इक्कीस प्रश्न।",
    "dukkhāya vedanāya sampayuttaabyākatamūlaṃ adukkhamasukhāya vedanāya sampayuttaabyākatamūlampi kātabbaṃ.":
        f"{P('dukkhāya vedanāya sampayutto abyākato')} परिघटना का {MULA} और "
        f"{P('adukkhamasukhāya vedanāya sampayutto abyākato')} परिघटना का {MULA} भी तैयार करना चाहिए।",
    "vedanāttikasadisaṃ. saṃkhittaṃ.": f"अनुभूति वाले तीन के वर्गीकरण के समान। {SAMKHITTAM}।",
    "pañhāvāraṃ vitthāretabbaṃ.": "प्रश्नों के खंड का विस्तार करना चाहिए।",
    # 5-14
    "sahetukasadisaṃ.": f"{P('sahetuko')} परिघटना के समान।",
    "asaṅkhataṃ appaccayasadisaṃ.": f"{P('asaṅkhato')} परिघटना, {P('appaccayo')} परिघटना के समान है।",
    "lokiyasadisaṃ.": f"{P('lokiyo')} परिघटना के समान।",
    "saṃkhittaṃ. nayavasena vitthāretabbaṃ": f"{SAMKHITTAM}। विधि के अनुसार विस्तार करना चाहिए",
    "saṅkhataṃ sappaccayasadisaṃ": f"{P('saṅkhato')} परिघटना, {P('sappaccayo')} परिघटना के समान है",
    "saṅkhataṃ sappaccayasadisaṃ.": f"{P('saṅkhato')} परिघटना, {P('sappaccayo')} परिघटना के समान है।",
    "sabbattha pañca.": "हर जगह पाँच।",
    "lokiyadukasadisaṃ.": f"{DUKA['lokiya']} वाले दो के वर्गीकरण के समान।",
    "sabbattha pañhe saṃkhittaṃ.": f"हर जगह प्रश्नों में {SAMKHITTAM}।",
    "sahetukadukasadisaṃ.": f"{DUKA['sahetuka']} वाले दो के वर्गीकरण के समान।",
    "hetusahetukadukasadisaṃ.": f"{DUKA['hetusahetuka']} वाले दो के वर्गीकरण के समान।",
    "etena upāyena sabbattha vitthāretabbaṃ.": "इसी उपाय से हर जगह विस्तार करना चाहिए।",
    # 5-15, 5-16
    "sahajātavāro paṭiccavārasadiso": "सह-उत्पत्ति का खंड निर्भरता के खंड के समान है",
    "yathā kusalattike pañhāvārassa anulomampi paccanīyampi anulomapaccanīyampi paccanīyānulomampi gaṇitaṃ, evaṃ gaṇetabbaṃ.":
        "जैसे हितकर वाले तीन के वर्गीकरण में प्रश्नों के खंड का सकारात्मक क्रम, नकारात्मक क्रम, सकारात्मक-नकारात्मक क्रम "
        "और नकारात्मक-सकारात्मक क्रम भी गिना गया है, वैसे ही गिनना चाहिए।",
    # 5-17
    "sabbattha nava pañhā.": "हर जगह नौ प्रश्न।",
    "saṃkhittaṃ, nava pañhā": f"{SAMKHITTAM}, नौ प्रश्न",
    "nava pañhā.": "नौ प्रश्न।",
    "saṃkhittaṃ, nava pañhā kātabbā": f"{SAMKHITTAM}, नौ प्रश्न तैयार करने चाहिए",
    "nava pañhā kātabbā.": "नौ प्रश्न तैयार करने चाहिए।",
    "nava pañhā kātabbā": "नौ प्रश्न तैयार करने चाहिए",
    "sappaccayadukasadisaṃ": f"{DUKA['sappaccaya']} वाले दो के वर्गीकरण के समान",
    "sabbattha nava.": "हर जगह नौ।",
    "dukamūlakaṃ ekaṃ.": f"{DUKAMULA} एक।",
    "āsavaāsavasampayuttadukaṃ natthi.": f"{DUKA['āsavaāsavasampayutta']} वाला दो का वर्गीकरण नहीं है।",
    "naakusale tīṇi. naabyākate tīṇi. saṃkhittaṃ.":
        f"{P('naakusalo')} परिघटना में तीन। {P('naabyākato')} परिघटना में तीन। {SAMKHITTAM}।",
    "nava pañhā saṃkhittaṃ.": f"नौ प्रश्न {SAMKHITTAM}।",
    "dukamūlaṃ ekaṃ saṃkhittaṃ, sabbattha tīṇi.": f"{DUKAMULA} एक, {SAMKHITTAM}, हर जगह तीन।",
    "ajjhattattiko na labbhati paṭiccavārādīsu.":
        f"{TIKA['ajjhatta']} वाला तीन का वर्गीकरण निर्भरता के खंड आदि में लागू नहीं होता।",
    "ajjhattabahiddhārammaṇaṃ natthi.": "स्वयं और दूसरों दोनों से संबंधित विषय वाली परिघटना नहीं है।",
    "nahetunaanidassanasappaṭighamūlepi tīṇiyeva.":
        f"{P('nahetu naanidassanasappaṭigho')} परिघटना के {MULA} में भी तीन ही।",
    "nasahetukanaanidassanasappaṭighamūlepi tīṇiyeva.":
        f"{P('nasahetuko naanidassanasappaṭigho')} परिघटना के {MULA} में भी तीन ही।",
    "nahetusampayuttaṃ nasanidassanasappaṭighaṃ sahetukadukasadisaṃ. tīṇi pañhā. hetusahetukaduke ca hetuhetusampayuttaduke ca pañhā no labbhati.":
        f"{P('nahetusampayuttaṃ nasanidassanasappaṭighaṃ')} परिघटना, {DUKA['sahetuka']} वाले दो के वर्गीकरण के समान है। "
        f"तीन प्रश्न। {DUKA['hetusahetuka']} वाले दो के वर्गीकरण में और {DUKA['hetuhetusampayutta']} वाले दो के "
        "वर्गीकरण में प्रश्न लागू नहीं होते।",
    "naappaccayanaanidassanaappaṭighamūlepi ekameva.":
        f"{P('naappaccayo naanidassanaappaṭigho')} परिघटना के {MULA} में भी एक ही।",
    "nasaṅkhataṃ nasappaccayasadisaṃ.":
        f"{P('nasaṅkhataṃ')} परिघटना, {P('nasappaccayaṃ')} परिघटना के समान है।",
    "sabbattha tīṇi.": "हर जगह तीन।",
    "gaṇitakena gaṇetabbā tīṇi pañhā.": f"{GANITAKENA} तीन प्रश्न गिनने चाहिए।",
    "tīṇiyeva pañhā kātabbā": "तीन ही प्रश्न तैयार करने चाहिए",
    "purimanayena tīṇi pañhā": "पहले की विधि से तीन प्रश्न",
    "nasāsavaṃ naanidassanasappaṭighamūlassa purimanayena tīṇi pañhā.":
        f"{P('nasāsavaṃ naanidassanasappaṭighaṃ')} परिघटना के {MULA} के लिए पहले की विधि से तीन प्रश्न।",
    "naāsavasampayuttanaanidassanasappaṭighamūle tīṇiyeva.":
        f"{P('naāsavasampayutto naanidassanasappaṭigho')} परिघटना के {MULA} में तीन ही।",
    "naāsavañceva naanāsavaṃ naanidassanasappaṭighamūlepi purimanayena tīṇiyeva.":
        f"{P('naāsavañceva naanāsavaṃ naanidassanasappaṭighaṃ')} परिघटना के {MULA} में भी पहले की विधि से तीन ही।",
    "āsavaāsavasampayuttaduke pañhā na labbhati.":
        f"{DUKA['āsavaāsavasampayutta']} वाले दो के वर्गीकरण में प्रश्न लागू नहीं होते।",
    "āsavavippayuttanasāsavanaanidassanasappaṭighamūlepi purimanayeneva tīṇi pañhā.":
        f"{P('āsavavippayutto nasāsavo naanidassanasappaṭigho')} परिघटना के {MULA} में भी पहले की विधि से ही तीन प्रश्न।",
    "tīṇi pañhā.": "तीन प्रश्न।",
    "anidassanasappaṭighe tīṇiyeva.": f"{P('anidassanasappaṭigho')} परिघटना में तीन ही।",
    "cittasamuṭṭhānarūpeneva tīṇi, saṃkhittaṃ.": f"मन से उत्पन्न भौतिक रूप के साथ ही तीन, {SAMKHITTAM}।",
    "sahajātavārampi paccayavārampi nissayavārampi saṃsaṭṭhavārampi sampayuttavārampi vitthāretabbaṃ.":
        f"{SAMPAYUTTAVARA_OBL} का भी विस्तार करना चाहिए।",
    # 5-18
    "ahetukasadisaṃ, saṃkhittaṃ.": f"{P('ahetuko')} परिघटना के समान, {SAMKHITTAM}।",
    "naakusale dve, naabyākate dve. paṭhamaṃ gaṇitakena ekaṃ, dutiyaṃ gaṇitakena ekaṃ, tatiyaṃ gaṇitakena ekaṃ, sabbattha nava pañhā.":
        f"{P('naakusalo')} परिघटना में दो, {P('naabyākato')} परिघटना में दो। पहले में {GANITAKENA} एक, "
        f"दूसरे में {GANITAKENA} एक, तीसरे में {GANITAKENA} एक, हर जगह नौ प्रश्न।",
    "gaṇitakena tīṇi pañhā.": f"{GANITAKENA} तीन प्रश्न।",
    "cha pañhā kātabbā.": "छह प्रश्न तैयार करने चाहिए।",
    "akusalamūle dve, dukamūle dve.": f"{P('akusalo')} परिघटना के {MULA} में दो, दो पदों वाले {MULA} में दो।",
    "apariyāpannasadisaṃ cha pañhā": f"{P('apariyāpanno')} परिघटना के समान छह प्रश्न",
    "dutiyaṃ gaṇitakena tīṇi": f"दूसरे में {GANITAKENA} तीन",
    "dve pañhāyeva": "दो ही प्रश्न",
    "dveyeva. paṭhamaṃ gaṇitakena ekaṃ, dutiyaṃ gaṇitakena ekaṃ, tatiyaṃ gaṇitakena ekaṃ kātabbaṃ.":
        f"दो ही। पहले में {GANITAKENA} एक, दूसरे में {GANITAKENA} एक, तीसरे में {GANITAKENA} एक करना चाहिए।",
    "nahetu nanahetu ovattā, tīṇi mūlāni, ekavīsati pañhā kātabbā.":
        f"{P('nahetu ca nanahetu ca')} परिघटनाओं को उलट दिया गया है, तीन {MULA}, इक्कीस प्रश्न तैयार करने चाहिए।",
    "sahajātavārampi paṭiccavārasadisaṃ vitthāretabbaṃ.":
        "सह-उत्पत्ति के खंड का भी निर्भरता के खंड के समान विस्तार करना चाहिए।",
    # 5-19
    "akusalāneva tīṇi.": f"{P('akusalo')} परिघटनाओं में ही तीन।",
    "cattāri gaṇitakena dve dve pañhā kātabbā.": f"चार, {GANITAKENA} दो-दो प्रश्न तैयार करने चाहिए।",
    "naakusalaṃ naabyākataṃ natthi.": f"{P('naakusalaṃ naabyākataṃ')} परिघटना नहीं है।",
    "atītattikaṃ uppannattikasadisaṃ.":
        f"{TIKA['atīta']} वाला तीन का वर्गीकरण, {TIKA['uppanna']} वाले तीन के वर्गीकरण के समान है।",
    "naanidassanasappaṭighanaabyākatamūlāni sattameva, dukamūlāni sattameva, sabbaṃ ekavīsatimeva.":
        f"{P('naanidassanasappaṭigho naabyākato')} परिघटना के {MULA} सात ही, दो पदों वाले {MULA} सात ही, "
        "कुल इक्कीस ही।",
    "sahajātavārampi paccayavārampi nissayavārampi saṃsaṭṭhavārampi sampayuttavārampi pañhāvārampi vitthāretabbaṃ.":
        "सह-उत्पत्ति के खंड, कारण के खंड, आश्रय के खंड, घुले-मिले होने के खंड, जुड़ाव के खंड और प्रश्नों के खंड का भी "
        "विस्तार करना चाहिए।",
    # 5-20
    "gaṇitakena tīṇi.": f"{GANITAKENA} तीन।",
    "sabbattha saṃkhittaṃ.": f"हर जगह {SAMKHITTAM}।",
    "antimadukaṃ na labbhati.": "अंतिम दो का वर्गीकरण लागू नहीं होता।",
    "hetuhetusampayuttadukaṃ saṃkhittaṃ.": f"{DUKA['hetuhetusampayutta']} वाला दो का वर्गीकरण {SAMKHITTAM} है।",
    "yathā kusalattike pañhāvāraṃ evaṃ vitthāretabbaṃ.":
        "जैसे हितकर वाले तीन के वर्गीकरण में प्रश्नों का खंड है, वैसे ही विस्तार करना चाहिए।",
}

# whole sentences (lowercase Pāli, without the final delimiter) that are not frames
SENT = {
    "akusale tīṇi": f"{P('akusalo')} परिघटना में तीन",
    "nahetu nadukkhāya vedanāya sampayuttamūlaṃ tīṇiyeva":
        f"{P('nahetu nadukkhāya vedanāya sampayutto')} परिघटना के {MULA} में तीन ही",
    "gaṇitakena tīṇi": f"{GANITAKENA} तीन",
    "abyākataṃ anupādinnupādāniye tīṇiyeva":
        f"{P('abyākataṃ anupādinnupādāniyaṃ')} परिघटना में तीन ही",
    "nakenaci viññeyyaṃ naanidassanaappaṭighamūlassa navapañhameva":
        f"{P('nakenaci viññeyyaṃ naanidassanaappaṭighaṃ')} परिघटना के {MULA} के लिए नौ ही प्रश्न",
    "hetuyā cha pañhā": f"{R.LOC['hetu']} छह प्रश्न",
    "gaṇitakena tīṇi pañhā": f"{GANITAKENA} तीन प्रश्न",
    "cha pañhā": "छह प्रश्न",
    "nakenaci viññeyyaṃ naanidassanasappaṭighassa purimasadisaṃ navapañhaṃ kātabbaṃ":
        f"{P('nakenaci viññeyyaṃ naanidassanasappaṭighaṃ')} परिघटना के लिए पहले के समान नौ प्रश्न तैयार करने चाहिए",
    "anulomadukatikapaṭṭhānato paṭṭhāya yāva pariyosānā tiṃsamattehi bhāṇavārehi paṭṭhānaṃ":
        "सकारात्मक क्रम में दो-दो और तीन-तीन के वर्गीकरणों के कारण-संबंध से लेकर अंत तक, लगभग तीस पाठ-खंडों में "
        "कारण-संबंध",
}
CLOSING = {  # «X niṭṭhitaṃ» = «X समाप्त»
    "anulomapaccanīyapaṭṭhānaṃ": "सकारात्मक-नकारात्मक क्रम के कारण-संबंध",
    "paccanīyānulomapaṭṭhānaṃ": "नकारात्मक-सकारात्मक क्रम के कारण-संबंध",
    "paṭṭhānapakaraṇaṃ": "“कारण-संबंध” ग्रंथ",
}
for _k, _v in list(HEAD.items()):
    if _k.startswith("Dhamm"):
        CLOSING[R.lower_initials(_k)] = _v
for _k, _v in CLOSING.items():
    SENT[_k + " niṭṭhitaṃ"] = _v + " समाप्त"

VARIANTS = {"{hetuyā aṭṭha?}": "[पाठभेद: hetuyā aṭṭha?]"}

# ---------------------------------------------------------------- 5. frames

KEYS_ALT = "|".join(sorted(R.KEYS, key=len, reverse=True))
NUM_ALT = "|".join(sorted(NUM, key=len, reverse=True))
FRAME_RE = re.compile(rf"^(?P<s>.+?) dhammaṃ (?P<v>paṭicca|paccayā)(?: (?P<o>.+?)(?: (?P<n>dhammo uppajjati|"
                      rf"dhammā uppajjanti)(?: (?P<c>{R.CHAIN_RE}))?(?: (?P<num>{NUM_ALT}))?)?)?$")
FRAME_NOVERB_RE = re.compile(rf"^(?P<s>.+?) dhammaṃ (?P<v>paṭicca|paccayā) (?P<o>.+?) (?P<n>dhammo|dhammā) "
                             rf"uppajj(?:ati|anti)$")
PANHA_RE = re.compile(rf"^(?P<s>.+?) (?P<n>dhammo|dhammā) (?P<d>.+?) dhammassa (?P<neg>na )?(?P<k>{KEYS_ALT})paccayena paccayo$")
INS_RE = re.compile(rf"^(?P<neg>na )?(?P<k>{KEYS_ALT})paccayena paccayo$")

STATE = {"g": "fs"}


def frame(core):
    m = FRAME_RE.match(core)
    if m:
        s = np_sg(m.group("s"))
        h = s + (" पर निर्भर होकर" if m.group("v") == "paṭicca" else " के कारण")
        if m.group("o"):
            if m.group("n") == "dhammā uppajjanti":
                h += " " + np_pl(m.group("o"))
                verb = R.ARISES["p"]
            else:
                h += " " + np_sg(m.group("o"))
                verb = R.ARISES["s"]
            if m.group("n"):
                if m.group("c"):
                    h += " " + R.CH(m.group("c"))
                h += " " + verb
                if m.group("num"):
                    h += " " + NUM[m.group("num")]
        return h
    m = PANHA_RE.match(core)
    if m:
        if m.group("n") == "dhammā":
            s, g = np_pl(m.group("s")), "fp"
        else:
            s, g = np_sg(m.group("s")), "fs"
        STATE["g"] = g
        d = np_sg(m.group("d")) + " के लिए"
        ins = R.NINS(m.group("k"), g) if m.group("neg") else R.INS(m.group("k"), g)
        return f"{s}, {d} {ins}"
    m = INS_RE.match(core)
    if m:
        return R.NINS(m.group("k"), STATE["g"]) if m.group("neg") else R.INS(m.group("k"), STATE["g"])
    return None


FUSED_RE = re.compile(r"vipākadhammadhamm(aṃ|o|assa)(?= (?:paṭicca|paccayā|uppajj|\S+paccayena)|$)")


def piece(core):
    low = R.lower_initials(core)
    if not core.strip():
        return core
    if re.fullmatch(r"\(\d+\)", core):
        return core
    m = re.match(r"^(\(\d+\)) (.*)$", low)
    if m:
        return m.group(1) + " " + piece(m.group(2))
    if low in SENT:
        return SENT[low]
    if is_count(low):
        return count(low)
    if low.startswith("saṃsaṭṭhavāre ") and is_count(low[14:]):
        return "घुले-मिले होने के खंड में, " + count(low[14:])
    low = FUSED_RE.sub(r"vipākadhamma dhamm\1", low)
    try:
        h = frame(low)
    except KeyError as e:
        h, err = None, e
    else:
        err = None
    if h is not None:
        return h
    m = re.fullmatch(r"(.+?) (dhammaṃ|dhammo)", low)
    if m:
        return np_sg(m.group(1))
    try:
        return np_sg(low)          # a bare item phrase («Naasaṅkhataṃ…pe…»)
    except KeyError:
        pass
    # a khandha clause run on into a frame («dve khandhe paṭicca dve khandhā nakusalaṃ dhammaṃ paṭicca …»)
    ws = low.split(" ")
    for j in range(1, len(ws)):
        left, right = " ".join(ws[:j]), " ".join(ws[j:])
        try:
            h = frame(right) if " dhammaṃ " in right else None
            if h is not None:
                return R.clause(left) + " " + h
        except KeyError:
            continue
    if err is not None:
        raise err
    return R.clause(low)


SPLIT_RE = re.compile(r"(⟦\d+⟧|\.\s|\.$|…pe…|…|,\s)")


def translate_line(line):
    if line.startswith("#"):
        return heading(line)
    inserts = []
    for v, br in VARIANTS.items():
        if v in line:
            line = line.replace(" " + v, "⟪V⟫")
            inserts.append(br)
    store = []

    def keep(m):
        key = R.lower_initials(m.group(1))
        h = NOTE.get(key) or R.NOTE.get(key)
        if h is None:
            raise KeyError("note: " + m.group(1))
        store.append("(" + h + ")")
        return f"⟦{len(store) - 1}⟧"

    text = re.sub(r"\(([^()]*[^\d().][^()]*)\)", keep, line)
    out = []
    for tok in SPLIT_RE.split(text):
        if not tok:
            continue
        if tok.startswith("⟦"):
            out.append(tok)
        elif tok in (". ",):
            out.append("। ")
        elif tok == ".":
            out.append("।")
        elif tok == "…pe…":
            out.append("…")
        elif tok in ("…", ", "):
            out.append(tok)
        else:
            core = tok.strip()
            lead = tok[: len(tok) - len(tok.lstrip())]
            trail = tok[len(tok.rstrip()):]
            vmark = ""
            if core.endswith("⟪V⟫"):
                core, vmark = core[:-3], "⟪V⟫"
            out.append(lead + piece(core) + vmark + trail)
    hi = "".join(out)
    hi = re.sub(r"⟦(\d+)⟧", lambda m: store[int(m.group(1))], hi)
    for br in inserts:
        hi = hi.replace("⟪V⟫", " " + br, 1)
    return hi


# ---------------------------------------------------------------- 6. file builder

ERRORS = []


def build_file(src, dst, report=False):
    lines = open(src, encoding="utf-8").read().split("\n")
    out = []
    for n, ln in enumerate(lines, 1):
        if not ln.strip():
            if out and out[-1] != "":
                out.append("")
            continue
        m = R.ID_RE.search(ln)
        body = ln[: m.start()] if m else ln.rstrip()
        try:
            hi = translate_line(body)
        except (KeyError, AttributeError, AssertionError) as e:
            if not report:
                raise
            ERRORS.append(f"{os.path.basename(src)}:{n}: {e}")
            hi = "??"
        out.append(hi + (f" ^{m.group(1)}" if m else ""))
    while out and out[-1] == "":
        out.pop()
    if not report:
        with open(dst, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(out) + "\n")


if __name__ == "__main__":
    rep = "--report" in sys.argv
    only = [a_ for a_ in sys.argv[1:] if not a_.startswith("--")]
    for name in FILES:
        if only and not any(name.startswith(o) for o in only):
            continue
        build_file(os.path.join(R.PALI_DIR, name), os.path.join(R.OUT_DIR, name), report=rep)
    if rep:
        print("\n".join(ERRORS))
        print(len(ERRORS), "errors")
    else:
        print("built")
