"""Pāli→Burmese keyword mapping for pi-3 (Dhātukathā, «ဓာတ်များအကြောင်း ဆွေးနွေးခြင်း»).
Chapters 12-ekadasamanayo, 13-dvadasamanayo, 14-terasamanayo, 15-cuddasamanayo (methods 11-14).

usage (python3 -I -X utf8, from any directory):
  map_ch12-15.py             writes <ch>.mapped.md for the four chapters in CHAPTERS and map-table-ch12-15.md, then
                             verifies them (keyword preservation, presence of every value chunk in its segment, no
                             ", " / «၊» / « / » in a value)
  map_ch12-15.py --report    writes nothing; lists unmapped keywords and presence failures
  map_ch12-15.py --seg ID..  prints Pāli, Burmese, keywords and mapping (with the source of each value) of segments
  map_ch12-15.py --dump CH   prints the mapping of every segment of a chapter with the source of each value

Method: a copy (not an import) of the user-approved sample's map_all.py (pi-3, itself a copy of the approved pi-2
mapper): its tables T_PREAMBLE / T_UDDESO / T_PATHAMA, context functions, compose rules and the presence verifier
are kept unchanged and shared; this file adds the table T_CH12_15, the instrumental-item redirect (Q1) and the
«X-ena vippayuttā» pair (Q2). It writes only the four chapters above and map-table-ch12-15.md; it never writes the
sample's files. The Burmese is the FINAL pi-3 text of this track (AI_translation/burmese/
pi-3-burmese-plain-zeroshot_split_chapters). No other Burmese source is used.

Lookup order per keyword:
  CTX[sid] -> the chapter's own table -> the shared tables (sample + T_CH12_15)
  -> an instrumental keyword that pi-1 / pi-2 map as such (dassanena)
  -> Q1: the nominative of an instrumental keyword, resolved by this same chain
  -> compose «X dhammā» (rule 5), the pairs (P1-P3, Q2)
  -> PI2 / PI1: the final pi-2, then pi-1 mapping, the most frequent value of that keyword that is present in THIS
     segment (pi-2 first where they differ; literal presence first, then presence by an ending rule)
  -> the other compose rules.
A value «@name» is a context function f(kw, pali, my).
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

# =====================================================================================================
# chapters 12-15 (methods 11-14): one table for the four chapters (the same frames), per-segment CTX below
# =====================================================================================================
T_CH12_15 = {
    # --- headings / colophons: the ordinal as the text writes it (the heading's own word, pi-1 decision 4)
    "ekādasama": "ဧကာဒသမ", "ekādasamo": "ဧကာဒသမ", "dvādasama": "ဒွါဒသမ", "dvādasamo": "ဒွါဒသမ",
    "terasama": "တေရသမ", "terasamo": "တေရသမ", "cuddasama": "စုဒ္ဒသမ", "cuddasamo": "စုဒ္ဒသမ",
    # the «…padaniddeso» heading members: «…သည့်အရာ» = participle «…သော» (N11), the head «အရာ» is not the keyword
    "sampayutta": "ယှဉ်တွဲသော", "vippayutta": "ကင်းကွာသော",
    "saṅgahita": "အကျုံးဝင်သော", "asaṅgahita": "အကျုံးမဝင်သော",
    "sacca": "သစ္စာ", "phassa": "တွေ့ထိမှု",
    "rūpīhi": "ရုပ် ဖြစ်သော",                                 # = Rūpīhi / rūpino (sample Mātikā Rūpino)
    "adhimokkho": "ဆုံးဖြတ်မှု",                               # my3 terms (pi-2 ^2-281 text «ဆုံးဖြတ်မှု»)
    # --- the frame word kehici «…တို့၏ အချို့နှင့်» (partly): the noun, «နှင့်» goes (rule 1)
    "kehici": "အချို့",
    "dhammehi khandhasaṅgahena": "သဘောတရား … အစုအဝေး အကျုံးဝင်ခြင်း",      # rule 1 (ဖြင့် goes), rule 10 gap
    # --- the summary verses (the text's words; locatives = rule 1 nouns, adverbs keep their locative, rule 11)
    "Uddhaṃ": "အထက်", "upari": "အထက်",                       # rule 1 (as the parallel chapters 7-10-11)
    "gocchaka": "အစု", "gocchake": "အစု",
    "vidhā": "မျိုး", "tiṃsa": "သုံးဆယ်",                     # tiṃsavidhā «သုံးဆယ်မျိုး» (one word)
    "niddese": "အကျယ် ဖော်ပြချက်", "Navamassa": "နဝမ",
    "tecattālīsaṃ": "လေးဆယ့်သုံးပါး", "cuddasa": "ဆယ့်လေးပါး", "pannarasa": "ဆယ့်ငါးပါး", "soḷasa": "ဆယ့်ခြောက်ပါး",
    "saṅgahaṃ gatā": "အကျုံးဝင်သော",                         # «are included» (rule 3, as saṅgahitā)
    "duke": "နှစ်မျိုးတွဲ", "antara": "ကြားညှပ်", "antare": "ကြားညှပ်",
    "su": "ကောင်းစွာ", "buddho": "နားလည်အပ်သော",              # subuddho «ကောင်းစွာ နားလည်အပ်သည်» (rule 3)
    "maccu": "သေခြင်း", "mataṃ": "သေခြင်း", "pumaṃ": "ယောက်ျား",
    "Samucchede": "ပိုင်းဖြတ်ခြင်း", "mogha": "အချည်းနှီး", "pucchakena": "မေးခွန်း",
    "sattacattālīsa": "လေးဆယ့်ခုနစ်ပါး", "sattacattālīsa dhammā": "သဘောတရား လေးဆယ့်ခုနစ်ပါး",
    "labbhare": "တွေ့ရသည်",                                   # na labbhare «မတွေ့ရကြ»: the positive verb (rules 4, 8)
    }

# the neuter -aṃ and plural -ā / -āni forms of the predicate (inflected forms keep one value)

SHARED_TABLES = [T_PREAMBLE, T_UDDESO, T_PATHAMA, T_CH12_15]


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

SECTIONS = {"preamble": T_PREAMBLE, "1-uddeso": T_UDDESO, "2-pathamanayo": T_PATHAMA,
            "12-ekadasamanayo": T_CH12_15, "13-dvadasamanayo": T_CH12_15, "14-terasamanayo": T_CH12_15,
            "15-cuddasamanayo": T_CH12_15}
CHAPTERS = ["12-ekadasamanayo", "13-dvadasamanayo", "14-terasamanayo", "15-cuddasamanayo"]


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
    if ws[-1] in ("sampayuttā", "vippayuttā") and len(ws) == 2:
        # Q2: «X-ena (ye dhammā) vippayuttā» = «Xနှင့် ကင်းကွာသော» (pi-1 vedanāya sampayuttā = «ခံစားမှုနှင့် ယှဉ်တွဲသော»;
        # the object keeps its «နှင့်»); not contiguous: «Xနှင့် … V», or «X … V» without «Xနှင့်» (rule 10)
        a, b = lookup(ch, sid, ws[0], pali, my), lookup(ch, sid, ws[1], pali, my)
        for pl in ("", "များ", "တို့"):                 # contiguous; an inner plural stays (pi-1 «…တို့နှင့် ကင်းကွာသော»)
            if (a + pl + "နှင့် " + b) in my:
                return a + pl + "နှင့် " + b
        return a + "နှင့် … " + b if (a + "နှင့်") in my else a + " … " + b
    if ws[-1] == "dhammā":
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


# Q1: the items of methods 11-14 are instrumentals («X-ena / X-ehi ye dhammā …»); the text renders the item by the
# topic's nominative Burmese + «နှင့်» (make_ch12-15 item_nom), so the keyword takes the value of its nominative
# (pi-1 rule 1: no case particle). Candidates per word, first one that resolves wins.
KEEP = {"ceva", "ca", "na", "no", "neva", "sukhāya", "dukkhāya", "adukkhamasukhāya", "dassanena", "bhāvanāya",
        "vedanāya"}
NOM_IRREG = {"hetūhi": ["hetū"], "dhammehi": ["dhammā"], "upādādhammehi": ["upādā dhammā"]}


def word_noms(w, multi):
    if multi and w in KEEP:
        return [w]
    if w in NOM_IRREG:
        return NOM_IRREG[w]
    out = []
    for suf, reps in (("bhūhi", ("bhuno", "bhū")), ("īhi", ("ino", "ī")), ("ūhi", ("ū", "uno")),
                      ("ehi", ("ā", "āni", "o", "aṃ")), ("ena", ("o", "aṃ", "ā")), ("āya", ("ā",)),
                      ("iyā", ("i",)), ("uyā", ("u",)), ("āhi", ("ā",))):
        if w.endswith(suf) and len(w) > len(suf) + 1:
            out += [w[:-len(suf)] + r for r in reps]
            break
    return out


def nom_cands(kw):
    ws = kw.split()
    if " / " in kw:
        return []
    alts = [word_noms(w, len(ws) > 1) or [w] for w in ws]
    if all(len(a) == 1 and a[0] == w for a, w in zip(alts, ws)):
        return []
    import itertools
    return [" ".join(c) for c in itertools.product(*alts)]


_REDIR = set()


def nom_redirect(ch, sid, kw, pali, my):
    cands = nom_cands(kw)
    if not cands or (sid, kw) in _REDIR:
        return None
    _REDIR.add((sid, kw))
    # a candidate in a table first; then the candidate the pi-1 / pi-2 mappings use most (the real lemma)
    intab = [c for c in cands if table_get(CTX.get(sid, {}), c) is not None or table_get(SHARED, c) is not None]
    rest = sorted((c for c in cands if c not in intab), key=lambda c: -sum(prev_any(c).values()))
    try:
        for c in intab + rest:
            try:
                v = lookup(ch, sid, c, pali, my)
            except KeyError:
                continue
            if presence(v, my)[0]:
                SRC[(sid, kw)] = "nom:" + c + ":" + SRC.get((sid, c), "?")
                return v
        return None
    finally:
        _REDIR.discard((sid, kw))


def _lookup(ch, sid, kw, pali, my):
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
    if nom_cands(kw) and prev_any(kw):          # an instrumental keyword that pi-1 / pi-2 map as such (dassanena)
        v, tag = pi_get(kw, my, tiers=("contig", "literal"))
        if v is not None:
            SRC[(sid, kw)] = tag
            return v
    v = nom_redirect(ch, sid, kw, pali, my)     # instrumental items -> the nominative keyword (Q1, below)
    if v is not None:
        return v
    if kw.endswith(" dhammā"):                 # a pi-1 / pi-2 «X dhammā» value that the text has as a phrase
        v, tag = pi_get(kw, my, tiers=("contig",))
        if v is not None:
            SRC[(sid, kw)] = tag
            return v
    v = compose_first(ch, sid, kw, pali, my)
    if v is not None:
        SRC[(sid, kw)] = "compose"
        return v
    v, tag = pi_get(kw, my)
    if v is not None:
        SRC[(sid, kw)] = tag
        return v
    v = compose_last(ch, sid, kw, pali, my)
    if v is not None:
        SRC[(sid, kw)] = "compose"
        return v
    raise KeyError(kw)


_DEPTH = [0]


def lookup(ch, sid, kw, pali, my):
    """map-harmonise: the script's own lookup, then the book-wide alignments of harmonise_rules.py, applied to the
    keyword's final value only (not to the inner lookups of compose / redirect rules, which look other keywords up)."""
    _DEPTH[0] += 1
    try:
        v = _lookup(ch, sid, kw, pali, my)
    finally:
        _DEPTH[0] -= 1
    if _DEPTH[0]:
        return v
    h = harmonise_rules.apply(kw, sid, v, pali, my)
    if h != v:
        SRC[(sid, kw)] = "harmonise"
    return h


# =====================================================================================================
# presence check: the ONE check shared by all pi-3 mapping scripts (presence_check.py; map-harmonise
# decision 3: the documented ending list). Imported, not copied, so every script uses the same form.
# =====================================================================================================
sys.path.insert(0, str(HERE))
from presence_check import ATTR_FROM, VERB_FROM, chunk_present, presence  # noqa: E402,F401
import harmonise_rules  # noqa: E402  (map-harmonise: the book-wide alignments, applied in lookup())


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

**Binding and unchanged:** everything the approved sample (`map-table.md`) lists: pi-1 rules 1–11, the agreed later
pi-1 rules (absolutives keep «…၍»; one sense per segment; no « / » alternatives …), pi-2's N1–N11 and harmonise
decisions, and the sample's M1–M9 (count biterms «āyatanehi N» = «အာရုံခံ နယ်ပယ် … N-ပါး» and «N dhātūhi» =
«ဓာတ် N-ပါး»; «A / B» = «A … B»; khandhato = «အစုအဝေး ရေတွက်ရာ»; «X dhammā» with a gap (M4: the negated
«na … pahātabbahetukehi» = «အမြစ် … သဘောတရား», avitakka / savitakka dhammā …); the presence endings «သနည်း», «ရာ»,
«သေးသည်»; nayo = «ခွဲနည်း» …). The sample's tables and context functions (rūpa, dukkha, sukha by the first compound
of the segment) are copied unchanged and shared, so every keyword the sample has keeps the sample's value
(saṅgahitā / asaṅgahitā, ṭhapetvā, asaṅkhataṃ, the counts, the topic members, aññāta, ñassāmi, bodhi / aṅgā,
upaṭṭhāna, dukkhaṃ = «ကိုယ်ဆင်းရဲခြင်း» …). pi-2 and pi-1 values are reused for the same keyword where they occur
in the segment, as in the sample.

## NEW rules (for the user's review)

Q1. **Instrumental items take the value of their nominative.** Methods 11-14 name every topic in the instrumental
    («Samudayasaccena / hetūhi dhammehi / dhātuyā ye dhammā …»); the text renders each item by the topic's
    nominative Burmese + «နှင့်» (the generator's item_nom), so the keyword takes the pi-1 / pi-2 / sample value of
    the nominative, without the case particle (pi-1 rule 1): saccena = သစ္စာ, indriyena = စွမ်းရည်, bhavena = ဘဝ,
    jātiyā = မွေးဖွားခြင်း, hetūhi = အမြစ်, hetukehi = အမြစ် (rule 2), sampayuttehi = ယှဉ်တွဲသော, Rūpīhi dhammehi =
    ရုပ် ဖြစ်သော သဘောတရား, bhāvanāya pahātabbehi = ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ရမည့် … Candidates per word (-ena
    -> -o / -aṃ / -ā; -ehi -> -ā / -āni / -o / -aṃ; -āya -> -ā; -iyā -> -i; -uyā -> -u; -īhi -> -ino / -ī;
    -bhūhi -> -bhuno; -ūhi -> -ū; hetūhi -> hetū; upādādhammehi -> upādā dhammā); a candidate in a table first,
    then the one pi-1 / pi-2 use most (the real lemma); its value must be present in the segment. An instrumental
    keyword that pi-1 / pi-2 already map as such keeps that value (dassanena = သစ္စာကို မြင်ခြင်း, pi-1 / pi-2).
    rūpīhi = «ရုပ် ဖြစ်သော» (the sample's Rūpino, the same as Rūpīhi; not pi-2's «ရုပ် ရှိသော» for rūpī).
Q2. **«X-ena / X-ehi (ye dhammā) vippayuttā»** (the extractor's pair of an item and the verb of the relative
    clause) = «Xနှင့် ကင်းကွာသော» where the text has it contiguously, as pi-1 «vedanāya sampayuttā = ခံစားမှုနှင့်
    ယှဉ်တွဲသော» (the object keeps its «နှင့်», rule 3): bhavena vippayuttā = ဘဝနှင့် ကင်းကွာသော, Adhimokkhena
    vippayuttā = ဆုံးဖြတ်မှုနှင့် ကင်းကွာသော; an inner plural stays (pi-1 vitakkavicāravippayuttā «…တို့နှင့်
    ကင်းကွာသော»): dhammehi vippayuttā = သဘောတရားများနှင့် ကင်းကွာသော (the text of these chapters has «များ»; the
    parallel chapters 7-10-11 have «တို့» in their text). Where other items stand between, « … » (rule 10) after
    «Xနှင့်»: viññāṇena vippayuttā = သိစိတ်နှင့် … ကင်းကွာသော, bhavena vippayuttā (3-470, 3-471) = ဘဝနှင့် …
    ကင်းကွာသော; where the text has no «Xနှင့်» (Kusalehi: «ကုသိုလ် သဘောတရားများနှင့်…»): ကုသိုလ် … ကင်းကွာသော.
    The same forms as the parallel chapters 7-10-11 (their M3).
Q3. **The frame words**: kehici = «အချို့» (text «… တို့၏ အချို့နှင့်», «partly»; the genitive of the counts and
    «နှင့်» go, rule 1); dhammehi khandhasaṅgahena = «သဘောတရား … အစုအဝေး အကျုံးဝင်ခြင်း» (the item's head noun and
    the instrumental «အစုအဝေး အကျုံးဝင်ခြင်းဖြင့်» without «ဖြင့်», rule 1; the gap holds «များနှင့်»; the same value
    as the parallel chapters 7-10-11).
Q4. **Headings and colophons**: the ordinals ekādasama / -mo, dvādasama / -mo, terasama / -mo, cuddasama / -mo =
    the text's word «ဧကာဒသမ / ဒွါဒသမ / တေရသမ / စုဒ္ဒသမ» (heading's own word, pi-1 decision 4); the members of the
    «…padaniddeso» headings sampayutta / vippayutta / saṅgahita / asaṅgahita = «ယှဉ်တွဲသော / ကင်းကွာသော /
    အကျုံးဝင်သော / အကျုံးမဝင်သော» (text «…သည့်အရာ», N11; the head «အရာ» is not the keyword, as the sample's
    sampayuttaṃ in the Uddesa); sacca / phassa (Saccādi, Phassādisattakaṃ) = «သစ္စာ / တွေ့ထိမှု», ādi = «စသည်»
    (sample; text «စသည့်» matched by the verb ending rule).
Q5. **Summary verses** (the text's words; pi-1 rule 1): Uddhaṃ / upari = «အထက်» (text «အထက်တွင်», «ထို့အထက်တွင်»;
    the locative goes, as the parallel chapters 7-10-11 do); gocchaka / gocchake = «အစု»; vidhā
    (tiṃsavidhā «သုံးဆယ်မျိုး») = «မျိုး», tiṃsa = «သုံးဆယ်» (pi-2); the counts with «ပါး» (pannarasa, cuddasa,
    soḷasa, tecattālīsaṃ, sattacattālīsa); sattacattālīsa dhammā = «သဘောတရား လေးဆယ့်ခုနစ်ပါး» (counted noun keeps
    its count, rule 1); saṅgahaṃ gatā («are included», text «အကျုံးဝင်ကြသည်») = «အကျုံးဝင်သော» (rule 3, as
    saṅgahitā); su / buddho (subuddho «ကောင်းစွာ နားလည်အပ်သည်») = «ကောင်းစွာ» / «နားလည်အပ်သော» (rule 3);
    maccu (maccurūpaṃ) / mataṃ (jātijarāmataṃ) = «သေခြင်း»; pumaṃ (itthipumaṃ) = «ယောက်ျား»; Samucchede =
    «ပိုင်းဖြတ်ခြင်း»; mogha / pucchakena (moghapucchakena «မေးခွန်း အချည်းနှီး ဖြစ်သောကြောင့်») = «အချည်းနှီး» /
    «မေးခွန်း»; labbhare (na labbhare «မတွေ့ရကြ») = «တွေ့ရသည်» (rules 4, 8: the positive verb, check by infixed
    «မ»); antara / antare (Mahantaraduke, Paṭhamantare) = «ကြားညှပ်» (pi-1 headings); duke = «နှစ်မျိုးတွဲ»;
    Navamassa = «နဝမ»; niddese = «အကျယ် ဖော်ပြချက်».
Q6. **adhimokkho** (in Adhimokkhena) = «ဆုံးဖြတ်မှု» (my3-zeroshot-terms, pi-2 ^2-281 text; pi-1 / pi-2 have only
    the compound adhimokkhapaccayā «ဆုံးဖြတ်မှုကြောင့်»).
"""

REASONS = {
    "antare": "Paṭhamantare «ပထမ ကြားညှပ်»: the Mātikā section word «ကြားညှပ်» (pi-1 headings, Q5); pi-2 «အကြား» is «between» in another sense",
    "maccu": "maccurūpaṃ in the jāti-jarā-maraṇa verse list: the text's «သေခြင်း» (death); pi-2 «သေမင်း» is Death personified (Q5)",
    "vidhā": "tiṃsavidhā «သုံးဆယ်မျိုး»: «kind» (Q5); pi-2 «နှိုင်းယှဉ် ချိန်ဆမှု» is the vidhā of conceit",
    "dukkhena": "the soko … upāyāso list: the sample's dukkhaṃ «ကိုယ်ဆင်းရဲခြင်း» (Q1); pi-2 «နာကျင်မှု / ဒုက္ခ» are not in the segment",
    "hetukehi dhammehi": "negated «na … pahātabbahetukehi» («…အမြစ် ရှိသည် မဟုတ်သော သဘောတရား»): the sample's M4 gap; the positive items keep pi-1",
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


for _k, _r in harmonise_rules.REASONS.items():   # map-harmonise reasons (harmonise_rules.py)
    REASONS.setdefault(_k, _r)
RULES += harmonise_rules.TABLE_NOTE


def prev_any(kw):
    return prev_vals(PI1, kw) + prev_vals(PI2, kw)


def nom_stats():
    same, diff, new = collections.Counter(), collections.Counter(), collections.Counter()
    for ch in CHAPTERS:
        my, pa, rows = load(ch)
        for sid, kws in rows:
            for kw in [k.strip() for k in kws.split(", ")]:
                src = SRC.get((sid, kw), "")
                if not src.startswith("nom:"):
                    continue
                c = src.split(":")[1]
                v = lookup(ch, sid, kw, pa.get(sid, ""), my[sid])
                pv = prev_any(c)
                (new if not pv else same if v in pv else diff)[(kw, c, v)] += 1
    return same, diff, new


def write_table(table, ruled_all, results):
    total = sum(sum(c.values()) for c in table.values())
    known = [kw for kw in table if prev_any(kw)]
    same = [(kw, v, n) for kw, c in table.items() for v, n in c.items() if v in prev_any(kw)]
    same2 = [x for x in same if x[1] in prev_vals(PI2, x[0])]
    same1 = [x for x in same if x[1] not in prev_vals(PI2, x[0])]
    with open(HERE / "map-table-ch12-15.md", "w", encoding="utf-8") as f:
        f.write("# pi-3 Burmese keyword mapping: rules and review table (Dhātukathā «ဓာတ်များအကြောင်း ဆွေးနွေးခြင်း», "
                "chapters " + ", ".join(CHAPTERS) + ")\n\n")
        f.write("Written by map_ch12-15.py (a copy of the approved sample's map_all.py, extended). Burmese from the FINAL pi-3 text of this track only "
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
                f"- Keywords new in pi-3 (in neither mapping): {len(table) - len(known)} distinct.\n")
        nom_same, nom_diff, nom_new = nom_stats()
        f.write(f"- Instrumental keywords resolved through their nominative (Q1): the value is the pi-1 / pi-2 value of "
                f"the nominative for {len(nom_same)} distinct keyword-value pairs, {sum(nom_same.values())} uses; "
                f"the nominative is in neither mapping for {len(nom_new)} pairs, {sum(nom_new.values())} uses "
                f"(sample / T_CH12_15 values and the Q2 / M4 pairs); it differs from the nominative's pi-1 / pi-2 "
                f"value for {len(nom_diff)} pairs (below).\n\n")
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
        f.write("\n### Instrumental keywords whose value differs from the pi-1 / pi-2 value of their nominative\n\n"
                "| keyword | nominative | pi-3 value (uses) | pi-1 / pi-2 value(s) of the nominative | reason |\n"
                "|---|---|---|---|---|\n")
        for (kw, c, v), n in sorted(nom_diff.items()):
            f.write(f"| {kw} | {c} | {v} ({n}) | " + " · ".join(f"{x} ({m})" for x, m in prev_any(c).most_common(4))
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
