r"""pi-6 Yamaka, Indriyayamaka 10-01..10-06: Hindi plain zero-shot builder with fixed frames.

usage: python -I -X utf8 build_10a_hi.py [10-01 10-02 ...]
Imports the approved sample constants (build_sample_hi, import only) and adds the
Indriyayamaka item table and frames (also listed in notes-10a.md).
Every sentence is translated by a rule or a fixed string; an unknown one raises an error.
"""
import pathlib
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi")
import build_sample_hi as S  # noqa: E402

PALI_DIR = S.PALI_DIR
HI_DIR = S.HI_DIR
ID_RE = S.ID_RE

# ---------------------------------------------------------------- item table
# (Pāli faculty name, Hindi, bare word, bare Hindi, bare oblique, bare stem for -ṃ/-ñca forms)
ITEMS = [
    ("cakkhundriyaṃ", "आँख की क्षमता", "cakkhu", "आँख", "आँख", "cakkhu"),
    ("sotindriyaṃ", "कान की क्षमता", "sotaṃ", "कान", "कान", "sota"),
    ("ghānindriyaṃ", "नाक की क्षमता", "ghānaṃ", "नाक", "नाक", "ghāna"),
    ("jivhindriyaṃ", "जीभ की क्षमता", "jivhā", "जीभ", "जीभ", "jivha"),
    ("kāyindriyaṃ", "शरीर की क्षमता", "kāyo", "शरीर", "शरीर", "kāya"),
    ("manindriyaṃ", "मन की क्षमता", "mano", "मन", "मन", "mana"),
    ("itthindriyaṃ", "स्त्रीत्व की क्षमता", "itthī", "स्त्री", "स्त्री", "itthi"),
    ("purisindriyaṃ", "पुरुषत्व की क्षमता", "puriso", "पुरुष", "पुरुष", "purisa"),
    ("jīvitindriyaṃ", "जीवन-क्षमता", "jīvitaṃ", "जीवन", "जीवन", "jīvita"),
    ("sukhindriyaṃ", "सुख की क्षमता", "sukhaṃ", "सुख", "सुख", "sukha"),
    ("dukkhindriyaṃ", "दुःख की क्षमता", "dukkhaṃ", "दुःख", "दुःख", "dukkha"),
    ("somanassindriyaṃ", "प्रसन्नता की क्षमता", "somanassaṃ", "प्रसन्नता", "प्रसन्नता", "somanassa"),
    ("domanassindriyaṃ", "उदासी की क्षमता", "domanassaṃ", "उदासी", "उदासी", "domanassa"),
    ("upekkhindriyaṃ", "समभाव की क्षमता", "upekkhā", "समभाव", "समभाव", "upekkha"),
    ("saddhindriyaṃ", "श्रद्धा की क्षमता", "saddhā", "श्रद्धा", "श्रद्धा", "saddha"),
    ("vīriyindriyaṃ", "उत्साह की क्षमता", "vīriyaṃ", "उत्साह", "उत्साह", "vīriya"),
    ("satindriyaṃ", "सजगता की क्षमता", "sati", "सजगता", "सजगता", "sati"),
    ("samādhindriyaṃ", "एकाग्रता की क्षमता", "samādhi", "एकाग्रता", "एकाग्रता", "samādhi"),
    ("paññindriyaṃ", "प्रज्ञा की क्षमता", "paññā", "प्रज्ञा", "प्रज्ञा", "pañña"),
    ("anaññātaññassāmītindriyaṃ", "“जो अब तक नहीं जाना उसे मैं जान लूँगा” की क्षमता",
     "anaññātaññassāmīti", "“जो अब तक नहीं जाना उसे मैं जान लूँगा”", "“जो अब तक नहीं जाना उसे मैं जान लूँगा”",
     "anaññātaññassāmīti"),
    ("aññindriyaṃ", "पूर्ण ज्ञान की क्षमता", "aññaṃ", "पूर्ण ज्ञान", "पूर्ण ज्ञान", "añña"),
    ("aññātāvindriyaṃ", "पूर्ण ज्ञान पा चुके की क्षमता", "aññātāvī", "पूर्ण ज्ञान पा चुका व्यक्ति", "पूर्ण ज्ञान पा चुके व्यक्ति", "aññātāvi"),
]
INDRIYA = {p: h for p, h, *_ in ITEMS}            # faculty name -> Hindi (feminine)
BARE = {b: bh for _, _, b, bh, _, _ in ITEMS}       # bare word -> Hindi
BARE_OBL = {b: bo for _, _, b, _, bo, _ in ITEMS}
BARE["cakkhuṃ"] = "आँख"                              # (Kha) cakkhundriyaṃ cakkhuṃ? (form as written)
BARE["anaññātaññāssāmīti"] = BARE["anaññātaññassāmīti"]   # 10-01 ^6-10-3, long ā as written
INDRIYAM = "क्षमता"          # indriyaṃ (sg.)
INDRIYA_PL = "क्षमताएँ"      # indriyā (pl.)
INDRIYA_OBL_PL = "क्षमताओं"  # indriye (acc. pl.) before ṭhapetvā

# subjects of the paṇṇatti questions: Pāli -> (Hindi, plural?)
SUBJ = {}
for _p, _h in INDRIYA.items():
    SUBJ[_p] = (_h, False)
for _b, _h in BARE.items():
    SUBJ[_b] = (_h, False)
SUBJ["indriyaṃ"] = (INDRIYAM, False)
SUBJ["indriyā"] = (INDRIYA_PL, True)


def cap(s):
    return s[0].upper() + s[1:]


def ca_form(ind):           # cakkhundriyaṃ -> cakkhundriyañca
    return ind[:-1] + "ñca"


# ---------------------------------------------------------------- headings and fixed lines
HEADINGS = dict(S.HEADINGS)
HEADINGS.update({
    "Suddhindriyavāro": "केवल क्षमताओं का खंड",
    "Suddhindriyamūlacakkavāro": "केवल क्षमताओं पर आधारित चक्र का खंड",
    "Pavattivāro": "प्रक्रिया का खंड",
    "Uppādavāro": "उत्पन्न होने का खंड",
})
MULAKA = "{X} पर आधारित"     # (Cakkhundriyamūlakaṃ)

VAR = S._var
FIXED_LINES = {
    "Bāvīsatindriyāni – cakkhundriyaṃ, sotindriyaṃ, ghānindriyaṃ, jivhindriyaṃ, kāyindriyaṃ, manindriyaṃ, itthindriyaṃ, purisindriyaṃ, jīvitindriyaṃ, sukhindriyaṃ, dukkhindriyaṃ, somanassindriyaṃ, domanassindriyaṃ, upekkhindriyaṃ, saddhindriyaṃ, vīriyindriyaṃ [viriyindiyaṃ (sī. syā.)], satindriyaṃ, samādhindriyaṃ, paññindriyaṃ, anaññātaññassāmītindriyaṃ, aññindriyaṃ, aññātāvindriyaṃ.":
        "बाईस क्षमताएँ – आँख की क्षमता, कान की क्षमता, नाक की क्षमता, जीभ की क्षमता, शरीर की क्षमता, मन की क्षमता, "
        "स्त्रीत्व की क्षमता, पुरुषत्व की क्षमता, जीवन-क्षमता, सुख की क्षमता, दुःख की क्षमता, प्रसन्नता की क्षमता, "
        "उदासी की क्षमता, समभाव की क्षमता, श्रद्धा की क्षमता, उत्साह की क्षमता " + VAR(S.VAR_SPELL, "Sī., Syā.", "viriyindiyaṃ")
        + ", सजगता की क्षमता, एकाग्रता की क्षमता, प्रज्ञा की क्षमता, “जो अब तक नहीं जाना उसे मैं जान लूँगा” की क्षमता, "
        "पूर्ण ज्ञान की क्षमता, पूर्ण ज्ञान पा चुके की क्षमता।",
}

# ---------------------------------------------------------------- answer sentences (fixed, per item)
DIBBA_CAKKHU = "दिव्य आँख और प्रज्ञा की आँख"       # Dibbacakkhu paññācakkhu
DIBBA_SOTA = "दिव्य कान और तृष्णा की धारा"          # Dibbasotaṃ taṇhāsotaṃ
QA_ANU_1_PL = "{A}, {B} हैं, पर {C} नहीं हैं।"      # A B, na C. (plural A)
QA_PACC_1 = S.QA_PACC_1                              # "{A}, {C} नहीं {V}, पर {B} {V}।"
QA_ANU_2 = S.QA_ANU_2                                # "{C}, {B} भी है और {C} भी।"
QA_PACC_2 = S.QA_PACC_2                              # "{B} और {C} को छोड़कर शेष न तो {Bn} हैं, न {Cn}।"
QA_PACC_2_SG = "{B} और {C} को छोड़कर शेष न तो {Bn} है, न {Cn}।"   # … avaseso (sg.)
EXCEPT = S.EXCEPT                                    # "{C} को छोड़कर"
AVASESA = S.AVASESA                                  # शेष

SENT = {
    "Āmantā.": S.AMANTA,
    "No.": "नहीं।",
    "Natthi.": "ऐसा कोई नहीं है।",
    "Paṇṇattiuddesavāro.": S.FIXED["Paṇṇattiuddesavāro."],
    "Paṇṇattiniddesavāro.": S.FIXED["Paṇṇattiniddesavāro."],
    # padasodhana, qualified answers
    "Dibbacakkhu paññācakkhu cakkhu, na cakkhundriyaṃ.":
        QA_ANU_1_PL.format(A=DIBBA_CAKKHU, B="आँख", C=INDRIYA["cakkhundriyaṃ"]),
    "Dibbasotaṃ taṇhāsotaṃ sotaṃ, na sotindriyaṃ.":
        QA_ANU_1_PL.format(A=DIBBA_SOTA, B="कान", C=INDRIYA["sotindriyaṃ"]),
    "Dibbacakkhu paññācakkhu na cakkhundriyaṃ, cakkhu.":
        QA_PACC_1.format(A=DIBBA_CAKKHU, C=INDRIYA["cakkhundriyaṃ"], B="आँख", V="हैं"),
    "Dibbasotaṃ taṇhāsotaṃ na sotindriyaṃ, sotaṃ.":
        QA_PACC_1.format(A=DIBBA_SOTA, C=INDRIYA["sotindriyaṃ"], B="कान", V="हैं"),
    "Kāyindriyaṃ ṭhapetvā avaseso kāyo [avasesā kāyo (sī. syā. ka.)], na kāyindriyaṃ.":
        EXCEPT.format(C=INDRIYA["kāyindriyaṃ"]) + " " + AVASESA + " शरीर "
        + VAR(S.VAR_SPELL, "Sī., Syā., Ka.", "avasesā kāyo") + ", " + INDRIYA["kāyindriyaṃ"] + " नहीं है।",
    "Kāyindriyaṃ ṭhapetvā avaseso kāyo, na kāyindriyaṃ.":
        EXCEPT.format(C=INDRIYA["kāyindriyaṃ"]) + " " + AVASESA + " शरीर, " + INDRIYA["kāyindriyaṃ"] + " नहीं है।",
    "Kāyindriyaṃ ṭhapetvā avaseso kāyo na kāyindriyaṃ.":
        EXCEPT.format(C=INDRIYA["kāyindriyaṃ"]) + " " + AVASESA + " शरीर, " + INDRIYA["kāyindriyaṃ"] + " नहीं है।",
    "Upekkhindriyaṃ ṭhapetvā avasesā upekkhā, na upekkhindriyaṃ.":
        EXCEPT.format(C=INDRIYA["upekkhindriyaṃ"]) + " " + AVASESA + " समभाव, " + INDRIYA["upekkhindriyaṃ"] + " नहीं है।",
    "Kāyindriyaṃ ṭhapetvā avaseso na kāyindriyaṃ, kāyo.":
        QA_PACC_1.format(A=EXCEPT.format(C=INDRIYA["kāyindriyaṃ"]) + " " + AVASESA,
                         C=INDRIYA["kāyindriyaṃ"], B="शरीर", V="है"),
    "Upekkhindriyaṃ ṭhapetvā avasesā na upekkhindriyaṃ, upekkhā.":
        QA_PACC_1.format(A=EXCEPT.format(C=INDRIYA["upekkhindriyaṃ"]) + " " + AVASESA,
                         C=INDRIYA["upekkhindriyaṃ"], B="समभाव", V="है"),
    "Kāyañca kāyindriyañca ṭhapetvā avaseso na ceva kāyo na ca kāyindriyaṃ.":
        QA_PACC_2_SG.format(B="शरीर", C=INDRIYA["kāyindriyaṃ"], Bn="शरीर", Cn=INDRIYA["kāyindriyaṃ"]),
    # suddhindriya
    "Yaṃ sotaṃ indriyaṃ taṃ sotañceva indriyañca.": "जो कान क्षमता है, वह कान भी है और क्षमता भी।",
    "Avasesaṃ sotaṃ na indriyaṃ.": "शेष कान, क्षमता नहीं है।",
    "Yo kāyo indriyaṃ so kāyo ceva indriyañca.": "जो शरीर क्षमता है, वह शरीर भी है और क्षमता भी।",
    "Avaseso kāyo na indriyaṃ.": "शेष शरीर, क्षमता नहीं है।",
    "Avaseso kāyo na indriyā.": "शेष शरीर, क्षमता नहीं है।",     # na indriyā (pl.) as written
    "Yā upekkhā indriyaṃ sā upekkhā ceva indriyañca.": "जो समभाव क्षमता है, वह समभाव भी है और क्षमता भी।",
    "Avasesā upekkhā na indriyaṃ.": "शेष समभाव, क्षमता नहीं है।",
    # 10-06 ^…: the "both" sentence is cut in two by a full stop in the source
    "Itaresaṃ kāmāvacarānaṃ tesaṃ tattha itthindriyañca uppajjissati.":
        "इंद्रिय-सुखों के लोक के बाकी प्राणियों में वहाँ स्त्रीत्व की क्षमता भी उत्पन्न होगी।",
    "Somanassindriyañca uppajjissati.": "प्रसन्नता की क्षमता भी उत्पन्न होगी।",
}
for _p, _h, _b, _bh, _bo, _st in ITEMS:
    _I = cap(_p)
    # C B ceva C ca: "Cakkhundriyaṃ cakkhu ceva cakkhundriyañca." / "Sotindriyaṃ sotañceva sotindriyañca."
    SENT[f"{_I} {_b} ceva {ca_form(_p)}."] = QA_ANU_2.format(C=_h, B=_bh)
    SENT[f"{_I} {_st}ñceva {ca_form(_p)}."] = QA_ANU_2.format(C=_h, B=_bh)
    # Bañca Cañca ṭhapetvā avasesā na ceva B na ca C.
    SENT[f"{cap(_st)}ñca {ca_form(_p)} ṭhapetvā avasesā na ceva {_b} na ca {_p}."] = \
        QA_PACC_2.format(B=_bo, C=_h, Bn=_bh, Cn=_h)
    # Itthindriyaṃ na itthī, itthindriyaṃ. / Itthī na itthindriyaṃ, itthī.
    SENT[f"{_I} na {_b}, {_p}."] = QA_PACC_1.format(A=_h, C=_bh, B=_h, V="है")
    SENT[f"{cap(_b)} na {_p}, {_b}."] = QA_PACC_1.format(A=_bh, C=_h, B=_bh, V="है")
    # Yindriyaṃ indriyañceva Yindriyañca. Avasesā indriyā na Yindriyaṃ.
    SENT[f"{_I} indriyañceva {ca_form(_p)}."] = QA_ANU_2.format(C=_h, B=INDRIYAM)
    SENT[f"Avasesā indriyā na {_p}."] = f"{AVASESA} {INDRIYA_PL}, {_h} नहीं हैं।"
    SENT[f"Avasesā indriyā na {_p}"] = f"{AVASESA} {INDRIYA_PL}, {_h} नहीं हैं"   # before …pe….
    # Xṃ ṭhapetvā avasesā indriyā na X, indriyā. Xñca indriye ca ṭhapetvā avasesā na ceva X na ca indriyā.
    SENT[f"{cap(_st)}ṃ ṭhapetvā avasesā indriyā na {_b}, indriyā."] = \
        QA_PACC_1.format(A=EXCEPT.format(C=_bo) + " " + AVASESA + " " + INDRIYA_PL, C=_bh, B=INDRIYA_PL, V="हैं")
    SENT[f"{cap(_st)}ñca indriye ca ṭhapetvā avasesā na ceva {_b} na ca indriyā."] = \
        QA_PACC_2.format(B=_bo, C=INDRIYA_OBL_PL, Bn=_bh, Cn=INDRIYA_PL)

# ---------------------------------------------------------------- verbs (feminine: क्षमता)
VERBS = S.VERBS_F
SHORT = {}
for _v, (_pos, _neg) in VERBS.items():
    SHORT[cap(_v) + "."] = _pos + "।"
    SHORT[("N" + _v if _v.startswith("u") else "Na " + _v) + "."] = _neg + "।"
SENT.update(SHORT)

KNOWN = set(SUBJ) | set(VERBS) | {"n" + v for v in VERBS}


def untie(word):
    """Remove the quotative -ti: indriyanti -> indriyaṃ, cakkhūti -> cakkhu, uppajjitthāti -> uppajjittha."""
    if word in KNOWN:
        return word
    for cand in (word[:-2], word[:-3] + "ṃ", word[:-3] + "u", word[:-3] + "i", word[:-3] + "a", word[:-3] + "ā"):
        if cand in KNOWN:
            return cand
    return word


# ---------------------------------------------------------------- questions
PANNATTI_Q_ANU = "क्या {X}, {Y} {V}?"
PANNATTI_Q_PACC = "जो {X} नहीं {V}, क्या {P} {Y} नहीं {V}?"


def tr_pannatti_q(q):
    m = re.fullmatch(r"(na )?(\S+) (na )?(\S+)\?", q)
    if not m:
        return None
    n1, x, n2, y = m.groups()
    x = x[0].lower() + x[1:]
    y = untie(y)
    if bool(n1) != bool(n2) or x not in SUBJ or y not in SUBJ:
        return None
    xh, pl = SUBJ[x]
    yh = SUBJ[y][0]
    v = "हैं" if pl else "है"
    if n1:
        return PANNATTI_Q_PACC.format(X=xh, Y=yh, V=v, P="वे" if pl else "वह")
    return PANNATTI_Q_ANU.format(X=xh, Y=yh, V=v)


def _vfix(tok):
    return tok.replace("upapajjissati", "uppajjissati")   # 10-06 "na upapajjissati", as written


def verb(tok):
    return S.verb(_vfix(tok), VERBS)[0]


def verb_flip(tok):
    return S.verb_flip(_vfix(tok), VERBS)


def ind_list(s):
    """'saddhindriyaṃ…pe… paññindriyaṃ' -> 'श्रद्धा की क्षमता… प्रज्ञा की क्षमता'."""
    parts = re.split(r"(\s*…(?:pe…)?\s*)", s)
    return "".join(p.replace("…pe…", "…") if i % 2 else INDRIYA[p] for i, p in enumerate(parts))


def tr_pavatti_q(q):
    m = re.fullmatch(r"([Yy]assa|[Yy]attha)( vā pana)?( yattha)? (.+?) ((?:na )?\S+) (tassa tattha|tassa|tattha) (.+?) ((?:na )?\S+)\?", q)
    if not m:
        return None
    rel, vp, rel2, x, v1, cor, y, v2 = m.groups()
    rel = rel.lower() + (rel2 or "")
    v2 = v2[:3] + untie(v2[3:]) if v2.startswith("na ") else untie(v2)
    return S.PAVATTI_Q.format(AND=S.VA_PANA if vp else "", REL=S.Q_REL[rel], X=ind_list(x), V1=verb(v1),
                              COR=S.Q_COR[cor], Y=ind_list(y), V2=verb(v2))


def tr_question(q):
    for f in (tr_pannatti_q, tr_pavatti_q):
        try:
            r = f(q)
        except KeyError:
            r = None
        if r:
            return r
    return None


# ---------------------------------------------------------------- beings and places (WHO)
# plain realm / being nouns (merged "A और B में" when a WHO consists only of these)
PLAIN = {
    "kāmāvacare": "इंद्रिय-सुखों के लोक", "rūpāvacare": "सूक्ष्म भौतिक लोक", "arūpāvacare": "अभौतिक लोक",
    "arūpe": "अभौतिक लोक", "asaññasatte": "पहचान-रहित प्राणियों के लोक", "pañcavokāre": "पाँच समूहों वाले अस्तित्व",
    "catuvokāre": "चार समूहों वाले अस्तित्व",
    "kāmāvacarānaṃ": "इंद्रिय-सुखों के लोक के प्राणियों", "rūpāvacarānaṃ": "सूक्ष्म भौतिक लोक के प्राणियों",
    "arūpāvacarānaṃ": "अभौतिक लोक के प्राणियों", "arūpānaṃ": "अभौतिक लोक के प्राणियों",
    "asaññasattānaṃ": "पहचान-रहित प्राणियों", "pañcavokārānaṃ": "पाँच समूहों वाले अस्तित्व के प्राणियों",
    "catuvokārānaṃ": "चार समूहों वाले अस्तित्व के प्राणियों", "suddhāvāsānaṃ": "शुद्ध निवास लोक के प्राणियों",
    "pacchimabhavikānaṃ": "अंतिम जन्म वालों", "pacchimacittasamaṅgīnaṃ": "अंतिम मन से युक्त लोगों",
    "pacchimacittasamaṅgīna": "अंतिम मन से युक्त लोगों",       # 10-06, as written
    "nirodhasamāpannānaṃ": "समाप्ति की ध्यान-अवस्था में लीन लोगों",
}
# realm of the "Itaresaṃ X" phrases
ITARA_REALM = {"kāmāvacarānaṃ": "इंद्रिय-सुखों के लोक", "pañcavokārānaṃ": "पाँच समूहों वाले अस्तित्व",
               "catuvokārānaṃ": "चार समूहों वाले अस्तित्व", "rūpāvacarānaṃ": "सूक्ष्म भौतिक लोक",
               "arūpāvacarānaṃ": "अभौतिक लोक"}
ITARESAM = "बाकी सबमें"
ITARA = "बाकी {R} के प्राणियों में"        # Itaresaṃ + realm group = बाकी + group (as builders 1-9)
# birth modifiers (genitive plural adjectives / instrumentals before upapajjantānaṃ)
MODS = {
    "sacakkhukānaṃ": "आँख वाले", "acakkhukānaṃ": "आँख से रहित",
    "sasotakānaṃ": "कान वाले", "asotakānaṃ": "कान से रहित",
    "saghānakānaṃ": "नाक वाले", "aghānakānaṃ": "नाक से रहित",
    "sacittakānaṃ": "मन वाले", "acittakānaṃ": "मन से रहित",
    "sahetukānaṃ": "मूल वाले", "ahetukānaṃ": "मूल से रहित",
    "ñāṇasampayuttānaṃ": "ज्ञान से जुड़े", "ñāṇavippayuttānaṃ": "ज्ञान से अलग",
    "somanassena": "प्रसन्नता के साथ", "upekkhāya": "समभाव के साथ",
    "vinā somanassena": "प्रसन्नता के बिना", "vinā upekkhāya": "समभाव के बिना",
}
BIRTH_PLACE = {"asaññasattaṃ": "पहचान-रहित प्राणियों के लोक में", "pañcavokāraṃ": "पाँच समूहों वाले अस्तित्व में",
               "arūpaṃ": "अभौतिक लोक में"}
BORN = "जन्म लेने वालों में"
BORN_F = "जन्म लेने वाली स्त्रियों में"
BORN_M = "जन्म लेने वाले पुरुषों में"
NOT_F = "स्त्री न होकर"
NOT_M = "पुरुष न होकर"
# components of "<C>cittassa"
CITTA_PART = {"somanassa": "प्रसन्नता", "upekkhā": "समभाव", "saddhā": "श्रद्धा", "ñāṇa": "ज्ञान"}
ASSOC = {"sampayutta": "से जुड़े", "vippayutta": "से अलग"}
PAVATTE = "जीवन के दौरान"
CITTA_UPPADA = "मन के उत्पन्न होने के क्षण में"
CITTA_BHANGA = "मन के भंग होने के क्षण में"
SABBESAM_CAVANTANAM = "सभी मरने वालों में"
SABBESAM = "सबमें"
UPAPATTI_UPPADA = "जन्म के मन के उत्पन्न होने के क्षण में"   # upapatticittassa uppādakkhaṇe (terms file)
SUDDHAVASA_DUTIYE ="दूसरे मन के चलते समय शुद्ध निवास लोक के प्राणियों में"
# relative clauses (future, the anāgatavāra)
REL_SUBJ = {"ye": ("जो", False), "ye purisā": ("जो पुरुष", False), "yā itthiyo": ("जो स्त्रियाँ", True),
            "ye sacakkhukā": ("जो आँख वाले", False), "ye saghānakā": ("जो नाक वाले", False)}
ETENEVA = "इसी रूप में कुछ और जन्म बिताकर"          # eteneva bhāvena katici bhave dassetvā
UPAPAJJITVA = "जन्म लेकर"
PARINIBBAYISSANTI = {False: "पूर्ण निर्वाण पाएँगे", True: "पूर्ण निर्वाण पाएँगी"}
REL_PLACE = {"arūpaṃ": "अभौतिक लोक", "rūpāvacaraṃ": "सूक्ष्म भौतिक लोक",
             "rūpāvacaraṃ arūpāvacaraṃ": "सूक्ष्म भौतिक लोक या अभौतिक लोक"}
REL_MANNER = {"somanassena": "प्रसन्नता के साथ", "upekkhāya": "समभाव के साथ"}
TESAM = ", उनमें"                                     # correlative closing a relative chunk
ANANTARA = "जिनमें ऐसा मन है जिसके ठीक बाद {C} अंतिम मन उत्पन्न होगा"   # Yassa cittassa anantarā Cpacchimacittaṃ uppajjissati


def citta_compound(c):
    """'saddhāvippayuttasomanassasampayutta' -> 'श्रद्धा से अलग और प्रसन्नता से जुड़े'; '' -> ''."""
    if not c:
        return ""
    if c == "upapatti":
        return "जन्म के"
    parts = re.findall(r"(somanassa|upekkhā|saddhā|ñāṇa)(sampayutta|vippayutta)", c)
    if "".join(a + b for a, b in parts) != c:
        raise KeyError(c)
    return " और ".join(f"{CITTA_PART[a]} {ASSOC[b]}" for a, b in parts)


def _and(items):
    if len(items) == 1:
        return items[0]
    return ", ".join(items[:-1]) + " और " + items[-1]


# locative places (Pañcavokāre …): a place group QUALIFIES the group that follows it
PLACE_LOC = {PLAIN[k] for k in ("kāmāvacare", "rūpāvacare", "arūpāvacare", "arūpe", "asaññasatte",
                                "pañcavokāre", "catuvokāre")}
COMPACT = [("चार समूहों वाले अस्तित्व के प्राणियों और पाँच समूहों वाले अस्तित्व के प्राणियों",
            "चार समूहों वाले और पाँच समूहों वाले अस्तित्व के प्राणियों"),
           ("चार समूहों वाले अस्तित्व और पाँच समूहों वाले अस्तित्व",
            "चार समूहों वाले और पाँच समूहों वाले अस्तित्व")]


def _strip_me(c):
    return c[:-len(" में")] if c.endswith(" में") else c


def _is_relative(c):
    return c.startswith(("जो ", "जिनमें ", "जिस "))


def join(chunks):
    """Join WHO chunks (with or without the final में).
    - Itaresaṃ + group = बाकी + group (Itaresaṃ alone = बाकी सबमें);
    - place locative(s) + group = "<places> में <group>" (the place qualifies the group);
    - everything else (ca, listed groups) = "A और B" / "A, B और C"."""
    chunks = list(chunks)
    out, i = [], 0
    while i < len(chunks):
        c = chunks[i]
        if c == ITARESAM and i + 1 < len(chunks):
            chunks[i + 1] = "बाकी " + chunks[i + 1]
            i += 1
            continue
        if _strip_me(c) in PLACE_LOC:
            j, group = i, []
            while j < len(chunks) and _strip_me(chunks[j]) in PLACE_LOC:
                group.append(_strip_me(chunks[j]))
                j += 1
            if j < len(chunks) and not _is_relative(chunks[j]) and chunks[j] != ITARESAM:
                out.append(_and(group) + " में " + chunks[j])
                i = j + 1
                continue
        out.append(c)
        i += 1
    res = _and(out)
    for a, b in COMPACT:
        res = res.replace(a, b)
    return res


def tr_relative(clause):
    """'ye ca purisā eteneva … parinibbāyissanti' (lower-cased start, without 'ca')."""
    m = re.fullmatch(r"(ye purisā|yā itthiyo|ye sacakkhukā|ye saghānakā|ye)"
                     r"( eteneva bhāvena katici bhave dassetvā)?"
                     r"(?:( somanassena| upekkhāya)?( arūpaṃ| rūpāvacaraṃ arūpāvacaraṃ| rūpāvacaraṃ)? upapajjitvā)?"
                     r" parinibbāyissanti", clause)
    if not m:
        raise KeyError(clause)
    subj, ete, manner, where = m.groups()
    sh, fem = REL_SUBJ[subj]
    out = [sh]
    if ete:
        out.append(ETENEVA)
    if manner or where:
        out.append(" ".join(([REL_MANNER[manner.strip()]] if manner else [])
                            + ([REL_PLACE[where.strip()] + " में"] if where else [])) + " " + UPAPAJJITVA)
    out.append(PARINIBBAYISSANTI[fem])
    return " ".join(out) + TESAM


def tr_who(who):
    """Translate a being/place phrase into Hindi chunks; returns (hindi, ends_with_relative)."""
    w = who[0].lower() + who[1:]
    chunks, plain = [], True
    rest = w
    while rest:
        rest = rest.strip()
        if rest.startswith("ca "):
            rest = rest[3:]
        # relative clauses
        m = re.match(r"((?:ye|yā) .*?parinibbāyissanti)(?: |$)", rest)
        if m:
            cl = m.group(1).replace("ye ca ", "ye ").replace("yā ca ", "yā ")
            chunks.append(tr_relative(cl))
            plain = False
            rest = rest[m.end():]
            continue
        m = re.match(r"yassa cittassa anantarā (\S+?)pacchimacittaṃ uppajjissati(?: |$)", rest)
        if m:
            chunks.append(ANANTARA.format(C=citta_compound(m.group(1)).replace("जुड़े", "जुड़ा")) + TESAM)
            plain = False
            rest = rest[m.end():]
            continue
        m = re.match(r"sabbesaṃ cavantānaṃ(?: |$)", rest)
        if m:
            chunks.append(SABBESAM_CAVANTANAM); plain = False; rest = rest[m.end():]; continue
        m = re.match(r"sabbesaṃ cittassa bhaṅgakkhaṇe(?: |$)", rest)
        if m:
            chunks.append(SABBESAM + " " + CITTA_BHANGA); plain = False; rest = rest[m.end():]; continue
        m = re.match(r"(pavatte )?(\S*?)cittassa (uppādakkhaṇe|bhaṅgakkhaṇe)(?: |$)", rest)
        if m:
            pav, comp, k = m.groups()
            c = citta_compound(comp)
            s = (PAVATTE + " " if pav else "") + (c + " " if c else "") + (CITTA_UPPADA if k == "uppādakkhaṇe" else CITTA_BHANGA)
            chunks.append(s); plain = False; rest = rest[m.end():]; continue
        m = re.match(r"suddhāvāsānaṃ upapatticittassa uppādakkhaṇe(?: |$)", rest)
        if m:
            chunks.append(PLAIN["suddhāvāsānaṃ"] + " में " + UPAPATTI_UPPADA); plain = False; rest = rest[m.end():]; continue
        m = re.match(r"suddhāvāsānaṃ dutiye citte vattamāne(?: |$)", rest)
        if m:
            chunks.append(SUDDHAVASA_DUTIYE); plain = False; rest = rest[m.end():]; continue
        m = re.match(r"itaresaṃ((?: (?:kāmāvacarānaṃ|pañcavokārānaṃ|catuvokārānaṃ|rūpāvacarānaṃ|arūpāvacarānaṃ))*)(?: |$)", rest)
        if m:
            realms = m.group(1).split()
            if realms:
                chunks.append(ITARA.format(R=" और ".join(ITARA_REALM[r] for r in realms)))
            else:
                chunks.append(ITARESAM)
            plain = False; rest = rest[m.end():]; continue
        m = re.match(r"(asaññasattaṃ|pañcavokāraṃ|arūpaṃ) upapajjantānaṃ(?: |$)", rest)
        if m:
            chunks.append(BIRTH_PLACE[m.group(1)] + " " + BORN); plain = False; rest = rest[m.end():]; continue
        # birth chunk: modifiers … upapajjantānaṃ / upapajjantīnaṃ
        # (uppajjantīnaṃ: 10-03 ^…, as written for upapajjantīnaṃ)
        m = re.match(r"((?:(?:vinā )?\S+ )*?)(upapajjantānaṃ|upapajjantīnaṃ|uppajjantīnaṃ)(?: |$)", rest)
        if m and all((t in MODS or t in ("itthīnaṃ", "purisānaṃ", "na", "vinā"))
                     for t in m.group(1).split()):
            toks = m.group(1).split()
            mods, gender = [], None
            i = 0
            while i < len(toks):
                t = toks[i]
                if t == "vinā":
                    mods.append(MODS["vinā " + toks[i + 1]]); i += 2; continue
                if t == "na":
                    gender = "not_" + toks[i + 1]; i += 2; continue
                if t in ("itthīnaṃ", "purisānaṃ"):
                    gender = t; i += 1; continue
                mods.append(MODS[t]); i += 1
            mod = " और ".join(mods)
            if gender == "itthīnaṃ":
                s = (mod + " " if mod else "") + BORN_F
            elif gender == "purisānaṃ":
                s = (mod + " " if mod else "") + BORN_M
            elif gender in ("not_itthīnaṃ", "not_purisānaṃ"):
                s = (mod + ", " if mod else "") + (NOT_F if gender == "not_itthīnaṃ" else NOT_M) + " " + BORN
            else:
                s = (mod + " " if mod else "") + BORN
            chunks.append(s); plain = False; rest = rest[m.end():]; continue
        m = re.match(r"(\S+)(?: |$)", rest)
        if m and m.group(1) in PLAIN:
            chunks.append(PLAIN[m.group(1)] + " में"); rest = rest[m.end():]; continue
        raise KeyError("WHO: " + who + " | at: " + rest)
    if plain and len(chunks) > 1:
        bare = [c[:-len(" में")] for c in chunks]
        return join(bare) + " में", False
    return join(chunks), chunks[-1].endswith(TESAM)


LOC_ALT = "tesaṃ tattha|tāsaṃ tattha|tesaṃ|tāsaṃ|tattha"
LOC1 = {"tesaṃ": "", "tāsaṃ": "", "tattha": "", "tesaṃ tattha": " वहाँ", "tāsaṃ tattha": " वहाँ"}
LOC2 = {"tesaṃ": "उनमें", "tāsaṃ": "उनमें", "tattha": "वहाँ", "tesaṃ tattha": "उनमें वहाँ", "tāsaṃ tattha": "उनमें वहाँ"}
ANS_BUT = S.ANS_BUT     # "{WHO}{L1} {X} {V1}, पर {L2} {Y} {V2}।"
ANS_BOTH = S.ANS_BOTH   # "{WHO}{L1} {X} भी {V1} और {Y} भी {V2}।"
_V = r"(?:na )?\S+"


def ind_ca(tok):
    """'cakkhundriyañca' -> 'cakkhundriyaṃ'."""
    if tok.endswith("ñca"):
        return tok[:-3] + "ṃ"
    return tok


def tr_pavatti_sentence(s):
    m = re.fullmatch(rf"(.+?) ({LOC_ALT}) (\S+) ((?:na )?[^\s,]+),? no ca ({LOC_ALT}) (\S+) ({_V})\.", s)
    if m:
        who, l1, x, v1, l2, y, v2 = m.groups()
        w, _ = tr_who(who)
        return ANS_BUT.format(WHO=w, L1=LOC1[l1], X=INDRIYA[x], V1=verb(v1), L2=LOC2[l2],
                              Y=INDRIYA[y], V2=verb_flip(v2))
    m = re.fullmatch(rf"(.+?) ({LOC_ALT}) (\S+?)(ñca| ca) ({_V}) (\S+?)(ñca| ca) ({_V})\.", s)
    if m:
        who, l1, x, c1, v1, y, c2, v2 = m.groups()
        x = x + "ṃ" if c1 == "ñca" else x        # cakkhundriyañca / manindriyaṃ ca
        y = y + "ṃ" if c2 == "ñca" else y
        w, _ = tr_who(who)
        return ANS_BOTH.format(WHO=w, L1=LOC1[l1], X=INDRIYA[x], V1=verb(v1),
                               Y=INDRIYA[y], V2=verb(v2))
    return None


# ---------------------------------------------------------------- line level
PE_TAIL = re.compile(r"(\s*)…[Pp]e…(\.?)$")
PE_HEAD = re.compile(r"^…[Pp]e…(\s*)")


def split_sentences(text):
    """Split at '? ' and '. ' outside square brackets."""
    out, buf, depth = [], "", 0
    i = 0
    while i < len(text):
        ch = text[i]
        buf += ch
        if ch == "[":
            depth += 1
        elif ch == "]":
            depth -= 1
        elif ch in "?." and depth == 0 and i + 1 < len(text) and text[i + 1] == " ":
            out.append(buf)
            buf = ""
            i += 1          # skip the space
        i += 1
    if buf:
        out.append(buf)
    return out


def tr_core(s):
    """One sentence without …pe… at its ends."""
    if s in SENT:
        return SENT[s]
    m = re.fullmatch(r"\((\w+)mūlakaṃ\)", s)
    if m:
        return "(" + MULAKA.format(X=INDRIYA[m.group(1)[0].lower() + m.group(1)[1:] + "ṃ"]) + ")"
    if s.endswith("?"):
        r = tr_question(s)
        if r:
            return r
    else:
        r = None
        try:
            r = tr_pavatti_sentence(s)
        except KeyError as e:
            raise ValueError(str(e))
        if r:
            return r
    raise ValueError("untranslated sentence: " + s)


def tr_sentence(s):
    head = ""
    m = PE_HEAD.match(s)
    if m:
        head = "…" + m.group(1)
        s = s[m.end():]
    tail = ""
    m = PE_TAIL.search(s)
    if m:
        sp, dot = m.groups()
        s = s[:m.start()]
        tail = sp + "…" + ("।" if dot else "")
    if s in ("", "."):
        return head.rstrip() + ("।" if s == "." else "") + tail
    if tail.endswith("।") and s + "." in SENT:
        s = s + "."                # "Āmantā …pe…." -> "हाँ …।"
    core = tr_core(s)
    if tail and core.endswith("।") and tail.endswith("।"):
        core = core[:-1]          # "Āmantā …pe…." -> "हाँ …।"
    return head + core + tail


def tr_body(text):
    label = ""
    m = re.match(r"^(\((?:Ka|Kha|Ga|Gha|Ṅa|Ca)\)) (.*)$", text)
    if m and not re.fullmatch(r"\(\w+mūlakaṃ\)", text):
        label, text = S.LABELS[m.group(1)] + " ", m.group(2)
    if text in FIXED_LINES:
        return label + FIXED_LINES[text]
    return label + " ".join(tr_sentence(s) for s in split_sentences(text))


def tr_line(line):
    if not line.strip():
        return ""
    m = ID_RE.search(line)
    bid = m.group(1) if m else None
    text = ID_RE.sub("", line) if m else line
    if text.startswith("#"):
        level = len(text) - len(text.lstrip("#"))
        h = text[level:].strip()
        if h not in HEADINGS:
            raise ValueError("untranslated heading: " + h)
        out = "#" * level + " " + HEADINGS[h]
    else:
        out = tr_body(text.strip())
    return out + (" " + bid if bid else "")


def build(name):
    fname = f"{name}-indriyayamaka.md"
    lines = (PALI_DIR / fname).read_text(encoding="utf-8").splitlines()
    out, errors = [], []
    for n, l in enumerate(lines, 1):
        try:
            out.append(tr_line(l))
        except (ValueError, KeyError) as e:
            errors.append(f"{fname}:{n}: {e}")
            out.append("")
    if errors:
        for e in errors[:40]:
            print(e)
        print(len(errors), "errors in", fname)
        return False
    (HI_DIR / fname).write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
    print(fname, "written,", len([l for l in lines if l.strip()]), "lines")
    return True


if __name__ == "__main__":
    names = sys.argv[1:] or [f"10-{i:02d}" for i in range(1, 7)]
    for nm in names:
        build(nm)
