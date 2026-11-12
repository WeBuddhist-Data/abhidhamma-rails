"""Builder: pi-2 chapter 15 (Paṭisambhidāvibhaṅga), Hindi rails, plain audience.

usage: python -I -X utf8 build_rails_15.py
Imports build_rails_sample (read-only constants and emit), build_rails_15_citta, build_rails_3_panha.
"""
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-hi\rails")
import build_rails_sample as S  # noqa: E402
import build_rails_15_citta as C  # noqa: E402
import build_rails_3_panha as P  # noqa: E402

CH = "15-patisambhidavibhango.md"
TITLE = "विश्लेषणात्मक ज्ञानों का विश्लेषण"
PS = "विश्लेषणात्मक ज्ञान"
ATTHA = f"अर्थ का {PS}"
DHAMMA = f"परिघटनाओं का {PS}"        # dhamma in dhammapaṭisambhidā = परिघटना
NIRUTTI = f"भाषा का {PS}"
PATIBHANA = f"सूझ-बूझ का {PS}"
FOUR_L = f"चार {PS} – {ATTHA}, {DHAMMA}, {NIRUTTI}, {PATIBHANA}"
FOUR = FOUR_L + "।"
THREE = f"तीन {PS} – {ATTHA}, {NIRUTTI}, {PATIBHANA}।"
VAR_PATIBHANA = "[वर्तनी-भेद (Syā.): paṭibhāṇapaṭisambhidā, आगे भी इसी तरह]"


def isk(x, y):
    """X-e ñāṇaṃ Y-paṭisambhidā"""
    return f"{x} का ज्ञान {y} है"


NIR = f"उसमें परिघटनाओं की भाषा की अभिव्यक्ति का ज्ञान {NIRUTTI} है"   # tatra dhammaniruttābhilāpe ñāṇaṃ niruttipaṭisambhidā
PAT = f"ज्ञानों का ज्ञान {PATIBHANA} है"                               # ñāṇesu ñāṇaṃ paṭibhānapaṭisambhidā
VARO = {"sangaha": "सारांश का खंड", "sacca": "सत्यों का खंड", "hetu": "कारणों का खंड",
        "dhamma": "परिघटनाओं का खंड", "pacca": "परस्पर-आश्रित उत्पत्ति का खंड",
        "pariyatti": "शिक्षा के अध्ययन का खंड", "kusala": "हितकर परिघटनाओं का खंड",
        "akusala": "हानिकर परिघटनाओं का खंड", "vipaka": "कर्म-फल रूपी परिघटनाओं का खंड",
        "kiriya": "केवल क्रिया रूपी परिघटनाओं का खंड"}


def ayam(v):
    return f"यह {VARO[v]} है।"


def four_truths(x, xo):
    """X-e / X-samudaye / X-nirodhe / X-nirodhagāminiyā paṭipadāya ñāṇaṃ …  (x: direct, xo: oblique)"""
    return (f"{isk(x, ATTHA)}, {isk(xo + ' की उत्पत्ति', DHAMMA)}, {isk(xo + ' के अंत', ATTHA)}, "
            f"{isk(xo + ' के अंत की ओर ले जाने वाले प्रगति के ढंग', DHAMMA)}")


BORN = "जन्मी हुई, हो चुकी, भली-भाँति जन्मी, पैदा हुई, पूरी तरह पैदा हुई, प्रकट हुई"  # jātā bhūtā sañjātā nibbattā abhinibbattā pātubhūtā

# Abhidhammabhājanīya tails
def tail_k(sep):
    return (f"इन परिघटनाओं का ज्ञान {DHAMMA} है। उनके कर्म-फल का ज्ञान {ATTHA} है{sep} {TAIL_NP}")


TAIL_NP = (f"जिस भाषा से उन परिघटनाओं का नामकरण होता है, उसमें परिघटनाओं की भाषा की अभिव्यक्ति का ज्ञान {NIRUTTI} है। "
           f"जिस ज्ञान से कोई उन ज्ञानों को जानता है – “ये ज्ञान इस अर्थ को प्रकाशित करने वाले हैं”, "
           f"ज्ञानों का वह ज्ञान {PATIBHANA} है।")
TAIL_V = f"इन परिघटनाओं का ज्ञान {ATTHA} है। {TAIL_NP}"

FACT = {"phassa": "संपर्क होता है", "vedana": "अनुभूति होती है", "sanna": "पहचान होती है",
        "cetana": "इरादा होता है", "citta": "मन होता है", "vitakka": "आरंभिक विचार होता है",
        "vicara": "सतत विचार होता है", "piti": "उल्लास होता है", "sukha": "सुख होता है", "dukkha": "दुःख होता है",
        "upekkha": "समभाव होता है", "ekagg": "मन की एकाग्रता होती है", "viriyi": "उत्साह की क्षमता होती है",
        "samadhii": "एकाग्रता की क्षमता होती है", "mani": "मन की क्षमता होती है",
        "upekkhi": "समभाव की क्षमता होती है", "somi": "प्रसन्नता की क्षमता होती है",
        "sukhi": "सुख की क्षमता होती है", "dukkhi": "दुःख की क्षमता होती है", "jivi": "जीवन-क्षमता होती है"}


def facts(*ks):
    """tasmiṃ samaye phasso hoti, … jīvitindriyaṃ hoti, ye vā pana … arūpino dhammā."""
    return "उस समय " + ", ".join(FACT[k] for k in ks) + f", {C.AÑÑE}।"


F_V5 = ("phassa", "vedana", "sanna", "cetana", "citta")
F_UPE = F_V5 + ("upekkha", "ekagg", "mani", "upekkhi", "jivi")
F_SUKHA = F_V5 + ("sukha", "ekagg", "mani", "sukhi", "jivi")
F_DUKKHA = F_V5 + ("dukkha", "ekagg", "mani", "dukkhi", "jivi")
F_MANODH = F_V5 + ("vitakka", "vicara", "upekkha", "ekagg", "mani", "upekkhi", "jivi")
F_SOM = F_V5 + ("vitakka", "vicara", "piti", "sukha", "ekagg", "mani", "somi", "jivi")
F_KIR_UPE = F_V5 + ("vitakka", "vicara", "upekkha", "ekagg", "viriyi", "samadhii", "mani", "upekkhi", "jivi")

KAMA_VIP = "इंद्रिय-सुखों के लोक से संबंधित हितकर कर्म किए जाने और संचित होने के कारण"
AKUS_VIP = "हानिकर कर्म किए जाने और संचित होने के कारण"
KIRIYA = "जो केवल क्रिया रूपी है, न हितकर, न हानिकर, न ही कर्म-फल"
MANODHATU = "मन का तत्व"
MANOVINNANADHATU = "मन की चेतना का तत्व"


def vinnana_obj(sense, feel, obj):
    """<X>viññāṇaṃ uppannaṃ hoti <feel>sahagataṃ <obj>ārammaṇaṃ (chain form, pi-1 ^1-556)"""
    return f"{sense} की चेतना उत्पन्न होती है, जो {feel} के साथ होने वाली है और जिसका विषय {obj} है"


def dhatu(name_, desc, obj):
    return f"{name_} उत्पन्न होता है, जो {desc} है {obj}"


DG, DGV = "ग़लत दृष्टि से जुड़ा", "ग़लत दृष्टि से अलग"
AKUSALA_CHAIN = "… ".join([C.q3(C.SN, DG, C.SAS), C.q2(C.SN, DGV), C.q3(C.SN, DGV, C.SAS), C.q2(C.UP, DG),
                           C.q3(C.UP, DG, C.SAS), C.q2(C.UP, DGV), C.q3(C.UP, DGV, C.SAS),
                           C.q2("उदासी के साथ होने वाला", "चिढ़ से जुड़ा"),
                           C.q3("उदासी के साथ होने वाला", "चिढ़ से जुड़ा", C.SAS),
                           C.q2(C.UP, "संशय से जुड़ा"), C.q2(C.UP, "बेचैनी से जुड़ा")])

PANHA_Q = ("चार विश्लेषणात्मक ज्ञानों में से कितने हितकर हैं, कितने हानिकर, कितने नैतिक रूप से अनिर्धारित… "
           "कितने संघर्ष वाले हैं, कितने संघर्ष से रहित?")
DEFAULT = P.Subj("चारों", "इन चारों", True)
BR_ASAVA = "[पाठभेद (Sī.): āsavā; तत्वों के विश्लेषण में पाठ-भेद नहीं है]"


def build(pali):
    lines = {sid: [S.ID.sub("", x).rstrip() for x in pl] for sid, pl in S.segs_of_lines(pali)}
    h = {}
    h["2-15-0"] = [f"### {TITLE}"]
    h["2-15-1-0"] = [f"#### {S.SUTTANTA_BH}"]
    h["2-15-1-1-0"] = [f"##### {VARO['sangaha']}"]
    h["2-718"] = [f"{FOUR_L} {VAR_PATIBHANA}। {isk('अर्थ', ATTHA)}, {isk('परिघटनाओं', DHAMMA)}, {NIR}, {PAT}। "
                  f"{ayam('sangaha')}"]
    h["2-15-1-2-0"] = [f"##### {VARO['sacca']}"]
    h["2-719"] = [f"{FOUR} {four_truths('दुःख', 'दुःख')}, {NIR}, {PAT}। {ayam('sacca')}"]
    h["2-15-1-3-0"] = [f"##### {VARO['hetu']}"]
    h["2-720"] = [f"{FOUR} {isk('कारण', DHAMMA)}, {isk('कारण के फल', ATTHA)}, {NIR}, {PAT}। {ayam('hetu')}"]
    h["2-15-1-4-0"] = [f"##### {VARO['dhamma']}"]
    h["2-721"] = [f"{FOUR} जो परिघटनाएँ {BORN} हैं, इन परिघटनाओं का ज्ञान {ATTHA} है; जिन परिघटनाओं से वे परिघटनाएँ "
                  f"{BORN} हैं, उन परिघटनाओं का ज्ञान {DHAMMA} है; {NIR}; {PAT}। {ayam('dhamma')}"]
    h["2-15-1-5-0"] = [f"##### {VARO['pacca']}"]
    h["2-722"] = [f"{FOUR} {four_truths('बुढ़ापे और मृत्यु', 'बुढ़ापे और मृत्यु')}, {NIR}, {PAT}।"]
    links = ["जन्म", "अस्तित्व", "आसक्ति", "तृष्णा", "अनुभूति", "संपर्क", "छह इंद्रिय-क्षेत्रों",
             "मानसिक पक्ष और भौतिक रूप", "चेतना"]
    h["2-723"] = [f"{FOUR} " + "… ".join(f"{x} का ज्ञान" for x in links) + "… "
                  f"{four_truths('मानसिक रचनाओं', 'मानसिक रचनाओं')}, {NIR}, {PAT}। {ayam('pacca')}"]
    h["2-15-1-6-0"] = [f"##### {VARO['pariyatti']}"]
    h["2-724"] = [FOUR,
                  f"यहाँ {DHAMMA} क्या है? यहाँ भिक्षु शिक्षा को जानता है – उपदेश, गद्य-पद्य मिश्रित उपदेश, व्याख्याएँ, "
                  f"पद्य, प्रेरित उद्गार, उद्धृत वचन, पूर्व जन्मों की कथाएँ, अद्भुत घटनाओं के वर्णन, प्रश्नोत्तर। "
                  f"यह “{DHAMMA}” कहा जाता है। वह उस-उस कथन का अर्थ जानता है – “इस कथन का यह अर्थ है, "
                  f"इस कथन का यह अर्थ है”। यह “{ATTHA}” कहा जाता है। {NIR}। {PAT}। {ayam('pariyatti')}",
                  f"{S.SUTTANTA_BH}।"]
    # ------------------------------------------------ Abhidhammabhājanīya
    h["2-15-2-0"] = [f"#### {S.ABHI_BH}"]
    h["2-15-2-1-0"] = [f"##### {VARO['kusala']}"]
    D1 = C.q2(C.SN, C.NS)
    h["2-725"] = [FOUR, f"{C.KUSALA_Q} {C.kusala_head(D1)} {C.OBJ_ALL}, {C.PHASSA_PE}, {C.IME_KUSALA}। {tail_k(',')}"]
    tk = tail_k("।")
    h["2-726"] = [FOUR, f"{C.KUSALA_Q} {C.kusala_head(C.CHAIN8)} {C.OBJ_ALL}, {C.PHASSA_PE}। {C.IME_KUSALA}। {tk}"]
    h["2-727"] = [FOUR, f"{C.KUSALA_Q} {C.RUPUPAPATTI}, {C.JHANA1_KASINA}, {C.PHASSA_PE}। {C.IME_KUSALA}। {tk}"]
    h["2-728"] = [FOUR, f"{C.KUSALA_Q} {C.ARUPUPAPATTI}, {C.ARUPA4}, {C.PHASSA_PE}। {C.IME_KUSALA}। {tk}"]
    h["2-729"] = [FOUR, f"{C.KUSALA_Q} {C.LOKUTTARA}, {C.JHANA1_PATH}, {C.PHASSA_PE}। {C.IME_KUSALA}। {tk}"]
    h["2-15-2-2-0"] = [f"##### {VARO['akusala']}"]
    ak_head = "जिस समय हानिकर मन उत्पन्न होता है, जो {} होता है"
    h["2-730"] = [FOUR, f"{C.AKUSALA_Q} {ak_head.format(C.q2(C.SN, DG))} {C.OBJ_ALL}, {C.PHASSA_PE}। "
                        f"{C.IME_AKUSALA}। {tk}"]
    h["2-731"] = [FOUR, f"{C.AKUSALA_Q} {ak_head.format(AKUSALA_CHAIN)} {C.OBJ_ALL}, {C.PHASSA_PE}। "
                        f"{C.IME_AKUSALA}। {tk}"]
    # ------------------------------------------------ vipāka
    h["2-15-2-3-0"] = [f"##### {VARO['vipaka']}"]
    AQ, IA = C.ABYAKATA_Q, C.IME_ABYAKATA
    h["2-732"] = [THREE, f"{AQ} जिस समय {KAMA_VIP} कर्म के फल रूपी आँख की चेतना उत्पन्न होती है, जो समभाव के साथ "
                         f"होने वाली है और जिसका विषय दृश्य रूप होता है, {facts(*F_UPE)} {IA}। {TAIL_V}"]
    chain5 = "… ".join([vinnana_obj("कान", "समभाव", "ध्वनि"), vinnana_obj("नाक", "समभाव", "गंध"),
                        vinnana_obj("जीभ", "समभाव", "स्वाद"), vinnana_obj("शरीर", "सुख", "स्पर्श")])
    h["2-733"] = [THREE, f"{AQ} जिस समय {KAMA_VIP} कर्म के फल रूपी {chain5}, {facts(*F_SUKHA)} {IA}। {TAIL_V}"]
    h["2-734"] = [f"{THREE} {AQ} जिस समय {KAMA_VIP} कर्म के फल रूपी "
                  f"{dhatu(MANODHATU, C.UP, C.OBJ_5)}, {facts(*F_MANODH)} {IA}। {TAIL_V}"]
    h["2-735"] = [THREE, f"{AQ} जिस समय {KAMA_VIP} कर्म के फल रूपी "
                         f"{dhatu(MANOVINNANADHATU, C.SN, C.OBJ_ALL)}, {facts(*F_SOM)} {IA}। {TAIL_V}"]
    h["2-736"] = [THREE, f"{AQ} जिस समय {KAMA_VIP} कर्म के फल रूपी "
                         f"{dhatu(MANOVINNANADHATU, C.UP, C.OBJ_ALL)}, {facts(*F_MANODH)} {IA}। {TAIL_V}"]
    h["2-737"] = [THREE, f"{AQ} जिस समय {KAMA_VIP} कर्म के फल रूपी "
                         f"{dhatu(MANOVINNANADHATU, D1 + '… ' + C.CHAIN8, C.OBJ_ALL)}, {C.PHASSA_PE}। {IA}। {TAIL_V}"]
    h["2-738"] = [THREE, f"{AQ} {C.RUPUPAPATTI}, {C.JHANA1_KASINA}, {C.PHASSA_PE}। {C.IME_KUSALA}। "
                         f"उसी सूक्ष्म भौतिक लोक से संबंधित हितकर कर्म किए जाने और संचित होने के कारण जिस समय वह "
                         f"इंद्रिय-सुखों से अलग होकर… कर्म के फल रूपी पहले ध्यान को प्राप्त करके उसमें रहता है, "
                         f"जो पृथ्वी के ध्यान-मंडल वाला है, {C.PHASSA_PE}। {IA}। {TAIL_V}"]
    h["2-739"] = [THREE, f"{AQ} {C.ARUPUPAPATTI}, {C.ARUPA4}, {C.PHASSA_PE}। {C.IME_KUSALA}। "
                         f"उसी अभौतिक लोक से संबंधित हितकर कर्म किए जाने और संचित होने के कारण जिस समय वह "
                         f"कुछ भी न होने के क्षेत्र को पूरी तरह पार करके, सुख को छोड़ने से… कर्म के फल रूपी चौथे ध्यान को "
                         f"प्राप्त करके उसमें रहता है, जो न पहचान, न अ-पहचान के क्षेत्र की पहचान के साथ होने वाला है, "
                         f"{C.PHASSA_PE}। {IA}। {TAIL_V}"]
    h["2-740"] = [THREE, f"{AQ} {C.LOKUTTARA}, {C.JHANA1_PATH}, {C.PHASSA_PE}। {C.IME_KUSALA}। "
                         f"उसी लोकोत्तर हितकर कर्म के किए जाने और अभ्यास किए जाने के कारण जिस समय वह "
                         f"इंद्रिय-सुखों से अलग होकर… कर्म के फल रूपी पहले ध्यान को प्राप्त करके उसमें रहता है, "
                         f"जो दुःखद प्रगति और धीमे उच्च ज्ञान वाला और शून्य होता है, {C.PHASSA_PE}। {IA}। {TAIL_V}"]
    chain_ak = "… ".join([vinnana_obj("आँख", "समभाव", "दृश्य रूप"), vinnana_obj("कान", "समभाव", "ध्वनि"),
                          vinnana_obj("नाक", "समभाव", "गंध"), vinnana_obj("जीभ", "समभाव", "स्वाद"),
                          vinnana_obj("शरीर", "दुःख", "स्पर्श")])
    h["2-741"] = [THREE, f"{AQ} जिस समय {AKUS_VIP} कर्म के फल रूपी {chain_ak}, {facts(*F_DUKKHA)} {IA}। {TAIL_V}"]
    obj5_pe = C.OBJ_5.replace(", या जिस किसी को भी वह विषय बनाए", "")
    h["2-742"] = [THREE, f"{AQ} जिस समय {AKUS_VIP} कर्म के फल रूपी {dhatu(MANODHATU, C.UP, obj5_pe)}… "
                         f"{dhatu(MANOVINNANADHATU, C.UP, C.OBJ_ALL)}, {facts(*F_MANODH)} {IA}। {TAIL_V}"]
    # ------------------------------------------------ kiriyā
    h["2-15-2-4-0"] = [f"##### {VARO['kiriya']}"]
    h["2-743"] = [THREE, f"{AQ} जिस समय {MANODHATU} उत्पन्न होता है, {KIRIYA}, जो {C.UP} है {C.OBJ_5}, "
                         f"{facts(*F_MANODH)} {IA}। {TAIL_V}"]
    objall_pe = C.OBJ_ALL.replace(", या जिस किसी को भी वह विषय बनाए", "")
    h["2-744"] = [THREE, f"{AQ} जिस समय {MANOVINNANADHATU} उत्पन्न होता है, {KIRIYA}, जो {C.SN} है {objall_pe}… "
                         f"{MANOVINNANADHATU} उत्पन्न होता है, {KIRIYA}, जो {C.UP} है {C.OBJ_ALL}, "
                         f"{facts(*F_KIR_UPE)} {IA}। {TAIL_V}"]
    h["2-745"] = [THREE, f"{AQ} जिस समय {MANOVINNANADHATU} उत्पन्न होता है, {KIRIYA}, जो {D1}… {C.CHAIN8} है… "
                         f"कोई सूक्ष्म भौतिक लोक से संबंधित ध्यान का अभ्यास करता है… अभौतिक लोक से संबंधित ध्यान का "
                         f"अभ्यास करता है, {KIRIYA}, जो इसी जीवन में सुख से रहने के लिए होता है… {C.ARUPA4}, "
                         f"{C.PHASSA_PE}। {IA}। {TAIL_V}"]
    h["2-746"] = [f"{FOUR} तीन {PS} इंद्रिय-सुखों के लोक से संबंधित हितकर मन की ज्ञान से जुड़ी चार उत्पत्तियों में, "
                  f"केवल क्रिया रूपी मन की ज्ञान से जुड़ी चार उत्पत्तियों में उत्पन्न होते हैं। {ATTHA} इनमें भी "
                  f"उत्पन्न होता है, और चार मार्गों और चार फलों में भी उत्पन्न होता है।",
                  f"{S.ABHI_BH}।"]
    # ------------------------------------------------ Pañhāpucchaka
    h["2-15-3-0"] = [f"#### {S.PANHA}"]
    h["2-747"] = [FOUR]
    h["2-748"] = [PANHA_Q]
    h["2-15-3-1-0"] = ["##### तीन-तीन के वर्गीकरण"]
    h["2-749"] = [P.render_line(x, DEFAULT) for x in lines["2-749"]]
    h["2-15-3-2-0"] = ["##### दो-दो के वर्गीकरण"]
    d = lines["2-750"]
    br = " [āsavā (sī.) dhātuvibhaṅge pana pāṭhanānattaṃ natthi]"
    l3 = P.render_line(d[2], DEFAULT, fixes=[(br, ""),
                                             ("āsavavippayuttā sāsavā", "āsavavippayuttasāsavā"),
                                             ("āsavavippayuttā anāsavā", "āsavavippayuttaanāsavā")])
    a = f"{ATTHA[:-len(PS)].replace('का ', 'के ')}{PS} को मन के मैल रूपी भी"
    assert a in l3, a
    l3 = l3.replace(a, a[: -len(" भी")] + f" {BR_ASAVA} भी", 1)
    b = "वह कभी मन के मैलों का विषय बनने वाला, पर स्वयं मन के मैल रूपी"
    assert b in l3, b
    l3 = l3.replace(b, f"{b} {BR_ASAVA}", 1)
    h["2-750"] = [P.render_line(d[0], DEFAULT),
                  P.render_line(d[1], DEFAULT, fixes=[(", kenaci viññeyyā", ", @kenaci viññeyyā")]),
                  l3,
                  P.render_line(d[3], DEFAULT),
                  P.render_line(d[4], DEFAULT),
                  f"{S.PANHA}।", f"{TITLE} {S.DONE}।"]
    return h


if __name__ == "__main__":
    pali = (S.PALI / CH).read_text(encoding="utf-8").splitlines()
    S.emit(pali, build(pali), S.OUT / CH)
