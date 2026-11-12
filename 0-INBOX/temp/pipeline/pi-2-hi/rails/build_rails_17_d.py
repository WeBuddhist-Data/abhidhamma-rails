"""Chapter 17, part D: the wanderings of craving and the 62 views (^2-973 … ^2-977)."""
from build_rails_17_k import *  # noqa: F401,F403
from build_rails_17_c import NS8, AS8

L = []
a = L.append

CLASSES = ["क्षत्रिय", "ब्राह्मण", "वैश्य", "शूद्र", "गृहस्थ", "गृहत्यागी", "देवता", "मनुष्य", "भौतिक रूप वाला", "अभौतिक",
           "पहचान रखने वाला", "पहचान से रहित", "न पहचान वाला, न पहचान से रहित"]


def subj(v, imina):
    return ("काश, " if v == "apa" else "") + ("इसके कारण " if imina else "") + "मैं"


def pred(v, x, neg=False):
    x = f"{x} " if x else ""
    if v == "asmi":
        return f"{x}{'नहीं ' if neg else ''}हूँ"
    if v == "bhav":
        return f"{x}{'नहीं ' if neg else ''}होऊँगा"
    if v == "siy":
        return f"{x}नहीं हो सकता" if neg else f"{x}हो सकता हूँ"
    return f"{x}{'न ' if neg else ''}होता"  # apa


KIND_WORD = {"plain": "", "ittha": "ऐसा", "eva": "वैसा ही", "anna": "अलग तरह का"}


def name(v, kind, imina=False):  # the quoted claim, e.g. “मैं ऐसा हूँ”
    return f"“{subj(v, imina)} {pred(v, KIND_WORD[kind])}”"


def bhava(v, kind, imina=False):  # … ऐसा भाव होता है
    return f"{name(v, kind, imina)} ऐसा भाव होता है"


ORDER = [("asmi", "plain"), ("asmi", "ittha"), ("asmi", "eva"), ("asmi", "anna"),
         ("bhav", "plain"), ("bhav", "ittha"), ("bhav", "eva"), ("bhav", "anna"),
         ("asas", None), ("sata", None),
         ("siy", "plain"), ("siy", "ittha"), ("siy", "eva"), ("siy", "anna"),
         ("apa", "plain"), ("apa", "ittha"), ("apa", "eva"), ("apa", "anna")]


def nm(v, kind, imina=False):
    if v == "asas":
        return f"“{subj('asmi', imina)} शाश्वत हूँ”"
    if v == "sata":
        return f"“{subj('asmi', imina)} नश्वर हूँ”"
    return name(v, kind, imina)


def eighteen(imina):
    return ", ".join(f"{nm(v, k, imina)} ऐसा भाव होता है" for v, k in ORDER)


def how(v, kind, imina):
    return f"{nm(v, kind, imina)} ऐसा भाव कैसे होता है?"


def thus(v, kind, imina):
    return f"इस तरह {nm(v, kind, imina)} ऐसा भाव होता है।"


AGG = "भौतिक रूप… अनुभूति… पहचान… मानसिक रचनाओं… चेतना को लेकर"


def root_line(num, v, imina, var=""):
    sep = "अलग करके" if imina else "अलग किए बिना"
    s = subj(v, imina)
    claim = f"“{s} {pred(v, '')}”"
    pre = f"({num}) " if num else ""
    return (f"{pre}{how(v, 'plain', imina)} किसी परिघटना को {sep}{var}, {AGG} {claim} ऐसी चाह पाता है, {claim} "
            f"ऐसा अहंकार पाता है, {claim} ऐसी दृष्टि पाता है। उसके होने पर ये मानसिक फैलाव होते हैं – "
            f"{name(v, 'ittha', imina)}, या {name(v, 'eva', imina)}, या {name(v, 'anna', imina)}।")


def ittha_line(num, v, imina, pe_from=None):
    items = [f"“{subj(v, imina)} {pred(v, c)}”" for c in CLASSES]
    if pe_from is None:
        body = ", या ".join(items)
    else:  # Iminā khattiyo bhavissanti vā…pe… iminā arūpī …
        body = items[0] + ", या… " + ", या ".join(items[pe_from:])
    return f"({num}) {how(v, 'ittha', imina)} {body} – {thus(v, 'ittha', imina)}"


def compare(c, v, imina, neg):
    wish = "काश, " if v == "apa" else ""
    i = "इसके कारण " if imina else ""
    if neg:
        return f"“जैसे वह {c} है, {wish}वैसा {i}मैं {pred(v, c, True)}”"
    return f"“जैसे वह {c} है, {wish}वैसे ही {i}मैं {pred(v, c)}”"


def eva_line(num, v, imina, neg, full=False, var="", closing_kind=None):
    kind = "anna" if neg else "eva"
    items = [compare(c, v, imina, neg) for c in CLASSES]
    body = ", या ".join(items) if full else f"{items[0]}, या {items[1]}… {items[-1]}"
    ck = closing_kind or kind
    return (f"({num}) {how(v, kind, imina)} दूसरे व्यक्ति{var} से तुलना करके, {body} – "
            f"{thus(v, ck, imina) if ck != 'plain' else thus(v, 'plain', imina)}")


def fixed_line(num, which, imina, var=""):
    sep = "अलग करके" if imina else "अलग किए बिना"
    i = "इसके कारण " if imina else ""
    words = ("“{i}मैं नित्य हूँ, स्थिर हूँ, शाश्वत हूँ, न बदलने के स्वभाव वाला हूँ”" if which == "asas" else
             "“{i}मैं नष्ट हो जाऊँगा, विनष्ट हो जाऊँगा, नहीं रहूँगा”").format(i=i)
    return f"({num}) {how(which, None, imina)} किसी परिघटना को {sep}{var}, {AGG} {words} – {thus(which, None, imina)}"


def block(imina):
    out = []
    var1 = "" if imina else " [वर्तनी-भेद (Sī., Ka.): anavakārī]"
    out.append(root_line(None if not imina else 1, "asmi", imina, var1))
    out.append(ittha_line(2, "asmi", imina))
    out.append(eva_line(3, "asmi", imina, False, full=not imina,
                        var="" if imina else " [वर्तनी-भेद (Syā.): paraṃ puggalaṃ]"))
    out.append(eva_line(4, "asmi", imina, True, full=not imina))
    out.append(root_line(5, "bhav", imina))
    out.append(ittha_line(6, "bhav", imina, pe_from=9 if imina else None))
    # source: (7) of the internal set closes with "evaṃ bhavissanti hoti" (one would expect evaṃ evaṃ …)
    out.append(eva_line(7, "bhav", imina, False, closing_kind=None if imina else "plain"))
    out.append(eva_line(8, "bhav", imina, True))
    out.append(fixed_line(9, "asas", imina, " [वर्तनी-भेद (Sī.): avakārī]" if imina else ""))
    out.append(fixed_line(10, "sata", imina))
    out.append(root_line(11, "siy", imina))
    out.append(ittha_line(12, "siy", imina))
    out.append(eva_line(13, "siy", imina, False))
    out.append(eva_line(14, "siy", imina, True))
    out.append(root_line(15, "apa", imina))
    out.append(ittha_line(16, "apa", imina))
    out.append(eva_line(17, "apa", imina, False))
    out.append(eva_line(18, "apa", imina, True))
    return out


INT = "आंतरिक को आधार बनाकर तृष्णा के अठारह विचरण"
EXT = "बाह्य को आधार बनाकर तृष्णा के अठारह विचरण"

a("#### तृष्णा के विचरणों की व्याख्या")
a("##### (1) आंतरिक को आधार बनाकर")
a(f"यहाँ {INT} कौन-से हैं? {eighteen(False)}।")
b = block(False)
b[0] = b[0]  # the first line has no "(1)" in the Pāli
b = b[:15] + [b[15] + " " + b[16]] + b[17:]  # (16) and (17) share one line in the Pāli
L += b
a(f"ये {INT} हैं।")

a("##### (2) बाह्य को आधार बनाकर")
a(f"यहाँ {EXT} कौन-से हैं? {eighteen(True)}।")
L += block(True)
a(f"ये {EXT} हैं।")
a(f"इस तरह ये {INT}, ये {EXT}, उस सबको एक साथ इकट्ठा करके, संक्षेप में समेटकर तृष्णा के छत्तीस विचरण होते हैं। "
  "इस तरह इस प्रकार के तृष्णा के छत्तीस विचरण अतीत के, छत्तीस विचरण भविष्य के, छत्तीस विचरण वर्तमान के, उस सबको एक "
  "साथ इकट्ठा करके, संक्षेप में समेटकर तृष्णा के एक सौ आठ विचरण होते हैं।")

V62 = "वे बासठ ग़लत दृष्टियाँ, जो भगवान ने ब्रह्मजाल व्याख्यान में कही हैं"
a(f"यहाँ {V62.replace('वे बासठ ग़लत दृष्टियाँ,', 'वे बासठ ग़लत दृष्टियाँ कौन-सी हैं,')}? शाश्वतता के चार मत, आंशिक "
  f"शाश्वतता के चार मत, लोक को सीमित और असीम मानने वाले चार मत, गोलमोल जवाब देने के चार मत, संयोग से उत्पत्ति के दो मत, आत्मा को पहचान रखने वाली "
  f"बताने वाले सोलह मत, {AS8}, {NS8}, विनाश के सात मत, इसी जीवन में निर्वाण के पाँच मत – ये {V62}।")
a(f"{CH_TITLE} {DONE}।")

LINES = L
