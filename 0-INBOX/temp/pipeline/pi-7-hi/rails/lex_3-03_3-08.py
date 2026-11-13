"""Phrase tables for build_rails_3-03_3-08.py (pi-7 Hindi plain RAILS, files 3-03 .. 3-08).

Pāli keys are lower-case and gocchaka-normalized: the cluster word becomes GG (āsav-, saññojan-, ganth-, nīvaraṇ-,
parāmās-), its 'object' word SG (sāsav-, saññojaniy-, ganthaniy-, nīvaraṇiy-, parāmaṭṭh-) and the negative aSG.
Hindi strings may hold {placeholders} filled from GOC[file]; '~' marks a word that inflects (वाला~ जुड़ा~ हुआ~).
"""

# ------------------------------------------------------------------ the clusters

_COMMON = dict(karne="करने")
GOC = {
    "3-03": dict(stems=[("sāsav", "SG"), ("anāsav", "aSG"), ("āsav", "GG")],
                 sg="मन का मैल", sgo="मन के मैल", pl="मन के मैल", plo="मन के मैलों", g="m",
                 w="मन के मैलों", rupi="मन के मैल रूपी", pron="उन",
                 cluster="मन के मैलों का वर्ग", cluster_o="मन के मैलों के वर्ग",
                 duka="मन के मैल वाला दो का वर्गीकरण", duka_o="मन के मैल वाले दो के वर्गीकरण",
                 sduka="मन के मैलों के विषय वाला दो का वर्गीकरण", karne_g="करने"),
    "3-04": dict(stems=[("saññojaniy", "SG"), ("asaññojaniy", "aSG"), ("saññojan", "GG")],
                 sg="बंधन", sgo="बंधन", pl="बंधन", plo="बंधनों", g="m",
                 w="बंधनों", rupi="बंधन रूपी", pron="उन",
                 cluster="बंधनों का वर्ग", cluster_o="बंधनों के वर्ग",
                 duka="बंधन वाला दो का वर्गीकरण", duka_o="बंधन वाले दो के वर्गीकरण",
                 sduka="बंधनों के विषय वाला दो का वर्गीकरण", karne_g="करने"),
    "3-05": dict(stems=[("ganthaniy", "SG"), ("aganthaniy", "aSG"), ("ganth", "GG")],
                 sg="गाँठ", sgo="गाँठ", pl="गाँठें", plo="गाँठों", g="f",
                 w="गाँठों", rupi="गाँठ रूपी", pron="उन",
                 cluster="गाँठों का वर्ग", cluster_o="गाँठों के वर्ग",
                 duka="गाँठ वाला दो का वर्गीकरण", duka_o="गाँठ वाले दो के वर्गीकरण",
                 sduka="गाँठों के विषय वाला दो का वर्गीकरण", karne_g="करनी"),
    "3-06": dict(stems=[]),
    "3-07": dict(stems=[("nīvaraṇiy", "SG"), ("anīvaraṇiy", "aSG"), ("nīvaraṇ", "GG")],
                 sg="बाधा", sgo="बाधा", pl="बाधाएँ", plo="बाधाओं", g="f",
                 w="बाधाओं", rupi="बाधा रूपी", pron="उन",
                 cluster="बाधाओं का वर्ग", cluster_o="बाधाओं के वर्ग",
                 duka="बाधा वाला दो का वर्गीकरण", duka_o="बाधा वाले दो के वर्गीकरण",
                 sduka="बाधाओं के विषय वाला दो का वर्गीकरण", karne_g="करनी"),
    "3-08": dict(stems=[("parāmaṭṭh", "SG"), ("aparāmaṭṭh", "aSG"), ("parāmās", "GG")],
                 sg="ग़लत धारणा", sgo="ग़लत धारणा", pl="ग़लत धारणाएँ", plo="ग़लत धारणाओं", g="f",
                 w="ग़लत धारणा", rupi="ग़लत धारणा रूपी", pron="उस",
                 cluster="ग़लत धारणा का वर्ग", cluster_o="ग़लत धारणा के वर्ग",
                 duka="ग़लत धारणा वाला दो का वर्गीकरण", duka_o="ग़लत धारणा वाले दो के वर्गीकरण",
                 sduka="ग़लत धारणा के विषय वाला दो का वर्गीकरण", karne_g="करनी"),
}

# sub-kinds of each cluster: Pāli stem -> (sg direct, sg oblique, gender)
SUBKIND = {
    "3-03": {"kāmāsav": ("इंद्रिय-सुखों का मैल", "इंद्रिय-सुखों के मैल", "m"),
             "diṭṭhāsav": ("दृष्टि का मैल", "दृष्टि के मैल", "m"),
             "avijjāsav": ("अज्ञान का मैल", "अज्ञान के मैल", "m"),
             "bhavāsav": ("अस्तित्व का मैल", "अस्तित्व के मैल", "m")},
    "3-04": {"kāmarāgasaññojan": ("इंद्रिय-सुखों के राग का बंधन", "इंद्रिय-सुखों के राग के बंधन", "m"),
             "paṭighasaññojan": ("चिढ़ का बंधन", "चिढ़ के बंधन", "m"),
             "mānasaññojan": ("अहंकार का बंधन", "अहंकार के बंधन", "m"),
             "diṭṭhisaññojan": ("दृष्टि का बंधन", "दृष्टि के बंधन", "m"),
             "vicikicchāsaññojan": ("संशय का बंधन", "संशय के बंधन", "m"),
             "sīlabbataparāmāsasaññojan": ("सदाचार और व्रतों के बारे में ग़लत धारणा का बंधन",
                                           "सदाचार और व्रतों के बारे में ग़लत धारणा के बंधन", "m"),
             "bhavarāgasaññojan": ("अस्तित्व के राग का बंधन", "अस्तित्व के राग के बंधन", "m"),
             "issāsaññojan": ("ईर्ष्या का बंधन", "ईर्ष्या के बंधन", "m"),
             "macchariyasaññojan": ("कंजूसी का बंधन", "कंजूसी के बंधन", "m"),
             "avijjāsaññojan": ("अज्ञान का बंधन", "अज्ञान के बंधन", "m")},
    "3-05": {"abhijjhākāyaganth": ("लालच रूपी काया की गाँठ", "लालच रूपी काया की गाँठ", "f"),
             "byāpādakāyaganth": ("दुर्भावना रूपी काया की गाँठ", "दुर्भावना रूपी काया की गाँठ", "f"),
             "sīlabbataparāmāsakāyaganth": ("सदाचार और व्रतों के बारे में ग़लत धारणा रूपी काया की गाँठ",
                                            "सदाचार और व्रतों के बारे में ग़लत धारणा रूपी काया की गाँठ", "f"),
             "idaṃsaccābhinivesakāyaganth": ("“केवल यही सत्य है” के आग्रह रूपी काया की गाँठ",
                                             "“केवल यही सत्य है” के आग्रह रूपी काया की गाँठ", "f"),
             "kāyaganth": ("काया की गाँठ", "काया की गाँठ", "f"),
             "sīlabbataparāmās": ("सदाचार और व्रतों के बारे में ग़लत धारणा", "सदाचार और व्रतों के बारे में ग़लत धारणा", "f"),
             "idaṃsaccābhinives": ("“केवल यही सत्य है” का आग्रह", "“केवल यही सत्य है” के आग्रह", "m")},
    "3-07": {"kāmacchandanīvaraṇ": ("इंद्रिय-सुखों की चाह की बाधा", "इंद्रिय-सुखों की चाह की बाधा", "f"),
             "byāpādanīvaraṇ": ("दुर्भावना की बाधा", "दुर्भावना की बाधा", "f"),
             "thinamiddhanīvaraṇ": ("आलस्य और तंद्रा की बाधा", "आलस्य और तंद्रा की बाधा", "f"),
             "thīnamiddhanīvaraṇ": ("आलस्य और तंद्रा की बाधा", "आलस्य और तंद्रा की बाधा", "f"),
             "uddhaccanīvaraṇ": ("बेचैनी की बाधा", "बेचैनी की बाधा", "f"),
             "kukkuccanīvaraṇ": ("पछतावे की बाधा", "पछतावे की बाधा", "f"),
             "vicikicchānīvaraṇ": ("संशय की बाधा", "संशय की बाधा", "f"),
             "avijjānīvaraṇ": ("अज्ञान की बाधा", "अज्ञान की बाधा", "f")},
    "3-08": {},
}

# ------------------------------------------------------------------ dyad items (with परिघटना, feminine)

ITEM = {
    "GG": "{rupi}",
    "noGG": "{rupi} न होने वाला~",
    "SG": "{w} का विषय बनने वाला~",
    "aSG": "{w} का विषय न बनने वाला~",
    "GGsampayutt": "{w} से जुड़ा~",
    "GGvippayutt": "{w} से अलग",
    "GGxSG": "{rupi} भी और {w} का विषय बनने वाला~ भी",
    "SGnGG": "{w} का विषय बनने वाला~, पर स्वयं {rupi} न होने वाला~",
    "GGxGGsampayutt": "{rupi} भी और {w} से जुड़ा~ भी",
    "GGsampayuttnGG": "{w} से जुड़ा~, पर स्वयं {rupi} न होने वाला~",
    "GGvippSG": "{w} से अलग, पर {pron}का विषय बनने वाला~",
    "GGvippaSG": "{w} से अलग और {pron}का विषय न बनने वाला~",
}
COMPOSITE = {"GGxSG", "SGnGG", "GGxGGsampayutt", "GGsampayuttnGG", "GGvippSG", "GGvippaSG"}
_E = r"(aṃ|o|ā|e|assa|ānaṃ)"
# composite items; run on text where -ñca/-ñceva were already split into 'ṃ ca' / 'ṃ ceva'
ITEM_JOIN = [
    (r"(?<!\w)GGsampayuttā ceva no ca GGādhipati(?!\w)", "GGsampayuttnGGādhipati"),
    (r"(?<!\w)SGā ceva no ca GGādhipati(?!\w)", "SGnGGādhipati"),
    (rf"(?<!\w)GG{_E} ceva SG{_E}(?: ca)?(?!\w)", r"GGxSG\2"),
    (rf"(?<!\w)GG{_E} ceva GGsampayutt{_E}(?: ca)?(?!\w)", r"GGxGGsampayutt\2"),
    (rf"(?<!\w)SG{_E} ceva no ca GG{_E}(?!\w)", r"SGnGG\2"),
    (rf"(?<!\w)GGsampayutt{_E} ceva no ca GG{_E}(?!\w)", r"GGsampayuttnGG\2"),
    (rf"(?<!\w)GGvippayutt{_E} SG{_E}(?!\w)", r"GGvippSG\2"),
    (rf"(?<!\w)GGvippayutt{_E} aSG{_E}(?!\w)", r"GGvippaSG\2"),
    (rf"(?<!\w)GGvippayuttaganthaniy{_E}(?!\w)", r"GGvippSG\1"),
    (rf"(?<!\w)GGvippayuttaaganthaniy{_E}(?!\w)", r"GGvippaSG\1"),
]

# ------------------------------------------------------------------ lexicon of the bodies

A_END = {"o": ("s", "n"), "aṃ": ("s", "n"), "assa": ("s", "d"), "ā": ("p", "n"), "e": ("p", "n"),
         "ānaṃ": ("p", "d"), "āni": ("p", "n")}


def _noun(lex, forms, hindi, head=False):
    for w, (n, c) in forms.items():
        lex[w] = dict(k="N", f=hindi, n=n, c=c, head=head)


def _astem(lex, stem, forms_hindi, head=False):
    """a-stem noun: generate the usual endings."""
    _noun(lex, {stem + e: nc for e, nc in A_END.items()}, forms_hindi, head)


def _adj(lex, stem, h, alt=False, ends=A_END):
    for e, (n, c) in ends.items():
        lex.setdefault(stem + e, dict(k="A", h=h, n=n, c=c, alt=alt))


def _same(h, g="m", plo=None):
    return (h, h, h, plo or (h + "ों"), g)


def build_lex(key):
    lex = {}
    # nouns
    _astem(lex, "khandh", ("समूह", "समूह", "समूह", "समूहों", "m"))
    _noun(lex, {"rūpaṃ": ("s", "n"), "rūpānaṃ": ("p", "d")}, ("भौतिक रूप", "भौतिक रूप", "भौतिक रूप", "भौतिक रूपों", "m"))
    _noun(lex, {"vatthu": ("s", "n"), "vatthuṃ": ("s", "n"), "vatthussa": ("s", "d")}, _same("आधार"))
    _astem(lex, "mahābhūt", ("महाभूत", "महाभूत", "महाभूत", "महाभूतों", "m"))
    _astem(lex, "moh", _same("मोह"))
    _noun(lex, {"cetanā": ("s", "n")}, ("इरादा", "इरादे", "इरादे", "इरादों", "m"), head=True)
    _noun(lex, {"hetu": ("s", "n"), "hetū": ("p", "n")}, _same("मूल"), head=True)
    _noun(lex, {"adhipati": ("s", "n")}, ("प्रधानता", "प्रधानता", "प्रधानताएँ", "प्रधानताओं", "f"), head=True)
    _noun(lex, {"āhārā": ("p", "n")}, _same("आहार"), head=True)
    _noun(lex, {"indriyā": ("p", "n")}, ("क्षमता", "क्षमता", "क्षमताएँ", "क्षमताओं", "f"), head=True)
    for st, h, g in [("dos", "द्वेष", "m"), ("lobh", "लोभ", "m"), ("mān", "अहंकार", "m"), ("rāg", "राग", "m")]:
        _astem(lex, st, _same(h, g))
    _noun(lex, {"paṭighaṃ": ("s", "n"), "paṭighassa": ("s", "d")}, ("चिढ़", "चिढ़", "चिढ़", "चिढ़ों", "f"))
    _noun(lex, {"diṭṭhi": ("s", "n"), "diṭṭhiṃ": ("s", "n"), "diṭṭhiyā": ("s", "d")},
          ("दृष्टि", "दृष्टि", "दृष्टियाँ", "दृष्टियों", "f"))
    _noun(lex, {"vicikicchā": ("s", "n"), "vicikicchaṃ": ("s", "n"), "vicikicchāya": ("s", "d")}, _same("संशय"))
    _noun(lex, {"uddhaccaṃ": ("s", "n"), "uddhaccassa": ("s", "d")}, ("बेचैनी", "बेचैनी", "बेचैनी", "बेचैनी", "f"))
    _noun(lex, {"kukkuccaṃ": ("s", "n"), "kukkuccassa": ("s", "d")}, ("पछतावा", "पछतावे", "पछतावे", "पछतावों", "m"))
    _noun(lex, {"domanassaṃ": ("s", "n"), "domanassassa": ("s", "d")}, ("उदासी", "उदासी", "उदासी", "उदासी", "f"))
    _noun(lex, {"saddhā": ("s", "n"), "saddhaṃ": ("s", "n"), "saddhāya": ("s", "d")},
          ("श्रद्धा", "श्रद्धा", "श्रद्धा", "श्रद्धा", "f"))
    _noun(lex, {"sīlaṃ": ("s", "n"), "sīlassa": ("s", "d")}, _same("सदाचार"))
    _noun(lex, {"paññā": ("s", "n"), "paññaṃ": ("s", "n"), "paññāya": ("s", "d")},
          ("प्रज्ञा", "प्रज्ञा", "प्रज्ञा", "प्रज्ञा", "f"))
    _noun(lex, {"patthanā": ("s", "n"), "patthanaṃ": ("s", "n"), "patthanāya": ("s", "d")},
          ("कामना", "कामना", "कामनाएँ", "कामनाओं", "f"))
    _noun(lex, {"senāsanaṃ": ("s", "n")}, _same("निवास-स्थान"))
    _noun(lex, {"utuṃ": ("s", "n"), "utu": ("s", "n")}, _same("तापमान"))
    _noun(lex, {"bhojanaṃ": ("s", "n")}, _same("भोजन"))
    _noun(lex, {"sukhaṃ": ("s", "n"), "sukhassa": ("s", "d")}, _same("सुख"))
    _noun(lex, {"dukkhaṃ": ("s", "n"), "dukkhassa": ("s", "d")}, _same("दुःख"))
    _noun(lex, {"nibbānaṃ": ("s", "n")}, _same("निर्वाण"))
    _noun(lex, {"cakkhuṃ": ("s", "n")}, ("आँख", "आँख", "आँखें", "आँखों", "f"))
    for p, h in [("cakkh", "आँख"), ("sot", "कान"), ("ghān", "नाक"), ("jivh", "जीभ"), ("kāy", "शरीर")]:
        _noun(lex, {p + "āyatanaṃ": ("s", "n")}, (f"{h} का इंद्रिय-क्षेत्र", f"{h} के इंद्रिय-क्षेत्र",
                                                   f"{h} के इंद्रिय-क्षेत्र", f"{h} के इंद्रिय-क्षेत्रों", "m"))
    for p, h in [("cakkhu", "आँख"), ("sota", "कान"), ("ghāna", "नाक"), ("jivhā", "जीभ"), ("kāya", "शरीर")]:
        _noun(lex, {p + "viññāṇaṃ": ("s", "n"), p + "viññāṇassa": ("s", "d")},
              (f"{h} की चेतना", f"{h} की चेतना", f"{h} की चेतना", f"{h} की चेतना", "f"))
    for p, h in [("cakkhundriyaṃ", "आँख"), ("sotindriyaṃ", "कान"), ("ghānindriyaṃ", "नाक"),
                 ("jivhindriyaṃ", "जीभ"), ("kāyindriyaṃ", "शरीर")]:
        _noun(lex, {p: ("s", "n")}, (f"{h} की क्षमता", f"{h} की क्षमता", f"{h} की क्षमताएँ", f"{h} की क्षमताओं", "f"))
    for p, h in [("rūpāyatanaṃ", "दृश्य रूप"), ("saddāyatanaṃ", "ध्वनि"), ("gandhāyatanaṃ", "गंध"),
                 ("rasāyatanaṃ", "स्वाद"), ("phoṭṭhabbāyatanaṃ", "स्पर्श")]:
        _noun(lex, {p: ("s", "n")}, (f"{h} का इंद्रिय-क्षेत्र", f"{h} के इंद्रिय-क्षेत्र",
                                     f"{h} के इंद्रिय-क्षेत्र", f"{h} के इंद्रिय-क्षेत्रों", "m"))
    _noun(lex, {"rūpajīvitindriyaṃ": ("s", "n")}, ("भौतिक जीवन-क्षमता",) * 4 + ("f",))
    _noun(lex, {"kaṭattārūpaṃ": ("s", "n"), "kaṭattārūpānaṃ": ("p", "d")},
          ("किए गए कर्म से उत्पन्न भौतिक रूप",) * 3 + ("किए गए कर्म से उत्पन्न भौतिक रूपों", "m"))
    _noun(lex, {"upādārūpaṃ": ("s", "n"), "upādārūpānaṃ": ("p", "d")},
          ("व्युत्पन्न भौतिक रूप",) * 3 + ("व्युत्पन्न भौतिक रूपों", "m"))
    _noun(lex, {"vuṭṭhānassa": ("s", "d"), "vuṭṭhānaṃ": ("s", "n")}, ("बाहर आना", "बाहर आने", "बाहर आना", "बाहर आने", "m"))
    _noun(lex, {"āvajjanā": ("s", "n"), "āvajjanāya": ("s", "d")},
          ("मन को विषय की ओर मोड़ना", "मन को विषय की ओर मोड़ने", "मन को विषय की ओर मोड़ना", "मन को विषय की ओर मोड़ने", "m"))
    _noun(lex, {"gotrabhussa": ("s", "d"), "gotrabhu": ("s", "n")}, _same("गोत्र-परिवर्तन"))
    _noun(lex, {"vodānassa": ("s", "d"), "vodānaṃ": ("s", "n")}, ("शुद्धि", "शुद्धि", "शुद्धि", "शुद्धि", "f"))
    _noun(lex, {"maggassa": ("s", "d")}, _same("मार्ग"))
    _noun(lex, {"phalassa": ("s", "d")}, _same("फल"))
    _noun(lex, {"phalasamāpattiyā": ("s", "d")}, ("फल की ध्यान-अवस्था",) * 4 + ("f",))
    _noun(lex, {"anulomaṃ": ("s", "n")}, ("अनुरूपता",) * 4 + ("f",))
    _noun(lex, {"bhavaṅgaṃ": ("s", "n"), "bhavaṅgassa": ("s", "d")}, ("जीवन-धारा",) * 4 + ("f",))
    for w, h in [("iddhividhañāṇassa", "अलौकिक शक्तियों"), ("cetopariyañāṇassa", "दूसरों के मन को जानने"),
                 ("pubbenivāsānussatiñāṇassa", "पूर्व जन्मों के अनुस्मरण"),
                 ("yathākammūpagañāṇassa", "प्राणियों के अपने कर्मों के अनुसार जाने"),
                 ("anāgataṃsañāṇassa", "भविष्य को जानने")]:
        _noun(lex, {w: ("s", "d")}, (f"{h} का ज्ञान", f"{h} के ज्ञान", f"{h} के ज्ञान", f"{h} के ज्ञानों", "m"))
    for w, h, c in [("ākāsānañcāyatanaṃ", "अनंत आकाश", "n"), ("viññāṇañcāyatanaṃ", "अनंत चेतना", "n"),
                    ("ākiñcaññāyatanaṃ", "कुछ भी न होने", "n"), ("nevasaññānāsaññāyatanaṃ", "न पहचान न अ-पहचान", "n"),
                    ("ākāsānañcāyatanassa", "अनंत आकाश", "d"), ("viññāṇañcāyatanassa", "अनंत चेतना", "d"),
                    ("ākiñcaññāyatanassa", "कुछ भी न होने", "d"),
                    ("nevasaññānāsaññāyatanassa", "न पहचान न अ-पहचान", "d")]:
        _noun(lex, {w: ("s", c)}, (f"{h} का क्षेत्र", f"{h} के क्षेत्र", f"{h} के क्षेत्र", f"{h} के क्षेत्रों", "m"))
    # fixed multiword nouns (see JOIN)
    _noun(lex, {"imassa_kāyassa": ("s", "d")}, _same("इस शरीर"))
    _noun(lex, {"purejātassa_imassa_kāyassa": ("s", "d")}, _same("पहले उत्पन्न इस शरीर"))
    _noun(lex, {"kabaḷīkāro_āhāro": ("s", "n")}, _same("कौर-कौर खाया जाने वाला भोजन"))
    _noun(lex, {"kilese": ("p", "n")}, ("मन का क्लेश", "मन के क्लेश", "मन के क्लेश", "मन के क्लेशों", "m"))
    _noun(lex, {"maggaṅgāni": ("p", "n")}, ("मार्ग का अंग", "मार्ग के अंग", "मार्ग के अंग", "मार्ग के अंगों", "m"), head=True)
    _noun(lex, {"jhānaṅgāni": ("p", "n")}, ("ध्यान का अंग", "ध्यान के अंग", "ध्यान के अंग", "ध्यान के अंगों", "m"), head=True)
    _noun(lex, {"phalaṃ": ("s", "n")}, _same("फल"))
    _noun(lex, {"maggaṃ": ("s", "n")}, _same("मार्ग"))
    _noun(lex, {"jhānaṃ": ("s", "n")}, _same("ध्यान"))
    _noun(lex, {"gotrabhuṃ": ("s", "n")}, _same("गोत्र-परिवर्तन"))
    _astem(lex, "diṭṭhigatavippayuttalobh", _same("ग़लत दृष्टि से अलग लोभ"))
    # adjectives
    _adj(lex, "pahīn", "छोड़ा~ जा चुका~")
    _adj(lex, "vikkhambhit", "दबाया~ जा चुका~")
    _adj(lex, "ahetukaparāmāsavippayutt", "मूल से रहित, ग़लत धारणा से अलग")
    _adj(lex, "sampayuttak", "जुड़ा~ हुआ~")
    _adj(lex, "vippayuttak", "अलग")
    _adj(lex, "ahetuk", "मूल से रहित")
    _adj(lex, "cittasamuṭṭhān", "मन से उत्पन्न")
    _adj(lex, "pacchājāt", "बाद में उत्पन्न")
    _adj(lex, "vipāk", "कर्म-फल रूपी")
    _adj(lex, "kāyik", "शारीरिक")
    lex["kaṭattā"] = dict(k="A", h="किए गए कर्म से उत्पन्न", n="p", c="d", alt=False)
    for st, h in [("domanassasahagat", "उदासी के साथ होने वाला~"), ("vicikicchāsahagat", "संशय के साथ होने वाला~"),
                  ("uddhaccasahagat", "बेचैनी के साथ होने वाला~"), ("lobhasahagat", "लोभ के साथ होने वाला~"),
                  ("diṭṭhigatavippayuttalobhasahagat", "ग़लत दृष्टि से अलग और लोभ के साथ होने वाला~"),
                  ("diṭṭhigatasampayutt", "ग़लत दृष्टि से जुड़ा~"), ("diṭṭhigatavippayutt", "ग़लत दृष्टि से अलग")]:
        _adj(lex, st, h, alt=True)
    lex["purimā_purimā"] = dict(k="D", h="पहले-पहले का~", n="p", c="n")
    lex["purimo_purimo"] = dict(k="D", h="पहले-पहले का~", n="s", c="n")
    lex["purimaṃ_purimaṃ"] = dict(k="D", h="पहले-पहले का~", n="s", c="n")
    lex["pacchimānaṃ_pacchimānaṃ"] = dict(k="D", h="बाद-बाद का~", n="p", c="d")
    lex["pacchimassa_pacchimassa"] = dict(k="D", h="बाद-बाद का~", n="s", c="d")
    # numerals
    for w, h, v, n, c in [("ekaṃ", "एक", 1, "s", "n"), ("eko", "एक", 1, "s", "n"), ("ekassa", "एक", 1, "s", "d"),
                          ("dve", "दो", 2, "p", "n"), ("dvinnaṃ", "दो", 2, "p", "d"), ("tayo", "तीन", 3, "p", "n"),
                          ("tiṇṇannaṃ", "तीन", 3, "p", "d"), ("cattāro", "चार", 4, "p", "n")]:
        lex[w] = dict(k="NUM", h=h, v=v, n=n, c=c)
    # cluster words
    if GOC[key]["stems"]:
        for e, (n, c) in A_END.items():
            lex["GG" + e] = dict(k="GN", n=n, c=c)
        for stem in ("noGG", "SG", "aSG", "GGsampayutt", "GGsampayuttak", "GGvippayutt", "GGvippayuttak",
                     "GGxSG", "SGnGG", "GGxGGsampayutt", "GGsampayuttnGG", "GGvippSG", "GGvippaSG"):
            base = stem.replace("GGsampayuttak", "GGsampayutt").replace("GGvippayuttak", "GGvippayutt")
            _adj(lex, stem, ITEM[base])
        for st, (h, ho, g) in SUBKIND[key].items():
            _astem(lex, st, (h, ho, h, ho, g))
        for stem in ("noGG", "GGsampayutt", "GGvippayutt", "SG", "aSG", "GGsampayuttnGG", "SGnGG", "GGxSG",
                     "GGxGGsampayutt", "GGvippSG", "GGvippaSG"):
            hf = ITEM[stem].replace("ा~", "ी").replace("~", "") + " प्रधानता"
            _noun(lex, {stem + "ādhipati": ("s", "n")}, (hf, hf, hf, hf, "f"))
    for st, h in [("domanassasahagat", "उदासी के साथ होने वाली"), ("diṭṭhigatavippayuttalobhasahagat",
                  "ग़लत दृष्टि से अलग और लोभ के साथ होने वाली"), ("lobhasahagat", "लोभ के साथ होने वाली")]:
        hf = h + " प्रधानता"
        _noun(lex, {st + "ādhipati": ("s", "n")}, (hf, hf, hf, hf, "f"))
    return lex


# multiword units fused before tokenizing
JOIN = {
    "purejātassa imassa kāyassa": "purejātassa_imassa_kāyassa",
    "imassa kāyassa": "imassa_kāyassa",
    "kabaḷīkāro āhāro": "kabaḷīkāro_āhāro",
    "purimā purimā": "purimā_purimā",
    "purimo purimo": "purimo_purimo",
    "purimaṃ purimaṃ": "purimaṃ_purimaṃ",
    "pacchimānaṃ pacchimānaṃ": "pacchimānaṃ_pacchimānaṃ",
    "pacchimassa pacchimassa": "pacchimassa_pacchimassa",
}

NP = {}
SD = {  # key without commas -> (hindi, gn)
    "nirodhā vuṭṭhahantassa nevasaññānāsaññāyatanaṃ phalasamāpattiyā":
        ("समाप्ति की ध्यान-अवस्था से बाहर आने वाले व्यक्ति में न पहचान न अ-पहचान का क्षेत्र फल की ध्यान-अवस्था के लिए",
         "ms"),
    "tīṇi upanissayā GGo ca sampayuttakā ca khandhā GGassa":
        ("तीन प्रबल आश्रय, {sg} और जुड़े हुए समूह {sgo} के लिए", "mp"),
}
CLAUSE = {
    # closing lines of the counting sections
    "paccanīyaṃ": "नकारात्मक क्रम",
    "anulomapaccanīyaṃ": "सकारात्मक-नकारात्मक क्रम",
    "paccanīyānulomaṃ": "नकारात्मक-सकारात्मक क्रम",
    # abbreviated object lists of the ārammaṇa / adhipati answers
    "dānaṃ": "दान",
    "dānaṃ datvā": "दान देकर",
    "uposathakammaṃ": "उपवास-व्रत",
    "pubbe": "पहले",
    "jhānā": "ध्यान से",
    "taṃ": "उसे",
    "dānaṃ datvā sīlaṃ": "दान देकर, सदाचार",
    "ariyā maggā": "आर्य मार्ग से",
    "ariyā maggaṃ": "आर्य मार्ग",
    "maggā vuṭṭhahitvā maggaṃ": "मार्ग से उठकर मार्ग",
    "ariyā maggā vuṭṭhahitvā maggaṃ": "आर्य मार्ग से उठकर मार्ग",
    "ariyā maggā vuṭṭhahitvā maggaṃ paccavekkhanti": "आर्य मार्ग से उठकर मार्ग पर पुनः विचार करते हैं",
    "phalaṃ paccavekkhanti": "फल पर पुनः विचार करते हैं",
    "phalaṃ": "फल",
    "nibbānaṃ garuṃ": "निर्वाण को महत्व",
    "nibbānaṃ garuṃ katvā paccavekkhanti": "निर्वाण को महत्व देकर पुनः विचार करते हैं",
    "uposathakammaṃ katvā taṃ paccavekkhati": "उपवास-व्रत का पालन करके उस पर पुनः विचार करता है",
    "uposathakammaṃ katvā taṃ assādeti abhinandati": "उपवास-व्रत का पालन करके उसका रस लेता है, उसमें आनंद लेता है",
    "uposathakammaṃ katvā taṃ garuṃ katvā paccavekkhati": "उपवास-व्रत का पालन करके उसे महत्व देकर पुनः विचार करता है",
    "uposathakammaṃ katvā taṃ garuṃ katvā assādeti abhinandati":
        "उपवास-व्रत का पालन करके उसे महत्व देकर उसका रस लेता है, उसमें आनंद लेता है",
    "pubbe suciṇṇāni": "पहले भली-भाँति किए गए कार्यों",
    "jhānā vuṭṭhahitvā jhānaṃ": "ध्यान से उठकर ध्यान",
    "vikkhambhite": "दबाए जा चुके",
    "vikkhambhite kilese": "दबाए जा चुके मन के क्लेशों",
    "pubbe samudāciṇṇe kilese jānanti": "पहले बार-बार उठे मन के क्लेशों को जानते हैं",
    "ariyā noGGe pahīne kilese": "आर्य {rupi} न होने वाले, छोड़े जा चुके मन के क्लेशों",
    "ariyā GGvippayutte pahīne kilese paccavekkhanti": "आर्य {w} से अलग, छोड़े जा चुके मन के क्लेशों पर पुनः विचार करते हैं",
    "dibbena cakkhunā rūpaṃ passati": "दिव्य आँख से दृश्य रूप को देखता है",
    "domanassaṃ uppajjati": "उदासी उत्पन्न होती है",
    "rāgo": "राग",
    "diṭṭhi": "दृष्टि",
    "vicikicchā": "संशय",
    "uddhaccaṃ": "बेचैनी",
    "domanassaṃ": "उदासी",
    "taṃ ārabbha rāgo": "उसे विषय बनाकर राग",
    "cakkhuṃ": "आँख",
    "assādeti abhinandati": "रस लेता है, उसमें आनंद लेता है",
    "taṃ assādeti abhinandati": "उसका रस लेता है, उसमें आनंद लेता है",
    "phalā vuṭṭhahitvā phalaṃ": "फल से उठकर फल",
    "abhinandati": "उसमें आनंद लेता है",
    "vipassati": "अंतर्दृष्टि से देखता है",
    "jhānaṃ": "ध्यान",
    "maggaṃ": "मार्ग",
    "gotrabhuṃ": "गोत्र-परिवर्तन",
    "ariyā maggā vuṭṭhahitvā maggaṃ garuṃ katvā": "आर्य मार्ग से उठकर मार्ग को महत्व देकर",
    "jhānaṃ uppādeti": "ध्यान उत्पन्न करता है",
    "pubbe samudāciṇṇe": "पहले बार-बार उठे",
    "vipassanaṃ": "अंतर्दृष्टि",
    "abhiññaṃ": "उच्च ज्ञान",
    "ariyā GGvippayutte pahīne kilese": "आर्य {w} से अलग, छोड़े जा चुके मन के क्लेशों",
    "vipassanaṃ uppādeti": "अंतर्दृष्टि उत्पन्न करता है",
    "maggaṃ uppādeti": "मार्ग उत्पन्न करता है",
    "abhiññaṃ uppādeti": "उच्च ज्ञान उत्पन्न करता है",
    "purimā purimā noGGā khandhā pacchimānaṃ": "पहले-पहले के {rupi} न होने वाले समूह बाद-बाद के",
    "purimā purimā GGvippayuttā khandhā pacchimānaṃ": "पहले-पहले के {w} से अलग समूह बाद-बाद के",
    # pakatūpanissaya verbs
    "dānaṃ deti": "दान देता है",
    "samāpattiṃ uppādeti": "ध्यान-अवस्था उत्पन्न करता है",
    "mānaṃ jappeti": "अहंकार पालता है",
    "diṭṭhiṃ gaṇhāti": "दृष्टि ग्रहण करता है",
    "saṅghaṃ bhindati": "संघ में फूट डालता है",
    "pāṇaṃ hanati": "जीव की हत्या करता है",
}
CLAUSE_BLOCK = set()
LABEL = {
    "sahajātaṃ": "सह-उत्पत्ति", "purejātaṃ": "पूर्व-उत्पत्ति", "pacchājātaṃ": "पश्चात्-उत्पत्ति",
    "āhāraṃ": "आहार", "indriyaṃ": "क्षमता", "sahajātā": "सह-उत्पत्ति", "sahajāto": "सह-उत्पत्ति",
    "pacchājātā": "पश्चात्-उत्पत्ति", "nānākkhaṇikā": "भिन्न क्षण",
    "ārammaṇādhipati": "विषय रूपी प्रधानता", "sahajātādhipati": "सह-उत्पत्ति रूपी प्रधानता",
    "ārammaṇūpanissayo": "विषय रूपी प्रबल आश्रय", "anantarūpanissayo": "निकटता रूपी प्रबल आश्रय",
    "pakatūpanissayo": "स्वाभाविक प्रबल आश्रय", "ārammaṇapurejātaṃ": "विषय रूपी पूर्व-उत्पत्ति",
    "vatthupurejātaṃ": "आधार रूपी पूर्व-उत्पत्ति",
}
SUBJ_PERSON = {"ariyā": "आर्य", "sekkhā": "सीखने के चरण वाले व्यक्ति", "arahā": "अर्हत्"}

# ------------------------------------------------------------------ headings

HEAD = {
    "Āsavagocchakaṃ": "मन के मैलों का वर्ग",
    "Saññojanagocchakaṃ": "बंधनों का वर्ग",
    "Ganthagocchakaṃ": "गाँठों का वर्ग",
    "Oghayogagocchakaṃ": "बाढ़ों और जकड़नों के वर्ग",
    "Nīvaraṇagocchakaṃ": "बाधाओं का वर्ग",
    "Parāmāsagocchakaṃ": "ग़लत धारणा का वर्ग",
    "Oghādidukāni": "बाढ़ आदि वाले दो-दो के वर्गीकरण",
    "Āsavadukaṃ": "मन के मैल वाला दो का वर्गीकरण",
    "Sāsavadukaṃ": "मन के मैलों के विषय वाला दो का वर्गीकरण",
    "Āsavasampayuttadukaṃ": "मन के मैलों से जुड़ाव वाला दो का वर्गीकरण",
    "Āsavasāsavadukaṃ": "मन के मैल और मन के मैलों के विषय वाला दो का वर्गीकरण",
    "Āsavaāsavasampayuttadukaṃ": "मन के मैल और मन के मैलों से जुड़ाव वाला दो का वर्गीकरण",
    "Āsavavippayuttasāsavadukaṃ": "मन के मैलों से अलगाव और मन के मैलों के विषय वाला दो का वर्गीकरण",
    "Saññojanadukaṃ": "बंधन वाला दो का वर्गीकरण",
    "Saññojaniyadukaṃ": "बंधनों के विषय वाला दो का वर्गीकरण",
    "Saññojanasampayuttadukaṃ": "बंधनों से जुड़ाव वाला दो का वर्गीकरण",
    "Saññojanasaññojaniyadukaṃ": "बंधन और बंधनों के विषय वाला दो का वर्गीकरण",
    "Saññojanasaññojanasampayuttadukaṃ": "बंधन और बंधनों से जुड़ाव वाला दो का वर्गीकरण",
    "Saññojanavippayuttasaññojaniyadukaṃ": "बंधनों से अलगाव और बंधनों के विषय वाला दो का वर्गीकरण",
    "Ganthadukaṃ": "गाँठ वाला दो का वर्गीकरण",
    "Ganthaniyadukaṃ": "गाँठों के विषय वाला दो का वर्गीकरण",
    "Ganthasampayuttadukaṃ": "गाँठों से जुड़ाव वाला दो का वर्गीकरण",
    "Ganthaganthaniyadukaṃ": "गाँठ और गाँठों के विषय वाला दो का वर्गीकरण",
    "Ganthaganthasampayuttadukaṃ": "गाँठ और गाँठों से जुड़ाव वाला दो का वर्गीकरण",
    "Ganthavippayuttaganthaniyadukaṃ": "गाँठों से अलगाव और गाँठों के विषय वाला दो का वर्गीकरण",
    "Nīvaraṇadukaṃ": "बाधा वाला दो का वर्गीकरण",
    "Nīvaraṇiyadukaṃ": "बाधाओं के विषय वाला दो का वर्गीकरण",
    "Nīvaraṇasampayuttadukaṃ": "बाधाओं से जुड़ाव वाला दो का वर्गीकरण",
    "Nīvaraṇanīvaraṇiyadukaṃ": "बाधा और बाधाओं के विषय वाला दो का वर्गीकरण",
    "Nīvaraṇanīvaraṇasampayuttadukaṃ": "बाधा और बाधाओं से जुड़ाव वाला दो का वर्गीकरण",
    "Nīvaraṇavippayuttanīvaraṇiyadukaṃ": "बाधाओं से अलगाव और बाधाओं के विषय वाला दो का वर्गीकरण",
    "Parāmāsadukaṃ": "ग़लत धारणा वाला दो का वर्गीकरण",
    "Parāmaṭṭhadukaṃ": "ग़लत धारणा के विषय वाला दो का वर्गीकरण",
    "Parāmāsasampayuttadukaṃ": "ग़लत धारणा से जुड़ाव वाला दो का वर्गीकरण",
    "Parāmāsaparāmaṭṭhadukaṃ": "ग़लत धारणा और ग़लत धारणा के विषय वाला दो का वर्गीकरण",
    "Parāmāsavippayuttaparāmaṭṭhadukaṃ": "ग़लत धारणा से अलगाव और ग़लत धारणा के विषय वाला दो का वर्गीकरण",
    "Sahajātavāro": "सह-उत्पत्ति का खंड",
    "Paccayavāro": "कारण का खंड",
    "Nissayavāro": "आश्रय का खंड",
    "Saṃsaṭṭhavāro": "घुले-मिले होने का खंड",
    "Sampayuttavāro": "जुड़ाव का खंड",
    "Paccanīyuddhāro": "नकारात्मक क्रम के लिए कारणों की छँटाई",
    "Paccayacatukkaṃ": "कारणों के चार क्रम",
    "Paccayānulomādi": "कारणों का सकारात्मक क्रम आदि",
    "Paṭiccavārādi": "निर्भरता का खंड आदि",
    "Vārasattakaṃ": "सात खंड",
    "Sahajāta-paccaya-nissaya-saṃsaṭṭha-sampayuttavāro": "सह-उत्पत्ति, कारण, आश्रय, घुले-मिले होने और जुड़ाव का खंड",
    "Nissaya-saṃsaṭṭha-sampayuttavāro": "आश्रय, घुले-मिले होने और जुड़ाव का खंड",
    "Hetudukaṃ": "मूल-कारण के साथ दो कारणों का मेल",
    "Nahetudukaṃ": "मूल-कारण के अभाव के साथ दो कारणों का मेल",
    "Vipākāhārapaccayā": "कर्म-फल-कारण और आहार-कारण",
    "Pacchājātāsevanapaccayā": "पश्चात्-उत्पत्ति-कारण और पुनरावृत्ति-कारण",
    "Pacchājāta-āsevanapaccayā": "पश्चात्-उत्पत्ति-कारण और पुनरावृत्ति-कारण",
}
_CONDS = ["hetu", "ārammaṇa", "adhipati", "anantara", "samanantara", "sahajāta", "aññamañña", "nissaya",
          "upanissaya", "purejāta", "pacchājāta", "āsevana", "kamma", "vipāka", "āhāra", "indriya", "jhāna",
          "magga", "sampayutta", "vippayutta", "atthi", "natthi", "vigata", "avigata"]
_NAMES = ["मूल-कारण", "विषय-कारण", "प्रधानता-कारण", "निकटता-कारण", "पूर्ण निकटता-कारण", "सह-उत्पत्ति-कारण",
          "परस्पर-कारण", "आश्रय-कारण", "प्रबल आश्रय-कारण", "पूर्व-उत्पत्ति-कारण", "पश्चात्-उत्पत्ति-कारण",
          "पुनरावृत्ति-कारण", "कर्म-कारण", "कर्म-फल-कारण", "आहार-कारण", "क्षमता-कारण", "ध्यान-कारण", "मार्ग-कारण",
          "जुड़ाव-कारण", "अलगाव-कारण", "उपस्थिति-कारण", "अनुपस्थिति-कारण", "विलीनता-कारण", "अविलीनता-कारण"]
for _k, _h in zip(_CONDS, _NAMES):
    _neg = "no" if _k in ("atthi", "natthi", "vigata", "avigata") else "na"
    HEAD[_k[0].upper() + _k[1:] + "paccayādi"] = _h + " आदि"
    _n = _neg + _k
    HEAD[_n[0].upper() + _n[1:] + "paccayādi"] = _h + " का अभाव आदि"

# closing lines «X niṭṭhitaṃ.» use HEAD[X] + « समाप्त।»

LINE_HAND = {
    # 3-06
    "Oghaṃ dhammaṃ paṭicca ogho dhammo uppajjati hetupaccayā…pe….":
        "बाढ़ रूपी परिघटना पर निर्भर होकर बाढ़ रूपी परिघटना मूल-कारण से उत्पन्न होती है…।",
    "Yogaṃ dhammaṃ paṭicca yogo dhammo uppajjati hetupaccayā…pe… (dvepi gocchakā āsavagocchakasadisā "
    "ninnānākaraṇā).":
        "जकड़न रूपी परिघटना पर निर्भर होकर जकड़न रूपी परिघटना मूल-कारण से उत्पन्न होती है… (दोनों वर्ग मन के मैलों "
        "के वर्ग के समान हैं, बिना किसी अंतर के)।",
    # 3-07 summary verse
    "Dvikkhattuṃ kāmacchandena, catukkhattuṃ paṭighena ca;": "इंद्रिय-सुखों की चाह के साथ दो बार, और चिढ़ के साथ चार बार;",
    "Uddhaccaṃ vicikicchā ca, ubhopete sakiṃ sakiṃ;": "बेचैनी और संशय, ये दोनों एक-एक बार;",
    "Nīvaraṇānaṃ nīvaraṇehi, aṭṭhavidhaṃ payojanaṃ.": "बाधाओं का बाधाओं के साथ, आठ प्रकार का मेल।",
}
VARIANTS = {"{thīnamiddhanīvaraṇaṃ (syā.)}": ("वर्तनी-भेद", "आलस्य और तंद्रा की बाधा")}
SLIPS = {"parāmāsampayuttakānaṃ": "parāmāsasampayuttakānaṃ"}

# ------------------------------------------------------------------ editorial notes (inside the parentheses)

_LOKIYA = "जैसे बीच के छोटे दो-दो के वर्गीकरणों में लौकिक परिघटनाओं वाला दो का वर्गीकरण है, वैसे ही"
_LOKIYA_SAD = "बीच के छोटे दो-दो के वर्गीकरणों में लौकिक परिघटनाओं वाले दो के वर्गीकरण के समान"
_VARA6 = ("निर्भरता का खंड भी, सह-उत्पत्ति का खंड भी, कारण का खंड भी, आश्रय का खंड भी, "
          "घुले-मिले होने का खंड भी और जुड़ाव का खंड भी")
_VARA5 = "सह-उत्पत्ति का खंड भी, कारण का खंड भी, आश्रय का खंड भी, घुले-मिले होने का खंड भी और जुड़ाव का खंड भी"
_VARA4 = "कारण का खंड भी, आश्रय का खंड भी, घुले-मिले होने का खंड भी और जुड़ाव का खंड भी"
NOTE = {
    "saṃkhittaṃ": "संक्षिप्त",
    "saṃkhittaṃ.": "संक्षिप्त।",
    "cakkaṃ": "चक्र",
    "sabbaṃ cakkaṃ": "पूरा चक्र",
    "cakkaṃ bandhitabbaṃ": "चक्र बाँधना चाहिए",
    "evaṃ cakkaṃ bandhitabbaṃ": "इसी तरह चक्र बाँधना चाहिए",
    "cakkaṃ bandhitabbaṃ. saṃkhittaṃ": "चक्र बाँधना चाहिए। संक्षिप्त",
    "cakkaṃ. saṃkhittaṃ": "चक्र। संक्षिप्त",
    "cakkaṃ. saṃkhittaṃ.": "चक्र। संक्षिप्त।",
    "cakkaṃ. evaṃ sabbe paccayā kātabbā.": "चक्र। इसी तरह सभी कारण करने चाहिए।",
    "ekekampi cakkaṃ kātabbaṃ": "एक-एक का भी चक्र बनाना चाहिए",
    "mūlaṃ kātabbaṃ": "मूल वाक्य बनाना चाहिए",
    "mūlaṃ kātabbaṃ.": "मूल वाक्य बनाना चाहिए।",
    "mūlaṃ pucchitabbaṃ": "मूल वाक्य पूछना चाहिए",
    "mūlaṃ pucchitabbaṃ ": "मूल वाक्य पूछना चाहिए",
    "pucchitabbaṃ mūlaṃ": "मूल वाक्य पूछना चाहिए",
    "mūlā pucchitabbā": "मूल वाक्य पूछने चाहिए",
    "tīsupi mūlā pucchitabbā": "तीनों में भी मूल वाक्य पूछने चाहिए",
    "mūlaṃ pucchitabbaṃ, tīṇipi upanissayā": "मूल वाक्य पूछना चाहिए, तीनों प्रबल आश्रय भी",
    "mūlaṃ, tīṇipi upanissayā": "मूल वाक्य, तीनों प्रबल आश्रय भी",
    "tīṇi upanissayā": "तीन प्रबल आश्रय",
    "sabbattha nava": "हर जगह नौ",
    " sabbattha nava, saṃkhittaṃ": "हर जगह नौ, संक्षिप्त",
    "sabbattha cha": "हर जगह छह",
    "sabbattha satta": "हर जगह सात",
    "sabbattha cattāri": "हर जगह चार",
    "sabbattha dve": "हर जगह दो",
    "sabbattha pañca": "हर जगह पाँच",
    "sabbattha tīṇi": "हर जगह तीन",
    "sabbattha ekaṃ": "हर जगह एक",
    "tīṇi": "तीन",
    "yāva asaññasattā": "पहचान-रहित प्राणियों तक",
    "yāva āsaññasattā": "पहचान-रहित प्राणियों तक",
    "yāva asaññasattā, saṃkhittaṃ": "पहचान-रहित प्राणियों तक, संक्षिप्त",
    "yāva asaññasattā. saṃkhittaṃ": "पहचान-रहित प्राणियों तक। संक्षिप्त",
    "yāva asaññasattā, mahābhūtā": "पहचान-रहित प्राणियों तक, महाभूत",
    "yāva asaññasattā mahābhūtā": "पहचान-रहित प्राणियों के महाभूतों तक",
    "yāva ajjhattikā mahābhūtā": "आंतरिक महाभूतों तक",
    "yāva mahābhūtā": "महाभूतों तक",
    "yāva paṭisandhi": "पुनर्जन्म तक",
    "yāva āvajjanāya": "मन को विषय की ओर मोड़ने तक",
    "yāva āvajjanā tāva kātabbā": "मन को विषय की ओर मोड़ने तक करना चाहिए",
    "yāva āvajjanā sabbaṃ kātabbaṃ": "मन को विषय की ओर मोड़ने तक सब करना चाहिए",
    "paṭiccasadisaṃ": "निर्भरता के खंड के समान",
    "paṭiccasadisā": "निर्भरता के खंड के समान",
    "paṭiccavārasadiso": "निर्भरता के खंड के समान",
    "paṭiccavārasadisaṃ": "निर्भरता के खंड के समान",
    "paṭiccavārasadisā": "निर्भरता के खंड के समान",
    "GGamūlakaṃ tīṇi, paṭiccasadisā": "{rupi} पद से शुरू होने वाले तीन, निर्भरता के खंड के समान",
    "evaṃ GGamūle tīṇi ": "इसी तरह {rupi} पद से शुरू होने वाली शृंखला में तीन",
    "sahajātavāro paṭiccavārasadiso.": "सह-उत्पत्ति का खंड निर्भरता के खंड के समान है।",
    "sahajātavāro paṭiccavārasadiso": "सह-उत्पत्ति का खंड निर्भरता के खंड के समान है",
    "sahajātavāropi paṭiccavārasadiso.": "सह-उत्पत्ति का खंड भी निर्भरता के खंड के समान है।",
    "nissayavāro paccayavārasadiso.": "आश्रय का खंड कारण के खंड के समान है।",
    "nissayavāro paccayavārasadiso": "आश्रय का खंड कारण के खंड के समान है",
    "nissayavāropi paccayavārasadiso.": "आश्रय का खंड भी कारण के खंड के समान है।",
    "sampayuttavāro saṃsaṭṭhavārasadiso": "जुड़ाव का खंड घुले-मिले होने के खंड के समान है",
    "sampayuttavāropi saṃsaṭṭhavārasadiso.": "जुड़ाव का खंड भी घुले-मिले होने के खंड के समान है।",
    "gaṇanāpi sampayuttavāropi saṃsaṭṭhavārasadiso.": "गणना भी और जुड़ाव का खंड भी घुले-मिले होने के खंड के समान है।",
    "nissayavāro paccayavārasadisova. saṃsaṭṭhavāropi sampayuttavāropi nava pañhā kātabbā, rūpaṃ natthi.":
        "आश्रय का खंड कारण के खंड के समान ही है। घुले-मिले होने के खंड में भी और जुड़ाव के खंड में भी नौ प्रश्न "
        "करने चाहिए, भौतिक रूप नहीं है।",
    "sahajātavāropi evaṃ kātabbo.": "सह-उत्पत्ति का खंड भी इसी तरह करना चाहिए।",
    "sahajātavāropi evaṃ vitthāretabbo": "सह-उत्पत्ति के खंड का भी इसी तरह विस्तार करना चाहिए",
    "saṃsaṭṭhavāropi sampayuttavāropi evaṃ kātabbā.":
        "घुले-मिले होने का खंड भी और जुड़ाव का खंड भी इसी तरह करने चाहिए।",
    "evaṃ itarepi dve gaṇanā kātabbā": "इसी तरह बाकी दो गणनाएँ भी करनी चाहिए",
    "evaṃ itare dve gaṇanāpi sampayuttavāropi kātabbo.": "इसी तरह बाकी दो गणनाएँ भी और जुड़ाव का खंड भी करना चाहिए।",
    "itare dve gaṇanāpi sampayuttavāropi kātabbo.": "बाकी दो गणनाएँ भी और जुड़ाव का खंड भी करना चाहिए।",
    "evaṃ itare dve gaṇanāpi sampayuttavārāpi kātabbā.":
        "इसी तरह बाकी दो गणनाएँ भी और जुड़ाव के खंड भी करने चाहिए।",
    "evaṃ itare dve gaṇanāpi nissayavāropi kātabbo.": "इसी तरह बाकी दो गणनाएँ भी और आश्रय का खंड भी करना चाहिए।",
    "evaṃ itarepi dve gaṇanā ca nissayavāro ca kātabbo.":
        "इसी तरह बाकी दो गणनाएँ भी और आश्रय का खंड भी करना चाहिए।",
    "evaṃ itare dve gaṇanāpi sahajātavāropi kātabbo. paccayavāropi nissayavāropi saṃsaṭṭhavāropi "
    "sampayuttavāropi paṭiccavārasadisā.":
        "इसी तरह बाकी दो गणनाएँ भी और सह-उत्पत्ति का खंड भी करना चाहिए। " + _VARA4 + " निर्भरता के खंड के समान हैं।",
    "evaṃ itare dve gaṇanāpi sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi "
    "paṭiccavārasadisā.":
        "इसी तरह बाकी दो गणनाएँ भी, " + _VARA5 + " निर्भरता के खंड के समान हैं।",
    "evaṃ itare dve gaṇanāpi sahajātavārampi paccayavārampi nissayavārampi saṃsaṭṭhavārampi "
    "sampayuttavārampi paripuṇṇaṃ paṭiccasadisā.":
        "इसी तरह बाकी दो गणनाएँ भी, " + _VARA5 + " परिपूर्ण, निर्भरता के खंड के समान हैं।",
    "evaṃ sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi paṭiccavārasadisā "
    "ninnānākaraṇā.":
        "इसी तरह " + _VARA5 + " निर्भरता के खंड के समान हैं, बिना किसी अंतर के।",
    "evaṃ paṭiccavāropi sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi "
    "yathā GGadukaṃ evaṃ kātabbaṃ, ninnānaṃ.":
        "इसी तरह " + _VARA6 + " जैसे {duka_o} में, वैसे ही करना चाहिए, बिना किसी अंतर के।",
    "paṭiccavārampi sahajātavārampi paccayavārampi nissayavārampi saṃsaṭṭhavārampi sampayuttavārampi "
    "GGadukasadisaṃ ninnānākaraṇaṃ.":
        _VARA6 + " {duka_o} के समान है, बिना किसी अंतर के।",
    "evaṃ sabbe gaṇanā gaṇetabbā": "इसी तरह सभी गणनाएँ गिननी चाहिए",
    "evaṃ sabbe gaṇanā vibhajitabbā, GGadukasadisaṃ ninnānākaraṇaṃ.":
        "इसी तरह सभी गणनाओं का विश्लेषण करना चाहिए, {duka_o} के समान, बिना किसी अंतर के।",
    "evaṃ gaṇetabbaṃ": "इसी तरह गिनना चाहिए",
    "evaṃ gaṇetabbaṃ, saṃkhittaṃ": "इसी तरह गिनना चाहिए, संक्षिप्त",
    "saṃkhittaṃ, evaṃ gaṇetabbaṃ": "संक्षिप्त, इसी तरह गिनना चाहिए",
    "evaṃ sabbaṃ gaṇetabbaṃ": "इसी तरह सब गिनना चाहिए",
    "yathā cūḷantaraduke lokiyadukaṃ evaṃ kātabbaṃ ninnānākaraṇaṃ.": _LOKIYA + " बिना किसी अंतर के करना चाहिए।",
    "yathā cūḷantaraduke lokiyadukaṃ evaṃ vitthāretabbaṃ ninnānākaraṇaṃ":
        _LOKIYA + " बिना किसी अंतर के विस्तार करना चाहिए",
    "yathā cūḷantaraduke lokiyadukaṃ evaṃ vitthāretabbaṃ ninnānākaraṇaṃ, saṃkhittaṃ.":
        _LOKIYA + " बिना किसी अंतर के विस्तार करना चाहिए, संक्षिप्त।",
    "yathā cūḷantaraduke lokiyadukaṃ evaṃ vibhajitabbaṃ ninnānākaraṇaṃ.":
        _LOKIYA + " बिना किसी अंतर के विश्लेषण करना चाहिए।",
    "SGadukaṃ yathā cūḷantaraduke lokiyadukaṃ evaṃ kātabbaṃ ninnānākaraṇaṃ":
        "{sduka}, " + _LOKIYA + " बिना किसी अंतर के करना चाहिए",
    "SGadukaṃ yathā lokiyadukaṃ evaṃ kātabbaṃ ninnānākaraṇaṃ":
        "{sduka}, जैसे लौकिक परिघटनाओं वाला दो का वर्गीकरण है, वैसे ही बिना किसी अंतर के करना चाहिए",
    "cūḷantaraduke lokiyadukasadisaṃ, ninnānākaraṇaṃ.": _LOKIYA_SAD + ", बिना किसी अंतर के।",
    "imaṃ dukaṃ cūḷantaraduke lokiyadukasadisaṃ ninnānākaraṇaṃ.":
        "यह दो का वर्गीकरण " + _LOKIYA_SAD + " है, बिना किसी अंतर के।",
    "vibhajitabbaṃ": "विश्लेषण करना चाहिए",
    "saṃkhittaṃ, vibhajitabbaṃ": "संक्षिप्त, विश्लेषण करना चाहिए",
    "vibhajitabbaṃ āsavasadisaṃ": "विश्लेषण करना चाहिए, मन के मैलों के समान",
    "saṃkhittaṃ, āsavasadisaṃ": "संक्षिप्त, मन के मैलों के समान",
    "āsavasadisaṃ": "मन के मैलों के समान",
    "saṃkhittaṃ. āsavagocchakasadisaṃ. naārammaṇāpi sabbe uddharitabbā.":
        "संक्षिप्त। मन के मैलों के वर्ग के समान। विषय-कारण के अभाव वाले भी सभी निकालने चाहिए।",
    "dvepi gocchakā āsavagocchakasadisā ninnānākaraṇā": "दोनों वर्ग मन के मैलों के वर्ग के समान हैं, बिना किसी अंतर के",
    "anulomamātikā": "सकारात्मक क्रम की मूल सूची",
    "anulomamātikā ": "सकारात्मक क्रम की मूल सूची",
    "anulomamātikā kātabbā": "सकारात्मक क्रम की मूल सूची बनानी चाहिए",
    "anulomamātikā vitthāretabbā": "सकारात्मक क्रम की मूल सूची का विस्तार करना चाहिए",
    "anulomapadāni gaṇitabbāni": "सकारात्मक क्रम के पद गिनने चाहिए",
    "anulomapadāni kātabbāni": "सकारात्मक क्रम के पद करने चाहिए",
    "anulomapadāni paripuṇṇāni kātabbāni": "सकारात्मक क्रम के पद परिपूर्ण करने चाहिए",
    "anulomapadā paripuṇṇā": "सकारात्मक क्रम के पद परिपूर्ण हैं",
    "anulomagaṇanā": "सकारात्मक क्रम की गणना",
    "āvajjanāpi vuṭṭhānampi natthi ": "मन को विषय की ओर मोड़ना भी और बाहर आना भी नहीं है",
    "āvajjanāpi vuṭṭhānampi natthi, sabbattha purimā purimā kātabbā":
        "मन को विषय की ओर मोड़ना भी और बाहर आना भी नहीं है, हर जगह पहले-पहले वाले करने चाहिए",
    "anantarasadisaṃ, āvajjanāpi vuṭṭhānampi natthi":
        "निकटता-कारण के समान, मन को विषय की ओर मोड़ना भी और बाहर आना भी नहीं है",
    "saṃkhittaṃ. vitthāretabbaṃ": "संक्षिप्त। विस्तार करना चाहिए",
    "saṃkhittaṃ, vitthāretabbaṃ": "संक्षिप्त, विस्तार करना चाहिए",
    "saṃkhittaṃ, evaṃ kātabbaṃ": "संक्षिप्त, इसी तरह करना चाहिए",
    "evaṃ vitthāretabbaṃ": "इसी तरह विस्तार करना चाहिए",
    "evaṃ sabbaṃ vitthāretabbaṃ": "इसी तरह सब का विस्तार करना चाहिए",
    "sabbaṃ vitthāretabbaṃ": "सब का विस्तार करना चाहिए",
    "evaṃ sabbattha kātabbaṃ": "इसी तरह हर जगह करना चाहिए",
    "evaṃ sabbe paccayā vitthāretabbā. saṃkhittaṃ.": "इसी तरह सभी कारणों का विस्तार करना चाहिए। संक्षिप्त।",
    "ārammaṇanayena kātabbā": "विषय-कारण की विधि से करने चाहिए",
    "ārabbha kātabbā": "विषय बनाकर करने चाहिए",
    "ārabbhayeva kātabbā": "विषय बनाकर ही करने चाहिए",
    "ārabbha kātabbāni GGadukasadisaṃ": "विषय बनाकर करने चाहिए, {duka_o} के समान",
    "dutiyagamanaṃ": "दूसरा प्रसंग",
    "tīṇi ārammaṇasadisā, garukārammaṇā kātabbā": "तीन, विषय-कारण के समान, महत्व दिए गए विषयों से करने चाहिए",
    "tīṇi, garukārammaṇā": "तीन, महत्व दिए गए विषय",
    "ārammaṇasadisā, garukārammaṇā": "विषय-कारण के समान, महत्व दिए गए विषय",
    "ārammaṇasadisā, garukārammaṇā kātabbā": "विषय-कारण के समान, महत्व दिए गए विषयों से करने चाहिए",
    "garukārammaṇā": "महत्व दिए गए विषय",
    "garukārammaṇāyeva": "महत्व दिए गए विषय ही",
    "vatthu ca dassetabbaṃ": "आधार भी दिखाना चाहिए",
    "napacchājātapaccayā nava, naāsevanapaccayā nava.": "पश्चात्-उत्पत्ति-कारण के बिना नौ, पुनरावृत्ति-कारण के बिना नौ।",
    "idha assādanā natthi": "यहाँ रस लेना नहीं है",
    "sahajātasadisaṃ": "सह-उत्पत्ति-कारण के समान",
    "pañhāvāre hetupaccayepi ārammaṇapaccayepi lokuttaraṃ na kātabbaṃ, sekhā gotrabhuṃ paccavekkhanti, "
    "vodānaṃ paccavekkhantīti kātabbā. adhipatipaccayampi sabbaṃ jānitvā kātabbaṃ.":
        "प्रश्नों के खंड में मूल-कारण में भी और विषय-कारण में भी लोकोत्तर को नहीं लेना चाहिए, “सीखने के चरण वाले "
        "व्यक्ति गोत्र-परिवर्तन पर पुनः विचार करते हैं, शुद्धि पर पुनः विचार करते हैं” ऐसा करना चाहिए। "
        "प्रधानता-कारण भी सब जानकर करना चाहिए।",
    "GGadukepi anantaraṃ iminā sadisaṃ kātabbaṃ. āvajjanāpi vuṭṭhānampi evaṃ samuddiṭṭhaṃ saṃkhittaṃ. "
    "sabbaṃ paripuṇṇaṃ. GGadukasadisaṃ kātabbaṃ, ninnānaṃ.":
        "{duka_o} में भी निकटता-कारण इसी के समान करना चाहिए। मन को विषय की ओर मोड़ना भी और बाहर आना भी इसी तरह "
        "बताया गया है, संक्षिप्त। सब परिपूर्ण है। {duka_o} के समान करना चाहिए, बिना किसी अंतर के।",
    "vipākaṃ natthi": "कर्म-फल-कारण नहीं है",
    "nahetumūlakaṃ natthi": "मूल-कारण के अभाव से शुरू होने वाली शृंखला नहीं है",
    "ārammaṇasadisāyeva, purimā purimāti kātabbā.": "विषय-कारण के समान ही, “पहले-पहले वाले” ऐसा करना चाहिए।",
    "idha purimā purimāti natthi": "यहाँ “पहले-पहले वाले” नहीं है",
    "ārammaṇasadisaṃyeva, vibhajanā natthi… tīṇi. upanissayaṃ sabbaṃ kātabbaṃ":
        "विषय-कारण के समान ही, विश्लेषण नहीं है… तीन। प्रबल आश्रय पूरा करना चाहिए",
    "ārammaṇapaccaye rūpaṃ natthi. adhipatipaccayo hetusadiso, vicikicchāsaññojanaṃ natthi.":
        "विषय-कारण में भौतिक रूप नहीं है। प्रधानता-कारण मूल-कारण के समान है, संशय का बंधन नहीं है।",
    "yattha yattha vatthu labbhati, tattha tattha ninnetabbaṃ": "जहाँ-जहाँ आधार लागू होता है, वहाँ-वहाँ जोड़ना चाहिए",
    "evaṃ nava pañhā. arūpāyeva kātabbā": "इसी तरह नौ प्रश्न। अभौतिक ही करने चाहिए",
    "tiṇṇampi ārammaṇādhipati, sahajātādhipatipi kātabbā, vibhajitabbā tīṇipi":
        "तीनों के लिए विषय रूपी प्रधानता और सह-उत्पत्ति रूपी प्रधानता भी करनी चाहिए, तीनों का भी विश्लेषण करना चाहिए",
    "evaṃ dvepi kātabbā": "इसी तरह दोनों करने चाहिए",
    "evaṃ tīṇipi": "इसी तरह तीनों भी",
    "GGagocchake paṭhamadukasadisaṃ.": "{cluster_o} में पहले दो के वर्गीकरण के समान।",
    "evaṃ imampi dukaṃ vitthāretabbaṃ, ninnānākaraṇaṃ ṭhapetvā lokuttaraṃ":
        "इसी तरह इस दो के वर्गीकरण का भी विस्तार करना चाहिए, लोकोत्तर को छोड़कर बिना किसी अंतर के",
    "imāsu tīsupi pañhāsu ārammaṇādhipatipi sahajātādhipatipi kātabbā":
        "इन तीनों प्रश्नों में विषय रूपी प्रधानता भी और सह-उत्पत्ति रूपी प्रधानता भी करनी चाहिए",
    "ninnānākaraṇaṃ, vibhajanā natthi. ārammaṇasadisā": "बिना किसी अंतर के, विश्लेषण नहीं है। विषय-कारण के समान",
    "saṃkhittaṃ. evaṃ nava pañhā kātabbā. tīsuyeva padesu parivattetabbā, nānākkhaṇikā natthi.":
        "संक्षिप्त। इसी तरह नौ प्रश्न करने चाहिए। तीनों पदों में ही उलट-पलट करना चाहिए, भिन्न क्षण नहीं है।",
    "dve pañhā kātabbā": "दो प्रश्न करने चाहिए",
    "arūpe sīlabbataparāmāso natthi, evaṃ nava pañhā kātabbā":
        "अभौतिक लोक में सदाचार और व्रतों के बारे में ग़लत धारणा नहीं है, इसी तरह नौ प्रश्न करने चाहिए",
    "dve āvajjanā kātabbā, paṭhamo natthi": "मन को विषय की ओर मोड़ना दो बार करना चाहिए, पहला नहीं है",
    "ekampi vuṭṭhānaṃ kātabbaṃ, majjhe": "एक बाहर आना भी करना चाहिए, बीच में",
    "napurejāte vibhajantena arūpaṃ paṭhamaṃ kātabbaṃ, rūpaṃ yattha labbhati pacchā kātabbaṃ, "
    "paṭighañca arūpe natthi":
        "पूर्व-उत्पत्ति-कारण के अभाव में विश्लेषण करते हुए अभौतिक को पहले करना चाहिए, भौतिक रूप जहाँ लागू होता है, "
        "उसे बाद में करना चाहिए, और चिढ़ अभौतिक लोक में नहीं है",
    "evaṃ nava pañhā vitthāretabbā": "इसी तरह नौ प्रश्नों का विस्तार करना चाहिए",
    "evaṃ itarepi tīṇi vitthāretabbā": "इसी तरह बाकी तीन का भी विस्तार करना चाहिए",
    "ārabbha kātabbā. imasmiṃ duke lokuttaraṃ natthi, GGadukasadisaṃ, ninnānākaraṇaṃ. \"SGa\"nti niyāmetabbaṃ, "
    "magge nava pañhā kātabbā.":
        "विषय बनाकर करने चाहिए। इस दो के वर्गीकरण में लोकोत्तर नहीं है, {duka_o} के समान, बिना किसी अंतर के। "
        "“{w} का विषय बनने वाली” ऐसा निश्चित करना चाहिए, मार्ग-कारण में नौ प्रश्न करने चाहिए।",
    "idha nahetupaccayo natthi": "यहाँ मूल-कारण का अभाव नहीं है",
    "evaṃ itarepi tīṇi pañhā kātabbā ārammaṇasadisaṃyeva. adhipatiyāpi anantarepi upanissayepi vibhāgo natthi.":
        "इसी तरह बाकी तीन प्रश्न भी विषय-कारण के समान ही करने चाहिए। प्रधानता-कारण में भी, निकटता-कारण में भी "
        "और प्रबल आश्रय-कारण में भी विभाजन नहीं है।",
    "arūpaṃyeva paccayaṃ, ekekassa tīṇi tīṇi kātabbā. ārammaṇañca sahajātañca upanissayañca navasupi "
    "parivattetabbaṃ. evaṃ pañhāvārepi sabbaṃ kātabbaṃ.":
        "केवल अभौतिक को कारण, हर एक के तीन-तीन करने चाहिए। विषय-कारण, सह-उत्पत्ति-कारण और प्रबल आश्रय-कारण को "
        "नौ में भी उलट-पलट करना चाहिए। इसी तरह प्रश्नों के खंड में भी सब करना चाहिए।",
    "avasesā pañhā sabbe vitthāretabbā. arūpaṃ paṭhamaṃ kātabbaṃ, rūpaṃ pacchā yathā labhati.":
        "शेष सभी प्रश्नों का विस्तार करना चाहिए। अभौतिक को पहले करना चाहिए, भौतिक रूप को बाद में, जैसा लागू होता है।",
    "ārammaṇasadisaṃ": "विषय-कारण के समान",
    "ārammaṇasadisaṃ, vipāko natthi": "विषय-कारण के समान, कर्म-फल नहीं है",
    "ārammaṇādhipatiyeva": "विषय रूपी प्रधानता ही",
    "ārammaṇādhipatiyeva kātabbā": "विषय रूपी प्रधानता ही करनी चाहिए",
    "purejātaṃ ārammaṇasadisaṃ kusalākusalassa vibhajitabbaṃ":
        "पूर्व-उत्पत्ति विषय-कारण के समान है, हितकर और हानिकर के लिए विश्लेषण करना चाहिए",
    "evaṃ avasesā cattāri pañhā kātabbā": "इसी तरह शेष चार प्रश्न करने चाहिए",
    "GGadukassa mātikā idha katā.": "{duka_o} की मूल सूची यहाँ बनाई गई है।",
    "evaṃ itarepi tīṇi kātabbā": "इसी तरह बाकी तीन भी करने चाहिए",
    "ārammaṇasadisā adhipatipaccayā, purejātampi ārammaṇasadisaṃ. upanissayepi lokuttaraṃ na kātabbaṃ. "
    "saṃkhittaṃ, evaṃ vitthāretabbaṃ yathā GGadukaṃ, evaṃ paccavekkhitvā kātabbaṃ.":
        "प्रधानता-कारण विषय-कारण के समान हैं, पूर्व-उत्पत्ति भी विषय-कारण के समान है। प्रबल आश्रय-कारण में भी "
        "लोकोत्तर को नहीं लेना चाहिए। संक्षिप्त, इसी तरह विस्तार करना चाहिए, जैसे {duka} है, वैसे ही जाँचकर करना चाहिए।",
    "cakkaṃ. sabbepi GGā kātabbā": "चक्र। सभी {pl} भी {karne_g} चाहिए",
    "cakkaṃ. sabbaṃ GGaṃ vitthāretabbaṃ": "चक्र। हर {sg} का विस्तार करना चाहिए",
    "evaṃ navapi tīsu padesu parivattetabbā": "इसी तरह नौ को भी तीनों पदों में उलट-पलट करना चाहिए",
    "evaṃ pañca pañhā kātabbā arūpeyeva, saṃsaṭṭhavāropi sampayuttavāropi evaṃ kātabbā":
        "इसी तरह अभौतिक लोक में ही पाँच प्रश्न करने चाहिए, घुले-मिले होने का खंड भी और जुड़ाव का खंड भी "
        "इसी तरह करने चाहिए",
    "evaṃ pañca pañhā kātabbā": "इसी तरह पाँच प्रश्न करने चाहिए",
    "pacchājātā kātabbā": "पश्चात्-उत्पत्ति करनी चाहिए",
    "sabbe vārā yathā GGadukaṃ evaṃ kātabbaṃ ninnānākaraṇaṃ.":
        "सभी खंड जैसे {duka_o} में हैं, वैसे ही बिना किसी अंतर के करने चाहिए।",
    "evaṃ itarepi tīṇi ārabbha kātabbāni. imaṃ dukaṃ GGadukasadisaṃ. lokuttaraṃ yahiṃ na labbhati tahiṃ na kātabbaṃ.":
        "इसी तरह बाकी तीन भी विषय बनाकर करने चाहिए। यह दो का वर्गीकरण {duka_o} के समान है। जहाँ लोकोत्तर लागू नहीं "
        "होता, वहाँ नहीं करना चाहिए।",
}
