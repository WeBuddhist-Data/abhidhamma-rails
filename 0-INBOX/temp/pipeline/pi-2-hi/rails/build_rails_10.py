"""Hindi rails builder: pi-2 chapter 10, Bojjhaṅgavibhaṅga.

usage: python -I -X utf8 build_rails_10.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import build_rails_5_7_10_11_common as C  # noqa: E402

NAME = "10-bojjhangavibhango.md"
B = C.BOJ
O = C.BOJ_ORDER
SEVEN_FULL = f"{C.SEVEN_BOJ} – " + ", ".join(B[k] for k in O) + "।"
SEVEN_PE = f"{C.SEVEN_BOJ} – {B['sati']}… {B['upekkha']}।"
WHAT = "यहाँ {} क्या है?"


def called(k):
    return f"यह “{B[k]}” कहा जाता है।"


# ^2-469: Atthi X, atthi Y. Yadapi X tadapi …sambojjhaṅgo abhiññāya sambodhāya nibbānāya saṃvattati.
LEADS = "उच्च ज्ञान, पूर्ण जागृति और निर्वाण की ओर ले जाता है"


def two(k, a, b, g, a_first=None, b_first=None):
    hv = "होती है" if g == "f" else "होता है"
    a1, b1 = a_first or a, b_first or b
    return (f"{WHAT.format(B[k])} {a1} {hv}, {b1} {hv}। "
            f"जो {a} है, वह भी {B[k]} है और {LEADS}। "
            f"जो {b} है, वह भी {B[k]} है और {LEADS}।")


INT, EXT = "स्वयं से संबंधित परिघटनाओं में", "दूसरों से संबंधित परिघटनाओं में"
SATI_LOK = f"उस समय जो {C.SATI_SHORT}, {B['sati']}, {C.MAGGA3} है"
UPEKKHA_LOK = f"उस समय जो {C.UPEKKHA}, {B['upekkha']} है"
CHAIN = "… ".join(C.remaining(C.boj_obl(k)) for k in O[:-1]) + "।"


def build():
    P = C.pali_segs(NAME)
    h = {}
    h["2-10-0"] = ["### जागृति के अंगों का विश्लेषण"]
    h["2-10-1-0"] = [f"#### {C.SUTTANTA_BH}"]
    h["2-466"] = [SEVEN_FULL]
    h["2-467"] = [
        f"{WHAT.format(B['sati'])} यहाँ भिक्षु सजग होता है, उच्चतम सजगता और सावधानी से युक्त होता है, "
        f"बहुत पहले किए गए और बहुत पहले कहे गए को भी याद करने वाला और बार-बार याद करने वाला होता है – {called('sati')}",
        f"इस तरह सजग रहते हुए वह उस शिक्षा की प्रज्ञा से छानबीन करता है, उसे गहराई से परखता है, "
        f"उसकी पूरी जाँच-पड़ताल में लग जाता है – {called('dhammavicaya')}",
        f"उस शिक्षा की प्रज्ञा से छानबीन करते हुए, उसे गहराई से परखते हुए, उसकी पूरी जाँच-पड़ताल में लगे हुए "
        f"उस भिक्षु का उत्साह जाग्रत होता है, ढीला नहीं पड़ता – {called('viriya')}",
        f"जाग्रत उत्साह वाले को सांसारिक भोग से रहित उल्लास उत्पन्न होता है – {called('piti')}",
        f"जिसका मन उल्लास से भरा है, उसकी काया भी शांत होती है, मन भी शांत होता है – {called('passaddhi')}",
        f"शांत काया वाले, सुखी व्यक्ति का मन एकाग्र होता है – {called('samadhi')}",
        f"इस तरह एकाग्र हुए मन को वह भली-भाँति समभाव से देखने वाला होता है – {called('upekkha')}",
    ]
    h["2-468"] = [SEVEN_FULL]
    h["2-469"] = [
        two("sati", f"{INT} सजगता", f"{EXT} सजगता", "f"),
        two("dhammavicaya", f"{INT} गहरी छानबीन", f"{EXT} गहरी छानबीन", "f"),
        two("viriya", "शारीरिक उत्साह", "मानसिक उत्साह", "m"),
        two("piti", "आरंभिक विचार और सतत विचार वाला उल्लास", "आरंभिक विचार और सतत विचार दोनों से रहित उल्लास", "m"),
        two("passaddhi", "मानसिक काया की प्रशांति", "मन की प्रशांति", "f",
            "मानसिक काया की प्रशांति [वर्तनी-भेद (Syā., Ka.): kāyappassaddhi]",
            "मन की प्रशांति [वर्तनी-भेद (Syā., Ka.): cittappassaddhi]"),
        two("samadhi", "आरंभिक विचार और सतत विचार वाली एकाग्रता",
            "आरंभिक विचार से रहित और सतत विचार से रहित एकाग्रता", "f"),
        two("upekkha", f"{INT} समभाव", f"{EXT} समभाव", "m"),
    ]
    h["2-470"] = [SEVEN_FULL]
    dev = [f"{C.boj_obl(k)} का अभ्यास करता है" for k in O]
    h["2-471"] = [
        f"{WHAT.format(B['sati'])} यहाँ भिक्षु {dev[0]}, {C.NISSITA['m']}, {dev[1]}… "
        + "… ".join(dev[2:]) + f", {C.NISSITA['m']}।",
        f"{C.SUTTANTA_BH}।",
    ]
    h["2-10-2-0"] = [f"#### {C.ABHI_BH}"]
    h["2-472"] = [SEVEN_FULL]
    h["2-473"] = [f"यहाँ {C.SEVEN_BOJ} कौन-से हैं? " + C.lok("k", f"उस समय {C.SEVEN_BOJ} होते हैं – {B['sati']}… {B['upekkha']}।")]
    defs = [
        f"{WHAT.format(B['sati'])} जो {C.SATI_PE}, {B['sati']}, {C.MAGGA3} है – {called('sati')}",
        f"{WHAT.format(B['dhammavicaya'])} जो {C.PANNA_PE}, {B['dhammavicaya']}, {C.MAGGA3} है – {called('dhammavicaya')}",
        f"{WHAT.format(B['viriya'])} जो {C.VIRIYA_PE}, {B['viriya']}, {C.MAGGA3} है – {called('viriya')}",
        f"{WHAT.format(B['piti'])} जो {C.PITI}, {B['piti']} है – {called('piti')}",
        f"{WHAT.format(B['passaddhi'])} {C.PASSADDHI}, {B['passaddhi']} है – {called('passaddhi')}",
        f"{WHAT.format(B['samadhi'])} जो {C.SAMADHI_PE}, {B['samadhi']}, {C.MAGGA3} है – {called('samadhi')}",
    ]
    upekkha_def = f"{WHAT.format(B['upekkha'])} जो {C.UPEKKHA}, {B['upekkha']} है – {called('upekkha')}"
    h["2-474"] = defs + [f"{upekkha_def} ये {C.SEVEN_BOJ} कहे जाते हैं। {C.remaining('जागृति के सात अंगों')}।"]
    h["2-475"] = [SEVEN_PE]
    sati_l = lambda kind: f"{WHAT.format(B['sati'])} " + C.lok(kind, f"{SATI_LOK} – {called('sati')} {CHAIN}")
    upek_l = lambda kind: f"{WHAT.format(B['upekkha'])} " + C.lok(
        kind, f"{UPEKKHA_LOK} – {called('upekkha')} {C.remaining(C.boj_obl('upekkha'))}।")
    h["2-476"] = [sati_l("k"), upek_l("k")]
    h["2-477"] = [SEVEN_PE]
    h["2-478"] = [f"यहाँ {C.SEVEN_BOJ} कौन-से हैं? " + C.lok("vd", f"उस समय {C.SEVEN_BOJ} होते हैं – {B['sati']}… {B['upekkha']}।")]
    h["2-479"] = [defs[0][:-1] + "…।",
                  f"{upekkha_def} ये “{C.SEVEN_BOJ}” कहे जाते हैं। {C.remaining('जागृति के सात अंगों')}।"]
    h["2-480"] = [SEVEN_PE]
    h["2-481"] = [sati_l("v-"), upek_l("v"), f"{C.ABHI_BH}।"]  # the first line has no suññataṃ in the Pāli
    h["2-10-3-0"] = [f"#### {C.PANHA}"]
    h["2-482"] = [SEVEN_FULL]
    h["2-483"] = ["जागृति के सात अंगों में से कितने हितकर हैं, कितने हानिकर, कितने नैतिक रूप से अनिर्धारित… "
                  "कितने संघर्ष वाले, कितने संघर्ष से रहित?"]
    h["2-10-3-1-0"] = [f"##### {C.TIKA_H}"]
    h["2-484"] = [C.pq_line(P["2-484"][0], "mp")]
    h["2-10-3-2-0"] = [f"##### {C.DUKA_H}"]
    h["2-485"] = [C.pq_line(P["2-485"][0], "mp"), C.pq_line(P["2-485"][1], "mp"),
                  f"{C.PANHA}।", f"जागृति के अंगों का विश्लेषण {C.DONE}।"]
    return h


if __name__ == "__main__":
    hi = build()
    C.check_unknown()
    C.emit(NAME, hi)
