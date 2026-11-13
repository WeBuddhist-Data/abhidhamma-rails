"""pi-7 Pāli->Hindi keyword maps for 1-03-vipakattika, 1-04-upadinnattika, 1-05-sankilitthattika,
2-01-vitakkattika. Built on map_sample_hi.py (imported read-only) and hi-map-conventions-pi7.md.

usage: python -I -B -X utf8 map_1-03_2-01_hi.py [file …]   (default: all four; writes <file>.mapped.md)
Importing this module writes nothing (T and OVRS are used by the probe/audit helpers).
"""
import sys, pathlib
sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import *  # noqa: F401,F403
from map_sample_hi import PI7, NDE, build_part, make_resolver, verify, audit

FILES = ("1-03-vipakattika", "1-04-upadinnattika", "1-05-sankilitthattika", "2-01-vitakkattika")

T = {}

# ---------------------------------------------------------------- triad items of these four triads
# vipāka triad (pi-1 1-matika; Hindi «कर्म-फल रूपी / कर्म-फल उत्पन्न करने वाली / न कर्म-फल रूपी, न …»)
NEVA_V = "न कर्म-फल रूपी न कर्म-फल उत्पन्न करने वाला"          # comma of the Hindi dropped
for _e in ("o", "aṃ", "assa", "añca", "ā", "e", "ānaṃ", "a"):
    T["nevavipākanavipākadhammadhamm" + _e] = NEVA_V
    T["vipākadhammadhamm" + _e] = "कर्म-फल उत्पन्न करने वाला"
T.update({
    "vipākādhipati": "कर्म-फल रूपी प्रधानता",
    "vipākadhammadhammādhipati": "कर्म-फल उत्पन्न करने वाली प्रधानता",
    "nevavipākanavipākadhammadhammādhipati": "न कर्म-फल रूपी न कर्म-फल उत्पन्न करने वाली प्रधानता",
    "vipākadhammadhammacittasamaṅgissa": "कर्म-फल उत्पन्न करने वाले मन से युक्त व्यक्ति",
    "nevavipākanavipākadhammadhammacittasamaṅgissa": "न कर्म-फल रूपी न कर्म-फल उत्पन्न करने वाले मन से युक्त व्यक्ति",
    "vipākacittasamaṅgissa": "कर्म-फल रूपी मन से युक्त व्यक्ति",
    "vipākassa": ("कर्म-फल रूपी", "कर्म के फल रूपी", "कर्म-फल"),
    "vicākānaṃ": ("कर्म के फल रूपी", "कर्म-फल रूपी"),          # Pāli slip for vipākānaṃ (builder)
    "vipāke": ("कर्म-फल रूपी", "कर्म के फल रूपी"),
})

# ---------------------------------------------------------------- headings: members of «X-Ypaccayā»
T.update({
    "kamma": ("कर्म-कारण", "कर्म"), "anantara": "निकटता-कारण", "upanissaya": "प्रबल आश्रय-कारण",
    "natthi": "अनुपस्थिति-कारण", "nonatthi": "अनुपस्थिति-कारण का अभाव", "atthi": "उपस्थिति-कारण",
    "vigatāvigatapaccayā": "विलीनता-कारण और अविलीनता-कारण",
    "sahajāta": ("सह-उत्पत्ति-कारण", "सह-उत्पत्ति"), "nissaya": ("आश्रय-कारण", "आश्रय"),
    "aññamañña": "परस्पर-कारण", "avigatanti": "अविलीनता-कारण", "avigataṃ": "अविलीनता-कारण",
    "vigataṃ": "विलीनता-कारण", "purejāta": "पूर्व-उत्पत्ति",
    "saṃsaṭṭha": "घुला-मिला होना",                                 # vāra name «घुले-मिले होने का खंड»
})

# ---------------------------------------------------------------- Pañhāvāra vocabulary
T.update({
    "cetopariyañāṇena": "दूसरों के मन को जानने का ज्ञान",
    "vicikicchāsahagate": "संशय के साथ होने वाला", "vicikicchāsahagato": "संशय के साथ होने वाला",
    "vicikicchāsahagataṃ": "संशय के साथ होने वाला",
    "uddhaccasahagate": "बेचैनी के साथ होने वाला", "uddhaccasahagato": "बेचैनी के साथ होने वाला",
    "uddhaccasahagataṃ": "बेचैनी के साथ होने वाला",
    "moho": "मोह", "doso": "द्वेष", "māno": "अहंकार", "dosaṃ": "द्वेष", "mohaṃ": "मोह",
    "rāgassa": "राग", "dosassa": "द्वेष", "mohassa": "मोह", "mānassa": "अहंकार", "diṭṭhiyā": "दृष्टि",
    "cāgaṃ": "त्याग", "cāgo": "त्याग", "cāgassa": "त्याग",
    "sutaṃ": "सुना-सीखा ज्ञान", "sutassa": "सुना-सीखा ज्ञान", "dukkhassa": "दुःख", "sukhassa": "सुख",
    "arahā": "अर्हत्", "puthujjanā": "साधारण व्यक्ति",
    "sekkhā": "सीखने के चरण वाला", "sekkhānaṃ": "सीखने के चरण वाला",
    "assādenti": "रस लेना", "abhinandanti": "आनंद लेना", "vipassanti": "अंतर्दृष्टि से देखना",
    "niruddhe": "समाप्त होना", "tadārammaṇatā": "उसी विषय को लेकर",
    "kusalākusale": "हितकर और हानिकर",
    "nibbānaṃ": "निर्वाण", "gotrabhuṃ": "गोत्र-परिवर्तन", "phalā": "फल",
    "āhāraṃ": ("आहार", "आहार रूपी"), "indriyaṃ": ("क्षमता", "क्षमता रूपी"),
    "parikammaṃ": "प्रारंभिक तैयारी", "jhānassa": "ध्यान",
    "paṭhamassa": "पहला", "dutiyassa": "दूसरा", "tatiyassa": "तीसरा", "catutthassa": "चौथा",
    "paṭhamo": "पहला", "dutiyo": "दूसरा", "tatiyo": "तीसरा",
    "pāṇātipāto": "प्राणी-हत्या", "pāṇātipātassa": "प्राणी-हत्या", "byāpādassa": "दुर्भावना",
    "micchādiṭṭhi": "ग़लत दृष्टि", "micchādiṭṭhiyā": "ग़लत दृष्टि",
    "mātughātikammaṃ": "माता की हत्या का कर्म", "mātughātikammassa": "माता की हत्या का कर्म",
    "niyatamicchādiṭṭhi": "नियत ग़लत दृष्टि", "niyatamicchādiṭṭhiyā": "नियत ग़लत दृष्टि",
    "saṅghabhedakakammassa": "संघ में फूट डालने का कर्म",
    "attānaṃ": "स्वयं", "ātāpeti": "तपाना", "paritāpeti": "कष्ट देना",
    "pariyiṭṭhimūlakaṃ": "खोज के कारण होने वाला", "paccanubhoti": "भोगना",
    "kiriyasamāpattiṃ": "केवल क्रिया रूपी ध्यान-अवस्था", "kusalasamāpattiṃ": "हितकर ध्यान-अवस्था",
    "samāpajjati": "प्रवेश करना", "samāpajjanti": "प्रवेश करना",
    "anuppannaṃ": "उत्पन्न न हुआ", "uppannaṃ": "उत्पन्न हो चुका",
    "uppādenti": "उत्पन्न करना", "saṅkhāre": "मानसिक रचनाएँ",
    "atthappaṭisambhidāya": "अर्थ का विश्लेषणात्मक ज्ञान",
    "dhammappaṭisambhidāya": "परिघटनाओं का विश्लेषणात्मक ज्ञान",
    "niruttippaṭisambhidāya": "भाषा का विश्लेषणात्मक ज्ञान",
    "paṭibhānappaṭisambhidāya": "सूझ-बूझ का विश्लेषणात्मक ज्ञान",
    "ṭhānāṭhānakosallassa": "संभव और असंभव को जानने की कुशलता",
    "hantvā": "हत्या करके", "bhinditvā": "फूट डालकर", "paṭighātatthāya": "निवारण",
    "pañcaviññāṇaṃ": "पाँच प्रकार की चेतना", "pañcaviññāṇasahagataṃ": "पाँच प्रकार की चेतना के साथ होने वाला",
    "viññāṇānaṃ": "चेतना", "pañcannaṃ": "पाँच",
    "bhavaṅgaṃ": "जीवन-धारा", "bhavaṅgañca": "जीवन-धारा", "bhavaṅgassa": "जीवन-धारा",
    "vuṭṭhānassa": "बाहर आना", "āvajjanā": "मन को विषय की ओर मोड़ना",
    "cuticittaṃ": "मृत्यु का मन", "cuticittañca": "मृत्यु का मन", "upapatticittassa": "जन्म का मन",
    "vipākamanodhātu": "कर्म के फल रूपी मन का तत्व", "vipākamanodhātuyā": "कर्म के फल रूपी मन का तत्व",
    "vipākamanoviññāṇadhātu": "कर्म के फल रूपी मन की चेतना का तत्व",
    "vipākamanoviññāṇadhātuyā": "कर्म के फल रूपी मन की चेतना का तत्व",
    "kiriyamanoviññāṇadhātuyā": "केवल क्रिया रूपी मन की चेतना का तत्व",
    "sota": "कान", "ghāna": "नाक", "jivhā": "जीभ", "kāya": "शरीर",
    "suṇanti": "सुनना", "passanti": "देखना",
    "jhānaṅgā": "ध्यान का अंग", "maggaṅgā": "मार्ग का अंग",
    "arahato": "अर्हत्", "ariyānaṃ": "आर्य",
    "pacchājātā": ("बाद में उत्पन्न", "पश्चात्-उत्पत्ति"),
    "adhipati": "प्रधानता",
})
for _p, _h in (("cakkhu", "आँख"), ("sota", "कान"), ("ghāna", "नाक"), ("jivhā", "जीभ"), ("kāya", "शरीर")):
    for _e in ("aṃ", "ānaṃ", "o", "e", "assa"):
        T[f"{_p}viññāṇasahagat{_e}"] = f"{_h} की चेतना के साथ होने वाला"
# formless-sphere minds «X के क्षेत्र का हितकर / कर्म के फल रूपी / केवल क्रिया रूपी मन»
for _k, _h in (("ākāsānañcāyatana", "अनंत आकाश के क्षेत्र"), ("viññāṇañcāyatana", "अनंत चेतना के क्षेत्र"),
               ("ākiñcaññāyatana", "कुछ भी न होने के क्षेत्र"),
               ("nevasaññānāsaññāyatana", "न पहचान न अ-पहचान के क्षेत्र")):
    for _q, _hq in (("kusal", "हितकर"), ("vipāk", "कर्म के फल रूपी"), ("kiriy", "केवल क्रिया रूपी")):
        for _e in ("aṃ", "assa"):
            T[f"{_k}{_q}{_e}"] = f"{_h} का {_hq} मन"
    T[_k + "ssa"] = _h.replace("के क्षेत्र", "का क्षेत्र")          # ākiñcaññāyatanassa = कुछ भी न होने का क्षेत्र

# ---------------------------------------------------------------- numbers and instructions
T.update({
    "ekā": "एक", "terasa": "तेरह", "dvādasa": "बारह", "ekādasa": "ग्यारह", "sattarasa": "सत्रह",
    "soḷasa": "सोलह", "cuddasa": "चौदह", "pannarasa": "पंद्रह", "tevīsa": "तेईस", "sattatiṃsa": "सैंतीस",
    "ekavīsa": "इक्कीस", "tettiṃsa": "तैंतीस", "aṭṭhavīsa": "अट्ठाईस", "bāvīsa": "बाईस",
    "pañcavīsa": "पच्चीस", "tiṃsa": "तीस", "pañcatiṃsa": "पैंतीस", "ekūnatiṃsa": "उनतीस",
    "catuttiṃsa": "चौंतीस", "sattavīsa": "सत्ताईस", "sattasu": "सात",
    "padāni": "पद", "vitthāretabbāni": "विस्तार करना चाहिए", "vibhajitabbāni": "विश्लेषण करना चाहिए",
    "vibhajitabbā": "विश्लेषण करना चाहिए", "vibhajitabbaṃ": "विश्लेषण करना चाहिए",
    "paccanīyagaṇanā": "नकारात्मक क्रम की गणना", "gaṇanā": "गणना", "gaṇitā": "गिना गया",
    "kusalattikassa": "हितकर वाला तीन का वर्गीकरण", "upādinnattike": "कर्म से उत्पन्न वाला तीन का वर्गीकरण",
    "sajjhāyamaggena": "पाठ का क्रम", "sajjhāyamaggo": "पाठ का क्रम",
    "asammohantena": "बिना भ्रमित हुए",
    "gambhīrā": "गहरा", "sukhumatarā": "अधिक सूक्ष्म", "paripuṇṇaṃ": "पूरा",
    "kātabbā": ("जोड़ना चाहिए", "बनाना चाहिए"), "kātabbaṃ": ("बनाना चाहिए", "जोड़ना चाहिए"),
    "kātabbo": ("बनाना चाहिए", "जोड़ना चाहिए"),
    "vitthāretabbo": ("विस्तार करना चाहिए", "विस्तार से कहना चाहिए"),
    "gaṇetabbaṃ": ("गिनना चाहिए", "करना चाहिए"), "gaṇetabbā": ("गिनना चाहिए", "करना चाहिए"),
    "mūlakaṃ": "शृंखला",                                            # «(mūlakaṃ saṃkhittaṃ)» = «(शृंखला संक्षिप्त)»
    "avasesā": ("बाकी", "शेष"), "avasesesu": ("बाकी", "शेष"), "vīsatipaccayā": "बीस कारण",
    "āgacchati": "आना", "suddhikaṃ": "अकेले कारण वाला खंड", "gacchantena": "लेते हुए",
    "dassetabbo": "दिखाना चाहिए", "dīpetabbā": "दिखाना चाहिए", "paṭhamaudāharaṇe": "पहला उदाहरण",
    "uddharitabbā": "उद्धृत करना चाहिए", "ṭhānesu": "स्थान", "paripuṇṇā": "पूरा",
    "anumajjantena": "अनुसरण करते हुए",
    "avitakkavicāramattamūlakā": "आरंभिक विचार से रहित केवल सतत विचार वाली परिघटना से शुरू होने वाला",
})

# ---------------------------------------------------------------- vitakka triad: the bare factors
for _e in ("o", "aṃ", "assa", "añca", "ā", "e", "ānaṃ"):
    T["vitakk" + _e] = "आरंभिक विचार"
    T["vicār" + _e] = "सतत विचार"
T.update({"dibbassa": "दिव्य", "cakkhussa": "आँख", "purimo": "पहले-पहले का",
          "pacchimassa": "बाद-बाद का", "ahetuke": "मूल से रहित",
          "rūpaṃ": ("भौतिक रूप", "दृश्य रूप"),
          "pāṇaṃ": ("जीव", "प्राणी"),
          "vipāko": ("कर्म-फल रूपी", "कर्म के फल रूपी", "कर्म-फल"),
          "sajjhāyamaggena": ("पाठ का क्रम", "पाठ करने का क्रम"),
          "saṃkiliṭṭhasaṃkilesikacittasamaṅgissa": "क्लेशों से मलिन और क्लेशों का विषय बनने वाले मन से युक्त व्यक्ति",
          "asaṃkiliṭṭhasaṃkilesikādhipati": "क्लेशों से मलिन न होने वाली पर क्लेशों का विषय बनने वाली प्रधानता",
          "naanantarampi": "निकटता-कारण का अभाव",
          "gaṇitā": ("गिना गया", "गणना की गई"),                     # «… की गणना की गई है»
          "anulomañca": ("सकारात्मक क्रम", "अनुरूपता"),            # javana «anulomañca vitakko ca» = अनुरूपता
          })
# bare negative condition stems in the abbreviated lists «Naāhāra-naindriya-…-nonatthi-novigatapaccayā»
for _st, _name, _loc, _neg, _plain in CONDITIONS:
    T.setdefault(_neg + _st, f"{_name} का अभाव")

# per-segment overrides {file: {bid: {kw: value}}}
OVRS = {f: {} for f in FILES}
# «Kusalākusale niruddhe vipāko tadārammaṇatā» = «कर्म-फल उसी विषय को लेकर»; the segment also has
# «… के कर्म के फल रूपी मन», which the tuple would pick
OVRS["1-04-upadinnattika"]["7-5-53"] = {"vipāko": "कर्म-फल"}
# label «– sahajātā, nānākkhaṇikā» = «सह-उत्पत्ति, भिन्न क्षण»; the segment also has one «के साथ जन्म लेकर»
OVRS["1-05-sankilitthattika"]["7-6-20"] = {"sahajātā": "सह-उत्पत्ति"}
# «Hetu-sahajāta-nissaya-vippayutta-atthi-avigatanti» = the condition names
OVRS["1-05-sankilitthattika"]["7-6-32"] = {"vippayutta": "अलगाव-कारण"}
# presence exceptions {file: {(bid, kw): reason}}
ALLOWED = {f: {} for f in FILES}
_PADA = "पद ~ «पदों»: the checker does not inflect a two-letter word"
ALLOWED["1-03-vipakattika"].update({("7-4-77", "padāni"): _PADA, ("7-4-83", "padāni"): _PADA,
                                   ("7-4-85", "padāni"): _PADA})
_AA = "आना ~ «आती है»: the checker does not inflect a one-letter verb stem"
ALLOWED["2-01-vitakkattika"].update({("7-7-52", "āgacchati"): _AA, ("7-7-53", "āgacchati"): _AA})

if __name__ == "__main__":
    files = sys.argv[1:] or FILES
    for f in files:
        build_part(f, make_resolver(f, {**PI7, **T}, OVRS[f]))
        verify(f, allowed=ALLOWED[f])
