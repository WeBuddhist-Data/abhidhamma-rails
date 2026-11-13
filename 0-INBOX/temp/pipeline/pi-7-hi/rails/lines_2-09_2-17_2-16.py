# 2-16 Ajjhattārammaṇattika: hand lines (exec'd by build_rails_2-09_2-17.py)
jr, br = "jr", "br"
AJ, BA = "स्वयं से संबंधित", "दूसरों से संबंधित"


def UD(x, y, keys, g="fs"):
    return f"{x}, {y} " + "… ".join(I(k, g) for k in keys)


def AH(c):
    return f"मूल से रहित, {J(c, 'o')} एक समूह"


SAHA, ARAM = LAB["ādh_s"], LAB["ādh_ā"]
UPA, UPN, UPP = LAB["up_ā"], LAB["up_a"], LAB["up_p"]
RV, RVp = "पुनः विचार करता है", "पुनः विचार करते हैं"
GK = "को महत्व देकर"
NEVA_O = "न पहचान न अ-पहचान के क्षेत्र"
KN5 = "अलौकिक शक्तियों के ज्ञान… पूर्व जन्मों के अनुस्मरण के ज्ञान… प्राणियों के अपने कर्मों के अनुसार जाने के ज्ञान… भविष्य को जानने के ज्ञान"


def ANU(c1, c2, comma=""):
    return (f"{J(c1, 'o')} अनित्यता का अवलोकन, दुःख का अवलोकन और आत्मा से रहित होने का अवलोकन{comma} {J(c2, 'o')} "
            f"अनित्यता के अवलोकन, दुःख के अवलोकन और आत्मा से रहित होने के अवलोकन के लिए {I('upanissaya', 'mp')}")


def PUR(c1, c2):
    return f"पहले-पहले के {KN(c1)} बाद-बाद के {KH(c2)} के लिए"


def VIP(c):
    return f"कर्म-फल रूपी, {J(c, 'o')} समूहों के लिए"


def KX(c1, x):
    return f"{J(c1, 'o')}, {x} समूहों"


def KXn(c1, x):
    return f"{J(c1, 'o')}, {x} समूह"


L = [
    # ^7-22-1
    PT(D(jr), D(jr), "hetu") + f" – {ONE(jr)} {B1} तीन समूह… दो समूहों… {PK} {ONE(jr)} {B1} तीन समूह… दो समूहों…। (1)",
    PT(D(br), D(br), "hetu") + f" – {ONE(br)} {B1} तीन समूह… दो समूहों… {PK} {ONE(br)} {B1} तीन समूह… दो समूहों…। (1)",
    PT(D(jr), D(jr), f"{A['ārammaṇa']}… {A['avigata']}") + " (संक्षिप्त)।",
    # paccanīya ^7-22-4
    PT(D(jr), D(jr), "na:hetu") + f" – {AH(jr)} {B1} तीन समूह… दो समूहों… {APK} {ONE(jr)} {B1} तीन समूह… दो समूहों… {MOHA}। (1)",
    PT(D(br), D(br), "na:hetu") + f" – {AH(br)} {B1} तीन समूह… दो समूहों… {APK}… {MOHA}। (1)",
    PT(D(jr), D(jr), f"{NA['adhipati']} … (सकारात्मक क्रम के सह-उत्पत्ति-कारण के समान, बिना किसी अंतर के) {NA['purejāta']}") + f" – {ARU} {ONE(jr)} {B1}… {PK}…। (1)",
    PT(D(br), D(br), "na:purejāta") + f" – {ARU} {ONE(br)} {B1} तीन समूह…। {PK}… {NA['pacchājāta']}… {NA['āsevana']}… (सह-उत्पत्ति-कारण के समान) {NA['kamma']} – {KH(jr)} {B1} {J(jr, 'm')} इरादा।",
    PT(D(br), D(br), "na:kamma") + f" – {KH(br)} {B1} {J(br, 'm')} इरादा।",
    PT(D(jr), D(jr), f"{NA['vipāka']} (पुनर्जन्म नहीं है)… {NA['jhāna']}") + f"… पाँच प्रकार की चेतना के साथ होने वाला, {J(jr, 'm')} एक…। (1)",
    PT(D(br), D(br), "na:jhāna") + f" – पाँच प्रकार की चेतना के साथ होने वाले, {J(br, 'o')} एक समूह {B1} तीन समूह… {NA['magga']} (मूल-कारण के अभाव के समान। मोह नहीं है)… {NA['vippayutta']} – {ARU} {ONE(jr)} {B1} तीन समूह…। (1)",
    PT(D(br), D(br), "na:vippayutta") + f" – {ARU} {ONE(br)} {B1} तीन समूह…। (1)",
    # ^7-U319
    "(सह-उत्पत्ति का खंड, कारण का खंड, आश्रय का खंड, घुले-मिले होने का खंड और जुड़ाव का खंड भी निर्भरता के खंड के समान हैं।)",
    # Pañhāvāra ^7-22-11
    PN(D(jr), DT(jr), "hetu") + f" – {J(jr, 'o')} मूल {SK} {I('hetu', 'mp')}। {PK} {J(jr, 'o')} मूल {SK} {I('hetu', 'mp')}। (1)",
    PN(D(br), DT(br), "hetu") + f" – {J(br, 'o')} मूल जुड़े हुए समूहों के लिए… {PK}…। (1)",
    # ārammaṇa ^7-22-12
    PN(D(jr), DT(jr), "ārammaṇa") + f" – {AJ} अनंत चेतना के क्षेत्र पर {RV}, {NEVA_O} पर {RV}, {J(jr)}, {AJ} दिव्य आँख पर {RV}, दिव्य कान के तत्व… {KN5} पर {RV}। आर्य {J(jr, 'o')}, {KIL_P} पर {RVp}, {KIL_V} पर {RVp}, {KIL_S} को जानते हैं। {KX(jr, AJ)} को अनित्य के रूप में… अंतर्दृष्टि से देखता है, {SAVp}, उसे विषय बनाकर {J(jr, 'm')} राग उत्पन्न होता है… उदासी उत्पन्न होती है। {KXn(jr, AJ)} {NL('pubbenivāsānussatiñāṇassa', 'yathākammūpagañāṇassa', 'anāgataṃsañāṇassa', 'āvajjanāya')} {I('ārammaṇa', 'mp')}। (1)",
    PN(D(jr), DT(br), "ārammaṇa") + f" – {BA} अनंत चेतना के क्षेत्र पर {RV}, {NEVA_O} पर {RV}। {J(jr)}, {BA} दिव्य आँख पर {RV}, दिव्य कान के तत्व… {KN5} पर {RV}, {KX(jr, BA)} को {ANI} अंतर्दृष्टि से देखता है… {CETO} {J(jr, 'o')}, {BA} मन से युक्त व्यक्ति के मन को जानता है, {KXn(jr, BA)} {NL('cetopariyañāṇassa', 'pubbenivāsānussatiñāṇassa', 'yathākammūpagañāṇassa', 'anāgataṃsañāṇassa', 'āvajjanāya')} {I('ārammaṇa', 'mp')}। (2)",
    PN(D(br), DT(br), "ārammaṇa") + f" – {J(br)}, {BA} दिव्य आँख पर {RV}, दिव्य कान के तत्व पर {RV}। अलौकिक शक्तियों के ज्ञान… दूसरों के मन को जानने के ज्ञान… पूर्व जन्मों के अनुस्मरण के ज्ञान… प्राणियों के अपने कर्मों के अनुसार जाने के ज्ञान… भविष्य को जानने के ज्ञान पर {RV}। {KX(br, BA)} को {ANI} अंतर्दृष्टि से देखता है… {CETO} {J(br, 'o')}, {BA} मन से युक्त व्यक्ति के मन को जानता है। {KXn(br, BA)} {NL('cetopariyañāṇassa', 'pubbenivāsānussatiñāṇassa', 'yathākammūpagañāṇassa', 'anāgataṃsañāṇassa', 'āvajjanāya')} {I('ārammaṇa', 'mp')}। (1)",
    PN(D(br), DT(jr), "ārammaṇa") + f" – {GIFT} उस पर {RV}, {DEEDS} पर {RV}, ध्यान से उठकर ध्यान पर {RV}। आर्य मार्ग से उठकर मार्ग पर {RVp}, फल पर {RVp}, {J(br, 'o')}, {KIL_P} पर {RVp}, {KIL_V} पर {RVp}, {KIL_S} को जानते हैं। {J(br)}, {AJ} दिव्य आँख पर {RV}, दिव्य कान के तत्व… अलौकिक शक्तियों के ज्ञान… दूसरों के मन को जानने के ज्ञान… पूर्व जन्मों के अनुस्मरण के ज्ञान… प्राणियों के अपने कर्मों के अनुसार जाने के ज्ञान… भविष्य को जानने के ज्ञान… {KX(br, AJ)} को अनित्य के रूप में… अंतर्दृष्टि से देखता है, {SAVp}, उसे विषय बनाकर {J(jr, 'm')} राग उत्पन्न होता है… उदासी उत्पन्न होती है। {KXn(br, AJ)} {NL('iddhividhañāṇassa', 'pubbenivāsānussatiñāṇassa', 'yathākammūpagañāṇassa', 'anāgataṃsañāṇassa', 'āvajjanāya')} {I('ārammaṇa', 'mp')}। (2)",
    # adhipati ^7-22-14
    PN(D(jr), DT(jr), "adhipati") + f" – {ARAM}, {SAHA}। {ARAM} – {AJ} अनंत चेतना के क्षेत्र {GK} {RV}, {NEVA_O} {GK} {RV}। {J(jr)}, {AJ} दिव्य आँख {GK}… दिव्य कान के तत्व… अलौकिक शक्तियों के ज्ञान… पूर्व जन्मों के अनुस्मरण के ज्ञान… प्राणियों के अपने कर्मों के अनुसार जाने के ज्ञान… भविष्य को जानने के ज्ञान {GK}… {KX(jr, AJ)} {GK} {SAVp}, उसे महत्व देकर {J(jr, 'm')} राग उत्पन्न होता है, दृष्टि उत्पन्न होती है। {SAHA} – {J(jr)} प्रधानता {SK} {I('adhipati')}। (1)",
    PN(D(br), DT(br), "adhipati") + f"। {SAHA} – {J(br)} प्रधानता {SK} {I('adhipati')}। (1)",
    PN(D(br), DT(jr), "adhipati") + f"। {ARAM} – {GIFT} उसे महत्व देकर {RV}, {DEEDS}… ध्यान से उठकर… आर्य मार्ग से उठकर मार्ग… फल {GK} {RVp}। {J(br)}, {AJ} दिव्य आँख {GK}… दिव्य कान के तत्व… अलौकिक शक्तियों के ज्ञान… दूसरों के मन को जानने के ज्ञान… पूर्व जन्मों के अनुस्मरण के ज्ञान… प्राणियों के अपने कर्मों के अनुसार जाने के ज्ञान… भविष्य को जानने के ज्ञान {GK} {RV}, {KX(br, AJ)} {GK} {SAVp}, उसे महत्व देकर {J(jr, 'm')} राग उत्पन्न होता है, दृष्टि उत्पन्न होती है। (2)",
    # anantara ^7-22-16
    PN(D(jr), DT(jr), "anantara") + f" – {PUR(jr, jr)} {I('anantara', 'mp')}। (1)",
    PN(D(jr), DT(br), "anantara") + f" – {J(jr, 'm')} मृत्यु का मन {J(br, 'o')} जन्म के मन के लिए {I('anantara', 'ms')}। {J(jr)} जीवन-धारा {J(br, 'o')} मन को विषय की ओर मोड़ने के लिए {I('anantara')}। {KN(jr)} {J(br, 'o')} बाहर आने के लिए {I('anantara', 'mp')}। {J(jr)} अनुरूपता गोत्र-परिवर्तन के लिए… अनुरूपता शुद्धि के लिए… अनुरूपता {FS}… {NIRODHA}… {NEVA} {FS} {I('anantara', 'ms')}। (2)",
    PN(D(br), DT(br), "anantara") + f" – {PUR(br, br)} {I('anantara', 'mp')}। {J(br)} {ANULOMA4}… मार्ग फल के लिए… फल फल के लिए… अनुरूपता {FS} {I('anantara')}। (1)",
    PN(D(br), DT(jr), "anantara") + f" – {J(br, 'm')} मृत्यु का मन {J(jr, 'o')} जन्म के मन के लिए {I('anantara', 'ms')}। {J(br)} जीवन-धारा {J(jr, 'o')} मन को विषय की ओर मोड़ने के लिए {I('anantara')}। {KN(br)} {J(jr, 'o')} बाहर आने के लिए {I('anantara', 'mp')}। (2)",
    UD(D(jr), DT(jr), ["samanantara", "sahajāta", "aññamañña", "nissaya"]) + "।",
    # upanissaya ^7-22-19
    PN(D(jr), DT(jr), "upanissaya") + f" – {UPA}, {UPN}, {UPP}…। {UPP} – {ANU(jr, jr, ',')}। (1)",
    PN(D(jr), DT(br), "upanissaya") + f" – {UPN}, {UPP}…। {UPP} – {ANU(jr, br)}। (2)",
    PN(D(br), DT(br), "upanissaya") + f" – {UPN}, {UPP}…। {UPP} – {ANU(br, br)}। (1)",
    PN(D(br), DT(jr), "upanissaya") + f" – {UPA}, {UPN}, {UPP}…। {UPP} – {ANU(br, jr)}। (2)",
    # āsevana ^7-22-21
    PN(D(jr), DT(jr), "āsevana") + f" – {PUR(jr, jr)} {I('āsevana', 'mp')}। (1)",
    PN(D(jr), DT(br), "āsevana") + f" – {J(jr)} अनुरूपता गोत्र-परिवर्तन के लिए, अनुरूपता शुद्धि के लिए {I('āsevana')}। (2)",
    PN(D(br), DT(br), "āsevana") + f" – {PUR(br, br)} {I('āsevana', 'mp')}। {J(br)} {ANULOMA4} {I('āsevana')}। (1)",
    # kamma ^7-22-22
    PN(D(jr), DT(jr), "kamma") + f" – सह-उत्पत्ति, भिन्न क्षण। सह-उत्पत्ति – {J(jr, 'm')} इरादा {SK} {I('kamma', 'ms')}। {PK}…। भिन्न क्षण – {J(jr, 'm')} इरादा {VIP(jr)} {I('kamma', 'ms')}। (1)",
    PN(D(jr), DT(br), "kamma") + f"। भिन्न क्षण – {J(jr, 'm')} इरादा {VIP(br)} {I('kamma', 'ms')}। (2)",
    PN(D(br), DT(br), "kamma") + f" – सह-उत्पत्ति, भिन्न क्षण। सह-उत्पत्ति – {J(br, 'm')} इरादा {SK} {I('kamma', 'ms')}। {PK}…। भिन्न क्षण – {J(br, 'm')} इरादा {VIP(br)} {I('kamma', 'ms')}। (1)",
    PN(D(br), DT(jr), "kamma") + f"। भिन्न क्षण – {J(br, 'm')} इरादा {VIP(jr)} {I('kamma', 'ms')}। (2)",
    UD(D(jr), DT(jr), ["vipāka", "āhāra", "indriya", "jhāna", "magga", "sampayutta", "atthi", "natthi", "vigata", "avigata"]) + "।",
    # Paccanīyuddhāra ^7-22-25
    UD(D(jr), DT(jr), ["ārammaṇa", "sahajāta", "upanissaya", "kamma"]) + "। (1)",
    UD(D(jr), DT(br), ["ārammaṇa", "upanissaya", "kamma"]) + "। (2)",
    UD(D(br), DT(br), ["ārammaṇa", "sahajāta", "upanissaya", "kamma"]) + "। (1)",
    UD(D(br), DT(jr), ["ārammaṇa", "upanissaya", "kamma"]) + "। (2)",
]
