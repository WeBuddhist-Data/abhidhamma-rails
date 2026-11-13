"""pi-7 Paṭṭhāna, Hindi plain RAILS: builder for 2-01 vitakkattika, 2-02 pitittika, 2-03 dassanenapahatabbattika.

Imports the approved sample builder read-only for every shared formula string.
  python -I -B -X utf8 build_rails_2-01_2-03.py          -> build the three files
  python -I -B -X utf8 build_rails_2-01_2-03.py --check  -> list untranslated pieces, write nothing
"""
import os
import re
import sys
from collections import Counter

RAILS = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, RAILS)
import build_rails_sample as S  # noqa: E402  (read-only import)

FILES = ["2-01-vitakkattika.md", "2-02-pitittika.md", "2-03-dassanenapahatabbattika.md"]

# ============================================================ items of the three triads

ITEM_KEYS = ["NN", "DA", "BH", "SV", "VM", "AV", "PI", "SU", "UP"]


def ITEM_HI(key, agr):
    """agr: 'm' masc sg direct, 'o' masc oblique / masc pl, 'f' fem."""
    if "+" in key:
        ks = key.split("+")
        hs = [ITEM_HI(k, agr) for k in ks]
        return hs[0] + " और " + hs[1] if len(hs) == 2 else ", ".join(hs[:-1]) + " और " + hs[-1]
    v = {"m": "वाला", "o": "वाले", "f": "वाली"}[agr]
    j = {"m": "छोड़ा जाने वाला", "o": "छोड़े जाने वाले", "f": "छोड़ी जाने वाली"}[agr]
    return {
        "SV": f"आरंभिक विचार और सतत विचार {v}",
        "VM": f"आरंभिक विचार से रहित, केवल सतत विचार {v}",
        "AV": "आरंभिक विचार और सतत विचार दोनों से रहित",
        "PI": f"उल्लास के साथ होने {v}",
        "SU": f"सुख के साथ होने {v}",
        "UP": f"समभाव के साथ होने {v}",
        "DA": f"सत्य-दर्शन से {j}",
        "BH": f"मानसिक अभ्यास से {j}",
        "NN": f"न सत्य-दर्शन से, न मानसिक अभ्यास से {j}",
    }[key]


STEM_RX = (r"(neva dassanena na bhāvanāya pahātabb|nevadassanena nabhāvanāya pahātabb|dassanena pahātabb|"
           r"bhāvanāya pahātabb|savitakkasavicār|avitakkavicāramatt|avitakkaavicār|pītisahagat|sukhasahagat|"
           r"upekkhāsahagat)")
STEM_KEY = {"neva dassanena na bhāvanāya pahātabb": "NN", "nevadassanena nabhāvanāya pahātabb": "NN",
            "dassanena pahātabb": "DA", "bhāvanāya pahātabb": "BH", "savitakkasavicār": "SV",
            "avitakkavicāramatt": "VM", "avitakkaavicār": "AV", "pītisahagat": "PI", "sukhasahagat": "SU",
            "upekkhāsahagat": "UP"}
ITEM_RX = re.compile(r"(?<![\w])" + STEM_RX + r"(ānaṃ|assa|āya|ena|āni|aṃ|o|ā|e|a)(?![\w])")

# ============================================================ triad-specific headings

HEAD = dict(S.HEAD)
HEAD.update({
    "(Dutiyo bhāgo)": "(दूसरा भाग)",
    "Vitakkattikaṃ": "आरंभिक विचार वाला तीन का वर्गीकरण",
    "Pītittikaṃ": "उल्लास वाला तीन का वर्गीकरण",
    "Dassanenapahātabbattikaṃ": "सत्य-दर्शन से छोड़ी जाने वाली परिघटनाओं वाला तीन का वर्गीकरण",
    "Sahajātavāro": "सह-उत्पत्ति का खंड",
    "Paccayavāro": "कारण का खंड",
    "Nissayavāro": "आश्रय का खंड",
    "Saṃsaṭṭhavāro": "घुले-मिले होने का खंड",
    "Sampayuttavāro": "जुड़ाव का खंड",
    "2-6. Sahajāta-paccaya-nissaya-saṃsaṭṭha-sampayuttavāro": "2-6. सह-उत्पत्ति, कारण, आश्रय, घुले-मिले होने और जुड़ाव का खंड",
    "1-4. Paccayānulomādi": "1-4. कारणों का सकारात्मक क्रम आदि",
    "Paccayānulomādi": "कारणों का सकारात्मक क्रम आदि",
    "Paccanīyuddhāro": "नकारात्मक क्रम के लिए कारणों की छँटाई",
    "Atthi-avigatapaccayā": f"{S.NAME['atthi']} और {S.NAME['avigata']}",
    "Natthivigatāvigatapaccayā": f"{S.NAME['natthi']}, {S.NAME['vigata']} और {S.NAME['avigata']}",
    "Aññamañña-nissayapaccayā": f"{S.NAME['aññamañña']} और {S.NAME['nissaya']}",
    "Naadhipati-naāsevanapaccayā": f"{S.NNAME['adhipati']} और {S.NNAME['āsevana']}",
    "Ārammaṇapaccayādi": f"{S.NAME['ārammaṇa']} आदि",
    "Adhipatipaccayādi": f"{S.NAME['adhipati']} आदि",
    "Aññamaññapaccayādi": f"{S.NAME['aññamañña']} आदि",
    "Nissayapaccayādi": f"{S.NAME['nissaya']} आदि",
    "Āhārapaccayādi": f"{S.NAME['āhāra']} आदि",
    "Naanantarapaccayādi": f"{S.NNAME['anantara']} आदि",
    "Naadhipatipaccayādi": f"{S.NNAME['adhipati']} आदि",
    "Napacchājātapaccayādi": f"{S.NNAME['pacchājāta']} आदि",
    "Navipākapaccayādi": f"{S.NNAME['vipāka']} आदि",
    "Najhānapaccayādi": f"{S.NNAME['jhāna']} आदि",
    "Hetudukaṃ": S.DUKA["hetu"],
    "Nahetudukaṃ": S.NDUKA["hetu"],
})

# ============================================================ editorial notes (inside the parentheses)

KT = "हितकर वाले तीन के वर्गीकरण"          # kusalattike / kusalattika- (oblique)
SVM = "आरंभिक विचार और सतत विचार वाली परिघटना से शुरू होने वाले"
VMM = "आरंभिक विचार से रहित, केवल सतत विचार वाली परिघटना से शुरू होने वाले"
VMP = "आरंभिक विचार से रहित, केवल सतत विचार वाली परिघटना"
NOTE = {
    '"arūpe"ti niyāmetabbaṃ "paṭisandhikkhaṇe"ti ca': "“अभौतिक लोक में” और “पुनर्जन्म के क्षण में” निश्चित करना चाहिए",
    "anantarapaccayasadisaṃ": S.SADISA["anantara"],
    "anantarapaccayopi samanantarapaccayopi sadiso": f"{S.NAME['anantara']} और {S.NAME['samanantara']} भी समान हैं",
    "anantarasadisaṃ": S.SADISA["anantara"],
    "Anulomapaccanīyagaṇanā iminā kāraṇena gaṇetabbā.": "सकारात्मक-नकारात्मक क्रम की गणना इस तरीके से गिननी चाहिए।",
    "Anulomapaccanīyaṃ anumajjantena gaṇetabbaṃ.": "सकारात्मक-नकारात्मक क्रम को अनुसरण करते हुए गिनना चाहिए।",
    "Anulomapaccanīyaṃ vitthārena gaṇetabbaṃ.": "सकारात्मक-नकारात्मक क्रम को विस्तार से गिनना चाहिए।",
    "ārammaṇapaccayasadisaṃ": S.SADISA["ārammaṇa"],
    "ārammaṇasadisaṃ": S.SADISA["ārammaṇa"],
    "āsevane vipākaṃ natthi": f"{S.LOC['āsevana']} कर्म-फल नहीं है",
    "avasesā hetupaccayasadisā": f"शेष {S.SADISA['hetu']} हैं",
    "Avasesesu dvīsu ghaṭanesu pavatti paṭisandhi vitthāretabbā.": "बाकी दो संयोजनों में जीवन-काल और पुनर्जन्म का विस्तार करना चाहिए।",
    "Avitakkavicāramattamūlakā pañca pañhā iminā kāraṇena vibhajitabbā.": f"{VMM} पाँच प्रश्नों का इस तरीके से विश्लेषण करना चाहिए।",
    "Avitakkavicāramattamūlakā pañca pañhā kātabbā, vipākanti niyāmetabbā.": f"{VMM} पाँच प्रश्न करने चाहिए, “कर्म-फल” निश्चित करना चाहिए।",
    "Avitakkavicāramattamūlakā pañca pañhā. Avasesā sahajātapaccayasadisā.": f"{VMM} पाँच प्रश्न हैं। शेष {S.SADISA['sahajāta']} हैं।",
    "cattāri kātabbāni, pītisahagataṃ anumajjantena vibhajitabbaṃ": "चार करने चाहिए, उल्लास के साथ होने वाली परिघटना का अनुसरण करते हुए विश्लेषण करना चाहिए",
    "cattāripi gaṇanāni passitvā kātabbāni": "चारों गणनाएँ देखकर करनी चाहिए",
    "dasa pañhā kātabbā": "दस प्रश्न करने चाहिए",
    "dasa pañhā vitthāretabbā": "दस प्रश्नों का विस्तार करना चाहिए",
    "dassanena sadisaṃ kātabbaṃ": "सत्य-दर्शन से छोड़ी जाने वाली परिघटना के समान करना चाहिए",
    "Dve paccayā sajjhāyamaggena vibhattā, evaṃ avasesā vīsatipaccayā vibhajitabbā.": "दो कारणों का पाठ के क्रम से विश्लेषण किया गया है, इसी तरह शेष बीस कारणों का विश्लेषण करना चाहिए।",
    "dve pañhā kātabbā": "दो प्रश्न करने चाहिए",
    "dve vārā vitthāretabbā": "दो खंडों का विस्तार करना चाहिए",
    "Evaṃ anulomagaṇanā gaṇetabbā.": "इसी तरह सकारात्मक क्रम की गणना गिननी चाहिए।",
    "Evaṃ anumajjantena gaṇetabbaṃ.": "इसी तरह अनुसरण करते हुए गिनना चाहिए।",
    "evaṃ gaṇetabbaṃ ": "इसी तरह गिनना चाहिए",
    "evaṃ gaṇetabbaṃ": "इसी तरह गिनना चाहिए",
    "evaṃ paṭisandhikkhaṇe cattāro": "इसी तरह पुनर्जन्म के क्षण में चार",
    "Ghaṭanā kusalattikasadisāyeva. Pañhāvāragaṇanaṃ evaṃ asammohantena gaṇetabbaṃ.":
        f"संयोजन {KT} के समान ही हैं। प्रश्नों के खंड की गणना इसी तरह बिना भ्रमित हुए गिननी चाहिए।",
    "Hetupaccayaṃ anumajjantena paccayavāro vitthāretabbo. Yathā paṭiccagaṇanā evaṃ gaṇetabbā. Adhipatiyā sattatiṃsa, purejāte ca āsevane ca ekavīsa, ayaṃ ettha viseso.":
        f"{S.NAME['hetu']} का अनुसरण करते हुए कारण के खंड का विस्तार करना चाहिए। जैसे निर्भरता के खंड की गणना है, वैसे ही गिनना चाहिए। "
        f"{S.LOC['adhipati']} सैंतीस, {S.LOC['purejāta']} और {S.LOC['āsevana']} इक्कीस, यही यहाँ अंतर है।",
    "Hetupaccayaṃ anumajjantena sabbe paccayā vitthāretabbā": f"{S.NAME['hetu']} का अनुसरण करते हुए सभी कारणों का विस्तार करना चाहिए",
    "hetupaccayasadisaṃ": S.SADISA["hetu"],
    "idampi dassanena sadisaṃ": "यह भी सत्य-दर्शन से छोड़ी जाने वाली परिघटना के समान है",
    "imāni padāni anumajjantena anulomaṃ gaṇetabbaṃ": "इन पदों का अनुसरण करते हुए सकारात्मक क्रम को गिनना चाहिए",
    "Iminā kāraṇena dasa pañhā vitthāretabbā.": "इस तरीके से दस प्रश्नों का विस्तार करना चाहिए।",
    "Iminā kāraṇena sabbesaṃ padānaṃ paccayoti dīpetabbo": "इस तरीके से सभी पदों के लिए “कारण” दिखाना चाहिए",
    "kammapaccayasadisaṃ": S.SADISA["kamma"],
    "Kusalattikaṃ anulomaṃ anumajjantena gaṇetabbaṃ.": f"{KT} के सकारात्मक क्रम का अनुसरण करते हुए गिनना चाहिए।",
    "kusalattike vippayuttapaccayasadisaṃ": f"{KT} में {S.SADISA['vippayutta']}",
    "naadhipatipaccayasadisaṃ, paṭisandhi natthi": f"{S.NSADISA['adhipati']}, पुनर्जन्म नहीं है",
    "naadhipatipaṭisandhikkhaṇe paripuṇṇaṃ": f"{S.NLOC['adhipati']} पुनर्जन्म के क्षण में परिपूर्ण",
    "naārammaṇasadisaṃ": S.NSADISA["ārammaṇa"],
    "Naāsevanamūlake avitakkavicāramattaṃ vipākena saha gacchantena napurejātasadisaṃ kātabbaṃ, avitakkavicāramattañca avitakkavicāramattagacchantena vipāko dassetabbo.":
        f"{S.NAME['āsevana']} के अभाव से शुरू होने वाली शृंखला में {VMP} को कर्म-फल के साथ लेते हुए "
        f"{S.NSADISA['purejāta']} करना चाहिए, और {VMP} को {VMP} के साथ लेते हुए कर्म-फल दिखाना चाहिए।",
    "Namaggapaccayā nahetupaccayasadisaṃ. Moho natthi. Navippayuttapaccayā paripuṇṇaṃ arūpapañhameva.":
        f"{S.NABL['magga']} {S.NSADISA['hetu']} है। मोह नहीं है। {S.NABL['vippayutta']} परिपूर्ण है, केवल अभौतिक लोक का प्रश्न है।",
    "Napurejātamūlake yathā suddhikaṃ arūpaṃ, tathā arūpā kātabbā":
        f"{S.NAME['purejāta']} के अभाव से शुरू होने वाली शृंखला में जैसे अकेले कारण वाले खंड में अभौतिक लोक है, "
        "वैसे ही अभौतिक लोक के प्रश्न करने चाहिए",
    "Natthipaccayañca vigatapaccayañca anantarasadisaṃ, avigataṃ atthisadisaṃ.":
        f"{S.NAME['natthi']} और {S.NAME['vigata']} {S.SADISA['anantara']} हैं, {S.NAME['avigata']} {S.SADISA['atthi']} है।",
    "natthipi vigatampi anantarasadisaṃ": f"{S.NAME['natthi']} और {S.NAME['vigata']} भी {S.SADISA['anantara']} हैं",
    "Ñatvā gaṇetabbaṃ.": "जानकर गिनना चाहिए।",
    "Navipāke sattatiṃsa pañhā kātabbā. Naāhāra-naindriya-najhāna-namagga-nasampayuttanavippayutta-nonatthi-novigatapaccayā vitthāretabbā.":
        f"{S.NLOC['vipāka']} सैंतीस प्रश्न करने चाहिए। {S.NAME['āhāra']} के अभाव, {S.NAME['indriya']} के अभाव, "
        f"{S.NAME['jhāna']} के अभाव, {S.NAME['magga']} के अभाव, {S.NAME['sampayutta']} के अभाव, {S.NAME['vippayutta']} के अभाव, "
        f"{S.NAME['natthi']} के अभाव और {S.NAME['vigata']} के अभाव का विस्तार करना चाहिए।",
    "Nissayampi ninnānaṃ": "आश्रय का खंड भी बिना किसी अंतर के है",
    "Nissayavāro paccayasadiso kātabbo.": "आश्रय का खंड कारण के खंड के समान करना चाहिए।",
    "Paccanīyaṃ anumajjantena gaṇetabbaṃ.": "नकारात्मक क्रम को अनुसरण करते हुए गिनना चाहिए।",
    "Paccanīyaṃ gaṇentena imāni padāni anumajjantena gaṇetabbāni.": "नकारात्मक क्रम को गिनते समय इन पदों का अनुसरण करते हुए गिनना चाहिए।",
    "Paccanīyaṃ kātabbaṃ asammohantena.": "नकारात्मक क्रम बिना भ्रमित हुए करना चाहिए।",
    "paccanīyaṃ paripuṇṇaṃ kātabbaṃ": "नकारात्मक क्रम परिपूर्ण करना चाहिए",
    "Paccanīyānulomaṃ anumajjantena gaṇetabbaṃ.": "नकारात्मक-सकारात्मक क्रम को अनुसरण करते हुए गिनना चाहिए।",
    "Paccanīyānulomaṃ iminā kāraṇena vibhajitabbaṃ.": "नकारात्मक-सकारात्मक क्रम का इस तरीके से विश्लेषण करना चाहिए।",
    "paripuṇṇaṃ hetupaccayasadisaṃ": f"परिपूर्ण, {S.SADISA['hetu']}",
    "paripuṇṇaṃ kātabbaṃ": "परिपूर्ण करना चाहिए",
    "paripuṇṇaṃ, ajjhattikā mahābhūtā ca āhārasamuṭṭhānañca": "परिपूर्ण, आंतरिक महाभूत और आहार से उत्पन्न भौतिक रूप",
    "paripuṇṇaṃ, paṭisandhi natthi": "परिपूर्ण, पुनर्जन्म नहीं है",
    "paripuṇṇaṃ. Ajjhattikā ca asaññasattānañca mahābhūtā": "परिपूर्ण। आंतरिक महाभूत और पहचान-रहित प्राणियों के महाभूत",
    "Paṭhamaghaṭanāyaṃ sampuṇṇā satta pañhā kātabbā.": "पहले संयोजन में पूरे सात प्रश्न करने चाहिए।",
    "paṭhamaudāharaṇe pavatte paṭisandhikkhaṇe satta pañhā kātabbā": "पहले उदाहरण में जीवन-काल में और पुनर्जन्म के क्षण में सात प्रश्न करने चाहिए",
    "paṭiccasadisaṃ sahajāte dasa pañhā": f"निर्भरता के खंड के समान, {S.LOC['sahajāta']} दस प्रश्न",
    "paṭiccavārasadisā": "निर्भरता के खंड के समान",
    "paṭisandhi natthi": "पुनर्जन्म नहीं है",
    "paṭisandhi natthi, vipākañca": "पुनर्जन्म नहीं है, और कर्म-फल भी नहीं",
    "paṭisandhikāni cattāri. Saṃkhittaṃ": "पुनर्जन्म वाले चार। संक्षिप्त",
    "paṭisandhikkhaṇe natthi": "पुनर्जन्म के क्षण में नहीं है",
    "Paṭisandhikkhaṇe pañca pañhā kātabbā. Yattha avitakkavicāramattaṃ āgacchati tattha vipākaṃ kātabbaṃ. Naadhipatimūlake sattatiṃsa pañhā kātabbā.":
        f"पुनर्जन्म के क्षण में पाँच प्रश्न करने चाहिए। जहाँ {VMP} आती है, वहाँ कर्म-फल करना चाहिए। "
        f"{S.NAME['adhipati']} के अभाव से शुरू होने वाली शृंखला में सैंतीस प्रश्न करने चाहिए।",
    "pavattipi, paṭisandhipi dīpetabbā": "जीवन-काल भी, पुनर्जन्म भी दिखाना चाहिए",
    "purejāte paṭisandhikkhaṇe natthi": f"{S.LOC['purejāta']} पुनर्जन्म का क्षण नहीं है",
    "sabbāni padāni vitthāretabbāni tīṇi, tīṇi": "सभी पदों का विस्तार करना चाहिए, तीन, तीन",
    "sahajātapaccayasadisaṃ": S.SADISA["sahajāta"],
    "sahajātasadisaṃ": S.SADISA["sahajāta"],
    "Sahajātavāro paṭiccavārasadiso.": "सह-उत्पत्ति का खंड निर्भरता के खंड के समान है।",
    "Sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi paṭiccavārasadisā.":
        "सह-उत्पत्ति का खंड, कारण का खंड, आश्रय का खंड, घुले-मिले होने का खंड और जुड़ाव का खंड भी निर्भरता के खंड के समान हैं।",
    "Sahajātavāropi paṭiccavārasadiso kātabbo.": "सह-उत्पत्ति का खंड भी निर्भरता के खंड के समान करना चाहिए।",
    "saṃkhittaṃ": "संक्षिप्त",
    "saṃkhittaṃ. Pītinayaṃ passitvā kātabbaṃ": "संक्षिप्त। उल्लास वाली विधि को देखकर करना चाहिए",
    "sampayuttavāro saṃsaṭṭhavārasadiso": "जुड़ाव का खंड घुले-मिले होने के खंड के समान है",
    "Sampayuttavāropi vitthāretabbo": "जुड़ाव के खंड का भी विस्तार करना चाहिए",
    "Savitakkasavicāramūlakā iminā kāraṇena satta pañhā vibhajitabbā.": f"{SVM} सात प्रश्नों का इस तरीके से विश्लेषण करना चाहिए।",
    "Savitakkasavicāramūlakā satta pañhā iminā kāraṇena vibhajitabbā.": f"{SVM} सात प्रश्नों का इस तरीके से विश्लेषण करना चाहिए।",
    "Savitakkasavicāramūlakā sattapi pañhā paripuṇṇā.": f"{SVM} सातों प्रश्न परिपूर्ण हैं।",
    "Savitakkasavicāramūlake avasesā pañhā sahajātapaccayasadisā.":
        f"आरंभिक विचार और सतत विचार वाली परिघटना से शुरू होने वाली शृंखला में शेष प्रश्न {S.SADISA['sahajāta']} हैं।",
    "sukhamūle tīṇi": "सुख के साथ होने वाली परिघटना से शुरू होने वाली शृंखला में तीन",
    "Tāniyeva ca gamanāni niyāmetabbāni.": "और वे ही प्रसंग निश्चित करने चाहिए।",
    "vipākapaṭisandhi natthi": "कर्म-फल और पुनर्जन्म नहीं है",
    "Yathā kusalattike anulomapaccanīyagaṇanā, evaṃ gaṇetabbaṃ.": f"जैसे {KT} में सकारात्मक-नकारात्मक क्रम की गणना है, वैसे ही गिनना चाहिए।",
    "Yathā kusalattike gaṇanā, evaṃ gaṇetabbaṃ": f"जैसे {KT} में गणना है, वैसे ही गिनना चाहिए",
    "Yathā kusalattike paccanīyagaṇanā, evaṃ gaṇetabbaṃ.": f"जैसे {KT} में नकारात्मक क्रम की गणना है, वैसे ही गिनना चाहिए।",
    "Yathā kusalattike paccanīyānulomagaṇanā, evaṃ gaṇetabbaṃ.": f"जैसे {KT} में नकारात्मक-सकारात्मक क्रम की गणना है, वैसे ही गिनना चाहिए।",
    "yathā paṭiccanaye tathā pañca pañhā kātabbā": "जैसे निर्भरता की विधि में, वैसे ही पाँच प्रश्न करने चाहिए",
    "Yathā paṭiccavāre hetupaccaye evaṃ vitthāretabbā dasa pañhā.": f"जैसे निर्भरता के खंड में {S.LOC['hetu']}, वैसे ही दस प्रश्नों का विस्तार करना चाहिए।",
}

# ============================================================ whole lines translated by hand

NL = S.NLOC
LINE = {
    "Paccanīye – nahetuyā tettiṃsa pañhā, sattasu ṭhānesu satta mohā uddharitabbā mūlapadesuyeva. Naārammaṇe satta cittasamuṭṭhānā uddharitabbā.":
        f"नकारात्मक क्रम में – {NL['hetu']} तैंतीस प्रश्न हैं, सात स्थानों में सात मोह निकालने चाहिए, केवल मूल पदों में ही। "
        f"{NL['ārammaṇa']} सात मन से उत्पन्न भौतिक रूप निकालने चाहिए।",
    "Savitakkasavicāramūlakā satta pañhā naadhipatiyā kātabbā.": f"{SVM} सात प्रश्न {NL['adhipati']} करने चाहिए।",
    "Naanantarampi {naanantarepi (ka.)} nasamanantarampi naaññamaññampi naupanissayampi satta pañhā rūpaṃyeva. Napurejāte sattatiṃsa paṭiccavārapaccanīyasadisaṃ. Napacchājāte sattatiṃsa, naāsevanepi sadisaṃ. Yattha avitakkavicāramattopi āgacchati, tattha vipākā kātabbā.":
        f"{S.NAME['anantara']} के अभाव [पाठभेद (Ka.): naanantarepi], {S.NAME['samanantara']} के अभाव, {S.NAME['aññamañña']} के अभाव "
        f"और {S.NAME['upanissaya']} के अभाव में भी सात प्रश्न हैं, केवल भौतिक रूप ही। {NL['purejāta']} सैंतीस, निर्भरता के खंड "
        f"के नकारात्मक क्रम के समान। {NL['pacchājāta']} सैंतीस, {NL['āsevana']} भी समान। जहाँ {VMP} भी आती है, वहाँ "
        "कर्म-फल रूपी परिघटनाएँ करनी चाहिए।",
    "Dassanena pahātabbo dhammo dassanena pahātabbassa dhammassa āhārapaccayena paccayo (saṃkhittaṃ) kabaḷīkāro… satta pañhā… indriyapaccayena paccayo… cakkhundriyañca…pe… rūpajīvitindriyañca …pe… satta pañhā jhānapaccayena paccayo… maggapaccayena paccayo… sampayuttapaccayena paccayo.":
        f"सत्य-दर्शन से छोड़ी जाने वाली परिघटना, सत्य-दर्शन से छोड़ी जाने वाली परिघटना के लिए {S.INS('āhāra', 'fs')} (संक्षिप्त) "
        f"कौर-कौर खाया जाने वाला भोजन… सात प्रश्न… {S.INS('indriya', 'fs')}… आँख की क्षमता और… भौतिक जीवन-क्षमता और …… "
        f"सात प्रश्न, {S.INS('jhāna', 'fs')}… {S.INS('magga', 'fs')}… {S.INS('sampayutta', 'fs')}।",
}

# ============================================================ lexicon for noun phrases

# heads: word -> (case, number, gender, direct, oblique);  case n=nom, a=acc, x=nom/acc, d=dat
H = {}


def head(words, case, num, gen, d, o=None):
    for w in words.split("|"):
        H[w] = (case, num, gen, d, o if o is not None else d)


head("khandho", "n", "s", "m", "समूह"); head("khandhaṃ", "a", "s", "m", "समूह")
head("khandhā", "n", "p", "m", "समूह", "समूहों"); head("khandhe", "a", "p", "m", "समूह", "समूहों")
head("khandhānaṃ", "d", "p", "m", "समूह", "समूहों"); head("khandhassa", "d", "s", "m", "समूह")
head("vatthu", "n", "s", "m", "आधार"); head("vatthuṃ", "a", "s", "m", "आधार"); head("vatthussa", "d", "s", "m", "आधार")
head("mahābhūtaṃ", "x", "s", "m", "महाभूत"); head("mahābhūtā", "n", "p", "m", "महाभूत", "महाभूतों")
head("mahābhūte", "a", "p", "m", "महाभूत", "महाभूतों"); head("mahābhūtānaṃ", "d", "p", "m", "महाभूत", "महाभूतों")
head("vitakko", "n", "s", "m", "आरंभिक विचार"); head("vitakkaṃ", "a", "s", "m", "आरंभिक विचार")
head("vitakkassa", "d", "s", "m", "आरंभिक विचार")
head("vicāro", "n", "s", "m", "सतत विचार"); head("vicāraṃ", "a", "s", "m", "सतत विचार")
head("vicārassa", "d", "s", "m", "सतत विचार")
head("cetanā", "n", "s", "m", "इरादा", "इरादे")
head("moho", "n", "s", "m", "मोह")
head("adhipati", "n", "s", "f", "प्रधानता")
head("hetū", "n", "p", "m", "मूल", "मूलों")
head("āhārā", "n", "p", "m", "आहार", "आहारों"); head("indriyā", "n", "p", "f", "क्षमताएँ", "क्षमताओं")
head("jhānaṅgāni", "n", "p", "m", "ध्यान के अंग", "ध्यान के अंगों"); head("maggaṅgāni", "n", "p", "m", "मार्ग के अंग", "मार्ग के अंगों")
RC, RK, RU = S.RUPA_CITTA, S.RUPA_KATATTA, S.RUPA_UPADA
head("cittasamuṭṭhānaṃrūpaṃ", "x", "s", "m", RC); head("cittasamuṭṭhānānaṃrūpānaṃ", "d", "p", "m", RC, RC + "ों")
head("kaṭattārūpaṃ", "x", "s", "m", RK); head("kaṭattārūpānaṃ", "d", "p", "m", RK, RK + "ों")
head("upādārūpaṃ", "x", "s", "m", RU); head("upādārūpānaṃ", "d", "p", "m", RU, RU + "ों")
head("rūpajīvitindriyaṃ", "x", "s", "f", "भौतिक जीवन-क्षमता")
head("kabaḷīkāroāhāro", "n", "s", "m", "कौर-कौर खाया जाने वाला भोजन", "कौर-कौर खाए जाने वाले भोजन")
head("cuticittaṃ", "x", "s", "m", "मृत्यु का मन", "मृत्यु के मन")
head("upapatticittassa", "d", "s", "m", "जन्म का मन", "जन्म के मन")
head("bhavaṅgaṃ", "x", "s", "f", "जीवन-धारा"); head("bhavaṅgassa", "d", "s", "f", "जीवन-धारा")
head("āvajjanā", "n", "s", "m", "मन को विषय की ओर मोड़ना", "मन को विषय की ओर मोड़ने")
head("āvajjanāya", "d", "s", "m", "मन को विषय की ओर मोड़ना", "मन को विषय की ओर मोड़ने")
head("anulomaṃ", "x", "s", "f", "अनुरूपता")
head("gotrabhu", "n", "s", "m", "गोत्र-परिवर्तन"); head("gotrabhussa", "d", "s", "m", "गोत्र-परिवर्तन")
head("vodānaṃ", "x", "s", "f", "शुद्धि"); head("vodānassa", "d", "s", "f", "शुद्धि")
head("maggo", "n", "s", "m", "मार्ग"); head("maggassa", "d", "s", "m", "मार्ग"); head("maggaṃ", "a", "s", "m", "मार्ग")
head("phalaṃ", "x", "s", "m", "फल"); head("phalassa", "d", "s", "m", "फल")
head("phalasamāpattiyā", "d", "s", "f", "फल की ध्यान-अवस्था")
head("jhānassa", "d", "s", "m", "ध्यान"); head("jhānaṃ", "a", "s", "m", "ध्यान")
head("vuṭṭhānassa", "d", "s", "m", "बाहर आना", "बाहर आने")
head("kusalākusalaṃ", "x", "s", "m", "हितकर और हानिकर मन"); head("kiriyaṃ", "x", "s", "m", "केवल क्रिया रूपी मन")
head("vipākamanoviññāṇadhātu", "n", "s", "m", "कर्म-फल रूपी मन की चेतना का तत्व", "कर्म-फल रूपी मन की चेतना के तत्व")
head("vipākamanoviññāṇadhātuyā", "d", "s", "m", "", "कर्म-फल रूपी मन की चेतना के तत्व")
head("kiriyamanoviññāṇadhātuyā", "d", "s", "m", "", "केवल क्रिया रूपी मन की चेतना के तत्व")
head("vipākamanodhātu", "n", "s", "m", "कर्म-फल रूपी मन का तत्व", "कर्म-फल रूपी मन के तत्व")
head("vipākamanodhātuyā", "d", "s", "m", "", "कर्म-फल रूपी मन के तत्व")
head("kāyaviññāṇaṃ", "x", "s", "f", "शरीर की चेतना"); head("kāyaviññāṇassa", "d", "s", "f", "शरीर की चेतना")
head("cakkhuviññāṇaṃ", "x", "s", "f", "आँख की चेतना"); head("cakkhuviññāṇassa", "d", "s", "f", "आँख की चेतना")
head("pañcaviññāṇaṃ", "x", "s", "f", "पाँच प्रकार की चेतना")
head("pañcannaṃviññāṇānaṃ", "d", "p", "f", "", "पाँच प्रकार की चेतना")
head("nibbānaṃ", "x", "s", "m", "निर्वाण")
head("rūpāyatanaṃ", "x", "s", "m", "दृश्य रूप का इंद्रिय-क्षेत्र", "दृश्य रूप के इंद्रिय-क्षेत्र")
head("phoṭṭhabbāyatanaṃ", "x", "s", "m", "स्पर्श का इंद्रिय-क्षेत्र", "स्पर्श के इंद्रिय-क्षेत्र")
head("cakkhāyatanaṃ", "x", "s", "m", "आँख का इंद्रिय-क्षेत्र", "आँख के इंद्रिय-क्षेत्र")
head("kāyāyatanaṃ", "x", "s", "m", "शरीर का इंद्रिय-क्षेत्र", "शरीर के इंद्रिय-क्षेत्र")
head("cakkhundriyaṃ", "x", "s", "f", "आँख की क्षमता"); head("kāyindriyaṃ", "x", "s", "f", "शरीर की क्षमता")
head("ākāsānañcāyatanaṃ", "x", "s", "m", "अनंत आकाश का क्षेत्र", "अनंत आकाश के क्षेत्र")
head("ākiñcaññāyatanaṃ", "x", "s", "m", "कुछ भी न होने का क्षेत्र", "कुछ भी न होने के क्षेत्र")
head("nevasaññānāsaññāyatanaṃ", "x", "s", "m", "न पहचान न अ-पहचान का क्षेत्र", "न पहचान न अ-पहचान के क्षेत्र")
head("viññāṇañcāyatanassa", "d", "s", "m", "", "अनंत चेतना के क्षेत्र")
head("ākāsānañcāyatanassa", "d", "s", "m", "", "अनंत आकाश के क्षेत्र")
head("ākiñcaññāyatanassa", "d", "s", "m", "", "कुछ भी न होने के क्षेत्र")
head("nevasaññānāsaññāyatanassa", "d", "s", "m", "", "न पहचान न अ-पहचान के क्षेत्र")
head("tatiyassajhānassa", "d", "s", "m", "", "तीसरे ध्यान"); head("catutthassajhānassa", "d", "s", "m", "", "चौथे ध्यान")
head("dibbassacakkhussa", "d", "s", "f", "", "दिव्य आँख"); head("dibbāyasotadhātuyā", "d", "s", "m", "", "दिव्य कान के तत्व")
head("purejātassaimassakāyassa", "d", "s", "m", "", "पहले उत्पन्न इस शरीर")
head("imassakāyassa", "d", "s", "m", "", "इस शरीर")
head("kāyikassasukhassa", "d", "s", "m", "", "शारीरिक सुख"); head("kāyikassadukkhassa", "d", "s", "m", "", "शारीरिक दुःख")
for _w, _h in S.NANA.items():
    if _w.endswith("ñāṇassa"):
        head(_w, "d", "s", "m", "", _h)
# objects of the knowing / savouring sentences
head("pahīnekilese", "a", "p", "m", "छोड़े जा चुके मन के क्लेश", S.KILESA["pahīne"])
head("vikkhambhitekilese", "a", "p", "m", "दबाए जा चुके मन के क्लेश", S.KILESA["vikkhambhite"])
head("pubbesamudāciṇṇekilese", "a", "p", "m", "पहले बार-बार उठे मन के क्लेश", S.KILESA["pubbe samudāciṇṇe"])
head("pubbesuciṇṇāni", "x", "p", "m", "पहले भली-भाँति किए गए कार्य", S.DEEDS)
head("cakkhuṃ", "x", "s", "f", "आँख"); head("sotaṃ", "x", "s", "m", "कान"); head("ghānaṃ", "x", "s", "f", "नाक")
head("jivhaṃ", "x", "s", "f", "जीभ"); head("kāyaṃ", "x", "s", "m", "शरीर")
head("rūpe", "a", "p", "m", "दृश्य रूप", "दृश्य रूपों"); head("sadde", "a", "p", "f", "ध्वनियाँ", "ध्वनियों")
head("gandhe", "a", "p", "m", "गंध", "गंधों"); head("rase", "a", "p", "m", "स्वाद", "स्वादों")
head("phoṭṭhabbe", "a", "p", "m", "स्पर्श", "स्पर्शों"); head("phoṭṭhabbaṃ", "x", "s", "m", "स्पर्श")
head("taṃ", "x", "s", "m", "वह", "उस")
# the strong-support lists (saddhā … patthanā, kāyika sukha …)
head("saddhā", "n", "s", "f", "श्रद्धा"); head("saddhaṃ", "a", "s", "f", "श्रद्धा"); head("saddhāya", "d", "s", "f", "", "श्रद्धा")
head("sīlaṃ", "x", "s", "m", "सदाचार"); head("sīlassa", "d", "s", "m", "", "सदाचार")
head("sutaṃ", "x", "s", "m", "सुना-सीखा ज्ञान", "सुने-सीखे ज्ञान"); head("sutassa", "d", "s", "m", "", "सुने-सीखे ज्ञान")
head("cāgo", "n", "s", "m", "त्याग"); head("cāgaṃ", "a", "s", "m", "त्याग"); head("cāgassa", "d", "s", "m", "", "त्याग")
head("paññā", "n", "s", "f", "प्रज्ञा"); head("paññaṃ", "a", "s", "f", "प्रज्ञा"); head("paññāya", "d", "s", "f", "", "प्रज्ञा")
head("rāgo", "n", "s", "m", "राग"); head("rāgaṃ", "a", "s", "m", "राग"); head("rāgassa", "d", "s", "m", "", "राग")
head("doso", "n", "s", "m", "द्वेष"); head("dosaṃ", "a", "s", "m", "द्वेष"); head("dosassa", "d", "s", "m", "", "द्वेष")
head("mohaṃ", "a", "s", "m", "मोह"); head("mohassa", "d", "s", "m", "", "मोह")
head("māno", "n", "s", "m", "अहंकार"); head("mānaṃ", "a", "s", "m", "अहंकार"); head("mānassa", "d", "s", "m", "", "अहंकार")
head("diṭṭhi", "n", "s", "f", "दृष्टि"); head("diṭṭhiṃ", "a", "s", "f", "दृष्टि"); head("diṭṭhiyā", "d", "s", "f", "", "दृष्टि")
head("patthanā", "n", "s", "f", "कामना"); head("patthanaṃ", "a", "s", "f", "कामना"); head("patthanāya", "d", "s", "f", "", "कामना")
head("vicikicchā", "n", "s", "m", "संशय"); head("vicikicchaṃ", "a", "s", "m", "संशय")
head("uddhaccaṃ", "x", "s", "f", "बेचैनी"); head("domanassaṃ", "x", "s", "f", "उदासी")
head("kāyikaṃsukhaṃ", "x", "s", "m", "शारीरिक सुख"); head("kāyikaṃdukkhaṃ", "x", "s", "m", "शारीरिक दुःख")
head("utu", "n", "s", "m", "तापमान"); head("utuṃ", "a", "s", "m", "तापमान")
head("bhojanaṃ", "x", "s", "m", "भोजन"); head("senāsanaṃ", "x", "s", "m", "निवास-स्थान")
head("sukhaṃ", "x", "s", "m", "सुख"); head("pañhā", "n", "p", "m", "प्रश्न")
head("chandarāgo", "n", "s", "m", "चाह-राग"); head("chandarāgassa", "d", "s", "m", "", "चाह-राग")

SUPPORT_DAT = {"saddhāya", "sīlassa", "sutassa", "cāgassa", "paññāya", "rāgassa", "dosassa", "mohassa", "mānassa", "diṭṭhiyā", "patthanāya"}
NUMW = {"eko": "एक", "ekaṃ": "एक", "ekassa": "एक", "dve": "दो", "dvinnaṃ": "दो", "tayo": "तीन",
        "tiṇṇannaṃ": "तीन", "satta": "सात"}


def _agr_any(a):
    return a


ADJ = {  # word -> (kind, function(agr) -> Hindi);  kind: adj (comma-joined), det, pre, sah (vicikicchā/uddhacca pair)
    "ahetukaṃ": ("adj", lambda a: "मूल से रहित"), "ahetuke": ("adj", lambda a: "मूल से रहित"),
    "ahetukā": ("adj", lambda a: "मूल से रहित"),
    "vipākaṃ": ("adj", lambda a: "कर्म-फल रूपी"), "vipāke": ("adj", lambda a: "कर्म-फल रूपी"),
    "vipākā": ("adj", lambda a: "कर्म-फल रूपी"), "vipāko": ("adj", lambda a: "कर्म-फल रूपी"),
    "vipākānaṃ": ("adj", lambda a: "कर्म-फल रूपी"), "vipākassa": ("adj", lambda a: "कर्म-फल रूपी"),
    "sampayuttakānaṃ": ("adj", lambda a: {"m": "जुड़ा हुआ", "o": "जुड़े हुए", "f": "जुड़ी हुई"}[a]),
    "pacchājātā": ("adj", lambda a: "बाद में उत्पन्न"),
    "purejātaṃ": ("adj", lambda a: "पहले उत्पन्न"),
    "purimāpurimā": ("det", lambda a: {"m": "पहले-पहले का", "o": "पहले-पहले के", "f": "पहले-पहले की"}[a]),
    "purimopurimo": ("det", lambda a: {"m": "पहले-पहले का", "o": "पहले-पहले के", "f": "पहले-पहले की"}[a]),
    "pacchimānaṃpacchimānaṃ": ("det", lambda a: {"m": "बाद-बाद का", "o": "बाद-बाद के", "f": "बाद-बाद की"}[a]),
    "pacchimassapacchimassa": ("det", lambda a: {"m": "बाद-बाद का", "o": "बाद-बाद के", "f": "बाद-बाद की"}[a]),
    "vicikicchāsahagate": ("sah", lambda a: "संशय के साथ होने " + {"m": "वाला", "o": "वाले", "f": "वाली"}[a]),
    "vicikicchāsahagato": ("sah", lambda a: "संशय के साथ होने " + {"m": "वाला", "o": "वाले", "f": "वाली"}[a]),
    "vicikicchāsahagataṃ": ("sah", lambda a: "संशय के साथ होने " + {"m": "वाला", "o": "वाले", "f": "वाली"}[a]),
    "uddhaccasahagate": ("sah", lambda a: "बेचैनी के साथ होने " + {"m": "वाला", "o": "वाले", "f": "वाली"}[a]),
    "uddhaccasahagato": ("sah", lambda a: "बेचैनी के साथ होने " + {"m": "वाला", "o": "वाले", "f": "वाली"}[a]),
    "uddhaccasahagataṃ": ("sah", lambda a: "बेचैनी के साथ होने " + {"m": "वाला", "o": "वाले", "f": "वाली"}[a]),
    "kāyaviññāṇasahagataṃ": ("adj", lambda a: "शरीर की चेतना के साथ होने " + {"m": "वाला", "o": "वाले", "f": "वाली"}[a]),
    "catuviññāṇasahagataṃ": ("adj", lambda a: "चार प्रकार की चेतना के साथ होने " + {"m": "वाला", "o": "वाले", "f": "वाली"}[a]),
    "pañcaviññāṇasahagataṃ": ("adj", lambda a: "पाँच प्रकार की चेतना के साथ होने " + {"m": "वाला", "o": "वाले", "f": "वाली"}[a]),
    "bāhiraṃ": ("adj", lambda a: "बाह्य"), "āhārasamuṭṭhānaṃ": ("adj", lambda a: "आहार से उत्पन्न"),
    "utusamuṭṭhānaṃ": ("adj", lambda a: "तापमान से उत्पन्न"),
    "asaññasattānaṃ": ("pre", lambda a: "पहचान-रहित प्राणियों में"),
    "dutiyejhāne": ("pre", lambda a: "दूसरे ध्यान में"),
    "kabaḷīkāro": ("adj", lambda a: "कौर-कौर खाया जाने वाला"),
    "kāyikaṃ": ("adj", lambda a: "शारीरिक"),
    "sakabhaṇḍe": ("pre", lambda a: "अपनी वस्तु के प्रति"), "parabhaṇḍe": ("pre", lambda a: "पराई वस्तु के प्रति"),
    "sakapariggahe": ("pre", lambda a: "अपनी संपत्ति के प्रति"), "parapariggahe": ("pre", lambda a: "पराई संपत्ति के प्रति"),
}
PK_GEN = {"dutiyassa_jhānassa": "दूसरे ध्यान", "tatiyassajhānassa": "तीसरे ध्यान", "catutthassajhānassa": "चौथे ध्यान",
          "ākāsānañcāyatanassa": "अनंत आकाश के क्षेत्र", "viññāṇañcāyatanassa": "अनंत चेतना के क्षेत्र",
          "ākiñcaññāyatanassa": "कुछ भी न होने के क्षेत्र", "nevasaññānāsaññāyatanassa": "न पहचान न अ-पहचान के क्षेत्र",
          "dibbassacakkhussa": "दिव्य आँख", "dibbāyasotadhātuyā": "दिव्य कान के तत्व"}
for _w, _h in S.NANA.items():
    if _w.endswith("ñāṇassa"):
        PK_GEN[_w] = _h


def pk_head(tok):
    g = tok[3:]
    m = re.fullmatch(r"I:([A-Z+]+):assa_jhānassa", g)
    gh = ITEM_HI(m.group(1), "o") + " ध्यान" if m else PK_GEN[g]
    H[tok] = ("x", "s", "f", gh + " की प्रारंभिक तैयारी", gh + " की प्रारंभिक तैयारी")

PREFIX = {"paṭisandhikkhaṇe": "पुनर्जन्म के क्षण में", "ahetukapaṭisandhikkhaṇe": "मूल से रहित पुनर्जन्म के क्षण में",
          "arūpe": "अभौतिक लोक में", "nirodhāvuṭṭhahantassa": "समाप्ति की ध्यान-अवस्था से बाहर आने वाले व्यक्ति में",
          "ariyā": "आर्य"}
REL = {"paṭicca": ("पर निर्भर होकर", ""), "paccayā": ("के कारण", ""), "sahajātā": ("के साथ जन्म लेकर", ""),
       "sahajāto": ("के साथ जन्म लेकर", ""), "saṃsaṭṭhā": ("से घुल-मिलकर", ""), "saṃsaṭṭho": ("से घुल-मिलकर", ""),
       "ārabbha": ("को विषय बनाकर", "उसे विषय बनाकर"), "garuṃkatvā": ("को महत्व देकर", "उसे महत्व देकर"),
       "upanissāya": ("के प्रबल आश्रय से", "उसके प्रबल आश्रय से")}
LABEL = {"ārammaṇūpanissayo": "विषय रूपी प्रबल आश्रय", "anantarūpanissayo": "निकटता रूपी प्रबल आश्रय",
         "pakatūpanissayo": "स्वाभाविक प्रबल आश्रय", "sahajātā": "सह-उत्पत्ति", "sahajāto": "सह-उत्पत्ति",
         "sahajātaṃ": "सह-उत्पत्ति", "purejātaṃ": "पूर्व-उत्पत्ति", "pacchājātaṃ": "पश्चात्-उत्पत्ति",
         "pacchājātā": "पश्चात्-उत्पत्ति", "āhāraṃ": "आहार", "indriyaṃ": "क्षमता", "nānākkhaṇikā": "भिन्न क्षण",
         "ārammaṇapurejātaṃ": "विषय रूपी पूर्व-उत्पत्ति", "vatthupurejātaṃ": "आधार रूपी पूर्व-उत्पत्ति",
         "ārammaṇādhipati": "विषय रूपी प्रधानता", "sahajātādhipati": "सह-उत्पत्ति रूपी प्रधानता",
         "kabaḷīkāro": "कौर-कौर खाया जाने वाला", "bāhiraṃ": "बाह्य", "āhārasamuṭṭhānaṃ": "आहार से उत्पन्न",
         "utusamuṭṭhānaṃ": "तापमान से उत्पन्न", "asaññasattānaṃ": "पहचान-रहित प्राणियों में",
         "kāyikaṃ": "शारीरिक", "anulomaṃ": "सकारात्मक क्रम", "nevadassanena": "न सत्य-दर्शन से",
         "nevadassanena nabhāvanāya": "न सत्य-दर्शन से, न मानसिक अभ्यास से", "bhāvanāya": "मानसिक अभ्यास से",
         "paccanīyuddhāro": "नकारात्मक क्रम के लिए कारणों की छँटाई"}
for _p, _h in PREFIX.items():
    LABEL.setdefault(_p, _h)

# predicates (the implicit subject is a person): Pāli -> (Hindi, number)
PRED = {
    "dānaṃ deti": "दान देता है", "sīlaṃ samādiyati": "सदाचार ग्रहण करता है",
    "uposathakammaṃ karoti": "उपवास-व्रत का पालन करता है", "jhānaṃ uppādeti": "ध्यान उत्पन्न करता है",
    "vipassanaṃ uppādeti": "अंतर्दृष्टि उत्पन्न करता है", "maggaṃ uppādeti": "मार्ग उत्पन्न करता है",
    "samāpattiṃ uppādeti": "ध्यान-अवस्था उत्पन्न करता है", "abhiññaṃ uppādeti": "उच्च ज्ञान उत्पन्न करता है",
    "mānaṃ jappeti": "अहंकार पालता है", "diṭṭhiṃ gaṇhāti": "दृष्टि ग्रहण करता है",
    "adinnaṃ ādiyati": "बिना दिया हुआ लेता है", "musā bhaṇati": "झूठ बोलता है",
    "pisuṇaṃ bhaṇati": "चुगली की बात बोलता है", "samphaṃ palapati": "व्यर्थ बकवास करता है",
    "sandhiṃ chindati": "सेंध लगाता है", "nillopaṃ harati": "डाका डालता है",
    "ekāgārikaṃ karoti": "एक ही घर में डाका डालता है", "paripanthe tiṭṭhati": "राह में घात लगाता है",
    "paradāraṃ gacchati": "पराई स्त्री के पास जाता है", "gāmaghātaṃ karoti": "गाँव पर हमला करता है",
    "nigamaghātaṃ karoti": "कस्बे पर हमला करता है", "pāṇaṃ hanati": "जीव की हत्या करता है",
    "saṅghaṃ bhindati": "संघ में फूट डालता है",
    "vipassanaṃ": "अंतर्दृष्टि", "maggaṃ": "मार्ग", "samāpattiṃ": "ध्यान-अवस्था", "abhiññaṃ": "उच्च ज्ञान",
    "dānaṃ datvā": "दान देकर",
    "paccavekkhati": "पुनः विचार करता है", "paccavekkhanti": "पुनः विचार करते हैं",
    "assādeti abhinandati": "उसका " + S.SAVOURS.format(p="उसमें"),
    "assādeti": "उसका रस लेता है",
    "satta pañhā": "सात प्रश्न",
}

# ============================================================ clause tables with masked items
# keys: the clause with each item replaced by «@<ending>» and each «<item> cittena» by «INS»;
# values: {0}, {1} … = the n-th placeholder; «{0:o}» = item with agreement o/m/f.
GIFT, ANI = S.GIFT, S.ANICCA
PROSE = {
    "INS dānaṃ datvā sīlaṃ samādiyitvā uposathakammaṃ katvā taṃ INS paccavekkhati": "{0} " + GIFT + " उस पर {1} पुनः विचार करता है",
    "INS dānaṃ datvā sīlaṃ samādiyitvā uposathakammaṃ katvā INS taṃ garuṃkatvā paccavekkhati": "{0} " + GIFT + " {1} उसे महत्व देकर पुनः विचार करता है",
    "INS dānaṃ datvā sīlaṃ samādiyitvā uposathakammaṃ katvā": "{0} " + GIFT,
    "INS dānaṃ datvā": "{0} दान देकर",
    "INS": "{0}",
    "dānaṃ datvā sīlaṃ samādiyitvā uposathakammaṃ katvā taṃ paccavekkhati": GIFT + " उस पर पुनः विचार करता है",
    "dānaṃ datvā sīlaṃ samādiyitvā uposathakammaṃ katvā taṃ garuṃkatvā paccavekkhati": GIFT + " उसे महत्व देकर पुनः विचार करता है",
    "dānaṃ datvā sīlaṃ samādiyitvā uposathakammaṃ katvā taṃ assādeti abhinandati": GIFT + " उसका " + S.SAVOURS.format(p="उसमें"),
    "dānaṃ datvā sīlaṃ samādiyitvā uposathakammaṃ katvā taṃ garuṃkatvā assādeti abhinandati":
        GIFT + " उसे महत्व देकर उसका " + S.SAVOURS.format(p="उसमें"),
    "dānaṃ datvā sīlaṃ samādiyitvā": "दान देकर, सदाचार ग्रहण करके",
    "uposathakammaṃ katvā taṃ garuṃkatvā paccavekkhati": "उपवास-व्रत का पालन करके उसे महत्व देकर पुनः विचार करता है",
    "pubbesuciṇṇāni garuṃkatvā": S.DEEDS + " को महत्व देकर",
    "pubbe": "पहले",
    "@ā jhānā vuṭṭhahitvā": "{0:o} ध्यान से उठकर",
    "ariyā @ā jhānā vuṭṭhahitvā": "आर्य {0:o} ध्यान से उठकर",
    "jhānā vuṭṭhahitvā": "ध्यान से उठकर",
    "maggā vuṭṭhahitvā": "मार्ग से उठकर",
    "maggā vuṭṭhahitvā phalā vuṭṭhahitvā": "मार्ग से उठकर, फल से उठकर",
    "phalā vuṭṭhahitvā": "फल से उठकर",
    "phalā vuṭṭhahitvā taṃ INS paccavekkhati": "फल से उठकर उस पर {0} पुनः विचार करता है",
    "phalā vuṭṭhahitvā INS taṃ garuṃkatvā paccavekkhati": "फल से उठकर {0} उसे महत्व देकर पुनः विचार करता है",
    "phalā vuṭṭhahitvā phalaṃ paccavekkhati": "फल से उठकर फल पर पुनः विचार करता है",
    "phalā vuṭṭhahitvā phalaṃ paccavekkhanti": "फल से उठकर फल पर पुनः विचार करते हैं",
    "phalā vuṭṭhahitvā phalaṃ garuṃkatvā paccavekkhati": "फल से उठकर फल को महत्व देकर पुनः विचार करता है",
    "phalā vuṭṭhahitvā phalaṃ garuṃkatvā paccavekkhanti": "फल से उठकर फल को महत्व देकर पुनः विचार करते हैं",
    "jhānā vuṭṭhahitvā jhānaṃ paccavekkhati": "ध्यान से उठकर ध्यान पर पुनः विचार करता है",
    "jhānā vuṭṭhahitvā jhānaṃ garuṃkatvā paccavekkhati": "ध्यान से उठकर ध्यान को महत्व देकर पुनः विचार करता है",
    "jhānā vuṭṭhahitvā jhānaṃ garuṃkatvā": "ध्यान से उठकर ध्यान को महत्व देकर",
    "jhānā vuṭṭhahitvā jhānaṃ assādeti abhinandati": "ध्यान से उठकर ध्यान का " + S.SAVOURS.format(p="उसमें"),
    "ariyā maggā vuṭṭhahitvā maggaṃ paccavekkhanti": "आर्य मार्ग से उठकर मार्ग पर पुनः विचार करते हैं",
    "ariyā maggā vuṭṭhahitvā maggaṃ garuṃkatvā paccavekkhanti": "आर्य मार्ग से उठकर मार्ग को महत्व देकर पुनः विचार करते हैं",
    "phalaṃ paccavekkhanti": "फल पर पुनः विचार करते हैं", "phalaṃ garuṃkatvā paccavekkhanti": "फल को महत्व देकर पुनः विचार करते हैं",
    "nibbānaṃ paccavekkhanti": "निर्वाण पर पुनः विचार करते हैं",
    "nibbānaṃ garuṃkatvā paccavekkhanti": "निर्वाण को महत्व देकर पुनः विचार करते हैं",
    "ariyā nibbānaṃ paccavekkhanti": "आर्य निर्वाण पर पुनः विचार करते हैं",
    "ariyā nibbānaṃ garuṃkatvā paccavekkhanti": "आर्य निर्वाण को महत्व देकर पुनः विचार करते हैं",
    "cetopariyañāṇena @a cittasamaṅgissa cittaṃ jānāti": S.CETOPARIYA + " {0:o} मन से युक्त व्यक्ति के मन को जानता है",
    "cetopariyañāṇena @a cittasamaṅgissa cittaṃ jānanti": S.CETOPARIYA + " {0:o} मन से युक्त व्यक्ति के मन को जानते हैं",
    "ārammaṇādhipati sahajātādhipati": "विषय रूपी प्रधानता और सह-उत्पत्ति रूपी प्रधानता",
    "dibbena cakkhunā rūpaṃ passati": S.CLAUSE["dibbena cakkhunā rūpaṃ passati"],
    "dibbāyasotadhātuyā saddaṃ suṇāti": S.CLAUSE["dibbāya sotadhātuyā saddaṃ suṇāti"],
    "jhāne parihīne vippaṭisārissa @aṃ domanassaṃ uppajjati":
        "ध्यान के छूट जाने पर ग्लानि से भरे व्यक्ति में {0:f} उदासी उत्पन्न होती है",
    "pīti": "उल्लास",
    "kabaḷīkāro": "कौर-कौर खाया जाने वाला",
}

# ============================================================ helpers


def lower_initials(s):
    return S.lower_initials(s)


SLIPS = [("avitakka vicāramattassa", "avitakkavicāramattassa"), ("kaṭattā rūpānaṃ", "kaṭattārūpānaṃ"),
         ("vicākānaṃ", "vipākānaṃ"), ("pītisahagatānañca sukhasahagatānañca āsevanapaccayena", "pītisahagatānañca sukhasahagatānañca khandhānaṃ āsevanapaccayena"), ("utusamuṭṭhāna…", "utusamuṭṭhānaṃ…"), ("rāgassa.. ", "rāgassa… ")]
JOIN = [("cittasamuṭṭhānaṃ ca rūpaṃ", "cittasamuṭṭhānaṃrūpaṃ ca"), ("cittasamuṭṭhānaṃ rūpaṃ", "cittasamuṭṭhānaṃrūpaṃ"),
        ("cittasamuṭṭhānānaṃ ca rūpānaṃ", "cittasamuṭṭhānānaṃrūpānaṃ ca"),
        ("cittasamuṭṭhānānaṃ rūpānaṃ", "cittasamuṭṭhānānaṃrūpānaṃ"),
        ("kaṭattā ca rūpaṃ", "kaṭattārūpaṃ ca"), ("kaṭattā ca rūpānaṃ", "kaṭattārūpānaṃ ca"),
        ("purejātassa imassa kāyassa", "purejātassaimassakāyassa"), ("imassa kāyassa", "imassakāyassa"),
        ("kāyikaṃ sukhaṃ", "kāyikaṃsukhaṃ"), ("kāyikaṃ dukkhaṃ", "kāyikaṃdukkhaṃ"),
        ("kāyikassa sukhassa", "kāyikassasukhassa"), ("kāyikassa dukkhassa", "kāyikassadukkhassa"),
        ("pañcannaṃ viññāṇānaṃ", "pañcannaṃviññāṇānaṃ"), ("dutiye jhāne", "dutiyejhāne"),
        ("purimā purimā", "purimāpurimā"), ("purimo purimo", "purimopurimo"),
        ("pacchimānaṃ pacchimānaṃ", "pacchimānaṃpacchimānaṃ"), ("pacchimassa pacchimassa", "pacchimassapacchimassa"),
        ("nirodhā vuṭṭhahantassa", "nirodhāvuṭṭhahantassa"), ("dibbassa cakkhussa", "dibbassacakkhussa"),
        ("dibbāya sotadhātuyā", "dibbāyasotadhātuyā"),
        ("tatiyassa jhānassa", "tatiyassajhānassa"), ("catutthassa jhānassa", "catutthassajhānassa"),
        ("garuṃ katvā", "garuṃkatvā"), ("pahīne kilese", "pahīnekilese"), ("vikkhambhite kilese", "vikkhambhitekilese"),
        ("pubbe samudāciṇṇe kilese", "pubbesamudāciṇṇekilese"), ("pubbe suciṇṇāni", "pubbesuciṇṇāni"),
        ("kabaḷīkāro āhāro", "kabaḷīkāroāhāro")]


def normalize(t):
    """Lower-case initials, spelling-slip fixes, -ñca split, compounds, multiword heads, item masks."""
    t = lower_initials(t)
    for a, b in SLIPS:
        t = t.replace(a, b)
    t = t.replace("pītisahagatasukhasahagatacittasamaṅgissa", "pītisahagata ca sukhasahagata ca cittasamaṅgissa")
    t = re.sub(STEM_RX + r"ādhipati", r"\1ā adhipati", t)
    t = re.sub(STEM_RX + r"acittasamaṅgissa", r"\1a cittasamaṅgissa", t)
    t = re.sub(r"(ñāṇassa|āvajjanāya|gotrabhussa|vodānassa|maggassa|phalassa|kāyikassa sukhassa|kāyikassa dukkhassa), (?=\w+ñāṇassa|āvajjanāya|vodānassa|maggassa|phalassa|kāyikassa)", r"\1 ", t)
    t = re.sub(r"(?<!\w)pañca(?!\w)", "PANCA", t)
    t = re.sub(r"(\w)ñca(?!\w)", r"\1ṃ ca", t)
    t = t.replace("PANCA", "pañca")
    for a, b in JOIN:
        t = t.replace(a, b)
    t = ITEM_RX.sub(lambda m: f"I:{STEM_KEY[m.group(1)]}:{m.group(2)}", t)
    # «<genitive> parikammaṃ» = one head «PK:<genitive>»
    t = re.sub(r"(I:[A-Z+]+:assa jhānassa|dutiyassa jhānassa|tatiyassajhānassa|catutthassajhānassa|"
               r"ākāsānañcāyatanassa|viññāṇañcāyatanassa|ākiñcaññāyatanassa|nevasaññānāsaññāyatanassa|"
               r"dibbassacakkhussa|dibbāyasotadhātuyā|\w+ñāṇassa) parikammaṃ",
               lambda m: "PK:" + m.group(1).replace(" ", "_"), t)
    # coordinate item runs «I:A:e ca I:B:e ca …» -> «I:A+B:e»
    t = re.sub(r"I:([A-Z]+):(\w+) ca I:([A-Z]+):\2 ca I:([A-Z]+):\2 ca(?!\w)", r"I:\1+\3+\4:\2", t)
    t = re.sub(r"I:([A-Z]+):(\w+) ca I:([A-Z]+):\2 ca(?!\w)", r"I:\1+\3:\2", t)
    # coordination without the second ca (cittasamaṅgissa compound)
    t = re.sub(r"I:([A-Z]+):a ca I:([A-Z]+):a ca", r"I:\1+\2:a", t)
    # «<item> cittena» = instrumental of mind
    t = re.sub(r"I:([A-Z+]+):ena cittena", r"INS:\1", t)
    return t


def INS_HI(key):
    return ITEM_HI(key, "o") + " मन से"


def jn(xs, sep_last=" और "):
    xs = [x for x in xs if x]
    if len(xs) <= 1:
        return "".join(xs)
    return ", ".join(xs[:-1]) + sep_last + xs[-1]


# ============================================================ noun-phrase parser

class NP:
    def __init__(self):
        self.det, self.adjs, self.pre, self.num, self.head, self.ca = None, [], [], None, None, False
        self.item_first = False

    @property
    def case(self):
        if self.head:
            return H[self.head][0]
        return "x"

    def gn(self):
        if self.head:
            c, n, g, d, o = H[self.head]
            return g, n
        return "f", "s"   # implicit परिघटना

    def render(self, role):
        g, n = self.gn()
        oblique = role in ("acc", "dat")
        if g == "f":
            agr = "f"
        else:
            agr = "m" if (n == "s" and not oblique) else "o"
        parts = []
        if self.det:
            parts.append(ADJ[self.det][1](agr))
        adj_txt = []
        i = 0
        while i < len(self.adjs):
            a = self.adjs[i]
            if a.startswith("I:"):
                adj_txt.append(ITEM_HI(a.split(":")[1], agr))
            elif ADJ[a][0] == "sah" and i + 1 < len(self.adjs) and not self.adjs[i + 1].startswith("I:") \
                    and ADJ[self.adjs[i + 1]][0] == "sah":
                adj_txt.append(ADJ[a][1](agr) + (" और " if n == "p" else " या ") + ADJ[self.adjs[i + 1]][1](agr))
                i += 1
            else:
                adj_txt.append(ADJ[a][1](agr))
            i += 1
        if adj_txt:
            parts.append(", ".join(adj_txt) + ("," if self.head in ("pahīnekilese", "vikkhambhitekilese", "pubbesamudāciṇṇekilese") else ""))
        num = NUMW.get(self.num) if self.num else None
        hd = None
        if self.head:
            c, nn, gg, d, o = H[self.head]
            hd = o if oblique else d
        elif adj_txt or self.det:
            hd = "परिघटना" if self.adjs and self.adjs[-1].startswith("I:") else None
        # bāhiraṃ ekaṃ mahābhūtaṃ = एक बाह्य महाभूत (sample)
        if num and self.adjs == ["bāhiraṃ"]:
            parts = [num] + parts
            num = None
        parts += self.pre and [ADJ[p][1](agr) for p in self.pre] or []
        if num:
            parts.append(num)
        if hd:
            parts.append(hd)
        return " ".join(parts)

    def first_word(self, role):
        return self.render(role).split(" ")[0]


def tok_kind(w):
    if w == "ca":
        return "ca"
    if w.startswith("I:"):
        return "item"
    if w.startswith("PK:"):
        pk_head(w)
        return "head"
    if w in H:
        return "head"
    if w in NUMW:
        return "num"
    if w in ADJ:
        return "adj"
    raise KeyError(w)


def parse_nps(words):
    nps, cur = [], NP()
    for w in words:
        k = tok_kind(w)
        if k == "ca":
            if cur.head is None and not cur.adjs and nps:
                nps[-1].ca = True
            else:
                cur.ca = True
            continue
        if k == "head":
            cur.head = w
            nps.append(cur)
            cur = NP()
        elif k == "num":
            cur.num = w
        elif k == "item":
            if not cur.adjs and cur.det is None:
                cur.item_first = True
            cur.adjs.append(w)
        else:
            kind = ADJ[w][0]
            if kind == "det":
                cur.det = w
            elif kind == "pre":
                cur.pre.append(w)
            else:
                cur.adjs.append(w)
    if cur.adjs or cur.det or cur.num or cur.pre:
        nps.append(cur)
    return nps


def render_group(nps, role):
    hs = [np.render(role) for np in nps]
    if role == "dat":
        if len(hs) == 1:
            return hs[0] + " के लिए"
        if len(hs) == 2:
            return hs[0] + " के लिए और " + hs[1] + " के लिए"
        cas = [np.ca for np in nps]
        if len(hs) % 2 == 0 and all(not cas[i] and cas[i + 1] for i in range(0, len(hs), 2)):
            return ", ".join(f"{hs[i]} और {hs[i + 1]} के लिए" for i in range(0, len(hs), 2))
        return jn(hs) + " के लिए"
    return jn(hs)


def group_gn(nps):
    if not nps:
        return None
    if len(nps) == 1:
        g, n = nps[0].gn()
        return g + n
    return ("m" if any(np.gn()[0] == "m" for np in nps) else "f") + "p"


ARISE = {"ms": "उत्पन्न होता है", "fs": "उत्पन्न होती है", "mp": "उत्पन्न होते हैं", "fp": "उत्पन्न होती हैं"}
COND_ABL = {}
for _k, _h, _l, _n in S.CONDS:
    COND_ABL[_k + "paccayā"] = S.ABL[_k]
    COND_ABL[_n + _k + "paccayā"] = S.NABL[_k]
COND_INS = re.compile(r"^(na )?(" + "|".join(sorted(S.KEYS, key=len, reverse=True)) + r")paccayena paccayo$")


# ============================================================ piece translators

class State:
    def __init__(self):
        self.g = None          # agreement of the current subject (ms/fs/mp/fp)
        self.acc_ctx = False   # the run of «…» pieces ends in «upanissāya»


def item_frame(key, end, plural=False):
    """Items in a «dhammaṃ/dhammo/dhammassa» frame."""
    ks = key.split("+")
    if end in ("aṃ", "assa", "e"):   # acc / dat lists repeat the noun
        hs = [ITEM_HI(k, "f") + " परिघटना" for k in ks]
        return jn(hs)
    if len(ks) == 1 and not plural:
        return ITEM_HI(key, "f") + " परिघटना"
    return ITEM_HI(key, "f") + " परिघटनाएँ"


def ins_piece(neg, k, st):
    if st.g is None:
        raise KeyError("no subject for INS")
    return S.NINS(k, st.g) if neg else S.INS(k, st.g)


HEADLINE_RE = re.compile(r"^I:([A-Z+]+):o (dhammo|dhammā)(?: I:([A-Z+]+):assa( dhammassa)?)?"
                         r"(?: (na )?(\w+?)paccayena paccayo| (\w+))?$")
DATITEM_RE = re.compile(r"^I:([A-Z+]+):assa(?: dhammassa)?(?: (na )?(\w+?)paccayena paccayo)?$")


def headline(core, st):
    m = HEADLINE_RE.match(core)
    if not m:
        return None
    k1, dh, k2, dhs, neg, ck, label = m.groups()
    if ck and ck not in S.KEYS:
        return None
    if label and label not in LABEL:
        return None
    plural = dh == "dhammā"
    st.g = "fp" if plural else "fs"
    out = item_frame(k1, "o", plural)
    if k2:
        out += ", " + item_frame(k2, "assa") + " के लिए"
    if ck:
        out += " " + ins_piece(neg, ck, st)
    if label:
        out += " " + LABEL[label]
    return out


def translate_core(core, st):
    """A piece without notes and separators; returns Hindi."""
    if core in LABEL:
        return LABEL[core]
    if core in PRED:
        return PRED[core]
    if core in NUMS:
        return NUMS[core]
    ph = pred_hi(core)
    if ph is not None:
        return ph
    if core.startswith("dhammassa"):
        rest = core[len("dhammassa"):].strip()
        return "परिघटना के लिए" + (" " + translate_core(rest, st) if rest else "")
    h = headline(core, st)
    if h is not None:
        return h
    m = DATITEM_RE.match(core)
    if m:
        k, neg, ck = m.groups()
        out = item_frame(k, "assa") + " के लिए"
        if ck:
            out += " " + ins_piece(neg, ck, st)
        return out
    m = COND_INS.match(core)
    if m:
        return ins_piece(m.group(1), m.group(2), st)
    if core in COND_ABL:
        return COND_ABL[core]
    # item frames without verb (truncated by «…pe…»)
    m = re.fullmatch(r"I:([A-Z+]+):(aṃ|o)( dhammaṃ| dhammo| dhammā)?", core)
    if m:
        return item_frame(m.group(1), m.group(2), m.group(3) == " dhammā")
    m = re.fullmatch(r"I:([A-Z+]+):o (dhammo|dhammā) (uppajjati|uppajjanti)", core)
    if m:
        return item_frame(m.group(1), "o", m.group(2) == "dhammā") + " " + ARISE["fp" if m.group(2) == "dhammā" else "fs"]
    # masked prose
    key, args = mask_key(core)
    if key in PROSE:
        return fill(PROSE[key], args)
    return body(core, st)


def pred_hi(text):
    ws = text.split(" ")
    pre = []
    if ws and ws[0].startswith("INS:"):
        pre.append(INS_HI(ws[0][4:]))
        ws = ws[1:]
    item = None
    if ws and ws[0].startswith("I:"):
        item = ws[0].split(":")[1]
        ws = ws[1:]
    rest = " ".join(ws)
    if rest not in PRED or (item and not rest.startswith("jhānaṃ")):
        return None
    h = PRED[rest]
    if item:
        h = ITEM_HI(item, "m") + " " + h
    return " ".join(pre + [h])


def mask_key(core):
    args = []

    def rep(m):
        if m.group(0).startswith("INS"):
            args.append(("INS", m.group(1)))
            return "INS"
        args.append(("I", m.group(2)))
        return "@" + m.group(3)
    key = re.sub(r"INS:([A-Z+]+)|I:(([A-Z+]+)):?(\w*)", lambda m: rep2(m, args), core)
    return key, args


def rep2(m, args):
    if m.group(0).startswith("INS"):
        args.append(("INS", m.group(1)))
        return "INS"
    args.append(("I", m.group(3)))
    return "@" + m.group(4)


def fill(tpl, args):
    def r(m):
        i = int(m.group(1))
        kind, key = args[i]
        if kind == "INS":
            return INS_HI(key)
        return ITEM_HI(key, m.group(2) or "o")
    return re.sub(r"\{(\d+)(?::(\w))?\}", r, tpl)


VERB_OBJ = {  # object-verb predicates (subject implicit): Pāli -> (object marker, Hindi template, plural verb?)
    "aniccatodukkhatoanattato vipassati": ("को", ANI + " " + S.VIPASSATI["s"], False),
    "aniccatodukkhatoanattato vipassanti": ("को", ANI + " " + S.VIPASSATI["p"], True),
    "aniccatodukkhatoanattato vipassati assādeti abhinandati": ("को", ANI + " " + S.VIPASSATI["s"] + ", {p}का रस लेता है, {p}में आनंद लेता है", False),
    "aniccatodukkhatoanattato vipassanti assādenti abhinandanti": ("को", ANI + " " + S.VIPASSATI["p"] + ", {p}का रस लेते हैं, {p}में आनंद लेते हैं", True),
    "assādeti abhinandati": ("का", "रस लेता है, {p}में आनंद लेता है", False),
    "assādeti": ("का", "रस लेता है", False),
    "garuṃkatvā assādeti abhinandati": ("को", "महत्व देकर {p}का रस लेता है, {p}में आनंद लेता है", False),
    "garuṃkatvā": ("को", "महत्व देकर", False),
    "paccavekkhati": ("पर", "पुनः विचार करता है", False), "paccavekkhanti": ("पर", "पुनः विचार करते हैं", True),
    "jānāti": ("को", "जानता है", False), "jānanti": ("को", "जानते हैं", True),
    "aniccatodukkhatoanattato": ("को", ANI, False),
}


def body(core, st):
    t = core.replace("aniccato dukkhato anattato", "aniccatodukkhatoanattato")
    words = t.split(" ")
    # object-verb sentences
    for vk in sorted(VERB_OBJ, key=lambda x: -len(x)):
        vw = vk.split(" ")
        if len(words) > len(vw) and words[-len(vw):] == vw:
            pre = words[:-len(vw)]
            subj = None
            if pre and pre[0] == "ariyā":
                subj = "आर्य"
                pre = pre[1:]
            ins_b = None
            if pre and pre[0].startswith("INS:"):
                ins_b = pre.pop(0)
            ins = None
            if pre and pre[-1].startswith("INS:"):
                ins = pre.pop()
            if "garuṃkatvā" in pre or not pre or any(w.startswith("INS:") for w in pre):
                break
            if ins_b:
                subj = (subj + " " if subj else "") + INS_HI(ins_b.split(":")[1])
            nps = parse_nps(pre)
            marker, tpl, _ = VERB_OBJ[vk]
            plural = len(nps) > 1 or nps[0].gn()[1] == "p"
            if nps[-1].head == "taṃ":
                obj = {"को": "उसे", "का": "उसका", "पर": "उस पर"}[marker]
            else:
                obj = render_group(nps, "acc") + " " + marker
            pron = "उन" if plural else "उस"
            out = (subj + " " if subj else "") + obj + (" " + INS_HI(ins.split(":")[1]) if ins else "") + " " + tpl.format(p=pron)
            return out.replace("उनका", "उनका").replace("{p}", pron)
    # «<object> upanissāya / garuṃ katvā <predicate>»
    for relw in ("upanissāya", "garuṃkatvā"):
        if relw in words:
            idx = words.index(relw)
            left, right = words[:idx], " ".join(words[idx + 1:])
            ph = pred_hi(right) if right else None
            if ph is None and right:
                key, args = mask_key(right)
                ph = fill(PROSE[key], args) if key in PROSE else None
            if ph is not None:
                rel_hi, tam_hi = REL[relw]
                if not left:
                    return rel_hi + " " + ph
                nps = parse_nps(left)
                if len(nps) == 1 and nps[0].head == "taṃ":
                    return tam_hi + " " + ph
                return render_group(nps, "acc") + " " + rel_hi + " " + ph
    # general: tokens -> spans split at REL / VERB / PVERB / ABL
    toks = []
    i = 0
    while i < len(words):
        w = words[i]
        two = " ".join(words[i:i + 2])
        if w in PREFIX:
            toks.append(("PRE", w))
        elif w in REL:
            toks.append(("REL", w))
        elif w in ("uppajjati", "uppajjanti"):
            toks.append(("VERB", w))
        elif w.endswith("paccayena") and i + 1 < len(words) and words[i + 1] == "paccayo":
            toks.append(("PV", (None, w[:-len("paccayena")])))
            i += 1
        elif w == "na" and i + 2 < len(words) and words[i + 1].endswith("paccayena"):
            toks.append(("PV", ("na ", words[i + 1][:-len("paccayena")])))
            i += 2
        elif w in COND_ABL:
            toks.append(("ABL", w))
        elif w.startswith("INS:"):
            toks.append(("INS", w))
        else:
            toks.append(("W", w))
        i += 1
    out = []
    span = []
    after_rel = False
    rel_seen = False
    pending_rel = None

    def flush(boundary):
        nonlocal span, after_rel
        nps = parse_nps(span) if span else []
        span = []
        res = []
        if boundary == "REL":
            if after_rel:
                cut = next((j for j, np in enumerate(nps) if np.case == "a"), len(nps) - 1 if nps else 0)
                nom, acc = nps[:cut], nps[cut:]
            else:
                nom, acc = [], nps
            if nom:
                res.append(("NOM", nom))
            res.append(("ACC", acc))
            return res
        if boundary in ("VERB",) or (boundary == "END" and after_rel):
            if nps:
                res.append(("NOM", nps))
            return res
        if boundary == "PV" or boundary == "END":
            nom = [np for np in nps if np.case != "d"]
            dat = [np for np in nps if np.case == "d"]
            # keep order: nominatives first then datives (as in the Pāli)
            if nom and dat and nps.index(dat[0]) < nps.index(nom[-1]):
                # odd order: render each group as it comes
                cur_role, grp = None, []
                for np in nps:
                    r = "DAT" if np.case == "d" else ("ACC" if np.case == "a" else "NOM")
                    if r != cur_role and grp:
                        res.append((cur_role, grp))
                        grp = []
                    cur_role = r
                    grp.append(np)
                if grp:
                    res.append((cur_role, grp))
                return res
            if boundary == "END" and not dat and nom and (st.acc_ctx or all(np.case == "a" for np in nom)):
                res.append(("ACCBARE", nom))
                return res
            if nom:
                res.append(("NOM", nom))
            if dat:
                res.append(("DAT", dat))
            return res
        if boundary == "ABL":
            acc_start = len(nps)
            for j in range(len(nps) - 1, -1, -1):
                if nps[j].case == "a":
                    acc_start = j
                else:
                    break
            if acc_start == len(nps) and nps:
                acc_start = len(nps) - 1 if len(nps) > 1 else 0
            nom, acc = nps[:acc_start], nps[acc_start:]
            if nom:
                res.append(("NOM", nom))
            if acc:
                res.append(("ACCP", acc))
            return res
        return res

    segs = []
    for kind, val in toks:
        if kind == "W":
            span.append(val)
            continue
        if kind == "PRE":
            segs += flush("END") if span else []
            segs.append(("PRE", val))
            continue
        if kind == "INS":
            segs += flush("END") if span else []
            segs.append(("INSX", val))
            continue
        if kind == "REL":
            segs += flush("REL")
            segs.append(("REL", val))
            after_rel = True
            continue
        if kind == "VERB":
            segs += flush("VERB")
            segs.append(("VERB", val))
            after_rel = False
            continue
        if kind == "PV":
            segs += flush("PV")
            segs.append(("PV", val))
            after_rel = False
            continue
        if kind == "ABL":
            segs += flush("ABL")
            segs.append(("ABL", val))
            continue
    if span:
        # predicate after «upanissāya» / «garuṃ katvā»
        rest = " ".join(span)
        if segs and segs[-1][0] == "REL" and (pred_hi(rest) is not None or mask_key(rest)[0] in PROSE):
            segs.append(("PRED", rest))
            span = []
        else:
            segs += flush("END")
    # render
    last_nom = None
    for j, (kind, val) in enumerate(segs):
        if kind == "PRE":
            out.append(PREFIX[val])
        elif kind == "INSX":
            out.append(INS_HI(val.split(":")[1]))
        elif kind == "NOM":
            last_nom = val
            st.g = group_gn(val)
            out.append(render_group(val, "nom"))
        elif kind == "ACC":
            nxt = segs[j + 1][1] if j + 1 < len(segs) else None
            rel_hi, tam_hi = REL[nxt]
            if len(val) == 1 and val[0].head == "taṃ":
                out.append("§" + tam_hi)
            elif not val:
                out.append("§" + rel_hi)
            else:
                out.append(render_group(val, "acc") + " §" + rel_hi)
        elif kind == "ACCBARE":
            out.append(render_group(val, "acc"))
        elif kind == "ACCP":
            out.append(render_group(val, "acc") + " पर")
        elif kind == "DAT":
            txt = render_group(val, "dat")
            if out and (val[0].head in SUPPORT_DAT or val[0].item_first or (val[0].adjs and val[0].adjs[0].startswith("vipāk")) or (last_nom and out[-1].split(" ")[-1] == txt.split(" ")[0])):
                out[-1] += ","
            out.append(txt)
        elif kind == "REL":
            continue
        elif kind == "VERB":
            g = st.g or ("fp" if val == "uppajjanti" else "fs")
            out.append(ARISE[g])
        elif kind == "PV":
            neg, k = val
            if st.g is None:
                raise KeyError("no subject: " + core)
            out.append(S.NINS(k, st.g) if neg else S.INS(k, st.g))
        elif kind == "ABL":
            out.append(COND_ABL[val])
        elif kind == "PRED":
            if pred_hi(val) is not None:
                out.append(pred_hi(val))
            else:
                key, args = mask_key(val)
                out.append(fill(PROSE[key], args))
    res = " ".join(x for x in out if x)
    return res.replace(" §", " ").replace("§", "")


# ============================================================ line translator

NUMS = dict(S.NUM)
NUMS.update({"dasa": "दस", "ekādasa": "ग्यारह", "dvādasa": "बारह", "terasa": "तेरह", "cuddasa": "चौदह",
             "soḷasa": "सोलह", "sattarasa": "सत्रह", "ekavīsa": "इक्कीस", "bāvīsa": "बाईस", "tevīsa": "तेईस",
             "pañcavīsa": "पच्चीस", "sattavīsa": "सत्ताईस", "aṭṭhavīsa": "अट्ठाईस", "ekūnatiṃsa": "उनतीस",
             "tiṃsa": "तीस", "tettiṃsa": "तैंतीस", "catuttiṃsa": "चौंतीस", "pañcatiṃsa": "पैंतीस",
             "sattatiṃsa": "सैंतीस", "sabbattha": "हर जगह", "sabbe": "सभी में"})
COUNT_WORDS = set(S.P_ABL) | set(S.P_NABL) | set(S.P_LOC) | set(S.P_NLOC) | set(NUMS)


def is_count(text):
    toks = [x for x in re.split(r"(…pe…|…|, |; | |\.)", text) if x and x not in ("…pe…", "…", ", ", "; ", " ", ".")]
    return bool(toks) and all(x in COUNT_WORDS for x in toks)


def count_hi(text):
    toks = [x for x in re.split(r"(…pe…|…|, |; | |\.$)", text) if x]
    out = []
    for i, x in enumerate(toks):
        if x == " ":
            out.append(", " if toks[i - 1] in S.P_ABL or toks[i - 1] in S.P_NABL else " ")
        elif x == "…pe…":
            out.append("…")
        elif x == ".":
            out.append("।")
        elif x in ("…", ", ", "; "):
            out.append(x)
        else:
            for d in (S.P_ABL, S.P_NABL, S.P_LOC, S.P_NLOC, NUMS):
                if x in d:
                    out.append(d[x])
                    break
    return "".join(out)


CLOSING = {"anulomaṃ": "सकारात्मक क्रम", "paccanīyaṃ": "नकारात्मक क्रम",
           "anulomapaccanīyaṃ": "सकारात्मक-नकारात्मक क्रम", "paccanīyānulomaṃ": "नकारात्मक-सकारात्मक क्रम",
           "paṭiccavāro": "निर्भरता का खंड", "paccayavāro": "कारण का खंड", "saṃsaṭṭhavāro": "घुले-मिले होने का खंड",
           "hetupaccayo": S.NAME["hetu"], "paccanīyuddhāro": "नकारात्मक क्रम के लिए कारणों की छँटाई",
           "vitakkattikaṃ niṭṭhitaṃ": "आरंभिक विचार वाला तीन का वर्गीकरण समाप्त",
           "pītittikaṃ niṭṭhitaṃ": "उल्लास वाला तीन का वर्गीकरण समाप्त",
           "dassanenapahātabbattikaṃ niṭṭhitaṃ": "सत्य-दर्शन से छोड़ी जाने वाली परिघटनाओं वाला तीन का वर्गीकरण समाप्त"}

VARIANTS = {"{nānākhaṇikā (syā. ka.)}": ("वर्तनी-भेद", "भिन्न क्षण")}

FRAME_RE = re.compile(r"I:([A-Z+]+):aṃ dhammaṃ(?: (paṭicca|paccayā|sahajāto|saṃsaṭṭho|sampayutto)"
                      r"(?: I:([A-Z+]+):o(?: (dhammo|dhammā)(?: (uppajjati|uppajjanti))?)?)?)?")
FRAME_REL = {"paṭicca": "पर निर्भर होकर", "paccayā": "के कारण", "sahajāto": "के साथ जन्म लेकर",
             "saṃsaṭṭho": "से घुल-मिलकर", "sampayutto": "से जुड़कर"}
SUBJFRAME_RE = re.compile(r"(?<![\w:])I:([A-Z+]+):o (dhammo|dhammā) (uppajjati|uppajjanti)(?= )")
COND_WORD = sorted(list(COND_ABL) + ["āhāra", "indriya", "jhāna", "magga", "sampayutta", "vippayutta",
                                     "atthi", "natthi", "vigata"], key=len, reverse=True)
BARE = {"āhāra": "āhārapaccayā", "indriya": "indriyapaccayā", "jhāna": "jhānapaccayā", "magga": "maggapaccayā",
        "sampayutta": "sampayuttapaccayā", "vippayutta": "vippayuttapaccayā", "atthi": "atthipaccayā",
        "natthi": "natthipaccayā", "vigata": "vigatapaccayā"}
CHAIN_TOK = re.compile(r"(?:( \x01\d+\x02)?(…pe… | …pe… |… | |, )(?:(\x01\d+\x02) )?)(" + "|".join(map(re.escape, COND_WORD)) + r"|tīṇi|ekaṃ|satta)(?![\w])")
FIRST_COND = re.compile(r" (" + "|".join(map(re.escape, COND_WORD)) + r")(?![\w])")


def chain_after(text, pos, store):
    """Scan an ablative chain starting at text[pos] (which begins with ' '). Returns (hindi, end)."""
    m = FIRST_COND.match(text, pos)
    if not m:
        return "", pos
    w = BARE.get(m.group(1), m.group(1))
    out = COND_ABL[w]
    end = m.end()
    best_out, best_end = out, end
    while True:
        m2 = CHAIN_TOK.match(text, end)
        if not m2:
            break
        note1, sep, note, w = m2.groups()
        w = BARE.get(w, w)
        sep_hi = ", " if sep == " " else sep.replace("…pe…", "…")
        out += (note1 or "") + sep_hi + (note + " " if note else "") + (COND_ABL[w] if w in COND_ABL else NUMS[w])
        end = m2.end()
        if w in COND_ABL:
            best_out, best_end = out, end
    return best_out, best_end


def frames(text, store):
    def keep(h):
        store.append(h)
        return f"\x01{len(store) - 1}\x02"
    out, pos = [], 0
    for m in FRAME_RE.finditer(text):
        k1, rel, k2, dh, verb = m.groups()
        h = item_frame(k1, "aṃ")
        if rel:
            h += " " + FRAME_REL[rel]
        if k2:
            plural = dh == "dhammā"
            h += " " + item_frame(k2, "o", plural)
        end = m.end()
        if verb:
            ch, end = chain_after(text, m.end(), store)
            h += (" " + ch if ch else "") + " " + ARISE["fp" if verb == "uppajjanti" else "fs"]
        out.append(text[pos:m.start()] + keep(h))
        pos = end
    text = "".join(out) + text[pos:]
    out, pos = [], 0
    for m in SUBJFRAME_RE.finditer(text):
        k, dh, verb = m.groups()
        ch, end = chain_after(text, m.end(), store)
        h = item_frame(k, "o", dh == "dhammā") + (" " + ch if ch else "") + " " + ARISE["fp" if verb == "uppajjanti" else "fs"]
        out.append(text[pos:m.start()] + keep(h))
        pos = end
    return "".join(out) + text[pos:]


SEP_RE = re.compile(r"( – |; |, |\. |…pe…|…|\.$)")
FAILS = Counter()


def translate_line(line):
    if line.startswith("#"):
        m = re.fullmatch(r"(#+) (\*?)(.*?)(\*?)", line)
        hashes, a, body_, b = m.groups()
        return f"{hashes} {a}{HEAD[body_]}{b}"
    if line in LINE:
        return LINE[line]
    store = []
    inserts = []
    for v, (kind, anchor) in VARIANTS.items():
        if v in line:
            line = line.replace(" " + v, "")
            inserts.append((anchor, S.variant_hi(v, kind)))
    if "{" in line:
        raise KeyError("variant: " + line)

    def keep_note(m):
        store.append("(" + NOTE[m.group(1)] + ")")
        return f"\x01{len(store) - 1}\x02"
    text = re.sub(r"\(([^()]*[^\d().][^()]*)\)", keep_note, line)
    # count lines
    head_, _, _ = text.partition("\x01")
    core = lower_initials(head_.rstrip(" "))
    if is_count(core):
        tail = text[len(core):]
        if tail.endswith("."):
            tail = tail[:-1] + "।"
        h = count_hi(core) + tail
        return finish(h, store, inserts)
    low = normalize(text)
    if low.rstrip(".") in CLOSING:
        return CLOSING[low.rstrip(".")] + ("।" if low.endswith(".") else "")
    low = frames(low, store)
    # pieces
    parts = SEP_RE.split(low)
    # «…» runs that end in «upanissāya»: ambiguous neuters are accusative there (handled by the parser's case)
    st = State()
    out = []
    accs = set()
    for i, p in enumerate(parts):
        if p in (" – ", "; ", ", ", "…", ". ", ".", "…pe…") or not p or "upanissāya" in p:
            continue
        j = i + 1
        while j < len(parts):
            if parts[j] in ("…", "…pe…", ""):
                j += 1
                continue
            if parts[j] in (" – ", "; ", ", ", ". ", "."):
                break
            if "upanissāya" in parts[j]:
                accs.add(i)
                break
            j += 1
    for i, p in enumerate(parts):
        st.acc_ctx = i in accs
        if p in (" – ", "; ", ", ", "…"):
            out.append(p)
        elif p == ". ":
            out.append("। ")
        elif p == ".":
            out.append("।")
        elif p == "…pe…":
            out.append("…")
        elif p:
            out.append(piece(p, st))
    return finish("".join(out), store, inserts)


def piece(p, st):
    res = []
    for sub in re.split(r"(\x01\d+\x02|\(\d+\))", p):
        if not sub.strip() or re.fullmatch(r"\x01\d+\x02|\(\d+\)", sub):
            res.append(sub)
            continue
        lead = sub[: len(sub) - len(sub.lstrip())]
        trail = sub[len(sub.rstrip()):]
        core = sub.strip()
        try:
            h = translate_core(core, st)
        except (KeyError, IndexError, TypeError, AttributeError) as e:
            FAILS[core] += 1
            h = "⟦" + core + "⟧"
        res.append(lead + h + trail)
    return "".join(res)


def finish(s, store, inserts):
    for _ in range(3):
        s = re.sub(r"\x01(\d+)\x02", lambda m: store[int(m.group(1))], s)
    s = s.replace("?।", "?")
    for anchor, br in inserts:
        assert anchor in s, (anchor, s)
        s = s.replace(anchor, anchor + " " + br, 1)
    return s


# ============================================================ file builder

ROOT = os.path.abspath(os.path.join(RAILS, "..", "..", "..", "..", ".."))
PALI_DIR = os.path.join(ROOT, "AI_translation", "pali", "pi-7_split_chapters")
OUT_DIR = os.path.join(ROOT, "AI_translation", "hindi", "pi-7-hindi-plain-rails_split_chapters")
ID_RE = re.compile(r" \^([0-9A-Za-z-]+)\s*$")


def build_file(name, write=True):
    lines = open(os.path.join(PALI_DIR, name), encoding="utf-8").read().split("\n")
    out = []
    for ln in lines:
        if not ln.strip():
            if out and out[-1] != "":
                out.append("")
            continue
        m = ID_RE.search(ln)
        body_ = ln[: m.start()] if m else ln.rstrip()
        hi = translate_line(body_)
        out.append(hi + (f" ^{m.group(1)}" if m else ""))
    while out and out[-1] == "":
        out.pop()
    if write:
        with open(os.path.join(OUT_DIR, name), "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(out) + "\n")


if __name__ == "__main__":
    check = "--check" in sys.argv
    for f in FILES:
        build_file(f, write=not check)
    if FAILS:
        for k, v in FAILS.most_common():
            print(v, k)
        print("FAILS", len(FAILS))
    else:
        print("built" if not check else "no failures")
