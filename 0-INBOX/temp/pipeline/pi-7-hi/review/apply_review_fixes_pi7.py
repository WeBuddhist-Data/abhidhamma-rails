"""Review fixes for the pi-7 Hindi plain RAILS translation (Paṭṭhāna), from review/findings-r1..r10.md and the user
decisions of 2026-11-14 (fix-brief.md).

Rules are fixed old -> new strings ("str"), regex substitutions ("rx") or functions ("fnp": gets (hindi, pali, ctx),
returns (hindi, n)). A rule touches a Hindi line only when the aligned Pāli line (non-empty line i <-> i) matches the
rule's Pāli pattern, and optionally only in some files / block-ID segments / non-empty line numbers.
Two passes are not line rules: the triad/dyad names (U1, a function line rule with placeholders) and the abbreviated
condition-chain agreement (CH, a file pass that needs the nearest preceding formula head).

Protected lines (preamble.md, 1-00-paccaya.md, 1-01 non-empty lines 1-190 and 1235-1262) are changed only by the
user decisions that include them (U1, U2, U3, SC); any other rule that would touch them is blocked and reported.
Line counts, block IDs, heading levels, dashes and '[' counts never change (asserted per changed line).
Backup: backup-pre-fixes/ (made once); the pass always starts from it, so it can be rerun.
Logs: fixes-log.tsv (file, line, rule, old, new), names-change.tsv (Pāli | old Hindi | new Hindi).

usage: python -I -B -X utf8 apply_review_fixes_pi7.py [--dry]
"""
import os, re, sys, shutil, collections

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "rails"))
import ar7_common as C  # noqa: E402
from ar7_common import PARTS, PDIR, HDIR  # noqa: E402

BAK = os.path.join(HERE, "backup-pre-fixes")
PROTECTED = {"preamble": None, "1-00-paccaya": None, "1-01-kusalattika": [(1, 190), (1235, 1262)]}
OPEN_RULES = ("U1", "U2", "U3", "SC")       # user decisions that include the protected (sample) lines
DEV = "ऀ-ॣ०-ॿ"
B = r"(?<![" + DEV + r"-])"                 # start of a Devanagari word

R = []        # (rid, pali_rx, old, new, kind, files, ids, lines)
REPORT = []


def rule(rid, pali, old, new, kind="str", files=None, ids=None, lines=None):
    R.append((rid, pali, old, new, kind, files, ids, lines))


# =============================================================== r1
rule("R1-386-paripunna", r"Napacchājātapaccayā paripuṇṇaṃ",
     "पश्चात्-उत्पत्ति-कारण के बिना परिपूर्ण है,", "पश्चात्-उत्पत्ति-कारण का अभाव परिपूर्ण है,", ids={"7-2-386"})
rule("R1-gaṇite-oblique", r"gaṇite", "का अभाव को गिनने पर", "के अभाव को गिनने पर")
rule("R1-yatha-abhava", r"[Yy]athā [^()]*?na\w*paccayā, evaṃ", r"(\(जैसे [^,()]*?)के बिना है, वैसे",
     r"\1का अभाव है, वैसे", "rx")
rule("R1-bina-comma", r"paccayā \(", r"के बिना, \(", "के बिना (", "rx")

# =============================================================== r2
rule("R2-sahajato-label", r"Sahajāto –", r"(?<=। )के साथ जन्म लेकर –", "सह-उत्पत्ति –", "rx")
# one shape book-wide (2-03..2-08 order «इरादा कर्म-फल रूपी <Y> समूहों») + the subject comma: «इरादा, कर्म-फल रूपी …»
rule("R2-nana-shape", r"cetanā vipāk", r"इरादा,? कर्म-फल रूपी,? ", "इरादा, कर्म-फल रूपी ", "rx")
rule("R2-sankhare-ko", r"saṅkhāre aniccato", "निर्मित परिघटनाओं अनित्य", "निर्मित परिघटनाओं को अनित्य")
rule("R2-ahara-list", r"kabaḷīkāro āhāro",
     "बनने वाला, कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाला, कौर-कौर",
     "बनने वाला और कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाला कौर-कौर", ids={"7-5-74", "7-5-86"})
rule("R2-ahara-85", r"kabaḷīkāro āhāro",
     "बनने वाले समूह, कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाला कौर-कौर खाया जाने वाला भोजन, कर्म से",
     "बनने वाले समूह और कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाला कौर-कौर खाया जाने वाला भोजन कर्म से",
     ids={"7-5-85"})
rule("R2-ahara-singular", r"kabaḷīkāro āhāro",
     r"((?:^|[।;–…] )(?:(?!समूह|क्षमता|आधार|मूल |महाभूत)[^।;–…])*?कौर-कौर खाया जाने वाला भोजन [^।;]*?कारण) होते हैं",
     r"\1 होता है", "rx", ids={"7-5-72", "7-5-73", "7-5-74", "7-5-82", "7-5-83", "7-5-86"})
rule("R2-84-aur", r"purejātassa imassa", r"(समूहों? के लिए) (पहले उत्पन्न इस)", r"\1 और \2", "rx", ids={"7-5-84"})
rule("R2-84-verb", r"eko khandho tiṇṇannaṃ khandhānaṃ purejātassa",
     r"(एक समूह तीन समूहों के लिए और पहले उत्पन्न [^।]*?कारण) होते हैं", r"\1 होता है", "rx", ids={"7-5-84"})
rule("R2-vatthu-par", r"[Vv]atthuṃ (?:purejāta|vippayutta)paccayā", r"(?<=। )आधार (पूर्व-उत्पत्ति|अलगाव)-कारण से",
     r"आधार पर \1-कारण से", "rx", ids={"7-3-2", "7-3-4"})
rule("R2-vatthu-karan", r"vatthuṃ purejātapaccayā", "दो समूह, आधार पूर्व-उत्पत्ति-कारण से",
     "दो समूह, आधार के कारण पूर्व-उत्पत्ति-कारण से", ids={"7-4-69"})
rule("R2-105-verb", r"tadārammaṇatā", r"(आधार को अनित्य… उसी विषय को लेकर उत्पन्न) होती है", r"\1 होता है", "rx",
     ids={"7-4-105"})
rule("R2-102-no-aur", r"Kāyikaṃ sukhaṃ kāyikaṃ dukkhaṃ", "शारीरिक सुख और शारीरिक दुःख श्रद्धा",
     "शारीरिक सुख, शारीरिक दुःख श्रद्धा", ids={"7-4-102"})
rule("R2-mahabhuta-list", r"upādārūpānaṃ",
     "भौतिक रूपों के लिए किए गए कर्म से उत्पन्न भौतिक रूपों के लिए व्युत्पन्न भौतिक रूपों के लिए",
     "भौतिक रूपों के लिए, किए गए कर्म से उत्पन्न भौतिक रूपों के लिए और व्युत्पन्न भौतिक रूपों के लिए")
rule("R2-mahabhuta-list", r"upādārūpānaṃ", r"रूपों के लिए व्युत्पन्न भौतिक रूपों के लिए",
     "रूपों के लिए और व्युत्पन्न भौतिक रूपों के लिए", "rx")

# =============================================================== r3
rule("R3-88-dative", r"pacchimānaṃ pacchimānaṃ…pe…", "समूह और बाद-बाद की…", "समूह बाद-बाद के…", files=("2-03",))
rule("R3-101-note", r"ime sahetukā kātabbā", "(इन्हें मूल वाला करना चाहिए)", "(इन्हें मूल वाले बनाना चाहिए)")
rule("R3-111-idhapi", r"Idhāpi ārammaṇapaccayā upanissayapaccayā atthi, pāḷiyaṃ",
     "(यहाँ भी विषय-कारण से और प्रबल आश्रय-कारण से (प्रश्न) हैं,", "(यहाँ भी विषय-कारण और प्रबल आश्रय-कारण हैं,")
rule("R3-6-mahabhuta", r"sabbepi mahābhūtā kātabbā", "(सभी महाभूत भी करने चाहिए)", "(सभी महाभूत शामिल करने चाहिए)")
rule("R3-91-ellipsis", r".", "और ……", "और …", ids={"7-9-91"})

# =============================================================== r4
rule("R4-utu-gender", r"[Uu]ppannaṃ utu", "उत्पन्न हो चुकी तापमान", "उत्पन्न हो चुका तापमान")

# =============================================================== r5
rule("R5-imassa-kaya", r"imassa", "इस शरीर, इस और ", "इस ", files=("3-02",))
rule("R5-imassa-kaya", r"imassa", r"इस और (?=[^।]{0,80}शरीर के लिए)", "इस ", "rx", files=("3-02",))
rule("R5-110-navapi", r"vajjetabbā navapi", "पुनरावृत्ति-कारण में नौ के नौ छोड़ देने चाहिए",
     "पुनरावृत्ति-कारण के नौ के नौ प्रश्नों में इन्हें छोड़ देना चाहिए")
rule("R5-ayatana-oblique", r"āyatan", r"का इंद्रिय-क्षेत्र (?=(?:के|पर|को|से|में) )", "के इंद्रिय-क्षेत्र ", "rx")
rule("R5-adj-oblique", r"mahābhūt|rūpaṃ", r"वाला (एक महाभूत|भौतिक रूप) (?=(?:को|पर|के|से|में) )", r"वाले \1 ", "rx")
rule("R5-upadana-fem", r"upādān", "बाद-बाद के आसक्ति", "बाद-बाद की आसक्ति")
rule("R5-157-verb", r"ariyānaṃ maggo", "कुशलता के लिए प्रबल आश्रय-कारण के रूप में कारण होती है;",
     "कुशलता के लिए प्रबल आश्रय-कारण के रूप में कारण होता है;", ids={"7-25-157"})
rule("R5-U323-nitthita", r"[Mm]ahābhūtesu niṭṭhitesu", "महाभूतों के पूरे हो जाने पर", "महाभूतों का अंश समाप्त हो जाने पर")
rule("R5-60-verb-end", r"maggapaccayā… \(jhānampi", "मार्ग-कारण से उत्पन्न होती है… (", "मार्ग-कारण से… (",
     ids={"7-24-60"})
rule("R5-60-verb-end", r"avigatapaccayā\. \^7-24-60", "अविलीनता-कारण से। ^7-24-60",
     "अविलीनता-कारण से उत्पन्न होती है। ^7-24-60", ids={"7-24-60"})
rule("R5-156-verb", r"senāsanaṃ lokiyāya saddhāya", "शारीरिक दुःख के लिए प्रबल आश्रय-कारण के रूप में कारण होती है;",
     "शारीरिक दुःख के लिए प्रबल आश्रय-कारण के रूप में कारण होता है;", ids={"7-25-156"})
# Ariyā maggā vuṭṭhahitvā / ariyā maggaṃ upanissāya: «आर्य, मार्ग …» (r5, r8; the subject-comma rule)
rule("R5-ariya-comma", r"[Aa]riy", B + r"आर्य मार्ग", "आर्य, मार्ग", "rx")
rule("R5-ariya-comma", r"[Aa]riy", r"आर्य, मार्ग से उठकर (?=[^\s…])", "आर्य, मार्ग से उठकर, ", "rx")

# =============================================================== r6
rule("R6-kayagantha", r"kāyaganth", "ग़लत धारणा और काया की गाँठ", "ग़लत धारणा रूपी काया की गाँठ")
rule("R6-kayagantha", r"kāyaganth", "ग़लत धारणा, काया की गाँठ", "ग़लत धारणा रूपी काया की गाँठ")
rule("R6-kayagantha", r"kāyaganth", r"(?:के|का) आग्रह और काया की गाँठ", "के आग्रह रूपी काया की गाँठ", "rx")
rule("R6-kayagantha-aur", r"kāyaganth", "एक समूह, सदाचार", "एक समूह और सदाचार", files=("3-05",), lines={53, 136, 395})
rule("R6-U374-arupe", r"arūpeyeva", "अभौतिक लोक में ही पाँच प्रश्न", "केवल अभौतिक परिघटनाओं में ही पाँच प्रश्न")
rule("R6-245-aur", r"diṭṭhigatavippayuttaṃ lobhasahagataṃ", "ग़लत दृष्टि से अलग या लोभ", "ग़लत दृष्टि से अलग और लोभ")
rule("R6-pacchajato-label", r"Pacchājāto –", "बाद में उत्पन्न –", "पश्चात्-उत्पत्ति –")
rule("R6-pacchajata-adj", r"paccayo – pacchājātā \w", r"– पश्चात्-उत्पत्ति, (?!आहार|क्षमता)", "– बाद में उत्पन्न ", "rx")
rule("R6-akincanna-comma", r"ākiñcaññāyatan\w* nevasaññānāsaññāyatan", "का क्षेत्र न पहचान न अ-पहचान",
     "का क्षेत्र, न पहचान न अ-पहचान")

# =============================================================== r7
rule("R7-72-comma", r"nocitte pahīne", "मन रूपी न होने वाले छोड़े जा चुके", "मन रूपी न होने वाले, छोड़े जा चुके")
rule("R7-tatha", r"[Cc]ittasaṃsaṭṭhasamuṭṭhān\w* ca nocittasaṃsaṭṭhasamuṭṭhān",
     "मन से घुली-मिली और मन से उत्पन्न और मन से घुली-मिली और मन से उत्पन्न न होने वाली परिघटनाएँ",
     "मन से घुली-मिली और मन से उत्पन्न तथा मन से घुली-मिली और मन से उत्पन्न न होने वाली परिघटनाएँ")

# =============================================================== r8
rule("R8-samkilesika-masc", r"ceva no ca kiles",r"वाली(, पर स्वयं [^,।]{0,60}? न होने वाले समूह)", r"वाले\1", "rx",
     files=("4-01",), ids={"7-34-76", "7-34-77", "7-34-78", "7-34-79"})
rule("R8-hettha-likhitam", r"heṭṭhā likhitaṃ lekhaṃ", "(नीचे लिखे गए लेख को इसी कारण से देखना चाहिए)",
     "(पहले लिखे गए पाठ को इस तरीके से देखना चाहिए)")
rule("R8-bhajana-me", r"bhājanakāraṇe", "के विभाजन के कारण", "के विभाजन में")
rule("R8-sahajata-sadisa", r"sahajātaṃ sahajātasadisaṃ", "सह-उत्पत्ति सह-उत्पत्ति के समान है",
     "सह-उत्पत्ति सह-उत्पत्ति-कारण के समान है")
rule("R8-amasana", r"Āmasanaṃ nānaṃ", "केवल उल्लेख भिन्न है।", "उल्लेख भिन्न है।")

# =============================================================== r9
rule("R9-yatha-drop", r"\(Yathā ", r"\(जैसे ([^,()]*? में), ", r"(\1 ", "rx", ids={"7-40-43", "7-44-42"})
rule("R9-yatha-drop", r"Yathā ", r"(\(संक्षिप्त। )जैसे ", r"\1", "rx", ids={"7-44-66", "7-47-76"})
rule("R9-114-kevala", r"tadārammaṇāyeva labbhanti", "(केवल उसी विषय को लेकर होने वाले ही लागू होते हैं)",
     "(उसी विषय को लेकर होने वाले ही लागू होते हैं)")

# =============================================================== r10
rule("R10-57-1-ya", r"akusalā abyākatā tayo khandhā", "हानिकर और नैतिक रूप से अनिर्धारित तीन समूह",
     "हानिकर या नैतिक रूप से अनिर्धारित तीन समूह")
rule("R10-nanocitta-quote", r"[Nn]anocittapadaṃ", "मन रूपी न होने वाली न होने वाली पद",
     "“मन रूपी न होने वाली न होने वाली” पद")
rule("R10-sadisa-plural", r"vārampi paṭiccavārasadisaṃ,? evaṃ", "के समान है, इसी तरह", "के समान हैं, इसी तरह",
     ids={"7-55-78", "7-58-2", "7-58-6"})
rule("R10-double-space", r".", "…  (", "… (")

# =============================================================== U2 vicikicchā / uddhacca pair: «या»
rule("U2-ya", r"vicikicchāsahagat\w* uddhaccasahagat", r"(संशय के साथ होने वा(?:ला|ले|ली)),? (?:और )?(बेचैनी के साथ होने वा)",
     r"\1 या \2", "rx")
rule("U2-ya", r"vicikicchānīvaraṇañca uddhaccanīvaraṇañca", "संशय की बाधा, बेचैनी की बाधा और",
     "संशय की बाधा या बेचैनी की बाधा और")
rule("U2-ya", r"vicikicchañca uddhaccañca paṭicca", "संशय और बेचैनी पर", "संशय या बेचैनी पर")

# =============================================================== U3 sahajāto = «के साथ उत्पन्न होकर»
rule("U3-sahajato", r"sahajāt", "साथ जन्म लेकर", "साथ उत्पन्न होकर")
rule("U3-sahajato", r"sahajātatt", "साथ जन्म लेना", "साथ उत्पन्न होना")
rule("U3-sahajato", r"sahajātatt", "साथ जन्म लेने", "साथ उत्पन्न होने")


# =============================================================== nibbāna object list (r5 CHECK, sample 1-01:1250/1261)
NMEM = ["सीखने के चरण के फल", "मन को विषय की ओर मोड़ने", "गोत्र-परिवर्तन", "शुद्धि", "मार्ग", "फल"]
NMEM_RX = "|".join(re.escape(x) for x in NMEM)
NSTART = re.compile(r"निर्वाण (?=(?:" + NMEM_RX + r")(?: के लिए)?(?:, | और ))")


def nibbana_fn(h, p, ctx):
    out, n, pos = h, 0, 0
    while True:
        m = NSTART.search(out, pos)
        if not m:
            break
        i, mem, end = m.end(), [], None
        while True:
            mm = re.match(r"(" + NMEM_RX + r")", out[i:])
            if not mm:
                break
            mem.append(mm.group(1))
            i += mm.end()
            sep = re.match(r"(?: के लिए)?(?:, | और )(?=(?:" + NMEM_RX + r")(?: के लिए|,| और ))", out[i:])
            if sep:
                i += sep.end()
                continue
            fin = re.match(r" के लिए", out[i:])
            if fin:
                end = i + fin.end()
            break
        if end and len(mem) >= 2:
            if mem == ["फल", "मन को विषय की ओर मोड़ने"]:
                new = "फल के लिए और मन को विषय की ओर मोड़ने के लिए"       # sample 1-01:1249
            else:
                new = ", ".join(mem[:-1]) + " और " + mem[-1] + " के लिए"
            if out[m.end():end] != new:
                out = out[:m.end()] + new + out[end:]
                n += 1
                end = m.end() + len(new)
        pos = (end or m.end())
    return out, n


rule("R5-nibbana-list", r"[Nn]ibbānaṃ \w+(?:ssa|āya)", None, nibbana_fn, "fnp")

# =============================================================== r9 several condition locatives sharing one count
LOC = (r"(?:na|no)?(?:hetuyā|ārammaṇe|adhipatiyā|anantare|samanantare|sahajāte|aññamaññe|nissaye|upanissaye|purejāte|"
       r"pacchājāte|āsevane|kamme|vipāke|āhāre|indriye|jhāne|magge|sampayutte|vippayutte|atthiyā|natthiyā|vigate|avigate)")
PLOC = re.compile(r"\b" + LOC + r" " + LOC + r"\b")
CITEM = r"(?:पूर्ण |प्रबल )?[^\s,।…()\[\]]+-कारण"
CRUN = re.compile(B + r"((?:" + CITEM + r" में ){2,}|(?:" + CITEM + r" के अभाव में ){2,})(?=\S)")


def condlist_fn(h, p, ctx):
    def rep(m):
        run = m.group(1)
        neg = run.endswith("के अभाव में ")
        items = re.findall(CITEM + (r"(?= के अभाव में )" if neg else r"(?= में )"), run)
        return ", ".join(items[:-1]) + " और " + items[-1] + (" के अभाव में " if neg else " में ")
    out, n = CRUN.subn(rep, h)
    if n > len(PLOC.findall(p)):
        REPORT.append(("R9-condlist", ctx, f"hindi runs {n} > pāli pairs {len(PLOC.findall(p))}"))
    return out, n


rule("R9-cond-list", PLOC.pattern, None, condlist_fn, "fnp")

# =============================================================== SC subject comma (pañhāvāra example clauses)
SUBJ = r"अनुरूपता|गोत्र-परिवर्तन|शुद्धि|मार्ग|मूल|इरादा|अंग|आहार|क्षमताएँ|क्षमता|प्रधानता"
SC_RX = re.compile(B + r"(?<!को )(?<!सह-उत्पत्ति रूपी )(?<!विषय रूपी )(" + SUBJ + r") "
                   r"(?!(?:के|की|का|को|से|में|पर|रूपी|और|या|भी|ही|न|नहीं|तथा|द्वारा|रूप)(?![" + DEV + r"])|वाल|बना)"
                   r"(?=[^।;–…()\[\]]*? के लिए)")
rule("SC-subject-comma", r"paccay(?:ena|o)\b", SC_RX.pattern, r"\1, ", "rx", files=tuple(
    p for p in PARTS if p not in ("preamble", "1-00-paccaya")))

# =============================================================== U1 triad / dyad names
# (Pāli, kind, old stem, new stem): name = «<stem> वाला दो/तीन का वर्गीकरण» (and its oblique / plural forms)
NAMES = [
    # first dyads of the clusters: «<item> रूपी परिघटनाओं वाला»
    ("Hetudukaṃ", "दो", "मूल", "मूल रूपी परिघटनाओं"),
    ("Āsavadukaṃ", "दो", "मन के मैल", "मन के मैल रूपी परिघटनाओं"),
    ("Saññojanadukaṃ", "दो", "बंधन", "बंधन रूपी परिघटनाओं"),
    ("Ganthadukaṃ", "दो", "गाँठ", "गाँठ रूपी परिघटनाओं"),
    ("Nīvaraṇadukaṃ", "दो", "बाधा", "बाधा रूपी परिघटनाओं"),
    ("Parāmāsadukaṃ", "दो", "ग़लत धारणा", "ग़लत धारणा रूपी परिघटनाओं"),
    ("Upādānadukaṃ", "दो", "आसक्ति", "आसक्ति रूपी परिघटनाओं"),
    ("Kilesadukaṃ", "दो", "मन के क्लेश", "मन के क्लेश रूपी परिघटनाओं"),
]
for P, a, b in (("Āsava", "मन के मैल", "मन के मैलों"), ("Saññojana", "बंधन", "बंधनों"), ("Gantha", "गाँठ", "गाँठों"),
                ("Nīvaraṇa", "बाधा", "बाधाओं")):
    s = {"Āsava": "Sāsava", "Saññojana": "Saññojaniya", "Gantha": "Ganthaniya", "Nīvaraṇa": "Nīvaraṇiya"}[P]
    NAMES += [
        (s + "dukaṃ", "दो", f"{b} के विषय", f"{b} का विषय बनने वाली परिघटनाओं"),
        (P + "sampayuttadukaṃ", "दो", f"{b} से जुड़ाव", f"{b} से जुड़ी परिघटनाओं"),
        (P + s.lower() + "dukaṃ", "दो", f"{a} और {b} के विषय", f"{a} रूपी भी और {b} का विषय बनने वाली भी परिघटनाओं"),
        (P + P.lower() + "sampayuttadukaṃ", "दो", f"{a} और {b} से जुड़ाव", f"{a} रूपी भी और {b} से जुड़ी भी परिघटनाओं"),
        (P + "vippayutta" + s.lower() + "dukaṃ", "दो", f"{b} से अलगाव और {b} के विषय",
         f"{b} से अलग पर उनका विषय बनने वाली परिघटनाओं"),
    ]
NAMES += [
    ("Parāmaṭṭhadukaṃ", "दो", "ग़लत धारणा के विषय", "ग़लत धारणा का विषय बनने वाली परिघटनाओं"),
    ("Parāmāsasampayuttadukaṃ", "दो", "ग़लत धारणा से जुड़ाव", "ग़लत धारणा से जुड़ी परिघटनाओं"),
    ("Parāmāsaparāmaṭṭhadukaṃ", "दो", "ग़लत धारणा और ग़लत धारणा के विषय",
     "ग़लत धारणा रूपी भी और ग़लत धारणा का विषय बनने वाली भी परिघटनाओं"),
    ("Parāmāsavippayuttaparāmaṭṭhadukaṃ", "दो", "ग़लत धारणा से अलगाव और ग़लत धारणा के विषय",
     "ग़लत धारणा से अलग पर उसका विषय बनने वाली परिघटनाओं"),
    ("Saṃkilesikadukaṃ", "दो", "क्लेशों का विषय बनने", "क्लेशों का विषय बनने वाली परिघटनाओं"),
    ("Kilesasampayuttadukaṃ", "दो", "क्लेशों से जुड़ाव", "क्लेशों से जुड़ी परिघटनाओं"),
    ("Kilesasaṃkilesikadukaṃ (= 4-12 Saṃkilesasaṃkilesikadukaṃ)", "दो", "मन के क्लेश और क्लेशों का विषय बनने",
     "मन के क्लेश रूपी भी और क्लेशों का विषय बनने वाली भी परिघटनाओं"),
    ("Kilesasaṃkiliṭṭhadukaṃ", "दो", "मन के क्लेश और क्लेशों से मलिन परिघटनाओं",
     "मन के क्लेश रूपी भी और क्लेशों से मलिन भी परिघटनाओं"),
    ("Kilesakilesasampayuttadukaṃ", "दो", "मन के क्लेश और क्लेशों से जुड़ाव",
     "मन के क्लेश रूपी भी और क्लेशों से जुड़ी भी परिघटनाओं"),
    ("Kilesavippayuttasaṃkilesikadukaṃ", "दो", "क्लेशों से अलगाव और क्लेशों का विषय बनने",
     "क्लेशों से अलग पर क्लेशों का विषय बनने वाली परिघटनाओं"),
    # piṭṭhiduka (4-01)
    ("Dassanenapahātabbadukaṃ", "दो", "सत्य-दर्शन से छोड़े जाने", "सत्य-दर्शन से छोड़ी जाने वाली परिघटनाओं"),
    ("Bhāvanāyapahātabbadukaṃ", "दो", "मानसिक अभ्यास से छोड़े जाने", "मानसिक अभ्यास से छोड़ी जाने वाली परिघटनाओं"),
    ("Dassanenapahātabbahetukadukaṃ", "दो", "सत्य-दर्शन से छोड़े जाने वाले मूलों",
     "सत्य-दर्शन से छोड़े जाने वाले मूलों वाली परिघटनाओं"),
    ("Bhāvanāyapahātabbahetukadukaṃ", "दो", "मानसिक अभ्यास से छोड़े जाने वाले मूलों",
     "मानसिक अभ्यास से छोड़े जाने वाले मूलों वाली परिघटनाओं"),
    ("Savitakkadukaṃ", "दो", "आरंभिक विचार", "आरंभिक विचार वाली परिघटनाओं"),
    ("Savicāradukaṃ", "दो", "सतत विचार", "सतत विचार वाली परिघटनाओं"),
    ("Sappītikadukaṃ", "दो", "उल्लास", "उल्लास वाली परिघटनाओं"),
    ("Pītisahagatadukaṃ", "दो", "उल्लास के साथ होने", "उल्लास के साथ होने वाली परिघटनाओं"),
    ("Sukhasahagatadukaṃ", "दो", "सुख के साथ होने", "सुख के साथ होने वाली परिघटनाओं"),
    ("Upekkhāsahagatadukaṃ", "दो", "समभाव के साथ होने", "समभाव के साथ होने वाली परिघटनाओं"),
    ("Kāmāvacaradukaṃ", "दो", "इंद्रिय-सुखों के लोक", "इंद्रिय-सुखों के लोक से संबंधित परिघटनाओं"),
    ("Rūpāvacaradukaṃ", "दो", "सूक्ष्म भौतिक लोक", "सूक्ष्म भौतिक लोक से संबंधित परिघटनाओं"),
    ("Arūpāvacaradukaṃ", "दो", "अभौतिक लोक", "अभौतिक लोक से संबंधित परिघटनाओं"),
    ("Pariyāpannadukaṃ", "दो", "अस्तित्व के लोकों में समाए होने", "अस्तित्व के लोकों में समाई हुई परिघटनाओं"),
    ("Niyyānikadukaṃ", "दो", "मुक्ति की ओर ले जाने", "मुक्ति की ओर ले जाने वाली परिघटनाओं"),
    ("Niyatadukaṃ", "दो", "निश्चित", "निश्चित परिघटनाओं"),
    ("Sauttaradukaṃ", "दो", "सर्वोच्च न होने", "सर्वोच्च न होने वाली परिघटनाओं"),
    ("Saraṇadukaṃ", "दो", "संघर्ष", "संघर्ष वाली परिघटनाओं"),
    # triads built from a participle
    ("Dassanenapahātabbahetukattikaṃ", "तीन", "सत्य-दर्शन से छोड़े जाने वाले मूलों",
     "सत्य-दर्शन से छोड़े जाने वाले मूलों वाली परिघटनाओं"),
    ("Ācayagāmittikaṃ", "तीन", "संचय की ओर ले जाने", "संचय की ओर ले जाने वाली परिघटनाओं"),
    ("Maggārammaṇattikaṃ", "तीन", "मार्ग को विषय बनाने", "मार्ग को विषय बनाने वाली परिघटनाओं"),
    ("Sanidassanasappaṭighattikaṃ (= Sanidassanattikaṃ)", "तीन", "दिखाई देने वाला और टकराव",
     "दिखाई देने वाली और टकराव वाली परिघटनाओं"),
]
# names that stay (protected from partial matches by the shorter stems above)
KEEP = [("तीन", s) for s in ("हितकर", "अनुभूति", "कर्म-फल", "आरंभिक विचार", "उल्लास", "सीखने के चरण", "सीमित", "सीमित विषय",
                              "हीन", "उत्पन्न", "अतीत", "अतीत के विषय", "स्वयं से संबंधित विषय")]
TAIL = r"(?= वा(?:ला|ले) (?:{k} (?:का|के) वर्गीकरण|{k}-{k} के वर्गीकरण|दोनों {k} के वर्गीकरण))"
U1_ITEMS = sorted([(old, k, new, pal) for pal, k, old, new in NAMES] + [(s, k, s, None) for k, s in KEEP],
                  key=lambda x: -len(x[0]))
U1_RX = [(re.compile(B + re.escape(old) + TAIL.format(k=k)), new, old, k) for old, k, new, pal in U1_ITEMS]
U1_HITS = collections.Counter()


def names_fn(h, p, ctx):
    if "वर्गीकरण" not in h:
        return h, 0
    out, slots = h, []
    for rx, new, old, k in U1_RX:
        def rep(m, new=new, old=old, k=k):
            slots.append((new, old != new, (old, k)))
            return f"\x00{len(slots) - 1}\x00"
        out = rx.sub(rep, out)
    n = 0
    for i, (new, changed, key) in enumerate(slots):
        out = out.replace(f"\x00{i}\x00", new)
        if changed:
            n += 1
            U1_HITS[key] += 1
    return out, n


# Pāli condition: any line (cross-references such as «kusalasavitakkasadisaṃ» carry no «duka»); the Hindi match is
# the full name tail «… वाला/वाले दो/तीन का/के वर्गीकरण»
rule("U1-names", r".", None, names_fn, "fnp")


# =============================================================== CH abbreviated chains (file pass)
VERB = r"(होती हैं|होते हैं|होता है|होती है)"
HEAD = re.compile(r"परिघटना(?:एँ)?, [^।–]*? के लिए [^।–]*?के रूप में कारण (होती हैं|होती है)")
LINK = re.compile(r"^(\s*(?:\([^()]*\)\s*)?(?:पूर्ण |प्रबल )?[^\s…()]+-कारण के रूप में कारण )" + VERB)
PLINK = re.compile(r"(?:^|…(?:pe…)?)\s*(?:\([^()]*\)\s*)?\w+paccayena paccayo")


def chain_pass(part, el, idx, pl, log, logrows, blocked):
    head = None
    for k, li in enumerate(idx):
        h = el[li]
        if h.startswith("#"):
            head = None
            continue
        units = h.split("…")
        changed = False
        has_plink = bool(PLINK.search(pl[k]))
        for j, u in enumerate(units):
            m = LINK.match(u)
            if m and head and has_plink and m.group(2) != head:
                prev = units[j - 1] if j else ""
                tail = re.split(r"– |। |; ", prev)[-1].strip()
                cont = j > 0 and not re.search(r"कारण हो(?:ता|ती|ते)", tail) and re.search(r"(?:के लिए|के|की|का)$", tail)
                if cont:
                    REPORT.append(("CH-keep", f"{part}:{k + 1}", f"continues example: …{tail[-40:]}"))
                else:
                    units[j] = m.group(1) + head + u[m.end():]
                    changed = True
            for hm in HEAD.finditer(units[j]):
                head = hm.group(1)
        if changed:
            new = "…".join(units)
            if protected(part, k) :
                blocked.append((part, k + 1, "CH-chain-agreement"))
                continue
            logrows.append((part, k + 1, "CH-chain-agreement") + span(h, new))
            log[("CH-chain-agreement", part)][0] += sum(1 for a, b in zip(h.split("…"), units) if a != b)
            log[("CH-chain-agreement", part)][1] += 1
            el[li] = new


# =============================================================== runner
def protected(part, k):
    if part not in PROTECTED:
        return False
    rng = PROTECTED[part]
    return rng is None or any(a <= k + 1 <= b for a, b in rng)


def span(a, b, ctx=12):
    i = 0
    while i < min(len(a), len(b)) and a[i] == b[i]:
        i += 1
    j = 0
    while j < min(len(a), len(b)) - i and a[-1 - j] == b[-1 - j]:
        j += 1
    s = max(0, i - ctx)
    return a[s:len(a) - j + ctx].replace("\t", " "), b[s:len(b) - j + ctx].replace("\t", " ")


def seg_ids(pl):
    out, cur = [None] * len(pl), None
    for k in range(len(pl) - 1, -1, -1):
        m = re.search(r"\^([\w-]+)\s*$", pl[k])
        if m:
            cur = m.group(1)
        out[k] = cur
    return out


def dashes(t):
    return t.count("—") + t.count("–")


def main(dry=False):
    if not os.path.isdir(BAK):
        os.makedirs(BAK)
        for part in PARTS:
            shutil.copy2(os.path.join(HDIR, part + ".md"), os.path.join(BAK, part + ".md"))
        print("backup made:", BAK)
    comp = []
    for rid, p, old, new, kind, files, ids, lines in R:
        comp.append((rid, re.compile(p), re.compile(old) if kind == "rx" else old, new, kind, files, ids, lines))
    log = collections.defaultdict(lambda: [0, 0])
    logrows, blocked, hit = [], [], set()
    changed_lines = collections.Counter()
    for part in PARTS:
        pl = [l for l in open(os.path.join(PDIR, part + ".md"), encoding="utf-8-sig").read().splitlines() if l.strip()]
        raw = open(os.path.join(BAK, part + ".md"), encoding="utf-8").read()
        bom = raw.startswith("﻿")
        text = raw.lstrip("﻿")
        assert "\r" not in text, part
        el = text.split("\n")
        idx = [i for i, l in enumerate(el) if l.strip()]
        assert len(idx) == len(pl), (part, len(idx), len(pl))
        sid = seg_ids(pl)
        orig = list(el)
        for k, li in enumerate(idx):
            p, e = pl[k], el[li]
            for ri, (rid, pr, old, new, kind, files, ids, lines) in enumerate(comp):
                if files and not part.startswith(files):
                    continue
                if ids and sid[k] not in ids:
                    continue
                if lines and (k + 1) not in lines:
                    continue
                if not pr.search(p):
                    continue
                if kind == "fnp":
                    e2, n = new(e, p, f"{part}:{k + 1}")
                elif kind == "rx":
                    e2, n = old.subn(new, e)
                else:
                    n = e.count(old)
                    e2 = e.replace(old, new)
                if e2 == e:
                    continue
                if protected(part, k) and not rid.startswith(OPEN_RULES):
                    blocked.append((part, k + 1, rid))
                    continue
                hit.add(ri)
                logrows.append((part, k + 1, rid) + span(e, e2))
                log[(rid, part)][0] += n
                log[(rid, part)][1] += 1
                e = e2
            el[li] = e
        chain_pass(part, el, idx, pl, log, logrows, blocked)
        for k, li in enumerate(idx):
            e, e0 = el[li], orig[li]
            if e != e0:
                assert dashes(e) == dashes(e0), (part, k + 1, "dash count changed", e0, e)
                assert re.findall(r"\^[\w-]+\s*$", e) == re.findall(r"\^[\w-]+\s*$", e0), (part, k + 1, "block id")
                assert re.match(r"#*", e).group(0) == re.match(r"#*", e0).group(0), (part, k + 1, "heading")
                assert e.count("[") == e0.count("["), (part, k + 1, "brackets")
                assert "\x00" not in e, (part, k + 1, "placeholder left")
                changed_lines[part] += 1
        assert len(el) == len(orig)
        if not dry:
            out = ("﻿" if bom else "") + "\n".join(el)
            open(os.path.join(HDIR, part + ".md"), "w", encoding="utf-8", newline="\n").write(out)
    if not dry:
        with open(os.path.join(HERE, "fixes-log.tsv"), "w", encoding="utf-8") as f:
            f.write("file\tline\trule\told\tnew\n")
            for row in logrows:
                f.write("\t".join(str(x) for x in row) + "\n")
        with open(os.path.join(HERE, "names-change.tsv"), "w", encoding="utf-8") as f:
            f.write("Pāli\told Hindi\tnew Hindi\toccurrences\n")
            for pal, k, old, new in NAMES:
                f.write(f"{pal}\t{old} वाला {k} का वर्गीकरण\t{new} वाला {k} का वर्गीकरण\t{U1_HITS[(old, k)]}\n")
    tot = collections.defaultdict(lambda: [0, 0, set()])
    for (rid, part), (n, l) in log.items():
        tot[rid][0] += n
        tot[rid][1] += l
        tot[rid][2].add(part[:4])
    for rid in sorted(tot):
        print(f"{rid:24s} repl={tot[rid][0]:5d} lines={tot[rid][1]:5d} files={len(tot[rid][2])}")
    print("lines changed:", sum(changed_lines.values()), "in", len(changed_lines), "files")
    if blocked:
        print("BLOCKED (protected lines):", blocked)
    for ri, r in enumerate(R):
        if ri not in hit:
            print("NO HIT:", r[0], "|", str(r[2])[:90])
    for pal, k, old, new in NAMES:
        if not U1_HITS[(old, k)]:
            print("U1 NO HIT:", pal, old)
    rep = collections.Counter(x[0] for x in REPORT)
    print("REPORT counts:", dict(rep))
    for x in REPORT:
        if x[0] != "CH-keep":
            print("REPORT:", x)
    for x in REPORT:
        if x[0] == "CH-keep":
            print("CH-keep:", x[1], x[2])


if __name__ == "__main__":
    main(dry="--dry" in sys.argv)
