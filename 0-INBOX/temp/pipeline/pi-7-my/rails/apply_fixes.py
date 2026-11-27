"""pi-7 Burmese rails: the bilingual-review fixes (review/report-A.md A1 … A9, report-B.md B1 … B19, report-C.md C1 …
C6; decisions in review/fix-brief.md, results in review/fix-notes.md). Model: pi-6-my/rails/apply_fixes.py (read only).

The pañhāvāra example clauses, the notes and the headings of this book are assembled by the lead / clause code of
18 generators (make_ch1-01 … make_ch5-13-20, my7_formulas' engine and each generator's own clause code), so the one
place that reaches every repetition of a frame with one rule is the built text, keyed on the Pāli (as pi-6 F02 …
F10). Every rule fires only on lines whose aligned Pāli matches its trigger; identical Pāli gets the identical change
(align_check stays at 0 differing).

Rule families:
  - CASE (case_fixes.py, frozen from case_propose.py, reviewed): K1 … K5, the conditioning subject of the example
    clauses (B1 … B9, A1, C1 and every other instance the case check finds book-wide);
  - M01 … : hand rules for the units the proposer cannot rewrite (co-subjects merged into the recipients, C1, …);
  - B11: «A ca B ca N» with two exclusive qualifiers = «A Nလည်းကောင်း၊ B Nလည်းကောင်း» (never the stack «A၊ B N»);
  - single rules for the other review items (A2 … A9, B10, B13 … B19, C2, C3, C4, C6).
After the rules the case check (case_check.py) runs on the result: it must report 0 left.

usage: python3 -I -X utf8 apply_fixes.py [--in DIR] [--out DIR]   (default: the rails folder, in place)
Run by regen_rails.sh right after apply_termbase.py (build_rails.py rewrites every chapter first, so a rebuild always
starts from the same input). Every replacement is logged in rails/fixes-log.tsv (ch, id, line, old, new, rule).
A rule: (rule, scope, Pāli trigger, changes, expected, hit)
  - scope: None = every segment, or a list of segment IDs;
  - trigger: regex the aligned Pāli line (variant brackets removed) must match;
  - changes: [(old, new)] exact strings, or [("re", pattern, replacement)] (a function replacement is allowed);
  - expected: replacements over the whole book (the run fails and writes nothing on a mismatch);
  - hit: "eq" each line gets exactly as many replacements as the Pāli trigger hits, "le" at most as many, None free.
Deterministic: files and rules in fixed order.
"""
import pathlib
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(HERE))
import case_check as cc  # noqa: E402
from case_fixes import CASE  # noqa: E402

PALI = ROOT / "AI_translation/pali/pi-7_split_chapters"
RAILS = ROOT / "AI_translation/burmese/pi-7-burmese-plain-rails_split_chapters"
LOG = HERE / "fixes-log.tsv"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
N = lambda s: unicodedata.normalize("NFC", s)  # noqa: E731
C = "၊"

# ===================================================================================================== B11
# exclusive qualifier pairs (Burmese of «A ca B ca dhammā» titles: «A သဘောတရားနှင့် B သဘောတရား»)
B11_PAIRS = [
    ("အတွင်းပိုင်း", "ပြင်ပ"),
    ("ကံကြောင့် ဖြစ်၍ စွဲလမ်းမှု၏ အာရုံလည်း ဖြစ်နိုင်သော", "ကံကြောင့် မဖြစ်သော်လည်း စွဲလမ်းမှု၏ အာရုံ ဖြစ်နိုင်သော"),
    ("ထိခိုက်မှု ရှိသော", "ထိခိုက်မှု မရှိသော"),
    ("မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိသော", "မမြင်နိုင်သော်လည်း ထိခိုက်မှု ရှိသော"),
    ("မြင်နိုင်သော", "မမြင်နိုင်သော"),
    ("မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော", "မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သည် မဟုတ်သော"),
    ("ကံကြောင့် ဖြစ်သော", "ကံကြောင့် မဖြစ်သော"),
    ("စိတ်နှင့်အတူ တည်ရှိသော", "စိတ်နှင့်အတူ တည်ရှိသည် မဟုတ်သော"),
    ("စိတ်မှ ဖြစ်ပေါ်လာသော", "စိတ်မှ ဖြစ်ပေါ်လာသည် မဟုတ်သော"),
    ("အထုံး ဖြစ်သော", "အထုံး မဟုတ်သော"),
    ("စွဲလမ်းမှု ဖြစ်သော", "စွဲလမ်းမှု မဟုတ်သော"),
    ("စိတ်အစွန်းအထင်း ဖြစ်သော", "စိတ်အစွန်းအထင်း မဟုတ်သော"),
]
B11_CASE = r"(တို့သည်|သည်|တို့အားလည်းကောင်း|အားလည်းကောင်း|တို့အား|အား|လည်းကောင်း|များ|တို့ကို)?"
_B11_HEAD = (r"(?P<this>ဤ )?(?P<a>" + "|".join(re.escape(a) for a, _ in B11_PAIRS) + r")၊ (?P<b>" +
             "|".join(re.escape(b) for _, b in B11_PAIRS) + r") (?P<noun>(?:[^\s၊…။()]+ ){0,4}?[^\s၊…။()]+?)")
B11_RX = re.compile(_B11_HEAD + B11_CASE.replace(")?", ")") + r"(?P<end>(?=[ ၊…။()])|$)")
B11_RX_BARE = re.compile(_B11_HEAD + r"()(?P<end>(?=[၊…။()])|(?= \()|$)")
B11_SUBJ = {"တို့သည်": "လည်းကောင်း", "သည်": "လည်းကောင်း", "လည်းကောင်း": "လည်းကောင်း"}
B11_DAT = {"တို့အားလည်းကောင်း": "တို့အားလည်းကောင်း", "အားလည်းကောင်း": "အားလည်းကောင်း",
           "တို့အား": "တို့အားလည်းကောင်း", "အား": "အားလည်းကောင်း"}
B11_PAL = re.compile(r"\b(\w+?)( ca|ñca) (\w+?)( ca|ñca) (\w+)")
B11_ASYN = re.compile(r"(?i)\bajjhattik\w* bāhir\w*|\bajjhattikabāhir\w*")   # 3-02 «(ime ajjhattikabāhirā …)»


def b11_sub(m):
    a, b, noun, case = m.group("a"), m.group("b"), m.group("noun"), m.group(5) or ""
    if (a, b) not in B11_PAIRS:
        return m.group(0)
    this = m.group("this") or ""
    if case in B11_SUBJ:
        tail = B11_SUBJ[case]
        return f"{this}{a} {noun}{tail}{C} {this}{b} {noun}{tail}"
    if case in B11_DAT:
        tail = B11_DAT[case]
        before = m.string[max(0, m.start() - 80):m.start()]
        if case.endswith("အား") and "အား၊ " in before and "အားလည်းကောင်း" not in before:
            tail = case + ""                            # inside a «…အား၊ …အား» list: keep its form
            return f"{this}{a} {noun}{tail}{C} {this}{b} {noun}{tail}"
        return f"{this}{a} {noun}{tail}{C} {this}{b} {noun}{tail}"
    # a member of a «၊» list / a bare noun / «…များ» / «…တို့ကို»: the noun with each qualifier, the case once
    return f"{this}{a} {noun}{case}{C} {this}{b} {noun}{case}"


def b11_trigger_count(p):
    def w(x, c):
        return x + "ṃ" if c == "ñca" else x
    return sum(1 for m in B11_PAL.finditer(p) if cc.exclusive(w(m.group(1), m.group(2)), w(m.group(3), m.group(4)))) \
        + len(B11_ASYN.findall(p))


# ===================================================================================================== B12
# two «…သော» qualifiers stacked on one noun take «၊» between them («အမြစ် မရှိသော၊ အကြောင်း ရှိသော အစုအဝေး»), where the
# Pāli has two qualifier words of the same noun. The qualifier phrases are the book's own renderings: the Burmese of
# every single-term title «X dhammo Y dhammassa …» = «Q သဘောတရားသည် …», and the descriptive qualifiers of the clauses
# (my7_formulas QUAL / the clause frames).
B12_EXTRA = ["ယုံမှားမှုနှင့်အတူ ဖြစ်သော", "ယောက်ယက်ခတ်မှုနှင့်အတူ ဖြစ်သော", "စိတ်ဆင်းရဲမှုနှင့်အတူ ဖြစ်သော",
             "နာကျင်မှုနှင့်အတူ ဖြစ်သော", "သာယာမှုနှင့်အတူ ဖြစ်သော", "ဥပေက္ခာနှင့်အတူ ဖြစ်သော", "ပီတိနှင့်အတူ ဖြစ်သော",
             "ကံ၏ အကျိုး ဖြစ်သော", "အမြစ် မရှိသော", "အမြစ် ရှိသော", "ရုပ် မဟုတ်သော", "ရုပ် ဖြစ်သော", "စိတ်မှ ဖြစ်ပေါ်လာသော",
             "နောက်မှ ဖြစ်ပေါ်သော", "ရှေးဦးစွာ ဖြစ်ပေါ်ပြီးသော", "ပြုရုံမျှသာ ဖြစ်သော", "ယှဉ်တွဲသော", "ကုသိုလ် ဖြစ်သော",
             "အယူမှားနှင့် ကင်းကွာသော", "လောဘနှင့်အတူ ဖြစ်သော"]


def b12_qualifiers(text, pali, files):
    q = set(B12_EXTRA)
    for f in files:
        for a, b in zip(pali[f], text[f]):
            m = re.match(r"(\w+) dhammo \w+ dhammassa ", a)
            if m:
                mb = re.match(r"(.+?) သဘောတရားသည် ", b)
                if mb and mb.group(1).endswith("သော") and C not in mb.group(1):
                    q.add(mb.group(1))
    ql = sorted(q, key=lambda x: (-len(x), x))
    alt = "|".join(re.escape(x) for x in ql)
    return re.compile(r"(?:(?<=[ (“၊])|^)(?:" + alt + r") (?=(?:" + alt + r") \S)"), ql


def b12_pali_pairs(a):
    """adjacent qualifier words of one noun (same case, no ca / cut between) in a Pāli line"""
    ws = re.sub(r"\{[^}]*\}", " ", a).split()
    n = 0
    for i in range(len(ws) - 2):
        w1, w2, w3 = (cc.core(x) for x in ws[i:i + 3])
        if not (w1 and w2 and w3) or any(x in ("ca", "ceva", "no", "na", "vā") for x in (w1, w2, w3)):
            continue
        if w1.endswith("ñca") or w2.endswith("ñca") or ws[i].endswith(("…", ",", ".")) or ws[i + 1].endswith(("…", ",", ".")):
            continue
        if not cc.is_head(w1) and not cc.is_head(w2) and cc.is_gen(w1) == cc.is_gen(w2):
            n += 1
    return n


# ===================================================================================================== RULES
AIDS = "(?:{})".format


def esc(s):
    return re.escape(s)


RULES = [
    # ------------------------------------------------------------------------------- meaning: the case of the subject
    ("M01 B1 «hetū ca sampayuttakā ca khandhā hetūnañca sampayuttakānañca khandhānaṃ»: two co-subjects «…လည်းကောင်း», "
     "two recipients «…အားလည်းကောင်း» (the associated khandhas were moved into the recipients and appeared twice)",
     None, r"\bhetū ca sampayuttakā ca khandhā hetūnañca sampayuttakānañca khandhānaṃ",
     [("အမြစ်တို့သည် ယှဉ်တွဲသော အစုအဝေးတို့အားလည်းကောင်း၊ အမြစ်တို့အားလည်းကောင်း၊ ယှဉ်တွဲသော အစုအဝေးတို့အားလည်းကောင်း",
       "အမြစ်လည်းကောင်း၊ ယှဉ်တွဲသော အစုအဝေးလည်းကောင်း အမြစ်တို့အားလည်းကောင်း၊ ယှဉ်တွဲသော အစုအဝေးတို့အားလည်းကောင်း")],
     1, "eq"),
    ("M02 B2 «purimā purimā nīvaraṇā ca sampayuttakā ca khandhā pacchimānaṃ pacchimānaṃ nīvaraṇānañca sampayuttakānañca "
     "khandhānaṃ»: the same pattern as B1",
     None, r"purimā purimā nīvaraṇā ca sampayuttakā ca khandhā pacchimānaṃ pacchimānaṃ nīvaraṇānañca",
     [("ရှေးရှေး အတားအဆီးတို့သည် ယှဉ်တွဲသော အစုအဝေးတို့အားလည်းကောင်း၊ နောက်နောက် အတားအဆီးတို့အားလည်းကောင်း၊ "
       "ယှဉ်တွဲသော အစုအဝေးတို့အားလည်းကောင်း",
       "ရှေးရှေး အတားအဆီးလည်းကောင်း၊ ယှဉ်တွဲသော အစုအဝေးလည်းကောင်း နောက်နောက် အတားအဆီးတို့အားလည်းကောင်း၊ "
       "ယှဉ်တွဲသော အစုအဝေးတို့အားလည်းကောင်း")], 1, "eq"),
    ("M03 B3 «sīlabbataparāmāso kāyagantho ca vatthu ca abhijjhākāyaganthassa ca sampayuttakānañca khandhānaṃ»: vatthu "
     "is a co-subject «…လည်းကောင်း၊ မှီရာ ဝတ္ထုလည်းကောင်း», not a recipient",
     None, r"sīlabbataparāmāso kāyagantho ca vatthu ca abhijjhākāyaganthassa ca",
     [("သီလ အကျင့်ဝတ်ဆိုင်ရာ မှားယွင်းသော ယူဆမှုဟူသော ကိုယ် အထုံးသည် မှီရာ ဝတ္ထုအားလည်းကောင်း၊ ",
       "သီလ အကျင့်ဝတ်ဆိုင်ရာ မှားယွင်းသော ယူဆမှုဟူသော ကိုယ် အထုံးလည်းကောင်း၊ မှီရာ ဝတ္ထုလည်းကောင်း ")], 1, "eq"),
    ("M04 B4 «nonīvaraṇo eko khandho ca kāmacchandanīvaraṇañca tiṇṇannaṃ khandhānaṃ …»: the neuter nominative "
     "kāmacchandanīvaraṇaṃ is a co-subject",
     None, r"nonīvaraṇo eko khandho ca kāmacchandanīvaraṇañca tiṇṇannaṃ khandhānaṃ",
     [("အတားအဆီး မဟုတ်သော အစုအဝေး တစ်ပါးသည် ကာမကို လိုလားမှု အတားအဆီးအားလည်းကောင်း၊ အစုအဝေး သုံးပါးတို့အားလည်းကောင်း၊",
       "အတားအဆီး မဟုတ်သော အစုအဝေး တစ်ပါးလည်းကောင်း၊ ကာမကို လိုလားမှု အတားအဆီးလည်းကောင်း အစုအဝေး သုံးပါးတို့အားလည်းကောင်း၊")],
     1, "eq"),
    ("M05 B6 «Sahajātaṃ – cittañca vatthuñca nocittānaṃ khandhānaṃ»: both conditioning items are co-subjects, the one "
     "recipient «…အား»",
     None, r"\bcittañca vatthuñca nocittānaṃ khandhānaṃ",
     [("စိတ်အားလည်းကောင်း၊ မှီရာ ဝတ္ထုအားလည်းကောင်း၊ စိတ် မဟုတ်သော အစုအဝေးတို့အားလည်းကောင်း",
       "စိတ်လည်းကောင်း၊ မှီရာ ဝတ္ထုလည်းကောင်း စိတ် မဟုတ်သော အစုအဝေးတို့အား")], 1, "eq"),
    ("M06 B9 «kāyikaṃ sukhaṃ moho ca …»: the co-subject sukha «…လည်းကောင်း၊» (was the accusative «ကို»)",
     None, r"\bkāyikaṃ sukhaṃ moho ca \w+sahagatānaṃ",
     [("ကိုယ်ပိုင်းဆိုင်ရာ သာယာမှုကို မောဟလည်းကောင်း ", "ကိုယ်ပိုင်းဆိုင်ရာ သာယာမှုလည်းကောင်း၊ မောဟလည်းကောင်း ")],
     1, "eq"),
    ("M07 C1 4-15 «uppannā / anuppannā / uppādī hetū …»: the subject hetū «… အမြစ်တို့သည်» (was a stacked "
     "qualifier with no case), «၊» between the two recipients",
     None, r"\b(?:uppannā|anuppannā|uppādī) hetū (?:sampayuttakānaṃ hetūnaṃ|cetopariyañāṇassa anāgataṃsañāṇassa)",
     [("ဖြစ်ပေါ်ပြီးသော၊ အမြစ် ဖြစ်သော ယှဉ်တွဲသော အမြစ်တို့အား", "ဖြစ်ပေါ်ပြီးသော အမြစ်တို့သည် ယှဉ်တွဲသော အမြစ်တို့အား"),
      ("မဖြစ်ပေါ်သေးသော၊ အမြစ် ဖြစ်သော စိတ်ကို ပိုင်းခြား၍ သိသော ဉာဏ်အား အနာဂတ်ကို သိသော ဉာဏ်အား",
       "မဖြစ်ပေါ်သေးသော အမြစ်တို့သည် စိတ်ကို ပိုင်းခြား၍ သိသော ဉာဏ်အား၊ အနာဂတ်ကို သိသော ဉာဏ်အား"),
      ("ဖြစ်ပေါ်လာမည့်၊ အမြစ် ဖြစ်သော စိတ်ကို ပိုင်းခြား၍ သိသော ဉာဏ်အား အနာဂတ်ကို သိသော ဉာဏ်အား",
       "ဖြစ်ပေါ်လာမည့် အမြစ်တို့သည် စိတ်ကို ပိုင်းခြား၍ သိသော ဉာဏ်အား၊ အနာဂတ်ကို သိသော ဉာဏ်အား")], 3, "eq"),
    ("M08 2-01 «nibbānaṃ gotrabhussa vitakkassa ca …»: the subject nibbāna «နိဗ္ဗာန်သည်» (was «ကို»)",
     None, r"\bnibbānaṃ gotrabhussa vitakkassa ca vodānassa",
     [("နိဗ္ဗာန်ကို အနွယ် ပြောင်းခြင်း စိတ်အားလည်းကောင်း၊", "နိဗ္ဗာန်သည် အနွယ် ပြောင်းခြင်း စိတ်အားလည်းကောင်း၊")], 1, "le"),
    ("M09 2-05 «patthanā, kāyikassa sukhassa, …»: the subject «တောင့်တခြင်းသည်» (was joined to the recipients by «၊»)",
     None, r"\bpatthanā, kāyikassa sukhassa, kāyikassa dukkhassa",
     [("တောင့်တခြင်း၊ ကိုယ်ပိုင်းဆိုင်ရာ သာယာမှုအား၊", "တောင့်တခြင်းသည် ကိုယ်ပိုင်းဆိုင်ရာ သာယာမှုအား၊")], 1, "eq"),
    ("M10 2-08 «…, kāyikaṃ sukhaṃ, kāyikaṃ dukkhaṃ, mahaggatārammaṇāya saddhāya…»: the last subject of the list "
     "«…နာကျင်မှုသည်»",
     None, r"\bkāyikaṃ dukkhaṃ, mahaggatārammaṇāya saddhāya",
     [("ကိုယ်ပိုင်းဆိုင်ရာ နာကျင်မှု၊ ကြီးမြတ်သည်ကို အာရုံပြုသော ယုံကြည်မှုအား",
       "ကိုယ်ပိုင်းဆိုင်ရာ နာကျင်မှုသည် ကြီးမြတ်သည်ကို အာရုံပြုသော ယုံကြည်မှုအား")], 1, "eq"),
    ("M11 2-16 «… aniccānupassanā, dukkhānupassanā, anattānupassanā, ajjhattārammaṇāya aniccānupassanāya, …»: the "
     "subject list closes with «…တို့သည်» before the recipients",
     None, r"\banattānupassanā, ajjhattārammaṇāya aniccānupassanāya",
     [("အတ္တ မဟုတ်ဟု အဖန်ဖန် ရှုခြင်း၊ မိမိ၌ ရှိသည်ကို အာရုံပြုသော မမြဲဟု အဖန်ဖန် ရှုခြင်းအား၊",
       "အတ္တ မဟုတ်ဟု အဖန်ဖန် ရှုခြင်းတို့သည် မိမိ၌ ရှိသည်ကို အာရုံပြုသော မမြဲဟု အဖန်ဖန် ရှုခြင်းအား၊")], 1, "eq"),
    ("M12 2-17 «Rūpāyatanañca cakkhāyatanañca cakkhuviññāṇañca …»: three co-subjects, each «…လည်းကောင်း»",
     None, r"\bRūpāyatanañca cakkhāyatanañca cakkhuviññāṇañca",
     [("အဆင်းအရောင် အာရုံခံ နယ်ပယ်၊ မျက်စိ အာရုံခံ နယ်ပယ်လည်းကောင်း၊",
       "အဆင်းအရောင် အာရုံခံ နယ်ပယ်လည်းကောင်း၊ မျက်စိ အာရုံခံ နယ်ပယ်လည်းကောင်း၊")], 1, "eq"),
    ("M13 3-09 «rūpāyatanaṃ cakkhuviññāṇassa ca sampayuttakānañca khandhānaṃ…»: the subject «…နယ်ပယ်သည်», two "
     "recipients «…အားလည်းကောင်း» (all three were co-subjects)",
     None, r"\brūpāyatanaṃ cakkhuviññāṇassa ca sampayuttakānañca khandhānaṃ",
     [("အဆင်းအရောင် အာရုံခံ နယ်ပယ်လည်းကောင်း၊ မျက်စိ သိစိတ်လည်းကောင်း၊ ယှဉ်တွဲသော အစုအဝေးလည်းကောင်းအား",
       "အဆင်းအရောင် အာရုံခံ နယ်ပယ်သည် မျက်စိ သိစိတ်အားလည်းကောင်း၊ ယှဉ်တွဲသော အစုအဝေးတို့အားလည်းကောင်း")], 1, "le"),
    ("M14 «X-ssa parikammaṃ» (the preparation of X) = «X၏ ကြိုတင် ပြင်ဆင်မှု» (as the 30 other places), not the "
     "recipient «Xအား»",
     None, r"\b\w+(?:ssa|āya|uyā) parikamm",
     [("re", r"(?<=\S)အား ကြိုတင် ပြင်ဆင်မှု", "၏ ကြိုတင် ပြင်ဆင်မှု")], 11, "le"),
    ("M15 «maggo sekkhānaṃ atthappaṭisambhidāya …»: sekkhānaṃ is the genitive of the persons «ကျင့်ကြံဆဲသူတို့၏» "
     "(= 1-03, and «ariyānaṃ» «အရိယာတို့၏» 8 times), not an extra recipient",
     None, r"(?i)\bmaggo sekkhānaṃ atthappaṭisambhidāya",
     [("မဂ်သည် ကျင့်ကြံဆဲသူတို့အား အကျိုးအနက်", "မဂ်သည် ကျင့်ကြံဆဲသူတို့၏ အကျိုးအနက်")], 2, "le"),
    ("M16 A1 1-01 ^7-2-423 «Adinnādānaṃ adinnādānassa…»: the subject «မပေးသည်ကို ယူခြင်းသည်» (was the object «ကို»; "
     "the parallel lines have «သည်»)",
     None, r"\bAdinnādānaṃ adinnādānassa",
     [("မပေးသည်ကို ယူခြင်းကို မပေးသည်ကို ယူခြင်းအား", "မပေးသည်ကို ယူခြင်းသည် မပေးသည်ကို ယူခြင်းအား")], 1, "eq"),
    ("M17 3-10 «diṭṭhupādānaṃ kāmupādānassa atthipaccayena paccayo»: the subject «အယူ စွဲလမ်းမှုသည်» (was merged into "
     "the recipient «… တို့အား»; = B5)",
     None, r"– diṭṭhupādānaṃ kāmupādānassa atthipaccayena",
     [("– အယူ စွဲလမ်းမှု၊ ကာမ စွဲလမ်းမှုတို့အား", "– အယူ စွဲလမ်းမှုသည် ကာမ စွဲလမ်းမှုအား")], 1, "eq"),
    ("M18 3-10 «noupādāno eko khandho ca diṭṭhupādānañca tiṇṇannaṃ khandhānaṃ …»: the neuter nominative diṭṭhupādānaṃ "
     "is a co-subject (= B4)",
     None, r"\bnoupādāno eko khandho ca diṭṭhupādānañca tiṇṇannaṃ khandhānaṃ",
     [("စွဲလမ်းမှု မဟုတ်သော အစုအဝေး တစ်ပါးသည် အယူ စွဲလမ်းမှုအားလည်းကောင်း၊ အစုအဝေး သုံးပါးတို့အားလည်းကောင်း၊",
       "စွဲလမ်းမှု မဟုတ်သော အစုအဝေး တစ်ပါးလည်းကောင်း၊ အယူ စွဲလမ်းမှုလည်းကောင်း အစုအဝေး သုံးပါးတို့အားလည်းကောင်း၊")],
     1, "eq"),
    ("M19 (coordinator, B8 remainder) «… senāsanaṃ cittaṃ / moho X-assa …» with no «ca»: senāsanaṃ is one of the listed "
     "subjects, «… အိပ်ရာ နေရာ၊ စိတ်သည် / မောဟသည် …» as at 3-09 line 1387 (^7-32-128, ^7-32-216 ×2, 3-04 line 488); "
     "«senāsanaṃ moho ca …» keeps «…လည်းကောင်း၊ …လည်းကောင်း»",
     None, r"senāsanaṃ (?:cittaṃ|moho) (?!ca\b|upanissāya)",
     [("အိပ်ရာ နေရာကို စိတ်သည် ", "အိပ်ရာ နေရာ၊ စိတ်သည် "),
      ("အိပ်ရာ နေရာကို မောဟသည် ", "အိပ်ရာ နေရာ၊ မောဟသည် ")], 4, "le"),
    # ------------------------------------------------------------------------------- meaning: other items
    ("A2 «paṭisandhikkhaṇe natthi» = «ပဋိသန္ဓေ နေသော ခဏ၌ မရှိ» (the locative kept, as ^7-2-339 / ^7-11-33)",
     None, r"paṭisandhikkhaṇe natthi",
     [("ပဋိသန္ဓေ နေသော ခဏ မရှိ", "ပဋိသန္ဓေ နေသော ခဏ၌ မရှိ")], 3, "le"),
    ("A5 1-04 ^7-5-34 «(Catuvīsatipaccayā vitthāretabbā, avigatapaccayā.)»: avigatapaccayā closes the list "
     "«… အကြောင်းအထိ»",
     ["7-5-34"], r"vitthāretabbā, avigatapaccayā",
     [("(အကြောင်း နှစ်ဆယ့်လေးပါးကို အကျယ် ချဲ့ရမည်၊ မပျောက်ကွယ်ခြင်းဟူသော အကြောင်းကြောင့်။)",
       "(အကြောင်း နှစ်ဆယ့်လေးပါးကို မပျောက်ကွယ်ခြင်းဟူသော အကြောင်းအထိ အကျယ် ချဲ့ရမည်။)")], 1, "eq"),
    ("B10 the source slip «Sahetuko ceva na ca hetu dhammo sahetukassa ceva na ca hetussa ca dhammassa» (a stray ca) "
     "and its pattern (ganthaniyo / upādāniyo; 5-11 «Hetu ceva sahetuko ca …»): the intended X→X reading "
     "«X သဘောတရားသည် X သဘောတရားအား» (as 3-10 line 590); spelling-only slip, logged — covered by CASE K2",
     None, r"(?!x)x", [], 0, None),
    ("B13 3-09 ^7-32-387 the stray «dhammaṃ» of «Upādā dhammañca noupādā dhammañca dhammaṃ paccayā»: not a third "
     "item, as line 2465 «… သဘောတရားနှင့် … သဘောတရားကြောင့်» (spelling-only slip)",
     None, r"\bUpādā dhammañca noupādā dhammañca dhammaṃ paccayā",
     [("မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော သဘောတရားကြောင့်လည်းကောင်း၊ မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သည် မဟုတ်သော "
       "သဘောတရားကြောင့်လည်းကောင်း၊ သဘောတရားကြောင့်လည်းကောင်း ",
       "မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော သဘောတရားနှင့် မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သည် မဟုတ်သော သဘောတရားကြောင့် ")],
     1, "eq"),
    ("B14 4-01 ^7-35-101 the source slip «novigatapaccayena» in an anuloma list: the intended positive avigata "
     "«… မပျောက်ကွယ်ခြင်းဟူသော အကြောင်းဖြင့် အကြောင်း ဖြစ်သည်။» (spelling-only slip)",
     None, r"…pe… novigatapaccayena paccayo\. \(Saṃkhittaṃ",
     [("… ပျောက်ကွယ်ခြင်းဟူသော အကြောင်းဖြင့် အကြောင်း ဖြစ်သည် မဟုတ်။",
       "… မပျောက်ကွယ်ခြင်းဟူသော အကြောင်းဖြင့် အကြောင်း ဖြစ်သည်။")], 1, "eq"),
    # ------------------------------------------------------------------------------- consistency
    ("A3 «(Cakkaṃ kātabbaṃ)» = «(စက်ဝိုင်း ပြုရမည်)» everywhere (was also «စက်ဝိုင်းကဲ့သို့ လှည့်ပတ်၍ ပြုရမည်»)",
     None, r"(?i)\(cakkaṃ kātabbaṃ",
     [("(စက်ဝိုင်းကဲ့သို့ လှည့်ပတ်၍ ပြုရမည်)", "(စက်ဝိုင်း ပြုရမည်)"),
      ("(စက်ဝိုင်းကဲ့သို့ လှည့်ပတ်၍ ကုသိုလ် သုံးမျိုးတွဲနှင့် တူအောင် ပြုရမည်)",
       "(စက်ဝိုင်း ပြုရမည်၊ ကုသိုလ် သုံးမျိုးတွဲနှင့် တူသည်)")], 4, "le"),
    ("A4 «idaṃ nānākaraṇaṃ» = «ဤသည်မှာ ကွဲပြားမှု ဖြစ်သည်» (= 1-03 ^7-4-13); also «imaṃ / idaṃ nānaṃ», the same word "
     "of the notes (L02)",
     None, r"(?i)\b(?:idaṃ|imaṃ) (?:nānākaraṇaṃ|nānaṃ)",
     [("ဤသည် ကွဲပြားမှု ဖြစ်သည်", "ဤသည်မှာ ကွဲပြားမှု ဖြစ်သည်")], 8, "le"),
    ("B15 the hetuka headings (termbase change 2026-11-26): «… pahātabbahetuka-» = «… ပယ်ရမည့် အမြစ် ရှိခြင်း "
     "နှစ်မျိုးတွဲ / သုံးမျိုးတွဲ», in every heading, colophon and note that names them",
     None, r"(?i)pahātabbahetuka(?:duk|ttik)|dassanahetu(?:ka)?ttik",
     [("re", r"ပယ်ရမည့် အမြစ် ((?:နှစ်|သုံး)မျိုးတွဲ)", r"ပယ်ရမည့် အမြစ် ရှိခြင်း \1")], None, "le"),
    ("B16 / A7 saṅghaṃ bhindati = «သံဃာကို သင်းခွဲသည်» (termbase change 2026-11-26; = «သင်းခွဲခြင်း ကံ», pi-5 «သင်းခွဲ»); "
     "the absolutive bhinditvā keeps the locked term «ဖြိုခွဲ၍» (not part of the change; reported)",
     None, r"(?i)\bsaṅghaṃ bhindati",
     [("သံဃာကို ဖြိုခွဲသည်", "သံဃာကို သင်းခွဲသည်")], None, "le"),
    ("B17 «tīṇiyeva moho» = the majority form «မောဟနှင့် သုံးခုသာ» (7 of 8): 4-01 ^7-35-184 «မောဟ သုံးခုသာ»",
     None, r"Tīṇiyeva moho, pavatte",
     [("မောဟ သုံးခုသာ၊ ဘဝ ဖြစ်စဉ်၌", "မောဟနှင့် သုံးခုသာ၊ ဘဝ ဖြစ်စဉ်၌")], 1, "eq"),
    ("C2 the chapter-end titles «Dhammānulome / Dhammapaccanīye … paṭṭhānaṃ niṭṭhitaṃ»: the order phrase stands "
     "outside the quote, as 5-xx / 2-17 «သဘောတရား အဟုတ်ပြ ပုံစံ၌ “…” ပြီးဆုံးပြီ»",
     None, r"(?i)paṭṭhānaṃ niṭṭhitaṃ",
     [("re", r"“(သဘောတရား (?:အဟုတ်ပြ|အငြင်းပြ|အဟုတ်ပြ အငြင်းပြ|အငြင်းပြ အဟုတ်ပြ) ပုံစံ၌ )", r"\1“")], 3, "le"),
    ("C3 5-20 «Anulomadukatikapaṭṭhānato paṭṭhāya … bhāṇavārehi paṭṭhānaṃ.»: no quotes (the Pāli has none and this "
     "is not a chapter-end title)",
     None, r"bhāṇavārehi paṭṭhānaṃ",
     [("“နှစ်မျိုးတွဲနှင့် သုံးမျိုးတွဲတို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ” မှ", "နှစ်မျိုးတွဲနှင့် သုံးမျိုးတွဲတို့၏ အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံမှ"),
      ("“အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ” သည်", "အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံသည်")], 2, None),
    ("C4 / A9 the variant mark «{… (?)}» = «(မသေချာ)» (the parentheses were doubled)",
     None, r"RAW:\{[^}]*\?",
     [("((မသေချာ))", "(မသေချာ)")], 5, "le"),
    ("C6 «…sampayuttavārampi paṭiccavārasadisaṃ»: «…ကိုလည်း၊ မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် …» (the «၊» against the garden "
     "path «relying also on»), every instance of the frame",
     None, r"(?i)paṭiccavārasadis",
     [("ကိုလည်း မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက်", "ကိုလည်း၊ မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက်")], None, "le"),
    # ------------------------------------------------------------------------------- minor
    ("A6 2-02 ^7-8-13 «(Namaggapaccayā nahetupaccayasadisaṃ.)»: the note gets a subject «မဂ်ဟူသော အကြောင်း "
     "မဟုတ်ခြင်းသည် …နှင့် တူသည်»",
     ["7-8-13"], r"Namaggapaccayā nahetupaccayasadisaṃ",
     [("(မဂ်ဟူသော အကြောင်းကြောင့် မဟုတ်ဘဲ အမြစ်ဟူသော အကြောင်း မဟုတ်ခြင်းနှင့် တူသည်။",
       "(မဂ်ဟူသော အကြောင်း မဟုတ်ခြင်းသည် အမြစ်ဟူသော အကြောင်း မဟုတ်ခြင်းနှင့် တူသည်။")], 1, "eq"),
    ("A8 2-04 ^7-10-86 «(dassanena sadisaṃ gamanaṃ)»: the note gets a subject «(သွားပုံသည် …နှင့် တူသည်)»",
     ["7-10-86"], r"dassanena sadisaṃ gamanaṃ",
     [("(သွားပုံ သစ္စာကို", "(သွားပုံသည် သစ္စာကို")], 1, "eq"),
    ("B18 3-05 Vārasattakaṃ = «ဖော်ပြချက် ခုနစ်မျိုး» («မျိုးတွဲ» is the dyad / triad word)",
     None, r"Vārasattakaṃ", [("ဖော်ပြချက် ခုနစ်မျိုးတွဲ", "ဖော်ပြချက် ခုနစ်မျိုး")], 1, "eq"),
    ("B19 4-01 ^7-35-176 «yadipi vimati atthi» = «အကယ်၍ သံသယ ရှိသော်လည်း» (vimati is doubt)",
     None, r"yadipi vimati atthi",
     [("အကယ်၍ စိတ်ရှုပ်ထွေးခြင်း ရှိသော်လည်း", "အကယ်၍ သံသယ ရှိသော်လည်း")], 1, "eq"),
]


def segs(lines):
    """[(id, [line indexes])] in file order."""
    out, buf = [], []
    for k, l in enumerate(lines):
        if not l.strip():
            continue
        buf.append(k)
        m = ID.search(l)
        if m:
            out.append((m.group(1), buf))
            buf = []
    return out


def marks(s):
    return tuple(s.count(c) for c in "[…–()")


def nobr(s):
    return re.sub(r"\s*\{[^}]*\}", "", s)


def do_change(text, ch):
    """-> (new text, n replacements)"""
    if ch[0] == "re":
        new, n = re.subn(ch[1], ch[2], text)
        return new, n
    old, new = ch
    n = text.count(old)
    return (text.replace(old, new), n) if n else (text, 0)


def main():
    args = sys.argv[1:]
    src = pathlib.Path(args[args.index("--in") + 1]) if "--in" in args else RAILS
    dst = pathlib.Path(args[args.index("--out") + 1]) if "--out" in args else RAILS
    files = sorted(p.name for p in PALI.glob("*.md"))
    pali = {f: N((PALI / f).read_text(encoding="utf-8-sig")).split("\n") for f in files}
    text = {f: N((src / f).read_text(encoding="utf-8")).split("\n") for f in files}
    pseg = {f: segs(pali[f]) for f in files}
    mseg = {f: dict(segs(text[f])) for f in files}
    lineid = {f: {} for f in files}
    for f in files:
        for i, idx in pseg[f]:
            for k in idx:
                lineid[f][k] = i
    log, errors, counts = [], [], {}
    all_rules = [(f"{r[0]}.{i:03d} «{r[1][:60]}»", None, r[1], [(r[2], r[3])], r[4], "le")
                 for i, r in enumerate(CASE)] + RULES
    for rule, ids, trig, chg, expect, hit in all_rules:
        raw = trig.startswith("RAW:")
        trig_re = re.compile(trig[4:] if raw else trig)
        done, found = 0, set()
        for f in files:
            for i, pidx in pseg[f]:
                if ids is not None and i not in ids:
                    continue
                found.add(i)
                midx = mseg[f].get(i)
                if midx is None or len(midx) != len(pidx):
                    errors.append(f"{rule[:12]}: {f} {i}: segment missing or not line-aligned")
                    continue
                for pk, mk in zip(pidx, midx):
                    np_ = len(trig_re.findall(pali[f][pk] if raw else nobr(pali[f][pk])))
                    if not np_:
                        continue
                    before, got = text[f][mk], 0
                    for c in chg:
                        new, n = do_change(text[f][mk], c)
                        if n:
                            text[f][mk] = new
                            got += n
                            log.append((f[:-3], i, str(mk + 1), c[-2] if c[0] == "re" else c[0],
                                        c[-1] if c[0] == "re" else c[1], rule.split(" ")[0], str(n)))
                    if hit == "eq" and got != np_:
                        errors.append(f"{rule[:12]}: {f[:-3]} {i} line {mk + 1}: {got} replacements, Pāli {np_}")
                    if hit == "le" and got > np_ and not rule.startswith(("B15", "B16", "C6", "M14")):
                        errors.append(f"{rule[:12]}: {f[:-3]} {i} line {mk + 1}: {got} replacements > Pāli {np_}")
                    if marks(before) != marks(text[f][mk]) and not rule.startswith("C4"):
                        errors.append(f"{rule[:12]}: {f[:-3]} {i} line {mk + 1}: «[ … – ( )» counts changed")
                    done += got
        if ids is not None and found != set(ids):
            errors.append(f"{rule[:12]}: segments not found: {sorted(set(ids) - found)}")
        counts[rule] = done
        if expect is not None and done != expect:
            errors.append(f"{rule[:16]}: {done} replacements, expected {expect}")
    n_case = sum(v for k, v in counts.items() if k.startswith(("K1", "K2", "K3", "K4", "K5")))
    if "--dev" in args:
        with open(HERE / "dev-case-counts.tsv", "w", encoding="utf-8") as fh:
            for k, v in counts.items():
                if k.startswith(("K1", "K2", "K3", "K4", "K5")):
                    fh.write(f"{k.split(' ')[0]}\t{v}\n")
    # ------------------------------------------------------------------ B11 (exclusive qualifiers, «A၊ B N»)
    b11 = 0
    for f in files:
        for k, line in enumerate(text[f]):
            if k >= len(pali[f]) or not b11_trigger_count(nobr(pali[f][k])):
                continue
            new, n = B11_RX.subn(b11_sub, line)
            new, n2 = B11_RX_BARE.subn(b11_sub, new)
            if (n or n2) and new != line:
                real = n + n2
                b11 += real
                log.append((f[:-3], lineid[f].get(k, ""), str(k + 1), "«A၊ B N»", "«A N…၊ B N…»", "B11", str(real)))
                text[f][k] = new
    counts["B11 «A ca B ca N» with exclusive qualifiers = «A Nလည်းကောင်း၊ B Nလည်းကောင်း» (not «A၊ B N»)"] = b11
    # ------------------------------------------------------------------ B12 (two qualifiers on one noun: «၊»)
    b11_lines = {(r[0], r[2]): int(r[6]) for r in log if r[5] == "B11"}
    rx12, ql12 = b12_qualifiers(text, pali, files)
    b12 = 0
    for f in files:
        for k, line in enumerate(text[f]):
            if k >= len(pali[f]):
                continue
            ms = list(rx12.finditer(line))
            if not ms:
                continue
            allow = b12_pali_pairs(pali[f][k]) + b11_lines.get((f[:-3], str(k + 1)), 0)
            if len(ms) > allow:
                errors.append(f"B12: {f[:-3]}:{k + 1}: {len(ms)} stacks, Pāli qualifier pairs {allow}")
                continue
            new = rx12.sub(lambda m: m.group(0)[:-1] + C + " ", line)
            b12 += len(ms)
            log.append((f[:-3], lineid[f].get(k, ""), str(k + 1), "«Q1 Q2 N»", "«Q1၊ Q2 N»", "B12", str(len(ms))))
            text[f][k] = new
    counts[f"B12 two «…သော» qualifiers on one noun = «Q1၊ Q2 N» ({len(ql12)} qualifier phrases)"] = b12
    # ------------------------------------------------------------------ book checks
    info = []
    left = []
    for f in files:
        for k, line in enumerate(text[f]):
            for a, b in B11_PAIRS:
                if f"{a}{C} {b} " in line:
                    left.append(f"{f[:-3]}:{k + 1}")
    info.append(f"B11 stacks «A၊ B N» of exclusive qualifiers left: {len(left)}")
    left12 = sum(len(rx12.findall(l)) for f in files for l in text[f])
    info.append(f"B12 qualifier stacks without «၊» left: {left12}")
    if left12:
        errors.append(f"B12: {left12} stacks left")
    if left:
        errors.append(f"B11 left on {left[:8]}")
    for label, rx in (("B16 «ဖြိုခွဲသည်»", "ဖြိုခွဲသည်"), ("B15 «ပယ်ရမည့် အမြစ် နှစ်/သုံးမျိုးတွဲ»", r"ပယ်ရမည့် အမြစ် (?:နှစ်|သုံး)မျိုးတွဲ"),
                      ("A3 «စက်ဝိုင်းကဲ့သို့ လှည့်ပတ်၍»", "စက်ဝိုင်းကဲ့သို့ လှည့်ပတ်၍"), ("C4 «((မသေချာ))»", r"\(\(မသေချာ\)\)"),
                      ("A4 «ဤသည် ကွဲပြားမှု»", "ဤသည် ကွဲပြားမှု"), ("A2 «ခဏ မရှိ»", "နေသော ခဏ မရှိ"),
                      ("M14 «အား ကြိုတင် ပြင်ဆင်မှု»", "အား ကြိုတင် ပြင်ဆင်မှု"),
                      ("C6 «ကိုလည်း မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက်»", "ကိုလည်း မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက်")):
        n = sum(len(re.findall(rx, l)) for f in files for l in text[f])
        info.append(f"{label} left: {n}")
        if n:
            errors.append(f"{label}: {n} left")
    # the case check on the result
    tmp = {f: "\n".join(text[f]) for f in files}
    n_cl, rows = cc.run_texts(tmp)
    info.append(f"case check: {n_cl} clauses, {len(rows)} left")
    if rows:
        errors.append(f"case check: {len(rows)} left: " + "; ".join(f"{r[0]}:{r[1]} {r[2]} «{r[3][:50]}»" for r in rows[:12]))
    for rule, n in counts.items():
        print(f"{n:6d}  {rule[:110]}")
    for x in info:
        print(f"        check: {x}")
    if errors:
        print("\n".join(errors[:40]))
        print(f"{len(errors)} errors")
        if "--dev" in args and dst != RAILS:       # inspection copy only (never the rails folder)
            dst.mkdir(parents=True, exist_ok=True)
            for f in files:
                (dst / f).write_text("\n".join(text[f]), encoding="utf-8")
        sys.exit(1)
    dst.mkdir(parents=True, exist_ok=True)
    for f in files:
        (dst / f).write_text("\n".join(text[f]), encoding="utf-8")
    with open(LOG, "w", encoding="utf-8") as fh:
        fh.write("ch\tid\tline\told\tnew\trule\tn\n")
        for row in log:
            fh.write("\t".join(row) + "\n")
    print(f"{len(all_rules) + 1} rules; {sum(int(r[6]) for r in log)} replacements; "
          f"{len({(r[0], r[2]) for r in log})} lines changed")


main()
