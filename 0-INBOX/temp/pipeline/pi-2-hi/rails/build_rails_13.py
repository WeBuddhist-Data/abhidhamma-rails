"""Builder for the Hindi rails translation of pi-2 chapter 13 (Appamaññāvibhaṅga), plain audience.

Reuses the shared strings of build_rails_12.py (jhāna formulas, citta definition, matrix frames)
and the approved sample builder (read-only).

usage: python -I -X utf8 build_rails_13.py
"""
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-hi\rails")
import build_rails_sample as S  # noqa: E402
import build_rails_12 as C  # noqa: E402

q, called = C.q, C.called

# the four boundless states: name, gender of the noun, synonym string (Yā sattesu X Xyanā Xyitattaṃ Xcetovimutti)
MUD = "दूसरों के सुख पर प्रसन्नता"
AP = {
    "metta": dict(n="मैत्री", g="f", syn="मैत्री, मैत्री करना, मैत्री से भरा होना, मैत्री द्वारा मन की मुक्ति",
                  sim="जैसे कोई किसी प्रिय, मनभावन व्यक्ति को देखकर उसके प्रति मैत्री रखे"),
    "karuna": dict(n="करुणा", g="f", syn="करुणा, करुणा करना, करुणा से भरा होना, करुणा द्वारा मन की मुक्ति",
                   sim="जैसे कोई किसी दुर्दशा में पड़े, दीन-हीन व्यक्ति को देखकर उसके प्रति करुणा करे"),
    "mudita": dict(n=MUD, g="f", syn=f"{MUD}, दूसरों के सुख पर प्रसन्न होना, {MUD} से भरा होना, {MUD} द्वारा मन की मुक्ति",
                   sim="जैसे कोई किसी प्रिय, मनभावन व्यक्ति को देखकर प्रसन्न हो"),
    "upekkha": dict(n="समभाव", g="m", syn="समभाव, समभाव रखना, समभाव से भरा होना, समभाव द्वारा मन की मुक्ति",
                    sim="जैसे कोई किसी ऐसे व्यक्ति को देखकर, जो न मनभावन हो, न मन को न भाने वाला, समभाव वाला हो"),
}
ORDER = ["metta", "karuna", "mudita", "upekkha"]
FOUR = "चार असीम भाव – मैत्री, करुणा, दूसरों के सुख पर प्रसन्नता, समभाव।"


def mind(k):
    return f"{AP[k]['n']} के साथ होने वाले मन"


def called_ap(k):
    return f"यह {q(AP[k]['n'])} {'कहा जाता है' if AP[k]['g'] == 'm' else 'कही जाती है'}।"


def ap_def(k, lead="यहाँ"):
    return f"{lead} {AP[k]['n']} क्या है? प्राणियों के प्रति जो {AP[k]['syn']} है – {called_ap(k)}"


def pervade(k, var1="", var2=""):
    """X-sahagatena cetasā ekaṃ disaṃ pharitvā viharati, tathā dutiyaṃ, … Iti uddhamadho … pharitvā viharati."""
    a = (f"{mind(k)} से एक दिशा को व्याप्त करके रहता है, उसी तरह दूसरी को, उसी तरह तीसरी को, "
         f"उसी तरह चौथी को{var1}")
    b = (f"ऊपर, नीचे, चारों ओर, हर जगह, सबको अपने समान मानकर, पूरे लोक को {AP[k]['n']} के साथ होने वाले, विशाल, उन्नत, "
         f"अपरिमित, वैर से रहित, दुर्भावना से रहित{var2} मन से व्याप्त करके रहता है")
    return a, b


L_DISA = "एक दिशा"
L_PHAR = "व्याप्त करके"
L_TATHA = "उसी तरह दूसरी"
L_SABBA = "हर जगह, सबको अपने समान मानकर, पूरे लोक को"
L_VIPUL = "विशाल"
DISA = (f"{q(L_DISA)}, यानी पूर्व दिशा, या पश्चिम दिशा, या उत्तर दिशा, या दक्षिण दिशा, या ऊपर, या नीचे, या चारों ओर, "
        f"या बीच की दिशा।")
PHAR = f"{q(L_PHAR)}, यानी व्याप्त करके उस पर मन को दृढ़ता से टिकाकर।"
TATHA = (f"{q(L_TATHA)}, यानी जैसे एक दिशा को, उसी तरह दूसरी दिशा को, उसी तरह तीसरी दिशा को, उसी तरह चौथी दिशा को, "
         f"उसी तरह ऊपर, उसी तरह नीचे, उसी तरह चारों ओर, उसी तरह बीच की दिशा को।")
SABBA = (f"{q(L_SABBA)}, यानी सब कुछ पूरी तरह, हर प्रकार से सब कुछ, बिना कुछ बचाए, बिना कुछ छोड़े। यह संपूर्णता को "
         f"समेटने वाला कथन है – {q(L_SABBA)}।")


def vipul(var=""):
    return (f"{q(L_VIPUL)}, यानी जो विशाल है, वही उन्नत है; जो उन्नत है, वही अपरिमित है; जो अपरिमित है, वही वैर से रहित है; "
            f"जो वैर से रहित है, वही दुर्भावना न रखने वाला{var} है।")


def citta_tail(k):
    return f"यह मन इस {AP[k]['n']} {C.SAHAGATA4}। {called(mind(k) + ' से')}"


def opening(k):
    return [f"भिक्षु {mind(k)} से एक दिशा को व्याप्त करके कैसे रहता है? {AP[k]['sim']}, उसी तरह वह सभी प्राणियों को "
            f"{AP[k]['n']} से व्याप्त करता है।",
            ap_def(k),
            f"{C.CITTA_DEF if k != 'metta' else C.CITTA_DEF_FULL} {citta_tail(k)}"]


def sahagata_seg(k):
    return [f"{q(mind(k) + ' से')}, {ap_def(k)}", f"{C.CITTA_DEF} {citta_tail(k)}"]


# --- Abhidhammabhājanīya
def ap_obj(k):
    return f", जो {AP[k]['n']} के साथ होने वाला है,"


def ap_close(k, syn=None):
    return (f"उस समय जो {syn or AP[k]['syn']} है – {called_ap(k)} शेष परिघटनाएँ {AP[k]['n']} से जुड़ी हैं।")


def ap_line(k, body, q_=True, open_=C.OPEN_RUPA, syn=None):
    head = f"यहाँ {AP[k]['n']} क्या है? " if q_ else ""
    return f"{head}{open_} {body}{ap_obj(k)} {ap_close(k, syn)}"


def ap_vip(k, kbody, vbody):
    return (f"यहाँ {AP[k]['n']} क्या है? {C.OPEN_RUPA} {kbody}{ap_obj(k)} {C.KUSALA_MID} {C.VIP_RUPA} {vbody}{ap_obj(k)} "
            f"{ap_close(k)}")


def build():
    H = {}
    jh, chain = C.jh, C.chain
    H["2-13-0"] = ["### असीम भावों का विश्लेषण"]
    H["2-13-1-0"] = [f"#### {S.SUTTANTA_BH}"]
    parts = []
    for i, k in enumerate(ORDER):
        a, b = pervade(k, " [वर्तनी-भेद (Sī.): catutthiṃ]" if i == 0 else "",
                       " [वर्तनी-भेद (Sī., Syā.): abyāpajjhena]" if i == 0 else "")
        parts.append(f"{a}। इस प्रकार {b}।")
    H["2-642"] = [f"चार असीम भाव – यहाँ भिक्षु {parts[0]} " + " ".join(p[0].upper() + p[1:] for p in parts[1:])]
    heads = {"metta": "मैत्री", "karuna": "करुणा", "mudita": MUD, "upekkha": "समभाव"}
    ids = {"metta": 643, "karuna": 653, "mudita": 663, "upekkha": 673}
    sub = {"metta": "2-13-1-1-0", "karuna": "2-13-1-2-0", "mudita": "2-13-1-3-0", "upekkha": "2-13-1-4-0"}
    for k in ORDER:
        b = ids[k]
        H[sub[k]] = [f"##### {heads[k]}"]
        H[f"2-{b}"] = opening(k)
        H[f"2-{b + 1}"] = [DISA]
        H[f"2-{b + 2}"] = [PHAR]
        seq = {  # the order of the next three segments differs in the source
            "metta": [C.VIH_SEG, TATHA, SABBA], "karuna": [C.VIH_SEG, TATHA, SABBA],
            "mudita": [C.VIH_SHORT, TATHA, SABBA], "upekkha": [C.VIH_SHORT, TATHA, SABBA]}[k]
        H[f"2-{b + 3}"] = [seq[0]]
        H[f"2-{b + 4}"] = [seq[1]]
        H[f"2-{b + 5}"] = [seq[2]]
        H[f"2-{b + 6}"] = sahagata_seg(k)
        H[f"2-{b + 7}"] = [vipul(" [वर्तनी-भेद (Sī., Syā.): abyāpajjho]" if k == "metta" else "")]
        H[f"2-{b + 8}"] = [PHAR]
        H[f"2-{b + 9}"] = [C.VIH_SHORT]
    H["2-682"] = [C.VIH_SHORT, f"{S.SUTTANTA_BH}।"]

    # ------------------------------------------------------------------ Abhidhammabhājanīya
    H["2-13-2-0"] = [f"#### {S.ABHI_BH}"]
    H["2-683"] = [FOUR]
    two5 = C.J2_FIVE
    for k, (i4, i5) in zip(["metta", "karuna", "mudita"], [(684, 685), (686, 687), (688, 689)]):
        second = jh("pit", 2) if k == "karuna" else jh("vit", 2)   # source: karuṇā 2nd line opens with pītiyā ca virāgā
        H[f"2-{i4}"] = [ap_line(k, jh("viv", 1)), ap_line(k, second), ap_line(k, jh("pit", 3))]
        H[f"2-{i5}"] = [ap_line(k, jh("viv", 1), False), ap_line(k, two5, False), ap_line(k, jh("vit", 3), False),
                        ap_line(k, jh("pit", 4), False)]
    H["2-690"] = [ap_line("upekkha", jh("suk", 4))]
    H["2-691"] = [FOUR]
    for k, i in zip(["metta", "karuna", "mudita"], [692, 693, 694]):
        H[f"2-{i}"] = [ap_vip(k, jh("viv", 1), jh("viv", 1, True)),
                       ap_vip(k, jh("vit", 2), chain([2, 3, 1, 2, 3, 4], True))]
    H["2-695"] = [ap_vip("upekkha", jh("suk", 4), jh("suk2", 4, True))]
    H["2-696"] = [FOUR]
    H["2-697"] = [ap_line("metta", jh("viv", 1), open_=C.OPEN_RUPA_KIR),
                  ap_line("metta", chain([2, 3, 1, 2, 3, 4]), open_=C.OPEN_RUPA_KIR)]
    H["2-698"] = [f"यहाँ करुणा क्या है?… यहाँ {MUD} क्या है?… "
                  + ap_line("upekkha", jh("suk2", 4), open_=C.OPEN_RUPA_KIR), f"{S.ABHI_BH}।"]

    # ------------------------------------------------------------------ Pañhāpucchaka
    H["2-13-3-0"] = [f"#### {S.PANHA}"]
    pp = []
    for k in ORDER:
        a, b = pervade(k)
        pp.append(f"{a}, इस प्रकार {b}")
    H["2-699"] = [f"चार असीम भाव – यहाँ भिक्षु {'; '.join(pp)}।"]
    H["2-700"] = [f"चार असीम भावों में से {C.KITI}"]
    H["2-13-3-1-0"] = ["##### तीन-तीन के वर्गीकरण"]
    T3 = "तीन असीम भाव"
    tika = [
        C.KUS_ABY,
        f"{T3} सुखद अनुभूति से जुड़े होते हैं, समभाव न दुःखद, न सुखद अनुभूति से जुड़ा होता है।",
        C.VIPAKA3,
        C.UPADINNA_A + "।",
        "क्लेशों से मलिन न होने वाले, पर क्लेशों का विषय बनने वाले होते हैं।",
        f"{T3} कभी आरंभिक विचार और सतत विचार वाले होते हैं, कभी आरंभिक विचार से रहित, केवल सतत विचार वाले, कभी आरंभिक "
        "विचार और सतत विचार दोनों से रहित; समभाव आरंभिक विचार और सतत विचार दोनों से रहित होता है।",
        f"{T3} कभी उल्लास के साथ होने वाले होते हैं, कभी सुख के साथ होने वाले, समभाव के साथ होने वाले नहीं होते, कभी इन्हें "
        "उल्लास के साथ होने वाले नहीं कहा जा सकता; समभाव समभाव के साथ होने वाला होता है।",
        C.NOT_SEEN, C.NOT_SEEN_ROOTS,
        "कभी संचय की ओर ले जाने वाले होते हैं, कभी न संचय की ओर, न संचय घटाने की ओर ले जाने वाले, न सीखने के चरण के, "
        "न सीखना पूरा होने के चरण के, उन्नत होते हैं, इन्हें न सीमित विषय वाले कहा जा सकता है, न उन्नत विषय वाले, "
        "न अपरिमित विषय वाले।",
        "मध्यम और अनिश्चित होते हैं, इन्हें न मार्ग को विषय बनाने वाले कहा जा सकता है, न मार्ग को मूल बनाने वाले, न मार्ग "
        "की प्रधानता वाले।",
        C.UPPANNA3, C.ATITA3,
        f"इन्हें {C.VATTABBA_ATITA_ARAM}।",
        f"{C.AJJH3}, दूसरों से संबंधित विषय वाले, दिखाई न देने वाले और टकराव से रहित होते हैं।",
    ]
    H["2-701"] = [" ".join(tika)]
    H["2-13-3-2-0"] = ["##### दो-दो के वर्गीकरण"]
    H["2-702"] = [
        f"मैत्री मूल रूपी है, {T3} मूल रूपी नहीं होते, ये मूल वाले होते हैं, मूलों से जुड़े होते हैं। मैत्री मूल रूपी भी है "
        f"और मूल वाली भी; {T3}ों को मूल रूपी भी और मूल वाले भी नहीं कहा जा सकता, ये मूल वाले हैं, पर स्वयं मूल रूपी नहीं। "
        f"मैत्री मूल रूपी भी है और मूलों से जुड़ी भी; {T3}ों को मूल रूपी भी और मूलों से जुड़े भी नहीं कहा जा सकता, ये "
        f"मूलों से जुड़े हैं, पर स्वयं मूल रूपी नहीं। {T3} मूल रूपी न होकर मूल वाले हैं; मैत्री को न मूल रूपी न होने वाली, "
        f"पर मूल वाली कहा जा सकता है, न मूल रूपी न होने वाली और मूल से रहित।",
        f"{C.SANKHATA}, अभौतिक और लौकिक होते हैं, {C.KENACI}, {C.ASAVA_A}, मन के मैलों का विषय बनने वाले होते हैं, "
        f"मन के मैलों से अलग होते हैं, {C.ASAVA_B.replace('“', '').replace('”', '')}, ये {C.ASAVA_C}, "
        f"{C.ASAVA_D}। ये मन के मैलों से अलग, पर उनका विषय बनने वाले होते हैं।",
        C.NO_FETTERS,
        f"{C.NO_CLINGING} {T3} कभी आरंभिक विचार वाले होते हैं, कभी आरंभिक विचार से रहित; समभाव आरंभिक विचार से रहित "
        f"होता है। {T3} कभी सतत विचार वाले होते हैं, कभी सतत विचार से रहित; समभाव सतत विचार से रहित होता है। {T3} कभी "
        f"उल्लास वाले होते हैं, कभी उल्लास से रहित; समभाव उल्लास से रहित होता है। {T3} कभी उल्लास के साथ होने वाले होते हैं, "
        f"कभी उल्लास के साथ न होने वाले; समभाव उल्लास के साथ न होने वाला होता है। {T3} सुख के साथ होने वाले होते हैं, "
        f"समभाव सुख के साथ न होने वाला होता है। समभाव समभाव के साथ होने वाला होता है, {T3} समभाव के साथ न होने वाले होते "
        f"हैं; ये इंद्रिय-सुखों के लोक से संबंधित नहीं होते, सूक्ष्म भौतिक लोक से संबंधित होते हैं, अभौतिक लोक से संबंधित "
        f"नहीं होते, अस्तित्व के लोकों में समाए हुए, मुक्ति की ओर न ले जाने वाले, अनिश्चित, सर्वोच्च न होने वाले और संघर्ष "
        f"से रहित होते हैं।",
        f"{S.PANHA}।",
        f"असीम भावों का विश्लेषण {S.DONE}।",
    ]
    return H


def main():
    src = (S.PALI / "13-appamannavibhango.md").read_text(encoding="utf-8").splitlines()
    S.emit(src, build(), S.OUT / "13-appamannavibhango.md")


if __name__ == "__main__":
    main()
