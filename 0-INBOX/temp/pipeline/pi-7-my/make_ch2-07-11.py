"""Burmese zero-shot of pi-7 2-07 parittattika, 2-08 parittārammaṇattika, 2-09 hīnattika, 2-10 micchattaniyatattika,
2-11 maggārammaṇattika («အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ»), from the Pāli only.

usage: python3 -I -X utf8 make_ch2-07-11.py [chapter ...] [--dev] [--out DIR] [--new]
Every line goes through my7_formulas.translate() with the approved sample's tables (make_sample.py), the finished
group 1-03 … 1-05 (make_ch1-03-05.py) and the finished group 2-01 … 2-02 (make_ch2-01-02.py): make_ch2-01-02 is
IMPORTED (it loads make_ch1-03-05 itself) for its in-memory extensions only; no main block of another script runs
and no file of the sample or of another group is edited or written. This script adds the five triads (pi-1 final
Mātikā), their nouns, notes and unique sentences; every new string is logged in notes-ch2-07-11.md.
A sentence that no frame matches stops the run; it is never guessed. --dev lists every unmatched skeleton instead
of stopping (nothing is written).
"""
import collections
import importlib.util
import pathlib
import re
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import my7_formulas as F  # noqa: E402
import make_sample as S  # noqa: E402,F401  (tables only)

_spec = importlib.util.spec_from_file_location("make_ch2_01_02", HERE / "make_ch2-01-02.py")
M = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(M)          # in-memory extensions of 2-01 … 2-02 (+ 1-03 … 1-05); its __main__ does not run
G = M.G
assert M.F is F and G.F is F
_TABLES = M._TABLES
_BEFORE = {t: dict(getattr(F, t)) for t in _TABLES}        # the tables as the sample + 1-03 … 2-02 leave them

ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-7_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters"
NAMES = ["2-07-parittattika.md", "2-08-parittarammanattika.md", "2-09-hinattika.md",
         "2-10-micchattaniyatattika.md", "2-11-maggarammanattika.md"]
C, END, PE, W = F.C, F.END, F.PE, F.W
WCH = r"[\wāīūṃṅñṭḍṇḷ]"

NEW = collections.OrderedDict()     # every new string of this script: Pāli -> Burmese


def new(pali, my):
    NEW.setdefault(pali, my)
    return my


# ===================================================================================== the five triads (pi-1 final)
_tw = G._tw
TRIADS_ADD = {
    "paritta": {
        "paritt": _tw("parittā dhammā", "အကန့်အသတ် ရှိသော", "^1-M1-12"),
        "mahaggat": _tw("mahaggatā dhammā", "ကြီးမြတ်သော", "^1-M1-12"),
        "appamāṇ": _tw("appamāṇā dhammā", "အတိုင်းအဆ မရှိသော", "^1-M1-12"),
    },
    "parittarammana": {
        "parittārammaṇ": _tw("parittārammaṇā dhammā", "အကန့်အသတ် ရှိသည်ကို အာရုံပြုသော", "^1-M1-13"),
        "mahaggatārammaṇ": _tw("mahaggatārammaṇā dhammā", "ကြီးမြတ်သည်ကို အာရုံပြုသော", "^1-M1-13"),
        "appamāṇārammaṇ": _tw("appamāṇārammaṇā dhammā", "အတိုင်းအဆ မရှိသည်ကို အာရုံပြုသော", "^1-M1-13"),
    },
    "hina": {
        "hīn": _tw("hīnā dhammā", "ယုတ်ညံ့သော", "^1-M1-14"),
        "majjhim": _tw("majjhimā dhammā", "အလယ်အလတ်", "^1-M1-14"),
        "paṇīt": _tw("paṇītā dhammā", "မွန်မြတ်သော", "^1-M1-14"),
    },
    "micchatta": {
        "micchattaniyat": _tw("micchattaniyatā dhammā", "မှားယွင်းမှု၌ ကျိန်းသေသော", "^1-M1-15"),
        "sammattaniyat": _tw("sammattaniyatā dhammā", "မှန်ကန်မှု၌ ကျိန်းသေသော", "^1-M1-15"),
        "aniyat": _tw("aniyatā dhammā", "မကျိန်းသေသော", "^1-M1-15"),
    },
    "magga": {
        "maggārammaṇ": _tw("maggārammaṇā dhammā", "မဂ်ကို အာရုံပြုသော", "^1-M1-16"),
        "maggahetuk": _tw("maggahetukā dhammā", "မဂ်ကို အမြစ်ပြုသော", "^1-M1-16"),
        # maggādhipati (an i-stem): prep() reads its endings as the a-stem endings «maggādhipat-o/-aṃ/…»
        "maggādhipat": _tw("maggādhipatino dhammā", "မဂ်ကို အကြီးအမှူးပြုသော", "^1-M1-16"),
    },
}
# two terms of two triads in one compound before «-cittasamaṅgissa» («parittārammaṇaparittacittasamaṅgissa»): both
# qualify the mind, stacked as the module stacks two terms on one noun (a space between them)
COMBO = {}
for _a in TRIADS_ADD["parittarammana"]:
    for _b in TRIADS_ADD["paritta"]:
        COMBO[f"{_a}a{_b}"] = f"{TRIADS_ADD['parittarammana'][_a]}{C} {TRIADS_ADD['paritta'][_b]}"   # harmonise H6 «A၊ B»
COMBO["maggahetukamaggādhipat"] = f"{TRIADS_ADD['magga']['maggahetuk']}{C} {TRIADS_ADD['magga']['maggādhipat']}"
# «maggārammaṇā ca maggādhipatī ca tayo khandhā», «maggārammaṇañca maggādhipatiñca ekaṃ khandhaṃ», «… -ānañca … -īnañca
# khandhānaṃ» (one noun that is BOTH; not with the noun dhamma): prep() joins the two terms into one slot «A-ca-B-»,
# rendered as two stacked qualifiers «A၊ B N» (as 2-01 … 2-02 «pītisahagatā ca sukhasahagatā ca tayo khandhā»);
# with the noun dhamma the module's coordination «A သဘောတရားနှင့် B သဘောတရား» stays (two kinds of phenomena)
for _a in ("maggārammaṇ", "maggahetuk"):
    COMBO[f"{_a}camaggādhipat"] = f"{TRIADS_ADD['magga'][_a]}{C} {TRIADS_ADD['magga']['maggādhipat']}"
TRIADS_ADD["combo"] = COMBO
_END = M._END
F.TRIADS.update(TRIADS_ADD)
F.TRIAD_END.update({t: _END for t in TRIADS_ADD})
F.rebuild()
_TERMW = (r"(?:[Pp]arittārammaṇ|[Mm]ahaggatārammaṇ|[Aa]ppamāṇārammaṇ|[Pp]aritt|[Mm]ahaggat|[Aa]ppamāṇ|[Hh]īn|"
          r"[Mm]ajjhim|[Pp]aṇīt|[Mm]icchattaniyat|[Ss]ammattaniyat|[Aa]niyat|[Mm]aggārammaṇ|[Mm]aggahetuk|"
          r"[Mm]aggādhipat)")

# ===================================================================================== Pāli preparation (in memory)
# maggādhipati (i-stem) -> the a-stem endings the frames know (the Burmese of a term does not depend on its ending)
_MAD = [("maggādhipatīnañca", "maggādhipatānañca"), ("maggādhipatīnaṃ", "maggādhipatānaṃ"),
        ("maggādhipatissa", "maggādhipatassa"), ("maggādhipatiñca", "maggādhipatañca"),
        ("maggādhipatiṃ", "maggādhipataṃ"), ("maggādhipatī", "maggādhipatā"),
        ("maggādhipaticittasamaṅgissa", "maggādhipatacittasamaṅgissa"), ("maggādhipati", "maggādhipato")]
SLIP_FIX = {}


_PJ_CASE = r"(ā|o|aṃ|assa|ena|āya|e|ānaṃ)"


def prep(text):
    text = M.prep(text)
    for a, b in SLIP_FIX.items():
        if a in text:
            F.SLIPS.add(f"«{a}» read as «{b}»")
            text = text.replace(a, b)
    text = text.replace("maggahetukamaggādhipaticittasamaṅgissa", "maggahetukamaggādhipatacittasamaṅgissa")
    for a, b in _MAD:
        for x, y in ((a, b), (a[0].upper() + a[1:], b[0].upper() + b[1:])):
            text = re.sub(r"(?<![\wāīūṃṅñṭḍṇḷ{(])" + x + r"(?![\wāīūṃṅñṭḍṇḷ])", y, text)
    # «X-assa ca Y-assa ca Zpaccayena» (two terms, the noun left out) = «… dhammassa» (the noun of the frame supplied;
    # as 1-03 … 1-05 prep for its terms; logged)
    def _noun(m):
        F.SLIPS.add(f"«{m[1]}» without «dhamm{m[2]}» (the noun supplied)")
        return f"{m[1]} dhamm{m[2]}"
    text = re.sub(r"(?<![\wāīūṃṅñṭḍṇḷ])(" + _TERMW + r"(assa|o|aṃ) ca " + _TERMW + r"(?:assa|o|aṃ) ca)"
                  r"(?= [a-zāīūṃṅñṭḍṇḷ]*paccayena|…)", _noun, text)
    # two terms on one noun (not dhamma): one slot «A-ca-B-» (see COMBO)
    _no = r"(?!dhamm|[a-zāīūṃṅñṭḍṇḷ]*paccay|…)"
    text = re.sub(r"(?<![\wāīūṃṅñṭḍṇḷ])([Mm]aggārammaṇ|[Mm]aggahetuk)" + _PJ_CASE + r" ca maggādhipat\2 ca " + _no,
                  r"\1camaggādhipat\2 ", text)
    text = re.sub(r"(?<![\wāīūṃṅñṭḍṇḷ])([Mm]aggārammaṇ|[Mm]aggahetuk)(a|āna)ñca maggādhipat\2ñca " + _no,
                  r"\1camaggādhipat\2ṃ ", text)
    # «X-ādhipati» = «X-o adhipati» (as 1-03 … 1-05 prep for its terms)
    text = re.sub(r"(?<![\wāīūṃṅñṭḍṇḷ])(" + _TERMW + r")ādhipati(?![\wāīūṃṅñṭḍṇḷ])", r"\1o adhipati", text)
    for i, a in enumerate(NOTEP):
        text = text.replace(a, f"(⁑m{i})")
    return text


HLINES = {}
SK = {}
SKF = {}

# triad names (NEW, the pattern of 1-03 … 1-05 «<abstract noun> သုံးမျိုးတွဲ»)
F.TIKA_NAME["Parittattikaṃ"] = new("Parittattikaṃ", f"အကန့်အသတ် ရှိခြင်း {F.TIKA}")
F.TIKA_NAME["Parittārammaṇattikaṃ"] = new("Parittārammaṇattikaṃ", f"အကန့်အသတ် ရှိသည်ကို အာရုံပြုခြင်း {F.TIKA}")
F.TIKA_NAME["Hīnattikaṃ"] = new("Hīnattikaṃ", f"ယုတ်ညံ့ခြင်း {F.TIKA}")
F.TIKA_NAME["Micchattaniyatattikaṃ"] = new("Micchattaniyatattikaṃ", f"မှားယွင်းမှု၌ ကျိန်းသေခြင်း {F.TIKA}")
F.TIKA_NAME["Maggārammaṇattikaṃ"] = new("Maggārammaṇattikaṃ", f"မဂ်ကို အာရုံပြုခြင်း {F.TIKA}")
for _p in ("Parittattikaṃ", "Parittārammaṇattikaṃ", "Hīnattikaṃ", "Micchattaniyatattikaṃ", "Maggārammaṇattikaṃ"):
    HLINES[f"{_p} niṭṭhitaṃ."] = F.finished(F.TIKA_NAME[_p])

# ===================================================================================== words of the instructions
# (the 2-01 … 2-02 / 1-03 … 1-05 / sample words where they exist; NEW otherwise)
KATABBA, PANHA, VITTH, GANETABBA, EVAM = M.KATABBA, M.PANHA, M.VITTH, M.GANETABBA, M.EVAM
PARIPUNNA, SADISA, SADISA_PL, SADISA_KAT, AVASESA = M.PARIPUNNA, M.SADISA, M.SADISA_PL, M.SADISA_KAT, M.AVASESA
NATTHI, PAVATTI, PATICCA_V, VARA_N, PS, NIYAM = M.NATTHI, M.PAVATTI, M.PATICCA_V, M.VARA_N, M.PS, M.NIYAM
VIPAKA_N, DH, LAK = M.VIPAKA_N, F.DHAMMA, F.LAKAUNG
cn, cd, CNT = F.cname, F.cond, F.COUNT
MAHABHUTA = F.NOUN["mahābhūtā"][0]
CITTASAM = G.CITTASAM
SABBE = M.SABBE                                                      # sabbe «အားလုံး» (2-01 … 2-02)
NIDDIS = new("niddisitabbaṃ", "ညွှန်ပြရမည်")
NAKAT = new("na kātabbaṃ", "မပြုရ")
CAKKA = new("cakkaṃ (kātabbaṃ)", "စက်ဝိုင်းကဲ့သို့ လှည့်ပတ်၍")
LUN = "လုံး"                                                          # «Npi» all N «…ခုလုံး» (2-01 … 2-02)


def note(pali, my):
    """a note without slot words (F.NOTES, used by every frame); an existing value is kept"""
    F.NOTES.setdefault(pali, new(pali, my))


note("(evaṃ gaṇetabbaṃ)", f"({M.EVAM_THUS} {GANETABBA})")          # harmonise H14 (= 2-03 … 2-06 «(ဤသို့ ရေတွက်ရမည်)»)
note("(sabbepi mahābhūtā kātabbā)", f"({MAHABHUTA} {SABBE}ကိုလည်း {KATABBA})")
note("(sabbe mahābhūtā kātabbā)", f"({MAHABHUTA} {SABBE}ကို {KATABBA})")
note("(tisso pañhā kātabbā)", f"({PANHA} {CNT['tīṇi']} {KATABBA})")
note("(terasa pañhā)", f"({PANHA} {CNT['terasa']})")
note("(vitthāretabbaṃ)", f"({VITTH})")
note("(paṭisandhikkhaṇe tīṇipi kātabbā)", f"({PS}၌ {CNT['tīṇi']}{LUN}ကိုလည်း {KATABBA})")
note("(paṭisandhi natthi, sattarasa pañhā paripuṇṇā)",
     f"({F.PATISANDHI} {NATTHI}{C} {PANHA} {CNT['sattarasa']} {PARIPUNNA}ကြသည်)")
note("(paṭiccavārasadisā dvādasa pañhā)", f"({PATICCA_V}နှင့် တူသော {PANHA} {CNT['dvādasa']})")
note("(paripuṇṇaṃ, vipākoti niddisitabbaṃ cittasamuṭṭhānaṃ rūpaṃ vipākoti na kātabbaṃ)",
     f"({PARIPUNNA}သည်{C} {VIPAKA_N}ဟု {NIDDIS} {CITTASAM} ရုပ်ကို {VIPAKA_N}ဟု {NAKAT})")
note("(paṭisandhivipākopi natthi)", f"({F.PATISANDHI}၌ {VIPAKA_N}လည်း {NATTHI})")
note("(paṭisandhi natthi)", f"({F.PATISANDHI} {NATTHI})")
note("(vipākopi paṭisandhipi natthi)", f"({VIPAKA_N}လည်း{C} {F.PATISANDHI}လည်း {NATTHI})")
note("(pavattipaṭisandhi kātabbā)", f"({PAVATTI}နှင့် {F.PATISANDHI}ကို {KATABBA})")
note("(tisso pañhā, pavattipaṭisandhi kātabbā)", f"({PANHA} {CNT['tīṇi']}{C} {PAVATTI}နှင့် {F.PATISANDHI}ကို {KATABBA})")
note("(pavattimeva)", f"({PAVATTI}သာ)")
note("(cakkaṃ kātabbaṃ)", f"({CAKKA} {KATABBA})")
note("(cakkaṃ kātabbaṃ kusalattikasadisaṃ)", f"({CAKKA} {S.KT}နှင့် တူအောင် {KATABBA})")
note("(paṭiccavārasadisaṃ", f"({PATICCA_V}{SADISA}")                  # closed in the next sentence «Pañca).»
SK["pañca)."] = f"{CNT['pañca']}){END}"
note("(paṭiccavārasadisā kātabbā)", f"({PATICCA_V}{SADISA_KAT})")
SAMKHITTA = F.NOTES["(saṃkhittaṃ)"][1:-1]
IMINA, VIBHAJ = M.IMINA, G.VIBHAJ
note("(sabbe paccayā iminā kāraṇena vitthāretabbā", f"({F.PACCAYA} {SABBE}ကို {IMINA} {VITTH}")   # closed by «Saṃkhittaṃ).»
note("(saṃkhittaṃ, sabbāni paccayāni vitthāretabbāni)", f"({SAMKHITTA}{C} {F.PACCAYA} {SABBE}ကို {VITTH})")
MICCHATTA_PART = new("micchatta- (-sadisaṃ: the micchattaniyata part)", "မှားယွင်းမှု အပိုင်း")
note("(tīṇi pañhā, micchattasadisaṃ)", f"({PANHA} {CNT['tīṇi']}{C} {MICCHATTA_PART}{SADISA})")
note("(saṃkhittaṃ, kusalattike paccayavārasadisaṃ vibhajitabbaṃ)",
     f"({SAMKHITTA}{C} {S.KT}၌ {VARA_N['Paccayavāro']}နှင့် တူအောင် {VIBHAJ})")
note("(kusalattikasadisaṃ, pañca kātabbā)", f"({S.KT}{SADISA}{C} {CNT['pañca']} {KATABBA})")
note("(paripuṇṇaṃ)", f"({PARIPUNNA}သည်)")
note("(paṭiccavārasadisaṃ, nava pañhā)", f"({PATICCA_V}{SADISA}{C} {PANHA} {CNT['nava']})")
note("(paṭiccavārasadisaṃ, tisso pañhā)", f"({PATICCA_V}{SADISA}{C} {PANHA} {CNT['tīṇi']})")
note("(kusalattikasadisā, terasa pañhā)", f"({S.KT}{SADISA_PL}{C} {PANHA} {CNT['terasa']})")
note("(tisso pañhā)", f"({PANHA} {CNT['tīṇi']})")
note("(paripuṇṇā dvepi)", f"({CNT['dve']}{LUN}လည်း {PARIPUNNA}ကြသည်)")
note("(pañca pañhā)", f"({PANHA} {CNT['pañca']})")
note("(paṭhamaghaṭane tīṇi)", f"(ပထမ {F.GHATANA}၌ {CNT['tīṇi']})")
note("(dutiyaghaṭane tīṇi pañhā)", f"(ဒုတိယ {F.GHATANA}၌ {PANHA} {CNT['tīṇi']})")
note("(paripuṇṇaṃ, arūpanti niyāmetabbaṃ)", f"({PARIPUNNA}သည်{C} {M.ARUPA_N}ဟု {NIYAM})")
note("(iminā kāraṇena sattarasa pañhā kātabbā)", f"({IMINA} {PANHA} {CNT['sattarasa']} {KATABBA})")
note("(tīsupi sattarasa pañhā kātabbā)", f"({CNT['tīṇi']}{LUN}၌လည်း {PANHA} {CNT['sattarasa']} {KATABBA})")
note("(anantarasadisaṃ", F.SK["(anantarasadisaṃ."][:-1])            # closed in the next sentence (as 1-03 … 1-05)
note("(nānākkhaṇikā natthi, sattarasa pañhā kātabbā)",
     f"({F.LEX['nānākkhaṇikā'][0]} {NATTHI}{C} {PANHA} {CNT['sattarasa']} {KATABBA})")
note("(ime satta paccayā sattarasa pañhā hetusadisā)",
     f"(ဤ {F.PACCAYA} ခုနစ်ပါး၌ {PANHA} {CNT['sattarasa']} {F.N['hetu']}{SADISA_PL})")
note("(anantarasadisā)", f"({F.N['anantara']}{SADISA_PL})")
note("(sattarasa pañhā)", f"({PANHA} {CNT['sattarasa']})")
PAKATA_AR = new("pakatārammaṇa", f"ပကတိ {F.N['ārammaṇa']}")
UPAN_AR = new("upanissayārammaṇa", f"{F.N['upanissaya']} {F.N['ārammaṇa']}")
note("(naārammaṇe gahite pakatārammaṇampi upanissayārammaṇampi dvepi chijjanti)",
     f"({cd('ārammaṇa', 'n', True)}ကို " + new("gahite", "ယူသောအခါ") + f" {PAKATA_AR}လည်း{C} {UPAN_AR}လည်း "
     f"{CNT['dve']}{LUN} " + new("chijjanti", "ပြတ်ကြသည်") + ")")
SK["paccayānulomaṃ."] = F.HEAD["Paccayānulomaṃ"] + END
SK["nava pañhā kātabbā, āvajjanā na kātabbā)."] = (f"{PANHA} {CNT['nava']} {KATABBA}{C} {F.LEX['āvajjanā'][0]}ကို "
                                                   f"{NAKAT}){END}")
SKF["ahetukaṃ §T§aṃ"] = f"{F.AHETUKA} {{T1}}"                         # the noun left out before «…»
SKF["dve khandhā ca"] = f"{F.KHANDHA} {F.PAA[2]}{LAK}"                # cut short (as 2-01 … 2-02 «dve khandhe ca»)
SK["pañhāvāro."] = F.HEAD["Pañhāvāro"] + END

# notes whose Pāli holds condition / term words: prep() puts a placeholder «(⁑m<i>)» in their place
ARUPE = M.ARUPE                                                       # arūpe «ရုပ်မရှိသော ဘုံ၌» (2-01 … 2-02)
T_PAR = TRIADS_ADD["paritta"]
NOTEP = {"(avasesā cha pañhā hetupaccayasadisā satta kātabbā)":
         f"({AVASESA} {PANHA} {CNT['cha']}ကို {cn('hetu')}နှင့် တူအောင် {CNT['satta']} {KATABBA})",
         "(sabbe mahābhūtā vitthāretabbā, arūpe parittamūlake tisso pañhā)":
         f"({MAHABHUTA} {SABBE}ကို {VITTH}{C} {ARUPE} {T_PAR['paritt']} {DH}{F.MULAKA}၌ {PANHA} {CNT['tīṇi']})",
         "(mahaggatārammaṇe paṭisandhi natthi)":
         f"({TRIADS_ADD['parittarammana']['mahaggatārammaṇ']} {DH}၌ {F.PATISANDHI} {NATTHI})",
         "(napacchājātapaccayañca naāsevanapaccayañca naadhipatisadisaṃ)":
         f"({cd('pacchājāta', 'n', True)}{LAK}{C} {cd('āsevana', 'n', True)}{LAK} {M.negbare('adhipati')}{SADISA})",
         "(dve pañhā micchattaniyatasadisā)":
         f"({PANHA} {CNT['dve']} {TRIADS_ADD['micchatta']['micchattaniyat']} {DH}{SADISA_PL})"}
# editorial notes in braces
F.EDNOTES["nevasaññānāsaññāyatanassa (?) aññesu tikesu oloketabbaṃ"] = new(
    "{nevasaññānāsaññāyatanassa (?) aññesu tikesu oloketabbaṃ}",
    F.variant("nevasaññānāsaññāyatanassa (?)")[1:-1] + " " + new("aññesu tikesu oloketabbaṃ",
                                                                  f"အခြား {F.TIKA}တို့၌ ကြည့်ရှုရမည်"))
SKF["53asaññasattānaṃ"] = "53" + F.SKF["asaññasattānaṃ"]               # a number glued to the word (kept as written)


def notep_register():
    for _i, (_p, _my) in enumerate(NOTEP.items()):
        F.NOTES[f"(⁑m{_i})"] = new(_p, _my)


def sk(pali, tpl):
    """a whole unit, registered by its Pāli (after prep), keyed by the skeleton; templates use the slots in order"""
    key, slots = F.slot(F.lc(F.pe(prep(pali).strip())))
    F.render(tpl, slots)
    SK[key] = tpl
    new(pali, tpl if isinstance(tpl, str) else "(frame)")


# --- whole units (2-07) ----------------------------------------------------------------------------------------------
sk("(Sahajātavāropi paṭiccavārasadiso.)", f"({VARA_N['Sahajātavāro']}သည်လည်း {PATICCA_V}{SADISA}{END})")
sk("(Nissayavāro paccayavārasadiso.)", f"({VARA_N['Nissayavāro']}သည် {VARA_N['Paccayavāro']}{SADISA}{END})")
sk("(Sampayuttavāro saṃsaṭṭhavārasadiso).", f"({VARA_N['Sampayuttavāro']}သည် {VARA_N['Saṃsaṭṭhavāro']}{SADISA}){END}")
sk("(Samanantarapaccayaṃ anantarapaccayasadisaṃ.)", f"({{C1.n}}သည် {cn('anantara')}{SADISA}{END})")

# «Anulomaṃ.» closing the positive order = «အဟုတ်ပြ ပုံစံ။» as 1-01 (1-03 … 2-02 render it through the LEX noun
# anulomaṃ «လျော်ညီခြင်း စိတ်», the conformity mind: logged for the consistency pass). Registered only while these
# chapters are translated, so that the finished groups regenerate unchanged.
LOCAL_HLINES = {"Anulomaṃ.": new("Anulomaṃ. (closing the positive order)", "အဟုတ်ပြ ပုံစံ" + END)}

# --- whole units (2-09) ----------------------------------------------------------------------------------------------
sk("(Hīnattikaṃ saṃkiliṭṭhattikasadisaṃ vitthāretabbaṃ paripuṇṇaṃ.)",
   f"({F.TIKA_NAME['Hīnattikaṃ']}ကို {F.TIKA_NAME['Saṃkiliṭṭhattikaṃ']}နှင့် တူအောင် {PARIPUNNA}စွာ {VITTH}{END})")

# --- whole units (2-08) ----------------------------------------------------------------------------------------------
sk("(Sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi paṭiccavārasadiso).",
   "(" + (C + " ").join(VARA_N[v] + "လည်း" for v in ("Sahajātavāro", "Paccayavāro", "Nissayavāro", "Saṃsaṭṭhavāro",
                                                       "Sampayuttavāro")) + f" {PATICCA_V}{SADISA}){END}")

# --- whole units (2-10) ----------------------------------------------------------------------------------------------
sk("(Sahajātavāro paṭiccavārasadiso.)", f"({VARA_N['Sahajātavāro']}သည် {PATICCA_V}{SADISA}{END})")
sk("(Sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi paṭiccavārasadiso.)",
   "(" + (C + " ").join(VARA_N[v] + "လည်း" for v in ("Sahajātavāro", "Paccayavāro", "Nissayavāro", "Saṃsaṭṭhavāro",
                                                       "Sampayuttavāro")) + f" {PATICCA_V}{SADISA}{END})")
sk("(Nissayavāro paccayavārasadiso).", f"({VARA_N['Nissayavāro']}သည် {VARA_N['Paccayavāro']}{SADISA}){END}")
VATTHU_OBJ = F.VATTHU                    # vatthu «မှီရာ ဝတ္ထု» (pi-5; the English cross-check also reads the physical base)
PARAMASANTA = new("parāmasantassa", "မှားယွင်းစွာ " + W("parāmāso", "ယူဆ", "1") + "သူ၏")
sk("Yaṃ vatthuṃ parāmasantassa micchattaniyatā khandhā uppajjanti, taṃ vatthu micchattaniyatānaṃ khandhānaṃ "
   "ārammaṇapaccayena paccayo.",
   f"အကြင် {VATTHU_OBJ}ကို {PARAMASANTA} {{T1}} {F.KHANDHA}တို့သည် ဖြစ်ပေါ်ကြ၏{C} ထို {VATTHU_OBJ}သည် {{T2}} "
   f"{F.KHANDHA}တို့အား {{C1.if}}{END}")

# --- lexicon (pañhāvāra) ---------------------------------------------------------------------------------------------
F.add_lex("g", {"vatthussa": F.VATTHU, "tasseva": new("tasseva", "ထိုအရာကိုယ်တိုင်")})
F.add_lex("a", {"dibbaṃ cakkhuṃ": M.DIBBA_C, "dibbaṃ sotadhātuṃ": M.DIBBA_S,
                "iddhividhañāṇaṃ": F.LEX["iddhividhañāṇassa"][0], "cetopariyañāṇaṃ": F.LEX["cetopariyañāṇassa"][0],
                "pubbenivāsānussatiñāṇaṃ": F.LEX["pubbenivāsānussatiñāṇassa"][0],
                "yathākammūpagañāṇaṃ": F.LEX["yathākammūpagañāṇassa"][0],
                "anāgataṃsañāṇaṃ": F.LEX["anāgataṃsañāṇassa"][0]})
# «X-paccavekkhaṇaṃ» the reviewing of X «Xကို ပြန်လည် ဆင်ခြင်ခြင်း» (pi-1 … pi-5 paccavekkhaṇā «ပြန်လည် ဆင်ခြင်ခြင်း»)
PACCAVEKKHANA = W("paccavekkhaṇā", "ပြန်လည် ဆင်ခြင်ခြင်း", "5")
_PV = {"maggapaccavekkhaṇaṃ": "မဂ်", "phalapaccavekkhaṇaṃ": "ဖိုလ်", "nibbānapaccavekkhaṇaṃ": F.LEX["nibbānaṃ"][0],
       "dibbacakkhupaccavekkhaṇaṃ": M.DIBBA_C, "dibbasotadhātupaccavekkhaṇaṃ": M.DIBBA_S,
       "ākāsānañcāyatanapaccavekkhaṇaṃ": F.LEX["ākāsānañcāyatanaṃ"][0],
       "viññāṇañcāyatanapaccavekkhaṇaṃ": F.LEX["viññāṇañcāyatanassa"][0],
       "ākiñcaññāyatanapaccavekkhaṇaṃ": F.LEX["ākiñcaññāyatanaṃ"][0],
       "nevasaññānāsaññāyatanapaccavekkhaṇaṃ": F.LEX["nevasaññānāsaññāyatanaṃ"][0]}
for _o, _my in G.ORD.items():
    _PV[f"{_o}ajjhānapaccavekkhaṇaṃ".replace("aajjh", "ajjh")] = f"{_my} ဈာန်"
for _p in ("iddhividha", "cetopariya", "pubbenivāsānussati", "yathākammūpaga", "anāgataṃsa"):
    _PV[f"{_p}ñāṇapaccavekkhaṇaṃ"] = F.LEX[f"{_p}ñāṇassa"][0]
F.add_lex("na", {k: new(k, f"{v}ကို {PACCAVEKKHANA}") for k, v in _PV.items()})
F.add_lex("na", {"viññāṇañcāyatanaṃ": F.LEX["viññāṇañcāyatanassa"][0]})
# the heinous deeds (1-03 … 1-05 / pi-5 «… ကံ»), the deeds as gerunds (the 1-01 values), wrong view
DEEDS = {"pitughātikamm": W("pitughātakammassa", "အဖကို သတ်ခြင်း ကံ", "5"),
         "arahantaghātikamm": W("arahantaghātakammassa", "ရဟန္တာကို သတ်ခြင်း ကံ", "5"),
         "ruhiruppādakamm": W("ruhiruppādakammassa", "ဘုရား၏ ကိုယ်တော်မှ သွေးကို ထွက်စေခြင်း ကံ", "5"),
         "saṅghabhedakamm": F.LEX["saṅghabhedakakammassa"][0]}
for _k, _my in DEEDS.items():
    F.add_lex("na", {_k + "aṃ": _my})
    F.add_lex("g", {_k + "assa": _my})
F.add_lex("na", {"rūpajīvitindriyaṃ": F.FIXED["rūpajīvitindriyaṃ"][0]})
F.add_lex("g", {"domanassassa": F.LEX["domanassaṃ"][0], "paccavekkhaṇāya": PACCAVEKKHANA})
F.add_lex("n", {"paccavekkhaṇā": PACCAVEKKHANA})
F.add_lex("n", {"aniyatamicchādiṭṭhi": f"{TRIADS_ADD['micchatta']['aniyat']} {F.LEX['micchādiṭṭhi'][0]}"})
F.add_lex("x", {"mātaraṃ jīvitā voropetvā": "အမိကို အသက်မှ သတ်၍", "pitaraṃ jīvitā voropetvā": "အဖကို အသက်မှ သတ်၍",
                "arahantaṃ jīvitā voropetvā": "ရဟန္တာကို အသက်မှ သတ်၍",
                "duṭṭhena cittena tathāgatassa lohitaṃ uppādetvā":
                "ပြစ်မှားသော စိတ်ဖြင့် မြတ်စွာဘုရား၏ သွေးကို ထွက်စေ၍"})
F.add_lex("na", {"uposathaṃ": F.LEX["uposathakammaṃ karoti"][0].split("ကို")[0],
                 "uposathakammaṃ": F.LEX["uposathakammaṃ karoti"][0].split("ကို")[0]})

# ===================================================================================== engine extensions (in memory)
# (a) a counting line with bare locatives sharing the next count: 2-01 … 2-02's count_line(), whose trigger does not
#     see locatives with «ñ» («nasamanantare naaññamaññe naupanissaye pañca»): the same rendering, a wider trigger
_count_line0 = M.count_line
_BARE2 = re.compile(r"(?:^|[\s…])(?:na|no)?[a-zāīūṃṅñṭḍṇḷ]+(?:e|yā) (?:na|no)?[a-zāīūṃṅñṭḍṇḷ]+(?:e|yā) ", re.I)


def count_line(u):
    r = _count_line0(u)
    if r is not None or not _BARE2.search(u):
        return r
    # the same algorithm with the wider trigger: «sabbattha» stands in so that the original's trigger opens; the
    # stand-in is a token of its own and is removed before rendering
    found = re.findall(r"(\s*)(…|\([^()]*\)|[^\s…]+)", u)
    toks = [t for _, t in found]
    for t in toks:
        core = t.rstrip(",.")
        if not core or t == "…" or t.startswith("("):
            continue
        if not (M._LOCW.match(core) or M._ABW.match(core) or core in F.COUNT):
            return None
    out, prev, bare = [], None, False
    for ws, t in found:
        sp = " " if ws and out else ""
        if t == "…":
            out.append(sp + F.PE)
            prev = "pe"
            continue
        if t.startswith("("):
            if t not in F.NOTES:
                return None
            out.append(sp + F.NOTES[t])
            prev = "note"
            continue
        core, pu = t.rstrip(",."), t[len(t.rstrip(",.")):]
        if not core:
            out.append(F.punct(pu))
            continue
        lw, ab = M._LOCW.match(core), M._ABW.match(core)
        if ab:
            my, kind = F.cond(ab["stem"].lower(), "ab", bool(ab["neg"])), "ab"
        elif lw and lw["loc"].lower() in F.LOC2STEM:
            my, kind = F.cond(F.LOC2STEM[lw["loc"].lower()], "loc", bool(lw["neg"])), "loc"
        elif core in F.COUNT:
            my, kind = F.COUNT[core], "cnt"
        else:
            return None
        if prev in ("loc", "ab") and kind == "loc" and not out[-1].endswith((C, END)):
            out[-1] += C
        out.append(sp + my + F.punct(pu))
        bare |= prev == "loc" and kind == "loc"
        prev = kind
    return "".join(out) if bare else None


M.count_line = count_line


# (b) comma lists in a fragment: the comma split of 1-03 … 1-05 (pairs2) is made outside brackets, and a part that is
#     a bare condition chain (with its notes) is rendered by the chain («…, vatthuṃ paccayā X khandhā (note),
#     adhipatipaccayā (note), anantarapaccayā…»)
def _split_out(body):
    parts, depth, cur, i = [], 0, "", 0
    while i < len(body):
        ch = body[i]
        depth += ch == "("
        depth -= ch == ")"
        if depth == 0 and body.startswith(", ", i):
            parts.append(cur)
            cur, i = "", i + 2
            continue
        cur += ch
        i += 1
    return parts + [cur]


def pairs2(sk_, slots):
    body = sk_.strip()
    end = ""
    if body[-1:] in ".;":
        body, end = body[:-1], F.punct(body[-1])
    parts = _split_out(body)
    if len(parts) < 2:
        return None
    outs = []
    for p_, sub in zip(parts, G._sub_slots(parts, slots)):
        try:
            r = G.part_my(p_, sub)
        except (KeyError, StopIteration, IndexError, ValueError):
            r = None
        if r is None:
            return None
        outs.append(r)
    return (C + " ").join(outs) + end


G.pairs2 = pairs2
_part_my1 = G.part_my
_NOTE_ALT = None


def _is_chain(p_):
    body = p_.strip()
    for k in sorted(F.NOTES, key=len, reverse=True):
        body = body.replace(k, "")
    return bool(re.fullmatch(r"\s*(?:§C§ā\s*)+", body))


def part_my(p_, sub):
    if "§C§ā" in p_ and _is_chain(p_) and not any(sub[k] for k in "TKVD"):
        return F.chain(p_.strip(), sub, [0], [0], [0])
    return _part_my1(p_, sub)


G.part_my = part_my

# --- source slips (translated as written; normalised in memory only where a frame needs it) -------------------------
SLIP_FIX.update({"paccayena paccaya…": "paccayena paccayo…", "maggāhetuk": "maggahetuk", "(evaṃ gaṇatabbaṃ)": "(evaṃ gaṇetabbaṃ)", "avigate eka (": "avigate ekaṃ (",
                 "vippassati": "vipassati", "rūpaṃ.(2)": "rūpaṃ. (2)", "….(1)": "…. (1)",
                 "āsevanapaccayā(vipākopi": "āsevanapaccayā (vipākopi"})


notep_register()
F.HLINES.update(HLINES)
F.SK.update(SK)
F.SKF.update(SKF)

REVIEW = False


def translate(name):
    keep = {k: F.HLINES.get(k) for k in LOCAL_HLINES}
    F.HLINES.update(LOCAL_HLINES)
    try:
        return F.translate(prep((PALI / name).read_text(encoding="utf-8-sig")))
    finally:
        for k, v in keep.items():
            if v is None:
                F.HLINES.pop(k, None)
            else:
                F.HLINES[k] = v


# 2-01 … 2-02's unit frame for «… vicāro ca paṭisandhikkhaṇe…pe….» (a missing full stop) also fires on the regular
# «… dve khandhe…pe… paṭisandhikkhaṇe…pe….» (the «…» before the prefix): same Burmese, but no slip; its message is
# dropped here
_PS_MSG = "«… vicāro ca paṭisandhikkhaṇe…pe….»: no full stop before «paṭisandhikkhaṇe» (none added)"


def chapter(name):
    txt = translate(name)
    F.SLIPS.discard(_PS_MSG)
    if not F.DEV or REVIEW:
        (OUT / name).write_text(txt, encoding="utf-8")
        print(f"wrote {name}: {sum(1 for l in txt.splitlines() if l)} lines")


if __name__ == "__main__":
    F.DEV = "--dev" in sys.argv
    if "--out" in sys.argv:
        REVIEW = True
        OUT = pathlib.Path(sys.argv[sys.argv.index("--out") + 1]).resolve()
        del sys.argv[sys.argv.index("--out"):sys.argv.index("--out") + 2]
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
    if "--new" in sys.argv:                  # every string this script adds, and any existing value it changes
        for t in _TABLES:
            for k, v in getattr(F, t).items():
                if k not in _BEFORE[t]:
                    v = "(frame)" if callable(v) else (v[0] if isinstance(v, tuple) else v)
                    print(f"- {k} = {v}  [{t}]")
                elif _BEFORE[t][k] != v:
                    print(f"CHANGED [{t}] {k}")
        for k, v in NEW.items():
            print(f"- {k} = {v}  [NEW]")
