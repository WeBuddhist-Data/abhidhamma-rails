"""pi-6 (Yamaka) Pāli->Hindi keyword maps for 2-02-khandhayamaka and 4-dhatuyamaka.

Builds on the approved sample (map_sample_hi.py, imported read-only): PI6 + this script's table T,
then per-segment overrides OVR. Conventions: hi-map-conventions-pi6.md (+ pi-1 / pi-2 files).

usage: python -I -X utf8 map_2-02_4_hi.py            build + verify both files
       python -I -X utf8 map_2-02_4_hi.py audit F    list every keyword of F with its values and prior values
"""
import collections
import pathlib
import sys

sys.dont_write_bytecode = True                      # no __pycache__ in the shared folder
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import (PI6, NDE, make_resolver, build_part, verify, prior,  # noqa: E402
                           read_keywords, read_hindi, present)

FILES = ("2-02-khandhayamaka", "4-dhatuyamaka")

T = {}

# ---------------------------------------------------------------- 2-02-khandhayamaka
T.update({
    "vadanākkhandho": "अनुभूति का समूह",              # Pāli misprint for vedanākkhandho (6-2-185)
    "uppādavāre": "उत्पन्न होने का खंड",              # «उत्पन्न होने के खंड में»
    "yatthakaṃ": "स्थान वाला भाग",                    # «(स्थान वाला भाग पूरा करके पढ़ना चाहिए)» (harmonise N-yassaka)
    # Pariññāvāra: present = infinitive, past/future = the finite form, Pāli number (pi6 conventions)
    "parijānāti": "पूरी तरह समझना", "parijānanti": "पूरी तरह समझना",
    "parijānittha": "पूरी तरह समझा था",
    "parijānissati": "पूरी तरह समझेगा", "parijānissanti": "पूरी तरह समझेंगे",
    "arahā": "अर्हत्", "arahantaṃ": "अर्हत्",
    "aggamaggasamaṅgī": "सर्वोच्च मार्ग से युक्त व्यक्ति", "aggamaggasamaṅgiṃ": "सर्वोच्च मार्ग से युक्त व्यक्ति",
    "puggalā": "व्यक्ति",
    "puthujjanā": "साधारण व्यक्ति",
    "maggaṃ paṭilabhissanti": "मार्ग प्राप्त करेंगे", "paṭilabhissanti": "प्राप्त करेंगे",
    # the keyword «(no direct equivalent)» is an artefact (an English keyword without Pāli): never a Hindi word
    "(no direct equivalent)": NDE,
})

# ---------------------------------------------------------------- 4-dhatuyamaka
DHATU = {  # build_4_hi DHATU (pi-2 Hindi)
    "cakkhu": "आँख", "sota": "कान", "ghāna": "नाक", "jivhā": "जीभ", "kāya": "शरीर",
    "rūpa": "दृश्य रूप", "sadda": "ध्वनि", "gandha": "गंध", "rasa": "स्वाद", "phoṭṭhabba": "स्पर्श",
    "cakkhuviññāṇa": "आँख की चेतना", "sotaviññāṇa": "कान की चेतना", "ghānaviññāṇa": "नाक की चेतना",
    "jivhāviññāṇa": "जीभ की चेतना", "kāyaviññāṇa": "शरीर की चेतना", "mano": "मन",
    "manoviññāṇa": "मन की चेतना", "dhamma": "मन के विषयों",
}
for _st, _h in DHATU.items():
    for _e in ("dhātu", "dhātuṃ", "dhātū"):
        T[_st + _e] = f"{_h} का तत्व"
# the bare words of the pairs (build_4_hi BARE4 after harmonise B11: raso = स्वाद), all case forms
BARE4 = {
    "cakkhu": "आँख", "cakkhuṃ": "आँख", "sotaṃ": "कान", "ghānaṃ": "नाक", "jivhā": "जीभ", "jivha": "जीभ",
    "jivhāpi": "जीभ", "kāyo": "शरीर", "kāyaṃ": "शरीर", "rūpaṃ": "रूप", "saddo": "ध्वनि", "saddaṃ": "ध्वनि",
    "gandho": "गंध", "gandhaṃ": "गंध", "raso": "स्वाद", "rasaṃ": "स्वाद", "phoṭṭhabbo": "स्पर्श",
    "phoṭṭhabbaṃ": "स्पर्श", "mano": "मन", "manaṃ": "मन",
}
for _st in ("cakkhu", "sota", "ghāna", "jivhā", "kāya", "mano"):
    BARE4[_st + "viññāṇaṃ"] = DHATU[_st + "viññāṇa"]
T.update(BARE4)
T.update({
    "dhātu": "तत्व", "dhātū": "तत्व", "dhātuṃ": "तत्व", "dhātuyo": "तत्व",
    "cakkaṃ": "चक्र",
    "dibbacakkhu": "दिव्य आँख", "paññācakkhu": "प्रज्ञा की आँख",
    "dibbasotaṃ": "दिव्य कान", "taṇhāsotaṃ": "तृष्णा की धारा",                # harmonise I2-sota
    "sīlagandho": "सदाचार की गंध", "samādhigandho": "एकाग्रता की गंध", "paññāgandho": "प्रज्ञा की गंध",
    "attharaso": "अर्थ का स्वाद", "dhammaraso": "शिक्षा का स्वाद", "vimuttiraso": "मुक्ति का स्वाद",  # B11
    "ghānasadiso": "नाक के समान", "ghānadhātusadisā": "नाक के तत्व के समान",
    "āyatanayamake": "इंद्रिय-क्षेत्रों पर प्रश्नों के जोड़े",
    "āyatanayamakassa": "इंद्रिय-क्षेत्रों पर प्रश्नों के जोड़े",
    "dhātuyamakepi": "तत्वों पर प्रश्नों के जोड़े", "dhātuyamakassa": "तत्वों पर प्रश्नों के जोड़े",
    "dhātuyamakampi": "तत्वों पर प्रश्नों के जोड़े",
    # sa-X-ka = «X वाला», a-X-ka = «X से रहित» (harmonise I1-organs), masc. direct sg. like upapajjantānaṃ
    "sacakkhukānaṃ": "आँख वाला", "acakkhukānaṃ": "आँख से रहित",
    "sasotakānaṃ": "कान वाला", "asotakānaṃ": "कान से रहित",
})

# per-segment overrides {bid: {kw (exact spelling): value}}
OVR = {
    "2-02-khandhayamaka": {},
    "4-dhatuyamaka": {},
}
# presence exceptions {file: {(bid, kw): reason}}
ALLOWED = {"2-02-khandhayamaka": {}, "4-dhatuyamaka": {}}

TABLE = {**PI6, **T}


def audit(f):
    res = make_resolver(f, TABLE, OVR[f])
    vals = collections.defaultdict(collections.Counter)
    for bid, kws in read_keywords(f):
        for kw in kws:
            vals[kw][res(bid, kw, kws)] += 1
    for kw, c in vals.items():
        pr = prior(kw)
        print(kw, dict(c), "| prior:", {n: dict(v.most_common(3)) for n, v in pr.items()} if pr else "")


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "audit":
        audit(sys.argv[2])
    else:
        for _f in FILES:
            build_part(_f, make_resolver(_f, TABLE, OVR[_f]))
            verify(_f, allowed=ALLOWED[_f])
