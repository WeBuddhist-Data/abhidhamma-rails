"""Build the Hindi rails translation of 3-01-rupakandam (pi-1) from fixed strings.

Every source line is parsed or looked up; an unknown Pali line or item stops the build.
Also writes notes-3-01.md (every list item as `Pali = Hindi`).
"""
import pathlib, re, sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
SRC = ROOT / "AI_translation/pali/pi-1_split_chapters/3-01-rupakandam.md"
OUT = ROOT / "AI_translation/hindi/pi-1-hindi-plain-rails_split_chapters/3-01-rupakandam.md"
NOTES = ROOT / "0-INBOX/temp/pipeline/pi-1-hi/rails/notes-3-01.md"
ID = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")

RUPA = "भौतिक रूप"

# ---------------------------------------------------------------- predicates
P = {}


def pos_neg(pali, hi, neg_hi=None, neg_pali=None):
    P[pali] = hi
    P[neg_pali or "na " + pali] = neg_hi or hi + " नहीं"


pos_neg("upādā", "व्युत्पन्न", neg_pali="no upādā")
pos_neg("upādiṇṇaṃ", "कर्म से उत्पन्न", neg_pali="anupādiṇṇaṃ")
P["upādiṇṇupādāniyaṃ"] = "कर्म से उत्पन्न और आसक्ति का विषय बनने वाला"
P["anupādiṇṇupādāniyaṃ"] = "कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाला"
P["sanidassanaṃ"] = "दिखाई देने वाला"
P["anidassanaṃ"] = "दिखाई न देने वाला"
P["sappaṭighaṃ"] = "टकराव वाला"
P["appaṭighaṃ"] = "टकराव से रहित"
pos_neg("indriyaṃ", "क्षमता")
pos_neg("mahābhūtaṃ", "महाभूत")
pos_neg("viññatti", "प्रकट अभिव्यक्ति")
pos_neg("cittasamuṭṭhānaṃ", "मन से उत्पन्न")
pos_neg("cittasahabhu", "मन के साथ-साथ होने वाला", "मन के साथ-साथ न होने वाला")
pos_neg("cittānuparivatti", "मन का अनुसरण करने वाला", "मन का अनुसरण न करने वाला")
P["ajjhattikaṃ"] = "आंतरिक"
P["bāhiraṃ"] = "बाह्य"
P["oḷārikaṃ"] = "स्थूल"
P["sukhumaṃ"] = "सूक्ष्म"
P["dūre"] = "दूर"
P["santike"] = "निकट"

SENSES = [("cakkhu", "आँख"), ("sota", "कान"), ("ghāna", "नाक"), ("jivhā", "जीभ"), ("kāya", "शरीर")]
for s, h in SENSES:
    gen = f"{h} के संपर्क का"
    P[f"{s}samphassassa"] = gen
    P[f"{s}samphassassa vatthu"] = f"{gen} आधार"
    P[f"{s}samphassassa na vatthu"] = f"{gen} आधार नहीं"
    P[f"{s}samphassassa ārammaṇaṃ"] = f"{gen} विषय"
    P[f"{s}samphassassa nārammaṇaṃ"] = f"{gen} विषय नहीं"
    P[f"{s}samphassajāya vedanāya"] = f"{h} के संपर्क से उत्पन्न अनुभूति का"
    v = f"{h} की चेतना का"
    P[f"{s}viññāṇassa vatthu"] = f"{v} आधार"
    P[f"{s}viññāṇassa na vatthu"] = f"{v} आधार नहीं"
    P[f"{s}viññāṇassa ārammaṇaṃ"] = f"{v} विषय"
    P[f"{s}viññāṇassa nārammaṇaṃ"] = f"{v} विषय नहीं"
P["saññāya"] = "पहचान का"
P["cetanāya"] = "इरादे का"

AY = {"cakkhāyatanaṃ": "आँख", "sotāyatanaṃ": "कान", "ghānāyatanaṃ": "नाक", "jivhāyatanaṃ": "जीभ",
      "kāyāyatanaṃ": "शरीर", "rūpāyatanaṃ": "दृश्य रूप", "saddāyatanaṃ": "ध्वनि", "gandhāyatanaṃ": "गंध",
      "rasāyatanaṃ": "स्वाद", "phoṭṭhabbāyatanaṃ": "स्पर्श"}
for k, h in AY.items():
    pos_neg(k, f"{h} का इंद्रिय-क्षेत्र")
DH = {"cakkhudhātu": "आँख", "sotadhātu": "कान", "ghānadhātu": "नाक", "jivhādhātu": "जीभ", "kāyadhātu": "शरीर",
      "rūpadhātu": "दृश्य रूप", "saddadhātu": "ध्वनि", "gandhadhātu": "गंध", "rasadhātu": "स्वाद",
      "phoṭṭhabbadhātu": "स्पर्श"}
for k, h in DH.items():
    pos_neg(k, f"{h} का तत्व")
IN = {"cakkhundriyaṃ": "आँख की क्षमता", "sotindriyaṃ": "कान की क्षमता", "ghānindriyaṃ": "नाक की क्षमता",
      "jivhindriyaṃ": "जीभ की क्षमता", "kāyindriyaṃ": "शरीर की क्षमता", "itthindriyaṃ": "स्त्रीत्व की क्षमता",
      "purisindriyaṃ": "पुरुषत्व की क्षमता", "jīvitindriyaṃ": "जीवन-क्षमता"}
for k, h in IN.items():
    pos_neg(k, h)
pos_neg("kāyaviññatti", "शरीर द्वारा प्रकट अभिव्यक्ति")
pos_neg("vacīviññatti", "वाणी द्वारा प्रकट अभिव्यक्ति")
pos_neg("ākāsadhātu", "आकाश तत्व")
pos_neg("āpodhātu", "जल तत्व")
pos_neg("kabaḷīkāro āhāro", "कौर-कौर खाया जाने वाला भोजन")
RQ = {"lahutā": "का हल्कापन", "mudutā": "की मृदुता", "kammaññatā": "की कार्य-योग्यता", "upacayo": "की वृद्धि",
      "santati": "की धारा", "jaratā": "का बुढ़ापा", "aniccatā": "की अनित्यता"}
for k, h in RQ.items():
    P[f"rūpassa {k}"] = f"{RUPA} {h}"
    P[f"rūpassa na {k}"] = f"{RUPA} {h} नहीं"


def chain(item):
    parts = [x.strip() for x in re.split(r"\s*…pe…\s*", item.strip())]
    return "… ".join(P[x] for x in parts)


def is_q(item):
    return item.strip().startswith("rūpassa ")


def atthi_two(x, y):
    if is_q(x):
        return f"कुछ {RUPA} ऐसा है जो {chain(x)} है, कुछ {RUPA} ऐसा है जो {chain(y)} है।"
    return f"कुछ {RUPA} {chain(x)} है, कुछ {RUPA} {chain(y)} है।"


def sentence(s):
    s = s.strip()
    assert s.endswith("."), s
    s = s[:-1]
    if s.startswith("Atthi rūpaṃ "):
        x, y = s[len("Atthi rūpaṃ "):].split(", atthi rūpaṃ ")
        return atthi_two(x, y)
    if s.startswith("Yaṃ taṃ rūpaṃ "):
        subj, pred = s[len("Yaṃ taṃ rūpaṃ "):].split(", taṃ ", 1)
        head = f"जो {RUPA} {chain(subj)} है,"
        if pred.startswith("atthi "):
            y, w = re.split(r",?\s*atthi\s+", pred[len("atthi "):])
            if is_q(y):
                return f"{head} उसमें कुछ ऐसा है जो {chain(y)} है, कुछ ऐसा है जो {chain(w)} है।"
            return f"{head} उसमें कुछ {chain(y)} है, कुछ {chain(w)} है।"
        return f"{head} वह {chain(pred)} है।"
    raise KeyError(s)


def frame_line(line):
    parts = re.split(r"(?<=\.)\s+(?=(?:Atthi|Yaṃ)\b)", line)
    return " ".join(sentence(x) for x in parts)


# ---------------------------------------------------------------- the one-kind list (1-584 / 1-594)
# (Pali in 1-584, Pali in 1-594, Hindi in 1-584, Hindi in 1-594)
def e(p1, p2, hi, hi2=None):
    return (p1, p2, hi, (hi2 or hi) + " ही")


EKA = [
    e("na hetu", "na hetumeva", "मूल रूपी न होने वाला"),
    e("ahetukaṃ", "ahetukameva", "मूल से रहित"),
    e("hetuvippayuttaṃ", "hetuvippayuttameva", "मूलों से अलग"),
    e("sappaccayaṃ", "sappaccayameva", "कारणों पर निर्भर रहने वाला"),
    e("saṅkhataṃ", "saṅkhatameva", "निर्मित"),
    e("rūpaṃ [rūpiyaṃ (sī.)]", "rūpameva", "भौतिक [पाठभेद (Sī.): rūpiyaṃ]", "भौतिक"),
    e("lokiyaṃ", "lokiyameva", "लौकिक"),
    e("sāsavaṃ", "sāsavameva", "मन के मैलों का विषय बनने वाला"),
    e("saṃyojaniyaṃ", "saṃyojaniyameva", "बंधनों का विषय बनने वाला"),
    e("ganthaniyaṃ", "ganthaniyameva", "गाँठों का विषय बनने वाला"),
    e("oghaniyaṃ", "oghaniyameva", "बाढ़ों का विषय बनने वाला"),
    e("yoganiyaṃ", "yoganiyameva", "जकड़नों का विषय बनने वाला"),
    e("nīvaraṇiyaṃ", "nīvaraṇiyameva", "बाधाओं का विषय बनने वाला"),
    e("parāmaṭṭhaṃ", "parāmaṭṭhameva", "ग़लत धारणा का विषय बनने वाला"),
    e("upādāniyaṃ", "upādāniyameva", "आसक्ति का विषय बनने वाला"),
    e("saṃkilesikaṃ", "saṃkilesikameva", "क्लेशों की ओर ले जाने वाला"),
    e("abyākataṃ", "abyākatameva", "नैतिक रूप से अनिर्धारित"),
    e("anārammaṇaṃ", "anārammaṇameva", "विषय से रहित"),
    e("acetasikaṃ", "acetasikameva", "मन का सहचर न होने वाला"),
    e("cittavippayuttaṃ", "cittavippayuttameva", "मन से अलग"),
    e("nevavipākanavipākadhammadhammaṃ", "nevavipākanavipākadhammadhammameva",
      "न कर्म-फल रूपी, न कर्म-फल उत्पन्न करने वाला"),
    e("asaṃkiliṭṭhasaṃkilesikaṃ", "asaṃkiliṭṭhasaṃkilesikameva",
      "क्लेशों से मलिन न होने वाला, पर क्लेशों की ओर ले जाने वाला"),
    e("na savitakkasavicāraṃ", "na savitakkasavicārameva", "न आरंभिक विचार और सतत विचार वाला"),
    e("na avitakkavicāramattaṃ", "na avitakkavicāramattameva", "न आरंभिक विचार से रहित और केवल सतत विचार वाला"),
    e("avitakkaavicāraṃ", "avitakkaavicārameva", "आरंभिक विचार और सतत विचार दोनों से रहित"),
    e("na pītisahagataṃ", "na pītisahagatameva", "उल्लास के साथ न होने वाला"),
    e("na sukhasahagataṃ", "na sukhasahagatameva", "सुख के साथ न होने वाला"),
    e("na upekkhāsahagataṃ", "na upekkhāsahagatameva", "समभाव के साथ न होने वाला"),
    e("neva dassanena na bhāvanāya pahātabbaṃ", "neva dassanena na bhāvanāya pahātabbameva",
      "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़ा जाने वाला"),
    e("neva dassanena na bhāvanāya pahātabbahetukaṃ", "neva dassanena na bhāvanāya pahātabbahetukameva",
      "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़े जाने वाले मूलों वाला"),
    e("neva ācayagāmi na apacayagāmi", "neva ācayagāmi na apacayagāmimeva",
      "न संचय की ओर, न संचय घटाने की ओर ले जाने वाला"),
    e("nevasekkhanāsekkhaṃ", "nevasekkhanāsekkhameva", "न सीखने के चरण का, न सीखना पूरा होने के चरण का"),
    e("parittaṃ", "parittameva", "सीमित"),
    e("kāmāvacaraṃ", "kāmāvacarameva", "इंद्रिय-सुखों के लोक से संबंधित"),
    e("na rūpāvacaraṃ", "na rūpāvacarameva", "सूक्ष्म भौतिक लोक से संबंधित न होने वाला"),
    e("na arūpāvacaraṃ", "na arūpāvacarameva", "अभौतिक लोक से संबंधित न होने वाला"),
    e("pariyāpannaṃ", "pariyāpannameva", "अस्तित्व के लोकों में समाया हुआ"),
    e("no apariyāpannaṃ", "no apariyāpannameva", "अस्तित्व के लोकों में न समाया हुआ नहीं"),
    e("aniyataṃ", "aniyatameva", "अनिश्चित"),
    e("aniyyānikaṃ", "aniyyānikameva", "मुक्ति की ओर न ले जाने वाला"),
    e("uppannaṃ, chahi viññāṇehi viññeyyaṃ", "uppannaṃ chahi viññāṇehi viññeyyameva",
      "उत्पन्न होने पर छह प्रकार की चेतनाओं से जाना जा सकने वाला"),
    e("aniccaṃ", "aniccameva", "अनित्य"),
    e("jarābhibhūtaṃ", "jarābhibhūtameva", "बुढ़ापे से ग्रस्त"),
]
EKA_P1 = "Sabbaṃ rūpaṃ " + ", ".join(x[0] for x in EKA) + "."
EKA_P2 = "Sabbaṃ rūpaṃ " + ", ".join(x[1] for x in EKA) + "."
EKA_H1 = f"सारा {RUPA} " + ", ".join(x[2] for x in EKA) + " है।"
EKA_H2 = f"सारा {RUPA} " + ", ".join(x[3] for x in EKA) + " है।"

# ---------------------------------------------------------------- fixed lines
NUM = {"Ekavidhena": "एक", "Duvidhena": "दो", "Tividhena": "तीन", "Catubbidhena": "चार", "Pañcavidhena": "पाँच",
       "Chabbidhena": "छह", "Sattavidhena": "सात", "Aṭṭhavidhena": "आठ", "Navavidhena": "नौ", "Dasavidhena": "दस",
       "Ekādasavidhena": "ग्यारह"}
L = {}
for k, h in NUM.items():
    L[f"{k} rūpasaṅgaho –"] = f"{h} प्रकार से {RUPA} का वर्गीकरण –"
    low = k[0].lower() + k[1:]
    L[f"Evaṃ {low} rūpasaṅgaho."] = f"इस तरह {h} प्रकार से {RUPA} का वर्गीकरण हुआ।"

GROUP = {"Ekakaṃ": "एक-एक", "Dukaṃ": "दो-दो", "Tikaṃ": "तीन-तीन", "Catukkaṃ": "चार-चार", "Pañcakaṃ": "पाँच-पाँच",
         "Chakkaṃ": "छह-छह", "Sattakaṃ": "सात-सात", "Aṭṭhakaṃ": "आठ-आठ", "Navakaṃ": "नौ-नौ", "Dasakaṃ": "दस-दस",
         "Ekādasakaṃ": "ग्यारह-ग्यारह"}
H = {"Rūpakaṇḍaṃ": f"{RUPA} का अध्याय", "Uddeso": "रूपरेखा", "Mātikā": "मूल सूची",
     "Rūpavibhatti": f"{RUPA} का वर्गीकरण", "Ekakaniddeso": "एक-एक के वर्गीकरणों की व्याख्या"}
for k, h in GROUP.items():
    H[k] = f"{h} के वर्गीकरण"
    L[k + "."] = f"{h} के वर्गीकरण।"
L["Mātikā."] = "मूल सूची।"
L["Ekakaniddeso."] = "एक-एक के वर्गीकरणों की व्याख्या।"

ABY_Q = "नैतिक रूप से अनिर्धारित परिघटनाएँ कौन-सी हैं?"
ABY_A = "ये नैतिक रूप से अनिर्धारित परिघटनाएँ हैं।"
L["Katame dhammā abyākatā? Kusalākusalānaṃ dhammānaṃ vipākā kāmāvacarā rūpāvacarā arūpāvacarā apariyāpannā vedanākkhandho saññākkhandho saṅkhārakkhandho viññāṇakkhandho, ye ca dhammā kiriyā neva kusalā nākusalā na ca kammavipākā, sabbañca rūpaṃ, asaṅkhatā ca dhātu – ime dhammā abyākatā."] = (
    f"{ABY_Q} हितकर और हानिकर परिघटनाओं के कर्म-फल रूपी, इंद्रिय-सुखों के लोक से संबंधित, सूक्ष्म भौतिक लोक से संबंधित, "
    "अभौतिक लोक से संबंधित और अस्तित्व के लोकों में न समाए हुए अनुभूति का समूह, पहचान का समूह, मानसिक रचनाओं का समूह और चेतना का समूह; "
    f"और जो परिघटनाएँ केवल क्रिया रूपी हैं, न हितकर, न हानिकर, और न ही कर्म-फल; और सारा {RUPA}; और अनिर्मित तत्व – {ABY_A}")
L["Tattha katamaṃ sabbaṃ rūpaṃ? Cattāro ca mahābhūtā, catunnañca mahābhūtānaṃ upādāya rūpaṃ – idaṃ vuccati sabbaṃ rūpaṃ. " + EKA_P1] = (
    f"यहाँ सारा {RUPA} क्या है? चार महाभूत और चार महाभूतों से व्युत्पन्न {RUPA} – इसे सारा {RUPA} कहा जाता है। {EKA_H1}")
L[EKA_P2] = EKA_H2

V = "से जाना जा सकने वाला " + RUPA
K5 = [f"{h} {V}" for _, h in SENSES]
K5P = "Cakkhuviññeyyaṃ rūpaṃ, sotaviññeyyaṃ rūpaṃ, ghānaviññeyyaṃ rūpaṃ, jivhāviññeyyaṃ rūpaṃ, kāyaviññeyyaṃ rūpaṃ"
MD = f"मन के तत्व {V}"
MV = f"मन की चेतना के तत्व {V}"
L["Diṭṭhaṃ sutaṃ mutaṃ viññātaṃ rūpaṃ."] = f"देखा हुआ, सुना हुआ, अनुभव किया हुआ और जाना हुआ {RUPA}।"
L["Pathavīdhātu, āpodhātu, tejodhātu, vāyodhātu, yañca rūpaṃ upādā."] = (
    f"पृथ्वी तत्व, जल तत्व, अग्नि तत्व, वायु तत्व और जो भी {RUPA} व्युत्पन्न है।")
L[K5P + ", manoviññeyyaṃ rūpaṃ."] = ", ".join(K5) + f" और मन {V}।"
L[K5P + ", manodhātuviññeyyaṃ rūpaṃ, manoviññāṇadhātuviññeyyaṃ rūpaṃ."] = ", ".join(K5) + f", {MD} और {MV}।"
L[K5P + ", atthi sukhasamphassaṃ, atthi dukkhasamphassaṃ, manodhātuviññeyyaṃ rūpaṃ, manoviññāṇadhātuviññeyyaṃ rūpaṃ."] = (
    ", ".join(K5) + f", जिसमें कुछ सुखद संपर्क वाला है, कुछ दुःखद संपर्क वाला है, {MD} और {MV}।")
IND8 = ", ".join(IN.values())
IND8P = "Cakkhundriyaṃ, sotindriyaṃ, ghānindriyaṃ, jivhindriyaṃ kāyindriyaṃ, itthindriyaṃ, purisindriyaṃ, jīvitindriyaṃ"
L[IND8P + ", yañca rūpaṃ na indriyaṃ."] = f"{IND8} और जो भी {RUPA} क्षमता नहीं है।"
L[IND8P + ", na indriyaṃ rūpaṃ atthi sappaṭighaṃ, atthi appaṭighaṃ."] = (
    f"{IND8} और जो {RUPA} क्षमता नहीं है, उसमें कुछ टकराव वाला है, कुछ टकराव से रहित है।")
L["Cakkhāyatanaṃ, sotāyatanaṃ, ghānāyatanaṃ, jivhāyatanaṃ, kāyāyatanaṃ, rūpāyatanaṃ, saddāyatanaṃ, gandhāyatanaṃ, rasāyatanaṃ, phoṭṭhabbāyatanaṃ, yañca rūpaṃ anidassanaappaṭighaṃ [anidassanaṃ appaṭighaṃ (sī. syā.)] dhammāyatanapariyāpannaṃ."] = (
    ", ".join(f"{h} का इंद्रिय-क्षेत्र" for h in AY.values())
    + f" और जो भी {RUPA} दिखाई न देने वाला और टकराव से रहित [वर्तनी-भेद (Sī., Syā.): anidassanaṃ appaṭighaṃ] है और मन के विषयों के इंद्रिय-क्षेत्र में समाया हुआ है।")


# ---------------------------------------------------------------- build
def tr(body):
    if body in L:
        return L[body]
    if body.startswith(("Atthi rūpaṃ ", "Yaṃ taṃ rūpaṃ ")):
        return frame_line(body)
    raise KeyError(body)


out, pairs = [], []
for raw in SRC.read_text(encoding="utf-8-sig").splitlines():
    if not raw.strip():
        if out and out[-1] != "":
            out.append("")
        continue
    m = ID.search(raw)
    body = ID.sub("", raw).rstrip()
    tail = f" ^{m.group(1)}" if m else ""
    hm = re.match(r"(#+) (.*)$", body)
    if hm:
        hi = f"{hm.group(1)} {H[hm.group(2)]}"
    else:
        hi = tr(body)
    pairs.append((body, hi))
    out.append(hi + tail)
while out and out[-1] == "":
    out.pop()
OUT.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")

# ---------------------------------------------------------------- notes
n = ["# notes-3-01: 3-01-rupakandam (pi-1, Hindi rails, plain)", "",
     "## New recurring formulas", "",
     f"Atthi rūpaṃ X, atthi rūpaṃ Y. = कुछ {RUPA} X है, कुछ {RUPA} Y है।",
     f"Atthi rūpaṃ rūpassa Q, atthi rūpaṃ rūpassa na Q. = कुछ {RUPA} ऐसा है जो {RUPA} का/की Q है, कुछ {RUPA} ऐसा है जो {RUPA} का/की Q नहीं है।",
     f"Yaṃ taṃ rūpaṃ X, taṃ Z. = जो {RUPA} X है, वह Z है।",
     f"Yaṃ taṃ rūpaṃ X, taṃ atthi Y, atthi W. = जो {RUPA} X है, उसमें कुछ Y है, कुछ W है।",
     f"Yaṃ taṃ rūpaṃ X, taṃ atthi rūpassa Q, atthi rūpassa na Q. = जो {RUPA} X है, उसमें कुछ ऐसा है जो {RUPA} का/की Q है, कुछ ऐसा है जो {RUPA} का/की Q नहीं है।",
     f"Evaṃ Nvidhena rūpasaṅgaho. = इस तरह N प्रकार से {RUPA} का वर्गीकरण हुआ।",
     f"Nvidhena rūpasaṅgaho – = N प्रकार से {RUPA} का वर्गीकरण –",
     "Ekakaṃ / Dukaṃ / Tikaṃ … Ekādasakaṃ (heading) = एक-एक / दो-दो / तीन-तीन … ग्यारह-ग्यारह के वर्गीकरण; closing line adds «।»",
     "Ekakaniddeso = एक-एक के वर्गीकरणों की व्याख्या (so Dukaniddeso = दो-दो के वर्गीकरणों की व्याख्या)",
     "Predicates: X-वाला items negate as in the matrix (न होने वाला, न करने वाला); noun and participle items negate with «नहीं» (व्युत्पन्न नहीं, क्षमता नहीं).",
     "", "## Terms the termbase lacks, as built here", "",
     "vatthu = आधार (samphassassa/viññāṇassa vatthu: आँख के संपर्क का आधार; na vatthu: … आधार नहीं)",
     "dūre = दूर; santike = निकट",
     "diṭṭhaṃ = देखा हुआ",
     "evaṃ (closing line) = इस तरह",
     "nārammaṇaṃ (genitive + nārammaṇaṃ) = … का विषय नहीं",
     "", "## List items (Pāli = Hindi)", "", "### Items of the matrix of matter", ""]
n += [f"{k} = {v}" for k, v in P.items()]
n += ["", "### Ekaka list (1-584; 1-594 adds «ही» to each item)", ""]
n += [f"{x[0]} = {x[2]}" for x in EKA]
n += ["", "### Every line of the chapter (Pāli = Hindi)", ""]
n += [f"{a} = {b}" for a, b in pairs]
n += ["", "## Decisions and source notes", "",
      "- 1-583 Kusalākusalānaṃ dhammānaṃ vipākā = हितकर और हानिकर परिघटनाओं के कर्म-फल रूपी (dhammānaṃ stays, so the bare class form is used).",
      "- rūpaṃ inside the ekaka list = भौतिक (DhsA 1-1547: it answers the matrix pair rūpino / arūpino), variant rūpiyaṃ = पाठभेद.",
      "- uppannaṃ, chahi viññāṇehi viññeyyaṃ: one item in both places (DhsA: paccuppannarūpameva … chahi veditabbaṃ). 1-594 has no comma and no -eva on uppannaṃ; 1-584's comma is treated as edition punctuation. Hindi: उत्पन्न होने पर छह प्रकार की चेतनाओं से जाना जा सकने वाला.",
      "- no apariyāpannaṃ = अस्तित्व के लोकों में न समाया हुआ नहीं (double negative kept).",
      "- na avitakkavicāramattaṃ in the list: «और» for the matrix comma, so that «केवल सतत विचार वाला» is not read as a separate item.",
      "- Termbase terms are masculine here because they agree with भौतिक रूप (समाया हुआ, समाए हुए, जाना जा सकने वाला).",
      "- apariyāpannaṃ in the termbase carries «परिघटना»; here it qualifies matter, so the noun is left out.",
      "- Source slips: line 'taṃ atthi sappaṭighaṃ atthi appaṭighaṃ' (1-586) lacks a comma; 'jivhindriyaṃ kāyindriyaṃ' (1-591, 1-592) lacks a comma; 'cetanāya …pe…' (U1) has a stray space. Hindi normalises all three.",
      ""]
NOTES.write_text("\n".join(n), encoding="utf-8", newline="\n")
print("lines", len(pairs))
