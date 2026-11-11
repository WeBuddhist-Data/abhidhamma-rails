"""Map 2-04-cittuppadakandam keywords to the Hindi translation (CH2 + 2-04 table + context rules + overrides).

usage: python -I -X utf8 map_2-04_hi.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_hi import CH2, NDE, GAP, ch2_value, build_part, verify, read_hindi, present, lc  # noqa: E402

PART = "2-04-cittuppadakandam"

# ---------------------------------------------------------------- 2-04 table (extends CH2)
T = {**CH2,
     # headings / closings
     "dvādasa": "बारह", "akusalāni": "हानिकर", "akusalacittāni": "हानिकर मन",
     "abyākata": "नैतिक रूप से अनिर्धारित", "abyākatavipāko": "नैतिक रूप से अनिर्धारित कर्म-फल",
     "vipāka": "कर्म के फल रूपी", "vipākā": "कर्म के फल रूपी", "vipākāni": "कर्म के फल रूपी",
     "kusalavipāka": "हितकर कर्म के फल रूपी", "kusalavipākā": "हितकर कर्म के फल रूपी",
     "kusalavipākāni": "हितकर कर्म के फल रूपी",
     "viññāṇāni": "चेतना",
     "vipākapañcaviññāṇāni": "कर्म के फल रूपी पाँच प्रकार की चेतना",
     "vipākāni pañcaviññāṇāni": "कर्म के फल रूपी पाँच प्रकार की चेतना",
     "manodhātu": "मन का तत्व",
     "vipākamanodhātu": "कर्म के फल रूपी मन का तत्व",
     "vipākā manodhātu": "कर्म के फल रूपी मन का तत्व",
     "vipākamanoviññāṇadhātu": "कर्म के फल रूपी" + GAP + "मन की चेतना का तत्व",
     "vipākā manoviññāṇadhātu": "कर्म के फल रूपी" + GAP + "मन की चेतना का तत्व",
     "vipākā upekkhāsahagatā manoviññāṇadhātu": "कर्म के फल रूपी समभाव के साथ होने वाला मन की चेतना का तत्व",
     "mahāvipākā": "बड़ा कर्म-फल",
     "rūpāvacara": "सूक्ष्म भौतिक लोक से संबंधित", "arūpāvacara": "अभौतिक लोक से संबंधित",
     "arūpa": "अभौतिक",
     # opening clauses
     "akusalā": "हानिकर", "dhammā akusalā": "हानिकर परिघटना", "akusalaṃ cittaṃ": "हानिकर मन",
     "akusala": "हानिकर", "cittaṃ uppannaṃ": "मन उत्पन्न",
     "abyākatā": "नैतिक रूप से अनिर्धारित", "dhammā abyākatā": "नैतिक रूप से अनिर्धारित परिघटना",
     "dhammārammaṇaṃ": "मन का विषय", "dhammārammaṇā": "मन का विषय", "ārammaṇā": "विषय",
     "diṭṭhigata": "ग़लत दृष्टि", "diṭṭhigatavippayuttaṃ": "ग़लत दृष्टि से अलग",
     "domanassa": "उदासी", "domanassasahagataṃ": "उदासी के साथ होना", "paṭigha": "चिढ़",
     "uddhacca": "बेचैनी",
     "sahagatā": "के साथ होना", "somanassasahagatā": "प्रसन्नता के साथ होना",
     "upekkhāsahagatā": "समभाव के साथ होना", "sukhasahagataṃ": "सुख के साथ होना", "sukha": "सुख",
     "uppannā": "उत्पन्न", "dhātu uppannā": "तत्व उत्पन्न",
     "sampayuttā": "जुड़ा", "vippayuttā": "अलग", "ñāṇavippayuttā": "ज्ञान से अलग",
     "kāmāvacarassa": "इंद्रिय-सुखों के लोक से संबंधित", "avacarassa": "लोक से संबंधित",
     "kusalassa": "हितकर", "kusalassa kammassa": "हितकर कर्म",
     "katattā": "किया जाना", "upacitattā": "संचित होना",
     "cakkhuviññāṇaṃ": "आँख की चेतना", "sotaviññāṇaṃ": "कान की चेतना",
     "ghānaviññāṇaṃ": "नाक की चेतना", "jivhāviññāṇaṃ": "जीभ की चेतना",
     "kāyaviññāṇaṃ": "शरीर की चेतना",
     "cakkhuviññāṇa": "आँख की चेतना", "cakkhuviññāṇadhātu": "आँख की चेतना का तत्व",
     "kāyaviññāṇa": "शरीर की चेतना", "kāyaviññāṇadhātu": "शरीर की चेतना का तत्व",
     "abyākatamūlaṃ": "नैतिक रूप से अनिर्धारित मूल",
     # factor names
     "micchā": "ग़लत", "micchādiṭṭhi": "ग़लत दृष्टि", "micchāsaṅkappo": "ग़लत संकल्प",
     "micchāvāyāmo": "ग़लत प्रयास", "micchāsamādhi": "ग़लत एकाग्रता",
     "ahirika": "निर्लज्जता", "ahirikaṃ": "निर्लज्जता", "ahirikabalaṃ": "निर्लज्जता का बल",
     "anottappa": "बुराई के प्रति निडरता", "anottappaṃ": "बुराई के प्रति निडरता",
     "anottappabalaṃ": "बुराई के प्रति निडरता का बल",
     "lobho": "लोभ", "doso": "द्वेष", "moho": "मोह", "abhijjhā": "लालच", "byāpādo": "दुर्भावना",
     "vicikicchā": "संशय", "uddhaccaṃ": "बेचैनी", "dukkhaṃ": "दुःख",
     "tivaṅgiko": "तीन अंगों वाला", "duvaṅgiko": "दो अंगों वाला", "hetu": "मूल",
     # ahirika / anottappa strings
     "ottappitabbena": "जिस बात से डरना चाहिए",
     # lobha string
     "samaye lobho": "उस समय" + GAP + "लोभ", "sārāgo": "राग",
     "akusalamūlaṃ": "हानिकर मूल",
     # moha string (pi-4 ^4-60 forms; fragments that lost a- map to the positive part)
     "aññāṇaṃ": "न जानना", "ñāṇaṃ": "जानना", "dassanaṃ": "देखना",
     "anabhisamayo": "सत्य तक न पहुँचना", "anubodho": "बोध", "sambodho": "पूर्ण बोध",
     "appaṭivedho": "भेद न पाना", "asaṃgāhanā": "न समेट पाना", "pariyogāhanā": "गहराई में उतरना",
     "samapekkhanā": "निष्पक्ष रूप से देखना", "paccavekkhanā": "पुनः विचार करना",
     "paccakkhakammaṃ": "प्रत्यक्ष करना", "dummejjhaṃ": "दुर्बुद्धि", "bālyaṃ": "मूर्खता",
     "pamoho": "गहरा मोह", "sammoho": "घोर मोह", "avijjā": "अज्ञान", "ogho": "बाढ़",
     "yogo": "जकड़न", "anusayo": "सुप्त प्रवृत्ति", "pariyuṭṭhānaṃ": "आवेश", "laṅgī": "रुकावट",
     # diṭṭhi string
     "diṭṭhigataṃ": "दृष्टि में पड़ जाना", "gahanaṃ": "घना जंगल", "kantāro": "बीहड़",
     "visūkāyikaṃ": "टेढ़ापन", "vipphanditaṃ": "छटपटाहट", "saṃyojanaṃ": "बंधन",
     "diṭṭhisaṃyojanaṃ": "दृष्टि का बंधन", "gāho": "पकड़", "patiṭṭhāho": "कसकर पकड़ना",
     "abhiniveso": "आग्रह", "parāmāso": "ग़लत धारणा", "kummaggo": "कुमार्ग",
     "micchāpatho": "ग़लत रास्ता", "patho": "रास्ता", "micchattaṃ": "ग़लतपन", "tittha": "मतवाद",
     "vipariyāsa": "उलटा", "vipariyāsaggāho": "उलटी पकड़",
     # dosa string (pi-4 ^4-45)
     "dussanā": "द्वेष करना", "dussitattaṃ": "द्वेष से भरा होना", "byāpatti": "दुर्भावना",
     "byāpajjanā": "दुर्भावना रखना", "virodho": "विरोध", "paṭivirodho": "प्रतिविरोध",
     "caṇḍikkaṃ": "उग्रता", "asuropo": "कटु वचन", "anattamanatā": "अप्रसन्नता",
     # vicikicchā string
     "kaṅkhā": "शंका", "kaṅkhāyanā": "शंका करना", "vimati": "दुविधा", "dveḷhakaṃ": "दुचित्तापन",
     "dvedhā": "दोराहा", "saṃsayo": "संदेह", "ekaṃsa": "एक बात",
     "anekaṃsaggāho": "किसी एक बात को पक्का न पकड़ पाना",
     "āsappanā": "हिचकिचाना", "parisappanā": "बार-बार हिचकिचाना",
     "thambhitattaṃ": "जड़ हो जाना", "vilekho": "खरोंच",
     # uddhacca string
     "avūpasamo": "अशांति", "vikkhepo": "भटकाव", "bhantattaṃ": "डोलना",
     # feeling strings (dukkha / kāyika)
     "cetasikaṃ dukkhaṃ": "मानसिक दुःख", "dukkhā vedanā": "दुःखद अनुभूति",
     "kāyikaṃ": "शारीरिक", "kāyasamphassajaṃ": "शरीर के संपर्क से उत्पन्न",
     "kāyasamphassajā": "शरीर के संपर्क से उत्पन्न",
     # fine-material / immaterial results
     "bhāveti": "अभ्यास करना", "maggaṃ": "मार्ग", "maggaṃ bhāveti": "मार्ग का अभ्यास करना",
     "upapattiyā": "जन्म", "upapattiyā maggaṃ": "जन्म की ओर ले जाने वाला मार्ग",
     "rūpāvacarassa": "सूक्ष्म भौतिक लोक से संबंधित", "arūpāvacarassa": "अभौतिक लोक से संबंधित",
     "vivicca": "अलग होकर", "eva": NDE, "kāmehi": "इंद्रिय-सुख",
     "vivicceva kāmehi": "इंद्रिय-सुखों से अलग होकर",
     "upasampajja": "प्राप्त करके", "viharati": "रहना",
     "upasampajja viharati": "प्राप्त करके उसमें रहना",
     "pathavī": "पृथ्वी", "kasiṇaṃ": "ध्यान-मंडल",
     "vitakka": "आरंभिक विचार", "vicārānaṃ": "सतत विचार", "vūpasamā": "शांत होना",
     "pañcamaṃ": "पाँचवाँ", "catutthaṃ jhānaṃ": "चौथा ध्यान",
     "sukhassa": "सुख", "pahānā": "त्याग", "sukhassa ca pahānā": "सुख का त्याग",
     "sabbaso": "पूरी तरह", "samatikkamā": "पार कर जाना", "samatikkamma": "पार करके",
     "atthaṅgamā": "मिट जाना", "nānatta": "विविधता", "manasikārā": "मनोयोग करना",
     "saññānaṃ": "पहचान", "ākāsa": "आकाश", "ānañca": "अनंत",
     "ānañcāyatana": "अनंत" + GAP + "क्षेत्र", "ānañcāyatanaṃ": "अनंत" + GAP + "क्षेत्र",
     "viññāṇañca": "अनंत चेतना", "viññāṇañcāyatanaṃ": "अनंत चेतना का क्षेत्र",
     "ākiñcañña": "कुछ भी न होना", "asaññā": "अ-पहचान",
     }

HEADING_SAHAGATA = {"1-1-7-3-0", "1-1-7-4-0", "1-483", "1-497"}   # «… के साथ होने वाला» (name/colophon)
JHANA = {"1-499", "1-500", "1-501", "1-502", "1-503", "1-504"}


def resolver(bid, kw, kws):
    o = OVERRIDES.get(bid, {})
    if kw in o:
        return o[kw]
    k = lc(kw)
    s = set(lc(x) for x in kws)
    # sahagatā in a heading or colophon = «… के साथ होने वाला»
    if bid in HEADING_SAHAGATA and k in ("sahagatā", "somanassasahagatā", "upekkhāsahagatā"):
        return {"sahagatā": "के साथ होने वाला", "somanassasahagatā": "प्रसन्नता के साथ होने वाला",
                "upekkhāsahagatā": "समभाव के साथ होने वाला"}[k]
    # mano outside the citta string (manodhātu, manovilekho) = मन
    if k == "mano" and "mānasaṃ" not in s and "manosañcetanā" not in s:
        return "मन"
    # rūpa: rūpārammaṇa = दृश्य रूप (CH2); rūpūpapatti / rūpāvacara = सूक्ष्म भौतिक; rūpasaññā = भौतिक रूप
    if k == "rūpa" and bid in JHANA:
        return "भौतिक रूप" if "saññānaṃ" in s else "सूक्ष्म भौतिक"
    # «X-saññāsahagataṃ» = «X की पहचान के साथ» (no verb)
    if k == "sahagataṃ" and bid in JHANA:
        return "के साथ"
    # patho of dvedhāpatho (vicikicchā string) = दोराहा
    if k == "patho" and "dvedhā" in s:
        return "दोराहा"
    return ch2_value(kw, kws, T)


# per-segment overrides: {bid: {kw: value}}
OVERRIDES = {
    "1-1-7-6-0": {"Rūpa": "सूक्ष्म भौतिक"},   # heading Rūpāvacaravipākā (as matrix 1-M2-94)
}


def presence_misses():
    """Presence check with one extra tolerance: «किया जाना» (katattā) ~ «किए जाने»."""
    hi = read_hindi(PART)
    miss = []
    for line in (pathlib.Path(__file__).resolve().parent / f"{PART}.mapped.md").read_text(encoding="utf-8").splitlines():
        bid, rest = line.split("] ", 1)
        bid = bid[1:]
        for pair in rest.split(", "):
            kw, v = pair.split("=", 1)
            if v == NDE:
                continue
            if not present(v.replace("किया जाना", "किए जाना"), hi.get(bid, "")):
                miss.append((bid, kw, v))
    return miss


if __name__ == "__main__":
    build_part(PART, resolver)
    verify(PART, show=0)
    m = presence_misses()
    print("presence misses after the किया~किए tolerance:", len(m))
    for x in m:
        print("   MISS", *x)
