"""Builder for the Hindi rails translation of pi-1 chapters 3-02 and 3-03 (Rūpakaṇḍa: duka ... ekādasaka).

All Hindi comes from the fixed strings below, so identical Pāli gives byte-identical Hindi.
usage: python -I -X utf8 build_rails_3-02_3-03.py
"""
import re
import sys
import pathlib

RAILS = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-hi\rails")
sys.path.insert(0, str(RAILS))
import build_rails_sample as B  # import only

S = B.S
PALI = B.PALI
OUT = B.OUT

PE = "…"
RUPA = "भौतिक रूप"
EVAM = "इस तरह {n} प्रकार से भौतिक रूप का वर्गीकरण हुआ।"

ANID = "दिखाई न देने वाला और टकराव वाला"
SANID = "दिखाई देने वाला और टकराव वाला"


def adj(vis, g, obl):
    base = SANID if vis else ANID
    if g == "f":
        return base.replace("वाला", "वाली")
    if obl:
        return base.replace("वाला", "वाले")
    return base


def strike(g):
    if g == "f":
        return "टकरा चुकी है, टकराती है, टकराएगी या टकरा सकती है"
    return "टकरा चुका है, टकराता है, टकराएगा या टकरा सकता है"


def arise(g):
    if g == "f":
        return "उत्पन्न हो चुकी है, उत्पन्न होती है, उत्पन्न होगी या उत्पन्न हो सकती है"
    return "उत्पन्न हो चुका है, उत्पन्न होता है, उत्पन्न होगा या उत्पन्न हो सकता है"


ORG = {
    "cakkhu": dict(hi="आँख", g="f", verb="देख चुका है, देखता है, देखेगा या देख सकता है"),
    "sota": dict(hi="कान", g="m", verb="सुन चुका है, सुनता है, सुनेगा या सुन सकता है"),
    "ghāna": dict(hi="नाक", g="f", verb="सूँघ चुका है, सूँघता है, सूँघेगा या सूँघ सकता है"),
    "jivhā": dict(hi="जीभ", g="f", verb="चख चुका है, चखता है, चखेगा या चख सकता है"),
    "kāya": dict(hi="शरीर", g="m", verb="छू चुका है, छूता है, छुएगा या छू सकता है"),
}
for o in ORG.values():
    h = o["hi"]
    o["ay"] = f"{h} का इंद्रिय-क्षेत्र"
    o["dh"] = f"{h} का तत्व"
    o["ind"] = f"{h} की क्षमता"
    o["co"] = f"{h} का संपर्क"
    o["cog"] = f"{h} के संपर्क"
    o["coj"] = f"{h} के संपर्क से उत्पन्न"
    o["vi"] = f"{h} की चेतना"

OBJ = {
    "rūpa": dict(hi="दृश्य रूप", g="m", vis=True, org="cakkhu"),
    "sadda": dict(hi="ध्वनि", g="f", vis=False, org="sota"),
    "gandha": dict(hi="गंध", g="f", vis=False, org="ghāna"),
    "rasa": dict(hi="स्वाद", g="m", vis=False, org="jivhā"),
    "phoṭṭhabba": dict(hi="स्पर्श", g="m", vis=False, org="kāya"),
}
for o in OBJ.values():
    o["ay"] = f"{o['hi']} का इंद्रिय-क्षेत्र"
    o["dh"] = f"{o['hi']} का तत्व"

ITEMS = {
    "itthindriyaṃ": "स्त्रीत्व की क्षमता",
    "purisindriyaṃ": "पुरुषत्व की क्षमता",
    "jīvitindriyaṃ": "जीवन-क्षमता",
    "kāyaviññatti": "शरीर द्वारा प्रकट अभिव्यक्ति",
    "vacīviññatti": "वाणी द्वारा प्रकट अभिव्यक्ति",
    "ākāsadhātu": "आकाश तत्व",
    "āpodhātu": "जल तत्व",
    "pathavīdhātu": "पृथ्वी तत्व",
    "tejodhātu": "अग्नि तत्व",
    "vāyodhātu": "वायु तत्व",
    "rūpassa lahutā": "भौतिक रूप का हल्कापन",
    "rūpassa mudutā": "भौतिक रूप की मृदुता",
    "rūpassa kammaññatā": "भौतिक रूप की कार्य-योग्यता",
    "rūpassa upacayo": "भौतिक रूप की वृद्धि",
    "rūpassa santati": "भौतिक रूप की धारा",
    "rūpassa jaratā": "भौतिक रूप का बुढ़ापा",
    "rūpassa aniccatā": "भौतिक रूप की अनित्यता",
    "kabaḷīkāro āhāro": "कौर-कौर खाया जाने वाला भोजन",
}
ITEMS["sotāyatanaṃ"] = ORG["sota"]["ay"]
ITEMS["cakkhāyatanaṃ"] = ORG["cakkhu"]["ay"]
ITEMS["ghānāyatanaṃ"] = ORG["ghāna"]["ay"]
ITEMS["jivhāyatanaṃ"] = ORG["jivhā"]["ay"]
ITEMS["kāyāyatanaṃ"] = ORG["kāya"]["ay"]
ITEMS.update({
    "cakkhudhātu": ORG["cakkhu"]["dh"], "sotadhātu": ORG["sota"]["dh"], "ghānadhātu": ORG["ghāna"]["dh"],
    "jivhādhātu": ORG["jivhā"]["dh"], "kāyadhātu": ORG["kāya"]["dh"],
    "cakkhundriyaṃ": ORG["cakkhu"]["ind"], "sotindriyaṃ": ORG["sota"]["ind"], "ghānindriyaṃ": ORG["ghāna"]["ind"],
    "jivhindriyaṃ": ORG["jivhā"]["ind"], "kāyindriyaṃ": ORG["kāya"]["ind"],
    "rūpāyatanaṃ": OBJ["rūpa"]["ay"], "saddāyatanaṃ": OBJ["sadda"]["ay"], "gandhāyatanaṃ": OBJ["gandha"]["ay"],
    "rasāyatanaṃ": OBJ["rasa"]["ay"], "phoṭṭhabbāyatanaṃ": OBJ["phoṭṭhabba"]["ay"],
    "rūpadhātu": OBJ["rūpa"]["dh"], "saddadhātu": OBJ["sadda"]["dh"], "gandhadhātu": OBJ["gandha"]["dh"],
    "rasadhātu": OBJ["rasa"]["dh"], "phoṭṭhabbadhātu": OBJ["phoṭṭhabba"]["dh"],
})
ITEM_KEYS = sorted(ITEMS, key=len, reverse=True)


def items(text):
    s = text.lower().replace(",", " ").strip()
    out = ""
    while s:
        if s.startswith("…pe…"):
            out += PE + " "
            s = s[4:].strip()
            continue
        for k in ITEM_KEYS:
            if s == k or s.startswith(k + " ") or s.startswith(k + "…"):
                if out and not out.endswith(PE + " "):
                    out += ", "
                out += ITEMS[k]
                s = s[len(k):].strip()
                break
        else:
            raise ValueError("unknown item: " + s[:60])
    return out.strip()


ADJ = {
    "upādā": "व्युत्पन्न",
    "ajjhattikaṃ": "आंतरिक",
    "bāhiraṃ": "बाह्य",
    "upādiṇṇaṃ": "कर्म से उत्पन्न",
    "upādiṇṇupādāniyaṃ": "कर्म से उत्पन्न और आसक्ति का विषय बनने वाला",
    "anupādiṇṇupādāniyaṃ": "कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाला",
    "sanidassanaṃ": "दिखाई देने वाला",
    "anidassanaṃ": "दिखाई न देने वाला",
    "sappaṭighaṃ": "टकराव वाला",
    "appaṭighaṃ": "टकराव से रहित",
    "oḷārikaṃ": "स्थूल",
    "sukhumaṃ": "सूक्ष्म",
    "dūre": "दूर",
    "santike": "निकट",
    "cittasamuṭṭhānaṃ": "मन से उत्पन्न",
    "cittasahabhu": "मन के साथ-साथ होने वाला",
    "na cittasahabhu": "मन के साथ-साथ न होने वाला",
    "cittānuparivatti": "मन का अनुसरण करने वाला",
    "na cittānuparivatti": "मन का अनुसरण न करने वाला",
    "dhammāyatanapariyāpannaṃ": "मन के विषयों के इंद्रिय-क्षेत्र में समाया हुआ",
}
NEG = {"no upādā": "व्युत्पन्न नहीं", "anupādiṇṇaṃ": "कर्म से उत्पन्न नहीं", "na cittasamuṭṭhānaṃ": "मन से उत्पन्न नहीं"}
NOUN = {"indriyaṃ": "क्षमता", "mahābhūtaṃ": "महाभूत", "viññatti": "प्रकट अभिव्यक्ति"}
NOUN.update(ITEMS)
for k in list(NOUN):
    if k.startswith("rūpassa "):
        tail = k.split(" ", 1)[1]
        NEG[f"rūpassa na {tail}"] = NOUN[k] + " नहीं"
    else:
        NEG[f"na {k}"] = NOUN[k] + " नहीं"
ATOMS = {}
ATOMS.update({k: (v, "a") for k, v in ADJ.items()})
ATOMS.update({k: (v, "x") for k, v in NEG.items()})
ATOMS.update({k: (v, "n") for k, v in NOUN.items()})
ATOM_KEYS = sorted(ATOMS, key=len, reverse=True)

GEN = {"saññāya": "पहचान", "cetanāya": "इरादे"}
for k, o in ORG.items():
    p = {"cakkhu": "cakkhu", "sota": "sota", "ghāna": "ghāna", "jivhā": "jivhā", "kāya": "kāya"}[k]
    GEN[f"{p}samphassassa"] = o["cog"]
    GEN[f"{p}samphassajāya vedanāya"] = o["coj"] + " अनुभूति"
    GEN[f"{p}viññāṇassa"] = o["vi"]


def rest_clause(p):
    parts = [x.strip() for x in re.split(r"\s*…pe…\s*", p)]
    last = parts[-1]
    m = re.match(r"^(.*?) (na )?(vatthu|ārammaṇaṃ)$", last)
    if m:
        parts[-1] = m.group(1)
        head = "आधार" if m.group(3) == "vatthu" else "विषय"
        neg = bool(m.group(2))
        tail = "का " + head + (" नहीं" if neg else "")
        rendered = [GEN[x] + " का" for x in parts[:-1]] + [GEN[parts[-1]] + " " + tail]
        return (f"{PE} ".join(rendered), "x" if neg else "n")
    rendered = []
    neg = False
    for x in parts:
        if x.startswith("na "):
            neg = True
            rendered.append(ITEMS[x[3:]] + " नहीं")
        else:
            rendered.append(ITEMS[x])
    return (f"{PE} ".join(rendered), "x" if neg else "n")


def pred(p):
    p = p.strip().lower()
    atoms = []
    while p:
        for k in ATOM_KEYS:
            if p == k or p.startswith(k + " "):
                atoms.append(ATOMS[k])
                p = p[len(k):].strip()
                break
        else:
            atoms.append(rest_clause(p))
            p = ""
    if len(atoms) == 1:
        return atoms[0][0] + " है"
    if len(atoms) == 2:
        (a, ka), (b, kb) = atoms
        if ka == "a" and kb == "a" and " और " not in a + b:
            return f"{a} और {b} है"
        return f"{a} है और {b} है"
    if len(atoms) == 3:
        return f"{atoms[0][0]}, {atoms[1][0]} और {atoms[2][0]} है"
    raise ValueError(p)


def frame(start, pr):
    return f"{start}, {pr}" if pr.startswith(RUPA) else f"{start} {pr}"


def question(p):
    return frame("कौन-सा " + RUPA, pred(p)) + "?"


def closing(p, end="।"):
    return frame("यह " + RUPA, pred(p)) + end


def organ_tail(k):
    o = ORG[k]
    extra = "यह नेत्र भी है, यह नयन भी है, " if k == "cakkhu" else ""
    return (f"यह {o['hi']} भी है, यह {o['ay']} भी है, यह {o['dh']} भी है, यह {o['ind']} भी है, यह लोक भी है, "
            f"यह द्वार भी है, यह सागर भी है, यह उज्ज्वलता भी है, यह खेत भी है, यह आधार भी है, {extra}"
            f"यह इस पार का किनारा भी है, यह सूना गाँव भी है")


def organ_head(k, var=""):
    return (f"जो {ORG[k]['hi']}{var} चार महाभूतों से व्युत्पन्न ऐसी संवेदनशीलता है जो व्यक्तिगत अस्तित्व में समाई हुई, "
            f"दिखाई न देने वाली और टकराव वाली है")


def run4_organ(k, obj):
    o, b = ORG[k], OBJ[obj]
    h, bh = o["hi"], b["hi"]
    return (f"जिस {h} के सहारे, {bh} को विषय बनाकर, {o['co']} {arise('m')}{PE} "
            f"जिस {h} के सहारे, {bh} को विषय बनाकर, {o['coj']} अनुभूति{PE} पहचान{PE} इरादा{PE} {o['vi']} {arise('f')}{PE} "
            f"जिस {h} के सहारे {bh} के विषय वाला {o['co']} {arise('m')}{PE} "
            f"जिस {h} के सहारे {bh} के विषय वाली, {o['coj']} अनुभूति{PE} पहचान{PE} इरादा{PE} {o['vi']} {arise('f')}")


def run4_object(obj):
    b = OBJ[obj]
    o = ORG[b["org"]]
    h, bh = o["hi"], b["hi"]
    return (f"जिस {bh} को विषय बनाकर, {h} के सहारे, {o['co']} {arise('m')}{PE} "
            f"जिस {bh} को विषय बनाकर, {h} के सहारे, {o['coj']} अनुभूति{PE} पहचान{PE} इरादा{PE} {o['vi']} {arise('f')}{PE} "
            f"जिस {bh} के विषय वाला {o['co']}, {h} के सहारे, {arise('m')}{PE} "
            f"जिस {bh} के विषय वाली, {o['coj']} अनुभूति{PE} पहचान{PE} इरादा{PE} {o['vi']}, {h} के सहारे, {arise('f')}")


def organ_seg(k, v, var=""):
    o = ORG[k]
    b = OBJ[[x for x in OBJ if OBJ[x]["org"] == k][0]]
    objk = [x for x in OBJ if OBJ[x]["org"] == k][0]
    h, bh = o["hi"], b["hi"]
    g, bg = o["g"], b["g"]
    if v == 1:
        c = f"जिस {adj(False, g, True)} {h} से कोई {adj(b['vis'], bg, True)} {bh} को {o['verb']}"
    elif v == 2:
        c = f"जिस {adj(False, g, True)} {h} से {adj(b['vis'], bg, False)} {bh} {strike(bg)}"
    elif v == 3:
        c = f"जो {adj(False, g, False)} {h} {adj(b['vis'], bg, True)} {bh} से {strike(g)}"
    else:
        c = run4_organ(k, objk)
    ayat = {"cakkhu": "cakkhāyatanaṃ", "sota": "sotāyatanaṃ", "ghāna": "ghānāyatanaṃ", "jivhā": "jivhāyatanaṃ", "kāya": "kāyāyatanaṃ"}[k]
    return f"{question(ayat)} {organ_head(k, var)}, {c}, {organ_tail(k)} – {closing(ayat)}"


V = lambda sig, word: f" [वर्तनी-भेद ({sig}): {word}]"
P = lambda sig, word: f" [पाठभेद ({sig}): {word}]"


def rupa_list(var):
    a = V("Sī., Syā.", "mañjeṭṭhakaṃ") if var else ""
    b = V("Sī., Ka.", "caturassaṃ") if var else ""
    c = V("Sī., Syā.", "suriyamaṇḍalassa") if var else ""
    return (f"नीला, पीला, लाल, सफ़ेद, काला, मजीठ जैसा गहरा लाल{a}, हरा, हरे रंग का, आम की कोंपलों के रंग का, लंबा, छोटा, महीन, मोटा, "
            f"गोल, वृत्ताकार, चौकोर{b}, छह कोनों वाला, आठ कोनों वाला, सोलह कोनों वाला, नीची भूमि, ऊँची भूमि, छाया, धूप, प्रकाश, अंधकार, "
            f"बादल, कोहरा, धुआँ, धूल, चंद्र-मंडल की रंग-आभा, सूर्य-मंडल{c} की रंग-आभा, तारों की रंग-आभा, दर्पण-मंडल की रंग-आभा, "
            f"मणि, शंख, मोती और वैदूर्य की रंग-आभा, सोने और चाँदी की रंग-आभा")


SADDA_LIST = ("नगाड़े की ध्वनि, मृदंग की ध्वनि, शंख की ध्वनि, ढोलक की ध्वनि, गाने की ध्वनि, बाजे की ध्वनि, मंजीरे की ध्वनि, ताली की ध्वनि, "
              "प्राणियों का शोर, वस्तुओं के आपस में टकराने की ध्वनि, हवा की ध्वनि, पानी की ध्वनि, मनुष्यों की ध्वनि, अमानवीय प्राणियों की ध्वनि")
GANDHA_LIST = ("जड़ों की गंध, लकड़ी के सार की गंध, छाल की गंध, पत्तों की गंध, फूलों की गंध, फलों की गंध, कच्चे मांस की गंध, सड़न की गंध, सुगंध, दुर्गंध")


def rasa_list(var):
    a = P("Sī.", "lapilakaṃ") if var else ""
    return ("जड़ों का स्वाद, तनों का स्वाद, छाल का स्वाद, पत्तों का स्वाद, फूलों का स्वाद, फलों का स्वाद, खट्टा, मीठा, कड़वा, तीखा, नमकीन, "
            f"खारा, हल्का खट्टा{a}, कसैला, स्वादिष्ट, बेस्वाद")


TOUCH_LIST = "पृथ्वी तत्व, अग्नि तत्व, वायु तत्व, कठोर, मुलायम, चिकना, खुरदरा, सुखद संपर्क वाला, दुःखद संपर्क वाला, भारी, हल्का"


def object_head(obj, var):
    b = OBJ[obj]
    bh, g = b["hi"], b["g"]
    d = adj(b["vis"], g, False)
    if obj == "phoṭṭhabba":
        return TOUCH_LIST
    if obj == "rūpa":
        lst, core = rupa_list(var), "चार महाभूतों से व्युत्पन्न रंग-आभा है"
    elif obj == "sadda":
        lst, core = SADDA_LIST, "चार महाभूतों से व्युत्पन्न है"
    elif obj == "gandha":
        lst, core = GANDHA_LIST, "चार महाभूतों से व्युत्पन्न है"
    else:
        lst, core = rasa_list(var), "चार महाभूतों से व्युत्पन्न है"
    return f"जो {bh} {core}, {d} है, जैसे {lst}, या जो भी अन्य {bh} {core}, {d} है"


def object_seg(obj, v, var=False):
    b = OBJ[obj]
    o = ORG[b["org"]]
    h, bh = o["hi"], b["hi"]
    g, bg = o["g"], b["g"]
    if v == 1:
        c = f"जिस {adj(b['vis'], bg, True)} {bh} को कोई {adj(False, g, True)} {h} से {o['verb']}"
    elif v == 2:
        c = f"जिस {adj(b['vis'], bg, True)} {bh} से {adj(False, g, False)} {h} {strike(g)}"
    elif v == 3:
        c = f"जो {adj(b['vis'], bg, False)} {bh} {adj(False, g, True)} {h} से {strike(bg)}"
    else:
        c = run4_object(obj)
    ayat = {"rūpa": "rūpāyatanaṃ", "sadda": "saddāyatanaṃ", "gandha": "gandhāyatanaṃ", "rasa": "rasāyatanaṃ", "phoṭṭhabba": "phoṭṭhabbāyatanaṃ"}[obj]
    tail = f"यह {bh} भी है, यह {b['ay']} भी है, यह {b['dh']} भी है"
    return f"{question(ayat)} {object_head(obj, var)}, {c}, {tail} – {closing(ayat)}"


CITTA3 = "हितकर मन वाले, हानिकर मन वाले या नैतिक रूप से अनिर्धारित मन वाले व्यक्ति"
INTIM = "प्रकट अभिव्यक्ति, प्रकट करना, प्रकट कर चुका होना"
BODY_DEF = (f"{CITTA3} के आगे बढ़ते, पीछे हटते, सामने देखते, इधर-उधर देखते, अंग सिकोड़ते या अंग फैलाते समय शरीर का जो तनना, भली-भाँति तनना, "
            f"भली-भाँति तना हुआ होना, {INTIM} है")
_vaci = f"{CITTA3} की जो वाणी, बोल, बोलने का ढंग, उच्चारण, आवाज़, आवाज़ निकालना, वाणी, वाणी का फूटना है{{sep}}यह वाणी कही जाती है। उस वाणी से जो {INTIM} है"
JIVITA = S["jīvita"] if "jīvita" in S else re.sub(r" \[[^\]]*\]", "", S["jīvita_var"])
_food = ("भात, दलिया, सत्तू, मछली, मांस, दूध, दही, घी, मक्खन, तेल, शहद, गुड़, या जो भी अन्य भौतिक रूप जिस-जिस प्रदेश में उन-उन प्राणियों के लिए "
         "मुँह से खाया जाने वाला, दाँतों से चबाया जाने वाला, गले से नीचे उतारा जाने वाला और पेट भरने वाला है, जिस पोषक सार से प्राणी जीवित रहते हैं")
_ext = "चाहे स्वयं में हो या दूसरों से संबंधित हो, चाहे कर्म से उत्पन्न हो या कर्म से उत्पन्न न हो"

ITTHI = "जो स्त्री की आकृति, स्त्री का चिह्न, स्त्री का आचरण, स्त्री का ढंग, स्त्री होना, स्त्री होने का भाव{v} है"
PURISA = "जो पुरुष की आकृति, पुरुष का चिह्न, पुरुष का आचरण, पुरुष का ढंग, पुरुष होना, पुरुष होने का भाव है"
AKASA = "जो आकाश, आकाश की प्रकृति वाला, रिक्त स्थान, रिक्त स्थान की प्रकृति वाला, छेद, छेद की प्रकृति वाला है, जो चार महाभूतों से अछूता है"
APO = "जो जल, जल की प्रकृति वाला, नमी, नमी की प्रकृति वाला, भौतिक रूप को बाँधे रखना है"
JARA = "भौतिक रूप का जो बुढ़ापा, जीर्ण होना, दाँतों का टूटना, बालों का पकना, त्वचा पर झुर्रियाँ पड़ना, आयु का घटना, इंद्रियों का पूरी तरह पक जाना है"
ANICCA = "भौतिक रूप का जो क्षय, नाश, टूटना, बिखर जाना, अनित्यता, लुप्त हो जाना है"

EXACT = {
    "Yaṃ cakkhu catunnaṃ mahābhūtānaṃ upādāya pasādo…pe… suñño gāmo peso": f"जो आँख चार महाभूतों से व्युत्पन्न संवेदनशीलता है{PE} यह सूना गाँव भी है",
    "Yo kāyo catunnaṃ mahābhūtānaṃ upādāya pasādo…pe… suñño gāmo peso": f"जो शरीर चार महाभूतों से व्युत्पन्न संवेदनशीलता है{PE} यह सूना गाँव भी है",
    "Yaṃ rūpaṃ catunnaṃ mahābhūtānaṃ upādāya vaṇṇanibhā…pe… rūpadhātu pesā": f"जो दृश्य रूप चार महाभूतों से व्युत्पन्न रंग-आभा है{PE} यह दृश्य रूप का तत्व भी है",
    "Pathavīdhātu…pe… phoṭṭhabbadhātu pesā": f"पृथ्वी तत्व{PE} यह स्पर्श का तत्व भी है",
    "Yaṃ itthiyā itthiliṅgaṃ itthinimittaṃ itthikuttaṃ itthākappo itthattaṃ itthibhāvo": ITTHI.format(v=""),
    "Yaṃ itthiyā itthiliṅgaṃ itthinimittaṃ itthikuttaṃ itthākappo itthattaṃ itthibhāvo [itthittaṃ itthībhāvo (syā.)]": ITTHI.format(v=V("Syā.", "itthittaṃ itthībhāvo")),
    "Yaṃ purisassa purisaliṅgaṃ purisanimittaṃ purisakuttaṃ purisākappo purisattaṃ purisabhāvo": PURISA,
    "Yo tesaṃ rūpīnaṃ dhammānaṃ āyu ṭhiti yapanā yāpanā iriyanā vattanā pālanā jīvitaṃ jīvitindriyaṃ": f"उन भौतिक परिघटनाओं की जो {JIVITA} है",
    "Yā kusalacittassa vā akusalacittassa vā abyākatacittassa vā abhikkamantassa vā paṭikkamantassa vā ālokentassa vā vilokentassa vā samiñjentassa vā pasārentassa vā kāyassa thambhanā santhambhanā santhambhitattaṃ viññatti viññāpanā viññāpitattaṃ": BODY_DEF,
    "Yā kusalacittassa vā akusalacittassa vā abyākatacittassa vā vācā girā byappatho udīraṇaṃ ghoso ghosakammaṃ vācā vacībhedo – ayaṃ vuccati vācā. Yā tāya vācāya viññatti viññāpanā viññāpitattaṃ": _vaci.format(sep=" – "),
    "Yā kusalacittassa vā akusalacittassa vā abyākatacittassa vā vācā girā byappatho udīraṇaṃ ghoso ghosakammaṃ vācā vacībhedo, ayaṃ vuccati vācā. Yā tāya vācāya viññatti viññāpanā viññāpitattaṃ": _vaci.format(sep=", "),
    "Yā kusalacittassa vā akusalacittassa vā abyākatacittassa vā vācā girā byappatho udīraṇaṃ dhoso ghosakammaṃ vācā vacībhedo, ayaṃ vuccati vācā. Yā tāya vācāya viññatti viññāpanā viññāpitattaṃ": _vaci.format(sep=", "),
    "Yo ākāso ākāsagataṃ aghaṃ aghagataṃ vivaro vivaragataṃ asamphuṭṭhaṃ catūhi mahābhūtehi": AKASA,
    "Yā rūpassa lahutā lahupariṇāmatā adandhanatā avitthanatā": f"भौतिक रूप का जो {S['lahutā']} है",
    "Yā rūpassa mudutā maddavatā akakkhaḷatā akathinatā": f"भौतिक रूप की जो {S['mudutā']} है",
    "Yā rūpassa kammaññatā kammaññattaṃ kammaññabhāvo": f"भौतिक रूप की जो {S['kammaññatā']} है",
    "Yo āyatanānaṃ ācayo, so rūpassa upacayo": "इंद्रिय-क्षेत्रों का जो संचय है, वह भौतिक रूप की वृद्धि है",
    "Yo rūpassa upacayo, sā rūpassa santati": "भौतिक रूप की जो वृद्धि है, वह भौतिक रूप की धारा है",
    "Yā rūpassa jarā jīraṇatā khaṇḍiccaṃ pāliccaṃ valittacatā āyuno saṃhāni indriyānaṃ paripāko": JARA,
    "Yo rūpassa khayo vayo bhedo paribhedo aniccatā antaradhānaṃ": ANICCA,
    "Odano kummāso sattu maccho maṃsaṃ khīraṃ dadhi sappi navanītaṃ telaṃ madhu phāṇitaṃ, yaṃ vā panaññampi atthi rūpaṃ yamhi yamhi janapade tesaṃ tesaṃ sattānaṃ mukhāsiyaṃ dantavikhādanaṃ galajjhoharaṇīyaṃ kucchivitthambhanaṃ, yāya ojāya sattā yāpenti": _food,
    "Odano kummāso sattu maccho maṃsaṃ khīraṃ dadhi sappi navanītaṃ telaṃ madhu phāṇitaṃ, yaṃ vā panaññampi atthi rūpaṃ yamhi yamhi janapade tesaṃ tesaṃ sattānaṃ mukhāsiyaṃ dantavikhādanaṃ galajjhoharaṇīyaṃ kucchivitthambhanaṃ yāya ojāya sattā yāpenti": _food,
    "Yaṃ āpo āpogataṃ sineho sinehagataṃ bandhanattaṃ rūpassa": APO,
    "Yaṃ āpo āpogataṃ sineho sinehagataṃ bandhanattaṃ rūpassa ajjhattaṃ vā bahiddhā vā upādiṇṇaṃ vā anupādiṇṇaṃ vā": f"{APO}, {_ext}",
    "Yaṃ kakkhaḷaṃ kharagataṃ [kharigataṃ (ka.)] kakkhaḷattaṃ kakkhaḷabhāvo ajjhattaṃ vā bahiddhā vā upādiṇṇaṃ vā anupādiṇṇaṃ vā": f"जो कठोर, कर्कशता की प्रकृति वाला{V('Ka.', 'kharigataṃ')}, कठोरता, कठोर होने का भाव है, {_ext}",
    "Yaṃ tejo tejogataṃ usmā usmāgataṃ usumaṃ usumagataṃ ajjhattaṃ vā bahiddhā vā upādiṇṇaṃ vā anupādiṇṇaṃ vā": f"जो अग्नि, अग्नि की प्रकृति वाला, ऊष्मा, ऊष्मा की प्रकृति वाला, गरमी, गरमी की प्रकृति वाला है, {_ext}",
    "Yaṃ vāyo vāyogataṃ thambhitattaṃ rūpassa ajjhattaṃ vā bahiddhā vā upādiṇṇaṃ vā anupādiṇṇaṃ vā": f"जो वायु, वायु की प्रकृति वाला, भौतिक रूप का तना हुआ होना है, {_ext}",
}

OTHER = {
    "kammassa katattā": "कर्म किए जाने के कारण है",
    "na kammassa katattā": "कर्म किए जाने के कारण नहीं है",
    "cittajaṃ cittahetukaṃ cittasamuṭṭhānaṃ": "मन से जन्मा, मन के कारण होने वाला और मन से उत्पन्न है",
    "na cittajaṃ na cittahetukaṃ na cittasamuṭṭhānaṃ": "न मन से जन्मा है, न मन के कारण होने वाला है, न मन से उत्पन्न है",
}


def answer(a):
    a = a.strip()
    if a in EXACT:
        return EXACT[a]
    m = re.match(r"^(Na k|K)ammassa katattā (.+)$", a)
    if m:
        lst = items(m.group(2))
        pl = "," in lst
        neg = m.group(1) == "Na k"
        verb = ("नहीं हैं" if pl else "नहीं है") if neg else ("हैं" if pl else "है")
        return f"{lst}, जो कर्म किए जाने के कारण {verb}"
    m = re.match(r"^(.*?),?\s*yaṃ vā panaññampi atthi rūpaṃ (na kammassa katattā|kammassa katattā|na cittajaṃ na cittahetukaṃ na cittasamuṭṭhānaṃ|cittajaṃ cittahetukaṃ cittasamuṭṭhānaṃ),?\s+(.*)$", a)
    if m:
        return f"{items(m.group(1))}, या जो भी अन्य भौतिक रूप {OTHER[m.group(2)]}, जैसे {items(m.group(3))}"
    return items(a)


FIX = {
    "Katamaṃ taṃ rūpaṃ upādā sukhumaṃ itthindriyaṃ": "Katamaṃ taṃ rūpaṃ upādā sukhumaṃ? Itthindriyaṃ",
    "Katamaṃ taṃ rūpaṃ upādiṇṇupādāniyaṃ santike cakkhāyatanaṃ": "Katamaṃ taṃ rūpaṃ upādiṇṇupādāniyaṃ santike? Cakkhāyatanaṃ",
}
REG = re.compile(r"^Katamaṃ taṃ rūpaṃ (.+?)[?.] (.+?) – idaṃ taṃ rūpaṃ (.+?)([.?])$")


def regular(line):
    for k, v in FIX.items():
        if line.startswith(k):
            line = line.replace(k, v, 1)
    m0 = re.match(r"^Katamaṃ taṃ rūpaṃ (.+?)\? ([^–]+)\.$", line)
    if m0:
        return f"{question(m0.group(1))} {items(m0.group(2))}।"
    m = REG.match(line)
    if not m:
        raise ValueError("no match: " + line[:90])
    q, a, c, e = m.groups()
    return f"{question(q)} {answer(a)} – {closing(c, '?' if e == '?' else '।')}"


L_NO = {"दो": "duvidhena", "तीन": "tividhena", "चार": "catubbidhena", "पाँच": "pañcavidhena", "छह": "chabbidhena",
        "सात": "sattavidhena", "आठ": "aṭṭhavidhena", "नौ": "navavidhena", "दस": "dasavidhena", "ग्यारह": "ekādasavidhena"}
LINES = {f"Evaṃ {v} rūpasaṅgaho.": EVAM.format(n=k) for k, v in L_NO.items()}
LINES.update({
    "Idaṃ taṃ rūpaṃ upādā.": "यह भौतिक रूप व्युत्पन्न है।",
    "Upādābhājanīyaṃ.": "व्युत्पन्न भौतिक रूप का विश्लेषण।",
    "Rūpakaṇḍe paṭhamabhāṇavāro.": "भौतिक रूप के अध्याय में पहला पाठ-खंड।",
    "Idaṃ taṃ rūpaṃ no upādā.": "यह भौतिक रूप व्युत्पन्न नहीं है।",
    "Dukaniddeso.": "दो-दो के वर्गीकरणों की व्याख्या।",
    "Tikaniddeso.": "तीन-तीन के वर्गीकरणों की व्याख्या।",
    "Catukkaṃ.": "चार-चार के वर्गीकरण।",
    "Pañcakaṃ.": "पाँच-पाँच के वर्गीकरण।",
    "Chakkaṃ.": "छह-छह के वर्गीकरण।",
    "Sattakaṃ.": "सात-सात के वर्गीकरण।",
    "Aṭṭhakaṃ.": "आठ-आठ के वर्गीकरण।",
    "Navakaṃ.": "नौ-नौ के वर्गीकरण।",
    "Dasakaṃ.": "दस-दस के वर्गीकरण।",
    "Ekādasakaṃ.": "ग्यारह-ग्यारह के वर्गीकरण।",
    "Aṭṭhamabhāṇavāro.": "आठवाँ पाठ-खंड।",
    "Rūpavibhatti.": "भौतिक रूप का वर्गीकरण।",
    "Rūpakaṇḍaṃ niṭṭhitaṃ.": "भौतिक रूप का अध्याय पूरा हुआ।",
})
HEAD = {
    "##### Dukaniddeso": "##### दो-दो के वर्गीकरणों की व्याख्या",
    "###### Upādābhājanīyaṃ": "###### व्युत्पन्न भौतिक रूप का विश्लेषण",
    "##### Tikaniddeso": "##### तीन-तीन के वर्गीकरणों की व्याख्या",
    "##### Catukkaṃ": "##### चार-चार के वर्गीकरण",
    "##### Pañcakaṃ": "##### पाँच-पाँच के वर्गीकरण",
    "##### Chakkaṃ": "##### छह-छह के वर्गीकरण",
    "##### Sattakaṃ": "##### सात-सात के वर्गीकरण",
    "##### Aṭṭhakaṃ": "##### आठ-आठ के वर्गीकरण",
    "##### Navakaṃ": "##### नौ-नौ के वर्गीकरण",
    "##### Dasakaṃ": "##### दस-दस के वर्गीकरण",
    "##### Ekādasakaṃ": "##### ग्यारह-ग्यारह के वर्गीकरण",
}

AY5 = "दृश्य रूप का इंद्रिय-क्षेत्र, ध्वनि का इंद्रिय-क्षेत्र, गंध का इंद्रिय-क्षेत्र, स्वाद का इंद्रिय-क्षेत्र और स्पर्श का इंद्रिय-क्षेत्र"
K = "जाना जा सकने वाला भौतिक रूप"
SENSE4 = (f"दृश्य रूप का इंद्रिय-क्षेत्र आँख से {K} है, ध्वनि का इंद्रिय-क्षेत्र कान से {K} है, गंध का इंद्रिय-क्षेत्र नाक से {K} है, "
          f"स्वाद का इंद्रिय-क्षेत्र जीभ से {K} है")
TOUCH5 = f"स्पर्श का इंद्रिय-क्षेत्र शरीर से {K} है"
MD = f"{AY5} मन के तत्व से {K} है"
MVD = f"सारा भौतिक रूप मन की चेतना के तत्व से {K} है"

SPECIAL = {
    "1-966": "दृश्य रूप का इंद्रिय-क्षेत्र देखा हुआ है, ध्वनि का इंद्रिय-क्षेत्र सुना हुआ है, गंध का इंद्रिय-क्षेत्र, स्वाद का इंद्रिय-क्षेत्र और स्पर्श का इंद्रिय-क्षेत्र अनुभव किया हुआ है, सारा भौतिक रूप मन से जाना हुआ भौतिक रूप है।",
    "1-972": f"{SENSE4}, {TOUCH5}, सारा भौतिक रूप मन से {K} है।",
    "1-973": f"{SENSE4}, {TOUCH5}, {MD}, {MVD}।",
    "1-974": f"{SENSE4}, मनभावन, सुखद संपर्क वाला स्पर्श शरीर से {K} है, मन को न भाने वाला, दुःखद संपर्क वाला स्पर्श शरीर से {K} है, {MD}, {MVD}।",
}

ORG_IDS = {}
for i, k in enumerate(["cakkhu", "sota", "ghāna", "jivhā", "kāya"]):
    for v in range(4):
        ORG_IDS[f"1-{596 + 4 * i + v}"] = (k, v + 1)
OBJ_IDS = {}
for i, k in enumerate(["rūpa", "sadda", "gandha", "rasa"]):
    for v in range(4):
        OBJ_IDS[f"1-{616 + 4 * i + v}"] = (k, v + 1)
for v in range(4):
    OBJ_IDS[f"1-{647 + v}"] = ("phoṭṭhabba", v + 1)

ID_TAIL = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")


def translate_line(sid, line, idx):
    t = ID_TAIL.sub("", line).strip()
    if t.startswith("#"):
        return HEAD[t]
    if t in LINES:
        return LINES[t]
    if idx == 0 and sid in SPECIAL:
        return SPECIAL[sid]
    if idx == 0 and sid in ORG_IDS:
        k, v = ORG_IDS[sid]
        var = V("Sī., Syā.", "cakkhuṃ") if sid == "1-596" else ""
        return organ_seg(k, v, var)
    if idx == 0 and sid in OBJ_IDS:
        k, v = OBJ_IDS[sid]
        return object_seg(k, v, sid in ("1-616", "1-628"))
    return regular(t)


def build(ch):
    src = PALI / ch
    hindi = {}
    for sid, plines in B.segments(src):
        hindi[sid] = [translate_line(sid, l, i) for i, l in enumerate(plines)]
    B.emit(src, hindi, OUT / ch)


if __name__ == "__main__":
    build("3-02-rupakandam.md")
    build("3-03-rupakandam.md")
