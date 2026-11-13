"""Tables for 1-01-kusalattika and 1-02-vedanattika (imported by map_1-01_1-02_hi.py and the probe).
Importing writes nothing and prints nothing. Reads map_sample_hi (read-only) for COND_NAME / CONDITIONS / NDE.
"""
import sys, pathlib
sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import CONDITIONS, NDE  # noqa: E402

T = {}

# --- bare condition stems inside the dvanda lists «Hetu-sahajāta-nissaya-atthi-avigatanti», headings
# «Anantara-samanantarapaccayā», «Jhāna-maggapaccayā» = the condition name (every form = the name).
# Tuple: where the name is absent from the segment, the plain term (adhipati paṭisandhikkhaṇe natthi …).
_PLAIN = {"adhipati": "प्रधानता", "kamma": "कर्म", "vipāka": "कर्म-फल", "āhāra": "आहार", "indriya": "क्षमता",
          "jhāna": "ध्यान", "magga": "मार्ग", "ārammaṇa": "विषय", "natthi": "नहीं", "sahajāta": "सह-उत्पन्न",
          "sampayutta": "जुड़ा", "vippayutta": "अलग"}
for _st, _name, _loc, _neg, _plain in CONDITIONS:
    if _st == "hetu":
        continue                                   # bare hetu stays pi-7 «मूल» (roots); not needed here
    _alts = (_name, _PLAIN[_st]) if _st in _PLAIN else _name
    for _f in (_st, _st + "nti"):
        T[_f] = _alts
    # negative bare stems: heading «… का अभाव और …», chain «naārammaṇa-naadhipati-… paccayā» «… के बिना»
    for _f in (_neg + _st, _neg + _st + "ṃ"):
        T[_f] = (f"{_name} का अभाव", f"{_name} के बिना")
    # series «X-mūlakaṃ» = «<name> से शुरू होने वाली शृंखला»; naX- «<name> के अभाव से …»
    for _e in ("mūlakaṃ", "mūlake", "mūlakā"):
        T[_st + _e] = f"{_name} से शुरू होने वाली शृंखला"
        T[_neg + _st + _e] = f"{_name} के अभाव से शुरू होने वाली शृंखला"
T["avigatanti"] = "अविलीनता-कारण"
T["sahajāta"] = ("सह-उत्पत्ति-कारण", "सह-उत्पन्न", "सह-उत्पत्ति")
T["atthi"] = "उपस्थिति-कारण"
T["āsevanaṃ"] = "पुनरावृत्ति-कारण"                  # «Vipākamūlake āsevanaṃ natthi» «… पुनरावृत्ति-कारण नहीं है»
T["paccayaṃ"] = "कारण"                               # «Ekekaṃ paccayaṃ mūlakaṃ kātūna» «एक-एक कारण को»
T["gaṇanā"] = "गणना"

# fused pairs in the dvanda lists (text «X-कारण, प्रधानता-कारण»; comma dropped)
for _p, _h in (("het", "मूल-कारण"), ("āhār", "आहार-कारण"), ("indriy", "क्षमता-कारण")):
    T[_p + "ādhipati"] = (f"{_h} प्रधानता-कारण",)
T["ārammaṇādhipati"] = ("विषय रूपी प्रधानता", "विषय-कारण प्रधानता-कारण")
T["kusalādhipati"] = "हितकर प्रधानता"
T["akusalādhipati"] = "हानिकर प्रधानता"
T["sampayuttādhipati"] = "जुड़ी प्रधानता"          # «सुखद अनुभूति से जुड़ी प्रधानता» (1-02)
# «Sa-X-ghaṭanā» headings «X-कारण … सहित संयोजन»
T.update({
    "sādhipati": "प्रधानता-कारण … सहित", "saindriya": "क्षमता-कारण … सहित", "sajhāna": "ध्यान-कारण … सहित",
    "sahetādhipati": "मूल-कारण प्रधानता-कारण … सहित",
})

# numbers
T.update({
    "ekaṃ": "एक", "dve": "दो", "tīṇi": "तीन", "cattāri": "चार", "pañca": "पाँच", "cha": "छह", "satta": "सात",
    "aṭṭha": "आठ", "nava": "नौ", "dasa": "दस", "ekādasa": "ग्यारह", "dvādasa": "बारह", "terasa": "तेरह",
    "cuddasa": "चौदह", "pannarasa": "पंद्रह", "soḷasa": "सोलह", "sattarasa": "सत्रह", "aṭṭhārasa": "अठारह",
    "ekūnavīsati": "उन्नीस", "vīsati": "बीस", "ekavīsati": "इक्कीस", "bāvīsati": "बाईस", "tevīsati": "तेईस",
    "soḷasakaṃ": "सोलह कारणों का मेल", "catuvīsakaṃ": "चौबीस कारणों का मेल",
})

# triad items and their compounds
for _e in ("aṃ", "o", "ā", "assa", "ānaṃ", "e", "āni", "a"):
    # «कर्म के फल रूपी या/और केवल क्रिया रूपी नैतिक रूप से अनिर्धारित» = the discontinuous form
    T["vipākābyākat" + _e] = ("कर्म के फल रूपी नैतिक रूप से अनिर्धारित", "कर्म-फल रूपी नैतिक रूप से अनिर्धारित",
                              "कर्म के फल रूपी … नैतिक रूप से अनिर्धारित")
    T["kiriyābyākat" + _e] = "केवल क्रिया रूपी नैतिक रूप से अनिर्धारित"
for _p, _h in (("vicikicchā", "संशय"), ("uddhacca", "बेचैनी"), ("dukkha", "दुःख"), ("sukha", "सुख"),
               ("kāyaviññāṇa", "शरीर की चेतना"), ("pañcaviññāṇa", "पाँच प्रकार की चेतना"),
               ("catuviññāṇa", "चार प्रकार की चेतना")):
    for _e in ("aṃ", "o", "ā", "e", "assa", "ānaṃ"):
        T[_p + "sahagat" + _e] = f"{_h} के साथ होने वाला"
T.update({
    "kusalattikassa": "हितकर वाला तीन का वर्गीकरण",
    "kusalacittasamaṅgissa": "हितकर मन से युक्त व्यक्ति", "akusalacittasamaṅgissa": "हानिकर मन से युक्त व्यक्ति",
    "vipākābyākatakiriyābyākatacittasamaṅgissa":
        "कर्म के फल रूपी या केवल क्रिया रूपी नैतिक रूप से अनिर्धारित मन से युक्त व्यक्ति",
    "sampayuttacittasamaṅgissa": "जुड़े मन से युक्त व्यक्ति",
    "nevasaññānāsaññāyatanakusalaṃ": "न पहचान न अ-पहचान के क्षेत्र का हितकर मन",
    "nevasaññānāsaññāyatanakiriyaṃ": "न पहचान न अ-पहचान के क्षेत्र का केवल क्रिया रूपी मन",
    "nevasaññānāsaññāyatanaṃ": "न पहचान न अ-पहचान का क्षेत्र",
    "viññāṇañcāyatanavipākassa": "अनंत चेतना के क्षेत्र का कर्म के फल रूपी मन",
    "viññāṇañcāyatanakiriyassa": "अनंत चेतना के क्षेत्र का केवल क्रिया रूपी मन",
    "kiriyassa": "केवल क्रिया रूपी मन", "kiriyaṃ": ("केवल क्रिया रूपी मन", "केवल क्रिया रूपी"),
    "vipākamanodhātu": "कर्म के फल रूपी मन का तत्व", "vipākamanodhātuyā": "कर्म के फल रूपी मन का तत्व",
    "vipākamanoviññāṇadhātu": "कर्म के फल रूपी मन की चेतना का तत्व",
    "vipākamanoviññāṇadhātuyā": "कर्म के फल रूपी मन की चेतना का तत्व",
    "kiriyamanoviññāṇadhātuyā": "केवल क्रिया रूपी मन की चेतना का तत्व",
    "upapatticittassa": "जन्म का मन", "cuticittaṃ": "मृत्यु का मन",
    "bhavaṅgaṃ": "जीवन-धारा", "bhavaṅgassa": "जीवन-धारा", "āvajjanā": "मन को विषय की ओर मोड़ना",
    "vuṭṭhānassa": "बाहर आना", "phalā": "फल", "sekkhāya": "सीखने के चरण वाला",
    "sekkhā": ("सीखने के चरण वाला", "सीखने के चरण का"),
})

# Pañhāvāra vocabulary (ārammaṇa / adhipati / upanissaya examples)
T.update({
    "arahā": "अर्हत्", "puthujjanā": "साधारण व्यक्ति", "ariyā": "आर्य",
    "vipassanti": "अंतर्दृष्टि से देखना", "suṇanti": "सुनना", "passanti": "देखना",
    "gotrabhuṃ": "गोत्र-परिवर्तन", "nibbānaṃ": "निर्वाण",
    "cetopariyañāṇena": "दूसरों के मन को जानने का ज्ञान",
    "niruddhe": "समाप्त होना", "tadārammaṇatā": "उसी विषय को लेकर",
    "parihīne": "छूट जाना", "vippaṭisārissa": "ग्लानि से भरा व्यक्ति",
    "moho": "मोह", "mohaṃ": "मोह", "mohassa": "मोह", "doso": "द्वेष", "dosaṃ": "द्वेष", "dosassa": "द्वेष",
    "paṭhamassa": "पहला", "dutiyassa": "दूसरा", "tatiyassa": "तीसरा", "catutthassa": "चौथा",
    "parikammaṃ": "प्रारंभिक तैयारी",
    "ākāsānañcāyatanassa": "अनंत आकाश का क्षेत्र", "ākiñcaññāyatanassa": "कुछ भी न होने का क्षेत्र",
    "dibbassa": "दिव्य", "cakkhussa": "आँख", "dibbacakkhu": "दिव्य आँख", "dibbasotadhātu": "दिव्य कान का तत्व",
    "anuppannaṃ": "अब तक उत्पन्न न हुआ", "uppannaṃ": "उत्पन्न हो चुका",
    "uppādenti": "उत्पन्न करना", "samāpajjanti": "प्रवेश करना", "samāpajjati": "प्रवेश करना",
    "saṅkhāre": "निर्मित परिघटना",
    "atthappaṭisambhidāya": "अर्थ का विश्लेषणात्मक ज्ञान", "dhammappaṭisambhidāya": "शिक्षा का विश्लेषणात्मक ज्ञान",
    "niruttippaṭisambhidāya": "भाषा का विश्लेषणात्मक ज्ञान",
    "paṭibhānappaṭisambhidāya": "प्रत्युत्पन्न बुद्धि का विश्लेषणात्मक ज्ञान",
    "ṭhānāṭhānakosallassa": "संभव और असंभव को जानने की कुशलता",
    "attānaṃ": "स्वयं", "ātāpeti": "तपाना", "paritāpeti": "संतप्त करना", "pariyiṭṭhimūlakaṃ": "खोज से उत्पन्न",
    "paccanubhoti": "भोगना", "vipākassa": "कर्म-फल", "kiriyasamāpattiṃ": "केवल क्रिया रूपी ध्यान-अवस्था",
    "adinnaṃ": "बिना दिया हुआ", "ādiyati": "लेना", "musā": "झूठ", "bhaṇati": "बोलना", "pisuṇaṃ": "चुगली",
    "pharusaṃ": "कठोर वचन", "samphaṃ": "व्यर्थ", "palapati": "बकवास करना", "sandhiṃ": "सेंध",
    "chindati": "लगाना", "nillopaṃ": "डाका", "harati": "डालना", "ekāgārikaṃ": "किसी एक घर को लूटना",
    "paripanthe": "राह", "tiṭṭhati": "घात लगाना", "paradāraṃ": "पराई स्त्री", "gāmaghātaṃ": "गाँव लूटना",
    "nigamaghātaṃ": "कस्बा लूटना", "mātaraṃ": "माता", "pitaraṃ": "पिता", "arahantaṃ": "अर्हत्",
    "jīvitā": "जान", "duṭṭhena": "दुष्ट", "cittena": "मन", "tathāgatassa": "तथागत", "lohitaṃ": "रक्त",
    "pāṇātipāto": "जीव-हत्या", "pāṇātipātassa": "जीव-हत्या",
    "adinnādānaṃ": "बिना दिया हुआ लेना", "adinnādānassa": "बिना दिया हुआ लेना",
    "kāmesumicchācārassa": "इंद्रिय-सुखों में दुराचार", "musāvādassa": "झूठ बोलना", "vācāya": "वचन",
    "samphappalāpassa": "व्यर्थ की बकवास", "abhijjhāya": "लालच", "byāpādassa": "दुर्भावना",
    "pisuṇavācā": "चुगली", "pharusavācā": "कठोर वचन",
    "niyatamicchādiṭṭhiyā": "नियत ग़लत दृष्टि", "niyatamicchādiṭṭhi": "नियत ग़लत दृष्टि",
    "mātughātikammaṃ": "माता की हत्या का कर्म", "mātughātikammassa": "माता की हत्या का कर्म",
    "pitughātikammaṃ": "पिता की हत्या का कर्म", "pitughātikammassa": "पिता की हत्या का कर्म",
    "arahantaghātikammaṃ": "अर्हत् की हत्या का कर्म", "arahantaghātikammassa": "अर्हत् की हत्या का कर्म",
    "ruhiruppādakammaṃ": "रक्त बहाने का कर्म", "ruhiruppādakammassa": "रक्त बहाने का कर्म",
    "saṅghabhedakammaṃ": "संघ में फूट डालने का कर्म", "saṅghabhedakammassa": "संघ में फूट डालने का कर्म",
    "cakkaṃ": "चक्र", "bandhitabbaṃ": "बाँधना चाहिए", "kātabbaṃ": ("बनाना चाहिए", "करना चाहिए"),
    "kātabbo": "करना चाहिए",
    "hantvā": "हत्या करके", "paṭighātatthāya": "प्रतिकार", "ādiyitvā": "लेकर", "bhaṇitvā": "बोलकर",
    "uppādetvā": "बहाकर", "bhinditvā": "फूट डालकर",
    "saddhāpañcamakesu": "श्रद्धा आदि पाँच",
    "cāgaṃ": "त्याग", "āhāraṃ": "आहार", "indriyaṃ": "क्षमता",     # labels «सह-उत्पत्ति, …, आहार, क्षमता»
    "sutaṃ": "सुना-सीखा ज्ञान",
    "mūlakaṃ": "शृंखला",                               # «(mūlakaṃ saṃkhittaṃ)» «(शृंखला संक्षिप्त)»
    # 1-02 renders the same Pañhāvāra list with other words: the value follows each segment's Hindi
    "pāṇaṃ": ("जीव", "प्राणी"), "adinnaṃ": ("बिना दिया हुआ", "बिना दी हुई वस्तु"),
    "ekāgārikaṃ": ("किसी एक घर को लूटना", "एक ही घर को लूटना"),
    "gāmaghātaṃ": ("गाँव लूटना", "गाँव को लूटना"), "nigamaghātaṃ": ("कस्बा लूटना", "कस्बे को लूटना"),
    "paritāpeti": ("संतप्त करना", "कष्ट देना"),
    "pariyiṭṭhimūlakaṃ": ("खोज से उत्पन्न", "खोज के कारण होने वाला"), "lohitaṃ": ("रक्त", "खून"),
    "paripuṇṇaṃ": ("पूर्ण", "पूरा"), "sampayuttakānaṃ": ("जुड़ा हुआ", "जुड़ा"),
    "gaṇitā": "गणना … की गई",                          # «… की गणना पाठ के क्रम से की गई है»
    # «vipākaṃ natthi / Vipākaṃ ṭhapetvā» «कर्म-फल-कारण …»
    "vipākaṃ": ("कर्म-फल रूपी", "कर्म के फल रूपी", "कर्म-फल-कारण"),
    "vipāko": ("कर्म-फल रूपी", "कर्म के फल रूपी", "कर्म-फल"),
})

# instructions, counting frames
T.update({
    "avasesāni": "बाकी", "avasesesu": "बाकी", "padāni": "पद", "vitthāretabbāni": "विस्तार करना चाहिए",
    "ekasadisāni": "एक जैसा", "ṭhitena": "टिके रहना",
    "sajjhāyantena": "पाठ करते हुए", "sajjhāyamaggena": "पाठ का क्रम",
    "gaṇite": "गिनना",
    "anulomagaṇanā": "सकारात्मक क्रम की गणना", "paccanīyagaṇanā": "नकारात्मक क्रम की गणना",
    "anulomapaccanīyagaṇanā": "सकारात्मक-नकारात्मक क्रम की गणना",
    "paccanīyānulomagaṇanā": "नकारात्मक-सकारात्मक क्रम की गणना",
})

OVR = {
    "1-01-kusalattika": {
        "7-2-406": {"vipāko": "कर्म-फल"},        # «vipāko tadārammaṇatā uppajjati» «कर्म-फल उसी विषय को लेकर …»
        "7-2-201": {"paccayā": "कारण"},           # «naaññamañña-paccayā» (split compound) «परस्पर-कारण के बिना»
        "7-2-339": {"adhipati": "प्रधानता"},      # «(adhipati paṭisandhikkhaṇe natthi.)» «(… प्रधानता नहीं है।)»
        "7-2-423": {"upanissaya": "प्रबल आश्रय से"},  # «paññaṃ upanissaya dānaṃ deti» = upanissāya «प्रज्ञा के प्रबल आश्रय से»
    },
    "1-02-vedanattika": {},
}
_PADA = "पद: text «पदों» (regular plural); the pi-1 checker matches 2-letter words only exactly"
ALLOWED = {"1-01-kusalattika": {("7-2-386", "padāni"): _PADA, ("7-U113", "padāni"): _PADA},
           "1-02-vedanattika": {}}
