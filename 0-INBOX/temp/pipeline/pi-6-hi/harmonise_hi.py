"""Consistency (harmonise) pass for the pi-6 Hindi plain zero-shot (Yamaka).

Applies fixed old -> new strings (some regex patterns, rx=True; the replacement may be a callable; kind "fn" rules
get the whole Hindi line and return it) to the Hindi chapter files. A rule touches a Hindi line ONLY when the
aligned Pāli line (non-empty line i <-> non-empty line i) matches the rule's Pāli pattern, and only in the
chapter groups listed for it (group = leading number of the file name: 1 … 10).
Line counts, block IDs, heading levels, dashes and '[' counts are never touched (asserted per changed line).
Protected (user-approved, never changed): preamble.md, 1-mulayamaka.md non-empty lines 1-122,
2-01-khandhayamaka.md non-empty lines 1-27, 219-248, 518-547.
Backup of the pre-pass files: backup-pre-harmonise/ (made once, if missing). The pass always reads from the
backup, so it is idempotent: rerunning it rebuilds the same output. Log: harmonise-log.tsv
(rule, file, replacements, lines).

usage: python -I -X utf8 harmonise_hi.py [--dry]
"""
import os, re, sys, shutil, collections

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PDIR = os.path.join(ROOT, r"AI_translation\pali\pi-6_split_chapters")
HDIR = os.path.join(ROOT, r"AI_translation\hindi\pi-6-hindi-plain-zeroshot_split_chapters")
HERE = os.path.join(ROOT, r"0-INBOX\temp\pipeline\pi-6-hi")
BAK = os.path.join(HERE, "backup-pre-harmonise")
sys.path.insert(0, HERE)
from hz6_common import PARTS  # noqa: E402

PROTECTED = {"preamble": None,  # whole file
             "1-mulayamaka": [(1, 122)],
             "2-01-khandhayamaka": [(1, 27), (219, 248), (518, 547)]}

R = []  # (id, pali_regex, old, new, kind, groups)
DEV = r"\u0900-\u097F"
E = r"(?![" + DEV + r"])"          # end of a Devanagari word
B = r"(?<![" + DEV + r"-])"         # start of a Devanagari word


def g(*nums):
    return {str(n) for n in nums}


def rule(rid, pali, old, new, kind="str", groups=None):
    R.append((rid, pali, old, new, kind, groups))


NOT7 = g(2, 3, 4, 5, 6, 8, 9, 10)

# ============================================================================== brief item 1: sense-organ beings
# One scheme for the whole book = the Indriya builder (build_10a_hi MODS, = the terms-file pattern
# sahetuka/ahetuka «मूल वाला / मूल से रहित»): sa-X-ka = «X वाले», a-X-ka = «X से रहित», several joined « और »;
# a modifier comes before the place (build_10a: «आँख से रहित इंद्रिय-सुखों के लोक में जन्म लेने वालों में»).
ORGANS = r"(भौतिक रूप|आँख|कान|नाक|जीभ|शरीर|मन)"
SAKA = r"\b([Ss]a|[Aa])(cakkhuk|sotak|ghānak|jivhak|kāyak|rūpak|cittak)"
# Āyatana chapter (3-01 … 3-06): «आँख के साथ / बिना आँख के»
rule("I1-organs", SAKA, ORGANS + r" के साथ पर बिना " + ORGANS + " के", r"\1 वाले और \2 से रहित", "rx", g(3))
rule("I1-organs", SAKA, r"बिना " + ORGANS + " के पर " + ORGANS + " के साथ", r"\1 से रहित और \2 वाले", "rx", g(3))
rule("I1-organs", SAKA, r"बिना " + ORGANS + " और " + ORGANS + " के", r"\1 से रहित और \2 से रहित", "rx", g(3))
rule("I1-organs", SAKA, B + ORGANS + " और " + ORGANS + " के साथ", r"\1 वाले और \2 वाले", "rx", g(3))
rule("I1-organs", SAKA, r"बिना " + ORGANS + " के", r"\1 से रहित", "rx", g(3))
rule("I1-organs", SAKA, B + ORGANS + " के साथ", r"\1 वाले", "rx", g(3))
# Dhātu chapter (4): «आँख वाले लेकिन कान-रहित», «आँख और कान वाले», «आँख-रहित»
rule("I1-organs", SAKA, ORGANS + " वाले लेकिन " + ORGANS + "-रहित", r"\1 वाले और \2 से रहित", "rx", g(4))
rule("I1-organs", SAKA, B + ORGANS + " और " + ORGANS + " वाले", r"\1 वाले और \2 वाले", "rx", g(4))
rule("I1-organs", SAKA, B + ORGANS + "-रहित", r"\1 से रहित", "rx", g(4))
# modifier before the place (3-0x had «इंद्रिय-सुखों के लोक में आँख के साथ जन्म लेने वालों में»)
PLACE = r"(इंद्रिय-सुखों के लोक|सूक्ष्म भौतिक लोक|अभौतिक लोक|पाँच समूहों वाले अस्तित्व|शुद्ध निवास लोक)"
MODS = r"((?:भौतिक रूप|आँख|कान|नाक|जीभ|शरीर|मन) (?:वाले|से रहित)(?: और (?:भौतिक रूप|आँख|कान|नाक|जीभ|शरीर|मन) (?:वाले|से रहित))*)"
rule("I1-organ-order", SAKA + r"ānaṃ (kāmāvacar|rūpāvacar|arūp|pañcavokār|suddhāvās)",
     PLACE + " में " + MODS + r" (जन्म लेने|मरने) वालों में", r"\2 \1 में \3 वालों में", "rx", g(3))

# ============================================================================== brief item 2: the sota pun
# = 3-01 / 10-01 «दिव्य कान और तृष्णा की धारा, कान हैं» (plain Hindi, no Pāli gloss; 4 had «तृष्णा का प्रवाह»
# and «“कान” (सोत)»)
rule("I2-sota", r"[Tt]aṇhāsot", "तृष्णा का प्रवाह", "तृष्णा की धारा", "str", g(4))
rule("I2-sota", r"[Tt]aṇhāsot", "“कान” (सोत)", "कान", "str", g(4))

# ============================================================================== brief item 3: catuvokāra pañcavokāra
# = build_2_hi (Khandha) «चार या पाँच समूहों वाले अस्तित्व» in every case form
CP = r"[Cc]atuvokār\w* pañcavokār"
rule("I3-catupanca", CP, "चार समूहों वाले अस्तित्व के प्राणियों में और पाँच समूहों वाले अस्तित्व के प्राणियों में",
     "चार या पाँच समूहों वाले अस्तित्व के प्राणियों में", "str", NOT7)
rule("I3-catupanca", CP, "चार समूहों वाले अस्तित्व और पाँच समूहों वाले अस्तित्व", "चार या पाँच समूहों वाले अस्तित्व", "str", NOT7)
rule("I3-catupanca", CP, "चार समूहों वाले अस्तित्व या पाँच समूहों वाले अस्तित्व", "चार या पाँच समूहों वाले अस्तित्व", "str", NOT7)
rule("I3-catupanca", CP, "चार समूहों वाले और पाँच समूहों वाले अस्तित्व", "चार या पाँच समूहों वाले अस्तित्व", "str", NOT7)

# ============================================================================== brief item 4: Natthi
# Same context everywhere (a question with no case to answer) -> «ऐसा कोई नहीं है।» (build_2_hi, 174 of 322)
rule("I4-natthi", r"\bNatthi\b", "ऐसा नहीं होता।", "ऐसा कोई नहीं है।", "str", g(7))

# ============================================================================== 6. other divergences
# B1 X-ā cavantānaṃ = «X से मरने वालों में» (build_2_hi; 3-0x had «X में मरने वालों में»)
rule("B1-cavanta-abl", r"ā cavantānaṃ", r"(लोक|अस्तित्व) में मरने वालों", r"\1 से मरने वालों", "rx", g(3))

# B2 Pacchimabhavikānaṃ X upapajjantānaṃ = one group «X में अंतिम जन्म लेने वालों में» (build_2_hi);
#    10-09 … 10-11 split it into «अंतिम जन्म वालों में, X में जन्म लेने वालों में»
PB = r"[Pp]acchimabhavikānaṃ (\w+aṃ |itthīnaṃ |purisānaṃ |saghānakānaṃ )upapajjant"
rule("B2-pacchimabhavika", PB, r"(?<!में )अंतिम जन्म वालों में(?:,| और) " + PLACE + " में जन्म लेने वालों में",
     r"\1 में अंतिम जन्म लेने वालों में", "rx", g(10))
rule("B2-pacchimabhavika", PB, r"(?<!में )अंतिम जन्म वालों में(?:,| और) जन्म लेने (वाली स्त्रियों|वाले पुरुषों) में",
     r"अंतिम जन्म लेने \1 में", "rx", g(10))
rule("B2-pacchimabhavika", PB, r"(?<!में )अंतिम जन्म वालों में(?:,| और) नाक वाले जन्म लेने वालों में",
     r"नाक वाले अंतिम जन्म लेने वालों में", "rx", g(10))

# B3 "… parinibbāyissanti tesaṃ upapajjantānaṃ / cavantānaṃ" = «…, उनमें से जन्म लेने / मरने वालों में»
#    (build_2_hi, 3-0x, 5-0x); 6-0x and 10-09 … 10-11 had «…, उन मरने वालों में»
rule("B3-tesam-cavanta", r"parinibbāyissanti (tesaṃ|tāsaṃ) (upapajjant|cavant)",
     r"(पाएँगे|पाएँगी), उन (जन्म लेने|मरने) (वालों|वाली स्त्रियों) में", r"\1, उनमें से \2 \3 में", "rx", NOT7)

# B4 Suddhāvāsānaṃ dutiye citte vattamāne = «शुद्ध निवास लोक के प्राणियों में दूसरे मन के चलते समय»
#    (5-0x, 9-0x: Pāli order, more occurrences); 10-05, 10-12 had the moment first
rule("B4-dutiye", r"[Ss]uddhāvāsānaṃ dutiye",
     r"दूसरे ((?:\S+ )?)मन के चलते समय शुद्ध निवास लोक के प्राणियों में",
     r"शुद्ध निवास लोक के प्राणियों में दूसरे \1मन के चलते समय", "rx", g(10))

# B5 Sabbesaṃ cittassa uppāda-/bhaṅgakkhaṇe = «सभी के मन के … क्षण में» (6-0x, 9-0x: 128 lines)
#    over «सबमें मन के …» (10-0x: 70) and «सभी में मन के …» (5-0x: 7)
rule("B5-sabbesam-cittassa", r"[Ss]abbesaṃ cittassa", r"(?:सबमें|सभी में) मन के (उत्पन्न|भंग) होने के क्षण में",
     r"सभी के मन के \1 होने के क्षण में", "rx", g(5, 10))

# B6 yassa cittassa anantarā X uppajjissati (tesaṃ) = «जिनमें इस मन के ठीक बाद X उत्पन्न होगा, उनमें»
#    (6-0x: 45 lines) over «जिनमें ऐसा मन है जिसके ठीक बाद …» (10-12: 7)
rule("B6-anantara", r"yassa cittassa anantarā \w+ uppajjissati(?! tassa)", "जिनमें ऐसा मन है जिसके ठीक बाद",
     "जिनमें इस मन के ठीक बाद", "str", g(10))

# B7 rūpāvacarānaṃ arūpāvacarānaṃ = «सूक्ष्म भौतिक लोक के प्राणियों में और अभौतिक लोक के प्राणियों में»
#    (3-0x = build_2_hi chunk joining; 6-0x had «सूक्ष्म भौतिक लोक और अभौतिक लोक के प्राणियों में»)
rule("B7-rupa-arupa-beings", r"[Rr]ūpāvacarānaṃ arūpāvacarānaṃ",
     "सूक्ष्म भौतिक लोक और अभौतिक लोक के प्राणियों में",
     "सूक्ष्म भौतिक लोक के प्राणियों में और अभौतिक लोक के प्राणियों में", "str", g(6))

# B8 being/place chunks: every chunk keeps its «में» (build_2_hi, 3-0x: «A में और B में», «A में, B में और C में»);
#    10-0x dropped «में» on plain-noun chunks («A के प्राणियों और B के प्राणियों में»)
rule("B8-chunk-me", r"\b(tesaṃ|tāsaṃ|tattha)\b", B + r"(वालों|प्राणियों|लोगों)(?=, | और )", r"\1 में", "rx", g(10))


# B9 chunk joining: the last chunk joined with « और » (build_2_hi, 3-0x, 10-0x);
#    5-0x, 6-0x, 8, 9-0x joined every chunk with ", " (and 5-0x had ", और जो …" in the middle of a chain)
SEG = re.compile(r"(?<=[।?])(\s+)")
VERB = re.compile(r" (उत्पन्न|समाप्त) (भी )?(नहीं )?(होता|होतीं|होती|होते|हुआ|हुईं|हुई|हुए|होगा|होगी|होंगे|होंगी|हो चुका|हो चुकी|हो चुके)" + E)
REL_AFTER = re.compile(r",\s*(उस|उन|उनमें|वे|जिस)" + E)
OK_FOLLOW = ("उनमें", "उन ", "उस ", "वे ", "और जो ", "जो ", "जिस ", "दूसरी", "तीसरी", "चौथी")
SKIPPED = []


def _pieces(w):
    out, buf = [], ""
    for r in w.split(", "):
        buf = (buf + ", " + r) if buf else r
        if re.search(r"(में|समय)( \[[^\]]*\])?$", buf):
            out.append(buf); buf = ""
    if buf:
        out.append(buf)
    return out


MASK = "\x00"


def _fix_sentence(s, ctx):
    if s.rstrip().endswith("?"):
        return s, 0
    # variant brackets: hide their inner ", " so they never split a chunk
    s = re.sub(r"\[[^\]]*\]", lambda mm: mm.group(0).replace(", ", MASK), s)
    m = None
    for mm in VERB.finditer(s):
        if REL_AFTER.match(s, mm.end()):
            continue
        m = mm
        break
    stop = m.start() if m else s.find(" वहाँ")  # abbreviated answers ("… वहाँ दुःख का सत्य…") have no verb
    if stop < 0:
        return s.replace(MASK, ", "), 0
    ends = [x.end() for x in re.finditer(r"(में|समय)(?=[ ,]|$)", s[:stop])]
    if not ends:
        return s.replace(MASK, ", "), 0
    end = ends[-1]
    w = s[:end]
    if "…" in w:
        return s.replace(MASK, ", "), 0
    new, n = _join(w, ctx)
    return (new + s[end:]).replace(MASK, ", "), n


def _join(w, ctx):
    ps = _pieces(w)
    if len(ps) < 2:
        return w, 0
    for p in ps:
        for k in [x.end() for x in re.finditer(", ", p)]:
            if not p[k:].startswith(OK_FOLLOW):
                SKIPPED.append((ctx, "list-comma", w.replace(MASK, ", ")))
                return w, 0
    pc = [re.sub(r" ?\[[^\]]*\]", "", p) for p in ps]  # checks ignore variant brackets
    has_join = [bool(re.search(r"(में|समय) और ", p)) for p in pc]
    lead = [i for i, p in enumerate(ps) if p.startswith("और ")]
    last = len(ps) - 1
    if any(has_join):
        if lead or any(has_join[:-1]):
            SKIPPED.append((ctx, "mixed-join", w.replace(MASK, ", ")))
        return w, 0
    ps2 = [p[len("और "):] if (i in lead and i != last) else p for i, p in enumerate(ps)]
    if last in lead:
        new = ", ".join(ps2[:-1]) + " " + ps2[-1]
    else:
        new = ", ".join(ps2[:-1]) + " और " + ps2[-1]
    return new, int(new != w)


SEG = re.compile(r"(?<=[।?…])(\s+)")


def fix_join(line, ctx):
    parts = SEG.split(line)
    n = 0
    for i in range(0, len(parts), 2):
        parts[i], k = _fix_sentence(parts[i], ctx)
        n += k
    return "".join(parts), n


rule("B9-chunk-join", r"\b(tesaṃ|tāsaṃ|tattha)\b", None, fix_join, "fn", g(2, 3, 4, 5, 6, 8, 9, 10))

# B10 "yo … so …" questions of the pariññā / pajahana / bhāvanā sections = «जो व्यक्ति …, क्या वह …?»
#     (Anusaya 7-03 … 7-08, build_7a_hi: ~620 question lines) over «जो …, क्या वह …?» (2-02, 3-06, 4, 5-03,
#     6-02, 9-03, 10-13: ~165); past «जिसने» = «जिस व्यक्ति ने»
YO = (r"^(\(\w+\) )?[Yy]o (vā pana )?([^.?]*?(parijān|pajah|nappajah|bhāve|bhāvi|sacchikar|sacchikā|sacchākāsi)[^.]*\?"
      r"|…pe…\?)")
rule("B10-yo-vyakti", YO, r"^((?:\([कख]\) )?(?:और )?)जो (?!व्यक्ति)", r"\1जो व्यक्ति ", "rx1", NOT7 - g(7))
rule("B10-yo-vyakti", YO, r"^((?:\([कख]\) )?(?:और )?)जिसने ", r"\1जिस व्यक्ति ने ", "rx1", NOT7 - g(7))

# B11 bare raso = «स्वाद» (3-01: the bare word = the noun of the compound, rasāyatana / rasadhātu = स्वाद का …);
#     4 had «रस» (also in Attharaso … = «अर्थ का स्वाद, शिक्षा का स्वाद और मुक्ति का स्वाद», 3-01)
rule("B11-raso", r"\b[Rr]as(o|aṃ|añca)\b|[Aa]ttharas", B + "रस" + E, "स्वाद", "rx", g(4))

# ============================================================================== editorial notes (parentheses)
# yassaka / yatthaka / yassayatthaka = «व्यक्ति वाला भाग / स्थान वाला भाग / व्यक्ति और स्थान वाला भाग»
# (build_2_hi «स्थान वाला भाग», 6-0x, 8; «खंड» stays for vāra); sadisaṃ = «समान» (3, 4, 6);
# vitthāretabbaṃ = «… का विस्तार करना चाहिए» (3, 4 = build_2_hi family); vibhajitabbaṃ / vibhattaṃ =
# «… का विभाजन करना चाहिए / किया गया है» (2-02 build_2_hi, 4); cakkaṃ bandhitabbaṃ = «चक्र पूरा करना चाहिए» (4);
# saṃkhittaṃ = «संक्षिप्त किया गया है» (4, build_2 family); asammohantena = «बिना भ्रम के»;
# anulomampi paccanīkampi = «सकारात्मक भी और नकारात्मक भी» (3, 6).
ED = r"\("
YS = "(व्यक्ति वाला भाग भी और व्यक्ति और स्थान वाला भाग भी समान हैं"
NOTES = [
    (g(3), "(चक्र को जोड़ लेना चाहिए)", "(चक्र पूरा करना चाहिए)"),
    (g(3), "(एक-एक शब्द पर आधारित चक्र को बिना भ्रम के जोड़ लेना चाहिए)", "(एक-एक शब्द पर आधारित चक्र बिना भ्रम के पूरा करना चाहिए)"),
    (g(3), "(चक्र जोड़ते समय हर जगह “हाँ” कहना चाहिए)", "(चक्र पूरा करते समय हर जगह “हाँ” कहना चाहिए)"),
    (g(3), "(संक्षेप में, व्यक्ति वाले खंड के समान [", "(संक्षिप्त किया गया है, व्यक्ति वाले भाग के समान ["),
    (g(3), "(संक्षेप में)", "(संक्षिप्त किया गया है)"),
    (g(3), "(स्थान वाला खंड वर्तमान में भी,", "(स्थान वाला भाग वर्तमान में भी,"),
    (g(3), "(व्यक्ति और स्थान वाले खंड का भी इसी प्रकार विस्तार करना चाहिए)", "(व्यक्ति और स्थान वाले भाग का भी इसी प्रकार विस्तार करना चाहिए)"),
    (g(3), "(व्यक्ति और स्थान वाला खंड भी व्यक्ति वाले खंड के समान है)", "(व्यक्ति और स्थान वाला भाग भी व्यक्ति वाले भाग के समान है)"),
    (g(3), "स्थान वाला खंड हर जगह समान है)", "स्थान वाला भाग हर जगह समान है)"),
    (g(3), "(स्थान वाले खंड में “नहीं” उत्तर नहीं देना चाहिए, स्थान वाले खंड को बाकी स्थान वाले खंडों के समान बनाना चाहिए, स्थान वाला खंड तीनों खंडों में समान है)",
     "(स्थान वाले भाग में “नहीं” उत्तर नहीं देना चाहिए, स्थान वाले भाग को बाकी स्थान वाले भागों के समान बनाना चाहिए, स्थान वाला भाग तीनों खंडों में समान है)"),
    (g(3), "(व्यक्ति वाला खंड भी और व्यक्ति और स्थान वाला खंड भी समान हैं)", YS + ")"),
    (g(3), "का विश्लेषण किया गया है, वैसे ही", "का विभाजन किया गया है, वैसे ही"),
    (g(3), "विश्लेषण करना चाहिए", "विभाजन करना चाहिए"),
    (g(3), "का व्यक्ति वाला खंड भी, स्थान वाला खंड भी, व्यक्ति और स्थान वाला खंड भी,", "का व्यक्ति वाला भाग भी, स्थान वाला भाग भी, व्यक्ति और स्थान वाला भाग भी,"),
    (g(3), "सकारात्मक भी और नकारात्मक भी विश्लेषण किया गया है", "सकारात्मक भी और नकारात्मक भी विभाजन किया गया है"),
    (g(5), "(“जिस व्यक्ति में” वाले खंड को भी और “जिस व्यक्ति में जिस स्थान पर” वाले खंड को भी इसी तरह विस्तार से कहना चाहिए)",
     "(व्यक्ति वाले भाग का भी और व्यक्ति और स्थान वाले भाग का भी इसी प्रकार विस्तार करना चाहिए)"),
    (g(5), "(“जिस स्थान पर” वाला खंड भी हर जगह एक जैसा है। पाठ का अंतर पहले वाले “जिस स्थान पर” वाले खंड जैसा है)",
     "(स्थान वाला भाग भी हर जगह समान है। पाठ का अंतर पहले वाले स्थान वाले भाग के समान है)"),
    (g(5), "(“जिस स्थान पर” वाले सभी खंड एक जैसे हैं)", "(स्थान वाले सभी भाग समान हैं)"),
    (g(5), "(“जिस स्थान पर” वाले खंड को भी “जिस व्यक्ति में जिस स्थान पर” वाले खंड जैसा बनाना चाहिए)",
     "(स्थान वाले भाग को भी व्यक्ति और स्थान वाले भाग के समान बनाना चाहिए)"),
    (g(5), "(“जिस स्थान पर” वाला खंड उत्पन्न होने में, समाप्त होने में और उत्पन्न होने और समाप्त होने में भी एक जैसा है, कोई अंतर नहीं है)",
     "(स्थान वाला भाग उत्पन्न होने में भी, समाप्त होने में भी, उत्पन्न होने और समाप्त होने में भी समान है, कोई अंतर नहीं है)"),
    (g(5), "(“जिस व्यक्ति में जिस स्थान पर” वाले खंड को भी इसी तरह विस्तार से कहना चाहिए)",
     "(व्यक्ति और स्थान वाले भाग का भी इसी प्रकार विस्तार करना चाहिए)"),
    (g(5), "(“जिस व्यक्ति में” वाला खंड और “जिस व्यक्ति में जिस स्थान पर” वाला खंड भी एक जैसे हैं", YS),
    (g(5), ", पर “जिस व्यक्ति में जिस स्थान पर” वाले खंड में “समाप्ति की ध्यान-अवस्था में लीन लोगों में”",
     ", पर व्यक्ति और स्थान वाले भाग में “समाप्ति की ध्यान-अवस्था में लीन लोगों में”"),
    (g(5), "(जैसे उत्पन्न होने के खंड में अतीत के प्रश्न सकारात्मक और नकारात्मक दोनों रूपों में बाँटकर बताए गए हैं, वैसे ही समाप्त होने में भी बाँटकर बताने चाहिए, कोई अंतर नहीं है)",
     "(जैसे उत्पन्न होने के खंड में अतीत के प्रश्नों का सकारात्मक भी और नकारात्मक भी विभाजन किया गया है, वैसे ही समाप्त होने में भी विभाजन करना चाहिए, कोई अंतर नहीं है)"),
    (g(5), "(“जिस स्थान पर” वाला खंड उत्पन्न होने के खंड में, समाप्त होने के खंड में और उत्पन्न होने और समाप्त होने के खंड में भी एक जैसा है, कोई अंतर नहीं है)",
     "(स्थान वाला भाग उत्पन्न होने के खंड में भी, समाप्त होने के खंड में भी, उत्पन्न होने और समाप्त होने के खंड में भी समान है, कोई अंतर नहीं है)"),
    (g(5), "(अतीत के प्रश्न जैसे उत्पन्न होने के खंड में बाँटकर बताए गए हैं, वैसे ही उत्पन्न होने और समाप्त होने के खंड में भी सकारात्मक और नकारात्मक दोनों रूपों में बाँटकर बताने चाहिए)",
     "(जैसे उत्पन्न होने के खंड में अतीत के प्रश्नों का विभाजन किया गया है, वैसे ही उत्पन्न होने और समाप्त होने के खंड में भी सकारात्मक भी और नकारात्मक भी विभाजन करना चाहिए)"),
    (g(5), "] उत्पन्न होने के खंड में भी और उत्पन्न होने और समाप्त होने के खंड में भी, “जिस व्यक्ति में” वाले खंड में, “जिस स्थान पर” वाले खंड में और “जिस व्यक्ति में जिस स्थान पर” वाले खंड में, सकारात्मक और नकारात्मक दोनों रूपों में एक जैसे हैं, इन्हें बिना भ्रम के बाँटकर बताना चाहिए)",
     "] उत्पन्न होने के खंड में भी और उत्पन्न होने और समाप्त होने के खंड में भी, व्यक्ति वाले भाग में भी, स्थान वाले भाग में भी, व्यक्ति और स्थान वाले भाग में भी, सकारात्मक भी और नकारात्मक भी समान हैं, इनका बिना भ्रम के विभाजन करना चाहिए)"),
    (g(5), "(जैसे समाप्त होने के खंड में अतीत और भविष्य के प्रश्न [", "(जैसे समाप्त होने के खंड में अतीत और भविष्य के प्रश्नों ["),
    (g(5), "] सकारात्मक और नकारात्मक दोनों रूपों में बाँटकर बताए गए हैं, वैसे ही उत्पन्न होने और समाप्त होने के खंड में भी बिना भ्रम के बाँटकर बताने चाहिए)",
     "] का सकारात्मक भी और नकारात्मक भी विभाजन किया गया है, वैसे ही उत्पन्न होने और समाप्त होने के खंड में भी बिना भ्रम के विभाजन करना चाहिए)"),
    (g(6), "(व्यक्ति वाले भाग को भी और व्यक्ति और स्थान वाले भाग को भी समान रूप से विस्तार देना चाहिए,",
     "(व्यक्ति वाले भाग का भी और व्यक्ति और स्थान वाले भाग का भी इसी प्रकार विस्तार करना चाहिए,"),
    (g(6), "(व्यक्ति वाला भाग भी और व्यक्ति और स्थान वाला भाग भी समान है", YS),
    (g(6), "(जैसे उत्पन्न होने के खंड में अतीत के प्रश्न व्यक्ति वाले भाग में भी और व्यक्ति और स्थान वाले भाग में भी, सकारात्मक भी और नकारात्मक भी, विभाजित किए गए हैं, वैसे ही समाप्त होने के खंड में भी विभाजित करने चाहिए, कोई अंतर नहीं है।)",
     "(जैसे उत्पन्न होने के खंड में अतीत के प्रश्नों का व्यक्ति वाले भाग में भी और व्यक्ति और स्थान वाले भाग में भी, सकारात्मक भी और नकारात्मक भी, विभाजन किया गया है, वैसे ही समाप्त होने के खंड में भी विभाजन करना चाहिए, कोई अंतर नहीं है।)"),
    (g(6), "(अतीत के प्रश्न को उत्पन्न होने के खंड में भी, समाप्त होने के खंड में भी और उत्पन्न होने और समाप्त होने के खंड में भी समान रूप से विस्तार देना चाहिए)",
     "(अतीत के प्रश्नों का उत्पन्न होने के खंड में भी, समाप्त होने के खंड में भी और उत्पन्न होने और समाप्त होने के खंड में भी इसी प्रकार विस्तार करना चाहिए)"),
    (g(6), "(जैसे उत्पन्न होने के खंड में वर्तमान और अतीत के प्रश्न सकारात्मक भी और नकारात्मक भी विभाजित किए गए हैं, वैसे ही उत्पन्न होने और समाप्त होने के खंड में भी वर्तमान और अतीत के प्रश्न सकारात्मक भी और नकारात्मक भी विभाजित करने चाहिए।)",
     "(जैसे उत्पन्न होने के खंड में वर्तमान और अतीत के प्रश्नों का सकारात्मक भी और नकारात्मक भी विभाजन किया गया है, वैसे ही उत्पन्न होने और समाप्त होने के खंड में भी वर्तमान और अतीत के प्रश्नों का सकारात्मक भी और नकारात्मक भी विभाजन करना चाहिए।)"),
    (g(6), "(जैसे समाप्त होने के खंड में अतीत और भविष्य के प्रश्न सकारात्मक भी और नकारात्मक भी हैं, वैसे ही उत्पन्न होने और समाप्त होने के खंड में भी अतीत और भविष्य के प्रश्न सकारात्मक भी और नकारात्मक भी बिना भ्रमित हुए, समाप्त होने के खंड के समान विभाजित करने चाहिए, कोई अंतर नहीं है।)",
     "(जैसे समाप्त होने के खंड में अतीत और भविष्य के प्रश्न सकारात्मक भी और नकारात्मक भी हैं, वैसे ही उत्पन्न होने और समाप्त होने के खंड में भी अतीत और भविष्य के प्रश्नों का सकारात्मक भी और नकारात्मक भी बिना भ्रम के, समाप्त होने के खंड के समान विभाजन करना चाहिए, कोई अंतर नहीं है।)"),
    (g(6), "(जैसे “समूहों पर प्रश्नों के जोड़े” में पूरी तरह समझने का खंड विभाजित किया गया है, वैसे ही “रचनाओं पर प्रश्नों के जोड़े” में भी पूरी तरह समझने का खंड विभाजित करना चाहिए।)",
     "(जैसे “समूहों पर प्रश्नों के जोड़े” में पूरी तरह समझने के खंड का विभाजन किया गया है, वैसे ही “रचनाओं पर प्रश्नों के जोड़े” में भी पूरी तरह समझने के खंड का विभाजन करना चाहिए।)"),
    (g(7), "(विस्तार से कहना चाहिए)", "(विस्तार करना चाहिए)"),
    (g(10), "(पहले जैसा)", "(समान)"),
]
for grp_, old, new in NOTES:
    rule("N-notes", ED, old, new, "str", grp_)
# the same terms inside variant brackets and the rest of the 5-0x notes
YK = r"[Yy]assak|[Yy]atthak|yassayatthak"
rule("N-yassaka", YK, "(“जिस व्यक्ति में” वाला खंड [", "(व्यक्ति वाला भाग भी [", "str", g(5))
rule("N-yassaka", YK, r"“जिस व्यक्ति में जिस स्थान पर” वाल(ा|े) खंड", r"व्यक्ति और स्थान वाल\1 भाग", "rx", NOT7)
rule("N-yassaka", YK + r"|sadis", "भाग भी एक जैसे हैं", "भाग भी समान हैं", "str", g(5))


# ======================================================================================
def group(part):
    return part.split("-")[0]


def nonempty_idx(lines):
    return [i for i, l in enumerate(lines) if l.strip()]


def dashes(t):
    return t.count("—") + t.count("–")


def protected(part, k):
    if part not in PROTECTED:
        return False
    rng = PROTECTED[part]
    return rng is None or any(a <= k + 1 <= b for a, b in rng)


def main(dry=False):
    if not os.path.isdir(BAK):
        os.makedirs(BAK)
        for part in PARTS:
            shutil.copy2(os.path.join(HDIR, part + ".md"), os.path.join(BAK, part + ".md"))
        print("backup made:", BAK)
    log = collections.defaultdict(lambda: [0, 0])  # (rid, part) -> [replacements, lines]
    changed_lines = collections.Counter()
    hit_idx = set()
    blocked = []
    comp = []
    for rid, p, old, new, kind, groups in R:
        o = re.compile(old) if kind in ("rx", "rx1") else old
        comp.append((rid, re.compile(p), o, new, kind, groups))
    for part in PARTS:
        pl = [l for l in open(os.path.join(PDIR, part + ".md"), encoding="utf-8-sig").read().splitlines() if l.strip()]
        raw = open(os.path.join(BAK, part + ".md"), encoding="utf-8").read()
        bom = raw.startswith("\ufeff")
        text = raw.lstrip("\ufeff")
        assert "\r" not in text, part
        el = text.split("\n")
        idx = nonempty_idx(el)
        assert len(idx) == len(pl), (part, len(idx), len(pl))
        grp = group(part)
        for k, li in enumerate(idx):
            p, e0 = pl[k], el[li]
            e = e0
            for ri, (rid, pr, old, new, kind, groups) in enumerate(comp):
                if groups and grp not in groups:
                    continue
                if not pr.search(p):
                    continue
                if kind == "fn":
                    e2, n = new(e, f"{part}:{k + 1}")
                elif kind in ("rx", "rx1"):
                    e2, n = old.subn(new, e, count=1 if kind == "rx1" else 0)
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
                if protected(part, k):
                    blocked.append((part, k + 1))
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
    if not dry:
        with open(os.path.join(HERE, "harmonise-log.tsv"), "w", encoding="utf-8") as f:
            f.write("rule\tfile\treplacements\tlines\n")
            for (rid, part), (n, l) in sorted(log.items(), key=lambda kv: (kv[0][0], PARTS.index(kv[0][1]))):
                f.write(f"{rid}\t{part}\t{n}\t{l}\n")
        with open(os.path.join(HERE, "harmonise-skipped.txt"), "w", encoding="utf-8") as f:
            for ctx, why, w in SKIPPED:
                f.write(f"{ctx}\t{why}\t{w}\n")
    tot = collections.defaultdict(lambda: [0, 0])
    for (rid, part), (n, l) in log.items():
        tot[rid][0] += n; tot[rid][1] += l
    for rid in sorted(tot):
        print(f"{rid:24s} repl={tot[rid][0]:5d} lines={tot[rid][1]:5d}")
    print("lines changed per file:", dict(changed_lines), "total", sum(changed_lines.values()))
    print("B9 sentences skipped:", collections.Counter(w for _, w, _ in SKIPPED))
    if blocked:
        print("BLOCKED (protected lines a rule would have changed):", blocked)
    for ri, r in enumerate(R):
        if ri not in hit_idx:
            print("NO HIT:", r[0], "|", str(r[2])[:100])


if __name__ == "__main__":
    main(dry="--dry" in sys.argv)
