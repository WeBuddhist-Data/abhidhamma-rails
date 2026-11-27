"""Pāli→Burmese keyword mapping for pi-3 (Dhātukathā, «ဓာတ်များအကြောင်း ဆွေးနွေးခြင်း»).
Chapters 7-chatthanayo, 10-navamanayo, 11-dasamanayo (parallel agent; a copy of the approved sample map_all.py:
its tables, compose rules, context functions and verifier unchanged, plus this script's tables T_FRAME / T_CH7 /
T_CH10 / T_CH11 and the rules 7-10-11 M1-M5). Writes only these three chapters and map-table-ch7-10-11.md.

usage (python3 -I -X utf8, from any directory):
  map_ch7-10-11.py       writes <ch>.mapped.md for every chapter in CHAPTERS and map-table-ch7-10-11.md, then verifies them
                         (keyword preservation, presence of every value chunk in its segment, no ", " / «၊» / « / »
                         in a value)
  map_ch7-10-11.py --report    writes nothing; lists unmapped keywords and presence failures
  map_ch7-10-11.py --seg ID..  prints Pāli, Burmese, keywords and mapping (with the source of each value) of segments
  map_ch7-10-11.py --dump CH  (and --pairs: every distinct keyword = value [source])   prints the mapping of every segment of a chapter with the source of each value

Method: a copy (not an import) of the approved pi-2 Burmese mapper (pi-2-my/mapper-my/map_all.py, itself the pi-2
version of pi-1's): tables keyword -> Burmese in dictionary form, per-segment overrides CTX, context functions,
compose rules and the presence verifier (a copy of pi-2's ONE shared presence_check.py). The Burmese is the FINAL
pi-3 text of this track (AI_translation/burmese/pi-3-burmese-plain-zeroshot_split_chapters). No other Burmese
source is used.

Lookup order per keyword:
  CTX[sid] -> the chapter's own table T_<ch> -> the shared tables of the other pi-3 chapters
  -> compose «X dhammā» (rule 5) and the pi-3 pairs (P1-P3 below)
  -> PI2 / PI1: the final pi-2, then pi-1 mapping, the most frequent value of that keyword that is present in THIS
     segment (pi-2 first where they differ; literal presence first, then presence by an ending rule)
  -> the other compose rules.
A value «@name» is a context function f(kw, pali, my).
Adding a chapter: write its table T_<ch> (and CTX entries), register it in SECTIONS, add it to CHAPTERS.
"""
import re, sys, pathlib, collections

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
MY = ROOT / "AI_translation/burmese/pi-3-burmese-plain-zeroshot_split_chapters"
PI = ROOT / "AI_translation/pali/pi-3_split_chapters"
PI1MAP = ROOT / "AI_translation/burmese/pi-1-keywords-by-reference-pali-burmese-plain.md"
PI2MAP = ROOT / "AI_translation/burmese/pi-2-keywords-by-reference-pali-burmese-plain.md"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
LINE = re.compile(r"^\[([^\]]+)\] (.*)$")
NONE = "(no direct equivalent)"
DH = "သဘောတရား"


def low(w):
    return w[:1].lower() + w[1:]


# =====================================================================================================
# chapter tables
# =====================================================================================================
T_PREAMBLE = {
    # pi-1 / pi-2 preamble values (approved samples), unchanged
    "Abhidhamma": "အဘိဓမ္မာ",
    "Abhidhammapiṭake": "အဘိဓမ္မာပိဋက",
    "Namo": "ရှိခိုးသည်",
    "bhagavato": "မြတ်စွာဘုရား",
    "arahato": "ရဟန္တာ",
    "sammāsambuddhassa": "အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရားရှင်",
    "sambuddha": "အမှန်ကို ကိုယ်တိုင် … သိမြင်တော်မူသော ဘုရားရှင်",     # = pi-1 / pi-2 sambuddhassa
    # the pi-3 book title (rule 7: the approved title whole); its members
    "Dhātukathā": "ဓာတ်များအကြောင်း ဆွေးနွေးခြင်း",
    "kathā": "ဆွေးနွေးခြင်း",
    "dhātu": "ဓာတ်",
}
CTX_PREAMBLE = {
    "T-1": {"sammā": "အပြည့်အဝ"},       # the homage (pi-1 / pi-2 preamble value; elsewhere sammā = မှန်ကန်သော)
}

T_UDDESO = {
    # --- headings (the heading's own Burmese, pi-1 decision 4)
    "Uddeso": "အကျဉ်း ဖော်ပြချက်",                          # pi-1
    "mātikā": "ခေါင်းစဉ်စာရင်း",                             # pi-1 / pi-2
    "naya": "ခွဲနည်း", "nayo": "ခွဲနည်း",                     # one word «ခွဲနည်း» (Q1)
    "nayamukha": "ခွဲနည်း၏ တံခါးဝ",
    "abbhantara": "အတွင်း",
    "lakkhaṇa": "လက္ခဏာ",
    "bāhira": "ပြင်ပ", "Bāhiramātikā": "ပြင်ပ ခေါင်းစဉ်စာရင်း",
    # --- the method words (my3-zeroshot-terms «Words of the method names»)
    "saṅgaho": "အကျုံးဝင်ခြင်း", "asaṅgaho": "အကျုံးမဝင်ခြင်း",
    "sampayogo": "ယှဉ်တွဲခြင်း", "vippayogo": "ကင်းကွာခြင်း",
    "saṅgaho asaṅgaho": "အကျုံးဝင်ခြင်း အကျုံးမဝင်ခြင်း",     # «၊» dropped (pi-1 rule 6)
    "saṅgahitaṃ": "အကျုံးဝင်သော", "asaṅgahitaṃ": "အကျုံးမဝင်သော",   # pi-2 saṅgahitaṃ; text «…သည့်အရာ» (N11)
    "sampayuttaṃ": "ယှဉ်တွဲသော", "vippayuttaṃ": "ကင်းကွာသော",        # pi-1 / pi-2; text «…သည့်အရာ» (N11)
    # --- the Abbhantaramātikā (my3-zeroshot-terms topic names, pi-1 / pi-2)
    "khandhā": "အစုအဝေး",
    "dvādasa": "ဆယ့်နှစ်ပါး", "dvādasāyatanāni": "အာရုံခံ နယ်ပယ် ဆယ့်နှစ်ပါး",
    "āyatanāni": "အာရုံခံ နယ်ပယ်",
    "aṭṭhārasa": "ဆယ့်ရှစ်ပါး", "aṭṭhārasa dhātuyo": "ဓာတ် ဆယ့်ရှစ်ပါး", "dhātuyo": "ဓာတ်",
    "saccāni": "သစ္စာ",
    "bāvīsati": "နှစ်ဆယ့်နှစ်ပါး", "indriyāni": "စွမ်းရည်",
    "paṭicca": "အကြောင်းတို့ကို မှီ၍", "samuppādo": "ဖြစ်ပေါ်ပုံ",
    "sati": "သတိ", "upaṭṭhānā": "ပဋ္ဌာန်",                    # pi-2 paṭṭhānā (inside သတိပဋ္ဌာန်)
    "sammā": "မှန်ကန်သော", "padhānā": "ကြိုးပမ်းအားထုတ်ခြင်း",
    "iddhi": "ဣဒ္ဓိ",
    "āyatanāni / pādā": "အာရုံခံ နယ်ပယ် … ပါဒ်",              # P4: both members; pādā = pi-2 «ပါဒ်»
    "jhānāni": "ဈာန်", "appamaññāyo": "အပ္ပမညာ", "balāni": "စွမ်းအား",
    "bodhi": "ဗောဇ္ဈင်", "aṅgā": NONE,                       # bojjhaṅga = one Burmese word (pi-2 ^2-522 aṅgo)
    "ariyo": "အရိယာ", "aṭṭhaṅgiko": "အင်္ဂါ ရှစ်ပါး ရှိသော", "maggo": "မဂ်",
    "phasso": "တွေ့ထိမှု", "vedanā": "ခံစားမှု", "saññā": "မှတ်သိမှု", "cetanā": "စေ့ဆော်မှု", "cittaṃ": "စိတ်",
    "manasikāro": "နှလုံးသွင်းခြင်း",
    # --- Lakkhaṇamātikā
    "visabhāgo": "ကွဲပြားသော သဘော", "sabhāgo": "တူညီသော သဘော",
    "bhāga": "သဘော",                                       # fragment of sabhāgo / visabhāgo (rule 8)
    # --- Bāhiramātikā
    "sabbā": "အားလုံး",
    "dhammasaṅgaṇī": "သဘောတရားများကို စုစည်းရေတွက်ခြင်း",   # pi-1 title
    "saṅgaṇī": "စုစည်းရေတွက်ခြင်း", "dhamma": "သဘောတရား",     # pi-1 [1-0]
    "dhātukathāya": "ဓာတ်များအကြောင်း ဆွေးနွေးခြင်း",         # the title (rule 7), the dative «၏» goes (rule 1)
}

# numbers (instrumental, my3-zeroshot-terms): the count with its classifier «ပါး» (pi-1 harmonise decision 5)
NUM = {
    "eka": "တစ်", "dvi": "နှစ်", "ti": "သုံး", "catu": "လေး", "pañca": "ငါး", "cha": "ခြောက်", "satta": "ခုနစ်",
    "aṭṭha": "ရှစ်", "nava": "ကိုး", "dasa": "ဆယ်", "ekādasa": "ဆယ့်တစ်", "dvādasa": "ဆယ့်နှစ်",
    "terasa": "ဆယ့်သုံး", "cuddasa": "ဆယ့်လေး", "pannarasa": "ဆယ့်ငါး", "soḷasa": "ဆယ့်ခြောက်",
    "sattarasa": "ဆယ့်ခုနစ်", "aṭṭhārasa": "ဆယ့်ရှစ်",
}
NUM_INSTR = {   # instrumental forms -> stem
    "ekena": "eka", "ekāya": "eka", "dvīhi": "dvi", "tīhi": "ti", "catūhi": "catu", "pañcahi": "pañca",
    "chahi": "cha", "sattahi": "satta", "aṭṭhahi": "aṭṭha", "navahi": "nava", "dasahi": "dasa",
    "ekādasahi": "ekādasa", "dvādasahi": "dvādasa", "terasahi": "terasa", "cuddasahi": "cuddasa",
    "pannarasahi": "pannarasa", "soḷasahi": "soḷasa", "sattarasahi": "sattarasa", "aṭṭhārasahi": "aṭṭhārasa",
}
NUM_AYATANA = {   # «N-āyatanehi» compounds -> stem
    "ekenāyatanena": "eka", "dvīhāyatanehi": "dvi", "tīhāyatanehi": "ti", "catūhāyatanehi": "catu",
    "pañcahāyatanehi": "pañca", "chahāyatanehi": "cha", "sattahāyatanehi": "satta", "aṭṭhahāyatanehi": "aṭṭha",
    "navahāyatanehi": "nava", "dasahāyatanehi": "dasa", "ekādasahāyatanehi": "ekādasa",
    "dvādasahāyatanehi": "dvādasa", "dvādasāyatanehi": "dvādasa",
}
KHANDHA = "အစုအဝေး"
AYATANA = "အာရုံခံ နယ်ပယ်"
DHATU = "ဓာတ်"

T_PATHAMA = {
    # --- headings and colophons (the heading's own Burmese, pi-1 decision 4)
    "nayo": "ခွဲနည်း",
    "saṅgaha": "အကျုံးဝင်ခြင်း", "asaṅgaha": "အကျုံးမဝင်ခြင်း",
    "saṅgahāsaṅgaha": "အကျုံးဝင်ခြင်းနှင့် အကျုံးမဝင်ခြင်း",   # the dvandva keeps its «နှင့်» (rule 1: only at the end)
    "niddeso": "အကျယ် ဖော်ပြချက်",                            # pi-1 / pi-2
    "Khandho": KHANDHA, "Āyatanaṃ": AYATANA, "Dhātu": DHATU, "Saccaṃ": "သစ္စာ", "Indriyaṃ": "စွမ်းရည်",
    "paṭicca": "အကြောင်းတို့ကို မှီ၍", "samuppāda": "ဖြစ်ပေါ်ပုံ", "ādi": "စသည်",     # pi-2
    # the colophons «(X-mūlakaṃ.)» = «(X-မျိုးတွဲကို အခြေခံသော ခွဲနည်း။)»; pi-2 N8 mūlakaṃ = «အခြေခံသော»
    "Ekamūlakaṃ": "တစ်မျိုးတွဲကို အခြေခံသော",
    "eka": "တစ်မျိုးတွဲ",                                    # the member of Ekamūlakaṃ, as pi-2 duka / tika
    "duka": "နှစ်မျိုးတွဲ", "tika": "သုံးမျိုးတွဲ", "catukka": "လေးမျိုးတွဲ",          # pi-2
    "Dvādasakaṃ": "ဆယ့်နှစ်မျိုးတွဲ", "Aṭṭhārasakaṃ": "ဆယ့်ရှစ်မျိုးတွဲ",
    # --- the frame (my3-zeroshot-terms «Frames of the first method»)
    "khandhehi": KHANDHA, "khandhena": KHANDHA, "khandho": KHANDHA,
    "āyatanehi": AYATANA, "āyatanena": AYATANA,
    "dhātūhi": DHATU, "dhātuyā": DHATU,
    "saṅgahito": "အကျုံးဝင်သော", "saṅgahitā": "အကျုံးဝင်သော", "saṅgahitaṃ": "အကျုံးဝင်သော",
    "saṅgahitāni": "အကျုံးဝင်သော",
    "asaṅgahito": "အကျုံးမဝင်သော", "asaṅgahitā": "အကျုံးမဝင်သော", "asaṅgahitaṃ": "အကျုံးမဝင်သော",
    "asaṅgahitāni": "အကျုံးမဝင်သော",
    "khandhato": "အစုအဝေး ရေတွက်ရာ",                        # N-a: text «အစုအဝေး ရေတွက်ရာမှ» (ablative မှ goes)
    "asaṅkhataṃ": "ပြုပြင်ဖန်တီးထားခြင်း မရှိသော",             # pi-2; the text's head «သဘောတရား» is not the keyword
    "ṭhapetvā": "ချန်ထား၍",                                  # pi-1 / pi-2
    # --- topic members (fragments of the topic compounds; pi-1 / pi-2 values)
    "cakkhu": "မျက်စိ", "sota": "နား", "ghāna": "နှာခေါင်း", "jivhā": "လျှာ", "kāya": "ကိုယ်", "mana": "မနော",
    "mano": "မနော",
    "sadda": "အသံ", "gandha": "အနံ့", "rasa": "အရသာ", "phoṭṭhabba": "အထိအတွေ့",
    "rūpa": "@rupa",
    "dukkha": "@dukkha", "sukha": "@sukha",
    "itthi": "မိန်းမ", "purisa": "ယောက်ျား", "jīvita": "အသက်",
    "Avijjā": "အမှန်ကို မသိမှု",
    "aññāta": "သိရသော",                    # positive part of anaññāta «မသိရသေးသည်» (rule 8; ending N-b «သေးသည်»)
    "ñassāmi": "သိရတော့သည်",              # rule 4 (verb + «သည်»); text future «သိရတော့မည်» (pi-2 N12 «မည်»)
    "upaṭṭhānaṃ": "ပဋ္ဌာန်",               # as upaṭṭhānā (pi-2 paṭṭhānā, inside သတိပဋ္ဌာန်)
    "dukkhaṃ": "ကိုယ်ဆင်းရဲခြင်း",          # the jāti list (my3 terms, pi-2 ^2-206)
    "pañhā": "မေးခွန်း", "pucchake": "ဖော်ပြချက်",   # the variant note «… မေးခွန်းများဖြင့် ဖော်ပြချက်၌လည်း»
    "pariyāpannā": "ဘဝဘုံတို့၌ အကျုံးဝင်သော",     # pi-2 pariyāpanno (Mātikā value)
    "paṭighā": "ထိခိုက်မှု",                # fragment of sappaṭighā (rule 2: the noun it rests on)
    "vokāra": "အစုအဝေး",                    # X-vokārabhavo «အစုအဝေး N-ပါး ရှိသော ဘဝ» (pi-2 ^2-234)
    "avitakka": "စတင်ကြံစည်မှု မရှိသော", "savitakka": "စတင်ကြံစည်မှု ရှိသော",     # pi-1 avitakkā / savitakkā
    "citta anuparivattino": "စိတ်နောက်သို့ လိုက်ပါသော",   # = pi-1 cittānuparivattino (the text's one word)
    "Bahiddhā": "မိမိ၏ ပြင်ပ၌", "bahiddhā": "မိမိ၏ ပြင်ပ၌",     # pi-2 N10 (adverb, locative kept)
    "Bahiddhā dhammā": "မိမိ၏ ပြင်ပ၌ ရှိသော သဘောတရား",       # pi-2 N10 adjective «… ရှိသော» + rule 5
}
CTX_PATHAMA = {
    # «no cittasaṃsaṭṭhasamuṭṭhānā dhammā» = «စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာသည် မဟုတ်သော သဘောတရား»: the
    # fragment's qualifier (rule 3, «၍» -> «သော»), the negative and the head noun after the gap
    "3-146": {"no saṃsaṭṭha dhammā": "ရောနှောသော … မဟုတ်သော သဘောတရား"},
}

# the neuter -aṃ and plural -ā / -āni forms of the predicate (inflected forms keep one value)

SHARED_TABLES = [T_PREAMBLE, T_UDDESO, T_PATHAMA]


def first_compound(pali, stems):
    """the first of the stems that occurs in the Pāli segment (word-start match), by position."""
    best = None
    for st, val in stems:
        for m in re.finditer(r"(?<![\wāīūṃṅñṭḍṇḷ])" + st, pali, flags=re.I):
            if best is None or m.start() < best[0]:
                best = (m.start(), val)
            break
    return best[1] if best else None


def f_rupa(kw, pali, my):
    """rūpa, one sense per segment (pi-1 harmonise decision 3): the sense of the FIRST rūpa compound of the Pāli
    segment (a-rūpa compounds are skipped, they carry the keyword arūpa): rūpāvacara / rūpabhava = the
    fine-material plane «သိမ်မွေ့သော ရုပ်», rūpāyatana / rūpadhātu = the visible object «အဆင်းအရောင်», matter
    «ရုပ်» elsewhere."""
    m = re.search(r"(?<![\wā])[Rr]ūp([aā]\w*)", pali)
    if m:
        rest = m.group(1)
        if rest.startswith(("āvacar", "abhav")):
            return "သိမ်မွေ့သော ရုပ်"
        if rest.startswith(("āyatana", "adhātu")):
            return "အဆင်းအရောင်"
    return "ရုပ်"


def f_dukkha(kw, pali, my):
    """dukkha, one sense per segment, by its first compound: the truth «ဒုက္ခ» (dukkhasacca), the faculty /
    feeling «နာကျင်မှု» (dukkhindriya), the painful feeling «နာကျင်သော» (dukkhāya vedanāya)."""
    v = first_compound(pali, [("adukkhamasukh", "နာကျင်"), ("dukkhasacc", "ဒုက္ခ"), ("dukkhindriy", "နာကျင်မှု"), ("dukkhāya", "နာကျင်သော"),
                              ("dukkhaṃ", "ကိုယ်ဆင်းရဲခြင်း")])
    return v or "ဒုက္ခ"


def f_sukha(kw, pali, my):
    """sukha, one sense per segment, by its first compound: the faculty / the accompanying feeling «သာယာမှု»
    (sukhindriya, sukhasahagata), the pleasant feeling «သာယာသော» (sukhāya vedanāya)."""
    v = first_compound(pali, [("sukhindriy", "သာယာမှု"), ("sukhasahagat", "သာယာမှု"), ("sukhāya", "သာယာသော")])
    return v or "သာယာမှု"


FUNCS = {"rupa": f_rupa, "dukkha": f_dukkha, "sukha": f_sukha}
CTX = {}
CTX.update(CTX_PREAMBLE)
CTX.update(CTX_PATHAMA)

# =====================================================================================================
# chapters 7-chatthanayo, 10-navamanayo, 11-dasamanayo (this script's own tables)
# =====================================================================================================
# the frame words and the summary verses, shared by the three chapters (ch7 and ch11 have the same verse)
T_FRAME = {
    "kehici": "အချို့",                         # «… တို့၏ အချို့နှင့်» (with some of): the noun, «၏ … နှင့်» go (rule 1)
    "sampayutta": "ယှဉ်တွဲသော", "vippayutta": "ကင်းကွာသော",        # heading members (pi-1 / pi-2)
    "vippayoga": "ကင်းကွာခြင်း",                 # = the sample's vippayogo (heading, colophon)
    # the relative frame «X-ena ye dhammā vippayuttā, tehi dhammehi ye dhammā vippayuttā» (7-10-11 M2)
    "dhammā vippayuttā": "ကင်းကွာသော သဘောတရား",          # «ye dhammā vippayuttā» (pi-1 dhammā saṅkhatā order)
    "dhammehi vippayuttā": "သဘောတရား … ကင်းကွာသော",   # «tehi dhammehi ye dhammā vippayuttā» (gap «တို့နှင့်», = ch12-15 Q2)
    # ordinals of the headings and colophons (pi-2 chaṭṭho = ဆဋ္ဌမ)
    "chaṭṭha": "ဆဋ္ဌမ", "navama": "နဝမ", "Navamassa": "နဝမ", "dasama": "ဒသမ", "dasamo": "ဒသမ",
    # the summary verses (my3 harmonise B5 forms)
    "Gocchakesu": "အစု", "gocchake": "အစု",                   # pi-1 «N-တို့၏ အစု»
    "antare": "ကြားညှပ်",                                     # pi-1 antara
    "duke": "နှစ်မျိုးတွဲ",                                    # pi-2 duka
    "bhavā": "ဘဝ",                    # mahābhavā «ဘဝကြီး»: the noun without ကြီး (pi-1 harmonise 5 bhūtā)
    "labbhati": "တွေ့ရသည်",           # «na labbhati» «မတွေ့ရ»: positive part (rule 8), verb + သည် (rule 4)
    "pare": "နောက်",                  # «tato pare» «ထို့နောက်တွင်»: «ထို့» is tato (7-10-11 M4)
    "upari": "အထက်",                  # «tato upari» «ထို့အထက်တွင်»: as ch4 upari «အထက်» (7-10-11 M4)
    "niddese": "အကျယ် ဖော်ပြချက်",     # rule 1 (the locative «တွင်» goes)
    "saṅgahaṃ gatā": "အကျုံးဝင်သော",    # participle (rule 3; text «အကျုံးဝင်ကြသည်»)
    # the verse counts with their classifier (pi-1 harmonise 5; text «… ပါး»)
    "ekūnavīsati": "ဆယ့်ကိုးပါး", "paññāsa": "ငါးဆယ်ပါး", "Tevīsa": "နှစ်ဆယ့်သုံးပါး",
    "tecattālīsaṃ": "လေးဆယ့်သုံးပါး", "cuddasa": "ဆယ့်လေးပါး",
}
T_CH7 = dict(T_FRAME)
T_CH10 = dict(T_FRAME)
T_CH11 = dict(T_FRAME)
T_CH10.update({
    "upādādhammehi": "မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော သဘောတရား",      # = upādā dhammā (pi-1), one Pāli word
})
T_CH11.update({
    "Adhimokkhena": "ဆုံးဖြတ်မှု",       # the noun of pi-2 adhimokkhapaccayā «ဆုံးဖြတ်မှုကြောင့်» (text «ဆုံးဖြတ်မှုနှင့်»)
    "upādādhammehi": "မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော သဘောတရား",      # = upādā dhammā (pi-1), one Pāli word
})
CTX.update({
    "3-352": {"arūpa": "ရုပ် မဟုတ်သော"},     # Arūpakkhandhā «ရုပ် မဟုတ်သော အစုအဝေး» (pi-1 arūpino), not the plane
})
SHARED_TABLES += [T_CH7, T_CH10, T_CH11]
SECTIONS = {"preamble": T_PREAMBLE, "1-uddeso": T_UDDESO, "2-pathamanayo": T_PATHAMA,
            "7-chatthanayo": T_CH7, "10-navamanayo": T_CH10, "11-dasamanayo": T_CH11}
CHAPTERS = ["7-chatthanayo", "10-navamanayo", "11-dasamanayo"]


# =====================================================================================================
# engine
# =====================================================================================================
def segments(path):
    out, buf = {}, []
    for l in path.read_text(encoding="utf-8-sig").splitlines():
        if not l.strip():
            continue
        buf.append(l)
        m = ID.search(l)
        if m:
            out[m.group(1)] = " ".join(buf)
            buf = []
    return out


def load_map(path):
    d = collections.defaultdict(collections.Counter)
    for l in path.read_text(encoding="utf-8").splitlines():
        m = LINE.match(l)
        if not m:
            continue
        for kv in m.group(2).split(", "):
            if "=" in kv:
                k, v = kv.split("=", 1)
                d[k][v] += 1
    return d


PI1 = load_map(PI1MAP)
PI2 = load_map(PI2MAP)

SHARED = {}
for _t in SHARED_TABLES:
    for _k, _v in _t.items():
        SHARED.setdefault(_k, _v)


def resolve(v, kw, pali, my):
    if v is not None and v.startswith("@"):
        return FUNCS[v[1:]](kw, pali, my)
    return v


def table_get(tab, kw):
    for k in (kw, low(kw), kw[:1].upper() + kw[1:]):
        if k in tab:
            return tab[k]
    return None


def prev_vals(P, kw):
    c = collections.Counter()
    for k in {kw, low(kw), kw[:1].upper() + kw[1:]}:
        c.update(P.get(k, {}))
    return c


def contiguous(v, my):
    """every « … »-part of the value occurs literally as a whole in the text (and a gap is a real gap)."""
    parts = v.split(" … ")
    if not all(p in my for p in parts):
        return False
    return len(parts) == 1 or v.replace(" … ", " ") not in my


def pi_get(kw, my, tiers=("contig", "literal", "rule")):
    """the most frequent pi-2 value (then pi-1) of the keyword present in the segment, by tier: first a value
    whose parts occur contiguously in the text (pi-2, then pi-1), then one whose every chunk is in the text
    literally, then one matched by an ending rule."""
    ranked = [[v for v, _ in prev_vals(P, kw).most_common() if v != NONE] for P in (PI2, PI1)]
    for tier in tiers:
        for tag, vals in zip(("pi2", "pi1"), ranked):
            for v in vals:
                ok, rules = presence(v, my)
                if not ok:
                    continue
                if (tier == "contig" and contiguous(v, my)) or (tier == "literal" and not rules) or tier == "rule":
                    return v, tag
    return None, None


SRC = {}   # (sid, kw) -> source of the value: ctx / table / pi1 / pi2 / compose


# P1: subject + predicate biterms «X saṅgahitā» (the predicate of the frame); P2 «āyatanehi N» / «N dhātūhi»
PRED = {"saṅgahito", "saṅgahitā", "saṅgahitaṃ", "saṅgahitāni"}


def compose_first(ch, sid, kw, pali, my):
    try:
        return _compose_first(ch, sid, kw, pali, my)
    except KeyError:
        return None


def _compose_first(ch, sid, kw, pali, my):
    ws = kw.split()
    if len(ws) < 2:
        return None
    if ws[-1] in PRED or ws[-1] == "ṭhapetvā":
        return lookup(ch, sid, " ".join(ws[:-1]), pali, my) + " … " + lookup(ch, sid, ws[-1], pali, my)
    if len(ws) == 2 and ws[-1] in VERB_PRED and ws[0] not in ("dhammā", "dhammehi"):
        # 7-10-11 M3: «X-ena (ye dhammā) vippayuttā» = «Xနှင့် ကင်းကွာသော» (pi-1 rule 3: the object keeps နှင့်)
        b, vv = lookup(ch, sid, ws[0], pali, my), VERB_PRED[ws[-1]]
        if b + "နှင့် " + vv in my:
            return b + "နှင့် " + vv
        return b + " … " + vv                    # the gap holds «နှင့်» and the other items (rule 10)
    if ws[-1] in ("dhammā", "dhammehi"):
        b = lookup(ch, sid, " ".join(ws[:-1]), pali, my)
        # rule 10: « … » where the head noun does not follow the qualifier in the text (a compound fragment)
        return b + (" " if (b + " " + DH) in my else " … ") + DH
    if len(ws) == 2 and ws[0] == "āyatanehi" and ws[1] in NUM_INSTR:
        return AYATANA + " … " + NUM[NUM_INSTR[ws[1]]] + "ပါး"
    if len(ws) == 2 and ws[1] in ("dhātūhi", "dhātuyā") and ws[0] in NUM_INSTR:
        return DHATU + " " + NUM[NUM_INSTR[ws[0]]] + "ပါး"
    return None


def compose_last(ch, sid, kw, pali, my):
    if kw in NUM_INSTR:
        return NUM[NUM_INSTR[kw]] + "ပါး"
    if kw in NUM_AYATANA:
        return AYATANA + " " + NUM[NUM_AYATANA[kw]] + "ပါး"
    if " / " in kw:                                    # P4: «A / B» = both members, « … » between
        a, b = kw.split(" / ", 1)
        return lookup(ch, sid, a, pali, my) + " … " + lookup(ch, sid, b, pali, my)
    ws = kw.split()
    if ws[0] in ("na", "no") and len(ws) >= 2:         # rule 5: «…သည် မဟုတ်သော»
        b = lookup(ch, sid, " ".join(ws[1:]), pali, my)
        if b.endswith(" " + DH):
            h = b[: -len(DH) - 1]
            return (h[:-3] + "သည် မဟုတ်သော" if h.endswith("သော") else h + " မဟုတ်သော") + " " + DH
        return b[:-3] + "သည် မဟုတ်သော" if b.endswith("သော") else b + " မဟုတ်သော"
    return None


NOM_END = [   # (inflected ending, nominative endings to try): the dictionary form is the same in every case (rule 1)
    ("dhātuyā", ["dhātu"]), ("uyā", ["u"]), ("āya", ["ā"]), ("iyā", ["i"]),
    ("ena", ["o", "aṃ", "a"]), ("ehi", ["ā", "āni", "a"]),
    ("īhi", ["ino", "ī", "i"]), ("ūhi", ["ū", "uno", "u"]), ("ehi", ["e"]),
]


def nom_cands(w):
    out = []
    for e, rs in NOM_END:
        if w.endswith(e) and len(w) > len(e) + 1:
            out += [w[: -len(e)] + r for r in rs]
    return list(dict.fromkeys(out))


def nom_phrases(kw):
    """the keyword with every inflected word put back into its nominative (first candidates)."""
    ws = kw.split()
    cands = [nom_cands(w) or [w] for w in ws]
    out = [" ".join(c[0] for c in cands), " ".join(ws[:-1] + [cands[-1][0]])]    # all words / the last word only
    if len(ws) == 1:
        out = cands[0]
    return [x for x in out if x != kw]


def nom_lookup(ch, sid, kw, pali, my):
    """7-10-11 M1: an instrumental / dative keyword takes the value of its nominative (tables first, then the
    pi-2 / pi-1 mapping), the value present in the segment."""
    cands = nom_phrases(kw)
    for c in cands:
        v = table_get(CTX.get(sid, {}), c)
        if v is None:
            v = table_get(SECTIONS.get(ch, {}), c)
        if v is None:
            v = table_get(SHARED, c)
        if v is not None:
            v = resolve(v, c, pali, my)
            if presence(v, my)[0]:
                return v, "table-nom"
    for c in cands:
        tiers = ("contig",) if c.endswith(" dhammā") else ("contig", "literal", "rule")
        v, tag = pi_get(c, my, tiers=tiers)
        if v is not None:
            return v, tag + "-nom"
    return None, None


VERB_PRED = {"sampayuttā": "ယှဉ်တွဲသော", "vippayuttā": "ကင်းကွာသော"}


def lookup(ch, sid, kw, pali, my):
    v = table_get(CTX.get(sid, {}), kw)
    if v is not None:
        SRC[(sid, kw)] = "ctx"
        return resolve(v, kw, pali, my)
    v = table_get(SECTIONS.get(ch, {}), kw)
    if v is None:
        v = table_get(SHARED, kw)
    if v is not None:
        SRC[(sid, kw)] = "table"
        return resolve(v, kw, pali, my)
    if kw.endswith(" dhammā"):                 # a pi-1 / pi-2 «X dhammā» value that the text has as a phrase
        v, tag = pi_get(kw, my, tiers=("contig",))
        if v is not None:
            SRC[(sid, kw)] = tag
            return v
    if kw.endswith(" dhammehi"):               # 7-10-11 M1: the pi-1 / pi-2 «X dhammā» phrase of the nominative
        for c in nom_phrases(kw):
            v, tag = pi_get(c, my, tiers=("contig",))
            if v is not None:
                SRC[(sid, kw)] = tag + "-nom"
                return v
    v = compose_first(ch, sid, kw, pali, my)
    if v is not None:
        SRC[(sid, kw)] = "compose"
        return v
    v, tag = pi_get(kw, my)
    if v is not None:
        SRC[(sid, kw)] = tag
        return v
    v, tag = nom_lookup(ch, sid, kw, pali, my)
    if v is not None:
        SRC[(sid, kw)] = tag
        return v
    v = compose_last(ch, sid, kw, pali, my)
    if v is not None:
        SRC[(sid, kw)] = "compose"
        return v
    raise KeyError(kw)


# =====================================================================================================
# presence check: a copy of pi-2's ONE shared presence_check.py (pi-2 map-harmonise decision 3), unchanged
# =====================================================================================================
ATTR_FROM = tuple(dict.fromkeys((
    "သော်", "၍", "ပြီး", "သည်", "ခြင်း", "သူ", "ပြီ", "ကြသော", "ဘဲ", "သေးသော", "၊", "သည့်",   # pi-1 / sample N11
    "လျက်", "ကုန်သော", "ကြသည်", "၏", "ကြ၏", "။", "”",                                    # pi-2 12-14 M1
    "ကြ", "ဟူ", "ဟု",                                                                   # pi-2 15-16 P1
    "ကုန်",                                                                             # pi-2 17
    "သနည်း", "ရာ", "သေးသည်",                                                          # pi-3 N-b
)))
VERB_FROM = tuple(dict.fromkeys((
    "ပါ၏", "၏", "ပြီ", "သော", "၍", "ပြီး", "ခြင်း", "ရန်", "သည့်", "ကြ", "၊", "ဟူ", "လိမ့်မည်", "။",  # pi-1
    "ရာ", "”", "သနည်း",                                                                  # pi-2 12-14 M1
    "လျှင်",                                                                            # pi-2 15-16 P5 / P6
    "ပါစေ", "သမျှ", "ဟု", "ကုန်", "အံ့", "လော့", "မည်",                                     # pi-2 17
)))


def chunk_present(c, text):
    """-> rule name ('exact', 'attr', 'verb', 'attr-fut', 'perf-pred', 'neg-verb', 'plural', 'neg-infix',
    'neg-attr') or None."""
    if c in text:
        return "exact"
    if c.endswith("သော") and len(c) > 3:
        st = c[:-3]
        if any(st + e in text for e in ATTR_FROM):
            return "attr"
    if c.endswith("သည်") and len(c) > 3:
        st = c[:-3]
        if any(st + e in text for e in VERB_FROM):
            return "verb"
    if c.endswith("ည့်") and c[:-3] + "ည်" in text:
        return "attr-fut"
    if c.endswith("ပြီးသော") and c[:-3] + " ဖြစ်" in text:
        return "perf-pred"
    if c.endswith("သည်") and len(c) > 3:
        st = c[:-3]
        if "မ" + st in text:
            return "neg-verb"
        for i in range(0, len(st)):
            if any(st[:i] + "မ" + st[i:] + e in text for e in VERB_FROM):
                return "neg-verb"
    for t in ("လိမ့်မည်", "ခဲ့သည်"):
        if c.endswith(t) and c[:-len(t)] + "ကြ" + t.replace("ခဲ့သည်", "ခဲ့") in text.replace("ခဲ့ကြ", "ကြခဲ့"):
            return "plural"
    for i in range(1, len(c)):
        if c[:i] + "မ" + c[i:] in text or c[:i] + " မ" + c[i:] in text:
            return "neg-infix"
    if c.endswith("သော") and len(c) > 3:
        st = c[:-3]
        for i in range(0, len(st)):
            if any((st[:i] + "မ" + st[i:]) + e in text for e in ATTR_FROM):
                return "neg-attr"
    return None


def presence(v, text):
    """-> (ok, [(chunk, rule) for every chunk not found literally])"""
    if v == NONE:
        return True, []
    bare = re.sub("[“”‘’]", "", text)
    rules = []
    for part in re.split(r" … ", v):
        for c in part.split():
            c = c.strip("“”‘’()")
            if not c:
                continue
            r = chunk_present(c, text) or chunk_present(c, bare)
            if r is None:
                return False, [(c, None)]
            if r != "exact":
                rules.append((c, r))
    return True, rules


def load(ch):
    my = segments(MY / f"{ch}.md")
    pa = segments(PI / f"{ch}.md")
    rows = [LINE.match(l).groups() for l in (HERE / f"{ch}.keywords.md").read_text(encoding="utf-8").splitlines()
            if LINE.match(l)]
    return my, pa, rows


def run(write=True):
    table = collections.defaultdict(collections.Counter)
    unmapped = collections.defaultdict(list)
    problems, summary = [], []
    for ch in CHAPTERS:
        my, pa, rows = load(ch)
        lines, nne = [], 0
        for sid, kws in rows:
            pairs = []
            for kw in [k.strip() for k in kws.split(", ")]:
                try:
                    v = lookup(ch, sid, kw, pa.get(sid, ""), my[sid])
                except KeyError:
                    unmapped[kw].append((ch, sid))
                    v = "?"
                else:
                    ok, _ = presence(v, my[sid])
                    if not ok:
                        problems.append((ch, sid, kw, v))
                pairs.append(f"{kw}={v}")
                table[kw][v] += 1
                nne += v == NONE
            lines.append(f"[{sid}] " + ", ".join(pairs))
        summary.append((ch, len(lines), nne))
        if write and not unmapped:
            (HERE / f"{ch}.mapped.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return table, unmapped, problems, summary


def verify(ch):
    a = [l.split("] ", 1) for l in (HERE / f"{ch}.keywords.md").read_text(encoding="utf-8").splitlines()]
    b = [l.split("] ", 1) for l in (HERE / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines()]
    assert [x[0] for x in a] == [x[0] for x in b]
    bad = [i for (i, x), (_, y) in zip(a, b)
           if [k.strip() for k in x.split(", ")] != [k.split("=", 1)[0] for k in y.split(", ")]]
    my, _, _ = load(ch)
    fails, ruled = [], []
    for (i, x), (_, y) in zip(a, b):
        for kv in y.split(", "):
            k, v = kv.split("=", 1)
            ok, rules = presence(v, my[i[1:]])
            if not ok:
                fails.append((i, k, v))
                continue
            for c, r in rules:
                ruled.append((i[1:], k, c, r))
    punct = [i for (i, x), (_, y) in zip(a, b)
             if any(", " in v or "၊" in v or " / " in v for v in [kv.split("=", 1)[1] for kv in y.split(", ")])
             or y.count("=") != len(x.split(", "))]
    return len(a), bad, fails, punct, ruled


# =====================================================================================================
# rules and reasons (written to map-table.md)
# =====================================================================================================
RULES = """## Rules

The value is the word or phrase of THAT segment's Burmese (the FINAL pi-3 text) that carries the keyword, in the
dictionary form of the approved mappings. **Binding and unchanged:** pi-1 rules 1–11 and the agreed later pi-1 rules,
pi-2 N1–N11 and its harmonise decisions, and the approved pi-3 sample (`map-table.md`, M1–M9, its 11 differences and
its values): this script is a copy of `map_all.py` with the same tables, compose rules, context functions and
presence check; the sample's values are taken for the same keyword in the same kind of segment (sampayutto /
vippayutto «ယှဉ်တွဲသော / ကင်းကွာသော» in every number and gender, the counts with «ပါး», the count biterms
«āyatanehi N» M1, «A / B» M2, «X dhammā» with a gap M4, ñassāmi «သိရတော့သည်», aññāta «သိရသော», bodhi «ဗောဇ္ဈင်» with
aṅgā (no direct equivalent), vokāra, rūpa / dukkha / sukha by the first compound). pi-2 and pi-1 values are reused
where they occur in the segment (pi-2 first).

Rules this run uses that pi-1 / pi-2 / the sample already had, applied to the shapes of the sixth, ninth and tenth
methods:

- **The association frame** «S katihi khandhehi … sampayutto? … X-hi … sampayutto; … kehici sampayutto»:
  sampayutto / -ā / -aṃ = ယှဉ်တွဲသော, vippayutto / -ā / -aṃ = ကင်းကွာသော (pi-1 / pi-2; text «…သည်», «…ကြသည်»,
  «…သနည်း»: rule 3, sample M7); Natthi = မရှိသည် (pi-1 / pi-2; text «မရှိ။», rule 4); the counts and counted nouns
  as in the sample (dasahāyatanehi = အာရုံခံ နယ်ပယ် ဆယ်ပါး, soḷasahi dhātūhi = ဓာတ် ဆယ့်ခြောက်ပါး, āyatanehi dasahi =
  အာရုံခံ နယ်ပယ် … ဆယ်ပါး).
- **Headings and colophons** (rule 7, decision 4): nayo = ခွဲနည်း (sample M8), the ordinals chaṭṭha / chaṭṭho = ဆဋ္ဌမ
  (pi-2), navama / Navamassa = နဝမ, dasama / dasamo = ဒသမ (the text's words); vippayoga = ကင်းကွာခြင်း (= the sample's
  vippayogo); sampayutta / vippayutta in «Sampayuttena sampayutta-» «ယှဉ်တွဲသည့်အရာဖြင့် ယှဉ်တွဲသည့်အရာ» = ယှဉ်တွဲသော /
  ကင်းကွာသော (pi-1 / pi-2, sample N11 «…သည့်အရာ»); niddeso / niddese = အကျယ် ဖော်ပြချက်; ādi = စသည်.
- **The summary verses** (identical in ch7 and ch11): the noun without its locative (rule 1): Gocchakesu / gocchake =
  အစု (pi-1 «N-တို့၏ အစု»), antare / antara = ကြားညှပ် (pi-1), duke = နှစ်မျိုးတွဲ (pi-2), niddese = အကျယ် ဖော်ပြချက်;
  the counts with the text's classifier «ပါး» (pi-1 harmonise decision 5): ekūnavīsati = ဆယ့်ကိုးပါး, paññāsa =
  ငါးဆယ်ပါး, pannarasa, aṭṭhārasa, cuddasa = ဆယ့်လေးပါး, tecattālīsaṃ = လေးဆယ့်သုံးပါး, Tevīsa (Tevīsa padasataṃ «ပုဒ်
  တစ်ရာ့နှစ်ဆယ့်သုံးပါး») = နှစ်ဆယ့်သုံးပါး with sataṃ = တစ်ရာ (pi-2); mahābhavā: bhavā = ဘဝ (the noun without «ကြီး»
  = mahā, as pi-1 harmonise decision 5 bhūtā «မူလဓာတ်» of mahābhūtā); «na labbhati» «မတွေ့ရ»: labbhati = တွေ့ရသည်
  (rule 8 positive part, rule 4 verb + သည်); «saṅgahaṃ gatā» «အကျုံးဝင်ကြသည်» = အကျုံးဝင်သော (rule 3, as the sample's
  saṅgahitā); jīvitaṃ = အသက်, nāmarūpaṃ, dukkhasaccaṃ (pi-2).
- **Sense by context, one sense per segment**: arūpa in Arūpabhavo / arūpāvacarā = ရုပ်မရှိသော (the plane, pi-1 /
  pi-2) but in the ch10 verse «Arūpakkhandhā cattāro» «ရုပ် မဟုတ်သော အစုအဝေး» = ရုပ် မဟုတ်သော (the non-material
  aggregates; pi-1 arūpino «ရုပ် မဟုတ်သော»; ^3-352, CTX); rūpa in Rūpabhavo / rūpāvacarā = သိမ်မွေ့သော ရုပ် (sample);
  dukkha in dukkhasaccaṃ (verse) = ဒုက္ခ, dukkhaṃ / dukkhena in the jāti list = ကိုယ်ဆင်းရဲခြင်း (sample).
- **Fragments** (rule 8): kāmāvacarehi in «Na kāmāvacarehi», pariyāpannehi in apariyāpannehi, uppannehi in
  anuppannehi, saṃsaṭṭhehi in cittavisaṃsaṭṭhehi, ārammaṇehi in anārammaṇehi = the positive part (pi-1 / pi-2 values
  of the nominative, M1 below).
- **Compound members inside one Burmese word** (pi-2 harmonise decision 4): aṅgā (ch7, bojjhaṅgā) and aṅgehi (ch10,
  ch11, bojjhaṅgehi «ဗောဇ္ဈင်») = (no direct equivalent), as the sample's aṅgā: the only (no direct equivalent), one
  per chapter. This is the same split as ch12-15 Q1 (inflected keywords) and ch3-6-8-9 M11.

## NEW rules (for the user's review)

7-10-11 M1. **Inflected keywords take the value of their nominative.** The ninth and tenth methods name every item
    in the instrumental («Vedanākkhandhena ye dhammā…», «Sukhasahagatehi dhammehi ye dhammā…», «Appamaññāya …»,
    «pañcahi indriyehi …»), and the text renders the item with its nominative's Burmese + «နှင့်». The dictionary
    form is the same in every case (rule 1: no case particle, no plural; rule 3 for adjectives), so the script tries
    the nominative of a keyword it has not found (-ena → -o / -aṃ, -ehi → -ā / -āni, -īhi → -ino, -ūhi → -ū / -uno,
    -āya → -ā, -uyā → -u) in the tables and then in the pi-2 / pi-1 mapping, keeping the value only if it occurs
    in the segment; «X dhammehi» first takes the pi-1 / pi-2 phrase of «X dhammā» where the text has it as a phrase
    (hetukehi dhammehi = အမြစ် ရှိသော သဘောတရား), otherwise it is composed as «X dhammā» (rule 5, sample M4:
    avitakka dhammehi = စတင်ကြံစည်မှု မရှိသော … သဘောတရား). Examples: Vedanākkhandhena = ခံစားမှု အစုအဝေး, indriyena =
    စွမ်းရည်, sahagatehi = အတူ ဖြစ်သော, sahagatehi dhammehi = အတူ ဖြစ်သော သဘောတရား, Hetūhi = အမြစ် (rule 2),
    anuparivattīhi = နောက်သို့ လိုက်ပါသော, sahabhūhi = အတူ တည်ရှိသော, rūpīhi = ရုပ် ဖြစ်သော. 231 keyword uses
    (labelled «-nom» in the --pairs listing); no new Burmese value comes from it.
7-10-11 M2. **The relative frame of the tenth method** «X-ena ye dhammā vippayuttā, tehi dhammehi ye dhammā
    vippayuttā» (text «Xနှင့် ကင်းကွာသော သဘောတရားများ၊ ထိုသဘောတရားတို့နှင့် ကင်းကွာသော သဘောတရားများ»):
    dhammā vippayuttā = «ကင်းကွာသော သဘောတရား» (the relative clause «ye dhammā vippayuttā», its first occurrence in
    every segment: the qualifier before the noun, as pi-1 dhammā saṅkhatā «ပြုပြင်ဖန်တီးထားသော သဘောတရား» and pi-2 N3;
    ch8's «dhammā vippayuttā» = «သဘောတရား … ကင်းကွာသော» (ch3-6-8-9 M12) is the subject + predicate frame, another kind
    of segment); dhammehi vippayuttā = «သဘောတရား … ကင်းကွာသော» (the gap holds «တို့နှင့်»; = ch12-15 Q2 for the same
    frame). One value in every segment (rule 10). ch10 has no such biterm keyword.
7-10-11 M3. **Item + verb biterms** «X-ena vippayuttā» (bhavena, viññāṇena, Adhimokkhena, Kusalehi vippayuttā),
    = ch12-15 Q2: «Xနှင့် ကင်းကွာသော» where the text has it contiguous (^3-364 «ဘဝနှင့် ကင်းကွာသော», ^3-368
    «ဆုံးဖြတ်မှုနှင့် ကင်းကွာသော»; the object keeps its «နှင့်», pi-1 rule 3), else «X … ကင်းကွာသော» (^3-362
    viññāṇena, ^3-365 bhavena: other items stand between; ^3-369 Kusalehi «ကုသိုလ် သဘောတရားများနှင့်…»; rule 10).
    Adhimokkhena = «ဆုံးဖြတ်မှု» (the noun of pi-2 adhimokkhapaccayā «ဆုံးဖြတ်မှုကြောင့်»; = ch12-15 Q6).
7-10-11 M4. **«tato pare» / «tato upari»** (verses, text «ထို့နောက်တွင်» / «ထို့အထက်တွင်»): pare = «နောက်», upari =
    «အထက်» («ထို့» is tato, not a keyword; the locative «တွင်» goes, rule 1; = ch4 upari «အထက်»). pi-2 pare
    «သူတစ်ပါး» (others) is another sense and not in the segment. For map-harmonise: ch13 has upari «အထက်တွင်».
7-10-11 M5. **kehici** (in «… ekāya dhātuyā kehici sampayutto», text «… တို့၏ အချို့နှင့်») = «အချို့» (some of):
    the noun, «၏ … နှင့်» are particles (rule 1). «na kehici» segments have no kehici keyword. **upādādhammehi** (one
    Pāli word, upādādhammehi ye dhammā) = «မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော သဘောတရား» (= pi-1 upādā dhammā, rule 5).
"""

REASONS = {
    "antare": "the verse's cūḷantare / mahantare «ကြားညှပ်» (pi-1 antara heading word); pi-2 «အကြား» (between) is not in the segment",
    "arūpa": "^3-352 verse «Arūpakkhandhā» «ရုပ် မဟုတ်သော အစုအဝေး» (the non-material aggregates, pi-1 arūpino «ရုပ် မဟုတ်သော»); the plane keeps «ရုပ်မရှိသော»",
    "pare": "«tato pare» «ထို့နောက်တွင်» = «နောက်» (after; 7-10-11 M4); pi-2 «သူတစ်ပါး» (others) is another sense, not in the segment",
    "paññāsa": "the verse count with the text's classifier «ငါးဆယ်ပါး» (pi-1 harmonise decision 5); pi-2 «ငါးဆယ်» is the bare number, not in this form in the segment",
    "aññāta": "pi-1 «သိသော» is not in the segment: the text renders anaññāta «မသိရသေးသည်ကို», positive part «သိရ» + «သော» (rule 8, M7)",
    "Bahiddhā dhammā": "pi-1 «သူတစ်ပါး၌ …» does not occur: the pi-3 text has the pi-2 term «မိမိ၏ ပြင်ပ၌ ရှိသော» (pi-2 N10)",
    "bodhi": "pi-2 «ဗောဓိ» is not in the segment: the text renders bojjhaṅgā by the one word «ဗောဇ္ဈင်» (aṅgā = no direct equivalent)",
    "dukkha": "fragment of adukkhamasukhāya: the positive part of the text's «မနာကျင်» (rule 8); one sense per segment",
    "dukkhaṃ": "the jāti list (soko … dukkhaṃ … upāyāso): the pi-3 text's word «ကိုယ်ဆင်းရဲခြင်း» (my3 terms, pi-2 ^2-206 rails); pi-2 «နာကျင်မှု / ဒုက္ခ» are not in the segment",
    "hetukā dhammā": "negated pahātabbahetukā («…အမြစ် ရှိသည် မဟုတ်သော သဘောတရား»): the pi-1 phrase is not in the text, gap (M4); the positive segments keep pi-1",
    "nayo": "the pi-3 text's one word «ခွဲနည်း» (M8); pi-1 «နည်း» stands alone in its text",
    "saṅgaha": "the method «inclusion» (text «အကျုံးဝင်ခြင်း»); pi-2 «အကျဉ်းချုပ်» is «summary»",
    "saṅgaho": "the method «inclusion» (text «အကျုံးဝင်ခြင်း»); pi-1 «စုစည်းခြင်း» is the compendium (Rūpasaṅgaho)",
    "vippayogo": "the method «dissociation» (text «ကင်းကွာခြင်း»); pi-2 «ကွေကွင်းရခြင်း» is separation from the loved",
    "āyatanena": "the counted noun «အာရုံခံ နယ်ပယ် N-ပါး» (ekenāyatanena); pi-2 (no direct equivalent) is a compound member inside one Burmese word",
}


def prev_any(kw):
    return prev_vals(PI1, kw) + prev_vals(PI2, kw)


def write_table(table, ruled_all, results):
    total = sum(sum(c.values()) for c in table.values())
    known = [kw for kw in table if prev_any(kw)]
    same = [(kw, v, n) for kw, c in table.items() for v, n in c.items() if v in prev_any(kw)]
    same2 = [x for x in same if x[1] in prev_vals(PI2, x[0])]
    same1 = [x for x in same if x[1] not in prev_vals(PI2, x[0])]
    with open(HERE / "map-table-ch7-10-11.md", "w", encoding="utf-8") as f:
        f.write("# pi-3 Burmese keyword mapping: rules and review table (Dhātukathā «ဓာတ်များအကြောင်း ဆွေးနွေးခြင်း», "
                "chapters " + ", ".join(CHAPTERS) + ")\n\n")
        f.write("Written by map_ch7-10-11.py (a copy of the approved sample map_all.py, parallel agent). Burmese from the FINAL pi-3 text of this track only "
                "(AI_translation/burmese/pi-3-burmese-plain-zeroshot_split_chapters); pi-1 / pi-2 values from "
                "AI_translation/burmese/pi-1- and pi-2-keywords-by-reference-pali-burmese-plain.md. No other Burmese "
                "source.\n\n")
        f.write("## Verification\n\n| chapter | lines | keyword preservation | presence failures | comma / ၊ / « / » "
                "| rule-matched chunks | (no direct equivalent) |\n|---|---|---|---|---|---|---|\n")
        for ch, ln, bad, fails, punct, ruled, nne in results:
            f.write(f"| {ch} | {ln} | bad {bad} | {len(fails)} | {punct} | {len(ruled)} | {nne} |\n")
        f.write(f"\n## Reuse of pi-1 / pi-2\n\n- Keyword uses: {total}; distinct keywords: {len(table)}.\n"
                f"- Keywords that pi-1 or pi-2 also has: {len(known)} distinct; their values taken **unchanged from "
                f"pi-1 / pi-2**: {len(same)} distinct keyword-value pairs, {sum(x[2] for x in same)} uses "
                f"(a pi-2 value: {len(same2)} pairs, {sum(x[2] for x in same2)} uses; a pi-1 value only: "
                f"{len(same1)} pairs, {sum(x[2] for x in same1)} uses).\n"
                f"- Keywords new in pi-3 (in neither mapping): {len(table) - len(known)} distinct.\n\n")
        f.write("### Values that differ from pi-1 / pi-2 for the same keyword\n\n| keyword | pi-3 value (uses) | "
                "pi-2 value(s) | pi-1 value(s) | reason |\n|---|---|---|---|---|\n")
        for kw in sorted(table, key=lambda x: (low(x).lower(), x)):
            pa = prev_any(kw)
            if not pa:
                continue
            for v, n in table[kw].items():
                if v not in pa:
                    f.write(f"| {kw} | {v} ({n}) | "
                            + (" · ".join(f"{x} ({m})" for x, m in prev_vals(PI2, kw).most_common(4)) or "-")
                            + " | " + (" · ".join(f"{x} ({m})" for x, m in prev_vals(PI1, kw).most_common(4)) or "-")
                            + f" | {REASONS.get(kw, 'UNEXPLAINED')} |\n")
        f.write("\n")
        f.write(RULES)
        f.write("\n## Presence: chunks matched by an ending rule (not literally in the segment)\n\n"
                "Every other chunk of every value occurs literally in its segment's Burmese.\n\n"
                "| segment | keyword | chunk | rule |\n|---|---|---|---|\n")
        for sid, k, c, r in ruled_all:
            f.write(f"| {sid} | {k} | {c} | {r} |\n")
        f.write("\n## Keyword → Burmese (uses)\n\n«pi-2» / «pi-1» = the value is a pi-2 / pi-1 value of the same "
                "keyword. Several values = the keyword reads differently by context.\n\n"
                "| Pāli keyword | Burmese (uses) |\n|---|---|\n")
        for kw in sorted(table, key=lambda x: (low(x).lower(), x)):
            p1, p2 = prev_vals(PI1, kw), prev_vals(PI2, kw)
            f.write(f"| {kw} | " + " · ".join(
                f"{v} ({n}{', pi-2' if v in p2 else (', pi-1' if v in p1 else '')})"
                for v, n in table[kw].most_common()) + " |\n")


def show(sids, pali=True):
    for ch in CHAPTERS:
        my, pa, rows = load(ch)
        R = dict(rows)
        for sid in sids:
            if sid not in R:
                continue
            print("==", sid)
            if pali:
                print(pa.get(sid))
            print(my[sid])
            out = []
            for kw in [k.strip() for k in R[sid].split(", ")]:
                try:
                    v = lookup(ch, sid, kw, pa.get(sid, ""), my[sid])
                    ok = presence(v, my[sid])[0]
                    out.append(f"{kw}={v}[{SRC[(sid, kw)]}{'' if ok else ' FAIL'}]")
                except KeyError:
                    out.append(f"{kw}=??")
            print(" | ".join(out))


def dump(ch):
    my, pa, rows = load(ch)
    for sid, kws in rows:
        out = []
        for kw in [k.strip() for k in kws.split(", ")]:
            try:
                v = lookup(ch, sid, kw, pa.get(sid, ""), my[sid])
                ok = presence(v, my[sid])[0]
                out.append(f"{kw}={v}[{SRC[(sid, kw)]}{'' if ok else ' FAIL'}]")
            except KeyError:
                out.append(f"{kw}=??")
        print(f"[{sid}] " + " | ".join(out))


if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "--seg":
        show(args[1:])
        sys.exit()
    if args and args[0] == "--dump":
        dump(args[1])
        sys.exit()
    if args and args[0] == "--pairs":           # distinct keyword = value [source] (uses, first segment)
        agg = collections.OrderedDict()
        for ch in CHAPTERS:
            my, pa, rows = load(ch)
            for sid, kws in rows:
                for kw in [k.strip() for k in kws.split(", ")]:
                    try:
                        v = lookup(ch, sid, kw, pa.get(sid, ""), my[sid])
                        key = (kw, v, SRC[(sid, kw)])
                    except KeyError:
                        key = (kw, "??", "-")
                    agg.setdefault(key, []).append(sid)
        for (kw, v, src), w in sorted(agg.items(), key=lambda x: (low(x[0][0]).lower(), x[0][1])):
            print(f"{kw} = {v} [{src}] ({len(w)}; {w[0]})")
        sys.exit()
    if args and args[0] == "--report":
        table, unmapped, problems, summary = run(write=False)
        print(f"UNMAPPED keywords: {len(unmapped)} distinct, {sum(len(v) for v in unmapped.values())} uses")
        for kw, where in sorted(unmapped.items(), key=lambda x: -len(x[1])):
            print(f"  {kw}\t{len(where)}\t{where[0][1]}")
        print(f"presence problems: {len(problems)}")
        for ch, sid, kw, v in problems:
            print(f"  {sid}\t{kw} = {v}")
        sys.exit()
    table, unmapped, problems, summary = run(write=True)
    if unmapped or problems:
        print("UNMAPPED", dict(unmapped), "PROBLEMS", problems)
        sys.exit(1)
    ruled_all, results = [], []
    for ch, n, nne in summary:
        ln, bad, fails, punct, ruled = verify(ch)
        ruled_all += ruled
        results.append((ch, ln, bad, fails, punct, ruled, nne))
    write_table(table, ruled_all, results)
    for ch, ln, bad, fails, punct, ruled, nne in results:
        print(f"{ch}: lines {ln} | keyword preservation bad {bad} | presence failures {len(fails)} "
              f"(rule-matched chunks {len(ruled)}) | comma/၊// {punct} | no-equivalent {nne}")
        for f_ in fails:
            print("   FAIL", f_)
    for sid, k, c, r in ruled_all:
        print(f"   rule {r:9} {sid:10} {k} : {c}")
