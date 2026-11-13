"""Hindi plain zero-shot builder for pi-7 Paṭṭhāna, files 2-04 .. 2-08.

Each Pāli line is translated by a fixed pipeline of formula rules (the same Pāli phrase always
gets the same Hindi), reusing the approved sample constants from build_sample_hi.py (imported,
never edited). Hindi agreement is resolved after the phrase rules:
  ⟦gnc⟧  noun tag (g 1=m 2=f, n 1=sg 2=pl, c 1=direct 2=oblique)
  ⟨i⟩    agreeing word (adjective / genitive particle), index into AGR, inflected by the next tag
  ⟨V⟩    verb "होता है" family, agrees with the previous direct-case tag in the clause
  ⟨PR⟩   pronoun उस/उन by the number of the previous tag
  ⟨J⟩    "या" (sg) / "और" (pl) between two agreeing words, by the next tag

    python -I -B -X utf8 build_2-04_2-08_hi.py            # write + report
    python -I -B -X utf8 build_2-04_2-08_hi.py --check    # report only
"""
import pathlib
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi")
import build_sample_hi as S  # noqa: E402

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PALI_DIR = ROOT / "AI_translation" / "pali" / "pi-7_split_chapters"
HI_DIR = ROOT / "AI_translation" / "hindi" / "pi-7-hindi-plain-zeroshot_split_chapters"

L = "a-zāīūṃñṅṭḍṇḷ"
B = rf"(?<![{L}])"
E = rf"(?![{L}])"

# =====================================================================================
# 1. Agreement machinery
# =====================================================================================
AGR = []          # (template, ending-set)
_AGR_IDX = {}


def agr(template, kind="m"):
    """Register an agreeing word; template has '{}' for the ending."""
    key = (template, kind)
    if key not in _AGR_IDX:
        _AGR_IDX[key] = len(AGR)
        AGR.append(key)
    return f"⟨{_AGR_IDX[key]}⟩"


ENDS = {"m": {"msd": "ा", "mso": "े", "mp": "े", "f": "ी"},
        "full": {"msd": "आ", "mso": "ए", "mp": "ए", "f": "ई"}}


def tag(g, n, c=1):
    return f"⟦{g}{n}{c}⟧"


K = agr("क{}")            # genitive particle का/के/की
HUA = agr("हु{}", "full")  # हुआ/हुए/हुई

# =====================================================================================
# 2. Triad items
# =====================================================================================
ITEM_T = {   # key: (template, kind, short)
    "d": ("सत्य-दर्शन से छोड़े जाने वाले मूलों वाल{}", "m", False),
    "b": ("मानसिक अभ्यास से छोड़े जाने वाले मूलों वाल{}", "m", False),
    "n": ("न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़े जाने वाले मूलों वाल{}", "m", False),
    "a": ("संचय की ओर ले जाने वाल{}", "m", False),
    "p": ("संचय घटाने की ओर ले जाने वाल{}", "m", False),
    "nn": ("न संचय की ओर, न संचय घटाने की ओर ले जाने वाल{}", "m", False),
    "s": ("सीखने के चरण क{}", "m", False),
    "as": ("सीखना पूरा होने के चरण क{}", "m", False),
    "ns": ("न सीखने के चरण क{0}, न सीखना पूरा होने के चरण क{0}", "m", False),
    "pa": ("सीमित", "inv", True),
    "ma": ("उन्नत", "inv", True),
    "ap": ("अपरिमित", "inv", True),
    "pr": ("सीमित विषय वाल{}", "m", False),
    "mr": ("उन्नत विषय वाल{}", "m", False),
    "ar": ("अपरिमित विषय वाल{}", "m", False),
}
# Pāli stems per file: (stem, declension 'a' or 'i', key)
STEMS = {
    "2-04": [("nevadassanena nabhāvanāya pahātabbahetuk", "a", "n"),
             ("dassanena pahātabbahetuk", "a", "d"), ("bhāvanāya pahātabbahetuk", "a", "b")],
    "2-05": [("nevācayagāmināpacayagām", "i", "nn"), ("nevācayagāmīnāpacayagām", "i", "nn"),
             ("apacayagām", "i", "p"), ("ācayagām", "i", "a")],
    "2-06": [("nevasekkhanāsekkh", "a", "ns"), ("asekkh", "a", "as"), ("sekkh", "a", "s")],
    "2-07": [("paritt", "a", "pa"), ("mahaggat", "a", "ma"), ("appamāṇ", "a", "ap")],
    "2-08": [("parittārammaṇ", "a", "pr"), ("mahaggatārammaṇ", "a", "mr"), ("appamāṇārammaṇ", "a", "ar"),
             ("paritt", "a", "pa"), ("mahaggat", "a", "ma"), ("appamāṇ", "a", "ap")],
}
TIKA_NAME = {"2-04": "सत्य-दर्शन से छोड़े जाने वाले मूलों", "2-05": "संचय की ओर ले जाने",
             "2-06": "सीखने के चरण", "2-07": "सीमित", "2-08": "सीमित विषय"}
TIKA_PALI = {"2-04": "dassanenapahātabbahetukattikaṃ", "2-05": "ācayagāmittikaṃ", "2-06": "sekkhattikaṃ",
             "2-07": "parittattikaṃ", "2-08": "parittārammaṇattikaṃ"}
END = {"a": {"acc": "aṃ", "nom": "o", "dat": "assa", "ca": "añca",
             "adj": "aṃ|o|ā|e|ānaṃ|āya|assa|añca"},
       "i": {"acc": "iṃ", "nom": "ī", "dat": "issa", "ca": "iñca",
             "adj": "iṃ|ī|īnaṃ|iyā|issa|iñca|i"}}


def item_f(key, form="f"):
    """Fixed form of an item adjective: 'f' feminine, 'msd', 'mso', 'mp'."""
    t, kind, _ = ITEM_T[key]
    if kind == "inv":
        return t
    return t.format(ENDS[kind][form])


def item_agr(key):
    t, kind, _ = ITEM_T[key]
    if kind == "inv":
        return t
    return agr(t, kind)


# =====================================================================================
# 3. Fixed vocabulary
# =====================================================================================
COND = S.COND_KEYS
COND_RX = "|".join(sorted(COND, key=len, reverse=True))
NAME, ABL, NABL, INS, NNAME = S.NAME, S.ABL, S.NABL, S.INS, S.NNAME
V = "⟨V⟩"
PR = "⟨PR⟩"
J = "⟨J⟩"

KH = "समूह"
KH_O = "समूहों"
CSR, CSR_OBL, KTR, KTR_OBL, UPR = S.CSR, S.CSR_OBL, S.KTR, S.KTR_OBL, S.UPR
VS = agr("संशय के साथ होने वाल{}")      # vicikicchāsahagata
US = agr("बेचैनी के साथ होने वाल{}")    # uddhaccasahagata
P5 = agr("पाँच प्रकार की चेतना के साथ होने वाल{}")   # pañcaviññāṇasahagata
PURIMA = "पहले-पहले " + K
PACCHIMA = "बाद-बाद " + K

ARUPA = {"ākāsānañcāyatan": "अनंत आकाश", "viññāṇañcāyatan": "अनंत चेतना",
         "ākiñcaññāyatan": "कुछ भी न होने", "nevasaññānāsaññāyatan": "न पहचान न अ-पहचान"}
NANA = {"iddhividhañāṇ": "अलौकिक शक्तियों", "cetopariyañāṇ": "दूसरों के मन को जानने",
        "pubbenivāsānussatiñāṇ": "पूर्व जन्मों के अनुस्मरण",
        "yathākammūpagañāṇ": "प्राणियों के अपने कर्मों के अनुसार जाने",
        "anāgataṃsañāṇ": "भविष्य को जानने"}
NANA_RX = "|".join(NANA)
SENSE = {"cakkh": "आँख", "sot": "कान", "ghān": "नाक", "jivh": "जीभ", "kāy": "शरीर"}
AYAT = {"cakkhāyatanaṃ": "आँख", "sotāyatanaṃ": "कान", "ghānāyatanaṃ": "नाक", "jivhāyatanaṃ": "जीभ",
        "kāyāyatanaṃ": "शरीर", "rūpāyatanaṃ": "दृश्य रूप", "saddāyatanaṃ": "ध्वनि",
        "gandhāyatanaṃ": "गंध", "rasāyatanaṃ": "स्वाद", "phoṭṭhabbāyatanaṃ": "स्पर्श"}
VINN = {"cakkhuviññāṇ": "आँख", "sotaviññāṇ": "कान", "ghānaviññāṇ": "नाक", "jivhāviññāṇ": "जीभ",
        "kāyaviññāṇ": "शरीर"}

NUMW = {"ekaṃ": "एक", "dve": "दो", "tīṇi": "तीन", "cattāri": "चार", "pañca": "पाँच", "cha": "छह",
        "satta": "सात", "aṭṭha": "आठ", "nava": "नौ", "dasa": "दस", "ekādasa": "ग्यारह",
        "dvādasa": "बारह", "terasa": "तेरह", "cuddasa": "चौदह", "pannarasa": "पंद्रह",
        "sattarasa": "सत्रह", "ekavīsa": "इक्कीस", "tīṇeva": "तीन ही"}

# =====================================================================================
# 4. Headings and whole-line formulas
# =====================================================================================
HEAD = {
    "paṭiccavāro": S.VARA["paṭicca"], "sahajātavāro": S.VARA["sahajāta"], "paccayavāro": S.VARA["paccaya"],
    "nissayavāro": S.VARA["nissaya"], "saṃsaṭṭhavāro": S.VARA["saṃsaṭṭha"],
    "sampayuttavāro": S.VARA["sampayutta"], "pañhāvāro": S.VARA["pañhā"], "vibhaṅgavāro": S.VARA["vibhaṅga"],
    "saṅkhyāvāro": S.VARA["saṅkhyā"], "suddhaṃ": S.SUDDHA,
    "paccayānulomaṃ": S.PACCAYANULOMA, "paccayapaccanīyaṃ": S.PACCAYAPACCANIYA,
    "paccayānulomapaccanīyaṃ": S.PACCAYANULOMAPACCANIYA, "paccayapaccanīyānulomaṃ": S.PACCAYAPACCANIYANULOMA,
    "hetudukaṃ": S.DUKANI("hetu"), "nahetudukaṃ": S.DUKANI("hetu", neg=True),
    "anantara-samanantarapaccayā": f"{NAME('anantara')} और {NAME('samanantara')}",
    "napacchājāta-naāsevanapaccayā": f"{NNAME('pacchājāta')} और {NNAME('āsevana')}",
    "paccanīyuddhāro": "नकारात्मक क्रम के लिए चयन",
    "2-6. sahajāta-paccaya-nissaya-saṃsaṭṭha-sampayuttavāro":
        "2-6. सह-उत्पत्ति, कारण, आश्रय, घुले-मिले होने और जुड़ाव के खंड",
}
CLOSE = {
    "anulomaṃ.": S.ANULOMA + "।", "paccanīyaṃ.": S.PACCANIYA + "।",
    "anulomapaccanīyaṃ.": S.ANULOMAPACCANIYA + "।", "paccanīyānulomaṃ.": S.PACCANIYANULOMA + "।",
    "paṭiccavāro.": S.VARA["paṭicca"] + "।", "paccayavāro.": S.VARA["paccaya"] + "।",
    "saṃsaṭṭhavāro.": S.VARA["saṃsaṭṭha"] + "।", "pañhāvāro.": S.VARA["pañhā"] + "।",
}


def heading(text, fid):
    t = text.strip().strip("*").strip().lower()
    if t == TIKA_PALI[fid]:
        return S.TIKA(TIKA_NAME[fid])
    if t in HEAD:
        return HEAD[t]
    m = re.fullmatch(rf"(na|no)?({COND_RX})paccay(o|ādi)", t)
    if m:
        base = NNAME(m.group(2)) if m.group(1) else NAME(m.group(2))
        return base + (" आदि" if m.group(3) == "ādi" else "")
    raise ValueError("heading? " + text)


# =====================================================================================
# 5. Parenthetical notes (lower-case Pāli inside the brackets -> Hindi inside the brackets)
# =====================================================================================
SAD = S.SADISA
DASS_T = "सत्य-दर्शन वाले तीन के वर्गीकरण"     # dassanattika
KUS_T = "हितकर वाले तीन के वर्गीकरण"            # kusalattika
PAREN = {
    "anantarasadisaṃ": SAD("anantara"),
    "anantarasadisaṃ, aṭṭha pañhā": f"{SAD('anantara')}, आठ प्रश्न",
    "asekkhamūlake tīṇi": f"{item_f('as', 'mso')} पद से शुरू होने वाली शृंखला में तीन",
    "avasesā cha pañhā hetupaccayasadisā satta kātabbā":
        f"बाकी छह प्रश्न {SAD('hetu')} हैं, सात बनाने चाहिए",
    "cakkaṃ kātabbaṃ": "चक्र बनाना चाहिए",
    "cakkaṃ kātabbaṃ kusalattikasadisaṃ": f"{KUS_T} के समान चक्र बनाना चाहिए",
    "cittasamuṭṭhānampi kaṭattārūpampi upādārūpampi natthi":
        f"{CSR} भी, {KTR} भी, {UPR} भी नहीं है",
    "dassanattikasadisaṃ": f"{DASS_T} के समान",
    "dassanattikasadisaṃ, dasa pañhā": f"{DASS_T} के समान, दस प्रश्न",
    "dassanena sadisaṃ": "सत्य-दर्शन वाले पद के समान",
    "dassanena sadisaṃ gamanaṃ": "सत्य-दर्शन वाले पद के समान क्रम",
    "dassanena sadisaṃ vibhajitabbaṃ.": "सत्य-दर्शन वाले पद के समान विभाजन करना चाहिए।",
    "dassanena sadisā": "सत्य-दर्शन वाले पद के समान",
    "dve kātabbā": "दो बनाने चाहिए",
    "dve kātabbā dassitanayena": "दिखाई गई विधि से दो बनाने चाहिए",
    "dve pañhā kātabbā, sekkhasadisā": f"दो प्रश्न बनाने चाहिए, {item_f('s', 'mso')} पद के समान",
    "ekaṃ, paripuṇṇaṃ, sekkhañca, nevasekkhanāsekkhañca, ghaṭanā paripuṇṇā, dvepi kātabbā. nava":
        f"एक, पूरा, {item_f('s', 'f')} और {item_f('ns', 'f')} परिघटनाओं का संयोजन पूरा, "
        "दोनों भी बनाने चाहिए। नौ",
    "ekā pañhā sabbe mahābhūtā kātabbā": "एक प्रश्न, सभी महाभूत शामिल करने चाहिए",
    "evaṃ gaṇatabbaṃ": "इस प्रकार गिनना चाहिए",
    "evaṃ gaṇetabbaṃ": "इस प्रकार गिनना चाहिए",
    "hetusadisā": SAD("hetu"),
    "hetusadisā, adhipatiyā moho natthi": f"{SAD('hetu')}, {S.LOC('adhipati')} मोह नहीं है",
    "idha sahajātaṃ, purejātaṃ, missagataṃ atthi, pāḷiyaṃ kātabbaṃ. gaṇanāya upadhāretvā gaṇetabbaṃ.":
        "यहाँ सह-उत्पत्ति, पूर्व-उत्पत्ति और मिश्रित रूप है, इसे पाठ में बनाना चाहिए। "
        "गणना में ध्यान से देखकर गिनना चाहिए।",
    'idhāpi "sahajātaṃ, purejātaṃ" yaṃ missakapañhā atthi':
        "यहाँ भी “सह-उत्पत्ति, पूर्व-उत्पत्ति” वाला जो मिश्रित प्रश्न है",
    'idhāpi "sahajātaṃ, purejātaṃ" yaṃ missakapañhā atthi, pāḷiyaṃ kātabbaṃ':
        "यहाँ भी “सह-उत्पत्ति, पूर्व-उत्पत्ति” वाला जो मिश्रित प्रश्न है, उसे पाठ में बनाना चाहिए",
    "idhāpi ghaṭanā hetusadisā": f"यहाँ भी संयोजन {SAD('hetu')} है",
    "idhāpi sahajātaṃ, purejātaṃ atthi. ye te pañhā na likhitā, te pāḷiyaṃ gaṇentānaṃ byañjanena na "
    "samenti. te pāḷiyaṃ na likhitā gaṇanā pākaṭā honti. yadi saṃsayo uppajjati, anulome atthipaccaye "
    "pekkhitabbaṃ.":
        "यहाँ भी सह-उत्पत्ति और पूर्व-उत्पत्ति है। जो प्रश्न लिखे नहीं गए हैं, वे पाठ में गिनने वालों के "
        "लिए शब्दों से मेल नहीं खाते। वे पाठ में लिखे नहीं गए हैं, पर उनकी गणना स्पष्ट है। यदि संशय "
        f"उत्पन्न हो, तो {S.ANULOMA} में {NAME('atthi')} में देखना चाहिए।",
    "idhāpi ārammaṇapaccayā upanissayapaccayā atthi, pāḷiyaṃ natthi. gaṇentena upadhāretvā gaṇetabbaṃ.":
        f"यहाँ भी {NAME('ārammaṇa')} और {NAME('upanissaya')} हैं, पर पाठ में नहीं हैं। "
        "गिनने वाले को ध्यान से देखकर गिनना चाहिए।",
    "idhāpi ārammaṇaupanissayā atthi": f"यहाँ भी {NAME('ārammaṇa')} और {NAME('upanissaya')} हैं",
    "ime sahetukā kātabbā": "इन्हें मूल वाली परिघटनाओं के साथ बनाना चाहिए",
    "imepi dve kātabbā": "ये दो भी बनाने चाहिए",
    "kusalattikasadisā": f"{KUS_T} के समान",
    "kusalattikasadisā satta pañhā": f"{KUS_T} के समान सात प्रश्न",
    "mahaggatārammaṇe paṭisandhi natthi": f"{item_f('mr', 'mso')} पद में पुनर्जन्म नहीं है",
    "mahābhūtā kātabbā": "महाभूत शामिल करने चाहिए",
    "napacchājātapaccayañca naāsevanapaccayañca naadhipatisadisaṃ":
        f"{NNAME('pacchājāta')} और {NNAME('āsevana')} {SAD('adhipati', neg=True)} हैं",
    "naārammaṇapaccayasadisaṃ": SAD("ārammaṇa", neg=True),
    "nevasekkhanāsekkhamūlake tīṇi": f"{item_f('ns', 'mso')} पद से शुरू होने वाली शृंखला में तीन",
    "nissayavāro paccayavārasadiso": "आश्रय का खंड कारण के खंड के समान है",
    "nissayavāro paccayavārasadiso.": "आश्रय का खंड कारण के खंड के समान है।",
    "paripuṇṇaṃ": "पूरा",
    "paripuṇṇaṃ kātabbaṃ, paṭisandhikkhaṇe natthi": "पूरा बनाना चाहिए, पुनर्जन्म के क्षण में नहीं है",
    "paripuṇṇaṃ, ekaṃ": "पूरा, एक",
    "paripuṇṇaṃ, paṭisandhi natthi": "पूरा, पुनर्जन्म नहीं है",
    "paripuṇṇaṃ, paṭisandhipi mahābhūtāpi sabbe": "पूरा, पुनर्जन्म भी और सभी महाभूत भी",
    "paripuṇṇaṃ, vipākoti niddisitabbaṃ cittasamuṭṭhānaṃ rūpaṃ vipākoti na kātabbaṃ":
        f"पूरा, “कर्म-फल” कहकर निर्देश करना चाहिए, {CSR} को “कर्म-फल” नहीं बनाना चाहिए",
    "pavattimeva": "केवल जीवन-प्रक्रिया",
    "pavattipaṭisandhi": "जीवन-प्रक्रिया और पुनर्जन्म",
    "pavattipaṭisandhi kātabbā": "जीवन-प्रक्रिया और पुनर्जन्म बनाने चाहिए",
    "paṭiccavārapaccanīye navippayuttasadisaṃ, ninnānaṃ. ekādasa":
        f"निर्भरता के खंड के नकारात्मक क्रम में {SAD('vippayutta', neg=True)}, बिना अंतर के। ग्यारह",
    "paṭiccavārasadisaṃ": "निर्भरता के खंड के समान",
    "paṭiccavārasadisaṃ, tīṇi": "निर्भरता के खंड के समान, तीन",
    "paṭiccavārasadisaṃ. pañca": "निर्भरता के खंड के समान। पाँच",
    "paṭiccavārasadisā": "निर्भरता के खंड के समान",
    "paṭiccavārasadisā dvādasa pañhā": "निर्भरता के खंड के समान बारह प्रश्न",
    "paṭiccavārasadisā kātabbā": "निर्भरता के खंड के समान बनाने चाहिए",
    "paṭiccavārasadisā, satta pañhā": "निर्भरता के खंड के समान, सात प्रश्न",
    "paṭiccavāre aññamaññasadisaṃ, tīṇi. nissayapaccaye kusalattike nissayapaccayasadisaṃ, terasa pañhā":
        f"निर्भरता के खंड में {SAD('aññamañña')}, तीन। {NAME('nissaya')} में {KUS_T} के "
        f"{SAD('nissaya')}, तेरह प्रश्न",
    "paṭiccavāre paccanīyasadisaṃ, terasa pañhā. ninnānaṃ":
        "निर्भरता के खंड में नकारात्मक क्रम के समान, तेरह प्रश्न। बिना अंतर के",
    "paṭiccavāre sahajātasadisaṃ, nava pañhā": f"निर्भरता के खंड में {SAD('sahajāta')}, नौ प्रश्न",
    "paṭiccavāre sampayuttavārasadisaṃ": "निर्भरता के खंड में जुड़ाव के खंड के समान",
    "paṭiccavāre ārammaṇasadisā": f"निर्भरता के खंड में {SAD('ārammaṇa')}",
    "paṭisandhi natthi": "पुनर्जन्म नहीं है",
    "paṭisandhi natthi, sattarasa pañhā paripuṇṇā": "पुनर्जन्म नहीं है, सत्रह प्रश्न पूरे",
    "paṭisandhikkhaṇe tīṇipi kātabbā": "पुनर्जन्म के क्षण में तीनों भी बनाने चाहिए",
    "paṭisandhivipākopi natthi": "पुनर्जन्म वाला कर्म-फल भी नहीं है",
    "sabbe mahābhūtā kātabbā": "सभी महाभूत शामिल करने चाहिए",
    "sabbe mahābhūtā vitthāretabbā, arūpe parittamūlake tisso pañhā":
        f"सभी महाभूतों का विस्तार करना चाहिए, अभौतिक लोक में {item_f('pa')} पद से शुरू होने वाली "
        "शृंखला में तीन प्रश्न",
    "sabbepi mahābhūtā kātabbā": "सभी महाभूत भी शामिल करने चाहिए",
    "sahajātapaccaye paṭiccavāre sahajātavārasadisā nava pañhā. aññamaññapaccaye paṭiccavāre "
    "aññamaññasadisaṃ tīṇi. nissayapaccaye paccayavāre nissayavārasadisaṃ. cattāripi hi visuṃ ghaṭanā "
    "natthi. terasa pañhā.":
        f"{NAME('sahajāta')} में निर्भरता के खंड में सह-उत्पत्ति के खंड के समान नौ प्रश्न। "
        f"{NAME('aññamañña')} में निर्भरता के खंड में {SAD('aññamañña')} तीन। "
        f"{NAME('nissaya')} में कारण के खंड में आश्रय के खंड के समान। चारों का भी अलग संयोजन नहीं है। "
        "तेरह प्रश्न।",
    "sahajātasadisaṃ": SAD("sahajāta"),
    "sahajātavāro paṭiccavārasadiso.": "सह-उत्पत्ति का खंड निर्भरता के खंड के समान है।",
    "sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi paṭiccavārasadiso":
        "सह-उत्पत्ति का खंड भी, कारण का खंड भी, आश्रय का खंड भी, घुले-मिले होने का खंड भी और "
        "जुड़ाव का खंड भी निर्भरता के खंड के समान है",
    "sahajātavāropi paṭiccavārasadiso.": "सह-उत्पत्ति का खंड भी निर्भरता के खंड के समान है।",
    "samanantarapaccayaṃ anantarapaccayasadisaṃ.": f"{NAME('samanantara')} {SAD('anantara')} है।",
    "sampayuttavāro saṃsaṭṭhavārasadiso": "जुड़ाव का खंड घुले-मिले होने के खंड के समान है",
    "sampayuttavāro saṃsaṭṭhavārasadiso.": "जुड़ाव का खंड घुले-मिले होने के खंड के समान है।",
    "satta": "सात",
    "saṃkhittaṃ": "संक्षिप्त",
    "saṃkhittaṃ, sabbe ghaṭanā kātabbā": "संक्षिप्त, सभी संयोजन बनाने चाहिए",
    "saṃkhittaṃ. dassanena sadisā": "संक्षिप्त। सत्य-दर्शन वाले पद के समान",
    "saṃkhittaṃ. hetusadisaṃ kātabbaṃ": f"संक्षिप्त। {SAD('hetu')} बनाना चाहिए",
    "saṃkhittaṃ. paccayavāre nissayavārasadisaṃ. visuṃ ghaṭanā natthi":
        "संक्षिप्त। कारण के खंड में आश्रय के खंड के समान। अलग संयोजन नहीं है",
    "saṃkhittaṃ. paṭiccavārasadisaṃ": "संक्षिप्त। निर्भरता के खंड के समान",
    "saṃkhittaṃ. paṭiccavāre aññamaññasadisaṃ": f"संक्षिप्त। निर्भरता के खंड में {SAD('aññamañña')}",
    "saṃkhittaṃ. paṭiccavāre sahajātasadisaṃ": f"संक्षिप्त। निर्भरता के खंड में {SAD('sahajāta')}",
    'saṃkhittaṃ. tisso pañhā, dassanena nayena vibhajitabbā, "uddhacca"nti niyāmetabbaṃ':
        "संक्षिप्त। तीन प्रश्न, सत्य-दर्शन वाले पद की विधि से उनका विभाजन करना चाहिए, "
        "“बेचैनी” ऐसा निश्चित करना चाहिए",
    "sekkhaghaṭanesu tīṇi": f"{item_f('s', 'mso')} पद के संयोजनों में तीन",
    "sekkhamūlake tīṇi": f"{item_f('s', 'mso')} पद से शुरू होने वाली शृंखला में तीन",
    "sekkhasadisaṃ": f"{item_f('s', 'mso')} पद के समान",
    "sekkhasadisā": f"{item_f('s', 'mso')} पद के समान",
    "terasa pañhā": "तेरह प्रश्न",
    "tisso pañhā kātabbā": "तीन प्रश्न बनाने चाहिए",
    "tisso pañhā, pavattipaṭisandhi kātabbā": "तीन प्रश्न, जीवन-प्रक्रिया और पुनर्जन्म बनाने चाहिए",
    "tīṇi": "तीन",
    "tīṇi, paripuṇṇaṃ": "तीन, पूरा",
    "vipākopi paṭisandhipi natthi": "कर्म-फल भी और पुनर्जन्म भी नहीं है",
    "vitthāretabbaṃ": "विस्तार करना चाहिए",
    "vitthāretabbaṃ dassanattikasadisaṃ": f"{DASS_T} के समान विस्तार करना चाहिए",
    "yathā dassanattikaṃ": f"जैसे {DASS_T} में",
    "ācayagāminayena kātabbaṃ": f"{item_f('a', 'mso')} पद की विधि से बनाना चाहिए",
    "āhārasadisaṃ. moho kātabbo": f"{SAD('āhāra')}। मोह शामिल करना चाहिए",
    "ārammaṇasadisaṃ": SAD("ārammaṇa"),
    "āsevanamūlake vuṭṭhānassapi āvajjanāyapi pahātabbaṃ, sattarasa pañhā paripuṇṇā, anantarasadisā":
        f"{S.MULAKA('āsevana')} में बाहर आने वाले मन को भी और मन को विषय की ओर मोड़ने को भी छोड़ देना "
        f"चाहिए, सत्रह प्रश्न पूरे, {SAD('anantara')}",
}

# =====================================================================================
# 6. Phrase rules (applied in order on the lower-cased Pāli line)
# =====================================================================================
RULES = []
PRE = []      # applied before the item rules (persons, purimā …)


def R(pat, rep):
    RULES.append((re.compile(pat), rep))


def P(pat, rep):
    PRE.append((re.compile(pat), rep))


def build_item_rules(fid):
    """Rules for the triad items of one file (frames first, then adjectives)."""
    out = []
    stems = STEMS[fid]

    def alt(kind_key):
        parts = []
        for st, dec, key in stems:
            parts.append((re.escape(st) + END[dec][kind_key], key))
        return parts

    def frame_alt(kind_key):
        return "|".join(f"(?P<{kind_key}{i}>{p})" for i, (p, _) in enumerate(alt(kind_key)))

    def which(m, kind_key, offset=0):
        for i, (_, key) in enumerate(alt(kind_key)):
            if m.groupdict().get(f"{kind_key}{i}"):
                return key
        raise KeyError

    one = {k: "|".join(p for p, _ in alt(k)) for k in ("acc", "nom", "dat", "ca")}
    keymap = {k: [(re.compile(B + p + E), key) for p, key in alt(k)] for k in ("acc", "nom", "dat", "ca")}

    def key_of(text, k):
        for rx, key in keymap[k]:
            if rx.fullmatch(text):
                return key
        raise KeyError(text)

    # pairs first
    out.append((re.compile(B + rf"({one['ca']}) ({one['ca']}) dhammaṃ" + E),
                lambda m: f"{item_f(key_of(m.group(1), 'ca'))} परिघटना और "
                          f"{item_f(key_of(m.group(2), 'ca'))} परिघटना{tag(2, 1)}"))
    out.append((re.compile(B + rf"({one['nom']}) ca ({one['nom']}) ca dhammā" + E),
                lambda m: f"{item_f(key_of(m.group(1), 'nom'))} और "
                          f"{item_f(key_of(m.group(2), 'nom'))} परिघटनाएँ{tag(2, 2)}"))
    out.append((re.compile(B + rf"({one['dat']}) ca ({one['dat']}) ca dhammassa" + E),
                lambda m: f"{item_f(key_of(m.group(1), 'dat'))} परिघटना और "
                          f"{item_f(key_of(m.group(2), 'dat'))} परिघटना{tag(2, 1, 2)} के लिए"))
    out.append((re.compile(B + rf"({one['acc']}) dhammaṃ" + E),
                lambda m: f"{item_f(key_of(m.group(1), 'acc'))} परिघटना{tag(2, 1)}"))
    out.append((re.compile(B + rf"({one['nom']}) dhammo" + E),
                lambda m: f"{item_f(key_of(m.group(1), 'nom'))} परिघटना{tag(2, 1)}"))
    out.append((re.compile(B + rf"({one['dat']}) dhammassa" + E),
                lambda m: f"{item_f(key_of(m.group(1), 'dat'))} परिघटना{tag(2, 1, 2)} के लिए"))
    # truncated frame words
    if fid == "2-04":
        out.append((re.compile(B + r"nevadassanena nabhāvanāya…"), lambda m: "न सत्य-दर्शन से, न मानसिक अभ्यास से…"))
        out.append((re.compile(B + r"bhāvanāya…"), lambda m: "मानसिक अभ्यास से…"))
        out.append((re.compile(B + r"bhāvanāya pahātabbahetukañca…"),
                    lambda m: f"{item_f('b')} परिघटना और…"))
    # compounds with citta / adhipati / mūlaka
    for st, dec, key in stems:
        stem_c = re.escape(st) + ("i" if dec == "i" else "a")
        out.append((re.compile(B + stem_c + r"cittasamaṅgissa cittaṃ jān(āti|anti)" + E),
                    lambda m, key=key: f"{item_f(key, 'mso')} मन से युक्त व्यक्ति के मन को "
                                       f"{'जानता है' if m.group(1) == 'āti' else 'जानते हैं'}"))
        out.append((re.compile(B + re.escape(st) + ("ā" if dec == "a" else "ā") + r"dhipati" + E),
                    lambda m, key=key: f"{item_f(key, 'f')} प्रधानता{tag(2, 1)}"))
    # 2-08 double compounds: parittārammaṇaparittacittasamaṅgissa ...
    if fid == "2-08":
        a_items = [("parittārammaṇa", "pr"), ("mahaggatārammaṇa", "mr"), ("appamāṇārammaṇa", "ar")]
        b_items = [("paritta", "pa"), ("mahaggata", "ma"), ("appamāṇa", "ap")]
        for pa, ka in a_items:
            for pb, kb in b_items:
                out.append((re.compile(B + pa + pb + r"cittasamaṅgissa cittaṃ jān(āti|anti)" + E),
                            lambda m, ka=ka, kb=kb: f"{item_f(ka, 'mso')} {item_f(kb, 'mso')} मन से युक्त "
                                                    f"व्यक्ति के मन को "
                                                    f"{'जानता है' if m.group(1) == 'āti' else 'जानते हैं'}"))
    # adjective + ekaṃ khandhaṃ (short items after एक, as in the sample)
    adj_alt = "|".join(re.escape(st) + f"(?:{END[dec]['adj']})" for st, dec, _ in stems)

    def key_any(text):
        for st, dec, key in stems:
            if re.fullmatch(re.escape(st) + f"(?:{END[dec]['adj']})", text):
                return key
        raise KeyError(text)

    out.append((re.compile(B + rf"({adj_alt})" + E), lambda m: item_agr(key_any(m.group(1)))))
    # pañhāvāra frame: comma after the subject ("X dhammo, Y dhammassa …")
    frame = re.compile(B + rf"^((?:{one['nom']}) dhammo|(?:{one['nom']}) ca (?:{one['nom']}) ca dhammā)"
                       rf"(?= (?:{one['dat']}) (?:ca (?:{one['dat']}) ca )?dhammassa)")
    return out, frame


def init_rules():
    # ---------- persons (sekkha as noun) — before item adjectives
    P(B + r"sekkhā vā puthujjanā vā" + E, S.SEKKHA_VA_PUTHUJJANA + tag(1, 2))
    P(B + r"sekkhā(?= (?:pahīne|maggā|phalaṃ|gotrabhuṃ|maggaṃ|appamāṇārammaṇaṃ|phalasamāpattiyā))",
      S.SEKKHA + tag(1, 2))
    P(B + r"sekkhānaṃ(?= anulomaṃ)", "सीखने के चरण वालों की")
    P(B + r"sekkhānaṃ(?= atthappaṭisambhidāya)", "सीखने के चरण वालों के")
    P(B + r"purim(ā|o) purim\1" + E, PURIMA)
    P(B + r"pacchim(ānaṃ|assa) pacchim\1" + E, PACCHIMA)
    P(B + r"ariyānaṃ" + E, "आर्यों के")
    P(B + r"ariyā" + E, "आर्य" + tag(1, 2))
    P(B + r"arahato" + E, "अर्हत् की")
    P(B + r"arahā" + E, S.ARAHA + tag(1, 1))
    R(B + r"atthappaṭisambhidāya" + E, "अर्थ के विश्लेषणात्मक ज्ञान के लिए")
    R(B + r"vatthussa ca" + E, "और आधार" + tag(1, 1, 2) + " के लिए")
    for p, h in NANA.items():
        R(B + p + r"assa parikammaṃ" + E, f"{h} के ज्ञान की प्रारंभिक तैयारी{tag(2, 1)}")
    # ---------- main-frame comma (pañhāvāra) is inserted in translate()
    # ---------- arūpa spheres and their minds
    for p, h in ARUPA.items():
        R(B + p + r"akusalaṃ" + E, f"{h} के क्षेत्र का हितकर मन{tag(1, 1)}")
        R(B + p + r"akusalassa" + E, f"{h} के क्षेत्र के हितकर मन{tag(1, 1, 2)} के लिए")
        R(B + p + r"akiriyaṃ" + E, f"{h} के क्षेत्र का केवल क्रिया रूपी मन{tag(1, 1)}")
        R(B + p + r"akiriyassa" + E, f"{h} के क्षेत्र के केवल क्रिया रूपी मन{tag(1, 1, 2)} के लिए")
        R(B + p + r"avipākassa ca kiriyassa ca" + E,
          f"{h} के क्षेत्र के कर्म के फल रूपी मन के लिए और केवल क्रिया रूपी मन{tag(1, 1, 2)} के लिए")
        R(B + p + r"apaccavekkhaṇaṃ" + E, f"{h} {K} क्षेत्र पर {HUA} पुनर्विचार{tag(1, 1)}")
        R(B + p + r"assa parikammaṃ" + E, f"{h} के क्षेत्र की प्रारंभिक तैयारी{tag(2, 1)}")
        R(B + p + r"aṃ" + E, f"{h} {K} क्षेत्र{tag(1, 1)}")
        R(B + p + r"assa" + E, f"{h} {K} क्षेत्र{tag(1, 1, 2)} के लिए")
    # ---------- ñāṇas
    nlist = rf"(?:{NANA_RX})assa"
    R(B + rf"({nlist}(?:,? {nlist})*)(,? āvajjanāya)?( mohassa ca)?" + E, _nana_list)
    for p, h in NANA.items():
        R(B + p + r"apaccavekkhaṇaṃ" + E, f"{h} के ज्ञान पर {HUA} पुनर्विचार{tag(1, 1)}")
        R(B + p + r"assa parikammaṃ" + E, f"{h} के ज्ञान की प्रारंभिक तैयारी{tag(2, 1)}")
        R(B + p + r"aṃ" + E, f"{h} {K} ज्ञान{tag(1, 1)}")
        R(B + p + r"ena" + E, f"{h} {K} ज्ञान{tag(1, 1, 2)} से")
    # ---------- other review objects (… paccavekkhaṇaṃ)
    for p, h in {"paṭhamajjhāna": "पहले ध्यान", "dibbacakkhu": "दिव्य आँख",
                 "dibbasotadhātu": "दिव्य कान के तत्व", "magga": "मार्ग", "phala": "फल",
                 "nibbāna": "निर्वाण"}.items():
        R(B + p + r"paccavekkhaṇaṃ" + E, f"{h} पर {HUA} पुनर्विचार{tag(1, 1)}")
    # ---------- preparation (parikamma) and numbered jhānas / paths
    for p, h in {"paṭhamassa jhānassa": "पहले ध्यान", "dibbassa cakkhussa": "दिव्य आँख",
                 "paṭhamassa maggassa": "पहले मार्ग", "catutthassa maggassa": "चौथे मार्ग"}.items():
        R(B + p + r" parikammaṃ" + E, f"{h} की प्रारंभिक तैयारी{tag(2, 1)}")
    for p, h in {"paṭhamassa": "पहले", "dutiyassa": "दूसरे", "tatiyassa": "तीसरे", "catutthassa": "चौथे"}.items():
        R(B + p + r" (jhānassa|maggassa)" + E,
          lambda m, h=h: f"{h} {'ध्यान' if m.group(1) == 'jhānassa' else 'मार्ग'}{tag(1, 1, 2)} के लिए")
    for p, h in {"paṭhamaṃ jhānaṃ": "पहला ध्यान", "paṭhamo maggo": "पहला मार्ग",
                 "dutiyo maggo": "दूसरा मार्ग", "tatiyo maggo": "तीसरा मार्ग"}.items():
        R(B + p + E, h + tag(1, 1))
    R(B + r"tasseva" + E, "उसी के लिए")
    # ---------- review / insight sentences
    R(B + r"dānaṃ datvā sīlaṃ samādiyitvā uposathakammaṃ katvā" + E, S.DANA3)
    R(B + r"dānaṃ datvā" + E, "दान देकर")
    R(B + r"pubbe suciṇṇāni" + E, S.SUCINNA + tag(1, 2))
    R(B + r"pubbe samudāciṇṇe kilese jān(āti|anti)" + E,
      lambda m: "पहले बार-बार उठे मन के क्लेशों को " + ("जानता है" if m.group(1) == "āti" else "जानते हैं"))
    R(B + r"pahīne kilese" + E, "छोड़े जा चुके मन के क्लेशों" + tag(1, 2, 2))
    R(B + r"vikkhambhite kilese" + E, "दबाए जा चुके मन के क्लेशों" + tag(1, 2, 2))
    R(B + r"(jhānā|maggā) vuṭṭhahitvā" + E,
      lambda m: ("ध्यान" if m.group(1) == "jhānā" else "मार्ग") + " से उठकर")
    R(B + r"nirodhā vuṭṭhahantassa" + E, "समाप्ति की ध्यान-अवस्था से उठने वाले व्यक्ति में")
    R(B + r"taṃ garuṃ katvā paccavekkh(ati|anti)" + E,
      lambda m: "उसे महत्व देकर उस पर " + (S.REVIEW_SG if m.group(1) == "ati" else S.REVIEW_PL))
    R(B + r"garuṃ katvā paccavekkh(ati|anti)" + E,
      lambda m: f"को महत्व देकर {PR} पर " + (S.REVIEW_SG if m.group(1) == "ati" else S.REVIEW_PL))
    R(B + r"taṃ garuṃ katvā" + E, "उसे" + tag(1, 1, 2) + " महत्व देकर")
    R(B + r"garuṃ katvā" + E, "को महत्व देकर")
    R(B + r"taṃ ārabbha" + E, "उसे" + tag(1, 1, 2) + " विषय बनाकर")
    R(B + r"ārabbha" + E, "को विषय बनाकर")
    R(B + r"taṃ paccavekkhati" + E, "उस पर " + S.REVIEW_SG)
    R(B + r"paccavekkhati" + E, "पर " + S.REVIEW_SG)
    R(B + r"paccavekkhanti" + E, "पर " + S.REVIEW_PL)
    R(B + r"aniccato dukkhato anattato vipassati" + E, f"को {S.ANICCA3} {S.VIPASSATI}")
    R(B + r"aniccato dukkhato anattato vipassanti" + E, f"को {S.ANICCA3} {S.VIPASSANTI}")
    R(B + r"aniccato…pe… vip?passati" + E, f"को अनित्य… {S.VIPASSATI}")
    R(B + r"aniccato…pe… vipassanti" + E, f"को अनित्य… {S.VIPASSANTI}")
    R(B + r"aniccato…pe…", "को अनित्य…")
    R(B + r"aniccato…", "को अनित्य…")
    R(B + r"vip?passati" + E, S.VIPASSATI)
    R(B + r"vipassanti" + E, S.VIPASSANTI)
    # assādeti abhinandati: after a verb / gerund the object is a pronoun
    R(rf"(?<=अंतर्दृष्टि से देखता है)(,?) assādeti abhinandati" + E,
      lambda m: f"{m.group(1)} {PR}का रस लेता है, {PR}में आनंद लेता है")
    R(rf"(?<=अंतर्दृष्टि से देखते हैं)(,?) assādenti abhinandanti" + E,
      lambda m: f"{m.group(1)} {PR}का रस लेते हैं, {PR}में आनंद लेते हैं")
    R(rf"(?<=अंतर्दृष्टि से देखते हैं)(,?) assādenti…pe…",
      lambda m: f"{m.group(1)} {PR}का रस लेते हैं…")
    R(rf"(?<=महत्व देकर) assādeti abhinandati" + E, f" {PR}का रस लेता है, {PR}में आनंद लेता है")
    R(rf"(?<=महत्व देकर) assādeti…pe…", f" {PR}का रस लेता है…")
    R(rf"(?<=अंतर्दृष्टि से देखता है)(,?) assādeti…pe…", lambda m: f"{m.group(1)} {PR}का रस लेता है…")
    R(B + r"assādeti abhinandati" + E, f"का रस लेता है, {PR}में आनंद लेता है")
    R(B + r"assādenti abhinandanti" + E, f"का रस लेते हैं, {PR}में आनंद लेते हैं")
    R(B + r"cetopariyañāṇena…pe…", f"{S.CETOPARIYENA}…")
    R(B + r"kusale niruddhe vipāko tadārammaṇatā uppajjati" + E, f"हितकर के समाप्त होने पर {S.TADARAMMANA}")
    R(B + r"akusale niruddhe vipāko tadārammaṇatā uppajjati" + E, f"हानिकर के समाप्त होने पर {S.TADARAMMANA}")
    R(B + r"dibbena cakkhunā rūpaṃ pass(ati|anti)" + E,
      lambda m: "दिव्य आँख से दृश्य रूप " + ("देखता है" if m.group(1) == "ati" else "देखते हैं"))
    R(B + r"dibbāya sotadhātuyā saddaṃ suṇ(āti|anti)" + E,
      lambda m: "दिव्य कान के तत्व से ध्वनि " + ("सुनता है" if m.group(1) == "āti" else "सुनते हैं"))
    R(B + r"dibbaṃ cakkhuṃ" + E, "दिव्य आँख" + tag(2, 1))
    R(B + r"dibbaṃ sotadhātuṃ" + E, f"दिव्य कान {K} तत्व{tag(1, 1)}")
    # ---------- upanissaya vocabulary
    R(B + r"ārammaṇūpanissayo" + E, S.ARAMMANUPANISSAYA)
    R(B + r"anantarūpanissayo" + E, S.ANANTARUPANISSAYA)
    R(B + r"pakatūpanissayo" + E, S.PAKATUPANISSAYA)
    R(B + r"upanissāya" + E, "के प्रबल आश्रय से")
    R(B + r"pāṇaṃ hanati" + E, "प्राणी की हत्या करता है")
    R(B + r"saṅghaṃ bhindati" + E, "संघ में फूट डालता है")
    R(B + r"mānaṃ jappeti" + E, "अहंकार पालता है")
    R(B + r"diṭṭhiṃ gaṇhāti" + E, "दृष्टि अपनाता है")
    R(B + r"dānaṃ deti" + E, "दान देता है")
    R(B + r"sīlaṃ samādiyati" + E, "सदाचार ग्रहण करता है")
    R(B + r"uposathakammaṃ karoti" + E, "उपवास-व्रत का पालन करता है")
    R(B + r"attānaṃ ātāpeti paritāpeti pariyiṭṭhimūlakaṃ dukkhaṃ paccanubhoti" + E,
      "स्वयं को तपाता है, संतप्त करता है, खोज से उत्पन्न दुःख भोगता है")
    R(B + r"attānaṃ ātāpeti paritāpeti" + E, "स्वयं को तपाता है, संतप्त करता है")
    R(B + r"anuppannaṃ kusalasamāpattiṃ uppādenti, uppannaṃ samāpajjanti" + E,
      "जो उत्पन्न नहीं हुई, उस हितकर ध्यान-अवस्था को उत्पन्न करते हैं, जो उत्पन्न हो चुकी, उसमें प्रवेश करते हैं")
    R(B + r"anuppannaṃ samāpattiṃ uppādenti, uppannaṃ samāpajjanti" + E,
      "जो उत्पन्न नहीं हुई, उस ध्यान-अवस्था को उत्पन्न करते हैं, जो उत्पन्न हो चुकी, उसमें प्रवेश करते हैं")
    R(B + r"anuppannaṃ kiriyasamāpattiṃ uppādeti, uppannaṃ samāpajjati" + E,
      "जो उत्पन्न नहीं हुई, उस केवल क्रिया रूपी ध्यान-अवस्था को उत्पन्न करता है, जो उत्पन्न हो चुकी, "
      "उसमें प्रवेश करता है")
    R(B + r"anuppannaṃ kiriyasamāpattiṃ uppādeti" + E,
      "जो उत्पन्न नहीं हुई, उस केवल क्रिया रूपी ध्यान-अवस्था को उत्पन्न करता है")
    R(B + r"uppādeti" + E, "उत्पन्न करता है")
    R(B + r"uppādenti" + E, "उत्पन्न करते हैं")
    R(B + r"sakabhaṇḍe chandarāgo parabhaṇḍe chandarāgassa" + E,
      "अपनी वस्तुओं के प्रति चाह भरा राग" + tag(1, 1) + " पराई वस्तुओं के प्रति चाह भरे राग के लिए")
    R(B + r"sakapariggahe chandarāgo parapariggahe chandarāgassa" + E,
      "अपने परिग्रह के प्रति चाह भरा राग" + tag(1, 1) + " पराए परिग्रह के प्रति चाह भरे राग के लिए")
    R(B + r"kusalākusalaṃ kammaṃ vipākassa" + E, "हितकर और हानिकर कर्म" + tag(1, 1) + " कर्म-फल के लिए")
    R(B + r"pāṇātipāto pāṇātipātassa" + E, "जीवों की हत्या" + tag(2, 1) + " जीवों की हत्या के लिए")
    R(B + r"mātughātikammaṃ mātughātikammassa" + E,
      "माता की हत्या का कर्म" + tag(1, 1) + " माता की हत्या के कर्म के लिए")
    R(B + r"paṭibhāna(?:p)?paṭisambhidāya" + E, "सूझ-बूझ के विश्लेषणात्मक ज्ञान के लिए")
    R(B + r"ṭhānāṭhānakosallassa" + E, "संभव और असंभव को जानने की कुशलता के लिए")
    # ---------- anantara vocabulary
    R(B + r"anulomaṃ (gotrabhussa|vodānassa|phalasamāpattiyā)" + E,
      lambda m: "अनुरूपता" + tag(2, 1) + " " + {"gotrabhussa": S.GOTRABHU + " के लिए",
                                                "vodānassa": S.VODANA + " के लिए",
                                                "phalasamāpattiyā": "फल की ध्यान-अवस्था के लिए"}[m.group(1)])
    R(B + r"anulomaṃ (sekkhāya|asekkhāya) phalasamāpattiyā" + E,
      lambda m: "अनुरूपता" + tag(2, 1) + " " + item_f("s" if m.group(1) == "sekkhāya" else "as", "f")
      + " फल की ध्यान-अवस्था के लिए")
    R(B + r"anulomaṃ" + E, "अनुरूपता" + tag(2, 1))
    R(B + r"gotrabhu" + E, S.GOTRABHU + tag(1, 1))
    R(B + r"gotrabhuṃ" + E, S.GOTRABHU + tag(1, 1))
    R(B + r"gotrabhussa" + E, S.GOTRABHU + tag(1, 1, 2) + " के लिए")
    R(B + r"vodānaṃ" + E, S.VODANA + tag(2, 1))
    R(B + r"vodānassa" + E, S.VODANA + tag(2, 1, 2) + " के लिए")
    R(B + r"bhavaṅgaṃ" + E, f"जीवन-धारा {K} मन{tag(1, 1)}")
    R(B + r"kiriyaṃ" + E, "केवल क्रिया रूपी मन" + tag(1, 1))
    R(B + r"vuṭṭhānassa" + E, f"बाहर आने वाले मन{tag(1, 1, 2)} के लिए")
    R(B + r"cuticittaṃ" + E, f"मृत्यु {K} मन{tag(1, 1)}")
    R(B + r"upapatticittassa" + E, f"जन्म {K} मन{tag(1, 1, 2)} के लिए")
    R(B + r"āvajjanā" + E, "मन को विषय की ओर मोड़ने की क्रिया" + tag(2, 1))
    R(B + r"āvajjanāya mohassa ca" + E, S.AVAJJANA_FOR + " और मोह के लिए")
    R(B + r"āvajjanāya" + E, S.AVAJJANA_FOR)
    R(B + r"phalasamāpattiyā" + E, "फल की ध्यान-अवस्था" + tag(2, 1, 2) + " के लिए")
    R(B + r"phalasamāpatti" + E, "फल की ध्यान-अवस्था" + tag(2, 1))
    R(B + r"phalasamāpattiṃ" + E, "फल की ध्यान-अवस्था" + tag(2, 1))
    R(B + r"samāpattiṃ" + E, "ध्यान-अवस्था" + tag(2, 1))
    R(B + r"maggassa" + E, "मार्ग" + tag(1, 1, 2) + " के लिए")
    R(B + r"phalassa" + E, "फल" + tag(1, 1, 2) + " के लिए")
    R(B + r"maggo" + E, "मार्ग" + tag(1, 1))
    R(B + r"maggaṃ" + E, "मार्ग" + tag(1, 1))
    R(B + r"phalaṃ" + E, "फल" + tag(1, 1))
    R(B + r"nibbānaṃ" + E, S.NIBBANA + tag(1, 1))
    R(B + r"jhānaṃ" + E, "ध्यान" + tag(1, 1))
    R(B + r"vipassanaṃ" + E, "अंतर्दृष्टि" + tag(2, 1))
    R(B + r"abhiññaṃ" + E, "उच्च ज्ञान" + tag(1, 1))
    R(B + r"uposathakammaṃ" + E, "उपवास-व्रत" + tag(1, 1))
    R(B + r"uposathaṃ" + E, "उपवास-व्रत" + tag(1, 1))
    R(B + r"saṅkhāre" + E, "मानसिक रचनाओं" + tag(2, 2, 2))
    # ---------- mind and its objects
    R(B + r"vicikicchāsahagat(\w+) uddhaccasahagat\1" + E, f"{VS}{J}{US}")
    R(B + r"vicikicchāsahagat\w+", VS)
    R(B + r"uddhaccasahagat\w+", US)
    R(B + r"pañcaviññāṇasahagataṃ" + E, P5)
    R(B + r"pañcaviññāṇaṃ" + E, "पाँच प्रकार की चेतना" + tag(2, 1))
    R(B + r"sampayuttakā cetanā" + E, f"जुड़ा हुआ इरादा{tag(1, 1)}")
    R(B + r"sampayuttakā khandhā" + E, "जुड़े हुए समूह" + tag(1, 2))
    R(B + r"sampayuttakānaṃ khandhānaṃ" + E, S.SAMPAYUTTAKA_KH_OBL + tag(1, 2, 2) + " के लिए")
    R(B + r"mohassa ca cittasamuṭṭhānānañca rūpānaṃ" + E,
      f", मोह के लिए और {CSR_OBL}{tag(1, 2, 2)} के लिए")
    R(B + r"mohassa cittasamuṭṭhānānañca rūpānaṃ" + E, f"मोह के लिए और {CSR_OBL}{tag(1, 2, 2)} के लिए")
    R(B + r"cittasamuṭṭhānānañca rūpānaṃ" + E, f"और {CSR_OBL}{tag(1, 2, 2)} के लिए")
    R(B + r"cittasamuṭṭhānānaṃ rūpānaṃ" + E, f"{CSR_OBL}{tag(1, 2, 2)} के लिए")
    R(B + r"kaṭattā ca rūpānaṃ" + E, f"और {KTR_OBL}{tag(1, 2, 2)} के लिए")
    R(B + r"kaṭattārūpānaṃ" + E, f"{KTR_OBL}{tag(1, 2, 2)} के लिए")
    R(B + r"mohassa ca" + E, "और मोह" + tag(1, 1, 2) + " के लिए")
    R(B + r"mohassa" + E, "मोह" + tag(1, 1, 2) + " के लिए")
    R(B + r"cittasamuṭṭhānaṃ rūpaṃ kaṭattārūpaṃ upādārūpaṃ" + E, f"{CSR}, {KTR}, {UPR}{tag(1, 1)}")
    R(B + r"cittasamuṭṭhānaṃ rūpaṃ upādārūpaṃ" + E, f"{CSR}, {UPR}{tag(1, 1)}")
    R(B + r"kaṭattārūpaṃ upādārūpaṃ" + E, f"{KTR}, {UPR}{tag(1, 1)}")
    R(B + r"khandhā moho ca cittasamuṭṭhānañca rūpaṃ" + E, f"{KH}, मोह और {CSR}{tag(1, 1)}")
    R(B + r"moho ca cittasamuṭṭhānañca rūpaṃ" + E, f"मोह और {CSR}{tag(1, 1)}")
    R(B + r"cittasamuṭṭhānañca rūpaṃ" + E, f"और {CSR}{tag(1, 1)}")
    R(B + r"cittasamuṭṭhānaṃ rūpaṃ" + E, f"{CSR}{tag(1, 1)}")
    R(B + r"kaṭattā ca rūpaṃ" + E, f"और {KTR}{tag(1, 1)}")
    R(B + r"kaṭattārūpaṃ" + E, f"{KTR}{tag(1, 1)}")
    R(B + r"upādārūpaṃ" + E, f"{UPR}{tag(1, 1)}")
    R(B + r"rūpajīvitindriyañca" + E, f"{S.RUPAJIVITINDRIYA}{tag(1, 2)}")
    R(B + r"rūpajīvitindriyaṃ" + E, f"{S.RUPAJIVITINDRIYA}{tag(2, 1)}")
    R(B + r"kabaḷīkāro āhāro ca" + E, f"कौर-कौर खाया जाने वाला भोजन{tag(1, 2)}")
    R(B + r"kabaḷīkāro āhāro" + E, f"कौर-कौर खाया जाने वाला भोजन{tag(1, 1)}")
    R(B + r"purejātassa imassa kāyassa" + E, "पहले उत्पन्न इस शरीर" + tag(1, 1, 2) + " के लिए")
    R(B + r"imassa kāyassa" + E, "इस शरीर" + tag(1, 1, 2) + " के लिए")
    R(B + r"pacchājātā(?= –)", "पश्चात्-उत्पत्ति")
    R(B + r"pacchājātā" + E, "बाद में उत्पन्न")
    R(B + r"sahajāt(?:ā|o|aṃ)(?= –)", "सह-उत्पत्ति")
    R(B + r"purejātaṃ(?= –)", "पूर्व-उत्पत्ति")
    R(B + r"nānākkhaṇikā" + E, "भिन्न-क्षणिक")
    R(B + r"sahajātā" + E, "सह-उत्पत्ति")
    R(B + r"ārammaṇādhipati" + E, S.ARAMMANADHIPATI)
    R(B + r"sahajātādhipati" + E, S.SAHAJATADHIPATI)
    R(B + r"ārammaṇapurejātaṃ" + E, S.ARAMMANAPUREJATA)
    R(B + r"vatthupurejātaṃ" + E, S.VATTHUPUREJATA)
    for w, h in {"sahajātaṃ": "सह-उत्पत्ति", "purejātaṃ": "पूर्व-उत्पत्ति", "pacchājātaṃ": "पश्चात्-उत्पत्ति",
                 "āhāraṃ": "आहार", "indriyaṃ": "क्षमता"}.items():
        R(B + w + E, h)
    # vippayutta "X vatthuṃ vippayuttapaccayā"
    for p, h in {"khandhe ca mohañca": f"{KH_O} और मोह", "vatthuṃ": "आधार", "khandhe": KH_O,
                 "mohaṃ": "मोह"}.items():
        R(B + p + r" (vippayutta|purejāta)paccayā" + E,
          lambda m, h=h: f"{h} पर {ABL(m.group(1))}")
    # ---------- khandha / mahābhūta phrases
    R(B + r"tiṇṇannaṃ" + E, "तीन")
    R(B + r"tayo" + E, "तीन")
    R(B + r"dve" + E, "दो")
    R(B + r"ek(?:aṃ|o)(?= (?:khandh|mahābhūt))", "एक")
    # coordination: the first member takes "और", the last member carries the plural tag
    R(B + r"khandhā moho ca cittasamuṭṭhānañca rūpaṃ" + E, f"{KH}, मोह और {CSR}{tag(1, 1)}")
    R(B + r"khandhā moho ca" + E, f"{KH} और मोह{tag(1, 2)}")
    R(B + r"senāsanaṃ moho ca" + E, f"निवास-स्थान और मोह{tag(1, 2)}")
    R(B + r"khandhā ca" + E, f"{KH} और")
    R(B + r"khandho ca" + E, f"{KH} और")
    R(B + r"moho ca" + E, "मोह" + tag(1, 2))
    R(B + r"vatthu ca" + E, "आधार" + tag(1, 2))
    R(B + r"mahābhūtā ca" + E, "महाभूत" + tag(1, 2))
    R(B + r"khandhe ca…", f"{KH_O}{tag(1, 2, 2)} और…")
    R(B + r"khandhe ca" + E, f"{KH_O}{tag(1, 2, 2)}")
    R(B + r"mahābhūte ca" + E, "और महाभूतों" + tag(1, 2, 2))
    R(B + r"khandhañca" + E, f"{KH}{tag(1, 1, 2)}")
    R(B + r"khandhaṃ" + E, f"{KH}{tag(1, 1)}")
    R(B + r"khandhānaṃ" + E, f"{KH_O}{tag(1, 2, 2)} के लिए")
    R(B + r"khandhā" + E, f"{KH}{tag(1, 2)}")
    R(B + r"khandhe" + E, f"{KH_O}{tag(1, 2, 2)}")
    R(B + r"khandho" + E, f"{KH}{tag(1, 1)}")
    R(B + r"mahābhūtaṃ" + E, "महाभूत" + tag(1, 1))
    R(B + r"mahābhūte" + E, "महाभूतों" + tag(1, 2, 2))
    R(B + r"mahābhūtā" + E, "महाभूत" + tag(1, 2))
    R(B + r"vatthuñca" + E, "और आधार" + tag(1, 1))
    R(B + r"vatthussa" + E, "आधार" + tag(1, 1, 2) + " के लिए")
    R(B + r"vatthuṃ" + E, "आधार" + tag(1, 1))
    R(B + r"vatthu" + E, "आधार" + tag(1, 1))
    R(B + r"mohañca" + E, "और मोह" + tag(1, 1))
    R(B + r"moho" + E, "मोह" + tag(1, 1))
    R(B + r"mohaṃ" + E, "मोह" + tag(1, 1))
    R(B + r"cetanā" + E, "इरादा" + tag(1, 1))
    R(B + r"hetū" + E, "मूल" + tag(1, 2))
    R(B + r"adhipati" + E, "प्रधानता" + tag(2, 1))
    R(B + r"āhārā" + E, "आहार" + tag(1, 2))
    R(B + r"indriyā" + E, "क्षमताएँ" + tag(2, 2))
    R(B + r"kilese" + E, "मन के क्लेशों" + tag(1, 2, 2))
    # ---------- sense bases, consciousness, faculties
    for p, h in AYAT.items():
        R(B + p + E, f"{h} {K} इंद्रिय-क्षेत्र{tag(1, 1)}")
    for p, h in VINN.items():
        R(B + p + r"aṃ" + E, f"{h} की चेतना{tag(2, 1)}")
        R(B + p + r"assa" + E, f"{h} की चेतना{tag(2, 1, 2)} के लिए")
    R(B + r"cakkhundriyaṃ" + E, f"आँख {K} क्षमता{tag(2, 1)}")
    R(B + r"kāyindriyaṃ" + E, f"शरीर {K} क्षमता{tag(2, 1)}")
    for p, h in {"cakkhuṃ": "आँख", "sotaṃ": "कान", "ghānaṃ": "नाक", "jivhaṃ": "जीभ", "kāyaṃ": "शरीर"}.items():
        R(B + p + E, h + tag(2 if h in ("आँख", "नाक", "जीभ") else 1, 1))
    R(B + r"rūpaṃ" + E, "दृश्य रूप" + tag(1, 1))
    # ---------- conditions
    R(B + rf"({COND_RX})paccayena paccay[oa]" + E, lambda m: f"{INS(m.group(1))} {V}")
    R(B + rf"(na|no)?({COND_RX})paccay[aā]" + E,
      lambda m: NABL(m.group(2)) if m.group(1) else ABL(m.group(2)))
    # ---------- dependence words
    R(B + r"paṭicca" + E, S.DEP["paṭicca"])
    R(B + r"paccayā" + E, S.DEP["paccaya"])
    R(B + r"saṃsaṭṭh[oā]" + E, S.DEP["saṃsaṭṭha"])
    R(B + r"uppajj(ati|anti)" + E, f"उत्पन्न {V}")
    # ---------- qualities (upanissaya lists)
    for p, (h, g) in {"saddh": ("श्रद्धा", 2), "paññ": ("प्रज्ञा", 2), "patthan": ("कामना", 2)}.items():
        R(B + p + r"āya" + E, f"{h}{tag(g, 1, 2)} के लिए")
        R(B + p + r"(?:aṃ|ā)" + E, f"{h}{tag(g, 1)}")
    for p, (h, g) in {"rāg": ("राग", 1), "dos": ("द्वेष", 1), "mān": ("अहंकार", 1)}.items():
        R(B + p + r"assa" + E, f"{h}{tag(g, 1, 2)} के लिए")
        R(B + p + r"(?:aṃ|o)" + E, f"{h}{tag(g, 1)}")
    R(B + r"diṭṭhiyā" + E, "दृष्टि" + tag(2, 1, 2) + " के लिए")
    R(B + r"diṭṭhi(?:ṃ)?" + E, "दृष्टि" + tag(2, 1))
    R(B + r"vicikicch(?:ā|aṃ)" + E, "संशय" + tag(1, 1))
    R(B + r"uddhaccaṃ" + E, "बेचैनी" + tag(2, 1))
    R(B + r"domanassaṃ" + E, "उदासी" + tag(2, 1))
    R(B + r"sīlaṃ" + E, "सदाचार" + tag(1, 1))
    R(B + r"sutaṃ" + E, "सुना हुआ ज्ञान" + tag(1, 1))
    R(B + r"cāgaṃ" + E, "त्याग" + tag(1, 1))
    R(B + r"kāyikassa sukhassa" + E, "शारीरिक सुख" + tag(1, 1, 2) + " के लिए")
    R(B + r"kāyikassa dukkhassa" + E, "शारीरिक दुःख" + tag(1, 1, 2) + " के लिए")
    R(B + r"kāyikaṃ sukhaṃ" + E, "शारीरिक सुख" + tag(1, 1))
    R(B + r"kāyikaṃ dukkhaṃ" + E, "शारीरिक दुःख" + tag(1, 1))
    R(B + r"utuṃ|utu" + E, "तापमान" + tag(1, 1))
    R(B + r"bhojanaṃ" + E, "भोजन" + tag(1, 1))
    R(B + r"senāsanaṃ" + E, "निवास-स्थान" + tag(1, 1))
    # ---------- other words
    R(B + r"ahetukapaṭisandhikkhaṇe" + E, S.AHETUKA_PATISANDHI)
    R(B + r"paṭisandhikkhaṇe" + E, S.PATISANDHI)
    R(B + r"arūpe" + E, S.ARUPE)
    R(B + r"bāhiraṃ" + E, S.BAHIRA)
    R(B + r"āhārasamuṭṭhānaṃ" + E, S.AHARASAM)
    R(B + r"utusamuṭṭhānaṃ" + E, S.UTUSAM)
    R(B + r"asaññasattānaṃ" + E, S.ASANNASATTA)
    R(B + r"ahetuk(?:aṃ|ā|e|o)" + E, S.AHETUKA)
    R(B + r"vipāk(?:aṃ|e)" + E, "कर्म के फल रूपी")
    R(B + r"vipākānaṃ" + E, "कर्म के फल रूपी")
    R(B + r"vipākassa" + E, "कर्म-फल" + tag(1, 1, 2) + " के लिए")
    R(B + r"vipākā" + E, "कर्म के फल रूपी")
    R(B + r"vipāko" + E, "कर्म के फल रूपी")
    R(B + r"kusal(?:aṃ|e)" + E, "हितकर")
    R(B + r"taṃ" + E, "उसे" + tag(1, 1, 2))
    for w, h in NUMW.items():
        R(B + w + E, h)


def _nana_list(m):
    names = re.findall(rf"({NANA_RX})assa", m.group(1))
    obl = [f"{NANA[n]} के ज्ञान" for n in names]
    s = obl[0] if len(obl) == 1 else ", ".join(obl[:-1]) + " और " + obl[-1]
    s += tag(1, 1, 2) + " के लिए"
    if m.group(2):
        s += " तथा " + S.AVAJJANA_FOR
    if m.group(3):
        s += " और मोह के लिए"
    return s


init_rules()

# =====================================================================================
# 7. Counting lines
# =====================================================================================
_ABL_RX = re.compile(rf"^(?:(na|no))?({COND_RX})paccayā$")
_LOC2KEY = {v: k for k, v in S.COND_LOC_PALI.items()}
_LOC_RX = re.compile(r"^(?:(na|no))?(" + "|".join(sorted(_LOC2KEY, key=len, reverse=True)) + r")$")
NUM_C = dict(S.NUM)
NUM_C.update({"ekavīsa": "इक्कीस", "sattārasa": "सत्रह", "eka": "एक"})


def count_line(p):
    """Same rules as build_sample_hi.count_hi, plus 'sabbattha' and the closing note."""
    note = ""
    m = re.search(r"\s*\(\s*evaṃ gaṇ[ae]tabbaṃ\)", p)
    if m:
        note = " (इस प्रकार गिनना चाहिए)"
        p = p[:m.start()] + "⟪N⟫" + p[m.end():]
    toks = re.findall(r"⟪N⟫|…pe…|…|[,;.]|[^\s,;.…⟪]+", p)
    items = []
    for t in toks:
        if t == "⟪N⟫":
            items.append(("note", note.strip()))
        elif t in ("…pe…", "…"):
            items.append(("ell", "…"))
        elif t in ",;.":
            items.append(("punct", t))
        else:
            low = t[0].lower() + t[1:]
            a, l_ = _ABL_RX.match(low), _LOC_RX.match(low)
            if a:
                items.append(("neg_abl" if a.group(1) else "abl", a.group(2)))
            elif l_:
                items.append(("neg_loc" if l_.group(1) else "loc", _LOC2KEY[l_.group(2)]))
            elif low in NUM_C:
                items.append(("num", low))
            elif low == "sabbattha":
                items.append(("adv", "हर जगह"))
            else:
                raise ValueError(f"count word {t!r}")
    words = ("abl", "neg_abl", "loc", "neg_loc", "num", "adv", "note")
    out = ""
    for i, (kind, v) in enumerate(items):
        nxt = items[i + 1][0] if i + 1 < len(items) else None
        if kind in words:
            if kind in ("abl", "neg_abl", "loc", "neg_loc"):
                text = {"abl": ABL, "neg_abl": NABL, "loc": S.LOC, "neg_loc": S.NLOC}[kind](v)
            elif kind == "num":
                text = NUM_C[v]
            else:
                text = v
            if kind in ("abl", "neg_abl", "num") and nxt in words and nxt != "note":
                text += ","
            if out and not out.endswith(" "):
                out += " "
            out += text
        else:
            out = out.rstrip(" ").rstrip(",") + ("…" if kind == "ell" else ("।" if v == "." else v))
    return out.strip()


# =====================================================================================
# 8. Line translation
# =====================================================================================
ID_RX = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")
VARIANTS = {   # Pāli {…} -> Hindi bracket, inserted after the n-th occurrence of an anchor
    "ācayagāmi (sī. syā.) evamuparipi": ("[वर्तनी-भेद (Sī., Syā.): ācayagāmi, इसी प्रकार आगे भी]",
                                         item_f("a"), 1),
    "nevasekhānāsekho (sī.), nevasekkhānāsekkho (syā. ka.)":
        ("[वर्तनी-भेद (Sī.): nevasekhānāsekho, (Syā., Ka.): nevasekkhānāsekkho]", item_f("ns"), 1),
    "paṭhamassa jhānassa (?)": ("[पाठभेद (?): paṭhamassa jhānassa]", "उसी के लिए", 1),
    "nevasaññānāsaññāyatanassa (?) aññesu tikesu oloketabbaṃ":
        ("[पाठभेद (?): nevasaññānāsaññāyatanassa, अन्य तीन-तीन के वर्गीकरणों में देखना चाहिए]",
         "उसी के लिए", 2),
}
OVR = {}   # exact Pāli line (no ID) -> Hindi, for lines outside the formulas
PROBLEMS = []


def resolve(h):
    """Resolve tags and agreeing words; returns plain Hindi."""
    # 1. a tag followed by a postposition is oblique
    h = re.sub(r"⟦(\d)(\d)1⟧(?= (?:पर|को|के|की|का|से|में)(?:[\s,।;…)]|$))", r"⟦\g<1>\g<2>2⟧", h)
    h = re.sub(r"⟦(\d)(\d)1⟧(?=(?:का|में) )", r"⟦\g<1>\g<2>2⟧", h)
    tags = [(m.start(), m.group(1), m.group(2), m.group(3)) for m in re.finditer(r"⟦(\d)(\d)(\d)⟧", h)]

    def next_tag(pos):
        for t in tags:
            if t[0] > pos:
                return t
        return None

    def prev_tag(pos, direct=False, bound=True):
        best = None
        for t in tags:
            if t[0] >= pos:
                break
            if bound:
                seg = h[t[0]:pos]
                if re.search(r"[।;–?]", seg):
                    continue
            if direct and t[3] != "1":
                continue
            best = t
        return best

    def form(t):
        g, n, c = t[1], t[2], t[3]
        if g == "2":
            return "f"
        if n == "2":
            return "mp"
        return "msd" if c == "1" else "mso"

    out = []
    i = 0
    for m in re.finditer(r"⟨(\d+|V|PR|J)⟩", h):
        out.append(h[i:m.start()])
        i = m.end()
        k = m.group(1)
        if k == "V":
            t = prev_tag(m.start(), direct=True)
            if t is None:
                out.append("होता है")   # subject left out by the abbreviation
            else:
                out.append({"msd": "होता है", "mso": "होता है", "mp": "होते हैं", "f": "होती है"}[form(t)]
                           if not (t[1] == "2" and t[2] == "2") else "होती हैं")
        elif k == "PR":
            t = prev_tag(m.start(), bound=False)
            out.append("उन" if t and t[2] == "2" else "उस")
        elif k == "J":
            t = next_tag(m.start())
            out.append(" और " if t and t[2] == "2" else " या ")
        else:
            tmpl, kind = AGR[int(k)]
            t = next_tag(m.start())
            if t is None:
                f = "mp"
            else:
                f = form(t)
            out.append(tmpl.format(ENDS[kind][f]))
    out.append(h[i:])
    h = "".join(out)
    h = re.sub(r"⟦\d\d\d⟧", "", h)
    return h


def translate(line, fid, item_rules):
    m = ID_RX.search(line)
    body = ID_RX.sub("", line).strip()
    if body in OVR:
        return OVR[body]
    if body.startswith("#"):
        hashes = body.split(" ", 1)[0]
        return f"{hashes} " + ("*" + heading(body[len(hashes):], fid) + "*"
                               if body[len(hashes):].strip().startswith("*") else heading(body[len(hashes):], fid))
    low = body.lower()
    if low in CLOSE:
        return CLOSE[low]
    if low == TIKA_PALI[fid] + " niṭṭhitaṃ.":
        return S.TIKA(TIKA_NAME[fid]) + " समाप्त।"
    if re.match(r"^(hetuyā|nahetuyā|hetupaccayā|nahetupaccayā) ", low):
        try:
            return count_line(body)
        except ValueError:
            pass
    # variants
    variants = []

    def vsub(mm):
        variants.append(VARIANTS[mm.group(1)])
        return ""
    low = re.sub(r"\s*\{([^}]*)\}", vsub, low)
    # parentheticals
    parens = []

    def psub(mm):
        inner = mm.group(1).strip()
        if re.fullmatch(r"\d+\.?", inner):
            return mm.group(0)
        if inner not in PAREN:
            PROBLEMS.append("paren? " + inner)
            return mm.group(0)
        parens.append("(" + PAREN[inner] + ")")
        return f"⟪{len(parens) - 1}⟫"
    low = re.sub(r"\(([^()]*)\)", psub, low)
    # move the condition chain before the verb (frame word order)
    chain = rf"(?:na|no)?(?:{COND_RX})paccay[aā]"
    low = re.sub(rf"{B}(uppajj(?:ati|anti)) ((?:{chain})(?:(?:, |… ?| … ){chain})*){E}", r"\2 \1", low)
    # pañhāvāra frame: comma after the subject
    rules, frame = item_rules
    h = frame.sub(r"\1,", low)
    for rx, rep in PRE + rules + RULES:
        h = rx.sub(rep, h)
    # short items stand after "एक", as in the sample ("एक हितकर समूह")
    h = re.sub(r"हितकर (सीमित|उन्नत|अपरिमित) एक ", r"एक हितकर \1 ", h)
    h = re.sub(r"(?<![^\s])(सीमित|उन्नत|अपरिमित) एक ", r"एक \1 ", h)
    # a qualifier before a long item adjective takes a comma (sample: "मूल से रहित, …")
    h = re.sub(r"(मूल से रहित|कर्म के फल रूपी) (?=⟨\d+⟩)", r"\1, ", h)
    # the item adjective stands next to the head noun: "मृत्यु का सीमित मन", "बाहर आने वाले सीमित मन"
    adj = r"(⟨\d+⟩|सीमित|उन्नत|अपरिमित)"
    h = re.sub(adj + r" (मृत्यु|जन्म|जीवन-धारा) (⟨\d+⟩) मन", r"\2 \3 \1 मन", h)
    h = re.sub(adj + r" बाहर आने वाले मन", r"बाहर आने वाले \1 मन", h)
    h = re.sub(adj + " " + re.escape(S.AVAJJANA_FOR),
               r"मन को विषय की ओर मोड़ने की \1 क्रिया" + tag(2, 1, 2) + " के लिए", h)
    h = resolve(h)
    h = re.sub(r"(वाले|वाली|वाला|के|की|का) (छोड़े जा चुके|दबाए जा चुके)", r"\1, \2", h)
    h = h.replace(" ,", ",")
    h = re.sub(r"(सीखने के चरण वाले|आर्य) (?=(?:सीमित|उन्नत|अपरिमित) विषय वाले)", r"\1, ", h)
    # punctuation
    h = h.replace("…pe…", "…")
    h = re.sub(r"\.(?=\s|$|\)|⟪)", "।", h)
    for i, p in enumerate(parens):
        h = h.replace(f"⟪{i}⟫", p)
    for txt, anchor, nth in variants:
        idx = -1
        for _ in range(nth):
            idx = h.find(anchor, idx + 1)
        if idx < 0:
            PROBLEMS.append("variant anchor missing: " + anchor)
        else:
            j = idx + len(anchor)
            h = h[:j] + " " + txt + h[j:]
    h = re.sub(r" {2,}", " ", h).strip()
    return h


LATIN = re.compile(r"[A-Za-zĀāĪīŪūṄṅÑñṬṭḌḍṆṇḶḷṂṃ]{2,}")


def latin_left(h):
    body = re.sub(r"\[(?:पाठभेद|वर्तनी-भेद) \([^)]*\): [^\]]*\]", "", h)
    return LATIN.findall(body)


FILES = {"2-04": "2-04-dassanenapahatabbahetukattika.md", "2-05": "2-05-acayagamittika.md",
         "2-06": "2-06-sekkhattika.md", "2-07": "2-07-parittattika.md", "2-08": "2-08-parittarammanattika.md"}


def build(fid):
    item_rules = build_item_rules(fid)
    ptxt = (PALI_DIR / FILES[fid]).read_text(encoding="utf-8")
    hl = []
    bad = []
    for n, line in enumerate([l for l in ptxt.splitlines() if l.strip()], 1):
        h = translate(line, fid, item_rules)
        left = latin_left(h)
        if left or "⟨" in h or "⟦" in h or "⟪" in h:
            bad.append((n, left[:8], h[:160]))
        hl.append(h)
    return S.assemble(ptxt, hl), bad


def main():
    only = [a for a in sys.argv[1:] if not a.startswith("--")]
    for fid, fname in FILES.items():
        if only and fid not in only:
            continue
        text, bad = build(fid)
        print(f"{fname}: {len(bad)} lines with residue")
        for n, left, h in bad[:60]:
            print(f"  L{n}: {left} :: {h}")
        if "--check" not in sys.argv:
            with open(HI_DIR / fname, "w", encoding="utf-8", newline="\n") as f:
                f.write(text)
    for p in sorted(set(PROBLEMS))[:60]:
        print("PROBLEM:", p)


if __name__ == "__main__":
    main()
