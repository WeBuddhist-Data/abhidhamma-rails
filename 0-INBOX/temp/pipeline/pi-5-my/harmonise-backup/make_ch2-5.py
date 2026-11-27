"""Burmese zero-shot of pi-5 (Kathāvatthu, «အငြင်းပွားရာ အကြောင်းအရာများကို ဆွေးနွေးခြင်း»), chapters 2-5:
2-parihanikatha, 3-brahmacariyakatha (Brahmacariyakathā + Odhisokathā), 4-jahatikatha, 5-sabbamatthitikatha.

usage: python3 -I -X utf8 make_ch2-5.py [chapter ...] [--misses]
Model: make_sample.py (the approved sample). Every line is generated from the Pāli by my5_formulas.translate_line()
through the frames, rules and tables of my5_formulas.py (imported, never edited; its tables are extended IN MEMORY
here) and the tables of this script: PROP_X (propositions), RULES (productive patterns, registered with F.rule),
FRAMES_X (sentence frames inserted before the two generic frames), QUOTE_X (sutta quotations), SENT_X (unique
sentences), LINES_X (whole lines: verses, multi-line quotations). A sentence no frame / rule / table entry matches
stops the run (my5_formulas.Miss): nothing is guessed. Each line is checked against its Pāli (dash, ellipsis, «[»,
item number, digits, no «?» «।» «:-»); a chapter is written only when every line passed.
NEW records every string added here (Pāli -> Burmese) for notes-ch2-5.md.
"""
import pathlib
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import my5_formulas as F  # noqa: E402
from my5_formulas import V, FR, Cl, C, END, PE, PUGGALA  # noqa: E402

ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-5_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-5-burmese-plain-zeroshot_split_chapters"
NAMES_OUT = ["2-parihanikatha.md", "3-brahmacariyakatha.md", "4-jahatikatha.md", "5-sabbamatthitikatha.md"]


def W(book, bid, pali, my):
    """F.witness(); when the given segment does not hold the pair, the first FINAL segment (pi-1 … pi-4) whose Pāli
    has «pali» and whose Burmese has «my» is the witness (recorded in F.WITNESS); none = Miss."""
    try:
        return F.witness(book, bid, pali, my)
    except (F.Miss, KeyError):
        pass
    for b in "1234":
        for k, (f, pl, ml) in F.FINAL.SEG[b].items():
            if pali.lower() in " ".join(pl).lower() and my in " ".join(ml):
                F.WITNESS.setdefault(pali, (b, k, my))
                return my
    raise F.Miss(f"no witness for «{pali}» / «{my}»")


PUG = PUGGALA
PROP_X, QUOTE_X, SENT_X, LINES_X, ANCHOR_X = {}, {}, {}, {}, {}
NEW = {}         # Pāli term / phrase -> Burmese (new strings of this script, for the notes)


def new(pali, my):
    NEW.setdefault(pali, my)
    return my


# ===================================================================================== clause classes of this script
class Wh(Cl):
    """A question-word clause (kiṃ / kattha / kuhiṃ / katamena …): every form ends «…သနည်း» (the clause is a
    question wherever it stands, also as a non-final part of a compound question)."""

    def f(self, form, depth=0):
        out = (self.pre + " " if self.pre else "") + self.v + "သနည်း" + self.post
        return F.q_set(out, depth)


class Nq(Cl):
    """A verbless phrase (an elliptical question / answer, «Sotāpattimaggenāti?»): question «…လော», statement
    «… ဖြစ်သည်»."""

    def f(self, form, depth=0):
        out = {"q": self.pre + "လော", "stmt": self.pre + " ဖြစ်သည်", "bare": self.pre, "cond": self.pre + " ဖြစ်လျှင်",
               "nanu": self.pre + " ဖြစ်သည် မဟုတ်လော", "rel": self.pre + " ဖြစ်သော"}[form]
        return F.q_set(out, depth)


def VV(pre, verb, neg=False, post=""):
    """V() for a verb stem without a standard negative: negative = «မ» + stem."""
    return Cl(pre, verb, "မ" + verb, neg, post)


MY_FRAMES = []


def frame(rx):
    def deco(fn):
        MY_FRAMES.append((re.compile(rx), fn))
        return fn
    return deco


# ===================================================================================== shared vocabulary (reused)
SOTAPANNA, SAKADAGAMI, ANAGAMI, ARAHA = F.SOTAPANNA, F.SAKADAGAMI, F.ANAGAMI, F.ARAHA
PUTHUJJANA = W("1", "^1-1223", "puthujjano", "ပုထုဇဉ်")
SAMAYAVIM = W("4", "^4-M-7", "Samayavimutto", "အချိန်အလိုက် လွတ်မြောက်သူ")
ASAMAYAVIM = W("4", "^4-M-7", "Asamayavimutto", "အချိန်အလိုက် မဟုတ်ဘဲ လွတ်မြောက်သူ")
SV_ADJ = "အချိန်အလိုက် လွတ်မြောက်သော"                  # samayavimutto (attributive of pi-4 «… လွတ်မြောက်သူ»)
ASV_ADJ = "အချိန်အလိုက် မဟုတ်ဘဲ လွတ်မြောက်သော"
ARAHATTA = W("2", "^2-807", "arahattaphale", "ရဟန္တာ")      # arahatta (compound member, pi-1 / pi-2)
ARAHATTA_N = new("arahatta (arahantship)", f"{ARAHATTA} အဖြစ်")
PHALA = W("2", "^2-807", "sotāpattiphale paññā", "သောတာပတ္တိဖိုလ်")
FRUIT = {"sotāpatti": PHALA, "sakadāgāmi": W("2", "^2-807", "sakadāgāmiphale", "သကဒါဂါမိဖိုလ်"),
         "anāgāmi": W("2", "^2-807", "anāgāmiphale", "အနာဂါမိဖိုလ်"), "arahatta": ARAHATTA_N}
MAGGA = W("2", "^2-807", "catūsu maggesu", "မဂ်")
MAGGA_OF = {"sotāpatti": W("2", "^2-807", "Sotāpattimagge", "သောတာပတ္တိမဂ်"),
            "sakadāgāmi": W("2", "^2-807", "sakadāgāmimagge", "သကဒါဂါမိမဂ်"),
            "anāgāmi": W("2", "^2-807", "anāgāmimagge", "အနာဂါမိမဂ်")}
KILESA = W("1", "^1-1173", "kilesā", "ကိလေသာ")
PAHINA = "ပယ်ပြီး"                                          # pahīna (pi-1 / pi-4 «ပယ်ပြီးသော»)
BHAVITA = "ပွားများပြီး"                                     # bhāvita (pi-4 «ပွားများအပ်ပြီးသော»)
SACCHI = W("4", "^4-17", "sotāpattiphalaṃ sacchikaroti", "မျက်မှောက်")   # sacchikaroti «မျက်မှောက်ပြု»
SACCHIKAROTI = "မျက်မှောက်ပြု"
PARINIBB = W("4", "^4-M-7", "Antarāparinibbāyī", "ပရိနိဗ္ဗာန် ပြု")
UPAPAJJ = "ပြန်လည် ဖြစ်ပေါ်"                                 # upapajjati (sample, pi-2 «… ငရဲ၌ ပြန်လည် ဖြစ်ပေါ်»)
W("2", "^2-U58", "nirayaṃ upapajjati", UPAPAJJ)
SAKKAYA = W("1", "^1-1006", "sakkāyadiṭṭhi", "ကိုယ်ကို အတ္တဟု ယူဆသော အယူ")
VICIKICCHA = W("1", "^1-1006", "vicikicchā", "ယုံမှားမှု")
SILABBATA = W("1", "^1-1006", "sīlabbataparāmāso", "သီလ အကျင့်ဝတ်ဆိုင်ရာ မှားယွင်းသော ယူဆမှု")
RAGA = W("2", "^2-U70", "Kāmarāgapariyuṭṭhānaṃ", "ရာဂ")
KAMARAGA = W("2", "^2-U70", "Kāmarāgapariyuṭṭhānaṃ", "ကာမရာဂ")
BYAPADA = W("1", "^1-1158", "byāpādanīvaraṇaṃ", "ဖျက်ဆီးလိုစိတ်")
DOSA = W("1", "^1-986", "lobho, doso, moho", "ဒေါသ")
MOHA = W("1", "^1-986", "lobho, doso, moho", "မောဟ")
MANA = "မာန"
W("2", "^2-U49", "māno", MANA)
UDDHACCA = W("2", "^2-U49", "uddhaccaṃ", "ယောက်ယက်ခတ်မှု")
AVIJJA = W("2", "^2-U49", "avijjā", "အမှန်ကို မသိမှု")
RUPARAGA = W("2", "^2-U49", "Rūparāgo", "သိမ်မွေ့သော ရုပ်ဘဝကို တပ်မက်သော ရာဂ")
ARUPARAGA = W("2", "^2-U49", "arūparāgo", "ရုပ်မရှိသော ဘဝကို တပ်မက်သော ရာဂ")
DITTHI = W("2", "^2-816", "diṭṭhānusayo", "အယူ")
THINA = W("1", "^1-1161", "Atthi thinaṃ", "ထိုင်းမှိုင်းမှု")
AHIRIKA = W("1", "^1-365", "ahirikaṃ hoti", "ဒုစရိုက်ကို မရှက်မှု")
ANOTTAPPA = W("1", "^1-365", "anottappaṃ hoti", "ဒုစရိုက်ကို မကြောက်ရွံ့မှု")
OLARIKA = W("1", "^1-U1", "rūpaṃ oḷārikaṃ", "ရုန့်ရင်းသော")
APAYA = W("2", "^2-U58", "apāyaṃ duggatiṃ", "အပါယ်")
APAYAGAM = new("apāyagamanīya", f"{APAYA}သို့ ရောက်စေတတ်သော")
ANUSAHA = new("aṇusahagata", "အနည်းငယ်မျှ ကျန်ရှိသော")
SATIP = W("2", "^2-U26", "Cattāro satipaṭṭhānā", "သတိပဋ္ဌာန်")
SAMMAPP = W("2", "^2-U26", "cattāro sammappadhānā", "မှန်ကန်သော ကြိုးပမ်းအားထုတ်ခြင်း")
IDDHIP = W("2", "^2-U26", "cattāro iddhipādā", "ဣဒ္ဓိပါဒ်")
INDRIYA_W = F.INDRIYA_W
BALA = W("2", "^2-U26", "pañca balāni", "စွမ်းအား")
BOJJH = W("2", "^2-U26", "satta bojjhaṅgā", "ဗောဇ္ဈင်")
DUKKHA = W("2", "^2-189", "dukkhaṃ ariyasaccaṃ", "ဒုက္ခ")
SAMUDAYA = W("2", "^2-189", "dukkhasamudayaṃ", "ဒုက္ခ ဖြစ်ပေါ်ခြင်း")    # samudaya (truth; pi-2 dukkhasamudaya)
NIRODHA = W("2", "^2-189", "dukkhanirodhaṃ", "ဒုက္ခ ချုပ်ငြိမ်းခြင်း")
SACCA4 = W("2", "^2-978", "cattāri saccāni", "သစ္စာ လေးပါး")
ANUSAYA = W("2", "^2-816", "anusayo", "ကိန်းအောင်းခြင်း")
PARIYUTTHANA = W("2", "^2-U70", "pariyuṭṭhānāni", "ထကြွခြင်း")
ORAMBH = W("2", "^2-836", "Pañcorambhāgiyāni saṃyojanāni", "အောက်ပိုင်း ဘုံနှင့် ဆိုင်သော နှောင်ကြိုး ငါးပါး")
UDDHAMBH = W("2", "^2-836", "pañcuddhambhāgiyāni saṃyojanāni", "အထက်ပိုင်း ဘုံနှင့် ဆိုင်သော နှောင်ကြိုး ငါးပါး")
SAMYOJANA = "နှောင်ကြိုး"
BRAHMA = W("2", "^2-509", "imasmiṃ brahmacariye", "မြင့်မြတ်သော အကျင့်")   # brahmacariya (pi-2)
BV = new("brahmacariyavāsa", f"{BRAHMA}ကို ကျင့်သုံးခြင်း")
DEVA, MANUSSA = F.DEVA, F.MANUSSA
ASANNA = W("2", "^2-1015", "asaññasattānaṃ devānaṃ", "အသညသတ်")              # asaññasatta (pi-2)
SAMMASAMB = W("1", "^T-1", "sammāsambuddhassa", "အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရားရှင်")
PACCEKA = W("4", "^4-M-7", "Paccekasambuddho", "ပစ္စေကဗုဒ္ဓါ")
BHAGAVA = F.BHAGAVA
SANGHA = F.SANGHA
PANATIPATA = F.PANATIPATA
MICCHADITTHI = W("2", "^2-U30", "Micchādiṭṭhi", "မှားယွင်းသော အယူ")
SAMMADITTHI = F.SAMMADITTHI
ABHISAMAYA = "ထင်ထင်ရှားရှား သိမြင်ခြင်း"                        # abhisamaya (pi-2 termbase)
AKUPPA = "မပျက်ယွင်းတတ်သော"                                   # akuppa (pi-4 termbase, akuppadhammo)
PATIVEDHA = "ထိုးထွင်း သိမြင်ခြင်း"                            # paṭivedha (sample Paṭivedhānuyogo)
KAYENA = W("4", "^4-1", "kāyena phusitvā", "ကိုယ်ဖြင့် ထိ၍")
JAHATI = new("jahati", "စွန့်ပယ်")
SANTHATI = new("saṇṭhāti", "တည်")
PARIH = new("parihāyati", "ဆုတ်ယုတ်")
W("4", "^4-7", "parihāyati tāhi samāpattīhi", PARIH)
EVAM = W("4", "^4-94", "Evamevaṃ", "ထို့အတူပင်")
ANUPASSI = W("2", "^2-487", "citte cittānupassī", "အဖန်ဖန် ရှု")

# ===================================================================================== headings and colophons
SECTION_X = {
    "Parihānikathā": f"{PARIH}ခြင်းအကြောင်း {F.KATHA_W}",
    "Vādayuttiparihāni": f"{PARIH}ခြင်း၌ ဝါဒ၏ ယုတ္တိ",
    "Ariyapuggalasaṃsandanaparihāni": f"{PARIH}ခြင်း၌ အရိယာ {PUG}တို့ကို နှိုင်းယှဉ်ခြင်း",
    "Ariyapuggalasaṃsandanaṃ": f"အရိယာ {PUG}တို့ကို နှိုင်းယှဉ်ခြင်း",
    "Suttasādhanaparihāni": f"{PARIH}ခြင်း၌ {F.SUTTANTA}ဖြင့် သက်သေပြခြင်း",
    "Brahmacariyakathā": f"{BRAHMA}အကြောင်း {F.KATHA_W}",
    "Suddhabrahmacariyakathā": f"ရိုးရိုး {BRAHMA}အကြောင်း {F.KATHA_W}",
    "Saṃsandanabrahmacariyakathā": f"နှိုင်းယှဉ်ခြင်းဖြင့် {BRAHMA}အကြောင်း {F.KATHA_W}",
    "Odhisokathā": f"အပိုင်းအပိုင်း {JAHATI}ခြင်းအကြောင်း {F.KATHA_W}",
    "Jahatikathā": f"{JAHATI}ခြင်းအကြောင်း {F.KATHA_W}",
    "Nasuttāharaṇakathā": f"{F.SUTTANTA}ကို မကိုးကားသော {F.KATHA_W}",
    "Suttāharaṇakathā": f"{F.SUTTANTA}ကို ကိုးကားသော {F.KATHA_W}",
    "Sabbamatthītikathā": f"အရာအားလုံး ရှိသည် ဟူသော {F.KATHA_W}",
    "Vādayutti": "ဝါဒ၏ ယုတ္တိ",
    "Kālasaṃsandanā": "အချိန်ကို နှိုင်းယှဉ်ခြင်း",
    "Vacanasodhanā": F.SECTION["Vacanasodhanaṃ"],
    "Atītacakkhurūpādikathā": f"အတိတ် မျက်စိ၊ ရုပ် စသည်အကြောင်း {F.KATHA_W}",
    "Atītañāṇādikathā": f"အတိတ် ဉာဏ် စသည်အကြောင်း {F.KATHA_W}",
    "Arahantādikathā": f"{ARAHA} စသည်အကြောင်း {F.KATHA_W}",
    "Atītahatthādikathā": f"အတိတ် လက် စသည်အကြောင်း {F.KATHA_W}",
    "Atītakkhandhādisamodhānakathā": f"အတိတ် {F.KHANDHA_W} စသည်တို့ကို ပေါင်းစုခြင်းအကြောင်း {F.KATHA_W}",
    "Padasodhanakathā": f"ပုဒ်ကို စိစစ်ခြင်းအကြောင်း {F.KATHA_W}",
    "Suttasādhanaṃ": f"{F.SUTTANTA}ဖြင့် သက်သေပြခြင်း",
}
for _k, _v in SECTION_X.items():
    new(_k, _v)
F.SECTION.update(SECTION_X)
F.HEAD.update(SECTION_X)
F.COLO.update({f"{k} niṭṭhitā": F.DONE.format(v) for k, v in SECTION_X.items()})
F.COLO.update(SECTION_X)
SENT_X["Vādayutti."] = SECTION_X["Vādayutti"] + END
SENT_X["(Saṃkhittaṃ)."] = F.SANKHITTA + END
SENT_X["Nanu vuttaṃ bhagavatā –"] = f"{BHAGAVA} ဤသို့ ဟောတော်မူသည် မဟုတ်လော –"

# ===================================================================================== brackets of chapters 2-5
F.VAR_KIND.update({
    "thīnaṃ": F.LEKHANA, "anabhāvakato": F.LEKHANA, "na parihāyatīti": F.PATHA, "mahāmoggalāno": F.LEKHANA,
    "mahākoṭṭhito": F.LEKHANA, "eḷamūgā": F.LEKHANA, "milakkhūsu": F.LEKHANA, "asaññasattesu": F.PATHA,
    "sacchikaroti": F.LEKHANA, "idhaparinibbāyī": F.PATHA, "sotāpattiphalaṃ patto": F.PATHA,
    "sakadāgāmiphalaṃ patto": F.PATHA, "anāgāmiphalaṃ patto": F.PATHA, "arahattaṃ patto": F.PATHA,
    "abhabbo": F.LEKHANA, "ahiṃsakā": F.PATHA, "karuṇādhimuttā": F.LEKHANA, "na jahati": F.LEKHANA,
})
F.REF_NOTE.update({"suttanipāte": f"{F.REF['su. ni.']}၌"})
AN_IN = "“အင်္ဂုတ္တရနိကာယ်”၌"
SN_IN = "“သံယုတ္တနိကာယ်”၌"
F.BR_TABLE.update({
    "[(āmantā) (ka.)]": f"[({F.YES}) (Ka.)]",
    "[no vata re (syā. pī.) evamuparipi]": f"[{F.PATHA} (Syā., Pī.): no vata re{C} အထက်၌လည်း ဤနည်းတူ]",
    "[mahākaccāno (ma. ni. 1.202 ādayo)]": f"[{F.LEKHANA} ({F.REF['ma. ni.']} 1.202 စသည်): mahākaccāno]",
    "[paṭipādā (aṭṭha.)]": f"[{F.LEKHANA} (အဋ္ဌကထာ): paṭipādā]",
    "[mahāva. 244; a. ni. 6.55]": f"[“မဟာဝဂ်” 244{C} {F.REF['a. ni.']} 6.55]",
    "[khu. pā. 6.10; su. ni. 233]": f"[“ခုဒ္ဒကပါဌ” 6.10{C} {F.REF['su. ni.']} 233]",
    "[aṅguttaranikāye]": f"[{AN_IN}]",
    "[saṃyuttanikāye]": f"[{SN_IN}]",
    "[( ) (?)]": "[( ) (မသေချာ)]",
    "[na jahatīti (bahūsu) aṭṭhakathā oloketabbā]": f"[{F.PATHA} (အများစု၌): na jahatīti{C} အဋ္ဌကထာကို ကြည့်ပါ]",
    "[na jahatīti (bahūsu) anulomapañhoyeva]": f"[{F.PATHA} (အများစု၌): na jahatīti{C} အစဉ်အတိုင်း အမေးသာ ဖြစ်သည်]",
    "[na jahatīti (?) purimapañhehi saṃsandetabbaṃ]":
        f"[{F.PATHA} (မသေချာ): na jahatīti{C} ရှေ့ အမေးတို့နှင့် နှိုင်းယှဉ်ရမည်]",
    "[na jahatīti (?) purimañhehi saṃsandetabbaṃ]":
        f"[{F.PATHA} (မသေချာ): na jahatīti{C} ရှေ့ အမေးတို့နှင့် နှိုင်းယှဉ်ရမည်]",
    "[sadaraṃ (saṃ. ni. 2.64) tadeva yuttataraṃ]":
        f"[{F.PATHA} ({F.REF['saṃ. ni.']} 2.64): sadaraṃ{C} ထိုပါဌ်ကပင် ပို၍ သင့်လျော်သည်]",
})
for _k, _v in F.BR_TABLE.items():
    new(_k, _v)

# ===================================================================================== persons (case forms)
PERS = {         # nominative -> Burmese
    "arahā": ARAHA, "sotāpanno": SOTAPANNA, "sakadāgāmī": SAKADAGAMI, "anāgāmī": ANAGAMI,
    "puthujjano": PUTHUJJANA, "samayavimutto arahā": f"{SV_ADJ} {ARAHA}",
    "asamayavimutto arahā": f"{ASV_ADJ} {ARAHA}",
    "anāgāmī puggalo": f"{ANAGAMI} {PUG}", "sotāpanno puggalo": f"{SOTAPANNA} {PUG}",
    "sakadāgāmī puggalo": f"{SAKADAGAMI} {PUG}",
}
THERA = {"sāriputto": "သာရိပုတ္တရာ", "mahāmoggallāno": "မဟာမောဂ္ဂလ္လာန်", "mahākassapo": "မဟာကဿပ",
         "mahākaccāyano": "မဟာကစ္စာယန", "mahākoṭṭhiko": "မဟာကောဋ္ဌိက", "mahāpanthako": "မဟာပန္ထက"}
THERA_W = "မထေရ်"
for _p, _m in THERA.items():
    PERS[f"{_p} thero"] = new(f"{_p} thero", f"{_m} {THERA_W}")
    PROP_X[f"{_p} thero"] = FR(PERS[f"{_p} thero"])
    ANCHOR_X[_p.capitalize()] = _m
    ANCHOR_X[_p] = _m
GEN = {"arahato": ARAHA, "sotāpannassa": SOTAPANNA, "sakadāgāmissa": SAKADAGAMI, "anāgāmissa": ANAGAMI,
       "puthujjanassa": PUTHUJJANA, "samayavimuttassa arahato": f"{SV_ADJ} {ARAHA}",
       "asamayavimuttassa arahato": f"{ASV_ADJ} {ARAHA}", "anāgāmissa puggalassa": f"{ANAGAMI} {PUG}"}
INS = {"arahatā": ARAHA, "sotāpannena": SOTAPANNA, "sakadāgāminā": SAKADAGAMI, "anāgāminā": ANAGAMI}
ABL = {"arahattā": ARAHATTA_N + "မှ", "sotāpattiphalā": FRUIT["sotāpatti"] + "မှ",
       "sakadāgāmiphalā": FRUIT["sakadāgāmi"] + "မှ", "anāgāmiphalā": FRUIT["anāgāmi"] + "မှ"}
LOC = {"arahatte": ARAHATTA_N + "၌", "anāgāmiphale": FRUIT["anāgāmi"] + "၌", "sakadāgāmiphale": FRUIT["sakadāgāmi"] + "၌",
       "sotāpattiphale": FRUIT["sotāpatti"] + "၌", "puthujjanabhūmiyaṃ": new("puthujjanabhūmi", f"{PUTHUJJANA} အဆင့်၌")}


def alt(d):
    return "|".join(re.escape(k) for k in sorted(d, key=len, reverse=True))


def altc(d):
    """alt() with the capitalised variants (a sentence-initial key in a frame)."""
    ks = set(d) | {k[:1].upper() + k[1:] for k in d}
    return "|".join(re.escape(k) for k in sorted(ks, key=len, reverse=True))


def low(x):
    return x[:1].lower() + x[1:]


# ---- parihāyati
@F.rule(r"(?P<w>sabbattha |sabbadā )?(?P<n1>na )?(?P<v1>parihāyati |parihāyittha )?(?P<s>" + alt(PERS) + r")"
        r"(?P<n3> na)?(?P<v3> parihāyittha)? (?P<f>" + alt(ABL) + r")(?P<n2> na)?(?P<v2> parihāyati| parihāyittha)?")
def _r_parih(m):
    """(sabbattha / sabbadā) (na) parihāyati S F / S F (na) parihāyati / S (na) parihāyittha F (past)."""
    vs = [x for x in (m["v1"], m["v2"], m["v3"]) if x]
    if len(vs) != 1:
        return None
    v = vs[0]
    neg = bool(m["n1"] or m["n2"] or m["n3"])
    verb = PARIH + ("ခဲ့" if "ittha" in v else "")
    pre = (F.WHERE[m["w"].strip()] + " " if m["w"] else "") + f"{PERS[m['s']]}သည် {ABL[m['f']]}"
    return V(pre, verb, neg)


PROP_X["sabbattha arahato parihāni"] = V(f"{F.WHERE['sabbattha']} {ARAHA}၏ {PARIH}ခြင်း", "ရှိ")
PROP_X["sabbadā arahato parihāni"] = V(f"{F.WHERE['sabbadā']} {ARAHA}၏ {PARIH}ခြင်း", "ရှိ")
PROP_X["sabbeva arahanto arahattā parihāyanti"] = V(f"{ARAHA} အားလုံးပင် {ABL['arahattā']}", PARIH + "ကြ")
PROP_X["sabbesaṃyeva arahantānaṃ parihāni"] = V(f"{ARAHA} အားလုံးတို့၏ပင် {PARIH}ခြင်း", "ရှိ")
PARIHAYAMANO = {s: f"{ABL[f]} {PARIH}နေသော {PERS[s]}" for s, f in
                (("arahā", "arahattā"), ("anāgāmī", "anāgāmiphalā"), ("sakadāgāmī", "sakadāgāmiphalā"),
                 ("sotāpanno", "sotāpattiphalā"))}
PROP_X["arahā arahattā parihāyamāno catūhi phalehi parihāyati"] = V(
    f"{PARIHAYAMANO['arahā']}သည် ဖိုလ် လေးပါးလုံးမှ", PARIH)
PROP_X["arahā arahattā parihāyamāno bhabbo catūhi phalehi parihāyituṃ"] = V(
    f"{PARIHAYAMANO['arahā']}သည် ဖိုလ် လေးပါးလုံးမှ {PARIH}နိုင်သူ")
_SETTHI = new("catūhi satasahassehi seṭṭhī seṭṭhittaṃ kārento satasahasse parihīne",
              f"ငွေ လေးသိန်းဖြင့် သူဌေး အဖြစ်ကို ပြုနေသော သူဌေးသည် ငွေ တစ်သိန်း {PARIH}သွားသောအခါ")
PROP_X["catūhi satasahassehi seṭṭhī seṭṭhittaṃ kārento satasahasse parihīne seṭṭhittā parihīno hoti"] = V(
    f"{_SETTHI} သူဌေး အဖြစ်မှ {PARIH}သူ")
PROP_X["sabbasāpateyyā parihīno hoti"] = V(f"ဥစ္စာ အားလုံးမှ {PARIH}သူ")
PROP_X["catūhi satasahassehi seṭṭhī seṭṭhittaṃ kārento satasahasse parihīne bhabbo sabbasāpateyyā parihāyituṃ"] = V(
    f"{_SETTHI} ဥစ္စာ အားလုံးမှ {PARIH}နိုင်သူ")


@F.rule(r"(?P<s>" + alt(PERS) + r") (?P<f>" + alt(ABL) + r") parihāyamāno (?P<l>" + alt(LOC) + r") saṇṭhāti")
def _r_santhati(m):
    return V(f"{ABL[m['f']]} {PARIH}နေသော {PERS[m['s']]}သည် {LOC[m['l']]}", SANTHATI)


@frame(r"(?P<s>" + altc(PERS) + r") (?P<f>" + alt(ABL) + r") parihāyamāno kattha saṇṭhātīti\?")
def _f_kattha(m):
    return f"{ABL[m['f']]} {PARIH}နေသော {PERS[low(m['s'])]}သည် အဘယ်၌ {SANTHATI}သနည်း{END}"


@frame(r"Hañci (?P<p>.+?)[,;] tena vata re vattabbe – (?P<q>.+?)ti…\.?")
def _f_if_pe(m):
    """Hañci P, tena vata re vattabbe – "Q"ti…pe…. (^5-246: the line ends in an ellipsis)."""
    return F.if_my(m["p"], m["q"]) + PE


for _k in ("Anāgāmiphaleti.", "Sakadāgāmiphaleti.", "Sotāpattiphaleti."):
    SENT_X[_k] = f"{LOC[_k[0].lower() + _k[1:-3]]} {SANTHATI}သည်{END}"
PROP_X["sotāpattiphalassa anantarā arahattaṃyeva sacchikaroti"] = V(
    f"{FRUIT['sotāpatti']}၏ နောက်တွင် ချက်ချင်း {ARAHATTA_N}ကိုပင်", SACCHIKAROTI)

# ---- kassa bahutarā kilesā pahīnā / kassa adhimattā …bhāvanā
BHAV = {"magga": MAGGA, "satipaṭṭhāna": SATIP, "sammappadhāna": SAMMAPP, "iddhipāda": IDDHIP,
        "indriya": INDRIYA_W, "bala": BALA, "bojjhaṅga": BOJJH}
BHAVANA = {k + "bhāvanā": f"{v}ကို ပွားများခြင်း" for k, v in BHAV.items()}
NEW["…bhāvanā (development of …)"] = "…ကို ပွားများခြင်း"


@frame(r"kassa (?:(?P<k>bahutarā kilesā pahīnā)|adhimattā (?P<l>.+?)) (?P<a>\S+) vā (?P<b>\S+) vāti\?")
def _f_kassa(m):
    a, b = GEN[m["a"]], GEN[m["b"]]
    head = f"{a}နှင့် {b}တို့အနက်"
    if m["k"]:
        return f"{head} အဘယ်သူသည် {KILESA}တို့ကို ပိုများစွာ {PAHINA} ဖြစ်သနည်း{END}"
    items = [BHAVANA[x.strip()] for x in m["l"].split("… ")]
    return f"{head} အဘယ်သူ၏ {'… '.join(items)}သည် ပို၍ လွန်ကဲသနည်း{END}"


for _g in ("arahato", "anāgāmissa", "sakadāgāmissa"):
    SENT_X[_g[0].upper() + _g[1:] + "."] = f"{GEN[_g]} ဖြစ်သည်{END}"


@F.rule(r"(?P<g>" + alt(GEN) + r") (?:bahutarā kilesā pahīnā|adhimattā (?P<b>\S+bhāvanā))")
def _r_bahutara(m):
    if m["b"]:
        return VV(f"{GEN[m['g']]}၏ {BHAVANA[m['b']]}သည် ပို၍", "လွန်ကဲ")
    return V(f"{GEN[m['g']]}သည် {KILESA}တို့ကို ပိုများစွာ {PAHINA}")


# ---- (arahatā) dukkhaṃ diṭṭhaṃ … cattāri saccāni diṭṭhāni
SEEN = {"dukkhaṃ diṭṭhaṃ": DUKKHA, "samudayo diṭṭho": SAMUDAYA, "nirodho diṭṭho": NIRODHA, "maggo diṭṭho": MAGGA,
        "cattāri saccāni diṭṭhāni": SACCA4}


@F.rule(r"(?:(?P<w>" + alt(INS) + r") )?(?P<x>" + alt(SEEN) + r")")
def _r_seen(m):
    who = f"{INS[m['w']]}သည် " if m["w"] else ""
    return V(f"{who}{SEEN[m['x']]}ကို မြင်ပြီး")


# ---- (arahato) rāgo pahīno … ; the uprooted defilement
KIL = {"rāgo": RAGA, "doso": DOSA, "moho": MOHA, "māno": MANA, "diṭṭhi": DITTHI, "vicikicchā": VICIKICCHA,
       "thinaṃ": THINA, "uddhaccaṃ": UDDHACCA, "ahirikaṃ": AHIRIKA, "anottappaṃ": ANOTTAPPA,
       "sakkāyadiṭṭhi": SAKKAYA, "sīlabbataparāmāso": SILABBATA,
       "apāyagamanīyo rāgo": f"{APAYAGAM} {RAGA}", "apāyagamanīyo doso": f"{APAYAGAM} {DOSA}",
       "apāyagamanīyo moho": f"{APAYAGAM} {MOHA}", "oḷāriko kāmarāgo": f"{OLARIKA} {KAMARAGA}",
       "oḷāriko byāpādo": f"{OLARIKA} {BYAPADA}", "aṇusahagato kāmarāgo": f"{ANUSAHA} {KAMARAGA}",
       "aṇusahagato byāpādo": f"{ANUSAHA} {BYAPADA}"}
UPROOT = new("ucchinnamūla tālāvatthukata anabhāvaṅkata āyatiṃ anuppādadhamma",
             "အမြစ်ပြတ်စေပြီး၊ ငုတ်တို ထန်းပင်ကဲ့သို့ ပြုပြီး၊ မရှိတော့အောင် ပြုပြီး၊ နောင်အခါ မဖြစ်ပေါ်တော့သော "
             "သဘော ရှိစေပြီး")
ANCHOR_X["anabhāvaṅkato"] = "မရှိတော့အောင် ပြုပြီး"
ANCHOR_X["thinaṃ"] = THINA


@F.rule(r"(?:(?P<w>" + alt(GEN) + r") )?(?P<k>" + alt(KIL) + r") (?:pahīno|pahīnā|pahīnaṃ)"
        r"(?P<u> ucchinnamūl(?:o|aṃ) tālāvatthukat(?:o|aṃ) anabhāvaṅkat(?:o|aṃ) āyatiṃ anuppādadhamm(?:o|aṃ))?")
def _r_pahina(m):
    who = f"{GEN[m['w']]}သည် " if m["w"] else ""
    if m["u"]:
        return V(f"{who}{KIL[m['k']]}ကို {PAHINA}၊ {UPROOT}")
    return V(f"{who}{KIL[m['k']]}ကို {PAHINA}")


# ---- (arahato) rāgappahānāya maggo bhāvito …
KIL_STEM = {"rāga": RAGA, "dosa": DOSA, "moha": MOHA, "anottappa": ANOTTAPPA}
DEV = {"maggo bhāvito": MAGGA, "satipaṭṭhānā bhāvitā": SATIP + "တို့", "sammappadhānā bhāvitā": SAMMAPP + "တို့",
       "iddhipādā bhāvitā": IDDHIP + "တို့", "indriyā bhāvitā": INDRIYA_W + "တို့", "balā bhāvitā": BALA + "တို့",
       "bojjhaṅgā bhāvitā": BOJJH + "တို့"}


@F.rule(r"(?:(?P<w>" + alt(GEN) + r") )?(?:(?P<k>rāga|dosa|moha|anottappa)p?pahānāya)?(?: ?(?P<d>" + alt(DEV) + r"))?")
def _r_dev(m):
    if not (m["k"] or m["d"]):
        return None
    pre = (f"{GEN[m['w']]}သည် " if m["w"] else "") + (f"{KIL_STEM[m['k']]}ကို ပယ်ရန်" if m["k"] else "")
    if not m["d"]:
        return FR(pre)
    return V(f"{pre} {DEV[m['d']]}ကို {BHAVITA}".strip())


# ---- the arahant's epithets and the accomplished tasks
EPI_PI = ("vītarāgo vītadoso vītamoho katakaraṇīyo ohitabhāro anuppattasadattho parikkhīṇabhavasaṃyojano "
          "sammadaññāvimutto ukkhittapaligho saṅkiṇṇaparikho abbūḷhesiko niraggaḷo ariyo pannaddhajo pannabhāro "
          "visaññutto suvijitavijayo")
VITA3 = f"{RAGA} ကင်းသူ၊ {DOSA} ကင်းသူ၊ {MOHA} ကင်းသူ"
W("2", "^2-798", "kāmesu vītarāgo", f"{RAGA} ကင်း")
EPI_MY = new(EPI_PI, f"{VITA3}၊ ပြုဖွယ် ကိစ္စကို ပြုပြီးသူ၊ ဝန်ကို ချပြီးသူ၊ မိမိ၏ အကျိုးစီးပွားသို့ ရောက်ပြီးသူ၊ "
                     f"ဘဝ {SAMYOJANA} ကုန်ခန်းပြီးသူ၊ ကောင်းစွာ သိ၍ လွတ်မြောက်ပြီးသူ၊ တံခါးကျင်ကို ဖယ်ရှားပြီးသူ၊ "
                     f"ကျုံးကို ဖို့ပြီးသူ၊ တိုင်ကို နုတ်ပစ်ပြီးသူ၊ တံခါးမင်းတုံး မရှိသူ၊ အရိယာ၊ အလံကို ချပြီးသူ၊ "
                     f"ဝန်ကို လွှတ်ချပြီးသူ၊ {SAMYOJANA}မှ ကင်းလွတ်ပြီးသူ၊ အောင်ပွဲကို ကောင်းစွာ အောင်ပြီးသူ")
TR_PI = ("dukkhaṃ tassa pariññātaṃ, samudayo pahīno, nirodho sacchikato, maggo bhāvito, abhiññeyyaṃ abhiññātaṃ, "
         "pariññeyyaṃ pariññātaṃ, pahātabbaṃ pahīnaṃ, bhāvetabbaṃ bhāvitaṃ, sacchikātabbaṃ sacchikataṃ")
SACCHIKATABBA = f"{SACCHIKAROTI}ရမည့် အရာကို {SACCHIKAROTI}ပြီး"
TR_MY = new(TR_PI, f"ထိုသူသည် {DUKKHA}ကို ပိုင်းခြား သိပြီး၊ {SAMUDAYA}ကို {PAHINA}၊ {NIRODHA}ကို {SACCHIKAROTI}ပြီး၊ "
                   f"{MAGGA}ကို {BHAVITA}၊ ထူးကဲစွာ သိရမည့် အရာကို ထူးကဲစွာ သိပြီး၊ ပိုင်းခြား သိရမည့် အရာကို "
                   f"ပိုင်းခြား သိပြီး၊ ပယ်ရမည့် အရာကို {PAHINA}၊ ပွားများရမည့် အရာကို {BHAVITA}၊ {SACCHIKATABBA}")
W("1", "^1-1", "pahātabbā", "ပယ်ရမည့်")
for _s in ("arahā", "samayavimutto arahā", "asamayavimutto arahā"):
    _m = PERS[_s]
    PROP_X[f"{_s} {EPI_PI}"] = V(f"{_m}သည် {EPI_MY}")
    PROP_X[f"{_s} {EPI_PI}; {TR_PI}"] = V(f"{_m}သည် {EPI_MY} ဖြစ်၍ {TR_MY}")
    PROP_X[f"{_s} vītarāgo vītadoso vītamoho"] = V(f"{_m}သည် {VITA3}")
PROP_X[TR_PI] = V(TR_MY)
PROP_X["sacchikātabbaṃ sacchikataṃ"] = V(SACCHIKATABBA)
PROP_X["ekadesaṃ " + EPI_PI] = V(f"တစ်စိတ်တစ်ဒေသ {EPI_MY}")
PROP_X["ekadesaṃ sacchikātabbaṃ sacchikataṃ"] = V(f"တစ်စိတ်တစ်ဒေသ {SACCHIKATABBA}")
PROP_X["ekadesaṃ sacchikātabbaṃ na sacchikataṃ"] = V(f"တစ်စိတ်တစ်ဒေသ {SACCHIKAROTI}ရမည့် အရာကို "
                                                     f"{SACCHIKAROTI}ပြီး", neg=True)
NEW["ekadesaṃ"] = "တစ်စိတ်တစ်ဒေသ"

# ---- Ariyapuggalasaṃsandana: the paravādī's thesis (^5-262)
PROP_X["samayavimutto arahā arahattā parihāyati, asamayavimutto arahā arahattā na parihāyati"] = V(
    f"{PERS['samayavimutto arahā']}သည် {ABL['arahattā']} {PARIH}သည်{C} {PERS['asamayavimutto arahā']}သည် "
    f"{ABL['arahattā']}", PARIH, neg=True)

# ---- Suttasādhana (^5-265 … ^5-268)
LINES_X["Uccāvacā hi paṭipadā, samaṇena pakāsitā;"] = new(
    "Uccāvacā hi paṭipadā, samaṇena pakāsitā;",
    "“ရဟန်းမြတ် ထင်ရှားပြတော်မူသော ကျင့်စဉ်တို့သည် ⟦0⟧ အမြင့်လည်း ရှိ၊ အနိမ့်လည်း ရှိ၏၊")
LINES_X["Na pāraṃ diguṇaṃ yanti, nayidaṃ ekaguṇaṃ mutanti."] = new(
    "Na pāraṃ diguṇaṃ yanti, nayidaṃ ekaguṇaṃ mutaṃ",
    "ကမ်းတစ်ဖက်သို့ နှစ်ကြိမ် မရောက်ကြ၊ ကမ်းတစ်ဖက်သို့ တစ်ကြိမ်တည်းဖြင့် ရောက်သည်ဟုလည်း မမှတ်ယူအပ်” ⟦0⟧။")
CHINNA = new("chinnassa chediyaṃ", "ဖြတ်ပြီးသော အရာ၌ ဖြတ်ဖွယ်")
PROP_X["atthi chinnassa chediyaṃ"] = V(CHINNA, "ရှိ")
LINES_X["Vītataṇho anādāno, kiccaṃ yassa na vijjati;"] = (
    "“တပ်မက်မှု ကင်း၍ စွဲလမ်းမှု မရှိသော၊ ပြုဖွယ် ကိစ္စ မရှိသော အကြင်သူ၌၊")
LINES_X["Chinnassa chediyaṃ natthi, oghapāso samūhatoti."] = (
    f"{CHINNA} မရှိ၊ ရေအလျဉ်ဟူသော ကျော့ကွင်းကို နုတ်ပယ်ပြီး ဖြစ်၏”{END}")
CAYA = new("katassa paticayo", "ပြုပြီးသော အရာ၌ ထပ်မံ စုဆောင်းခြင်း")
PROP_X["atthi katassa paticayo"] = V(CAYA, "ရှိ")
LINES_X["Tassa sammā vimuttassa, santacittassa bhikkhuno;"] = (
    "“ကောင်းစွာ လွတ်မြောက်၍ ငြိမ်သက်သော စိတ် ရှိသော ထိုရဟန်းအား၊")
LINES_X["Katassa paticayo natthi, karaṇīyaṃ na vijjati."] = f"{CAYA} မရှိ၊ ပြုဖွယ်လည်း မရှိ{END}"
LINES_X["Selo yathā ekagghano, vātena na samīrati;"] = (
    "“တစ်ခဲနက် ဖြစ်သော ကျောက်တောင်သည် လေကြောင့် မလှုပ်ရှားသကဲ့သို့၊")
LINES_X["Evaṃ rūpā rasā saddā, gandhā phassā ca kevalā."] = (
    "ထို့အတူ အဆင်းအရောင်၊ အရသာ၊ အသံ၊ အနံ့၊ အတွေ့တို့ အားလုံးသည်လည်း၊")
LINES_X["Iṭṭhā dhammā aniṭṭhā ca, nappavedhenti tādino;"] = (
    "“နှစ်သက်ဖွယ် သဘောတရားတို့နှင့် မနှစ်သက်ဖွယ် သဘောတရားတို့သည် ထိုသို့ တည်ကြည်သူကို မတုန်လှုပ်စေနိုင်ကြ၊")
LINES_X["Ṭhitaṃ cittaṃ vippamuttaṃ, vayaṃ cassānupassatīti."] = (
    f"ထိုသူ၏ စိတ်သည် တည်ငြိမ်၍ လွတ်မြောက်ပြီး ဖြစ်၏၊ ထိုသူသည် ထိုစိတ်၏ ပျက်ခြင်းကိုလည်း {ANUPASSI}၏” ⟦0⟧{END}")
for _k in list(LINES_X):
    new(_k, LINES_X[_k])
QUOTE_X["pañcime, bhikkhave, dhammā samayavimuttassa bhikkhuno parihānāya saṃvattanti. Katame pañca? Kammārāmatā, "
        "bhassārāmatā, niddārāmatā, saṅgaṇikārāmatā, yathāvimuttaṃ cittaṃ na paccavekkhati. Ime kho, bhikkhave, "
        "pañca dhammā samayavimuttassa bhikkhuno parihānāya saṃvattanti"] = (
    f"ရဟန်းတို့၊ ဤသဘောတရား ငါးပါးတို့သည် {SV_ADJ} ရဟန်း၏ {PARIH}ခြင်းအတွက် ဖြစ်စေကုန်၏။ အဘယ် ငါးပါးတို့နည်း။ "
    "အလုပ်ကို နှစ်သက်ခြင်း၊ စကားပြောခြင်းကို နှစ်သက်ခြင်း၊ အိပ်ခြင်းကို နှစ်သက်ခြင်း၊ အပေါင်းအသင်းကို နှစ်သက်ခြင်း၊ "
    "လွတ်မြောက်သည့်အတိုင်း စိတ်ကို ပြန်လည် မဆင်ခြင်ခြင်း။ ရဟန်းတို့၊ ဤသဘောတရား ငါးပါးတို့သည် "
    f"{SV_ADJ} ရဟန်း၏ {PARIH}ခြင်းအတွက် ဖြစ်စေကုန်၏")
ARAMATA = {"kammārāmatā": "အလုပ်ကို နှစ်သက်ခြင်း", "bhassārāmatā": "စကားပြောခြင်းကို နှစ်သက်ခြင်း",
           "niddārāmatā": "အိပ်ခြင်းကို နှစ်သက်ခြင်း", "saṅgaṇikārāmatā": "အပေါင်းအသင်းကို နှစ်သက်ခြင်း"}
for _k, _v in ARAMATA.items():
    PROP_X[f"atthi arahato {_k}"] = V(f"{ARAHA}၌ {_v}", "ရှိ")
    new(_k, _v)
KAMA7_PI = ("rāgo kāmarāgo kāmarāgapariyuṭṭhānaṃ kāmarāgasaṃyojanaṃ kāmogho kāmayogo kāmacchandanīvaraṇaṃ")
KAMACCHANDA = W("1", "^1-1158", "kāmacchandanīvaraṇaṃ", "ကာမကို လိုလားမှု အတားအဆီး")
KAMA7 = new(KAMA7_PI, f"{RAGA}၊ {KAMARAGA}၊ {KAMARAGA} {PARIYUTTHANA}၊ {KAMARAGA} {SAMYOJANA}၊ ကာမ ရေအလျဉ်၊ "
                      f"ကာမ ထမ်းပိုး၊ {KAMACCHANDA}")
PROP_X[f"atthi arahato {KAMA7_PI}"] = V(f"{ARAHA}၌ {KAMA7}", "ရှိ")
# ---- pariyuṭṭhāna / anusaya (^5-268)
SENT_X["Arahā arahattā parihāyamāno kiṃ pariyuṭṭhito parihāyatīti?"] = (
    f"{PARIHAYAMANO['arahā']}သည် အဘယ်အရာ၏ {PARIYUTTHANA}ကို ခံရ၍ {PARIH}သနည်း{END}")
for _k, _v in (("rāga", RAGA), ("dosa", DOSA), ("moha", MOHA)):
    PROP_X[f"{_k}pariyuṭṭhito parihāyati"] = V(f"{_v}၏ {PARIYUTTHANA}ကို ခံရ၍", PARIH)
SENT_X["Pariyuṭṭhānaṃ kiṃ paṭicca uppajjatīti?"] = f"{PARIYUTTHANA}သည် အဘယ်အရာကို မှီ၍ ဖြစ်ပေါ်သနည်း{END}"
PROP_X["anusayaṃ paṭicca uppajjati"] = V(f"{ANUSAYA}ကို မှီ၍", "ဖြစ်ပေါ်")
PROP_X["atthi arahato anusayā"] = V(f"{ARAHA}၌ {ANUSAYA}တို့", "ရှိ")
ANUS7 = W("2", "^2-816", "kāmarāgānusayo, paṭighānusayo, mānānusayo, diṭṭhānusayo, vicikicchānusayo, "
          "bhavarāgānusayo, avijjānusayo",
          "ကာမရာဂ ကိန်းအောင်းခြင်း၊ မုန်းတီးမှု ကိန်းအောင်းခြင်း၊ မာန ကိန်းအောင်းခြင်း၊ အယူ ကိန်းအောင်းခြင်း၊ "
          "ယုံမှားမှု ကိန်းအောင်းခြင်း၊ ဘဝရာဂ ကိန်းအောင်းခြင်း၊ အမှန်ကို မသိမှု ကိန်းအောင်းခြင်း")
PROP_X["atthi arahato kāmarāgānusayo paṭighānusayo mānānusayo diṭṭhānusayo vicikicchānusayo bhavarāgānusayo "
       "avijjānusayo"] = V(f"{ARAHA}၌ {ANUS7}", "ရှိ")
PROP_X["atthi arahato kāmarāgānusayo"] = FR(f"{ARAHA}၌ {KAMARAGA} {ANUSAYA}")
PROP_X["avijjānusayo"] = V(f"{AVIJJA} {ANUSAYA}", "ရှိ")
# ---- upacaya
SENT_X["Arahato arahattā parihāyamānassa kiṃ upacayaṃ gacchatīti?"] = (
    f"{PARIHAYAMANO['arahā']}၌ အဘယ်အရာသည် တိုးပွားခြင်းသို့ ရောက်သနည်း{END}")


@F.rule(r"(?P<k>" + alt(KIL) + r") upacayaṃ gacchati")
def _r_upacaya(m):
    return V(f"{KIL[m['k']]}သည် တိုးပွားခြင်းသို့", "ရောက်")


ACINA = {"ācinati": "စုဆောင်း", "apacinati": "ဖြိုဖျက်", "pajahati": "ပယ်", "upādiyati": "စွဲလမ်း",
         "visineti": "ဖြန့်ကြဲ", "ussineti": "စုပုံ", "vidhūpeti": "ငြိမ်းစေ", "sandhūpeti": "တောက်လောင်စေ"}
for _k, _v in ACINA.items():
    PROP_X[f"arahā {_k}"] = VV(f"{ARAHA}သည်", _v)
    new(_k, _v)
for _a, _b, _c in (("nevācinati na apacinati apacinitvā", "ācinati", "apacinati"),
                   ("neva pajahati na upādiyati pajahitvā", "pajahati", "upādiyati"),
                   ("neva visineti na ussineti visinitvā", "visineti", "ussineti"),
                   ("neva vidhūpeti na sandhūpeti vidhūpetvā", "vidhūpeti", "sandhūpeti")):
    PROP_X[f"arahā {_a} ṭhito"] = V(f"{ARAHA}သည် မ{ACINA[_b]}၊ မ{ACINA[_c]}၊ {ACINA[_b if _b != 'ācinati' else _c]}ပြီး၍ "
                                    "တည်နေသူ")


# ===================================================================================== Brahmacariyakathā (^5-269 … ^5-273)
LATE = []        # functions run after the tables are merged (lines composed from translated units)
SADHU = "ကောင်းစွာ ဆိုအပ်သော စကား၊ ဆိုးစွာ ဆိုအပ်သော စကားတို့၏ အနက်ကို"     # subhāsitadubbhāsitānaṃ atthaṃ
AVARANA = "အဟန့်အတား"                                              # āvaraṇa (kept apart from nīvaraṇa)
NIYAMA = f"ကုသိုလ် သဘောတရားတို့၌ မှန်ကန်ခြင်း၏ သေချာသော လမ်းသို့"     # niyāmaṃ … kusalesu dhammesu sammattaṃ
ANCHOR_X["elamūgā"] = "ဆွံ့အကြ၊"
ALL_DEVA = f"{DEVA}အားလုံးတို့သည်"
PROP_X["sabbe devā jaḷā elamūgā aviññū hatthasaṃvācikā nappaṭibalā subhāsitadubbhāsitānaṃ atthamaññātuṃ"] = Cl(
    f"{ALL_DEVA} ထုံထိုင်းကြ၊ ဆွံ့အကြ၊ နားမလည်တတ်ကြ၊ လက်ဟန်ဖြင့်သာ ပြောဆိုကြ၍ {SADHU}", "သိနိုင်ကြ", "မသိနိုင်ကြ",
    True)
PROP_X["sabbe devā na buddhe pasannā na dhamme pasannā na saṅghe pasannā"] = Cl(
    f"{ALL_DEVA} ဘုရား၌ မကြည်ညိုကြ၊ တရား၌ မကြည်ညိုကြ၊ {SANGHA}၌", "ကြည်ညိုကြ", "မကြည်ညိုကြ", True)
PROP_X["na buddhaṃ bhagavantaṃ payirupāsanti"] = VV(f"{BHAGAVA}ကို", "ဆည်းကပ်ကြ", True)
PROP_X["na buddhaṃ bhagavantaṃ pañhaṃ pucchanti"] = VV(f"{BHAGAVA}ကို ပြဿနာ", "မေးကြ", True)
VISSAJJ = f"{BHAGAVA} ပြဿနာကို ဖြေကြားတော်မူသောအခါ"
PROP_X["na buddhena bhagavatā pañhe vissajjite attamanā"] = VV(VISSAJJ, "နှစ်သက်ကြ", True)
PROP_X["sabbe devā kammāvaraṇena samannāgatā kilesāvaraṇena samannāgatā vipākāvaraṇena samannāgatā assaddhā "
       "acchandikā duppaññā abhabbā niyāmaṃ okkamituṃ kusalesu dhammesu sammattaṃ"] = VV(
    f"{ALL_DEVA} {F.KAMMA}၏ {AVARANA}နှင့် ပြည့်စုံကြ၊ {KILESA}၏ {AVARANA}နှင့် ပြည့်စုံကြ၊ {F.VIPAKA}၏ {AVARANA}နှင့် "
    f"ပြည့်စုံကြ၊ ယုံကြည်မှု မရှိကြ၊ ဆန္ဒ မရှိကြ၊ ပညာ ညံ့ကြ၍ {NIYAMA}", "သက်ဆင်းနိုင်ကြ", True)
KILL5 = ["အမိကို သတ်သူ", "အဖကို သတ်သူ", f"{ARAHA}ကို သတ်သူ", "ဘုရားရှင်၏ သွေးကို ထွက်စေသူ", f"{SANGHA}ကို ခွဲသူ"]
PROP_X["sabbe devā mātughātakā pitughātakā arahantaghātakā ruhiruppādakā saṅghabhedakā"] = Cl(
    f"{ALL_DEVA} {'၊ '.join(KILL5)}တို့", "ဖြစ်ကြ", "မဟုတ်ကြ")
TEN = [PANATIPATA.replace("ခြင်း", "သူ"), "မပေးသည်ကို ယူသူ", "ကာမတို့၌ မှားယွင်းစွာ ကျင့်သူ", "မုသား ပြောသူ",
       "ကုန်းတိုက်သော စကားကို ပြောသူ", "ကြမ်းတမ်းသော စကားကို ပြောသူ", "အကျိုးမဲ့ ပြိန်ဖျင်းသော စကားကို ပြောသူ",
       "သူ့ဥစ္စာကို လိုချင်သူ"]
for _x in TEN:
    W("4", "^4-136", "pāṇātipātī hoti, adinnādāyī hoti", _x)
W("2", "^2-487", "Adinnādānā veramaṇī", "မပေးသည်ကို ယူခြင်း")
W("2", "^2-487", "Kāmesumicchācārā veramaṇī", "ကာမတို့၌ မှားယွင်းစွာ ကျင့်ခြင်း")
W("2", "^2-487", "Musāvādā veramaṇī", "မုသား ပြောခြင်း")
BYAPANNA = f"{BYAPADA} ရှိသော စိတ် ရှိသူ"                         # byāpannacitto (pi-4 abyāpannacitto «… မရှိသော စိတ် ရှိသော»)
ABYAPANNA = f"{BYAPADA} မရှိသော စိတ် ရှိသူ"
W("4", "^4-136", "byāpannacitto hoti", BYAPANNA)
W("2", "^2-543", "Abyāpannacitto", ABYAPANNA)
W("4", "^4-136", "micchādiṭṭhi", f"{MICCHADITTHI} ရှိသူ")
MICCHAD = f"{MICCHADITTHI} ရှိသူ"
PROP_X["sabbe devā pāṇātipātino adinnādāyino kāmesumicchācārino musāvādino pisuṇavācā pharusāvācā samphappalāpino "
       "abhijjhāluno byāpannacittā micchādiṭṭhikā"] = Cl(
    f"{ALL_DEVA} {'၊ '.join(TEN + [BYAPANNA, MICCHAD])}တို့", "ဖြစ်ကြ", "မဟုတ်ကြ")
THERE_ARE = f"ကြသော {DEVA}တို့"                                     # atthi devā … (= «…ကြသော နတ်တို့ ရှိ»)
PROP_X["atthi devā ajaḷā anelamūgā viññū na hatthasaṃvācikā paṭibalā subhāsitadubbhāsitānaṃ atthamaññātuṃ"] = V(
    f"မထုံထိုင်းကြ၊ မဆွံ့အကြ၊ နားလည်တတ်ကြ၊ လက်ဟန်ဖြင့်သာ ပြောဆိုသူ မဟုတ်ကြဘဲ {SADHU} သိနိုင်{THERE_ARE}", "ရှိ")
PROP_X["atthi devā buddhe pasannā dhamme pasannā saṅghe pasannā"] = V(
    f"ဘုရား၌ ကြည်ညိုကြ၊ တရား၌ ကြည်ညိုကြ၊ {SANGHA}၌ ကြည်ညို{THERE_ARE}", "ရှိ")
PROP_X["atthi devā buddhe pasannā"] = V(f"ဘုရား၌ ကြည်ညို{THERE_ARE}", "ရှိ")
PROP_X["buddhaṃ bhagavantaṃ payirupāsanti"] = VV(f"{BHAGAVA}ကို", "ဆည်းကပ်ကြ")
PROP_X["buddhaṃ bhagavantaṃ pañhaṃ pucchanti"] = VV(f"{BHAGAVA}ကို ပြဿနာ", "မေးကြ")
PROP_X["buddhena bhagavatā pañhe vissajjite attamanā honti"] = VV(VISSAJJ, "နှစ်သက်ကြ")
PROP_X["atthi devā na kammāvaraṇena samannāgatā na kilesāvaraṇena samannāgatā na vipākāvaraṇena samannāgatā saddhā "
       "chandikā paññavanto bhabbā niyāmaṃ okkamituṃ kusalesu dhammesu sammattaṃ"] = V(
    f"{F.KAMMA}၏ {AVARANA}နှင့် မပြည့်စုံကြ၊ {KILESA}၏ {AVARANA}နှင့် မပြည့်စုံကြ၊ {F.VIPAKA}၏ {AVARANA}နှင့် "
    f"မပြည့်စုံကြ၊ ယုံကြည်မှု ရှိကြ၊ ဆန္ဒ ရှိကြ၊ ပညာ ရှိကြ၍ {NIYAMA} သက်ဆင်းနိုင်{THERE_ARE}", "ရှိ")
PROP_X["atthi devā na mātughātakā na pitughātakā na arahantaghātakā na ruhiruppādakā na saṅghabhedakā"] = V(
    f"{' မဟုတ်ကြ၊ '.join(KILL5)} မဟုတ်{THERE_ARE}", "ရှိ")
PROP_X["atthi devā na pāṇātipātino na adinnādāyino na kāmesumicchācārino na musāvādino na pisuṇāvācā na pharusāvācā "
       "na samphappalāpino na abhijjhāluno abyāpannacittā sammādiṭṭhikā"] = V(
    f"{' မဟုတ်ကြ၊ '.join(TEN)} မဟုတ်ကြ၊ {ABYAPANNA} ဖြစ်ကြ၊ {SAMMADITTHI} ရှိ{THERE_ARE}", "ရှိ")
PROP_X["sammādiṭṭhikā"] = V(f"{SAMMADITTHI} ရှိ{THERE_ARE}", "ရှိ")

# ---- the place of the holy life
MIL_PI = "milakkhesu aviññātāresu yattha natthi gati bhikkhūnaṃ bhikkhunīnaṃ upāsakānaṃ upāsikānaṃ"
BHIKKHU4 = W("2", "^2-514", "bhikkhūnaṃ bhikkhunīnaṃ upāsakānaṃ upāsikānaṃ", "ရဟန်းတို့၊ ဘိက္ခုနီတို့၊ ဥပါသကာတို့၊ ဥပါသိကာတို့")
MIL_MY = new(MIL_PI, f"{BHIKKHU4} သွားလာခြင်း မရှိသော၊ နားမလည်သော မိစ္ဆာ လူမျိုးတို့ နေထိုင်ရာ")
ANCHOR_X["milakkhesu"] = "မိစ္ဆာ လူမျိုးတို့"
ANCHOR_X["saññasattesu"] = ANCHOR_X["Saññasattesu"] = "မှတ်သိမှု ရှိသော"
BVLOC = {"devesu": f"{DEVA}တို့၌", "manussesu": f"{MANUSSA}တို့၌", "sabbadevesu": f"{DEVA}အားလုံးတို့၌",
         "sabbamanussesu": f"{MANUSSA}အားလုံးတို့၌", "asaññasattesu devesu": f"{ASANNA} {DEVA}တို့၌",
         "saññasattesu devesu": f"မှတ်သိမှု ရှိသော {DEVA}တို့၌", "paccantimesu janapadesu": "အစွန်အဖျား ဇနပုဒ်တို့၌",
         "majjhimesu janapadesu": "အလယ် ဇနပုဒ်တို့၌", "sāvatthiyaṃyeva": "သာဝတ္ထိ၌သာ", "tattheva": "ထိုအရပ်၌သာ",
         "tattha": "ထိုအရပ်၌", "aññatra": "အခြားအရပ်၌", "tasseva": "ထိုသူ၌သာ", "tassa": "ထိုသူ၌"}


def bv_loc(loc, mil):
    return (f"{MIL_MY} " if mil else "") + BVLOC[loc]


@F.rule(r"(?:(?P<n1>n)?atthi (?P<a>" + alt(BVLOC) + r")|(?P<b>" + alt(BVLOC) + r")(?: (?P<n2>n)?atthi)?|(?P<n3>n)atth(?P<c>aññatra))"
        r" brahmacariyavāso(?P<mil> " + MIL_PI + r")?")
def _r_bv(m):
    """(n)atthi LOC brahmacariyavāso / LOC (n)atthi brahmacariyavāso (MIL) / tattheva brahmacariyavāso (implied atthi)
    / natthaññatra brahmacariyavāso."""
    loc = m["a"] or m["b"] or m["c"]
    neg = bool(m["n1"] or m["n2"] or m["n3"])
    return V(f"{bv_loc(loc, m['mil'])} {BV}", "ရှိ", neg)


@F.rule(r"(?P<loc>" + alt(BVLOC) + r") atthi yattha atthi, atthi yattha natthi brahmacariyavāso(?P<mil> " + MIL_PI + r")?")
def _r_bv_some(m):
    return V(f"{bv_loc(m['loc'], m['mil'])} {BV} ရှိသော အရပ်လည်း ရှိ၏၊ မရှိသော အရပ်လည်း", "ရှိ")


PROP_X["atthi yattha atthi, atthi yattha natthi"] = V("ရှိသော အရပ်လည်း ရှိ၏၊ မရှိသော အရပ်လည်း", "ရှိ")
SENT_X["Kattha atthi, kattha natthīti?"] = f"အဘယ်အရပ်၌ ရှိ၍ အဘယ်အရပ်၌ မရှိသနည်း{END}"
MARK = {"pabbajjā": "ရဟန်းပြုခြင်း", "muṇḍiyaṃ": "ခေါင်းတုံးခြင်း", "kāsāvadhāraṇā": "သင်္ကန်း ဝတ်ဆောင်ခြင်း",
        "pattadhāraṇā": "သပိတ် ဆောင်ခြင်း"}
ARISE = {"sammāsambuddhā": (f"{SAMMASAMB}တို့", "ပေါ်ပေါက်ကြ"), "paccekasambuddhā": (f"{PACCEKA}တို့", "ပေါ်ပေါက်ကြ"),
         "sāvakayugaṃ": ("တပည့် အစုံ", "ပေါ်ပေါက်")}
W("2", "^2-487", "ariyasāvako", "အရိယာ တပည့်")
NEW["sāvakayuga"] = "တပည့် အစုံ"
PROP_X["atthi tattha pabbajjā muṇḍiyaṃ kāsāvadhāraṇā pattadhāraṇā"] = V(
    f"ထိုနတ်တို့၌ {'၊ '.join(MARK.values())}", "ရှိ")
for _k, (_s, _v) in ARISE.items():
    PROP_X[f"devesu {_k} uppajja{'ti' if _k == 'sāvakayugaṃ' else 'nti'}"] = VV(f"{DEVA}တို့၌ {_s}", _v)
    PROP_X[f"{_k} uppajja{'ti' if _k == 'sāvakayugaṃ' else 'nti'}"] = VV(_s, _v)
    PROP_X[f"devesu {_k} nuppajja{'ti' if _k == 'sāvakayugaṃ' else 'nti'}"] = VV(f"{DEVA}တို့၌ {_s}", _v, True)
for _k, _v in MARK.items():
    PROP_X[f"devesu {_k} natthi"] = V(f"{DEVA}တို့၌ {_v}", "ရှိ", True)


@F.rule(r"yattha (?:(?P<n1>n)?atthi (?P<x>" + alt(MARK) + r")|(?P<y>" + alt(ARISE) + r") (?P<n2>n)?uppajja(?:nti|ti))"
        r" (?:tattheva brahmacariyavāso|(?P<n3>n)atthi tattha brahmacariyavāso)")
def _r_yattha(m):
    neg = bool(m["n1"] or m["n2"])
    if neg != bool(m["n3"]):
        return None
    if m["x"]:
        head = f"အကြင်အရပ်၌ {MARK[m['x']]} {'မရှိ' if neg else 'ရှိ၏'}"
    else:
        s, v = ARISE[m["y"]]
        head = f"အကြင်အရပ်၌ {s} {'မ' + v if neg else v + '၏'}"
    return V(f"{head}၊ {'ထိုအရပ်၌' if neg else 'ထိုအရပ်၌သာ'} {BV}", "ရှိ", neg)


WHO_DOES = {"pabbajati": ("ရဟန်းပြု", "ရဟန်း မပြု"), "muṇḍo hoti": ("ခေါင်းတုံးသူ ဖြစ်", "ခေါင်းတုံးသူ မဖြစ်"),
            "kāsāvaṃ dhāreti": ("သင်္ကန်းကို ဝတ်ဆောင်", "သင်္ကန်းကို မဝတ်ဆောင်"),
            "pattaṃ dhāreti": ("သပိတ်ကို ဆောင်", "သပိတ်ကို မဆောင်")}


@F.rule(r"yo (?P<a>pabbajati|muṇḍo hoti|kāsāvaṃ dhāreti|pattaṃ dhāreti|na pabbajati|muṇḍo na hoti|kāsāvaṃ na dhāreti|"
        r"pattaṃ na dhāreti) (?:tasseva brahmacariyavāso|(?P<n>n)atthi tassa brahmacariyavāso)")
def _r_yo(m):
    a = m["a"].replace(" na ", " ").replace("na ", "")
    neg = " na " in f" {m['a']} " or m["a"].startswith("na ")
    if neg != bool(m["n"]):
        return None
    pos, ng = WHO_DOES[a]
    head = f"အကြင်သူ {ng}" if neg else f"အကြင်သူ {pos}၏"
    return V(f"{head}၊ {'ထိုသူ၌' if neg else 'ထိုသူ၌သာ'} {BV}", "ရှိ", neg)


PROP_X["lumbiniyā bhagavā jāto"] = VV(f"လုမ္ဗိနီ၌ {BHAGAVA}", "ဖွားမြင်တော်မူ")
PROP_X["bodhiyā mūle abhisambuddho"] = VV("ဗောဓိပင်ရင်း၌ ဘုရား", "ဖြစ်တော်မူ")
PROP_X["bārāṇasiyaṃ bhagavatā dhammacakkaṃ pavattitaṃ"] = VV(f"ဗာရာဏသီ၌ {BHAGAVA} ဓမ္မစကြာကို", "လည်စေတော်မူ")
PROP_X["majjhimesu janapadesu paccekasambuddhā uppajjanti"] = VV(f"{BVLOC['majjhimesu janapadesu']} {PACCEKA}တို့",
                                                                 "ပေါ်ပေါက်ကြ")
PROP_X["magadhesu sāvakayugaṃ uppannaṃ"] = VV("မဂဓ တိုင်း၌ တပည့် အစုံ", "ပေါ်ပေါက်ခဲ့")
IDHA_BV = new("idha brahmacariyavāso (sutta)", f"ဤနေရာ၌ {BV} ရှိခြင်း")
QUOTE_X["tīhi, bhikkhave, ṭhānehi jambudīpakā manussā uttarakuruke ca manusse adhiggaṇhanti deve ca tāvatiṃse! "
        "Katamehi tīhi? Sūrā, satimanto, idha brahmacariyavāso"] = (
    f"ရဟန်းတို့၊ ဇမ္ဗူဒီပါ ကျွန်း၌ နေသော {MANUSSA}တို့သည် အကြောင်း သုံးပါးတို့ဖြင့် ဥတ္တရကုရု ကျွန်း၌ နေသော "
    f"{MANUSSA}တို့ကိုလည်းကောင်း၊ တာဝတိံသာ {DEVA}တို့ကိုလည်းကောင်း သာလွန်ကြ၏။ အဘယ် သုံးပါးတို့ဖြင့်နည်း။ "
    f"ရဲရင့်ကြခြင်း၊ သတိ ရှိကြခြင်း၊ {IDHA_BV}")
PROP_X["sāvatthiyaṃ vuttaṃ bhagavatā – idha brahmacariyavāso"] = Cl(
    f"သာဝတ္ထိ၌ {BHAGAVA} ဤသို့", "ဟောတော်မူ", "မဟောတော်မူ", post=f" – «{IDHA_BV}»")

# ---- the non-returner reborn there (^5-272)
ANAG_P = f"{ANAGAMI} {PUG}"
PROP_X["anāgāmissa puggalassa pañcorambhāgiyāni saṃyojanāni pahīnāni"] = V(f"{ANAG_P}သည် {ORAMBH}တို့ကို {PAHINA}")
PROP_X["pañcuddhambhāgiyāni saṃyojanāni appahīnāni"] = Cl(f"{UDDHAMBH}တို့ကို", PAHINA, "မပယ်ရသေး", True)
REBORN = new("ito cutassa tattha upapannassa", f"ဤလောကမှ သေ၍ ထိုဘုံ၌ {UPAPAJJ}သော ထိုသူ၏")
W("4", "^4-40", "avihā cuto", "သေ၍")
TASK = {"phaluppatti": "ဖိုလ် ဖြစ်ပေါ်ခြင်း", "bhāroharaṇaṃ": "ဝန်ကို ချခြင်း",
        "dukkhapariññātaṃ": f"{DUKKHA}ကို ပိုင်းခြား သိခြင်း", "kilesappahānaṃ": f"{KILESA}ကို ပယ်ခြင်း",
        "nirodhasacchikiriyā": f"{NIRODHA}ကို {SACCHIKAROTI}ခြင်း", "akuppapaṭivedho": f"{AKUPPA} အရာကို {PATIVEDHA}"}


@F.rule(r"(?P<r>ito cutassa tattha upapannassa )?(?P<w>kuhiṃ|tahiṃ) (?P<t>" + alt(TASK) + r")")
def _r_task(m):
    pre = f"{REBORN} " if m["r"] else ""
    if m["w"] == "kuhiṃ":
        return Wh(f"{pre}{TASK[m['t']]}သည် အဘယ်အရပ်၌", "ဖြစ်")
    return V(f"{pre}{TASK[m['t']]}သည် ထိုဘုံ၌")


SENT_X["Tattheva."] = f"ထိုဘုံ၌ပင် ဖြစ်သည်{END}"


def _kena(m):
    inner = F.prop_my("natthi devesu brahmacariyavāso", "stmt", 1)
    return Wh("အဘယ် အကြောင်းကြောင့် သင်သည်", "ပြော", post=f" – «{inner}»")


F.RULES.append((re.compile(r"kenaṭṭhena vadesi – natthi devesu brahmacariyavāso"), _kena))
IDHA, TATTHA = "ဤလောက၌", "ထိုဘုံ၌"
PARINIBB_P = f"{IDHA} {PARINIBB}မည့်"
ANCHOR_X["parinibbāyipuggalo"] = PARINIBB_P
PPN = {"anāgāmī puggalo": ANAG_P, "sotāpanno puggalo": f"{SOTAPANNA} {PUG}", "sakadāgāmī puggalo": f"{SAKADAGAMI} {PUG}"}


@F.rule(r"(?P<h>handa hi )?(?P<p>" + alt(PPN) + r")(?P<ip> idha parinibbāyipuggalo)? (?P<a>idha|tattha) bhāvitena maggena"
        r" (?P<b>idha|tattha) (?P<s>phalaṃ sacchikaroti|sasallova parinibbāyati)")
def _r_phala(m):
    who = PPN[m["p"]]
    if m["ip"]:
        who = f"{PARINIBB_P} {who}"
    a = IDHA if m["a"] == "idha" else TATTHA
    b = IDHA if m["b"] == "idha" else TATTHA
    pre = ("ကဲ၊ " if m["h"] else "") + f"{who}သည် {a} ပွားများခဲ့သော {MAGGA}ဖြင့် {b}"
    if m["s"].startswith("phalaṃ"):
        return VV(f"{pre} ဖိုလ်ကို", SACCHIKAROTI)
    return VV(f"{pre} မြားပါလျက်ပင်", PARINIBB)


IVN = W("4", "^4-M-16", "idha vihāya niṭṭhā", "ဤလောကကို စွန့်ခွာပြီးမှ")
GENP = {"idha vihāya niṭṭhassa puggalassa": f"{IVN} ပြီးမြောက်သော {PUG}",
        "sotāpattiphalasacchikiriyāya paṭipannassa puggalassa": f"{FRUIT['sotāpatti']}ကို {SACCHIKAROTI}ရန် ကျင့်ကြံသော {PUG}",
        "sakadāgāmiphalasacchikiriyāya paṭipannassa puggalassa":
            f"{FRUIT['sakadāgāmi']}ကို {SACCHIKAROTI}ရန် ကျင့်ကြံသော {PUG}",
        "arahattasacchikiriyāya paṭipannassa puggalassa": f"{ARAHATTA_N}ကို {SACCHIKAROTI}ရန် ကျင့်ကြံသော {PUG}"}
W("4", "^4-M-7", "Sotāpattiphalasacchikiriyāya paṭipanno", f"{FRUIT['sotāpatti']}ကို {SACCHIKAROTI}ရန် ကျင့်ကြံသူ")
APUBBA = W("2", "^2-809", "apubbaṃ acarimaṃ", "ရှေ့ မရှိ၊ နောက် မရှိဘဲ")
for _k, _v in GENP.items():
    PROP_X[_k] = FR(_v)


@F.rule(r"(?P<g>" + alt(GENP) + r")(?P<ac> apubbaṃ acarimaṃ)? maggo ca bhāvīyati")
def _r_bhaviyati(m):
    return VV(f"{GENP[m['g']]}သည်{' ' + APUBBA if m['ac'] else ''} {MAGGA}ကိုလည်း", "ပွားများ")


PROP_X["na ca kilesā pahīyanti"] = VV(f"{KILESA}တို့ကိုကား", "ပယ်", True)
PROP_X["kilesā ca pahīyanti"] = VV(f"{KILESA}တို့ကိုလည်း", "ပယ်")
KATA = new("katakaraṇīyo bhāvitabhāvano", "ပြုဖွယ် ကိစ္စကို ပြုပြီး၊ ပွားများဖွယ်ကို ပွားများပြီး")
ANOHATA = "ဝန်ကို မချရသေး"
UNDONE = new("apariññātadukkho appahīnakileso asacchikatanirodho appaṭividdhākuppo",
             f"{DUKKHA}ကို ပိုင်းခြား မသိရသေး၊ {KILESA}ကို မပယ်ရသေး၊ {NIRODHA}ကို မျက်မှောက် မပြုရသေး၊ "
             f"{AKUPPA} အရာကို ထိုးထွင်း မသိမြင်ရသေး")
UNSEEN = f"{AKUPPA} အရာကို ထိုးထွင်း မသိမြင်ရသေး"
PROP_X["anāgāmī puggalo katakaraṇīyo bhāvitabhāvano tattha upapajjati"] = VV(f"{KATA}သော {ANAG_P}သည် {TATTHA}",
                                                                            UPAPAJJ)
PROP_X["anāgāmī puggalo katakaraṇīyo bhāvitabhāvano anohaṭabhāro tattha upapajjati"] = VV(
    f"{KATA}၍ {ANOHATA}သော {ANAG_P}သည် {TATTHA}", UPAPAJJ)
PROP_X["anāgāmī puggalo katakaraṇīyo bhāvitabhāvano apariññātadukkho appahīnakileso asacchikatanirodho "
       "appaṭividdhākuppo tattha upapajjati"] = VV(f"{KATA}၍ {UNDONE}သော {ANAG_P}သည် {TATTHA}", UPAPAJJ)
PROP_X["arahā upapajjati"] = VV(f"{ARAHA}သည်", UPAPAJJ)
PUNABBHAVA = new("punabbhava", "ဘဝသစ်")
PROP_X["atthi arahato punabbhavo"] = V(f"{ARAHA}၌ {PUNABBHAVA}", "ရှိ")
PROP_X["arahā bhavena bhavaṃ gacchati"] = VV(f"{ARAHA}သည် ဘဝမှ ဘဝသို့", "သွား")
PROP_X["gatiyā gatiṃ gacchati"] = VV("လားရာမှ လားရာသို့", "သွား")
PROP_X["saṃsārena saṃsāraṃ gacchati"] = VV("သံသရာမှ သံသရာသို့", "သွား")
PROP_X["upapattiyā upapattiṃ gacchati"] = VV(f"{UPAPAJJ}ခြင်းမှ {UPAPAJJ}ခြင်းသို့", "သွား")
PROP_X["bhāroharaṇāya puna maggaṃ bhāveti"] = VV(f"ဝန်ကို ချရန် {MAGGA}ကို တစ်ဖန်", "ပွားများ")
PROP_X["na ca bhāroharaṇāya puna maggaṃ bhāveti"] = VV(f"ဝန်ကို ချရန် {MAGGA}ကိုလည်း တစ်ဖန်", "ပွားများ", True)
PROP_X["akuppapaṭivedhāya puna maggaṃ bhāveti"] = VV(f"{AKUPPA} အရာကို ထိုးထွင်း သိမြင်ရန် {MAGGA}ကို တစ်ဖန်", "ပွားများ")
PROP_X["na ca akuppapaṭivedhāya puna maggaṃ bhāveti"] = VV(
    f"{AKUPPA} အရာကို ထိုးထွင်း သိမြင်ရန် {MAGGA}ကိုလည်း တစ်ဖန်", "ပွားများ", True)
PROP_X["anohaṭabhāro ca tattha parinibbāyati"] = VV(f"{ANOHATA}ဘဲလည်း {TATTHA}", PARINIBB)
PROP_X["appaṭividdhākuppo ca tattha parinibbāyati"] = VV(f"{UNSEEN}ဘဲလည်း {TATTHA}", PARINIBB)
MIGA = new("yathā migo sallena viddho dūrampi gantvā", "မြားဖြင့် ထိုးမိသော သမင်သည် အဝေးသို့ပင် သွားပြီးမှ")
PROP_X["yathā migo sallena viddho dūrampi gantvā kālaṃ karoti, evamevaṃ anāgāmī puggalo idha bhāvitena maggena "
       "tattha phalaṃ sacchikaroti"] = VV(
    f"{MIGA} သေသကဲ့သို့ {EVAM} {ANAG_P}သည် {IDHA} ပွားများခဲ့သော {MAGGA}ဖြင့် {TATTHA} ဖိုလ်ကို", SACCHIKAROTI)
PROP_X["yathā migo sallena viddho dūrampi gantvā sasallova kālaṃ karoti, evamevaṃ anāgāmī puggalo idha bhāvitena "
       "maggena tattha sasallova parinibbāyati"] = VV(
    f"{MIGA} မြားပါလျက်ပင် သေသကဲ့သို့ {EVAM} {ANAG_P}သည် {IDHA} ပွားများခဲ့သော {MAGGA}ဖြင့် {TATTHA} မြားပါလျက်ပင်",
    PARINIBB)

# ===================================================================================== Odhisokathā (^5-274 … ^5-278)
PROP_X["odhisodhiso kilese jahati"] = VV(f"{KILESA}တို့ကို အပိုင်းအပိုင်း", JAHATI)
PATIPANNO = {f"{k}sacchikiriyāya paṭipanno puggalo": f"{v}ကို {SACCHIKAROTI}ရန် ကျင့်ကြံသော {PUG}" for k, v in
             (("sotāpattiphala", FRUIT["sotāpatti"]), ("sakadāgāmiphala", FRUIT["sakadāgāmi"]),
              ("anāgāmiphala", FRUIT["anāgāmi"]), ("arahatta", ARAHATTA_N))}
SEE4 = {"dukkha": DUKKHA, "samudaya": SAMUDAYA, "nirodha": NIRODHA, "magga": MAGGA}


@frame(r"(?:(?P<p>" + altc(PATIPANNO) + r") )?(?P<d>[Dd]ukkha|[Ss]amudaya|[Nn]irodha|[Mm]agga)dassanena kiṃ jahatīti\?")
def _f_kim(m):
    who = f"{PATIPANNO[low(m['p'])]}သည် " if m["p"] else ""
    return f"{who}{SEE4[low(m['d'])]}ကို မြင်ခြင်းဖြင့် အဘယ်အရာကို {JAHATI}သနည်း{END}"


ACCK = {"sakkāyadiṭṭhiṃ": SAKKAYA, "vicikicchaṃ": VICIKICCHA, "sīlabbataparāmāsaṃ": SILABBATA,
        "oḷārikaṃ kāmarāgaṃ": f"{OLARIKA} {KAMARAGA}", "oḷārikaṃ byāpādaṃ": f"{OLARIKA} {BYAPADA}",
        "aṇusahagataṃ kāmarāgaṃ": f"{ANUSAHA} {KAMARAGA}", "aṇusahagataṃ byāpādaṃ": f"{ANUSAHA} {BYAPADA}",
        "rūparāgaṃ": RUPARAGA, "arūparāgaṃ": ARUPARAGA, "mānaṃ": MANA, "uddhaccaṃ": UDDHACCA, "avijjaṃ": AVIJJA,
        "kāmarāgabyāpādaṃ": f"{KAMARAGA}နှင့် {BYAPADA}"}
TADEK = W("1", "^1-986", "tadekaṭṭhā ca kilesā", "ထိုတို့နှင့် တစ်နေရာတည်း တည်ရှိသော ကိလေသာ")
INS_M = {"anāgāmimaggena": MAGGA_OF["anāgāmi"] + "ဖြင့်"}


@F.rule(r"(?:(?P<i>anāgāmimaggena) )?(?P<o>(?:(?:" + alt(ACCK) + r") )*)(?P<t>tadekaṭṭhe ca kilese )?(?P<e>ekadese )?jahati")
def _r_jahati_obj(m):
    objs = re.findall(alt(ACCK), m["o"])
    if not objs and not m["t"]:
        return None
    parts = []
    if objs:
        parts.append("၊ ".join(ACCK[x] for x in objs) + "ကို")
    if m["t"]:
        parts.append(f"{TADEK}တို့ကိုလည်း")
    pre = (INS_M[m["i"]] + " " if m["i"] else "") + "၊ ".join(parts) + (" တစ်စိတ်တစ်ဒေသ" if m["e"] else "")
    return VV(pre, JAHATI)


ONE = "တစ်စိတ်တစ်ဒေသ"
EKAP = {"sotāpanno": SOTAPANNA, "sakadāgāmī": SAKADAGAMI, "anāgāmī": ANAGAMI, "arahā": ARAHA}


@F.rule(r"ekadesaṃ (?P<n>na )?(?P<p>sotāpanno|sakadāgāmī|anāgāmī|arahā)")
def _r_ekadesa_p(m):
    return V(f"{ONE} {EKAP[m['p']]}", neg=bool(m["n"]))


ATTAINED = {"sotāpattiphala": FRUIT["sotāpatti"], "sakadāgāmiphala": FRUIT["sakadāgāmi"],
            "anāgāmiphala": FRUIT["anāgāmi"], "arahatta": ARAHATTA_N}
for _k, _v in ATTAINED.items():
    PROP_X[f"ekadesaṃ {_k}ppatto paṭiladdho adhigato sacchikato upasampajja viharati"] = VV(
        f"{ONE} {_v}သို့ ရောက်ပြီး၊ ရရှိပြီး၊ ပိုင်ဆိုင်ပြီး၊ {SACCHIKAROTI}ပြီး၍ ပြည့်စုံစွာ ဝင်ရောက်၍", "နေ")
    ANCHOR_X[f"{_k}ppatto"] = f"{_v}သို့ ရောက်ပြီး"
PROP_X["kāyena phusitvā viharati"] = VV(KAYENA, "နေ")
PROP_X["ekadesaṃ na kāyena phusitvā viharati"] = VV(f"{ONE} {KAYENA}", "နေ", True)
SATTAKKH = W("4", "^4-M-7", "Sattakkhattuparamo", "အများဆုံး ခုနစ်ကြိမ်သာ ပြန်လည် ဖြစ်ပေါ်သူ")
KOLANK = W("4", "^4-M-7", "Kolaṅkolo", "အမျိုးမှ အမျိုးသို့ ကူးသူ")
EKABIJI = W("4", "^4-M-7", "Ekabījī", "မျိုးစေ့ တစ်စေ့သာ ရှိသူ")
PROP_X["ekadesaṃ sattakkhattuparamo"] = V(f"{ONE} {SATTAKKH}")
PROP_X["kolaṅkolo"] = V(KOLANK)
PROP_X["ekabījī"] = V(EKABIJI)
PROP_X["buddhe aveccappasādena samannāgato"] = VV("ဘုရား၌ ခိုင်မြဲသော ကြည်ညိုမှုနှင့်", "ပြည့်စုံ")
PROP_X["dhamme"] = FR("တရား၌")
PROP_X["saṅghe"] = FR(f"{SANGHA}၌")
ARIYAKANTA = new("ariyakantehi sīlehi", "အရိယာတို့ နှစ်သက်သော သီလတို့နှင့်")
PROP_X["ariyakantehi sīlehi samannāgato"] = VV(ARIYAKANTA, "ပြည့်စုံ")
PROP_X["ekadesaṃ ariyakantehi sīlehi samannāgato"] = VV(f"{ONE} {ARIYAKANTA}", "ပြည့်စုံ")
PROP_X["ekadesaṃ ariyakantehi sīlehi na samannāgato"] = VV(f"{ONE} {ARIYAKANTA}", "ပြည့်စုံ", True)
PROP_X["ariyakantehi sīlehi samannāgato ekadesaṃ ariyakantehi sīlehi na samannāgato"] = VV(
    f"{ARIYAKANTA} ပြည့်စုံ၏၊ {ONE} {ARIYAKANTA}", "ပြည့်စုံ", True)        # source: no comma (^5-274)
ANAG5 = {"antarāparinibbāyī": "Antarāparinibbāyī", "upahaccaparinibbāyī": "Upahaccaparinibbāyī",
         "asaṅkhāraparinibbāyī": "Asaṅkhāraparinibbāyī", "sasaṅkhāraparinibbāyī": "Sasaṅkhāraparinibbāyī"}
_A5 = {"antarāparinibbāyī": "သက်တမ်း၏ အလယ်သို့ မရောက်မီ ပရိနိဗ္ဗာန် ပြုသူ",
       "upahaccaparinibbāyī": "သက်တမ်း၏ အလယ်ကို ကျော်ပြီးမှ ပရိနိဗ္ဗာန် ပြုသူ",
       "asaṅkhāraparinibbāyī": "တိုက်တွန်းမှု မရှိဘဲ ပရိနိဗ္ဗာန် ပြုသူ",
       "sasaṅkhāraparinibbāyī": "တိုက်တွန်းမှုဖြင့် ပရိနိဗ္ဗာန် ပြုသူ"}
for _k, _p in ANAG5.items():
    W("4", "^4-M-7", _p, _A5[_k])
UDDHAMSOTA = W("4", "^4-40", "uddhaṃsoto akaniṭṭhagāmī", "အထက်သို့ စီးဆင်း၍ အကနိဋ္ဌ ဘုံသို့ ရောက်သူ")
PROP_X["ekadesaṃ antarāparinibbāyī"] = V(f"{ONE} {_A5['antarāparinibbāyī']}")
for _k in ("upahaccaparinibbāyī", "asaṅkhāraparinibbāyī", "sasaṅkhāraparinibbāyī"):
    PROP_X[_k] = V(_A5[_k])
PROP_X["uddhaṃsoto akaniṭṭhagāmī"] = V(UDDHAMSOTA)
PROP_X["ekadesaṃ uddhaṃsoto akaniṭṭhagāmī"] = V(f"{ONE} {UDDHAMSOTA}")
PROP_X["ekadesaṃ na uddhaṃsoto akaniṭṭhagāmī"] = V(f"{ONE} {UDDHAMSOTA}", neg=True)
PROP_X["(ekadesaṃ sacchikātabbaṃ sacchikataṃ,) ekadesaṃ sacchikātabbaṃ na sacchikataṃ"] = V(
    f"({ONE} {SACCHIKATABBA}၊) {ONE} {SACCHIKAROTI}ရမည့် အရာကို {SACCHIKAROTI}ပြီး", neg=True)
_L72 = ("Arahattasacchikiriyāya paṭipanno puggalo dukkhadassanena kiṃ jahatīti? Rūparāgaṃ arūparāgaṃ mānaṃ uddhaccaṃ "
        "avijjaṃ tadekaṭṭhe ca kilese ekadese jahatīti. Ekadesaṃ arahā, ekadesaṃ na arahā, ekadesaṃ arahattappatto "
        "paṭiladdho adhigato sacchikato upasampajja viharati, kāyena phusitvā viharati, ekadesaṃ na kāyena phusitvā "
        "viharati, ekadesaṃ " + EPI_PI + ", " + TR_PI + ", (ekadesaṃ sacchikātabbaṃ sacchikataṃ,) ekadesaṃ "
        "sacchikātabbaṃ na sacchikatanti? Na hevaṃ vattabbe…pe….")


def _late_l72():
    sents = re.split(r"(?<=\?|\.) (?=[A-Z])", F.norm_pe(_L72))
    my = [F.unit_my(x) for x in sents]
    s3 = my[2].replace(ANCHOR_X["arahattappatto"], ANCHOR_X["arahattappatto"] + " ⟦0⟧", 1).replace("၊)", "၊) ⟦1⟧", 1)
    my[2] = s3
    LINES_X[F.norm_pe(_L72)] = " ".join(my)
    F.LINES[F.norm_pe(_L72)] = LINES_X[F.norm_pe(_L72)]


LATE.append(_late_l72)
LINES_X["Anupubbena medhāvī, thokaṃ thokaṃ khaṇe khaṇe;"] = "“ပညာရှိသည် အစဉ်အတိုင်း၊ အနည်းငယ် အနည်းငယ်၊ ခဏ ခဏ၌၊"
LINES_X["Kammāro rajatasseva, niddhame malamattanoti."] = (
    f"ပန်းထိမ်သည် ငွေ၏ အညစ်အကြေးကို ဖယ်ရှားသကဲ့သို့ မိမိ၏ အညစ်အကြေးကို ဖယ်ရှားရာ၏” ⟦0⟧{END}")
LINES_X["Sahāvassa dassanasampadāya,"] = "“ထိုသူ၏ အမြင် ပြည့်စုံခြင်းနှင့် တစ်ပြိုင်နက်ပင်၊"
LINES_X["Tayassu dhammā jahitā bhavanti;"] = f"သဘောတရား သုံးပါးတို့ကို {JAHATI}ပြီး ဖြစ်ကုန်၏၊"
LINES_X["Sakkāyadiṭṭhī vicikicchitañca,"] = f"{SAKKAYA}၊ ယုံမှားခြင်း၊"
LINES_X["Sīlabbataṃ vāpi yadatthi kiñci;"] = "သီလ အကျင့်ဝတ်ဆိုင်ရာ ယူဆမှု တစ်စုံတစ်ရာ ရှိသမျှကိုလည်းကောင်း၊"
LINES_X["Catūhapāyehi ca vippamutto,"] = f"{APAYA} လေးပါးတို့မှလည်း လွတ်မြောက်ပြီး ဖြစ်၏၊"
LINES_X["Chaccābhiṭhānāni abhabba kātunti."] = "ကြီးလေးသော ဒုစရိုက် ခြောက်ပါးတို့ကို ပြုလုပ်ရန် မစွမ်းနိုင် ⟦0⟧” ⟦1⟧။"
QUOTE_X["yasmiṃ, bhikkhave, samaye ariyasāvakassa virajaṃ vītamalaṃ dhammacakkhuṃ udapādi – yaṃ kiñci "
        "samudayadhammaṃ, sabbaṃ taṃ nirodhadhammanti, saha dassanuppādā, bhikkhave, ariyasāvakassa tīṇi saṃyojanāni "
        "pahīyanti – sakkāyadiṭṭhi vicikicchā sīlabbataparāmāso"] = (
    "ရဟန်းတို့၊ အကြင်အခါ၌ အရိယာ တပည့်အား မြူ ကင်းသော၊ အညစ်အကြေး ကင်းသော တရားမျက်စိ ဖြစ်ပေါ်၏ – "
    "‹ဖြစ်ပေါ်တတ်သော သဘော ရှိသမျှ အားလုံးသည် ချုပ်ငြိမ်းတတ်သော သဘော ရှိ၏›ဟု၊ ရဟန်းတို့၊ (သစ္စာကို) မြင်ခြင်း "
    f"ဖြစ်ပေါ်သည်နှင့် တစ်ပြိုင်နက် အရိယာ တပည့်သည် {SAMYOJANA} သုံးပါးတို့ကို ပယ်၏ – {SAKKAYA}၊ {VICIKICCHA}၊ "
    f"{SILABBATA}")


# ===================================================================================== Jahatikathā (^5-279 … ^5-281)
VIKKH = new("vikkhambheti", "ဖိနှိပ်ထား")
JV = {"jahati": JAHATI, "vikkhambheti": VIKKH}
ADV = {"accantaṃ": "အပြီးအပိုင်", "anavasesaṃ": "အကြွင်းမဲ့", "appaṭisandhiyaṃ": "ပြန်လည် မဆက်စပ်နိုင်အောင်",
       "samūlaṃ": "အမြစ်နှင့်တကွ", "sataṇhaṃ": "တပ်မက်မှုနှင့်တကွ", "sānusayaṃ": f"{ANUSAYA}နှင့်တကွ",
       "ariyena ñāṇena": "အရိယာ ဉာဏ်ဖြင့်", "ariyena maggena": f"အရိယာ {MAGGA}ဖြင့်",
       "akuppaṃ paṭivijjhanto": f"{AKUPPA} အရာကို ထိုးထွင်း သိမြင်လျက်",
       "anāgāmiphalaṃ sacchikaronto": f"{FRUIT['anāgāmi']}ကို {SACCHIKAROTI}လျက်"}
for _k, _v in ADV.items():
    new(_k, _v)


@F.rule(r"(?P<so>so ca )?(?P<n>na )?(?P<a>" + alt(ADV) + r") (?P<v>jahati|vikkhambheti)")
def _r_adv(m):
    pre = ("ထိုသူသည်လည်း " if m["so"] else "") + ADV[m["a"]]
    return VV(pre, JV[m["v"]], bool(m["n"]))


WHOJ = {"puthujjano": PUTHUJJANA, "anāgāmiphalasacchikiriyāya paṭipanno puggalo": PATIPANNO[
    "anāgāmiphalasacchikiriyāya paṭipanno puggalo"]}
RUPAVAC = W("1", "^1-1289", "Katame dhammā rūpāvacarā", "သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော")
MAGGA_INS = {"rūpāvacarena maggena": f"{RUPAVAC} {MAGGA}ဖြင့်", "anāgāmimaggena": f"{MAGGA_OF['anāgāmi']}ဖြင့်"}
KB = ACCK["kāmarāgabyāpādaṃ"]


@F.rule(r"(?P<v>jahati|vikkhambheti) (?P<w>" + alt(WHOJ) + r")(?: (?P<m>" + alt(MAGGA_INS) + r"))? kāmarāgabyāpādaṃ")
def _r_jahati_who(m):
    mg = f"{MAGGA_INS[m['m']]} " if m["m"] else ""
    return VV(f"{WHOJ[m['w']]}သည် {mg}{KB}ကို", JV[m["v"]])


NIYY = {"niyyāniko": ("လွတ်မြောက်ရာသို့ ပို့ဆောင်သော", "လွတ်မြောက်ရာသို့ မပို့ဆောင်သော"),
        "khayagāmī": ("ကုန်ခန်းခြင်းဆီသို့ ဦးတည်သော", "ကုန်ခန်းခြင်းဆီသို့ ဦးမတည်သော"),
        "bodhagāmī": ("ထိုးထွင်း သိခြင်းဆီသို့ ဦးတည်သော", "ထိုးထွင်း သိခြင်းဆီသို့ ဦးမတည်သော"),
        "apacayagāmī": ("လျော့ပါးခြင်းဆီသို့ ဦးတည်သော", "လျော့ပါးခြင်းဆီသို့ ဦးမတည်သော"),
        "āsavo": ("စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော", "စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော"),
        "saṃyojaniyo": ("နှောင်ကြိုး၏ အာရုံ မဖြစ်နိုင်သော", "နှောင်ကြိုး၏ အာရုံ ဖြစ်နိုင်သော"),
        "ganthaniyo": ("အထုံး၏ အာရုံ မဖြစ်နိုင်သော", "အထုံး၏ အာရုံ ဖြစ်နိုင်သော"),
        "oghaniyo": ("ရေအလျဉ်၏ အာရုံ မဖြစ်နိုင်သော", "ရေအလျဉ်၏ အာရုံ ဖြစ်နိုင်သော"),
        "yoganiyo": ("ထမ်းပိုး၏ အာရုံ မဖြစ်နိုင်သော", "ထမ်းပိုး၏ အာရုံ ဖြစ်နိုင်သော"),
        "nīvaraṇiyo": ("အတားအဆီး၏ အာရုံ မဖြစ်နိုင်သော", "အတားအဆီး၏ အာရုံ ဖြစ်နိုင်သော"),
        "parāmaṭṭho": ("မှားယွင်းသော ယူဆမှု၏ အာရုံ မဖြစ်နိုင်သော", "မှားယွင်းသော ယူဆမှု၏ အာရုံ ဖြစ်နိုင်သော"),
        "upādāniyo": ("စွဲလမ်းမှု၏ အာရုံ မဖြစ်နိုင်သော", "စွဲလမ်းမှု၏ အာရုံ ဖြစ်နိုင်သော"),
        "saṃkilesiyo": ("ကိလေသာ၏ အာရုံ မဖြစ်နိုင်သော", "ကိလေသာ၏ အာရုံ ဖြစ်နိုင်သော")}
NIYY_TOK = {"niyyāniko": ("niyyāniko", 0), "aniyyāniko": ("niyyāniko", 1), "anāsavo": ("āsavo", 0),
            "sāsavo": ("āsavo", 1), "asaṃyojaniyo": ("saṃyojaniyo", 0), "saṃyojaniyo": ("saṃyojaniyo", 1),
            "aganthaniyo": ("ganthaniyo", 0), "anoghaniyo": ("oghaniyo", 0), "ayoganiyo": ("yoganiyo", 0),
            "anīvaraṇiyo": ("nīvaraṇiyo", 0), "aparāmaṭṭho": ("parāmaṭṭho", 0), "anupādāniyo": ("upādāniyo", 0),
            "asaṃkilesiyo": ("saṃkilesiyo", 0), "saṃkilesiyo": ("saṃkilesiyo", 1)}
for _w in ("khayagāmī", "bodhagāmī", "apacayagāmī"):
    NIYY_TOK[_w] = (_w, 0)
    NIYY_TOK["na " + _w] = (_w, 1)
W("1", "^1-M2-51", "parāmaṭṭhā dhammā", "မှားယွင်းသော ယူဆမှု၏ အာရုံ ဖြစ်နိုင်သော")
W("2", "^2-U26", "apacayagāmi", "လျော့ပါးခြင်းဆီသို့ ဦးတည်သော")
MAGGA_H = {"rūpāvacaro maggo": f"{RUPAVAC} {MAGGA}", "so ca maggo": f"ထို{MAGGA}"}
_NT = alt(NIYY_TOK)


@F.rule(r"(?:(?P<h>" + alt(MAGGA_H) + r") )?(?P<l>(?:(?:" + _NT + r") )*(?:" + _NT + r"))")
def _r_niyy(m):
    toks = re.findall(_NT, m["l"])
    if " ".join(toks) != m["l"]:
        return None
    items = [NIYY[NIYY_TOK[t][0]][NIYY_TOK[t][1]] for t in toks]
    pre = (f"{MAGGA_H[m['h']]}သည် " if m["h"] else "") + "၊ ".join(items) + f" {MAGGA}"
    return V(pre)


SENT_X["Katamena maggenāti?"] = f"အဘယ် {MAGGA}ဖြင့်နည်း{END}"
SENT_X["Rūpāvacarena maggenāti."] = f"{MAGGA_INS['rūpāvacarena maggena']} ဖြစ်သည်{END}"
SENT_X["Anāgāmimaggenāti."] = f"{MAGGA_INS['anāgāmimaggena']} ဖြစ်သည်{END}"
SENT_X["Sotāpattimaggenāti?"] = f"{MAGGA_OF['sotāpatti']}ဖြင့်လော{END}"
SENT_X["Sakadāgāmimaggenāti?"] = f"{MAGGA_OF['sakadāgāmi']}ဖြင့်လော{END}"
VITARAGA_P = f"ကာမတို့၌ {RAGA} ကင်းသော {PUTHUJJANA}သည် တရားကို {ABHISAMAYA}နှင့် တစ်ပြိုင်နက်"
W("2", "^2-798", "kāmesu vītarāgo", f"ကာမတို့၌ {RAGA} ကင်း")
PROP_X["puthujjano kāmesu vītarāgo saha dhammābhisamayā anāgāmiphale saṇṭhāti"] = VV(
    f"{VITARAGA_P} {LOC['anāgāmiphale']}", SANTHATI)
PROP_X["arahatte saṇṭhāti"] = VV(LOC["arahatte"], SANTHATI)
PROP_X["apubbaṃ acarimaṃ tayo magge bhāveti"] = VV(f"{APUBBA} {MAGGA} သုံးပါးတို့ကို", "ပွားများ")
SAMANNA = W("2", "^2-818", "sāmaññaphalāni", "ရဟန်းအဖြစ်၏ ဖိုလ်")
PROP_X["apubbaṃ acarimaṃ tīṇi sāmaññaphalāni sacchikaroti"] = VV(f"{APUBBA} {SAMANNA} သုံးပါးတို့ကို", SACCHIKAROTI)
TEN3 = ["တွေ့ထိမှု", "ခံစားမှု", "မှတ်သိမှု", "စေ့ဆော်မှု", "စိတ်", "ယုံကြည်မှု", "ဝီရိယ", "သတိ", "သမာဓိ", "ပညာ"]
W("2", "^2-978", "satta phassā, satta vedanā, satta saññā, satta cetanā, satta cittāni",
  "တွေ့ထိမှု ခုနစ်ပါး၊ ခံစားမှု ခုနစ်ပါး၊ မှတ်သိမှု ခုနစ်ပါး၊ စေ့ဆော်မှု ခုနစ်ပါး၊ စိတ် ခုနစ်ပါး")
PROP_X["tiṇṇaṃ phassānaṃ tissannaṃ vedanānaṃ tissannaṃ saññānaṃ tissannaṃ cetanānaṃ tiṇṇaṃ cittānaṃ tissannaṃ "
       "saddhānaṃ tiṇṇaṃ vīriyānaṃ tissannaṃ satīnaṃ tiṇṇaṃ samādhīnaṃ tissannaṃ paññānaṃ samodhānaṃ hoti"] = V(
    "၊ ".join(f"{x} သုံးပါး" for x in TEN3) + "တို့၏ ပေါင်းဆုံခြင်း")
PROP_X["tiṇṇaṃ saṃyojanānaṃ pahānā sotāpattiphalaṃ vuttaṃ bhagavatā"] = Cl(
    f"{SAMYOJANA} သုံးပါးတို့ကို ပယ်ခြင်းကြောင့် {FRUIT['sotāpatti']} ဖြစ်သည်ဟု {BHAGAVA}", "ဟောတော်မူ", "မဟောတော်မူ")
PROP_X["kāmarāgabyāpādānaṃ tanubhāvā sakadāgāmiphalaṃ vuttaṃ bhagavatā"] = Cl(
    f"{KB}တို့ ပါးလျခြင်းကြောင့် {FRUIT['sakadāgāmi']} ဖြစ်သည်ဟု {BHAGAVA}", "ဟောတော်မူ", "မဟောတော်မူ")
PROP_X["ye keci dhammaṃ abhisamenti, sabbe te saha dhammābhisamayā anāgāmiphale saṇṭhahanti"] = VV(
    f"တရားကို ထင်ထင်ရှားရှား သိမြင်ကြသူ မည်သူမဆို၊ ထိုသူ အားလုံးတို့သည် တရားကို {ABHISAMAYA}နှင့် တစ်ပြိုင်နက် "
    f"{LOC['anāgāmiphale']}", SANTHATI + "ကြ")
LINES_X["Ahesuṃ te atītaṃse, cha satthāro yasassino;"] = "“အတိတ်ကာလ၌ ကျော်ကြားသော ဆရာ ခြောက်ယောက်တို့ ⟦0⟧ ရှိခဲ့ကြ၏၊"
NIRAMA = "ကိလေသာ အပုပ်နံ့ ကင်းကြ၍ ကရုဏာ၌ စိတ်ညွှတ်ကြ"
LINES_X["Nirāmagandhā karuṇedhimuttā, kāmasaṃyojanātigā."] = f"ထိုဆရာတို့သည် {NIRAMA} ⟦0⟧၊ ကာမ {SAMYOJANA}ကို ကျော်လွန်ကြ၏၊"
BRAHMALOKA = W("1", "^1-1289", "brahmalokaṃ", "ဗြဟ္မာ့ပြည်")
LINES_X["Kāmarāgaṃ virājetvā, brahmalokūpagā ahu;"] = f"“{KAMARAGA}ကို ကင်းစေ၍ {BRAHMALOKA}သို့ ရောက်ကြ၏၊"
LINES_X["Ahesuṃ sāvakā tesaṃ, anekāni satānipi."] = "ထိုဆရာတို့၏ တပည့်တို့သည်လည်း ရာပေါင်း များစွာ ရှိခဲ့ကြ၏၊"
LINES_X["Nirāmagandhā karuṇedhimuttā, kāmasaṃyojanātigā;"] = f"“{NIRAMA}၊ ကာမ {SAMYOJANA}ကို ကျော်လွန်ကြ၏၊"
LINES_X["Kāmarāgaṃ virājetvā, brahmalokūpagā ahūti."] = f"{KAMARAGA}ကို ကင်းစေ၍ {BRAHMALOKA}သို့ ရောက်ကြ၏” ⟦0⟧{END}"
SUNETTA = (
    "ရဟန်းတို့၊ ထိုသုနေတ္တ ဆရာသည် ဤသို့ အသက် ရှည်လျက်၊ ဤသို့ ကြာမြင့်စွာ တည်နေလျက်ပင် မွေးဖွားခြင်း၊ အိုခြင်း၊ "
    "သေခြင်း၊ စိုးရိမ်ခြင်းတို့၊ ငိုကြွေးခြင်းတို့၊ ကိုယ်ဆင်းရဲခြင်းတို့၊ စိတ်ဆင်းရဲမှုတို့၊ ပြင်းစွာ ပူပန်ခြင်းတို့မှ "
    "မလွတ်မြောက်ခဲ့၊ ဒုက္ခမှ မလွတ်မြောက်ခဲ့ဟု ငါ ဆို၏။ ထိုသို့ ဖြစ်ခြင်းသည် အဘယ်ကြောင့်နည်း။ တရား လေးပါးတို့ကို "
    "အစဉ်အတိုင်း မသိခြင်း၊ ထိုးထွင်း မသိမြင်ခြင်းကြောင့် ဖြစ်၏။ အဘယ် လေးပါးတို့ကိုနည်း။ အရိယာ သီလကို အစဉ်အတိုင်း "
    "မသိခြင်း၊ ထိုးထွင်း မသိမြင်ခြင်းကြောင့်၊ အရိယာ သမာဓိကို၊ အရိယာ ပညာကို၊ အရိယာ လွတ်မြောက်မှုကို အစဉ်အတိုင်း "
    "မသိခြင်း၊ ထိုးထွင်း မသိမြင်ခြင်းကြောင့် ဖြစ်၏။ ရဟန်းတို့၊ ထိုအရိယာ သီလကို အစဉ်အတိုင်း သိပြီး၊ ထိုးထွင်း သိမြင်ပြီး၊ "
    "အရိယာ သမာဓိကို အစဉ်အတိုင်း သိပြီး၊ ထိုးထွင်း သိမြင်ပြီး၊ အရိယာ ပညာကို အစဉ်အတိုင်း သိပြီး၊ ထိုးထွင်း သိမြင်ပြီး၊ "
    "အရိယာ လွတ်မြောက်မှုကို အစဉ်အတိုင်း သိပြီး၊ ထိုးထွင်း သိမြင်ပြီး ဖြစ်၏၊ ဘဝကို တပ်မက်မှုကို ဖြတ်ပြီး၊ "
    "ဘဝသို့ ဆောင်သော ကြိုးသည် ကုန်ပြီ၊ ယခုအခါ ဘဝသစ် မရှိတော့ပြီဟူ၍။")
W("1", "^1-M2-110", "bhavataṇhā", "ဘဝကို တပ်မက်မှု")
_L125 = ("Jahati puthujjano kāmarāgabyāpādanti? Āmantā. Nanu vuttaṃ bhagavatā – so hi nāma, bhikkhave, sunetto satthā "
         "evaṃ dīghāyuko samāno evaṃ ciraṭṭhitiko aparimutto ahosi jātiyā jarāya maraṇena sokehi paridevehi dukkhehi "
         "domanassehi upāyāsehi aparimutto dukkhasmāti vadāmi. Taṃ kissa hetu? Catunnaṃ dhammānaṃ ananubodhā "
         "appaṭivedhā. Katamesaṃ catunnaṃ? Ariyassa sīlassa ananubodhā appaṭivedhā, ariyassa samādhissa, ariyāya "
         "paññāya, ariyāya vimuttiyā ananubodhā appaṭivedhā. Tayidaṃ, bhikkhave, ariyaṃ sīlaṃ anubuddhaṃ paṭividdhaṃ, "
         "ariyo samādhi anubuddho paṭividdho, ariyā paññā anubuddhā paṭividdhā, ariyā vimutti anubuddhā paṭividdhā, "
         "ucchinnā bhavataṇhā, khīṇā bhavanetti, natthi dāni punabbhavoti.")


def _late_l125():
    first = F.unit_my("Jahati puthujjano kāmarāgabyāpādanti?")
    LINES_X[_L125] = f"{first} {F.YES}{END} {BHAGAVA} ဤသို့ ဟောတော်မူသည် မဟုတ်လော – “{SUNETTA}"
    F.LINES[_L125] = LINES_X[_L125]


LATE.append(_late_l125)
LINES_X["Sīlaṃ samādhi paññā ca, vimutti ca anuttarā;"] = "“သီလ၊ သမာဓိ၊ ပညာနှင့် အမြတ်ဆုံး လွတ်မြောက်မှု၊"
LINES_X["Anubuddhā ime dhammā, gotamena yasassinā."] = (
    "ဤတရားတို့ကို ကျော်ကြားတော်မူသော ဂေါတမ ဘုရားရှင်သည် အစဉ်အတိုင်း သိတော်မူခဲ့၏။")
LINES_X["Iti buddho abhiññāya, dhammamakkhāsi bhikkhunaṃ;"] = (
    "“ဤသို့ ဘုရားရှင်သည် ထူးကဲစွာ သိ၍ ရဟန်းတို့အား တရားကို ဟောကြားတော်မူ၏၊")
LINES_X["Dukkhassantakaro satthā, cakkhumā parinibbutoti."] = (
    f"{F.DUKKHA_END}တော်မူသော၊ မျက်စိ ရှိတော်မူသော ဆရာသည် {PARINIBB}တော်မူပြီ” ⟦0⟧{END}")


# ===================================================================================== Sabbamatthītikathā (^5-282 … ^5-296)
ALL = new("sabbaṃ (everything)", "အရာအားလုံး")
PROP_X["sabbamatthi"] = V(ALL, "ရှိ")
PROP_X["sabbattha sabbamatthi"] = V(f"{F.WHERE['sabbattha']} {ALL}", "ရှိ")
PROP_X["sabbadā sabbamatthi"] = V(f"{F.WHERE['sabbadā']} {ALL}", "ရှိ")
PROP_X["sabbena sabbaṃ sabbamatthi"] = V(f"အပြည့်အဝ {ALL}", "ရှိ")
PROP_X["sabbesu sabbamatthi"] = V(f"{F.WHERE['sabbesu']} {ALL}", "ရှိ")
PROP_X["ayoganti katvā sabbamatthi"] = V(f"မဆက်စပ်ဟု မှတ်ယူ၍ {ALL}", "ရှိ")
PROP_X["yampi natthi, tampatthi"] = V("အကြင် အရာ မရှိ၏၊ ထိုအရာသည်လည်း", "ရှိ")
PROP_X["sabbamatthīti yā diṭṭhi sā diṭṭhi micchādiṭṭhi"] = V(
    f"{ALL} ရှိသည်ဟူသော အကြင် အယူ ရှိ၏၊ ထိုအယူသည် {MICCHADITTHI}")
PROP_X["yā diṭṭhi sā diṭṭhi sammādiṭṭhi"] = V(f"ထိုအယူသည်ပင် {SAMMADITTHI}")
PROP_X["hevamatthi"] = V("ဤသို့လည်း", "ရှိ")
TIME = {"atīt": "အတိတ်", "anāgat": "အနာဂတ်", "paccuppann": "ပစ္စုပ္ပန်"}
W("1", "^1-M1-18", "atītā dhammā", "အတိတ်")
W("1", "^1-M1-18", "anāgatā dhammā", "အနာဂတ်")
W("1", "^1-M1-18", "paccuppannā dhammā", "ပစ္စုပ္ပန်")
EXIST = {"rūpā": "အဆင်းအရောင်တို့", "saddā": "အသံတို့", "gandhā": "အနံ့တို့", "rasā": "အရသာတို့",
         "phoṭṭhabbā": "အထိအတွေ့တို့", "dhammā": "သဘောတရားတို့", "āloko": "အလင်း", "manasikāro": "နှလုံးသွင်းခြင်း",
         "ākāso": "ဟင်းလင်းပြင်", "vāyo": "လေ", "āpo": "ရေ", "tejo": "မီး", "pathavī": "မြေ", "vatthuṃ": "မှီရာ ဝတ္ထု",
         "cakkhuṃ": "မျက်စိ", "sotaṃ": "နား", "ghānaṃ": "နှာခေါင်း", "jivhā": "လျှာ", "kāyo": F.KAYA, "mano": "မနော",
         "ñāṇaṃ": "ဉာဏ်", "hatthā": "လက်တို့", "pādā": "ခြေတို့", "pabbā": "အဆစ်တို့", "kucchi": "ဝမ်း",
         "rājā cakkavattī": "စကြဝတေး မင်း", "sammāsambuddho": SAMMASAMB, "sammāsammuddho": SAMMASAMB,
         "pañcakkhandhā": f"{F.KHANDHA_W} ငါးပါး", "dvādasāyatanāni": f"{F.AYATANA_W} ဆယ့်နှစ်ပါး",
         "aṭṭhārasa dhātuyo": f"{F.DHATU_W} ဆယ့်ရှစ်ပါး", "bāvīsatindriyāni": f"{INDRIYA_W} နှစ်ဆယ့်နှစ်ပါး"}
for _p, _m in F._KH.items():
    EXIST[_p] = _m
for _p, _m in F._DH.items():
    if _p.endswith("viññāṇadhātu"):
        EXIST[_p[:-5] + "ṃ"] = _m[:-len(" ဓာတ်")]                 # cakkhuviññāṇaṃ = «မျက်စိ သိစိတ်»
EXIST.update({"cakkhāyatanaṃ": F._AY["cakkhāyatanaṃ"], "cakkhudhātu": F._DH["cakkhudhātu"],
              "cakkhundriyaṃ": F._IN["cakkhundriyaṃ"], "vedanā": F.VEDANA.my, "saññā": F.SANNA.my,
              "saṅkhārā": F.SANKHARA.my, "viññāṇaṃ": F.VINNANA.my, "rūpaṃ": F.RUPA.my})
EXIST.update({k: v for k, v in KIL.items()})
for _x in ("Rūpā", "Saddā", "Gandhā", "Rasā"):
    W("2", "^2-154", _x + " aniccā", EXIST[_x.lower()])
W("2", "^2-154", "Phoṭṭhabbā aniccā", "အထိအတွေ့တို့")
W("1", "^1-M2-106", "adhivacanapathā", "အမည်ခေါ်ဝေါ်မှု၏ လမ်းကြောင်း")
W("2", "^2-809", "rājāno cakkavattī", "စကြဝတေး မင်း")
TIME_RX = r"(?:(?P<t>atīt|anāgat|paccuppann)(?:aṃ|ā|o|āni) )?"


def np_my(x):
    """A noun phrase with an optional time adjective: «atītā vedanā» = «အတိတ် ခံစားမှု»."""
    m = re.fullmatch(r"(atīt|anāgat|paccuppann)(?:aṃ|ā|o|āni)(?: (.+))?", x)
    if m:
        t = TIME[m[1]]
        if m[2] is None:
            return t
        return f"{t} {EXIST[m[2]]}" if m[2] in EXIST else None
    return EXIST.get(x)


def _exist(m):
    s_ = m.string
    if ", " in s_ or "…" in s_ or ";" in s_:
        return None
    g = None
    for k in sorted(GEN, key=len, reverse=True):
        if s_.startswith(k + " "):
            g, s_ = k, s_[len(k) + 1:]
            break
    if not s_.endswith(" atthi"):
        return None
    parts = s_[:-len(" atthi")].split(" atthi ")
    my = [np_my(x) for x in parts]
    if None in my:
        return None
    pre = (f"{GEN[g]}၌ " if g else "") + "".join(f"{x} ရှိ၏၊ " for x in my[:-1]) + my[-1]
    return V(pre, "ရှိ")


F.RULES.append((re.compile(r".+ atthi"), _exist))
NV = {"nvatthi": "မရှိ"}
PROP_X["atītaṃ nvatthi"] = V(TIME["atīt"], "ရှိ", True)
PROP_X["anāgataṃ nvatthi"] = V(TIME["anāgat"], "ရှိ", True)
EXISTING = "ရှိသော အရာ"
for _t, _pl in (("atīt", "atītaṃ"), ("anāgat", "anāgataṃ"), ("paccuppann", "paccuppannaṃ")):
    PROP_X[f"atthi {_pl}"] = V(f"{EXISTING}သည် {TIME[_t]}")
PROP_X["atthi nibbānaṃ"] = V(f"{EXISTING}သည် {F.NIBBANA}")
PROP_X["atthi nvātītaṃ"] = V(f"{EXISTING}သည် {TIME['atīt']}", neg=True)
PROP_X["atthi nvānāgataṃ"] = V(f"{EXISTING}သည် {TIME['anāgat']}", neg=True)


@frame(r"Hañci (?P<alt>vā pana )?(?P<p>[^,]+), (?P<q>[^,]+?)ti micchā\.")
def _f_if_miccha(m):
    """Hañci P, Q-ti micchā. (^5-288)"""
    pre = "သို့မဟုတ် အကယ်၍" if m["alt"] else "အကယ်၍"
    return f"{pre} {F.pq(m['p'], 'cond')} {F.pq(m['q'], 'stmt')} ဟူသည် မှားသည်{END}"


# ---- the participle lists (ceased / not ceased, born / not born)
CEASE = [("niruddhaṃ", "ချုပ်ငြိမ်း"), ("vigataṃ", "ကင်းကွာ"), ("vipariṇataṃ", "ဖောက်ပြန်ပြောင်းလဲ"),
         ("atthaṅgataṃ", "ကွယ်"), ("abbhatthaṅgataṃ", "လုံးဝ ကွယ်")]
BORN = [("jātaṃ", "ဖြစ်"), ("bhūtaṃ", "ဖြစ်တည်"), ("sañjātaṃ", "ဖြစ်ပေါ်"), ("nibbattaṃ", "ဖြစ်မြောက်"),
        ("abhinibbattaṃ", "ထင်ရှားစွာ ဖြစ်မြောက်"), ("pātubhūtaṃ", "ထင်ရှား ပေါ်ပေါက်")]
PART = {}
for _set in (CEASE, BORN):
    for _p, _m in _set:
        PART[_p] = (_m + "ပြီး", len(_set))
        _neg = ("na " + _p) if _p in ("atthaṅgataṃ", "abbhatthaṅgataṃ") else ("an" + _p if _p[0] in "aā" and False
                                                                                else None)
        _np = {"niruddhaṃ": "aniruddhaṃ", "vigataṃ": "avigataṃ", "vipariṇataṃ": "avipariṇataṃ",
               "atthaṅgataṃ": "na atthaṅgataṃ", "abbhatthaṅgataṃ": "na abbhatthaṅgataṃ", "jātaṃ": "ajātaṃ",
               "bhūtaṃ": "abhūtaṃ", "sañjātaṃ": "asañjātaṃ", "nibbattaṃ": "anibbattaṃ",
               "abhinibbattaṃ": "anabhinibbattaṃ", "pātubhūtaṃ": "apātubhūtaṃ"}[_p]
        _w = _m.rsplit(" ", 1)
        PART[_np] = ((_w[0] + " မ" + _w[1] if len(_w) == 2 else "မ" + _m) + "သေး", len(_set))
_PX = "|".join(re.escape(k) for k in sorted(PART, key=len, reverse=True))
SUBJ_RX = r"(?P<s>(?:atīt|anāgat|paccuppann)aṃ(?: rūpaṃ| viññāṇaṃ)?)(?P<a> atthi (?:atīt|anāgat|paccuppann)aṃ(?: rūpaṃ| viññāṇaṃ)?)?"


@F.rule(r"(?:" + SUBJ_RX + r" )?(?P<l>(?:(?:" + _PX + r") )*(?:" + _PX + r"))")
def _r_part(m):
    toks = re.findall(_PX, m["l"])
    if " ".join(toks) != m["l"]:
        return None
    items = [PART[t][0] for t in toks]
    full = len(toks) == PART[toks[0]][1]
    subj = ""
    if m["s"]:
        sm = np_my(m["s"])
        subj = f"{sm} ရှိ၍ ထို{sm}သည် " if m["a"] else f"{sm}သည် "
    if m["s"] and not full:
        return FR(subj + "၊ ".join(items))
    return V(subj + "၊ ".join(items) + "သော အရာ")


# ---- Kālasaṃsandanā: synonyms and the nature that is not given up
PAC_RUPA = f"{TIME['paccuppann']} {F.RUPA.my}"
SYN_TAIL = "ဟူသော စကားကို ဦးစားမပေးဘဲ ဤစကားတို့သည် အနက် တူသော၊ ညီမျှသော၊ အချိုး တူသော၊ တစ်မျိုးတည်းမှ ဖြစ်သော စကားတို့"
for _a, _b, _am, _bm in (("paccuppann", "rūp", TIME["paccuppann"], F.RUPA.my), ("odāt", "vatth", "အဖြူ", "အဝတ်")):
    PROP_X[f"{_a}anti vā {_b}anti vā, {_b}anti vā {_a}anti vā {_a}aṃ {_b}aṃ appiyaṃ karitvā esese ekaṭṭhe same "
           "samabhāge tajjāte"] = V(f"«{_am}ဟုဖြစ်စေ၊ {_bm}»ဟုဖြစ်စေ၊ «{_bm}ဟုဖြစ်စေ၊ {_am}»ဟုဖြစ်စေ၊ {_am} {_bm}"
                                   + SYN_TAIL)
BHAVA = {"paccuppanna": TIME["paccuppann"], "rūpa": F.RUPA.my, "odāta": "အဖြူ", "vattha": "အဝတ်",
         "nibbāna": F.NIBBANA, "atīta": TIME["atīt"], "anāgata": TIME["anāgat"]}
BEING = {"nirujjhamānaṃ": "ချုပ်ငြိမ်းနေစဉ်", "rajjamānaṃ": "ဆိုးဆေး ဆိုးနေစဉ်"}
SUBJ2 = {"paccuppannaṃ rūpaṃ": PAC_RUPA, "odātaṃ vatthaṃ": "အဖြူ အဝတ်", "rūpaṃ": F.RUPA.my, "nibbānaṃ": F.NIBBANA}


def subj_my(x):
    """«X» / «X atthi X» -> «Xသည်» / «X ရှိ၍ ထိုXသည်»."""
    m = re.fullmatch(r"(.+?) atthi (.+)", x)
    if m and m[1] == m[2]:
        n = np_my(m[1]) or (F.NIBBANA if m[1] == "nibbānaṃ" else None)
        return f"{n} ရှိ၍ ထို{n}သည်" if n else None
    n = SUBJ2.get(x) or np_my(x)
    return f"{n}သည်" if n else None


@F.rule(r"(?:(?P<s>.+?) (?:(?P<b2>nirujjhamānaṃ|rajjamānaṃ) )?)?(?P<x>\S+)bhāvaṃ (?P<n>na )?jahati")
def _r_bhava(m):
    if m["x"] not in BHAVA:
        return None
    subj = ""
    if m["s"]:
        subj = subj_my(m["s"])
        if subj is None:
            return None
        subj += " " + (BEING[m["b2"]] + " " if m["b2"] else "")
    return VV(f"{subj}{BHAVA[m['x']]} ဖြစ်ခြင်းကို", JAHATI, bool(m["n"]))


NICCA = f"မြဲသော၊ ခိုင်ခံ့သော၊ {F.SASSATA}သော၊ ဖောက်ပြန်ပြောင်းလဲတတ်သော သဘော မရှိသော"   # as make_sample NICCA
ANICCA4 = new("aniccaṃ adhuvaṃ asassataṃ vipariṇāmadhammaṃ",
              f"မမြဲသော၊ မခိုင်ခံ့သော၊ {F.ASASSATA}သော၊ ဖောက်ပြန်ပြောင်းလဲတတ်သော သဘော ရှိသော")
W("2", "^2-943", "vipariṇāmadhammā", "ဖောက်ပြန်ပြောင်းလဲတတ်သော သဘော")


@F.rule(r"(?P<s>.+?) (?P<k>niccaṃ dhuvaṃ sassataṃ avipariṇāmadhammaṃ|aniccaṃ adhuvaṃ asassataṃ vipariṇāmadhammaṃ)")
def _r_nicca(m):
    if " jahati" in m["s"] or "jahatīti" in m["s"]:
        return None
    subj = subj_my(m["s"])
    if subj is None:
        return None
    return V(f"{subj} {NICCA if m['k'].startswith('nicca') else ANICCA4} အရာ")


@F.rule(r"(?P<a>.+? na jahat)(?P<ti>īti|i) (?P<b>\S+(?: \S+)? (?:niccaṃ dhuvaṃ sassataṃ avipariṇāmadhammaṃ|aniccaṃ adhuvaṃ "
        r"asassataṃ vipariṇāmadhammaṃ))")
def _r_jahati_nicca(m):
    a, b = F.lookup(m["a"] + "i"), F.lookup(m["b"])
    if not a or not b:
        return None
    a, b = a[0], b[0]
    return Cl(f"{a.f('stmt')}{'ဟူ၍' if m['ti'] == 'īti' else C} {b.pre}", b.v, b.nv, b.neg)


@frame(r"nanu (?P<p>.+?)ti\?")
def _f_nanu_low(m):
    """nanu P-ti? after «…pe… » (a small letter)."""
    return F.pq(m["p"], "nanu") + END


ANCHOR_X["jahatīti"] = f"မ{JAHATI}ဟူ၍"
ANCHOR_X["jahati"] = f"မ{JAHATI}"

# ---- Vacanasodhanā (^5-288)
for _a, _b in (("anāgat", "paccuppann"), ("paccuppann", "atīt")):
    PROP_X[f"{_a}aṃ hutvā {_b}aṃ hoti"] = V(f"{TIME[_a]} ဖြစ်ပြီးမှ {TIME[_b]}")
    PROP_X[f"taññeva {_a}aṃ taṃ {_b}aṃ"] = V(f"ထို{TIME[_a]}သည်ပင် ထို{TIME[_b]}")
PROP_X["taññeva anāgataṃ taṃ paccuppannaṃ taṃ atītaṃ"] = V(
    f"ထို{TIME['anāgat']}သည်ပင် ထို{TIME['paccuppann']}၊ ထို{TIME['atīt']}")
PROP_X["hutvā hoti hutvā hoti"] = V("ဖြစ်ပြီးမှ ဖြစ်၏၊ ဖြစ်ပြီးမှ")
PROP_X["na hutvā na hoti na hutvā na hoti"] = Cl("မဖြစ်ခဲ့ဘဲ မဖြစ်၊ မဖြစ်ခဲ့ဘဲ", "ဖြစ်", "မဖြစ်", True)

# ---- Atītacakkhurūpādi (^5-289): seeing with a past eye
ORGAN = {"cakkhunā": "မျက်စိ", "sotena": "နား", "ghānena": "နှာခေါင်း", "jivhāya": "လျှာ", "kāyena": F.KAYA,
         "manena": "မနော"}
OBJ = {"rūpaṃ": "အဆင်းအရောင်", "saddaṃ": "အသံ", "gandhaṃ": "အနံ့", "rasaṃ": "အရသာ", "phoṭṭhabbaṃ": "အထိအတွေ့",
       "dhammaṃ": "သဘောတရား"}
SEE = {"passati": "မြင်", "suṇāti": "ကြား", "ghāyati": "အနံ့ ခံ", "sāyati": "အရသာ ခံ", "phusati": "ထိ",
       "vijānāti": "သိ"}                                              # as make_sample SEE


@F.rule(r"(?P<n>na ca )?(?P<t>atīt|anāgat|paccuppann)(?:ena|āya) (?P<o>" + alt(ORGAN) + r") (?:atīt|anāgat|paccuppann)aṃ"
        r" (?P<x>" + alt(OBJ) + r") (?P<v>" + alt(SEE) + r")")
def _r_see(m):
    t = TIME[m["t"]]
    return VV(f"{t} {ORGAN[m['o']]}ဖြင့် {t} {OBJ[m['x']]}ကို", SEE[m["v"]], bool(m["n"]))


@F.rule(r"(?P<a>.+? atthi), (?P<b>(?:na ca )?(?:atīt|anāgat|paccuppann)(?:ena|āya) .+)")
def _r_exist_see(m):
    a, b = F.lookup(m["a"]), F.lookup(m["b"])
    if not a or not b:
        return None
    return Cl(f"{a[0].f('stmt')}{C} {b[0].pre}", b[0].v, b[0].nv, b[0].neg)


# ---- Atītañāṇādi (^5-290)
KICCA = "ပြုဖွယ် ကိစ္စ"
PROP_X["tena ñāṇena ñāṇakaraṇīyaṃ karoti"] = VV(f"ထိုဉာဏ်ဖြင့် ဉာဏ်၏ {KICCA}ကို", "ပြု")
PROP_X["na ca tena ñāṇena ñāṇakaraṇīyaṃ karoti"] = VV(f"ထိုဉာဏ်ဖြင့်ကား ဉာဏ်၏ {KICCA}ကို", "ပြု", True)
PROP_X["tena ñāṇena dukkhaṃ parijānāti"] = VV(f"ထိုဉာဏ်ဖြင့် {DUKKHA}ကို", "ပိုင်းခြား သိ")
PROP_X["samudayaṃ pajahati"] = VV(f"{SAMUDAYA}ကို", "ပယ်")
PROP_X["nirodhaṃ sacchikaroti"] = VV(f"{NIRODHA}ကို", SACCHIKAROTI)
PROP_X["maggaṃ bhāveti"] = VV(f"{MAGGA}ကို", "ပွားများ")
PROP_X["na ca tena ñāṇena dukkhaṃ parijānāti, samudayaṃ pajahati, nirodhaṃ sacchikaroti, maggaṃ bhāveti"] = VV(
    f"ထိုဉာဏ်ဖြင့်ကား {DUKKHA}ကို ပိုင်းခြား သိခြင်း၊ {SAMUDAYA}ကို ပယ်ခြင်း၊ {NIRODHA}ကို {SACCHIKAROTI}ခြင်း၊ "
    f"{MAGGA}ကို ပွားများခြင်းကို", "ပြု", True)

# ---- Arahantādi (^5-291 … ^5-292)
KILI = {"rāgena": RAGA, "dosena": DOSA, "mohena": MOHA, "mānena": MANA, "diṭṭhiyā": DITTHI,
        "vicikicchāya": VICIKICCHA, "thinena": THINA, "uddhaccena": UDDHACCA, "ahirikena": AHIRIKA,
        "anottappena": ANOTTAPPA, "byāpādena": BYAPADA}
HAS = {"sarāgo": f"{RAGA} ရှိသူ", "sadoso": f"{DOSA} ရှိသူ", "samoho": f"{MOHA} ရှိသူ", "samāno": f"{MANA} ရှိသူ",
       "sadiṭṭhiko": f"{DITTHI} ရှိသူ", "savicikiccho": f"{VICIKICCHA} ရှိသူ", "sathino": f"{THINA} ရှိသူ",
       "sauddhacco": f"{UDDHACCA} ရှိသူ", "saahiriko": f"{AHIRIKA} ရှိသူ", "saanottappī": f"{ANOTTAPPA} ရှိသူ",
       "anottappī": "ဒုစရိုက်ကို မကြောက်ရွံ့သူ", "byāpannacitto": BYAPANNA}


@F.rule(r"(?P<n>na ca )?(?P<p>arahā|anāgāmī|sakadāgāmī|sotāpanno|puthujjano) (?:tena|tāya) (?P<k>" + alt(KILI) + r") "
        r"(?P<h>" + alt(HAS) + r")")
def _r_has(m):
    return V(f"{PERS[m['p']]}သည် ထို{KILI[m['k']]}ကြောင့် {HAS[m['h']]}", neg=bool(m["n"]))


@F.rule(r"(?P<a>.+? atthi),? (?P<b>(?:na ca )?(?:arahā|anāgāmī|sakadāgāmī|sotāpanno|puthujjano) (?:tena|tāya) .+)")
def _r_exist_has(m):
    a, b = F.lookup(m["a"]), F.lookup(m["b"])
    if not a or not b:
        return None
    return Cl(f"{a[0].f('stmt')}{C} {b[0].pre}", b[0].v, b[0].nv, b[0].neg)


# ---- Atītahatthādi (^5-293)
SATI = {"atītesu hatthesu": ("အတိတ် လက်တို့", "ယူခြင်း ချခြင်း", "ādānanikkhepanaṃ"),
        "atītesu pādesu": ("အတိတ် ခြေတို့", "ရှေ့သို့ တက်ခြင်း နောက်သို့ ဆုတ်ခြင်း", "abhikkamapaṭikkamo"),
        "atītesu pabbesu": ("အတိတ် အဆစ်တို့", "ကွေးခြင်း ဆန့်ခြင်း", "samiñjanapasāraṇaṃ"),
        "atītasmiṃ kucchismiṃ": ("အတိတ် ဝမ်း", "ဆာလောင်ခြင်း ရေငတ်ခြင်း", "jighacchā pipāsā")}
for _k, (_a, _b, _c) in SATI.items():
    PROP_X[f"{_k} sati {_c} paññāyati"] = VV(f"{_a} ရှိနေသောအခါ {_b}", "ထင်ရှား")
PROP_X["atīto kāyo paggahaniggahupago chedanabhedanupago kākehi gijjhehi kulalehi sādhāraṇo"] = V(
    f"အတိတ် {F.KAYA}သည် ချီးမြှောက်ခြင်း နှိပ်ကွပ်ခြင်းကို ခံရနိုင်သော၊ ဖြတ်ခြင်း ခွဲခြင်းကို ခံရနိုင်သော၊ "
    "ကျီးတို့၊ လင်းတတို့၊ စွန်တို့နှင့် ဆက်ဆံရသော အရာ")
PROP_X["atīte kāye visaṃ kameyya"] = VV(f"အတိတ် {F.KAYA}၌ အဆိပ်", "ထိရောက်နိုင်")
PROP_X["satthaṃ kameyya"] = VV("လက်နက်", "ထိရောက်နိုင်")
PROP_X["aggi kameyya"] = VV("မီး", "ထိရောက်နိုင်")
_BAND = ["ခြေချင်း", "ကြိုး", "သံကြိုး", "ရွာ", "နိဂုံး", "မြို့", "ဇနပုဒ်"]
PROP_X["labbhā atīto kāyo addubandhanena bandhituṃ, rajjubandhanena bandhituṃ, saṅkhalikabandhanena bandhituṃ, "
       "gāmabandhanena bandhituṃ, nigamabandhanena bandhituṃ, nagarabandhanena bandhituṃ, janapadabandhanena "
       "bandhituṃ, kaṇṭhapañcamehi bandhanehi bandhituṃ"] = VV(
    f"အတိတ် {F.KAYA}ကို " + "၊ ".join(f"{x} အနှောင်ဖြင့် နှောင်ဖွဲ့ခြင်း" for x in _BAND)
    + f"၊ လည်ပင်းကို {F.ORD_MY[5]} ပြုသော အနှောင်တို့ဖြင့် နှောင်ဖွဲ့ခြင်းကို", "ပြုနိုင်")
for _k, _v in (("āpena āpakaraṇīyaṃ", "ရေ"), ("tejena tejakaraṇīyaṃ", "မီး"), ("vāyena vāyakaraṇīyaṃ", "လေ")):
    PROP_X[f"tena {_k} karoti"] = VV(f"ထို{_v}ဖြင့် {_v}၏ {KICCA}ကို", "ပြု")

# ---- Atītakkhandhādisamodhāna (^5-294)
COUNTS = {"tayo rūpakkhandhā": f"{F._KH['rūpakkhandho']} သုံးပါး", "pannarasakkhandhā": f"{F.KHANDHA_W} ဆယ့်ငါးပါး",
          "tīṇi cakkhāyatanāni": f"{F._AY['cakkhāyatanaṃ']} သုံးပါး",
          "chattiṃsāyatanāni": f"{F.AYATANA_W} သုံးဆယ့်ခြောက်ပါး", "tisso cakkhudhātuyo": f"{F._DH['cakkhudhātu']} သုံးပါး",
          "catupaññāsa dhātuyo": f"{F.DHATU_W} ငါးဆယ့်လေးပါး", "tīṇi cakkhundriyāni": f"{F._IN['cakkhundriyaṃ']} သုံးပါး",
          "chasaṭṭhindriyāni": f"{INDRIYA_W} ခြောက်ဆယ့်ခြောက်ပါး"}
for _k, _v in COUNTS.items():
    PROP_X[_k] = V(_v)
PROP_X["tiṇṇannaṃ rājūnaṃ cakkavattīnaṃ sammukhībhāvo hoti"] = V("စကြဝတေး မင်း သုံးပါးတို့၏ မျက်မှောက် ဆုံဆည်းခြင်း")
PROP_X["tiṇṇannaṃ sammāsambuddhānaṃ sammukhībhāvo hoti"] = V(f"{SAMMASAMB} သုံးပါးတို့၏ မျက်မှောက် ဆုံဆည်းခြင်း")

# ---- Padasodhanā (^5-295)
OBJN = {"atītaṃ": TIME["atīt"], "anāgataṃ": TIME["anāgat"], "paccuppannaṃ": TIME["paccuppann"], "nibbānaṃ": F.NIBBANA}
NOT_X = {"atītaṃ": "nvātītaṃ", "anāgataṃ": "nvānāgataṃ", "paccuppannaṃ": "no paccuppannaṃ", "nibbānaṃ": "no nibbānaṃ"}
TENA_X = {"atītaṃ": "tenātītaṃ", "anāgataṃ": "tenānāgataṃ", "paccuppannaṃ": "tena paccuppannaṃ",
          "nibbānaṃ": "tena nibbānaṃ"}
for _x, _m in OBJN.items():
    _n = NOT_X[_x]
    PROP_X[f"atthi siyā {_x}"] = Cl(f"{EXISTING}သည် {_m}", "ဖြစ်နိုင်", "မဖြစ်နိုင်")
    PROP_X[f"{_x} atthi atthi siyā {_x}"] = Cl(f"{_m} ရှိ၏၊ {EXISTING}သည် {_m}", "ဖြစ်နိုင်", "မဖြစ်နိုင်")
    PROP_X[f"siyā {_n}"] = Cl(f"{_m} မဟုတ်သည်လည်း", "ဖြစ်နိုင်", "မဖြစ်နိုင်")
    PROP_X[f"atthi siyā {_x} siyā {_n}"] = Cl(f"{EXISTING}သည် {_m} ဖြစ်နိုင်၏၊ {_m} မဟုတ်သည်လည်း", "ဖြစ်နိုင်",
                                               "မဖြစ်နိုင်")
    PROP_X[f"{_x} atthi atthi siyā {_x} siyā {_n}"] = Cl(
        f"{_m} ရှိ၏၊ {EXISTING}သည် {_m} ဖြစ်နိုင်၏၊ {_m} မဟုတ်သည်လည်း", "ဖြစ်နိုင်", "မဖြစ်နိုင်")
    PROP_X[f"{TENA_X[_x]} {_n}"] = V(f"ထို့ကြောင့် {_m}သည် {_m}", neg=True)
    PROP_X[f"{TENA_X[_x]}, {_n}"] = V(f"ထို့ကြောင့် {_m}သည် {_m}", neg=True)      # source: comma (^5-295)
    PROP_X[f"{_n} {_x}"] = V(f"{_m} မဟုတ်သော အရာသည် {_m}")
    PROP_X[f"{_x} {_n} {_n} {_x}"] = V(f"{_m}သည် {_m} မဟုတ်၊ {_m} မဟုတ်သော အရာသည် {_m}")
    PROP_X[f"{_x} {_n}, {_n} {_x}"] = PROP_X[f"{_x} {_n} {_n} {_x}"]
    PROP_X[f"{_x} atthi"] = V(_m, "ရှိ")
    PROP_X[f"atthi {_x}"] = V(f"{EXISTING}သည် {_m}")


@frame(r"Hañci (?P<p>.+?), (?P<q>ten.+?)ti\.")
def _f_if_tena(m):
    """Hañci P, tena X nvāX, nvāX Xti. (^5-295, no «tena vata re vattabbe»)"""
    return f"အကယ်၍ {F.pq(m['p'], 'cond')} {F.pq(m['q'], 'stmt')}{END}"


@frame(r"No ce pan(?:a |(?=ā))(?P<p>.+?)ti, no ca vata re vattabbe – (?P<q>.+?)ti\.")
def _f_noce(m):
    """No ce pana P-ti, no ca vata re vattabbe – "Q"ti. (^5-295: no «vattabbe –» after «No ce pana»)"""
    p = m["p"]
    if p.startswith("ā"):
        p = "a" + p[1:]                                              # panānāgataṃ = pana anāgataṃ
    return (f"တစ်ဖန် အကယ်၍ {F.pq(p, 'stmt')} ဟူသည် မဟုတ်လျှင် အမှန်ပင် ဤသို့လည်း မဆိုသင့် – "
            f"“{F.pq(m['q'], 'stmt', 1)}”{END}")


def _late_pac():
    SENT_X["Paccuppannaṃ atthīti, āmantā."] = f"{F.pq('paccuppannaṃ atthi', 'q')}{C} {F.YES}{END}"
    F.SENT["Paccuppannaṃ atthīti, āmantā."] = SENT_X["Paccuppannaṃ atthīti, āmantā."]


LATE.append(_late_pac)


PROP_X["vipariṇāmadhammaṃ"] = V("ဖောက်ပြန်ပြောင်းလဲတတ်သော သဘော ရှိသော အရာ")
for _s in ("atītaṃ rūpaṃ", "atītaṃ viññāṇaṃ", "atītaṃ"):
    PROP_X[f"{_s} aniccaṃ"] = FR(f"{np_my(_s)}သည် မမြဲသော")


# ---- the sutta passages of the Suttasādhana (^5-296): units / lines composed from the source
def src_unit(name, start):
    """The engine's key of the sentence of chapter «name» that starts with «start» (quotes and brackets out)."""
    for line in (PALI / name).read_text(encoding="utf-8-sig").splitlines():
        clean = F.BR_RE.sub("", F.strip_id(line).strip())
        for a, b in F.split_sents(clean):
            k = F.norm_pe(F.strip_q(clean[a:b].strip()))
            if k.startswith(start):
                return k
    raise F.Miss("src_unit: " + start)


def src_line(name, start):
    """The engine's key of the whole line of chapter «name» that starts with «start»."""
    for line in (PALI / name).read_text(encoding="utf-8-sig").splitlines():
        k = F.norm_pe(F.strip_q(F.BR_RE.sub("", F.strip_id(line).strip())))
        if k.startswith(start):
            return k
    raise F.Miss("src_line: " + start)


CH5 = "5-sabbamatthitikatha.md"
FORM = W("2", "^2-2", "atītānāgatapaccuppannaṃ ajjhattaṃ vā bahiddhā vā oḷārikaṃ vā sukhumaṃ vā hīnaṃ vā paṇītaṃ vā",
         "အတိတ်ဖြစ်စေ၊ အနာဂတ်ဖြစ်စေ၊ ပစ္စုပ္ပန်ဖြစ်စေ၊ မိမိ၌ ရှိသည်ဖြစ်စေ၊ မိမိ၏ ပြင်ပ၌ ရှိသည်ဖြစ်စေ၊ ရုန့်ရင်းသည်ဖြစ်စေ၊ "
         "နုညံ့သည်ဖြစ်စေ၊ ယုတ်ညံ့သည်ဖြစ်စေ၊ မွန်မြတ်သည်ဖြစ်စေ၊ အဝေး၌ ရှိသည်ဖြစ်စေ၊ အနီး၌ ရှိသည်ဖြစ်စေ")
W("2", "^2-2", "Tattha katamo rūpakkhandho", f"ဤသည်ကို {F._KH['rūpakkhandho']}ဟု ခေါ်သည်")
QUOTE_X["yaṃ kiñci, bhikkhave, rūpaṃ atītānāgatapaccuppannaṃ ajjhattaṃ vā bahiddhā vā oḷārikaṃ vā sukhumaṃ vā hīnaṃ vā "
        "paṇītaṃ vā yaṃ dūre santike vā – ayaṃ vuccati rūpakkhandho. Yā kāci vedanā… yā kāci saññā… ye keci "
        "saṅkhārā… yaṃ kiñci viññāṇaṃ atītānāgatapaccuppannaṃ ajjhattaṃ vā bahiddhā vā oḷārikaṃ vā sukhumaṃ vā hīnaṃ "
        "vā paṇītaṃ vā yaṃ dūre santike vā – ayaṃ vuccati viññāṇakkhandho"] = (
    f"ရဟန်းတို့၊ {FORM} မည်သည့် {F.RUPA.my}မဆို – ဤသည်ကို {F._KH['rūpakkhandho']}ဟု ခေါ်သည်။ မည်သည့် "
    f"{F.VEDANA.my}မဆို… မည်သည့် {F.SANNA.my}မဆို… မည်သည့် {F.SANKHARA.my}မဆို… {FORM} မည်သည့် {F.VINNANA.my}မဆို – "
    f"ဤသည်ကို {F._KH['viññāṇakkhandho']}ဟု ခေါ်သည်")
PATHS = (f"စကားဖြင့် ဖော်ပြမှု၏ လမ်းကြောင်း၊ အမည်ခေါ်ဝေါ်မှု၏ လမ်းကြောင်း၊ {F.PANNATTI}၏ လမ်းကြောင်း")
W("1", "^1-M2-106", "niruttipathā", "စကားဖြင့် ဖော်ပြမှု၏ လမ်းကြောင်း")
W("1", "^1-M2-106", "paññattipathā", f"{F.PANNATTI}၏ လမ်းကြောင်း")
UNMIXED = (f"{PATHS} ဟူသော ဤ သုံးပါးတို့သည် ရောနှောခြင်း မရှိကြ၊ ရှေးကလည်း ရောနှောခြင်း မရှိခဲ့ကြ၊ ယခုလည်း "
           f"မရောနှောကြ၊ နောင်လည်း မရောနှောကြလိမ့်မည်၊ ပညာရှိ ရဟန်း {F.BRAHMANA}တို့ မကန့်ကွက်အပ်ကြ")
SANKHA = {"ahosi": "ရှိခဲ့ပြီ", "atthi": "ရှိ၏", "bhavissati": "ရှိလိမ့်မည်"}


def _three(noun, desc, is_, nots):
    """«Yaṃ … rūpaṃ DESC ‘X’ti tassa saṅkhā, … samaññā, … paññatti; na tassa saṅkhā ‘Y’ti, na tassa saṅkhā ‘Z’ti»."""
    x = SANKHA[is_]
    head = f"{desc}သော အကြင် {noun} ရှိ၏၊ "
    says = "၊ ".join(f"ထို{noun}၏ {w}သည် ‘{x}’ဟူ၍ ဖြစ်၏" for w in ("ရေတွက်ခေါ်ဆိုချက်", "အမည်ပေးချက်", F.PANNATTI))
    nos = "၊ ".join(f"ထို{noun}၏ ရေတွက်ခေါ်ဆိုချက်သည် ‘{SANKHA[y]}’ဟူ၍ မဖြစ်" for y in nots)
    return f"{head}{says}၊ {nos}"


def _para(desc, is_, nots):
    return (f"ရဟန်းတို့၊ {_three(F.RUPA.my, desc, is_, nots)}။ အကြင် {F.VEDANA.my}… အကြင် {F.SANNA.my}… "
            f"အကြင် {F.SANKHARA.my}… {_three(F.VINNANA.my, desc, is_, nots)}")


PAST_D = f"{TIME['atīt']} ဖြစ်၍ " + "၊ ".join(PART[k][0] for k in ("niruddhaṃ", "vigataṃ", "vipariṇataṃ"))
FUT_D = "၊ ".join(PART[k][0] for k in ("ajātaṃ", "apātubhūtaṃ"))
PRES_D = "၊ ".join(PART[k][0] for k in ("jātaṃ", "pātubhūtaṃ"))
VADAMI = "ဟု ငါ ဆို၏"
AHARA_K = W("1", "^1-U1", "kabaḷīkāro āhāro", "လုတ်ပြု၍ စားရသော အာဟာရ")
AHARA3 = W("1", "^1-70", "Phassāhāro, manosañcetanāhāro, viññāṇāhāro", "တွေ့ထိမှု အာဟာရ၊ မနော၏ စေ့ဆော်ခြင်း အာဟာရ၊ သိစိတ် အာဟာရ")
NAMARUPA = W("1", "^1-1343", "nāmarūpaṃ", "စိတ်ပိုင်းနှင့် ရုပ်ပိုင်း")
JJM = W("1", "^1-1343", "jarāmaraṇaṃ sokaparidevadukkhadomanassupāyāsā", "အိုခြင်း၊ သေခြင်း၊ စိုးရိမ်ခြင်း")
LOBHA = W("1", "^1-986", "lobho, doso, moho", "လောဘ")
TANHA = W("1", "^1-1343", "taṇhā", "တပ်မက်မှု")


def _ahara(pos):
    r = "ရှိ" if pos else "မရှိ"
    head = (f"{RAGA} ရှိ၏၊ ပျော်မွေ့မှု ရှိ၏၊ {TANHA} ရှိ၏ ဆိုလျှင် ထိုအာဟာရ၌ {F.VINNANA.my}သည် တည်၍ စည်ပင်၏" if pos else
            f"{RAGA} မရှိ၊ ပျော်မွေ့မှု မရှိ၊ {TANHA} မရှိ ဆိုလျှင် ထိုအာဟာရ၌ {F.VINNANA.my}သည် မတည်၊ မစည်ပင်")
    vin = f"{F.VINNANA.my}သည် တည်၍ စည်ပင်၏" if pos else f"{F.VINNANA.my}သည် မတည်၊ မစည်ပင်"
    chain = [f"{NAMARUPA}၏ သက်ဆင်းခြင်း", f"{F.SANKHARA.my}၏ ကြီးထွားခြင်း", f"နောင်အခါ {PUNABBHAVA} ဖြစ်ပေါ်ခြင်း",
             "နောင်အခါ မွေးဖွားခြင်း၊ အိုခြင်း၊ သေခြင်း"]
    out = [f"ရဟန်းတို့၊ အကယ်၍ {AHARA_K}၌ {head}"]
    prev = vin
    for c in chain:
        out.append(f"အကြင်အရပ်၌ {prev}{'၊' if not pos else ''} ထိုအရပ်၌ {c} {r if not pos else 'ရှိ၏'}"
                   .replace("၏ ထိုအရပ်", "၏၊ ထိုအရပ်"))
        prev = f"{c} {r if not pos else 'ရှိ၏'}"
    tail = ("စိုးရိမ်ခြင်း ရှိသော၊ မြူ ရှိသော ⟦0⟧၊ ပြင်းစွာ ပူပန်ခြင်း ရှိသော" if pos else
            "စိုးရိမ်ခြင်း မရှိသော၊ မြူ မရှိသော၊ ပြင်းစွာ ပူပန်ခြင်း မရှိသော")
    last = f"ရဟန်းတို့၊ အကြင်အရပ်၌ {prev}{'၊' if not pos else '၊'} ထိုအရာကို {tail} အရာ{VADAMI}"
    return "။ ".join(out) + "။ " + last.replace("ရှိ၏၊၊", "ရှိ၏၊")


def _ahara3(pos):
    k3 = AHARA3.split("၊ ")
    mid = f"{RAGA} ရှိ၏၊ ပျော်မွေ့မှု ရှိ၏… မြူ ရှိသော၊ ပြင်းစွာ ပူပန်ခြင်း ရှိသော" if pos else \
        f"{RAGA} မရှိ၊ ပျော်မွေ့မှု မရှိ… မြူ မရှိသော၊ ပြင်းစွာ ပူပန်ခြင်း မရှိသော"
    return (f"“ရဟန်းတို့၊ အကယ်၍ {k3[0]}၌… ရဟန်းတို့၊ အကယ်၍ {k3[1]}၌… ရဟန်းတို့၊ အကယ်၍ {k3[2]}၌ {mid} "
            f"အရာ{VADAMI}”{END}")


PHAGGUNA_D = ("ပရိနိဗ္ဗာန် စံဝင်တော်မူပြီးသော၊ ပပဉ္စ တရားကို ဖြတ်ပြီးသော၊ သံသရာ လမ်းကို ဖြတ်ပြီးသော၊ ဝဋ်ကို ကုန်ဆုံးစေပြီးသော၊ "
              "ဒုက္ခ အားလုံးကို ကျော်လွန်ပြီးသော အတိတ် ဘုရားရှင်တို့ကို ထင်ရှားပြလိုသူသည်")


def _late_ch5():
    first = lambda k: F.unit_my(k)   # noqa: E731
    SENT_X[src_unit(CH5, "Natthi kho taṃ, phagguna")] = (
        f"“ဖဂ္ဂုန၊ {PHAGGUNA_D} အကြင် မျက်စိဖြင့် ထင်ရှားပြနိုင်ရာ၏၊ ထိုမျက်စိ မရှိ။ ဖဂ္ဂုန၊ ထိုလျှာ မရှိ… ဖဂ္ဂုန၊ "
        f"{PHAGGUNA_D} အကြင် မနောဖြင့် ထင်ရှားပြနိုင်ရာ၏၊ ထိုမနော မရှိ”{END}")
    SENT_X[src_unit(CH5, "Nanu āyasmā phagguno")] = (
        f"အသျှင် ဖဂ္ဂုနသည် {BHAGAVA}ကို ဤသို့ လျှောက်ခဲ့သည် မဟုတ်လော – “အသျှင်ဘုရား၊ {PHAGGUNA_D} အကြင် မျက်စိဖြင့် "
        f"ထင်ရှားပြနိုင်ရာ၏၊ ထိုမျက်စိ ရှိပါသလော။ အသျှင်ဘုရား၊ ထိုလျှာ… အသျှင်ဘုရား၊ {PHAGGUNA_D} အကြင် "
        f"မနောဖြင့် ထင်ရှားပြနိုင်ရာ၏၊ ထိုမနော ရှိပါသလော”{END}")
    SENT_X[src_unit(CH5, "Nanu āyasmā nandako")] = (
        f"အသျှင် နန္ဒကသည် ဤသို့ ပြောခဲ့သည် မဟုတ်လော – “ရှေးက {LOBHA} ရှိခဲ့၏၊ ထိုအခါ အကုသိုလ် ဖြစ်ခဲ့၏၊ ထို{LOBHA}သည် "
        f"ယခု မရှိ၊ ဤသို့ဖြင့် ဤသည်ကား ကုသိုလ် ဖြစ်၏။ ရှေးက {DOSA} ရှိခဲ့၏… ရှေးက {MOHA} ရှိခဲ့၏၊ ထိုအခါ အကုသိုလ် "
        f"ဖြစ်ခဲ့၏၊ ထို{MOHA}သည် ယခု မရှိ၊ ဤသို့ဖြင့် ဤသည်ကား ကုသိုလ် ဖြစ်၏”{END}")
    SENT_X[src_unit(CH5, "Yepi te, bhikkhave")] = (
        f"“ရဟန်းတို့၊ ဥက္ကလ ဇနပုဒ်သား ဖြစ်ကြသော ဝဿနှင့် ဘည၊ အကြောင်း မရှိဟု ဆိုသော ဝါဒ ရှိသူ၊ ကံ၏ အကျိုး မရှိဟု ဆိုသော "
        f"ဝါဒ ရှိသူ၊ ဘာမျှ မရှိဟု ဆိုသော ဝါဒ ရှိသူတို့ ရှိခဲ့ကြ၏၊ ထိုသူတို့သည်ပင် ဤ {PATHS} သုံးပါးတို့ကို မကဲ့ရဲ့အပ်၊ "
        f"မပယ်ချအပ်ဟု ထင်မှတ်ခဲ့ကြ၏။ ထိုသို့ ဖြစ်ခြင်းသည် အဘယ်ကြောင့်နည်း။ ကဲ့ရဲ့ခြင်း၊ ပြစ်တင်ခြင်း၊ အပြစ်တင် စွပ်စွဲခြင်းကို "
        f"ကြောက်သောကြောင့် ဖြစ်၏”{END}")
    SENT_X[src_unit(CH5, "Phasse ce, bhikkhave, āhāre… manosañcetanāya ce, bhikkhave, āhāre… viññāṇe ce, bhikkhave, "
                         "āhāre atthi")] = _ahara3(True)
    SENT_X[src_unit(CH5, "Phasse ce, bhikkhave, āhāre… manosañcetanāya ce, bhikkhave, āhāre… viññāṇe ce, bhikkhave, "
                         "āhāre natthi")] = _ahara3(False)
    nanu = f"{BHAGAVA} ဤသို့ ဟောတော်မူသည် မဟုတ်လော – “"
    k = src_line(CH5, "Atītaṃ atthi, anāgataṃ atthīti? Āmantā. Nanu vuttaṃ bhagavatā – tayome")
    LINES_X[k] = (f"{first('Atītaṃ atthi, anāgataṃ atthīti?')} {F.YES}{END} {nanu}ရဟန်းတို့၊ {UNMIXED}။ အဘယ် "
                  f"သုံးပါးတို့နည်း။ {_para(PAST_D, 'ahosi', ('atthi', 'bhavissati'))}။")
    k = src_line(CH5, "Yaṃ, bhikkhave, rūpaṃ ajātaṃ")
    LINES_X[k] = f"“{_para(FUT_D, 'bhavissati', ('atthi', 'ahosi'))}။"
    k = src_line(CH5, "Yaṃ, bhikkhave, rūpaṃ jātaṃ")
    LINES_X[k] = f"“{_para(PRES_D, 'atthi', ('ahosi', 'bhavissati'))}။ ရဟန်းတို့၊ {UNMIXED}။"
    k = src_line(CH5, "Na vattabbaṃ – anāgataṃ atthīti? Āmantā. Nanu vuttaṃ bhagavatā – kabaḷīkāre")
    LINES_X[k] = f"{first('Na vattabbaṃ – anāgataṃ atthīti?')} {F.YES}{END} {nanu}{_ahara(True)}။"
    k = src_line(CH5, "Anāgataṃ atthīti? Āmantā. Nanu vuttaṃ bhagavatā – kabaḷīkāre")
    LINES_X[k] = f"{first('Anāgataṃ atthīti?')} {F.YES}{END} {nanu}{_ahara(False)}။"
    F.SENT.update(SENT_X)
    F.LINES.update(LINES_X)


LATE.append(_late_ch5)




# ===================================================================================== run
F.PROP.update(PROP_X)
F.QUOTE.update(QUOTE_X)
F.SENT.update(SENT_X)
F.LINES.update(LINES_X)
F.ANCHOR.update(ANCHOR_X)
F.FRAMES[-2:-2] = MY_FRAMES          # before the two generic frames (P-ti? / P-ti.)
for _fn in LATE:
    _fn()
for _k, _v in QUOTE_X.items():
    new(_k, _v)
for _k, _v in SENT_X.items():
    new(_k, _v)

DASH = ("–", "—")


def line_check(p, m):
    """Per-line hard rules against the Pāli line (as make_sample.line_check)."""
    errs = []
    if sum(p.count(d) for d in DASH) != sum(m.count(d) for d in DASH):
        errs.append("dash")
    if p.replace("…Pe…", "…pe…").replace("…pe…", "…").count("…") != m.count("…"):
        errs.append("ellipsis")
    if p.count("[") != m.count("["):
        errs.append("[")
    if (re.match(r"\((\d+)\)", p) or [None, None])[1] != (re.match(r"\((\d+)\)", m) or [None, None])[1]:
        errs.append("item number")
    for bad in ("?", "।", ":-"):
        if bad in m:
            errs.append(bad)
    if re.findall(r"\d+", F.strip_id(p)) != re.findall(r"\d+", F.strip_id(m)):
        errs.append("digits")
    return errs


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
        errs = line_check(line, my)
        if errs:
            bad += 1
            print(f"{name}:{ln}: CHECK {errs}\n  P: {line[:300]}\n  M: {my[:300]}")
            if not misses:
                sys.exit(1)
        out.append(my)
    return "\n".join(out).rstrip("\n") + "\n", bad


def main():
    args = sys.argv[1:]
    misses = "--misses" in args
    names = [a for a in args if not a.startswith("--")] or NAMES_OUT
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


if __name__ == "__main__":
    main()
