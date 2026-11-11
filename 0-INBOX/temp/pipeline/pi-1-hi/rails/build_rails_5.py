"""Builder for the Hindi rails translation of pi-1 chapter 5-atthakathakandam (plain audience).

Every Hindi string comes from the fixed tables below or from the approved 1-matika.md, so identical Pāli
gives byte-identical Hindi. Unknown Pāli raises an error instead of being guessed.

usage: python -I -X utf8 build_rails_5.py
"""
import pathlib
import re

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PALI = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
OUT = ROOT / "AI_translation" / "hindi" / "pi-1-hindi-plain-rails_split_chapters"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
CH = "5-atthakathakandam.md"


def segments(path):
    out, buf = [], []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        m = ID.search(line)
        if m:
            buf.append(line[: m.start()].rstrip())
            out.append((m.group(1), buf))
            buf = []
        else:
            buf.append(line)
    assert not buf
    return out


# ------------------------------------------------------------------ matrix names, read from the approved files
def matrix_names():
    names = {}
    pal = dict(segments(PALI / "1-matika.md"))
    hin = dict(segments(OUT / "1-matika.md"))
    labels = ("(Ka) ", "(Kha) ", "(Ga) ")
    kho = None
    for sid, plines in pal.items():
        for p, h in zip(plines, hin[sid]):
            if not p.startswith(labels):
                continue
            key = re.sub(r"\s*\[[^\]]*\]", "", p.split(") ", 1)[1]).strip().lower().rstrip(".")
            if " kho pana dhammā " in key:
                prefix, rest = key.split(" kho pana dhammā ", 1)
                key = f"{prefix} {rest[:-2] if rest.endswith('pi') else rest}"
                kho = prefix
            elif p.startswith("(Kha) ") and kho and key.endswith("pi"):
                key = f"{kho} {key[:-2]}"
                kho = None
            key = re.sub(r" dhammā\b", "", key).strip()
            val = re.sub(r"\s*\[[^\]]*\]", "", h.split(") ", 1)[1]).strip().rstrip("।")
            if val.endswith(" परिघटनाएँ"):
                val = val[: -len(" परिघटनाएँ")]
            elif not val.startswith("ऐसी परिघटनाएँ जो "):
                continue
            assert names.get(key, val) == val, (key, names[key], val)
            names[key] = val
    return names


NAMES = matrix_names()


def name(key):
    return NAMES[key.strip().lower()]


def phen(key):
    """The bare matrix name, with «परिघटनाएँ»."""
    v = name(key)
    return v if v.startswith("ऐसी ") else f"{v} परिघटनाएँ"


# ------------------------------------------------------------------ fixed vocabulary
KM = "इंद्रिय-सुखों के लोक से संबंधित"
RV = "सूक्ष्म भौतिक लोक से संबंधित"
AV = "अभौतिक लोक से संबंधित"
LU = "लोकोत्तर"
APAR = "अस्तित्व के लोकों में न समाए हुए"
MIND = "मन"
KB = "केवल क्रिया रूपी नैतिक रूप से अनिर्धारित मन"
NUM = {"eko": "एक", "dve": "दो", "cattāro": "चार", "pañca": "पाँच", "cha": "छह", "satta": "सात", "aṭṭha": "आठ",
       "nava": "नौ", "dasa": "दस", "ekādasa": "ग्यारह"}
FROM = {
    "kāmāvacarakusalato": f"{KM} हितकर मन",
    "akusalato": "हानिकर मन",
    "kāmāvacarakusalassa vipākato": f"{KM} हितकर कर्म के फल रूपी मन",
    "akusalassa vipākato": "हानिकर कर्म के फल रूपी मन",
    "kiriyato": "केवल क्रिया रूपी मन",
}
KIND = {
    "": "",
    " cittuppādā": "",
    " somanassasahagatacittuppādā": "प्रसन्नता के साथ होने वाली ",
    " upekkhāsahagatacittuppādā": "समभाव के साथ होने वाली ",
    " ñāṇavippayuttacittuppādā": "ज्ञान से अलग ",
    " ñāṇasampayuttacittuppādā": "ज्ञान से जुड़ी ",
}
LO = {
    "aṭṭhasu lobhasahagatesu cittuppādesu": "लोभ के साथ होने वाली मन की आठ उत्पत्तियों में",
    "dvīsu domanassasahagatesu cittuppādesu": "उदासी के साथ होने वाली मन की दो उत्पत्तियों में",
    "catūsu diṭṭhigatavippayuttalobhasahagatesu cittuppādesu":
        "ग़लत दृष्टि से अलग और लोभ के साथ होने वाली मन की चार उत्पत्तियों में",
    "catūsu diṭṭhigatasampayuttesu cittuppādesu": "ग़लत दृष्टि से जुड़ी मन की चार उत्पत्तियों में",
    "vicikicchāsahagatesu cittuppādesu": "संशय के साथ होने वाली मन की उत्पत्तियों में",
    "uddhaccasahagatesu cittuppādesu": "बेचैनी के साथ होने वाली मन की उत्पत्तियों में",
    "sabbākusalesu": "सभी हानिकर मनों में",
    "sasaṅkhārikesu akusalesu": "प्रेरणा सहित होने वाले हानिकर मनों में",
}
A8 = "aṭṭhasu lobhasahagatesu cittuppādesu"
D2 = "dvīsu domanassasahagatesu cittuppādesu"
V4 = "catūsu diṭṭhigatavippayuttalobhasahagatesu cittuppādesu"
S4 = "catūsu diṭṭhigatasampayuttesu cittuppādesu"
VS = "vicikicchāsahagatesu cittuppādesu"
US = "uddhaccasahagatesu cittuppādesu"
AL = "sabbākusalesu"
SK = "sasaṅkhārikesu akusalesu"

# subject, locus, Hindi subject, verb form
M, F, MP, FP = "होता है", "होती है", "होते हैं", "होती हैं"
ARISE = [
    ("kāmāsavo", A8, "इंद्रिय-सुखों का मैल", M),
    ("bhavāsavo", V4, "अस्तित्व का मैल", M),
    ("diṭṭhāsavo", S4, "दृष्टि का मैल", M),
    ("avijjāsavo", AL, "अज्ञान का मैल", M),
    ("kāmarāgasaṃyojanaṃ", A8, "इंद्रिय-सुखों के राग का बंधन", M),
    ("paṭighasaṃyojanaṃ", D2, "चिढ़ का बंधन", M),
    ("mānasaṃyojanaṃ", V4, "अहंकार का बंधन", M),
    ("diṭṭhisaṃyojanaṃ", S4, "दृष्टि का बंधन", M),
    ("vicikicchāsaṃyojanaṃ", VS, "संशय का बंधन", M),
    ("sīlabbataparāmāsasaṃyojanaṃ", S4, "सदाचार और व्रतों के बारे में ग़लत धारणा का बंधन", M),
    ("bhavarāgasaṃyojanaṃ", V4, "अस्तित्व के राग का बंधन", M),
    ("issāsaṃyojanañca macchariyasaṃyojanañca", D2, "ईर्ष्या का बंधन और कंजूसी का बंधन", MP),
    ("avijjāsaṃyojanaṃ", AL, "अज्ञान का बंधन", M),
    ("abhijjhākāyagantho", A8, "लालच रूपी काया की गाँठ", F),
    ("byāpādo kāyagantho", D2, "दुर्भावना रूपी काया की गाँठ", F),
    ("sīlabbataparāmāso kāyagantho ca idaṃsaccābhiniveso kāyagantho ca", S4,
     "सदाचार और व्रतों के बारे में ग़लत धारणा रूपी काया की गाँठ और “केवल यही सत्य है” के आग्रह रूपी काया की गाँठ", FP),
    ("kāmacchandanīvaraṇaṃ", A8, "इंद्रिय-सुखों की चाह की बाधा", F),
    ("byāpādanīvaraṇaṃ", D2, "दुर्भावना की बाधा", F),
    ("thinamiddhanīvaraṇaṃ", SK, "आलस्य और तंद्रा की बाधा", F),
    ("uddhaccanīvaraṇaṃ", US, "बेचैनी की बाधा", F),
    ("kukkuccanīvaraṇaṃ", D2, "पछतावे की बाधा", F),
    ("vicikicchānīvaraṇaṃ", VS, "संशय की बाधा", F),
    ("avijjānīvaraṇaṃ", AL, "अज्ञान की बाधा", F),
    ("diṭṭhiparāmāso", S4, "दृष्टि रूपी ग़लत धारणा", F),
    ("kāmupādānaṃ", A8, "इंद्रिय-सुखों के प्रति आसक्ति", F),
    ("diṭṭhupādānañca sīlabbatupādānañca attavādupādānañca", S4,
     "दृष्टियों के प्रति आसक्ति, सदाचार और व्रतों के प्रति आसक्ति और आत्मा के सिद्धांत के प्रति आसक्ति", FP),
    ("lobho", A8, "लोभ", M),
    ("doso", D2, "द्वेष", M),
    ("moho", AL, "मोह", M),
    ("māno", V4, "अहंकार", M),
    ("diṭṭhi", S4, "दृष्टि", F),
    ("vicikicchā", VS, "संशय", M),
    ("thinaṃ", SK, "आलस्य", M),
    ("uddhaccañca ahirikañca anottappañca", AL, "बेचैनी, निर्लज्जता और बुराई के प्रति निडरता", FP),
]

# the "&" prefix marks items that carry Pāli "ca": the last such item in a list is joined with «और»
T = {
    "catūsu bhūmīsu kusalaṃ": "चारों स्तरों का हितकर मन",
    "tīsu bhūmīsu kusalaṃ": "तीनों स्तरों का हितकर मन",
    "akusalaṃ": "हानिकर मन",
    "catūsu bhūmīsu vipāko": "चारों स्तरों का कर्म-फल रूपी मन",
    "tīsu bhūmīsu vipāko": "तीनों स्तरों का कर्म-फल रूपी मन",
    "tīsu bhūmīsu kiriyābyākataṃ": f"तीनों स्तरों का {KB}",
    "rūpañca nibbānañca": "भौतिक रूप और निर्वाण",
    "rūpañca": "&भौतिक रूप",
    "nibbānañca": "&निर्वाण",
    "nibbānaṃ": "निर्वाण",
    "sabbañca rūpaṃ": "&सारा भौतिक रूप",
    "avasesañca rūpaṃ": "&शेष भौतिक रूप",
    "cittañca": "&मन",
    "sukhañca": "&सुख",
    "pīti ca": "&उल्लास",
    "upekkhā ca": "&समभाव",
    "vitakko ca": "&आरंभिक विचार",
    "vicāro ca": "&सतत विचार",
    "yañca rūpaṃ kammassa katattā": "&जो भी भौतिक रूप कर्म किए जाने के कारण है",
    "yañca rūpaṃ na kammassa katattā": "&जो भी भौतिक रूप कर्म किए जाने के कारण नहीं है",
    "yañca rūpaṃ anidassanaṃ appaṭighaṃ dhammāyatanapariyāpannaṃ":
        "और जो भी भौतिक रूप दिखाई न देने वाला, टकराव से रहित और मन के विषयों के इंद्रिय-क्षेत्र में समाया हुआ है",
    "cattāro maggā apariyāpannā": f"{APAR} चार मार्ग",
    "cattāri ca sāmaññaphalāni": "&श्रमण-जीवन के चार फल",
    "heṭṭhimāni ca tīṇi sāmaññaphalāni": "&श्रमण-जीवन के नीचे के तीन फल",
    "upariṭṭhimaṃ arahattaphalaṃ": "सबसे ऊँचा अर्हत्-पद का फल",
    "dvādasa akusalacittuppādā": "हानिकर मन की बारह उत्पत्तियाँ",
    "dvādasākusalacittuppādā": "हानिकर मन की बारह उत्पत्तियाँ",
    "kāmāvacarakusalaṃ": f"{KM} हितकर मन",
    "kāmāvacaraṃ kusalaṃ": f"{KM} हितकर मन",
    "sabbo kāmāvacarassa vipāko": f"{KM} सारा कर्म-फल रूपी मन",
    "kāmāvacarakiriyābyākataṃ": f"{KM} {KB}",
    "sabbaṃ akusalaṃ": "सारा हानिकर मन",
    "avasesaṃ akusalaṃ": "शेष हानिकर मन",
    "catutthassa jhānassa vipāko": "चौथे ध्यान का कर्म-फल रूपी मन",
    # arisings of mind
    "cattāro diṭṭhigatasampayuttacittuppādā": "ग़लत दृष्टि से जुड़ी मन की चार उत्पत्तियाँ",
    "cattāro diṭṭhigatasampayuttalobhasahagatacittuppādā":
        "ग़लत दृष्टि से जुड़ी और लोभ के साथ होने वाली मन की चार उत्पत्तियाँ",
    "cattāro diṭṭhigatavippayuttalobhasahagatacittuppādā":
        "ग़लत दृष्टि से अलग और लोभ के साथ होने वाली मन की चार उत्पत्तियाँ",
    "cattāro diṭṭhigatavippayuttā lobhasahagatacittuppādā":
        "ग़लत दृष्टि से अलग और लोभ के साथ होने वाली मन की चार उत्पत्तियाँ",
    "dve domanassasahagatacittuppādā": "उदासी के साथ होने वाली मन की दो उत्पत्तियाँ",
    "aṭṭha lobhasahagatacittuppādā": "लोभ के साथ होने वाली मन की आठ उत्पत्तियाँ",
    "vicikicchāsahagato cittuppādo": "संशय के साथ होने वाली मन की उत्पत्ति",
    "uddhaccasahagato cittuppādo": "बेचैनी के साथ होने वाली मन की उत्पत्ति",
    "vicikicchāsahagato moho": "संशय के साथ होने वाला मोह",
    "uddhaccasahagato moho": "बेचैनी के साथ होने वाला मोह",
    "dvīsu domanassasahagatesu cittuppādesu uppanno moho": f"{LO[D2]} उत्पन्न मोह",
    "catūsu diṭṭhigatavippayuttalobhasahagatesu cittuppādesu uppanno lobho": f"{LO[V4]} उत्पन्न लोभ",
    "dvīsu domanassasahagatesu cittuppādesu uppannaṃ paṭighaṃ": f"{LO[D2]} उत्पन्न चिढ़",
    "kāmāvacarakusalassa vipākato ca kiriyato ca pañca":
        f"{KM} हितकर कर्म के फल रूपी और केवल क्रिया रूपी मन की पाँच-पाँच उत्पत्तियाँ",
    # feeling and sense consciousness
    "dukkhasahagataṃ kāyaviññāṇaṃ": "दुःख के साथ होने वाली शरीर की चेतना",
    "dukkhasahagatakāyaviññāṇaṃ": "दुःख के साथ होने वाली शरीर की चेतना",
    "tisso ca vedanā": "&तीन अनुभूतियाँ",
    "yā ca vedanā upekkhā": "&जो भी अनुभूति समभाव है",
    "dvepañcaviññāṇāni": "दोनों पाँच-पाँच इंद्रिय-चेतनाएँ",
    "tisso ca manodhātuyo": "&मन के तीन तत्व",
    "pañca ca ahetukamanoviññāṇadhātuyo": "&मूल से रहित मन की चेतना के पाँच तत्व",
    "kiriyāmanodhātu": "केवल क्रिया रूपी मन का तत्व",
    "kiriyāhetukamanoviññāṇadhātu somanassasahagatā":
        "मूल से रहित केवल क्रिया रूपी मन की चेतना का प्रसन्नता के साथ होने वाला तत्व",
    "kiriyāhetukamanoviññāṇadhātu upekkhāsahagatā":
        "मूल से रहित केवल क्रिया रूपी मन की चेतना का समभाव के साथ होने वाला तत्व",
    "akusalassa vipākato manoviññāṇadhātu upekkhāsahagatā":
        "हानिकर कर्म के फल रूपी मन में से समभाव के साथ होने वाला मन की चेतना का तत्व",
    # immaterial bases and sense bases
    "viññāṇañcāyatanaṃ": "अनंत चेतना का क्षेत्र",
    "nevasaññānāsaññāyatanaṃ": "न पहचान, न अ-पहचान का क्षेत्र",
    "ākāsānañcāyatanaṃ": "अनंत आकाश का क्षेत्र",
    "ākiñcaññāyatanaṃ": "कुछ भी न होने का क्षेत्र",
    "rūpāyatanaṃ": "दृश्य रूप का इंद्रिय-क्षेत्र",
    "cakkhāyatanaṃ…pe… phoṭṭhabbāyatanaṃ": "आँख का इंद्रिय-क्षेत्र… स्पर्श का इंद्रिय-क्षेत्र",
    "cakkhāyatanaṃ…pe… manāyatanaṃ": "आँख का इंद्रिय-क्षेत्र… मन का इंद्रिय-क्षेत्र",
    "rūpāyatanaṃ…pe… dhammāyatanaṃ": "दृश्य रूप का इंद्रिय-क्षेत्र… मन के विषयों का इंद्रिय-क्षेत्र",
    "cakkhāyatanaṃ…pe… kabaḷīkāro āhāro": "आँख का इंद्रिय-क्षेत्र… कौर-कौर खाया जाने वाला भोजन",
    "cakkhuviññāṇaṃ": "आँख की चेतना",
    "sotaviññāṇaṃ": "कान की चेतना",
    "ghānaviññāṇaṃ": "नाक की चेतना",
    "jivhāviññāṇaṃ": "जीभ की चेतना",
    "kāyaviññāṇaṃ": "शरीर की चेतना",
    "manodhātu": "मन का तत्व",
    "manoviññāṇadhātu": "मन की चेतना का तत्व",
    "vedanākkhandho": "अनुभूति का समूह",
    "saññākkhandho": "पहचान का समूह",
    "saṅkhārakkhandho": "मानसिक रचनाओं का समूह",
    "kāyaviññatti": "शरीर द्वारा प्रकट अभिव्यक्ति",
    "vacīviññatti": "वाणी द्वारा प्रकट अभिव्यक्ति",
    "yaṃ vā panaññampi atthi rūpaṃ cittajaṃ cittahetukaṃ cittasamuṭṭhānaṃ – rūpāyatanaṃ saddāyatanaṃ gandhāyatanaṃ "
    "rasāyatanaṃ phoṭṭhabbāyatanaṃ ākāsadhātu āpodhātu rūpassa lahutā rūpassa mudutā rūpassa kammaññatā rūpassa "
    "upacayo rūpassa santati kabaḷīkāro āhāro":
        "या जो भी अन्य भौतिक रूप मन से जन्मा, मन के कारण होने वाला और मन से उत्पन्न है – दृश्य रूप का इंद्रिय-क्षेत्र, "
        "ध्वनि का इंद्रिय-क्षेत्र, गंध का इंद्रिय-क्षेत्र, स्वाद का इंद्रिय-क्षेत्र, स्पर्श का इंद्रिय-क्षेत्र, आकाश तत्व, जल तत्व, "
        "भौतिक रूप का हल्कापन, भौतिक रूप की मृदुता, भौतिक रूप की कार्य-योग्यता, भौतिक रूप की वृद्धि, भौतिक रूप की धारा, "
        "कौर-कौर खाया जाने वाला भोजन",
    "cattāro ca mahābhūtā": "&चार महाभूत",
    "catunnañca mahābhūtānaṃ upādāya rūpaṃ": "&चार महाभूतों से व्युत्पन्न भौतिक रूप",
    # sphere lists
    "rūpāvacarā arūpāvacarā kusalābyākatā": f"{RV} और {AV} हितकर और नैतिक रूप से अनिर्धारित मन",
    "rūpāvacarā arūpāvacarā apariyāpannā":
        f"{RV}, {AV} और अस्तित्व के लोकों में न समाई हुई परिघटनाएँ",
    "kāmāvacarā arūpāvacarā apariyāpannā":
        f"{KM}, {AV} और अस्तित्व के लोकों में न समाई हुई परिघटनाएँ",
    "kāmāvacarā rūpāvacarā apariyāpannā":
        f"{KM}, {RV} और अस्तित्व के लोकों में न समाई हुई परिघटनाएँ",
    "sabbeva kāmāvacarā kusalākusalābyākatā dhammā":
        f"{KM} सभी हितकर, हानिकर और नैतिक रूप से अनिर्धारित परिघटनाएँ",
    # leaving aside
    "ṭhapetvā hetū": "मूलों को छोड़कर",
    "ṭhapetvā āsave avasesaṃ akusalaṃ": "मन के मैलों को छोड़कर शेष हानिकर मन",
    "ṭhapetvā saṃyojane avasesaṃ akusalaṃ": "बंधनों को छोड़कर शेष हानिकर मन",
    "ṭhapetvā ganthe avasesaṃ akusalaṃ": "गाँठों को छोड़कर शेष हानिकर मन",
    "ṭhapetvā nīvaraṇe avasesaṃ akusalaṃ": "बाधाओं को छोड़कर शेष हानिकर मन",
    "ṭhapetvā parāmāsaṃ avasesaṃ akusalaṃ": "ग़लत धारणा को छोड़कर शेष हानिकर मन",
    "ṭhapetvā upādāne avasesaṃ akusalaṃ": "आसक्तियों को छोड़कर शेष हानिकर मन",
    "ṭhapetvā kilese avasesaṃ akusalaṃ": "मन के क्लेशों को छोड़कर शेष हानिकर मन",
    "rūpaṃ ṭhapetvā": "भौतिक रूप को छोड़कर",
    "vicikicchāsahagataṃ uddhaccasahagataṃ mohaṃ ṭhapetvā avasesaṃ akusalaṃ":
        "संशय के साथ होने वाले और बेचैनी के साथ होने वाले मोह को छोड़कर शेष हानिकर मन",
    "vicikicchāsahagataṃ uddhaccasahagataṃ mohaṃ ṭhapetvā":
        "संशय के साथ होने वाले और बेचैनी के साथ होने वाले मोह को छोड़कर",
    "uddhaccasahagataṃ mohaṃ ṭhapetvā avasesaṃ akusalaṃ": "बेचैनी के साथ होने वाले मोह को छोड़कर शेष हानिकर मन",
    "kāmāvacarassa vipākato ahetuke cittuppāde ṭhapetvā":
        f"{KM} कर्म-फल रूपी मन की मूल से रहित उत्पत्तियों को छोड़कर",
    "kāmāvacarakiriyato ahetuke cittuppāde ṭhapetvā":
        f"{KM} केवल क्रिया रूपी मन की मूल से रहित उत्पत्तियों को छोड़कर",
    "etthuppannaṃ sukhaṃ vedanaṃ ṭhapetvā": "इनमें उत्पन्न सुखद अनुभूति को छोड़कर",
    "etthuppannaṃ dukkhaṃ vedanaṃ ṭhapetvā": "इनमें उत्पन्न दुःखद अनुभूति को छोड़कर",
    "etthuppannaṃ adukkhamasukhaṃ vedanaṃ ṭhapetvā": "इनमें उत्पन्न न दुःखद, न सुखद अनुभूति को छोड़कर",
    "etthuppanne vitakkavicāre ṭhapetvā": "इनमें उत्पन्न आरंभिक विचार और सतत विचार को छोड़कर",
    "etthuppannaṃ vicāraṃ ṭhapetvā": "इनमें उत्पन्न सतत विचार को छोड़कर",
    "etthuppannaṃ vitakkaṃ ṭhapetvā": "इनमें उत्पन्न आरंभिक विचार को छोड़कर",
    "etthuppannaṃ pītiṃ ṭhapetvā": "इनमें उत्पन्न उल्लास को छोड़कर",
    "etthuppannaṃ sukhaṃ ṭhapetvā": "इनमें उत्पन्न सुख को छोड़कर",
    "etthuppannaṃ upekkhaṃ ṭhapetvā": "इनमें उत्पन्न समभाव को छोड़कर",
    "etthuppannaṃ mohaṃ ṭhapetvā": "इनमें उत्पन्न मोह को छोड़कर",
    "etthuppannaṃ lobhaṃ ṭhapetvā": "इनमें उत्पन्न लोभ को छोड़कर",
    "etthuppannaṃ paṭighaṃ ṭhapetvā": "इनमें उत्पन्न चिढ़ को छोड़कर",
    "etthuppannaṃ parāmāsaṃ ṭhapetvā": "इनमें उत्पन्न ग़लत धारणा को छोड़कर",
    "etthuppanne hetū ṭhapetvā": "इनमें उत्पन्न मूलों को छोड़कर",
    "etthuppanne ganthe ṭhapetvā": "इनमें उत्पन्न गाँठों को छोड़कर",
    "etthuppanne upādāne ṭhapetvā": "इनमें उत्पन्न आसक्तियों को छोड़कर",
    # co-arising
    "yattha dve tayo hetū ekato uppajjanti": "जहाँ दो या तीन मूल एक साथ उत्पन्न होते हैं",
    "yattha dve tayo āsavā ekato uppajjanti": "जहाँ मन के दो या तीन मैल एक साथ उत्पन्न होते हैं",
    "yattha dve tīṇi saṃyojanāni ekato uppajjanti": "जहाँ दो या तीन बंधन एक साथ उत्पन्न होते हैं",
    "yattha diṭṭhi ca lobho ca ekato uppajjanti": "जहाँ दृष्टि और लोभ एक साथ उत्पन्न होते हैं",
    "yattha dve tīṇi nīvaraṇāni ekato uppajjanti": "जहाँ दो या तीन बाधाएँ एक साथ उत्पन्न होती हैं",
    "yattha dve tayo kilesā ekato uppajjanti": "जहाँ मन के दो या तीन क्लेश एक साथ उत्पन्न होते हैं",
    # the root lines of ^1-1441
    "alobho kiriyahetu adoso kiriyahetu kāmāvacarakiriyato ahetuke cittuppāde ṭhapetvā tīsu bhūmīsu kiriyesu uppajjanti":
        "लोभ का अभाव, जो केवल क्रिया रूपी मूल है, और द्वेष का अभाव, जो केवल क्रिया रूपी मूल है, "
        f"{KM} केवल क्रिया रूपी मन की मूल से रहित उत्पत्तियों को छोड़कर, तीनों स्तरों के केवल क्रिया रूपी मनों में उत्पन्न होते हैं",
    "amoho kiriyahetu kāmāvacarakiriyato ahetuke cittuppāde ṭhapetvā cattāro ñāṇavippayutte cittuppāde ṭhapetvā "
    "tīsu bhūmīsu kiriyesu uppajjati":
        f"मोह का अभाव, जो केवल क्रिया रूपी मूल है, {KM} केवल क्रिया रूपी मन की मूल से रहित उत्पत्तियों को छोड़कर, "
        "ज्ञान से अलग मन की चार उत्पत्तियों को छोड़कर, तीनों स्तरों के केवल क्रिया रूपी मनों में उत्पन्न होता है",
}

for f, fh in FROM.items():
    for n, nh in NUM.items():
        for k, kh in KIND.items():
            noun = "उत्पत्ति" if n == "eko" else "उत्पत्तियाँ"
            T[f"{f} {n}{k}"] = f"{fh} की {kh}{nh} {noun}"

JH = {}
for pre, ph in (("rūpāvacara", RV), ("lokuttara", LU)):
    JH[f"{pre}tikacatukkajjhānā"] = f"{ph} वे ध्यान जो चार-चार की विधि में तीन और पाँच-पाँच की विधि में चार हैं"
    JH[f"{pre}tikatikajjhānā"] = f"{ph} वे ध्यान जो चार-चार की विधि में तीन और पाँच-पाँच की विधि में तीन हैं"
    JH[f"{pre}dukatikajjhānā"] = f"{ph} वे ध्यान जो चार-चार की विधि में दो और पाँच-पाँच की विधि में तीन हैं"
    JH[f"{pre}dukadukajjhānā"] = f"{ph} वे ध्यान जो चार-चार की विधि में दो और पाँच-पाँच की विधि में दो हैं"
    JH[f"{pre}ekakadukajjhānā"] = f"{ph} वे ध्यान जो चार-चार की विधि में एक और पाँच-पाँच की विधि में दो हैं"
JH.update({
    "rūpāvacaracatukkapañcakajjhānā": f"{RV} वे ध्यान जो चार-चार की विधि और पाँच-पाँच की विधि में आते हैं",
    "rūpāvacaraṃ catutthaṃ jhānaṃ": f"{RV} चौथा ध्यान",
    "rūpāvacaracatutthaṃ jhānaṃ": f"{RV} चौथा ध्यान",
    "lokuttaraṃ catutthaṃ jhānaṃ": f"{LU} चौथा ध्यान",
    "rūpāvacaraṃ paṭhamaṃ jhānaṃ": f"{RV} पहला ध्यान",
    "lokuttaraṃ paṭhamaṃ jhānaṃ": f"{LU} पहला ध्यान",
    "rūpāvacarapañcakanaye dutiyaṃ jhānaṃ": f"पाँच-पाँच की विधि में {RV} दूसरा ध्यान",
    "lokuttarapañcakanaye dutiyaṃ jhānaṃ": f"पाँच-पाँच की विधि में {LU} दूसरा ध्यान",
    "cattāro āruppā": "चार अभौतिक अवस्थाएँ",
    "cattāro arūpāvacarā": f"{AV} चार अवस्थाएँ",
})
for j, jh in JH.items():
    T[f"{j} kusalato ca vipākato ca kiriyato ca"] = f"हितकर, कर्म-फल रूपी और केवल क्रिया रूपी मन में से {jh}"
    T[f"{j} kusalato ca vipākato ca"] = f"हितकर और कर्म-फल रूपी मन में से {jh}"
    T[f"{j} kusalato ca kiriyato ca"] = f"हितकर और केवल क्रिया रूपी मन में से {jh}"
T["pañcakanaye dutiye jhāne [dutiyajjhāne (sī.)] uppanno ca vicāro"] = \
    "&पाँच-पाँच की विधि के दूसरे ध्यान [वर्तनी-भेद (Sī.): dutiyajjhāne] में उत्पन्न सतत विचार"

for subj, loc, hs, verb in ARISE:
    T[f"{subj} {loc} {'uppajjati' if verb in (M, F) else 'uppajjanti'}"] = f"{LO[loc]} {hs} उत्पन्न {verb}"

TOK = re.compile("|".join(re.escape(k) for k in sorted(T, key=len, reverse=True)))


def tokens(body):
    s = re.sub(r"\s+", " ", body.lower().replace(",", " ").replace(";", " ")).strip()
    s = s.replace(" …pe…", "…pe…")
    pos, out = 0, []
    while pos < len(s):
        if s[pos] == " ":
            pos += 1
            continue
        m = TOK.match(s, pos)
        if not m:
            raise KeyError(f"no token at: {s[pos:pos + 90]}")
        out.append(T[m.group(0)])
        pos = m.end()
    return out


def join(items):
    last_ca = len(items) - 1 if items[-1].startswith("&") else None
    out = ""
    for i, it in enumerate(items):
        txt = it.lstrip("&")
        if i == 0:
            out = txt
        elif i == last_ca:
            out += (", और " if out.endswith(("कर", "है")) else " और ") + txt
        else:
            out += ", " + txt
    return out


def body(text):
    return join(tokens(text))


# ------------------------------------------------------------------ frames
def strip_ti(w):
    w = w.strip()
    for suf in ("cātipi", "cāti"):
        if w.endswith(suf):
            return w[: -len(suf)] + "ca"
    for suf in ("tipi", "ti"):
        if w.endswith(suf):
            return w[: -len(suf)]
    return w


def nv_list(names):
    if len(names) == 1:
        return f"{phen(names[0])} नहीं कहा जा सकता"
    first, *rest = [phen(n) for n in names]
    return f"न {first} कहा जा सकता है, " + ", ".join(f"न {r}" for r in rest)


def siya(text):
    """Translate the predicate of 'ime dhammā siyā X, siyā Y; na Z, siyā na vattabbā Atipi, Btipi'."""
    text = re.sub(r"(?<=[^\s,;]) siyā ", ", siyā ", text)
    parts = re.split(r"([,;]) ", text)
    clauses, seps = parts[0::2], parts[1::2]
    out, i = [], 0
    while i < len(clauses):
        c = clauses[i].strip()
        sep = seps[i] if i < len(seps) else ""
        m = re.match(r"(siyā )?na vattabbā (.+)$", c)
        if m:
            names = [strip_ti(m.group(2))]
            while i + 1 < len(clauses) and not clauses[i + 1].startswith(("siyā", "na ")):
                i += 1
                names.append(strip_ti(clauses[i]))
                sep = seps[i] if i < len(seps) else ""
            out.append(("कभी " if m.group(1) else "") + "इन्हें " + nv_list(names))
        elif c.startswith("siyā "):
            out.append(f"कभी {phen(c[5:])} होती हैं")
        elif c.startswith("na "):
            out.append(f"{phen(c[3:])} नहीं होतीं")
        else:
            out.append(f"{phen(c)} होती हैं")
        if sep:
            out.append(sep)
        i += 1
    txt = ""
    for x in out:
        txt += x if x in ",;" else (" " if txt else "") + x
    return txt


Q_RE = re.compile(r"^Katame dhammā (.+)[?.]$")
ANS = re.compile(r"^(.*) – ime dhammā (.+)\.$", re.S)
NEG = re.compile(r"^(.+?) dhammā na vattabbā – (.+)\.$")

ALL3 = "न सुखद अनुभूति से जुड़ी परिघटनाएँ कहा जा सकता है, न दुःखद अनुभूति से जुड़ी परिघटनाएँ"
EXACT = {
    "Katame dhammā oghā…pe….": f"{phen('oghā')} कौन-सी हैं…।",
    "Katame dhammā yogā…pe….": f"{phen('yogā')} कौन-सी हैं…।",
    "Katame dhammā no saṃyojanā.": f"{phen('no saṃyojanā')} कौन-सी हैं?",
    # the Pāli (^1-1389) reads "ya vedanāya": a truncated adukkhamasukhāya
    "Tisso ca vedanā, rūpañca, nibbānañca – ime dhammā na vattabbā sukhāya vedanāya sampayuttātipi, dukkhāya vedanāya sampayuttātipi, ya vedanāya sampayuttātipi.":
        f"तीन अनुभूतियाँ, भौतिक रूप और निर्वाण – इन परिघटनाओं को {ALL3}, और उन्हें {phen('adukkhamasukhāya vedanāya sampayuttā')} भी नहीं कहा जा सकता।",
    "Vitakkasahajāto vicāro na vattabbo savitakkasavicārotipi, avitakkavicāramattotipi, avitakkaavicārotipi.":
        "आरंभिक विचार के साथ उत्पन्न सतत विचार को न आरंभिक विचार और सतत विचार वाली परिघटना कहा जा सकता है, "
        "न आरंभिक विचार से रहित, केवल सतत विचार वाली परिघटना, न आरंभिक विचार और सतत विचार दोनों से रहित परिघटना।",
    "Pīti na pītisahagatā, sukhasahagatā, na upekkhāsahagatā.":
        "उल्लास स्वयं उल्लास के साथ होने वाली परिघटना नहीं है, सुख के साथ होने वाली परिघटना है, समभाव के साथ होने वाली परिघटना नहीं है।",
    "Sukhaṃ na sukhasahagataṃ, siyā pītisahagataṃ, na upekkhāsahagataṃ, siyā na vattabbaṃ pītisahagatanti.":
        "सुख स्वयं सुख के साथ होने वाली परिघटना नहीं है, कभी उल्लास के साथ होने वाली परिघटना है, "
        "समभाव के साथ होने वाली परिघटना नहीं है, कभी उसे उल्लास के साथ होने वाली परिघटना नहीं कहा जा सकता।",
    "Rūpañca nibbānañca anārammaṇā.": "भौतिक रूप और निर्वाण विषय से रहित हैं।",
    "Cattāro ariyamaggā na maggārammaṇā, maggahetukā; siyā maggādhipatino, siyā na vattabbā maggādhipatinoti.":
        f"चार आर्य मार्ग स्वयं {phen('maggārammaṇā')} नहीं हैं, {phen('maggahetukā')} हैं; "
        f"वे कभी {phen('maggādhipatino')} होते हैं, कभी उन्हें {phen('maggādhipatino')} नहीं कहा जा सकता।",
    "Nibbānaṃ na vattabbaṃ uppannantipi, anuppannantipi, uppādinotipi.":
        "निर्वाण को न उत्पन्न हो चुकी परिघटना कहा जा सकता है, न उत्पन्न न हुई परिघटना, न उत्पन्न होने वाली परिघटना।",
    "Nibbānaṃ ṭhapetvā sabbe dhammā siyā atītā, siyā anāgatā, siyā paccuppannā.":
        f"निर्वाण को छोड़कर सभी परिघटनाएँ कभी {phen('atītā')} होती हैं, कभी {phen('anāgatā')} होती हैं, कभी {phen('paccuppannā')} होती हैं।",
    "Nibbānaṃ na vattabbaṃ atītantipi, anāgatantipi, paccuppannantipi.":
        "निर्वाण को न अतीत की परिघटना कहा जा सकता है, न भविष्य की परिघटना, न वर्तमान की परिघटना।",
    "Niyogā anāgatārammaṇā natthi.": f"अनिवार्य रूप से {phen('anāgatārammaṇā')} कोई नहीं हैं।",
    "Anindriyabaddharūpañca nibbānañca ṭhapetvā, sabbe dhammā siyā ajjhattā, siyā bahiddhā, siyā ajjhattabahiddhā.":
        f"इंद्रियों से न बँधे भौतिक रूप और निर्वाण को छोड़कर, सभी परिघटनाएँ कभी {phen('ajjhattā')} होती हैं, "
        f"कभी {phen('bahiddhā')} होती हैं, कभी {phen('ajjhattabahiddhā')} होती हैं।",
    "Anindriyabaddharūpañca nibbānañca bahiddhā.": f"इंद्रियों से न बँधा भौतिक रूप और निर्वाण {phen('bahiddhā')} हैं।",
    "Ākiñcaññāyatanaṃ na vattabbaṃ ajjhattārammaṇantipi, bahiddhārammaṇantipi, ajjhattabahiddhārammaṇantipi.":
        "कुछ भी न होने के क्षेत्र को न स्वयं से संबंधित विषय वाली परिघटना कहा जा सकता है, "
        "न दूसरों से संबंधित विषय वाली परिघटना, न स्वयं और दूसरों दोनों से संबंधित विषय वाली परिघटना।",
    "Sabbe [sabbeva (syā.)] dhammā kenaci viññeyyā, kenaci na viññeyyā.":
        "सभी [पाठभेद (Syā.): sabbeva] परिघटनाएँ किसी एक प्रकार की चेतना से जानी जा सकने वाली परिघटनाएँ हैं, "
        "और किसी एक प्रकार की चेतना से न जानी जा सकने वाली परिघटनाएँ भी हैं।",
    "Cittaṃ na vattabbaṃ – cittena sampayuttantipi, cittena vippayuttantipi.":
        "मन को नहीं कहा जा सकता – न मन से जुड़ी परिघटना, न मन से अलग परिघटना।",
    "Cittaṃ na vattabbaṃ – cittena saṃsaṭṭhantipi, cittena visaṃsaṭṭhantipi.":
        "मन को नहीं कहा जा सकता – न मन से घुली-मिली परिघटना, न मन से घुली-मिली न होने वाली परिघटना।",
    "Parāmāso na vattabbo – parāmāsasampayuttotipi, parāmāsavippayuttotipi.":
        "ग़लत धारणा को नहीं कहा जा सकता – न ग़लत धारणा से जुड़ी परिघटना, न ग़लत धारणा से अलग परिघटना।",
    "Parāmāsā ca parāmāsasampayuttā ca dhammā na vattabbā – parāmāsavippayuttā parāmaṭṭhātipi, parāmāsavippayuttā aparāmaṭṭhātipi.":
        f"{phen('parāmāsā')[:-len('परिघटनाएँ')]}परिघटनाओं और {phen('parāmāsasampayuttā')[:-len('परिघटनाएँ')]}परिघटनाओं को नहीं कहा जा सकता – "
        f"न {phen('parāmāsavippayuttā parāmaṭṭhā')}, न {phen('parāmāsavippayuttā aparāmaṭṭhā')}।",
    "Teva āsavā āsavā ceva sāsavā ca.": f"{phen('āsavā ceva sāsavā ca')} वे ही मन के मैल हैं।",
    "Tāneva saṃyojanāni saṃyojanā ceva saṃyojaniyā ca.": f"{phen('saṃyojanā ceva saṃyojaniyā ca')} वे ही बंधन हैं।",
    "Teva ganthā ganthā ceva ganthaniyā ca.": f"{phen('ganthā ceva ganthaniyā ca')} वे ही गाँठें हैं।",
    "Tāneva nīvaraṇāni nīvaraṇā ceva nīvaraṇiyā ca.": f"{phen('nīvaraṇā ceva nīvaraṇiyā ca')} वे ही बाधाएँ हैं।",
    "Tāneva upādānāni upādānā ceva upādāniyā ca.": f"{phen('upādānā ceva upādāniyā ca')} वे ही आसक्तियाँ हैं।",
    "Teva kilesā kilesā ceva saṃkilesikā ca.": f"{phen('kilesā ceva saṃkilesikā ca')} वे ही मन के क्लेश हैं।",
    "Teva kilesā kilesā ceva saṃkiliṭṭhā ca.": f"{phen('kilesā ceva saṃkiliṭṭhā ca')} वे ही मन के क्लेश हैं।",
    "So eva parāmāso parāmāso ceva parāmaṭṭho ca.":
        f"{name('parāmāsā ceva parāmaṭṭhā ca')} परिघटना वही ग़लत धारणा है।",
    "Cattāro āsavā – kāmāsavo, bhavāsavo, diṭṭhāsavo, avijjāsavo.":
        "मन के चार मैल – इंद्रिय-सुखों का मैल, अस्तित्व का मैल, दृष्टि का मैल, अज्ञान का मैल।",
    "Dasa saṃyojanāni – kāmarāgasaṃyojanaṃ, paṭighasaṃyojanaṃ, mānasaṃyojanaṃ, diṭṭhisaṃyojanaṃ, vicikicchāsaṃyojanaṃ, sīlabbataparāmāsasaṃyojanaṃ, bhavarāgasaṃyojanaṃ, issāsaṃyojanaṃ, macchariyasaṃyojanaṃ, avijjāsaṃyojanaṃ.":
        "दस बंधन – इंद्रिय-सुखों के राग का बंधन, चिढ़ का बंधन, अहंकार का बंधन, दृष्टि का बंधन, संशय का बंधन, "
        "सदाचार और व्रतों के बारे में ग़लत धारणा का बंधन, अस्तित्व के राग का बंधन, ईर्ष्या का बंधन, कंजूसी का बंधन, अज्ञान का बंधन।",
    "Cattāro ganthā – abhijjhākāyagantho, byāpādo kāyagantho, sīlabbataparāmāso kāyagantho, idaṃsaccābhiniveso kāyagantho.":
        "चार गाँठें – लालच रूपी काया की गाँठ, दुर्भावना रूपी काया की गाँठ, सदाचार और व्रतों के बारे में ग़लत धारणा रूपी काया की गाँठ, "
        "“केवल यही सत्य है” के आग्रह रूपी काया की गाँठ।",
    "Cha nīvaraṇā – kāmacchandanīvaraṇaṃ, byāpādanīvaraṇaṃ, thinamiddhanīvaraṇaṃ, uddhaccakukkuccanīvaraṇaṃ, vicikicchānīvaraṇaṃ, avijjānīvaraṇaṃ.":
        "छह बाधाएँ – इंद्रिय-सुखों की चाह की बाधा, दुर्भावना की बाधा, आलस्य और तंद्रा की बाधा, बेचैनी और पछतावे की बाधा, संशय की बाधा, अज्ञान की बाधा।",
    "Cattāri upādānāni – kāmupādānaṃ, diṭṭhupādānaṃ, sīlabbatupādānaṃ, attavādupādānaṃ.":
        "चार आसक्तियाँ – इंद्रिय-सुखों के प्रति आसक्ति, दृष्टियों के प्रति आसक्ति, सदाचार और व्रतों के प्रति आसक्ति, आत्मा के सिद्धांत के प्रति आसक्ति।",
    "Dasa kilesavatthūni – lobho, doso, moho, māno, diṭṭhi, vicikicchā, thinaṃ, uddhaccaṃ, ahirikaṃ, anottappaṃ.":
        "मन के क्लेशों के दस आधार – लोभ, द्वेष, मोह, अहंकार, दृष्टि, संशय, आलस्य, बेचैनी, निर्लज्जता, बुराई के प्रति निडरता।",
    "Tayo kusalahetū, tayo akusalahetū, tayo abyākatahetū.": "तीन हितकर मूल, तीन हानिकर मूल, तीन नैतिक रूप से अनिर्धारित मूल।",
    "Alobho kusalahetu, adoso kusalahetu, catūsu bhūmīsu kusalesu uppajjanti.":
        "लोभ का अभाव रूपी हितकर मूल और द्वेष का अभाव रूपी हितकर मूल चारों स्तरों के हितकर मनों में उत्पन्न होते हैं।",
    "Amoho kusalahetu, kāmāvacarakusalato cattāro ñāṇavippayutte cittuppāde ṭhapetvā, catūsu bhūmīsu kusalesu uppajjati.":
        f"मोह का अभाव रूपी हितकर मूल, {KM} हितकर मन की ज्ञान से अलग चार उत्पत्तियों को छोड़कर, चारों स्तरों के हितकर मनों में उत्पन्न होता है।",
    "Alobho vipākahetu adoso vipākahetu, kāmāvacarassa vipākato ahetuke cittuppāde ṭhapetvā, catūsu bhūmīsu vipākesu uppajjanti.":
        "लोभ का अभाव, जो कर्म-फल रूपी मूल है, और द्वेष का अभाव, जो कर्म-फल रूपी मूल है, "
        f"{KM} कर्म-फल रूपी मन की मूल से रहित उत्पत्तियों को छोड़कर, चारों स्तरों के कर्म-फल रूपी मनों में उत्पन्न होते हैं।",
    "Amoho vipākahetu, kāmāvacarassa vipākato ahetuke cittuppāde ṭhapetvā, cattāro ñāṇavippayutte cittuppāde ṭhapetvā, catūsu bhūmīsu vipākesu uppajjati.":
        f"मोह का अभाव, जो कर्म-फल रूपी मूल है, {KM} कर्म-फल रूपी मन की मूल से रहित उत्पत्तियों को छोड़कर, "
        "ज्ञान से अलग मन की चार उत्पत्तियों को छोड़कर, चारों स्तरों के कर्म-फल रूपी मनों में उत्पन्न होता है।",
    "Alobho kiriyahetu adoso kiriyahetu, kāmāvacarakiriyato ahetuke cittuppāde ṭhapetvā, tīsu bhūmīsu kiriyesu uppajjanti.":
        "लोभ का अभाव, जो केवल क्रिया रूपी मूल है, और द्वेष का अभाव, जो केवल क्रिया रूपी मूल है, "
        f"{KM} केवल क्रिया रूपी मन की मूल से रहित उत्पत्तियों को छोड़कर, तीनों स्तरों के केवल क्रिया रूपी मनों में उत्पन्न होते हैं।",
    "Tikaṃ.": "तीन-तीन के वर्गीकरण।",
    "Atthuddhāro niṭṭhito.": "अर्थ-निर्धारण पूरा हुआ।",
    "Dhammasaṅgaṇīpakaraṇaṃ niṭṭhitaṃ.": "“परिघटनाओं की गणना” ग्रंथ पूरा हुआ।",
}

HEAD = {
    "Aṭṭhakathākaṇḍaṃ": "अर्थ-व्याख्या का अध्याय",
    "Tikaatthuddhāro": "तीन-तीन के वर्गीकरणों का अर्थ-निर्धारण",
    "Dukaatthuddhāro": "दो-दो के वर्गीकरणों का अर्थ-निर्धारण",
    "Hetugocchakaṃ": "मूलों का वर्ग",
    "Cūḷantaradukaṃ": "बीच के छोटे दो-दो के वर्गीकरण",
    "Āsavagocchakaṃ": "मन के मैलों का वर्ग",
    "Saṃyojanagocchakaṃ": "बंधनों का वर्ग",
    "Ganthagocchakaṃ": "गाँठों का वर्ग",
    "Oghagocchakaṃ": "बाढ़ों का वर्ग",
    "Yogagocchakaṃ": "जकड़नों का वर्ग",
    "Nīvaraṇagocchakaṃ": "बाधाओं का वर्ग",
    "Parāmāsagocchakaṃ": "ग़लत धारणा का वर्ग",
    "Mahantaradukaṃ": "बीच के बड़े दो-दो के वर्गीकरण",
    "Upādānagocchakaṃ": "आसक्ति का वर्ग",
    "Kilesagocchakaṃ": "मन के क्लेशों का वर्ग",
    "Piṭṭhidukaṃ": "अंतिम दो-दो के वर्गीकरण",
}


def obl(key):
    return phen(key)[: -len("परिघटनाएँ")] + "परिघटनाओं"


def sentence(s):
    if s in EXACT:
        return EXACT[s]
    m = Q_RE.match(s)
    if m and s.endswith("?"):
        v = name(m.group(1))
        if v.startswith("ऐसी परिघटनाएँ जो "):
            return "कौन-सी परिघटनाएँ " + v[len("ऐसी परिघटनाएँ जो "):] + "?"
        return f"{v} परिघटनाएँ कौन-सी हैं?"
    m = NEG.match(s)
    if m:
        items = [strip_ti(x) for x in m.group(2).split(", ")]
        return f"{obl(m.group(1).lower())} को नहीं कहा जा सकता – " + ", ".join(f"न {phen(x)}" for x in items) + "।"
    m = ANS.match(s)
    if m:
        b, pred = m.group(1), m.group(2).strip()
        lead = body(b)
        if pred.startswith("na vattabbā "):
            names = [strip_ti(x) for x in pred[len("na vattabbā "):].split(", ")]
            return f"{lead} – इन परिघटनाओं को {nv_list(names)}।"
        if pred.startswith("siyā "):
            return f"{lead} – ये {siya(pred)}।"
        v = name(pred)
        if v.startswith("ऐसी परिघटनाएँ जो "):
            return f"{lead} – ये परिघटनाएँ {v[len('ऐसी परिघटनाएँ जो '):]}।"
        return f"{lead} – ये {v} परिघटनाएँ हैं।"
    return body(s.rstrip(".")) + "।"


def line(l):
    if l.startswith("#"):
        hashes, text = l.split(" ", 1)
        return f"{hashes} {HEAD[text]}"
    parts = re.split(r"(?<=[?.])\s+", l)
    return " ".join(sentence(p) for p in parts)


def main():
    errs, blocks = [], []
    for sid, plines in segments(PALI / CH):
        hl = []
        for p in plines:
            try:
                hl.append(line(p))
            except KeyError as e:
                errs.append(f"{sid}: {e}")
                hl.append("?")
        hl[-1] += f" ^{sid}"
        blocks.append("\n".join(hl))
    if errs:
        print(len(errs), "unresolved")
        print("\n".join(errs[:60]))
        raise SystemExit(1)
    (OUT / CH).write_text("\n\n".join(blocks) + "\n", encoding="utf-8", newline="\n")
    print("wrote", OUT / CH, len(blocks), "segments")


if __name__ == "__main__":
    main()
