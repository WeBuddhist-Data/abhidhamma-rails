"""Cross-chapter alignment of the pi-2 Hindi rails chapters: identical Pāli -> one Hindi wording.

usage: python -I -X utf8 align_rails_pi2.py [--dry]
  --dry   apply nothing; print the per-rule counts and write align-preview.txt (before/after of every changed line)
Without --dry: backs up the 19 chapter files to backup-pre-align/ (only if not there yet), writes the changed
chapter files and align-log.tsv (rule, chapter, replacements, lines).

Every rule touches only Hindi lines (or sentences / comma-items of lines) whose ALIGNED Pāli line (sentence, item)
matches the rule's Pāli pattern. Line counts, block IDs, heading levels and dash counts are asserted unchanged.
preamble.md and the first 77 non-empty lines of 1-khandhavibhango.md (the approved sample) are never touched.
"""
import collections, os, re, shutil, sys

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PDIR = os.path.join(ROOT, r"AI_translation\pali\pi-2_split_chapters")
HDIR = os.path.join(ROOT, r"AI_translation\hindi\pi-2-hindi-plain-rails_split_chapters")
HERE = os.path.dirname(os.path.abspath(__file__))
BAK = os.path.join(HERE, "backup-pre-align")
DRY = "--dry" in sys.argv
SAMPLE_LINES = 77  # protected prefix of chapter 1 (non-empty lines)

CHAPTERS = ["1-khandhavibhango", "2-ayatanavibhango", "3-dhatuvibhango", "4-saccavibhango",
            "5-indriyavibhango", "6-paticcasamuppadavibhango", "7-satipatthanavibhango", "8-sammappadhanavibhango",
            "9-iddhipadavibhango", "10-bojjhangavibhango", "11-maggangavibhango", "12-jhanavibhango",
            "13-appamannavibhango", "14-sikkhapadavibhango", "15-patisambhidavibhango", "16-nanavibhango",
            "17-khuddakavatthuvibhango", "18-dhammahadayavibhango"]
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
SENT_P = re.compile(r"(?<=[.?])\s+")
SENT_H = re.compile(r"(?<=[।?])\s+")
ITEM_P = re.compile(r"((?<=[?.;:,])\s+|\s+[–—]\s+)")
ITEM_H = re.compile(r"((?<=[?।;:,])\s+|\s+[–—]\s+)")


def chno(name):
    return int(name.split("-")[0])


# ----------------------------------------------------------------------------------------------------------------
# rule kinds
# R(name, chapters, pali, old, new, scope="line"|"sentence"|"item", zone=None|"pp", rx=False)
#   chapters: None (all) or a set of chapter numbers; pali: regex searched in the aligned Pāli unit;
#   old/new: fixed strings (rx=True: regex + replacement template); a callable new(h) -> h for kind "F".
# ----------------------------------------------------------------------------------------------------------------
class R:
    def __init__(self, name, chapters, pali, old, new, scope="line", zone=None, rx=False, func=None):
        self.name, self.chapters, self.scope, self.zone = name, chapters, scope, zone
        self.pali = re.compile(pali)
        self.old, self.new, self.rx, self.func = old, new, rx, func
        self.orx = re.compile(old) if rx else None

    def apply(self, h):
        if self.func:
            nh = self.func(h)
            return nh, (0 if nh == h else 1)
        if self.rx:
            return self.orx.subn(self.new, h)
        n = h.count(self.old)
        return (h.replace(self.old, self.new), n) if n else (h, 0)


RULES = []


def rule(*a, **k):
    RULES.append(R(*a, **k))


# ================================================================================================================
# A. Pañhāpucchaka frames
# ================================================================================================================
DASH = {1, 2, 3, 4, 5}
# A1 question line: «कितने हितकर हैं, कितने हानिकर, … कितने संघर्ष वाले, कितने संघर्ष से रहित?» (ch7-13 shape)
rule("A1 kati-question (one हैं)", {1, 2, 4}, r"kati kusalā",
     "कितने हानिकर हैं, कितने नैतिक रूप से अनिर्धारित हैं… कितने संघर्ष वाले हैं, कितने संघर्ष से रहित हैं?",
     "कितने हानिकर, कितने नैतिक रूप से अनिर्धारित… कितने संघर्ष वाले, कितने संघर्ष से रहित?")
rule("A1 kati-question (one हैं)", {3, 14, 15}, r"kati kusalā",
     "कितने संघर्ष वाले हैं, कितने संघर्ष से रहित?", "कितने संघर्ष वाले, कितने संघर्ष से रहित?")
# A2 siyā na vattabba (dash): «कभी उसे/उन्हें नहीं कहा जा सकता – …» (ch1, ch3 and pi-1 rails ^1-1429 shape)
rule("A2 siyā na vattabba: drop «ऐसा होता है कि»", {2, 4}, r"siyā na vattabb",
     "कभी ऐसा होता है कि उसे नहीं कहा", "कभी उसे नहीं कहा", zone="pp")
rule("A2 siyā na vattabba: drop «ऐसा होता है कि»", {2, 4}, r"siyā na vattabb",
     "कभी ऐसा होता है कि उन्हें नहीं कहा", "कभी उन्हें नहीं कहा", zone="pp")
# A3 anaphoric pronoun after a stated subject: उसे/उन्हें (ch5 had इसे/इन्हें)
rule("A3 anaphoric pronoun उसे/उन्हें", {5}, r"siyā na vattabb", "कभी इसे नहीं कहा", "कभी उसे नहीं कहा", zone="pp")
rule("A3 anaphoric pronoun उसे/उन्हें", {5}, r"siyā na vattabb", "कभी इन्हें नहीं कहा", "कभी उन्हें नहीं कहा", zone="pp")
rule("A3 anaphoric pronoun उसे/उन्हें", {5}, r"na vattabb", ", इन्हें नहीं कहा जा सकता –", ", उन्हें नहीं कहा जा सकता –",
     zone="pp")
rule("A3 anaphoric pronoun उसे/उन्हें", {5}, r"na vattabb", ", इसे नहीं कहा जा सकता –", ", उसे नहीं कहा जा सकता –",
     zone="pp")
# A4 «S को नहीं कहा जा सकता – “A”, वे/वह (कभी) B …» (Pāli comma; ch2/ch3/ch4 shape)
rule("A4 na vattabba – A, B: «”, वे/वह»", {1}, r'"ti, (siyā|"|\w)', "”; वे कभी", "”, वे कभी", scope="sentence", zone="pp")
rule("A4 na vattabba – A, B: «”, वे/वह»", {1}, r'"ti, (siyā|"|\w)', "”; वह ", "”, वह ", scope="sentence", zone="pp")
rule("A4 na vattabba – A, B: «”, वे/वह»", {5}, r'"ti, siyā', "”, कभी ये ", "”, वे कभी ", scope="sentence", zone="pp")
rule("A4 na vattabba – A, B: «”, वे/वह»", {5}, r'"ti, ', "”, ये ", "”, वे ", scope="sentence", zone="pp")
rule("A4 na vattabba – A, B: «”, वे/वह»", {5}, r'"ti, ', "”, यह ", "”, वह ", scope="sentence", zone="pp")
# A5 no noun subject added where the Pāli has none; after «;» a resumptive «वे»
rule("A5 no added subject: «; वे» for a continuing subject", {2}, r"tipi; siyā", "”; इंद्रिय-क्षेत्र कभी", "”; वे कभी",
     scope="sentence", zone="pp")
rule("A5 no added subject: «; वे» for a continuing subject", {3}, r"tipi; siyā", "”; सभी तत्व कभी", "”; वे कभी",
     scope="sentence", zone="pp")
rule("A5 no added subject: «; वे» for a continuing subject", {5}, r"tipi; siyā", "”; कभी ", "”; वे कभी ",
     scope="sentence", zone="pp")
KEN_M = "किसी एक प्रकार की चेतना से जाने जा सकने वाले हैं, किसी एक प्रकार की चेतना से न जाने जा सकने वाले हैं"
KEN_F = "किसी एक प्रकार की चेतना से जानी जा सकने वाली हैं, किसी एक प्रकार की चेतना से न जानी जा सकने वाली हैं"
rule("A6 kenaci viññeyyā (one wording)", {1}, r"; kenaci viññeyy",
     "; वे किसी एक प्रकार की चेतना से जाने जा सकने वाले हैं और किसी एक प्रकार की चेतना से न जाने जा सकने वाले भी हैं",
     "; वे " + KEN_M, scope="sentence", zone="pp")
rule("A6 kenaci viññeyyā (one wording)", {2}, r"; kenaci viññeyy",
     "; इंद्रिय-क्षेत्र किसी एक प्रकार की चेतना से जाने जा सकने वाले भी हैं, किसी एक प्रकार की चेतना से न जाने जा सकने वाले भी",
     "; वे " + KEN_M, scope="sentence", zone="pp")
rule("A6 kenaci viññeyyā (one wording)", {4}, r"; kenaci viññeyy",
     "; सत्य किसी एक प्रकार की चेतना से जाने जा सकने वाले भी हैं, किसी एक प्रकार की चेतना से न जाने जा सकने वाले भी",
     "; वे " + KEN_M, scope="sentence", zone="pp")
rule("A6 kenaci viññeyyā (one wording)", {3}, r"; kenaci viññeyy", "; सभी तत्व " + KEN_M, "; वे " + KEN_M,
     scope="sentence", zone="pp")
rule("A6 kenaci viññeyyā (one wording)", {5}, r"; kenaci viññeyy", "; " + KEN_F, "; वे " + KEN_F,
     scope="sentence", zone="pp")
rule("A5 no added subject (sentence start)", {1}, r"^Sappaccayā, saṅkhatā\.",
     "पाँचों समूह कारणों पर निर्भर रहने वाले हैं, निर्मित हैं।", "कारणों पर निर्भर रहने वाले हैं, निर्मित हैं।",
     scope="sentence", zone="pp")
rule("A5 no added subject (sentence start)", {8, 9}, r"^Kusalāyeva\.", "वे केवल हितकर हैं।", "केवल हितकर हैं।",
     scope="sentence", zone="pp")
rule("A5 no added subject (sentence start)", {14}, r"^[A-Z]", r"^पाँचों ", "", rx=True, scope="sentence", zone="pp")
rule("A5 no added subject (sentence start)", {15}, r"^[A-Z]", r"^चारों ", "", rx=True, scope="sentence", zone="pp")
rule("A5 no added subject: «इन्हें»", {14}, r"vattabb", "इन पाँचों को ", "इन्हें ", scope="sentence", zone="pp")
rule("A5 no added subject: «इन्हें»", {15}, r"vattabb", "इन चारों को ", "इन्हें ", scope="sentence", zone="pp")
rule("A5 no added subject (sentence start)", {14}, r"^Āsavavippayuttā sāsavā, no saṃyojanā", r"^पाँचों ", "", rx=True, zone="pp")
rule("A5 no added subject (sentence start)", {15}, r"siyā lokuttarā, kenaci viññeyyā", ", चारों किसी एक प्रकार",
     ", किसी एक प्रकार", zone="pp")


# A7 negated items «na X / no X / siyā na X / siyā no X» -> predicate negation (pi-1 rails ^1-1404/^1-1422 shape,
#    majority of the chapters): «X नहीं है/हैं», «कभी X नहीं होता/होते/होती/होतीं»
NEG_P = re.compile(r"^(?:(?![Ss]iyā\b|[Nn][ao]\b)\S+ (?:(?![Ss]iyā\b|[Nn][ao]\b)\S+ )?)?(?:[Ss]iyā )?(?:na|no|Na|No) "
                   r"(?!vattabb|ca\b|hetu\w|hetū\w)(?:\S+|dassanena \S+|bhāvanāya \S+)[.,;]?$")
VERB_NEG = {"होता है": "होता", "होते हैं": "होते", "होती है": "होती", "होती हैं": "होतीं", "है": "है", "हैं": "हैं"}


def neg_item(h):
    """h: one Hindi item (no trailing separator). Returns the predicate-negated form or h."""
    m = re.match(r"^(.*?)((?:होता है|होते हैं|होती है|होती हैं|है|हैं))([।,;]?)$", h)
    if not m or "नहीं" in h:
        return h
    body, verb, end = m.groups()
    body = body.rstrip()
    siya = body.startswith("कभी ") or " कभी " in body
    v = VERB_NEG[verb] if siya else verb
    # subject + कभी prefix stays as is; transform the predicate tail
    pats = [
        (r"^(.*?) से न (छोड़[ाेी] जाने वाल[ाेी])$", r"\1 से \2"),                              # na dassanena pahātabbā
        (r"^(.*?) छोड़े जाने वाले मूलों से रहित$", None),                                     # …hetukā
        (r"^(.*?रूपी) न होने वाल[ाेी]$", r"\1"),                                            # no āsavā …
        (r"^(.*?से संबंधित) न होने वाल[ाेी]$", r"\1"),                                       # na kāmāvacarā …
        (r"^(.*?(?:के साथ|साथ-साथ)) न (होने वाल[ाेी])$", r"\1 \2"),                           # na pītisahagatā …
        (r"^(.*?(?:से घुला-मिला|से घुले-मिले|से घुली-मिली|से उत्पन्न)) न होने वाल[ाेी]$", r"\1"),
        (r"^(.*?) न (होने वाल[ाेी])$", r"\1 \2"),
    ]
    for p, t in pats:
        mm = re.match(p, body)
        if not mm:
            continue
        if t is None:  # मूलों से रहित -> मूलों वाला/वाले नहीं
            sing = verb in ("होता है", "है")
            new = mm.group(1) + " छोड़े जाने वाले मूलों " + ("वाला" if sing else "वाले")
        else:
            new = mm.expand(t)
        return f"{new} नहीं {v}{end}"
    return h


def neg_item_func(h):
    core = h.rstrip()
    ws = h[len(core):]
    # an item may carry a leading quote-closing / other matter only if it is a whole sentence; keep it simple
    return neg_item(core) + ws


rule("A7 negated item -> predicate negation", None, NEG_P.pattern, None, None, scope="item", zone="pp",
     func=neg_item_func)
# «X ऐसे हैं जो Y नहीं हैं» / «कभी ऐसा होता है जो Y नहीं है» (ch2, ch4) -> «X Y नहीं हैं» / «कभी Y नहीं होता»
rule("A7 negated item -> predicate negation", {2, 4}, r"\bno citta", r"ऐसे हैं जो (\S[^।;]*?) नहीं हैं", r"\1 नहीं हैं",
     rx=True, scope="sentence", zone="pp")
rule("A7 negated item -> predicate negation", {2, 4}, r"\bno citta", r"ऐसा है जो (\S[^।;]*?) नहीं है", r"\1 नहीं है",
     rx=True, scope="sentence", zone="pp")
rule("A7 negated item -> predicate negation", {2, 4}, r"\bno citta", r"कभी ऐसा होता है जो (\S[^।;]*?) नहीं है",
     r"कभी \1 नहीं होता", rx=True, scope="sentence", zone="pp")


rule("A7 negated item -> predicate negation", {4}, r"Dve saccā no nīvaraṇā", "दो सत्य बाधा रूपी न होने वाले हैं।",
     "दो सत्य बाधा रूपी नहीं हैं।", zone="pp")
rule("A7 negated item -> predicate negation", {4}, r"siyā no nīvaraṇaṃ", "कभी बाधा रूपी न होने वाला होता है।",
     "कभी बाधा रूपी नहीं होता।", zone="pp")


# A8 no quotes where the Pāli of the no-dash frame has none (ch8, ch9, ch12)
def unquote_vattabba(h):
    parts = re.split(r"(?<=[।;])", h)
    out = []
    for s in parts:
        if "कहा जा सकता" in s:
            s = s.replace("“", "").replace("”", "")
        out.append(s)
    return "".join(out)


rule("A8 no-dash na vattabba: no added quotes", None, r'^[^"]*vattabb[^"]*$', None, None, scope="sentence", zone="pp",
     func=unquote_vattabba)
# A9 «na vattabbā Xti, Y» (no dash): «इन्हें X नहीं कहा जा सकता, ये Y हैं» with the matrix item name (ch7 shape)
def a9(h):
    pron = "ये" if h.startswith("इन्हें ") else "वे"  # deictic in a subjectless sentence, anaphoric after a subject
    h = h.replace(", वे मूल वाले हैं, पर स्वयं मूल रूपी नहीं हैं", f", {pron} मूल वाले, पर स्वयं मूल रूपी न होने वाले हैं")
    return h.replace(", वे मूलों से जुड़े हैं, पर स्वयं मूल रूपी नहीं हैं", f", {pron} मूलों से जुड़े, पर स्वयं मूल रूपी न होने वाले हैं")


rule("A9 na vattabba Xti, Y: item name", {8, 9}, r"na ca hetū", None, None, scope="sentence", zone="pp", func=a9)

# ================================================================================================================
# B. Four noble truths; Suttanta definitions (ch4 = ch6)
# ================================================================================================================
# nirodhasacca: termbase nirodha (compound member) = अंत, sacca = सत्य -> «अंत का सत्य» (ch4, 34x)
rule("B1 nirodhasacca = अंत का सत्य", None, r"[Nn]irodhasacc", "दुःख के अंत का सत्य", "अंत का सत्य")
rule("B1 nirodhasacca = अंत का सत्य", None, r"[Nn]irodhasacc", "दुःख के अंत के सत्य", "अंत के सत्य")
# -itattaṃ = «… से भरा होना» (book-wide house pattern, ch6); byasana list without «या» before each item (ch4)
rule("B2 soka/parideva/upāyāsa -itattaṃ = «से भरा होना»", {4}, r"socitattaṃ", "शोकग्रस्त होना", "शोक से भरा होना")
rule("B2 soka/parideva/upāyāsa -itattaṃ = «से भरा होना»", {4}, r"ādevitattaṃ",
     "रोने की अवस्था, विलाप की अवस्था", "रोने से भरा होना, विलाप से भरा होना")
rule("B2 soka/parideva/upāyāsa -itattaṃ = «से भरा होना»", {4}, r"lālappitattaṃ", "बिलखने की अवस्था", "बिलखने से भरा होना")
rule("B2 soka/parideva/upāyāsa -itattaṃ = «से भरा होना»", {4}, r"āyāsitattaṃ",
     "हताश होने की अवस्था, निराश होने की अवस्था", "हताशा से भरा होना, निराशा से भरा होना")
rule("B3 byasana list (ch4 wording)", {6}, r"Ñātibyasanena",
     "पीड़ित, या धन-संपत्ति की हानि से पीड़ित, या रोग रूपी हानि से पीड़ित, या सदाचार की हानि से पीड़ित, या दृष्टि",
     "पीड़ित, धन-संपत्ति की हानि से पीड़ित, रोग रूपी हानि से पीड़ित, सदाचार की हानि से पीड़ित या दृष्टि")
rule("B4 dukkhe ñāṇaṃ = «दुःख का ज्ञान» (ch11, ch16)", {4}, r"Dukkhe ñāṇaṃ, dukkhasamudaye ñāṇaṃ",
     "दुःख के बारे में ज्ञान, दुःख की उत्पत्ति के बारे में ज्ञान, दुःख के अंत के बारे में ज्ञान, दुःख के अंत की ओर ले जाने वाले प्रगति के ढंग के बारे में ज्ञान",
     "दुःख का ज्ञान, दुःख की उत्पत्ति का ज्ञान, दुःख के अंत का ज्ञान, दुःख के अंत की ओर ले जाने वाले प्रगति के ढंग का ज्ञान")
rule("B5 typo «दुःखके»", {16}, r"dukkhanirodh", "दुःखके अंत", "दुःख के अंत")
rule("B6 dhamme ñāṇaṃ = «परिघटनाओं का ज्ञान» (ch15)", {16}, r"dhamme ñāṇaṃ dhammapaṭisambhidā",
     "परिघटना का ज्ञान परिघटनाओं का विश्लेषणात्मक", "परिघटनाओं का ज्ञान परिघटनाओं का विश्लेषणात्मक")

# ================================================================================================================
# C. Right efforts; āsevati bhāveti bahulīkaroti; upeto hoti …; vīriya string
# ================================================================================================================
rule("C1 right-effort formula = pi-1 ^1-1377", {11}, r"anuppannānaṃ pāpakānaṃ", "बुरी, हानिकर", "बुरी हानिकर")
rule("C1 right-effort formula = pi-1 ^1-1377", {11}, r"anuppannānaṃ pāpakānaṃ", "पूरा ज़ोर लगाता है; उत्पन्न",
     "पूरा ज़ोर लगाता है, उत्पन्न")
rule("C1 right-effort formula = pi-1 ^1-1377", {11}, r"bhiyyobhāvāya vepullāya",
     "उनकी वृद्धि के लिए, विपुलता के लिए और अभ्यास की परिपूर्णता के लिए",
     "उन्हें और बढ़ाने के लिए, उनकी विपुलता के लिए, उनके अभ्यास के लिए, उनकी परिपूर्णता के लिए")
rule("C2 āsevati bhāveti bahulīkaroti (one string)", {7}, r"āsevati bhāveti bahulīkaroti",
     "का निरंतर सेवन करता है, उसका अभ्यास करता है, उसे बार-बार करता है",
     "का निरंतर सेवन करता है, अभ्यास करता है, बार-बार करता है")
rule("C2 āsevati bhāveti bahulīkaroti (one string)", {7}, r"āsevitvā bhāvetvā bahulīkatvā",
     "का निरंतर सेवन करके, उसका अभ्यास करके, उसे बार-बार करके", "का निरंतर सेवन करके, अभ्यास करके, बार-बार करके")
rule("C2 āsevati bhāveti bahulīkaroti (one string)", {12}, r"āsevati bhāveti bahulīkaroti",
     "निरंतर सेवन करता है, अभ्यास करता है, उन्हें बार-बार करता है", "निरंतर सेवन करता है, अभ्यास करता है, बार-बार करता है")
UPETO_LONG = "से सुसज्जित, भली-भाँति सुसज्जित, उस तक पहुँचा हुआ, उस तक भली-भाँति पहुँचा हुआ, उसे पाया हुआ, उससे संपन्न और उससे युक्त होता है"
rule("C3 upeto hoti … samannāgato (ch8/ch9 wording)", {7}, r"upeto hoti",
     "से सुसज्जित होता है, भली-भाँति सुसज्जित होता है, इस तक पहुँचा हुआ होता है, इस तक भली-भाँति पहुँचा हुआ होता है, इसे पाया हुआ होता है, इससे संपन्न होता है, इससे युक्त होता है",
     UPETO_LONG)
rule("C3 upeto hoti … samannāgato (ch8/ch9 wording)", {7}, r"upeto hoti", "से सुसज्जित होता है… इससे युक्त होता है",
     "से सुसज्जित… उससे युक्त होता है")
rule("C3 upeto hoti … samannāgato (ch8/ch9 wording)", {12}, r"upeto hoti",
     "से सुसज्जित, भली-भाँति सुसज्जित, उस तक पहुँचा हुआ, भली-भाँति पहुँचा हुआ, उसे पाया हुआ, उससे संपन्न, उससे युक्त होता है",
     UPETO_LONG)
rule("C3 upeto hoti … samannāgato (two objects: उनसे)", {12}, r"upeto hoti",
     r"(से और इस [^।]*?से सुसज्जित(?:, भली-भाँति सुसज्जित)?)… युक्त होता है", r"\1… उनसे युक्त होता है", rx=True)
rule("C3 upeto hoti … samannāgato (ch8/ch9 wording)", {12}, r"upeto hoti",
     r"(सुसज्जित(?:, भली-भाँति सुसज्जित)?)… युक्त होता है", r"\1… उससे युक्त होता है", rx=True)
rule("C4 vīriya string: anikkhittachandatā = चाह न छोड़ना", {9}, r"anikkhittachandatā", "लगन न छोड़ना",
     "चाह न छोड़ना")

# ================================================================================================================
# D. «Tena vuccati "X"ti» = «इसीलिए “X” कहा जाता है।» (ch7, ch12, ch13 shape)
# ================================================================================================================
rule("D1 Tena vuccati = «इसीलिए “X” कहा जाता है।»", {6, 8, 9}, r"[Tt]ena vuccati",
     r"इसीलिए कहा जाता है(?:,| कि वह) “([^”]+)”।", r"इसीलिए “\1” कहा जाता है।", rx=True)
rule("D1 Tena vuccati = «इसीलिए “X” कहा जाता है।»", {9}, r"[Tt]ena vuccati",
     r"इसीलिए वह “([^”]+)” कहा जाता है।", r"इसीलिए “\1” कहा जाता है।", rx=True)

# ================================================================================================================
# E. veramaṇī: precept phrases = termbase phrase entries «… से दूर रहना» (ch11); list item veramaṇī = «बचना»
# ================================================================================================================
# phrase entries exist for Musāvādā / Pāṇātipātā / adinnādānā / kāmesumicchācārā veramaṇī (= «… से दूर रहना»);
# pisuṇāya vācāya / pharusāya vācāya / samphappalāpā veramaṇī have none -> veramaṇī = «बचना» (ch4 = ch11)
rule("E1 precept phrase «X से दूर रहना»", {4}, r"Musāvādā veramaṇī", "झूठ बोलने से बचना", "झूठ बोलने से दूर रहना")
rule("E1 precept phrase «X से दूर रहना»", {4}, r"Pāṇātipātā veramaṇī", "से बचना", "से दूर रहना")
rule("E2 veramaṇī without a phrase entry = «बचना»", {11}, r"pisuṇāya vācāya veramaṇī", "चुगली की वाणी से दूर रहना",
     "चुगली की वाणी से बचना")
rule("E2 veramaṇī without a phrase entry = «बचना»", {11}, r"pharusāya vācāya veramaṇī", "कठोर वाणी से दूर रहना",
     "कठोर वाणी से बचना")
rule("E2 veramaṇī without a phrase entry = «बचना»", {11}, r"samphappalāpā veramaṇī", "व्यर्थ की बकवास से दूर रहना",
     "व्यर्थ की बकवास से बचना")
rule("E1 precept phrase «X से दूर रहना»", {4}, r"adinnādānā veramaṇī", "न दिए हुए को लेने से", "बिना दी गई चीज़ लेने से")

# ================================================================================================================
# F. Dhammasaṅgaṇī references = «परिघटनाओं की गणना»
# ================================================================================================================
rule("F1 dha. sa. = «परिघटनाओं की गणना»", {10}, r"dha\. ?sa\.", "धम्मसंगणी ", "परिघटनाओं की गणना ")
rule("F1 dha. sa. = «परिघटनाओं की गणना»", {17}, r"dha\. ?sa\.", "dha. sa. ", "परिघटनाओं की गणना ")

# ================================================================================================================
# G. formulas: rūpa list (hi-rails-formulas.md), vipāka (termbase), jhāna formulas, «Idha bhikkhu yasmiṃ samaye»
# ================================================================================================================
rule("G1 yañca rūpaṃ anidassanaappaṭighaṃ … (formulas file)", None, r"yañca rūpaṃ anidassanaappaṭighaṃ",
     "वह भौतिक रूप जो दिखाई न देने वाला और टकराव से रहित है", "जो भी भौतिक रूप दिखाई न देने वाला और टकराव से रहित है")
rule("G2 vipāka = कर्म-फल रूपी (termbase)", {15}, r"katattā (upacitattā|bhāvitattā) vipāk", "कर्म के फल रूपी",
     "कर्म-फल रूपी")
rule("G3 third jhāna: upekkhako = समभाव वाला, satimā = सजग (termbase)", {11}, r"upekkhako ca viharati",
     "वह समभाव के साथ, सजग और स्पष्ट समझ रखते हुए रहता है", "वह समभाव वाला होकर, सजग और स्पष्ट समझ रखते हुए रहता है")
rule("G3 third jhāna: upekkhako = समभाव वाला, satimā = सजग (termbase)", {12}, r"satimā", "सजगता वाला", "सजग")
rule("G4 «Idha bhikkhu yasmiṃ samaye» = «यहाँ भिक्षु जिस समय»", {12, 13}, r"Idha bhikkhu yasmiṃ samaye",
     "यहाँ जिस समय कोई भिक्षु ", "यहाँ भिक्षु जिस समय ")
rule("G4 «Idha bhikkhu yasmiṃ samaye» = «यहाँ भिक्षु जिस समय»", {8}, r"Idha bhikkhu yasmiṃ samaye",
     "यहाँ जिस समय भिक्षु ", "यहाँ भिक्षु जिस समय ")

# ================================================================================================================
# H. ch12/ch13 Pañhāpucchaka lines (comma-list Pāli): the same frames as ch7 (verb repeated in every «कभी» clause,
#    «हैं/है» for plain predicates, no added «ये», predicate negation, item names). Whole-line replacements:
#    (chapter, non-empty line) -> (Pāli line prefix that must match, new Hindi line without the block ID)
# ================================================================================================================
_PP_NO_SAMYOJANA = ("बंधन रूपी नहीं हैं… गाँठ रूपी नहीं हैं… बाढ़ रूपी नहीं हैं… जकड़न रूपी नहीं हैं… बाधा रूपी नहीं हैं… "
                    "ग़लत धारणा रूपी नहीं हैं… विषय वाले हैं, मन रूपी नहीं हैं, मन के सहचर हैं, मन से जुड़े हैं, मन से घुले-मिले हैं, "
                    "मन से उत्पन्न हैं, मन के साथ-साथ होने वाले हैं, मन का अनुसरण करने वाले हैं, मन से घुले-मिले और मन से उत्पन्न हैं, "
                    "मन से घुले-मिले, मन से उत्पन्न और मन के साथ-साथ होने वाले हैं, मन से घुले-मिले, मन से उत्पन्न और मन का अनुसरण "
                    "करने वाले हैं, बाह्य हैं, व्युत्पन्न नहीं हैं, कभी कर्म से उत्पन्न होते हैं, कभी कर्म से उत्पन्न न होने वाले होते हैं।")
_PP_NO_UPADANA = ("आसक्ति रूपी नहीं हैं… मन के क्लेश रूपी नहीं हैं… सत्य-दर्शन से छोड़े जाने वाले नहीं हैं, मानसिक अभ्यास से "
                  "छोड़े जाने वाले नहीं हैं, सत्य-दर्शन से छोड़े जाने वाले मूलों वाले नहीं हैं, मानसिक अभ्यास से छोड़े जाने वाले मूलों "
                  "वाले नहीं हैं।")
LINEFIX = {
    (12, 217): ("Siyā kusalā, siyā abyākatā. Tīṇi jhānāni",
                "कभी हितकर होते हैं, कभी नैतिक रूप से अनिर्धारित होते हैं। "
                "तीन ध्यान – इनमें उत्पन्न सुखद अनुभूति को छोड़कर सुखद अनुभूति से जुड़े हैं, चौथा ध्यान – इसमें उत्पन्न न दुःखद, न सुखद "
                "अनुभूति को छोड़कर न दुःखद, न सुखद अनुभूति से जुड़ा है। "
                "कभी कर्म-फल रूपी होते हैं, कभी कर्म-फल उत्पन्न करने वाले होते हैं, कभी न कर्म-फल रूपी, न कर्म-फल उत्पन्न करने वाले होते हैं। "
                "कभी कर्म से उत्पन्न और आसक्ति का विषय बनने वाले होते हैं, कभी कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाले होते हैं, "
                "कभी न कर्म से उत्पन्न, न आसक्ति का विषय बनने वाले होते हैं। "
                "कभी क्लेशों से मलिन न होने वाले, पर क्लेशों का विषय बनने वाले होते हैं, कभी क्लेशों से मलिन न होने वाले और क्लेशों का "
                "विषय न बनने वाले होते हैं। "
                "पहला ध्यान – इसमें उत्पन्न आरंभिक विचार और सतत विचार को छोड़कर आरंभिक विचार और सतत विचार वाला है, तीन ध्यान आरंभिक "
                "विचार और सतत विचार दोनों से रहित हैं। "
                "दो ध्यान – इनमें उत्पन्न उल्लास को छोड़कर उल्लास के साथ होने वाले हैं, तीन ध्यान – इनमें उत्पन्न सुख को छोड़कर सुख के "
                "साथ होने वाले हैं, चौथा ध्यान – इसमें उत्पन्न समभाव को छोड़कर समभाव के साथ होने वाला है। "
                "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़े जाने वाले हैं। "
                "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़े जाने वाले मूलों वाले हैं। "
                "कभी संचय की ओर ले जाने वाले होते हैं, कभी संचय घटाने की ओर ले जाने वाले होते हैं, कभी न संचय की ओर, न संचय घटाने की "
                "ओर ले जाने वाले होते हैं। "
                "कभी सीखने के चरण के होते हैं, कभी सीखना पूरा होने के चरण के होते हैं, कभी न सीखने के चरण के, न सीखना पूरा होने के "
                "चरण के होते हैं। "
                "कभी उन्नत होते हैं, कभी अपरिमित होते हैं। "
                "तीन ध्यानों को न सीमित विषय वाले कहा जा सकता है, न उन्नत विषय वाले, वे कभी अपरिमित विषय वाले होते हैं, कभी उन्हें "
                "अपरिमित विषय वाले नहीं कहा जा सकता; चौथा ध्यान कभी सीमित विषय वाला होता है, कभी उन्नत विषय वाला होता है, कभी अपरिमित "
                "विषय वाला होता है; कभी उसे न सीमित विषय वाला कहा जा सकता है, न उन्नत विषय वाला, न अपरिमित विषय वाला। "
                "कभी मध्यम होते हैं, कभी उत्तम होते हैं। "
                "कभी सही दिशा में निश्चित होते हैं, कभी अनिश्चित होते हैं। "
                "तीन ध्यान मार्ग को विषय बनाने वाले नहीं हैं, कभी मार्ग को मूल बनाने वाले होते हैं, कभी मार्ग की प्रधानता वाले होते हैं, "
                "कभी उन्हें न मार्ग को मूल बनाने वाले कहा जा सकता है, न मार्ग की प्रधानता वाले; चौथा ध्यान कभी मार्ग को विषय बनाने वाला "
                "होता है, कभी मार्ग को मूल बनाने वाला होता है, कभी मार्ग की प्रधानता वाला होता है, कभी उसे न मार्ग को विषय बनाने वाला कहा "
                "जा सकता है, न मार्ग को मूल बनाने वाला, न मार्ग की प्रधानता वाला। "
                "कभी उत्पन्न हो चुके होते हैं, कभी उत्पन्न न हुए होते हैं, कभी उत्पन्न होने वाले होते हैं। "
                "कभी अतीत के होते हैं, कभी भविष्य के होते हैं, कभी वर्तमान के होते हैं। "
                "तीन ध्यानों को न अतीत के विषय वाले कहा जा सकता है, न भविष्य के विषय वाले, न वर्तमान के विषय वाले; चौथा ध्यान कभी अतीत "
                "के विषय वाला होता है, कभी भविष्य के विषय वाला होता है, कभी वर्तमान के विषय वाला होता है, कभी उसे न अतीत के विषय वाला कहा "
                "जा सकता है, न भविष्य के विषय वाला, न वर्तमान के विषय वाला। "
                "कभी स्वयं से संबंधित होते हैं, कभी दूसरों से संबंधित होते हैं, कभी स्वयं और दूसरों दोनों से संबंधित होते हैं। "
                "तीन ध्यान दूसरों से संबंधित विषय वाले हैं, चौथा ध्यान कभी स्वयं से संबंधित विषय वाला होता है, कभी दूसरों से संबंधित "
                "विषय वाला होता है, कभी स्वयं और दूसरों दोनों से संबंधित विषय वाला होता है, कभी उसे न स्वयं से संबंधित विषय वाला कहा जा "
                "सकता है, न दूसरों से संबंधित विषय वाला, न स्वयं और दूसरों दोनों से संबंधित विषय वाला। "
                "दिखाई न देने वाले और टकराव से रहित हैं।"),
    (12, 219): ("Na hetū, sahetukā, hetusampayuttā",
                "मूल रूपी नहीं हैं, मूल वाले हैं, मूलों से जुड़े हैं, इन्हें “मूल रूपी भी और मूल वाले भी” नहीं कहा जा सकता, ये मूल वाले, "
                "पर स्वयं मूल रूपी न होने वाले हैं, इन्हें “मूल रूपी भी और मूलों से जुड़े भी” नहीं कहा जा सकता, ये मूलों से जुड़े, पर "
                "स्वयं मूल रूपी न होने वाले हैं, मूल रूपी न होने वाले, पर मूल वाले हैं।"),
    (12, 220): ("Sappaccayā, saṅkhatā, anidassanā, appaṭighā, arūpā, siyā lokiyā",
                "कारणों पर निर्भर रहने वाले हैं, निर्मित हैं, दिखाई न देने वाले हैं, टकराव से रहित हैं, अभौतिक हैं, कभी लौकिक होते हैं, "
                "कभी लोकोत्तर होते हैं, किसी एक प्रकार की चेतना से जाने जा सकने वाले हैं, किसी एक प्रकार की चेतना से न जाने जा सकने "
                "वाले हैं।"),
    (12, 221): ("No āsavā, siyā sāsavā, siyā anāsavā",
                "मन के मैल रूपी नहीं हैं, कभी मन के मैलों का विषय बनने वाले होते हैं, कभी मन के मैलों का विषय न बनने वाले होते हैं, मन के "
                "मैलों से अलग हैं, इन्हें “मन के मैल रूपी भी और मन के मैलों का विषय बनने वाले भी” नहीं कहा जा सकता, ये कभी मन के मैलों का "
                "विषय बनने वाले, पर स्वयं मन के मैल रूपी न होने वाले होते हैं, कभी इन्हें “मन के मैलों का विषय बनने वाले, पर स्वयं मन के "
                "मैल रूपी न होने वाले” नहीं कहा जा सकता। "
                "इन्हें न “मन के मैल रूपी भी और मन के मैलों से जुड़े भी” कहा जा सकता है, न मन के मैलों से जुड़े, पर स्वयं मन के मैल रूपी "
                "न होने वाले। "
                "कभी मन के मैलों से अलग, पर उनका विषय बनने वाले होते हैं, कभी मन के मैलों से अलग और उनका विषय न बनने वाले होते हैं।"),
    (12, 222): ("No saṃyojanā…pe… no ganthā", _PP_NO_SAMYOJANA),
    (12, 223): ("No upādānā…pe… no kilesā",
                _PP_NO_UPADANA + " "
                "पहला ध्यान – इसमें उत्पन्न आरंभिक विचार को छोड़कर आरंभिक विचार वाला है, तीन ध्यान आरंभिक विचार से रहित हैं। "
                "पहला ध्यान – इसमें उत्पन्न सतत विचार को छोड़कर सतत विचार वाला है, तीन ध्यान सतत विचार से रहित हैं। "
                "दो ध्यान – इनमें उत्पन्न उल्लास को छोड़कर उल्लास वाले हैं, दो ध्यान उल्लास से रहित हैं। "
                "दो ध्यान – इनमें उत्पन्न उल्लास को छोड़कर उल्लास के साथ होने वाले हैं, दो ध्यान उल्लास के साथ होने वाले नहीं हैं। "
                "तीन ध्यान – इनमें उत्पन्न सुख को छोड़कर सुख के साथ होने वाले हैं, चौथा ध्यान सुख के साथ होने वाला नहीं है। "
                "चौथा ध्यान – इसमें उत्पन्न समभाव को छोड़कर समभाव के साथ होने वाला है, तीन ध्यान समभाव के साथ होने वाले हैं, "
                "इंद्रिय-सुखों के लोक से संबंधित नहीं हैं, कभी सूक्ष्म भौतिक लोक से संबंधित होते हैं, कभी सूक्ष्म भौतिक लोक से संबंधित "
                "नहीं होते, तीन ध्यान अभौतिक लोक से संबंधित नहीं हैं, चौथा ध्यान कभी अभौतिक लोक से संबंधित होता है, कभी अभौतिक लोक से "
                "संबंधित नहीं होता, कभी अस्तित्व के लोकों में समाए हुए होते हैं, कभी अस्तित्व के लोकों में न समाए हुए होते हैं, कभी मुक्ति "
                "की ओर ले जाने वाले होते हैं, कभी मुक्ति की ओर न ले जाने वाले होते हैं, कभी निश्चित होते हैं, कभी अनिश्चित होते हैं, कभी "
                "सर्वोच्च न होने वाले होते हैं, कभी सर्वोच्च होते हैं, संघर्ष से रहित हैं।"),
    (13, 102): ("Siyā kusalā, siyā abyākatā. Tisso appamaññāyo",
                "कभी हितकर होते हैं, कभी नैतिक रूप से अनिर्धारित होते हैं। "
                "तीन असीम भाव सुखद अनुभूति से जुड़े हैं, समभाव न दुःखद, न सुखद अनुभूति से जुड़ा है। "
                "कभी कर्म-फल रूपी होते हैं, कभी कर्म-फल उत्पन्न करने वाले होते हैं, कभी न कर्म-फल रूपी, न कर्म-फल उत्पन्न करने वाले होते हैं। "
                "कभी कर्म से उत्पन्न और आसक्ति का विषय बनने वाले होते हैं, कभी कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाले होते हैं। "
                "क्लेशों से मलिन न होने वाले, पर क्लेशों का विषय बनने वाले हैं। "
                "तीन असीम भाव कभी आरंभिक विचार और सतत विचार वाले होते हैं, कभी आरंभिक विचार से रहित, केवल सतत विचार वाले होते हैं, कभी "
                "आरंभिक विचार और सतत विचार दोनों से रहित होते हैं; समभाव आरंभिक विचार और सतत विचार दोनों से रहित है। "
                "तीन असीम भाव कभी उल्लास के साथ होने वाले होते हैं, कभी सुख के साथ होने वाले होते हैं, समभाव के साथ होने वाले नहीं हैं, "
                "कभी उन्हें उल्लास के साथ होने वाले नहीं कहा जा सकता; समभाव समभाव के साथ होने वाला है। "
                "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़े जाने वाले हैं। "
                "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़े जाने वाले मूलों वाले हैं। "
                "कभी संचय की ओर ले जाने वाले होते हैं, कभी न संचय की ओर, न संचय घटाने की ओर ले जाने वाले होते हैं, न सीखने के चरण के, न "
                "सीखना पूरा होने के चरण के हैं, उन्नत हैं, इन्हें न सीमित विषय वाले कहा जा सकता है, न उन्नत विषय वाले, न अपरिमित विषय वाले। "
                "मध्यम हैं, अनिश्चित हैं, इन्हें न मार्ग को विषय बनाने वाले कहा जा सकता है, न मार्ग को मूल बनाने वाले, न मार्ग की "
                "प्रधानता वाले। "
                "कभी उत्पन्न हो चुके होते हैं, कभी उत्पन्न न हुए होते हैं, कभी उत्पन्न होने वाले होते हैं। "
                "कभी अतीत के होते हैं, कभी भविष्य के होते हैं, कभी वर्तमान के होते हैं। "
                "इन्हें न अतीत के विषय वाले कहा जा सकता है, न भविष्य के विषय वाले, न वर्तमान के विषय वाले। "
                "कभी स्वयं से संबंधित होते हैं, कभी दूसरों से संबंधित होते हैं, कभी स्वयं और दूसरों दोनों से संबंधित होते हैं, दूसरों से "
                "संबंधित विषय वाले हैं, दिखाई न देने वाले और टकराव से रहित हैं।"),
    (13, 104): ("Mettā hetu, tisso appamaññāyo na hetū",
                "मैत्री मूल रूपी है, तीन असीम भाव मूल रूपी नहीं हैं, मूल वाले हैं, मूलों से जुड़े हैं। "
                "मैत्री मूल रूपी भी और मूल वाली भी है; तीन असीम भावों को मूल रूपी भी और मूल वाले भी नहीं कहा जा सकता, वे मूल वाले, पर "
                "स्वयं मूल रूपी न होने वाले हैं। "
                "मैत्री मूल रूपी भी और मूलों से जुड़ी भी है; तीन असीम भावों को मूल रूपी भी और मूलों से जुड़े भी नहीं कहा जा सकता, वे "
                "मूलों से जुड़े, पर स्वयं मूल रूपी न होने वाले हैं। "
                "तीन असीम भाव मूल रूपी न होने वाले, पर मूल वाले हैं; मैत्री को न मूल रूपी न होने वाली, पर मूल वाली कहा जा सकता है, न "
                "मूल रूपी न होने वाली और मूल से रहित।"),
    (13, 105): ("Sappaccayā, saṅkhatā, anidassanā, appaṭighā, arūpā, lokiyā",
                "कारणों पर निर्भर रहने वाले हैं, निर्मित हैं, दिखाई न देने वाले हैं, टकराव से रहित हैं, अभौतिक हैं, लौकिक हैं, किसी एक "
                "प्रकार की चेतना से जाने जा सकने वाले हैं, किसी एक प्रकार की चेतना से न जाने जा सकने वाले हैं, मन के मैल रूपी नहीं हैं, "
                "मन के मैलों का विषय बनने वाले हैं, मन के मैलों से अलग हैं, इन्हें मन के मैल रूपी भी और मन के मैलों का विषय बनने वाले भी "
                "नहीं कहा जा सकता, ये मन के मैलों का विषय बनने वाले, पर स्वयं मन के मैल रूपी न होने वाले हैं, इन्हें न मन के मैल रूपी भी "
                "और मन के मैलों से जुड़े भी कहा जा सकता है, न मन के मैलों से जुड़े, पर स्वयं मन के मैल रूपी न होने वाले। "
                "मन के मैलों से अलग, पर उनका विषय बनने वाले हैं।"),
    (13, 106): ("No saṃyojanā…pe… no ganthā", _PP_NO_SAMYOJANA),
    (13, 107): ("No upādānā…pe… no kilesā",
                _PP_NO_UPADANA + " "
                "तीन असीम भाव कभी आरंभिक विचार वाले होते हैं, कभी आरंभिक विचार से रहित होते हैं; समभाव आरंभिक विचार से रहित है। "
                "तीन असीम भाव कभी सतत विचार वाले होते हैं, कभी सतत विचार से रहित होते हैं; समभाव सतत विचार से रहित है। "
                "तीन असीम भाव कभी उल्लास वाले होते हैं, कभी उल्लास से रहित होते हैं; समभाव उल्लास से रहित है। "
                "तीन असीम भाव कभी उल्लास के साथ होने वाले होते हैं, कभी उल्लास के साथ होने वाले नहीं होते; समभाव उल्लास के साथ होने वाला "
                "नहीं है। "
                "तीन असीम भाव सुख के साथ होने वाले हैं, समभाव सुख के साथ होने वाला नहीं है। "
                "समभाव समभाव के साथ होने वाला है, तीन असीम भाव समभाव के साथ होने वाले नहीं हैं, इंद्रिय-सुखों के लोक से संबंधित नहीं हैं, "
                "सूक्ष्म भौतिक लोक से संबंधित हैं, अभौतिक लोक से संबंधित नहीं हैं, अस्तित्व के लोकों में समाए हुए हैं, मुक्ति की ओर न ले "
                "जाने वाले हैं, अनिश्चित हैं, सर्वोच्च न होने वाले हैं, संघर्ष से रहित हैं।"),
}

# ================================================================================================================
# S. sentence sync: in the subjectless masculine Pañhāpucchaka sections (ch7-15), a Pāli sentence identical to one in
#    ch7 gets ch7's Hindi (ch7 = the shape chosen above); otherwise the majority Hindi of that Pāli sentence.
# ================================================================================================================
SYNC_CH = {7, 8, 9, 10, 11, 12, 13, 14, 15}
SYNC_REF = 7

# ----------------------------------------------------------------------------------------------------------------
# engine
# ----------------------------------------------------------------------------------------------------------------


def nonempty(path):
    raw = open(path, encoding="utf-8").read().split("\n")
    idx = [i for i, l in enumerate(raw) if l.strip()]
    return raw, idx


def split_keep(rx, s):
    """split keeping separators: [unit, sep, unit, sep, …, unit]"""
    return rx.split(s)


def apply_unit(rule_, p, h, ch, stats, lineno):
    mp, mh = ID.search(p), ID.search(h)
    if mp and mh:
        tail = h[mh.start():]
        res = apply_unit(rule_, p[:mp.start()].rstrip(), h[:mh.start()].rstrip(), ch, stats, lineno)
        return res + " " + tail.strip() if res != h[:mh.start()].rstrip() else h
    if rule_.scope == "line":
        if not rule_.pali.search(p):
            return h
        nh, n = rule_.apply(h)
        if n:
            stats[(rule_.name, ch)].append((lineno, n))
        return nh
    if rule_.scope == "sentence":
        sp, sh = SENT_P.split(p), SENT_H.split(h)
        seps = SENT_H.findall(h)
        if len(sp) != len(sh):
            if any(rule_.pali.search(x) for x in sp):
                SKIPPED[(rule_.name, ch)].append(lineno)
            return h
        tot = 0
        for i, (a, b) in enumerate(zip(sp, sh)):
            if rule_.pali.search(a):
                nb, n = rule_.apply(b)
                if n:
                    sh[i] = nb; tot += n
        if tot:
            stats[(rule_.name, ch)].append((lineno, tot))
            out = sh[0]
            for s, b in zip(seps, sh[1:]):
                out += s + b
            return out
        return h
    if rule_.scope == "item":
        sp, sh = SENT_P.split(p), SENT_H.split(h)
        seps = SENT_H.findall(h)
        if len(sp) != len(sh):
            if any(rule_.pali.search(x.strip()) for s in sp for x in items(s, True)):
                SKIPPED[(rule_.name, ch)].append(lineno)
            return h
        tot = 0
        for si, (ps, hs) in enumerate(zip(sp, sh)):
            up, uh = items(ps, True), items(hs, False)
            if not any(rule_.pali.search(x.strip()) for x in up):
                continue
            if len(up) != len(uh):
                SKIPPED[(rule_.name, ch)].append(lineno)
                MISMATCH.append((ch, lineno, ps, hs))
                continue
            for i, (a, b) in enumerate(zip(up, uh)):
                if rule_.pali.search(a.strip()):
                    nb, n = rule_.apply(b)
                    if n and nb != b:
                        uh[i] = nb; tot += 1
                    elif rule_.func is not None and re.search(r"न होने|से न |से रहित|ऐसा|ऐसे", b) and "नहीं" not in b:
                        UNHANDLED.append((ch, lineno, a, b))
            sh[si] = "".join(uh)
        if tot:
            stats[(rule_.name, ch)].append((lineno, tot))
            out = sh[0]
            for s, b in zip(seps, sh[1:]):
                out += s + b
            return out
        return h
    raise ValueError(rule_.scope)


def items(s, pali):
    """comma/dash items of one sentence, each keeping its trailing separator; continuation items are merged:
    Pāli items starting with a quote, Hindi items starting with «न », «पर », «और »."""
    parts = split_keep(ITEM_P if pali else ITEM_H, s)
    units = []
    for i in range(0, len(parts), 2):
        u = parts[i] + (parts[i + 1] if i + 1 < len(parts) else "")
        cont = (u.startswith('"') or u.startswith("'")) if pali else re.match(r"^(न |पर |और |न“)", u)
        if units and cont:
            units[-1] += u
        else:
            units.append(u)
    return units


MISMATCH = []


SKIPPED = collections.defaultdict(list)
UNHANDLED = []


def pp_start(P):
    for i, l in enumerate(P):
        if re.match(r"^#+\s*Pañhāpucchak", l) or "Pañcannaṃ khandhānaṃ kati kusalā" in l:
            return i
    return None


def invariants(a, b):
    def heads(x):
        return re.match(r"^#*", x).group(0)

    def idof(x):
        m = ID.search(x)
        return m.group(1) if m else None
    assert heads(a) == heads(b), (a, b)
    assert idof(a) == idof(b), (a, b)
    assert a.count("–") == b.count("–"), ("dash count", a, b)
    assert "—" not in b and ":-" not in b, b


def norm_p(s):
    s = re.sub(r"\s*\[[^\]]*\]", "", s)
    return re.sub(r"\s+", " ", s).strip()


def sync_pass(D, stats):
    """S rule: identical Pāli sentence in the Pañhāpucchaka zone of SYNC_CH -> one Hindi sentence."""
    occ = collections.defaultdict(list)  # pali sentence -> [(ch, k, si, hindi)]
    for name, (ch, P, H, newH, pps) in D.items():
        if ch not in SYNC_CH or pps is None:
            continue
        for k in range(pps, len(P)):
            p = ID.sub("", P[k]).rstrip()
            h = ID.sub("", newH[k]).rstrip()
            sp, sh = SENT_P.split(p), SENT_H.split(h)
            if len(sp) != len(sh) or P[k].startswith("#"):
                continue
            for si, (a, b) in enumerate(zip(sp, sh)):
                if len(a) < 6:
                    continue
                occ[norm_p(a)].append((name, ch, k, si, b))
    for pk, lst in occ.items():
        forms = collections.Counter(x[4] for x in lst)
        if len(forms) < 2:
            continue
        ref = [x[4] for x in lst if x[1] == SYNC_REF]
        canon = ref[0] if ref else sorted(forms.items(), key=lambda kv: (-kv[1], min(x[1] for x in lst if x[4] == kv[0])))[0][0]
        for name, ch, k, si, b in lst:
            if b == canon:
                continue
            ch_, P, H, newH, pps = D[name]
            m = ID.search(newH[k])
            tail = (" " + m.group(0).strip()) if m else ""
            h = ID.sub("", newH[k]).rstrip()
            seps = SENT_H.findall(h)
            sh = SENT_H.split(h)
            sh[si] = canon
            out = sh[0]
            for s_, b_ in zip(seps, sh[1:]):
                out += s_ + b_
            newH[k] = out + tail
            stats[("S1 sentence sync (Pañhāpucchaka ch7-15, ch7 / majority form)", ch)].append((k + 1, 1))


def main():
    stats = collections.defaultdict(list)
    preview = []
    changed = {}
    D = {}
    for name in CHAPTERS:
        ch = chno(name)
        hp = os.path.join(HDIR, name + ".md")
        P = [l for l in open(os.path.join(PDIR, name + ".md"), encoding="utf-8-sig").read().split("\n") if l.strip()]
        src = os.path.join(BAK, name + ".md") if os.path.exists(os.path.join(BAK, name + ".md")) else hp
        raw, idx = nonempty(src)
        H = [raw[i] for i in idx]
        assert len(P) == len(H), (name, len(P), len(H))
        pps = pp_start(P)
        newH = list(H)
        for (c_, ln), (pref, txt) in LINEFIX.items():
            if c_ != ch:
                continue
            k = ln - 1
            assert P[k].startswith(pref), (name, ln, P[k][:80])
            m = ID.search(H[k])
            newH[k] = txt + ((" " + m.group(0).strip()) if m else "")
            stats[("H1 ch12/ch13 Pañhāpucchaka line (ch7 frames)", ch)].append((ln, 1))
        for r_ in RULES:
            if r_.chapters is not None and ch not in r_.chapters:
                continue
            for k in range(len(P)):
                if ch == 1 and k < SAMPLE_LINES:
                    continue
                if r_.zone == "pp" and (pps is None or k < pps):
                    continue
                newH[k] = apply_unit(r_, P[k], newH[k], ch, stats, k + 1)
        D[name] = (ch, P, H, newH, pps)
    sync_pass(D, stats)
    for name in CHAPTERS:
        ch, P, H, newH, pps = D[name]
        src = os.path.join(BAK, name + ".md") if os.path.exists(os.path.join(BAK, name + ".md")) else os.path.join(HDIR, name + ".md")
        raw, idx = nonempty(src)
        for k in range(len(P)):
            if ch == 1 and k < SAMPLE_LINES:
                assert newH[k] == H[k], "sample prefix touched"
            if newH[k] != H[k]:
                invariants(H[k], newH[k])
                preview.append(f"## {name} line {k + 1}\n- {H[k]}\n+ {newH[k]}\n")
                raw[idx[k]] = newH[k]
        if newH != H:
            changed[name] = "\n".join(raw)
    # report
    tot = 0
    log = ["rule\tchapter\treplacements\tlines"]
    for (rn, ch), lst in sorted(stats.items(), key=lambda kv: (kv[0][0], kv[0][1])):
        n = sum(x[1] for x in lst)
        tot += n
        log.append(f"{rn}\t{ch}\t{n}\t{','.join(str(x[0]) for x in lst)}")
    print("\n".join(log))
    print("total replacements:", tot, "files changed:", len(changed))
    for (rn, ch), lst in SKIPPED.items():
        print("SKIPPED (unit count mismatch):", rn, ch, lst[:10])
    for u in UNHANDLED[:60]:
        print("UNHANDLED:", u)
    if "--mm" in sys.argv:
        for u in MISMATCH:
            print("MISMATCH:", u[0], u[1], "\n   P:", u[2], "\n   H:", u[3])
    open(os.path.join(HERE, "align-preview.txt"), "w", encoding="utf-8", newline="\n").write("\n".join(preview))
    if DRY:
        print("(dry run: nothing written; preview in align-preview.txt)")
        return
    os.makedirs(BAK, exist_ok=True)
    for name in CHAPTERS + ["preamble"]:
        b = os.path.join(BAK, name + ".md")
        if not os.path.exists(b):
            shutil.copy2(os.path.join(HDIR, name + ".md"), b)
    for name, text in changed.items():
        open(os.path.join(HDIR, name + ".md"), "w", encoding="utf-8", newline="\n").write(text)
    open(os.path.join(HERE, "align-log.tsv"), "w", encoding="utf-8", newline="\n").write("\n".join(log) + "\n")
    print("written")


if __name__ == "__main__":
    main()
