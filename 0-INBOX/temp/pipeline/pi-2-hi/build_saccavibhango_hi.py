# -*- coding: utf-8 -*-
"""pi-2 Vibhaṅga, chapter 4 (Saccavibhaṅga), Hindi plain zero-shot.

usage: python -I -X utf8 build_saccavibhango_hi.py
Writes AI_translation\\hindi\\pi-2-hindi-plain-zeroshot_split_chapters\\4-saccavibhango.md
Block IDs are copied from the Pāli. Every repeated passage is one fixed string or one function, so the
repeats are byte-identical. pi-1 strings: jhāna formulas (^1-160 … ^1-17x), lokuttara path factors (^1-292,
^1-283, ^1-299 … ^1-301, ^1-289 … ^1-291), sammappadhāna (^1-1377), jarā (^1-643), dukkha/domanassa feeling
strings (^1-558, ^1-415). pi-5 strings: the truth names, the craving formula (^5-679).
"""
import sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-hi")
from common_ch2_ch4_hi import S, DASH, check_in_pi, write_chapter, pali_lines, strip_id, join_and, PI1_HI_DIR, PI5_HI_DIR
import matrix_ch2_ch4_hi as M
import subjects_ch2_ch4_hi as SJ

NAME = "4-saccavibhango.md"

# ---------------------------------------------------------------- names (pi-5)
DUKKHA = "दुःख"
SAMUDAYA = "दुःख की उत्पत्ति"
NIRODHA = "दुःख का अंत"
PATIPADA = "दुःख के अंत की ओर ले जाने वाला मार्ग"
PATIPADA_OBL = "दुःख के अंत की ओर ले जाने वाले मार्ग"
AS = "आर्य सत्य"
TRUTH = {"dukkha": f"{DUKKHA} {AS}", "samudaya": f"{SAMUDAYA} {AS}", "nirodha": f"{NIRODHA} {AS}",
         "magga": f"{PATIPADA} {AS}"}
HEAD = {"dukkha": "दुःख का सत्य", "samudaya": "उत्पत्ति का सत्य", "nirodha": "दुःख के अंत का सत्य",
        "magga": "मार्ग का सत्य"}          # Dukkhasaccaṃ … Maggasaccaṃ (pi-5 ^5-452, 10-dutiyavaggo)


def kaha(x, f=False, pl=False):
    """Idaṃ/Ayaṃ vuccati "X" -> यह “X” कहा/कही जाता/जाती है।"""
    if pl:
        return f"ये “{x}” कहे जाते हैं।"
    return f"यह “{x}” {'कही जाती' if f else 'कहा जाता'} है।"


def q(x, f=False):
    return f"यहाँ {x} क्या है?"


FOUR_ARIYA = f"चार {AS} {DASH} " + ", ".join(TRUTH[k] for k in ("dukkha", "samudaya", "nirodha", "magga")) + "।"
FOUR_ARIYA_VAR = (f"चार {AS} {DASH} {TRUTH['dukkha']}, {SAMUDAYA} [वर्तनी-भेद (Syā.): dukkhasamudayo] {AS}, "
                  f"{NIRODHA} [वर्तनी-भेद (Syā.): dukkhanirodho] {AS}, {TRUTH['magga']}।")
FOUR = f"चार सत्य {DASH} {DUKKHA}, {SAMUDAYA}, {NIRODHA}, {PATIPADA}।"

# ---------------------------------------------------------------- dukkha sacca (Suttanta)
GRIEF5 = "शोक, विलाप, दुःख, उदासी और निराशा"                                   # pi-5 ^5-452
UPADANA_KHANDHA = "आसक्ति का विषय बनने वाले पाँच समूह"                       # pañcupādānakkhandhā
APPIYA = "अप्रिय से संयोग रूपी दुःख"                                           # appiyehi sampayogo dukkho
PIYA = "प्रिय से वियोग रूपी दुःख"
YAMPICCHAM = "जो चाहता है, वह न मिलना भी दुःख है"                            # yampicchaṃ na labhati tampi dukkhaṃ
SANKHITTENA = f"संक्षेप में दुःख रूपी, {UPADANA_KHANDHA}"
STHA = "उन-उन प्राणियों का उस-उस प्राणी-वर्ग में"                             # tesaṃ tesaṃ sattānaṃ tamhi tamhi sattanikāye
BYASANA = ("संबंधियों की हानि से पीड़ित, धन-संपत्ति की हानि से पीड़ित, रोग की विपत्ति से पीड़ित, "
           "सदाचार की हानि से पीड़ित या दृष्टि की हानि से पीड़ित, किसी न किसी विपत्ति से घिरे, "
           "किसी न किसी दुःखद परिघटना से पीड़ित व्यक्ति का")
KAYIKA_DUKKHA = ("शारीरिक असुहावनापन, शारीरिक दुःख, शरीर के संपर्क से उत्पन्न असुहावना दुःखद अनुभव, "
                 "शरीर के संपर्क से उत्पन्न असुहावनी दुःखद अनुभूति")                     # pi-1 ^1-558
CETASIKA_DUKKHA = ("मानसिक असुहावनापन, मानसिक दुःख, मन के संपर्क से उत्पन्न असुहावना दुःखद अनुभव, "
                   "मन के संपर्क से उत्पन्न असुहावनी दुःखद अनुभूति")                       # pi-1 ^1-415
JARA = ("बुढ़ापा, जीर्ण होना, दाँतों का टूटना, बालों का पकना, त्वचा पर झुर्रियाँ पड़ना, आयु का घटना, "
        "इंद्रियों का पूरी तरह पक जाना")                                                     # pi-1 ^1-643
FIVE_OBJ = "दृश्य रूप, ध्वनियाँ, गंध, स्वाद और स्पर्श"                                  # rūpā saddā gandhā rasā phoṭṭhabbā
NOT_GET = "पर यह इच्छा करने से नहीं मिल सकता।"                                         # Na kho panetaṃ icchāya pattabbaṃ.


def wish(nature, plural_noun=None, verb="आता"):
    """… sattānaṃ evaṃ icchā uppajjati – "aho vata, mayaṃ na …dhammā assāma; na ca, vata, no … āgaccheyyā"ti!"""
    return (f"ऐसी इच्छा उत्पन्न होती है {DASH} “अहा, काश हम {nature} के स्वभाव वाले न होते; और काश हमारे पास "
            f"{plural_noun or nature} न {verb}”!")


def dukkha_lines():
    return [
        "##### " + HEAD["dukkha"],
        (f"यहाँ {TRUTH['dukkha']} क्या है? जन्म भी दुःख है, बुढ़ापा भी दुःख है, मृत्यु भी दुःख है, "
         f"{GRIEF5} भी दुःख हैं, अप्रिय से संयोग दुःख है, प्रिय से वियोग दुःख है, {YAMPICCHAM}, "
         f"संक्षेप में {UPADANA_KHANDHA} दुःख हैं।"),
        (f"यहाँ जन्म क्या है? {STHA} जो जन्म, भली-भाँति जन्म, प्रवेश, पूरी तरह पैदा होना, समूहों का प्रकट होना, "
         f"इंद्रिय-क्षेत्रों की प्राप्ति है {DASH} {kaha('जन्म')}"),
        f"यहाँ बुढ़ापा क्या है? {STHA} जो {JARA} है {DASH} {kaha('बुढ़ापा')}",
        (f"यहाँ मृत्यु क्या है? उन-उन प्राणियों का उस-उस प्राणी-वर्ग से जो च्युत होना, चल बसना, टूट जाना, लुप्त हो जाना, "
         f"मौत, मरना, देह छोड़ना, समूहों का बिखर जाना, शरीर का गिर जाना, जीवन-क्षमता का कट जाना है {DASH} "
         f"{kaha('मृत्यु', f=True)}"),
        (f"यहाँ शोक क्या है? {BYASANA} जो शोक, शोक करना, शोक में डूबे रहना, भीतर का शोक, भीतर का गहरा शोक, "
         f"मन का जलना, उदासी, शोक का काँटा है {DASH} {kaha('शोक')}"),
        (f"यहाँ विलाप क्या है? {BYASANA} जो रोना, विलाप, रोना-धोना, विलाप करना, रोते रहना, विलाप करते रहना, "
         f"बोल पड़ना, बड़बड़ाना, अनाप-शनाप बोलना, बिलखना, बिलख-बिलखकर रोना, बिलखते रहना "
         f"[वर्तनी-भेद (Syā.): lālapo lālapanā lālapitattaṃ] है {DASH} {kaha('विलाप')}"),
        f"यहाँ दुःख क्या है? जो {KAYIKA_DUKKHA} है {DASH} {kaha('दुःख')}",
        f"यहाँ उदासी क्या है? जो {CETASIKA_DUKKHA} है {DASH} {kaha('उदासी', f=True)}",
        (f"यहाँ निराशा क्या है? {BYASANA} जो परेशानी, निराशा, परेशान रहना, निराश रहना है {DASH} "
         f"{kaha('निराशा', f=True)}"),
        (f"यहाँ {APPIYA} क्या है? यहाँ जिसके लिए अनचाहे, अप्रिय, मन को न भाने वाले {FIVE_OBJ} होते हैं, "
         f"या जो लोग उसका अनर्थ चाहने वाले, अहित चाहने वाले, असुविधा चाहने वाले, उसका कुशल-क्षेम न चाहने वाले होते हैं; "
         f"उनके साथ जो मिलना, एक साथ आना, साथ रहना, घुल-मिल जाना है {DASH} {kaha(APPIYA)}"),
        (f"यहाँ {PIYA} क्या है? यहाँ जिसके लिए मनचाहे, प्रिय, मनभावन {FIVE_OBJ} होते हैं, "
         f"या जो लोग उसका भला चाहने वाले, हित चाहने वाले, सुविधा चाहने वाले, उसका कुशल-क्षेम चाहने वाले होते हैं, "
         f"जैसे माता या पिता या भाई या बहन या मित्र या साथी या संबंधी या रक्त-संबंधी; "
         f"उनके साथ जो न मिलना, एक साथ न आना, साथ न रहना, घुल-मिल न पाना है {DASH} {kaha(PIYA)}"),
        (f"यहाँ “{YAMPICCHAM}” क्या है? जन्म के स्वभाव वाले प्राणियों में {wish('जन्म')} {NOT_GET} "
         f"यह भी “{YAMPICCHAM}” कहा जाता है।"),
        (f"बुढ़ापे के स्वभाव वाले प्राणियों में… रोग के स्वभाव वाले प्राणियों में… मृत्यु के स्वभाव वाले प्राणियों में… "
         f"{GRIEF5} के स्वभाव वाले प्राणियों में {wish(GRIEF5, verb='आते')} {NOT_GET} "
         f"यह भी “{YAMPICCHAM}” कहा जाता है।"),
        (f"यहाँ {SANKHITTENA} कौन-से हैं? यानी {DASH} "
         + ", ".join(f"आसक्ति का विषय बनने वाला {S.AGG[a]['khandha']}" for a in ("rupa", "vedana", "sanna", "sankhara", "vinnana"))
         + f"। {kaha(SANKHITTENA, pl=True)}"),
        kaha(TRUTH["dukkha"]),
    ]


# ---------------------------------------------------------------- samudaya / nirodha (Suttanta)
TANHA_DEF = ("यह जो तृष्णा बार-बार पुनर्जन्म दिलाने वाली [वर्तनी-भेद (Syā., Ka.): ponobbhavikā] है, आनंद और राग से युक्त है, "
             f"जहाँ-तहाँ आनंद लेने वाली है, यानी {DASH} इंद्रिय-सुखों की तृष्णा, अस्तित्व की तृष्णा, अनस्तित्व की तृष्णा।")  # pi-5 ^5-679
PIYA_RUPA = "प्रिय लगने वाली, सुहावनी लगने वाली चीज़"                    # piyarūpaṃ sātarūpaṃ
LOKE = "संसार में"
ARISE = "यहीं यह तृष्णा उत्पन्न होते समय उत्पन्न होती है, यहीं टिकते समय टिकती है।"      # Etthesā taṇhā uppajjamānā …
CEASE = "यहीं यह तृष्णा छूटते समय छूटती है, यहीं समाप्त होते समय समाप्त होती है।"       # Etthesā taṇhā pahīyamānā …
SENSE6 = ["आँख", "कान", "नाक", "जीभ", "शरीर", "मन"]
OBJ6 = ["दृश्य रूप", "ध्वनि", "गंध", "स्वाद", "स्पर्श", "मन के विषयों"]
OBJ6_PL = ["दृश्य रूप", "ध्वनियाँ", "गंध", "स्वाद", "स्पर्श", "मन के विषय"]   # Rūpā saddā … dhammā (plural)
GROUPS = [  # (list of six names, plural?)
    (SENSE6, False),
    (OBJ6_PL, True),
    ([f"{s} की चेतना" for s in SENSE6], False),
    ([f"{s} का संपर्क" for s in SENSE6], False),
    ([f"{s} के संपर्क से उत्पन्न अनुभूति" for s in SENSE6], False),
    ([f"{o} की पहचान" for o in OBJ6], False),
    ([f"{o} के बारे में इरादा" for o in OBJ6], False),
    ([f"{o} की तृष्णा" for o in OBJ6], False),
    ([f"{o} के बारे में आरंभिक विचार" for o in OBJ6], False),
    ([f"{o} के बारे में सतत विचार" for o in OBJ6], False),
]


def is_piya(x, pl):
    return f"{LOKE} {x} {PIYA_RUPA} {'हैं' if pl else 'है'}।"


def group_line(names, pl, tail, mode):
    """mode 'full': first spelled out + tail, '…' chain, last + tail ('X loke. Etthesā… Y loke…pe… Z loke piyarūpaṃ…');
    'chain': chain only, last + tail; 'all': every item spelled out with its tail."""
    if mode == "all":
        return " ".join(f"{is_piya(n, pl)} {tail}" for n in names)
    chain = "… ".join(f"{LOKE} {n}" for n in names[1:-1]) + "… "
    last = f"{is_piya(names[-1], pl)} {tail}"
    if mode == "full":
        return f"{is_piya(names[0], pl)} {tail} {LOKE} {names[1]}… " + "… ".join(f"{LOKE} {n}" for n in names[2:-1]) + "… " + last
    return f"{LOKE} {names[0]}… " + chain + last


def samudaya_lines():
    L = ["##### " + HEAD["samudaya"],
         f"यहाँ {TRUTH['samudaya']} क्या है? {TANHA_DEF}",
         (f"यह तृष्णा उत्पन्न होते समय कहाँ उत्पन्न होती है, टिकते समय कहाँ टिकती है? "
          f"{LOKE} जो {PIYA_RUPA} है, वहीं यह तृष्णा उत्पन्न होते समय उत्पन्न होती है, वहीं टिकते समय टिकती है।"),
         f"और {LOKE} {PIYA_RUPA} क्या है? " + group_line(*GROUPS[0], ARISE, "full")]
    for names, pl in GROUPS[1:9]:
        L.append(group_line(names, pl, ARISE, "full"))
    L.append(group_line(*GROUPS[9], ARISE, "all"))
    L.append(kaha(TRUTH["samudaya"]))
    return L


def nirodha_lines():
    L = ["##### " + HEAD["nirodha"],
         (f"यहाँ {TRUTH['nirodha']} क्या है? उसी तृष्णा का जो पूरी तरह फीका पड़कर समाप्त हो जाना, त्याग, छोड़ देना, "
          f"उससे मुक्ति और उसमें लगाव का न रहना है।"),
         (f"यह तृष्णा छूटते समय कहाँ छूटती है, समाप्त होते समय कहाँ समाप्त होती है? "
          f"{LOKE} जो {PIYA_RUPA} है, वहीं यह तृष्णा छूटते समय छूटती है, वहीं समाप्त होते समय समाप्त होती है।"),
         f"और {LOKE} {PIYA_RUPA} क्या है? " + group_line(*GROUPS[0], CEASE, "full")]
    for names, pl in GROUPS[1:5]:
        L.append(group_line(names, pl, CEASE, "full"))
    for names, pl in GROUPS[5:10]:
        L.append(group_line(names, pl, CEASE, "chain"))
    L.append(kaha(TRUTH["nirodha"]))
    return L


# ---------------------------------------------------------------- magga sacca (Suttanta)
FACTORS = ["सही दृष्टि", "सही संकल्प", "सही वाणी", "सही कर्म", "सही आजीविका", "सही प्रयास", "सही सजगता", "सही एकाग्रता"]
FEM = {"सही दृष्टि", "सही वाणी", "सही आजीविका", "सही सजगता", "सही एकाग्रता"}
PADH_V = "चाह जगाता है, प्रयास करता है, उत्साह जगाता है, मन को तत्पर करता है, पूरा ज़ोर लगाता है"   # pi-1 ^1-1377
SATI_TAIL = "तत्पर, स्पष्ट समझ रखते हुए और सजग, संसार के प्रति लालच और उदासी को दूर करके"
JHANA1 = ("इंद्रिय-सुखों से अलग होकर, हानिकर परिघटनाओं से अलग होकर, आरंभिक विचार और सतत विचार वाले, "
          "अलगाव से उत्पन्न उल्लास और सुख वाले पहले ध्यान को प्राप्त करके उसमें रहता है")                 # pi-1 ^1-160
JHANA2 = ("आरंभिक विचार और सतत विचार के शांत होने से, स्वयं में निर्मलता वाले, मन के एक बिंदु पर टिकने वाले, "
          "आरंभिक विचार और सतत विचार से रहित, एकाग्रता से उत्पन्न उल्लास और सुख वाले दूसरे ध्यान को प्राप्त करके उसमें रहता है")
JHANA3 = ("उल्लास के फीका पड़ने से वह समभाव के साथ, सजग और स्पष्ट समझ रखते हुए रहता है और काया से सुख का अनुभव करता है, "
          f"जिसके बारे में आर्य कहते हैं {DASH} “समभाव वाला, सजगता वाला, सुख से रहने वाला”, ऐसे तीसरे ध्यान को प्राप्त करके उसमें रहता है")
JHANA4 = ("सुख को छोड़ने से और दुःख को छोड़ने से, और पहले ही प्रसन्नता और उदासी के मिट जाने से, न दुःखद, न सुखद, "
          "समभाव और सजगता से पूरी तरह शुद्ध चौथे ध्यान को प्राप्त करके उसमें रहता है")


def fq(x):
    return f"यहाँ {x} क्या है?"


def fk(x):
    return kaha(x, f=x in FEM)


def magga_lines():
    return [
        "##### " + HEAD["magga"],
        f"यहाँ {TRUTH['magga']} क्या है? यही आर्य अष्टांगिक मार्ग, यानी {DASH} " + ", ".join(FACTORS) + "।",
        (f"{fq('सही दृष्टि')} दुःख का ज्ञान, दुःख की उत्पत्ति का ज्ञान, दुःख के अंत का ज्ञान, {PATIPADA_OBL} का ज्ञान "
         f"{DASH} {fk('सही दृष्टि')}"),
        f"{fq('सही संकल्प')} त्याग का संकल्प, दुर्भावना के अभाव का संकल्प, अहिंसा का संकल्प {DASH} {fk('सही संकल्प')}",
        (f"{fq('सही वाणी')} झूठ बोलने से दूर रहना, चुगली से दूर रहना, कठोर वाणी से दूर रहना, व्यर्थ की बकवास से दूर रहना "
         f"{DASH} {fk('सही वाणी')}"),
        (f"{fq('सही कर्म')} जीव-हत्या से दूर रहना, न दी गई वस्तु लेने से दूर रहना, इंद्रिय-सुखों में दुराचार से दूर रहना "
         f"{DASH} {fk('सही कर्म')}"),
        (f"{fq('सही आजीविका')} यहाँ आर्य शिष्य ग़लत आजीविका को छोड़कर सही आजीविका से जीवन-यापन करता है "
         f"{DASH} {fk('सही आजीविका')}"),
        (f"{fq('सही प्रयास')} यहाँ भिक्षु उत्पन्न न हुई बुरी हानिकर परिघटनाओं को उत्पन्न न होने देने के लिए {PADH_V}। "
         f"उत्पन्न हो चुकी बुरी हानिकर परिघटनाओं को छोड़ने के लिए {PADH_V}। "
         f"उत्पन्न न हुई हितकर परिघटनाओं की उत्पत्ति के लिए {PADH_V}। "
         f"उत्पन्न हो चुकी हितकर परिघटनाओं की स्थिरता के लिए, उनके लुप्त न होने के लिए, उन्हें और बढ़ाने के लिए, "
         f"उनकी विपुलता के लिए, उनके अभ्यास के लिए, उनकी परिपूर्णता के लिए {PADH_V}। {fk('सही प्रयास')}"),
        (f"{fq('सही सजगता')} यहाँ भिक्षु शरीर में शरीर का अवलोकन करते हुए रहता है, {SATI_TAIL}। "
         f"अनुभूतियों में… मन में… मन के विषयों में मन के विषयों का अवलोकन करते हुए रहता है, {SATI_TAIL}। {fk('सही सजगता')}"),
        f"{fq('सही एकाग्रता')} यहाँ भिक्षु {JHANA1}। {JHANA2}। {JHANA3}। {JHANA4}। {fk('सही एकाग्रता')}",
        kaha(TRUTH["magga"]),
        S.SECTION_TITLES["Suttantabhājanīyaṃ"] + "।",
    ]


# ---------------------------------------------------------------- Abhidhammabhājanīya
A_KILESA = ("शेष मन के क्लेश", "शेष मन के क्लेशों")
B_AKUSALA = ("शेष हानिकर परिघटनाएँ", "शेष हानिकर परिघटनाओं")
C_MULA = ("मन के मैलों का विषय बनने वाले तीन हितकर मूल", "मन के मैलों का विषय बनने वाले तीन हितकर मूलों")
D_KUSALA = ("मन के मैलों का विषय बनने वाली शेष हितकर परिघटनाएँ", "मन के मैलों का विषय बनने वाली शेष हितकर परिघटनाओं")
E_VIPAKA = "मन के मैलों का विषय बनने वाली, हितकर और हानिकर कर्म के फल रूपी परिघटनाएँ"              # pi-1 ^1-583
F_KIRIYA = "जो परिघटनाएँ केवल क्रिया रूपी हैं, न हितकर, न हानिकर, न ही कर्म-फल रूपी"                  # pi-1 ^1-583
G_RUPA = "सारा भौतिक रूप"
TANHA = ("तृष्णा", "तृष्णा")
STEPS = [A_KILESA, B_AKUSALA, C_MULA, D_KUSALA]


def samudaya_def(k):
    """k = number of extra items after craving (0 … 4)."""
    items = [TANHA[0]] + [x[0] for x in STEPS[:k]]
    return f"यहाँ {SAMUDAYA} क्या है? {join_and(items)} {DASH} {kaha(SAMUDAYA, f=True)}"


def dukkha_def(k):
    items = [x[0] for x in STEPS[k:]] + [E_VIPAKA, F_KIRIYA]
    return f"यहाँ {DUKKHA} क्या है? " + ", ".join(items) + f", और {G_RUPA} {DASH} {kaha(DUKKHA)}"


def nirodha_def(k):
    items = [TANHA[1]] + [x[1] for x in STEPS[:k]]
    return f"यहाँ {NIRODHA} क्या है? {join_and(items)} को छोड़ देना {DASH} {kaha(NIRODHA)}"


LOKUTTARA = ("यहाँ जिस समय भिक्षु लोकोत्तर ध्यान का अभ्यास करता है, जो मुक्ति की ओर ले जाने वाला और संचय घटाने की ओर "
             "ले जाने वाला होता है, दृष्टियों में फँसने को छोड़ने के लिए और पहले चरण की प्राप्ति के लिए, "
             "इंद्रिय-सुखों से अलग होकर… पहले ध्यान को प्राप्त करके उसमें रहता है, जो दुःखद प्रगति और धीमे उच्च ज्ञान वाला होता है, "
             "उस समय")                                                                                        # pi-1 ^1-277
AVASESA = f"शेष परिघटनाएँ {PATIPADA_OBL} से जुड़ी हैं।"
PANCA = ["सही दृष्टि", "सही संकल्प", "सही प्रयास", "सही सजगता", "सही एकाग्रता"]
MAGGA_DEFS = {
    "sammādiṭṭhi": f"{fq('सही दृष्टि')} जो प्रज्ञा, जानना… मोह का अभाव, परिघटनाओं की छानबीन, सही दृष्टि, "
                   f"परिघटनाओं की छानबीन नामक जागृति का अंग, मार्ग का अंग, मार्ग में समाया हुआ है {DASH} {fk('सही दृष्टि')}",
    "sammāsaṅkappo": f"{fq('सही संकल्प')} जो सोचना, आरंभिक विचार… सही संकल्प, मार्ग का अंग, मार्ग में समाया हुआ है "
                     f"{DASH} {fk('सही संकल्प')}",
    "sammāvācā": f"{fq('सही वाणी')} जो वाणी के चार दुराचरणों से दूर रहना, विरत रहना, पूरी तरह विरत रहना, बचना "
                 f"[वर्तनी-भेद (Ka.): veramaṇi, आगे भी इसी तरह], न करना, न अपनाना, दोष में न पड़ना, मर्यादा का उल्लंघन न करना, "
                 f"पुल को तोड़ देना, सही वाणी, मार्ग का अंग, मार्ग में समाया हुआ है {DASH} {fk('सही वाणी')}",
    "sammākammanto": f"{fq('सही कर्म')} जो शरीर के तीन दुराचरणों से दूर रहना, विरत रहना, पूरी तरह विरत रहना, बचना, न करना, "
                     f"न अपनाना, दोष में न पड़ना, मर्यादा का उल्लंघन न करना, पुल को तोड़ देना, सही कर्म, मार्ग का अंग, "
                     f"मार्ग में समाया हुआ है {DASH} {fk('सही कर्म')}",
    "sammāājīvo": f"{fq('सही आजीविका')} जो ग़लत आजीविका से दूर रहना, विरत रहना, पूरी तरह विरत रहना, बचना, न करना, "
                  f"न अपनाना, दोष में न पड़ना, मर्यादा का उल्लंघन न करना, पुल को तोड़ देना, सही आजीविका, मार्ग का अंग, "
                  f"मार्ग में समाया हुआ है {DASH} {fk('सही आजीविका')}",
    "sammāvāyāmo_var": f"{fq('सही प्रयास')} जो मानसिक रूप से उत्साह जगाना [वर्तनी-भेद (Sī., Syā.): viriyārambho]… "
                       f"सही प्रयास, उत्साह नामक जागृति का अंग, मार्ग का अंग, मार्ग में समाया हुआ है {DASH} {fk('सही प्रयास')}",
    "sammāvāyāmo": f"{fq('सही प्रयास')} जो मानसिक रूप से उत्साह जगाना… सही प्रयास, उत्साह नामक जागृति का अंग, "
                   f"मार्ग का अंग, मार्ग में समाया हुआ है {DASH} {fk('सही प्रयास')}",
    "sammāsati": f"{fq('सही सजगता')} जो सजगता, बार-बार स्मरण… सही सजगता, सजगता नामक जागृति का अंग, मार्ग का अंग, "
                 f"मार्ग में समाया हुआ है {DASH} {fk('सही सजगता')}",
    "sammāsamādhi_2": f"{fq('सही एकाग्रता')} जो मन की स्थिरता, ठहराव… सही एकाग्रता, एकाग्रता नामक जागृति का अंग, "
                      f"मार्ग का अंग, मार्ग में समाया हुआ है {DASH} {fk('सही एकाग्रता')}",
    "sammāsamādhi_1": f"{fq('सही एकाग्रता')} जो मन की स्थिरता… सही एकाग्रता, एकाग्रता नामक जागृति का अंग, "
                      f"मार्ग का अंग, मार्ग में समाया हुआ है {DASH} {fk('सही एकाग्रता')}",
}
PATIPADA_IS = kaha(PATIPADA)


def patipada_def(kind, dash_list=True):
    """kind: '8' (aṭṭhaṅgiko …pe…), '5' (pañcaṅgiko, five spelled out), 'phassa' (phasso hoti…pe… avikkhepo hoti)."""
    if kind == "8":
        lst = f"अष्टांगिक मार्ग होता है {DASH} सही दृष्टि… सही एकाग्रता" if dash_list else \
              "अष्टांगिक मार्ग होता है, यानी सही दृष्टि… सही एकाग्रता"
    elif kind == "5":
        lst = f"पाँच अंगों वाला मार्ग होता है {DASH} " + ", ".join(PANCA)
    else:
        lst = "संपर्क होता है… भटकाव का अभाव होता है"
    return f"यहाँ {PATIPADA} क्या है? {LOKUTTARA} {lst}।"


def abhidhamma_lines(P):
    """built from the Pāli line by line (the five/six cycles differ in small details)."""
    H = []
    for p in P:
        t = strip_id(p)
        if t.startswith("Cattāri saccāni"):
            H.append(FOUR)
        elif t.startswith("Tattha katamo dukkhasamudayo?"):
            H.append(samudaya_def(t.lower().count("avasesā ca") + t.lower().count("tīṇi ca")))
        elif t.startswith("Tattha katamaṃ dukkhaṃ?"):
            # which of the leading items are still present: kilesa, akusala, mūla, kusala
            tl = t.lower()
            present = [("avasesā ca kilesā" in tl), ("avasesā ca akusalā" in tl), ("tīṇi ca kusalamūlāni" in tl),
                       ("avasesā ca sāsavā kusalā" in tl)]
            k = present.index(True) if True in present else 4
            assert all(present[k:]), t
            H.append(dukkha_def(k))
        elif t.startswith("Tattha katamo dukkhanirodho?"):
            k = t.lower().count("avasesānañca") + t.lower().count("tiṇṇañca")
            H.append(nirodha_def(k))
        elif t.startswith("Tattha katamā dukkhanirodhagāminī paṭipadā?"):
            if "pañcaṅgiko" in t:
                line = patipada_def("5")
            elif "phasso hoti" in t:
                line = patipada_def("phassa")
            else:
                line = patipada_def("8", dash_list="hoti – sammādiṭṭhi" in t)
            if t.endswith("sammāsamādhi."):
                pass
            elif 'Ayaṃ vuccati – "dukkhanirodhagāminī paṭipadā". Avasesā' in t:
                line += f" यह कहा जाता है {DASH} “{PATIPADA}”। {AVASESA}"
            elif t.endswith('"dukkhanirodhagāminī paṭipadā". Avasesā dhammā dukkhanirodhagāminiyā paṭipadāya sampayuttā.'):
                line += f" {PATIPADA_IS} {AVASESA}"
            elif t.endswith('"dukkhanirodhagāminī paṭipadā".'):
                line += f" {PATIPADA_IS}"
            else:
                raise ValueError(t)
            H.append(line)
        elif t.startswith("Tattha katamā sammādiṭṭhi?"):
            H.append(MAGGA_DEFS["sammādiṭṭhi"])
        elif t.startswith("Tattha katamo sammāsaṅkappo?"):
            H.append(MAGGA_DEFS["sammāsaṅkappo"])
        elif t.startswith("Tattha katamā sammāvācā?"):
            H.append(MAGGA_DEFS["sammāvācā"])
        elif t.startswith("Tattha katamo sammākammanto?"):
            H.append(MAGGA_DEFS["sammākammanto"])
        elif t.startswith("Tattha katamo sammāājīvo?"):
            H.append(MAGGA_DEFS["sammāājīvo"])
        elif t.startswith("Tattha katamo sammāvāyāmo?"):
            H.append(MAGGA_DEFS["sammāvāyāmo_var" if "[" in t else "sammāvāyāmo"])
        elif t.startswith("Tattha katamā sammāsati?"):
            H.append(MAGGA_DEFS["sammāsati"])
        elif t.startswith("Tattha katamo sammāsamādhi?"):
            line = MAGGA_DEFS["sammāsamādhi_2" if "ṭhiti saṇṭhiti" in t else "sammāsamādhi_1"]
            assert t.endswith('Ayaṃ vuccati "dukkhanirodhagāminī paṭipadā". Avasesā dhammā dukkhanirodhagāminiyā paṭipadāya sampayuttā.'), t
            H.append(f"{line} {PATIPADA_IS} {AVASESA}")
        elif t == "Abhidhammabhājanīyaṃ.":
            H.append(S.SECTION_TITLES["Abhidhammabhājanīyaṃ"] + "।")
        else:
            raise ValueError("unhandled: " + t[:80])
    return H


# ---------------------------------------------------------------- Pañhāpucchaka
QUESTION = (f"चार {AS}ों में से कितने हितकर हैं, कितने हानिकर हैं, कितने नैतिक रूप से अनिर्धारित हैं… "
            f"कितने संघर्ष वाले हैं, कितने संघर्ष से रहित हैं?")
TIKA_HEADING, DUKA_HEADING = "तीन-तीन के वर्गीकरण", "दो-दो के वर्गीकरण"


def build():
    P = pali_lines(NAME)
    H = ["### " + S.CHAPTER_TITLES[4], "#### " + S.SECTION_TITLES["Suttantabhājanīyaṃ"], FOUR_ARIYA_VAR]
    H += dukkha_lines() + samudaya_lines() + nirodha_lines() + magga_lines()
    assert strip_id(P[len(H)]) == "#### Abhidhammabhājanīyaṃ", P[len(H)]
    H.append("#### " + S.SECTION_TITLES["Abhidhammabhājanīyaṃ"])
    end = next(i for i, p in enumerate(P) if p.startswith("Abhidhammabhājanīyaṃ."))
    H += abhidhamma_lines(P[len(H):end + 1])
    H += ["#### " + S.SECTION_TITLES["Pañhāpucchakaṃ"], FOUR_ARIYA, QUESTION, "##### " + TIKA_HEADING]
    pan = [strip_id(l) for l in P[len(H):]]
    i = 0
    while not pan[i].startswith("##### Dukaṃ"):
        H.append(M.paragraph(pan[i], SJ.SUBJ_SACCA, SJ.OVR_SACCA))
        i += 1
    H.append("##### " + DUKA_HEADING)
    i += 1
    while pan[i] != "Pañhāpucchakaṃ.":
        H.append(M.paragraph(pan[i], SJ.SUBJ_SACCA, SJ.OVR_SACCA))
        i += 1
    H += [S.SECTION_TITLES["Pañhāpucchakaṃ"] + "।", S.CHAPTER_TITLES[4] + " पूरा हुआ।"]
    return H


def main():
    check_in_pi([KAYIKA_DUKKHA, CETASIKA_DUKKHA, JARA, PADH_V, F_KIRIYA, "हितकर और हानिकर कर्म के फल रूपी परिघटनाएँ",
                 JHANA1, JHANA2, JHANA3, JHANA4, LOKUTTARA.replace("यहाँ जिस समय भिक्षु", "जिस समय कोई"),
                 "परिघटनाओं की छानबीन नामक जागृति का अंग, मार्ग का अंग, मार्ग में समाया हुआ है",
                 "वाणी के चार दुराचरणों से दूर रहना, विरत रहना, पूरी तरह विरत रहना, बचना",
                 "न करना, न अपनाना, दोष में न पड़ना, मर्यादा का उल्लंघन न करना, पुल को तोड़ देना",
                 "दुःख का ज्ञान, दुःख की उत्पत्ति का ज्ञान, दुःख के अंत का ज्ञान", "शरीर में शरीर का अवलोकन करते हुए रहता है",
                 "उत्पन्न हो चुकी हितकर परिघटनाओं की स्थिरता के लिए, उनके लुप्त न होने के लिए, उन्हें और बढ़ाने के लिए, "
                 "उनकी विपुलता के लिए, उनके अभ्यास के लिए, उनकी परिपूर्णता के लिए"],
                dirs=(PI1_HI_DIR, PI5_HI_DIR))
    check_in_pi([TANHA_DEF.split(" [")[0], "बार-बार पुनर्जन्म दिलाने वाली है, आनंद और राग से युक्त है, जहाँ-तहाँ आनंद लेने वाली है",
                 GRIEF5, "दुःख का सत्य", "उत्पत्ति का सत्य", "दुःख के अंत का सत्य", "मार्ग का सत्य",
                 "दुःख के अंत की ओर ले जाने वाला मार्ग आर्य सत्य", "दुःख की उत्पत्ति आर्य सत्य", "दुःख का अंत आर्य सत्य"],
                dirs=(PI5_HI_DIR,))
    write_chapter(NAME, build())


if __name__ == "__main__":
    main()
