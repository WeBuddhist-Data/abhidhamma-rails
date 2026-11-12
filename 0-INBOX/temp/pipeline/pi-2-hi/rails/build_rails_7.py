"""Hindi rails builder: pi-2 chapter 7, Satipaṭṭhānavibhaṅga.

usage: python -I -X utf8 build_rails_7.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import build_rails_5_7_10_11_common as C  # noqa: E402

NAME = "7-satipatthanavibhango.md"
B = C.BOJ
INT, EXT, BOTH = "स्वयं से संबंधित", "दूसरों से संबंधित", "स्वयं और दूसरों दोनों से संबंधित"
SP = "सजगता का आधार"
FOUR = "सजगता के चार आधार"
an = C.anupassi


def how(f, q=""):
    return f"भिक्षु {an(f, q)} किस प्रकार रहता है?"


def evam(f, q=""):
    return f"इस प्रकार भिक्षु {C.ATAPI}, {an(f, q)} रहता है।"


SIGN = ("वह उस चिह्न का निरंतर सेवन करता है, उसका अभ्यास करता है, उसे बार-बार करता है और उसे सुनिश्चित रूप से "
        "भली-भाँति निर्धारित करता है।")  # So taṃ nimittaṃ āsevati bhāveti bahulīkaroti svāvatthitaṃ vavatthapeti.


def sign2(target):
    """So taṃ nimittaṃ āsevitvā … vavatthapetvā <target> cittaṃ upasaṃharati."""
    return (f"उस चिह्न का निरंतर सेवन करके, उसका अभ्यास करके, उसे बार-बार करके और उसे सुनिश्चित रूप से भली-भाँति "
            f"निर्धारित करके वह {target} पर मन को ले जाता है।")


def parts(v=False):
    v1 = " [वर्तनी-भेद (Sī.): nahāru]" if v else ""
    v2 = " [वर्तनी-भेद (Sī.): aṭṭhimiñjā]" if v else ""
    return (f"सिर के बाल, रोएँ, नाखून, दाँत, त्वचा, मांस, नसें{v1}, हड्डियाँ, हड्डियों की मज्जा{v2}, गुर्दे, हृदय, यकृत, "
            "झिल्ली, तिल्ली, फेफड़े, आँतें, आँतों की मेखला, पेट का भोजन, मल, पित्त, कफ, पीब, खून, पसीना, चर्बी, आँसू, "
            "वसा, लार, नाक का मैल, जोड़ों का तरल और मूत्र")


def review(q):
    return (f"यहाँ भिक्षु पैरों के तलवों से ऊपर और सिर के बालों के सिरे से नीचे, त्वचा से घिरे और अनेक प्रकार की "
            f"अशुद्धि से भरे {q} शरीर को जाँचता है")


def endow(x, pe=False):
    """X-ena upeto hoti samupeto upāgato samupāgato upapanno sampanno samannāgato."""
    if pe:
        return f"वह {x} से सुसज्जित होता है… इससे युक्त होता है।"
    return (f"वह {x} से सुसज्जित होता है, भली-भाँति सुसज्जित होता है, इस तक पहुँचा हुआ होता है, इस तक भली-भाँति "
            "पहुँचा हुआ होता है, इसे पाया हुआ होता है, इससे संपन्न होता है, इससे युक्त होता है।")


VINITA = ("इस प्रकार यह लालच और यह उदासी इस लोक में दूर कर दिए गए, पूरी तरह दूर कर दिए गए, शांत हो चुके, थम चुके, "
          "पूरी तरह शांत हो चुके, अस्त हो चुके, पूरी तरह अस्त हो चुके, नष्ट हो चुके, पूरी तरह नष्ट हो चुके, सूख चुके, "
          "पूरी तरह सूख चुके और पूरी तरह समाप्त हो चुके होते हैं।")
VINEYYA_Q = "“लोक में लालच और उदासी को दूर करके”"
HEADS_PE = "“अवलोकन करते हुए”… “रहता है”… “उद्यमी”… “स्पष्ट समझ रखते हुए”… “सजग”… " + VINEYYA_Q + "।"


def vineyya(head, loka, dash_after_loka=False):
    five = "आसक्ति के पाँचों समूह भी लोक हैं"
    mid = f"{five} – यहाँ लालच क्या है?" if dash_after_loka else f"{five}। यह “लोक” कहा जाता है। यहाँ लालच क्या है?"
    return (f"{head} यहाँ लोक क्या है? {loka} {mid} जो {C.RAGA_PE} है – यह “लालच” कहा जाता है। "
            f"यहाँ उदासी क्या है? जो {C.DOMANASSA} है – यह “उदासी” कही जाती है। {VINITA} "
            f"इसीलिए {VINEYYA_Q} कहा जाता है।")


FEEL = [("सुखद अनुभूति", False), ("दुःखद अनुभूति", False), ("न दुःखद, न सुखद अनुभूति", False)]
for adj in ("सुखद", "दुःखद", "न दुःखद, न सुखद"):
    FEEL += [(f"सांसारिक भोग से जुड़ी {adj} अनुभूति", True), (f"सांसारिक भोग से रहित {adj} अनुभूति", True)]
FEEL = FEEL[:3] + [FEEL[3], FEEL[4], FEEL[5], FEEL[6], FEEL[7], FEEL[8]]

CITTA = [("राग-युक्त", "राग-युक्त"), ("राग से मुक्त", "राग से मुक्त"), ("द्वेष-युक्त", "द्वेष-युक्त"),
         ("द्वेष से मुक्त", "द्वेष से मुक्त"), ("मोह-युक्त", "मोह-युक्त"), ("मोह से मुक्त", "मोह से मुक्त"),
         ("सिमटे हुए", "सिमटा हुआ"), ("बिखरे हुए", "बिखरा हुआ"), ("उन्नत", "उन्नत"),
         ("उन्नत न होने वाले", "उन्नत नहीं"), ("सर्वोच्च न होने वाले", "सर्वोच्च नहीं"), ("सर्वोच्च", "सर्वोच्च"),
         ("एकाग्र", "एकाग्र"), ("एकाग्रता से रहित", "एकाग्रता से रहित"), ("मुक्त", "मुक्त"), ("अमुक्त", "अमुक्त")]

CTX = {"int": ("स्वयं में {} होने पर", "स्वयं में {} न होने पर", "स्वयं मुझमें {} है", "स्वयं मुझमें {} नहीं है"),
       "ext": ("उसमें {} होने पर", "उसमें {} न होने पर", "उसमें {} है", "उसमें {} नहीं है"),
       "both": ("{} होने पर", "{} न होने पर", "{} है", "{} नहीं है")}


def present(x, ctx, var=""):
    v = f" {var}" if var else ""
    return CTX[ctx][0].format(x + v)


def hindrance_full(x, g, ctx):
    p, n, qp, qn = CTX[ctx]
    if g == "f":
        a, b, c = (f"उत्पन्न न हुई {x} उत्पन्न होती है", f"उत्पन्न हो चुकी {x} को छोड़ दिया जाता है",
                   f"छोड़ी जा चुकी {x} भविष्य में उत्पन्न नहीं होती")
    else:
        a, b, c = (f"उत्पन्न न हुआ {x} उत्पन्न होता है", f"उत्पन्न हो चुके {x} को छोड़ दिया जाता है",
                   f"छोड़ा जा चुका {x} भविष्य में उत्पन्न नहीं होता")
    return (f"{p.format(x)} जानता है कि “{qp.format(x)}”, {n.format(x)} जानता है कि “{qn.format(x)}”, "
            f"जिस तरह {a}, उसे भी जानता है, जिस तरह {b}, उसे भी जानता है, जिस तरह {c}, उसे भी जानता है")


def factor_full(k, ctx):
    p, n, qp, qn = CTX[ctx]
    x = B[k]
    return (f"{p.format(x)} जानता है कि “{qp.format(x)}”, {n.format(x)} जानता है कि “{qn.format(x)}”, "
            f"जिस तरह उत्पन्न न हुआ {x} उत्पन्न होता है, उसे भी जानता है, जिस तरह उत्पन्न हो चुके "
            f"{C.boj_obl(k)} का अभ्यास परिपूर्ण होता है, उसे भी जानता है")


KAMA, VIC = "इंद्रिय-सुखों की चाह", "संशय"


def hindrances(ctx, thina_var=""):
    mid = "… ".join([present("दुर्भावना", ctx), present("आलस्य और तंद्रा", ctx, thina_var),
                     present("बेचैनी और पछतावा", ctx)])
    return (f"यहाँ भिक्षु {hindrance_full(KAMA, 'f', ctx)}। {mid}… {hindrance_full(VIC, 'm', ctx)}।")


def factors(ctx, join, viriya_var=""):
    mid = "… ".join(present(B[k], ctx, viriya_var if k == "viriya" else "")
                    for k in ["dhammavicaya", "viriya", "piti", "passaddhi", "samadhi"])
    first = factor_full("sati", ctx)
    return f"{first}{join}{mid}… {factor_full('upekkha', ctx)}।"


def lok_sp(kind, f=None, quote=True):
    an_part = f"और {an(f)} रहता है, " if f else ""
    sp = f"“{SP}”" if quote else SP
    return C.lok(kind, f"{an_part}उस समय जो {C.SATI_SHORT}, {B['sati']}, {C.MAGGA3} है – यह {sp} कहा जाता है। "
                       f"{C.remaining('सजगता के आधार')}।")


def build():
    P = C.pali_segs(NAME)
    h = {}
    h["2-7-0"] = ["### सजगता के आधारों का विश्लेषण"]
    h["2-7-1-0"] = [f"#### {C.SUTTANTA_BH}"]
    groups = [f"{C.ATAPI}, {an(f, INT)} रहता है, {an(f, EXT)} रहता है और {an(f, BOTH)} रहता है" for f in C.FIELD]
    h["2-355"] = [f"{FOUR} – यहाँ भिक्षु " + "; ".join(groups) + "।"]
    # ----- body
    h["2-7-1-1-0"] = ["##### शरीर के अवलोकन की व्याख्या"]
    h["2-356"] = [
        f"{how('kaya', INT)} {review(INT)} – “इस शरीर में {parts(True)} हैं”। {SIGN} {sign2(EXT + ' शरीर')}",
        f"{how('kaya', EXT)} {review(EXT)} – “उसके शरीर में {parts()} हैं”। {SIGN} {sign2(BOTH + ' शरीर')}",
        f"{how('kaya', BOTH)} {review(BOTH)} – “इस शरीर में {parts()} हैं”। {evam('kaya', BOTH)}",
    ]
    anup = lambda q=True: (f"“अवलोकन करते हुए”। यहाँ अवलोकन क्या है? जो {C.PANNA_PE} है – यह "
                           + ("“अवलोकन”" if q else "अवलोकन") + f" कहा जाता है। {endow('इस अवलोकन')} "
                           "इसीलिए “अवलोकन करते हुए” कहा जाता है।")
    vihar = ("“रहता है”। वह चलता-फिरता है, आचरण करता है, स्वयं को बनाए रखता है, निभाता है, जीवन चलाता है, "
             "विचरता है, रहता है। इसीलिए “रहता है” कहा जाता है।")
    atapi = lambda var, pe: (f"“उद्यमी”। यहाँ उद्यमशीलता{var} क्या है? जो {C.VIRIYA_PE} है – यह “उद्यमशीलता” कही जाती है। "
                             f"{endow('इस उद्यमशीलता', pe)} इसीलिए “उद्यमी” कहा जाता है।")
    sampaj = lambda pe: (f"“स्पष्ट समझ रखते हुए”। यहाँ स्पष्ट समझ क्या है? जो {C.PANNA_PE} है – यह “स्पष्ट समझ” कही जाती है। "
                         f"{endow('इस स्पष्ट समझ', pe)} इसीलिए “स्पष्ट समझ रखते हुए” कहा जाता है।")
    satima = lambda pe: (f"“सजग”। यहाँ सजगता क्या है? जो {C.SATI_PE} है – यह “सजगता” कही जाती है। "
                         f"{endow('इस सजगता', pe)} इसीलिए “सजग” कहा जाता है।")
    h["2-357"] = [anup()]
    h["2-358"] = [vihar]
    h["2-359"] = [atapi(" [पाठभेद (सभी संस्करणों में): katamaṃ ātāpaṃ]", False)]
    h["2-360"] = [sampaj(False)]
    h["2-361"] = [satima(False)]
    h["2-362"] = [vineyya(VINEYYA_Q + "।", "वही शरीर लोक है।"), "शरीर के अवलोकन की व्याख्या।"]
    # ----- feelings
    h["2-7-1-2-0"] = ["##### अनुभूतियों के अवलोकन की व्याख्या"]
    l1 = ", ".join(f"{x} का अनुभव करते हुए जानता है कि “मैं {x} का अनुभव कर रहा हूँ”" for x, _ in FEEL)
    l2 = ", ".join(f"{x} का अनुभव करने वाले के बारे में जानता है कि “वह {x} का अनुभव कर रहा है”" for x, _ in FEEL)
    l3 = ", ".join(f"{x} को “{x}” के रूप में जानता है" for x, _ in FEEL)
    h["2-363"] = [
        f"{how('vedana', INT)} यहाँ भिक्षु {l1}। {SIGN} {sign2(EXT + ' अनुभूतियों')}",
        f"{how('vedana', EXT)} यहाँ भिक्षु {l2}। {SIGN} {sign2(BOTH + ' अनुभूतियों')}",
        f"{how('vedana', BOTH)} यहाँ भिक्षु {l3}। {evam('vedana', BOTH)}",
    ]
    h["2-364"] = [vineyya(HEADS_PE, "वही अनुभूति लोक है।"), "अनुभूतियों के अवलोकन की व्याख्या।"]
    # ----- mind
    h["2-7-1-3-0"] = ["##### मन के अवलोकन की व्याख्या"]
    c1 = ", ".join(f"{a} मन को जानता है कि “मेरा मन {p} है”" for a, p in CITTA)
    c2 = ", ".join(f"उसके {a} मन को जानता है कि “उसका मन {p} है”" for a, p in CITTA)
    c3 = ", ".join(f"{a} मन को जानता है कि “मन {p} है”" for a, p in CITTA)
    h["2-365"] = [
        f"{how('citta', INT)} यहाँ भिक्षु {c1}। {SIGN} {sign2(EXT + ' मन')}",
        f"{how('citta', EXT)} यहाँ भिक्षु {c2}। {SIGN} {sign2(BOTH + ' मन')}",
        f"{how('citta', BOTH)} यहाँ भिक्षु {c3}। {evam('citta', BOTH)}",
    ]
    h["2-366"] = [vineyya(HEADS_PE, "वही मन लोक है।", dash_after_loka=True), "मन के अवलोकन की व्याख्या।"]
    # ----- phenomena
    h["2-7-1-4-0"] = ["##### परिघटनाओं के अवलोकन की व्याख्या"]
    th_var = "[वर्तनी-भेद (Sī., Syā.): thīnamiddhaṃ]"
    vi_var = "[वर्तनी-भेद (Sī., Syā.): viriyasambojjhaṅgaṃ]"
    h["2-367"] = [
        f"{how('dhamma', INT)} {hindrances('int', th_var)}",
        f"{factors('int', ', ', vi_var)[:-1]}। {SIGN} {sign2(EXT + ' परिघटनाओं')}",
        f"{how('dhamma', EXT)} {hindrances('ext')}",
        f"{factors('ext', '। ')[:-1]}। {SIGN} {sign2(BOTH + ' परिघटनाओं')}",
        f"{how('dhamma', BOTH)} {hindrances('both')}",
        f"{factors('both', '। ')[:-1]}। {evam('dhamma', BOTH)}",
    ]
    h["2-368"] = [anup(False)]
    h["2-369"] = [vihar]
    h["2-370"] = [atapi("", True)]
    h["2-371"] = [sampaj(True)]
    h["2-372"] = [satima(True)]
    h["2-373"] = [vineyya(VINEYYA_Q + "।", "वे ही परिघटनाएँ लोक हैं।"), "परिघटनाओं के अवलोकन की व्याख्या।",
                  f"{C.SUTTANTA_BH}।"]
    # ----- Abhidhammabhājanīya
    h["2-7-2-0"] = [f"#### {C.ABHI_BH}"]
    four_plain = f"{FOUR} – यहाँ भिक्षु " + ", ".join(f"{an(f)} रहता है" for f in C.FIELD) + "।"
    h["2-374"] = [four_plain]
    fl = list(C.FIELD)
    for i, sid in enumerate(["2-375", "2-376", "2-377", "2-378"]):
        h[sid] = [f"{how(fl[i])} " + lok_sp("k", fl[i], quote=(sid != "2-376"))]
    h["2-379"] = [f"यहाँ {SP} क्या है? " + lok_sp("k", "dhamma")]
    h["2-380"] = [four_plain]
    for i, sid in enumerate(["2-381", "2-382", "2-383", "2-384"]):
        h[sid] = [f"{how(fl[i])} " + lok_sp("v", fl[i])]
    h["2-385"] = [f"यहाँ {SP} क्या है? " + lok_sp("v"), f"{C.ABHI_BH}।"]
    # ----- Pañhāpucchaka
    h["2-7-3-0"] = [f"#### {C.PANHA}"]
    h["2-386"] = [f"{FOUR} – यहाँ भिक्षु " + "; ".join(f"{C.ATAPI}, {an(f)} रहता है" for f in C.FIELD) + "।"]
    h["2-387"] = ["सजगता के चार आधारों में से कितने हितकर हैं, कितने हानिकर, कितने नैतिक रूप से अनिर्धारित… "
                  "कितने संघर्ष वाले, कितने संघर्ष से रहित?"]
    h["2-7-3-1-0"] = [f"##### {C.TIKA_H}"]
    h["2-388"] = [C.pq_line(P["2-388"][0], "mp")]
    h["2-7-3-2-0"] = [f"##### {C.DUKA_H}"]
    h["2-389"] = [C.pq_line(x, "mp") for x in P["2-389"][:3]] + [f"{C.PANHA}।", f"सजगता के आधारों का विश्लेषण {C.DONE}।"]
    return h


if __name__ == "__main__":
    hi = build()
    C.check_unknown()
    C.emit(NAME, hi)
