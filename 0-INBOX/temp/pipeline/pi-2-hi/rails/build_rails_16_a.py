"""Chapter 16 (Ñāṇavibhaṅga) Hindi rails, part A: shared strings, the matrix sections, Ekaka/Duka/Tika expositions.
Imported by build_rails_16.py (read-only use of build_rails_sample). Writes nothing.
"""
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-hi\rails")
import build_rails_sample as S  # noqa: E402

P = "प्रज्ञा"
NV = "ज्ञान का आधार"  # ñāṇavatthu
NUMW = {1: "एक", 2: "दो", 3: "तीन", 4: "चार", 5: "पाँच", 6: "छह", 7: "सात", 8: "आठ", 9: "नौ", 10: "दस"}
GROUP = {1: "एकल वर्गीकरण", 2: "दो-दो के वर्गीकरण", 3: "तीन-तीन के वर्गीकरण", 4: "चार-चार के वर्गीकरण",
         5: "पाँच-पाँच के वर्गीकरण", 6: "छह-छह के वर्गीकरण", 7: "सात-सात के वर्गीकरण", 8: "आठ-आठ के वर्गीकरण",
         9: "नौ-नौ के वर्गीकरण", 10: "दस-दस के वर्गीकरण"}  # pi-1 Rūpakaṇḍa scheme


def group_obl(n):
    return GROUP[n] if n == 1 else GROUP[n] + "ों"  # दो-दो के वर्गीकरणों


def matika_heading(n):
    return f"#### {group_obl(n)} की {'मूल सूची'}"


def niddesa_heading(n):
    return f"##### {group_obl(n)} की व्याख्या"


def vidha_open(n):
    return f"{NUMW[n]} प्रकार से {NV} –"


def vidha_end(n):
    return f"इस तरह {NUMW[n]} प्रकार से {NV} बताया गया।"


# ---------------------------------------------------------------- attributes of प्रज्ञा / चेतनाएँ (feminine forms, pi-1 matrix)
F = {
    "nahetu": "मूल रूपी न होने वाली", "ahetuka": "मूल से रहित", "hetuvippayutta": "मूलों से अलग",
    "sappaccaya": "कारणों पर निर्भर रहने वाली", "sankhata": "निर्मित", "arupa": "अभौतिक", "lokiya": "लौकिक",
    "lokuttara": "लोकोत्तर",
    "sasava": "मन के मैलों का विषय बनने वाली", "anasava": "मन के मैलों का विषय न बनने वाली",
    "sanyojaniya": "बंधनों का विषय बनने वाली", "asanyojaniya": "बंधनों का विषय न बनने वाली",
    "ganthaniya": "गाँठों का विषय बनने वाली", "aganthaniya": "गाँठों का विषय न बनने वाली",
    "oghaniya": "बाढ़ों का विषय बनने वाली", "anoghaniya": "बाढ़ों का विषय न बनने वाली",
    "yoganiya": "जकड़नों का विषय बनने वाली", "ayoganiya": "जकड़नों का विषय न बनने वाली",
    "nivaraniya": "बाधाओं का विषय बनने वाली", "anivaraniya": "बाधाओं का विषय न बनने वाली",
    "paramattha": "ग़लत धारणा का विषय बनने वाली", "aparamattha": "ग़लत धारणा का विषय न बनने वाली",
    "upadaniya": "आसक्ति का विषय बनने वाली", "anupadaniya": "आसक्ति का विषय न बनने वाली",
    "sankilesika": "क्लेशों का विषय बनने वाली", "asankilesika": "क्लेशों का विषय न बनने वाली",
    "abyakata": "नैतिक रूप से अनिर्धारित", "sarammana": "विषय वाली", "acetasika": "मन का सहचर न होने वाली",
    "vipaka": "कर्म-फल रूपी", "vipakadhamma": "कर्म-फल उत्पन्न करने वाली",
    "nevavipaka": "न कर्म-फल रूपी, न कर्म-फल उत्पन्न करने वाली",
    "upadinnupadaniya": "कर्म से उत्पन्न और आसक्ति का विषय बनने वाली",
    "anupadinnupadaniya": "कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाली",
    "anupadinnaanupadaniya": "न कर्म से उत्पन्न, न आसक्ति का विषय बनने वाली",
    "asankilitthasankilesika": "क्लेशों से मलिन न होने वाली, पर क्लेशों का विषय बनने वाली",
    "savitakkasavicara": "आरंभिक विचार और सतत विचार वाली",
    "avitakkavicaramatta": "आरंभिक विचार से रहित और केवल सतत विचार वाली",
    "avitakkaavicara": "आरंभिक विचार और सतत विचार दोनों से रहित",
    "na_savitakkasavicara": "न आरंभिक विचार और सतत विचार वाली",
    "na_avitakkavicaramatta": "न आरंभिक विचार से रहित और केवल सतत विचार वाली",
    "pitisahagata": "उल्लास के साथ होने वाली", "na_pitisahagata": "उल्लास के साथ न होने वाली",
    "sukhasahagata": "सुख के साथ होने वाली", "na_sukhasahagata": "सुख के साथ न होने वाली",
    "upekkhasahagata": "समभाव के साथ होने वाली", "na_upekkhasahagata": "समभाव के साथ न होने वाली",
    "neva_dassana": "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़ी जाने वाली",
    "neva_dassana_hetuka": "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़े जाने वाले मूलों वाली",
    "acayagami": "संचय की ओर ले जाने वाली", "apacayagami": "संचय घटाने की ओर ले जाने वाली",
    "nevacaya": "न संचय की ओर, न संचय घटाने की ओर ले जाने वाली",
    "sekkha": "सीखने के चरण की", "asekkha": "सीखना पूरा होने के चरण की",
    "nevasekkha": "न सीखने के चरण की, न सीखना पूरा होने के चरण की",
    "paritta": "सीमित", "mahaggata": "उन्नत", "appamana": "अपरिमित",
    "parittarammana": "सीमित विषय वाली", "mahaggatarammana": "उन्नत विषय वाली", "appamanarammana": "अपरिमित विषय वाली",
    "maggarammana": "मार्ग को विषय बनाने वाली", "maggahetuka": "मार्ग को मूल बनाने वाली",
    "maggadhipati": "मार्ग की प्रधानता वाली",
    "uppanna": "उत्पन्न हो चुकी", "anuppanna": "उत्पन्न न हुई", "uppadi": "उत्पन्न होने वाली",
    "atita": "अतीत की", "anagata": "भविष्य की", "paccuppanna": "वर्तमान की",
    "atitarammana": "अतीत के विषय वाली", "anagatarammana": "भविष्य के विषय वाली",
    "paccuppannarammana": "वर्तमान के विषय वाली",
    "ajjhatta": "स्वयं से संबंधित", "bahiddha": "दूसरों से संबंधित", "ajjhattabahiddha": "स्वयं और दूसरों दोनों से संबंधित",
    "ajjhattarammana": "स्वयं से संबंधित विषय वाली", "bahiddharammana": "दूसरों से संबंधित विषय वाली",
    "ajjhattabahiddharammana": "स्वयं और दूसरों दोनों से संबंधित विषय वाली",
    "kenaci_v": "किसी एक प्रकार की चेतना से जानी जा सकने वाली",
    "kenaci_nv": "किसी एक प्रकार की चेतना से न जानी जा सकने वाली",
    "upadinna": "कर्म से उत्पन्न", "anupadinna": "कर्म से उत्पन्न न होने वाली",
    "savitakka": "आरंभिक विचार वाली", "avitakka": "आरंभिक विचार से रहित",
    "savicara": "सतत विचार वाली", "avicara": "सतत विचार से रहित",
    "sappitika": "उल्लास वाली", "appitika": "उल्लास से रहित",
    "kamavacara": "इंद्रिय-सुखों के लोक से संबंधित", "na_kamavacara": "इंद्रिय-सुखों के लोक से संबंधित न होने वाली",
    "rupavacara": "सूक्ष्म भौतिक लोक से संबंधित", "na_rupavacara": "सूक्ष्म भौतिक लोक से संबंधित न होने वाली",
    "arupavacara": "अभौतिक लोक से संबंधित", "na_arupavacara": "अभौतिक लोक से संबंधित न होने वाली",
    "pariyapanna": "अस्तित्व के लोकों में समाई हुई", "apariyapanna": "अस्तित्व के लोकों में न समाई हुई",
    "no_apariyapanna": "अस्तित्व के लोकों में न समाई हुई नहीं",
    "niyyanika": "मुक्ति की ओर ले जाने वाली", "aniyyanika": "मुक्ति की ओर न ले जाने वाली",
    "niyata": "निश्चित", "aniyata": "अनिश्चित", "sauttara": "सर्वोच्च न होने वाली", "anuttara": "सर्वोच्च",
    "atthajapika": "लक्ष्य को सिद्ध करने वाली", "japitattha": "लक्ष्य सिद्ध कर चुकी",
    "cinta": "चिंतन से बनी", "suta": "सुनने से बनी", "bhavana": "मानसिक अभ्यास से बनी",
    "dana": "दान से बनी", "sila": "सदाचार से बनी",
    "adhisila": "उच्च सदाचार में", "adhicitta": "उच्च मन में", "adhipanna": "उच्च प्रज्ञा में",
}
for k in ("asava", "sanyojana", "gantha", "ogha", "yoga", "nivarana"):
    pass


def vipp(noun_obl, pron="उनका"):
    """X-vippayuttā sāsavā / anāsavā (pi-1 matrix)"""
    return (f"{noun_obl} से अलग, पर {pron} विषय बनने वाली", f"{noun_obl} से अलग और {pron} विषय न बनने वाली")


VIPP = {"asava": vipp("मन के मैलों"), "sanyojana": vipp("बंधनों"), "gantha": vipp("गाँठों"), "ogha": vipp("बाढ़ों"),
        "yoga": vipp("जकड़नों"), "nivarana": vipp("बाधाओं"), "paramasa": vipp("ग़लत धारणा", "उसका"),
        "upadana": vipp("आसक्ति", "उसका"),
        "kilesa": ("क्लेशों से अलग, पर क्लेशों का विषय बनने वाली", "क्लेशों से अलग और क्लेशों का विषय न बनने वाली")}


def pp(adj):
    return f"{adj} {P}"


# ---------------------------------------------------------------- 2-751 one-fold matrix
EKAKA_KEYS = ["nahetu", "ahetuka", "hetuvippayutta", "sappaccaya", "sankhata", "arupa", "lokiya", "sasava",
              "sanyojaniya", "ganthaniya", "oghaniya", "yoganiya", "nivaraniya", "paramattha", "upadaniya",
              "sankilesika", "abyakata", "sarammana", "acetasika", "vipaka", "upadinnupadaniya",
              "asankilitthasankilesika", "na_savitakkasavicara", "na_avitakkavicaramatta", "avitakkaavicara",
              "na_pitisahagata", "neva_dassana", "neva_dassana_hetuka", "nevacaya", "nevasekkha", "paritta",
              "kamavacara", "na_rupavacara", "na_arupavacara", "pariyapanna", "no_apariyapanna", "aniyata",
              "aniyyanika"]
FIVE = "पाँच प्रकार की चेतनाएँ"
FIVE_INS = "पाँच प्रकार की चेतनाओं से"
FIVE_AFTER = "पाँच प्रकार की चेतनाओं के ठीक बाद भी"
FIVE_AFTER_MD = "पाँच प्रकार की चेतनाओं के ठीक बाद मन के तत्व से भी"
KANCI_VAR = "[वर्तनी-भेद (Sī., Ka.): kiñci]"

# items (2)–(27): base strings shared by matrix and exposition
VATTHU = {  # quoted base for (2)–(6)
    2: "उत्पन्न आधार वाली और उत्पन्न विषय वाली",
    3: "पहले उत्पन्न हो चुके आधार वाली और पहले उत्पन्न हो चुके विषय वाली",
    4: "आंतरिक आधार वाली और बाह्य विषय वाली",
    5: "नष्ट न हुए आधार वाली और नष्ट न हुए विषय वाली",
    6: "अलग-अलग आधार वाली और अलग-अलग विषय वाली",
}
NA = {
    7: "एक-दूसरे के कार्यक्षेत्र का अनुभव नहीं करतीं",
    8: "मन को उस ओर ले जाए बिना उत्पन्न नहीं होतीं",
    9: "मनोयोग न करने से उत्पन्न नहीं होतीं",
    10: "बिना अंतराल के उत्पन्न नहीं होतीं",
    11: "बिना आगे-पीछे हुए उत्पन्न नहीं होतीं",
    12: "एक-दूसरे के ठीक बाद उत्पन्न नहीं होतीं",
}
ANABHOGA = f"{FIVE} मन लगाने से रहित हैं"
ACTS = {  # what is not done "with/after" the five
    "dhamma": "कोई किसी परिघटना को नहीं पहचानता",
    "iriya": "कोई किसी मुद्रा को नहीं अपनाता",
    "kamma": "कोई न शारीरिक कर्म आरंभ करता है, न वाणी का कर्म",
    "kusala": "कोई किसी हितकर या हानिकर परिघटना को नहीं अपनाता",
    "samapatti": "कोई न ध्यान-अवस्था में प्रवेश करता है, न उससे बाहर आता है",
    "cavati": "कोई न मरता है, न जन्म लेता है",
    "supati": "कोई न सोता है, न जागता है, न सपना देखता है",
}
ACT_ORDER = ["dhamma", "iriya", "kamma", "kusala", "samapatti", "cavati", "supati"]
ABHINIPATA = "विषय के टकराने भर को छोड़कर"
VIBHAVANA = "आधारों को यथार्थ रूप में स्पष्ट करने वाली प्रज्ञा"  # yāthāvakavatthuvibhāvanā paññā
POSTURES = "न चलना, न खड़ा होना, न बैठना, न लेटना"  # gamanaṃ vā ṭhānaṃ vā nisajjaṃ vā seyyaṃ vā


def act(key, var=False):
    s = ACTS[key]
    if var:
        s = s.replace("किसी परिघटना", f"किसी {KANCI_VAR} परिघटना")
    return s


def ekaka_matika():
    L = [f"{vidha_open(1)} {FIVE} " + ", ".join(F[k] for k in EKAKA_KEYS) + " हैं,",
         f"{VATTHU[2]} हैं,"]
    for n in range(3, 7):
        L.append(f"({n}) {VATTHU[n]} हैं")
    for n in range(7, 13):
        L.append(f"({n}) {NA[n]}")
    L.append(f"(13) {ANABHOGA}")
    n = 14
    for key in ACT_ORDER:
        if key == "dhamma":
            L.append(f"({n}) {FIVE_INS} {act(key, True)}, {ABHINIPATA}")
        else:
            L.append(f"({n}) {FIVE_INS} {act(key)}")
        tail = f", यह {VIBHAVANA} है" if key == "supati" else ""
        L.append(f"({n + 1}) {FIVE_AFTER} {act(key)}{tail}")
        n += 2
    L.append(vidha_end(1))
    return L


# ---------------------------------------------------------------- 2-752 two-fold matrix
DUKA = [("lokiya", "lokuttara"), ("kenaci_v", "kenaci_nv"), ("sasava", "anasava"), ("V:asava",),
        ("sanyojaniya", "asanyojaniya"), ("V:sanyojana",), ("ganthaniya", "aganthaniya"), ("V:gantha",),
        ("oghaniya", "anoghaniya"), ("V:ogha",), ("yoganiya", "ayoganiya"), ("V:yoga",),
        ("nivaraniya", "anivaraniya"), ("V:nivarana",), ("paramattha", "aparamattha"), ("V:paramasa",),
        ("upadinna", "anupadinna"), ("upadaniya", "anupadaniya"), ("V:upadana",),
        ("sankilesika", "asankilesika"), ("V:kilesa",), ("savitakka", "avitakka"), ("savicara", "avicara"),
        ("sappitika", "appitika"), ("pitisahagata", "na_pitisahagata"), ("sukhasahagata", "na_sukhasahagata"),
        ("upekkhasahagata", "na_upekkhasahagata"), ("kamavacara", "na_kamavacara"),
        ("rupavacara", "na_rupavacara"), ("arupavacara", "na_arupavacara"), ("pariyapanna", "apariyapanna"),
        ("niyyanika", "aniyyanika"), ("niyata", "aniyata"), ("sauttara", "anuttara"),
        ("atthajapika", "japitattha")]


def duka_pair(item):
    if item[0].startswith("V:"):
        return VIPP[item[0][2:]]
    return F[item[0]], F[item[1]]


def duka_matika():
    L = [vidha_open(2)]
    for i, it in enumerate(DUKA, 1):
        a, b = duka_pair(it)
        L.append(f"({i}) {pp(a)}, {pp(b)}")
    L.append(vidha_end(2))
    return L


# ---------------------------------------------------------------- 2-753 three-fold matrix
TIKA_ITEMS = {
    "cinta": ("cinta", "suta", "bhavana"), "dana": ("dana", "sila", "bhavana"),
    "adhi": ("adhisila", "adhicitta", "adhipanna"),
    "vipaka": ("vipaka", "vipakadhamma", "nevavipaka"),
    "upadinna": ("upadinnupadaniya", "anupadinnupadaniya", "anupadinnaanupadaniya"),
    "vitakka": ("savitakkasavicara", "avitakkavicaramatta", "avitakkaavicara"),
    "piti": ("pitisahagata", "sukhasahagata", "upekkhasahagata"),
    "acaya": ("acayagami", "apacayagami", "nevacaya"), "sekkha": ("sekkha", "asekkha", "nevasekkha"),
    "paritta": ("paritta", "mahaggata", "appamana"),
    "parittarammana": ("parittarammana", "mahaggatarammana", "appamanarammana"),
    "magga": ("maggarammana", "maggahetuka", "maggadhipati"), "uppanna": ("uppanna", "anuppanna", "uppadi"),
    "atita": ("atita", "anagata", "paccuppanna"),
    "atitarammana": ("atitarammana", "anagatarammana", "paccuppannarammana"),
    "ajjhatta": ("ajjhatta", "bahiddha", "ajjhattabahiddha"),
    "ajjhattarammana": ("ajjhattarammana", "bahiddharammana", "ajjhattabahiddharammana"),
}
KOSALLA_W = ("उन्नति में कुशलता", "अवनति में कुशलता", "उपाय में कुशलता")  # āya-, apāya-, upāyakosallaṃ (āya/apāya: no entry)
KOSALLA = ", ".join(KOSALLA_W)
TIKA_MATIKA_ORDER = ["cinta", "dana", "adhi", "KOSALLA", "vipaka", "upadinna", "vitakka", "piti", "acaya", "sekkha",
                     "paritta", "parittarammana", "magga", "uppanna", "atita", "atitarammana", "ajjhatta",
                     "ajjhattarammana"]
ATTHI_FIRST = {"vipākā": "vipaka", "upādinnupādāniyā": "upadinna", "savitakkasavicārā": "vitakka",
               "pītisahagatā": "piti", "ācayagāminī": "acaya", "sekkhā": "sekkha", "parittā": "paritta",
               "parittārammaṇā": "parittarammana", "maggārammaṇā": "magga", "uppannā": "uppanna",
               "atītā": "atita", "atītārammaṇā": "atitarammana", "ajjhattā": "ajjhatta", "ajjhatā": "ajjhatta",
               "ajjhattārammaṇā": "ajjhattarammana"}
SUBJ = {"Savitakkasavicārā paññā": pp(F["savitakkasavicara"]),
        "Avitakkavicāramattā paññā": pp(F["avitakkavicaramatta"]),
        "Avitakkaavicārā paññā": pp(F["avitakkaavicara"]),
        "Pītisahagatā paññā sukhasahagatā paññā": f"{pp(F['pitisahagata'])} और {pp(F['sukhasahagata'])}",
        "Upekkhāsahagatā paññā": pp(F["upekkhasahagata"])}


def kuch3(key):
    a, b, c = (F[x] for x in TIKA_ITEMS[key])
    return f"कुछ {a} है, कुछ {b} है, कुछ {c} है"


def tika_matika(pali_lines):
    """pali_lines: the 77 lines of segment 2-753 (to read the (19)–(75) atthi rows)."""
    L = [vidha_open(3)]
    for i, key in enumerate(TIKA_MATIKA_ORDER, 1):
        if key == "KOSALLA":
            L.append(f"({i}) {KOSALLA}")
        else:
            L.append(f"({i}) " + ", ".join(pp(F[x]) for x in TIKA_ITEMS[key]))
    for line in pali_lines[19:-1]:
        num, rest = line.split(") ", 1)
        num = num + ")"
        subj = ""
        for sp, sh in SUBJ.items():
            if rest.startswith(sp + " atthi"):
                subj = sh + " में "
                rest = rest[len(sp) + 1:]
                break
        first = rest.split(",")[0].split()[1]
        key = ATTHI_FIRST[first]
        L.append(f"{num} {subj}{kuch3(key)}")
    L.append(vidha_end(3))
    return L


# ---------------------------------------------------------------- 2-754 … 2-760 matrices
SAMANGI = "से युक्त व्यक्ति का ज्ञान"
PATIPADA_TO = "के अंत की ओर ले जाने वाले प्रगति के ढंग"  # …nirodhagāminiyā paṭipadāya


def truth4(x, gen_x):
    """x = 'दुःख' / 'बुढ़ापे और मृत्यु' / 'मानसिक रचनाओं'; returns the four knowledges"""
    return [f"{gen_x} का ज्ञान", f"{x} की उत्पत्ति का ज्ञान", f"{x} के अंत का ज्ञान", f"{x}{PATIPADA_TO} का ज्ञान"]


DUKKHA4 = truth4("दुःख", "दुःख")
JARA4 = truth4("बुढ़ापे और मृत्यु", "बुढ़ापे और मृत्यु")
SANKHARA4 = truth4("मानसिक रचनाओं", "मानसिक रचनाओं")
LINKS = ["जन्म", "अस्तित्व", "आसक्ति", "तृष्णा", "अनुभूति", "संपर्क", "छह इंद्रिय-क्षेत्रों",
         "मानसिक पक्ष और भौतिक रूप", "चेतना"]
PARIYE_VAR = "[पाठभेद (सर्वत्र): paricce; दीघनिकाय देखें]"
SAMMUTI_VAR = "[वर्तनी-भेद (Syā.): sammatiñāṇaṃ; दीघनिकाय देखें]"
DHAMME_N = "परिघटना का ज्ञान"
ANVAYE_N = "अनुमान का ज्ञान"
PARIYE_N = "दूसरों के मन को जानने का ज्ञान"
SAMMUTI_N = "लोक-मान्यता का ज्ञान"
ACAYA4 = ["कुछ प्रज्ञा संचय के लिए होती है, संचय घटाने के लिए नहीं",
          "कुछ प्रज्ञा संचय घटाने के लिए होती है, संचय के लिए नहीं",
          "कुछ प्रज्ञा संचय के लिए भी होती है और संचय घटाने के लिए भी",
          "कुछ प्रज्ञा न संचय के लिए होती है, न संचय घटाने के लिए"]
NIBBIDA4 = ["कुछ प्रज्ञा विरक्ति के लिए होती है, गहरी पैठ के लिए नहीं",
            "कुछ प्रज्ञा गहरी पैठ के लिए होती है, विरक्ति के लिए नहीं",
            "कुछ प्रज्ञा विरक्ति के लिए भी होती है और गहरी पैठ के लिए भी",
            "कुछ प्रज्ञा न विरक्ति के लिए होती है, न गहरी पैठ के लिए"]
BHAGI = {"hana": "पतन की भागी", "thiti": "स्थिरता की भागी", "visesa": "विशेष उन्नति की भागी",
         "nibbedha": "भेदन की भागी"}
MP = "चार मार्गों में, चार फलों में प्रज्ञा"  # catūsu maggesu catūsu phalesu paññā


def catukka_matika():
    L = [vidha_open(4),
         "(1) कर्म के अपना होने का ज्ञान, सत्यों के अनुरूप ज्ञान, मार्ग " + SAMANGI + ", फल " + SAMANGI,
         "(2) " + ", ".join(DUKKHA4),
         "(3) " + ", ".join(pp(F[k]) for k in ("kamavacara", "rupavacara", "arupavacara", "apariyapanna")),
         f"(4) {DHAMME_N}, {ANVAYE_N}, दूसरों के मन को जानने का {PARIYE_VAR} ज्ञान, {SAMMUTI_N} {SAMMUTI_VAR}",
         "(5) " + "; ".join(ACAYA4),
         "(6) " + "; ".join(NIBBIDA4),
         "(7) " + ", ".join(pp(BHAGI[k]) for k in ("hana", "thiti", "visesa", "nibbedha")),
         "(8) चार विश्लेषणात्मक ज्ञान",
         "(9) प्रगति के चार ढंग",
         "(10) चार विषय",
         "(11) " + ", ".join(JARA4),
         "(12-21) " + "… ".join(f"{x} का ज्ञान" for x in LINKS) + "… " + ", ".join(SANKHARA4) + "। " + vidha_end(4)]
    return L


TATHAGATA_ACTS = "श्रेष्ठ वृषभ के स्थान का दावा करते हैं, सभाओं में सिंहनाद करते हैं, श्रेष्ठ चक्र चलाते हैं"
POWERS_OBJ = {  # what the Tathāgata knows as it really is (object + को, for the matrix of tens)
    1: "संभव को संभव के रूप में और असंभव को असंभव के रूप में",
    2: "अतीत, भविष्य और वर्तमान में अपनाए गए कर्मों के कर्म-फल को परिस्थिति और कारण के अनुसार",
    3: "सभी गतियों की ओर ले जाने वाले प्रगति के ढंग को",
    4: "अनेक तत्वों वाले, अलग-अलग तत्वों वाले लोक को",
    5: "प्राणियों के अलग-अलग झुकावों को",
    6: "दूसरे प्राणियों, दूसरे व्यक्तियों की क्षमताओं की ऊँच-नीच को",
    7: "ध्यानों, मुक्ति की अवस्थाओं, एकाग्रताओं और ध्यान-अवस्थाओं के दूषित होने, शुद्ध होने और उनसे बाहर आने को",
    8: "पूर्व जन्मों के अनुस्मरण को",
    9: "प्राणियों की मृत्यु और पुनर्जन्म को",
    10: "मन के मैलों के क्षय को",
}
ANEKADHATU_VAR = "[पाठभेद (Syā.): anekadhātuṃ nānādhātuṃ lokaṃ; मज्झिम निकाय 1.148]"


def power_matika_line(n):
    obj = POWERS_OBJ[n]
    obj1 = obj.replace("लोक को", f"लोक {ANEKADHATU_VAR} को") if n == 4 else obj
    opener = "यहाँ" if n == 1 else "फिर,"
    s = (f"({n}) {opener} तथागत {obj1} यथार्थ जानते हैं। तथागत जो {obj} यथार्थ जानते हैं, यह भी तथागत का एक "
         f"तथागत-बल है, जिस बल के सहारे तथागत {TATHAGATA_ACTS}।")
    if n == 10:
        s += f" ये तथागत के दस तथागत-बल हैं, जिन बलों से युक्त होकर तथागत {TATHAGATA_ACTS}।"
    return s


def small_matikas():
    h = {}
    h["2-755"] = [vidha_open(5), "(1) पाँच अंगों वाली सही एकाग्रता (2) पाँच ज्ञानों वाली सही एकाग्रता", vidha_end(5)]
    h["2-756"] = [vidha_open(6), "(1) छह उच्च ज्ञानों में प्रज्ञा", vidha_end(6)]
    h["2-757"] = [vidha_open(7), "(1) ज्ञान के सतहत्तर आधार", vidha_end(7)]
    h["2-758"] = [vidha_open(8), "(1) चार मार्गों में, चार फलों में प्रज्ञा", vidha_end(8)]
    h["2-759"] = [vidha_open(9), "(1) नौ क्रमिक ध्यान-अवस्थाओं में प्रज्ञा", vidha_end(9)]
    h["2-760"] = ([f"{vidha_open(10)} तथागत के दस तथागत-बल, जिन बलों से युक्त होकर तथागत {TATHAGATA_ACTS}। "
                   "वे दस कौन-से हैं?"] + [power_matika_line(n) for n in range(1, 11)] + [vidha_end(10)])
    return h


# ---------------------------------------------------------------- 2-761 … 2-766 one-fold exposition
EKAKA_EVA = EKAKA_KEYS + ["uppanna_mano", "anicca", "jara"]


def ekaka_niddesa_761():
    extra = {"uppanna_mano": "उत्पन्न होने पर मन की चेतना से जानी जा सकने वाली", "anicca": "अनित्य",
             "jara": "बुढ़ापे से ग्रस्त"}
    items = [(F.get(k) or extra[k]) + " ही" for k in EKAKA_EVA]
    return [f"{FIVE} " + ", ".join(items) + " हैं।"]


def ekaka_niddesa_762():
    SENSE = ["आँख", "कान", "नाक", "जीभ", "शरीर"]
    return [
        f"“{FIVE} {VATTHU[2]} हैं” यानी वे आधार के उत्पन्न हो चुकने पर, विषय के उत्पन्न हो चुकने पर उत्पन्न होती हैं।",
        f"“{VATTHU[3]} हैं” यानी वे आधार के पहले उत्पन्न हो चुकने पर, विषय के पहले उत्पन्न हो चुकने पर उत्पन्न होती हैं।",
        f"“{VATTHU[4]} हैं” यानी पाँच प्रकार की चेतनाओं के आधार आंतरिक हैं, विषय बाह्य हैं।",
        f"“{VATTHU[5]} हैं” यानी वे आधार के नष्ट न होने पर, विषय के नष्ट न होने पर उत्पन्न होती हैं।",
        f"“{VATTHU[6]} हैं” यानी " + ", ".join(f"{s} की चेतना का आधार और विषय अलग है" for s in SENSE) + "।",
    ]


def cross(a, b, kind):
    """kind 'gocara' (2-763) or 'after' (2-765)"""
    if kind == "gocara":
        return (f"{a} की चेतना के कार्यक्षेत्र का अनुभव {b} की चेतना नहीं करती, "
                f"{b} की चेतना के कार्यक्षेत्र का अनुभव भी {a} की चेतना नहीं करती।")
    return (f"{a} की चेतना के उत्पन्न होने के ठीक बाद {b} की चेतना उत्पन्न नहीं होती, "
            f"{b} की चेतना के उत्पन्न होने के ठीक बाद भी {a} की चेतना उत्पन्न नहीं होती।")


def cross_segment(kind):
    head = NA[7] if kind == "gocara" else NA[12]
    first = [cross("आँख", x, kind) for x in ("कान", "नाक", "जीभ", "शरीर")]
    if kind == "gocara":
        mid = "कान की चेतना के… नाक की चेतना के… जीभ की चेतना के… " + cross("शरीर", "आँख", kind)
    else:
        mid = "कान की चेतना के… नाक की चेतना के… जीभ की चेतना के… " + cross("शरीर", "आँख", kind)
    last = [cross("शरीर", x, kind) for x in ("कान", "नाक", "जीभ")]
    return [f"“{head}” यानी " + " ".join(first + [mid] + last)]


def ekaka_niddesa_764():
    return [f"“{NA[8]}” यानी मन को उस ओर ले जाने वाले व्यक्ति में उत्पन्न होती हैं।",
            f"“{NA[9]}” यानी मनोयोग करने वाले व्यक्ति में उत्पन्न होती हैं।",
            f"“{NA[10]}” यानी एक के बाद एक लगातार उत्पन्न नहीं होतीं।",
            f"“{NA[11]}” यानी एक ही क्षण में उत्पन्न नहीं होतीं।"]


def ekaka_niddesa_766():
    L = [f"“{ANABHOGA}” यानी पाँच प्रकार की चेतनाओं में न मन का मुड़ना होता है, न मन लगाना, "
         "न मन को उस ओर ले जाना, न मनोयोग।"]
    for key in ACT_ORDER:
        a = f"“{FIVE_INS} {act(key)}” यानी {FIVE_INS} {act(key)}"
        b = f"“{FIVE_AFTER} {act(key)}” यानी {FIVE_AFTER_MD} {act(key)}"
        if key == "iriya":
            a += f" – {POSTURES}"
            b += f" – {POSTURES}"
        L.append(a + "।")
        if key == "dhamma":
            L.append(f"“{ABHINIPATA}” यानी विषय के सामने आने भर को छोड़कर।")
        tail = f" इस तरह यह {VIBHAVANA} है।" if key == "supati" else ""
        L.append(b + "।" + tail)
    L += [vidha_end(1), f"{GROUP[1]}।"]
    return L


# ---------------------------------------------------------------- 2-767 two-fold exposition
TB = "तीन स्तरों के"
CB = "चार स्तरों के"
KA_MIND = "हितकर और नैतिक रूप से अनिर्धारित मन में"  # kusalābyākate
K_MIND = "हितकर मन में"                              # kusale
V_MIND = "कर्म-फल रूपी मन में"                        # vipāke
KR_MIND = "केवल क्रिया रूपी नैतिक रूप से अनिर्धारित मन में"  # kiriyābyākate
TB_KA = f"{TB} {KA_MIND} प्रज्ञा"


def is_(subject, adj):
    return f"{subject} {pp(adj)} है"


def duka_niddesa():
    L = []
    std = {1: ("lokiya", "lokuttara"), 3: ("sasava", "anasava"), 5: ("sanyojaniya", "asanyojaniya"),
           7: ("ganthaniya", "aganthaniya"), 9: ("oghaniya", "anoghaniya"), 11: ("yoganiya", "ayoganiya"),
           13: ("nivaraniya", "anivaraniya"), 15: ("paramattha", "aparamattha"),
           18: ("upadaniya", "anupadaniya"), 20: ("sankilesika", "asankilesika"),
           31: ("pariyapanna", "apariyapanna"), 34: ("sauttara", "anuttara")}
    vp = {4: "asava", 6: "sanyojana", 8: "gantha", 10: "ogha", 12: "yoga", 14: "nivarana", 16: "paramasa",
          19: "upadana", 21: "kilesa"}
    assoc = {22: ("आरंभिक विचार", "savitakka", "avitakka"), 23: ("सतत विचार", "savicara", "avicara"),
             24: ("उल्लास", "sappitika", "appitika"), 25: ("उल्लास", "pitisahagata", "na_pitisahagata"),
             26: ("सुख", "sukhasahagata", "na_sukhasahagata"), 27: ("समभाव", "upekkhasahagata", "na_upekkhasahagata")}
    sph = {28: ("इंद्रिय-सुखों के लोक से संबंधित", "kamavacara", ["rupavacara", "arupavacara", "apariyapanna"], "na_kamavacara"),
           29: ("सूक्ष्म भौतिक लोक से संबंधित", "rupavacara", ["kamavacara", "arupavacara", "apariyapanna"], "na_rupavacara"),
           30: ("अभौतिक लोक से संबंधित", "arupavacara", ["kamavacara", "rupavacara", "apariyapanna"], "na_arupavacara")}
    for n in range(1, 35):
        if n in std:
            a, b = std[n]
            L.append(f"({n}) {is_(TB_KA, F[a])}, {is_(MP, F[b])}।")
        elif n in vp:
            a, b = VIPP[vp[n]]
            L.append(f"({n}) {is_(TB_KA, a)}, {is_(MP, b)}।")
        elif n == 2:
            L.append(f"(2) सारी प्रज्ञा {F['kenaci_v']} है, {F['kenaci_nv']} है।")
        elif n == 17:
            L.append(f"(17) {is_(f'{TB} {V_MIND} प्रज्ञा', F['upadinna'])}, "
                     f"{is_(f'{TB} {K_MIND}, {TB} {KR_MIND}, चार मार्गों में, चार फलों में प्रज्ञा', F['anupadinna'])}।")
        elif n in assoc:
            x, a, b = assoc[n]
            L.append(f"({n}) {is_(f'{x} से जुड़ी प्रज्ञा', F[a])}, {is_(f'{x} से अलग प्रज्ञा', F[b])}।")
        elif n in sph:
            x, a, others, neg = sph[n]
            subj2 = [pp(F[o]) for o in others]
            subj2 = ", ".join(subj2[:-1]) + " और " + subj2[-1]
            L.append(f"({n}) {is_(f'{x} {KA_MIND} प्रज्ञा', F[a])}, {subj2} {pp(F[neg])} है।")
        elif n in (32, 33):
            a, b = ("niyyanika", "aniyyanika") if n == 32 else ("niyata", "aniyata")
            L.append(f"({n}) {is_('चार मार्गों में प्रज्ञा', F[a])}, "
                     f"{is_(f'{TB} {K_MIND}, {CB} {V_MIND}, {TB} {KR_MIND} प्रज्ञा', F[b])}।")
    L.append(f"(35) यहाँ {pp(F['atthajapika'])} क्या है?")
    L.append(f"{CB} {K_MIND}, और उच्च ज्ञान उत्पन्न करने वाले, ध्यान-अवस्था उत्पन्न करने वाले अर्हत् के {KR_MIND} "
             f"प्रज्ञा {pp(F['atthajapika'])} है, {CB} {V_MIND}, और उच्च ज्ञान के उत्पन्न हो चुकने पर, ध्यान-अवस्था के "
             f"उत्पन्न हो चुकने पर अर्हत् के {KR_MIND} प्रज्ञा {pp(F['japitattha'])} है।")
    L += [vidha_end(2), f"{GROUP[2]}।"]
    return L


# ---------------------------------------------------------------- 2-768 … 2-792 three-fold exposition
PANNA_ABBR = "प्रज्ञा, जानना… मोह का अभाव, परिघटनाओं की छानबीन, सही दृष्टि"  # PI1 ^1-16, abbreviated


def arises(cond, name, called="कही जाती है"):
    """X ārabbha yā uppajjati paññā pajānanā…pe… sammādiṭṭhi – ayaṃ vuccati "name"."""
    return f"{cond} जो {PANNA_ABBR} उत्पन्न होती है – यह “{name}” {called}।"


def q(label, name, kya="क्या है?"):
    return f"{label} यहाँ {name} {kya}"


SAMAP = "ध्यान-अवस्था में लीन व्यक्ति की सारी प्रज्ञा"
YOGA = ("कौशल से रचे गए कर्म के क्षेत्रों में, कौशल से रचे गए शिल्प के क्षेत्रों में या कौशल से रचे गए विद्या की "
        "शाखाओं में, चाहे कर्म के अपना होने के बारे में हो, चाहे सत्यों के अनुरूप हो, चाहे “भौतिक रूप अनित्य है”, "
        "या अनुभूति… पहचान… मानसिक रचनाएँ… “चेतना अनित्य है”, इस बारे में इस प्रकार की जो अनुकूल स्वीकृति, दृष्टि, "
        "रुचि, अनुमोदन, परख, परिघटनाओं के मनन की स्वीकृति कोई दूसरों से")


def tika_niddesa_a():
    h = {}
    c, s_, b = pp(F["cinta"]), pp(F["suta"]), pp(F["bhavana"])
    h["2-768"] = [q("(1. क)", c),
                  f"{YOGA} सुने बिना पाता है – यह “{c}” कही जाती है।",
                  f"{q('(ख)', s_)} {YOGA} सुनकर पाता है – यह “{s_}” कही जाती है।",
                  f"(ग) {SAMAP} {b} है।"]
    d, sl = pp(F["dana"]), pp(F["sila"])
    h["2-769"] = [f"{q('(2. क)', d)} {arises('दान को लेकर, दान के कारण', d)}",
                  f"{q('(ख)', sl)} {arises('सदाचार को लेकर, सदाचार के कारण', sl)}",
                  f"(ग) {SAMAP} {b} है।"]
    a1, a2, a3 = (pp(F[k]) for k in ("adhisila", "adhicitta", "adhipanna"))
    h["2-770"] = [f"{q('(3. क)', a1)} {arises('भिक्षु-नियमों की संहिता के संयम से स्वयं को संयमित करने वाले व्यक्ति में', a1)}",
                  f"{q('(ख)', a2)} {arises('सूक्ष्म भौतिक लोक और अभौतिक लोक से संबंधित ध्यान-अवस्था में प्रवेश करने वाले व्यक्ति में', a2)}",
                  f"{q('(ग)', a3)} {MP} – यह “{a3}” कही जाती है।"]
    MAN = "इन परिघटनाओं पर मनोयोग करने वाले व्यक्ति में"
    GROW = "और बढ़ने, विपुलता, अभ्यास और परिपूर्णता की ओर ले जाती हैं"  # bhiyyobhāvāya … saṃvattanti
    ay, ap, up = KOSALLA_W
    h["2-771"] = [
        f"{q('(4. क)', ay)} “{MAN} उत्पन्न न हुई हानिकर परिघटनाएँ उत्पन्न नहीं होतीं और उत्पन्न हो चुकी हानिकर "
        f"परिघटनाएँ छूट जाती हैं। या फिर {MAN} उत्पन्न न हुई हितकर परिघटनाएँ उत्पन्न होती हैं और उत्पन्न हो चुकी "
        f"हितकर परिघटनाएँ {GROW}” – यहाँ जो {PANNA_ABBR} है – यह “{ay}” कही जाती है।",
        f"{q('(ख)', ap)} “{MAN} उत्पन्न न हुई हितकर परिघटनाएँ उत्पन्न नहीं होतीं और उत्पन्न हो चुकी हितकर "
        f"परिघटनाएँ समाप्त हो जाती हैं। या फिर {MAN} उत्पन्न न हुई हानिकर परिघटनाएँ उत्पन्न होती हैं और उत्पन्न हो "
        f"चुकी हानिकर परिघटनाएँ और बढ़ने और विपुलता की ओर ले जाती हैं” – यहाँ जो {PANNA_ABBR} है – "
        f"यह “{ap}” कही जाती है।",
        f"(ग) वहाँ उपाय के रूप में होने वाली सारी प्रज्ञा {up} है।"]
    h["2-772"] = [f"(5. क) {CB} {V_MIND} प्रज्ञा {pp(F['vipaka'])} है।",
                  f"(ख) {CB} {K_MIND} प्रज्ञा {pp(F['vipakadhamma'])} है।",
                  f"(ग) {TB} {KR_MIND} प्रज्ञा {pp(F['nevavipaka'])} है।"]
    h["2-773"] = [f"(6. क) {TB} {V_MIND} प्रज्ञा {pp(F['upadinnupadaniya'])} है।",
                  f"(ख) {TB} {K_MIND}, {TB} {KR_MIND} प्रज्ञा {pp(F['anupadinnupadaniya'])} है।",
                  f"(ग) {MP} {pp(F['anupadinnaanupadaniya'])} है।"]
    h["2-774"] = [f"(7. क) आरंभिक विचार और सतत विचार से जुड़ी प्रज्ञा {pp(F['savitakkasavicara'])} है।",
                  f"(ख) आरंभिक विचार से अलग और सतत विचार से जुड़ी प्रज्ञा {pp(F['avitakkavicaramatta'])} है।",
                  f"(ग) आरंभिक विचार और सतत विचार से अलग प्रज्ञा {pp(F['avitakkaavicara'])} है।"]
    h["2-775"] = [f"(8. क) उल्लास से जुड़ी प्रज्ञा {pp(F['pitisahagata'])} है।",
                  f"(ख) सुख से जुड़ी प्रज्ञा {pp(F['sukhasahagata'])} है।",
                  f"(ग) समभाव से जुड़ी प्रज्ञा {pp(F['upekkhasahagata'])} है।"]
    h["2-776"] = [f"(9. क) {TB} {K_MIND} प्रज्ञा {pp(F['acayagami'])} है।",
                  f"(ख) चार मार्गों में प्रज्ञा {pp(F['apacayagami'])} है।",
                  f"(ग) {CB} {V_MIND}, {TB} {KR_MIND} प्रज्ञा {pp(F['nevacaya'])} है।"]
    up_var = "[पाठभेद (Syā.): upariṭṭhime; (Ka.): upariṭṭhimaṃ]"
    h["2-777"] = [f"(10. क) चार मार्गों में, तीन फलों में प्रज्ञा {pp(F['sekkha'])} है।",
                  f"(ख) सबसे ऊँचे {up_var} अर्हत्-पद के फल में प्रज्ञा {pp(F['asekkha'])} है।",
                  f"(ग) {TB} {K_MIND}, {TB} {V_MIND}, {TB} {KR_MIND} प्रज्ञा {pp(F['nevasekkha'])} है।"]
    h["2-778"] = [f"(11. क) इंद्रिय-सुखों के लोक से संबंधित {KA_MIND} प्रज्ञा {pp(F['paritta'])} है।",
                  f"(ख) सूक्ष्म भौतिक लोक और अभौतिक लोक से संबंधित {KA_MIND} प्रज्ञा {pp(F['mahaggata'])} है।",
                  f"(ग) {MP} {pp(F['appamana'])} है।"]
    for sid, lab, key, cond in (("2-779", "(12. क)", "parittarammana", "सीमित परिघटनाओं को लेकर"),
                                ("2-780", "(ख)", "mahaggatarammana", "उन्नत परिघटनाओं को लेकर"),
                                ("2-781", "(ग)", "appamanarammana", "अपरिमित परिघटनाओं को लेकर")):
        h[sid] = [f"{q(lab, pp(F[key]))} {arises(cond, pp(F[key]))}"]
    m1, m2, m3 = (pp(F[k]) for k in ("maggarammana", "maggahetuka", "maggadhipati"))
    h["2-782"] = [f"{q('(13. क)', m1)} {arises('आर्य मार्ग को लेकर', m1)}", f"(ख) चार मार्गों में प्रज्ञा {m2} है।"]
    h["2-783"] = [f"{q('(ग)', m3)} {arises('आर्य मार्ग को प्रधान बनाकर', m3)}"]
    h["2-784"] = [f"(14) {CB} {V_MIND} प्रज्ञा कभी उत्पन्न हो चुकी होती है, कभी उत्पन्न होने वाली होती है, उसे "
                  f"“उत्पन्न न हुई” नहीं कहा जा सकता। {CB} {K_MIND}, {TB} {KR_MIND} प्रज्ञा कभी उत्पन्न हो चुकी होती "
                  "है, कभी उत्पन्न न हुई होती है, उसे “उत्पन्न होने वाली” नहीं कहा जा सकता।"]
    h["2-785"] = ["(15) सारी प्रज्ञा कभी अतीत की होती है, कभी भविष्य की होती है, कभी वर्तमान की होती है।"]
    for sid, lab, key, cond in (("2-786", "(16. क)", "atitarammana", "अतीत की परिघटनाओं को लेकर"),
                                ("2-787", "(ख)", "anagatarammana", "भविष्य की परिघटनाओं को लेकर"),
                                ("2-788", "(ग)", "paccuppannarammana", "वर्तमान की परिघटनाओं को लेकर")):
        h[sid] = [f"{q(lab, pp(F[key]))} {arises(cond, pp(F[key]))}"]
    h["2-789"] = ["(17) सारी प्रज्ञा कभी स्वयं से संबंधित होती है, कभी दूसरों से संबंधित होती है, कभी स्वयं और दूसरों "
                  "दोनों से संबंधित होती है।"]
    for sid, lab, key, cond in (("2-790", "(18. क)", "ajjhattarammana", "स्वयं से संबंधित परिघटनाओं को लेकर"),
                                ("2-791", "(ख)", "bahiddharammana", "दूसरों से संबंधित परिघटनाओं को लेकर"),
                                ("2-792", "(ग)", "ajjhattabahiddharammana",
                                 "स्वयं और दूसरों दोनों से संबंधित परिघटनाओं को लेकर")):
        h[sid] = [f"{q(lab, pp(F[key]))} {arises(cond, pp(F[key]))}"]
    h["2-792"] += [vidha_end(3), f"{GROUP[3]}।"]
    return h
