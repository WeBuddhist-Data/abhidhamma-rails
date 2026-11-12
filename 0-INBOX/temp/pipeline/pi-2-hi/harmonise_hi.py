"""Consistency (harmonise) pass for the pi-2 Hindi plain zero-shot (Vibhaṅga).

Applies fixed old -> new strings (some regex patterns, rx=True, replacement may be a callable) to the Hindi
chapter files. A rule touches a Hindi line ONLY when the aligned Pāli line (non-empty line i <-> non-empty line i)
matches the rule's Pāli pattern, only in the chapters listed for it, and (pp=True) only inside a
Pañhāpucchaka region (from the 'kati kusalā' question to the closing 'Pañhāpucchakaṃ.' / 'niṭṭhito' line).
Line counts, block IDs, heading levels, dashes and '[' counts are never touched (asserted per changed line).
Protected (user-approved, never changed): preamble.md and the first 77 non-empty lines of 1-khandhavibhango.md.
Backup of the pre-pass files: backup-pre-harmonise/. Log: harmonise-log.tsv (rule, chapter, replacements, lines).
The pass reads from the backup, so it is idempotent: rerunning it rebuilds the same output.

usage: python -I -X utf8 harmonise_hi.py [--dry]
"""
import os, re, sys, collections

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PDIR = os.path.join(ROOT, r"AI_translation\pali\pi-2_split_chapters")
HDIR = os.path.join(ROOT, r"AI_translation\hindi\pi-2-hindi-plain-zeroshot_split_chapters")
HERE = os.path.join(ROOT, r"0-INBOX\temp\pipeline\pi-2-hi")
BAK = os.path.join(HERE, "backup-pre-harmonise")
PARTS = ["preamble", "1-khandhavibhango", "2-ayatanavibhango", "3-dhatuvibhango", "4-saccavibhango",
         "5-indriyavibhango", "6-paticcasamuppadavibhango", "7-satipatthanavibhango", "8-sammappadhanavibhango",
         "9-iddhipadavibhango", "10-bojjhangavibhango", "11-maggangavibhango", "12-jhanavibhango",
         "13-appamannavibhango", "14-sikkhapadavibhango", "15-patisambhidavibhango", "16-nanavibhango",
         "17-khuddakavatthuvibhango", "18-dhammahadayavibhango"]
PROTECTED_PARTS = {"preamble"}
PROTECTED_CH1 = 77  # first 77 non-empty lines of chapter 1 = approved sample

R = []  # (id, pali_regex, old, new, is_regex, chapters or None, pp_only)


def ch(*nums):
    return [str(n) for n in nums]


def rule(rid, pali, old, new, rx=False, chs=None, pp=False):
    R.append((rid, pali, old, new, rx, chs, pp))


CUR = {}  # current chapter number (str), for callables

# ====================================================================================== brief, step 2, items 1-7
# 1. Suttanta definitions (ch4 Sacca, ch6 Paṭiccasamuppāda): one wording.
#    Frame from ch4 (singular sattanikāya as in the Pāli; the byasana phrase repeats «पीड़ित» for each phuṭṭhassa);
#    the synonym lists from ch6 (pi-1 conventions: -itattaṃ = «… से भरा होना», -tā = «… की अवस्था»,
#    the defined term inside its own list = मृत्यु).
rule("I1-sattanikaya", r"tamhi tamhi sattanikāye", "उन-उन प्राणी-वर्गों में", "उस-उस प्राणी-वर्ग में", chs=ch(6))
rule("I1-sattanikaya", r"tamhā tamhā sattanikāyā", "उन-उन प्राणी-वर्गों से", "उस-उस प्राणी-वर्ग से", chs=ch(6))
BYASANA_4 = ("संबंधियों की हानि से पीड़ित, धन-संपत्ति की हानि से पीड़ित, रोग की विपत्ति से पीड़ित, सदाचार की हानि से पीड़ित "
             "या दृष्टि की हानि से पीड़ित, किसी न किसी विपत्ति से घिरे, किसी न किसी दुःखद परिघटना से पीड़ित व्यक्ति का जो")
BYASANA_6 = ("रिश्तेदारों की हानि से, या धन-संपत्ति की हानि से, या रोग की विपत्ति से, या सदाचार की हानि से, या दृष्टि की हानि से "
             "प्रभावित व्यक्ति में, किसी न किसी विपत्ति से घिरे व्यक्ति में, किसी न किसी दुःखद परिघटना से प्रभावित व्यक्ति में जो")
rule("I1-byasana", r"Ñātibyasanena", BYASANA_6, BYASANA_4, chs=ch(6))
rule("I1-jati", r"jāti sañjāti okkanti", "जन्म, भली-भाँति जन्म, प्रवेश,", "जन्म, भली-भाँति जन्म, गर्भ में उतरना,", chs=ch(4))
rule("I1-marana", r"cuti cavanatā",
     "च्युत होना, चल बसना, टूट जाना, लुप्त हो जाना, मौत, मरना, देह छोड़ना, समूहों का बिखर जाना, शरीर का गिर जाना, जीवन-क्षमता का कट जाना",
     "गुज़र जाना, गुज़र जाने की अवस्था, टूटना, लुप्त हो जाना, मौत, मृत्यु, काल का पूरा होना, समूहों का टूटना, शरीर का त्याग, जीवन-क्षमता का कट जाना",
     chs=ch(4))
rule("I1-soka", r"soko socanā", "शोक, शोक करना, शोक में डूबे रहना,", "शोक, शोक करना, शोक से भरा होना,", chs=ch(4))
rule("I1-parideva", r"ādevo paridevo",
     "रोना, विलाप, रोना-धोना, विलाप करना, रोते रहना, विलाप करते रहना, बोल पड़ना, बड़बड़ाना, अनाप-शनाप बोलना, बिलखना, बिलख-बिलखकर रोना, बिलखते रहना",
     "रोना, विलाप, रोते रहना, विलाप करते रहना, रोने से भरा होना, विलाप से भरा होना, शब्दों की झड़ी, प्रलाप, बड़बड़ाना, बिलखना, बिलखते रहना, बिलखने से भरा होना",
     chs=ch(4))
rule("I1-upayasa", r"āyāso upāyāso", "परेशानी, निराशा, परेशान रहना, निराश रहना",
     "हताशा, निराशा, हताशा से भरा होना, निराशा से भरा होना", chs=ch(4))

# 2. dukkhanirodhagāminī paṭipadā = «… ले जाने वाला प्रगति का ढंग» (pi-1 rails 4-01/4-02, amoha and moha lists;
#    already in ch6, ch11, ch15, ch17); ch4 and ch16 had «… मार्ग» (pi-5).
rule("I2-patipada", r"[Nn]irodhagāmin", r"(अंत की ओर ले जाने) वाला मार्ग", r"\1 वाला प्रगति का ढंग", rx=True, chs=ch(4, 16))
rule("I2-patipada", r"[Nn]irodhagāmin", r"(अंत की ओर ले जाने) वाले मार्ग", r"\1 वाले प्रगति के ढंग", rx=True, chs=ch(4, 16))

# 3. Pañhāpucchaka frames: see the PP rules below.

# 4. niddesa headings / closings = «… की व्याख्या» (pi-1 3-01 «एकल वर्गीकरण की व्याख्या», ch16, ch17, pi-3)
rule("I4-niddesa", r"[Nn]iddeso", "शुरू होने वाला ", "शुरू होने वाली ", chs=ch(6))
rule("I4-niddesa", r"[Nn]iddeso", " का विवरण", " की व्याख्या", chs=ch(6, 7))

# 5. mātikā / ekaka … dasaka headings and closings: the pi-1 Rūpakaṇḍa scheme (= ch16):
#    Ekakaṃ = एकल वर्गीकरण, Dukaṃ = दो-दो के वर्गीकरण …; -mātikā = «… की मूल सूची», -niddeso = «… की व्याख्या»
HEAD = r"^#*\s*(Ekak|Duk|Tik|Catukk|Pañcak|Chakk|Sattak|Aṭṭhak|Navak|Dasak)(amātikā|aniddeso|aṃ\.)"
rule("I5-heads", HEAD, r"एकल प्रकारों की (मूल सूची|व्याख्या)", r"एकल वर्गीकरण की \1", rx=True, chs=ch(17))
rule("I5-heads", HEAD, r"(\S+-\S+) प्रकारों की (मूल सूची|व्याख्या)", r"\1 के वर्गीकरणों की \2", rx=True, chs=ch(17))
rule("I5-heads", HEAD, "एकल प्रकार।", "एकल वर्गीकरण।", chs=ch(17))
rule("I5-heads", HEAD, r"^(\S+-\S+) प्रकार।", r"\1 के वर्गीकरण।", rx=True, chs=ch(17))

# 6. upekkhā string: pi-1 has none -> majority (ch10 4 lines, notes 5/7/10/11) over ch12 (3 lines)
rule("I6-upekkha", r"upekkhanā ajjhupekkhanā", "उदासीन भाव से देखना, मन का संतुलन", "तटस्थ भाव से देखना, मन की तटस्थता", chs=ch(12))

# 7. akaniṭṭha = «अकनिष्ठ देवता» (pi-1 4-02 ^1-1287 ff.)
rule("I7-akanittha", r"[Aa]kaniṭṭh", "सबसे ऊँचे अकनिष्ठ", "अकनिष्ठ", chs=ch(18))

# ====================================================================================== 8. other divergences
# B1 sacca names: samudayasacca / maggasacca = pi-3 / pi-4 («दुःख की उत्पत्ति का सत्य», «दुःख के अंत के मार्ग का सत्य»; = ch18)
rule("B1-sacca", r"[Ss]amudayasacc", r"(?<!दुःख की )उत्पत्ति (का|के) सत्य", r"दुःख की उत्पत्ति \1 सत्य", rx=True, chs=ch(4))
rule("B1-sacca", r"[Mm]aggasacc", r"(?<!अंत के )मार्ग (का|के) सत्य", r"दुःख के अंत के मार्ग \1 सत्य", rx=True, chs=ch(4))

# B2 Tena vuccati "X"ti = «इसीलिए “X” कहा जाता है» (ch12, ch13, ch7 order; इसीलिए: 108 of 129 lines)
rule("B2-tena", r"Tena vuccati", r"इसलिए कहा जाता है, “([^”]*)”", r"इसीलिए “\1” कहा जाता है", rx=True)
rule("B2-tena", r"Tena vuccati", r"इसीलिए कहा जाता है “([^”]*)”", r"इसीलिए “\1” कहा जाता है", rx=True)
rule("B2-tena", r"Tena vuccati", r"इसलिए “([^”]*)” कहा जाता है", r"इसीलिए “\1” कहा जाता है", rx=True)

# B3 avasesā dhammā = «शेष परिघटनाएँ» (ch4, 8, 9, 12, 13, 14; pi-1 avasesa = शेष)
rule("B3-avasesa", r"Avasesā dhammā", "बाकी परिघटनाएँ", "शेष परिघटनाएँ", chs=ch(7, 10, 11))

# B4 iriyati vattati … string (ch12, ch13: 5 lines) over ch7 (2 lines)
rule("B4-iriyati", r"[Ii]riyati vattati",
     "गतिशील रहता है, बना रहता है, अपना पालन करता है, चलता रहता है, चलाए रखता है, विचरता है, रहता है",
     "चलता-फिरता है, आचरण करता है, स्वयं को बनाए रखता है, निभाता है, जीवन चलाता है, विचरता है, रहता है", chs=ch(7))

# B5 ātāpī sampajāno satimā vineyya loke abhijjhādomanassaṃ (ch7, ch11 over ch4; loka = लोक, ch12 notes)
rule("B5-atapi", r"ātāpī sampajāno satimā",
     "तत्पर, स्पष्ट समझ रखते हुए और सजग, संसार के प्रति लालच और उदासी को दूर करके",
     "उद्यमी, स्पष्ट समझ रखते हुए और सजग, लोक में लालच और उदासी को दूर करके", chs=ch(4))

# B6 veramaṇī items (ch4 = ch11 lines): adinnādāna / kāmesumicchācāra = pi-4 (= ch14); pisuṇā / pharusā = ch11
#    (closest to pi-4 «चुगली भरी बातें बोलने», «कठोर बातें बोलने»)
rule("B6-veramani", r"pisuṇāya vācāya veramaṇī", "चुगली से दूर रहना", "चुगली करने से दूर रहना", chs=ch(4))
rule("B6-veramani", r"pharusāya vācāya veramaṇī", "कठोर वाणी से दूर रहना", "कठोर वचन बोलने से दूर रहना", chs=ch(4))
rule("B6-veramani", r"adinnādānā veramaṇī", "न दी गई वस्तु लेने से दूर रहना", "बिना दी गई चीज़ लेने से दूर रहना", chs=ch(4))
rule("B6-veramani", r"adinnādānā veramaṇī", "जो न दिया गया हो, उसे लेने से दूर रहना", "बिना दी गई चीज़ लेने से दूर रहना", chs=ch(11))
rule("B6-veramani", r"kāmesumicchācārā veramaṇī", "काम-संबंधी ग़लत आचरण से दूर रहना", "इंद्रिय-सुखों में दुराचार से दूर रहना", chs=ch(11))

# B7 aṭṭhaṅgiko maggo = «आठ अंगों वाला मार्ग» (pi-1 2-03; ch11, ch17)
rule("B7-atthangika", r"[Aa]ṭṭhaṅgik", "आर्य अष्टांगिक मार्ग", "आठ अंगों वाला आर्य मार्ग", chs=ch(4))
rule("B7-atthangika", r"[Aa]ṭṭhaṅgik", "अष्टांगिक मार्ग", "आठ अंगों वाला मार्ग", chs=ch(4))

# B8 metti mettāyanā … = «मैत्री, मैत्री करना, …» (pi-1 4-01 ^1-1062, ch13); karuṇā the same
rule("B8-metti", r"metti mettāyanā", "मैत्री रखना", "मैत्री करना", chs=ch(3))
rule("B8-metti", r"karuṇā karuṇāyanā", "करुणा रखना", "करुणा करना", chs=ch(3))

# B9 upādānakkhandhā = «आसक्ति का विषय बनने वाले … समूह» (ch4, pi-1 upādāniya)
rule("B9-upadanakkhandha", r"upādānakkhandh", "आसक्ति के विषय बनने वाले", "आसक्ति का विषय बनने वाले", chs=ch(12))
rule("B9-upadanakkhandha", r"upādānakkhandh", "आसक्ति के पाँचों समूह", "आसक्ति का विषय बनने वाले पाँचों समूह", chs=ch(7))

# B10 body parts (ch7: 3 lines over ch3: 2 lines)
for a, b in [("अस्थि-मज्जा", "हड्डियों की मज्जा"), ("आँतों की बंधनी", "आँतों की मेखला"), ("पेट में पड़ा भोजन", "पेट का भोजन"),
             ("पिघली चर्बी", "वसा"), ("नाक का बलगम", "नाक का मैल")]:
    rule("B10-body", r"kesā lomā|pittaṃ semhaṃ", a, b, chs=ch(3))

# B11 the four paṭisambhidā (ch16 ^2-800 = ch15 ^2-718 …, 27 occurrences in ch15)
rule("B11-patisambhida", r"atthapaṭisambhidā, dhamme ñāṇaṃ",
     "परिघटना का ज्ञान परिघटना का विश्लेषणात्मक ज्ञान है", "परिघटनाओं का ज्ञान परिघटनाओं का विश्लेषणात्मक ज्ञान है", chs=ch(16))
rule("B11-patisambhida", r"dhammaniruttābhilāpe", "वहाँ परिघटना को व्यक्त करने वाली भाषा के उच्चारण का ज्ञान",
     "वहाँ परिघटनाओं की भाषा की अभिव्यक्ति का ज्ञान", chs=ch(16))
rule("B11-patisambhida", r"dhammapaṭisambhid", "परिघटना का विश्लेषणात्मक ज्ञान", "परिघटनाओं का विश्लेषणात्मक ज्ञान", chs=ch(16))
rule("B11-patisambhida", r"paṭibhānapaṭisambhid", "प्रत्युत्पन्न बुद्धि का विश्लेषणात्मक ज्ञान", "सूझ-बूझ का विश्लेषणात्मक ज्ञान", chs=ch(16))

# B12 yañca rūpaṃ anidassanaappaṭighaṃ dhammāyatanapariyāpannaṃ (ch2 ^2-167 = ch3 ^2-184)
rule("B12-yanca", r"yañca rūpaṃ anidassanaappaṭighaṃ", "और जो भौतिक रूप दिखाई न देने वाला", "वह भौतिक रूप जो दिखाई न देने वाला", chs=ch(3))

# B13 upeto hoti samupeto upāgato samupāgato upapanno sampanno samannāgato = ch8 wording
#     (samannāgata = युक्त, pi-5; = ch10, ch16), pronoun after the referent (उस- singular, उन- plural)
UP = "सुसज्जित होता है, भली-भाँति सुसज्जित, {p} तक पहुँचा हुआ, भली-भाँति पहुँचा हुआ, {o} पाया हुआ, {p}से संपन्न और {p}से युक्त होता है"
UPETO = r"upeto|Upeto|samannāgat"
rule("B13-upeto", UPETO, "युक्त, भली-भाँति युक्त, इस तक पहुँचा हुआ, भली-भाँति पहुँचा हुआ, इसे प्राप्त किए हुए, इससे संपन्न और इससे समन्वित होता है",
     UP.format(p="उस", o="उसे"), chs=ch(7))
rule("B13-upeto", UPETO, "युक्त… इससे समन्वित होता है", "सुसज्जित होता है… उससे युक्त होता है", chs=ch(7))
rule("B13-upeto", UPETO, "युक्त होता है, भली-भाँति युक्त होता है, उन तक पहुँचा हुआ, भली-भाँति पहुँचा हुआ, उनसे सुसज्जित, उनसे परिपूर्ण, उनसे संपन्न होता है",
     UP.format(p="उन", o="उन्हें"), chs=ch(9))
rule("B13-upeto", UPETO, "युक्त होता है… उनसे संपन्न होता है", "सुसज्जित होता है… उनसे युक्त होता है", chs=ch(9))


def _upeto12(m):
    before = m.string[max(0, m.string.rfind("।", 0, m.start())):m.start()]
    pl = " और इस " in before
    p = "उन" if pl else "उस"
    if m.group(1):  # full string
        return "सुसज्जित होता है, भली-भाँति सुसज्जित, {0} तक पहुँचा हुआ, भली-भाँति पहुँचा हुआ, {1} पाया हुआ, {0}से संपन्न और {0}से युक्त होता है".format(
            p, "उन्हें" if pl else "उसे")
    return f"सुसज्जित होता है… {p}से युक्त होता है"


rule("B13-upeto", UPETO, r"युक्त होता है(?:(, भली-भाँति युक्त, सहित, भली-भाँति सहित, संपन्न, परिपूर्ण, समन्वित)|(?:, भली-भाँति युक्त)?… समन्वित)",
     _upeto12, rx=True, chs=ch(12))
rule("B13-upeto", UPETO, "से समन्वित होकर", "से युक्त होकर", chs=ch(12))

# B14 chando chandikatā kattukamyatā kusalo dhammacchando (ch8: 4 lines over ch9: 3)
rule("B14-chanda", r"chando chandikatā", "चाह, चाहत रखना,", "चाह, चाहना,", chs=ch(9))

# B15 Ekavidhena X – phassasampayuttaṃ = «… – संपर्क से जुड़ा/जुड़ी है» (ch1, ch2, ch3)
rule("B15-phassa", r"– phassasampayutt", r"(– संपर्क से जुड़ी)(?=।)", r"\1 है", rx=True, chs=ch(5))

# B16 word-commentary frames: "X"ti <definition> = «“X”: <definition>» (ch12, ch13: 109 lines) over «“X” का अर्थ है …»
#     (ch9, ch16: 59); "X"ti. Tattha katamo …? = «“X”। यहाँ … क्या है?» (ch6, 7, 8: 39 lines) over «“X”: यहाँ …» (ch12, ch13)
rule("B16-gloss", r"ti\b", r"(“[^”]+”) का अर्थ है ", r"\1: ", rx=True, chs=ch(9, 16))
rule("B16-gloss", r"ti\. Tattha", r"”: (?=यहाँ [^?।]{0,60}(?:क्या|कौन))", "”। ", rx=True, chs=ch(12, 13))

# ====================================================================================== 3. Pañhāpucchaka frames
# PP1 ch9 elided verbs in siyā series: «कभी A, कभी B होते हैं» -> «कभी A होते हैं, कभी B होते हैं» (pi-1 ^1-1406)
VERB = re.compile(r" (होते हैं|होता है|होती हैं|होती है)")


def _siya_full(text):
    out = []
    for sent in re.split(r"(?<=।) ", text):
        segs = re.split(r", (?=कभी )", sent)
        for i in range(len(segs) - 1):
            s = segs[i]
            if s.lstrip().startswith("कभी ") or re.search(r"(^|\s)कभी ", s):
                tail = s[s.rfind("कभी "):]
                if "होत" in tail or "नहीं" in tail or "कहा जा सकता" in tail:
                    continue
                for nxt in segs[i + 1:]:
                    m = VERB.search(nxt)
                    if m:
                        segs[i] = s + " " + m.group(1)
                        break
        out.append(", ".join(segs))
    return " ".join(out)


rule("PP1-siya", r"\b[Ss]iyā\b", r"^.*$", lambda m: _siya_full(m.group(0)), rx=True, chs=ch(9), pp=True)

# PP2 no added subject on subjectless sentences (Pāli has none; ch8, 9, 12, 13): drop «ये» / «वे» at sentence start
#     (ch5, 7–15), «सभी क्षमताएँ» (ch5) and «पाँचों समूह» (ch1); drop «वे» before the kenaci frame (ch1–4, 15)
rule("PP2-subject", r".", r"(^|(?<=। ))(?<!”। )(?<!सकता। )(ये|वे) ", r"\1", rx=True, chs=ch(5, 7, 8, 9, 10, 11, 12, 13, 14, 15), pp=True)
rule("PP2-subject", r"^(?!.*[Ss]abb)", r"(^|(?<=। ))सभी क्षमताएँ ", r"\1", rx=True, chs=ch(5), pp=True)
rule("PP2-subject", r"^Sappaccayā, saṅkhatā\.", "पाँचों समूह ", "", chs=ch(1), pp=True)
rule("PP2-subject", r"siyā", r"(?<!”)(?<!सकता); ये (?=कभी )", "; ", rx=True, chs=ch(5), pp=True)
rule("PP2-subject", r"(?i)kenaci viññeyy",r"(?<=[;,] )(?:वे|सभी क्षमताएँ) (?=किसी एक प्रकार की चेतना से)", "", rx=True, pp=True)

# PP3 negation: one shape, «<positive label> नहीं है/हैं», «कभी <label> नहीं होता/होते/होती/होतीं»
#     (ch1, 3, 8, 12–15; pi-1 «… नहीं होतीं» for a label without its own negative); quoted labels and the
#     neither-nor / 'पर' compound labels keep the matrix wording
VMAP = {"होता है": "होता", "होते हैं": "होते", "होती है": "होती", "होती हैं": "होतीं", "है": "है", "हैं": "हैं"}
VEND = r"(?P<V>होता है|होते हैं|होती है|होती हैं|हैं|है)(?=[।,;…]|$)"


def _neg(m):
    V = VMAP[m.group("V")]
    if m.group("pre"):
        return f"{m.group('pre')} होने {m.group('v')} नहीं {V}"
    return f" नहीं {V}"


rule("PP3-neg", r".", r"(?P<pre> के साथ| साथ-साथ)? न होने (?P<v>वाला|वाले|वाली) " + VEND, _neg, rx=True, pp=True)
rule("PP3-neg", r".", r" न (?P<c>छोड़ा|छोड़े|छोड़ी) जाने (?P<v>वाला|वाले|वाली) " + VEND,
     lambda m: f" {m.group('c')} जाने {m.group('v')} नहीं {VMAP[m.group('V')]}", rx=True, pp=True)


def _vala(V):
    if CUR["ch"] == "5" or V.startswith("होती"):
        return "वाली"
    return "वाला" if V in ("है", "होता है") else "वाले"


rule("PP3-neg", r".", r"(छोड़े जाने वाले मूलों) से रहित " + VEND,
     lambda m: f"{m.group(1)} {_vala(m.group('V'))} नहीं {VMAP[m.group('V')]}", rx=True, pp=True)

# PP4 sahagata: the label «X के साथ होने वाला» kept (ch2, 4, 5, 7, 9–11, 13): «कभी X के साथ होने वाले होते हैं»,
#     «X के साथ होने वाले हैं», negated «… होने वाले नहीं होते / नहीं हैं» (ch1, 3, 8, 14, 15 had «… के साथ होते हैं»)
SAHA = r"((?:उल्लास|सुख|समभाव) के साथ) "


def _siya_ctx(m):
    s = m.string
    cut = max(s.rfind(x, 0, m.start()) for x in ("।", ",", ";", "…"))
    return "कभी " in s[cut + 1:m.start()]


def _saha_pos(m):
    V = m.group(2)
    v = {"होता": "वाला", "होते": "वाले", "होती": "वाली"}[V.split()[0]]
    if _siya_ctx(m):
        return f"{m.group(1)} होने {v} {V}"
    return f"{m.group(1)} होने {v} {V.split()[1]}"


def _saha_neg(m):
    V = m.group(2)
    v = {"होता": "वाला", "होते": "वाले", "होती": "वाली", "होतीं": "वाली"}[V]
    if _siya_ctx(m):
        return f"{m.group(1)} होने {v} नहीं {V}"
    return f"{m.group(1)} होने {v} नहीं {'है' if V in ('होता', 'होती') else 'हैं'}"


rule("PP4-sahagata", r"sahagat", SAHA + r"(होता है|होते हैं|होती है|होती हैं)", _saha_pos, rx=True, pp=True)
rule("PP4-sahagata", r"sahagat", SAHA + r"नहीं (होता|होते|होतीं|होती)(?=[।,;…]|$)", _saha_neg, rx=True, pp=True)

# PP5 compound labels as predicate: «B, पर स्वयं A रूपी नहीं हैं» (one predicate, no «हैं» after B: ch3, ch7, ch14);
#     anupādinnaanupādāniyā = «न कर्म से उत्पन्न, न आसक्ति का विषय बनने वाले हैं» (ch1–4, 7, 10–12, 18)
rule("PP5-compound", r"ceva na ca hetū", r"(मूल वाले|मूलों से जुड़े) हैं, पर स्वयं", r"\1, पर स्वयं", rx=True, pp=True)
rule("PP5-compound", r"nupādinnaanupādāniy", "न कर्म से उत्पन्न हैं, न आसक्ति का विषय बनने वाले",
     "न कर्म से उत्पन्न, न आसक्ति का विषय बनने वाले हैं", pp=True)

# PP6 na vattabbā pronouns: object «उन्हें» / «उसे», the clause after it «वे» / «वह» (ch1–4, 8, 14, 15; pi-1 ^1-1427
#     «वे … उन्हें»); pi-1 ^1-1389 «और उन्हें … भी नहीं कहा जा सकता» (ch18) already so
rule("PP6-pronoun", r"vattabb", r"(?<!\S)इन्हें(?=[^,।;]*कहा जा सकता)", "उन्हें", rx=True, pp=True)
rule("PP6-pronoun", r"vattabb", r"(?<!\S)इसे(?=[^,।;]*कहा जा सकता)", "उसे", rx=True, pp=True)
rule("PP6-pronoun", r"vattabb", r"((?:कहा जा सकता|”)[,।;] )ये ", r"\1वे ", rx=True, pp=True)
rule("PP6-pronoun", r"vattabb", r"((?:कहा जा सकता|”)[,।;] )यह ", r"\1वह ", rx=True, pp=True)

# PP7 kenaci viññeyyā, kenaci na viññeyyā = «… जाने जा सकने वाले भी हैं, … न जाने जा सकने वाले भी हैं»
#     (pi-1 ^1-1464 «… भी हैं»; ch1–4, 15); not the «atthi kenaci» classes («कुछ …»)
rule("PP7-kenaci", r"(?i)(?<!atthi )kenaci viññeyy",
     r"(?<!कुछ )(किसी एक प्रकार की चेतना से (?:न )?(?:जाने|जानी|जाना) जा सकने (?:वाले|वाली|वाला)) (हैं|है)(?=[,।;]|$)",
     r"\1 भी \2", rx=True)

# PP8 kati question: «… में से कितने हितकर हैं, कितने हानिकर हैं, …» (ch1–5, 7, 10, 11, 14, 15)
rule("PP8-kati", r"kati kusalā", r"(कितन[ेी] .*?)(?=, कितन[ेी] |…|\?)",
     lambda m: m.group(1) if m.group(1).endswith(" हैं") else m.group(1) + " हैं", rx=True, pp=True)


# ======================================================================================
def nonempty_idx(lines):
    return [i for i, l in enumerate(lines) if l.strip()]


def dashes(t):
    return t.count("—") + t.count("–")


def pp_set(pl):
    on, s = False, set()
    for k, p in enumerate(pl):
        if "kati kusalā" in p:
            on = True
        if on and not p.startswith("#"):
            s.add(k)
        if on and ("Pañhāpucchakaṃ" in p or "niṭṭhit" in p):
            on = False
    return s


def main(dry=False):
    log = collections.defaultdict(lambda: [0, 0])  # (rid, part) -> [replacements, lines]
    changed_lines = collections.Counter()
    hit_idx = set()
    blocked = []
    comp = [(rid, re.compile(p), (re.compile(old, re.M) if rx else old), new, rx, chs, pp)
            for rid, p, old, new, rx, chs, pp in R]
    for part in PARTS:
        pl = [l for l in open(os.path.join(PDIR, part + ".md"), encoding="utf-8-sig").read().splitlines() if l.strip()]
        raw = open(os.path.join(BAK, part + ".md"), encoding="utf-8").read()
        bom = raw.startswith("\ufeff")
        text = raw.lstrip("\ufeff")
        assert "\r" not in text, part
        el = text.split("\n")
        idx = nonempty_idx(el)
        assert len(idx) == len(pl), (part, len(idx), len(pl))
        num = part.split("-")[0]
        CUR["ch"] = num
        pps = pp_set(pl)
        for k, li in enumerate(idx):
            p, e0 = pl[k], el[li]
            e = e0
            for ri, (rid, pr, old, new, rx, chs, pp) in enumerate(comp):
                if chs and num not in chs:
                    continue
                if pp and k not in pps:
                    continue
                if not pr.search(p):
                    continue
                if rx:
                    e2, n = old.subn(new, e)
                    if e2 == e:
                        n = 0
                else:
                    n = e.count(old)
                    e2 = e.replace(old, new)
                if n:
                    e = e2
                    hit_idx.add(ri)
                    log[(rid, part)][0] += n
                    log[(rid, part)][1] += 1
            if e != e0:
                if part in PROTECTED_PARTS or (part.startswith("1-") and k < PROTECTED_CH1):
                    blocked.append((part, k))
                    continue
                assert dashes(e) == dashes(e0), (part, k, "dash count changed")
                assert re.findall(r"\^[\w-]+\s*$", e) == re.findall(r"\^[\w-]+\s*$", e0), (part, k, "block id")
                assert re.match(r"#*", e).group(0) == re.match(r"#*", e0).group(0), (part, k, "heading")
                assert e.count("[") == e0.count("["), (part, k, "brackets")
                el[li] = e
                changed_lines[part] += 1
        if not dry:
            out = ("\ufeff" if bom else "") + "\n".join(el)
            open(os.path.join(HDIR, part + ".md"), "w", encoding="utf-8", newline="\n").write(out)
    with open(os.path.join(HERE, "harmonise-log.tsv"), "w", encoding="utf-8") as f:
        f.write("rule\tchapter\treplacements\tlines\n")
        for (rid, part), (n, l) in sorted(log.items(), key=lambda kv: (kv[0][0], PARTS.index(kv[0][1]))):
            f.write(f"{rid}\t{part}\t{n}\t{l}\n")
    tot = collections.defaultdict(lambda: [0, 0])
    for (rid, part), (n, l) in log.items():
        tot[rid][0] += n; tot[rid][1] += l
    for rid in sorted(tot):
        print(f"{rid:22s} repl={tot[rid][0]:5d} lines={tot[rid][1]:5d}")
    print("lines changed per chapter:", dict(changed_lines), "total", sum(changed_lines.values()))
    if blocked:
        print("BLOCKED (protected lines a rule would have changed):", blocked)
    for ri, r in enumerate(R):
        if ri not in hit_idx:
            print("NO HIT:", r[0], "|", str(r[2])[:90])


if __name__ == "__main__":
    main(dry="--dry" in sys.argv)
