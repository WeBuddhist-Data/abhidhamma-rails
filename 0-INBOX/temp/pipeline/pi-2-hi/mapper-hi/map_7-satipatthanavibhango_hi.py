"""pi-2 ch. 7 (Satipaṭṭhānavibhaṅga) Pāli->Hindi keyword map.  usage: python -I -X utf8 map_7-satipatthanavibhango_hi.py

Imports map_sample_hi (read-only). Table T extends PI2; OVR holds per-segment exceptions.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import PI2, PP_SEGMENTS, NDE, pi2_value, build_part, verify, read_hindi  # noqa: E402

CH = "7-satipatthanavibhango"
PP_SEGMENTS.update({"2-388", "2-389"})

T = {
    # headings
    "satipaṭṭhāna": "सजगता का आधार", "paṭṭhāna": "आधार", "satipaṭṭhānavibhaṅgo": "सजगता के आधारों का विश्लेषण",
    "satipaṭṭhānā": "सजगता … आधार", "paṭṭhānā": "आधार",          # «सजगता के चार आधार»
    "satipaṭṭhānaṃ": "सजगता का आधार", "paṭṭhānaṃ": "आधार",
    "satipaṭṭhānānaṃ": "सजगता … आधार", "paṭṭhānānaṃ": "आधार",
    "ānupassanā": "अवलोकन", "anupassanā": "अवलोकन", "niddeso": "व्याख्या", "ānupassanāniddeso": "अवलोकन की व्याख्या",
    "kāyānupassanā": "शरीर का अवलोकन", "kāyānupassanāniddeso": "शरीर के अवलोकन की व्याख्या",
    "vedanānupassanā": "अनुभूतियों का अवलोकन", "vedanānupassanāniddeso": "अनुभूतियों के अवलोकन की व्याख्या",
    "cittānupassanā": "मन का अवलोकन", "cittānupassanāniddeso": "मन के अवलोकन की व्याख्या",
    "dhammānupassanā": "परिघटनाओं का अवलोकन", "dhammānupassanāniddeso": "परिघटनाओं के अवलोकन की व्याख्या",
    # the formula (2-355)
    "bhikkhu": "भिक्षु", "kāye": "शरीर", "vedanāsu": "अनुभूति", "citte": "मन", "dhammesu": "परिघटना",
    "ajjhattaṃ": "स्वयं से संबंधित", "bahiddhā": "दूसरों से संबंधित",
    "ajjhattabahiddhā": "स्वयं और दूसरों दोनों से संबंधित",
    "ānupassī": "अवलोकन करते हुए", "anupassī": "अवलोकन करते हुए",
    "kāyānupassī": "शरीर का अवलोकन करते हुए", "vedanānupassī": "अनुभूतियों का अवलोकन करते हुए",
    "cittānupassī": "मन का अवलोकन करते हुए", "dhammānupassī": "परिघटनाओं का अवलोकन करते हुए",
    "kāyānupassī viharati": "शरीर का अवलोकन करते हुए रहना",
    "vedanānupassī viharati": "अनुभूतियों का अवलोकन करते हुए रहना",
    "cittānupassī viharati": "मन का अवलोकन करते हुए रहना",
    "dhammānupassī viharati": "परिघटनाओं का अवलोकन करते हुए रहना",
    "vedanāsu vedanānupassī": "अनुभूतियों में अनुभूतियों का अवलोकन करते हुए",
    "ajjhattaṃ kāye": "स्वयं से संबंधित शरीर", "bahiddhā kāye": "दूसरों से संबंधित शरीर",
    "ajjhattabahiddhā kāye": "स्वयं और दूसरों दोनों से संबंधित शरीर",
    "ajjhattaṃ vedanāsu": "स्वयं से संबंधित अनुभूति", "bahiddhā vedanāsu": "दूसरों से संबंधित अनुभूति",
    "ajjhattabahiddhā vedanāsu": "स्वयं और दूसरों दोनों से संबंधित अनुभूति",
    "ajjhattaṃ citte": "स्वयं से संबंधित मन", "bahiddhā citte": "दूसरों से संबंधित मन",
    "ajjhattabahiddhā citte": "स्वयं और दूसरों दोनों से संबंधित मन",
    "bahiddhā dhammesu": "दूसरों से संबंधित परिघटना",    "viharati": "रहना", "viharatīti": "रहना", "ātāpī": "उद्यमी", "sampajāno": "स्पष्ट समझ रखते हुए", "satimā": "सजग",
    "vineyya": "दूर करके", "loke": "लोक", "abhijjhā": "लालच", "domanassaṃ": "उदासी",
    "abhijjhādomanassaṃ": "लालच और उदासी", "abhijjhādomanassa": "लालच और उदासी",
    "loke abhijjhādomanassaṃ": "लोक में लालच और उदासी", "loke abhijjhādomanassa": "लोक में लालच और उदासी",
    # body parts (2-356)
    "pāda": "पैर", "talā": "तलवा", "kesamatthakā": "सिर के बालों का सिरा", "matthakā": "सिरा",
    "pariyantaṃ": "घिरा", "pakārassa": "प्रकार", "asucino": "अशुद्धि", "paccavekkhati": "जाँचना",
    "atthissa": "उसके … हैं", "kāye kesā": "शरीर में सिर के बाल",
    "kesā": "सिर के बाल", "lomā": "रोएँ", "nakhā": "नाखून", "dantā": "दाँत", "taco": "त्वचा", "maṃsaṃ": "मांस",
    "nhāru": "नसें", "aṭṭhi": "हड्डी", "miñjaṃ": "मज्जा", "vakkaṃ": "गुर्दा", "hadayaṃ": "हृदय", "yakanaṃ": "यकृत",
    "kilomakaṃ": "झिल्ली", "pihakaṃ": "तिल्ली", "papphāsaṃ": "फेफड़ा", "antaṃ": "आँत",
    "antaguṇaṃ": "आँतों की मेखला", "udariyaṃ": "पेट का भोजन", "karīsaṃ": "मल", "pittaṃ": "पित्त",
    "semhaṃ": "कफ", "pubbo": "पीब", "lohitaṃ": "रक्त", "sedo": "पसीना", "medo": "चर्बी", "assu": "आँसू",
    "vasā": "वसा", "kheḷo": "लार", "siṅghāṇikā": "नाक का मैल", "lasikā": "जोड़ों का तरल", "mutta": "मूत्र",
    "nimittaṃ": "चिह्न", "āsevati": "सेवन करना", "taṃ nimittaṃ āsevati": "उस चिह्न का सेवन करना",
    "āsevitvā": "सेवन करके", "taṃ nimittaṃ āsevitvā": "उस चिह्न का सेवन करके",
    "bhāveti": "अभ्यास करना", "bhāvetvā": "अभ्यास करके", "bahulīkaroti": "बार-बार करना",
    "bahulīkaritvā": "बार-बार करके", "vavatthapeti": "भली-भाँति निर्धारित करना",
    "vavatthapetvā": "भली-भाँति निर्धारित करके", "upasaṃharati": "ले जाना", "cittaṃ upasaṃharati": "मन को ले जाना",
    # the word explanations (2-357 … 2-362)
    "tena": "इसीलिए", "upeto": "सुसज्जित", "samupeto": "भली-भाँति सुसज्जित", "upapanno": "पाया हुआ",
    "sampanno": "संपन्न", "samannāgato": "युक्त",
    "sammā": "सही", "paññā": "प्रज्ञा", "pajānanā": "जानना", "amoho": "मोह का अभाव", "vicayo": "छानबीन",
    "dhammavicayo": "परिघटनाओं की छानबीन", "dhamma": "परिघटना", "diṭṭhi": "दृष्टि",
    "iriyati": "चलना-फिरना", "vattati": "आचरण करना", "pāleti": "स्वयं को बनाए रखना", "yapeti": "निभाना",
    "yāpeti": "जीवन चलाना", "carati": "विचरना",
    "ātāpo": "उद्यमशीलता", "cetasiko": "मानसिक", "vīriyārambho": "उत्साह जगाना",
    "cetasiko vīriyārambho": "मानसिक रूप से उत्साह जगाना", "ārambho": "जगाना", "vāyāmo": "प्रयास",
    "sampajaññaṃ": "स्पष्ट समझ", "sati": "सजगता", "anussati": "बार-बार स्मरण",
    "kāyo": "शरीर", "khandhā": "समूह", "upādāna": "आसक्ति", "rāgo": "राग", "sārāgo": "प्रबल राग", "cittassa": "मन",
    "paṭivinītā": "पूरी तरह दूर कर दिए गए", "santā": "शांत", "samitā": "शमित", "vūpasantā": "पूरी तरह शांत",
    "atthaṅgatā": "अस्त", "abbhatthaṅgatā": "पूरी तरह अस्त", "appitā": "समाप्त", "byappitā": "पूरी तरह समाप्त",
    "sositā": "सुखा दिए गए", "visositā": "पूरी तरह सुखा दिए गए", "byantīkatā": "मिटा दिए गए",
    "cetasikaṃ": "मानसिक", "cetasikaṃ asātaṃ": "मानसिक असुहावनापन", "cetasikaṃ dukkhaṃ": "मानसिक दुःख",
    "cetosamphassa": "मन का संपर्क", "dukkhaṃ": "दुःख", "dukkhaṃ vedayitaṃ": "दुःखद अनुभव",
    "asātaṃ dukkhaṃ": "असुहावना दुःखद", "asātaṃ dukkhaṃ vedayitaṃ": "असुहावना दुःखद अनुभव",
    "asātā dukkhā vedanā": "असुहावनी दुःखद अनुभूति",
    # vedanā / citta / dhamma (2-363 … 2-367)
    "vedayamāno": "अनुभव करते हुए", "vedayāmī": "अनुभव करना", "vedayatī": "अनुभव करना", "pajānāti": "जानना",
    "sukhaṃ": "सुखद", "sukhaṃ vedanaṃ": "सुखद अनुभूति", "dukkhaṃ vedanaṃ": "दुःखद अनुभूति",
    "sāmisaṃ": "सांसारिक भोग से जुड़ा", "nirāmisaṃ": "सांसारिक भोग से रहित",
    "sāmisaṃ sukhaṃ": "सांसारिक भोग से जुड़ा सुखद", "sāmisaṃ dukkhaṃ": "सांसारिक भोग से जुड़ा दुःखद",
    "nirāmisaṃ sukhaṃ": "सांसारिक भोग से रहित सुखद", "nirāmisaṃ dukkhaṃ": "सांसारिक भोग से रहित दुःखद",
    "sāmisaṃ sukhaṃ vedanaṃ": "सांसारिक भोग से जुड़ी सुखद अनुभूति",
    "sāmisaṃ dukkhaṃ vedanaṃ": "सांसारिक भोग से जुड़ी दुःखद अनुभूति",
    "nirāmisaṃ sukhaṃ vedanaṃ": "सांसारिक भोग से रहित सुखद अनुभूति",
    "nirāmisaṃ dukkhaṃ vedanaṃ": "सांसारिक भोग से रहित दुःखद अनुभूति",
    "vedanāsu cittaṃ": "अनुभूति पर मन",
    "rāgaṃ": "राग", "dosaṃ": "द्वेष", "mohaṃ": "मोह",
    "sarāgaṃ vā cittaṃ": "मन राग-युक्त", "vītarāgaṃ vā cittaṃ": "मन राग से मुक्त",
    "sadosaṃ vā cittaṃ": "मन द्वेष-युक्त", "vītadosaṃ vā cittaṃ": "मन द्वेष से मुक्त",
    "samohaṃ vā cittaṃ": "मन मोह-युक्त", "vītamohaṃ vā cittaṃ": "मन मोह से मुक्त",
    "saṃkhittaṃ": "सिमटा हुआ", "saṃkhittaṃ vā cittaṃ": "मन सिमटा हुआ",
    "vikkhittaṃ": "बिखरा हुआ", "vikkhittaṃ vā cittaṃ": "मन बिखरा हुआ",
    "mahaggataṃ": "उन्नत", "mahaggataṃ vā cittaṃ": "मन उन्नत",
    "amahaggataṃ": "उन्नत न होने वाला", "amahaggataṃ vā cittaṃ": "मन उन्नत न होने वाला",
    "sauttaraṃ": "सर्वोच्च न होने वाला", "sauttaraṃ vā cittaṃ": "मन सर्वोच्च न होने वाला",
    "anuttaraṃ": "सर्वोच्च", "anuttaraṃ vā cittaṃ": "मन सर्वोच्च",
    "samāhitaṃ": "एकाग्र", "samāhitaṃ vā cittaṃ": "मन एकाग्र",
    "asamāhitaṃ": "एकाग्रता से रहित", "asamāhitaṃ vā cittaṃ": "मन एकाग्रता से रहित",
    "vimuttaṃ": "मुक्त", "vimuttaṃ vā cittaṃ": "मन मुक्त", "avimuttaṃ": "अमुक्त", "avimuttaṃ vā cittaṃ": "मन अमुक्त",
    "santaṃ": "होना", "kāma": "इंद्रिय-सुख", "chandaṃ": "चाह", "kāmacchandaṃ": "इंद्रिय-सुखों की चाह",
    "uppādo": "उत्पन्न होना", "anuppādo": "उत्पन्न नहीं होना",
    "kāmacchandassa uppādo": "इंद्रिय-सुखों की चाह उत्पन्न होना",
    "anuppannassa": "उत्पन्न न हुआ", "uppannassa": "उत्पन्न हो चुका", "pahīnassa": "छोड़ा जा चुका",
    "anuppannassa kāmacchandassa": "उत्पन्न न हुई इंद्रिय-सुखों की चाह",
    "uppannassa kāmacchandassa": "उत्पन्न हो चुकी इंद्रिय-सुखों की चाह",
    "pahīnassa kāmacchandassa": "छोड़ी जा चुकी इंद्रिय-सुखों की चाह",
    "vicikicchaṃ": "संशय", "vicikicchāya uppādo": "संशय उत्पन्न होना",
    "anuppannāya vicikicchāya": "उत्पन्न न हुआ संशय", "uppannāya vicikicchāya": "उत्पन्न हो चुका संशय",
    "pahīnāya vicikicchāya": "छोड़ा जा चुका संशय",
    "anuppannāya vicikicchāya uppādo": "उत्पन्न न हुआ संशय उत्पन्न होना",
    "byāpādaṃ": "दुर्भावना", "thina": "आलस्य", "middhaṃ": "तंद्रा", "thinamiddhaṃ": "आलस्य और तंद्रा",
    "uddhacca": "बेचैनी", "kukkuccaṃ": "पछतावा", "uddhaccakukkuccaṃ": "बेचैनी और पछतावा",
    "sambojjhaṅgaṃ": "जागृति का अंग", "satisambojjhaṅgaṃ": "सजगता नामक जागृति का अंग",
    "dhammavicayasambojjhaṅgaṃ": "परिघटनाओं की छानबीन नामक जागृति का अंग",
    "dhammavicaya": "परिघटनाओं की छानबीन", "vicaya": "छानबीन",
    "vīriyasambojjhaṅgaṃ": "उत्साह नामक जागृति का अंग", "pītisambojjhaṅgaṃ": "उल्लास नामक जागृति का अंग",
    "passaddhisambojjhaṅgaṃ": "प्रशांति नामक जागृति का अंग", "passaddhi": "प्रशांति",
    "samādhisambojjhaṅgaṃ": "एकाग्रता नामक जागृति का अंग", "samādhi": "एकाग्रता",
    "upekkhāsambojjhaṅgaṃ": "समभाव नामक जागृति का अंग",
    "upekkhāsambojjhaṅgassa uppādo": "समभाव नामक जागृति का अंग उत्पन्न होना",
    "satisambojjhaṅgassa uppādo": "सजगता नामक जागृति का अंग उत्पन्न होना",
    "uppannassa satisambojjhaṅgassa": "उत्पन्न हो चुका सजगता नामक जागृति का अंग",
    "anuppannassa satisambojjhaṅgassa": "उत्पन्न न हुआ सजगता नामक जागृति का अंग",
    "satisambojjhaṅgassa bhāvanāya pāripūrī": "सजगता नामक जागृति के अंग का अभ्यास परिपूर्ण होना",
    "pāripūrī": "परिपूर्ण होना",
    # Abhidhammabhājanīya (2-375 … 2-385)
    "dhammā": "परिघटना", "avasesā": "शेष", "avasesā dhammā": "शेष परिघटना", "sampayuttā": "जुड़ा",
    "sambojjhaṅgo": "जागृति का अंग", "satisambojjhaṅgo": "सजगता नामक जागृति का अंग", "maggaṅgaṃ": "मार्ग का अंग",
    "samaye": "उस समय", "uttaraṃ": "लोकोत्तर", "jhānaṃ": "ध्यान", "jhānaṃ bhāveti": "ध्यान का अभ्यास करना",
    "apacayagāmiṃ": "संचय घटाने की ओर ले जाने वाला", "diṭṭhigatānaṃ": "दृष्टियों में फँसना",
    "pahānāya": "छोड़ना", "diṭṭhigatānaṃ pahānāya": "दृष्टियों में फँसने को छोड़ना", "pattiyā": "प्राप्ति",
    "bhūmiyā": "चरण", "kāmehi": "इंद्रिय-सुख", "vivicceva": "अलग होकर",
    "vivicceva kāmehi": "इंद्रिय-सुखों से अलग होकर", "upasampajja": "प्राप्त करके",
    "upasampajja viharati": "प्राप्त करके उसमें रहना", "dukkhapaṭipadaṃ": "दुःखद प्रगति", "paṭipadaṃ": "प्रगति",
    "ābhiññaṃ": "उच्च ज्ञान", "dandhābhiññaṃ": "धीमे उच्च ज्ञान वाला",
    "paṭipadaṃ dandhābhiññaṃ": "प्रगति और धीमे उच्च ज्ञान वाला",
    "katattā": "किया जाना", "bhāvitattā": "अभ्यास किया जाना", "suññataṃ": "शून्य",
    "kusalassa jhānassa": "हितकर ध्यान",
    # Pañhāpucchaka
    "pahātabbā": "छोड़ा जाने वाला", "hetukā": "मूलों वाला", "sahetukā": "मूल वाला",
    "saṃkilesikā": "क्लेशों का विषय बनने वाला", "vicāra": "सतत विचार", "vicārā": "सतत विचार",
    "vitakkā": "आरंभिक विचार", "pītisahagatā": "उल्लास के साथ होने वाला",
    "anidassanaappaṭighā": "दिखाई न देने वाला और टकराव से रहित", "appaṭighā": "टकराव से रहित",
    "apacayagāmino": "संचय घटाने की ओर ले जाने वाला", "paṇītā": "उत्तम", "aniyatā": "अनिश्चित",
    "ārammaṇā": "विषय वाला", "vippayuttā": "अलग", "cittā": "मन", "kāmāvacarā": "इंद्रिय-सुखों के लोक से संबंधित",
    "rūpāvacarā": "सूक्ष्म भौतिक लोक से संबंधित", "arūpāvacarā": "अभौतिक लोक से संबंधित",
    "āvacarā": "लोक से संबंधित",
}
TABLE = {**PI2, **T}

OVR = {}
# Abhidhammabhājanīya: «… में … का अवलोकन करता है» (verb), the question «… का अवलोकन करते हुए कैसे रहता है»
for _b in ("2-375", "2-376", "2-377", "2-378", "2-379", "2-381", "2-382", "2-383", "2-384"):
    _o = OVR.setdefault(_b, {})
    _o["ānupassī"] = "अवलोकन करना"
    for _p, _h in (("kāyā", "शरीर"), ("vedanā", "अनुभूतियों"), ("cittā", "मन"), ("dhammā", "परिघटनाओं")):
        _o[_p + "nupassī"] = f"{_h} का अवलोकन करना"
        _o[_p + "nupassī viharati"] = f"{_h} का अवलोकन करते हुए … रहना"
OVR.update({    "2-363": {"sukhaṃ": "सुखद", "dukkhaṃ": "दुःखद"},
    "2-388": {"uppannā": "उत्पन्न हो चुका",               # matrix label (siyā uppannā)
              "dhammā": NDE},                              # fragment of vipākadhammadhammā, no noun in the Hindi
})
ALLOWED = {}
for _b in ("2-381", "2-382", "2-383", "2-384", "2-385"):
    ALLOWED[(_b, "katattā")] = "text «किए जाने»: किया ~ किए is regular inflection the checker does not model (pi-1 value)"
    ALLOWED[(_b, "bhāvitattā")] = "text «अभ्यास किए जाने»: किया ~ किए (pi-1 value)"
_HI = {}


def resolver(bid, kw, kws):
    if not _HI:
        _HI.update(read_hindi(CH))
    o = OVR.get(bid, {})
    if kw in o:
        return o[kw]
    return pi2_value(kw, kws, TABLE, bid, _HI.get(bid))


if __name__ == "__main__":
    build_part(CH, resolver)
    verify(CH, allowed=ALLOWED)
