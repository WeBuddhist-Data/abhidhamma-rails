"""pi-2 Pāli->Hindi keyword map: 9-iddhipadavibhango.

usage: python -I -X utf8 map_9-iddhipadavibhango_hi.py
Imports map_sample_hi (read-only) and the shared table of chapters 2/3/8/9; extends them here only.
"""
import importlib
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import PP_SEGMENTS, NDE, build_part, verify, read_hindi  # noqa: E402
C = importlib.import_module("map_2-3-8-9_common_hi")

CH = "9-iddhipadavibhango"
PP_SEGMENTS.update({"2-464", "2-465"})

IP = "सिद्धि का आधार"

T = {
    # the iddhipāda names
    "iddhi": "सिद्धि", "pāda": "आधार", "pādā": "आधार", "pādānaṃ": "आधार",
    "iddhipāda": IP, "iddhipādo": IP, "iddhipādaṃ": IP,
    # always «cattāro / tayo iddhipādā(naṃ)» = «सिद्धि के चार / तीन आधार(ों)»
    "iddhipādā": "सिद्धि का … आधार", "iddhipādānaṃ": "सिद्धि का … आधार",
    "chandiddhipādo": f"चाह रूपी {IP}", "vīriyiddhipādo": f"उत्साह रूपी {IP}",
    "cittiddhipādo": f"मन रूपी {IP}", "vīmaṃsiddhipādo": f"जाँच-परख रूपी {IP}",
    "chandasamādhi": "चाह से प्राप्त एकाग्रता", "vīriyasamādhi": "उत्साह से प्राप्त एकाग्रता",
    "cittasamādhi": "मन से प्राप्त एकाग्रता", "vīmaṃsāsamādhi": "जाँच-परख से प्राप्त एकाग्रता",
    "vīmaṃsā": "जाँच-परख", "vīmaṃsaṃ": "जाँच-परख",
    "citta": "मन", "samādhi": "एकाग्रता", "samādhiṃ": "एकाग्रता",
    "padhāna": "प्रयत्न", "padhānasaṅkhāra": "प्रयत्न की रचना", "padhānasaṅkhāro": "प्रयत्न की रचना",
    "padhānasaṅkhārā": "प्रयत्न की रचना", "saṅkhāro": "रचना", "saṅkhārā": "रचना",
    "samannāgataṃ": "संपन्न", "samādhipadhānasaṅkhārasamannāgataṃ": "एकाग्रता और प्रयत्न की रचनाओं से संपन्न",
    "samādhipadhānasaṅkhārasamannāgato": "एकाग्रता और प्रयत्न की रचनाओं से संपन्न",
    "samannāgataṃ iddhipādaṃ": "संपन्न सिद्धि का आधार",
    "iddhipādaṃ bhāveti": "सिद्धि के आधार का अभ्यास करना", "iddhipādaṃ bhāvetī": "सिद्धि के आधार का अभ्यास करना",
    # «Chandaṃ ce bhikkhu adhipatiṃ karitvā labhati samādhiṃ, labhati cittassekaggataṃ»
    "adhipatiṃ": "प्रधान", "labhati": "प्राप्त करना", "labhati samādhiṃ": "एकाग्रता प्राप्त करना",
    "ekaggataṃ": "एकाग्रता", "cittassekaggataṃ": "मन की एकाग्रता",
    # «tadekajjhaṃ abhisaññūhitvā abhisaṅkhipitvā …otveva saṅkhyaṃ gacchati»
    "ekajjhaṃ": "एक साथ", "abhisaññahitvā": "इकट्ठा करके", "tveva": "ही", "saṅkhyaṃ": "गिनती",
    "gacchati": "आना", "saṅkhyaṃ gacchati": "गिनती में आना",
    # iddhi string; «Te dhamme āsevati bhāveti bahulīkaroti» = «… निरंतर सेवन करता है, अभ्यास करता है, … बार-बार करता है»
    "samiddhi": "समृद्धि", "ijjhanā": "सफल होना", "samijjhanā": "भली-भाँति सफल होना",
    "paṭilābho": "उपलब्धि", "patti": "प्राप्ति", "sampatti": "भली-भाँति प्राप्ति", "phusanā": "स्पर्श करना",
    "sacchikiriyā": "साक्षात्कार", "upasampadā": "पूरी तरह प्राप्त करना",
    "āsevati": "निरंतर सेवन करना", "bahulīkaroti": "बार-बार करना",
    "viññāṇakhandho": "चेतना का समूह",
}
TABLE = {**C.SHARED_TABLE, **T}

OVR = {
    # «Vipākadhammadhammā» = «कर्म-फल उत्पन्न करने वाले हैं»: the dhammā fragment has no word of its own
    "2-464": {"dhammā": NDE, "uppannā": "उत्पन्न हो चुका"},
}
# «Kathañca bhikkhu … iddhipādaṃ bhāveti?» = «… का अभ्यास कैसे करता है?»
for _b in ("2-432", "2-435", "2-438", "2-441"):
    OVR[_b] = {"bhāveti": "अभ्यास … करना", "iddhipādaṃ bhāveti": "सिद्धि के आधार का अभ्यास … करना"}


def value(bid, kw, kws, text):
    if kw.lower() == "saṅkhāra" and "padhānasaṅkhāra" not in kws:   # member of saṅkhārakkhandho
        return "मानसिक रचनाएँ"
    return C.shared_value(kw, kws, TABLE, bid, text)


def resolver(bid, kw, kws, _hi={}):
    if not _hi:
        _hi.update(read_hindi(CH))
    o = OVR.get(bid, {})
    if kw in o:
        return o[kw]
    return value(bid, kw, kws, _hi.get(bid))


_R = "text «गिनती … में आता है»: आना ~ आता is regular inflection the checker does not model (stem of one letter)"
ALLOWED = {("2-432", "gacchati"): _R, ("2-435", "saṅkhyaṃ gacchati"): _R,
           ("2-438", "saṅkhyaṃ gacchati"): _R, ("2-441", "saṅkhyaṃ gacchati"): _R}

if __name__ == "__main__":
    build_part(CH, resolver)
    verify(CH, allowed=ALLOWED)
