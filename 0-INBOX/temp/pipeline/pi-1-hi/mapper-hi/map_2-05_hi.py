"""Map 2-05-cittuppadakandam (lokuttara vipāka, akusala vipāka, kiriyā) keywords to the Hindi translation.

CH2 + the 2-03 table (same lokuttara formula) + own extensions + context rules + per-segment overrides.
usage: python -I -X utf8 map_2-05_hi.py
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_hi import NDE, ch2_value, build_part, verify, read_hindi, present, lc  # noqa: E402
import importlib  # noqa: E402
T203 = importlib.import_module("map_2-03_hi").TABLE   # importing it writes nothing

PART = "2-05-cittuppadakandam"

TABLE = {**T203,
    # result clause of the path-consciousness
    "katattā": "किया जाना", "bhāvitattā": "अभ्यास किया जाना", "upacitattā": "संचित होना",
    "kusalassa jhānassa": "हितकर ध्यान", "lokuttarassa kusalassa": "लोकोत्तर हितकर",
    "lokuttarassa kusalassa jhānassa": "लोकोत्तर हितकर ध्यान",
    "abyākatā": "नैतिक रूप से अनिर्धारित", "dhammā abyākatā": "नैतिक रूप से अनिर्धारित परिघटना",
    "abyākataṃ": "नैतिक रूप से अनिर्धारित",
    "animittaṃ": "चिह्नों से रहित", "animittanti": "चिह्नों से रहित", "suññatanti": "शून्य",
    "appaṇihitanti": "इच्छा-रहित", "abhiññanti": "उच्च ज्ञान", "dandhābhiññanti": "धीमे उच्च ज्ञान वाला",
    "adhipateyyaṃ": "प्रधानता वाला", "adhipateyyanti": "प्रधानता वाला", "adhipateyya": "प्रधानता",
    "suññatā": "शून्यता", "suddhikaappaṇihitaṃ": "केवल इच्छाओं का अभाव",
    "lokuttaraṃ satipaṭṭhānaṃ bhāveti": "लोकोत्तर सजगता के आधार का अभ्यास करना",
    "aññātāvī": "पूर्ण ज्ञान पा चुका",
    # akusala vipāka
    "akusala": "हानिकर", "akusalassa": "हानिकर", "akusalassa kammassa": "हानिकर कर्म",
    "vipāka": "कर्म के फल रूपी", "vipākā": "कर्म के फल रूपी", "viññāṇāni": "चेतना",
    "vipākaabyākataṃ": "कर्म के फल रूपी नैतिक रूप से अनिर्धारित मन",
    "vipākapañcaviññāṇāni": "कर्म के फल रूपी पाँच प्रकार की चेतना",
    "vipākamanodhātu": "कर्म के फल रूपी मन का तत्व", "vipākā manodhātu": "कर्म के फल रूपी मन का तत्व",
    "vipākamanoviññāṇadhātu": "कर्म के फल रूपी मन की चेतना का तत्व",
    "vipākā manoviññāṇadhātu": "कर्म के फल रूपी मन की चेतना का तत्व",
    "vipākā abyākatā": "नैतिक रूप से अनिर्धारित कर्म-फल",
    "mano": "मन", "manodhātu": "मन का तत्व",
    "cakkhuviññāṇaṃ": "आँख की चेतना", "sotaviññāṇaṃ": "कान की चेतना", "ghānaviññāṇaṃ": "नाक की चेतना",
    "jivhāviññāṇaṃ": "जीभ की चेतना", "kāyaviññāṇaṃ": "शरीर की चेतना",
    "kāyaviññāṇa": "शरीर की चेतना", "kāyaviññāṇadhātu": "शरीर की चेतना का तत्व",
    "kāyikaṃ": "शारीरिक", "kāyasamphassa": "शरीर का संपर्क", "samphassa": "संपर्क",
    "kāyasamphassajaṃ": "शरीर के संपर्क से उत्पन्न",
    "dukkhaṃ": "दुःख", "dukkhā vedanā": "दुःखद अनुभूति", "dukkhindriyaṃ": "दुःख की क्षमता",
    "ārammaṇā": "विषय", "uppannā": "उत्पन्न", "dhātu uppannā": "तत्व उत्पन्न",
    "sahagatā": "के साथ होना", "upekkhāsahagatā": "समभाव के साथ होना",
    "somanassasahagatā": "प्रसन्नता के साथ होना",
    # kiriyā
    "kiriyā": "केवल क्रिया रूपी", "kiriyaṃ": "केवल क्रिया रूपी",
    "kiriyāabyākataṃ": "केवल क्रिया रूपी नैतिक रूप से अनिर्धारित मन",
    "kiriyā abyākatā": "केवल क्रिया रूपी नैतिक रूप से अनिर्धारित मन",
    "kiriyāmano": "केवल क्रिया रूपी मन", "kiriyā mano": "केवल क्रिया रूपी मन",
    "kiriyāmanodhātu": "केवल क्रिया रूपी मन का तत्व", "kiriyā manodhātu": "केवल क्रिया रूपी मन का तत्व",
    "kiriyāmanoviññāṇa": "केवल क्रिया रूपी … मन की चेतना",
    "kiriyā manoviññāṇa": "केवल क्रिया रूपी … मन की चेतना",
    "kiriyāmanoviññāṇadhātu": "केवल क्रिया रूपी … मन की चेतना का तत्व",
    "kiriyā manoviññāṇadhātu": "केवल क्रिया रूपी … मन की चेतना का तत्व",
    "dhātusomanassasahagatā": "प्रसन्नता के साथ होने वाला … तत्व",
    "dhātu somanassasahagatā": "प्रसन्नता के साथ होने वाला … तत्व",
    "dhātuupekkhāsahagatā": "समभाव के साथ होने वाला … तत्व",
    "dhātu upekkhāsahagatā": "समभाव के साथ होने वाला … तत्व",
    "manoviññāṇadhātusomanassasahagatā": "प्रसन्नता के साथ होने वाला मन की चेतना का तत्व",
    "manoviññāṇadhātu somanassasahagatā": "प्रसन्नता के साथ होने वाला मन की चेतना का तत्व",
    "manoviññāṇadhātuupekkhāsahagatā": "समभाव के साथ होने वाला मन की चेतना का तत्व",
    "manoviññāṇadhātu upekkhāsahagatā": "समभाव के साथ होने वाला मन की चेतना का तत्व",
    "kammavipākā": "कर्म-फल", "kammavipākaṃ": "कर्म-फल",
    "akusalā": "हानिकर", "akusalaṃ": "हानिकर",
    "kusalā nākusalā": "न हितकर न हानिकर", "kusalaṃ nākusalaṃ": "न हितकर न हानिकर",
    "sampayuttā": "जुड़ा", "vippayuttā": "अलग", "ñāṇavippayuttā": "ज्ञान से अलग",
    "abyākatamūlaṃ": "नैतिक रूप से अनिर्धारित मूल",
    "rūpāvacara": "सूक्ष्म भौतिक लोक से संबंधित", "rūpāvacaraṃ": "सूक्ष्म भौतिक लोक से संबंधित",
    "arūpāvacara": "अभौतिक लोक से संबंधित", "arūpāvacaraṃ": "अभौतिक लोक से संबंधित",
    "arūpa": "अभौतिक", "avacaraṃ": "लोक से संबंधित",
    # rūpāvacara / arūpāvacara kiriyā
    "vihāraṃ": "रहना", "jhānaṃ bhāveti": "ध्यान का अभ्यास करना", "kasiṇaṃ": "ध्यान-मंडल",
    "pathavī": "पृथ्वी", "sukhassa": "सुख", "pahānā": "त्याग", "sukhassa ca pahānā": "सुख का त्याग",
    "sabbaso": "पूरी तरह", "samatikkamā": "पार कर जाना", "samatikkamma": "पार करके",
    "atthaṅgamā": "मिट जाना", "nānatta": "विविधता", "manasikārā": "मनोयोग करना",
    "saññānaṃ": "पहचान", "ākāsa": "आकाश", "ānañca": "अनंत",
    "ānañcāyatana": "अनंत … क्षेत्र", "ānañcāyatanaṃ": "अनंत … क्षेत्र",
    "viññāṇañca": "अनंत चेतना", "viññāṇañcāyatanaṃ": "अनंत चेतना का क्षेत्र",
    "ākiñcañña": "कुछ भी न होना", "asaññā": "अ-पहचान",
    "niṭṭhitaṃ": "पूरा हुआ",
}

HEADING_LIKE = {"1-573", "1-575"}   # closing lines «…, प्रसन्नता/समभाव के साथ होने वाला मन की चेतना का तत्व»
EXACT = {"Lokuttara": "लोकोत्तर"}

# per-segment overrides: {bid: {kw: value}}
OVERRIDES = {
    "1-1-8-2-0": {"suññataṃ": "शून्यता"},               # heading Suddhikasuññataṃ = «केवल शून्यता»
    "1-1-8-4-0": {"appaṇihitaṃ": "इच्छाओं का अभाव"},    # heading Suddhikaappaṇihitaṃ
    "1-1-10-0": {"hetuka": "मूल"},                       # Ahetuka- = «मूल से रहित» (positive part)
    "1-1-10-4-0": {"hetuka": "मूल वाला", "kiriyā": "केवल क्रिया रूपी"},   # Sahetuka- = «मूल वाला»
    "1-1-10-5-0": {"Rūpa": "सूक्ष्म भौतिक"},
    "1-575": {"hetukā": "मूल"},                          # Ahetukā kiriyā abyākatā
    "1-576": {"hetukā": "मूल वाला"},                     # Sahetukā kāmāvacarakiriyā
    "1-577": {"rūpa": "सूक्ष्म भौतिक"},                  # rūpāvacaraṃ
    "1-578": {"rūpa": "सूक्ष्म भौतिक"},
    "1-579": {"rūpa": "भौतिक रूप", "sahagataṃ": "के साथ"},   # rūpasaññānaṃ; …saññāsahagataṃ = «की पहचान के साथ»
    "1-580": {"sahagataṃ": "के साथ"},
    "1-581": {"sahagataṃ": "के साथ"},
    "1-582": {"sahagataṃ": "के साथ"},
    # rūparāga / arūparāga = «सूक्ष्म भौतिक लोक के राग, अभौतिक लोक के राग» (as 2-03 ^1-363)
    "1-553": {"rūpa": "सूक्ष्म भौतिक लोक", "arūpa": "अभौतिक लोक"},
}


def resolver(bid, kw, kws):
    o = OVERRIDES.get(bid, {})
    if kw in o:
        return o[kw]
    if kw in EXACT:
        return EXACT[kw]
    k = lc(kw)
    s = set(lc(x) for x in kws)
    if k in ("sahagatā", "somanassasahagatā", "upekkhāsahagatā") and (bid.endswith("-0") or bid in HEADING_LIKE):
        return {"sahagatā": "के साथ होने वाला", "somanassasahagatā": "प्रसन्नता के साथ होने वाला",
                "upekkhāsahagatā": "समभाव के साथ होने वाला"}[k]
    if k in ("kiriyāmano", "kiriyā mano") and s & {"kiriyāmanoviññāṇa", "kiriyā manoviññāṇa"}:
        return "केवल क्रिया रूपी … मन"   # «केवल क्रिया रूपी, X के साथ होने वाला मन की चेतना …»
    if k == "dukkha":           # dukkhapaṭipadaṃ = «दुःखद प्रगति»; dukkhasahagataṃ / dukkhindriyaṃ = «दुःख»
        return "दुःखद" if "dukkhapaṭipadaṃ" in s else "दुःख"
    if k == "sukha":             # sukhapaṭipadaṃ = «सुखद प्रगति»; diṭṭhadhammasukhavihāraṃ = «सुख से रहने»
        return "सुखद" if "sukhapaṭipadaṃ" in s else "सुख"
    return ch2_value(kw, kws, TABLE)


def kiya_ok(v, text):
    """Presence with the passive participle in its oblique/feminine form (किया ~ किए / की)."""
    return any(present(v.replace("किया", alt), text) for alt in ("किए", "की"))


if __name__ == "__main__":
    build_part(PART, resolver)
    bad, nde, miss = verify(PART, show=0)
    rest = [m for m in miss if not kiya_ok(m[2], read_hindi(PART)[m[0]])]
    print("presence misses explained by किया ~ किए/की:", len(miss) - len(rest), "| other misses:", len(rest))
    for m in rest:
        print("   MISS", *m)
