"""Per-line check of the Burmese pi-7 chapter 4-01 kilesagocchaka (the kilesa dyads and the piṭṭhiduka dyads) against
the Pāli (adapted from check_ch3-07-08-10.py; independent of the generator's frames: its tables and the dyad-term
regexes are typed here again; the active dyad of a line is read from the Pāli dyad headings; the sister dyads of the
piṭṭhiduka that name each other's terms are read as one family).

usage: python3 -I -X utf8 check_ch4-01.py [chapter ...] [--out DIR] [--mutate] [--sample] [--pe] [--groups]
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
--mutate  plants 12 errors in copies (pi-7-my/chk-mut-ch4-01/, deleted afterwards); each must be caught.
--pe      runs pi-3-mr/check_text.py on a «…Pe…»-folded copy of the Pāli in pi-7-my/chk-pe/ch4-01/ (deleted).
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
MINE = ["4-01-kilesagocchaka.md"]
GROUPS = ["1-01-kusalattika.md", "1-03-vipakattika.md", "1-04-upadinnattika.md", "1-05-sankilitthattika.md",
          "2-03-dassanenapahatabbattika.md", "2-04-dassanenapahatabbahetukattika.md", "2-05-acayagamittika.md",
          "2-06-sekkhattika.md", "3-01-hetugocchaka.md", "3-02-culantaraduka.md", "2-01-vitakkattika.md",
          "2-02-pitittika.md", "3-03-asavagocchaka.md", "3-04-sannojanagocchaka.md", "3-05-ganthagocchaka.md",
          "3-06-oghayogagocchaka.md", "3-07-nivaranagocchaka.md", "3-08-paramasagocchaka.md",
          "3-10-upadanagocchaka.md"]
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
# dyad terms (the pi-1 Mātikā values ^1-M2-75 … ^1-M2-100, typed here again; two NEW for the eighth kilesa dyad)
_K = "ကိလေသာ"
TERMS_MY = {
    "kil1": {"kilesa": f"{_K} ဖြစ်သော", "nokilesa": f"{_K} မဟုတ်သော"},
    "kil2": {"saṃkilesika": f"{_K}၏ အာရုံ ဖြစ်နိုင်သော", "asaṃkilesika": f"{_K}၏ အာရုံ မဖြစ်နိုင်သော"},
    "kilS": {"saṃkiliṭṭha": f"{_K}ဖြင့် ညစ်နွမ်းသော", "asaṃkiliṭṭha": f"{_K}ဖြင့် မညစ်နွမ်းသော"},
    "kilP": {"kilesasampayutta": f"{_K}နှင့် ယှဉ်တွဲသော", "kilesavippayutta": f"{_K}နှင့် ကင်းကွာသော"},
    "kil4": {"kilesa ceva saṃkilesika": f"{_K}လည်း ဖြစ်၊ {_K}၏ အာရုံလည်း ဖြစ်နိုင်သော",
             "saṃkilesika ceva no ca kilesa": f"{_K}၏ အာရုံ ဖြစ်နိုင်သော်လည်း {_K} မဟုတ်သော"},
    "kilB": {"kilesa ceva saṃkiliṭṭha": f"{_K}လည်း ဖြစ်၊ {_K}ဖြင့်လည်း ညစ်နွမ်းသော",
             "saṃkiliṭṭha ceva no ca kilesa": f"{_K}ဖြင့် ညစ်နွမ်းသော်လည်း {_K} မဟုတ်သော"},
    "kil5": {"kilesa ceva kilesasampayutta": f"{_K}လည်း ဖြစ်၊ {_K}နှင့်လည်း ယှဉ်တွဲသော",
             "kilesasampayutta ceva no ca kilesa": f"{_K}နှင့် ယှဉ်တွဲသော်လည်း {_K} မဟုတ်သော"},
    "kil6": {"kilesavippayutta saṃkilesika": f"{_K}နှင့် ကင်းကွာသော်လည်း {_K}၏ အာရုံ ဖြစ်နိုင်သော",
             "kilesavippayutta asaṃkilesika": f"{_K}နှင့် ကင်းကွာ၊ {_K}၏ အာရုံ မဖြစ်နိုင်သော"},
    "dass": {"dassanena pahātabba": "သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့်",
             "nadassanena pahātabba": "သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည် မဟုတ်သော"},
    "bhav": {"bhāvanāya pahātabba": "ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ရမည့်",
             "nabhāvanāya pahātabba": "ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ရမည် မဟုတ်သော"},
    "dassh": {"dassanena pahātabbahetuka": "သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် အမြစ် ရှိသော",
              "nadassanena pahātabbahetuka": "သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် အမြစ် ရှိသည် မဟုတ်သော"},
    "bhavh": {"bhāvanāya pahātabbahetuka": "ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ရမည့် အမြစ် ရှိသော",
              "nabhāvanāya pahātabbahetuka": "ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ရမည့် အမြစ် ရှိသည် မဟုတ်သော"},
    "vitakka": {"savitakka": "စတင်ကြံစည်မှု ရှိသော", "avitakka": "စတင်ကြံစည်မှု မရှိသော"},
    "vicara": {"savicāra": "ဆက်လက်သုံးသပ်မှု ရှိသော", "avicāra": "ဆက်လက်သုံးသပ်မှု မရှိသော"},
    "sappitika": {"sappītika": "ပီတိ ရှိသော", "appītika": "ပီတိ မရှိသော"},
    "piti": {"pītisahagata": "ပီတိနှင့်အတူ ဖြစ်သော", "napītisahagata": "ပီတိနှင့်အတူ ဖြစ်သည် မဟုတ်သော"},
    "sukha": {"sukhasahagata": "သာယာမှုနှင့်အတူ ဖြစ်သော", "nasukhasahagata": "သာယာမှုနှင့်အတူ ဖြစ်သည် မဟုတ်သော"},
    "upekkha": {"upekkhāsahagata": "ဥပေက္ခာနှင့်အတူ ဖြစ်သော",
                "naupekkhāsahagata": "ဥပေက္ခာနှင့်အတူ ဖြစ်သည် မဟုတ်သော"},
    "kama": {"kāmāvacara": "ကာမဘုံနှင့် ဆိုင်သော", "nakāmāvacara": "ကာမဘုံနှင့် ဆိုင်သည် မဟုတ်သော"},
    "rupa": {"rūpāvacara": "သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော", "narūpāvacara": "သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သည် မဟုတ်သော"},
    "arupa": {"arūpāvacara": "ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော", "naarūpāvacara": "ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သည် မဟုတ်သော"},
    "pariyapanna": {"pariyāpanna": "ဘဝဘုံတို့၌ အကျုံးဝင်သော", "apariyāpanna": "ဘဝဘုံတို့၌ အကျုံးမဝင်သော"},
    "niyyanika": {"niyyānika": "လွတ်မြောက်ရာသို့ ပို့ဆောင်သော", "aniyyānika": "လွတ်မြောက်ရာသို့ မပို့ဆောင်သော"},
    "niyata": {"niyata": "ကျိန်းသေသော", "aniyata": "မကျိန်းသေသော"},
    "sauttara": {"sauttara": "ထိုထက် သာလွန်သည် ရှိသေးသော", "anuttara": "ထိုထက် သာလွန်သည် မရှိသော"},
    "sarana": {"saraṇa": "ပဋိပက္ခ ရှိသော", "araṇa": "ပဋိပက္ခ မရှိသော"},
}
_E = r"(?:o|aṃ|assa|ā|ānaṃ|añca|e)"
_ND = r"(?!aduk)\w*"                          # not a dyad name («savitakkadukaṃ»)


def _cap(w):
    return f"[{w[0].upper()}{w[0]}]" + w[1:]


# Pāli regexes of the terms of each dyad (raw Pāli, variants removed), longer forms first
TERM_PI = {
    "kil1": [(r"[Kk]iles" + _E + r"(?= (?:ca )?(?:[Nn]okiles\w*(?: ca)? )?(?:dhamm|hetū?(?!\w)))|[Kk]ilesādhipati",
              "kilesa"), (r"[Nn]okiles\w*", "nokilesa")],
    "kil2": [(r"[Aa]saṃkilesik\w*", "asaṃkilesika"), (r"[Ss]aṃkilesik" + _ND, "saṃkilesika")],
    "kilS": [(r"[Aa]saṃkiliṭṭh\w*", "asaṃkiliṭṭha"), (r"[Ss]aṃkiliṭṭh" + _ND, "saṃkiliṭṭha")],
    "kilP": [(r"[Kk]ilesasampayutt" + _ND, "kilesasampayutta"), (r"[Kk]ilesavippayutt\w*", "kilesavippayutta")],
    "kil4": [(r"[Kk]iles\w*?(?:ñceva| ceva) saṃkilesik\w*?(?:ñca| ca(?!\w))", "kilesa ceva saṃkilesika"),
             (r"[Ss]aṃkilesik\w*?(?:ñceva| ceva) no ca kiles\w*", "saṃkilesika ceva no ca kilesa")],
    "kilB": [(r"[Kk]iles\w*?(?:ñceva| ceva) saṃkiliṭṭh\w*?(?:ñca| ca(?!\w))", "kilesa ceva saṃkiliṭṭha"),
             (r"[Ss]aṃkiliṭṭh\w*?(?:ñceva| ceva) no ca kiles\w*", "saṃkiliṭṭha ceva no ca kilesa")],
    "kil5": [(r"[Kk]iles\w*?(?:ñceva| ceva) kilesasampayutt\w*?(?:ñca| ca(?!\w))", "kilesa ceva kilesasampayutta"),
             (r"[Kk]ilesasampayutt\w*?(?:ñceva| ceva) no ca kiles\w*", "kilesasampayutta ceva no ca kilesa")],
    "kil6": [(r"[Kk]ilesavippayutt\w* asaṃkilesik\w*", "kilesavippayutta asaṃkilesika"),
             (r"[Kk]ilesavippayutt\w* saṃkilesik\w*", "kilesavippayutta saṃkilesika")],
}
_PLAIN = {  # dyad -> [(stem regex, key)] for the piṭṭhiduka (a term is any form of its stem; not a dyad name)
    "dass": [("[Nn]adassanena pahātabb", "nadassanena pahātabba"), ("[Dd]assanena pahātabb", "dassanena pahātabba")],
    "bhav": [("[Nn]abhāvanāya pahātabb", "nabhāvanāya pahātabba"), ("[Bb]hāvanāya pahātabb", "bhāvanāya pahātabba")],
    "dassh": [("[Nn]adassanena pahātabbahetuk", "nadassanena pahātabbahetuka"),
              ("[Dd]assanena pahātabbahetuk", "dassanena pahātabbahetuka")],
    "bhavh": [("[Nn]abhāvanāya pahātabbahetuk", "nabhāvanāya pahātabbahetuka"),
              ("[Bb]hāvanāya pahātabbahetuk", "bhāvanāya pahātabbahetuka")],
    "vitakka": [("[Ss]avitakk", "savitakka"), ("[Aa]vitakk", "avitakka")],
    "vicara": [("[Ss]avicār", "savicāra"), ("[Aa]vicār", "avicāra")],
    "sappitika": [("[Ss]appītik", "sappītika"), ("[Aa]ppītik", "appītika")],
    "piti": [("[Nn]apītisahagat", "napītisahagata"), ("[Pp]ītisahagat", "pītisahagata")],
    "sukha": [("[Nn]asukhasahagat", "nasukhasahagata"), ("[Ss]ukhasahagat", "sukhasahagata")],
    "upekkha": [("[Nn]aupekkhāsahagat", "naupekkhāsahagata"), ("[Uu]pekkhāsahagat", "upekkhāsahagata")],
    "kama": [("[Nn]akāmāvacar", "nakāmāvacara"), ("[Kk]āmāvacar", "kāmāvacara")],
    "rupa": [("[Nn]arūpāvacar", "narūpāvacara"), ("[Rr]ūpāvacar", "rūpāvacara")],
    "arupa": [("[Nn]aarūpāvacar", "naarūpāvacara"), ("[Aa]rūpāvacar", "arūpāvacara")],
    "pariyapanna": [("[Aa]pariyāpann", "apariyāpanna"), ("[Pp]ariyāpann", "pariyāpanna")],
    "niyyanika": [("[Aa]niyyānik", "aniyyānika"), ("[Nn]iyyānik", "niyyānika")],
    "niyata": [("[Aa]niyat", "aniyata"), ("[Nn]iyat", "niyata")],
    "sauttara": [("[Ss]auttar", "sauttara"), ("[Aa]nuttar", "anuttara")],
    "sarana": [("[Ss]araṇ", "saraṇa"), ("[Aa]raṇ", "araṇa")],
}
for _d, _rx in _PLAIN.items():
    TERM_PI[_d] = [(st + _ND, k) for st, k in _rx]
# the dyads whose terms are named in each other's parts (a sentence or note of a sister dyad): a line is read with the
# terms of its whole family (Pāli and Burmese alike)
FAMILY = [("dass", "bhav", "dassh", "bhavh"), ("vitakka", "vicara"), ("sappitika", "piti", "sukha", "upekkha"),
          ("kama", "rupa", "arupa")]
FAM = {d: f for f in FAMILY for d in f}
assert all(k in TERMS_MY[d] for d, rxs in TERM_PI.items() for _, k in rxs)
# Burmese strings that contain a term value but are not that term (masked before the term count)
MY_MASK = ["မှားယွင်းမှု၌ ကျိန်းသေသော"]                                # micchattaniyata (2-10)
# dyad names (headings, colophons, inside notes): Pāli stem -> Burmese (NEW names, typed here again)
_AR, _KS = "၏ အာရုံ ဖြစ်နိုင်ခြင်း", "ဖြင့် ညစ်နွမ်းခြင်း"
_DN = "နှစ်မျိုးတွဲ"
NAMES_MY = {"lokiyaduk": f"လောကနှင့် သက်ဆိုင်ခြင်း {_DN}",
            "kilesaduk": f"{_K} {_DN}", "saṃkilesikaduk": f"{_K}{_AR} {_DN}", "saṃkiliṭṭhaduk": f"{_K}{_KS} {_DN}",
            "kilesasampayuttaduk": f"{_K}နှင့် ယှဉ်တွဲခြင်း {_DN}",
            "kilesasaṃkilesikaduk": f"{_K} ဖြစ်ခြင်းနှင့် {_K}{_AR} {_DN}",
            "kilesasaṃkiliṭṭhaduk": f"{_K} ဖြစ်ခြင်းနှင့် {_K}{_KS} {_DN}",
            "kilesakilesasampayuttaduk": f"{_K} ဖြစ်ခြင်းနှင့် {_K}နှင့် ယှဉ်တွဲခြင်း {_DN}",
            "kilesavippayuttasaṃkilesikaduk": f"{_K}နှင့် ကင်းကွာခြင်းနှင့် {_K}{_AR} {_DN}",
            "dassanenapahātabbaduk": f"သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ခြင်း {_DN}",
            "bhāvanāyapahātabbaduk": f"ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ခြင်း {_DN}",
            "dassanenapahātabbahetukaduk": f"သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် အမြစ် {_DN}",
            "bhāvanāyapahātabbahetukaduk": f"ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ရမည့် အမြစ် {_DN}",
            "savitakkaduk": f"စတင်ကြံစည်မှု ရှိခြင်း {_DN}", "savicāraduk": f"ဆက်လက်သုံးသပ်မှု ရှိခြင်း {_DN}",
            "sappītikaduk": f"ပီတိ ရှိခြင်း {_DN}", "pītisahagataduk": f"ပီတိနှင့်အတူ ဖြစ်ခြင်း {_DN}",
            "sukhasahagataduk": f"သာယာမှုနှင့်အတူ ဖြစ်ခြင်း {_DN}",
            "upekkhāsahagataduk": f"ဥပေက္ခာနှင့်အတူ ဖြစ်ခြင်း {_DN}",
            "kāmāvacaraduk": f"ကာမဘုံနှင့် ဆိုင်ခြင်း {_DN}", "rūpāvacaraduk": f"သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်ခြင်း {_DN}",
            "arūpāvacaraduk": f"ရုပ်မရှိသော ဘုံနှင့် ဆိုင်ခြင်း {_DN}",
            "pariyāpannaduk": f"ဘဝဘုံတို့၌ အကျုံးဝင်ခြင်း {_DN}",
            "niyyānikaduk": f"လွတ်မြောက်ရာသို့ ပို့ဆောင်ခြင်း {_DN}", "niyataduk": f"ကျိန်းသေခြင်း {_DN}",
            "sauttaraduk": f"ထိုထက် သာလွန်သည် ရှိခြင်း {_DN}", "saraṇaduk": f"ပဋိပက္ခ ရှိခြင်း {_DN}",
            # as written inside the notes: «dassanaduka» (the dassanena pahātabba dyad), «arūpaduka»
            "dassanaduk": f"သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ခြင်း {_DN}", "arūpaduk": f"ရုပ်မရှိသော ဘုံ {_DN}"}
# names written with a space or before a compound member (regex -> NAMES_MY key)
NAME_REF = {r"dassanena pahātabbahetukaduk(?=a)": "dassanenapahātabbahetukaduk",
            r"sappītikaduk(?=apaccayavāra)": "sappītikaduk"}
_DUKA_HEAD = ["Kilesadukaṃ", "Saṃkilesikadukaṃ", "Saṃkiliṭṭhadukaṃ", "Kilesasampayuttadukaṃ", "Kilesasaṃkilesikadukaṃ",
              "Kilesasaṃkiliṭṭhadukaṃ", "Kilesakilesasampayuttadukaṃ", "Kilesavippayuttasaṃkilesikadukaṃ",
              "Dassanenapahātabbadukaṃ", "Bhāvanāyapahātabbadukaṃ", "Dassanenapahātabbahetukadukaṃ",
              "Bhāvanāyapahātabbahetukadukaṃ", "Savitakkadukaṃ", "Savicāradukaṃ", "Sappītikadukaṃ", "Pītisahagatadukaṃ",
              "Sukhasahagatadukaṃ", "Upekkhāsahagatadukaṃ", "Kāmāvacaradukaṃ", "Rūpāvacaradukaṃ", "Arūpāvacaradukaṃ",
              "Pariyāpannadukaṃ", "Niyyānikadukaṃ", "Niyatadukaṃ", "Sauttaradukaṃ", "Saraṇadukaṃ"]
DYAD_HEAD = dict(zip(_DUKA_HEAD, ["kil1", "kil2", "kilS", "kilP", "kil4", "kilB", "kil5", "kil6", "dass", "bhav",
                                  "dassh", "bhavh", "vitakka", "vicara", "sappitika", "piti", "sukha", "upekkha",
                                  "kama", "rupa", "arupa", "pariyapanna", "niyyanika", "niyata", "sauttara", "sarana"]))
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
            # 3-07 … 3-10 notes: «tīsu (padesu)», «catūsupi», «ekaṃyeva»
            "tīsu": 3, "catūsupi": 4, "ekaṃyeva": 1,
            # 4-01 notes: «pañcapi» «ငါးခုလုံး», «tīṇiyeva» «သုံးခုသာ»
            "pañcapi": 5, "tīṇiyeva": 3}
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
# 3-07 … 3-10: the heading «X-Y» without a hyphen and the notes whose conditions stand in another order in Burmese
NOTE_PAIRS.update({
    "*Pacchājātāsevanapaccayā*": ("*နောက်မှ ဖြစ်ပေါ်ခြင်းဟူသော အကြောင်းနှင့် အလေ့အကျင့် ပြုခြင်းဟူသော အကြောင်း*",
                                  [("pacchājāta", False), ("āsevana", False)]),
    "(Ārammaṇasadisā adhipatipaccayā, purejātampi ārammaṇasadisaṃ. Upanissayepi":
        ("(အကြီးအမှူးဟူသော အကြောင်းတို့သည် အာရုံနှင့် တူကြသည်၊ ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်းသည်လည်း အာရုံနှင့် တူသည်။ "
         "အားကြီးသော အမှီဟူသော အကြောင်း၌လည်း",
         [("adhipati", False), ("ārammaṇa", False), ("ārammaṇa", False), ("upanissaya", False)]),
    "(ārammaṇe noupādānamūlake": ("(အာရုံဟူသော အကြောင်း၌ စွဲလမ်းမှု မဟုတ်သော သဘောတရားကို အခြေခံခြင်း၌",
                                  [("ārammaṇa", False)]),
})
NOTE_PAIRS.update({
    "4-5. Nissaya-saṃsaṭṭhavāro": (f"4-5. {_V['nissaya']}နှင့် {_V['saṃsaṭṭha']}", []),
    "(evaṃ nahetupañhā cattāri kātabbā.)": ("(ဤသို့ အမြစ်ဟူသော အကြောင်း မဟုတ်ခြင်း၏ ပြဿနာ လေးခုကို ပြုရမည်။)",
                                            [("hetu", True)]),
    "Upanissaye lokuttaraṃ natthi": ("အားကြီးသော အမှီဟူသော အကြောင်း၌ လောကကို ကျော်လွန်သော သဘောတရား မရှိ",
                                     [("upanissaya", False)]),
    "(Ārammaṇepi adhipatiyāpi sappītikadukasadisā,":
        ("(အာရုံဟူသော အကြောင်း၌လည်း၊ အကြီးအမှူးဟူသော အကြောင်း၌လည်း ပီတိ ရှိခြင်း နှစ်မျိုးတွဲနှင့် တူကြသည်၊",
         [("ārammaṇa", False), ("adhipati", False)]),
})
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
           # 4-01: «no-kilesa», «… ceva no ca kilesa»; the piṭṭhiduka «na-X» terms (one «မဟုတ်» each; the hetuka forms
           # «… အမြစ် ရှိသည် မဟုတ်သော»); arūpa (noun) in the notes
           (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])nokiles", 1), (r"(?<![\wāīūṃṅñṭḍṇḷ])no ca kiles", 1),
           (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])na(?:dassanena|bhāvanāya) pahātabb", 1),
           (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])na(?:pītisahagat|sukhasahagat|upekkhāsahagat|kāmāvacar|rūpāvacar|arūpāvacar)", 1),
           (r"(?i)arūpaṃ(?:yeva)?(?![\wāīūṃṅñṭḍṇḷ])", 1), (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])arūpamissak", 1)]
NEG_MA = [(r"(?i)adukkhamasukh", 2), (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])(?:no)?natthi(?:paccay|yā|\b)", 1),
          (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])(?:no)?avigat", 1), (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])ahetuk", 1), (r"(?i)aniccato", 1),
          (r"(?i)asamm(?:uyh|oh)antena", 1), (r"(?<=vigat)āvigat", 1), (r"na labbhati", 1), (r"(?<![\wāīūṃṅñṭḍṇḷ])na kātabbaṃ", 1), (r"(?i)natthi(?=vigat)", 1),
          (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])arūpe(?![\wāīūṃṅñṭḍṇḷ])", 1), (r"(?i)ākāsānañcāyatan", 1), (r"(?i)viññāṇañcāyatan", 1),
          (r"(?i)ākiñcaññāyatan", 1), (r"(?i)nevasaññānāsaññāyatan", 1),
          (r"(?i)anupādinnupādāniy", 1), (r"(?i)anupādinnaanupādāniy", 2),
          (r"(?i)asaṃkiliṭṭhasaṃkilesik|asaṅkiliṭṭhasaṃkilisik", 1), (r"(?i)asaṃkiliṭṭhaasaṃkilesik", 2),
          (r"(?i)anuppann", 1), (r"(?i)ṭhānāṭhān", 1), (r"\(Avipākaṃ", 1),
          (r"(?i)ninnānaṃ", 1), (r"na likhitā", 1), (r"na samenti", 1),
          # the dyads of 3-07 … 3-10: «a-Y» «… မဖြစ်နိုင်»; the nouns: avijjā «အမှန်ကို မသိမှု»; the notes:
          # «ninnānā(karaṇa)» «… မရှိ», «arūpeyeva», «na kātabbaṃ» «မပြုရ»
          (r"(?i)arūpeyeva", 1), (r"(?i)ninnānākaraṇ|ninnānā(?![\wāīūṃṅñṭḍṇḷ])", 1),
          # 4-01: the «a-» terms (one «မ…» each), the kilesas ahirika «မရှက်», anottappa «မကြောက်ရွံ့», the notes
          # «na kātabbo» «မပြုရ», «na sameti» «မညီ», «arūpa(dukasadisa)» «ရုပ်မရှိသော ဘုံ»
          (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])(?:asaṃkilesik|asaṃkiliṭṭh|avitakk|avicār|appītik|apariyāpann|aniyyānik|aniyat|"
           r"anuttar|araṇ)", 1), (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])(?:ahirik|anottapp)", 1),
          (r"(?<![\wāīūṃṅñṭḍṇḷ])na kātabbo", 1), (r"(?<![\wāīūṃṅñṭḍṇḷ])na sameti", 1),
          (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])arūpaduk", 1), (r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])(?:na)?arūpāvacar", 1)]
MA_MY = re.compile(r"မ(?:နာကျင်|သာယာ|ရှိ|ပျောက်ကွယ်|မြဲ|ရောထွေး|တွေ့ရ|ထည့်ရ|ဖြစ်|ညစ်နွမ်း|ပါဝင်|ရေးထား|ညီ|မြင်|သိ|ပြုရ|"
                   r"ဝင်|ပို့ဆောင်|ကျိန်းသေ|ရှက်|ကြောက်ရွံ့)")


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
    for m in re.finditer(r"(?<![^\s(“*…])(" + NAME_ALT + r")ဟူသော အကြောင်း((?:ကြောင့်)? မဟုတ်|ဖြင့် အကြောင်း ဖြစ်သည် မဟုတ်)?", s):
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
NAME_PI = re.compile(r"(?i)(?<![\wāīūṃṅñṭḍṇḷ])(" + "|".join(sorted(NAMES_MY, key=len, reverse=True)) + r")(?=aṃ|āni|assa|asadis|e(?![\wāīūṃṅñṭḍṇḷ]))")
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


def _fam(d):
    return FAM.get(d, (d,))


ALIAS = {"name:dassanaduk": "name:dassanenapahātabbaduk"}        # one Burmese name for the two Pāli spellings


def pali_terms(line, d):
    return [ALIAS.get(k, k) for k in _pali_terms(line, d)]


def _pali_terms(line, d):
    s = strip_var(ID.sub("", line))
    found = []
    for m in ([] if re.match(r"^#+ \*", s) else NAME_PI.finditer(s)):   # «*Hetudukaṃ*»: the condition pair
        found.append((m.start(), m.end(), "name:" + m.group(1).lower()))
    for k, v in NAME_REF.items():
        for m in re.finditer(k, s):
            if not any(a <= m.start() < b for a, b, _ in found):
                found.append((m.start(), m.end(), "name:" + v))
    rxs = sorted(((rx, key) for dd in _fam(d) for rx, key in TERM_PI[dd]), key=lambda x: -len(x[0]))
    for rx, key in rxs:
        for m in re.finditer(r"(?<![\wāīūṃṅñṭḍṇḷ])(?:" + rx + ")", s):
            if not any(a <= m.start() < b for a, b, _ in found):
                found.append((m.start(), m.end(), key))
    found.sort()
    return [k for _, _, k in found]


def my_terms(line, d):
    vals = dict(_NAME_MY)
    for dd in _fam(d):
        vals.update({v: k for k, v in TERMS_MY[dd].items()})
    rx = re.compile("(" + "|".join(re.escape(v) for v in sorted(vals, key=len, reverse=True)) + ")")
    t = strip_var(ID.sub("", line))
    for mk_ in MY_MASK:
        t = t.replace(mk_, "#" * len(mk_))
    return [ALIAS.get(vals[m.group(1)], vals[m.group(1)]) for m in rx.finditer(t)]


# ----------------------------------------------------------------------------- N: numbers
KH_NOUN = r"(?:khandh|mahābhūt|viññāṇ|upādānā(?![\wāīūṃṅñṭḍṇḷ]))"


def pali_numbers(line):
    s = strip_var(ID.sub("", line))
    s = s.replace("catukkhattuṃ", "catu-khattuṃ")          # «four times» (the verse of 3-07: not a group of four)
    # «tīṇi tīṇi / cattāri cattāri» (N each) = one count «Nခုစီ»; «ekekassa mūle» «… တစ်ခုစီ၌»
    s = re.sub(r"(?<![\wāīūṃṅñṭḍṇḷ])([Tt]īṇi|[Cc]attāri) (?:tīṇi|cattāri)(?![\wāīūṃṅñṭḍṇḷ])", r"\1", s).replace("ekekassa mūle", "ekaṃ mūle")
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
    for m in re.finditer(r"(?i)(pañca|catu) ?viññāṇ", s):
        kh.append((m.start(), 5 if m.group(1).lower() == "pañca" else 4))
    for m in re.finditer(r"(?i)tevīsatipaccayā|catuvīsatipaccayā", s):
        kh.append((m.start(), 23 if m.group(0).lower().startswith("tev") else 24))
    for m in re.finditer(r"tayokhandh", s):                       # source slip «tayokhandhā»
        kh.append((m.start(), 3))
    if "Cha " in s and "nayā" in s:
        kh.append((s.find("Cha "), 6))
    if "ubhopete" in s:                                     # «both of these» «ထိုနှစ်ပါးလုံး» (the verse of 3-07)
        kh.append((s.find("ubhopete"), 2))
    for m in re.finditer(r"(?i)pañcāyatan", s):
        kh.append((m.start(), 5))
    if "saddhāpañcamakesu" in s:
        kh.append((s.find("saddhāpañcamakesu"), 5))
    for m in re.finditer(r"(?i)((?<!ghā)(?<!ajjha)(?<!ajjhat)(?<!mā)(?<!ka)(?<!pī)t?tik|duk)(?=[aāue])|(" + "|".join(GROUP_PI) + r")", s):
        grp.append(3 if m.group(1) and "tik" in m.group(1).lower() else (2 if m.group(1) else GROUP_PI[m.group(2).lower()]))
    for k in NAME_REF:                                    # a dyad named inside a note «… နှစ်မျိုးတွဲ»
        grp += [2] * s.count(k)
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
    spec = importlib.util.spec_from_file_location("make_ch4_01", HERE / "make_ch4-01.py")
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
    for d, tab in mk.DYADS_ADD.items():
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
    mk.D.set_dyad(mk.F, None)
    mk.D.set_dyad(mk.FG, None)
    mk.FG.translate("")
    for n in SAMPLE:
        src = (PALI / n).read_text(encoding="utf-8-sig")
        for label, txt in (("raw", src), ("prep", mk.D.prep(src, None))):
            same = mk.F.translate(txt) == (disk / n).read_text(encoding="utf-8")
            print(f"sample identity {n} ({label}): {'identical' if same else 'DIFFERS'}")
            bad += not same
    return bad


F4 = "4-01-kilesagocchaka.md"
MUT = [  # (file, old, new, what)
    (F4, "အမြစ်ဟူသော အကြောင်း၌ ကိုးခု၊ အာရုံဟူသော", "အမြစ်ဟူသော အကြောင်း၌ ရှစ်ခု၊ အာရုံဟူသော", "count"),
    (F4, "အမြစ်ဟူသော အကြောင်းကြောင့် မဟုတ်ဘဲ ဖြစ်ပေါ်သည်", "အမြစ်ဟူသော အကြောင်းကြောင့် ဖြစ်ပေါ်သည်", "polarity"),
    (F4, "ကိလေသာ ဖြစ်သော သဘောတရားကို မှီ၍ ကိလေသာ မဟုတ်သော သဘောတရားသည်",
     "ကိလေသာ မဟုတ်သော သဘောတရားကို မှီ၍ ကိလေသာ ဖြစ်သော သဘောတရားသည်", "term order"),
    (F4, "အမြစ်ဟူသော အကြောင်းကြောင့် ဖြစ်ပေါ်သည်", "အာရုံဟူသော အကြောင်းကြောင့် ဖြစ်ပေါ်သည်", "condition"),
    (F4, "အစုအဝေး တစ်ပါးကို မှီ၍ အစုအဝေး သုံးပါး", "အစုအဝေး တစ်ပါးကို မှီ၍ အစုအဝေး နှစ်ပါး", "khandha count"),
    (F4, "သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည် မဟုတ်သော အစုအဝေး တစ်ပါးကို", "သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် အစုအဝေး တစ်ပါးကို",
     "term"),
    (F4, "(3) ^7-34-1\n", "(2) ^7-34-1\n", "digits"),
    (F4, "(ရုပ်မရှိသော ဘုံ၌ ဒေါသကို အခြေခံခြင်း မရှိ)", "(ရုပ်မရှိသော ဘုံ၌ ဒေါသကို အခြေခံခြင်း ရှိ)", "note"),
    (F4, "ကိလေသာ၏ အာရုံ ဖြစ်နိုင်ခြင်း နှစ်မျိုးတွဲ ^", "ကိလေသာ နှစ်မျိုးတွဲ ^", "dyad name"),
    (F4, "ကိလေသာနှင့် ကင်းကွာသော်လည်း ကိလေသာ၏ အာရုံ ဖြစ်နိုင်သော", "ကိလေသာနှင့် ကင်းကွာ၊ ကိလေသာ၏ အာရုံ မဖြစ်နိုင်သော",
     "dyad-8 term"),
    (F4, "စတင်ကြံစည်မှု မရှိသော အစုအဝေး", "စတင်ကြံစည်မှု ရှိသော အစုအဝေး", "a- term"),
    (F4, "သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည် မဟုတ်သော သဘောတရားသည် သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည် မဟုတ်သော သဘောတရားအား…",
     "သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် သဘောတရားသည် သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည် မဟုတ်သော သဘောတရားအား…",
     "sister-dyad term"),
]


def mutate():
    tmp = HERE / "chk-mut-ch4-01"
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
        r = subprocess.run([sys.executable, "-I", "-X", "utf8", str(HERE / "check_ch4-01.py"), "--out", str(tmp)],
                           capture_output=True, text=True)
        last = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr[-200:]
        ok = r.returncode != 0
        caught += ok
        print(f"{what:14} -> {'caught' if ok else 'MISSED'} ({last})")
    shutil.rmtree(tmp)
    print(f"{caught} / {len(MUT)} planted errors caught")
    return len(MUT) - caught


def pe_check(names):
    tmp = HERE / "chk-pe" / "ch4-01"
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
