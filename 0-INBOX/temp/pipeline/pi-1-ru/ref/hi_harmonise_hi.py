"""Consistency (harmonise) pass for the pi-1 Hindi plain zero-shot.

Applies fixed old -> new strings (a few regex patterns, marked rx=True, replacement may be a callable) to the
Hindi part files. A rule touches a Hindi line ONLY when the aligned Pāli line (non-empty line i <-> non-empty
line i) matches the rule's Pāli pattern, and only in the parts listed for it. Line counts, block IDs, heading
levels and dashes are never touched (asserted per changed line).
Protected (user-approved, never changed): preamble, 1-matika, the first 122 non-empty lines of 2-01.
Backup of the pre-pass files: backup-pre-harmonise/. Log: harmonise-log.tsv (rule, part, replacements, lines).
The pass reads from the backup, so it is idempotent: rerunning it rebuilds the same output.

usage: python -I -X utf8 harmonise_hi.py [--dry]
"""
import os, re, sys, collections

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PDIR = os.path.join(ROOT, r"AI_translation\pali\pi-1_split_chapters")
HDIR = os.path.join(ROOT, r"AI_translation\hindi\pi-1-hindi-plain-zeroshot_split_chapters")
HERE = os.path.join(ROOT, r"0-INBOX\temp\pipeline\pi-1-hi")
BAK = os.path.join(HERE, "backup-pre-harmonise")
PARTS = ["preamble", "1-matika", "2-01-cittuppadakandam", "2-02-cittuppadakandam", "2-03-cittuppadakandam",
         "2-04-cittuppadakandam", "2-05-cittuppadakandam", "3-01-rupakandam", "3-02-rupakandam", "3-03-rupakandam",
         "4-01-nikkhepakandam", "4-02-nikkhepakandam", "4-03-nikkhepakandam", "5-atthakathakandam"]
PROTECTED_PARTS = {"preamble", "1-matika"}
PROTECTED_2_01 = 122  # first 122 non-empty lines of 2-01 = approved sample

R = []  # (id, pali_regex, old, new, is_regex, parts_prefixes or None)


def rule(rid, pali, old, new, rx=False, parts=None):
    R.append((rid, pali, old, new, rx, parts))


# =============================================================== coordinator decisions (brief, step 2)
# 1. ^1-1-2-12-0 Appamāṇāni
rule("D1-appamana", r"Appamāṇāni", "असीम भाव", "अपरिमित रूपों पर विजय के आधार", parts=["2-02"])

# 2. sammappadhāna = सही परिश्रम (sammāvāyāma stays सही प्रयास; परिश्रम is unused elsewhere in pi-1)
rule("D2-sammappadhana", r"sammappadhān", "लोकोत्तर सही प्रयास का अभ्यास", "लोकोत्तर सही परिश्रम का अभ्यास", parts=["2-03", "2-05"])

# 3. viññatti = प्रकट अभिव्यक्ति (3-01/3-02/3-03, pi-5)
for a, b in [("शरीर द्वारा अभिव्यक्ति", "शरीर द्वारा प्रकट अभिव्यक्ति"), ("वाणी द्वारा अभिव्यक्ति", "वाणी द्वारा प्रकट अभिव्यक्ति")]:
    rule("D3-vinnatti", r"viññatt", a, b, parts=["4-02"])
for a, b in [("शारीरिक संकेत", "शरीर द्वारा प्रकट अभिव्यक्ति"), ("वाचिक संकेत", "वाणी द्वारा प्रकट अभिव्यक्ति")]:
    rule("D3-vinnatti", r"viññatt", a, b, parts=["5-"])

# 4. paṭipadā / adhipati qualifiers: the 2-03 / 2-05 clause shape everywhere («जो ध्यान … उच्च ज्ञान वाला है»,
#    «… की प्रधानता वाला»); khippābhiññā = शीघ्र
def _patipada(m):
    speed = "शीघ्र" if m.group(3) == "तीव्र" else "धीमे"
    return f"जो ध्यान {m.group(1)} प्रगति{m.group(2) or ''} और {speed} उच्च ज्ञान वाला है"


rule("D4-patipada", r"paṭipad", r"(दुःखद|सुखद) प्रगति( \[[^\]]*\])? और (धीमे|तीव्र) उच्च ज्ञान के साथ", _patipada, rx=True, parts=["2-02"])
# a run of adjacent paṭipadā items (…pe… between them) shares one «जो ध्यान … है», as in 2-03
rule("D4-patipada-run", r"bhiññaṃ ?…pe… ?(dukkha|sukha)paṭipadaṃ", r"उच्च ज्ञान वाला है( ?…) जो ध्यान ", r"उच्च ज्ञान वाला\1 ", rx=True, parts=["2-02"])
rule("D4-adhipati", r"dhipateyy", r"जिसमें (चाह|उत्साह|मन|जाँच-परख) प्रधान है", r"जो \1 की प्रधानता वाला है", rx=True, parts=["2-02"])

# 5. bhūmi (catūsu / tīsu bhūmīsu, X-bhūmiyaṃ) = स्तर; heading Tebhūmaka (2-02) untouched
rule("D5-bhumi", r"bhūmīsu", "चारों लोकों से संबंधित", "चारों स्तरों से संबंधित", parts=["5-"])
rule("D5-bhumi", r"bhūmīsu", "तीनों लोकों से संबंधित", "तीनों स्तरों से संबंधित", parts=["5-"])
rule("D5-bhumi", r"bhūmiyaṃ", " की भूमि में,", " के स्तर पर,", parts=["4-01"])
rule("D5-bhumi", r"bhūmiyaṃ", " वाली भूमि में,", " वाले स्तर पर,", parts=["4-01"])
rule("D5-bhumi", r"bhūmiyaṃ", " रहित भूमि में,", " रहित स्तर पर,", parts=["4-01"])
rule("D5-bhumi", r"bhūmiyaṃ", "लोकों में न समाई हुई हो,", "लोकों में न समाया हुआ हो,", parts=["4-01"])
# sphere qualifier after the level: 4-01 shape («A से संबंधित, B से संबंधित या C …»)
rule("D5-bhumi-spheres", r"bhūmiyaṃ", "से संबंधित हो, ", "से संबंधित, ", parts=["4-02"])
rule("D5-bhumi-spheres", r"bhūmiyaṃ", "से संबंधित हो या ", "से संबंधित या ", parts=["4-02"])

# 6. siglum bahūsu = (कई संस्करणों में)
rule("D6-bahusu", r"bahūsu", "(अनेक संस्करण)", "(कई संस्करणों में)", parts=["4-01"])

# 7. sārāga beside rāga = प्रबल राग (4-02; keeps गहरा for the pa-/sam- intensifiers padosa, paligedha, sammoha)
rule("D7-saraga", r"rāgo sārāgo", "गहरा राग", "प्रबल राग", parts=["4-01"])

# =============================================================== 8. other divergences (4-01 vs 4-02/4-03 and others)
# N. ellipsis spacing: Pāli 'X…pe… Y' -> Hindi 'X… Y' (4-01 had 'X … Y'); see main()
ELL = "N-ellipsis"

# B1 avasesa = शेष (pi-4/pi-5, 4-02, ch5)
rule("B1-avasesa", r"[Aa]vases", "छोड़कर बाकी", "छोड़कर शेष", parts=["4-01"])
rule("B1-avasesa", r"Avaseso lobho", "बाकी लोभ", "शेष लोभ", parts=["4-01"])

# B2 sphere list after a plural noun: 4-01 shape
rule("B2-spheres", r"kāmāvacarā, rūpāvacarā", "से संबंधित हों, ", "से संबंधित, ", parts=["4-02"])
rule("B2-spheres", r"kāmāvacarā, rūpāvacarā", "से संबंधित हों या ", "से संबंधित या ", parts=["4-02"])
rule("B2-spheres", r"rūpāvacarā arūpāvacarā", "से संबंधित हों, ", "से संबंधित, ", parts=["4-02"])
rule("B2-spheres", r"rūpāvacarā arūpāvacarā", "से संबंधित हों या ", "से संबंधित या ", parts=["4-02"])

# B3 'Tehi dhammehi ye dhammā …' frames: 4-01 shape
T = r"Tehi dhammehi ye dhammā"
rule("B3-tehi", T + r" sampayuttā(?!,? te dhamme)", "उन परिघटनाओं से जुड़ी परिघटनाएँ: ", "उन परिघटनाओं से जो परिघटनाएँ जुड़ी हैं, यानी ", parts=["4-02"])
rule("B3-tehi", T + r" vippayuttā(?! sāsavā)", "उन परिघटनाओं से अलग परिघटनाएँ: ", "उन परिघटनाओं से जो परिघटनाएँ अलग हैं, यानी ", parts=["4-02"])
rule("B3-tehi", T + r" sampayuttā,? te dhamme", "उन परिघटनाओं से जुड़ी परिघटनाओं में से उन परिघटनाओं को छोड़कर ",
     "उन परिघटनाओं से जो परिघटनाएँ जुड़ी हैं, उनमें से उन्हीं परिघटनाओं को छोड़कर, ", parts=["4-02"])
rule("B3-tehi", T + r" saṃkiliṭṭhā, te dhamme", "उन परिघटनाओं से मलिन परिघटनाओं में से उन परिघटनाओं को छोड़कर ",
     "उन परिघटनाओं के संबंध में जो परिघटनाएँ क्लेशों से मलिन हैं, उनमें से उन्हीं परिघटनाओं को छोड़कर, ", parts=["4-02"])
for pal, grp in [("nīvaraṇiyā", "बाधाओं"), ("upādāniyā", "आसक्ति"), ("parāmaṭṭhā", "ग़लत धारणा")]:
    rule("B3-tehi", T + rf" {pal}, te dhamme", "उन परिघटनाओं का विषय बनने वाली परिघटनाओं में से उन परिघटनाओं को छोड़कर शेष ",
         f"उन परिघटनाओं के संबंध में जो परिघटनाएँ {grp} का विषय बनती हैं, उनमें से उन्हीं परिघटनाओं को छोड़कर शेष, ", parts=["4-02"])
rule("B3-tehi", T + r" saṃkilesikā, te dhamme", "उन परिघटनाओं की ओर ले जाने वाली परिघटनाओं में से उन परिघटनाओं को छोड़कर शेष ",
     "उन परिघटनाओं के संबंध में जो परिघटनाएँ क्लेशों की ओर ले जाती हैं, उनमें से उन्हीं परिघटनाओं को छोड़कर शेष, ", parts=["4-02"])
rule("B3-tehi", T + r" vippayuttā sāsavā", r"उन परिघटनाओं से अलग, मन के मैलों का विषय बनने वाली (.*?) परिघटनाएँ, चाहे",
     r"उन परिघटनाओं से जो परिघटनाएँ अलग हैं और मन के मैलों का विषय बनने वाली \1 परिघटनाएँ हैं, चाहे", rx=True, parts=["4-02"])

# B4 tadekaṭṭha = उनके साथ रहने वाला/वाले (4-01), with «और» for «ca»
rule("B4-tadekattha", r"[Tt]adekaṭṭho", "उनके साथ-साथ रहने वाले लोभ", "उनके साथ रहने वाला लोभ", parts=["4-02"])
rule("B4-tadekattha", r"[Tt]adekaṭṭhā ca", r"(?<!और )उनके साथ-साथ रहने वाले(?= मन के क्लेश)", "और उनके साथ रहने वाले", rx=True, parts=["4-02"])
rule("B4-tadekattha", r"[Tt]adekaṭṭh", "उनके साथ-साथ रहने वाल", "उनके साथ रहने वाल", parts=["4-02"])

# B5 taṃsamuṭṭhānaṃ kāyakammaṃ, vacīkammaṃ, manokammaṃ (4-01 = pi-5)
rule("B5-kamma", r"taṃsamuṭṭhānaṃ kāyakammaṃ", "उनसे उत्पन्न शरीर का कर्म, वाणी का कर्म, मन का कर्म",
     "उनसे उत्पन्न शारीरिक कर्म, वाणी का कर्म, मानसिक कर्म", parts=["4-02"])

# B6 taṃsampayutto = उनसे जुड़ा (4-01)
rule("B6-tamsampayutta", r"[Tt]aṃsampayutt", "उससे जुड़ा", "उनसे जुड़ा", parts=["4-02"])

# B7 sīlabbata = सदाचार और व्रत (4-01: sīla = सदाचार, terms file; parāmāsa = ग़लत धारणा, matrix)
SILA = "सदाचार और व्रतों के बारे में ग़लत धारणा"
rule("B7-silabbata", r"sīlabbataparāmās|Sīlabbataparāmās", "कर्मकांडों और व्रतों से जुड़ी ग़लत धारणा", SILA, parts=["4-02"])
rule("B7-silabbata", r"sīlabbataparāmās|Sīlabbataparāmās", "कर्मकांडों और व्रतों से चिपकाव", SILA, parts=["5-"])
rule("B7-silabbata", r"sīlabbatupādān", "कर्मकांडों और व्रतों के प्रति आसक्ति", "सदाचार और व्रतों के प्रति आसक्ति", parts=["4-02"])
rule("B7-silabbata", r"sīlabbatupādān", "कर्मकांडों और व्रतों की आसक्ति", "सदाचार और व्रतों के प्रति आसक्ति", parts=["5-"])
rule("B7-silabbata", r"sīlena suddhi",
     "इस शिक्षा के बाहर के श्रमणों और ब्राह्मणों का यह मत कि “कर्मकांड से शुद्धि होती है, व्रत से शुद्धि होती है, कर्मकांड और व्रत से शुद्धि होती है”",
     "इस शिक्षा से बाहर के श्रमण और ब्राह्मण मानते हैं कि “सदाचार से शुद्धि होती है, व्रत से शुद्धि होती है, सदाचार और व्रत से शुद्धि होती है”",
     parts=["4-02"])

# B8 diṭṭhi in the defilement lists = दृष्टि (terms file; 4-01/4-02), diṭṭhigata stays ग़लत दृष्टि
rule("B8-ditthi", r"diṭṭhāsav", "ग़लत दृष्टि का मैल", "दृष्टि का मैल", parts=["5-"])
rule("B8-ditthi", r"[Dd]iṭṭhisaṃyojan", "ग़लत दृष्टि का बंधन", "दृष्टि का बंधन", parts=["5-"])
rule("B8-ditthi", r"kilesavatthūni", "अहंकार, ग़लत दृष्टि, संशय", "अहंकार, दृष्टि, संशय", parts=["5-"])
rule("B8-ditthi", r"kilesavatthūni", "। ग़लत दृष्टि ग़लत दृष्टि से जुड़ी", "। दृष्टि ग़लत दृष्टि से जुड़ी", parts=["5-"])
# upādāna list = «… के प्रति आसक्ति» (4-02)
for a, b in [("इंद्रिय-सुखों की आसक्ति", "इंद्रिय-सुखों के प्रति आसक्ति"), ("ग़लत दृष्टि की आसक्ति", "दृष्टियों के प्रति आसक्ति"),
             ("आत्मा के सिद्धांत की आसक्ति", "आत्मा के सिद्धांत के प्रति आसक्ति")]:
    rule("B8-upadana", r"kāmupādān|diṭṭhupādān", a, b, parts=["5-"])

# B9 thina = आलस्य (pi-4; 4-02, more occurrences) rather than pi-5 सुस्ती (ch5)
rule("B9-thina", r"[Tt]hinamiddh", "सुस्ती और तंद्रा", "आलस्य और तंद्रा", parts=["5-"])
rule("B9-thina", r"kilesavatthūni", "संशय, सुस्ती, बेचैनी", "संशय, आलस्य, बेचैनी", parts=["5-"])
rule("B9-thina", r"Thinaṃ sasaṅkhārikesu", "। सुस्ती प्रेरणा सहित होने वाले हानिकर मनों में उत्पन्न होती है।",
     "। आलस्य प्रेरणा सहित होने वाले हानिकर मनों में उत्पन्न होता है।", parts=["5-"])

# B10 «वे ही X, X रूपी भी …» (4-01 comma)
for h, x in [("बाधाएँ", "बाधा"), ("मन के क्लेश", "मन के क्लेश"), ("मन के मैल", "मन के मैल"), ("बंधन", "बंधन"),
             ("गाँठें", "गाँठ"), ("आसक्तियाँ", "आसक्ति"), ("बाढ़ें", "बाढ़"), ("जकड़नें", "जकड़न")]:
    rule("B10-teva", r"(Tāneva|Teyeva|Teva) ", f"वे ही {h} {x} रूपी भी", f"वे ही {h}, {x} रूपी भी", parts=["4-02", "4-03", "5-"])

# B11 kabaḷīkāro āhāro = कौर-कौर खाया जाने वाला भोजन (3-02/3-03/4-02, pi-5)
rule("B11-kabalikara", r"kabaḷīkāro āhāro", "कौर-कौर खाया जाने वाला आहार", "कौर-कौर खाया जाने वाला भोजन", parts=["5-"])

# B12 sekkhā (4-01, keeps the Pāli comma) / asekkhā (ch5, no added «यानी»)
rule("B12-sekkha", r"heṭṭhimāni ca tīṇi", "चार मार्ग और श्रमण-जीवन के निचले तीन फल", "चार मार्ग, और श्रमण-जीवन के तीन निचले फल", parts=["5-"])
rule("B12-asekkha", r"Upariṭṭhimaṃ", "सबसे ऊपर का [पाठभेद (Syā.): uparimaṃ] फल, यानी अर्हत्-पद का फल",
     "सबसे ऊँचा [पाठभेद (Syā.): uparimaṃ] फल, अर्हत्-पद का फल", parts=["4-01"])

# B13 Cittaṃ na vattabbaṃ – ch5 frame («… को कहा नहीं जा सकता – न …, न …»), used for every na vattabbā in ch5
rule("B13-vattabba", r"Cittaṃ na vattabbaṃ", "मन के बारे में यह नहीं कहना चाहिए – न यह कि वह “मन से जुड़ा” है, न यह कि वह “मन से अलग” है।",
     "मन को कहा नहीं जा सकता – न मन से जुड़ा, न मन से अलग।", parts=["4-02"])
rule("B13-vattabba", r"Cittaṃ na vattabbaṃ", "मन के बारे में यह नहीं कहना चाहिए – न यह कि वह “मन से घुला-मिला” है, न यह कि वह “मन से घुला-मिला नहीं” है।",
     "मन को कहा नहीं जा सकता – न मन से घुला-मिला, न मन से घुला-मिला न होने वाला।", parts=["4-02"])

# B14 ānantarika kamma (4-02 = pi-4)
rule("B14-anantarika", r"ānantarik", "तत्काल फल देने वाले पाँच घोर कर्म", "अगले ही जन्म में निश्चित फल देने वाले पाँच कर्म", parts=["4-01"])

# B15 'Yo S – ayaṃ vuccati X' frame = «जो S है – …» (terms file 3a; 4-02/4-03) instead of «जो <first> है, <rest> –»
rule("B15-frame", r"\? Yo (alobho|adoso|amoho|rāgo sārāgo|kāmesu|bhavesu)",
     r"(\? (?:[^?]*? के प्रति )?)जो ([^,\[]+?) है((?: \[[^\]]*\])?), (.*?) – इसे", r"\1जो \2\3, \4 है – इसे", rx=True, parts=["4-01"])

# B16 lobha string: 4-01 items, except nandī = आनंद, upakkilesa = मलिनता (pi-5)
rule("B16-lobha", r"rāgo sārāgo", "रस लेना, रस-भरा राग", "आनंद, आनंद और राग", parts=["4-01"])
rule("B16-lobha", r"rāgo sārāgo", ", दूषण,", ", मलिनता,", parts=["4-01"])
for a, b in [("झुकाव, अनुकूलता, आनंद", "झुकाव, अनुकूल होना, आनंद"),
             ("इच्छा, नशा, डूबे रहना, भूख, गहरी भूख,", "इच्छा, मूर्छा, चिपके रहना, लालसा, गहरी लालसा,"),
             ("सीने वाली, जाल बिछाने वाली", "सिलने वाली, जाल बुनने वाली"), ("धारा, उलझाने वाली", "धारा, फँसाने वाली"),
             ("अस्तित्व की ओर ले जाने वाली डोर", "अस्तित्व की डोर"),
             ("ललक, तीव्र ललक, अत्यधिक ललक, ललक, ललक रखना, ललक से भरा होना", "तड़प, गहरी तड़प, अत्यधिक तड़प, तड़प, तड़पना, तड़प से भरा होना"),
             ("अनुचित राग, अन्यायपूर्ण लोभ, रुचि, कामना, चाहना, ललचाना, गहरी चाहना", "अनैतिक राग, अनुचित लोभ, रुचि, गहरी कामना, कामना, ललक, प्रबल कामना"),
             ("निरोध की तृष्णा", "समाप्ति की तृष्णा"), (", ढक्कन,", ", पर्दा,")]:
    rule("B16-lobha", r"rāgo sārāgo", a, b, parts=["4-02"])

# B17 dosa intro and string (4-01)
for a, b in [("” यह सोचकर आक्रोश", "” इस विचार से आक्रोश"), ("अप्रिय और अनचाहे व्यक्ति", "अप्रिय और मन को न भाने वाले व्यक्ति"),
             ("या बिना कारण ही आक्रोश", "या बिना कारण भी आक्रोश")]:
    rule("B17-dosa", r"āghāto jāyati", a, b, parts=["4-02"])
for a, b in [("भारी प्रकोप", "तीव्र प्रकोप"), ("भारी द्वेष", "तीव्र द्वेष"), ("मन में द्वेष", "मन का द्वेष")]:
    rule("B17-dosa", r"āghāto paṭighāto", a, b, parts=["4-02"])

# B18 moha intro (4-01; paṭipadā = मार्ग, pi-4/pi-5)
rule("B18-moha", r"Dukkhe aññāṇaṃ", "के विषय में न जानना", "को न जानना", parts=["4-02"])
rule("B18-moha", r"Dukkhe aññāṇaṃ", "ले जाने वाले रास्ते को न जानना", "ले जाने वाले मार्ग को न जानना", parts=["4-02"])

# B19 kaṅkhā string and the Satthari intro (4-01; dveḷhaka spelled दुचित्तापन as 2-04)
KANKHA_TAIL = "किसी एक बात को पक्का न पकड़ पाना, हिचकिचाना, बार-बार हिचकिचाना"
rule("B19-kankha", r"kaṅkhāyanā", "दोचित्तापन", "दुचित्तापन", parts=["4-01"])
rule("B19-kankha", r"kaṅkhāyanā", "किसी एक बात को न पकड़ पाना, हिचकना, डगमगाना", KANKHA_TAIL, parts=["2-04"])
rule("B19-kankha", r"kaṅkhāyanā", "मति-भ्रम, संशय, दुविधा, दोराहा", "दुविधा, संशय, दुचित्तापन, दोराहा", parts=["4-02"])
rule("B19-kankha", r"kaṅkhāyanā|manovilekho", "किसी एक बात पर न टिक पाना, डगमगाना, बार-बार डगमगाना", KANKHA_TAIL, parts=["4-02"])
rule("B19-kankha", r"kaṅkhāyanā|manovilekho", "मन की जड़ता, मन को कुरेदना", "मन का जड़ हो जाना, मन की खरोंच", parts=["4-02"])
rule("B19-kankha", r"Satthari kaṅkhati", "कोई व्यक्ति गुरु के विषय में", "कोई गुरु के विषय में", parts=["4-02"])
rule("B19-kankha", r"Satthari kaṅkhati", "के विषय में शंका और संशय करता है", "के बारे में शंका करता है, संशय करता है", parts=["4-02"])

# B20 diṭṭhi string: gāho paṭiggāho / patiṭṭhāho = पकड़, कसकर पकड़ना (pi-4 ^4-62, 4-01, 2-04)
rule("B20-ditthi", r"diṭṭhigataṃ", "पकड़, अड़ जाना,", "पकड़, कसकर पकड़ना,", parts=["4-02"])

# B21 kāma / bhava strings (4-01; kāmanandī = आनंद after nandī)
rule("B21-kama", r"Yo kāmesu", "इंद्रिय-सुखों में रस लेना", "इंद्रिय-सुखों का आनंद", parts=["4-01"])
rule("B21-kama", r"Yo bhavesu", "अस्तित्व में रस लेना", "अस्तित्व का आनंद", parts=["4-01"])
for a, b in [("इंद्रिय-सुखों की जलन", "इंद्रिय-सुखों का ताप"), ("इंद्रिय-सुखों का नशा", "इंद्रिय-सुखों की मूर्छा"),
             ("इंद्रिय-सुखों में डूबे रहना", "इंद्रिय-सुखों से चिपके रहना")]:
    rule("B21-kama", r"Yo kāmesu", a, b, parts=["4-02"])
rule("B21-kama", r"Yo bhavesu", "अस्तित्वों के प्रति", "अस्तित्व के प्रति", parts=["4-03"])
rule("B21-kama", r"Yo bhavesu", "अस्तित्व में डूबे रहना", "अस्तित्व से चिपके रहना", parts=["4-03"])

# B22 māna string (4-01)
rule("B22-mana", r"Seyyohamasmīti", "स्वयं को कुछ मानना, स्वयं को कुछ मान बैठना, घमंड, अकड़, झंडा उठाना, स्वयं को ऊँचा रखना, मन की ध्वजा फहराने की चाह",
     "मान लेना, मान चुका होना, ऊँचा उठना, अकड़, झंडा, स्वयं को ऊपर उठाना, मन की झंडा फहराने की इच्छा", parts=["4-02"])

# B23 sakkāyadiṭṭhi body (4-01)
rule("B23-sakkaya", r"assutavā puthujjano",
     "इस संसार में कोई अशिक्षित साधारण व्यक्ति, जो आर्यों को नहीं देखता, आर्यों की शिक्षा से अनजान है, आर्यों की शिक्षा में अनुशासित नहीं है, जो सज्जनों को नहीं देखता, सज्जनों की शिक्षा से अनजान है, सज्जनों की शिक्षा में अनुशासित नहीं है,",
     "यहाँ कोई अशिक्षित साधारण व्यक्ति, जिसने आर्यों के दर्शन नहीं किए, जो आर्यों की शिक्षा में निपुण नहीं और आर्यों की शिक्षा में प्रशिक्षित नहीं, जिसने सज्जनों के दर्शन नहीं किए, जो सज्जनों की शिक्षा में निपुण नहीं और सज्जनों की शिक्षा में प्रशिक्षित नहीं,",
     parts=["4-02"])
rule("B23-sakkaya", r"attato samanupassati", "को आत्मा मानता है", "को आत्मा के रूप में देखता है", parts=["4-02"])

# B25 sāsavā … vipākā (4-01 word order)
rule("B25-vipaka", r"Sāsavā kusalākusalānaṃ dhammānaṃ vipākā", "हितकर और हानिकर परिघटनाओं के, मन के मैलों का विषय बनने वाले कर्म-फल",
     "मन के मैलों का विषय बनने वाले, हितकर और हानिकर परिघटनाओं के कर्म-फल", parts=["4-02"])

# B26 rūpassa upacayo = वृद्धि (ch3, 4-02; ācaya = संचय in the matrix), rūpassa santati = धारा (ch3, ch5, pi-5)
rule("B26-rupa", r"rūpassa upacayo", "भौतिक रूप का संचय", "भौतिक रूप की वृद्धि", parts=["5-"])
rule("B26-rupa", r"rūpassa santati", "भौतिक रूप की निरंतरता", "भौतिक रूप की धारा", parts=["4-02"])

# B27 ye ca dhammā kiriyā neva kusalā nākusalā na ca kammavipākā (4-01)
rule("B27-kiriya", r"ye ca dhammā kiriyā", "; जो परिघटनाएँ केवल क्रिया हैं, न हितकर, न हानिकर, न कर्म-फल;",
     "; और वे परिघटनाएँ जो केवल क्रिया रूपी हैं, न हितकर हैं, न हानिकर, और न ही कर्म-फल रूपी;", parts=["4-02"])

# B28 kammassa katattā = कर्म किए जाने के कारण (pi-5 katattā; 4-01, ch5), verb «है» (ch3, ch5; no added «बना»)
rule("B28-katatta", r"kammassa katattā", "किए गए कर्म के कारण", "कर्म किए जाने के कारण", parts=["3-02", "3-03", "4-02"])
rule("B28-katatta", r"kammassa katattā(?! uppajjissati)", "कर्म किए जाने के कारण बना है", "कर्म किए जाने के कारण है", parts=["4-01"])
rule("B28-katatta", r"kammassa katattā", "कर्म किए जाने के कारण नहीं बना है", "कर्म किए जाने के कारण नहीं है", parts=["4-01"])
rule("B28-katatta", r"na kammassa katattā", "; जो भौतिक रूप कर्म किए जाने के कारण नहीं है;", "; और जो भौतिक रूप कर्म किए जाने के कारण नहीं है;", parts=["4-02"])

# B24 «X, Y के साथ, Z भी है और Z से जुड़ा/जुड़ी भी» (4-01: no closing «है»)
rule("B24-ceva", r"ceva \w*sampayutt|ñceva \w*sampayutt", r"(से जुड़(?:ा|ी|े) भी) है(?=[;,] | –)", r"\1", rx=True, parts=["4-02", "4-03"])


def nonempty_idx(lines):
    return [i for i, l in enumerate(lines) if l.strip()]


def dashes(t):
    return t.count("—") + t.count("–")


def main(dry=False):
    log = collections.defaultdict(lambda: [0, 0])  # (rid, part) -> [replacements, lines]
    changed_lines = collections.Counter()
    hit_idx = set()
    blocked = []
    comp = [(rid, re.compile(p), old, new, rx, parts) for rid, p, old, new, rx, parts in R]
    for part in PARTS:
        pl = [l for l in open(os.path.join(PDIR, part + ".md"), encoding="utf-8-sig").read().splitlines() if l.strip()]
        raw = open(os.path.join(BAK, part + ".md"), encoding="utf-8").read()
        bom = raw.startswith("\ufeff")
        text = raw.lstrip("\ufeff")
        assert "\r" not in text, part
        el = text.split("\n")
        idx = nonempty_idx(el)
        assert len(idx) == len(pl), (part, len(idx), len(pl))
        for k, li in enumerate(idx):
            p, e0 = pl[k], el[li]
            e = e0
            # N: ellipsis spacing
            if "…pe…" in p and not re.search(r"\s…pe…", p):
                n_e = re.subn(r"(?<=[^\s…]) …", "…", e)
                if n_e[1]:
                    e = n_e[0]
                    log[(ELL, part)][0] += n_e[1]; log[(ELL, part)][1] += 1
            for ri, (rid, pr, old, new, rx, parts) in enumerate(comp):
                if parts and not any(part.startswith(x) for x in parts):
                    continue
                if not pr.search(p):
                    continue
                if rx:
                    e2, n = re.subn(old, new, e)
                else:
                    n = e.count(old)
                    e2 = e.replace(old, new)
                if n:
                    e = e2
                    hit_idx.add(ri)
                    log[(rid, part)][0] += n
                    log[(rid, part)][1] += 1
            if e != e0:
                if part in PROTECTED_PARTS or (part.startswith("2-01") and k < PROTECTED_2_01):
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
        f.write("rule\tpart\treplacements\tlines\n")
        for (rid, part), (n, l) in sorted(log.items()):
            f.write(f"{rid}\t{part}\t{n}\t{l}\n")
    tot = collections.defaultdict(lambda: [0, 0])
    for (rid, part), (n, l) in log.items():
        tot[rid][0] += n; tot[rid][1] += l
    for rid in sorted(tot):
        print(f"{rid:24s} repl={tot[rid][0]:5d} lines={tot[rid][1]:5d}")
    print("lines changed per part:", dict(changed_lines), "total", sum(changed_lines.values()))
    if blocked:
        print("BLOCKED (protected lines a rule would have changed):", blocked)
    for ri, r in enumerate(R):
        if ri not in hit_idx:
            print("NO HIT:", r[0], "|", str(r[2])[:90])


if __name__ == "__main__":
    main(dry="--dry" in sys.argv)
