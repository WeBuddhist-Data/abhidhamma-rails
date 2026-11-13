"""pi-6 Pāli->Hindi keyword maps: Saṅkhārayamaka (6-01, 6-02) and Dhammayamaka (9-01, 9-02, 9-03).

Imports the approved sample module map_sample_hi.py read-only (PI6, pi6_value, make_resolver, build_part,
verify). Own table T extends PI6; OVR holds the per-segment overrides; ALLOWED the listed presence exceptions.
usage: python -I -X utf8 map_6_9_hi.py [file ...]
"""
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import PI6, NDE, make_resolver, build_part, verify, read_hindi, read_keywords  # noqa: E402

FILES = ("6-01-sankharayamaka", "6-02-sankharayamaka", "9-01-dhammayamaka", "9-02-dhammayamaka",
         "9-03-dhammayamaka")

T = {}

# --- Saṅkhārayamaka items (notes-6-9: feminine singular items; terms file saṅkhāra bare = रचना)
for _st, _h in (("kāya", "शरीर की रचना"), ("vacī", "वाणी की रचना"), ("citta", "मन की रचना")):
    for _form in ("saṅkhāro", "saṅkhāraṃ", "saṅkhārañca", "saṅkhāroti"):
        T[_st + _form] = _h
T.update({
    # bare words of the word-checking pairs (build_6_hi BARE): kāyo शरीर, vacī वाणी, cittaṃ मन, saṅkhārā रचनाएँ
    "kāyo": "शरीर", "kāyañca": "शरीर", "kāyoti": "शरीर",
    "vacī": "वाणी", "vaciñca": "वाणी", "vacīti": "वाणी",
    "saṅkhāro": "रचना",                     # bare singular (terms file: saṅkhāra bare = रचना)
    "saṅkhārā": "रचनाएँ",                   # bare plural (brief: saṅkhārā = रचनाएँ); «तीन रचनाएँ»
    "cittasampayuttakā": "मन से जुड़ा",      # «मन से जुड़ी सभी परिघटनाएँ» (masc. sg., pi-1 sampayuttā = जुड़ा)
    "assāsapassāsā": "साँस लेना और छोड़ना",   # pi-5
    "assāsapassāsānaṃ": "साँस लेना और छोड़ना", "assāsapassāsehi": "साँस लेना और छोड़ना",
    "vitakkavicārā": "आरंभिक विचार और सतत विचार", "vitakkavicāre": "आरंभिक विचार और सतत विचार",
    "vitakkavicārānaṃ": "आरंभिक विचार और सतत विचार", "vitakkavicārehi": "आरंभिक विचार और सतत विचार",
    "parijānāti": "पूरी तरह समझना",          # pi-5
    "pariññāvāraṃ": "पूरी तरह समझने का खंड",
    "khandhayamake": "समूहों पर प्रश्नों के जोड़े", "saṅkhārayamakepi": "रचनाओं पर प्रश्नों के जोड़े",
})

# --- Dhammayamaka items (build_9_hi: «हितकर परिघटनाएँ» …; dhammā = परिघटना)
for _st, _h in (("kusal", "हितकर"), ("akusal", "हानिकर"), ("abyākat", "नैतिक रूप से अनिर्धारित")):
    T[f"{_st}ā ca dhammā"] = f"{_h} परिघटना भी"            # «हितकर परिघटनाएँ भी …» (X ca V Y ca V = X भी …)
    T[f"{_st}añca dhamme"] = f"{_h} और परिघटना"             # «हितकर और परिघटनाओं को छोड़कर»
    T[f"{_st}aṃ dhammaṃ"] = f"{_h} परिघटना"                 # «हितकर परिघटना का अभ्यास …»
    T[f"{_st}e citte"] = f"{_h} मन"                          # «दूसरे हानिकर मन के चलते समय»
    T[f"{_st}ānaṃ"] = f"{_h} परिघटना"
T.update({
    "kusalākusalānaṃ": "हितकर और हानिकर परिघटना",
    "bhāveti": "अभ्यास करना", "pajahati": "छोड़ना", "nappajahati": "नहीं छोड़ना",
    "aggamaggassa": "सर्वोच्च मार्ग", "aggamaggaṃ": "सर्वोच्च मार्ग",
    "aggamaggaṃ paṭilabhissanti": "सर्वोच्च मार्ग प्राप्त करेंगे",
    "aggamaggasamaṅgīnaṃ": "सर्वोच्च मार्ग से युक्त लोग",
    "arahantānaṃ": "अर्हत्",                  # «अर्हतों में» (pi-5 arahantānaṃ = अर्हत्)
    "pavatte": "जीवन के दौरान",
})

# --- process verbs not in PI6 (value masc., Pāli number; the feminine text forms pass the presence check)
T.update({
    "nuppajjissanti": "उत्पन्न नहीं होंगे", "nirujjhissanti": "समाप्त होंगे",
    "nuppajjitthāti": "उत्पन्न नहीं हुआ था",
})

# --- moments: X-ssa uppāda-/bhaṅgakkhaṇe = «X के उत्पन्न होने / भंग होने का क्षण» (direct: का क्षण)
CITTA = {   # common_6_9_hi CITTA_GEN (oblique inside the genitive kept)
    "kusalavippayuttaakusalavippayuttacitta": "हितकर से अलग और हानिकर से अलग मन",
    "akusalavippayuttakusalavippayuttacitta": "हानिकर से अलग और हितकर से अलग मन",
    "kusalavippayuttacitta": "हितकर से अलग मन",
    "akusalavippayuttacitta": "हानिकर से अलग मन",
    "savitakkasavicārapacchimacitta": "आरंभिक विचार और सतत विचार वाले अंतिम मन",
    "avitakkaavicārapacchimacitta": "आरंभिक विचार और सतत विचार से रहित अंतिम मन",
    "avitakkaavicāracitta": "आरंभिक विचार और सतत विचार से रहित मन",
    "pacchimacitta": "अंतिम मन",
    "aggamagga": "सर्वोच्च मार्ग",
    "citta": "मन",
}
PLG = {"kusalākusalānaṃ": "हितकर और हानिकर परिघटनाओं", "kusalānaṃ": "हितकर परिघटनाओं",
       "akusalānaṃ": "हानिकर परिघटनाओं", "assāsapassāsānaṃ": "साँस लेने और छोड़ने",
       "vitakkavicārānaṃ": "आरंभिक विचार और सतत विचार"}
KHANA = {"uppāda": "उत्पन्न होने का क्षण", "bhaṅga": "भंग होने का क्षण"}
for _k, _kh in KHANA.items():
    T[f"{_k}kkhaṇe"] = _kh
    for _c, _ch in CITTA.items():
        T[f"{_c}ssa {_k}kkhaṇe"] = f"{_ch} के {_kh}"
    for _c, _ch in PLG.items():
        T[f"{_c} {_k}kkhaṇe"] = f"{_ch} के {_kh}"
T.update({
    "cittassa": "मन", "citte": "मन", "pacchimacittaṃ": "अंतिम मन",
    "pacchimacittassa": "अंतिम मन",
    "savitakkasavicārapacchimacittassa": "आरंभिक विचार और सतत विचार वाला अंतिम मन",
    "avitakkaavicārapacchimacittassa": "आरंभिक विचार और सतत विचार से रहित अंतिम मन",
    "avitakkaavicāraṃ": "आरंभिक विचार और सतत विचार से रहित",
    "anantarā": "ठीक बाद",                                   # pi-5
    "vattamāne": "चलना",                                     # «… मन के चलते समय» (pi-5 चलना)
    "tesaṃyeva": "उन्हीं",                                   # «उन्हीं में»
    "pacchimacittasamaṅgīnaṃ": "अंतिम मन से युक्त लोग",
    "avitakkaavicārapacchimacittasamaṅgīnaṃ": "आरंभिक विचार और सतत विचार से रहित अंतिम मन से युक्त लोग",
})

# --- beings and places (conventions-pi6 «Beings and places»; common_6_9_hi SPHERE)
T.update({
    "samāpannānaṃ": "लीन लोग",                               # «ध्यान की पहली अवस्था में लीन लोगों में»
    "nirodhasamāpannānaṃ": "समाप्ति की ध्यान-अवस्था में लीन लोग",
    "nirodhasamāpannānanti": "समाप्ति की ध्यान-अवस्था में लीन लोग",
    "catutthajjhānaṃ": ("ध्यान की चौथी अवस्था", "ध्यान की … चौथी अवस्था"),
    "catutthajjhāne": ("ध्यान की चौथी अवस्था", "ध्यान की … चौथी अवस्था"),
    "kāmāvacarānaṃ": ("इंद्रिय-सुखों के लोक के प्राणी", "इंद्रिय-सुखों के लोक के … प्राणी"),  # «… के जिन प्राणियों में»
    "rūpāvacarānaṃ": ("सूक्ष्म भौतिक लोक के प्राणी", "सूक्ष्म भौतिक लोक … के प्राणी"),
    "arūpāvacarānaṃ": "अभौतिक लोक के प्राणी",
    "kāmāvacare": "इंद्रिय-सुखों का लोक", "rūpāvacare": "सूक्ष्म भौतिक लोक", "arūpāvacare": "अभौतिक लोक",
    "arūpāvacaraṃ": "अभौतिक लोक",                            # «… या अभौतिक लोक में जन्म लेकर»
    "catuvokāre": ("चार समूहों वाला अस्तित्व", "चार … समूहों वाला अस्तित्व"),
    "savitakkasavicārabhūmiyaṃ": "आरंभिक विचार और सतत विचार वाला स्तर",
    "avitakkaavicārabhūmiyaṃ": "आरंभिक विचार और सतत विचार से रहित स्तर",
})

# --- relatives, editorial notes, section names inside notes
T.update({
    "yassa yattha": "जिस व्यक्ति … जिस स्थान",
    "yassakampi": "व्यक्ति वाला भाग", "yatthakampi": "स्थान वाला भाग", "yatthakānaṃ": "स्थान वाला भाग",
    "yassayatthakampi": "व्यक्ति और स्थान वाला भाग", "yassayatthake": "व्यक्ति और स्थान वाला भाग",
    "uppādavāre": "उत्पन्न होने का खंड", "uppādavārepi": "उत्पन्न होने का खंड",
    "nirodhavāre": "समाप्त होने का खंड", "nirodhavārepi": "समाप्त होने का खंड",
    "nirodhavārena": "समाप्त होने का खंड",
    "uppādanirodhavārepi": "उत्पन्न होने और समाप्त होने का खंड",
    "uppādavāranirodhavārepi": "उत्पन्न होने और समाप्त होने का खंड",
    "anulomampi": "सकारात्मक", "paccanīkampi": "नकारात्मक", "pucchā": "प्रश्न",
    "paccanīkaokāsā": "नकारात्मक: स्थान",
    "paccuppannavārādi": "वर्तमान का खंड आदि",
    "(no direct equivalent)": NDE,         # a placeholder the keyword list carries (no Pāli word behind it)
})

TABLE = {**PI6, **T}

# per-segment overrides {file: {bid: {kw: value}}}
OVR = {f: {} for f in FILES}
# presence exceptions {file: {(bid, kw): reason}}
ALLOWED = {f: {} for f in FILES}


def _arahant_exceptions(f):
    """arahantānaṃ = अर्हत् (pi-4/5 value) on the text «अर्हतों में»: the regular oblique plural of अर्हत्; the
    checker does not model the dropped virama."""
    hi = read_hindi(f)
    return {(bid, kw): "अर्हत् ~ «अर्हतों» (oblique plural; virama dropped)"
            for bid, kws in read_keywords(f) for kw in kws
            if kw == "arahantānaṃ" and "अर्हतों" in (hi.get(bid) or "")}


if __name__ == "__main__":
    for _f in (sys.argv[1:] or FILES):
        ALLOWED[_f].update(_arahant_exceptions(_f))
        build_part(_f, make_resolver(_f, TABLE, OVR[_f]))
        verify(_f, allowed=ALLOWED[_f])
