"""Apply the independent review's fixes (findings-r1 … r6) to the pi-2 rails Hindi plain translation.

usage: python -I -X utf8 apply_review_fixes.py [--dry]
- Backup: review/backup-pre-fixes/ (created once from the current files; every run starts from it, so the
  script can be rerun).
- Each rule: fixed Hindi regex -> replacement, limited to files and to lines whose aligned Pāli line matches a
  pattern, with an expected replacement count. Nothing is written unless every rule hits its count.
- The first 77 non-empty lines of 1-khandhavibhango.md (the user-approved sample) and preamble.md are touched
  only by rules marked SAMPLE_OK (the upādinna formula, approved by the user).
- Log: review/fixes-log.tsv (rule, file, ID, replacements, finding ref); preview: review/fixes-preview.txt.
"""
import collections, pathlib, re, shutil, sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PDIR = ROOT / r"AI_translation\pali\pi-2_split_chapters"
HDIR = ROOT / r"AI_translation\hindi\pi-2-hindi-plain-rails_split_chapters"
HERE = pathlib.Path(__file__).parent
BAK = HERE / "backup-pre-fixes"
DRY = "--dry" in sys.argv
SAMPLE_FILE, SAMPLE_N = "1-khandhavibhango.md", 77
IDRX = re.compile(r"\^([0-9A-Za-z-]+)\s*$")

# ---- the na vattabbā frame without a dash: «OBJ न A कहा जा सकता है, न B[, न C]» -> labels in quotes ----
FRAME = re.compile(
    r"((?:को|इन्हें|उन्हें|उसे) )न (?!“[^”]*”\s*कहा)((?:(?!कहा जा सकता)[^।;])+?) कहा जा सकता है, "
    r"(न (?:(?!, (?:और|वे|ये|इन्हें|उन्हें|उसे|कभी|वह) )[^।;])+?)(?=[।;]|, (?:और|वे|ये|इन्हें|उन्हें|उसे|कभी|वह) |$)")
FRAME_Q = re.compile(  # same frame where the first label is already quoted
    r"((?:को|इन्हें|उन्हें|उसे) )न “([^”]+)” कहा जा सकता है, "
    r"(न (?:(?!, (?:और|वे|ये|इन्हें|उन्हें|उसे|कभी|वह) )[^।;])+?)(?=[।;]|, (?:और|वे|ये|इन्हें|उन्हें|उसे|कभी|वह) |$)")


def unq(s):
    s = s.strip()
    return s[1:-1] if s.startswith("“") and s.endswith("”") else s


def frame_repl(m):
    obj, a, rest = m.group(1), unq(m.group(2)), m.group(3)
    items = [unq(x) for x in re.split(r"(?:^|, )न ", rest) if x]
    return f"{obj}न “{a}” कहा जा सकता है, " + ", ".join(f"न “{x}”" for x in items)


# (finding ref, rule name, file prefixes or None, Pāli regex or None, Hindi regex, replacement, expected, sample_ok)
R = []


def rule(ref, name, files, prx, hrx, rep, want, sample_ok=False):
    R.append(dict(ref=ref, name=name, files=files, prx=re.compile(prx, re.I) if prx else None,
                  hrx=re.compile(hrx), rep=rep, want=want, sample_ok=sample_ok))


# --- user decision: upādinna in the Suttanta internal/external formula (also inside the sample) ---
rule("r1 MAJOR ^2-4…^2-28 (user approved)", "upādinna masc sg", ("1-",), r"pāṭipuggalik",
     r"हर व्यक्ति का निजी और कर्म से उत्पन्न है", "हर व्यक्ति का निजी और (अपना मानकर) ग्रहण किया हुआ है", 2, True)
rule("r1 MAJOR ^2-4…^2-28 (user approved)", "upādinna fem sg", ("1-",), r"pāṭipuggalik",
     r"हर व्यक्ति की निजी और कर्म से उत्पन्न है(?!ं)", "हर व्यक्ति की निजी और (अपना मानकर) ग्रहण की हुई है", 6, True)
rule("r1 MAJOR ^2-4…^2-28 (user approved)", "upādinna fem pl", ("1-",), r"pāṭipuggalik",
     r"हर व्यक्ति की निजी और कर्म से उत्पन्न हैं", "हर व्यक्ति की निजी और (अपना मानकर) ग्रहण की हुई हैं", 2, True)
# --- user decision: ^2-187 emendation ---
rule("r6 source slip ^2-187 (user decision)", "nine elements sappaṭigha", ("3-",), r"Nava dhātuyo anidassanaappaṭighā",
     r"नौ तत्व दिखाई न देने वाले और टकराव से रहित हैं।",
     "नौ तत्व दिखाई न देने वाले, पर टकराव वाले [पाठ में: anidassanaappaṭighā] हैं।", 1)

# --- r1 ---
rule("r1 MAJOR ^2-36/64/93/122", "pahātabbahetuka neg", ("1-",), r"na (dassanena|bhāvanāya) pahātabbahetuko",
     r"छोड़े जाने वाले मूलों से रहित है", "छोड़े जाने वाले मूलों वाला नहीं है", 8)
rule("r1 MINOR", "anuppanna predicate", None, r"anuppann",
     r"उत्पन्न न (हुआ|हुई|हुए) (है|होता|होती|होते)", r"उत्पन्न नहीं \1 \2", 36)
rule("r1 MINOR", "kilesa vippayutta saṃkilesika", None, r"saṃkilesik",
     r"क्लेशों से अलग, पर क्लेशों का विषय", "क्लेशों से अलग, पर उनका विषय", 23)
rule("r1 MINOR (parallel)", "kilesa vippayutta asaṃkilesika", None, r"saṃkilesik",
     r"क्लेशों से अलग और क्लेशों का विषय न", "क्लेशों से अलग और उनका विषय न", 20)

# --- r2 ---
rule("r2 MINOR ^2-249 ff.", "akusalamūla list item", None, r"(lobho|doso|moho)\s*a?kusa(la)?mūl",
     r"(मोह|लोभ|द्वेष|लोभ का अभाव|द्वेष का अभाव|मोह का अभाव) रूपी (हितकर|हानिकर) मूल", r"\1, \2 मूल", 38)
rule("r2 MINOR ^2-349", "suññataṃ", None, r"suññat",
     r"उच्च ज्ञान वाला और शून्य होता है", "उच्च ज्ञान वाला और शून्यता वाला होता है", 15)
rule("r2 MINOR ^2-322/^2-348", "vipāka word order", ("6-",), r"nevasaññānāsaññāyatanasaññāsahagataṃ",
     r"कर्म-फल रूपी और न पहचान, न अ-पहचान के क्षेत्र की पहचान के साथ होने वाले चौथे ध्यान",
     "न पहचान, न अ-पहचान के क्षेत्र की पहचान के साथ होने वाले, कर्म-फल रूपी चौथे ध्यान", 2)
rule("r2 MINOR ^2-393 ff.", "upeto लैस", None, r"upet", r"सुसज्जित", "लैस", 44)

# --- r3 ---
rule("r3 CRITICAL ^2-717", "added पाँचों", ("14-",), r"Āsavavippayuttā|āsavavippayuttā",
     r"”। पाँचों मन के मैलों से अलग", "”। मन के मैलों से अलग", 1)
rule("r3 MAJOR ^2-844", "iriyāpatha चाल-ढाल", ("17-",), r"iriyāpathaṃ paṭicca", r"मुद्रा के कारण", "चाल-ढाल के कारण", 1)
rule("r3 MINOR ^2-974/976", "triple negation quoted", ("17-",), r"nevasaññīnāsaññī",
     r"मैं न पहचान वाला, न पहचान से रहित (नहीं|न) ", r"मैं ‘न पहचान वाला, न पहचान से रहित’ \1 ", 8)
rule("r3 MAJOR ^2-974/^2-975", "nāhaṃ … siyaṃ modal", ("17-",), r"nāhaṃ tathā",
     r"नहीं हो सकता”", "न भी हो सकता हूँ”", 6)
# r3 MAJOR ^2-913 vacīkamma: not applied; the termbase phrase entry akusalaṃ vacīkammaṃ = «हानिकर वाचिक कर्म» is kept.
rule("r3 MINOR ^2-862", "क्या हैं", ("17-",), r"lapanā", r"चिकनी-चुपड़ी बातें क्या है\?", "चिकनी-चुपड़ी बातें क्या हैं?", 1)
rule("r3 MINOR ^2-U40", "ग़लत रास्ता", ("17-",), r"agati agatigamanaṃ",
     r"इस प्रकार का जो ग़लत राह,", "इस प्रकार का जो ग़लत रास्ता,", 1)
rule("r3 MINOR ^2-951", "inner quotes", ("17-",), r"tamañño evamāha",
     r"“(आकाश अनंत है|चेतना अनंत है|कुछ भी नहीं है)” इस तरह", r"‘\1’ इस तरह", 3)
rule("r3 MINOR ^2-919", "या इस प्रकार", ("17-",), r"brahmacariyesanā",
     r"”, या इस प्रकार की जो दृष्टि", "”, इस प्रकार की जो दृष्टि", 1)

# --- citta: «मन रूपी नहीं हैं / मन रूपी है» (r3, r5 MAJOR, r6 MAJOR) ---
rule("r5/r6 MAJOR no cittā", "no cittā (sentences)", ("7-", "8-", "10-", "11-"), r"No cittā",
     r"। मन नहीं हैं। मन के सहचर", "। मन रूपी नहीं हैं। मन के सहचर", 4)
rule("r6 MAJOR ^2-224", "no cittā ch5", ("5-",), r"no cittā",
     r"इक्कीस क्षमताएँ मन नहीं हैं।", "इक्कीस क्षमताएँ मन रूपी नहीं हैं।", 1)
rule("r6 MAJOR ^2-224", "cittaṃ ch5", ("5-",), r"Manindriyaṃ cittaṃ", r"मन की क्षमता मन है।", "मन की क्षमता मन रूपी है।", 1)
rule("r6 MAJOR (uniform)", "no cittā / cittaṃ ch9", ("9-",), r"no cittā, cittiddhipādo cittaṃ",
     r"सिद्धि के तीन आधार मन नहीं हैं, मन रूपी सिद्धि का आधार मन है।",
     "सिद्धि के तीन आधार मन रूपी नहीं हैं, मन रूपी सिद्धि का आधार मन रूपी है।", 1)

# --- r4 ---
rule("r4 MINOR ^2-754/802/803", "glued postposition", ("16-",), None, r"(मृत्यु|रचनाओं)के ", r"\1 के ", 8)
rule("r4 MINOR ^2-810/813", "missing danda", ("16-",), None, r"(फल देते हैं|उठेंगे-बैठेंगे)” यहाँ", r"\1”। यहाँ", 2)
rule("r4 MINOR ^2-809/829/830", "danda outside quote", ("16-",), None,
     r"(असंभव है|उत्पन्न हुआ हूँ|उत्पन्न हुए हैं)।” (यहाँ|इस तरह)", r"\1”। \2", 3)
rule("r4 MINOR", "न पहचान, न अ-पहचान", ("16-",), None, r"न पहचान न अ-पहचान", "न पहचान, न अ-पहचान", 5)
rule("r4 MINOR ^2-1029", "मन के सभी मैलों", ("18-",), None, r"सभी मन के मैलों", "मन के सभी मैलों", 1)
rule("r4 MINOR ^2-1027", "कुछ, कुछ भी न", ("18-",), r"ākiñcaññāyatan", r"हैं, कुछ, कुछ भी न होने", "हैं, कुछ लोग कुछ भी न होने", 1)

# --- r5 ---
rule("r5 MAJOR ^2-650/660/670/680", "avero so abyāpajjo", ("13-",), r"yo avero so abyāpajjo",
     r"वही दुर्भावना न रखने वाला", "वही दुर्भावना से रहित", 4)
rule("r5 MAJOR ^2-749", "maggārammaṇa frame quoted", ("15-",), r"Niruttipaṭisambhidā na vattabbā",
     r"नहीं कहा जा सकता – न मार्ग को विषय बनाने वाला, न मार्ग को मूल बनाने वाला, न मार्ग की प्रधानता वाला;",
     "नहीं कहा जा सकता – न “मार्ग को विषय बनाने वाला”, न “मार्ग को मूल बनाने वाला”, न “मार्ग की प्रधानता वाला”;", 1)
rule("r5 MINOR muditā", "इस प्रसन्नता", ("13-",), None,
     r"यह मन इस दूसरों के सुख पर प्रसन्नता के साथ", "यह मन दूसरों के सुख पर इस प्रसन्नता के साथ", 2)
rule("r5 MINOR katattā (to pi-1/ch6 form)", "कर्म किए जाने", ("12-", "13-"), r"katattā upacitattā",
     r"कर्म के किए जाने और संचित होने के कारण", "कर्म किए जाने और संचित होने के कारण", 10)
rule("r5 MINOR ^2-510", "भिक्षु कहने", ("12-",), r"paṭiññāya", r"स्वयं को भिक्षु मानने से", "स्वयं को भिक्षु कहने से", 1)
rule("r5 MINOR ^2-526/532", "drop तो", ("12-",), None, r", तो इसीलिए वह", ", इसीलिए वह", 4)
rule("r5 MINOR ^2-750", "पाठभेद", ("15-",), None, r"पाठ-भेद नहीं है", "पाठभेद नहीं है", 2)

# --- r6 ---
rule("r6 MAJOR ^2-194/195/198", "diṭṭhibyasana", None, r"diṭṭhibyasan",
     r"(?<!सही )दृष्टि की हानि", "सही दृष्टि की हानि", 7)
rule("r6 MAJOR ^2-198", "हताशा gender", None, r"āyāso",
     r"पीड़ित व्यक्ति का जो हताशा", "पीड़ित व्यक्ति की जो हताशा", 2)
rule("r6 MAJOR ^2-220", "aññātāvīnaṃ", ("5-",), r"aññātāvīnaṃ",
     r"जो परिघटनाएँ पूर्ण ज्ञान पा चुकी हैं, देखी जा चुकी हैं,",
     "पूर्ण ज्ञान पा चुके व्यक्ति द्वारा जो परिघटनाएँ पूरी तरह जानी जा चुकी हैं, देखी जा चुकी हैं,", 1)
rule("r6 MAJOR ^2-203/204", "rūpavitakka", ("4-",), r"vitakko loke",
     r"के बारे में विचार", "के बारे में आरंभिक विचार", 12)
rule("r6 MINOR ^2-154", "dukkha predicate", ("2-",), r"aniccaṃ dukkhaṃ|anicco dukkho|aniccā dukkhā",
     r"अनित्य, दुःख, आत्मा", "अनित्य, दुःख रूपी, आत्मा", 6)
rule("r6 MINOR ^2-173–177", "top-level quotes", ("3-",), r"vuccati ‘",
     r"यह ‘([^’]+)’ कहा जाता", r"यह “\1” कहा जाता", 10)
rule("r6 MINOR ^2-224", "fragment वे", ("5-",), r"Sahetukā ceva na ca hetū\.",
     r"”। मूल वाली, पर स्वयं मूल रूपी न होने वाली हैं।", "”। वे मूल वाली, पर स्वयं मूल रूपी न होने वाली हैं।", 1)
rule("r6 MINOR ^2-224", "यह -> वह", ("5-",), r"Domanassindriyaṃ na vattabbaṃ – \"gantho",
     r"”, यह गाँठों से जुड़ी", "”, वह गाँठों से जुड़ी", 1)
rule("r6 MINOR no upādā", "no upādā pl", ("2-", "4-"), r"no upādā",
     r"व्युत्पन्न होने वाले नहीं हैं", "व्युत्पन्न नहीं हैं", 2)
rule("r6 MINOR no upādā", "no upādā sg", ("2-", "4-"), r"no upādā",
     r"व्युत्पन्न होने वाला नहीं होता", "व्युत्पन्न नहीं होता", 2)

# --- na vattabbā frames without a dash: one quoted shape (r2 ^2-465, r3 ^2-485, r4, r5) ---
rule("r2/r3/r4/r5 na vattabbā", "frame quoted (first label quoted)", None, r"vattabb", FRAME_Q, frame_repl, 2)
rule("r2/r3/r4/r5 na vattabbā", "frame quoted", None, r"vattabb", FRAME, frame_repl, 55)
rule("r3 MINOR ^2-485 (as ch7/8/11)", "frame quoted, no object", ("10-",), r"āsavasampayuttā",
     r"”। न मन के मैल रूपी भी और मन के मैलों से जुड़े भी कहा जा सकता है, न मन के मैलों से जुड़े, पर स्वयं मन के मैल रूपी न होने वाले।",
     "”। इन्हें न “मन के मैल रूपी भी और मन के मैलों से जुड़े भी” कहा जा सकता है, न “मन के मैलों से जुड़े, पर स्वयं मन के मैल रूपी न होने वाले”।", 1)
rule("r4 MINOR ^2-1039", "ch18 third label", ("18-",), r"adukkhamasukhāya",
     r", और (?:इन्हें|उसे) न दुःखद, न सुखद अनुभूति से (जुड़ा|जुड़ी|जुड़े) भी नहीं कहा जा सकता",
     r", न “न दुःखद, न सुखद अनुभूति से \1”", 11)


def nonempty(text):
    return [i for i, l in enumerate(text.split("\n")) if l.strip()]


def main():
    files = sorted(HDIR.glob("*.md"))
    assert len(files) == 19, len(files)
    if not BAK.exists():
        BAK.mkdir()
        for p in files:
            shutil.copy2(p, BAK / p.name)
        print("backup created", BAK)
    cnt, log, preview, out = collections.Counter(), [], [], {}
    for bp in sorted(BAK.glob("*.md")):
        if bp.name == "preamble.md":
            continue
        raw = bp.read_text(encoding="utf-8").split("\n")
        pali = [l for l in (PDIR / bp.name).read_text(encoding="utf-8-sig").split("\n") if l.strip()]
        idx = [i for i, l in enumerate(raw) if l.strip()]
        assert len(idx) == len(pali), bp.name
        ids, cur = [None] * len(pali), None
        for n in range(len(pali) - 1, -1, -1):
            m = IDRX.search(pali[n])
            cur = m.group(1) if m else cur
            ids[n] = cur
        for n, i in enumerate(idx):
            line = old = raw[i]
            for r in R:
                if r["files"] and not bp.name.startswith(r["files"]):
                    continue
                if bp.name == SAMPLE_FILE and n < SAMPLE_N and not r["sample_ok"]:
                    continue
                if r["prx"] and not r["prx"].search(pali[n]):
                    continue
                line, k = r["hrx"].subn(r["rep"], line)
                if k:
                    cnt[r["name"]] += k
                    log.append((r["name"], bp.name, ids[n], k, r["ref"]))
            if line != old:
                raw[i] = line
                preview.append(f"== {bp.name} L{n+1} ^{ids[n]}\n- {old}\n+ {line}")
        out[bp.name] = "\n".join(raw)
    bad = []
    for r in R:
        flag = "" if cnt[r["name"]] == r["want"] else "   <-- MISMATCH"
        print(f"{cnt[r['name']]:5} / {r['want']:<5} {r['name']}{flag}")
        if flag:
            bad.append(r["name"])
    (HERE / "fixes-preview.txt").write_text("\n".join(preview) + "\n", encoding="utf-8", newline="\n")
    print("lines changed", len(preview))
    if bad:
        sys.exit(f"unexpected counts, nothing written: {bad}")
    (HERE / "fixes-log.tsv").write_text(
        "rule\tfile\tID\treplacements\tfinding\n" + "\n".join("\t".join(map(str, x)) for x in log) + "\n",
        encoding="utf-8", newline="\n")
    if DRY:
        print("(dry run; nothing written to the chapter files)")
        return
    for name, text in out.items():
        (HDIR / name).write_text(text, encoding="utf-8", newline="\n")
    print("written", len(out), "chapter files")


main()
