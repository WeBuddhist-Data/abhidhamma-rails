"""Builder for the Hindi rails SAMPLE of pi-1 (Dhammasaṅgaṇī, plain audience).

Writes:
  AI_translation/hindi/pi-1-hindi-plain-rails_split_chapters/preamble.md
  AI_translation/hindi/pi-1-hindi-plain-rails_split_chapters/1-matika.md
  0-INBOX/temp/pipeline/pi-1-hi/rails/sample-2-01/2-01-sample.md
  0-INBOX/temp/pipeline/pi-1-hi/rails/hi-rails-formulas.md

All Hindi comes from the fixed strings below, so identical Pāli gives byte-identical Hindi.
Every term follows the locked termbase AI_translation/hindi/pi-1-pali-hindi-termbase-plain.md.

usage: python -I -X utf8 build_rails_sample.py
"""
import os
import pathlib
import re

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PALI = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
OUT = ROOT / "AI_translation" / "hindi" / "pi-1-hindi-plain-rails_split_chapters"
PIPE = ROOT / "0-INBOX" / "temp" / "pipeline" / "pi-1-hi"
RAILS = PIPE / "rails"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")


def segments(path):
    out, buf = [], []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        buf.append(line)
        m = ID.search(line)
        if m:
            out.append((m.group(1), buf))
            buf = []
    assert not buf, f"lines without id in {path}"
    return out


def emit(pali_path, hindi, target):
    """Write hindi {id: [lines]} in the Pāli's order, checking ids, line counts and heading levels."""
    segs = segments(pali_path)
    ids = [i for i, _ in segs]
    assert set(ids) == set(hindi), (sorted(set(ids) - set(hindi))[:10], sorted(set(hindi) - set(ids))[:10])
    blocks = []
    for sid, plines in segs:
        hlines = hindi[sid]
        assert len(plines) == len(hlines), (sid, len(plines), len(hlines))
        for a, b in zip(plines, hlines):
            assert len(a) - len(a.lstrip("#")) == len(b) - len(b.lstrip("#")), sid
        hlines = list(hlines)
        hlines[-1] = f"{hlines[-1]} ^{sid}"
        blocks.append("\n".join(hlines))
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n\n".join(blocks) + "\n", encoding="utf-8", newline="\n")
    print("wrote", target, len(blocks), "segments")


# ------------------------------------------------------------------ preamble
preamble = {
    "T-1": ["उन भगवान, अर्हत्, पूर्ण रूप से जागृत बुद्ध को नमन"],
    "0": ["# अभिधम्म पिटक में"],
    "1-0": ["## परिघटनाओं की गणना"],
}

# ------------------------------------------------------------------ matrix names
PH = "परिघटनाएँ"
TIKA = "तीन-तीन के वर्गीकरणों की मूल सूची"
DUKA = "दो-दो के वर्गीकरणों की मूल सूची"
ABHI_DUKA = "अभिधम्म के दो-दो के वर्गीकरणों की मूल सूची"
SUTTA_DUKA = "उपदेशों के दो-दो के वर्गीकरणों की मूल सूची"

m = {}


def trio(sid, a, b, c, closing=None):
    lines = [f"(क) {a}।", f"(ख) {b}।", f"(ग) {c}।"]
    if closing:
        lines.append(closing + "।")
    m[sid] = lines


def pair(sid, a, b, *closing):
    m[sid] = [f"(क) {a}।", f"(ख) {b}।"] + [c + "।" for c in closing]


def ph(x):
    return f"{x} {PH}"


m["1-M-0"] = ["### मूल सूची"]
m["1-M-1-0"] = [f"#### {TIKA}"]
trio("1-M1-1", ph("हितकर"), ph("हानिकर"), ph("नैतिक रूप से अनिर्धारित"))
trio("1-M1-2", ph("सुखद अनुभूति से जुड़ी"), ph("दुःखद अनुभूति से जुड़ी"), ph("न दुःखद, न सुखद अनुभूति से जुड़ी"))
trio("1-M1-3", ph("कर्म-फल रूपी"), ph("कर्म-फल उत्पन्न करने वाली"), ph("न कर्म-फल रूपी, न कर्म-फल उत्पन्न करने वाली"))
trio("1-M1-4",
     f"कर्म से उत्पन्न और आसक्ति का विषय बनने वाली [वर्तनी-भेद (Syā.): upādinnupādāniyā] {PH}",
     ph("कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाली"),
     f"न कर्म से उत्पन्न, न आसक्ति का विषय बनने वाली [वर्तनी-भेद (Syā.): anupādinnānupādāniyā] {PH}")
trio("1-M1-5",
     ph("क्लेशों से मलिन और क्लेशों की ओर ले जाने वाली"),
     ph("क्लेशों से मलिन न होने वाली, पर क्लेशों की ओर ले जाने वाली"),
     f"क्लेशों से मलिन न होने वाली और क्लेशों की ओर न ले जाने वाली [वर्तनी-भेद (Syā.): asaṃkiliṭṭhāsaṃkilesikā] {PH}")
trio("1-M1-6",
     ph("आरंभिक विचार और सतत विचार वाली"),
     ph("आरंभिक विचार से रहित, केवल सतत विचार वाली"),
     f"आरंभिक विचार और सतत विचार दोनों से रहित [वर्तनी-भेद (Syā.): avitakkāvicārā] {PH}")
trio("1-M1-7", ph("उल्लास के साथ होने वाली"), ph("सुख के साथ होने वाली"), ph("समभाव के साथ होने वाली"))
trio("1-M1-8", ph("सत्य-दर्शन से छोड़ी जाने वाली"), ph("मानसिक अभ्यास से छोड़ी जाने वाली"),
     ph("न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़ी जाने वाली"))
trio("1-M1-9", ph("सत्य-दर्शन से छोड़े जाने वाले मूलों वाली"), ph("मानसिक अभ्यास से छोड़े जाने वाले मूलों वाली"),
     ph("न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़े जाने वाले मूलों वाली"))
trio("1-M1-10", ph("संचय की ओर ले जाने वाली"), ph("संचय घटाने की ओर ले जाने वाली"),
     f"न संचय की ओर, न संचय घटाने की ओर ले जाने वाली [वर्तनी-भेद (Syā.): nevācayagāmino nāpacayagāmino] {PH}")
trio("1-M1-11", ph("सीखने के चरण की"), ph("सीखना पूरा होने के चरण की"),
     f"न सीखने के चरण की, न सीखना पूरा होने के चरण की [वर्तनी-भेद (Sī., Syā.): nevasekkhānāsekkhā] {PH}")
trio("1-M1-12", ph("सीमित"), ph("उन्नत"), ph("अपरिमित"))
trio("1-M1-13", ph("सीमित विषय वाली"), ph("उन्नत विषय वाली"), ph("अपरिमित विषय वाली"))
trio("1-M1-14", ph("हीन"), ph("मध्यम"), ph("उत्तम"))
trio("1-M1-15", ph("ग़लत दिशा में निश्चित"), ph("सही दिशा में निश्चित"), ph("अनिश्चित"))
trio("1-M1-16", ph("मार्ग को विषय बनाने वाली"), ph("मार्ग को मूल बनाने वाली"), ph("मार्ग की प्रधानता वाली"))
trio("1-M1-17", ph("उत्पन्न हो चुकी"), ph("उत्पन्न न हुई"), ph("उत्पन्न होने वाली"))
trio("1-M1-18", ph("अतीत की"), ph("भविष्य की"), ph("वर्तमान की"))
trio("1-M1-19", ph("अतीत के विषय वाली"), ph("भविष्य के विषय वाली"), ph("वर्तमान के विषय वाली"))
trio("1-M1-20", ph("स्वयं से संबंधित"), ph("दूसरों से संबंधित"), ph("स्वयं और दूसरों दोनों से संबंधित"))
trio("1-M1-21", ph("स्वयं से संबंधित विषय वाली"), ph("दूसरों से संबंधित विषय वाली"),
     ph("स्वयं और दूसरों दोनों से संबंधित विषय वाली"))
trio("1-M1-22", ph("दिखाई देने वाली और टकराव वाली"), ph("दिखाई न देने वाली, पर टकराव वाली"),
     f"दिखाई न देने वाली और टकराव से रहित [वर्तनी-भेद (Syā.): anidassanāppaṭighā] {PH}", TIKA)

m["1-M-2-0"] = [f"#### {DUKA}"]

# Group of roots
m["1-M-2-1-0"] = ["##### मूलों का वर्ग"]
pair("1-M2-1", ph("मूल रूपी"), ph("मूल रूपी न होने वाली"))
pair("1-M2-2", ph("मूल वाली"), ph("मूल से रहित"))
pair("1-M2-3", ph("मूलों से जुड़ी"), ph("मूलों से अलग"))
pair("1-M2-4", ph("मूल रूपी भी और मूल वाली भी"), ph("मूल वाली, पर स्वयं मूल रूपी न होने वाली"))
pair("1-M2-5", ph("मूल रूपी भी और मूलों से जुड़ी भी"), ph("मूलों से जुड़ी, पर स्वयं मूल रूपी न होने वाली"))
pair("1-M2-6", ph("मूल रूपी न होने वाली, पर मूल वाली"), ph("मूल रूपी न होने वाली और मूल से रहित"), "मूलों का वर्ग")

# Lesser intermediate pairs
CUL = "बीच के छोटे दो-दो के वर्गीकरण"
m["1-M-2-2-0"] = [f"##### {CUL}"]
pair("1-M2-7", ph("कारणों पर निर्भर रहने वाली"), ph("कारणों पर निर्भर न रहने वाली"))
pair("1-M2-8", ph("निर्मित"), ph("अनिर्मित"))
pair("1-M2-9", ph("दिखाई देने वाली"), ph("दिखाई न देने वाली"))
pair("1-M2-10", ph("टकराव वाली"), ph("टकराव से रहित"))
pair("1-M2-11", ph("भौतिक"), ph("अभौतिक"))
pair("1-M2-12", ph("लौकिक"), ph("लोकोत्तर"))
pair("1-M2-13", ph("किसी एक प्रकार की चेतना से जानी जा सकने वाली"),
     ph("किसी एक प्रकार की चेतना से न जानी जा सकने वाली"), CUL)


def gocchaka(first, hid, title, R, V, O, P):
    """Six-pair group. R = 'X रूपी', V = 'X का विषय', O = oblique plural, P = pronoun for the last pair."""
    m[hid] = [f"##### {title}"]
    n = first
    pair(f"1-M2-{n}", ph(R), ph(f"{R} न होने वाली"))
    pair(f"1-M2-{n+1}", ph(f"{V} बनने वाली"), ph(f"{V} न बनने वाली"))
    pair(f"1-M2-{n+2}", ph(f"{O} से जुड़ी"), ph(f"{O} से अलग"))
    pair(f"1-M2-{n+3}", ph(f"{R} भी और {V} बनने वाली भी"), ph(f"{V} बनने वाली, पर स्वयं {R} न होने वाली"))
    pair(f"1-M2-{n+4}", ph(f"{R} भी और {O} से जुड़ी भी"), ph(f"{O} से जुड़ी, पर स्वयं {R} न होने वाली"))
    pair(f"1-M2-{n+5}", ph(f"{O} से अलग, पर {P} विषय बनने वाली"), ph(f"{O} से अलग और {P} विषय न बनने वाली"), title)


gocchaka(14, "1-M-2-3-0", "मन के मैलों का वर्ग", "मन के मैल रूपी", "मन के मैलों का विषय", "मन के मैलों", "उनका")
gocchaka(20, "1-M-2-4-0", "बंधनों का वर्ग", "बंधन रूपी", "बंधनों का विषय", "बंधनों", "उनका")
gocchaka(26, "1-M-2-5-0", "गाँठों का वर्ग", "गाँठ रूपी", "गाँठों का विषय", "गाँठों", "उनका")
gocchaka(32, "1-M-2-6-0", "बाढ़ों का वर्ग", "बाढ़ रूपी", "बाढ़ों का विषय", "बाढ़ों", "उनका")
gocchaka(38, "1-M-2-7-0", "जकड़नों का वर्ग", "जकड़न रूपी", "जकड़नों का विषय", "जकड़नों", "उनका")
gocchaka(44, "1-M-2-8-0", "बाधाओं का वर्ग", "बाधा रूपी", "बाधाओं का विषय", "बाधाओं", "उनका")

# Misapprehension: five pairs only
PAR = "ग़लत धारणा का वर्ग"
m["1-M-2-9-0"] = [f"##### {PAR}"]
R, V, O = "ग़लत धारणा रूपी", "ग़लत धारणा का विषय", "ग़लत धारणा"
pair("1-M2-50", ph(R), ph(f"{R} न होने वाली"))
pair("1-M2-51", ph(f"{V} बनने वाली"), ph(f"{V} न बनने वाली"))
pair("1-M2-52", ph(f"{O} से जुड़ी"), ph(f"{O} से अलग"))
pair("1-M2-53", ph(f"{R} भी और {V} बनने वाली भी"), ph(f"{V} बनने वाली, पर स्वयं {R} न होने वाली"))
pair("1-M2-54", ph(f"{O} से अलग, पर उसका विषय बनने वाली"), ph(f"{O} से अलग और उसका विषय न बनने वाली"), PAR)

# Greater intermediate pairs
MAH = "बीच के बड़े दो-दो के वर्गीकरण"
m["1-M-2-10-0"] = [f"##### {MAH}"]
pair("1-M2-55", ph("विषय वाली"), ph("विषय से रहित"))
pair("1-M2-56", ph("मन रूपी"), ph("मन रूपी न होने वाली"))
pair("1-M2-57", ph("मन की सहचर"), ph("मन की सहचर न होने वाली"))
pair("1-M2-58", ph("मन से जुड़ी"), ph("मन से अलग"))
pair("1-M2-59", ph("मन से घुली-मिली"), ph("मन से घुली-मिली न होने वाली"))
pair("1-M2-60", ph("मन से उत्पन्न"), ph("मन से उत्पन्न न होने वाली"))
pair("1-M2-61", ph("मन के साथ-साथ होने वाली"), ph("मन के साथ-साथ न होने वाली"))
pair("1-M2-62", ph("मन का अनुसरण करने वाली"), ph("मन का अनुसरण न करने वाली"))
pair("1-M2-63", ph("मन से घुली-मिली और मन से उत्पन्न"), f"ऐसी {PH} जो मन से घुली-मिली और मन से उत्पन्न नहीं हैं")
pair("1-M2-64", ph("मन से घुली-मिली, मन से उत्पन्न और मन के साथ-साथ होने वाली"),
     f"ऐसी {PH} जो मन से घुली-मिली, मन से उत्पन्न और मन के साथ-साथ होने वाली नहीं हैं")
pair("1-M2-65", ph("मन से घुली-मिली, मन से उत्पन्न और मन का अनुसरण करने वाली"),
     f"ऐसी {PH} जो मन से घुली-मिली, मन से उत्पन्न और मन का अनुसरण करने वाली नहीं हैं")
pair("1-M2-66", ph("आंतरिक"), ph("बाह्य"))
pair("1-M2-67", ph("व्युत्पन्न"), ph("व्युत्पन्न न होने वाली"))
pair("1-M2-68", f"कर्म से उत्पन्न [वर्तनी-भेद (Sī., Syā.): upādinnā] {PH}", ph("कर्म से उत्पन्न न होने वाली"), MAH)

# Clinging: six pairs, singular pronoun
gocchaka(69, "1-M-2-11-0", "आसक्ति का वर्ग", "आसक्ति रूपी", "आसक्ति का विषय", "आसक्ति", "उसका")

# Defilements: eight pairs
KIL = "मन के क्लेशों का वर्ग"
m["1-M-2-12-0"] = [f"##### {KIL}"]
R, L, M, O = "मन के क्लेश रूपी", "क्लेशों की ओर ले जाने वाली", "क्लेशों से मलिन", "क्लेशों"
pair("1-M2-75", ph(R), ph(f"{R} न होने वाली"))
pair("1-M2-76", ph(L), ph("क्लेशों की ओर न ले जाने वाली"))
pair("1-M2-77", ph(M), ph(f"{M} न होने वाली"))
pair("1-M2-78", ph(f"{O} से जुड़ी"), ph(f"{O} से अलग"))
pair("1-M2-79", ph(f"{R} भी और {L} भी"), ph(f"{L}, पर स्वयं {R} न होने वाली"))
pair("1-M2-80", ph(f"{R} भी और {M} भी"), ph(f"{M}, पर स्वयं {R} न होने वाली"))
pair("1-M2-81", ph(f"{R} भी और {O} से जुड़ी भी"), ph(f"{O} से जुड़ी, पर स्वयं {R} न होने वाली"))
pair("1-M2-82", ph(f"{O} से अलग, पर {L}"), ph(f"{O} से अलग और क्लेशों की ओर न ले जाने वाली"), KIL)

# Final pairs of the Abhidhamma matrix
PIT = "अंतिम दो-दो के वर्गीकरण"
m["1-M-2-13-0"] = [f"##### {PIT}"]
pair("1-M2-83", ph("सत्य-दर्शन से छोड़ी जाने वाली"), ph("सत्य-दर्शन से न छोड़ी जाने वाली"))
pair("1-M2-84", ph("मानसिक अभ्यास से छोड़ी जाने वाली"), ph("मानसिक अभ्यास से न छोड़ी जाने वाली"))
pair("1-M2-85", ph("सत्य-दर्शन से छोड़े जाने वाले मूलों वाली"), ph("सत्य-दर्शन से छोड़े जाने वाले मूलों से रहित"))
pair("1-M2-86", ph("मानसिक अभ्यास से छोड़े जाने वाले मूलों वाली"), ph("मानसिक अभ्यास से छोड़े जाने वाले मूलों से रहित"))
pair("1-M2-87", ph("आरंभिक विचार वाली"), ph("आरंभिक विचार से रहित"))
pair("1-M2-88", ph("सतत विचार वाली"), ph("सतत विचार से रहित"))
pair("1-M2-89", ph("उल्लास वाली"), ph("उल्लास से रहित"))
pair("1-M2-90", ph("उल्लास के साथ होने वाली"), ph("उल्लास के साथ न होने वाली"))
pair("1-M2-91", ph("सुख के साथ होने वाली"), ph("सुख के साथ न होने वाली"))
pair("1-M2-92", ph("समभाव के साथ होने वाली"), ph("समभाव के साथ न होने वाली"))
pair("1-M2-93", ph("इंद्रिय-सुखों के लोक से संबंधित"), ph("इंद्रिय-सुखों के लोक से संबंधित न होने वाली"))
pair("1-M2-94", ph("सूक्ष्म भौतिक लोक से संबंधित"), ph("सूक्ष्म भौतिक लोक से संबंधित न होने वाली"))
pair("1-M2-95", ph("अभौतिक लोक से संबंधित"), ph("अभौतिक लोक से संबंधित न होने वाली"))
pair("1-M2-96", ph("अस्तित्व के लोकों में समाई हुई"), ph("अस्तित्व के लोकों में न समाई हुई"))
pair("1-M2-97", ph("मुक्ति की ओर ले जाने वाली"), ph("मुक्ति की ओर न ले जाने वाली"))
pair("1-M2-98", ph("निश्चित"), ph("अनिश्चित"))
pair("1-M2-99", ph("सर्वोच्च न होने वाली"), ph("सर्वोच्च"))
pair("1-M2-100", ph("संघर्ष वाली"), ph("संघर्ष से रहित"), PIT, ABHI_DUKA)

# Pairs from the discourses
m["1-M-2-14-0"] = [f"##### {SUTTA_DUKA}"]
pair("1-M2-101", ph("विद्या की भागी"), ph("अज्ञान की भागी"))
pair("1-M2-102", ph("बिजली जैसी"), ph("वज्र जैसी"))
pair("1-M2-103", ph("मूर्खतापूर्ण"), ph("बुद्धिमत्तापूर्ण"))
pair("1-M2-104", ph("काली"), ph("उजली"))
pair("1-M2-105", ph("संताप देने वाली"), ph("संताप न देने वाली"))
pair("1-M2-106", ph("नाम रूपी"), ph("नाम के मार्ग रूपी"))
pair("1-M2-107", ph("अभिव्यक्ति रूपी"), ph("अभिव्यक्ति के मार्ग रूपी"))
pair("1-M2-108", ph("नामकरण रूपी"), ph("नामकरण के मार्ग रूपी"))
pair("1-M2-109", "मानसिक पक्ष", "भौतिक रूप")
pair("1-M2-110", "अज्ञान", "अस्तित्व की तृष्णा")
pair("1-M2-111", "अस्तित्व की दृष्टि", "अनस्तित्व की दृष्टि")
pair("1-M2-112", "शाश्वतता की दृष्टि", "विनाश की दृष्टि")
pair("1-M2-113", "सीमित होने की दृष्टि", "असीम होने की दृष्टि")
pair("1-M2-114", "अतीत के बारे में दृष्टि", "भविष्य के बारे में दृष्टि")
pair("1-M2-115", "निर्लज्जता", "बुराई के प्रति निडरता")
pair("1-M2-116", "लज्जा", "बुराई का डर")
pair("1-M2-117", "सलाह न मानने की प्रवृत्ति", "बुरे मित्रों की संगति")
pair("1-M2-118", "सलाह मानने की प्रवृत्ति", "अच्छे मित्रों की संगति")
pair("1-M2-119", "दोषों के विषय में कुशलता", "दोषों से उबरने में कुशलता")
pair("1-M2-120", "ध्यान-अवस्थाओं के विषय में कुशलता", "ध्यान-अवस्थाओं से बाहर आने में कुशलता")
pair("1-M2-121", "तत्वों के विषय में कुशलता", "मनोयोग के विषय में कुशलता")
pair("1-M2-122", "इंद्रिय-क्षेत्रों के विषय में कुशलता", "परस्पर-आश्रित उत्पत्ति के विषय में कुशलता")
pair("1-M2-123", "संभव बातों के विषय में कुशलता", "असंभव बातों के विषय में कुशलता")
pair("1-M2-124", "सरलता", "कोमलता")
pair("1-M2-125", "सहनशीलता", "सौम्यता")
pair("1-M2-126", "मधुर व्यवहार", "आदर-सत्कार [वर्तनी-भेद (Ka.): paṭisandhāro ca]")
pair("1-M2-127", "इंद्रियों के द्वारों की रक्षा न करने की प्रवृत्ति", "भोजन में मात्रा के ज्ञान का अभाव")
pair("1-M2-128", "इंद्रियों के द्वारों की रक्षा करने की प्रवृत्ति", "भोजन में मात्रा का ज्ञान")
pair("1-M2-129", "सजगता की कमी", "स्पष्ट समझ का अभाव")
pair("1-M2-130", "सजगता", "स्पष्ट समझ")
pair("1-M2-131", "सोच-विचार का बल", "मानसिक अभ्यास का बल")
pair("1-M2-132", "शांति", "अंतर्दृष्टि")
pair("1-M2-133", "शांति का चिह्न", "तत्परता का चिह्न")
pair("1-M2-134", "तत्परता", "भटकाव का अभाव")
pair("1-M2-135", "सदाचार में विफलता", "दृष्टि में विफलता")
pair("1-M2-136", "सदाचार की संपन्नता", "दृष्टि की संपन्नता")
pair("1-M2-137", "सदाचार की शुद्धि", "दृष्टि की शुद्धि")
pair("1-M2-138", "दृष्टि की शुद्धि", "और अपनी दृष्टि के अनुरूप प्रयास")
pair("1-M2-139", "झकझोर देने वाली बातों से मन का झकझोरा जाना", "और झकझोरे गए व्यक्ति का उचित ढंग से किया गया प्रयास")
pair("1-M2-140", "हितकर परिघटनाओं से संतुष्ट न होना", "प्रयास में पीछे न हटना")
pair("1-M2-141", "विद्या", "मुक्ति")
pair("1-M2-142", "क्षय का ज्ञान", "उत्पन्न न होने का ज्ञान",
     f"{SUTTA_DUKA} [पाठभेद (Syā.): suttantamātikā]", "मूल सूची पूरी हुई")

# ------------------------------------------------------------------ chapter 2 opening: fixed strings
VAR = {
    "vir_ind": " [वर्तनी-भेद (Sī., Syā.): viriyindriyaṃ]",
    "vir_bal": " [वर्तनी-भेद (Sī., Syā.): viriyabalaṃ]",
    "kpas": " [वर्तनी-भेद (Syā.): kāyappassaddhi]",
    "cpas": " [वर्तनी-भेद (Syā.): cittappassaddhi]",
    "kuju": " [वर्तनी-भेद (Sī., Ka.): kāyujjukatā]",
    "cuju": " [वर्तनी-भेद (Sī., Ka.): cittujjukatā]",
}

# Factor names: Pāli, Hindi, gender of the Hindi predicate
F = {
    "phasso": ("संपर्क", "m"),
    "vedanā": ("अनुभूति", "f"),
    "saññā": ("पहचान", "f"),
    "cetanā": ("इरादा", "m"),
    "cittaṃ": ("मन", "m"),
    "vitakko": ("आरंभिक विचार", "m"),
    "vicāro": ("सतत विचार", "m"),
    "pīti": ("उल्लास", "m"),
    "sukhaṃ": ("सुख", "m"),
    "cittassekaggatā": ("मन की एकाग्रता", "f"),
    "saddhindriyaṃ": ("श्रद्धा की क्षमता", "f"),
    "vīriyindriyaṃ": ("उत्साह की क्षमता", "f"),
    "satindriyaṃ": ("सजगता की क्षमता", "f"),
    "samādhindriyaṃ": ("एकाग्रता की क्षमता", "f"),
    "paññindriyaṃ": ("प्रज्ञा की क्षमता", "f"),
    "manindriyaṃ": ("मन की क्षमता", "f"),
    "somanassindriyaṃ": ("प्रसन्नता की क्षमता", "f"),
    "jīvitindriyaṃ": ("जीवन-क्षमता", "f"),
    "sammādiṭṭhi": ("सही दृष्टि", "f"),
    "sammāsaṅkappo": ("सही संकल्प", "m"),
    "sammāvāyāmo": ("सही प्रयास", "m"),
    "sammāsati": ("सही सजगता", "f"),
    "sammāsamādhi": ("सही एकाग्रता", "f"),
    "saddhābalaṃ": ("श्रद्धा का बल", "m"),
    "vīriyabalaṃ": ("उत्साह का बल", "m"),
    "satibalaṃ": ("सजगता का बल", "m"),
    "samādhibalaṃ": ("एकाग्रता का बल", "m"),
    "paññābalaṃ": ("प्रज्ञा का बल", "m"),
    "hiribalaṃ": ("लज्जा का बल", "m"),
    "ottappabalaṃ": ("बुराई के डर का बल", "m"),
    "alobho": ("लोभ का अभाव", "m"),
    "adoso": ("द्वेष का अभाव", "m"),
    "amoho": ("मोह का अभाव", "m"),
    "anabhijjhā": ("लालच का अभाव", "m"),
    "abyāpādo": ("दुर्भावना का अभाव", "m"),
    "hirī": ("लज्जा", "f"),
    "ottappaṃ": ("बुराई का डर", "m"),
    "kāyapassaddhi": ("मानसिक काया की प्रशांति", "f"),
    "cittapassaddhi": ("मन की प्रशांति", "f"),
    "kāyalahutā": ("मानसिक काया का हल्कापन", "m"),
    "cittalahutā": ("मन का हल्कापन", "m"),
    "kāyamudutā": ("मानसिक काया की मृदुता", "f"),
    "cittamudutā": ("मन की मृदुता", "f"),
    "kāyakammaññatā": ("मानसिक काया की कार्य-योग्यता", "f"),
    "cittakammaññatā": ("मन की कार्य-योग्यता", "f"),
    "kāyapāguññatā": ("मानसिक काया की दक्षता", "f"),
    "cittapāguññatā": ("मन की दक्षता", "f"),
    "kāyujukatā": ("मानसिक काया का सीधापन", "m"),
    "cittujukatā": ("मन का सीधापन", "m"),
    "sati": ("सजगता", "f"),
    "sampajaññaṃ": ("स्पष्ट समझ", "f"),
    "samatho": ("शांति", "f"),
    "vipassanā": ("अंतर्दृष्टि", "f"),
    "paggāho": ("तत्परता", "f"),
    "avikkhepo": ("भटकाव का अभाव", "m"),
}

LIST_1_1 = [
    ("phasso", ""), ("vedanā", ""), ("saññā", ""), ("cetanā", ""), ("cittaṃ", ""), ("vitakko", ""), ("vicāro", ""),
    ("pīti", ""), ("sukhaṃ", ""), ("cittassekaggatā", ""), ("saddhindriyaṃ", ""), ("vīriyindriyaṃ", VAR["vir_ind"]),
    ("satindriyaṃ", ""), ("samādhindriyaṃ", ""), ("paññindriyaṃ", ""), ("manindriyaṃ", ""), ("somanassindriyaṃ", ""),
    ("jīvitindriyaṃ", ""), ("sammādiṭṭhi", ""), ("sammāsaṅkappo", ""), ("sammāvāyāmo", ""), ("sammāsati", ""),
    ("sammāsamādhi", ""), ("saddhābalaṃ", ""), ("vīriyabalaṃ", VAR["vir_bal"]), ("satibalaṃ", ""), ("samādhibalaṃ", ""),
    ("paññābalaṃ", ""), ("hiribalaṃ", ""), ("ottappabalaṃ", ""), ("alobho", ""), ("adoso", ""), ("amoho", ""),
    ("anabhijjhā", ""), ("abyāpādo", ""), ("sammādiṭṭhi", ""), ("hirī", ""), ("ottappaṃ", ""),
    ("kāyapassaddhi", VAR["kpas"]), ("cittapassaddhi", VAR["cpas"]), ("kāyalahutā", ""), ("cittalahutā", ""),
    ("kāyamudutā", ""), ("cittamudutā", ""), ("kāyakammaññatā", ""), ("cittakammaññatā", ""), ("kāyapāguññatā", ""),
    ("cittapāguññatā", ""), ("kāyujukatā", VAR["kuju"]), ("cittujukatā", VAR["cuju"]), ("sati", ""), ("sampajaññaṃ", ""),
    ("samatho", ""), ("vipassanā", ""), ("paggāho", ""), ("avikkhepo", ""),
]


def hoti(g):
    return "होता है" if g == "m" else "होती है"


# Opening of the wholesome-mind formula, fixed for reuse by later agents
Q_KUSALA = "हितकर परिघटनाएँ कौन-सी हैं?"
OPEN_KAMA = ("जिस समय इंद्रिय-सुखों के लोक से संबंधित हितकर मन उत्पन्न होता है, जो प्रसन्नता के साथ होने वाला और ज्ञान से जुड़ा होता है "
             "और जिसका विषय दृश्य रूप हो, या ध्वनि, या गंध, या स्वाद, या स्पर्श, या मन का विषय, या जिस किसी को भी वह विषय बनाए,")
CLOSE_OTHERS = "या उस समय जो भी अन्य परस्पर-आश्रित रूप से उत्पन्न अभौतिक परिघटनाएँ होती हैं"
CLOSE_KUSALA = "ये हितकर परिघटनाएँ हैं"
list_1_1 = ", ".join(f"{F[k][0]}{v} {hoti(F[k][1])}" for k, v in LIST_1_1)

# Synonym strings (Hindi). Variants are inserted only where that segment's Pāli has them.
TAJJA = "उसके अनुरूप मन की चेतना के तत्व के संपर्क से उत्पन्न"
SUKHA_TAIL = "मानसिक सुहावनापन, मानसिक सुख, मन के संपर्क से उत्पन्न सुहावना सुखद अनुभव, मन के संपर्क से उत्पन्न सुहावनी सुखद अनुभूति"
S = {
    "phasso": "संपर्क, छूना, भली-भाँति छूना, भली-भाँति छू चुका होना",
    "vedanā": f"{TAJJA} {SUKHA_TAIL}",
    "saññā": f"{TAJJA} पहचान, पहचानना, पहचान चुका होना",
    "cetanā_var": f"{TAJJA} इरादा, इरादा करना, इरादा कर चुका होना [पाठभेद (Syā.): sañcetayitattaṃ]",
    "cittaṃ": ("मन, मानस, मानसिक क्रिया, हृदय, उज्ज्वलता, मानस, मन का इंद्रिय-क्षेत्र, मन की क्षमता, चेतना, चेतना का समूह, "
               "उसके अनुरूप मन की चेतना का तत्व"),
    "vitakko": "सोचना, आरंभिक विचार, संकल्प, टिकाना, भली-भाँति टिकाना, मन को विषय की ओर ले जाना, सही संकल्प",
    "vicāro": "विचरण, सतत विचार, बार-बार सतत विचार, गहरा सतत विचार, मन का विषय से जुड़े रहना, लगातार निहारते रहना",
    "pīti": "उल्लास, आनंद, आनंदित होना, प्रमुदित होना, हर्ष, महाहर्ष, तृप्ति, उमंग, मन का खिल उठना",
    "sukhaṃ": SUKHA_TAIL,
    "samādhi": ("मन की स्थिरता, ठहराव, दृढ़ता, बिखराव का अभाव, भटकाव का अभाव, मन का न बिखरा होना, शांति, "
                "एकाग्रता की क्षमता, एकाग्रता का बल, सही एकाग्रता"),
    "saddhā": "श्रद्धा, श्रद्धा रखना, भरोसा करना, गहरी आस्था, श्रद्धा, श्रद्धा की क्षमता, श्रद्धा का बल",
    "sati": ("सजगता, बार-बार स्मरण, पुनः स्मरण, सजगता, याद रखना, धारण करना, उथला न होना, भूल न जाना, "
             "सजगता, सजगता की क्षमता, सजगता का बल, सही सजगता"),
    "paññā": ("प्रज्ञा, जानना, छानबीन, गहरी छानबीन, परिघटनाओं की छानबीन, पहचानना, भली-भाँति पहचानना, हर पहलू को पहचानना, "
              "पांडित्य, कुशलता, निपुणता, विवेक, चिंतन, परख, व्यापक बुद्धि, मेधा, मार्गदर्शक बुद्धि, अंतर्दृष्टि, स्पष्ट समझ, अंकुश, "
              "प्रज्ञा, प्रज्ञा की क्षमता, प्रज्ञा का बल, प्रज्ञा रूपी शस्त्र, प्रज्ञा रूपी महल, प्रज्ञा रूपी आलोक, प्रज्ञा रूपी आभा, "
              "प्रज्ञा रूपी दीपक, प्रज्ञा रूपी रत्न, मोह का अभाव, परिघटनाओं की छानबीन, सही दृष्टि"),
    "jīvita_var": "आयु, टिके रहना, चलते रहना, चलाए रखना, गतिशील रहना [वर्तनी-भेद (Sī.): irīyanā], बने रहना, पालन, जीवन, जीवन-क्षमता",
    "alobho": ("लोभ का अभाव, लोभ न करना, लोभ से भरा न होना, राग का अभाव, राग न करना, राग से भरा न होना, "
               "लालच का अभाव, लोभ का अभाव रूपी हितकर मूल"),
    "adoso": "द्वेष का अभाव, द्वेष न करना, द्वेष से भरा न होना{v}, दुर्भावना का अभाव, दुर्भावना न रखना, द्वेष का अभाव रूपी हितकर मूल",
    "vīriya": ("मानसिक रूप से उत्साह जगाना{v1}, आगे बढ़ना, प्रयत्न, उद्यम, प्रयास, जोश, लगन{v2}, शक्ति, धैर्य, "
               "ढीला न पड़ने वाला प्रयत्न, चाह न छोड़ना, भार न छोड़ना, भार को दृढ़ता से उठाए रखना, "
               "उत्साह, उत्साह की क्षमता, उत्साह का बल, सही प्रयास"),
    "passaddhi": "प्रशांति, पूरी प्रशांति{v1}, शांत होना, पूरी तरह शांत होना{v2}, पूरी तरह शांत हो चुका होना{v3}",
    "lahutā": "हल्कापन, जल्दी बदल पाना, सुस्ती का अभाव, जड़ता का अभाव",
    "mudutā": "मृदुता, कोमलता, कठोरता का अभाव, कड़ेपन का अभाव",
    "kammaññatā": "कार्य-योग्यता, कार्य-योग्य होना, कार्य-योग्य होने का भाव",
    "pāguññatā": "दक्षता, दक्ष होना, दक्ष होने का भाव",
    "ujukatā": "सीधाई, सीधापन, टेढ़ेपन का अभाव, वक्रता का अभाव, कुटिलता का अभाव",
}
S["adoso_plain"] = S["adoso"].replace("{v}", "")
S["adoso_var"] = S["adoso"].replace("{v}", " [वर्तनी-भेद (Syā.): adūsanā adūsitattaṃ]")
S["vīriya_plain"] = S["vīriya"].replace("{v1}", "").replace("{v2}", "")
S["vīriya_var"] = S["vīriya"].replace("{v1}", " [वर्तनी-भेद (Sī., Syā.): viriyārambho]").replace("{v2}", " [वर्तनी-भेद (Sī.): ussoḷhi]")
S["passaddhi_plain"] = S["passaddhi"].format(v1="", v2="", v3="")
S["passaddhi_var"] = S["passaddhi"].format(
    v1=" [वर्तनी-भेद (Sī., Syā.): paṭippassaddhi]",
    v2=" [वर्तनी-भेद (Sī., Syā.): paṭippassambhanā]",
    v3=" [वर्तनी-भेद (Sī., Syā.): paṭippassambhitattaṃ]",
)

HIRI = "जिस बात से लज्जा आनी चाहिए उससे लज्जा आना, बुरी हानिकर परिघटनाओं को अपनाने से लज्जा आना"
OTT = "जिस बात से डरना चाहिए उससे डरना, बुरी हानिकर परिघटनाओं को अपनाने से डरना"

K3 = "अनुभूति के समूह, पहचान के समूह और मानसिक रचनाओं के समूह"
K1 = "चेतना के समूह"


def question(x):
    name, g = F[x]
    verb = "होता" if g == "m" else "होती"
    return f"उस समय {name} क्या {verb} है?"


def answer_end(x, final="।"):
    name, g = F[x]
    return f"यह उस समय {name} {hoti(g)}{final}"


def d(x, string, final="।"):
    """Plain definition: Katamo … hoti? Yo tasmiṃ samaye S – ayaṃ tasmiṃ samaye X hoti."""
    return f"{question(x)} उस समय जो {string} है – {answer_end(x, final)}"


def dg(x, gen, g2, string):
    """Definition with a khandha genitive before the relative: K की/का जो S."""
    post = "की" if g2 == "f" else "का"
    return f"{question(x)} उस समय {gen} {post} जो {string} है – {answer_end(x)}"


s = {}
s["1-1-0"] = ["### मन की उत्पत्ति का अध्याय"]
s["1-1-1-0"] = ["#### इंद्रिय-सुखों के लोक से संबंधित हितकर मन"]
s["1-1-1-1-0"] = ["##### पदों का विश्लेषण"]
s["1-1"] = [f"{Q_KUSALA} {OPEN_KAMA} उस समय {list_1_1}; {CLOSE_OTHERS} – {CLOSE_KUSALA}।"]
s["1-2"] = [d("phasso", S["phasso"])]
s["1-3"] = [d("vedanā", S["vedanā"])]
s["1-4"] = [d("saññā", S["saññā"])]
s["1-5"] = [d("cetanā", S["cetanā_var"])]
s["1-6"] = [d("cittaṃ", S["cittaṃ"])]
s["1-7"] = [d("vitakko", S["vitakko"])]
s["1-8"] = [d("vicāro", S["vicāro"])]
s["1-9"] = [d("pīti", S["pīti"])]
s["1-10"] = [d("sukhaṃ", S["sukhaṃ"])]
s["1-11"] = [d("cittassekaggatā", S["samādhi"])]
s["1-12"] = [d("saddhindriyaṃ", S["saddhā"])]
s["1-13"] = [d("vīriyindriyaṃ", S["vīriya_var"])]
s["1-14"] = [d("satindriyaṃ", S["sati"])]
s["1-15"] = [d("samādhindriyaṃ", S["samādhi"])]
s["1-16"] = [d("paññindriyaṃ", S["paññā"])]
s["1-17"] = [d("manindriyaṃ", S["cittaṃ"])]
s["1-18"] = [d("somanassindriyaṃ", S["sukhaṃ"])]
s["1-19"] = [f"{question('jīvitindriyaṃ')} उन अभौतिक परिघटनाओं की जो {S['jīvita_var']} है – {answer_end('jīvitindriyaṃ')}"]
s["1-20"] = [d("sammādiṭṭhi", S["paññā"])]
s["1-21"] = [d("sammāsaṅkappo", S["vitakko"])]
s["1-22"] = [d("sammāvāyāmo", S["vīriya_plain"])]
s["1-23"] = [d("sammāsati", S["sati"])]
s["1-24"] = [d("sammāsamādhi", S["samādhi"])]
s["1-25"] = [d("saddhābalaṃ", S["saddhā"])]
s["1-26"] = [d("vīriyabalaṃ", S["vīriya_plain"])]
s["1-27"] = [d("satibalaṃ", S["sati"])]
s["1-28"] = [d("samādhibalaṃ", S["samādhi"])]
s["1-29"] = [d("paññābalaṃ", S["paññā"])]
s["1-30"] = [f"{question('hiribalaṃ')} उस समय {HIRI} – {answer_end('hiribalaṃ')}"]
s["1-31"] = [f"{question('ottappabalaṃ')} उस समय {OTT} – {answer_end('ottappabalaṃ')}"]
s["1-32"] = [d("alobho", S["alobho"])]
s["1-33"] = [d("adoso", S["adoso_var"], final="?")]
s["1-34"] = [d("amoho", S["paññā"] + ", मोह का अभाव रूपी हितकर मूल")]
s["1-35"] = [d("anabhijjhā", S["alobho"])]
s["1-36"] = [d("abyāpādo", S["adoso_plain"])]
s["1-37"] = [d("sammādiṭṭhi", S["paññā"])]
s["1-38"] = [f"{question('hirī')} उस समय {HIRI} – {answer_end('hirī')}"]
s["1-39"] = [f"{question('ottappaṃ')} उस समय {OTT} – {answer_end('ottappaṃ')}"]
s["1-40"] = [dg("kāyapassaddhi", K3, "f", S["passaddhi_var"])]
s["1-41"] = [dg("cittapassaddhi", K1, "f", S["passaddhi_plain"])]
s["1-42"] = [dg("kāyalahutā", K3, "m", S["lahutā"])]
s["1-43"] = [dg("cittalahutā", K1, "m", S["lahutā"])]
s["1-44"] = [dg("kāyamudutā", K3, "f", S["mudutā"])]
s["1-45"] = [dg("cittamudutā", K1, "f", S["mudutā"])]
s["1-46"] = [dg("kāyakammaññatā", K3, "f", S["kammaññatā"])]
s["1-47"] = [dg("cittakammaññatā", K1, "f", S["kammaññatā"])]
s["1-48"] = [dg("kāyapāguññatā", K3, "f", S["pāguññatā"])]
s["1-49"] = [dg("cittapāguññatā", K1, "f", S["pāguññatā"])]
s["1-50"] = [dg("kāyujukatā", K3, "f", S["ujukatā"])]
s["1-51"] = [dg("cittujukatā", K1, "f", S["ujukatā"])]
s["1-52"] = [d("sati", S["sati"])]
s["1-53"] = [d("sampajaññaṃ", S["paññā"])]
s["1-54"] = [d("samatho", S["samādhi"])]
s["1-55"] = [d("vipassanā", S["paññā"])]
s["1-56"] = [d("paggāho", S["vīriya_plain"])]
s["1-57"] = [
    d("avikkhepo", S["samādhi"]),
    f"{CLOSE_OTHERS} – {CLOSE_KUSALA}।",
    "पदों का विश्लेषण।",
    "पहला पाठ-खंड।",
]

# ------------------------------------------------------------------ formula file
FORMULAS = [
    ("Text frame and headings", [
        "Namo tassa bhagavato arahato sammāsambuddhassa = उन भगवान, अर्हत्, पूर्ण रूप से जागृत बुद्ध को नमन",
        "# Abhidhammapiṭake = # अभिधम्म पिटक में",
        "## Dhammasaṅgaṇīpāḷi = ## परिघटनाओं की गणना (mid-sentence: “परिघटनाओं की गणना”)",
        "### Mātikā = ### मूल सूची",
        f"#### Tikamātikā = #### {TIKA}",
        f"Tikamātikā. (closing line) = {TIKA}।",
        f"#### Dukamātikā = #### {DUKA}",
        f"##### Suttantikadukamātikā = ##### {SUTTA_DUKA}",
        f"Abhidhammadukamātikā. (closing line) = {ABHI_DUKA}।",
        "Mātikā niṭṭhitā. = मूल सूची पूरी हुई।",
        "##### Hetugocchakaṃ / Āsavagocchakaṃ / Saṃyojanagocchakaṃ / Ganthagocchakaṃ / Oghagocchakaṃ / Yogagocchakaṃ / Nīvaraṇagocchakaṃ / Parāmāsagocchakaṃ / Upādānagocchakaṃ / Kilesagocchakaṃ = ##### मूलों / मन के मैलों / बंधनों / गाँठों / बाढ़ों / जकड़नों / बाधाओं / ग़लत धारणा / आसक्ति / मन के क्लेशों का वर्ग (the closing line repeats the name with «।»)",
        f"##### Cūḷantaradukaṃ / Mahantaradukaṃ / Piṭṭhidukaṃ = ##### {CUL} / {MAH} / {PIT}",
        "### Cittuppādakaṇḍaṃ = ### मन की उत्पत्ति का अध्याय",
        "#### Kāmāvacarakusalaṃ = #### इंद्रिय-सुखों के लोक से संबंधित हितकर मन",
        "##### Padabhājanī = ##### पदों का विश्लेषण",
        "Padabhājanīyaṃ. (closing line) = पदों का विश्लेषण।",
        "Paṭhamabhāṇavāro. = पहला पाठ-खंड।",
    ]),
    ("Line labels, variants, punctuation", [
        "(Ka) / (Kha) / (Ga) = (क) / (ख) / (ग)",
        "[word (sī. syā.)] spelling only = [वर्तनी-भेद (Sī., Syā.): word]",
        "[word (syā.)] different word or wording = [पाठभेद (Syā.): word]",
        "…pe… = … (same spot)",
        "– (Pāli dash) = – (same spot, same count; never add one)",
        "neva X na Y (in names and sentences) = न X, न Y (normal Hindi commas; the termbase's comma-free terms are only its file format)",
        "X … Y in contrast (kho pana, ceva … na ca, in names and sentences) = X, पर Y",
        "bare vipāka/vipākā as a class of phenomena = कर्म-फल रूपी",
        "vipāka/vipākā after kusala/akusala = हितकर/हानिकर कर्म के फल रूपी …",
    ]),
    ("Question and answer frames", [
        f"Katame dhammā kusalā? = {Q_KUSALA}",
        "Katame dhammā X? = X परिघटनाएँ कौन-सी हैं? (X = the matrix name in 1-matika.md without «परिघटनाएँ» and without a variant bracket)",
        f"ime dhammā kusalā. = {CLOSE_KUSALA}।",
        "ime dhammā X. = ये X परिघटनाएँ हैं।",
        "Katame dhammā no cittasaṃsaṭṭhasamuṭṭhānā? (matrix form «ऐसी परिघटनाएँ जो …») = कौन-सी परिघटनाएँ मन से घुली-मिली और मन से उत्पन्न नहीं हैं?",
        "ime dhammā no cittasaṃsaṭṭhasamuṭṭhānā. = ये परिघटनाएँ मन से घुली-मिली और मन से उत्पन्न नहीं हैं।",
        "Yasmiṃ samaye … cittaṃ uppannaṃ hoti = जिस समय … मन उत्पन्न होता है",
        f"Yasmiṃ samaye kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti somanassasahagataṃ ñāṇasampayuttaṃ rūpārammaṇaṃ vā saddārammaṇaṃ vā gandhārammaṇaṃ vā rasārammaṇaṃ vā phoṭṭhabbārammaṇaṃ vā dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha, = {OPEN_KAMA}",
        "tasmiṃ samaye = उस समय",
        "tasmiṃ samaye X hoti, Y hoti, … = उस समय X होता/होती है, Y होता/होती है, … (verb agrees with each factor; gender in the factor table)",
        f"ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā = {CLOSE_OTHERS}",
        f"… – ime dhammā kusalā. = … – {CLOSE_KUSALA}।",
    ]),
    ("Definition formulas (chapter 2)", [
        "Katamo/Katamā/Katamaṃ tasmiṃ samaye X hoti? = उस समय X क्या होता है? (feminine X: क्या होती है?)",
        "Yo/Yā/Yaṃ tasmiṃ samaye S – = उस समय जो S है –",
        "ayaṃ/idaṃ tasmiṃ samaye X hoti. = यह उस समय X होता है। (feminine X: होती है।)",
        f"Yā tasmiṃ samaye vedanākkhandhassa saññākkhandhassa saṅkhārakkhandhassa S – = उस समय {K3} की जो S है – (masculine first noun of S: का जो)",
        f"Yā tasmiṃ samaye viññāṇakkhandhassa S – = उस समय {K1} की जो S है – (masculine first noun of S: का जो)",
        "Yo tesaṃ arūpīnaṃ dhammānaṃ S – = उन अभौतिक परिघटनाओं की जो S है –",
        f"Yaṃ tasmiṃ samaye hirīyati hiriyitabbena hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā – = उस समय {HIRI} –",
        f"Yaṃ tasmiṃ samaye ottappati ottappitabbena ottappati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā – = उस समय {OTT} –",
        "alobho/adoso/amoho kusalamūlaṃ = लोभ/द्वेष/मोह का अभाव रूपी हितकर मूल",
    ]),
    ("Factor names (m = होता है, f = होती है)", [f"{k} = {v[0]} ({v[1]})" for k, v in F.items()]),
    ("Fixed synonym strings", [
        f"phasso phusanā saṃphusanā saṃphusitattaṃ = {S['phasso']}",
        f"tajjāmanoviññāṇadhātusamphassajaṃ cetasikaṃ sātaṃ cetasikaṃ sukhaṃ cetosamphassajaṃ sātaṃ sukhaṃ vedayitaṃ cetosamphassajā sātā sukhā vedanā = {S['vedanā']}",
        f"cetasikaṃ sātaṃ cetasikaṃ sukhaṃ cetosamphassajaṃ sātaṃ sukhaṃ vedayitaṃ cetosamphassajā sātā sukhā vedanā = {S['sukhaṃ']}",
        f"tajjāmanoviññāṇadhātusamphassajā saññā sañjānanā sañjānitattaṃ = {S['saññā']}",
        f"tajjāmanoviññāṇadhātusamphassajā cetanā sañcetanā cetayitattaṃ [sañcetayitattaṃ (syā.)] = {S['cetanā_var']}",
        f"cittaṃ mano mānasaṃ hadayaṃ paṇḍaraṃ mano manāyatanaṃ manindriyaṃ viññāṇaṃ viññāṇakkhandho tajjāmanoviññāṇadhātu = {S['cittaṃ']}",
        "mano inside this citta string only = मानस (the one place mano = मानस; everywhere else mano = मन)",
        f"takko vitakko saṅkappo appanā byappanā cetaso abhiniropanā sammāsaṅkappo = {S['vitakko']}",
        f"cāro vicāro anuvicāro upavicāro cittassa anusandhānatā anupekkhanatā = {S['vicāro']}",
        f"pīti pāmojjaṃ āmodanā pamodanā hāso pahāso vitti odagyaṃ attamanatā cittassa = {S['pīti']}",
        f"cittassa ṭhiti saṇṭhiti avaṭṭhiti avisāhāro avikkhepo avisāhaṭamānasatā samatho samādhindriyaṃ samādhibalaṃ sammāsamādhi = {S['samādhi']}",
        f"saddhā saddahanā okappanā abhippasādo saddhā saddhindriyaṃ saddhābalaṃ = {S['saddhā']}",
        f"cetasiko vīriyārambho nikkamo parakkamo uyyāmo vāyāmo ussāho ussoḷhī thāmo dhiti asithilaparakkamatā anikkhittachandatā anikkhittadhuratā dhurasampaggāho vīriyaṃ vīriyindriyaṃ vīriyabalaṃ sammāvāyāmo = {S['vīriya_plain']}",
        f"sati anussati paṭissati sati saraṇatā dhāraṇatā apilāpanatā asammussanatā sati satindriyaṃ satibalaṃ sammāsati = {S['sati']}",
        f"paññā pajānanā vicayo pavicayo dhammavicayo sallakkhaṇā upalakkhaṇā paccupalakkhaṇā paṇḍiccaṃ kosallaṃ nepuññaṃ vebhabyā cintā upaparikkhā bhūrī medhā pariṇāyikā vipassanā sampajaññaṃ patodo paññā paññindriyaṃ paññābalaṃ paññāsatthaṃ paññāpāsādo paññāāloko paññāobhāso paññāpajjoto paññāratanaṃ amoho dhammavicayo sammādiṭṭhi = {S['paññā']}",
        "… sammādiṭṭhi amoho kusalamūlaṃ (the amoho definition) = … सही दृष्टि, मोह का अभाव रूपी हितकर मूल",
        f"āyu ṭhiti yapanā yāpanā iriyanā [irīyanā (sī.)] vattanā pālanā jīvitaṃ jīvitindriyaṃ = {S['jīvita_var']}",
        f"alobho alubbhanā alubbhitattaṃ asārāgo asārajjanā asārajjitattaṃ anabhijjhā alobho kusalamūlaṃ = {S['alobho']}",
        f"adoso adussanā adussitattaṃ abyāpādo abyāpajjo adoso kusalamūlaṃ = {S['adoso_plain']}",
        f"passaddhi paṭipassaddhi passambhanā paṭipassambhanā paṭipassambhitattaṃ = {S['passaddhi_plain']}",
        f"lahutā lahupariṇāmatā adandhanatā avitthanatā = {S['lahutā']}",
        f"mudutā maddavatā akakkhaḷatā akathinatā = {S['mudutā']}",
        f"kammaññatā kammaññattaṃ kammaññabhāvo = {S['kammaññatā']}",
        f"paguṇatā paguṇattaṃ paguṇabhāvo = {S['pāguññatā']}",
        f"ujutā ujukatā ajimhatā avaṅkatā akuṭilatā = {S['ujukatā']}",
    ]),
]


def write_formulas():
    out = ["# pi-1 Dhammasaṅgaṇī: Hindi rails sentence formulas (read-only for chapter agents)", "",
           "Format: Pāli = Hindi, one per line. Generated by build_rails_sample.py. Copy the strings; do not retype them.", ""]
    for title, lines in FORMULAS:
        out.append(f"## {title}")
        out.append("")
        out.extend(lines)
        out.append("")
    (RAILS / "hi-rails-formulas.md").write_text("\n".join(out).rstrip("\n") + "\n", encoding="utf-8", newline="\n")
    print("wrote formulas", sum(len(l) for _, l in FORMULAS), "lines")


if __name__ == "__main__":
    os.makedirs(RAILS / "sample-2-01", exist_ok=True)
    emit(PALI / "preamble.md", preamble, OUT / "preamble.md")
    emit(PALI / "1-matika.md", m, OUT / "1-matika.md")
    emit(PIPE / "ch2-01-pali-1-122.md", s, RAILS / "sample-2-01" / "2-01-sample.md")
    write_formulas()
