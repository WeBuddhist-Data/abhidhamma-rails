"""Burmese zero-shot of pi-5 (Kathāvatthu, «အငြင်းပွားရာ အကြောင်းအရာများကို ဆွေးနွေးခြင်း»), chapters 26-31:
26-attharasamavaggo, 27-ekunavisatimavaggo, 28-visatimavaggo, 29-ekavisatimavaggo, 30-bavisatimavaggo,
31-tevisatimavaggo (with the book colophon).

usage: python3 -I -X utf8 make_ch26-31.py [chapter ...] [--misses] [--units]
Model: the approved sample. Every line is generated from the Pāli by my5_formulas.translate_line() through the
frames, rules and tables of my5_formulas.py, make_sample.py, make_ch6-10.py and make_ch11-12.py (all imported READ
ONLY: they install their tables at import and write nothing; their __main__ never runs) and the tables of THIS
script, which extends them IN MEMORY only (nothing in my5_formulas.py / make_*.py / my5-zeroshot-terms.md changes).
  * PROP_X (propositions), QUOTE_X (sutta quotations), SENT_X (unique sentences), LINES_X (verses, uddāna),
    HEAD_X / COLO_X (headings, colophons); productive propositions are built from small tables;
  * NEW: every new recurring term or phrase (Pāli = Burmese), copied into notes-ch26-31.md.
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
MS = P11.MS
F = P11.F
from my5_formulas import V, FR, Cl, C, END, PE  # noqa: E402,F401

PALI = MS.PALI
OUT = MS.OUT
NAMES_OUT = ["26-attharasamavaggo.md", "27-ekunavisatimavaggo.md", "28-visatimavaggo.md", "29-ekavisatimavaggo.md",
             "30-bavisatimavaggo.md", "31-tevisatimavaggo.md"]
W = P6.W
PROP_X, QUOTE_X, SENT_X, LINES_X, HEAD_X, COLO_X, ANCHOR_X = {}, {}, {}, {}, {}, {}, {}
VAR_X, REF_X, REF_NOTE_X, BR_X = {}, {}, {}, {}
NEW = {}
REUSED = []      # keys already defined by an earlier chapter: the earlier Burmese is kept (identical Pāli)


def new(pali, my):
    NEW.setdefault(pali, my)
    return my


def section(pali, my):
    if pali in F.HEAD:
        REUSED.append(("HEAD", pali))
        return F.HEAD[pali]
    HEAD_X[pali] = my
    COLO_X[f"{pali} niṭṭhitā"] = F.DONE.format(my)
    new(pali, my)
    return my


KATHA = F.KATHA_W
EXIST, NEXIST = P6.EXIST, P6.NEXIST
key = P11.key


def P(pali, cl):
    k = key(pali)
    k = k[:1].lower() + k[1:]
    if k in F.PROP:
        REUSED.append(("PROP", k))
        return F.PROP[k]
    hit = F.lookup(k)
    if hit is not None and not isinstance(hit[0], type(None)):
        REUSED.append(("RULE", k))
        return hit[0]
    PROP_X[k] = cl
    return cl


def S(pali, my):
    k = key(pali)
    if k in F.SENT:
        REUSED.append(("SENT", k))
        return F.SENT[k]
    SENT_X[k] = my
    return my


def Q(pali, my):
    k = key(pali)
    if k in F.QUOTE:
        REUSED.append(("QUOTE", k))
        return F.QUOTE[k]
    QUOTE_X[k] = my
    return my


VV = P11.VV
NSAY = P11.NSAY


def before_generic():
    """Move the frame just registered before the generic «P-ti?» / «P-ti.» frames."""
    fr = F.FRAMES.pop()
    F.FRAMES.insert(next(i for i, (_, fn) in enumerate(F.FRAMES) if fn is F._f_q), fr)


# ===================================================================================== TABLES

# ===================================================================================== shared vocabulary (ch26-31)
P6_ = P6
BUDDHA = P11.BUDDHA                                                  # bhagavā «မြတ်စွာဘုရား»
BB = "ဘုရားရှင် မြတ်စွာဘုရား"                                          # buddho bhagavā (ch10 VOH «ဘုရားရှင် မြတ်စွာဘုရား၏»)
assert P6.VOH.startswith(BB + "၏")
SAV = P11.SAV                                                        # sāvaka «တပည့်»
SAMANNA = P11.SAMANNA                                                # sāmaññaphala «ရဟန်း၏ အကျိုး» (ch11-12)
MG = P11.MG                                                          # sotāpattimaggo … «သောတာပတ္တိမဂ်» …
PH = dict(P11.PH, arahatta=P6.PAT["arahatta"])                       # sotāpattiphalaṃ … arahattaphalaṃ
JH = P6.JH                                                           # jhāna «ဈာန်»
ORDJ = P6.ORDJ                                                       # paṭhamaṃ … catutthaṃ
ORD_ABL = {"paṭhamā": 1, "dutiyā": 2, "tatiyā": 3, "catutthā": 4}
ORD_GEN = {"paṭhamassa": 1, "dutiyassa": 2, "tatiyassa": 3, "catutthassa": 4}
ORD_ACC = {"paṭhamaṃ": 1, "dutiyaṃ": 2, "tatiyaṃ": 3, "catutthaṃ": 4}
SAMAP = P6.SAMAP                                                     # samāpanno «သမာပတ်ကို ဝင်စားနေသူ»
VV2 = P6.VV2                                                         # vitakkavicārā
KANTAKA = P6.KANTAKA                                                 # kaṇṭako «ဆူးငြောင့်»
SENSE = P6.SENSE
ARUPA4 = P6.ARUPA4
KIL12 = P11.KIL12
EPI11 = P11.EPI11                                                    # jino satthā … dhammappaṭisaraṇo
_R = "ရဟန်းတို့၊"                                                      # bhikkhave (ch11-12)
SAID = ("ဟောတော်မူ", "မဟောတော်မူ")                                     # vuttaṃ bhagavatā (verb)


def vagga(pali, n):
    """### / #### Xvaggo heading and the colophon «Xvaggo.» = «ORD ဝဂ်» (harmonise B1: the Pāli ordinal F.ORD_MY,
    one series book-wide; was «N-ခုမြောက် ဝဂ်»)."""
    my = new(pali, f"{F.ORD_MY[n]} {F.VAGGA_W}")
    HEAD_X[pali] = my
    COLO_X[pali] = my
    return my


def bb(pre, verb, neg=False):
    return Cl(pre, verb, "မ" + verb, neg)


# ===================================================================================== 26. Aṭṭhārasamavaggo
vagga("Aṭṭhārasamavaggo", 18)
# --- (177) 1. Manussalokakathā
MLOKA = new("manussaloka", "လူ့ပြည်")
section("(177) 1. Manussalokakathā", f"(177) 1. {MLOKA}အကြောင်း {KATHA}")
section("Manussalokakathā", f"{MLOKA}အကြောင်း {KATHA}")
STAY_B = new("(buddho bhagavā manussaloke) aṭṭhāsi", "နေတော်မူခဲ့")
P("buddho bhagavā manussaloke aṭṭhāsi", bb(f"{BB}သည် {MLOKA}၌", STAY_B))
P("atthi buddhavutthāni cetiyāni ārāmavihāragāmanigamanagarāni raṭṭhāni janapadāni",
  V(f"{BB} သီတင်းသုံးတော်မူခဲ့သော စေတီ၊ အရံ၊ ကျောင်း၊ ရွာ၊ နိဂုံး၊ မြို့၊ တိုင်း၊ ဇနပုဒ်တို့", EXIST))
P("bhagavā lumbiniyā jāto", bb(f"{BUDDHA}သည် လုမ္ဗိနီ၌", "ဖွားမြင်တော်မူခဲ့"))
P("bodhiyā mūle abhisambuddho", bb("ဗောဓိပင်ရင်း၌ အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ", "သိမြင်တော်မူခဲ့"))
P("bārāṇasiyaṃ bhagavatā dhammacakkaṃ pavattitaṃ", bb(f"ဗာရာဏသီ၌ {BUDDHA}သည် ဓမ္မစကြာကို", "လည်စေတော်မူခဲ့"))
P("cāpāle cetiye āyusaṅkhāro ossaṭṭho", bb("စာပါလ စေတီ၌ အသက်ကို ဆက်လက် တည်စေသော ပြုပြင်ဖန်တီးမှုကို",
                                            "စွန့်လွှတ်တော်မူခဲ့"))
P("kusinārāyaṃ bhagavā parinibbuto", bb(f"ကုသိနာရုံ၌ {BUDDHA}သည်", "ပရိနိဗ္ဗာန် ပြုတော်မူခဲ့"))
_EK = "တစ်ရံရောအခါက ငါသည်"
Q('ekamidāhaṃ, bhikkhave, samayaṃ ukkaṭṭhāyaṃ viharāmi subhagavane sālarājamūleti; ekamidāhaṃ, bhikkhave, samayaṃ '
  'uruvelāyaṃ viharāmi ajapālanigrodhe paṭhamābhisambuddhoti; ekamidāhaṃ, bhikkhave, samayaṃ rājagahe viharāmi veḷuvane '
  'kaḷandakanivāpeti; ekamidāhaṃ, bhikkhave, samayaṃ sāvatthiyaṃ viharāmi jetavane anāthapiṇḍikassa ārāmeti; '
  'ekamidāhaṃ, bhikkhave, samayaṃ vesāliyaṃ viharāmi mahāvane kūṭāgārasālāyan',
  f"{_R} {_EK} ဥက္ကဋ္ဌာ၌ သုဘဂဝုန်တော အင်ကြင်းမင်းပင်ရင်း၌ နေခဲ့၏»ဟူ၍ ⟦b⟧၊ «{_R} {_EK} ဥရုဝေလ၌ အဇပါလ "
  f"ညောင်ပင်ရင်း၌ ဘုရား ဖြစ်စ နေခဲ့၏»ဟူ၍ ⟦b⟧၊ «{_R} {_EK} ရာဇဂြိုဟ်၌ ဝေဠုဝန် ကလန္ဒကနိဝါပ၌ နေခဲ့၏»ဟူ၍ ⟦b⟧၊ "
  f"«{_R} {_EK} သာဝတ္ထိ၌ ဇေတဝန် အနာထပိဏ်သူဌေး၏ အရံ၌ နေခဲ့၏»ဟူ၍၊ «{_R} {_EK} ဝေသာလီ၌ မဟာဝုန်တော "
  f"ကူဋာဂါရ ဇရပ်၌ နေခဲ့၏")
P("bhagavā loke jāto", bb(f"{BUDDHA}သည် လောက၌", "ဖွားမြင်တော်မူ"))
P("loke saṃvaḍḍho", bb("လောက၌", "ကြီးပြင်းတော်မူ"))
P("lokaṃ abhibhuyya viharati anupalitto lokena", bb("လောကကို လွှမ်းမိုး၍ လောကဖြင့် မလိမ်းကျံဘဲ",
                                                       "နေတော်မူ"))
# --- (178) 2. Dhammadesanākathā
DESANA = new("dhammadesanā", "တရား ဟောကြားခြင်း")
section("(178) 2. Dhammadesanākathā", f"(178) 2. {DESANA}အကြောင်း {KATHA}")
section("Dhammadesanākathā", f"{DESANA}အကြောင်း {KATHA}")
P("buddhena bhagavatā dhammo desito", bb(f"{BB}သည် တရားကို", "ဟောတော်မူခဲ့"))
S("Kena desitoti?", f"အဘယ်သူက ဟောခဲ့သနည်း{END}")
NIMM = new("abhinimmito (a created figure)", "ဖန်ဆင်းထားသော သူ")
S("Abhinimmitena desitoti.", f"{NIMM}က ဟောခဲ့သည်{END}")
P("abhinimmito jino satthā sammāsambuddho sabbaññū sabbadassāvī dhammassāmī dhammappaṭisaraṇo",
  V(f"{NIMM}သည် {EPI11}"))
ANANDA = P11.WHO["āyasmā ānando"]                                     # «အသျှင် အာနန္ဒာ»
S("Āyasmatā ānandena desitoti.", f"{ANANDA}က ဟောခဲ့သည်{END}")
P("āyasmā ānando jino satthā sammāsambuddho sabbaññū sabbadassāvī dhammassāmī dhammappaṭisaraṇo",
  V(f"{ANANDA}သည် {EPI11}"))
_SAR = f"{P11.SARIPUTTA}၊ ငါသည်"
Q("saṃkhittenapi kho ahaṃ, sāriputta, dhammaṃ deseyyaṃ; vitthārenapi kho ahaṃ, sāriputta, dhammaṃ deseyyaṃ; "
  "saṃkhittavitthārenapi kho ahaṃ, sāriputta, dhammaṃ deseyyaṃ; aññātāro ca dullabhā",
  f"{_SAR} အကျဉ်းအားဖြင့်လည်း တရားကို ဟောနိုင်၏၊ {_SAR} အကျယ်အားဖြင့်လည်း တရားကို ဟောနိုင်၏၊ {_SAR} "
  f"အကျဉ်းနှင့် အကျယ်အားဖြင့်လည်း တရားကို ဟောနိုင်၏၊ နားလည်သူတို့ကမူ ရှားပါးကြ၏")
REF_NOTE_X["sāriputtasutte"] = "သာရိပုတ္တ သုတ်၌"
_ABH = "ထူးကဲစွာ သိ၍"
Q("‘abhiññāyāhaṃ, bhikkhave, dhammaṃ desemi, no anabhiññāya; sanidānāhaṃ, bhikkhave, dhammaṃ desemi, no anidānaṃ; "
  "sappāṭihāriyāhaṃ, bhikkhave, dhammaṃ desemi, no appāṭihāriyaṃ; tassa mayhaṃ, bhikkhave, abhiññāya dhammaṃ desayato "
  "no anabhiññāya, sanidānaṃ dhammaṃ desayato no anidānaṃ, sappāṭihāriyaṃ dhammaṃ desayato no appāṭihāriyaṃ karaṇīyo "
  "ovādo karaṇīyā anusāsanī; alañca pana vo, bhikkhave, tuṭṭhiyā alaṃ attamanatāya alaṃ somanassāya – "
  "sammāsambuddho bhagavā, svākkhāto dhammo, suppaṭipanno saṅgho’ti. Imasmiñca pana veyyākaraṇasmiṃ bhaññamāne "
  "dasasahassilokadhātu akampitthā",
  f"‹{_R} ငါသည် {_ABH} တရားကို ဟော၏၊ မသိဘဲ မဟော၊ {_R} ငါသည် အကြောင်း ရှိသော တရားကို ဟော၏၊ အကြောင်း "
  f"မရှိသော တရားကို မဟော၊ {_R} ငါသည် အံ့ဖွယ် ရှိသော တရားကို ဟော၏၊ အံ့ဖွယ် မရှိသော တရားကို မဟော၊ {_R} "
  f"ထိုသို့ ⟦b⟧ {_ABH} တရားကို ဟော၍ မသိဘဲ မဟောသော၊ အကြောင်း ရှိသော တရားကို ဟော၍ အကြောင်း မရှိသော "
  f"တရားကို မဟောသော၊ အံ့ဖွယ် ရှိသော တရားကို ဟော၍ အံ့ဖွယ် မရှိသော တရားကို မဟောသော ငါ၏ {F.OVADA}ကို "
  f"လိုက်နာသင့်၏၊ {F.ANUSASANI}ကို လိုက်နာသင့်၏၊ {_R} သင်တို့အဖို့ ကျေနပ်ခြင်းငှာလည်း လုံလောက်၏၊ စိတ် "
  f"နှစ်သက်ခြင်းငှာ လုံလောက်၏၊ ဝမ်းမြောက်ခြင်းငှာ လုံလောက်၏ – {BUDDHA}သည် အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ "
  f"သိမြင်တော်မူသော ဘုရားရှင် ဖြစ်တော်မူ၏၊ တရားတော်ကို ကောင်းစွာ ဟောထား၏၊ သံဃာတော်သည် ကောင်းစွာ ကျင့်ကြံ၏›ဟူ၍။ "
  f"ဤဖြေရှင်းချက်ကို ဟောနေစဉ် စကြဝဠာ တစ်သောင်းသည် တုန်လှုပ်ခဲ့၏")
VAR_X["yañcassa"] = F.PATHA
# --- (179) 3. Karuṇākathā
section("(179) 3. Karuṇākathā", f"(179) 3. ကရုဏာအကြောင်း {KATHA}")
section("Karuṇākathā", f"ကရုဏာအကြောင်း {KATHA}")
BRAH = {"karuṇā": "ကရုဏာ", "mettā": "မေတ္တာ", "muditā": "မုဒိတာ", "upekkhā": "ဥပေက္ခာ"}
W("1", "^1-258", "karuṇāsahagataṃ", "ကရုဏာ")
W("1", "^1-251", "mettāsahagataṃ", "မေတ္တာ")
BB_LOC = f"{BB}၌"
for _k, _m in BRAH.items():
    for _a, _neg in (("atthi", False), ("natthi", True)):
        P(f"{_a} buddhassa bhagavato {_k}", V(f"{BB_LOC} {_m}", EXIST, _neg))
for _a, _neg in (("atthi", False), ("natthi", True)):
    P(f"{_a} buddhassa bhagavato muditā… upekkhā", V(f"{BB_LOC} {BRAH['muditā']}… {BRAH['upekkhā']}", EXIST, _neg))
AKAR = new("akāruṇiko / kāruṇiko", ("ကရုဏာ မရှိသူ", "ကရုဏာ ရှိသူ"))
P("bhagavā akāruṇiko", V(f"{BUDDHA}သည် {AKAR[0]}"))
P("bhagavā kāruṇiko lokahito lokānukampako lokatthacaro",
  V(f"{BUDDHA}သည် {AKAR[1]}၊ လောက၏ အကျိုးကို လိုလားသူ၊ လောကကို သနားစောင့်ရှောက်သူ၊ လောက၏ အကျိုးအတွက် ကျင့်သူ"))
P("bhagavā mahākaruṇāsamāpattiṃ samāpajji", bb(f"{BUDDHA}သည် မဟာကရုဏာ သမာပတ်ကို", "ဝင်စားတော်မူခဲ့"))
P("bhagavā sarāgo", V(f"{BUDDHA}သည် ရာဂ ရှိသူ"))
# --- (180) 4. Gandhajātikathā
UCC = new("uccārapassāvo", "ကျင်ကြီး ကျင်ငယ်")
GJ = new("gandhajāta", "နံ့သာ မျိုး")
section("(180) 4. Gandhajātikathā", f"(180) 4. {GJ}အကြောင်း {KATHA}")
section("Gandhajātikathā", f"{GJ}အကြောင်း {KATHA}")
P("buddhassa bhagavato uccārapassāvo ativiya aññe gandhajāte adhiggaṇhāti",
  bb(f"{BB}၏ {UCC}သည် အခြား {GJ}တို့ကို အလွန်", "လွှမ်းမိုး"))
P("bhagavā gandhabhojī", V(f"{BUDDHA}သည် အနံ့ကို စားသုံးသူ"))
P("bhagavā odanakummāsaṃ bhuñjati", bb(f"{BUDDHA}သည် ထမင်းနှင့် မုန့်ကို", "ဘုဉ်းပေးတော်မူ"))
P("atthi keci buddhassa bhagavato uccārapassāvaṃ nhāyanti vilimpanti ucchādenti peḷāya paṭisāmenti karaṇḍāya "
  "nikkhipanti āpaṇe pasārenti, tena ca gandhena gandhakaraṇīyaṃ karonti",
  V(f"{BB}၏ {UCC}ဖြင့် ရေချိုးကြ၊ လိမ်းကျံကြ၊ ပွတ်တိုက်ကြ ⟦b⟧၊ သေတ္တာ၌ သိမ်းဆည်းကြ၊ ကြုတ်၌ ထည့်ထားကြ၊ "
    f"ဈေး၌ ခင်းကျင်းကြ၍ ထိုအနံ့ဖြင့် နံ့သာ ပြုလုပ်ကြသော အချို့သူတို့", EXIST))
VAR_X["uccārenti"] = F.PATHA
# --- (181) 5. Ekamaggakathā
EKAM = new("ekena ariyamaggena", "အရိယာ မဂ် တစ်ပါးတည်းဖြင့်")
section("(181) 5. Ekamaggakathā", f"(181) 5. မဂ် တစ်ပါးတည်းအကြောင်း {KATHA}")
section("Ekamaggakathā", f"မဂ် တစ်ပါးတည်းအကြောင်း {KATHA}")
_S4 = f"{SAMANNA} {F.NUM_MY[4]}{F.CL}တို့ကို"
SACCHI_V = "မျက်မှောက်ပြု"
P("ekena ariyamaggena cattāri sāmaññaphalāni sacchikaroti", bb(f"{EKAM} {_S4}", SACCHI_V))
P("bhagavā ekena ariyamaggena cattāri sāmaññaphalāni sacchikaroti", bb(f"{BUDDHA}သည် {EKAM} {_S4}", SACCHI_V))
P("sāvakā catūhi ariyamaggehi cattāri sāmaññaphalāni sacchikaronti",
  bb(f"{SAV}တို့သည် အရိယာ မဂ် {F.NUM_MY[4]}{F.CL}တို့ဖြင့် {_S4}", SACCHI_V + "ကြ"))
P("catunnaṃ phassānaṃ… catunnaṃ saññānaṃ samodhānaṃ hoti",
  V(f"တွေ့ထိမှု {F.NUM_MY[4]}{F.CL}… မှတ်သိမှု {F.NUM_MY[4]}{F.CL}တို့၏ ပေါင်းဆုံခြင်း"))
# copied from ch2-5 (make_ch2-5.py SENT_X, checked against 4-jahatikatha.md by check_ch26-31.py)
S("Katamena maggenāti?", f"အဘယ် မဂ်ဖြင့်နည်း{END}")
S("Sotāpattimaggenāti?", f"{MG['sotāpatti']}ဖြင့်လော{END}")
S("Sakadāgāmimaggenāti?", f"{MG['sakadāgāmi']}ဖြင့်လော{END}")
S("sakadāgāmi…pe… anāgāmimaggenāti?", f"သကဒါဂါမိ… {MG['anāgāmi']}ဖြင့်လော{END}")
S("Arahattamaggenāti.", f"{MG['arahatta']}ဖြင့် ဖြစ်သည်{END}")
for _k, _m in KIL12.items():
    P(f"arahattamaggena {_k} jahati", VV(f"{MG['arahatta']}ဖြင့် {_m}ကို", "စွန့်ပယ်"))   # jahati (ch2-5)
BHAVITA = P11.BHAVITA
P("bhagavatā sotāpattimaggo bhāvito", Cl(f"{BUDDHA}သည် {MG['sotāpatti']}ကို", *BHAVITA))
P("bhagavatā sakadāgāmi… anāgāmimaggo bhāvito", Cl(f"{BUDDHA}သည် သကဒါဂါမိ… {MG['anāgāmi']}ကို", *BHAVITA))
P("bhagavā sotāpanno", V(f"{BUDDHA}သည် {F.SOTAPANNA}"))
P("bhagavā anāgāmī", V(f"{BUDDHA}သည် {F.ANAGAMI}"))
P("sāvakā buddhassa bhagavato adiṭṭhaṃ dakkhanti anadhigataṃ adhigacchanti asacchikataṃ sacchikaronti",
  bb(f"{SAV}တို့သည် {BB} မမြင်ဖူးသည်ကို မြင်ကြ၊ မရောက်ဖူးသည်ကို ရောက်ကြ၊ မျက်မှောက် မပြုဖူးသည်ကို",
     SACCHI_V + "ကြ"))
# --- (182) 6. Jhānasaṅkantikathā
SANK = new("saṅkamati (passes over)", "ကူးပြောင်း")
section("(182) 6. Jhānasaṅkantikathā", f"(182) 6. {JH} {SANK}ခြင်းအကြောင်း {KATHA}")
section("Jhānasaṅkantikathā", f"{JH} {SANK}ခြင်းအကြောင်း {KATHA}")
P("jhānā jhānaṃ saṅkamati", VV(f"{JH}မှ {JH}သို့", SANK))
for _a, _x in ORD_ABL.items():
    for _b, _y in ORD_ACC.items():
        if _y > _x:
            P(f"{_a} jhānā {_b} jhānaṃ saṅkamati", VV(f"{F.ORD_MY[_x]} {JH}မှ {F.ORD_MY[_y]} {JH}သို့", SANK))
AVT = W("2", "^2-766", "natthi āvaṭṭanā", "စိတ်ကို လှည့်ဆောင်ခြင်း")       # āvaṭṭanā (pi-2)
PNDH = new("paṇidhi", F.AVATTANA[-1])          # harmonise B6: = ch15 (was «စိတ် ဦးတည်ထားခြင်း»)
AVP = f"{AVT}… {PNDH}"                                                # āvaṭṭanā…pe… paṇidhi
for _g, _x in ORD_GEN.items():
    for _h, _y in ORD_GEN.items():
        if _y == _x + 1:
            P(f"yā {_g} jhānassa uppādāya āvaṭṭanā… paṇidhi, sāva {_h} jhānassa uppādāya āvaṭṭanā… paṇidhi",
              V(f"{F.ORD_MY[_x]} {JH} ဖြစ်ပေါ်ရန် အကြင် {AVP} ရှိ၏၊ ထိုအရာသည်ပင် {F.ORD_MY[_y]} {JH} ဖြစ်ပေါ်ရန် {AVP}"))
            _y_my = PROP_X[f"yā {_g} jhānassa uppādāya āvaṭṭanā… paṇidhi, sāva {_h} jhānassa uppādāya āvaṭṭanā… paṇidhi"]
            P(f"na vattabbaṃ – yā {_g} jhānassa uppādāya āvaṭṭanā… paṇidhi, sāva {_h} jhānassa uppādāya āvaṭṭanā… paṇidhi",
              NSAY("", "«" + _y_my.f("stmt") + "»"))
for _b, _y in ORD_ACC.items():
    P(f"{_b} jhānaṃ anāvaṭṭentassa uppajjati… appaṇidahantassa uppajjati",
      VV(f"{F.ORD_MY[_y]} {JH}သည် စိတ်ကို မလှည့်ဆောင်သူ၌ ဖြစ်ပေါ်၏… စိတ် ဦးမတည်ထားသူ၌", "ဖြစ်ပေါ်"))
    P(f"{_b} jhānaṃ āvaṭṭentassa uppajjati… paṇidahantassa uppajjati",
      VV(f"{F.ORD_MY[_y]} {JH}သည် စိတ်ကို လှည့်ဆောင်သူ၌ ဖြစ်ပေါ်၏… စိတ် ဦးတည်ထားသူ၌", "ဖြစ်ပေါ်"))
ADIN = {"kāme": "ကာမတို့ကို", "vitakkavicāre": f"{VV2}တို့ကို", "pītiṃ": "ပီတိကို"}
for _b, _y in ORD_ACC.items():
    for _o, _om in ADIN.items():
        P(f"{_b} jhānaṃ {_o} ādīnavato manasikaroto uppajjati",
          VV(f"{F.ORD_MY[_y]} {JH}သည် {_om} အပြစ်အားဖြင့် နှလုံးသွင်းသူ၌", "ဖြစ်ပေါ်"))
    P(f"{_b} jhānaṃ savitakkaṃ savicāraṃ", V(f"{F.ORD_MY[_y]} {JH}သည် စတင်ကြံစည်မှု ရှိ၍ ဆက်လက်သုံးသပ်မှု ရှိသော {JH}"))
    P(f"{_b} jhānaṃ sappītikaṃ", V(f"{F.ORD_MY[_y]} {JH}သည် " + W("1", "^1-M2-89", "sappītikā dhammā", "ပီတိ ရှိသော")
                                  + f" {JH}"))
    P(f"{_b} jhānaṃ sukhasahagataṃ", V(f"{F.ORD_MY[_y]} {JH}သည် " + W("1", "^1-M2-91", "sukhasahagatā dhammā",
                                                                       "သာယာမှုနှင့်အတူ ဖြစ်သော") + f" {JH}"))
for _a, _x in ORD_ACC.items():
    for _b, _y in ORD_ACC.items():
        if _y == _x + 1:
            P(f"taññeva {_a} jhānaṃ taṃ {_b} jhānaṃ",
              V(f"ထို{F.ORD_MY[_x]} {JH}သည်ပင် ထို{F.ORD_MY[_y]} {JH}"))
Q("idha, bhikkhave, bhikkhu vivicceva kāmehi… catutthaṃ jhānaṃ upasampajja viharati",
  f"{_R} ဤသာသနာ၌ ရဟန်းသည် ကာမတို့မှ ကင်းဆိတ်၍သာ… စတုတ္ထ {JH}ကို ဝင်စား၍ နေ၏")
W("2", "^2-487", "Idha bhikkhu vivicceva kāmehi", "ဤသာသနာ၌ ရဟန်းသည် ကာမတို့မှ ကင်းဆိတ်၍သာ")
# --- (183) 7. Jhānantarikakathā
JA = new("jhānantarikā", f"{JH}တို့အကြား ကာလ")
section("(183) 7. Jhānantarikakathā", f"(183) 7. {JA}အကြောင်း {KATHA}")
section("Jhānantarikakathā", f"{JA}အကြောင်း {KATHA}")
P("atthi jhānantarikā", V(JA, EXIST))
P("atthi phassantarikā", V("တွေ့ထိမှုတို့အကြား ကာလ", EXIST))
P("atthi saññantarikā", V("မှတ်သိမှုတို့အကြား ကာလ", EXIST))
for _a, _x in ORD_GEN.items():
    for _b, _y in ORD_GEN.items():
        if _y == _x + 1:
            for _e, _neg in (("atthi", False), ("natthi", True)):
                P(f"{_a} ca jhānassa {_b} ca jhānassa antare {_e} jhānantarikā",
                  V(f"{F.ORD_MY[_x]} {JH}နှင့် {F.ORD_MY[_y]} {JH}တို့၏ အကြား၌ {JA}", EXIST, _neg))
_SM2 = F.FINAL.seg("2", "^2-828")[2][12]
SAMADHI3 = {"savitakko savicāro samādhi": "စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှု ရှိသော သမာဓိ",
            "avitakko vicāramatto samādhi": "စတင်ကြံစည်မှု မရှိဘဲ ဆက်လက်သုံးသပ်မှုသာ ရှိသော သမာဓိ",
            "avitakko avicāro samādhi": "စတင်ကြံစည်မှုလည်း မရှိ၊ ဆက်လက်သုံးသပ်မှုလည်း မရှိသော သမာဓိ"}
assert all(v in _SM2 for v in SAMADHI3.values()), _SM2
W("2", "^2-828", "avitakkavicāramatto samādhi", SAMADHI3["avitakko vicāramatto samādhi"])
for _k, _m in SAMADHI3.items():
    P(f"{_k} jhānantarikā", V(f"{_m}သည် {JA}"))
    P(f"{_k} na jhānantarikā", V(f"{_m}သည် {JA}", neg=True))
AVM = SAMADHI3["avitakko vicāramatto samādhi"]
P("dvinnaṃ jhānānaṃ paṭuppannānamantare avitakko vicāramatto samādhi",
  V(f"ဖြစ်ပေါ်နေသော {JH} {F.NUM_MY[2]}{F.CL}တို့၏ အကြား၌ {AVM}", EXIST))
P("dvinnaṃ jhānānaṃ paṭuppannānamantare avitakko vicāramatto samādhi jhānantarikā",
  V(f"ဖြစ်ပေါ်နေသော {JH} {F.NUM_MY[2]}{F.CL}တို့၏ အကြား၌ ရှိသော {AVM}သည် {JA}"))
P("avitakke vicāramatte samādhimhi vattamāne paṭhamaṃ jhānaṃ niruddhaṃ dutiyaṃ jhānaṃ paṭuppannaṃ",
  VV(f"{AVM} ဖြစ်နေစဉ် ပထမ {JH} ချုပ်ငြိမ်းပြီး ဒုတိယ {JH}", "ဖြစ်ပေါ်နေ"))
P("avitakko vicāramatto samādhi paṭhamaṃ jhānaṃ… dutiyaṃ jhānaṃ… tatiyaṃ jhānaṃ… catutthaṃ jhānaṃ",
  V(f"{AVM}သည် ပထမ {JH}… ဒုတိယ {JH}… တတိယ {JH}… စတုတ္ထ {JH}"))
_S3 = f"သမာဓိ {F.NUM_MY[3]}{F.CL}တို့ကို {BUDDHA}"
P("tayo samādhī vuttā bhagavatā – savitakko savicāro samādhi, avitakko vicāramatto samādhi, avitakko avicāro samādhi",
  Cl(_S3, *SAID, post=" – " + "၊ ".join(SAMADHI3.values())))
P("tayo samādhī vuttā bhagavatā – savitakko… avicāro samādhi",
  Cl(_S3, *SAID, post=" – စတင်ကြံစည်မှုနှင့်… ဆက်လက်သုံးသပ်မှုလည်း မရှိသော သမာဓိ"))
BR_X["[a. ni. 2.13; 4.163]"] = f"[{F.REF['a. ni.']} 2.13၊ 4.163]"
BR_X["[dī. ni. 3.305, 353]"] = f"[{F.REF['dī. ni.']} 3.305, 353]"
# --- (184) 8. Saddaṃ suṇātītikathā
HEAR = f"{SAMAP}သည် အသံကို"
section("(184) 8. Saddaṃ suṇātītikathā", f"(184) 8. အသံကို ကြားသည် ဟူသော {KATHA}")
section("Saddaṃ suṇātītikathā", f"အသံကို ကြားသည် ဟူသော {KATHA}")
P("samāpanno saddaṃ suṇāti", VV(HEAR, "ကြား"))
P("samāpanno cakkhunā rūpaṃ passati… sotena… ghānena… jivhāya… kāyena phoṭṭhabbaṃ phusati",
  VV(f"{SAMAP}သည် {SENSE['cakkhunā rūpaṃ passati']}… နားဖြင့်… နှာခေါင်းဖြင့်… လျှာဖြင့်… ကိုယ်ဖြင့် အထိအတွေ့ကို", "ထိ"))
SVS = new("sotaviññāṇasamaṅgī", "နား သိစိတ်နှင့် ပြည့်စုံနေသူ")
MVS = new("manoviññāṇasamaṅgissa", "မနော သိစိတ်နှင့် ပြည့်စုံနေသူ၌")
P("sotaviññāṇasamaṅgī samāpanno", V(f"{SVS}သည် {SAMAP}"))
P("samādhi manoviññāṇasamaṅgissa", V(f"{MVS} သမာဓိ", EXIST))
P("sotaviññāṇasamaṅgī saddaṃ suṇāti", VV(f"{SVS}သည် အသံကို", "ကြား"))
P("dvinnaṃ phassānaṃ… dvinnaṃ cittānaṃ samodhānaṃ hoti",
  V(f"တွေ့ထိမှု {F.NUM_MY[2]}{F.CL}… စိတ် {F.NUM_MY[2]}{F.CL}တို့၏ ပေါင်းဆုံခြင်း"))
P("dutiyassa jhānassa vitakko vicāro kaṇṭako vutto bhagavatā",
  Cl(f"ဒုတိယ {JH}၏ {VV2}သည် {KANTAKA}ဟု {BUDDHA}", *SAID))
P("atthi tassa vitakkavicārā", V(f"ထိုသူ၌ {VV2}တို့", EXIST))
SVN = "မှတ်သိမှုနှင့် ခံစားရခြင်း ချုပ်ငြိမ်းရာ ဈာန်"
W("2", "^2-808", "saññāvedayitanirodhasamāpattiyā", SVN)
_SQ = lambda x: f"{x}ကို ဝင်စားနေသူ၏"
P("tatiyassa jhānassa pīti kaṇṭako… catutthassa jhānassa assāsapassāso kaṇṭako… ākāsānañcāyatanaṃ samāpannassa "
  "rūpasaññā kaṇṭako… viññāṇañcāyatanaṃ samāpannassa ākāsānañcāyatanasaññā kaṇṭako… ākiñcaññāyatanaṃ samāpannassa "
  "viññāṇañcāyatanasaññā kaṇṭako… nevasaññānāsaññāyatanaṃ samāpannassa ākiñcaññāyatanasaññā kaṇṭako… "
  "saññāvedayitanirodhaṃ samāpannassa saññā ca vedanā ca kaṇṭako vutto bhagavatā",
  Cl(f"တတိယ {JH}၏ ပီတိသည် {KANTAKA}… စတုတ္ထ {JH}၏ ဝင်လေ ထွက်လေသည် {KANTAKA}… "
     f"{_SQ(ARUPA4['ākāsānañcāyatanaṃ'])} ရုပ်ဟု မှတ်သိမှုသည် {KANTAKA}… "
     f"{_SQ(ARUPA4['viññāṇañcāyatanaṃ'])} {ARUPA4['ākāsānañcāyatanaṃ']}ဟု မှတ်သိမှုသည် {KANTAKA}… "
     f"{_SQ(ARUPA4['ākiñcaññāyatanaṃ'])} {ARUPA4['viññāṇañcāyatanaṃ']}ဟု မှတ်သိမှုသည် {KANTAKA}… "
     f"{_SQ(ARUPA4['nevasaññānāsaññāyatanaṃ'])} {ARUPA4['ākiñcaññāyatanaṃ']}ဟု မှတ်သိမှုသည် {KANTAKA}… "
     f"{_SQ(SVN)} မှတ်သိမှုနှင့် ခံစားမှုသည် {KANTAKA}ဟု {BUDDHA}", *SAID))
P("atthi tassa saññā ca vedanā ca", V(f"ထိုသူ၌ မှတ်သိမှုနှင့် ခံစားမှု", EXIST))
# --- (185) 9. Cakkhunā rūpaṃ passatītikathā
section("(185) 9. Cakkhunā rūpaṃ passatītikathā", f"(185) 9. {SENSE['cakkhunā rūpaṃ passati']}သည် ဟူသော {KATHA}")
section("Cakkhunā rūpaṃ passatītikathā", f"{SENSE['cakkhunā rūpaṃ passati']}သည် ဟူသော {KATHA}")
for _k, _m in SENSE.items():
    _pre, _v = _m.rsplit(" ", 1)
    P(_k, VV(_pre, _v))
for _v, _m in (("passati", "မြင်"), ("paṭivijānāti", "ခွဲခြား သိ"), ("phusati", "ထိ")):
    P(f"rūpena rūpaṃ {_v}", VV("ရုပ်ဖြင့် ရုပ်ကို", _m))
P("rūpaṃ manoviññāṇaṃ", V("ရုပ်သည် မနော သိစိတ်"))
for _o, _om in (("cakkhussa", "မျက်စိ"), ("kāyassa", "ကိုယ်")):
    for _e, _neg in (("atthi", False), ("natthi", True)):
        P(f"{_e} {_o} āvaṭṭanā… paṇidhi", V(f"{_om}၌ {AVP}", EXIST, _neg))
Q("idha, bhikkhave, bhikkhu cakkhunā rūpaṃ passati… kāyena phoṭṭhabbaṃ phusati",
  f"{_R} ဤသာသနာ၌ ရဟန်းသည် {SENSE['cakkhunā rūpaṃ passati']}၏… {SENSE['kāyena phoṭṭhabbaṃ phusati']}၏")
BR_X["[ma. ni. 1.349; a. ni. 4.37 (aṭṭhakathā passitabbā)]"] = (
    f"[{F.REF['ma. ni.']} 1.349၊ {F.REF['a. ni.']} 4.37 (အဋ္ဌကထာကို ကြည့်ပါ)]")
LINES_X[key("Buddho bhagavā manussaloke aṭṭhāsi, buddhena bhagavatā dhammo desito, natthi buddhassa bhagavato karuṇā, "
            "buddhassa bhagavato uccārapassāvo ativiya aññe gandhajāte adhiggaṇhāti, ekena ariyamaggena cattāri "
            "sāmaññaphalāni sacchikaroti, jhānā jhānaṃ saṅkamati, atthi jhānantarikā, samāpanno saddaṃ suṇāti, "
            "cakkhunā rūpaṃ passati kāyena phoṭṭhabbaṃ phusati.")] = (
    f"{BB}သည် {MLOKA}၌ {STAY_B}၊ {BB}သည် တရားကို ဟောတော်မူခဲ့၊ {BB_LOC} ကရုဏာ မရှိ၊ {BB}၏ {UCC}သည် "
    f"အခြား {GJ}တို့ကို အလွန် လွှမ်းမိုး၊ {EKAM} {_S4} မျက်မှောက်ပြု၊ {JH}မှ {JH}သို့ {SANK}၊ {JA} ရှိ၊ "
    f"{HEAR} ကြား၊ {SENSE['cakkhunā rūpaṃ passati']}၊ {SENSE['kāyena phoṭṭhabbaṃ phusati']}{END}")

# ===================================================================================== 27. Ekūnavīsatimavaggo
vagga("Ekūnavīsatimavaggo", 19)
KIL = F.witness("1", "^1-M2-75", "kilesā dhammā", "ကိလေသာ")
KILS = f"{KIL}တို့"
TIME3 = {"atīte": P6.ATITA, "anāgate": P6.ANAGATA, "paccuppanne": P6.PACCUP}
# --- (186) 1. Kilesajahanakathā
JAHATI = "စွန့်ပယ်"                                                    # jahati (make_ch2-5.py NEW «jahati = စွန့်ပယ်»)
section("(186) 1. Kilesajahanakathā", f"(186) 1. {KIL} {JAHATI}ခြင်းအကြောင်း {KATHA}")
section("Kilesajahanakathā", f"{KIL} {JAHATI}ခြင်းအကြောင်း {KATHA}")
for _k, _m in TIME3.items():
    P(f"{_k} kilese jahati", VV(f"{_m} {KILS}ကို", JAHATI))
P("natthi kilese jahati", V(f"{KILS}ကို {JAHATI}ခြင်း", EXIST, True))
for _k, _m in (("niruddhaṃ nirodheti", ("ချုပ်ငြိမ်းပြီးသော", "ချုပ်ငြိမ်းစေ")),
               ("vigataṃ vigameti", ("ကင်းပျောက်ပြီးသော", "ကင်းပျောက်စေ")),
               ("khīṇaṃ khepeti", ("ကုန်ခန်းပြီးသော", "ကုန်ခန်းစေ")),
               ("atthaṅgataṃ atthaṅgameti", ("ကွယ်ပျောက်ပြီးသော", "ကွယ်ပျောက်စေ")),
               ("abbhatthaṅgataṃ abbhatthaṅgameti", ("လုံးဝ ကွယ်ပျောက်ပြီးသော", "လုံးဝ ကွယ်ပျောက်စေ"))):
    P(_k, VV(f"{_m[0]} အရာကို", _m[1]))
for _k, _m in (("ajātaṃ ajaneti", ("မမွေးဖွားသေးသော", "မမွေးဖွားစေ")),
               ("asañjātaṃ asañjaneti", ("မပေါ်ပေါက်သေးသော", "မပေါ်ပေါက်စေ")),
               ("anibbattaṃ anibbatteti", ("မဖြစ်ထွန်းသေးသော", "မဖြစ်ထွန်းစေ")),
               ("apātubhūtaṃ apātubhāveti", ("မထင်ရှားသေးသော", "မထင်ရှားစေ"))):
    P(_k, Cl(f"{_m[0]} အရာကို", _m[1], _m[1]))
P("atītaṃ niruddhaṃ", Cl(P6.ATITA, *P6.DONE7["niruddhaṃ"]))
P("anāgataṃ ajātaṃ", Cl(P6.ANAGATA, "မမွေးဖွားသေး", "မမွေးဖွားသေး"))
for _w, _k, _o in (("ratto", "rāgaṃ", "တပ်မက်နေသူသည် ရာဂကို"), ("duṭṭho", "dosaṃ", "ဒေါသ ဖြစ်နေသူသည် ဒေါသကို"),
                   ("mūḷho", "mohaṃ", "တွေဝေနေသူသည် မောဟကို"), ("kiliṭṭho", "kilese", f"ညစ်နွမ်းနေသူသည် {KILS}ကို")):
    P(f"{_w} {_k} jahati", VV(_o, JAHATI))
for _w, _k, _o in (("rāgena", "rāgaṃ", "ရာဂဖြင့် ရာဂကို"), ("dosena", "dosaṃ", "ဒေါသဖြင့် ဒေါသကို"),
                   ("mohena", "mohaṃ", "မောဟဖြင့် မောဟကို"), ("kilesehi", "kilese", f"{KILS}ဖြင့် {KILS}ကို")):
    P(f"{_w} {_k} jahati", VV(_o, JAHATI))
CSAMP = new("cittasampayutto", "စိတ်နှင့် ယှဉ်တွဲသော အရာ")
P("rāgo cittasampayutto", V(f"ရာဂသည် {CSAMP}"))
P("maggo cittasampayutto", V(f"မဂ်သည် {CSAMP}"))
P("dvinnaṃ cittānaṃ samodhānaṃ hoti", V(f"စိတ် {F.NUM_MY[2]}{F.CL}တို့၏ ပေါင်းဆုံခြင်း"))
P("rāgo akusalo", V("ရာဂသည် အကုသိုလ်"))
P("maggo kusalo", V("မဂ်သည် ကုသိုလ်"))
W("4", "^4-104", "kusalākusale dhamme", "ကုသိုလ် အကုသိုလ် သဘောတရားတို့")
W("4", "^4-104", "kaṇhasukkasappaṭibhāge dhamme", "မည်းနက်သော ဖြူစင်သော ဆန့်ကျင်ဘက် ရှိသော သဘောတရားတို့")
SAMMUKH = F.SAMMUKHA     # harmonise B6: = ch15 (was «မျက်နှာချင်းဆိုင် ဖြစ်လာကြ»)
P("kusalākusalā sāvajjānavajjā hīnapaṇītā kaṇhasukkasappaṭibhāgā dhammā sammukhībhāvaṃ āgacchanti",
  Cl(f"{F.KSA}သည်", *SAMMUKH))
P("kusalākusalā… sammukhībhāvaṃ āgacchanti", Cl("ကုသိုလ် အကုသိုလ်… သဘောတရားတို့သည်", *SAMMUKH))
Q("cattārimāni, bhikkhave, suvidūravidūrāni! Katamāni cattāri? Nabhañca, bhikkhave, pathavī ca – idaṃ paṭhamaṃ "
  "suvidūravidūraṃ… tasmā sataṃ dhammo asabbhi ārakā",
  f"{F.FAR4_HEAD}… {F.FAR4_LAST}")             # harmonise B6: = ch15
# --- (187) 2. Suññatākathā
SUNN = new("suññatā", "ဆိတ်သုဉ်းခြင်း")
section("(187) 2. Suññatākathā", f"(187) 2. {SUNN}အကြောင်း {KATHA}")
section("Suññatākathā", f"{SUNN}အကြောင်း {KATHA}")
KHN = {"rūpakkhandh": F._KH["rūpakkhandho"], "vedanākkhandh": F._KH["vedanākkhandho"],
       "saññākkhandh": F._KH["saññākkhandho"], "saṅkhārakkhandh": F._KH["saṅkhārakkhandho"],
       "viññāṇakkhandh": F._KH["viññāṇakkhandho"]}
INC = new("X-pariyāpanna (of a khandha)", "၌ အကျုံးဝင်သော အရာ")
SUBJ_S = {"suññatā": SUNN, "animittaṃ": "အမှတ်အသား မရှိခြင်း", "appaṇihito": "တောင့်တမှု မရှိခြင်း"}
for _k, _m in SUBJ_S.items():
    _end = {"suññatā": "ā", "animittaṃ": "aṃ", "appaṇihito": "o"}[_k]
    P(f"{_k} saṅkhārakkhandhapariyāpann{_end}", V(f"{_m}သည် {KHN['saṅkhārakkhandh']}{INC}"))
    _nv = {"suññatā": "vattabbā", "animittaṃ": "vattabbaṃ", "appaṇihito": "vattabbo"}[_k]
    P(f"{_k} na {_nv} – saṅkhārakkhandhapariyāpann{_end}",
      NSAY(f"{_m}ကို", f"«{KHN['saṅkhārakkhandh']}{INC}»ဟု"))
for _a, _am in KHN.items():
    for _b, _bm in KHN.items():
        if _a == _b:
            continue
        P(f"{_a}assa suññatā {_b}apariyāpannā", V(f"{_am}၏ {SUNN}သည် {_bm}{INC}"))
        P(f"{_a}assa suññatā na vattabbā – {_b}apariyāpannā", NSAY(f"{_am}၏ {SUNN}ကို", f"«{_bm}{INC}»ဟု"))
    P(f"{_a}assa", FR(f"{_am}၏"))
P("saṅkhārakkhandhassa suññatā na vattabbā – vedanākkhandhapariyāpannā… saññākkhandhapariyāpannā… "
  "viññāṇakkhandhapariyāpannā",
  NSAY(f"{KHN['saṅkhārakkhandh']}၏ {SUNN}ကို", f"«{KHN['vedanākkhandh']}{INC}… {KHN['saññākkhandh']}{INC}… "
                                                 f"{KHN['viññāṇakkhandh']}{INC}»ဟု"))
_AN = F.PROP["bhavo anicco saṅkhato paṭiccasamuppanno khayadhammo vayadhammo virāgadhammo nirodhadhammo "
             "vipariṇāmadhammo"].f("stmt")
_AN = _AN[len("ဘဝသည် "):-len(" ရှိသော အရာ ဖြစ်သည်")]
ANICCA8 = _AN.split("၊ ")                                           # the eight items (sample / ch2-5 wording)
assert len(ANICCA8) == 8, ANICCA8
ANICCA_POS = "၊ ".join(ANICCA8) + " ရှိသော အရာ"
_NEG8 = [x + (" အရာ" if not x.endswith("သဘော") else "") for x in ANICCA8]
ANICCA_NEG = " မဟုတ်၊ ".join(_NEG8)                                    # «… မဟုတ်၊ … » (final «မဟုတ်» = the verb)
SKH = KHN["saṅkhārakkhandh"]
P("saṅkhārakkhandho na anicco na saṅkhato na paṭiccasamuppanno na khayadhammo na vayadhammo na virāgadhammo na "
  "nirodhadhammo na vipariṇāmadhammo", V(f"{SKH}သည် {ANICCA_NEG}", neg=True))
P("saṅkhārakkhandho anicco saṅkhato paṭiccasamuppanno khayadhammo vayadhammo virāgadhammo nirodhadhammo "
  "vipariṇāmadhammo", V(f"{SKH}သည် {ANICCA_POS}"))
P("saṅkhārakkhandho anicco… vipariṇāmadhammo", V(f"{SKH}သည် {ANICCA8[0]}… {ANICCA8[-1]} ရှိသော အရာ"))
Q("suññamidaṃ, bhikkhave, saṅkhārā attena vā attaniyena vā",
  f"{_R} ဤပြုပြင်ဖန်တီးမှုတို့သည် အတ္တမှ ဖြစ်စေ၊ အတ္တနှင့် ဆိုင်သော အရာမှ ဖြစ်စေ ဆိတ်သုဉ်း၏")
REF_NOTE_X["āneñjasappāye"] = "အာနေဉ္ဇသပ္ပာယ သုတ်၌"
SLIP_X = [('Na vattabbaṃ – suññatā saṅkhārakkhandhapariyāpannā"ti? Āmantā. Nanu vuttaṃ bhagavatā – "suññamidaṃ, '
           'bhikkhave, saṅkhārā attena vā attaniyena vā"ti [ma. ni. 3.69 āneñjasappāye]! Attheva suttantoti? Āmantā. '
           'Tena hi suññatā saṅkhārakkhandhapariyāpannāti.',
           ["Na vattabbaṃ – suññatā saṅkhārakkhandhapariyāpannāti?", "Āmantā.",
            "Nanu vuttaṃ bhagavatā – suññamidaṃ, bhikkhave, saṅkhārā attena vā attaniyena vāti!",
            "Attheva suttantoti?", "Āmantā.", "Tena hi suññatā saṅkhārakkhandhapariyāpannāti."], {2: 1})]   # ^5-834
# --- (188) 3 Sāmaññaphalakathā
ASK = f"{F.ASANKHATA} အရာ"                                          # asaṅkhata (pi-1; ch10 «nibbānaṃ asaṅkhataṃ»)
SKT = f"{F.SANKHATA} အရာ"
section("(188) 3 Sāmaññaphalakathā", f"(188) 3 {SAMANNA}အကြောင်း {KATHA}")
section("Sāmaññaphalakathā", f"{SAMANNA}အကြောင်း {KATHA}")
NIBB_EPI = new("tāṇaṃ leṇaṃ saraṇaṃ parāyaṇaṃ accutaṃ amataṃ",       # harmonise B6: = ch10 (make_ch6-10 ^5-353)
               "၊ ".join(F.PROP[k].pre.rsplit(" ", 1)[0] for k in ("tāṇāni", "leṇāni", "saraṇāni", "parāyaṇāni",
                                                                   "accutāni", "amatāni")))
assert NIBB_EPI == "ကာကွယ်ရာ၊ ပုန်းအောင်းရာ၊ ကိုးကွယ်ရာ၊ မှီခိုရာ၊ မစုတေသော အရာ၊ အမြိုက်"   # (was «ဆုံးခန်းတိုင်ရာ», «မသေသော အရာ»)
_NE = NIBB_EPI.split("၊ ")
P("nibbānaṃ tāṇaṃ leṇaṃ saraṇaṃ parāyaṇaṃ accutaṃ amataṃ", V(f"{F.NIBBANA}သည် {NIBB_EPI}"))
P("nibbānaṃ… amataṃ", V(f"{F.NIBBANA}သည် {_NE[0]}… {_NE[-1]}"))
P("nibbānaṃ… accutaṃ amataṃ", V(f"{F.NIBBANA}သည် {_NE[0]}… {_NE[-2]}၊ {_NE[-1]}"))
NUMS = {"dve": 2, "pañca": 5, "nava": 9, "cha": 6}
for _n, _v in NUMS.items():
    P(f"{_n} asaṅkhatāni", V(f"{ASK} {F.NUM_MY[_v]}{F.CL}", EXIST))
    P(f"{_n} tāṇāni", V(f"{_NE[0]} {F.NUM_MY[_v]}{F.CL}", EXIST))   # harmonise B6: «X tāṇāni…pe… antarikā vā» = the
P("antarikā vā", V("ကြားအပိုင်းဖြစ်စေ", EXIST))                    # series form of ch10 / ch14 («… ရှိသလော… … ရှိသလော»)
SUBJ_A = {"sāmaññaphalaṃ": SAMANNA, "sāmaññaṃ": "ရဟန်းအဖြစ်", "nibbānaṃ": F.NIBBANA}   # harmonise B2: pi-1 «ရဟန်းအဖြစ်»
for _k in ("sotāpatti", "sakadāgāmi", "anāgāmi", "arahatta"):
    SUBJ_A[f"{_k}phalaṃ"] = PH[_k]
    SUBJ_A[f"{_k}maggo"] = MG[_k]
for _k, _m in SUBJ_A.items():
    _e = "o" if _k.endswith("o") else "aṃ"
    P(f"{_k} asaṅkhat{_e}", V(f"{_m}သည် {ASK}"))
    P(f"{_k} saṅkhat{_e}", V(f"{_m}သည် {SKT}"))
    if _k.endswith("phalaṃ"):
        P(_k, FR(_m))
# --- (189) 4. Pattikathā
PATTI = new("patti (attainment)", "ရရှိခြင်း")
section("(189) 4. Pattikathā", f"(189) 4. {PATTI}အကြောင်း {KATHA}")
section("Pattikathā", f"{PATTI}အကြောင်း {KATHA}")
P("patti asaṅkhatā", V(f"{PATTI}သည် {ASK}"))
PGEN = {"cīvarassa": P11.REQ["cīvaraṃ"], "piṇḍapātassa": P11.REQ["piṇḍapātaṃ"], "senāsanassa": P11.REQ["senāsanaṃ"],
        "gilānapaccayabhesajjaparikkhārassa": P11.REQ["gilānapaccayabhesajjaparikkhāraṃ"]}
for _g, _x in ORD_GEN.items():
    PGEN[f"{_g} jhānassa"] = f"{F.ORD_MY[_x]} {JH}"
for _k, _m in ARUPA4.items():
    PGEN[_k[:-1] + "ssa"] = _m
for _k in ("sotāpatti", "sakadāgāmi", "anāgāmi", "arahatta"):
    PGEN[f"{_k}maggassa"] = MG[_k]
    PGEN[f"{_k}phalassa"] = PH[_k]
for _k, _m in PGEN.items():
    P(f"{_k} patti asaṅkhatā", V(f"{_m}ကို {PATTI}သည် {ASK}"))
    P(_k, FR(f"{_m}ကို"))
_PL = ["dutiyassa jhānassa", "tatiyassa jhānassa", "catutthassa jhānassa", "ākāsānañcāyatanassa",
       "viññāṇañcāyatanassa", "ākiñcaññāyatanassa", "nevasaññānāsaññāyatanassa", "sotāpattimaggassa",
       "sotāpattiphalassa", "sakadāgāmimaggassa", "sakadāgāmiphalassa", "anāgāmimaggassa", "anāgāmiphalassa",
       "arahattamaggassa"]
P("paṭhamassa jhānassa patti asaṅkhatā (evaṃ sabbaṃ vitthāretabbaṃ) " + "… ".join(_PL) + "… arahattaphalassa patti asaṅkhatā",
  V(f"{PGEN['paṭhamassa jhānassa']}ကို {PATTI}သည် {ASK} (ဤနည်းဖြင့် အားလုံးကို အကျယ် ချဲ့ရမည်) "
    + "… ".join(PGEN[x] + "ကို" for x in _PL) + f"… {PGEN['arahattaphalassa']}ကို {PATTI}သည် {ASK}"))
P("patti rūpaṃ… vedanā… saññā… saṅkhārā… viññāṇaṃ",
  V(f"{PATTI}သည် {F.RUPA.my}… {F.VEDANA.my}… {F.SANNA.my}… {F.SANKHARA.my}… {F.VINNANA.my}"))
# --- (190) 5. Tathatākathā
TATH = new("tathatā", "ဟုတ်တိုင်းမှန်သော သဘော")
section("(190) 5. Tathatākathā", f"(190) 5. {TATH}အကြောင်း {KATHA}")
section("Tathatākathā", f"{TATH}အကြောင်း {KATHA}")
ALLDH = f"{P6.ALL_DH}တို့၏ {TATH}"                                 # sabbadhammānaṃ tathatā
P("sabbadhammānaṃ tathatā asaṅkhatā", V(f"{ALLDH}သည် {ASK}"))
P("sabbadhammānaṃ tathatā rūpaṃ… vedanā… saññā… saṅkhārā… viññāṇaṃ",
  V(f"{ALLDH}သည် {F.RUPA.my}… {F.VEDANA.my}… {F.SANNA.my}… {F.SANKHARA.my}… {F.VINNANA.my}"))
TA = {"rūpassa rūpatā": ("ရုပ်၏ ရုပ်ဖြစ်ခြင်း", "ရုပ်ဖြစ်ခြင်း"),
      "vedanāya vedanatā": ("ခံစားမှု၏ ခံစားမှုဖြစ်ခြင်း", "ခံစားမှုဖြစ်ခြင်း"),
      "saññāya saññatā": ("မှတ်သိမှု၏ မှတ်သိမှုဖြစ်ခြင်း", "မှတ်သိမှုဖြစ်ခြင်း"),
      "saṅkhārānaṃ saṅkhāratā": ("ပြုပြင်ဖန်တီးမှုတို့၏ ပြုပြင်ဖန်တီးမှုဖြစ်ခြင်း", "ပြုပြင်ဖန်တီးမှုဖြစ်ခြင်း"),
      "viññāṇassa viññāṇatā": ("သိစိတ်၏ သိစိတ်ဖြစ်ခြင်း", "သိစိတ်ဖြစ်ခြင်း")}


class NanuPart(Cl):
    """«X-assa X-tā, nanu X-tā (asaṅkhatā)»: a statement followed by a «nanu» question in every form."""

    def __init__(self, a, b):
        super().__init__(a, "ဖြစ်")
        self.b = b

    def f(self, form, depth=0):
        return F.q_set(f"{self.pre} ရှိ၏၊ {self.b} မဟုတ်လော", depth)


for _k, (_a, _b) in TA.items():
    _n = _k.split()[1]
    P(f"{_k}, nanu {_n} asaṅkhatā", NanuPart(_a, f"{_b}သည် {ASK} ဖြစ်သည်"))
    P(f"{_k}, nanu {_n}", NanuPart(_a, _b))
# --- (191) 6. Kusalakathā
NDH = new("nibbānadhātu", "နိဗ္ဗာန် ဓာတ်")
section("(191) 6. Kusalakathā", f"(191) 6. ကုသိုလ်အကြောင်း {KATHA}")
section("Kusalakathā", f"ကုသိုလ်အကြောင်း {KATHA}")
SAR = (W("1", "^1-M2-55", "sārammaṇā dhammā", "အာရုံ ရှိသော") + " အရာ",
       W("1", "^1-M2-55", "anārammaṇā dhammā", "အာရုံ မရှိသော") + " အရာ")
P("nibbānadhātu kusalā", V(f"{NDH}သည် ကုသိုလ်"))
P("sārammaṇā", V(SAR[0]))
P("anārammaṇā", V(SAR[1]))
for _e, _neg in (("atthi", False), ("natthi", True)):
    P(f"{_e} tāya āvaṭṭanā… paṇidhi", V(f"{F.AVATTANA_IN} {AVP}", EXIST, _neg))   # harmonise B6 (was «ထိုဓာတ်၌»)
    P(f"{_e} tassa āvaṭṭanā… paṇidhi", V(f"ထိုအရာ၌ {AVP}", EXIST, _neg))
ALOB = {"alobho": W("1", "^1-32", "alobho kusalamūlaṃ", "လောဘ မရှိခြင်း"), "adoso": "ဒေါသ မရှိခြင်း",
        "amoho": "မောဟ မရှိခြင်း"}
for _i, (_s, _o) in enumerate((("sārammaṇā", "sārammaṇo"), ("anārammaṇā", "anārammaṇo"))):
    P(f"nibbānadhātu kusalā {_s}", V(f"{NDH}သည် ကုသိုလ် ဖြစ်၍ {SAR[_i]}"))
    P(f"alobho kusalo {_o}", V(f"{ALOB['alobho']}သည် ကုသိုလ် ဖြစ်၍ {SAR[_i]}"))
    P(f"adoso kusalo… amoho kusalo… saddhā… vīriyaṃ… sati… samādhi… paññā kusalā {_s}",
      V(f"{ALOB['adoso']}သည် ကုသိုလ်… {ALOB['amoho']}သည် ကုသိုလ်… {P11.IND['saddhā']}… {P11.IND['vīriyaṃ']}… "
        f"{P11.IND['sati']}… {P11.IND['samādhi']}… {P11.IND['paññā']}သည် ကုသိုလ် ဖြစ်၍ {SAR[_i]}"))
ANAVAJJA = new("anavajja", "အပြစ် မရှိသော အရာ")
P("nibbānadhātu anavajjā", V(f"{NDH}သည် {ANAVAJJA}"))
# --- (192) 7. Accantaniyāmakathā
ACN = new("accantaniyāmatā", "အပြီးအပိုင် ကျိန်းသေခြင်း")
NIYATA = W("1", "^1-M1-15", "micchattaniyatā dhammā", "ကျိန်းသေ")        # niyata (pi-1 «… ၌ ကျိန်းသေသော»)
section("(192) 7. Accantaniyāmakathā", f"(192) 7. {ACN}အကြောင်း {KATHA}")
section("Accantaniyāmakathā", f"{ACN}အကြောင်း {KATHA}")
PUTHU = P11.PUTHU
P("atthi puthujjanassa accantaniyāmatā", V(f"{PUTHU}၌ {ACN}", EXIST))
ACNP = f"အပြီးအပိုင် {NIYATA}သူ"                                         # accantaniyato
HEIN = P6.HEIN
P("mātughātako accantaniyato, pitughātako… arahantaghātako… ruhiruppādako… saṅghabhedako accantaniyato",
  V(f"{HEIN['mātughātako']}သည် {ACNP}၊ {HEIN['pitughātako']}… {HEIN['arahantaghātako']}… "
    f"{HEIN['ruhiruppādako']}… {HEIN['saṅghabhedako']}သည် {ACNP}"))
ACNPG = f"အပြီးအပိုင် {NIYATA}သော {F.PUGGALA}၌"                             # accantaniyatassa puggalassa
SD = W("1", "^1-M2-112", "sassatadiṭṭhi", "အတ္တသည် ထာဝရ တည်မြဲသည်ဟူသော အယူ")
UD = W("1", "^1-M2-112", "ucchedadiṭṭhi", "အတ္တသည် ပြတ်စဲသွားသည်ဟူသော အယူ")
NIYP = {"accantaniyatassa puggalassa": ACNPG,
        "sassatadiṭṭhiyā niyatassa puggalassa": f"{SD}၌ {NIYATA}သော {F.PUGGALA}၌",
        "ucchedadiṭṭhiyā niyatassa puggalassa": f"{UD}၌ {NIYATA}သော {F.PUGGALA}၌"}
ARISE = ("ဖြစ်ပေါ်ရာ", "မဖြစ်ပေါ်ရာ")
for _k, _x, _xm in (("accantaniyatassa puggalassa", "vicikicchā", P11.VICI),
                    ("sassatadiṭṭhiyā niyatassa puggalassa", "ucchedadiṭṭhi", UD),
                    ("ucchedadiṭṭhiyā niyatassa puggalassa", "sassatadiṭṭhi", SD)):
    P(f"{_k} {_x} uppajjeyya", Cl(f"{NIYP[_k]} {_xm}", *ARISE))
    P(f"{_k} {_x} nuppajjeyya", Cl(f"{NIYP[_k]} {_xm}", *ARISE, neg=True))
    P(f"{_k} {_x} akusalena maggena pahīnā", Cl(f"{NIYP[_k][:-1]}၏ {_xm}ကို အကုသိုလ် မဂ်ဖြင့်", *P11.PAHINA))
S("Pahīnāti?", f"{P11.PAHINA[0]}သလော{END}")
S("pahīnāti?", f"{P11.PAHINA[0]}သလော{END}")
S("sakadāgāmimaggena …pe… anāgāmimaggena…pe… arahattamaggenāti?",
  f"{MG['sakadāgāmi']}ဖြင့်… {MG['anāgāmi']}ဖြင့်… {MG['arahatta']}ဖြင့်လော{END}")
S("sakadāgāmimaggena…pe… anāgāmimaggena…pe… arahattamaggenāti?",
  f"{MG['sakadāgāmi']}ဖြင့်… {MG['anāgāmi']}ဖြင့်… {MG['arahatta']}ဖြင့်လော{END}")
S("Akusalena maggenāti.", f"အကုသိုလ် မဂ်ဖြင့် ဖြစ်သည်{END}")
S("Akusalena maggena.", f"အကုသိုလ် မဂ်ဖြင့် ဖြစ်သည်{END}")
# the path epithets (copied from make_ch2-5.py NIYY; checked against 4-jahatikatha.md)
NIYY_P = ["လွတ်မြောက်ရာသို့ ပို့ဆောင်သော", "ကုန်ခန်းခြင်းဆီသို့ ဦးတည်သော", F.BODHAGAMI,
          "စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော", "ကိလေသာ၏ အာရုံ မဖြစ်နိုင်သော"]
NIYY_N = ["လွတ်မြောက်ရာသို့ မပို့ဆောင်သော", "ကိလေသာ၏ အာရုံ ဖြစ်နိုင်သော"]
AKM = "အကုသိုလ် မဂ်"
P("akusalo maggo niyyāniko khayagāmī bodhagāmī anāsavo… asaṃkilesiko",
  V(f"{AKM}သည် {'၊ '.join(NIYY_P[:4])}… {NIYY_P[4]} မဂ်"))
P("akusalo maggo aniyyāniko… saṃkilesiko", V(f"{AKM}သည် {NIYY_N[0]}… {NIYY_N[1]} မဂ်"))
for _k, _x in (("sassatadiṭṭhiyā niyatassa puggalassa", "ucchedadiṭṭhi"),
               ("ucchedadiṭṭhiyā niyatassa puggalassa", "sassatadiṭṭhi")):
    _q = PROP_X[f"{_k} {_x} akusalena maggena pahīnā"].f("stmt", 1)
    S(f"Akusalo maggo…pe… no ca vata re vattabbe – {_k} {_x} akusalena maggena pahīnāti.",
      f"{AKM}သည်… အမှန်ပင် ဤသို့လည်း မဆိုသင့် – “{_q}”{END}")
_SO = "ထိုသူသည်"
Q("idha, bhikkhave, ekacco puggalo samannāgato hoti ekantakāḷakehi akusalehi dhammehi, so sakiṃ nimuggo nimuggova hoti",
  f"{_R} ဤလောက၌ အချို့သော {F.PUGGALA}သည် လုံးဝ မည်းနက်သော အကုသိုလ် သဘောတရားတို့နှင့် ပြည့်စုံ၏၊ {_SO} "
  f"တစ်ကြိမ် နစ်မြုပ်လျှင် နစ်မြုပ်လျက်သာ ဖြစ်၏")
ANCHOR_X["so"] = _SO
VAR_X["evaṃ kho bhikkhave puggalo"] = F.PATHA
UMM = "ပေါ်လာပြီး"
Q("idha, bhikkhave, ekacco puggalo ummujjitvā nimujjati",
  f"{_R} ဤလောက၌ အချို့သော {F.PUGGALA}သည် {UMM} ပြန်နစ်၏")
P("sabbakālaṃ ummujjitvā nimujjati", VV(f"အချိန်ခပ်သိမ်း {UMM}", "ပြန်နစ်"))
Q("idha, bhikkhave, ekacco puggalo ummujjitvā ṭhito hoti, ummujjitvā vipassati viloketi, ummujjitvā patarati, "
  "ummujjitvā patigādhappatto hoti",
  f"{_R} ဤလောက၌ အချို့သော {F.PUGGALA}သည် {UMM} တည်နေ၏၊ {UMM} ကြည့်ရှု၏၊ ဝေ့ဝဲ ကြည့်၏၊ {UMM} ကူးခတ်၏၊ "
  f"{UMM} ခြေကုတ်ရာ မြေသို့ ရောက်၏")
P("sabbakālaṃ ummujjitvā patigādhappatto hoti", V(f"အချိန်ခပ်သိမ်း {UMM} ခြေကုတ်ရာ မြေသို့ ရောက်သူ"))


@F.frame(r"(?P<x>.+?)ti – katvā (?P<k>tena ca kāraṇena|teneva kāraṇena) (?P<p>.+?)ti\?")
def _f_katva_dash(m):
    """«"Q"ti – katvā tena ca kāraṇena P-ti?» (^5-852: a dash before «katvā», kept)."""
    return (f"{F.pq(m['x'], 'stmt')}ဟု – အကြောင်းပြု၍ {F.TENA_CA if m['k'].startswith('tena ca') else F.TENEVA} "
            f"{F.pq(m['p'], 'q')}{END}")


before_generic()
# --- (193) 8. Indriyakathā
section("(193) 8. Indriyakathā", f"(193) 8. {F.INDRIYA_W}အကြောင်း {KATHA}")
section("Indriyakathā", f"{F.INDRIYA_W}အကြောင်း {KATHA}")
IND = P11.IND
LOKIYA, LOKUTTARA = P6.LOKIYA, P6.LOKUTTARA
_G = {"saddhā": "ā", "vīriyaṃ": "aṃ", "sati": "ā", "samādhi": "o", "paññā": "ā", "mano": "o", "somanassaṃ": "aṃ",
      "jīvitaṃ": "aṃ"}
_INDR = {"saddhā": "saddhindriyaṃ", "vīriyaṃ": "vīriyindriyaṃ", "sati": "satindriyaṃ", "samādhi": "samādhindriyaṃ",
         "paññā": "paññindriyaṃ", "mano": "manindriyaṃ", "somanassaṃ": "somanassindriyaṃ", "jīvitaṃ": "jīvitindriyaṃ"}
for _l, _lm in (("lokiy", LOKIYA), ("lokuttar", LOKUTTARA)):
    for _t, _g in _G.items():
        for _e, _neg in (("atthi", False), ("natthi", True)):
            P(f"{_e} {_l}{_g} {_t}", V(f"{_lm} {IND[_t]}", EXIST, _neg))
            P(f"{_e} {_l}aṃ {_INDR[_t]}", V(f"{_lm} {IND[_INDR[_t]]}", EXIST, _neg))
    for _e, _neg in (("atthi", False), ("natthi", True)):
        P(f"{_e} {_l}āni pañcindriyāni", V(f"{_lm} {IND['pañcindriyāni']}", EXIST, _neg))
P("natthi lokiyaṃ vīriyindriyaṃ… satindriyaṃ… samādhindriyaṃ… paññindriyaṃ",
  V(f"{LOKIYA} {IND['vīriyindriyaṃ']}… {IND['satindriyaṃ']}… {IND['samādhindriyaṃ']}… {IND['paññindriyaṃ']}", EXIST,
    True))
P("atthi lokiyaṃ vīriyaṃ… sati… samādhi… paññā",
  V(f"{LOKIYA} {IND['vīriyaṃ']}… {IND['sati']}… {IND['samādhi']}… {IND['paññā']}", EXIST))
Q("addasaṃ kho ahaṃ, bhikkhave, buddhacakkhunā lokaṃ volokento satte apparajakkhe mahārajakkhe, tikkhindriye "
  "mudindriye, svākāre, suviññāpaye, appekacce paralokavajjabhayadassāvino viharante",
  f"{_R} ငါသည် ဘုရား မျက်စိဖြင့် လောကကို ကြည့်ရှုလျက် မျက်စိ၌ မြူ နည်းသော၊ မြူ များသော၊ ထက်မြက်သော "
  f"{F.INDRIYA_W} ရှိသော၊ နုံ့သော {F.INDRIYA_W} ရှိသော၊ အခြင်းအရာ ကောင်းသော၊ သိအောင် ပြရ လွယ်ကူသော၊ အချို့သည် "
  f"တမလွန် လောကနှင့် အပြစ်၌ ဘေးကို မြင်လျက် နေကြသော သတ္တဝါတို့ကို မြင်ခဲ့၏")
BR_X['[ma. ni. 1.283 tattha "dvākāre duviññāpaye" iccādīnipi padāni dissanti]'] = (
    f"[{F.REF['ma. ni.']} 1.283 ထိုနေရာ၌ “dvākāre duviññāpaye” စသော ပုဒ်တို့ကိုလည်း မြင်ရသည်]")
LINES_X[key("Atīte kilese jahati anāgate kilese jahati paccuppanne kilese jahati, suññatā "
            "saṅkhārakkhandhapariyāpannā, sāmaññaphalaṃ asaṅkhataṃ, patti asaṅkhatā, sabbadhammānaṃ tathatā "
            "asaṅkhatā, nibbānadhātu kusalā, atthi puthujjanassa accantaniyāmatā, natthi lokiyāni pañcindriyānīti.")] = (
    f"{P6.ATITA} {KILS}ကို {JAHATI}၊ {P6.ANAGATA} {KILS}ကို {JAHATI}၊ {P6.PACCUP} {KILS}ကို {JAHATI}၊ {SUNN}သည် "
    f"{SKH}{INC}၊ {SAMANNA}သည် {ASK}၊ {PATTI}သည် {ASK}၊ {ALLDH}သည် {ASK}၊ {NDH}သည် ကုသိုလ်၊ "
    f"{PUTHU}၌ {ACN} ရှိ၊ {LOKIYA} {IND['pañcindriyāni']} မရှိ{END}")

# ===================================================================================== 28. Vīsatimavaggo
vagga("Vīsatimavaggo", 20)
# --- (194) 1. Asañciccakathā
ASAN = new("asañcicca / sañcicca", ("မရည်ရွယ်ဘဲ", "ရည်ရွယ်၍"))
section("(194) 1. Asañciccakathā", f"(194) 1. {ASAN[0]} ပြုခြင်းအကြောင်း {KATHA}")
section("Asañciccakathā", f"{ASAN[0]} ပြုခြင်းအကြောင်း {KATHA}")
ANANT = new("ānantariko", "အနန္တရိယကံ ရှိသူ")
for _a, _am in (("asañcicca", ASAN[0]), ("sañcicca", ASAN[1])):
    for _h, _neg in (("hoti", False), ("na hoti", True)):
        P(f"{_a} mātaraṃ jīvitā voropetvā ānantariko {_h}", V(f"{_am} အမိကို သတ်၍ {ANANT}", neg=_neg))
for _h, _neg in (("hoti", False), ("na hoti", True)):
    P(f"asañcicca pāṇaṃ hantvā pāṇātipātī {_h}", V(f"{ASAN[0]} သတ္တဝါကို သတ်၍ {F.PANATIPATA[:-len('ခြင်း')]}သူ", neg=_neg))
    P(f"asañcicca adinnaṃ ādiyitvā… musā bhaṇitvā musāvādī {_h}",
      V(f"{ASAN[0]} မပေးသည်ကို ယူ၍… မုသား ပြော၍ မုသား ပြောသူ", neg=_neg))
_SUT = F.SUTTA_IS              # harmonise B5: «“P”ဟု – ထိုသို့သော …» (was «”ဟူ၍ –»)


@F.frame(r"(?P<p>.+?)ti – attheva suttantoti\?")
def _f_sutt_q(m):
    """«"P"ti – attheva suttantoti?» = «“P”ဟု – ထိုသို့သော သုတ္တန် အမှန်ပင် ရှိသလော။» (the dash kept; harmonise B5)."""
    return f"“{F.pq(m['p'], 'stmt', 1)}”{F.SUTTA_TI} – {_SUT} {EXIST}သလော{END}"


before_generic()


@F.rule(r"(?P<p>.+?)ti – (?P<n>n?)attheva suttanto")
def _r_sutt(m):
    """«"P"ti – (n)attheva suttanto» inside a condition: «“P”ဟု – ထိုသို့သော သုတ္တန် အမှန်ပင် (မ)ရှိ» (depth 0)."""
    try:
        q = F.prop_my(m["p"], "stmt", 1)
    except F.Miss:
        return None
    return Cl(f"“{q}”{F.SUTTA_TI} – {_SUT}", EXIST, NEXIST, bool(m["n"]))


for _k in ("mātughātako", "pitughātako", "arahantaghātako", "ruhiruppādako", "saṅghabhedako"):
    P(f"{_k} ānantariko", V(f"{HEIN[_k]}သည် {ANANT}"))
KILLED = ("သတ်ခဲ့ပြီး", "မသတ်ရသေး")
P("mātā jīvitā voropitā", Cl(f"{F.MATA}ကို", *KILLED))
P("pitā jīvitā voropito", Cl(f"{F.PITA}ကို", *KILLED))
P("arahā jīvitā voropito", Cl(f"{F.ARAHA}ကို", *KILLED))
P("tathāgatassa lohitaṃ uppāditaṃ", Cl(f"{BUDDHA}၏ သွေးကို", "စိမ်းစေခဲ့ပြီး", "မစိမ်းစေရသေး"))
P("sabbe saṅghabhedakā ānantarikā", V(f"{HEIN['saṅghabhedako']} အားလုံးတို့သည် {ANANT}တို့"))
DSS = new("dhammasaññī saṅghabhedako", f"တရားဟု မှတ်ထင်လျက် {HEIN['saṅghabhedako']}")
P("dhammasaññī saṅghabhedako ānantariko", V(f"{DSS}သည် {ANANT}"))
Q("atthupāli, saṅghabhedako āpāyiko nerayiko kappaṭṭho atekiccho; atthupāli, saṅghabhedako na āpāyiko na nerayiko "
  "na kappaṭṭho na atekiccho",
  f"ဥပါလိ၊ အပါယ်သို့ ရောက်မည့်၊ ငရဲ၌ ကျမည့်၊ ကမ္ဘာ ပတ်လုံး တည်ရမည့်၊ ကုစား၍ မရနိုင်သော "
  f"{HEIN['saṅghabhedako']} ရှိ၏၊ ဥပါလိ၊ အပါယ်သို့ မရောက်မည့်၊ ငရဲ၌ မကျမည့်၊ ကမ္ဘာ ပတ်လုံး မတည်ရမည့်၊ "
  f"ကုစား၍ မရနိုင်သူ မဟုတ်သော {HEIN['saṅghabhedako']} ရှိ၏")
LINES_X[key('"Āpāyiko nerayiko, kappaṭṭho saṅghabhedako;')] = F.VERSE_SANGHABHEDA[0]   # harmonise B6: = ch21
LINES_X[key("Vaggarato adhammaṭṭho, yogakkhemā padhaṃsati;")] = F.VERSE_SANGHABHEDA[1]
LINES_X[key('Saṅghaṃ samaggaṃ bhetvāna, kappaṃ nirayamhi paccatī"ti.')] = (
    f"{F.VERSE_SANGHABHEDA[2]} {F.VERSE_SANGHABHEDA[3]} ⟦0⟧{END}")
BR_X["[cūḷava. 354; a. ni. 10.39; itivu. 18]"] = f"[{F.REF['cūḷava.']} 354၊ {F.REF['a. ni.']} 10.39၊ {F.REF['itivu.']} 18]"
# --- (195) 2. Ñāṇakathā
NANA = "ဉာဏ်"
section("(195) 2. Ñāṇakathā", f"(195) 2. {NANA}အကြောင်း {KATHA}")
section("(199) 6. Ñāṇakathā", f"(199) 6. {NANA}အကြောင်း {KATHA}")
section("Ñāṇakathā", f"{NANA}အကြောင်း {KATHA}")
for _e, _neg in (("atthi", False), ("natthi", True)):
    P(f"{_e} puthujjanassa ñāṇaṃ", V(f"{PUTHU}၌ {NANA}", EXIST, _neg))
_PNY = F.FINAL.seg("1", "^1-16")[2][0]
PANNA8 = "ပညာ၊ ကွဲပြားစွာ သိခြင်း၊ စိစစ်ခြင်း၊ သေချာစွာ စိစစ်ခြင်း၊ သဘောတရားများကို စိစစ်ခြင်း၊ လက္ခဏာကို ကောင်းစွာ " \
         "ခွဲခြားခြင်း၊ လက္ခဏာကို အနီးကပ် ခွဲခြားခြင်း၊ လက္ခဏာကို အသီးသီး ခွဲခြားခြင်း"
assert PANNA8 in _PNY
F.WITNESS.setdefault("paññā pajānanā vicayo pavicayo dhammavicayo sallakkhaṇā upalakkhaṇā paccupalakkhaṇā",
                     ("1", "^1-16", PANNA8))
_P8 = PANNA8.split("၊ ")
for _e, _neg in (("atthi", False), ("natthi", True)):
    P(f"{_e} puthujjanassa paññā pajānanā vicayo pavicayo dhammavicayo sallakkhaṇā upalakkhaṇā paccupalakkhaṇā",
      V(f"{PUTHU}၌ {PANNA8}", EXIST, _neg))
    P(f"{_e} puthujjanassa paññā pajānanā vicayo… paccupalakkhaṇā",
      V(f"{PUTHU}၌ {_P8[0]}၊ {_P8[1]}၊ {_P8[2]}… {_P8[-1]}", EXIST, _neg))
ENTER = ("ဝင်စားရာ", "မဝင်စားရာ")
GIVE = ("ပေးရာ", "မပေးရာ")
P("puthujjano paṭhamaṃ jhānaṃ samāpajjeyya", Cl(f"{PUTHU}သည် ပထမ {JH}ကို", *ENTER))
P("puthujjano dutiyaṃ jhānaṃ… tatiyaṃ jhānaṃ… catutthaṃ jhānaṃ… ākāsānañcāyatanaṃ samāpajjeyya, "
  "viññāṇañcāyatanaṃ ākiñcaññāyatanaṃ nevasaññānāsaññāyatanaṃ samāpajjeyya, puthujjano dānaṃ dadeyya… cīvaraṃ "
  "dadeyya, piṇḍapātaṃ dadeyya, senāsanaṃ dadeyya, gilānapaccayabhesajjaparikkhāraṃ dadeyya",
  Cl(f"{PUTHU}သည် ဒုတိယ {JH}ကို… တတိယ {JH}ကို… စတုတ္ထ {JH}ကို… {ARUPA4['ākāsānañcāyatanaṃ']}ကို ဝင်စားရာ၏၊ "
     f"{ARUPA4['viññāṇañcāyatanaṃ']}၊ {ARUPA4['ākiñcaññāyatanaṃ']}၊ {ARUPA4['nevasaññānāsaññāyatanaṃ']}ကို "
     f"ဝင်စားရာ၏၊ {PUTHU}သည် အလှူကို ပေးရာ၏… {P11.REQ['cīvaraṃ']}ကို ပေးရာ၏၊ {P11.REQ['piṇḍapātaṃ']}ကို ပေးရာ၏၊ "
     f"{P11.REQ['senāsanaṃ']}ကို ပေးရာ၏၊ {P11.REQ['gilānapaccayabhesajjaparikkhāraṃ']}ကို", *GIVE))
P("puthujjano gilānapaccayabhesajjaparikkhāraṃ dadeyya",
  Cl(f"{PUTHU}သည် {P11.REQ['gilānapaccayabhesajjaparikkhāraṃ']}ကို", *GIVE))
P("puthujjano tena ñāṇena dukkhaṃ parijānāti", VV(f"{PUTHU}သည် ထို{NANA}ဖြင့် ဒုက္ခကို", "ပိုင်းခြား သိ"))
# --- (196) 3. Nirayapālakathā
NP = new("nirayapālā", "ငရဲထိန်းတို့")
KK = new("kammakāraṇā / kāraṇikā", ("ညှဉ်းပန်း နှိပ်စက်ခြင်းတို့", "ညှဉ်းပန်း နှိပ်စက်သူတို့"))
section("(196) 3. Nirayapālakathā", f"(196) 3. ငရဲထိန်းအကြောင်း {KATHA}")
section("Nirayapālakathā", f"ငရဲထိန်းအကြောင်း {KATHA}")
for _e, _neg in (("atthi", False), ("natthi", True)):
    P(f"{_e} nirayesu nirayapālā", V(f"ငရဲတို့၌ {NP}", EXIST, _neg))
    P(f"{_e} nirayesu kammakāraṇā", V(f"ငရဲတို့၌ {KK[0]}", EXIST, _neg))
    P(f"{_e} manussesu kammakāraṇā", V(f"လူတို့၌ {KK[0]}", EXIST, _neg))
    P(f"{_e} ca kāraṇikā", V(f"{KK[1]}လည်း", EXIST, _neg))
LINES_X[key('"Na vessabhū nopi ca pettirājā,')] = "“ဝေဿဘူ မဟုတ်၊ ပြိတ္တာတို့၏ မင်းလည်း မဟုတ်၊"
LINES_X[key("Somo yamo vessavaṇo ca rājā;")] = "သောမ၊ ယမ၊ ဝေဿဝဏ် မင်းလည်း၊"
LINES_X[key('Sakāni kammāni hananti tattha, ito paṇunnaṃ paralokapatta"nti.')] = (
    "ဤလောကမှ နှင်ထုတ်ခံရ ⟦0⟧၍ တမလွန် လောကသို့ ရောက်သွားသူကို ထိုငရဲ၌ မိမိတို့၏ ကံတို့ကသာ သတ်ကြကုန်၏”" + END)
VAR_X.update({"paṇuṇṇaṃ": F.LEKHANA, "panunnaṃ": F.LEKHANA, "kudhārīhi": F.LEKHANA, "sañjotibhūtāya": F.LEKHANA,
              "dukkhanirodhā": F.LEKHANA, "gaṇḍupādāti": F.LEKHANA, "hatthibhaṇḍā assabhaṇḍā": F.PATHA})
_TAM = f"{_R} ထိုသူကို {NP}သည်"
_HOT = "ပူလောင်သော သံချောင်းကို"
_PAIN = "ထိုသူသည် ထိုငရဲ၌ ဆင်းရဲသော၊ ပြင်းထန်သော၊ ခါးသက်သော ခံစားမှုကို ခံစားရ၏"
_DIE = "ထိုယုတ်မာသော ကံ မကုန်သေးသမျှ ကာလပတ်လုံး မသေနိုင်"
Q("tamenaṃ, bhikkhave, nirayapālā pañcavidhabandhanaṃ nāma kāraṇaṃ kārenti – tattaṃ ayokhīlaṃ hatthe gamenti, tattaṃ "
  "ayokhīlaṃ dutiye hatthe gamenti, tattaṃ ayokhīlaṃ pāde gamenti, tattaṃ ayokhīlaṃ dutiye pāde gamenti, tattaṃ "
  "ayokhīlaṃ majjheurasmiṃ gamenti; so tattha dukkhā tibbā kaṭukā vedanā vedeti; na ca tāva kālaṃ karoti yāva na "
  "taṃ pāpakammaṃ byantīhoti",
  f"{_TAM} အနှောင် ငါးပါး မည်သော ညှဉ်းပန်းမှုကို ပြုကြ၏ ⟦b⟧ – {_HOT} လက်၌ ရိုက်သွင်းကြ၏၊ {_HOT} ဒုတိယ လက်၌ "
  f"ရိုက်သွင်းကြ၏၊ {_HOT} ခြေ၌ ရိုက်သွင်းကြ၏၊ {_HOT} ဒုတိယ ခြေ၌ ရိုက်သွင်းကြ၏၊ {_HOT} ရင်ဘတ် အလယ်၌ "
  f"ရိုက်သွင်းကြ၏၊ {_PAIN}၊ {_DIE}")
BR_X["[karonti (ma. ni. 3.250; a. ni. 3.36)]"] = (
    f"[{F.PATHA} ({F.REF['ma. ni.']} 3.250၊ {F.REF['a. ni.']} 3.36): karonti]")
BR_X["[kudhārīhi (sabbattha)]"] = f"[{F.LEKHANA} (နေရာတိုင်း၌): kudhārīhi]"
_FIRE = "ပူလောင်နေသော၊ တောက်လောင်နေသော၊ မီးလျှံ ထွက်နေသော"
S("Nanu vuttaṃ bhagavatā – tamenaṃ, bhikkhave, nirayapālā saṃvesetvā kuṭhārīhi tacchanti…pe… tamenaṃ, bhikkhave, "
  "nirayapālā uddhampādaṃ adhosiraṃ ṭhapetvā vāsīhi tacchanti…pe… tamenaṃ, bhikkhave, nirayapālā rathe yojetvā "
  "ādittāya pathaviyā sampajjalitāya sajotibhūtāya sārentipi paccāsārentipi…pe… tamenaṃ, bhikkhave, nirayapālā "
  "mahantaṃ aṅgārapabbataṃ ādittaṃ sampajjalitaṃ sajotibhūtaṃ āropentipi oropentipi…pe… tamenaṃ, bhikkhave, "
  "nirayapālā uddhampādaṃ adhosiraṃ gahetvā tattāya lohakumbhiyā pakkhipanti ādittāya sampajjalitāya sajotibhūtāya. "
  "So tattha pheṇuddehakaṃ paccati, so tattha pheṇuddehakaṃ paccamāno sakimpi uddhaṃ gacchati, sakimpi adho gacchati, "
  "sakimpi tiriyaṃ gacchati. So tattha dukkhā tibbā kaṭukā vedanā vedayati, na ca tāva kālaṃ karoti yāva na taṃ "
  "pāpakammaṃ byantīhoti. Tamenaṃ, bhikkhave, nirayapālā mahāniraye pakkhipanti! So kho pana, bhikkhave, mahānirayo –",
  f"{BUDDHA} ဤသို့ ဟောတော်မူသည် မဟုတ်လော – “{_TAM} လှဲချ၍ ပုဆိန်တို့ဖြင့် ⟦0⟧ ခုတ်ကြ၏… {_TAM} ခြေကို အထက်၊ "
  f"ခေါင်းကို အောက် ထား၍ ပဲခွပ်တို့ဖြင့် ခုတ်ကြ၏… {_TAM} ရထား၌ ကပ်၍ {_FIRE} ⟦1⟧ မြေပြင်ပေါ်၌ ရှေ့သို့လည်း "
  f"ဆွဲကြ၏၊ နောက်သို့လည်း ဆွဲကြ၏… {_TAM} {_FIRE} မီးကျီး တောင်ကြီးပေါ်သို့ တက်စေကြ၏၊ ဆင်းစေကြ၏… {_TAM} "
  f"ခြေကို အထက်၊ ခေါင်းကို အောက် ကိုင်၍ {_FIRE} ပူလောင်သော ကြေးအိုး၌ ပစ်ထည့်ကြ၏။ ထိုသူသည် ထိုအိုး၌ အမြှုပ် "
  f"ဆူပွက်လျက် ကျက်၏၊ ထိုသူသည် ထိုအိုး၌ အမြှုပ် ဆူပွက်လျက် ကျက်နေစဉ် တစ်ခါ အထက်သို့ သွား၏၊ တစ်ခါ အောက်သို့ "
  f"သွား၏၊ တစ်ခါ ဘေးသို့ သွား၏။ ထိုသူသည် ထိုအိုး၌ ဆင်းရဲသော၊ ပြင်းထန်သော၊ ခါးသက်သော ခံစားမှုကို ခံစားရ၏၊ "
  f"{_DIE}။ {_TAM} ငရဲကြီး၌ ပစ်ထည့်ကြ၏။ ရဟန်းတို့၊ ထိုငရဲကြီးသည်ကား –")
SLIP_X.append(('Natthi nirayesu nirayapālāti? Āmantā. Nanu vuttaṃ bhagavatā – "tamenaṃ, bhikkhave, nirayapālā saṃvesetvā '
               'kuṭhārīhi [kudhārīhi (sabbattha)] tacchanti…pe… tamenaṃ, bhikkhave, nirayapālā uddhampādaṃ adhosiraṃ '
               'ṭhapetvā vāsīhi tacchanti…pe… tamenaṃ, bhikkhave, nirayapālā rathe yojetvā ādittāya pathaviyā '
               'sampajjalitāya sajotibhūtāya [sañjotibhūtāya (syā.)] sārentipi paccāsārentipi…pe… tamenaṃ, bhikkhave, '
               'nirayapālā mahantaṃ aṅgārapabbataṃ ādittaṃ sampajjalitaṃ sajotibhūtaṃ āropentipi oropentipi…pe… tamenaṃ, '
               'bhikkhave, nirayapālā uddhampādaṃ adhosiraṃ gahetvā tattāya lohakumbhiyā pakkhipanti ādittāya '
               'sampajjalitāya sajotibhūtāya. So tattha pheṇuddehakaṃ paccati, so tattha pheṇuddehakaṃ paccamāno sakimpi '
               'uddhaṃ gacchati, sakimpi adho gacchati, sakimpi tiriyaṃ gacchati. So tattha dukkhā tibbā kaṭukā vedanā '
               'vedayati, na ca tāva kālaṃ karoti yāva na taṃ pāpakammaṃ byantīhoti. Tamenaṃ, bhikkhave, nirayapālā '
               'mahāniraye pakkhipanti! So kho pana, bhikkhave, mahānirayo –',
               ["Natthi nirayesu nirayapālāti?", "Āmantā.",
                "Nanu vuttaṃ bhagavatā – tamenaṃ, bhikkhave, nirayapālā saṃvesetvā kuṭhārīhi tacchanti…pe… tamenaṃ, "
                "bhikkhave, nirayapālā uddhampādaṃ adhosiraṃ ṭhapetvā vāsīhi tacchanti…pe… tamenaṃ, bhikkhave, "
                "nirayapālā rathe yojetvā ādittāya pathaviyā sampajjalitāya sajotibhūtāya sārentipi "
                "paccāsārentipi…pe… tamenaṃ, bhikkhave, nirayapālā mahantaṃ aṅgārapabbataṃ ādittaṃ sampajjalitaṃ "
                "sajotibhūtaṃ āropentipi oropentipi…pe… tamenaṃ, bhikkhave, nirayapālā uddhampādaṃ adhosiraṃ gahetvā "
                "tattāya lohakumbhiyā pakkhipanti ādittāya sampajjalitāya sajotibhūtāya. So tattha pheṇuddehakaṃ "
                "paccati, so tattha pheṇuddehakaṃ paccamāno sakimpi uddhaṃ gacchati, sakimpi adho gacchati, sakimpi "
                "tiriyaṃ gacchati. So tattha dukkhā tibbā kaṭukā vedanā vedayati, na ca tāva kālaṃ karoti yāva na taṃ "
                "pāpakammaṃ byantīhoti. Tamenaṃ, bhikkhave, nirayapālā mahāniraye pakkhipanti! So kho pana, "
                "bhikkhave, mahānirayo –"], {}))
LINES_X[key('"Catukkaṇṇo catudvāro, vibhatto bhāgaso mito;')] = (
    "“ထောင့် လေးထောင့် ရှိ၏၊ တံခါး လေးပေါက် ရှိ၏၊ အပိုင်းအခြားအလိုက် ခွဲခြား တိုင်းတာထား၏၊")
LINES_X[key("Ayopākārapariyanto, ayasā paṭikujjito.")] = "သံ တံတိုင်းဖြင့် ဝန်းရံထား၍ သံဖြင့် အပေါ်မှ အုပ်ထား၏။"
LINES_X[key('"Tassa ayomayā bhūmi, jalitā tejasā yutā;')] = (
    "“ထိုငရဲ၏ သံဖြင့် ပြီးသော မြေပြင်သည် တောက်လောင်၍ မီးနှင့် ယှဉ်၏၊")
LINES_X[key('Samantā yojanasataṃ, pharitvā tiṭṭhati sabbadā"ti.')] = (
    "ပတ်လည် ယူဇနာ တစ်ရာကို ပျံ့နှံ့၍ အမြဲ တည်နေ၏” ⟦0⟧" + END)
REF_X["pe. va."] = "“ပေတဝတ္ထု”"
# --- (197) 4. Tiracchānakathā
TIR = f"{F.TIRACCHANA}တို့"
section("(197) 4. Tiracchānakathā", f"(197) 4. {F.TIRACCHANA}အကြောင်း {KATHA}")
section("Tiracchānakathā", f"{F.TIRACCHANA}အကြောင်း {KATHA}")
for _e, _neg in (("atthi", False), ("natthi", True)):
    P(f"{_e} devesu tiracchānagatā", V(f"{P11.DEVA_PL}၌ {TIR}", EXIST, _neg))
P("atthi tiracchānagatesu devā", V(f"{TIR}၌ {P11.DEVA_PL}", EXIST))
P("devaloko tiracchānayoni", V(f"နတ်ပြည်သည် {F.TIRACCHANA} {P11.TOK['yoni']}"))
P("atthi tattha kīṭā paṭaṅgā makasā makkhikā ahī vicchikā satapadī gaṇḍuppādā",
  V("ထိုနတ်ပြည်၌ ပိုးမွှား၊ ပိုးဖလံ၊ ခြင်၊ ယင်၊ မြွေ၊ ကင်းမြီးကောက်၊ ကင်းခြေများ၊ တီကောင်တို့", EXIST))
ANCHOR_X["gaṇḍuppādāti"] = "တီကောင်တို့"
P("atthi tattha erāvaṇo nāma hatthināgo sahassayuttaṃ dibbaṃ yānaṃ",
  V("ထိုနတ်ပြည်၌ ဧရာဝဏ မည်သော ဆင်ပြောင်နှင့် တစ်ထောင်ဖြင့် ကပ်ထားသော နတ် ယာဉ်", EXIST))
P("atthi tattha hatthibandhā assabandhā yāvasikā kāraṇikā bhattakārakā",
  V("ထိုနတ်ပြည်၌ ဆင်ထိန်း၊ မြင်းထိန်း၊ မြက်ကျွေးသူ၊ လေ့ကျင့်ပေးသူ၊ အစာ ချက်ပြုတ်သူတို့", EXIST))
ANCHOR_X["assabandhā"] = "မြင်းထိန်း"
# --- (198) 5. Maggakathā
MGA = {"pañcaṅgiko maggo": f"အင်္ဂါ {F.NUM_MY[5]}{F.CL} ရှိသော မဂ်", "aṭṭhaṅgiko maggo": f"အင်္ဂါ {F.NUM_MY[8]}{F.CL} ရှိသော မဂ်"}
section("(198) 5. Maggakathā", f"(198) 5. မဂ်အကြောင်း {KATHA}")
section("Maggakathā", f"မဂ်အကြောင်း {KATHA}")
MGB = {"pañcaṅgiko maggo": f"မဂ်သည် အင်္ဂါ {F.NUM_MY[5]}{F.CL}", "aṭṭhaṅgiko maggo": f"မဂ်သည် အင်္ဂါ {F.NUM_MY[8]}{F.CL}"}
for _k, _m in MGB.items():
    P(_k, V(_m, EXIST))
_PF = F.FINAL.seg("1", "^1-277")[2][0]
FAC = {"sammādiṭṭhi": "မှန်ကန်သော အယူ", "sammāsaṅkappo": "မှန်ကန်သော ကြံစည်မှု", "sammāvācā": "မှန်ကန်သော စကား",
       "sammākammanto": "မှန်ကန်သော အလုပ်", "sammāājīvo": "မှန်ကန်သော အသက်မွေးမှု", "sammāvāyāmo": "မှန်ကန်သော အားထုတ်မှု",
       "sammāsati": "မှန်ကန်သော သတိ", "sammāsamādhi": "မှန်ကန်သော သမာဓိ"}
for _k, _m in FAC.items():
    assert _m + " ရှိသည်" in _PF, _m
    F.WITNESS.setdefault(_k, ("1", "^1-277", _m))
_SEY = "ယင်းမှာ"
P("aṭṭhaṅgiko maggo vutto bhagavatā, seyyathidaṃ – sammādiṭṭhi… sammāsamādhi",
  Cl(f"{MGA['aṭṭhaṅgiko maggo']}ကို {BUDDHA}", *SAID, post=f"၊ {_SEY} – {FAC['sammādiṭṭhi']}… {FAC['sammāsamādhi']}"))
LINES_X[key('"Maggānaṃ aṭṭhaṅgiko seṭṭho, saccānaṃ caturo padā;')] = (
    f"“မဂ်တို့တွင် {MGA['aṭṭhaṅgiko maggo']}သည် အမြတ်ဆုံး ဖြစ်၏၊ သစ္စာတို့တွင် ပုဒ် လေးပါးသည် အမြတ်ဆုံး ဖြစ်၏၊")
LINES_X[key('Virāgo seṭṭho dhammānaṃ, dvipadānañca cakkhumā"ti.')] = (
    "သဘောတရားတို့တွင် ရာဂ ကင်းခြင်းသည် အမြတ်ဆုံး ဖြစ်၏၊ ခြေ နှစ်ချောင်း ရှိသူတို့တွင် မျက်စိ ရှိတော်မူသူသည် "
    "အမြတ်ဆုံး ဖြစ်၏” ⟦0⟧" + END)
MAGGANGA_W = "မဂ်၏ အင်္ဂါ"
for _k, _m in FAC.items():
    _pr = "sā" if _k in ("sammādiṭṭhi", "sammāvācā", "sammāsati", "sammāsamādhi") else "so"
    for _pp in ("sā", "so"):
        for _n, _neg in (("", False), ("na ", True)):
            P(f"{_k} maggaṅgaṃ, {_pp} ca {_n}maggo",
              V(f"{_m}သည် {MAGGANGA_W} ဖြစ်၍ ထိုအရာသည်လည်း မဂ်", neg=_neg))
    P(_k, FR(_m))
AAM = f"{MGA['aṭṭhaṅgiko maggo']}"
P("ariyo aṭṭhaṅgiko maggo", V(f"အရိယာ {MGB['aṭṭhaṅgiko maggo']}", EXIST))
Q("pubbeva kho panassa kāyakammaṃ vacīkammaṃ ājīvo suparisuddho hoti; evamassāyaṃ ariyo aṭṭhaṅgiko maggo "
  "bhāvanāpāripūriṃ gacchati",
  f"ထိုသူ၏ {F.KAYAKAMMA}၊ {F.VACIKAMMA}၊ အသက်မွေးမှုသည် ရှေးဦးစွာပင် ကောင်းစွာ စင်ကြယ်၏၊ ဤသို့ ထိုသူ၏ ဤ{AAM}၊ "
  f"အရိယာ မဂ်သည် ပွားများခြင်း၏ ပြည့်စုံခြင်းသို့ ရောက်၏")
_SB = "သုဘဒ္ဒ၊"
_DV = "တရားနှင့် ဝိနည်း၌"
_AM = f"{AAM}၊ အရိယာ မဂ်ကို"
_FD = F.FOUND
Q("yasmiṃ kho, subhadda, dhammavinaye ariyo aṭṭhaṅgiko maggo na upalabbhati, samaṇopi tattha na upalabbhati, dutiyopi "
  "tattha samaṇo na upalabbhati, tatiyopi tattha samaṇo na upalabbhati, catutthopi tattha samaṇo na upalabbhati. "
  "Yasmiñca kho, subhadda, dhammavinaye ariyo aṭṭhaṅgiko maggo upalabbhati, samaṇopi tattha upalabbhati, dutiyopi… "
  "tatiyopi… catutthopi tattha samaṇo upalabbhati. Imasmiṃ kho, subhadda, dhammavinaye ariyo aṭṭhaṅgiko maggo "
  "upalabbhati. Idheva, subhadda, samaṇo, idha dutiyo samaṇo, idha tatiyo samaṇo, idha catuttho samaṇo. Suññā "
  "parappavādā samaṇebhi aññehi",
  f"{_SB} အကြင် {_DV} {_AM} မ{_FD}၊ ထို{_DV} ရဟန်းကိုလည်း မ{_FD}၊ ထို{_DV} ဒုတိယ ရဟန်းကိုလည်း မ{_FD}၊ "
  f"ထို{_DV} တတိယ ရဟန်းကိုလည်း မ{_FD}၊ ထို{_DV} စတုတ္ထ ရဟန်းကိုလည်း မ{_FD}။ {_SB} အကြင် {_DV} {_AM} {_FD}၏၊ "
  f"ထို{_DV} ရဟန်းကိုလည်း {_FD}၏၊ ဒုတိယ ရဟန်းကိုလည်း… တတိယ ရဟန်းကိုလည်း… စတုတ္ထ ရဟန်းကိုလည်း ထို{_DV} {_FD}၏။ "
  f"{_SB} ဤ{_DV} {_AM} {_FD}၏။ {_SB} ဤ{_DV}သာ ရဟန်း ရှိ၏၊ ဤ၌ ဒုတိယ ရဟန်း ရှိ၏၊ ဤ၌ တတိယ ရဟန်း ရှိ၏၊ ဤ၌ "
  f"စတုတ္ထ ရဟန်း ရှိ၏။ အခြား ဝါဒတို့သည် ရဟန်းတို့မှ ဆိတ်သုဉ်း၏")
# --- (199) 6. Ñāṇakathā
DVV = new("dvādasavatthukaṃ ñāṇaṃ", f"အခြေ {F.NUM_MY[12]}{F.CL} ရှိသော {NANA}")
P("dvādasavatthukaṃ ñāṇaṃ lokuttaraṃ", V(f"{DVV}သည် {LOKUTTARA} အရာ"))
P("dvādasa lokuttarañāṇāni", V(f"{LOKUTTARA} {NANA} {F.NUM_MY[12]}{F.CL}", EXIST))
for _k in ("sotāpatti", "sakadāgāmi", "anāgāmi", "arahatta"):
    P(f"dvādasa {_k}maggā", V(f"{MG[_k]} {F.NUM_MY[12]}{F.CL}", EXIST))
    P(f"dvādasa {_k}phalāni", V(f"{PH[_k]} {F.NUM_MY[12]}{F.CL}", EXIST))
P("dvādasa sakadāgāmimaggā… anāgāmimaggā… arahattamaggā",
  V(f"{MG['sakadāgāmi']} {F.NUM_MY[12]}{F.CL}… {MG['anāgāmi']}… {MG['arahatta']}", EXIST))
_TR, _AS, _EYE5, _ANAN = P11._TR, P11._AS, P11._EYE5, P11._ANAN
S("Nanu vuttaṃ bhagavatā – idaṃ dukkhaṃ ariyasaccanti me, bhikkhave, pubbe ananussutesu dhammesu cakkhuṃ udapādi, ñāṇaṃ "
  "udapādi, paññā udapādi, vijjā udapādi, āloko udapādi. Taṃ kho panidaṃ dukkhaṃ ariyasaccaṃ pariññeyyanti me, "
  "bhikkhave…pe… pariññātanti me, bhikkhave…pe… idaṃ dukkhasamudayaṃ ariyasaccanti me, bhikkhave…pe… taṃ kho "
  "panidaṃ dukkhasamudayaṃ ariyasaccaṃ pahātabbanti me, bhikkhave…pe… pahīnanti me, bhikkhave…pe… idaṃ dukkhanirodhaṃ "
  "ariyasaccanti me, bhikkhave…pe… taṃ kho panidaṃ dukkhanirodhaṃ ariyasaccaṃ sacchikātabbanti me, bhikkhave…pe… "
  "sacchikatanti me, bhikkhave…pe… idaṃ dukkhanirodhagāminī paṭipadā ariyasaccanti me, bhikkhave…pe… taṃ kho panidaṃ "
  "dukkhanirodhagāminī paṭipadā ariyasaccaṃ bhāvetabbanti me, bhikkhave…pe… bhāvitanti me, bhikkhave, pubbe "
  "ananussutesu dhammesu cakkhuṃ udapādi…pe… āloko udapādīti!",
  f"{BUDDHA} ဤသို့ ဟောတော်မူသည် မဟုတ်လော – “{_R} ‘ဤသည်ကား {_TR['dukkhaṃ']} {_AS}’ဟု {_ANAN} ငါ့အား {_EYE5}။ "
  f"{_R} ‘ထို{_TR['dukkhaṃ']} {_AS}ကို ပိုင်းခြား သိရမည်’ဟု ငါ့အား… {_R} ပိုင်းခြား သိပြီးပြီဟု ငါ့အား… {_R} "
  f"‘ဤသည်ကား {_TR['dukkhasamudayaṃ']} ⟦0⟧ {_AS}’ဟု ငါ့အား… {_R} ‘ထို{_TR['dukkhasamudayaṃ']} {_AS}ကို ပယ်ရမည်’ဟု "
  f"ငါ့အား… {_R} ပယ်ပြီးပြီဟု ငါ့အား… {_R} ‘ဤသည်ကား {_TR['dukkhanirodhaṃ']} ⟦1⟧ {_AS}’ဟု ငါ့အား… {_R} "
  f"‘ထို{_TR['dukkhanirodhaṃ']} {_AS}ကို မျက်မှောက်ပြုရမည်’ဟု ငါ့အား… {_R} မျက်မှောက်ပြုပြီးပြီဟု ငါ့အား… {_R} "
  f"‘ဤသည်ကား {_TR['dukkhanirodhagāminī paṭipadā']} {_AS}’ဟု ငါ့အား… {_R} ‘ထို{_TR['dukkhanirodhagāminī paṭipadā']} "
  f"{_AS}ကို ပွားများရမည်’ဟု ငါ့အား… {_R} ပွားများပြီးပြီဟု {_ANAN} ငါ့အား မျက်စိ ဖြစ်ပေါ်၏… အလင်း ဖြစ်ပေါ်၏” "
  f"⟦2⟧{END}")   # harmonise B5: the closing «ti» of a quotation = «”» (sample)
SLIP_X.append(('Na vattabbaṃ – "dvādasavatthukaṃ ñāṇaṃ lokuttara"nti? Āmantā. Nanu vuttaṃ bhagavatā – "idaṃ dukkhaṃ '
               'ariyasacca"nti me, bhikkhave, pubbe ananussutesu dhammesu cakkhuṃ udapādi, ñāṇaṃ udapādi, paññā udapādi, '
               'vijjā udapādi, āloko udapādi. ‘Taṃ kho panidaṃ dukkhaṃ ariyasaccaṃ pariññeyya’nti me, bhikkhave…pe… '
               'pariññātanti me, bhikkhave…pe… ‘idaṃ dukkhasamudayaṃ [dukkhasamudayo (syā. kaṃ. pī.)] ariyasacca’nti me, '
               'bhikkhave…pe… ‘taṃ kho panidaṃ dukkhasamudayaṃ ariyasaccaṃ pahātabba’nti me, bhikkhave…pe… pahīnanti me, '
               'bhikkhave…pe… ‘idaṃ dukkhanirodhaṃ [dukkhanirodhā (syā. kaṃ. pī.)] ariyasacca’nti me, bhikkhave…pe… ‘taṃ '
               'kho panidaṃ dukkhanirodhaṃ ariyasaccaṃ sacchikātabba’nti me, bhikkhave…pe… sacchikatanti me, '
               'bhikkhave…pe… ‘idaṃ dukkhanirodhagāminī paṭipadā ariyasacca’nti me, bhikkhave…pe… ‘taṃ kho panidaṃ '
               'dukkhanirodhagāminī paṭipadā ariyasaccaṃ bhāvetabba’nti me, bhikkhave…pe… bhāvitanti me, bhikkhave, pubbe '
               'ananussutesu dhammesu cakkhuṃ udapādi…pe… āloko udapādī"ti [mahāva. 15; saṃ. ni. 5.1081; paṭi. ma. '
               '2.30]! Attheva suttantoti? Āmantā. Tena hi dvādasavatthukaṃ ñāṇaṃ lokuttaranti.',
               ["Na vattabbaṃ – dvādasavatthukaṃ ñāṇaṃ lokuttaranti?", "Āmantā.",
                "Nanu vuttaṃ bhagavatā – idaṃ dukkhaṃ ariyasaccanti me, bhikkhave, pubbe ananussutesu dhammesu cakkhuṃ "
                "udapādi, ñāṇaṃ udapādi, paññā udapādi, vijjā udapādi, āloko udapādi. Taṃ kho panidaṃ dukkhaṃ ariyasaccaṃ "
                "pariññeyyanti me, bhikkhave…pe… pariññātanti me, bhikkhave…pe… idaṃ dukkhasamudayaṃ ariyasaccanti me, "
                "bhikkhave…pe… taṃ kho panidaṃ dukkhasamudayaṃ ariyasaccaṃ pahātabbanti me, bhikkhave…pe… pahīnanti me, "
                "bhikkhave…pe… idaṃ dukkhanirodhaṃ ariyasaccanti me, bhikkhave…pe… taṃ kho panidaṃ dukkhanirodhaṃ "
                "ariyasaccaṃ sacchikātabbanti me, bhikkhave…pe… sacchikatanti me, bhikkhave…pe… idaṃ "
                "dukkhanirodhagāminī paṭipadā ariyasaccanti me, bhikkhave…pe… taṃ kho panidaṃ dukkhanirodhagāminī "
                "paṭipadā ariyasaccaṃ bhāvetabbanti me, bhikkhave…pe… bhāvitanti me, bhikkhave, pubbe ananussutesu "
                "dhammesu cakkhuṃ udapādi…pe… āloko udapādīti!",
                "Attheva suttantoti?", "Āmantā.", "Tena hi dvādasavatthukaṃ ñāṇaṃ lokuttaranti."], {}))
LINES_X[key("Mātughātako ānantariko pitughātako ānantariko arahantaghātako ānantariko ruhiruppādako ānantariko "
            "saṅghabhedako ānantariko, natthi puthujjanassa ñāṇaṃ, natthi nirayesu nirayapālā, atthi devesu "
            "tiracchānagatā, pañcaṅgiko maggo, dvādasavatthukaṃ ñāṇaṃ lokuttaranti.")] = (  # noqa
    " ".join(f"{HEIN[k]}သည် {ANANT}" for k in ("mātughātako", "pitughātako", "arahantaghātako", "ruhiruppādako",
                                               "saṅghabhedako"))
    + f"၊ {PUTHU}၌ {NANA} မရှိ၊ ငရဲတို့၌ {NP} မရှိ၊ {P11.DEVA_PL}၌ {TIR} ရှိ၊ {MGB['pañcaṅgiko maggo']} ရှိ၊ "
      f"{DVV}သည် {LOKUTTARA} အရာ{END}")
PANNASA = new("paṇṇāsako (a group of fifty)", "ငါးဆယ်အစု")
LINES_X["Catuttho paṇṇāsako."] = f"{F.ORD_MY[4]} {PANNASA}{END}"
LINES_X[key("Niggaho, puññasañcayo, aṭṭhāsi, atītena ca mātughātako.")] = (
    f"{F.KATHA_NAME['niggaha']}၊ {F.KATHA_NAME['puññūpacaya']}၊ {STAY_B}၊ {P6.ATITA}နှင့် {HEIN['mātughātako']}{END}")
# harmonise B2: niggaho / puññasañcayo name the first kathās of vaggas 16 / 17 = their headings (ch24 / ch25)

# ===================================================================================== 29. Ekavīsatimavaggo
vagga("Ekavīsatimavaggo", 21)


class Fixed(Cl):
    """A clause with one Burmese wording in every form (a wish «… ပါစေ», a verbless item)."""

    def __init__(self, text):
        super().__init__(text)

    def f(self, form, depth=0):
        return F.q_set(self.pre, depth)


# --- (200) 1. Sāsanakathā
SASANA = "သာသနာ"
NEW_ = "အသစ်"
section("(200) 1. Sāsanakathā", f"(200) 1. {SASANA}အကြောင်း {KATHA}")
section("Sāsanakathā", f"{SASANA}အကြောင်း {KATHA}")
MADE = ("ပြုထား", "မပြုထား")
GRP = P11.GRP11
_G6 = ("sammappadhānā", "iddhipādā", "indriyā", "balā", "bojjhaṅgā")
P("sāsanaṃ navaṃ kataṃ", Cl(f"{SASANA}ကို {NEW_}", *MADE))
P("satipaṭṭhānā navaṃ katā", Cl(f"{GRP['satipaṭṭhānā']}တို့ကို {NEW_}", *MADE))
P("sammappadhānā… iddhipādā… indriyā… balā… bojjhaṅgā navaṃ katā",
  Cl("… ".join(GRP[x] for x in _G6) + f"တို့ကို {NEW_}", *MADE))
P("pubbe akusalaṃ pacchā kusalaṃ kataṃ", Cl("ရှေးက အကုသိုလ် ဖြစ်သည်ကို နောက်မှ ကုသိုလ်", *MADE))
_MS = P11.MAT
_SAS = (f"ရှေးက {_MS['sāsava']}… {'၊ '.join(_MS[x] for x in ('saṃyojaniya', 'ganthaniya', 'oghaniya', 'yoganiya', 'nīvaraṇiya', 'parāmaṭṭha', 'upādāniya'))}… "
        f"{_MS['saṃkilesiya']} အရာကို နောက်မှ ကိလေသာ၏ အာရုံ မဖြစ်နိုင်သော အရာ")
P("pubbe sāsavaṃ… saṃyojaniyaṃ ganthaniyaṃ oghaniyaṃ yoganiyaṃ nīvaraṇiyaṃ parāmaṭṭhaṃ upādāniyaṃ… saṃkilesikaṃ "
  "pacchā asaṃkilesikaṃ kataṃ", Cl(_SAS, *MADE))
_SAS2 = f"ရှေးက {_MS['sāsava']}… {_MS['saṃkilesiya']} အရာကို နောက်မှ ကိလေသာ၏ အာရုံ မဖြစ်နိုင်သော အရာ"
KOCI = "တစ်စုံတစ်ယောက်"
_DO = "ပြုလုပ်သော " + KOCI
P("atthi koci tathāgatassa sāsanaṃ navaṃ karoti", V(f"{BUDDHA}၏ {SASANA}ကို {NEW_} {_DO}", EXIST))
P("atthi koci satipaṭṭhāne navaṃ karoti", V(f"{GRP['satipaṭṭhānā']}တို့ကို {NEW_} {_DO}", EXIST))
P("atthi koci sammappadhāne… iddhipāde… indriye… bale… bojjhaṅge navaṃ karoti",
  V("… ".join(GRP[x] for x in _G6) + f"တို့ကို {NEW_} {_DO}", EXIST))
P("atthi koci pubbe akusalaṃ pacchā kusalaṃ karoti", V(f"ရှေးက အကုသိုလ် ဖြစ်သည်ကို နောက်မှ ကုသိုလ် {_DO}", EXIST))
P("atthi koci pubbe sāsavaṃ… saṃkilesikaṃ pacchā asaṃkilesiyaṃ karoti", V(f"{_SAS2} {_DO}", EXIST))
CAN = ("ပြုလုပ်နိုင်", "မပြုလုပ်နိုင်")
P("labbhā tathāgatassa sāsanaṃ puna navaṃ kātuṃ", Cl(f"{BUDDHA}၏ {SASANA}ကို တစ်ဖန် {NEW_}", *CAN))
P("labbhā satipaṭṭhānā puna navaṃ kātuṃ", Cl(f"{GRP['satipaṭṭhānā']}တို့ကို တစ်ဖန် {NEW_}", *CAN))
P("labbhā sammappadhānā… iddhipādā… indriyā… balā… bojjhaṅgā puna navaṃ kātuṃ",
  Cl("… ".join(GRP[x] for x in _G6) + f"တို့ကို တစ်ဖန် {NEW_}", *CAN))
P("labbhā pubbe akusalaṃ pacchā kusalaṃ kātuṃ", Cl("ရှေးက အကုသိုလ် ဖြစ်သည်ကို နောက်မှ ကုသိုလ်", *CAN))
P("labbhā pubbe sāsavaṃ… saṃkilesiyaṃ pacchā asaṃkilesiyaṃ kātuṃ", Cl(_SAS2, *CAN))
# --- (201) 2. Avivittakathā
TEDH = new("tedhātuka", "ဘုံ သုံးပါးနှင့် ဆိုင်သော")
AVIV = new("avivitto (not detached from)", "မကင်းသူ")
section("(201) 2. Avivittakathā", f"(201) 2. မကင်းခြင်းအကြောင်း {KATHA}")
section("Avivittakathā", f"မကင်းခြင်းအကြောင်း {KATHA}")
P("puthujjano tedhātukehi dhammehi avivitto", V(f"{PUTHU}သည် {TEDH} သဘောတရားတို့မှ {AVIV}"))
P("puthujjano tedhātukehi kammehi avivitto", V(f"{PUTHU}သည် {TEDH} ကံတို့မှ {AVIV}"))
_MN = P11.MENT
P("puthujjano tedhātukehi phassehi… tedhātukāhi vedanāhi… saññāhi… cetanāhi… cittehi… saddhāhi… vīriyehi… satīhi… "
  "samādhīhi… tedhātukāhi paññāhi avivitto",
  V(f"{PUTHU}သည် {TEDH} {_MN['phassehi']}တို့မှ… {TEDH} {_MN['vedanāhi']}တို့မှ… {_MN['saññāhi']}တို့မှ… "
    f"{_MN['cetanāhi']}တို့မှ… {_MN['cittehi']}တို့မှ… {_MN['saddhāhi']}တို့မှ… ဝီရိယတို့မှ… သတိတို့မှ… "
    f"သမာဓိတို့မှ… {TEDH} ပညာတို့မှ {AVIV}"))
DWELL = ("နေ", "မနေ")
_UV = "ကို ဝင်စား၍"
P("yasmiṃ khaṇe puthujjano cīvaraṃ deti, tasmiṃ khaṇe paṭhamaṃ jhānaṃ upasampajja viharati… ākāsānañcāyatanaṃ "
  "upasampajja viharati",
  Cl(f"အကြင် ခဏ၌ {PUTHU}သည် {P11.REQ['cīvaraṃ']}ကို ပေး၏၊ ထိုခဏ၌ ပထမ {JH}{_UV} နေ၏… "
     f"{ARUPA4['ākāsānañcāyatanaṃ']}{_UV}", *DWELL))
P("yasmiṃ khaṇe puthujjano piṇḍapātaṃ deti… senāsanaṃ deti… gilānapaccayabhesajjaparikkhāraṃ deti, tasmiṃ khaṇe "
  "catutthaṃ jhānaṃ upasampajja viharati… nevasaññānāsaññāyatanaṃ upasampajja viharati",
  Cl(f"အကြင် ခဏ၌ {PUTHU}သည် {P11.REQ['piṇḍapātaṃ']}ကို ပေး၏… {P11.REQ['senāsanaṃ']}ကို ပေး၏… "
     f"{P11.REQ['gilānapaccayabhesajjaparikkhāraṃ']}ကို ပေး၏၊ ထိုခဏ၌ စတုတ္ထ {JH}{_UV} နေ၏… "
     f"{ARUPA4['nevasaññānāsaññāyatanaṃ']}{_UV}", *DWELL))
RAD = new("rūpadhātuarūpadhātūpagaṃ kammaṃ", "သိမ်မွေ့သော ရုပ်ဘုံနှင့် ရုပ်မရှိသော ဘုံသို့ ရောက်စေသော ကံ")
P("puthujjanassa rūpadhātuarūpadhātūpagaṃ kammaṃ pariññātaṃ",
  Cl(f"{PUTHU}သည် {RAD}ကို", "ပိုင်းခြား သိပြီး", "ပိုင်းခြား မသိရသေး"))
S("Tena hi puthujjano tedhātukehi kammehi avivittoti…pe….",
  f"{F.TENA_HI} {PUTHU}သည် {TEDH} ကံတို့မှ {AVIV} ဖြစ်သည်…")
# --- (202) 3. Saṃyojanakathā
SAMY = "နှောင်ကြိုး"
section("(202) 3. Saṃyojanakathā", f"(202) 3. {SAMY}အကြောင်း {KATHA}")
section("Saṃyojanakathā", f"{SAMY}အကြောင်း {KATHA}")
APP = "ကို မပယ်ဘဲ"                                                    # appahāya (ch12 «… ကို မပယ်ဘဲ»)
ARP = new("arahattappatti", f"{P11.ARAHATTA_N}သို့ ရောက်ခြင်း")
PNB = new("parinibbānaṃ", "ပရိနိဗ္ဗာန် ပြုခြင်း")
for _g, _gm in (("arahattappatti", ARP), ("parinibbānaṃ", PNB)):
    P(f"atthi kiñci saṃyojanaṃ appahāya {_g}", V(f"{SAMY} တစ်စုံတစ်ရာ{APP} {_gm}", EXIST))
P("atthi kiñci sakkāyadiṭṭhiṃ appahāya… vicikicchaṃ appahāya… sīlabbataparāmāsaṃ appahāya… rāgaṃ appahāya… dosaṃ "
  "appahāya… mohaṃ appahāya… anottappaṃ appahāya arahattappatti",
  V(f"{P11.SAKKAYA} တစ်စုံတစ်ရာ{APP}… {P11.VICI}{APP}… {P11.SILAB}{APP}… ရာဂ{APP}… ဒေါသ{APP}… မောဟ{APP}… "
    f"ဒုစရိုက်ကို မကြောက်ရွံ့မှု{APP} {ARP}", EXIST))
P("atthi kiñci sakkāyadiṭṭhiṃ appahāya… anottappaṃ appahāya parinibbānaṃ",
  V(f"{P11.SAKKAYA} တစ်စုံတစ်ရာ{APP}… ဒုစရိုက်ကို မကြောက်ရွံ့မှု{APP} {PNB}", EXIST))
SA8 = ["ရာဂ", "ဒေါသ", "မောဟ", "မာန", W("2", "^2-833", "makkho", "ကျေးဇူး ချေဖျက်မှု"),
       W("2", "^2-833", "paḷāso", "တုပြိုင်မှု"), W("1", "^1-1343", "upāyāsā", "ပြင်းစွာ ပူပန်ခြင်း"), KIL]
P("arahā sarāgo sadoso samoho samāno samakkho sapaḷāso saupāyāso sakileso",
  V(f"{F.ARAHA}သည် " + "၊ ".join(f"{x} ရှိသူ" for x in SA8)))
P("arahā nirāgo niddoso nimmoho nimmāno nimmakkho nippaḷāso nirupāyāso nikkileso",
  V(f"{F.ARAHA}သည် " + "၊ ".join(f"{x} ကင်းသူ" for x in SA8)))
P("arahā nirāgo… nikkileso", V(f"{F.ARAHA}သည် {SA8[0]} ကင်းသူ… {SA8[-1]} ကင်းသူ"))
P("arahā sarāgo… sakileso", V(f"{F.ARAHA}သည် {SA8[0]} ရှိသူ… {SA8[-1]} ရှိသူ"))
P("arahā sabbaṃ buddhavisayaṃ jānāti", VV(f"{F.ARAHA}သည် ဘုရား၏ နယ်ပယ် အားလုံးကို", "သိ"))
# --- (203) 4. Iddhikathā
API = new("adhippāyaiddhi", f"အလိုအတိုင်း ဖြစ်စေနိုင်သော {F.IDDHI}")
section("(203) 4. Iddhikathā", f"(203) 4. {F.IDDHI}အကြောင်း {KATHA}")
section("Iddhikathā", f"{F.IDDHI}အကြောင်း {KATHA}")
_BS = f"ဘုရားတို့၏ဖြစ်စေ {SAV}တို့၏ဖြစ်စေ"
P("atthi adhippāyaiddhi buddhānaṃ vā sāvakānaṃ vā", V(f"{_BS} {API}", EXIST))
for _k, _m in (("niccapaṇṇā rukkhā hontu", "သစ်ပင်တို့သည် အမြဲ ရွက်စိမ်းကြပါစေ"),
               ("niccapupphā rukkhā hontu", "သစ်ပင်တို့သည် အမြဲ ပန်းပွင့်ကြပါစေ"),
               ("niccaphalikā rukkhā hontu", "သစ်ပင်တို့သည် အမြဲ အသီး သီးကြပါစေ"),
               ("niccaṃ juṇhaṃ hotu", "အမြဲ လရောင် သာပါစေ"), ("niccaṃ khemaṃ hotu", "အမြဲ ဘေးကင်းပါစေ"),
               ("niccaṃ subhikkhaṃ hotu", "အမြဲ စားနပ်ရိက္ခာ ပေါများပါစေ"), ("niccaṃ suvatthi hotu", "အမြဲ ချမ်းသာပါစေ"),
               ("uppanno phasso mā nirujjhi", "ဖြစ်ပေါ်ပြီးသော တွေ့ထိမှုသည် မချုပ်ငြိမ်းပါစေနှင့်"),
               ("rūpaṃ niccaṃ hotu", "ရုပ်သည် မြဲပါစေ"), ("viññāṇaṃ niccaṃ hotu", "သိစိတ်သည် မြဲပါစေ")):
    P(_k, Fixed(_m))
ANCHOR_X["suvatthi"] = "ချမ်းသာပါစေ"
VAR_X["suvuṭṭhikaṃ"] = F.PATHA
P("uppannā vedanā… saññā… cetanā… cittaṃ… saddhā… vīriyaṃ… sati… samādhi… paññā mā nirujjhi",
  Fixed("ဖြစ်ပေါ်ပြီးသော ခံစားမှု… မှတ်သိမှု… စေ့ဆော်မှု… စိတ်… ယုံကြည်မှု… ဝီရိယ… သတိ… သမာဓိ… ပညာသည် "
        "မချုပ်ငြိမ်းပါစေနှင့်"))


@F.frame(r"(?P<x>.+?)ti – (?P<p>atthi adhippāyaiddhi buddhānaṃ vā sāvakānaṃ vā)ti\?")
def _f_wish(m):
    """«"WISH"ti – atthi adhippāyaiddhi …ti?» = «“WISH”ဟု – … ဣဒ္ဓိ ရှိသလော။» (the dash kept; harmonise B5: «ti» = «ဟု»)."""
    return f"“{F.pq(m['x'], 'stmt', 1)}”ဟု – {F.pq(m['p'], 'q')}{END}"


before_generic()
_APQ = V(f"{_BS} {API}", EXIST).f("q")
S("Rūpaṃ niccaṃ hotūti – atthi adhippāyaiddhi… vedanā…pe… saññā…pe… saṅkhārā…pe… viññāṇaṃ niccaṃ hotūti – atthi "
  "adhippāyaiddhi buddhānaṃ vā sāvakānaṃ vāti?",
  f"“ရုပ်သည် မြဲပါစေ”ဟု – {API} ရှိ… ခံစားမှု… မှတ်သိမှု… ပြုပြင်ဖန်တီးမှုတို့… “သိစိတ်သည် မြဲပါစေ”ဟု – "
  f"{_APQ}{END}")
S("Jātidhammā sattā mā jāyiṃsūti atthi…pe… jarādhammā sattā mā jīriṃsūti…pe… byādhidhammā sattā mā byādhiyiṃsūti…pe… "
  "maraṇadhammā sattā mā mīyiṃsūti – atthi adhippāyaiddhi buddhānaṃ vā sāvakānaṃ vāti?",
  f"“မွေးဖွားခြင်း သဘော ရှိသော သတ္တဝါတို့သည် မမွေးဖွားကြပါစေနှင့်”ဟု ရှိ… “အိုခြင်း သဘော ရှိသော "
  f"သတ္တဝါတို့သည် မအိုကြပါစေနှင့်”ဟု… “နာခြင်း သဘော ရှိသော သတ္တဝါတို့သည် မနာကြပါစေနှင့်”ဟု… “သေခြင်း သဘော "
  f"ရှိသော သတ္တဝါတို့သည် မသေကြပါစေနှင့်”ဟု – {_APQ}{END}")
PIL = "အသျှင် ပိလိန္ဒဝစ္ဆ"
_KING = "မဂဓ မင်း သေနိယ ဗိမ္ဗိသာရ၏ ပြာသာဒ်ကို"
P("āyasmā pilindavaccho rañño māgadhassa seniyassa bimbisārassa pāsādaṃ suvaṇṇantveva adhimucci",
  bb(f"{PIL}သည် {_KING} «ရွှေ»ဟုသာ", "ဆုံးဖြတ်ခဲ့"))
P("suvaṇṇo ca pana āsi", Cl("ရွှေလည်း အမှန်ပင်", "ဖြစ်ခဲ့", "မဖြစ်ခဲ့"))
REF_X["pārā."] = "“ပါရာဇိကဏ်”"
# --- (204) 5. Buddhakathā
section("(204) 5. Buddhakathā", f"(204) 5. ဘုရားအကြောင်း {KATHA}")
section("Buddhakathā", f"ဘုရားအကြောင်း {KATHA}")
P("atthi buddhānaṃ buddhehi hīnātirekatā", V("ဘုရားတို့၌ ဘုရားတို့ထက် ယုတ်ခြင်း ထူးခြင်း", EXIST))
_ATO = "အားဖြင့်"
S("Satipaṭṭhānatoti?", f"{GRP['satipaṭṭhānā']}{_ATO}လော{END}")
S("sammappadhānato…pe… iddhipādato… indriyato… balato… bojjhaṅgato… vasibhāvato…pe… sabbaññutañāṇadassanatoti?",
  "… ".join(f"{GRP[x]}{_ATO}" for x in _G6) + f"… အစိုးရခြင်း{_ATO}… အလုံးစုံကို သိမြင်သော ဉာဏ်{_ATO}လော{END}")
# --- (205) 6. Sabbadisākathā
DIS = {"puratthimāya": "အရှေ့", "dakkhiṇāya": "တောင်", "pacchimāya": "အနောက်", "uttarāya": "မြောက်",
       "heṭṭhimāya": "အောက်", "uparimāya": "အထက်"}
section("(205) 6. Sabbadisākathā", f"(205) 6. အရပ် အားလုံးအကြောင်း {KATHA}")
section("Sabbadisākathā", f"အရပ် အားလုံးအကြောင်း {KATHA}")
STD = ("တည်ရှိ", "မတည်ရှိ")
P("sabbā disā buddhā tiṭṭhanti", Cl("အရပ် အားလုံးတို့၌ ဘုရားတို့", "တည်ရှိကြ", "မတည်ရှိကြ"))
for _k, _m in DIS.items():
    P(f"{_k} disāya buddho tiṭṭhati", Cl(f"{_m} အရပ်၌ ဘုရား", *STD))
    P(f"{_k} disāya", FR(f"{_m} အရပ်၌"))
_WHO = (f"ထိုမြတ်စွာဘုရားသည် အဘယ် အမည် ရှိသနည်း၊ အဘယ် အမျိုးဇာတ် ရှိသနည်း၊ အဘယ် အနွယ် ရှိသနည်း၊ "
        f"ထိုမြတ်စွာဘုရား၏ မိဘတို့သည် အဘယ် အမည် ရှိကြသနည်း၊ ထိုမြတ်စွာဘုရား၏ တပည့် အစုံသည် အဘယ် အမည် "
        f"ရှိသနည်း၊ ထိုမြတ်စွာဘုရား၏ အလုပ်အကျွေးသည် အဘယ် အမည် ရှိသနည်း၊ အဘယ်သို့သော သင်္ကန်းကို "
        f"ဆောင်သနည်း၊ အဘယ်သို့သော သပိတ်ကို ဆောင်သနည်း၊ အဘယ် ရွာ၌ဖြစ်စေ၊ နိဂုံး၌ဖြစ်စေ၊ မြို့၌ဖြစ်စေ၊ "
        f"တိုင်း၌ဖြစ်စေ၊ ဇနပုဒ်၌ဖြစ်စေ နေသနည်း{END}")
S("Kinnāmo so bhagavā, kiṃjacco, kiṃgotto, kinnāmā tassa bhagavato mātāpitaro, kinnāmaṃ tassa bhagavato sāvakayugaṃ, "
  "konāmo tassa bhagavato upaṭṭhāko, kīdisaṃ cīvaraṃ dhāreti, kīdisaṃ pattaṃ dhāreti, katarasmiṃ gāme vā nigame vā "
  "nagare vā raṭṭhe vā janapade vāti?", _WHO)
S("Kinnāmo so bhagavā…pe… janapade vāti?", f"ထိုမြတ်စွာဘုရားသည် အဘယ် အမည် ရှိသနည်း… ဇနပုဒ်၌ဖြစ်စေ နေသနည်း{END}")
for _k, _m in (("cātumahārājike", "စာတုမဟာရာဇ် နတ်ပြည်၌"), ("tāvatiṃse", "တာဝတိံသာ နတ်ပြည်၌"),
               ("yāme", "ယာမာ နတ်ပြည်၌"), ("tusite", "တုသိတာ နတ်ပြည်၌"), ("nimmānaratiyā", "နိမ္မာနရတီ နတ်ပြည်၌"),
               ("paranimmitavasavattiyā", "ပရနိမ္မိတဝသဝတ္တီ နတ်ပြည်၌"), ("brahmaloke", "ဗြဟ္မာ့ပြည်၌")):
    P(f"{_k} tiṭṭhati", Cl(_m, *STD))
# --- (206) 7. Dhammakathā / (207) 8. Kammakathā
section("(206) 7. Dhammakathā", f"(206) 7. သဘောတရားအကြောင်း {KATHA}")
section("Dhammakathā", f"သဘောတရားအကြောင်း {KATHA}")
section("(207) 8. Kammakathā", f"(207) 8. ကံအကြောင်း {KATHA}")
section("Kammakathā", f"ကံအကြောင်း {KATHA}")
MN = new("micchattaniyata / sammattaniyata / aniyata (pi-1)", ("မှားယွင်းမှု၌ ကျိန်းသေ", "မှန်ကန်မှု၌ ကျိန်းသေ", "မကျိန်းသေ"))
W("1", "^1-M1-15", "sammattaniyatā dhammā", "မှန်ကန်မှု၌ ကျိန်းသေ")
W("1", "^1-M1-15", "aniyatā dhammā", "မကျိန်းသေ")
for _k, _m in (("sabbe dhammā niyatā", f"{P6.ALL_DH}တို့သည် {NIYATA}ကြ"), ("sabbe kammā niyatā", f"ကံ အားလုံးတို့သည် {NIYATA}ကြ")):
    P(_k, Cl(_m[:-len(NIYATA + "ကြ")].rstrip(), NIYATA + "ကြ", "မ" + NIYATA + "ကြ"))
P("micchattaniyatā", Cl(MN[0][:-len(NIYATA)].rstrip(), NIYATA + "ကြ", "မ" + NIYATA + "ကြ"))
P("sammattaniyatā", Cl(MN[1][:-len(NIYATA)].rstrip(), NIYATA + "ကြ", "မ" + NIYATA + "ကြ"))
P("micchattaniyataṃ", Cl(MN[0][:-len(NIYATA)].rstrip(), NIYATA, "မ" + NIYATA))
P("sammattaniyataṃ", Cl(MN[1][:-len(NIYATA)].rstrip(), NIYATA, "မ" + NIYATA))
RASI = "အစု"
for _e, _neg in (("atthi", False), ("natthi", True)):
    P(f"{_e} aniyato rāsi", V(f"{MN[2]}သော {RASI}", EXIST, _neg))
_R3 = f"{MN[0]}သော {RASI}၊ {MN[1]}သော {RASI}၊ {MN[2]}သော {RASI}"
P("tayo rāsī vuttā bhagavatā – micchattaniyato rāsi, sammattaniyato rāsi, aniyato rāsi",
  Cl(f"{RASI} {F.NUM_MY[3]}{F.CL}တို့ကို {BUDDHA}", *SAID, post=f" – {_R3}"))
BR_X["[dha. sa. tikamātikā 15]"] = f"[“{F.heads('Dhammasaṅgaṇīpakaraṇaṃ niṭṭhitaṃ').split('”')[0].lstrip('“')}” {F.heads('Tikamātikā')} 15]"
_RN = f"{F.RUPA.my}သည် {F.RUPA.my}၏ အနက်အားဖြင့်"
_VN = f"{F.VINNANA.my}သည် {F.VINNANA.my}၏ အနက်အားဖြင့်"
P("rūpaṃ rūpaṭṭhena niyataṃ", Cl(_RN, NIYATA, "မ" + NIYATA))
P("vedanā… saññā… saṅkhārā… viññāṇaṃ viññāṇaṭṭhena niyataṃ",
  Cl(f"{F.VEDANA.my}… {F.SANNA.my}… {F.SANKHARA.my}… {_VN}", NIYATA, "မ" + NIYATA))
P("rūpaṃ rūpaṭṭhena niyataṃ… vedanā… saññā… saṅkhārā… viññāṇaṃ viññāṇaṭṭhena niyataṃ",
  Cl(f"{_RN} {NIYATA}၏… {F.VEDANA.my}… {F.SANNA.my}… {F.SANKHARA.my}… {_VN}", NIYATA, "မ" + NIYATA))
P("rūpaṃ rūpaṭṭhena niyataṃ, vedanā… saññā… saṅkhārā… viññāṇaṃ viññāṇaṭṭhena niyataṃ",
  Cl(f"{_RN} {NIYATA}၏၊ {F.VEDANA.my}… {F.SANNA.my}… {F.SANKHARA.my}… {_VN}", NIYATA, "မ" + NIYATA))
P("rūpaṃ vedanā hoti… saññā hoti… saṅkhārā honti… viññāṇaṃ hoti… vedanā… saññā… saṅkhārā… viññāṇaṃ rūpaṃ hoti… "
  "vedanā hoti… saññā hoti… saṅkhārā honti",
  V(f"{F.RUPA.my}သည် {F.VEDANA.my} ဖြစ်၏… {F.SANNA.my} ဖြစ်၏… {F.SANKHARA.my} ဖြစ်ကြ၏… {F.VINNANA.my} ဖြစ်၏… "
    f"{F.VEDANA.my}… {F.SANNA.my}… {F.SANKHARA.my}… {F.VINNANA.my}သည် {F.RUPA.my} ဖြစ်၏… {F.VEDANA.my} ဖြစ်၏… "
    f"{F.SANNA.my} ဖြစ်၏… {F.SANKHARA.my}"))
KV = new("diṭṭhadhamma- / upapajja- / aparāpariyavedanīyaṃ kammaṃ",
         ("မျက်မှောက်ဘဝ၌ ခံစားရမည့် ကံ", "နောက်ဘဝ၌ ခံစားရမည့် ကံ", "နောက်ဘဝ အဆက်ဆက်၌ ခံစားရမည့် ကံ"))
_KVP = {"diṭṭhadhammavedanīyaṃ": KV[0], "upapajjavedanīyaṃ": KV[1], "aparāpariyavedanīyaṃ": KV[2]}
_KVN = {k: v.rsplit(" ", 1)[0] for k, v in _KVP.items()}                # «… ခံစားရမည့်»
for _k, _m in _KVP.items():
    P(f"{_k} kammaṃ {_k[:-1]}ṭṭhena niyataṃ", Cl(f"{_m}သည် {_KVN[_k]} အနက်အားဖြင့်", NIYATA, "မ" + NIYATA))
    P(f"{_k} kammaṃ", FR(_m))
_KV3 = (f"{KV[0]}သည် {_KVN['diṭṭhadhammavedanīyaṃ']} အနက်အားဖြင့် {NIYATA}၏၊ {KV[1]}… {KV[2]}သည် "
        f"{_KVN['aparāpariyavedanīyaṃ']} အနက်အားဖြင့်")
P("diṭṭhadhammavedanīyaṃ kammaṃ diṭṭhadhammavedanīyaṭṭhena niyataṃ, upapajjavedanīyaṃ kammaṃ… aparāpariyavedanīyaṃ "
  "kammaṃ aparāpariyavedanīyaṭṭhena niyataṃ", Cl(_KV3, NIYATA, "မ" + NIYATA))
P("diṭṭhadhammavedanīyaṃ kammaṃ upapajjavedanīyaṃ hoti, aparāpariyavedanīyaṃ hoti… upapajjavedanīyaṃ kammaṃ "
  "diṭṭhadhammavedanīyaṃ hoti, aparāpariyavedanīyaṃ hoti… aparāpariyavedanīyaṃ kammaṃ diṭṭhadhammavedanīyaṃ hoti, "
  "upapajjavedanīyaṃ hoti",
  V(f"{KV[0]}သည် {KV[1]} ဖြစ်၏၊ {KV[2]} ဖြစ်၏… {KV[1]}သည် {KV[0]} ဖြစ်၏၊ {KV[2]} ဖြစ်၏… {KV[2]}သည် {KV[0]} "
    f"ဖြစ်၏၊ {KV[1]}"))
LINES_X[key("Sāsanaṃ navaṃ kataṃ atthi koci tathāgatassa sāsanaṃ navaṃ karoti labbhā tathāgatassa sāsanaṃ puna navaṃ "
            "kātuṃ, puthujjano tedhātukehi dhammehi avivitto, atthi kiñci saṃyojanaṃ appahāya arahattappatti, atthi "
            "adhippāyiddhi buddhānaṃ vā sāvakānaṃ vā, atthi buddhānaṃ buddhehi hīnātirekatā, sabbā disā buddhā "
            "tiṭṭhanti, sabbe dhammā niyatā, sabbe kammā niyatāti.")] = (
    f"{SASANA}ကို {NEW_} ပြုထား၊ {BUDDHA}၏ {SASANA}ကို {NEW_} {_DO} ရှိ၊ {BUDDHA}၏ {SASANA}ကို တစ်ဖန် {NEW_} "
    f"ပြုလုပ်နိုင်၊ {PUTHU}သည် {TEDH} သဘောတရားတို့မှ {AVIV}၊ {SAMY} တစ်စုံတစ်ရာ{APP} {ARP} ရှိ၊ {_BS} {API} "
    f"ရှိ၊ ဘုရားတို့၌ ဘုရားတို့ထက် ယုတ်ခြင်း ထူးခြင်း ရှိ၊ အရပ် အားလုံးတို့၌ ဘုရားတို့ တည်ရှိကြ၊ "
    f"{P6.ALL_DH}တို့သည် {NIYATA}ကြ၊ ကံ အားလုံးတို့သည် {NIYATA}ကြ{END}")

# ===================================================================================== 30. Bāvīsatimavaggo
vagga("Bāvīsatimavaggo", 22)
section("(208) 1. Parinibbānakathā", f"(208) 1. {PNB}အကြောင်း {KATHA}")
section("Parinibbānakathā", f"{PNB}အကြောင်း {KATHA}")
PNV = ("ပရိနိဗ္ဗာန် ပြု", "ပရိနိဗ္ဗာန် မပြု")                          # parinibbāyati (pi-4 «ပရိနိဗ္ဗာန် ပြု»)
ARH = F.ARAHA
# --- (209) 2. Kusalacittakathā
section("(209) 2. Kusalacittakathā", f"(209) 2. ကုသိုလ် စိတ်အကြောင်း {KATHA}")
section("Kusalacittakathā", f"ကုသိုလ် စိတ်အကြောင်း {KATHA}")
P("arahā kusalacitto parinibbāyati", Cl(f"{ARH}သည် ကုသိုလ် စိတ် ရှိလျက်", *PNV))
_SV = "သို့ ပို့ဆောင်တတ်သော ကံကို ပြုလျက်"
P("arahā puññābhisaṅkhāraṃ abhisaṅkharonto… āneñjābhisaṅkhāraṃ abhisaṅkharonto… gatisaṃvattaniyaṃ kammaṃ karonto… "
  "bhavasaṃvattaniyaṃ kammaṃ karonto… issariyasaṃvattaniyaṃ kammaṃ karonto… adhipaccasaṃvattaniyaṃ kammaṃ karonto… "
  "mahābhogasaṃvattaniyaṃ kammaṃ karonto… mahāparivārasaṃvattaniyaṃ kammaṃ karonto… devasobhagyasaṃvattaniyaṃ kammaṃ "
  "karonto… manussasobhagyasaṃvattaniyaṃ kammaṃ karonto parinibbāyati",
  Cl(f"{ARH}သည် ကောင်းမှု ပြုပြင်ဖန်တီးမှုကို ပြုပြင်ဖန်တီးလျက်… မတုန်မလှုပ်သော ပြုပြင်ဖန်တီးမှုကို "
     f"ပြုပြင်ဖန်တီးလျက်… လားရာ{_SV}… ဘဝ{_SV}… အစိုးရခြင်း{_SV}… အကြီးအကဲ ဖြစ်ခြင်း{_SV}… စည်းစိမ် "
     f"များခြင်း{_SV}… အခြံအရံ များခြင်း{_SV}… နတ်တို့၏ ကောင်းကျိုး ချမ်းသာ{_SV}… လူတို့၏ ကောင်းကျိုး ချမ်းသာ{_SV}",
     *PNV))
P("arahā ācinanto apacinanto pajahanto upādiyanto visinento ussinento vidhūpento sandhūpento parinibbāyati",
  Cl(f"{ARH}သည် စုဆောင်းလျက်၊ ဖျက်ဆီးလျက်၊ ပယ်လျက်၊ စွဲလမ်းလျက်၊ ဖြန့်ကျက်လျက်၊ စုစည်းလျက်၊ ငြိမ်းစေလျက်၊ "
     f"တောက်လောင်စေလျက်", *PNV))
P("arahā nevācināti na apacināti apacinitvā ṭhito", V(f"{ARH}သည် မစုဆောင်း၊ မဖျက်ဆီး၊ ဖျက်ဆီးပြီး၍ တည်နေသူ"))
P("arahā neva vidhūpeti na sandhūpeti vidhūpetvā ṭhito", V(f"{ARH}သည် မငြိမ်းစေ၊ မတောက်လောင်စေ၊ ငြိမ်းစေပြီး၍ တည်နေသူ"))
S("Nanu arahā neva pajahati na upādiyati pajahitvā ṭhito, neva visineti na ussineti visinetvā ṭhito; nanu arahā neva "
  "vidhūpeti na sandhūpeti vidhūpetvā ṭhitoti?",
  f"{ARH}သည် မပယ်၊ မစွဲလမ်း၊ ပယ်ပြီး၍ တည်နေသူ ဖြစ်သည်၊ မဖြန့်ကျက်၊ မစုစည်း၊ ဖြန့်ကျက်ပြီး၍ တည်နေသူ ဖြစ်သည် "
  f"မဟုတ်လော၊ {ARH}သည် မငြိမ်းစေ၊ မတောက်လောင်စေ၊ ငြိမ်းစေပြီး၍ တည်နေသူ ဖြစ်သည် မဟုတ်လော{END}")
P("arahā upaṭṭhitassati sato sampajāno parinibbāyati",
  Cl(f"{ARH}သည် သတိ ထင်ရှား တည်လျက်၊ သတိ ရှိလျက်၊ ကောင်းစွာ ဆင်ခြင်သိမြင်လျက်", *PNV))
# --- (210) 3. Āneñjakathā
ANJ = new("āneñja (the imperturbable)", "မတုန်မလှုပ်သော အခြေ")
section("(210) 3. Āneñjakathā", f"(210) 3. {ANJ}အကြောင်း {KATHA}")
section("Āneñjakathā", f"{ANJ}အကြောင်း {KATHA}")
ABY = "ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော"                       # abyākata (book frame, pi-1)
for _k, _m in (("āneñje", ANJ), ("pakaticitte", "ပကတိ စိတ်"), ("kiriyamaye citte", "ကြိယာ စိတ်"),
               ("vipākacitte", "အကျိုး စိတ်"), ("kiriyābyākate citte", f"{ABY} ကြိယာ စိတ်"),
               ("vipākābyākate citte", f"{ABY} အကျိုး စိတ်")):
    P(f"arahā {_k} ṭhito parinibbāyati", Cl(f"{ARH}သည် {_m}၌ တည်လျက်", *PNV))
P("bhagavā catutthajjhānā vuṭṭhahitvā samanantarā parinibbuto",
  bb(f"{BUDDHA}သည် စတုတ္ထ {JH}မှ ထ၍ ချက်ချင်း", "ပရိနိဗ္ဗာန် ပြုတော်မူခဲ့"))
# --- (211) 4. Dhammābhisamayakathā
DAB = new("dhammābhisamayo", f"တရားကို {'ထင်ထင်ရှားရှား သိမြင်ခြင်း'}")       # abhisamaya (make_ch2-5.py ABHISAMAYA)
GAB = new("gabbhaseyyāya", "အမိဝမ်း၌ ကိန်းအောင်းစဉ်")
SUP = new("supinagatassa", "အိပ်မက် မက်နေသူ၌")
section("(211) 4. Dhammābhisamayakathā", f"(211) 4. {DAB}အကြောင်း {KATHA}")
section("Dhammābhisamayakathā", f"{DAB}အကြောင်း {KATHA}")
for _w, _wm in (("gabbhaseyyāya", GAB), ("supinagatassa", SUP)):
    P(f"atthi {_w} dhammābhisamayo", V(f"{_wm} {DAB}", EXIST))
    P(f"atthi {_w} arahattappatti", V(f"{_wm} {ARP}", EXIST))
_GD = W("1", "^1-M2-128", "indriyesu guttadvāratā", "အာရုံခံ အင်္ဂါတို့၏ တံခါးကို စောင့်ထိန်းခြင်း")
_MT = W("1", "^1-1355", "bhojane mattaññutā", "အစားအစာ၌ အတိုင်းအရှည်ကို သိခြင်း")
_L8 = ["တရား ဟောကြားခြင်း", "တရား နာကြားခြင်း", "တရား ဆွေးနွေးခြင်း", "မေးမြန်းခြင်း", "သီလ ဆောက်တည်ခြင်း", _GD, _MT,
       "ညဉ့်ဦးယံ ညဉ့်နောက်ယံ၌ နိုးကြားစွာ အားထုတ်ခြင်း"]
for _e, _neg in (("atthi", False), ("natthi", True)):
    P(f"{_e} gabbhaseyyāya dhammadesanā, dhammassavanaṃ, dhammasākacchā, paripucchā, sīlasamādānaṃ, indriyesu "
      "guttadvāratā, bhojane mattaññutā, pubbarattāpararattaṃ jāgariyānuyogo", V(f"{GAB} " + "၊ ".join(_L8), EXIST, _neg))
    P(f"{_e} gabbhaseyyāya dhammadesanā, dhammassavanaṃ… pubbarattāpararattaṃ jāgariyānuyogo",
      V(f"{GAB} {_L8[0]}၊ {_L8[1]}… {_L8[-1]}", EXIST, _neg))
P("dve paccayā sammādiṭṭhiyā uppādāya – parato ca ghoso, yoniso ca manasikāro",
  V(f"{FAC['sammādiṭṭhi']} ဖြစ်ပေါ်ရန် အကြောင်း {F.NUM_MY[2]}{F.CL}", EXIST,
    post=" – သူတစ်ပါးထံမှ ကြားရသော အသံနှင့် သင့်လျော်စွာ နှလုံးသွင်းခြင်း"))
SPM = "အိပ်ပျော်နေသူ၊ မေ့လျော့နေသူ၊ သတိ လစ်နေသူ၊ ကောင်းစွာ ဆင်ခြင်သိမြင်ခြင်း ကင်းသူ၌"
P("suttassa pamattassa muṭṭhassatissa asampajānassa dhammābhisamayo", V(f"{SPM} {DAB}", EXIST))
P("suttassa pamattassa muṭṭhassatissa asampajānassa arahattappatti", V(f"{SPM} {ARP}", EXIST))
section("(212-4) 5-7. Tissopikathā", f"(212-4) 5-7. သုံးပါးလုံးအကြောင်း {KATHA}")
section("Tissopikathā", f"သုံးပါးလုံးအကြောင်း {KATHA}")
# --- (215) 8. Abyākatakathā
section("(215) 8. Abyākatakathā", f"(215) 8. {ABY} အရာအကြောင်း {KATHA}")
section("Abyākatakathā", f"{ABY} အရာအကြောင်း {KATHA}")
SUPC = "အိပ်မက် မက်နေသူ၏ စိတ်"
P("sabbaṃ supinagatassa cittaṃ abyākataṃ", V(f"{SUPC} အားလုံးသည် {ABY} အရာ"))
SUPN = "အိပ်မက်ထဲ၌"
P("supinantena pāṇaṃ haneyya", Cl(f"{SUPN} သတ္တဝါကို", "သတ်ရာ", "မသတ်ရာ"))
P("supinantena cetiyaṃ abhidakkhiṇaṃ kareyya", Cl(f"{SUPN} စေတီကို", "လက်ယာရစ် လှည့်ရာ", "လက်ယာရစ် မလှည့်ရာ"))
ACT11 = [("adinnaṃ", "မပေးသည်ကို ယူ"), ("musā", "မုသား ပြော"), ("pisuṇaṃ", "ကုန်းချောစကား ပြော"),
         ("pharusaṃ", "ကြမ်းတမ်းသော စကား ပြော"), ("samphaṃ", "အကျိုးမဲ့ စကား ပြော"), ("sandhiṃ", "အိမ်ကို ဖောက်ထွင်း"),
         ("nillopaṃ", "လုယက်"), ("ekāgārikaṃ", "အိမ်တစ်လုံးကို ဝိုင်းဝန်း လုယက်"), ("paripanthe", "လမ်း၌ ဓားပြ တိုက်"),
         ("paradāraṃ", "သူတစ်ပါး၏ မယားထံ သွား"), ("gāmaghātakaṃ", "ရွာကို ဖျက်ဆီး"), ("nigamaghātakaṃ", "နိဂုံးကို ဖျက်ဆီး")]
_A = dict(ACT11)
P("supinantena adinnaṃ ādiyeyya… musā bhaṇeyya, pisuṇaṃ bhaṇeyya, pharusaṃ bhaṇeyya, samphaṃ palapeyya, sandhiṃ "
  "chindeyya, nillopaṃ hareyya, ekāgārikaṃ kareyya, paripanthe tiṭṭheyya, paradāraṃ gaccheyya, gāmaghātakaṃ kareyya, "
  "nigamaghātakaṃ kareyya, supinantena methunaṃ dhammaṃ paṭiseveyya, supinagatassa asuci mucceyya, supinantena "
  "dānaṃ dadeyya, cīvaraṃ dadeyya, piṇḍapātaṃ dadeyya, senāsanaṃ dadeyya, gilānapaccayabhesajjaparikkhāraṃ dadeyya, "
  "khādanīyaṃ dadeyya, bhojanīyaṃ dadeyya, pānīyaṃ dadeyya, cetiyaṃ vandeyya, cetiye mālaṃ āropeyya, gandhaṃ "
  "āropeyya, vilepanaṃ āropeyya… cetiyaṃ abhidakkhiṇaṃ kareyya",
  Cl(f"{SUPN} {_A['adinnaṃ']}ရာ၏… " + "၊ ".join(f"{_A[k]}ရာ၏" for k, _ in ACT11[1:]) +
     f"၊ {SUPN} {P6.ACTS['methunaṃ dhammaṃ paṭiseveyya'][0]} {P6.ACTS['methunaṃ dhammaṃ paṭiseveyya'][1]}၏၊ "
     f"အိပ်မက် မက်နေသူ၏ {P6.ASUCI_ACC} ထွက်ရာ၏၊ {SUPN} အလှူကို ပေးရာ၏၊ {P11.REQ['cīvaraṃ']}ကို ပေးရာ၏၊ "
     f"{P11.REQ['piṇḍapātaṃ']}ကို ပေးရာ၏၊ {P11.REQ['senāsanaṃ']}ကို ပေးရာ၏၊ "
     f"{P11.REQ['gilānapaccayabhesajjaparikkhāraṃ']}ကို ပေးရာ၏၊ ခဲဖွယ်ကို ပေးရာ၏၊ စားဖွယ်ကို ပေးရာ၏၊ သောက်ရေကို "
     f"ပေးရာ၏၊ စေတီကို ရှိခိုးရာ၏၊ စေတီ၌ ပန်းကို တင်ရာ၏၊ နံ့သာကို တင်ရာ၏၊ နံ့သာပျောင်းကို တင်ရာ၏… စေတီကို",
     "လက်ယာရစ် လှည့်ရာ", "လက်ယာရစ် မလှည့်ရာ"))
ABBOH = new("abbohāriya", "ထည့်တွက်ရန် မထိုက်သော အရာ")
P("supinagatassa cittaṃ abbohāriyaṃ vuttaṃ bhagavatā", Cl(f"{SUPC}ကို {ABBOH}ဟု {BUDDHA}", *SAID))
# --- (216) 9. Āsevanapaccayakathā
ASV = new("āsevanapaccayatā", "အဖန်ဖန် မှီဝဲခြင်း အကြောင်းဖြစ်ခြင်း")
section("(216) 9. Āsevanapaccayakathā", f"(216) 9. {ASV}အကြောင်း {KATHA}")
section("Āsevanapaccayakathā", f"{ASV}အကြောင်း {KATHA}")
for _e, _neg in (("atthi", False), ("natthi", True)):
    P(f"{_e} kāci āsevanapaccayatā", V(f"{ASV} တစ်စုံတစ်ရာ", EXIST, _neg))
_ASB = "အဖန်ဖန် မှီဝဲထား၊ ပွားများထား၊ အကြိမ်များစွာ ပြုထားသော"
_LEAD = "သို့ ပို့ဆောင်တတ်၏"
_HELL3 = f"ငရဲ{_LEAD}၊ {F.TIRACCHANA} {P11.TOK['yoni']}{_LEAD}၊ ပြိတ္တာ နယ်{_LEAD}"
_LH = "၏ အပေါ့ဆုံး အကျိုးသည် လူ ဖြစ်လာသူအား"
Q("pāṇātipāto, bhikkhave, āsevito bhāvito bahulīkato nirayasaṃvattaniko tiracchānayonisaṃvattaniko "
  "pettivisayasaṃvattaniko, yo sabbalahuso pāṇātipātassa vipāko manussabhūtassa appāyukasaṃvattaniko hoti",
  f"{_R} {_ASB} {F.PANATIPATA}သည် {_HELL3}၊ {F.PANATIPATA}{_LH} အသက် တိုခြင်း{_LEAD}")
Q("adinnādānaṃ, bhikkhave, āsevitaṃ bhāvitaṃ bahulīkataṃ nirayasaṃvattanikaṃ tiracchānayonisaṃvattanikaṃ "
  "pettivisayasaṃvattanikaṃ, yo sabbalahuso adinnādānassa vipāko manussabhūtassa bhogabyasanasaṃvattaniko hoti… yo "
  "sabbalahuso kāmesumicchācārassa vipāko manussabhūtassa sapattaverasaṃvattaniko hoti… yo sabbalahuso musāvādassa "
  "vipāko manussabhūtassa abbhūtabbhakkhānasaṃvattaniko hoti… yo sabbalahuso pisuṇāya vācāya vipāko manussabhūtassa "
  "mittehi bhedanasaṃvattaniko hoti… yo sabbalahuso pharusāya vācāya vipāko manussabhūtassa amanāpasaddasaṃvattaniko "
  "hoti… yo sabbalahuso samphappalāpassa vipāko manussabhūtassa anādeyyavācāsaṃvattaniko hoti, surāmerayapānaṃ, "
  "bhikkhave, āsevitaṃ… yo sabbalahuso surāmerayapānassa vipāko manussabhūtassa ummattakasaṃvattaniko hoti",
  f"{_R} {_ASB} မပေးသည်ကို ယူခြင်းသည် {_HELL3}၊ မပေးသည်ကို ယူခြင်း{_LH} စည်းစိမ် ပျက်စီးခြင်း{_LEAD}… "
  f"ကာမတို့၌ မှားယွင်းစွာ ကျင့်ခြင်း{_LH} ရန်သူ ရန်ငြိုး{_LEAD}… မုသား ပြောခြင်း{_LH} လုပ်ကြံ "
  f"စွပ်စွဲခံရခြင်း{_LEAD}… ကုန်းချောစကား{_LH} မိတ်ဆွေတို့နှင့် ကွဲပြားခြင်း{_LEAD}… ကြမ်းတမ်းသော စကား{_LH} "
  f"မနှစ်သက်ဖွယ် အသံ{_LEAD}… အကျိုးမဲ့ စကား{_LH} လက်မခံထိုက်သော စကား{_LEAD}၊ {_R} {_ASB} သေရည် အရက် "
  f"သောက်ခြင်းသည်… သေရည် အရက် သောက်ခြင်း{_LH} ရူးသွပ်ခြင်း{_LEAD}")
MICCHA = {"micchādiṭṭhi": "မှားယွင်းသော အယူ", "micchāsaṅkappo": "မှားယွင်းသော ကြံစည်မှု",
          "micchāsamādhi": "မှားယွင်းသော သမာဓိ"}
Q("micchādiṭṭhi, bhikkhave, āsevitā bhāvitā bahulīkatā nirayasaṃvattanikā tiracchānayonisaṃvattanikā "
  "pettivisayasaṃvattanikā", f"{_R} {_ASB} {MICCHA['micchādiṭṭhi']}သည် {_HELL3}")
Q("micchāsaṅkappo… micchāsamādhi, bhikkhave, āsevito bhāvito… pettivisayasaṃvattaniko",
  f"{MICCHA['micchāsaṅkappo']}… {_R} အဖန်ဖန် မှီဝဲထား၊ ပွားများထား… {MICCHA['micchāsamādhi']}သည် ပြိတ္တာ နယ်{_LEAD}")
_AMT = "အမြိုက်၌ သက်ဝင်သည်၊ အမြိုက်ကို ဆုံးခန်းတိုင်ရာ ပြုသည်၊ အမြိုက်၌ အဆုံးသတ်သည် ဖြစ်၏"   # harmonise B2: amata = «အမြိုက်» (ch10, ch13-16, ch17; was «မသေခြင်း»)
Q("sammādiṭṭhi, bhikkhave, āsevitā bhāvitā bahulīkatā amatogadhā hoti amataparāyanā amatapariyosānā",
  f"{_R} {_ASB} {FAC['sammādiṭṭhi']}သည် {_AMT}")
S("Nanu vuttaṃ bhagavatā – sammāsaṅkappo, bhikkhave, āsevito bhāvito bahulīkato…pe… sammāsamādhi, bhikkhave, āsevito "
  "bhāvito bahulīkato amatogadho hoti amataparāyano amatapariyosānoti attheva suttantoti, āmantā.",
  f"{BUDDHA} ဤသို့ ဟောတော်မူသည် မဟုတ်လော – “{_R} {_ASB} {FAC['sammāsaṅkappo']}… {_R} {_ASB} "
  f"{FAC['sammāsamādhi']}သည် {_AMT}”{F.SUTTA_TI} {F.ATTHEVA}၊ {F.YES}{END}")
# --- (217) 10. Khaṇikakathā
section("(217) 10. Khaṇikakathā", f"(217) 10. ခဏအကြောင်း {KATHA}")
section("Khaṇikakathā", f"ခဏအကြောင်း {KATHA}")
EKC = f"စိတ် {F.NUM_MY[1]}ခု၏ ခဏမျှသာ တည်သော အရာ"
for _k in ("ekacittakkhaṇikā sabbe dhammā",):
    P(_k, V(f"{P6.ALL_DH}တို့သည် {EKC}တို့"))
P("citte mahāpathavī saṇṭhāti, mahāsamuddo saṇṭhāti, sinerupabbatarājā saṇṭhāti, āpo saṇṭhāti, tejo saṇṭhāti, vāyo "
  "saṇṭhāti, tiṇakaṭṭhavanappatayo saṇṭhahanti",
  Cl("စိတ် (တစ်ခု၏ ခဏ)၌ မဟာပထဝီ မြေကြီး တည်၏၊ မဟာသမုဒ္ဒရာ တည်၏၊ မြင့်မိုရ် တောင်မင်း တည်၏၊ ရေ တည်၏၊ မီး တည်၏၊ "
     "လေ တည်၏၊ မြက်၊ ထင်း၊ တောအုပ်၊ သစ်ပင်တို့", "တည်ကြ", "မတည်ကြ"))
SHJ = "နှင့်အတူ ပေါ်ပေါက်သော အရာ"                                   # sahajāta (ch11-12 SAHA)
assert P11.SAHA["sahajātaṃ"] == "နှင့်အတူ ပေါ်ပေါက်သော"
_AYT = {k: F.AYATANA[k].my for k in ("cakkhāyatana", "sotāyatana", "ghānāyatana", "jivhāyatana", "kāyāyatana")}
P("cakkhāyatanaṃ cakkhuviññāṇena sahajātaṃ", V(f"{_AYT['cakkhāyatana']}သည် မျက်စိ သိစိတ်{SHJ}"))
P("kāyāyatanaṃ kāyaviññāṇena sahajātaṃ", V(f"{_AYT['kāyāyatana']}သည် ကိုယ် သိစိတ်{SHJ}"))
P("sotāyatanaṃ… ghānāyatanaṃ… jivhāyatanaṃ… kāyāyatanaṃ kāyaviññāṇena sahajātaṃ",
  V(f"{_AYT['sotāyatana']}… {_AYT['ghānāyatana']}… {_AYT['jivhāyatana']}… {_AYT['kāyāyatana']}သည် ကိုယ် သိစိတ်{SHJ}"))
_AV = "ငါ့ရှင်တို့၊"
_EYE = "မိမိ၏ မျက်စိသည် မပျက်စီးဘဲ ရှိ၏"
_TJ = "ထိုအရာနှင့် ဆိုင်သော"
Q("ajjhattikañceva, āvuso, cakkhuṃ aparibhinnaṃ hoti, bāhirā ca rūpā na āpāthaṃ āgacchanti, no ca tajjo samannāhāro "
  "hoti, neva tāva tajjassa viññāṇabhāgassa pātubhāvo hoti. Ajjhattikañceva, āvuso, cakkhuṃ aparibhinnaṃ hoti, bāhirā "
  "ca rūpā āpāthaṃ āgacchanti, no ca tajjo samannāhāro hoti, neva tāva tajjassa viññāṇabhāgassa pātubhāvo hoti. Yato "
  "ca kho, āvuso, ajjhattikañceva cakkhuṃ aparibhinnaṃ hoti, bāhirā ca rūpā āpāthaṃ āgacchanti, tajjo ca samannāhāro "
  "hoti, evaṃ tajjassa viññāṇabhāgassa pātubhāvo hoti",
  f"{_AV} {_EYE}၊ ပြင်ပ အဆင်းအရောင်တို့သည်လည်း မျက်စိ၏ နယ်ပယ်သို့ မရောက်လာကြ၊ {_TJ} နှလုံးသွင်းမှုလည်း မဖြစ်၊ "
  f"ထိုသို့ ဖြစ်လျှင် {_TJ} သိစိတ် အစိတ်အပိုင်း ⟦b⟧ ထင်ရှား ဖြစ်ပေါ်ခြင်း မဖြစ်သေး။ {_AV} {_EYE}၊ ပြင်ပ "
  f"အဆင်းအရောင်တို့သည်လည်း နယ်ပယ်သို့ ရောက်လာကြ၏၊ {_TJ} နှလုံးသွင်းမှုကား မဖြစ်၊ ထိုသို့ ဖြစ်လျှင် {_TJ} သိစိတ် "
  f"အစိတ်အပိုင်း ထင်ရှား ဖြစ်ပေါ်ခြင်း မဖြစ်သေး။ {_AV} အကြင်အခါ {_EYE}၊ ပြင်ပ အဆင်းအရောင်တို့သည်လည်း နယ်ပယ်သို့ "
  f"ရောက်လာကြ၏၊ {_TJ} နှလုံးသွင်းမှုလည်း ဖြစ်၏၊ ဤသို့ ဖြစ်လျှင် {_TJ} သိစိတ် အစိတ်အပိုင်း ထင်ရှား ဖြစ်ပေါ်ခြင်း ဖြစ်၏")
VAR_X["viññāṇabhāvassa"] = F.PATHA
_BODY = "မိမိ၏ ကိုယ်သည် မပျက်စီးဘဲ ရှိ၏"
Q("ajjhattiko ceva, āvuso, kāyo aparibhinno hoti, bāhirā ca phoṭṭhabbā na āpāthaṃ āgacchanti, no ca… ajjhattiko "
  "ceva, āvuso, kāyo aparibhinno hoti, bāhirā ca phoṭṭhabbā āpāthaṃ āgacchanti, no ca… yato ca kho, āvuso, ajjhattiko "
  "ceva kāyo aparibhinno hoti, bāhirā ca phoṭṭhabbā āpāthaṃ āgacchanti, tajjo ca samannāhāro hoti, evaṃ tajjassa "
  "viññāṇabhāgassa pātubhāvo hoti",
  f"{_AV} {_BODY}၊ ပြင်ပ အထိအတွေ့တို့သည်လည်း ကိုယ်၏ နယ်ပယ်သို့ မရောက်လာကြ၊ {_TJ} နှလုံးသွင်းမှုလည်း မဖြစ်… "
  f"{_AV} {_BODY}၊ ပြင်ပ အထိအတွေ့တို့သည်လည်း နယ်ပယ်သို့ ရောက်လာကြ၏၊ {_TJ} နှလုံးသွင်းမှုကား မဖြစ်… {_AV} အကြင်အခါ "
  f"{_BODY}၊ ပြင်ပ အထိအတွေ့တို့သည်လည်း နယ်ပယ်သို့ ရောက်လာကြ၏၊ {_TJ} နှလုံးသွင်းမှုလည်း ဖြစ်၏၊ ဤသို့ ဖြစ်လျှင် "
  f"{_TJ} သိစိတ် အစိတ်အပိုင်း ထင်ရှား ဖြစ်ပေါ်ခြင်း ဖြစ်၏")


@F.frame(r"Nanu āyasmā sāriputto etadavoca – (?P<x>.+?)ti(?P<e>[.?!])")
def _f_sari(m):
    """«Nanu āyasmā sāriputto etadavoca – "Q"ti!» = «အသျှင် သာရိပုတ္တရာသည် ဤသို့ ပြောခဲ့သည် မဟုတ်လော – “Q”။» (harmonise B5)."""
    return f"{P11.SARI}သည် ဤသို့ ပြောခဲ့သည် မဟုတ်လော – “{F.q_set(F.QUOTE_RAW(m['x']), 1)}”{END}"   # harmonise B5: = ch11


before_generic()
P("sabbe dhammā niccā dhuvā sassatā avipariṇāmadhammā",
  V(f"{P6.ALL_DH}တို့သည် မြဲသော၊ ခိုင်ခံ့သော၊ {F.SASSATA}သော၊ ဖောက်ပြန်ပြောင်းလဲခြင်း မရှိသော သဘော ရှိသော အရာတို့"))
LINES_X[key("Atthi kiñci saṃyojanaṃ appahāya parinibbānaṃ, arahā kusalacitto parinibbāyati, arahā āneñje ṭhito "
            "parinibbāyati, atthi gabbhaseyyāya dhammābhisamayo, atthi gabbhaseyyāya arahattappatti, atthi "
            "supinagatassa dhammābhisamayo, atthi supinagatassa arahattappatti, sabbaṃ supinagatassa cittaṃ abyākataṃ, "
            "natthi kāci āsevanapaccayatā, ekacittakkhaṇikā sabbe dhammāti.")] = (
    f"{SAMY} တစ်စုံတစ်ရာ{APP} {PNB} ရှိ၊ {ARH}သည် ကုသိုလ် စိတ် ရှိလျက် ပရိနိဗ္ဗာန် ပြု၊ {ARH}သည် {ANJ}၌ တည်လျက် "
    f"ပရိနိဗ္ဗာန် ပြု၊ {GAB} {DAB} ရှိ၊ {GAB} {ARP} ရှိ၊ {SUP} {DAB} ရှိ၊ {SUP} {ARP} ရှိ၊ {SUPC} အားလုံးသည် "
    f"{ABY} အရာ၊ {ASV} တစ်စုံတစ်ရာ မရှိ၊ {P6.ALL_DH}တို့သည် {EKC}တို့{END}")


# ===================================================================================== 31. Tevīsatimavaggo
vagga("Tevīsatimavaggo", 23)


class Must(Cl):
    """-tabba (gerundive): «… ရမည်» / question «… ရမည်လော»."""

    def __init__(self, pre, v):
        super().__init__(pre, v)

    def f(self, form, depth=0):
        tail = {"stmt": "ရမည်", "q": "ရမည်လော", "bare": "ရမည်", "cond": "ရမည် ဆိုလျှင်", "nanu": "ရမည် မဟုတ်လော",
                "rel": "ရမည့်"}[form]
        return F.q_set(f"{self.pre} {self.v}{tail}", depth)


EKA = new("ekādhippāyena", "တူညီသော ရည်ရွယ်ချက်ဖြင့်")
section("(218) 1. Ekādhippāyakathā", f"(218) 1. တူညီသော ရည်ရွယ်ချက်အကြောင်း {KATHA}")
section("Ekādhippāyakathā", f"တူညီသော ရည်ရွယ်ချက်အကြောင်း {KATHA}")
_MET = P6.ACTS["methunaṃ dhammaṃ paṭiseveyya"][0]                     # «မေထုန် အကျင့်ကို»
P("ekādhippāyena methuno dhammo paṭisevitabbo", Must(f"{EKA} {_MET}", "မှီဝဲ"))
P("ekādhippāyena assamaṇena hotabbaṃ, abhikkhunā hotabbaṃ, chinnamūlena hotabbaṃ pārājikena hotabbaṃ",
  Must(f"{EKA} ရဟန်း မဟုတ်သူ ဖြစ်ရမည်၊ ဘိက္ခု မဟုတ်သူ ဖြစ်ရမည်၊ အမြစ် ပြတ်သူ ဖြစ်ရမည်၊ ပါရာဇိက ကျသူ", "ဖြစ်"))
_T11 = "၊ ".join(f"{_A[k]}ရမည်" for k, _ in ACT11[:-1])
P("ekādhippāyena pāṇo hantabbo, adinnaṃ ādiyitabbaṃ, musā bhaṇitabbā, pisuṇaṃ bhaṇitabbaṃ, pharusaṃ bhaṇitabbaṃ, "
  "samphaṃ palapitabbaṃ, sandhi cheditabbo, nillopaṃ hātabbaṃ, ekāgārikaṃ kātabbaṃ, paripanthe ṭhātabbaṃ, paradāro "
  "gantabbo, gāmaghātako kātabbo, nigamaghātako kātabbo",
  Must(f"{EKA} သတ္တဝါကို သတ်ရမည်၊ {_T11}၊ နိဂုံးကို", "ဖျက်ဆီး"))
# --- (219) 2. Arahantavaṇṇakathā
AMAN = new("amanussā", "လူ မဟုတ်သူတို့")
ARV = f"ရဟန္တာတို့၏ အသွင်ဖြင့် {AMAN}သည်"
section("(219) 2. Arahantavaṇṇakathā", f"(219) 2. ရဟန္တာတို့၏ အသွင်အကြောင်း {KATHA}")
section("Arahantavaṇṇakathā", f"ရဟန္တာတို့၏ အသွင်အကြောင်း {KATHA}")
P("arahantānaṃ vaṇṇena amanussā methunaṃ dhammaṃ paṭisevanti", VV(f"{ARV} {_MET}", "မှီဝဲကြ"))
P("arahantānaṃ vaṇṇena amanussā pāṇaṃ hananti… adinnaṃ ādiyanti, musā bhaṇanti, pisuṇaṃ bhaṇanti, pharusaṃ bhaṇanti, "
  "samphaṃ palapanti, sandhiṃ chindanti, nillopaṃ haranti, ekāgārikaṃ karonti, paripanthe tiṭṭhanti, paradāraṃ "
  "gacchanti, gāmaghātakaṃ karonti… nigamaghātakaṃ karonti",
  VV(f"{ARV} သတ္တဝါကို သတ်ကြ၏… " + "၊ ".join(f"{_A[k]}ကြ၏" for k, _ in ACT11[:-2]) + f"၊ {_A['gāmaghātakaṃ']}ကြ၏… "
     f"နိဂုံးကို", "ဖျက်ဆီးကြ"))
# --- (220-4) 3-7. Issariyakāmakārikādikathā
IKK = new("issariyakāmakārikāhetu", "မိမိ၏ အစွမ်းဖြင့် အလိုရှိတိုင်း ပြုခြင်းကြောင့်")
BSI = f"{P11.BS}သည် {IKK}"
section("(220-4) 3-7. Issariyakāmakārikādikathā", f"(220-4) 3-7. မိမိ၏ အစွမ်းဖြင့် အလိုရှိတိုင်း ပြုခြင်း စသည်တို့အကြောင်း {KATHA}")
section("Issariyakāmakārikākathā", f"မိမိ၏ အစွမ်းဖြင့် အလိုရှိတိုင်း ပြုခြင်းအကြောင်း {KATHA}")
GO = ("သွား", "မသွား")
P("bodhisatto issariyakāmakārikāhetu vinipātaṃ gacchati", Cl(f"{BSI} ပျက်စီးကျရောက်ရာ ဘုံသို့", *GO))
_HELLS = ["ငရဲ", "သဉ္ဇီဝ ငရဲ", "ကာလသုတ် ငရဲ", "တာပန ငရဲ", "မဟာတာပန ငရဲ", "သင်္ဃာတ ငရဲ", "ရောရုဝ ငရဲ"]
P("bodhisatto issariyakāmakārikāhetu nirayaṃ gacchati, sañjīvaṃ gacchati, kālasuttaṃ gacchati, tāpanaṃ gacchati, "
  "mahātāpanaṃ gacchati, saṅghātakaṃ gacchati, roruvaṃ gacchati… avīciṃ gacchati",
  Cl(f"{BSI} " + "၊ ".join(f"{x}သို့ သွား၏" for x in _HELLS).replace("မဟာတာပန ငရဲသို့", "မဟာတာပန ⟦b⟧ ငရဲသို့")
     + "… အဝီစိ ငရဲသို့", *GO))
VAR_X["patāpanaṃ"] = F.PATHA
P("bodhisatto issariyakāmakārikāhetu gabbhaseyyaṃ okkamati", VV(f"{BSI} အမိဝမ်း၌ ကိန်းအောင်းခြင်းသို့", "သက်ဆင်း"))
P("bodhisatto issariyakāmakārikāhetu nirayaṃ upapajjeyya", Cl(f"{BSI} ငရဲ၌", "ပြန်လည် ဖြစ်ပေါ်ရာ", "ပြန်လည် မဖြစ်ပေါ်ရာ"))
P("tiracchānayoniṃ upapajjeyya", Cl(f"{F.TIRACCHANA} {P11.TOK['yoni']}၌", "ပြန်လည် ဖြစ်ပေါ်ရာ", "ပြန်လည် မဖြစ်ပေါ်ရာ"))
P("bodhisatto iddhimā", V(f"{P11.BS}သည် {F.IDDHI} ရှိသူ"))
P("bodhisattena chandiddhipādo bhāvito… vīriyiddhipādo… cittiddhipādo… vīmaṃsiddhipādo bhāvito",
  Cl(f"{P11.BS}သည် ဆန္ဒ ဣဒ္ဓိပါဒ်ကို ပွားများပြီး၏… ဝီရိယ ဣဒ္ဓိပါဒ်… စိတ္တ ဣဒ္ဓိပါဒ်… ဝီမံသ ဣဒ္ဓိပါဒ်ကို", *BHAVITA))
P("bodhisatto issariyakāmakārikāhetu dukkarakārikaṃ akāsi", bb(f"{BSI} {P11.DKK}ကို", "ပြုခဲ့"))
P("bodhisatto issariyakāmakārikāhetu aññaṃ satthāraṃ uddisi", bb(f"{BSI} အခြား ဆရာကို", "ကိုးကွယ်ခဲ့"))
P("bodhisatto issariyakāmakārikāhetu aparantapaṃ akāsi", bb(f"{BSI} အခြား ပြင်းထန်သော အကျင့်ကို ⟦b⟧", "ကျင့်ခဲ့"))
P("aññaṃ satthāraṃ uddisi", bb("အခြား ဆရာကို", "ကိုးကွယ်ခဲ့"))
BR_X["[amaraṃ tapaṃ (saṃ. ni. 1.137)]"] = f"[{F.PATHA} ({F.REF['saṃ. ni.']} 1.137): amaraṃ tapaṃ]"
_FV = F.FINAL.seg("1", "^1-1105")[2][0]
TEN = ["လောကသည် ထာဝရ တည်မြဲသည်", "လောကသည် ထာဝရ မတည်မြဲ", "လောကသည် အဆုံး ရှိသည်", "လောကသည် အဆုံး မရှိ",
       "အသက်သည် ကိုယ်ခန္ဓာပင် ဖြစ်သည်", "အသက်နှင့် ကိုယ်ခန္ဓာသည် တခြားစီ ဖြစ်သည်", f"{BUDDHA}သည် သေပြီးနောက် ရှိသည်",
       f"{BUDDHA}သည် သေပြီးနောက် မရှိ", f"{BUDDHA}သည် သေပြီးနောက် ရှိသည်လည်း ဖြစ် မရှိသည်လည်း ဖြစ်သည်",
       f"{BUDDHA}သည် သေပြီးနောက် ရှိသည်လည်း မဟုတ် မရှိသည်လည်း မဟုတ်"]
assert all(x + "ဟူ၍ဖြစ်စေ" in _FV for x in TEN)
F.WITNESS.setdefault("sassato loko … neva hoti na na hoti tathāgato paraṃ maraṇā (the ten views)", ("1", "^1-1105", TEN[0]))
_HELD = "ဟု ယူဆခဲ့၏"
P("bodhisatto issariyakāmakārikāhetu sassato lokoti paccāgacchi, asassato lokoti… antavā lokoti… anantavā lokoti… taṃ "
  "jīvaṃ taṃ sarīranti… aññaṃ jīvaṃ aññaṃ sarīranti… hoti tathāgato paraṃ maraṇāti… na hoti tathāgato paraṃ "
  "maraṇāti… hoti ca na ca hoti tathāgato paraṃ maraṇāti… neva hoti na na hoti tathāgato paraṃ maraṇāti paccāgacchi",
  bb(f"{BSI} «{TEN[0]}»{_HELD}၊ " + "… ".join(f"«{x}»" for x in TEN[1:-1]) + f"… «{TEN[-1]}»ဟု", "ယူဆခဲ့"))
P("bodhisatto issariyakāmakārikāhetu sassato lokoti paccāgacchi… neva hoti na na hoti tathāgato paraṃ maraṇāti "
  "paccāgacchi", bb(f"{BSI} «{TEN[0]}»{_HELD}… «{TEN[-1]}»ဟု", "ယူဆခဲ့"))
# --- (225) 8. Patirūpakathā
section("(225) 8. Patirūpakathā", f"(225) 8. အတုအယောင်အကြောင်း {KATHA}")
section("Patirūpakathā", f"အတုအယောင်အကြောင်း {KATHA}")
PTR = {"rāgo": ("ရာဂ", "ako"), "doso": ("ဒေါသ", "ako"), "moho": ("မောဟ", "ako"), "kileso": (KIL, "ako"),
       "phasso": ("တွေ့ထိမှု", "ako"), "vedanā": ("ခံစားမှု", "ikā"), "saññā": ("မှတ်သိမှု", "ikā"),
       "cetanā": ("စေ့ဆော်မှု", "ikā"), "cittaṃ": ("စိတ်", "akaṃ"), "saddhā": ("ယုံကြည်မှု", "ikā"),
       "vīriyaṃ": ("ဝီရိယ", "akaṃ"), "sati": ("သတိ", "ikā"), "samādhi": ("သမာဓိ", "ako"), "paññā": ("ပညာ", "ikā")}
for _k, (_m, _e) in PTR.items():
    _st = _k[:-2] if _k.endswith("ṃ") or _k.endswith("o") else _k
    _st = {"rāgo": "rāga", "doso": "dosa", "moho": "moha", "kileso": "kilesa", "phasso": "phassa", "cittaṃ": "citta",
           "vīriyaṃ": "vīriya", "samādhi": "samādhi"}.get(_k, _k)
    P(f"atthi na {_k} {_st}patirūp{_e}", V(f"{_m} မဟုတ်ဘဲ {_m}နှင့် တူသော အရာ", EXIST))
# --- (226) 9. Aparinipphannakathā
APN = new("aparinipphanna / parinipphanna", ("ပြည့်စုံစွာ မပြီးမြောက်သော အရာ", "ပြည့်စုံစွာ ပြီးမြောက်သော အရာ"))
section("(226) 9. Aparinipphannakathā", f"(226) 9. ပြည့်စုံစွာ မပြီးမြောက်သော အရာအကြောင်း {KATHA}")
section("Aparinipphannakathā", f"ပြည့်စုံစွာ မပြီးမြောက်သော အရာအကြောင်း {KATHA}")
_SIX = {"rūpaṃ": F.RUPA.my, "aññātāvindriyaṃ": F.INDRIYA["aññātāvindriya"].my}
for _k, _m in _SIX.items():
    P(f"{_k} aparinipphannaṃ", V(f"{_m}သည် {APN[0]}"))
    P(f"{_k} na aniccaṃ na saṅkhataṃ na paṭiccasamuppannaṃ na khayadhammaṃ na vayadhammaṃ na virāgadhammaṃ na "
      "nirodhadhammaṃ na vipariṇāmadhammaṃ", V(f"{_m}သည် {ANICCA_NEG}", neg=True))
    P(f"{_k} aniccaṃ saṅkhataṃ paṭiccasamuppannaṃ khayadhammaṃ vayadhammaṃ virāgadhammaṃ nirodhadhammaṃ "
      "vipariṇāmadhammaṃ", V(f"{_m}သည် {ANICCA_POS}"))
    P(f"{_k} aniccaṃ saṅkhataṃ… vipariṇāmadhammaṃ",
      V(f"{_m}သည် {ANICCA8[0]}၊ {ANICCA8[1]}… {ANICCA8[-1]} ရှိသော အရာ"))
    P(f"yadaniccaṃ taṃ dukkhaṃ vuttaṃ bhagavatā – {_k} aniccaṃ",
      Cl(f"«မမြဲသော အရာသည် ဆင်းရဲ၏»ဟု {BUDDHA}", *SAID, post=f" – «{_m}သည် မမြဲ»"))
P("aññātāvindriyaṃ na aniccaṃ… na vipariṇāmadhammaṃ",
  V(f"{_SIX['aññātāvindriyaṃ']}သည် {_NEG8[0]} မဟုတ်… {_NEG8[-1]}", neg=True))
ANCHOR_X["dukkhaṃ"] = "ဆင်းရဲ၏”"
P("dukkhaññeva parinipphannaṃ", V(f"ဆင်းရဲ ဒုက္ခသည်သာ {APN[1]}"))
_N10 = [F.VEDANA.my, F.SANNA.my, F.SANKHARA.my, F.VINNANA.my, F.AYATANA["cakkhāyatana"].my,
        F.AYATANA["dhammāyatana"].my, F.DHATU["cakkhudhātu"].my, F.DHATU["dhammadhātu"].my,
        F.INDRIYA["cakkhundriya"].my, F.INDRIYA["aññātāvindriya"].my]
P("vedanā… saññā… saṅkhārā… viññāṇaṃ… cakkhāyatanaṃ… dhammāyatanaṃ… cakkhudhātu… dhammadhātu… cakkhundriyaṃ… "
  "aññātāvindriyaṃ aparinipphannaṃ", V("… ".join(_N10) + f"သည် {APN[0]}"))
LINES_X[key("Ekādhippāyena methuno dhammo paṭisevitabbo, arahantānaṃ vaṇṇena amanussā methunaṃ dhammaṃ paṭisevanti, "
            "bodhisatto issariyakāmakārikāhetu vinipātaṃ gacchati, gabbhaseyyaṃ okkamati, dukkarakārikaṃ akāsi, "
            "aparantapaṃ akāsi, aññaṃ satthāraṃ uddisi, atthi na rāgo rāgapatirūpako atthi na doso dosapatirūpako "
            "atthi na moho mohapatirūpako atthi na kileso kilesapatirūpako, rūpaṃ aparinipphannaṃ aññātāvindriyaṃ "
            "aparinipphannanti.")] = (
    f"{EKA} {_MET} မှီဝဲရမည်၊ {ARV} {_MET} မှီဝဲကြ၊ {BSI} ပျက်စီးကျရောက်ရာ ဘုံသို့ သွား၊ အမိဝမ်း၌ "
    f"ကိန်းအောင်းခြင်းသို့ သက်ဆင်း၊ {P11.DKK}ကို ပြုခဲ့၊ အခြား ပြင်းထန်သော အကျင့်ကို ကျင့်ခဲ့၊ အခြား ဆရာကို "
    f"ကိုးကွယ်ခဲ့၊ " + " ".join(f"{PTR[k][0]} မဟုတ်ဘဲ {PTR[k][0]}နှင့် တူသော အရာ ရှိ" for k in ("rāgo", "doso", "moho",
                                                                                          "kileso"))
    + f"၊ {F.RUPA.my}သည် {APN[0]}၊ {_SIX['aññātāvindriyaṃ']}သည် {APN[0]}{END}")
LINES_X["Khuddako aḍḍhapaṇṇāsako."] = f"{F.KATHA_NAME['khuddaka']} ငါးဆယ်တစ်ဝက်အစု{END}"
LINES_X[key("Navaṃ, nibbuti, ekādhippāyoti.")] = f"အသစ်၊ ငြိမ်းအေးခြင်း၊ တူညီသော ရည်ရွယ်ချက်{END}"
LINES_X["Paṇṇāsakuddānaṃ –"] = f"{PANNASA}တို့၏ အကျဉ်းချုပ် –"
LINES_X[key("Mahāniyāmo, anusayā, niggaho, khuddakapañcamo;")] = (
    f"{F.KATHA_NAME['mahā']} အစု၊ သေချာသော လမ်းကြောင်း၊ {P11.ANUSAYA}တို့၊ {F.KATHA_NAME['niggaha']}၊ {F.ORD_MY[5]} "
    f"{F.KATHA_NAME['khuddaka']} အစု၊")   # harmonise B2: Mahā = Mahāpaṇṇāsako (ch13), niggaho = ch24 heading
W("4", "^4-13", "niyāmaṃ okkamituṃ", "သေချာသော လမ်းကြောင်း")
LINES_X[key("Parappavādamaddanā, suttamūlasamāhitā;")] = (
    "သူတစ်ပါး ဝါဒတို့ကို ချေမှုန်းတတ်သော၊ သုတ္တန်ဟူသော အမြစ်၌ ကောင်းစွာ တည်သော၊")
LINES_X[key("Ujjotanā satthusamaye, kathāvatthupakaraṇeti.")] = (
    f"ဆရာ၏ အယူဝါဒ၌ ထွန်းလင်းစေတတ်သော “{F.TITLE}” ကျမ်း၌{END}")
LINES_X["Pañcattiṃsabhāṇavāraṃ"] = (W("1", "^1-57", "Paṭhamabhāṇavāro", "ရွတ်ဖတ်ရန် အပိုင်း") + " သုံးဆယ့်ငါးပိုင်း")
# harmonise B7: bhāṇavāra = pi-1 «ရွတ်ဖတ်ရန် အပိုင်း» (was «ရွတ်ဆိုရန် …»); no full stop (the Pāli has none)
COLO_X["Kathāvatthupakaraṇaṃ niṭṭhitaṃ"] = F.BOOK_END


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


install()
SLIP = SLIP_X   # (Pāli line without ID, [sentence keys], {sentence index: bracket count after it}) for lines the
                 # sentence cutter cannot cut (unbalanced quotes in the source); built after install()


def slip_lines():
    for line, sents, brs in SLIP:
        out, n = [], 0
        for i, u in enumerate(sents):
            my = F.unit_my(u)
            for _ in range(brs.get(i, 0)):
                my = my[:-1] + f" ⟦{n}⟧" + my[-1]
                n += 1
            out.append(my)
        F.LINES[key(line)] = " ".join(out)


slip_lines()


def run(name, misses=False):
    return P6.run(name, misses)


def main():
    args = sys.argv[1:]
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
