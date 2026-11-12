"""Hindi rails builder: pi-2 chapter 11, Maggaṅgavibhaṅga.

usage: python -I -X utf8 build_rails_11.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import build_rails_5_7_10_11_common as C  # noqa: E402

NAME = "11-maggangavibhango.md"
M = C.MAGGA
B = C.BOJ
EIGHT = "आठ अंगों वाला मार्ग"
FIVE = "पाँच अंगों वाला मार्ग"
LIST8 = ", ".join(M[k][0] for k in C.MAGGA8)
LIST5 = ", ".join(M[k][0] for k in C.MAGGA5)
PE8 = f"{M['ditthi'][0]}… {M['samadhi'][0]}"


def what(k):
    return f"यहाँ {M[k][0]} क्या है?"


def called(k):
    name, g = M[k]
    return f"यह {C.called(name, g)}"


# Abhidhammabhājanīya definitions (pi-1 ^1-283, ^1-292, ^1-299..301, ^1-289, ^1-290)
BODY = {
    "ditthi": f"जो {C.PANNA_PE}, {B['dhammavicaya']}, {C.MAGGA3} है",
    "sankappa": f"जो {C.SANKAPPA_FULL}, {C.MAGGA3} है",
    "sankappa_pe": f"जो {C.SANKAPPA_PE}, {C.MAGGA3} है",
    "vaca": f"जो {C.VACA}, {C.MAGGA3} है",
    "kammanta": f"जो {C.KAMMANTA}, {C.MAGGA3} है",
    "ajiva": f"जो {C.AJIVA}, {C.MAGGA3} है",
    "vayama": f"जो {C.VIRIYA_PE}, {B['viriya']}, {C.MAGGA3} है",
    "sati": f"जो {C.SATI_PE}, {B['sati']}, {C.MAGGA3} है",
    "samadhi": f"जो {C.SAMADHI_PE}, {B['samadhi']}, {C.MAGGA3} है",
}


def define(k, body_key=None):
    return f"{what(k)} {BODY[body_key or k]} – {called(k)}"


def path_closing(name):
    return f"यह “{name}” कहा जाता है। {C.remaining(name.replace('वाला मार्ग', 'वाले मार्ग'))}।"


EFFORT = "चाह जगाता है, प्रयास करता है, उत्साह जगाता है, मन को तत्पर करता है, पूरा ज़ोर लगाता है"
JHANA4 = (
    "यहाँ भिक्षु इंद्रिय-सुखों से अलग होकर, हानिकर परिघटनाओं से अलग होकर, आरंभिक विचार और सतत विचार वाले, "
    "अलगाव से उत्पन्न उल्लास और सुख वाले पहले ध्यान को प्राप्त करके उसमें रहता है; आरंभिक विचार और सतत विचार के "
    "शांत होने से, स्वयं में निर्मलता वाले, मन के एक बिंदु पर टिकने वाले, आरंभिक विचार और सतत विचार से रहित, "
    "एकाग्रता से उत्पन्न उल्लास और सुख वाले दूसरे ध्यान को प्राप्त करके उसमें रहता है; उल्लास के फीका पड़ने से "
    "वह समभाव के साथ, सजग और स्पष्ट समझ रखते हुए रहता है और काया से सुख का अनुभव करता है, जिसके बारे में आर्य "
    "कहते हैं, “समभाव वाला, सजग, सुख से रहने वाला”, ऐसे तीसरे ध्यान को प्राप्त करके उसमें रहता है; सुख को छोड़ने "
    "से और दुःख को छोड़ने से, और पहले ही प्रसन्नता और उदासी के मिट जाने से, न दुःखद, न सुखद, समभाव और सजगता से "
    "पूरी तरह शुद्ध चौथे ध्यान को प्राप्त करके उसमें रहता है"
)  # PI1 ^1-160 .. (four jhānas), satimā = सजग (pi-2 termbase)


def build():
    P = C.pali_segs(NAME)
    h = {}
    h["2-11-0"] = ["### मार्ग के अंगों का विश्लेषण"]
    h["2-11-1-0"] = [f"#### {C.SUTTANTA_BH}"]
    ARIYO = f"आठ अंगों वाला आर्य मार्ग, यानी – {LIST8}।"
    h["2-486"] = [ARIYO]
    h["2-487"] = [
        f"{what('ditthi')} दुःख का ज्ञान, दुःख की उत्पत्ति का ज्ञान, दुःख के अंत का ज्ञान, "
        f"दुःख के अंत की ओर ले जाने वाले प्रगति के ढंग का ज्ञान – {called('ditthi')}",
        f"{what('sankappa')} त्याग का संकल्प, दुर्भावना के अभाव का संकल्प, अहिंसा का संकल्प – {called('sankappa')}",
        f"{what('vaca')} झूठ बोलने से दूर रहना, चुगली की वाणी से दूर रहना, कठोर वाणी से दूर रहना, "
        f"व्यर्थ की बकवास से दूर रहना – {called('vaca')}",
        f"{what('kammanta')} जीव-हत्या से दूर रहना, बिना दी गई चीज़ लेने से दूर रहना, "
        f"इंद्रिय-सुखों में दुराचार से दूर रहना – {called('kammanta')}",
        f"{what('ajiva')} यहाँ आर्य शिष्य ग़लत आजीविका को छोड़कर सही आजीविका से जीविका चलाता है – {called('ajiva')}",
        f"{what('vayama')} यहाँ भिक्षु उत्पन्न न हुई बुरी, हानिकर परिघटनाओं को उत्पन्न न होने देने के लिए {EFFORT}; "
        f"उत्पन्न हो चुकी बुरी, हानिकर परिघटनाओं को छोड़ने के लिए {EFFORT}; "
        f"उत्पन्न न हुई हितकर परिघटनाओं की उत्पत्ति के लिए {EFFORT}; "
        f"उत्पन्न हो चुकी हितकर परिघटनाओं की स्थिरता के लिए, उनके लुप्त न होने के लिए, उनकी वृद्धि के लिए, "
        f"विपुलता के लिए और अभ्यास की परिपूर्णता के लिए {EFFORT} – {called('vayama')}",
        f"{what('sati')} यहाँ भिक्षु " + "; ".join(f"{C.ATAPI}, {C.anupassi(f)} रहता है" for f in C.FIELD)
        + f" – {called('sati')}",
        f"{what('samadhi')} {JHANA4} – {called('samadhi')}",
    ]
    h["2-488"] = [ARIYO]
    dev = [f"{M[k][0]} का अभ्यास करता है" for k in C.MAGGA8]
    h["2-489"] = [
        f"{what('ditthi')} यहाँ भिक्षु {dev[0]}, {C.NISSITA['f']}, " + "… ".join(dev[1:])
        + f", {C.NISSITA['f']}।",
        f"{C.SUTTANTA_BH}।",
    ]
    h["2-11-2-0"] = [f"#### {C.ABHI_BH}"]
    h["2-490"] = [f"{EIGHT} – {LIST8}।"]
    h["2-491"] = [f"यहाँ {EIGHT} क्या है? " + C.lok("k", f"उस समय {EIGHT} होता है – {PE8}।")]
    defs8 = [define(k) for k in C.MAGGA8]
    defs8[-1] += " " + path_closing(EIGHT)
    h["2-492"] = defs8
    h["2-493"] = [f"{FIVE} – {LIST5}।"]
    h["2-494"] = [f"यहाँ {FIVE} क्या है? " + C.lok("k", f"उस समय {FIVE} होता है – {LIST5}।")]
    defs5 = [define("ditthi"), define("sankappa", "sankappa_pe"), define("vayama"), define("sati"), define("samadhi")]
    defs5[-1] += " " + path_closing(FIVE)
    h["2-495"] = defs5
    h["2-496"] = [f"{FIVE} – {LIST5}।"]
    chain = "… ".join(C.remaining(M[k][0]) for k in ["ditthi", "sankappa", "vayama", "sati"]) + "।"
    dl = lambda kind: what("ditthi") + " " + C.lok(kind, f"उस समय {BODY['ditthi']} – {called('ditthi')} {chain}")
    samadhi_full = f"उस समय जो {C.SAMADHI_FULL}, {B['samadhi']}, {C.MAGGA3} है"
    sl = lambda kind, body: what("samadhi") + " " + C.lok(
        kind, f"{body} – {called('samadhi')} {C.remaining(M['samadhi'][0])}।")
    h["2-497"] = [dl("k"), sl("k", f"उस समय {BODY['samadhi']}")]
    h["2-498"] = [f"{EIGHT} – {PE8}।"]
    h["2-499"] = [f"यहाँ {EIGHT} क्या है? " + C.lok("v", f"उस समय {EIGHT} होता है – {PE8}। {path_closing(EIGHT)}")]
    h["2-500"] = [f"{FIVE} – {LIST5}।"]
    h["2-501"] = [f"यहाँ {FIVE} क्या है? " + C.lok("v", f"उस समय {FIVE} होता है – {LIST5}। {path_closing(FIVE)}")]
    h["2-502"] = [f"{FIVE} – {LIST5}।"]
    h["2-503"] = [dl("v"), sl("v", samadhi_full), f"{C.ABHI_BH}।"]
    h["2-11-3-0"] = [f"#### {C.PANHA}"]
    h["2-504"] = [ARIYO]
    h["2-505"] = ["मार्ग के आठ अंगों में से कितने हितकर हैं, कितने हानिकर, कितने नैतिक रूप से अनिर्धारित… "
                  "कितने संघर्ष वाले, कितने संघर्ष से रहित?"]
    h["2-11-3-1-0"] = [f"##### {C.TIKA_H}"]
    h["2-506"] = [C.pq_line(P["2-506"][0], "mp")]
    h["2-11-3-2-0"] = [f"##### {C.DUKA_H}"]
    h["2-507"] = [C.pq_line(x, "mp") for x in P["2-507"][:5]] + [f"{C.PANHA}।", f"मार्ग के अंगों का विश्लेषण {C.DONE}।"]
    return h


if __name__ == "__main__":
    hi = build()
    C.check_unknown()
    C.emit(NAME, hi)
