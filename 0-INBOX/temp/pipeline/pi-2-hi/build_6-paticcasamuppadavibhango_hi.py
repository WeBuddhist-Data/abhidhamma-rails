# -*- coding: utf-8 -*-
"""pi-2 Vibhaṅga, chapter 6 (Paṭiccasamuppādavibhaṅga), Hindi plain zero-shot.

usage: python -I -X utf8 build_6-paticcasamuppadavibhango_hi.py
Writes AI_translation\\hindi\\pi-2-hindi-plain-zeroshot_split_chapters\\6-paticcasamuppadavibhango.md

Sentence-level formula translator: every Pāli sentence is translated by fixed formula strings
(links of the chain, question/answer frames, synonym strings from the reviewed pi-1 Hindi), so every
repeat is byte-identical. Any sentence the rules do not cover raises an error.
Block IDs are copied from the Pāli at build time.
"""
import os, re, sys

HERE = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-hi"
sys.path.insert(0, HERE)
import build_ch1_sample_hi as S  # noqa: E402  (approved constants; importing writes nothing)

CH = "6-paticcasamuppadavibhango.md"
DASH = S.DASH
MODE = {"sutta": True}  # Suttantabhājanīya: saṅkhārā plural; Abhidhammabhājanīya: saṅkhāro singular

# ---------------------------------------------------------------- 1. the links of the chain
# key: (nominative, oblique, gender, number)
LINK = {
    "avijja": ("अज्ञान", "अज्ञान", "m", "sg"),
    "sankhara": ("मानसिक रचना", "मानसिक रचना", "f", "sg"),            # saṅkhāro (one mind-moment)
    "sankhara_pl": ("मानसिक रचनाएँ", "मानसिक रचनाओं", "f", "pl"),     # saṅkhārā (pi-1 ^1-1343)
    "vinnana": ("चेतना", "चेतना", "f", "sg"),
    "nama": ("मानसिक पक्ष", "मानसिक पक्ष", "m", "sg"),                   # pi-1 nāma
    "rupa": ("भौतिक रूप", "भौतिक रूप", "m", "sg"),
    "namarupa": ("मानसिक पक्ष और भौतिक रूप", "मानसिक पक्ष और भौतिक रूप", "m", "pl"),  # pi-1 ^1-1343
    "salayatana": ("छह इंद्रिय-क्षेत्र", "छह इंद्रिय-क्षेत्रों", "m", "pl"),           # pi-1 ^1-1343
    "chattha": ("छठा इंद्रिय-क्षेत्र", "छठे इंद्रिय-क्षेत्र", "m", "sg"),
    "phassa": ("संपर्क", "संपर्क", "m", "sg"),
    "vedana": ("अनुभूति", "अनुभूति", "f", "sg"),
    "tanha": ("तृष्णा", "तृष्णा", "f", "sg"),
    "upadana": ("आसक्ति", "आसक्ति", "f", "sg"),
    "bhava": ("अस्तित्व", "अस्तित्व", "m", "sg"),
    "jati": ("जन्म", "जन्म", "m", "sg"),
    "jaramarana": ("बुढ़ापा और मृत्यु", "बुढ़ापे और मृत्यु", "m", "pl"),
    "jara": ("बुढ़ापा", "बुढ़ापे", "m", "sg"),
    "marana": ("मृत्यु", "मृत्यु", "f", "sg"),
    "adhimokkha": ("निश्चय", "निश्चय", "m", "sg"),
    "pasada": ("आस्था", "आस्था", "f", "sg"),
    "patigha": ("चिढ़", "चिढ़", "f", "sg"),
    "vicikiccha": ("संशय", "संशय", "m", "sg"),
    "uddhacca": ("बेचैनी", "बेचैनी", "f", "sg"),
    "kusalamula": ("हितकर मूल", "हितकर मूलों", "m", "pl"),
    "akusalamula": ("हानिकर मूल", "हानिकर मूलों", "m", "pl"),
    # simple terms (no "X-paccayā")
    "punna": ("पुण्य की कर्म-रचना", "पुण्य की कर्म-रचना", "f", "sg"),             # pi-5
    "apunna": ("अपुण्य की कर्म-रचना", "अपुण्य की कर्म-रचना", "f", "sg"),
    "anenja": ("अविचल अवस्था की कर्म-रचना", "अविचल अवस्था की कर्म-रचना", "f", "sg"),  # pi-5
    "kayasankhara": ("शरीर की रचना", "शरीर की रचना", "f", "sg"),                 # pi-5
    "kammabhava": ("कर्म रूपी अस्तित्व", "कर्म रूपी अस्तित्व", "m", "sg"),
    "upapattibhava": ("पुनर्जन्म रूपी अस्तित्व", "पुनर्जन्म रूपी अस्तित्व", "m", "sg"),
    "soka": ("शोक", "शोक", "m", "sg"),
    "parideva": ("विलाप", "विलाप", "m", "sg"),
    "dukkha": ("दुःख", "दुःख", "m", "sg"),
    "domanassa": ("उदासी", "उदासी", "f", "sg"),
    "upayasa": ("निराशा", "निराशा", "f", "sg"),
    "alobha": ("लोभ का अभाव", "लोभ के अभाव", "m", "sg"),                       # pi-1
    "adosa": ("द्वेष का अभाव", "द्वेष के अभाव", "m", "sg"),
    "amoha": ("मोह का अभाव", "मोह के अभाव", "m", "sg"),
}

SRC = {  # stem in "<stem>paccayā", "<stem>hetuko", "<stem>sampayutto"
    "avijjā": "avijja", "saṅkhāra": "sankhara", "viññāṇa": "vinnana", "nāma": "nama", "nāmarūpa": "namarupa",
    "chaṭṭhāyatana": "chattha", "saḷāyatana": "salayatana", "phassa": "phassa", "vedanā": "vedana",
    "taṇhā": "tanha", "upādāna": "upadana", "bhava": "bhava", "jāti": "jati", "adhimokkha": "adhimokkha",
    "pasāda": "pasada", "paṭigha": "patigha", "vicikicchā": "vicikiccha", "uddhacca": "uddhacca",
    "kusalamūla": "kusalamula", "akusalamūla": "akusalamula",
}
DST = {  # nominative Pāli word
    "avijjā": "avijja", "saṅkhāro": "sankhara", "saṅkhārā": "sankhara_pl", "viññāṇaṃ": "vinnana",
    "nāmaṃ": "nama", "rūpaṃ": "rupa", "nāmarūpaṃ": "namarupa", "chaṭṭhāyatanaṃ": "chattha",
    "saḷāyatanaṃ": "salayatana", "phasso": "phassa", "vedanā": "vedana", "taṇhā": "tanha",
    "upādānaṃ": "upadana", "bhavo": "bhava", "jāti": "jati", "jarāmaraṇaṃ": "jaramarana", "jarā": "jara",
    "maraṇaṃ": "marana", "adhimokkho": "adhimokkha", "pasādo": "pasada", "paṭighaṃ": "patigha",
    "vicikicchā": "vicikiccha", "uddhaccaṃ": "uddhacca", "kusalamūlā": "kusalamula",
    "puññābhisaṅkhāro": "punna", "apuññābhisaṅkhāro": "apunna", "āneñjābhisaṅkhāro": "anenja",
    "kāyasaṅkhāro": "kayasankhara", "kammabhavo": "kammabhava", "upapattibhavo": "upapattibhava",
    "soko": "soka", "paridevo": "parideva", "dukkhaṃ": "dukkha", "domanassaṃ": "domanassa",
    "upāyāso": "upayasa", "alobho": "alobha", "adoso": "adosa", "amoho": "amoha",
}


def _k(key):
    if key == "sankhara" and MODE["sutta"]:
        return "sankhara_pl"
    return key


def nom(k): return LINK[_k(k)][0]
def obl(k): return LINK[_k(k)][1]
def pl(k): return LINK[_k(k)][3] == "pl"
def fem(k): return LINK[_k(k)][2] == "f"
def cop(k): return "हैं" if pl(k) else "है"
def yah(k): return "ये" if pl(k) else "यह"
def vala(k): return "वाले" if (pl(k) and not fem(k)) else ("वाली" if fem(k) else "वाला")
def jura(k): return "जुड़े" if (pl(k) and not fem(k)) else ("जुड़ी" if fem(k) else "जुड़ा")


def kaha(k):
    if fem(k):
        return "कही जाती हैं" if pl(k) else "कही जाती है"
    return "कहे जाते हैं" if pl(k) else "कहा जाता है"


def parse_term(p):
    """'saṅkhārapaccayāpi avijjā', 'avijjāpaccayā saṅkhāro avijjāhetuko', 'nāmaṃ' ... -> dict"""
    toks = p.strip().split()
    t = {"src": None, "pi": False, "mod": None}
    if toks[0].endswith("paccayāpi"):
        t["src"], t["pi"] = SRC[toks[0][:-len("paccayāpi")]], True
        toks = toks[1:]
    elif toks[0].endswith("paccayā"):
        t["src"] = SRC[toks[0][:-len("paccayā")]]
        toks = toks[1:]
    t["dst"] = DST[toks[0]]
    mods = toks[1:]
    if len(mods) == 1:
        m = mods[0]
        if "hetuk" in m:
            t["mod"] = ("hetu", SRC[m.split("hetuk")[0]])
        elif "sampayutt" in m:
            t["mod"] = ("samp", SRC[m.split("sampayutt")[0]])
        else:
            raise KeyError("modifier: " + p)
    elif len(mods) == 2:  # viññāṇasampayuttaṃ nāmaṃ / nāmasampayuttaṃ chaṭṭhāyatanaṃ
        assert "sampayutt" in mods[0], p
        t["mod"] = ("part", SRC[mods[0].split("sampayutt")[0]], DST[mods[1]])
    elif mods:
        raise KeyError("modifier: " + p)
    return t


def modtext(t):
    m, d = t["mod"], t["dst"]
    if not m:
        return ""
    if m[0] == "hetu":
        return f", {'जिनका' if pl(d) else 'जिसका'} मूल {nom(m[1])} है"
    if m[0] == "samp":
        return f", जो {obl(m[1])} से {jura(d)} {cop(d)}"
    part = m[2]
    return f", जिनमें {nom(part)} {obl(m[1])} से {jura(part)} है"


def chain_item(p):
    """avijjāpaccayā saṅkhāro  ->  अज्ञान के कारण मानसिक रचना"""
    t = parse_term(p)
    if t["src"]:
        base = f"{obl(t['src'])} के कारण{' भी' if t['pi'] else ''} {nom(t['dst'])}"
    else:
        base = nom(t["dst"])
    return base + modtext(t)


def np(p):
    """noun phrase for questions and answers: अज्ञान के कारण होने वाली मानसिक रचना"""
    t = parse_term(p)
    if t["src"]:
        base = f"{obl(t['src'])} के कारण{' भी' if t['pi'] else ''} होने {vala(t['dst'])} {nom(t['dst'])}"
    else:
        base = nom(t["dst"])
    return base + modtext(t), t


def question(p):
    """Tattha katamo <p>?  ->  यहाँ <np> क्या है?"""
    parts = [x.strip() for x in p.split("…pe…")]
    nps = [np(x) for x in parts]
    t = nps[-1][1]
    comma = "," if t["mod"] else ""
    return f"यहाँ {'… '.join(n for n, _ in nps)}{comma} क्या {cop(t['dst'])}?"


# ---------------------------------------------------------------- 2. answers
DUKKHA_SAMUDAYA = "इस प्रकार इस पूरे दुःख के समूह की उत्पत्ति होती है"   # pi-1 ^1-1343
DHAMMA_SAMUDAYA = "इस प्रकार इन परिघटनाओं की उत्पत्ति होती है"
TENA = "इसलिए कहा जाता है,"


def answer_part(a):
    a = a.strip()
    m = re.match(r'^(?:tena|Tena) vuccati "?(evametassa kevalassa dukkhakkhandhassa samudayo hot[iī]|evametesaṃ dhammānaṃ samudayo hot[iī])"ti\.?$', a)
    if m:
        what = DUKKHA_SAMUDAYA if "dukkhakkhandhassa" in m.group(1) else DHAMMA_SAMUDAYA
        return f"{TENA} “{what}”"
    m = re.match(r'^(?:ayaṃ|idaṃ|ime|Ayaṃ|Idaṃ|Ime) vucca(?:ti|nti)( –)?(.+?)\.?$', a)
    if not m:
        raise KeyError("answer: " + a)
    dash, rest = m.group(1), m.group(2)
    quoted = '"' in rest
    term = rest.replace('"', "").strip().rstrip(".")
    phrase, t = np(term)
    q1, q2 = ("“", "”") if quoted else ("", "," if t["mod"] else "")
    return f"{yah(t['dst'])}{' ' + DASH if dash else ''} {q1}{phrase}{q2} {kaha(t['dst'])}"


def answer(a):
    """'ayaṃ vuccati "avijjā"…pe… tena vuccati "…"ti.'  (parts joined by '…')"""
    a = a.strip()
    end = "।" if a.endswith(".") else ""
    body = a[:-1] if end else a
    parts = body.split("…pe…")
    out = []
    for i, p in enumerate(parts):
        if not p.strip():
            assert i == len(parts) - 1, a
            continue
        out.append(answer_part(p))
    text = "… ".join(out)
    if not parts[-1].strip():
        text += "…"
    return text + end


# ---------------------------------------------------------------- 3. bodies (definitions before " – ")
KHANDHA3 = "अनुभूति का समूह, पहचान का समूह और मानसिक रचनाओं का समूह"
KHANDHA4 = "अनुभूति का समूह, पहचान का समूह, मानसिक रचनाओं का समूह और चेतना का समूह"
KHANDHA_NO_VEDANA = "पहचान का समूह, मानसिक रचनाओं का समूह और चेतना का समूह"
CITTA_FULL = ("जो मन, मानस, मानसिक क्रिया, हृदय, उज्ज्वलता, मानस, मन का इंद्रिय-क्षेत्र, मन की क्षमता, चेतना, "
              "चेतना का समूह, उसके अनुरूप मन की चेतना का तत्व है")                      # pi-1 ^1-6
CITTA_PE = "जो मन, मानस, मानसिक क्रिया… उसके अनुरूप {} है"
TAJJA = {"tajjāmanoviññāṇadhātu": "मन की चेतना का तत्व", "tajjācakkhuviññāṇadhātu": "आँख की चेतना का तत्व",
         "tajjāmanodhātu": "मन का तत्व", "tajjākāyaviññāṇadhātu": "शरीर की चेतना का तत्व"}
CETANA = "जो इरादा, इरादा करना, इरादा कर चुका होना है"                                    # pi-1 ^1-5
PHASSA = "जो संपर्क, छूना, भली-भाँति छूना, भली-भाँति छू चुका होना है"                       # pi-1 ^1-2
FEEL_SUKHA = ("जो मानसिक सुहावनापन, मानसिक सुख, मन के संपर्क से उत्पन्न सुहावना सुखद अनुभव, "
              "मन के संपर्क से उत्पन्न सुहावनी सुखद अनुभूति है")                             # pi-1 ^1-3
FEEL_ADM = ("जो न मानसिक सुहावनापन, न मानसिक असुहावनापन, मन के संपर्क से उत्पन्न न दुःखद, न सुखद अनुभव, "
            "मन के संपर्क से उत्पन्न न दुःखद, न सुखद अनुभूति है")                           # pi-1 ^1-152
FEEL_DOMANASSA = ("जो मानसिक असुहावनापन, मानसिक दुःख, मन के संपर्क से उत्पन्न असुहावना दुःखद अनुभव, "
                  "मन के संपर्क से उत्पन्न असुहावनी दुःखद अनुभूति है")                        # pi-1 ^1-415
FEEL_KAYA_SUKHA = ("जो शारीरिक सुहावनापन, शारीरिक सुख, शरीर के संपर्क से उत्पन्न सुहावना सुखद अनुभव, "
                   "शरीर के संपर्क से उत्पन्न सुहावनी सुखद अनुभूति है")                       # pi-1 ^1-445
FEEL_KAYA_DUKKHA = ("जो शारीरिक असुहावनापन, शारीरिक दुःख, शरीर के संपर्क से उत्पन्न असुहावना दुःखद अनुभव, "
                    "शरीर के संपर्क से उत्पन्न असुहावनी दुःखद अनुभूति है")                    # pi-1 ^1-558
AVIJJA_PE = "जो न जानना, न देखना… अज्ञान की रुकावट, मोह रूपी हानिकर मूल है"            # pi-1 ^1-390
TANHA_FULL = "जो राग, प्रबल राग, झुकाव, अनुकूल होना, आनंद, आनंद का राग, मन का प्रबल राग है"   # pi-1 ^1-1065
DITTHI_LIST = ("दृष्टि, दृष्टियों में फँसना, दृष्टि का घना जंगल, दृष्टि का बीहड़, दृष्टि का टेढ़ापन, "
               "दृष्टि की छटपटाहट, दृष्टि का बंधन, पकड़, कसकर पकड़ना, आग्रह, ग़लत धारणा, कुमार्ग, "
               "ग़लत रास्ता, ग़लतपन, मतवादों का आधार, उलटी पकड़")                           # pi-1 ^1-381
ADHIMOKKHA = "जो मन का निश्चय, निश्चय करना, उस पर निश्चय कर चुका होना है"               # new
SADDHA = "जो श्रद्धा, श्रद्धा रखना, भरोसा करना, गहरी आस्था है"                             # pi-1 ^1-12
ALOBHA = ("जो लोभ का अभाव, लोभ न करना, लोभ से भरा न होना, प्रबल राग का अभाव, राग न करना, "
          "राग से भरा न होना, लालच का अभाव, लोभ का अभाव रूपी हितकर मूल है")                  # pi-1 ^1-32
ADOSA = ("जो द्वेष का अभाव, द्वेष न करना, द्वेष से भरा न होना, दुर्भावना का अभाव, दुर्भावना न रखना, "
         "द्वेष का अभाव रूपी हितकर मूल है")                                                # pi-1 ^1-33
AMOHA_PE = "जो प्रज्ञा, जानना… मोह का अभाव, परिघटनाओं की छानबीन, सही दृष्टि"               # pi-1 ^1-1343
AMOHA_LOK = "परिघटनाओं की छानबीन नामक जागृति का अंग, मार्ग का अंग, मार्ग में समाया हुआ"    # pi-1 ^1-292
UDDHACCA = "जो मन की बेचैनी, अशांति, मन का भटकाव, मन का डाँवाडोल होना है"                 # pi-1 ^1-427
DOSA_PE = "जो मन का आक्रोश… उग्रता, कटु वचन [वर्तनी-भेद (Syā.): asulopo], मन की अप्रसन्नता है"  # pi-1 ^1-1066
VICIKICCHA = ("जो शंका, शंका करना, शंका से भरा होना, दुविधा, संशय, दुचित्तापन, दोराहा "
              "[वर्तनी-भेद (Sī., Syā.): dvedhāpatho], संदेह, किसी एक बात को पक्का न पकड़ पाना, हिचकिचाना, "
              "बार-बार हिचकिचाना, गहराई में न उतर पाना [वर्तनी-भेद (Sī., Syā., Ka.): apariyogāhanā], "
              "मन का जड़ हो जाना, मन की खरोंच है")                                          # pi-1 ^1-423
DHAMMANAM = "उन-उन परिघटनाओं का जो"
JATI_DH = DHAMMANAM + " जन्म, भली-भाँति जन्म, पैदा होना, पूरी तरह पैदा होना, प्रकट होना है"   # SYN_PACCUPPANNA words
JARA_DH = DHAMMANAM + " बुढ़ापा, जीर्ण होना, आयु का घटना है"                                # pi-1 ^1-643
MARANA_DH = DHAMMANAM + " क्षय, नाश, टूटना, बिखर जाना, अनित्यता, लुप्त हो जाना है"           # pi-1 ^1-644
SATTANAM = "उन-उन प्राणियों का उन-उन प्राणी-वर्गों "
JATI_SATTA = (SATTANAM + "में जो जन्म, भली-भाँति जन्म, गर्भ में उतरना, पूरी तरह पैदा होना, "
              "समूहों का प्रकट होना, इंद्रिय-क्षेत्रों की प्राप्ति है")
JARA_SATTA = (SATTANAM + "में जो बुढ़ापा, जीर्ण होना, दाँतों का टूटना, बालों का पकना, त्वचा पर झुर्रियाँ पड़ना, "
              "आयु का घटना, इंद्रियों का पूरी तरह पक जाना है")                                # pi-1 ^1-643
MARANA_SATTA = (SATTANAM + "से जो गुज़र जाना, गुज़र जाने की अवस्था, टूटना, लुप्त हो जाना, मौत, मृत्यु, "
                "काल का पूरा होना [वर्तनी-भेद (Ka.): kālaṃkiriyā], समूहों का टूटना, शरीर का त्याग, "
                "जीवन-क्षमता का कट जाना है")
UPACAYA = (", ".join(f"{s} के इंद्रिय-क्षेत्र की वृद्धि" for s in ["आँख", "कान", "नाक", "जीभ", "शरीर"])
           + ", या जो भी अन्य भौतिक रूप मन से जन्मा, मन के कारण होने वाला और मन से उत्पन्न है")   # pi-1 ^1-641, ^1-666
VATTHU = "जिस भौतिक रूप के सहारे मन की चेतना का तत्व काम करता है"
VATTHU_MAHA = "चार महाभूत और वह भौतिक रूप, जिसके सहारे मन की चेतना का तत्व काम करता है"
SIX = ["आँख", "कान", "नाक", "जीभ", "शरीर", "मन"]


def six(fmt):
    items = [fmt.format(s) for s in SIX]
    return ", ".join(items[:-1]) + " और " + items[-1]


COND = ("रिश्तेदारों की हानि से, या धन-संपत्ति की हानि से, या रोग की विपत्ति से, या सदाचार की हानि से, "
        "या दृष्टि की हानि से प्रभावित व्यक्ति में, किसी न किसी विपत्ति से घिरे व्यक्ति में, "
        "किसी न किसी दुःखद परिघटना से प्रभावित व्यक्ति में")
P_COND = ("Ñātibyasanena vā phuṭṭhassa, bhogabyasanena vā phuṭṭhassa, rogabyasanena vā phuṭṭhassa, "
          "sīlabyasanena vā phuṭṭhassa, diṭṭhibyasanena vā phuṭṭhassa, aññataraññatarena byasanena "
          "samannāgatassa, aññataraññatarena dukkhadhammena phuṭṭhassa ")
P_CETANA = "Yā cetanā sañcetanā sañcetayitattaṃ"
P_CITTA = "Yaṃ cittaṃ mano mānasaṃ"
P_K4 = "vedanākkhandho saññākkhandho saṅkhārakkhandho viññāṇakkhandho"

BODY = {
    # Suttantabhājanīya
    "Dukkhe aññāṇaṃ, dukkhasamudaye aññāṇaṃ, dukkhanirodhe aññāṇaṃ, dukkhanirodhagāminiyā paṭipadāya aññāṇaṃ":
        "दुःख को न जानना, दुःख की उत्पत्ति को न जानना, दुःख के अंत को न जानना, "
        "दुःख के अंत की ओर ले जाने वाले प्रगति के ढंग को न जानना",                          # pi-1 ^1-1067
    "Kusalā cetanā kāmāvacarā rūpāvacarā dānamayā sīlamayā bhāvanāmayā":
        "हितकर इरादा, जो इंद्रिय-सुखों के लोक से संबंधित और सूक्ष्म भौतिक लोक से संबंधित है, "
        "दान से बना, सदाचार से बना और मानसिक अभ्यास से बना",
    "Akusalā cetanā kāmāvacarā": "हानिकर इरादा, जो इंद्रिय-सुखों के लोक से संबंधित है",
    "Kusalā cetanā arūpāvacarā": "हितकर इरादा, जो अभौतिक लोक से संबंधित है",
    "Cakkhuviññāṇaṃ, sotaviññāṇaṃ, ghānaviññāṇaṃ, jivhāviññāṇaṃ, kāyaviññāṇaṃ, manoviññāṇaṃ": S.MEMBERS["vinnana"],
    "Vedanākkhandho, saññākkhandho, saṅkhārakkhandho": KHANDHA3,
    "Vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho": KHANDHA4,
    "Cattāro mahābhūtā, catunnañca mahābhūtānaṃ upādāya rūpaṃ": S.MEMBERS["rupa"],
    "Cakkhāyatanaṃ, sotāyatanaṃ, ghānāyatanaṃ, jivhāyatanaṃ, kāyāyatanaṃ, manāyatanaṃ": six("{} का इंद्रिय-क्षेत्र"),
    "Cakkhusamphasso sotasamphasso ghānasamphasso jivhāsamphasso kāyasamphasso manosamphasso": six("{} का संपर्क"),
    "Cakkhusamphassajā vedanā, sotasamphassajā vedanā, ghānasamphassajā vedanā, jivhāsamphassajā vedanā, "
    "kāyasamphassajā vedanā, manosamphassajā vedanā": six("{} के संपर्क से उत्पन्न अनुभूति"),
    "Rūpataṇhā, saddataṇhā, gandhataṇhā, rasataṇhā, phoṭṭhabbataṇhā, dhammataṇhā":
        "दृश्य रूप की तृष्णा, ध्वनि की तृष्णा, गंध की तृष्णा, स्वाद की तृष्णा, स्पर्श की तृष्णा और मन के विषयों की तृष्णा",
    "Kāmupādānaṃ, diṭṭhupādānaṃ, sīlabbatupādānaṃ, attavādupādānaṃ":
        "इंद्रिय-सुखों के प्रति आसक्ति, दृष्टियों के प्रति आसक्ति, सदाचार और व्रतों के प्रति आसक्ति, "
        "आत्मा के सिद्धांत के प्रति आसक्ति",                                               # pi-1 ^1-1219
    "Puññābhisaṅkhāro, apuññābhisaṅkhāro, āneñjābhisaṅkhāro":
        "पुण्य की कर्म-रचना, अपुण्य की कर्म-रचना और अविचल अवस्था की कर्म-रचना",
    "Kāmabhavo, rūpabhavo, arūpabhavo, saññābhavo, asaññābhavo, nevasaññānāsaññābhavo, ekavokārabhavo, "
    "catuvokārabhavo, pañcavokārabhavo":
        "इंद्रिय-सुखों के लोक का अस्तित्व, सूक्ष्म भौतिक लोक का अस्तित्व, अभौतिक लोक का अस्तित्व, "
        "पहचान वाला अस्तित्व, पहचान से रहित अस्तित्व, न पहचान, न अ-पहचान वाला अस्तित्व, "
        "एक समूह वाला अस्तित्व, चार समूहों वाला अस्तित्व और पाँच समूहों वाला अस्तित्व",     # pi-5 ^5-111
    "Yā tesaṃ tesaṃ sattānaṃ tamhi tamhi sattanikāye jāti sañjāti okkanti abhinibbatti, khandhānaṃ pātubhāvo, "
    "āyatanānaṃ paṭilābho": JATI_SATTA,
    "Yā tesaṃ tesaṃ sattānaṃ tamhi tamhi sattanikāye jarā jīraṇatā khaṇḍiccaṃ pāliccaṃ valittacatā āyuno "
    "saṃhāni indriyānaṃ paripāko": JARA_SATTA,
    "Yā tesaṃ tesaṃ sattānaṃ tamhā tamhā sattanikāyā cuti cavanatā bhedo antaradhānaṃ maccu maraṇaṃ "
    "kālakiriyā [kālaṃkiriyā (ka.)] khandhānaṃ bhedo kaḷevarassa nikkhepo jīvitindriyassupacchedo": MARANA_SATTA,
    P_COND + "soko socanā socitattaṃ antosoko antoparisoko cetaso parijjhāyanā domanassaṃ sokasallaṃ":
        COND + " जो शोक, शोक करना, शोक से भरा होना, भीतर का शोक, भीतर का गहरा शोक, मन का जलना, उदासी, शोक का काँटा है",
    P_COND + "ādevo paridevo ādevanā paridevanā ādevitattaṃ paridevitattaṃ vācā palāpo vippalāpo lālappo "
             "lālappanā lālappitattaṃ":
        COND + " जो रोना, विलाप, रोते रहना, विलाप करते रहना, रोने से भरा होना, विलाप से भरा होना, "
               "शब्दों की झड़ी, प्रलाप, बड़बड़ाना, बिलखना, बिलखते रहना, बिलखने से भरा होना है",
    P_COND + "āyāso upāyāso āyāsitattaṃ upāyāsitattaṃ":
        COND + " जो हताशा, निराशा, हताशा से भरा होना, निराशा से भरा होना है",
    "Yaṃ kāyikaṃ asātaṃ kāyikaṃ dukkhaṃ kāyasamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ kāyasamphassajā asātā dukkhā vedanā":
        FEEL_KAYA_DUKKHA,
    "Yaṃ cetasikaṃ asātaṃ, cetasikaṃ dukkhaṃ, cetosamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ, cetosamphassajā asātā dukkhā vedanā":
        FEEL_DOMANASSA,
    # Abhidhammabhājanīya
    "Yaṃ aññāṇaṃ adassanaṃ…pe… avijjālaṅgī moho akusalamūlaṃ": AVIJJA_PE,
    "Yaṃ aññāṇaṃ adassanaṃ…pe… avijjālaṅgī moho akusamūlaṃ": AVIJJA_PE,
    P_CETANA: CETANA,
    P_CETANA + " [cetayitattaṃ (sī. ka.)]": "जो इरादा, इरादा करना, इरादा कर चुका होना [पाठभेद (Sī., Ka.): cetayitattaṃ] है",
    P_CITTA + " hadayaṃ paṇḍaraṃ mano manāyatanaṃ manindriyaṃ viññāṇaṃ viññāṇakkhandho tajjāmanoviññāṇadhātu": CITTA_FULL,
    "Yo phasso phusanā samphusanā samphusitattaṃ": PHASSA,
    "Yaṃ cetasikaṃ sātaṃ cetasikaṃ sukhaṃ cetosamphassajaṃ sātaṃ sukhaṃ vedayitaṃ cetosamphassajā sātā sukhā vedanā":
        FEEL_SUKHA,
    "Yaṃ cetasikaṃ neva sātaṃ nāsātaṃ cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ cetosamphassajā adukkhamasukhā vedanā":
        FEEL_ADM,
    "Yaṃ cetasikaṃ neva sātaṃ nāsātaṃ cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ, cetosamphassajā adukkhamasukhā vedanā":
        FEEL_ADM,
    "Yaṃ cetasikaṃ asātaṃ cetasikaṃ dukkhaṃ cetosamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ cetosamphassajā asātā dukkhā vedanā":
        FEEL_DOMANASSA,
    "Yaṃ kāyikaṃ sātaṃ kāyikaṃ sukhaṃ kāyasamphassajaṃ sātaṃ sukhaṃ vedayitaṃ kāyasamphassajā sātā sukhā vedanā":
        FEEL_KAYA_SUKHA,
    "Yo rāgo sārāgo anunayo anurodho nandī nandirāgo cittassa sārāgo": TANHA_FULL,
    "Yo rāgo sārāgo…pe… cittassa sārāgo": "जो राग, प्रबल राग… मन का प्रबल राग है",
    "Yo rāgo…pe… cittassa sārāgo": "जो राग… मन का प्रबल राग है",
    "Yā diṭṭhi diṭṭhigataṃ diṭṭhigahanaṃ diṭṭhikantāro diṭṭhivisūkāyikaṃ diṭṭhivipphanditaṃ diṭṭhisaṃyojanaṃ gāho "
    "patiṭṭhāho abhiniveso parāmāso kummaggo micchāpatho micchattaṃ titthāyatanaṃ vipariyāsaggāho "
    "[vipariyesaggāho (bahūsu)]": "जो " + DITTHI_LIST + " [वर्तनी-भेद (Bahūsu): vipariyesaggāho] है",
    "Yā diṭṭhi diṭṭhigataṃ…pe… titthāyatanaṃ vipariyāsaggāho": "जो दृष्टि, दृष्टियों में फँसना… मतवादों का आधार, उलटी पकड़ है",
    "Ṭhapetvā upādānaṃ, " + P_K4: "आसक्ति को छोड़कर, " + KHANDHA4,
    "Ṭhapetvā phassaṃ, " + P_K4: "संपर्क को छोड़कर, " + KHANDHA4,
    "Ṭhapetvā adhimokkhaṃ, " + P_K4: "निश्चय को छोड़कर, " + KHANDHA4,
    "Ṭhapetvā adhimokkhaṃ, vedanākkhandho saññākkhandho saṅkhārakkhandho, viññāṇakkhandho": "निश्चय को छोड़कर, " + KHANDHA4,
    "Ṭhapetvā vicikicchaṃ, " + P_K4: "संशय को छोड़कर, " + KHANDHA4,
    "Ṭhapetvā vedanaṃ, saññākkhandho saṅkhārakkhandho viññāṇakkhandho": "अनुभूति को छोड़कर, " + KHANDHA_NO_VEDANA,
    "Yā tesaṃ tesaṃ dhammānaṃ jāti sañjāti nibbatti abhinibbatti pātubhāvo": JATI_DH,
    "Yā tesaṃ tesaṃ dhammānaṃ jāti sañjāti nibbatti abhinibbati pātubhāvo": JATI_DH,
    "Yā tesaṃ tesaṃ dhammānaṃ jarā jīraṇatā āyuno saṃhāni": JARA_DH,
    "Yo tesaṃ tesaṃ dhammānaṃ khayo vayo bhedo paribhedo aniccatā antaradhānaṃ": MARANA_DH,
    "Cakkhāyatanassa upacayo, sotāyatanassa upacayo, ghānāyatanassa upacayo, jivhāyatanassa upacayo, "
    "kāyāyatanassa upacayo, yaṃ vā panaññampi atthi rūpaṃ cittajaṃ cittahetukaṃ cittasamuṭṭhānaṃ": UPACAYA,
    "Yaṃ rūpaṃ nissāya manoviññāṇadhātu vattati": VATTHU,
    "Cattāro ca mahābhūtā, yañca rūpaṃ nissāya manoviññāṇadhātu vattati": VATTHU_MAHA,
    "Yo cittassa adhimokkho adhimuccanā tadadhimuttatā": ADHIMOKKHA,
    "Yā saddhā saddahanā okappanā abhippasādo": SADDHA,
    "Yo cittassa āghāto…pe… caṇḍikkaṃ asuropo [asulopo (syā.)] anattamanatā cittassa": DOSA_PE,
    "Yā kaṅkhā kaṅkhāyanā kaṅkhāyitattaṃ vimati vicikicchā dveḷhakaṃ dvidhāpatho [dvedhāpatho (sī. syā.)] saṃsayo "
    "anekaṃsaggāho āsappanā parisappanā apariyogāhaṇā [apariyogāhanā (sī. syā. ka.)] chambhitattaṃ cittassa manovilekho":
        VICIKICCHA,
    "Yaṃ cittassa uddhaccaṃ avūpasamo cetaso vikkhepo bhantattaṃ cittassa": UDDHACCA,
    "Yo alobho alubbhanā alubbhitattaṃ asārāgo asārajjanā asārajjitattaṃ anabhijjhā alobho kusalamūlaṃ": ALOBHA,
    "Yo adoso adussanā adussitattaṃ abyāpādo abyāpajjo adoso kusalamūlaṃ": ADOSA,
    "Yā paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi": AMOHA_PE + " है",
    "Yā paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi dhammavicayasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ":
        AMOHA_PE + ", " + AMOHA_LOK + " है",
    "Alobho, adoso, amoho": "लोभ का अभाव, द्वेष का अभाव और मोह का अभाव",
    "Alobho, adoso": "लोभ का अभाव और द्वेष का अभाव",
}
for _t, _h in TAJJA.items():
    BODY[P_CITTA + "…pe… " + _t] = CITTA_PE.format(_h)
    BODY[P_CITTA + " …pe… " + _t] = CITTA_PE.format(_h)

# ---------------------------------------------------------------- 4. fixed sentences
SAMUDAYA_PARTS = "का मेल होता है, मिलन होता है, जुड़ाव होता है, प्रकटन होता है"
SENT = {
    # chapter frame and section closings
    "Suttantabhājanīyaṃ.": S.SECTION_TITLES["Suttantabhājanīyaṃ"] + "।",
    "Abhidhammabhājanīyaṃ.": S.SECTION_TITLES["Abhidhammabhājanīyaṃ"] + "।",
    "Paṭiccasamuppādavibhaṅgo [paccayākāravibhaṅgo (sī. syā.)] niṭṭhito.":
        S.CHAPTER_TITLES[6] + " [पाठभेद (Sī., Syā.): paccayākāravibhaṅgo] पूरा हुआ।",
    # Suttanta chain (pi-1 ^1-1343, without the quotation marks)
    "Avijjāpaccayā saṅkhārā, saṅkhārapaccayā viññāṇaṃ, viññāṇapaccayā nāmarūpaṃ, nāmarūpapaccayā saḷāyatanaṃ, "
    "saḷāyatanapaccayā phasso, phassapaccayā vedanā, vedanāpaccayā taṇhā, taṇhāpaccayā upādānaṃ, upādānapaccayā bhavo, "
    "bhavapaccayā jāti, jātipaccayā jarāmaraṇaṃ sokaparidevadukkhadomanassupāyāsā sambhavanti.":
        "अज्ञान के कारण मानसिक रचनाएँ, मानसिक रचनाओं के कारण चेतना, चेतना के कारण मानसिक पक्ष और भौतिक रूप, "
        "मानसिक पक्ष और भौतिक रूप के कारण छह इंद्रिय-क्षेत्र, छह इंद्रिय-क्षेत्रों के कारण संपर्क, संपर्क के कारण अनुभूति, "
        "अनुभूति के कारण तृष्णा, तृष्णा के कारण आसक्ति, आसक्ति के कारण अस्तित्व, अस्तित्व के कारण जन्म, "
        "जन्म के कारण बुढ़ापा और मृत्यु, शोक, विलाप, दुःख, उदासी और निराशा होते हैं।",
    "Evametassa kevalassa dukkhakkhandhassa samudayo hoti.": DUKKHA_SAMUDAYA + "।",
    "Evametesaṃ dhammānaṃ samudayo hoti.": DHAMMA_SAMUDAYA + "।",
    "Evametassa kevalassa dukkhakkhandhassa samudayo hotīti, evametassa kevalassa dukkhakkhandhassa saṅgati hoti, "
    "samāgamo hoti, samodhānaṃ hoti, pātubhāvo hoti.":
        f"“{DUKKHA_SAMUDAYA}”, यानी इस प्रकार इस पूरे दुःख के समूह {SAMUDAYA_PARTS}।",
    "Evametassa kevalassa dukkhakkhandhassa samudayo hotīti.": f"“{DUKKHA_SAMUDAYA}”।",
    "Evametassa kevalassa dukkhakkhandhassa saṅgati hoti, samāgamo hoti, samodhānaṃ hoti, pātubhāvo hoti.":
        f"इस प्रकार इस पूरे दुःख के समूह {SAMUDAYA_PARTS}।",
    "Evametesaṃ dhammānaṃ samudayo hotīti.": f"“{DHAMMA_SAMUDAYA}”।",
    "Evametesaṃ dhammānaṃ saṅgati hoti, samāgamo hoti, samodhānaṃ hoti, pātubhāvo hoti.":
        f"इस प्रकार इन परिघटनाओं {SAMUDAYA_PARTS}।",
    "Puññābhisaṅkhāro, apuññābhisaṅkhāro, āneñjābhisaṅkhāro, kāyasaṅkhāro, vacīsaṅkhāro, cittasaṅkhāro.":
        "पुण्य की कर्म-रचना, अपुण्य की कर्म-रचना, अविचल अवस्था की कर्म-रचना, शरीर की रचना, वाणी की रचना और मन की रचना।",
    "Kāyasañcetanā kāyasaṅkhāro, vacīsañcetanā vacīsaṅkhāro, manosañcetanā cittasaṅkhāro.":
        "शरीर का इरादा शरीर की रचना है, वाणी का इरादा वाणी की रचना है, मन का इरादा मन की रचना है।",
    "Atthi nāmaṃ, atthi rūpaṃ.": "मानसिक पक्ष भी है, भौतिक रूप भी है।",
    "Atthi jarā, atthi maraṇaṃ.": "बुढ़ापा भी है, मृत्यु भी है।",
    "Iti idañca nāmaṃ, idañca rūpaṃ.": "इस तरह यह मानसिक पक्ष है और यह भौतिक रूप है।",
    "Iti ayañca jarā, idañca maraṇaṃ.": "इस तरह यह बुढ़ापा है और यह मृत्यु है।",
    "Iti ayañca kammabhavo, ayañca upapattibhavo.": "इस तरह यह कर्म रूपी अस्तित्व है और यह पुनर्जन्म रूपी अस्तित्व है।",
    "Bhavo duvidhena – atthi kammabhavo, atthi upapattibhavo.":
        f"अस्तित्व दो प्रकार का है {DASH} कर्म रूपी अस्तित्व भी है, पुनर्जन्म रूपी अस्तित्व भी है।",
    "Sabbampi bhavagāmikammaṃ kammabhavo.": "अस्तित्व की ओर ले जाने वाला सारा कर्म भी कर्म रूपी अस्तित्व है।",
    "Alobho, adoso, amoho.": "लोभ का अभाव, द्वेष का अभाव और मोह का अभाव।",
    "Alobho, adoso.": "लोभ का अभाव और द्वेष का अभाव।",
    "Katame dhammā kusalā?": "हितकर परिघटनाएँ कौन-सी हैं?",                    # pi-1 ^1-1
    "Katame dhammā akusalā?": "हानिकर परिघटनाएँ कौन-सी हैं?",                   # pi-1 ^1-365
    "Katame dhammā abyākatā?": "नैतिक रूप से अनिर्धारित परिघटनाएँ कौन-सी हैं?",   # pi-1 ^1-431
}
SUBSECTION = {  # ##### headings and their closing lines
    "Paccayacatukkaṃ": "कारण के चार रूप",
    "Hetucatukkaṃ": "मूल के चार रूप",
    "Sampayuttacatukkaṃ": "जुड़ाव के चार रूप",
    "Aññamaññacatukkaṃ": "परस्परता के चार रूप",
    "Mātikā": "मूल सूची",                                                     # pi-1 Mātikā
    "Akusalaniddeso": "हानिकर परिघटनाओं का विवरण",
    "Kusalaniddeso": "हितकर परिघटनाओं का विवरण",
    "Abyākataniddeso": "नैतिक रूप से अनिर्धारित परिघटनाओं का विवरण",
    "Avijjāmūlakakusalaniddeso": "अज्ञान से शुरू होने वाला हितकर परिघटनाओं का विवरण",
    "Kusalamūlakavipākaniddeso": "हितकर मूलों से शुरू होने वाला कर्म-फल का विवरण",
    "Akusalamūlakavipākaniddeso": "हानिकर मूलों से शुरू होने वाला कर्म-फल का विवरण",
}
for _p, _h in SUBSECTION.items():
    SENT[_p + "."] = _h + "।"

# ---------------------------------------------------------------- 5. mind-state openings (pi-1 Cittuppādakaṇḍa wording)
ATT = {
    "somanassasahagata": "प्रसन्नता के साथ होने वाला", "upekkhāsahagata": "समभाव के साथ होने वाला",
    "domanassasahagata": "उदासी के साथ होने वाला", "sukhasahagata": "सुख के साथ होने वाला",
    "dukkhasahagata": "दुःख के साथ होने वाला",
    "diṭṭhigatasampayutta": "ग़लत दृष्टि से जुड़ा", "diṭṭhigatavippayutta": "ग़लत दृष्टि से अलग",
    "ñāṇasampayutta": "ज्ञान से जुड़ा", "ñāṇavippayutta": "ज्ञान से अलग",
    "paṭighasampayutta": "चिढ़ से जुड़ा", "vicikicchāsampayutta": "संशय से जुड़ा",
    "uddhaccasampayutta": "बेचैनी से जुड़ा", "sasaṅkhārena": "प्रेरणा सहित",
}
SUBJ = {
    "akusalaṃ cittaṃ": ("हानिकर मन", "m"),
    "kāmāvacaraṃ kusalaṃ cittaṃ": ("इंद्रिय-सुखों के लोक से संबंधित हितकर मन", "m"),
    "cakkhuviññāṇaṃ": ("आँख की चेतना", "f"), "sotaviññāṇaṃ": ("कान की चेतना", "f"),
    "ghānaviññāṇaṃ": ("नाक की चेतना", "f"), "jivhāviññāṇaṃ": ("जीभ की चेतना", "f"),
    "kāyaviññāṇaṃ": ("शरीर की चेतना", "f"),
    "manodhātu": ("मन का तत्व", "m"), "manoviññāṇadhātu": ("मन की चेतना का तत्व", "m"),
}
VIP = {
    "kāmāvacarassa kusalassa": "इंद्रिय-सुखों के लोक से संबंधित हितकर कर्म किए जाने और संचित होने के कारण कर्म के फल रूपी ",
    "akusalassa": "हानिकर कर्म किए जाने और संचित होने के कारण कर्म के फल रूपी ",
}
KIRIYA = "जो केवल क्रिया रूपी है, न हितकर, न हानिकर, न ही कर्म-फल, "                 # pi-1 ^1-568
ARM = [("rūpārammaṇ", "दृश्य रूप", "m"), ("saddārammaṇ", "ध्वनि", "f"), ("gandhārammaṇ", "गंध", "f"),
       ("rasārammaṇ", "स्वाद", "m"), ("phoṭṭhabbārammaṇ", "स्पर्श", "m"), ("dhammārammaṇ", "मन का विषय", "m")]
ANY = "या जिस किसी को भी वह विषय बनाए"
CHUNK = re.compile(
    r"^(?:Yasmiṃ samaye )?"
    r"(?:(?P<vip>kāmāvacarassa kusalassa|akusalassa) kammassa katattā upacitattā vipāk(?:aṃ|ā) )?"
    r"(?:(?P<subj>akusalaṃ cittaṃ|kāmāvacaraṃ kusalaṃ cittaṃ|(?:cakkhu|sota|ghāna|jivhā|kāya)viññāṇaṃ|manodhātu|manoviññāṇadhātu)"
    r" uppann(?:aṃ|ā) hoti ?)?"
    r"(?P<kir>kiriyā neva kusalā nākusalā na ca kammavipākā ?)?"
    r"(?P<rest>.*)$")


def att_key(tok):
    """somanassasahagataṃ / somanassasahagatā -> somanassasahagata"""
    if tok.endswith("ṃ"):
        return tok[:-1]
    if tok.endswith("ā"):
        return tok[:-1] + "a"
    return tok


def _g(text, g):
    return text.replace("वाला", "वाली").replace("जुड़ा", "जुड़ी") if g == "f" else text


def desc(attrs, g):
    a = [_g(ATT[x], g) for x in attrs]
    hota = "होती है" if g == "f" else "होता है"
    if len(a) == 1:
        return f"जो {a[0]} है"
    if len(a) == 2:
        return f"जो {a[0]} और {a[1]} {hota}"
    return f"जो {', '.join(a[:-1])} और {a[-1]} {hota}"


def arm_text(tokens, start):
    objs, anyx = [], False
    i = 0
    while i < len(tokens):
        tk = tokens[i]
        if tk == "yaṃ":
            assert tokens[i:i + 4] == ["yaṃ", "yaṃ", "vā", "panārabbha"], tokens
            anyx = True
            i += 4
            continue
        for pre, hi, g in ARM:
            if tk.startswith(pre):
                objs.append((hi, g))
                break
        else:
            raise KeyError("arm token: " + tk)
        if i + 1 < len(tokens) and tokens[i + 1] == "vā":
            i += 2
        else:
            i += 1
            assert not anyx
            # single object without "vā" (sense consciousness): और जिसका विषय ध्वनि होती है
            assert start and len(tokens) == 1, tokens
            hi, g = objs[0]
            return f"और जिसका विषय {hi} {'होती है' if g == 'f' else 'होता है'}"
    parts = []
    for n, (hi, _) in enumerate(objs):
        if n == 0 and start:
            parts.append(f"और जिसका विषय {hi} हो")
        else:
            parts.append(f"या {hi}")
    if anyx:
        parts.append(ANY)
    return ", ".join(parts)


def citta_head(head):
    chunks = [c.strip() for c in head.split("…pe…")]
    out, g = [], "m"
    for n, c in enumerate(chunks):
        m = CHUNK.match(c)
        rest = m.group("rest").split()
        attrs = []
        while rest and att_key(rest[0]) in ATT:
            attrs.append(att_key(rest.pop(0)))
        text = ""
        if m.group("subj"):
            subj, g = SUBJ[m.group("subj")]
            vip = VIP[m.group("vip")] if m.group("vip") else ""
            text = f"{vip}{subj} उत्पन्न {'होती' if g == 'f' else 'होता'} है, "
            if m.group("kir"):
                text += KIRIYA
            if n == 0:
                text = "जिस समय " + text
        else:
            assert not m.group("vip") and not m.group("kir"), c
        if attrs:
            text += desc(attrs, g)
        if rest:
            text += (" " if attrs else "") + arm_text(rest, start=bool(attrs))
        assert text, c
        out.append(text)
    return "… ".join(out)


# jhāna openings (pi-1 ^1-160, ^1-277, ^1-499, ^1-501, ^1-505, ^1-577, ^1-579, 2-02 ^arūpūpapatti)
J_VIVICCA = "इंद्रिय-सुखों से अलग होकर… "
J_FIRST = "पहले ध्यान को प्राप्त करके उसमें रहता है, "
J_KASINA = "जो पृथ्वी के ध्यान-मंडल वाला है"
J_KASINA_V = "जो पृथ्वी के ध्यान-मंडल वाला [वर्तनी-भेद (Sī., Syā.): paṭhavīkasiṇaṃ] है"
J_ARUPA = "कुछ भी न होने के क्षेत्र को पूरी तरह पार करके, सुख को छोड़ने से… "
J_FOURTH = "चौथे ध्यान को प्राप्त करके उसमें रहता है, "
J_NEVASANNA = "जो न पहचान, न अ-पहचान के क्षेत्र की पहचान के साथ होने वाला है"
J_PATIPADA = "जो दुःखद प्रगति और धीमे उच्च ज्ञान वाला होता है"
J_PATIPADA_S = "जो दुःखद प्रगति और धीमे उच्च ज्ञान वाला और शून्य होता है"
J_RUPU = "जिस समय कोई सूक्ष्म भौतिक लोक में जन्म की ओर ले जाने वाले मार्ग का अभ्यास करता है, "
J_ARUPU = "जिस समय कोई अभौतिक लोक में जन्म की ओर ले जाने वाले मार्ग का अभ्यास करता है, "
J_LOK = ("जिस समय कोई लोकोत्तर ध्यान का अभ्यास करता है, जो मुक्ति की ओर ले जाने वाला और संचय घटाने की ओर ले जाने वाला "
         "होता है, दृष्टियों में फँसने को छोड़ने के लिए और पहले चरण की प्राप्ति के लिए, ")
J_KIR = "जो केवल क्रिया रूपी है, न हितकर, न हानिकर, न ही कर्म-फल, जो इसी जीवन में सुख से रहने के लिए होता है, "
VIP_FIRST = "कर्म के फल रूपी "
P_VIVICCA = "vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja viharati "
P_ARUPA = ("sabbaso ākiñcaññāyatanaṃ samatikkamma nevasaññānāsaññāyatanasaññāsahagataṃ sukhassa ca pahānā…pe… "
           "catutthaṃ jhānaṃ upasampajja viharati")
P_LOK = "lokuttaraṃ jhānaṃ bhāveti niyyānikaṃ apacayagāmiṃ diṭṭhigatānaṃ pahānāya paṭhamāya bhūmiyā pattiyā "
P_KIR = "kiriyaṃ neva kusalaṃ nākusalaṃ na ca kammavipākaṃ diṭṭhadhammasukhavihāraṃ "
JHANA = {
    "Yasmiṃ samaye rūpūpapattiyā maggaṃ bhāveti " + P_VIVICCA + "pathavīkasiṇaṃ":
        J_RUPU + J_VIVICCA + J_FIRST + J_KASINA,
    "Yasmiṃ samaye rūpūpapattiyā maggaṃ bhāveti " + P_VIVICCA + "pathavīkasiṇaṃ [paṭhavīkasiṇaṃ (sī. syā.)]":
        J_RUPU + J_VIVICCA + J_FIRST + J_KASINA_V,
    "Yasmiṃ samaye arūpūpapattiyā maggaṃ bhāveti " + P_ARUPA: J_ARUPU + J_ARUPA + J_FOURTH + J_NEVASANNA,
    "Yasmiṃ samaye " + P_LOK + P_VIVICCA + "dukkhapaṭipadaṃ dandhābhiññaṃ": J_LOK + J_VIVICCA + J_FIRST + J_PATIPADA,
    "Tasseva rūpāvacarassa kusalassa kammassa katattā upacitattā vipākaṃ " + P_VIVICCA + "pathavīkasiṇaṃ":
        "उसी सूक्ष्म भौतिक लोक से संबंधित हितकर कर्म किए जाने और संचित होने के कारण जिस समय वह "
        + J_VIVICCA + VIP_FIRST + J_FIRST + J_KASINA,                                        # pi-1 ^1-499
    "Tasseva arūpāvacarassa kusalassa kammassa katattā upacitattā vipākaṃ " + P_ARUPA:
        "उसी अभौतिक लोक से संबंधित हितकर कर्म किए जाने और संचित होने के कारण जिस समय वह "
        + J_ARUPA + VIP_FIRST + J_FOURTH + J_NEVASANNA,                                      # pi-1 ^1-501
    "Tasseva lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ " + P_VIVICCA + "dukkhapaṭipadaṃ dandhābhiññaṃ":
        "उसी लोकोत्तर हितकर ध्यान के किए जाने और अभ्यास किए जाने के कारण जिस समय वह "
        + J_VIVICCA + VIP_FIRST + J_FIRST + J_PATIPADA,                                      # pi-1 ^1-505
    "Tasseva lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ " + P_VIVICCA + "dukkhapaṭipadaṃ dandhābhiññaṃ suññataṃ":
        "उसी लोकोत्तर हितकर ध्यान के किए जाने और अभ्यास किए जाने के कारण जिस समय वह "
        + J_VIVICCA + VIP_FIRST + J_FIRST + J_PATIPADA_S,
    "Yasmiṃ samaye rūpāvacaraṃ jhānaṃ bhāveti " + P_KIR + P_VIVICCA + "pathavīkasiṇaṃ":
        "जिस समय कोई सूक्ष्म भौतिक लोक से संबंधित ध्यान का अभ्यास करता है, " + J_KIR + J_VIVICCA + J_FIRST + J_KASINA,
    "Yasmiṃ samaye arūpāvacaraṃ jhānaṃ bhāveti " + P_KIR + P_ARUPA:
        "जिस समय कोई अभौतिक लोक से संबंधित ध्यान का अभ्यास करता है, " + J_KIR + J_ARUPA + J_FOURTH + J_NEVASANNA,
}
KUSALA_TAIL = {  # tasmiṃ samaye phasso hoti…pe… avikkhepo hoti – ime dhammā kusalā.
    "phasso hoti…pe… avikkhepo hoti – ime dhammā kusalā.":
        f"संपर्क होता है… भटकाव का अभाव होता है {DASH} ये हितकर परिघटनाएँ हैं।",
}


def head(h):
    h = h.replace(" …pe…", "…pe…")
    if h in JHANA:
        return JHANA[h]
    if "jhānaṃ" in h:
        raise KeyError("jhāna head: " + h)
    return citta_head(h)


# ---------------------------------------------------------------- 6. chains
def chain(s):
    """'Avijjāpaccayā saṅkhāro, saṅkhārapaccayā viññāṇaṃ, … jarāmaraṇaṃ.' -> Hindi"""
    end = ""
    if s.endswith("."):
        s, end = s[:-1], "।"
    s = s[0].lower() + s[1:]
    s = re.sub(r"(?<=[^,;…]) (?=[^\s,;…]+paccayā(?:pi)? )", ", ", s)  # ^2-262: a comma missing in the Pāli
    toks = re.split(r"(, |; |…pe… )", s)
    out = []
    for t in toks:
        if t in (", ", "; "):
            out.append(t)
        elif t == "…pe… ":
            out.append("… ")
        else:
            out.append(chain_item(t))
    return "".join(out) + end


def citation(s):
    """'Nāmapaccayā phassoti.' / 'Nāmarūpapaccayā chaṭṭhāyatananti.' -> “…”।"""
    body = s[:-1]
    if body.endswith("nti"):
        body = body[:-3] + "ṃ"
    elif body.endswith("ti"):
        body = body[:-2]
    else:
        raise KeyError("citation: " + s)
    body = body[0].lower() + body[1:]
    return f"“{chain_item(body)}”।"


# ---------------------------------------------------------------- 7. sentence and line translation
def sentence(s):
    if s in SENT:
        return SENT[s]
    m = re.match(r"^Tattha katam(?:o|ā|aṃ|e) (.+)\?$", s)
    if m:
        return question(m.group(1))
    m = re.match(r"^Tattha katam(?:o|ā|aṃ|e) (.+)$", s)
    if m:  # 'Tattha katamā avijjā…pe… tena vuccati …' / '… phassapaccayā vedanā…pe… ayaṃ vuccati …'
        parts = [p.strip() for p in m.group(1).split("…pe…")]
        k = next(i for i, p in enumerate(parts) if re.match(r"^(ayaṃ|idaṃ|tena) vuccati", p))
        terms, rest = parts[:k], "…pe… ".join(parts[k:])
        nps = [np(x) for x in terms]
        first = f"यहाँ {nps[0][0]} क्या {cop(nps[0][1]['dst'])}"
        return "… ".join([first] + [n for n, _ in nps[1:]] + [answer(rest)])
    low = s.lower()
    if "tasmiṃ samaye " in low:
        if low.startswith("tasmiṃ samaye "):
            h, tail = "", s[len("Tasmiṃ samaye "):]
        else:
            h, tail = s.split(", tasmiṃ samaye ", 1)
        if tail in KUSALA_TAIL:
            tail_hi = KUSALA_TAIL[tail]
        else:
            tail_hi = chain(tail)
        return (head(h) + ", उस समय " if h else "उस समय ") + tail_hi
    if re.match(r"^(Ayaṃ|Idaṃ|Ime|Tena) vucca(?:ti|nti) ", s):
        return answer(s)
    first = s.split()[0]
    if s.endswith("ti.") and "paccayā" in first:
        return citation(s)
    if " – " in s:
        body, ans = s.split(" – ", 1)
        if body not in BODY:
            raise KeyError("body: " + body)
        return f"{BODY[body]} {DASH} {answer(ans)}"
    if "paccayā" in s:
        return chain(s)
    raise KeyError("sentence: " + s)


def split_sentences(line):
    prot = re.sub(r"\[[^\]]*\]", lambda m: m.group(0).replace(".", "\x00"), line)
    return [p.replace("\x00", ".") for p in re.split(r"(?<=[?.])\s+", prot) if p]


HEAD3 = {"Paṭiccasamuppādavibhaṅgo": "### " + S.CHAPTER_TITLES[6]}


def line_hi(text):
    if text.startswith("#"):
        level, title = text.split(" ", 1)
        if level == "###":
            return HEAD3[title]
        if level == "####":
            return "#### " + S.SECTION_TITLES[title]
        return "##### " + SUBSECTION[title]
    return " ".join(sentence(s) for s in split_sentences(text))


# ---------------------------------------------------------------- 8. pi-1 strings reused verbatim (checked in main)
PI1_REUSED = [CITTA_FULL[3:-3], "इरादा, इरादा करना, इरादा कर चुका होना", PHASSA[3:-3], FEEL_SUKHA[3:-3],
              FEEL_ADM[3:-3], FEEL_DOMANASSA[3:-3], FEEL_KAYA_SUKHA[3:-3], FEEL_KAYA_DUKKHA[3:-3],
              "अज्ञान की रुकावट, मोह रूपी हानिकर मूल है", "राग, प्रबल राग, झुकाव, अनुकूल होना, आनंद, आनंद का राग",
              "मन का प्रबल राग", DITTHI_LIST, SADDHA[3:-3], ALOBHA[3:-3], "द्वेष का अभाव, द्वेष न करना, द्वेष से भरा न होना",
              "दुर्भावना का अभाव, दुर्भावना न रखना, द्वेष का अभाव रूपी हितकर मूल है", AMOHA_PE[3:].split("… ")[1],
              AMOHA_LOK, UDDHACCA[3:-3], "उग्रता, कटु वचन", "मन की अप्रसन्नता",
              "शंका, शंका करना, शंका से भरा होना, दुविधा, संशय, दुचित्तापन, दोराहा", "मन का जड़ हो जाना, मन की खरोंच",
              "किसी एक बात को पक्का न पकड़ पाना, हिचकिचाना, बार-बार हिचकिचाना, गहराई में न उतर पाना",
              "बुढ़ापा, जीर्ण होना, दाँतों का टूटना, बालों का पकना, त्वचा पर झुर्रियाँ पड़ना, आयु का घटना, इंद्रियों का पूरी तरह पक जाना",
              "क्षय, नाश, टूटना, बिखर जाना, अनित्यता, लुप्त हो जाना",
              "या जो भी अन्य भौतिक रूप मन से जन्मा, मन के कारण होने वाला और मन से उत्पन्न है",
              "इंद्रिय-सुखों के प्रति आसक्ति, दृष्टियों के प्रति आसक्ति, सदाचार और व्रतों के प्रति आसक्ति, आत्मा के सिद्धांत के प्रति आसक्ति",
              "दुःख को न जानना, दुःख की उत्पत्ति को न जानना, दुःख के अंत को न जानना, दुःख के अंत की ओर ले जाने वाले प्रगति के ढंग को न जानना",
              SENT["Avijjāpaccayā saṅkhārā, saṅkhārapaccayā viññāṇaṃ, viññāṇapaccayā nāmarūpaṃ, nāmarūpapaccayā saḷāyatanaṃ, "
                   "saḷāyatanapaccayā phasso, phassapaccayā vedanā, vedanāpaccayā taṇhā, taṇhāpaccayā upādānaṃ, upādānapaccayā bhavo, "
                   "bhavapaccayā jāti, jātipaccayā jarāmaraṇaṃ sokaparidevadukkhadomanassupāyāsā sambhavanti."][:-12],
              DUKKHA_SAMUDAYA, "जिस समय हानिकर मन उत्पन्न होता है, जो प्रसन्नता के साथ होने वाला और ग़लत दृष्टि से जुड़ा होता है",
              "जो उदासी के साथ होने वाला और चिढ़ से जुड़ा होता है", "जो समभाव के साथ होने वाला और संशय से जुड़ा होता है",
              "जो समभाव के साथ होने वाला और बेचैनी से जुड़ा होता है",
              "प्रसन्नता के साथ होने वाला, ग़लत दृष्टि से जुड़ा और प्रेरणा सहित होता है",
              "जिस समय इंद्रिय-सुखों के लोक से संबंधित हितकर मन उत्पन्न होता है, जो प्रसन्नता के साथ होने वाला और ज्ञान से जुड़ा होता है",
              "और जिसका विषय दृश्य रूप हो, या ध्वनि, या गंध, या स्वाद, या स्पर्श, या मन का विषय, या जिस किसी को भी वह विषय बनाए",
              "इंद्रिय-सुखों के लोक से संबंधित हितकर कर्म किए जाने और संचित होने के कारण कर्म के फल रूपी आँख की चेतना उत्पन्न होती है, "
              "जो समभाव के साथ होने वाली है और जिसका विषय दृश्य रूप होता है",
              "जो समभाव के साथ होने वाली है और जिसका विषय ध्वनि होती है", "जो सुख के साथ होने वाली है और जिसका विषय स्पर्श होता है",
              "हानिकर कर्म किए जाने और संचित होने के कारण कर्म के फल रूपी मन का तत्व उत्पन्न होता है, जो समभाव के साथ होने वाला है",
              "मन की चेतना का तत्व उत्पन्न होता है, जो केवल क्रिया रूपी है, न हितकर, न हानिकर, न ही कर्म-फल, जो प्रसन्नता के साथ होने वाला है",
              J_RUPU + J_VIVICCA + J_FIRST + J_KASINA, J_LOK + J_VIVICCA + J_FIRST + J_PATIPADA,
              "उसी सूक्ष्म भौतिक लोक से संबंधित हितकर कर्म किए जाने और संचित होने के कारण जिस समय वह " + J_VIVICCA + VIP_FIRST + J_FIRST,
              "उसी लोकोत्तर हितकर ध्यान के किए जाने और अभ्यास किए जाने के कारण जिस समय वह " + J_VIVICCA + VIP_FIRST + J_FIRST,
              "जिस समय कोई सूक्ष्म भौतिक लोक से संबंधित ध्यान का अभ्यास करता है, " + J_KIR + J_VIVICCA + J_FIRST + J_KASINA,
              "अभौतिक लोक में जन्म की ओर ले जाने वाले मार्ग का अभ्यास करता है, कुछ भी न होने के क्षेत्र को पूरी तरह पार करके, सुख को छोड़ने से… चौथे ध्यान को प्राप्त करके उसमें रहता है, जो न पहचान, न अ-पहचान के क्षेत्र की पहचान के साथ होने वाला",
              "संपर्क होता है… भटकाव का अभाव होता है", "हितकर परिघटनाएँ कौन-सी हैं?", "हानिकर परिघटनाएँ कौन-सी हैं?",
              "नैतिक रूप से अनिर्धारित परिघटनाएँ कौन-सी हैं?"]


def check_pi1():
    d = S.PI1_HI_DIR
    corpus = "\n".join(open(os.path.join(d, f), encoding="utf-8-sig").read() for f in os.listdir(d) if f.endswith(".md"))
    corpus = re.sub(r"\s*\[[^\]]*\]", "", corpus)
    missing = [x for x in PI1_REUSED if re.sub(r"\s*\[[^\]]*\]", "", x) not in corpus]
    assert not missing, "not found in pi-1 Hindi:\n" + "\n".join(missing)


def main():
    check_pi1()
    src = open(os.path.join(S.PALI_DIR, CH), encoding="utf-8").read().splitlines()
    out, errors = [], []
    for i, p in enumerate(src):
        if not p.strip():
            out.append("")
            continue
        if p.startswith("#### Abhidhammabhājanīyaṃ"):
            MODE["sutta"] = False
        m = S.ID.search(p)
        text = S.ID.sub("", p) if m else p
        try:
            h = line_hi(text)
        except (KeyError, AssertionError, AttributeError, StopIteration) as e:
            errors.append(f"line {i + 1}: {type(e).__name__}: {e}")
            h = "???"
        if m:
            h += " " + m.group(1)
        out.append(h)
    if errors:
        print("\n".join(errors[:40]))
        print("errors:", len(errors))
        sys.exit(1)
    while out and not out[-1]:
        out.pop()
    path = os.path.join(S.HI_DIR, CH)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out) + "\n")
    print("written", path)


if __name__ == "__main__":
    main()
