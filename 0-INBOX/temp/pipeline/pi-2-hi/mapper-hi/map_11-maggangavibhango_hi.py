"""pi-2 ch. 11 (Maggaṅgavibhaṅga) Pāli->Hindi keyword map.  usage: python -I -X utf8 map_11-maggangavibhango_hi.py

Imports map_sample_hi (read-only) and reuses the tables of the ch. 4 and ch. 7 scripts (same formulas:
the eightfold path definitions of the Saccavibhaṅga, the satipaṭṭhāna formula). T11 settles the conflicts.
"""
import importlib.util
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from map_sample_hi import PI2, PP_SEGMENTS, NDE, pi2_value, build_part, verify, read_hindi  # noqa: E402


def _load(name):
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), HERE / f"{name}.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


T4 = _load("map_4-saccavibhango_hi").T
T7 = _load("map_7-satipatthanavibhango_hi").T

CH = "11-maggangavibhango"
PP_SEGMENTS.update({"2-506", "2-507"})

T11 = {
    "maggaṅga": "मार्ग का अंग", "aṅga": "अंग", "magga": "मार्ग",
    "maggaṅgā": "मार्ग … अंग", "maggaṅgānaṃ": "मार्ग … अंग",       # «मार्ग के सात अंग», «मार्ग के आठ अंगों»
    "aṅgānaṃ": "अंग", "sukhassa ca pahānā": "सुख को छोड़ना", "aṅgaṃ": "अंग", "maggaṅgaṃ": "मार्ग का अंग",
    "ariyo": "आर्य", "ajjhattaṃ": "स्वयं में", "sukhaṃ": "सुख", "dhammesu": "परिघटना", "vācā": "वाणी",
    "dhammesu dhammānupassī": "परिघटनाओं में परिघटनाओं का अवलोकन करते हुए",
    "dukkhe": "दुःख", "nirodhe": "अंत", "dukkhanirodhe": "दुःख का अंत", "dhammānaṃ": "परिघटना",
    "vitakkavicārānaṃ": "आरंभिक विचार और सतत विचार", "upekkhā": "समभाव",
    "musāvādā veramaṇī": "झूठ बोलने से दूर रहना", "pāṇātipātā veramaṇī": "जीव-हत्या से दूर रहना",
    "kāmesumicchācārā veramaṇī": "इंद्रिय-सुखों में दुराचार से दूर रहना",
    "adinnādānā veramaṇī": "बिना दी गई चीज़ लेने से दूर रहना",
    "jīvikaṃ": "जीवन-यापन", "vīriyaṃ ārabhati": "उत्साह जगाना", "cittaṃ paggaṇhāti": "मन को तत्पर करना",
    # 2-489
    "diṭṭhiṃ": "दृष्टि", "saṅkappaṃ": "संकल्प", "vācaṃ": "वाणी", "ājīvaṃ": "आजीविका", "vāyāmaṃ": "प्रयास",
    "satiṃ": "सजगता", "samādhiṃ": "एकाग्रता", "viveka": "अलगाव", "virāga": "वैराग्य", "nirodha": "समाप्ति",
    "vossagga": "त्याग", "pariṇāmiṃ": "परिणत होने वाला",
    # Abhidhammabhājanīya
    "lokuttaraṃ": "लोकोत्तर", "appanā": "टिकाना", "abhiniropanā": "विषय की ओर ले जाना", "cetaso": "मन",
    "vāyāmena": "प्रयास", "saṅkappena": "संकल्प", "satiyā": "सजगता", "samatho": "शांति",
    # Pañhāpucchaka
    "anupādāniyā": "न आसक्ति का विषय बनने वाला",         # «न कर्म से उत्पन्न, न आसक्ति का विषय बनने वाले» "sahagato": "के साथ होने वाला", "sampayutto": "जुड़ा",
    "asaṃkilesikā": "क्लेशों का विषय न बनने वाला", "lokuttarā": "लोकोत्तर", "araṇāti": "संघर्ष से रहित",
    "na hetu": "मूल रूपी न होने वाला", "vicāro": "सतत विचार",
}
TABLE = {**PI2, **T4, **T7, **T11}

OVR = {
    "2-506": {"uppannā": "उत्पन्न हो चुका"},               # matrix label (siyā uppannā)
    "2-492": {"veramaṇī": "बचना"},                         # the virati string (pi-1; ch. 4 2-206)
}
for _b in ("2-486", "2-488", "2-504"):                     # «आठ अंगों वाला आर्य मार्ग»
    OVR.setdefault(_b, {})["aṭṭhaṅgiko maggo"] = "आठ अंगों वाला … मार्ग"
ALLOWED = {}
for _b in ("2-499", "2-501", "2-503"):
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
