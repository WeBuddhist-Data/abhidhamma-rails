"""Burmese zero-shot of pi-6 (Yamaka, «အတွဲလိုက် မေးဖြေခြင်း»), group ch9-10a: 9-01 / 9-02 / 9-03 Dhammayamaka and
10-01 … 10-04 Indriyayamaka.

usage: python3 -I -X utf8 make_ch9-10a.py [chapter ...] [--misses]
Model: make_sample.py (approved sample) and make_ch2-02-4-5.py (sacca chapter: the same pavatti leads with moments,
aggamagga, nirodhasamāpanna …; functions COPIED here, never run). Imports my6_formulas.py unchanged and only EXTENDS
its tables in memory (add_subject / add_term / PLACES / H / COLO / LINES / SPELLING; who_my / body_my wrapped). Every
reused value is read / checked in the FINAL pi-1 … pi-5 rails texts at import (F.W, F.items: the run stops if a text
drifts) or logged as NEW (notes-ch9-10a.md). A sentence that no frame / table entry matches stops the run (Miss):
nothing is guessed. Each line is checked against its Pāli (dashes, «…», «[», item number, label, block ID, heading
level, no «?» «।» «:-», no Latin letters outside variant brackets, final «။»); a chapter is written only when every
line passed. --misses lists the unmatched lines and writes nothing.

The TABLES FOR THE OTHER INDRIYA AGENTS (10-05 … 10-13) are at the top: the 22 faculties (pi-2 ^2-221 order and
Burmese), their bare words, the person attributes of the indriya pavattivāra, the women frames (itthīnaṃ upapajjantīnaṃ
tāsaṃ), the citta-compound members of the moments, and the frame examples (IND_FRAMES, rendered by the real functions
at the end of this file: `--frames` prints them).
"""
import pathlib
import re
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import my6_formulas as F  # noqa: E402

ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-6_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters"
NAMES_OUT = ["9-01-dhammayamaka.md", "9-02-dhammayamaka.md", "9-03-dhammayamaka.md", "10-01-indriyayamaka.md",
             "10-02-indriyayamaka.md", "10-03-indriyayamaka.md", "10-04-indriyayamaka.md"]
W, C, END, PE, AND, DAT = F.W, F.C, F.END, F.PE, F.AND, F.DAT
NEW = {}          # every NEW string of this group (Pāli -> Burmese), for the notes and the check


def new(pali, my):
    NEW.setdefault(pali, my)
    return my


# =====================================================================================================================
# TABLE 1. The 22 faculties: pi-1 / pi-2 order and FINAL Burmese (pi-2 ^2-221, read at import; = pi-2 termbase)
# =====================================================================================================================
IND_H, IND = F.items("2", "^2-221")       # «စွမ်းရည် နှစ်ဆယ့်နှစ်ပါး», {cakkhundriyaṃ: «မျက်စိ၏ စွမ်းရည်», …}
IND_ORDER = ["cakkhundriyaṃ", "sotindriyaṃ", "ghānindriyaṃ", "jivhindriyaṃ", "kāyindriyaṃ", "manindriyaṃ",
             "itthindriyaṃ", "purisindriyaṃ", "jīvitindriyaṃ", "sukhindriyaṃ", "dukkhindriyaṃ", "somanassindriyaṃ",
             "domanassindriyaṃ", "upekkhindriyaṃ", "saddhindriyaṃ", "vīriyindriyaṃ", "satindriyaṃ", "samādhindriyaṃ",
             "paññindriyaṃ", "anaññātaññassāmītindriyaṃ", "aññindriyaṃ", "aññātāvindriyaṃ"]
assert list(IND) == IND_ORDER, "pi-2 ^2-221 order"
INDRIYA = W("1", "^1-1", "indriy", "စွမ်းရည်", key="indriya")             # indriyaṃ (sg.)
INDRIYA_PL = new("indriyā (plural)", INDRIYA + "တို့")                        # as khandhā «အစုအဝေးတို့» (pi-5)
OF_IND = "၏ " + INDRIYA                                                       # «X၏ စွမ်းရည်»
# bare words of the paṇṇattivāra (Pāli nominative -> (faculty, accusative or None)); Burmese = the faculty name without
# «၏ စွမ်းရည်» (cakkhu … mano as the dhātu / āyatana chapters; anaññātaññassāmīti without «ဟူသော စွမ်းရည်», quoted:
# the Pāli is itself a quoted phrase with «iti»)
BARE_IND = {"cakkhu": ("cakkhundriyaṃ", "cakkhuṃ"), "sotaṃ": ("sotindriyaṃ", None), "ghānaṃ": ("ghānindriyaṃ", None),
            "jivhā": ("jivhindriyaṃ", "jivhaṃ"), "kāyo": ("kāyindriyaṃ", "kāyaṃ"), "mano": ("manindriyaṃ", "manaṃ"),
            "itthī": ("itthindriyaṃ", "itthiṃ"), "puriso": ("purisindriyaṃ", "purisaṃ"),
            "jīvitaṃ": ("jīvitindriyaṃ", None), "sukhaṃ": ("sukhindriyaṃ", None), "dukkhaṃ": ("dukkhindriyaṃ", None),
            "somanassaṃ": ("somanassindriyaṃ", None), "domanassaṃ": ("domanassindriyaṃ", None),
            "upekkhā": ("upekkhindriyaṃ", "upekkhaṃ"), "saddhā": ("saddhindriyaṃ", "saddhaṃ"),
            "vīriyaṃ": ("vīriyindriyaṃ", None), "sati": ("satindriyaṃ", "satiṃ"), "samādhi": ("samādhindriyaṃ", "samādhiṃ"),
            "paññā": ("paññindriyaṃ", "paññaṃ"), "anaññātaññassāmīti": ("anaññātaññassāmītindriyaṃ", None),
            "aññaṃ": ("aññindriyaṃ", None), "aññātāvī": ("aññātāvindriyaṃ", None)}
ANANNATA = "anaññātaññassāmītindriyaṃ"
BARE_MY = {}
for _k, (_i, _acc) in BARE_IND.items():
    _m = IND[_i]
    if _i == ANANNATA:
        assert _m.endswith("ဟူသော " + INDRIYA)
        BARE_MY[_k] = F.quoted(_m[: -len("ဟူသော " + INDRIYA)])          # «“မသိရသေးသည်ကို သိရတော့မည်”»
    else:
        assert _m.endswith(OF_IND), _i
        BARE_MY[_k] = _m[: -len(OF_IND)]
new("anaññātaññassāmīti (bare word)", BARE_MY["anaññātaññassāmīti"])

# =====================================================================================================================
# TABLE 2. Indriya pavattivāra: person attributes (Pāli gen. pl. -> Burmese adverbial before the participle)
# A person group = [attributes …] [itthīnaṃ / purisānaṃ] participle; Burmese = the attributes in Pāli order, joined
# with a space, then the participle («ပြန်လည် ဖြစ်ပေါ်ဆဲ» / «စုတေဆဲ»), then the head: «မိန်းမတို့» (itthīnaṃ),
# «ယောက်ျားတို့» (purisānaṃ), else «…သူတို့». E.g. Sacakkhukānaṃ asotakānaṃ upapajjantānaṃ = «မျက်စိ ရှိလျက် နား
# မရှိဘဲ ပြန်လည် ဖြစ်ပေါ်ဆဲသူတို့» (as ch. 3 / ch2-02-4-5); Itthīnaṃ acakkhukānaṃ upapajjantīnaṃ tāsaṃ = «မျက်စိ မရှိဘဲ
# ပြန်လည် ဖြစ်ပေါ်ဆဲ မိန်းမတို့အား».
# =====================================================================================================================
WITH, WITHOUT = "ရှိလျက်", "မရှိဘဲ"                       # sa-X-ka / a-X-ka (as ch. 3 and ch2-02-4-5)
SA = {"cakkhu": BARE_MY["cakkhu"], "sota": BARE_MY["sotaṃ"], "ghāna": BARE_MY["ghānaṃ"],
      "citta": W("1", "^1-6", "cittaṃ", "စိတ်", key="citta"),
      "hetu": W("1", "^1-M2-2", "sahetukā dhammā", "အမြစ်", key="hetu (sahetuka / ahetuka)")}
SA_RE = re.compile(r"^(sa|a)(" + "|".join(SA) + r")kānaṃ$")
ITTHI = W("2", "^2-219", "itthindriyaṃ", "မိန်းမ", key="itthī")
PURISA = W("2", "^2-219", "purisindriyaṃ", "ယောက်ျား", key="puriso")
SOMANASSA = W("2", "^2-219", "somanassindriyaṃ", "ဝမ်းမြောက်မှု", key="somanassa")
UPEKKHA = W("2", "^2-219", "upekkhindriyaṃ", "ဥပေက္ခာ", key="upekkhā")
SADDHA = W("2", "^2-219", "saddhindriyaṃ", "ယုံကြည်မှု", key="saddhā")
NANA = W("1", "^1-1", "ñāṇasampayuttaṃ", "ဉာဏ်", key="ñāṇa")
SAMP = W("1", "^1-1", "ñāṇasampayuttaṃ", "နှင့် ယှဉ်တွဲ", key="-sampayutta")       # «Xနှင့် ယှဉ်တွဲသော»
VIPP = W("1", "^1-147", "ñāṇavippayuttaṃ", "နှင့် ကင်းကွာ", key="-vippayutta")      # «Xနှင့် ကင်းကွာသော»
SAHA = W("1", "^1-M1-7", "upekkhāsahagatā", "နှင့်အတူ", key="-sahagata / instr. (with)")   # «ဥပေက္ခာနှင့်အတူ ဖြစ်သော»
VINA = W("5", "^5-227", "vinā rūpena", "မပါဘဲ", key="vinā X")                             # «X မပါဘဲ» (as ch6-8)
NOT_BE = "မဟုတ်ဘဲ"                                                                       # na itthīnaṃ: «မိန်းမ မဟုတ်ဘဲ»
NOUNS = {"itthīnaṃ": ITTHI, "purisānaṃ": PURISA}            # gen. pl. nouns: head «…တို့», after «na» an attribute
INSTR = {"somanassena": SOMANASSA, "upekkhāya": UPEKKHA}   # instrumental: «Xနှင့်အတူ»; after «vinā» «X မပါဘဲ»
YUTTA = {"ñāṇasampayuttānaṃ": f"{NANA}{SAMP}လျက်", "ñāṇavippayuttānaṃ": f"{NANA}{VIPP}လျက်"}
IND_ATTR = {}                                               # for the notes / the other agents: every attribute form
for _k, _v in SA.items():
    IND_ATTR[f"sa{_k}kānaṃ"] = new(f"sa{_k}ka (attribute)", f"{_v} {WITH}")
    IND_ATTR[f"a{_k}kānaṃ"] = new(f"a{_k}ka (attribute)", f"{_v} {WITHOUT}")
for _k, _v in NOUNS.items():
    IND_ATTR["na " + _k] = new(f"na {_k} (attribute)", f"{_v} {NOT_BE}")
for _k, _v in INSTR.items():
    IND_ATTR[_k] = new(f"{_k} (attribute)", f"{_v}{SAHA}")
    IND_ATTR["vinā " + _k] = new(f"vinā {_k} (attribute)", f"{_v} {VINA}")
for _k, _v in YUTTA.items():
    IND_ATTR[_k] = new(f"{_k} (attribute)", _v)
REBORN = F.PART["upapajjantānaṃ"][0]                        # «ပြန်လည် ဖြစ်ပေါ်ဆဲ» (sample)
DYING = F.PART["cavantānaṃ"][0]                             # «စုတေဆဲ» (sample)
HEADS = {"upapajjantānaṃ": REBORN, "upapajjantīnaṃ": REBORN, "cavantānaṃ": DYING,
         "uppajjantīnaṃ": REBORN}                           # «uppajjantīnaṃ» (^6-10-, slip for upapajjantīnaṃ)
THEY_F = new("tāsaṃ (fem. «to them»)", "ထိုမိန်းမတို့")       # tāsaṃ: «ထိုမိန်းမတို့အား» (tesaṃ «ထိုသူတို့အား»)
PRO = dict(F.PRO)
PRO["tāsaṃ"] = THEY_F + DAT
PRO["tāsaṃ tattha"] = THEY_F + DAT + " " + F.FT["tattha"]
PROR = r"(?:tesaṃ tattha|tāsaṃ tattha|tattha|tesaṃ|tāsaṃ)"

# =====================================================================================================================
# TABLE 3. Moments: genitive members of «X-cittassa uppāda- / bhaṅgakkhaṇe» (pi-1 sampayutta / vippayutta pattern;
# several members: «Aနှင့် ယှဉ်တွဲ၍ Bနှင့် ကင်းကွာသော စိတ်», as ch2-02-4-5 «မဂ်နှင့် ကင်းကွာ၍ တပ်မက်မှုနှင့် ကင်းကွာသော စိတ်»)
# =====================================================================================================================
KUSALA, AKUSALA = F.BASE["kusala"][0], F.BASE["akusala"][0]
MEMBER = {"kusala": KUSALA, "akusala": AKUSALA, "saddhā": SADDHA, "somanassa": SOMANASSA, "upekkhā": UPEKKHA,
          "ñāṇa": NANA}
CITTA = SA["citta"]
COMP_RE = re.compile(r"^((?:" + "|".join(sorted(MEMBER, key=len, reverse=True)) + r")(?:sampayutta|vippayutta))+"
                     r"cittassa$")
COMP_ONE = re.compile(r"(" + "|".join(sorted(MEMBER, key=len, reverse=True)) + r")(sampayutta|vippayutta)")


def citta_compound(tok):
    """'kusalavippayuttaakusalavippayuttacittassa' -> «ကုသိုလ်နှင့် ကင်းကွာ၍ အကုသိုလ်နှင့် ကင်းကွာသော စိတ်» (no «၏»)."""
    if not COMP_RE.match(tok):
        return None
    parts = COMP_ONE.findall(tok[: -len("cittassa")])
    out = []
    for k, (m, y) in enumerate(parts):
        rel = SAMP if y == "sampayutta" else VIPP
        out.append(f"{MEMBER[m]}{rel}" + ("သော" if k == len(parts) - 1 else "၍"))
    return " ".join(out) + " " + CITTA


# =====================================================================================================================
# TABLE 4. Frame examples (Pāli sentence -> Burmese, rendered by the real frames: `make_ch9-10a.py --frames`)
# =====================================================================================================================
IND_FRAMES = [
    "(Ka) cakkhu cakkhundriyaṃ?", "(Ka) na cakkhu na cakkhundriyaṃ?", "(Kha) indriyā sotindriyaṃ?",
    "(Kha) na indriyā na sotindriyaṃ?", "(Ka) sotaṃ indriyanti?",
    "Dibbacakkhu paññācakkhu cakkhu, na cakkhundriyaṃ. Cakkhundriyaṃ cakkhu ceva cakkhundriyañca.",
    "Kāyindriyaṃ ṭhapetvā avaseso na kāyindriyaṃ, kāyo. Kāyañca kāyindriyañca ṭhapetvā avaseso na ceva kāyo na ca "
    "kāyindriyaṃ.",
    "Itthindriyaṃ na itthī, itthindriyaṃ. Itthiñca itthindriyañca ṭhapetvā avasesā na ceva itthī na ca itthindriyaṃ.",
    "Yaṃ sotaṃ indriyaṃ taṃ sotañceva indriyañca. Avasesaṃ sotaṃ na indriyaṃ.",
    "Sotindriyaṃ indriyañceva sotindriyañca. Avasesā indriyā na sotindriyaṃ.",
    "(Ka) yassa cakkhundriyaṃ uppajjati tassa sotindriyaṃ uppajjatīti?",
    "(Kha) yassa vā pana yattha manindriyaṃ na uppajjittha tassa tattha cakkhundriyaṃ na uppajjitthāti?",
    "Sacakkhukānaṃ asotakānaṃ upapajjantānaṃ tesaṃ cakkhundriyaṃ uppajjati, no ca tesaṃ sotindriyaṃ uppajjati.",
    "Sacakkhukānaṃ itthīnaṃ upapajjantīnaṃ tāsaṃ cakkhundriyañca uppajjati itthindriyañca uppajjati.",
    "Itthīnaṃ acakkhukānaṃ upapajjantīnaṃ tāsaṃ itthindriyaṃ uppajjati, no ca tāsaṃ cakkhundriyaṃ uppajjati.",
    "Sacakkhukānaṃ na purisānaṃ upapajjantānaṃ tesaṃ cakkhundriyaṃ uppajjati, no ca tesaṃ purisindriyaṃ uppajjati.",
    "Sacakkhukānaṃ vinā somanassena upapajjantānaṃ tesaṃ cakkhundriyaṃ uppajjati, no ca tesaṃ somanassindriyaṃ "
    "uppajjati.",
    "Sacakkhukānaṃ ñāṇavippayuttānaṃ upapajjantānaṃ tesaṃ cakkhundriyaṃ uppajjati, no ca tesaṃ paññindriyaṃ uppajjati.",
    "Somanassena upapajjantānaṃ pavatte somanassasampayuttasaddhāsampayuttacittassa uppādakkhaṇe tesaṃ tattha "
    "somanassindriyañca uppajjati saddhindriyañca uppajjati.",
    "Sabbesaṃ cittassa bhaṅgakkhaṇe somanassavippayuttaupekkhāvippayuttacittassa uppādakkhaṇe asaññasattānaṃ tesaṃ "
    "tattha somanassindriyañca na uppajjati upekkhindriyañca na uppajjati.",
    "Sabbesaṃ cavantānaṃ na itthīnaṃ na purisānaṃ upapajjantānaṃ tesaṃ itthindriyañca na uppajjati purisindriyañca "
    "na uppajjati.",
    "Rūpāvacare arūpāvacare tattha manindriyaṃ uppajjati, no ca tattha ghānindriyaṃ uppajjati.",
    "Uppajjati.",
]

# =====================================================================================================================
# Dhamma chapter terms (pi-1)
# =====================================================================================================================
DHAMMA, DHAMMA_PL = F.DHAMMA, F.DHAMMA_PL
DH_BASE = {"kusalā": KUSALA, "akusalā": AKUSALA, "abyākatā": F.ABY}
DH_SUBJ = {f"{k}_dhammā": f"{v} {DHAMMA_PL}" for k, v in DH_BASE.items()}      # «ကုသိုလ် သဘောတရားများ» (pi-1 ^1-M1-1)
W("1", "^1-M1-1", "kusalā dhammā", DH_SUBJ["kusalā_dhammā"])
W("1", "^1-M1-1", "akusalā dhammā", DH_SUBJ["akusalā_dhammā"])
W("1", "^1-M1-1", "abyākatā dhammā", DH_SUBJ["abyākatā_dhammā"])
PLURAL = set(DH_SUBJ)                                        # plural pavatti subjects: verbs take «ကြ»
for k, v in DH_SUBJ.items():
    F.add_subject(k, v)
    F.add_term(k, v, plural=True)
ABY_N = new("abyākatā (bare term, paṇṇattivāra)", f"{F.ABY} {F.THING}များ")     # the adjective needs a noun
for k, v in DH_BASE.items():                                 # bare kusalā … (plural); acc. kusalaṃ (Kusalaṃ ṭhapetvā …)
    F.add_term(k, ABY_N if k == "abyākatā" else v, plural=True, acc=k[:-1] + "aṃ")
F.add_term("dhammā", DHAMMA_PL, plural=True, acc="dhamme")
DH_GEN = {"kusalānaṃ": W("1", "^1-583", "kusalākusalānaṃ dhammānaṃ", f"{KUSALA} {DHAMMA}တို့", key="kusalānaṃ (dhammānaṃ)"),
          "akusalānaṃ": W("1", "^1-30", "akusalānaṃ dhammānaṃ", f"{AKUSALA} {DHAMMA}တို့", key="akusalānaṃ (dhammānaṃ)"),
          "kusalākusalānaṃ": W("1", "^1-583", "kusalākusalānaṃ dhammānaṃ", f"{KUSALA}{AND} {AKUSALA} {DHAMMA}တို့",
                               key="kusalākusalānaṃ (dhammānaṃ)")}
DH_SUB1 = re.compile(r"\b([Kk]usalā|[Aa]kusalā|[Aa]byākatā) ca dhammā\b")
DH_SUB2 = re.compile(r"\b([Kk]usalā|[Aa]kusalā|[Aa]byākatā) dhammā(?=ti\b|(?!\w))")
DH_SUDDHA = re.compile(r"^(?:na )?(?:[Kk]usalā|[Aa]kusalā|[Aa]byākatā) (?:na )?dhammā(?:ti)?[?.]$")   # suddhadhammavāra


def dh_join(s):
    """«kusalā dhammā» -> one token «kusalā_dhammā» (also «kusalā ca dhammā» -> «kusalā_dhammā ca»), so that the
    frames read a two-word subject as one term. Not in the suddhadhammavāra questions «(Ka) kusalā dhammā?» (= are
    the wholesome phenomena?: kusalā and dhammā are the two terms)."""
    if DH_SUDDHA.match(s):
        return s
    s = DH_SUB1.sub(lambda m: f"{m[1]}_dhammā ca", s)
    return DH_SUB2.sub(lambda m: f"{m[1]}_dhammā", s)


# =====================================================================================================================
# Indriya chapter terms
# =====================================================================================================================
for k in IND_ORDER:
    F.add_subject(k, IND[k])
    F.add_term(k, IND[k])
F.add_term("indriyaṃ", INDRIYA)
F.add_term("indriyā", INDRIYA_PL, plural=True)
for k, (i, acc) in BARE_IND.items():
    F.add_term(k, BARE_MY[k], acc=acc)
for a, b in (("cakkhū", "cakkhu"), ("satī", "sati"), ("samādhī", "samādhi"),      # «-ti» forms (cakkhūti, satīti …)
             ("anaññātaññāssāmīti", "anaññātaññassāmīti"),
             ("indriye", "indriyā"), ("aññātāviṃ", "aññātāvī"), ("anaññātaññassāmītiṃ", "anaññātaññassāmīti")):                          # slip ^6-10-3
    F.PT_ACC[a] = b
SPECIAL = {   # special subjects of the paṇṇatti sentences: identical Pāli and Burmese as ch2-02-4-5 (dhātu chapter)
    "Dibbacakkhu paññācakkhu": ("နတ်မျက်စိနှင့် ပညာမျက်စိတို့", True),
    "Dibbasotaṃ taṇhāsotaṃ": ("နတ်နားနှင့် တပ်မက်မှု ရေစီးတို့", True),
}
W("5", "^5-374", "dibbacakkhuṃ, paññācakkhu", "နတ်မျက်စိ၊ ပညာမျက်စိ", key="dibbacakkhu / paññācakkhu")
W("5", "^5-375", "dibbasotaṃ", "နတ်နား", key="dibbasotaṃ")
SOTA_WORD = "“သောတ” (နား သို့မဟုတ် ရေစီး)"          # sotaṃ in the Dibbasotaṃ taṇhāsotaṃ sentences (as ch. 3 / ch2-02-4-5)
F.SPELLING.add("viriyindiyaṃ (sī. syā.)")            # spelling only (pi-2 ^2-219 has the same variant as spelling)

# places: the planes (as ch. 3 / ch6-8)
F.PLACES["kāmāvacara"] = W("1", "^1-M2-93", "kāmāvacarā", "ကာမဘုံ", key="kāmāvacara (place)")
F.PLACES["rūpāvacara"] = W("1", "^1-M2-94", "rūpāvacarā", "သိမ်မွေ့သော ရုပ်ဘုံ", key="rūpāvacara (place)")
F.PLACES["arūpāvacara"] = F.PLACES["arūpa"]          # = «ရုပ်မရှိသော ဘုံ» (as ch. 3; pi-1 / pi-2)

# =====================================================================================================================
# verbs with plural subjects
# =====================================================================================================================
def V(w, form="stmt", pl=False):
    root, tense, neg = F.pali_verb(w)
    return F.my_verb(root, tense, neg, form, pl)


def not_so(root, tense, pl=False):
    """«no ca … na V»: «… မVသည်ကား မဟုတ်» (plural «မVကြသည်ကား မဟုတ်»; future «…လိမ့်မည်ကား မဟုတ်»)."""
    return F.my_verb(root, tense, True, pl=pl) + ("" if tense == "fut" else "သည်") + F.NOT_SO


def subj(x):
    return F.subj(x), x in PLURAL


VB = F.VB
CLR = F.CLR
Q_PAV = re.compile(rf"^{CLR} (?P<x>\S+) (?P<v1>{VB}) (?P<ft>tassa tattha|tassa|tattha) (?P<y>\S+) (?P<v2>{VB})[?.]$")
A_BUT = re.compile(rf"^(?P<who>.+?) (?P<pro>{PROR}) (?P<x>\S+) (?P<v1>{VB}), no ca (?P<pro2>{PROR}) (?P<y>\S+) "
                   rf"(?P<v2>{VB})\.$")
A_BOTH = re.compile(rf"^(?P<who>.+?) (?P<pro>{PROR}) (?P<x>\S+?)(?P<c1>ñca| ca)? (?P<v1>{VB}),? (?P<y>\S+?)"
                    rf"(?P<c2>ñca| ca)? (?P<v2>{VB})\.$")
A_SHORT = re.compile(rf"^(?P<v>{VB})\.$")


def q_pavatti(cl, x, v1, ft, y, v2):
    c = cl.lower()
    pre = ""
    if " vā pana" in c:
        pre = F.VA_PANA + " "
        c = c.replace(" vā pana", "")
    X, px = subj(x)
    Y, py = subj(y)
    return f"{pre}{F.CL[c][0]} {X} {V(v1, 'cl', px)}{C} {F.FT[ft]} {Y} {V(v2, 'q', py)}{END}"


def a_but(who, pro, x, v1, pro2, y, v2):
    X, px = subj(x)
    Y, py = subj(y)
    r2, t2, n2 = F.pali_verb(v2)
    v2m = not_so(r2, t2, py) if n2 else F.my_verb(r2, t2, True, pl=py)
    return f"{who_my(who, pro)} {X} {V(v1, pl=px)}{C} {F.BUT} {PRO[pro2]} {Y} {v2m}{END}"


def subj_ca(x, c):
    return subj(x + "ṃ" if c == "ñca" else x)


def a_both(m):
    if not (m["c1"] or m["c2"]):
        return None
    (X, px), (Y, py) = subj_ca(m["x"], m["c1"]), subj_ca(m["y"], m["c2"])
    also = "လည်း"
    return (f"{who_my(m['who'], m['pro'])} {X}{also if m['c1'] else ''} {V(m['v1'], pl=px)}{C} "
            f"{Y}{also if m['c2'] else ''} {V(m['v2'], pl=py)}{END}")


def pavatti_sentence(s):
    if s in F.ANSWERS:
        return F.ANSWERS[s]
    m = Q_PAV.match(s)
    if m:
        return q_pavatti(m["cl"], m["x"], m["v1"], m["ft"], m["y"], m["v2"])
    m = A_BUT.match(s)
    if m:
        return a_but(m["who"], m["pro"], m["x"], m["v1"], m["pro2"], m["y"], m["v2"])
    m = A_BOTH.match(s)
    if m:
        r = a_both(m)
        if r:
            return r
    m = A_SHORT.match(s)
    if m:
        pl = m["v"].endswith(("anti", "issanti"))   # the number of the verb form: «Uppajjittha.» = the sample's
        return V(m["v"], pl=pl) + END                  # «ဖြစ်ပေါ်ခဲ့သည်။» (identical Pāli), «Uppajjanti.» «…ကြသည်။»
    return None


# =====================================================================================================================
# leads (persons / moments / places before tesaṃ / tāsaṃ / tattha): the module first, else the lead parser
# (copied from make_ch2-02-4-5.py, extended with the indriya groups of TABLE 2 and the moments of TABLE 3)
# =====================================================================================================================
MOMENT = {"uppādakkhaṇe": W("5", "^5-366", "Uppādakkhaṇe vimuttaṃ, bhaṅgakkhaṇe", "ဖြစ်ခြင်း ခဏ၌", key="uppādakkhaṇe"),
          "bhaṅgakkhaṇe": W("5", "^5-366", "bhaṅgakkhaṇe", "ပြိုပျက်ခြင်း ခဏ၌")}
MAGGA = W("1", "^1-1039", "maggahetukā", "မဂ်", key="magga")
AGGA = W("2", "^2-1029", "agga", "အမြတ်ဆုံး", key="agga")
AGGAMAGGA = f"{AGGA} {MAGGA}"
SAMANGI = W("1", "^1-1039", "Ariyamaggasamaṅgissa", "နှင့် ပြည့်စုံသူ", key="-samaṅgī")
PATILABH = W("2", "^2-974", "paṭilabhati", "ရရှိ", key="paṭilabhati")
GET_PATH = f"{MAGGA}ကို {PATILABH}မည့်"                       # as ch2-02-4-5
ANANTARA = W("2", "^2-751", "samanantarā", "ချက်ချင်း နောက်၌", key="anantarā")
GEN = {   # genitive of a moment phrase -> Burmese (before «၏»): as ch2-02-4-5, plus the dhamma chapter
    "cittassa": CITTA,
    "aggamaggassa": AGGAMAGGA,
    "pacchimacittassa": f"နောက်ဆုံး {CITTA}",
}
GEN.update(DH_GEN)
PAVATTE = "ဘဝ တည်နေစဉ်"                                        # pavatte (as ch2-02-4-5)
VATTAMANE = W("5", "^5-556", "citte vattamāne", "စိတ် ဖြစ်နေစဉ်", key="citte vattamāne")
CITTE = {"dutiye citte": f"ဒုတိယ {VATTAMANE}", "dutiye akusale citte": f"ဒုတိယ {AKUSALA} {VATTAMANE}"}   # ch2-02-4-5
ARAHA_PL = W("5", "^5-546", "arahantānaṃ", "ရဟန္တာတို့", key="arahantānaṃ")
REL = {   # relative clauses and named persons (gen. pl.) -> Burmese person phrase (as ch2-02-4-5)
    "ye maggaṃ paṭilabhissanti": f"{GET_PATH}{F.THEM}",
    "ye ca maggaṃ paṭilabhissanti": f"{GET_PATH}{F.THEM}",
    "yassa cittassa anantarā aggamaggaṃ paṭilabhissanti": f"အကြင်{CITTA}၏ {ANANTARA} {AGGAMAGGA}ကို {PATILABH}မည့်{F.THEM}",
    "arahantānaṃ": ARAHA_PL,
    "aggamaggasamaṅgīnaṃ": f"{AGGAMAGGA}{SAMANGI}တို့",
    "pacchimacittasamaṅgīnaṃ": f"{GEN['pacchimacittassa']}{SAMANGI}တို့",
    "nirodhasamāpannānaṃ": "ချုပ်ငြိမ်းခြင်း သမာပတ်ကို ဝင်စားနေ" + F.THEM,
}
REL_RE = sorted(REL, key=lambda k: -len(k.split()))
SLIPS = {}


def gen_of(toks, j):
    """(Burmese genitive noun, tokens used) of a moment phrase at toks[j], or None."""
    for n in (1,):
        g = " ".join(toks[j:j + n])
        if g in GEN:
            return GEN[g], n
    c = citta_compound(toks[j]) if j < len(toks) else None
    if c:
        return c, 1
    return None


def _moment_at(toks, i):
    """[places-loc] [pavatte] GEN (uppāda|bhaṅga)kkhaṇe | … citte vattamāne -> (Burmese, next i) or None."""
    j, pre, places = i, [], []
    while j < len(toks) and F._place_form(toks[j]) and F._place_form(toks[j])[1] == "loc":
        places.append(F._place_form(toks[j])[0])
        j += 1
    if places:
        pre.append(F._join_places(places) + F.LOC)
    if j < len(toks) and toks[j] == "pavatte":
        pre.append(PAVATTE)
        j += 1
    if toks[j:j + 2] == ["tassa", "cittassa"] and j + 2 < len(toks) and toks[j + 2] in MOMENT:   # as ch2-02-4-5
        return " ".join(pre + [f"ထို{CITTA}၏ {MOMENT[toks[j + 2]]}"]), j + 3
    g = gen_of(toks, j) if j < len(toks) else None
    if g and j + g[1] < len(toks) and toks[j + g[1]] in MOMENT:
        return " ".join(pre + [f"{g[0]}၏ {MOMENT[toks[j + g[1]]]}"]), j + g[1] + 1
    for n in (3, 2):
        g = " ".join(toks[j:j + n])
        if g in CITTE and j + n < len(toks) and toks[j + n] == "vattamāne":
            return " ".join(pre + [CITTE[g]]), j + n + 1
    return None


def ind_group(toks, i):
    """TABLE 2 person group at toks[i] -> (Burmese, next i, feminine) or None."""
    j, advs, noun = i, [], None
    while j < len(toks):
        t = toks[j]
        nxt = toks[j + 1] if j + 1 < len(toks) else None
        if t == "na" and nxt in NOUNS:
            advs.append(IND_ATTR["na " + nxt])
            j += 2
        elif t == "vinā" and nxt in INSTR:
            advs.append(IND_ATTR["vinā " + nxt])
            j += 2
        elif t in INSTR or t in YUTTA or SA_RE.match(t):
            advs.append(IND_ATTR[t])
            j += 1
        elif t in NOUNS and noun is None:
            noun = t
            j += 1
        else:
            break
    if j == i or j >= len(toks) or toks[j] not in HEADS:
        return None
    head = toks[j]
    if head == "uppajjantīnaṃ":
        new("uppajjantīnaṃ (slip for upapajjantīnaṃ, ^6-10-)", REBORN)
    if (head in ("upapajjantīnaṃ", "uppajjantīnaṃ")) != (noun == "itthīnaṃ"):
        raise F.Miss("women frame: " + " ".join(toks[i:j + 1]))
    who = " ".join(advs + [HEADS[head]])
    who += f" {NOUNS[noun]}တို့" if noun else F.THEM
    return who, j + 1, noun == "itthīnaṃ"


def _is_module_tok(t):
    return t in ("sabbesaṃ", "itaresaṃ", "pacchimabhavikānaṃ") or t in F.PART or bool(F._place_form(t))


def lead_units(who):
    """A lead -> list of (kind, Burmese, feminine): P person, M moment, L place (brackets after their word)."""
    raw = [t.rstrip(",") for t in who.split()]
    toks, brs = [], {}
    for t in raw:
        if t.startswith("⟦"):
            brs.setdefault(len(toks) - 1, []).append(t)
        else:
            t = t[0].lower() + t[1:]
            toks.append(SLIPS.get(t, t))
    out = []
    for kind, txt, a, b, fem in _lead_units(toks):
        for k in range(a, b):
            for br in brs.get(k, []):
                txt += " " + br
        out.append((kind, txt, fem))
    return out


def _lead_units(toks):
    units, i, prefix = [], 0, ""
    while i < len(toks):
        t = toks[i]
        mo = _moment_at(toks, i)
        if mo:
            units.append(("M", prefix + mo[0], i, mo[1], False))
            prefix = ""
            i = mo[1]
            continue
        if t == "sabbesaṃ" and _moment_at(toks, i + 1):
            prefix = f"{F.ALL_OF}၏ "                                  # as ch2-02-4-5 «သူ အားလုံးတို့၏ …»
            i += 1
            continue
        hit = None
        for k in REL_RE:
            kt = k.split()
            if toks[i:i + len(kt)] == kt:
                hit = (REL[k], i + len(kt))
                break
        if hit:
            units.append(("P", hit[0], i, hit[1], False))
            i = hit[1]
            continue
        g = ind_group(toks, i)
        if g:
            units.append(("P", g[0], i, g[1], g[2]))
            i = g[1]
            continue
        if _is_module_tok(t):
            j = i
            while j < len(toks) and _is_module_tok(toks[j]) and not (j > i and _moment_at(toks, j)) \
                    and not (toks[j] == "sabbesaṃ" and _moment_at(toks, j + 1)) and not (j > i and ind_group(toks, j)):
                j += 1
            run = toks[i:j]
            if all(F._place_form(x) and F._place_form(x)[1] == "loc" for x in run):
                units.append(("L", F.place_my(" ".join(run)), i, j, False))
            else:
                k = i
                while run:
                    n = len(run)
                    txt = F._one_group(run)
                    units.append(("P", txt, k, k + n - len(run), False))
                    k += n - len(run)
            i = j
            continue
        raise F.Miss("lead token: " + t + " in " + " ".join(toks))
    if prefix:
        raise F.Miss("lead: dangling prefix")
    return units


def _join_p(parts):
    return parts[0] if len(parts) == 1 else f"{C} ".join(parts[:-1]) + f"{AND} " + parts[-1]


def join_lead(units):
    """Consecutive person units joined as the module joins groups («A၊ Bနှင့် C»), the rest with «၊ »."""
    segs, run = [], []
    for kind, txt, _ in units:
        if kind == "P":
            run.append(txt)
            continue
        if run:
            segs.append(_join_p(run))
            run = []
        segs.append(txt)
    if run:
        segs.append(_join_p(run))
    return f"{C} ".join(segs)


_who_module = F.who_my


def who_my(who, pro):
    """Module who_my first (pure person runs / places: identical to the sample); else the lead parser. «tāsaṃ» (the
    women): «…မိန်းမတို့အား»; after a final moment «ထိုမိန်းမတို့အား» (tesaṃ «ထိုသူတို့အား»)."""
    fem = pro.startswith("tāsaṃ")
    mpro = pro.replace("tāsaṃ", "tesaṃ")
    if not fem:
        try:
            return _who_module(who, mpro)
        except F.Miss:
            pass
    units = lead_units(who)
    out = join_lead(units)
    mb = re.search(r"((?: ⟦\d+⟧)+)$", out)
    tail = mb[1] if mb else ""
    out = out[: len(out) - len(tail)]
    last = units[-1][0]
    if fem and not (last == "M" or units[-1][2]):
        raise F.Miss("tāsaṃ after a group that is not women: " + who)
    if mpro == "tattha":
        if any(k != "L" for k, _, _ in units):
            raise F.Miss("lead: tattha after persons")
        return out + tail
    if last == "P":
        out += DAT
    elif last == "M":
        out += " " + (PRO["tāsaṃ"] if fem else F.PRO["tesaṃ"])
    else:
        raise F.Miss("lead: place before tesaṃ")
    return out + tail + (" " + F.FT["tattha"] if mpro == "tesaṃ tattha" else "")


F.who_my = who_my

# =====================================================================================================================
# paṇṇattivāra frames (copied from make_ch2-02-4-5.py pannatti2, the ch6-8 «X na Y, X.» frame)
# =====================================================================================================================
AV_N = {"avaseso": (F.AVASESA + " " + F.THING, False), "avasesaṃ": (F.AVASESA + " " + F.THING, False),
        "avasesā": (F.AVASESA_N, True)}
AVR = r"(?P<av>avaseso|avasesaṃ|avasesā)"
SPR = "(?P<s>" + "|".join(re.escape(k) for k in SPECIAL) + ")"
V_ = r"(?P<v> ⟦\d+⟧)?"
TK = r"[^\s,⟦]+"
X1 = re.compile(rf"^{SPR} (?P<a>\S+), na (?P<b>\S+)\.$")
X4 = re.compile(rf"^{SPR} na (?P<b>\S+), (?P<a>\S+)\.$")
Y1 = re.compile(rf"^(?P<s>\S+) ṭhapetvā {AVR} (?:(?P<k>{TK}) )?(?P<a>{TK}){V_}, na (?P<b>\S+)\.$")
Y1C = re.compile(rf"^(?P<s>\S+) ṭhapetvā {AVR} (?:(?P<k>{TK}) )?(?P<a>{TK}){V_} na (?P<b>\S+)\.$")     # comma missing
Y4 = re.compile(rf"^(?P<s>\S+) ṭhapetvā {AVR}{V_} (?:(?P<k>{TK}) )?na (?P<b>{TK})(?:, (?P<a>\S+))?\.$")
Y5 = re.compile(rf"^(?P<a>\S+?ñca|\S+ ca) (?P<b>\S+?ñca|\S+ ca) ṭhapetvā {AVR}{V_} na ceva (?P<a2>\S+) "
                rf"na ca (?P<b2>\S+)\.$")
Y3 = re.compile(rf"^Avasesā (?P<a>[^\s,⟦]+){V_} na (?P<b>\S+)\.$")
Y2 = re.compile(r"^(?P<x>\S+) (?P<a>\S+?)(?P<ce>ñceva| ceva) (?P<b>\S+?ñca|\S+ ca)\.$")
YAM_TAM = re.compile(r"^(?P<y>Yaṃ|Yo|Yā) (?P<x>\S+) indriyaṃ (?P<t>taṃ|so|sā) (?P<x2>\S+?)(?:ñceva| ceva) indriyañca\.$")
AV_SG = re.compile(rf"^(?P<av>Avasesaṃ|Avaseso) (?P<a>[^\s,⟦]+){V_} na (?P<b>\S+)\.$")
XNY = re.compile(r"^(?P<s>\S+) na (?P<b>\S+), (?P<a>\S+)\.$")
P_Q = re.compile(r"^(?P<n1>na )?(?P<a>\S+) (?P<n2>na )?(?P<b>\S+?)[?.]$")


YAM, TAM = "အကြင်", "ထို"                                 # yaṃ / yo / yā … taṃ / so / sā (as ch6-8 «အကြင်စိတ်»)
new("Yaṃ X indriyaṃ taṃ Xñceva indriyañca.", "အကြင်Xသည် စွမ်းရည် ဖြစ်၏၊ ထိုXသည် Xလည်း ဖြစ်၊ စွမ်းရည်လည်း ဖြစ်သည်။")


def T(w):
    if w.endswith("ūti"):
        w = w[:-3] + "u"
    return F.term(w)


def av_subj(av, k=None):
    if k:
        return f"{F.AVASESA} {T(k)[0]}", T(k)[1]
    return AV_N[av]


def pannatti_sentence(s):
    m = X1.match(s) or X4.match(s)
    if m:
        S, pl = SPECIAL[m["s"]]
        A = SOTA_WORD if (m["s"].startswith("Dibbasot") and m["a"] == "sotaṃ") else T(m["a"])[0]
        B = T(m["b"])[0]
        if m.re is X1:
            return f"{S}သည် {F.is_(A, pl)}{C} {F.isnt(B, pl)}{END}"
        return f"{S}သည် {F.isnt(B, pl)}{C} {F.is_(A, pl)}{END}"
    m = Y1.match(s) or Y1C.match(s)
    if m and not s.startswith(tuple(SPECIAL)):
        S, A, B = T(m["s"]), T(m["a"]), T(m["b"])
        sub, pl = av_subj(m["av"], m["k"])
        sep = C if m.re is Y1 else ""
        return f"{F.leave(S)} {sub}သည် {A[0]}{m['v'] or ''} {F.BE}{'ကြ' if pl else ''}သည်{sep} {F.isnt(B[0], pl)}{END}"
    m = Y4.match(s)
    if m and not s.startswith(tuple(SPECIAL)):
        S, B = T(m["s"]), T(m["b"])
        sub, pl = av_subj(m["av"], m["k"])
        tail = f"{C} {F.is_(T(m['a'])[0], pl)}" if m["a"] else ""
        return f"{F.leave(S)} {sub}သည်{m['v'] or ''} {F.isnt(B[0], pl)}{tail}{END}"
    m = Y5.match(s)
    if m:
        A, B, A2, B2 = (T(m[k]) for k in ("a", "b", "a2", "b2"))
        sub, pl = AV_N[m["av"]]
        return (f"{F.leave(A, B)} {sub}သည်{m['v'] or ''} {A2[0]}လည်း {F.NEGV[F.BE]}{C} {B2[0]}လည်း "
                f"{F.NEGV[F.BE]}{END}")
    m = Y3.match(s)
    if m:
        A, B = T(m["a"]), T(m["b"])
        return f"{F.AVASESA} {A[0]}သည်{m['v'] or ''} {F.isnt(B[0], A[1])}{END}"
    m = Y2.match(s)
    if m:
        X, B = T(m["x"]), T(m["b"])
        A = T(m["a"] + ("ñceva" if m["ce"] == "ñceva" else ""))
        return f"{X[0]}သည် {A[0]}လည်း {F.BE}{C} {B[0]}လည်း {F.BE}{F.ko(X)}သည်{END}"
    m = YAM_TAM.match(s)
    if m:       # «Yaṃ sotaṃ indriyaṃ taṃ sotañceva indriyañca.» (NEW frame)
        X = T(m["x"])[0]
        return (f"{YAM}{X}သည် {F.is_(INDRIYA, False)[:-len('သည်')]}၏{C} {TAM}{X}သည် {X}လည်း {F.BE}{C} "
                f"{INDRIYA}လည်း {F.BE}သည်{END}")
    m = AV_SG.match(s)
    if m:       # «Avasesaṃ sotaṃ na indriyaṃ.» / «Avaseso kāyo na indriyā.» (singular avasesa + noun)
        A, B = T(m["a"]), T(m["b"])
        return f"{F.AVASESA} {A[0]}သည်{m['v'] or ''} {F.isnt(B[0], A[1])}{END}"
    m = XNY.match(s)
    if m and not s.startswith(tuple(SPECIAL)):
        try:
            S, A, B = T(m["s"]), T(m["a"]), T(m["b"])
        except F.Miss:
            S = None
        if S:
            return f"{S[0]}သည် {F.isnt(B[0], S[1])}{C} {F.is_(A[0], S[1])}{END}"
    m = P_Q.match(s[0].lower() + s[1:])
    if m and bool(m["n1"]) == bool(m["n2"]):
        try:
            A, B = T(m["a"]), T(m["b"])
        except F.Miss:
            return None
        if m["n1"]:
            return f"{A[0]} {F.NEGV[F.BE]}သော {F.THING}သည် {B[0]} {F.NEGV[F.BE]}သလော{END}"
        return f"{A[0]}သည် {B[0]} {F.BE}{F.ko(A)}သလော{END}"
    return None


# =====================================================================================================================
# bhāvanāvāra (9-03): yo kusalaṃ dhammaṃ bhāveti so akusalaṃ dhammaṃ pajahatīti?
# =====================================================================================================================
BHAVETI = W("5", "^5-390", "maggaṃ bhāvetīti", "ပွားများ", key="bhāveti")
PAJAHATI = W("5", "^5-317", "pajahaṃ", "ပယ်", key="pajahati")
BHAVANA = W("1", "^1-M1-8", "bhāvanāya pahātabbā", "ဘာဝနာ ပွားများခြင်း", key="bhāvanā")
YO = ("အကြင်သူသည်", "ထိုသူသည်")                              # yo … so … (as ch2-02-4-5 / ch6-8)
DH_ACC = {"kusalaṃ dhammaṃ": f"{KUSALA} {DHAMMA}ကို", "akusalaṃ dhammaṃ": f"{AKUSALA} {DHAMMA}ကို"}
new("kusalaṃ / akusalaṃ dhammaṃ (acc.)", DH_ACC["kusalaṃ dhammaṃ"])
BV = r"(?:na bhāvet\w*|bhāvet\w*|nappajah\w*|pajah\w*)"
Q_BHA = re.compile(rf"^(?P<yo>[Yy]o vā pana|[Yy]o) (?P<x>a?kusalaṃ dhammaṃ) (?P<v1>{BV}) so (?P<y>a?kusalaṃ dhammaṃ) "
                   rf"(?P<v2>{BV})[?.]$")


def b_verb(w, form):
    neg = w.startswith(("na ", "nap"))
    stem = BHAVETI if "bhāvet" in w else PAJAHATI
    v = (F.NEG if neg else "") + stem
    if form == "cl":
        return v if neg else v + "၏"
    return v + "သလော"


def bhavana_sentence(s):
    m = Q_BHA.match(s)
    if m:
        pre = F.VA_PANA + " " if "vā pana" in m["yo"] else ""
        return (f"{pre}{YO[0]} {DH_ACC[m['x']]} {b_verb(m['v1'], 'cl')}{C} {YO[1]} {DH_ACC[m['y']]} "
                f"{b_verb(m['v2'], 'q')}{END}")
    return None


# =====================================================================================================================
# headings, colophons, notes, whole lines
# =====================================================================================================================
UN = f"{F.UPPADA}{AND} {F.NIRODHA}"
HEADS_NEW = {
    "Pavattivāro": F.vara(F.PAVATTI),
    "Uppādavāro": F.vara(F.UPPADA),
    "Nirodhavāro": F.vara(F.NIRODHA),
    "Uppādanirodhavāro": F.vara(UN),
    "Suddhadhammavāro": F.vara(f"{F.SUDDHA} {DHAMMA}", False),
    "Suddhadhammamūlacakkavāro": F.vara(f"{F.SUDDHA} {DHAMMA}{F.BASED} {F.CAKKA}", False),
    "Suddhindriyavāro": F.vara(f"{F.SUDDHA} {INDRIYA}", False),
    "Suddhindriyamūlacakkavāro": F.vara(f"{F.SUDDHA} {INDRIYA}{F.BASED} {F.CAKKA}", False),
    "Bhāvanāvāro": F.vara(BHAVANA),
}
HEADS_NEW["3 Suddhadhammavāro"] = "3 " + HEADS_NEW["Suddhadhammavāro"]
HEADS_NEW["4 Suddhadhammamūlacakkavāro"] = "4 " + HEADS_NEW["Suddhadhammamūlacakkavāro"]
for k, v in HEADS_NEW.items():
    if k in F.H and F.H[k] != v:
        raise SystemExit("heading clash " + k)
    F.H[k] = new(k + " (heading)", v) if k in ("Suddhadhammavāro", "Suddhadhammamūlacakkavāro", "Suddhindriyavāro",
                                               "Suddhindriyamūlacakkavāro", "Bhāvanāvāro") else v
COLO_NEW = {
    "Bhāvanāvāro.": F.vara(BHAVANA) + END,
    "Pavattivāro niṭṭhito.": F.finished(F.vara(F.PAVATTI)),
    "Uppādavāro.": F.vara(F.UPPADA) + END,
    "Nirodhavāro.": F.vara(F.NIRODHA) + END,
    "Uppādanirodhavāro.": F.vara(UN) + END,
}
for k, v in COLO_NEW.items():
    F.COLO.setdefault(k, v)
NOTES = {}
for k in IND_ORDER:      # (Cakkhundriyamūlakaṃ) «(မျက်စိ၏ စွမ်းရည်ကို အခြေခံ၍)» (as ch. 3 «(… နယ်ပယ်ကို အခြေခံ၍)»)
    NOTES[f"({k[0].upper()}{k[1:-1]}mūlakaṃ)"] = f"({IND[k]}{F.BASED})"
new("(Xindriyamūlakaṃ)", "(X၏ စွမ်းရည်ကို အခြေခံ၍)")
LINES_CH = {
    "Abhidhammapiṭake": F.ABHI,
    "niddeso": F.NIDDESO,                    # ^6-9-16 «(Kha) niddeso» as a text line (heading without «#»)
    "paccanīkapuggalokāsā": F.H["paccanīkapuggalokāsā"],
    "anulomapuggalokāsā": F.H["anulomapuggalokāsā"],
    "Bāvīsatindriyāni – " + ", ".join(k + ("⟦v⟧" if k == "vīriyindriyaṃ" else "") for k in IND_ORDER) + ".":
        f"{IND_H} – " + f"{C} ".join(IND[k] + ("{v}" if k == "vīriyindriyaṃ" else "") for k in IND_ORDER) + END,
}
F.LINES.update(LINES_CH)

# =====================================================================================================================
# «…pe…» lines (copied from make_ch2-02-4-5.py: each piece between «…» translated, every «…» kept)
# =====================================================================================================================
FR_Q_PAV = re.compile(rf"^{CLR}(?: (?P<x>\S+) (?P<v1>{VB}))?(?: (?P<ft>tassa tattha|tassa|tattha) (?P<y>\S+))?$")
FR_ANS = re.compile(rf"^(?P<who>.+?) (?P<pro>{PROR}) (?P<x>\S+) (?P<v>{VB})$")
FR_VB = re.compile(rf"^(?P<v>{VB})$")
FR_YV = re.compile(rf"^(?P<y>\S+) (?P<v>{VB})$")


def fragment(p):
    """A piece between «…» that no sentence frame takes. With «?» it ends «…လော။» / «…သလော။», with «.» «။»."""
    p = dh_join(p)
    q, st = p.endswith("?"), p.endswith(".")
    t = p[:-1] if (q or st) else p
    endq = "လော" + END if q else (END if st else "")
    if t in NOTES:
        return NOTES[t] + (END if st else "")
    m = FR_VB.match(t)
    if m and q:
        return V(m["v"], "q", m["v"].endswith(("anti", "antīti", "issanti", "issantīti"))) + END
    m = FR_YV.match(t)
    if m and q and m["y"] in F.SUBJ:                            # «… Y uppajjatīti?» (the end of a cut question)
        Y, py = subj(m["y"])
        return f"{Y} {V(m['v'], 'q', py)}{END}"
    m = FR_Q_PAV.match(t)
    if m:
        c = m["cl"].lower()
        pre = F.VA_PANA + " " if " vā pana" in c else ""
        c = c.replace(" vā pana", "")
        out = f"{pre}{F.CL[c][0]}"
        if m["x"]:
            X, px = subj(m["x"])
            out += f" {X} {V(m['v1'], 'cl', px)}"
        if m["ft"]:
            out += f"{C} {F.FT[m['ft']]} {subj(m['y'])[0]}"
        return out + endq
    m = re.fullmatch(rf"(?P<who>.+?) (?P<pro>{PROR})(?: (?P<x>\S+))?", t)
    if m and not q and (not m["x"] or m["x"] in F.SUBJ):
        return who_my(m["who"], m["pro"]) + (f" {subj(m['x'])[0]}" if m["x"] else "") + (END if st else "")
    m = FR_ANS.match(t)
    if m and not q:
        X, px = subj(m["x"])
        return f"{who_my(m['who'], m['pro'])} {X} {V(m['v'], pl=px)}" + (END if st else "")
    if t in F.SUBJ:                                             # a bare subject between «…» («… paññindriyaṃ…»)
        return subj(t)[0] + endq
    raise F.Miss("fragment: " + p)


def piece_my(p):
    p0 = p.strip()
    if not p0:
        return ""
    if p0 in (".", "?"):
        return END if p0 == "." else "လော" + END
    lead = ""
    if p0.startswith("? "):
        lead, p0 = "လော" + END + " ", p0[2:]
    elif p0.startswith(". "):
        lead, p0 = END + " ", p0[2:]
    sents = F.SPLIT.split(p0)
    out = []
    for k, s in enumerate(sents):
        last = k == len(sents) - 1
        if s == "Āmantā" and last:
            out.append(F.YES[:-1])
            continue
        open_ = last and not s.endswith((".", "?", ")"))
        try:
            r = sentence_my(s + "." if open_ else s)
            if open_:
                r = r[:-1]
        except F.Miss:
            r = fragment(s)
        out.append(r)
    return lead + " ".join(out)


def pe_line(line):
    s = line.replace("…pe…", PE).replace("…Pe…", PE)
    out = []
    parts = s.split(PE)
    for n, p in enumerate(parts):
        q = piece_my(p)
        lead = " " if p.startswith(" ") and q and not q.startswith(("လော", END)) else ""
        trail = " " if p.endswith(" ") and p.strip() and n < len(parts) - 1 else ""
        out.append(lead + q + trail)
    return PE.join(out)


# =====================================================================================================================
# engine
# =====================================================================================================================
NOTE_END = re.compile(r"^(?P<a>.+?) (?P<n>\([^)]*\))$")


def sentence_my(s):
    s = dh_join(s)
    if s in NOTES:
        return NOTES[s]
    for fn in (pavatti_sentence, bhavana_sentence, pannatti_sentence):
        r = fn(s)
        if r:
            return r
    r = F.pannatti_sentence(s)
    if r:
        return r
    raise F.Miss("no frame for: " + s)


def body_my(line):
    if line in F.COLO:
        return F.COLO[line]
    if line in F.LINES:
        return F.LINES[line]
    vars_ = []

    def keep(m):
        vars_.append(F.variant(m[1]))
        return f" ⟦{len(vars_) - 1}⟧"
    key = F.BRACKET.sub("⟦v⟧", line)
    if key in F.LINES:
        return F.LINES[key].format(v=" " + F.variant(F.BRACKET.search(line)[1]))
    line = F.BRACKET.sub(keep, line)
    if "…" in line:
        out = pe_line(line)
    else:
        sents = F.SPLIT.split(line)
        outs = []
        for s in sents:
            m = NOTE_END.match(s)
            if m and m["n"] in NOTES:                 # «… Āmantā. (Cakkhundriyamūlakaṃ)»
                outs.append(sentence_my(m["a"]) + " " + NOTES[m["n"]])
            else:
                outs.append(sentence_my(s))
        out = " ".join(outs)
    for i, v in enumerate(vars_):
        out = out.replace(f"⟦{i}⟧", v)
    return out


F.body_my = body_my


# =====================================================================================================================
# per-line check (make_sample.py), run
# =====================================================================================================================
def num(l):
    m = re.match(r"\((\d+)\)", l)
    return m[1] if m else None


def line_check(p, m):
    e = []
    for mark in ("–", "—"):
        if p.count(mark) != m.count(mark):
            e.append(f"dash {mark}")
    if p.replace("…pe…", "…").replace("…Pe…", "…").count("…") != m.count("…"):
        e.append("ellipsis")
    if p.count("[") != m.count("[") or p.count("]") != m.count("]"):
        e.append("brackets")
    if num(p) != num(m):
        e.append("item number")
    lp, lm = F.LABEL_RE.match(p), re.match(r"^\(([က-အ])\) ", m)
    if bool(lp) != bool(lm) or (lp and F.AKKHARA[lp[1]] != lm[1]):
        e.append("label")
    ip, im = F.ID_RE.search(p), F.ID_RE.search(m)
    if bool(ip) != bool(im) or (ip and ip[1] != im[1]):
        e.append("block ID")
    hp, hm = re.match(r"^(#+) ", p), re.match(r"^(#+) ", m)
    if (hp and hp[1]) != (hm and hm[1]):
        e.append("heading level")
    for bad in ("?", "।", ":-"):
        if bad in m:
            e.append(f"«{bad}»")
    if re.search(r"[A-Za-zāīūṃṅñṭḍṇḷ]", re.sub(r"\[[^\]]*\]", "", F.strip_id(m))):
        e.append("Latin letters")
    if not hm and not F.strip_id(m).rstrip().endswith(("။", "…", ")")) and F.strip_id(p).rstrip()[-1:] in ".?":
        e.append("no final «။»")
    return e


def run(name):
    src = (PALI / name).read_text(encoding="utf-8-sig")
    out = F.translate_text(src)
    nbad = 0
    P = [l for l in src.splitlines() if l.strip()]
    M = [l for l in out.splitlines() if l.strip()]
    if len(P) != len(M):
        print(f"{name}: {len(P)} vs {len(M)} lines")
        nbad += 1
    for i, (p, m) in enumerate(zip(P, M), 1):
        e = line_check(p, m)
        if e:
            nbad += 1
            print(f"{name}:{i} {e}\n  {p}\n  {m}")
    return out, nbad


def misses(name):
    n = 0
    for i, l in enumerate((PALI / name).read_text(encoding="utf-8-sig").splitlines(), 1):
        try:
            F.translate_line(l)
        except (F.Miss, KeyError, IndexError, AttributeError, TypeError) as ex:
            n += 1
            print(f"{name}:{i} {type(ex).__name__} {ex}")
    return n


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    names = args or NAMES_OUT
    if "--frames" in sys.argv:
        for x in IND_FRAMES:
            print(f"- {x} = {F.translate_line(x)}")
        sys.exit(0)
    if "--misses" in sys.argv:
        print("misses:", sum(misses(n) for n in names))
        sys.exit(0)
    OUT.mkdir(parents=True, exist_ok=True)
    for n in names:
        if n not in NAMES_OUT:
            sys.exit(f"{n}: not one of this agent's chapters")
        text, nbad = run(n)
        if nbad:
            sys.exit(f"{n}: {nbad} bad lines, nothing written")
        (OUT / n).write_text(text, encoding="utf-8")
        print(f"{n}: written, {len([l for l in text.splitlines() if l.strip()])} lines")
