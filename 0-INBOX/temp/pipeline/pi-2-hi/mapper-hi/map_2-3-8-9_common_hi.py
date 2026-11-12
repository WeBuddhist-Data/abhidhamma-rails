"""Shared table + context rules for the pi-2 Hindi maps of chapters 2, 3, 8, 9 (importing writes nothing).

    from map_2-3-8-9_common_hi import SHARED, shared_value   (via importlib, the name has hyphens)

SHARED extends PI2 (map_sample_hi, read-only) with the formulas these chapters share:
the sammappadhāna formula (pi-1 ^1-1377 wording), the lokuttara first-jhāna frame (pi-1 ^1-277),
the chanda / vīriya / samādhi / citta / paññā strings, the «upeto hoti … samannāgato» string and the
Pañhāpucchaka tika/duka labels that the sample did not need.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import PI2, pi2_value, lc  # noqa: E402

SHARED = {
    "sammā": "सही", "bhikkhu": "भिक्षु", "tena": "इसीलिए", "tattha": "यहाँ",
    # sammappadhāna formula
    "uppannānaṃ": "उत्पन्न हो चुका", "anuppannānaṃ": "उत्पन्न न हुआ", "pāpakānaṃ": "बुरा",
    "anuppādāya": "उत्पन्न न होने देना", "pahānāya": "छोड़ना", "uppādāya": "उत्पत्ति", "ṭhitiyā": "स्थिरता",
    "asammosāya": "लुप्त न होना", "vepullāya": "विपुलता", "pāripūriyā": "परिपूर्णता",
    "janeti": "जगाना", "chandaṃ": "चाह", "chandaṃ janeti": "चाह जगाना", "vāyamati": "प्रयास करना",
    "ārabhati": "जगाना", "vīriyaṃ ārabhati": "उत्साह जगाना", "paggaṇhāti": "तत्पर करना",
    "cittaṃ paggaṇhāti": "मन को तत्पर करना", "padahati": "पूरा ज़ोर लगाना",
    "kusalānaṃ": "हितकर", "kusalānaṃ dhammānaṃ": "हितकर परिघटना", "dhammānaṃ": "परिघटना",
    "akusalānaṃ dhammānaṃ": "हानिकर परिघटना",
    # chanda string
    "chanda": "चाह", "chando": "चाह", "chandikatā": "चाहना", "kattu": "करना", "kamyatā": "इच्छा",
    "kusalo": "हितकर", "kusalo dhammacchando": "हितकर परिघटना रूपी चाह", "dhamma": "परिघटना",
    # vīriya / samādhi strings
    "vīriyārambho": "उत्साह जगाना", "anikkhitta": "न छोड़ना", "dhura": "भार", "ṭhiti": "स्थिरता",
    # «upeto hoti samupeto upāgato samupāgato upapanno sampanno samannāgato»
    "upeto": "सुसज्जित", "samupeto": "भली-भाँति सुसज्जित", "upapanno": "पाया हुआ", "sampanno": "संपन्न",
    "samannāgato": "युक्त",
    # lokuttara first jhāna (pi-1 ^1-277)
    "uttaraṃ": "लोकोत्तर", "bhāveti": "अभ्यास करना", "jhānaṃ bhāveti": "ध्यान का अभ्यास करना",
    "apacayagāmiṃ": "संचय घटाने की ओर ले जाने वाला",
    "diṭṭhigatānaṃ": "दृष्टियों में फँसना", "diṭṭhigatānaṃ pahānāya": "दृष्टियों में फँसने को छोड़ना",
    "bhūmiyā": "चरण", "pattiyā": "प्राप्ति", "vivicceva": "अलग होकर", "kāmehi": "इंद्रिय-सुख",
    "vivicceva kāmehi": "इंद्रिय-सुखों से अलग होकर", "upasampajja": "प्राप्त करके",
    "upasampajja viharati": "प्राप्त करके उसमें रहना", "viharati": "रहना",
    "dukkhapaṭipadaṃ": "दुःखद प्रगति", "paṭipadaṃ": "प्रगति", "dandhābhiññaṃ": "धीमे उच्च ज्ञान वाला",
    "paṭipadaṃ dandhābhiññaṃ": "प्रगति और धीमे उच्च ज्ञान वाला", "ābhiññaṃ": "उच्च ज्ञान",
    "samaye": "उस समय",
    "sambojjhaṅgo": "जागृति का अंग", "samādhisambojjhaṅgo": "एकाग्रता नामक जागृति का अंग",
    "vīriyasambojjhaṅgo": "उत्साह नामक जागृति का अंग",
    "dhammavicayasambojjhaṅgo": "परिघटनाओं की छानबीन नामक जागृति का अंग", "maggaṅgaṃ": "मार्ग का अंग",
    "avasesā": "शेष", "avasesā dhammā": "शेष परिघटना", "dhammā": "परिघटना",
    # Pañhāpucchaka labels not in PI2
    "pahātabbā": "छोड़ा जाने वाला", "pītisahagatā": "उल्लास के साथ होने वाला", "vicāra": "सतत विचार",
    "vicārā": "सतत विचार", "vitakkā": "आरंभिक विचार", "apacayagāmino": "संचय घटाने की ओर ले जाने वाला",
    "appaṭighā": "टकराव से रहित", "anidassanaappaṭighā": "दिखाई न देने वाला और टकराव से रहित",
    "ārammaṇā": "विषय वाला", "saṃkilesikā": "क्लेशों का विषय बनने वाला",
    "sahetukā": "मूल वाला", "na hetu": "मूल रूपी न होने वाला", "cittā": "मन",
    "acetasiko": "मन का सहचर न होने वाला", "visaṃsaṭṭho": "घुला-मिला न होने वाला", "sahabhū": "साथ-साथ होने वाला",
    "vippayuttā": "अलग", "kāmāvacarā": "इंद्रिय-सुखों के लोक से संबंधित",
    "rūpāvacarā": "सूक्ष्म भौतिक लोक से संबंधित", "arūpāvacarā": "अभौतिक लोक से संबंधित",
    "āvacarā": "लोक से संबंधित",
}
SHARED_TABLE = {**PI2, **SHARED}


def shared_value(kw, kws, table, bid, text):
    """pi2_value + the context rules of these chapters."""
    k = lc(kw)
    s = set(lc(x) for x in kws)
    if k == "mano" and "mānasaṃ" in s:          # citta string «cittaṃ mano mānasaṃ» = «मन, मानस, मानसिक क्रिया» (pi-1)
        return "मानस"
    if k == "saṅkhāra" and "padhānasaṅkhāra" in s:   # member of padhānasaṅkhāra = «प्रयत्न की रचना»
        return "रचना"
    return pi2_value(kw, kws, table, bid, text)
