"""Builder for the Hindi rails translation of pi-2 chapter 4 (Saccavibhaṅga), plain audience.

Writes AI_translation/hindi/pi-2-hindi-plain-rails_split_chapters/4-saccavibhango.md
Imports the sample builder (read-only) for shared strings and emit(); Pañhāpucchaka sentences come
from build_rails_2_pp.py. Abhidhammabhājanīya lines are composed from item tables so that identical
Pāli items always give identical Hindi.
usage: python -I -X utf8 build_rails_4.py
"""
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-hi\rails")
import build_rails_sample as S  # noqa: E402
import build_rails_2_pp as PP  # noqa: E402

CH = "4-saccavibhango.md"
TITLE = "सत्यों का विश्लेषण"

DUK = "दुःख"
SAM = "दुःख की उत्पत्ति"
NIR = "दुःख का अंत"
PAT = "दुःख के अंत की ओर ले जाने वाला प्रगति का ढंग"
PAT_OBL = "दुःख के अंत की ओर ले जाने वाले प्रगति के ढंग"
AS = "आर्य सत्य"

# --------------------------------------------------------------------------- Suttantabhājanīya
FOUR_NOBLE = (f"चार {AS} – {DUK} {AS}, {SAM} [वर्तनी-भेद (Syā.): dukkhasamudayo] {AS}, "
              f"{NIR} [वर्तनी-भेद (Syā.): dukkhanirodho] {AS}, {PAT} {AS}।")
FOUR_NOBLE_PLAIN = f"चार {AS} – {DUK} {AS}, {SAM} {AS}, {NIR} {AS}, {PAT} {AS}।"
SPDDU = "शोक, विलाप, दुःख, उदासी और निराशा"  # sokaparidevadukkhadomanassupāyāsā
NOT_GET = "जो चाहता है, उसे प्राप्त न करना भी दुःख है"  # yaṃ (yam)picchaṃ na labhati tampi dukkhaṃ
UPK5 = "आसक्ति का विषय बनने वाले पाँच समूह"  # pañcupādānakkhandhā
UNPLEASANT = "अप्रिय से संयोग का दुःख"  # appiyehi sampayogo dukkho (as a name)
PLEASANT = "प्रिय से वियोग का दुःख"  # piyehi vippayogo dukkho (as a name)
DUKKHA_DEF = (f"यहाँ {DUK} {AS} क्या है? जन्म भी दुःख है, बुढ़ापा भी दुःख है, मृत्यु भी दुःख है, {SPDDU} भी दुःख हैं, "
              f"अप्रिय से संयोग दुःख है, प्रिय से वियोग दुःख है, {NOT_GET}, संक्षेप में {UPK5} दुःख रूपी हैं।")
BEINGS = "उन-उन प्राणियों का उस-उस प्राणी-वर्ग में जो"
JATI = (f"यहाँ जन्म क्या है? {BEINGS} जन्म, भली-भाँति जन्म, गर्भ में उतरना, पूरी तरह पैदा होना, समूहों का प्रकट होना, "
        f"इंद्रिय-क्षेत्रों की उपलब्धि है – यह “जन्म” कहा जाता है।")
JARA = (f"यहाँ बुढ़ापा क्या है? {BEINGS} बुढ़ापा, जीर्ण होना, दाँतों का टूटना, बालों का पकना, त्वचा पर झुर्रियाँ पड़ना, "
        f"आयु का घटना, इंद्रियों का पूरी तरह पक जाना है – यह “बुढ़ापा” कहा जाता है।")  # pi-1 rails ^1-643 list
MARANA = ("यहाँ मृत्यु क्या है? उन-उन प्राणियों का उस-उस प्राणी-वर्ग से जो गुज़र जाना, गुज़र जाने की अवस्था, टूटना, "
          "लुप्त हो जाना, मौत, मृत्यु, काल का पूरा होना, समूहों का टूटना, शरीर का त्याग, जीवन-क्षमता का कट जाना है – "
          "यह “मृत्यु” कही जाती है।")
AFFLICTED = ("रिश्तेदारों की हानि से पीड़ित, धन-संपत्ति की हानि से पीड़ित, रोग रूपी हानि से पीड़ित, सदाचार की हानि से पीड़ित "
             "या दृष्टि की हानि से पीड़ित, किसी न किसी हानि से घिरे, किसी न किसी दुःख रूपी परिघटना से पीड़ित व्यक्ति का जो")
SOKA = (f"यहाँ शोक क्या है? {AFFLICTED} शोक, शोक करना, शोकग्रस्त होना, भीतर का शोक, भीतर का गहरा शोक, मन का जलना, "
        f"उदासी, शोक का काँटा है – यह “शोक” कहा जाता है।")
PARIDEVA = (f"यहाँ विलाप क्या है? {AFFLICTED} रोना, विलाप, रोते रहना, विलाप करते रहना, रोने की अवस्था, विलाप की अवस्था, "
            f"शब्दों की झड़ी, प्रलाप, बड़बड़ाना, बिलखना, बिलखते रहना, बिलखने की अवस्था "
            f"[वर्तनी-भेद (Syā.): lālapo lālapanā lālapitattaṃ] है – यह “विलाप” कहा जाता है।")
DUKKHA = ("यहाँ दुःख क्या है? जो शारीरिक असुहावनापन, शारीरिक दुःख, शरीर के संपर्क से उत्पन्न असुहावना दुःखद अनुभव, "
          "शरीर के संपर्क से उत्पन्न असुहावनी दुःखद अनुभूति है – यह “दुःख” कहा जाता है।")  # pi-1 rails ^1-559
DOMANASSA = ("यहाँ उदासी क्या है? जो मानसिक असुहावनापन, मानसिक दुःख, मन के संपर्क से उत्पन्न असुहावना दुःखद अनुभव, "
             "मन के संपर्क से उत्पन्न असुहावनी दुःखद अनुभूति है – यह “उदासी” कही जाती है।")  # pi-1 rails ^1-416
UPAYASA = (f"यहाँ निराशा क्या है? {AFFLICTED} हताशा, निराशा, हताश होने की अवस्था, निराश होने की अवस्था है – "
           f"यह “निराशा” कही जाती है।")
APPIYA = (f"यहाँ {UNPLEASANT} क्या है? यहाँ जिसके लिए अनचाहे, अप्रिय, मन को न भाने वाले {S.SENSE_OBJECTS} होते हैं, "
          f"या जो लोग उसका अनर्थ चाहने वाले, अहित चाहने वाले, असुविधा चाहने वाले, कुशल-क्षेम न चाहने वाले होते हैं; "
          f"उनके साथ जो मेल, एक साथ आना, जुड़ाव, घुल-मिल जाना है – यह “{UNPLEASANT}” कहा जाता है।")
PIYA = (f"यहाँ {PLEASANT} क्या है? यहाँ जिसके लिए मनचाहे, प्रिय, मनभावन {S.SENSE_OBJECTS} होते हैं, "
        f"या जो लोग उसका अर्थ चाहने वाले, हित चाहने वाले, सुविधा चाहने वाले, कुशल-क्षेम चाहने वाले माता, पिता, भाई, बहन, "
        f"मित्र, साथी, रिश्तेदार या रक्त-संबंधी होते हैं; उनके साथ जो मेल न होना, एक साथ न आना, साथ न रहना, "
        f"घुल-मिल न पाना है – यह “{PLEASANT}” कहा जाता है।")
NOT_GET_Q = f"यहाँ “{NOT_GET}” क्या है?"
WISH_END = f"पर यह इच्छा करने से नहीं मिल सकता। यह भी “{NOT_GET}”।"
WISH1 = (f"{NOT_GET_Q} जन्म के स्वभाव वाले प्राणियों में ऐसी इच्छा उत्पन्न होती है – “अहो, सचमुच ऐसा हो कि हम जन्म के "
         f"स्वभाव वाले न हों; और सचमुच, हम पर जन्म न आए”! {WISH_END}")
WISH2 = (f"बुढ़ापे के स्वभाव वाले प्राणियों में… रोग के स्वभाव वाले प्राणियों में… मृत्यु के स्वभाव वाले प्राणियों में… "
         f"{SPDDU} के स्वभाव वाले प्राणियों में ऐसी इच्छा उत्पन्न होती है – “अहो, सचमुच ऐसा हो कि हम {SPDDU} के स्वभाव वाले न हों; "
         f"और सचमुच, हम पर {SPDDU} न आएँ”! {WISH_END}")
UPK_LIST = ", ".join(f"आसक्ति का विषय बनने वाला {S.KH[k]}" for k in S.ORDER)
UPK = (f"यहाँ संक्षेप में दुःख रूपी, {UPK5} कौन-से हैं? यानी – {UPK_LIST}। "
       f"ये “संक्षेप में दुःख रूपी, {UPK5}” कहे जाते हैं।")


def called(x, f=False):
    return f"यह “{x}” {'कही जाती है' if f else 'कहा जाता है'}।"


# --- origin / cessation: "dear and pleasing in the world"
SIX = {  # key: list of (Hindi, gender m/f, number s/p)
    "organ": [("आँख", "f", "s"), ("कान", "m", "s"), ("नाक", "f", "s"), ("जीभ", "f", "s"), ("शरीर", "m", "s"), ("मन", "m", "s")],
    "object": [("दृश्य रूप", "m", "p"), ("ध्वनियाँ", "f", "p"), ("गंधें", "f", "p"), ("स्वाद", "m", "p"), ("स्पर्श", "m", "p"),
               ("मन के विषय", "m", "p")],
}
SENSE6 = ["आँख", "कान", "नाक", "जीभ", "शरीर", "मन"]
OBJ6 = ["दृश्य रूप", "ध्वनि", "गंध", "स्वाद", "स्पर्श", "मन के विषयों"]
SIX["vinnana"] = [(f"{s} की चेतना", "f", "s") for s in SENSE6]
SIX["phassa"] = [(f"{s} का संपर्क", "m", "s") for s in SENSE6]
SIX["vedana"] = [(f"{s} के संपर्क से उत्पन्न अनुभूति", "f", "s") for s in SENSE6]
SIX["sanna"] = [(f"{o} की पहचान", "f", "s") for o in OBJ6]
SIX["sancetana"] = [(f"{o} के बारे में इरादा करना", "m", "s") for o in OBJ6]
SIX["tanha"] = [(f"{o} की तृष्णा", "f", "s") for o in OBJ6]
SIX["vitakka"] = [(f"{o} के बारे में विचार", "m", "s") for o in OBJ6]
SIX["vicara"] = [(f"{o} के बारे में सतत विचार", "m", "s") for o in OBJ6]


def piya(g, n):
    if g == "f":
        return "प्रिय लगने वाली, सुहावनी लगने वाली " + ("हैं" if n == "p" else "है")
    if n == "p":
        return "प्रिय लगने वाले, सुहावने लगने वाले हैं"
    return "प्रिय लगने वाला, सुहावना लगने वाला है"


ETTHA_U = "इसी में यह तृष्णा उत्पन्न होते समय उत्पन्न होती है, इसी में टिकते समय टिकती है।"
ETTHA_N = "इसी में यह तृष्णा छूटते समय छूटती है, इसी में समाप्त होते समय समाप्त होती है।"
LOKE = "लोक में"


def full(item, ettha):
    h, g, n = item
    return f"{LOKE} {h} {piya(g, n)}। {ettha}"


def abbrev(items, ettha, first_full=True):
    """Cakkhuṃ loke … ettha …. Sotaṃ loke…pe… ghānaṃ loke… … mano loke piyarūpaṃ sātarūpaṃ. Ettha …"""
    h, g, n = items[-1]
    mid = "… ".join(f"{LOKE} {x[0]}" for x in items[1 if first_full else 0:-1])
    tail = f"{mid}… {LOKE} {h} {piya(g, n)}। {ettha}"
    return f"{full(items[0], ettha)} {tail}" if first_full else tail


DEAR_Q = f"{LOKE} प्रिय लगने वाला, सुहावना लगने वाला क्या है?"
ORDER6 = ["organ", "object", "vinnana", "phassa", "vedana", "sanna", "sancetana", "tanha", "vitakka"]
SAMUDAYA_LINES = [
    (f"यहाँ {SAM} {AS} क्या है? यह जो तृष्णा बार-बार पुनर्जन्म दिलाने वाली [वर्तनी-भेद (Syā., Ka.): ponobbhavikā] है, "
     f"आनंद और राग के साथ होने वाली है, जहाँ-तहाँ आनंद लेने वाली है, यानी – इंद्रिय-सुखों की तृष्णा, अस्तित्व की तृष्णा, "
     f"अनस्तित्व की तृष्णा।"),
    ("यह तृष्णा कहाँ उत्पन्न होते समय उत्पन्न होती है, कहाँ टिकते समय टिकती है? लोक में जो प्रिय लगने वाला, सुहावना लगने वाला है, "
     "उसी में यह तृष्णा उत्पन्न होते समय उत्पन्न होती है, उसी में टिकते समय टिकती है।"),
    f"{DEAR_Q} {abbrev(SIX['organ'], ETTHA_U)}",
] + [abbrev(SIX[k], ETTHA_U) for k in ORDER6[1:]] + [
    " ".join(full(x, ETTHA_U) for x in SIX["vicara"]),
    called(f"{SAM} {AS}"),
]
NIRODHA_LINES = [
    (f"यहाँ {NIR} {AS} क्या है? उसी तृष्णा का जो पूरी तरह फीका पड़ना और अंत, त्याग, छोड़ देना, मुक्ति, "
     f"लगाव का न रहना है।"),
    ("यह तृष्णा कहाँ छूटते समय छूटती है, कहाँ समाप्त होते समय समाप्त होती है? लोक में जो प्रिय लगने वाला, सुहावना लगने वाला है, "
     "उसी में यह तृष्णा छूटते समय छूटती है, उसी में समाप्त होते समय समाप्त होती है।"),
    f"{DEAR_Q} {abbrev(SIX['organ'], ETTHA_N)}",
] + [abbrev(SIX[k], ETTHA_N) for k in ORDER6[1:5]] + [
    abbrev(SIX[k], ETTHA_N, first_full=False) for k in ORDER6[5:] + ["vicara"]] + [called(f"{NIR} {AS}")]

EIGHT = "सही दृष्टि, सही संकल्प, सही वाणी, सही कर्म, सही आजीविका, सही प्रयास, सही सजगता, सही एकाग्रता"
FIVE_F = "सही दृष्टि, सही संकल्प, सही प्रयास, सही सजगता, सही एकाग्रता"
EFFORT_VERBS = "चाह जगाता है, प्रयास करता है, उत्साह जगाता है, मन को तत्पर करता है, पूरा ज़ोर लगाता है"  # pi-1 rails ^1-1377
SATI_TAIL = "का अवलोकन करते हुए रहता है, उद्यमी, स्पष्ट समझ रखते हुए, सजग, लोक में लालच और उदासी को दूर करके"
MAGGA_LINES = [
    f"यहाँ {PAT} {AS} क्या है? यही आर्य आठ अंगों वाला मार्ग, यानी – {EIGHT}।",
    (f"यहाँ सही दृष्टि क्या है? दुःख के बारे में ज्ञान, दुःख की उत्पत्ति के बारे में ज्ञान, दुःख के अंत के बारे में ज्ञान, "
     f"{PAT_OBL} के बारे में ज्ञान – {called('सही दृष्टि', True)}"),
    f"यहाँ सही संकल्प क्या है? त्याग का संकल्प, दुर्भावना के अभाव का संकल्प, अहिंसा का संकल्प – {called('सही संकल्प')}",
    (f"यहाँ सही वाणी क्या है? झूठ बोलने से बचना, चुगली की वाणी से बचना, कठोर वाणी से बचना, व्यर्थ की बकवास से बचना – "
     f"{called('सही वाणी', True)}"),
    (f"यहाँ सही कर्म क्या है? जीव-हत्या से बचना, न दिए हुए को लेने से बचना, इंद्रिय-सुखों में दुराचार से बचना – "
     f"{called('सही कर्म')}"),
    (f"यहाँ सही आजीविका क्या है? यहाँ आर्य शिष्य ग़लत आजीविका को छोड़कर सही आजीविका से जीविका चलाता है – "
     f"{called('सही आजीविका', True)}"),
    (f"यहाँ सही प्रयास क्या है? यहाँ भिक्षु उत्पन्न न हुई बुरी हानिकर परिघटनाओं को उत्पन्न न होने देने के लिए {EFFORT_VERBS}। "
     f"उत्पन्न हो चुकी बुरी हानिकर परिघटनाओं को छोड़ने के लिए {EFFORT_VERBS}। "
     f"उत्पन्न न हुई हितकर परिघटनाओं की उत्पत्ति के लिए {EFFORT_VERBS}। "
     f"उत्पन्न हो चुकी हितकर परिघटनाओं की स्थिरता के लिए, उनके लुप्त न होने के लिए, उन्हें और बढ़ाने के लिए, "
     f"उनकी विपुलता के लिए, उनके अभ्यास के लिए, उनकी परिपूर्णता के लिए {EFFORT_VERBS}। {called('सही प्रयास')}"),
    (f"यहाँ सही सजगता क्या है? यहाँ भिक्षु शरीर में शरीर {SATI_TAIL}। अनुभूतियों में… मन में… "
     f"मन के विषयों में परिघटनाओं {SATI_TAIL}। {called('सही सजगता', True)}"),
    ("यहाँ सही एकाग्रता क्या है? यहाँ भिक्षु इंद्रिय-सुखों से अलग होकर, हानिकर परिघटनाओं से अलग होकर, "
     "आरंभिक विचार और सतत विचार वाले, अलगाव से उत्पन्न उल्लास और सुख वाले पहले ध्यान को प्राप्त करके उसमें रहता है। "
     "आरंभिक विचार और सतत विचार के शांत होने से, स्वयं में निर्मलता वाले, मन के एक बिंदु पर टिकने वाले, "
     "आरंभिक विचार और सतत विचार से रहित, एकाग्रता से उत्पन्न उल्लास और सुख वाले दूसरे ध्यान को प्राप्त करके उसमें रहता है। "
     "उल्लास के फीका पड़ने से वह समभाव के साथ, सजग और स्पष्ट समझ रखते हुए रहता है और काया से सुख का अनुभव करता है, "
     "जिसके बारे में आर्य कहते हैं – “समभाव वाला, सजग, सुख से रहने वाला”, ऐसे तीसरे ध्यान को प्राप्त करके उसमें रहता है। "
     "सुख को छोड़ने से और दुःख को छोड़ने से, और पहले ही प्रसन्नता और उदासी के मिट जाने से, न दुःखद, न सुखद, "
     "समभाव और सजगता से पूरी तरह शुद्ध चौथे ध्यान को प्राप्त करके उसमें रहता है। "
     + called("सही एकाग्रता", True)),
    called(f"{PAT} {AS}"),
    f"{S.SUTTANTA_BH}।",
]

# --------------------------------------------------------------------------- Abhidhammabhājanīya
FOUR_PLAIN = f"चार सत्य – {DUK}, {SAM}, {NIR}, {PAT}।"
I_KIL, I_AKU = "शेष मन के क्लेश", "शेष हानिकर परिघटनाएँ"
I_ROOT = "मन के मैलों का विषय बनने वाले तीन हितकर मूल"
I_SKU = "मन के मैलों का विषय बनने वाली शेष हितकर परिघटनाएँ"
I_VIP = "मन के मैलों का विषय बनने वाली, हितकर और हानिकर कर्म के फल रूपी परिघटनाएँ"
I_KIR = "केवल क्रिया रूपी वे परिघटनाएँ जो न हितकर हैं, न हानिकर, न कर्म-फल"
ITEMS = {
    "taṇhā": "तृष्णा", "avasesā ca kilesā": I_KIL, "avasesā ca akusalā dhammā": I_AKU,
    "tīṇi ca kusalamūlāni sāsavāni": I_ROOT, "avasesā ca sāsavā kusalā dhammā": I_SKU,
    "sāsavā ca kusalākusalānaṃ dhammānaṃ vipākā": I_VIP, "sāsavā kusalākusalānaṃ dhammānaṃ vipākā": I_VIP,
    "ye ca dhammā kiriyā neva kusalā nākusalā na ca kammavipākā": I_KIR, "sabbañca rūpaṃ": "सारा भौतिक रूप",
}
OBL = {"taṇhāya": "तृष्णा", "avasesānañca kilesānaṃ": "शेष मन के क्लेशों",
       "avasesānañca akusalānaṃ dhammānaṃ": "शेष हानिकर परिघटनाओं",
       "tiṇṇañca kusalamūlānaṃ sāsavānaṃ": "मन के मैलों का विषय बनने वाले तीन हितकर मूलों",
       "avasesānañca sāsavānaṃ kusalānaṃ dhammānaṃ": "मन के मैलों का विषय बनने वाली शेष हितकर परिघटनाओं"}


def items_of(s):
    s = s.replace("Taṇhā ca avasesā", "Taṇhā ca, avasesā")
    out = []
    for x in s.split(", "):
        x = x[0].lower() + x[1:]
        x = re.sub(r"^taṇhā ca$", "taṇhā", x)
        out.append(x)
    return out


def join_and(xs):
    return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " और " + xs[-1]


PATH_HEAD = ("यहाँ भिक्षु जिस समय लोकोत्तर ध्यान का अभ्यास करता है, जो मुक्ति की ओर ले जाने वाला और संचय घटाने की ओर "
             "ले जाने वाला होता है, दृष्टियों में फँसने को छोड़ने के लिए और पहले चरण की प्राप्ति के लिए, "
             "इंद्रिय-सुखों से अलग होकर… पहले ध्यान को प्राप्त करके उसमें रहता है, जो दुःखद प्रगति और धीमे उच्च ज्ञान "
             "वाला होता है, उस समय")  # pi-1 rails ^1-277 frame
REST = f"शेष परिघटनाएँ {PAT_OBL} से जुड़ी हैं।"
MAG = "मार्ग का अंग, मार्ग में समाया हुआ है"
FACTOR = {  # pi-1 rails ^1-283 … ^1-301, ^1-289, ^1-290
    "Tattha katamā sammādiṭṭhi? Yā paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi dhammavicayasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ – ayaṃ vuccati \"sammādiṭṭhi\".":
        f"यहाँ सही दृष्टि क्या है? जो प्रज्ञा, जानना… मोह का अभाव, परिघटनाओं की छानबीन, सही दृष्टि, परिघटनाओं की छानबीन नामक जागृति का अंग, {MAG} – {called('सही दृष्टि', True)}",
    "Tattha katamo sammāsaṅkappo? Yo takko vitakko…pe… sammāsaṅkappo maggaṅgaṃ maggapariyāpannaṃ – ayaṃ vuccati \"sammāsaṅkappo\".":
        f"यहाँ सही संकल्प क्या है? जो सोचना, आरंभिक विचार… सही संकल्प, {MAG} – {called('सही संकल्प')}",
    "Tattha katamā sammāvācā? Yā catūhi vacīduccaritehi ārati virati paṭivirati veramaṇī [veramaṇi (ka.) evamuparipi] akiriyā akaraṇaṃ anajjhāpatti velāanatikkamo setughāto sammāvācā maggaṅgaṃ maggapariyāpannaṃ – ayaṃ vuccati \"sammāvācā\".":
        f"यहाँ सही वाणी क्या है? जो वाणी के चार दुराचरणों से दूर रहना, विरत रहना, पूरी तरह विरत रहना, बचना [वर्तनी-भेद (Ka.): veramaṇi; आगे भी इसी तरह], न करना, न अपनाना, दोष में न पड़ना, मर्यादा का उल्लंघन न करना, पुल को तोड़ देना, सही वाणी, {MAG} – {called('सही वाणी', True)}",
    "Tattha katamo sammākammanto? Yā tīhi kāyaduccaritehi ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti velāanatikkamo setughāto sammākammanto maggaṅgaṃ maggapariyāpannaṃ – ayaṃ vuccati \"sammākammanto\".":
        f"यहाँ सही कर्म क्या है? जो शरीर के तीन दुराचरणों से दूर रहना, विरत रहना, पूरी तरह विरत रहना, बचना, न करना, न अपनाना, दोष में न पड़ना, मर्यादा का उल्लंघन न करना, पुल को तोड़ देना, सही कर्म, {MAG} – {called('सही कर्म')}",
    "Tattha katamo sammāājīvo? Yā micchā ājīvā ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti velāanatikkamo setughāto sammāājīvo maggaṅgaṃ maggapariyāpannaṃ – ayaṃ vuccati \"sammāājīvo\".":
        f"यहाँ सही आजीविका क्या है? जो ग़लत आजीविका से दूर रहना, विरत रहना, पूरी तरह विरत रहना, बचना, न करना, न अपनाना, दोष में न पड़ना, मर्यादा का उल्लंघन न करना, पुल को तोड़ देना, सही आजीविका, {MAG} – {called('सही आजीविका', True)}",
    "Tattha katamo sammāvāyāmo? Yo cetasiko vīriyārambho [viriyārambho (sī. syā.)] …pe… sammāvāyāmo vīriyasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ – ayaṃ vuccati \"sammāvāyāmo\".":
        f"यहाँ सही प्रयास क्या है? जो मानसिक रूप से उत्साह जगाना [वर्तनी-भेद (Sī., Syā.): viriyārambho]… सही प्रयास, उत्साह नामक जागृति का अंग, {MAG} – {called('सही प्रयास')}",
    "Tattha katamo sammāvāyāmo? Yo cetasiko vīriyārambho…pe… sammāvāyāmo vīriyasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ – ayaṃ vuccati \"sammāvāyāmo\".":
        f"यहाँ सही प्रयास क्या है? जो मानसिक रूप से उत्साह जगाना… सही प्रयास, उत्साह नामक जागृति का अंग, {MAG} – {called('सही प्रयास')}",
    "Tattha katamā sammāsati? Yā sati anussati…pe… sammāsati satisambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ – ayaṃ vuccati \"sammāsati\".":
        f"यहाँ सही सजगता क्या है? जो सजगता, बार-बार स्मरण… सही सजगता, सजगता नामक जागृति का अंग, {MAG} – {called('सही सजगता', True)}",
}
SAMADHI_HEAD = {"Yā cittassa ṭhiti saṇṭhiti…pe…": "जो मन की स्थिरता, ठहराव…", "Yā cittassa ṭhiti…pe…": "जो मन की स्थिरता…"}


def abhi_line(p):
    if p == "Cattāri saccāni – dukkhaṃ, dukkhasamudayo, dukkhanirodho, dukkhanirodhagāminī paṭipadā.":
        return FOUR_PLAIN
    if p in FACTOR:
        return FACTOR[p]
    m = re.match(r'^Tattha katamo dukkhasamudayo\? (.*) – ayaṃ vuccati "dukkhasamudayo"\.$', p)
    if m:
        return f"यहाँ {SAM} क्या है? {join_and([ITEMS[x] for x in items_of(m.group(1))])} – {called(SAM, True)}"
    m = re.match(r'^Tattha katamaṃ dukkhaṃ\? (.*) – idaṃ vuccati "dukkhaṃ"\.$', p)
    if m:
        xs = [ITEMS[x] for x in items_of(m.group(1))]
        assert xs[-1] == "सारा भौतिक रूप"
        return f"यहाँ {DUK} क्या है? " + ", ".join(xs[:-1]) + f", और सारा भौतिक रूप – {called(DUK)}"
    m = re.match(r'^Tattha katamo dukkhanirodho\? (.*) pahānaṃ – ayaṃ vuccati "dukkhanirodho"\.$', p)
    if m:
        xs = [OBL[x[0].lower() + x[1:]] for x in re.sub(r"Taṇhāya ca", "Taṇhāya", m.group(1)).split(", ")]
        return f"यहाँ {NIR} क्या है? {join_and(xs)} को छोड़ देना – {called(NIR)}"
    m = re.match(r"^Tattha katamā dukkhanirodhagāminī paṭipadā\? Idha bhikkhu yasmiṃ samaye lokuttaraṃ jhānaṃ bhāveti "
                 r"niyyānikaṃ apacayagāmiṃ diṭṭhigatānaṃ pahānāya paṭhamāya bhūmiyā pattiyā,? vivicceva kāmehi…pe… "
                 r"paṭhamaṃ jhānaṃ upasampajja viharati dukkhapaṭipadaṃ dandhābhiññaṃ, tasmiṃ samaye (.*)$", p)
    if m:
        rest = m.group(1)
        ends = [("aṭṭhaṅgiko maggo hoti sammādiṭṭhi…pe… sammāsamādhi.", "आठ अंगों वाला मार्ग होता है, सही दृष्टि… सही एकाग्रता।"),
                ("aṭṭhaṅgiko maggo hoti – sammādiṭṭhi…pe… sammāsamādhi.", "आठ अंगों वाला मार्ग होता है – सही दृष्टि… सही एकाग्रता।"),
                ("pañcaṅgiko maggo hoti – sammādiṭṭhi, sammāsaṅkappo, sammāvāyāmo, sammāsati, sammāsamādhi.",
                 f"पाँच अंगों वाला मार्ग होता है – {FIVE_F}।"),
                ("phasso hoti…pe… avikkhepo hoti.", "संपर्क होता है… भटकाव का अभाव होता है।")]
        for a, b in ends:
            if rest.startswith(a):
                out = f"यहाँ {PAT} क्या है? {PATH_HEAD} {b}"
                tail = rest[len(a):].strip()
                tails = {"": "",
                         'Ayaṃ vuccati "dukkhanirodhagāminī paṭipadā". Avasesā dhammā dukkhanirodhagāminiyā paṭipadāya sampayuttā.':
                             f" {called(PAT)} {REST}",
                         'Ayaṃ vuccati – "dukkhanirodhagāminī paṭipadā". Avasesā dhammā dukkhanirodhagāminiyā paṭipadāya sampayuttā.':
                             f" यह कहा जाता है – “{PAT}”। {REST}",
                         'Ayaṃ vuccati "dukkhanirodhagāminī paṭipadā".': f" {called(PAT)}"}
                return out + tails[tail]
        raise ValueError(rest[:80])
    m = re.match(r'^Tattha katamo sammāsamādhi\? (Yā cittassa ṭhiti(?: saṇṭhiti)?…pe…) sammāsamādhi samādhisambojjhaṅgo '
                 r'maggaṅgaṃ maggapariyāpannaṃ – ayaṃ vuccati "sammāsamādhi"\. Ayaṃ vuccati "dukkhanirodhagāminī paṭipadā"\. '
                 r'Avasesā dhammā dukkhanirodhagāminiyā paṭipadāya sampayuttā\.$', p)
    if m:
        head = SAMADHI_HEAD[m.group(1).replace("ṭhiti …", "ṭhiti…")]
        return (f"यहाँ सही एकाग्रता क्या है? {head} सही एकाग्रता, एकाग्रता नामक जागृति का अंग, {MAG} – "
                f"{called('सही एकाग्रता', True)} {called(PAT)} {REST}")
    if p == "Abhidhammabhājanīyaṃ.":
        return f"{S.ABHI_BH}।"
    raise ValueError(f"no rule: {p[:100]}")


# --------------------------------------------------------------------------- Pañhāpucchaka
SUBJ = {
    "Samudayasaccaṃ": ("उत्पत्ति का सत्य", "उत्पत्ति के सत्य", "s"),
    "Maggasaccaṃ": ("मार्ग का सत्य", "मार्ग के सत्य", "s"),
    "Nirodhasaccaṃ": ("अंत का सत्य", "अंत के सत्य", "s"),
    "Dukkhasaccaṃ": ("दुःख का सत्य", "दुःख के सत्य", "s"),
    "Dve saccā": ("दो सत्य", "दो सत्यों", "p"),
    "dve saccā": ("दो सत्य", "दो सत्यों", "p"),
    "Tīṇi saccāni": ("तीन सत्य", "तीन सत्यों", "p"),
}
KENACI = "सत्य किसी एक प्रकार की चेतना से जाने जा सकने वाले भी हैं, किसी एक प्रकार की चेतना से न जाने जा सकने वाले भी"
SPECIAL = {
    PP.canon("kenaci viññeyyā, kenaci na viññeyyā"): KENACI,
    PP.canon("siyā mahaggatārammaṇaṃ na appamāṇārammaṇaṃ"): "कभी उन्नत विषय वाला होता है, अपरिमित विषय वाला नहीं",
    PP.canon("na maggārammaṇaṃ maggahetukaṃ"): "मार्ग को विषय बनाने वाला नहीं है, मार्ग को मूल बनाने वाला है",
    PP.canon("siyā maggārammaṇaṃ na maggahetukaṃ"): "कभी मार्ग को विषय बनाने वाला होता है, मार्ग को मूल बनाने वाला नहीं",
}
PRE = [("Dve saccā nīvaraṇiyā dve saccā", "Dve saccā nīvaraṇiyā. dve saccā"),  # source lacks the full stop
       ('" tipi', '"tipi'),
       # ajjhatta paired with bāhira is the ajjhattika/bāhira dyad (pi-1 ^1-M2-66)
       ("Dukkhasaccaṃ siyā ajjhattaṃ, siyā bāhiraṃ", "Dukkhasaccaṃ siyā ajjhattikaṃ, siyā bāhiraṃ")]
QUESTION = ("चार आर्य सत्यों में से कितने हितकर हैं, कितने हानिकर हैं, कितने नैतिक रूप से अनिर्धारित हैं… "
            "कितने संघर्ष वाले हैं, कितने संघर्ष से रहित हैं?")


def pp(p):
    return PP.line(p, SUBJ, SPECIAL, None, PRE)


def build(pali_lines):
    segs = S.segs_of_lines(pali_lines)
    src = {i: [S.ID.sub("", x).rstrip() for x in ls] for i, ls in segs}
    h = {}
    h["2-4-0"] = [f"### {TITLE}"]
    h["2-4-1-0"] = [f"#### {S.SUTTANTA_BH}"]
    h["2-189"] = [FOUR_NOBLE]
    h["2-4-1-1-0"] = ["##### दुःख का सत्य"]
    h["2-190"] = [DUKKHA_DEF]
    h["2-191"], h["2-192"], h["2-193"] = [JATI], [JARA], [MARANA]
    h["2-194"], h["2-195"], h["2-196"] = [SOKA], [PARIDEVA], [DUKKHA]
    h["2-197"], h["2-198"] = [DOMANASSA], [UPAYASA]
    h["2-199"], h["2-200"] = [APPIYA], [PIYA]
    h["2-201"] = [WISH1, WISH2]
    h["2-202"] = [UPK, called(f"{DUK} {AS}")]
    h["2-4-1-2-0"] = ["##### उत्पत्ति का सत्य"]
    h["2-203"] = SAMUDAYA_LINES
    h["2-4-1-3-0"] = ["##### अंत का सत्य"]
    h["2-204"] = NIRODHA_LINES
    h["2-4-1-4-0"] = ["##### मार्ग का सत्य"]
    h["2-205"] = MAGGA_LINES
    h["2-4-2-0"] = [f"#### {S.ABHI_BH}"]
    for i in ["2-206", "2-207", "2-208", "2-209", "2-210", "2-211", "2-212", "2-213", "2-214"]:
        h[i] = [abhi_line(x) for x in src[i]]
    h["2-4-3-0"] = [f"#### {S.PANHA}"]
    h["2-215"] = [FOUR_NOBLE_PLAIN]
    h["2-216"] = [QUESTION]
    h["2-4-3-1-0"] = ["##### तीन-तीन के वर्गीकरण"]
    h["2-217"] = [pp(x) for x in src["2-217"]]
    h["2-4-3-2-0"] = ["##### दो-दो के वर्गीकरण"]
    body = src["2-218"]
    assert body[-2:] == ["Pañhāpucchakaṃ.", "Saccavibhaṅgo niṭṭhito."], body[-2:]
    h["2-218"] = [pp(x) for x in body[:-2]] + [f"{S.PANHA}।", f"{TITLE} {S.DONE}।"]
    return h


def main():
    pali = (S.PALI / CH).read_text(encoding="utf-8").splitlines()
    S.emit(pali, build(pali), S.OUT / CH)


if __name__ == "__main__":
    main()
