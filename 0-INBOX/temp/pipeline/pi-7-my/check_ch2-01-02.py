"""Per-line check of the Burmese pi-7 chapters 2-01 vitakkattika, 2-02 pītittika against the Pāli (adapted from
check_ch1-03-05.py / check_sample.py; independent of the generator's frames).

usage: python3 -I -X utf8 check_ch2-01-02.py [chapter ...] [--out DIR] [--mutate] [--sample] [--pe]
Checks, line by line (Pāli line i <-> Burmese line i):
  S  structure: equal non-empty lines, heading #-level, block IDs, no «?» «।» «:-», no Latin left outside variants;
  P  polarity: «မဟုတ်» count and the «မ…» negatives expected from the Pāli tokens (TABLES NEG_*);
  C  conditions: the sequence of conditions (stem + polarity) named in the Pāli = the sequence of
     «Nဟူသော အကြောင်း» / bare names (ghaṭanā lists, «(Xsadisaṃ)») in the Burmese; whole notes and headings
     whose conditions the regexes cannot see are compared through this checker's own table NOTE_PAIRS / HEAD_CONDS;
  O  term order: the sequence of triad terms in the Pāli = the sequence in the Burmese (conditioning -> conditioned);
  N  numbers: counts «… ခု», khandha numbers «… ပါး», group numbers «… မျိုးတွဲ», digits «(n)»;
  I  identity: identical Pāli sentences have identical Burmese sentences (these chapters and the approved sample);
  T  tables: the module's condition names, counts and the new triad terms equal this checker's own copy;
  R  reuse: every value taken from pi-1 … pi-6 (WITNESS) is re-read from the FINAL rails and found in every line
     whose Pāli contains its Pāli; sentences that occur in pi-1 … pi-6 are identical.
--sample  also regenerates the approved sample (1-00, 1-02) and the group 1-03 … 1-05 in memory with this
          generator's extensions and requires them to be identical to the files on disk.
--mutate  plants 8 errors in copies (pi-7-my/chk-mut-ch2-01-02/, deleted afterwards); each must be caught.
--pe      runs pi-3-mr/check_text.py on a «…Pe…»-folded copy of the Pāli in pi-7-my/chk-pe/ch2-01-02/ (deleted).
Exit 1 on any mismatch.
"""
import pathlib
import re
import shutil
import subprocess
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-7_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters"
SAMPLE = ["1-00-paccaya.md", "1-02-vedanattika.md"]
MINE = ["2-01-vitakkattika.md", "2-02-pitittika.md"]
_args = sys.argv[1:]
FLAGS = {a for a in _args if a in ("--mutate", "--sample", "--pe")}
_args = [a for a in _args if a not in FLAGS]
if "--out" in _args:
    OUT = pathlib.Path(_args[_args.index("--out") + 1]).resolve()
    del _args[_args.index("--out"):_args.index("--out") + 2]
NAMES = _args or MINE
ID = re.compile(r"\s*(\^[0-9A-Za-z-]+)\s*$")
W_ = r"[\wāīūṃṅñṭḍṇḷ]"

# ----------------------------------------------------------------------------- this checker's own tables
CONDS_MY = {"hetu": "အမြစ်", "ārammaṇa": "အာရုံ", "adhipati": "အကြီးအမှူး", "anantara": "ချက်ချင်း နောက်၌ ဖြစ်စေခြင်း",
            "samanantara": "ကောင်းစွာ ချက်ချင်း နောက်၌ ဖြစ်စေခြင်း", "sahajāta": "အတူ ပေါ်ပေါက်ခြင်း",
            "aññamañña": "အချင်းချင်း ထောက်ပံ့ခြင်း", "nissaya": "အမှီ", "upanissaya": "အားကြီးသော အမှီ",
            "purejāta": "ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်း", "pacchājāta": "နောက်မှ ဖြစ်ပေါ်ခြင်း",
            "āsevana": "အလေ့အကျင့် ပြုခြင်း", "kamma": "ကံ", "vipāka": "ကံ၏ အကျိုး", "āhāra": "အာဟာရ",
            "indriya": "စွမ်းရည်", "jhāna": "ဈာန်", "magga": "မဂ်", "sampayutta": "ယှဉ်တွဲခြင်း",
            "vippayutta": "ကင်းကွာခြင်း", "atthi": "ရှိခြင်း", "natthi": "မရှိခြင်း", "vigata": "ပျောက်ကွယ်ခြင်း",
            "avigata": "မပျောက်ကွယ်ခြင်း"}
STEMS = sorted(CONDS_MY, key=len, reverse=True)
ABY = "ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော"
# triad terms: key -> Burmese (the pi-1 Mātikā values, typed here again)
TERMS_MY = {
    "savitakkasavicār": "စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှု ရှိသော",
    "avitakkavicāramatt": "စတင်ကြံစည်မှု မရှိဘဲ ဆက်လက်သုံးသပ်မှုသာ ရှိသော",
    "avitakkaavicār": "စတင်ကြံစည်မှုလည်း မရှိ၊ ဆက်လက်သုံးသပ်မှုလည်း မရှိသော",
    "pītisahagat": "ပီတိနှင့်အတူ ဖြစ်သော", "sukhasahagat": "သာယာမှုနှင့်အတူ ဖြစ်သော",
    "upekkhāsahagat": "ဥပေက္ခာနှင့်အတူ ဖြစ်သော"}
NUM_MY = {1: "တစ်", 2: "နှစ်", 3: "သုံး", 4: "လေး", 5: "ငါး", 6: "ခြောက်", 7: "ခုနစ်", 8: "ရှစ်", 9: "ကိုး", 10: "ဆယ်",
          11: "ဆယ့်တစ်", 12: "ဆယ့်နှစ်", 13: "ဆယ့်သုံး", 14: "ဆယ့်လေး", 15: "ဆယ့်ငါး", 16: "ဆယ့်ခြောက်",
          17: "ဆယ့်ခုနစ်", 18: "ဆယ့်ရှစ်", 19: "ဆယ့်ကိုး", 20: "နှစ်ဆယ်", 21: "နှစ်ဆယ့်တစ်", 22: "နှစ်ဆယ့်နှစ်",
          23: "နှစ်ဆယ့်သုံး", 24: "နှစ်ဆယ့်လေး", 25: "နှစ်ဆယ့်ငါး", 26: "နှစ်ဆယ့်ခြောက်", 27: "နှစ်ဆယ့်ခုနစ်",
          28: "နှစ်ဆယ့်ရှစ်", 29: "နှစ်ဆယ့်ကိုး", 30: "သုံးဆယ်", 31: "သုံးဆယ့်တစ်", 32: "သုံးဆယ့်နှစ်", 33: "သုံးဆယ့်သုံး",
          34: "သုံးဆယ့်လေး", 35: "သုံးဆယ့်ငါး", 36: "သုံးဆယ့်ခြောက်", 37: "သုံးဆယ့်ခုနစ်"}
MY_NUM = {v: k for k, v in NUM_MY.items()}
COUNT_PI = {"ekaṃ": 1, "ekā": 1, "dve": 2, "tīṇi": 3, "tisso": 3, "cattāri": 4, "pañca": 5, "cha": 6, "satta": 7,
            "aṭṭha": 8, "nava": 9, "dasa": 10, "ekādasa": 11, "dvādasa": 12, "terasa": 13, "cuddasa": 14,
            "pannarasa": 15, "soḷasa": 16, "sattarasa": 17, "aṭṭhārasa": 18, "ekūnavīsati": 19, "vīsati": 20,
            "ekavīsati": 21, "dvāvīsati": 22, "bāvīsati": 22, "tevīsati": 23, "tevīsa": 23, "catuvīsati": 24,
            "ekavīsa": 21, "bāvīsa": 22, "pañcavīsa": 25, "chabbīsa": 26, "sattavīsa": 27, "aṭṭhavīsa": 28,
            "ekūnatiṃsa": 29, "tiṃsa": 30, "ekatiṃsa": 31, "dvattiṃsa": 32, "tettiṃsa": 33, "catuttiṃsa": 34,
            "pañcatiṃsa": 35, "chattiṃsa": 36, "sattatiṃsa": 37,
            "sattasu": 7, "dvīsu": 2, "sattapi": 7, "cattāripi": 4}
KH_PI = {"eko": 1, "ekaṃ": 1, "ekassa": 1, "dve": 2, "dvinnaṃ": 2, "tayo": 3, "tiṇṇannaṃ": 3, "tiṇṇaṃ": 3,
         "cattāro": 4, "pañcannaṃ": 5}
GROUP_PI = {"catukk": 4, "pañcak": 5, "chakk": 6, "sattak": 7, "aṭṭhak": 8, "navak": 9, "dasak": 10, "ekādasak": 11,
            "dvādasak": 12, "terasak": 13, "tevīsak": 23, "catuvīsak": 24}
MULA_PI = {"ekamūlak": 1, "dumūlak": 2, "timūlak": 3, "catumūlak": 4, "pañcamūlak": 5, "tevīsatimūlak": 23}
# notes / headings whose conditions the regexes below cannot see: Pāli -> (Burmese, [(stem, neg)])
NOTE_PAIRS = {
    "(purejāte paṭisandhikkhaṇe natthi)": ("(ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်း၌ ပဋိသန္ဓေ နေသော ခဏ မရှိ)", [("purejāta", False)]),
    "(āsevane vipākaṃ natthi)": ("(အလေ့အကျင့် ပြုခြင်းဟူသော အကြောင်း၌ ကံ၏ အကျိုး မရှိ)", [("āsevana", False)]),
    "(naadhipatipaṭisandhikkhaṇe paripuṇṇaṃ)": ("(အကြီးအမှူးဟူသော အကြောင်း မဟုတ်ခြင်း၌ ပဋိသန္ဓေ နေသော ခဏ၌ ပြည့်စုံသည်)",
                                                [("adhipati", True)]),
    "(natthipi vigatampi anantarasadisaṃ)": ("(မရှိခြင်းလည်း၊ ပျောက်ကွယ်ခြင်းလည်း ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းနှင့် တူသည်)",
                                             [("natthi", False), ("vigata", False), ("anantara", False)]),
    "(Natthipaccayañca vigatapaccayañca anantarasadisaṃ, avigataṃ atthisadisaṃ.)":
        ("(မရှိခြင်းဟူသော အကြောင်းလည်းကောင်း၊ ပျောက်ကွယ်ခြင်းဟူသော အကြောင်းလည်းကောင်း ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းနှင့် "
         "တူသည်၊ မပျောက်ကွယ်ခြင်းသည် ရှိခြင်းနှင့် တူသည်။)",
         [("natthi", False), ("vigata", False), ("anantara", False), ("avigata", False), ("atthi", False)]),
    "*Natthivigatāvigatapaccayā*": ("*မရှိခြင်းဟူသော အကြောင်း၊ ပျောက်ကွယ်ခြင်းဟူသော အကြောင်းနှင့် မပျောက်ကွယ်ခြင်းဟူသော အကြောင်း*",
                                    [("natthi", False), ("vigata", False), ("avigata", False)]),
    "*2-6. Sahajāta-paccaya-nissaya-saṃsaṭṭha-sampayuttavāro*":
        ("*2-6. အတူ ပေါ်ပေါက်ခြင်း၊ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်း၊ အမှီပြု၍ ဖြစ်ပေါ်ခြင်း၊ ရောနှောခြင်းနှင့် "
         "ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်*", []),
}
NOTE_CONDS_SAMPLE = {"(adhipatiyā paṭisandhi natthi)": [("adhipati", False)],
                     "(nādhipati paripuṇṇaṃ paṭisandhikaṃ)": [("adhipati", True)],
                     "(napacchājātampi naāsevanampi": [("pacchājāta", True), ("āsevana", True)],
                     "(aññamaññampi nissayampi": [("aññamañña", False), ("nissaya", False)]}
HEAD_CONDS = {"Saindriya-maggaghaṭanā": [("indriya", False), ("magga", False)],
              "Sādhipati-indriya-maggaghaṭanā": [("adhipati", False), ("indriya", False), ("magga", False)],
              "(saupanissayaṃ)": [("upanissaya", False)], "(sakammaṃ)": [("kamma", False)]}
# negation: Pāli token regex -> number of «မဟုတ်» / of «မ…» negatives expected in the Burmese
NEG_SANDHI = "|".join(x[:-1] for x in STEMS if x.endswith("a"))
_LOCS = ["hetuyā", "adhipatiyā", "atthiyā", "natthiyā"] + [x[:-1] + "e" for x in STEMS
                                                         if x not in ("hetu", "adhipati", "atthi", "natthi")]
NEG_NOT = [(r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])(?:na|no)(?:" + "|".join(sorted(STEMS + _LOCS, key=len, reverse=True)) + "|(?:"
            + NEG_SANDHI + r")(?=ādi))", 1),
           (r"(?<=samanantara)nasahajāta|(?<=vipāka)naāhāra", 1),
           (r"(?<![\wāīūṃṅñṭḍṇḷ])na (?=§C§|\w+paccayena paccayo)", 1),
           (r"(?<![\wāīūṃṅñṭḍṇḷ])na (?=(?:" + "|".join(_LOCS) + r") \w|\w+paccayā)", 1),   # «na adhipatiyā …» apart
           (r"(?i)(?<!kiriy)ābyākat|(?<![\wāīūṃṅñṭḍṇḷ])[Aa]byākat", 2),
           (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])arūp(?:ino|īnaṃ)", 1), (r"(?i)kiriyābyākat", 2),
           (r"(?i)nevasaññānāsaññāyatan", 2), (r"(?i)anattato", 1), (r"nādhipati", 1),
           (r"(?i)nevavipākanavipākadhamma", 2), (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])arūp(?:aṃ|ā|apañh)", 1)]
NEG_MA = [(r"(?i)adukkhamasukh", 2), (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])(?:no)?natthi(?:paccay|yā|\b)", 1),
          (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])(?:no)?avigat", 1), (r"(?i)ahetuk", 1), (r"(?i)aniccato", 1),
          (r"(?i)asamm(?:uyh|oh)antena", 1), (r"(?<=vigat)āvigat", 1), (r"na labbhati", 1), (r"na kātabbaṃ", 1),
          (r"(?<![\wāīūṃṅñṭḍṇḷ])arūpe(?![\wāīūṃṅñṭḍṇḷ])", 1), (r"(?i)ākāsānañcāyatan", 1), (r"(?i)viññāṇañcāyatan", 1),
          (r"(?i)ākiñcaññāyatan", 1), (r"(?i)nevasaññānāsaññāyatan", 1),
          (r"(?i)anupādinnupādāniy", 1), (r"(?i)anupādinnaanupādāniy", 2),
          (r"(?i)asaṃkiliṭṭhasaṃkilesik|asaṅkiliṭṭhasaṃkilisik", 1), (r"(?i)asaṃkiliṭṭhaasaṃkilesik", 2),
          (r"(?i)anuppann", 1), (r"(?i)ṭhānāṭhān", 1), (r"\(Avipākaṃ", 1),
          (r"(?i)avitakkavicāramatt|avitakka vicāramatt", 1), (r"(?i)avitakkaavicār", 2), (r"(?i)ninnān", 1),
          (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])natthi(?:vigat|pi)", 1)]
MA_MY = re.compile(r"မ(?:နာကျင်|သာယာ|ရှိ|ပျောက်ကွယ်|မြဲ|ရောထွေး|တွေ့ရ|ထည့်ရ|ဖြစ်|ညစ်နွမ်း|ပါဝင်)")


SLIPS = {"nasampayuttanavippayutta": "nasampayutta-navippayutta"}     # the generator's slips, read the same way


def nonempty(p):
    out = [l for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
    if p.parent == PALI:
        for a, b in SLIPS.items():
            out = [l.replace(a, b) for l in out]
    return out


def strip_var(s):
    return re.sub(r"\{[^{}]*\}", "", s)


# ----------------------------------------------------------------------------- C: conditions
def seg(comp):
    out = []
    for part in comp.replace(" -", "-").replace("- ", "-").split("-"):
        p = part.lower()
        if p.endswith("ṃ") and p[:-1] in CONDS_MY:
            p = p[:-1]
        if p.endswith("adhipat"):
            p += "i"
        while p:
            for st in STEMS:
                for cand in ([st, st[:-1] + "ā"] if st.endswith(("a", "u")) else [st]):
                    if p.startswith(cand):
                        out.append(st)
                        p = p[len(cand):]
                        if cand != st:
                            p = "a" + p
                        break
                else:
                    continue
                break
            else:
                raise ValueError("seg: " + part)
    return out


def pali_conds(line):
    s = strip_var(ID.sub("", line))
    found = []
    for k, (_, v) in NOTE_PAIRS.items():
        if k in s:
            found += [(s.find(k) + j / 10, st, ng) for j, (st, ng) in enumerate(v)]
            s = s.replace(k, " " * len(k))
    for k, v in NOTE_CONDS_SAMPLE.items():
        i = s.find(k)
        while i >= 0:
            found += [(i + j / 10, st, ng) for j, (st, ng) in enumerate(v)]
            i = s.find(k, i + 1)
    for k, v in HEAD_CONDS.items():
        if k in s:
            found += [(s.find(k) + j / 10, st, ng) for j, (st, ng) in enumerate(v)]
    head = s.startswith("#")
    stems = "|".join(STEMS)
    for m in re.finditer(r"(?i)(?<!" + W_ + r")(na |na|no)?(" + stems + r")paccay", s):
        found.append((m.start(), m.group(2).lower(), bool(m.group(1))))
    loc = {"hetuyā": "hetu", "adhipatiyā": "adhipati", "atthiyā": "atthi", "natthiyā": "natthi"}
    loc.update({x[:-1] + "e": x for x in STEMS if x not in loc})
    for m in re.finditer(r"(?i)(?<!" + W_ + r")(na |no |na|no)?(" + "|".join(sorted(loc, key=len, reverse=True))
                         + r") (?:" + "|".join(COUNT_PI) + r")(?!" + W_ + r")(?! (?:\S+ )?khandh)", s):
        found.append((m.start(), loc[m.group(2).lower()], bool(m.group(1))))
    # «naanantarampi», «naāsevanepi»; bare locatives sharing a count («anantare samanantare … dasa», «… sabbattha»)
    for m in re.finditer(r"(?i)(?<!" + W_ + r")(na|no)?(" + "|".join(STEMS) + r")(?:mpi)(?!" + W_ + ")", s):
        found.append((m.start(), m.group(2).lower(), bool(m.group(1))))
    for m in re.finditer(r"(?i)(?<!" + W_ + r")(na|no)?(" + "|".join(sorted(loc, key=len, reverse=True))
                         + r")(?:pi)?(?= (?:(?:na|no)?(?:" + "|".join(loc) + r")|sabbattha|sabbe|kātabb[āaoṃni]+|ca (?:(?:na|no)?(?:"
                         + "|".join(loc) + r")|" + "|".join(COUNT_PI) + r"))(?!" + W_ + r")|pi sadisaṃ)", s):
        if not any(abs(f[0] - m.start()) < 1 for f in found):
            found.append((m.start(), loc[m.group(2).lower()], bool(m.group(1))))
    sandhi = "|".join(x[:-1] if x.endswith("a") else x for x in STEMS)
    look = r"(?=ādi|sabhāg|mūlak|ghaṭan|duk|sadisaṃ" + ("|-" if head else "") + ")"
    for m in re.finditer(r"(?i)(?<![\wāīūṃṅñṭḍṇḷ-])(na|no)?(" + sandhi + r")a?" + look, s):
        stem = next(x for x in STEMS if x == m.group(2).lower() or x[:-1] == m.group(2).lower())
        if any(abs(f[0] - m.start()) < 1 for f in found):
            continue
        found.append((m.start(), stem, bool(m.group(1))))
    for m in re.finditer(r"(?i)(?<!" + W_ + r")([\wāīūṃṅñṭḍṇḷ]+(?: ?- ?[\wāīūṃṅñṭḍṇḷ]+)+)(?:nti|īti) (?:(?:"
                         + "|".join(COUNT_PI) + r")(?!" + W_ + ")|(?=na|no))", s):
        for k, st in enumerate(seg(m.group(1))):
            found.append((m.start() + k / 100, st, False))
    for m in re.finditer(r"(?i)((?:n[ao][\wāīūṃṅñṭḍṇḷ]+-)+)(?=n[ao][\wāīūṃṅñṭḍṇḷ]+paccayā)", s):
        k = 0
        found = [f for f in found if not (m.start() <= f[0] < m.end())]
        for part in m.group(1).strip("-").split("-"):
            p = part.lower()
            while p:
                pre, p = p[:2], p[2:]
                st = next(x for x in STEMS if p.startswith(x))
                found.append((m.start() + k / 100, st, True))
                p = p[len(st):]
                k += 1
    found.sort()
    return [(st, ng) for _, st, ng in found]


NAME_ALT = "|".join(re.escape(CONDS_MY[s]) for s in sorted(CONDS_MY, key=lambda x: len(CONDS_MY[x]), reverse=True))
MY_NAME = {v: k for k, v in CONDS_MY.items()}
GH_MY = re.compile(r"((?:(?:" + NAME_ALT + r")၊ )*(?:" + NAME_ALT + r")) ဟူသော ပေါင်းစပ်ချက်")


def my_conds(line, pline):
    s = strip_var(ID.sub("", line))
    found = []
    for k, (my, v) in NOTE_PAIRS.items():
        if k in strip_var(pline):
            if my not in s:
                return None                              # the note's Burmese is not the checker's
            found += [(s.find(my) + j / 10, st, ng) for j, (st, ng) in enumerate(v)]
            s = s.replace(my, " " * len(my))
    for m in re.finditer(r"(?<![^\s(“*])(" + NAME_ALT + r")ဟူသော အကြောင်း((?:ကြောင့်)? မဟုတ်)?", s):
        found.append((m.start(), MY_NAME[m.group(1)], bool(m.group(2))))
    for m in GH_MY.finditer(s):
        for k, nm in enumerate(m.group(1).split("၊ ")):
            found.append((m.start() + k / 100, MY_NAME[nm], False))
    for m in re.finditer(r"(?<![^\s(])(" + NAME_ALT + r")( မဟုတ်ခြင်း)?နှင့် တူ", s):    # «(Xsadisaṃ)» bare names
        found.append((m.start(), MY_NAME[m.group(1)], bool(m.group(2))))
    found.sort()
    return [(st, ng) for _, st, ng in found]


# ----------------------------------------------------------------------------- O: triad terms
_NUMS = "|".join(sorted(COUNT_PI, key=len, reverse=True))
T_PI = re.compile(r"(?i)(savitakkasavicār|avitakkavicāramatt|avitakkaavicār|pītisahagat|sukhasahagat|upekkhāsahagat)")
T_ALIAS = {}
T_MY = re.compile("(" + "|".join(re.escape(v) for v in sorted(TERMS_MY.values(), key=len, reverse=True)) + ")")
MY_T = {v: k for k, v in TERMS_MY.items()}


def pali_terms(line):
    out = []
    for m in T_PI.finditer(strip_var(line).replace("avitakka vicāramatt", "avitakkavicāramatt")):
        k = m.group(1).lower()
        out.append(T_ALIAS.get(k, k))
    return out


def my_terms(line):
    return [MY_T[m.group(1)] for m in T_MY.finditer(strip_var(line))]


# ----------------------------------------------------------------------------- N: numbers
KH_NOUN = r"(?:khandh|mahābhūt|viññāṇ|paccay)"


def pali_numbers(line):
    s = strip_var(ID.sub("", line))
    cnt, kh, grp = [], [], []
    for m in re.finditer(r"(?<!" + W_ + r")(" + "|".join(sorted(COUNT_PI, key=len, reverse=True)) + r")(?!" + W_
                         + r")(?! (?:\S+ )?" + KH_NOUN + r")", s):
        if m.group(1) in ("ekaṃ", "dve") and re.match(r" (?:\S+ )?" + KH_NOUN, s[m.end():]):
            continue
        cnt.append((m.start(), COUNT_PI[m.group(1)]))
    for m in re.finditer(r"(?i)(?<!" + W_ + r")(" + "|".join(MULA_PI) + r")", s):
        cnt.append((m.start(), MULA_PI[m.group(1).lower()]))
    if "ekekassa padassa" in s.lower():
        cnt.append((s.lower().find("ekekassa"), 1))
    if "tiṇṇannaṃ kātabbā" in s:
        cnt.append((s.find("tiṇṇannaṃ kātabbā"), 3))
    for m in re.finditer(r"(?i)(?<!" + W_ + r")(" + "|".join(KH_PI) + r")(?!" + W_ + r")(?= (?:\S+ )?" + KH_NOUN
                         + r"|(?:…pe…)?…|\.\.\.|(?:…pe…)?[.,)]| (?:\S+ )?§)", s):
        w = m.group(1).lower()
        if w in ("ekaṃ", "dve") and not re.match(r" (?:\S+ )?" + KH_NOUN, s[m.end():]):
            continue
        kh.append((m.start(), KH_PI[w]))
    for m in re.finditer(r"(?i)(pañca|catu)viññāṇ", s):
        kh.append((m.start(), 5 if m.group(1).lower() == "pañca" else 4))
    for m in re.finditer(r"(?i)(?<!" + W_ + r")(tevīsati|catuvīsati|vīsati)paccayā", s):
        kh.append((m.start(), {"tevīsati": 23, "catuvīsati": 24, "vīsati": 20}[m.group(1).lower()]))
    for m in re.finditer(r"tayokhandh", s):                       # source slip «tayokhandhā»
        kh.append((m.start(), 3))
    if "Cha " in s and "nayā" in s:
        kh.append((s.find("Cha "), 6))
    if "saddhāpañcamakesu" in s:
        kh.append((s.find("saddhāpañcamakesu"), 5))
    for m in re.finditer(r"(?i)((?<!ghā)t?tik|duk)(?=[aāue])|(" + "|".join(GROUP_PI) + r")", s):
        grp.append(3 if m.group(1) and "tik" in m.group(1).lower() else (2 if m.group(1) else GROUP_PI[m.group(2).lower()]))
    digits = re.findall(r"\((\d+)\.?\)", s)
    return [v for _, v in sorted(cnt)], [v for _, v in sorted(kh)], grp, digits


def my_numbers(line):
    s = strip_var(ID.sub("", line))
    alt = "|".join(sorted(MY_NUM, key=len, reverse=True))
    cnt = [MY_NUM[m.group(1)] for m in re.finditer(r"(?<!ဆယ့်)(?<!နှစ်ဆယ့်)(" + alt + r")ခု", s)]
    kh = [MY_NUM[m.group(1)] for m in re.finditer(r"(?<!သူ)(?<!ဆယ့်)(" + alt + r")ပါး", s)]
    grp = [MY_NUM[m.group(1)] for m in re.finditer(r"(?<!ဆယ့်)(" + alt + r")မျိုးတွဲ", s)]
    digits = re.findall(r"\((\d+)\.?\)", s)
    return cnt, kh, grp, digits


# ----------------------------------------------------------------------------- run
def load_make():
    import importlib.util
    spec = importlib.util.spec_from_file_location("make_ch2_01_02", HERE / "make_ch2-01-02.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def check(names, out):
    mk = load_make()
    F = mk.F
    bad = []
    stats = {k: 0 for k in "SPCONITR"}
    pairs_all = []
    for name in names:
        pl, ml = nonempty(PALI / name), nonempty(out / name)
        if len(pl) != len(ml):
            bad.append(("S", name, 0, f"line count {len(pl)} vs {len(ml)}"))
            continue
        for i, (p, m) in enumerate(zip(pl, ml), 1):
            pairs_all.append((name, i, p, m))
            stats["S"] += 1
            pid, mid = ID.search(p), ID.search(m)
            if (pid and pid.group(1)) != (mid and mid.group(1)):
                bad.append(("S", name, i, "block id"))
            if p.startswith("#") and p.split(" ")[0] != m.split(" ")[0]:
                bad.append(("S", name, i, "heading level"))
            if any(x in m for x in ("?", "।", ":-")):
                bad.append(("S", name, i, "forbidden mark"))
            body = re.sub(r"\{[^{}]*\}", "", ID.sub("", m))
            if re.search(r"[A-Za-zāīūṃṅñṭḍṇḷ]{2,}", body):
                bad.append(("S", name, i, "Latin left: " + re.findall(r"[A-Za-zāīūṃṅñṭḍṇḷ]{2,}", body)[0]))
            if re.search(r"[ၠ-႟]|[ꩠ-ꩿ]", m):
                bad.append(("S", name, i, "non-Burmese Myanmar block code point"))
            stats["P"] += 1
            ps = strip_var(p)
            exp_not = sum(len(re.findall(rx, ps)) * n for rx, n in NEG_NOT)
            exp_ma = sum(len(re.findall(rx, ps)) * n for rx, n in NEG_MA)
            got_not = strip_var(m).count("မဟုတ်")
            got_ma = len(MA_MY.findall(strip_var(m)))
            if exp_not != got_not or exp_ma != got_ma:
                bad.append(("P", name, i, f"negation မဟုတ် {exp_not}/{got_not}, မ… {exp_ma}/{got_ma}"))
            stats["C"] += 1
            pc, mc = pali_conds(p), my_conds(m, p)
            if mc is None:
                bad.append(("C", name, i, "a note's Burmese differs from the checker's table"))
            elif pc != mc:
                bad.append(("C", name, i, f"conditions {pc[:6]}… vs {mc[:6]}… ({len(pc)}/{len(mc)})"))
            stats["O"] += 1
            pt, mt = pali_terms(p), my_terms(m)
            if pt != mt:
                bad.append(("O", name, i, f"terms {pt[:6]} vs {mt[:6]} ({len(pt)}/{len(mt)})"))
            stats["N"] += 1
            pn, mn = pali_numbers(p), my_numbers(m)
            for lab, a, b in zip(("counts", "khandha", "groups", "digits"), pn, mn):
                if a != b:
                    bad.append(("N", name, i, f"{lab} {a} vs {b}"))
    # I: identity (these chapters + the approved sample on disk)
    seen = {}
    extra = []
    for n in SAMPLE + ["1-03-vipakattika.md", "1-04-upadinnattika.md", "1-05-sankilitthattika.md"]:
        pl, ml = nonempty(PALI / n), nonempty(ROOT / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters" / n)
        extra += [(n, i, p, m) for i, (p, m) in enumerate(zip(pl, ml), 1)]
    for name, i, p, m in pairs_all + extra:
        ps = re.split(r"(?<=[.?])\s+(?=\S)", ID.sub("", p).strip())
        ms = re.split(r"(?<=။)\s+(?=\S)", ID.sub("", m).strip())
        if len(ps) != len(ms):
            continue
        for a, b in zip(ps, ms):
            if name in names:
                stats["I"] += 1
            key = a[:1].lower() + a[1:]
            seen.setdefault(key, {}).setdefault(b, (name, i))
    for k, v in seen.items():
        if len(v) > 1 and any(x[0] in names for x in v.values()):
            bad.append(("I", "-", 0, f"«{k[:70]}» has {len(v)} renderings: {list(v.values())[:3]}"))
    # T: tables
    for st, my in CONDS_MY.items():
        stats["T"] += 1
        if F.N.get(st) != my:
            bad.append(("T", "-", 0, f"condition {st}: module «{F.N.get(st)}» vs checker «{my}»"))
    for tri in ("vitakka", "piti"):
        for k, v in F.TRIADS[tri].items():
            stats["T"] += 1
            want = (TERMS_MY["pītisahagat"] + "၊ " + TERMS_MY["sukhasahagat"] if k == "pītisukhasahagat"
                    else TERMS_MY.get(k))
            if want != v:
                bad.append(("T", "-", 0, f"term {k}: module «{v}» vs checker «{want}»"))
    for w, n in COUNT_PI.items():
        if w in F.COUNT:
            stats["T"] += 1
            if F.COUNT[w] != NUM_MY[n] + "ခု":
                bad.append(("T", "-", 0, f"count {w}"))
    # R: reuse
    reuse_n = reuse_ok = 0
    for pali, (book, bid, my) in F.WITNESS.items():
        f_, pseg, mseg = F.FINAL.SEG[book][bid]
        if my not in " ".join(mseg):
            bad.append(("R", "-", 0, f"witness «{pali}» no longer in pi-{book} {bid}"))
            continue
        rx = re.compile(r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])" + re.escape(pali) + r"(?![\wāīūṃṅñṭḍṇḷ])")
        hits = [(n_, i, p, m) for n_, i, p, m in pairs_all if rx.search(strip_var(p))]
        if not hits:
            continue
        reuse_n += 1
        miss = [(n_, i) for n_, i, p, m in hits if my not in m]
        if miss:
            bad.append(("R", miss[0][0], miss[0][1], f"«{pali}» = «{my}» (pi-{book} {bid}) not used: {len(miss)} lines"))
        else:
            reuse_ok += 1
    import reuse_index as RI
    idx = RI.index()
    sent_n = sent_ok = 0
    for name, i, p, m in pairs_all:
        ps = re.split(r"(?<=[.?])\s+(?=\S)", ID.sub("", p).strip())
        ms = re.split(r"(?<=။)\s+(?=\S)", ID.sub("", m).strip())
        if len(ps) != len(ms):
            continue
        for a, b in zip(ps, ms):
            k = RI.norm(a)
            if k in idx:
                sent_n += 1
                if b in idx[k]:
                    sent_ok += 1
                else:
                    bad.append(("R", name, i, f"sentence «{a[:50]}» differs from pi-1 … pi-6 {list(idx[k])[:1]}"))
    src = {(n_, i): p for n_, i, p, m in pairs_all}
    for b_ in bad:
        print(*b_, "|", src.get((b_[1], b_[2]), "")[:90])
    print("checked:", ", ".join(f"{k} {v}" for k, v in stats.items() if k != "R"))
    print(f"reuse test: terms {reuse_ok} / {reuse_n} identical (of {len(F.WITNESS)} witnessed values); "
          f"sentences {sent_ok} / {sent_n} identical")
    print(f"{len(bad)} mismatches")
    return mk, bad


def sample_identity(mk):
    """the approved sample, regenerated with this generator's extensions, equals the files on disk"""
    bad = 0
    disk = ROOT / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters"
    for n in SAMPLE:
        src = (PALI / n).read_text(encoding="utf-8-sig")
        for label, txt in (("raw", src), ("prep", mk.prep(src))):
            same = mk.F.translate(txt) == (disk / n).read_text(encoding="utf-8")
            print(f"sample identity {n} ({label}): {'identical' if same else 'DIFFERS'}")
            bad += not same
    for n in ("1-03-vipakattika.md", "1-04-upadinnattika.md", "1-05-sankilitthattika.md"):   # the group 1-03 … 1-05
        same = mk.F.translate(mk.G.prep((PALI / n).read_text(encoding="utf-8-sig"))) == \
            (disk / n).read_text(encoding="utf-8")
        print(f"group 1-03 … 1-05 identity {n} (its own prep, with this generator's extensions): "
              f"{'identical' if same else 'DIFFERS'}")
        bad += not same
    return bad


MUT = [  # (file, old, new, what)
    ("2-01-vitakkattika.md", "အမြစ်ဟူသော အကြောင်း၌ သုံးဆယ့်ခုနစ်ခု", "အမြစ်ဟူသော အကြောင်း၌ သုံးဆယ့်ခြောက်ခု", "count"),
    ("2-01-vitakkattika.md", "အမြစ်ဟူသော အကြောင်းကြောင့် မဟုတ်ဘဲ ဖြစ်ပေါ်သည်", "အမြစ်ဟူသော အကြောင်းကြောင့် ဖြစ်ပေါ်သည်", "polarity"),
    ("2-01-vitakkattika.md", "စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှု ရှိသော သဘောတရားကို မှီ၍ စတင်ကြံစည်မှု မရှိဘဲ ဆက်လက်သုံးသပ်မှုသာ ရှိသော သဘောတရားသည်",
     "စတင်ကြံစည်မှု မရှိဘဲ ဆက်လက်သုံးသပ်မှုသာ ရှိသော သဘောတရားကို မှီ၍ စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှု ရှိသော သဘောတရားသည်", "term order"),
    ("2-02-pitittika.md", "အာရုံဟူသော အကြောင်းဖြင့် အကြောင်း ဖြစ်သည်", "အကြီးအမှူးဟူသော အကြောင်းဖြင့် အကြောင်း ဖြစ်သည်", "condition"),
    ("2-02-pitittika.md", "အစုအဝေး တစ်ပါးကို မှီ၍ အစုအဝေး သုံးပါး", "အစုအဝေး တစ်ပါးကို မှီ၍ အစုအဝေး နှစ်ပါး", "khandha count"),
    ("2-02-pitittika.md", "ဥပေက္ခာနှင့်အတူ ဖြစ်သော", "သာယာမှုနှင့်အတူ ဖြစ်သော", "term"),
    ("2-02-pitittika.md", "(3) ^7-8-1", "(4) ^7-8-1", "digits"),
    ("2-02-pitittika.md", "(ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်း၌ ပဋိသန္ဓေ", "(အလေ့အကျင့် ပြုခြင်းဟူသော အကြောင်း၌ ပဋိသန္ဓေ", "note"),
]


def mutate():
    tmp = HERE / "chk-mut-ch2-01-02"
    caught = 0
    for f, old, new, what in MUT:
        if tmp.exists():
            shutil.rmtree(tmp)
        tmp.mkdir()
        for n in MINE:
            shutil.copy(OUT / n, tmp / n)
        t = (tmp / f).read_text(encoding="utf-8")
        if old not in t:
            print("mutation not applicable:", what)
            continue
        (tmp / f).write_text(t.replace(old, new, 1), encoding="utf-8")
        r = subprocess.run([sys.executable, "-I", "-X", "utf8", str(HERE / "check_ch2-01-02.py"), "--out", str(tmp)],
                           capture_output=True, text=True)
        last = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr[-200:]
        ok = r.returncode != 0
        caught += ok
        print(f"{what:14} -> {'caught' if ok else 'MISSED'} ({last})")
    shutil.rmtree(tmp)
    print(f"{caught} / {len(MUT)} planted errors caught")
    return len(MUT) - caught


def pe_check(names):
    tmp = HERE / "chk-pe" / "ch2-01-02"
    tmp.mkdir(parents=True, exist_ok=True)
    call = []
    for n in names:
        folded = tmp / n
        folded.write_text((PALI / n).read_text(encoding="utf-8-sig").replace("…Pe…", "…pe…"), encoding="utf-8")
        call += [str(folded), str(OUT / n)]
    r = subprocess.run([sys.executable, "-I", "-X", "utf8", str(HERE.parent / "pi-3-mr/check_text.py")] + call)
    shutil.rmtree(tmp)
    try:
        (HERE / "chk-pe").rmdir()                    # only if no other agent's folder is in it
    except OSError:
        pass
    return r.returncode


if __name__ == "__main__":
    mk, bad = check(NAMES, OUT)
    fail = bool(bad)
    if "--sample" in FLAGS:
        fail |= bool(sample_identity(mk))
    if "--pe" in FLAGS:
        fail |= bool(pe_check(NAMES))
    if "--mutate" in FLAGS:
        fail |= bool(mutate())
    sys.exit(1 if fail else 0)
