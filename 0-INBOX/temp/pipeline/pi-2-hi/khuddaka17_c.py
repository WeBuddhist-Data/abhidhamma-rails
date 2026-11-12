# -*- coding: utf-8 -*-
"""Chapter 17, part C: exposition of the fours to the tens (catukka- ... dasakaniddesa)."""
from khuddaka17_f import *
from khuddaka17_a import CATUKKA15, PANCAKA15, CHAKKA14, SATTAKA7, ATTHAKA8, NAVAKA9, DASAKA7, NAMES_61_67
from khuddaka17_b import MICCHADITTHI_BODY, SAMANA, ORAM, UDDHAM, KS

LINES = []


def L(p, h):
    LINES.append((p, h))


def heads(n, items):
    return "##### (" + str(n) + ") " + items[n - 1].split(" [")[0]


def lst(name, g, items, close=None):
    """Tattha katame/katamā/katamāni <name>? a, b, c – ime <name>."""
    return f"{kaun(name, g)} {', '.join(items)} {D} {ime(close or name)}"


# ---------------------------------------------------------------- fours
AS4 = ["इंद्रिय-सुखों का मैल", "अस्तित्व का मैल", "दृष्टि का मैल", "अज्ञान का मैल"]
L("#### Catukkaniddeso", "#### चार-चार प्रकारों की व्याख्या")
L("##### (1) Cattāro āsavā", heads(1, CATUKKA15))
L("Tattha katame cattāro āsavā?", f"{kaun('मन के चार मैल', 'm')} {', '.join(AS4)}।")
L("##### (Ka) kāmāsavo", "##### (क) " + AS4[0])
L("Tattha katamo kāmāsavo?", f"{q(AS4[0])} {KAMA_FULL} {D} {called(AS4[0], 'm')}")
L("##### (Kha) bhavāsavo", "##### (ख) " + AS4[1])
L("Tattha katamo bhavāsavo?", f"{q(AS4[1])} {BHAVA_PE} {D} {called(AS4[1], 'm')}")
L("##### (Ga) diṭṭhāsavo", "##### (ग) " + AS4[2])
L("Tattha katamo diṭṭhāsavo?",
  f"{q(AS4[2])} {SASSATO_LOKO_ALL}। {DITTHI_PE} {D} {called(AS4[2], 'm')} सारी ग़लत दृष्टि भी दृष्टि का मैल है।")
L("##### (Gha) avijjāsavo", "##### (घ) " + AS4[3])
L("Tattha katamo avijjāsavo?",
  f"{q(AS4[3])} {MOHA_KNOW}। {YAM_EVARUPAM_ANNANAM} {D} {called(AS4[3], 'm')} {ime('मन के चार मैल')}")
UP4 = ["इंद्रिय-सुखों के प्रति आसक्ति", "दृष्टियों के प्रति आसक्ति", "सदाचार और व्रतों के प्रति आसक्ति",
       "आत्मा के सिद्धांत के प्रति आसक्ति"]
L("##### (2-5) Cattāro ganthādī", "##### (2-5) चार गाँठें आदि")
L("Tattha katame cattāro ganthā", f"यहाँ चार गाँठें… चार बाढ़ें… चार जकड़नें… चार आसक्तियाँ कौन-सी हैं? {', '.join(UP4)}।")
L("##### (Ka) kāmupādānaṃ", "##### (क) " + UP4[0])
L("Tattha katamaṃ kāmupādānaṃ?", f"{q(UP4[0])} {KAMA_PE} {D} {called(UP4[0], 'f')}")
L("##### (Kha) diṭṭhupādānaṃ", "##### (ख) " + UP4[1])
L("Tattha katamaṃ diṭṭhupādānaṃ?",
  f"{q(UP4[1])} “{NATTHI_DINNAM_PE}”। {DITTHI_PE} {D} {called(UP4[1], 'f')} {UP4[2]} और {UP4[3]} को छोड़कर सारी ग़लत दृष्टि "
  f"भी {UP4[1]} है।")
L("##### (Ga) sīlabbatupādānaṃ", "##### (ग) " + UP4[2])
L("Tattha katamaṃ sīlabbatupādānaṃ?", f"{q(UP4[2])} {SILABBATA_Q}। {DITTHI_PE} {D} {called(UP4[2], 'f')}")
L("##### (Gha) attavādupādānaṃ", "##### (घ) " + UP4[3])
L("Tattha katamaṃ attavādupādānaṃ?", f"{q(UP4[3])} {PUTHUJJANA} {D} {called(UP4[3], 'f')} {ime('चार आसक्तियाँ')}")
TU = "भिक्षु में उत्पन्न होने वाली तृष्णा उत्पन्न होती है"
L("##### (6) Cattāro taṇhuppādā", heads(6, CATUKKA15))
L("Tattha katame cattāro taṇhuppādā?",
  f"{kaun(CATUKKA15[5], 'm')} वस्त्र के कारण {TU}, भिक्षा के भोजन के कारण {TU}, निवास-स्थान के कारण {TU}, "
  f"इस या उस प्रकार के अस्तित्व के कारण {TU} {D} {ime(CATUKKA15[5])}")
AG = "ग़लत राह पर जाता है"
L("##### (7) Cattāri agatigamanāni", heads(7, CATUKKA15))
L("Tattha katamāni cattāri agatigamanāni?",
  f"{kaun(CATUKKA15[6], 'm')} चाह के कारण {AG}, द्वेष के कारण {AG}, मोह के कारण {AG}, भय के कारण {AG}। इस प्रकार की जो "
  f"ग़लत राह, ग़लत राह पर जाना, चाह के अनुसार जाना, गुटबाज़ी, पानी की तरह ढलान पर बहना है {D} {ime(CATUKKA15[6])}")
VP = "मानने वाला पहचान का उलटापन, मन का उलटापन, दृष्टि का उलटापन"
VIP = "उलटेपन के चार रूप"
L("##### (8) Cattāro vipariyāsā", heads(8, CATUKKA15))
L("Tattha katame cattāro vipariyāsā?",
  f"{kaun(VIP, 'm')} अनित्य में “नित्य” {VP}, दुःख में “सुख” {VP}, अनात्म में “आत्मा” {VP}, अशुभ में “शुभ” {VP} {D} {ime(VIP)}")
AV = [("न देखे को", "देखा हुआ"), ("न सुने को", "सुना हुआ"), ("अनुभव न किए को", "अनुभव किया हुआ"), ("न जाने को", "जाना हुआ")]
AV_A = [f"{a} {b} कहना" for a, b in AV]
AV_B = ["देखे को न देखा हुआ कहना", "सुने को न सुना हुआ कहना", "अनुभव किए को अनुभव न किया हुआ कहना",
        "जाने को न जाना हुआ कहना"]
L("##### (9) Cattāro anariyavohārā", heads(9, CATUKKA15))
L("Tattha katame cattāro anariyavohārā?", lst("चार अनार्य कथन", "m", AV_A))
L("##### (10) Aparepi cattāro anariyavohārā", heads(10, CATUKKA15))
L("Tattha katame aparepi cattāro anariyavohārā?", lst("और भी चार अनार्य कथन", "m", AV_B, "चार अनार्य कथन"))
L("##### (11) Cattāri duccaritāni", heads(11, CATUKKA15))
L("Tattha katamāni cattāri duccaritāni?", lst("चार दुराचरण", "m", DUCCARITA_10[:4]))
L("##### (12) Aparānipi cattāri duccaritāni", heads(12, CATUKKA15))
L("Tattha katamāni aparānipi cattāri duccaritāni?", lst("और भी चार दुराचरण", "m", DUCCARITA_10[3:7], "चार दुराचरण"))
L("##### (13) Cattāri bhayāni", heads(13, CATUKKA15))
L("Tattha katamāni cattāri bhayāni?", lst("चार भय", "m", ["जन्म का भय", "बुढ़ापे का भय", "रोग का भय", "मृत्यु का भय"]))
L("##### (14) Aparānipi cattāri bhayāni", heads(14, CATUKKA15))
L("Tattha katamāni aparānipi cattāri bhayāni? Rāja",
  lst("और भी चार भय", "m", ["राजा का भय", "चोर का भय", "आग का भय", "पानी का भय"], "चार भय"))
L("Tattha katamāni aparānipi cattāri bhayāni? Ūmi",
  lst("और भी चार भय", "m", ["लहरों का भय",
                              "मगरमच्छ का भय [वर्तनी-भेद: kumbhīrabhayaṃ, kumbhīḷabhayaṃ (?) (kumbha + īra + a = bhaya)]",
                              "भँवर का भय", "सूँस का भय"], "चार भय"))
L("Tattha katamāni aparānipi cattāri bhayāni? Attā",
  lst("और भी चार भय", "m", ["आत्म-निंदा का भय", "दूसरों द्वारा निंदा का भय", "दंड का भय", "दुर्गति का भय"], "चार भय"))
SACCATO = "इसे सत्य और पक्का मानते हुए दृष्टि उत्पन्न होती है"
SD = ["सुख और दुःख स्वयं के किए हुए हैं", "सुख और दुःख दूसरे के किए हुए हैं",
      "सुख और दुःख स्वयं के किए हुए भी हैं और दूसरे के किए हुए भी",
      "सुख और दुःख न स्वयं के किए हुए हैं, न दूसरे के किए हुए, वे संयोग से उत्पन्न हुए हैं"]
L("##### (15) Catasso diṭṭhiyo", heads(15, CATUKKA15))
L("Tattha katamā catasso diṭṭhiyo?",
  f"{kaun('चार दृष्टियाँ', 'f')} " + ", ".join(f"“{s}”, {SACCATO}" for s in SD) + f" {D} {ime('चार दृष्टियाँ')}")
L("Catukkaṃ.", "चार-चार प्रकार।")

# ---------------------------------------------------------------- fives
L("#### Pañcakaniddeso", "#### पाँच-पाँच प्रकारों की व्याख्या")
L("##### (1) Pañcorambhāgiyāni", heads(1, PANCAKA15))
L("Tattha katamāni pañcorambhāgiyāni",
  lst(ORAM, "m", ["स्थायी आत्मा की ग़लत दृष्टि", "संशय", "सदाचार और व्रतों के बारे में ग़लत धारणा", "इंद्रिय-सुखों की चाह",
                  "दुर्भावना"]))
L("##### (2) Pañcuddhambhāgiyāni", heads(2, PANCAKA15))
L("Tattha katamāni pañcuddhambhāgiyāni",
  lst(UDDHAM, "m", ["सूक्ष्म भौतिक लोक का राग", "अभौतिक लोक का राग", "अहंकार", "बेचैनी", "अज्ञान"]))
L("##### (3) Pañca macchariyāni", heads(3, PANCAKA15))
L("Tattha katamāni pañca macchariyāni?",
  "यहाँ पाँच प्रकार की कंजूसी कौन-सी है? निवास-स्थान की कंजूसी, परिवार की कंजूसी, लाभ की कंजूसी, प्रशंसा की कंजूसी, "
  f"शिक्षा की कंजूसी {D} यह पाँच प्रकार की कंजूसी है।")
FIVE = ["राग", "द्वेष", "मोह", "अहंकार", "दृष्टि"]
L("##### (4) Pañca saṅgā", heads(4, PANCAKA15))
L("Tattha katame pañca saṅgā?", lst("पाँच लगाव", "m", [f"{x} का लगाव" for x in FIVE]))
L("##### (5) Pañca sallā", heads(5, PANCAKA15))
L("Tattha katame pañca sallā?", lst("पाँच काँटे", "m", [f"{x} का काँटा" for x in FIVE]))
KH = "शंका करता है, संशय करता है, निश्चय नहीं कर पाता, आश्वस्त नहीं होता"
L("##### (6) Pañca cetokhilā", heads(6, PANCAKA15))
L("Tattha katame pañca cetokhilā?",
  f"{kaun('मन की पाँच कठोरताएँ', 'f')} " +
  ", ".join(f"{x} के बारे में {KH}" for x in ["गुरु", "शिक्षा", "संघ", "प्रशिक्षण"]) +
  f", साथी साधकों पर कुपित होता है, अप्रसन्न होता है, आहत मन वाला होता है, मन कठोर हो जाता है {D} "
  f"{ime('मन की पाँच कठोरताएँ')}")
AVITA = "के प्रति राग से मुक्त नहीं होता"
L("##### (7) Pañca cetaso vinibandhā", "##### (7) मन की पाँच बेड़ियाँ")
L("Tattha katame pañca cetaso vinibandhā?",
  f"{kaun('मन की पाँच बेड़ियाँ', 'f')} इंद्रिय-सुखों {AVITA}, चाह से मुक्त नहीं होता, प्रेम से मुक्त नहीं होता, प्यास से मुक्त नहीं होता, "
  f"ताप से मुक्त नहीं होता, तृष्णा से मुक्त नहीं होता; शरीर {AVITA}… भौतिक रूप {AVITA}… पेट भरकर जितना चाहे खाकर सोने के सुख, "
  f"करवटें बदलने के सुख, ऊँघने के सुख में लगा रहता है; किसी देव-लोक की कामना करके पवित्र जीवन जीता है {D} “इस सदाचार से, "
  f"या व्रत से, या तप से, या पवित्र जीवन से मैं देवता बनूँगा या देवताओं में से कोई” {D} {ime('मन की पाँच बेड़ियाँ')}")
L("##### (8) Pañca nīvaraṇāni", heads(8, PANCAKA15))
L("Tattha katamāni pañca nīvaraṇāni?",
  lst("पाँच बाधाएँ", "f", ["इंद्रिय-सुखों की चाह की बाधा", "दुर्भावना की बाधा", "आलस्य और तंद्रा की बाधा",
                           "बेचैनी और पछतावे की बाधा", "संशय की बाधा"]))
L("##### (9) Pañca kammāni ānantarikāni", heads(9, PANCAKA15))
L("Tattha katamāni pañca kammāni ānantarikāni?",
  lst(PANCAKA15[8], "m", ["माता की जान ली गई होती है", "पिता की जान ली गई होती है", "अर्हत् की जान ली गई होती है",
                          "दुष्ट मन से तथागत का रक्त बहाया गया होता है", "संघ में फूट डाली गई होती है"]))
DEATH = "मृत्यु के बाद आत्मा"
AROGO = "और विकार-रहित होती है"
UCCHEDA_DECL = "विद्यमान प्राणी के पूर्ण नाश, विनाश, मिट जाने की घोषणा करते हैं"
SOME = "कुछ लोग ऐसा कहते हैं"
L("##### (10) Pañca diṭṭhiyo", heads(10, PANCAKA15))
L("Tattha katamā pañca diṭṭhiyo?",
  f"{kaun('पाँच दृष्टियाँ', 'f')} " +
  ", ".join(f"“{DEATH} {a} {AROGO}”, {SOME}" for a in
            ["पहचान वाली", "पहचान से रहित", "न पहचान वाली, न पहचान से रहित"]) +
  f", या फिर {UCCHEDA_DECL}, या फिर कुछ लोग इसी जीवन में निर्वाण का दावा करते हैं {D} {ime('पाँच दृष्टियाँ')}")
L("##### (11) Pañca verā", heads(11, PANCAKA15))
L("Tattha katame pañca verā?",
  lst("पाँच वैर", "m", DUCCARITA_10[:4] + ["लापरवाही का कारण बनने वाली शराब और नशीली चीज़ें"]))
L("##### (12) Pañca byasanā", heads(12, PANCAKA15))
L("Tattha katame pañca byasanā?",
  lst("पाँच विपत्तियाँ", "f", [f"{x} की विपत्ति" for x in ["रिश्तेदारों", "धन", "रोग", "सदाचार", "दृष्टि"]]))
APAYA = "शरीर छूटने पर, मृत्यु के बाद दुःखद लोक में, दुर्गति में, पतन के लोक में, नरक में उत्पन्न होता है"   # [pi-4]
L("##### (13) Pañca akkhantiyā ādīnavā", heads(13, PANCAKA15))
L("Tattha katame pañca akkhantiyā ādīnavā?",
  f"{kaun(PANCAKA15[12], 'm')} बहुत लोगों को अप्रिय और मन को न भाने वाला होता है, बहुत वैर वाला होता है, और बहुत दोषों वाला, "
  f"मोह में पड़ा हुआ मरता है, {APAYA} {D} {ime(PANCAKA15[12])}")
L("##### (14) Pañca bhayāni", heads(14, PANCAKA15))
L("Tattha katamāni pañca bhayāni?",
  lst("पाँच भय", "m", ["जीविका का भय", "अपयश का भय", "सभा में झिझक का भय", "मृत्यु का भय", "दुर्गति का भय"]))
NIB = "इसी जीवन में निर्वाण के पाँच मत"
BHO = "मित्र"
ETTAVATA_N = f"तो {BHO}, इतने से यह आत्मा इसी जीवन में परम निर्वाण पा लेती है”। इस तरह कुछ लोग विद्यमान प्राणी के लिए इसी जीवन में परम निर्वाण की घोषणा करते हैं।"
TAMANNO = f"उससे कोई दूसरा ऐसा कहता है {D} “{BHO}, जिस आत्मा की तुम बात करते हो, वह है। मैं यह नहीं कहता कि वह नहीं है।"
NO_CA_N = f"परंतु {BHO}, इतने से यह आत्मा इसी जीवन में परम निर्वाण नहीं पा लेती। ऐसा किस कारण?"
YATO = f"{BHO}, जब यह आत्मा"
L("##### (15) Pañca diṭṭhadhammanibbānavādā", heads(15, PANCAKA15))
L("Tattha katame pañca diṭṭhadhammanibbānavādā?", f"{kaun(NIB, 'm')}")
L("(Ka) idhekacco samaṇo",
  f"(क) यहाँ कोई श्रमण या ब्राह्मण ऐसा कहने वाला, ऐसी दृष्टि वाला [वर्तनी-भेद (Syā.): evaṃdiṭṭhi] होता है {D} “{YATO} "
  f"इंद्रिय-सुखों के पाँच भोगों से युक्त होकर, उनसे घिरी हुई उनका आनंद लेती है, {ETTAVATA_N}")
L("(Kha) tamañño evamāha",
  f"(ख) {TAMANNO} {NO_CA_N} {BHO}, इंद्रिय-सुख अनित्य, दुःखद और बदलने के स्वभाव वाले हैं। उनके बदलने और कुछ और हो जाने से "
  f"शोक, विलाप, दुःख, उदासी और निराशा उत्पन्न होते हैं। {YATO} इंद्रिय-सुखों से अलग होकर… पहले ध्यान को प्राप्त करके उसमें "
  f"रहती है, {ETTAVATA_N}")
L("(Ga) tamañño evamāha",
  f"(ग) {TAMANNO} {NO_CA_N} वहाँ जो कुछ आरंभिक विचार और सतत विचार है, उसी के कारण यह स्थूल कहा जाता है। {YATO} आरंभिक "
  f"विचार और सतत विचार के शांत होने से… दूसरे ध्यान को प्राप्त करके उसमें रहती है, {ETTAVATA_N}")
L("(Gha) tamañño evamāha",
  f"(घ) {TAMANNO} {NO_CA_N} वहाँ जो उल्लास से भरा मन का उछाह है, उसी के कारण यह स्थूल कहा जाता है। {YATO} उल्लास के फीका "
  f"पड़ने से… तीसरे ध्यान को प्राप्त करके उसमें रहती है, {ETTAVATA_N}")
L("(Ṅa) tamañño evamāha",
  f"(ङ) {TAMANNO} {NO_CA_N} वहाँ जो सुख और उल्लास की ओर मन का झुकाव है, उसी के कारण यह स्थूल कहा जाता है। {YATO} सुख को "
  f"छोड़ने से… चौथे ध्यान को प्राप्त करके उसमें रहती है, {ETTAVATA_N} {ime(NIB)}")
L("Pañcakaṃ.", "पाँच-पाँच प्रकार।")

# ---------------------------------------------------------------- sixes
SG = [("दृश्य रूपों", "m"), ("ध्वनियों", "f"), ("गंधों", "f"), ("स्वादों", "m"), ("स्पर्शों", "m"), ("मन के विषयों", "m")]
SG1 = ["दृश्य रूप", "ध्वनि", "गंध", "स्वाद", "स्पर्श", "मन के विषय"]
SG1_G = ["m", "f", "f", "m", "m", "m"]


def six(first, last, pre):
    """first item in full, middle items 'pre X में…', last item in full"""
    mid = "… ".join(f"{pre(i)}" for i in range(1, 5))
    return f"{first}, {mid}… {last}"


def amanapa(g):
    return "मन को न भाने वाले" if g == "m" else "मन को न भाने वाली"


def kaarana(word, g):
    return f"{word} का कारण बनने {'वाले' if g == 'm' else 'वाली'}"


L("#### Chakkaniddeso", "#### छह-छह प्रकारों की व्याख्या")
L("##### (1) Cha vivādamūlāni", heads(1, CHAKKA14))
L("Tattha katamāni cha vivādamūlāni?",
  lst(CHAKKA14[0], "m", ["क्रोध", "दूसरों को नीचा दिखाना", "ईर्ष्या", "धूर्तता", "बुरी इच्छा", "अपनी दृष्टि को ही पकड़े रहना"]))
GR = f"सांसारिक जो {RAGA} है"
L("##### (2) Cha chandarāgā", heads(2, CHAKKA14))
L("Tattha katame cha chandarāgā?",
  f"{kaun(CHAKKA14[1], 'm')} चाह भरे राग सांसारिक परिघटनाएँ हैं। " +
  six(f"मनभावन {SG[0][0]} में {GR}", f"मनभावन {SG[5][0]} में {GR}", lambda i: f"मनभावन {SG[i][0]} में") +
  f" {D} {ime(CHAKKA14[1])}")
AGH = "मन का जो आक्रोश, प्रतिघात, उग्रता, कटु वचन, मन की अप्रसन्नता है"
L("##### (3) Cha virodhavatthūni", heads(3, CHAKKA14))
L("Tattha katamāni cha virodhavatthūni?",
  f"{kaun(CHAKKA14[2], 'm')} " +
  six(f"{amanapa(SG[0][1])} {SG[0][0]} पर {AGH}", f"{amanapa(SG[5][1])} {SG[5][0]} पर {AGH}",
      lambda i: f"{amanapa(SG[i][1])} {SG[i][0]} पर") + f" {D} {ime(CHAKKA14[2])}")
L("##### (4) Cha taṇhākāyā", heads(4, CHAKKA14))
L("Tattha katame cha taṇhākāyā?",
  lst(CHAKKA14[3], "m", ["दृश्य रूप की तृष्णा", "ध्वनि की तृष्णा", "गंध की तृष्णा", "स्वाद की तृष्णा", "स्पर्श की तृष्णा",
                         "मन के विषयों की तृष्णा"]))
AGARAVA = "के प्रति अनादर के साथ, बात पर कान न देते हुए रहता है"
L("##### (5) Cha agāravā", heads(5, CHAKKA14))
L("Tattha katame cha agāravā?",
  f"{kaun(CHAKKA14[4], 'm')} " +
  ", ".join(f"{x} {AGARAVA}" for x in ["गुरु", "शिक्षा", "संघ", "प्रशिक्षण", "लापरवाही न करने", "आदर-सत्कार"]) +
  f" {D} {ime(CHAKKA14[4])}")
PH4 = ["काम-काज में रमना", "बातचीत में रमना", "नींद में रमना", "भीड़-भाड़ में रमना"]
L("##### (6) Cha parihāniyā dhammā", heads(6, CHAKKA14))
L("Tattha katame cha parihāniyā dhammā?",
  lst(CHAKKA14[5], "f", PH4 + ["मेल-जोल में रमना", "मानसिक फैलाव में रमना"]))
L("##### (7) Aparepi cha parihāniyā dhammā", heads(7, CHAKKA14))
L("Tattha katame aparepi cha parihāniyā dhammā?",
  lst(CHAKKA14[6], "f", PH4 + ["सलाह न मानने की प्रवृत्ति", "बुरे मित्रों की संगति"], CHAKKA14[5]))


def upavicara(n, word, name):
    def obj(i):
        return f"{kaarana(word, SG1_G[i])} {SG1[i]} पर मन से विचरण करता है"
    body = (f"{SEE6[0]} {obj(0)}, " + "… ".join(SEE6[1:5]) + f"… {SEE6[5]} {obj(5)}")
    return f"{kaun(name, 'm')} {body} {D} {ime(name)}"


L("##### (8) Cha somanassupavicārā", heads(8, CHAKKA14))
L("Tattha katame cha somanassupavicārā?", upavicara(8, "प्रसन्नता", CHAKKA14[7]))
L("##### (9) Cha domanassupavicārā", heads(9, CHAKKA14))
L("Tattha katame cha domanassupavicārā?", upavicara(9, "उदासी", CHAKKA14[8]))
L("##### (10) Cha upekkhupavicārā", heads(10, CHAKKA14))
L("Tattha katame cha upekkhupavicārā?", upavicara(10, "समभाव", CHAKKA14[9]))
FEEL_SOM = ("मानसिक सुहावनापन, मानसिक सुख, मन के संपर्क से उत्पन्न सुहावना सुखद अनुभव, मन के संपर्क से उत्पन्न सुहावनी "
            "सुखद अनुभूति")                                                                                       # [pi-1 ^1-3]
FEEL_DOM = ("मानसिक असुहावनापन, मानसिक दुःख, मन के संपर्क से उत्पन्न असुहावना दुःखद अनुभव, मन के संपर्क से उत्पन्न "
            "असुहावनी दुःखद अनुभूति")                                                                             # [pi-1 ^1-415]
FEEL_UPE = ("न मानसिक सुहावनापन, न मानसिक असुहावनापन, मन के संपर्क से उत्पन्न न दुःखद, न सुखद अनुभव, मन के संपर्क से "
            "उत्पन्न न दुःखद, न सुखद अनुभूति")                                                                    # [pi-1 ^1-152]


def geha(name, g, adj, feel):
    def pre(i):
        return f"{adj(SG[i][1])} {SG[i][0]} में"
    return (f"{kaun(name, g)} " + six(f"{pre(0)} सांसारिक {feel}", f"{pre(5)} सांसारिक {feel}", pre) + f" {D} {ime(name)}")


L("##### (11) Cha gehasitāni somanassāni", heads(11, CHAKKA14))
L("Tattha katamāni cha gehasitāni somanassāni?", geha(CHAKKA14[10], "f", lambda g: "मनभावन", FEEL_SOM))
L("##### (12) Cha gehasitāni domanassāni", heads(12, CHAKKA14))
L("Tattha katamāni cha gehasitāni domanassāni?", geha(CHAKKA14[11], "f", amanapa, FEEL_DOM))
L("##### (13) Cha gehasitā upekkhā", heads(13, CHAKKA14))
L("Tattha katamā cha gehasitā upekkhā?", geha(CHAKKA14[12], "m", lambda g: kaarana("समभाव", g), FEEL_UPE))
SACCATO6 = "उसमें " + SACCATO
L("##### (14) Cha diṭṭhiyo", heads(14, CHAKKA14))
L("Tattha katamā cha diṭṭhiyo?",
  f"{kaun('छह दृष्टियाँ', 'f')} " +
  ", या ".join(f"“{s}”, {SACCATO6}" for s in
            ["मेरी आत्मा है", "मेरी आत्मा नहीं है", "मैं आत्मा से ही आत्मा को पहचानता हूँ", "मैं आत्मा से अनात्म को पहचानता हूँ",
             "मैं अनात्म से आत्मा को पहचानता हूँ"]) +
  f"; या फिर उसकी ऐसी दृष्टि होती है {D} “यह मेरी आत्मा, जो बोलने वाली है, अनुभव करने वाली है, जो जहाँ-तहाँ लंबे समय तक "
  f"अच्छे और बुरे कर्मों का फल भोगती है, ऐसा नहीं है कि वह उत्पन्न न हुई हो और न रही हो, ऐसा नहीं है कि वह उत्पन्न न होगी और "
  f"न रहेगी; वह नित्य, स्थिर, शाश्वत, न बदलने वाली है”, या फिर {SACCATO6}। {ime('छह दृष्टियाँ')}")
L("Chakkaṃ.", "छह-छह प्रकार।")

# ---------------------------------------------------------------- sevens
SEVEN = ["इंद्रिय-सुखों के राग", "चिढ़", "अहंकार", "दृष्टि", "संशय", "अस्तित्व के राग", "अज्ञान"]
L("#### Sattakaniddeso", "#### सात-सात प्रकारों की व्याख्या")
L("##### (1) Sattānusayā", heads(1, SATTAKA7))
L("Tattha katame sattānusayā?", lst(SATTAKA7[0], "f", [f"{x} की सुप्त प्रवृत्ति" for x in SEVEN]))
L("##### (2) Satta saṃyojanāni", heads(2, SATTAKA7))
L("Tattha katamāni satta saṃyojanāni?", lst(SATTAKA7[1], "m", [f"{x} का बंधन" for x in SEVEN]))
L("##### (3) Satta pariyuṭṭhānāni", heads(3, SATTAKA7))
L("Tattha katamāni satta pariyuṭṭhānāni?", lst(SATTAKA7[2], "m", [f"{x} का आवेश" for x in SEVEN]))
L("##### (4) Satta asaddhammā", heads(4, SATTAKA7))
L("Tattha katame satta asaddhammā?",
  lst(SATTAKA7[3], "m", [f"{x} होता है" for x in ["श्रद्धाहीन", "निर्लज्ज", "बुराई के प्रति निडर", "कम सुना-सीखा", "आलसी",
                                                  "सजगता खोया हुआ", "प्रज्ञाहीन"]]))
L("##### (5) Satta duccaritāni", heads(5, SATTAKA7))
L("Tattha katamāni satta duccaritāni?", lst(SATTAKA7[4], "m", DUCCARITA_10[:7]))
L("##### (6) Satta mānā", heads(6, SATTAKA7))
L("Tattha katame satta mānā?", lst(SATTAKA7[5], "m", NAMES_61_67))
ETTAVATA_U = f"तो {BHO}, इतने से यह आत्मा पूरी तरह मिट जाती है”। इस तरह कुछ लोग {UCCHEDA_DECL}।"
TAMANNO_Q = f"उससे कोई दूसरा ऐसा कहता है {D} “{BHO}, जिस आत्मा की तुम बात करते हो, वह है। मैं यह नहीं कहता कि ‘वह नहीं है’।"
NO_CA_U = f"परंतु {BHO}, इतने से यह आत्मा पूरी तरह नहीं मिटती।"
ANNO = f"{BHO}, एक दूसरी आत्मा है, जो"
KNOW = "उसे तुम न जानते हो, न देखते हो। उसे मैं जानता हूँ, देखता हूँ।"
SO_KHO = f"{BHO}, जब वह आत्मा शरीर छूटने पर नष्ट हो जाती है, विनष्ट हो जाती है, मृत्यु के बाद नहीं रहती,"


def seven(mark, desc, opener=TAMANNO_Q, close=""):
    end = (" " + close) if close else ""
    return f"({mark}) {opener} {NO_CA_U} {ANNO} {desc}। {KNOW} {SO_KHO} {ETTAVATA_U}{end}"


L("##### (7) Satta diṭṭhiyo", heads(7, SATTAKA7))
L("(Ka) tattha katamā satta diṭṭhiyo?",
  f"(क) {kaun('सात दृष्टियाँ', 'f')} {SAMANA} {D} “{BHO}, जब यह आत्मा भौतिक रूप वाली, चार महाभूतों से बनी "
  f"[वर्तनी-भेद (Sī., Syā.): cātummahābhūtiko], माता-पिता से उत्पन्न होकर शरीर छूटने पर नष्ट हो जाती है, विनष्ट हो जाती है, "
  f"मृत्यु के बाद नहीं रहती, {ETTAVATA_U}")
L("(Kha) tamañño evamāha",
  seven("ख", "दिव्य, भौतिक रूप वाली, इंद्रिय-सुखों के लोक की और कौर-कौर खाया जाने वाला भोजन खाने वाली है"))
L("(Ga) tamañño evamāha",
  seven("ग", "दिव्य, भौतिक रूप वाली, मन से बनी, सभी बड़े-छोटे अंगों से युक्त और पूर्ण इंद्रियों वाली है"))
L("(Gha) tamañño evamāha",
  seven("घ", "भौतिक रूप की पहचानों को पूरी तरह पार कर जाने से, टकराव की पहचानों के मिट जाने से, विविधता की पहचानों पर "
             "मनोयोग न करने से, “आकाश अनंत है” इस प्रकार अनंत आकाश के क्षेत्र तक पहुँची हुई है"))
L("(Ṅa) tamañño evamāha",
  seven("ङ", "अनंत आकाश के क्षेत्र को पूरी तरह पार करके, “चेतना अनंत है” इस प्रकार अनंत चेतना के क्षेत्र तक पहुँची हुई है"))
L("(Ca) tamañño evamāha",
  seven("च", "अनंत चेतना के क्षेत्र को पूरी तरह पार करके, “कुछ भी नहीं है” इस प्रकार कुछ भी न होने के क्षेत्र तक पहुँची हुई है"))
L("(Cha) tamañño evamāha",
  seven("छ", "कुछ भी न होने के क्षेत्र को पूरी तरह पार करके न पहचान, न अ-पहचान के क्षेत्र तक पहुँची हुई है",
        opener=f"उससे कोई दूसरा ऐसा कहता है {D} “जिस आत्मा की तुम बात करते हो, वह तो है। मैं यह नहीं कहता कि ‘वह नहीं है’।",
        close=ime("सात दृष्टियाँ")))
L("Sattakaṃ.", "सात-सात प्रकार।")

# ---------------------------------------------------------------- eights
L("#### Aṭṭhakaniddeso", "#### आठ-आठ प्रकारों की व्याख्या")
L("##### (1) Aṭṭha kilesavatthūni", heads(1, ATTHAKA8))
L("Tattha katamāni aṭṭha kilesavatthūni?", lst(ATTHAKA8[0], "m", KILESA_10[:8]))
L("##### (2) Aṭṭha kusītavatthūni", heads(2, ATTHAKA8))
L("Tattha katamāni aṭṭha kusītavatthūni?", kaun(ATTHAKA8[1], "m"))
LIE = "चलो, मैं लेट जाता हूँ”।"
KUS_END = ("वह लेट जाता है; जो प्राप्त नहीं हुआ उसकी प्राप्ति के लिए, जो पाया नहीं उसे पाने के लिए, जिसका साक्षात्कार नहीं हुआ "
           "उसके साक्षात्कार के लिए उत्साह नहीं जगाता।")
ORD = ["पहला", "दूसरा", "तीसरा", "चौथा", "पाँचवाँ", "छठा", "सातवाँ", "आठवाँ"]


def kus(i):
    return f"{KUS_END} यह आलसीपन का {ORD[i]} आधार है।"


TASSA = f"उसे ऐसा होता है {D} “"
PUNA = "और फिर,"
PIND = "गाँव या कस्बे में भिक्षा के लिए घूमते हुए रूखा-सूखा या बढ़िया, जितना चाहिए उतना भरपूर भोजन"
L("(Ka) idha bhikkhunā kammaṃ kātabbaṃ",
  f"(क) यहाँ भिक्षु को कोई काम करना होता है। {TASSA}मुझे काम करना होगा। पर काम करते हुए मेरा शरीर थक जाएगा। {LIE} {kus(0)}")
L("(Kha) puna caparaṃ bhikkhunā kammaṃ kataṃ",
  f"(ख) {PUNA} भिक्षु ने कोई काम कर लिया होता है। {TASSA}मैंने काम कर लिया। पर काम करते हुए मेरा शरीर थक गया है। {LIE} {kus(1)}")
L("(Ga) puna caparaṃ bhikkhunā maggo gantabbo",
  f"(ग) {PUNA} भिक्षु को कहीं रास्ते पर जाना होता है। {TASSA}मुझे रास्ते पर जाना होगा। पर रास्ते पर जाते हुए मेरा शरीर थक जाएगा। "
  f"{LIE} {kus(2)}")
L("(Gha) puna caparaṃ bhikkhunā maggo gato",
  f"(घ) {PUNA} भिक्षु रास्ते पर जा चुका होता है। {TASSA}मैं रास्ते पर जा चुका। पर रास्ते पर जाते हुए मेरा शरीर थक गया है। "
  f"{LIE} {kus(3)}")
L("(Ṅa) puna caparaṃ bhikkhu gāmaṃ",
  f"(ङ) {PUNA} भिक्षु {PIND} नहीं पाता। {TASSA}मैंने {PIND} नहीं पाया। मेरा शरीर थका हुआ है, काम के लायक़ नहीं है। {LIE} {kus(4)}")
L("(Ca) puna caparaṃ bhikkhu gāmaṃ",
  f"(च) {PUNA} भिक्षु {PIND} पाता है। {TASSA}मैंने {PIND} पाया। मेरा शरीर थका हुआ है, काम के लायक़ नहीं है, मानो भीगे उड़द-सा "
  f"भारी हो। {LIE} {kus(5)}")
L("(Cha) puna caparaṃ bhikkhuno uppanno",
  f"(छ) {PUNA} भिक्षु को कोई छोटा-सा रोग हो जाता है। {TASSA}मुझे यह छोटा-सा रोग हो गया है। लेट जाना ठीक रहेगा। {LIE} {kus(6)}")
L("(Ja) puna caparaṃ bhikkhu gilānā",
  f"(ज) {PUNA} भिक्षु रोग से उठा होता है [वर्तनी-भेद (saddanībhi): gilānavuṭṭhito; a. ni. 6.16 की पालि की टीका देखनी चाहिए], "
  f"रोग से उठे उसे अधिक समय नहीं हुआ होता। {TASSA}मैं रोग से उठा हूँ, रोग से उठे मुझे अधिक समय नहीं हुआ। मेरा शरीर दुर्बल है, "
  f"काम के लायक़ नहीं है। {LIE} {kus(7)} {ime(ATTHAKA8[1])}")
LD = "आठ सांसारिक परिघटनाओं"
L("##### (3) Aṭṭhasu lokadhammesu", heads(3, ATTHAKA8))
L("Tattha katamesu aṭṭhasu lokadhammesu",
  f"{q(ATTHAKA8[2])} लाभ में प्रबल राग, हानि में प्रतिविरोध, यश में प्रबल राग, अपयश में प्रतिविरोध, प्रशंसा में प्रबल राग, "
  f"निंदा में प्रतिविरोध, सुख में प्रबल राग, दुःख में प्रतिविरोध {D} यह {ATTHAKA8[2]} है।")
L("##### (4) Aṭṭhaanariyavohārā", heads(4, ATTHAKA8))
L("Tattha katame aṭṭha anariyavohārā?", lst(ATTHAKA8[3], "m", AV_A + AV_B))
L("##### (5) Aṭṭha micchattā", heads(5, ATTHAKA8))
L("Tattha katame aṭṭha micchattā?", lst(ATTHAKA8[4], "m", MICCHATTA_10[:8]))
COD = "भिक्षु किसी भिक्षु पर अपराध का आरोप लगाते हैं। भिक्षुओं द्वारा अपराध का आरोप लगाए जाने पर"
ORD_M = ORD


def pd(i):
    return f"यह व्यक्ति का {ORD_M[i]} दोष है।"


L("##### (6) Aṭṭha purisadosā", heads(6, ATTHAKA8))
L("Tattha katame aṭṭha purisadosā?",
  f"{kaun(ATTHAKA8[5], 'm')} (क) यहाँ भिक्षु किसी भिक्षु पर अपराध का आरोप लगाते हैं। भिक्षुओं द्वारा अपराध का आरोप लगाए जाने पर "
  f"[वर्तनी-भेद (Sī., Syā.): codiyamāno; a. ni. 8.14] वह भिक्षु “मुझे याद नहीं, मुझे याद नहीं” कहकर भूलने के बहाने से टाल "
  f"देता है। {pd(0)}")
L("(Kha) puna caparaṃ bhikkhū",
  f"(ख) {PUNA} {COD} वह भिक्षु आरोप लगाने वाले पर ही पलटवार करता है {D} “तुझ मूर्ख, अनाड़ी के कहने से क्या होगा! तू भी मुझसे "
  f"कुछ कहने की सोचता है!” {pd(1)}")
L("(Ga) puna caparaṃ bhikkhū",
  f"(ग) {PUNA} {COD} वह भिक्षु आरोप लगाने वाले पर ही [पाठभेद (Syā.): codakasseva; a. ni. 8.14] उलटा आरोप लगाता है {D} "
  f"“तुमने भी तो अमुक अपराध किया है। पहले तुम उसका प्रायश्चित्त करो”। {pd(2)}")
L("(Gha) puna caparaṃ bhikkhū",
  f"(घ) {PUNA} {COD} वह भिक्षु एक बात से दूसरी बात पर टाल देता है, बात को बाहर की ओर मोड़ देता है, क्रोध, द्वेष और असंतोष "
  f"प्रकट करता है। {pd(3)}")
L("(Ṅa) puna caparaṃ bhikkhū",
  f"(ङ) {PUNA} {COD} वह भिक्षु संघ के बीच हाथ फेंक-फेंककर बोलता है। {pd(4)}")
L("(Ca) puna caparaṃ bhikkhū",
  f"(च) {PUNA} {COD} वह भिक्षु संघ की परवाह न करके, आरोप लगाने वाले की परवाह न करके, अपराधी रहते हुए ही "
  f"[पाठभेद (Ka.): āpattikova; a. ni. 8.14] जहाँ मन हो चला जाता है। {pd(5)}")
L("(Cha) puna caparaṃ bhikkhū",
  f"(छ) {PUNA} {COD} वह भिक्षु “न तो मैंने अपराध किया है, न मैंने अपराध नहीं किया है” कहकर चुप रहकर संघ को परेशान करता है। "
  f"{pd(6)}")
L("(Ja) puna caparaṃ bhikkhū",
  f"(ज) {PUNA} {COD} वह भिक्षु ऐसा कहता है {D} “आप आयुष्मान लोग मेरे पीछे इतना क्यों पड़े हैं? अब मैं प्रशिक्षण छोड़कर गृहस्थ "
  f"जीवन में लौट जाऊँगा”। वह प्रशिक्षण छोड़कर गृहस्थ जीवन में लौटकर ऐसा कहता है {D} “अब आप आयुष्मान लोग प्रसन्न हो जाइए”। "
  f"{pd(7)} {ime(ATTHAKA8[5])}")
AT8 = ["भौतिक रूप वाली", "भौतिक रूप से रहित", "भौतिक रूप वाली भी और भौतिक रूप से रहित भी", "न भौतिक रूप वाली, न भौतिक रूप से रहित",
       "सीमित", "असीम", "सीमित भी और असीम भी", "न सीमित, न असीम"]


def vada(attr, label):
    return f"“{DEATH} {attr} {AROGO}” {D} उसे {label} बताते हैं"


L("##### (7) Aṭṭha asaññīvādā", heads(7, ATTHAKA8))
L("Tattha katame aṭṭha asaññīvādā?",
  f"{kaun(ATTHAKA8[6], 'm')} {vada(AT8[0], 'पहचान से रहित')}; भौतिक रूप से रहित आत्मा… भौतिक रूप वाली भी और भौतिक रूप से "
  f"रहित भी… न भौतिक रूप वाली, न भौतिक रूप से रहित… " + "; ".join(vada(a, "पहचान से रहित") for a in AT8[4:]) +
  f"। {ime(ATTHAKA8[6])}")
L("##### (8) Aṭṭha nevasaññīnāsaññīvādā", heads(8, ATTHAKA8))
L("Tattha katame aṭṭha nevasaññīnāsaññīvādā?",
  f"{kaun(ATTHAKA8[7], 'm')} " + "; ".join(vada(a, "न पहचान वाली, न पहचान से रहित") for a in AT8) + f"। {ime(ATTHAKA8[7])}")
L("Aṭṭhakaṃ.", "आठ-आठ प्रकार।")

# ---------------------------------------------------------------- nines
L("#### Navakaniddeso", "#### नौ-नौ प्रकारों की व्याख्या")
L("##### (1) Nava āghātavatthūni", heads(1, NAVAKA9))
L("Tattha katamāni nava āghātavatthūni?", f"{kaun(NAVAKA9[0], 'm')} {DOSA_1.format(s=';')}। {ime(NAVAKA9[0])}")
L("##### (2) Nava purisamalāni", heads(2, NAVAKA9))
L("Tattha katamāni nava purisamalāni?",
  lst(NAVAKA9[1], "m", ["क्रोध", "दूसरों को नीचा दिखाना", "ईर्ष्या", "कंजूसी", "कपट", "धूर्तता", "झूठ बोलना", "बुरी इच्छा",
                        "ग़लत दृष्टि"]))
L("##### (3) Navavidhā mānā", heads(3, NAVAKA9))
L("Tattha katame navavidhā mānā?",
  f"{kaun(NAVAKA9[2], 'm')} " + ", ".join(mana_name(w, i) for w in ("seyya", "sadisa", "hina")
                                            for i in ("seyya", "sadisa", "hina")) + f" {D} {ime(NAVAKA9[2])}")
L("##### (4) Nava taṇhāmūlakā dhammā", heads(4, NAVAKA9))
CH = ["तृष्णा", "खोज", "लाभ", "निर्णय", "चाह भरे राग", "चिपके रहने", "अपना बना लेने", "कंजूसी", "रखवाली"]
CH_NOM = ["खोज", "लाभ", "निर्णय", "चाह भरा राग", "चिपके रहना", "अपना बना लेना", "कंजूसी", "रखवाली"]
L("Tattha katame nava taṇhāmūlakā dhammā?",
  f"{kaun(NAVAKA9[3], 'f')} " + ", ".join(f"{CH[i]} के कारण {CH_NOM[i]}" for i in range(8)) +
  ", रखवाली के कारण डंडा उठाना, शस्त्र उठाना, कलह, झगड़ा, विवाद, तू-तू मैं-मैं, चुगली, झूठ बोलना जैसी अनेक बुरी हानिकर "
  f"परिघटनाएँ उत्पन्न होती हैं {D} {ime(NAVAKA9[3])}")
NINE_I = ["मैं हूँ", "मैं ही हूँ", "यह मैं हूँ", "मैं होऊँगा", "मैं भौतिक रूप वाला होऊँगा", "मैं भौतिक रूप से रहित होऊँगा",
          "मैं पहचान वाला होऊँगा", "मैं पहचान से रहित होऊँगा", "मैं न पहचान वाला, न पहचान से रहित होऊँगा"]
L("##### (5) Nava iñjitāni", heads(5, NAVAKA9))
L("Tattha katamāni nava iñjitāni?",
  f"{kaun(NAVAKA9[4], 'f')} " + ", ".join(f"“{x}” यह हलचल है" for x in NINE_I) + f" {D} {ime(NAVAKA9[4])}")
L("##### (6-9) Nava maññitādīni", "##### (6-9) नौ मान्यताएँ आदि")
L("Tattha katamāni nava maññitāni",
  "यहाँ नौ मान्यताएँ… नौ छटपटाहटें… नौ मानसिक फैलाव… नौ निर्मितियाँ कौन-सी हैं? " +
  ", ".join(f"“{x}” यह निर्मित है" for x in NINE_I) + f" {D} {ime(NAVAKA9[8])}")
L("Navakaṃ.", "नौ-नौ प्रकार।")

# ---------------------------------------------------------------- tens
L("#### Dasakaniddeso", "#### दस-दस प्रकारों की व्याख्या")
L("##### (1) Dasa kilesavatthūni", heads(1, DASAKA7))
L("Tattha katamāni dasa kilesavatthūni?", lst(DASAKA7[0], "m", KILESA_10))
L("##### (2) Dasa āghātavatthūni", heads(2, DASAKA7))
L("Tattha katamāni dasa āghātavatthūni?", f"{kaun(DASAKA7[1], 'm')} {DOSA_1.format(s=',')}, {ATTHANE} {D} {ime(DASAKA7[1])}")
L("##### (3) Dasa akusalakammapathā", heads(3, DASAKA7))
L("Tattha katame dasa akusalakammapathā?", lst(DASAKA7[2], "m", DUCCARITA_10))
TEN_S = ["इंद्रिय-सुखों के राग", "चिढ़", "अहंकार", "दृष्टि", "संशय", "सदाचार और व्रतों के बारे में ग़लत धारणा", "अस्तित्व के राग",
         "ईर्ष्या", "कंजूसी", "अज्ञान"]
L("##### (4) Dasa saṃyojanāni", heads(4, DASAKA7))
L("Tattha katamāni dasa saṃyojanāni?", lst(DASAKA7[3], "m", [f"{x} का बंधन" for x in TEN_S]))
L("##### (5) Dasa micchattā", heads(5, DASAKA7))
L("Tattha katame dasa micchattā?", lst(DASAKA7[4], "m", MICCHATTA_10))
L("##### (6) Dasavatthukā micchādiṭṭhi", heads(6, DASAKA7))
L("Tattha katamā dasavatthukā micchādiṭṭhi?",
  f"{q(DASAKA7[5])} “{NATTHI_DINNAM.format(v=' [पाठभेद (Ka.): samaggatā]')}” {D} यह {DASAKA7[5]} है।")
L("##### (7) Dasavatthukā antaggāhikā diṭṭhi", heads(7, DASAKA7))
L("Tattha katamā dasavatthukā antaggāhikā diṭṭhi?", f"{q(DASAKA7[6])} {SASSATO_LOKO_ALL} {D} यह {DASAKA7[6]} है।")
L("Dasakaṃ.", "दस-दस प्रकार।")
