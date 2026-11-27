"""Burmese zero-shot of pi-5 (Kathāvatthu, «အငြင်းပွားရာ အကြောင်းအရာများကို ဆွေးနွေးခြင်း»), chapters 6 … 10:
6-atitakkhandhadikatha, 7-ekaccam-atthitikatha, 8-satipatthanakatha, 9-hevatthikatha, 10-dutiyavaggo.

usage: python3 -I -X utf8 make_ch6-10.py [chapter ...] [--misses] [--units]
Model: make_sample.py (the approved sample). Every line is generated from the Pāli by my5_formulas.translate_line()
through the frames, rules and tables of my5_formulas.py and make_sample.py (both imported READ ONLY: make_sample
installs the approved sample tables at import and writes nothing; its __main__ is never run) and the tables of THIS
script, which extends them IN MEMORY only (nothing in my5_formulas.py / make_sample.py / my5-zeroshot-terms.md is
changed):
  * PROP_X (propositions, canonical Pāli -> Cl), QUOTE_X (sutta quotations), SENT_X (unique sentences), LINES_X
    (unique whole lines: verses, uddāna), HEAD_X / COLO_X (headings and colophons), ANCHOR_X (bracket anchors);
  * productive propositions are generated from small tables (subjects × predicates) so that the same Pāli
    proposition is the same Burmese in every frame;
  * NEW: every new recurring term or phrase (Pāli = Burmese), written to notes-ch6-10.md by hand from this table.
A unit no frame / rule / table matches stops the run (my5_formulas.Miss): nothing is guessed. A chapter is written
only when every line passed make_sample.line_check(). --misses lists the misses and writes nothing; --units lists
every failing unit of a chapter (all units, not only the first per line) and writes nothing.
"""
import collections
import pathlib
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import make_sample as MS  # noqa: E402  (installs the approved sample tables; writes nothing at import)

F = MS.F
from my5_formulas import V, FR, Cl, C, END, PE, PUGGALA, SACC, FOUND  # noqa: E402

ROOT = HERE.parents[3]
PALI = MS.PALI
OUT = MS.OUT
NAMES_OUT = ["6-atitakkhandhadikatha.md", "7-ekaccam-atthitikatha.md", "8-satipatthanakatha.md",
             "9-hevatthikatha.md", "10-dutiyavaggo.md"]
W = F.witness
NOUN = F.add_noun
PUG = PUGGALA
PROP_X, QUOTE_X, SENT_X, LINES_X, HEAD_X, COLO_X, ANCHOR_X = {}, {}, {}, {}, {}, {}, {}
NEW = {}         # new recurring strings (Pāli = Burmese) for the notes


def new(pali, my):
    NEW.setdefault(pali, my)
    return my


def section(pali, my):
    """A section name: heading = the name; colophon «X niṭṭhitā.» = «“X” ပြီးဆုံးပြီ။»."""
    HEAD_X[pali] = my
    COLO_X[f"{pali} niṭṭhitā"] = F.DONE.format(my)
    new(pali, my)
    return my


EXIST, NEXIST = "ရှိ", "မရှိ"                                  # atthi / natthi
KATHA = F.KATHA_W

# ===================================================================================== 6. Atītakkhandhādikathā
ATITA = W("1", "^1-M1-18", "atītā dhammā", "အတိတ်")
ANAGATA = W("1", "^1-M1-18", "anāgatā dhammā", "အနာဂတ်")
PACCUP = W("1", "^1-M1-18", "paccuppannā dhammā", "ပစ္စုပ္ပန်")
TIME = {"atīt": ATITA, "anāgat": ANAGATA, "paccuppann": PACCUP}
section("Atītakkhandhādikathā", f"အတိတ် အစုအဝေး စသည်တို့အကြောင်း {KATHA}")
section("Nasuttasādhanaṃ", "သုတ္တန်ဖြင့် မသက်သေပြခြင်း")
section("Suttasādhanaṃ", "သုတ္တန်ဖြင့် သက်သေပြခြင်း")
KH_PL = "အစုအဝေးတို့"                                          # khandhā (sample noun)
TRIAD = f"{F.KHANDHA_W}၊ {F.DHATU_W}၊ {F.AYATANA_W}"            # khandhā dhātu āyatanaṃ
SUBJ6 = {}       # Pāli subject -> Burmese
for _t, _tm in TIME.items():
    SUBJ6[_t + "aṃ"] = _tm
    SUBJ6[f"{_t}aṃ rūpaṃ"] = f"{_tm} {F.RUPA.my}"
    SUBJ6[f"{_t}ā vedanā"] = f"{_tm} {F.VEDANA.my}"
    SUBJ6[f"{_t}ā saññā"] = f"{_tm} {F.SANNA.my}"
    SUBJ6[f"{_t}ā saṅkhārā"] = f"{_tm} {F.SANKHARA.my}"
    SUBJ6[f"{_t}aṃ viññāṇaṃ"] = f"{_tm} {F.VINNANA.my}"
PRED6 = {"khandhā": KH_PL, "khandho": F.KHANDHA_W, "āyatanaṃ": F.AYATANA_W, "dhātu": F.DHATU_W,
         "khandhā dhātu āyatanaṃ": TRIAD}
for _s, _sm in SUBJ6.items():
    PROP_X[f"{_s} atthi"] = V(_sm, EXIST)
    PROP_X[f"{_s} natthi"] = V(_sm, EXIST, neg=True)
    PROP_X[_s] = FR(f"{_sm}သည်")
    for _p, _pm in PRED6.items():
        PROP_X[f"{_s} {_p}"] = V(f"{_sm}သည် {_pm}")
        for _neg, _v in ((False, "atthi"), (True, "natthi")):
            PROP_X[f"{_s} {_p} {_s} {_v}"] = V(f"{_sm}သည် {_pm} ဖြစ်၍ {_sm}", EXIST, neg=_neg)
new("atītaṃ / anāgataṃ / paccuppannaṃ (the past …)", f"{ATITA} / {ANAGATA} / {PACCUP}")
new("atthi / natthi (exists)", f"{EXIST} / {NEXIST}")
new("khandhā dhātu āyatanaṃ", TRIAD)
new("X khandhā / khandho (is aggregates / an aggregate)", f"Xသည် {KH_PL} / {F.KHANDHA_W} ဖြစ်")
new("X P X atthi / natthi", f"Xသည် P ဖြစ်၍ X {EXIST} / {NEXIST}")
_ATAN = f"{ATITA}နှင့် {ANAGATA}"
PROP_X["atītānāgatā khandhā dhātu āyatanaṃ natthi cete"] = V(
    f"{_ATAN}သည် {TRIAD}တို့ ဖြစ်ကြ၍ ထိုအရာတို့", EXIST, neg=True)
new("atītānāgatā khandhā dhātu āyatanaṃ natthi cete",
    f"{_ATAN}သည် {TRIAD}တို့ ဖြစ်ကြ၍ ထိုအရာတို့ {NEXIST}")
NIRUTTI = W("1", "^1-M2-107", "niruttipathā dhammā", "စကားဖြင့် ဖော်ပြမှု၏ လမ်းကြောင်း")
ADHIVACANA = W("1", "^1-M2-106", "adhivacanapathā dhammā", "အမည်ခေါ်ဝေါ်မှု၏ လမ်းကြောင်း")
PANNATTIPATHA = W("1", "^1-M2-108", "paññattipathā dhammā", "သတ်မှတ်ချက်၏ လမ်းကြောင်း")
QUOTE_X["tayome, bhikkhave, niruttipathā adhivacanapathā paññatti… viññūhīti…"] = (
    f"ရဟန်းတို့၊ ဤ သုံးပါးတို့ကား {NIRUTTI}၊ {ADHIVACANA}၊ {F.PANNATTI}… ပညာရှိတို့…")
SENT_X["Nanu vuttaṃ bhagavatā – tayome, bhikkhave, niruttipathā adhivacanapathā paññatti… viññūhīti…."] = (
    F.vutt_cl(QUOTE_X["tayome, bhikkhave, niruttipathā adhivacanapathā paññatti… viññūhīti…"]).f("nanu") + END)
_KH_DEF = {}     # the khandha definitions (pi-2 ^2-2 / ^2-8 / ^2-14 / ^2-20 / ^2-26), read from the FINAL Burmese
for _bid, _stem in (("^2-2", "rūpa"), ("^2-8", "vedanā"), ("^2-14", "saññā"), ("^2-20", "saṅkhāra"),
                    ("^2-26", "viññāṇa")):
    _m = F.strip_id(F.FINAL.seg("2", _bid)[2][0]).split("။ ", 1)[1]
    _pre, _rest = _m.split(" မည်သည့် ", 1)
    _KH_DEF[_stem] = (_pre, "မည်သည့် " + _rest.split("၊ ထိုအားလုံးကို")[0].split(" ထိုအားလုံးကို")[0])
    F.WITNESS.setdefault(f"{_stem} (khandha definition)", ("2", _bid, _KH_DEF[_stem][1]))
_TIMES = _KH_DEF["rūpa"][0].split("၊ မိမိ၌")[0]               # «အတိတ်ဖြစ်စေ၊ အနာဂတ်ဖြစ်စေ၊ ပစ္စုပ္ပန်ဖြစ်စေ»
assert all(v[0] == _KH_DEF["rūpa"][0] for v in _KH_DEF.values())
_KH_CALL = "ဤသည်ကို {}ဟု ခေါ်သည်"                              # ayaṃ vuccati X (pi-2 «– ဤသည်ကို X အစုအဝေးဟု ခေါ်သည်»)
QUOTE_X["yaṃ kiñci, bhikkhave, rūpaṃ atītānāgatapaccuppannaṃ ajjhattaṃ vā bahiddhā vā oḷārikaṃ vā sukhumaṃ vā hīnaṃ "
        "vā paṇītaṃ vā yaṃ dūre santike vā, ayaṃ vuccati rūpakkhandho. Yā kāci vedanā… yā kāci saññā… ye keci "
        "saṅkhārā… yaṃ kiñci viññāṇaṃ atītānāgatapaccuppannaṃ… ayaṃ vuccati viññāṇakkhandho"] = (
    f"ရဟန်းတို့၊ {_KH_DEF['rūpa'][0]} {_KH_DEF['rūpa'][1]}၊ {_KH_CALL.format(F._KH['rūpakkhandho'])}။ "
    f"{_KH_DEF['vedanā'][1]}… {_KH_DEF['saññā'][1]}… {_KH_DEF['saṅkhāra'][1]}… {_TIMES}… {_KH_DEF['viññāṇa'][1]}၊ "
    f"{_KH_CALL.format(F._KH['viññāṇakkhandho'])}")


# ===================================================================================== 7. Ekaccaṃ atthītikathā
class Fut(Cl):
    """A clause in the future («…လိမ့်မည်»), positive only: vipaccissanti, uppajjissanti, nirujjhissanti."""

    def f(self, form, depth=0):
        tail = {"stmt": "", "q": "လော", "bare": "", "cond": "ဆိုလျှင်", "nanu": " မဟုတ်လော", "rel": "သော"}[form]
        return F.q_set((self.pre + " " if self.pre else "") + self.v + "လိမ့်မည်" + tail + self.post, depth)


section("Ekaccaṃ atthītikathā", f"အချို့ ရှိသည်ဟူသော {KATHA}")
section("Atītādiekaccakathā", f"အတိတ် စသည်တို့၏ အချို့အကြောင်း {KATHA}")
section("Anāgatādiekaccakathā", f"အနာဂတ် စသည်တို့၏ အချို့အကြောင်း {KATHA}")
SOME = new("ekaccaṃ / ekacce (some)", "အချို့")
THEY = new("te (those dhammas, after «–»)", "ထိုအရာတို့")
DH_PL = "သဘောတရားတို့"                                              # dhammā (sample noun)
AVV = W("1", "^1-1043", "avipakkavipākānaṃ", "အကျိုး မရင့်ကျက်သေးသော")
VV = new("vipakkavipāka", "အကျိုး ရင့်ကျက်ပြီးသော")
AVP = new("avipāka (dhammā)", "အကျိုး မပေးသော")
UPPADI = W("1", "^1-1043", "dhammā uppādino", "ဖြစ်ပေါ်လာမည့်")
ANUPPADI = new("anuppādino (dhammā)", "မဖြစ်ပေါ်လာမည့်")
W("1", "^1-1044", "niruddhā vigatā vipariṇatā atthaṅgatā abbhatthaṅgatā",
  "ချုပ်ငြိမ်းပြီးသော၊ ကင်းပျောက်ပြီးသော၊ ဖောက်ပြန် ပြောင်းလဲပြီးသော၊ ကွယ်ပျောက်ပြီးသော၊ လုံးဝ ကွယ်ပျောက်ပြီးသော")
W("1", "^1-1046", "jātā bhūtā sañjātā nibbattā", "မွေးဖွားပြီးသော၊ ဖြစ်ပြီးသော၊ ကောင်းစွာ မွေးဖွားပြီးသော၊ ပေါ်ထွက်ပြီးသော")
W("1", "^1-1046", "pātubhūtā", "ထင်ရှားလာပြီးသော")
W("1", "^1-1045", "ajātā abhūtā asañjātā anibbattā", "မမွေးဖွားသေးသော၊ မဖြစ်သေးသော၊ ကောင်းစွာ မမွေးဖွားသေးသော၊ မပေါ်ထွက်သေးသော")
W("1", "^1-1045", "apātubhūtā", "ထင်ရှား မလာသေးသော")
DONE7 = {  # participle (pi-1 ^1-1044 / ^1-1046 / ^1-1045): Pāli -> (positive stem, negative stem)
    "niruddhaṃ": ("ချုပ်ငြိမ်းပြီး", "မချုပ်ငြိမ်းသေး"), "vigataṃ": ("ကင်းပျောက်ပြီး", "မကင်းပျောက်သေး"),
    "atthaṅgataṃ": ("ကွယ်ပျောက်ပြီး", "မကွယ်ပျောက်သေး"), "abbhatthaṅgataṃ": ("လုံးဝ ကွယ်ပျောက်ပြီး", "လုံးဝ မကွယ်ပျောက်သေး"),
    "jātaṃ": ("မွေးဖွားပြီး", "မမွေးဖွားသေး"), "sañjātaṃ": ("ကောင်းစွာ မွေးဖွားပြီး", "ကောင်းစွာ မမွေးဖွားသေး"),
    "nibbattaṃ": ("ပေါ်ထွက်ပြီး", "မပေါ်ထွက်သေး"), "pātubhūtaṃ": ("ထင်ရှားလာပြီး", "ထင်ရှား မလာသေး"),
}
for _k, (_v, _nv) in DONE7.items():
    new(_k, f"{_v} / {_nv}")
    PROP_X[f"ekaccaṃ {_k}"] = Cl(SOME, _v, _nv)
    _neg = "na " + _k
    _neg2 = "a" + _k if _k[0] not in "aā" else None
    PROP_X[f"ekaccaṃ na {_k}"] = Cl(SOME, _v, _nv, neg=True)
    if _k in ("vigataṃ", "jātaṃ", "sañjātaṃ", "nibbattaṃ", "pātubhūtaṃ"):
        PROP_X[f"ekaccaṃ a{_k}"] = Cl(SOME, _v, _nv, neg=True)
PROP_X["ekaccaṃ atthi"] = V(SOME, EXIST)
PROP_X["ekaccaṃ natthi"] = V(SOME, EXIST, neg=True)
_SOME2 = V(f"{SOME} {EXIST}သည်{C} {SOME}", EXIST, neg=True)
for _t in ("atītaṃ", "anāgataṃ"):
    PROP_X[f"{_t} ekaccaṃ atthi, ekaccaṃ natthi"] = V(f"{SUBJ6[_t]}၌ {SOME} {EXIST}သည်{C} {SOME}", EXIST, neg=True)
    PROP_X[f"{_t} ekaccaṃ atthi ekaccaṃ natthi"] = PROP_X[f"{_t} ekaccaṃ atthi, ekaccaṃ natthi"]
SENT_X["Kiṃ atthi kiṃ natthīti?"] = f"အဘယ်အရာ {EXIST}၍ အဘယ်အရာ {NEXIST}သနည်း{END}"
SENT_X["Kiṃ atthi, kiṃ natthīti?"] = SENT_X["Kiṃ atthi kiṃ natthīti?"]
new("Kiṃ atthi(,) kiṃ natthīti?", SENT_X["Kiṃ atthi kiṃ natthīti?"])
DS7 = {}         # Pāli subject (… dhammā) -> Burmese
for _t, _tm in (("atītā", ATITA), ("anāgatā", ANAGATA)):
    for _a, _am in (("avipakkavipākā", AVV), ("vipakkavipākā", VV), ("avipākā", AVP), ("uppādino", UPPADI),
                    ("anuppādino", ANUPPADI)):
        DS7[f"{_t} {_a} dhammā"] = f"{_am} {_tm} {DH_PL}"
DS7["atītā ekadesaṃ vipakkavipākā dhammā ekadesaṃ avipakkavipākā dhammā"] = (
    f"တစ်စိတ်တစ်ဒေသ {VV[:-len('သော')]}၍ တစ်စိတ်တစ်ဒေသ {AVV} {ATITA} {DH_PL}")
new("ekadesaṃ (in part)", "တစ်စိတ်တစ်ဒေသ")
DS7["paccuppannā dhammā"] = f"{PACCUP} {DH_PL}"
VERB7 = {"niruddhā": ("ချုပ်ငြိမ်းပြီး", "မချုပ်ငြိမ်းသေး", False), "ajātā": ("မွေးဖွားပြီး", "မမွေးဖွားသေး", True)}
FUT7 = {"vipaccissanti": "အကျိုး ပေးကြ", "uppajjissanti": "ဖြစ်ပေါ်ကြ", "nirujjhissanti": "ချုပ်ငြိမ်းကြ"}
for _f, _fm in FUT7.items():
    new(_f, _fm + "လိမ့်မည်")
    PROP_X[_f] = Fut("", _fm)
PROP_X["paccuppannā"] = V(PACCUP)
for _neg, _v in ((False, "atthi"), (True, "natthi")):
    PROP_X[f"te {_v}"] = V(THEY, EXIST, neg=_neg)
for _s, _sm in DS7.items():
    PROP_X[f"{_s} ekacce atthi, ekacce natthi"] = V(f"{_sm}၌ {SOME} {EXIST}သည်{C} {SOME}", EXIST, neg=True)
    PROP_X[f"{_s} ekacce atthi ekacce natthi"] = PROP_X[f"{_s} ekacce atthi, ekacce natthi"]
    for _neg, _v in ((False, "atthi"), (True, "natthi")):
        PROP_X[f"{_s} – te {_v}"] = V(f"{_sm} – {THEY}", EXIST, neg=_neg)
    for _k, (_pv, _nv, _ng) in VERB7.items():
        PROP_X[f"{_s} {_k}"] = Cl(f"{_sm}သည်", _pv, _nv, neg=_ng)
        _rel = _nv if _ng else _pv
        for _neg, _v in ((False, "atthi"), (True, "natthi")):
            PROP_X[f"{_s} {_k} – te {_v}"] = V(f"{_rel}သော {_sm} – {THEY}", EXIST, neg=_neg)
        PROP_X[f"{_s} {_k} – te ekacce atthi ekacce natthi"] = V(
            f"{_rel}သော {_sm} – {THEY}၌ {SOME} {EXIST}သည်{C} {SOME}", EXIST, neg=True)
    for _f, _fm in FUT7.items():
        PROP_X[f"{_s} {_f}"] = Fut(f"{_sm}သည်", _fm)
new("X dhammā – te atthi / natthi", f"X {DH_PL} – {THEY} {EXIST} / {NEXIST}")
new("X ekacce atthi, ekacce natthi", f"X၌ {SOME} {EXIST}သည်{C} {SOME} {NEXIST}")


@F.frame(r"(?P<x>.+?)ti katvā (?P<p>.+?)(?:ti)?\?")
def _f_katva_p(m):
    """X-ti katvā P-ti? = «Xဟု အကြောင်းပြု၍ Pသလော» (sample KATVA)."""
    return f"{F.pq(m['x'], 'stmt')}{F.KATVA} {F.pq(m['p'], 'q')}{END}"


new("X-ti katvā P-ti?", f"X{F.KATVA} Pသလော")
VAR_X7 = {"dhammā niruddhā te": F.PATHA, "atītā avipakkavipākā dhammā te natthīti": F.PATHA,
          "vipakkavipākā": F.PATHA, "avipakkavipākā": F.PATHA, "avipākā": F.PATHA}
ANCHOR_X["te"] = THEY


# ===================================================================================== 8. Satipaṭṭhānakathā
SATIPATTHANA = F.heads("Satipaṭṭhānavibhaṅgo").split("များကို")[0]          # «သတိပဋ္ဌာန်» (pi-2)
section("Satipaṭṭhānakathā", f"{SATIPATTHANA}အကြောင်း {KATHA}")
SATI = W("1", "^1-290", "satisambojjhaṅgo", "သတိ")
ALL_DH = "သဘောတရား အားလုံး"                                         # sabbe dhammā (sample QUOTE «sabbe dhammā anattā»)
ALL_SATTA = f"{F.SATTA} အားလုံးတို့"                                 # sabbe sattā
SAT_W = {  # the predicate words of ^5-301 (pi-1 / pi-2 FINAL wording; new ones logged)
    "sati": SATI, "satindriyaṃ": W("1", "^1-290", "satindriyaṃ", "သတိ၏ စွမ်းရည်"),
    "satibalaṃ": W("1", "^1-290", "satibalaṃ", "သတိ၏ စွမ်းအား"),
    "sammāsati": W("1", "^1-290", "sammāsati", "မှန်ကန်သော သတိ"),
    "satisambojjhaṅgo": W("1", "^1-290", "satisambojjhaṅgo", "သတိ ဗောဇ္ဈင်"),
    "ekāyanamaggo": new("ekāyanamaggo", "တစ်ကြောင်းတည်းသော လမ်း"),
    "khayagāmī": new("khayagāmī", "ကုန်ခန်းခြင်းဆီသို့ ဦးတည်သော"),
    "bodhagāmī": new("bodhagāmī", "ဗောဓိဆီသို့ ဦးတည်သော"),
    "apacayagāmī": W("1", "^1-M1-10", "apacayagāmino dhammā", "လျော့ပါးခြင်းဆီသို့ ဦးတည်သော"),
}
for _a, _n in (("anāsav", "စိတ်အစွန်းအထင်း"), ("asaṃyojaniy", "နှောင်ကြိုး"), ("aganthaniy", "အထုံး"),
               ("anoghaniy", "ရေအလျဉ်"), ("ayoganiy", "ထမ်းပိုး"), ("anīvaraṇiy", "အတားအဆီး"),
               ("aparāmaṭṭh", "မှားယွင်းသော ယူဆမှု"), ("anupādāniy", "စွဲလမ်းမှု"), ("asaṃkilesik", "ကိလေသာ")):
    _my = f"{_n}၏ အာရုံ မဖြစ်နိုင်သော"
    if _a not in ("anupādāniy", "asaṃkilesik"):     # pi-1 Mātikā dyads «(Kha) X dhammā» (read from the FINAL text)
        assert F.heads(f"(Kha) {_a}ā dhammā") == f"(ခ) {_my} သဘောတရားများ", _a
    SAT_W[_a + "ā"] = SAT_W[_a + "aṃ"] = _my
W("1", "^1-M2-15", "anāsavā dhammā", "စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော")
W("1", "^1-M2-51", "aparāmaṭṭhā dhammā", "မှားယွင်းသော ယူဆမှု၏ အာရုံ မဖြစ်နိုင်သော")
_ANU = W("2", "^2-U26", "Cattāro satipaṭṭhānā", "သတိပဋ္ဌာန် လေးပါး")
ANUSS = "အဖန်ဖန် အောက်မေ့ခြင်း"                                      # anussati (termbase)
SAT_W.update({
    "buddhānussati": f"ဘုရားကို {ANUSS}", "dhammānussati": f"တရားကို {ANUSS}", "saṅghānussati": f"{F.SANGHA}ကို {ANUSS}",
    "sīlānussati": f"သီလကို {ANUSS}", "cāgānussati": f"စွန့်ကြဲမှုကို {ANUSS}", "devatānussati": f"နတ်တို့ကို {ANUSS}",
    "ānāpānassati": "ထွက်သက် ဝင်သက်၌ သတိ ထားခြင်း", "maraṇānussati": f"သေခြင်းကို {ANUSS}",
    "kāyagatāsati": f"{F.KAYA}ကို အာရုံပြုသော သတိ", "upasamānussati": f"ငြိမ်းချမ်းခြင်းကို {ANUSS}",
})
for _k in ("ekāyanamaggo", "khayagāmī", "bodhagāmī", "buddhānussati", "dhammānussati", "saṅghānussati", "sīlānussati",
           "cāgānussati", "devatānussati", "ānāpānassati", "maraṇānussati", "kāyagatāsati", "upasamānussati"):
    new(_k, SAT_W[_k])


def plist(pali):
    """A predicate list «w1 w2 …pe… wn» -> «m1၊ m2… mn» (+ «အရာ» after a final adjective)."""
    out, seps = [], []
    for tok in re.split(r"(…)", pali):
        if tok == "…":
            seps[-1:] = ["… "]
            continue
        for w in tok.split():
            out.append(SAT_W[w])
            seps.append(f"{C} ")
    s = ""
    for i, w in enumerate(out):
        s += w + (seps[i] if i < len(out) - 1 else "")
    return s + (" အရာ" if s.endswith("သော") else "")


SUBJ8 = {"sabbe dhammā": ALL_DH}
_P1 = ("sati satindriyaṃ satibalaṃ sammāsati satisambojjhaṅgo ekāyanamaggo khayagāmī bodhagāmī apacayagāmī {a}")
_A1 = "anāsavā asaṃyojaniyā aganthaniyā anoghaniyā ayoganiyā anīvaraṇiyā aparāmaṭṭhā anupādāniyā asaṃkilesikā"
_P2 = ("buddhānussati dhammānussati saṅghānussati sīlānussati cāgānussati devatānussati ānāpānassati maraṇānussati "
       "kāyagatāsati upasamānussati")
_CA = F.AYATANA["cakkhāyatana"].my
for _k, _subj, _a in (("sabbe dhammā", ALL_DH, _A1), ("cakkhāyatanaṃ", _CA, "anāsavaṃ asaṃyojaniyaṃ… asaṃkilesikaṃ")):
    _l1 = _P1.format(a=_a)
    PROP_X[f"{_k} {_l1}, {_k} {_P2}"] = V(f"{_subj}သည် {plist(_l1)} ဖြစ်{C} {_subj}သည် {plist(_P2)}")
PROP_X["anottappaṃ sati satindriyaṃ satibalaṃ sammāsati… kāyagatāsati upasamānussati"] = V(
    f"ဒုစရိုက်ကို မကြောက်ရွံ့မှုသည် {plist('sati satindriyaṃ satibalaṃ sammāsati… kāyagatāsati upasamānussati')}")
KIL = dict(zip(("rāgo", "doso", "moho", "māno", "diṭṭhi", "vicikicchā", "thinaṃ", "uddhaccaṃ", "ahirikaṃ",
                "anottappaṃ"),
               ("ရာဂ",) + tuple(F.items("1", "^1-1235")[1].values())[1:]))
for _k, _m in KIL.items():
    NOUN(_m, nom=_k)
_X8 = {F.AYATANA[a].pali["nom"]: F.AYATANA[a].my for a in F.AYATANA}
_X8.update(KIL)
PROP_X["sabbe dhammā satipaṭṭhānā"] = V(f"{ALL_DH}သည် {SATIPATTHANA}")
PROP_X["sati satipaṭṭhānā, sā ca sati"] = V(f"{SATI}သည် {SATIPATTHANA} ဖြစ်၍ ထိုအရာသည်လည်း {SATI}")
PROP_X["sati satipaṭṭhānā, sā ca na sati"] = V(f"{SATI}သည် {SATIPATTHANA} ဖြစ်၍ ထိုအရာသည်လည်း {SATI}", neg=True)
for _k, _m in _X8.items():
    PROP_X[f"{_k} satipaṭṭhānaṃ"] = V(f"{_m}သည် {SATIPATTHANA}")
    PROP_X[f"{_k} satipaṭṭhānaṃ, tañca sati"] = V(f"{_m}သည် {SATIPATTHANA} ဖြစ်၍ ထိုအရာသည်လည်း {SATI}")
    PROP_X[f"{_k} satipaṭṭhānaṃ, tañca na sati"] = V(f"{_m}သည် {SATIPATTHANA} ဖြစ်၍ ထိုအရာသည်လည်း {SATI}", neg=True)
new("satipaṭṭhāna", SATIPATTHANA)
new("X satipaṭṭhānaṃ, tañca (na) sati", f"Xသည် {SATIPATTHANA} ဖြစ်၍ ထိုအရာသည်လည်း {SATI} (မဟုတ်)")
STAND = ("တည်နေ", "မတည်နေ")                                         # santiṭṭhati (termbase «တည်နေသည်»)
_ARB = "ကို အာရုံပြု၍"                                               # ārabbha (pi-1 «… ကို အာရုံပြု၍»)
W("1", "^1-1047", "Atīte dhamme ārabbha", "အတိတ် သဘောတရားတို့ကို အာရုံပြု၍")
_MENT = {"sati": SATI, "phasso": "တွေ့ထိမှု", "vedanā": F.VEDANA.my,
         "saññā": F.SANNA.my, "cetanā": "စေ့ဆော်မှု", "cittaṃ": "စိတ်"}
W("1", "^1-1", "phasso hoti", "တွေ့ထိမှု")
W("1", "^1-1", "cetanā hoti", "စေ့ဆော်မှု")
for _k, _m in _MENT.items():
    for _o in ("sabbe dhamme", "sabbaṃ dhammaṃ"):
        PROP_X[f"{_o} ārabbha {_k} santiṭṭhati"] = Cl(f"{ALL_DH}{_ARB} {_m}", *STAND)
    PROP_X[f"{_k} santiṭṭhati"] = Cl(_m, *STAND)
PT = "ပဋ္ဌာန်"                                                       # -paṭṭhāna (as in satipaṭṭhāna)
for _k, _m in (("phassa", "တွေ့ထိမှု"), ("citta", "စိတ်")):
    PROP_X[f"sabbe dhammā {_k}paṭṭhānā"] = V(f"{ALL_DH}သည် {_m} {PT}")
new("phassapaṭṭhāna / cittapaṭṭhāna", f"တွေ့ထိမှု {PT} / စိတ် {PT}")
new("ārabbha … santiṭṭhati", f"…{_ARB} … တည်နေ")


@F.frame(r"(?P<x>.+?santiṭṭhatī)ti (?P<p>sabbe dhammā \S+)ti\?")
def _f_ti_q(m):
    """X-ti P-ti? (P because of X) = «Xဟူ၍ Pသလော» (the module's «…ဟူ၍» for a «ti» part)."""
    return f"{F.pq(m['x'], 'stmt')}ဟူ၍ {F.pq(m['p'], 'q')}{END}"


new("X-ti P-ti? (P because of X)", "Xဟူ၍ Pသလော")
PROP_X["sabbe sattā upaṭṭhitasatino satiyā samannāgatā satiyā samohitā"] = V(
    f"{ALL_SATTA}သည် သတိ ထင်ရှား ရှိသူ၊ သတိနှင့် အပြည့်အဝ ပြည့်စုံသူ၊ သတိနှင့် ယှဉ်တွဲသူတို့")
PROP_X["sabbesaṃ sattānaṃ sati paccupaṭṭhitā"] = Cl(f"{ALL_SATTA}၌ {SATI}သည် ရှေ့မှောက်၌", *STAND)
QUOTE_X["amataṃ te, bhikkhave, na paribhuñjanti ye kāyagatāsatiṃ na paribhuñjanti. Amataṃ te, bhikkhave, "
        "paribhuñjanti ye kāyagatāsatiṃ paribhuñjantī"] = (
    f"ရဟန်းတို့၊ {SAT_W['kāyagatāsati']}ကို မသုံးဆောင်ကြသူတို့သည် အမြိုက်ကို မသုံးဆောင်ကြ။ ရဟန်းတို့၊ "
    f"{SAT_W['kāyagatāsati']}ကို သုံးဆောင်ကြသူတို့သည် အမြိုက်ကို သုံးဆောင်ကြ၏")
new("amata (the deathless)", "အမြိုက်")
new("paribhuñjati", "သုံးဆောင်")
PROP_X["sabbe sattā kāyagatāsatiṃ paribhuñjanti paṭilabhanti āsevanti bhāventi bahulīkaronti"] = Cl(
    f"{ALL_SATTA}သည် {SAT_W['kāyagatāsati']}ကို သုံးဆောင်ကြ၊ ရရှိကြ၊ အလေ့အကျင့် ပြုကြ၊ ပွားများကြ၊ အကြိမ်ကြိမ်",
    "ပြုကြ", "မပြုကြ")
QUOTE_X["ekāyano ayaṃ, bhikkhave, maggo sattānaṃ visuddhiyā sokaparidevānaṃ samatikkamāya dukkhadomanassānaṃ "
        "atthaṅgamāya ñāyassa adhigamāya nibbānassa sacchikiriyāya yadidaṃ cattāro satipaṭṭhānā"] = (
    f"ရဟန်းတို့၊ {F.SATTA}တို့ စင်ကြယ်ရန်၊ စိုးရိမ်ခြင်း ငိုကြွေးခြင်းတို့ကို လွန်မြောက်ရန်၊ ကိုယ်ဆင်းရဲခြင်း "
    f"စိတ်ဆင်းရဲမှုတို့ ချုပ်ငြိမ်းရန်၊ မှန်ကန်သော နည်းလမ်းကို ရရှိရန်၊ {F.NIBBANA}ကို မျက်မှောက်ပြုရန် ဤလမ်းသည် "
    f"{SAT_W['ekāyanamaggo']} ဖြစ်၏၊ ယင်းကား {_ANU}တို့ပင် ဖြစ်သည်")
PROP_X["sabbe dhammā ekāyanamaggo"] = V(f"{ALL_DH}သည် {SAT_W['ekāyanamaggo']}")
_TG = (f"{F.ARAHA}၊ {F.NAMO.split('၊ ')[-1].replace('ဘုရားရှင်အား ရှိခိုးပါ၏', 'ဘုရားရှင်')} ဖြစ်တော်မူသော "
       f"{F.BHAGAVA}")                                                # Tathāgata arahant sammāsambuddha
W("4", "^4-11", "Arahā", F.ARAHA)
PV = "ထင်ရှား လာခြင်း"                                              # pātubhāva (termbase)
_CK = "စကြဝတေး မင်း"
_RAT = [("cakka", "စက်"), ("hatthi", "ဆင်"), ("assa", "မြင်း"), ("maṇi", "ပတ္တမြား"), ("itthi", "မိန်းမ"),
        ("gahapati", "သူကြွယ်"), ("pariṇāyaka", "ခေါင်းဆောင်")]
_R = {k: f"{m} ရတနာ" for k, m in _RAT}
SENT_X["Nanu vuttaṃ bhagavatā – rañño, bhikkhave, cakkavattissa pātubhāvā sattannaṃ ratanānaṃ pātubhāvo hoti. "
       "Katamesaṃ sattannaṃ? Cakkaratanassa pātubhāvo hoti, hatthiratanassa pātubhāvo hoti, assaratanassa… "
       "maṇiratanassa… itthiratanassa… gahapatiratanassa… pariṇāyakaratanassa pātubhāvo hoti. Rañño, bhikkhave, "
       "cakkavattissa pātubhāvā imesaṃ sattannaṃ ratanānaṃ pātubhāvo hoti."] = (
    f"{F.BHAGAVA} ဤသို့ ဟောတော်မူသည် မဟုတ်လော – “ရဟန်းတို့၊ {_CK} {PV}ကြောင့် ရတနာ ခုနစ်ပါးတို့၏ {PV} ဖြစ်၏။ "
    f"အဘယ် ခုနစ်ပါးတို့နည်း။ {_R['cakka']}၏ {PV} ဖြစ်၏၊ {_R['hatthi']}၏ {PV} ဖြစ်၏၊ {_R['assa']}၏… "
    f"{_R['maṇi']}၏… {_R['itthi']}၏… {_R['gahapati']}၏… {_R['pariṇāyaka']}၏ {PV} ဖြစ်၏။ ရဟန်းတို့၊ {_CK} "
    f"{PV}ကြောင့် ဤ ရတနာ ခုနစ်ပါးတို့၏ {PV} ဖြစ်၏။")
_BJ_H, _BJ = F.items("2", "^2-466")
_BR = {k[:-len("sambojjhaṅgo")]: f"{v} ရတနာ" for k, v in _BJ.items()}
_BRL = [f"{_BR[k]}၏ {PV} ဖြစ်၏" for k in ("sati", "dhammavicaya", "vīriya", "pīti", "passaddhi", "samādhi", "upekkhā")]
SENT_X["Tathāgatassa, bhikkhave, pātubhāvā arahato sammāsambuddhassa sattannaṃ bojjhaṅgaratanānaṃ pātubhāvo hoti. "
       "Katamesaṃ sattannaṃ? Satisambojjhaṅgaratanassa pātubhāvo hoti, dhammavicayasambojjhaṅgaratanassa pātubhāvo "
       "hoti, vīriyasambojjhaṅgaratanassa pātubhāvo hoti, pītisambojjhaṅgaratanassa pātubhāvo hoti, "
       "passaddhisambojjhaṅgaratanassa pātubhāvo hoti, samādhisambojjhaṅgaratanassa pātubhāvo hoti, "
       "upekkhāsambojjhaṅgaratanassa pātubhāvo hoti. Tathāgatassa, bhikkhave, pātubhāvā arahato sammāsambuddhassa "
       "imesaṃ sattannaṃ bojjhaṅgaratanānaṃ pātubhāvo hotīti."] = (
    f"“ရဟန်းတို့၊ {_TG} {PV}ကြောင့် ဗောဇ္ဈင် ရတနာ ခုနစ်ပါးတို့၏ {PV} ဖြစ်၏။ အဘယ် ခုနစ်ပါးတို့နည်း။ "
    + f"{C} ".join(_BRL) + f"။ ရဟန်းတို့၊ {_TG} {PV}ကြောင့် ဤ ဗောဇ္ဈင် ရတနာ ခုနစ်ပါးတို့၏ {PV} ဖြစ်၏”{END}")
new("cakkavattī (rājā)", _CK)
new("ratana", "ရတနာ")
new("tathāgata arahant sammāsambuddha", _TG)
PROP_X["tathāgatassa pātubhāvā arahato sammāsambuddhassa sabbe dhammā satisambojjhaṅgaratanāva honti"] = V(
    f"{_TG} {PV}ကြောင့် {ALL_DH}သည် {_BR['sati']}ပင်")
_SP = F.heads("Sammappadhānavibhaṅgo").split("များကို")[0]
_ID = F.heads("Iddhipādavibhaṅgo").split("များကို")[0]
_BJW = F.heads("Bojjhaṅgavibhaṅgo").split("များကို")[0]
PROP_X["sabbe dhammā sammappadhānā"] = V(f"{ALL_DH}သည် {_SP}")
PROP_X["iddhipādā"] = V(_ID)
PROP_X["indriyā"] = V(F.INDRIYA_W)
PROP_X["balā"] = V(SAT_W["satibalaṃ"].split()[-1])
PROP_X["bojjhaṅgā"] = V(_BJW)


# ===================================================================================== 9. Hevatthikathā
HEVA = new("heva (in a way, hevatthi / heva natthi)", "တစ်နည်းအားဖြင့်")
section("Hevatthikathā", f"{HEVA} ရှိသည်ဟူသော {KATHA}")
_HV = V(f"{HEVA} {EXIST}သည်{C} {HEVA}", EXIST, neg=True)           # hevatthi, heva natthi
PROP_X["hevatthi, heva natthi"] = PROP_X["hevatthi heva natthi"] = _HV
PROP_X["hevatthi"] = V(HEVA, EXIST)
PROP_X["heva natthi"] = V(HEVA, EXIST, neg=True)
new("hevatthi, heva natthi", _HV.f("stmt"))
PROP_X["sevatthi, seva natthi"] = V(f"ထိုအရာပင် {EXIST}သည်{C} ထိုအရာပင်", EXIST, neg=True)
new("sevatthi, seva natthi", PROP_X["sevatthi, seva natthi"].f("stmt"))
SENT_X["Kintatthi, kinti natthīti?"] = f"အဘယ်နည်းဖြင့် {EXIST}၍ အဘယ်နည်းဖြင့် {NEXIST}သနည်း{END}"
new("Kintatthi, kinti natthīti?", SENT_X["Kintatthi, kinti natthīti?"])
_AT = f"{EXIST}ခြင်း၏ အနက်"                                       # atthaṭṭho
_NAT = f"{NEXIST}ခြင်း၏ အနက်"                                     # natthaṭṭho
_AB = f"{EXIST}ခြင်း၏ အဖြစ်"                                      # atthibhāvo
_NAB = f"{NEXIST}ခြင်း၏ အဖြစ်"                                    # natthibhāvo
_SAME = "ဤစကားတို့သည် အနက် တူသော၊ ညီမျှသော၊ အချိုး တူသော၊ တစ်မျိုးတည်းမှ ဖြစ်သော စကားတို့"   # sample _KAYA_SYN
assert _SAME in MS._KAYA_SYN
_SAME_T = _SAME[_SAME.index("ညီမျှသော"):]                         # after «…pe… same»
for _k, _m in (
        ("atthaṭṭho natthaṭṭho, natthaṭṭho atthaṭṭho, atthibhāvo natthibhāvo, natthibhāvo atthibhāvo, atthīti vā "
         "natthīti vā, natthīti vā atthīti vā esese ekaṭṭhe same samabhāge tajjāte",
         f"{_AT}နှင့် {_NAT}{C} {_NAT}နှင့် {_AT}{C} {_AB}နှင့် {_AB.replace(EXIST, NEXIST)}{C} {_NAB}နှင့် {_AB}{C} "
         f"{EXIST}ဟုဖြစ်စေ {NEXIST}ဟုဖြစ်စေ{C} {NEXIST}ဟုဖြစ်စေ {EXIST}ဟုဖြစ်စေ {_SAME}"),
        ("atthaṭṭho natthaṭṭho… same samabhāge tajjāte", f"{_AT}နှင့် {_NAT}… {_SAME_T}"),
        ("atthaṭṭho natthaṭṭho, natthaṭṭho atthaṭṭho… same samabhāge tajjāte",
         f"{_AT}နှင့် {_NAT}{C} {_NAT}နှင့် {_AT}… {_SAME_T}")):
    PROP_X[_k] = V(_m)
new("atthaṭṭho / natthaṭṭho; atthibhāvo / natthibhāvo", f"{_AT} / {_NAT}; {_AB} / {_NAB}")
AS = "အနေဖြင့်"                                                    # X Y-ti (as Y)
_HN9 = {"atītaṃ": ATITA, "anāgataṃ": ANAGATA, "paccuppannaṃ": PACCUP}
for _n in F.KHANDHA5:
    _HN9[_n.pali["nom"]] = _n.my
_HN9_AS = dict(_HN9)
_HN9_AS.update({"atītan": ATITA, "anāgatan": ANAGATA, "paccuppannan": PACCUP, "rūpan": F.RUPA.my,
                "viññāṇan": F.VINNANA.my, "vedanā": F.VEDANA.my, "saññā": F.SANNA.my, "saṅkhārā": F.SANKHARA.my})
for _x, _xm in _HN9.items():
    PROP_X[f"{_x} atthi"] = V(_xm, EXIST)
    PROP_X[f"{_x} hevatthi, heva natthi"] = PROP_X[f"{_x} hevatthi heva natthi"] = V(
        f"{_xm}သည် {HEVA} {EXIST}သည်{C} {HEVA}", EXIST, neg=True)
    for _y, _ym in _HN9_AS.items():
        if _y in ("atītaṃ", "anāgataṃ", "paccuppannaṃ", "rūpaṃ", "viññāṇaṃ"):
            continue
        for _h, _neg in (("hevatthi", False), ("heva natthi", True), ("hevaṃ natthi", True)):
            PROP_X[f"{_x} {_y}ti {_h}"] = V(f"{_xm}သည် {_ym} {AS} {HEVA}", EXIST, neg=_neg)
new("X Y-ti hevatthi / heva natthi", f"Xသည် Y {AS} {HEVA} {EXIST} / {NEXIST}")
for _n in F.KHANDHA5[1:]:
    NOUN(_n.my, nom=_n.pali["nom"]) if F.noun(_n.pali["nom"], "nom") is None else None
LINES_X["Tassuddānaṃ –"] = new("Tassuddānaṃ –", "ထို၏ အကျဉ်းချုပ် –")
LINES_X["Upalabbho parihāni, brahmacariyavāso odhiso;"] = (
    f"{FOUND}ခြင်း{C} ဆုတ်ယုတ်ခြင်း{C} မြတ်သော အကျင့်ကို ကျင့်ခြင်း{C} အပိုင်းအခြားအားဖြင့်{C}")
LINES_X["Pariññā kāmarāgappahānaṃ, sabbatthivādo āyatanaṃ;"] = (
    f"ပိုင်းခြား သိခြင်း{C} ကာမရာဂကို ပယ်ခြင်း{C} အားလုံး ရှိသည်ဟူသော ဝါဒ{C} {F.AYATANA_W}{C}")
LINES_X["Atītānāgato subhaṅgo, sabbe dhammā satipaṭṭhānā."] = (
    f"{ATITA}နှင့် {ANAGATA}{C} ကောင်းစွာ ခွဲခြားချက် ⟦0⟧{C} {ALL_DH}သည် {SATIPATTHANA}{END}")
VAR_X9 = {"atītānāgatesu bhāgo": F.PATHA}
VAGGA_LINE = {"Paṭhamavaggo": f"{F.ORD_MY[1]} {F.VAGGA_W}", "Mahāvaggo": f"“ကြီးမြတ်သော” {F.VAGGA_W}"}
for _k, _v in VAGGA_LINE.items():
    COLO_X[_k] = new(_k, _v)


# ===================================================================================== 10. Dutiyavaggo: shared parts
section("Dutiyavaggo", f"{F.ORD_MY[2]} {F.VAGGA_W}")
COLO_X["Dutiyavaggo"] = HEAD_X["Dutiyavaggo"]
ARAHA = F.ARAHA                                                      # «ရဟန္တာ»
PUTHU = "ပုထုဇဉ်"                                                   # puthujjano (termbase)
SADH = "မိမိ၏ အရာ၌ ကျွမ်းကျင်သော ရဟန္တာ"                            # sadhammakusala arahā
PARA = "သူတစ်ပါး၏ အရာ၌ ကျွမ်းကျင်သော ရဟန္တာ"                       # paradhammakusala arahā
new("sadhammakusala / paradhammakusala arahā", f"{SADH} / {PARA}")
GEN = {  # genitive (atthi G X) -> Burmese «G၌»
    "arahato": f"{ARAHA}၌", "puthujjanassa": f"{PUTHU}၌", "tassa": "ထိုသူ၌",
    "mārakāyikānaṃ devatānaṃ": "မာရ်နတ်၏ အပေါင်းအပါ နတ်တို့၌", "sabbesaṃyeva": "ထိုသူ အားလုံးတို့၌ပင်",
    "dārakānaṃ": "ကလေးငယ်တို့၌", "paṇḍakānaṃ": "ပဏ္ဍုက်တို့၌", "devatānaṃ": "နတ်တို့၌",
    "sadhammakusalassa arahato": f"{SADH}၌", "paradhammakusalassa arahato": f"{PARA}၌",
}
MK = "မာရ်နတ်၏ အပေါင်းအပါ နတ်တို့"                                  # mārakāyikā devatā
new("mārakāyikā devatā", MK)
ASUCI = "မစင်ကြယ်သော သုက်ထွက်ခြင်း"                                # asuci sukkavissaṭṭhi
ASUCI_ACC = "မစင်ကြယ်သော သုက်"                                      # asuciṃ sukkavissaṭṭhiṃ (as a thing brought)
new("asuci sukkavissaṭṭhi", ASUCI)
_AV = "အမှန်ကို မသိမှု"
_VC = "ယုံမှားမှု"
OBJ10 = {"satthari": "ဘုရားရှင်အပေါ်", "dhamme": "တရားတော်အပေါ်", "saṅghe": "သံဃာတော်အပေါ်", "sikkhāya": "ကျင့်စဉ်အပေါ်",
         "pubbante": "အတိတ်ကာလအပေါ်", "aparante": "အနာဂတ်ကာလအပေါ်",
         "pubbantāparante": "အတိတ်ကာလနှင့် အနာဂတ်ကာလအပေါ်",
         "idappaccayatāpaṭiccasamuppannesu dhammesu":
             "ဤအကြောင်းကြောင့် ဤအကျိုး ဖြစ်ပုံနှင့် အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်လာသော သဘောတရားတို့အပေါ်"}
W("2", "^2-915", "idappaccayatāpaṭiccasamuppannesu dhammesu", OBJ10["idappaccayatāpaṭiccasamuppannesu dhammesu"])
W("2", "^2-915", "Satthari kaṅkhati", OBJ10["satthari"])
VIMATI = W("1", "^1-1008", "vimati", "စိတ်ရှုပ်ထွေးခြင်း")
ANNANA = "မသိခြင်း"                                                  # aññāṇaṃ (termbase)
KANKHA = W("1", "^1-425", "kaṅkhā", "သံသယ")
LST = {  # list words (atthi G X …): Pāli -> Burmese
    "asuci sukkavissaṭṭhi": ASUCI, "rāgo": "ရာဂ", "kāmarāgo": "ကာမရာဂ",
    "kāmarāgapariyuṭṭhānaṃ": "ကာမရာဂ ထကြွခြင်း", "kāmarāgasaṃyojanaṃ": "ကာမရာဂ နှောင်ကြိုး",
    "kāmogho": "ကာမ ရေအလျဉ်", "kāmayogo": "ကာမ ထမ်းပိုး", "kāmacchandanīvaraṇaṃ": "ကာမကို လိုလားမှု အတားအဆီး",
    "vimati": VIMATI, "aññāṇaṃ": ANNANA, "kaṅkhā": KANKHA, "āsayo": "သိုလှောင်ရာ",
    "parūpahāro": "သူတစ်ပါးက ဆောင်ယူပေးခြင်း",
    "avijjā": _AV, "avijjogho": f"{_AV} ရေအလျဉ်", "avijjāyogo": f"{_AV} ထမ်းပိုး",
    "avijjānusayo": f"{_AV} ကိန်းအောင်းခြင်း", "avijjāpariyuṭṭhānaṃ": f"{_AV} ထကြွခြင်း",
    "avijjāsaṃyojanaṃ": f"{_AV} နှောင်ကြိုး", "avijjānīvaraṇaṃ": f"{_AV} အတားအဆီး",
    "vicikicchā": _VC, "vicikicchāpariyuṭṭhānaṃ": f"{_VC} ထကြွခြင်း", "vicikicchāsaṃyojanaṃ": f"{_VC} နှောင်ကြိုး",
    "vicikicchānīvaraṇaṃ": f"{_VC} အတားအဆီး",
}
for _k in ("kāmarāgapariyuṭṭhānaṃ", "kāmogho", "kāmayogo", "kāmacchandanīvaraṇaṃ", "avijjogho", "avijjānusayo",
           "avijjāpariyuṭṭhānaṃ", "vicikicchāpariyuṭṭhānaṃ", "āsayo", "parūpahāro"):
    new(_k, LST[_k])
for _o, _om in OBJ10.items():
    for _x, _xm in (("vimati", VIMATI), ("aññāṇaṃ", ANNANA), ("kaṅkhā", KANKHA)):
        LST[f"{_o} {_x}"] = f"{_om} {_xm}"
_LSEP = re.compile(r"(, |… |…| )")


def lst(pali):
    """A list «w1 w2, w3…pe… w4» of LST words -> «m1၊ m2၊ m3… m4» (None when a word is unknown)."""
    parts = _LSEP.split(pali.strip())
    words, seps = parts[0::2], parts[1::2]
    out, i = [], 0
    while i < len(words):
        for j in range(len(words), i, -1):
            if any(x != " " for x in seps[i:j - 1]):
                continue
            k = " ".join(words[i:j])
            if k in LST:
                out.append((LST[k], seps[j - 1] if j - 1 < len(seps) else ""))
                i = j
                break
        else:
            return None
    return "".join(m + ("" if not sp else (PE + " " if "…" in sp else f"{C} ")) for m, sp in out)


def _gen_split(rest):
    for g in sorted(GEN, key=len, reverse=True):
        if rest.startswith(g + " "):
            return g, rest[len(g) + 1:]
    return None, None


@F.rule(r"(?P<n>n)?atthi (?P<rest>.+)")
def _r_atthi_gen(m):
    """(n)atthi G X (a list): «G၌ X (မ)ရှိ»."""
    g, x = _gen_split(m["rest"])
    if g is None or lst(x) is None:
        return None
    return V(f"{GEN[g]} {lst(x)}", EXIST, neg=bool(m["n"]))


@F.rule(r"(?P<g>.+?) (?P<n>n)?atthi (?P<x>.+)")
def _r_gen_atthi(m):
    """G (n)atthi X: the same clause («sadhammakusalassa arahato atthi …»)."""
    if m["g"] not in GEN or lst(m["x"]) is None:
        return None
    return V(f"{GEN[m['g']]} {lst(m['x'])}", EXIST, neg=bool(m["n"]))


new("atthi G X / natthi G X", f"G၌ X {EXIST} / {NEXIST}")
SENT_X["Kenaṭṭhenāti?"] = new("Kenaṭṭhenāti?", f"အဘယ် အနက်ကြောင့်နည်း{END}")
SENT_X["Kiṃ kāraṇāti?"] = new("Kiṃ kāraṇāti?", f"အဘယ် အကြောင်းကြောင့်နည်း{END}")
UPAS = ("ဆောင်ယူပေးကြ", "ဆောင်ယူ မပေးကြ")                          # upasaṃharanti
new("upasaṃharanti", UPAS[0])
SENT_X["Handa hi mārakāyikā devatā arahato asuciṃ sukkavissaṭṭhiṃ upasaṃharantīti."] = (
    f"အမှန်အားဖြင့် {MK}သည် {ARAHA}အား {ASUCI_ACC}ကို {UPAS[0]}သောကြောင့် ဖြစ်သည်{END}")
PROP_X["mārakāyikā devatā arahato asuciṃ sukkavissaṭṭhiṃ upasaṃharanti"] = Cl(
    f"{MK}သည် {ARAHA}အား {ASUCI_ACC}ကို", *UPAS)
for _w, _wm in (("attano", "မိမိတို့၏"), ("aññesaṃ", "အခြားသူတို့၏"), ("tassa", "ထိုရဟန္တာ၏")):
    PROP_X[f"{_w} asuciṃ sukkavissaṭṭhiṃ upasaṃharanti"] = Cl(f"{_wm} {ASUCI_ACC}ကို", *UPAS)
    PROP_X[f"mārakāyikā devatā {_w} asuciṃ sukkavissaṭṭhiṃ upasaṃharanti"] = Cl(
        f"{MK}သည် {_wm} {ASUCI_ACC}ကို", *UPAS)
PROP_X["mārakāyikā devatā neva attano na aññesaṃ na tassa asuciṃ sukkavissaṭṭhiṃ upasaṃharanti"] = Cl(
    f"{MK}သည် မိမိတို့၏လည်း မဟုတ်၊ အခြားသူတို့၏လည်း မဟုတ်၊ ထိုရဟန္တာ၏လည်း မဟုတ်သော {ASUCI_ACC}ကို", *UPAS,
    neg=True)
PROP_X["lomakūpehi upasaṃharanti"] = Cl("ချွေးပေါက်တို့မှ", *UPAS)
SENT_X["Handa hi vimatiṃ gāhayissāmāti."] = f"အမှန်အားဖြင့် {VIMATI}ကို ဖြစ်စေကြမည်ဟု ဖြစ်သည်{END}"
ASITA = "စား၊ သောက်၊ ခဲ၊ လျက်ထားသော အရာ"                            # asitapītakhāyitasāyita
NISS = "အကျိုးဆက်"                                                   # nissando
new("asitapītakhāyitasāyitassa nissando", f"{ASITA}၏ {NISS}")
SENT_X["Arahato asuci sukkavissaṭṭhi kissa nissandoti?"] = f"{ARAHA}၏ {ASUCI}သည် အဘယ်အရာ၏ {NISS}နည်း{END}"
SENT_X["Asitapītakhāyitasāyitassa nissandoti."] = f"{ASITA}၏ {NISS} ဖြစ်သည်{END}"
PROP_X["arahato asuci sukkavissaṭṭhi asitapītakhāyitasāyitassa nissando"] = V(
    f"{ARAHA}၏ {ASUCI}သည် {ASITA}၏ {NISS}")
PROP_X["arahato uccārapassāvo asitapītakhāyitasāyitassa nissando"] = V(
    f"{ARAHA}၏ ကျင်ကြီး ကျင်ငယ်သည် {ASITA}၏ {NISS}")
W("2", "^2-508", "uccārapassāvakamme", "ကျင်ကြီး ကျင်ငယ်")
PROP_X["atthi tassa āsayo"] = V("ထိုအရာ၏ သိုလှောင်ရာ", EXIST)
PROP_X["natthi tassa āsayo"] = V("ထိုအရာ၏ သိုလှောင်ရာ", EXIST, neg=True)
_EAT = "စားကြ၊ သောက်ကြ၊ ခဲကြ၊"
PROP_X["ye keci asanti pivanti khādanti sāyanti"] = FR(f"{_EAT} လျက်ကြသူ မည်သူမဆို")
for _k, _m in (("dārakā", "ကလေးငယ်တို့"), ("paṇḍakā", "ပဏ္ဍုက်တို့"), ("devā", F.DEVA + "တို့")):
    PROP_X[f"{_k} asanti pivanti khādanti sāyanti"] = Cl(f"{_m}သည် {_EAT}", "လျက်ကြ", "မလျက်ကြ")
ACTS = {  # optative acts: Pāli -> (object / adverb, verb)
    "methunaṃ dhammaṃ paṭiseveyya": ("မေထုန် အကျင့်ကို", "မှီဝဲရာ"), "methunaṃ uppādeyya": ("မေထုန်ကို", "ဖြစ်စေရာ"),
    "puttasambādhasayanaṃ ajjhāvaseyya": ("သားသမီးတို့ဖြင့် ကျဉ်းကျပ်သော အိပ်ရာ၌", "နေရာ"),
    "kāsikacandanaṃ paccanubhaveyya": ("ကာသိ စန္ဒကူးကို", "ခံစားရာ"),
    "mālāgandhavilepanaṃ dhāreyya": ("ပန်း၊ နံ့သာ၊ နံ့သာပျောင်းကို", "ဆောင်ရာ"),
    "jātarūparajataṃ sādiyeyya": ("ရွှေ ငွေကို", "သာယာရာ"),
    "pāṇaṃ haneyya": ("သူ့အသက်ကို", "သတ်ရာ"), "adinnaṃ ādiyeyya": ("မပေးသည်ကို", "ယူရာ"),
    "musā bhaṇeyya": ("မုသား", "ပြောရာ"), "pisuṇaṃ bhaṇeyya": ("ကုန်းတိုက်သော စကားကို", "ပြောရာ"),
    "pharusaṃ bhaṇeyya": ("ကြမ်းတမ်းသော စကားကို", "ပြောရာ"), "samphaṃ palapeyya": ("အကျိုးမဲ့ စကားကို", "ပြောရာ"),
    "sandhiṃ chindeyya": ("အိမ်ကို", "ဖောက်ရာ"), "nillopaṃ hareyya": ("ဥစ္စာကို", "လုယူရာ"),
    "ekāgāriyaṃ kareyya": ("အိမ်တစ်လုံးတည်းကို ဝိုင်း၍", "တိုက်ရာ"),
    "paripanthe tiṭṭheyya": ("လမ်းခရီး၌ ဓားပြ", "တိုက်ရာ"),
    "paradāraṃ gaccheyya": ("သူတစ်ပါး၏ မယားထံ", "သွားရာ"),
    "gāmaghātaṃ kareyya": ("ရွာကို ဖျက်ဆီး၍", "လုယက်ရာ"), "nigamaghātaṃ kareyya": ("နိဂုံးကို ဖျက်ဆီး၍", "လုယက်ရာ"),
}
for _k, (_o, _v) in ACTS.items():
    new(_k, f"{_o} {_v}")
SUBJ10 = {"arahā": f"{ARAHA}သည်", "puthujjano": f"{PUTHU}သည်"}
_ACT_SEP = re.compile(r"(, |… )")


@F.rule(r"(?:atthi (?P<g>\S+) (?P<x>\S+(?: \S+)?), )?(?P<na>na ca )?(?P<s>arahā|puthujjano)"
        r"(?P<ap> aññāṇapakato)? (?P<acts>.+)")
def _r_acts(m):
    """(atthi G X,) (na ca) S (aññāṇapakato) act, act…pe… act: «… Sသည် (မသိခြင်းဖြင့် လွှမ်းမိုးခံရ၍) …(မ)…ရာ»."""
    parts = _ACT_SEP.split(m["acts"])
    acts, seps = parts[0::2], parts[1::2]
    if any(a not in ACTS for a in acts):
        return None
    neg = bool(m["na"])
    words = []
    for a in acts[:-1]:
        o, v = ACTS[a]
        words.append(f"{o} {'မ' + v if neg else v}")
    out = ""
    for w, sp in zip(words, seps):
        out += w + (PE + " " if "…" in sp else f"{C} ")
    o, v = ACTS[acts[-1]]
    pre = ""
    if m["g"]:
        if m["g"] not in GEN or lst(m["x"]) is None:
            return None
        pre = f"{GEN[m['g']]} {lst(m['x'])} {EXIST}သည်{C} "
    ap = f" {ANNANA}ဖြင့် လွှမ်းမိုးခံရ၍" if m["ap"] else ""
    return Cl(f"{pre}{SUBJ10[m['s']]}{ap} {out}{o}", v, "မ" + v, neg=neg)


new("aññāṇapakato", f"{ANNANA}ဖြင့် လွှမ်းမိုးခံရ၍")
# kilesa abandoned / path developed (arahato …)
KIL_PAH = {"rāgo": "rāga", "doso": "dosa", "moho": "moha", "māno": None, "diṭṭhi": None, "vicikicchā": None,
           "thinaṃ": None, "uddhaccaṃ": None, "ahirikaṃ": None, "anottappaṃ": "anottappa"}
_PAH = {"rāgo": "pahīno", "doso": "pahīno", "moho": "pahīno", "māno": "pahīno", "diṭṭhi": "pahīnā",
        "vicikicchā": "pahīnā", "thinaṃ": "pahīnaṃ", "uddhaccaṃ": "pahīnaṃ", "ahirikaṃ": "pahīnaṃ",
        "anottappaṃ": "pahīnaṃ"}
_UCCH = {"pahīno": "ucchinnamūlo tālāvatthukato anabhāvaṅkato āyatiṃ anuppādadhammo",
         "pahīnaṃ": "ucchinnamūlaṃ tālāvatthukataṃ anabhāvaṅkataṃ āyatiṃ anuppādadhammaṃ"}
UCCH_MY = ("အမြစ် ပြတ်ပြီး၊ ထန်းငုတ်ကဲ့သို့ ပြုထားပြီး၊ ပျောက်ပျက်အောင် ပြုထားပြီး ဖြစ်၍ နောင်အခါ မဖြစ်ပေါ်နိုင်သော "
           "သဘော")
new("pahīno ucchinnamūlo tālāvatthukato anabhāvaṅkato āyatiṃ anuppādadhammo", f"ပယ်ပြီး၊ {UCCH_MY}")
PAHINA = ("ပယ်ပြီး", "မပယ်ရသေး")
BHAVITA = ("ပွားများပြီး", "မပွားများရသေး")
OWN = {"": "", "arahato": f"{ARAHA}သည် ", "sadhammakusalassa arahato": f"{SADH}သည် ",
       "paradhammakusalassa arahato": f"{PARA}သည် "}
GRP = {"maggo": ("bhāvito", "မဂ်"), "satipaṭṭhānā": ("bhāvitā", SATIPATTHANA), "sammappadhānā": ("bhāvitā", _SP),
       "iddhipādā": ("bhāvitā", _ID), "indriyā": ("bhāvitā", F.INDRIYA_W), "balā": ("bhāvitā", "စွမ်းအား"),
       "bojjhaṅgā": ("bhāvitā", _BJW)}
for _o, _om in OWN.items():
    _op = _o + " " if _o else ""
    for _k, _km in KIL.items():
        PROP_X[f"{_op}{_k} {_PAH[_k]}"] = Cl(f"{_om}{_km}ကို", *PAHINA)
        if _PAH[_k] in _UCCH:
            PROP_X[f"{_op}{_k} {_PAH[_k]} {_UCCH[_PAH[_k]]}"] = V(f"{_om}{_km}ကို ပယ်ပြီး၊ {UCCH_MY}")
        if KIL_PAH[_k]:
            _st = KIL_PAH[_k]
            _pp = f"{_st}ppahānāya" if _st != "anottappa" else "anottappapahānāya"
            PROP_X[f"{_op}{_pp}"] = FR(f"{_om}{_km}ကို ပယ်ရန်")
            for _g, (_b, _gm) in GRP.items():
                PROP_X[f"{_op}{_pp} {_g} {_b}"] = Cl(f"{_om}{_km}ကို ပယ်ရန် {_gm}ကို", *BHAVITA)
    for _g, (_b, _gm) in GRP.items():
        if not _o:
            PROP_X[f"{_g} {_b}"] = Cl(f"{_gm}ကို", *BHAVITA)
PROP_X["dosappahānāya mohappahānāya"] = FR(f"{KIL['doso']}ကို ပယ်ရန်၊ {KIL['moho']}ကို ပယ်ရန်")
new("Xppahānāya maggo bhāvito", f"Xကို ပယ်ရန် မဂ်ကို {BHAVITA[0]}")
EPI = [("vītarāgo", "ရာဂ ကင်းသူ"), ("vītadoso", "ဒေါသ ကင်းသူ"), ("vītamoho", "မောဟ ကင်းသူ"),
       ("katakaraṇīyo", "ပြုဖွယ်ကိစ္စကို ပြုပြီးသူ"), ("ohitabhāro", "ဝန်ကို ချထားပြီးသူ"),
       ("anuppattasadattho", "မိမိ၏ အကျိုးသို့ ရောက်ပြီးသူ"),
       ("parikkhīṇabhavasaṃyojano", "ဘဝ နှောင်ကြိုး ကုန်ခန်းပြီးသူ"),
       ("sammadaññāvimutto", "မှန်ကန်စွာ သိ၍ လွတ်မြောက်ပြီးသူ"),
       ("ukkhittapaligho", "တံခါး ကန့်လန့်ကို ဖယ်ရှားပြီးသူ"), ("saṅkiṇṇaparikho", "ကျုံးကို ဖို့ပြီးသူ"),
       ("abbūḷhesiko", "တိုင်ကို နုတ်ပြီးသူ"), ("niraggaḷo", "တံခါး ဂျက်ကို ဖြုတ်ပြီးသူ"), ("ariyo", "အရိယာ"),
       ("pannaddhajo", "အလံကို ချပြီးသူ"), ("pannabhāro", "ဝန်ထုပ်ကို ပစ်ချပြီးသူ"),
       ("visaññutto", "နှောင်ကြိုးမှ ကင်းလွတ်ပြီးသူ"), ("suvijitavijayo", "အောင်ပွဲကို ကောင်းစွာ အောင်ပြီးသူ")]
for _k, _m in EPI:
    new(_k, _m)
EPI_MY = f"{C} ".join(m for _, m in EPI)
EPI_PI = " ".join(k for k, _ in EPI)
TRUTH10 = [("dukkhaṃ tassa pariññātaṃ", "ထိုသူသည် ဒုက္ခကို ပိုင်းခြား သိပြီး"),
           ("samudayo pahīno", "ဖြစ်ပေါ်ခြင်းကို ပယ်ပြီး"), ("nirodho sacchikato", "ချုပ်ငြိမ်းခြင်းကို မျက်မှောက်ပြုပြီး"),
           ("maggo bhāvito", "မဂ်ကို ပွားများပြီး"),
           ("abhiññeyyaṃ abhiññātaṃ", "ထူးကဲစွာ သိရမည့် အရာကို ထူးကဲစွာ သိပြီး"),
           ("pariññeyyaṃ pariññātaṃ", "ပိုင်းခြား သိရမည့် အရာကို ပိုင်းခြား သိပြီး"),
           ("pahātabbaṃ pahīnaṃ", "ပယ်ရမည့် အရာကို ပယ်ပြီး"),
           ("bhāvetabbaṃ bhāvitaṃ", "ပွားများရမည့် အရာကို ပွားများပြီး")]
SACCHI = ("မျက်မှောက်ပြုပြီး", "မျက်မှောက် မပြုရသေး")
_TR_MY = f"{C} ".join(m for _, m in TRUTH10)
_TR_PI = ", ".join(k for k, _ in TRUTH10)
for _s, _sm in (("arahā", f"{ARAHA}သည်"), ("nanu arahā", f"{ARAHA}သည်"), ("sadhammakusalo arahā", f"{SADH}သည်"),
                ("paradhammakusalo arahā", f"{PARA}သည်")):
    PROP_X[f"{_s} {EPI_PI}, {_TR_PI}, sacchikātabbaṃ sacchikataṃ"] = Cl(
        f"{_sm} {EPI_MY}{C} {_TR_MY}{C} မျက်မှောက်ပြုရမည့် အရာကို", *SACCHI)
    for _n in (1, 3, 4):
        PROP_X[f"{_s} {' '.join(k for k, _ in EPI[:_n])}"] = FR(f"{_sm} " + f"{C} ".join(m for _, m in EPI[:_n]))
PROP_X["sacchikātabbaṃ sacchikataṃ"] = Cl("မျက်မှောက်ပြုရမည့် အရာကို", *SACCHI)
new("dukkhaṃ tassa pariññātaṃ … sacchikātabbaṃ sacchikataṃ", f"{_TR_MY}၊ မျက်မှောက်ပြုရမည့် အရာကို {SACCHI[0]}")
REF_X = {"mahāva.": "“မဟာဝဂ်”", "udā.": "“ဥဒါန်း”"}
REF_NOTE_X = {"atthato samānaṃ": "အဓိပ္ပာယ်အားဖြင့် တူသည်", "passitabbaṃ": "ကြည့်ပါ", "udānepi": "“ဥဒါန်း”၌လည်း"}
QUOTE_X["ye te, bhikkhave, bhikkhū puthujjanā sīlasampannā satā sampajānā niddaṃ okkamanti, tesaṃ asuci na muccati. "
        "Yepi te, bhikkhave, bāhirakā isayo kāmesu vītarāgā, tesampi asuci na muccati. Aṭṭhānametaṃ, bhikkhave, "
        "anavakāso yaṃ arahato asuci mucceyyā"] = (
    f"ရဟန်းတို့၊ သီလ ပြည့်စုံ၍ သတိ ရှိကြ၊ ကောင်းစွာ ဆင်ခြင်သိမြင်ကြလျက် အိပ်ပျော်သွားကြသော {PUTHU} ရဟန်း "
    "အကြင်သူတို့ ⟦b⟧ ရှိကြ၏၊ ထိုသူတို့၏ မစင်ကြယ်သော သုက် မထွက်။ ရဟန်းတို့၊ ကာမတို့၌ ရာဂ ကင်းကြသော သာသနာပ "
    f"ရသေ့ အကြင်သူတို့ ရှိကြ၏၊ ထိုသူတို့၏လည်း မစင်ကြယ်သော သုက် မထွက်။ ရဟန်းတို့၊ {ARAHA}၏ မစင်ကြယ်သော သုက် "
    "ထွက်ရာသည် ဟူသော ဤအရာသည် အကြောင်း မဟုတ်၊ အခွင့် မဟုတ်")
VAR_X10 = {"ye keci": F.PATHA, "methunaṃ dhammaṃ uppādeyya": F.PATHA}
PROP_X["arahato cīvarapiṇḍapātasenāsanagilānapaccayabhesajjaparikkhāraṃ pare upasaṃhareyyuṃ"] = Cl(
    f"{ARAHA}အား သင်္ကန်း၊ ဆွမ်း၊ ကျောင်းအိပ်ရာနေရာ၊ သူနာ၏ အထောက်အပံ့ ဖြစ်သော ဆေးအသုံးအဆောင်ကို "
    "သူတစ်ပါးတို့က", "ဆောင်ယူပေးကြရာ", "ဆောင်ယူ မပေးကြရာ")
W("2", "^2-929", "Itarītaracīvarapiṇḍapātasenāsanagilānapaccayabhesajjaparikkhārehi",
  "သင်္ကန်း၊ ဆွမ်း၊ ကျောင်းအိပ်ရာနေရာ၊ သူနာ၏ အထောက်အပံ့ ဖြစ်သော ဆေးအသုံးအဆောင်")
FRUIT = {"sotāpattiphal": "သောတာပတ္တိဖိုလ်", "sakadāgāmiphal": "သကဒါဂါမိဖိုလ်", "anāgāmiphal": "အနာဂါမိဖိုလ်",
         "arahatt": "ရဟန္တာ ဖိုလ်"}
W("2", "^2-807", "sotāpattiphale", "သောတာပတ္တိဖိုလ်")
W("1", "^1-1024", "arahattaphalaṃ", "ရဟန္တာ ဖိုလ်")
_FR4 = "ကိုဖြစ်စေ၊ ".join(FRUIT.values()) + "ကိုဖြစ်စေ"
_FR4_LOC = "၌ဖြစ်စေ၊ ".join(FRUIT.values()) + "၌ဖြစ်စေ"
PROP_X["arahato sotāpattiphalaṃ vā sakadāgāmiphalaṃ vā anāgāmiphalaṃ vā arahattaṃ vā pare upasaṃhareyyuṃ"] = Cl(
    f"{ARAHA}အား {_FR4} သူတစ်ပါးတို့က", "ဆောင်ယူပေးကြရာ", "ဆောင်ယူ မပေးကြရာ")
section("(10) 1. Parūpahārakathā", f"(10) 1. သူတစ်ပါးက ဆောင်ယူပေးခြင်းအကြောင်း {KATHA}")
HEAD_X["(10) 1. Parūpahārakathā"] = f"(10) 1. သူတစ်ပါးက ဆောင်ယူပေးခြင်းအကြောင်း {KATHA}"
section("Parūpahārakathā", f"သူတစ်ပါးက ဆောင်ယူပေးခြင်းအကြောင်း {KATHA}")


# ===================================================================================== 10. kathās 11-13 (Aññāṇa, Kaṅkhā, Paravitāraṇā)
section("(11) 2. Aññāṇakathā", f"(11) 2. မသိခြင်းအကြောင်း {KATHA}")
section("Aññāṇakathā", f"မသိခြင်းအကြောင်း {KATHA}")
section("(12) 3. Kaṅkhākathā", f"(12) 3. သံသယအကြောင်း {KATHA}")
section("Kaṅkhākathā", f"သံသယအကြောင်း {KATHA}")
section("(13) 4. Paravitāraṇakathā", f"(13) 4. သူတစ်ပါးက ရှင်းပြပေးခြင်းအကြောင်း {KATHA}")
section("Paravitāraṇakathā", f"သူတစ်ပါးက ရှင်းပြပေးခြင်းအကြောင်း {KATHA}")
PVT = new("paravitāraṇā", "သူတစ်ပါးက ရှင်းပြပေးခြင်း")
LST["paravitāraṇā"] = PVT
for _o, _om in OBJ10.items():
    LST[f"{_o} paravitāraṇā"] = f"{_om} {PVT}"
LST["idapaccayatāpaṭiccasamuppannesu dhammesu paravitāraṇā"] = LST[
    "idappaccayatāpaṭiccasamuppannesu dhammesu paravitāraṇā"]           # source slip (idapaccayatā)
KNOW = "သိသူ၊ မြင်သူ"                                                  # jānato passato
AK = F.ASAVAKHAYA                                                    # «စိတ်အစွန်းအထင်းတို့ ကုန်ခန်းခြင်း»
_J_HEAD = (f"ရဟန်းတို့၊ ငါသည် {KNOW}၏ {AK}ကို ဟော၏၊ မသိသူ၊ မမြင်သူ၏ {AK}ကို မဟော{{e}} ရဟန်းတို့၊ အဘယ်ကို "
           f"သိသူ၊ အဘယ်ကို မြင်သူ၏ {AK} ဖြစ်သနည်း။ ")
_J_END = f"ရဟန်းတို့၊ ဤသို့ သိသူ၊ ဤသို့ မြင်သူ၏ {AK} ဖြစ်၏"
_ATTH = "ချုပ်ငြိမ်းသွားခြင်း"                                       # atthaṅgamo (pi-1 «… ချုပ်ငြိမ်းသွားခြင်းကြောင့်»)
_SAM = "ဖြစ်ပေါ်ခြင်း"                                               # samudayo (termbase)
_RU, _VI = F.RUPA.my, F.VINNANA.my
_J_KH = (f"‹ဤကား {_RU}၊ ဤကား {_RU}၏ {_SAM}၊ ဤကား {_RU}၏ {_ATTH}၊ ဤကား {F.VEDANA.my}… ဤကား {F.SANNA.my}… ဤကား "
         f"{F.SANKHARA.my}… ဤကား {_VI}၊ ဤကား {_VI}၏ {_SAM}၊ ဤကား {_VI}၏ {_ATTH}›ဟု – ")
_J_KH_S = f"‹ဤကား {_RU}›… ‹ဤကား {_VI}၏ {_ATTH}›ဟု – "
_JP = "jānatohaṃ, bhikkhave, passato āsavānaṃ khayaṃ vadāmi, no ajānato no apassato{e} Kiñca, bhikkhave, jānato kiṃ passato āsavānaṃ khayo hoti? "
QUOTE_X[_JP.format(e=".") + "Iti rūpaṃ, iti rūpassa samudayo, iti rūpassa atthaṅgamo, iti vedanā… iti saññā… iti "
        "saṅkhārā… iti viññāṇaṃ, iti viññāṇassa samudayo, iti viññāṇassa atthaṅgamoti – evaṃ kho, bhikkhave, jānato "
        "evaṃ passato āsavānaṃ khayo hotī"] = _J_HEAD.format(e="။") + _J_KH + _J_END
QUOTE_X[_JP.format(e="!") + "Iti rūpaṃ… iti viññāṇassa atthaṅgamoti – evaṃ kho, bhikkhave, jānato evaṃ passato "
        "āsavānaṃ khayo hotī"] = _J_HEAD.format(e="။") + _J_KH_S + _J_END
_DK = "ဒုက္ခ"
_TRU = {"idaṃ dukkhan": f"ဤကား {_DK}", "ayaṃ dukkhasamudayo": f"ဤကား {_DK} ဖြစ်ပေါ်ခြင်း",
        "ayaṃ dukkhanirodho": f"ဤကား {_DK} ချုပ်ငြိမ်းခြင်း",
        "ayaṃ dukkhanirodhagāminī paṭipadā": f"ဤကား {_DK} ချုပ်ငြိမ်းခြင်းသို့ ရောက်ကြောင်း အကျင့်"}
new("dukkhasamudayo / dukkhanirodho / dukkhanirodhagāminī paṭipadā",
    " / ".join(list(_TRU.values())[1:]).replace("ဤကား ", ""))
_JKP = f"{KNOW}၏ {AK} ဖြစ်၏"
_t = list(_TRU.values())
QUOTE_X[_JP.format(e=".") + "Idaṃ dukkhanti – bhikkhave, jānato passato āsavānaṃ khayo hoti, ayaṃ dukkhasamudayoti – "
        "jānato passato āsavānaṃ khayo hoti, ayaṃ dukkhanirodhoti – jānato passato āsavānaṃ khayo hoti, ayaṃ "
        "dukkhanirodhagāminī paṭipadāti – jānato passato āsavānaṃ khayo hoti. Evaṃ kho, bhikkhave, jānato evaṃ "
        "passato āsavānaṃ khayo hotī"] = (
    _J_HEAD.format(e="။") + f"‹{_t[0]}›ဟု – ရဟန်းတို့၊ {_JKP}၊ ‹{_t[1]}›ဟု – {_JKP}၊ ‹{_t[2]}›ဟု – {_JKP}၊ "
    f"‹{_t[3]}›ဟု – {_JKP}။ " + _J_END)
QUOTE_X[_JP.format(e="!") + "Idaṃ dukkhanti, bhikkhave… ayaṃ dukkhanirodhagāminī paṭipadāti jānato passato "
        "āsavānaṃ khayo hoti. Evaṃ kho, bhikkhave, jānato evaṃ passato āsavānaṃ khayo hotī"] = (
    _J_HEAD.format(e="။") + f"‹{_t[0]}›ဟု ရဟန်းတို့… ‹{_t[3]}›ဟု {_JKP}။ " + _J_END)
QUOTE_X[_JP.format(e="!") + "Idaṃ dukkhanti – bhikkhave, jānato passato āsavānaṃ khayo hoti, ayaṃ dukkhasamudayoti… "
        "ayaṃ dukkhanirodhoti… ayaṃ dukkhanirodhagāminī paṭipadāti – jānato passato āsavānaṃ khayo hoti. Evaṃ kho, "
        "bhikkhave, jānato evaṃ passato āsavānaṃ khayo hotī"] = (
    _J_HEAD.format(e="။") + f"‹{_t[0]}›ဟု – ရဟန်းတို့၊ {_JKP}၊ ‹{_t[1]}›ဟု… ‹{_t[2]}›ဟု… ‹{_t[3]}›ဟု – "
    f"{_JKP}။ " + _J_END)
_SB1 = ("ရဟန်းတို့၊ အလုံးစုံကို ထူးကဲစွာ မသိဘဲ၊ ပိုင်းခြား မသိဘဲ၊ တပ်မက်မှုကို မကင်းစေဘဲ၊ မပယ်ဘဲ နေသူသည် "
        "ဒုက္ခ ကုန်ခန်းရန် မထိုက်တန်")
_SB2 = ("ရဟန်းတို့၊ အလုံးစုံကို ထူးကဲစွာ သိ၍၊ ပိုင်းခြား သိ၍၊ တပ်မက်မှုကို ကင်းစေ၍၊ ပယ်၍ နေသူသည် ဒုက္ခ ကုန်ခန်းရန် "
        "ထိုက်တန်၏")
for _sep in (", ", "; "):
    QUOTE_X[f"sabbaṃ, bhikkhave, anabhijānaṃ aparijānaṃ avirājayaṃ appajahaṃ abhabbo dukkhakkhayāya{_sep}sabbañca kho, "
            "bhikkhave, abhijānaṃ parijānaṃ virājayaṃ pajahaṃ bhabbo dukkhakkhayāyā"] = f"{_SB1}{C} {_SB2}"
_SAKK = W("2", "^2-915", "sakkāyadiṭṭhi", "ကိုယ်ကို အတ္တဟု ယူဆသော အယူ")
_SILA = "သီလ အကျင့်ဝတ်ဆိုင်ရာ မှားယွင်းသော ယူဆမှု"
W("2", "^2-915", "sīlabbataparāmāso", _SILA)
VERSE_SAHA = [
    ("Sahāvassa dassanasampadāya,", "“သစ္စာကို မြင်ခြင်း ပြည့်စုံသည်နှင့် တပြိုင်နက်"),
    ("Tayassu dhammā jahitā bhavanti;", "ထိုသူ၏ တရား သုံးပါးတို့ကို ပယ်ပြီး ဖြစ်ကြ၏၊"),
    ("Sakkāyadiṭṭhī vicikicchitañca,", f"{_SAKK}နှင့် ယုံမှားခြင်း၊"),
    ("Sīlabbataṃ vāpi yadatthi kiñci;", "သီလ အကျင့်ဝတ် တစ်စုံတစ်ရာ ရှိသမျှလည်း ဖြစ်၏၊"),
    ("Catūhapāyehi ca vippamutto,", "အပါယ် လေးပါးတို့မှလည်း လွတ်မြောက်၏၊"),
    ("Chaccābhiṭhānāni abhabba kātunti.", "ကြီးလေးသော အမှု ခြောက်ပါးတို့ကို ပြုရန်လည်း မထိုက်တန်”။"),
]
for _k, _m in VERSE_SAHA:
    LINES_X[_k] = _m
LINES_X["Sahāvassa dassanasampadāya,"] += C
QUOTE_X["sahāvassa dassanasampadāya… chaccābhiṭhānāni abhabba kātun"] = (
    "သစ္စာကို မြင်ခြင်း ပြည့်စုံသည်နှင့် တပြိုင်နက်… ကြီးလေးသော အမှု ခြောက်ပါးတို့ကို ပြုရန်လည်း မထိုက်တန်")
_DC = (f"ရဟန်းတို့၊ အကြင် အချိန်၌ အရိယာ တပည့်အား မြူမှုန် ကင်းသော၊ အညစ်အကြေး ကင်းသော တရားမျက်စိ ဖြစ်ပေါ်လာ၏ – "
       f"‹ဖြစ်ပေါ်ခြင်း သဘော ရှိသော အရာ မှန်သမျှ အားလုံးသည် ချုပ်ငြိမ်းခြင်း သဘော ရှိ၏›ဟု၊ ရဟန်းတို့၊ မြင်ခြင်း "
       f"ဖြစ်ပေါ်သည်နှင့် တပြိုင်နက် အရိယာ တပည့်၏ နှောင်ကြိုး သုံးပါးတို့ကို ပယ်ရ၏ – {_SAKK}၊ {_VC}၊ {_SILA}")
for _y in ("yaṃ kiñci samudayadhammaṃ sabbaṃ taṃ nirodhadhammanti", "yaṃ kiñci samudayadhammaṃ, sabbaṃ taṃ nirodhadhammanti"):
    QUOTE_X["yasmiṃ, bhikkhave, samaye ariyasāvakassa virajaṃ vītamalaṃ dhammacakkhuṃ udapādi – " + _y + ", saha "
            "dassanuppādā, bhikkhave, ariyasāvakassa tīṇi saṃyojanāni pahīyanti – sakkāyadiṭṭhi, vicikicchā, "
            "sīlabbataparāmāso"] = _DC
IPN = "မိန်းမ ယောက်ျားတို့၏ အမည်နှင့် အနွယ်"                          # itthipurisānaṃ nāmagotta
MAM = "လမ်း ဟုတ် မဟုတ်"                                              # maggāmagga
TKV = "မြက်၊ ထင်း၊ သစ်ပင်တို့၏ အမည်"                                 # tiṇakaṭṭhavanappatīnaṃ nāmaṃ
assert MS.THING["tiṇakaṭṭhavanappatayo"][0] == "မြက်၊ ထင်း၊ သစ်ပင်တို့"
_JN = ("သိရာ", "မသိရာ")
PROP_X["arahā itthipurisānaṃ nāmagottaṃ na jāneyya, maggāmaggaṃ na jāneyya, tiṇakaṭṭhavanappatīnaṃ nāmaṃ na "
       "jāneyya"] = Cl(f"{ARAHA}သည် {IPN}ကို {_JN[1]}၊ {MAM}ကို {_JN[1]}၊ {TKV}ကို", *_JN, neg=True)
PROP_X["arahā sotāpattiphalaṃ vā sakadāgāmiphalaṃ vā anāgāmiphalaṃ vā arahattaṃ vā na jāneyya"] = Cl(
    f"{ARAHA}သည် {_FR4}", *_JN, neg=True)
_KK = ("သံသယ ဖြစ်ရာ", "သံသယ မဖြစ်ရာ")
PROP_X["arahā itthipurisānaṃ nāmagotte kaṅkheyya, maggāmagge kaṅkheyya, tiṇakaṭṭhavanappatīnaṃ nāme kaṅkheyya"] = Cl(
    f"{ARAHA}သည် {IPN}၌ {_KK[0]}၊ {MAM}၌ {_KK[0]}၊ {TKV}၌", *_KK)
PROP_X["arahā sotāpattiphale vā sakadāgāmiphale vā anāgāmiphale vā arahatte vā kaṅkheyya"] = Cl(
    f"{ARAHA}သည် {_FR4_LOC}", *_KK)
_VT = ("ရှင်းပြပေးကြရာ", "ရှင်းပြ မပေးကြရာ")
PROP_X["arahato itthipurisānaṃ nāmagottaṃ pare vitāreyyuṃ, maggāmaggaṃ pare vitāreyyuṃ, tiṇakaṭṭhavanappatīnaṃ "
       "nāmaṃ pare vitāreyyuṃ"] = Cl(
    f"{ARAHA}အား {IPN}ကို သူတစ်ပါးတို့က {_VT[0]}၊ {MAM}ကို သူတစ်ပါးတို့က {_VT[0]}၊ {TKV}ကို သူတစ်ပါးတို့က", *_VT)
PROP_X["arahato sotāpattiphalaṃ vā sakadāgāmiphalaṃ vā anāgāmiphalaṃ vā arahattaṃ vā pare vitāreyyuṃ"] = Cl(
    f"{ARAHA}အား {_FR4} သူတစ်ပါးတို့က", *_VT)
_PN4 = ["သူတစ်ပါး လမ်းပြရသူ", "သူတစ်ပါးကို ယုံကြည်ရသူ", "သူတစ်ပါးကို အားကိုးရသူ", "သူတစ်ပါးနှင့် ချည်နှောင်နေသူ"]
_PN4_PI = "paraneyyo parapattiyo parapaccayo parapaṭibaddhabhū"
_PN4_NA = "na paraneyyo na parapattiyo na parapaccayo na parapaṭibaddhabhū"
_NJ = "မသိ၊ မမြင်၊ တွေဝေ၍ ကောင်းစွာ ဆင်ခြင်သိမြင်ခြင်း ကင်းသူ"          # na jānāti na passati sammūḷho asampajāno
_JJ = "သိ၏၊ မြင်၏၊ မတွေဝေ၊ ကောင်းစွာ ဆင်ခြင်သိမြင်သူ"                 # jānāti passati asammūḷho sampajāno
for _k in _PN4_PI.split():
    pass
for _s, _sm in (("arahā", f"{ARAHA}သည်"), ("so ca", "ထိုသူသည်လည်း")):
    PROP_X[f"{_s} {_PN4_PI}"] = V(f"{_sm} {C.join([' ' + x for x in _PN4]).strip()}".replace("  ", " "))
    PROP_X[f"{_s} {_PN4_NA}"] = V(f"{_sm} " + f" မဟုတ်{C} ".join(_PN4), neg=True)
PROP_X["arahā paraneyyo parapattiyo parapaccayo parapaṭibaddhabhū"] = V(f"{ARAHA}သည် " + f"{C} ".join(_PN4))
PROP_X["so ca paraneyyo parapattiyo parapaccayo parapaṭibaddhabhū"] = V("ထိုသူသည်လည်း " + f"{C} ".join(_PN4))
PROP_X["na jānāti na passati sammūḷho asampajāno"] = V(_NJ)
PROP_X["jānāti passati asammūḷho sampajāno"] = V(_JJ)
PROP_X[f"arahā {_PN4_NA} jānāti passati asammūḷho sampajāno"] = V(
    f"{ARAHA}သည် " + f" မဟုတ်{C} ".join(_PN4) + f" မဟုတ်{C} {_JJ}")
for _k, _m in zip(_PN4_PI.split(), _PN4):
    new(_k, _m)
new("na jānāti na passati sammūḷho asampajāno", _NJ)
REF_NOTE_X.update({"suttanipāte": "“သုတ္တနိပါတ်”၌",
                   "dhotakamāṇavapucchāniddesa": "ဓောတက လုလင်၏ အမေးကို ဖွင့်ဆိုချက်"})
VAR_X10.update({"jānatāhaṃ": F.LEKHANA, "jānatvāhaṃ": F.PATHA, "gamissāmi": F.PATHA, "samīhāmi": F.PATHA,
                "kiñci": F.LEKHANA})
LINES_X["Nāhaṃ sahissāmi pamocanāya,"] = "“ဓောတက၊ ငါသည် ⟦0⟧ လောက၌ ယုံမှားသံသယ ရှိသူ"
LINES_X["Kathaṅkathiṃ dhotaka kañci loke;"] = "တစ်စုံတစ်ယောက်ကိုမျှ ⟦0⟧ လွတ်မြောက်စေရန် မတတ်နိုင်၊"
LINES_X["Dhammañca seṭṭhaṃ abhijānamāno,"] = "မြတ်သော တရားကို ထူးကဲစွာ သိလျက်"
LINES_X["Evaṃ tuvaṃ oghamimaṃ taresīti."] = "သင်သည် ဤသို့ ဤရေအလျဉ်ကို ကူးမြောက်ရာ၏”ဟူ၍ ⟦0⟧။"

# ===================================================================================== 10. kathā 14 (Vacībheda)
section("(14) 5. Vacībhedakathā", f"(14) 5. နှုတ်ဖြင့် စကား ထွက်ခြင်းအကြောင်း {KATHA}")
section("Vacībhedakathā", f"နှုတ်ဖြင့် စကား ထွက်ခြင်းအကြောင်း {KATHA}")
VB = new("vacībhedo", "နှုတ်ဖြင့် စကား ထွက်ခြင်း")
KB = new("kāyabhedo", "ကိုယ်ကို လှုပ်ရှားခြင်း")
VACA = "စကား"
SAMAP = new("samāpannassa", "သမာပတ်ကို ဝင်စားနေသူ")
VV2 = "စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှု"                            # vitakkavicārā
LST.update({"vacībhedo": VB, "kāyabhedo": KB, "vācā": VACA, "kāyo": F.KAYA, "vitakkavicārā": VV2,
            "saññā": F.SANNA.my, "saññā ca vedanā ca": f"{F.SANNA.my}နှင့် {F.VEDANA.my}"})
GEN.update({"samāpannassa": f"{SAMAP}၌", "sabbattha samāpannānaṃ": f"နေရာတိုင်း၌ {SAMAP}တို့၌",
            "sabbadā samāpannānaṃ": f"အချိန်တိုင်း၌ {SAMAP}တို့၌", "sabbesaṃ samāpannānaṃ": f"{SAMAP} အားလုံးတို့၌",
            "sabbasamāpattīsu": "သမာပတ် အားလုံးတို့၌"})
for _x in ("vacībhedo", "kāyabhedo", "vitakkavicārā"):
    PROP_X[f"atthi {_x}"] = V(LST[_x], EXIST)
    PROP_X[f"natthi {_x}"] = V(LST[_x], EXIST, neg=True)
JH = "ဈာန်"
LOKIYA, LOKUTTARA = "လောကနှင့် သက်ဆိုင်သော", "လောကကို ကျော်လွန်သော"
ORDJ = {"paṭhamaṃ": F.ORD_MY[1], "dutiyaṃ": F.ORD_MY[2], "tatiyaṃ": F.ORD_MY[3], "catutthaṃ": F.ORD_MY[4]}
KAS = {"pathavī": "မြေ", "āpo": "ရေ", "tejo": "မီး", "vāyo": "လေ", "nīla": "အပြာ", "pīta": "အဝါ", "lohita": "အနီ",
       "odāta": "အဖြူ"}
W("1", "^1-165", "pathavīkasiṇaṃ", "မြေ ကသိုဏ်း")
ARUPA4 = {"ākāsānañcāyatanaṃ": "အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ်", "viññāṇañcāyatanaṃ": "အဆုံး မရှိသော သိစိတ် နယ်ပယ်",
          "ākiñcaññāyatanaṃ": "ဘာမျှ မရှိသော နယ်ပယ်",
          "nevasaññānāsaññāyatanaṃ": "မှတ်သိမှု ရှိသည်လည်း မဟုတ်၊ မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ်"}
W("1", "^1-1432", "Viññāṇañcāyatanaṃ, nevasaññānāsaññāyatanaṃ",
  "အဆုံး မရှိသော သိစိတ် နယ်ပယ်၊ မှတ်သိမှု ရှိသည်လည်း မဟုတ်၊ မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ်")
ATT = {}         # attainment (accusative, before «samāpannassa») -> Burmese object
for _j, _jm in ORDJ.items():
    ATT[f"{_j} jhānaṃ"] = f"{_jm} {JH}"
    ATT[f"lokiyaṃ {_j} jhānaṃ"] = f"{LOKIYA} {_jm} {JH}"
    ATT[f"lokuttaraṃ {_j} jhānaṃ"] = f"{LOKUTTARA} {_jm} {JH}"
for _k, _km in KAS.items():
    ATT[f"{_k}kasiṇaṃ"] = f"{_km} ကသိုဏ်း"
    ATT[f"{_k}kasiṇaṃ samāpattiṃ"] = f"{_km} ကသိုဏ်း သမာပတ်"
    ATT[f"{_k}kasiṇaṃ paṭhamaṃ jhānaṃ"] = f"{_km} ကသိုဏ်း ပထမ {JH}"
ATT.update(ARUPA4)
ATT["lokiyasamāpattiṃ"] = ATT["lokiyaṃ samāpattiṃ"] = f"{LOKIYA} သမာပတ်"
ATT["saññāvedayitanirodhaṃ"] = "မှတ်သိမှုနှင့် ခံစားမှု ချုပ်ငြိမ်းခြင်း သမာပတ်"
for _a, _am in ATT.items():
    GEN[f"{_a} samāpannassa"] = f"{_am}ကို ဝင်စားနေသူ၌"
    PROP_X[_a] = FR(_am)
for _j in ("dutiyaṃ", "tatiyaṃ", "catutthaṃ"):
    PROP_X[f"{_j} jhānaṃ"] = FR(ATT[f"{_j} jhānaṃ"])
TRUTH14 = {"dukkhan": _DK, "samudayo": "ဖြစ်ပေါ်ခြင်း", "nirodho": "ချုပ်ငြိမ်းခြင်း",
           "maggo": "မဂ်"}
for _k, _m in TRUTH14.items():
    PROP_X[f"{_k}ti jānanto {_k}ti vācaṃ bhāsati"] = Cl(f"{_m}ဟု သိလျက် {_m}ဟူသော {VACA}ကို", "ပြော", "မပြော")
    PROP_X[f"{_k}ti jānanto na ca {_k}ti vācaṃ bhāsati"] = Cl(f"{_m}ဟု သိလျက် {_m}ဟူသော {VACA}ကို", "ပြော",
                                                               "မပြော", neg=True)
_GOC = ("ကျက်စားရာ ပြု", "ကျက်စားရာ မပြု")
SENT_X["Ñāṇaṃ kiṃgocaranti?"] = f"ဉာဏ်သည် အဘယ်အရာကို ကျက်စားရာ ပြုသနည်း{END}"
SENT_X["Sotaṃ kiṃ gocaranti?"] = f"နားသည် အဘယ်အရာကို ကျက်စားရာ ပြုသနည်း{END}"
for _a, _am in (("ñāṇaṃ", "ဉာဏ်"), ("sotaṃ", "နား")):
    for _b, _bm in (("sacca", "သစ္စာ"), ("sadda", "အသံ")):
        PROP_X[f"{_a} {_b}gocaraṃ"] = Cl(f"{_am}သည် {_bm}ကို", *_GOC)
PROP_X["samāpannassa atthi vacībhedo ñāṇaṃ saccagocaraṃ"] = Cl(f"{SAMAP}၌ {VB} {EXIST}၍ ဉာဏ်သည် သစ္စာကို", *_GOC)
new("ñāṇaṃ saccagocaraṃ / sotaṃ saddagocaraṃ", "ဉာဏ်သည် သစ္စာကို ကျက်စားရာ ပြု / နားသည် အသံကို ကျက်စားရာ ပြု")
_TWO = F.NUM_MY[2]
PROP_X["dvinnaṃ phassānaṃ, dvinnaṃ vedanānaṃ, dvinnaṃ saññānaṃ, dvinnaṃ cetanānaṃ, dvinnaṃ cittānaṃ samodhānaṃ hoti"] = V(
    f"တွေ့ထိမှု {_TWO}{F.CL}၊ {F.VEDANA.my} {_TWO}{F.CL}၊ {F.SANNA.my} {_TWO}{F.CL}၊ စေ့ဆော်မှု {_TWO}{F.CL}၊ စိတ် "
    f"{_TWO}{F.CL}တို့၏ ပေါင်းဆုံခြင်း")
_VSK = "စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှုတို့ကို နှုတ်၏ ပြုပြင်ဖန်တီးမှုတို့ဟု"
SAID = {"vitakkavicārā vacīsaṅkhārā": _VSK,
        "vitakkasamuṭṭhānā vācā": "စတင်ကြံစည်မှုကြောင့် ဖြစ်ပေါ်သော စကားဟု",
        "saññāsamuṭṭhānā vācā": f"{F.SANNA.my}ကြောင့် ဖြစ်ပေါ်သော စကားဟု"}
new("vitakkavicārā vacīsaṅkhārā / vitakkasamuṭṭhānā vācā", _VSK + " / " + SAID["vitakkasamuṭṭhānā vācā"])


@F.rule(r"(?P<s>vitakkavicārā vacīsaṅkhārā|vitakkasamuṭṭhānā vācā|saññāsamuṭṭhānā vācā) vuttā bhagavatā – (?P<q>.+)")
def _r_said(m):
    """S vuttā bhagavatā – "Q": «Sဟု မြတ်စွာဘုရား ဟောတော်မူ – “Q”»."""
    if re.search(r"ti, ", m["q"]):      # the quotation ended inside (…"ti, atthi tassa …): not one clause
        return None
    try:
        q = F.prop_my(m["q"], "stmt", 0)
    except F.Miss:
        return None
    return Cl(f"{SAID[m['s']]} {F.BHAGAVA}", "ဟောတော်မူ", "မဟောတော်မူ", post=f" – «{q}»")


NIR = ("ချုပ်ငြိမ်းသွား", "မချုပ်ငြိမ်းသွား")
LST.update({"pīti": "ပီတိ", "assāsapassāsā": "ထွက်သက် ဝင်သက်", "rūpasaññā": "ရုပ်ဟု မှတ်သိမှု",
            "ākāsānañcāyatanasaññā": f"{ARUPA4['ākāsānañcāyatanaṃ']}ဟု မှတ်သိမှု",
            "viññāṇañcāyatanasaññā": f"{ARUPA4['viññāṇañcāyatanaṃ']}ဟု မှတ်သိမှု",
            "ākiñcaññāyatanasaññā": f"{ARUPA4['ākiñcaññāyatanaṃ']}ဟု မှတ်သိမှု", "saddo": "အသံ"})
W("1", "^1-265", "rūpasaññānaṃ", "ရုပ်ဟု မှတ်သိမှု")


@F.rule(r"(?P<g>.+?) samāpannassa (?P<y>.+?) niruddhā (?:hoti|honti)")
def _r_niruddha(m):
    """X samāpannassa Y niruddhā hoti: «Xကို ဝင်စားနေသူ၏ Yသည် ချုပ်ငြိမ်းသွား»."""
    if m["g"] not in ATT or lst(m["y"]) is None:
        return None
    return Cl(f"{ATT[m['g']]}ကို ဝင်စားနေသူ၏ {lst(m['y'])}သည်", *NIR)


PROP_X["attheva suttanto"] = V(f"ထိုသို့သော {F.SUTTANTA} အမှန်ပင်", EXIST)
SENT_X["Nanu paṭhamaṃ jhānaṃ samāpannassa vācā niruddhā hotīti!"] = (
    f"“{ATT['paṭhamaṃ jhānaṃ']}ကို ဝင်စားနေသူ၏ {VACA}သည် {NIR[0]}သည်”ဟူ၍ ဟောထားသည် မဟုတ်လော{END}")
KANTAKA = new("kaṇṭako / kaṇḍako (a thorn)", "ဆူးငြောင့်")
JGEN = {f"{o}assa jhānassa": f"{ORDJ[o + 'aṃ']} {JH}၏" for o in ("paṭham", "dutiy", "tatiy", "catutth")}


@F.rule(r"(?P<g>\S+ \S+|.+? samāpannassa) (?P<y>.+?) kaṇ[ṭḍ]ako vutto bhagavatā")
def _r_kantaka(m):
    """G Y kaṇṭako vutto bhagavatā: «Gအတွက် Yသည် ဆူးငြောင့်ဟု မြတ်စွာဘုရား ဟောတော်မူ»."""
    g = m["g"]
    if g in JGEN:
        gm = JGEN[g]
    elif g.endswith(" samāpannassa") and g[:-len(" samāpannassa")] in ATT:
        gm = f"{ATT[g[:-len(' samāpannassa')]]}ကို ဝင်စားနေသူ၏"
    else:
        return None
    y = lst(m["y"])
    if y is None:
        return None
    return Cl(f"{gm} {y}သည် {KANTAKA}ဟု {F.BHAGAVA}", "ဟောတော်မူ", "မဟောတော်မူ")


F.BR_TABLE["[kaṇṭako (syā.) a. ni. 10.72]"] = f"[{F.PATHA} (Syā.): kaṇṭako{C} “အင်္ဂုတ္တရနိကာယ်” 10.72]"
F.BR_TABLE["[atthi vitakkavicārā (syā.) evamuparipi]"] = f"[{F.PATHA} (Syā.): atthi vitakkavicārā{C} အောက်၌လည်း ဤနည်းတူ]"
REF_NOTE_X["kaṇṭakasuttaṃ nissāya pucchati"] = "“ကဏ္ဋက” သုတ်ကို မှီ၍ မေးသည်"
SENT_X["Nanu vuttaṃ bhagavatā – sikhissa, ānanda, bhagavato arahato sammāsambuddhassa abhibhū nāma sāvako brahmaloke "
       "ṭhito dasasahassilokadhātuṃ sarena viññāpesi –"] = (
    f"{F.BHAGAVA} ဤသို့ ဟောတော်မူသည် မဟုတ်လော – “အာနန္ဒာ၊ {_TG[:_TG.rindex(F.BHAGAVA)]}သိခီ {F.BHAGAVA}၏ အဘိဘူ "
    "အမည်ရှိသော တပည့်သည် ဗြဟ္မာ့လောက၌ တည်လျက် လောကဓာတ် တစ်သောင်းကို အသံဖြင့် သိစေခဲ့၏ –")
LINES_X["Ārabbhatha nikkamatha, yuñjatha buddhasāsane;"] = (
    "‘အားထုတ်ကြလော့၊ ထွက်မြောက်ကြလော့၊ ဘုရားရှင်၏ သာသနာ၌ ကြိုးစားကြလော့၊")
LINES_X["Dhunātha maccuno senaṃ, naḷāgāraṃva kuñjaro."] = (
    "ဆင်သည် ကျူရိုး အိမ်ကို ဖြိုဖျက်သကဲ့သို့ သေမင်း၏ စစ်သည်တို့ကို ဖြိုဖျက်ကြလော့’။")
LINES_X["Yo imasmiṃ dhammavinaye, appamatto vihassati;"] = (
    "‘အကြင်သူသည် ဤ ဓမ္မ ဝိနည်း၌ မမေ့မလျော့ဘဲ နေလိမ့်မည် ⟦0⟧၊")
LINES_X["Pahāya jātisaṃsāraṃ, dukkhassantaṃ karissatīti."] = (
    f"ထိုသူသည် ပဋိသန္ဓေ နေခြင်းဟူသော သံသရာကို ပယ်၍ {F.DUKKHA_END}လိမ့်မည်’”ဟူ၍ ⟦0⟧။")
VAR_X10.update({"vihessati": F.LEKHANA, "viharissati": F.PATHA, "kaṇṭako": F.PATHA})


# ===================================================================================== 10. Kaṅkhā verses
REF_X.update({"cūḷava.": "“စူဠဝဂ်”"})
REF_NOTE_X.update({"udāne ca": "“ဥဒါန်း”၌လည်း", "udāne": "“ဥဒါန်း”"})
VAR_X10.update({"suriyova": F.LEKHANA, "ye jhāyino": F.PATHA, "nitiṇṇaoghaṃ": F.LEKHANA, "nittiṇṇaoghaṃ": F.LEKHANA})
_YADA = "“အကြင်အခါ၌ သဘောတရားတို့သည် ဧကန်မုချ ထင်ရှား ပေါ်လာကြ၏၊"
LINES_X["Yadā have pātubhavanti dhammā,"] = _YADA
LINES_X["Ātāpino jhāyato brāhmaṇassa;"] = "အားထုတ်သော၊ ဈာန် ဝင်စားသော ပုဏ္ဏားအား၊"
LINES_X["Athassa kaṅkhā vapayanti sabbā,"] = "ထိုအခါ ထိုပုဏ္ဏား၏ သံသယ အားလုံးတို့ ကင်းပျောက်ကြ၏၊"
LINES_X["Yato pajānāti sahetudhammanti."] = "အကြောင်းနှင့်တကွ ဖြစ်သော သဘောတရားကို ကွဲပြားစွာ သိသောကြောင့်တည်း။"
LINES_X["Yato khayaṃ paccayānaṃ avedīti."] = "အကြောင်းတို့၏ ကုန်ခန်းခြင်းကို သိသောကြောင့်တည်း။"
LINES_X["Vidhūpayaṃ tiṭṭhati mārasenaṃ,"] = "မာရ်နတ်၏ စစ်သည်ကို ဖြိုခွင်းလျက် တည်၏၊"
LINES_X["Sūriyova obhāsayamantalikkhanti."] = "နေမင်းသည် ⟦0⟧ ကောင်းကင်ကို ထွန်းလင်းစေသကဲ့သို့တည်း ⟦1⟧။"
LINES_X["Yā kāci kaṅkhā idha vā huraṃ vā,"] = "“ဤလောက၌ဖြစ်စေ၊ တမလွန်လောက၌ဖြစ်စေ၊"
LINES_X["Sakavediyā vā paravediyā vā;"] = "မိမိ၌ ဖြစ်သည်ဖြစ်စေ၊ သူတစ်ပါး၌ ဖြစ်သည်ဖြစ်စေ သံသယ ရှိသမျှတို့ကို"
LINES_X["Jhāyino tā pajahanti sabbā,"] = "ဈာန် ဝင်စားသူတို့သည် ⟦0⟧ ထိုသံသယ အားလုံးတို့ကို ပယ်ကြ၏၊"
LINES_X["Ātāpino brahmacariyaṃ carantāti."] = "ထိုသူတို့သည် အားထုတ်၍ မြတ်သော အကျင့်ကို ကျင့်ကြသူတို့ ဖြစ်ကြ၏ ⟦0⟧။"
_SN = F.REF["saṃ. ni."]
F.BR_TABLE.update({
    "[ye jhāyino (udāne)]": f"[{F.PATHA} (“ဥဒါန်း”): ye jhāyino]",
    "[saṃ. ni. 4.259, 263]": f"[{_SN} 4.259{C} 263]",
    "[saṃ. ni. 4.259, 263; a. ni. 9.31; dī. ni. 3.344]": (
        f"[{_SN} 4.259{C} 263{C} {F.REF['a. ni.']} 9.31{C} {F.REF['dī. ni.']} 3.344]"),
    "[a. ni. 1 tikanipāte; saṃ. ni. 1.285]": f"[{F.REF['a. ni.']} 1 တိကနိပါတ်{C} {_SN} 1.285]",
    "[cūḷava. 385; a. ni. 8.20; udā. 45 udāne ca]": (
        f"[“စူဠဝဂ်” 385{C} {F.REF['a. ni.']} 8.20{C} “ဥဒါန်း” 45{C} “ဥဒါန်း”၌လည်း]"),
})
LINES_X["Ye kaṅkhāsamatikkantā, kaṅkhābhūtesu pāṇisu;"] = (
    "“သံသယ ဖြစ်နေကြသော သတ္တဝါတို့အကြား သံသယကို လွန်မြောက်ပြီးသော၊")
LINES_X["Asaṃsayā visaṃyuttā, tesu dinnaṃ mahapphalanti."] = (
    "ယုံမှားခြင်း ကင်း၍ နှောင်ကြိုးမှ ကင်းလွတ်ကြသူတို့၌ ပေးလှူသော အလှူသည် ကြီးမားသော အကျိုး ရှိ၏။")
LINES_X["Etādisī dhammapakāsanettha,"] = "“ဤ၌ တရားကို ပြသခြင်းသည် ဤသို့ ဖြစ်၏၊"
LINES_X["Na tattha kiṃ kaṅkhati koci sāvako;"] = "ထိုတရား၌ မည်သည့် တပည့်မျှ အဘယ်ကိုမျှ သံသယ မဖြစ်၊"
LINES_X["Nitthiṇṇaoghaṃ vicikicchachinnaṃ,"] = "ရေအလျဉ်ကို ကူးမြောက်ပြီး ⟦0⟧ ယုံမှားမှုကို ဖြတ်ပြီးသော"
LINES_X["Buddhaṃ namassāma jinaṃ janindāti."] = "အောင်မြင်တော်မူသော လူတို့၏ အရှင် ဘုရားရှင်ကို ရှိခိုးကြပါ၏”ဟူ၍ ⟦0⟧။"
OPEN_Q_X = {
    "Na vattabbaṃ – buddhassa bhagavato vohāro lokiyaṃ voharantassa lokiyo hoti, lokuttaraṃ voharantassa lokuttaro "
    "hotīti? Āmantā. Nanu bhagavā lokiyampi lokuttarampi dhammaṃ voharatīti? Āmantā. Hañci bhagavā lokiyampi "
    "lokuttarampi dhammaṃ voharati, tena vata re vattabbe – buddhassa bhagavato vohāro lokiyaṃ voharantassa lokiyo "
    "hoti, lokuttaraṃ voharantassa lokuttaro hotīti.": [
        "Na vattabbaṃ – buddhassa bhagavato vohāro lokiyaṃ voharantassa lokiyo hoti, lokuttaraṃ voharantassa "
        "lokuttaro hotīti?", "Āmantā.", "Nanu bhagavā lokiyampi lokuttarampi dhammaṃ voharatīti?", "Āmantā.",
        "Hañci bhagavā lokiyampi lokuttarampi dhammaṃ voharati, tena vata re vattabbe – buddhassa bhagavato vohāro "
        "lokiyaṃ voharantassa lokiyo hoti, lokuttaraṃ voharantassa lokuttaro hotīti."],
    "Na vattabbaṃ – atthi arahato kaṅkhāti? Āmantā. Nanu arahā itthipurisānaṃ nāmagotte kaṅkheyya, maggāmagge "
    "kaṅkheyya, tiṇakaṭṭhavanappatīnaṃ nāme kaṅkheyyāti? Āmantā. Hañci arahā itthipurisānaṃ nāmagotte kaṅkheyya, "
    "maggāmagge kaṅkheyya, tiṇakaṭṭhavanappatīnaṃ nāme kaṅkheyya; tena vata re vattabbe – atthi arahato kaṅkhāti.": [
        "Na vattabbaṃ – atthi arahato kaṅkhāti?", "Āmantā.",
        "Nanu arahā itthipurisānaṃ nāmagotte kaṅkheyya, maggāmagge kaṅkheyya, tiṇakaṭṭhavanappatīnaṃ nāme "
        "kaṅkheyyāti?", "Āmantā.",
        "Hañci arahā itthipurisānaṃ nāmagotte kaṅkheyya, maggāmagge kaṅkheyya, tiṇakaṭṭhavanappatīnaṃ nāme "
        "kaṅkheyya; tena vata re vattabbe – atthi arahato kaṅkhāti."],
}

# ===================================================================================== 10. kathā 15 (Dukkhāhāra)
section("(15) 6. Dukkhāhārakathā", f"(15) 6. ဒုက္ခဟု ဆိုခြင်းအကြောင်း {KATHA}")
section("Dukkhāhārakathā", f"ဒုက္ခဟု ဆိုခြင်းအကြောင်း {KATHA}")
MAGGANGA = "မဂ်၏ အင်္ဂါ ဖြစ်၍ မဂ်၌ အကျုံးဝင်သော အရာ"              # maggaṅgaṃ maggapariyāpannaṃ
PROP_X["dukkhāhāro maggaṅgaṃ maggapariyāpannaṃ"] = V(f"ဒုက္ခဟု ဆိုခြင်းသည် {MAGGANGA}")
new("dukkhāhāro", "ဒုက္ခဟု ဆိုခြင်း")
_DV = f"{_DK}ဟူသော {VACA}ကို"
BHAV = ("ပွားများကြ", "မပွားများကြ")
PROP_X["ye keci dukkhanti vācaṃ bhāsanti"] = FR(f"{_DV} ပြောကြသူ မည်သူမဆို")
PROP_X["ye keci buddhassa bhagavato vohāraṃ suṇanti"] = FR(
    f"ဘုရားရှင် {F.BHAGAVA}၏ ပြောဆို သုံးနှုန်းခြင်းကို ကြားကြသူ မည်သူမဆို")
PROP_X["sabbe te maggaṃ bhāventi"] = Cl("ထိုသူ အားလုံးတို့သည် မဂ်ကို", *BHAV)
BALA = "မိုက်မဲသော ပုထုဇဉ်တို့"
PROP_X["bālaputhujjanā dukkhanti vācaṃ bhāsanti"] = Cl(f"{BALA}သည် {_DV}", "ပြောကြ", "မပြောကြ")
PROP_X["bālaputhujjanā buddhassa bhagavato vohāraṃ suṇanti"] = Cl(
    f"{BALA}သည် ဘုရားရှင် {F.BHAGAVA}၏ ပြောဆို သုံးနှုန်းခြင်းကို", "ကြားကြ", "မကြားကြ")
PROP_X["bālaputhujjanā maggaṃ bhāventi"] = Cl(f"{BALA}သည် မဂ်ကို", *BHAV)
HEIN = {"mātughātako": "အမိကို သတ်သူ", "pitughātako": "အဖကို သတ်သူ", "arahantaghātako": "ရဟန္တာကို သတ်သူ",
        "ruhiruppādako": "ဘုရားရှင်၏ သွေးကို စိမ်းစေသူ", "saṅghabhedako": "သံဃာကို သင်းခွဲသူ"}
for _k, _m in HEIN.items():
    new(_k, _m)
    PROP_X[_k] = FR(f"{_m}သည်")
    PROP_X[f"{_k} maggaṃ bhāveti"] = Cl(f"{_m}သည် မဂ်ကို", "ပွားများ", "မပွားများ")
    PROP_X[f"{_k} dukkhanti vācaṃ bhāsati"] = Cl(f"{_m}သည် {_DV}", "ပြော", "မပြော")
    PROP_X[f"{_k} buddhassa bhagavato vohāraṃ suṇāti"] = Cl(
        f"{_m}သည် ဘုရားရှင် {F.BHAGAVA}၏ ပြောဆို သုံးနှုန်းခြင်းကို", "ကြား", "မကြား")
F.BR_TABLE["[lohituppādako (sī. ka.) aññaṭṭhānesu pana ruhiruppādakotveva dissati]"] = (
    f"[{F.PATHA} (Sī., Ka.): lohituppādako{C} အခြား နေရာတို့၌ကား ruhiruppādako ဟူ၍သာ တွေ့ရသည်]")

# ===================================================================================== 10. kathā 16 (Cittaṭṭhiti)
section("(16) 7. Cittaṭṭhitikathā", f"(16) 7. စိတ်၏ တည်ခြင်းအကြောင်း {KATHA}")
section("Cittaṭṭhitikathā", f"စိတ်၏ တည်ခြင်းအကြောင်း {KATHA}")
ONE_C = f"စိတ် {F.NUM_MY[1]}ခုသည်"                                  # ekaṃ cittaṃ
STAY = ("တည်", "မတည်")
N = {"dve": "နှစ်", "cattāro": "လေး", "cattāri": "လေး", "aṭṭha": "ရှစ်", "dasa": "ဆယ်", "vīsati": "နှစ်ဆယ်",
     "tiṃsa": "သုံးဆယ်", "cattārīsa": "လေးဆယ်", "paññāsa": "ငါးဆယ်", "pañca": "ငါး", "soḷasa": "ဆယ့်ခြောက်",
     "bāttiṃsa": "သုံးဆယ့်နှစ်", "catusaṭṭhi": "ခြောက်ဆယ့်လေး"}
NTH = {"dve": "နှစ်ထောင်", "cattāri": "လေးထောင်", "aṭṭha": "ရှစ်ထောင်", "soḷasa": "တစ်သောင်းခြောက်ထောင်",
       "vīsati": "နှစ်သောင်း", "cattārīsa": "လေးသောင်း", "saṭṭhi": "ခြောက်သောင်း", "caturāsīti": "ရှစ်သောင်းလေးထောင်",
       "dvecattārīsa": "လေးသောင်းနှစ်ထောင်"}
NH = {"dve": "နှစ်ရာ", "cattāri": "လေးရာ", "pañca": "ငါးရာ"}
DUR = {"divasaṃ": "တစ်ရက်", "māsaṃ": "တစ်လ", "saṃvaccharaṃ": "တစ်နှစ်", "vassasataṃ": "နှစ် တစ်ရာ",
       "vassasahassaṃ": "နှစ် တစ်ထောင်", "kappaṃ": "တစ်ကမ္ဘာ", "ekaṃ kappaṃ": "တစ်ကမ္ဘာ",
       "kappasahassaṃ": "ကမ္ဘာ တစ်ထောင်", "kappasahassāni": "ကမ္ဘာ တစ်ထောင်",
       "kappassa tatiyabhāgaṃ": "ကမ္ဘာ၏ သုံးပုံတစ်ပုံ", "upaḍḍhakappaṃ": "ကမ္ဘာ တစ်ဝက်",
       "yāvatāyukaṃ": "အသက် ရှည်သမျှ ကာလပတ်လုံး"}
for _n, _m in N.items():
    DUR[f"{_n} divase"] = f"{_m}ရက်"
    DUR[f"{_n} māse"] = f"{_m}လ"
    DUR[f"{_n} vassāni"] = f"{_m}နှစ်"
    DUR[f"{_n} kappe"] = f"{_m}ကမ္ဘာ"
for _n, _m in NH.items():
    DUR[f"{_n} vassasatāni"] = f"နှစ် {_m}"
    DUR[f"{_n} kappasatāni"] = f"ကမ္ဘာ {_m}"
for _n, _m in NTH.items():
    DUR[f"{_n} vassasahassāni"] = f"နှစ် {_m}"
    DUR[f"{_n} kappasahassāni"] = f"ကမ္ဘာ {_m}"
W("2", "^2-1027", "Soḷasa kappasahassāni", "ကမ္ဘာ တစ်သောင်းခြောက်ထောင်")
W("2", "^2-1026", "Catusaṭṭhi kappā", "ခြောက်ဆယ့်လေးကမ္ဘာ")
W("2", "^2-1024", "Kappassa tatiyo bhāgo", "ကမ္ဘာ၏ သုံးပုံတစ်ပုံ")
DEVA_N = {"cātumahārājikānaṃ": "စာတုမဟာရာဇ်", "tāvatiṃsānaṃ": "တာဝတိံသာ", "yāmānaṃ": "ယာမာ", "tusitānaṃ": "တုသိတာ",
          "nimmānaratīnaṃ": "နိမ္မာနရတီ", "paranimmitavasavattīnaṃ": "ပရနိမ္မိတဝသဝတ္တီ",
          "brahmapārisajjānaṃ": "ဗြဟ္မပါရိသဇ္ဇ", "brahmapurohitānaṃ": "ဗြဟ္မပုရောဟိတ", "mahābrahmānaṃ": "မဟာဗြဟ္မာ",
          "parittābhānaṃ": "ပရိတ္တာဘ", "appamāṇābhānaṃ": "အပ္ပမာဏာဘ", "ābhassarānaṃ": "အာဘဿရ",
          "parittasubhānaṃ": "ပရိတ္တသုဘ", "appamāṇasubhānaṃ": "အပ္ပမာဏသုဘ", "subhakiṇhānaṃ": "သုဘကိဏှ",
          "vehapphalānaṃ": "ဝေဟပ္ဖိုလ်", "avihānaṃ": "အဝိဟာ", "atappānaṃ": "အတပ္ပါ", "sudassānaṃ": "သုဒဿာ",
          "sudassīnaṃ": "သုဒဿီ", "akaniṭṭhānaṃ": "အကနိဋ္ဌ",
          "ākāsānañcāyatanūpagānaṃ": f"{ARUPA4['ākāsānañcāyatanaṃ']} ဘုံသို့ ရောက်သော"}
for _k, _bid in (("tāvatiṃsānaṃ", "^2-1023"), ("akaniṭṭhānaṃ", "^2-1027"), ("subhakiṇhānaṃ", "^2-1026"),
                 ("ākāsānañcāyatanūpagānaṃ", "^2-1028")):
    if _bid in F.FINAL.SEG["2"]:
        W("2", _bid, _k[:-2], DEVA_N[_k])
WHO16 = {f"{k} devānaṃ": f"{v} နတ်တို့၏" for k, v in DEVA_N.items()}
WHO16["manussānaṃ"] = f"{F.MANUSSA}တို့၏"
for _w, _wm in WHO16.items():
    PROP_X[_w] = FR(_wm)
_DURK = sorted(DUR, key=len, reverse=True)


@F.rule(r"(?P<all>.+) tiṭṭhati")
def _r_stay(m):
    """(WHO) (ekaṃ cittaṃ) DUR tiṭṭhati: «(WHO) စိတ် တစ်ခုသည် DUR တည်»."""
    x, who, one = m["all"], "", ""
    for w in sorted(WHO16, key=len, reverse=True):
        if x.startswith(w + " "):
            who, x = WHO16[w] + " ", x[len(w) + 1:]
            break
    if x.startswith("ekaṃ cittaṃ "):
        one, x = ONE_C + " ", x[len("ekaṃ cittaṃ "):]
    if x not in DUR:
        return None
    return Cl(f"{who}{one}{DUR[x]}", *STAY)


@F.rule(r"(?P<all>.+) āyuppamāṇaṃ")
def _r_ayu(m):
    """WHO DUR āyuppamāṇaṃ: «WHO သက်တမ်း အတိုင်းအတာသည် DUR ဖြစ်» (pi-2 «သက်တမ်း အတိုင်းအတာ»)."""
    for w in sorted(WHO16, key=len, reverse=True):
        if m["all"].startswith(w + " ") and m["all"][len(w) + 1:] in DUR:
            return V(f"{WHO16[w]} သက်တမ်း အတိုင်းအတာသည် {DUR[m['all'][len(w) + 1:]]}")
    return None


W("2", "^2-1027", "āyuppamāṇaṃ", "သက်တမ်း အတိုင်းအတာ")
_UK, _VK = "ဖြစ်ခြင်း ခဏ", "ပျက်ခြင်း ခဏ"
for _d, _dm in (("upaḍḍhadivaso", "နေ့ တစ်ဝက်"), ("divaso", "တစ်ရက်"),
                ("dvecattārīsa kappasahassāni", DUR["dvecattārīsa kappasahassāni"])):
    PROP_X[f"{_d} uppādakkhaṇo"] = V(f"{_dm}သည် {_UK}")
    PROP_X[f"{_d} vayakkhaṇo"] = V(f"{_dm}သည် {_VK}")
new("uppādakkhaṇo / vayakkhaṇo", f"{_UK} / {_VK}")
PROP_X["atthaññe dhammā ekāhaṃ bahumpi uppajjitvā nirujjhanti"] = V(
    "တစ်ရက်တည်း၌ပင် အကြိမ်များစွာ ဖြစ်ပေါ်၍ ချုပ်ငြိမ်းကြသော အခြား သဘောတရားတို့", EXIST)
PROP_X["te dhammā cittena lahuparivattā"] = V("ထိုသဘောတရားတို့သည် စိတ်ထက် လျင်မြန်စွာ ပြောင်းလဲတတ်သော အရာ")
new("lahuparivatta", "လျင်မြန်စွာ ပြောင်းလဲတတ်သော")
QUOTE_X["nāhaṃ, bhikkhave, aññaṃ ekadhammampi samanupassāmi evaṃ lahuparivattaṃ yathayidaṃ cittaṃ. Yāvañcidaṃ, "
        "bhikkhave, upamāpi na sukarā yāva lahuparivattaṃ cittan"] = (
    "ရဟန်းတို့၊ ဤစိတ်ကဲ့သို့ ဤမျှ လျင်မြန်စွာ ပြောင်းလဲတတ်သော အခြား သဘောတရား တစ်ပါးကိုမျှ ငါ မမြင်။ ရဟန်းတို့၊ "
    "စိတ်သည် မည်မျှ လျင်မြန်စွာ ပြောင်းလဲတတ်သည်ကို ဥပမာ ပြရန်ပင် မလွယ်ကူ")
QUOTE_X["seyyathāpi, bhikkhave, makkaṭo araññe pavane caramāno sākhaṃ gaṇhati, taṃ muñcitvā aññaṃ gaṇhati, taṃ "
        "muñcitvā aññaṃ gaṇhati; evameva kho, bhikkhave, yamidaṃ vuccati cittaṃ itipi mano itipi viññāṇaṃ itipi taṃ "
        "rattiyā ca divasassa ca aññadeva uppajjati aññaṃ nirujjhati"] = (
    "ရဟန်းတို့၊ ဥပမာ မျောက်သည် တောအုပ်ကြီး၌ လှည့်လည် သွားလာလျက် သစ်ကိုင်းကို ဆွဲကိုင်၏၊ ထိုကိုင်းကို လွှတ်၍ "
    "အခြား ကိုင်းကို ဆွဲကိုင်၏၊ ထိုကိုင်းကို လွှတ်၍ အခြား ကိုင်းကို ဆွဲကိုင်၏၊ ရဟန်းတို့၊ ထို့အတူပင် စိတ်ဟူ၍လည်းကောင်း၊ "
    "မနောဟူ၍လည်းကောင်း၊ သိစိတ်ဟူ၍လည်းကောင်း ခေါ်ဆိုသော ဤအရာ ⟦b⟧သည် ညဉ့်၌လည်းကောင်း၊ နေ့၌လည်းကောင်း "
    "တစ်ခု ဖြစ်ပေါ်၍ အခြား တစ်ခု ချုပ်ငြိမ်း၏")
VAR_X10["yadidaṃ"] = F.PATHA
_VJ = {k[:-len("dhātu")]: v[:-len(" ဓာတ်")] for k, v in ((p, F.DHATU[p].my) for p in F.DHATU)
       if k.endswith("viññāṇadhātu")}
for _k, _m in _VJ.items():
    PROP_X[f"{_k}ṃ"] = FR(_m)
    PROP_X[f"{_k}ṃ divasaṃ tiṭṭhati"] = Cl(f"{_m}သည် {DUR['divasaṃ']}", *STAY)
PROP_X["akusalaṃ cittaṃ"] = FR("အကုသိုလ် စိတ်")
SAHA = {"rāga": "ရာဂ", "dosa": "ဒေါသ", "moha": "မောဟ", "māna": "မာန", "diṭṭhi": KIL["diṭṭhi"],
        "vicikicchā": KIL["vicikicchā"], "thina": KIL["thinaṃ"], "uddhacca": KIL["uddhaccaṃ"],
        "ahirika": KIL["ahirikaṃ"], "anottappa": KIL["anottappaṃ"]}
for _k, _m in SAHA.items():
    PROP_X[f"{_k}sahagataṃ"] = FR(f"{_m}နှင့်အတူ ဖြစ်သော")
PROP_X["anottappasahagataṃ cittaṃ divasaṃ tiṭṭhati"] = Cl(
    f"{SAHA['anottappa']}နှင့်အတူ ဖြစ်သော စိတ်သည် {DUR['divasaṃ']}", *STAY)
SENSE = {"cakkhunā rūpaṃ passati": "မျက်စိဖြင့် အဆင်းအရောင်ကို မြင်", "sotena saddaṃ suṇāti": "နားဖြင့် အသံကို ကြား",
         "ghānena gandhaṃ ghāyati": "နှာခေါင်းဖြင့် အနံ့ကို ခံ", "jivhāya rasaṃ sāyati": "လျှာဖြင့် အရသာကို ခံ",
         "kāyena phoṭṭhabbaṃ phusati": "ကိုယ်ဖြင့် အထိအတွေ့ကို ထိ", "manasā dhammaṃ vijānāti": "မနောဖြင့် သဘောတရားကို သိ"}
_YC, _TC = "အကြင် စိတ်ဖြင့်ပင်", "ထိုစိတ်ဖြင့်ပင်"
_S = {k: v + "၏" for k, v in SENSE.items()}
PROP_X["yeneva cittena cakkhunā rūpaṃ passati, teneva cittena sotena saddaṃ suṇāti… ghānena gandhaṃ ghāyati… jivhāya "
       "rasaṃ sāyati… kāyena phoṭṭhabbaṃ phusati… manasā dhammaṃ vijānāti… yeneva cittena manasā dhammaṃ vijānāti, "
       "teneva cittena cakkhunā rūpaṃ passati… sotena saddaṃ suṇāti… ghānena gandhaṃ ghāyati… jivhāya rasaṃ sāyati… "
       "kāyena phoṭṭhabbaṃ phusati"] = Cl(
    f"{_YC} {_S['cakkhunā rūpaṃ passati']}၊ {_TC} {_S['sotena saddaṃ suṇāti']}… {_S['ghānena gandhaṃ ghāyati']}… "
    f"{_S['jivhāya rasaṃ sāyati']}… {_S['kāyena phoṭṭhabbaṃ phusati']}… {_S['manasā dhammaṃ vijānāti']}… {_YC} "
    f"{_S['manasā dhammaṃ vijānāti']}၊ {_TC} {_S['cakkhunā rūpaṃ passati']}… {_S['sotena saddaṃ suṇāti']}… "
    f"{_S['ghānena gandhaṃ ghāyati']}… {_S['jivhāya rasaṃ sāyati']}… ကိုယ်ဖြင့် အထိအတွေ့ကို", "ထိ", "မထိ")
MOVE = [("abhikkamati", "ရှေ့သို့ တိုး"), ("paṭikkamati", "နောက်သို့ ဆုတ်"), ("āloketi", "ရှေ့သို့ ကြည့်"),
        ("viloketi", "ဘေးသို့ ကြည့်"), ("samiñjeti", "ကွေး"), ("pasāreti", "ဆန့်")]
W("2", "^2-508", "abhikkante paṭikkante", "ရှေ့သို့ တိုးရာ၊ နောက်သို့ ဆုတ်ရာ")
_MV = dict(MOVE)
_pairs = [("abhikkamati", "paṭikkamati"), ("paṭikkamati", "abhikkamati"), ("āloketi", "viloketi"),
          ("viloketi", "āloketi"), ("samiñjeti", "pasāreti"), ("pasāreti", "samiñjeti")]
_mv = [f"{_YC} {_MV[a]}၏၊ {_TC} {_MV[b]}၏" for a, b in _pairs]
PROP_X["; ".join(f"yeneva cittena {a}, teneva cittena {b}" for a, b in _pairs)] = Cl(
    "၊ ".join(_mv)[:-len(_MV["samiñjeti"] + "၏")].rstrip(), _MV["samiñjeti"], "မ" + _MV["samiñjeti"])
_AKD = f"{DEVA_N['ākāsānañcāyatanūpagānaṃ']} နတ်တို့"
PROP_X["ākāsānañcāyatanūpagānaṃ devānaṃ cittaṃ muhuttaṃ muhuttaṃ uppajjati muhuttaṃ muhuttaṃ nirujjhati"] = Cl(
    f"{_AKD}၏ စိတ်သည် ခဏခဏ ဖြစ်ပေါ်၍ ခဏခဏ", "ချုပ်ငြိမ်း", "မချုပ်ငြိမ်း")
PROP_X["ākāsānañcāyatanūpagā devā muhuttaṃ muhuttaṃ cavanti muhuttaṃ muhuttaṃ uppajjanti"] = Cl(
    f"{_AKD}သည် ခဏခဏ စုတေ၍ ခဏခဏ ပြန်လည်", "ဖြစ်ပေါ်ကြ", "မဖြစ်ပေါ်ကြ")
PROP_X["ākāsānañcāyatanūpagā devā yeneva cittena uppajjanti, teneva cittena cavanti"] = Cl(
    f"{_AKD}သည် {_YC} ပြန်လည် ဖြစ်ပေါ်ကြ၏၊ {_TC}", "စုတေကြ", "မစုတေကြ")

# ===================================================================================== 10. kathā 17 (Kukkuḷa)
section("(17) 8. Kukkuḷakathā", f"(17) 8. ပြာပူအကြောင်း {KATHA}")
section("Kukkuḷakathā", f"ပြာပူအကြောင်း {KATHA}")
ALL_SK = f"{F.SANKHARA.my[:-len('တို့')]} အားလုံးတို့"                 # sabbe saṅkhārā
KUKK = f"{ALL_SK}သည် ချွင်းချက် မထားဘဲ ပြာပူ"                         # sabbe saṅkhārā anodhiṃ katvā kukkuḷā
PROP_X["sabbe saṅkhārā anodhiṃ katvā kukkuḷā"] = V(KUKK)
new("sabbe saṅkhārā anodhiṃ katvā kukkuḷā", KUKK + " ဖြစ်")
SUKHA = [("sukhā vedanā", "သာယာသော ခံစားမှု"), ("kāyikaṃ sukhaṃ", "ကိုယ်၏ ချမ်းသာ"),
         ("cetasikaṃ sukhaṃ", "စိတ်၏ ချမ်းသာ"), ("dibbaṃ sukhaṃ", MS.THING["dibbaṃ sukhaṃ"][0]),
         ("mānusakaṃ sukhaṃ", MS.THING["mānusakaṃ sukhaṃ"][0]), ("lābhasukhaṃ", "လာဘ် ရခြင်း၏ ချမ်းသာ"),
         ("sakkārasukhaṃ", "အရိုအသေ ပြုခံရခြင်း၏ ချမ်းသာ"), ("yānasukhaṃ", "ယာဉ်၏ ချမ်းသာ"),
         ("sayanasukhaṃ", "အိပ်ရာ၏ ချမ်းသာ"), ("issariyasukhaṃ", "အစိုးရခြင်း၏ ချမ်းသာ"),
         ("ādhipaccasukhaṃ", "အကြီးအကဲ ဖြစ်ခြင်း၏ ချမ်းသာ"), ("gihisukhaṃ", "လူဝတ်ကြောင်၏ ချမ်းသာ"),
         ("sāmaññasukhaṃ", "ရဟန်း၏ ချမ်းသာ"), ("sāsavaṃ sukhaṃ", "စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော ချမ်းသာ"),
         ("anāsavaṃ sukhaṃ", "စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော ချမ်းသာ"),
         ("upadhisukhaṃ", "ဥပဓိနှင့် စပ်သော ချမ်းသာ"), ("nirūpadhisukhaṃ", "ဥပဓိ ကင်းသော ချမ်းသာ"),
         ("sāmisaṃ sukhaṃ", "ကာမဂုဏ်နှင့် စပ်သော ချမ်းသာ"), ("nirāmisaṃ sukhaṃ", "ကာမဂုဏ် ကင်းသော ချမ်းသာ"),
         ("sappītikaṃ sukhaṃ", "ပီတိနှင့်တကွ ဖြစ်သော ချမ်းသာ"), ("nippītikaṃ sukhaṃ", "ပီတိ ကင်းသော ချမ်းသာ"),
         ("jhānasukhaṃ", "ဈာန်၏ ချမ်းသာ"), ("vimuttisukhaṃ", "လွတ်မြောက်ခြင်း၏ ချမ်းသာ"),
         ("kāmasukhaṃ", "ကာမ၏ ချမ်းသာ"), ("nekkhammasukhaṃ", "ကာမမှ ထွက်မြောက်ခြင်း၏ ချမ်းသာ"),
         ("vivekasukhaṃ", "ဆိတ်ငြိမ်ခြင်း၏ ချမ်းသာ"), ("upasamasukhaṃ", "ငြိမ်းချမ်းခြင်း၏ ချမ်းသာ"),
         ("sambodhasukhaṃ", "အမှန်ကို သိခြင်း၏ ချမ်းသာ")]
PROP_X["atthi " + ", ".join(k for k, _ in SUKHA)] = V(f"{C} ".join(m for _, m in SUKHA), EXIST)
PROP_X["atthi sukhā vedanā… sambodhasukhaṃ"] = V(f"{SUKHA[0][1]}… {SUKHA[-1][1]}", EXIST)
for _k, _m in SUKHA:
    new(_k, _m)
PROP_X["sabbe saṅkhārā dukkhā vedanā kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ sokaparidevadukkhadomanassaupāyāsā"] = V(
    f"{ALL_SK}သည် နာကျင်သော ခံစားမှု၊ ကိုယ်၏ ဆင်းရဲ၊ စိတ်၏ ဆင်းရဲ၊ စိုးရိမ်ခြင်း ငိုကြွေးခြင်း ကိုယ်ဆင်းရဲခြင်း "
    "စိတ်ဆင်းရဲမှု ပြင်းစွာ ပူပန်ခြင်းတို့")


@F.frame(r"Tena hi vattabbaṃ – (?P<p>.+?)ti\.")
def _f_tenahi_say(m):
    """Tena hi vattabbaṃ – "P"ti. = «သို့ဖြစ်လျှင် ဤသို့ ဆိုသင့် – “P”။»"""
    return f"{F.TENA_HI} ဤသို့ ဆိုသင့် – “{F.pq(m['p'], 'stmt', 1)}”{END}"


ANCHOR_X["vattabbaṃ"] = "ဆိုသင့်"
VAR_X10.update({"tena hi": F.PATHA, "tena hi na vattabbaṃ": F.PATHA, "yampidaṃ": F.PATHA, "paṭividdho": F.PATHA})
_AD = "လောင်ကျွမ်းနေ၏"                                              # ādittaṃ
_FIRE = ("‹ရာဂ မီး၊ ဒေါသ မီး၊ မောဟ မီးဖြင့် လောင်ကျွမ်းနေ၏၊ ပဋိသန္ဓေ နေခြင်း၊ အိုခြင်း၊ သေခြင်း၊ စိုးရိမ်ခြင်းတို့၊ "
         "ငိုကြွေးခြင်းတို့၊ ကိုယ်ဆင်းရဲခြင်းတို့၊ စိတ်ဆင်းရဲခြင်းတို့၊ ပြင်းစွာ ပူပန်ခြင်းတို့ဖြင့် လောင်ကျွမ်းနေ၏›ဟု")
QUOTE_X["sabbaṃ, bhikkhave, ādittaṃ! Kiñca, bhikkhave, sabbaṃ ādittaṃ? Cakkhuṃ, bhikkhave, ādittaṃ, rūpā ādittā, "
        "cakkhuviññāṇaṃ ādittaṃ, cakkhusamphasso āditto; yamidaṃ cakkhusamphassapaccayā uppajjati vedayitaṃ sukhaṃ "
        "vā dukkhaṃ vā adukkhamasukhaṃ vā, tampi ādittaṃ. Kena ādittaṃ? Rāgagginā dosagginā mohagginā ādittaṃ, "
        "jātiyā jarāya maraṇena sokehi paridevehi dukkhehi domanassehi upāyāsehi ādittanti vadāmi. Sotaṃ ādittaṃ, "
        "saddā ādittā… ghānaṃ ādittaṃ, gandhā ādittā… jivhā ādittā, rasā ādittā… kāyo āditto, phoṭṭhabbā ādittā… "
        "mano āditto, dhammā ādittā, manoviññāṇaṃ ādittaṃ, manosamphasso āditto; yamidaṃ manosamphassapaccayā "
        "uppajjati vedayitaṃ sukhaṃ vā dukkhaṃ vā adukkhamasukhaṃ vā, tampi ādittaṃ. Kena ādittaṃ? Rāgagginā "
        "dosagginā mohagginā ādittaṃ, jātiyā jarāya maraṇena sokehi paridevehi dukkhehi domanassehi upāyāsehi "
        "ādittanti vadāmī"] = (
    f"ရဟန်းတို့၊ အလုံးစုံ {_AD}။ ရဟန်းတို့၊ အဘယ် အလုံးစုံ လောင်ကျွမ်းနေသနည်း။ ရဟန်းတို့၊ မျက်စိ {_AD}၊ "
    f"အဆင်းအရောင်တို့ {_AD}၊ မျက်စိ သိစိတ် {_AD}၊ မျက်စိ တွေ့ထိမှု {_AD}၊ မျက်စိ တွေ့ထိမှုကြောင့် ဖြစ်ပေါ်သော "
    f"သာယာသည်ဖြစ်စေ၊ နာကျင်သည်ဖြစ်စေ၊ မနာကျင် မသာယာသည်ဖြစ်စေ ခံစားရမှု ⟦b⟧ ရှိသမျှ၊ ထိုခံစားရမှုသည်လည်း {_AD}။ "
    f"အဘယ်ဖြင့် လောင်ကျွမ်းနေသနည်း။ {_FIRE} ငါ ဟော၏။ နား {_AD}၊ အသံတို့ {_AD}… နှာခေါင်း {_AD}၊ အနံ့တို့ {_AD}… "
    f"လျှာ {_AD}၊ အရသာတို့ {_AD}… ကိုယ် {_AD}၊ အထိအတွေ့တို့ {_AD}… မနော {_AD}၊ သဘောတရားတို့ {_AD}၊ မနော သိစိတ် "
    f"{_AD}၊ မနော တွေ့ထိမှု {_AD}၊ မနော တွေ့ထိမှုကြောင့် ဖြစ်ပေါ်သော သာယာသည်ဖြစ်စေ၊ နာကျင်သည်ဖြစ်စေ၊ မနာကျင် "
    f"မသာယာသည်ဖြစ်စေ ခံစားရမှု ရှိသမျှ၊ ထိုခံစားရမှုသည်လည်း {_AD}။ အဘယ်ဖြင့် လောင်ကျွမ်းနေသနည်း။ {_FIRE} ငါ ဟော၏")
_KG = [("cakkhu", "မျက်စိ", "rūpā", "အဆင်းအရောင်တို့"), ("sota", "နား", "saddā", "အသံတို့"),
       ("ghāna", "နှာခေါင်း", "gandhā", "အနံ့တို့"), ("jivhā", "လျှာ", "rasā", "အရသာတို့"),
       ("kāya", "ကိုယ်", "phoṭṭhabbā", "အထိအတွေ့တို့")]
_IK = ("လိုလားဖွယ်ကောင်းသော၊ ချစ်ခင်ဖွယ်ကောင်းသော၊ စိတ်နှင့် တွေ့သော၊ ချစ်ဖွယ် သဘော ရှိသော၊ ကာမနှင့် စပ်သော၊ "
       "တပ်မက်ဖွယ်ကောင်းသော")
QUOTE_X["pañcime, bhikkhave, kāmaguṇā! Katame pañca? Cakkhuviññeyyā rūpā iṭṭhā kantā manāpā piyarūpā kāmūpasaṃhitā "
        "rajanīyā, sotaviññeyyā saddā… ghānaviññeyyā gandhā… jivhāviññeyyā rasā… kāyaviññeyyā phoṭṭhabbā iṭṭhā kantā "
        "manāpā piyarūpā kāmūpasaṃhitā rajanīyā. Ime kho, bhikkhave, pañca kāmaguṇā"] = (
    f"ရဟန်းတို့၊ ဤ ကာမဂုဏ် ငါးပါးတို့ ရှိကုန်၏။ အဘယ် ငါးပါးတို့နည်း။ မျက်စိဖြင့် သိနိုင်သော {_IK} အဆင်းအရောင်တို့၊ "
    f"နားဖြင့် သိနိုင်သော အသံတို့… နှာခေါင်းဖြင့် သိနိုင်သော အနံ့တို့… လျှာဖြင့် သိနိုင်သော အရသာတို့… ကိုယ်ဖြင့် "
    f"သိနိုင်သော {_IK} အထိအတွေ့တို့။ ရဟန်းတို့၊ ဤသည်တို့ကား ကာမဂုဏ် ငါးပါးတို့ ဖြစ်ကုန်၏")
_NS_HEAD = ("ရဟန်းတို့၊ သင်တို့အတွက် လာဘ်ပင် ဖြစ်၏၊ ရဟန်းတို့၊ သင်တို့ ကောင်းစွာ ရပြီ၊ သင်တို့ မြတ်သော အကျင့်ကို "
            "ကျင့်ရန် အခါ ⟦b⟧ကို ရပြီ။ ရဟန်းတို့၊ တွေ့ထိမှု ခြောက်ပါးနှင့် စပ်သော {w} ဟူသည်တို့ကို ငါ မြင်ခဲ့ပြီ။ ")
_NS_HEAD2 = _NS_HEAD.replace(" ⟦b⟧", "")


def _ns(w, good):
    a, b = ("မလိုလားဖွယ်", "လိုလားဖွယ်") if not good else ("လိုလားဖွယ်", "မလိုလားဖွယ်")
    c, d = ("မချစ်ခင်ဖွယ်", "ချစ်ခင်ဖွယ်") if not good else ("ချစ်ခင်ဖွယ်", "မချစ်ခင်ဖွယ်")
    e, f_ = ("စိတ်နှင့် မတွေ့ဖွယ်", "စိတ်နှင့် တွေ့ဖွယ်") if not good else ("စိတ်နှင့် တွေ့ဖွယ်", "စိတ်နှင့် မတွေ့ဖွယ်")
    tail = lambda v: (f"{a} အရာကိုသာ {v}၏၊ {b} အရာကို မ{v}၊ {c} အရာကိုသာ {v}၏၊ {d} အရာကို မ{v}၊ {e} အရာကိုသာ {v}၏၊ "
                      f"{f_} အရာကို မ{v}")
    return (f"ထိုအရပ်၌ မျက်စိဖြင့် အဆင်းအရောင် မည်သည်ကို မြင်သည်ဖြစ်စေ၊ {tail('မြင်')}။ နားဖြင့် အသံ မည်သည်ကို "
            "ကြားသည်ဖြစ်စေ… နှာခေါင်းဖြင့် အနံ့ကို ခံသည်… လျှာဖြင့် အရသာကို ခံသည်… ကိုယ်ဖြင့် အထိအတွေ့ကို ထိသည်… "
            f"မနောဖြင့် သဘောတရားကို သိသည်ဖြစ်စေ၊ {tail('သိ')}")


for _w, _wm, _good, _var in (("nirayā", "ငရဲ", False, True), ("saggā", "နတ်ပြည်", True, False)):
    _x = [("iṭṭha", "aniṭṭha"), ("kanta", "akanta"), ("manāpa", "amanāpa")]
    _x = [(b, a) for a, b in _x] if not _good else _x
    _seq = lambda v: ", ".join(f"{p_}rūpaññeva {v} no {n_}rūpaṃ" for p_, n_ in _x)
    QUOTE_X["lābhā vo, bhikkhave, suladdhaṃ vo, bhikkhave, khaṇo vo paṭiladdho brahmacariyavāsāya! Diṭṭhā mayā, "
            f"bhikkhave, cha phassāyatanikā nāma {_w}. Tattha yaṃ kiñci cakkhunā rūpaṃ passati, {_seq('passati')}. Yaṃ "
            "kiñci sotena saddaṃ suṇāti… ghānena gandhaṃ ghāyati… jivhāya rasaṃ sāyati… kāyena phoṭṭhabbaṃ phusati… "
            f"manasā dhammaṃ vijānāti, {_seq('vijānāti')[:-1]}n"] = (
        (_NS_HEAD if _var else _NS_HEAD2).format(w=_wm) + _ns(_w, _good))
new("cha phassāyatanikā nirayā / saggā", "တွေ့ထိမှု ခြောက်ပါးနှင့် စပ်သော ငရဲ / နတ်ပြည်")
PROP_X["yadaniccaṃ taṃ dukkhaṃ, vuttaṃ bhagavatā, sabbe saṅkhārā aniccā"] = Cl(
    f"«အကြင်အရာသည် မမြဲ၊ ထိုအရာသည် ဒုက္ခ»ဟု {F.BHAGAVA} ဟောတော်မူ၍ «{ALL_SK}သည် မမြဲ»ဟုလည်း", "ဟောတော်မူ",
    "မဟောတော်မူ")
REF_X["dha. pa."] = F.REF["dha. pa."]
_FK = MS._FR_K.split("၊ ")[2:]
_FA = MS._FR_A.split("၊ ")[2:]
for _k, _m in (("dānaṃ", "ပေးလှူခြင်း"), ("sīlaṃ", "သီလ"), ("uposatho", "ဥပုသ်"), ("bhāvanā", "ဘာဝနာ"),
               ("brahmacariyaṃ", "မြတ်သော အကျင့်")):
    PROP_X[_k] = FR(f"{_m}သည်")
    PROP_X[f"{_k} aniṭṭhaphalaṃ akantaphalaṃ amanuññaphalaṃ secanakaphalaṃ dukkhudrayaṃ dukkhavipākaṃ"] = V(
        f"{_m}သည် {'၊ '.join(_FA)} အရာ")
    PROP_X[f"{_k} iṭṭhaphalaṃ kantaphalaṃ manuññaphalaṃ asecanakaphalaṃ sukhudrayaṃ sukhavipākaṃ"] = V(
        f"{_m}သည် {'၊ '.join(_FK)} အရာ")
LINES_X["Sukho viveko tuṭṭhassa, sutadhammassa passato;"] = (
    "“တရားကို ကြားနာဖူး၍ ရောင့်ရဲလျက် မြင်သိသူ၏ ဆိတ်ငြိမ်ခြင်းသည် ချမ်းသာ၏၊")
LINES_X["Abyāpajjaṃ sukhaṃ loke, pāṇabhūtesu saṃyamo."] = (
    "လောက၌ မဖျက်ဆီးခြင်း၊ သတ္တဝါတို့အပေါ် စောင့်စည်းခြင်းသည် ချမ်းသာ၏။")
LINES_X["Sukhā virāgatā loke, kāmānaṃ samatikkamo;"] = (
    "“လောက၌ တပ်မက်မှု ကင်းခြင်း၊ ကာမတို့ကို လွန်မြောက်ခြင်းသည် ချမ်းသာ၏၊")
LINES_X["Asmimānassa yo vinayo, etaṃ ve paramaṃ sukhaṃ."] = (
    "‘ငါ’ဟူသော မာနကို ပယ်ဖျောက်ခြင်း ရှိ၏၊ ဤသည်ကား အမြတ်ဆုံး ချမ်းသာ ဧကန် ဖြစ်၏ ⟦0⟧။")
LINES_X["Taṃ sukhena sukhaṃ pattaṃ, accantasukhameva taṃ;"] = (
    "“ချမ်းသာဖြင့် ချမ်းသာသို့ ရောက်၏၊ ထိုချမ်းသာသည် အဆုံးစွန် ချမ်းသာပင် ဖြစ်၏၊")
LINES_X["Tisso vijjā anuppattā, etaṃ ve paramaṃ sukhanti."] = (
    "အမှန်သိမြင်မှု သုံးပါးတို့သို့ ရောက်ပြီ၊ ဤသည်ကား အမြတ်ဆုံး ချမ်းသာ ဧကန် ဖြစ်၏”။")

PROP_X["arahā vītarāgo vītadoso vītamoho sacchikātabbaṃ sacchikataṃ"] = Cl(     # source slip (no …pe…)
    f"{ARAHA}သည် " + f"{C} ".join(m for _, m in EPI[:3]) + f"{C} မျက်မှောက်ပြုရမည့် အရာကို", *SACCHI)

# ===================================================================================== 10. kathā 18 (Anupubbābhisamaya)
section("(18) 9. Anupubbābhisamayakathā", f"(18) 9. အစဉ်အတိုင်း ထင်ထင်ရှားရှား သိမြင်ခြင်းအကြောင်း {KATHA}")
section("Anupubbābhisamayakathā", f"အစဉ်အတိုင်း ထင်ထင်ရှားရှား သိမြင်ခြင်းအကြောင်း {KATHA}")
ABHIS = new("anupubbābhisamayo", "အစဉ်အတိုင်း ထင်ထင်ရှားရှား သိမြင်ခြင်း")
PROP_X["anupubbābhisamayo"] = V(ABHIS)
MG = {"sotāpatti": "သောတာပတ္တိ", "sakadāgāmi": "သကဒါဂါမိ", "anāgāmi": "အနာဂါမိ", "arahatta": "ရဟန္တာ "}
for _k, _m in MG.items():
    _m2 = _m if _k != "arahatta" else "ရဟန္တာ "
    _mag = (f"{_m}မဂ်" if _k != "arahatta" else "ရဟန္တာ မဂ်")
    _phal = (f"{_m}ဖိုလ်" if _k != "arahatta" else "ရဟန္တာ ဖိုလ်")
    PROP_X[f"anupubbena {_k}maggaṃ bhāveti"] = Cl(f"အစဉ်အတိုင်း {_mag}ကို", "ပွားများ", "မပွားများ")
    PROP_X[f"anupubbena {_k}phalaṃ sacchikaroti"] = Cl(f"အစဉ်အတိုင်း {_phal}ကို", "မျက်မှောက်ပြု", "မျက်မှောက် မပြု")
PAT = {"sotāpattiphala": "သောတာပတ္တိဖိုလ်", "sakadāgāmiphala": "သကဒါဂါမိဖိုလ်", "anāgāmiphala": "အနာဂါမိဖိုလ်",
       "arahatta": "ရဟန္တာ ဖိုလ်"}
W("4", "^4-M-7", "Sotāpattiphalasacchikiriyāya paṭipanno", "သောတာပတ္တိဖိုလ်ကို မျက်မှောက်ပြုရန် ကျင့်ကြံသူ")
DASS = {"dukkha": f"{_DK}ကို မြင်ခြင်း", "samudaya": "ဖြစ်ပေါ်ခြင်းကို မြင်ခြင်း",
        "nirodha": "ချုပ်ငြိမ်းခြင်းကို မြင်ခြင်း", "magga": "မဂ်ကို မြင်ခြင်း"}
for _k, _m in PAT.items():
    SENT_X[f"{_k[0].upper() + _k[1:]}sacchikiriyāya paṭipanno puggalo dukkhadassanena kiṃ jahatīti?"] = (
        f"{_m}ကို မျက်မှောက်ပြုရန် ကျင့်ကြံသော {PUG}သည် {DASS['dukkha']}ဖြင့် အဘယ်ကို ပယ်သနည်း{END}")
_SMD = f"{DASS['samudaya']}ဖြင့်… {DASS['nirodha']}ဖြင့်… {DASS['magga']}ဖြင့် အဘယ်ကို ပယ်သနည်း{END}"
SENT_X["Samudayadassanena… nirodhadassanena… maggadassanena kiṃ jahatīti?"] = _SMD
SENT_X["samudayadassanena… nirodhadassanena… maggadassanena kiṃ jahatīti?"] = _SMD
TADEK = "ထိုတို့နှင့် တစ်နေရာတည်း တည်ရှိသော ကိလေသာတို့ကိုလည်း လေးပုံတစ်ပုံ ပယ်သည်"
new("tadekaṭṭhe ca kilese catubhāgaṃ jahati", TADEK)
_OL, _AN = "ရုန့်ရင်းသော", "သိမ်မွေ့သော"
_KR, _BY = "ကာမရာဂ", "ဖျက်ဆီးလိုစိတ်"
for _k, _m in (("sakkāyadiṭṭhiṃ, vicikicchaṃ, sīlabbataparāmāsaṃ", f"{_SAKK}၊ {_VC}၊ {_SILA}"),
               ("oḷārikaṃ kāmarāgaṃ, oḷārikaṃ byāpādaṃ", f"{_OL} {_KR}၊ {_OL} {_BY}"),
               ("aṇusahagataṃ kāmarāgaṃ, aṇusahagataṃ byāpādaṃ", f"{_AN} {_KR}၊ {_AN} {_BY}"),
               ("rūparāgaṃ, arūparāgaṃ, mānaṃ, uddhaccaṃ, avijjaṃ",
                f"ရုပ်၌ တပ်မက်မှု၊ ရုပ်မဲ့၌ တပ်မက်မှု၊ မာန၊ {KIL['uddhaccaṃ']}၊ {_AV}")):
    SENT_X[f"{_k[0].upper() + _k[1:]}, tadekaṭṭhe ca kilese catubhāgaṃ jahatīti."] = f"{_m}ကိုလည်းကောင်း၊ {TADEK}{END}"
CATU = "လေးပုံတစ်ပုံ"
new("catubhāgaṃ", CATU)
_FP = ("ရောက်၍ ရ၍ ပြည့်မီ၍ မျက်မှောက်ပြု၍ ပြည့်စုံစေလျက် နေ၏၊ ကိုယ်ဖြင့် တွေ့ထိ၍ နေ၏၊ "
       f"{CATU} ကိုယ်ဖြင့် မတွေ့ထိဘဲ နေ")                             # …phalappatto paṭiladdho … na kāyena phusitvā viharati


def _catu_head(p_my, phal_my):
    return (f"{CATU} {p_my} ဖြစ်၍ {CATU} {p_my} မဟုတ်၊ {CATU} {phal_my}သို့ {_FP}")


_SOT = f"{_catu_head(F.SOTAPANNA, PAT['sotāpattiphala'])}၏၊ {CATU} အများဆုံး ခုနစ်ကြိမ်သာ ပြန်လည် ဖြစ်ပေါ်သူ၊ "
_SOT += ("အမျိုးမှ အမျိုးသို့ ကူးသူ၊ မျိုးစေ့ တစ်စေ့သာ ရှိသူ၊ ဘုရားရှင်၌ မတုန်မလှုပ်သော ကြည်ညိုမှုနှင့် ပြည့်စုံသူ၊ "
         "တရားတော်၌… သံဃာတော်၌… အရိယာတို့ နှစ်သက်သော သီလတို့နှင့် ပြည့်စုံ၍ "
         f"{CATU} အရိယာတို့ နှစ်သက်သော သီလတို့နှင့်")
for _w, _bid, _l, _my in (("Sattakkhattuparamo", "^4-M-7", 37, "အများဆုံး ခုနစ်ကြိမ်သာ ပြန်လည် ဖြစ်ပေါ်သူ"),
                          ("Kolaṅkolo", "^4-M-7", 38, "အမျိုးမှ အမျိုးသို့ ကူးသူ"),
                          ("Ekabījī", "^4-M-7", 39, "မျိုးစေ့ တစ်စေ့သာ ရှိသူ")):
    W("4", _bid, _w, _my)
_SP_PI = ("catubhāgaṃ sotāpanno, catubhāgaṃ na sotāpanno, catubhāgaṃ sotāpattiphalappatto paṭiladdho adhigato "
          "sacchikato upasampajja viharati, kāyena phusitvā viharati, catubhāgaṃ na kāyena phusitvā viharati, "
          "catubhāgaṃ sattakkhattuparamo kolaṅkolo ekabījī buddhe aveccappasādena samannāgato, dhamme… saṅghe… "
          "ariyakantehi sīlehi samannāgato{c} catubhāgaṃ na ariyakantehi sīlehi samannāgato")
for _c in ("", ","):
    PROP_X[_SP_PI.format(c=_c)] = Cl(_SOT, "ပြည့်စုံ", "မပြည့်စုံ", neg=True)
PROP_X["catubhāgaṃ sakadāgāmī, catubhāgaṃ na sakadāgāmī, catubhāgaṃ sakadāgāmiphalappatto paṭiladdho adhigato "
       "sacchikato upasampajja viharati, kāyena phusitvā viharati, catubhāgaṃ na kāyena phusitvā viharati"] = Cl(
    _catu_head(F.SAKADAGAMI, PAT["sakadāgāmiphala"])[:-len(" နေ")], "နေ", "မနေ")
_PT4 = {k: v for k, v in (("antarāparinibbāyī", "သက်တမ်း၏ အလယ်သို့ မရောက်မီ ပရိနိဗ္ဗာန် ပြုသူ"),
                          ("upahaccaparinibbāyī", "သက်တမ်း၏ အလယ်ကို ကျော်ပြီးမှ ပရိနိဗ္ဗာန် ပြုသူ"),
                          ("asaṅkhāraparinibbāyī", "တိုက်တွန်းမှု မရှိဘဲ ပရိနိဗ္ဗာန် ပြုသူ"),
                          ("sasaṅkhāraparinibbāyī", "တိုက်တွန်းမှုဖြင့် ပရိနိဗ္ဗာန် ပြုသူ"))}
for _k, _l in (("Antarāparinibbāyī", 42), ("Upahaccaparinibbāyī", 43), ("Asaṅkhāraparinibbāyī", 44),
               ("Sasaṅkhāraparinibbāyī", 45)):
    W("4", "^4-M-7", _k, _PT4[_k.lower()])
_UDH = W("4", "^4-M-7", "Uddhaṃsotoakaniṭṭhagāmī", "အထက်သို့ စီးဆင်း၍ အကနိဋ္ဌ ဘုံသို့ ရောက်သူ")
_ANA = (f"{_catu_head(F.ANAGAMI, PAT['anāgāmiphala'])}၏၊ {CATU} {_PT4['antarāparinibbāyī']}… "
        f"{_PT4['upahaccaparinibbāyī']}… {_PT4['asaṅkhāraparinibbāyī']}… {_PT4['sasaṅkhāraparinibbāyī']}… {_UDH}၊ "
        f"{CATU} အထက်သို့ မစီးဆင်း၍ အကနိဋ္ဌ ဘုံသို့")
_AN_PI = ("catubhāgaṃ anāgāmī, catubhāgaṃ na anāgāmī, catubhāgaṃ anāgāmiphalappatto paṭiladdho adhigato sacchikato "
          "upasampajja viharati, kāyena phusitvā viharati, catubhāgaṃ na kāyena phusitvā viharati, catubhāgaṃ "
          "antarāparinibbāyī… upahaccaparinibbāyī… asaṅkhāraparinibbāyī… sasaṅkhāraparinibbāyī… uddhaṃsoto "
          "akaniṭṭhagāmī, catubhāgaṃ na uddhaṃsoto {n}akaniṭṭhagāmī")
PROP_X[_AN_PI.format(n="na ")] = Cl(_ANA, "မရောက်သူ", "မရောက်သူ", neg=True)
PROP_X[_AN_PI.format(n="")] = Cl(_ANA, "ရောက်သူ", "ရောက်သူ မဟုတ်", neg=True)
_ARH = (f"{_catu_head(ARAHA, PAT['arahatta'])}၏၊ {CATU} {EPI[0][1]}… {EPI[1][1]}… {EPI[2][1]}… "
        + f"{C} ".join(m for _, m in EPI[3:]) + f"{C} " + f"{C} ".join(m for _, m in TRUTH10[:-1])
        + f"{C} {TRUTH10[-1][1]}… မျက်မှောက်ပြုရမည့် အရာကို မျက်မှောက်ပြုပြီး၍ {CATU} မျက်မှောက်ပြုရမည့် အရာကို")
_AR_PI = ("catubhāgaṃ arahā, catubhāgaṃ na arahā, catubhāgaṃ arahattappatto paṭiladdho adhigato sacchikato upasampajja "
          "viharati, kāyena phusitvā viharati, catubhāgaṃ na kāyena phusitvā viharati, catubhāgaṃ vītarāgo… vītadoso… "
          "vītamoho… " + " ".join(k for k, _ in EPI[3:]) + ", " + ", ".join(k for k, _ in TRUTH10[:-1]) + ", "
          + TRUTH10[-1][0] + "… sacchikātabbaṃ sacchikataṃ, catubhāgaṃ sacchikātabbaṃ na sacchikataṃ")
PROP_X[_AR_PI] = Cl(_ARH, SACCHI[0], "မျက်မှောက် မပြုရသေး", neg=True)
_PTK = "ကျင့်ကြံဆဲသူ"                                                # paṭipannako
new("paṭipannako / phale ṭhito", f"{_PTK} / ဖိုလ်၌ တည်သူ")
_SPP = f"{PAT['sotāpattiphala']}ကို မျက်မှောက်ပြုရန် ကျင့်ကြံသော {PUG}ကို "
_SAY = ("ဆိုသင့်", "မဆိုသင့်")
SEEN = {"dukkhaṃ": (f"{_DK}ကို", "dukkhe"), "samudayaṃ": ("ဖြစ်ပေါ်ခြင်းကို", "samudaye"),
        "nirodhaṃ": ("ချုပ်ငြိမ်းခြင်းကို", "nirodhe"), "maggaṃ": ("မဂ်ကို", "magge")}
for _k, (_km, _loc) in SEEN.items():
    _dk = f"{_km} မြင်နေစဉ် {_PTK}ဟု"
    PROP_X[f"{_k} dakkhanto"] = FR(f"{_km} မြင်နေစဉ်")
    PROP_X[f"{_k} dakkhanto paṭipannakoti vattabbo"] = Cl(_dk, *_SAY)
    PROP_X[f"sotāpattiphalasacchikiriyāya paṭipanno puggalo {_k} dakkhanto paṭipannakoti vattabbo"] = Cl(
        _SPP + _dk, *_SAY)
    PROP_X[f"{_loc} diṭṭhe phale ṭhitoti vattabbo"] = Cl(f"{_km} မြင်ပြီးသောအခါ ဖိုလ်၌ တည်သူဟု", *_SAY)
    PROP_X[f"{_loc} diṭṭhe na vattabbaṃ – phale ṭhitoti vattabbo"] = Cl(
        f"{_km} မြင်ပြီးသောအခါ ဤသို့", *_SAY, neg=True, post=" – «ဖိုလ်၌ တည်သူဟု ဆိုသင့်သည်»")
    PROP_X[f"niratthiyaṃ {_k[:-1]}dassanaṃ"] = V(f"{DASS[_k[:-1]]}သည် အကျိုးမဲ့")
F.NOTE["sakavādīpucchālakkhaṇaṃ"] = f"{F.SAKAVADI}၏ အမေး၏ အမှတ်အသား"
F.NOTE["paravādīpucchālakkhaṇaṃ"] = f"{F.PARAVADI}၏ အမေး၏ အမှတ်အသား"
new("[sakavādīpucchālakkhaṇaṃ] / [paravādīpucchālakkhaṇaṃ]", F.NOTE["sakavādīpucchālakkhaṇaṃ"] + " / "
    + F.NOTE["paravādīpucchālakkhaṇaṃ"])
PROP_X["dukkhe diṭṭhe cattāri saccāni diṭṭhāni honti"] = Cl(
    f"{_DK}ကို မြင်ပြီးသောအခါ သစ္စာ လေးပါးတို့ကို", "မြင်ပြီး ဖြစ်ကြ", "မြင်ပြီး မဖြစ်ကြ")
PROP_X["dukkhasaccaṃ cattāri saccāni"] = V(f"{_DK} သစ္စာသည် သစ္စာ လေးပါး")
_SETS = [("rūpakkhandhe", "rūpakkhandho", F._KH["rūpakkhandho"], "pañcakkhandhā", f"{F.KHANDHA_W} ငါးပါး"),
         ("cakkhāyatane", "cakkhāyatanaṃ", F.AYATANA["cakkhāyatana"].my, "dvādasāyatanāni",
          f"{F.AYATANA_W} ဆယ့်နှစ်ပါး"),
         ("cakkhudhātuyā", "cakkhudhātu", F.DHATU["cakkhudhātu"].my, "aṭṭhārasa dhātuyo", f"{F.DHATU_W} ဆယ့်ရှစ်ပါး"),
         ("cakkhundriye", "cakkhundriyaṃ", F.INDRIYA["cakkhundriya"].my, "bāvīsatindriyāni",
          f"{F.INDRIYA_W} နှစ်ဆယ့်နှစ်ပါး")]
for _loc, _nom, _m, _all, _allm in _SETS:
    _d = "diṭṭhāya" if _loc.endswith("yā") else "diṭṭhe"
    _d2 = {"pañcakkhandhā": "diṭṭhā", "aṭṭhārasa dhātuyo": "diṭṭhā"}.get(_all, "diṭṭhāni")
    PROP_X[f"{_loc} aniccato {_d} {_all} aniccato {_d2} honti"] = Cl(
        f"{_m}ကို မမြဲဟု မြင်ပြီးသောအခါ {_allm}တို့ကို မမြဲဟု", "မြင်ပြီး ဖြစ်ကြ", "မြင်ပြီး မဖြစ်ကြ")
    PROP_X[f"{_nom} {_all}"] = V(f"{_m}သည် {_allm}")
F.WITNESS.setdefault("Dvādasāyatanāni", ("2", "^2-154", f"{F.AYATANA_W} ဆယ့်နှစ်ပါး"))
_NUMN = {"catūhi": "လေး", "aṭṭhahi": "ရှစ်", "dvādasahi": "ဆယ့်နှစ်", "catucattārīsāya": "လေးဆယ့်လေး",
         "sattasattatiyā": "ခုနစ်ဆယ့်ခုနစ်"}
_NUMF = {"cattāri": "လေး", "aṭṭha": "ရှစ်", "dvādasa": "ဆယ့်နှစ်", "catucattārīsaṃ": "လေးဆယ့်လေး",
         "sattasattati": "ခုနစ်ဆယ့်ခုနစ်"}
for _k, _m in _NUMN.items():
    PROP_X[f"{_k} ñāṇehi sotāpattiphalaṃ sacchikaroti"] = Cl(
        f"ဉာဏ် {_m}ပါးဖြင့် {PAT['sotāpattiphala']}ကို", "မျက်မှောက်ပြု", "မျက်မှောက် မပြု")
for _k, _m in _NUMF.items():
    PROP_X[f"{_k} sotāpattiphalāni"] = V(f"{PAT['sotāpattiphala']} {_m}ပါး", EXIST)
QUOTE_X["seyyathāpi, bhikkhave, mahāsamuddo anupubbaninno anupubbapoṇo anupubbapabbhāro, na āyatakeneva papāto; "
        "evameva kho, bhikkhave, imasmiṃ dhammavinaye anupubbasikkhā anupubbakiriyā anupubbapaṭipadā, na "
        "āyatakeneva aññāpaṭivedho"] = (
    "ရဟန်းတို့၊ ဥပမာ သမုဒ္ဒရာသည် အစဉ်အတိုင်း နိမ့်ဆင်း၏၊ အစဉ်အတိုင်း ညွတ်ကိုင်း၏၊ အစဉ်အတိုင်း စောင်း၏၊ "
    "ရုတ်တရက် ချောက်ကမ်းပါး မဟုတ်၊ ရဟန်းတို့၊ ထို့အတူပင် ဤ ဓမ္မ ဝိနည်း၌ အစဉ်အတိုင်း ကျင့်ခြင်း၊ အစဉ်အတိုင်း "
    "ပြုခြင်း၊ အစဉ်အတိုင်း အကျင့် ရှိ၏၊ ရုတ်တရက် ရဟန္တာ ဖိုလ်ကို ထိုးထွင်း သိခြင်း မဟုတ်")
REF_NOTE_X["dhammapade"] = F.REF_NOTE["dhammapade"]
LINES_X["Anupubbena medhāvī, thokaṃ thokaṃ khaṇe khaṇe;"] = "“ပညာရှိသည် အစဉ်အတိုင်း အနည်းငယ် အနည်းငယ်၊ ခဏခဏ၊"
LINES_X["Kammāro rajatasseva, niddhame malamattanoti."] = (
    "ပန်းထိမ်သည် ငွေ၏ အညစ်အကြေးကို ဖယ်ရှားသကဲ့သို့ မိမိ၏ အညစ်အကြေးကို ဖယ်ရှားရာ၏”ဟူ၍ ⟦0⟧။")
SENT_X["Nanvāyasmā gavampati thero bhikkhū etadavoca – sammukhā metaṃ, āvuso, bhagavato sutaṃ sammukhā paṭiggahitaṃ – "
       "yo, bhikkhave, dukkhaṃ passati dukkhasamudayampi so passati, dukkhanirodhampi passati, dukkhanirodhagāminiṃ "
       "paṭipadampi passati; yo dukkhasamudayaṃ passati dukkhampi so passati, dukkhanirodhampi passati, "
       "dukkhanirodhagāminiṃ paṭipadampi passati; yo dukkhanirodhaṃ passati dukkhampi so passati, dukkhasamudayampi "
       "passati, dukkhanirodhagāminiṃ paṭipadampi passati; yo dukkhanirodhagāminiṃ paṭipadaṃ passati dukkhampi so "
       "passati, dukkhasamudayampi passati, dukkhanirodhampi passatīti!"] = (
    "အသျှင် ဂဝမ္ပတိ ထေရ်သည် ရဟန်းတို့အား ဤသို့ ပြောခဲ့သည် မဟုတ်လော – “ငါ့ရှင်တို့၊ ဤစကားကို ငါသည် မြတ်စွာဘုရား၏ "
    "မျက်မှောက်၌ ကြားခဲ့ရ၏၊ မျက်မှောက်၌ ခံယူခဲ့ရ၏ – ‘ရဟန်းတို့၊ အကြင်သူသည် ဒုက္ခကို မြင်၏၊ ထိုသူသည် ဒုက္ခ "
    "ဖြစ်ပေါ်ခြင်းကိုလည်း မြင်၏၊ ဒုက္ခ ချုပ်ငြိမ်းခြင်းကိုလည်း မြင်၏၊ ဒုက္ခ ချုပ်ငြိမ်းခြင်းသို့ ရောက်ကြောင်း "
    "အကျင့်ကိုလည်း မြင်၏၊ အကြင်သူသည် ဒုက္ခ ဖြစ်ပေါ်ခြင်းကို မြင်၏၊ ထိုသူသည် ဒုက္ခကိုလည်း မြင်၏၊ ဒုက္ခ "
    "ချုပ်ငြိမ်းခြင်းကိုလည်း မြင်၏၊ ဒုက္ခ ချုပ်ငြိမ်းခြင်းသို့ ရောက်ကြောင်း အကျင့်ကိုလည်း မြင်၏၊ အကြင်သူသည် ဒုက္ခ "
    "ချုပ်ငြိမ်းခြင်းကို မြင်၏၊ ထိုသူသည် ဒုက္ခကိုလည်း မြင်၏၊ ဒုက္ခ ဖြစ်ပေါ်ခြင်းကိုလည်း မြင်၏၊ ဒုက္ခ "
    "ချုပ်ငြိမ်းခြင်းသို့ ရောက်ကြောင်း အကျင့်ကိုလည်း မြင်၏၊ အကြင်သူသည် ဒုက္ခ ချုပ်ငြိမ်းခြင်းသို့ ရောက်ကြောင်း "
    "အကျင့်ကို မြင်၏၊ ထိုသူသည် ဒုက္ခကိုလည်း မြင်၏၊ ဒုက္ခ ဖြစ်ပေါ်ခြင်းကိုလည်း မြင်၏၊ ဒုက္ခ ချုပ်ငြိမ်းခြင်းကိုလည်း "
    "မြင်၏’”ဟူ၍။")

# ===================================================================================== 10. kathā 19 (Vohāra)
section("(19) 10. Vohārakathā", f"(19) 10. ပြောဆို သုံးနှုန်းခြင်းအကြောင်း {KATHA}")
section("Vohārakathā", f"ပြောဆို သုံးနှုန်းခြင်းအကြောင်း {KATHA}")
VOH = new("buddhassa bhagavato vohāro", f"ဘုရားရှင် {F.BHAGAVA}၏ ပြောဆို သုံးနှုန်းခြင်း")
PROP_X["buddhassa bhagavato vohāro lokuttaro"] = V(f"{VOH}သည် {LOKUTTARA} အရာ")
_HIT = ("ထိခိုက်", "မထိခိုက်")
PROP_X["lokuttare sote paṭihaññati no lokiye, lokuttarena viññāṇena paṭivijānanti no lokiyena, sāvakā paṭivijānanti "
       "no puthujjanā"] = Cl(
    f"{LOKUTTARA} နား၌ ထိခိုက်၏၊ {LOKIYA} နား၌ မထိခိုက်၊ {LOKUTTARA} သိစိတ်ဖြင့် ထိုးထွင်း သိကြ၏၊ {LOKIYA} "
    f"သိစိတ်ဖြင့် ထိုးထွင်း မသိကြ၊ တပည့်တို့ ထိုးထွင်း သိကြ၏၊ {PUTHU}တို့", "ထိုးထွင်း သိကြ", "ထိုးထွင်း မသိကြ",
    neg=True)
PROP_X["buddhassa bhagavato vohāro lokiye sote paṭihaññati"] = Cl(f"{VOH}သည် {LOKIYA} နား၌", *_HIT)
PROP_X["buddhassa bhagavato vohāraṃ lokiyena viññāṇena paṭivijānanti"] = Cl(
    f"{VOH}ကို {LOKIYA} သိစိတ်ဖြင့်", "ထိုးထွင်း သိကြ", "ထိုးထွင်း မသိကြ")
PROP_X["buddhassa bhagavato vohāraṃ puthujjanā paṭivijānanti"] = Cl(
    f"{VOH}ကို {PUTHU}တို့", "ထိုးထွင်း သိကြ", "ထိုးထွင်း မသိကြ")
PROP_X["maggo phalaṃ nibbānaṃ, sotāpattimaggo sotāpattiphalaṃ, sakadāgāmimaggo sakadāgāmiphalaṃ, anāgāmimaggo "
       "anāgāmiphalaṃ, arahattamaggo arahattaphalaṃ, satipaṭṭhānaṃ sammappadhānaṃ iddhipādo indriyaṃ balaṃ "
       "bojjhaṅgo"] = V(
    f"မဂ်၊ ဖိုလ်၊ {F.NIBBANA}၊ သောတာပတ္တိမဂ်၊ {PAT['sotāpattiphala']}၊ သကဒါဂါမိမဂ်၊ {PAT['sakadāgāmiphala']}၊ "
    f"အနာဂါမိမဂ်၊ {PAT['anāgāmiphala']}၊ ရဟန္တာ မဂ်၊ {PAT['arahatta']}၊ {SATIPATTHANA}၊ {_SP}၊ {_ID}၊ "
    f"{F.INDRIYA_W}၊ စွမ်းအား၊ {_BJW}")
PROP_X["atthi keci buddhassa bhagavato vohāraṃ suṇanti"] = V(f"{VOH}ကို ကြားကြသူ အချို့", EXIST)
for _v, _vm in (("rajjeyyuṃ", "တပ်မက်ကြရာ"), ("dusseyyuṃ", "အမျက်ထွက်ကြရာ"), ("muyheyyuṃ", "တွေဝေကြရာ")):
    PROP_X[f"atthi keci buddhassa bhagavato vohāre {_v}"] = V(f"{VOH}၌ {_vm}သူ အချို့", EXIST)
_LD = f"{LOKUTTARA} သဘောတရားသည်"
PROP_X["lokuttaro dhammo sotaviññeyyo, sotasmiṃ paṭihaññati, sotassa āpāthaṃ āgacchati"] = Cl(
    f"{_LD} နားဖြင့် သိနိုင်သော အရာ ဖြစ်၏၊ နား၌ ထိခိုက်၏၊ နား၏ အာရုံ နယ်ပယ်သို့", "ရောက်လာ", "မရောက်လာ")
PROP_X["lokuttaro dhammo na sotaviññeyyo, na sotasmiṃ paṭihaññati, na sotassa āpāthaṃ āgacchati"] = Cl(
    f"{_LD} နားဖြင့် သိနိုင်သော အရာ မဟုတ်၊ နား၌ မထိခိုက်၊ နား၏ အာရုံ နယ်ပယ်သို့", "ရောက်လာ", "မရောက်လာ",
    neg=True)
_RG = ["ရာဂ ဖြစ်ကြောင်း", "တပ်မက်ဖွယ်ကောင်းသော", "လိုချင်ဖွယ်ကောင်းသော", "မူးယစ်စေတတ်သော", "နှောင်ဖွဲ့တတ်သော",
       "တွေဝေစေတတ်သော"]
_DS = ["ဒေါသ ဖြစ်ကြောင်း", "အမျက် ဖြစ်ကြောင်း", "ထိခိုက်မှု ဖြစ်ကြောင်း"]
_MH_POS = ["မောဟ ဖြစ်ကြောင်း", "မသိခြင်းကို ပြုတတ်သော", "မျက်စိ မမြင်ခြင်းကို ပြုတတ်သော", "ပညာကို ချုပ်ငြိမ်းစေတတ်သော",
           "ပင်ပန်းခြင်း၏ ဘက်၌ ပါသော", "နိဗ္ဗာန်သို့ မပို့ဆောင်တတ်သော"]
_MH_NEG = ["မောဟ ဖြစ်ကြောင်း မဟုတ်", "မသိခြင်းကို ပြုတတ်သည် မဟုတ်", "မျက်စိ မမြင်ခြင်းကို ပြုတတ်သည် မဟုတ်",
           "ပညာကို တိုးပွားစေတတ်သော", "မပင်ပန်းခြင်း၏ ဘက်၌ ပါသော", "နိဗ္ဗာန်သို့ ပို့ဆောင်တတ်သော"]
PROP_X["lokuttaro dhammo rāgaṭṭhāniyo rajanīyo kamanīyo madanīyo bandhanīyo mucchanīyo"] = V(
    f"{_LD} " + f"{C} ".join(_RG) + " အရာ")
PROP_X["lokuttaro dhammo na rāgaṭṭhāniyo na rajanīyo na kamanīyo na madanīyo na bandhanīyo na mucchanīyo"] = V(
    f"{_LD} " + f" မဟုတ်{C} ".join(_RG[:1] + [x + " အရာ" for x in _RG[1:]]), neg=True)
PROP_X["lokuttaro dhammo dosaṭṭhāniyo kopaṭṭhāniyo paṭighaṭṭhāniyo"] = V(f"{_LD} " + f"{C} ".join(_DS) + " အရာ")
PROP_X["lokuttaro dhammo na dosaṭṭhāniyo na kopaṭṭhāniyo na paṭighaṭṭhāniyo"] = V(
    f"{_LD} " + f" မဟုတ်{C} ".join(_DS), neg=True)
PROP_X["lokuttaro dhammo mohaṭṭhāniyo aññāṇakaraṇo acakkhukaraṇo paññānirodhiko vighātapakkhiko "
       "anibbānasaṃvattaniko"] = V(f"{_LD} " + f"{C} ".join(_MH_POS) + " အရာ")
PROP_X["lokuttaro dhammo na mohaṭṭhāniyo na aññāṇakaraṇo na acakkhukaraṇo paññāvuddhiko avighātapakkhiko "
       "nibbānasaṃvattaniko"] = V(f"{_LD} " + f"{C} ".join(_MH_NEG) + " အရာ")
_GOLD = "ရွှေ အပုံ"
for _k, _m in (("sovaṇṇamayāya", "ရွှေဖြင့် ပြုလုပ်သော"), ("elaṇḍiyāya", "ကြက်ဆူပင်ဖြင့် ပြုလုပ်သော")):
    SENT_X[f"Labbhā {_k} laṭṭhiyā dhaññapuñjopi suvaṇṇapuñjopi ācikkhitunti?"] = (
        f"{_m} တုတ်ဖြင့် စပါး အပုံကိုလည်း၊ {_GOLD}ကိုလည်း ညွှန်ပြနိုင်သလော{END}")
for _k, _m in (("lokuttarena", LOKUTTARA), ("lokiyena", LOKIYA)):
    SENT_X[f"Evamevaṃ bhagavā {_k} vohārena lokiyampi lokuttarampi dhammaṃ voharatīti."] = (
        f"{MS.EVAM} {F.BHAGAVA}သည် {_m} ပြောဆို သုံးနှုန်းခြင်းဖြင့် {LOKIYA} သဘောတရားကိုလည်း၊ {LOKUTTARA} "
        f"သဘောတရားကိုလည်း ပြောဆို သုံးနှုန်းတော်မူ၏{END}")
_LV = f"{LOKIYA} အရာကို ပြောဆိုသောအခါ"
_UV = f"{LOKUTTARA} အရာကို ပြောဆိုသောအခါ"
PROP_X["buddhassa bhagavato vohāro lokiyaṃ voharantassa lokiyo hoti, lokuttaraṃ voharantassa lokuttaro hoti"] = V(
    f"{VOH}သည် {_LV} {LOKIYA} အရာ ဖြစ်၏၊ {_UV} {LOKUTTARA} အရာ")
PROP_X["lokiyaṃ voharantassa lokiye sote paṭihaññati, lokuttaraṃ voharantassa lokuttare sote paṭihaññati; lokiyaṃ "
       "voharantassa lokiyena viññāṇena paṭivijānanti, lokuttaraṃ voharantassa lokuttarena viññāṇena paṭivijānanti; "
       "lokiyaṃ voharantassa puthujjanā paṭivijānanti, lokuttaraṃ voharantassa sāvakā paṭivijānanti"] = Cl(
    f"{_LV} {LOKIYA} နား၌ ထိခိုက်၏၊ {_UV} {LOKUTTARA} နား၌ ထိခိုက်၏၊ {_LV} {LOKIYA} သိစိတ်ဖြင့် ထိုးထွင်း သိကြ၏၊ "
    f"{_UV} {LOKUTTARA} သိစိတ်ဖြင့် ထိုးထွင်း သိကြ၏၊ {_LV} {PUTHU}တို့ ထိုးထွင်း သိကြ၏၊ {_UV} တပည့်တို့",
    "ထိုးထွင်း သိကြ", "ထိုးထွင်း မသိကြ")
PROP_X["bhagavā lokiyampi lokuttarampi dhammaṃ voharati"] = Cl(
    f"{F.BHAGAVA}သည် {LOKIYA} သဘောတရားကိုလည်း၊ {LOKUTTARA} သဘောတရားကိုလည်း", "ပြောဆို သုံးနှုန်းတော်မူ",
    "ပြောဆို မသုံးနှုန်းတော်မူ")
_VP = [("maggaṃ", "maggo", "မဂ်"), ("amaggaṃ", "amaggo", "မဂ် မဟုတ်သော အရာ"), ("phalaṃ", "phalaṃ", "ဖိုလ်"),
       ("aphalaṃ", "aphalaṃ", "ဖိုလ် မဟုတ်သော အရာ"), ("nibbānaṃ", "nibbānaṃ", F.NIBBANA),
       ("anibbānaṃ", "anibbānaṃ", f"{F.NIBBANA} မဟုတ်သော အရာ"), ("saṅkhataṃ", "saṅkhataṃ", f"{F.SANKHATA} အရာ"),
       ("asaṅkhataṃ", "asaṅkhataṃ", f"{F.ASANKHATA} အရာ"), ("rūpaṃ", "rūpaṃ", F.RUPA.my),
       ("arūpaṃ", "arūpaṃ", f"{F.RUPA.my} မဟုတ်သော အရာ"), ("vedanaṃ", "vedanā", F.VEDANA.my),
       ("avedanaṃ", "avedanā", f"{F.VEDANA.my} မဟုတ်သော အရာ"), ("saññaṃ", "saññā", F.SANNA.my),
       ("asaññaṃ", "asaññā", f"{F.SANNA.my} မဟုတ်သော အရာ"), ("saṅkhāre", "saṅkhārā", F.SANKHARA.my),
       ("asaṅkhāre", "asaṅkhārā", f"{F.SANKHARA.my} မဟုတ်သော အရာ"), ("viññāṇaṃ", "viññāṇaṃ", F.VINNANA.my),
       ("aviññāṇaṃ", "aviññāṇaṃ", f"{F.VINNANA.my} မဟုတ်သော အရာ")]
_vp_pi = ", ".join(f"{a} voharantassa {b} {'honti' if b.endswith('ārā') else 'hoti'}" for a, b, _ in _VP)
_vp_my = [f"{m}ကို ပြောဆိုသောအခါ {m} ဖြစ်၏" for _, _, m in _VP]
PROP_X[_vp_pi] = V(f"{C} ".join(_vp_my)[:-len(" ဖြစ်၏")])

# ===================================================================================== 10. kathā 20 (Nirodha)
section("(20) 11. Nirodhakathā", f"(20) 11. ချုပ်ငြိမ်းခြင်းအကြောင်း {KATHA}")
section("Nirodhakathā", f"ချုပ်ငြိမ်းခြင်းအကြောင်း {KATHA}")
_N2 = f"{F.NUM_MY[2]}{F.CL}"
for _k, _m in (("nirodhā", "ချုပ်ငြိမ်းခြင်း"), ("dukkhanirodhā", f"{_DK} ချုပ်ငြိမ်းခြင်း"),
               ("nirodhasaccāni", "ချုပ်ငြိမ်းခြင်း သစ္စာ"), ("dukkhasaccāni", f"{_DK} သစ္စာ"),
               ("samudayasaccāni", "ဖြစ်ပေါ်ခြင်း သစ္စာ"), ("maggasaccāni", "မဂ် သစ္စာ"),
               ("tāṇāni", "ကာကွယ်ရာ"), ("leṇāni", "ပုန်းအောင်းရာ"), ("saraṇāni", "ကိုးကွယ်ရာ"),
               ("parāyaṇāni", "မှီခိုရာ"), ("accutāni", "မစုတေသော အရာ"), ("amatāni", "အမြိုက်"),
               ("nibbānāni", F.NIBBANA)):
    PROP_X[f"dve {_k}"] = V(f"{_m} {_N2}", EXIST)
    PROP_X[_k] = V(f"{_m} {_N2}", EXIST)
new("tāṇa / leṇa / saraṇa / parāyaṇa / accuta / amata", "ကာကွယ်ရာ / ပုန်းအောင်းရာ / ကိုးကွယ်ရာ / မှီခိုရာ / "
    "မစုတေသော အရာ / အမြိုက်")
PROP_X["atthi dvinnaṃ nibbānānaṃ uccanīcatā hīnapaṇītatā ukkaṃsāvakaṃso sīmā vā bhedo vā rāji vā antarikā vā"] = V(
    f"{F.NIBBANA} {_N2}တို့၏ မြင့်ခြင်း နိမ့်ခြင်း၊ ယုတ်ခြင်း မြတ်ခြင်း၊ ထူးကဲခြင်း ညံ့ဖျင်းခြင်း၊ နယ်နိမိတ်ဖြစ်စေ၊ "
    "ကွဲပြားခြင်းဖြစ်စေ၊ မျဉ်းကြောင်းဖြစ်စေ၊ ကြားအပိုင်းဖြစ်စေ", EXIST)
PSN = "ပြန်လည် ဆင်ခြင်၍"                                             # paṭisaṅkhā (termbase «ပြန်လည် ဆင်ခြင်ခြင်း»)
APSN = "ပြန်လည် မဆင်ခြင်ဘဲ"
PROP_X["appaṭisaṅkhāniruddhe saṅkhāre paṭisaṅkhā nirodhenti"] = Cl(
    f"{APSN} ချုပ်ငြိမ်းသော {F.SANKHARA.my}ကို {PSN}", "ချုပ်ငြိမ်းစေကြ", "မချုပ်ငြိမ်းစေကြ")
for _k, _m in (("appaṭisaṅkhāniruddhāpi", f"{APSN} ချုပ်ငြိမ်းသော"), ("paṭisaṅkhāniruddhāpi", f"{PSN} ချုပ်ငြိမ်းသော")):
    PROP_X[f"{_k} saṅkhārā accantabhaggā"] = V(f"{_m} {F.SANKHARA.my}သည်လည်း လုံးဝ ပျက်စီးပြီးသော အရာ")
for _k, _m in (("paṭisaṅkhāniruddhāpi", f"{PSN} ချုပ်ငြိမ်းသော"), ("paṭisaṅkhāniruddhā", f"{PSN} ချုပ်ငြိမ်းသော"),
               ("appaṭisaṅkhāniruddhā", f"{APSN} ချုပ်ငြိမ်းသော")):
    _l = "လည်း" if _k.endswith("pi") else ""
    PROP_X[f"{_k} saṅkhārā ariyamaggaṃ āgamma niruddhā"] = Cl(
        f"{_m} {F.SANKHARA.my}သည်{_l} အရိယာ မဂ်ကို အကြောင်းပြု၍", "ချုပ်ငြိမ်းပြီး", "မချုပ်ငြိမ်းသေး")
    PROP_X[f"{_k} saṅkhārā na puna uppajjanti"] = Cl(f"{_m} {F.SANKHARA.my}သည် နောက်တစ်ဖန်", "ဖြစ်ပေါ်ကြ",
                                                     "မဖြစ်ပေါ်ကြ", neg=True)
VAR_X10["paṭisaṅkhāniruddhā"] = F.PATHA
LINES_X["Parūpahāro aññāṇaṃ, kaṅkhā paravitāraṇā;"] = (
    f"{LST['parūpahāro']}၊ {ANNANA}၊ {KANKHA}၊ {PVT}၊")
LINES_X["Vacībhedo dukkhāhāro, cittaṭṭhiti ca kukkuḷā;"] = (
    f"{VB}၊ ဒုက္ခဟု ဆိုခြင်း၊ စိတ်၏ တည်ခြင်းနှင့် ပြာပူ၊")
LINES_X["Anupubbābhisamayo, vohāro ca nirodhakoti."] = (
    f"{ABHIS}၊ ပြောဆို သုံးနှုန်းခြင်းနှင့် ချုပ်ငြိမ်းခြင်း{END}")


# ===================================================================================== run
VAR_X = {"khandhadhātuāyatananti": F.PATHA}
VAR_X.update(VAR_X7)
VAR_X.update(VAR_X9)
VAR_X.update(VAR_X10)


def install():
    F.VAR_KIND.update(VAR_X)
    F.REF.update(REF_X)
    F.REF_NOTE.update(REF_NOTE_X)
    F._REF_RE = re.compile(r"(?P<r>pu\. pa\. mātikā|a\. ni\.|ma\. ni\.|dī\. ni\.|saṃ\. ni\.|itivu\.|su\. ni\.|"
                           r"cūḷani\.|dha\. pa\.|pu\. pa\.|mahāva\.|udā\.) (?P<n>[\d.\-]+)")
    F.PROP.update(PROP_X)
    F.QUOTE.update(QUOTE_X)
    F.SENT.update(SENT_X)
    F.LINES.update(LINES_X)
    F.ANCHOR.update(ANCHOR_X)
    F.HEAD.update(HEAD_X)
    F.COLO.update(COLO_X)


install()


def run(name, misses=False):
    src = (PALI / name).read_text(encoding="utf-8-sig")
    out, bad = [], 0
    for ln, line in enumerate(src.splitlines(), 1):
        if not line.strip():
            out.append("")
            continue
        try:
            my = unicodedata.normalize("NFC", F.translate_line(line))
        except F.Miss as e:
            bad += 1
            print(f"{name}:{ln}: MISS {e}")
            if not misses:
                sys.exit(1)
            out.append("?")
            continue
        errs = MS.line_check(line, my)
        if errs:
            bad += 1
            print(f"{name}:{ln}: CHECK {errs}\n  P: {line[:300]}\n  M: {my[:300]}")
            if not misses:
                sys.exit(1)
        out.append(my)
    return "\n".join(out).rstrip("\n") + "\n", bad


def units(name):
    """Every failing unit of a chapter (scratch listing; writes nothing)."""
    cnt = collections.Counter()
    for line in (PALI / name).read_text(encoding="utf-8-sig").splitlines():
        if not line.strip():
            continue
        m = F.ID_RE.search(line)
        body = (line[:m.start()] if m else line).strip()
        if F.HEAD_RE.fullmatch(body):
            if body.split(" ", 1)[1] not in F.HEAD:
                cnt["HEAD " + body] += 1
            continue
        clean = F.BR_RE.sub("", body)
        key = F.norm_pe(F.strip_q(clean))
        if key in F.LINES or key.rstrip(".") in F.COLO:
            continue
        if any(rx.fullmatch(key) for rx, fn in F.LINE_FRAMES):
            try:
                F.line_my(body)
            except F.Miss as e:
                cnt["LINEFRAME " + str(e)] += 1
            continue
        for a, b in F.split_sents(clean):
            u = F.strip_q(clean[a:b].strip())
            try:
                F.unit_my(u)
            except F.Miss as e:
                msg = str(e)
                for rx, fn in F.FRAMES:
                    mm = rx.fullmatch(F.norm_pe(u))
                    if mm:
                        try:
                            fn(mm)
                        except F.Miss as e2:
                            msg = str(e2)
                            break
                cnt[msg] += 1
    for k, v in sorted(cnt.items(), key=lambda x: -x[1]):
        print(v, k)
    print(len(cnt), "distinct")


def main():
    args = sys.argv[1:]
    misses = "--misses" in args
    names = [a for a in args if not a.startswith("--")] or NAMES_OUT
    if "--units" in args:
        for name in names:
            units(name)
        return
    total = 0
    for name in names:
        text, bad = run(name, misses)
        total += bad
        if not misses and not bad:
            OUT.mkdir(parents=True, exist_ok=True)
            assert "\n\n\n" not in text
            (OUT / name).write_text(text, encoding="utf-8")
            print(f"wrote {name}")
    if misses:
        print(f"{total} misses")


# lines with an unclosed quotation in the Pāli (source slip): the sentences are cut by hand and rendered by the
# engine one by one (the quotation closed where its «ti» ends it)
OPEN_Q = {
    "Na vattabbaṃ – rūpaṃ hevatthi, heva natthīti; vedanā… saññā… saṅkhārā… viññāṇaṃ hevatthi, heva natthīti? Āmantā. "
    "Rūpaṃ vedanāti hevatthi… rūpaṃ saññāti hevatthi… rūpaṃ saṅkhārāti hevatthi… rūpaṃ viññāṇanti hevatthi… vedanā… "
    "saññā… saṅkhārā… viññāṇaṃ rūpanti hevatthi… viññāṇaṃ vedanāti hevatthi… viññāṇaṃ saññāti hevatthi… viññāṇaṃ "
    "saṅkhārāti hevatthīti? Na hevaṃ vattabbe… tena hi rūpaṃ hevatthi, heva natthi; vedanā… saññā… saṅkhārā… "
    "viññāṇaṃ hevatthi, heva natthīti.": [
        "Na vattabbaṃ – rūpaṃ hevatthi, heva natthīti; vedanā… saññā… saṅkhārā… viññāṇaṃ hevatthi, heva natthīti?",
        "Āmantā.",
        "Rūpaṃ vedanāti hevatthi… rūpaṃ saññāti hevatthi… rūpaṃ saṅkhārāti hevatthi… rūpaṃ viññāṇanti hevatthi… "
        "vedanā… saññā… saṅkhārā… viññāṇaṃ rūpanti hevatthi… viññāṇaṃ vedanāti hevatthi… viññāṇaṃ saññāti "
        "hevatthi… viññāṇaṃ saṅkhārāti hevatthīti?",
        "Na hevaṃ vattabbe…",
        "tena hi rūpaṃ hevatthi, heva natthi; vedanā… saññā… saṅkhārā… viññāṇaṃ hevatthi, heva natthīti."],
}
OPEN_Q.update(OPEN_Q_X)
for _k, _us in OPEN_Q.items():
    assert " ".join(_us) == _k
    F.LINES[_k] = " ".join(F.unit_my(u) for u in _us)


if __name__ == "__main__":
    main()
