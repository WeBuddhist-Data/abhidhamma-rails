"""Burmese zero-shot SAMPLE of pi-7 (Paṭṭhāna, «အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ»): 1-00-paccaya, 1-02-vedanattika.

usage: python3 -I -X utf8 make_sample.py [chapter ...] [--dev] [--terms]
Every line is generated from the Pāli by my7_formulas.translate() through the shared frames of my7_formulas.py
and the sentence templates below (SK: a whole unit; SKF: a fragment between «…»; HLINES: a whole line or heading).
Templates hold only this sample's unique sentences; their slots ({T1} triad term, {C1.ab} condition …) are filled
by the shared functions, and every repeated phrase comes from the module or the PH table, so identical Pāli gets
identical Burmese. A sentence that no frame or template matches stops the run (Miss): nothing is guessed.
--dev lists every unmatched skeleton instead of stopping. --terms rewrites my7-zeroshot-terms.md.
Each chapter is written as soon as it is complete. Model for later chapters: copy this file and change the tables.
"""
import pathlib
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import my7_formulas as F  # noqa: E402

ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-7_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters"
NAMES = ["1-00-paccaya.md", "1-02-vedanattika.md"]
C, END, PE = F.C, F.END, F.PE

# ===================================================================================== shared phrases of this sample
PH = {
    "vitthārito": "အကျယ် ချဲ့ထားသည့်အတိုင်း",   # yathā … vitthārito (pi-2 «… အကျယ် ဖော်ပြထားသည့်အတိုင်း»)
    "evaṃ": F.W("evaṃ sabbepi tikā vitthāretabbā", "ထိုနည်းတူ", "2"),       # evaṃ (after yathā …)
    "vitthāretabbo": F.W("vitthāretabbaṃ", "အကျယ် ချဲ့ရမည်", "5"),   # vitthāretabbo / -baṃ «… အကျယ် ချဲ့ရမည်»
    "vācanāmaggena": "ရွတ်ဆိုသည့် နည်းလမ်းအတိုင်း",          # NEW
    "sajjhāyamaggena": "သရဇ္ဈာယ်သည့် နည်းလမ်းအတိုင်း",       # NEW (a different word from vācanāmagga)
    "asammuyhantena": "မရောထွေးစေဘဲ",                       # NEW
    "anulome": F.HEAD["Paccayānulomaṃ"].split()[-2] + " ပုံစံ၌",   # «အဟုတ်ပြ ပုံစံ၌»
    "paccanīye": "အငြင်းပြ ပုံစံ၌",
    "anulomapaccanīye": "အဟုတ်ပြ အငြင်းပြ ပုံစံ၌",
    "ekekassa padassa": f"{F.PADA} တစ်ခုစီ၏",
    "saṃkhittā": "အကျဉ်းချုပ်ထားသည်",
    "gaṇetabbaṃ": "ရေတွက်ရမည်",
}
MUL = {"eka": "Ekamūlakaṃ", "du": "Dumūlakaṃ", "ti": "Timūlakaṃ", "catu": "Catumūlakaṃ", "pañca": "Pañcamūlakaṃ",
       "sabba": "Sabbamūlakaṃ"}


def mul(k):
    return F.HEAD[MUL[k]]


MUL_LIST6 = (C + " ").join(mul(k) for k in ("eka", "du", "ti", "catu", "pañca", "sabba"))
MUL_LIST4 = (C + " ").join(mul(k) for k in ("eka", "du", "ti", "catu"))

# ===================================================================================== whole lines / headings
HLINES = {}
COLO = {
    "Paccayaniddeso.": F.heading("Paccayaniddeso") + END,
    "Pucchāvāro.": F.heading("Pucchāvāro") + END,
    "Ekamūlakaṃ.": mul("eka") + END,
    "Dumūlakaṃ.": mul("du") + END,
    "Timūlakaṃ.": mul("ti") + END,
    "Catumūlakaṃ.": mul("catu") + END,
    "Hetumūlakaṃ.": F.heading("Hetumūlakaṃ") + END,
    "Nahetumūlakaṃ.": F.heading("Nahetumūlakaṃ") + END,
    "Hetupaccayavāro.": F.cname("hetu") + F.VARA + END,
    "Niddesavāre tevīsatipaccayā.": f"{F.HEAD['Paccayaniddeso']}၌ {F.PACCAYA} နှစ်ဆယ့်သုံးပါး{END}",
    "Paṭiccavāro.": F.HEAD["Paṭiccavāro"] + END,
    "Sampayuttavāro.": F.HEAD["Sampayuttavāro"] + END,
    "Paccanīyagaṇanā.": "အငြင်းပြ ပုံစံ၏ ရေတွက်ချက်" + END,        # gaṇanā «ရေတွက်ချက်»
    "Anulomapaccanīyaṃ.": "အဟုတ်ပြ အငြင်းပြ ပုံစံ" + END,
    "Anulomapaccanīyagaṇanā.": "အဟုတ်ပြ အငြင်းပြ ပုံစံ၏ ရေတွက်ချက်" + END,
    "Paccanīyānulomaṃ.": "အငြင်းပြ အဟုတ်ပြ ပုံစံ" + END,
    "Paccanīyaṃ.": "အငြင်းပြ ပုံစံ" + END,
    "Pañhāvārassa anulomaṃ.": f"{F.HEAD['Pañhāvāro']}၏ အဟုတ်ပြ ပုံစံ{END}",
    "Vedanāttikaṃ niṭṭhitaṃ.": F.finished(F.TIKA_NAME["Vedanāttikaṃ"]),
}
HLINES.update(COLO)
# the verse (four lines; the last line names the order)
V1 = f"{F.TIKA}တို့၏ မြတ်သော {F.TITLE}၊ {F.DUKA}တို့၏ အမြတ်ဆုံး ဆက်စပ်ပုံ၊"
V2 = f"{F.DUKA}နှင့် {F.TIKA}၊ {F.TIKA}နှင့် {F.DUKA}၊"
V3 = f"{F.TIKA}နှင့် {F.TIKA}၊ {F.DUKA}နှင့် {F.DUKA}၊"
V4 = "{order}၌ နည်း ခြောက်ပါးတို့သည် အလွန် နက်နဲကြ၏။"
W_NAYA = F.W("nayā", "နည်း")
for _ka in ("Ka", "Kha", "Ga", "Gha"):
    HLINES[f"({_ka}) tikañca paṭṭhānavaraṃ dukuttamaṃ,"] = f"({F.AKKHARA[_ka]}) {V1}"
HLINES["Dukaṃ tikañceva tikaṃ dukañca;"] = V2
HLINES["Tikaṃ tikañceva dukaṃ dukañca,"] = V3
for _p, _my in (("anulomamhi", "အဟုတ်ပြ ပုံစံ"), ("paccanīyamhi", "အငြင်းပြ ပုံစံ"),
                ("anulomapaccanīyamhi", "အဟုတ်ပြ အငြင်းပြ ပုံစံ"), ("paccanīyānulomamhi", "အငြင်းပြ အဟုတ်ပြ ပုံစံ")):
    HLINES[f"Cha {_p} nayā sugambhīrāti."] = V4.format(order=_my)

# ===================================================================================== unit templates (SK)
SK = {}
# the uddesa list «Hetupaccayo, ārammaṇapaccayo, … avigatapaccayoti.»
SK[", ".join(["§C§o"] * 23) + ", §C§oti."] = (C + " ").join("{C%d.n}" % i for i in range(1, 25)) + END
SK["§C§oti"] = "{C1.n} ဟူသည်"                        # «Hetupaccayoti –»
# the closing «ye ye … te te …» sentences
YAM = "အကြင်အကြင်"
TE = "ထိုထို"
CC = F.CITTACETASIKA
SK["yaṃ yaṃ dhammaṃ ārabbha ye ye dhammā uppajjanti cittacetasikā dhammā, te te dhammā tesaṃ tesaṃ dhammānaṃ "
   "§C§ena paccayo."] = (f"{YAM} {F.DHAMMA}ကို အာရုံပြု၍ {YAM} {CC} {F.DHAMMA}တို့ ဖြစ်ပေါ်ကြ၏{C} {TE} "
                          f"{F.DHAMMA}တို့သည် {TE} {F.DHAMMA}တို့အား {{C1.if}}{END}")
GARU = F.W("ariyaṃ dhammaṃ garuṃ katvā", "လေးစားဖွယ်ရာ ပြု၍", "5")
SK["yaṃ yaṃ dhammaṃ garuṃ katvā ye ye dhammā uppajjanti cittacetasikā dhammā, te te dhammā tesaṃ tesaṃ dhammānaṃ "
   "§C§ena paccayo."] = (f"{YAM} {F.DHAMMA}ကို {GARU} {YAM} {CC} {F.DHAMMA}တို့ ဖြစ်ပေါ်ကြ၏{C} {TE} "
                          f"{F.DHAMMA}တို့သည် {TE} {F.DHAMMA}တို့အား {{C1.if}}{END}")
ANANTARA = "ချက်ချင်း နောက်၌"                          # anantarā (adverb)
SAMANANTARA = "ကောင်းစွာ ချက်ချင်း နောက်၌"              # samanantarā (adverb; pi-5 has «ချက်ချင်း နောက်၌», logged)
for _adv, _my in (("anantarā", ANANTARA), ("samanantarā", SAMANANTARA)):
    SK[f"yesaṃ yesaṃ dhammānaṃ {_adv} ye ye dhammā uppajjanti cittacetasikā dhammā, te te dhammā tesaṃ tesaṃ "
       "dhammānaṃ §C§ena paccayo."] = (f"{YAM} {F.DHAMMA}တို့၏ {_my} {YAM} {CC} {F.DHAMMA}တို့ ဖြစ်ပေါ်ကြ၏{C} "
                                        f"{TE} {F.DHAMMA}တို့သည် {TE} {F.DHAMMA}တို့အား {{C1.if}}{END}")
# «Yaṃ rūpaṃ nissāya manodhātu ca manoviññāṇadhātu ca vattanti, taṃ rūpaṃ …»
YAM_RUPA = (f"အကြင် {F.NOUN['rūpānaṃ'][0]}ကို မှီ၍ {F.FIXED['manodhātu'][0]}{F.LAKAUNG}{C} "
            f"{F.FIXED['manoviññāṇadhātu'][0]}{F.LAKAUNG} ဖြစ်ပွားကြ၏{C} ")


def _yam_rupa(rest):
    def f(slots):
        sk, sl = F.slot(rest)
        sl["C"] = slots["C"]
        r = F.panha(sk, sl)
        if r is None:
            raise F.Miss("yaṃ rūpaṃ: " + rest)
        return YAM_RUPA + r
    return f


for _rest in ("taṃ rūpaṃ manodhātuyā ca manoviññāṇadhātuyā ca taṃsampayuttakānañca dhammānaṃ §C§ena paccayo.",
              "taṃ rūpaṃ manodhātuyā taṃsampayuttakānañca dhammānaṃ §C§ena paccayo."):
    SK["yaṃ rūpaṃ nissāya manodhātu ca manoviññāṇadhātu ca vattanti, " + _rest] = \
        _yam_rupa(_rest.replace("§C§ena", "hetupaccayena"))
SK["kabaḷīkāro §V§ āhāro imassa kāyassa §C§ena paccayo."] = \
    f"{F.W('kabaḷīkāro āhāro', 'လုတ်ပြု၍ စားရသော အာဟာရ', '1')[:-len(' အာဟာရ')]} {{V1}} အာဟာရသည် ဤကိုယ်အား {{C1.if}}{END}"
# the parenthetical instructions
SK["(yathā §C§o vitthārito, evaṃ §C§opi vitthāretabbo vācanāmaggena.)"] = \
    f"({{C1.obj}} {PH['vitthārito']} {{C2.pi}} {PH['evaṃ']} {PH['vācanāmaggena']} {PH['vitthāretabbo']}{END})"
SK["(yathā anulome §C§o vitthārito, evaṃ paccanīyepi §C§o vitthāretabbo.)"] = \
    f"({PH['anulome']} {{C1.obj}} {PH['vitthārito']} {PH['paccanīye']}လည်း {PH['evaṃ']} {{C2.obj}} {PH['vitthāretabbo']}{END})"
SK["(yathā anulome §C§o vitthārito, evaṃ anulomapaccanīyepi padaṃ vitthāretabbaṃ.)"] = \
    (f"({PH['anulome']} {{C1.obj}} {PH['vitthārito']} {PH['anulomapaccanīye']}လည်း {PH['evaṃ']} {F.PADA}ကို "
     f"{PH['vitthāretabbo']}{END})")
SK["(pañcamūlakādikā saṃkhittā."] = f"({mul('pañca')} {F.ADI}တို့ကို {PH['saṃkhittā']}{END}"
SK["ekamūlakaṃ, dumūlakaṃ, timūlakaṃ, catumūlakaṃ, pañcamūlakaṃ, sabbamūlakaṃ asammuyhantena vitthāretabbaṃ.)"] = \
    f"{MUL_LIST6}ကို {PH['asammuyhantena']} {PH['vitthāretabbo']}{END})"
SK["(ekekassa padassa ekamūlakaṃ, dumūlakaṃ, timūlakaṃ, catumūlakaṃ, pañcamūlakaṃ, sabbamūlakaṃ asammuyhantena "
   "vitthāretabbaṃ. )"] = f"({PH['ekekassa padassa']} {MUL_LIST6}ကို {PH['asammuyhantena']} {PH['vitthāretabbo']}{END} )"
SK["(yathā anulome ekekassa padassa ekamūlakaṃ, dumūlakaṃ, timūlakaṃ, catumūlakaṃ, yāva tevīsatimūlakaṃ evaṃ "
   "paccanīyepi vitthāretabbaṃ. )"] = \
    (f"({PH['anulome']} {PH['ekekassa padassa']} {MUL_LIST4}မှ အကြောင်း နှစ်ဆယ့်သုံးခုကို အခြေခံခြင်းအထိ "
     f"ရှိသည့်အတိုင်း {PH['paccanīye']}လည်း {PH['evaṃ']} {PH['vitthāretabbo']}{END} )")

# the counting instructions of 1-02
KT = F.W("kusalattike", "ကုသိုလ် သုံးမျိုးတွဲ", "2")              # kusalattika
GANANA = "ရေတွက်ချက်"                                               # gaṇanā (NEW)
ORDER = {"paccaya": F.PACCAYA, "paccanīya": "အငြင်းပြ ပုံစံ၏", "anulomapaccanīya": "အဟုတ်ပြ အငြင်းပြ ပုံစံ၏",
         "paccanīyānuloma": "အငြင်းပြ အဟုတ်ပြ ပုံစံ၏"}
GANITA = "ရေတွက်ထားသည့်အတိုင်း"                                     # gaṇitā (after yathā)
IDAMPI = "ဤသည်ကိုလည်း"
SK["(yathā kusalattikassa paccayagaṇanā, evaṃ vitthāretabbā)."] = \
    f"({KT}၏ {ORDER['paccaya']} {GANANA}အတိုင်း {PH['evaṃ']} {PH['vitthāretabbo']})" + END
SK["(yathā kusalattikaṃ, evaṃ gaṇetabbaṃ.)"] = f"({KT}ကဲ့သို့ {PH['evaṃ']} {PH['gaṇetabbaṃ']}{END})"
SK["(yathā kusalattikassa paccanīyagaṇanā gaṇitā, evaṃ idampi asammuyhantena sabbaṃ mūlakaṃ gaṇetabbaṃ §V§.)"] = \
    (f"({KT}၏ {ORDER['paccanīya']} {GANANA}ကို {GANITA} {IDAMPI} {PH['evaṃ']} {PH['asammuyhantena']} "
     f"အခြေခံ အားလုံးကို {PH['gaṇetabbaṃ']} {{V1}}{END})")
SK["(yathā kusalattikassa anulomapaccanīyagaṇanā sajjhāyamaggena gaṇitā, evaṃ idampi gaṇetabbaṃ.)"] = \
    (f"({KT}၏ {ORDER['anulomapaccanīya']} {GANANA}ကို {PH['sajjhāyamaggena']} {GANITA} {IDAMPI} {PH['evaṃ']} "
     f"{PH['gaṇetabbaṃ']}{END})")
SK["(yathā kusalattikassa paccanīyānulomagaṇanā sajjhāyamaggena gaṇitā, evaṃ gaṇetabbaṃ.)"] = \
    (f"({KT}၏ {ORDER['paccanīyānuloma']} {GANANA}ကို {PH['sajjhāyamaggena']} {GANITA} {PH['evaṃ']} "
     f"{PH['gaṇetabbaṃ']}{END})")

SKF = {}

# ===================================================================================== engine setup
F.HLINES.update(HLINES)
F.SK.update(SK)
F.SKF.update(SKF)
F.SPELLING.update({"kabaḷiṅkāro (ka. sī. syā.)", "nānākhaṇikā (ka.)"})


def chapter(name):
    txt = F.translate((PALI / name).read_text(encoding="utf-8-sig"))
    if not F.DEV:
        (OUT / name).write_text(txt, encoding="utf-8")
        print(f"wrote {name}: {sum(1 for l in txt.splitlines() if l)} lines")


if __name__ == "__main__":
    F.DEV = "--dev" in sys.argv
    names = [a for a in sys.argv[1:] if not a.startswith("--")] or NAMES
    for n in names:
        chapter(n)
    if F.DEV:
        for k, v in F.UNSEEN.items():
            print("SK:", k)
            print("   ", v)
        print(len(F.UNSEEN), "unmatched")
    if F.SLIPS:
        print("slips:", *sorted(F.SLIPS), sep="\n  ")
    if "--terms" in sys.argv:
        import write_terms
        write_terms.write(F, sys.modules[__name__])
