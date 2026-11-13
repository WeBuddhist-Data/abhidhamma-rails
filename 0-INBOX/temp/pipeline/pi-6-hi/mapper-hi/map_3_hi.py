"""pi-6 Āyatanayamaka (3-01 … 3-06) Pāli->Hindi keyword maps.

Imports the sample's map_sample_hi.py read-only (PI6, pi6_value, build_part, verify, present ...) and extends PI6
with this chapter's table T; per-segment overrides in OVR (a list value = one value per occurrence of a keyword
that occurs more than once in the line). usage: python -I -X utf8 map_3_hi.py [file ...]"""
import collections
import pathlib
import sys

sys.dont_write_bytecode = True                      # no __pycache__ in the shared folder
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import (PI6, NDE, GAP, read_hindi, pi6_value, build_part, verify)  # noqa: E402,F401

FILES = [f"3-0{i}-ayatanayamaka" for i in range(1, 7)]

T = {}
# --- the twelve āyatana names (notes-3, pi-1/pi-2: «X का इंद्रिय-क्षेत्र») and the bare words of the
#     word-checking pairs (brief: the bare word keeps its bare Hindi, the āyatana name gets the full term)
SENSES = {  # stem of X-āyatana: (bare word forms, Hindi of X)
    "cakkh": (("cakkhu", "cakkhuṃ"), "आँख"),
    "sot": (("sotaṃ",), "कान"),
    "ghān": (("ghānaṃ",), "नाक"),
    "jivh": (("jivhā", "jivhaṃ"), "जीभ"),
    "kāy": (("kāyo", "kāyaṃ"), "शरीर"),
    "rūp": (("rūpaṃ",), "रूप"),                    # bare rūpaṃ = रूप; rūpāyatana = दृश्य रूप का …
    "sadd": (("saddo", "saddaṃ"), "ध्वनि"),
    "gandh": (("gandho", "gandhaṃ"), "गंध"),
    "ras": (("raso", "rasaṃ"), "स्वाद"),
    "phoṭṭhabb": (("phoṭṭhabbo", "phoṭṭhabbaṃ"), "स्पर्श"),
    "man": (("mano", "manaṃ"), "मन"),
    "dhamm": (("dhammo",), "परिघटना"),
}
NAME = {"rūp": "दृश्य रूप", "dhamm": "मन के विषयों"}  # the āyatana name where it differs from the bare word
for _st, (_bare, _h) in SENSES.items():
    for _b in _bare:
        T[_b] = _h
    _n = NAME.get(_st, _h)
    _obl = "मन के विषयों" if _st == "dhamm" else _n
    for _e in ("āyatanaṃ", "āyatana", "āyatanā"):
        T[_st + _e] = f"{_n} का इंद्रिय-क्षेत्र"
    T[_st + "āyatanamūlakaṃ"] = f"{_obl} के इंद्रिय-क्षेत्र पर आधारित"     # (Cakkhāyatanamūlakaṃ)
T["sotāyananti"] = "कान का इंद्रिय-क्षेत्र"                      # Pāli misprint for sotāyatananti (6-3-13)
T.update({
    "āyatanaṃ": "इंद्रिय-क्षेत्र", "āyatanā": "इंद्रिय-क्षेत्र", "āyatana": "इंद्रिय-क्षेत्र",
    # fused negative na + āyatana keeps «नहीं» (pi-6 nuppajjati rule): «जो इंद्रिय-क्षेत्र नहीं हैं»
    "nāyatanaṃ": "इंद्रिय-क्षेत्र नहीं", "nāyatanā": "इंद्रिय-क्षेत्र नहीं",
    "avaseso": "शेष",
    # the other senses of the bare words (notes-3, harmonise I2 / B11)
    "dibbacakkhu": "दिव्य आँख", "paññācakkhu": "प्रज्ञा की आँख",
    "dibbasotaṃ": "दिव्य कान", "taṇhāsotaṃ": "तृष्णा की धारा",
    "sīlagandho": "सदाचार की गंध", "samādhigandho": "एकाग्रता की गंध", "paññāgandho": "प्रज्ञा की गंध",
    "attharaso": "अर्थ का स्वाद", "dhammaraso": "शिक्षा का स्वाद", "vimuttiraso": "मुक्ति का स्वाद",
    "cakkaṃ": "चक्र",                                                # (Cakkaṃ bandhitabbaṃ) «चक्र पूरा करना …»
})

# --- beings with / without an organ (harmonise I1: sa-X-ka «X वाले», a-X-ka «X से रहित»), masc. direct sg.
for _p, _h in (("cakkhuk", "आँख"), ("sotak", "कान"), ("ghānak", "नाक"), ("rūpak", "भौतिक रूप"),
               ("cittak", "मन")):
    T[f"sa{_p}ānaṃ"] = f"{_h} वाला"
    T[f"a{_p}ānaṃ"] = f"{_h} से रहित"

# --- the planes (pi-6 places/beings rule): place sense (loc. / acc. of destination / abl.) = the realm, direct
#     case; beings sense (gen. pl.) = «… के प्राणी»
for _p, _h in (("kāmāvacar", "इंद्रिय-सुखों का लोक"), ("rūpāvacar", "सूक्ष्म भौतिक लोक"),
               ("arūpāvacar", "अभौतिक लोक")):
    for _e in ("e", "aṃ", "ā"):
        T[_p + _e] = _h
    T[_p + "ānaṃ"] = _h.replace("का लोक", "के लोक") + " के प्राणी"
# «चार या पाँच समूहों वाले अस्तित्व» (harmonise I3): catuvokāra- = «चार … समूहों वाला अस्तित्व» there
for _e in ("e", "aṃ", "ā"):
    T["catuvokār" + _e] = ("चार समूहों वाला अस्तित्व", "चार" + GAP + "समूहों वाला अस्तित्व")
T["catuvokārānaṃ"] = ("चार समूहों वाले अस्तित्व के प्राणी", "चार" + GAP + "समूहों वाले अस्तित्व के प्राणी")

# --- process verbs: misprints / spellings of the same verbs
T.update({
    "nirujjhatī": "समाप्त होना",                                       # «na nirujjhatī ti» (6-3-131)
    "upapajjissati": "उत्पन्न होगा",                                   # misprint for uppajjissati (6-3-212)
    "parinibbāntānaṃ": "पूर्ण निर्वाण पाने वाला",                       # spelling of parinibbantānaṃ (6-3-172)
    # the fused misprint «dhammāyatanañca uppajjittharūpāyatanañca uppajjittha» (6-3-43)
    "uppajjittharūpāyatanañca": "उत्पन्न हुआ था" + GAP + "दृश्य रूप का इंद्रिय-क्षेत्र",
})

# --- Pariññāvāra (notes-3; pi-5 parijānāti = पूरी तरह समझना). Present = infinitive; past / future keep the
#     tense, masculine, Pāli number (pi-6 process-verb rule)
T.update({
    "parijānāti": "पूरी तरह समझना", "parijānanti": "पूरी तरह समझना",
    "parijānittha": "पूरी तरह समझा था",
    "parijānissati": "पूरी तरह समझेगा", "parijānissanti": "पूरी तरह समझेंगे",
    "aggamaggasamaṅgī": "सर्वोच्च मार्ग से युक्त व्यक्ति", "aggamaggasamaṅgiṃ": "सर्वोच्च मार्ग से युक्त व्यक्ति",
    "arahā": "अर्हत्", "arahantaṃ": "अर्हत्",
    "puggalā": "व्यक्ति", "puthujjanā": "साधारण व्यक्ति",
    "maggaṃ paṭilabhissanti": "मार्ग प्राप्त करेंगे", "paṭilabhissanti": "प्राप्त करेंगे",
})

# --- notes on the abbreviated sections (harmonise N-yassaka: yassaka / yatthaka / yassayatthaka =
#     «व्यक्ति वाला भाग / स्थान वाला भाग / व्यक्ति और स्थान वाला भाग»; -pi «भी» is dropped like -ñca)
T.update({
    "yatthakaṃ": "स्थान वाला भाग", "yatthakampi": "स्थान वाला भाग", "yatthakānaṃ": "स्थान वाला भाग",
    "yassakampi": "व्यक्ति वाला भाग", "yassayatthakampi": "व्यक्ति और स्थान वाला भाग",
    "yassa yatthakampi": "व्यक्ति और स्थान वाला भाग", "yassa yatthake": "व्यक्ति और स्थान वाला भाग",
    "yassakasadisaṃ": "व्यक्ति वाले भाग के समान",
    "yassa yattha": "जिस व्यक्ति" + GAP + "जिस स्थान",                  # «जिस व्यक्ति में जिस स्थान पर»
    "uppādepi": "उत्पन्न होना", "nirodhepi": "समाप्त होना",
    "uppādanirodhepi": "उत्पन्न होना और समाप्त होना",
    "uppādavāre": "उत्पन्न होने का खंड", "uppādavārepi": "उत्पन्न होने का खंड",
    "nirodhavāre": "समाप्त होने का खंड", "nirodhavārepi": "समाप्त होने का खंड",
    "uppādanirodhavārepi": "उत्पन्न होने और समाप्त होने का खंड",
    "vāresu": "खंड", "vārasaṅkhepo": "खंड संक्षेप में",            # «आगे के खंड संक्षेप में हैं»
    "paccuppannepi": "वर्तमान", "atītepi": "अतीत", "paccuppannātītepi": "वर्तमान और अतीत",
    "paccuppannānāgatepi": "वर्तमान और भविष्य", "atītānāgatepi": "अतीत और भविष्य",
    "anulomampi": "सकारात्मक", "paccanīkampi": "नकारात्मक", "pucchā": "प्रश्न",
})

# --- the keyword «(no direct equivalent)»: an artefact of the keyword lists (an English keyword without Pāli),
#     not a Pāli word; coordinator rule for all pi-6 Hindi maps: kept in place, mapped to (no direct equivalent)
T["(no direct equivalent)"] = NDE
OVR = {f: {} for f in FILES}                        # no per-segment overrides needed
# presence exceptions {file: {(bid, kw): reason}}
ALLOWED = {f: {} for f in FILES}


def resolver_for(f, table, ovr):
    hi = read_hindi(f)
    seen = collections.Counter()

    def resolver(bid, kw, kws):
        o = ovr.get(bid, {})
        if kw in o:
            v = o[kw]
            if isinstance(v, list):
                i = seen[(bid, kw)]
                seen[(bid, kw)] += 1
                return v[min(i, len(v) - 1)]
            return v
        return pi6_value(kw, kws, table, bid, hi.get(bid))
    return resolver


if __name__ == "__main__":
    for _f in (sys.argv[1:] or FILES):
        build_part(_f, resolver_for(_f, {**PI6, **T}, OVR[_f]))
        verify(_f, allowed=ALLOWED[_f])
