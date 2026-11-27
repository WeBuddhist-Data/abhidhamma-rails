"""Pāli→Burmese keyword mapping for pi-3 (Dhātukathā, «ဓာတ်များအကြောင်း ဆွေးနွေးခြင်း»).
CHAPTERS 3-dutiyanayo, 4-tatiyanayo, 5-catutthanayo, 6-pancamanayo, 8-sattamanayo, 9-atthamanayo (a parallel
agent's script; the approved sample's tables, compose rules, context functions and verifier are COPIED from
map_all.py, which this script does not import or change). Writes only its own <ch>.mapped.md files and
map-table-ch3-6-8-9.md.

usage (python3 -I -X utf8, from any directory):
  map_ch3-6-8-9.py       writes <ch>.mapped.md for every chapter in CHAPTERS and map-table-ch3-6-8-9.md, then verifies them
                         (keyword preservation, presence of every value chunk in its segment, no ", " / «၊» / « / »
                         in a value)
  map_all.py --report    writes nothing; lists unmapped keywords and presence failures
  map_all.py --seg ID..  prints Pāli, Burmese, keywords and mapping (with the source of each value) of segments
  map_all.py --dump CH   prints the mapping of every segment of a chapter with the source of each value

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

# =====================================================================================================
# THIS AGENT'S chapter tables (3, 4, 5, 6, 8, 9)
# =====================================================================================================
# T_MINE: the instrumental / dative forms of the subjects of the frames «X-ena ye dhammā …» of methods 2-8 (the
# same lemma as the pi-1 / pi-2 / sample value, rule 1: no case particle «နှင့်»); the frame words of the
# saṅgahita / sampayutta methods; the verse words of the colophon verses.
T_MINE = {
    # --- headings and colophons
    "asaṅgahita": "အကျုံးမဝင်သော",               # member of X-asaṅgahita-padaniddeso: «…သည့်အရာ» (N11), = sample asaṅgahitaṃ
    "sampayutta": "ယှဉ်တွဲသော", "vippayutta": "ကင်းကွာသော",    # pi-1 sampayutta; members of the heading compounds
    "pañcama": "ပဉ္စမ", "pañcamo": "ပဉ္စမ", "sattama": "သတ္တမ", "sattamo": "သတ္တမ",
    "aṭṭhama": "အဋ္ဌမ", "aṭṭhamo": "အဋ္ဌမ",          # ordinals (my3-zeroshot-terms)
    # --- the frame (my3-zeroshot-terms «Frames»; sample P1)
    "khandhasaṅgahena": "အစုအဝေး အကျုံးဝင်ခြင်း",     # text «အစုအဝေး အကျုံးဝင်ခြင်းဖြင့်» (instrumental ဖြင့် goes)
    "āyatanasaṅgahena": "အာရုံခံ နယ်ပယ် အကျုံးဝင်ခြင်း",
    "sampayuttā": "ယှဉ်တွဲသော", "vippayuttā": "ကင်းကွာသော",   # pi-1 / pi-2 sampayuttā; the predicate of methods 7-8
    "kehici": "အချို့",                           # M10: «…တို့၏ အချို့နှင့် ကင်းကွာကြသည်»
    # --- subjects: aggregates, bases, elements, faculties (pi-1 / pi-2 nominative values)
    "Rūpakkhandhena": "ရုပ် အစုအဝေး", "Vedanākkhandhena": "ခံစားမှု အစုအဝေး", "saññākkhandhena": "မှတ်သိမှု အစုအဝေး",
    "saṅkhārakkhandhena": "ပြုပြင်ဖန်တီးမှု အစုအဝေး", "viññāṇakkhandhena": "သိစိတ် အစုအဝေး",
    "Cakkhāyatanena": "မျက်စိ အာရုံခံ နယ်ပယ်", "phoṭṭhabbāyatanena": "အထိအတွေ့ အာရုံခံ နယ်ပယ်",
    "manāyatanena": "မနော အာရုံခံ နယ်ပယ်",
    "cakkhudhātuyā": "မျက်စိ ဓာတ်", "phoṭṭhabbadhātuyā": "အထိအတွေ့ ဓာတ်",
    "Cakkhuviññāṇadhātuyā": "မျက်စိ သိစိတ် ဓာတ်", "sotaviññāṇadhātuyā": "နား သိစိတ် ဓာတ်",
    "ghānaviññāṇadhātuyā": "နှာခေါင်း သိစိတ် ဓာတ်", "jivhāviññāṇadhātuyā": "လျှာ သိစိတ် ဓာတ်",
    "kāyaviññāṇadhātuyā": "ကိုယ် သိစိတ် ဓာတ်", "manoviññāṇadhātuyā": "မနော သိစိတ် ဓာတ်",
    "Cakkhundriyena": "မျက်စိ၏ စွမ်းရည်",           # pi-2 cakkhundriya
    "indriyena": "စွမ်းရည်", "indriyehi": "စွမ်းရည်", "indriyato": "စွမ်းရည်",
    "saccena": "သစ္စာ",
    # --- subjects: dependent origination, the jāti list, the wings of awakening, mental factors (pi-2 values)
    "saṅkhārena": "ပြုပြင်ဖန်တီးမှု", "viññāṇena": "သိစိတ်", "nāmarūpena": "စိတ်ပိုင်းနှင့် ရုပ်ပိုင်း",
    "phassena": "တွေ့ထိမှု", "upādānena": "စွဲလမ်းမှု", "bhavena": "ဘဝ",
    "jarāya": "အိုခြင်း", "maraṇena": "သေခြင်း", "jhānena": "ဈာန်",
    "Sokena": "စိုးရိမ်ခြင်း", "Paridevena": "ငိုကြွေးခြင်း", "dukkhena": "ကိုယ်ဆင်းရဲခြင်း",
    "domanassena": "စိတ်ဆင်းရဲမှု", "upāyāsena": "ပြင်းစွာ ပူပန်ခြင်း",
    "upaṭṭhānena": "ပဋ္ဌာန်", "padhānena": "ကြိုးပမ်းအားထုတ်ခြင်း", "appamaññāya": "အပ္ပမညာ",
    "balehi": "စွမ်းအား", "aṅgehi": NONE,             # bojjhaṅgehi = «ဗောဇ္ဈင်» (sample: aṅgā = no direct equivalent)
    "ariyena": "အရိယာ", "aṭṭhaṅgikena": "အင်္ဂါ ရှစ်ပါး ရှိသော", "maggena": "မဂ်",
    "manasikārena": "နှလုံးသွင်းခြင်း", "manasi": "နှလုံးသွင်းခြင်း",   # manasi = member of manasi(kāra) in the verse
    "Cittena": "စိတ်", "manena": "စိတ်",               # manena yuttā «စိတ်နှင့် ယှဉ်သော» (the verse)
    "yuttā": "ယှဉ်သော",
    # --- subjects: the dyads of the Mātikā (pi-1 / pi-2 values of the nominative)
    "Hetūhi": "အမြစ်", "sampayuttehi": "ယှဉ်တွဲသော", "vippayuttehi": "ကင်းကွာသော",
    "asaṅkhatehi": "ပြုပြင်ဖန်တီးထားခြင်း မရှိသော",
    "Āsavehi": "စိတ်အစွန်းအထင်း", "Saṃyojanehi": "နှောင်ကြိုး", "ganthehi": "အထုံး", "oghehi": "ရေအလျဉ်",
    "yogehi": "ထမ်းပိုး", "parāmāsehi": "မှားယွင်းသော ယူဆမှု", "Upādānehi": "စွဲလမ်းမှု", "kilesehi": "ကိလေသာ",
    "Cittehi": "စိတ်",
    "upādādhammehi": "မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော သဘောတရား",   # one Pāli word: pi-1 «upādā dhammā»
    "sahabhūmi": "အတူ တည်ရှိသော",                    # the reading Cittasahabhūmi (= sahabhū, pi-1 / pi-2)
    "punareva": NONE,                               # only the variant in the bracket (pi-1 brief)
    # --- the colophon verses
    "upari": "အထက်", "Uddhaṃ": "အထက်",               # «cuddasūpari» «အထက်တွင်»; «Uddhaṃ puna» «အထက်တွင် တဖန်»
    "cuddasa": "ဆယ့်လေးပါး", "Samatiṃsa": "သုံးဆယ်ပါး အပြည့်",
    "gocchaka": "အစု", "gocchakesu": "အစု", "gocchake": "အစု",   # M11: gocchaka «အစု» (the clusters)
    "dukā": "နှစ်မျိုးတွဲ", "vidhā": "မျိုး",          # pi-2 duka; pi-1 vidhena = မျိုး (tiṃsavidhā «သုံးဆယ်မျိုး»)
    "antarā": "ကြားညှပ်", "antare": "ကြားညှပ်",         # pi-1 antara
    "tathariva": "ထို့အတူ",                         # = tathā (pi-2) with the euphonic r
    "vicāraṇā": "ဆက်လက်သုံးသပ်မှု",                   # vitakkavicāraṇā «စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှု»
    "Samucchede": "ပိုင်းဖြတ်ခြင်း", "labbhare": "တွေ့ရသည်",    # «… မတွေ့ရကြ» (verb rule 4, negative in the text)
    "mataṃ": "သေခြင်း",                             # jātijarāmataṃ = jāti jarā maraṇa (the text «… သေခြင်း»)
    "mogha": "အချည်းနှီး", "pucchakena": "မေးခွန်း",   # moghapucchakena «မေးခွန်း အချည်းနှီး ဖြစ်သောကြောင့်»
    "sattacattālīsa": "လေးဆယ့်ခုနစ်ပါး",
    "sattacattālīsa dhammā": "သဘောတရား လေးဆယ့်ခုနစ်ပါး",   # «ဤသဘောတရား လေးဆယ့်ခုနစ်ပါးတို့သည်» (rule 1, count kept)
}
T_DUTIYA = {}
T_TATIYA = {}
T_CATUTTHA = {}
T_PANCAMA = {}
T_SATTAMA = {}
T_ATTHAMA = {}
CTX_MINE = {
    # the colophon verse of the fifth method: «… itthipumaṃ … jāti jarā maccurūpaṃ … esanayo subuddho»
    # = «… မိန်းမ၊ ယောက်ျား … သေခြင်း၊ ရုပ် ဖြစ်သော သဘောတရား … ဤခွဲနည်းကို ကောင်းစွာ နားလည်အပ်သည်»
    "3-227": {"pumaṃ": "ယောက်ျား", "maccu": "သေခြင်း", "su": "ကောင်းစွာ", "buddho": "နားလည်အပ်သော"},
}

SHARED_TABLES = [T_PREAMBLE, T_UDDESO, T_PATHAMA, T_MINE, T_DUTIYA, T_TATIYA, T_CATUTTHA, T_PANCAMA, T_SATTAMA, T_ATTHAMA]


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
CTX.update(CTX_MINE)

SECTIONS = {"preamble": T_PREAMBLE, "1-uddeso": T_UDDESO, "2-pathamanayo": T_PATHAMA,
            "3-dutiyanayo": T_DUTIYA, "4-tatiyanayo": T_TATIYA, "5-catutthanayo": T_CATUTTHA,
            "6-pancamanayo": T_PANCAMA, "8-sattamanayo": T_SATTAMA, "9-atthamanayo": T_ATTHAMA}
CHAPTERS = ["3-dutiyanayo", "4-tatiyanayo", "5-catutthanayo", "6-pancamanayo", "8-sattamanayo", "9-atthamanayo"]


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
TOP = []   # the (sid, kw) of every top-level keyword use


# P1: subject + predicate biterms «X saṅgahitā» (the predicate of the frame); P2 «āyatanehi N» / «N dhātūhi»
PRED = {"saṅgahito", "saṅgahitā", "saṅgahitaṃ", "saṅgahitāni"}
# this agent's chapters: the same biterm with the predicates of methods 2, 5 (asaṅgahitā) and 7, 8 (vippayuttā /
# sampayuttā): «dhammā asaṅgahitā» = သဘောတရား … အကျုံးမဝင်သော (sample P1)
PRED |= {"asaṅgahito", "asaṅgahitā", "asaṅgahitaṃ", "asaṅgahitāni", "sampayuttā", "vippayuttā"}


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
    if ws[-1] in ("dhammā", "dhammehi"):          # «X dhammehi» = «X dhammā» (rule 5; the instrumental goes)
        b = lookup(ch, sid, " ".join(ws[:-1]), pali, my)
        # rule 10: « … » where the head noun does not follow the qualifier in the text (a compound fragment)
        return b + (" " if (b + " " + DH) in my else " … ") + DH
    if len(ws) == 2 and ws[0] == "āyatanehi" and ws[1] in NUM_INSTR:
        return AYATANA + " … " + NUM[NUM_INSTR[ws[1]]] + "ပါး"
    if len(ws) == 2 and ws[1] in ("dhātūhi", "dhātuyā") and ws[0] in NUM_INSTR:
        return DHATU + " " + NUM[NUM_INSTR[ws[0]]] + "ပါး"
    return None


CASE_END = [("ehi", ("ā", "a", "aṃ", "o", "āni")), ("īhi", ("ino", "ī", "i")), ("ūhi", ("ū", "u", "uno")),
            ("ena", ("o", "aṃ", "a", "ā")), ("āya", ("ā", "a")), ("iyā", ("i", "ī")), ("uyā", ("u",)),
            ("esu", ("ā", "a")), ("ato", ("o", "a"))]


def case_variants(kw):
    """the nominative forms of an instrumental / dative / locative keyword (word by word; dhammehi -> dhammā), the
    lemma's pi-1 / pi-2 keys: «Sanidassanehi» -> Sanidassanā …; only variants that pi-1 or pi-2 has."""
    import itertools
    opts = []
    for w in kw.split():
        if w == "dhammehi":
            opts.append(["dhammā"])
            continue
        o = [w]
        for end, news in CASE_END:
            if w.endswith(end) and len(w) > len(end) + 1:
                o += [w[: -len(end)] + n for n in news]
                break
        opts.append(o)
    out = []
    for combo in itertools.product(*opts):
        alt = " ".join(combo)
        if alt != kw and (prev_vals(PI2, alt) or prev_vals(PI1, alt)):
            out.append(alt)
    return out


def compose_last(ch, sid, kw, pali, my):
    v = _compose_last(ch, sid, kw, pali, my)
    if v is not None:
        return v
    ws = kw.split()
    if 2 <= len(ws) <= 3 and "/" not in ws:     # M12: any other biterm = its members in text order, « … » for a gap
        parts = [lookup(ch, sid, w, pali, my) for w in ws]
        parts = [x for x in parts if x != NONE]
        out = parts[0]
        for x in parts[1:]:
            out += (" " if (out.split(" … ")[-1] + " " + x) in my else " … ") + x
        return out
    return None


def _compose_last(ch, sid, kw, pali, my):
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
    if kw.endswith(" dhammehi"):               # the same for «X dhammehi» = the pi-1 «X dhammā» (case variant)
        for alt in case_variants(kw):
            v, tag = pi_get(alt, my, tiers=("contig",))
            if v is not None:
                SRC[(sid, kw)] = tag + "-case"
                return v
    v = compose_first(ch, sid, kw, pali, my)
    if v is not None:
        SRC[(sid, kw)] = "compose"
        return v
    v, tag = pi_get(kw, my)
    if v is not None:
        SRC[(sid, kw)] = tag
        return v
    for alt in case_variants(kw):              # the pi-1 / pi-2 value of the same lemma in the nominative (rule 1)
        v, tag = pi_get(alt, my)
        if v is not None:
            SRC[(sid, kw)] = tag + "-case"
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
                    TOP.append((sid, kw))
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
dictionary form of the approved pi-1 and pi-2 Burmese mappings. **Binding and unchanged:** pi-1 `map-table.md`
rules 1–11 (approved sample), the agreed later pi-1 rules (`map-table-2-01 … -5.md`, `map-harmonise-notes.md`:
absolutives keep «…၍»; «samaye X» = «အချိန်၌ ရှိသော X» (none here); relative pronouns = (no direct equivalent)
where the Burmese builds the clause with «ရှိသော / ရှိသမျှ» (none here); one sense per segment; no « / »
alternatives; caya = (no direct equivalent) where apacaya is one word (none here)) and pi-2's approved rules N1–N11
and harmonise decisions (compound members inside one Burmese word = (no direct equivalent); the ONE presence check).
pi-2 and pi-1 values are reused for the same keyword where they occur in the pi-3 segment: the script looks every
keyword not in its own table up in the final pi-2 mapping, then pi-1 (a value the text has as a phrase first; for
«X dhammā» keywords only such a phrase).

Rules this sample uses that pi-1 / pi-2 already had, applied to the Dhātukathā's shapes:

- **Nouns** (pi-1 rule 1): no case particle, no plural at the end: khandhehi / khandhena = အစုအဝေး, āyatanehi /
  āyatanena = အာရုံခံ နယ်ပယ်, dhātūhi / dhātuyā = ဓာတ် (text «… တို့တွင်», «… မည်မျှတို့တွင်»); saṅkhārā =
  ပြုပြင်ဖန်တီးမှု (text «…မှုများ»); sabbā = အားလုံး (text «အားလုံးသည်လည်း»). Verbal nouns keep «ခြင်း»: saṅgaho =
  အကျုံးဝင်ခြင်း, asaṅgaho = အကျုံးမဝင်ခြင်း, vippayogo = ကင်းကွာခြင်း; saṅgahāsaṅgaha keeps its inner «နှင့်».
- **Participles** (pi-1 rule 3; pi-2 saṅgahitaṃ = အကျုံးဝင်သော): the predicate saṅgahito / -ā / -aṃ / -āni =
  အကျုံးဝင်သော, asaṅgahito / -ā / -aṃ / -āni = အကျုံးမဝင်သော, whatever the text's ending (statement «…သည်။»,
  plural «…ကြသည်», negative answer «…မဝင်။», question «…သနည်း», «where» clause «…ရာ»); in the Uddesa
  sampayuttaṃ / vippayuttaṃ / asaṅgahitaṃ = ယှဉ်တွဲသော / ကင်းကွာသော / အကျုံးမဝင်သော: the text's «…သည့်အရာ» (N11)
  supplies the head noun «အရာ», which is not the keyword (rule 3). asaṅkhataṃ = ပြုပြင်ဖန်တီးထားခြင်း မရှိသော (pi-2;
  the text's head «သဘောတရား» is not the keyword).
- **Numerals** (pi-1 harmonise decision 5): the text's count with its classifier: ekādasa = ဆယ့်တစ်ပါး, dasa =
  ဆယ်ပါး, dvādasa = ဆယ့်နှစ်ပါး (pi-1 / pi-2), aṭṭhārasa = ဆယ့်ရှစ်ပါး, bāvīsati = နှစ်ဆယ့်နှစ်ပါး, and every
  instrumental count (sattarasahi = ဆယ့်ခုနစ်ပါး …); a counted noun keeps its count (rule 1): ekādasahāyatanehi =
  အာရုံခံ နယ်ပယ် ဆယ့်တစ်ပါး, sattarasahi dhātūhi = ဓာတ် ဆယ့်ခုနစ်ပါး, aṭṭhārasa dhātuyo = ဓာတ် ဆယ့်ရှစ်ပါး (pi-2).
- **«X dhammā»** (pi-1 rule 5): the qualifier + « သဘောတရား»; «na / no X» = the text's «…သည် မဟုတ်သော» (na sahagatā
  dhammā = အတူ ဖြစ်သည် မဟုတ်သော သဘောတရား). Mātikā items keep the pi-1 / pi-2 values (Rūpino = ရုပ် ဖြစ်သော, hetukā
  = အမြစ် (rule 2), raṇā = ပဋိပက္ခ, avacarā = ဘုံနှင့် ဆိုင်သော …).
- **Subject + predicate pairs** (pi-1 5 rule 21, pi-2 «khandhā siyā»): the biterms of the frame «X saṅgahito /
  -ā / -aṃ / -āni» = X … အကျုံးဝင်သော (Rūpakkhandho … saṅgahito: «ရုပ် အစုအဝေးသည် … အကျုံးဝင်သည်»; khandhā
  saṅgahitā = အစုအဝေး … အကျုံးဝင်သော; dhammā saṅgahitā = သဘောတရား … အကျုံးဝင်သော; Aṭṭhārasa dhātuyo saṅgahitā =
  ဓာတ် ဆယ့်ရှစ်ပါး … အကျုံးဝင်သော); «asaṅkhataṃ ṭhapetvā» = ပြုပြင်ဖန်တီးထားခြင်း မရှိသော … ချန်ထား၍ (absolutive
  «၍» kept, pi-1 harmonise decision 1).
- **Fragments** (pi-1 rule 8): the positive part of a negated word: aññāta (anaññāta) = သိရသော, dukkha in
  adukkhamasukhāya = နာကျင် (the text builds the pair «မနာကျင် မသာယာသော» with one «သော», so the fragment keeps the
  text's form, pi-1 rule 3), uppannā in anuppannā = ဖြစ်ပေါ်သော (pi-1: no «ပြီး» in the text), paṭighā in
  (a)ppaṭighā = ထိခိုက်မှု (rule 2), pariyāpannā (apariyāpannā) = ဘဝဘုံတို့၌ အကျုံးဝင်သော (pi-2 Mātikā value).
- **Verbs** (pi-1 rule 4): ñassāmi (anaññātaññassāmītindriya) = သိရတော့သည် (text future «သိရတော့မည်», pi-2 N12
  ending «မည်»); namo = ရှိခိုးသည်.
- **Compound members inside one Burmese word** (pi-2 harmonise decision 4): bojjhaṅga «ဗောဇ္ဈင်»: bodhi = ဗောဇ္ဈင်,
  aṅgā = (no direct equivalent) (pi-2 ^2-522 aṅgo); upaṭṭhānā / upaṭṭhānaṃ (satipaṭṭhāna) = ပဋ္ဌာန် and pādā
  (iddhipāda) = ပါဒ် (the pi-2 values); kāma in kāmabhavo / kāmāvacarā = ကာမ (inside «ကာမဘုံ»).
- **Sense by context, one sense per segment** (pi-1 harmonise decision 3): rūpa by the first rūpa compound of the
  Pāli segment (rūpakkhandha «ရုပ်»; rūpāyatana / rūpadhātu «အဆင်းအရောင်»; rūpāvacara and now rūpabhava
  «သိမ်မွေ့သော ရုပ်», text «သိမ်မွေ့သော ရုပ်ဘုံ၌ ဖြစ်သော ဘဝ»); the same for dukkha (dukkhasacca «ဒုက္ခ»,
  dukkhindriya «နာကျင်မှု», dukkhāya vedanāya «နာကျင်သော», adukkhamasukha «နာကျင်») and sukha (sukhindriya /
  sukhasahagata «သာယာမှု», sukhāya vedanāya «သာယာသော»); sammā = အပြည့်အဝ in the homage (pi-1 / pi-2 preamble),
  မှန်ကန်သော in sammappadhāna (pi-1 / pi-2); bahiddhā = မိမိ၏ ပြင်ပ၌ (pi-2 N10).
- **Titles and headings** (pi-1 rule 7, decision 4): Dhātukathā / dhātukathāya = ဓာတ်များအကြောင်း ဆွေးနွေးခြင်း (the
  approved title whole; the dative's «၏» goes), its members kathā = ဆွေးနွေးခြင်း, dhātu = ဓာတ်; dhammasaṅgaṇī =
  သဘောတရားများကို စုစည်းရေတွက်ခြင်း, saṅgaṇī, dhamma (pi-1 [1-0]); Uddeso = အကျဉ်း ဖော်ပြချက် (pi-1); mātikā =
  ခေါင်းစဉ်စာရင်း; niddeso = အကျယ် ဖော်ပြချက်; paṭicca / samuppāda / ādi (pi-2); the mātikā names naya, abbhantara,
  nayamukha, lakkhaṇa, bāhira = the heading's own words.

## Approved sample rules M1–M9 (map-table.md, user 2026-11-18; binding, copied unchanged)

M1. **The count biterms of the frame** «āyatanehi N» (from «…āyatanehi N-hi dhātūhi») = «အာရုံခံ နယ်ပယ် …
    N-ပါး»: the āyatana noun of the compound before and the count that belongs to the dhātus after; the gap holds
    the āyatana count and «ဓာတ်» (text «အာရုံခံ နယ်ပယ် ဆယ့်တစ်ပါး၊ ဓာတ် ဆယ့်ခုနစ်ပါး»). The pair «N dhātūhi» is
    contiguous in Burmese order: «ဓာတ် N-ပါး».
M2. **«A / B» keywords** (the extractor's pair of two Pāli words: āyatanāni / pādā, vitakka / vicārā, vitakkā /
    vicārā, vitakka / vicāra, aññā / aññātāvī, kāma / āyatanehi) = «A … B», both members in text order (no « / »
    alternatives allowed in a value): vitakka / vicārā = စတင်ကြံစည်မှု … ဆက်လက်သုံးသပ်မှု.
M3. **khandhato** (in «asaṅkhataṃ khandhato ṭhapetvā») = «အစုအဝေး ရေတွက်ရာ»: the text says «from the count of the
    aggregates» («အစုအဝေး ရေတွက်ရာမှ»); only the ablative «မှ» goes (rule 1), «ရေတွက်ရာ» carries the ablative's
    meaning here (the aggregates as a class counted), like pi-2 N9 kenaci = «တစ်စုံတစ်ခုသော စိတ်».
M4. **«X dhammā» with a gap** (pi-1 rule 10 applied by the script): where the head noun does not follow the
    qualifier in the text, « … » marks the gap: the fragments hetukā dhammā in the negated «na … pahātabbahetukā»
    («…အမြစ် ရှိသည် မဟုတ်သော သဘောတရား») = အမြစ် … သဘောတရား, avitakka dhammā (avitakkavicāramattā, avitakkaavicārā)
    = စတင်ကြံစည်မှု မရှိသော … သဘောတရား, savitakka dhammā (savitakkasavicārā) = စတင်ကြံစည်မှု ရှိသော … သဘောတရား,
    saṃsaṭṭha dhammā (cittasaṃsaṭṭhasamuṭṭhānā) = ရောနှောသော … သဘောတရား, no saṃsaṭṭha dhammā = ရောနှောသော …
    မဟုတ်သော သဘောတရား. Where the text has the pi-1 / pi-2 «X dhammā» value as a phrase, that value is used.
M5. **The colophon members**: Ekamūlakaṃ = «တစ်မျိုးတွဲကို အခြေခံသော» (pi-2 N8 mūlakaṃ «အခြေခံသော», the head
    «ခွဲနည်း» is not the keyword); eka (its member) = «တစ်မျိုးတွဲ», as pi-2 duka / tika / catukka = «နှစ်မျိုးတွဲ /
    သုံးမျိုးတွဲ / လေးမျိုးတွဲ» for the members of Dukamūlakaṃ … (eka is not ekena: the counts are «တစ်ပါး»).
    Dvādasakaṃ / Aṭṭhārasakaṃ (none keywords here) would be «ဆယ့်နှစ်မျိုးတွဲ / ဆယ့်ရှစ်မျိုးတွဲ».
M6. **The Lakkhaṇamātikā**: visabhāgo = «ကွဲပြားသော သဘော» (a noun, the whole noun phrase of the text, rule 1);
    bhāga (the member of sabhāga / visabhāga) = «သဘော».
M7. **Presence check, three more endings for «Xသော»** (ATTR_FROM): «သနည်း» (the question «အကျုံးမဝင်သနည်း»),
    «ရာ» (the «where» clause «အကျုံးမဝင်ရာ … မရှိ») and «သေးသည်» (aññāta in «မသိရသေးသည်ကို», as pi-1's «သေးသော»).
    pi-2 accepts «သနည်း» and «ရာ» for «Xသည်» already (12-14 M1); a participle in a question / «where» clause is
    the same normalisation (rule 3). All other endings are pi-2's merged list, unchanged.
M8. **nayo / naya** = «ခွဲနည်း» (one word in the pi-3 text and the pi-1 rails text, my3-zeroshot-terms), not pi-1's
    «နည်း» (a separate word in its text: «ဈာန် လေးပါး နည်း»).
M9. **vokāra** (in eka- / catu- / pañcavokārabhavo «အစုအဝေး N-ပါး ရှိသော ဘဝ») = «အစုအဝေး»; **pucchake** (in the
    variant note «vibha. dukapañhāpucchakepi» = «… နှစ်မျိုးတွဲ မေးခွန်းများဖြင့် ဖော်ပြချက်၌လည်း») = «ဖော်ပြချက်»,
    pañhā = «မေးခွန်း» (pi-2): the note is translated, so its words have a Burmese equivalent (pi-1's (no direct
    equivalent) is for Pāli kept in Roman script inside a variant bracket).
"""

MY_RULES = """
## NEW rules in chapters 3, 4, 5, 6, 8, 9 (for the user's review)

M10. **kehici** (in «ekenāyatanena ekāya dhātuyā kehici vippayuttā») = «အချို့»: the text says «…တို့၏ အချို့နှင့်
     ကင်းကွာကြသည်» (dissociated from some of them, i.e. from part of the base and the element). pi-2 N9 kenaci =
     «တစ်စုံတစ်ခုသော စိတ်» is the singular «by some consciousness», another construction, not in these segments.
M11. **Case forms of a pi-1 / pi-2 lemma**: the subjects of the frames stand in the instrumental (Vedanākkhandhena,
     Sanidassanehi dhammehi, saṃkilesikehi, cittānuparivattīhi …), which pi-1 / pi-2 hardly have. They get the pi-2
     (then pi-1) value of the SAME word in the nominative where it occurs in the segment (rule 1: the text's
     «…နှင့်» goes): the script derives the nominative keys (-ehi → -ā / -a / -aṃ / -o, -īhi → -ino / -ī, -ūhi → -ū,
     -ena → -o / -aṃ, -āya → -ā, -iyā → -i, -esu → -ā; dhammehi → dhammā) and applies the usual pi_get (phrase first,
     then literal chunks, then an ending rule). «X dhammehi» = the pi-1 «X dhammā» value where the text has it as a
     phrase, else «X» + « သဘောတရား» (rule 5). Words that neither mapping has in any case (Cakkhāyatanena,
     cakkhudhātuyā, saccena, upāyāsena …) are in the table with the pi-1 / pi-2 value of their members.
M12. **Frame biterms of methods 2–8**: «dhammā asaṅgahitā» = «သဘောတရား … အကျုံးမဝင်သော», «dhammā vippayuttā» =
     «သဘောတရား … ကင်းကွာသော» (the sample's «dhammā saṅgahitā» with the other predicates); «āyatanasaṅgahena
     saṅgahitā» = «အာရုံခံ နယ်ပယ် အကျုံးဝင်ခြင်း … အကျုံးဝင်သော»; khandhasaṅgahena = «အစုအဝေး အကျုံးဝင်ခြင်း»,
     āyatanasaṅgahena = «အာရုံခံ နယ်ပယ် အကျုံးဝင်ခြင်း» (the verbal noun keeps «ခြင်း», the instrumental «ဖြင့်»
     goes, rule 1). Any other two- or three-word keyword of the extractor (dhammehi khandhasaṅgahena, indriyena
     khandhasaṅgahena, paccayā āyatanena) = its members in Pāli order, « … » where they are not adjacent in the
     Burmese (pi-1 rule 10): dhammehi khandhasaṅgahena = «သဘောတရား … အစုအဝေး အကျုံးဝင်ခြင်း».
M13. **Colophon verse words** (the text's own words): gocchaka / gocchakesu / gocchake = «အစု» (the clusters: «အစု
     ဆယ်ပါးတို့တွင်», «အစုတို့၏ ပုဒ်», «အစုတို့တွင်»); upari / Uddhaṃ = «အထက်»; Samatiṃsa = «သုံးဆယ်ပါး အပြည့်»;
     cuddasa = «ဆယ့်လေးပါး»; antarā / antare = «ကြားညှပ်» (pi-1 antara); tathariva = «ထို့အတူ» (pi-2 tathā); vidhā
     (tiṃsavidhā «သုံးဆယ်မျိုး») = «မျိုး» (pi-1 vidhena); manasi (adhimuccanā manasi = manasikāra) = «နှလုံးသွင်းခြင်း»;
     manena yuttā «စိတ်နှင့် ယှဉ်သော»: manena = «စိတ်», yuttā = «ယှဉ်သော»; vicāraṇā = «ဆက်လက်သုံးသပ်မှု»;
     Samucchede = «ပိုင်းဖြတ်ခြင်း»; labbhare = «တွေ့ရသည်» (verb rule 4; the separate na is not a keyword, the text
     «မတွေ့ရကြ» matches by the negative-verb rule, as pi-1 rule 8); mataṃ (jātijarāmataṃ) = «သေခြင်း»; mogha =
     «အချည်းနှီး», pucchakena = «မေးခွန်း» (moghapucchakena «မေးခွန်း အချည်းနှီး ဖြစ်သောကြောင့်»; the sample's
     pucchake = «ဖော်ပြချက်» is the section of the variant note «dukapañhāpucchake»); sattacattālīsa = «လေးဆယ့်ခုနစ်ပါး»,
     sattacattālīsa dhammā = «သဘောတရား လေးဆယ့်ခုနစ်ပါး» (a counted noun keeps its count, as pi-2 aṭṭhārasa dhātuyo);
     3-227 (one segment, CTX): su / buddho (subuddho) = «ကောင်းစွာ» / «နားလည်အပ်သော» (participle, rule 3; text
     «နားလည်အပ်သည်»), maccu = «သေခြင်း» (the text's word, not pi-2 «သေမင်း»), pumaṃ (itthipumaṃ) = «ယောက်ျား».

Applied as before (no new rule): the ordinals pañcama(o) / sattama(o) / aṭṭhama(o) = «ပဉ္စမ / သတ္တမ / အဋ္ဌမ»
(my3-zeroshot-terms); the heading members asaṅgahita / sampayutta / vippayutta = «အကျုံးမဝင်သော / ယှဉ်တွဲသော /
ကင်းကွာသော» (the sample's asaṅgahitaṃ …, text «…သည့်အရာ», N11); the predicates sampayuttā / vippayuttā =
«ယှဉ်တွဲသော / ကင်းကွာသော» (text «…ကြသည်», «…ကြသနည်း»); punareva = (no direct equivalent) (only in the variant
bracket, pi-1 brief); aṅgehi in bojjhaṅgehi = (no direct equivalent) (sample: «ဗောဇ္ဈင်» is one word); sahabhūmi (the
reading Cittasahabhūmi) = «အတူ တည်ရှိသော» (= sahabhū, pi-1 / pi-2); Natthi = «မရှိသည်» (pi-1 / pi-2; text «မရှိ။»);
the fragments of negated words keep the positive part (rule 8): saṃsaṭṭhaṃ in visaṃsaṭṭhaṃ, ārammaṇaṃ in
anārammaṇaṃ, pariyāpannehi in apariyāpannehi, upādinna in anupādinna, kāmāvacarehi after na; one sense per
segment: rūpa in 3-227 = «သိမ်မွေ့သော ရုပ်» (its first rūpa compound is rūpāvacarehi), dukkha in 3-312 = «နာကျင်»
(adukkhamasukhāya), sukha in 3-210 = «သာယာသော» (sukhāya vedanāya first).
"""

REASONS = {
    "antare": "aparante «နောက် ကြားညှပ်တွင်» = the intermediate dyads: the text's «ကြားညှပ်» (pi-1 antara, M13); pi-2 «အကြား» (between) is not in the segment",
    "maccu": "the verse's jāti jarā maccu = «မွေးဖွားခြင်း၊ အိုခြင်း၊ သေခြင်း»: the text names death «သေခြင်း»; pi-2 «သေမင်း» (Death personified) is not in the segment",
    "saṅkhārena": "avijjāpaccayā saṅkhārena: the text's «ပြုပြင်ဖန်တီးမှု» (pi-2 saṅkhārā); pi-1 «တိုက်တွန်းမှု» is sasaṅkhārena (with prompting), another sense",
    "vidhā": "tiṃsavidhā «သုံးဆယ်မျိုး» = kinds (pi-1 vidhena = မျိုး); pi-2 «နှိုင်းယှဉ် ချိန်ဆမှု» is vidhā = the discriminations (conceit), another sense",
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
    with open(HERE / "map-table-ch3-6-8-9.md", "w", encoding="utf-8") as f:
        f.write("# pi-3 Burmese keyword mapping: rules and review table (Dhātukathā «ဓာတ်များအကြောင်း ဆွေးနွေးခြင်း», "
                "chapters " + ", ".join(CHAPTERS) + ")\n\n")
        f.write("Written by map_ch3-6-8-9.py. Burmese from the FINAL pi-3 text of this track only "
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
                f"- Keywords new in pi-3 (in neither mapping): {len(table) - len(known)} distinct; of their uses, "
                f"{sum(1 for x in TOP if SRC.get(x, '').endswith('-case'))} take the pi-1 / pi-2 value of the same word "
                f"in the nominative (M11).\n"
                f"- Sources of the {len(TOP)} values: " + ", ".join(f"{k} {v}" for k, v in collections.Counter(
                    SRC.get(x, '?') for x in TOP).most_common()) + " (table / ctx = this script's or the approved "
                f"sample's tables; compose = the compose rules).\n\n")
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
        f.write(MY_RULES)
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
