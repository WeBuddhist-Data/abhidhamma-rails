"""pi-7 Pāli->Hindi keyword map for 3-09-mahantaraduka (the great intermediate dyads), following
hi-map-conventions-pi7.md. Imports map_sample_hi read-only; chapter additions in T, per-segment overrides in OVR.
usage: python -I -B -X utf8 map_3-09_hi.py            (build + verify + fallback audit)
Importing this file (probe_3-09_hi.py does) builds nothing.
"""
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import *  # noqa: E402,F401
from map_sample_hi import headnames  # noqa: E402

F = "3-09-mahantaraduka"
KAT = ("तैयार करना चाहिए", "बनाना चाहिए", "करना चाहिए")   # «तैयार करनी/करने चाहिए», «बनानी चाहिए» (mātikā)

T = {}

# --- dyad items of the Mahantaraduka (items_sample_hi.py on this file): masc. sg. of the frame wording.
# Cluster-like items keep the plain term (citta = मन, as gantha = गाँठ); the negative keeps «… न होने वाला».
ITEMS = {
    "sārammaṇ": "विषय वाला", "anārammaṇ": "विषय से रहित",
    "citt": "मन", "nocitt": "मन रूपी न होने वाला",
    "cetasik": "मन का सहचर", "acetasik": "मन का सहचर न होने वाला",
    "cittasampayutt": "मन से जुड़ा", "cittavippayutt": "मन से अलग",
    "cittasaṃsaṭṭh": "मन से घुला-मिला", "cittavisaṃsaṭṭh": "मन से घुला-मिला न होने वाला",
    "cittasamuṭṭhān": "मन से उत्पन्न", "nocittasamuṭṭhān": "मन से उत्पन्न न होने वाला",
    "cittasaṃsaṭṭhasamuṭṭhān": "मन से घुला-मिला और मन से उत्पन्न",
    "nocittasaṃsaṭṭhasamuṭṭhān": "मन से घुला-मिला और मन से उत्पन्न न होने वाला",
    "ajjhattik": "आंतरिक", "bāhir": "बाह्य",
    "upādinn": "कर्म से उत्पन्न", "anupādinn": "कर्म से उत्पन्न न होने वाला",
}
A_END = ("aṃ", "o", "ā", "assa", "ānaṃ", "e", "añca", "a", "ānañca", "āni", "esu", "ena", "aṃyeva")
for _st, _h in ITEMS.items():
    for _e in A_END:
        T[_st + _e] = _h
# ū/u-stems (sahabhū) and i-stems (anuparivatti)
SAHABHU = {"cittasahabh": "मन के साथ-साथ होने वाला", "nocittasahabh": "मन के साथ-साथ न होने वाला",
           "cittasaṃsaṭṭhasamuṭṭhānasahabh": "मन से घुला-मिला मन से उत्पन्न और मन के साथ-साथ होने वाला",
           "nocittasaṃsaṭṭhasamuṭṭhānasahabh":
               "मन से घुला-मिला मन से उत्पन्न और मन के साथ-साथ न होने वाला"}
for _st, _h in SAHABHU.items():
    for _e in ("ū", "u", "uṃ", "ussa", "ūnaṃ", "ūnañca", "uñca", "ū ca"):
        T[_st + _e] = _h
ANUP = {"cittānuparivatt": "मन का अनुसरण करने वाला", "nocittānuparivatt": "मन का अनुसरण न करने वाला",
        "cittasaṃsaṭṭhasamuṭṭhānānuparivatt": "मन से घुला-मिला मन से उत्पन्न और मन का अनुसरण करने वाला",
        "nocittasaṃsaṭṭhasamuṭṭhānānuparivatt":
            "मन से घुला-मिला मन से उत्पन्न और मन का अनुसरण न करने वाला"}
for _st, _h in ANUP.items():
    for _e in ("i", "iṃ", "ī", "ino", "issa", "īnaṃ", "iñca"):
        T[_st + _e] = _h
T.update({"upādā": "व्युत्पन्न", "noupādā": "व्युत्पन्न न होने वाला"})

# --- «X-duke» (locative) = the dyad name; «X-dukasadisaṃ / -ā» = «… वाले दो के वर्गीकरण के समान»
for _k, _v in list(headnames().items()):
    if _k.endswith("dukaṃ") and _v.endswith("वाला दो का वर्गीकरण") and "-" not in _k:
        _s = _k[:-2]
        T.setdefault(_s + "e", _v)
        _obl = _v[: -len("वाला दो का वर्गीकरण")] + "वाले दो के वर्गीकरण के समान"
        for _e in ("asadisaṃ", "asadisā"):
            T.setdefault(_s + _e, _obl)

# --- chapter vocabulary (read in the segments)
T.update({
    "cetasikaṃ": "मन का सहचर", "cetasiko": "मन का सहचर",          # not CH2 «मानसिक»: the pi-7 text has «मन की सहचर»
    "vicikicchāsahagate": "संशय के साथ होने वाला", "vicikicchāsahagato": "संशय के साथ होने वाला",
    "vicikicchāsahagataṃ": "संशय के साथ होने वाला",
    "uddhaccasahagate": "बेचैनी के साथ होने वाला", "uddhaccasahagato": "बेचैनी के साथ होने वाला",
    "uddhaccasahagataṃ": "बेचैनी के साथ होने वाला",
    "moho": "मोह", "rāgassa": "राग",
    "kātabbā": KAT, "kātabbaṃ": KAT, "kātabbo": KAT, "kātabbāni": KAT,
    "yāva": "तक", "asaññasattā": "पहचान-रहित प्राणी",
    "ninnānākaraṇaṃ": "बिना किसी अंतर के", "ninnānākaraṇā": "बिना किसी अंतर के",
    "paṭhamagamanasadisaṃ": "पहले प्रसंग के समान", "gamanā": "प्रसंग",
    "cetopariyañāṇena": "दूसरों के मन को जानने का ज्ञान",
    "cakkhuviññāṇasahagatānaṃ": "आँख की चेतना के साथ होने वाला",
    "cakkhuviññāṇasahagatā": "आँख की चेतना के साथ होने वाला",
    "cakkhuviññāṇasahagataṃ": "आँख की चेतना के साथ होने वाला",
    "cakkhuviññāṇasahagate": "आँख की चेतना के साथ होने वाला",
    "kāyaviññāṇasahagatānaṃ": "शरीर की चेतना के साथ होने वाला",
    "kāyaviññāṇasahagatā": "शरीर की चेतना के साथ होने वाला",
    "kāyaviññāṇasahagataṃ": "शरीर की चेतना के साथ होने वाला",
    "kāyaviññāṇasahagate": "शरीर की चेतना के साथ होने वाला",
    "pañcaviññāṇasahagataṃ": "पाँच प्रकार की चेतना के साथ होने वाला",
    "pañcaviññāṇaṃ": "पाँच प्रकार की चेतना",
    "nibbānaṃ": "निर्वाण", "dvepi": "दोनों",
    "āhāraṃ": "आहार", "kabaḷīkāraṃ": "कौर-कौर खाया जाने वाला",
    "anulomamātikā": "सकारात्मक क्रम की मूल सूची",
    "purimaṃ": "पहले-पहले का", "pacchimassa": "बाद-बाद का",
    "vuṭṭhānassa": "बाहर आना", "pūretukāmena": "पूरा करना चाहने वाला",
    "garukārammaṇā": "महत्व दिए गए विषय वाला",
    "pavattipaṭisandhiyā": ("जीवन-प्रवाह और पुनर्जन्म", "जीवन-प्रवाह … पुनर्जन्म"),
    "pavattipaṭisandhi": ("जीवन-प्रवाह और पुनर्जन्म", "जीवन-प्रवाह … पुनर्जन्म"),
    "asammohantena": "बिना भ्रमित हुए", "uppajanti": "उत्पन्न होना",
    "upanissayā": "प्रबल आश्रय", "sampayuttake": "जुड़ा हुआ",
    "ahetukā": "मूल से रहित", "ahetuke": "मूल से रहित",
    "natthi": ("नहीं", "न … है"), "atthi": "उपस्थिति-कारण",
    "itare": ("अन्य", "बाकी"), "gaṇanāpi": "गणना", "gaṇanā": "गणना",
    "iminākāreneva": "इसी ढंग से", "pañhānaṃ": "प्रश्न", "pañhesu": "प्रश्न",
    "arūpaṃ": "अभौतिक", "uddharitabbaṃ": "निकाल लेना चाहिए", "niyāmetabbaṃ": "निश्चित करना चाहिए",
    "labbhati": "मिलना", "ekāyeva": "केवल एक", "adhipatī": "प्रधानता",
    "cittasamuṭṭhānādhipati": "मन से उत्पन्न प्रधानता",
    "cakkaṃ": "चक्र", "pavesetvā": "शामिल करके", "ekasadisā": "एक जैसा",
    "sabbaṭṭhāne": "हर स्थान", "padā": "पद",
    "vibhajitabbā": "विश्लेषण करना चाहिए", "vibhajitabbāni": "विश्लेषण करना चाहिए",
    "vitthāretabbāni": "विस्तार करना चाहिए",
    "bāhiracittasamaṅgissa": "बाह्य मन से युक्त व्यक्ति",
    "noupādācittasamaṅgissa": "व्युत्पन्न न होने वाले मन से युक्त व्यक्ति",
    "kusalākusale": "हितकर और हानिकर", "niruddhe": "समाप्त होना", "tadārammaṇatā": "उसी विषय को लेकर",
    "ākāsānañcāyatanakusalaṃ": "अनंत आकाश के क्षेत्र का हितकर मन",
    "viññāṇañcāyatanavipākassa": "अनंत चेतना के क्षेत्र का कर्म के फल रूपी मन",
    "vipākamanoviññāṇadhātu": "कर्म के फल रूपी मन की चेतना का तत्व",
    "vipākamanodhātuyā": "कर्म के फल रूपी मन का तत्व",
    "bhavaṅgaṃ": "भवांग", "āvajjanā": "मन को विषय की ओर मोड़ना", "viññāṇānaṃ": "चेतना",
    "attānaṃ": "स्वयं", "ātāpeti": "तपाना", "paritāpeti": "कष्ट देना",
    "pariyiṭṭhimūlakaṃ": "खोज के कारण होने वाला", "vipākassa": "कर्म-फल",
    "upādinnamūlake": "कर्म से उत्पन्न परिघटना से शुरू होने वाली शृंखला",
    "paṭhamasseva": "केवल पहले",
    # members of the paired condition headings «Kamma-vipākapaccayā» = «कर्म-कारण और कर्म-फल-कारण»
    "kamma": "कर्म-कारण", "vipāka": "कर्म-फल-कारण", "anantara": "निकटता-कारण",
    "gaṇhāti": ("ग्रहण करना", "अपनाना"),                         # «दृष्टि अपनाता है»
    # PI7 values plus the wording this file uses
    "katvā": ("देकर", "पालन करके"),                                # «उपवास-व्रत का पालन करके» where no «महत्व देकर»
    "rūpaṃ": ("भौतिक रूप", "दृश्य रूप"),                            # «dibbena cakkhunā rūpaṃ passati» = «दृश्य रूप देखता है»
    "pāṇaṃ": ("जीव", "प्राणी"),                                    # «प्राणी की हत्या करता है»
    "vaṇṇasampadaṃ": ("रंग-रूप की संपन्नता", "रूप-रंग की संपन्नता"),
})

# per-segment overrides (exact keyword spelling); reasons in the report
OVR = {
    "7-32-305": {"āhāraṃ": "भोजन"},            # «ekaṃyeva kabaḷīkāraṃ āhāraṃ» = «केवल एक कौर-कौर खाया जाने वाला भोजन»
    # «anulomaṃ gotrabhussa» = the conformity moment, text «अनुरूपता गोत्र-परिवर्तन के लिए», not the method
    "7-32-126": {"anulomaṃ": "अनुरूपता"}, "7-32-397": {"anulomaṃ": "अनुरूपता"},
    "7-32-450": {"anulomaṃ": "अनुरूपता"},
    # «Tīṇipi pacchājātā» = «तीनों में पश्चात्-उत्पत्ति रूपी» (the bare label)
    "7-32-304": {"pacchājātā": "पश्चात्-उत्पत्ति"},
    # «kusalākusale niruddhe vipāko tadārammaṇatā uppajjati» = «… कर्म-फल उसी विषय को लेकर उत्पन्न होता है»
    "7-32-447": {"vipāko": "कर्म-फल"}, "7-32-464": {"vipāko": "कर्म-फल"},
    # «Yathā cittasahabhūduke ārammaṇaṃ evaṃ kātabbaṃ» = «… दो के वर्गीकरण में विषय-कारण, वैसे ही …»
    "7-32-301": {"ārammaṇaṃ": "विषय-कारण"},
}
ALLOWED = {
    ("7-32-362", "padā"): "«Sabbe padā» = «सभी पदों»: plural oblique of पद; the checker does not inflect 2-letter words",
}

if __name__ == "__main__":
    build_part(F, make_resolver(F, {**PI7, **T}, OVR))
    verify(F, show=400, allowed=ALLOWED)
