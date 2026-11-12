"""pi-2 Pāli->Hindi keyword map: 6-paticcasamuppadavibhango.

Imports map_sample_hi (read-only; PI2, pi2_value, build_part, verify, present). Writes only
6-paticcasamuppadavibhango.mapped.md.

Chapter rules (beyond hi-map-conventions-pi2.md), all read off this chapter's Hindi:
- X-paccayā: «X के कारण» where the segment uses the link as a chain (X के कारण Y / X के कारण भी Y);
  «X के कारण होने वाला» where it only occurs inside the «Tattha katamo X-paccayā Y?» definitions
  (attributive, as 1-khandhavibhango cakkhusamphassapaccayā = «… के कारण होने वाला»). Bare paccayā likewise.
  saṅkhārapaccayā = «मानसिक रचनाओं के कारण» in the Suttanta part (saṅkhārā plural), «मानसिक रचना के कारण»
  in the Abhidhamma part (saṅkhāro, one mind-moment; notes-6).
- Hetucatukka «Y X-hetuko» = «Y जिसका मूल X है» (comma dropped); hetuko / hetukaṃ / hetukā = «जिसका मूल … है».
- Sampayuttacatukka «Y X-sampayutto» = «Y जो X से जुड़ा है»; sampayutto = जुड़ा.
- catukkaṃ = चार रूप (Paccaya- कारण के चार रूप, Hetu- मूल के, Sampayutta- जुड़ाव के, Aññamañña- परस्परता के).
- X-ārammaṇaṃ/-ā in «जिसका विषय दृश्य रूप हो, या ध्वनि …»: «विषय X» where contiguous, else «विषय … X»;
  dhammārammaṇa = मन का विषय (pi-1).
- kevalassa dukkhakkhandhassa = पूरे दुःख का समूह (text «इस पूरे दुःख के समूह»).

usage: python -I -X utf8 map_6-paticcasamuppadavibhango_hi.py
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import (PI2, NDE, pi2_value, build_part, verify, present,  # noqa: E402
                           read_hindi, read_pali, lc)
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pi-1-hi" / "mapper-hi"))
from map_common_hi import _norm, _pattern  # noqa: E402  (read-only)

CH = "6-paticcasamuppadavibhango"
HI = read_hindi(CH)
PA = read_pali(CH)
SUTTANTA = {f"2-{n}" for n in range(225, 243)} | {"2-6-0", "2-6-1-0"}

# ---------------------------------------------------------------- the links of the chain (Hindi oblique stem)
LINK = {
    "avijjā": "अज्ञान", "saṅkhāra": None, "viññāṇa": "चेतना", "nāmarūpa": "मानसिक पक्ष और भौतिक रूप",
    "nāma": "मानसिक पक्ष", "rūpa": "भौतिक रूप", "saḷāyatana": "छह इंद्रिय-क्षेत्रों",
    "chaṭṭhāyatana": "छठे इंद्रिय-क्षेत्र", "āyatana": "इंद्रिय-क्षेत्र", "phassa": "संपर्क",
    "vedanā": "अनुभूति", "taṇhā": "तृष्णा", "upādāna": "आसक्ति", "bhava": "अस्तित्व", "jāti": "जन्म",
    "pasāda": "आस्था", "adhimokkha": "निश्चय", "kusalamūla": "हितकर मूलों", "akusalamūla": "हानिकर मूलों",
    "mūla": "मूलों", "paṭigha": "चिढ़", "vicikicchā": "संशय", "uddhacca": "बेचैनी",
}

T = {
    # headings
    "vibhaṅgo": "विश्लेषण", "paṭicca": "परस्पर-आश्रित", "samuppāda": "उत्पत्ति",
    "catukkaṃ": "चार रूप", "paccayacatukkaṃ": "कारण के चार रूप", "hetu": "मूल",
    "sampayuttacatukkaṃ": "जुड़ाव के चार रूप", "aññamañña": "परस्परता",
    "aññamaññacatukkaṃ": "परस्परता के चार रूप", "mātikā": "मूल सूची", "niddeso": "व्याख्या",
    "mūlaka": "से शुरू होने वाला", "vipākaniddeso": "कर्म-फल की व्याख्या",
    "mūlakavipāka": "मूलों से शुरू होने वाला कर्म-फल",
    # chain terms
    "avijjā": "अज्ञान", "saṅkhārā": "मानसिक रचनाएँ", "saṅkhāro": "मानसिक रचना",
    "viññāṇaṃ": "चेतना", "viññāṇa": "चेतना", "nāma": "मानसिक पक्ष", "nāmaṃ": "मानसिक पक्ष",
    "nāmarūpaṃ": "मानसिक पक्ष और भौतिक रूप", "nāmarūpa": "मानसिक पक्ष और भौतिक रूप",
    "rūpaṃ": "भौतिक रूप", "rūpa": "भौतिक रूप",
    "saḷāyatanaṃ": "छह इंद्रिय-क्षेत्र", "saḷāyatana": "छह इंद्रिय-क्षेत्र",
    "chaṭṭhāyatanaṃ": "छठा इंद्रिय-क्षेत्र", "chaṭṭhāyatana": "छठा इंद्रिय-क्षेत्र",
    "āyatanaṃ": "इंद्रिय-क्षेत्र", "āyatana": "इंद्रिय-क्षेत्र", "āyatanānaṃ": "इंद्रिय-क्षेत्र",
    "phasso": "संपर्क", "phassa": "संपर्क", "vedanā": "अनुभूति", "taṇhā": "तृष्णा",
    "upādānaṃ": "आसक्ति", "upādāna": "आसक्ति", "bhavo": "अस्तित्व", "bhava": "अस्तित्व",
    "jāti": "जन्म", "jarā": "बुढ़ापा", "maraṇaṃ": "मृत्यु", "jarāmaraṇaṃ": "बुढ़ापा और मृत्यु",
    "pasādo": "आस्था", "adhimokkho": "निश्चय",
    "soka": "शोक", "parideva": "विलाप", "upāyāsā": "निराशा", "domanassupāyāsā": "उदासी और निराशा",
    "dukkha": "दुःख", "kevalassa": "पूरा", "khandhassa": "समूह", "dukkhakkhandhassa": "दुःख का समूह",
    "kevalassa dukkhakkhandhassa": "पूरे दुःख का समूह", "samudayo": "उत्पत्ति",
    "saṅgati": "मेल", "samodhānaṃ": "जुड़ाव", "dhammānaṃ": "परिघटना",
    "tattha": "यहाँ", "samaye": "उस समय",
    # hetu / sampayutta catukka
    "saṅkhāro avijjāhetuko": "मानसिक रचना जिसका मूल अज्ञान है",
    "vedanā phassahetukā": "अनुभूति जिसका मूल संपर्क है",
    "taṇhā vedanāhetukā": "तृष्णा जिसका मूल अनुभूति है",
    "upādānaṃ taṇhāhetukaṃ": "आसक्ति जिसका मूल तृष्णा है",
    "sampayutto": "जुड़ा", "sampayuttaṃ": "जुड़ा", "sampayuttā": "जुड़ा",
    # 2-226 avijjā, saṅkhārā
    "dukkhe": "दुःख", "aññāṇaṃ": "न जानना", "ñāṇaṃ": "जानना", "samudaye": "उत्पत्ति",
    "dukkhasamudaye": "दुःख की उत्पत्ति", "nirodhe": "अंत", "dukkhanirodhe": "दुःख का अंत",
    "puññābhisaṅkhāro": "पुण्य की कर्म-रचना", "apuññābhisaṅkhāro": "अपुण्य की कर्म-रचना",
    "āneñjābhisaṅkhāro": "अविचल अवस्था की कर्म-रचना", "ābhisaṅkhāro": "कर्म-रचना",
    "kāyasaṅkhāro": "शरीर की रचना", "kāya": "शरीर", "vacī": "वाणी", "citta": "मन",
    "dāna": "दान", "sīla": "सदाचार", "bhāvanā": "मानसिक अभ्यास",
    "kāmāvacarā": "इंद्रिय-सुखों के लोक से संबंधित", "rūpāvacarā": "सूक्ष्म भौतिक लोक से संबंधित",
    "arūpāvacarā": "अभौतिक लोक से संबंधित", "āvacarā": "लोक से संबंधित",
    # 2-227 .. 2-233
    "upādāya rūpaṃ": "व्युत्पन्न भौतिक रूप", "bhūtā": "महाभूत",
    "kāmupādānaṃ": "इंद्रिय-सुखों के प्रति आसक्ति", "diṭṭhupādānaṃ": "दृष्टियों के प्रति आसक्ति",
    "sīlabbatupādānaṃ": "सदाचार और व्रतों के प्रति आसक्ति",
    "attavādupādānaṃ": "आत्मा के सिद्धांत के प्रति आसक्ति", "atta": "आत्मा",
    "dhamma": "मन के विषय", "gandha": "गंध", "sadda": "ध्वनि", "rasa": "स्वाद", "phoṭṭhabba": "स्पर्श",
    # 2-234 bhava
    "kammabhavo": "कर्म रूपी अस्तित्व", "upapattibhavo": "पुनर्जन्म रूपी अस्तित्व", "duvidhena": "दो प्रकार",
    "kāma": "इंद्रिय-सुख", "arūpa": "अभौतिक लोक", "asaññā": "पहचान से रहित",
    "nevasaññānāsaññā": "न पहचान न अ-पहचान", "ekavokāra": "एक समूह वाला",
    "catuvokāra": "चार समूहों वाला", "pañcavokāra": "पाँच समूहों वाला", "gāmi": "की ओर ले जाने वाला",
    # 2-235 / 2-236 jāti, jarāmaraṇa
    "tesaṃ tesaṃ": "उन-उन", "sattānaṃ": "प्राणी", "nikāye": "प्राणी-वर्ग", "sañjāti": "भली-भाँति जन्म",
    "okkanti": "गर्भ में उतरना", "abhinibbatti": "पूरी तरह पैदा होना", "nibbatti": "पैदा होना",
    "khandhānaṃ": "समूह", "paṭilābho": "प्राप्ति",
    "jīraṇatā": "जीर्ण होना", "khaṇḍiccaṃ": "दाँतों का टूटना", "pāliccaṃ": "बालों का पकना",
    "vali": "झुर्री", "taca": "त्वचा", "āyuno": "आयु", "indriyānaṃ": "इंद्रिय", "paripāko": "पूरी तरह पक जाना",
    "cuti": "गुज़र जाना", "bhedo": "टूटना", "antaradhānaṃ": "लुप्त हो जाना", "maccu": "मौत",
    "kālakiriyā": "काल का पूरा होना", "kaḷevarassa": "शरीर", "nikkhepo": "त्याग",
    "jīvitindriya": "जीवन-क्षमता", "indriya": "क्षमता", "upacchedo": "कट जाना",
    "khayo": "क्षय", "vayo": "नाश", "paribhedo": "बिखर जाना", "aniccatā": "अनित्यता",
    # 2-237 .. 2-241 soka, parideva, dukkha, domanassa, upāyāsa
    "ñāti": "संबंधी", "bhoga": "धन-संपत्ति", "roga": "रोग", "diṭṭhi": "दृष्टि", "byasanena": "हानि",
    "phuṭṭhassa": "पीड़ित", "byasanena vā phuṭṭhassa": "हानि से पीड़ित", "samannāgatassa": "घिरा",
    "dhammena": "परिघटना", "soko": "शोक", "socanā": "शोक करना", "anto": "भीतर", "parisoko": "गहरा शोक",
    "cetaso": "मन", "parijjhāyanā": "जलना", "domanassaṃ": "उदासी", "sallaṃ": "काँटा",
    "paridevo": "विलाप", "ādevo": "रोना", "ādevanā": "रोते रहना", "vācā": "शब्दों की झड़ी",
    "palāpo": "प्रलाप", "vippalāpo": "बड़बड़ाना", "lālappo": "बिलखना",
    "kāyikaṃ": "शारीरिक", "asātaṃ": "असुहावना", "dukkhaṃ": "दुःख", "dukkhaṃ vedayitaṃ": "दुःखद अनुभव",
    "dukkhā vedanā": "दुःखद अनुभूति", "asātaṃ dukkhaṃ": "असुहावना दुःखद",
    "asātaṃ dukkhaṃ vedayitaṃ": "असुहावना दुःखद अनुभव", "asātā dukkhā vedanā": "असुहावनी दुःखद अनुभूति",
    "kāyasamphassajaṃ": "शरीर के संपर्क से उत्पन्न", "cetasikaṃ": "मानसिक",
    "cetasikaṃ asātaṃ": "मानसिक असुहावनापन", "cetasikaṃ dukkhaṃ": "मानसिक दुःख",
    "cetosamphassa": "मन का संपर्क", "upāyāso": "निराशा", "āyāso": "हताशा",
    # 2-242 summary
    "bhājanīyaṃ": "विश्लेषण", "suttanta": "उपदेश",
    # Abhidhamma part: openings of the types of mind (pi-1 wording, pi-2 Hindi)
    "dhammā": "परिघटना", "dhammā akusalā": "हानिकर परिघटना", "dhammā kusalā": "हितकर परिघटना",
    "dhammā abyākatā": "नैतिक रूप से अनिर्धारित परिघटना",
    "akusalaṃ": "हानिकर", "akusalaṃ cittaṃ": "हानिकर मन", "kusalaṃ": "हितकर", "kusalaṃ cittaṃ": "हितकर मन",
    "akusala": "हानिकर", "akusalā": "हानिकर", "ākusalaṃ": "हानिकर", "ākusalā": "हानिकर",
    "akusalassa": "हानिकर", "kusalassa": "हितकर", "kusalassa kammassa": "हितकर कर्म",
    "kāmāvacarassa": "इंद्रिय-सुखों के लोक से संबंधित", "kāmāvacarassa kusalassa": "इंद्रिय-सुखों के लोक से संबंधित हितकर",
    "rūpāvacarassa": "सूक्ष्म भौतिक लोक से संबंधित", "arūpāvacarassa": "अभौतिक लोक से संबंधित",
    "āvacarassa": "लोक से संबंधित", "āvacaraṃ": "लोक से संबंधित",
    "uppannaṃ": "उत्पन्न", "uppannā": "उत्पन्न", "cittaṃ": "मन", "cittassa": "मन",
    "sahagataṃ": "के साथ होने वाला", "sahagatā": "के साथ होने वाला",
    "somanassasahagataṃ": "प्रसन्नता के साथ होने वाला", "somanassasahagatā": "प्रसन्नता के साथ होने वाला",
    "upekkhāsahagataṃ": "समभाव के साथ होने वाला", "upekkhāsahagatā": "समभाव के साथ होने वाला",
    "sukhasahagataṃ": "सुख के साथ होने वाला",
    "somanassa": "प्रसन्नता", "upekkhā": "समभाव", "ñāṇa": "ज्ञान",
    "ñāṇavippayuttaṃ": "ज्ञान से अलग", "ñāṇavippayuttā": "ज्ञान से अलग",
    "vippayuttaṃ": "अलग", "vippayuttā": "अलग",
    "diṭṭhigata": "ग़लत दृष्टि", "sasaṅkhārena": "प्रेरणा सहित", "yaṃ yaṃ": "जिस किसी",
    "ārammaṇaṃ": "विषय", "ārammaṇā": "विषय",
    "dhammārammaṇaṃ": "मन का विषय", "dhammārammaṇā": "मन का विषय",
    "katattā": "किया जाना", "upacitattā": "संचित होना", "vipākaṃ": "कर्म के फल रूपी",
    "vipākā": "कर्म के फल रूपी", "kiriyā": "केवल क्रिया रूपी", "kiriyaṃ": "केवल क्रिया रूपी",
    "kusalā nākusalā": "न हितकर न हानिकर", "kusalaṃ nākusalaṃ": "न हितकर न हानिकर",
    "dhātu uppannā": "तत्व उत्पन्न", "manodhātu": "मन का तत्व",
    # jhāna openings
    "bhāveti": "अभ्यास करना", "maggaṃ": "मार्ग", "maggaṃ bhāveti": "मार्ग का अभ्यास करना",
    "jhānaṃ": "ध्यान", "jhānaṃ bhāveti": "ध्यान का अभ्यास करना",
    "rūpūpapattiyā": "सूक्ष्म भौतिक लोक में जन्म", "arūpūpapattiyā": "अभौतिक लोक में जन्म",
    "ūpapattiyā": "जन्म", "ūpapattiyā maggaṃ": "जन्म की ओर ले जाने वाला मार्ग",
    "vivicceva": "अलग होकर", "kāmehi": "इंद्रिय-सुख", "vivicceva kāmehi": "इंद्रिय-सुखों से अलग होकर",
    "upasampajja": "प्राप्त करके", "viharati": "रहना", "upasampajja viharati": "प्राप्त करके उसमें रहना",
    "kasiṇaṃ": "ध्यान-मंडल", "pathavī": "पृथ्वी", "pathavīkasiṇaṃ": "पृथ्वी का ध्यान-मंडल",
    "sabbaso": "पूरी तरह", "samatikkamma": "पार करके", "ākiñcaññāyatanaṃ": "कुछ भी न होने का क्षेत्र",
    "nevasaññānāsaññāyatana": "न पहचान न अ-पहचान का क्षेत्र", "saññā": "पहचान",
    "sukhassa": "सुख", "pahānā": "छोड़ना", "sukhassa ca pahānā": "सुख को छोड़ना",
    "catutthaṃ jhānaṃ": "चौथा ध्यान", "lokuttaraṃ": "लोकोत्तर",
    "apacaya": "संचय घटाना", "apacayagāmiṃ": "संचय घटाने की ओर ले जाने वाला",
    "diṭṭhigatānaṃ": "दृष्टियों में फँसना", "pahānāya": "छोड़ना",
    "diṭṭhigatānaṃ pahānāya": "दृष्टियों में फँसने को छोड़ना", "bhūmiyā": "चरण", "pattiyā": "प्राप्ति",
    "dukkhapaṭipadaṃ": "दुःखद प्रगति", "paṭipadaṃ": "प्रगति", "dandhābhiññaṃ": "धीमे उच्च ज्ञान वाला",
    "ābhiññaṃ": "उच्च ज्ञान वाला", "paṭipadaṃ dandhābhiññaṃ": "प्रगति और धीमे उच्च ज्ञान वाला",
    # definitions inside the Abhidhamma part (pi-1 strings, pi-2 Hindi)
    "adassanaṃ": "न देखना", "laṅgī": "रुकावट", "moho": "मोह", "mūlaṃ": "मूल", "mūla": "मूल", "mūlā": "मूल",
    "akusalamūlaṃ": "हानिकर मूल", "kusalamūlaṃ": "हितकर मूल", "kusalamūla": "हितकर मूल",
    "kusalamūlā": "हितकर मूल", "akusalamūla": "हानिकर मूल",
    "sañcetayitattaṃ": "इरादा कर चुका होना",
    "rāgo": "राग", "sārāgo": "प्रबल राग", "anunayo": "झुकाव", "anurodho": "अनुकूल होना", "nandī": "आनंद",
    "nandirāgo": "आनंद का राग",
    "diṭṭhigataṃ": "दृष्टियों में फँसना", "gahanaṃ": "घना जंगल", "kantāro": "बीहड़",
    "visūkāyikaṃ": "टेढ़ापन", "vipphanditaṃ": "छटपटाहट", "saṃyojanaṃ": "बंधन", "gāho": "पकड़",
    "abhiniveso": "आग्रह", "parāmāso": "ग़लत धारणा", "kummaggo": "कुमार्ग", "maggo": "कुमार्ग",
    "micchāpatho": "ग़लत रास्ता", "patho": "रास्ता", "micchā": "ग़लत", "micchattaṃ": "ग़लतपन",
    "titthāyatanaṃ": "मतवादों का आधार", "vipariyāsa": "उलटा", "vipariyāsaggāho": "उलटी पकड़",
    "sātaṃ sukhaṃ": "सुहावना सुखद", "sātaṃ sukhaṃ vedayitaṃ": "सुहावना सुखद अनुभव",
    "sātā sukhā vedanā": "सुहावनी सुखद अनुभूति", "nāsātaṃ": "न … असुहावना",
    "adukkhamasukhā vedanā": "न दुःखद न सुखद अनुभूति",
    "alubbhanā": "लोभ न करना", "asārāgo": "प्रबल राग का अभाव", "adussanā": "द्वेष न करना",
    "vicayo": "छानबीन", "sammā": "सही", "sambojjhaṅgo": "जागृति का अंग",
    "vicayasambojjhaṅgo": "छानबीन नामक जागृति का अंग", "aṅgaṃ": "अंग", "maggaṅgaṃ": "मार्ग का अंग",
    "maggapariyāpannaṃ": "मार्ग में समाया हुआ",
    "adhimuccanā": "निश्चय करना", "tadadhimuttatā": "उस पर निश्चय कर चुका होना",
    "upādāya": "व्युत्पन्न",
}
for _p, _h in (("cakkhu", "आँख"), ("sota", "कान"), ("ghāna", "नाक"), ("jivhā", "जीभ"), ("kāya", "शरीर"),
               ("mano", "मन")):
    T[_p + "samphasso"] = f"{_h} का संपर्क"
    T[_p + "viññāṇa"] = f"{_h} की चेतना"
    T[_p + "viññāṇadhātu"] = f"{_h} की चेतना का तत्व"
for _k, _h in (("cakkhāyatanassa", "आँख"), ("sotāyatanassa", "कान"), ("ghānāyatanassa", "नाक"),
               ("jivhāyatanassa", "जीभ"), ("kāyāyatanassa", "शरीर")):
    T[_k] = f"{_h} का इंद्रिय-क्षेत्र"
for _p, _h in (("rūp", "दृश्य रूप"), ("sadd", "ध्वनि"), ("gandh", "गंध"), ("ras", "स्वाद"),
               ("phoṭṭhabb", "स्पर्श")):
    for _e in ("ārammaṇaṃ", "ārammaṇā"):
        T[_p + _e] = ("ARAMMANA", _h)
T.update({
    "abyākata": "नैतिक रूप से अनिर्धारित",
    # rūpa in the Abhidhamma nāmarūpa definitions (2-253 …)
    "cittajaṃ": "मन से जन्मा", "nissāya": "सहारा", "vattati": "काम करना", "samuṭṭhānaṃ": "उत्पन्न",
    "abhinibbati": "पूरी तरह पैदा होना",
    # paṭigha / vicikicchā / uddhacca strings (2-286 … 2-291)
    "paṭighaṃ": "चिढ़", "domanassa": "उदासी", "āghāto": "आक्रोश", "caṇḍikkaṃ": "उग्रता", "asuropo": "कटु वचन",
    "anattamanatā": "अप्रसन्नता", "vicikicchā": "संशय", "kaṅkhāyanā": "शंका करना", "vimati": "दुविधा",
    "dveḷhakaṃ": "दुचित्तापन", "dvidhāpatho": "दोराहा", "saṃsayo": "संदेह",
    "anekaṃsa": "किसी एक बात को पक्का न", "āsappanā": "हिचकिचाना", "parisappanā": "बार-बार हिचकिचाना",
    "apariyogāhaṇā": "गहराई में न उतर पाना", "chambhitattaṃ": "जड़ हो जाना", "vilekho": "खरोंच",
    "uddhaccaṃ": "बेचैनी", "avūpasamo": "अशांति", "vikkhepo": "भटकाव", "cetaso vikkhepo": "मन का भटकाव",
    "bhantattaṃ": "डाँवाडोल होना",
    # kiriya / vipāka jhāna openings
    "bhāvitattā": "अभ्यास किया जाना", "kusalassa jhānassa": "हितकर ध्यान", "suññataṃ": "शून्य",
    "diṭṭhadhamma": "इसी जीवन", "sukha": "सुख", "vihāraṃ": "रहना", "rūpāvacaraṃ": "सूक्ष्म भौतिक लोक से संबंधित",
    "arūpāvacaraṃ": "अभौतिक लोक से संबंधित", "arūpāvacaraṃ jhānaṃ": "अभौतिक लोक से संबंधित ध्यान",
})

PER_SEG = {
    "2-232": {"Rūpa": "दृश्य रूप"},
    "2-234": {"rūpa": "सूक्ष्म भौतिक लोक", "saññā": "पहचान"},
}


def _short_link(stem_hi, text):
    """True if «<stem> के कारण» occurs as a chain link (not followed by «होने वाल»)."""
    t = _norm(text)
    for m in _pattern(f"{stem_hi} के कारण").finditer(t):
        if not t[m.end():].lstrip().startswith("होने वाल"):
            return True
    return False


def _link_stem(stem, bid):
    if stem == "saṅkhāra":
        return "मानसिक रचनाओं" if bid in SUTTANTA else "मानसिक रचना"
    return LINK[stem]


def resolver(bid, kw, kws):
    text = HI[bid]
    k = lc(kw)
    s = set(lc(x) for x in kws)
    o = PER_SEG.get(bid, {})
    if kw in o:
        return o[kw]
    if k.endswith("paccayā") and k != "paccayā":
        stem = k[: -len("paccayā")]
        hi = _link_stem(stem, bid)
        return f"{hi} के कारण" if _short_link(hi, text) else f"{hi} के कारण होने वाला"
    if k == "paccayā":
        return "के कारण" if _short_link("", text) else "के कारण होने वाला"
    if k in ("hetuko", "hetukaṃ", "hetukā"):
        hetucatukka = "जिसका मूल" in text or "जिनका मूल" in text
        return "जिसका मूल … है" if hetucatukka else "के कारण होने वाला"   # cittahetukaṃ «मन के कारण होने वाला»
    if k == "gāho" and "anekaṃsa" in s:                  # anekaṃsaggāho «… पक्का न पकड़ पाना» (pi-1)
        return "पकड़ पाना"
    if k == "rūpaṃ nissāya":                             # «जिस भौतिक रूप के सहारे» / «वह भौतिक रूप, जिसके सहारे»
        return "भौतिक रूप के सहारे" if present("भौतिक रूप के सहारे", text) else "भौतिक रूप … जिसके सहारे"
    if k == "saṅkhāra":
        return "मानसिक रचनाएँ" if (bid in SUTTANTA or "saṅkhārakkhandho" in s) else "मानसिक रचना"
    if k == "saṅkhāro" and "kāyasaṅkhāro" in s:
        return "रचना"
    if k == "mano":
        return "मानस" if "mānasaṃ" in s else "मन"
    if k == "dhamma" and "dhammavicayo" in s:
        return "परिघटना"
    if k == "dukkha":
        if "dhammena" in s:
            return "दुःखद"
        if "dukkhapaṭipadaṃ" in s and "dukkhakkhandhassa" not in s:
            return "दुःखद"
        return "दुःख"
    if k == "pātubhāvo":
        # the jāti string («… पूरी तरह पैदा होना, प्रकट होना») before the closing «… प्रकटन होता है»
        return "प्रकट होना" if ({"sañjāti", "khandhānaṃ", "nibbatti", "abhinibbatti"} & s) else "प्रकटन"
    if k == "mūlaka" and present("मूलों से शुरू होने वाला", text):   # Kusalamūlaka- «हितकर मूलों से शुरू होने वाली»
        return "मूलों से शुरू होने वाला"
    if k == "tena":
        return "इसीलिए" if "इसीलिए" in text else "इसलिए"
    v = T.get(k)
    if isinstance(v, tuple):
        h = v[1]
        return f"विषय {h}" if present(f"विषय {h}", text) else f"विषय … {h}"
    if v is not None:
        return v
    return pi2_value(kw, kws, PI2, bid, text)


def allowed():
    """katattā / bhāvitattā = «(अभ्यास) किया जाना» (pi-1 value); the text has «किए जाने», regular inflection
    (किया ~ किए) that the checker does not model (pi-1 map_2-04_hi.py added the same tolerance)."""
    out = {}
    for line in (pathlib.Path(__file__).resolve().parent / f"{CH}.mapped.md").read_text(encoding="utf-8").splitlines():
        bid, rest = line[1:].split("] ", 1)
        for pair in rest.split(", "):
            kw, v = pair.split("=", 1)
            if v in ("किया जाना", "अभ्यास किया जाना") and not present(v, HI[bid]) \
                    and present(v.replace("किया जाना", "किए जाने"), HI[bid]):
                out[(bid, kw)] = "text «किए जाने»: किया ~ किए is regular inflection the checker does not model"
    return out


if __name__ == "__main__":
    n = build_part(CH, resolver)
    verify(CH, show=200, allowed=allowed())
