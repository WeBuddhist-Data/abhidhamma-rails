"""pi-7 4-01-kilesagocchaka: Pāli->Hindi keyword map (conventions: hi-map-conventions-pi7.md).
The kilesa cluster and the final dyads (dassanena … saraṇa). Tables extend PI7 (map_sample_hi.py, read-only).
usage: python -I -B -X utf8 map_4-01_hi.py [--audit [--all]] [--missing]
"""
import sys, pathlib; sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import *  # noqa: F401,F403

F = "4-01-kilesagocchaka"
T = {}

ENDS = ("aṃ", "o", "ā", "assa", "ānaṃ", "e", "a", "āya", "ena", "ehi", "esu", "āni", "ānañca")


def gen(stem, value, ends=ENDS):
    for e in ends:
        T[stem + e] = value


# --- dyad items (masculine direct singular of the frame wording; build_4-01_hi.py DYADS)
for st, h in (
        ("saṃkiliṭṭh", "क्लेशों से मलिन"), ("asaṃkiliṭṭh", "क्लेशों से मलिन न होने वाला"),
        ("pahātabb", "छोड़ा जाने वाला"),
        ("pahātabbahetuk", ("छोड़े जाने वाले मूलों वाला", "छोड़े जाने वाले मूल")),
        ("savitakk", "आरंभिक विचार वाला"), ("avitakk", "आरंभिक विचार से रहित"),
        ("savicār", "सतत विचार वाला"), ("avicār", "सतत विचार से रहित"),
        ("sappītik", "उल्लास वाला"), ("appītik", "उल्लास से रहित"),
        ("pītisahagat", "उल्लास के साथ होने वाला"), ("napītisahagat", "उल्लास के साथ न होने वाला"),
        ("sukhasahagat", "सुख के साथ होने वाला"), ("nasukhasahagat", "सुख के साथ न होने वाला"),
        ("upekkhāsahagat", "समभाव के साथ होने वाला"), ("naupekkhāsahagat", "समभाव के साथ न होने वाला"),
        ("kāmāvacar", "इंद्रिय-सुखों के लोक से संबंधित"),
        ("nakāmāvacar", "इंद्रिय-सुखों के लोक से संबंधित न होने वाला"),
        ("rūpāvacar", "सूक्ष्म भौतिक लोक से संबंधित"),
        ("narūpāvacar", "सूक्ष्म भौतिक लोक से संबंधित न होने वाला"),
        ("arūpāvacar", "अभौतिक लोक से संबंधित"),
        ("naarūpāvacar", "अभौतिक लोक से संबंधित न होने वाला"),
        ("pariyāpann", "अस्तित्व के लोकों में समाया हुआ"),
        ("apariyāpann", "अस्तित्व के लोकों में न समाया हुआ"),
        ("niyyānik", "मुक्ति की ओर ले जाने वाला"), ("aniyyānik", "मुक्ति की ओर न ले जाने वाला"),
        ("niyat", "निश्चित"), ("aniyat", "अनिश्चित"),
        ("sauttar", "सर्वोच्च न होने वाला"), ("anuttar", "सर्वोच्च"),
        ("saraṇ", "संघर्ष वाला"), ("araṇ", "संघर्ष से रहित"),
        # defilements and factors (pi-1 terms)
        ("lobh", "लोभ"), ("dos", "द्वेष"), ("moh", "मोह"), ("mān", "अहंकार"), ("rāg", "राग"),
        ("thin", "आलस्य"), ("uddhacc", "बेचैनी"), ("ahirik", "निर्लज्जता"),
        ("anottapp", "बुराई के प्रति निडरता"),
        ("vicikicchāsahagat", "संशय के साथ होने वाला"), ("uddhaccasahagat", "बेचैनी के साथ होने वाला"),
        ("vitakk", "आरंभिक विचार"), ("vicār", "सतत विचार"), ("sukh", "सुख"), ("upekkh", "समभाव"),
        ("bhavaṅg", "जीवन-धारा"), ("parikamm", "प्रारंभिक तैयारी"),
        ("cuticitt", "मृत्यु का मन"), ("upapatticitt", "जन्म का मन"),
        ("mātughātikamm", "माता की हत्या का कर्म"), ("pitughātikamm", "पिता की हत्या का कर्म"),
        ("arahantaghātikamm", "अर्हत् की हत्या का कर्म"), ("ruhiruppādakamm", "बुद्ध का खून बहाने का कर्म"),
        ("saṅghabhedakamm", "संघ में फूट डालने का कर्म"),
        ("dibb", "दिव्य"), ("jhān", "ध्यान"),
):
    gen(st, h)

T.update({
    "ahetukā": "मूल से रहित", "sampayuttake": "जुड़ा हुआ",
    "vipākamanodhātu": "कर्म-फल रूपी मन का तत्व", "vipākamanodhātuyā": "कर्म-फल रूपी मन का तत्व",
    "vipākamanoviññāṇadhātu": "कर्म-फल रूपी मन की चेतना का तत्व",
    "vipākamanoviññāṇadhātuyā": "कर्म-फल रूपी मन की चेतना का तत्व",
    "kiriyamanoviññāṇadhātuyā": "केवल क्रिया रूपी मन की चेतना का तत्व",
    "kiriyamanoviññāṇadhātu": "केवल क्रिया रूपी मन की चेतना का तत्व",
    # adhipati compounds: «<item> प्रधानता»
    "adhipati": "प्रधानता",
    "aniyatādhipati": "अनिश्चित प्रधानता", "nakāmāvacarādhipati": "इंद्रिय-सुखों के लोक से संबंधित न होने वाली प्रधानता",
    "niyyānikādhipati": "मुक्ति की ओर ले जाने वाली प्रधानता",
    "pahātabbahetukādhipati": "छोड़े जाने वाले मूलों वाली प्रधानता",
    "sappītikādhipati": "उल्लास वाली प्रधानता", "saraṇādhipati": "संघर्ष वाली प्रधानता",
    # na- items of the dassanena / bhāvanāya dyads (negation kept; context rule in resolver for -hetuka)
    "nadassanena": "सत्य-दर्शन … न", "nabhāvanāya": "मानसिक अभ्यास … न",
    "bhāvanāya": "मानसिक अभ्यास",
    "pīti": "उल्लास", "pītiṃ": "उल्लास", "pītiyā": "उल्लास", "pītiñca": "उल्लास",
    "diṭṭhiyā": "दृष्टि", "vicikicchaṃ": "संशय", "vicikicchā": "संशय", "vicikicchañca": "संशय",
    "upekkhā": "समभाव", "sukhassa": "सुख", "dukkhassa": "दुःख",
    "vicikicchāsahagatamohaṭṭhāne": "संशय के साथ होने वाले मोह का स्थान",
    "niyatamicchādiṭṭhiyā": "निश्चित ग़लत दृष्टि", "micchādiṭṭhi": "ग़लत दृष्टि",
    # Pañhāvāra vocabulary
    "āvajjanā": "मन को विषय की ओर मोड़ना", "vuṭṭhānassa": "बाहर आना", "vuṭṭhānaṃ": "बाहर आना",
    "kiriyaṃ": "केवल क्रिया रूपी", "nibbānaṃ": "निर्वाण", "nibbānassa": "निर्वाण", "phalā": "फल",
    "gotrabhuṃ": "गोत्र-परिवर्तन", "cittena": "मन", "cakkhussa": "आँख", "sotadhātuṃ": "कान का तत्व",
    "iddhividhañāṇaṃ": "अलौकिक शक्तियों का ज्ञान",
    "cetopariyañāṇaṃ": "दूसरों के मन को जानने का ज्ञान", "cetopariyañāṇena": "दूसरों के मन को जानने का ज्ञान",
    "pubbenivāsānussatiñāṇaṃ": "पूर्व जन्मों के अनुस्मरण का ज्ञान",
    "yathākammūpagañāṇaṃ": "प्राणियों के अपने कर्मों के अनुसार जाने का ज्ञान",
    "anāgataṃsañāṇaṃ": "भविष्य को जानने का ज्ञान",
    "paṭhamaṃ": "पहला", "paṭhamassa": "पहला", "dutiyaṃ": "दूसरा", "dutiyassa": "दूसरा",
    "tatiyaṃ": "तीसरा", "tatiyassa": "तीसरा", "tatiyo": "तीसरा", "catutthaṃ": "चौथा", "catutthassa": "चौथा",
    "ākāsānañcāyatanassa": "अनंत आकाश का क्षेत्र", "ākiñcaññāyatanassa": "कुछ भी न होने का क्षेत्र",
    "pañcannaṃ": "पाँच", "viññāṇānaṃ": "चेतना", "viññāṇā": "चेतना", "pañcaviññāṇā": "पाँच प्रकार की चेतना",
    "adinnaṃ": "बिना दिया हुआ", "ādiyati": "लेना", "musā": "झूठ", "bhaṇati": "बोलना", "pisuṇaṃ": "चुगली",
    "samphaṃ": "व्यर्थ बकवास", "sandhiṃ": "सेंध", "nillopaṃ": "लूटपाट", "ekāgārikaṃ": "एक ही घर में डाका",
    "paripanthe": "रास्ते में घात", "paradāraṃ": "पराई स्त्री", "gāmaghātaṃ": "गाँव पर हमला",
    "nigamaghātaṃ": "कस्बे पर हमला",
    "mātaraṃ": "माता", "jīvitā": "हत्या", "voropeti": "हत्या करना", "voropetvā": "हत्या करके",
    "bhinditvā": "फूट डालकर", "paṭighātatthāya": "प्रतिकार",
    "anuppannaṃ": "उत्पन्न न हुआ", "uppannaṃ": "उत्पन्न हुआ", "uppādenti": "उत्पन्न करना",
    "samāpajjanti": "प्रवेश करना", "saṅkhāre": "निर्मित परिघटना", "vipassanti": "अंतर्दृष्टि से देखना",
    "atthapaṭisambhidāya": "अर्थ का विश्लेषणात्मक ज्ञान", "dhammapaṭisambhidāya": "परिघटनाओं का विश्लेषणात्मक ज्ञान",
    "niruttipaṭisambhidāya": "भाषा का विश्लेषणात्मक ज्ञान",
    "paṭibhānapaṭisambhidāya": "सूझ-बूझ का विश्लेषणात्मक ज्ञान",
    "ṭhānāṭhānakosallassa": "संभव और असंभव को जानने की कुशलता",
    "sakabhaṇḍe": "अपनी वस्तु", "parabhaṇḍe": "पराई वस्तु", "parihīne": "छूट जाना",
    "vippaṭisārissa": "ग्लानि से भरा व्यक्ति",
    "paccavekkhitvā": "जाँच करके", "passitvā": "देखकर",
    "asaññasattā": "पहचान-रहित प्राणी", "yāva": "तक",
    "kammāni": "कर्म", "lokuttaraṃ": "लोकोत्तर", "āhāraṃ": ("आहार", "भोजन"),
    "upanissayā": "प्रबल आश्रय", "arūpe": ("अभौतिक लोक", "अभौतिक"),
    "pahātabbacittasamaṅgissa": "छोड़े जाने वाले मन से युक्त व्यक्ति",
    "saṃkiliṭṭhacittasamaṅgissa": "क्लेशों से मलिन मन से युक्त व्यक्ति",
    "purimo": "पहले-पहले का", "pacchimassa": "बाद-बाद का", "pacchimāya": "बाद-बाद का",
    # instructions and notes
    "kātabbaṃ": ("तैयार करना चाहिए", "बनाना चाहिए", "लेना चाहिए", "शामिल करना चाहिए", "करना चाहिए"),
    "anulomamātikā": "सकारात्मक क्रम की मूल सूची",
    "niyāmetabbaṃ": "निर्दिष्ट करना चाहिए", "niyāmetabbā": "निर्दिष्ट करना चाहिए",
    "uddharitabbo": "अलग करके लेना चाहिए", "vibhajitabbo": "करना चाहिए", "vibhajitabbāni": "विभाजन करना चाहिए",
    "labbhati": "मिलना", "likhitaṃ": "लिखा गया",
    "gaṇanā": "गणना", "gaṇanāpi": "गणना",
    "ninnānākaraṇaṃ": ("बिना किसी अंतर के", "कोई भिन्नता नहीं"), "ninnānākaraṇā": "बिना किसी अंतर के",
    "āmasanaṃ": "पदों का उल्लेख", "āmasanā": "पदों का उल्लेख",
    "pākatikā": "सामान्य", "avasesā": "बाकी", "avasesesu": "बाकी",
    "sahajāta": "सह-उत्पत्ति", "saṃsaṭṭha": "घुले-मिले होने",
    "pavattipaṭisandhi": "जीवन-काल और पुनर्जन्म", "paṭisandhiyāpi": "पुनर्जन्म", "paripuṇṇā": "पूरा",
    "pañcapi": "पाँचों", "sabbatthameva": "हर जगह", "cakkaṃ": "चक्र", "nti": "ऐसा",
    "natthi": "नहीं है",
    "suddhake": "शुद्ध पद", "arūpamissake": "अभौतिक-मिश्रित पद",
    "pahātabbabhājanakāraṇe": "छोड़े जाने वाले के विभाजन के कारण",
    "dutiyagamanasadisaṃ": "दूसरे प्रसंग के समान", "dutiyagamanasadisā": "दूसरे प्रसंग के समान",
    "dutiyavārasadisaṃ": "दूसरे खंड के समान", "dutiyavāre": "दूसरा खंड",
    "anulomapaccayavāraṃ": "सकारात्मक क्रम का कारण का खंड",
    "anulomapaṭiccavāro": "सकारात्मक क्रम वाला निर्भरता का खंड",
    # «X वाले दो के वर्गीकरण के समान» and dyad references
    "kilesadukasadisaṃ": "मन के क्लेश वाले दो के वर्गीकरण के समान",
    "kilesadukasadisā": "मन के क्लेश वाले दो के वर्गीकरण के समान",
    "arūpadukasadisaṃ": "अभौतिक लोक वाले दो के वर्गीकरण के समान",
    "arūpadukasadisā": "अभौतिक लोक वाले दो के वर्गीकरण के समान",
    "arūpāvacaradukasadisaṃ": "अभौतिक लोक वाले दो के वर्गीकरण के समान",
    "arūpāvacaradukasadisā": "अभौतिक लोक वाले दो के वर्गीकरण के समान",
    "lokiyadukasadisaṃ": "लौकिक वाले दो के वर्गीकरण के समान",
    "sappītikadukasadisaṃ": "उल्लास वाले दो के वर्गीकरण के समान",
    "sappītikadukasadisā": "उल्लास वाले दो के वर्गीकरण के समान",
    "pahātabbahetukadukasadisā": "छोड़े जाने वाले मूलों वाले दो के वर्गीकरण के समान",
    "savitakkadukassa": "आरंभिक विचार वाला दो का वर्गीकरण", "savitakkaduke": "आरंभिक विचार वाला दो का वर्गीकरण",
    "savicāraduke": "सतत विचार वाला दो का वर्गीकरण",
    "sappītikadukassa": "उल्लास वाला दो का वर्गीकरण", "sappītikaduke": "उल्लास वाला दो का वर्गीकरण",
    "arūpāvacaradukassa": "अभौतिक लोक वाला दो का वर्गीकरण",
    "cūḷantaraduke": "बीच के छोटे दो-दो के वर्गीकरण",
    "dassanadukaṃ": "सत्य-दर्शन से छोड़े जाने वाला दो का वर्गीकरण",
})
for _st, _name, _loc, _neg, _plain in CONDITIONS:          # «Anantarapaccaye …» = «निकटता-कारण में»
    T[_st + "paccaye"] = _name
for _k in ("kātabbo", "kātabbā"):
    T[_k] = T["kātabbaṃ"]
# «(Mūlaṃ kātabbaṃ.)» = «(मूल वाक्य बनाना चाहिए।)» (86 of 95 occurrences): बनाना first
T["kātabbaṃ"] = ("बनाना चाहिए", "तैयार करना चाहिए", "लेना चाहिए", "शामिल करना चाहिए", "करना चाहिए")
# PI7 words with a second reading in this file (tuple: the first present in the segment wins)
T.update({
    "pāṇaṃ": ("जीव", "प्राणी"),                                   # «प्राणी की हत्या करता है»
    "lokiyadukaṃ": ("लौकिक परिघटनाओं वाला दो का वर्गीकरण", "लौकिक वाला दो का वर्गीकरण"),
    "sekkhā": ("सीखने के चरण का", "सीखने के चरण वाला"),          # «सीखने के चरण वाले गोत्र-परिवर्तन»
    "anulomaṃ": ("सकारात्मक क्रम", "अनुरूपता"),                  # moment before gotrabhu (harmonise M1)
    "anantarā": ("ठीक बाद", "निकटता-कारण"),                       # «अन्य दो निकटता-कारण …» (note)
    "katvā": ("देकर", "करके"),                                    # «उपवास-व्रत का पालन करके»
    "pacchājātā": ("बाद में उत्पन्न", "पश्चात्-उत्पत्ति"),          # label «(तीन, पश्चात्-उत्पत्ति रूपी)»
    "kusalākusalaṃ": ("हितकर और हानिकर", "हितकर या हानिकर"),      # «हितकर या हानिकर मन»
    "āmasanaṃ": ("पदों का उल्लेख", "उल्लेख"), "āmasanā": ("पदों का उल्लेख", "उल्लेख"),
    "vipāke": ("कर्म-फल-कारण", "कर्म के फल रूपी", "कर्म-फल रूपी"),
    "karoti": ("पालन करना", "करना"),                              # «कस्बे पर हमला करता है»
    "vibhajitabbāni": "विभाजन … करना चाहिए",
    "pahātabbahetukādhipati": ("छोड़े जाने वाले मूलों वाली प्रधानता", "छोड़े जाने वाले मूल … प्रधानता"),
    "rūpaṃ": ("भौतिक रूप", "दृश्य रूप"),                           # «दिव्य आँख से दृश्य रूप देखता है»
})
# heading «Nahetu-naārammaṇapaccayā» = «मूल-कारण का अभाव और विषय-कारण का अभाव» (noun, not ablative)
OVR = {b: {"naārammaṇapaccayā": "विषय-कारण का अभाव"}
       for b in ("7-4-1-1-275-1-0", "7-4-1-1-306-1-0", "7-4-1-1-335-1-0")}
OVR["7-34-8"] = {"paccayā": "कारण"}            # «(Evaṃ sabbe paccayā kātabbā.)» = «सभी कारणों के साथ» (noun)


def _hetuka_ctx(kws):
    return any("pahātabbahetuk" in lc(x) for x in kws)


CTX = {   # (kw lower) -> function(kws) returning a value or None (context rules)
    "nadassanena": lambda kws: "सत्य-दर्शन … रहित" if _hetuka_ctx(kws) else None,
    "nabhāvanāya": lambda kws: "मानसिक अभ्यास … रहित" if _hetuka_ctx(kws) else None,
}

ALLOWED = {}


def resolver_factory():
    base = make_resolver(F, {**PI7, **T}, OVR)

    def res(bid, kw, kws):
        if kw not in OVR.get(bid, {}):
            f = CTX.get(lc(kw))
            if f:
                v = f(kws)
                if v is not None:
                    return v
        return base(bid, kw, kws)
    return res


if __name__ == "__main__":
    if "--missing" in sys.argv:
        tab = {**PI7, **T}
        hi, pa = read_hindi(F), read_pali(F)
        miss = collections.Counter()
        for bid, kws in read_keywords(F):
            for kw in kws:
                if kw in OVR.get(bid, {}):
                    continue
                try:
                    pi7_value(kw, kws, tab, pa.get(bid), hi.get(bid))
                except KeyError:
                    miss[kw] += 1
        for k, c in sorted(miss.items(), key=lambda x: lc(x[0])):
            print(c, k)
        sys.exit()
    build_part(F, resolver_factory())
    verify(F, show=400, allowed=ALLOWED)
    if "--audit" in sys.argv:
        audit(F, {**PI7, **T}, OVR, only_fallback="--all" not in sys.argv)
