"""pi-6 Indriyayamaka, second half (10-07 .. 10-13): Pāli->Hindi keyword maps (driver).
Table: PI6 (sample, map_sample_hi) + IND (map_10_common_hi, the shared Indriya table, both imported read-only)
+ T (only what 10-07 .. 10-13 need beyond IND; no key of T overrides IND), per-segment OVR.
Conventions: hi-map-conventions-pi6.md (+ the pi-1 / pi-2 files).
usage: python -I -X utf8 map_10b_hi.py [file ...]"""
import pathlib
import sys

sys.dont_write_bytecode = True                     # no __pycache__ in the shared folder
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import PI6, NDE, make_resolver, build_part, verify  # noqa: E402  (read-only import)
from map_10_common_hi import IND  # noqa: E402  (read-only import)

FILES = [f"10-{n:02d}-indriyayamaka" for n in range(7, 14)]
assert IND["(no direct equivalent)"] == NDE        # artefact keyword: mapped to itself (coordinator rule, IND)

T = {
    # Pāli slip «Pacchimabhavikānaṃ purisānaṃ uppajjantānaṃ» for upapajjantānaṃ (10-11 ^6-10-398):
    # «… जन्म लेने वाले पुरुषों में»
    "uppajjantānaṃ": "जन्म लेने वाला",
}

# Pariññāvāra (10-13). parijānāti को पूरी तरह समझता है, pajahati को छोड़ता है, bhāveti का अभ्यास करता है,
# sacchikaroti का साक्षात्कार करता है (notes-10b). Present (sg./pl.) = infinitive; past / future = the finite form,
# masc., in the Pāli's number (sample rule uppajjittha / uppajjissati / uppajjissanti); a fused negative
# (n-ppajahati) keeps «नहीं» as the Hindi has it (sample rule nuppajjati); a separate «na» is not a keyword, so the
# verb after it is the positive part.
_V = {  # stem: (forms: present sg, present pl, past, future sg, future pl), (infinitive, past, future sg, future pl)
    "parijān": (("āti", "anti", "ittha", "issati", "issanti"),
                ("पूरी तरह समझना", "पूरी तरह समझा था", "पूरी तरह समझेगा", "पूरी तरह समझेंगे")),
    "pajah": (("ati", "anti", "ittha", "issati", "issanti"), ("छोड़ना", "छोड़ा था", "छोड़ेगा", "छोड़ेंगे")),
    "nappajah": (("ati", "anti", "ittha", "issati", "issanti"),
                 ("नहीं छोड़ना", "नहीं छोड़ा था", "नहीं छोड़ेगा", "नहीं छोड़ेंगे")),
    "bhāv": (("eti", "enti", "ittha", "essati", "essanti"),
             ("अभ्यास करना", "अभ्यास किया था", "अभ्यास करेगा", "अभ्यास करेंगे")),
    "sacchikar": (("oti", "onti", "ittha", "issati", "issanti"),
                  ("साक्षात्कार करना", "साक्षात्कार किया था", "साक्षात्कार करेगा", "साक्षात्कार करेंगे")),
}
for _st, (_ends, (_inf, _past, _fut, _futpl)) in _V.items():
    for _e, _h in zip(_ends, (_inf, _inf, _past, _fut, _futpl)):
        T[_st + _e] = _h
T.update({
    "sacchākāsi": "साक्षात्कार कर लिया है",           # aorist: «जिसने सर्वोच्च फल का साक्षात्कार कर लिया है»
    "paṭilabhissanti": "प्राप्त करेंगे", "maggaṃ": "मार्ग",
    "maggaṃ paṭilabhissanti": "मार्ग प्राप्त करेंगे",    # «जो साधारण व्यक्ति मार्ग प्राप्त (नहीं) करेंगे»
    "puggalā": "व्यक्ति", "puthujjanā": "साधारण व्यक्ति",  # pi-1/2/5 puthujjano
    "arahā": "अर्हत्", "arahantaṃ": "अर्हत्",             # arahantañca
    "anāgāmī": "फिर न लौटने वाला",
    "aggamaggasamaṅgī": "सर्वोच्च मार्ग से युक्त व्यक्ति",  # pi-5 Maggasamaṅgī = मार्ग से युक्त व्यक्ति
    "aggamaggasamaṅgiṃ": "सर्वोच्च मार्ग से युक्त व्यक्ति",  # Aggamaggasamaṅgiñca
    "anāgāmimaggasamaṅgī": "फिर न लौटने के मार्ग से युक्त व्यक्ति",
    "anāgāmimaggasamaṅgi": "फिर न लौटने के मार्ग से युक्त व्यक्ति",
    "anāgāmimaggasamaṅgiṃ": "फिर न लौटने के मार्ग से युक्त व्यक्ति",
    "aṭṭhamako": "आठवें स्तर का व्यक्ति", "aṭṭhamakaṃ": "आठवें स्तर का व्यक्ति",
    "maggasamaṅgino": "मार्ग से युक्त व्यक्ति",           # «दो मार्गों से युक्त व्यक्तियों»
    "aggaphalaṃ": "सर्वोच्च फल",
    "yamakapakaraṇaṃ": "प्रश्नों के जोड़े ग्रंथ",          # «“प्रश्नों के जोड़े” ग्रंथ समाप्त» (pi-2/4 pakaraṇaṃ ग्रंथ)
})
_overlap = sorted(k for k in T if k in IND)
assert not _overlap, f"T overrides IND: {_overlap}"

OVR = {f: {} for f in FILES}
# Pāli slip «itthindriyaṃ na uppajjissanti» (pl. for sg.); the Hindi has the singular «उत्पन्न नहीं होगी»
OVR["10-10-indriyayamaka"]["6-10-385"] = {"uppajjissanti": "उत्पन्न होगा"}
ALLOWED = {f: {} for f in FILES}

if __name__ == "__main__":
    table = {**PI6, **IND, **T}
    for f in (sys.argv[1:] or FILES):
        build_part(f, make_resolver(f, table, OVR[f]))
        verify(f, allowed=ALLOWED[f])
