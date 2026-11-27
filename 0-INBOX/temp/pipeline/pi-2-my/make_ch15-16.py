"""Burmese zero-shot of pi-2 (Vibhaṅga, «ခွဲခြမ်းစိတ်ဖြာခြင်း»): 15-patisambhidavibhango, 16-nanavibhango.

usage: python3 -I -X utf8 make_ch15-16.py [chapter ...]
Model: make_sample.py (approved pi-2 sample). Every line is generated from the Pāli by translate_line(): headings and
colophons from tables, the pañhāpucchaka of ch. 15 through the sample engine my2_formulas.clauses_my() (subjects added
in memory), everything else clause by clause through the frames (FRAMES) and the phrase tables (FIX) of this file. The
cittuppāda openings are the FINAL pi-1 Burmese, looked up sentence by sentence in the pi-1 rails text (P1_OPEN) or built
from the pi-1 tables where pi-1 has no identical opening. A clause no frame or table matches stops the run
(my2_formulas.Miss): nothing is guessed. A chapter is written only when every line passed; on a stop the lines that
passed are counted, nothing is written.
my2_formulas.py, my2-zeroshot-terms.md and pi-1-my/ are read only; every new string is logged in notes-ch15-16.md.
"""
import pathlib
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import my2_formulas as F  # noqa: E402

ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-2_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-2-burmese-plain-zeroshot_split_chapters"
NAMES_OUT = ["15-patisambhidavibhango.md", "16-nanavibhango.md"]

P1, T, Miss = F.P1, F.T, F.Miss
C, END, PE, DH, DHP = F.C, F.END, F.PE, F.DH, F.DHP
COP = F.COP
HOTI = P1.CU_HOTI["sg"]                       # ရှိသည်
TASMIM = P1.TASMIM                            # ထိုအချိန်၌
TI, TIPI = F.TI, F.TIPI                       # ဟု / ဟုလည်းကောင်း
HUSI = "ဟူသည်"                                # «X»ti (Y) : «X ဟူသည် Y» (pi-1 ^1-1382 «Khaye ñāṇanti – …»)
NANA = "ဉာဏ်"                                 # ñāṇa (pi-1)
PANNA = P1.SYN["paññā"]                       # ပညာ
KNOW = "သိသော"                                # X-e ñāṇaṃ = «Xကို သိသော ဉာဏ်» (pi-1 Dukkhe ñāṇaṃ, khaye ñāṇaṃ)
CL = P1.CL                                    # ပါး
NUM = P1.NUM


def cnt(x, stem):
    return P1.count_my(x, stem)


def low(s):
    return s[0].lower() + s[1:]


def ci(word):
    """Regex for a Pāli word whose first letter may be upper or lower case."""
    return f"[{word[0].upper()}{word[0]}]" + re.escape(word[1:])


def alt(keys):
    return "(?:" + "|".join(ci(k) for k in sorted(keys, key=len, reverse=True)) + ")"


# ===================================================================================== vocabulary (new in ch. 15-16)
PATI = f"ပိုင်းခြားသိသော {NANA}"             # paṭisambhidā (analytical knowledge)
ATTHA = "အကျိုးအနက်"                         # attha (meaning / result) in the paṭisambhidā chapter
DHAMMA_T = "တရား"                            # dhamma (cause / the teaching) in dhammapaṭisambhidā (pi-1 «တရား» sense)
PATIBHANA = "ဉာဏ်ပေါ်မှု"                      # paṭibhāna (ready insight)
PS = {
    "atthapaṭisambhidā": f"{ATTHA}ကို {PATI}",
    "dhammapaṭisambhidā": f"{DHAMMA_T}ကို {PATI}",
    "niruttipaṭisambhidā": f"{P1.NAMES.get('nirutti', 'စကားဖြင့် ဖော်ပြမှု')}ကို {PATI}",
    "paṭibhānapaṭisambhidā": f"{PATIBHANA}ကို {PATI}",
}
NIRUTTI = "စကားဖြင့် ဖော်ပြမှု"               # nirutti (pi-1 termbase)
PS["niruttipaṭisambhidā"] = f"{NIRUTTI}ကို {PATI}"
PSG = {     # counted groups (subjects of the pañhāpucchaka too)
    "catasso paṭisambhidā": cnt(PATI, "catu"), "tisso paṭisambhidā": cnt(PATI, "ti"),
    "dve paṭisambhidā": cnt(PATI, "dvi"),
}
TATRA = "ထိုအရာ၌"                             # tatra
ABHILAPA = "ခေါ်ဆိုခြင်း"                      # abhilāpa (pi-1 abhilāpo)
# objects of «X ñāṇaṃ»: Pāli locative -> Burmese object (before «ကို သိသော ဉာဏ်»)
DUKKHA_N = "ဒုက္ခ"
TRUTH = {   # pi-1 ^1-? moho list: Dukkhe aññāṇaṃ … = «ဒုက္ခကို မသိခြင်း၊ ဒုက္ခ ဖြစ်ပေါ်ခြင်းကို …»
    "": DUKKHA_N, "samudaye": "ဖြစ်ပေါ်ခြင်း", "nirodhe": "ချုပ်ငြိမ်းခြင်း",
    "nirodhagāminiyā paṭipadāya": "ချုပ်ငြိမ်းရာသို့ ရောက်စေသော ကျင့်စဉ်",
}
PS_LINK = {  # links of dependent origination (pi-1 ^1-1343)
    "jarāmaraṇa": "အိုခြင်းနှင့် သေခြင်း", "jāti": "မွေးဖွားခြင်း", "bhava": "ဘဝ", "upādāna": "စွဲလမ်းမှု",
    "taṇhā": "တပ်မက်မှု", "vedanā": P1.FEEL, "phassa": P1.PHASSA, "saḷāyatana": "အာရုံခံ နယ်ပယ် ခြောက်ပါး",
    "nāmarūpa": "စိတ်ပိုင်းနှင့် ရုပ်ပိုင်း", "viññāṇa": P1.VINNANA, "saṅkhārā": F.nmy("saṅkhārā"),
    "avijjā": "အမှန်ကို မသိမှု",
}
LOC = {     # locative forms of the links
    "jarāmaraṇe": "jarāmaraṇa", "jātiyā": "jāti", "bhave": "bhava", "upādāne": "upādāna", "taṇhāya": "taṇhā",
    "vedanāya": "vedanā", "phasse": "phassa", "saḷāyatane": "saḷāyatana", "nāmarūpe": "nāmarūpa",
    "viññāṇe": "viññāṇa", "saṅkhāresu": "saṅkhārā",
}
OBJ = {     # «X ñāṇaṃ»: Pāli X -> Burmese X
    "atthe": ATTHA, "dhamme": DHAMMA_T, "ñāṇesu": f"{NANA}တို့",
    "hetumhi": "အကြောင်းရင်း", "hetuphale": "အကြောင်းရင်း၏ အကျိုး",
    "imesu dhammesu": f"ဤ{DH}တို့", "tesu dhammesu": f"ထို{DH}တို့",
    "tesaṃ vipāke": f"ထို{DH}တို့၏ အကျိုး",
    "tatra dhammaniruttābhilāpe": f"{TATRA} {DHAMMA_T}၏ {NIRUTTI}ကို {ABHILAPA}",
    "paracitte": "အခြားသူ၏ စိတ်", "iddhividhe": "တန်ခိုး အမျိုးမျိုး",          # ch. 16
}
_TRUTH_STEM = {"dukkha": DUKKHA_N}
_TRUTH_STEM.update({k: v for k, v in PS_LINK.items()})
for _st, _sm in _TRUTH_STEM.items():
    _loc = {"dukkha": "dukkhe", "jāti": "jātiyā", "taṇhā": "taṇhāya", "vedanā": "vedanāya",
            "saṅkhārā": "saṅkhāresu"}.get(_st, _st[:-1] + "e")
    OBJ[_loc] = _sm
    _b = "saṅkhāra" if _st == "saṅkhārā" else _st
    OBJ[_b + "samudaye"] = f"{_sm} {TRUTH['samudaye']}"
    OBJ[_b + "nirodhe"] = f"{_sm} {TRUTH['nirodhe']}"
    OBJ[_b + "nirodhagāminiyā paṭipadāya"] = f"{_sm} {TRUTH['nirodhagāminiyā paṭipadāya']}"


def obj_nana(p):
    k = low(p)
    if k not in OBJ:
        raise Miss("ñāṇa object: " + p)
    return f"{OBJ[k]}ကို {KNOW} {NANA}"


# ===================================================================================== headings and colophons
VARA = P1.VARA
HEAD = dict(P1.HEAD)
HEAD.update(F.HEAD)
HEAD.update({
    "Paṭisambhidāvibhaṅgo": f"{PATI}များကို {F.TITLE}",
    "Ñāṇavibhaṅgo": f"{NANA}ကို {F.TITLE}",
    "Saṅgahavāro": f"အကျဉ်းချုပ် {VARA}",
    "Saccavāro": f"သစ္စာအလိုက် {VARA}",
    "Hetuvāro": f"အကြောင်းရင်းအလိုက် {VARA}",
    "Dhammavāro": f"{DH}အလိုက် {VARA}",
    "Paṭiccasamuppādavāro": f"{T['paṭiccasamuppādo'] if 'paṭiccasamuppādo' in T else 'အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်ပုံ'}အလိုက် {VARA}",
    "Pariyattivāro": f"ပရိယတ္တိအလိုက် {VARA}",
    "Kusalavāro": f"{T['kusalā']}အလိုက် {VARA}",
    "Akusalavāro": f"{T['akusalā']}အလိုက် {VARA}",
    "Vipākavāro": f"ကံ၏ အကျိုးအလိုက် {VARA}",
    "Kiriyavāro": f"{P1.KIRIYA} စိတ်အလိုက် {VARA}",
})
HEAD["Paṭiccasamuppādavāro"] = f"အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်ပုံအလိုက် {VARA}"   # pi-1 locked paṭiccasamuppāda
COLO = dict(F.COLO)
COLO.update({
    "Paṭisambhidāvibhaṅgo niṭṭhito": f"“{HEAD['Paṭisambhidāvibhaṅgo']}” {F.NITTHITA}",
    "Ñāṇavibhaṅgo niṭṭhito": f"“{HEAD['Ñāṇavibhaṅgo']}” {F.NITTHITA}",
})
for _k in ("Ekakaṃ", "Dukaṃ", "Tikaṃ", "Catukkaṃ", "Pañcakaṃ", "Chakkaṃ", "Sattakaṃ", "Aṭṭhakaṃ", "Navakaṃ",
           "Dasakaṃ"):
    COLO[_k] = HEAD[_k]

# ===================================================================================== pi-1 sentence lookup
ID_RE = F.ID_RE


def _psplit(l):
    l = ID_RE.sub("", l)
    l = re.sub(r"\[[^\]]*\]", lambda m: m[0].replace(". ", ".\x00"), l)
    return [s.replace("\x00", " ") for s in re.split(r"(?<=[.?])(?:\"|”)? (?=\S)", l) if s]


def _bsplit(l):
    return [s for s in re.split(r"(?<=။) ", ID_RE.sub("", l)) if s]


P1_SENT = []          # (Pāli sentence, Burmese sentence) of the final pi-1 text
for _p in sorted(F.P1_PALI.glob("*.md")):
    _pl = _p.read_text(encoding="utf-8-sig").split("\n")
    _bl = (F.P1_RAILS / _p.name).read_text(encoding="utf-8").split("\n")
    for _x, _y in zip(_pl, _bl):
        if not _x.strip() or _x.startswith("#"):
            continue
        _a, _b = _psplit(_x), _bsplit(_y)
        if len(_a) == len(_b):
            P1_SENT += list(zip(_a, _b))

CUT = f"{P1.YASMIM}{C} {TASMIM}"               # «… အချိန်၌၊ ထိုအချိန်၌» (end of a pi-1 opening)
CUT2 = f"{P1.YASMIM} {TASMIM}"                 # the same without the comma (pi-1 2-05 kiriya arūpa)


def _norm(s):
    return s.replace(" …pe…", "…pe…")


def p1_open(o):
    """Final pi-1 Burmese of the opening «Yasmiṃ samaye … / Tasseva …» (up to «… အချိန်၌»), or None."""
    o = _norm(o)
    for s, t in P1_SENT:
        s = _norm(s)
        if s.startswith(o + ", tasmiṃ samaye") or s.startswith(o + " tasmiṃ samaye"):
            for cut in (CUT, CUT2):
                if cut in t:
                    return t[:t.index(cut) + len(P1.YASMIM)]
    return None


# ===================================================================================== cittuppāda openings (ch. 15)
OBJ_VA = P1.ARAMMANA_VA                        # ကို အာရုံပြု၍ဖြစ်စေ
YAM_YAM = P1.YAM_YAM
UPP = P1.UPPANNA                               # ဖြစ်ပေါ်ပြီးသော
YAS = P1.YASMIM                                # အချိန်၌
ADV = P1.QUAL_ADV["sasaṅkhārena"]             # တိုက်တွန်းမှုဖြင့်
CQUAL = dict(P1.QUAL)
CQUAL.update({   # the akusala qualifiers (pi-1 2-04 final)
    "diṭṭhigatasampayuttaṃ": P1.DITTHIGATA + P1.SAMP, "diṭṭhigatavippayuttaṃ": P1.DITTHIGATA + P1.VIPP,
    "domanassasahagataṃ": "စိတ်ဆင်းရဲမှု" + P1.TOGETHER, "paṭighasampayuttaṃ": P1.PATIGHA_AV + P1.SAMP,
    "vicikicchāsampayuttaṃ": P1.VICIKICCHA + P1.SAMP, "uddhaccasampayuttaṃ": P1.UDDHACCA + P1.SAMP,
})
for _k in list(CQUAL):
    CQUAL[_k[:-2] + "ā"] = CQUAL[_k]           # feminine forms (manoviññāṇadhātu …)
ARAM = {}
for _k, _v in P1.ARAMMANA.items():
    ARAM[_k] = _v
    ARAM[_k[:-2] + "ā"] = _v
CITTA = {"kāmāvacaraṃ kusalaṃ cittaṃ": P1.CITTA_KIND["kāmāvacaraṃ kusalaṃ cittaṃ"],
         "akusalaṃ cittaṃ": T["akusalā"] + P1.MIND}
VIP_MANO = f"{T['vipākā']} {P1.NAMES['manoviññāṇadhātu']}"     # vipākā manoviññāṇadhātu
VIP_MANODH = f"{T['vipākā']} {P1.MANO} ဓာတ်"                    # vipākā manodhātu
KIR_ATTR = P1.KIRIYA_ATTR


def _objs(text):
    """«rūpārammaṇaṃ vā…pe… dhammārammaṇaṃ vā[ yaṃ yaṃ vā panārabbha]» -> Burmese (pi-1 r_open)."""
    yy = text.endswith(" yaṃ yaṃ vā panārabbha")
    text = text.removesuffix(" yaṃ yaṃ vā panārabbha")
    objs = re.findall(r"(\S+ārammaṇ(?:aṃ|ā)) vā(…pe…)?", text)
    if "".join(o + " vā" + (pe + " " if pe else " ") for o, pe in objs).rstrip() != text.rstrip():
        raise Miss("objects: " + text)
    s = ""
    for i, (o, pe) in enumerate(objs):
        s += ARAM[o] + OBJ_VA
        if i < len(objs) - 1:
            s += (PE + " ") if pe else (C + " ")
        elif pe:
            raise Miss("objects end with pe: " + text)
    if yy:
        s += f"{C} {YAM_YAM}"
    return s


def _quals(seq):
    """«Q1 Q2 [sasaṅkhārena]» -> «Q1၊ Q2[ တိုက်တွန်းမှုဖြင့်]»."""
    ws = seq.split(" ")
    out, adv = [], ""
    for w in ws:
        if w == "sasaṅkhārena":
            adv = " " + ADV
        elif w in CQUAL:
            out.append(CQUAL[w])
        else:
            raise Miss("qualifier: " + w)
    return f"{C} ".join(out) + adv


def r_open_multi(m):
    """«Yasmiṃ samaye KIND uppannaṃ hoti Q…pe… Q…pe… Q OBJS» (several cittas in one). Consistency pass: the order of
    the pi-1 single opening (r_open_single) and of ch14 open_citta: «OBJS Q… Q… Q KIND-သည် [ADV] ဖြစ်ပေါ်ပြီးသော
    အချိန်၌» (a final «sasaṅkhārena» after «KIND-သည်»)."""
    kind = CITTA[m["k"]]
    qs = [_quals(p) for p in m["q"].split("…pe… ")]
    adv = ""
    if qs[-1].endswith(" " + ADV):
        qs[-1], adv = qs[-1][:-len(ADV) - 1], ADV + " "
    return f"{_objs(m['o'])} " + f"{PE} ".join(qs) + f" {kind}သည် {adv}{UPP} {YAS}"


def r_open_single(m):
    """«Yasmiṃ samaye KIND uppannaṃ hoti Q OBJS» : «OBJS Q KIND-သည် [ADV] ဖြစ်ပေါ်ပြီးသော အချိန်၌» (pi-1 r_open)."""
    q = _quals(m["q"])
    adv = ""
    if q.endswith(" " + ADV):
        q, adv = q[:-len(ADV) - 1], ADV + " "
    return f"{_objs(m['o'])} {q} {CITTA[m['k']]}သည် {adv}{UPP} {YAS}"


def opening(o):
    """Any opening: pi-1 first, then the frames above, then FIX_OPEN."""
    r = p1_open(o)
    if r:
        return r
    if o in FIX_OPEN:
        return FIX_OPEN[o]
    qa = r"(?:" + "|".join(re.escape(k) for k in sorted(CQUAL, key=len, reverse=True)) + r"|sasaṅkhārena)"
    m = re.fullmatch(r"Yasmiṃ samaye (?P<k>kāmāvacaraṃ kusalaṃ cittaṃ|akusalaṃ cittaṃ) uppannaṃ hoti "
                     r"(?P<q>" + qa + r"(?: " + qa + r")*) (?P<o>\S+ārammaṇaṃ vā.*)", o)
    if m:
        return r_open_single(m)
    m = re.fullmatch(r"Yasmiṃ samaye (?P<k>kāmāvacaraṃ kusalaṃ cittaṃ|akusalaṃ cittaṃ) uppannaṃ hoti "
                     r"(?P<q>" + qa + r"(?: " + qa + r")*(?:…pe… " + qa + r"(?: " + qa + r")*)+) "
                     r"(?P<o>\S+ārammaṇaṃ vā.*)", o)
    if m:
        return r_open_multi(m)
    raise Miss("opening: " + o[:120])


def _p1o(o):
    r = p1_open(o)
    if not r:
        raise SystemExit("pi-1 opening not found: " + o)
    return r


# openings pi-1 has not got verbatim, built from pi-1 pieces
_AKV = "အကုသိုလ်ကံကို ပြုခဲ့၍ ဆည်းပူးခဲ့သောကြောင့်"       # akusalassa kammassa katattā upacitattā (pi-1 2-05)
_OBJ5 = _objs("rūpārammaṇā vā…pe… phoṭṭhabbārammaṇā vā")
_OBJ6Y = _objs("rūpārammaṇā vā…pe… dhammārammaṇā vā yaṃ yaṃ vā panārabbha")
_UPE = CQUAL["upekkhāsahagatā"]
_SOM = CQUAL["somanassasahagatā"]
_MANO_VIN = P1.NAMES["manoviññāṇadhātu"]
_MANODH = f"{P1.MANO} ဓာတ်"
_LOKV = _p1o("Tasseva lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ vivicceva kāmehi…pe… paṭhamaṃ "
             "jhānaṃ upasampajja viharati dukkhapaṭipadaṃ dandhābhiññaṃ suññataṃ")
_KIR_RUPA = _p1o("Yasmiṃ samaye rūpāvacaraṃ jhānaṃ bhāveti kiriyaṃ neva kusalaṃ nākusalaṃ na ca kammavipākaṃ "
                 "diṭṭhadhammasukhavihāraṃ vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja viharati pathavīkasiṇaṃ")
_ARUPA_NEVA = _p1o("Yasmiṃ samaye arūpūpapattiyā maggaṃ bhāveti sabbaso ākiñcaññāyatanaṃ samatikkamma "
                   "nevasaññānāsaññāyatanasaññāsahagataṃ sukhassa ca pahānā…pe… catutthaṃ jhānaṃ upasampajja viharati")
_MAHAKIR = _p1o("Yasmiṃ samaye manoviññāṇadhātu uppannā hoti kiriyā neva kusalā nākusalā na ca kammavipākā "
                "somanassasahagatā ñāṇasampayuttā…pe… somanassasahagatā ñāṇasampayuttā sasaṅkhārena…pe… "
                "somanassasahagatā ñāṇavippayuttā…pe… somanassasahagatā ñāṇavippayuttā sasaṅkhārena…pe… "
                "upekkhāsahagatā ñāṇasampayuttā…pe… upekkhāsahagatā ñāṇasampayuttā sasaṅkhārena…pe… "
                "upekkhāsahagatā ñāṇavippayuttā…pe… upekkhāsahagatā ñāṇavippayuttā sasaṅkhārena rūpārammaṇā vā…pe… "
                "dhammārammaṇā vā yaṃ yaṃ vā panārabbha")
_RUPA_BH = T["rūpāvacarā"]
_ARUPA_BH = T["arūpāvacarā"]
_DDSV = "မျက်မှောက်ဘဝ၌ပင် သာယာစွာ နေထိုင်ရန် ဖြစ်သော"   # diṭṭhadhammasukhavihāraṃ (pi-1 2-05 ^1-577)
assert _DDSV in _KIR_RUPA
_ARUPA_TAIL = _ARUPA_NEVA.split(f"{P1.JH_BHAVETI}{C} ", 1)[1]    # «ဘာမျှ မရှိသော နယ်ပယ်ကို …ဝင်စား၍ နေသော အချိန်၌»
FIX_OPEN = {
    # 2-15 ^2-741: as pi-1 2-05 ^1-556 (pi-1 has «gandhārammaṇaṃ …pe…» with a space)
    # 2-15 ^2-742: akusala-vipāka manodhātu …pe… manoviññāṇadhātu
    "Yasmiṃ samaye akusalassa kammassa katattā upacitattā vipākā manodhātu uppannā hoti upekkhāsahagatā "
    "rūpārammaṇā vā…pe… phoṭṭhabbārammaṇā vā…pe… manoviññāṇadhātu uppannā hoti upekkhāsahagatā rūpārammaṇā vā…pe… "
    "dhammārammaṇā vā yaṃ yaṃ vā panārabbha":
        f"{_AKV} {_OBJ5} {_UPE} {VIP_MANODH}သည် {UPP}{PE} {_OBJ6Y} {_UPE} {VIP_MANO}သည် {UPP} {YAS}",
    # 2-15 ^2-744: kiriya manoviññāṇadhātu somanassa …pe… upekkhā
    "Yasmiṃ samaye manoviññāṇadhātu uppannā hoti kiriyā neva kusalā nākusalā na ca kammavipākā somanassasahagatā "
    "rūpārammaṇā vā…pe… dhammārammaṇā vā…pe… manoviññāṇadhātu uppannā hoti kiriyā neva kusalā nākusalā na ca "
    "kammavipākā upekkhāsahagatā rūpārammaṇā vā…pe… dhammārammaṇā vā yaṃ yaṃ vā panārabbha":
        f"{_objs('rūpārammaṇā vā…pe… dhammārammaṇā vā')} {KIR_ATTR}{C} {_SOM} {_MANO_VIN}သည် {UPP}{PE} "
        f"{_OBJ6Y} {KIR_ATTR}{C} {_UPE} {_MANO_VIN}သည် {UPP} {YAS}",
    # 2-15 ^2-740: lokuttara vipāka of the kamma (pi-1 has «… kusalassa jhānassa …»)
    "Tasseva lokuttarassa kusalassa kammassa katattā bhāvitattā vipākaṃ vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ "
    "upasampajja viharati dukkhapaṭipadaṃ dandhābhiññaṃ suññataṃ":
        _LOKV.replace(f"{T['lokuttarā']} {T['kusalā']} {P1.JHANA}ကိုပင်", f"{T['lokuttarā']} {T['kusalā']}ကံကိုပင်"),
    # 2-15 ^2-745: the eight great kiriya cittas …pe… rūpāvacara jhāna …pe… arūpāvacara jhāna
    "Yasmiṃ samaye manoviññāṇadhātu uppannā hoti kiriyā neva kusalā nākusalā na ca kammavipākā somanassasahagatā "
    "ñāṇasampayuttā…pe… somanassasahagatā ñāṇasampayuttā sasaṅkhārena…pe… somanassasahagatā ñāṇavippayuttā…pe… "
    "somanassasahagatā ñāṇavippayuttā sasaṅkhārena…pe… upekkhāsahagatā ñāṇasampayuttā…pe… upekkhāsahagatā "
    "ñāṇasampayuttā sasaṅkhārena…pe… upekkhāsahagatā ñāṇavippayuttā…pe… upekkhāsahagatā ñāṇavippayuttā "
    "sasaṅkhārena…pe… rūpāvacaraṃ jhānaṃ bhāveti…pe… arūpāvacaraṃ jhānaṃ bhāveti kiriyaṃ neva kusalaṃ nākusalaṃ na "
    "ca kammavipākaṃ diṭṭhadhammasukhavihāraṃ…pe… sabbaso ākiñcaññāyatanaṃ samatikkamma "
    "nevasaññānāsaññāyatanasaññāsahagataṃ sukhassa ca pahānā…pe… catutthaṃ jhānaṃ upasampajja viharati":
        _MAHAKIR.split(f" {_OBJ6Y}")[0]
        + f"{PE} {_RUPA_BH} {P1.JHANA}{P1.JH_BHAVETI}{PE} {KIR_ATTR}{C} {_DDSV} {_ARUPA_BH} {P1.JHANA}"
          f"{P1.JH_BHAVETI}{PE} {_ARUPA_TAIL}",
}
assert _MAHAKIR.count(f" {_OBJ6Y}") == 1

# factor names «X hoti» (pi-1 final)
FACT = dict(P1.NAMES)
FACT.update({"dukkhaṃ": f"{P1.DUKKHA}မှု", "sukhindriyaṃ": F.INDR["sukhindriyaṃ"],
             "dukkhindriyaṃ": F.INDR["dukkhindriyaṃ"]})
IME = {"kusalā": P1.IME_KUSALA, "akusalā": f"ဤ{DHP}သည် {T['akusalā']} {COP[True]}",
       "abyākatā": f"ဤ{DHP}သည် {T['abyākatā']} {DHP} {COP[True]}"}
KATAME = {"kusalā": P1.KATAME_KUSALA, "akusalā": f"{T['akusalā']} {DHP} {P1.CU_Q['pl']}",
          "abyākatā": f"{T['abyākatā']} {DHP} {P1.CU_Q['pl']}"}


# ===================================================================================== the clause engine
SEP = list(F.SEP)
FIX = {}            # exact Pāli clause / sentence -> Burmese (tables of this file)
FRAMES = []         # (regex, function) tried after FIX
HIGH = []           # (regex, function) tried before FIX (filled at the end from FIRST)
STATE = {}
W = r"[\wāīūṃṅñṭḍṇḷ]"
NW = r"(?![\wāīūṃṅñṭḍṇḷ])"
_FIXRE = [None]


def frame(pattern):
    def deco(fn):
        FRAMES.append((re.compile(pattern), fn))
        return fn
    return deco


def fixed(table):
    for k, v in table.items():
        if k in FIX and FIX[k] != v:
            raise SystemExit("FIX conflict: " + k)
        FIX[k] = v


def tr(s):
    """Pāli clause string -> Burmese, clause by clause."""
    if _FIXRE[0] is None:
        _FIXRE[0] = re.compile("|".join(re.escape(k) for k in sorted(FIX, key=len, reverse=True)))
    pos, out = 0, []
    while pos < len(s):
        for p, my in SEP:
            if s.startswith(p, pos):
                out.append(my)
                pos += len(p)
                break
        else:
            hit = None
            for rx, f in HIGH:                 # frames that must win over a shorter FIX entry
                m = rx.match(s, pos)
                if m and m.end() > pos:
                    hit = (m, f(m))
                    break
            if hit:
                out.append(hit[1])
                pos = hit[0].end()
                continue
            m = _FIXRE[0].match(s, pos)
            if m and m.end() > pos:
                out.append(FIX[m[0]])
                pos = m.end()
                continue
            last = None
            for rx, f in FRAMES:
                m = rx.match(s, pos)
                if m and m.end() > pos:
                    try:
                        r = f(m)
                    except Miss as e:          # a frame whose tables do not cover this text: try the next one
                        last, r = e, None
                    if r is None:
                        continue
                    out.append(r)
                    pos = m.end()
                    break
            else:
                raise Miss(f"no frame: {s[pos:pos + 110]}" + (f"  (last: {last})" if last else ""))
    return "".join(out)


LABEL = {"Ka": "က", "Kha": "ခ", "Ga": "ဂ", "Gha": "ဃ", "Ṅa": "င", "Kha-gha": "ခ-ဃ"}


@frame(r"\((?P<n>\d+(?:-\d+)?)?(?:\. )?(?P<l>Ka|Kha|Ga|Gha|Ṅa|Kha-gha)?\)")
def r_label(m):
    if not m["n"] and not m["l"]:
        return None
    if m["n"] and m["l"]:
        return f"({m['n']}. {LABEL[m['l']]})"
    return f"({m['n'] or LABEL[m['l']]})"


# ---------------------------------------------------------------- variant readings and editorial notes
UPARI = "နောက်တွင်လည်း ဤနည်းတူ"                 # evamuparipi (so also below)
PASSA = "ကို ကြည့်ပါ"                          # passa X (see X)
DIGHA = "“ဒီဃနိကာယ်”"                         # dīghanikāye
VARS = {    # bracket -> Burmese (kind, sigla, Pāli text kept in Roman script; notes translated)
    "[paṭibhāṇapaṭisambhidā (syā.) evamuparipi]": f"[{P1.LEKHANA} (Syā.): paṭibhāṇapaṭisambhidā{C} {UPARI}]",
    "[āsavā (sī.) dhātuvibhaṅge pana pāṭhanānattaṃ natthi]":
        f"[{P1.PATHA} (Sī.): āsavā{C} “ဓာတ်များကို {F.TITLE}”၌ကား ပါဌ် ကွဲပြားမှု မရှိ]",
    "[kiñci (sī. ka.)]": f"[{P1.PATHA} (Sī., Ka.): kiñci]",
    "[paricce (sabbattha) passa dīghanikāye]": f"[{P1.PATHA} (Sabbattha): paricce{C} {DIGHA}{PASSA}]",
    "[sammatiñāṇaṃ (syā.) passa dīghanikāye]": f"[{P1.LEKHANA} (Syā.): sammatiñāṇaṃ{C} {DIGHA}{PASSA}]",
    "[anekadhātuṃ nānādhātuṃ lokaṃ (syā.) ma. ni. 1.148]":
        f"[{P1.PATHA} (Syā.): anekadhātuṃ nānādhātuṃ lokaṃ{C} “မဇ္ဈိမနိကာယ်” 1.148]",
    "[abbhaññiṃsu (syā.) evamuparipi]": f"[{P1.LEKHANA} (Syā.): abbhaññiṃsu{C} {UPARI}]",
    "[upariṭṭhime (syā.), upariṭṭhimaṃ (ka.)]":
        f"[{P1.LEKHANA} (Syā.): upariṭṭhime{C} {P1.LEKHANA} (Ka.): upariṭṭhimaṃ]",
    "[cakkavatti (sī. syā.)]": f"[{P1.LEKHANA} (Sī., Syā.): cakkavatti]",
    "[nirayagāminīti (syā.)]": f"[{P1.PATHA} (Syā.): nirayagāminīti]",
    "[tiracchānagāminīti (syā.) evamuparipi. aṭṭhakathā oloketabbā]":
        f"[{P1.PATHA} (Syā.): tiracchānagāminīti{C} {UPARI}{C} အဋ္ဌကထာကို ကြည့်ရမည်]",
    "[sampattiyeva (ka.)]": f"[{P1.LEKHANA} (Ka.): sampattiyeva]",
    "[vipattiyeva (ka.)]": f"[{P1.LEKHANA} (Ka.): vipattiyeva]",
}


@frame(r"\[[^\]]+\]")
def r_var(m):
    if m[0] not in VARS:
        raise Miss("variant: " + m[0])
    return VARS[m[0]]


@frame(r"[Tt]attha katam(?P<e>o|ā|aṃ|e|āni) (?P<x>[^?]+)(?=\?)")
def r_tattha(m):
    """«Tattha katamā X?» = «ထိုတို့အနက် X ဟူသည် အဘယ်နည်း» (sample; plural katame / katamāni / a counted X: …တို့နည်း)."""
    pl = m["e"] in ("e", "āni") or bool(re.match(r"(?:catasso|cattāri|sattasattati|catūsu|navasu|chasu) ", m["x"]))
    return f"ထိုတို့အနက် {tr(m['x'])} {HUSI} အဘယ်{'တို့' if pl else ''}နည်း"


# ---------------------------------------------------------------- ch. 15: the paṭisambhidā frames
PS_ALT = alt(PS)
OBJ_ALT = alt(OBJ)
PSG_ALT = alt(PSG)


@frame(r"(?P<x>" + OBJ_ALT + r") ñāṇaṃ (?P<p>" + PS_ALT + r")" + NW)
def r_obj_ps(m):
    return f"{obj_nana(m['x'])}သည် {PS[low(m['p'])]} {COP[False]}"


@frame(r"(?P<x>" + OBJ_ALT + r") ñāṇaṃ(?=…pe…|,|\.|$)")
def r_obj(m):
    return obj_nana(m["x"])


@frame(r"(?P<g>" + PSG_ALT + r")(?= – )")
def r_psg(m):
    return PSG[low(m["g"])]


@frame(PS_ALT + NW)
def r_ps(m):
    return PS[low(m[0])]


VARO = {low(k): v for k, v in HEAD.items() if k.endswith("vāro")}


@frame(r"Ayaṃ (?P<v>" + alt(VARO) + r")(?=\.)")
def r_ayam_varo(m):
    return f"{P1.CU_DEM['sg']} {VARO[low(m['v'])]} {COP[False]}"


@frame(r"(?P<y>Ye|yamhā) dhammā (?P<te>te dhammā )?(?P<l>jātā bhūtā sañjātā nibbattā abhinibbattā pātubhūtā)")
def r_ye_jata(m):
    items = [F.DEF[F.dkey(w)] for w in m["l"].split(" ")]
    if m["y"] == "Ye":       # «Ye dhammā L» = «L1၊ … သဘောတရားများ ရှိသမျှ» (sample relative frame)
        return f"{C} ".join(items) + f" {DHP} ရှိသမျှ"
    stems = [F.stem(x) for x in items]   # «yamhā dhammā te dhammā L» = «အကြင် သဘောတရားမှ ထိုသဘောတရားများ L ဖြစ်ကြ၏»
    return f"အကြင် {DH}မှ ထို{DHP} " + f"{C} ".join(stems) + " ဖြစ်ကြ၏"


# ---------------------------------------------------------------- ch. 15: the abhidhamma part
@frame(r"Katame dhammā (?P<k>kusalā|akusalā|abyākatā)(?=\?)")
def r_katame(m):
    return KATAME[m["k"]]


@frame(r"(?P<o>(?:Yasmiṃ samaye|Tasseva) .+?)(?=,? tasmiṃ samaye )")
def r_opening(m):
    return opening(m["o"])


@frame(r"tasmiṃ samaye(?= )")
def r_tasmim(m):
    return TASMIM


FACT_ALT = alt(FACT)


@frame(r"(?P<n>" + FACT_ALT + r") hoti" + NW)
def r_fact(m):
    return f"{FACT[low(m['n'])]} {HOTI}"


@frame(r"ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā")
def r_yeva(m):
    return P1.YEVA


@frame(r"[Ii]me dhammā (?P<k>kusalā|akusalā|abyākatā)(?=[.,]|$)")
def r_ime(m):
    return IME[m["k"]]


fixed({
    # pariyattivāra (^2-724)
    "Idha bhikkhu dhammaṃ jānāti – suttaṃ geyyaṃ veyyākaraṇaṃ gāthaṃ udānaṃ itivuttakaṃ jātakaṃ abbhutadhammaṃ "
    "vedallaṃ":
        f"ဤသာသနာတော်၌ ရဟန်းသည် {DHAMMA_T}ကို သိသည် – သုတ်{C} ဂေယျ{C} ဝေယျာကရဏ{C} ဂါထာ{C} ဥဒါန်း{C} ဣတိဝုတ်{C} "
        f"ဇာတ်{C} အဗ္ဘုတဓမ္မ{C} ဝေဒလ္လ",
    'So tassa tasseva bhāsitassa atthaṃ jānāti – "ayaṃ imassa bhāsitassa attho, ayaṃ imassa bhāsitassa attho"ti':
        f"ထိုရဟန်းသည် ထိုထို ဟောပြောချက်၏ {ATTHA}ကိုပင် သိသည် – “ဤသည်မှာ ဤဟောပြောချက်၏ {ATTHA} {COP[False]}{C} "
        f"ဤသည်မှာ ဤဟောပြောချက်၏ {ATTHA} {COP[False]}”{TI}",
    # the abhidhamma part
    "yāya niruttiyā tesaṃ dhammānaṃ paññatti hoti": f"အကြင် {NIRUTTI}ဖြင့် ထို{DH}တို့၏ သတ်မှတ်ချက် ဖြစ်၏",
    "Yāya niruttiyā tesaṃ dhammānaṃ paññatti hoti": f"အကြင် {NIRUTTI}ဖြင့် ထို{DH}တို့၏ သတ်မှတ်ချက် ဖြစ်၏",
    'Yena ñāṇena tāni ñāṇāni jānāti – "imāni ñāṇāni idamatthajotakānī"ti':
        f"အကြင် {NANA}ဖြင့် ထို{NANA}တို့ကို သိ၏ – “ဤ{NANA}တို့သည် ဤ{ATTHA}ကို ထင်ရှားစေကြသည်”{TI}",
    "Tisso paṭisambhidā kāmāvacarakusalato catūsu ñāṇasampayuttesu cittuppādesu, kiriyato catūsu ñāṇasampayuttesu "
    "cittuppādesu uppajjanti":
        f"{PSG['tisso paṭisambhidā']}သည် {T['kāmāvacarā']} {T['kusalā']}ထဲမှ ဉာဏ်{P1.SAMP} စိတ် ဖြစ်ပေါ်မှု "
        f"{NUM['catu']}{CL}တို့၌{C} {P1.KIRIYA} စိတ်ထဲမှ ဉာဏ်{P1.SAMP} စိတ် ဖြစ်ပေါ်မှု {NUM['catu']}{CL}တို့၌ "
        f"ဖြစ်ပေါ်ကြသည်",
    "Atthapaṭisambhidā etesu ceva uppajjati, catūsu maggesu catūsu phalesu ca uppajjati":
        f"{PS['atthapaṭisambhidā']}သည် ဤစိတ် ဖြစ်ပေါ်မှုတို့၌လည်း ဖြစ်ပေါ်သည်{C} {cnt(P1.MAGGA, 'catu')}{C} "
        f"{cnt('ဖိုလ်', 'catu')}တို့၌လည်း ဖြစ်ပေါ်သည်",
})
FIX.update({f"Ayaṃ vuccati \"{k}\"": f"ဤသည်ကို “{v}”{TI} ခေါ်သည်" for k, v in PS.items()})


# ===================================================================================== ch. 15 pañhāpucchaka (sample engine)
for _k, _v in PSG.items():
    F.KH[_k] = (_v, None, True)
F.KH["atthapaṭisambhidā"] = (PS["atthapaṭisambhidā"], None, False)
F.KH["niruttipaṭisambhidā"] = (PS["niruttipaṭisambhidā"], None, False)
F.TERM_IRREG.update({
    "anidassanaapaṭighā": "anidassanaappaṭighā",      # source slip (apaṭighā for appaṭighā)
    "nahetūahetukā": "na hetū ahetukā",
})
for _k in ("ācayagāmino", "apacayagāmino", "nevācayagāmināpacayagāmino", "maggādhipatino", "uppādino"):
    F.TERM_IRREG[_k[:-1] + "ī"] = _k              # feminine «-inī» (paññā, paṭisambhidā)
for _st, _d in P1.FAMILY.items():                  # «āsavavippayuttā sāsavā» written as two words
    for _y in (_d["y"], _d["ny"]):
        F.TERM_IRREG[f"{_st}vippayuttā {_y}"] = f"{_st}vippayutta{_y}"
AMONG_PS = f"{PSG['catasso paṭisambhidā']}တို့အနက်"   # Catunnaṃ paṭisambhidānaṃ (sample AMONG_KH form)


def _pl():
    return F.STATE.get("pl", True)


def x_neg(m):
    """«na T» (free na before a mātikā term, no table entry) = «T သဘောတရား(များ) မဟုတ်(ကြ)»."""
    t = m["t"]
    if "na " + t in T or ("na " + t).replace("upādinn", "upādiṇṇ") in T:
        return None
    pl = _pl()
    return f"{F.term_my(t)} {DHP if pl else DH} မဟုတ်{'ကြ' if pl else ''}"


def x_tipi(m):
    """unquoted «X-tipi, Y-tipi» after «na vattabbā» = «X သဘောတရား(များ)ဟုလည်းကောင်း၊ … ခေါ်ဆို၍ မရ»."""
    if not F.STATE.get("nv"):
        return None
    F.STATE["nv"] = False
    items = m[0].split(", ")
    d = DHP if _pl() else DH
    out = []
    for it in items:
        if it.endswith("tipi"):
            out.append(f"{F.term_my(it[:-4])} {d}{TIPI}")
        elif it.endswith("ti"):
            out.append(f"{F.term_my(it[:-2])} {d}{TI}")
        else:
            raise Miss("tipi: " + it)
    return f"{C} ".join(out) + " " + F.NVATT


def x_nv(m):
    F.STATE["nv"] = True
    return F.SIYA if m["s"] else ""


def x_subj_nv(m):
    name, _, pl = F.kh(m["s"])
    F.STATE["pl"] = pl
    F.STATE["nv"] = True
    return f"{name}သည်"


_TERMW = r"[\wāīūṃṅñṭḍṇḷ]+"
_TIPI = r"(?:na )?" + _TERMW + r"(?: " + _TERMW + r"){0,5}?ti(?:pi)?"
F.EXTRA_RULES[:] = [
    (r"[Cc]atunnaṃ paṭisambhidānaṃ(?= kati)", lambda m: (F.STATE.__setitem__("pl", True), AMONG_PS)[1]),
    (r"Siyā (?P<t>" + _TERMW + r"(?: " + _TERMW + r"){0,6}?)(?=, |\.|;|$)", F.r_siya),
    (r"(?P<s>" + F._alt(F.KH) + r") na vattabb(?:o|ā)(?= " + _TERMW + ")", x_subj_nv),
    (r"(?P<s>[Ss]iyā) [Nn]a vattabb(?:o|ā)(?= " + _TERMW + ")", x_nv),
    (r"(?P<s>)[Nn]a vattabb(?:o|ā) (?=" + _TERMW + ")", x_nv),
    (_TIPI + r"(?:, " + _TIPI + r")*(?=;|\.|$)", x_tipi),
    (r"(?P<t>(?:[^\s,;.]+ ){1,3}?)c[aā]ti(?=,|;|\.|$)",
     lambda m: (f"{F.term_my(m['t'] + 'ca')} {DHP if _pl() else DH}{TI} {F.NVATT}"
                if F.STATE.pop("nv", False) else None)),
    (r"[Nn]a (?P<t>" + _TERMW + r"(?: " + _TERMW + r"){0,4}?)(?=, |\.|;|$)", x_neg),
]
F.rebuild()


def pan_sentences(body):
    body = re.sub(r"\[[^\]]*\]", lambda m: m[0].replace(". ", ".\x00"), body)
    return [s.replace("\x00", " ") for s in re.split(r"(?<=\.) (?=\S)", body)]


def pan_clauses(s):
    F.STATE.clear()
    F.STATE.update({"part": "pan", "pl": True})
    return F.clauses_my(low(s).replace("upādinn", "upādiṇṇ"))


def pan_line(body):
    out = []
    for s in pan_sentences(body):
        brs = re.findall(r" (\[[^\]]+\])", s)
        if not brs:
            out.append(pan_clauses(s))
            continue
        # a variant inside a mātikā term: translate without it, then put the bracket after that term's Burmese
        my = pan_clauses(re.sub(r" \[[^\]]+\]", "", s))
        for m in re.finditer(r" (\[[^\]]+\])", s):
            head = re.split(r", |; ", s[:m.start()])[-1]
            tail = re.split(r", |; |\.", s[m.end():])[0]
            cl = re.sub(r" \[[^\]]+\]", "", head + tail)
            cl = re.sub(r"^(?:\S+ )?(?:siyā )?(?:na vattabb[āo] )?", "", cl) if " ceva " in cl else cl
            cl = re.sub(r"^(?:siyā |na vattabb[āo] )+", "", cl)
            cl = cl[:-2] if cl.endswith("ti") else cl
            term = F.term_my(cl)
            start = m.start() - len(head)
            prefix = re.sub(r" \[[^\]]+\]", "", s[:start]).rstrip(" ,;")
            n = pan_clauses(prefix).count(term) if prefix else 0
            j = -1
            for _ in range(n + 1):
                j = my.find(term, j + 1)
            if j < 0:
                raise Miss("variant term: " + cl)
            k = j + len(term)
            my = my[:k] + " " + VARS[m[1]] + my[k:]
        out.append(my)
    return " ".join(out)


FIX_PAN = {}        # whole pañhāpucchaka sentences the sample engine cannot build (filled below)


# ===================================================================================== ch. 16: Ñāṇavibhaṅga
NV = f"{NANA} အခြေခံ"                         # ñāṇavatthu (pi-1 kilesavatthu = ကိလေသာ အခြေခံ)
PLIST = P1.items_my(P1.list_items("paññā pajānanā…pe… amoho dhammavicayo sammādiṭṭhi")) + " ရှိသမျှ"
TATTHA_PL = f"ထို၌ ရှိသော {PLIST}"            # yā tattha paññā …pe… sammādiṭṭhi (pi-1 ^1-1343)
EVARUPA_PL = f"ဤသို့ သဘောရှိသော {PLIST}"      # yā evarūpā paññā … (pi-1 diṭṭhisampadā)
UPP_PL = f"ဖြစ်ပေါ်သော {PLIST}"                # yā uppajjati paññā …
MAG4, PHA4 = cnt(P1.MAGGA, "catu"), cnt("ဖိုလ်", "catu")
TATHA = "မြတ်စွာဘုရား"                         # tathāgata (pi-1)
TBALA = f"ဘုရားဆိုင်ရာ {P1.BALA}"               # tathāgatabala (the power proper to a Tathāgata)
KNOWS = "သိတော်မူသည်"                         # (tathāgato) pajānāti
YATHA = "ဟုတ်မှန်သည့်အတိုင်း"                   # yathābhūtaṃ
for _k, _n in (("Catukka", "catu"), ("Pañcaka", "pañca"), ("Chakka", "cha"), ("Sattaka", "satta"),
               ("Aṭṭhaka", "aṭṭha"), ("Navaka", "nava"), ("Dasaka", "dasa"), ("Ekaka", "eka"), ("Duka", "dvi"),
               ("Tika", "ti")):
    _base = HEAD[_k + "ṃ"] if _k + "ṃ" in HEAD else HEAD[{"Duka": "Dukaṃ", "Tika": "Tikaṃ"}[_k]]
    HEAD.setdefault(_k + "mātikā", f"{_base} {P1.MATIKA}")
    HEAD.setdefault(_k + "niddeso", f"{_base} အကျယ် {VARA}")
HEAD["Dukamātikā"] = P1.HEAD["Dukamātikā"]
HEAD["Tikamātikā"] = P1.HEAD["Tikamātikā"]

# ---- paññā terms: mātikā terms (pi-1) + the new ones
NEWT = {
    "cintāmayā": "စဉ်းစားခြင်းမှ ဖြစ်သော", "sutamayā": "ကြားနာခြင်းမှ ဖြစ်သော",
    "bhāvanāmayā": f"{P1.BHAV.removesuffix('ဖြင့်')}မှ ဖြစ်သော", "dānamayā": "ပေးလှူခြင်းမှ ဖြစ်သော",
    "sīlamayā": "သီလမှ ဖြစ်သော", "atthajāpikā": "အကျိုးကို ဖြစ်စေတတ်သော", "jāpitatthā": "အကျိုးကို ဖြစ်စေပြီးသော",
    "hānabhāginī": "ဆုတ်ယုတ်ခြင်း၏ အစိတ်အပိုင်း ဖြစ်သော", "ṭhitibhāginī": "တည်တံ့ခြင်း၏ အစိတ်အပိုင်း ဖြစ်သော",
    "visesabhāginī": "ထူးခြားခြင်း၏ အစိတ်အပိုင်း ဖြစ်သော", "nibbedhabhāginī": "ဖောက်ထွင်းခြင်း၏ အစိတ်အပိုင်း ဖြစ်သော",
    "uppādinī": T["uppādino"],
    "dukkhapaṭipadā dandhābhiññā": f"{P1.JH_Q['dukkhapaṭipadaṃ']}{C} {P1.JH_Q['dandhābhiññaṃ']}",
    "dukkhapaṭipadā khippābhiññā": f"{P1.JH_Q['dukkhapaṭipadaṃ']}{C} {P1.JH_Q['khippābhiññaṃ']}",
    "sukhapaṭipadā dandhābhiññā": f"{P1.JH_Q['sukhapaṭipadaṃ']}{C} {P1.JH_Q['dandhābhiññaṃ']}",
    "sukhapaṭipadā khippābhiññā": f"{P1.JH_Q['sukhapaṭipadaṃ']}{C} {P1.JH_Q['khippābhiññaṃ']}",
    "parittā parittārammaṇā": f"{T['parittā']}{C} {T['parittārammaṇā']}",
    "parittā appamāṇārammaṇā": f"{T['parittā']}{C} {T['appamāṇārammaṇā']}",
    "appamāṇā parittārammaṇā": f"{T['appamāṇā']}{C} {T['parittārammaṇā']}",
    "appamāṇā appamāṇārammaṇā": f"{T['appamāṇā']}{C} {T['appamāṇārammaṇā']}",
}
for _k, _v in (("vitakka", P1.VIT), ("vicāra", P1.VIC), ("pīti", "ပီတိ"), ("sukha", f"{P1.SUKHA}မှု"),
               ("upekkhā", "ဥပေက္ခာ")):
    NEWT[_k + "sampayuttā"] = _v + P1.SAMP
    NEWT[_k + "vippayuttā"] = _v + P1.VIPP
NEWT["vitakkavicārasampayuttā"] = f"{P1.VIT}နှင့် {P1.VIC}တို့{P1.SAMP}"
NEWT["vitakkavicāravippayuttā"] = f"{P1.VIT}နှင့် {P1.VIC}တို့{P1.VIPP}"
NEWT["vitakkavippayuttā vicārasampayuttā"] = f"{P1.VIT}{P1.VIPP}{C} {P1.VIC}{P1.SAMP}"
for _st, _d in P1.FAMILY.items():                 # «āsavavippayuttā sāsavā paññā»: both qualifiers of the paññā
    for _y in (_d["y"], _d["ny"]):
        NEWT[f"{_st}vippayuttā {_y}"] = f"{T[_st + 'vippayuttā']}{C} {T[_y]}"
F.TERM_IRREG.update({"anuppādinnupādāniyā": "anupādiṇṇupādāniyā",          # source slip ^2-753 (40)
                     "anuppādinnaanupādāniyā": "anupādiṇṇaanupādāniyā",
                     "ajjhatā": "ajjhattā"})                                    # source slip ^2-753 (62)


def tm(t):
    """Burmese attributive of a paññā term (mātikā term, «na / no» + term, or a new term)."""
    k = low(t).replace("upādinn", "upādiṇṇ").replace("anuppādiṇṇ", "anupādiṇṇ")
    if k in NEWT:
        return NEWT[k]
    try:
        return F.term_my(k.replace("upādiṇṇ", "upādinn") if k.replace("upādiṇṇ", "upādinn") in F.TERM_IRREG else k)
    except Miss:
        pass
    neg = re.fullmatch(r"(na|no) (.+)", k)
    if neg:
        return P1.no_(tm(neg[2]))
    raise Miss("paññā term: " + t)


# ---- locatives (where the paññā occurs): «L1 L2 … paññā» = «L1၊ L2၊ … ၌ ရှိသော ပညာ»
_KA = f"{T['kusalā']} {DH}နှင့် {T['abyākatā']} {DH}"            # kusalābyākata (sample QV form)
_KIRA = f"{P1.KIRIYA}{C} {T['abyākatā']} {DH}"                   # kiriyābyākata
_PLANE = {"kāmāvacara": T["kāmāvacarā"], "rūpāvacara": T["rūpāvacarā"], "arūpāvacara": T["arūpāvacarā"],
          "rūpāvacarārūpāvacara": f"{T['rūpāvacarā']}{C} {T['arūpāvacarā']}"}
LOCT = {
    "tīsu bhūmīsu": f"ဘုံ {NUM['ti']}{CL}၌ ဖြစ်သော", "catūsu bhūmīsu": f"ဘုံ {NUM['catu']}{CL}၌ ဖြစ်သော",
    "kusalābyākate": _KA + "၌", "kusale": f"{T['kusalā']} {DH}၌", "vipāke": f"{T['vipākā']} {DH}၌",
    "kiriyābyākate": _KIRA + "၌",
    "catūsu maggesu": f"{MAG4}တို့၌", "catūsu phalesu": f"{PHA4}တို့၌", "tīsu phalesu": f"{cnt('ဖိုလ်', 'ti')}တို့၌",
    "upariṭṭhime arahattaphale": "အမြင့်ဆုံး ဖြစ်သော အရဟတ္တဖိုလ်၌",
    "adhisīle": "လွန်မြတ်သော သီလ၌", "adhicitte": "လွန်မြတ်သော စိတ်၌", "adhipaññāya": "လွန်မြတ်သော ပညာ၌",
    "chasu abhiññāsu": f"{cnt(P1.ABHINNA, 'cha')}တို့၌",
    "navasu anupubbavihārasamāpattīsu": f"အစဉ်အတိုင်း နေထိုင်ရာ ဈာန် ဝင်စားရာ {NUM['nava']}{CL}တို့၌",
    "dvīsu jhānesu": f"{cnt(P1.JHANA, 'dvi')}တို့၌", "tīsu jhānesu": f"{cnt(P1.JHANA, 'ti')}တို့၌",
}
for _p, _pm in _PLANE.items():
    LOCT[_p + "kusalābyākate"] = f"{_pm} {_KA}၌"
    LOCT[_p + "kusale"] = f"{_pm} {T['kusalā']} {DH}၌"
for _n, _m in (("sotāpatti", "သောတာပတ္တိ"), ("sakadāgāmi", "သကဒါဂါမိ"), ("anāgāmi", "အနာဂါမိ"), ("arahatta", "အရဟတ္တ")):
    LOCT[_n + "magge"] = f"{_m}မဂ်၌"
    LOCT[_n + "phale"] = f"{_m}ဖိုလ်၌"
for _o, _om in P1.ORD.items():
    LOCT[_o + "jjhānasamāpattiyā"] = f"{_om} {P1.JHANA} ဝင်စားရာ၌"
for _a, _am in P1.JH_ARUPA_BASE.items():
    LOCT[_a + "samāpattiyā"] = f"{_am} ဝင်စားရာ၌"
_LOC_ALT = alt(LOCT)
LOC_RE = re.compile(r"(?P<l>" + _LOC_ALT + r"(?:,? " + _LOC_ALT + r")*) paññā" + NW)


def loc_my(s):
    toks = re.findall(_LOC_ALT, s)
    if " ".join(toks) != s.replace(", ", " "):
        raise Miss("locative chain: " + s)
    out, i = [], 0
    while i < len(toks):
        t = low(toks[i])
        if t in ("tīsu bhūmīsu", "catūsu bhūmīsu"):
            out.append(f"{LOCT[t]} {LOCT[low(toks[i + 1])]}")
            i += 2
        else:
            out.append(LOCT[t])
            i += 1
    return f"{C} ".join(out) + " ရှိသော " + PANNA


@frame(r"(?P<v>" + alt(F.VIDHA) + r") ñāṇavatthu(?= –)")
def r_vidha_nv(m):
    return f"{F.VIDHA[low(m['v'])]} {F.LOOK} {NV}"


@frame(r"Evaṃ (?P<v>" + alt(F.VIDHA) + r") ñāṇavatthu(?=\.)")
def r_evam_nv(m):
    return f"{F.EVAM} {F.VIDHA[low(m['v'])]} {F.LOOK} {NV} {COP[False]}"


# identity «A paññā B paññā» (A: locative chain or term) = «A ပညာသည် B ပညာ ဖြစ်သည်»
@frame(r"(?P<a>[^,.?–()\"]+?) paññā (?P<b>[^,.?–()\"]+?) paññā(?=[,.]|$)")
def r_ident(m):
    a = m["a"]
    try:
        subj = loc_my(a)
    except Miss:
        subj = f"{tm(a)} {PANNA}"
    return f"{subj}သည် {tm(m['b'])} {PANNA} {COP[False]}"


@frame(r"(?P<a>[^,.?–()\"]+?) paññā (?P<b>(?:[^,.?–()\" ]+ )?[^,.?–()\" ]+ ñāṇaṃ|[^,.?–()\" ]+ñāṇaṃ)(?=[,.]|$)")
def r_ident_nana(m):
    return f"{loc_my(m['a'])}သည် {tr(m['b'])} {COP[False]}"


@frame(r"(?P<l>" + _LOC_ALT + r"(?:,? " + _LOC_ALT + r")*) paññā(?P<s> (?=siyā ))?" + NW)
def r_loc(m):
    return loc_my(m["l"]) + ("သည် " if m["s"] else "")


@frame(r"(?P<t>(?:(?!paññā)[^,.?–()\"])+?) paññā(?P<x> (?=atthi ))?(?=[,.]| atthi |$| \(| [A-Za-zāīūṃṅñṭḍṇḷ]+ paññā)")
def r_term_panna(m):
    t = m["t"]
    if t.lower().startswith(("atthi ", "sabbāva", "sabbāpi")):
        return None
    return f"{tm(t)} {PANNA}" + ("တွင် " if m["x"] else "")


@frame(r"[Aa]tthi (?P<t>[^,.?–()\" ]+(?: [^,.?–()\" ]+)?)(?=,|$)")
def r_atthi_t(m):
    try:
        return f"{tm(m['t'])} {PANNA} {HOTI}"
    except Miss:
        return None


@frame(r"Sabbāva paññā")
def r_sabbava(m):
    return f"{PANNA} အားလုံးသည်"


@frame(r"siyā (?P<t>[^,.?–()\" ]+)(?=[,.]|$)")
def r_siya_p(m):
    return f"{F.SIYA} {tm(m['t'])} {PANNA} {COP[False]}"


@frame(r"na vattabbā (?P<t>[^,.?–()\" ]+?)ti(?=\.)")
def r_nv_p(m):
    return f"{tm(m['t'])} {PANNA}{TI} {F.NVATT}"


@frame(r"kenaci viññeyyā, kenaci na viññeyyā")
def r_kenaci(m):
    return f"{T['kenaci viññeyyā']} {PANNA} {COP[False]}{C} {T['kenaci na viññeyyā']} {PANNA} {COP[False]}"


# «(X) Pañca viññāṇā na hetū, ahetukā, …» (ekaka list) as the pi-1 Rūpakaṇḍa ^1-594 form
VIN5 = cnt(P1.VINNANA, "pañca")


def _eka_key(it):
    it = it.replace("upādinn", "upādiṇṇ")
    sp = {"na hetū": "na hetu", "nevācayagāmināpacayagāmino": "nevācayagāmināpacayagāmī",
          "nevasekkhanāsekkhā": "nevasekkhanāsekkhaṃ"}
    if it in sp:
        return sp[it]
    return re.sub(r"ā$", "aṃ", it)


def _eka_attr(it):
    try:
        return F.C3["eka_attr"](it)
    except Miss:
        return tm(re.sub(r"aṃ$", "ā", it))


def eka_list(items, eva):
    out = []
    for it in items:
        if eva:
            if it == "uppannaṃ manoviññāṇaviññeyyameva":
                out.append(f"{F.stem(T['uppannā'])}၍ {P1.NAMES['manoviññāṇadhātu'].removesuffix(' ဓာတ်')}ဖြင့် "
                           f"သိနိုင်သည်ပင်")
                continue
            if not it.endswith("meva"):
                raise Miss("eva: " + it)
            it = (it[:-5] + "aṃ") if it.endswith("ameva") else it[:-4]
            it = it.replace("upādinn", "upādiṇṇ")
            if it == "nevācayagāmināpacayagāmi":
                it = "nevācayagāmināpacayagāmī"
            out.append(F.stem(_eka_attr(it)) + "သည်ပင်")
        else:
            out.append(F.stem(_eka_attr(_eka_key(it))))
    if not eva:
        out[-1] += "သည်"
    return f"{C} ".join(out)


@frame(r"pañca viññāṇā (?P<l>na hetū, .+?, aniyyānikā)(?=,$)")
def r_eka5(m):
    return f"{VIN5}သည် " + eka_list(m["l"].split(", "), False)


@frame(r"Pañca viññāṇā (?P<l>na hetumeva, .+?, jarābhibhūtameva)(?=\.)")
def r_eka5_eva(m):
    return f"{VIN5}သည် " + eka_list(m["l"].split(", "), True)


def fixed_ci(table):
    """FIX entries that occur with an upper- or lower-case first letter."""
    t = {}
    for k, v in table.items():
        t[k[0].upper() + k[1:]] = v
        t[k[0].lower() + k[1:]] = v
    fixed(t)


# ---- ekaka mātikā / niddesa (the five consciousnesses)
VAT = "မှီရာ"                                  # vatthu (physical base)
ARM = "အာရုံ"                                  # ārammaṇa
UPP_ = F.stem(T["uppannā"])                    # ဖြစ်ပေါ်ပြီး
PURE = f"ရှေးဦးစွာ {T['uppannā']}"              # purejāta (arisen before)
ASAMB = "မပျက်စီးသေးသော"                       # asambhinna (not yet broken up)
NANA_ = "အသီးသီး ကွဲပြားသော"                    # nānā- (various, different)
SAMN = "ချက်ချင်း နောက်၌"                       # samanantarā (immediately after)
AVAJ = "အာရုံသို့ စိတ်ညွတ်ခြင်း"                 # samannāhāra
SUPA = "အိပ်မက်"
EKQ = {     # the ekaka mātikā items as statements (subject: the five consciousnesses)
    "uppannavatthukā uppannārammaṇā": f"{T['uppannā']} {VAT} ရှိ၍ {T['uppannā']} {ARM} ရှိကြသည်",
    "purejātavatthukā purejātārammaṇā": f"{PURE} {VAT} ရှိ၍ {PURE} {ARM} ရှိကြသည်",
    "ajjhattikavatthukā bāhirārammaṇā": f"{T['ajjhattikā']} {VAT} ရှိ၍ {T['bāhirā']} {ARM} ရှိကြသည်",
    "asambhinnavatthukā asambhinnārammaṇā": f"{ASAMB} {VAT} ရှိ၍ {ASAMB} {ARM} ရှိကြသည်",
    "nānāvatthukā nānārammaṇā": f"{NANA_} {VAT} ရှိ၍ {NANA_} {ARM} ရှိကြသည်",
    "na aññamaññassa gocaravisayaṃ paccanubhonti": "အချင်းချင်း၏ ကျက်စားရာ နယ်ပယ်ကို မခံစားကြ",
    "na asamannāhārā uppajjanti": f"{AVAJ} မရှိဘဲ ဖြစ်ပေါ်ကြသည် မဟုတ်",
    "na amanasikārā uppajjanti": "နှလုံး မသွင်းဘဲ ဖြစ်ပေါ်ကြသည် မဟုတ်",
    "na abbokiṇṇā uppajjanti": "ကြားမပြတ် ဆက်တိုက် ဖြစ်ပေါ်ကြသည် မဟုတ်",
    "na apubbaṃ acarimaṃ uppajjanti": f"ရှေ့ မရှိ{C} နောက် မရှိဘဲ ဖြစ်ပေါ်ကြသည် မဟုတ်",
    "na aññamaññassa samanantarā uppajjanti": f"အချင်းချင်း၏ {SAMN} ဖြစ်ပေါ်ကြသည် မဟုတ်",
    "pañca viññāṇā anābhogā": f"{VIN5}သည် ဆင်ခြင်ခြင်း မရှိကြ",
    "aññatra abhinipātamattā": "အာရုံ ကျရောက်ရုံမျှမှလွဲ၍",
}
PRE5 = {
    "pañcahi viññāṇehi": f"{VIN5}ဖြင့်",
    "pañcannaṃ viññāṇānaṃ samanantarāpi": f"{VIN5}၏ {SAMN}လည်း",
    "pañcannaṃ viññāṇānaṃ samanantarā manodhātuyāpi": f"{VIN5}၏ {SAMN} ဖြစ်သော {P1.MANO} ဓာတ်ဖြင့်လည်း",
}
VP5 = {
    "na kañci dhammaṃ paṭivijānāti": f"မည်သည့် {DH}ကိုမျှ ပိုင်းခြား၍ မသိ",
    "na kañci iriyāpathaṃ kappeti": "မည်သည့် ဣရိယာပုထ်ကိုမျှ မပြုလုပ်",
    "na kāyakammaṃ na vacīkammaṃ paṭṭhapeti":
        f"ကိုယ်ဖြင့် ပြုသော ကံကိုလည်း မဖြစ်စေ{C} နှုတ်ဖြင့် ပြုသော ကံကိုလည်း မဖြစ်စေ",
    "na kusalākusalaṃ dhammaṃ samādiyati": f"{T['kusalā']} {T['akusalā']} {DH}ကို မဆောက်တည်",
    "na samāpajjati na vuṭṭhāti": f"မဝင်စား{C} မထမြောက်",
    "na cavati na uppajjati": f"မသေ{C} မဖြစ်ပေါ်",
    "na supati na paṭibujjhati na supinaṃ passati": f"မအိပ်{C} မနိုး{C} {SUPA} မမြင်",
}
for _p, _pm in PRE5.items():
    for _v, _vm in VP5.items():
        EKQ[f"{_p} {_v}"] = f"{_pm} {_vm}"
EKQ["pañcahi viññāṇehi na kañci [kiñci (sī. ka.)] dhammaṃ paṭivijānāti aññatra abhinipātamattā"] = (
    f"{EKQ['aññatra abhinipātamattā']} {VIN5}ဖြင့် မည်သည့် {VARS['[kiñci (sī. ka.)]']} {DH}ကိုမျှ ပိုင်းခြား၍ မသိ")
fixed_ci(EKQ)
EKQ_TI = {}     # the same items quoted in the niddesa («…ti» = «… ဟူသည်»), final i lengthened before ti
for _k, _v in EKQ.items():
    _kt = re.sub(r"i$", "ī", _k)
    EKQ_TI[_kt + "ti"] = f"{_v} {HUSI}"
EKQ_TI["Pañca viññāṇā uppannavatthukā, uppannārammaṇāti"] = (
    f"{VIN5}သည် {T['uppannā']} {VAT} ရှိ၍{C} {T['uppannā']} {ARM} ရှိကြသည် {HUSI}")
for _a, _b, _m in (("Purejāta", "purejāt", PURE), ("Asambhinna", "asambhinn", ASAMB), ("Nānā", "nān", NANA_)):
    EKQ_TI[f"{_a}vatthukā, {_b}ārammaṇāti"] = f"{_m} {VAT} ရှိ၍{C} {_m} {ARM} ရှိကြသည် {HUSI}"
EKQ_TI["Ajjhattikavatthukā, bāhirārammaṇāti"] = (
    f"{T['ajjhattikā']} {VAT} ရှိ၍{C} {T['bāhirā']} {ARM} ရှိကြသည် {HUSI}")
fixed_ci(EKQ_TI)
_XV = {s: f"{F.SENSE[s]} {P1.VINNANA}" for s in ("cakkhu", "sota", "ghāna", "jivhā", "kāya")}
_XV_ALT = "(?:" + "|".join(_XV) + ")"


@frame(r"(?P<a>[Cc]akkhu|[Ss]ota|[Gg]hāna|[Jj]ivhā|[Kk]āya)viññāṇassa (?P<g>gocaravisayaṃ|gocaravisayampi|"
       r"uppannasamanantarā|uppannasamanantarāpi) (?P<b>" + _XV_ALT + r")viññāṇaṃ na (?P<v>paccanubhoti|uppajjati)")
def r_five_pair(m):
    a, b = _XV[low(m["a"])], _XV[m["b"]]
    pi = "လည်း" if m["g"].endswith("pi") else ""
    if m["v"] == "paccanubhoti":
        return f"{a}၏ ကျက်စားရာ နယ်ပယ်ကို{pi} {b}သည် မခံစား"
    return f"{a} {UPP_}၍ {SAMN}{pi} {b} မဖြစ်ပေါ်"


@frame(r"(?P<a>[Cc]akkhu|[Ss]ota|[Gg]hāna|[Jj]ivhā|[Kk]āya)viññāṇassa(?=…pe…)")
def r_five_gen(m):
    return f"{_XV[low(m['a'])]}၏"


@frame(r"aññaṃ (?P<a>" + _XV_ALT + r")viññāṇassa vatthu ca ārammaṇañca")
def r_five_other(m):
    return f"{_XV[m['a']]}၏ {VAT}နှင့် {ARM}သည် တခြား {COP[False]}"


fixed_ci({
    "uppannasmiṃ vatthusmiṃ uppanne ārammaṇe uppajjanti": f"{T['uppannā']} {VAT}၌{C} {T['uppannā']} {ARM}၌ ဖြစ်ပေါ်ကြသည်",
    "purejātasmiṃ vatthusmiṃ purejāte ārammaṇe uppajjanti": f"{PURE} {VAT}၌{C} {PURE} {ARM}၌ ဖြစ်ပေါ်ကြသည်",
    "pañcannaṃ viññāṇānaṃ vatthu ajjhattikā ārammaṇā bāhirā":
        f"{VIN5}၏ {VAT}တို့သည် {T['ajjhattikā']} ဖြစ်ကြ၍ {ARM}တို့သည် {T['bāhirā']} ဖြစ်ကြသည်",
    "asambhinnasmiṃ vatthusmiṃ asambhinne ārammaṇe uppajjanti": f"{ASAMB} {VAT}၌{C} {ASAMB} {ARM}၌ ဖြစ်ပေါ်ကြသည်",
    "samannāharantassa uppajjanti": "အာရုံသို့ စိတ်ညွတ်သူအား ဖြစ်ပေါ်ကြသည်",
    "manasikarontassa uppajjanti": "နှလုံးသွင်းသူအား ဖြစ်ပေါ်ကြသည်",
    "na paṭipāṭiyā uppajjanti": "အစဉ်အတိုင်း ဆက်တိုက် ဖြစ်ပေါ်ကြသည် မဟုတ်",
    "na ekakkhaṇe uppajjanti": "တစ်ခဏတည်း၌ ဖြစ်ပေါ်ကြသည် မဟုတ်",
    "pañcannaṃ viññāṇānaṃ natthi āvaṭṭanā vā ābhogo vā samannāhāro vā manasikāro vā":
        f"{VIN5}၌ စိတ်ကို လှည့်ဆောင်ခြင်းဖြစ်စေ{C} ဆင်ခြင်ခြင်းဖြစ်စေ{C} {AVAJ}ဖြစ်စေ{C} နှလုံးသွင်းခြင်းဖြစ်စေ မရှိ",
    "aññatra āpātamattā": "အာရုံ ရှေ့သို့ ရောက်လာရုံမျှမှလွဲ၍",
    "gamanaṃ vā ṭhānaṃ vā nisajjaṃ vā seyyaṃ vā":
        f"သွားခြင်းဖြစ်စေ{C} ရပ်ခြင်းဖြစ်စေ{C} ထိုင်ခြင်းဖြစ်စေ{C} လျောင်းခြင်းဖြစ်စေ",
    "yāthāvakavatthuvibhāvanā paññā": f"အရာဝတ္ထုကို {YATHA} ထင်ရှားစေသော {PANNA}",
    "Evaṃ yāthāvakavatthuvibhāvanā paññā": f"{F.EVAM} အရာဝတ္ထုကို {YATHA} ထင်ရှားစေသော {PANNA} {COP[False]}",
})

# ---- the paññā list frames (pi-1 final list)
@frame(r"[Yy]ā (?P<k>tattha|evarūpā|uppajjati) paññā pajānanā ?…pe… amoho dhammavicayo sammādiṭṭhi")
def r_plist(m):
    return {"tattha": TATTHA_PL, "evarūpā": EVARUPA_PL, "uppajjati": UPP_PL}[m["k"]]


@frame(r"(?P<d>[Aa]yaṃ|[Ii]daṃ) vuccati \"(?P<y>[^\"]+)\"")
def r_vuccati_q(m):
    return f"ဤသည်ကို “{tr(m['y'])}”{TI} ခေါ်သည်"


@frame(r"idaṃ vuccati \"(?P<y>[^\".]+)(?=\. )")
def r_vuccati_q_open(m):          # source slip ^2-803: closing quote missing (kept)
    return f"ဤသည်ကို “{tr(m['y'])}{TI} ခေါ်သည်"


@frame(r"(?P<d>[Aa]yaṃ) vuccati (?P<y>[^\".]+)(?=\.)")
def r_vuccati_plain(m):
    return f"ဤသည်ကို {tr(m['y'])}{TI} ခေါ်သည်"


ACC = {     # «X ārabbha» = «Xကို အာရုံပြု၍»
    "dānaṃ": "ပေးလှူခြင်း", "sīlaṃ": "သီလ", "ariyamaggaṃ": f"{T['ariyā'] if 'ariyā' in T else 'အရိယာ'} {P1.MAGGA}",
    "paritte dhamme": f"{T['parittā']} {DH}တို့", "mahaggate dhamme": f"{T['mahaggatā']} {DH}တို့",
    "appamāṇe dhamme": f"{T['appamāṇā']} {DH}တို့", "atīte dhamme": f"{T['atītā']} {DH}တို့",
    "anāgate dhamme": f"{T['anāgatā']} {DH}တို့", "paccuppanne dhamme": f"{T['paccuppannā']} {DH}တို့",
    "ajjhatte dhamme": f"{T['ajjhattā']} {DH}တို့", "bahiddhādhamme": f"{T['bahiddhā']} {DH}တို့",
    "ajjhattabahiddhā dhamme": f"{T['ajjhattabahiddhā']} {DH}တို့",
    "saṅkhāre": PS_LINK["saṅkhārā"],
}
ACC["ariyamaggaṃ"] = f"အရိယာ {P1.MAGGA}"
for _st, _sm in _TRUTH_STEM.items():
    _b = "saṅkhāra" if _st == "saṅkhārā" else _st
    if _st not in ("saṅkhārā",):
        ACC[_st + "ṃ"] = _sm
    ACC[_b + "samudayaṃ"] = f"{_sm} {TRUTH['samudaye']}"
    ACC[_b + "nirodhaṃ"] = f"{_sm} {TRUTH['nirodhe']}"
    ACC[_b + "nirodhagāminiṃ paṭipadaṃ"] = f"{_sm} {TRUTH['nirodhagāminiyā paṭipadāya']}"
ACC_ALT = alt(ACC)


@frame(r"(?P<x>" + ACC_ALT + r") ārabbha")
def r_arabbha(m):
    return f"{ACC[low(m['x'])]}ကို အာရုံပြု၍"


fixed_ci({
    "dānādhigaccha": "ပေးလှူခြင်းဖြင့် ရရှိ၍", "sīlādhigaccha": "သီလဖြင့် ရရှိ၍",
    "pātimokkhasaṃvaraṃ saṃvarantassa": "ပါတိမောက် စောင့်စည်းမှုဖြင့် စောင့်စည်းသူအား",
    "rūpāvacarārūpāvacarasamāpattiṃ samāpajjantassa":
        f"{T['rūpāvacarā']}{C} {T['arūpāvacarā']} ဈာန် ဝင်စားရာကို ဝင်စားသူအား",
    "ariyamaggaṃ adhipatiṃ karitvā": f"အရိယာ {P1.MAGGA}ကို အကြီးအမှူး ပြု၍",
    "kicchena kasirena samādhiṃ uppādentassa": "ခက်ခဲစွာ ပင်ပန်းစွာ သမာဓိကို ဖြစ်စေ၍",
    "akicchena akasirena samādhiṃ uppādentassa": "မခက်ခဲဘဲ မပင်ပန်းဘဲ သမာဓိကို ဖြစ်စေ၍",
    "dandhaṃ taṇṭhānaṃ abhijānantassa": "ထိုအရာကို နှေးကွေးစွာ ထူးကဲစွာ သိသူအား",
    "khippaṃ taṇṭhānaṃ abhijānantassa": "ထိုအရာကို လျင်မြန်စွာ ထူးကဲစွာ သိသူအား",
    "samādhissa na nikāmalābhissa": "သမာဓိကို စိတ်တိုင်းကျ မရဘဲ",
    "samādhissa nikāmalābhissa": "သမာဓိကို စိတ်တိုင်းကျ ရ၍",
    "ārammaṇaṃ thokaṃ pharantassa": "အာရုံကို အနည်းငယ် ပျံ့နှံ့စေသူအား",
    "ārammaṇaṃ vipulaṃ pharantassa": "အာရုံကို ကျယ်ပြန့်စွာ ပျံ့နှံ့စေသူအား",
    "sabbāpi samāpannassa paññā bhāvanāmayā paññā":
        f"ဈာန် ဝင်စားသူ၏ {PANNA} အားလုံးသည် {NEWT['bhāvanāmayā']} {PANNA} {COP[False]}",
    "sabbāpi tatrupāyā paññā upāyakosallaṃ":
        f"ထိုအရာ၌ နည်းလမ်း ဖြစ်သော {PANNA} အားလုံးသည် နည်းလမ်း၌ ကျွမ်းကျင်ခြင်း {COP[False]}",
    "āyakosallaṃ": "တိုးတက်ရာ၌ ကျွမ်းကျင်ခြင်း", "apāyakosallaṃ": "ဆုတ်ယုတ်ရာ၌ ကျွမ်းကျင်ခြင်း",
    "upāyakosallaṃ": "နည်းလမ်း၌ ကျွမ်းကျင်ခြင်း",
})

# ---- duka niddesa specials
_KAM, _RUP, _ARU, _APA = (f"{T[k]} {PANNA}" for k in ("kāmāvacarā", "rūpāvacarā", "arūpāvacarā", "apariyāpannā"))
fixed({
    "Kāmāvacarakusalābyākate paññā kāmāvacarā paññā, rūpāvacarā paññā arūpāvacarā paññā, apariyāpannā paññā na "
    "kāmāvacarā paññā":
        f"{loc_my('kāmāvacarakusalābyākate')}သည် {_KAM} {COP[False]}{C} {_RUP}{C} {_ARU}{C} {_APA}သည် "
        f"{tm('na kāmāvacarā')} {PANNA} {COP[False]}",
    "Rūpāvacarakusalābyākate paññā rūpāvacarā paññā, kāmāvacarā paññā arūpāvacarā paññā apariyāpannā paññā na "
    "rūpāvacarā paññā":
        f"{loc_my('rūpāvacarakusalābyākate')}သည် {_RUP} {COP[False]}{C} {_KAM}{C} {_ARU}{C} {_APA}သည် "
        f"{tm('na rūpāvacarā')} {PANNA} {COP[False]}",
    "Arūpāvacarakusalābyākate paññā arūpāvacarā paññā, kāmāvacarā paññā rūpāvacarā paññā apariyāpannā paññā na "
    "arūpāvacarā paññā":
        f"{loc_my('arūpāvacarakusalābyākate')}သည် {_ARU} {COP[False]}{C} {_KAM}{C} {_RUP}{C} {_APA}သည် "
        f"{tm('na arūpāvacarā')} {PANNA} {COP[False]}",
    "Catūsu bhūmīsu kusale arahato abhiññaṃ uppādentassa samāpattiṃ uppādentassa kiriyābyākate paññā atthajāpikā "
    "paññā":
        f"{LOCT['catūsu bhūmīsu']} {LOCT['kusale']}လည်းကောင်း{C} {P1.ABHINNA}ကို ဖြစ်စေသော၊ ဈာန် ဝင်စားရာကို "
        f"ဖြစ်စေသော ရဟန္တာ၏ {_KIRA}၌လည်းကောင်း ရှိသော {PANNA}သည် {NEWT['atthajāpikā']} {PANNA} {COP[False]}",
    "catūsu bhūmīsu vipāke arahato uppannāya abhiññāya uppannāya samāpattiyā kiriyābyākate paññā jāpitatthā paññā":
        f"{LOCT['catūsu bhūmīsu']} {LOCT['vipāke']}လည်းကောင်း{C} {P1.ABHINNA} {UPP_}သော၊ ဈာန် ဝင်စားရာ "
        f"{UPP_}သော ရဟန္တာ၏ {_KIRA}၌လည်းကောင်း ရှိသော {PANNA}သည် {NEWT['jāpitatthā']} {PANNA} {COP[False]}",
    "upariṭṭhimā [upariṭṭhime (syā.), upariṭṭhimaṃ (ka.)] arahattaphale paññā asekkhā paññā":
        f"အမြင့်ဆုံး ဖြစ်သော {VARS['[upariṭṭhime (syā.), upariṭṭhimaṃ (ka.)]']} အရဟတ္တဖိုလ်၌ ရှိသော {PANNA}သည် "
        f"{tm('asekkhā')} {PANNA} {COP[False]}",
})

# ---- tika niddesa (1): cintāmayā / sutamayā
RUPA_ = F.RUPA
_YOGA = "ပညာရှိတို့ စီမံထားသော"                  # yogavihita (arranged by the wise)
_KHANTI = f"လျော်ညီသော သည်းခံ လက်ခံမှု{C} အယူ{C} နှစ်သက်မှု{C} ကြည်နူးမှု{C} ရှုကြည့်မှု{C} {DH}ကို ဆင်ခြင်၍ လက်ခံမှု"
_KAMMA = "ကံသာ မိမိ၏ ဥစ္စာ ဖြစ်ကြောင်း"            # kammassakata (pi-1)
_SACCA = "သစ္စာနှင့် လျော်ညီသော"                   # saccānulomika (pi-1)
for _h, _hm in (("assutvā", "မကြားနာဘဲ"), ("sutvā", "ကြားနာ၍")):
    FIX[("Yogavihitesu vā kammāyatanesu yogavihitesu vā sippāyatanesu yogavihitesu vā vijjāṭṭhānesu kammassakataṃ vā "
         "saccānulomikaṃ vā rūpaṃ aniccanti vā vedanā…pe… saññā… saṅkhārā… viññāṇaṃ aniccanti vā, yaṃ evarūpiṃ "
         f"anulomikaṃ khantiṃ diṭṭhiṃ ruciṃ mudiṃ pekkhaṃ dhammanijjhānakkhantiṃ parato {_h} paṭilabhati")] = (
        f"{_YOGA} အလုပ်အကိုင်တို့၌ဖြစ်စေ{C} {_YOGA} အတတ်ပညာတို့၌ဖြစ်စေ{C} {_YOGA} အသိပညာ ဌာနတို့၌ဖြစ်စေ "
        f"{_KAMMA}ကိုဖြစ်စေ{C} {_SACCA}အရာကိုဖြစ်စေ{C} {RUPA_}သည် မမြဲဟူ၍ဖြစ်စေ{C} {P1.FEEL}{PE} {P1.SANNA}{PE} "
        f"{PS_LINK['saṅkhārā']}{PE} {P1.VINNANA}သည် မမြဲဟူ၍ဖြစ်စေ{C} ဤသို့ သဘောရှိသော {_KHANTI}ကို အခြားသူထံမှ "
        f"{_hm} ရရှိ၏")
fixed({
    '"Rūpaṃ anicca"nti vā vedanā…pe… saññā… saṅkhārā… "viññāṇaṃ anicca"nti vā yā evarūpī anulomikā khanti diṭṭhi '
    'ruci mudi pekkhā dhammanijjhānakkhanti':
        f"“{RUPA_}သည် မမြဲ”ဟူ၍ဖြစ်စေ {P1.FEEL}{PE} {P1.SANNA}{PE} {PS_LINK['saṅkhārā']}{PE} “{P1.VINNANA}သည် မမြဲ”"
        f"ဟူ၍ဖြစ်စေ ဤသို့ သဘောရှိသော {_KHANTI} ရှိသမျှ",
    "Ṭhapetvā saccānulomikaṃ ñāṇaṃ, sabbāpi sāsavā kusalā paññā kammassakatañāṇaṃ":
        f"{_SACCA} {NANA}{P1.THAPETVA}{C} {T['sāsavā']} {T['kusalā']} {PANNA} အားလုံးသည် {_KAMMA} {KNOW} {NANA} "
        f"{COP[False]}",
})

# ---- tika niddesa (4): āya / apāya
_MAN = "ဤသဘောတရားတို့ကို နှလုံးသွင်းသူအား"
_AK, _KU = T["akusalā"], T["kusalā"]
_ANU, _UPN = T["anuppannā"], T["uppannā"]
fixed({
    '"Ime dhamme manasikaroto anuppannā ceva akusalā dhammā na uppajjanti, uppannā ca akusalā dhammā pahīyanti':
        f"“{_MAN} {_ANU} {_AK} {DH}တို့လည်း မဖြစ်ပေါ်ကြ{C} {_UPN} {_AK} {DH}တို့လည်း ပျောက်ကင်းကြသည်",
    'Ime vā panime dhamme manasikaroto anuppannā ceva kusalā dhammā uppajjanti, uppannā ca kusalā dhammā '
    'bhiyyobhāvāya vepullāya bhāvanāya pāripūriyā saṃvattantī"ti':
        f"{F.VA_OR} {_MAN} {_ANU} {_KU} {DH}တို့လည်း ဖြစ်ပေါ်ကြသည်{C} {_UPN} {_KU} {DH}တို့လည်း ပိုမို "
        f"တိုးပွားရန်{C} ပြန့်ပြောရန်{C} ပွားများရန်{C} ပြည့်စုံရန် ဖြစ်ကြသည်”{TI}",
    '"Ime dhamme manasikaroto anuppannā ceva kusalā dhammā na uppajjanti, uppannā ca kusalā dhammā nirujjhanti':
        f"“{_MAN} {_ANU} {_KU} {DH}တို့လည်း မဖြစ်ပေါ်ကြ{C} {_UPN} {_KU} {DH}တို့လည်း ချုပ်ငြိမ်းကြသည်",
    'Ime vā panime dhamme manasikaroto anuppannā ceva akusalā dhammā uppajjanti, uppannā ca akusalā dhammā '
    'bhiyyobhāvāya vepullāya saṃvattantī"ti':
        f"{F.VA_OR} {_MAN} {_ANU} {_AK} {DH}တို့လည်း ဖြစ်ပေါ်ကြသည်{C} {_UPN} {_AK} {DH}တို့လည်း ပိုမို "
        f"တိုးပွားရန်{C} ပြန့်ပြောရန် ဖြစ်ကြသည်”{TI}",
})

# ---- catukka mātikā / niddesa
_ATTHI = next(t for s_, t in P1_SENT if s_.startswith("Atthi dinnaṃ, atthi yiṭṭhaṃ")).split(f"ဟူ၍{C} ဤသို့")[0]
FIX['"Atthi dinnaṃ, atthi yiṭṭhaṃ, atthi hutaṃ, atthi sukatadukkaṭānaṃ kammānaṃ phalaṃ vipāko, atthi ayaṃ loko, '
    'atthi paro loko, atthi mātā, atthi pitā, atthi sattā opapātikā, atthi loke samaṇabrāhmaṇā sammaggatā '
    'sammāpaṭipannā ye imañca lokaṃ parañca lokaṃ sayaṃ abhiññā sacchikatvā pavedentī"ti'] = f"“{_ATTHI}”{TI}"   # pi-1
fixed_ci({
    "kammassakatañāṇaṃ": f"{_KAMMA} {KNOW} {NANA}", "saccānulomikaṃ ñāṇaṃ": f"{_SACCA} {NANA}",
    "maggasamaṅgissa ñāṇaṃ": f"{P1.MAGGA}နှင့် ပြည့်စုံသူ၏ {NANA}", "phalasamaṅgissa ñāṇaṃ": f"ဖိုလ်နှင့် ပြည့်စုံသူ၏ {NANA}",
    "anvaye ñāṇaṃ": f"ဆက်စပ်၍ {KNOW} {NANA}", "pariye ñāṇaṃ": f"စိတ်ကို ပိုင်းခြား၍ {KNOW} {NANA}",
    "sammutiñāṇaṃ": f"သမုတ်ကို {KNOW} {NANA}",
    "pariye [paricce (sabbattha) passa dīghanikāye] ñāṇaṃ":
        f"စိတ်ကို ပိုင်းခြား၍ {KNOW} {NANA} {VARS['[paricce (sabbattha) passa dīghanikāye]']}",
    "catasso paṭisambhidā": PSG["catasso paṭisambhidā"], "catasso paṭipadā": cnt(P1.PATIPADA, "catu"),
    "cattāri ārammaṇāni": cnt(ARM, "catu"),
    "Imā catasso paṭisambhidā": f"{P1.CU_DEM['pl']} {PSG['catasso paṭisambhidā']} {COP[True]}",
    "Imā catasso paṭipadā": f"{P1.CU_DEM['pl']} {cnt(P1.PATIPADA, 'catu')} {COP[True]}",
    "Imāni cattāri ārammaṇāni": f"{P1.CU_DEM['pl']} {cnt(ARM, 'catu')} {COP[True]}",
    "pañcaṅgiko sammāsamādhi": f"{cnt(P1._ANGA if hasattr(P1, '_ANGA') else 'အင်္ဂါ', 'pañca')} ရှိသော {P1.NAMES['sammāsamādhi']}",
    "pañcañāṇiko sammāsamādhi": f"{cnt(NANA, 'pañca')} ရှိသော {P1.NAMES['sammāsamādhi']}",
    "sattasattati ñāṇavatthūni": f"{NV} ခုနစ်ဆယ့်ခုနစ်{CL}",
    "Imāni sattasattati ñāṇavatthūni": f"{P1.CU_DEM['pl']} {NV} ခုနစ်ဆယ့်ခုနစ်{CL} {COP[True]}",
})
_DASA = "Dasa kilesavatthūni – lobho, doso, moho, māno, diṭṭhi, vicikicchā, thinaṃ, uddhaccaṃ, ahirikaṃ, anottappaṃ"
FIX[_DASA] = next(t for s, t in P1_SENT if s == _DASA + ".").removesuffix(END)     # pi-1 ^1-1565 (final)
fixed_ci({
    "sotadhātuvisuddhiyā ñāṇaṃ": f"စင်ကြယ်သော နား ဓာတ်ဖြင့် {KNOW} {NANA}",
    "pubbenivāsānussatiyā ñāṇaṃ": f"ရှေးဘဝများကို အဖန်ဖန် အောက်မေ့နိုင်သော {NANA}",
    "sattānaṃ cutūpapāte ñāṇaṃ": f"သတ္တဝါတို့၏ သေခြင်းနှင့် ဖြစ်ပေါ်ခြင်းကို {KNOW} {NANA}",
    "āsavānaṃ khaye ñāṇaṃ": f"စိတ်အစွန်းအထင်းတို့ ကုန်ခန်းခြင်းကို {KNOW} {NANA}",
    "imā chasu abhiññāsu paññā": f"{P1.CU_DEM['pl']} {loc_my('chasu abhiññāsu')} {COP[True]}",
    "imā catūsu maggesu catūsu phalesu paññā": f"{P1.CU_DEM['pl']} {loc_my('catūsu maggesu catūsu phalesu')} {COP[True]}",
    "imā navasu anupubbavihārasamāpattīsu paññā":
        f"{P1.CU_DEM['pl']} {loc_my('navasu anupubbavihārasamāpattīsu')} {COP[True]}",
    "saññāvedayitanirodhasamāpattiyā vuṭṭhitassa paccavekkhaṇāñāṇaṃ":
        f"{P1.SANNA}နှင့် {P1.FEEL} ချုပ်ငြိမ်းရာ ဈာန် ဝင်စားရာမှ ထမြောက်သူ၏ ပြန်လည် ဆင်ခြင်သော {NANA}",
})


@frame(r"(?P<s>[Mm]agga|[Dd]hamma)samaṅgissa ñāṇaṃ (?=\S+petaṃ)")
def r_samangi(m):
    return f"{P1.MAGGA if low(m['s']) == 'magga' else DHAMMA_T}နှင့် ပြည့်စုံသူ၏ {NANA}သည် "


@frame(r"(?P<x>" + OBJ_ALT + r")petaṃ ñāṇaṃ")
def r_petam(m):
    return f"{obj_nana(m['x'])}လည်း {COP[False]}"


AC = {
    "ācayāya no apacayāya": "စုပုံခြင်းအတွက် ဖြစ်၍ လျော့ပါးခြင်းအတွက် မဖြစ်သော",
    "apacayāya no ācayāya": "လျော့ပါးခြင်းအတွက် ဖြစ်၍ စုပုံခြင်းအတွက် မဖြစ်သော",
    "ācayāya ceva apacayāya ca": "စုပုံခြင်းအတွက်လည်း ဖြစ်၊ လျော့ပါးခြင်းအတွက်လည်း ဖြစ်သော",
    "nevācayāya no apacayāya": "စုပုံခြင်းအတွက်လည်း မဖြစ်၊ လျော့ပါးခြင်းအတွက်လည်း မဖြစ်သော",
    "neva ācayāya no apacayāya": "စုပုံခြင်းအတွက်လည်း မဖြစ်၊ လျော့ပါးခြင်းအတွက်လည်း မဖြစ်သော",
    "nibbidāya no paṭivedhāya": "ငြီးငွေ့ခြင်းအတွက် ဖြစ်၍ ထိုးဖောက်၍ သိခြင်းအတွက် မဖြစ်သော",
    "paṭivedhāya no nibbidāya": "ထိုးဖောက်၍ သိခြင်းအတွက် ဖြစ်၍ ငြီးငွေ့ခြင်းအတွက် မဖြစ်သော",
    "nibbidāya ceva paṭivedhāya ca": "ငြီးငွေ့ခြင်းအတွက်လည်း ဖြစ်၊ ထိုးဖောက်၍ သိခြင်းအတွက်လည်း ဖြစ်သော",
    "neva nibbidāya no paṭivedhāya": "ငြီးငွေ့ခြင်းအတွက်လည်း မဖြစ်၊ ထိုးဖောက်၍ သိခြင်းအတွက်လည်း မဖြစ်သော",
}
AC_ALT = "(?:" + "|".join(re.escape(k) for k in sorted(AC, key=len, reverse=True)) + ")"


@frame(r"[Aa]tthi paññā (?P<x>" + AC_ALT + r")(?=,|$)")
def r_atthi_ac(m):
    return f"{AC[m['x']]} {PANNA} {HOTI}"


@frame(r"paññā (?P<x>" + AC_ALT + r")(?=\?|\"|$)")
def r_panna_ac(m):
    return f"{AC[m['x']]} {PANNA}"


@frame(r"(?P<a>" + _LOC_ALT + r"(?: " + _LOC_ALT + r")*|avasesā) paññā (?P<x>" + AC_ALT + r")(?=\.)")
def r_ident_ac(m):
    a = "ကြွင်းသော " + PANNA if m["a"] == "avasesā" else loc_my(m["a"])
    return f"{a}သည် {AC[m['x']]} {PANNA} {COP[False]}"


fixed_ci({
    "so iminā dhammena ñātena diṭṭhena pattena viditena pariyogāḷhena atītānāgatena nayaṃ neti":
        f"ထိုသူသည် သိပြီး၊ မြင်ပြီး၊ ရောက်ပြီး၊ ထင်ရှားစွာ သိပြီး၊ နက်နက်နဲနဲ သက်ဝင်ပြီးသော ဤ{DHAMMA_T}ဖြင့် "
        f"အတိတ်နှင့် အနာဂတ်သို့ နည်းကို ဆောင်သည်",
    "ṭhapetvā dhamme ñāṇaṃ anvaye ñāṇaṃ pariye ñāṇaṃ, avasesā paññā sammutiñāṇaṃ":
        f"{DHAMMA_T}ကို {KNOW} {NANA}၊ ဆက်စပ်၍ {KNOW} {NANA}၊ စိတ်ကို ပိုင်းခြား၍ {KNOW} {NANA}{P1.THAPETVA}{C} "
        f"ကြွင်းသော {PANNA}သည် သမုတ်ကို {KNOW} {NANA} {COP[False]}",
    "Idha bhikkhu parasattānaṃ parapuggalānaṃ cetasā ceto paricca pajānāti":
        f"ဤသာသနာတော်၌ ရဟန်းသည် အခြား သတ္တဝါ၊ အခြား ပုဂ္ဂိုလ်တို့၏ စိတ်ကို မိမိ စိတ်ဖြင့် ပိုင်းခြား၍ {F.PAJANATI}",
    "Yāya paññāya kāmesu vītarāgo hoti, na ca abhiññāyo paṭivijjhati na ca saccāni":
        f"အကြင် {PANNA}ဖြင့် ကာမတို့၌ ရာဂ ကင်း၏{C} {P1.ABHINNA}တို့ကိုလည်း ထိုးဖောက်၍ မသိ{C} သစ္စာတို့ကိုလည်း "
        f"ထိုးဖောက်၍ မသိ",
    "sveva paññāya kāmesu vītarāgo samāno abhiññāyo paṭivijjhati na ca saccāni":
        f"ထိုသူပင် {PANNA}ဖြင့် ကာမတို့၌ ရာဂ ကင်းလျက် {P1.ABHINNA}တို့ကို ထိုးဖောက်၍ သိ၏၊ သစ္စာတို့ကိုကား "
        f"ထိုးဖောက်၍ မသိ",
})

# the sixteen states of mind (pariye ñāṇaṃ)
CST = dict(F.CITTA16)        # consistency pass: the sixteen states of mind, shared with ch7
CST_ALT = alt(CST)


@frame(r"(?P<a>" + CST_ALT + r") vā cittaṃ \"(?P<b>" + CST_ALT + r") citta\"nti pajānāt(?:īti|i)")
def r_cst(m):
    a, b = CST[low(m["a"])], CST[m["b"]]
    return f"{a} {P1.MIND}ကိုဖြစ်စေ “{b} {P1.MIND}”{TI} {KNOWB}"


KNOWB = F.PAJANATI                             # (bhikkhu) pajānāti (consistency pass: = ch7 «ကွဲပြားစွာ သိ၏»)

# the four past / future knowers (anvaye ñāṇaṃ)
@frame(r"\"?[Yy]e hi keci (?P<t>atītamaddhānaṃ|anāgatamaddhānaṃ) samaṇā vā brāhmaṇā vā")
def r_yehikeci(m):
    q = "“" if m[0].startswith('"') else ""
    t = "အတိတ်ကာလ၌" if m["t"].startswith("atīt") else "အနာဂတ်ကာလ၌"
    return f"{q}{t} ရဟန်းဖြစ်စေ၊ ပုဏ္ဏားဖြစ်စေ အကြင်သူတို့သည်"


@frame(r"(?P<i>imaññeva te )?(?P<x>" + ACC_ALT + r") (?P<v>abbhaññaṃsu|abhijānissanti|abhijānissantī\"ti)")
def r_abbhannamsu(m):
    pre = "ထိုသူတို့သည် ဤ" if m["i"] else ""
    x = ACC[low(m["x"])]
    if m["i"]:
        x += "ကိုပင်"
    else:
        x += "ကို"
    v = {"abbhaññaṃsu": "ထူးကဲစွာ သိခဲ့ကြ၏", "abhijānissanti": "ထူးကဲစွာ သိကြလိမ့်မည်",
         'abhijānissantī"ti': f"ထူးကဲစွာ သိကြလိမ့်မည်”{TI}"}[m["v"]]
    return f"{pre}{x} {v}"

# ---- catukka (7): hāna / ṭhiti / visesa / nibbedha
_SM = f"{P1.SANNA}နှင့် နှလုံးသွင်းခြင်းတို့"         # saññāmanasikārā
_SAMUD = "ထကြွလာလျှင်"                           # samudācaranti (when they assail)
JLABHA = {f"{_o.capitalize()}ssa jhānassa": f"{_om} {P1.JHANA}" for _o, _om in P1.ORD.items() if _o in
          ("paṭhama", "dutiya", "tatiya", "catuttha")}
for _a, _am in P1.JH_ARUPA_BASE.items():
    JLABHA[_a.capitalize() + "ssa"] = _am
SAHA = {"kāma": "ကာမ", "avitakka": f"{P1.VIT} မရှိခြင်း", "nibbidā": "ငြီးငွေ့ခြင်း", "vitakka": P1.VIT,
        "upekkhā": "ဥပေက္ခာ", "pītisukha": f"ပီတိနှင့် {P1.SUKHA}မှု", "adukkhamasukha": f"မ{P1.DUKKHA} မ{P1.SUKHA}မှု",
        "rūpa": F.RUPA}
for _a, _am in P1.JH_ARUPA_BASE.items():
    SAHA[_a] = _am
SAHA_ALT = alt(SAHA)
BHAG = {k: v for k, v in NEWT.items() if k.endswith("bhāginī")}
BHAG_ALT = alt(BHAG)


@frame(r"(?:(?P<j>" + alt(JLABHA) + r") lābhiṃ )?(?P<q>" + SAHA_ALT + r")sahagatā saññāmanasikārā samudācaranti "
       r"(?P<v>virāgūpasañhitā )?(?P<b>" + BHAG_ALT + r") paññā")
def r_bhagini(m):
    j = f"{JLABHA[m['j']]}ကို ရသူအား " if m["j"] else ""
    v = "ရာဂ ကင်းခြင်းနှင့် စပ်သော " if m["v"] else ""
    return f"{j}{SAHA[low(m['q'])]}နှင့်အတူ ဖြစ်သော {_SM} {_SAMUD} {v}{BHAG[m['b']]} {PANNA} {COP[False]}"


@frame(r"[Tt]adanudhammatā sati santiṭṭhati ṭhitibhāginī paññā")
def r_thiti(m):
    return f"ထိုဈာန်နှင့် လျော်ညီသော သတိ တည်တံ့လျှင် {BHAG['ṭhitibhāginī']} {PANNA} {COP[False]}"


# ---- pañcaka
_PHAR = "ပျံ့နှံ့ခြင်း"
fixed_ci({
    "pītipharaṇatā": f"ပီတိ {_PHAR}", "sukhapharaṇatā": f"{P1.SUKHA}မှု {_PHAR}", "cetopharaṇatā": f"စိတ် {_PHAR}",
    "ālokapharaṇatā": f"အလင်း {_PHAR}", "paccavekkhaṇānimittaṃ": "ပြန်လည် ဆင်ခြင်ခြင်း၏ အမှတ်အသား",
    "Dvīsu jhānesu paññā pītipharaṇatā": f"{loc_my('dvīsu jhānesu')}သည် ပီတိ {_PHAR} {COP[False]}",
    "Tīsu jhānesu paññā sukhapharaṇatā": f"{loc_my('tīsu jhānesu')}သည် {P1.SUKHA}မှု {_PHAR} {COP[False]}",
    "Paracitte ñāṇaṃ cetopharaṇatā": f"အခြားသူ၏ စိတ်ကို {KNOW} {NANA}သည် စိတ် {_PHAR} {COP[False]}",
    "Dibbacakkhu ālokapharaṇatā": f"နတ်မျက်စိသည် အလင်း {_PHAR} {COP[False]}",
    "Tamhā tamhā samādhimhā vuṭṭhitassa paccavekkhaṇāñāṇaṃ paccavekkhaṇānimittaṃ":
        f"ထိုထို သမာဓိမှ ထမြောက်သူ၏ ပြန်လည် ဆင်ခြင်သော {NANA}သည် ပြန်လည် ဆင်ခြင်ခြင်း၏ အမှတ်အသား {COP[False]}",
    "Ayaṃ pañcañāṇiko sammāsamādhi": f"{P1.CU_DEM['sg']} {FIX['pañcañāṇiko sammāsamādhi']} {COP[False]}",
    '"Ayaṃ samādhi paccuppannasukho ceva āyatiñca sukhavipāko"ti':
        f"“ဤသမာဓိသည် ယခုလည်း {P1.SUKHA}၍ နောင်အခါ၌လည်း {P1.SUKHA}သော အကျိုး ရှိသည်”{TI}",
    '"Ayaṃ samādhi ariyo nirāmiso"ti': f"“ဤသမာဓိသည် အရိယာ ဖြစ်သည်{C} လောကီ အာမိသ မရှိ”{TI}",
    '"Ayaṃ samādhi akāpurisasevito"ti': f"“ဤသမာဓိကို သူယုတ်မာတို့ မမှီဝဲကြ”{TI}",
    '"Ayaṃ samādhi santo paṇīto paṭippassaddhaladdho ekodibhāvādhigato na sasaṅkhāraniggayhavāritagato"ti':
        f"“ဤသမာဓိသည် ငြိမ်သက်သည်{C} မွန်မြတ်သည်{C} ငြိမ်းအေးခြင်းဖြင့် ရအပ်သည်{C} စိတ်ကို စုစည်း တည်ငြိမ်ခြင်းသို့ "
        f"ရောက်သည်{C} တိုက်တွန်းမှုဖြင့် နှိပ်ကွပ် တားမြစ်ရသည် မဟုတ်”{TI}",
    'So kho panāhaṃ imaṃ samādhiṃ sato samāpajjāmi sato vuṭṭhahāmī"ti':      # opening quote missing (source)
        f"ငါသည် ဤသမာဓိကို သတိ ရှိလျက် ဝင်စားသည်{C} သတိ ရှိလျက် ထမြောက်သည်”{TI}",
    "paccattaññeva ñāṇaṃ uppajjati": f"မိမိ၌ပင် {NANA} ဖြစ်ပေါ်သည်",
})

# ---- sattaka: the seventy-seven knowledges
CAUSE = {"jāti": "jāti", "bhava": "bhava", "upādāna": "upādāna", "taṇhā": "taṇhā", "vedanā": "vedanā",
         "phassa": "phassa", "saḷāyatana": "saḷāyatana", "nāmarūpa": "nāmarūpa", "viññāṇa": "viññāṇa",
         "saṅkhāra": "saṅkhārā", "avijjā": "avijjā"}
RES = {"jarāmaraṇan": "jarāmaraṇa", "jātī": "jāti", "bhavo": "bhava", "upādānan": "upādāna", "taṇhā": "taṇhā",
       "vedanā": "vedanā", "phasso": "phassa", "saḷāyatanan": "saḷāyatana", "nāmarūpan": "nāmarūpa",
       "viññāṇan": "viññāṇa", "saṅkhārā": "saṅkhārā"}
LOCG = {"jātiyā": "jāti", "avijjāya": "avijjā"}


@frame(r"(?P<a>" + alt(CAUSE) + r")paccayā (?P<b>" + alt(RES) + r")ti ñāṇaṃ")
def r_paccaya_n(m):
    return f"{PS_LINK[CAUSE[low(m['a'])]]}ကြောင့် {PS_LINK[RES[m['b']]]} ဖြစ်ပေါ်သည်{TI} {KNOW} {NANA}"


@frame(r"asati (?P<a>" + alt(LOCG) + r") natthi (?P<b>" + alt(RES) + r")ti ñāṇaṃ")
def r_asati_n(m):
    return f"{PS_LINK[LOCG[m['a']]]} မရှိလျှင် {PS_LINK[RES[m['b']]]} မရှိ{TI} {KNOW} {NANA}"


fixed_ci({
    "atītampi addhānaṃ": "အတိတ်ကာလ၌လည်း", "anāgatampi addhānaṃ": "အနာဂတ်ကာလ၌လည်း",
    "Yampissa taṃ dhammaṭṭhitiñāṇaṃ tampi khayadhammaṃ vayadhammaṃ virāgadhammaṃ nirodhadhammanti ñāṇaṃ":
        f"ထိုသူ၏ {DH} တည်ရှိပုံကို {KNOW} {NANA} ရှိသမျှ၊ ထို{NANA}သည်လည်း ကုန်ခန်းတတ်သော သဘော၊ ပျက်စီးတတ်သော "
        f"သဘော၊ ကင်းပြတ်တတ်သော သဘော၊ ချုပ်ငြိမ်းတတ်သော သဘော ရှိသည်{TI} {KNOW} {NANA}",
})

# ---- dasaka: the ten powers of the Tathāgata
TBALA10 = f"{TATHA}၏ {TBALA} {NUM['dasa']}{CL}"
fixed_ci({
    "dasa tathāgatassa tathāgatabalāni": TBALA10 + C,          # (followed by «yehi balehi …» without a comma)
    "Imāni dasa tathāgatassa tathāgatabalāni": f"{P1.CU_DEM['pl']} {TBALA10} {COP[True]}",
    "yehi balehi samannāgato tathāgato": f"အကြင် {P1.BALA}တို့နှင့် ပြည့်စုံသော {TATHA}သည်",
    "yaṃ balaṃ āgamma tathāgato": f"အကြင် {P1.BALA}ကို မှီ၍ {TATHA}သည်",
    "āsabhaṃ ṭhānaṃ paṭijānāti": "အမြတ်ဆုံး နေရာကို ဝန်ခံတော်မူ၏",
    "parisāsu sīhanādaṃ nadati": "ပရိသတ်တို့၌ ခြင်္သေ့ဟိန်းသံကို ဟိန်းတော်မူ၏",
    "brahmacakkaṃ pavatteti": "မြတ်သော တရားစက်ကို လည်စေတော်မူ၏",
    "idampi tathāgatassa tathāgatabalaṃ hoti": f"ဤသည်လည်း {TATHA}၏ {TBALA} {COP[False]}",
    "Katamāni dasa": f"{NUM['dasa']}{CL} {HUSI} အဘယ်တို့နည်း",
    "Idha tathāgato pajānāti": f"ဤလောက၌ {TATHA}သည် {KNOWS}",
})
DOBJ = {    # «X yathābhūtaṃ pajānāti / ñāṇaṃ» (with the case marker)
    "ṭhānañca ṭhānato aṭṭhānañca aṭṭhānato":
        "ဖြစ်နိုင်သော အကြောင်းကို ဖြစ်နိုင်သော အကြောင်းအဖြစ်လည်းကောင်း၊ မဖြစ်နိုင်သော အကြောင်းကို မဖြစ်နိုင်သော "
        "အကြောင်းအဖြစ်လည်းကောင်း",
    "atītānāgatapaccuppannānaṃ kammasamādānānaṃ ṭhānaso hetuso vipākaṃ":
        f"{T['atītā']}၊ {T['anāgatā']}၊ {T['paccuppannā']} ကံ ဆောက်တည်မှုတို့၏ အကျိုးကို ဖြစ်ရာ အခြေအနေအားဖြင့်၊ "
        f"အကြောင်းရင်းအားဖြင့်",
    "sabbatthagāminiṃ paṭipadaṃ": f"ဘုံ အားလုံးသို့ ရောက်စေသော {P1.PATIPADA}ကို",
    "anekadhātu nānādhātulokaṃ": "ဓာတ် များပြား၍ ဓာတ် အမျိုးမျိုး ရှိသော လောကကို",
    "anekadhātunānādhātulokaṃ": "ဓာတ် များပြား၍ ဓာတ် အမျိုးမျိုး ရှိသော လောကကို",
    "sattānaṃ nānādhimuttikataṃ": "သတ္တဝါတို့၏ စိတ်ညွတ်ရာ အမျိုးမျိုး ကွဲပြားခြင်းကို",
    "parasattānaṃ parapuggalānaṃ indriyaparopariyattaṃ":
        f"အခြား သတ္တဝါ၊ အခြား ပုဂ္ဂိုလ်တို့၏ {P1.INDRIYA}တို့ မြင့်မြတ်ခြင်း နိမ့်ကျခြင်းကို",
    "jhānavimokkhasamādhisamāpattīnaṃ saṃkilesaṃ vodānaṃ vuṭṭhānaṃ":
        "ဈာန်၊ လွတ်မြောက်ခြင်း၊ သမာဓိ၊ ဈာန် ဝင်စားရာတို့၏ ညစ်နွမ်းခြင်း၊ စင်ကြယ်ခြင်း၊ ထမြောက်ခြင်းကို",
    "jhānavimokkhasamādhisamāpattīnaṃ saṃkilesaṃ vodānaṃ":
        "ဈာန်၊ လွတ်မြောက်ခြင်း၊ သမာဓိ၊ ဈာန် ဝင်စားရာတို့၏ ညစ်နွမ်းခြင်း၊ စင်ကြယ်ခြင်းကို",
    "pubbenivāsānussatiṃ": "ရှေးဘဝများကို အဖန်ဖန် အောက်မေ့ခြင်းကို",
    "pubbenivāsānussati": "ရှေးဘဝများကို အဖန်ဖန် အောက်မေ့ခြင်းကို",
    "sattānaṃ cutūpapātaṃ": "သတ္တဝါတို့၏ သေခြင်းနှင့် ဖြစ်ပေါ်ခြင်းကို",
    "āsavānaṃ khayaṃ": "စိတ်အစွန်းအထင်းတို့ ကုန်ခန်းခြင်းကို",
}
DOBJ_ALT = "(?:" + "|".join(re.escape(k) for k in sorted(DOBJ, key=len, reverse=True)) + ")"


@frame(r"(?P<p>Idha|Puna caparaṃ|Yampi) tathāgato(?= )")
def r_tatha_pre(m):
    STATE["yp"] = m["p"] == "Yampi"
    return {"Idha": f"ဤလောက၌ {TATHA}သည်", "Puna caparaṃ": f"တစ်ဖန် {TATHA}သည်", "Yampi": f"{TATHA}သည်"}[m["p"]]


@frame(r"(?P<x>" + DOBJ_ALT + r")(?: (?P<v>\[[^\]]+\]))? yathābhūtaṃ pajānāti")
def r_dobj_knows(m):
    v = (" " + VARS[m["v"]]) if m["v"] else ""
    end = "သိတော်မူခြင်း ရှိသမျှ" if STATE.pop("yp", False) else KNOWS
    return f"{DOBJ[m['x']]}{v} {YATHA} {end}"


@frame(r"(?P<i>idaṃ )?tathāgatassa (?P<x>" + DOBJ_ALT + r") yathābhūtaṃ ñāṇa(?:ṃ|nti)(?=\?|\.|$)")
def r_dobj_nana(m):
    s = f"{TATHA}၏ {DOBJ[m['x']]} {YATHA} {KNOW} {NANA}"
    return f"{P1.CU_DEM['sg']} {s} {COP[False]}" if m["i"] else s


# (1) possible and impossible
DSUB = {
    "diṭṭhisampanno puggalo": "အယူ ပြည့်စုံသော ပုဂ္ဂိုလ်သည်", "puthujjano": "ပုထုဇဉ်သည်",
    "ekissā lokadhātuyā dve arahanto sammāsambuddhā":
        "လောကဓာတ် တစ်ခုတည်း၌ ရဟန္တာ ဖြစ်တော်မူ၍ အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရား "
        f"{NUM['dvi']}{CL}တို့သည်",
    "ekissā lokadhātuyā eko arahaṃ sammāsambuddho":
        "လောကဓာတ် တစ်ခုတည်း၌ ရဟန္တာ ဖြစ်တော်မူ၍ အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရား "
        f"{NUM['eka']}{CL}သည်",
    "ekissā lokadhātuyā dve rājāno cakkavattī [cakkavatti (sī. syā.)]":
        f"လောကဓာတ် တစ်ခုတည်း၌ စကြဝတေး {VARS['[cakkavatti (sī. syā.)]']} မင်း {NUM['dvi']}{CL}တို့သည်",
    "ekissā lokadhātuyā eko rājā cakkavattī": f"လောကဓာတ် တစ်ခုတည်း၌ စကြဝတေး မင်း {NUM['eka']}{CL}သည်",
    "itthī": "အမျိုးသမီးသည်", "puriso": "အမျိုးသားသည်",
}
_CONDUCT = {"kāya": "ကိုယ်ဖြင့် ပြုသော", "vacī": "နှုတ်ဖြင့် ပြုသော", "mano": "မနောဖြင့် ပြုသော"}
for _c, _cm in _CONDUCT.items():
    for _d, _dm in (("duccarita", "ဒုစရိုက်"), ("sucarita", "သုစရိုက်")):
        DSUB[f"{_c}{_d}ssa"] = f"{_cm} {_dm}၏"
        DSUB[f"{_c}{_d}samaṅgī"] = f"{_cm} {_dm}နှင့် ပြည့်စုံသူသည်"
_IKM = f"{F.DEF['iṭṭh']}{C} {F.DEF['kant']}{C} {F.DEF['manāp']}"
_AIKM = f"{F.DEF['aniṭṭh']}{C} {F.DEF['akant']}{C} {F.DEF['amanāp']}"
_BHEDA = "ထိုအရာကြောင့်၊ ထိုအရာကို အကြောင်းပြု၍ ခန္ဓာကိုယ် ပြိုကွဲ၍ သေပြီးနောက်"
SUGATI = "ကောင်းသော လားရာ၊ နတ်ပြည် လောကသို့"
APAYA = "အပါယ်၊ ဆိုးသော လားရာ၊ ပျက်စီး ကျရောက်ရာ၊ ငရဲသို့"
SSB = "ရဟန္တာ ဖြစ်တော်မူ၍ အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရား"
DVERB = {
    "kañci saṅkhāraṃ niccato upagaccheyya": f"မည်သည့် {P1.SANKHARA}ကိုမဆို မြဲသည်ဟု ယူဆရာ၏",
    "kañci saṅkhāraṃ sukhato upagaccheyya": f"မည်သည့် {P1.SANKHARA}ကိုမဆို {P1.SUKHA}သည်ဟု ယူဆရာ၏",
    "kañci dhammaṃ atthato upagaccheyya": f"မည်သည့် {DH}ကိုမဆို အနှစ်သာရ ရှိသည်ဟု ယူဆရာ၏",
    "mātaraṃ jīvitā voropeyya": "အမိကို အသက်မှ သတ်ရာ၏", "pitaraṃ jīvitā voropeyya": "အဖကို အသက်မှ သတ်ရာ၏",
    "arahantaṃ jīvitā voropeyya": "ရဟန္တာကို အသက်မှ သတ်ရာ၏",
    "paduṭṭhena cittena tathāgatassa lohitaṃ uppādeyya":
        f"ပြစ်မှားလိုသော စိတ်ဖြင့် {TATHA}၏ သွေးကို ထွက်စေရာ၏",
    "saṅghaṃ bhindeyya": "သံဃာကို ခွဲရာ၏", "aññaṃ satthāraṃ uddiseyya": "အခြား ဆရာကို ကိုးကွယ်ရာ၏",
    "aṭṭhamaṃ bhavaṃ nibbatteyya": "ရှစ်ကြိမ်မြောက် ဘဝကို ဖြစ်စေရာ၏",
    "apubbaṃ acarimaṃ uppajjeyyuṃ": f"ရှေ့ မရှိ{C} နောက် မရှိဘဲ ဖြစ်ပေါ်ကြရာ၏", "uppajjeyya": "ဖြစ်ပေါ်ရာ၏",
    "arahaṃ assa sammāsambuddho": f"{SSB} ဖြစ်ရာ၏", "rājā assa cakkavattī": "စကြဝတေး မင်း ဖြစ်ရာ၏",
    "sakkattaṃ kareyya": "သိကြားမင်း အဖြစ်ကို ပြုရာ၏", "mārattaṃ kareyya": "မာရ်နတ် အဖြစ်ကို ပြုရာ၏",
    "brahmattaṃ kareyya": "ဗြဟ္မာ အဖြစ်ကို ပြုရာ၏",
    "iṭṭho kanto manāpo vipāko nibbatteyya": f"{_IKM} အကျိုး ဖြစ်ပေါ်ရာ၏",
    "aniṭṭho akanto amanāpo vipāko nibbatteyya": f"{_AIKM} အကျိုး ဖြစ်ပေါ်ရာ၏",
    "tannidānaṃ tappaccayā kāyassa bhedā paraṃ maraṇā sugatiṃ saggaṃ lokaṃ upapajjeyya": f"{_BHEDA} {SUGATI} ရောက်ရာ၏",
    "tannidānaṃ tappaccayā kāyassa bhedā paraṃ maraṇā apāyaṃ duggatiṃ vinipātaṃ nirayaṃ upapajjeyya":
        f"{_BHEDA} {APAYA} ရောက်ရာ၏",
}
fixed(DSUB)
fixed(DVERB)
FIX["yaṃ "] = ""                                 # a repeated «yaṃ» inside a …pe… chain (the clause frame has it)


@frame(r"\"?[Aa]ṭṭhānametaṃ anavakāso yaṃ (?P<b>.+?), netaṃ ṭhānaṃ vijjatī\"ti pajānāti")
def r_atthana(m):
    q = "“" if m[0].startswith('"') else ""
    return (f"{q}{tr(m['b'])} {HUSI} မဖြစ်နိုင်သော အကြောင်း {COP[False]}{C} အခွင့်အလမ်း မရှိ{C} ထိုအကြောင်း မရှိ”"
            f"{TI} {KNOWS}")


@frame(r"\"[Ṭṭ]hānañca kho etaṃ vijjati yaṃ (?P<b>.+?), ṭhānametaṃ vijjatī\"ti pajānāti")
def r_thana(m):
    return f"“{tr(m['b'])} {HUSI}ကား ဖြစ်နိုင်သော အကြောင်း ရှိသည်{C} ထိုအကြောင်း ရှိသည်”{TI} {KNOWS}"


fixed({
    '"Ye ye dhammā yesaṃ yesaṃ dhammānaṃ hetū paccayā upādāya taṃ taṃ ṭhānaṃ, ye ye dhammā yesaṃ yesaṃ dhammānaṃ '
    'na hetū appaccayā upādāya taṃ taṃ aṭṭhāna"nti':
        f"“အကြင် အကြင် {DH}တို့သည် အကြင် အကြင် {DH}တို့၏ အကြောင်းရင်း၊ အကြောင်း ဖြစ်ကြ၏၊ ထိုထိုအရာကို မှီ၍ "
        f"ထိုထို ဖြစ်နိုင်သော အကြောင်း {COP[False]}{C} အကြင် အကြင် {DH}တို့သည် အကြင် အကြင် {DH}တို့၏ "
        f"အကြောင်းရင်း မဟုတ်၊ အကြောင်း မဟုတ်ကြ၏၊ ထိုထိုအရာကို မှီ၍ ထိုထို မဖြစ်နိုင်သော အကြောင်း {COP[False]}”{TI}",
})

# (2) kamma and its results
_KS = {"pāpakāni": "ယုတ်မာသော", "kalyāṇāni": "ကောင်းမြတ်သော"}
_COND = {"gati": "လားရာ ဘဝ", "upadhi": "ခန္ဓာကိုယ်", "kāla": "အချိန်ကာလ", "payoga": "ကြိုးစား အားထုတ်မှု"}
_SV = {"sampatti": "ပြည့်စုံမှု", "vipatti": "ချို့ယွင်းမှု"}


@frame(r"(?P<q>\")?[Aa]tthekaccāni (?P<k>pāpakāni|kalyāṇāni) kammasamādānāni (?P<c>gati|upadhi|kāla|payoga)"
       r"(?P<s>sampatti|vipatti)(?P<f>paṭibāḷhāni na vipaccanti|ṃ āgamma vipaccanti|ṃ āgamma vipaccantī\"ti)")
def r_kammasam(m):
    q = "“" if m["q"] else ""
    head = f"{q}{_KS[m['k']]} ကံ ဆောက်တည်မှု အချို့သည် {_COND[m['c']]} {_SV[m['s']]}"
    if m["f"].startswith("paṭi"):
        return f"{head}ဖြင့် တားဆီးခံရ၍ အကျိုး မပေးကြ"
    return f"{head}ကို မှီ၍ အကျိုး ပေးကြသည်" + (f"”{TI}" if m["f"].endswith('"ti') else "")


# (3) the way leading everywhere
DEST = {"niraya": "ငရဲ", "tiracchānayoni": "တိရစ္ဆာန် ဘဝ", "pettivisaya": "ပြိတ္တာ ဘုံ", "manussaloka": "လူ့ပြည်",
        "devaloka": "နတ်ပြည်", "nibbāna": "နိဗ္ဗာန်"}


@frame(r"\"ayaṃ maggo ayaṃ paṭipadā (?P<d>" + "|".join(DEST) + r")gāmī\"ti(?: (?P<v>\[[^\]]+\]))? pajānāt(?:īti|i)")
def r_dest(m):
    v = (" " + VARS[m["v"]]) if m["v"] else ""
    d = DEST[m["d"]]
    return (f"“ဤသည်မှာ {d}သို့ ရောက်စေသော လမ်း {COP[False]}{C} ဤသည်မှာ {d}သို့ ရောက်စေသော {P1.PATIPADA} {COP[False]}”"
            f"{TI}{v} {KNOWS}")


# (4) the world of many elements
NANATTA = {"khandha": f"{P1.KHANDHA}တို့", "āyatana": "အာရုံခံ နယ်ပယ်တို့", "dhātu": "ဓာတ်တို့",
           "anekadhātunānādhātuloka": "ဓာတ် များပြား၍ ဓာတ် အမျိုးမျိုး ရှိသော လောက"}


@frame(r"(?P<x>" + "|".join(sorted(NANATTA, key=len, reverse=True)) + r")nānattaṃ pajānāt(?:īti|i)")
def r_nanatta(m):
    return f"{NANATTA[m['x']]}၏ ကွဲပြားမှုကို {KNOWS}"


# (5) / adhimutti
_HD = {"hīn": T["hīnā"], "paṇīt": T["paṇītā"], "Hīn": T["hīnā"], "Paṇīt": T["paṇītā"],
       "hīna": T["hīnā"], "paṇīta": T["paṇītā"]}
_VB = {"sevanti bhajanti payirupāsanti": "မှီဝဲကြ ပေါင်းဖော်ကြ ဆည်းကပ်ကြသည်",
       "seviṃsu bhajiṃsu payirupāsiṃsu": "မှီဝဲခဲ့ကြ ပေါင်းဖော်ခဲ့ကြ ဆည်းကပ်ခဲ့ကြသည်",
       "sevissanti bhajissanti payirupāsissanti": "မှီဝဲကြလိမ့်မည် ပေါင်းဖော်ကြလိမ့်မည် ဆည်းကပ်ကြလိမ့်မည်",
       'sevissanti bhajissanti payirupāsissantī"ti': f"မှီဝဲကြလိမ့်မည် ပေါင်းဖော်ကြလိမ့်မည် ဆည်းကပ်ကြလိမ့်မည်”{TI}"}


def _adh(x):
    return f"{_HD[x]} စိတ်ညွတ်ရာ ရှိသော သတ္တဝါတို့"


@frame(r"(?P<a>Hīn|Paṇīt|hīn|paṇīt)ādhimuttikā sattā (?P<b>hīn|paṇīt)ādhimuttike satte (?P<v>"
       + "|".join(re.escape(k) for k in sorted(_VB, key=len, reverse=True)) + ")")
def r_adhim(m):
    return f"{_adh(m['a'])}သည် {_adh(m['b'])}ကို {_VB[m['v']]}"


fixed_ci({
    '"santi sattā hīnādhimuttikā, santi sattā paṇītādhimuttikā':
        f"“{_adh('hīna')} ရှိကြသည်{C} {_adh('paṇīta')} ရှိကြသည်",
    "Santi sattā hīnādhimuttikā, santi sattā paṇītādhimuttikā":
        f"{_adh('hīna')} ရှိကြသည်{C} {_adh('paṇīta')} ရှိကြသည်",
})

# (6) faculties of beings
ASAYA, ANUSAYA, CARITA, ADHIM = "စိတ်သဘောထား", T.get("anusayo", "ကိန်းအောင်းခြင်း"), "စရိုက်", "စိတ်ညွတ်ရာ"
ANUSAYA = "ကိန်းအောင်းခြင်း"
RAJA_A, RAJA_M = "ကိလေသာ မြူ နည်းသော", "ကိလေသာ မြူ များသော"
IND_T, IND_M = f"{P1.INDRIYA} ထက်မြက်သော", f"{P1.INDRIYA} နုံ့သော"
AK_S, AK_D = "အခြင်းအရာ ကောင်းသော", "အခြင်းအရာ ဆိုးသော"
VN_S, VN_D = "သိအောင် ပြောပြရ လွယ်သော", "သိအောင် ပြောပြရ ခက်သော"
BH_Y, BH_N = "ထိုက်တန်သော", "မထိုက်တန်သော"
SATTA_TE = "ထိုသတ္တဝါတို့"
fixed_ci({
    "sattānaṃ āsayaṃ pajānāti": f"သတ္တဝါတို့၏ {ASAYA}ကို {KNOWS}", "anusayaṃ pajānāti": f"{ANUSAYA}ကို {KNOWS}",
    "caritaṃ pajānāti": f"{CARITA}ကို {KNOWS}", "adhimuttiṃ pajānāti": f"{ADHIM}ကို {KNOWS}",
    "apparajakkhe mahārajakkhe tikkhindriye mudindriye svākāre dvākāre suviññāpaye duviññāpaye bhabbābhabbe satte "
    "pajānāti":
        f"{RAJA_A}၊ {RAJA_M}၊ {IND_T}၊ {IND_M}၊ {AK_S}၊ {AK_D}၊ {VN_S}၊ {VN_D}၊ {BH_Y} {BH_N} သတ္တဝါတို့ကို {KNOWS}",
    "Katamo ca sattānaṃ āsayo": f"သတ္တဝါတို့၏ {ASAYA} {HUSI} အဘယ်နည်း",
    "Ayaṃ sattānaṃ āsayo": f"{P1.CU_DEM['sg']} သတ္တဝါတို့၏ {ASAYA} {COP[False]}",
    "Katamo ca sattānaṃ anusayo": f"သတ္တဝါတို့၏ {ANUSAYA} {HUSI} အဘယ်နည်း",
    "Ayaṃ sattānaṃ anusayo": f"{P1.CU_DEM['sg']} သတ္တဝါတို့၏ {ANUSAYA} {COP[False]}",
    "Katamañca sattānaṃ caritaṃ": f"သတ္တဝါတို့၏ {CARITA} {HUSI} အဘယ်နည်း",
    "idaṃ sattānaṃ caritaṃ": f"{P1.CU_DEM['sg']} သတ္တဝါတို့၏ {CARITA} {COP[False]}",
    "Katamā ca sattānaṃ adhimutti": f"သတ္တဝါတို့၏ {ADHIM} {HUSI} အဘယ်နည်း",
    "Ayaṃ sattānaṃ adhimutti": f"{P1.CU_DEM['sg']} သတ္တဝါတို့၏ {ADHIM} {COP[False]}",
    "iti bhavadiṭṭhisannissitā vā sattā honti vibhavadiṭṭhisannissitā vā":
        "ဤသို့ သတ္တဝါတို့သည် ဘဝ ဆက်လက် တည်ရှိသည်ဟူသော အယူကို မှီသူများဖြစ်စေ၊ ဘဝ ပျောက်ကွယ်သည်ဟူသော အယူကို "
        "မှီသူများဖြစ်စေ ဖြစ်ကြသည်",
    "Ete vā pana ubho ante anupagamma idappaccayatā paṭiccasamuppannesu dhammesu anulomikā khanti paṭiladdhā hoti "
    "yathābhūtaṃ ñāṇaṃ":
        f"{F.VA_OR} ဤအစွန်း နှစ်ဖက်စလုံးသို့ မကပ်ရောက်ဘဲ ဤအကြောင်းကြောင့် ဤအကျိုး ဖြစ်ပုံနှင့် အကြောင်းတို့ကို "
        f"မှီ၍ ဖြစ်ပေါ်လာသော {DH}တို့၌ လျော်ညီသော သည်းခံ လက်ခံမှုကို ရရှိထား၏၊ ဤသည် {YATHA} {KNOW} {NANA} "
        f"{COP[False]}",
    "Sattānusayā – kāmarāgānusayo, paṭighānusayo, mānānusayo, diṭṭhānusayo, vicikicchānusayo, bhavarāgānusayo, "
    "avijjānusayo":
        f"{ANUSAYA} {NUM['satta']}{CL} – {P1.KAMARAGA} {ANUSAYA}၊ {P1.PATIGHA_AV} {ANUSAYA}၊ {P1.MANA} {ANUSAYA}၊ "
        f"အယူ {ANUSAYA}၊ {P1.VICIKICCHA} {ANUSAYA}၊ {P1.BHAVARAGA} {ANUSAYA}၊ {PS_LINK['avijjā']} {ANUSAYA}",
    "Yaṃ loke piyarūpaṃ sātarūpaṃ ettha sattānaṃ rāgānusayo anuseti":
        f"လောက၌ ချစ်ဖွယ် သဘော၊ နှစ်သက်ဖွယ် သဘော ရှိသော အရာ ရှိသမျှ၊ ထိုအရာ၌ သတ္တဝါတို့၏ {P1.RAGA} {ANUSAYA}သည် "
        f"ကိန်းအောင်း၏",
    "Yaṃ loke appiyarūpaṃ asātarūpaṃ ettha sattānaṃ paṭighānusayo anuseti":
        f"လောက၌ မချစ်ဖွယ် သဘော၊ မနှစ်သက်ဖွယ် သဘော ရှိသော အရာ ရှိသမျှ၊ ထိုအရာ၌ သတ္တဝါတို့၏ {P1.PATIGHA_AV} "
        f"{ANUSAYA}သည် ကိန်းအောင်း၏",
    "Iti imesu dvīsu dhammesu avijjānupatitā":
        f"ဤသို့ ဤ{DH} {NUM['dvi']}{CL}တို့၌ {PS_LINK['avijjā']}သည် လိုက်ပါ ကျရောက်၏",
    "Tadekaṭṭho māno ca diṭṭhi ca vicikicchā ca daṭṭhabbā":
        f"ထိုအရာနှင့် တစ်နေရာတည်း တည်ရှိသော {P1.MANA}ကိုလည်းကောင်း၊ အယူကိုလည်းကောင်း၊ {P1.VICIKICCHA}ကိုလည်းကောင်း "
        f"{F.SHOULD}",
    "Puññābhisaṅkhāro, apuññābhisaṅkhāro, āneñjābhisaṅkhāro, parittabhūmako vā mahābhūmako vā":
        f"ကောင်းမှုကို {P1.SANKHARA}၊ မကောင်းမှုကို {P1.SANKHARA}၊ မတုန်လှုပ်ခြင်းကို {P1.SANKHARA}၊ "
        f"{T['parittā']} ဘုံနှင့် ဆိုင်သည်ဖြစ်စေ၊ {T['mahaggatā']} ဘုံနှင့် ဆိုင်သည်ဖြစ်စေ",
    "Katame te sattā mahārajakkhā": f"{RAJA_M} {SATTA_TE} {HUSI} အဘယ်တို့နည်း",
    "Katame te sattā apparajakkhā": f"{RAJA_A} {SATTA_TE} {HUSI} အဘယ်တို့နည်း",
    "Katame te sattā mudindriyā": f"{IND_M} {SATTA_TE} {HUSI} အဘယ်တို့နည်း",
    "Katame te sattā tikkhindriyā": f"{IND_T} {SATTA_TE} {HUSI} အဘယ်တို့နည်း",
    "Katame te sattā dvākārā": f"{AK_D} {SATTA_TE} {HUSI} အဘယ်တို့နည်း",
    "Katame te sattā svākārā": f"{AK_S} {SATTA_TE} {HUSI} အဘယ်တို့နည်း",
    "Katame te sattā duviññāpayā": f"{VN_D} {SATTA_TE} {HUSI} အဘယ်တို့နည်း",
    "Katame te sattā abhabbā": f"{BH_N} {SATTA_TE} {HUSI} အဘယ်တို့နည်း",
    "Katame te sattā bhabbā": f"{BH_Y} {SATTA_TE} {HUSI} အဘယ်တို့နည်း",
    "ime te sattā mahārajakkhā": f"ဤသူတို့သည် {RAJA_M} {SATTA_TE} {COP[True]}",
    "ime te sattā apparajakkhā": f"ဤသူတို့သည် {RAJA_A} {SATTA_TE} {COP[True]}",
    "ime te sattā mudindriyā": f"ဤသူတို့သည် {IND_M} {SATTA_TE} {COP[True]}",
    "ime te sattā tikkhindriyā": f"ဤသူတို့သည် {IND_T} {SATTA_TE} {COP[True]}",
    "ime te sattā dvākārā": f"ဤသူတို့သည် {AK_D} {SATTA_TE} {COP[True]}",
    "ime te sattā svākārā": f"ဤသူတို့သည် {AK_S} {SATTA_TE} {COP[True]}",
    "ime te sattā abhabbā": f"ဤသူတို့သည် {BH_N} {SATTA_TE} {COP[True]}",
    "ime te sattā bhabbāti": f"ဤသူတို့သည် {BH_Y} {SATTA_TE} {COP[True]}",
    "Pañcindriyāni – saddhindriyaṃ, vīriyindriyaṃ, satindriyaṃ, samādhindriyaṃ, paññindriyaṃ":
        f"{cnt(P1.INDRIYA, 'pañca')} – " + f"{C} ".join(P1.NAMES[k] for k in (
            "saddhindriyaṃ", "vīriyindriyaṃ", "satindriyaṃ", "samādhindriyaṃ", "paññindriyaṃ")),
    "Ye ca te sattā dvākārā, teva te sattā duviññāpayā":
        f"{AK_D} သတ္တဝါ ရှိသမျှ၊ ထိုသတ္တဝါတို့ပင် {VN_D} သတ္တဝါတို့ {COP[True]}",
    "Ye ca te sattā svākārā, teva te sattā suviññāpayā":
        f"{AK_S} သတ္တဝါ ရှိသမျှ၊ ထိုသတ္တဝါတို့ပင် {VN_S} သတ္တဝါတို့ {COP[True]}",
})
_DONE = {"āsevitāni bhāvitāni bahulīkatāni ussadagatāni": "မှီဝဲအပ်ပြီး၊ ပွားများအပ်ပြီး၊ အဖန်ဖန် ပြုအပ်ပြီး၊ ထူထပ်နေကြ၏",
         "anāsevitāni abhāvitāni abahulīkatāni anussadagatāni":
             "မမှီဝဲအပ်၊ မပွားများအပ်၊ အဖန်ဖန် မပြုအပ်၊ မထူထပ်ကြ"}
for _g, _gm in (("imāni dasa kilesavatthūni", f"ဤကိလေသာ အခြေခံ {NUM['dasa']}{CL}တို့သည်"),
                ("imāni pañcindriyāni", f"ဤ{cnt(P1.INDRIYA, 'pañca')}တို့သည်")):
    for _d, _dm in _DONE.items():
        FIX[f"Yesaṃ sattānaṃ {_g} {_d}"] = f"အကြင် သတ္တဝါတို့၏ {_gm} {_dm}"
_AV = {"kamma": "ကံ", "kilesa": "ကိလေသာ", "vipāka": "အကျိုး"}
_ABH = f"{T['kusalā']} {DH}တို့၌ မှန်ကန်မှု ဖြစ်သော သေချာသော လမ်းကြောင်းသို့ သက်ဆင်းရန်"
fixed({
    "Ye te sattā pāpāsayā pāpānusayā pāpacaritā pāpādhimuttikā mahārajakkhā mudindriyā":
        f"ယုတ်မာသော {ASAYA} ရှိသော၊ ယုတ်မာသော {ANUSAYA} ရှိသော၊ ယုတ်မာသော {CARITA} ရှိသော၊ ယုတ်မာသော {ADHIM} "
        f"ရှိသော၊ {RAJA_M}၊ {IND_M} သတ္တဝါ ရှိသမျှ",
    "Ye te sattā kalyāṇāsayā kalyāṇacaritā kalyāṇādhimuttikā apparajakkhā tikkhindriyā":
        f"ကောင်းမြတ်သော {ASAYA} ရှိသော၊ ကောင်းမြတ်သော {CARITA} ရှိသော၊ ကောင်းမြတ်သော {ADHIM} ရှိသော၊ {RAJA_A}၊ "
        f"{IND_T} သတ္တဝါ ရှိသမျှ",
    "Ye te sattā kammāvaraṇena samannāgatā kilesāvaraṇena samannāgatā vipākāvaraṇena samannāgatā assaddhā "
    "acchandikā duppaññā abhabbā niyāmaṃ okkamituṃ kusalesu dhammesu sammattaṃ":
        "၊ ".join(f"{_m} အဟန့်အတားနှင့် ပြည့်စုံသော" for _m in _AV.values())
        + f"၊ ယုံကြည်မှု မရှိသော၊ ဆန္ဒ မရှိသော၊ ပညာ နည်းသော၊ {_ABH} {BH_N} သတ္တဝါ ရှိသမျှ",
    "Ye te sattā na kammāvaraṇena samannāgatā na kilesāvaraṇena samannāgatā na vipākāvaraṇena samannāgatā saddhā "
    "chandikā paññavanto bhabbā niyāmaṃ okkamituṃ kusalesu dhammesu sammattaṃ":
        "၊ ".join(f"{_m} အဟန့်အတားနှင့် မပြည့်စုံသော" for _m in _AV.values())
        + f"၊ ယုံကြည်မှု ရှိသော၊ ဆန္ဒ ရှိသော၊ ပညာ ရှိသော၊ {_ABH} {BH_Y} သတ္တဝါ ရှိသမျှ",
})

# the ten views (pi-1 final, ^1-? diṭṭhāsavo)
_VIEW_P = ["sassato loko", "asassato loko", "antavā loko", "anantavā loko", "taṃ jīvaṃ taṃ sarīraṃ",
           "aññaṃ jīvaṃ aññaṃ sarīraṃ", "hoti tathāgato paraṃ maraṇā", "na hoti tathāgato paraṃ maraṇā",
           "hoti ca na ca hoti tathāgato paraṃ maraṇā", "neva hoti na na hoti tathāgato paraṃ maraṇā"]
_vs = next(t for s, t in P1_SENT if s.startswith("Sassato lokoti vā, asassato lokoti vā"))
_vs = _vs.split(f"ဟူ၍ဖြစ်စေ{C} ဤသို့")[0].split(f"ဟူ၍ဖြစ်စေ{C} ")
assert len(_vs) == 10, _vs
VIEW = dict(zip(_VIEW_P, _vs))


_VIEW_ALT = sorted({x for v in _VIEW_P for x in (v, v[0].upper() + v[1:], v.removesuffix("ṃ"))}, key=len, reverse=True)


@frame(r"\"(?P<v>" + "|".join(re.escape(v) for v in _VIEW_ALT) + r")(?P<c>\"nti|\"ti|ti) vā")
def r_view(m):
    v = low(m["v"])
    if m["c"] == '"nti':
        v = v + "ṃ"
    close = "”" if m["c"].startswith('"') else ""        # ^2-815: one closing quote missing (source)
    return f"“{VIEW[v]}{close}ဟူ၍ဖြစ်စေ"


# (7) meditators, jhānas, deliverances, concentrations, attainments
JHAYI = "ဈာန်ဝင်စားသူ"
_SA = {"sampatti": "ပြည့်စုံမှု", "vipatti": "ချို့ယွင်းမှု"}


@frame(r"[Aa]tthekacco jhāyī (?P<a>sampatti|vipatti)ṃ?yeva(?: (?P<v>\[[^\]]+\]))? samānaṃ (?P<b>sampatt|vipatt)īti "
       r"pacceti")
def r_jhayi1(m):
    v = (" " + VARS[m["v"]]) if m["v"] else ""
    return f"{JHAYI} အချို့သည် {_SA[m['a']]}ကိုပင်{v} {_SA[m['b'] + 'i']}ဟု ထင်မှတ်၏"


_SP = {"dandhaṃ": "နှေးကွေးစွာ", "khippaṃ": "လျင်မြန်စွာ"}


@frame(r"[Aa]tthekacco jhāyī (?P<a>dandhaṃ|khippaṃ) samāpajjati (?P<b>dandhaṃ|khippaṃ) vuṭṭhāti")
def r_jhayi2(m):
    return f"{JHAYI} အချို့သည် {_SP[m['a']]} ဝင်စား၍ {_SP[m['b']]} ထမြောက်၏"


_SK, _PK = "သမာဓိ၌ သမာဓိ ကျွမ်းကျင်", "သမာဓိ၌ ဝင်စားခြင်း၌ ကျွမ်းကျင်"
fixed_ci({
    "Jhāyīti": f"{JHAYI} {HUSI}", "Cattāro jhāyī": cnt(JHAYI, "catu"),
    "ime cattāro jhāyī": f"ဤသူတို့သည် {cnt(JHAYI, 'catu')} {COP[True]}",
    "Aparepi cattāro jhāyī": f"နောက်ထပ်လည်း {cnt(JHAYI, 'catu')}",
    "Atthekacco jhāyī samādhismiṃ samādhikusalo hoti, na samādhismiṃ samāpattikusalo":
        f"{JHAYI} အချို့သည် {_SK}၏၊ {_PK}သည် မဟုတ်",
    "atthekacco jhāyī samādhismiṃ samāpattikusalo hoti, na samādhismiṃ samādhikusalo":
        f"{JHAYI} အချို့သည် {_PK}၏၊ {_SK}သည် မဟုတ်",
    "atthekacco jhāyī samādhismiṃ samādhikusalo ca hoti, samādhismiṃ samāpattikusalo ca":
        f"{JHAYI} အချို့သည် {_SK}လည်း ဖြစ်၏၊ {_PK}လည်း ဖြစ်၏",
    "atthekacco jhāyī neva samādhismiṃ samādhikusalo hoti, na samādhismiṃ samāpattikusalo":
        f"{JHAYI} အချို့သည် {_SK}သည်လည်း မဟုတ်၊ {_PK}သည်လည်း မဟုတ်",
    '"Jhāna"nti': f"“{P1.JHANA}” {HUSI}",
    "Cattāri jhānāni – paṭhamaṃ jhānaṃ, dutiyaṃ jhānaṃ, tatiyaṃ jhānaṃ, catutthaṃ jhānaṃ":
        f"{cnt(P1.JHANA, 'catu')} – " + f"{C} ".join(f"{P1.ORD[o]} {P1.JHANA}" for o in
                                                    ("paṭhama", "dutiya", "tatiya", "catuttha")),
    '"Vimokkho"ti': f"“လွတ်မြောက်ခြင်း” {HUSI}", "Aṭṭha vimokkhā": cnt("လွတ်မြောက်ခြင်း", "aṭṭha"),
    "Rūpī rūpāni passati": "ရုပ် ရှိသူသည် အဆင်းအရောင်တို့ကို မြင်၏",
    "Ajjhattaṃ arūpasaññī bahiddhā rūpāni passati":
        "မိမိ၌ ရုပ်ဟု မှတ်သိမှု မရှိသူသည် မိမိ၏ ပြင်ပ၌ အဆင်းအရောင်တို့ကို မြင်၏",
    "Subhanteva adhimutto hoti": "တင့်တယ်သည်ဟုသာ စိတ်ညွတ်၏",
    '"ananto ākāso"ti ākāsānañcāyatanaṃ upasampajja viharati':
        f"“ဟင်းလင်းပြင်သည် အဆုံး မရှိ”{TI} {P1.JH_ARUPA_BASE['ākāsānañcāyatana']}ကို ဝင်စား၍ နေ၏",
    '"anantaṃ viññāṇa"nti viññāṇañcāyatanaṃ upasampajja viharati':
        f"“{P1.VINNANA}သည် အဆုံး မရှိ”{TI} {P1.JH_ARUPA_BASE['viññāṇañcāyatana']}ကို ဝင်စား၍ နေ၏",
    '"natthi kiñci"ti ākiñcaññāyatanaṃ upasampajja viharati':
        f"“ဘာမျှ မရှိ”{TI} {P1.JH_ARUPA_BASE['ākiñcaññāyatana']}ကို ဝင်စား၍ နေ၏",
    "nevasaññānāsaññāyatanaṃ upasampajja viharati":
        f"{P1.JH_ARUPA_BASE['nevasaññānāsaññāyatana']}ကို ဝင်စား၍ နေ၏",
    "Sabbaso nevasaññānāsaññāyatanaṃ samatikkamma":
        f"{P1.JH_ARUPA_BASE['nevasaññānāsaññāyatana']}ကို အလုံးစုံ ကျော်လွန်၍",
    "saññāvedayitanirodhaṃ upasampajja viharati": f"{P1.SANNA}နှင့် {P1.FEEL} ချုပ်ငြိမ်းခြင်းကို ဝင်စား၍ နေ၏",
    '"Samādhī"ti': f"“သမာဓိ” {HUSI}",
    "Tayo samādhī – savitakkasavicāro samādhi, avitakkavicāramatto samādhi, avitakkaavicāro samādhi":
        f"{cnt('သမာဓိ', 'ti')} – " + f"{C} ".join(f"{T[k]} သမာဓိ" for k in (
            "savitakkasavicārā", "avitakkavicāramattā", "avitakkaavicārā")),
    '"Samāpattī"ti': f"“ဈာန် ဝင်စားရာ” {HUSI}",
    '"Saṃkilesa"nti hānabhāgiyo dhammo': f"“ညစ်နွမ်းခြင်း” {HUSI} {NEWT['hānabhāginī']} {DH} {COP[False]}",
    '"Vodāna"nti visesabhāgiyo dhammo': f"“စင်ကြယ်ခြင်း” {HUSI} {NEWT['visesabhāginī']} {DH} {COP[False]}",
    '"Vuṭṭhāna"nti': f"“ထမြောက်ခြင်း” {HUSI}",
    "Vodānampi vuṭṭhānaṃ, tamhā tamhā samādhimhā vuṭṭhānampi vuṭṭhānanti":
        f"စင်ကြယ်ခြင်းသည်လည်း ထမြောက်ခြင်း {COP[False]}{C} ထိုထို သမာဓိမှ ထမြောက်ခြင်းသည်လည်း ထမြောက်ခြင်း {COP[False]}",
})
for _a in ("ākāsānañcāyatana", "viññāṇañcāyatana", "ākiñcaññāyatana"):
    FIX["Sabbaso " + _a + "ṃ samatikkamma"] = P1.JH_FORM[f"sabbaso {_a}ṃ samatikkamma"]
for _k in ("sabbaso rūpasaññānaṃ samatikkamā", "paṭighasaññānaṃ atthaṅgamā", "nānattasaññānaṃ amanasikārā"):
    FIX[_k[0].upper() + _k[1:]] = P1.JH_FORM[_k]
    FIX[_k] = P1.JH_FORM[_k]
_ORDM = {"paṭhamo": "paṭhama", "dutiyo": "dutiya", "tatiyo": "tatiya", "catuttho": "catuttha", "pañcamo": "pañcama",
         "chaṭṭho": "chaṭṭha", "sattamo": "sattama", "aṭṭhamo": "aṭṭhama"}


@frame(r"ayaṃ (?P<o>" + "|".join(_ORDM) + r") vimokkho")
def r_vimokkha(m):
    return f"{P1.CU_DEM['sg']} {P1.ORD[_ORDM[m['o']]]} လွတ်မြောက်ခြင်း {COP[False]}"


_SAMAP = [f"{P1.ORD[o]} {P1.JHANA} ဝင်စားရာ" for o in ("paṭhama", "dutiya", "tatiya", "catuttha")]
_SAMAP += [f"{P1.JH_ARUPA_BASE[a]} ဝင်စားရာ" for a in P1.JH_ARUPA_BASE]
_SAMAP.append(f"{P1.SANNA}နှင့် {P1.FEEL} ချုပ်ငြိမ်းရာ ဈာန် ဝင်စားရာ")
FIX["Nava anupubbavihārasamāpattiyo – paṭhamajjhānasamāpatti, dutiyajjhānasamāpatti, tatiyajjhānasamāpatti, "
    "catutthajjhānasamāpatti, ākāsānañcāyatanasamāpatti, viññāṇañcāyatanasamāpatti, ākiñcaññāyatanasamāpatti, "
    "nevasaññānāsaññāyatanasamāpatti, saññāvedayitanirodhasamāpatti"] = (
    f"အစဉ်အတိုင်း နေထိုင်ရာ ဈာန် ဝင်စားရာ {NUM['nava']}{CL} – " + f"{C} ".join(_SAMAP))

# (8) former lives
_LIVES = ["တစ်ဘဝ", "နှစ်ဘဝ", "သုံးဘဝ", "လေးဘဝ", "ငါးဘဝ", "ဆယ်ဘဝ", "နှစ်ဆယ်ဘဝ", "သုံးဆယ်ဘဝ", "လေးဆယ်ဘဝ",
          "ငါးဆယ်ဘဝ", "ဘဝ တစ်ရာ", "ဘဝ တစ်ထောင်", "ဘဝ တစ်သိန်း", "ကမ္ဘာ ပျက်ခြင်း များစွာ", "ကမ္ဘာ တည်ခြင်း များစွာ",
          "ကမ္ဘာ ပျက်ခြင်း တည်ခြင်း များစွာ"]
_EVAM = (f"ဤသို့ အမည် ရှိခဲ့၏{C} ဤသို့ အနွယ် ရှိခဲ့၏{C} ဤသို့ အဆင်း ရှိခဲ့၏{C} ဤသို့ အစာ ရှိခဲ့၏{C} ဤသို့ "
         f"{P1.SUKHA}မှုနှင့် {P1.DUKKHA}မှုကို ခံစားခဲ့၏{C} ဤသို့ အသက် အပိုင်းအခြား ရှိခဲ့၏")
fixed({
    "Idha tathāgato anekavihitaṃ pubbenivāsaṃ anussarati, seyyathidaṃ – ekampi jātiṃ dvepi jātiyo tissopi jātiyo "
    "catassopi jātiyo pañcapi jātiyo dasapi jātiyo vīsampi jātiyo tiṃsampi jātiyo cattālīsampi jātiyo paññāsampi "
    "jātiyo jātisatampi jātisahassampi jātisatasahassampi anekepi saṃvaṭṭakappe anekepi vivaṭṭakappe anekepi "
    "saṃvaṭṭavivaṭṭakappe":
        f"ဤလောက၌ {TATHA}သည် အမျိုးမျိုးသော ရှေးဘဝများကို အဖန်ဖန် အောက်မေ့တော်မူ၏၊ ဥပမာ – "
        + f"{C} ".join(x + "ကိုလည်းကောင်း" for x in _LIVES),
    '"amutrāsiṃ evaṃnāmo evaṃgotto evaṃvaṇṇo evamāhāro evaṃsukhadukkhappaṭisaṃvedī evamāyupariyanto, so tato cuto '
    'amutra udapādiṃ; tatrāpāsiṃ evaṃnāmo evaṃgotto evaṃvaṇṇo evamāhāro evaṃsukhadukkhappaṭisaṃvedī '
    'evamāyupariyanto, so tato cuto idhūpapanno"ti':
        f"“ထိုဘဝ၌ ငါသည် {_EVAM}{C} ထိုငါသည် ထိုဘဝမှ သေ၍ အခြားဘဝ၌ ဖြစ်ပေါ်ခဲ့၏{C} ထိုဘဝ၌လည်း ငါသည် "
        f"{_EVAM}{C} ထိုငါသည် ထိုဘဝမှ သေ၍ ဤဘဝ၌ ဖြစ်ပေါ်လာ၏”{TI}",
    "Iti sākāraṃ sauddesaṃ anekavihitaṃ pubbenivāsaṃ anussaratīti":
        "ဤသို့ အခြင်းအရာနှင့် တကွ၊ ညွှန်ပြချက်နှင့် တကွ အမျိုးမျိုးသော ရှေးဘဝများကို အဖန်ဖန် အောက်မေ့တော်မူ၏",
})

# (9) the divine eye
_DIBBA = "စင်ကြယ်၍ လူ၏ မျက်စိကို ကျော်လွန်သော နတ်မျက်စိဖြင့်"
_BEINGS = (f"သေဆဲ၊ ဖြစ်ပေါ်ဆဲ၊ {T['hīnā']}၊ {T['paṇītā']}၊ အဆင်း လှသော၊ အဆင်း ဆိုးသော၊ ကောင်းသော လားရာ ရှိသော၊ "
           f"ဆိုးသော လားရာ ရှိသော သတ္တဝါတို့ကို မြင်တော်မူ၏၊ ကံအားလျော်စွာ ရောက်သွားကြသော သတ္တဝါတို့ကို")


def _conduct(d):
    return f"{C} ".join(f"{_CONDUCT[c]} {d}နှင့် ပြည့်စုံကြ၏" for c in ("kāya", "vacī", "mano"))


fixed({
    "Idha tathāgato dibbena cakkhunā visuddhena atikkantamānusakena satte passati cavamāne upapajjamāne hīne "
    "paṇīte suvaṇṇe dubbaṇṇe sugate duggate yathākammūpage satte pajānāti":
        f"ဤလောက၌ {TATHA}သည် {_DIBBA} {_BEINGS} {KNOWS}",
    "Iti dibbena cakkhunā visuddhena atikkantamānusakena satte passati cavamāne upapajjamāne hīne paṇīte suvaṇṇe "
    "dubbaṇṇe sugate duggate yathākammūpage satte pajānātīti":
        f"ဤသို့ {_DIBBA} {_BEINGS} {KNOWS}",
    '"ime vata bhonto sattā kāyaduccaritena samannāgatā vacīduccaritena samannāgatā manoduccaritena samannāgatā '
    'ariyānaṃ upavādakā micchādiṭṭhikā micchādiṭṭhikammasamādānā':
        f"“အချင်းတို့၊ ဤသတ္တဝါတို့သည် {_conduct('ဒုစရိုက်')}{C} အရိယာတို့ကို စွပ်စွဲ ပြောဆိုကြ၏{C} မှားယွင်းသော "
        f"အယူ ရှိကြ၏{C} မှားယွင်းသော အယူကြောင့် ဖြစ်သော ကံကို ဆောက်တည်ကြ၏",
    "Ime vā pana bhonto sattā kāyasucaritena samannāgatā vacīsucaritena samannāgatā manosucaritena samannāgatā "
    "ariyānaṃ anupavādakā sammādiṭṭhikā sammādiṭṭhikammasamādānā":
        f"{F.VA_OR} အချင်းတို့၊ ဤသတ္တဝါတို့သည် {_conduct('သုစရိုက်')}{C} အရိယာတို့ကို မစွပ်စွဲကြ{C} မှန်ကန်သော "
        f"အယူ ရှိကြ၏{C} မှန်ကန်သော အယူကြောင့် ဖြစ်သော ကံကို ဆောက်တည်ကြ၏",
    "Te kāyassa bhedā paraṃ maraṇā apāyaṃ duggatiṃ vinipātaṃ nirayaṃ upapannā":
        f"ထိုသူတို့သည် ခန္ဓာကိုယ် ပြိုကွဲ၍ သေပြီးနောက် {APAYA} ရောက်ကြပြီ",
    'Te kāyassa bhedā paraṃ maraṇā sugatiṃ saggaṃ lokaṃ upapannā"ti':
        f"ထိုသူတို့သည် ခန္ဓာကိုယ် ပြိုကွဲ၍ သေပြီးနောက် {SUGATI} ရောက်ကြပြီ”{TI}",
    # (10)
    "Idha tathāgato āsavānaṃ khayā anāsavaṃ cetovimuttiṃ paññāvimuttiṃ diṭṭheva dhamme sayaṃ abhiññā sacchikatvā "
    "upasampajja viharatīti":
        f"ဤလောက၌ {TATHA}သည် စိတ်အစွန်းအထင်းတို့ ကုန်ခန်းခြင်းကြောင့် စိတ်အစွန်းအထင်း မရှိသော စိတ်၏ "
        f"လွတ်မြောက်ခြင်း၊ ပညာဖြင့် လွတ်မြောက်ခြင်းကို မျက်မှောက်ဘဝ၌ပင် ကိုယ်တိုင် ထူးကဲစွာ သိ၍ မျက်မှောက်ပြုပြီး "
        f"ဝင်စား၍ နေတော်မူ၏",
})
SEP[:0] = [(" –", " –")]
SEP.append((",", C))


@frame(r"\"(?=[A-Za-zĀ-ỹ])")
def r_open_quote(m):                             # an opening quote not part of a frame (paragraph-initial «"»)
    return "“"


FIRST = ("r_ident_ac", "r_samangi")             # frames tried before FIX and before the general frames
HIGH[:] = [rf for rf in FRAMES if rf[1].__name__ in FIRST]
FRAMES[:] = [rf for rf in FRAMES if rf[1].__name__ not in FIRST]


# ===================================================================================== lines
HEAD_RE = re.compile(r"(?P<h>#+) (?P<t>.+?)$")


def translate_line(line):
    if not line.strip():
        return ""
    m = ID_RE.search(line)
    body = line[:m.start()] if m else line
    tail = (" " + m.group(1)) if m else ""
    h = HEAD_RE.fullmatch(body)
    if h:
        if h["t"] not in HEAD:
            raise Miss("heading: " + body)
        STATE["part"] = {"Suttantabhājanīyaṃ": "sut", "Abhidhammabhājanīyaṃ": "abh",
                         "Pañhāpucchakaṃ": "pan"}.get(h["t"], STATE.get("part"))
        return f"{h['h']} {HEAD[h['t']]}{tail}"
    if body.endswith(".") and body[:-1] in COLO:
        return COLO[body[:-1]] + END + tail
    if STATE.get("part") == "pan" and not body.startswith("Catasso paṭisambhidā – "):
        return pan_line(body) + tail
    return tr(body) + tail


def write(name, txt):
    txt = unicodedata.normalize("NFC", txt)
    (OUT / name).write_text(txt, encoding="utf-8")
    print(f"wrote {name}: {sum(1 for l in txt.splitlines() if l)} lines")


def chapter(name):
    lines = (PALI / name).read_text(encoding="utf-8-sig").splitlines()
    done = []
    STATE.clear()
    for i, line in enumerate(lines):
        try:
            done.append(translate_line(line))
        except Miss as e:
            print(f"STOP {name} line {i + 1}: {e}\n  {line[:160]}\n  ({len(done)} lines passed; nothing written)")
            sys.exit(1)
    write(name, "\n".join(done).rstrip("\n") + "\n")


if __name__ == "__main__":
    names = [a for a in sys.argv[1:] if not a.startswith("--")] or NAMES_OUT
    for n in names:
        chapter(n)
