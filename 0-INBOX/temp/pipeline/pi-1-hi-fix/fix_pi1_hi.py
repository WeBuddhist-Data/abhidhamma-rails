"""Apply the verified error fixes to the Hindi pi-1 rails chapters (2026-11-27).

Source of the fixes: 0-INBOX/temp/language-priority/pi1-verify/ (verification, alignment and profile reviews).
Every rule has an expected count over the 14 chapter files; any mismatch aborts before anything is written.

usage: python3 -I fix_pi1_hi.py [--write]
Without --write it only checks the counts.
"""
import re, sys, glob, pathlib

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import vinnana  # noqa: E402

REPO = HERE.parents[3]
CH = REPO / "AI_translation/hindi/pi-1-hindi-plain-rails_split_chapters"
WRITE = "--write" in sys.argv

# (name, pattern, replacement, expected count, is_regex)
RULES = [
    ("idappaccayatā (doubt): two objects, not 'by the law'",
     "कार्य-कारण के नियम से परस्पर-आश्रित रूप से उत्पन्न परिघटनाओं के बारे में शंका",
     "कार्य-कारण के नियम के बारे में और कारणों पर आश्रित होकर उत्पन्न परिघटनाओं के बारे में शंका", 4, False),
    ("idappaccayatā (not knowing): two objects",
     "कार्य-कारण के नियम से परस्पर-आश्रित रूप से उत्पन्न परिघटनाओं को न जानना",
     "कार्य-कारण के नियम को और कारणों पर आश्रित होकर उत्पन्न परिघटनाओं को न जानना", 5, False),
    ("idappaccayatā (knowledge): two objects",
     "कार्य-कारण के नियम से परस्पर-आश्रित रूप से उत्पन्न परिघटनाओं का ज्ञान",
     "कार्य-कारण के नियम का और कारणों पर आश्रित होकर उत्पन्न परिघटनाओं का ज्ञान", 2, False),
    ("paṭiccasamuppanna: dependent on conditions, not 'mutually'",
     "परस्पर-आश्रित रूप से उत्पन्न", "कारणों पर आश्रित होकर उत्पन्न", 112, False),
    ("paṭiccasamuppāda", "परस्पर-आश्रित उत्पत्ति", "कारणों पर आश्रित उत्पत्ति", 3, False),
    ("sīlabbataparāmāsa: the wrong view that rules and vows bring purity (its own definition); parāmāsa stays ग़लत धारणा",
     "सदाचार और व्रतों के बारे में ग़लत धारणा", "नियमों और व्रतों को ही शुद्धि का मार्ग मानने की ग़लत धारणा", 30, False),
    ("appaṇihita headings: absence of aspirations", "इच्छाओं का अभाव", "आकांक्षाओं का अभाव", 4, False),
    ("appaṇihita headings (oblique)", "इच्छाओं के अभाव", "आकांक्षाओं के अभाव", 2, False),
    ("sīlabbatupādāna: rules and vows", "सदाचार और व्रतों के प्रति आसक्ति", "नियमों और व्रतों के प्रति आसक्ति", 8, False),
    ("the view 'sīlena suddhi, vatena suddhi, sīlabbatena suddhi': rules, same word as the compound",
     "शुद्धि सदाचार से होती है, व्रत से होती है, सदाचार और व्रत से होती है",
     "शुद्धि नियमों से होती है, व्रतों से होती है, नियमों और व्रतों से होती है", 6, False),
    ("sakkāyadiṭṭhi: no 'permanent' (that is sassatadiṭṭhi); all four modes of ^1-1007 (as, having, in, containing a self)",
     "स्थायी आत्मा की ग़लत दृष्टि", "पाँच समूहों के संबंध में आत्मा की ग़लत दृष्टि", 14, False),
    ("appaṇihita: without aspiration (इच्छा = चाह made 'desireless yet desire-dominated')",
     "इच्छा-रहित", "आकांक्षा-रहित", 76, False),
    ("siyā: modal 'in some cases', not temporal 'sometimes'", "कभी ", "कुछ स्थितियों में ", 52, False),
    ("mucchā: infatuation, not fainting", "मूर्छा", "मदहोशी", 9, False),
    ("assutavā: not having heard the teaching, not illiterate",
     "यहाँ अशिक्षित साधारण व्यक्ति", "यहाँ उपदेश से अनजान साधारण व्यक्ति", 4, False),
    ("anottappa: not fearing wrongdoing (निडरता reads as praise)",
     "बुराई के प्रति निडरता", "बुराई से न डरने की वृत्ति", 66, False),
    ("āghāta: resentment, not outcry", "आक्रोश", "रोष", 35, False),
    ("maññanā, maññitatta: conceit, not 'assume'",
     "मान लेना, मान चुका होना", "अपने को कुछ मानना, अपने को कुछ मान बैठना", 2, False),
    ("āsevanā: practising, not consuming", "निरंतर सेवन", "निरंतर आचरण", 2, False),
    ("dukkhapaṭipadā: painful/laborious, not 'sad'", "दुःखद प्रगति", "कष्टदायक प्रगति", 147, False),
    ("amanussasadda: every sound other than human speech (aṭṭhakathā on ^1-621), not 'inhumane' or only 'beings'",
     "अमानवीय प्राणियों की ध्वनि", "मनुष्येतर ध्वनि", 4, False),
    ("khārika: alkaline, not the same as 'salty'", r"(?<![ऀ-ॿ])खारा(?![ऀ-ॿ])", "क्षारीय", 4, True),
    ("nāma: includes the unconditioned, so not only 'mental'", "मानसिक पक्ष", "अभौतिक पक्ष", 5, False),
    ("paritta/appamāṇa jhāna and object, same quality: says which is which",
     r"(?<=[ ,…])(सीमित|अपरिमित) और \1 विषय वाला", r"स्वयं \1 और \1 विषय वाला", 40, True),
    ("paritta jhāna, appamāṇa object: 'itself limited, but with an unlimited object'",
     "सीमित और अपरिमित विषय वाला", "स्वयं सीमित, पर अपरिमित विषय वाला", 20, False),
    ("appamāṇa jhāna, paritta object", "अपरिमित और सीमित विषय वाला", "स्वयं अपरिमित, पर सीमित विषय वाला", 20, False),
    ("kamma-born list is closed: 'that is', not 'for example' (no dash: dash counts follow the Pāli)",
     "कर्म किए जाने के कारण है, जैसे", "कर्म किए जाने के कारण है, यानी", 22, False),
    ("kamma-born list (negative)", "कर्म किए जाने के कारण नहीं है, जैसे", "कर्म किए जाने के कारण नहीं है, यानी", 22, False),
    ("mind-born list", "मन से उत्पन्न है, जैसे", "मन से उत्पन्न है, यानी", 4, False),
    ("1-1050/1-1051 ajjhattaṃ paccattaṃ: grammatical Hindi",
     "के स्वयं में, अपनी, उनसे बँधी", "के भीतर की, उनकी अपनी, उन्हीं से बँधी", 2, False),
    ("nevasaññānāsaññā: अ-पहचान is not a Hindi word (oblique)", "न अ-पहचान के", "न पहचान के अभाव के", 6, False),
    ("nevasaññānāsaññā (before का)", "न अ-पहचान का", "न पहचान के अभाव का", 3, False),
    ("dukkhasahagata kāyaviññāṇa: one item, not two in the list",
     "दुःख के साथ होने वाला शरीर का विज्ञान", "शरीर से होने वाला वह विज्ञान जो दुःख के साथ होता है", 2, False),
    ("viññāṇa of a sense: X से होने वाला विज्ञान",
     r"(?<![\u0900-\u0963\u0971-\u097F-])(आँख|कान|नाक|जीभ|शरीर|मन) का विज्ञान(?![\u0900-\u0963\u0971-\u097F])",
     r"\1 से होने वाला विज्ञान", 40, True),
    ("viññāṇa of a sense, oblique: X से होने वाले विज्ञान",
     r"(?<![\u0900-\u0963\u0971-\u097F-])(आँख|कान|नाक|जीभ|शरीर|मन) के विज्ञान(?![\u0900-\u0963\u0971-\u097F])",
     r"\1 से होने वाले विज्ञान", 165, True),
    ("4th jhāna in the formless-object lines: oblique agreement (pre-existing)",
     "होने वाला चौथे ध्यान को", "होने वाले चौथे ध्यान को", 4, False),
    ("^1-1050/1-1051 upādiṇṇā: taken up, grasped (aṭṭhakathā: kammanibbattā vā hontu mā vā), not 'kamma-born'",
     "हर व्यक्ति की निजी और कर्म से उत्पन्न हैं", "हर व्यक्ति की निजी और ग्रहण की हुई हैं", 2, False),
    ("title heading with the book's name", "## परिघटनाओं की गणना ^1-0", "## धम्मसंगणी (परिघटनाओं की गणना) ^1-0", 1, False),
    ("colophon with the book's name", "“परिघटनाओं की गणना” ग्रंथ पूरा हुआ",
     "“धम्मसंगणी (परिघटनाओं की गणना)” ग्रंथ पूरा हुआ", 1, False),
]
VINNANA_EXPECTED = 515  # चेतना occurrences, all viññāṇa


def main():
    files = sorted(CH.glob("*.md"))
    assert len(files) == 14, len(files)
    texts = {f: f.read_text(encoding="utf-8") for f in files}
    orig = dict(texts)

    # 1. viññāṇa
    total_before = sum(t.count("चेतना") for t in texts.values())
    assert total_before == VINNANA_EXPECTED, f"चेतना count {total_before} != {VINNANA_EXPECTED}"
    agg = {}
    for f in files:
        texts[f], log = vinnana.convert(texts[f])
        for k, v in log.items():
            agg[k] = agg.get(k, 0) + v
    left = sum(t.count("चेतन") for t in texts.values())
    assert left == 0, f"चेतन left: {left}"
    print(f"viññāṇa: {total_before} चेतना -> विज्ञान; agreement: " +
          ", ".join(f"{k} {v}" for k, v in agg.items() if v))

    # 2. the other rules
    report = []
    for name, pat, rep, exp, is_re in RULES:
        n = 0
        for f in files:
            if is_re:
                texts[f], k = re.subn(pat, rep, texts[f])
            else:
                k = texts[f].count(pat)
                texts[f] = texts[f].replace(pat, rep)
            n += k
        status = "OK" if n == exp else "MISMATCH"
        report.append((status, n, exp, name))
        print(f"{status:8} {n:4d}/{exp:<4d} {name}")
    if any(r[0] != "OK" for r in report):
        sys.exit("aborted: a count differs; nothing written")

    changed = sum(1 for f in files if texts[f] != orig[f])
    print(f"files changed: {changed} of {len(files)}")
    if WRITE:
        for f in files:
            if texts[f] != orig[f]:
                f.write_text(texts[f], encoding="utf-8", newline="\n")
        print("written")
    else:
        print("dry run: use --write to apply")


if __name__ == "__main__":
    main()
