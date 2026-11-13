"""Template table for build_2-01_2-03_hi.py (pi-7 files 2-01, 2-02, 2-03).

Each line: <normalised Pāli> ⇒ <Hindi template>
Normalised Pāli: triad items -> @<ending> (@aṃ, @o, @ā, @assa, @ānaṃ, @ena, @e, @āya, @āni, @a ...),
a 'ca' group of items is one slot; conditions -> %A (…paccayā), %N (na…paccayā), %I (…paccayena paccayo),
%P (…paccayo), %NP (na…paccayo). First letter lower-cased.
Hindi slots: {n} = n-th slot; item forms {n:dh} OBJ, {n:dhs} RES, {n:dat}, {n:f}/{n:m}/{n:mo} adjective,
{n:upp} "उत्पन्न होती है/हैं", {n:hoti} "होती है/हैं".
"""
import build_sample_hi as S

VARIANT_KIND = {"nānākhaṇikā": "वर्तनी-भेद"}

# ---------------------------------------------------------------- headings
HEADINGS = {
    "(Dutiyo bhāgo)": S.BHAGA[2],
    "Dhammānulome": S.DHAMMANULOMA,
    "Tikapaṭṭhānaṃ": S.TIKAPATTHANA,
    "Vitakkattikaṃ": S.TIKA("आरंभिक विचार"),
    "Pītittikaṃ": S.TIKA("उल्लास"),
    "Dassanenapahātabbattikaṃ": S.TIKA("सत्य-दर्शन से छोड़ी जाने वाली परिघटनाओं"),
    "Paṭiccavāro": S.VARA["paṭicca"], "Sahajātavāro": S.VARA["sahajāta"], "Paccayavāro": S.VARA["paccaya"],
    "Nissayavāro": S.VARA["nissaya"], "Saṃsaṭṭhavāro": S.VARA["saṃsaṭṭha"],
    "Sampayuttavāro": S.VARA["sampayutta"], "Pañhāvāro": S.VARA["pañhā"], "Vibhaṅgavāro": S.VARA["vibhaṅga"],
    "Saṅkhyāvāro": S.VARA["saṅkhyā"],
    "Paccayānulomaṃ": S.PACCAYANULOMA, "Paccayapaccanīyaṃ": S.PACCAYAPACCANIYA,
    "Paccayānulomapaccanīyaṃ": S.PACCAYANULOMAPACCANIYA, "Paccayapaccanīyānulomaṃ": S.PACCAYAPACCANIYANULOMA,
    "Paccayānulomādi": S.PACCAYANULOMA + " आदि",
    "1-4. Paccayānulomādi": "1-4. " + S.PACCAYANULOMA + " आदि",
    "2-6. Sahajāta-paccaya-nissaya-saṃsaṭṭha-sampayuttavāro":
        "2-6. सह-उत्पत्ति, कारण, आश्रय, घुले-मिले होने और जुड़ाव के खंड",
    "Suddhaṃ": S.SUDDHA, "Dukaṃ": S.GROUP_HI(2),
    "Hetudukaṃ": S.DUKANI("hetu"), "Nahetudukaṃ": S.DUKANI("hetu", neg=True),
    "Paccanīyuddhāro": "नकारात्मक क्रम के लिए उद्धरण",
    "Anantara-samanantarapaccayā": f"{S.NAME('anantara')} और {S.NAME('samanantara')}",
    "Aññamañña-nissayapaccayā": f"{S.NAME('aññamañña')} और {S.NAME('nissaya')}",
    "Atthi-avigatapaccayā": f"{S.NAME('atthi')} और {S.NAME('avigata')}",
    "Natthivigatāvigatapaccayā": f"{S.NAME('natthi')}, {S.NAME('vigata')} और {S.NAME('avigata')}",
    "Naadhipati-naāsevanapaccayā": f"{S.NNAME('adhipati')} और {S.NNAME('āsevana')}",
    "Nonatthi-novigatapaccayā": f"{S.NNAME('natthi')} और {S.NNAME('vigata')}",
}
for _k in S.COND_KEYS:
    _cap = _k[0].upper() + _k[1:]
    _neg = "No" if _k in ("atthi", "natthi", "vigata", "avigata") else "Na"
    HEADINGS[f"{_cap}paccayo"] = S.NAME(_k)
    HEADINGS[f"{_cap}paccayādi"] = S.NAME(_k) + " आदि"
    HEADINGS[f"{_neg}{_k}paccayo"] = S.NNAME(_k)
    HEADINGS[f"{_neg}{_k}paccayādi"] = S.NNAME(_k) + " आदि"

_SAD = {k: S.SADISA(k) for k in S.COND_KEYS}
_NSAD = {k: S.SADISA(k, neg=True) for k in S.COND_KEYS}
_KT = "हितकर वाले तीन के वर्गीकरण"   # kusalattike (locative)
_BN = "बनाने चाहिए"
_BNA = "बनाना चाहिए"
_VT = "का विस्तार करना चाहिए"

TEMPLATES = rf"""
# ---------------------------------------------------------------- frames
@aṃ dhammaṃ paṭicca @o dhammo uppajjati %A ⇒ {{1:dh}} पर निर्भर होकर {{2:dhs}} {{3}} {{2:upp}}
@aṃ dhammaṃ paṭicca @o dhammā uppajjanti %A ⇒ {{1:dh}} पर निर्भर होकर {{2:dhs}} {{3}} {{2:upp}}
@aṃ dhammaṃ paṭicca @o dhammo uppajjati %N ⇒ {{1:dh}} पर निर्भर होकर {{2:dhs}} {{3}} {{2:upp}}
@aṃ dhammaṃ paṭicca @o dhammā uppajjanti %N ⇒ {{1:dh}} पर निर्भर होकर {{2:dhs}} {{3}} {{2:upp}}
@o dhammo @assa dhammassa %I ⇒ {{1:dhs}}, {{2:dat}} {{3}} {{1:hoti}}
@o dhammā @assa dhammassa %I ⇒ {{1:dhs}}, {{2:dat}} {{3}} {{1:hoti}}
@o dhammā @assa %I ⇒ {{1:dhs}}, {{2:dat}} {{3}} {{1:hoti}}
@o dhammo @assa dhammassa ⇒ {{1:dhs}}, {{2:dat}}
@o dhammā @assa dhammassa ⇒ {{1:dhs}}, {{2:dat}}
@o dhammo @assa ⇒ {{1:dhs}}, {{2:dat}}
@o dhammā @assa ⇒ {{1:dhs}}, {{2:dat}}
@o ⇒ {{1:dhs}}
@aṃ ⇒ {{1:dh}}
%P ⇒ {{1}}

# ---------------------------------------------------------------- labels and short words
saṃkhittaṃ ⇒ संक्षिप्त
satta ⇒ सात
pañca ⇒ पाँच
tīṇi ⇒ तीन
ekaṃ ⇒ एक
anulomaṃ ⇒ {S.ANULOMA}
paccanīyaṃ ⇒ {S.PACCANIYA}
anulomapaccanīyaṃ ⇒ {S.ANULOMAPACCANIYA}
paccanīyānulomaṃ ⇒ {S.PACCANIYANULOMA}
paccanīye ⇒ {S.PACCANIYA} में
paṭiccavāro ⇒ {S.VARA["paṭicca"]}
paccayavāro ⇒ {S.VARA["paccaya"]}
saṃsaṭṭhavāro ⇒ {S.VARA["saṃsaṭṭha"]}
paccanīyuddhāro ⇒ नकारात्मक क्रम के लिए उद्धरण
sahajātaṃ ⇒ सह-उत्पत्ति
sahajātā ⇒ सह-उत्पत्ति
sahajāto ⇒ सह-उत्पत्ति
purejātaṃ ⇒ पूर्व-उत्पत्ति
pacchājātaṃ ⇒ पश्चात्-उत्पत्ति
pacchājātā ⇒ पश्चात्-उत्पत्ति
āhāraṃ ⇒ आहार
indriyaṃ ⇒ क्षमता
nānākkhaṇikā ⇒ भिन्न-क्षणिक
paripuṇṇaṃ ⇒ पूरा
paṭisandhi natthi ⇒ पुनर्जन्म नहीं है
paṭisandhikkhaṇe natthi ⇒ पुनर्जन्म के क्षण में नहीं है
vipākapaṭisandhi natthi ⇒ कर्म-फल और पुनर्जन्म नहीं है
moho natthi ⇒ मोह नहीं है
ārammaṇasadisaṃ ⇒ {_SAD["ārammaṇa"]}
hetupaccayasadisaṃ ⇒ {_SAD["hetu"]}
naārammaṇasadisaṃ ⇒ {_NSAD["ārammaṇa"]}
naadhipatipaccayasadisaṃ ⇒ {_NSAD["adhipati"]}
kammapaccayasadisaṃ ⇒ {_SAD["kamma"]}
ārammaṇapaccayasadisaṃ ⇒ {_SAD["ārammaṇa"]}
sahajātapaccayasadisaṃ ⇒ {_SAD["sahajāta"]}
sahajātasadisaṃ ⇒ {_SAD["sahajāta"]}
anantarasadisaṃ ⇒ {_SAD["anantara"]}
anantarapaccayasadisaṃ ⇒ {_SAD["anantara"]}
paripuṇṇaṃ hetupaccayasadisaṃ ⇒ पूरा, {_SAD["hetu"]}
kusalattike vippayuttapaccayasadisaṃ ⇒ {_KT} में {_SAD["vippayutta"]}
%N nahetupaccayasadisaṃ ⇒ {{1}} {_NSAD["hetu"]}
%N paripuṇṇaṃ arūpapañhameva ⇒ {{1}} पूरा, केवल अभौतिक लोक वाला प्रश्न ही
paṭiccavārasadisā ⇒ निर्भरता के खंड के समान
avasesā hetupaccayasadisā ⇒ बाकी {_SAD["hetu"]} हैं
avasesā sahajātapaccayasadisā ⇒ बाकी {_SAD["sahajāta"]} हैं

# ---------------------------------------------------------------- counting notes
evaṃ gaṇetabbaṃ ⇒ इसी तरह गिनना चाहिए
evaṃ anumajjantena gaṇetabbaṃ ⇒ इसी तरह अनुसरण करते हुए गिनना चाहिए
evaṃ anulomagaṇanā gaṇetabbā ⇒ इसी तरह सकारात्मक क्रम की गणना करनी चाहिए
yathā kusalattike gaṇanā, evaṃ gaṇetabbaṃ ⇒ जैसे {_KT} में गणना है, वैसे ही गिनना चाहिए
yathā kusalattike paccanīyagaṇanā, evaṃ gaṇetabbaṃ ⇒ जैसे {_KT} में नकारात्मक क्रम की गणना है, वैसे ही गिनना चाहिए
yathā kusalattike anulomapaccanīyagaṇanā, evaṃ gaṇetabbaṃ ⇒ जैसे {_KT} में सकारात्मक-नकारात्मक क्रम की गणना है, वैसे ही गिनना चाहिए
yathā kusalattike paccanīyānulomagaṇanā, evaṃ gaṇetabbaṃ ⇒ जैसे {_KT} में नकारात्मक-सकारात्मक क्रम की गणना है, वैसे ही गिनना चाहिए
yathā paṭiccagaṇanā evaṃ gaṇetabbā ⇒ जैसे निर्भरता के खंड की गणना है, वैसे ही गिनना चाहिए
adhipatiyā sattatiṃsa, purejāte ca āsevane ca ekavīsa, ayaṃ ettha viseso ⇒ {S.LOC("adhipati")} सैंतीस, {S.LOC("purejāta")} और {S.LOC("āsevana")} इक्कीस, यहाँ यही अंतर है
nahetuyā tettiṃsa pañhā, sattasu ṭhānesu satta mohā uddharitabbā mūlapadesuyeva ⇒ {S.NLOC("hetu")} तैंतीस प्रश्न, सात स्थानों पर, मूल पदों में ही, सात मोह उद्धृत करने चाहिए
naārammaṇe satta cittasamuṭṭhānā uddharitabbā ⇒ {S.NLOC("ārammaṇa")} मन से उत्पन्न सात भौतिक रूप उद्धृत करने चाहिए
kusalattikaṃ anulomaṃ anumajjantena gaṇetabbaṃ ⇒ हितकर वाले तीन के वर्गीकरण के सकारात्मक क्रम का अनुसरण करते हुए गिनना चाहिए
paccanīyaṃ anumajjantena gaṇetabbaṃ ⇒ नकारात्मक क्रम को अनुसरण करते हुए गिनना चाहिए
anulomapaccanīyaṃ anumajjantena gaṇetabbaṃ ⇒ सकारात्मक-नकारात्मक क्रम को अनुसरण करते हुए गिनना चाहिए
paccanīyānulomaṃ anumajjantena gaṇetabbaṃ ⇒ नकारात्मक-सकारात्मक क्रम को अनुसरण करते हुए गिनना चाहिए
paccanīyaṃ paripuṇṇaṃ kātabbaṃ ⇒ नकारात्मक क्रम पूरा करना चाहिए
anulomapaccanīyaṃ vitthārena gaṇetabbaṃ ⇒ सकारात्मक-नकारात्मक क्रम को विस्तार से गिनना चाहिए
imāni padāni anumajjantena anulomaṃ gaṇetabbaṃ ⇒ इन पदों का अनुसरण करते हुए सकारात्मक क्रम गिनना चाहिए
paccanīyaṃ gaṇentena imāni padāni anumajjantena gaṇetabbāni ⇒ नकारात्मक क्रम गिनते हुए इन पदों का अनुसरण करते हुए इन्हें गिनना चाहिए
anulomapaccanīyagaṇanā iminā kāraṇena gaṇetabbā ⇒ सकारात्मक-नकारात्मक क्रम की गणना इसी तरीके से करनी चाहिए
paccanīyānulomaṃ iminā kāraṇena vibhajitabbaṃ ⇒ नकारात्मक-सकारात्मक क्रम का इसी तरीके से विश्लेषण करना चाहिए
pañhāvāragaṇanaṃ evaṃ asammohantena gaṇetabbaṃ ⇒ प्रश्नों के खंड की गणना इसी तरह बिना भ्रमित हुए करनी चाहिए
ghaṭanā kusalattikasadisāyeva ⇒ संयोजन {_KT} के समान ही हैं
ñatvā gaṇetabbaṃ ⇒ जानकर गिनना चाहिए
nahetuyā tettiṃsa pañhā ⇒ {S.NLOC("hetu")} तैंतीस प्रश्न

# ---------------------------------------------------------------- method notes
dve paccayā sajjhāyamaggena vibhattā, evaṃ avasesā vīsatipaccayā vibhajitabbā ⇒ दो कारणों का पाठ करने के क्रम से विश्लेषण किया गया है, इसी तरह बाकी बीस कारणों का विश्लेषण करना चाहिए
napurejātamūlake yathā suddhikaṃ arūpaṃ, tathā arūpā kātabbā ⇒ {S.MULAKA("purejāta", neg=True)} में, जैसे अकेले कारण वाले खंड में अभौतिक लोक है, वैसे ही अभौतिक लोक वाले प्रश्न {_BN}
naāsevanamūlake @aṃ vipākena saha gacchantena napurejātasadisaṃ kātabbaṃ, @aṃ avitakkavicāramattagacchantena vipāko dassetabbo ⇒ {S.MULAKA("āsevana", neg=True)} में {{1:dh}} को कर्म-फल के साथ लेते हुए {_NSAD["purejāta"]} {_BNA}, और {{2:dh}} के साथ {{2:dh}} को लेते हुए कर्म-फल दिखाना चाहिए
sahajātavāropi paṭiccavārasadiso kātabbo ⇒ {S.VARA["sahajāta"]} भी निर्भरता के खंड के समान {_BNA}
sahajātavāro paṭiccavārasadiso ⇒ {S.VARA["sahajāta"]} निर्भरता के खंड के समान है
paṭhamaudāharaṇe pavatte paṭisandhikkhaṇe satta pañhā kātabbā ⇒ पहले उदाहरण में जीवन के प्रवाह में और पुनर्जन्म के क्षण में सात प्रश्न {_BN}
evaṃ paṭisandhikkhaṇe cattāro ⇒ इसी तरह पुनर्जन्म के क्षण में चार
avasesesu dvīsu ghaṭanesu pavatti paṭisandhi vitthāretabbā ⇒ बाकी दो संयोजनों में जीवन के प्रवाह और पुनर्जन्म {_VT}
hetupaccayaṃ anumajjantena paccayavāro vitthāretabbo ⇒ मूल-कारण का अनुसरण करते हुए कारण के खंड {_VT}
hetupaccayaṃ anumajjantena sabbe paccayā vitthāretabbā ⇒ मूल-कारण का अनुसरण करते हुए सभी कारणों {_VT}
@amūlakā satta pañhā naadhipatiyā kātabbā ⇒ {{1:f}} परिघटना से शुरू होने वाले सात प्रश्न {S.NLOC("adhipati")} {_BN}
yathā paṭiccanaye tathā pañca pañhā kātabbā ⇒ जैसे निर्भरता की विधि में, वैसे ही पाँच प्रश्न {_BN}
paṭhamaghaṭanāyaṃ sampuṇṇā satta pañhā kātabbā ⇒ पहले संयोजन में पूरे सात प्रश्न {_BN}
paṭisandhikkhaṇe pañca pañhā kātabbā ⇒ पुनर्जन्म के क्षण में पाँच प्रश्न {_BN}
yattha @aṃ āgacchati tattha vipākaṃ kātabbaṃ ⇒ जहाँ {{1:dh}} आती है, वहाँ कर्म-फल {_BNA}
naadhipatimūlake sattatiṃsa pañhā kātabbā ⇒ {S.MULAKA("adhipati", neg=True)} में सैंतीस प्रश्न {_BN}
naanantarampi ⇒ {S.NLOC("anantara")} भी
nasamanantarampi naaññamaññampi naupanissayampi satta pañhā rūpaṃyeva ⇒ {S.NLOC("samanantara")} भी, {S.NLOC("aññamañña")} भी, {S.NLOC("upanissaya")} भी सात प्रश्न हैं, केवल भौतिक रूप ही
napurejāte sattatiṃsa paṭiccavārapaccanīyasadisaṃ ⇒ {S.NLOC("purejāta")} सैंतीस, निर्भरता के खंड के नकारात्मक क्रम के समान
napacchājāte sattatiṃsa, naāsevanepi sadisaṃ ⇒ {S.NLOC("pacchājāta")} सैंतीस, {S.NLOC("āsevana")} भी समान
yattha @opi āgacchati, tattha vipākā kātabbā ⇒ जहाँ {{1:dh}} भी आती है, वहाँ कर्म-फल {_BN}
paripuṇṇaṃ kātabbaṃ ⇒ पूरा {_BNA}
navipāke sattatiṃsa pañhā kātabbā ⇒ {S.NLOC("vipāka")} सैंतीस प्रश्न {_BN}
naāhāra-naindriya-najhāna-namagga-nasampayuttanavippayutta-nonatthi-%N vitthāretabbā ⇒ {S.NNAME_OBL("āhāra")}, {S.NNAME_OBL("indriya")}, {S.NNAME_OBL("jhāna")}, {S.NNAME_OBL("magga")}, {S.NNAME_OBL("sampayutta")}, {S.NNAME_OBL("vippayutta")}, {S.NNAME_OBL("natthi")} और {S.NNAME_OBL("vigata")} {_VT}
nissayampi ninnānaṃ ⇒ आश्रय का खंड भी अलग नहीं है
paccanīyaṃ kātabbaṃ asammohantena ⇒ बिना भ्रमित हुए नकारात्मक क्रम {_BNA}
sampayuttavāropi vitthāretabbo ⇒ {S.VARA["sampayutta"]} का भी विस्तार करना चाहिए

# ---------------------------------------------------------------- pañhāvāra pieces
cetopariyañāṇena @acittasamaṅgissa cittaṃ jānāti ⇒ {S.CETOPARIYENA} {{1:mo}} मन से युक्त व्यक्ति के मन को जानता है
cetopariyañāṇena @acittasamaṅgissa cittaṃ jānanti ⇒ {S.CETOPARIYENA} {{1:mo}} मन से युक्त व्यक्ति के मन को जानते हैं
cetopariyañāṇena pītisahagatasukhasahagatacittasamaṅgissa cittaṃ jānāti ⇒ {S.CETOPARIYENA} उल्लास के साथ होने वाले और सुख के साथ होने वाले मन से युक्त व्यक्ति के मन को जानता है
dānaṃ datvā sīlaṃ samādiyitvā ⇒ दान देकर, सदाचार ग्रहण करके
uposathakammaṃ katvā taṃ garuṃ katvā paccavekkhati ⇒ उपवास-व्रत का पालन करके उसे महत्व देकर उस पर {S.REVIEW_SG}
@o dhammā @assa dhammassa sahajātaṃ ⇒ {{1:dhs}}, {{2:dat}} सह-उत्पत्ति
@amūlakā sattapi pañhā paripuṇṇā ⇒ {{1:f}} परिघटना से शुरू होने वाले सातों प्रश्न पूरे हैं
@amūlakā pañca pañhā kātabbā ⇒ {{1:f}} परिघटना से शुरू होने वाले पाँच प्रश्न {_BN}
@amūlakā pañca pañhā ⇒ {{1:f}} परिघटना से शुरू होने वाले पाँच प्रश्न
vipākanti niyāmetabbā ⇒ “कर्म-फल” कहकर निर्धारित करने चाहिए
@amūlakā iminā kāraṇena satta pañhā vibhajitabbā ⇒ {{1:f}} परिघटना से शुरू होने वाले सात प्रश्नों का इसी तरीके से विश्लेषण करना चाहिए
@amūlakā satta pañhā iminā kāraṇena vibhajitabbā ⇒ {{1:f}} परिघटना से शुरू होने वाले सात प्रश्नों का इसी तरीके से विश्लेषण करना चाहिए
@amūlakā pañca pañhā iminā kāraṇena vibhajitabbā ⇒ {{1:f}} परिघटना से शुरू होने वाले पाँच प्रश्नों का इसी तरीके से विश्लेषण करना चाहिए
@amūlake avasesā pañhā sahajātapaccayasadisā ⇒ {{1:f}} परिघटना से शुरू होने वाली शृंखला में बाकी प्रश्न {_SAD["sahajāta"]} हैं
natthipaccayañca vigatapaccayañca anantarasadisaṃ, avigataṃ atthisadisaṃ ⇒ {S.NAME("natthi")} और {S.NAME("vigata")} {_SAD["anantara"]} हैं, {S.NAME("avigata")} {_SAD["atthi"]} है
anantarapaccayopi samanantarapaccayopi sadiso ⇒ {S.NAME("anantara")} भी और {S.NAME("samanantara")} भी समान हैं
pavattipi, paṭisandhipi dīpetabbā ⇒ जीवन का प्रवाह भी, पुनर्जन्म भी दिखाना चाहिए
paṭisandhikāni cattāri ⇒ पुनर्जन्म वाले चार
dve vārā vitthāretabbā ⇒ दो खंडों {_VT}
purejāte paṭisandhikkhaṇe natthi ⇒ {S.LOC("purejāta")} पुनर्जन्म के क्षण में नहीं है
āsevane vipākaṃ natthi ⇒ {S.LOC("āsevana")} {S.NAME("vipāka")} नहीं है
āhāra ⇒ {S.ABL("āhāra")}
indriya ⇒ {S.ABL("indriya")}
jhāna ⇒ {S.ABL("jhāna")}
magga ⇒ {S.ABL("magga")}
sampayutta ⇒ {S.ABL("sampayutta")}
vippayutta ⇒ {S.ABL("vippayutta")}
atthi ⇒ {S.ABL("atthi")}
natthi ⇒ {S.ABL("natthi")}
vigata ⇒ {S.ABL("vigata")}
utusamuṭṭhāna ⇒ {S.UTUSAM}
utusamuṭṭhānaṃ ⇒ {S.UTUSAM}
āhārasamuṭṭhānaṃ ⇒ {S.AHARASAM}
bāhiraṃ ⇒ {S.BAHIRA}
naadhipatipaṭisandhikkhaṇe paripuṇṇaṃ ⇒ {S.NLOC("adhipati")} पुनर्जन्म के क्षण में पूरा
"arūpe"ti niyāmetabbaṃ "paṭisandhikkhaṇe"ti ca ⇒ “{S.ARUPE}” और “{S.PATISANDHI}” कहकर निर्धारित करना चाहिए
iminā kāraṇena dasa pañhā vitthāretabbā ⇒ इसी तरीके से दस प्रश्नों {_VT}
sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi paṭiccavārasadisā ⇒ {S.VARA["sahajāta"]} भी, {S.VARA["paccaya"]} भी, {S.VARA["nissaya"]} भी, {S.VARA["saṃsaṭṭha"]} भी और {S.VARA["sampayutta"]} भी निर्भरता के खंड के समान हैं
sukhamūle tīṇi ⇒ सुख के साथ होने वाली परिघटना से शुरू होने वाली शृंखला में तीन
iminā kāraṇena sabbesaṃ padānaṃ paccayoti dīpetabbo ⇒ इसी तरीके से सभी पदों के लिए “कारण” दिखाना चाहिए
tāniyeva ca gamanāni niyāmetabbāni ⇒ और वही क्रम निर्धारित करने चाहिए
paṭiccasadisaṃ sahajāte dasa pañhā ⇒ निर्भरता के खंड के समान, {S.LOC("sahajāta")} दस प्रश्न
dasa pañhā kātabbā ⇒ दस प्रश्न {_BN}
pītinayaṃ passitvā kātabbaṃ ⇒ उल्लास वाली विधि को देखकर {_BNA}
cattāripi gaṇanāni passitvā kātabbāni ⇒ चारों गणनाओं को देखकर {_BN}
cattāri kātabbāni, @aṃ anumajjantena vibhajitabbaṃ ⇒ चार {_BN}, {{1:dh}} का अनुसरण करते हुए विश्लेषण करना चाहिए
yathā paṭiccavāre hetupaccaye evaṃ vitthāretabbā dasa pañhā ⇒ जैसे निर्भरता के खंड में {S.NAME("hetu")} में, वैसे ही दस प्रश्नों {_VT}
dasa pañhā vitthāretabbā ⇒ दस प्रश्नों {_VT}
natthipi vigatampi anantarasadisaṃ ⇒ {S.NAME("natthi")} भी और {S.NAME("vigata")} भी {_SAD["anantara"]} हैं
purimā purimā @ā khandhā pacchimānaṃ pacchimānaṃ @ānaṃ %I ⇒ पहले-पहले के, {{1:mo}} समूह बाद-बाद के, उल्लास के साथ होने वालों और सुख के साथ होने वालों के लिए {{3}} होते हैं
@aṃ dhammaṃ paṭicca @o ⇒ {{1:dh}} पर निर्भर होकर {{2:dhs}}
@aṃ dhammaṃ paṭicca nevadassanena nabhāvanāya ⇒ {{1:dh}} पर निर्भर होकर न सत्य-दर्शन से, न मानसिक अभ्यास से
@aṃ dhammaṃ paccayā bhāvanāya ⇒ {{1:dh}} के कारण मानसिक अभ्यास से
@aṃ dhammaṃ paccayā nevadassanena ⇒ {{1:dh}} के कारण न सत्य-दर्शन से
nevadassanena nabhāvanāya pahātabbaṃ dhammaṃ paccayā nevadassanena ⇒ न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़ी जाने वाली परिघटना के कारण न सत्य-दर्शन से
nevadassanena nabhāvanāya ⇒ न सत्य-दर्शन से, न मानसिक अभ्यास से
ahetukaṃ @aṃ ⇒ {S.AHETUKA}, {{1:f}}
ahetukaṃ ⇒ {S.AHETUKA}
pañcaviññāṇaṃ ⇒ पाँच प्रकार की चेतना
asaññasattānaṃ ekaṃ ⇒ {S.ASANNASATTA} एक
paṭisandhi natthi, vipākañca ⇒ पुनर्जन्म नहीं है, और कर्म-फल भी नहीं
ajjhattikā ca asaññasattānañca mahābhūtā ⇒ आंतरिक महाभूत और पहचान-रहित प्राणियों के महाभूत
ajjhattikā mahābhūtā ca āhārasamuṭṭhānañca ⇒ आंतरिक महाभूत और आहार से उत्पन्न भौतिक रूप
jhāne parihīne vippaṭisārissa @aṃ domanassaṃ uppajjati ⇒ ध्यान के छूट जाने पर ग्लानि से भरे व्यक्ति में {{1:f}} उदासी उत्पन्न होती है
pubbe ⇒ पहले
kāyikaṃ ⇒ शारीरिक
sukhaṃ ⇒ सुख
kabaḷīkāro ⇒ कौर-कौर खाया जाने वाला भोजन
satta pañhā ⇒ सात प्रश्न
satta pañhā %I ⇒ सात प्रश्न, {{1}} होती है
idampi dassanena sadisaṃ ⇒ यह भी सत्य-दर्शन से छोड़ी जाने वाली परिघटना के समान है
dassanena sadisaṃ kātabbaṃ ⇒ सत्य-दर्शन से छोड़ी जाने वाली परिघटना के समान {_BNA}
dve pañhā kātabbā ⇒ दो प्रश्न {_BN}
nissayavāro paccayasadiso kātabbo ⇒ {S.VARA["nissaya"]} कारण के खंड के समान {_BNA}
sabbāni padāni vitthāretabbāni tīṇi, tīṇi ⇒ सभी पदों {_VT}, तीन, तीन
sampayuttavāro saṃsaṭṭhavārasadiso ⇒ {S.VARA["sampayutta"]} घुले-मिले होने के खंड के समान है
vitakkattikaṃ niṭṭhitaṃ ⇒ “{S.TIKA("आरंभिक विचार")}” समाप्त
pītittikaṃ niṭṭhitaṃ ⇒ “{S.TIKA("उल्लास")}” समाप्त
dassanenapahātabbattikaṃ niṭṭhitaṃ ⇒ “{S.TIKA("सत्य-दर्शन से छोड़ी जाने वाली परिघटनाओं")}” समाप्त
"""
