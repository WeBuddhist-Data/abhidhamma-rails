"""pi-7 Pāli->Hindi keyword maps for 2-02-pitittika … 2-08-parittarammanattika.

Conventions: hi-map-conventions-pi7.md (+ pi-1/pi-2/pi-6). Table module map_sample_hi.py imported read-only.
usage: python -I -B -X utf8 map_2-02_2-08_hi.py [<file> …] [--audit]
"""
import sys, pathlib
sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import *  # noqa: F401,F403

FILES = ("2-02-pitittika", "2-03-dassanenapahatabbattika", "2-04-dassanenapahatabbahetukattika",
         "2-05-acayagamittika", "2-06-sekkhattika", "2-07-parittattika", "2-08-parittarammanattika")

T = {}
# --- conditions: the locative X-paccaye (text «X-कारण में») = the name; bare stems of abbreviated lists
#     («āhāra…pe… indriya… jhāna…», text «आहार-कारण से… क्षमता-कारण से…») and heading members
#     («Aññamañña-nissayapaccayā», «Naadhipati-naāsevanapaccayā») = the name / «<name> का अभाव».
for _st, _name, _loc, _neg, _plain in CONDITIONS:
    T[_st + "paccaye"] = _name
    T[_neg + _st + "paccaye"] = f"{_name} का अभाव"
    T.setdefault(_st, (_name, _plain) if _plain else _name)
    T.setdefault(_neg + _st, f"{_name} का अभाव")
T["atthi"] = ("उपस्थिति-कारण", "है")                  # condition in a list; «… atthi» (there is) = है
T["natthi"] = ("नहीं", "अनुपस्थिति-कारण")              # «(paṭisandhi natthi)» = नहीं है; else the condition
T["adhipati"] = "प्रधानता"          # the predominant state itself («… adhipati», text «उन्नत प्रधानता»)
T["sampayutta"] = ("जुड़ाव-कारण", "जुड़ा")
T["vippayutta"] = ("अलगाव-कारण", "अलग")
T["sahajāta"] = ("सह-उत्पत्ति-कारण", "सह-उत्पत्ति")
T["anantara"] = ("निकटता-कारण", "निकटता")
T["saṃsaṭṭha"] = "घुला-मिला होना"                      # heading member «घुले-मिले होने … का खंड»
T.update({
    # counts
    "soḷasa": "सोलह", "sattarasa": "सत्रह", "terasa": "तेरह", "cuddasa": "चौदह", "dvādasa": "बारह",
    "ekādasa": "ग्यारह", "pannarasa": "पंद्रह", "ekavīsa": "इक्कीस",
    "suddhaṃ": "अकेले-अकेले कारण",                      # count heading «*अकेले-अकेले कारण*» (4-02 agent too)
    # instructions
    "paripuṇṇaṃ": "पूरा", "paripuṇṇā": "पूरा",
    "kātabbaṃ": ("बनाना चाहिए", "शामिल करना चाहिए", "करना चाहिए", "लेना चाहिए"),
    "kātabbā": ("बनाना चाहिए", "शामिल करना चाहिए", "करना चाहिए", "लेना चाहिए"),
    "kātabbo": ("शामिल करना चाहिए", "बनाना चाहिए", "करना चाहिए", "लेना चाहिए"),
    "kātabbāni": ("बनाना चाहिए", "करना चाहिए"),
    "niyāmetabbaṃ": ("निर्धारित करना चाहिए", "निश्चित करना चाहिए"), "niyāmetabbāni": "निर्धारित करना चाहिए",
    "dīpetabbo": "दिखाना चाहिए", "vibhajitabbaṃ": ("विश्लेषण करना चाहिए", "विभाजन करना चाहिए"),
    "vibhajitabbā": ("विभाजन करना चाहिए", "विश्लेषण करना चाहिए"),
    "vitthāretabbāni": "विस्तार करना चाहिए", "niddisitabbaṃ": "निर्देश करना चाहिए",
    "anumajjantena": "अनुसरण करते हुए", "passitvā": "देखकर", "gaṇanāni": "गणना", "gaṇanā": "गणना",
    "gaṇanāya": "गणना", "gamanāni": "प्रसंग", "padāni": "पद", "dassitanayena": "दिखाई गई विधि",
    "pāḷiyaṃ": "पाठ", "likhitā": "लिखा गया", "byañjanena": "शब्द", "samenti": "मेल खाना",
    "missagataṃ": "मिश्रित रूप", "missakapañhā": "मिश्रित प्रश्न", "ghaṭanā": "संयोजन",
    "cakkaṃ": "चक्र", "avasesā": "बाकी", "pañhā": "प्रश्न",
    "pavattipaṭisandhi": ("जीवन-प्रक्रिया और पुनर्जन्म", "प्रक्रिया और पुनर्जन्म"),
    # items and their companions
    "vicikicchāsahagat": "संशय के साथ होने वाला",
    "uddhaccasahagat": "बेचैनी के साथ होने वाला",
    "kāyaviññāṇasahagataṃ": "शरीर की चेतना के साथ होने वाला",
    "catuviññāṇasahagataṃ": "चार प्रकार की चेतना के साथ होने वाला",
    "pañcaviññāṇasahagataṃ": "पाँच प्रकार की चेतना के साथ होने वाला",
    "pañcaviññāṇaṃ": "पाँच प्रकार की चेतना", "viññāṇānaṃ": "चेतना",
    "nevadassanena": "न सत्य-दर्शन", "nabhāvanāya": "न मानसिक अभ्यास",
    "moho": "मोह", "mohaṃ": "मोह", "mohassa": "मोह", "mohañca": "मोह",
    "doso": "द्वेष", "dosaṃ": "द्वेष", "dosassa": "द्वेष", "māno": "अहंकार", "rāgassa": "राग",
    "diṭṭhiyā": "दृष्टि", "cāgaṃ": "त्याग", "cāgo": "त्याग",
    "sutaṃ": ("सुना-सीखा ज्ञान", "सुना हुआ ज्ञान", "सुना हुआ"),
    "gaṇhāti": ("पकड़ना", "अपनाना", "ग्रहण करना"),
    "pāṇaṃ": ("प्राणी", "जीव"),
    # Pañhāvāra vocabulary
    "cittena": "मन", "phalā": "फल", "vipassanti": "अंतर्दृष्टि से देखना", "assādenti": "रस लेना",
    "abhinandanti": "आनंद लेना", "cetopariyañāṇena": "दूसरों के मन को जानने का ज्ञान",
    "cetopariyañāṇaṃ": "दूसरों के मन को जानने का ज्ञान", "iddhividhañāṇaṃ": "अलौकिक शक्तियों का ज्ञान",
    "pubbenivāsānussatiñāṇaṃ": "पूर्व जन्मों के अनुस्मरण का ज्ञान",
    "yathākammūpagañāṇaṃ": "प्राणियों के अपने कर्मों के अनुसार जाने का ज्ञान",
    "anāgataṃsañāṇaṃ": "भविष्य को जानने का ज्ञान",
    "upapatticittassa": "जन्म का मन", "cuticittaṃ": "मृत्यु का मन", "bhavaṅgaṃ": "जीवन-धारा",
    "vipākamanoviññāṇadhātu": "कर्म के फल रूपी मन की चेतना का तत्व",
    "vipākamanoviññāṇadhātuyā": "कर्म के फल रूपी मन की चेतना का तत्व",
    "kiriyamanoviññāṇadhātuyā": "केवल क्रिया रूपी मन की चेतना का तत्व",
    "vipākamanodhātu": "कर्म के फल रूपी मन का तत्व", "vipākamanodhātuyā": "कर्म के फल रूपी मन का तत्व",
    "vuṭṭhānassa": ("बाहर आने वाला मन", "बाहर आना"), "vuṭṭhānassapi": ("बाहर आने वाला मन", "बाहर आना"),
    "kiriyaṃ": "केवल क्रिया रूपी", "kiriyassa": "केवल क्रिया रूपी",
    "āvajjanā": ("मन को विषय की ओर मोड़ने की क्रिया", "मन को विषय की ओर मोड़ना"),
    "anulomaṃ": ("सकारात्मक क्रम", "अनुरूपता"),
    "adinnaṃ": "बिना दिया हुआ", "ādiyati": "लेना", "musā": "झूठ", "bhaṇati": "बोलना",
    "pisuṇaṃ": "चुगली", "samphaṃ": "व्यर्थ", "palapati": "बकवास करना", "sandhiṃ": "सेंध",
    "chindati": "लगाना", "nillopaṃ": "डाका", "harati": "डालना", "ekāgārikaṃ": "एक घर को लूटना",
    "paripanthe": "राह में घात", "tiṭṭhati": "खड़ा होना", "paradāraṃ": "पराई स्त्री",
    "gacchati": "पास जाना", "gāmaghātaṃ": "गाँव पर धावा", "nigamaghātaṃ": "कस्बे पर धावा",
    "nibbānaṃ": "निर्वाण", "arahā": "अर्हत्", "puthujjanā": "साधारण व्यक्ति",
    "parihīne": "छूट जाना", "vippaṭisārissa": "ग्लानि से भरा व्यक्ति",
    "sakabhaṇḍe": "अपनी वस्तु",
    "niruddhe": "समाप्त होना", "tadārammaṇatā": "उसी विषय को लेकर",
    "attānaṃ": "स्वयं", "ātāpeti": "तपाना", "paritāpeti": "संतप्त करना",
    "pariyiṭṭhimūlakaṃ": "खोज से उत्पन्न", "paccanubhoti": "भोगना",
    "anuppannaṃ": "उत्पन्न नहीं हुआ", "uppannaṃ": "उत्पन्न हो चुका",
    "kusalasamāpattiṃ": "हितकर ध्यान-अवस्था", "kiriyasamāpattiṃ": "केवल क्रिया रूपी ध्यान-अवस्था",
    "uppādenti": "उत्पन्न करना", "samāpajjanti": "प्रवेश करना", "samāpajjati": "प्रवेश करना",
    "saṅkhāre": "मानसिक रचनाएँ",
    "atthappaṭisambhidāya": "अर्थ का विश्लेषणात्मक ज्ञान",
    "paṭibhānapaṭisambhidāya": "सूझ-बूझ का विश्लेषणात्मक ज्ञान",
    "paṭibhānappaṭisambhidāya": "सूझ-बूझ का विश्लेषणात्मक ज्ञान",
    "ṭhānāṭhānakosallassa": "संभव और असंभव को जानने की कुशलता",
    "parikammaṃ": "प्रारंभिक तैयारी", "paṭhamassa": "पहला", "dutiyassa": "दूसरा", "tatiyassa": "तीसरा",
    "catutthassa": "चौथा", "tatiyo": "तीसरा", "jhānassa": "ध्यान", "tasseva": "उसी",
    "phalasamāpatti": "फल की ध्यान-अवस्था", "phalasamāpattiṃ": "फल की ध्यान-अवस्था",
    "sukhassa": "सुख", "dukkhassa": "दुःख",
    "gotrabhuṃ": "गोत्र-परिवर्तन", "dibbaṃ": "दिव्य", "dibbassa": "दिव्य", "cakkhussa": "आँख",
    "sotadhātuṃ": "कान का तत्व", "uposathaṃ": "उपवास-व्रत",
    "pāṇātipāto": ("जीवों की हत्या", "जीव-हत्या"), "mātughātikammaṃ": "माता की हत्या का कर्म",
    "suṇanti": "सुनना",
    "purimo": "पहले-पहले का", "pacchimassa": "बाद-बाद का",
    "maggapaccavekkhaṇaṃ": "मार्ग पर हुआ पुनर्विचार",
    "paṭhamajjhānapaccavekkhaṇaṃ": "पहले ध्यान पर हुआ पुनर्विचार",
    "ahetukā": "मूल से रहित",
    "āhāraṃ": "आहार", "indriyaṃ": "क्षमता",                 # atthipaccaya subtypes «…, आहार, क्षमता»
    "ārammaṇaupanissayā": "विषय-कारण और प्रबल आश्रय-कारण",
    "rūpaṃ": ("भौतिक रूप", "दृश्य रूप"),                    # «dibbena cakkhunā rūpaṃ passati»
    "vipāke": ("कर्म-फल-कारण", "कर्म के फल रूपी", "कर्म-फल"),   # count word / «vipāke … khandhe»
    "upapatticittassa": ("जन्म का मन", "जन्म का … मन"),     # «जन्म के उन्नत मन के लिए»
    "mahaggatādhipati": "उन्नत प्रधानता", "appamāṇādhipati": "अपरिमित प्रधानता",
    "parittādhipati": "सीमित प्रधानता",
    "ācayagāmiyā": "संचय की ओर ले जाने वाला", "apacayagāmiyā": "संचय घटाने की ओर ले जाने वाला",
    "nevācayagāmināpacayagāmiyā": "न संचय की ओर न संचय घटाने की ओर ले जाने वाला",
    # persons: sekkhā (noun) «सीखने के चरण वाले», the item adjective «सीखने के चरण का» (tuple)
    "sekkhā": ("सीखने के चरण का", "सीखने के चरण वाला"), "sekkhānaṃ": ("सीखने के चरण का", "सीखने के चरण वाला"),
    "asekkhā": ("सीखना पूरा होने के चरण का", "सीखना पूरा होने के चरण वाला"),
    "pītisahagatacittasamaṅgissa": "उल्लास के साथ होने वाले मन से युक्त व्यक्ति",
    "pahātabbacittasamaṅgissa": "छोड़े जाने वाले मन से युक्त व्यक्ति",
    "appamāṇārammaṇaappamāṇacittasamaṅgissa": "अपरिमित विषय वाले अपरिमित मन से युक्त व्यक्ति",
    "nevasaññānāsaññāyatanakiriyaṃ": "न पहचान न अ-पहचान के क्षेत्र का केवल क्रिया रूपी मन",
    "viññāṇañcāyatanakiriyassa": "अनंत चेतना के क्षेत्र का केवल क्रिया रूपी मन",
})
for _st in ("vicikicchāsahagat", "uddhaccasahagat"):
    _h = T.pop(_st)
    for _e in ("aṃ", "o", "ā", "assa", "ānaṃ", "e", "añca", "a", "āya"):
        T[_st + _e] = _h

OVR_ALL = {f: {} for f in FILES}
OVR_ALL["2-02-pitittika"].update({
    "7-8-4": {"vipākaṃ": "कर्म-फल-कारण"},              # «(āsevane vipākaṃ natthi)» = «(… कर्म-फल-कारण नहीं है)»
})
OVR_ALL["2-04-dassanenapahatabbahetukattika"].update({
    "7-10-112": {"atthi": "है"},                         # «(… missakapañhā atthi)» = «… मिश्रित प्रश्न है»
    "7-10-79": {"dassanattikaṃ": "सत्य-दर्शन वाला तीन का वर्गीकरण"},   # «(yathā dassanattikaṃ)», text
})                                                       # «जैसे सत्य-दर्शन वाले तीन के वर्गीकरण में»
ALLOWED = {f: {} for f in FILES}
_PADA = "the checker does not inflect the two-letter noun पद (text «पदों»)"
ALLOWED["2-03-dassanenapahatabbattika"].update({("7-9-15", "padāni"): _PADA, ("7-9-61", "padāni"): _PADA})
ALLOWED["2-04-dassanenapahatabbahetukattika"].update({
    ("7-10-112", "likhitā"): "separate «na» is not a keyword: positive part; text «लिखे नहीं गए»",
    ("7-10-112", "samenti"): "separate «na» is not a keyword: positive part; text «मेल नहीं खाते»",
})

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")] or list(FILES)
    for _f in args:
        build_part(_f, make_resolver(_f, {**PI7, **T}, OVR_ALL[_f]))
        verify(_f, allowed=ALLOWED[_f])
        if "--audit" in sys.argv:
            audit(_f, {**PI7, **T}, OVR_ALL[_f], only_fallback=True)
