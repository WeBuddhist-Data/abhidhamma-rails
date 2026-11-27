"""Per-line check of the Burmese pi-7 chapters 2-12 uppannattika, 2-13 atītattika, 2-14 atītārammaṇattika,
2-15 ajjhattattika, 2-16 ajjhattārammaṇattika, 2-17 sanidassanasappaṭighattika against the Pāli (adapted from
check_ch2-03-06.py / check_sample.py; independent of the generator's frames: its tables are typed here again).

usage: python3 -I -X utf8 check_ch2-12-17.py [chapter ...] [--out DIR] [--mutate] [--sample] [--pe]
Checks, line by line (Pāli line i <-> Burmese line i):
  S  structure: equal non-empty lines, heading #-level, block IDs, no «?» «।» «:-», no Latin left outside variants;
  P  polarity: «မဟုတ်» count and the «မ…» negatives expected from the Pāli tokens (TABLES NEG_*);
  C  conditions: the sequence of conditions (stem + polarity) named in the Pāli = the sequence of
     «Nဟူသော အကြောင်း» / bare names (ghaṭanā lists, «(Xsadisaṃ)») in the Burmese; whole notes and headings
     whose conditions the regexes cannot see are compared through this checker's own table NOTE_PAIRS / HEAD_CONDS;
  O  term order: the sequence of triad terms in the Pāli = the sequence in the Burmese (conditioning -> conditioned);
  N  numbers: counts «… ခု», khandha numbers «… ပါး», group numbers «… မျိုးတွဲ», digits «(n)»;
  I  identity: identical Pāli sentences have identical Burmese sentences (these chapters and the approved sample);
     against the finished groups 1-01 and 1-03 … 1-05 (which differ between themselves in places) the agreement is
     counted and every difference listed (informational); also 2-03 … 2-06 (same engine);
  T  tables: the module's condition names, counts and the new triad terms equal this checker's own copy;
  R  reuse: every value taken from pi-1 … pi-6 (WITNESS) is re-read from the FINAL rails and found in every line
     whose Pāli contains its Pāli; sentences that occur in pi-1 … pi-6 are identical.
--sample  also regenerates the approved sample (1-00, 1-02) in memory with this generator's extensions and
          requires it to be identical to the files on disk.
--mutate  plants 10 errors in copies (pi-7-my/chk-mut-ch2-12-17/, deleted afterwards); each must be caught.
--pe      runs pi-3-mr/check_text.py on a «…Pe…»-folded copy of the Pāli in pi-7-my/chk-pe/ch2-12-17/ (deleted).
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
MINE = ["2-12-uppannattika.md", "2-13-atitattika.md", "2-14-atitarammanattika.md", "2-15-ajjhattattika.md",
        "2-16-ajjhattarammanattika.md", "2-17-sanidassanasappatighattika.md"]
GROUPS = ["1-01-kusalattika.md", "1-03-vipakattika.md", "1-04-upadinnattika.md", "1-05-sankilitthattika.md",
          "2-03-dassanenapahatabbattika.md", "2-04-dassanenapahatabbahetukattika.md", "2-05-acayagamittika.md",
          "2-06-sekkhattika.md"]
_args = sys.argv[1:]
FLAGS = {a for a in _args if a in ("--mutate", "--sample", "--pe", "--groups")}
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
# triad terms: key -> Burmese (the pi-1 Mātikā values ^1-M1-17 … ^1-M1-22, typed here again)
TERMS_MY = {
    "uppann": "ဖြစ်ပေါ်ပြီးသော", "anuppann": "မဖြစ်ပေါ်သေးသော", "uppād": "ဖြစ်ပေါ်လာမည့်",
    "atīt": "အတိတ်", "anāgat": "အနာဂတ်", "paccuppann": "ပစ္စုပ္ပန်",
    "atītārammaṇ": "အတိတ်ကို အာရုံပြုသော", "anāgatārammaṇ": "အနာဂတ်ကို အာရုံပြုသော",
    "paccuppannārammaṇ": "ပစ္စုပ္ပန်ကို အာရုံပြုသော",
    "ajjhatt": "မိမိ၌ ရှိသော", "bahiddh": "မိမိ၏ ပြင်ပ၌ ရှိသော", "ajjhattabahiddh": "မိမိ၌နှင့် မိမိ၏ ပြင်ပ၌ ရှိသော",
    "ajjhattārammaṇ": "မိမိ၌ ရှိသည်ကို အာရုံပြုသော", "bahiddhārammaṇ": "မိမိ၏ ပြင်ပ၌ ရှိသည်ကို အာရုံပြုသော",
    "ajjhattabahiddhārammaṇ": "မိမိ၌နှင့် မိမိ၏ ပြင်ပ၌ ရှိသည်ကို အာရုံပြုသော",
    "sanidassanasappaṭigh": "မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိသော", "anidassanasappaṭigh": "မမြင်နိုင်သော်လည်း ထိခိုက်မှု ရှိသော",
    "anidassanaappaṭigh": "မမြင်နိုင်၊ ထိခိုက်မှုလည်း မရှိသော"}
NAMES_MY = {"uppannattik": "ဖြစ်ပေါ်ပြီးခြင်း သုံးမျိုးတွဲ", "atītattik": "အတိတ် သုံးမျိုးတွဲ",
            "atītārammaṇattik": "အတိတ်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲ", "ajjhattattik": "မိမိ၌ ရှိခြင်း သုံးမျိုးတွဲ",
            "ajjhattārammaṇattik": "မိမိ၌ ရှိသည်ကို အာရုံပြုခြင်း သုံးမျိုးတွဲ",
            "sanidassanasappaṭighattik": "မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိခြင်း သုံးမျိုးတွဲ"}
# per chapter: the triad keys counted (the active triad, plus another triad's words used as plain adjectives)
CH_TERMS = {
    "2-12": ["anuppann", "uppann", "uppād"],
    "2-13": ["atīt", "anāgat", "paccuppann"],
    "2-14": ["atītārammaṇ", "anāgatārammaṇ", "paccuppannārammaṇ", "atīt", "anāgat", "paccuppann"],
    "2-15": ["ajjhattabahiddh", "ajjhatt", "bahiddh"],
    "2-16": ["ajjhattārammaṇ", "bahiddhārammaṇ", "ajjhattabahiddhārammaṇ", "ajjhatt", "bahiddh"],
    "2-17": ["sanidassanasappaṭigh", "anidassanasappaṭigh", "anidassanaappaṭigh"]}
TERM_NOT = {"uppād": r"(?!et)", "ajjhatt": r"(?!ik)", "anāgat": r"(?!aṃs)"}   # uppādeti, ajjhattika, anāgataṃsañāṇa
CH_REF = {   # Pāli regex inside a word (no left boundary) -> term key, per chapter
    "2-12": [], "2-15": [], "2-17": [],
    "2-13": [(r"(?<![\wāīūṃṅñṭḍṇḷ])paccuppano(?= eko)", "paccuppann")],      # source slip (read as paccuppanno)
    "2-14": [(r"(?<=ārammaṇa)paccuppann(?=acitta)", "paccuppann")],
    "2-16": [(r"(?<=ārammaṇa)bahiddh(?=ācitta)", "bahiddh")]}
# Burmese words that contain a term value but are not a term (blanked before the term count)
MY_NOT_TERM = ["အနာဂတ်ကို သိသော ဉာဏ်", "ရှေးဦးစွာ ဖြစ်ပေါ်ပြီးသော"]
NUM_MY = {1: "တစ်", 2: "နှစ်", 3: "သုံး", 4: "လေး", 5: "ငါး", 6: "ခြောက်", 7: "ခုနစ်", 8: "ရှစ်", 9: "ကိုး", 10: "ဆယ်",
          11: "ဆယ့်တစ်", 12: "ဆယ့်နှစ်", 13: "ဆယ့်သုံး", 14: "ဆယ့်လေး", 15: "ဆယ့်ငါး", 16: "ဆယ့်ခြောက်",
          17: "ဆယ့်ခုနစ်", 18: "ဆယ့်ရှစ်", 19: "ဆယ့်ကိုး", 20: "နှစ်ဆယ်", 21: "နှစ်ဆယ့်တစ်", 22: "နှစ်ဆယ့်နှစ်",
          23: "နှစ်ဆယ့်သုံး", 24: "နှစ်ဆယ့်လေး", 25: "နှစ်ဆယ့်ငါး"}
MY_NUM = {v: k for k, v in NUM_MY.items()}
COUNT_PI = {"ekaṃ": 1, "ekā": 1, "dve": 2, "tīṇi": 3, "tisso": 3, "cattāri": 4, "pañca": 5, "cha": 6, "satta": 7,
            "aṭṭha": 8, "nava": 9, "dasa": 10, "ekādasa": 11, "dvādasa": 12, "terasa": 13, "cuddasa": 14,
            "pannarasa": 15, "soḷasa": 16, "sattarasa": 17, "aṭṭhārasa": 18, "ekūnavīsati": 19, "vīsati": 20,
            "ekavīsati": 21, "dvāvīsati": 22, "bāvīsati": 22, "tevīsati": 23, "tevīsa": 23, "catuvīsati": 24,
            "ekavīsa": 21, "sattārasa": 17, "dvepi": 2, "cattāripi": 4, "pañcavīsa": 25, "dvāvīsa": 22,
            "bāvīsa": 22, "catuvīsa": 24, "cattāro": 4, "catasso": 4, "sattapi": 7, "tissopi": 3, "ekaṃyeva": 1,
            "ekavīsāpi": 21, "sattasupi": 7}
KH_PI = {"eko": 1, "ekaṃ": 1, "ekassa": 1, "dve": 2, "dvinnaṃ": 2, "tayo": 3, "tiṇṇannaṃ": 3, "tiṇṇaṃ": 3,
         "cattāro": 4, "pañcannaṃ": 5}
GROUP_PI = {"catukk": 4, "pañcak": 5, "chakk": 6, "sattak": 7, "aṭṭhak": 8, "navak": 9, "dasak": 10, "ekādasak": 11,
            "dvādasak": 12, "terasak": 13, "tevīsak": 23, "catuvīsak": 24}
MULA_PI = {"ekamūlak": 1, "dumūlak": 2, "timūlak": 3, "catumūlak": 4, "pañcamūlak": 5, "tevīsatimūlak": 23}
# notes / headings whose conditions the regexes below cannot see: Pāli -> (Burmese, [(stem, neg)])
NOTE_PAIRS = {
    "*Natthivigatāvigatapaccayā*": ("*မရှိခြင်းဟူသော အကြောင်း၊ ပျောက်ကွယ်ခြင်းဟူသော အကြောင်းနှင့် မပျောက်ကွယ်ခြင်းဟူသော "
                                    "အကြောင်း*", [("natthi", False), ("vigata", False), ("avigata", False)]),
}
NOTE_PAIRS["(hetusadisā, adhipatiyā moho natthi)"] = (
    "(အမြစ်နှင့် တူကြသည်၊ အကြီးအမှူးဟူသော အကြောင်း၌ မောဟ မရှိ)", [("hetu", False), ("adhipati", False)])
NOTE_PAIRS["(Natthivigatapaccayaṃ anantarasadisaṃ."] = (
    "(မရှိခြင်းဟူသော အကြောင်း၊ ပျောက်ကွယ်ခြင်းဟူသော အကြောင်းသည် ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းနှင့် တူသည်။",
    [("natthi", False), ("vigata", False), ("anantara", False)])
NOTE_CONDS_SAMPLE = {}
for _k, _my, _v in (
        ("(adhipatiyā paṭisandhi natthi)", "(အကြီးအမှူးဟူသော အကြောင်း၌ ပဋိသန္ဓေ မရှိ)", [("adhipati", False)]),
        ("(purejātepi āsevanepi paṭisandhi natthi)",
         "(ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်း၌လည်း၊ အလေ့အကျင့် ပြုခြင်းဟူသော အကြောင်း၌လည်း ပဋိသန္ဓေ မရှိ)",
         [("purejāta", False), ("āsevana", False)]),
        ("(navipāke paṭisandhi natthi)", "(ကံ၏ အကျိုးဟူသော အကြောင်း မဟုတ်ခြင်း၌ ပဋိသန္ဓေ မရှိ)", [("vipāka", True)]),
        ("(anulomasahajātasadisaṃ, ninnānākaraṇaṃ)", "(အဟုတ်ပြ ပုံစံ၌ အတူ ပေါ်ပေါက်ခြင်းနှင့် တူသည်၊ ကွဲပြားချက် မရှိ)",
         [("sahajāta", False)]),
        ("(anulomasahajātasadisaṃ)", "(အဟုတ်ပြ ပုံစံ၌ အတူ ပေါ်ပေါက်ခြင်းနှင့် တူသည်)", [("sahajāta", False)]),
        ("*2-6. Sahajāta-paccaya-nissaya-saṃsaṭṭha-sampayuttavāro*",
         "*2-6. အတူ ပေါ်ပေါက်ခြင်း၊ အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်း၊ အမှီပြု၍ ဖြစ်ပေါ်ခြင်း၊ ရောနှောခြင်းနှင့် ယှဉ်တွဲခြင်းအလိုက် "
         "ဖော်ပြချက်*", []),
        ("*4-6. Nissaya-saṃsaṭṭha-sampayuttavāro*",
         "*4-6. အမှီပြု၍ ဖြစ်ပေါ်ခြင်း၊ ရောနှောခြင်းနှင့် ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်*", []),
        ("(avipākaṃ-4)", "(ကံ၏ အကျိုးဟူသော အကြောင်း မပါဝင်သော-4)", [("vipāka", False)]),
        ("(savipākaṃ-5)", "(ကံ၏ အကျိုးဟူသော အကြောင်း ပါဝင်သော-5)", [("vipāka", False)]),
        ("(kammaṃ vibhajitvā nakammeneva ekavīsa pañhā kātabbā)",
         "(ကံကို ခွဲခြမ်းစိတ်ဖြာ၍ ကံဟူသော အကြောင်း မဟုတ်ခြင်းဖြင့်ပင် ပြဿနာ နှစ်ဆယ့်တစ်ခုကို ပြုရမည်)", [("kamma", True)])):
    NOTE_PAIRS[_k] = (_my, _v)
HEAD_CONDS = {"Hetusāmaññaghaṭanā": [("hetu", False)], "*Nahetutikaṃ*": [("hetu", True)]}
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
           (r"(?i)nevasaññānāsaññāyatan", 2), (r"(?i)anattato", 1), (r"(?<!ppan)nādhipati", 1),
           (r"(?i)nevavipākanavipākadhamma", 2),
           (r"(?i)nevadassanena nabhāvanāya", 2), (r"(?i)nevadassanena(?=…)", 2),
           (r"(?i)nevācayagāmināpacayagām|nevācayagāmīnāpacayagām", 2), (r"(?i)nevasekkhanāsekkh|nevasekkhānāsekkh", 2),
           (r"(?i)anattānupassan", 1), (r"(?i)arūpeyeva", 1)]
NEG_MA = [(r"(?i)adukkhamasukh", 2), (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])(?:no)?natthi(?:paccay|yā|\b)", 1),
          (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])(?:no)?avigat", 1), (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])ahetuk", 1), (r"(?i)aniccato", 1),
          (r"(?i)asamm(?:uyh|oh)antena", 1), (r"(?<=vigat)āvigat", 1), (r"na labbhati", 1), (r"(?<![\wāīūṃṅñṭḍṇḷ])na kātabbaṃ", 1), (r"(?i)natthi(?=vigat)", 1),
          (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])arūpe(?![\wāīūṃṅñṭḍṇḷ])", 1), (r"(?i)ākāsānañcāyatan", 1), (r"(?i)viññāṇañcāyatan", 1),
          (r"(?i)ākiñcaññāyatan", 1), (r"(?i)nevasaññānāsaññāyatan", 1),
          (r"(?i)anupādinnupādāniy", 1), (r"(?i)anupādinnaanupādāniy", 2),
          (r"(?i)asaṃkiliṭṭhasaṃkilesik|asaṅkiliṭṭhasaṃkilisik", 1), (r"(?i)asaṃkiliṭṭhaasaṃkilesik", 2),
          (r"(?i)anuppann", 1), (r"(?i)ṭhānāṭhān", 1), (r"\(Avipākaṃ", 1),
          (r"(?i)ninnānaṃ", 1), (r"na likhitā", 1), (r"na samenti", 1),
          (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])anidassan", 1), (r"(?i)(?<![sS])appaṭigh", 1), (r"(?i)aniccānupassan", 1),
          (r"\(avipākaṃ", 1), (r"(?i)ninnānākaraṇ", 1),
          (r"(?<=atthi)avigat", 1)]
MA_MY = re.compile(r"မ(?:မြင်နိုင်|နာကျင်|သာယာ|ရှိ|ပျောက်ကွယ်|မြဲ|ရောထွေး|တွေ့ရ|ထည့်ရ|ဖြစ်|ညစ်နွမ်း|ပါဝင်|ရေးထား|ညီ)")


def nonempty(p):
    return [l for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]


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
    _la = "|".join(sorted(loc, key=len, reverse=True))
    for m in re.finditer(r"(?i)(?<!" + W_ + r")(na |no |na|no)?(" + _la + r")(?= (?:(?:na|no)?(?:" + _la + r") )*"
                         r"(?:sabbattha )?(?:" + "|".join(COUNT_PI) + r")(?!" + W_ + r")(?! (?:\S+ )?khandh))", s):
        found.append((m.start(), loc[m.group(2).lower()], bool(m.group(1))))
    for m in re.finditer(r"(?i)(?<!" + W_ + r")((?:(?:na|no)?(?:" + _la + r")(?: |(?=…)))+)(?=…)", s):   # a run cut by «…»
        for w in re.finditer(r"(?i)(na|no)?(" + _la + r")", m.group(1)):
            if not any(abs(f[0] - (m.start() + w.start())) < 1 for f in found):
                found.append((m.start() + w.start(), loc[w.group(2).lower()], bool(w.group(1))))
    sandhi = "|".join(x[:-1] if x.endswith("a") else x for x in STEMS)
    look = r"(?=ādi|sabhāg|mūlak|ghaṭan|duk|sadis" + ("|-" if head else "") + ")"
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
    for m in re.finditer(r"(?<![^\s(“*…])(" + NAME_ALT + r")ဟူသော အကြောင်း((?:ကြောင့်)? မဟုတ်)?", s):
        found.append((m.start(), MY_NAME[m.group(1)], bool(m.group(2))))
    for m in GH_MY.finditer(s):
        for k, nm in enumerate(m.group(1).split("၊ ")):
            found.append((m.start() + k / 100, MY_NAME[nm], False))
    for m in re.finditer(r"(?<![^\s(])(" + NAME_ALT + r")((?: မဟုတ်ခြင်း)?)နှင့် တူ(?:ကြ)?(?:သည်|သော|အောင်)", s):
        found.append((m.start(), MY_NAME[m.group(1)], bool(m.group(2))))
    found.sort()
    return [(st, ng) for _, st, ng in found]


# ----------------------------------------------------------------------------- O: triad terms
_NUMS = "|".join(sorted(COUNT_PI, key=len, reverse=True))
NAME_PI = re.compile(r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])(" + "|".join(sorted(NAMES_MY, key=len, reverse=True)) + ")")


def pali_terms(line, name):
    ch = name[:4]
    s = strip_var(line)
    s = re.sub(r"(?i)anāgataṃsañāṇ", lambda m: " " * len(m[0]), s)
    found = []
    keys = sorted(CH_TERMS[ch], key=len, reverse=True)
    rx = re.compile(r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])(?:" + "|".join(f"({re.escape(k)}){TERM_NOT.get(k, '')}" for k in keys)
                    + ")")
    for m in rx.finditer(s):
        k = next(keys[j] for j, g in enumerate(m.groups()) if g)
        found.append((m.start(), k, len(m[0])))
    for pat, k in CH_REF[ch]:
        for m in re.finditer(pat, s):
            found.append((m.start(), k, len(m[0])))
    for m in NAME_PI.finditer(s):
        found = [f for f in found if not (m.start() <= f[0] < m.end())]
        found.append((m.start(), "name:" + NAMES_MY[m.group(1).lower()], len(m[0])))
    found.sort()
    return [k for _, k, _ in found]


def my_terms(line, name):
    ch = name[:4]
    s = strip_var(line)
    for w in MY_NOT_TERM:
        s = s.replace(w, " " * len(w))
    vals = {TERMS_MY[k]: k for k in CH_TERMS[ch]}
    vals.update({v: "name:" + v for v in NAMES_MY.values()})
    rx = re.compile("(" + "|".join(re.escape(v) for v in sorted(vals, key=len, reverse=True)) + ")")
    return [vals[m.group(1)] for m in rx.finditer(s)]


# ----------------------------------------------------------------------------- N: numbers
KH_NOUN = r"(?:khandh|mahābhūt|viññāṇ)"


def pali_numbers(line):
    s = strip_var(ID.sub("", line))
    cnt, kh, grp = [], [], []
    for m in re.finditer(r"(?i)(?<!" + W_ + r")(" + "|".join(sorted(COUNT_PI, key=len, reverse=True)) + r")(?!" + W_
                         + r")(?! (?:\S+ )?" + KH_NOUN + r")", s):
        if m.group(1) in ("ekaṃ", "dve") and re.match(r" (?:\S+ )?" + KH_NOUN, s[m.end():]):
            continue
        if s[max(0, m.start() - 9):m.start()] == "ahetukaṃ ":       # «ahetukaṃ ekaṃ…» (one aggregate)
            continue
        cnt.append((m.start(), COUNT_PI[m.group(1).lower()]))
    for m in re.finditer(r"(?i)(?<!" + W_ + r")(" + "|".join(MULA_PI) + r")", s):
        cnt.append((m.start(), MULA_PI[m.group(1).lower()]))
    if "ekekassa padassa" in s.lower():
        cnt.append((s.lower().find("ekekassa"), 1))
    if "tiṇṇannaṃ kātabbā" in s:
        cnt.append((s.find("tiṇṇannaṃ kātabbā"), 3))
    for m in re.finditer(r"(?i)(?<!" + W_ + r")(" + "|".join(KH_PI) + r")(?!" + W_ + r")(?= (?:\S+ )?" + KH_NOUN
                         + r"|(?:…pe…)?…|\.\.\.|(?:…pe…)?[.,]| (?:\S+ )?§)", s):
        w = m.group(1).lower()
        if (w in ("ekaṃ", "dve") and not re.match(r" (?:\S+ )?" + KH_NOUN, s[m.end():])
                and s[max(0, m.start() - 9):m.start()] != "ahetukaṃ "):
            continue
        kh.append((m.start(), KH_PI[w]))
    for m in re.finditer(r"(?i)(pañca|catu)viññāṇ", s):
        kh.append((m.start(), 5 if m.group(1).lower() == "pañca" else 4))
    for m in re.finditer(r"(?i)tevīsatipaccayā|catuvīsatipaccayā", s):
        kh.append((m.start(), 23 if m.group(0).lower().startswith("tev") else 24))
    for m in re.finditer(r"tayokhandh", s):                       # source slip «tayokhandhā»
        kh.append((m.start(), 3))
    if "Cha " in s and "nayā" in s:
        kh.append((s.find("Cha "), 6))
    for rx_, n_ in ((r"tayopi paccayā", 3), (r"pañcāyatanāni", 5), (r"pañcavokār", 5)):
        for m in re.finditer(rx_, s):
            kh.append((m.start(), n_))
    for m in re.finditer(r"(?<=aṃ )ekaṃ(?=…)", s):              # «Xārammaṇaṃ ekaṃ…» (one aggregate, cut)
        kh.append((m.start(), 1))
        cnt[:] = [x for x in cnt if x[0] != m.start()]
    if "saddhāpañcamakesu" in s:
        kh.append((s.find("saddhāpañcamakesu"), 5))
    for m in re.finditer(r"(?i)((?<!ghā)(?<!ajjha)(?<!ajjhat)(?<!mā)t?tik|duk)(?=[aāue])|(" + "|".join(GROUP_PI) + r")", s):
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
    spec = importlib.util.spec_from_file_location("make_ch2_12_17", HERE / "make_ch2-12-17.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


GROUP_DIFF = []


def check(names, out):
    mk = load_make()
    F = mk.F
    bad = []
    stats = {k: 0 for k in "SPCONITR"}
    mk.K.CUR["fix"] = True
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
            pt, mt = pali_terms(p, name), my_terms(m, name)
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
    for n in SAMPLE:
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
    grp = {}
    for n in GROUPS:
        pl, ml = nonempty(PALI / n), nonempty(ROOT / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters" / n)
        for i, (p, m) in enumerate(zip(pl, ml), 1):
            ps = re.split(r"(?<=[.?])\s+(?=\S)", ID.sub("", p).strip())
            ms = re.split(r"(?<=။)\s+(?=\S)", ID.sub("", m).strip())
            if len(ps) == len(ms):
                for a, b in zip(ps, ms):
                    grp.setdefault(a[:1].lower() + a[1:], {}).setdefault(b, (n, i))
    g_n = g_ok = 0
    GROUP_DIFF.clear()
    for k, v in seen.items():
        mine = {b: x for b, x in v.items() if x[0] in names}
        if mine and k in grp:
            g_n += 1
            if set(mine) & set(grp[k]):
                g_ok += 1
            else:
                GROUP_DIFF.append((k, list(mine.items())[0], list(grp[k].items())[0]))
    stats["G"] = f"{g_ok} / {g_n}"
    # T: tables
    for st, my in CONDS_MY.items():
        stats["T"] += 1
        if F.N.get(st) != my:
            bad.append(("T", "-", 0, f"condition {st}: module «{F.N.get(st)}» vs checker «{my}»"))
    for tri, tab in mk.TRIADS_ADD.items():
        for k, v in tab.items():
            stats["T"] += 1
            if TERMS_MY.get(k) != v:
                bad.append(("T", "-", 0, f"term {k}: generator «{v}» vs checker «{TERMS_MY.get(k)}»"))
    for p, v in mk.TIKA_ADD.items():
        stats["T"] += 1
        k = p[0].lower() + p[1:-2]
        if NAMES_MY.get(k) != v:
            bad.append(("T", "-", 0, f"name {p}: generator «{v}» vs checker «{NAMES_MY.get(k)}»"))
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
    print("checked:", ", ".join(f"{k} {v}" for k, v in stats.items() if k not in ("R", "G")))
    print(f"reuse test: terms {reuse_ok} / {reuse_n} identical (of {len(F.WITNESS)} witnessed values); "
          f"sentences {sent_ok} / {sent_n} identical")
    print(f"identity with the finished groups 1-01, 1-03 … 1-05, 2-03 … 2-06: {stats['G']} sentences identical "
          f"(the differences are listed with --groups)")
    if "--groups" in sys.argv:
        for k, a, b in GROUP_DIFF:
            print("G |", k[:110], "\n    mine:", a[0][:160], a[1], "\n    grp: ", b[0][:160], b[1])
    print(f"{len(bad)} mismatches")
    return mk, bad


def sample_identity(mk):
    """the approved sample, regenerated with this generator's extensions, equals the files on disk"""
    bad = 0
    disk = ROOT / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters"
    mk.set_triad(mk.F, None)
    mk.set_triad(mk.FG, None)
    mk.FG.translate("")
    for n in SAMPLE:
        src = (PALI / n).read_text(encoding="utf-8-sig")
        for label, txt in (("raw", src), ("prep", mk.prep(src))):
            same = mk.F.translate(txt) == (disk / n).read_text(encoding="utf-8")
            print(f"sample identity {n} ({label}): {'identical' if same else 'DIFFERS'}")
            bad += not same
    return bad


MUT = [  # (file, old, new, what)
    ("2-12-uppannattika.md", "အမြစ်ဟူသော အကြောင်း၌ တစ်ခု၊ အာရုံဟူသော အကြောင်း၌ သုံးခု",
     "အမြစ်ဟူသော အကြောင်း၌ နှစ်ခု၊ အာရုံဟူသော အကြောင်း၌ သုံးခု", "count"),
    ("2-14-atitarammanattika.md", "အမြစ်ဟူသော အကြောင်းကြောင့် မဟုတ်ဘဲ ဖြစ်ပေါ်သည်", "အမြစ်ဟူသော အကြောင်းကြောင့် ဖြစ်ပေါ်သည်",
     "polarity"),
    ("2-13-atitattika.md", "အတိတ် သဘောတရားသည် ပစ္စုပ္ပန် သဘောတရားအား", "ပစ္စုပ္ပန် သဘောတရားသည် အတိတ် သဘောတရားအား",
     "term order"),
    ("2-15-ajjhattattika.md", "အမြစ်ဟူသော အကြောင်းကြောင့် ဖြစ်ပေါ်သည်", "အာရုံဟူသော အကြောင်းကြောင့် ဖြစ်ပေါ်သည်", "condition"),
    ("2-12-uppannattika.md", "အစုအဝေး တစ်ပါးသည် အစုအဝေး သုံးပါးတို့အား", "အစုအဝေး တစ်ပါးသည် အစုအဝေး နှစ်ပါးတို့အား",
     "khandha count"),
    ("2-17-sanidassanasappatighattika.md", "မြင်နိုင်၍ ထိခိုက်မှုလည်း ရှိသော စိတ်မှ",
     "မမြင်နိုင်သော်လည်း ထိခိုက်မှု ရှိသော စိတ်မှ", "term"),
    ("2-12-uppannattika.md", "(1) ^7-18-1", "(2) ^7-18-1", "digits"),
    ("2-16-ajjhattarammanattika.md", "(ပဋိသန္ဓေ မရှိ)", "(ပဋိသန္ဓေ ရှိ)", "note"),
    ("2-13-atitattika.md", "ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း၌၊ ကောင်းစွာ", "ကောင်းစွာ",
     "shared count"),
    ("2-14-atitarammanattika.md", "အတိတ် အစုအဝေး", "အနာဂတ် အစုအဝေး", "adjective term"),
]


def mutate():
    tmp = HERE / "chk-mut-ch2-12-17"
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
        r = subprocess.run([sys.executable, "-I", "-X", "utf8", str(HERE / "check_ch2-12-17.py"), "--out", str(tmp)],
                           capture_output=True, text=True)
        last = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr[-200:]
        ok = r.returncode != 0
        caught += ok
        print(f"{what:14} -> {'caught' if ok else 'MISSED'} ({last})")
    shutil.rmtree(tmp)
    print(f"{caught} / {len(MUT)} planted errors caught")
    return len(MUT) - caught


def pe_check(names):
    tmp = HERE / "chk-pe" / "ch2-12-17"
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
