# 2-14 Atītārammaṇattika: hand lines (exec'd by build_rails_2-09_2-17.py)
ar, gr, pr = "ar", "gr", "pr"


def UD(x, y, keys, g="fs"):
    return f"{x}, {y} " + "… ".join(I(k, g) for k in keys)


def AH(c):
    return f"मूल से रहित, {J(c, 'o')} एक समूह"


SAHA, ARAM = LAB["ādh_s"], LAB["ādh_ā"]
UPA, UPN, UPP = LAB["up_ā"], LAB["up_a"], LAB["up_p"]
NEVA_O = "न पहचान न अ-पहचान के क्षेत्र"
CONE = f"दो समूहों {B1} दो समूह"
RV, RVp = "पुनः विचार करता है", "पुनः विचार करते हैं"
GK = "को महत्व देकर पुनः विचार करता है"


def T(c):
    """time adjective of the object (atītaṃ / anāgataṃ / paccuppannaṃ) for masc. oblique nouns."""
    return {"ar": "अतीत के", "gr": "भविष्य के", "pr": "वर्तमान के"}[c]


def Tf(c):
    return {"ar": "अतीत की", "gr": "भविष्य की", "pr": "वर्तमान की"}[c]


def ANU(c1, c2):
    return (f"{J(c1, 'o')} अनित्यता का अवलोकन, दुःख का अवलोकन और आत्मा से रहित होने का अवलोकन {J(c2, 'o')} "
            f"अनित्यता के अवलोकन, दुःख के अवलोकन और आत्मा से रहित होने के अवलोकन के लिए {I('upanissaya', 'mp')}")


def PUR(c1, c2):
    return f"पहले-पहले के {KN(c1)} बाद-बाद के {KH(c2)} के लिए"


def VIP(c):
    return f"कर्म-फल रूपी, {J(c, 'o')} समूहों के लिए"


def KX(c1, c2):
    """atītārammaṇe atīte khandhe (object + time)."""
    return f"{J(c1, 'o')}, {T(c2)} समूहों"


def KXn(c1, c2):
    return f"{J(c1, 'o')}, {T(c2)} समूह"


CH19 = (f"{A['ārammaṇa']}… {A['adhipati']} (प्रधानता-कारण में पुनर्जन्म नहीं है)… {A['anantara']}… {A['samanantara']}… "
        f"{A['sahajāta']}… {A['aññamañña']}… {A['nissaya']}… {A['upanissaya']}… {A['purejāta']}… {A['āsevana']} "
        f"(पूर्व-उत्पत्ति-कारण में भी और पुनरावृत्ति-कारण में भी पुनर्जन्म नहीं है)… {A['kamma']}… {A['vipāka']} "
        f"(कर्म-फल रूपी, {J(ar, 'm')} एक समूह, तीनों प्रश्न भी परिपूर्ण। जीवन-काल और पुनर्जन्म करने चाहिए)… "
        + "… ".join(A[k] for k in ["āhāra", "indriya", "jhāna", "magga", "sampayutta", "vippayutta", "atthi", "natthi",
                                   "vigata", "avigata"]))

L = [
    # ^7-20-1
    PT(D(ar), D(ar), "hetu") + f" – {ONE(ar)} {B1} तीन समूह… {CONE}। {PK} {ONE(ar)} {B1} तीन समूह… {CONE}। (1)",
    PT(D(gr), D(gr), "hetu") + f" – {ONE(gr)} {B1} तीन समूह… दो समूह। (1)",
    PT(D(pr), D(pr), "hetu") + f" – {ONE(pr)} {B1} तीन समूह… दो समूह। {PK} {ONE(pr)} {B1} तीन समूह… दो समूह। (1)",
    PT(D(ar), D(ar), CH19) + "।",
    # paccanīya ^7-20-6
    PT(D(ar), D(ar), "na:hetu") + f" – {AH(ar)} {B1} तीन समूह… दो समूहों… {APK} … {MOHA}। (1)",
    PT(D(gr), D(gr), "na:hetu") + f" – {AH(gr)} {B1} तीन समूह… दो समूहों… {MOHA}। (1)",
    PT(D(pr), D(pr), "na:hetu") + f" – {AH(pr)} {B1} तीन समूह… दो समूहों… {APK}… {MOHA}। (1)",
    PT(D(ar), D(ar), "na:adhipati") + " (सकारात्मक क्रम के सह-उत्पत्ति-कारण के समान)।",
    PT(D(ar), D(ar), "na:purejāta") + f" – {ARU} {ONE(ar)} {B1}… दो समूहों… {PK}…। (1)",
    PT(D(gr), D(gr), "na:purejāta") + f" – {ARU} {ONE(gr)} {B1} तीन समूह… दो समूहों…। (1)",
    PT(D(pr), D(pr), "na:purejāta") + f" – {PK} {ONE(pr)} {B1}… दो समूहों…। (1)",
    PT(D(ar), D(ar), f"{NA['pacchājāta']}… {NA['āsevana']} (प्रधानता-कारण के अभाव के समान)… {NA['kamma']}") + f" – {KH(ar)} {B1} {J(ar, 'm')} इरादा। (1)",
    PT(D(gr), D(gr), "na:kamma") + f" – {KH(gr)} {B1} {J(gr, 'm')} इरादा। (1)",
    PT(D(pr), D(pr), "na:kamma") + f" – {KH(pr)} {B1} {J(pr, 'm')} इरादा। (1)",
    PT(D(ar), D(ar), "na:vipāka") + "… (कर्म-फल-कारण के अभाव में पुनर्जन्म नहीं है)।",
    PT(D(pr), D(pr), "na:jhāna") + f" – पाँच प्रकार की चेतना के साथ होने वाले एक समूह {B1} तीन समूह… दो समूहों…। (1)",
    PT(D(ar), D(ar), "na:magga") + f" – {AH(ar)} {B1} तीन समूह… (मूल-कारण के अभाव के समान तीन प्रश्न, मोह नहीं है)।",
    PT(D(ar), D(ar), "na:vippayutta") + f" – {ARU} {ONE(ar)} {B1} तीन समूह… दो समूहों…। (1)",
    PT(D(gr), D(gr), "na:vippayutta") + f" – {ARU} {ONE(gr)} {B1} तीन समूह… दो समूहों…। (1)",
    # ^7-U316
    "(सह-उत्पत्ति का खंड, कारण का खंड, आश्रय का खंड, घुले-मिले होने का खंड और जुड़ाव का खंड भी निर्भरता के खंड के समान हैं।)",
    # Pañhāvāra hetu ^7-20-19
    PN(D(ar), DT(ar), "hetu") + f" – {J(ar, 'o')} मूल {SK} {I('hetu', 'mp')}। {PK} {J(ar, 'o')} मूल {SK} {I('hetu', 'mp')}। (1)",
    PN(D(gr), DT(gr), "hetu") + f" – {J(gr, 'o')} मूल {SK} {I('hetu', 'mp')}। (1)",
    PN(D(pr), DT(pr), "hetu") + f" – {J(pr, 'o')} मूल {SK} {I('hetu', 'mp')}। {PK} {J(pr, 'o')} मूल {SK} {I('hetu', 'mp')}। (1)",
    # ārammaṇa ^7-20-20
    PN(D(ar), DT(ar), "ārammaṇa") + f" – अतीत के अनंत चेतना के क्षेत्र पर {RV}, {NEVA_O} पर {RV}। {J(ar, 'o')}, अतीत के अलौकिक शक्तियों के ज्ञान पर {RV}, दूसरों के मन को जानने के ज्ञान… पूर्व जन्मों के अनुस्मरण के ज्ञान… प्राणियों के अपने कर्मों के अनुसार जाने के ज्ञान पर {RV}। आर्य {J(ar, 'o')}, {KIL_P} पर {RVp}, {KIL_V} पर {RVp}, {KIL_S} को जानते हैं। {KX(ar, ar)} को {ANI} अंतर्दृष्टि से देखता है, {SAVp}; उसे विषय बनाकर {J(ar, 'm')} राग उत्पन्न होता है, दृष्टि… संशय… बेचैनी… उदासी उत्पन्न होती है। {KXn(ar, ar)} {NL('cetopariyañāṇassa', 'pubbenivāsānussatiñāṇassa', 'yathākammūpagañāṇassa', 'āvajjanāya')} {I('ārammaṇa', 'mp')}। (1)",
    PN(D(ar), DT(gr), "ārammaṇa") + f" – भविष्य के अनंत चेतना के क्षेत्र पर {RV}, {NEVA_O} पर {RV}। {J(ar, 'o')}, भविष्य के अलौकिक शक्तियों के ज्ञान पर {RV}, दूसरों के मन को जानने के ज्ञान… पूर्व जन्मों के अनुस्मरण के ज्ञान… प्राणियों के अपने कर्मों के अनुसार जाने के ज्ञान पर {RV}। {KX(ar, gr)} को अनित्य के रूप में… अंतर्दृष्टि से देखता है, {SAVp}; उसे विषय बनाकर {J(gr, 'm')} राग उत्पन्न होता है… उदासी उत्पन्न होती है। {KXn(ar, gr)} {NL('cetopariyañāṇassa', 'anāgataṃsañāṇassa', 'āvajjanāya')} {I('ārammaṇa', 'mp')}। (2)",
    PN(D(ar), DT(pr), "ārammaṇa") + f" – {CETO} {J(ar, 'o')}, वर्तमान के मन से युक्त व्यक्ति के मन को जानता है। {KXn(ar, pr)} {NL('cetopariyañāṇassa', 'āvajjanāya')} {I('ārammaṇa', 'mp')}। (3)",
    PN(D(gr), DT(gr), "ārammaṇa") + f" – {J(gr, 'o')}, भविष्य के अलौकिक शक्तियों के ज्ञान पर {RV}, दूसरों के मन को जानने के ज्ञान… भविष्य को जानने के ज्ञान… {KX(gr, gr)} को अनित्य के रूप में… अंतर्दृष्टि से देखता है, {SAVp}; उसे विषय बनाकर {J(gr, 'm')} राग उत्पन्न होता है… उदासी उत्पन्न होती है। {KXn(gr, gr)} {NL('cetopariyañāṇassa', 'anāgataṃsañāṇassa', 'āvajjanāya')} {I('ārammaṇa', 'mp')}। (1)",
    PN(D(gr), DT(ar), "ārammaṇa") + f" – {J(gr, 'o')}, अतीत के अलौकिक शक्तियों के ज्ञान पर {RV}, दूसरों के मन को जानने के ज्ञान… भविष्य को जानने के ज्ञान… आर्य {J(gr, 'o')}, {KIL_P} पर {RVp}, {KIL_V} पर {RVp}। {KIL_S} को जानते हैं। {KX(gr, ar)} को अनित्य के रूप में… अंतर्दृष्टि से देखता है, {SAVp}; उसे विषय बनाकर {J(ar, 'm')} राग उत्पन्न होता है… उदासी उत्पन्न होती है। {KXn(gr, ar)} {NL('cetopariyañāṇassa', 'pubbenivāsānussatiñāṇassa', 'yathākammūpagañāṇassa', 'āvajjanāya')} {I('ārammaṇa', 'mp')}। (2)",
    PN(D(gr), DT(pr), "ārammaṇa") + f" – {CETO} {J(gr, 'o')}, वर्तमान के मन से युक्त व्यक्ति के मन को जानता है। {KXn(gr, pr)} {NL('cetopariyañāṇassa', 'āvajjanāya')} {I('ārammaṇa', 'mp')}। (3)",
    PN(D(pr), DT(pr), "ārammaṇa") + f" – {CETO} {J(pr, 'o')}, वर्तमान के मन से युक्त व्यक्ति के मन को जानता है। {KXn(pr, pr)} {NL('cetopariyañāṇassa', 'āvajjanāya')} {I('ārammaṇa', 'mp')}। (1)",
    PN(D(pr), DT(ar), "ārammaṇa") + f" – अतीत की दिव्य आँख पर {RV}, दिव्य कान के तत्व पर {RV}, {J(pr, 'o')}, अतीत के अलौकिक शक्तियों के ज्ञान पर {RV}, दूसरों के मन को जानने के ज्ञान पर {RV}। आर्य {J(pr, 'o')}, {KIL_P} पर {RVp}, {KIL_V} पर {RVp}, {KIL_S} को जानते हैं। {KX(pr, ar)} को अनित्य के रूप में… अंतर्दृष्टि से देखता है, {SAVp}; उसे विषय बनाकर {J(ar, 'm')} राग उत्पन्न होता है… उदासी उत्पन्न होती है। {KXn(pr, ar)} {NL('cetopariyañāṇassa', 'pubbenivāsānussatiñāṇassa', 'yathākammūpagañāṇassa', 'āvajjanāya')} {I('ārammaṇa', 'mp')}। (2)",
    PN(D(pr), DT(gr), "ārammaṇa") + f" – भविष्य की दिव्य आँख पर {RV}, दिव्य कान के तत्व पर {RV}, {J(pr, 'o')}, भविष्य के अलौकिक शक्तियों के ज्ञान पर {RV}, दूसरों के मन को जानने के ज्ञान… {KX(pr, gr)} को अनित्य के रूप में… अंतर्दृष्टि से देखता है… उसे विषय बनाकर {J(gr, 'm')} राग उत्पन्न होता है… उदासी उत्पन्न होती है। {KXn(pr, gr)} {NL('cetopariyañāṇassa', 'anāgataṃsañāṇassa', 'āvajjanāya')} {I('ārammaṇa', 'mp')}। (3)",
    # adhipati ^7-20-23
    PN(D(ar), DT(ar), "adhipati") + f" – {ARAM}, {SAHA}। {ARAM} – अतीत के अनंत चेतना के क्षेत्र {GK}, {NEVA_O} {GK}। {J(ar, 'o')}, अतीत के अलौकिक शक्तियों के ज्ञान {GK}, दूसरों के मन को जानने के ज्ञान… पूर्व जन्मों के अनुस्मरण के ज्ञान… प्राणियों के अपने कर्मों के अनुसार जाने के ज्ञान {GK}। {KX(ar, ar)} को महत्व देकर {SAVp}, उसे महत्व देकर {J(ar, 'm')} राग उत्पन्न होता है, दृष्टि उत्पन्न होती है। {SAHA} – {J(ar)} प्रधानता {SK} {I('adhipati')}। (1)",
    PN(D(ar), DT(gr), "adhipati") + f"। {ARAM} – भविष्य के अनंत चेतना के क्षेत्र को महत्व देकर… {NEVA_O} … {J(ar, 'o')}, भविष्य के अलौकिक शक्तियों के ज्ञान को महत्व देकर… दूसरों के मन को जानने के ज्ञान… पूर्व जन्मों के अनुस्मरण के ज्ञान… प्राणियों के अपने कर्मों के अनुसार जाने के ज्ञान… {KX(ar, gr)} को महत्व देकर {SAVp}; उसे महत्व देकर {J(gr, 'm')} राग उत्पन्न होता है, दृष्टि उत्पन्न होती है। (2)",
    PN(D(gr), DT(gr), "adhipati") + f" – {ARAM}, {SAHA}। {ARAM} – {J(gr, 'o')}, भविष्य के अलौकिक शक्तियों के ज्ञान को महत्व देकर… दूसरों के मन को जानने के ज्ञान… भविष्य को जानने के ज्ञान {GK}। {KX(gr, gr)} को महत्व देकर {SAVp}; उसे महत्व देकर {J(gr, 'm')} राग उत्पन्न होता है, दृष्टि उत्पन्न होती है। {SAHA} – {J(gr)} प्रधानता {SK} {I('adhipati')}। (1)",
    PN(D(gr), DT(ar), "adhipati") + f"। {ARAM} – {J(gr, 'o')}, अतीत के अलौकिक शक्तियों के ज्ञान को महत्व देकर… दूसरों के मन को जानने के ज्ञान… भविष्य को जानने के ज्ञान को महत्व देकर… {KX(gr, ar)} को महत्व देकर {SAVp}; उसे महत्व देकर {J(ar, 'm')} राग उत्पन्न होता है, दृष्टि उत्पन्न होती है। (2)",
    PN(D(pr), DT(pr), "adhipati") + f"। {SAHA} – {J(pr)} प्रधानता {SK} {I('adhipati')}। (1)",
    PN(D(pr), DT(ar), "adhipati") + f"। {ARAM} – अतीत की दिव्य आँख {GK}, दिव्य कान के तत्व {GK}, {J(pr, 'o')}, अतीत के अलौकिक शक्तियों के ज्ञान को महत्व देकर… दूसरों के मन को जानने के ज्ञान को महत्व देकर… {KX(pr, ar)} को महत्व देकर {SAVp}; उसे महत्व देकर {J(ar, 'm')} राग उत्पन्न होता है, दृष्टि उत्पन्न होती है। (2)",
    PN(D(pr), DT(gr), "adhipati") + f"। {ARAM} – भविष्य की दिव्य आँख {GK}, दिव्य कान के तत्व को महत्व देकर … {J(pr, 'o')}, भविष्य के अलौकिक शक्तियों के ज्ञान को महत्व देकर… दूसरों के मन को जानने के ज्ञान को महत्व देकर… {KX(pr, gr)} को महत्व देकर {SAVp}; उसे महत्व देकर {J(gr, 'm')} राग उत्पन्न होता है, दृष्टि उत्पन्न होती है। (3)",
    # anantara ^7-20-26
    PN(D(ar), DT(ar), "anantara") + f" – {PUR(ar, ar)} {I('anantara', 'mp')}। (1)",
    PN(D(ar), DT(gr), "anantara") + f" – {J(ar)} जीवन-धारा {J(gr, 'o')} मन को विषय की ओर मोड़ने के लिए {I('anantara')}। (2)",
    PN(D(ar), DT(pr), "anantara") + f" – {J(ar, 'm')} मृत्यु का मन {J(pr, 'o')} पुनर्जन्म के मन के लिए {I('anantara', 'ms')}। {J(ar)} जीवन-धारा {J(pr, 'o')} मन को विषय की ओर मोड़ने के लिए {I('anantara')}। (3)",
    PN(D(gr), DT(gr), "anantara") + f" – {PUR(gr, gr)} {I('anantara', 'mp')}। (1)",
    PN(D(gr), DT(ar), "anantara") + f" – {J(gr, 'm')} अलौकिक शक्तियों का ज्ञान {J(ar, 'o')} बाहर आने के लिए… दूसरों के मन को जानने का ज्ञान {J(ar, 'o')} बाहर आने के लिए… भविष्य को जानने का ज्ञान {J(ar, 'o')} बाहर आने के लिए… {KN(gr)} {J(ar, 'o')} बाहर आने के लिए {I('anantara', 'mp')}। (2)",
    PN(D(pr), DT(pr), "anantara") + f" – {PUR(pr, pr)} {I('anantara', 'mp')}। {J(pr, 'm')} पुनर्जन्म का मन {J(pr)} जीवन-धारा के लिए… {J(pr)} जीवन-धारा {J(pr)} जीवन-धारा के लिए {I('anantara')}। (1)",
    PN(D(pr), DT(ar), "anantara") + f" – {J(pr, 'm')} पुनर्जन्म का मन {J(ar)} जीवन-धारा के लिए… {J(pr)} जीवन-धारा {J(ar)} जीवन-धारा के लिए… {KN(pr)} {J(ar, 'o')} बाहर आने के लिए {I('anantara', 'mp')}। (2)",
    PN(D(ar), DT(ar), "samanantara") + " (निकटता-कारण के समान)।",
    UD(D(ar), DT(ar), ["sahajāta", "aññamañña", "nissaya"]) + "…(तीनों कारण भी निर्भरता के खंड के समान हैं)।",
    # upanissaya ^7-20-31
    PN(D(ar), DT(ar), "upanissaya") + f" – {UPA}, {UPN}, {UPP}…। {UPP} – {ANU(ar, ar)}। (1)",
    PN(D(ar), DT(gr), "upanissaya") + f" – {UPA}, {UPN}, {UPP}…। {UPP} – {ANU(ar, gr)}। (2)",
    PN(D(ar), DT(pr), "upanissaya") + f" – {UPN}, {UPP}…। {UPP} – {ANU(ar, pr)}। (3)",
    PN(D(gr), DT(gr), "upanissaya") + f" – {UPA}, {UPN}, {UPP}…। {UPP} – {ANU(gr, gr)}। (1)",
    PN(D(gr), DT(ar), "upanissaya") + f" – {UPA}, {UPN}, {UPP}…। {UPP} – {ANU(gr, ar)}। (2)",
    PN(D(gr), DT(pr), "upanissaya") + f"। {UPP} – {ANU(gr, pr)}। (3)",
    PN(D(pr), DT(pr), "upanissaya") + f" – {UPN}, {UPP}…। {UPP} – {ANU(pr, pr)}। (1)",
    PN(D(pr), DT(ar), "upanissaya") + f" – {UPA}, {UPN}, {UPP}…। {UPP} – {ANU(pr, ar)}। (2)",
    PN(D(pr), DT(gr), "upanissaya") + f" – {UPA}, {UPP}…। {UPP} – {ANU(pr, gr)}। (3)",
    # āsevana ^7-20-34
    PN(D(ar), DT(ar), "āsevana") + f" – {PUR(ar, ar)} {I('āsevana', 'mp')}। (1)",
    PN(D(gr), DT(gr), "āsevana") + f" – {PUR(gr, gr)} {I('āsevana', 'mp')}। (1)",
    PN(D(pr), DT(pr), "āsevana") + f" – {PUR(pr, pr)} {I('āsevana', 'mp')}। (1)",
    # kamma ^7-20-35
    PN(D(ar), DT(ar), "kamma") + f" – सह-उत्पत्ति, भिन्न क्षण। सह-उत्पत्ति – {J(ar, 'm')} इरादा {SK} {I('kamma', 'ms')}। {PK}…। भिन्न क्षण – {J(ar, 'm')} इरादा {VIP(ar)} {I('kamma', 'ms')}। (1)",
    PN(D(ar), DT(gr), "kamma") + f"। भिन्न क्षण – {J(ar, 'm')} इरादा {VIP(gr)} {I('kamma', 'ms')}। (2)",
    PN(D(ar), DT(pr), "kamma") + f"। भिन्न क्षण – {J(ar, 'm')} इरादा {VIP(pr)} {I('kamma', 'ms')}। (3)",
    PN(D(gr), DT(gr), "kamma") + f" – सह-उत्पत्ति, भिन्न क्षण। सह-उत्पत्ति – {J(gr, 'm')} इरादा {SK} {I('kamma', 'ms')}। भिन्न क्षण – {J(gr, 'm')} इरादा {VIP(gr)} {I('kamma', 'ms')}। (1)",
    PN(D(gr), DT(ar), "kamma") + f"। भिन्न क्षण – {J(gr, 'm')} इरादा {VIP(ar)} {I('kamma', 'ms')}। (2)",
    PN(D(gr), DT(pr), "kamma") + f"। भिन्न क्षण – {J(gr, 'm')} इरादा {VIP(pr)} {I('kamma', 'ms')}। (3)",
    PN(D(pr), DT(pr), "kamma") + f" – सह-उत्पत्ति, भिन्न क्षण। सह-उत्पत्ति – {J(pr, 'm')} इरादा {SK} {I('kamma', 'ms')}। {PK}… भिन्न क्षण – {J(pr, 'm')} इरादा {VIP(pr)} {I('kamma', 'ms')}। (1)",
    PN(D(pr), DT(ar), "kamma") + f"। भिन्न क्षण – {J(pr, 'm')} इरादा {VIP(ar)} {I('kamma', 'ms')}। (2)",
    PN(D(pr), DT(gr), "kamma") + f"। भिन्न क्षण – {J(pr, 'm')} इरादा {VIP(gr)} {I('kamma', 'ms')}। (3)",
    UD(D(ar), DT(ar), ["vipāka", "āhāra", "indriya", "jhāna", "magga", "sampayutta", "atthi", "natthi", "vigata", "avigata"]) + "।",
    # Paccanīyuddhāra ^7-20-40
    UD(D(ar), DT(ar), ["ārammaṇa", "sahajāta", "upanissaya", "kamma"]) + "। (1)",
    UD(D(ar), DT(gr), ["ārammaṇa", "upanissaya", "kamma"]) + "। (2)",
    UD(D(ar), DT(pr), ["ārammaṇa", "upanissaya", "kamma"]) + "। (3)",
    UD(D(gr), DT(gr), ["ārammaṇa", "sahajāta", "upanissaya", "kamma"]) + "। (1)",
    UD(D(gr), DT(ar), ["ārammaṇa", "upanissaya", "kamma"]) + "। (2)",
    UD(D(gr), DT(pr), ["ārammaṇa", "upanissaya", "kamma"]) + "। (3)",
    UD(D(pr), DT(pr), ["ārammaṇa", "sahajāta", "upanissaya", "kamma"]) + "। (1)",
    UD(D(pr), DT(ar), ["ārammaṇa", "upanissaya", "kamma"]) + "। (2)",
    UD(D(pr), DT(gr), ["ārammaṇa", "upanissaya", "kamma"]) + "। (3)",
]
