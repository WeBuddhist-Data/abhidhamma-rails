# 2-11 Maggārammaṇattika: hand lines (exec'd by build_rails_2-09_2-17.py)
mr, mh, md = "mr", "mh", "md"


def UD(x, y, keys, g="fs"):
    return f"{x}, {y} " + "… ".join(I(k, g) for k in keys)


def AH(c):
    return f"मूल से रहित, {J(c, 'o')} एक समूह"


def ONEc(c1, c2):
    return f"{J(c1, 'o')} और {J(c2, 'o')} एक समूह"


def ADJo(*cs):
    return " और ".join(J(c, "o") for c in cs)


def BOD(one, adj=None, n=""):
    return f"{one} {B1} " + (adj + " " if adj else "") + f"तीन समूह… दो समूहों…। ({n})"


def SKX(*cs):
    return f"जुड़े हुए, {ADJo(*cs)} समूहों के लिए"


def ADH(*cs):
    return " और ".join(J(c) for c in cs) + " प्रधानता"


SAHA, ARAM = LAB["ādh_s"], LAB["ādh_ā"]
UPA, UPN, UPP = LAB["up_ā"], LAB["up_a"], LAB["up_p"]
AG = "आर्य मार्ग से उठकर मार्ग को महत्व देकर पुनः विचार करते हैं"
AP = "आर्य मार्ग से उठकर मार्ग पर पुनः विचार करते हैं"
PV = f"पुनः विचार, पुनः विचार के लिए {I('upanissaya', 'ms')}"
MG1 = f"पहला मार्ग दूसरे मार्ग के लिए {I('upanissaya', 'ms')}… तीसरा मार्ग चौथे मार्ग के लिए {I('upanissaya', 'ms')}"
MG2 = f"पहला मार्ग दूसरे मार्ग के लिए… तीसरा मार्ग चौथे मार्ग के लिए {I('upanissaya', 'ms')}"
NL4 = NL("cetopariyañāṇassa", "pubbenivāsānussatiñāṇassa", "anāgataṃsañāṇassa", "āvajjanāya")
CH11 = R.CH("ārammaṇapaccayā… adhipatipaccayā… anantarapaccayā… samanantarapaccayā… sahajātapaccayā… "
            "aññamaññapaccayā… nissayapaccayā… upanissayapaccayā… purejātapaccayā… āsevanapaccayā… kammapaccayā… "
            "āhārapaccayā… indriyapaccayā… jhānapaccayā… maggapaccayā… sampayuttapaccayā… vippayuttapaccayā… "
            "atthipaccayā… natthipaccayā… vigatapaccayā… avigatapaccayā")


def ICE(c, *names):
    return f"{CETO} {ADJo(*names)} मन से युक्त व्यक्ति के मन को जानते हैं"


L = [
    # ^7-17-1
    PT(D(mr), D(mr), "hetu") + " – " + BOD(ONE(mr), None, 1),
    PT(D(mr), D(md), "hetu") + f" – {ONE(mr)} {B1} {J(md, 'o')} तीन समूह, तीन समूहों {B1} एक समूह। दो समूहों…। (2)",
    PT(D(mr), DP(mr, md), "hetu") + " – " + BOD(ONE(mr), ADJo(mr, md), 3),
    PT(D(mh), D(mh), "hetu") + " – " + BOD(ONE(mh), None, 1),
    PT(D(mh), D(md), "hetu") + " – " + BOD(ONE(mh), ADJo(md), 2),
    PT(D(mh), DP(mh, md), "hetu") + " – " + BOD(ONE(mh), ADJo(mh, md), 3),
    PT(D(md), D(md), "hetu") + " – " + BOD(ONE(md), None, 1),
    PT(D(md), D(mr), "hetu") + " – " + BOD(ONE(md), ADJo(mr), 2),
    PT(D(md), D(mh), "hetu") + " – " + BOD(ONE(md), ADJo(mh), 3),
    PT(D(md), DP(mr, md), "hetu") + " – " + BOD(ONE(md), ADJo(mr, md), 4),
    PT(D(md), DP(mh, md), "hetu") + " – " + BOD(ONE(md), ADJo(mh, md), 5),
    PT(D2(mr, md), D(mr), "hetu") + " – " + BOD(ONEc(mr, md), ADJo(mr), 1),
    PT(D2(mr, md), D(md), "hetu") + " – " + BOD(ONEc(mr, md), ADJo(md), 2),
    PT(D2(mr, md), DP(mr, md), "hetu") + " – " + BOD(ONEc(mr, md), ADJo(mr, md), 3),
    PT(D2(mh, md), D(mh), "hetu") + " – " + BOD(ONEc(mh, md), ADJo(mh), 1),
    PT(D2(mh, md), D(md), "hetu") + " – " + BOD(ONEc(mh, md), ADJo(md), 2),
    PT(D2(mh, md), DP(mh, md), "hetu") + " – " + BOD(ONEc(mh, md), ADJo(mh, md), 3),
    # ^7-17-6
    PT(D(mr), D(mr), CH11) + "।",
    # paccanīya ^7-17-8
    PT(D(mr), D(mr), "na:hetu") + " – " + BOD(AH(mr), None, 1),
    PT(D(mr), D(mr), "na:adhipati") + " – " + BOD(ONE(mr), None, 1),
    PT(D(mr), D(md), "na:adhipati") + " – " + BOD(ONE(mr), ADJo(md), 2),
    PT(D(mr), DP(mr, md), "na:adhipati") + " – " + BOD(ONE(mr), ADJo(mr, md), 3),
    PT(D(mh), D(mh), "na:adhipati") + f" – {KH(mh)} {B1} {ADH(mh)}। (1)",
    PT(D(mh), D(md), "na:adhipati") + f" – {KH(mh)} {B1} {ADH(md)}। (2)",
    PT(D(mh), DP(mh, md), "na:adhipati") + f" – {KH(mh)} {B1} {ADH(mh, md)}। (3)",
    PT(D(md), D(md), "na:adhipati") + f" – {KH(md)} {B1} {ADH(md)}। " + BOD(ONE(md), None, 1),
    PT(D(md), D(mr), "na:adhipati") + " – " + BOD(ONE(md), ADJo(mr), 2),
    PT(D(md), D(mh), "na:adhipati") + f" – {KH(md)} {B1} {ADH(mh)}। (3)",
    PT(D(md), DP(mr, md), "na:adhipati") + " – " + BOD(ONE(md), ADJo(mr, md), 4),
    PT(D(md), DP(mh, md), "na:adhipati") + f" – {KH(md)} {B1} {ADH(mh, md)}। (5)",
    PT(D2(mr, md), D(mr), "na:adhipati") + " – " + BOD(ONEc(mr, md), ADJo(mr), 1),
    PT(D2(mr, md), D(md), "na:adhipati") + " – " + BOD(ONEc(mr, md), ADJo(md), 2),
    PT(D2(mr, md), DP(mr, md), "na:adhipati") + " – " + BOD(ONEc(mr, md), ADJo(mr, md), 3),
    PT(D2(mh, md), D(mh), "na:adhipati") + f" – {ADJo(mh, md)} समूहों {B1} {ADH(mh)}। (1)",
    PT(D2(mh, md), D(md), "na:adhipati") + f" – {ADJo(mh, md)} समूहों {B1} {ADH(md)}। (2)",
    PT(D2(mh, md), DP(mh, md), "na:adhipati") + f" – {ADJo(mh, md)} समूहों {B1} {ADH(mh, md)}। (3)",
    PT(D(mr), D(mr), f"{NA['purejāta']}… {NA['pacchājāta']}") + " (दोनों परिपूर्ण)।",
    PT(D(mr), D(mr), "na:āsevana") + " – " + BOD(ONE(mr), None, 1),
    PT(D(mr), D(md), "na:āsevana") + " – " + BOD(ONE(mr), ADJo(md), 2),
    PT(D(mr), DP(mr, md), "na:āsevana") + " – " + BOD(ONE(mr), ADJo(mr, md), 3),
    PT(D(md), D(md), "na:āsevana") + " – " + BOD(ONE(md), None, 1),
    PT(D(md), D(mr), "na:āsevana") + " – " + BOD(ONE(md), ADJo(mr), 2),
    PT(D(md), DP(mr, md), "na:āsevana") + " – " + BOD(ONE(md), ADJo(mr, md), 3),
    PT(D2(mr, md), D(mr), "na:āsevana") + " – " + BOD(ONEc(mr, md), ADJo(mr), 1),
    PT(D2(mr, md), D(md), "na:āsevana") + " – " + BOD(ONEc(mr, md), ADJo(md), 2),
    PT(D2(mr, md), DP(mr, md), "na:āsevana") + " – " + BOD(ONEc(mr, md), ADJo(mr, md), 3),
    PT(D(mr), D(mr), "na:kamma") + f" – {KH(mr)} {B1} {J(mr, 'm')} इरादा। (1)",
    PT(D(mr), D(md), "na:kamma") + f" – {KH(mr)} {B1} {J(md, 'm')} इरादा। (2)",
    PT(D(mr), DP(mr, md), "na:kamma") + f" – {KH(mr)} {B1} {J(mr, 'm')} और {J(md, 'm')} इरादा। (3)",
    PT(D(mh), D(mh), "na:kamma") + f" – {KH(mh)} {B1} {J(mh, 'm')} इरादा। (1)",
    PT(D(mh), D(md), "na:kamma") + f" – {KH(mh)} {B1} {J(md, 'm')} इरादा। (2)",
    PT(D(mh), DP(mh, md), "na:kamma") + f" – {KH(mh)} {B1} {J(mh, 'm')} और {J(md, 'm')} इरादा। (3)",
    PT(D(md), D(md), "na:kamma") + f" – {KH(md)} {B1} {J(md, 'm')} इरादा (पाँच प्रश्न)।",
    PT(D2(mr, md), D(mr), "na:kamma") + " (पहले संयोजन में तीन)।",
    PT(D2(mh, md), D(mh), "na:kamma") + " (दूसरे संयोजन में तीन प्रश्न)।",
    PT(D(mr), D(mr), "na:vipāka") + " (परिपूर्ण)।",
    PT(D(mr), D(mr), "na:magga") + " – " + BOD(AH(mr), None, 1),
    PT(D(mr), D(mr), "na:vippayutta") + " (परिपूर्ण, “अभौतिक लोक में” ऐसा निश्चित करना चाहिए)।",
    # ^7-U315
    "(सह-उत्पत्ति का खंड, कारण का खंड, आश्रय का खंड, घुले-मिले होने का खंड और जुड़ाव का खंड भी निर्भरता के खंड के समान हैं।)",
    # Pañhāvāra hetu ^7-17-27
    PN(D(mr), DT(mr), "hetu") + f" – {J(mr, 'o')} मूल {SK} {I('hetu', 'mp')}। (1)",
    PN(D(mr), DT(md), "hetu") + f" – {J(mr, 'o')} मूल {SKX(md)} {I('hetu', 'mp')}। (2)",
    PN(D(mr), DT(mr, md), "hetu") + " (इस तरीके से सत्रह प्रश्न करने चाहिए)।",
    # ārammaṇa ^7-17-28
    PN(D(mh), DT(mr), "ārammaṇa") + f" – {AP}, {ICE(0, mh)}, {KN(mh)} {NL4} {I('ārammaṇa', 'mp')}। (1)",
    PN(D(mh), DT(md), "ārammaṇa") + f" – {AG}। (2)",
    PN(D(mh), DT(mr, md), "ārammaṇa") + f" – {AG}। (3)",
    PN(D(md), DT(md), "ārammaṇa") + f" – {AG}। (1)",
    PN(D(md), DT(mr), "ārammaṇa") + f" – {AP}, {ICE(0, md)}, {KN(md)} {NL4} {I('ārammaṇa', 'mp')}। (2)",
    PN(D(md), DT(mr, md), "ārammaṇa") + f" – {AG}। (3)",
    PN(DP(mh, md), DT(mr), "ārammaṇa", "fp") + f" – {AP}, {ICE(0, mh, md)}, {ADJo(mh, md)} समूह {NL4} {I('ārammaṇa', 'mp')}। (1)",
    PN(DP(mh, md), DT(md), "ārammaṇa", "fp") + f" – {AG}। (2)",
    PN(DP(mh, md), DT(mr, md), "ārammaṇa", "fp") + f" – {AG}। (3)",
    # adhipati ^7-17-31
    PN(D(mr), DT(mr), "adhipati") + f"। {SAHA} – {ADH(mr)} {SK} {I('adhipati')}। (1)",
    PN(D(mr), DT(md), "adhipati") + f"। {SAHA} – {ADH(mr)} {SKX(md)} {I('adhipati')}। (2)",
    PN(D(mr), DT(mr, md), "adhipati") + f"। {SAHA} – {ADH(mr)} {SKX(mr, md)} {I('adhipati')}। (3)",
    PN(D(mh), DT(mh), "adhipati") + f"। {SAHA} – {ADH(mh)} {SK} {I('adhipati')}। (1)",
    PN(D(mh), DT(mr), "adhipati") + f"। {ARAM} – {AG}। (2)",
    PN(D(mh), DT(md), "adhipati") + f" – {ARAM}, {SAHA}। {ARAM} – {AG}। {SAHA} – {ADH(mh)} {SKX(md)} {I('adhipati')}। (3)",
    PN(D(mh), DT(mr, md), "adhipati") + f"। {ARAM} – {AG}। (4)",
    PN(D(mh), DT(mh, md), "adhipati") + f"। {SAHA} – {ADH(mh)} {SKX(mh, md)} {I('adhipati')}। (5)",
    PN(D(md), DT(md), "adhipati") + f" – {ARAM}, {SAHA}। {ARAM} – {AG}। {SAHA} – {ADH(md)} {SK} {I('adhipati')}। (1)",
    PN(D(md), DT(mr), "adhipati") + f" – {ARAM}, {SAHA}। {ARAM} – {AG}। {SAHA} – {ADH(md)} {SKX(mr)} {I('adhipati')}। (2)",
    PN(D(md), DT(mh), "adhipati") + f"। {SAHA} – {ADH(md)} {SKX(mh)} {I('adhipati')}। (3)",
    PN(D(md), f"{J(mr)} और {J(md)} के लिए", "adhipati") + f" – {ARAM}, {SAHA}। {ARAM} – {AG}। {SAHA} – {ADH(md)} {SKX(mr, md)} {I('adhipati')}। (4)",
    PN(D(md), DT(mh, md), "adhipati") + f"। {SAHA} – {ADH(md)} {SKX(mh, md)} {I('adhipati')}। (5)",
    PN(DP(mr, md), DT(mr), "adhipati", "fp") + f"। {SAHA} – {ADH(mr, md)} {SKX(mr)} {I('adhipati')}। (1)",
    PN(DP(mr, md), DT(md), "adhipati", "fp") + f"। {SAHA} – {ADH(mr, md)} {SKX(md)} {I('adhipati')}। (2)",
    PN(DP(mr, md), DT(mr, md), "adhipati", "fp") + f"। {SAHA} – {ADH(mr, md)} {SKX(mr, md)} {I('adhipati')}। (3)",
    PN(DP(mh, md), DT(mr), "adhipati", "fp") + f"। {ARAM} – {AG}। (1)",
    PN(DP(mh, md), DT(mh), "adhipati", "fp") + f"। {SAHA} – {ADH(mh, md)} {SKX(mh)} {I('adhipati')}। (2)",
    PN(DP(mh, md), DT(md), "adhipati", "fp") + f" – {ARAM}, {SAHA}। {ARAM} – {AG}। {SAHA} – {ADH(mh, md)} {SKX(md)} {I('adhipati')}। (3)",
    PN(DP(mh, md), DT(mr, md), "adhipati", "fp") + f"। {ARAM} – {AG}। (4)",
    PN(DP(mh, md), DT(mh, md), "adhipati", "fp") + f"। {SAHA} – {ADH(mh, md)} {SKX(mh, md)} {I('adhipati')}। (5)",
    # anantara ^7-17-36
    PN(D(mr), DT(mr), "anantara") + f" – पहले-पहले के {KN(mr)} बाद-बाद के {KH(mr)} के लिए {I('anantara', 'mp')}। मन को विषय की ओर मोड़ना {KH(mr)} के लिए {I('anantara', 'ms')}। (1)",
    PN(D(mr), DT(md), "anantara") + f" – पहले-पहले के {KN(mr)} बाद-बाद के {KH(md)} के लिए {I('anantara', 'mp')}। मन को विषय की ओर मोड़ना {KH(md)} के लिए {I('anantara', 'ms')}। (2)",
    PN(D(mr), DT(mr, md), "anantara") + f" – पहले-पहले के {KN(mr)} बाद-बाद के {ADJo(mr, md)} समूहों के लिए {I('anantara', 'mp')}। मन को विषय की ओर मोड़ना {ADJo(mr, md)} समूहों के लिए {I('anantara', 'ms')}। (3)",
    PN(D(md), DT(md), "anantara") + f" – पहले-पहले के {KN(md)} बाद-बाद के {KH(md)} के लिए {I('anantara', 'mp')}। (1)",
    PN(D(md), DT(mr), "anantara") + f" – पहले-पहले के {KN(md)} बाद-बाद के {KH(mr)} के लिए {I('anantara', 'mp')}। (2)",
    PN(D(md), DT(mr, md), "anantara") + f" – पहले-पहले के {KN(md)} बाद-बाद के {ADJo(mr, md)} समूहों के लिए {I('anantara', 'mp')}। (3)",
    PN(DP(mr, md), DT(mr), "anantara", "fp") + f" – पहले-पहले के {ADJo(mr, md)} समूह बाद-बाद के {KH(mr)} के लिए {I('anantara', 'mp')}। (1)",
    PN(DP(mr, md), DT(md), "anantara", "fp") + f" – पहले-पहले के {ADJo(mr, md)} समूह बाद-बाद के {KH(md)} के लिए {I('anantara', 'mp')}। (2)",
    PN(DP(mr, md), DT(mr, md), "anantara", "fp") + f" – पहले-पहले के {ADJo(mr, md)} समूह बाद-बाद के {ADJo(mr, md)} समूहों के लिए {I('anantara', 'mp')}। (3)",
    # ^7-17-39
    PN(D(mr), DT(mr), "samanantara") + f"… (निकटता-कारण के समान) {I('sahajāta')}… {I('aññamañña')}… {I('nissaya')}… (तीनों में भी सत्रह प्रश्न करने चाहिए)।",
    # upanissaya ^7-17-40
    PN(D(mr), DT(mr), "upanissaya") + f" – {UPN}, {UPP}…। {UPP} – {PV}। (1)",
    PN(D(mr), DT(md), "upanissaya") + f" – {UPN}, {UPP}…। {UPP} – {PV}। (2)",
    PN(D(mr), DT(mr, md), "upanissaya") + f" – {UPN}, {UPP}…। {UPP} – {PV}। (3)",
    PN(D(mh), DT(mh), "upanissaya") + f"। {UPP} – {MG1}। (1)",
    PN(D(mh), DT(mr), "upanissaya") + f"। {UPA} – {AG}। (2)",
    PN(D(mh), DT(md), "upanissaya") + f" – {UPA}, {UPP}…। {UPP} – {MG2}। (3)",
    PN(D(mh), DT(mr, md), "upanissaya") + f"। {UPA} – {AG}। (4)",
    PN(D(mh), DT(mh, md), "upanissaya") + f"। {UPP} – {MG2}। (5)",
    PN(D(md), DT(md), "upanissaya") + f" – {UPA}, {UPN}, {UPP}…। {UPP} – {MG2}; {PV}। (1)",
    PN(D(md), DT(mr), "upanissaya") + f" – {UPA}, {UPN}, {UPP}…। {UPP} – {PV}। (2)",
    PN(D(md), DT(mh), "upanissaya") + f"। {UPP} – {MG2}। (3)",
    PN(D(md), DT(mr, md), "upanissaya") + f" – {UPA}, {UPN}, {UPP}…। {UPP} – {PV}। (4)",
    PN(D(md), DT(mh, md), "upanissaya") + f"। {UPP} – {MG2}। (5)",
    PN(DP(mr, md), DT(mr), "upanissaya", "fp") + f" – {UPN}, {UPP}…। {UPP} – {PV}। (1)",
    PN(DP(mr, md), DT(md), "upanissaya", "fp") + f" – {UPN}, {UPP}…। {UPP} – {PV}। (2)",
    PN(DP(mr, md), DT(mr, md), "upanissaya", "fp") + f" – {UPN}, {UPP}…। {UPP} – {PV}। (3)",
    PN(DP(mh, md), DT(mr), "upanissaya", "fp") + f"। {UPA} – {AG}। (1)",
    PN(DP(mh, md), DT(mh), "upanissaya", "fp") + f"। {UPP} – {MG2}। (2)",
    PN(DP(mh, md), DT(md), "upanissaya", "fp") + f" – {UPA}, {UPP}…। {UPP} – {MG2}। (3)",
    PN(DP(mh, md), DT(mr, md), "upanissaya", "fp") + f"। {UPA} – {AG}। (4)",
    PN(DP(mh, md), DT(mh, md), "upanissaya", "fp") + f"। {UPP} – {MG2}। (5)",
    # āsevana ^7-17-45
    PN(D(mr), DT(mr), "āsevana") + f" – पहले-पहले के {KN(mr)} बाद-बाद के {KH(mr)} के लिए {I('āsevana', 'mp')}।",
    PN(D(mr), DT(md), "āsevana") + " (निकटता-कारण के समान। नौ प्रश्न करने चाहिए, मन को विषय की ओर मोड़ना शामिल नहीं करना चाहिए)।",
    # kamma ^7-17-46
    PN(D(mr), DT(mr), "kamma") + " – सह-उत्पत्ति… (भिन्न क्षण नहीं है, सत्रह प्रश्न करने चाहिए)।",
    # āhāra … ^7-17-47
    UD(D(mr), DT(mr), ["āhāra", "indriya", "jhāna", "magga", "sampayutta", "atthi"])
    + f" (इन सात कारणों में सत्रह प्रश्न, मूल-कारण के समान)… {I('natthi')}… {I('vigata')} (निकटता-कारण के समान)… {I('avigata')} (सत्रह प्रश्न)।",
    # Paccanīyuddhāra ^7-17-49
    UD(D(mr), DT(mr), ["sahajāta", "upanissaya"]) + "। (1)",
    UD(D(mr), DT(md), ["sahajāta", "upanissaya"]) + "। (2)",
    UD(D(mr), DT(mr, md), ["sahajāta", "upanissaya"]) + "। (3)",
    UD(D(mh), DT(mh), ["sahajāta", "upanissaya"]) + "। (1)",
    UD(D(mh), DT(mr), ["ārammaṇa", "upanissaya"]) + "। (2)",
    UD(D(mh), DT(md), ["ārammaṇa", "sahajāta", "upanissaya"]) + "। (3)",
    UD(D(mh), DT(mr, md), ["ārammaṇa", "upanissaya"]) + "। (4)",
    UD(D(mh), DT(mh, md), ["sahajāta", "upanissaya"]) + "। (5)",
    UD(D(md), DT(md), ["sahajāta", "upanissaya"]) + "। (1)",
    UD(D(md), DT(mr), ["ārammaṇa", "sahajāta", "upanissaya"]) + "। (2)",
    UD(D(md), DT(mh), ["sahajāta", "upanissaya"]) + "। (3)",
    UD(D(md), DT(mr, md), ["sahajāta", "upanissaya"]) + "। (4)",
    UD(D(md), DT(mh, md), ["sahajāta", "upanissaya"]) + "। (5)",
    UD(DP(mr, md), DT(mr), ["sahajāta", "upanissaya"], "fp") + "। (1)",
    UD(DP(mr, md), DT(md), ["sahajāta", "upanissaya"], "fp") + "। (2)",
    UD(DP(mr, md), DT(mr, md), ["sahajāta", "upanissaya"], "fp") + "। (3)",
    UD(DP(mh, md), DT(mr), ["ārammaṇa", "upanissaya"], "fp") + "। (1)",
    UD(DP(mh, md), DT(mh), ["sahajāta", "upanissaya"], "fp") + "। (2)",
    UD(DP(mh, md), DT(md), ["sahajāta", "upanissaya"], "fp") + "। (3)",
    UD(DP(mh, md), DT(mr, md), ["upanissaya"], "fp") + "। (4)",
    UD(DP(mh, md), DT(mh, md), ["sahajāta", "upanissaya"], "fp") + "। (5)",
]
