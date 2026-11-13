# 2-10 Micchattaniyatattika: hand lines (exec'd by build_rails_2-09_2-17.py)
mi, sa, an = "mi", "sa", "an"


def UD(x, y, keys, g="fs"):
    return f"{x}, {y} " + "… ".join(I(k, g) for k in keys)


def AH(c, post="o"):
    return f"मूल से रहित, {J(c, post)} एक समूह"


ADH = {c: f"{J(c)} प्रधानता" for c in ADJ}
SAHA = LAB["ādh_s"]
ARAM = LAB["ādh_ā"]
CRIME4 = "माता की हत्या के कर्म के लिए… पिता की हत्या के कर्म के लिए… अर्हत् की हत्या के कर्म के लिए… बुद्ध का खून बहाने के कर्म के लिए"
GIFT3 = "दान देता है, सदाचार ग्रहण करता है, उपवास-व्रत का पालन करता है"

L = [
    # ^7-16-1
    PT(D(mi), D(mi), "hetu") + f" – {ONE(mi)} {B1} तीन समूह… दो समूह। (1)",
    PT(D(mi), D(an), "hetu") + f" – {KH(mi)} {B1} {RC}। (2)",
    PT(D(mi), DP(mi, an), "hetu") + f" – {ONE(mi)} {B1} तीन समूह और {RC}… दो समूहों…। (3)",
    PT(D(sa), D(sa), "hetu") + "… तीन।",
    PT(D(an), D(an), "hetu") + f" – {ONE(an)} {B1} तीन समूह और {RC}… दो समूहों… {PK} {ONE(an)} {B1} तीन समूह और {RK}, दो समूहों… {KV}; एक महाभूत {B1} तीन महाभूत… दो महाभूत। महाभूतों {B1} {RCKU}। (1)",
    PT(D2(mi, an), D(an), "hetu") + f" – {KH(mi)} और महाभूतों {B1} {RC}। (1)",
    PT(D2(sa, an), D(an), "hetu") + f" – {KH(sa)} और महाभूतों {B1} {RC}। (1)",
    # ^7-16-5
    PT(D(mi), D(mi), "ārammaṇa") + f" – {ONE(mi)} {B1} तीन समूह… दो समूहों…। (1)",
    PT(D(sa), D(sa), "ārammaṇa") + f" – {ONE(sa)} {B1} तीन समूह… दो समूहों…। (1)",
    PT(D(an), D(an), "ārammaṇa") + f" – {ONE(an)} {B1} तीन समूह… दो समूहों… {PK} {ONE(an)} {B1} तीन समूह… दो समूहों… आधार {B1} समूह (सभी कारणों का इस तरीके से विस्तार करना चाहिए। संक्षिप्त)।",
    # ^7-16-7
    PT(D(an), D(an), "na:hetu") + f" – {AH(an)} {B1} तीन समूह और {RC}… दो समूहों… {APK}… एक महाभूत {B1}… बाह्य… आहार से उत्पन्न… तापमान से उत्पन्न… पहचान-रहित प्राणियों में… {MOHA}। (1)",
    PT(D(mi), D(an), "na:ārammaṇa") + f" – {KH(mi)} {B1} {RC} (संक्षिप्त)।",
    PT(D(mi), D(mi), "na:adhipati") + f" – {KH(mi)} {B1} {ADH[mi]}। (1)",
    PT(D(sa), D(sa), "na:adhipati") + f" – {KH(sa)} {B1} {ADH[sa]}। (1)",
    PT(D(an), D(an), "na:adhipati") + f" – {ONE(an)} {B1} तीन समूह और {RC}… दो समूहों… {PK}… {KV}; एक महाभूत… पहचान-रहित प्राणियों में…। (1)",
    PT(D(mi), D(an), "na:anantara") + " (संक्षिप्त, सभी कारणों का विस्तार करना चाहिए)।",
    # ^7-U312
    "(सह-उत्पत्ति का खंड निर्भरता के खंड के समान है।)",
    # Paccayavāra ^7-16-14
    PT(D(mi), D(mi), "hetu", "c") + "… तीन।",
    PT(D(sa), D(sa), "hetu", "c") + "… तीन।",
    PT(D(an), D(an), "hetu", "c") + f" – {ONE(an)} के कारण तीन समूह और {RC}… दो समूहों… {PK}… {KVc}; एक महाभूत के कारण… आधार के कारण {KN(an)}। (1)",
    PT(D(an), D(mi), "hetu", "c") + f" – आधार के कारण {KN(mi)}। (2)",
    PT(D(an), D(sa), "hetu", "c") + f" – आधार के कारण {KN(sa)}। (3)",
    PT(D(an), DP(mi, an), "hetu", "c") + f" – आधार के कारण {KN(mi)}, महाभूतों के कारण {RC}। (4)",
    PT(D(an), DP(sa, an), "hetu", "c") + f" – आधार के कारण {KN(sa)}, महाभूतों के कारण {RC}। (5)",
    PT(D2(mi, an), D(mi), "hetu", "c") + f" – {ONE(mi)} और आधार के कारण तीन समूह… दो समूहों…। (1)",
    PT(D2(mi, an), D(an), "hetu", "c") + f" – {KH(mi)} और महाभूतों के कारण {RC}। (2)",
    PT(D2(mi, an), DP(mi, an), "hetu", "c") + f" – {ONE(mi)} और आधार के कारण तीन समूह… दो समूहों… {KH(mi)} और महाभूतों के कारण {RC}। (3)",
    PT(D2(sa, an), D(sa), "hetu", "c") + " (तीन प्रश्न, ग़लत दिशा में निश्चित परिघटना के समान)।",
    # ^7-16-17
    PT(D(mi), D(mi), f"{A['ārammaṇa']}… (संक्षिप्त, हितकर वाले तीन के वर्गीकरण में कारण के खंड के समान विश्लेषण करना चाहिए)… {A['avigata']}", "c") + "।",
    # ^7-16-19
    PT(D(an), D(an), "na:hetu", "c") + f" – {AH(an)} के कारण तीन समूह और {RC}… दो समूहों… {APK}… {KVc}। एक महाभूत… पहचान-रहित प्राणियों में… आँख के इंद्रिय-क्षेत्र के कारण आँख की चेतना… शरीर के इंद्रिय-क्षेत्र के कारण शरीर की चेतना। आधार के कारण मूल से रहित, {KN(an)}। संशय के साथ होने वाले और बेचैनी के साथ होने वाले समूहों और आधार के कारण संशय के साथ होने वाला या बेचैनी के साथ होने वाला मोह। (1)",
    PT(D(mi), D(an), "na:ārammaṇa", "c") + f" – {KH(mi)} के कारण {RC} (हितकर वाले तीन के वर्गीकरण के समान, पाँच करने चाहिए)।",
    PT(D(mi), D(mi), "na:adhipati", "c") + f" – {KH(mi)} के कारण {ADH[mi]}। (1)",
    PT(D(sa), D(sa), "na:adhipati", "c") + f" – {KH(sa)} के कारण {ADH[sa]}। (1)",
    PT(D(an), D(an), "na:adhipati", "c") + f" – {ONE(an)} के कारण तीन समूह और {RC}… दो समूहों… {PK} … पहचान-रहित प्राणियों में… आँख के इंद्रिय-क्षेत्र के कारण आँख की चेतना… शरीर के इंद्रिय-क्षेत्र के कारण शरीर की चेतना। आधार के कारण {KN(an)}। (1)",
    PT(D(an), D(mi), "na:adhipati", "c") + f" – आधार के कारण {ADH[mi]}। (2)",
    PT(D(an), D(sa), "na:adhipati", "c") + f" – आधार के कारण {ADH[sa]}। (3)",
    PT(D2(mi, an), D(mi), "na:adhipati", "c") + f" – {KH(mi)} और आधार के कारण {ADH[mi]}। (1)",
    PT(D2(sa, an), D(sa), "na:adhipati", "c") + f" – {KH(sa)} और आधार के कारण {ADH[sa]}। (1)",
    PT(D(mi), D(an), f"{NA['anantara']}… {NA['natthi']}… {NA['vigata']}", "c") + "।",
    # ^7-U313
    "(आश्रय का खंड कारण के खंड के समान है)।",
    # Saṃsaṭṭhavāra ^7-16-26
    PT(D(mi), D(mi), "hetu", "s") + f" – {ONE(mi)} से घुल-मिलकर तीन समूह… दो समूहों…। (1)",
    PT(D(sa), D(sa), "hetu", "s") + f" – {ONE(sa)} से घुल-मिलकर तीन समूह… दो समूहों…। (1)",
    PT(D(an), D(an), "hetu", "s") + f" – {ONE(an)} से घुल-मिलकर तीन समूह… दो समूहों… {PK}…। (1)",
    PT(D(mi), D(mi), f"{A['ārammaṇa']}… {A['avigata']}", "s") + "।",
    PT(D(an), D(an), "na:hetu", "s") + f" – {AH(an)} से घुल-मिलकर तीन समूह… दो समूहों… {APK}…। (1)",
    PT(D(mi), D(mi), "na:adhipati", "s") + f" – {KH(mi)} से घुल-मिलकर {ADH[mi]}। (1)",
    PT(D(sa), D(sa), "na:adhipati", "s") + f" – {KH(sa)} से घुल-मिलकर {ADH[sa]}। (1)",
    PT(D(an), D(an), "na:adhipati", "s") + f" – {ONE(an)} से घुल-मिलकर तीन समूह… दो समूहों… {PK}…।(1)",
    PT(D(sa), D(sa), "na:purejāta", "s") + f" – {ARU} {ONE(sa)} से घुल-मिलकर तीन समूह… दो समूहों…। (1)",
    PT(D(an), D(an), "na:purejāta", "s") + f" – {ARU} {ONE(an)} से घुल-मिलकर तीन समूह… दो समूहों… {PK}…। (1)",
    PT(D(mi), D(mi), "na:pacchājāta", "s") + " (परिपूर्ण)।",
    PT(D(an), D(an), "na:āsevana", "s") + f" – {ONE(an)} से घुल-मिलकर तीन समूह… दो समूहों… {PK}…। (1)",
    PT(D(mi), D(mi), f"{NA['kamma']}, {NA['vipāka']}", "s") + " (संक्षिप्त)।",
    PT(D(an), D(an), "na:jhāna", "s") + f" – पाँच प्रकार की चेतना… {NA['magga']} – मूल से रहित, अनिश्चित…।",
    PT(D(sa), D(sa), "na:vippayutta", "s") + f" – {ARU} {ONE(sa)} से घुल-मिलकर तीन समूह… दो समूहों…। (1)",
    PT(D(an), D(an), "na:vippayutta", "s") + f" – {ARU} {ONE(an)} से घुल-मिलकर तीन समूह… दो समूहों…। (1)",
    # ^7-U314
    "(जुड़ाव का खंड घुले-मिले होने के खंड के समान है)।",
    # Pañhāvāra hetu ^7-16-36
    PN(D(mi), DT(mi), "hetu") + f" – {J(mi)} मूल {SK} {I('hetu', 'mp')}। (1)",
    PN(D(mi), DT(an), "hetu") + f" – {J(mi)} मूल {DCR} {I('hetu', 'mp')}। (2)",
    PN(D(mi), DT(mi, an), "hetu") + f" – {J(mi)} मूल {SKC} {I('hetu', 'mp')}। (3)",
    PN(D(sa), DT(sa), "hetu") + "… तीन।",
    PN(D(an), DT(an), "hetu") + f" – {J(an)} मूल {SKC} {I('hetu', 'mp')}। {PK}…। (1)",
    # ārammaṇa ^7-16-37
    PN(D(mi), DT(an), "ārammaṇa") + f" – आर्य {J(mi)}, {KIL_P} पर पुनः विचार करते हैं, {KIL_S} को जानते हैं। {KH(mi)} को अनित्य के रूप में… अंतर्दृष्टि से देखते हैं। {CETO} {J(mi)} मन से युक्त व्यक्ति के मन को जानते हैं। {KN(mi)} {NL('cetopariyañāṇassa', 'pubbenivāsānussatiñāṇassa', 'yathākammūpagañāṇassa', 'anāgataṃsañāṇassa', 'āvajjanāya')} {I('ārammaṇa', 'mp')}। (1)",
    PN(D(sa), DT(an), "ārammaṇa") + f" – आर्य मार्ग से उठकर मार्ग पर पुनः विचार करते हैं। {CETO} {J(sa)} मन से युक्त व्यक्ति के मन को जानते हैं। {KN(sa)} {NL('cetopariyañāṇassa', 'pubbenivāsānussatiñāṇassa', 'anāgataṃsañāṇassa', 'āvajjanāya')} {I('ārammaṇa', 'mp')}। (1)",
    PN(D(an), DT(an), "ārammaṇa") + f" – {GIFT} उस पर पुनः विचार करता है, {DEEDS} पर पुनः विचार करता है, ध्यान से उठकर ध्यान पर पुनः विचार करता है, आर्य फल पर पुनः विचार करते हैं, निर्वाण पर पुनः विचार करते हैं, निर्वाण {NL('gotrabhussa', 'vodānassa', 'phalassa', 'āvajjanāya')} {I('ārammaṇa', 'ms')}। आर्य {J(an)}, {KIL_P} पर पुनः विचार करते हैं, {KIL_V} पर पुनः विचार करते हैं। {KIL_S} को जानते हैं। आँख… आधार… {KH(an)} को {ANI} अंतर्दृष्टि से देखते हैं, उनका रस लेते हैं, उनमें आनंद लेते हैं, उसे विषय बनाकर {J(an)} राग उत्पन्न होता है… उदासी उत्पन्न होती है। {DIBBA}, {CETO} {J(an)} मन से युक्त व्यक्ति के मन को जानता है, अनंत आकाश का क्षेत्र, अनंत चेतना के क्षेत्र के लिए… कुछ भी न होने का क्षेत्र, न पहचान न अ-पहचान के क्षेत्र के लिए {I('ārammaṇa', 'ms')}। {RUPA5} {I('ārammaṇa', 'ms')}। {KN(an)} {NL('iddhividhañāṇassa', 'cetopariyañāṇassa', 'pubbenivāsānussatiñāṇassa', 'yathākammūpagañāṇassa', 'anāgataṃsañāṇassa', 'āvajjanāya')} {I('ārammaṇa', 'mp')}। (1)",
    PN(D(an), DT(mi), "ārammaṇa") + f" – {RJI} {CRIME4} {I('ārammaṇa')}। जिस आधार को ग़लत धारणा से पकड़ने वाले व्यक्ति में {KN(mi)} उत्पन्न होते हैं, वह आधार {KH(mi)} के लिए {I('ārammaṇa', 'ms')}। (2)",
    PN(D(an), DT(sa), "ārammaṇa") + f" – निर्वाण मार्ग के लिए {I('ārammaṇa', 'ms')}। (3)",
    # adhipati ^7-16-39
    PN(D(mi), DT(mi), "adhipati") + f"। {SAHA} – {ADH[mi]} {SK} {I('adhipati')}। (1)",
    PN(D(mi), DT(an), "adhipati") + f"। {SAHA} – {ADH[mi]} {DCR} {I('adhipati')}। (2)",
    PN(D(mi), DT(mi, an), "adhipati") + f"। {SAHA} – {ADH[mi]} {SKC} {I('adhipati')}। (3)",
    PN(D(sa), DT(sa), "adhipati") + f"। {SAHA} – {ADH[sa]} {SK} {I('adhipati')}। (1)",
    PN(D(sa), DT(an), "adhipati") + f" – {ARAM}, {SAHA}। {ARAM} – आर्य मार्ग से उठकर मार्ग को महत्व देकर पुनः विचार करते हैं। {SAHA} – {ADH[sa]} {DCR} {I('adhipati')}। (2)",
    PN(D(sa), DT(sa, an), "adhipati") + f"। {SAHA} – {ADH[sa]} {SKC} {I('adhipati')}। (3)",
    PN(D(an), DT(an), "adhipati") + f" – {ARAM} {SAHA}। {ARAM} – {GIFT} उसे महत्व देकर पुनः विचार करता है, {DEEDS} को महत्व देकर पुनः विचार करता है, ध्यान से… आर्य फल को महत्व देकर पुनः विचार करते हैं, निर्वाण को महत्व देकर पुनः विचार करते हैं, निर्वाण {NL('gotrabhussa', 'vodānassa', 'phalassa')} {I('adhipati', 'ms')}। आँख… आधार… {KH(an)} को महत्व देकर {SAVp}, उसे महत्व देकर {J(an)} राग उत्पन्न होता है, दृष्टि उत्पन्न होती है। {SAHA} – {ADH[an]} {SKC} {I('adhipati')}। (1)",
    PN(D(an), DT(sa), "adhipati") + f"। {ARAM} – निर्वाण मार्ग के लिए {I('adhipati', 'ms')}। (2)",
    # anantara ^7-16-42
    PN(D(mi), DT(an), "anantara") + f" – {KN(mi)} बाहर आने के लिए {I('anantara', 'mp')}। (1)",
    PN(D(sa), DT(an), "anantara") + f" – मार्ग फल के लिए {I('anantara', 'ms')}। (1)",
    PN(D(an), DT(an), "anantara") + f" – पहले-पहले के {KN(an)} बाद-बाद के {KH(an)} के लिए {I('anantara', 'mp')}। अनुरूपता गोत्र-परिवर्तन के लिए… अनुरूपता शुद्धि के लिए… फल फल के लिए… अनुरूपता {FS}… {NIRODHA} {NEVA} {FS} {I('anantara', 'ms')}। (1)",
    PN(D(an), DT(mi), "anantara") + f" – {J(an)} उदासी {J(mi)} उदासी के लिए {I('anantara')}। {J(an)} ग़लत दृष्टि निश्चित ग़लत दृष्टि के लिए {I('anantara')}। (2)",
    PN(D(an), DT(sa), "anantara") + f" – गोत्र-परिवर्तन मार्ग के लिए… शुद्धि मार्ग के लिए {I('anantara')}। (3)",
    # samanantara … nissaya ^7-16-44
    PN(D(mi), DT(an), "samanantara") + f" (निकटता-कारण के समान)… {I('sahajāta')} (निर्भरता के खंड के समान, नौ प्रश्न)… {I('aññamañña')} (निर्भरता के खंड के समान, तीन प्रश्न)… {I('nissaya')} (हितकर वाले तीन के वर्गीकरण के समान, तेरह प्रश्न)।",
    # upanissaya ^7-16-45
    PN(D(mi), DT(mi), "upanissaya") + f"। {LAB['up_p']} – माता की हत्या का कर्म, माता की हत्या के कर्म के लिए {I('upanissaya', 'ms')}। माता की हत्या का कर्म… पिता की हत्या का कर्म… अर्हत् की हत्या का कर्म… बुद्ध का खून बहाने का कर्म… संघ में फूट डालने का कर्म… निश्चित ग़लत दृष्टि के लिए {I('upanissaya', 'ms')} (चक्र बनाना चाहिए)। निश्चित ग़लत दृष्टि, निश्चित ग़लत दृष्टि के लिए {I('upanissaya')}। निश्चित ग़लत दृष्टि माता की हत्या के कर्म के लिए… संघ में फूट डालने के कर्म के लिए {I('upanissaya')}। (1)",
    PN(D(mi), DT(an), "upanissaya") + f" – {LAB['up_a']}, {LAB['up_p']}…। {LAB['up_p']} – माता की जान लेकर उसके प्रतिकार के लिए {GIFT3}। पिता की जान लेकर… अर्हत् की जान लेकर… दुष्ट मन से तथागत का खून बहाकर… संघ में फूट डालकर उसके प्रतिकार के लिए {GIFT3}। (2)",
    PN(D(sa), DT(sa), "upanissaya") + f"। {LAB['up_p']} – पहला मार्ग दूसरे मार्ग के लिए {I('upanissaya', 'ms')}… तीसरा मार्ग चौथे मार्ग के लिए {I('upanissaya', 'ms')}। (1)",
    PN(D(sa), DT(an), "upanissaya") + f" – {LAB['up_ā']}, {LAB['up_a']}, {LAB['up_p']}…। {LAB['up_p']} – आर्य मार्ग के प्रबल आश्रय से उत्पन्न न हुई ध्यान-अवस्था को उत्पन्न करते हैं, उत्पन्न हो चुकी ध्यान-अवस्था में प्रवेश करते हैं, निर्मित परिघटनाओं को {ANI} अंतर्दृष्टि से देखते हैं। मार्ग आर्यों के अर्थ के विश्लेषणात्मक ज्ञान के लिए… संभव और असंभव को जानने की कुशलता के लिए {I('upanissaya', 'ms')}। मार्ग {FS} {I('upanissaya', 'ms')}। (2)",
    PN(D(an), DT(an), "upanissaya") + f" – {LAB['up_ā']}, {LAB['up_a']}, {LAB['up_p']}…। {LAB['up_p']} – {J(an)} श्रद्धा के प्रबल आश्रय से दान देता है, सदाचार ग्रहण करता है, उपवास-व्रत… ध्यान उत्पन्न करता है, अंतर्दृष्टि… उच्च ज्ञान… ध्यान-अवस्था उत्पन्न करता है, अहंकार पालता है, दृष्टि ग्रहण करता है। {J(an)} सदाचार… सुने-सीखे ज्ञान… त्याग… प्रज्ञा… राग… कामना… शारीरिक सुख… शारीरिक दुःख… तापमान… भोजन… निवास-स्थान के प्रबल आश्रय से दान देता है… कस्बे पर हमला करता है। {J(an)} श्रद्धा… प्रज्ञा, राग… निवास-स्थान {J(an)} श्रद्धा के लिए… शारीरिक सुख, शारीरिक दुःख और {FS} {I('upanissaya', 'mp')}। पहले ध्यान की प्रारंभिक तैयारी उसी के लिए… न पहचान न अ-पहचान के क्षेत्र की प्रारंभिक तैयारी उसी के लिए… पहला ध्यान दूसरे ध्यान के लिए… कुछ भी न होने का क्षेत्र न पहचान न अ-पहचान के क्षेत्र के लिए… जीव-हत्या, जीव-हत्या के लिए {I('upanissaya')} (चक्र बनाना चाहिए)। (1)",
    PN(D(an), DT(mi), "upanissaya") + f" – {LAB['up_a']}, {LAB['up_p']}…। {LAB['up_p']} – {J(an)} राग के प्रबल आश्रय से माता की जान लेता है… संघ में फूट डालता है। {J(an)} द्वेष… कामना… शारीरिक सुख… निवास-स्थान के प्रबल आश्रय से माता की जान लेता है… संघ में फूट डालता है। {J(an)} राग… निवास-स्थान {CRIME4}… संघ में फूट डालने के कर्म के लिए… निश्चित ग़लत दृष्टि के लिए {I('upanissaya', 'mp')}। (2)",
    PN(D(an), DT(sa), "upanissaya") + f" – {LAB['up_ā']}, {LAB['up_a']}, {LAB['up_p']}…। {LAB['up_p']} – पहले मार्ग की प्रारंभिक तैयारी पहले मार्ग के लिए… चौथे मार्ग की प्रारंभिक तैयारी चौथे मार्ग के लिए {I('upanissaya')}। (3)",
    # purejāta ^7-16-48
    PN(D(an), DT(an), "purejāta") + f" – {LAB['pj_ā']}, {LAB['pj_v']}। {LAB['pj_ā']} – आँख… आधार को अनित्य के रूप में… अंतर्दृष्टि से देखता है, {SAV}, उसे विषय बनाकर {J(an)} राग उत्पन्न होता है… उदासी उत्पन्न होती है। {DIBBA}, {RUPA5} {I('purejāta', 'ms')}। {LAB['pj_v']} – {VATTHU5}… आधार {KH(an)} के लिए {I('purejāta', 'ms')}। (1)",
    PN(D(an), DT(mi), "purejāta") + f" – {LAB['pj_ā']}, {LAB['pj_v']}। {LAB['pj_ā']} – {RJI} {CRIME4} {I('purejāta')}। {LAB['pj_v']} – आधार {KH(mi)} के लिए {I('purejāta', 'ms')}। (2)",
    PN(D(an), DT(sa), "purejāta") + f"। {LAB['pj_v']} – आधार {KH(sa)} के लिए {I('purejāta', 'ms')}। (3)",
    # pacchājāta ^7-16-49
    PN(D(mi), DT(an), "pacchājāta") + f" – बाद में उत्पन्न {KN(mi)} {KAYA} {I('pacchājāta', 'mp')}। (1)",
    PN(D(sa), DT(an), "pacchājāta") + f"। बाद में उत्पन्न {KN(sa)} {KAYA} {I('pacchājāta', 'mp')}। (1)",
    PN(D(an), DT(an), "pacchājāta") + f" – बाद में उत्पन्न {KN(an)} {KAYA} {I('pacchājāta', 'mp')}। (1)",
    # āsevana ^7-16-50
    PN(D(an), DT(an), "āsevana") + f" – पहले-पहले के {KN(an)} बाद-बाद के {KH(an)} के लिए {I('āsevana', 'mp')}। अनुरूपता गोत्र-परिवर्तन के लिए… अनुरूपता शुद्धि के लिए {I('āsevana')}। (1)",
    PN(D(an), DT(mi), "āsevana") + f" – {J(an)} उदासी {J(mi)} उदासी के लिए {I('āsevana')}। {J(an)} ग़लत दृष्टि निश्चित ग़लत दृष्टि के लिए {I('āsevana')}। (2)",
    PN(D(an), DT(sa), "āsevana") + f" – गोत्र-परिवर्तन मार्ग के लिए… शुद्धि मार्ग के लिए {I('āsevana')}। (3)",
    # kamma ^7-16-51
    PN(D(mi), DT(mi), "kamma") + f" – {J(mi)} इरादा {SK} {I('kamma', 'ms')}। (1)",
    PN(D(mi), DT(an), "kamma") + f" – सह-उत्पत्ति, भिन्न क्षण। सह-उत्पत्ति – {J(mi)} इरादा {DCR} {I('kamma', 'ms')}। भिन्न क्षण – {J(mi)} इरादा {VKK} {I('kamma', 'ms')}। (2)",
    PN(D(mi), DT(mi, an), "kamma") + f" – {J(mi)} इरादा {SKC} {I('kamma', 'ms')}। (3)",
    PN(D(sa), DT(sa), "kamma") + f" – {J(sa)} इरादा {SK} {I('kamma', 'ms')}। (1)",
    PN(D(sa), DT(an), "kamma") + f" – सह-उत्पत्ति, भिन्न क्षण। सह-उत्पत्ति – {J(sa)} इरादा {DCR} {I('kamma', 'ms')}। भिन्न क्षण – {J(sa)} इरादा कर्म-फल रूपी समूहों के लिए {I('kamma', 'ms')}। (2)",
    PN(D(sa), DT(sa, an), "kamma") + f" – {J(sa)} इरादा {SKC} {I('kamma', 'ms')}। (3)",
    PN(D(an), DT(an), "kamma") + f" – सह-उत्पत्ति, भिन्न क्षण। सह-उत्पत्ति – {J(an)} इरादा {SKC} {I('kamma', 'ms')}। {PK}…। भिन्न क्षण – {J(an)} इरादा {VKK} {I('kamma', 'ms')}। (1)",
    # vipāka ^7-16-53
    PN(D(an), DT(an), "vipāka") + f" – कर्म-फल रूपी, {J(an)} एक समूह तीन समूहों के लिए और {DCR} {I('vipāka', 'ms')}… {PK}… समूह आधार के लिए…।",
    # āhāra … ^7-16-54
    UD(D(mi), DT(mi), ["āhāra", "indriya", "jhāna", "magga", "sampayutta"]) + "।",
    # vippayutta ^7-16-55
    PN(D(mi), DT(an), "vippayutta") + f" – सह-उत्पत्ति, पश्चात्-उत्पत्ति। सह-उत्पत्ति – {KN(mi)} {DCR} {I('vippayutta', 'mp')}। पश्चात्-उत्पत्ति – {KN(mi)} {KAYA} {I('vippayutta', 'mp')}। (1)",
    PN(D(sa), DT(an), "vippayutta") + f" – सह-उत्पत्ति, पश्चात्-उत्पत्ति। सह-उत्पत्ति – {KN(sa)} {DCR} {I('vippayutta', 'mp')}। पश्चात्-उत्पत्ति – {KN(sa)} {KAYA} {I('vippayutta', 'mp')}। (1)",
    PN(D(an), DT(an), "vippayutta") + f" – सह-उत्पत्ति, पूर्व-उत्पत्ति, पश्चात्-उत्पत्ति। सह-उत्पत्ति – {KN(an)} {DCR} {I('vippayutta', 'mp')}। {PK}… समूह आधार के लिए {I('vippayutta', 'mp')}। आधार समूहों के लिए {I('vippayutta', 'ms')}। पूर्व-उत्पत्ति – {VATTHU5}… आधार {KH(an)} के लिए {I('vippayutta', 'ms')}। पश्चात्-उत्पत्ति – {KN(an)} {KAYA} {I('vippayutta', 'mp')}। (1)",
    PN(D(an), DT(mi), "vippayutta") + f"। पूर्व-उत्पत्ति – आधार {KH(mi)} के लिए {I('vippayutta', 'ms')}। (2)",
    PN(D(an), DT(sa), "vippayutta") + f"। पूर्व-उत्पत्ति – आधार {KH(sa)} के लिए {I('vippayutta', 'ms')}। (3)",
    # atthi ^7-16-56
    PN(D(mi), DT(mi), "atthi") + f" – {ONE(mi, 'm')} तीन समूहों के लिए… दो समूह दो समूहों के लिए {I('atthi', 'mp')}। (1)",
    PN(D(mi), DT(an), "atthi") + f" – सह-उत्पत्ति, पश्चात्-उत्पत्ति। सह-उत्पत्ति – {KN(mi)} {DCR} {I('atthi', 'mp')}। पश्चात्-उत्पत्ति – {KN(mi)} {KAYA} {I('atthi', 'mp')}। (2)",
    PN(D(mi), f"{J(mi)} और {J(an)} के लिए", "atthi") + f" – {ONE(mi, 'm')} तीन समूहों के लिए और {DCR} {I('atthi', 'ms')}… दो समूह…। (3)",
    PN(D(sa), DT(sa), "atthi") + "… (तीन प्रश्न)।",
    PN(D(an), DT(an), "atthi") + f" – सह-उत्पत्ति, पूर्व-उत्पत्ति, पश्चात्-उत्पत्ति, आहार, क्षमता। सह-उत्पत्ति – {ONE(an, 'm')} तीन समूहों के लिए और {DCR} {I('atthi', 'ms')}… दो समूह… {PK}… समूह आधार के लिए {I('atthi', 'mp')}। आधार समूहों के लिए {I('atthi', 'ms')}। एक महाभूत… पहचान-रहित प्राणियों में एक महाभूत…। पूर्व-उत्पत्ति – आँख… आधार को {ANI} अंतर्दृष्टि से देखता है, {SAV}, {RAGO}… उदासी उत्पन्न होती है। {DIBBA}, {RUPA5}… {VATTHU5}… आधार {KH(an)} के लिए {I('atthi', 'ms')}। पश्चात्-उत्पत्ति – {KN(an)} {KAYA} {I('atthi', 'mp')}। {KABA} इस शरीर के लिए {I('atthi', 'ms')}। {RJI} {DKR} {I('atthi')}। (1)",
    PN(D(an), DT(mi), "atthi") + f"। पूर्व-उत्पत्ति – {RJI} माता की हत्या के कर्म के लिए… बुद्ध का खून बहाने के कर्म के लिए {I('atthi')}। आधार {KH(mi)} के लिए {I('atthi', 'ms')}। (2)",
    PN(D(an), DT(sa), "atthi") + f"। पूर्व-उत्पत्ति – आधार {KH(sa)} के लिए {I('atthi', 'ms')}। (3)",
    PN(DP(mi, an), DT(mi), "atthi", "fp") + f" – सह-उत्पत्ति, पूर्व-उत्पत्ति। सह-उत्पत्ति – {ONE(mi, 'm')} और आधार तीन समूहों के लिए… दो समूह और…। (1)",
    PN(DP(mi, an), DT(an), "atthi", "fp") + f" – सह-उत्पत्ति, पश्चात्-उत्पत्ति, आहार, क्षमता। सह-उत्पत्ति – {KN(mi)} और महाभूत {DCR} {I('atthi', 'mp')}। पश्चात्-उत्पत्ति – {KN(mi)} और {KABA} इस शरीर के लिए {I('atthi', 'mp')}। पश्चात्-उत्पत्ति – {KN(mi)} और {RJI} {DKR} {I('atthi', 'mp')}। (2)",
    PN(DP(sa, an), DT(sa), "atthi", "fp") + "… (दो प्रश्न, ग़लत दिशा में निश्चित परिघटना के समान)।",
    # Paccanīyuddhāra ^7-16-59
    UD(D(mi), DT(mi), ["sahajāta", "upanissaya"]) + "। (1)",
    UD(D(mi), DT(an), ["ārammaṇa", "sahajāta", "upanissaya", "pacchājāta", "kamma"]) + "। (2)",
    UD(D(mi), DT(mi, an), ["sahajāta"]) + "। (3)",
    UD(D(sa), DT(sa), ["sahajāta", "upanissaya"]) + "। (1)",
    UD(D(sa), DT(an), ["ārammaṇa", "sahajāta", "upanissaya", "pacchājāta"]) + "। (2)",
    UD(D(sa), DT(sa, an), ["sahajāta"]) + "। (3)",
    UD(D(an), DT(an), ["ārammaṇa", "sahajāta", "upanissaya", "purejāta", "pacchājāta", "kamma", "āhāra", "indriya"]) + "। (1)",
    UD(D(an), DT(mi), ["ārammaṇa", "upanissaya", "purejāta"]) + "। (2)",
    UD(D(an), DT(sa), ["upanissaya", "purejāta"]) + "। (3)",
    f"{DP(mi, an)}, {DT(mi)} सह-उत्पत्ति, पूर्व-उत्पत्ति। (1)",
    f"{DP(mi, an)}, {DT(an)} सह-उत्पत्ति, पश्चात्-उत्पत्ति, आहार, क्षमता। (2)",
    f"{DP(sa, an)}, {DT(sa)} सह-उत्पत्ति, पूर्व-उत्पत्ति। (1)",
    f"{DP(sa, an)}, {DT(an)} सह-उत्पत्ति, पश्चात्-उत्पत्ति, आहार, क्षमता। (2)",
]
