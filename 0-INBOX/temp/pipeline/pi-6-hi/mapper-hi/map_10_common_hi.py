"""pi-6 Indriyayamaka (10-01 .. 10-13) Pāli->Hindi keyword map: the shared Indriya table.

Importing this module writes nothing and prints nothing. Use it on top of the sample's PI6:

    import sys, pathlib; sys.dont_write_bytecode = True
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    from map_sample_hi import *                 # PI6, make_resolver, build_part, verify, ...
    from map_10_common_hi import IND            # this table
    T = {...}                                   # your own chapter entries (they win over IND)
    build_part(f, make_resolver(f, {**PI6, **IND, **T}, OVR))

Keys are lower-case first letter (the resolver lower-cases the first letter); the quotative -ti and the enclitics
-ñca / -ñceva are stripped by pi6_value, so «cakkhundriyanti», «Cakkhundriyañca» find «cakkhundriyaṃ».
A tuple value = alternatives, the first one present in the segment's Hindi wins (else the first).

Sources: notes-10a.md (the builder's item table), the Hindi translation files 10-01 .. 10-06 (the truth),
hi-map-conventions-pi6.md (sample rules) and the pi-1/2/5 Hindi maps (prior values, grep).

- The 22 faculties: «X की क्षमता» (jīvitindriya «जीवन-क्षमता»), every case form, also inside the Khandha-style
  word-checking pairs; indriyaṃ / indriyā / indriye = क्षमता (dictionary form, singular, like khandhā = समूह).
- (Xindriyamūlakaṃ) headings = «X की क्षमता पर आधारित».
- Bare words of the word-checking pairs keep their bare Hindi (brief; notes-10a «approved choice 2»):
  cakkhu आँख, sotaṃ कान, … aññātāvī «पूर्ण ज्ञान पा चुका व्यक्ति».
- Verbs: क्षमता is FEMININE, so the text says «उत्पन्न होती है / हुई थी / होगी». The values stay the sample's
  masculine dictionary forms (uppajjati उत्पन्न होना, uppajjittha उत्पन्न हुआ था, uppajjissati उत्पन्न होगा):
  conventions «Feminine/plural text forms pass the presence check; do not change the value». Those entries live in
  PI6; VERBS below only adds the Indriya slips and the women's plural (parinibbāyissanti पूर्ण निर्वाण पाएँगे also
  covers «… पाएँगी»).
- Beings and places of the Pavatti/Uppāda sections (participle nouns masc. direct sg; place sense = the realm,
  direct case; beings sense = «… के प्राणी»; instrumental «के साथ» stripped as in kusalamūlena: somanassena =
  प्रसन्नता, upekkhāya = समभाव; the moment phrases «… मन के उत्पन्न / भंग होने का क्षण»).
- «(no direct equivalent)» as a keyword is an artefact: mapped to itself (see NDE_KW).
- Entries used only in 10-07 .. 10-13 (bhaṅgakkhaṇe, pacchimacittassa …, upapatticittassa bhaṅgakkhaṇe,
  cavantīnaṃ, kāmāvacarā …) follow the same pattern but were not checked against those files' Hindi.
"""
import sys

sys.dont_write_bytecode = True

IND = {}

# ---------------------------------------------------------------------------- artefact keyword (rule for all pi-6 maps)
# «(no direct equivalent)» in a Pāli keyword list is an artefact (an English keyword that had no Pāli), not a Pāli
# word: keep it in place and map it to itself, never to a Hindi word (not «व्यक्ति», even where the Hindi has
# «जो व्यक्ति»).
NDE_KW = "(no direct equivalent)"
IND[NDE_KW] = NDE_KW

# ---------------------------------------------------------------------------- the 22 faculties
# compound stem (Pāli, as in «<stem>indriyaṃ») -> (faculty Hindi, bare word Hindi)
FACULTIES = {
    "cakkhu": ("आँख की क्षमता", "आँख"),
    "sot": ("कान की क्षमता", "कान"),
    "ghān": ("नाक की क्षमता", "नाक"),
    "jivh": ("जीभ की क्षमता", "जीभ"),
    "kāy": ("शरीर की क्षमता", "शरीर"),
    "man": ("मन की क्षमता", "मन"),
    "itth": ("स्त्रीत्व की क्षमता", "स्त्री"),
    "puris": ("पुरुषत्व की क्षमता", "पुरुष"),
    "jīvit": ("जीवन-क्षमता", "जीवन"),
    "sukh": ("सुख की क्षमता", "सुख"),
    "dukkh": ("दुःख की क्षमता", "दुःख"),
    "somanass": ("प्रसन्नता की क्षमता", "प्रसन्नता"),
    "domanass": ("उदासी की क्षमता", "उदासी"),
    "upekkh": ("समभाव की क्षमता", "समभाव"),
    "saddh": ("श्रद्धा की क्षमता", "श्रद्धा"),
    "vīriy": ("उत्साह की क्षमता", "उत्साह"),
    "viriy": ("उत्साह की क्षमता", "उत्साह"),                     # variant spelling
    "sat": ("सजगता की क्षमता", "सजगता"),
    "samādh": ("एकाग्रता की क्षमता", "एकाग्रता"),
    "paññ": ("प्रज्ञा की क्षमता", "प्रज्ञा"),
    "anaññātaññassāmīt": ("“जो अब तक नहीं जाना उसे मैं जान लूँगा” की क्षमता",
                          "“जो अब तक नहीं जाना उसे मैं जान लूँगा”"),
    "aññ": ("पूर्ण ज्ञान की क्षमता", "पूर्ण ज्ञान"),
    "aññātāv": ("पूर्ण ज्ञान पा चुके की क्षमता", "पूर्ण ज्ञान पा चुका व्यक्ति"),
}
_CASES = ("ṃ", "", "ssa", "ā", "āni", "ena", "e", "esu", "ānaṃ")
for _st, (_fac, _bare) in FACULTIES.items():
    _join = "ndriya" if _st == "cakkhu" else "indriya"
    for _e in _CASES:
        IND[f"{_st}{_join}{_e}"] = _fac
    for _e in ("mūlakaṃ", "mūlaka", "mūlakā"):
        IND[f"{_st}{_join}{_e}"] = f"{_fac} पर आधारित"           # (Cakkhundriyamūlakaṃ) heading
IND["ghānandriyamūlakaṃ"] = "नाक की क्षमता पर आधारित"           # Pāli misprint (10-08)
IND["viriyindiyaṃ"] = "उत्साह की क्षमता"                         # variant in the [वर्तनी-भेद] bracket

IND.update({
    "indriyaṃ": "क्षमता", "indriya": "क्षमता", "indriyā": "क्षमता", "indriye": "क्षमता", "indriyāni": "क्षमता",
    "indriyānaṃ": "क्षमता", "indriyassa": "क्षमता",
    "bāvīsatindriyāni": "बाईस क्षमताएँ",                           # pi-2 ^2-219 (plural concept, like pañcakkhandhā)
})

# ---------------------------------------------------------------------------- bare words (word-checking pairs)
# every case form the keyword files use; -ti / -ñca / -ñceva are stripped by pi6_value, the odd ones are listed
BARE_IND = {
    "cakkhu": "आँख", "cakkhuṃ": "आँख",
    "sotaṃ": "कान", "sota": "कान",
    "ghānaṃ": "नाक", "ghāna": "नाक",
    "jivhā": "जीभ", "jivhaṃ": "जीभ",
    "kāyo": "शरीर", "kāyaṃ": "शरीर", "kāya": "शरीर",
    "mano": "मन", "manaṃ": "मन",
    "itthī": "स्त्री", "itthiṃ": "स्त्री", "itthi": "स्त्री",
    "puriso": "पुरुष", "purisaṃ": "पुरुष",
    "jīvitaṃ": "जीवन",
    "sukhaṃ": "सुख", "dukkhaṃ": "दुःख", "somanassaṃ": "प्रसन्नता", "domanassaṃ": "उदासी",
    "upekkhā": "समभाव", "upekkhaṃ": "समभाव",
    "saddhā": "श्रद्धा", "saddhaṃ": "श्रद्धा",
    "vīriyaṃ": "उत्साह",
    "sati": "सजगता", "satiṃ": "सजगता",
    "samādhi": "एकाग्रता", "samādhiṃ": "एकाग्रता",
    "paññā": "प्रज्ञा", "paññaṃ": "प्रज्ञा",
    "anaññātaññassāmīti": "“जो अब तक नहीं जाना उसे मैं जान लूँगा”",
    "anaññātaññassāmītiṃ": "“जो अब तक नहीं जाना उसे मैं जान लूँगा”",
    "anaññātaññāssāmīti": "“जो अब तक नहीं जाना उसे मैं जान लूँगा”",   # as written (10-01 ^6-10-3)
    "aññaṃ": "पूर्ण ज्ञान",
    "aññātāvī": "पूर्ण ज्ञान पा चुका व्यक्ति", "aññātāviṃ": "पूर्ण ज्ञान पा चुका व्यक्ति",
    "aññātāvi": "पूर्ण ज्ञान पा चुका व्यक्ति",                     # aññātāvīti after -īti stripping
    # the qualified answers (notes-10a): «दिव्य आँख और प्रज्ञा की आँख», «दिव्य कान और तृष्णा की धारा» (I2)
    "dibbacakkhu": "दिव्य आँख", "paññācakkhu": "प्रज्ञा की आँख",
    "dibbasotaṃ": "दिव्य कान", "taṇhāsotaṃ": "तृष्णा की धारा",
    "avaseso": "शेष", "avasesaṃ": "शेष", "avasesā": "शेष",
}
IND.update(BARE_IND)

# ---------------------------------------------------------------------------- verbs
VERBS = {
    "upapajjissati": "उत्पन्न होगा",            # Pāli slip «na upapajjissati» for na uppajjissati (10-06, notes-10a)
    "parinibbāyissanti": "पूर्ण निर्वाण पाएँगे",  # also «जो स्त्रियाँ … पूर्ण निर्वाण पाएँगी»
}
IND.update(VERBS)

# ---------------------------------------------------------------------------- beings and places (Pavatti)
# sa-X-ka = «X वाला», a-X-ka = «X से रहित» (I1-organs), participle-noun forms in -ānaṃ and the nom. pl. -ā
for _p, _h in (("cakkhuka", "आँख"), ("sotaka", "कान"), ("ghānaka", "नाक"), ("jivhaka", "जीभ"),
               ("kāyaka", "शरीर"), ("cittaka", "मन"), ("hetuka", "मूल")):
    for _e in ("ānaṃ", "ā", "o", "aṃ", "e", "āna"):
        _s = _p[:-1] + _e
        IND["sa" + _s] = f"{_h} वाला"
        IND["a" + _s] = f"{_h} से रहित"
IND.update({
    "ñāṇasampayuttānaṃ": "ज्ञान से जुड़ा", "ñāṇavippayuttānaṃ": "ज्ञान से अलग",
    "ñāṇasampayuttā": "ज्ञान से जुड़ा", "ñāṇavippayuttā": "ज्ञान से अलग",
    "somanassena": "प्रसन्नता", "upekkhāya": "समभाव",      # «प्रसन्नता के साथ / के बिना» (instrumental stripped)
    "itthīnaṃ": "स्त्री", "itthiyo": "स्त्री", "purisānaṃ": "पुरुष", "purisā": "पुरुष",
    "upapajjantānaṃ": "जन्म लेने वाला", "upapajjantīnaṃ": "जन्म लेने वाली स्त्री",
    "uppajjantīnaṃ": "जन्म लेने वाली स्त्री",           # Pāli slip for upapajjantīnaṃ (10-03, notes-10a)
    "cavantānaṃ": "मरने वाला", "cavantāna": "मरने वाला", "cavantīnaṃ": "मरने वाली स्त्री",
    "nirodhasamāpannānaṃ": "समाप्ति की ध्यान-अवस्था में लीन",
    "pavatte": "जीवन के दौरान",
    "cittassa": "मन", "citte": "मन", "vattamāne": "चलना", "anantarā": "ठीक बाद",
    "uppādakkhaṇe": "उत्पन्न होने का क्षण", "bhaṅgakkhaṇe": "भंग होने का क्षण",
    "upapatticittassa": "जन्म का मन",
    "pacchimacittasamaṅgīnaṃ": "अंतिम मन से युक्त", "pacchimacittasamaṅgīna": "अंतिम मन से युक्त",
    "somanassasampayuttapacchimacittaṃ": "प्रसन्नता से जुड़ा अंतिम मन",
    "upekkhāsampayuttapacchimacittaṃ": "समभाव से जुड़ा अंतिम मन",
    "itarāsaṃ": ("बाकी सब", "बाकी"),                      # feminine of itaresaṃ
    # realms: place sense = the realm (direct case), beings sense = «… के प्राणी»
    "kāmāvacare": "इंद्रिय-सुखों का लोक", "kāmāvacaraṃ": "इंद्रिय-सुखों का लोक", "kāmāvacarā": "इंद्रिय-सुखों का लोक",
    "kāmāvacarānaṃ": "इंद्रिय-सुखों के लोक के प्राणी",
    "rūpāvacare": "सूक्ष्म भौतिक लोक", "rūpāvacaraṃ": "सूक्ष्म भौतिक लोक", "rūpāvacarā": "सूक्ष्म भौतिक लोक",
    "rūpāvacarānaṃ": "सूक्ष्म भौतिक लोक के प्राणी",
    "arūpāvacare": "अभौतिक लोक", "arūpāvacaraṃ": "अभौतिक लोक", "arūpāvacarā": "अभौतिक लोक",
    "arūpāvacarānaṃ": "अभौतिक लोक के प्राणी",
    # «चार या पाँच समूहों वाले अस्तित्व» (I3): catuvokāra is discontinuous there
    "catuvokāre": ("चार समूहों वाला अस्तित्व", "चार … समूहों वाला अस्तित्व"),
    "catuvokāraṃ": ("चार समूहों वाला अस्तित्व", "चार … समूहों वाला अस्तित्व"),
    "catuvokārā": ("चार समूहों वाला अस्तित्व", "चार … समूहों वाला अस्तित्व"),
    "catuvokārānaṃ": ("चार समूहों वाले अस्तित्व के प्राणी", "चार … समूहों वाले अस्तित्व के प्राणी"),
})

# the moment phrases: [<q1>[<q2>]]cittassa uppādakkhaṇe / bhaṅgakkhaṇe = «[<q1> [और <q2>]] मन के … होने का क्षण»
_Q = {"somanassa": "प्रसन्नता", "upekkhā": "समभाव", "saddhā": "श्रद्धा", "ñāṇa": "ज्ञान"}
_R = {"sampayutta": "से जुड़े", "vippayutta": "से अलग"}
_MOMENT = {"uppādakkhaṇe": "उत्पन्न होने का क्षण", "bhaṅgakkhaṇe": "भंग होने का क्षण"}
_QUALS = {"": ""}
for _q1, _h1 in _Q.items():
    for _r1, _g1 in _R.items():
        _QUALS[_q1 + _r1] = f"{_h1} {_g1} "
        for _q2, _h2 in _Q.items():
            if _q2 != _q1:
                for _r2, _g2 in _R.items():
                    _QUALS[_q1 + _r1 + _q2 + _r2] = f"{_h1} {_g1} और {_h2} {_g2} "
for _qp, _qh in _QUALS.items():
    for _m, _mh in _MOMENT.items():
        IND[f"{_qp}cittassa {_m}"] = f"{_qh}मन के {_mh}"
        IND[f"{_qp}pacchimacittassa {_m}"] = f"{_qh}अंतिम मन के {_mh}"
        IND[f"upapatticittassa {_m}"] = f"जन्म के मन के {_mh}"
for _qp, _qh in list(_QUALS.items())[1:]:
    IND[f"{_qp}pacchimacittasamaṅgīnaṃ"] = f"{_qh}अंतिम मन से युक्त"
