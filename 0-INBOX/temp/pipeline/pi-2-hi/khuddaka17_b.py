# -*- coding: utf-8 -*-
"""Chapter 17, part B: exposition of the twos (dukaniddesa) and the threes (tikaniddesa)."""
from khuddaka17_f import *
from khuddaka17_a import DUKA18, TIKA35, ARATI, LINATTA

LINES = []


def L(p, h):
    LINES.append((p, h))


def heads(n, items):
    return "##### (" + str(n) + ") " + items[n - 1].split(" [")[0]


# ---------------------------------------------------------------- twos
L("#### Dukaniddeso", "#### दो-दो प्रकारों की व्याख्या")
L("##### (1) Kodho ca", heads(1, DUKA18))
L("(Ka) tattha katamo kodho?", f"(क) {q('क्रोध')} जो {KODHA_SYN} है {D} {called('क्रोध', 'm')}")
L("(Kha) tattha katamo upanāho?",
  f"(ख) {q('बैर')} पहले क्रोध होता है, बाद में बैर। इस प्रकार का जो बैर, बैर रखना, बैर से भरा होना, मन में जमाए रखना, "
  f"टिकाए रखना, अच्छी तरह टिकाए रखना, बार-बार जोड़ते रहना, लगातार बनाए रखना, क्रोध को पक्का करना है {D} {called('बैर', 'm')}")
L("##### (2) Makkho", heads(2, DUKA18))
L("(Ka) tattha katamo makkho?",
  f"(क) {q('दूसरों को नीचा दिखाना')} जो दूसरों को नीचा दिखाना, नीचा दिखाने की क्रिया, नीचा दिखाने के भाव से भरा होना "
  f"[वर्तनी-भेद (Sī., Ka.): makkhiyanā makkhiyitattaṃ], निष्ठुरता, निष्ठुर व्यवहार करना है {D} "
  f"{called('दूसरों को नीचा दिखाना', 'm')}")
L("(Kha) tattha katamo paḷāso?",
  f"(ख) {q('बराबरी की होड़')} जो बराबरी की होड़, होड़ करना [वर्तनी-भेद (Syā.): palāsāyanā palāsāyitattaṃ], होड़ का रवैया, "
  f"झगड़े का कारण, बराबरी पर अड़ना, अपनी बात न छोड़ना है {D} {called('बराबरी की होड़', 'f')}")
L("##### (3) Issā", heads(3, DUKA18))
L("(Ka) tattha katamā issā?",
  f"(क) {q('ईर्ष्या')} दूसरों के लाभ, सत्कार, सम्मान, आदर, वंदना और पूजा पर जो ईर्ष्या, ईर्ष्या करना, ईर्ष्या से भरा होना, "
  f"जलन, जलना, जलन से भरा होना है {D} {called('ईर्ष्या', 'f')}")
L("(Kha) tattha katamaṃ macchariyaṃ?",
  f"(ख) {q('कंजूसी')} {MACCHARIYA_5} {MACCHARIYA_SYN_A}, मन का संकुचित होना [पाठभेद (Sī., Ka.): paggahitattaṃ; dha. sa. 1127] "
  f"है {D} {called('कंजूसी', 'f')}")
MAYA_WISH = "“कोई मेरे बारे में न जान पाए”"
L("##### (4) Māyā", heads(4, DUKA18))
L("(Ka) tattha katamā māyā?",
  f"(क) {q('कपट')} यहाँ कोई व्यक्ति शरीर से दुराचरण करके, वाणी से दुराचरण करके, मन से दुराचरण करके उसे छिपाने के लिए "
  f"बुरी इच्छा ठान लेता है। वह चाहता है कि {MAYA_WISH}। संकल्प करता है कि {MAYA_WISH}। ऐसी बात बोलता है कि {MAYA_WISH}। "
  f"शरीर से प्रयत्न करता है कि {MAYA_WISH}। इस प्रकार का जो कपट, कपटीपन, अति-चालाकी, ठगी, छल, बात घुमाना, टालमटोल, "
  f"छिपाना, पूरी तरह छिपाना, ढकना, ढककर छिपाना, साफ़-साफ़ न बताना, प्रकट न करना, अच्छी तरह ढक देना, पाप-कर्म है {D} "
  f"{called('कपट', 'm')}")
L("(Kha) tattha katamaṃ sāṭheyyaṃ?",
  f"(ख) {q('धूर्तता')} यहाँ कोई व्यक्ति धूर्त होता है, पूरी तरह धूर्त। उसमें जो धूर्तपन, धूर्त होना, धूर्तता, कुटिलता, कुटिल व्यवहार "
  f"[पाठभेद (Syā.): kakkhaḷatā kakkhaḷiyaṃ], चालाकी, चालबाज़ी है {D} {called('धूर्तता', 'f')}")
L("##### (5) Avijjā", heads(5, DUKA18))
L("(Ka) tattha katamā avijjā?", f"(क) {q('अज्ञान')} {YAM_ANNANAM} {D} {called('अज्ञान', 'm')}")
L("(Kha) tattha katamā bhavataṇhā?", f"(ख) {q('अस्तित्व की तृष्णा')} {BHAVA_FULL} {D} {called('अस्तित्व की तृष्णा', 'f')}")


def view(mark, name, belief, quoted=True):
    c = called(name, "f") if quoted else called_plain(name, "f")
    return f"({mark}) {q(name)} “{belief}” {D} {DITTHI_PE} {D} {c}"


L("##### (6) Bhavadiṭṭhi", heads(6, DUKA18))
L("(Ka) tattha katamā bhavadiṭṭhi?", view("क", "अस्तित्व की दृष्टि", "आत्मा और लोक बने रहेंगे"))
L("(Kha) tattha katamā vibhavadiṭṭhi?", view("ख", "अनस्तित्व की दृष्टि", "आत्मा और लोक नहीं रहेंगे", quoted=False))
L("##### (7) Sassatadiṭṭhi", heads(7, DUKA18))
L("(Ka) tattha katamā sassatadiṭṭhi?", view("क", "शाश्वतता की दृष्टि", "आत्मा और लोक शाश्वत हैं"))
L("(Kha) tattha katamā ucchedadiṭṭhi?", view("ख", "विनाश की दृष्टि", "आत्मा और लोक नष्ट हो जाएँगे"))
L("##### (8) Antavādiṭṭhi", heads(8, DUKA18))
L("(Ka) tattha katamā antavādiṭṭhi?", view("क", "सीमितता की दृष्टि", "आत्मा और लोक सीमित हैं"))
L("(Kha) tattha katamā anantavādiṭṭhi?", view("ख", "असीमता की दृष्टि", "आत्मा और लोक असीम हैं"))
L("##### (9) Pubbantānudiṭṭhi", heads(9, DUKA18))
L("(Ka) tattha katamā pubbantānudiṭṭhi?",
  f"(क) {q('अतीत के बारे में दृष्टि')} अतीत को लेकर जो दृष्टि, दृष्टियों में फँसना… उलटी पकड़ उत्पन्न होती है {D} "
  f"{called('अतीत के बारे में दृष्टि', 'f')}")
L("(Kha) tattha katamā aparantānudiṭṭhi?",
  f"(ख) {q('भविष्य के बारे में दृष्टि')} भविष्य को लेकर जो दृष्टि, दृष्टियों में फँसना… उलटी पकड़ उत्पन्न होती है {D} "
  f"{called('भविष्य के बारे में दृष्टि', 'f')}")
AHIRIKA_L = f"{q('निर्लज्जता')} {AHIRIKA} {D} {called('निर्लज्जता', 'f')}"
ANOTTAPPA_L = f"{q('बुराई के प्रति निडरता')} {ANOTTAPPA} {D} {called('बुराई के प्रति निडरता', 'f')}"
L("##### (10) Ahirikañca", heads(10, DUKA18))
L("(Ka) tattha katamaṃ ahirikaṃ?", "(क) " + AHIRIKA_L)
L("(Kha) tattha katamaṃ anottappaṃ?", "(ख) " + ANOTTAPPA_L)
DOVA_L = f"{q('सलाह न मानने की प्रवृत्ति')} {DOVACASSA} {D} {called('सलाह न मानने की प्रवृत्ति', 'f')}"


def papamitta(extra, tam):
    return f"{q('बुरे मित्रों की संगति')} {PAPAMITTA_WHO}, उनकी जो {sevana(extra, tam)} है {D} {called('बुरे मित्रों की संगति', 'f')}"


L("##### (11) Dovacassatā", heads(11, DUKA18))
L("(Ka) tattha katamā dovacassatā?", "(क) " + DOVA_L)
L("(Kha) tattha katamā pāpamittatā?", "(ख) " + papamitta(False, False))
L("##### (12) Anajjavo", heads(12, DUKA18))
L("(Ka) tattha katamo anajjavo?",
  f"(क) {q('सरलता का अभाव')} जो सरलता का अभाव, सरल न होना, टेढ़ापन, वक्रता, कुटिलता है {D} {called('सरलता का अभाव', 'm')}")
L("(Kha) tattha katamo amaddavo?",
  f"(ख) {q('कोमलता का अभाव')} जो मृदुता का अभाव, कोमलता का अभाव, कठोरता, रूखापन, कठोर होना, कड़ापन "
  f"[वर्तनी-भेद (Syā., Ka.): kathinatā], मन का तना रहना, मृदुता का अभाव है {D} {called('कोमलता का अभाव', 'm')}")
L("##### (13) Akkhanti", heads(13, DUKA18))
L("(Ka) tattha katamā akkhanti?",
  f"(क) {q('सहनशीलता का अभाव')} जो सहनशीलता का अभाव, क्षमा न करना, सह न पाना, उग्रता, कटु वचन, मन की अप्रसन्नता है {D} "
  f"{called('सहनशीलता का अभाव', 'm')}")
L("(Kha) tattha katamaṃ asoraccaṃ?",
  f"(ख) {q('सौम्यता का अभाव')} {VITIKKAMA} {D} {called('सौम्यता का अभाव', 'm')} सारा दुराचार भी सौम्यता का अभाव है।")
L("##### (14) Asākhalyañca", heads(14, DUKA18))
L("(Ka) tattha katamaṃ asākhalyaṃ?",
  f"(क) {q('मधुर व्यवहार का अभाव')} जो वाणी काँटेदार, कठोर, दूसरों को कड़वी लगने वाली, दूसरों को चुभने वाली, क्रोध के निकट की "
  f"और एकाग्रता की ओर न ले जाने वाली है, कोई वैसी वाणी बोलने वाला होता है। उसमें जो कोमल न होने वाली वाणी, मधुर न होने "
  f"वाली वाणी, कठोर वाणी है {D} {called('मधुर व्यवहार का अभाव', 'm')}")
L("(Kha) tattha katamo appaṭisanthāro",
  f"(ख) यहाँ आदर-सत्कार का अभाव [वर्तनी-भेद (Ka.): appaṭisandhāro] क्या है? दो आदर-सत्कार {D} भौतिक वस्तुओं से "
  f"आदर-सत्कार और शिक्षा से आदर-सत्कार। यहाँ कोई व्यक्ति भौतिक वस्तुओं से या शिक्षा से आदर-सत्कार न करने वाला होता है "
  f"{D} {called('आदर-सत्कार का अभाव', 'm')}")
L("##### (15) Indriyesu", heads(15, DUKA18))
INDR_NAME = "इंद्रियों के द्वारों की रक्षा न करने की प्रवृत्ति"
L("(Ka) tattha katamā indriyesu aguttadvāratā?",
  f"(क) {q(INDR_NAME)} {INDRIYA_AGUTTA}। {INDRIYA_AGUTTA_END} {D} {called(INDR_NAME, 'f')}")
L("(Kha) tattha katamā bhojane amattaññutā?",
  f"(ख) {q('भोजन में मात्रा के ज्ञान का अभाव')} यहाँ कोई व्यक्ति बिना सोचे-विचारे, अनुचित ढंग से, मौज के लिए, मद के लिए, "
  f"शरीर सुडौल बनाने के लिए, सुंदर दिखने के लिए भोजन करता है। भोजन के विषय में यहाँ जो संतुष्ट न होना, मात्रा के ज्ञान का अभाव, "
  f"बिना सोचे-विचारे होना है {D} {called('भोजन में मात्रा के ज्ञान का अभाव', 'm')}")
MUTTHA_L = f"{q('सजगता की कमी')} {MUTTHASSACCA} {D} {called('सजगता की कमी', 'f')}"
ASAMPAJ_L = f"{q('स्पष्ट समझ का अभाव')} {YAM_ANNANAM} {D} {called('स्पष्ट समझ का अभाव', 'm')}"
L("##### (16) Muṭṭhassaccañca", heads(16, DUKA18))
L("(Ka) tattha katamaṃ muṭṭhassaccaṃ?", "(क) " + MUTTHA_L)
L("(Kha) tattha katamaṃ asampajaññaṃ?", "(ख) " + ASAMPAJ_L)
L("##### (17) Sīlavipatti", heads(17, DUKA18))
L("(Ka) tattha katamā sīlavipatti?",
  f"(क) {q('सदाचार में विफलता')} जो {VITIKKAMA} है {D} {called('सदाचार में विफलता', 'f')} सारा दुराचार भी सदाचार में विफलता है।")
MICCHADITTHI_BODY = f"“{NATTHI_DINNAM_PE}” {D} {DITTHI_PE}"
L("(Kha) tattha katamā diṭṭhivipatti?",
  f"(ख) {q('दृष्टि में विफलता')} {MICCHADITTHI_BODY} {D} {called('दृष्टि में विफलता', 'f')} "
  f"सारी ग़लत दृष्टि भी दृष्टि में विफलता है।")
ORAM = "निचले लोकों से बाँधने वाले पाँच बंधन"
UDDHAM = "ऊपरी लोकों से बाँधने वाले पाँच बंधन"
L("##### (18) Ajjhattasaṃyojanañca", heads(18, DUKA18))
L("(Ka) tattha katamaṃ ajjhattasaṃyojanaṃ?",
  f"(क) {q('भीतरी बंधन')} {ORAM} {D} भीतरी बंधन। (ख) {UDDHAM} {D} बाहरी बंधन।")
L("Dukaṃ.", "दो-दो प्रकार।")

# ---------------------------------------------------------------- threes
L("#### Tikaniddeso", "#### तीन-तीन प्रकारों की व्याख्या")
L("##### (1) Tīṇi akusalamūlāni", heads(1, TIKA35))
L("Tattha katamāni tīṇi akusalamūlāni?", f"{kaun('तीन हानिकर मूल', 'm')} लोभ, द्वेष, मोह।")
L("(Ka) tattha katamo lobho?",
  f"(क) {q('लोभ')} {LOBHA_SYN_1} [पाठभेद (Sī., Ka.): visadā; dha. sa. 1141], {LOBHA_SYN_2} [वर्तनी-भेद (Ka.): āyūhinī], "
  f"{LOBHA_SYN_3} [वर्तनी-भेद (Ka.): sandhavo], {LOBHA_SYN_4} [वर्तनी-भेद (Sī., Syā.): āsiṃsanā āsiṃsitattaṃ], "
  f"{LOBHA_SYN_5} {D} {called('लोभ', 'm')}")
L("(Kha) tattha katamo doso?", f"(ख) {q('द्वेष')} {DOSA_1.format(s=',')}, {ATTHANE}। {DOSA_2} {D} {called('द्वेष', 'm')}")
L("(Ga) tattha katamo moho?",
  f"(ग) {q('मोह')} {MOHA_KNOW}, {YAM_EVARUPAM_ANNANAM} {D} {called('मोह', 'm')} {ime('तीन हानिकर मूल')}")

KV = ["इंद्रिय-सुखों का विचार", "दुर्भावना का विचार", "हिंसा का विचार"]
KV_SRC = ["इंद्रिय-सुखों", "दुर्भावना", "हिंसा"]
MARKS = ["क", "ख", "ग"]
PM = ["(Ka)", "(Kha)", "(Ga)"]


def vitakka_lines(close):
    for i in range(3):
        end = (" " + close) if i == 2 else ""
        L(f"{PM[i]} tattha katamo", f"({MARKS[i]}) {q(KV[i])} {KV_SRC[i]} से जुड़ा जो {TAKKA} है {D} {called(KV[i], 'm')}{end}")


L("##### (2) Tayo akusalavitakkā", heads(2, TIKA35))
L("Tattha katame tayo akusalavitakkā?", f"{kaun('तीन हानिकर विचार', 'm')} {', '.join(KV)}।")
vitakka_lines(ime("तीन हानिकर विचार"))
KS = ["इंद्रिय-सुखों की पहचान", "दुर्भावना की पहचान", "हिंसा की पहचान"]
L("##### (3) Tisso akusalasaññā", heads(3, TIKA35))
L("Tattha katamā tisso akusalasaññā?", f"{kaun('तीन हानिकर पहचानें', 'f')} {', '.join(KS)}।")
for i in range(3):
    end = (" " + ime("तीन हानिकर पहचानें")) if i == 2 else ""
    L(f"{PM[i]} tattha katamā",
      f"({MARKS[i]}) {q(KS[i])} {KV_SRC[i]} से जुड़ी जो पहचान, पहचानना, पहचान चुका होना है {D} {called(KS[i], 'f')}{end}")
KD = ["इंद्रिय-सुखों का तत्व", "दुर्भावना का तत्व", "हिंसा का तत्व"]
L("##### (4) Tisso akusaladhātuyo", heads(4, TIKA35))
L("Tattha katamā tisso akusaladhātuyo?", f"{kaun('तीन हानिकर तत्व', 'm')} {', '.join(KD)}।")
L("Tattha katamā kāmadhātu?", f"{q(KD[0])} " + " ".join(f"{KV[i]} {KD[i]} है।" for i in range(3)))
vitakka_lines(ime("तीन हानिकर तत्व"))
DC = ["शारीरिक दुराचरण", "वाचिक दुराचरण", "मानसिक दुराचरण"]
L("##### (5) Tīṇi duccaritāni", heads(5, TIKA35))
L("Tattha katamāni tīṇi duccaritāni?", f"{kaun('तीन दुराचरण', 'm')} {', '.join(DC)}।")
L("(Ka) tattha katamaṃ kāyaduccaritaṃ?", f"(क) {q(DC[0])} {', '.join(DUCCARITA_10[:3])} {D} {called(DC[0], 'm')}")
L("(Kha) tattha katamaṃ vacīduccaritaṃ?", f"(ख) {q(DC[1])} {', '.join(DUCCARITA_10[3:7])} {D} {called(DC[1], 'm')}")
L("(Ga) tattha katamaṃ manoduccaritaṃ?", f"(ग) {q(DC[2])} {', '.join(DUCCARITA_10[7:])} {D} {called(DC[2], 'm')}")
KM = ["शारीरिक कर्म", "वाचिक कर्म", "मानसिक कर्म"]
KC = ["शारीरिक इरादा", "वाचिक इरादा", "मानसिक इरादा"]
L("(Ka-ga) tattha katamaṃ kāyaduccaritaṃ?",
  f"(क-ग) {q(DC[0])} " + ", ".join(f"हानिकर {KM[i]} {DC[i]} है" for i in range(3)) + "।")
L("Tattha katamaṃ akusalaṃ kāyakammaṃ?",
  f"{q('हानिकर ' + KM[0])} " + ", ".join(f"हानिकर {KC[i]} हानिकर {KM[i]} है" for i in range(3)) + "। " + ime("तीन दुराचरण"))
AS = ["इंद्रिय-सुखों का मैल", "अस्तित्व का मैल", "अज्ञान का मैल"]
L("##### (6) Tayo āsavā", heads(6, TIKA35))
L("Tattha katame tayo āsavā?", f"{kaun('मन के तीन मैल', 'm')} {', '.join(AS)}।")
L("(Ka) tattha katamo kāmāsavo?", f"(क) {q(AS[0])} {KAMA_FULL} {D} {called(AS[0], 'm')}")
L("(Kha) tattha katamo bhavāsavo?", f"(ख) {q(AS[1])} {BHAVA_PE} {D} {called(AS[1], 'm')}")
L("(Ga) tattha katamo avijjāsavo?",
  f"(ग) {q(AS[2])} दुःख को न जानना… अज्ञान की रुकावट, मोह रूपी हानिकर मूल है {D} {called(AS[2], 'm')} {ime('मन के तीन मैल')}")
SJ = ["स्थायी आत्मा की ग़लत दृष्टि", "संशय", "सदाचार और व्रतों के बारे में ग़लत धारणा"]
L("##### (7) Tīṇi saṃyojanāni", heads(7, TIKA35))
L("Tattha katamāni tīṇi saṃyojanāni?", f"{kaun('तीन बंधन', 'm')} {', '.join(SJ)}।")
L("(Ka) tattha katamā sakkāyadiṭṭhi?", f"(क) {q(SJ[0])} {PUTHUJJANA} {D} {called(SJ[0], 'f')}")
L("(Kha) tattha katamā vicikicchā?",
  f"(ख) {q(SJ[1])} {VICIKICCHA_1}। इस प्रकार की जो शंका, शंका करना, शंका से भरा होना, मन का जड़ हो जाना, मन की खरोंच है "
  f"{D} {called(SJ[1], 'm')}")
L("(Ga) tattha katamo sīlabbataparāmāso?",
  f"(ग) {q(SJ[2])} {SILABBATA_Q} {D} {DITTHI_PE} {D} {called(SJ[2], 'f')} {ime('तीन बंधन')}")

T_KAMA, T_BHAVA, T_VIBHAVA = "इंद्रिय-सुखों की तृष्णा", "अस्तित्व की तृष्णा", "अनस्तित्व की तृष्णा"
T_RUPA, T_ARUPA, T_NIRODHA = "सूक्ष्म भौतिक लोक की तृष्णा", "अभौतिक लोक की तृष्णा", "समाप्ति की तृष्णा"
UCCH = f"विनाश की दृष्टि के साथ होने वाला जो {RAGA} है"
KAMADHATU = f"इंद्रिय-सुखों के लोक से जुड़ा जो {RAGA} है"
RUPADHATU = f"सूक्ष्म भौतिक लोक से जुड़ा जो {RAGA} है"
ARUPADHATU = f"अभौतिक लोक से जुड़ा जो {RAGA} है"
L("##### (8) Tisso taṇhā", heads(8, TIKA35))
L("Tattha katamā tisso taṇhā?", f"{kaun('तीन तृष्णाएँ', 'f')} {T_KAMA}, {T_BHAVA}, {T_VIBHAVA}।")
L("Tattha katamā bhavataṇhā?",
  f"{q(T_BHAVA)} अस्तित्व की दृष्टि के साथ होने वाला जो {RAGA} है {D} {called(T_BHAVA, 'f')}")
L("Tattha katamā vibhavataṇhā?", f"{q(T_VIBHAVA)} {UCCH} {D} {called(T_VIBHAVA, 'f')} बाकी तृष्णा इंद्रिय-सुखों की तृष्णा है।")
L("Tattha katamā kāmataṇhā?", f"{q(T_KAMA)} {KAMADHATU} {D} {called(T_KAMA, 'f')}")
L("( ) [(tattha katamā bhavataṇhā)]",
  f"( ) [({q(T_BHAVA)})] सूक्ष्म भौतिक लोक और अभौतिक लोक से जुड़ा जो {RAGA} है {D} {called(T_BHAVA, 'f')}")
L("( ) [(tattha katamā vibhavataṇhā) (?)]",
  f"( ) [({q(T_VIBHAVA)}) (?)] {UCCH} {D} {called(T_VIBHAVA, 'f')} {ime('तीन तृष्णाएँ')}")
L("##### (9) Aparāpi tisso taṇhā", heads(9, TIKA35))
L("Tattha katamā aparāpi tisso taṇhā?", f"{kaun('और भी तीन तृष्णाएँ', 'f')} {T_KAMA}, {T_RUPA}, {T_ARUPA}।")
L("(Ka) tattha katamā kāmataṇhā?", f"(क) {q(T_KAMA)} {KAMADHATU} {D} {called(T_KAMA, 'f')}")
L("(Kha) tattha katamā rūpataṇhā?", f"(ख) {q(T_RUPA)} {RUPADHATU} {D} {called(T_RUPA, 'f')}")
L("(Ga) tattha katamā arūpataṇhā?", f"(ग) {q(T_ARUPA)} {ARUPADHATU} {D} {called(T_ARUPA, 'f')} {ime('तीन तृष्णाएँ')}")
L("##### (10) Aparāpi tisso taṇhā", heads(10, TIKA35))
L("Tattha katamā aparāpi tisso taṇhā?", f"{kaun('और भी तीन तृष्णाएँ', 'f')} {T_RUPA}, {T_ARUPA}, {T_NIRODHA}।")
L("(Ka) tattha katamā rūpataṇhā?", f"(क) {q(T_RUPA)} {RUPADHATU} {D} {called(T_RUPA, 'f')}")
L("(Kha) tattha katamā arūpataṇhā?", f"(ख) {q(T_ARUPA)} {ARUPADHATU} {D} {called(T_ARUPA, 'f')}")
L("(Ga) tattha katamā nirodhataṇhā?", f"(ग) {q(T_NIRODHA)} {UCCH} {D} {called(T_NIRODHA, 'f')} {ime('तीन तृष्णाएँ')}")

ES = ["इंद्रिय-सुखों की खोज", "अस्तित्व की खोज", "पवित्र जीवन की खोज"]
TADEKATTHA = f"और उसके साथ जुड़ा हानिकर शारीरिक कर्म, वाचिक कर्म, मानसिक कर्म"
L("##### (11) Tisso esanā", heads(11, TIKA35))
L("Tattha katamā tisso esanā?", f"{kaun('तीन खोजें', 'f')} {', '.join(ES)}।")
L("(Ka) tattha katamā kāmesanā?", f"(क) {q(ES[0])} {KAMA_PE} {D} {called(ES[0], 'f')}")
L("(Kha) tattha katamā bhavesanā?", f"(ख) {q(ES[1])} {BHAVA_PE} {D} {called(ES[1], 'f')}")
L("(Ga) tattha katamā brahmacariyesanā?",
  f"(ग) {q(ES[2])} {SASSATO_LOKO[0]}, या {D} {SASSATO_LOKO[1]}… या {SASSATO_LOKO[9]}, "
  f"{DITTHI_PE} {D} {called(ES[2], 'f')}")
L("(Ka) tattha katamā kāmesanā,", f"(क) {q(ES[0])} इंद्रिय-सुखों का राग, {TADEKATTHA} {D} {called(ES[0], 'f')}")
L("(Kha) tattha katamā bhavesanā,", f"(ख) {q(ES[1])} अस्तित्व का राग, {TADEKATTHA} {D} {called(ES[1], 'f')}")
L("(Ga) tattha katamā brahmacariyesanā,",
  f"(ग) {q(ES[2])} अतिवादी दृष्टि, {TADEKATTHA} {D} {called(ES[2], 'f')} {ime('तीन खोजें')}")
VIDHA = "स्वयं को आँकने के तीन ढंग"
L("##### (12) Tisso vidhā", heads(12, TIKA35))
L("Tattha katamā tisso vidhā?",
  f"{kaun(VIDHA, 'm')} " + ", ".join(f"“{I_AM[k]}” यह ढंग" for k in ("seyya", "sadisa", "hina")) + f" {D} {ime(VIDHA)}")
BH = ["जन्म का भय", "बुढ़ापे का भय", "मृत्यु का भय"]
BH_SRC = ["जन्म", "बुढ़ापे", "मृत्यु"]
L("##### (13) Tīṇi bhayāni", heads(13, TIKA35))
L("Tattha katamāni tīṇi bhayāni?", f"{kaun('तीन भय', 'm')} {', '.join(BH)}।")
for i in range(3):
    end = (" " + ime("तीन भय")) if i == 2 else ""
    L(f"{PM[i]} tattha katamaṃ",
      f"({MARKS[i]}) {q(BH[i])} {BH_SRC[i]} के कारण जो भय, डर, घबराहट, रोंगटे खड़े होना, मन का दहल जाना है {D} "
      f"{called(BH[i], 'm')}{end}")
TAMA = "शंका करता है, संशय करता है, निश्चय नहीं कर पाता, आश्वस्त नहीं होता"
L("##### (14) Tīṇi tamāni", heads(14, TIKA35))
L("Tattha katamāni tīṇi tamāni?",
  f"{kaun('तीन अंधकार', 'm')} अतीत काल को लेकर {TAMA}, या भविष्य काल को लेकर {TAMA}, या अभी के वर्तमान काल को लेकर {TAMA} "
  f"{D} {ime('तीन अंधकार')}")
SAMANA = "यहाँ कोई श्रमण या ब्राह्मण ऐसा कहने वाला, ऐसी दृष्टि वाला होता है"
SAMANA_PANA = "और यहाँ कोई श्रमण या ब्राह्मण ऐसा कहने वाला, ऐसी दृष्टि वाला होता है"
FEEL = "“यह व्यक्ति जो कुछ भी अनुभव करता है, सुख या दुःख या न दुःख, न सुख, वह सब"
L("##### (15) Tīṇi titthāyatanāni", heads(15, TIKA35))
L("Tattha katamāni tīṇi titthāyatanāni?",
  f"{kaun('मतवादों के तीन आधार', 'm')} {SAMANA} {D} {FEEL} पहले किए गए कर्मों के कारण है”; {SAMANA_PANA} {D} {FEEL} "
  f"ईश्वर की रचना के कारण है”; {SAMANA_PANA} {D} {FEEL} बिना किसी कारण, बिना किसी आधार के है” {D} "
  f"{ime('मतवादों के तीन आधार')}")


L("##### (16) Tayo kiñcanā", heads(16, TIKA35))
L("Tattha katame tayo kiñcanā",
  f"यहाँ तीन बोझ कौन-से हैं [पाठभेद (?): katamāni tīṇi kiñcanāni; dī. ni. 3.305]? राग बोझ है, द्वेष बोझ है, मोह बोझ है {D} "
  f"{ime('तीन बोझ')}")
for n, pali, nm, w, g in [(17, "Tīṇi aṅgaṇāni", "तीन दाग़", "दाग़", "m"), (18, "Tīṇi malāni", "तीन कलुष", "कलुष", "m"),
                          (19, "Tīṇi visamāni", "तीन विषमताएँ", "विषमता", "f")]:
    L(f"##### ({n}) {pali}", heads(n, TIKA35))
    L("Tattha katamāni tīṇi", f"{kaun(nm, g)} राग {w} है, द्वेष {w} है, मोह {w} है {D} {ime(nm)}")
L("##### (20) Aparānipi tīṇi visamāni", heads(20, TIKA35))
L("Tattha katamāni aparānipi tīṇi visamāni?",
  f"{kaun('और भी तीन विषमताएँ', 'f')} शारीरिक विषमता, वाचिक विषमता, मानसिक विषमता {D} {ime('तीन विषमताएँ')}")
L("##### (21) Tayo aggī", heads(21, TIKA35))
L("Tattha katame tayo aggī?", f"{kaun('तीन अग्नियाँ', 'f')} राग की अग्नि, द्वेष की अग्नि, मोह की अग्नि {D} {ime('तीन अग्नियाँ')}")
L("##### (22) Tayo kasāvā", heads(22, TIKA35))
L("Tattha katame tayo kasāvā?",
  f"{kaun('तीन कड़वाहटें', 'f')} राग की कड़वाहट, द्वेष की कड़वाहट, मोह की कड़वाहट {D} {ime('तीन कड़वाहटें')}")
L("##### (23) Aparepi tayo kasāvā", heads(23, TIKA35))
L("Tattha katame aparepi tayo kasāvā?",
  f"{kaun('और भी तीन कड़वाहटें', 'f')} शारीरिक कड़वाहट, वाचिक कड़वाहट, मानसिक कड़वाहट {D} {ime('तीन कड़वाहटें')}")

V3 = ["भोग-स्वाद की दृष्टि", "आत्मा को मानने वाली दृष्टि", "ग़लत दृष्टि"]
L("##### (24. Ka) assādadiṭṭhi", "##### (24. क) " + V3[0])
L("Tattha katamā assādadiṭṭhi?",
  f"{q(V3[0])} {SAMANA} {D} “इंद्रिय-सुखों में कोई दोष नहीं है”। वह इंद्रिय-सुखों में डूब जाता है। {called(V3[0], 'f')}")
L("##### (Kha) attānudiṭṭhi", "##### (ख) " + V3[1])
L("Tattha katamā attānudiṭṭhi?", f"{q(V3[1])} {PUTHUJJANA} {D} {called(V3[1], 'f')}")
L("##### (Ga) micchādiṭṭhi", "##### (ग) " + V3[2])
L("Tattha katamā micchādiṭṭhi?",
  f"{q(V3[2])} {MICCHADITTHI_BODY} {D} {called(V3[2], 'f')} शाश्वतता की दृष्टि भोग-स्वाद की दृष्टि है, स्थायी आत्मा की ग़लत "
  f"दृष्टि आत्मा को मानने वाली दृष्टि है, विनाश की दृष्टि ग़लत दृष्टि है।")
L("##### (25. Ka) arati", "##### (25. क) अरुचि")
L("Tattha katamā arati?", ARATI)
L("##### (Kha) vihesā", "##### (ख) उत्पीड़न")
L("Tattha katamā vihesā?",
  f"{q('उत्पीड़न')} यहाँ कोई व्यक्ति हाथ से, या ढेले से, या डंडे से, या शस्त्र से, या रस्सी से, या किसी और चीज़ से प्राणियों को "
  f"सताता है, इस प्रकार का जो सताना, बहुत सताना, चोट पहुँचाना, बहुत चोट पहुँचाना, चिढ़ाना, बहुत चिढ़ाना, दूसरों को हानि "
  f"पहुँचाना है {D} {called('उत्पीड़न', 'm')}")
ADH = "अनुचित आचरण और विषम आचरण"
L("##### (Ga) adhammacariyā", "##### (ग) अनुचित आचरण")
L("Tattha katamā adhammacariyā?",
  f"{q('अनुचित आचरण')} शरीर से {ADH}, वाणी से {ADH}, मन से {ADH} {D} {called('अनुचित आचरण', 'm')}")
L("##### (26. Ka) dovacassatā", "##### (26. क) सलाह न मानने की प्रवृत्ति")
L("Tattha katamā dovacassatā?", DOVA_L)
L("##### (Kha) pāpamittatā", "##### (ख) बुरे मित्रों की संगति")
L("Tattha katamā pāpamittatā?", papamitta(False, True))
L("##### (Ga) nānattasaññā", "##### (ग) विविधता की पहचान")
L("Tattha katamā nānattasaññā?",
  f"{q('विविधता की पहचान')} {', '.join(KS)} {D} {called('विविधता की पहचान', 'f')} सारी हानिकर पहचान भी विविधता की पहचान है।")
UDDHACCA_L = f"{q('बेचैनी')} {UDDHACCA} {D} {called('बेचैनी', 'f')}"
KOSAJJA_L = f"{q('आलसीपन')} {pamada_core(False)} {D} {called('आलसीपन', 'm')}"
PAMADA_L = f"{q('लापरवाही')} {pamada_core(False)}, {PAMADA_TAIL} {D} {called('लापरवाही', 'f')}"
L("##### (27. Ka) uddhaccaṃ", "##### (27. क) बेचैनी")
L("Tattha katamaṃ uddhaccaṃ?", UDDHACCA_L)
L("##### (Kha) kosajjaṃ", "##### (ख) आलसीपन")
L("Tattha katamaṃ kosajjaṃ?", KOSAJJA_L)
L("##### (Ga) pamādo", "##### (ग) लापरवाही")
L("Tattha katamo pamādo?", PAMADA_L)
L("##### (28. Ka) asantuṭṭhitā", "##### (28. क) असंतोष")
L("Tattha katamā asantuṭṭhitā?", f"{q('असंतोष')} {REQ}, {iccha_para('असंतोष')} {D} {called('असंतोष', 'm')}")
L("##### (Kha) asampajaññatā", "##### (ख) स्पष्ट समझ का अभाव")
L("Tattha katamā asampajaññatā?", ASAMPAJ_L)
L("##### (Ga) mahicchatā", "##### (ग) अत्यधिक इच्छा")
L("Tattha katamā mahicchatā?",
  f"{q('अत्यधिक इच्छा')} {REQ}, {iccha_para('अत्यधिक इच्छा')} {D} {called('अत्यधिक इच्छा', 'f')}")
L("##### (29. Ka) ahirikaṃ", "##### (29. क) निर्लज्जता")
L("Tattha katamaṃ ahirikaṃ?", AHIRIKA_L)
L("##### (Kha) anottappaṃ", "##### (ख) बुराई के प्रति निडरता")
L("Tattha katamaṃ anottappaṃ?", ANOTTAPPA_L)
L("##### (Ga) pamādo", "##### (ग) लापरवाही")
L("Tattha katamo pamādo?", PAMADA_L)
L("##### (30. Ka) anādariyaṃ", "##### (30. क) अनादर")
L("Tattha katamaṃ anādariyaṃ?",
  f"{q('अनादर')} जो अनादर, अनादर का भाव, अगौरव, बात पर कान न देना, उपेक्षा, उपेक्षा करना, उपेक्षा से भरा होना "
  f"[वर्तनी-भेद (Syā.): anādā anādāyanā anādāyitattaṃ], अशिष्टता, सम्मान न करना है {D} {called('अनादर', 'm')}")
L("##### (Kha) dovacassatā", "##### (ख) सलाह न मानने की प्रवृत्ति")
L("Tattha katamā dovacassatā?", DOVA_L)
L("##### (Ga) pāpamittatā", "##### (ग) बुरे मित्रों की संगति")
L("Tattha katamā pāpamittatā?", papamitta(True, True))
L("##### (31. Ka) assaddhiyaṃ", "##### (31. क) श्रद्धा का अभाव")
L("Tattha katamaṃ assaddhiyaṃ?",
  f"{q('श्रद्धा का अभाव')} यहाँ कोई व्यक्ति श्रद्धाहीन होता है, बुद्ध पर, या शिक्षा पर, या संघ पर श्रद्धा नहीं रखता, इस प्रकार का जो "
  f"श्रद्धा का अभाव, श्रद्धा न रखना, भरोसा न करना, मन में प्रसन्नता का अभाव है {D} {called('श्रद्धा का अभाव', 'm')}")
L("##### (Kha) avadaññutā", "##### (ख) उदारता का अभाव")
L("Tattha katamā avadaññutā?",
  f"{q('उदारता का अभाव')} {MACCHARIYA_5} {MACCHARIYA_SYN_A}, {MACCHARIYA_SYN_B} {D} {called('उदारता का अभाव', 'm')}")
L("##### (Ga) kosajjaṃ", "##### (ग) आलसीपन")
L("Tattha katamaṃ kosajjaṃ?", KOSAJJA_L)
L("##### (32. Ka) uddhaccaṃ", "##### (32. क) बेचैनी")
L("Tattha katamaṃ uddhaccaṃ?", UDDHACCA_L)
L("##### (Kha) asaṃvaro", "##### (ख) असंयम")
L("Tattha katamo asaṃvaro?", f"{q('असंयम')} {INDRIYA_AGUTTA} {D} {called('असंयम', 'm')}")
L("##### (Ga) dussīlyaṃ", "##### (ग) दुराचार")
L("Tattha katamaṃ dussīlyaṃ?", f"{q('दुराचार')} {VITIKKAMA} {D} {called('दुराचार', 'm')}")
AD = "आर्यों के दर्शन न करने की इच्छा"
L("##### (33. Ka) ariyānaṃ adassanakamyatā", "##### (33. क) " + AD)
L("Tattha katamā ariyānaṃ adassanakamyatā?",
  f"{q(AD)} {kaun('आर्य', 'm').replace('कौन-से', 'कौन')} बुद्ध और बुद्ध के शिष्य आर्य कहे जाते हैं। इन आर्यों के जो दर्शन न करने की "
  f"इच्छा, उन्हें न देखने की इच्छा, उनसे न मिलने की इच्छा, उनके साथ न जुड़ने की इच्छा है {D} {called(AD, 'f')}")
SDN = "सच्ची शिक्षा को न सुनने की इच्छा"
L("##### (Kha) saddhammaṃ asotukamyatā", "##### (ख) " + SDN)
L("Tattha katamā saddhammaṃ asotukamyatā?",
  f"{q(SDN)} {q('सच्ची शिक्षा')} सजगता के चार आधार, चार सही प्रयत्न, सिद्धि के चार आधार, पाँच क्षमताएँ, पाँच बल, "
  f"जागृति के सात अंग, आठ अंगों वाला आर्य मार्ग {D} {called('सच्ची शिक्षा', 'f')} इस सच्ची शिक्षा को जो न सुनने की इच्छा, "
  f"उस पर कान न देने की इच्छा, उसे ग्रहण न करने की इच्छा, उसे धारण न करने की इच्छा है {D} {called(SDN, 'f')}")
UPA = "दोष ढूँढने वाला मन"
L("##### (Ga) upārambhacittatā", "##### (ग) " + UPA)
L("Tattha katamā upārambhacittatā?",
  f"{q(UPA)} {q('दोष ढूँढना')} जो दोष ढूँढना, बार-बार दोष ढूँढना, दोष निकालना, बार-बार दोष निकालना, दोष निकालने से भरा होना, "
  f"तुच्छ समझना, तिरस्कार, अपमान, छिद्र खोजना है {D} {called(UPA, 'm')}")
L("##### (34. Ka) muṭṭhassaccaṃ", "##### (34. क) सजगता की कमी")
L("Tattha katamaṃ muṭṭhassaccaṃ?", MUTTHA_L)
L("##### (Kha) asampajaññaṃ", "##### (ख) स्पष्ट समझ का अभाव")
L("Tattha katamaṃ asampajaññaṃ?", ASAMPAJ_L)
L("##### (Ga) cetaso vikkhepo", "##### (ग) मन का भटकाव")
L("Tattha katamo cetaso vikkhepo?", f"{q('मन का भटकाव')} {UDDHACCA} {D} {called('मन का भटकाव', 'm')}")
AYO = "अनुचित मनोयोग"
L("##### (35. Ka) ayoniso manasikāro", "##### (35. क) " + AYO)
L("Tattha katamo ayoniso manasikāro?",
  f"{q(AYO)} अनित्य में “नित्य” मानकर {AYO}, दुःख में “सुख” मानकर {AYO}, अनात्म में “आत्मा” मानकर {AYO}, अशुभ में "
  f"“शुभ” मानकर {AYO}, या सत्य के विपरीत ढंग से मन का मुड़ना, बार-बार मुड़ना, ध्यान देना, ध्यान में लाना, मनोयोग "
  f"{D} {called(AYO, 'm')}")
KUM = "कुमार्ग की संगति"
L("##### (Kha) kummaggasevanā", "##### (ख) " + KUM)
L("Tattha katamā kummaggasevanā?",
  f"{q(KUM)} {q('कुमार्ग')} {', '.join(MICCHATTA_10[:8])} {D} {called('कुमार्ग', 'm')} इस कुमार्ग की जो "
  f"{sevana(False, True).replace('उनकी ओर', 'उसकी ओर')} है {D} {called(KUM, 'f')}")
L("##### (Ga) cetaso ca līnattaṃ", "##### (ग) मन की शिथिलता")
L("Tattha katamaṃ cetaso ca līnattaṃ?", LINATTA)
L("Tikaṃ.", "तीन-तीन प्रकार।")
