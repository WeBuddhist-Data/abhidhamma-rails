"""Shared strings and helpers for the Hindi rails builders of pi-2 chapters 5, 7, 10 and 11.

Imports the approved sample builder read-only (constants and emit) and adds:
- the factor synonym strings shared with pi-1 (sati, paññā, vīriya, samādhi, pīti, passaddhi, upekkhā, path factors),
- the supramundane-jhāna (lokuttara) formulas of pi-1, with the pi-2 termbase terms,
- a small translator for the Pañhāpucchaka answers (matrix triads and dyads in pi-1 rails item names).
"""
import pathlib
import re
import sys

RAILS = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-hi\rails")
sys.path.insert(0, str(RAILS))
import build_rails_sample as S  # noqa: E402  (read-only import)

PALI = S.PALI
OUT = S.OUT

# =========================================================================== frames and headings
SUTTANTA_BH = S.SUTTANTA_BH
ABHI_BH = S.ABHI_BH
PANHA = S.PANHA
DONE = S.DONE
TIKA_H = "तीन-तीन के वर्गीकरण"
DUKA_H = "दो-दो के वर्गीकरण"

# =========================================================================== lokuttara jhāna (pi-1 ^1-277, ^1-505)
LOK_HEAD = ("यहाँ भिक्षु जिस समय लोकोत्तर ध्यान का अभ्यास करता है, जो मुक्ति की ओर ले जाने वाला और संचय घटाने की ओर "
            "ले जाने वाला होता है, दृष्टियों में फँसने को छोड़ने के लिए और पहले चरण की प्राप्ति के लिए, "
            "इंद्रिय-सुखों से अलग होकर… पहले ध्यान को प्राप्त करके उसमें रहता है, जो दुःखद प्रगति और धीमे उच्च ज्ञान वाला होता है")
KUSALA_DASH = "उस समय जो संपर्क होता है… भटकाव का अभाव होता है – ये हितकर परिघटनाएँ हैं।"  # yo tasmiṃ samaye phasso hoti…pe… avikkhepo hoti – ime dhammā kusalā.
KUSALA_DOT = "उस समय संपर्क होता है… भटकाव का अभाव होता है। ये हितकर परिघटनाएँ हैं।"   # tasmiṃ samaye phasso hoti…pe… avikkhepo hoti. Ime dhammā kusalā.
VIPAKA = ("उसी लोकोत्तर हितकर ध्यान के किए जाने और अभ्यास किए जाने के कारण जिस समय वह इंद्रिय-सुखों से अलग होकर… "
          "कर्म-फल रूपी पहले ध्यान को प्राप्त करके उसमें रहता है, जो दुःखद प्रगति और धीमे उच्च ज्ञान वाला और शून्य होता है")


def lok(kind, tail):
    """kind: 'k' = kusala path only; 'v' = kusala path + resultant (dot form); 'vd' = resultant with the dash form."""
    if kind == "k":
        return f"{LOK_HEAD}, {tail}"
    kus = KUSALA_DASH if kind == "vd" else KUSALA_DOT
    vip = VIPAKA.replace(" और शून्य होता है", " होता है") if kind == "v-" else VIPAKA  # ^2-481: no suññataṃ
    return f"{LOK_HEAD}, {kus} {vip}, {tail}"


# =========================================================================== factor synonym strings (pi-1 rails, pi-2 terms)
MAGGA3 = "मार्ग का अंग, मार्ग में समाया हुआ"  # maggaṅgaṃ maggapariyāpannaṃ
SATI_FULL = ("सजगता, बार-बार स्मरण, पुनः स्मरण, सजगता, याद रखना, धारण करना, उथला न होना, भूल न जाना, "
             "सजगता, सजगता की क्षमता, सजगता का बल, सही सजगता")          # PI1 ^1-1358
SATI_PE = "सजगता, बार-बार स्मरण… सही सजगता"                             # sati anussati…pe… sammāsati
SATI_SHORT = "सजगता, बार-बार स्मरण, सही सजगता"                           # sati anussati sammāsati
PANNA_PE = "प्रज्ञा, जानना… मोह का अभाव, परिघटनाओं की छानबीन, सही दृष्टि"  # paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi
VIRIYA_FULL = ("मानसिक रूप से उत्साह जगाना, आगे बढ़ना, पराक्रम, उद्यम, प्रयास, जोश, लगन, शक्ति, स्थिरता, "
               "ढीला न पड़ने वाला पराक्रम, चाह न छोड़ना, भार न छोड़ना, भार को दृढ़ता से उठाए रखना, उत्साह, "
               "उत्साह की क्षमता, उत्साह का बल")  # PI1 ^1-22 with parakkama = पराक्रम, ṭhiti (pi-2 reading for dhiti) = स्थिरता
VIRIYA_PE = "मानसिक रूप से उत्साह जगाना… सही प्रयास"                    # cetasiko vīriyārambho…pe… sammāvāyāmo
SAMADHI_FULL = ("मन की स्थिरता, ठहराव, दृढ़ता, बिखराव का अभाव, भटकाव का अभाव, मन का न बिखरा होना, शांति, "
                "एकाग्रता की क्षमता, एकाग्रता का बल, सही एकाग्रता")    # PI1 ^1-11
SAMADHI_PE = "मन की स्थिरता… सही एकाग्रता"                             # cittassa ṭhiti…pe… sammāsamādhi
ODAGGA_VAR = "[वर्तनी-भेद (Sī.): odaggaṃ; धम्मसंगणी 9]"
PITI = f"उल्लास, आनंद, आनंदित होना, प्रमुदित होना, हर्ष, महाहर्ष, तृप्ति, उमंग {ODAGGA_VAR}, मन का खिल उठना"  # PI1 ^1-285
PASSADDHI = ("अनुभूति के समूह, पहचान के समूह, मानसिक रचनाओं के समूह और चेतना के समूह की जो प्रशांति, पूरी प्रशांति, "
             "शांत होना, पूरी तरह शांत होना, पूरी तरह शांत हो चुका होना")  # PI1 ^1-320 + viññāṇakkhandhassa
UPEKKHA = "समभाव, समभाव रखना, तटस्थ भाव से देखना, मन की तटस्थता"      # upekkhā upekkhanā ajjhupekkhanā majjhattatā cittassa
SANKAPPA_FULL = "सोचना, आरंभिक विचार, संकल्प, टिकाना, भली-भाँति टिकाना, मन को विषय की ओर ले जाना, सही संकल्प"  # PI1 ^1-283
SANKAPPA_PE = "सोचना, आरंभिक विचार… सही संकल्प"
ABSTAIN = "दूर रहना, विरत रहना, पूरी तरह विरत रहना, बचना, न करना, न अपनाना, दोष में न पड़ना, मर्यादा का उल्लंघन न करना, पुल को तोड़ देना"
VACA = f"वाणी के चार दुराचरणों से {ABSTAIN}, सही वाणी"       # PI1 ^1-299
KAMMANTA = f"शरीर के तीन दुराचरणों से {ABSTAIN}, सही कर्म"    # PI1 ^1-300
AJIVA = f"ग़लत आजीविका से {ABSTAIN}, सही आजीविका"             # PI1 ^1-301
RAGA_PE = "राग, प्रबल राग… मन का प्रबल राग"                    # rāgo sārāgo…pe… cittassa sārāgo
DOMANASSA = ("मानसिक असुहावनापन, मानसिक दुःख, मन के संपर्क से उत्पन्न असुहावना दुःखद अनुभव, "
             "मन के संपर्क से उत्पन्न असुहावनी दुःखद अनुभूति")  # PI1 ^1-415

# factor names
BOJ = {  # sambojjhaṅga names (m)
    "sati": "सजगता नामक जागृति का अंग",
    "dhammavicaya": "परिघटनाओं की छानबीन नामक जागृति का अंग",
    "viriya": "उत्साह नामक जागृति का अंग",
    "piti": "उल्लास नामक जागृति का अंग",
    "passaddhi": "प्रशांति नामक जागृति का अंग",
    "samadhi": "एकाग्रता नामक जागृति का अंग",
    "upekkha": "समभाव नामक जागृति का अंग",
}
BOJ_ORDER = ["sati", "dhammavicaya", "viriya", "piti", "passaddhi", "samadhi", "upekkha"]


def boj_obl(k):
    return BOJ[k][:-len("का अंग")] + "के अंग"


SEVEN_BOJ = "जागृति के सात अंग"
MAGGA = {  # path factors: (name, gender)
    "ditthi": ("सही दृष्टि", "f"), "sankappa": ("सही संकल्प", "m"), "vaca": ("सही वाणी", "f"),
    "kammanta": ("सही कर्म", "m"), "ajiva": ("सही आजीविका", "f"), "vayama": ("सही प्रयास", "m"),
    "sati": ("सही सजगता", "f"), "samadhi": ("सही एकाग्रता", "f"),
}
MAGGA8 = ["ditthi", "sankappa", "vaca", "kammanta", "ajiva", "vayama", "sati", "samadhi"]
MAGGA5 = ["ditthi", "sankappa", "vayama", "sati", "samadhi"]


def called(name, g, quote=True, pl=False):
    n = f"“{name}”" if quote else name
    if pl:
        return f"{n} कहे जाते हैं।" if g == "m" else f"{n} कही जाती हैं।"
    return f"{n} कहा जाता है।" if g == "m" else f"{n} कही जाती है।"


def yah_called(name, g, quote=True):
    return f"यह {called(name, g, quote)}"


# =========================================================================== Pañhāpucchaka translator
ENDINGS = ["ñcā", "ñca", "ino", "uno", "aṃ", "iṃ", "uṃ", "ī", "ū", "ā", "o", "a", "i", "u", "e", "ṃ"]


def _stem(w):
    for e in ENDINGS:
        if w.endswith(e) and len(w) > len(e) + 1:
            return w[: -len(e)]
    return w


def _prenorm(s):
    s = s.lower().replace('"', "").replace("“", "").replace("”", "")
    s = re.sub(r"(?<=ā)cā(?=ti|\b)", " cā", s)
    s = s.replace("ñceva", " ceva")
    s = re.sub(r"ñcā\b|ñca\b", " ca", s)
    return s.strip()


def key(s):
    words = [_stem(w) for w in _prenorm(s).split()]
    words = ["na" if w == "no" else w for w in words]
    return " ".join(w for w in words if w not in ("c", "ca", "cā"))


# Hindi predicate base forms (masculine singular). A tuple gives (m.sg, m.pl, f) explicitly.
PRED_SRC = {
    "kusalā": "हितकर", "akusalā": "हानिकर", "abyākatā": "नैतिक रूप से अनिर्धारित",
    "sukhāya vedanāya sampayuttā": "सुखद अनुभूति से जुड़ा",
    "dukkhāya vedanāya sampayuttā": "दुःखद अनुभूति से जुड़ा",
    "adukkhamasukhāya vedanāya sampayuttā": "न दुःखद, न सुखद अनुभूति से जुड़ा",
    "vipākā": "कर्म-फल रूपी", "vipākadhammadhammā": "कर्म-फल उत्पन्न करने वाला",
    "nevavipākanavipākadhammadhammā": "न कर्म-फल रूपी, न कर्म-फल उत्पन्न करने वाला",
    "upādinnupādāniyā": "कर्म से उत्पन्न और आसक्ति का विषय बनने वाला",
    "anupādinnupādāniyā": "कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाला",
    "anupādinnaanupādāniyā": "न कर्म से उत्पन्न, न आसक्ति का विषय बनने वाला",
    "saṃkiliṭṭhasaṃkilesikā": "क्लेशों से मलिन और क्लेशों का विषय बनने वाला",
    "asaṃkiliṭṭhasaṃkilesikā": "क्लेशों से मलिन न होने वाला, पर क्लेशों का विषय बनने वाला",
    "asaṃkiliṭṭhaasaṃkilesikā": "क्लेशों से मलिन न होने वाला और क्लेशों का विषय न बनने वाला",
    "savitakkasavicārā": "आरंभिक विचार और सतत विचार वाला",
    "avitakkavicāramattā": "आरंभिक विचार से रहित, केवल सतत विचार वाला",
    "avitakkaavicārā": "आरंभिक विचार और सतत विचार दोनों से रहित",
    "pītisahagatā": "उल्लास के साथ होने वाला", "sukhasahagatā": "सुख के साथ होने वाला",
    "upekkhāsahagatā": "समभाव के साथ होने वाला",
    "dassanena pahātabbā": "सत्य-दर्शन से छोड़ा जाने वाला",
    "bhāvanāya pahātabbā": "मानसिक अभ्यास से छोड़ा जाने वाला",
    "neva dassanena na bhāvanāya pahātabbā": "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़ा जाने वाला",
    "dassanena pahātabbahetukā": "सत्य-दर्शन से छोड़े जाने वाले मूलों वाला",
    "bhāvanāya pahātabbahetukā": "मानसिक अभ्यास से छोड़े जाने वाले मूलों वाला",
    "neva dassanena na bhāvanāya pahātabbahetukā": "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़े जाने वाले मूलों वाला",
    "ācayagāmino": "संचय की ओर ले जाने वाला", "apacayagāmino": "संचय घटाने की ओर ले जाने वाला",
    "nevācayagāmināpacayagāmino": "न संचय की ओर, न संचय घटाने की ओर ले जाने वाला",
    "sekkhā": "सीखने के चरण का", "asekkhā": "सीखना पूरा होने के चरण का",
    "nevasekkhanāsekkhā": "न सीखने के चरण का, न सीखना पूरा होने के चरण का",
    "parittā": "सीमित", "mahaggatā": "उन्नत", "appamāṇā": "अपरिमित",
    "parittārammaṇā": "सीमित विषय वाला", "mahaggatārammaṇā": "उन्नत विषय वाला",
    "appamāṇārammaṇā": "अपरिमित विषय वाला",
    "hīnā": "हीन", "majjhimā": "मध्यम", "paṇītā": "उत्तम",
    "micchattaniyatā": "ग़लत दिशा में निश्चित", "sammattaniyatā": "सही दिशा में निश्चित",
    "aniyatā": "अनिश्चित", "niyatā": "निश्चित",
    "maggārammaṇā": "मार्ग को विषय बनाने वाला", "maggahetukā": "मार्ग को मूल बनाने वाला",
    "maggādhipatino": "मार्ग की प्रधानता वाला",
    "uppannā": "उत्पन्न हो चुका", "anuppannā": "उत्पन्न न हुआ", "uppādino": "उत्पन्न होने वाला",
    "atītā": "अतीत का", "anāgatā": "भविष्य का", "paccuppannā": "वर्तमान का",
    "atītārammaṇā": "अतीत के विषय वाला", "anāgatārammaṇā": "भविष्य के विषय वाला",
    "paccuppannārammaṇā": "वर्तमान के विषय वाला",
    "ajjhattā": "स्वयं से संबंधित", "bahiddhā": "दूसरों से संबंधित",
    "ajjhattabahiddhā": "स्वयं और दूसरों दोनों से संबंधित",
    "ajjhattārammaṇā": "स्वयं से संबंधित विषय वाला", "bahiddhārammaṇā": "दूसरों से संबंधित विषय वाला",
    "ajjhattabahiddhārammaṇā": "स्वयं और दूसरों दोनों से संबंधित विषय वाला",
    "anidassanasappaṭighā": "दिखाई न देने वाला, पर टकराव वाला",
    "anidassanaappaṭighā": "दिखाई न देने वाला और टकराव से रहित",
    # dyads: roots
    "hetū": "मूल रूपी", "sahetukā": "मूल वाला", "ahetukā": "मूल से रहित",
    "hetusampayuttā": "मूलों से जुड़ा", "hetuvippayuttā": "मूलों से अलग",
    "hetū ceva sahetukā ca": "मूल रूपी भी और मूल वाला भी",
    "sahetukā ceva na ca hetū": "मूल वाला, पर स्वयं मूल रूपी न होने वाला",
    "hetū ceva hetusampayuttā ca": "मूल रूपी भी और मूलों से जुड़ा भी",
    "hetusampayuttā ceva na ca hetū": "मूलों से जुड़ा, पर स्वयं मूल रूपी न होने वाला",
    "na hetū sahetukā": "मूल रूपी न होने वाला, पर मूल वाला",
    "na hetū ahetukā": "मूल रूपी न होने वाला और मूल से रहित",
    "na hetusahetukā": "मूल रूपी न होने वाला, पर मूल वाला",
    "na hetuahetukā": "मूल रूपी न होने वाला और मूल से रहित",
    # small intermediate dyads
    "sappaccayā": "कारणों पर निर्भर रहने वाला", "saṅkhatā": "निर्मित", "anidassanā": "दिखाई न देने वाला",
    "sappaṭighā": "टकराव वाला", "appaṭighā": "टकराव से रहित", "rūpā": "भौतिक", "arūpā": "अभौतिक",
    "lokiyā": "लौकिक", "lokuttarā": "लोकोत्तर",
    "kenaci viññeyyā": "किसी एक प्रकार की चेतना से जाना जा सकने वाला",
    "kenaci na viññeyyā": "किसी एक प्रकार की चेतना से न जाना जा सकने वाला",
    # mind dyads
    "sārammaṇā": "विषय वाला", "anārammaṇā": "विषय से रहित",
    "cittā": "मन",
    "cetasikā": ("मन का सहचर", "मन के सहचर", "मन की सहचर"),
    "acetasikā": ("मन का सहचर न होने वाला", "मन के सहचर न होने वाले", "मन की सहचर न होने वाली"),
    "cittasampayuttā": "मन से जुड़ा", "cittavippayuttā": "मन से अलग",
    "cittasaṃsaṭṭhā": "मन से घुला-मिला", "cittavisaṃsaṭṭhā": "मन से घुला-मिला न होने वाला",
    "cittasamuṭṭhānā": "मन से उत्पन्न", "cittasahabhuno": "मन के साथ-साथ होने वाला",
    "cittānuparivattino": "मन का अनुसरण करने वाला",
    "cittasaṃsaṭṭhasamuṭṭhānā": "मन से घुला-मिला और मन से उत्पन्न",
    "cittasaṃsaṭṭhasamuṭṭhānasahabhuno": "मन से घुला-मिला, मन से उत्पन्न और मन के साथ-साथ होने वाला",
    "cittasaṃsaṭṭhasamuṭṭhānānuparivattino": "मन से घुला-मिला, मन से उत्पन्न और मन का अनुसरण करने वाला",
    "cittena sampayuttā": "मन से जुड़ा", "cittena vippayuttā": "मन से अलग",
    "cittena saṃsaṭṭhā": "मन से घुला-मिला", "cittena visaṃsaṭṭhā": "मन से घुला-मिला न होने वाला",
    "ajjhattikā": "आंतरिक", "bāhirā": "बाह्य", "upādā": "व्युत्पन्न",
    "upādinnā": "कर्म से उत्पन्न", "anupādinnā": "कर्म से उत्पन्न न होने वाला",
    # remaining dyads
    "savitakkā": "आरंभिक विचार वाला", "avitakkā": "आरंभिक विचार से रहित",
    "savicārā": "सतत विचार वाला", "avicārā": "सतत विचार से रहित",
    "sappītikā": "उल्लास वाला", "appītikā": "उल्लास से रहित",
    "kāmāvacarā": "इंद्रिय-सुखों के लोक से संबंधित", "rūpāvacarā": "सूक्ष्म भौतिक लोक से संबंधित",
    "arūpāvacarā": "अभौतिक लोक से संबंधित",
    "pariyāpannā": "अस्तित्व के लोकों में समाया हुआ", "apariyāpannā": "अस्तित्व के लोकों में न समाया हुआ",
    "niyyānikā": "मुक्ति की ओर ले जाने वाला", "aniyyānikā": "मुक्ति की ओर न ले जाने वाला",
    "sauttarā": "सर्वोच्च न होने वाला", "anuttarā": "सर्वोच्च",
    "saraṇā": "संघर्ष वाला", "araṇā": "संघर्ष से रहित",
    "anāsavā āsavavippayuttā": "मन के मैलों का विषय न बनने वाला और मन के मैलों से अलग",
}
# the gocchaka dyads (āsava, saṃyojana, gantha, nīvaraṇa, parāmāsa, upādāna, kilesa)
GOCCHA = {
    # pali stem: (X rūpी noun, "X-ों का विषय" object form, "X-ों से" form, pronoun for 'their')
    "āsava": ("मन के मैल रूपी", "मन के मैलों का विषय", "मन के मैलों से", "उनका"),
    "saṃyojana": ("बंधन रूपी", "बंधनों का विषय", "बंधनों से", "उनका"),
    "gantha": ("गाँठ रूपी", "गाँठों का विषय", "गाँठों से", "उनका"),
    "nīvaraṇa": ("बाधा रूपी", "बाधाओं का विषय", "बाधाओं से", "उनका"),
    "parāmāsa": ("ग़लत धारणा रूपी", "ग़लत धारणा का विषय", "ग़लत धारणा से", "उसका"),
    "upādāna": ("आसक्ति रूपी", "आसक्ति का विषय", "आसक्ति से", "उसका"),
    "kilesa": ("मन के क्लेश रूपी", "क्लेशों का विषय", "क्लेशों से", "क्लेशों का"),
}
OBJ_ADJ = {"āsava": "sāsavā", "saṃyojana": "saṃyojaniyā", "gantha": "ganthaniyā", "nīvaraṇa": "nīvaraṇiyā",
           "parāmāsa": "parāmaṭṭhā", "upādāna": "upādāniyā", "kilesa": "saṃkilesikā"}
NEG_OBJ = {"āsava": "anāsavā", "saṃyojana": "asaṃyojaniyā", "gantha": "aganthaniyā", "nīvaraṇa": "anīvaraṇiyā",
           "parāmāsa": "aparāmaṭṭhā", "upādāna": "anupādāniyā", "kilesa": "asaṃkilesikā"}
for g, (rupi, obj, se, their) in GOCCHA.items():
    pl = g[:-1] + "ā"
    o, no = OBJ_ADJ[g], NEG_OBJ[g]
    PRED_SRC[pl] = rupi
    PRED_SRC[o] = f"{obj} बनने वाला"
    PRED_SRC[no] = f"{obj} न बनने वाला"
    PRED_SRC[g + "sampayuttā"] = f"{se} जुड़ा"
    PRED_SRC[g + "vippayuttā"] = f"{se} अलग"
    PRED_SRC[f"{pl} ceva {o} ca"] = f"{rupi} भी और {obj} बनने वाला भी"
    PRED_SRC[f"{o} ceva no ca {pl}"] = f"{obj} बनने वाला, पर स्वयं {rupi} न होने वाला"
    PRED_SRC[f"{pl} ceva {g}sampayuttā ca"] = f"{rupi} भी और {se} जुड़ा भी"
    PRED_SRC[f"{g}sampayuttā ceva no ca {pl}"] = f"{se} जुड़ा, पर स्वयं {rupi} न होने वाला"
    PRED_SRC[f"{g}vippayutta{o}"] = f"{se} अलग, पर {their} विषय बनने वाला"
    PRED_SRC[f"{g}vippayutta{no}"] = f"{se} अलग और {their} विषय न बनने वाला"
PRED_SRC["oghā"] = "बाढ़ रूपी"
PRED_SRC["yogā"] = "जकड़न रूपी"
PRED_SRC["saṃkiliṭṭhā"] = "क्लेशों से मलिन"
PRED_SRC["asaṃkiliṭṭhā"] = "क्लेशों से मलिन न होने वाला"
PRED_SRC["kilesā ceva saṃkiliṭṭhā ca"] = "मन के क्लेश रूपी भी और क्लेशों से मलिन भी"
PRED_SRC["saṃkiliṭṭhā ceva no ca kilesā"] = "क्लेशों से मलिन, पर स्वयं मन के क्लेश रूपी न होने वाला"
PRED = {key(k): v for k, v in PRED_SRC.items()}

FORMS = ("ms", "mp", "fs", "fp")
_INF = {
    "mp": {"छोड़ा": "छोड़े", "जाना": "जाने", "वाला": "वाले", "हुआ": "हुए", "चुका": "चुके", "जुड़ा": "जुड़े", "घुला-मिला": "घुले-मिले", "समाया": "समाए", "का": "के"},
    "f": {"छोड़ा": "छोड़ी", "जाना": "जानी", "वाला": "वाली", "हुआ": "हुई", "चुका": "चुकी", "जुड़ा": "जुड़ी", "घुला-मिला": "घुली-मिली", "समाया": "समाई", "का": "की"},
}


def infl(h, form):
    if isinstance(h, tuple):
        return {"ms": h[0], "mp": h[1]}.get(form, h[2])
    if form == "ms":
        return h
    table = _INF["mp" if form == "mp" else "f"]
    toks = h.split(" ")
    out = []
    for i, t in enumerate(toks):
        core, comma = (t[:-1], ",") if t.endswith(",") else (t, "")
        if core in table and (core != "का" or comma or i == len(toks) - 1):
            core = table[core]
        out.append(core + comma)
    return " ".join(out)


def cop(form):
    return "हैं" if form in ("mp", "fp") else "है"


def hota(form):
    return {"ms": "होता", "mp": "होते", "fs": "होती", "fp": "होती"}[form]


def hota_neg(form):
    return {"ms": "होता", "mp": "होते", "fs": "होती", "fp": "होतीं"}[form]


NUMW = {"das": "दस", "nav": "नौ", "aṭṭh": "आठ", "satt": "सात", "pañc": "पाँच", "cattār": "चार", "tīṇ": "तीन",
        "dv": "दो", "ekādas": "ग्यारह", "dvādas": "बारह", "teras": "तेरह", "cuddas": "चौदह", "pannaras": "पंद्रह",
        "soḷas": "सोलह", "sattaras": "सत्रह", "aṭṭhāras": "अठारह", "ekavīsat": "इक्कीस"}
SING_FAC = {"domanass": "उदासी की क्षमता",
            "anaññātaññassāmīt": "“जो अब तक नहीं जाना उसे मैं जान लूँगा” की क्षमता",
            "aññ": "पूर्ण ज्ञान की क्षमता", "aññātāv": "पूर्ण ज्ञान पा चुके की क्षमता",
            "upekkh": "समभाव की क्षमता", "somanass": "प्रसन्नता की क्षमता", "jīvit": "जीवन-क्षमता",
            "man": "मन की क्षमता"}
OTHER_SUBJ = {
    "cha indriyā": ("छह क्षमताएँ", "छह क्षमताओं", "fp"),
    "pītisambojjhaṅgo": (BOJ["piti"], boj_obl("piti"), "ms"),
    "dhammavicayasambojjhaṅgo": (BOJ["dhammavicaya"], boj_obl("dhammavicaya"), "ms"),
    "cha bojjhaṅgā": ("जागृति के छह अंग", "जागृति के छह अंगों", "mp"),
    "satta maggaṅgā": ("मार्ग के सात अंग", "मार्ग के सात अंगों", "mp"),
    "sammāsaṅkappo": ("सही संकल्प", "सही संकल्प", "ms"),
    "sammādiṭṭhi": ("सही दृष्टि", "सही दृष्टि", "fs"),
}


def subject(clause):
    """Return (nom, obl, form, rest) if the clause starts with a subject, else None."""
    low = clause.lower()
    for k, v in OTHER_SUBJ.items():
        if low.startswith(k + " "):
            return v + (clause[len(k) + 1:],)
    m = re.match(r"(\w+?)indriyā (.*)$", low)
    if m and m.group(1) in NUMW:
        n = NUMW[m.group(1)]
        return (f"{n} क्षमताएँ", f"{n} क्षमताओं", "fp", clause[m.start(2):])
    m = re.match(r"(\w+?)indriyaṃ (.*)$", low)
    if m and m.group(1) in SING_FAC:
        n = SING_FAC[m.group(1)]
        return (n, n, "fs", clause[m.start(2):])
    return None


UNKNOWN = []


def pred(core, form):
    cands = [core]
    m = re.search(r"(n?ti ?pi|n?ti)$", core)
    if m:
        cands.append(core[: m.start()])
    for c in cands:
        k = key(c)
        if k in PRED:
            return infl(PRED[k], form), False
        low = _prenorm(c)
        for neg in ("na ", "no "):
            if low.startswith(neg) and key(low[3:]) in PRED:
                return infl(PRED[key(low[3:])], form), True
    UNKNOWN.append(core)
    return f"??{core}??", False


def pred_known(core):
    n = len(UNKNOWN)
    pred(core.replace('"', ""), "ms")
    if len(UNKNOWN) > n:
        del UNKNOWN[n:]
        return False
    return True


TI = re.compile(r'(?:"?n?ti ?pi|"?n?ti)$')


def _item(s):
    """Strip quotes and the quoting 'ti/tipi' of an item; return (core, had_ti)."""
    s = s.strip().rstrip(".")
    s2 = s.replace('"', "")
    if key(s2) in PRED or (s2.lower().startswith(("na ", "no ")) and key(s2[3:]) in PRED):
        return s2, False
    m = re.search(r"(n?ti ?pi|n?ti)$", s2)
    if m:
        return s2[: m.start()], True
    return s2, False


def _split_clauses(text):
    """Split a sentence part into (separator, clause) on ', ' and '…pe…'."""
    parts = re.split(r"(\s*…pe…\s*|,\s+)", text)
    out, sep = [], ""
    for p in parts:
        if re.fullmatch(r"\s*…pe…\s*|,\s+", p or ""):
            sep = "… " if "pe" in p else ", "
        elif p and p.strip():
            # 'siyā X siyā Y' without comma (never split a subject from its first 'siyā')
            toks = re.split(r"\s+(?=siyā\s)", p.strip())
            sub = [toks[0]]
            for t in toks[1:]:
                if "siyā" in sub[-1].lower().split():
                    sub.append(t)
                else:
                    sub[-1] += " " + t
            for j, s in enumerate(sub):
                out.append((sep if j == 0 else ", ", s))
            sep = ""
    return out


def _ends_ti(s):
    s = s.strip().rstrip(".")
    return bool(re.search(r'(?:n?ti ?pi|n?ti)$', s.replace('"', ""))) and not (
        key(s.replace('"', "")) in PRED)


def pq_sentence(text, default_form):
    """Translate one Pañhāpucchaka sentence (no final '.')."""
    out_parts = []
    for part in text.split(";"):
        part = part.strip()
        if not part:
            continue
        clauses = _split_clauses(part)
        # merge na vattabbā item lists
        merged = []
        i = 0
        while i < len(clauses):
            sep, c = clauses[i]
            low = c.lower()
            subj = subject(c)
            body = subj[3] if subj else c
            bl = body.lower()
            m = re.match(r"(siyā )?na vattabb\w*\s*(–\s*)?(.*)$", bl)
            if m:
                items = [body[m.start(3):]]
                j = i + 1
                while j < len(clauses) and clauses[j][0] == ", " and subject(clauses[j][1]) is None:
                    nxt = clauses[j][1]
                    if _ends_ti(nxt):
                        items.append(nxt)
                        j += 1
                    else:
                        break
                merged.append((sep, subj, "nv", (bool(m.group(1)), bool(m.group(2)), items)))
                i = j
                continue
            if not subj and re.search(r"ti ?pi$", body.replace('"', "").rstrip(".")):
                # a list of 'Xtipi, Ytipi' whose 'na vattabbā' the source leaves out
                items = [body]
                j = i + 1
                while j < len(clauses) and _ends_ti(clauses[j][1]):
                    items.append(clauses[j][1])
                    j += 1
                merged.append((sep, None, "nv", (False, False, items, "")))
                i = j
                continue
            merged.append((sep, subj, "p", body))
            i += 1
        # render
        form = default_form
        cur_subj = None
        prev_nv = False
        segs = []
        for sep, subj, kind, data in merged:
            if subj:
                cur_subj, form = subj, subj[2]
            if kind == "nv":
                siya, dash, items = data[:3]
                if len(data) == 4:
                    obj = data[3]
                elif subj:
                    obj = f"{subj[1]} को"
                else:
                    obj = "इन्हें" if form in ("mp", "fp") else "इसे"
                cores = [_item(x)[0] for x in items]
                hs = [pred(c, form)[0] for c in cores]
                lead = "कभी " if siya else ""
                obj = obj + " " if obj else ""
                if dash:
                    q = [f"“{h}”" for h in hs]
                    tail = q[0] if len(q) == 1 else ", ".join(f"न {x}" for x in q)
                    s = f"{lead}{obj}नहीं कहा जा सकता – {tail}"
                else:
                    if len(hs) == 1:
                        s = f"{lead}{obj}{hs[0]} नहीं कहा जा सकता"
                    else:
                        s = f"{lead}{obj}न {hs[0]} कहा जा सकता है, " + ", ".join(f"न {h}" for h in hs[1:])
                prev_nv = True
            else:
                body = data.strip()
                bl = body.lower()
                siya = bl.startswith("siyā ")
                core = body[5:] if siya else body
                core = _item(core)[0] if core.endswith('"') or core.replace('"', "") != core else core
                h, neg = pred(core, form)
                pron = ""
                if prev_nv and not subj:
                    pron = "ये " if form in ("mp", "fp") else "यह "
                if siya:
                    s = f"कभी {pron}{h} नहीं {hota_neg(form)}" if neg else f"कभी {pron}{h} {hota(form)} {cop(form)}"
                else:
                    s = f"{pron}{h} नहीं {cop(form)}" if neg else f"{pron}{h} {cop(form)}"
                if subj:
                    s = f"{subj[0]} {s}"
                prev_nv = False
            segs.append((sep, s))
        txt = ""
        for k, (sep, s) in enumerate(segs):
            txt += (sep if k else "") + s
        out_parts.append(txt)
    return "; ".join(out_parts)


OVERRIDE = {}


def pq_line(line, default_form):
    """Translate a full Pañhāpucchaka line: sentences end with '.', output with «।»."""
    line = line.strip()
    # ^2-223: three predicates of one 'siyā' without commas; the Hindi takes normal commas
    line = line.replace("siyā pītisahagataṃ na sukhasahagataṃ na upekkhāsahagataṃ",
                        "siyā pītisahagataṃ, na sukhasahagataṃ, na upekkhāsahagataṃ")
    sents = re.split(r"(?<=\.)\s+", line)
    out = []
    for s in sents:
        s0 = s.strip()
        if s0 in OVERRIDE:
            out.append(OVERRIDE[s0])
            continue
        body = s0[:-1] if s0.endswith(".") else s0
        if body.endswith("…pe…"):
            out.append(pq_sentence(body[:-5], default_form) + "…।")
            continue
        out.append(pq_sentence(body, default_form) + "।")
    return " ".join(out)


# =========================================================================== shared sentence pieces
ATAPI = "उद्यमी, स्पष्ट समझ रखते हुए और सजग होकर, लोक में लालच और उदासी को दूर करके"  # ātāpī sampajāno satimā vineyya loke abhijjhādomanassaṃ
FIELD = {"kaya": ("शरीर", "शरीर"), "vedana": ("अनुभूतियों", "अनुभूतियों"), "citta": ("मन", "मन"),
         "dhamma": ("परिघटनाओं", "परिघटनाओं")}


def anupassi(f, qual=""):
    """<qual> kāye kāyānupassī = <qual> शरीर में शरीर का अवलोकन करते हुए"""
    loc, gen = FIELD[f]
    q = f"{qual} " if qual else ""
    return f"{q}{loc} में {gen} का अवलोकन करते हुए"


NISSITA = {"m": "जो अलगाव पर आधारित, वैराग्य पर आधारित, अंत पर आधारित और त्याग में परिणत होने वाला है",
           "f": "जो अलगाव पर आधारित, वैराग्य पर आधारित, अंत पर आधारित और त्याग में परिणत होने वाली है"}
# vivekanissitaṃ virāganissitaṃ nirodhanissitaṃ vossaggapariṇāmiṃ


def remaining(x):
    """Avasesā dhammā X-sampayuttā = शेष परिघटनाएँ X से जुड़ी हैं"""
    return f"शेष परिघटनाएँ {x} से जुड़ी हैं"


def pali_segs(name):
    lines = (PALI / name).read_text(encoding="utf-8").splitlines()
    out = {}
    for sid, pl in S.segs_of_lines(lines):
        pl = list(pl)
        pl[-1] = re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", pl[-1])
        out[sid] = pl
    return out


# =========================================================================== writing
def emit(pali_name, hindi):
    lines = (PALI / pali_name).read_text(encoding="utf-8").splitlines()
    S.emit(lines, hindi, OUT / pali_name)


def check_unknown():
    if UNKNOWN:
        raise SystemExit("UNKNOWN predicates: " + " | ".join(UNKNOWN))
