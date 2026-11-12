"""pi-2 ch. 15 (Paṭisambhidāvibhaṅga) Pāli->Hindi keyword map.  usage: python -I -X utf8 map_15-patisambhidavibhango_hi.py

Imports map_sample_hi (read-only). Table T extends PI2; OVR holds per-segment exceptions.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import PI2, PP_SEGMENTS, NDE, pi2_value, build_part, verify, read_hindi  # noqa: E402

CH = "15-patisambhidavibhango"
PP_SEGMENTS.update({"2-749", "2-750"})

# --- the four analytical knowledges (builder PS table) and the vāra headings
T = {
    "paṭisambhidā": "विश्लेषणात्मक ज्ञान", "paṭisambhidānaṃ": "विश्लेषणात्मक ज्ञान",
    "atthapaṭisambhidā": "अर्थ का विश्लेषणात्मक ज्ञान",
    "dhammapaṭisambhidā": "परिघटनाओं का विश्लेषणात्मक ज्ञान",
    "niruttipaṭisambhidā": "भाषा का विश्लेषणात्मक ज्ञान",
    "paṭibhānapaṭisambhidā": "सूझ-बूझ का विश्लेषणात्मक ज्ञान",
    "attha": "अर्थ", "atthe": "अर्थ", "atthaṃ": "अर्थ", "dhamma": "परिघटना", "dhamme": "परिघटना",
    "dhammā": "परिघटना", "nirutti": "भाषा", "niruttiyā": "भाषा", "paṭibhāna": "सूझ-बूझ",
    "paṭisambhidā aniyatā": "विश्लेषणात्मक ज्ञान अनिश्चित",
    "ñāṇaṃ": "ज्ञान", "ñāṇesu": "ज्ञान", "ñāṇa": "ज्ञान",
    "ābhilāpe": "अभिव्यक्ति",                              # dhammaniruttābhilāpe «परिघटनाओं की भाषा की अभिव्यक्ति»
    "jānāti": "जानना", "jotakānī": "प्रकाशित करने वाला",
    "idamatthajotakānī": "इस अर्थ को प्रकाशित करने वाला",
    "ñāṇāni idamatthajotakānī": "ज्ञान इस अर्थ को प्रकाशित करने वाला",
    "paññatti": "नामकरण", "dhammānaṃ paññatti": "परिघटनाओं का नामकरण",
    "vāro": "खंड", "saṅgaha": "सारांश", "saṅgahavāro": "सारांश का खंड", "sacca": "सत्य",
    "saccavāro": "सत्यों का खंड", "dhammavāro": "परिघटनाओं का खंड", "samuppāda": "उत्पत्ति",
    "samuppādavāro": "उत्पत्ति का खंड", "pariyatti": "शिक्षा का अध्ययन",
    "pariyattivāro": "शिक्षा के अध्ययन का खंड", "akusala": "हानिकर", "kiriya": "केवल क्रिया",
    "paṭicca": "परस्पर-आश्रित",
    # Suttanta vāras
    "dukkhe": "दुःख", "samudaye": "उत्पत्ति", "dukkhasamudaye": "दुःख की उत्पत्ति", "nirodhe": "अंत",
    "dukkhanirodhe": "दुःख का अंत", "hetumhi": "कारण", "phale": "फल",
    "jātā": "जन्मा हुआ", "sañjātā": "भली-भाँति जन्मा", "nibbattā": "पैदा हुआ", "pātubhūtā": "प्रकट हुआ",
    "ye": "जो",
    "jarā": "बुढ़ापा", "maraṇe": "मृत्यु", "jarāmaraṇe": "बुढ़ापा और मृत्यु",
    "jarāmaraṇe ñāṇaṃ": "बुढ़ापे और मृत्यु का ज्ञान", "jarāmaraṇanirodhe": "बुढ़ापे और मृत्यु का अंत",
    "jātiyā": "जन्म", "bhave": "अस्तित्व", "upādāne": "आसक्ति", "taṇhāya": "तृष्णा", "vedanāya": "अनुभूति",
    "phasse": "संपर्क", "āyatane": "इंद्रिय-क्षेत्र", "nāma": "मानसिक पक्ष", "rūpe": "भौतिक रूप",
    "nāmarūpe": "मानसिक पक्ष और भौतिक रूप", "viññāṇe": "चेतना", "viññāṇe ñāṇaṃ": "चेतना का ज्ञान",
    "saṅkhāresu": "मानसिक रचनाएँ", "saṅkhāresu ñāṇaṃ": "मानसिक रचनाओं का ज्ञान",
    "saṅkhāranirodhe": "मानसिक रचनाओं का अंत",
    # pariyattivāra (navaṅga, pi-4 wording)
    "bhikkhu": "भिक्षु", "dhammaṃ": "शिक्षा", "suttaṃ": "उपदेश", "geyyaṃ": "गद्य-पद्य मिश्रित उपदेश",
    "veyyākaraṇaṃ": "व्याख्याएँ", "gāthaṃ": "पद्य", "udānaṃ": "प्रेरित उद्गार", "itivuttakaṃ": "उद्धृत वचन",
    "jātakaṃ": "पूर्व जन्मों की कथाएँ", "abbhutadhammaṃ": "अद्भुत घटनाओं के वर्णन", "abbhuta": "अद्भुत",
    "vedallaṃ": "प्रश्नोत्तर", "bhāsitassa": "कथन",
    # Abhidhammabhājanīya (pi-1 cittuppāda wording; here the Hindi has «… के साथ होने वाला»)
    "sahagataṃ": "के साथ होने वाला", "somanassasahagataṃ": "प्रसन्नता के साथ होने वाला",
    "somanassasahagatā": "प्रसन्नता के साथ होने वाला", "upekkhāsahagataṃ": "समभाव के साथ होने वाला",
    "sukhasahagataṃ": "सुख के साथ होने वाला", "sasaṅkhārena": "प्रेरणा सहित",
    "ñāṇavippayuttā": "ज्ञान से अलग", "diṭṭhigata": "ग़लत दृष्टि", "paṭigha": "चिढ़", "vicikicchā": "संशय",
    "uddhacca": "बेचैनी", "domanassa": "उदासी",
    "rūpārammaṇaṃ": "विषय दृश्य रूप", "saddārammaṇaṃ": "विषय ध्वनि", "gandhārammaṇaṃ": "विषय गंध",
    "rasārammaṇaṃ": "विषय स्वाद", "phoṭṭhabbārammaṇaṃ": "विषय स्पर्श", "rūpārammaṇā": "विषय दृश्य रूप",
    "phoṭṭhabbārammaṇā": "विषय … स्पर्श",
    "dhammārammaṇaṃ": "मन का विषय", "dhammārammaṇā": "मन का विषय", "ārammaṇā": "विषय वाला",
    "dhammā akusalā": "हानिकर परिघटना", "dhammā abyākatā": "नैतिक रूप से अनिर्धारित परिघटना",
    "akusalaṃ cittaṃ": "हानिकर मन",
    "kāmāvacarassa": "इंद्रिय-सुखों के लोक से संबंधित", "kusalassa": "हितकर", "akusalassa": "हानिकर",
    "kāmāvacarassa kusalassa": "इंद्रिय-सुखों के लोक से संबंधित हितकर", "kusalassa kammassa": "हितकर कर्म",
    "katattā": "किया जाना", "upacitattā": "संचित होना", "bhāvitattā": "अभ्यास किया जाना",
    "vipākaṃ": "कर्म के फल रूपी", "vipākā": "कर्म के फल रूपी",
    "dhātu uppannā": "तत्व उत्पन्न", "ye vā pana": "या … जो भी", "dukkhaṃ": "दुःख",
    "kiriyā": "केवल क्रिया रूपी", "ākusalā": "हानिकर", "neva kusalā nākusalā": "न हितकर न हानिकर",
    # jhāna strings (pi-1)
    "bhāveti": "अभ्यास करना", "maggaṃ bhāveti": "मार्ग का अभ्यास करना", "jhānaṃ bhāveti": "ध्यान का अभ्यास करना",
    "maggaṃ": "मार्ग", "kasiṇaṃ": "ध्यान-मंडल", "pathavīkasiṇaṃ": "पृथ्वी का ध्यान-मंडल", "viharati": "रहना",
    "upasampajja": "प्राप्त करके", "upasampajja viharati": "प्राप्त करके उसमें रहना",
    "kāmehi": "इंद्रिय-सुख", "vivicceva": "अलग होकर", "vivicceva kāmehi": "इंद्रिय-सुखों से अलग होकर",
    "ūpapattiyā": "जन्म", "rūpūpapattiyā": "सूक्ष्म भौतिक लोक में जन्म",
    "rūpūpapattiyā maggaṃ": "सूक्ष्म भौतिक लोक में जन्म की ओर ले जाने वाला मार्ग",
    "arūpūpapattiyā": "अभौतिक लोक में जन्म",
    "arūpūpapattiyā maggaṃ": "अभौतिक लोक में जन्म की ओर ले जाने वाला मार्ग",
    "pahānā": "छोड़ना", "sukhassa": "सुख", "sukhassa ca pahānā": "सुख को छोड़ना",
    "samatikkamma": "पार करके", "sabbaso": "पूरी तरह", "ākiñcaññāyatanaṃ": "कुछ भी न होने का क्षेत्र",
    "nevasaññānāsaññāyatanasaññāsahagataṃ": "न पहचान न अ-पहचान के क्षेत्र की पहचान के साथ होने वाला",
    "catutthaṃ jhānaṃ": "चौथा ध्यान",
    "pahānāya": "छोड़ना", "diṭṭhigatānaṃ": "दृष्टियों में फँसना",
    "diṭṭhigatānaṃ pahānāya": "दृष्टियों में फँसने को छोड़ना", "uttaraṃ": "लोकोत्तर",
    "dukkhapaṭipadaṃ": "दुःखद प्रगति", "paṭipadaṃ": "प्रगति", "ābhiññaṃ": "उच्च ज्ञान",
    "dandhābhiññaṃ": "धीमे उच्च ज्ञान वाला",
    "dukkhapaṭipadaṃ dandhābhiññaṃ": "दुःखद प्रगति और धीमे उच्च ज्ञान वाला",
    "apacayagāmiṃ": "संचय घटाने की ओर ले जाने वाला", "pattiyā": "प्राप्ति", "bhūmiyā": "चरण",
    "rūpāvacarassa": "सूक्ष्म भौतिक लोक से संबंधित", "arūpāvacarassa": "अभौतिक लोक से संबंधित",
    "āvacarassa": "लोक से संबंधित", "suññataṃ": "शून्य",
    "vihāraṃ": "रहना", "diṭṭhadhamma": "इसी जीवन", "rūpāvacaraṃ": "सूक्ष्म भौतिक लोक से संबंधित",
    "arūpāvacaraṃ jhānaṃ": "अभौतिक लोक से संबंधित ध्यान",
    # 2-746 summary
    "kāmāvacara": "इंद्रिय-सुखों के लोक से संबंधित", "kusalato": "हितकर", "kiriyato": "केवल क्रिया रूपी",
    "sampayuttesu": "जुड़ा", "cittuppādesu": "मन की … उत्पत्ति", "uppādesu": "उत्पत्ति",
    "uppajjanti": "उत्पन्न होना", "uppajjati": "उत्पन्न होना", "maggesu": "मार्ग", "phalesu": "फल",
    # Pañhāpucchaka (plural -ā forms of the PI2 labels)
    "pahātabbā": "छोड़ा जाने वाला", "saṃkilesikā": "क्लेशों का विषय बनने वाला",
    "ācayagāmino": "संचय की ओर ले जाने वाला", "apacayagāminī": "संचय घटाने की ओर ले जाने वाला",
    "parittā": "सीमित", "majjhimā": "मध्यम", "paṇītā": "उत्तम", "aniyatā": "अनिश्चित",
    "vicārā": "सतत विचार", "vitakkā": "आरंभिक विचार",
    "nevavipākanavipākadhammadhammā": "न कर्म-फल रूपी न कर्म-फल उत्पन्न करने वाला",
    "anidassana": "दिखाई न देने वाला", "apaṭighā": "टकराव से रहित", "appaṭighā": "टकराव से रहित",
    "anidassanaapaṭighā": "दिखाई न देने वाला और टकराव से रहित",
    "cittā": "मन", "na hetū": "मूल रूपी न होने वाला", "lokiyā": "लौकिक",
    "kāmāvacarā": "इंद्रिय-सुखों के लोक से संबंधित", "rūpāvacarā": "सूक्ष्म भौतिक लोक से संबंधित",
    "arūpāvacarā": "अभौतिक लोक से संबंधित", "āvacarā": "लोक से संबंधित",
    "samaye": "उस समय", "vippayuttā": "अलग", "pītisahagatā": "उल्लास के साथ होने वाला",
}
TABLE = {**PI2, **T}

OVR = {
    "2-15-1-3-0": {"Hetu": "कारण"},                      # Hetuvāro «कारण का खंड»
    "2-15-1-4-0": {"Dhamma": "परिघटना"},
    "2-15-1-5-0": {"Paṭicca": "परस्पर-आश्रित"},
    "2-724": {"dhamma": "परिघटना"},                       # dhammapaṭisambhidā / dhammanirutt-; dhammaṃ = शिक्षा
    "2-749": {"uppannā": "उत्पन्न हो चुका",               # matrix label (siyā uppannā)
              "dhammā": NDE},                              # fragment of (neva)vipākadhammadhammā: «… करने वाला», no noun
    "2-750": {"sahabhuno": "साथ-साथ होना"},               # «मन के साथ-साथ होते हैं»
}
# cittuppāda segments: ārammaṇā = विषय («जिसका विषय … हो»), not the matrix «विषय वाला»
for _b in ("2-734", "2-735", "2-736", "2-737", "2-742", "2-743", "2-744"):
    OVR.setdefault(_b, {})["ārammaṇā"] = "विषय"
# ākiñcaññāyatana / nevasaññānāsaññāyatana: āyatana = क्षेत्र («… के क्षेत्र»), not इंद्रिय-क्षेत्र
for _b in ("2-728", "2-739", "2-745"):
    OVR.setdefault(_b, {})["āyatanaṃ"] = "क्षेत्र"

ALLOWED = {("2-746", "phalesu"): "text «फलों»: फल ~ फलों, the checker treats 2-letter words as exact"}
for _b in ("2-732", "2-733", "2-734", "2-735", "2-736", "2-737", "2-738", "2-739", "2-740", "2-741", "2-742"):
    ALLOWED[(_b, "katattā")] = "text «किए जाने»: किया ~ किए is regular inflection the checker does not model (pi-1 value)"
ALLOWED[("2-740", "bhāvitattā")] = "text «अभ्यास किए जाने»: किया ~ किए (pi-1 value)"
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
