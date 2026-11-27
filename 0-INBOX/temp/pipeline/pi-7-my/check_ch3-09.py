"""Per-line check of the Burmese pi-7 chapter 3-09 mahantaraduka against the Pāli (adapted from check_ch3-03-06.py;
independent of the generator's frames: its tables and the dyad-term regexes are typed here again; the active dyad of a
line is read from the Pāli dyad headings).

usage: python3 -I -X utf8 check_ch3-09.py [chapter ...] [--out DIR] [--mutate] [--sample] [--pe]
Checks, line by line (Pāli line i <-> Burmese line i):
  S  structure: equal non-empty lines, heading #-level, block IDs, no «?» «।» «:-», no Latin left outside variants;
  P  polarity: «မဟုတ်» count and the «မ…» negatives expected from the Pāli tokens (TABLES NEG_*);
  C  conditions: the sequence of conditions (stem + polarity) named in the Pāli = the sequence of
     «Nဟူသော အကြောင်း» / bare names (ghaṭanā lists, «(Xsadisaṃ)») in the Burmese; whole notes and headings
     whose conditions the regexes cannot see are compared through this checker's own table NOTE_PAIRS / HEAD_CONDS;
  O  term order: the sequence of dyad terms (and dyad names) in the Pāli = the sequence in the Burmese (conditioning -> conditioned);
  N  numbers: counts «… ခု», khandha numbers «… ပါး», group numbers «… မျိုးတွဲ», digits «(n)»;
  I  identity: identical Pāli sentences have identical Burmese sentences (these chapters and the approved sample);
     against the finished groups 1-01 and 1-03 … 1-05 (which differ between themselves in places) the agreement is
     counted and every difference listed (informational);
  T  tables: the module's condition names, counts and the new triad terms equal this checker's own copy;
  R  reuse: every value taken from pi-1 … pi-6 (WITNESS) is re-read from the FINAL rails and found in every line
     whose Pāli contains its Pāli; sentences that occur in pi-1 … pi-6 are identical.
--sample  also regenerates the approved sample (1-00, 1-02) in memory with this generator's extensions and
          requires it to be identical to the files on disk.
--mutate  plants 11 errors in copies (pi-7-my/chk-mut-ch3-09/, deleted afterwards); each must be caught.
--pe      runs pi-3-mr/check_text.py on a «…Pe…»-folded copy of the Pāli in pi-7-my/chk-pe/ch3-09/ (deleted).
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
MINE = ["3-09-mahantaraduka.md"]
GROUPS = ["1-01-kusalattika.md", "1-03-vipakattika.md", "1-04-upadinnattika.md", "1-05-sankilitthattika.md",
          "2-03-dassanenapahatabbattika.md", "2-04-dassanenapahatabbahetukattika.md", "2-05-acayagamittika.md",
          "2-06-sekkhattika.md", "3-01-hetugocchaka.md", "3-02-culantaraduka.md", "3-03-asavagocchaka.md",
          "3-04-sannojanagocchaka.md", "3-05-ganthagocchaka.md", "3-06-oghayogagocchaka.md"]
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
# dyad terms (the pi-1 Mātikā values ^1-M2-55 … ^1-M2-68, typed here again) and their Pāli regexes (raw Pāli)
TERMS_MY = {
    "sarammana": {"S": "အာရုံ ရှိသော", "aS": "အာရုံ မရှိသော"},
    "citta": {"C": "စိတ် ဖြစ်သော", "noC": "စိတ် မဟုတ်သော"},
    "cetasika": {"Ce": "စိတ်၏ အဖော် ဖြစ်သော", "aCe": "စိတ်၏ အဖော် မဟုတ်သော"},
    "cittasamp": {"Csamp": "စိတ်နှင့် ယှဉ်တွဲသော", "Cvipp": "စိတ်နှင့် ကင်းကွာသော"},
    "cittasams": {"Csams": "စိတ်နှင့် ရောနှောသော", "Cvisams": "စိတ်နှင့် မရောနှောသော"},
    "cittasamu": {"Csamu": "စိတ်မှ ဖြစ်ပေါ်လာသော", "noCsamu": "စိတ်မှ ဖြစ်ပေါ်လာသည် မဟုတ်သော"},
    "cittasaha": {"Csaha": "စိတ်နှင့်အတူ တည်ရှိသော", "noCsaha": "စိတ်နှင့်အတူ တည်ရှိသည် မဟုတ်သော"},
    "cittanu": {"Canu": "စိတ်နောက်သို့ လိုက်ပါသော", "noCanu": "စိတ်နောက်သို့ လိုက်ပါသည် မဟုတ်သော"},
    "css": {"Css": "စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာသော", "noCss": "စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာသည် မဟုတ်သော"},
    "csssaha": {"Csssaha": "စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာပြီး စိတ်နှင့်အတူ တည်ရှိသော",
                "noCsssaha": "စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာပြီး စိတ်နှင့်အတူ တည်ရှိသည် မဟုတ်သော"},
    "cssanu": {"Cssanu": "စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာပြီး စိတ်နောက်သို့ လိုက်ပါသော",
               "noCssanu": "စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာပြီး စိတ်နောက်သို့ လိုက်ပါသည် မဟုတ်သော"},
    "ajjhattika": {"A": "အတွင်းပိုင်း", "B": "ပြင်ပ"},
    "upada": {"U": "မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော", "noU": "မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သည် မဟုတ်သော"},
    "upadinna": {"Ud": "ကံကြောင့် ဖြစ်သော", "aUd": "ကံကြောင့် မဖြစ်သော"},
}
_E = r"(?:o|aṃ|añca|assa|ā|ānaṃ|ānañca|e|ena|ādhipati|acittasamaṅgissa|asamaṅgissa|amūlak\w*)"
_NOT_NAME = r"(?!\w*(?:duk|gaman))"
_U = r"(?:ū|uṃ|uñca|ussa|ūnaṃ|ūnañca|uno|u)(?!\w)"
_I = r"(?:ī|iṃ|iñca|issa|īnaṃ|īnañca|ino|i)(?!\w)"
_CSS = "cittasaṃsaṭṭhasamuṭṭhān"
TERM_PI = {
    "sarammana": [(r"[Ss]ārammaṇ" + _E + r"(?!\w)", "S"), (r"[Aa]nārammaṇ" + _E + r"(?!\w)", "aS")],
    "citta": [(r"[Cc]itt" + _E + r"(?= (?:ca )?(?:[Nn]ocitt\w*(?: ca)? )?(?:dhamm|…))", "C"),
              (r"[Nn]ocitt" + _E + r"(?!\w)", "noC")],
    "cetasika": [(r"[Cc]etasik" + _E + r"(?!\w)", "Ce"), (r"[Aa]cetasik" + _E + r"(?!\w)", "aCe")],
    "cittasamp": [(r"[Cc]ittasampayutt(?:ak)?" + _E + r"(?!\w)", "Csamp"), (r"[Cc]ittavippayutt" + _E + r"(?!\w)", "Cvipp")],
    "cittasams": [(r"[Cc]ittasaṃsaṭṭh" + _E + r"(?!\w)", "Csams"), (r"[Cc]ittavisaṃsaṭṭh" + _E + r"(?!\w)", "Cvisams")],
    "cittasamu": [(r"[Cc]ittasamuṭṭhān" + _E + r"(?!\w)", "Csamu"), (r"[Nn]ocittasamuṭṭhān" + _E + r"(?!\w)", "noCsamu")],
    "cittasaha": [(r"[Cc]ittasahabh" + _NOT_NAME + _U, "Csaha"), (r"[Nn]ocittasahabh" + _U, "noCsaha")],
    "cittanu": [(r"[Cc]ittānuparivatt" + _NOT_NAME + _I, "Canu"), (r"[Nn]ocittānuparivatt" + _I, "noCanu")],
    "css": [(r"[Cc]" + _CSS[1:] + _E + r"(?!\w)", "Css"), (r"[Nn]o" + _CSS + _E + r"(?!\w)", "noCss")],
    "csssaha": [(r"[Cc]" + _CSS[1:] + r"asahabh" + _NOT_NAME + _U, "Csssaha"),
                (r"[Nn]o" + _CSS + r"asahabh" + _U, "noCsssaha")],
    "cssanu": [(r"[Cc]" + _CSS[1:] + r"ānuparivatt" + _NOT_NAME + _I, "Cssanu"),
               (r"[Nn]o" + _CSS + r"ānuparivatt" + _I, "noCssanu")],
    "ajjhattika": [(r"[Aa]jjhattik" + _E + r"(?!\w)", "A"), (r"[Bb]āhir" + _E + r"(?!\w)", "B")],
    "upada": [(r"[Nn]o ?upādā(?:dhipati|cittasamaṅgissa|mūlak\w*)?(?!\w)", "noU"),
              (r"[Uu]pādā(?:dhipati|cittasamaṅgissa|mūlak\w*)?(?!\w)", "U")],
    "upadinna": [(r"[Uu]pādinn" + _E + r"(?!\w)", "Ud"), (r"[Aa]nupādinn" + _E + r"(?!\w)", "aUd")],
}
DYAD_HEAD = {"Sārammaṇadukaṃ": "sarammana", "Cittadukaṃ": "citta", "Cetasikadukaṃ": "cetasika",
             "Cittasampayuttadukaṃ": "cittasamp", "Cittasaṃsaṭṭhadukaṃ": "cittasams",
             "Cittasamuṭṭhānadukaṃ": "cittasamu", "Cittasahabhūdukaṃ": "cittasaha",
             "Cittānuparivattidukaṃ": "cittanu", "Cittasaṃsaṭṭhasamuṭṭhānadukaṃ": "css",
             "Cittasaṃsaṭṭhasamuṭṭhānasahabhūdukaṃ": "csssaha",
             "Cittasaṃsaṭṭhasamuṭṭhānānuparivattidukaṃ": "cssanu", "Ajjhattikadukaṃ": "ajjhattika",
             "Upādādukaṃ": "upada", "Upādinnadukaṃ": "upadinna"}
_DU = "နှစ်မျိုးတွဲ"
NAMES_MY = {
    "sārammaṇaduk": f"အာရုံ ရှိခြင်း {_DU}", "cittaduk": f"စိတ် ဖြစ်ခြင်း {_DU}",
    "cetasikaduk": f"စိတ်၏ အဖော် ဖြစ်ခြင်း {_DU}", "cittasampayuttaduk": f"စိတ်နှင့် ယှဉ်တွဲခြင်း {_DU}",
    "cittasaṃsaṭṭhaduk": f"စိတ်နှင့် ရောနှောခြင်း {_DU}", "cittasamuṭṭhānaduk": f"စိတ်မှ ဖြစ်ပေါ်လာခြင်း {_DU}",
    "cittasahabhūduk": f"စိတ်နှင့်အတူ တည်ရှိခြင်း {_DU}", "cittānuparivattiduk": f"စိတ်နောက်သို့ လိုက်ပါခြင်း {_DU}",
    "cittasaṃsaṭṭhasamuṭṭhānaduk": f"စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာခြင်း {_DU}",
    "cittasaṃsaṭṭhasamuṭṭhānasahabhūduk": f"စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာပြီး စိတ်နှင့်အတူ တည်ရှိခြင်း {_DU}",
    "cittasaṃsaṭṭhasamuṭṭhānānuparivattiduk":
        f"စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာပြီး စိတ်နောက်သို့ လိုက်ပါခြင်း {_DU}",
    "ajjhattikaduk": f"အတွင်းပိုင်း ဖြစ်ခြင်း {_DU}", "upādāduk": f"မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်ခြင်း {_DU}",
    "upādinnaduk": f"ကံကြောင့် ဖြစ်ခြင်း {_DU}",
    "mahantaraduk": "ကြားညှပ် နှစ်မျိုးတွဲ အစုကြီး",
}
# dyad names inside notes in other forms («-dukasadisaṃ», «-duke», «-gamana-»)
NAME_REF = {"cittasaṃsaṭṭhasamuṭṭhānadukasadis": "cittasaṃsaṭṭhasamuṭṭhānaduk",
            "cittasamuṭṭhānadukasadis": "cittasamuṭṭhānaduk", "cittasamuṭṭhānaduke": "cittasamuṭṭhānaduk",
            "cittasahabhūdukasadis": "cittasahabhūduk", "cittasahabhūduke": "cittasahabhūduk",
            "cittasahabhūgamanasadis": "cittasahabhūduk"}
NUM_MY = {1: "တစ်", 2: "နှစ်", 3: "သုံး", 4: "လေး", 5: "ငါး", 6: "ခြောက်", 7: "ခုနစ်", 8: "ရှစ်", 9: "ကိုး", 10: "ဆယ်",
          11: "ဆယ့်တစ်", 12: "ဆယ့်နှစ်", 13: "ဆယ့်သုံး", 14: "ဆယ့်လေး", 15: "ဆယ့်ငါး", 16: "ဆယ့်ခြောက်",
          17: "ဆယ့်ခုနစ်", 18: "ဆယ့်ရှစ်", 19: "ဆယ့်ကိုး", 20: "နှစ်ဆယ်", 21: "နှစ်ဆယ့်တစ်", 22: "နှစ်ဆယ့်နှစ်",
          23: "နှစ်ဆယ့်သုံး", 24: "နှစ်ဆယ့်လေး"}
MY_NUM = {v: k for k, v in NUM_MY.items()}
COUNT_PI = {"ekaṃ": 1, "ekā": 1, "dve": 2, "tīṇi": 3, "tisso": 3, "cattāri": 4, "pañca": 5, "cha": 6, "satta": 7,
            "aṭṭha": 8, "nava": 9, "dasa": 10, "ekādasa": 11, "dvādasa": 12, "terasa": 13, "cuddasa": 14,
            "pannarasa": 15, "soḷasa": 16, "sattarasa": 17, "aṭṭhārasa": 18, "ekūnavīsati": 19, "vīsati": 20,
            "ekavīsati": 21, "dvāvīsati": 22, "bāvīsati": 22, "tevīsati": 23, "tevīsa": 23, "catuvīsati": 24,
            "ekavīsa": 21, "sattārasa": 17, "dvepi": 2, "cattāripi": 4,
            # 3-01 … 3-02 notes: «-pi» (all N «…ခုလုံး»), locatives «dvīsu / tīsupi», «ekāyeva» «တစ်ခုတည်း»
            "tīṇipi": 3, "navapi": 9, "dvīsu": 2, "dvīsupi": 2, "tīsupi": 3, "dvinnampi": 2, "ekāyeva": 1, "ekoyeva": 1,
            # 3-03 … 3-06 notes: «ekekampi» / «ekekassa» «တစ်ခုစီ», «tīsuyeva», «navasupi», «tiṇṇampi», «ekampi»
            "ekekampi": 1, "ekekassa": 1, "tīsuyeva": 3, "navasupi": 9, "tiṇṇampi": 3, "ekampi": 1,
            # 3-09 notes: «chasupi», «channampi», «pañcapi», «tīsu», «tiṇṇaṃ» (not before a khandha word), «ekaṃyeva»
            "chasupi": 6, "channampi": 6, "pañcapi": 5, "tīsu": 3, "tiṇṇaṃ": 3, "ekaṃyeva": 1,
            "tīṇiyeva": 3}
KH_PI = {"eka": 1, "eko": 1, "ekaṃ": 1, "ekassa": 1, "dve": 2, "dvinnaṃ": 2, "tayo": 3, "tiṇṇannaṃ": 3, "tiṇṇaṃ": 3,
         "cattāro": 4, "pañcannaṃ": 5}
GROUP_PI = {"catukk": 4, "pañcak": 5, "chakk": 6, "sattak": 7, "aṭṭhak": 8, "navak": 9, "dasak": 10, "ekādasak": 11,
            "dvādasak": 12, "terasak": 13, "tevīsak": 23, "catuvīsak": 24}
MULA_PI = {"ekamūlān": 1, "ekamūlak": 1, "dumūlak": 2, "timūlak": 3, "catumūlak": 4, "pañcamūlak": 5, "tevīsatimūlak": 23}
# notes / headings whose conditions the regexes below cannot see: Pāli -> (Burmese, [(stem, neg)])
NOTE_PAIRS = {
    "*Natthivigatāvigatapaccayā*": ("*မရှိခြင်းဟူသော အကြောင်း၊ ပျောက်ကွယ်ခြင်းဟူသော အကြောင်းနှင့် မပျောက်ကွယ်ခြင်းဟူသော "
                                    "အကြောင်း*", [("natthi", False), ("vigata", False), ("avigata", False)]),
}
NOTE_PAIRS["*Pacchājātāsevanapaccayā*"] = (
    "*နောက်မှ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်းနှင့် အလေ့အကျင့် ပြုခြင်းဟူသော အကြောင်း*",
    [("pacchājāta", False), ("āsevana", False)])
NOTE_PAIRS["naadhipatiyā…pe…"] = ("အကြီးအမှူးဟူသော အကြောင်း မဟုတ်ခြင်း၌…", [("adhipati", True)])   # no count (cut)
NOTE_PAIRS["(hetusadisā, adhipatiyā moho natthi)"] = (
    "(အမြစ်နှင့် တူကြသည်၊ အကြီးအမှူးဟူသော အကြောင်း၌ မောဟ မရှိ)", [("hetu", False), ("adhipati", False)])
# 3-01 … 3-02: notes and headings whose condition words the regexes cannot see (or see where there is none)
_V = {"sahajāta": "အတူ ပေါ်ပေါက်ခြင်း", "paccaya": "အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်း", "nissaya": "အမှီပြု၍ ဖြစ်ပေါ်ခြင်း",
      "saṃsaṭṭha": "ရောနှောခြင်း", "sampayutta": "ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်"}
NOTE_PAIRS.update({
    "2-6 Sahajāta-paccaya-nissaya-saṃsaṭṭha-sampayuttavāro":
        (f"2-6 {_V['sahajāta']}၊ {_V['paccaya']}၊ {_V['nissaya']}၊ {_V['saṃsaṭṭha']}နှင့် {_V['sampayutta']}", []),
    "2-6. Sahajāta-paccaya-nissaya-saṃsaṭṭha-sampayuttavāro":
        (f"2-6. {_V['sahajāta']}၊ {_V['paccaya']}၊ {_V['nissaya']}၊ {_V['saṃsaṭṭha']}နှင့် {_V['sampayutta']}", []),
    "4-6. Nissaya-saṃsaṭṭha-sampayuttavāro": (f"4-6. {_V['nissaya']}၊ {_V['saṃsaṭṭha']}နှင့် {_V['sampayutta']}", []),
    "(dutiyaupanissayasadisaṃ)": ("(ဒုတိယ အားကြီးသော အမှီနှင့် တူသည်)", [("upanissaya", False)]),
    "Vipākavibhaṅge nava pañhā": ("ကံ၏ အကျိုးဟူသော အကြောင်း၏ ခွဲခြမ်းစိတ်ဖြာခြင်း၌ ပြဿနာ ကိုးခု",
                                  [("vipāka", False)]),
    "(jhānampi maggampi sahajātapaccayasadisā, bāhirā mahābhūtā natthi )":
        ("(ဈာန်ဟူသော အကြောင်းလည်း၊ မဂ်ဟူသော အကြောင်းလည်း အတူ ပေါ်ပေါက်ခြင်းဟူသော အကြောင်းနှင့် တူကြသည်၊ ပြင်ပ "
         "မူလဓာတ်ကြီးတို့ မရှိ)", [("jhāna", False), ("magga", False), ("sahajāta", False)]),
    "(anulomasahajātasadisā)": ("(အဟုတ်ပြ ပုံစံ၏ အတူ ပေါ်ပေါက်ခြင်းဟူသော အကြောင်းနှင့် တူကြသည်)",
                                [("sahajāta", False)]),
    "ādhipatiyā cattāri": ("အကြီးအမှူးဟူသော အကြောင်း၌ လေးခု", [("adhipati", False)]),   # source slip «ā-»
    "(dve pañhā upanissayamūlaṃ)": ("(အားကြီးသော အမှီဟူသော အကြောင်းကို အခြေခံခြင်း၌ ပြဿနာ နှစ်ခု)",
                                    [("upanissaya", False)]),
    "*Vipākāhārapaccayā*": ("*ကံ၏ အကျိုးဟူသော အကြောင်းနှင့် အာဟာရဟူသော အကြောင်း*",
                            [("vipāka", False), ("āhāra", False)]),
    "(naanantarapadādī paccanīyasadisā)":
        ("(ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း ပုဒ် စသည်တို့သည် အငြင်းပြ ပုံစံနှင့် တူကြသည်)",
         [("anantara", True)]),
    "(nasamanantarapadādī paccanīyasadisā)":
        ("(ကောင်းစွာ ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်း မဟုတ်ခြင်း ပုဒ် စသည်တို့သည် အငြင်းပြ ပုံစံနှင့် "
         "တူကြသည်)", [("samanantara", True)]),
    # dyad terms with «-mūlaka» (not the condition): «nahetumūlakaṃ», «sahetuko ceva na ca hetumūlakaṃ / -e»
    "(nahetumūlakaṃ tīṇipi ekasadisaṃ)": ("(အမြစ် မဟုတ်သော သဘောတရားကို အခြေခံခြင်း၌ သုံးခုလုံး တူညီကြသည်)", []),
    "(hetumūlake tīṇi)": ("(အမြစ် ဖြစ်သော သဘောတရားကို အခြေခံခြင်း၌ သုံးခု)", []),
    "Sahetuko ceva na ca hetumūlak": ("အမြစ် ရှိသော်လည်း အမြစ် မဟုတ်သော သဘောတရားကို အခြေခံခြင်း", []),
})
# 3-03 … 3-06: whole notes whose condition words the regexes cannot see; the conditions typed here, the Burmese of the
# note read from the generator's note table (it must stand in the line)
NOTE_CONDS_MINE = {
    # 3-09: whole notes whose condition words the regexes cannot see (or see where there is none)
    "(sahajātapaccayavārasadisaṃ ninnānākaraṇaṃ, paṭhamagamanasadisaṃyeva. Sabbe padā paṭhamaghaṭanānayena "
    "vibhajitabbā)": [],
    "(Idha atthi sabbaṭṭhāne sahajātaṃ paccayavārasadisaṃ. Purejātaṃ purejātasadisaṃ. Pacchājātaṃ "
    "pacchājātasadisaṃ kātabbaṃ, ninnānākaraṇaṃ)": [("atthi", False), ("purejāta", False), ("pacchājāta", False)],
    "(Saṃkhittaṃ. Yathā cittasahabhūduke ārammaṇaṃ evaṃ kātabbaṃ, ninnānākaraṇaṃ. Navapi pañhā.)":
        [("ārammaṇa", False)],
    "(iminākāreneva pacchājāto vitthāretabbo)": [("pacchājāta", False)],
    "(cittasamuṭṭhānadukasadisā. Imampi ekaṃ kabaḷīkāraāhārasadisaṃ)": [],     # kabaḷīkāra āhāra (food, not the condition)
}
NOTE_CONDS_SAMPLE = {}
HEAD_CONDS = {}
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
           (r"(?i)nevasaññānāsaññāyatan", 2), (r"(?i)anattato", 1), (r"(?<![\wāīūṃṅñṭḍṇḷ])nādhipati", 1),
           (r"(?i)nevavipākanavipākadhamma", 2),
           (r"(?i)nevadassanena nabhāvanāya", 2), (r"(?i)nevadassanena(?=…)", 2),
           (r"(?i)nevācayagāmināpacayagām|nevācayagāmīnāpacayagām", 2), (r"(?i)nevasekkhanāsekkh|nevasekkhānāsekkh", 2),
           # the dyads of 3-01 … 3-02: nahetū (the long ū is not the condition stem), «… ceva na ca hetu», arūpī
           (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])nahetū", 1), (r"(?<![\wāīūṃṅñṭḍṇḷ])na ca het", 1),
           (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])arūp(?:ī|iṃ|iñca|issa|inā|icittasamaṅgissa)(?![\wāīūṃṅñṭḍṇḷ])", 1),
           (r"(?i)arūpameva|arūpapañh", 1),
           # 3-03 … 3-06: «no X» (term), «… ceva no ca X», the noun arūpa «ရုပ် မဟုတ်သော သဘောတရား»
           (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])no(?:āsav|saññojan|ganth|ogh|yog)", 1),
           (r"(?<![\wāīūṃṅñṭḍṇḷ])no ca (?:āsav|saññojan|ganth|ogh|yog)", 1),
           (r"(?i)arūpāyeva|arūpaṃyeva|(?<![\wāīūṃṅñṭḍṇḷ])arūpaṃ(?= paṭhamaṃ)", 1),
           (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])naārammaṇāpi", 1),
           # 3-09: «no-citta…» / «no upādā» terms «… မဟုတ်သော», acetasika «… မဟုတ်သော», arūpaṃ (noun)
           (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])no ?(?:citt|upādā)", 1), (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])acetasik", 1),
           (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])arūpaṃ(?= sabbaṃ)", 1)]
NEG_MA = [(r"(?i)adukkhamasukh", 2), (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])(?:no)?natthi(?:paccay|yā|\b)", 1),
          (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])(?:no)?avigat", 1), (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])ahetuk", 1), (r"(?i)aniccato", 1),
          (r"(?i)asamm(?:uyh|oh)antena", 1), (r"(?<=vigat)āvigat", 1), (r"na labbhati", 1), (r"(?<![\wāīūṃṅñṭḍṇḷ])na kātabbaṃ", 1), (r"(?i)natthi(?=vigat)", 1),
          (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])arūpe(?![\wāīūṃṅñṭḍṇḷ])", 1), (r"(?i)ākāsānañcāyatan", 1), (r"(?i)viññāṇañcāyatan", 1),
          (r"(?i)ākiñcaññāyatan", 1), (r"(?i)nevasaññānāsaññāyatan", 1),
          (r"(?i)anupādinnupādāniy", 1), (r"(?i)anupādinnaanupādāniy", 2),
          (r"(?i)asaṃkiliṭṭhasaṃkilesik|asaṅkiliṭṭhasaṃkilisik", 1), (r"(?i)asaṃkiliṭṭhaasaṃkilesik", 2),
          (r"(?i)anuppann", 1), (r"(?i)ṭhānāṭhān", 1), (r"\(Avipākaṃ", 1),
          (r"(?i)ninnānaṃ", 1), (r"na likhitā", 1), (r"na samenti", 1),
          # the dyads of 3-01 … 3-02 and their nouns: alobha / adosa / amoha «… မရှိခြင်း», nahetu ahetuka,
          # appaccaya / asaṅkhata / appaṭigha «… မရှိ», anidassana «မမြင်…», kenaci naviññeyya «မသိ…»
          (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])a(?:lobh|dos|moh)", 1), (r"(?i)nahetuahetuk", 1),
          (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])(?:appaccay|asaṅkhat|appaṭigh|anidassan)", 1), (r"(?i)na ?viññeyy", 1),
          (r"(?i)arūpeyeva", 1), (r"(?i)ninnānākaraṇ", 1),
          # 3-03 … 3-06: a-S «… မဖြစ်နိုင်သော», avijjā «အမှန်ကို မသိမှု», «na kātabbaṃ» «မပြုရ»
          (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])(?:anāsav|asaññojaniy|aganthaniy|anoghaniy|ayoganiy)", 1),
          (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])avijjā", 1),
          # 3-09: anārammaṇa «အာရုံ မရှိသော», cittavisaṃsaṭṭha «… မရောနှောသော», anupādinna «… မဖြစ်သော»
          (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])anārammaṇ", 1), (r"(?i)cittavisaṃsaṭṭh", 1), (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])anupādinn", 1)]
MA_MY = re.compile(r"မ(?:ရောနှော|နာကျင်|သာယာ|ရှိ|ပျောက်ကွယ်|မြဲ|ရောထွေး|တွေ့ရ|ထည့်ရ|ဖြစ်|ညစ်နွမ်း|ပါဝင်|ရေးထား|ညီ|မြင်|သိ|ပြုရ)")


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
    s = re.sub(r"(?<![\wāīūṃṅñṭḍṇḷ*])(?:" + "|".join(DYAD_HEAD) + r")(?: niṭṭhitaṃ\.)?", lambda m: " " * len(m[0]), s)
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
    for m in re.finditer(r"(?<![^\s(“*])(" + NAME_ALT + r")ဟူသော အကြောင်း((?:ကြောင့်)? မဟုတ်)?", s):
        found.append((m.start(), MY_NAME[m.group(1)], bool(m.group(2))))
    for m in GH_MY.finditer(s):
        for k, nm in enumerate(m.group(1).split("၊ ")):
            found.append((m.start() + k / 100, MY_NAME[nm], False))
    for m in re.finditer(r"(?<![^\s(])(" + NAME_ALT + r")((?: မဟုတ်ခြင်း)?)နှင့် တူ(?:ကြ)?(?:သည်|သော|အောင်)", s):
        found.append((m.start(), MY_NAME[m.group(1)], bool(m.group(2))))
    found.sort()
    return [(st, ng) for _, st, ng in found]


# ----------------------------------------------------------------------------- O: dyad terms
_ALL_MY = {v: (d, k) for d, tab in TERMS_MY.items() for k, v in tab.items()}
_NAME_MY = {v: "name:" + k for k, v in NAMES_MY.items()}
NAME_PI = re.compile(r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])(" + "|".join(sorted(NAMES_MY, key=len, reverse=True)) + r")(?=aṃ|āni)")
DYAD_OF_LINE = {}


def dyads_of(name):
    """the active dyad of each non-empty Pāli line (from the dyad headings «###### Xdukaṃ»)"""
    if name not in DYAD_OF_LINE:
        cur, out = None, []
        for l in nonempty(PALI / name):
            m = re.match(r"^###### (\S+) \^", l)
            if m and m.group(1) in DYAD_HEAD:
                cur = DYAD_HEAD[m.group(1)]
            out.append(cur)
        first = next(d for d in out if d)
        DYAD_OF_LINE[name] = [d or first for d in out]
    return DYAD_OF_LINE[name]


def pali_terms(line, d):
    s = strip_var(ID.sub("", line))
    found = []
    for m in ([] if re.match(r"^#+ \*", s) else NAME_PI.finditer(s)):   # «*Hetudukaṃ*»: the condition pair
        found.append((m.start(), m.end(), "name:" + m.group(1).lower()))
    for k, v in NAME_REF.items():
        for m in re.finditer("(?i)" + k, s):
            found.append((m.start(), m.end(), "name:" + v))
    for rx, key in TERM_PI[d]:
        for m in re.finditer(r"(?<![\wāīūṃṅñṭḍṇḷ])(?:" + rx + ")", s):
            if not any(a <= m.start() < b for a, b, _ in found):
                found.append((m.start(), m.end(), key))
    found.sort()
    return [k for _, _, k in found]


def my_terms(line, d):
    vals = dict(_NAME_MY)
    vals.update({v: k for k, v in TERMS_MY[d].items()})
    rx = re.compile("(" + "|".join(re.escape(v) for v in sorted(vals, key=len, reverse=True)) + ")")
    return [vals[m.group(1)] for m in rx.finditer(strip_var(ID.sub("", line)))]


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
    pass
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
    for m in re.finditer(r"(?i)pañcāyatanāni", s):
        kh.append((m.start(), 5))
    if "saddhāpañcamakesu" in s:
        kh.append((s.find("saddhāpañcamakesu"), 5))
    for m in re.finditer(r"(?i)((?<!ghā)(?<!ajjha)(?<!ajjhat)(?<!mā)(?<!ka)t?tik|duk)(?=[aāue])|(" + "|".join(GROUP_PI) + r")", s):
        grp.append(3 if m.group(1) and "tik" in m.group(1).lower() else (2 if m.group(1) else GROUP_PI[m.group(2).lower()]))
    for k in NAME_REF:                                    # a dyad named inside a note «… နှစ်မျိုးတွဲ»
        grp += [2] * (s.lower().count(k) if "duk" not in k else 0)
    digits = re.findall(r"\((\d+)\.?\)", s)
    return [v for _, v in sorted(cnt)], [v for _, v in sorted(kh)], grp, digits


def my_numbers(line):
    s = strip_var(ID.sub("", line)).replace("တစ်စုံတစ်ခုသော", "")     # kenaci «တစ်စုံတစ်ခုသော» (not a count)
    alt = "|".join(sorted(MY_NUM, key=len, reverse=True))
    cnt = [MY_NUM[m.group(1)] for m in re.finditer(r"(?<!ဆယ့်)(?<!နှစ်ဆယ့်)(" + alt + r")ခု", s)]
    kh = [MY_NUM[m.group(1)] for m in re.finditer(r"(?<!သူ)(?<!ဆယ့်)(" + alt + r")ပါး", s)]
    grp = [MY_NUM[m.group(1)] for m in re.finditer(r"(?<!ဆယ့်)(" + alt + r")မျိုးတွဲ", s)]
    digits = re.findall(r"\((\d+)\.?\)", s)
    return cnt, kh, grp, digits


# ----------------------------------------------------------------------------- run
def load_make():
    import importlib.util
    spec = importlib.util.spec_from_file_location("make_ch3_09", HERE / "make_ch3-09.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


GROUP_DIFF = []


def check(names, out):
    mk = load_make()
    F = mk.F
    for k, v in NOTE_CONDS_MINE.items():
        NOTE_PAIRS[k] = (mk.M3.NOTEP[k], v)
    bad = []
    stats = {k: 0 for k in "SPCONITR"}
    mk.K.CUR["fix"] = True
    pairs_all = []
    for name in names:
        pl, ml = nonempty(PALI / name), nonempty(out / name)
        dl = dyads_of(name)
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
            pt, mt = pali_terms(p, dl[i - 1]), my_terms(m, dl[i - 1])
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
    for d, tab in mk.DYADS.items():
        mine = list(TERMS_MY[d].values())
        gen = [v for k, v in tab.items() if not k.endswith("_both")]
        stats["T"] += len(gen) + 1
        if gen != mine:
            bad.append(("T", "-", 0, f"dyad {d}: generator {gen} vs checker {mine}"))
        both = [v for k, v in tab.items() if k.endswith("_both")]
        if both != [f"{mine[0]}၊ {mine[1]}"]:
            bad.append(("T", "-", 0, f"dyad {d}: both-members value {both}"))
    for p, v in mk.DUKA_NAME.items():
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
    print(f"identity with the finished groups 1-01, 1-03 … 1-05, 2-03 … 2-06, 3-01 … 3-06: {stats['G']} sentences identical "
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
    mk.M3.set_dyad(mk.F, None)
    mk.M3.set_dyad(mk.FG, None)
    mk.FG.translate("")
    for n in SAMPLE:
        src = (PALI / n).read_text(encoding="utf-8-sig")
        for label, txt in (("raw", src), ("prep", mk.M3.prep(src, None))):
            same = mk.F.translate(txt) == (disk / n).read_text(encoding="utf-8")
            print(f"sample identity {n} ({label}): {'identical' if same else 'DIFFERS'}")
            bad += not same
    return bad


MUT = [  # (file, old, new, what)
    ("3-09-mahantaraduka.md", "အမြစ်ဟူသော အကြောင်း၌ ကိုးခု၊ အာရုံဟူသော", "အမြစ်ဟူသော အကြောင်း၌ ရှစ်ခု၊ အာရုံဟူသော", "count"),
    ("3-09-mahantaraduka.md", "အမြစ်ဟူသော အကြောင်းကြောင့် မဟုတ်ဘဲ ဖြစ်ပေါ်သည်", "အမြစ်ဟူသော အကြောင်းကြောင့် ဖြစ်ပေါ်သည်", "polarity"),
    ("3-09-mahantaraduka.md", "စိတ် ဖြစ်သော သဘောတရားကို မှီ၍ စိတ် မဟုတ်သော သဘောတရားသည်",
     "စိတ် မဟုတ်သော သဘောတရားကို မှီ၍ စိတ် ဖြစ်သော သဘောတရားသည်", "term order"),
    ("3-09-mahantaraduka.md", "စိတ်၏ အဖော် ဖြစ်သော သဘောတရားသည် အမြစ်ဟူသော အကြောင်းကြောင့်",
     "စိတ်၏ အဖော် ဖြစ်သော သဘောတရားသည် အာရုံဟူသော အကြောင်းကြောင့်", "condition"),
    ("3-09-mahantaraduka.md", "အစုအဝေး တစ်ပါးကို မှီ၍ အစုအဝေး သုံးပါး", "အစုအဝေး တစ်ပါးကို မှီ၍ အစုအဝေး နှစ်ပါး", "khandha count"),
    ("3-09-mahantaraduka.md", "ကံကြောင့် မဖြစ်သော အစုအဝေး", "ကံကြောင့် ဖြစ်သော အစုအဝေး", "term"),
    ("3-09-mahantaraduka.md", "(3) ^7-32-1\n", "(2) ^7-32-1\n", "digits"),
    ("3-09-mahantaraduka.md", "ဤ ပုံစံအတိုင်းပင် နောက်မှ ဖြစ်ပေါ်ခြင်းဟူသော", "ဤ ပုံစံအတိုင်းပင် ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းဟူသော", "note"),
    ("3-09-mahantaraduka.md", "စိတ်နှင့်အတူ တည်ရှိသော၊ စိတ်နှင့်အတူ တည်ရှိသည် မဟုတ်သော စိတ်မှ", "စိတ်နှင့်အတူ တည်ရှိသော စိတ်မှ",
     "both members"),
    ("3-09-mahantaraduka.md", "မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်ခြင်း နှစ်မျိုးတွဲ ^", "ကံကြောင့် ဖြစ်ခြင်း နှစ်မျိုးတွဲ ^", "dyad name"),
    ("3-09-mahantaraduka.md", "စိတ်နှင့် မရောနှောသော", "စိတ်နှင့် ရောနှောသော", "term (visaṃsaṭṭha)"),
]


def mutate():
    tmp = HERE / "chk-mut-ch3-09"
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
        r = subprocess.run([sys.executable, "-I", "-X", "utf8", str(HERE / "check_ch3-09.py"), "--out", str(tmp)],
                           capture_output=True, text=True)
        last = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr[-200:]
        ok = r.returncode != 0
        caught += ok
        print(f"{what:14} -> {'caught' if ok else 'MISSED'} ({last})")
    shutil.rmtree(tmp)
    print(f"{caught} / {len(MUT)} planted errors caught")
    return len(MUT) - caught


def pe_check(names):
    tmp = HERE / "chk-pe" / "ch3-09"
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
