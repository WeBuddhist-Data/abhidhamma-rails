"""Burmese zero-shot of pi-5 (Kathāvatthu, «အငြင်းပွားရာ အကြောင်းအရာများကို ဆွေးနွေးခြင်း»), chapters 17-20:
17-navamavaggo, 18-dasamavaggo, 19-ekadasamavaggo, 20-dvadasamavaggo.

usage: python3 -I -X utf8 make_ch17-20.py [chapter ...] [--misses] [--units]
Model: the approved sample. Every line is generated from the Pāli by my5_formulas.translate_line() through the
frames, rules and tables of my5_formulas.py, make_sample.py, make_ch6-10.py and make_ch11-12.py (all imported READ
ONLY: they install their tables at import and write nothing; their __main__ never runs) and the tables of THIS
script, which extends them IN MEMORY only.
  * PROP_X (propositions), QUOTE_X (sutta quotations), SENT_X (unique sentences), LINES_X (uddāna),
    HEAD_X / COLO_X (headings, colophons);
  * NEW: every new recurring term or phrase (Pāli = Burmese), copied into notes-ch17-20.md.
A unit no frame / rule / table matches stops the run (Miss): nothing is guessed.
"""
import importlib.util
import pathlib
import re
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
_spec = importlib.util.spec_from_file_location("make_ch11_12", HERE / "make_ch11-12.py")
P11 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(P11)         # installs make_sample + make_ch6-10 + make_ch11-12 tables; writes nothing
P6 = P11.P6
MS = P6.MS
F = P6.F
from my5_formulas import V, FR, Cl, C, END, PE  # noqa: E402

PALI = MS.PALI
OUT = MS.OUT
NAMES_OUT = ["17-navamavaggo.md", "18-dasamavaggo.md", "19-ekadasamavaggo.md", "20-dvadasamavaggo.md"]
W = F.witness
PROP_X, QUOTE_X, SENT_X, LINES_X, HEAD_X, COLO_X, ANCHOR_X = {}, {}, {}, {}, {}, {}, {}
VAR_X, REF_X, REF_NOTE_X, BR_X = {}, {}, {}, {}
NEW = {}
key, VV = P11.key, P11.VV


def new(pali, my):
    NEW.setdefault(pali, my)
    return my


def section(pali, my):
    HEAD_X[pali] = my
    COLO_X[f"{pali} niṭṭhitā"] = F.DONE.format(my)
    new(pali, my)
    return my


def P(pali, cl):
    k = key(pali)
    PROP_X[k[:1].lower() + k[1:]] = cl
    return cl


def S(pali, my):
    SENT_X[key(pali)] = my
    return my


def Q(pali, my):
    QUOTE_X[key(pali)] = my
    return my


KATHA = F.KATHA_W
EXIST, NEXIST = P6.EXIST, P6.NEXIST


# ===================================================================================== shared vocabulary (ch17-20)
YES_V = (EXIST, NEXIST)
SK = F.SANKHARA.my                                                    # saṅkhārā (sample noun «ပြုပြင်ဖန်တီးမှုတို့»)
KH = F._KH                                                            # rūpakkhandho … (pi-2)
AY = F._AY
AMATA = "အမြိုက်"                                                     # amata (ch12 «အမြိုက် စည်»)
NIB = F.NIBBANA
PUTHU = P6.PUTHU
ARAHA = F.ARAHA
FET = "နှောင်ကြိုး"                                                    # saṃyojana (pi-1 cluster)
ANUS = P11.ANUSAYA                                                    # anusaya «ကိန်းအောင်းခြင်း» (pi-2)
MF = {  # mental factors and kilesas (pi-1 ^1-1 / ^1-1235 FINAL; ch8 / ch10 / ch11 tables)
    "phasso": "တွေ့ထိမှု", "vedanā": F.VEDANA.my, "saññā": F.SANNA.my, "cetanā": "စေ့ဆော်မှု", "cittaṃ": "စိတ်",
    "saddhā": P11.IND["saddhā"], "vīriyaṃ": "ဝီရိယ", "sati": P6.SATI, "samādhi": "သမာဓိ", "paññā": "ပညာ",
}
MF.update(P6.KIL)
W("1", "^1-1", "vitakko hoti", "စတင်ကြံစည်မှု")
W("1", "^1-1", "pīti hoti", "ပီတိ")
W("1", "^1-1", "sukhaṃ hoti", "သာယာမှု")
W("1", "^1-417", "domanassindriyaṃ", "စိတ်ဆင်းရဲမှု")
W("1", "^1-153", "upekkhā hoti", "ဥပေက္ခာ")
VIT, VIC = "စတင်ကြံစည်မှု", "ဆက်လက်သုံးသပ်မှု"                        # vitakka / vicāra (style §core)


def mlist(pali, sep=None):
    """«phasso vedanā …» (space-separated nouns of MF) -> «တွေ့ထိမှု၊ ခံစားမှု …»."""
    return f"{C} ".join(MF[w] for w in pali.split())


AR_Y = "အာရုံ"                                                        # ārammaṇa (pi-1 sārammaṇā «အာရုံ ရှိသော»)
W("1", "^1-M2-55", "sārammaṇā dhammā", "အာရုံ ရှိသော")
W("1", "^1-M2-55", "anārammaṇā dhammā", "အာရုံ မရှိသော")


def ar(subj, neg):
    """S sārammaṇo / anārammaṇo = «Sသည် အာရုံ ရှိသော / မရှိသော အရာ (ဖြစ်)» (harmonise B6: the predicate of ch15 /
    ch16 / ch23 / ch24 / ch27, F.SARAMMANA_TH; was «Sသည် အာရုံ ရှိ / မရှိ»)."""
    return V(f"{subj}သည် {F.SARAMMANA_TH[int(bool(neg))]}")


ADV = ["စိတ်ကို လှည့်ဆောင်ခြင်း", "စိတ်ညွတ်ခြင်း", "စိတ်ကို ဆောင်ခြင်း", "နှလုံးသွင်းခြင်း"]   # pi-2 ^2-766
W("2", "^2-766", "āvaṭṭanā vā ābhogo vā samannāhāro vā manasikāro",
  "စိတ်ကို လှည့်ဆောင်ခြင်းဖြစ်စေ၊ စိတ်ညွတ်ခြင်းဖြစ်စေ၊ စိတ်ကို ဆောင်ခြင်းဖြစ်စေ၊ နှလုံးသွင်းခြင်း")
ADV += F.AVATTANA[4:]          # cetanā, patthanā, paṇidhi (harmonise B6: = ch15; paṇidhi was «ဆုတောင်းမှု»)
assert ADV == F.AVATTANA
ADV_ALL = f"{C} ".join(ADV)
ADV_PE = f"{ADV[0]}{C} {ADV[1]}… {ADV[-1]}"                          # āvaṭṭanā ābhogo…pe… paṇidhi
ADV_PE1 = f"{ADV[0]}… {ADV[-1]}"                                      # āvaṭṭanā…pe… paṇidhi
new("āvaṭṭanā ābhogo samannāhāro manasikāro cetanā patthanā paṇidhi", ADV_ALL)
THAT = "ထိုအရာ၌"                                                      # tassa / tāya (atthi tassa …)
for _t in ("tassa", "tāya"):
    P(f"atthi {_t} āvaṭṭanā ābhogo samannāhāro manasikāro cetanā patthanā paṇidhi", V(f"{THAT} {ADV_ALL}", EXIST))
    P(f"natthi {_t} āvaṭṭanā ābhogo samannāhāro manasikāro cetanā patthanā paṇidhi",
      V(f"{THAT} {ADV_ALL}", EXIST, True))
    for _pe, _m in (("āvaṭṭanā ābhogo… paṇidhi", ADV_PE), ("āvaṭṭanā… paṇidhi", ADV_PE1)):
        P(f"atthi {_t} {_pe}", V(f"{THAT} {_m}", EXIST))
        P(f"natthi {_t} {_pe}", V(f"{THAT} {_m}", EXIST, True))
SAMODH2 = FR(f"{P6._MENT['phasso']} {F.NUM_MY[2]}{F.CL}")               # dvinnaṃ phassānaṃ…pe… (series head)
P("dvinnaṃ phassānaṃ", SAMODH2)
P("dvinnaṃ cittānaṃ samodhānaṃ hoti", V(f"စိတ် {F.NUM_MY[2]}{F.CL}တို့၏ ပေါင်းဆုံခြင်း"))
KAKHP = "အဘယ် အစုအဝေး၌ အကျုံးဝင်သနည်း"                               # katamakkhandhapariyāpanno
PARIY = "၌ အကျုံးဝင်"                                                 # -pariyāpanna (pi-1 «… အကျုံးဝင်သော»)
for _g in ("o", "an", "ā"):
    S(f"Katamakkhandhapariyāpann{_g}ti?", KAKHP + END)
    S(f"Saṅkhārakkhandhapariyāpann{_g}ti.", f"{KH['saṅkhārakkhandho']}{PARIY}သည်{END}")
new("katamakkhandhapariyāpanno? saṅkhārakkhandhapariyāpanno", f"{KAKHP} / {KH['saṅkhārakkhandho']}{PARIY}သည်")
SKP = f"{KH['saṅkhārakkhandho']}{PARIY}သော"                             # saṅkhārakkhandhapariyāpanna (attribute)
KH3 = f"{KH['vedanākkhandho']}{C} {KH['saññākkhandho']}{C} {KH['viññāṇakkhandho']}"
EK = P11.EK                                                           # ekadeso «တစ်စိတ်တစ်ဒေသ»
for _k, _m in (("saṅkhārakkhandho", KH["saṅkhārakkhandho"]),
               ("vedanākkhandho saññākkhandho viññāṇakkhandho", KH3)):
    P(f"{_k} anārammaṇo", ar(_m, True))
    P(f"{_k} sārammaṇo", ar(_m, False))
    P(f"{_k} ekadeso sārammaṇo ekadeso anārammaṇo",
      V(f"{_m}၏ {EK}သည် {F.SARAMMANA_TH[0]} ဖြစ်၍ {EK}သည် {F.SARAMMANA_TH[1]}"))     # harmonise B6
new("X ekadeso sārammaṇo ekadeso anārammaṇo", f"X၏ {EK}သည် {F.SARAMMANA_TH[0]} ဖြစ်၍ {EK}သည် {F.SARAMMANA_TH[1]} ဖြစ်")
RNC = f"ရုပ်{C} {NIB}{C} {AY['cakkhāyatanaṃ']}… {AY['phoṭṭhabbāyatanaṃ']}"
P("rūpaṃ nibbānaṃ cakkhāyatanaṃ… phoṭṭhabbāyatanaṃ", V(RNC))

# ===================================================================================== 17. Navamavaggo
section("Navamavaggo", f"{F.ORD_MY[9]} {F.VAGGA_W}")
COLO_X["Navamavaggo"] = HEAD_X["Navamavaggo"]

# --- 84. Ānisaṃsadassāvīkathā
ANIS = new("ānisaṃsadassāvī", "အကျိုးကျေးဇူးကို ရှုမြင်သူ")
section("(84) 1. Ānisaṃsadassāvīkathā", f"(84) 1. {ANIS}အကြောင်း {KATHA}")
section("Ānisaṃsadassāvīkathā", f"{ANIS}အကြောင်း {KATHA}")
P("ānisaṃsadassāvissa saṃyojanānaṃ pahānaṃ", V(f"{ANIS}၏ {FET}တို့ကို ပယ်ခြင်း"))
new("ānisaṃsadassāvissa saṃyojanānaṃ pahānaṃ", f"{ANIS}၏ {FET}တို့ကို ပယ်ခြင်း ဖြစ်")
PAHIY = ("ပယ်ခံရကြ", "ပယ်ခံ မရကြ")                                     # pahīyanti (ch12)
ASPECT = [("anicca", "မမြဲ"), ("dukkha", "ဆင်းရဲ"), ("roga", "ရောဂါ"), ("gaṇḍa", "အနာ"), ("salla", "ငြောင့်"),
          ("agha", "ဒုက္ခ ဖိစီးမှု"), ("ābādha", "ဖျားနာမှု"), ("para", "သူစိမ်း"), ("paloka", "ပျက်စီးတတ်သော အရာ"),
          ("īti", "ဘေးဒဏ်"), ("upaddava", "ဥပဒ်"), ("bhaya", "ကြောက်ဖွယ်"), ("upasagga", "ဘေးအန္တရာယ်"),
          ("cala", "လှုပ်ရှားတတ်သော အရာ"), ("pabhaṅgu", "ပြိုပျက်တတ်သော အရာ"), ("addhuva", "မခိုင်မြဲသော အရာ"),
          ("atāṇa", "ကာကွယ်ရာ မဟုတ်"), ("aleṇa", "ပုန်းအောင်းရာ မဟုတ်"), ("asaraṇa", "ကိုးကွယ်ရာ မဟုတ်"),
          ("asaraṇībhūta", "ကိုးကွယ်ရာ မဖြစ်သော အရာ"), ("ritta", "ဗလာ"), ("tuccha", "အနှစ်မဲ့"),
          ("suñña", "ဆိတ်သုဉ်း"), ("anatta", "အတ္တ မဟုတ်"), ("ādīnava", "အပြစ်"),
          ("vipariṇāmadhamma", W("2", "^2-943", "vipariṇāmadhammā", "ဖောက်ပြန်ပြောင်းလဲတတ်သော သဘော"))]
ASP = {}
for _a, _m in ASPECT:
    _pa = {"pabhaṅgu": "pabhaṅguto", "īti": "ītito"}.get(_a, _a + "to")
    ASP[_pa] = _m + "ဟု"
    P(_pa, FR(ASP[_pa]))
    P(f"saṅkhāre {_pa}", FR(f"{SK}ကို {ASP[_pa]}"))
    P(f"saṅkhāre ca {_pa}", FR(f"{SK}ကိုလည်း {ASP[_pa]}"))
    P(f"{_pa} manasikaroto saṃyojanā pahīyanti", Cl(f"{ASP[_pa]} နှလုံးသွင်းသူ၏ {FET}တို့", *PAHIY))
    P(f"saṅkhāre {_pa} manasikaroto saṃyojanā pahīyanti", Cl(f"{SK}ကို {ASP[_pa]} နှလုံးသွင်းသူ၏ {FET}တို့", *PAHIY))
    P(f"{_pa} manasi karoti nibbāne ca ānisaṃsadassāvī hoti", V(f"{ASP[_pa]} နှလုံးသွင်း၍ {NIB}၌လည်း {ANIS}"))
    P(f"saṅkhāre ca {_pa} manasi karoti nibbāne ca ānisaṃsadassāvī hoti",
      V(f"{SK}ကိုလည်း {ASP[_pa]} နှလုံးသွင်း၍ {NIB}၌လည်း {ANIS}"))
new("aniccato … vipariṇāmadhammato (the 26 aspects)", "၊ ".join(m + "ဟု" for _, m in ASPECT))
Q("idha, bhikkhave, bhikkhu nibbāne sukhānupassī viharati sukhasaññī sukhapaṭisaṃvedī, satataṃ samitaṃ abbokiṇṇaṃ "
  "cetasā adhimuccamāno paññāya pariyogāhamāno",
  f"ရဟန်းတို့၊ ဤသာသနာ၌ ရဟန်းသည် {NIB}၌ ချမ်းသာဟု အဖန်ဖန် ရှုလျက်၊ ချမ်းသာဟု မှတ်သိလျက်၊ ချမ်းသာကို ခံစားလျက်၊ "
  f"အမြဲတမ်း၊ အစဉ်တစိုက်၊ ကြားမလပ်ဘဲ စိတ်ဖြင့် ဆုံးဖြတ်လျက်၊ ပညာဖြင့် သက်ဝင်လျက် နေ၏")
new("idha, bhikkhave, bhikkhu", "ရဟန်းတို့၊ ဤသာသနာ၌ ရဟန်းသည်")

# --- 85. Amatārammaṇakathā
section("(85) 2. Amatārammaṇakathā", f"(85) 2. {AMATA}ကို အာရုံပြုခြင်းအကြောင်း {KATHA}")
section("Amatārammaṇakathā", f"{AMATA}ကို အာရုံပြုခြင်းအကြောင်း {KATHA}")
COLO_X["Navamavaggo"] = HEAD_X["Navamavaggo"]
ARV = P11.AR_V                                                        # («အာရုံပြု», «အာရုံ မပြု»)
P("amatārammaṇaṃ saṃyojanaṃ", Cl(f"{FET}သည် {AMATA}ကို", *ARV))
new("amatārammaṇaṃ saṃyojanaṃ", f"{FET}သည် {AMATA}ကို အာရုံပြု")
MAT = P11.MAT
_MK9 = ("saṃyojaniya", "ganthaniya", "oghaniya", "yoganiya", "nīvaraṇiya", "parāmaṭṭha", "upādāniya", "saṃkilesiya")
MATP = {k: MAT[k] for k in _MK9}
MATN = {k: v.replace("ဖြစ်နိုင်သော", "မဖြစ်နိုင်သော") for k, v in MATP.items()}
for _k in ("saṃyojaniya", "ganthaniya", "oghaniya", "yoganiya", "nīvaraṇiya"):
    W("1", {"saṃyojaniya": "^1-M2-21", "ganthaniya": "^1-M2-27", "oghaniya": "^1-M2-33", "yoganiya": "^1-M2-39",
            "nīvaraṇiya": "^1-M2-45"}[_k], "(Kha)", MATN[_k])
_PI9 = ["saṃyojaniyaṃ", "ganthaniyaṃ", "oghaniyaṃ", "yoganiyaṃ", "nīvaraṇiyaṃ", "parāmaṭṭhaṃ", "upādāniyaṃ",
        "saṃkilesiyaṃ"]
_NI9 = ["asaṃyojaniyaṃ", "aganthaniyaṃ", "anoghaniyaṃ", "ayoganiyaṃ", "anīvaraṇiyaṃ", "aparāmaṭṭhaṃ", "anupādāniyaṃ",
        "asaṃkilesiyaṃ"]
_PM = [MATP[k] for k in _MK9]
_NM = [MATN[k] for k in _MK9]
OBJ_S = {"amataṃ": AMATA, "rūpaṃ": "ရုပ်"}
for _s, _sm in OBJ_S.items():
    P(f"{_s} {' '.join(_PI9)}", V(f"{_sm}သည် {f'{C} '.join(_PM)} အရာ"))
    P(f"{_s} {' '.join(_NI9)}", V(f"{_sm}သည် {f'{C} '.join(_NM)} အရာ"))
    P(f"{_s} {_PI9[0]} {_PI9[1]}", FR(f"{_sm}သည် {_PM[0]}{C} {_PM[1]}"))
    P(f"{_s} {_NI9[0]} {_NI9[1]}", FR(f"{_sm}သည် {_NM[0]}{C} {_NM[1]}"))
    P(f"{_s} {_PI9[0]}", FR(f"{_sm}သည် {_PM[0]}"))
    P(f"{_s} {_NI9[0]}", FR(f"{_sm}သည် {_NM[0]}"))
P("saṃkilesiyaṃ", V(f"{_PM[-1]} အရာ"))
P("asaṃkilesiyaṃ", V(f"{_NM[-1]} အရာ"))
RG, DS, MHP, MHN = P6._RG, P6._DS, P6._MH_POS, P6._MH_NEG                # ch10 lists (rāgaṭṭhāniya …)
_RGN = [RG[0] + " မဟုတ်"] + [x + " အရာ မဟုတ်" for x in RG[1:]]          # na rāgaṭṭhāniyaṃ na rajaniyaṃ …
_DSN = [x + " မဟုတ်" for x in DS]
RGP_PI = "rāgaṭṭhāniyaṃ rajaniyaṃ kamaniyaṃ madaniyaṃ bandhaniyaṃ mucchaniyaṃ"
RGN_PI = "na rāgaṭṭhāniyaṃ na rajaniyaṃ na kamaniyaṃ na madaniyaṃ na bandhaniyaṃ na mucchaniyaṃ"
DSP_PI, DSN_PI = "dosaṭṭhāniyaṃ kopaṭṭhāniyaṃ paṭighaṭṭhāniyaṃ", "na dosaṭṭhāniyaṃ na kopaṭṭhāniyaṃ na paṭighaṭṭhāniyaṃ"
MHP_PI = "mohaṭṭhāniyaṃ aññāṇakaraṇaṃ acakkhukaraṇaṃ paññānirodhiyaṃ vighātapakkhiyaṃ anibbānasaṃvattaniyaṃ"
MHN_PI = "na mohaṭṭhāniyaṃ na aññāṇakaraṇaṃ na acakkhukaraṇaṃ paññābuddhiyaṃ avighātapakkhiyaṃ nibbānasaṃvattaniyaṃ"
for _s, _sm in OBJ_S.items():
    _h = f"{_sm}သည် "
    P(f"{_s} {RGP_PI}", V(_h + f"{C} ".join(RG) + " အရာ"))
    P(f"{_s} {RGN_PI}", V(_h + f"{C} ".join(_RGN[:-1] + [_RGN[-1][:-len(' မဟုတ်')]]), neg=True))
    P(f"{_s} rāgaṭṭhāniyaṃ", FR(_h + RG[0]))
    P(f"{_s} na rāgaṭṭhāniyaṃ", FR(_h + _RGN[0]))
    P("mucchaniyaṃ", V(RG[-1] + " အရာ"))
    P("na mucchaniyaṃ", V(RG[-1] + " အရာ", neg=True))
    P(f"{_s} {DSP_PI}", V(_h + f"{C} ".join(DS) + " အရာ"))
    P(f"{_s} {DSN_PI}", V(_h + f"{C} ".join(_DSN[:-1] + [DS[-1]]), neg=True))
    P(f"{_s} {MHP_PI}", V(_h + f"{C} ".join(MHP) + " အရာ"))
    P(f"{_s} {MHN_PI}", V(_h + f"{C} ".join(MHN) + " အရာ"))
    P(f"{_s} mohaṭṭhāniyaṃ aññāṇakaraṇaṃ", FR(_h + f"{MHP[0]}{C} {MHP[1]}"))
    P(f"{_s} na mohaṭṭhāniyaṃ na aññāṇakaraṇaṃ", FR(_h + f"{MHN[0]}{C} {MHN[1]}"))
    P("anibbānasaṃvattaniyaṃ", V(MHP[-1] + " အရာ"))
    P("nibbānasaṃvattaniyaṃ", V(MHN[-1] + " အရာ"))
    for _kl, _km in (("saṃyojanā uppajjanti", f"{FET}တို့ ဖြစ်ပေါ်ကြ"), ("rāgo uppajjati", "ရာဂ ဖြစ်ပေါ်"),
                     ("doso uppajjati", "ဒေါသ ဖြစ်ပေါ်"), ("moho uppajjati", "မောဟ ဖြစ်ပေါ်")):
        P(f"{_s} ārabbha {_kl}", Cl(f"{_sm}{P6._ARB} {_km.rsplit(' ', 1)[0]}", _km.rsplit(' ', 1)[1],
                                    "မ" + _km.rsplit(' ', 1)[1]))
Q("nibbānaṃ nibbānato sañjānāti, nibbānaṃ nibbānato sañjānitvā nibbānaṃ maññati, nibbānasmiṃ maññati, nibbānato "
  "maññati, nibbānaṃ meti maññati, nibbānaṃ abhinandati",
  f"{NIB}ကို {NIB}ဟု မှတ်သိ၏၊ {NIB}ကို {NIB}ဟု မှတ်သိ၍ {NIB}ကို ထင်မှတ်၏၊ {NIB}၌ ထင်မှတ်၏၊ {NIB}မှ ထင်မှတ်၏၊ "
  f"{NIB}သည် ငါ၏ ဥစ္စာဟု ထင်မှတ်၏၊ {NIB}ကို နှစ်သက်၏")
new("maññati (conceives)", "ထင်မှတ်")

# --- 86. Rūpaṃ sārammaṇantikathā
section("(86) 3. Rūpaṃ sārammaṇantikathā", f"(86) 3. ရုပ်သည် {F.SARAMMANA_TH[0]} ဖြစ်သည်ဟူသော {KATHA}")   # B6
section("Rūpaṃ sārammaṇantikathā", f"ရုပ်သည် {F.SARAMMANA_TH[0]} ဖြစ်သည်ဟူသော {KATHA}")
_MF16 = "saññā cetanā cittaṃ saddhā vīriyaṃ sati samādhi paññā rāgo doso moho māno diṭṭhi vicikicchā thinaṃ uddhaccaṃ ahirikaṃ"
_MF16M = f"{MF['vedanā']}… {mlist(_MF16)}… {MF['anottappaṃ']}"
for _neg, _sfx in ((False, "sārammaṇaṃ"), (True, "anārammaṇaṃ")):
    P(f"vedanā… {_MF16}… anottappaṃ {_sfx}", ar(_MF16M, _neg))
    P(f"vedanā… anottappaṃ {_sfx}", ar(f"{MF['vedanā']}… {MF['anottappaṃ']}", _neg))
for _k, _m in list(MF.items()) + [("rūpaṃ", "ရုပ်"), ("ñāṇaṃ", "ဉာဏ်")]:
    P(f"{_k} sārammaṇaṃ", ar(_m, False))
    P(f"{_k} sārammaṇo", ar(_m, False))
    P(f"{_k} sārammaṇā", ar(_m, False))
    P(f"{_k} anārammaṇaṃ", ar(_m, True))
    P(f"{_k} anārammaṇo", ar(_m, True))
    P(f"{_k} anārammaṇā", ar(_m, True))
P("rūpaṃ sappaccayaṃ", V(f"ရုပ်သည် {F.SAPPACCAYA} အရာ"))

# --- 87. Anusayā anārammaṇākathā
section("(87) 4. Anusayā anārammaṇakathā", f"(87) 4. {ANUS}တို့သည် {F.SARAMMANA_TH[1]} ဖြစ်သည်ဟူသော {KATHA}")
section("Anusayā anārammaṇātikathā", f"{ANUS}တို့သည် {F.SARAMMANA_TH[1]} ဖြစ်သည်ဟူသော {KATHA}")
P("anusayā anārammaṇā", ar(f"{ANUS}တို့", True))
AN7 = dict(zip(("kāmarāgānusayo", "paṭighānusayo", "mānānusayo", "diṭṭhānusayo", "vicikicchānusayo",
                "bhavarāgānusayo", "avijjānusayo"),
               F.strip_id(F.FINAL.seg("2", "^2-949")[2][0]).split("။ ", 1)[1].split(" – ")[0].split(f"{C} ")))
W("2", "^2-949", "Kāmarāgānusayo", AN7["kāmarāgānusayo"])
KR = {"kāmarāgo": "ကာမရာဂ", "kāmarāgapariyuṭṭhānaṃ": f"ကာမရာဂ {P11.PARIYUTTH}",
      "kāmarāgasaṃyojanaṃ": W("1", "^1-1118", "kāmarāgasaṃyojanaṃ", "ကာမရာဂ နှောင်ကြိုး"),
      "kāmogho": "ကာမ ရေအလျဉ်", "kāmayogo": "ကာမ ထမ်းပိုး",
      "kāmacchandanīvaraṇaṃ": W("1", "^1-1158", "kāmacchandanīvaraṇaṃ", "ကာမကို လိုလားမှု အတားအဆီး")}
_AVJ = P6._AV                                                         # «အမှန်ကို မသိမှု»
AV = {"avijjā": _AVJ, "avijjogho": f"{_AVJ} ရေအလျဉ်", "avijjāyogo": f"{_AVJ} ထမ်းပိုး",
      "avijjānusayo": f"{_AVJ} {ANUS}", "avijjāpariyuṭṭhānaṃ": f"{_AVJ} {P11.PARIYUTTH}",
      "avijjāsaṃyojanaṃ": f"{_AVJ} {FET}", "avijjānīvaraṇaṃ": f"{_AVJ} အတားအဆီး"}
W("1", "^1-1118", "avijjāsaṃyojanaṃ", AV["avijjāsaṃyojanaṃ"])
W("1", "^1-1158", "avijjānīvaraṇaṃ", AV["avijjānīvaraṇaṃ"])
_KR = f"{C} ".join(KR.values())
_AVL = f"{C} ".join(AV.values())
_AVPE = f"{AV['avijjā']}{C} {AV['avijjogho']}… {AV['avijjānīvaraṇaṃ']}"
for _neg, _sfx in ((True, "anārammaṇaṃ"), (False, "sārammaṇaṃ")):
    P(f"{' '.join(KR)} {_sfx}", ar(_KR, _neg))
    P(f"{' '.join(AV)} {_sfx}", ar(_AVL, _neg))
    P(f"avijjā avijjogho… avijjānīvaraṇaṃ {_sfx}", ar(_AVPE, _neg))
_AN6 = " ".join(list(AN7)[1:])
P(f"{_AN6} anārammaṇo", ar(f"{C} ".join(list(AN7.values())[1:]), True))
for _k, _m in (("kāmarāgānusayo", AN7["kāmarāgānusayo"]), ("avijjānusayo", AN7["avijjānusayo"]),
               ("kāmarāgo", "ကာမရာဂ"), ("avijjā", _AVJ), ("ñāṇaṃ", "ဉာဏ်"), ("paññā", "ပညာ")):
    for _neg, _sfx in ((True, "anārammaṇ"), (False, "sārammaṇ")):
        for _e in ("o", "aṃ", "ā"):
            P(f"{_k} {_sfx}{_e}", ar(_m, _neg))
            P(f"{_k} saṅkhārakkhandhapariyāpann{_e} {_sfx}{_e}", ar(f"{SKP} {_m}", _neg))
_AM = F.ABY if hasattr(F, "ABY") else None
ABYK = "ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော"                         # abyākata (pi-1)
W("1", "^1-431", "Katame dhammā abyākatā", ABYK)
KAC = new("kusalābyākate citte vattamāne", f"ကုသိုလ်စိတ်နှင့် {ABYK} စိတ် ဖြစ်နေစဉ်")
assert KAC == F.KUSALABYAKATE
P("puthujjano kusalābyākate citte vattamāne sānusayoti vattabbo",
  Cl(f"{KAC} {PUTHU}ကို «{ANUS} ရှိသူ»ဟု", "ဆိုသင့်", "မဆိုသင့်"))
P("puthujjano kusalābyākate citte vattamāne sarāgoti vattabbo",
  Cl(f"{KAC} {PUTHU}ကို «ရာဂ ရှိသူ»ဟု", "ဆိုသင့်", "မဆိုသင့်"))
P("atthi tesaṃ anusayānaṃ ārammaṇaṃ", V(f"ထို{ANUS}တို့၏ {AR_Y}", EXIST))
P("atthi tassa rāgassa ārammaṇaṃ", V(f"ထိုရာဂ၏ {AR_Y}", EXIST))
P("rāgo anārammaṇo", ar("ရာဂ", True))

# --- 88. Ñāṇaṃ anārammaṇantikathā
section("(88) 5. Ñāṇaṃ anārammaṇantikathā", f"(88) 5. ဉာဏ်သည် {F.SARAMMANA_TH[1]} ဖြစ်သည်ဟူသော {KATHA}")
section("Ñāṇaṃ anārammaṇantikathā", f"ဉာဏ်သည် {F.SARAMMANA_TH[1]} ဖြစ်သည်ဟူသော {KATHA}")
_PN = "paññā paññindriyaṃ paññābalaṃ sammādiṭṭhi dhammavicayasambojjhaṅgo"
_PNM = f"{C} ".join(["ပညာ", F._IN["paññindriyaṃ"], W("1", "^1-1", "paññābalaṃ hoti", "ပညာ၏ စွမ်းအား"),
                     F.SAMMADITTHI, P6._BJ["dhammavicayasambojjhaṅgo"]])
P(f"{_PN} anārammaṇo", ar(_PNM, True))
P(f"{_PN} sārammaṇo", ar(_PNM, False))
CVS = f"{F._DH['cakkhuviññāṇadhātu'].rsplit(' ', 1)[0]}"                   # cakkhuviññāṇa «မျက်စိ သိစိတ်»
SAMANGI = "နှင့် ပြည့်စုံသော"                                          # -samaṅgī (pi-1 maggasamaṅgī «မဂ်နှင့် ပြည့်စုံသူ»)
W("1", "^1-1373", "maggasamaṅgissa", "မဂ်နှင့် ပြည့်စုံသူ")
P("arahā cakkhuviññāṇasamaṅgī ñāṇīti vattabbo",
  Cl(f"{CVS}{SAMANGI} {ARAHA}ကို «ဉာဏ် ရှိသူ»ဟု", "ဆိုသင့်", "မဆိုသင့်"))
P("arahā cakkhuviññāṇasamaṅgī paññavāti vattabbo",
  Cl(f"{CVS}{SAMANGI} {ARAHA}ကို «ပညာ ရှိသူ»ဟု", "ဆိုသင့်", "မဆိုသင့်"))
P("atthi tassa ñāṇassa ārammaṇaṃ", V(f"ထိုဉာဏ်၏ {AR_Y}", EXIST))
P("atthi tāya paññāya ārammaṇaṃ", V(f"ထိုပညာ၏ {AR_Y}", EXIST))

# --- 89. Atītānāgatārammaṇakathā
TIME = P6.TIME                                                        # atīt / anāgat / paccuppann
section("(89) 6. Atītānāgatārammaṇakathā", f"(89) 6. {TIME['atīt']}နှင့် {TIME['anāgat']}ကို အာရုံပြုခြင်းအကြောင်း {KATHA}")
section("Atītānāgatārammaṇakathā", f"{TIME['atīt']}နှင့် {TIME['anāgat']}ကို အာရုံပြုခြင်းအကြောင်း {KATHA}")
for _t in ("atīt", "anāgat", "paccuppann"):
    _tm = TIME[_t]
    _c = f"{_tm}ကို အာရုံပြုသော စိတ်"
    P(f"{_t}ārammaṇaṃ cittaṃ anārammaṇaṃ", ar(_c, True))
    P(f"{_t}ārammaṇaṃ cittaṃ sārammaṇaṃ", ar(_c, False))
    P(f"{_t}ārammaṇaṃ", Cl(f"ထိုစိတ်သည် {_tm}ကို", *ARV))
    P(f"anārammaṇaṃ {_t}ārammaṇaṃ", Cl(f"{AR_Y} မရှိသော အရာသည် {_tm}ကို", *ARV))
    P(f"{_t}aṃ ārabbha atthi āvaṭṭanā… paṇidhi", V(f"{_tm}{P6._ARB} {ADV_PE1}", EXIST))
    P(f"{_t}aṃ ārabbha atthi āvaṭṭanā… paṇidhi, {_t}ārammaṇaṃ cittaṃ sārammaṇaṃ",
      V(f"{_tm}{P6._ARB} {ADV_PE1} ရှိ၍ {_c}သည် {F.SARAMMANA_TH[0]}"))
    P(f"{_t}aṃ ārabbha atthi āvaṭṭanā… paṇidhi, {_t}ārammaṇaṃ cittaṃ anārammaṇaṃ",
      V(f"{_tm}{P6._ARB} {ADV_PE1} ရှိ၍ {_c}သည် {F.SARAMMANA_TH[1]}"))
P("anārammaṇaṃ", V(F.SARAMMANA_TH[1]))            # harmonise B6: the bare predicate = ch16
_ATAN = f"{TIME['atīt']}နှင့် {TIME['anāgat']}"
P("atītānāgatārammaṇaṃ cittaṃ anārammaṇaṃ", ar(f"{_ATAN}ကို အာရုံပြုသော စိတ်", True))
P("atītānāgataṃ natthi", V(f"{_ATAN}သည်", EXIST, True))


# --- 90. Vitakkānupatitakathā
ANUP = ("တွဲဖက်နေ", "မတွဲဖက်နေ")                                       # -anupatita (accompanied by)
section("(90) 7. Vitakkānupatitakathā", f"(90) 7. {VIT}နှင့် တွဲဖက်နေခြင်းအကြောင်း {KATHA}")
section("Vitakkānupatitakathā", f"{VIT}နှင့် တွဲဖက်နေခြင်းအကြောင်း {KATHA}")
ALLC = "စိတ် အားလုံး"                                                  # sabbaṃ cittaṃ
P("sabbaṃ cittaṃ vitakkānupatitaṃ", Cl(f"{ALLC}သည် {VIT}နှင့်", *ANUP))
new("X-anupatita", "Xနှင့် တွဲဖက်နေ")
_ANL = [VIC, "ပီတိ", "သာယာမှု", "နာကျင်မှု", "ဝမ်းမြောက်မှု", "စိတ်ဆင်းရဲမှု", "ဥပေက္ခာ", MF["saddhā"], MF["vīriyaṃ"],
        MF["sati"], MF["samādhi"], MF["paññā"], MF["rāgo"], MF["doso"]]
P("sabbaṃ cittaṃ vicārānupatitaṃ pītānupatitaṃ sukhānupatitaṃ dukkhānupatitaṃ somanassānupatitaṃ "
  "domanassānupatitaṃ upekkhānupatitaṃ saddhānupatitaṃ vīriyānupatitaṃ satānupatitaṃ samādhānupatitaṃ "
  "paññānupatitaṃ rāgānupatitaṃ dosānupatitaṃ… anottappānupatitaṃ",
  Cl(f"{ALLC}သည် " + f"{C} ".join(x + "နှင့်" for x in _ANL) + f"… {MF['anottappaṃ']}နှင့်", *ANUP))
AVV = W("1", "^1-M1-6", "avitakkavicāramattā dhammā", "စတင်ကြံစည်မှု မရှိဘဲ ဆက်လက်သုံးသပ်မှုသာ ရှိသော")
AVA = W("1", "^1-M1-6", "avitakkaavicārā", "စတင်ကြံစည်မှုလည်း မရှိ၊ ဆက်လက်သုံးသပ်မှုလည်း မရှိသော")
SVV = W("1", "^1-M1-6", "savitakkasavicārā dhammā", "စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှု ရှိသော")
P("atthi avitakko vicāramatto samādhi", V(f"{AVV} သမာဓိ", EXIST))
P("atthi avitakko avicāro samādhi", V(f"{AVA} သမာဓိ", EXIST))
_TS = f"{SVV} သမာဓိ{C} {AVV} သမာဓိ{C} {AVA} သမာဓိ"
P("tayo samādhī vuttā bhagavatā – savitakko savicāro samādhi, avitakko vicāramatto samādhi, avitakko avicāro samādhi",
  Cl(f"{F.BHAGAVA}သည် သမာဓိ {F.NUM_MY[3]}{F.CL}ကို", "ဟောတော်မူ", "မဟောတော်မူ", post=f" – {_TS}"))
BR_X["[dī. ni. 3.305, 353]"] = f"[{F.REF['dī. ni.']} 3.305, 353]"

# --- 91. Vitakkavipphārasaddakathā
VSAD = new("vitakkavipphāro saddo", f"{VIT} ပျံ့နှံ့ခြင်းဟူသော အသံ")
section("(91) 8. Vitakkavipphārasaddakathā", f"(91) 8. {VSAD}အကြောင်း {KATHA}")
section("Vitakkavipphārasaddakathā", f"{VSAD}အကြောင်း {KATHA}")
SABBASO = "အခါခပ်သိမ်း"                                                 # sabbaso (in every case)
for _k, _who, _w in (("vitakkayato vicārayato vitakka", f"{VIT} ပြုနေသူ၊ {VIC} ပြုနေသူ", VIT),
                     ("phusayato phassa", "တွေ့ထိနေသူ", MF["phasso"]), ("vedayato vedanā", "ခံစားနေသူ", MF["vedanā"]),
                     ("sañjānato saññā", "မှတ်သိနေသူ", MF["saññā"]), ("cetayato cetanā", "စေ့ဆော်နေသူ", MF["cetanā"]),
                     ("cintayato citta", "ကြံတွေးနေသူ", MF["cittaṃ"]), ("sarato sati", "အောက်မေ့နေသူ", MF["sati"]),
                     ("pajānato paññā", "ပိုင်းခြား သိနေသူ", MF["paññā"])):
    P(f"sabbaso {_k}vipphāro saddo", V(f"{_who}၏ {_w} ပျံ့နှံ့ခြင်းသည် {SABBASO} အသံ"))
_SOT = "နားဖြင့် သိနိုင်သော အရာ ဖြစ်၏၊ နား၌ ထိခိုက်၏၊ နား၏ အာရုံ နယ်ပယ်သို့"   # ch10 (lokuttaro dhammo sotaviññeyyo …)
_SOTN = "နားဖြင့် သိနိုင်သော အရာ မဟုတ်၊ နား၌ မထိခိုက်၊ နား၏ အာရုံ နယ်ပယ်သို့"
P("vitakkavipphāro saddo sotaviññeyyo sotasmiṃ paṭihaññati sotassa āpāthaṃ āgacchati",
  Cl(f"{VSAD}သည် {_SOT}", "ရောက်လာ", "မရောက်လာ"))
P("vitakkavipphāro saddo na sotaviññeyyo na sotasmiṃ paṭihaññati na sotassa āpāthaṃ āgacchati",
  Cl(f"{VSAD}သည် {_SOTN}", "ရောက်လာ", "မရောက်လာ", neg=True))

# --- 92 / 93. Na yathācittassa vācā / kāyakammaṃ
VACA = "စကား"                                                          # vācā
KK = W("2", "^2-751", "na kāyakammaṃ na vacīkammaṃ", "ကိုယ်ဖြင့် ပြုသော ကံ")   # kāyakammaṃ (pi-2)
NYC = {"vācā": VACA, "kāyakammaṃ": KK}
section("(92) 9. Na yathācittassa vācātikathā", f"(92) 9. {VACA}သည် စိတ်အတိုင်း မဟုတ်ဟူသော {KATHA}")
section("Na yathācittassa vācātikathā", f"{VACA}သည် စိတ်အတိုင်း မဟုတ်ဟူသော {KATHA}")
section("(93) 10. Na yathācittassa kāyakammantikathā", f"(93) 10. {KK}သည် စိတ်အတိုင်း မဟုတ်ဟူသော {KATHA}")
section("Na yathācittassa kāyakammantikathā", f"{KK}သည် စိတ်အတိုင်း မဟုတ်ဟူသော {KATHA}")
new("na yathācittassa X", "Xသည် စိတ်အတိုင်း မဟုတ်")
WHO = [("phassakassa", MF["phasso"]), ("vedanakassa", MF["vedanā"]), ("saññakassa", MF["saññā"]),
       ("cetanakassa", MF["cetanā"]), ("cittakassa", MF["cittaṃ"])]
ADVW = [("āvaṭṭentassa", "anāvaṭṭentassa", "စိတ်ကို လှည့်ဆောင်သူ", "စိတ်ကို မလှည့်ဆောင်သူ"),
        ("ābhogassa", "anābhogassa", "စိတ်ညွတ်သူ", "စိတ် မညွတ်သူ"),
        ("paṇidahantassa", "appaṇidahantassa", "ဆုတောင်းသူ", "ဆု မတောင်းသူ")]
for _k, _m in NYC.items():
    P(f"na yathācittassa {_k}", V(f"{_m}သည် စိတ်အတိုင်း", neg=True))
    _pos = [f"{w} ရှိသူ၏ {_m}" for _, w in WHO]
    _neg = [f"{w} မရှိသူ၏ {_m}" for _, w in WHO]
    P(" ".join(f"a{p} {_k}" for p, _ in WHO), V(f"{C} ".join(_neg)))
    P(" ".join(f"sa{p} {_k}" for p, _ in WHO), V(f"{C} ".join(_pos)))
    P(f"saphassakassa {_k}… sacittakassa {_k}", V(f"{_pos[0]}… {_pos[-1]}"))
    P(f"aphassakassa {_k}… acittakassa {_k}", V(f"{_neg[0]}… {_neg[-1]}"))
    _ap = {a: f"{m}၏ {_m}" for a, _, m, _ in ADVW}
    _an = {a: f"{m}၏ {_m}" for _, a, _, m in ADVW}
    P(f"anāvaṭṭentassa {_k}… anābhogassa {_k}… appaṇidahantassa {_k}",
      V(f"{_an['anāvaṭṭentassa']}… {_an['anābhogassa']}… {_an['appaṇidahantassa']}"))
    P(f"anāvaṭṭentassa {_k}… appaṇidahantassa {_k}", V(f"{_an['anāvaṭṭentassa']}… {_an['appaṇidahantassa']}"))
    P(f"āvaṭṭentassa {_k} ābhogassa {_k}… paṇidahantassa {_k}",
      V(f"{_ap['āvaṭṭentassa']}{C} {_ap['ābhogassa']}… {_ap['paṇidahantassa']}"))
    P(f"āvaṭṭentassa {_k} ābhogassa {_k} paṇidahantassa {_k}",
      V(f"{_ap['āvaṭṭentassa']}{C} {_ap['ābhogassa']}{C} {_ap['paṇidahantassa']}"))
    P(f"āvaṭṭentassa {_k}… paṇidahantassa {_k}", V(f"{_ap['āvaṭṭentassa']}… {_ap['paṇidahantassa']}"))
ANCHOR_X["Anāvaṭṭentassa"] = "စိတ်ကို မလှည့်ဆောင်သူ၏"
BR_X["[anāvaṭṭantassa (pī.), anāvajjantassa (sī. syā. ka.) kathā. 484 passitabbaṃ]"] = (
    f"[{F.PATHA} (Pī.): anāvaṭṭantassa{C} (Sī., Syā., Ka.): anāvajjantassa{C} ဤကျမ်း၏ ဆွေးနွေးချက် 484 ကို ကြည့်ပါ]")
_CS = W("1", "^1-M2-60", "cittasamuṭṭhānā dhammā", "စိတ်မှ ဖြစ်ပေါ်လာသော")
_SJ = "စိတ်နှင့်အတူ ပေါ်ပေါက်သော"                                       # cittena sahajāta (ch11 X-sahajāta)
_EU = "စိတ်နှင့် တစ်ပြိုင်နက် ဖြစ်ပေါ်သော"                              # cittena saha ekuppāda
new("cittena saha ekuppāda", _EU)
P("vācā cittasamuṭṭhānā cittena sahajātā cittena saha ekuppādā", V(f"{VACA}သည် {_CS}{C} {_SJ}{C} {_EU} အရာ"))
P("kāyakammaṃ cittasamuṭṭhānaṃ cittena sahajātaṃ cittena saha ekuppādaṃ", V(f"{KK}သည် {_CS}{C} {_SJ}{C} {_EU} အရာ"))
SPEAK = [("bhaṇitukāmo bhaṇati", "ပြောလို", "ပြော"), ("kathetukāmo katheti", "ပြောဆိုလို", "ပြောဆို"),
         ("ālapitukāmo ālapati", "ခေါ်ပြောလို", "ခေါ်ပြော"), ("voharitukāmo voharati", "သုံးနှုန်းပြောလို", "သုံးနှုန်းပြော")]
MOVE = [("abhikkamitukāmo abhikkamati", "ရှေ့သို့ တိုးလို", "ရှေ့သို့ တိုး"),
        ("paṭikkamitukāmo paṭikkamati", "နောက်သို့ ဆုတ်လို", "နောက်သို့ ဆုတ်"),
        ("āloketukāmo āloketi", "ရှေ့သို့ ကြည့်လို", "ရှေ့သို့ ကြည့်"), ("viloketukāmo viloketi", "ဘေးသို့ ကြည့်လို", "ဘေးသို့ ကြည့်"),
        ("samiñjitukāmo samiñjeti", "ကွေးလို", "ကွေး"), ("pasāretukāmo pasāreti", "ဆန့်လို", "ဆန့်")]


def _negw(w):
    a = w.rsplit(" ", 1)
    return f"{a[0]} မ{a[1]}" if len(a) == 2 else "မ" + w


for _p, _want, _do in SPEAK + MOVE:
    P(_p, VV(f"{_want}၍", _do))
    _pre, _v = (_do.rsplit(" ", 1) + [""])[:2] if " " in _do else ("", _do)
    P("na " + _p, Cl(f"{_negw(_want)}ဘဲ {_pre}".strip(), _v, "မ" + _v))
P("abhikkamitukāmo abhikkamati… pasāretukāmo pasāreti", VV(f"{MOVE[0][1]}၍ {MOVE[0][2]}… {MOVE[-1][1]}၍", "ဆန့်"))
new("na X-tukāmo X-ti (does X without wishing to)", "X မလိုဘဲ X")
SOMEONE = "တစ်စုံတစ်ယောက်"                                              # koci (sample)
_OTH = [("bhaṇ", "ပြော"), ("kath", "ပြောဆို"), ("ālap", "ခေါ်ပြော"), ("vohar", "သုံးနှုန်းပြော")]
_OTHP = {"bhaṇ": ("bhaṇissāmī", "bhaṇati"), "kath": ("kathessāmī", "katheti"), "ālap": ("ālapissāmī", "ālapati"),
         "vohar": ("voharissāmī", "voharati")}
_om = [f"«တစ်ခုကို {m}မည်»ဟု ကြံ၍ အခြား တစ်ခုကို {m}" for _, m in _OTH]
P("atthi koci " + ", ".join(f"aññaṃ {_OTHP[k][0]}ti aññaṃ {_OTHP[k][1]}" for k, _ in _OTH),
  V(f"{'၏၊ '.join(_om)}သော {SOMEONE}", EXIST))
P(f"atthi koci aññaṃ bhaṇissāmīti aññaṃ bhaṇati,… aññaṃ voharissāmīti aññaṃ voharati",
  V(f"{_om[0]}၏၊… {_om[-1]}သော {SOMEONE}", EXIST))
P("atthi koci aññatra gacchissāmīti aññatra gacchati… aññaṃ pasāressāmīti aññaṃ pasāreti",
  V(f"«တစ်နေရာသို့ သွားမည်»ဟု ကြံ၍ အခြား တစ်နေရာသို့ သွား၏… «တစ်ခုကို ဆန့်မည်»ဟု ကြံ၍ အခြား တစ်ခုကို ဆန့်သော "
    f"{SOMEONE}", EXIST))
new("aññaṃ X-issāmīti aññaṃ X-ti", "«တစ်ခုကို Xမည်»ဟု ကြံ၍ အခြား တစ်ခုကို X")

# --- 94. Atītānāgatasamannāgatakathā
SMN = P11.SAMANN                                                       # («ပြည့်စုံ», «မပြည့်စုံ»)
_ATAN2 = new("atītānāgatehi (samannāgato)", f"{TIME['atīt']}၊ {TIME['anāgat']}တို့")
section("(94) 11. Atītānāgatasamannāgatakathā", f"(94) 11. {_ATAN2}နှင့် ပြည့်စုံခြင်းအကြောင်း {KATHA}")
section("Atītānāgatasamannāgatakathā", f"{_ATAN2}နှင့် ပြည့်စုံခြင်းအကြောင်း {KATHA}")
P("atītena samannāgato", Cl(f"{TIME['atīt']}နှင့်", *SMN))
P("anāgatena samannāgato", Cl(f"{TIME['anāgat']}နှင့်", *SMN))
P("atītānāgatehi samannāgato", Cl(f"{_ATAN2}နှင့်", *SMN))
_CEASED = "ချုပ်ငြိမ်းပြီး၊ ကင်းကွာပြီး၊ ဖောက်ပြန်ပြောင်းလဲပြီး၊ ကွယ်ပြီး၊ လုံးဝ ကွယ်ပြီးသော အရာ"            # ch5 (copied)
_UNBORN = ("မဖြစ်သေး၊ မဖြစ်တည်သေး၊ မဖြစ်ပေါ်သေး၊ မဖြစ်မြောက်သေး၊ ထင်ရှားစွာ မဖြစ်မြောက်သေး၊ ထင်ရှား "
           "မပေါ်ပေါက်သေးသော အရာ")                                                                     # ch5 (copied)
COPY25 = {"atītaṃ niruddhaṃ vigataṃ vipariṇataṃ atthaṅgataṃ abbhatthaṅgataṃ": f"{TIME['atīt']}သည် {_CEASED}",
          "anāgataṃ ajātaṃ abhūtaṃ asañjātaṃ anibbattaṃ anabhinibbattaṃ apātubhūtaṃ": f"{TIME['anāgat']}သည် {_UNBORN}"}
for _k, _m in COPY25.items():
    P(_k, V(_m))
NUM_X = {3: F.NUM_MY[3], 5: F.NUM_MY[5], 12: F.NUM_MY[12], 15: "ဆယ့်ငါး", 18: F.NUM_MY[18], 22: F.NUM_MY[22],
         36: "သုံးဆယ့်ခြောက်", 54: "ငါးဆယ့်လေး", 66: "ခြောက်ဆယ့်ခြောက်"}
_TI = {"atīt": ("atītena", "atītāya", "atītehi", "atītāhi"), "anāgat": ("anāgatena", "anāgatāya", "anāgatehi", "anāgatāhi"),
       "paccuppann": ("paccuppannena", "paccuppannāya", "paccuppannehi", "paccuppannāhi")}
for _t, (_m1, _f1, _mp, _fp) in _TI.items():
    _tm = TIME[_t]
    P(f"{_m1} rūpakkhandhena samannāgato", Cl(f"{_tm} {KH['rūpakkhandho']}နှင့်", *SMN))
    P(f"{_mp} pañcahi khandhehi samannāgato", Cl(f"{_tm} {F.KHANDHA_W} {NUM_X[5]}{F.CL}နှင့်", *SMN))
    P(f"{_m1} cakkhāyatanena samannāgato", Cl(f"{_tm} {AY['cakkhāyatanaṃ']}နှင့်", *SMN))
    P(f"{_mp} dvādasahi āyatanehi samannāgato", Cl(f"{_tm} {F.AYATANA_W} {NUM_X[12]}{F.CL}နှင့်", *SMN))
    P(f"{_f1} cakkhudhātuyā samannāgato", Cl(f"{_tm} {F._DH['cakkhudhātu']}နှင့်", *SMN))
    P(f"{_fp} aṭṭhārasahi dhātūhi samannāgato", Cl(f"{_tm} {F.DHATU_W} {NUM_X[18]}{F.CL}နှင့်", *SMN))
    P(f"{_m1} cakkhundriyena samannāgato", Cl(f"{_tm} {F._IN['cakkhundriyaṃ']}နှင့်", *SMN))
    P(f"{_mp} bāvīsatindriyehi samannāgato", Cl(f"{_tm} {F.INDRIYA_W} {NUM_X[22]}{F.CL}နှင့်", *SMN))
for _k, _m in (("tīhi rūpakkhandhehi", f"{KH['rūpakkhandho']} {NUM_X[3]}{F.CL}"),
               ("pannarasahi khandhehi", f"{F.KHANDHA_W} {NUM_X[15]}{F.CL}"),
               ("tīhi cakkhāyatanehi", f"{AY['cakkhāyatanaṃ']} {NUM_X[3]}{F.CL}"),
               ("chattiṃsāyatanehi", f"{F.AYATANA_W} {NUM_X[36]}{F.CL}"),
               ("tīhi cakkhudhātūhi", f"{F._DH['cakkhudhātu']} {NUM_X[3]}{F.CL}"),
               ("catupaññāsadhātūhi", f"{F.DHATU_W} {NUM_X[54]}{F.CL}"),
               ("tīhi cakkhundriyehi", f"{F._IN['cakkhundriyaṃ']} {NUM_X[3]}{F.CL}"),
               ("chasaṭṭhindriyehi", f"{F.INDRIYA_W} {NUM_X[66]}{F.CL}")):
    P(f"{_k} samannāgato", Cl(f"{_m}နှင့်", *SMN))
_VM = W("2", "^2-828", "Aṭṭha vimokkhā", f"လွတ်မြောက်ခြင်း {F.NUM_MY[8]}{F.CL}")
_NAV = W("2", "^2-808", "navasu anupubbavihārasamāpattīsu", f"အစဉ်အတိုင်း နေထိုင်ရာ ဈာန် ဝင်စားရာ {F.NUM_MY[9]}{F.CL}")
JHANA4 = f"ဈာန် {F.NUM_MY[4]}{F.CL}"
_AVJH = (f"{_VM}ဖြင့် ဈာန်ဝင်သူ၊ {JHANA4}ကို အလိုရှိတိုင်း ရသူ၊ {_NAV}ကို ရသူ")
new("aṭṭhavimokkhajhāyī catunnaṃ jhānānaṃ nikāmalābhī navannaṃ anupubbavihārasamāpattīnaṃ lābhī", _AVJH)
P("atthi aṭṭhavimokkhajhāyī catunnaṃ jhānānaṃ nikāmalābhī navannaṃ anupubbavihārasamāpattīnaṃ lābhī",
  V(f"{_AVJH} ဖြစ်သော {F.PUGGALA}", EXIST))


# --- 17. uddāna
EVAM = P6.MS.EVAM                                                      # evamevaṃ «ထို့အတူပင်» (pi-4)
TATHEVA = new("tatheva (uddāna)", F.TATHEVA)       # harmonise B7: = the sample
LINES_X[key("Ānisaṃsadassāvissa saṃyojanānaṃ pahānaṃ, amatārammaṇaṃ saṃyojanaṃ, rūpaṃ sārammaṇaṃ, anusayā "
            "anārammaṇā, evamevaṃ ñāṇaṃ, atītānāgatārammaṇaṃ cittaṃ, sabbaṃ cittaṃ vitakkānupatitaṃ, sabbaso "
            "vitakkayato vicārayato vitakkavipphāro saddo, na yathācittassa vācā, tatheva kāyakammaṃ "
            "atītānāgatehi samannāgatoti.")] = (
    f"{ANIS}၏ {FET}တို့ကို ပယ်ခြင်း၊ {FET}သည် {AMATA}ကို အာရုံပြုခြင်း၊ ရုပ်သည် {F.SARAMMANA_TH[0]} ဖြစ်ခြင်း၊ {ANUS}တို့သည် "
    f"{F.SARAMMANA_TH[1]} ဖြစ်ခြင်း၊ {EVAM} ဉာဏ်၊ {_ATAN}ကို အာရုံပြုသော စိတ်၊ {ALLC}သည် {VIT}နှင့် တွဲဖက်နေခြင်း၊ {SABBASO} "
    f"{VIT} ပြုနေသူ၊ {VIC} ပြုနေသူ၏ {VIT} ပျံ့နှံ့ခြင်းသည် အသံ ဖြစ်ခြင်း၊ {VACA}သည် စိတ်အတိုင်း မဟုတ်ခြင်း၊ "
    f"{TATHEVA} {KK}၊ {_ATAN2}နှင့် ပြည့်စုံခြင်း{END}")


# ===================================================================================== 18. Dasamavaggo
section("Dasamavaggo", f"{F.ORD_MY[10]} {F.VAGGA_W}")
COLO_X["Dasamavaggo"] = HEAD_X["Dasamavaggo"]
MAGGA = "မဂ်"
ARB = P6._ARB                                                          # ārabbha «ကို အာရုံပြု၍»
UPPAJJ = ("ဖြစ်ပေါ်", "မဖြစ်ပေါ်")
UPPAJJK = ("ဖြစ်ပေါ်ကြ", "မဖြစ်ပေါ်ကြ")
for _g in ("aṃ", "ā", "o"):                                             # bare predicates (subject elided)
    P(f"sār{'ammaṇ'}{_g}", V(F.SARAMMANA_TH[0]))         # harmonise B6: the bare predicate = ch16 (was «ထိုအရာသည် အာရုံ ရှိ»)
    P(f"anārammaṇ{_g}", V(F.SARAMMANA_TH[1]))
for _pr, _g in (("so", "o"), ("sā", "ā")):
    P(f"{_pr} ca sārammaṇ{_g}", V(f"ထိုအရာသည်လည်း {F.SARAMMANA_TH[0]}"))
    P(f"{_pr} ca anārammaṇ{_g}", V(f"ထိုအရာသည်လည်း {F.SARAMMANA_TH[1]}"))

# --- 95. Nirodhakathā
section("(95) 1. Nirodhakathā", f"(95) 1. ချုပ်ငြိမ်းခြင်းအကြောင်း {KATHA}")
section("Nirodhakathā", f"ချုပ်ငြိမ်းခြင်းအကြောင်း {KATHA}")
UPE = "ပြန်လည် ဖြစ်ပေါ်ခြင်းကို ရှာသော"                                 # upapattesiya (ch12 UPC)
KIRIYA = W("1", "^1-567", "Kiriyā manodhātu", "ပြုရုံမျှသာ ဖြစ်သော")    # kiriyā (pi-1)
KH5 = f"{F.KHANDHA_W} {F.NUM_MY[5]}{F.CL}"
_UPA = f"{UPE} {KH5} မချုပ်ငြိမ်းသေးမီ"
new("upapattesiye pañcakkhandhe aniruddhe / niruddhe", f"{UPE} {KH5} မချုပ်ငြိမ်းသေးမီ / ချုပ်ငြိမ်းပြီးသောအခါ")
P("upapattesiye pañcakkhandhe aniruddhe kiriyā pañcakkhandhā uppajjanti",
  Cl(f"{_UPA} {KIRIYA} {KH5}တို့", *UPPAJJK))
P("upapattesiye pañcakkhandhe aniruddhe kiriyā cattāro khandhā uppajjanti",
  Cl(f"{_UPA} {KIRIYA} {F.KHANDHA_W} {F.NUM_MY[4]}{F.CL}တို့", *UPPAJJK))
P("upapattesiye pañcakkhandhe aniruddhe kiriyāñāṇaṃ uppajjati", Cl(f"{_UPA} {KIRIYA} ဉာဏ်", *UPPAJJ))
P("upapattesiye pañcakkhandhe niruddhe maggo uppajjati",
  Cl(f"{UPE} {KH5} ချုပ်ငြိမ်းပြီးသောအခါ {MAGGA}", *UPPAJJ))
SAMM = F.SAMMUKHA         # harmonise B6: = ch15 (was «မျက်မှောက်သို့ ရောက်လာကြ»)         # sammukhībhāvaṃ āgacchanti
new("sammukhībhāvaṃ āgacchanti", SAMM[0])
for _n, _gen, _nom in ((10, "dasannaṃ", "dasa"), (9, "navannaṃ", "nava"), (6, "channaṃ", "cha")):
    _nm = {10: F.NUM_MY[10], 9: F.NUM_MY[9], 6: F.NUM_MY[6]}[_n]
    P(f"{_gen} khandhānaṃ samodhānaṃ hoti", V(f"{F.KHANDHA_W} {_nm}{F.CL}တို့၏ ပေါင်းဆုံခြင်း"))
    P(f"{_nom} khandhā sammukhībhāvaṃ āgacchanti", Cl(f"{F.KHANDHA_W} {_nm}{F.CL}တို့", *SAMM))
P("mato maggaṃ bhāveti", VV("သေပြီးသူသည် မဂ်ကို", "ပွားများ"))
P("kālaṅkato maggaṃ bhāveti", VV("ကွယ်လွန်ပြီးသူသည် မဂ်ကို", "ပွားများ"))

# --- 96. Rūpaṃ maggotikathā
section("(96) 2. Rūpaṃ maggotikathā", f"(96) 2. ရုပ်သည် {MAGGA} ဖြစ်သည်ဟူသော {KATHA}")
section("Rūpaṃ maggotikathā", f"ရုပ်သည် {MAGGA} ဖြစ်သည်ဟူသော {KATHA}")
MSG = W("1", "^1-1373", "maggasamaṅgissa", "မဂ်နှင့် ပြည့်စုံသူ")
P("maggasamaṅgissa rūpaṃ maggo", V(f"{MSG}၏ ရုပ်သည် {MAGGA}"))
PF = [("sammādiṭṭhi", "sammādiṭṭhiyā", "f", "မှန်ကန်သော အယူ"),
      ("sammāsaṅkappo", "sammāsaṅkappena", "m", "မှန်ကန်သော ကြံစည်မှု"),
      ("sammāvācā", "sammāvācāya", "f", "မှန်ကန်သော စကား"),
      ("sammākammanto", "sammākammantena", "m", "မှန်ကန်သော အလုပ်"),
      ("sammāājīvo", "sammāājīvena", "m", "မှန်ကန်သော အသက်မွေးမှု"),
      ("sammāvāyāmo", "sammāvāyāmena", "m", "မှန်ကန်သော အားထုတ်မှု"),
      ("sammāsati", "sammāsatiyā", "f", "မှန်ကန်သော သတိ"),
      ("sammāsamādhi", "sammāsamādhinā", "m", "မှန်ကန်သော သမာဓိ")]
W("2", "^2-486", "sammāvācā, sammākammanto, sammāājīvo", "မှန်ကန်သော စကား၊ မှန်ကန်သော အလုပ်၊ မှန်ကန်သော အသက်မွေးမှု")
PFM = {k: m for k, _, _, m in PF}
for _k, _ins, _g, _m in PF:
    P(_k, FR(_m))
    P(f"{_k} maggo", V(f"{_m}သည် {MAGGA}"))
S("sammāsaṅkappo… sammāvāyāmo… sammāsati….",                           # «…sati» would lose its «ti» in the frame
  f"{PFM['sammāsaṅkappo']}… {PFM['sammāvāyāmo']}… {PFM['sammāsati']}{PE}")
P("sammāvācā sammākammanto sammāājīvo maggo",
  V(f"{PFM['sammāvācā']}{C} {PFM['sammākammanto']}{C} {PFM['sammāājīvo']}သည် {MAGGA}"))

# --- 97-99. the five consciousnesses (pi-2 ^2-751 FINAL wording)
_751 = [re.sub(r"^\(\d+\) ", "", F.strip_id(x)).rstrip("၊") for x in F.FINAL.seg("2", "^2-751")[2]]
W("2", "^2-751", "Uppannavatthukā uppannārammaṇā", _751[1])
PV5 = "သိစိတ် ငါးပါး"                                                   # pañca viññāṇā (pi-2)
W("2", "^2-751", "Pañca viññāṇā anābhogā", f"{PV5}သည် စိတ်ညွတ်ခြင်း မရှိကြ")
_UV = _751[1][:-len(" ရှိကြသည်")]                                       # «ဖြစ်ပေါ်ပြီးသော မှီရာ ရှိ၍ ဖြစ်ပေါ်ပြီးသော အာရုံ»
P("pañcaviññāṇā uppannavatthukā uppannārammaṇā", Cl(f"{PV5}သည် {_UV}", "ရှိကြ", "မရှိကြ"))
_NANU5 = f"{PV5}သည် " + f"{C} ".join(_751[2:12])                       # (3) … (12)
P("pañcaviññāṇā anābhogā", Cl(f"{PV5}သည် စိတ်ညွတ်ခြင်း", "ရှိကြ", "မရှိကြ", neg=True))
_PL = ("pañcaviññāṇā purejātavatthukā purejātārammaṇā ajjhattikavatthukā bāhirārammaṇā asambhinnavatthukā "
       "asambhinnārammaṇā nānāvatthukā nānārammaṇā na aññamaññassa gocaravisayaṃ paccanubhonti, na asamannāhārā "
       "uppajjanti, na amanasikārā uppajjanti, na abbokiṇṇā uppajjanti, na apubbaṃ acarimaṃ uppajjanti, ")
P(_PL + "na aññamaññassa samanantarā uppajjanti, nanu pañcaviññāṇā anābhogā",
  Cl(f"{_NANU5}{C} {PV5}သည် စိတ်ညွတ်ခြင်း", "ရှိကြ", "မရှိကြ", neg=True))
_SAMN = _751[11][:-len(" ဖြစ်ပေါ်ကြသည် မဟုတ်")]                        # «အချင်းချင်း၏ ချက်ချင်း နောက်၌»
P(_PL + "nanu pañcaviññāṇā na aññamaññassa samanantarā uppajjanti",
  Cl(f"{f'{C} '.join([f'{PV5}သည် ' + _751[2]] + _751[3:11])}{C} {PV5}သည် {_SAMN}", *UPPAJJK, neg=True))
P("pañcaviññāṇā na aññamaññassa samanantarā uppajjanti", Cl(f"{PV5}သည် {_SAMN}", *UPPAJJK, neg=True))
P("pañcaviññāṇā sābhogā", Cl(f"{PV5}သည် စိတ်ညွတ်ခြင်း", "ရှိကြ", "မရှိကြ"))
P("pañcaviññāṇā kusalāpi akusalāpi", Cl(f"{PV5}သည် ကုသိုလ်လည်း ဖြစ်ကြ၍ အကုသိုလ်လည်း", "ဖြစ်ကြ", "မဖြစ်ကြ"))
VSAM = {"pañcaviññāṇa": PV5, "cakkhuviññāṇa": CVS, "manoviññāṇa": F._DH["manoviññāṇadhātu"].rsplit(" ", 1)[0]}
MBH = "မဂ်ကို ပွားများခြင်း"                                             # maggabhāvanā
for _k, _m in VSAM.items():
    P(f"{_k}samaṅgissa atthi maggabhāvanā", V(f"{_m}နှင့် ပြည့်စုံသူ၌ {MBH}", EXIST))
for _k in ("cakkhuviññāṇa", "manoviññāṇa"):
    _m = VSAM[_k]
    P(f"{_k}ṃ suññataṃ ārabbha uppajjati", Cl(f"{_m}သည် ဆိတ်သုဉ်းခြင်း{ARB}", *UPPAJJ))
    P(f"{_k}ṃ atītānāgataṃ ārabbha uppajjati", Cl(f"{_m}သည် {_ATAN}{ARB}", *UPPAJJ))
    P(f"{_k}ṃ phassaṃ ārabbha", FR(f"{_m}သည် {MF['phasso']}{ARB}"))
    P(f"{_k}ṃ kusalaṃ", V(f"{_m}သည် ကုသိုလ်"))
    P(f"{_k}ṃ kusalampi akusalampi", V(f"{_m}သည် ကုသိုလ်လည်း ဖြစ် အကုသိုလ်လည်း"))   # harmonise A4 (no comma: no «၍ / ၊»)
    P(f"{_k}ṃ sābhogaṃ", V(f"{_m}သည် စိတ်ညွတ်ခြင်း", EXIST))
for _k, _m in (("vedanaṃ", MF["vedanā"]), ("saññaṃ", MF["saññā"]), ("cetanaṃ", MF["cetanā"]), ("cittaṃ", MF["cittaṃ"]),
               ("cakkhuṃ", "မျက်စိ"), ("kāyaṃ", "ကိုယ်"), ("saddaṃ", "အသံ")):
    P(f"{_k} ārabbha", FR(f"{_m}{ARB}"))
P("phoṭṭhabbaṃ ārabbha uppajjati", Cl(f"အထိအတွေ့{ARB}", *UPPAJJ))
_CPR = W("2", "^2-184", "Cakkhuñca paṭicca rūpe ca uppajjati",
         "မျက်စိကိုလည်းကောင်း၊ အဆင်းအရောင်တို့ကိုလည်းကောင်း မှီ၍")
_CPS = "မျက်စိကိုလည်းကောင်း၊ ဆိတ်သုဉ်းခြင်းကိုလည်းကောင်း မှီ၍"
P("cakkhuñca paṭicca suññatañca uppajjati cakkhuviññāṇaṃ", Cl(f"{_CPS} {CVS}", *UPPAJJ))
TH_SUTTA = F.SUTTA_IS                                                 # attheva suttanto (sample ATTHEVA)
for _k, _m in (("suññatañca", _CPS), ("rūpe ca", _CPR)):
    _cl = Cl(f"«{_m} {CVS} ဖြစ်ပေါ်သည်»{F.SUTTA_TI} – {TH_SUTTA}", EXIST, NEXIST)   # harmonise B5: «”ဟု –»
    P(f"cakkhuñca paṭicca {_k} uppajjati cakkhuviññāṇanti – attheva suttanto", _cl)
    if _k == "rūpe ca":
        S(f"Natthi… cakkhuñca paṭicca {_k} uppajjati cakkhuviññāṇanti – attheva suttantoti?",
          f"မရှိပါ… {_cl.f('q')}{END}")
new("X-ti – attheva suttantoti?", f"“X”{F.SUTTA_TI} – {TH_SUTTA} ရှိသလော")
_NMG = "အမှတ်အသားကို စွဲယူသူ"                                          # nimittaggāhī (pi-1 ^1-1354)
_ABG = "အသေးစိတ်ကို စွဲယူသူ"                                           # anubyañjanaggāhī
W("1", "^1-1354", "na nimittaggāhī hoti na anubyañjanaggāhī", f"{_NMG} မဟုတ်၊ {_ABG} မဟုတ်")
_EYE = "မျက်စိဖြင့် အဆင်းအရောင်ကို မြင်၍"
_EAR, _NOSE, _TON, _BOD = ("နားဖြင့် အသံကို ကြား၍", "နှာခေါင်းဖြင့် အနံ့ကို နမ်း၍", "လျှာဖြင့် အရသာကို လျက်၍",
                           "ကိုယ်ဖြင့် အထိအတွေ့ကို ထိ၍")
W("1", "^1-1354", "cakkhunā rūpaṃ disvā", _EYE)
W("1", "^1-1354", "kāyena phoṭṭhabbaṃ phusitvā", _BOD)
_BH = "ရဟန်းတို့၊ ဤသာသနာ၌ ရဟန်းသည်"
Q("idha, bhikkhave, bhikkhu cakkhunā rūpaṃ disvā na nimittaggāhī hoti nānubyañjanaggāhī… sotena saddaṃ sutvā… "
  "ghānena gandhaṃ ghāyitvā… jivhāya rasaṃ sāyitvā… kāyena phoṭṭhabbaṃ phusitvā na nimittaggāhī hoti "
  "nānubyañjanaggāhī",
  f"{_BH} {_EYE} {_NMG} မဟုတ်၊ {_ABG} မဟုတ်… {_EAR}… {_NOSE}… {_TON}… {_BOD} {_NMG} မဟုတ်၊ {_ABG} မဟုတ်")
_NMGP = f"{_NMG} ဖြစ်၏"
Q("idha, bhikkhave, bhikkhu cakkhunā rūpaṃ disvā nimittaggāhī hoti… na nimittaggāhī hoti… sotena saddaṃ sutvā… "
  "kāyena phoṭṭhabbaṃ phusitvā nimittaggāhī hoti… na nimittaggāhī hoti",
  f"{_BH} {_EYE} {_NMGP}… {_NMG} မဟုတ်… {_EAR}… {_BOD} {_NMGP}… {_NMG} မဟုတ်")
Q("idha, bhikkhave, bhikkhu cakkhunā rūpaṃ disvā nimittaggāhī hoti… na nimittaggāhī hoti… kāyena phoṭṭhabbaṃ "
  "phusitvā nimittaggāhī hoti… na nimittaggāhī hoti",
  f"{_BH} {_EYE} {_NMGP}… {_NMG} မဟုတ်… {_BOD} {_NMGP}… {_NMG} မဟုတ်")
BR_X["[ma. ni. 1.349; a. ni. 4.37]"] = f"[{F.REF['ma. ni.']} 1.349{C} {F.REF['a. ni.']} 4.37]"
section("(97) 3. Pañcaviññāṇasamaṅgissa maggakathā", f"(97) 3. {PV5}နှင့် ပြည့်စုံသူ၏ {MAGGA}အကြောင်း {KATHA}")
section("Pañcaviññāṇasamaṅgissa maggakathā", f"{PV5}နှင့် ပြည့်စုံသူ၏ {MAGGA}အကြောင်း {KATHA}")
_KAK = f"{PV5}သည် ကုသိုလ်လည်း ဖြစ်ကြ၍ အကုသိုလ်လည်း ဖြစ်ကြသည်ဟူသော {KATHA}"
section("(98) 4. Pañcaviññāṇā kusalāpi akusalāpītikathā", f"(98) 4. {_KAK}")
section("Pañcaviññāṇā kusalāpi akusalāpītikathā", _KAK)
section("(99) 5. Sābhogātikathā", f"(99) 5. စိတ်ညွတ်ခြင်း ရှိကြသည်ဟူသော {KATHA}")
section("Sābhogātikathā", f"စိတ်ညွတ်ခြင်း ရှိကြသည်ဟူသော {KATHA}")


@F.frame(r"(?P<t>[Tt])ena hi (?P<p>.+?)ti(?P<e>…\.?)")
def _f_tenahi_pe(m):
    """Tena hi P-ti…pe…. (^5-586)"""
    return f"{F.TENA_HI} {F.pq(m['p'], 'stmt')}" + F.endmark(m["e"])


P11.before_generic()
OPEN_Q_X = {}    # lines with an unclosed quotation in the Pāli (source slip): cut by hand, regular marks used
_L581 = [
    "Cakkhuviññāṇaṃ kusalanti?", "Āmantā.", "Cakkhuviññāṇaṃ suññataṃ ārabbha uppajjatīti?", "Na hevaṃ vattabbe…",
    "cakkhuviññāṇaṃ suññataṃ ārabbha uppajjatīti?", "Āmantā.",
    "Cakkhuñca paṭicca suññatañca uppajjati cakkhuviññāṇanti?", "Na hevaṃ vattabbe.",
    "Cakkhuñca paṭicca suññatañca uppajjati cakkhuviññāṇanti?", "Āmantā.",
    "Cakkhuñca paṭicca suññatañca uppajjati cakkhuviññāṇanti – attheva suttantoti?", "Natthi.",
    "Cakkhuñca paṭicca rūpe ca uppajjati cakkhuviññāṇanti – attheva suttantoti?", "Āmantā.",
    "Hañci cakkhuñca paṭicca rūpe ca uppajjati cakkhuviññāṇanti – attheva suttanto, no ca vata re vattabbe – "
    "cakkhuñca paṭicca suññatañca uppajjati cakkhuviññāṇanti."]
OPEN_Q_X[" ".join(_L581)] = _L581

# --- 100. Dvīhisīlehikathā
section("(100) 6. Dvīhisīlehikathā", f"(100) 6. သီလ {F.NUM_MY[2]}{F.CL}နှင့် ပြည့်စုံခြင်းအကြောင်း {KATHA}")
section("Dvīhisīlehikathā", f"သီလ {F.NUM_MY[2]}{F.CL}နှင့် ပြည့်စုံခြင်းအကြောင်း {KATHA}")
LOKIYA, LOKUTT = P11.MAT["lokiya"], W("1", "^1-M2-12", "lokuttarā dhammā", "လောကကို ကျော်လွန်သော")
MS2 = f"{MSG}သည်"
P("maggasamaṅgī dvīhi sīlehi samannāgato", Cl(f"{MS2} သီလ {F.NUM_MY[2]}{F.CL}နှင့်", *SMN))
_D10 = ["phasso", "vedanā", "saññā", "cetanā", "cittaṃ", "saddhā", "vīriyaṃ", "sati", "samādhi", "paññā"]
P("maggasamaṅgī dvīhi phassehi dvīhi vedanāhi dvīhi saññāhi dvīhi cetanāhi dvīhi cittehi dvīhi saddhāhi dvīhi "
  "vīriyehi dvīhi satīhi dvīhi samādhīhi dvīhi paññāhi samannāgato",
  Cl(f"{MS2} " + f"{C} ".join(f"{MF[x]} {F.NUM_MY[2]}{F.CL}" for x in _D10) + "တို့နှင့်", *SMN))
_INS = {"sīlena": ("n", "သီလ"), "phassena": ("n", MF["phasso"]), "vedanāya": ("f", MF["vedanā"]),
        "saññāya": ("f", MF["saññā"]), "cetanāya": ("f", MF["cetanā"]), "cittena": ("n", MF["cittaṃ"]),
        "saddhāya": ("f", MF["saddhā"]), "vīriyena": ("n", MF["vīriyaṃ"]), "satiyā": ("f", MF["sati"]),
        "samādhinā": ("n", MF["samādhi"]), "paññāya": ("f", MF["paññā"])}
_INS.update({ins: ("f" if g == "f" else "n", m) for _, ins, g, m in PF})


def _lk(g, both):
    if both:
        return ("lokiyāya ca lokuttarāya ca" if g == "f" else "lokiyena ca lokuttarena ca",
                f"{LOKIYA} {{m}}နှင့်လည်း {LOKUTT} {{m}}နှင့်လည်း")
    return ("lokiyāya" if g == "f" else "lokiyena", f"{LOKIYA} {{m}}နှင့်")


for _ins, (_g, _m) in _INS.items():
    for _both in (False, True):
        _lp, _lm = _lk(_g, _both)
        _mm = _lm.format(m=_m)
        _bare = _mm[:-len("နှင့်")] if _mm.endswith("နှင့်") else _mm
        P(f"maggasamaṅgī {_lp} {_ins} samannāgato", Cl(f"{MS2} {_mm}", *SMN))
        P(f"{_lp} {_ins} samannāgato", Cl(_mm, *SMN))
        P(f"maggasamaṅgī {_lp} {_ins}", FR(f"{MS2} {_mm}"))
        P(f"{_lp} {_ins}", FR(_mm))
P("sammāājīvena samannāgato", Cl(f"{PFM['sammāājīvo']}နှင့်", *SMN))
_L10 = [("lokiyena", "phassena"), ("lokiyāya", "vedanāya"), ("lokiyāya", "paññāya"), ("lokiyāya", "cetanāya"),
        ("lokiyena", "cittena"), ("lokiyāya", "saddhāya"), ("lokiyena", "vīriyena"), ("lokiyāya", "satiyā"),
        ("lokiyena", "samādhinā"), ("lokiyāya", "paññāya")]
P("maggasamaṅgī " + " ".join(f"{a} {b}" for a, b in _L10) + " samannāgato",
  Cl(f"{MS2} " + f"{C} ".join(f"{LOKIYA} {_INS[b][1]}" for a, b in _L10) + "တို့နှင့်", *SMN))
P("maggasamaṅgī puthujjano", V(f"{MS2} {PUTHU}"))
P("lokiye sīle niruddhe maggo uppajjati", Cl(f"{LOKIYA} သီလ ချုပ်ငြိမ်းပြီးသောအခါ {MAGGA}", *UPPAJJ))
DUSS = W("1", "^1-1333", "dussīlā", "သီလ ပျက်သော")
P("dussīlo khaṇḍasīlo chinnasīlo maggaṃ bhāveti", VV("သီလ ပျက်သူ၊ သီလ ကျိုးသူ၊ သီလ ပြတ်သူသည် မဂ်ကို", "ပွားများ"))

# --- 101. Sīlaṃ acetasikantikathā
CET = W("1", "^1-M2-57", "cetasikā dhammā", "စိတ်၏ အဖော် ဖြစ်သော")
ACET = W("1", "^1-M2-57", "acetasikā dhammā", "စိတ်၏ အဖော် မဟုတ်သော")
CETN = "စိတ်၏ အဖော်"
SILA = "သီလ"
section("(101) 7. Sīlaṃ acetasikantikathā", f"(101) 7. {SILA}သည် {CETN} မဟုတ်ဟူသော {KATHA}")
section("Sīlaṃ acetasikantikathā", f"{SILA}သည် {CETN} မဟုတ်ဟူသော {KATHA}")
CANU = W("1", "^1-M2-62", "cittānuparivattino dhammā", "စိတ်နောက်သို့ လိုက်ပါသော") + " အရာ"   # cittānuparivatti
SUBJ18 = dict(MF)
SUBJ18.update({"sīlaṃ": SILA, "cakkhāyatanaṃ": AY["cakkhāyatanaṃ"]})
SUBJ18.update(PFM)
for _k, _m in SUBJ18.items():
    for _e in ("aṃ", "o", "ā"):
        P(f"{_k} cetasik{_e}", V(f"{_m}သည် {CETN}"))
        P(f"{_k} acetasik{_e}", V(f"{_m}သည် {CETN}", neg=True))
    P(f"{_k} cittānuparivatti", V(f"{_m}သည် {CANU}"))
    P(f"{_k} na cittānuparivatti", V(f"{_m}သည် {CANU}", neg=True))

_R18 = (f"ရုပ်… {NIB}… {AY['cakkhāyatanaṃ']}… {AY['kāyāyatanaṃ']}… {AY['rūpāyatanaṃ']}… "
        f"{AY['phoṭṭhabbāyatanaṃ']}")
P("rūpaṃ… nibbānaṃ… cakkhāyatanaṃ… kāyāyatanaṃ… rūpāyatanaṃ… phoṭṭhabbāyatanaṃ", V(_R18))
P("rūpaṃ… nibbānaṃ… cakkhāyatanaṃ… phoṭṭhabbāyatanaṃ",
  V(f"ရုပ်… {NIB}… {AY['cakkhāyatanaṃ']}… {AY['phoṭṭhabbāyatanaṃ']}"))
_V9 = "vedanā… saññā… cetanā… saddhā… vīriyaṃ… sati… samādhi… paññā"
_V9M = "… ".join(MF[x] for x in ("vedanā", "saññā", "cetanā", "saddhā", "vīriyaṃ", "sati", "samādhi", "paññā"))
for _e in ("ā",):
    P(f"{_V9} acetasik{_e}", V(f"{_V9M}သည် {CETN}", neg=True))
    P(f"{_V9} cetasik{_e}", V(f"{_V9M}သည် {CETN}"))
P(f"{_V9} na cittānuparivatti", V(f"{_V9M}သည် {CANU}", neg=True))
P(f"{_V9} cittānuparivatti", V(f"{_V9M}သည် {CANU}"))
IPH = "လိုလားအပ်သော အကျိုး"                                             # iṭṭhaphala
P("aniṭṭhaphalaṃ", V(f"မ{IPH} ရှိသော အရာ"))
P("iṭṭhaphalaṃ", V(f"{IPH} ရှိသော အရာ"))
for _k, _m in SUBJ18.items():
    for _e in ("aṃ", "ā"):
        P(f"{_k} iṭṭhaphal{_e}", V(f"{_m}သည် {IPH} ရှိသော အရာ"))
for _a, _b in (("vīriyaṃ… sati… samādhi… paññā", "… ".join(MF[x] for x in ("vīriyaṃ", "sati", "samādhi", "paññā"))),):
    P(f"{_a} iṭṭhaphalā", FR(f"{_b}သည် {IPH} ရှိသော အရာ ဖြစ်"))
AVP_ = P6.AVP                                                          # avipāka «အကျိုး မရှိသော» (harmonise B3)
SVP = F.SAVIPAKA
P("aphalaṃ avipākaṃ", V(f"{F.APHALA}၊ {AVP_} အရာ"))          # harmonise B2: = the sample's saphala / savipāka
P("saphalaṃ savipākaṃ", V(f"{F.SAPHALA}၊ {SVP} အရာ"))
for _k, _m in SUBJ18.items():
    P(f"{_k} acetasikaṃ avipākaṃ", V(f"{_m}သည် {CETN} မဟုတ်၍ {AVP_} အရာ"))
    P(f"{_k} acetasikaṃ savipākaṃ", V(f"{_m}သည် {CETN} မဟုတ်၍ {SVP} အရာ"))
P("phoṭṭhabbāyatanaṃ acetasikaṃ avipākaṃ", V(f"{AY['phoṭṭhabbāyatanaṃ']}သည် {CETN} မဟုတ်၍ {AVP_} အရာ"))
P("phoṭṭhabbāyatanaṃ acetasikaṃ savipākaṃ", V(f"{AY['phoṭṭhabbāyatanaṃ']}သည် {CETN} မဟုတ်၍ {SVP} အရာ"))
P("sīle uppajjitvā niruddhe dussīlo hoti", V(f"{SILA} ဖြစ်ပေါ်ပြီး ချုပ်ငြိမ်းသွားသောအခါ သီလ ပျက်သူ"))

# --- 102. Sīlaṃ na cittānuparivattītikathā
section("(102) 8. Sīlaṃ na cittānuparivattītikathā", f"(102) 8. {SILA}သည် {CANU} မဟုတ်ဟူသော {KATHA}")
section("Sīlaṃ na cittānuparivattītikathā", f"{SILA}သည် {CANU} မဟုတ်ဟူသော {KATHA}")

# --- 103. Samādānahetukathā
SAMAD = "ဆောက်တည်ခြင်းကြောင့် ဖြစ်သော"                                   # samādānahetuka
VADD = ("တိုးပွား", "မတိုးပွား")
section("(103) 9. Samādānahetukathā", f"(103) 9. {SAMAD} {SILA}အကြောင်း {KATHA}")
section("Samādānahetukathā", f"{SAMAD} {SILA}အကြောင်း {KATHA}")
P("samādānahetukaṃ sīlaṃ vaḍḍhati", Cl(f"{SAMAD} {SILA}သည်", *VADD))
P("samādānahetuko phasso vaḍḍhati", Cl(f"{SAMAD} {MF['phasso']}သည်", *VADD))
for _k in ("vedanā", "saññā", "cetanā", "cittaṃ", "saddhā", "vīriyaṃ", "sati", "samādhi", "paññā"):
    P(f"{_k} vaḍḍhati", Cl(f"{MF[_k]}သည်", *VADD))
for _k, _m in F.LIKE_GROW:       # harmonise B6: = ch15 (was «မာလုဝါ နွယ်», «ဖြူဆံမြက် အပုံ»)
    P(f"{_k} viya vaḍḍhati", Cl(f"{_m}ကဲ့သို့", *VADD))
_KV = F.strip_id(F.FINAL.seg("2", "^2-910")[2][0]).split("။ ", 1)[1].rstrip("။").split(f"{C} ")
W("2", "^2-910", "Kāmavitakko", _KV[0])
P("sīlaṃ samādiyitvā kāmavitakkaṃ vitakkentassa byāpādavitakkaṃ vitakkentassa vihiṃsāvitakkaṃ vitakkentassa sīlaṃ "
  "vaḍḍhati",
  Cl(f"{SILA}ကို ဆောက်တည်ပြီး၍ {_KV[0]}ကို ပြုနေသူ၊ {_KV[1]}ကို ပြုနေသူ၊ {_KV[2]}ကို ပြုနေသူ၏ {SILA}သည်", *VADD))
_KAK4 = (W("4", "^4-104", "kusalākusale dhamme", "ကုသိုလ် အကုသိုလ်") + "၊ "
         + W("4", "^4-104", "sāvajjānavajje dhamme", "အပြစ် ရှိသော အပြစ် မရှိသော") + "၊ "
         + W("4", "^4-104", "hīnappaṇīte dhamme", "ယုတ်ညံ့သော မွန်မြတ်သော") + "၊ "
         + W("4", "^4-104", "kaṇhasukkasappaṭibhāge dhamme", "မည်းနက်သော ဖြူစင်သော ဆန့်ကျင်ဘက် ရှိသော") + " သဘောတရားတို့")
assert _KAK4 == F.KSA
P("kusalākusalā sāvajjānavajjā hīnapaṇītā kaṇhasukkasappaṭibhāgā dhammā sammukhībhāvaṃ āgacchanti",
  Cl(f"{F.KSA}သည်", *SAMM))           # harmonise B6: + «သည်» as ch15 / ch21 / ch27
Q("cattārimāni, bhikkhave, suvidūravidūrāni! Katamāni cattāri? Nabhañca, bhikkhave, pathavī ca – idaṃ paṭhamaṃ "
  "suvidūravidūraṃ… tasmā sataṃ dhammo asabbhi ārakā",
  f"{F.FAR4_HEAD}… {F.FAR4_LAST}")             # harmonise B6: = ch15
Q("ārāmaropā vanaropā… dhammaṭṭhā sīlasampannā te janā saggagāmino",
  "ဥယျာဉ် စိုက်ပျိုးသူ၊ တော စိုက်ပျိုးသူ… တရား၌ တည်၍ သီလနှင့် ပြည့်စုံသော ထိုလူတို့သည် နတ်ပြည်သို့ သွားကြသူများ ဖြစ်ကြ၏")

# --- 104. Viññatti sīlantikathā
VINN = W("1", "^1-U1", "Atthi rūpaṃ viññatti", "ထုတ်ဖော်ပြသမှု")
AVINN = f"{VINN} မဟုတ်သော အရာ"                                           # aviññatti (pi-1 «na viññatti» pattern)
section("(104) 10. Viññatti sīlantikathā", f"(104) 10. {VINN}သည် {SILA} ဖြစ်သည်ဟူသော {KATHA}")
section("Viññatti sīlantikathā", f"{VINN}သည် {SILA} ဖြစ်သည်ဟူသော {KATHA}")
P("viññatti sīlaṃ", V(f"{VINN}သည် {SILA}"))
_V5 = F.strip_id(F.FINAL.seg("2", "^2-703")[2][0]).split(" – ", 1)[1].rstrip("။").split(f" သိက္ခာပုဒ်{C} ")
_V5[-1] = _V5[-1][:-len(" သိက္ခာပုဒ်")]
for _k, _m in zip(("pāṇātipātā veramaṇī", "adinnādānā veramaṇī", "kāmesumicchācārā veramaṇī", "musāvādā veramaṇī",
                   "surāmerayamajjapamādaṭṭhānā veramaṇī"), _V5):
    P(_k, V(_m))
    P(_k.replace("ā veramaṇī", "o") if _k.startswith(("pāṇ", "kām", "mus")) else _k.replace("ā veramaṇī", "aṃ"),
      V(_m[:-len("မှ ကင်းဝေးခြင်း")]))
W("2", "^2-703", "adinnādānā veramaṇī", _V5[1])
_SL = [("abhivādanaṃ", "ရှိခိုးခြင်း"), ("paccuṭṭhānaṃ", "ထ၍ ကြိုဆိုခြင်း"), ("añjalikammaṃ", "လက်အုပ်ချီခြင်း"),
       ("sāmīcikammaṃ", "ရိုသေစွာ ပြုမူခြင်း"), ("āsanābhihāro", "နေရာ ဆောင်ပေးခြင်း"), ("seyyābhihāro", "အိပ်ရာ ဆောင်ပေးခြင်း"),
       ("pādodakābhihāro", "ခြေဆေးရေ ဆောင်ပေးခြင်း"), ("pādakathalikābhihāro", "ခြေသုတ်ခုံ ဆောင်ပေးခြင်း"),
       ("nhāne piṭṭhiparikammaṃ", "ရေချိုးရာ၌ ကျောကို ပွတ်တိုက်ပေးခြင်း")]
for _k, _m in _SL:
    P(f"{_k} sīlaṃ", V(f"{_m}သည် {SILA}"))
DUSY = W("2", "^2-513", "dussīlyaṃ", "သီလ ပျက်ခြင်း")                    # dussilya (pi-2)
P("dussilyaṃ", V(DUSY))

# --- 105. Aviññatti dussilyantikathā
section("(105) 11. Aviññatti dussilyantikathā", f"(105) 11. {AVINN}သည် {DUSY} ဖြစ်သည်ဟူသော {KATHA}")
section("Aviññatti dussilyantikathā", f"{AVINN}သည် {DUSY} ဖြစ်သည်ဟူသော {KATHA}")
P("aviññatti dussilyaṃ", V(f"{AVINN}သည် {DUSY}"))
PAPA = F.PAPAKAMMA       # pāpakamma (harmonise B3 / B2: the sample's «ယုတ်မာသော ကံ»; was «ဆိုးညစ်သော ကံ»)
P("pāpakammaṃ samādiyitvā dānaṃ dadantassa puññañca apuññañca ubho vaḍḍhanti",
  Cl(f"{PAPA}ကို ဆောက်တည်ပြီး၍ အလှူ ပေးသူ၏ ကောင်းမှုနှင့် မကောင်းမှု နှစ်ပါးစလုံး", "တိုးပွားကြ", "မတိုးပွားကြ"))
P("puññañca apuññañca ubho vaḍḍhanti", Cl("ကောင်းမှုနှင့် မကောင်းမှု နှစ်ပါးစလုံး", "တိုးပွားကြ", "မတိုးပွားကြ"))
P("pāpakammaṃ samādinno āsi", Cl(f"{PAPA}ကို ဆောက်တည်ခဲ့ပြီးသူ", "ဖြစ်ခဲ့", "မဖြစ်ခဲ့"))

# --- 18. uddāna and the paṇṇāsaka
LINES_X[key("Upapattesiye pañcakkhandhe aniruddhe kiriyā pañcakkhandhā uppajjanti, maggasamaṅgissa rūpaṃ maggo, "
            "pañcaviññāṇasamaṅgissa atthi maggabhāvanā, pañcaviññāṇā kusalāpi akusalāpi, pañcaviññāṇā sābhogā, "
            "maggasamaṅgī dvīhi sīlehi samannāgato, sīlaṃ acetasikaṃ, sīlaṃ na cittānuparivatti, samādānahetukaṃ "
            "sīlaṃ vaḍḍhatīti, viññattisīlaṃ aviññatti dussilyanti.")] = (
    f"{_UPA} {KIRIYA} {KH5} ဖြစ်ပေါ်ခြင်း၊ {MSG}၏ ရုပ်သည် {MAGGA} ဖြစ်ခြင်း၊ {PV5}နှင့် ပြည့်စုံသူ၌ {MBH} ရှိခြင်း၊ "
    f"{PV5}သည် ကုသိုလ်လည်း အကုသိုလ်လည်း ဖြစ်ခြင်း၊ {PV5}သည် စိတ်ညွတ်ခြင်း ရှိခြင်း၊ {MS2} သီလ {F.NUM_MY[2]}{F.CL}နှင့် "
    f"ပြည့်စုံခြင်း၊ {SILA}သည် {CETN} မဟုတ်ခြင်း၊ {SILA}သည် {CANU} မဟုတ်ခြင်း၊ {SAMAD} {SILA}သည် တိုးပွားခြင်း၊ "
    f"{VINN}သည် {SILA} ဖြစ်ခြင်း၊ {AVINN}သည် {DUSY} ဖြစ်ခြင်း{END}")
PANN = new("paṇṇāsako (a set of fifty)", "ငါးဆယ်အစု")                    # ch13-16 «Mahāpaṇṇāsako»
S("Dutiyo paṇṇāsako.", f"{F.ORD_MY[2]} {PANN}{END}")
LINES_X[key("Niyāmasaṅgahagatānisaṃsatā ca nirodhoti.")] = (
    f"သေချာသော လမ်းကြောင်း၊ {F.KATHA_NAME['saṅgaha']}၊ လားရာ၊ အကျိုးကျေးဇူးနှင့် ချုပ်ငြိမ်းခြင်း ⟦0⟧" + END)   # B2: saṅgaha = ch15   # vagga 6-10 first kathās
BR_X["[niyāma saṅgahagatānisaṃsatā atthi pañcavokārabhavo nirodho maggasamaṅgissa pañcavokārabhavoti (sī. syā. ka.), "
     "niyāma saṅgaha gatānisaṃsatā atthi pañcavokārabhavo maggasamaṅgissa no pañcavokārabhavo (pī.)]"] = (
    f"[{F.PATHA} (Sī., Syā., Ka.): niyāma saṅgahagatānisaṃsatā atthi pañcavokārabhavo nirodho maggasamaṅgissa "
    f"pañcavokārabhavoti{C} (Pī.): niyāma saṅgaha gatānisaṃsatā atthi pañcavokārabhavo maggasamaṅgissa no "
    f"pañcavokārabhavo]")


# ===================================================================================== 19. Ekādasamavaggo
ORD11 = new("ekādasama (11th)", F.ORD_MY[11])   # harmonise B1: F.ORD_MY
section("Ekādasamavaggo", f"{ORD11} {F.VAGGA_W}")
COLO_X["Ekādasamavaggo"] = HEAD_X["Ekādasamavaggo"]
section("(106-108) 1-3. Tissopi anusayakathā", f"(106-108) 1-3. {ANUS}အကြောင်း {KATHA} {F.NUM_MY[3]}ရပ်လုံး")
section("Tissopi anusayakathā", f"{ANUS}အကြောင်း {KATHA} {F.NUM_MY[3]}ရပ်လုံး")
ABYP = f"{ABYK} အရာ"                                                    # abyākata (predicate)
KLW = dict(KR)
KLW.update(AV)
KLW.update({"paṭighaṃ": "မုန်းတီးမှု", "paṭighapariyuṭṭhānaṃ": f"မုန်းတီးမှု {P11.PARIYUTTH}",
            "paṭighasaṃyojanaṃ": W("1", "^1-1118", "paṭighasaṃyojanaṃ", "မုန်းတီးမှု နှောင်ကြိုး"),
            "māno": "မာန", "mānapariyuṭṭhānaṃ": f"မာန {P11.PARIYUTTH}", "mānasaṃyojanaṃ": "မာန နှောင်ကြိုး",
            "diṭṭhi": "အယူ", "diṭṭhogho": "အယူ ရေအလျဉ်", "diṭṭhiyogo": "အယူ ထမ်းပိုး",
            "diṭṭhipariyuṭṭhānaṃ": f"အယူ {P11.PARIYUTTH}", "diṭṭhisaṃyojanaṃ": "အယူ နှောင်ကြိုး",
            "vicikicchā": MF["vicikicchā"], "vicikicchāpariyuṭṭhānaṃ": f"{MF['vicikicchā']} {P11.PARIYUTTH}",
            "vicikicchāsaṃyojanaṃ": f"{MF['vicikicchā']} {FET}", "vicikicchānīvaraṇaṃ": f"{MF['vicikicchā']} အတားအဆီး",
            "bhavarāgo": "ဘဝရာဂ", "bhavarāgapariyuṭṭhānaṃ": f"ဘဝရာဂ {P11.PARIYUTTH}",
            "bhavarāgasaṃyojanaṃ": "ဘဝရာဂ နှောင်ကြိုး"})
for _k in ("mānasaṃyojanaṃ", "diṭṭhisaṃyojanaṃ", "vicikicchāsaṃyojanaṃ", "bhavarāgasaṃyojanaṃ"):
    W("1", "^1-1118", _k, KLW[_k])


def klist(pali):
    """«kāmarāgo kāmarāgapariyuṭṭhānaṃ… kāmacchandanīvaraṇaṃ» -> Burmese (spaces «၊», «…» kept)."""
    out = []
    for part in pali.split("… "):
        out.append(f"{C} ".join(KLW[w] for w in part.split()))
    return "… ".join(out)


PRED19 = {"abyākat": lambda m: V(f"{m}သည် {ABYP}"), "akusal": lambda m: V(f"{m}သည် အကုသိုလ်"),
          "ahetuk": lambda m: V(f"{m}သည် အမြစ်", EXIST, True), "sahetuk": lambda m: V(f"{m}သည် အမြစ်", EXIST),
          "cittavippayutt": lambda m: V(f"{m}သည် စိတ်နှင့် ကင်းကွာသော အရာ"),
          "cittasampayutt": lambda m: V(f"{m}သည် စိတ်နှင့် ယှဉ်တွဲသော အရာ")}
W("2", "^2-751", "ahetukā", "အမြစ် မရှိ")
W("1", "^1-M2-58", "cittasampayuttā dhammā", "စိတ်နှင့် ယှဉ်တွဲသော")
W("1", "^1-M2-58", "cittavippayuttā dhammā", "စိတ်နှင့် ကင်းကွာသော")
_KL19 = ["kāmarāgo kāmarāgapariyuṭṭhānaṃ kāmarāgasaṃyojanaṃ kāmogho kāmayogo kāmacchandanīvaraṇaṃ",
         "kāmarāgo kāmarāgapariyuṭṭhānaṃ… kāmacchandanīvaraṇaṃ",
         "kāmarāgo kāmarāgapariyuṭṭhānaṃ kāmarāgasaṃyojanaṃ kāmacchandanīvaraṇaṃ",
         "paṭighaṃ paṭighapariyuṭṭhānaṃ paṭighasaṃyojanaṃ", "māno mānapariyuṭṭhānaṃ mānasaṃyojanaṃ",
         "diṭṭhi diṭṭhogho diṭṭhiyogo diṭṭhipariyuṭṭhānaṃ diṭṭhisaṃyojanaṃ",
         "vicikicchā vicikicchāpariyuṭṭhānaṃ vicikicchāsaṃyojanaṃ vicikicchānīvaraṇaṃ",
         "bhavarāgo bhavarāgapariyuṭṭhānaṃ bhavarāgasaṃyojanaṃ",
         "avijjā avijjogho avijjāyogo avijjāpariyuṭṭhānaṃ avijjāsaṃyojanaṃ avijjānīvaraṇaṃ",
         "avijjā avijjogho… avijjānīvaraṇaṃ", "avijjā avijjogho avijjāyogo avijjānīvaraṇaṃ"]
for _l in _KL19:
    for _pr, _fn in PRED19.items():
        P(f"{_l} {_pr}aṃ", _fn(klist(_l)))
_SUB19 = dict(AN7)
_SUB19.update({"anusayā": f"{ANUS}တို့", "rāgo": "ရာဂ", "ñāṇaṃ": "ဉာဏ်", "paññā": "ပညာ", "kāmarāgo": "ကာမရာဂ", "avijjā": _AVJ,
               "saṅkhārakkhandho": KH["saṅkhārakkhandho"],
               "vedanākkhandho saññākkhandho": f"{KH['vedanākkhandho']}{C} {KH['saññākkhandho']}",
               _AN6: f"{C} ".join(list(AN7.values())[1:]),
               "paññā paññindriyaṃ paññābalaṃ sammādiṭṭhi dhammavicayasambojjhaṅgo": _PNM})
for _k, _m in _SUB19.items():
    for _pr, _fn in PRED19.items():
        for _e in ("o", "ā", "aṃ"):
            P(f"{_k} {_pr}{_e}", _fn(_m))
            P(f"{_k} saṅkhārakkhandhapariyāpann{_e} {_pr}{_e}", _fn(f"{SKP} {_m}"))
for _k, _m in list(AN7.items())[1:]:
    P(_k, FR(_m))


@F.frame(r"Na hevaṃ vattabbe… (?P<p>[^a-zāīū…].*?|.+?)(?:ti)?\?")
def _f_no_q(m):
    """Na hevaṃ vattabbe…pe… "P"ti? (a quotation after the elision: the line is not cut there, ^5-618)."""
    return f"{F.NO_SAY}{PE} {F.pq(m['p'], 'q')}{END}"


P11.before_generic()
P("avijjāsaṅkhārakkhandhapariyāpannā cittasampayuttā", PRED19["cittasampayutt"](f"{SKP} {_AVJ}"))   # source slip ^5-612
_VAK = f"ကံ၏ အကျိုး ဖြစ်သော {ABYP}၊ {KIRIYA} {ABYP}"
P("vipākābyākatā kiriyābyākatā rūpaṃ nibbānaṃ cakkhāyatanaṃ… phoṭṭhabbāyatanaṃ", V(f"{_VAK}၊ {RNC}"))
_EKS = f"{EK}သည် စိတ်နှင့် ယှဉ်တွဲသော အရာ ဖြစ်၍ {EK}သည် စိတ်နှင့် ကင်းကွာသော အရာ"
for _k in ("saṅkhārakkhandho", "vedanākkhandho saññākkhandho"):
    P(f"{_k} ekadeso cittasampayutto ekadeso cittavippayutto", V(f"{_SUB19[_k]}၏ {_EKS}"))
P("kusalākusalā dhammā sammukhībhāvaṃ āgacchanti", Cl("ကုသိုလ် အကုသိုလ် သဘောတရားတို့", *SAMM))
P("anusayā tena hetunā sahetukā", Cl(f"{ANUS}တို့သည် ထိုအမြစ်ဖြင့် အမြစ်", "ရှိကြ", "မရှိကြ"))
P("rāgo tena hetunā sahetuko", V("ရာဂသည် ထိုအမြစ်ဖြင့် အမြစ်", EXIST))
P("anusayā tena cittena sampayuttā", V(f"{ANUS}တို့သည် ထိုစိတ်နှင့် ယှဉ်တွဲသော အရာ"))
for _k, _m in (("rāgo", "ရာဂ"), ("ñāṇaṃ", "ဉာဏ်"), ("paññā", "ပညာ")):
    for _e in ("o", "aṃ", "ā"):
        P(f"{_k} tena cittena sampayutt{_e}", V(f"{_m}သည် ထိုစိတ်နှင့် ယှဉ်တွဲသော အရာ"))

# --- 109. Ñāṇakathā
section("(109) 4. Ñāṇakathā", f"(109) 4. ဉာဏ်အကြောင်း {KATHA}")
section("Ñāṇakathā", f"ဉာဏ်အကြောင်း {KATHA}")
ANN = P6.ANNANA                                                        # aññāṇa «မသိခြင်း»
VIG = "ကင်းသွားသောအခါ"                                                  # X-e vigate
NVC = f"{ANN} {VIG} ဉာဏ်နှင့် ကင်းကွာသော စိတ် ဖြစ်နေစဉ်"                 # aññāṇe vigate ñāṇavippayutte citte vattamāne
for _neg, _na in ((True, "na "), (False, "")):
    P(f"aññāṇe vigate ñāṇavippayutte citte vattamāne {_na}vattabbaṃ – ñāṇī", P11.NSAY(NVC, "«ဉာဏ် ရှိသူ»", _neg))
    P(f"rāge vigate {_na}vattabbaṃ – vītarāgo", P11.NSAY(f"ရာဂ {VIG}", f"«{P6.EPI[0][1]}»", _neg))
    P(f"kilese vigate {_na}vattabbaṃ – nikkileso", P11.NSAY(f"ကိလေသာ {VIG}", "«ကိလေသာ ကင်းသူ»", _neg))
for _k, _m in (("dose", "ဒေါသ"), ("mohe", "မောဟ")):
    P(f"{_k} vigate", FR(f"{_m} {VIG}"))
new("X-e vigate", f"X {VIG}")
P("atītena ñāṇena ñāṇī niruddhena vigatena paṭipassaddhena ñāṇena ñāṇī",
  V(f"{TIME['atīt']} ဉာဏ်ဖြင့် ဉာဏ် ရှိသူ၊ ချုပ်ငြိမ်းပြီး၊ ကင်းကွာပြီး၊ ငြိမ်းအေးပြီးသော ဉာဏ်ဖြင့် ဉာဏ် ရှိသူ"))

# --- 110. Ñāṇaṃ cittavippayuttantikathā
_NCV = f"ဉာဏ်သည် စိတ်နှင့် ကင်းကွာသော အရာ ဖြစ်သည်ဟူသော {KATHA}"
section("(110) 5. Ñāṇaṃ cittavippayuttantikathā", f"(110) 5. {_NCV}")
section("Ñāṇaṃ cittavippayuttantikathā", _NCV)
F.NOTE["sakavādīpucchā viya dissati"] = f"{F.SAKAVADI}၏ အမေးကဲ့သို့ ထင်ရသည်"

# --- 111. Idaṃ dukkhantikathā
TRU = P6._TRU
section("(111) 6. Idaṃ dukkhantikathā", f"(111) 6. “{TRU['idaṃ dukkhan']}”ဟူသော {KATHA}")
section("Idaṃ dukkhantikathā", f"“{TRU['idaṃ dukkhan']}”ဟူသော {KATHA}")
COLO_X["Idaṃ dukkhantikathā niṭṭhitā"] = F.DONE.format(f"‘{TRU['idaṃ dukkhan']}’ဟူသော {KATHA}")   # inner marks
PAV = ("ဖြစ်ပွား", "မဖြစ်ပွား")                                         # ñāṇaṃ pavattati
_SAY19 = {"idaṃ dukkhan": TRU["idaṃ dukkhan"], "ayaṃ dukkhasamudayo": TRU["ayaṃ dukkhasamudayo"],
          "ayaṃ dukkhanirodho": TRU["ayaṃ dukkhanirodho"], "ayaṃ maggo": "ဤကား မဂ်",
          "ayaṃ samudayo": "ဤကား ဖြစ်ပေါ်ခြင်း", "ayaṃ nirodho": "ဤကား ချုပ်ငြိမ်းခြင်း"}
for _n, _nm in (("rūpaṃ", "ရုပ်"), ("viññāṇaṃ", F.VINNANA.my)):
    _SAY19[f"{_n} aniccan"] = f"{_nm}သည် မမြဲ"
    _SAY19[f"{_n} anattā"] = f"{_nm}သည် အတ္တ မဟုတ်"
_SAYP = {"idaṃ dukkhan": "idaṃ dukkhanti", "ayaṃ dukkhasamudayo": "ayaṃ dukkhasamudayoti",
         "ayaṃ dukkhanirodho": "ayaṃ dukkhanirodhoti", "ayaṃ maggo": "ayaṃ maggoti", "ayaṃ samudayo": "ayaṃ samudayoti",
         "ayaṃ nirodho": "ayaṃ nirodhoti", "rūpaṃ aniccan": "rūpaṃ aniccanti", "viññāṇaṃ aniccan": "viññāṇaṃ aniccanti",
         "rūpaṃ anattā": "rūpaṃ anattāti", "viññāṇaṃ anattā": "viññāṇaṃ anattāti"}
VBH = "ဟု စကား ပြောနေသူ၌"                                               # "X"ti vācaṃ bhāsato
for _k, _pk in _SAYP.items():
    _q = f"«{_SAY19[_k]}»"
    P(f"{_pk} vācaṃ bhāsato {_pk} ñāṇaṃ pavattati", Cl(f"{_q}{VBH} {_q}ဟု ဉာဏ်", *PAV))
    P(f"{_pk} vācaṃ bhāsato na ca {_pk} ñāṇaṃ pavattati", Cl(f"{_q}{VBH} {_q}ဟု ဉာဏ်ကား", *PAV, neg=True))
    P(_pk, FR(f"{_q}ဟု"))
P("idaṃ dukkhanti vācaṃ bhāsato na ca dukkhanti ñāṇaṃ pavattati",                     # ^5-619 «na ca "dukkha"nti»
  Cl(f"«{TRU['idaṃ dukkhan']}»{VBH} «ဒုက္ခ»ဟု ဉာဏ်ကား", *PAV, neg=True))
_VSS = f"{MF['vedanā']}… {MF['saññā']}… {SK}"
for _neg, _na in ((False, ""), (True, "na ca ")):
    for _k in ("viññāṇaṃ aniccanti", "viññāṇaṃ anattāti"):
        _q = f"«{_SAY19[_k[:-2] if _k.endswith('nti') else _k[:-2]]}»" if False else None
    for _k, _kk in (("viññāṇaṃ aniccanti", "viññāṇaṃ aniccan"), ("viññāṇaṃ anattāti", "viññāṇaṃ anattā")):
        _q = f"«{_SAY19[_kk]}»"
        P(f"vedanā… saññā… saṅkhārā… {_k} vācaṃ bhāsato {_na}{_k} ñāṇaṃ pavattati",
          Cl(f"{_VSS}… {_q}{VBH} {_q}ဟု ဉာဏ်{'ကား' if _neg else ''}", *PAV, neg=_neg))
_IDK = ("“ဣ”ဟူ၍လည်း ⟦0⟧ “ဒံ”ဟူ၍လည်း “ဒု”ဟူ၍လည်း ⟦1⟧ “ခ”ဟူ၍လည်း ဉာဏ် ဖြစ်ပွားသလော" + END)
VAR_X.update({"īti": F.LEKHANA, "dūti": F.LEKHANA})
LINE_PARTS = {}  # whole lines with inner brackets: (units rendered by the engine, hand-written unit with ⟦n⟧ slots)
LINE_PARTS[key('"Idaṃ dukkha"nti vācaṃ bhāsato "idaṃ dukkha"nti ñāṇaṃ pavattatīti? Āmantā. "I"ti ca "da"nti ca '
               '"du"ti ca "kha"nti ca ñāṇaṃ pavattatīti? Na hevaṃ vattabbe…pe….')] = (
    ['Idaṃ dukkhanti vācaṃ bhāsato idaṃ dukkhanti ñāṇaṃ pavattatīti?', "Āmantā."], _IDK, ["Na hevaṃ vattabbe…."])
new("I-ti ca da-nti ca du-ti ca kha-nti ca (the syllables)", "“ဣ”ဟူ၍လည်း “ဒံ”ဟူ၍လည်း “ဒု”ဟူ၍လည်း “ခ”ဟူ၍လည်း")

# --- 112. Iddhibalakathā
IDB = f"{F.IDDHI} စွမ်းအား"                                               # iddhibala
KAPPA = "ကမ္ဘာ"                                                          # kappa (pi-2 «ခြောက်ဆယ့်လေးကမ္ဘာ»)
STAY = F.STAY                                                         # tiṭṭheyya (harmonise B6: one value)
section("(112) 7. Iddhibalakathā", f"(112) 7. {IDB}အကြောင်း {KATHA}")
section("Iddhibalakathā", f"{IDB}အကြောင်း {KATHA}")
IKT = f"{IDB}နှင့် ပြည့်စုံသူသည် {KAPPA} ပတ်လုံး"
P("iddhibalena samannāgato kappaṃ tiṭṭheyya", Cl(IKT, *STAY))
new("iddhibalena samannāgato kappaṃ tiṭṭheyya", f"{IKT} တည်နေရာ")
_IM = f"{F.IDDHI}ဖြင့် ဖြစ်သော အရာ"
P("iddhimayiko so āyu, iddhimayikā sā gati, iddhimayiko so attabhāvappaṭilābho",
  V(f"ထိုသက်တမ်းသည် {_IM} ဖြစ်သည်၊ ထိုလားရာသည် {_IM} ဖြစ်သည်၊ ထိုကိုယ်ခန္ဓာ ရရှိခြင်းသည် {_IM}"))
P("atītaṃ kappaṃ tiṭṭheyya", Cl(f"{TIME['atīt']} {KAPPA} ပတ်လုံး", *STAY))
P("anāgataṃ kappaṃ tiṭṭheyya", Cl(f"{TIME['anāgat']} {KAPPA} ပတ်လုံး", *STAY))
for _k, _n in (("dve", 2), ("tayo", 3), ("cattāro", 4)):
    P(f"{_k} kappe tiṭṭheyya", Cl(f"{F.NUM_MY[_n]}{KAPPA} ပတ်လုံး", *STAY))
_SJ = "အသက်နှင့် အသက်၏ အကြွင်း ရှိနေစဉ်"
_ASJ = "အသက်နှင့် အသက်၏ အကြွင်း မရှိနေစဉ်"
P("sati jīvite jīvitāvasese tiṭṭheyya", Cl(_SJ, *STAY))
P("asati jīvite jīvitāvasese tiṭṭheyya", Cl(_ASJ, *STAY))
P("sati jīvite jīvitāvasese tiṭṭheyya, asati jīvite jīvitāvasese tiṭṭheyya",
  Cl(f"{_SJ} တည်နေရာသလော၊ သို့မဟုတ် {_ASJ}", *STAY))
P("mato tiṭṭheyya", Cl("သေပြီးသူ", *STAY))
P("kālaṅkato tiṭṭheyya", Cl("ကွယ်လွန်ပြီးသူ", *STAY))
LAB = ("ထိန်းထားနိုင်", "ထိန်းထား မနိုင်")                                # labbhā iddhiyā paggahetuṃ
IDP = f"ဟု {F.IDDHI}ဖြင့်"
_UP = {"uppanno phasso": MF["phasso"], "uppannā vedanā": MF["vedanā"], "uppannā saññā": MF["saññā"],
       "uppannā cetanā": MF["cetanā"], "uppannaṃ cittaṃ": MF["cittaṃ"], "uppannā saddhā": MF["saddhā"],
       "uppannaṃ vīriyaṃ": MF["vīriyaṃ"], "uppannā sati": MF["sati"], "uppanno samādhi": MF["samādhi"],
       "uppannā paññā": MF["paññā"]}
MANIR = "မချုပ်ငြိမ်းပါစေနှင့်"                                          # mā nirujjhi
for _k, _m in _UP.items():
    P(_k, FR(f"ဖြစ်ပေါ်ပြီးသော {_m}ကို"))
    P(f"{_k} mā nirujjhīti labbhā iddhiyā paggahetuṃ", Cl(f"ဖြစ်ပေါ်ပြီးသော {_m}ကို {MANIR}{IDP}", *LAB))
P("rūpaṃ niccaṃ hotūti labbhā iddhiyā paggahetuṃ", Cl(f"ရုပ်ကို မြဲပါစေ{IDP}", *LAB))
P("vedanā… saññā… saṅkhārā… viññāṇaṃ niccaṃ hotūti labbhā iddhiyā paggahetuṃ",
  Cl(f"{_VSS}… {F.VINNANA.my}ကို မြဲပါစေ{IDP}", *LAB))
_JD = [("jātidhammā sattā mā jāyiṃsūti", "ဖြစ်ခြင်း သဘော ရှိသော သတ္တဝါတို့ကို မဖြစ်ကြပါစေနှင့်ဟု"),
       ("jarādhammā sattā mā jīriṃsūti", "အိုခြင်း သဘော ရှိသော သတ္တဝါတို့ကို မအိုကြပါစေနှင့်ဟု"),
       ("byādhidhammā sattā mā byādhiyiṃsūti", "နာခြင်း သဘော ရှိသော သတ္တဝါတို့ကို မနာကြပါစေနှင့်ဟု"),
       ("maraṇadhammā sattā mā mīyiṃsūti", "သေခြင်း သဘော ရှိသော သတ္တဝါတို့ကို မသေကြပါစေနှင့်ဟု")]
for _k, _m in _JD:
    P(_k, FR(_m))
    P(f"{_k} labbhā iddhiyā paggahetuṃ", Cl(f"{_m} {F.IDDHI}ဖြင့်", *LAB))
_IDDP = W("2", "^2-9-0", "Iddhipādavibhaṅgo", P6._ID)
Q("yassa kassaci, ānanda, cattāro iddhipādā bhāvitā bahulīkatā yānīkatā vatthukatā anuṭṭhitā paricitā susamāraddhā, "
  "so ākaṅkhamāno kappaṃ vā tiṭṭheyya kappāvasesaṃ vā",
  f"အာနန္ဒာ၊ မည်သူမဆို၏ {_IDDP} {F.NUM_MY[4]}{F.CL}တို့ကို ပွားများထား၏၊ အဖန်ဖန် ပြုထား၏၊ ယာဉ်ကဲ့သို့ ပြုထား၏၊ "
  f"တည်ရာ အခြေကဲ့သို့ ပြုထား၏၊ အမြဲ လေ့ကျင့်ထား၏၊ ကျွမ်းဝင်အောင် ပြုထား၏၊ ကောင်းစွာ အားထုတ်ထား၏၊ ထိုသူသည် "
  f"အလိုရှိလျှင် {KAPPA} ပတ်လုံးဖြစ်စေ၊ {KAPPA}၏ အကြွင်း ပတ်လုံးဖြစ်စေ တည်နေရာ၏")
_GUAR = (f"ရဟန်းဖြစ်စေ၊ ပုဏ္ဏားဖြစ်စေ၊ နတ်ဖြစ်စေ၊ မာရ်ဖြစ်စေ၊ ဗြဟ္မာဖြစ်စေ၊ လောက၌ တစ်စုံတစ်ယောက်ဖြစ်စေ "
         f"အာမခံနိုင်သူ တစ်စုံတစ်ယောက်မျှ မရှိ")
Q("catunnaṃ, bhikkhave, dhammānaṃ natthi koci pāṭibhogo samaṇo vā brāhmaṇo vā devo vā māro vā brahmā vā koci vā "
  "lokasmiṃ! Katamesaṃ catunnaṃ? Jarādhammo mā jīrīti natthi koci pāṭibhogo samaṇo vā brāhmaṇo vā devo vā māro vā "
  "brahmā vā koci vā lokasmiṃ. Byādhidhammo mā byādhiyīti… maraṇadhammo mā mīyīti… yāni kho pana tāni pubbe katāni "
  "pāpakāni kammāni saṃkilesikāni ponobbhavikāni sadarāni dukkhavipākāni āyatiṃ jātijarāmaraṇiyāni tesaṃ vipāko mā "
  "nibbattīti natthi koci pāṭibhogo samaṇo vā brāhmaṇo vā devo vā māro vā brahmā vā koci vā lokasmiṃ. Imesaṃ kho, "
  "bhikkhave, catunnaṃ dhammānaṃ natthi koci pāṭibhogo samaṇo vā brāhmaṇo vā devo vā māro vā brahmā vā koci vā "
  "lokasmin",
  f"ရဟန်းတို့၊ သဘောတရား {F.NUM_MY[4]}{F.CL}တို့အတွက် {_GUAR}{END} အဘယ် {F.NUM_MY[4]}{F.CL}တို့အတွက်နည်း{END} "
  f"အိုခြင်း သဘော ရှိသော အရာကို ‹မအိုပါစေနှင့်›ဟု {_GUAR}{END} နာခြင်း သဘော ရှိသော အရာကို ‹မနာပါစေနှင့်›ဟု… "
  f"သေခြင်း သဘော ရှိသော အရာကို ‹မသေပါစေနှင့်›ဟု… ရှေးက ပြုခဲ့သော၊ ကိလေသာ၏ အာရုံ ဖြစ်နိုင်သော၊ ဘဝသစ်ကို "
  f"ဖြစ်စေတတ်သော ⟦b⟧၊ ပူပန်ဖွယ် ရှိသော ⟦b⟧၊ ဆင်းရဲ အကျိုး ရှိသော၊ နောင်အခါ ဖြစ်ခြင်း အိုခြင်း သေခြင်းကို ဖြစ်စေတတ်သော "
  f"ယုတ်မာသော ကံ မှန်သမျှ၊ ထိုကံတို့၏ အကျိုးကို ‹မဖြစ်ပေါ်ပါစေနှင့်›ဟု {_GUAR}{END} ရဟန်းတို့၊ ဤသဘောတရား "
  f"{F.NUM_MY[4]}{F.CL}တို့အတွက် {_GUAR}")
VAR_X.update({"ponobhavikāni": F.LEKHANA, "nissārāni": F.PATHA, "dukkhudrayāni": F.PATHA})
REF_X["udā."] = "“ဥဒါန်း”"

# --- 113. Samādhikathā
CSN = "စိတ်အစဉ်"                                                        # cittasantati
section("(113) 8. Samādhikathā", f"(113) 8. သမာဓိအကြောင်း {KATHA}")
section("Samādhikathā", f"သမာဓိအကြောင်း {KATHA}")
P("cittasantati samādhi", V(f"{CSN}သည် သမာဓိ"))
P("atītā cittasantati samādhi", V(f"{TIME['atīt']} {CSN}သည် သမာဓိ"))
P("anāgatā cittasantati samādhi", V(f"{TIME['anāgat']} {CSN}သည် သမာဓိ"))
P("atītaṃ niruddhaṃ anāgataṃ ajātaṃ",
  V(f"{TIME['atīt']}သည် ချုပ်ငြိမ်းပြီးသော အရာ ဖြစ်၍ {TIME['anāgat']}သည် မဖြစ်သေးသော အရာ"))
P("ekacittakkhaṇiko samādhi", V(f"သမာဓိသည် စိတ် {F.NUM_MY[1]}ခဏ၌သာ ဖြစ်သော အရာ"))
SAMAP = ("ဝင်စားနေသူ", "ဝင်စားနေသူ မဟုတ်")                               # samāpanno (pi-2 samāpajjati «ဝင်စား»)
_SAG = "နှင့်အတူ ဖြစ်သော"                                               # -sahagata (pi-1)
_CSG = {"cakkhuviññāṇa": CVS, "sotaviññāṇa": F._DH["sotaviññāṇadhātu"].rsplit(" ", 1)[0],
        "ghānaviññāṇa": F._DH["ghānaviññāṇadhātu"].rsplit(" ", 1)[0],
        "jivhāviññāṇa": F._DH["jivhāviññāṇadhātu"].rsplit(" ", 1)[0],
        "kāyaviññāṇa": F._DH["kāyaviññāṇadhātu"].rsplit(" ", 1)[0], "akusalacitta": "အကုသိုလ်စိတ်",
        "rāgasahagatacitta": f"ရာဂ{_SAG} စိတ်", "dosasahagatacitta": f"ဒေါသ{_SAG} စိတ်",
        "mohasahagatacitta": f"မောဟ{_SAG} စိတ်", "anottappasahagatacitta": f"{MF['anottappaṃ']}{_SAG} စိတ်"}
for _k, _m in _CSG.items():
    P(f"{_k}samaṅgī", FR(f"{_m}နှင့် ပြည့်စုံသူ"))
    P(f"{_k}samaṅgī samāpanno", V(f"{_m}နှင့် ပြည့်စုံသူသည် ဝင်စားနေသူ"))
P("akusalacittasantati samādhi", V(f"အကုသိုလ် {CSN}သည် သမာဓိ"))
for _k, _m in (("rāga", "ရာဂ"), ("dosa", "ဒေါသ"), ("moha", "မောဟ")):
    P(f"{_k}sahagatā", FR(f"{_m}{_SAG}"))
P("anottappasahagatā cittasantati samādhi", V(f"{MF['anottappaṃ']}{_SAG} {CSN}သည် သမာဓိ"))
Q("ahaṃ kho, āvuso nigaṇṭhā, pahomi aniñjamāno kāyena, abhāsamāno vācaṃ, satta rattindivāni ekantasukhaṃ "
  "paṭisaṃvedī viharitun",
  f"ငါ့ရှင် နိဂဏ္ဌတို့၊ ငါသည် ကိုယ်ဖြင့် မလှုပ်ရှားဘဲ၊ စကား မပြောဘဲ ခုနစ်ရက်ခုနစ်ညဉ့် ⟦b⟧ ပတ်လုံး "
  f"တစ်ထစ်ချ ချမ်းသာကို ခံစားလျက် နေနိုင်၏")
VAR_X["rattidivāni"] = F.LEKHANA

# --- 114 / 115. Dhammaṭṭhitatā / Aniccatā
PNP = "ပြည့်စုံစွာ ဖြစ်ပေါ်ပြီးသော အရာ"                                  # parinipphanna
THT = "တည်နေခြင်း သဘော"                                                  # ṭhitatā
section("(114) 9. Dhammaṭṭhitatākathā", f"(114) 9. သဘောတရားတို့၏ {THT}အကြောင်း {KATHA}")
section("Dhammaṭṭhitatākathā", f"သဘောတရားတို့၏ {THT}အကြောင်း {KATHA}")
ANC = "မမြဲခြင်း သဘော"                                                   # aniccatā
section("(115) 10. Aniccatākathā", f"(115) 10. {ANC}အကြောင်း {KATHA}")
section("Aniccatākathā", f"{ANC}အကြောင်း {KATHA}")
new("parinipphanna", PNP)
_TH = {"dhammaṭṭhitatā": f"သဘောတရားတို့၏ {THT}", "tāya ṭhitatā": f"ထို{THT}၏ {THT}",
       "rūpassa ṭhitatā": f"ရုပ်၏ {THT}", "vedanāya ṭhitatā": f"{MF['vedanā']}၏ {THT}",
       "saññāya ṭhitatā": f"{MF['saññā']}၏ {THT}", "saṅkhārānaṃ ṭhitatā": f"{SK}၏ {THT}",
       "viññāṇassa ṭhitatā": f"{F.VINNANA.my}၏ {THT}", "aniccatā": ANC, "tāya aniccatāya aniccatā": f"ထို{ANC}၏ {ANC}",
       "jarā": "အိုခြင်း", "tāya jarāya jarā": "ထိုအိုခြင်း၏ အိုခြင်း", "maraṇaṃ": "သေခြင်း",
       "tassa maraṇassa maraṇaṃ": "ထိုသေခြင်း၏ သေခြင်း", "rūpaṃ": "ရုပ်", "viññāṇaṃ": F.VINNANA.my}
for _k, _m in _TH.items():
    for _e in ("ā", "aṃ"):
        P(f"{_k} parinipphann{_e}", V(f"{_m}သည် {PNP}"))
    P(_k, FR(f"{_m}…") if False else FR(_m))
for _k in ("vedanāya ṭhitatā", "saññāya ṭhitatā", "saṅkhārānaṃ ṭhitatā"):
    P(_k, FR(_TH[_k]))
P("vedanā… saññā… saṅkhārā… viññāṇaṃ parinipphannaṃ", V(f"{_VSS}… {F.VINNANA.my}သည် {PNP}"))
for _t in ("tāya tāyeva", "tassa tasseva"):
    P(f"{_t} natthi dukkhassantakiriyā", V(f"ထိုထိုအရာ၏ပင် {F.DUKKHA_END}ခြင်း", EXIST, True))
_AT = {"rūpassa aniccatā": f"ရုပ်၏ {ANC}", "aniccatāya aniccatā": f"{ANC}၏ {ANC}", "rūpassa jarā": "ရုပ်၏ အိုခြင်း",
       "jarāya jarā": "အိုခြင်း၏ အိုခြင်း", "viññāṇassa aniccatā": f"{F.VINNANA.my}၏ {ANC}",
       "viññāṇassa jarā": f"{F.VINNANA.my}၏ အိုခြင်း", "rūpassa bhedo": "ရုပ်၏ ပြိုပျက်ခြင်း",
       "maraṇassa bhedo": "သေခြင်း၏ ပြိုပျက်ခြင်း", "viññāṇassa bhedo": f"{F.VINNANA.my}၏ ပြိုပျက်ခြင်း",
       "antaradhānaṃ": "ကွယ်ပျောက်ခြင်း"}
for _k, _m in _AT.items():
    P(f"{_k} atthi", V(_m, EXIST))

# --- 19. uddāna
LINES_X[key("Anusayā abyākatā, ahetukā, cittavippayuttā, aññāṇe vigate ñāṇī, ñāṇaṃ cittavippayuttaṃ, yattha sadde "
            "ñāṇaṃ pavattati, iddhibalena samannāgato kappaṃ tiṭṭheyya, cittasantati samādhi, dhammaṭṭhitatā, "
            "aniccatāti.")] = (
    f"{ANUS}တို့သည် {ABYK} အရာ ဖြစ်ခြင်း၊ အမြစ် မရှိခြင်း၊ စိတ်နှင့် ကင်းကွာသော အရာ ဖြစ်ခြင်း၊ {ANN} {VIG} ဉာဏ် ရှိသူ၊ "
    f"ဉာဏ်သည် စိတ်နှင့် ကင်းကွာသော အရာ ဖြစ်ခြင်း၊ အကြင် အသံ၌ ⟦0⟧ ဉာဏ် ဖြစ်ပွားခြင်း၊ {IKT} တည်နေရာခြင်း၊ {CSN}သည် သမာဓိ ဖြစ်ခြင်း၊ "
    f"သဘောတရားတို့၏ {THT}၊ {ANC}{END}")
VAR_X.update({"yattha saddo": F.PATHA, "yathāsaddaṃ": F.PATHA})


# ===================================================================================== 20. Dvādasamavaggo
ORD12 = new("dvādasama (12th)", F.ORD_MY[12])   # harmonise B1: F.ORD_MY
section("Dvādasamavaggo", f"{ORD12} {F.VAGGA_W}")
COLO_X["Dvādasamavaggo"] = HEAD_X["Dvādasamavaggo"]

# --- 116. Saṃvaro kammantikathā
SV, ASV = P11.SV, P11.ASV                                               # saṃvaro / asaṃvaro (ch11)
KM = F.KAMMA
section("(116) 1. Saṃvaro kammantikathā", f"(116) 1. {SV}သည် {KM} ဖြစ်သည်ဟူသော {KATHA}")
section("Saṃvaro kammantikathā", f"{SV}သည် {KM} ဖြစ်သည်ဟူသော {KATHA}")
W("1", "^1-985", "kāyakammaṃ, vacīkammaṃ, manokammaṃ", "ကိုယ်ဖြင့် ပြုသော ကံ၊ နှုတ်ဖြင့် ပြုသော ကံ၊ မနောဖြင့် ပြုသော ကံ")
W("1", "^1-1354", "cakkhundriye saṃvaraṃ", "မျက်စိ၏ စွမ်းရည်၌ စောင့်စည်းမှု")
P("saṃvaro kammaṃ", V(f"{SV}သည် {KM}"))
P("asaṃvaro kammaṃ", V(f"{ASV}သည် {KM}"))
P("saṃvaropi asaṃvaropi kammaṃ", V(f"{SV}သည်လည်း {ASV}သည်လည်း {KM}"))
_SI = {"cakkhundriya": ("cakkhukammaṃ", "မျက်စိ"), "sotindriya": ("sotakammaṃ", "နား"),
       "ghānindriya": ("ghānakammaṃ", "နှာခေါင်း"), "jivhindriya": ("jivhākammaṃ", "လျှာ"),
       "kāyindriya": ("kāyakammaṃ", "ကိုယ်"), "manindriya": ("manokammaṃ", "မနော")}
for _i, (_kk, _w) in _SI.items():
    _im = F._IN[_i + "ṃ"]
    for _a, _am in (("saṃvaro", SV), ("asaṃvaro", ASV)):
        P(f"{_i}{_a}", FR(f"{_im}၌ {_am}"))
        P(f"{_i}{_a} {_kk}", V(f"{_im}၌ {_am}သည် {_w}ဖြင့် ပြုသော {KM}"))
_MANAS = "မနောဖြင့် သဘောတရားကို သိ၍"
W("1", "^1-1354", "manasā dhammaṃ viññāya", _MANAS)
Q("idha, bhikkhave, bhikkhu cakkhunā rūpaṃ disvā nimittaggāhī hoti… na nimittaggāhī hoti, sotena saddaṃ sutvā… "
  "manasā dhammaṃ viññāya nimittaggāhī hoti… na nimittaggāhī hoti",
  f"{_BH} {_EYE} {_NMGP}… {_NMG} မဟုတ်၊ {_EAR}… {_MANAS} {_NMGP}… {_NMG} မဟုတ်")

# --- 117. Kammakathā
section("(117) 2. Kammakathā", f"(117) 2. {KM}အကြောင်း {KATHA}")
section("Kammakathā", f"{KM}အကြောင်း {KATHA}")
ALLCET = f"{MF['cetanā']} အားလုံး"
P("sabbaṃ kammaṃ savipākaṃ", V(f"{KM} အားလုံးသည် {SVP} အရာ"))
P("sabbā cetanā savipākā", V(f"{ALLCET}သည် {SVP} အရာ"))
VIPA = f"ကံ၏ အကျိုး ဖြစ်သော {ABYK}"                                       # vipākābyākata
KIRA = f"{KIRIYA} {ABYK}"                                                 # kiriyābyākata
AVC = {"kāmāvacarā": P11.KAMA_AV, "rūpāvacarā": P11.RUPA_AV, "arūpāvacarā": P11.ARUPA_AV, "apariyāpannā": P11.APARIY}
for _pl, _pm in (("", ""), ("kāmāvacarā ", AVC["kāmāvacarā"] + "၊ "), ("rūpāvacarā arūpāvacarā apariyāpannā ",
                 f"{AVC['rūpāvacarā']}၊ {AVC['arūpāvacarā']}၊ {AVC['apariyāpannā']}၊ "),
                 ("rūpāvacarā arūpāvacarā ", f"{AVC['rūpāvacarā']}၊ {AVC['arūpāvacarā']}၊ "),
                 ("kāmāvacarā rūpāvacarā arūpāvacarā apariyāpannā ",
                  f"{AVC['kāmāvacarā']}၊ {AVC['rūpāvacarā']}၊ {AVC['arūpāvacarā']}၊ {AVC['apariyāpannā']}၊ "),
                 ("kāmāvacarā rūpāvacarā arūpāvacarā ",
                  f"{AVC['kāmāvacarā']}၊ {AVC['rūpāvacarā']}၊ {AVC['arūpāvacarā']}၊ "),
                 ("apariyāpannā ", AVC["apariyāpannā"] + "၊ "), ("arūpāvacarā ", AVC["arūpāvacarā"] + "၊ ")):
    for _t, _tm in (("vipākābyākatā", VIPA), ("kiriyābyākatā", KIRA)):
        P(f"{_pl}{_t} cetanā savipākā", V(f"{_pm}{_tm} {MF['cetanā']}သည် {SVP} အရာ"))
        P(f"{_pl}{_t} cetanā avipākā", V(f"{_pm}{_tm} {MF['cetanā']}သည် {AVP_} အရာ"))
Q("nāhaṃ, bhikkhave, sañcetanikānaṃ kammānaṃ katānaṃ upacitānaṃ appaṭisaṃviditvā byantibhāvaṃ vadāmi, tañca kho "
  "diṭṭheva dhamme upapajje vā apare vā pariyāye",
  f"ရဟန်းတို့၊ ငါသည် ရည်ရွယ်၍ ပြုခဲ့ ဆည်းပူးခဲ့သော ကံတို့၏ အကျိုးကို မခံစားရဘဲ ကုန်ဆုံးခြင်းကို မဟော၊ "
  f"ထိုအကျိုးကိုလည်း {W('4', '^4-131', 'diṭṭhe ceva dhamme', 'မျက်မှောက်ဘဝ၌ပင်')}ဖြစ်စေ၊ နောက်ဘဝ၌ဖြစ်စေ၊ "
  f"ထို့နောက် အခြား ဘဝ အလှည့်၌ဖြစ်စေ ခံစားရ၏")
ANCHOR_X["upapajje"] = "နောက်ဘဝ၌ဖြစ်စေ"
VAR_X["upapajjaṃ"] = F.PATHA

# --- 118 / 119. Saddo vipāko / Saḷāyatana
VPK = "ကံ၏ အကျိုး"                                                       # vipāko (pi-1)
section("(118) 3. Saddo vipākotikathā", f"(118) 3. အသံသည် {VPK} ဖြစ်သည်ဟူသော {KATHA}")
section("Saddo vipākotikathā", f"အသံသည် {VPK} ဖြစ်သည်ဟူသော {KATHA}")
SALA = f"{F.AYATANA_W} {F.NUM_MY[6]}{F.CL}"                               # saḷāyatana
section("(119) 4. Saḷāyatanakathā", f"(119) 4. {SALA}အကြောင်း {KATHA}")
section("Saḷāyatanakathā", f"{SALA}အကြောင်း {KATHA}")
VDN = ["သာယာသော ခံစားမှုကို ဖြစ်စေတတ်သော", "နာကျင်သော ခံစားမှုကို ဖြစ်စေတတ်သော",
       "မနာကျင် မသာယာသော ခံစားမှုကို ဖြစ်စေတတ်သော"]                       # -vedaniya
W("1", "^1-M1-2", "sukhāya vedanāya sampayuttā dhammā", "သာယာသော ခံစားမှုနှင့် ယှဉ်တွဲသော")
SBJ20 = {"saddo": "အသံ", "phasso": MF["phasso"], "cakkhāyatanaṃ": AY["cakkhāyatanaṃ"], "kāyāyatanaṃ": AY["kāyāyatanaṃ"],
         "saḷāyatanaṃ": SALA}
for _g, _sfx in (("m", "o"), ("n", "aṃ")):
    _sv, _dv = f"sukhavedaniy{_sfx}", f"dukkhavedaniy{_sfx}"
    P(f"{_sv} {_dv} adukkhamasukhavedaniy{_sfx}", V(f"{VDN[0]}၊ {VDN[1]}၊ {VDN[2]} အရာ"))
    P(f"{_sv} {_dv}", FR(f"{VDN[0]}၊ {VDN[1]}"))
    P(_sv, FR(VDN[0]))
    P(f"na {_sv} na {_dv}", FR(f"{VDN[0]} အရာ မဟုတ်၊ {VDN[1]} အရာ မဟုတ်"))
    P(f"na {_sv}", FR(f"{VDN[0]} အရာ မဟုတ်"))
    P(f"na {_dv}", FR(f"{VDN[1]} အရာ မဟုတ်"))
    for _k, _m in SBJ20.items():
        P(f"{_k} {_sv}", FR(f"{_m}သည် {VDN[0]}"))
        P(f"{_k} na {_sv}", V(f"{_m}သည် {VDN[0]} အရာ", neg=True))
for _k, _m in SBJ20.items():
    P(f"{_k} vipāko", V(f"{_m}သည် {VPK}"))
for _v, _vm in (("sukhāya vedanāya", "သာယာသော ခံစားမှု"), ("dukkhāya vedanāya", "နာကျင်သော ခံစားမှု"),
                ("adukkhamasukhāya vedanāya", "မနာကျင် မသာယာသော ခံစားမှု"), ("phassena", MF["phasso"]),
                ("vedanāya", MF["vedanā"]), ("saññāya", MF["saññā"]), ("cetanāya", MF["cetanā"]), ("cittena", "စိတ်")):
    P(f"{_v} sampayutto", V(f"{_vm}နှင့် ယှဉ်တွဲသော အရာ"))
BR_X["[dīghanikāye]"] = f"[{F.REF['dī. ni.']}၌]"
Q("so tassa kammassa katattā upacitattā ussannattā vipulattā brahmassaro hoti karavikabhāṇī",
  "ထိုသူသည် ထိုကံကို ပြုခဲ့ခြင်း၊ ဆည်းပူးခဲ့ခြင်း၊ များပြားခြင်း၊ ကြွယ်ဝခြင်းကြောင့် ဗြဟ္မာ၏ အသံကဲ့သို့ အသံ ရှိသူ၊ "
  "ကရဝိက်ငှက်ကဲ့သို့ ပြောဆိုသူ ဖြစ်၏")
P("saḷāyatanaṃ kammassa katattā uppannaṃ", V(f"{SALA}သည် ကံကို ပြုခဲ့ခြင်းကြောင့် ဖြစ်ပေါ်ပြီးသော အရာ"))

# --- 120-122. Sattakkhattuparama / Kolaṅkola / Ekabījī
NIYT = W("1", "^1-M1-15", "sammattaniyatā dhammā", "ကျိန်းသေ")         # niyata (pi-1 «… ကျိန်းသေသော»)
NIYM = "ကျိန်းသေမှု"                                                     # niyama
PT = {"sattakkhattuparam": W("4", "^4-M-7", "Sattakkhattuparamo", "အများဆုံး ခုနစ်ကြိမ်သာ ပြန်လည် ဖြစ်ပေါ်သူ"),
      "kolaṅkol": W("4", "^4-M-7", "Kolaṅkolo", "အမျိုးမှ အမျိုးသို့ ကူးသူ"),
      "ekabīj": W("4", "^4-M-7", "Ekabījī", "မျိုးစေ့ တစ်စေ့သာ ရှိသူ")}
_PTP = {"sattakkhattuparam": ("sattakkhattuparamo puggalo", "sattakkhattuparamatāniyato", "sattakkhattuparamo"),
        "kolaṅkol": ("kolaṅkolo puggalo", "kolaṅkolatāniyato", "kolaṅkolo"),
        "ekabīj": ("ekabījī puggalo", "ekabījitāniyato", "ekabījī")}
section("(120) 5. Sattakkhattuparamakathā", f"(120) 5. {PT['sattakkhattuparam']}အကြောင်း {KATHA}")
section("Sattakkhattuparamakathā", f"{PT['sattakkhattuparam']}အကြောင်း {KATHA}")
section("(121) 6. Kolaṅkolakathā", f"(121) 6. {PT['kolaṅkol']}အကြောင်း {KATHA}")
section("Kolaṅkolakathā", f"{PT['kolaṅkol']}အကြောင်း {KATHA}")
section("(122) 7. Ekabījīkathā", f"(122) 7. {PT['ekabīj']}အကြောင်း {KATHA}")
section("Ekabījīkathā", f"{PT['ekabīj']}အကြောင်း {KATHA}")
PTN = {}
for _k, (_pp, _pn, _ps) in _PTP.items():
    _who = f"{PT[_k]} ဖြစ်သော {F.PUGGALA}"
    _niy = f"{PT[_k]}၏ အဖြစ်၌ {NIYT}သူ"            # «… ကျိန်းသေသူ»
    PTN[_k] = (_who, _niy)
    P(f"{_pp} {_pn}", V(f"{_who}သည် {_niy}"))
    P(f"so {_ps}", V(f"ထိုသူသည် {PT[_k]}"))
new("X puggalo X-tāniyato", f"X ဖြစ်သော ပုဂ္ဂိုလ်သည် X၏ အဖြစ်၌ {NIYT}သူ ဖြစ်")
_SKW, _SKN = PTN["sattakkhattuparam"]
_U55 = {"mātā jīvitā voropitā": ("အမိသည် အသက်မှ", "ချခံရ"), "pitā jīvitā voropito": ("အဖသည် အသက်မှ", "ချခံရ"),
        "arahā jīvitā voropito": (f"{ARAHA}သည် အသက်မှ", "ချခံရ"),
        "duṭṭhena cittena tathāgatassa lohitaṃ uppāditaṃ": (f"ပြစ်မှားသော စိတ်ဖြင့် {F.BHAGAVA}၏ သွေးကို", "ထွက်စေအပ်"),
        "saṅgho bhinno": ("သံဃာသည်", "ကွဲပြားစေခံရ")}
W("2", "^2-U55", "Mātā jīvitā voropitā hoti", "အမိသည် အသက်မှ ချခံရ")
W("2", "^2-U55", "saṅgho bhinno hoti", "သံဃာသည် ကွဲပြားစေခံရ")
for _k, (_o, _v) in _U55.items():
    P(_k, Cl(_o, _v, "မ" + _v))
P("abhabbo antarā dhammaṃ abhisametuṃ", Cl("ကြားကာလ၌ တရားကို ထိုးထွင်း သိမြင်ရန်", "ထိုက်တန်", "မထိုက်တန်", neg=True))
_YN = f"အကြင် {NIYM}ဖြင့် {_SKW}သည် {_SKN} ဖြစ်၏၊ ထို{NIYM}"
P("atthi so niyamo yena niyamena sattakkhattuparamo puggalo sattakkhattuparamatāniyato", V(_YN, EXIST))
P("natthi so niyamo yena niyamena sattakkhattuparamo puggalo sattakkhattuparamatāniyato", V(_YN, EXIST, True))
_GR = f"{P6.SATIPATTHANA}… {P6._SP}… {P6._ID}… {F.INDRIYA_W}… စွမ်းအား… {P6._BJW}"
_YB = f"အကြင် {P6._BJW}တို့ဖြင့် {_SKW}သည် {_SKN} ဖြစ်၏၊ ထို"
P("atthi te satipaṭṭhānā… sammappadhānā… iddhipādā… indriyā… balā… bojjhaṅgā yehi bojjhaṅgehi sattakkhattuparamo "
  "puggalo sattakkhattuparamatāniyato", V(f"{_YB}{_GR}", EXIST))
P("natthi te satipaṭṭhānā… bojjhaṅgā yehi bojjhaṅgehi sattakkhattuparamo puggalo sattakkhattuparamatāniyato",
  V(f"{_YB}{P6.SATIPATTHANA}… {P6._BJW}", EXIST, True))
P("natthi te bojjhaṅgā yehi bojjhaṅgehi sattakkhattuparamo puggalo sattakkhattuparamatāniyato",
  V(f"{_YB}{P6._BJW}", EXIST, True))
for _k, _m in (("Sakadāgāminiyamenāti?", F.SAKADAGAMI), ("anāgāminiyamenāti?", F.ANAGAMI),
               ("arahattaniyamenāti?", "ရဟန္တာ အဖြစ်")):
    S(_k, f"{_m}၏ {NIYM}ဖြင့်လော{END}")
S("Katamena niyamenāti?", f"အဘယ် {NIYM}ဖြင့်နည်း{END}")
S("Sotāpattiniyamenāti.", f"သောတာပတ္တိ၏ {NIYM}ဖြင့် ဖြစ်သည်{END}")
P("ye keci sotāpattiniyāmaṃ okkamanti, sabbe te sattakkhattuparamatāniyatā",
  V(f"သောတာပတ္တိ၏ {W('4', '^4-13', 'niyāmaṃ okkamituṃ', 'သေချာသော လမ်းကြောင်းသို့ သက်ဆင်း')}ကြသူ "
    f"မည်သူမဆို ထိုသူ အားလုံးသည် {_SKN}များ"))

# --- 123. Jīvitā voropanakathā
DSP = W("2", "^2-809", "diṭṭhisampanno puggalo", "အယူ ပြည့်စုံသော ပုဂ္ဂိုလ်")
section("(123) 8. Jīvitā voropanakathā", f"(123) 8. အသက်မှ သတ်ခြင်းအကြောင်း {KATHA}")
section("Jīvitā voropanakathā", f"အသက်မှ သတ်ခြင်းအကြောင်း {KATHA}")
SANC = "ရည်ရွယ်၍"                                                       # sañcicca
_KILL = {"pāṇaṃ": "သတ္တဝါကို", "mātaraṃ": "အမိကို", "pitaraṃ": "အဖကို", "arahantaṃ": f"{ARAHA}ကို"}
W("2", "^2-809", "pitaraṃ jīvitā voropeyya", "အဖကို အသက်မှ သတ်ရာ")
for _k, _m in _KILL.items():
    P(f"diṭṭhisampanno puggalo sañcicca {_k} jīvitā voropeyya", Cl(f"{DSP}သည် {SANC} {_m} အသက်မှ", "သတ်ရာ", "မသတ်ရာ"))
    P(f"{_k} jīvitā voropeyya", Cl(f"{_m} အသက်မှ", "သတ်ရာ", "မသတ်ရာ"))
P("duṭṭhena cittena tathāgatassa lohitaṃ uppādeyya", Cl(f"ပြစ်မှားသော စိတ်ဖြင့် {F.BHAGAVA}၏ သွေးကို", "ထွက်စေရာ", "မထွက်စေရာ"))
P("saṅghaṃ bhindeyya", Cl("သံဃာကို", "ခွဲရာ", "မခွဲရာ"))
W("2", "^2-809", "saṅghaṃ bhindeyya", "သံဃာကို ခွဲရာ")
GAR = ("ရိုသေသူ", "မရိုသေသူ")
_STH = W("2", "^2-915", "Satthari kaṅkhati", "ဘုရားရှင်အပေါ်")
_GOBJ = {"satthari": _STH, "dhamme": "တရားတော်အပေါ်", "saṅghe": "သံဃာတော်အပေါ်", "sikkhāya": "သိက္ခာအပေါ်"}
for _k, _m in _GOBJ.items():
    P(f"diṭṭhisampanno puggalo {_k} agāravo", V(f"{DSP}သည် {_m} {GAR[1]}"))
    P(f"diṭṭhisampanno puggalo {_k} sagāravo", V(f"{DSP}သည် {_m} {GAR[0]}"))
P("dhamme… saṅghe… sikkhāya agāravo", V(f"{_GOBJ['dhamme']}… {_GOBJ['saṅghe']}… {_GOBJ['sikkhāya']} {GAR[1]}"))
P("diṭṭhisampanno puggalo dhamme… saṅghe… sikkhāya sagāravo",
  V(f"{DSP}သည် {_GOBJ['dhamme']}… {_GOBJ['saṅghe']}… {_GOBJ['sikkhāya']} {GAR[0]}"))
P("diṭṭhisampanno puggalo buddhathūpe ohadeyya omutteyya niṭṭhubheyya buddhathūpe apabyāmato kareyya",
  Cl(f"{DSP}သည် ဘုရား စေတီ၌ ကျင်ကြီး စွန့်ရာ၊ ကျင်ငယ် စွန့်ရာ၊ တံတွေး ထွေးရာ၊ ဘုရား စေတီကို လက်ဝဲ ထား၍",
     "ပြုရာ", "မပြုရာ"))
ANCHOR_X["apabyāmato"] = "လက်ဝဲ ထား၍"
VAR_X["asabyākato"] = F.PATHA
Q("seyyathāpi, bhikkhave, mahāsamuddo ṭhitadhammo velaṃ nātivattati; evameva kho, bhikkhave, yaṃ mayā sāvakānaṃ "
  "sikkhāpadaṃ paññattaṃ taṃ mama sāvakā jīvitahetupi nātikkamanti",
  f"ရဟန်းတို့၊ ဥပမာအားဖြင့် သမုဒ္ဒရာကြီးသည် တည်မြဲသော သဘော ရှိ၍ ကမ်းစပ်ကို မကျော်လွန်သကဲ့သို့၊ ရဟန်းတို့၊ "
  f"{EVAM} ငါ သတ်မှတ်ထားသော သိက္ခာပုဒ်ကို ငါ၏ {P11.SAV}တို့သည် အသက်ကို အကြောင်းပြု၍ပင် မကျော်လွန်ကြ")
REF_X["cūḷava."] = "“စူဠဝဂ်”"

# --- 124. Duggatikathā
DUG = W("2", "^2-809", "apāyaṃ duggatiṃ vinipātaṃ nirayaṃ", "ဆိုးသော လားရာ")
section("(124) 9. Duggatikathā", f"(124) 9. {DUG}အကြောင်း {KATHA}")
section("Duggatikathā", f"{DUG}အကြောင်း {KATHA}")
PH2 = ("ပယ်ပြီး", "မပယ်ရသေး")
for _k, _m in (("diṭṭhisampannassa puggalassa", DSP), ("arahato", ARAHA), ("sattamabhavikassa puggalassa", None)):
    if _m is None:
        _m = f"{F.NUM_MY[7]}ကြိမ်မြောက် ဘဝ၌ ရှိသော ပုဂ္ဂိုလ်"
    P(f"{_k} pahīnā duggati", Cl(f"{_m}သည် {DUG}ကို", *PH2))
SMB = f"{F.NUM_MY[7]}ကြိမ်မြောက် ဘဝ၌ ရှိသော ပုဂ္ဂိုလ်"                   # sattamabhaviko puggalo
new("sattamabhaviko puggalo", SMB)
APY = "အပါယ်နှင့် ဆိုင်သော"                                              # āpāyika
_SEN = f"{APY} အသံတို့၌… အနံ့တို့၌… အရသာတို့၌… အထိအတွေ့တို့၌"
_MET = f"လူ မဟုတ်သော မိန်းမ၊ တိရစ္ဆာန် မိန်းမ၊ နဂါး သတို့သမီးနှင့် {P6.ACTS['methunaṃ dhammaṃ paṭiseveyya'][0]}"
_A12 = P6.ACTS
_ACTL = [f"{_A12[k][0]} {_A12[k][1]}" for k in ("ajeḷakaṃ paṭiggaṇheyya", "kukkuṭasūkaraṃ paṭiggaṇheyya",
                                                  "hatthigavassavaḷavaṃ paṭiggaṇheyya")]
_TIT = _A12["tittiravaṭṭakamorakapiñjaraṃ paṭiggaṇheyya"]
for _s, _sm in (("diṭṭhisampanno puggalo", DSP), ("arahā", ARAHA)):
    P(f"{_s} āpāyike rūpe rajjeyya", Cl(f"{_sm}သည် {APY} အဆင်းအရောင်တို့၌", "တပ်မက်ရာ", "မတပ်မက်ရာ"))
    P(f"na ca {_s} āpāyike rūpe rajjeyya", Cl(f"{_sm}သည်ကား {APY} အဆင်းအရောင်တို့၌", "တပ်မက်ရာ", "မတပ်မက်ရာ", neg=True))
    P(f"{_s} tittiravaṭṭakamorakapiñjaraṃ paṭiggaṇheyya", Cl(f"{_sm}သည် {_TIT[0]}", _TIT[1], "မ" + _TIT[1]))
    P(f"na ca {_s} tittiravaṭṭakamorakapiñjaraṃ paṭiggaṇheyya",
      Cl(f"{_sm}သည်ကား {_TIT[0]}", _TIT[1], "မ" + _TIT[1], neg=True))
    P(f"{_s} āpāyike sadde… gandhe… rase… phoṭṭhabbe… tittiravaṭṭakamorakapiñjaraṃ paṭiggaṇheyya",
      Cl(f"{_sm}သည် {_SEN}… {_TIT[0]}", _TIT[1], "မ" + _TIT[1]))
_LONG = (" āpāyike sadde… gandhe… rase… phoṭṭhabbe… amanussitthiyā tiracchānagatitthiyā nāgakaññāya methunaṃ "
         "dhammaṃ paṭiseveyya, ajeḷakaṃ paṭiggaṇheyya, kukkuṭasūkaraṃ paṭiggaṇheyya, hatthigavassavaḷavaṃ "
         "paṭiggaṇheyya… tittiravaṭṭakamorakapiñjaraṃ paṭiggaṇheyya")
_LONGM = (f"{_SEN}… {_MET} မှီဝဲရာ၊ {'၊ '.join(_ACTL)}… {_TIT[0]}")
P("diṭṭhisampanno puggalo" + _LONG, Cl(f"{DSP}သည် {_LONGM}", _TIT[1], "မ" + _TIT[1]))
P("na ca arahā" + _LONG, Cl(f"{ARAHA}သည်ကား {_LONGM}", _TIT[1], "မ" + _TIT[1], neg=True))
ANCHOR_X["tittiravaṭṭakamorakapiñjaraṃ"] = P11.ANCHOR_X["tittiravaṭṭakamorakapiñjaraṃ"]
_UPP = {"nirayaṃ": "ငရဲသို့", "tiracchānayoniṃ": "တိရစ္ဆာန် ဘဝသို့", "pettivisayaṃ": "ပြိတ္တာ ဘုံသို့"}
W("2", "^2-811", "tiracchānayonigāmī", "တိရစ္ဆာန် ဘဝသို့")
W("2", "^2-811", "pettivisayagāmī", "ပြိတ္တာ ဘုံသို့")
for _k, _m in _UPP.items():
    P(f"{_k} upapajjeyya", Cl(_m, "ရောက်ရာ", "မရောက်ရာ"))
for _s, _sm in (("diṭṭhisampanno puggalo", DSP), ("sattamabhaviko puggalo", SMB)):
    P(f"{_s} nirayaṃ upapajjeyya", Cl(f"{_sm}သည် {_UPP['nirayaṃ']}", "ရောက်ရာ", "မရောက်ရာ"))
BR_X["[aṭṭhakathānulomaṃ paravādīpucchālakkhaṇaṃ. tathāpāyaṃ pucchā sakavādissa, purimāyo ca imissaṃ duggatikathāyaṃ "
     "paravādissāti gahetabbā viya dissanti]"] = (
    f"[အဋ္ဌကထာနှင့် လျော်ညီစွာ {F.PARAVADI}၏ အမေး၏ အမှတ်အသား ဖြစ်သည်။ သို့သော် ဤအမေးသည် {F.SAKAVADI}၏ အမေး ဖြစ်၍ "
    f"ဤ{DUG}အကြောင်း {KATHA}၌ ရှေ့ အမေးတို့ကို {F.PARAVADI}၏ အမေးဟု ယူရမည်ကဲ့သို့ ထင်ရသည်]")

# --- 125. Sattamabhavikakathā
section("(125) 10. Sattamabhavikakathā", f"(125) 10. {SMB}အကြောင်း {KATHA}")
section("Sattamabhavikakathā", f"{SMB}အကြောင်း {KATHA}")
S("Na vattabbaṃ sattamabhavikassa puggalassa pahīnā duggatīti?",                     # no dash in the Pāli
  f"“{Cl(f'{SMB}သည် {DUG}ကို', *PH2).f('stmt', 1)}”ဟု မဆိုသင့်သလော{END}")

# --- 20. uddāna
LINES_X[key("Saṃvaro kammaṃ tatheva asaṃvaro, sabbakammaṃ savipākaṃ, saddo vipāko, saḷāyatanaṃ vipāko, "
            "sattakkhattuparamo puggalo sattakkhattuparamatāniyato, kolaṅkolapuggalo kolaṅkolatāniyato, ekabījī "
            "puggalo ekabījitāniyato, diṭṭhisampanno puggalo sañcicca pāṇaṃ jīvitā voropeyya, diṭṭhisampannassa "
            "puggalassa pahīnā duggati, tatheva sattamabhavikassāti.")] = (
    f"{SV}သည် {KM} ဖြစ်ခြင်း၊ {TATHEVA} {ASV}၊ {KM} အားလုံးသည် {SVP} အရာ ဖြစ်ခြင်း၊ အသံသည် {VPK} ဖြစ်ခြင်း၊ "
    f"{SALA}သည် {VPK} ဖြစ်ခြင်း၊ {PTN['sattakkhattuparam'][0]}သည် {PTN['sattakkhattuparam'][1]} ဖြစ်ခြင်း၊ "
    f"{PTN['kolaṅkol'][0]}သည် {PTN['kolaṅkol'][1]} ဖြစ်ခြင်း၊ {PTN['ekabīj'][0]}သည် {PTN['ekabīj'][1]} ဖြစ်ခြင်း၊ "
    f"{DSP}သည် {SANC} သတ္တဝါကို အသက်မှ သတ်ရာခြင်း၊ {DSP}သည် {DUG}ကို ပယ်ပြီးခြင်း၊ {TATHEVA} {SMB}၏ အကြောင်း{END}")


# ===================================================================================== run
def install():
    F.VAR_KIND.update(VAR_X)
    F.REF.update(REF_X)
    F.REF_NOTE.update(REF_NOTE_X)
    F._REF_RE = re.compile(r"(?P<r>" + "|".join(re.escape(k) for k in sorted(F.REF, key=len, reverse=True))
                           + r") (?P<n>[\d.\-]+)")
    F.BR_TABLE.update(BR_X)
    F.PROP.update(PROP_X)
    F.QUOTE.update(QUOTE_X)
    F.SENT.update(SENT_X)
    F.LINES.update(LINES_X)
    F.ANCHOR.update(ANCHOR_X)
    F.HEAD.update(HEAD_X)
    F.COLO.update(COLO_X)
    for _k, (_pre, _hand, _post) in LINE_PARTS.items():
        F.LINES[_k] = " ".join([F.unit_my(u) for u in _pre] + [_hand] + [F.unit_my(u) for u in _post])
    for _k, _us in OPEN_Q_X.items():
        assert " ".join(_us) == _k
        F.LINES[_k] = " ".join(F.unit_my(u) for u in _us)


install()


def run(name, misses=False):
    return P6.run(name, misses)


def look(rx, mx=6):
    """Scratch lookup (writes nothing): Pāli lines of the finished pi-5 chapters matching rx, with the Burmese line."""
    rx = re.compile(rx, re.I)
    n = 0
    for f in sorted(OUT.glob("*.md")):
        if f.name in NAMES_OUT:
            continue
        pl = [l for l in (PALI / f.name).read_text(encoding="utf-8-sig").splitlines() if l.strip()]
        ml = [l for l in f.read_text(encoding="utf-8").splitlines() if l.strip()]
        for a, b in zip(pl, ml):
            for x in F.split_sents(F.BR_RE.sub("", a)):
                u = F.BR_RE.sub("", a)[x[0]:x[1]]
                if rx.search(u):
                    n += 1
                    if n <= mx:
                        print(f"== {f.name}\n{u}")
                        try:
                            print(F.unit_my(F.strip_q(u.strip())))
                        except Exception as e:
                            print("  (line)", b[:600])
    print(f"[{n} hits]")


def main():
    args = sys.argv[1:]
    if args and args[0] == "--look":
        look(args[1], int(args[2]) if len(args) > 2 else 6)
        return
    misses = "--misses" in args
    names = [a for a in args if not a.startswith("--")] or NAMES_OUT
    if "--units" in args:
        for name in names:
            P6.units(name)
        return
    total = 0
    for name in names:
        text, bad = run(name, misses)
        total += bad
        if not misses and not bad:
            assert "\n\n\n" not in text
            (OUT / name).write_text(text, encoding="utf-8")
            print(f"wrote {name}")
    if misses:
        print(f"{total} misses")


if __name__ == "__main__":
    main()
