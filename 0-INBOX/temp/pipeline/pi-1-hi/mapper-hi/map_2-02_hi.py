"""Map 2-02-cittuppadakandam keywords to the Hindi translation (CH2 + 2-02 table + context rules + overrides).

usage: python -I -X utf8 map_2-02_hi.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_hi import CH2, ch2_value, build_part, verify, lc  # noqa: E402

PART = "2-02-cittuppadakandam"

# 2-02 additions (rūpāvacara / arūpāvacara / tebhūmaka kusala). Values follow the Hindi phrase tables
# of build_2-01_2-02_hi.py as harmonised in the final translation.
T = {
    # frame: «… लोक में जन्म की ओर ले जाने वाले मार्ग का अभ्यास करता है»
    "upapattiyā": "जन्म", "maggaṃ": "मार्ग", "upapattiyā maggaṃ": "जन्म की ओर ले जाने वाला मार्ग",
    "bhāveti": "अभ्यास करना", "maggaṃ bhāveti": "मार्ग का अभ्यास करना",
    "upasampajja": "प्राप्त करके", "viharati": "रहना", "upasampajja viharati": "प्राप्त करके उसमें रहना",
    "jhānaṃ": "ध्यान", "jhānāni": "ध्यान", "catutthaṃ jhānaṃ": "चौथा ध्यान",
    "kasiṇaṃ": "ध्यान-मंडल", "pathavī": "पृथ्वी", "āpo": "जल", "tejo": "अग्नि", "vāyo": "वायु",
    "nīla": "नीला", "pīta": "पीला", "lohita": "लाल", "odāta": "सफ़ेद",
    # first absorption
    "kāmehi": "इंद्रिय-सुख", "vivicceva": "अलग होकर", "vivicceva kāmehi": "इंद्रिय-सुखों से अलग होकर",
    "akusalehi": "हानिकर", "akusalehi dhammehi": "हानिकर परिघटना",
    "vitakkaṃ": "आरंभिक विचार", "vicāraṃ": "सतत विचार", "vivekajaṃ": "अलगाव से उत्पन्न",
    # second absorption
    "vitakka": "आरंभिक विचार", "vicārānaṃ": "सतत विचार", "vicāra": "सतत विचार", "vūpasamā": "शांत होना",
    "ajjhattaṃ": "भीतरी", "sampasādanaṃ": "निर्मलता", "ekodibhāvaṃ": "एक बिंदु पर टिकना",
    "samādhijaṃ": "एकाग्रता से उत्पन्न", "tivaṅgikaṃ": "तीन अंगों वाला",
    # third absorption
    "pītiyā": "उल्लास", "virāgā": "फीका पड़ना", "upekkhako": "समभाव वाला",
    "upekkhako ca viharati": "समभाव के साथ … रहना", "sato": "सजग",
    "sampajāno": "स्पष्ट समझ रखते हुए", "sukhañca": "सुख", "kāyena": "शरीर",
    "paṭisaṃvedeti": "अनुभव करना", "ariyā": "आर्य", "ācikkhanti": "कहना",
    "duvaṅgikaṃ": "दो अंगों वाला", "duvaṅgikaṃ jhānaṃ": "दो अंगों वाला ध्यान",
    # fourth absorption
    "pahānā": "त्याग", "sukhassa": "सुख", "sukhassa ca pahānā": "सुख का त्याग", "dukkhassa": "दुःख",
    "domanassānaṃ": "उदासी", "atthaṅgamā": "मिट जाना", "pārisuddhiṃ": "पूरी तरह शुद्ध होना",
    # modes of progress
    "paṭipadā": "प्रगति का … ढंग", "paṭipadaṃ": "प्रगति", "dukkha": "दुःखद", "sukha": "सुखद",
    "dukkhapaṭipadaṃ": "दुःखद प्रगति", "sukhapaṭipadaṃ": "सुखद प्रगति",
    "abhiññaṃ": "उच्च ज्ञान", "dandha": "धीमा", "dandhābhiññaṃ": "धीमे उच्च ज्ञान वाला",
    "khippa": "शीघ्र", "khippābhiññaṃ": "शीघ्र उच्च ज्ञान वाला",
    "paṭipadaṃ dandha": "प्रगति और धीमा", "paṭipadaṃ khippa": "प्रगति और शीघ्र",
    # absorption and object (matrix paritta / appamāṇa)
    "parittaṃ": "सीमित", "paritta": "सीमित", "parittāni": "सीमित",
    "appamāṇaṃ": "अपरिमित", "appamāṇa": "अपरिमित", "appamāṇāni": "अपरिमित",
    "ārammaṇaṃ": "विषय वाला", "parittārammaṇaṃ": "सीमित विषय वाला",
    "appamāṇārammaṇaṃ": "अपरिमित विषय वाला", "ārammaṇāni": "विषय",
    # headings and colophons
    "rūpāvacara": "सूक्ष्म भौतिक लोक से संबंधित", "arūpāvacara": "अभौतिक लोक से संबंधित",
    "bhūmaka": "लोक से संबंधित",
    "catukka": "चार-चार", "catukkanayo": "चार-चार की विधि", "pañcaka": "पाँच-पाँच",
    "pañcakanayo": "पाँच-पाँच की विधि", "nayo": "विधि",
    "soḷasakkhattukaṃ": "सोलह गुना", "soḷasakkhattukāni": "सोलह गुना", "aṭṭhakkhattukaṃ": "आठ गुना",
    "abhibhāyatanāni": "विजय के आधार", "abhibhu": "विजय",
    "vimokkhāni": "मुक्ति-अवस्था", "vihāra": "विहार", "brahma": "ब्रह्म", "asubha": "असुंदरता",
    # bases of mastery
    "ajjhattaṃ arūpa": "स्वयं में भौतिक रूप … न", "rūpasaññī": "भौतिक रूप की पहचान रखना",
    "saññī": "पहचान रखना", "bahiddhā": "बाहर", "rūpāni": "दृश्य रूप",
    "abhibhuyya": "विजय पाकर", "jānāmi": "जानना", "passāmīti": "देखना",
    "suvaṇṇa": "सुंदर", "dubbaṇṇāni": "कुरूप",
    "nīlāni": "नीला", "pītāni": "पीला", "lohitakāni": "लाल", "odātāni": "सफ़ेद",
    "vaṇṇāni": "रंग वाला", "nidassanāni": "दिखने वाला", "nibhāsāni": "आभा वाला",
    # liberations
    "rūpī": "भौतिक रूप वाला", "subhanti": "सुंदर",
    # divine abidings
    "mettā": "मैत्री", "mettāsahagataṃ": "मैत्री के साथ होना", "karuṇā": "करुणा",
    "muditā": "दूसरों के सुख पर प्रसन्नता",
    # the unattractive
    "uddhumātaka": "फूली हुई लाश", "vinīlaka": "नीली पड़ चुकी लाश", "vipubbaka": "पीप से भरी लाश",
    "vicchiddaka": "बीच से कटी लाश", "vikkhāyitaka": "जानवरों द्वारा नोची गई लाश",
    "vikkhittaka": "बिखरी हुई लाश", "hata": "काटकर", "lohitaka": "खून से सनी लाश",
    "puḷavaka": "कीड़ों से भरी लाश", "aṭṭhika": "कंकाल",
    # immaterial absorptions
    "sabbaso": "पूरी तरह", "samatikkamā": "पार कर जाना", "samatikkamma": "पार करके",
    "saññānaṃ": "पहचान", "nānatta": "विविधता", "manasikārā": "मनोयोग करना",
    "ākāsa": "आकाश", "ānañca": "अनंत", "ānañcāyatana": "अनंत … क्षेत्र", "ānañcāyatanaṃ": "अनंत … क्षेत्र",
    "viññāṇañca": "अनंत चेतना", "viññāṇañcāyatanaṃ": "अनंत चेतना का क्षेत्र",
    "ākiñcañña": "कुछ भी न होना", "nāsaññā": "न अ-पहचान",
    # levels and dominant factors
    "hīnaṃ": "हीन", "majjhimaṃ": "मध्यम", "paṇītaṃ": "उत्तम", "chanda": "चाह",
    "vīmaṃsā": "जाँच-परख", "adhipateyyaṃ": "प्रधानता वाला",
}
TABLE = {**CH2, **T}

# per-segment overrides: {bid: {kw: value}}
OVERRIDES = {
    # adukkhamasukhaṃ: the fragments map to the positive parts of «न दुःखद न सुखद»
    "1-165": {"sukhaṃ": "सुखद", "dukkha": "दुःखद"},
    # «विजय के (ये) आधार»
    "1-1-2-7-0": {"āyatanāni": "आधार"},
    "1-247": {"āyatanāni": "आधार", "abhibhāyatanāni": "विजय के … आधार"},   # «विजय के ये आधार»
    # …saññāsahagataṃ here only as «… की पहचान के साथ» (no verb; no upekkhāsahagataṃ clause)
    "1-273": {"sahagataṃ": "के साथ"},
    "1-274": {"sahagataṃ": "के साथ"},
    "1-275": {"sahagataṃ": "के साथ"},
    "1-276": {"sahagataṃ": "के साथ"},
}


def resolver(bid, kw, kws):
    o = OVERRIDES.get(bid, {})
    if kw in o:
        return o[kw]
    k = lc(kw)
    s = set(lc(x) for x in kws)
    if k == "rūpa":
        if "upapattiyā" in s:
            # arūpa segments: rūpa of rūpasaññānaṃ; otherwise rūpa of rūpūpapattiyā
            return "भौतिक रूप" if "arūpa" in s else "सूक्ष्म भौतिक लोक"
        return "सूक्ष्म भौतिक"                         # heading Rūpāvacara (as 1-matika)
    if k == "arūpa":
        return "अभौतिक लोक" if "upapattiyā" in s else "अभौतिक"
    if k == "ajjhattaṃ" and "sampasādanaṃ" not in s:  # ajjhattaṃ arūpasaññī
        return "स्वयं में"
    return ch2_value(kw, kws, TABLE)


if __name__ == "__main__":
    build_part(PART, resolver)
    verify(PART)
