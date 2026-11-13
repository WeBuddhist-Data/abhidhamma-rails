"""pi-7 Paṭṭhāna, Hindi plain RAILS: builder for 1-02 vedanāttika, 1-03 vipākattika, 1-04 upādinnattika,
1-05 saṃkiliṭṭhattika. Imports the approved sample builder read-only (constants and count words).

usage: python -I -B -X utf8 build_rails_1-02_1-05.py [stem ...]      (writes the output files)
       python -I -B -X utf8 build_rails_1-02_1-05.py --dry [stem ...] (reports residues only)

Method: each Pāli line is split into clauses at the Pāli separators; inside a clause, the triad items become
tokens, a few reorder rules move Hindi-final material (the condition chain before «उत्पन्न होती है», the
postposition of an object before an instrumental), then a phrase table (longest match first) gives the Hindi in
Pāli order. Hindi agreement is resolved at the end: an adjective's «@» takes the gender/number of the next noun
marker, a verb token takes the last subject marker before it.
"""
import collections
import os
import re
import sys

RAILS = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\rails"
sys.path.insert(0, RAILS)
import build_rails_sample as S  # noqa: E402  (read-only import)

FILES = ["1-02-vedanattika", "1-03-vipakattika", "1-04-upadinnattika", "1-05-sankilitthattika"]

# ---------------------------------------------------------------- markers and agreement


def MK(t):
    return "\x01" + t + "\x02"


MS, FS, MP, FP, OM, OF = (MK(t) for t in ("ms", "fs", "mp", "fp", "om", "of"))
NOM_TAGS = {"ms", "fs", "mp", "fp"}
ADJ_END = {"ms": "ा", "mp": "े", "om": "े", "fs": "ी", "fp": "ी", "of": "ी"}


def V(name):
    """verb token, agrees with the last subject marker before it"""
    return "\x03" + name + "\x04"


VERB = {
    "arise": {"ms": "उत्पन्न होता है", "fs": "उत्पन्न होती है", "mp": "उत्पन्न होते हैं", "fp": "उत्पन्न होती हैं"},
}
VERB["P0"] = {"ms": "कारण होता है", "fs": "कारण होती है", "mp": "कारण होते हैं", "fp": "कारण होती हैं"}
for _k in S.KEYS:
    VERB["P:" + _k] = {g: S.INS(_k, g) for g in NOM_TAGS}
    VERB["NP:" + _k] = {g: S.NINS(_k, g) for g in NOM_TAGS}

TOKEN_RE = re.compile("\x01(\\w+)\x02|\x03([^\x04]+)\x04|@")


def resolve(s, state):
    out = []
    pos = 0
    for m in TOKEN_RE.finditer(s):
        out.append(s[pos:m.start()])
        pos = m.end()
        if m.group(1):
            if m.group(1) in NOM_TAGS:
                state["subj"] = m.group(1)
            elif m.group(1) == "pl" and state.get("subj"):  # after a coordination: plural verb
                state["subj"] = state["subj"][0] + "p"
        elif m.group(2):
            g = state.get("subj")
            if g is None:
                raise KeyError("verb without subject: " + s)
            out.append(VERB[m.group(2)][g])
        else:  # @: next marker
            n = re.search("\x01(ms|fs|mp|fp|om|of)\x02", s[m.end():])
            if not n:
                raise KeyError("adjective without noun: " + s)
            if s[max(0, m.start() - 2):m.start()] == "हु":
                out.append({"ms": "आ", "mp": "ए", "om": "ए"}.get(n.group(1), "ई"))
            else:
                out.append(ADJ_END[n.group(1)])
    out.append(s[pos:])
    return "".join(out)


# ---------------------------------------------------------------- the triad items

ITEM_HI = {
    "vs": "सुखद अनुभूति से जुड़@",
    "vd": "दुःखद अनुभूति से जुड़@",
    "va": "न दुःखद, न सुखद अनुभूति से जुड़@",
    "vp": "कर्म-फल रूपी",
    "vk": "कर्म-फल उत्पन्न करने वाल@",
    "nv": "न कर्म-फल रूपी, न कर्म-फल उत्पन्न करने वाल@",
    "u1": "कर्म से उत्पन्न और आसक्ति का विषय बनने वाल@",
    "u2": "कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाल@",
    "u3": "न कर्म से उत्पन्न, न आसक्ति का विषय बनने वाल@",
    "up": "कर्म से उत्पन्न",
    "un": "कर्म से उत्पन्न न होने वाल@",
    "s1": "क्लेशों से मलिन और क्लेशों का विषय बनने वाल@",
    "s2": "क्लेशों से मलिन न होने वाल@, पर क्लेशों का विषय बनने वाल@",
    "s3": "क्लेशों से मलिन न होने वाल@ और क्लेशों का विषय न बनने वाल@",
    "sk": "क्लेशों से मलिन",
    "sn": "क्लेशों से मलिन न होने वाल@",
}
# (regex on the lowercased line, key, has its own noun 'dhamma' inside the word)
ITEM_RX = [
    (r"adukkhamasukhāya vedanāya sampayutt", "va", False),
    (r"sukhāya vedanāya sampayutt", "vs", False),
    (r"dukkhāya vedanāya sampayutt", "vd", False),
    (r"nevavipākanavipākadhammadhamm", "nv", True),
    (r"vipākadhammadhamm", "vk", True),
    (r"vipāk", "vp", False),
    (r"anupādinnaanupādāniy", "u3", False),
    (r"anupādinnupādāniy", "u2", False),
    (r"upādinnupādāniy", "u1", False),
    (r"anupādinn", "un", False),
    (r"upādinn", "up", False),
    (r"asaṃkiliṭṭhaasaṃkilesik", "s3", False),
    (r"asaṃkiliṭṭhasaṃkilesik", "s2", False),
    (r"asaṅkiliṭṭhasaṃkilisik", "s2", False),   # spelling slip in 1-05, rendered as meant
    (r"saṃkiliṭṭhasaṃkilesik", "s1", False),
    (r"asaṃkiliṭṭh", "sn", False),
    (r"saṃkiliṭṭh", "sk", False),
]
ITEM_WORD_RE = re.compile(r"(?<![\w‹›])(" + "|".join(r for r, _, _ in ITEM_RX) + r")([\wāīūṃṅñṭḍṇḷ]*)")
ITEM_KEY = {r.replace("\\", ""): (k, own) for r, k, own in ITEM_RX}
INFL = {"aṃ", "o", "ā", "e", "assa", "ānaṃ", "akānaṃ", "āya", "ena", "āni", "akā", "ake", ""}
NOUN_AFTER = re.compile(r"^(?:ekaṃ|eko|ekassa|khandh|tiṇṇannaṃ|dvinnaṃ|hetū|cetanā|cittena|cittaṃ|jhān|rūp|kāy|"
                        r"kabaḷīkāro|āhār|indriy|maggaṅg|jhānaṅg|mahābhūt|vatthu|sadd|gandh|ras|phoṭṭhabb|"
                        r"cakkh|sot|ghān|jivh|saddh|sīl|sut|cāg|paññ|rāg|moh|mān|diṭṭh|patthan|dos|uddhacc|"
                        r"vicikicch|domanass|anulom|bhavaṅg|cuticitt|upapatticitt|gotrabh|vodān|magg|phal|"
                        r"kusal|akusal|kiriy|āvajjan|vuṭṭhān|ākāsānañc|viññāṇañc|ākiñcañ|nevasaññ|sukhasahagat|"
                        r"dukkhasahagat|kāyaviññāṇ|cakkhuviññāṇ|manoviññāṇ|manodhāt|upādārūp|kaṭattā|"
                        r"cittasamuṭṭhān|senāsan|utu|bhojan|puggal|pahīne|vikkhambhite|nibbān)")
DHAMMA_FORM = {"aṃ": "dhammaṃ", "o": "dhammo", "ā": "dhammā", "assa": "dhammassa", "ānaṃ": "dhammānaṃ", "e": "dhamme"}


def items_to_tokens(text):
    """Item words -> ‹key›; -ñca -> ' ca'; compound tails stay as '‹key›_tail'."""
    out = []
    pos = 0
    for m in ITEM_WORD_RE.finditer(text):
        stem, tail = m.group(1), m.group(2)
        key, own = ITEM_KEY[stem]
        bare = tail[:-3] if tail.endswith("ñca") else tail
        if not (bare in INFL or bare + "ṃ" in INFL or bare.rstrip("ṃ") + "ṃ" in INFL or bare in TAIL):
            continue  # not an item word (vipākapaccayā, vipākamanodhātu, upādinnattike …)
        out.append(text[pos:m.start()])
        pos = m.end()
        rest = text[m.end():].lstrip()
        ca = ""
        if tail.endswith("ñca"):
            tail, ca = tail[:-3] + "aṃ" if tail[:-3].endswith("a") else tail[:-3], " ca"
            tail = tail.replace("aaṃ", "aṃ")
        if tail in INFL or tail.rstrip("ṃ") + "ṃ" in INFL:
            tok = "‹" + key + ("+h" if key in ("vs", "vd", "va") and tail in ("akānaṃ", "akā", "ake") else "") + "›"
            with_ca = bool(ca) or bool(re.match(r"ca(?![\wāīūṃṅñṭḍṇḷ])", rest))
            first = rest.split(" ", 1)[0]
            noun_after = bool(NOUN_AFTER.match(rest)) and "paccay" not in first
            if with_ca and tail == "assa":
                tok += " §dat"
            elif not with_ca and not rest.startswith("dhamm") and not noun_after \
                    and (own or rest == "" or rest[0] in "….\x05;,–"):
                tok += " " + DHAMMA_FORM.get(tail, "dhamm" + tail)
            out.append(tok + ca)
        else:
            out.append("‹" + key + "›_" + tail + ca)
    out.append(text[pos:])
    return "".join(out)


def item_hi(key):
    if key.endswith("+h"):  # sampayuttaka-: «जुड़े हुए» (termbase)
        return ITEM_HI[key[:-2]] + " हु@"
    return ITEM_HI[key]


# ---------------------------------------------------------------- phrase table (Pāli in lowercase, Hindi with markers)

RC, RK, RU = S.RUPA_CITTA, S.RUPA_KATATTA, S.RUPA_UPADA
PH = {
    # dhamma
    "dhammaṃ": OF + "परिघटना", "dhammo": FS + "परिघटना", "dhammā": FP + "परिघटनाएँ",
    "dhammo§c": FS + "परिघटना,", "dhammā§c": FP + "परिघटनाएँ,",
    "dhammassa": OF + "परिघटना के लिए", "dhammānaṃ": OF + "परिघटनाओं के लिए", "dhamme": OF + "परिघटनाओं",
    # khandha
    "ekaṃ khandhaṃ": OM + "एक समूह", "eko khandho": MS + "एक समूह", "khandho": MS + "समूह",
    "khandhaṃ": OM + "समूह",
    "tayo khandhā": MP + "तीन समूह", "dve khandhā": MP + "दो समूह", "khandhā": MP + "समूह",
    "cattāro khandhā": MP + "चार समूह",
    "tayo khandhe": OM + "तीन समूहों", "dve khandhe": OM + "दो समूहों", "khandhe": OM + "समूहों",
    "khandhānaṃ": OM + "समूहों के लिए", "tiṇṇannaṃ khandhānaṃ": OM + "तीन समूहों के लिए",
    "dvinnaṃ khandhānaṃ": OM + "दो समूहों के लिए", "ekassa khandhassa": OM + "एक समूह के लिए",
    "khandhassa": OM + "समूह के लिए",
    "sampayuttakānaṃ khandhānaṃ": OM + "जुड़े हुए समूहों के लिए",
    "cittasamuṭṭhānānaṃ rūpānaṃ": OM + "मन से उत्पन्न भौतिक रूपों के लिए",
    "kaṭattārūpānaṃ": OM + "किए गए कर्म से उत्पन्न भौतिक रूपों के लिए",
    "upādārūpānaṃ": OM + "व्युत्पन्न भौतिक रूपों के लिए",
    "cittasamuṭṭhānānañca rūpānaṃ": OM + "और मन से उत्पन्न भौतिक रूपों के लिए",
    "kaṭattā ca rūpānaṃ": OM + "और किए गए कर्म से उत्पन्न भौतिक रूपों के लिए",
    "cittasamuṭṭhānañca rūpaṃ": MS + "और " + RC, "kaṭattā ca rūpaṃ": MS + "और " + RK,
    "vatthu ca": MS + "और आधार",
    "cittasamuṭṭhānaṃ rūpaṃ": MS + RC, "kaṭattārūpaṃ": MS + RK, "upādārūpaṃ": MS + RU,
    "hetū": MP + "मूल", "cetanā": MS + "इरादा", "cittena": OM + "मन से", "duṭṭhena cittena": OM + "दुष्ट मन से",
    # matter
    "ekaṃ mahābhūtaṃ": MS + "एक महाभूत", "tayo mahābhūtā": MP + "तीन महाभूत", "dve mahābhūtā": MP + "दो महाभूत",
    "mahābhūtā": MP + "महाभूत", "tayo mahābhūte": OM + "तीन महाभूतों", "dve mahābhūte": OM + "दो महाभूतों",
    "mahābhūte": OM + "महाभूतों", "tiṇṇannaṃ mahābhūtānaṃ": OM + "तीन महाभूतों के लिए",
    "dvinnaṃ mahābhūtānaṃ": OM + "दो महाभूतों के लिए", "ekassa mahābhūtassa": OM + "एक महाभूत के लिए",
    "mahābhūtānaṃ": OM + "महाभूतों के लिए",
    "bāhiraṃ ekaṃ mahābhūtaṃ": MS + "एक बाह्य महाभूत",
    "āhārasamuṭṭhānaṃ ekaṃ mahābhūtaṃ": MS + "आहार से उत्पन्न एक महाभूत",
    "utusamuṭṭhānaṃ ekaṃ mahābhūtaṃ": MS + "तापमान से उत्पन्न एक महाभूत",
    "asaññasattānaṃ ekaṃ mahābhūtaṃ": MS + "पहचान-रहित प्राणियों में एक महाभूत",
    "bāhiraṃ": "बाह्य", "āhārasamuṭṭhānaṃ": "आहार से उत्पन्न", "utusamuṭṭhānaṃ": "तापमान से उत्पन्न",
    "asaññasattānaṃ": "पहचान-रहित प्राणियों में",
    "vatthu": MS + "आधार", "vatthuṃ": OM + "आधार", "vatthussa": OM + "आधार के लिए",
    "rūpajīvitindriyaṃ": FS + "भौतिक जीवन-क्षमता",
    # moments
    "paṭisandhikkhaṇe": "पुनर्जन्म के क्षण में", "ahetukapaṭisandhikkhaṇe": "मूल से रहित पुनर्जन्म के क्षण में",
    "arūpe": "अभौतिक लोक में", "ahetukaṃ": "मूल से रहित,", "ahetuke": "मूल से रहित,",
    # frame words
    "paṭicca": "पर निर्भर होकर", "paccayā": "के कारण", "nissāya": "के आश्रय से",
    "sahajāto": "के साथ जन्म लेकर", "sahajātā§f": "के साथ जन्म लेकर",
    "saṃsaṭṭho": "से घुल-मिलकर", "saṃsaṭṭhā": "से घुल-मिलकर",
    "sampayutto": "से जुड़कर", "sampayuttā": "से जुड़कर",
    "ārabbha": "को विषय बनाकर", "upanissāya": "के प्रबल आश्रय से",
    "taṃ ārabbha": "उसे विषय बनाकर", "taṃ garuṃ katvā": "उसे महत्व देकर",
    "§aur": "और", "§comma": ",", "§pl": MK("pl"),
    "purimā purimā": "पहले-पहले क@", "pacchimānaṃ pacchimānaṃ": "बाद-बाद क@",
    "taṃ": "उस", "cittaṃ": OM + "मन", "adukkhamasukhāya vedanāya": "न दुःखद, न सुखद अनुभूति से",
    "uppajjati": V("arise"), "uppajjanti": V("arise"),
    # labels
    "ārammaṇādhipati": FS + "विषय रूपी प्रधानता", "sahajātādhipati": FS + "सह-उत्पत्ति रूपी प्रधानता",
    "ārammaṇūpanissayo": MS + "विषय रूपी प्रबल आश्रय", "anantarūpanissayo": MS + "निकटता रूपी प्रबल आश्रय",
    "pakatūpanissayo": MS + "स्वाभाविक प्रबल आश्रय",
    "ārammaṇapurejātaṃ": "विषय रूपी पूर्व-उत्पत्ति", "vatthupurejātaṃ": "आधार रूपी पूर्व-उत्पत्ति",
    "sahajātaṃ": "सह-उत्पत्ति", "purejātaṃ": "पूर्व-उत्पत्ति", "pacchājātaṃ": "पश्चात्-उत्पत्ति",
    "āhāraṃ": "आहार", "indriyaṃ": "क्षमता", "sahajātā": "सह-उत्पत्ति", "pacchājātā": "पश्चात्-उत्पत्ति",
    "nānākkhaṇikā": "भिन्न क्षण", "purejātā": "पूर्व-उत्पत्ति",
    # Pañhāvāra objects and actions
    "dānaṃ datvā": "दान देकर", "sīlaṃ samādiyitvā": "सदाचार ग्रहण करके",
    "uposathakammaṃ katvā": "उपवास-व्रत का पालन करके",
    "dānaṃ deti": "दान देता है", "sīlaṃ samādiyati": "सदाचार ग्रहण करता है",
    "uposathakammaṃ karoti": "उपवास-व्रत का पालन करता है",
    "jhānaṃ uppādeti": "ध्यान उत्पन्न करता है", "vipassanaṃ uppādeti": "अंतर्दृष्टि उत्पन्न करता है",
    "maggaṃ uppādeti": "मार्ग उत्पन्न करता है", "abhiññaṃ uppādeti": "उच्च ज्ञान उत्पन्न करता है",
    "samāpattiṃ uppādeti": "ध्यान-अवस्था उत्पन्न करता है", "uppādeti": "उत्पन्न करता है",
    "mānaṃ jappeti": "अहंकार पालता है", "diṭṭhiṃ gaṇhāti": "दृष्टि ग्रहण करता है",
    "adinnaṃ ādiyati": "बिना दिया हुआ लेता है", "musā bhaṇati": "झूठ बोलता है",
    "pisuṇaṃ bhaṇati": "चुगली की बात बोलता है", "pharusaṃ bhaṇati": "कठोर वचन बोलता है",
    "samphaṃ palapati": "व्यर्थ बकवास करता है", "sandhiṃ chindati": "सेंध लगाता है",
    "nillopaṃ harati": "डाका डालता है", "ekāgārikaṃ karoti": "एक ही घर में डाका डालता है",
    "paripanthe tiṭṭhati": "राह में घात लगाता है", "paradāraṃ gacchati": "पराई स्त्री के पास जाता है",
    "gāmaghātaṃ karoti": "गाँव पर हमला करता है", "nigamaghātaṃ karoti": "कस्बे पर हमला करता है",
    "pāṇaṃ hanati": "जीव की हत्या करता है", "mātaraṃ jīvitā voropeti": "माता की जान लेता है",
    "pitaraṃ jīvitā voropeti": "पिता की जान लेता है", "arahantaṃ jīvitā voropeti": "अर्हत् की जान लेता है",
    "tathāgatassa lohitaṃ uppādeti": "तथागत का खून बहाता है", "saṅghaṃ bhindati": "संघ में फूट डालता है",
    "attānaṃ ātāpeti paritāpeti": "स्वयं को तपाता है, कष्ट देता है",
    "pariyiṭṭhimūlakaṃ dukkhaṃ paccanubhoti": "खोज के कारण होने वाला दुःख भोगता है",
    "jhānā vuṭṭhahitvā": "ध्यान से उठकर", "maggā vuṭṭhahitvā": "मार्ग से उठकर", "phalā vuṭṭhahitvā": "फल से उठकर",
    "jhāne parihīne vippaṭisārissa domanassaṃ uppajjati": "ध्यान के छूट जाने पर ग्लानि से भरे व्यक्ति में उदासी उत्पन्न होती है",
    "vippaṭisārissa domanassaṃ uppajjati": "ग्लानि से भरे व्यक्ति में उदासी उत्पन्न होती है",
    "jhāne parihīne": "ध्यान के छूट जाने पर",
    "ariyā": MP + "आर्य", "sekkhā": MP + S.SEKKHA, "sekkhā vā puthujjanā vā": MP + S.SEKKHA_PUTHU,
    "arahā": MS + S.ARAHA,
    "pahīne kilese": OM + S.KILESA["pahīne"], "vikkhambhite kilese": OM + S.KILESA["vikkhambhite"],
    "pubbe samudāciṇṇe kilese": OM + S.KILESA["pubbe samudāciṇṇe"],
    "pubbe suciṇṇāni": OM + S.DEEDS,
    "cetopariyañāṇena": S.CETOPARIYA,
    "rāgo": MS + "राग", "diṭṭhi": FS + "दृष्टि", "vicikicchā": MS + "संशय", "uddhaccaṃ": FS + "बेचैनी",
    "domanassaṃ": FS + "उदासी", "doso": MS + "द्वेष", "moho": MS + "मोह", "māno": MS + "अहंकार",
    "saddhā": FS + "श्रद्धा", "sīlaṃ": MS + "सदाचार", "sutaṃ": MS + "सुना-सीखा ज्ञान", "cāgo": MS + "त्याग",
    "paññā": FS + "प्रज्ञा", "patthanā": FS + "कामना",
    "saddhaṃ": OF + "श्रद्धा", "cāgaṃ": OM + "त्याग", "paññaṃ": OF + "प्रज्ञा", "rāgaṃ": OM + "राग",
    "mohaṃ": OM + "मोह", "mānaṃ": OM + "अहंकार", "diṭṭhiṃ": OF + "दृष्टि", "patthanaṃ": OF + "कामना",
    "dosaṃ": OM + "द्वेष", "vicikicchaṃ": OM + "संशय",
    "saddhāya": OF + "श्रद्धा के लिए", "sīlassa": OM + "सदाचार के लिए", "sutassa": OM + "सुने-सीखे ज्ञान के लिए",
    "cāgassa": OM + "त्याग के लिए", "paññāya": OF + "प्रज्ञा के लिए", "rāgassa": OM + "राग के लिए",
    "mohassa": OM + "मोह के लिए", "mānassa": OM + "अहंकार के लिए", "diṭṭhiyā": OF + "दृष्टि के लिए",
    "patthanāya": OF + "कामना के लिए", "dosassa": OM + "द्वेष के लिए",
    "kāyaviññāṇaṃ": FS + "शरीर की चेतना", "kāyaviññāṇassa": OF + "शरीर की चेतना के लिए",
    "sukhasahagataṃ kāyaviññāṇaṃ": FS + "सुख के साथ होने वाली शरीर की चेतना",
    "dukkhasahagataṃ kāyaviññāṇaṃ": FS + "दुःख के साथ होने वाली शरीर की चेतना",
    "sukhasahagatassa kāyaviññāṇassa": OF + "सुख के साथ होने वाली शरीर की चेतना के लिए",
    "dukkhasahagatassa kāyaviññāṇassa": OF + "दुःख के साथ होने वाली शरीर की चेतना के लिए",
    "sukhasahagataṃ kāyaviññāṇasahagataṃ ekaṃ khandhaṃ":
        OM + "सुख के साथ होने वाले और शरीर की चेतना के साथ होने वाले एक समूह",
    "dukkhasahagataṃ kāyaviññāṇasahagataṃ ekaṃ khandhaṃ":
        OM + "दुःख के साथ होने वाले और शरीर की चेतना के साथ होने वाले एक समूह",
    "catuviññāṇasahagataṃ ekaṃ khandhaṃ": OM + "चार प्रकार की चेतना के साथ होने वाले एक समूह",
    "pañcaviññāṇasahagataṃ ekaṃ khandhaṃ": OM + "पाँच प्रकार की चेतना के साथ होने वाले एक समूह",
    "vicikicchāsahagate uddhaccasahagate khandhe": OM + "संशय के साथ होने वाले और बेचैनी के साथ होने वाले समूहों",
    "vicikicchāsahagato uddhaccasahagato moho": MS + "संशय के साथ होने वाला या बेचैनी के साथ होने वाला मोह",
    # moments of the process
    "anulomaṃ§m": FS + "अनुरूपता", "gotrabhu": MS + "गोत्र-परिवर्तन", "vodānaṃ": FS + "शुद्धि",
    "maggo": MS + "मार्ग", "phalaṃ": MS + "फल",
    "gotrabhussa": OM + "गोत्र-परिवर्तन के लिए", "vodānassa": OF + "शुद्धि के लिए", "maggassa": OM + "मार्ग के लिए",
    "phalassa": OM + "फल के लिए",
    "phalasamāpattiyā": OF + "फल की ध्यान-अवस्था के लिए",
    "cuticittaṃ": MS + "मृत्यु का मन", "upapatticittassa": OM + "जन्म के मन के लिए",
    "bhavaṅgaṃ": FS + "जीवन-धारा", "bhavaṅgassa": OF + "जीवन-धारा के लिए",
    "āvajjanā": MS + "मन को विषय की ओर मोड़ना", "āvajjanāya": OM + "मन को विषय की ओर मोड़ने के लिए",
    "vuṭṭhānassa": OM + "बाहर आने के लिए",
    "vipākamanodhātu": MS + "कर्म-फल रूपी मन का तत्व", "vipākamanodhātuyā": OM + "कर्म-फल रूपी मन के तत्व के लिए",
    "vipākamanoviññāṇadhātu": MS + "कर्म-फल रूपी मन की चेतना का तत्व",
    "vipākamanoviññāṇadhātuyā": OM + "कर्म-फल रूपी मन की चेतना के तत्व के लिए",
    "kiriyamanoviññāṇadhātuyā": OM + "केवल क्रिया रूपी मन की चेतना के तत्व के लिए",
    "kusalākusalaṃ": MS + "हितकर और हानिकर मन", "kiriyaṃ": MS + "केवल क्रिया रूपी मन",
    "ākāsānañcāyatanaṃ": MS + "अनंत आकाश का क्षेत्र", "ākiñcaññāyatanaṃ": MS + "कुछ भी न होने का क्षेत्र",
    "viññāṇañcāyatanassa": OM + "अनंत चेतना के क्षेत्र के लिए",
    "nevasaññānāsaññāyatanassa": OM + "न पहचान न अ-पहचान के क्षेत्र के लिए",
    "nevasaññānāsaññāyatanaṃ": MS + "न पहचान न अ-पहचान का क्षेत्र",
}
PH.update({
    "purejātassa imassa": "पहले उत्पन्न इस", "imassa": "इस", "kāyassa": OM + "शरीर के लिए",
    "purejātassa imassa kāyassa": OM + "पहले उत्पन्न इस शरीर के लिए",
    "kabaḷīkāro āhāro": MS + "कौर-कौर खाया जाने वाला भोजन",
    "cakkhuṃ": OM + "आँख", "sotaṃ": OM + "कान", "ghānaṃ": OM + "नाक", "jivhaṃ": OM + "जीभ", "kāyaṃ": OM + "शरीर",
    "rūpe": OM + "दृश्य रूपों", "sadde": OM + "ध्वनियों", "gandhe": OM + "गंधों", "rase": OM + "स्वादों",
    "phoṭṭhabbe": OM + "स्पर्शों", "rūpaṃ": OM + "दृश्य रूप", "saddaṃ": OF + "ध्वनि",
    "dibbena cakkhunā": "दिव्य आँख से", "dibbāya sotadhātuyā": "दिव्य कान के तत्व से",
    "nibbānaṃ": MS + "निर्वाण", "jhānaṃ": OM + "ध्यान", "maggaṃ": OM + "मार्ग", "gotrabhuṃ": OM + "गोत्र-परिवर्तन",
    "āhārā": MP + "आहार", "indriyā": FP + "क्षमताएँ", "jhānaṅgāni": MP + "ध्यान के अंग", "jhānaṅgā": MP + "ध्यान के अंग",
    "maggaṅgāni": MP + "मार्ग के अंग", "adhipati": FS + "प्रधानता",
    "kāyikaṃ sukhaṃ": MS + "शारीरिक सुख", "kāyikaṃ dukkhaṃ": MS + "शारीरिक दुःख",
    "kāyikassa sukhassa": OM + "शारीरिक सुख के लिए", "kāyikassa dukkhassa": OM + "शारीरिक दुःख के लिए",
    "utu": MS + "तापमान", "utuṃ": OM + "तापमान", "bhojanaṃ": MS + "भोजन", "senāsanaṃ": MS + "निवास-स्थान",
    "parikammaṃ": FS + "प्रारंभिक तैयारी",
    "anuppannaṃ kusalasamāpattiṃ": OF + "उत्पन्न न हुई हितकर ध्यान-अवस्था",
    "anuppannaṃ kiriyasamāpattiṃ": OF + "उत्पन्न न हुई केवल क्रिया रूपी ध्यान-अवस्था",
    "uppādenti": "उत्पन्न करते हैं", "uppannaṃ samāpajjati": "उत्पन्न हो चुकी में प्रवेश करता है",
    "uppannaṃ samāpajjanti": "उत्पन्न हो चुकी में प्रवेश करते हैं",
    "phalasamāpattiṃ samāpajjati": "फल की ध्यान-अवस्था में प्रवेश करता है",
    "phalasamāpattiṃ samāpajjanti": "फल की ध्यान-अवस्था में प्रवेश करते हैं",
    "saṅkhāre": OF + "निर्मित परिघटनाओं",
    "sekkhānaṃ": "सीखने के चरण वाले व्यक्तियों क@", "arahato": "अर्हत् क@", "ariyānaṃ": "आर्यों क@",
    "atthappaṭisambhidāya": OM + "अर्थ के विश्लेषणात्मक ज्ञान के लिए",
    "ṭhānāṭhānakosallassa": OF + "संभव और असंभव को जानने की कुशलता के लिए",
    "pāṇaṃ hantvā": "जीव की हत्या करके", "saṅghaṃ bhinditvā": "संघ में फूट डालकर",
    "tassa paṭighātatthāya": "उसके प्रतिकार के लिए",
    "pāṇātipāto pāṇātipātassa": FS + "जीव-हत्या, जीव-हत्या के लिए",
    "niyatamicchādiṭṭhi niyatamicchādiṭṭhiyā": FS + "निश्चित ग़लत दृष्टि, निश्चित ग़लत दृष्टि के लिए",
    "pañcaviññāṇaṃ": FS + "पाँच प्रकार की चेतना", "pañcannaṃ viññāṇānaṃ": OF + "पाँच प्रकार की चेतना के लिए",
    "tiṇṇannaṃ": "तीन", "dvinnaṃ": "दो",
    "ahetukā": "मूल से रहित,", "kusale": "हितकर", "kusalā": "हितकर", "akusale": "हानिकर", "akusalā": "हानिकर",
    "kusalaṃ§a": "हितकर", "akusalaṃ§a": "हानिकर",
    "kusalaṃ": OM + "हितकर", "akusalaṃ": OM + "हानिकर",
    "pacchājātā§a": "बाद में उत्पन्न", "sahajātā§a": "साथ उत्पन्न",
    "paccayo": V("P0"), "anulomaṃ§m": FS + "अनुरूपता",
    "cakkhuviññāṇaṃ": FS + "आँख की चेतना", "cakkhuviññāṇassa": OF + "आँख की चेतना के लिए",
})
PH.update({
    "sota": "कान", "ghāna": "नाक", "jivhā": "जीभ", "kāya": "शरीर",
    "micchādiṭṭhiyā": OF + "ग़लत दृष्टि के लिए", "micchādiṭṭhi micchādiṭṭhiyā": FS + "ग़लत दृष्टि, ग़लत दृष्टि के लिए",
    "byāpādassa": OF + "दुर्भावना के लिए", "niyatamicchādiṭṭhiyā": OF + "निश्चित ग़लत दृष्टि के लिए",
    "mātughātikammaṃ mātughātikammassa": MS + "माता की हत्या का कर्म, माता की हत्या के कर्म के लिए",
    "vatthussa ca": OM + "और आधार के लिए",
    "nevasaññānāsaññāyatanakusalaṃ": MS + "न पहचान न अ-पहचान के क्षेत्र का हितकर मन",
    "nevasaññānāsaññāyatanakiriyaṃ": MS + "न पहचान न अ-पहचान के क्षेत्र का केवल क्रिया रूपी मन",
    "mātughātikammassa": OM + "माता की हत्या के कर्म के लिए", "pitughātikammassa": OM + "पिता की हत्या के कर्म के लिए",
    "arahantaghātikammassa": OM + "अर्हत् की हत्या के कर्म के लिए",
    "ruhiruppādakammassa": OM + "बुद्ध का खून बहाने के कर्म के लिए",
    "saṅghabhedakammassa": OM + "संघ में फूट डालने के कर्म के लिए",
    "saṅghabhedakakammassa": OM + "संघ में फूट डालने के कर्म के लिए",
    "anuppannaṃ samāpattiṃ": OF + "उत्पन्न न हुई ध्यान-अवस्था",
    "uppannaṃ samāpattiṃ samāpajjanti": "उत्पन्न हो चुकी ध्यान-अवस्था में प्रवेश करते हैं",
    "uppannaṃ samāpattiṃ samāpajjati": "उत्पन्न हो चुकी ध्यान-अवस्था में प्रवेश करता है",
    "dhammappaṭisambhidāya": OM + "परिघटनाओं के विश्लेषणात्मक ज्ञान के लिए",
    "niruttippaṭisambhidāya": OM + "भाषा के विश्लेषणात्मक ज्ञान के लिए",
    "paṭibhānappaṭisambhidāya": OM + "सूझ-बूझ के विश्लेषणात्मक ज्ञान के लिए",
    "nirodhā vuṭṭhahantassa": "समाप्ति की ध्यान-अवस्था से बाहर आने वाले व्यक्ति में",
    "phalasamāpatti": FS + "फल की ध्यान-अवस्था", "maggaṅgā": MP + "मार्ग के अंग",
    "vipassanaṃ": OF + "अंतर्दृष्टि", "samāpattiṃ": OF + "ध्यान-अवस्था", "abhiññaṃ": OM + "उच्च ज्ञान",
    "viññāṇañcāyatanavipākassa": OM + "अनंत चेतना के क्षेत्र के कर्म-फल रूपी मन के लिए",
    "nevasaññānāsaññāyatanavipākassa": OM + "न पहचान न अ-पहचान के क्षेत्र के कर्म-फल रूपी मन के लिए",
})
_SENSE = {"cakkhu": ("आँख", "cakkh"), "sota": ("कान", "sot"), "ghāna": ("नाक", "ghān"), "jivhā": ("जीभ", "jivh"),
          "kāya": ("शरीर", "kāy")}
for _p, (_h, _s) in _SENSE.items():
    PH[_p + "viññāṇaṃ"] = FS + f"{_h} की चेतना"
    PH[_p + "viññāṇassa"] = OF + f"{_h} की चेतना के लिए"
    PH[_p + "viññāṇasahagataṃ ekaṃ khandhaṃ"] = OM + f"{_h} की चेतना के साथ होने वाले एक समूह"
    PH[_p + "viññāṇasahagato eko khandho"] = MS + f"{_h} की चेतना के साथ होने वाला एक समूह"
    PH[_p + "viññāṇasahagatānaṃ khandhānaṃ"] = OM + f"{_h} की चेतना के साथ होने वाले समूहों के लिए"
    PH[_p + "viññāṇasahagatā khandhā"] = MP + f"{_h} की चेतना के साथ होने वाले समूह"
    PH[_p + "viññāṇasahagato"] = f"{_h} की चेतना के साथ होने वाला"
    PH[_p + "viññāṇasahagataṃ"] = f"{_h} की चेतना के साथ होने वाले"
    PH[_s + "āyatanaṃ"] = MS + f"{_h} का इंद्रिय-क्षेत्र"
    PH[_s + ("indriyaṃ" if _p != "jivhā" else "indriyaṃ")] = FS + f"{_h} की क्षमता"
PH["jivhindriyaṃ"] = FS + "जीभ की क्षमता"
PH["cakkhundriyaṃ"] = FS + "आँख की क्षमता"
PH["kāyindriyaṃ"] = FS + "शरीर की क्षमता"
PH["sotindriyaṃ"] = FS + "कान की क्षमता"
PH["ghānindriyaṃ"] = FS + "नाक की क्षमता"
for _p, _h in (("rūp", "दृश्य रूप"), ("sadd", "ध्वनि"), ("gandh", "गंध"), ("ras", "स्वाद"), ("phoṭṭhabb", "स्पर्श")):
    PH[_p + "āyatanaṃ"] = MS + f"{_h} का इंद्रिय-क्षेत्र"
_ORD = {"paṭham": ("पहला", "पहले"), "dutiy": ("दूसरा", "दूसरे"), "tatiy": ("तीसरा", "तीसरे"),
        "catutth": ("चौथा", "चौथे")}
for _o, (_d, _ob) in _ORD.items():
    for _n, _nh in (("magg", "मार्ग"), ("jhān", "ध्यान")):
        PH[f"{_o}o {_n}o"] = MS + f"{_d} {_nh}"
        PH[f"{_o}aṃ {_n}aṃ"] = MS + f"{_d} {_nh}"
        PH[f"{_o}assa {_n}assa"] = OM + f"{_ob} {_nh} के लिए"
        PH[f"{_o}assa {_n}assa parikammaṃ"] = FS + f"{_ob} {_nh} की प्रारंभिक तैयारी"
    PH[f"{_o}assa"] = OM + f"{_ob} के लिए"
PH["nevasaññānāsaññāyatanassa parikammaṃ"] = FS + "न पहचान न अ-पहचान के क्षेत्र की प्रारंभिक तैयारी"
for _k in ("ākāsānañcāyatanakusalaṃ", "ākiñcaññāyatanakusalaṃ", "ākāsānañcāyatanakiriyaṃ", "ākiñcaññāyatanakiriyaṃ"):
    PH[_k] = MS + S.SUBJ[_k][0]
for _k in ("viññāṇañcāyatanakusalassa", "nevasaññānāsaññāyatanakusalassa", "viññāṇañcāyatanavipākassa ca, kiriyassa ca",
           "viññāṇañcāyatanakiriyassa", "nevasaññānāsaññāyatanakiriyassa"):
    PH[_k] = OM + S.DAT[_k]
PH["nirodhā vuṭṭhahantassa nevasaññānāsaññāyatanaṃ"] = \
    "समाप्ति की ध्यान-अवस्था से बाहर आने वाले व्यक्ति में " + MS + "न पहचान न अ-पहचान का क्षेत्र"

# condition words inside clauses (ablatives in chains are handled by CH)
COND_ABL = dict(S.P_ABL)
COND_ABL.update(S.P_NABL)

# compound tails of item words: '‹key›_tail'
TAIL = {
    "acittasamaṅgissa": ("@", OM + "मन से युक्त व्यक्ति के"),
    "cittasamaṅgissa": ("@", OM + "मन से युक्त व्यक्ति के"),
    "ādhipati": ("@", FS + "प्रधानता"),
    "apaṭisandhi": ("@", MS + "पुनर्जन्म"),
}

# object verbs: Pāli verb phrase -> (postposition after the object, Hindi verb)
OBJV = {
    "paccavekkhati": ("पर", "पुनः विचार करता है"), "paccavekkhanti": ("पर", "पुनः विचार करते हैं"),
    "jānāti": ("को", "जानता है"), "jānanti": ("को", "जानते हैं"),
    "aniccato dukkhato anattato vipassati": ("को", S.ANICCA + " " + S.VIPASSATI["s"]),
    "aniccato dukkhato anattato vipassanti": ("को", S.ANICCA + " " + S.VIPASSATI["p"]),
    "assādeti abhinandati": ("का", "रस लेता है, {p} आनंद लेता है"),
    "assādenti abhinandanti": ("का", "रस लेते हैं, {p} आनंद लेते हैं"),
    "assādeti": ("का", "रस लेता है"), "assādenti": ("का", "रस लेते हैं"),
    "garuṃ katvā": ("को", "महत्व देकर"),
    "aniccato": ("को", "अनित्य"),
    "passati": ("को", "देखता है"), "passanti": ("को", "देखते हैं"),
    "suṇāti": ("को", "सुनता है"), "suṇanti": ("को", "सुनते हैं"),
}
OBJV_ALT = "|".join(re.escape(k) for k in sorted(OBJV, key=len, reverse=True))
OBJV_RE = re.compile(r"^(?P<pre>.*?)(?P<ins> (?:‹\w+› |duṭṭhena )?cittena)? ?(?P<v>" + OBJV_ALT + r")$")

PH_KEYS_BY_LEN = None


def build_ph_index():
    global PH_KEYS_BY_LEN
    PH_KEYS_BY_LEN = sorted({len(k.split(" ")) for k in PH}, reverse=True)


# ---------------------------------------------------------------- notes, headings, counts

KT = "हितकर वाले तीन के वर्गीकरण"          # kusalattika, oblique
GAN = {  # the kinds of count named in the notes
    "gaṇanā": "गणना", "paccayagaṇanā": "कारणों की गणना", "paccanīyagaṇanā": "नकारात्मक क्रम की गणना",
    "anulomapaccanīyagaṇanā": "सकारात्मक-नकारात्मक क्रम की गणना",
    "paccanīyānulomagaṇanā": "नकारात्मक-सकारात्मक क्रम की गणना",
    "paṭiccagaṇanā": "निर्भरता के खंड की गणना",
}
NOTE = {  # Pāli inside the parentheses -> Hindi inside
    "saṃkhittaṃ": "संक्षिप्त", "Saṃkhittaṃ.": "संक्षिप्त।", "saṃkhittaṃ.": "संक्षिप्त।",
    "mūlakaṃ saṃkhittaṃ": "शृंखला संक्षिप्त है",
    "saṃkhittaṃ. Sabbāni padāni vitthāretabbāni.": "संक्षिप्त। सभी पदों का विस्तार करना चाहिए।",
    "Sabbāni padāni vibhajitabbāni.": "सभी पदों का विश्लेषण करना चाहिए।",
    "Saṃkhittaṃ. Sabbāni padāni vitthāretabbāni.": "संक्षिप्त। सभी पदों का विस्तार करना चाहिए।",
    "ārammaṇapaccayasadisaṃ": "विषय-कारण के समान", "sahajātasadisaṃ": "सह-उत्पत्ति-कारण के समान",
    "anantarasadisaṃ": "निकटता-कारण के समान", "anantarapaccayasadisaṃ": "निकटता-कारण के समान",
    "naārammaṇapaccayasadisaṃ": "विषय-कारण के अभाव के समान", "nakammapaccayasadisaṃ": "कर्म-कारण के अभाव के समान",
    "hetupaccayasadisā nava": "मूल-कारण के समान नौ",
    "anantarasadisaṃ. Saṃkhittaṃ": "निकटता-कारण के समान। संक्षिप्त",
    "Saṃkhittaṃ. Yathā anulomaṃ sahajātasadisaṃ.": "संक्षिप्त। जैसे सकारात्मक क्रम में, सह-उत्पत्ति-कारण के समान।",
    "aññamaññampi nissayampi sahajātapaccayasadisaṃ":
        "परस्पर-कारण और आश्रय-कारण भी सह-उत्पत्ति-कारण के समान हैं",
    "Natthi-vigataṃ anantarasadisaṃ, avigataṃ atthisadisaṃ.":
        "अनुपस्थिति-कारण और विलीनता-कारण निकटता-कारण के समान हैं, अविलीनता-कारण उपस्थिति-कारण के समान है।",
    "sahajātaṃ sabbaṃ hetupaccayasadisaṃ": "सह-उत्पत्ति-कारण पूरा मूल-कारण के समान है",
    "sahajāte idaṃ nānākaraṇaṃ": "सह-उत्पत्ति-कारण में यह अंतर है",
    "idaṃ nānattaṃ": "यह अंतर है",
    "Avipākaṃ – 4": "कर्म-फल-कारण के बिना – 4", "Savipākaṃ – 5": "कर्म-फल-कारण सहित – 5",
    "vitthārena gaṇetabbaṃ": "विस्तार से गिनना चाहिए", "Vitthārena gaṇetabbaṃ.": "विस्तार से गिनना चाहिए।",
    "Ekā pañhā.": "एक प्रश्न।", "Satta pañhā": "सात प्रश्न", "Terasa pañhā": "तेरह प्रश्न",
    "paṭisandhi paripuṇṇaṃ": "पुनर्जन्म परिपूर्ण है",
    "adhipatiyā paṭisandhi natthi": "प्रधानता-कारण में पुनर्जन्म नहीं है",
    "adhipatiyā paṭisandhikkhaṇe natthi": "प्रधानता-कारण में पुनर्जन्म का क्षण नहीं है",
    "nādhipati paripuṇṇaṃ paṭisandhikaṃ": "प्रधानता-कारण का अभाव पुनर्जन्म सहित परिपूर्ण है",
    "napacchājātampi naāsevanampi paripuṇṇaṃ paṭisandhikaṃ":
        "पश्चात्-उत्पत्ति-कारण का अभाव और पुनरावृत्ति-कारण का अभाव भी पुनर्जन्म सहित परिपूर्ण हैं",
    "Dukkhāya vedanāya sampayuttapaṭisandhi na labbhati.": "दुःखद अनुभूति से जुड़ा पुनर्जन्म लागू नहीं होता।",
    "Paṭisandhipi imesaṃ tiṇṇannaṃ kātabbā.": "इन तीनों में पुनर्जन्म भी शामिल करना चाहिए।",
    "paṭisandhi kātabbā {kātabbaṃ (sī.)}.": "पुनर्जन्म शामिल करना चाहिए [वर्तनी-भेद (Sī.): kātabbaṃ]।",
    "saddhāpañcamakesu \"mānaṃ jappeti, diṭṭhiṃ gaṇhātī\"ti kātabbaṃ, avasesesu na kātabbaṃ":
        "श्रद्धा आदि पाँच में “अहंकार पालता है, दृष्टि ग्रहण करता है” शामिल करना चाहिए, बाकी में शामिल नहीं करना चाहिए",
    "Paccayavāropi nissayavāropi sadiso": "कारण का खंड और आश्रय का खंड भी समान हैं",
    "Saṃsaṭṭhavāropi sampayuttavāropi sadiso.": "घुले-मिले होने का खंड और जुड़ाव का खंड भी समान हैं।",
    "Paṭiccavāropi sahajātavāropi sadiso.": "निर्भरता का खंड और सह-उत्पत्ति का खंड भी समान हैं।",
    "Sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi vitthāretabbo.":
        "सह-उत्पत्ति का खंड, कारण का खंड, आश्रय का खंड, घुले-मिले होने का खंड और जुड़ाव का खंड भी "
        "विस्तार से देना चाहिए।",
    "Catuvīsatipaccayā vitthāretabbā, avigatapaccayā.": "चौबीस कारणों का विस्तार करना चाहिए, अविलीनता-कारण तक।",
    "Atthipaccayā… natthipaccayā… vigatapaccayā… avigatapaccayā…pe….":
        "उपस्थिति-कारण से… अनुपस्थिति-कारण से… विलीनता-कारण से… अविलीनता-कारण से…।",
    "Yathā kusalattikaṃ, evaṃ gaṇetabbaṃ.": "जैसे हितकर वाला तीन का वर्गीकरण है, वैसे ही गिनना चाहिए।",
    "Yathā kusalattike, evaṃ vitthāretabbaṃ": f"जैसे {KT} में है, वैसे ही विस्तार करना चाहिए",
    "Yathā kusalattike vibhattaṃ, evaṃ vibhajitabbaṃ.":
        f"जैसे {KT} में विश्लेषण किया गया है, वैसे ही विश्लेषण करना चाहिए।",
    "Yathā kusalattike sajjhāyamaggena gaṇitaṃ, evaṃ idhāpi gaṇetabbaṃ.":
        f"जैसे {KT} में पाठ के क्रम से गिना गया है, वैसे ही यहाँ भी गिनना चाहिए।",
    "Yathā kusalattikassa paṭiccavāro sajjhāyamaggena vitthārito, evaṃ vitthāretabbaṃ.":
        f"जैसे {KT} के निर्भरता के खंड का पाठ के क्रम से विस्तार किया गया है, वैसे ही विस्तार करना चाहिए।",
    "Yathā kusalattike paccanīyavāro vitthārito, evaṃ vitthāretabbo.":
        f"जैसे {KT} में नकारात्मक क्रम के खंड का विस्तार किया गया है, वैसे ही विस्तार करना चाहिए।",
    "Yathā kusalattike nahetumūlakaṃ gaṇitaṃ, evaṃ gaṇetabbaṃ. Yathā kusalattike paccanīyānulomaṃ vitthāritaṃ, "
    "evaṃ idaṃ vitthāretabbaṃ.":
        f"जैसे {KT} में मूल-कारण के अभाव से शुरू होने वाली शृंखला गिनी गई है, वैसे ही गिनना चाहिए। "
        f"जैसे {KT} में नकारात्मक-सकारात्मक क्रम का विस्तार किया गया है, वैसे ही इसका विस्तार करना चाहिए।",
    "Yathā kusalattike anulomapaccanīyagaṇanā vitthāritā evaṃ vitthāretabbaṃ. Asammohantena eso sajjhāyamaggo.":
        f"जैसे {KT} में सकारात्मक-नकारात्मक क्रम की गणना का विस्तार किया गया है, वैसे ही विस्तार करना चाहिए। "
        "बिना भ्रमित हुए, यह पाठ का क्रम है।",
    "Yathā kusalattikassa gaṇanā sajjhāyamaggena gaṇitā, evaṃ gaṇetabbā. Kusalattikassa gaṇanato upādinnattike "
    "gaṇanā gambhīrā sukhumatarā ca, evaṃ kātūna asammohantena gaṇetabbaṃ.":
        f"जैसे {KT} की गणना पाठ के क्रम से की गई है, वैसे ही गिनना चाहिए। {KT} की गणना से कर्म से उत्पन्न "
        "परिघटनाओं वाले तीन के वर्गीकरण में गणना गहरी और अधिक सूक्ष्म है, ऐसा करके बिना भ्रमित हुए गिनना चाहिए।",
    "Yathā kusalattikassa paccanīyagaṇanā gaṇitā, evaṃ idampi asammuyhantena sabbaṃ mūlakaṃ gaṇetabbaṃ "
    "{gahetabbaṃ (syā.)}.":
        f"जैसे {KT} की नकारात्मक क्रम की गणना की गई है, वैसे ही इसमें भी पूरी शृंखला को बिना भ्रमित हुए "
        "गिनना चाहिए [पाठभेद (Syā.): gahetabbaṃ]।",
    "Yathā kusalattike pañhāvārassa anulomagaṇanā gaṇitā, evaṃ vitthāretabbā.":
        f"जैसे {KT} में प्रश्नों के खंड की सकारात्मक क्रम की गणना की गई है, वैसे ही विस्तार करना चाहिए।",
}
# «Yathā kusalattike/kusalattikassa <count> [<done>], evaṃ [idampi] [sajjhāyamaggena] <verb>.» composed
_DONE = {"": "है", "gaṇitā": "की गई है", "vitthāritā": "का विस्तार किया गया है", "vibhattā": "का विश्लेषण किया गया है"}
_DO = {"gaṇetabbaṃ": "गिनना चाहिए", "gaṇetabbā": "गिनना चाहिए", "vitthāretabbā": "विस्तार करना चाहिए",
       "vitthāretabbaṃ": "विस्तार करना चाहिए", "vitthāratabbaṃ": "विस्तार करना चाहिए",  # spelling slip, as meant
       "vibhajitabbaṃ": "विश्लेषण करना चाहिए"}
YATHA_RE = re.compile(r"Yathā (kusalattike|kusalattikassa) (\w+)( sajjhāyamaggena)?(?: (gaṇitā|vitthāritā|vibhattā))?"
                      r"(,?) evaṃ( idampi)? (\w+)(\.?)")


def note_hi(t):
    if t in NOTE:
        return NOTE[t]
    m = YATHA_RE.fullmatch(t)
    if not m or m.group(2) not in GAN or m.group(7) not in _DO:
        raise Untranslated("note: " + t)
    loc, g, saj, done, comma, idampi, verb, dot = m.groups()
    lh = f"{KT} में" if loc == "kusalattike" else f"{KT} की"
    x = GAN[g] + (" पाठ के क्रम से" if saj else "")
    if done == "gaṇitā":
        x += " की गई है"
    elif done:
        x += " " + _DONE[done]
    else:
        x += " है"
    return f"जैसे {lh} {x}{comma} वैसे ही{' इसे भी' if idampi else ''} {_DO[verb]}{'।' if dot else ''}"

HEAD = dict(S.HEAD)
HEAD.update({
    "Vedanāttikaṃ": "अनुभूति वाला तीन का वर्गीकरण",
    "Vipākattikaṃ": "कर्म-फल वाला तीन का वर्गीकरण",
    "Upādinnattikaṃ": "कर्म से उत्पन्न परिघटनाओं वाला तीन का वर्गीकरण",
    "Saṃkiliṭṭhattikaṃ": "क्लेशों से मलिन परिघटनाओं वाला तीन का वर्गीकरण",
    "Sahajātavāro": "सह-उत्पत्ति का खंड", "Paccayavāro": "कारण का खंड", "Nissayavāro": "आश्रय का खंड",
    "Saṃsaṭṭhavāro": "घुले-मिले होने का खंड", "Sampayuttavāro": "जुड़ाव का खंड",
    "Paccanīyuddhāro": "नकारात्मक क्रम के लिए कारणों की छँटाई",
    "Anulomaṃ": "सकारात्मक क्रम", "Paccanīyaṃ.": "नकारात्मक क्रम।",
    "Nahetumūlakaṃ.": "मूल-कारण के अभाव से शुरू होने वाली शृंखला।",
    "1-4. Paccayacatukkaṃ": "1-4. कारणों के चार क्रम",
    "2-6 Sahajāta-paccaya-nissaya-saṃsaṭṭha-sampayuttavāro":
        "2-6 सह-उत्पत्ति का खंड, कारण का खंड, आश्रय का खंड, घुले-मिले होने का खंड और जुड़ाव का खंड",
    "Sabhāgaṃ": "साथी कारण", "Ghaṭanā": "संयोजन",
    "Sāmaññaghaṭanā": "सामान्य संयोजन", "Hetughaṭanā": "मूल-कारण के संयोजन",
    "Hetusāmaññaghaṭanā": "मूल-कारण के सामान्य संयोजन",
    "Pakiṇṇakaghaṭanā": "फुटकर संयोजन",
    "Saindriya-maggaghaṭanā": "क्षमता-कारण और मार्ग-कारण सहित संयोजन",
    "Sādhipati-indriya-maggaghaṭanā": "प्रधानता-कारण, क्षमता-कारण और मार्ग-कारण सहित संयोजन",
    "Catuvīsakaṃ": "चौबीस कारणों का मेल",
    "(sakammaṃ)": "(कर्म-कारण सहित)", "(saupanissayaṃ)": "(प्रबल आश्रय-कारण सहित)",
})
_COUNT_HEAD = {"Dukaṃ": "दो", "Tikaṃ": "तीन", "Catukkaṃ": "चार", "Pañcakaṃ": "पाँच", "Chakkaṃ": "छह",
               "Sattakaṃ": "सात", "Aṭṭhakaṃ": "आठ", "Navakaṃ": "नौ", "Dasakaṃ": "दस", "Ekādasakaṃ": "ग्यारह",
               "Dvādasakaṃ": "बारह", "Terasakaṃ": "तेरह", "Tevīsakaṃ": "तेईस", "Bāvīsakaṃ": "बाईस"}
for _p, _h in _COUNT_HEAD.items():
    HEAD[_p] = f"{_h} कारणों का मेल"
STEM_CAP = {k[0].upper() + k[1:]: k for k in S.KEYS}


def cond_seq(s):
    """'Natthi-vigatāvigata' / 'Anantara-samanantara' -> list of condition keys (greedy, sandhi ā = a+a)."""
    s = s.lower().replace("-", "").replace(" ", "").replace("ṃ", "")
    keys = sorted(S.KEYS, key=len, reverse=True)
    out = []
    i = 0
    pending = False  # the previous key ended in a sandhi 'ā' = a + a
    while i < len(s):
        for k in keys:
            if pending:
                if k[0] == "a" and s.startswith(k[1:], i):
                    out.append(k)
                    i += len(k) - 1
                    pending = False
                    break
                continue
            if s.startswith(k, i):
                out.append(k)
                i += len(k)
                break
            if k.endswith("a") and s.startswith(k[:-1] + "ā", i) and i + len(k) < len(s):
                out.append(k)
                i += len(k)
                pending = True
                break
            if k.endswith("a") and s[i:] == k[:-1]:  # '…jāt' before 'ādi'
                out.append(k)
                i += len(k) - 1
                break
        else:
            raise Untranslated("cond_seq: " + s[i:])
    return out


def join_and(xs):
    return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " और " + xs[-1]


def heading_body(b):
    if b in HEAD:
        return HEAD[b]
    m = re.fullmatch(r"(.*?) (\(\d+\))", b)
    if m:
        return heading_body(m.group(1)) + " " + m.group(2)
    m = re.fullmatch(r"(\S+) (\(\w+\))", b)
    if m and m.group(2) in HEAD:
        return heading_body(m.group(1)) + " " + HEAD[m.group(2)]
    neg = b.startswith(("Na", "No")) and not b.startswith("Natthi")
    m = re.fullmatch(r"(.+?)paccay(?:o|ā)", b)
    if m:  # single or combined condition heading
        parts = m.group(1).split("-")
        names = []
        for p in parts:
            pn = p[2:] if neg and p[:2].lower() in ("na", "no") else p
            ks = cond_seq(pn)
            names += [(S.NNAME[k] if neg else S.NAME[k]) for k in ks]
        return join_and(names)
    m = re.fullmatch(r"(.+?)paccayādi", b)
    if m:
        p = m.group(1)
        if neg:
            return S.NNAME[cond_seq(p[2:])[0]] + " आदि"
        return join_and([S.NAME[k] for k in cond_seq(p)]) + " आदि"
    m = re.fullmatch(r"(.+?)(?:ādi)?dukāni", b)
    if m:
        p = m.group(1)
        if neg:
            return f"{S.NAME[cond_seq(p[2:])[0]]} के अभाव आदि के साथ दो कारणों के मेल"
        return f"{S.NAME[cond_seq(p)[0]]} आदि के साथ दो कारणों के मेल"
    m = re.fullmatch(r"(.+?)dukaṃ", b)
    if m:
        p = m.group(1)
        return S.NDUKA[cond_seq(p[2:])[0]] if neg else S.DUKA[cond_seq(p)[0]]
    m = re.fullmatch(r"(.+?)(ādi)?sabhāgaṃ", b)
    if m:
        return S.NAME[cond_seq(m.group(1))[0]] + (" आदि" if m.group(2) else "") + " के साथी कारण"
    m = re.fullmatch(r"(.+?)ghaṭanā", b)
    if m:
        return S.NAME[cond_seq(m.group(1))[0]] + " के संयोजन"
    raise Untranslated("heading: " + b)


def heading_hi(line):
    m = re.fullmatch(r"(#+) (\*?)(.*?)(\*?)", line)
    hashes, st, body, en = m.groups()
    return f"{hashes} {st}{heading_body(body)}{en}"


NUMW = dict(S.NUM)
NUMW.update({"dasa": "दस", "ekādasa": "ग्यारह", "dvādasa": "बारह", "terasa": "तेरह", "cuddasa": "चौदह",
             "pannarasa": "पंद्रह", "soḷasa": "सोलह", "sattarasa": "सत्रह", "aṭṭhārasa": "अठारह",
             "vīsati": "बीस", "bāvīsati": "बाईस", "tevīsati": "तेईस", "tevīsa": "तेईस", "catuvīsati": "चौबीस",
             "ekā": "एक", "tisso": "तीन", "ekavīsati": "इक्कीस"})
LOCW = dict(S.P_LOC)
LOCW.update(S.P_NLOC)
ABLW = dict(S.P_ABL)
ABLW.update(S.P_NABL)
GHAT_RE = re.compile(r"^([a-zāīūṃṅñṭḍṇḷ -]+?)(?:nti|īti)$")


def ghatana_hi(word):
    m = GHAT_RE.match(word)
    stems = m.group(1)
    if stems.endswith("adhipat"):  # adhipatīti
        stems += "i"
    return join_and([S.NAME[k] for k in cond_seq(stems)]) + " के संयोजन"


COUNT_TOK = re.compile(r"(…pe…|…|, |\. |; | |\.$)")


def is_count_line(text):
    """text already lowercased, notes protected as \x05n\x06 tokens"""
    body = re.sub("\x05\\d+\x06|\\(\\d+\\)|=\\d+", " ", text)
    toks = [t for t in COUNT_TOK.split(body) if t and not COUNT_TOK.fullmatch(t) and t.strip()]
    if not toks:
        return False
    for t in toks:
        t = t.strip()
        if t in NUMW or t in LOCW or t in ABLW or "-" in t and GHAT_RE.match(t):
            continue
        if GHAT_RE.match(t) and t.endswith(("nti", "īti")):
            try:
                cond_seq(GHAT_RE.match(t).group(1))
                continue
            except Untranslated:
                return False
        if re.fullmatch(r"[a-zāīūṃṅñṭḍṇḷ-]+paccayā", t):  # hyphenated negative chain na-…-paccayā
            continue
        return False
    return True


def count_hi(text):
    """counting lines: like the sample's count_hi, with numbers beyond nine and ghaṭanā lists"""
    toks = [t for t in re.split(r"(…pe…|…|, |\. |; | |\.$)", text) if t]
    out = []
    for i, t in enumerate(toks):
        prev = toks[i - 1] if i else ""
        if t == " ":
            # an ablative (or a ghaṭanā used as one) before another word takes ", "
            if prev in ABLW or prev.endswith("paccayā") and "-" in prev:
                out.append(", ")
            elif GHAT_RE.match(prev or "") and prev.endswith(("nti", "īti")) and i + 1 < len(toks) \
                    and toks[i + 1] in LOCW and toks[i + 1].startswith(("na", "no")):
                out.append(", ")
            else:
                out.append(" ")
        elif t == "…pe…":
            out.append("…")
        elif t in (". ", "."):
            out.append("। " if t == ". " else "।")
        elif t in ("…", ", ", "; "):
            out.append(t)
        elif t in ABLW:
            out.append(ABLW[t])
        elif t in LOCW:
            out.append(LOCW[t])
        elif t in NUMW:
            out.append(NUMW[t])
        elif re.fullmatch("\x05\\d+\x06|\\(\\d+\\)|=\\d+", t):
            out.append(t)
        elif t.endswith(("nti", "īti")) and GHAT_RE.match(t):
            nxt = toks[i + 2] if i + 2 < len(toks) else ""
            gh = ghatana_hi(t)
            out.append(gh + (" से" if nxt in LOCW and nxt.startswith(("na", "no")) else " में"))
        elif t.endswith("paccayā") and "-" in t:  # na-…-paccayā written as one hyphenated chain
            out.append(", ".join(S.NABL[k] for k in neg_seq(t[:-len("paccayā")])))
        else:
            raise Untranslated("count: " + t)
    return "".join(out)


LINE = {  # whole lines (lowercased initials), Pāli -> Hindi
    "paccanīyagaṇanā.": "नकारात्मक क्रम की गणना।",
    "anulomapaccanīyaṃ.": "सकारात्मक-नकारात्मक क्रम।",
    "paccanīyānulomaṃ.": "नकारात्मक-सकारात्मक क्रम।",
    "paccanīyaṃ.": "नकारात्मक क्रम।", "paccanīyaṃ": "नकारात्मक क्रम",
    "anulomaṃ.": "सकारात्मक क्रम।",
    "paṭiccavāro.": "निर्भरता का खंड।",
    "sampayuttavāro.": "जुड़ाव का खंड।",
    "anulomagaṇanā.": "सकारात्मक क्रम की गणना।",
    "anulomapaccanīyagaṇanā.": "सकारात्मक-नकारात्मक क्रम की गणना।",
    "paccanīyānulomagaṇanā.": "नकारात्मक-सकारात्मक क्रम की गणना।",
    "nahetumūlakaṃ.": "मूल-कारण के अभाव से शुरू होने वाली शृंखला।",
    "pañhāvārassa anulomaṃ.": "प्रश्नों के खंड का सकारात्मक क्रम।",
    "vedanāttikaṃ niṭṭhitaṃ.": "अनुभूति वाला तीन का वर्गीकरण समाप्त।",
    "vipākattikaṃ niṭṭhitaṃ.": "कर्म-फल वाला तीन का वर्गीकरण समाप्त।",
    "upādinnattikaṃ niṭṭhitaṃ.": "कर्म से उत्पन्न परिघटनाओं वाला तीन का वर्गीकरण समाप्त।",
    "saṃkiliṭṭhattikaṃ niṭṭhitaṃ.": "क्लेशों से मलिन परिघटनाओं वाला तीन का वर्गीकरण समाप्त।",
    "paṭṭhānapāḷi paṭhamo bhāgo niṭṭhito.": "“कारण-संबंध” का पहला भाग समाप्त।",
    "sahajātavāro.": "सह-उत्पत्ति का खंड।", "paccayavāro.": "कारण का खंड।", "nissayavāro.": "आश्रय का खंड।",
    "saṃsaṭṭhavāro.": "घुले-मिले होने का खंड।",
}

RESIDUE = collections.Counter()
EXAMPLE = {}

RESIDUE = collections.Counter()
SLIPS_SEEN = collections.Counter()


class Untranslated(Exception):
    pass


OBL_TRIGGER = {"paṭicca", "paccayā", "nissāya", "ārabbha", "upanissāya", "sahajāto", "saṃsaṭṭho", "saṃsaṭṭhā",
               "sampayutto", "sampayuttā"}
ADJ_TOKENS = {"kusale", "kusalā", "akusale", "akusalā", "kusalaṃ", "akusalaṃ"}
_TO_OBL = {"ms": "om", "mp": "om", "fs": "of", "fp": "of"}


def oblique(chunk):
    """a direct-case Hindi noun phrase before a postposition: markers -> oblique, «का/वाला» -> «के/वाले»"""
    chunk = re.sub("\x01(ms|mp|fs|fp)\x02", lambda m: MK(_TO_OBL[m.group(1)]), chunk)
    chunk = re.sub(r"(?<=\s)का(?= )", "के", chunk)
    chunk = re.sub(r"वाला(?= |$)", "वाले", chunk)
    return chunk


def words_hi(piece, state, obl_last=False):
    """greedy longest-match over the phrase table; returns Hindi with markers"""
    toks = piece.split()
    out = []
    i = 0
    while i < len(toks):
        if toks[i] in OBL_TRIGGER and out:
            out[-1] = oblique(out[-1])
        if toks[i] in ADJ_TOKENS and i + 1 < len(toks) and toks[i + 1].startswith("‹"):
            out.append(PH.get(toks[i] + "§a", PH[toks[i]]) + ",")
            i += 1
            continue
        if toks[i] == "‹vp›" and i + 1 < len(toks) and toks[i + 1].startswith("‹"):
            out.append(item_hi("vp") + ",")
            i += 1
            continue
        for n in PH_KEYS_BY_LEN:
            if i + n <= len(toks):
                key = " ".join(toks[i:i + n])
                if key in PH:
                    out.append(PH[key])
                    i += n
                    break
        else:
            if toks[i] in NUMW and toks[i] not in PH:
                out.append(NUMW[toks[i]])
                i += 1
                continue
            if toks[i] in LOCW:
                out.append(LOCW[toks[i]])
                i += 1
                continue
            t = toks[i]
            if t.startswith("‹") and t.endswith("›"):
                out.append(item_hi(t[1:-1]))
            elif t.startswith("‹") and "›_" in t:
                key, tail = t[1:].split("›_", 1)
                if tail not in TAIL:
                    raise Untranslated(t)
                adj, noun = TAIL[tail]
                out.append(item_hi(key) + " " + noun)
            elif t.startswith("\x05") or re.fullmatch(r"\(\d+\)|=\d+", t):
                out.append(t)
            elif t in COND_ABL:
                out.append(COND_ABL[t])
            else:
                raise Untranslated(t)
            i += 1
    if obl_last and out:
        out[-1] = oblique(out[-1])
    return " ".join(out)


def neg_seq(s):
    """'naārammaṇa-naadhipati-…-noatthi' (hyphens possibly missing) -> condition keys"""
    s = s.replace("-", "").replace(" ", "")
    keys = sorted(S.KEYS, key=len, reverse=True)
    out = []
    i = 0
    while i < len(s):
        if not s.startswith(("na", "no"), i):
            raise Untranslated("neg_seq: " + s[i:])
        i += 2
        for k in keys:
            if s.startswith(k, i):
                out.append(k)
                i += len(k)
                break
        else:
            raise Untranslated("neg_seq: " + s[i:])
    return out


# ---------------------------------------------------------------- clauses

OBJ_WORDS = {"taṃ", "khandhe", "kilese", "suciṇṇāni", "jhānaṃ", "maggaṃ", "phalaṃ", "nibbānaṃ", "gotrabhuṃ",
             "vodānaṃ", "cakkhuṃ", "sotaṃ", "ghānaṃ", "jivhaṃ", "kāyaṃ", "rūpe", "sadde", "gandhe", "rase",
             "phoṭṭhabbe", "vatthuṃ", "rāgaṃ", "diṭṭhiṃ", "cittaṃ", "rūpaṃ", "saddaṃ", "kusalaṃ", "akusalaṃ",
             "dosaṃ", "mohaṃ", "mānaṃ", "vicikicchaṃ", "uddhaccaṃ", "domanassaṃ", "dhamme", "rūpāni", "saddhaṃ"}
PLURAL_OBJ = {"khandhe", "kilese", "suciṇṇāni", "rūpe", "sadde", "gandhe", "rase", "phoṭṭhabbe", "dhamme", "rūpāni"}
CA_STRIP = {"khandhañca": "khandhaṃ", "vatthuñca": "vatthu", "rūpajīvitindriyañca": "rūpajīvitindriyaṃ"}


def coordinate(core):
    """'A ca B ca' -> 'A §aur B'; 'A ca B ca C ca' -> 'A §comma B §aur C' (A, B: any words before each ca)"""
    toks = core.split()
    toks2 = []
    for t in toks:
        if t in CA_STRIP:
            toks2 += [CA_STRIP[t], "ca"]
        elif t.endswith("ñca") and len(t) > 4 and t not in PH:
            b = t[:-3]
            toks2 += [b + "ṃ" if b.endswith("a") else b, "ca"]
        else:
            toks2.append(t)
    pos = [i for i, t in enumerate(toks2) if t == "ca"]
    if len(pos) < 2:
        return core
    for j, p in enumerate(pos):
        if j == len(pos) - 1:
            toks2[p] = "§pl"
        elif j == len(pos) - 2:
            toks2[p] = "§aur"
        else:
            toks2[p] = "§comma"
    return " ".join(t for t in toks2 if t).replace(" §comma", "§comma")


def obj_info(pre):
    toks = pre.split()
    while toks and toks[-1].startswith("\x05"):
        toks = toks[:-1]
    if toks and toks[-1] in OBJ_WORDS:
        return True, toks[-1] in PLURAL_OBJ
    return False, None


def clause_hi(piece, state):
    core = piece.strip()
    if not core:
        return piece
    lead = piece[: len(piece) - len(piece.lstrip())]
    trail = piece[len(piece.rstrip()):]
    if S.SHORT_RE.match(core):  # «Vatthuṃ purejātapaccayā» = «आधार पर पूर्व-उत्पत्ति-कारण से»
        return S.clause(piece)
    core = coordinate(core)
    core = core.replace("§comma", " §comma")
    if core.endswith(",") and len(core) > 1:
        return lead + clause_hi(core[:-1], state).strip() + "," + trail
    if core == "purimā purimā":
        return lead + "पहले-पहले के" + trail
    core = re.sub(r"^(pacchājātā|sahajātā) (?=\S)", r"\1§a ", core)
    # «… garuṃ katvā <rest>»: the object takes «को» before an instrumental
    m = re.fullmatch(r"(?P<pre>.*?)(?P<ins> (?:‹\w+› |duṭṭhena )?cittena)? garuṃ katvā (?P<rest>.+)", core)
    if m and obj_info(m.group("pre"))[0]:
        has, pl = obj_info(m.group("pre"))
        state["objpl"] = pl
        h = words_hi(m.group("pre"), state, obl_last=True) + " को"
        if m.group("ins"):
            h += " " + words_hi(m.group("ins").strip(), state)
        h += " महत्व देकर " + clause_hi(m.group("rest"), state).strip()
        return lead + h + trail
    m = OBJV_RE.fullmatch(core)
    if m:
        pre, ins, v = m.group("pre").strip(), m.group("ins"), m.group("v")
        postp, vh = OBJV[v]
        has, pl = obj_info(pre)
        if has:
            state["objpl"] = pl
        h = words_hi(pre, state, obl_last=has) if pre else ""
        if has:
            h += " " + postp
        if ins:
            h += " " + words_hi(ins.strip(), state)
        if "{p}" in vh:
            vh = vh.format(p="उनमें" if state.get("objpl") else "उसमें")
        if not has and postp == "का":  # elided object of assādeti
            vh = ("उनका " if state.get("objpl") else "उसका ") + vh
        h = (h + " " + vh).strip()
        return lead + h + trail
    return lead + words_hi(core, state) + trail


# ---------------------------------------------------------------- the line

SIG_KIND = {"{nānākhaṇikā (ka.)}": "वर्तनी-भेद"}
NOTE_RE = re.compile(r"\(((?:[^()]|\([^()]*\))*?[A-Za-zāīūṃ](?:[^()]|\([^()]*\))*)\)")
COND_WORD = "|".join(re.escape(k) for k in sorted(ABLW, key=len, reverse=True))
CHAIN_RE = re.compile(r"\b(uppajjati|uppajjanti) ((?:" + COND_WORD + r")(?:(?:…pe…|…| |\x05\d+\x06)+(?:"
                      + COND_WORD + r"))*)")
PAN_RE = re.compile(r"\b(na )?(" + "|".join(sorted(S.KEYS, key=len, reverse=True)) + r")paccayena paccayo\b")
PROTECT = [  # applied to the lowercased line before the items become tokens
    (r"kusalākusale niruddhe vipāko tadārammaṇatā uppajjati",
     "हितकर और हानिकर के समाप्त होने पर " + S.VIPAKA_TADARAMMANA),
    (r"kusale niruddhe vipāko tadārammaṇatā uppajjati", S.CLAUSE["kusale niruddhe vipāko tadārammaṇatā uppajjati"]),
    (r"akusale niruddhe vipāko tadārammaṇatā uppajjati",
     S.CLAUSE["akusale niruddhe vipāko tadārammaṇatā uppajjati"]),
    (r"kusalākusalaṃ kammaṃ vipākassa", MS + "हितकर और हानिकर कर्म, कर्म-फल के लिए"),
    (r"kusalaṃ kammaṃ vipākassa", MS + "हितकर कर्म, कर्म-फल के लिए"),
    (r"vipāko ca ubhayañca", FS + "कर्म-फल रूपी परिघटना और दोनों"),
    (r"akusalaṃ kammaṃ vipākassa", MS + "हानिकर कर्म, कर्म-फल के लिए"),
]
NANA_RE = re.compile(r"(?:(?:iddhividha|cetopariya|pubbenivāsānussati|yathākammūpaga|anāgataṃsa)ñāṇassa,? )+"
                     r"(?:(?:iddhividha|cetopariya|pubbenivāsānussati|yathākammūpaga|anāgataṃsa)ñāṇassa|āvajjanāya)")


def chain_hi(ch):
    toks = [t for t in re.split(r"(…pe…|…| |\x05\d+\x06)", ch) if t]
    out = []
    for i, t in enumerate(toks):
        if t == " ":
            prev = toks[i - 1]
            nxt = toks[i + 1] if i + 1 < len(toks) else ""
            out.append(", " if prev in ABLW and nxt in ABLW else " ")
        elif t == "…pe…":
            out.append("…")
        elif t in ABLW:
            out.append(ABLW[t])
        else:
            out.append(t)
    return "".join(out)


def finish(s, store, state):
    for _ in range(4):
        s = re.sub("\x05(\\d+)\x06", lambda m: store[int(m.group(1))], s)
    s = resolve(s, state)
    for a, b in (("उस को", "उसे"), ("उस का", "उसका"), ("उन को", "उन्हें"), ("उन का", "उनका"), (" ,", ","),
                 ("  ", " "), ("?।", "?")):
        s = s.replace(a, b)
    # a subject touching the identical noun in the dative takes a comma (formulas §0)
    s = re.sub(r"(?<![ऀ-ॿ-])((?:[ऀ-ॿ-]+ ){0,3}[ऀ-ॿ-]+) \1 के लिए", r"\1, \1 के लिए", s)
    return s


def translate_line(body):
    store = []
    state = {}

    def keep(h):
        store.append(h)
        return f"\x05{len(store) - 1}\x06"

    text = body
    # variants
    def var(m):
        v = m.group(0)
        if v in NOTE_VARIANT:
            return v
        kind = SIG_KIND.get(v, "पाठभेद")
        return keep(S.variant_hi(v, kind))
    text = re.sub(r"\{[^{}]*\}", var, text)
    # notes
    text = NOTE_RE.sub(lambda m: keep("(" + note_hi(m.group(1)) + ")"), text)
    text = S.lower_initials(text)
    if text in LINE:
        return LINE[text]
    for a in ("na adhipatiyā", "na sampayutte"):
        if a in text:
            SLIPS_SEEN[a] += 1
            text = text.replace(a, a.replace(" ", ""))
    text = re.sub(r" -|- ", "-", text) if is_count_line(re.sub(r" -|- ", "-", text)) else text
    if is_count_line(text):
        return finish(count_hi(text), store, state)
    for rx, h in PROTECT:
        text = re.sub(r"(?<![\w])" + rx, lambda m, h=h: keep(h), text)
    text = NANA_RE.sub(lambda m: keep(OM + S.dat_list(m.group(0))), text)
    for a, b in SLIP_FIX.items():
        if a in text:
            SLIPS_SEEN[a] += 1
            text = text.replace(a, b)
    for a in JOIN_CA:
        text = text.replace(a, a.replace(" ", "_"))
    text = items_to_tokens(text)
    text = re.sub(r"(‹\w+›) §dat ca (‹\w+›) §dat ca (‹\w+›) §dat ca(?: dhammassa)?(?! kāyassa)",
                  r"\1 dhammaṃ §comma \2 dhammaṃ §aur \3 dhammassa", text)
    text = re.sub(r"(‹\w+›) §dat ca (‹\w+›) §dat ca(?: dhammassa)?(?! kāyassa)", r"\1 dhammaṃ §aur \2 dhammassa", text)
    text = text.replace(" §dat", "")
    text = re.sub(r"purejātassa imassa (‹\w+›) ca kāyassa", r"§aur purejātassa imassa \1 kāyassa", text)
    text = re.sub(r"(‹\w+›) ca (‹\w+›) ca (‹\w+›) ca dhamm(aṃ|assa)\b",
                  r"\1 dhammaṃ §comma \2 dhammaṃ §aur \3 dhamm\4", text)
    text = re.sub(r"(‹\w+›) ca (‹\w+›) ca dhamm(aṃ|assa)\b", r"\1 dhammaṃ §aur \2 dhamm\3", text)
    text = re.sub(r"\bdhamm(o|ā)(?= (?:(?:‹\w+›|ca|dhammaṃ|§aur|§comma) )+dhammassa\b)", r"dhamm\1§c", text)
    text = CHAIN_RE.sub(lambda m: keep(chain_hi(m.group(2))) + " " + m.group(1), text)
    text = PAN_RE.sub(lambda m: keep(V(("NP:" if m.group(1) else "P:") + m.group(2))), text)
    if "paccayena paccayo" in body or "ārammaṇādhipati" in body:
        text = re.sub(r"\banulomaṃ\b", "anulomaṃ§m", text)
    text = re.sub(r"(‹\w+›) ca (‹\w+›) ca(?=…)", r"\1 dhammaṃ §aur \2 dhammaṃ", text)
    pieces = re.split(r"( – |; |, |,(?=…)|\. |…pe…|…|\.$)", text)
    out = []
    for p in pieces:
        if p in (" – ", "; ", ", ", "…", ","):
            out.append(p)
        elif p == ". ":
            out.append("। ")
        elif p == ".":
            out.append("।")
        elif p == "…pe…":
            out.append("…")
        elif p:
            try:
                out.append(clause_hi(p, state))
            except Untranslated as e:
                raise Untranslated(f"{e} @ {p.strip()[:80]}")
    return finish("".join(out), store, state)


SLIP_FIX = {  # pure spelling / spacing slips, rendered as meant (listed in the report)
    "nevavipākanavipākadhamma-dhammo": "nevavipākanavipākadhammadhammo",
    "sappayuttakānaṃ": "sampayuttakānaṃ",
    "paṭisandhikhaṇe": "paṭisandhikkhaṇe",
    "tayokhandhā": "tayo khandhā",
    "na adhipatiyā": "naadhipatiyā",
    "na adhipatipaccayā": "naadhipatipaccayā",
    "pakatūnissayo": "pakatūpanissayo",
    "vippassanti": "vipassanti", "vippassati": "vipassati",
}
JOIN_CA = ["cittasamuṭṭhānañca rūpaṃ", "cittasamuṭṭhānānañca rūpānaṃ", "kaṭattā ca rūpaṃ", "kaṭattā ca rūpānaṃ"]
PH["cittasamuṭṭhānañca rūpānaṃ"] = PH["cittasamuṭṭhānānañca rūpānaṃ"]  # agreement slip in 1-03, Hindi grammatical
JOIN_CA.append("cittasamuṭṭhānañca rūpānaṃ")
PH.update({
    "‹vp› tadārammaṇatā": MS + "कर्म-फल उसी विषय को लेकर", "tadārammaṇatā": "उसी विषय को लेकर",
    "kusalākusale niruddhe": "हितकर और हानिकर के समाप्त होने पर", "kusale niruddhe": "हितकर के समाप्त होने पर",
    "akusale niruddhe": "हानिकर के समाप्त होने पर",
})
OBJV["assādenti abhinandati"] = ("का", "रस लेते हैं, {p} आनंद लेते हैं")  # number slip in 1-03, Hindi plural
OBJV_ALT = "|".join(re.escape(k) for k in sorted(OBJV, key=len, reverse=True))
OBJV_RE = re.compile(r"^(?P<pre>.*?)(?P<ins> (?:‹\w+› |duṭṭhena )?cittena)? ?(?P<v>" + OBJV_ALT + r")$")
PH["purejāta"] = S.NAME["purejāta"]
for _o in ("cittasamuṭṭhānaṃ rūpaṃ kaṭattārūpaṃ upādārūpaṃ", "cittasamuṭṭhānaṃ rūpaṃ upādārūpaṃ",
           "kaṭattārūpaṃ upādārūpaṃ"):
    PH[_o] = MS + S.OBJ_P[_o]
PH["kāyikaṃ sukhaṃ kāyikaṃ dukkhaṃ"] = MS + "शारीरिक सुख और शारीरिक दुःख"
for _a in JOIN_CA:
    PH[_a.replace(" ", "_")] = PH[_a]
NOTE_VARIANT = {"{kātabbaṃ (sī.)}", "{gahetabbaṃ (syā.)}"}  # kept inside their notes (see NOTE)


# ---------------------------------------------------------------- files

PALI_DIR, OUT_DIR = S.PALI_DIR, S.OUT_DIR
ID_RE = S.ID_RE


def build_file(stem, write=True):
    src = os.path.join(PALI_DIR, stem + ".md")
    lines = open(src, encoding="utf-8").read().split("\n")
    out = []
    errors = 0
    for ln in lines:
        if not ln.strip():
            if out and out[-1] != "":
                out.append("")
            continue
        m = ID_RE.search(ln)
        body = ln[: m.start()] if m else ln.rstrip()
        try:
            hi = heading_hi(body) if body.startswith("#") else translate_line(body)
        except (Untranslated, KeyError) as e:
            errors += 1
            key = str(e)
            RESIDUE[key] += 1
            EXAMPLE.setdefault(key, body[:300])
            hi = "??? " + body
        out.append(hi + (f" ^{m.group(1)}" if m else ""))
    while out and out[-1] == "":
        out.pop()
    if write:
        with open(os.path.join(OUT_DIR, stem + ".md"), "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(out) + "\n")
    return errors


build_ph_index()

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry" in sys.argv
    stems = [f for f in FILES if not args or any(f.startswith(a) for a in args)]
    for st in stems:
        n = build_file(st, write=not dry)
        print(f"{st}: {n} lines with residue")
    for k, v in RESIDUE.most_common(60):
        print(v, repr(k), "|", EXAMPLE[k][:160])
