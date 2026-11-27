"""Burmese zero-shot of pi-6 ch. 3 (Āyatanayamaka, «အာရုံခံ နယ်ပယ်များကို အတွဲလိုက် မေးဖြေခြင်း»): 3-01 … 3-06.

usage: python3 -I -X utf8 make_ch3.py [3-01 3-02 …] [--misses]   (no chapter = all six)
Every line is generated from the Pāli by the frames and tables of my6_formulas.py (imported, never edited; its tables
are extended IN MEMORY here only) plus the āyatana tables, person / place extensions, fragment, paṇṇatti-niddesa and
pariññā frames and the NOTES table of this script. Reused values are read from / checked against the FINAL pi-1 … pi-5
rails texts at import (F.items / F.witness). A sentence that no frame matches stops the run (F.Miss): nothing is
guessed. Each line is checked against its Pāli (line_check, copied from make_sample.py); a chapter file is written only
when every line passed. --misses lists unmatched lines and writes nothing. New strings are logged in notes-ch3.md.
"""
import pathlib
import re
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import my6_formulas as F  # noqa: E402

W = F.W
ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-6_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters"
NAMES_OUT = [f"3-0{i}-ayatanayamaka.md" for i in range(1, 7)]
C, END, PE = F.C, F.END, F.PE

# ===================================================================================== āyatana terms (pi-2 ^2-154)
AY_H, AY = F.items("2", "^2-154")            # «အာရုံခံ နယ်ပယ် ဆယ့်နှစ်ပါး», {cakkhāyatanaṃ: «မျက်စိ အာရုံခံ နယ်ပယ်», …}
AYATANA = W("1", "^1-M2-122", "āyatan", "အာရုံခံ နယ်ပယ်", key="āyatana")
AYATANA_PL = W("1", "^1-1342", "āyatanānaṃ", AYATANA + "တို့", key="āyatanā (pl.)")
for k, v in AY.items():
    F.add_subject(k, v)                       # pavattivāra subjects
    F.add_term(k, v, False)                   # paṇṇattivāra terms
# bare words (paṇṇattivāra): the first member of each base name; rūpaṃ = «ရုပ်» (sample, pi-1 ^1-1044), not the
# visible-form «အဆင်းအရောင်» (the text argues that other rūpa is rūpa but not the visible-form base)
BARE = {"cakkhu": "cakkhāyatanaṃ", "sotaṃ": "sotāyatanaṃ", "ghānaṃ": "ghānāyatanaṃ", "jivhā": "jivhāyatanaṃ",
        "kāyo": "kāyāyatanaṃ", "saddo": "saddāyatanaṃ", "gandho": "gandhāyatanaṃ", "raso": "rasāyatanaṃ",
        "phoṭṭhabbo": "phoṭṭhabbāyatanaṃ", "mano": "manāyatanaṃ", "dhammo": "dhammāyatanaṃ"}
for k, v in BARE.items():
    my = AY[v][: -len(" " + AYATANA)]
    F.add_term(k, my, False)
W("2", "^2-154", "cakkhāyatanaṃ", "မျက်စိ အာရုံခံ နယ်ပယ်", key="cakkhu (bare) «မျက်စိ»")
W("1", "^1-M1-1", "dhammā", F.DHAMMA, key="dhammo (bare) «သဘောတရား»")
F.add_term("āyatanaṃ", AYATANA, False)
F.add_term("āyatanā", AYATANA_PL, True)
F.PT_ACC.update({"cakkhuṃ": "cakkhu", "cakkhū": "cakkhu", "jivhaṃ": "jivhā", "manaṃ": "mano", "kāyaṃ": "kāyo",
                 "gandhaṃ": "gandho", "rasaṃ": "raso", "saddaṃ": "saddo", "phoṭṭhabbaṃ": "phoṭṭhabbo",
                 "dhammaṃ": "dhammo",
                 "sotāyanaṃ": "sotāyatanaṃ"})      # source slip «sotāyananti» (3-01 ^6-3-13)

# special subjects of the paṇṇatti niddesa (all plural: two or three things named)
DIBBA_C = W("5", "^5-11-7-1-0", "Dibbacakkhu", "နတ်မျက်စိ")                     # dibbacakkhu (pi-5)
PANNA_C = W("5", "^5-374", "paññācakkhu", "ပညာမျက်စိ")                       # paññācakkhu (pi-5)
DIBBA_S = W("5", "^5-11-8-1-0", "Dibbasot", "နတ်နား")                       # dibbasota (pi-5)
TANHA = W("1", "^1-1065", "taṇhā", "တပ်မက်မှု", key="taṇhā")                # taṇhā (pi-1 … pi-5 «တပ်မက်မှု»)
STREAM = W("4", "^4-M-10", "Anusot", "ရေစီး", key="sota (stream)")             # sota = stream (pi-4 anusota)
SILA = W("1", "^1-M2-135", "sīla", "သီလ")
SAMADHI = W("1", "^1-1", "samādhi", "သမာဓိ")
PANNA = W("2", "^2-796", "paññā", "ပညာ")
ATTHA = W("2", "^2-718", "atthapaṭisambhid", "အနက်", key="attha")
DHAMMA_T = W("4", "^4-94", "dhammadesan", "တရား", key="dhamma (teaching)")
VIMUTTI = W("1", "^1-M2-141", "vimutti", "လွတ်မြောက်မှု")
GANDHA, RASA = F.PT["gandho"][0], F.PT["raso"][0]
AND = F.AND
SPEC = {
    "Dibbacakkhu paññācakkhu": f"{DIBBA_C}{AND} {PANNA_C}",
    "Dibbasotaṃ taṇhāsotaṃ": f"{DIBBA_S}{AND} {TANHA} {STREAM}",
    "Sīlagandho samādhigandho paññāgandho": f"{SILA}၏ {GANDHA}{C} {SAMADHI}၏ {GANDHA}{AND} {PANNA}၏ {GANDHA}",
    "Attharaso dhammaraso vimuttiraso": f"{ATTHA}၏ {RASA}{C} {DHAMMA_T}၏ {RASA}{AND} {VIMUTTI}၏ {RASA}",
}
# «sotaṃ» said of the divine ear and the stream of craving: the Pāli word play (sota = ear and stream), NEW
SOTA_PUN = f"“သောတ” ({F.PT['sotaṃ'][0]} သို့မဟုတ် {STREAM})"
THEY = "တို့"                                  # «A နှင့် Bတို့သည်» (joined subjects)

# ===================================================================================== places and persons
F.PLACES["kāmāvacara"] = "ကာမဘုံ"                     # the sense sphere as a place (style core plane names)
F.PLACES["rūpāvacara"] = "သိမ်မွေ့သော ရုပ်ဘုံ"          # fine-material sphere (style; pi-1 «သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော»)
F.PLACES["arūpāvacara"] = F.PLACES["arūpa"]          # immaterial sphere = «ရုပ်မရှိသော ဘုံ» (pi-1 / pi-2)
W("1", "^1-M2-93", "kāmāvacarā", "ကာမဘုံ", key="kāmāvacara (place)")
W("1", "^1-M2-94", "rūpāvacarā", "သိမ်မွေ့သော ရုပ်ဘုံ", key="rūpāvacara (place)")
W("1", "^1-M2-95", "arūpāvacarā", "ရုပ်မရှိသော ဘုံ", key="arūpāvacara (place)")
# sa-X-ka / a-X-ka beings: «X ရှိလျက်» / «X မရှိဘဲ» before the place and the participle (NEW)
ATTR = {"cakkhuk": F.PT["cakkhu"][0], "sotak": F.PT["sotaṃ"][0], "ghānak": F.PT["ghānaṃ"][0],
        "rūpak": F.RUPA_W, "cittak": W("1", "^1-6", "cittaṃ", "စိတ်", key="citta")}
ATTR_RE = re.compile(r"^(sa|a)(" + "|".join(ATTR) + r")ānaṃ$")
WITH, WITHOUT = "ရှိလျက်", "မရှိဘဲ"


def attr_my(w):
    m = ATTR_RE.match(w.lower())
    if not m:
        return None
    return f"{ATTR[m[2]]} {WITH if m[1] == 'sa' else WITHOUT}"


_ORIG_ONE_GROUP = F._one_group


def one_group(toks):
    """F._one_group plus the «sacakkhukānaṃ / acakkhukānaṃ …» attributes before place and participle."""
    j = 0
    while j < len(toks) and toks[j].lower() in ("sabbesaṃ", "itaresaṃ"):
        j += 1
    if not (j < len(toks) and attr_my(toks[j])):
        return _ORIG_ONE_GROUP(toks)
    allf = othf = False
    if toks[0].lower() == "sabbesaṃ":
        allf = True
        toks.pop(0)
    if toks[0].lower() == "itaresaṃ":
        othf = True
        toks.pop(0)
    attrs = []
    while toks and attr_my(toks[0]):
        attrs.append(attr_my(toks.pop(0)))
    places, case = [], None
    while toks and F._place_form(toks[0]) and F._place_form(toks[0])[1] in ("acc", "abl") \
            and case in (None, F._place_form(toks[0])[1]):
        k, case = F._place_form(toks.pop(0))
        places.append(k)
    if not toks or toks[0].lower() not in ("upapajjantānaṃ", "cavantānaṃ"):
        raise F.Miss("attribute without participle: " + " ".join(toks))
    head = toks.pop(0).lower()
    verb, cw = F.PART[head]
    if case and case != {"upapajjantānaṃ": "acc", "cavantānaṃ": "abl"}[head]:
        raise F.Miss("place case")
    loc = (F._join_places(places) + cw + " ") if places else ""
    a = " ".join(attrs) + " "
    if othf:
        return f"{a}{loc}{verb} {F.OTHERS}"
    return f"{a}{loc}{verb}{F.ALL_OF if allf else F.THEM}"


F._one_group = one_group

# «… ye (ca) <places acc> upapajjitvā parinibbāyissanti [tesaṃ upapajjantānaṃ / cavantānaṃ]»
YE_RE = re.compile(r"(?:^|\s)(?:ye ca|ye) ((?:\w+aṃ )+)upapajjitvā parinibbāyissanti"
                   r"(?: tesaṃ (upapajjantānaṃ|cavantānaṃ))?$", re.I)
AMONG = "အနက်"                                   # «… သူတို့အနက် …» (among them) (pi-2 «…တို့အနက်»)
_ORIG_GROUP = F.group_my


def ye_atom(places, part=None):
    pl = F._join_places([F._place_form(w)[0] for w in places.split()])
    atom = f"{pl}{F.LOC} ပြန်လည် ဖြစ်ပေါ်ပြီး ပရိနိဗ္ဗာန် ပြုမည့်{F.THEM}"
    if part:
        atom += f"{AMONG} {F.PART[part.lower()][0]}{F.THEM}"
    return atom


assert ye_atom("arūpaṃ ") == F.GROUP_ATOMS["ye arūpaṃ upapajjitvā parinibbāyissanti"]


def group_my(g):
    g = g.strip()
    m = YE_RE.search(g)
    if not m:
        return _ORIG_GROUP(g)
    atom = ye_atom(m[1], m[2])
    pre = g[: m.start()].strip()
    if not pre:
        return atom
    first = _ORIG_GROUP(pre)
    n_pre = first.count(f"{F.AND} ") + first.count(f"{C} ")
    sep = f"{C} " if n_pre else f"{F.AND} "
    if n_pre:            # «A၊ Bနှင့် C» -> «A၊ B၊ Cနှင့် (ye …)»
        first = first.replace(f"{F.AND} ", f"{C} ")
        return f"{first}{F.AND} {atom}"
    return f"{first}{sep}{atom}"


F.group_my = group_my

# ===================================================================================== headings, colophons, notes
VARA, ALIKE = F.VARA, F.ALIKE
PARINNA = W("2", "^2-1029", "pariññāya", "ပိုင်းခြား သိ", key="pariññā / parijānāti") + "ခြင်း"
UPP_NIR = f"{F.UPPADA}{AND} {F.NIRODHA}"
F.H.update({
    "Suddhāyatanavāro": F.vara(f"{F.SUDDHA} {AYATANA}", False),
    "Suddhāyatanamūlacakkavāro": F.vara(f"{F.SUDDHA} {AYATANA}{F.BASED} {F.CAKKA}", False),
    "Pavatti 3. uppādanirodhavāro": f"{F.PAVATTI} 3. {F.vara(UPP_NIR)}",
    "Pariññāvāro": F.vara(PARINNA),
})
COLO = dict(F.COLO)
COLO.update({
    "Uppādavāro.": f"{F.vara(F.UPPADA)}{END}",
    "Nirodhavāro.": f"{F.vara(F.NIRODHA)}{END}",
    "Uppādanirodhavāro.": f"{F.vara(UPP_NIR)}{END}",
    "Pavattivāro niṭṭhito.": F.finished(F.vara(F.PAVATTI)),
    "Pariññāvāro.": f"{F.vara(PARINNA)}{END}",
})
F.SIGLA["sī"] = "Sī."                      # source slip «(sī syā. ka.)» without the dot (3-06)


def variants(inner):
    """'a (syā.), b (sī. ka.)' -> «[ပါဌ်ကွဲ (Syā.): a၊ (Sī., Ka.): b]»; one reading -> F.variant()."""
    parts = re.findall(r"(.+?) \(([^)]*)\)(?:, |$)", inner.strip())
    if len(parts) <= 1:
        return F.variant(inner)
    segs = [f"({', '.join(F.SIGLA[s] for s in sig.split())}): {r}" for r, sig in parts]
    return f"[{F.VAR_P} " + f"{C} ".join(segs) + "]"


YASSAKA = f"“{F.CL['yassa'][0]}” အပိုင်း"                    # yassaka: the «yassa» part (NEW)
YATTHAKA = f"“{F.CL['yattha'][0]}” အပိုင်း"                  # yatthaka (NEW)
YY_KA = f"“{F.CL['yassa yattha'][0]}” အပိုင်း"               # yassayatthaka (NEW)
PUCCHA = W("5", "^5-1", "pucchā", "အမေး", key="pucchā")                    # pucchā (pi-5 termbase «အမေး»)
SAME = "တူညီ"                                               # sadisa
VITTH = W("5", "^5-839", "vitthāretabb", "အကျယ် ချဲ့", key="vitthāreti")      # vitthāreti (pi-5)
VIBH = W("2", "^2-33", "vibhaj", "ခွဲခြား", key="vibhajati") + " ပြ"           # vibhajati (pi-2 «ခွဲခြားပြ»)
T = F.TIMES
ALSO = "လည်း"
CAKKA_BIND = f"{F.CAKKA}ကို အပြည့်အစုံ ဖွဲ့ရမည်"              # cakkaṃ bandhitabbaṃ (NEW)
NOTES = {
    "(Cakkaṃ bandhitabbaṃ)": f"({CAKKA_BIND})",
    "(Ekekapadamūlakaṃ cakkaṃ bandhitabbaṃ asammohantena)":
        f"(စကားလုံး တစ်လုံးစီ{F.BASED} {F.CAKKA}ကို မရောထွေးစေဘဲ အပြည့်အစုံ ဖွဲ့ရမည်)",
    "(Cakkaṃ bandhantena sabbattha āmantāti kātabbaṃ)":
        f"({F.CAKKA}ကို ဖွဲ့သောအခါ နေရာတိုင်း၌ “{F.YES[:-1]}” ဟု ဖြေရမည်)",
    "(Saṃkhittaṃ)": "(အကျဉ်း ဖော်ပြထားသည်)",
    "(saṃkhittaṃ yassakasadisaṃ [yassakampi sadisaṃ (sī.), yassekasadisaṃ (syā.)] )":
        f"(အကျဉ်း ဖော်ပြထားသည်၊ {YASSAKA}နှင့် {SAME}သည် "
        + variants("yassakampi sadisaṃ (sī.), yassekasadisaṃ (syā.)") + " )",
    "(Yattha ghānāyatanaṃ uppajjati tattha manāyatanaṃ dhammāyatanañca ekasadisaṃ, nānaṃ natthi, upari pana "
    "vārasaṅkhepo [uparivāre saṅkhepo (syā.), uparivāre saṅkhepaṃ (sī. ka.)] tīti jānitabbaṃ.)":
        f"({F.CL['yattha'][0]} {AY['ghānāyatanaṃ']} {F.my_verb('uppajj', 'pres', form='cl')}{C} {F.CL['yattha'][1]} "
        f"{AY['manāyatanaṃ']}{AND} {AY['dhammāyatanaṃ']}{THEY}သည် တစ်ထပ်တည်း {SAME}ကြသည်{C} ကွဲပြားခြင်း မရှိ{C} "
        f"သို့သော် နောက်ပိုင်း ဖော်ပြချက်တို့၌ အကျဉ်း ဖော်ပြထားသည် "
        + variants("uparivāre saṅkhepo (syā.), uparivāre saṅkhepaṃ (sī. ka.)") + f" ဟု သိရမည်{END})",
    "(yatthakaṃ paccuppannepi atītepi anāgatepi paccuppannātītepi paccuppannānāgatepi atītānāgatepi sabbattha "
    "sadisaṃ, uppajjati uppajjitthāti nāmaṃ atirekaṃ kātabbaṃ)":
        f"({YATTHAKA}သည် {T['Paccuppanna']}၌{ALSO}{C} {T['Atīta']}၌{ALSO}{C} {T['Anāgata']}၌{ALSO}{C} "
        f"{T['Paccuppanna']}{AND} {T['Atīta']}၌{ALSO}{C} {T['Paccuppanna']}{AND} {T['Anāgata']}၌{ALSO}{C} "
        f"{T['Atīta']}{AND} {T['Anāgata']}၌{ALSO} နေရာတိုင်း၌ {SAME}သည်{C} “{F.my_verb('uppajj', 'pres')}”{C} "
        f"“{F.my_verb('uppajj', 'past')}” ဟူသော စကားကိုသာ ပိုမို ထည့်ရမည်)",
    "(tassa manāyatanañca dhammāyatanañca sadisaṃ, ime dve sadisāyeva honti)":
        f"({F.FT['tassa']} {AY['manāyatanaṃ']}{AND} {AY['dhammāyatanaṃ']}{THEY}သည် {SAME}ကြသည်{C} "
        f"ဤနှစ်ပါးတို့သည် {SAME}ကြသည်သာ ဖြစ်သည်)",
    "(uppādepi nirodhepi uppādanirodhepi yatthakaṃ sabbattha sadisaṃ)":
        f"({F.UPPADA}၌{ALSO}{C} {F.NIRODHA}၌{ALSO}{C} {UPP_NIR}၌{ALSO} {YATTHAKA}သည် နေရာတိုင်း၌ {SAME}သည်)",
    "(Yassa yatthakampi sadisaṃ vitthāretabbaṃ)": f"({YY_KA}ကို{ALSO} ထို့အတူ {VITTH}ရမည်)",
    "(yassa yatthakampi yassakasadisaṃ)": f"({YY_KA}သည်{ALSO} {YASSAKA}နှင့် {SAME}သည်)",
    "(Uppādavārepi nirodhavārepi uppādanirodhavārepi atītā pucchā anulomampi paccanīkampi [paccaniyampi (sī. "
    "syā. ka.)] sadisaṃ.)":
        f"({F.vara(F.UPPADA)}၌{ALSO}{C} {F.vara(F.NIRODHA)}၌{ALSO}{C} {F.vara(UPP_NIR)}၌{ALSO} {T['Atīta']} "
        f"{PUCCHA}တို့သည် {F.ANULOMA}၌{ALSO}{C} {F.PACCANIKA}၌{ALSO} " + variants("paccaniyampi (sī. syā. ka.)")
        + f" {SAME}ကြသည်{END})",
    "(Yathā uppādavāre yassa yatthake anāgatā pucchā vitthāritā, evaṃ nirodhepi vitthāretabbā)":
        f"({F.vara(F.UPPADA)}၌ {YY_KA}တွင် {T['Anāgata']} {PUCCHA}တို့ကို {VITTH}ထားသကဲ့သို့ "
        f"{F.NIRODHA}၌{ALSO} {VITTH}ရမည်)",
    "(yathā paccuppannātītepi tividhaṃ vitthāritaṃ evaṃ idampi vitthāretabbaṃ)":
        f"({T['Paccuppanna']}{AND} {T['Atīta']}၌ သုံးမျိုး {VITTH}ထားသကဲ့သို့ ဤအပိုင်းကို{ALSO} {VITTH}ရမည်)",
    "(yatthakaṃ noti na kātabbaṃ, yatthakaṃ itaresaṃ yatthakānaṃ sadisaṃ kātabbaṃ, yatthakaṃ tīsupi vāresu "
    "sadisaṃ)":
        f"({YATTHAKA}၌ “{F.NO[:-1]}” ဟု မဖြေရ{C} {YATTHAKA}ကို အခြား “{F.CL['yattha'][0]}” အပိုင်းတို့နှင့် "
        f"{SAME}အောင် ပြုရမည်{C} {YATTHAKA}သည် ဖော်ပြချက် သုံးပါးလုံး၌ {SAME}သည်)",
    "(Yassakampi yassayatthakampi sadisaṃ)": f"({YASSAKA}{AND} {YY_KA}{THEY}သည်{ALSO} {SAME}ကြသည်)",
    "(Atītā pucchā uppādepi nirodhepi uppādanirodhepi anulomampi paccanīkampi sadisaṃ)":
        f"({T['Atīta']} {PUCCHA}တို့သည် {F.UPPADA}၌{ALSO}{C} {F.NIRODHA}၌{ALSO}{C} {UPP_NIR}၌{ALSO}{C} "
        f"{F.ANULOMA}၌{ALSO}{C} {F.PACCANIKA}၌{ALSO} {SAME}ကြသည်)",
    "(Yathā uppādavāre paccuppannātītā pucchā vibhattā evaṃ uppādanirodhepi paccuppannātītā pucchā anulomampi "
    "paccanīkampi vibhajitabbā [vibhajitabbaṃ (sī syā. ka.)] )":
        f"({F.vara(F.UPPADA)}၌ {T['Paccuppanna']}{AND} {T['Atīta']} {PUCCHA}တို့ကို {VIBH}ထားသကဲ့သို့ "
        f"{UPP_NIR}၌{ALSO} {T['Paccuppanna']}{AND} {T['Atīta']} {PUCCHA}တို့ကို {F.ANULOMA}{C} {F.PACCANIKA} "
        f"{VIBH}ရမည် " + variants("vibhajitabbaṃ (sī syā. ka.)") + " )",
    "(Yathā nirodhavāre atītānāgatā [atītenānāgatā (syā.)] pucchā yassakampi yatthakampi yassayatthakampi "
    "anulomampi paccanīkampi vibhattaṃ, evaṃ uppādanirodhepi atītānāgatā pucchā vibhajitabbā.)":
        f"({F.vara(F.NIRODHA)}၌ {T['Atīta']}{AND} {T['Anāgata']} " + variants("atītenānāgatā (syā.)")
        + f" {PUCCHA}တို့ကို {YASSAKA}{C} {YATTHAKA}{C} {YY_KA}{C} {F.ANULOMA}{C} {F.PACCANIKA}၌ "
        f"{VIBH}ထားသကဲ့သို့ {UPP_NIR}၌{ALSO} {T['Atīta']}{AND} {T['Anāgata']} {PUCCHA}တို့ကို {VIBH}ရမည်{END})",
}
for st in ("cakkh", "ghān", "rūp", "man"):
    pal = st + "āyatanaṃ"
    NOTES[f"({pal[0].upper()}{pal[1:-1]}mūlakaṃ)"] = f"({AY[pal]}{F.BASED})"    # (Cakkhāyatanamūlakaṃ)

# ===================================================================================== source slips (read as written)
SLIPS = [
    ("uppajjittharūpāyatanañca", "uppajjittha rūpāyatanañca"),        # 3-01 ^6-3-43 (missing space)
    ("rūpāyatanañca ca uppajjittha", "rūpāyatanañca uppajjittha"),    # 3-02 (doubled ca; one «လည်း»)
    ("na nirujjhatī ti…", "na nirujjhatīti…"),                       # 3-04 ^6-3-131
    ("parinibbāntānaṃ", "parinibbantānaṃ"),                          # 3-05 ^6-3-172
    ("manāyatana…pe…", "manāyatanaṃ…pe…"),                           # 3-05 ^6-3-186
    ("arūpānaṃ tasaṃ tattha", "arūpānaṃ tesaṃ tattha"),               # 3-06 (tasaṃ for tesaṃ)
    ("no ca tesaṃ ghānāyatanaṃ upapajjissati", "no ca tesaṃ ghānāyatanaṃ uppajjissati"),   # 3-06 (upapajj-)
    ("yassa =93 yattha", "yassa yattha"),                            # 3-03 ^6-3-118 (stray «=93», kept: SLIP_POST)
    ("na nirujjhissati, parinibbantānaṃ asaññasattānaṃ",              # 3-04 ^6-3-148: «,» for «.» (comma kept)
     "na nirujjhissati. Parinibbantānaṃ asaññasattānaṃ"),
]
# output repairs for the slips whose Pāli mark is kept in the Burmese (Pāli key -> (Burmese before, after))
SLIP_POST = {
    "yassa =93 yattha": (f"{F.CL['yassa'][0]} {F.CL['yattha'][0]}", f"{F.CL['yassa'][0]} =93 {F.CL['yattha'][0]}"),
    "na nirujjhissati, parinibbantānaṃ": (f"{F.NOT_SO}{END} {F.PART['parinibbantānaṃ'][0]}",
                                          f"{F.NOT_SO}{C} {F.PART['parinibbantānaṃ'][0]}"),
}


def unslip(s):
    for a, b in SLIPS:
        s = s.replace(a, b)
    return s


# ===================================================================================== paṇṇatti frames
END_R = r"(?P<end>[?.]?)"
VAR_R = r"(?P<v> ⟦\d+⟧)?"
SPEC_R = "(?P<s>" + "|".join(SPEC) + ")"
P_LIST = re.compile(r"^Dvādasāyatanāni – (?P<l>.+)\.$")
P1 = re.compile(rf"^{SPEC_R} (?P<a>\S+), na (?P<b>\S+?){END_R}$")
P4 = re.compile(rf"^{SPEC_R} na (?P<b>\S+), (?P<a>\S+?){END_R}$")
P1B = re.compile(rf"^(?P<s>\S+) ṭhapetvā (?P<av>avaseso|avasesaṃ|avasesā) (?P<a>\S+){VAR_R}, na (?P<b>\S+?){END_R}$")
P4B = re.compile(rf"^(?P<s>\S+) ṭhapetvā (?P<av>avaseso|avasesaṃ|avasesā) (?:(?P<k>\S+) )?na (?P<b>\S+), "
                 rf"(?P<a>\S+?){END_R}$")
P2 = re.compile(rf"^(?P<x>\S+) (?P<a>\S+?)(?P<ce>ñceva| ceva) (?P<b>\S+?)(?P<bc>ñca| ca){END_R}$")
P3 = re.compile(rf"^[Aa]vasesā (?P<a>\S+){VAR_R} na (?P<b>\S+?){END_R}$")
P5 = re.compile(rf"^(?P<a>\S+?ñca|\S+ ca) (?P<b>\S+?ñca|\S+ ca) ṭhapetvā (?P<av>avasesaṃ|avasesā|avaseso){VAR_R} "
                rf"na ceva (?P<a2>\S+) na ca (?P<b2>\S+?){END_R}$")
P_THAP = re.compile(rf"^(?P<s>\S+) ṭhapetvā{END_R}$")              # fragment «Sotaṃ ṭhapetvā»
P_NACA = re.compile(rf"^na ca (?P<b>\S+?){END_R}$")                # fragment «na ca āyatanā»
P_NA = re.compile(rf"^na (?P<b>\S+?){END_R}$")                     # fragment «na cakkhāyatanaṃ» (… avasesā āyatanā na X)
P_Q = re.compile(rf"^(?P<n1>na )?(?P<a>\S+) (?P<n2>na )?(?P<b>\S+?){END_R}$")
P_ONE = re.compile(rf"^(?P<a>\S+?){END_R}$")                       # fragment «ghānaṃ» (a term of a listed question)
THING, THING_PL = F.THING, F.THING + "များ"
BE, ISNT = F.BE, F.NEGV[F.BE]


def tm(w):
    return F.term(w)


def endm(e, q=False):
    return END if e else ""


def avas_noun(av):
    """avaseso / avasesaṃ (sg.) = «ကြွင်းကျန်သော အရာ»; avasesā (pl.) = «ကြွင်းကျန်သော အရာများ» (sample)."""
    return (F.AVASESA_N, True) if av == "avasesā" else (f"{F.AVASESA} {THING}", False)


def ko(pl):
    return "ကြ" if pl else ""


def leave(*ts):
    """«Aနှင့် Bကို ချန်ထား၍၊» (as F.leave)."""
    return f"{AND} ".join(t[0] for t in ts) + f"ကို {F.THAPETVA}{C}"


def pannatti(s):
    m = P_LIST.match(s)
    if m:
        its = [AY[w.strip(",")] for w in m["l"].split()]
        return f"{AY_H} – " + f"{C} ".join(its) + END
    m = P1.match(s)
    if m:
        S, A, B = SPEC[m["s"]], tm(m["a"]), tm(m["b"])
        a = SOTA_PUN if m["s"].startswith("Dibbasota") else A[0]
        return f"{S}{THEY}သည် {a} {BE}ကြသည်{C} {B[0]} {ISNT}ကြ{endm(m['end'])}"
    m = P4.match(s)
    if m:
        S, A, B = SPEC[m["s"]], tm(m["a"]), tm(m["b"])
        a = SOTA_PUN if m["s"].startswith("Dibbasota") else A[0]
        return f"{S}{THEY}သည် {B[0]} {ISNT}ကြ{C} {a} {BE}ကြသည်{endm(m['end'])}"
    m = P1B.match(s)
    if m:
        S, A, B = tm(m["s"]), tm(m["a"]), tm(m["b"])
        n, pl = avas_noun(m["av"])
        return f"{leave(S)} {n}သည် {A[0]}{m['v'] or ''} {BE}{ko(pl)}သည်{C} {B[0]} {ISNT}{ko(pl)}{endm(m['end'])}"
    m = P4B.match(s)
    if m:
        S, A, B = tm(m["s"]), tm(m["a"]), tm(m["b"])
        if m["k"]:
            K = tm(m["k"])
            n, pl = f"{F.AVASESA} {K[0]}", K[1]
        else:
            n, pl = avas_noun(m["av"])
        return f"{leave(S)} {n}သည် {B[0]} {ISNT}{ko(pl)}{C} {A[0]} {BE}{ko(pl)}သည်{endm(m['end'])}"
    m = P2.match(s)
    if m:
        X = tm(m["x"])
        A = tm(m["a"] + ("ñceva" if m["ce"] == "ñceva" else ""))
        B = tm(m["b"] + ("ñca" if m["bc"] == "ñca" else ""))
        return f"{X[0]}သည် {A[0]}{ALSO} {BE}{C} {B[0]}{ALSO} {BE}{ko(X[1])}သည်{endm(m['end'])}"
    m = P3.match(s)
    if m:
        A, B = tm(m["a"]), tm(m["b"])
        return f"{F.AVASESA} {A[0]}သည်{m['v'] or ''} {B[0]} {ISNT}{ko(A[1])}{endm(m['end'])}"
    m = P5.match(s)
    if m:
        A, B, A2, B2 = (tm(m[k]) for k in ("a", "b", "a2", "b2"))
        n, pl = avas_noun(m["av"])
        return (f"{leave(A, B)} {n}သည်{m['v'] or ''} {A2[0]}{ALSO} {ISNT}{C} {B2[0]}{ALSO} {ISNT}"
                f"{endm(m['end'])}")
    m = P_THAP.match(s)
    if m:
        return f"{tm(m['s'])[0]}ကို {F.THAPETVA}{endm(m['end'])}"
    m = P_NACA.match(s)
    if m:
        return f"{tm(m['b'])[0]}{ALSO} {ISNT}{endm(m['end'])}"
    m = P_NA.match(s)
    if m:
        try:
            B = tm(m["b"])
            return f"{B[0]} {ISNT}ကြ{endm(m['end'])}"      # the end of «avasesā āyatanā na X» (plural subject)
        except F.Miss:
            pass
    s2 = re.sub(r"(?:(?<= )|^)([Nn])āyatan", lambda x: x[1].lower() + "a āyatan", s)   # nāyatanā = na āyatanā
    s2 = s2[0].lower() + s2[1:]
    m = P_Q.match(s2)
    if m and bool(m["n1"]) == bool(m["n2"]):
        try:
            r = F.q_term(m["a"], m["b"], bool(m["n1"]))
            return r if m["end"] else r[:-1]
        except F.Miss:
            pass
    m = P_ONE.match(s)
    if m:
        try:
            return tm(m["a"])[0] + endm(m["end"])
        except F.Miss:
            pass
    return None


# ===================================================================================== pariññā frames
F.VERB["parijān"] = "သိ"                    # «ပိုင်းခြား သိ» (pi-5 ^5-390 parijānāti); the «မ» goes before «သိ»
PJ_PRE = "ပိုင်းခြား "
W("5", "^5-390", "parijānāti", "ပိုင်းခြား သိသည်", key="parijānāti")
PJ_FORMS = {"parijānāti": ("pres", False), "parijānātīti": ("pres", True), "parijānanti": ("pres", False),
            "parijānittha": ("past", False), "parijānitthāti": ("past", True),
            "parijānissati": ("fut", False), "parijānissatīti": ("fut", True), "parijānissanti": ("fut", False)}
PJ_RE = r"(?:na )?parijān\w+"


def pj_parse(w):
    neg = w.startswith("na ")
    tense, q = PJ_FORMS[w[3:] if neg else w]
    return tense, neg, q


def pj(w, form="stmt", pl=False):
    tense, neg, _ = pj_parse(w)
    return PJ_PRE + F.my_verb("parijān", tense, neg, form, pl)


def pj_not_so(w, pl=False):
    """«no ca … na parijān…»: «ပိုင်းခြား မသိ(ခဲ့)(ကြ)သည်ကား မဟုတ်» (as F.not_so)."""
    tense, _, _ = pj_parse(w)
    return PJ_PRE + F.my_verb("parijān", tense, True, pl=pl) + ("" if tense == "fut" else "သည်") + F.NOT_SO


ARAHA = W("4", "^4-M-7", "Arahā", "ရဟန္တာ", key="arahā")                    # arahā (termbases «ရဟန္တာ»)
W("2", "^2-1029", "agga", "အမြတ်ဆုံး", key="agga")
W("2", "^2-809", "samaṅgī", "ပြည့်စုံသော", key="samaṅgī")
W("1", "^1-M1-16", "magg", "မဂ်", key="magga")
W("2", "^2-768", "paṭilabh", "ရရှိ", key="paṭilabhati")
W("1", "^1-1007", "puthujjan", "ပုထုဇဉ်", key="puthujjana")
W("1", "^1-1051", "puggalā", "ပုဂ္ဂိုလ်", key="puggalā")
AGGA_SAM = "အမြတ်ဆုံး မဂ်နှင့် ပြည့်စုံသူ"     # aggamaggasamaṅgī (agga «အမြတ်ဆုံး», magga «မဂ်», samaṅgī «ပြည့်စုံသော»)
PUTHU_NO = f"မဂ်ကို မရရှိမည့် ပုထုဇဉ်တို့"   # ye ca puthujjanā maggaṃ na paṭilabhissanti (te)
PUGGALA_PL = f"{F.PUGGALA}တို့"
# Pāli subject -> (Burmese subject, plural)
PJ_SUBJ = {
    "Arahā": (ARAHA, False),
    "Aggamaggasamaṅgī": (AGGA_SAM, False),
    "Aggamaggasamaṅgiñca arahantañca ṭhapetvā avasesā puggalā":
        (f"{AGGA_SAM}{AND} {ARAHA}ကို {F.THAPETVA}{C} {F.AVASESA} {PUGGALA_PL}", True),
    "Ye maggaṃ paṭilabhissanti te": (f"မဂ်ကို ရရှိမည့်{F.THEM}", True),
    "Arahā ye ca puthujjanā maggaṃ na paṭilabhissanti te": (f"{ARAHA}{AND} {PUTHU_NO}", True),
    "Aggamaggasamaṅgī ye ca puthujjanā maggaṃ na paṭilabhissanti te": (f"{AGGA_SAM}{AND} {PUTHU_NO}", True),
}
PJ_SUBJ_R = "(?P<who>" + "|".join(re.escape(k) for k in sorted(PJ_SUBJ, key=len, reverse=True)) + ")"
PJ_Q = re.compile(rf"^(?P<cl>yo vā pana|yo) (?P<x>\S+) (?P<v1>{PJ_RE}) so (?P<y>\S+) (?P<v2>{PJ_RE})\?$")
PJ_BUT = re.compile(rf"^{PJ_SUBJ_R} (?P<x>\S+) (?P<v1>{PJ_RE}), no ca (?P<y>\S+) (?P<v2>{PJ_RE})\.$")
PJ_BOTH = re.compile(rf"^{PJ_SUBJ_R} (?P<x>\S+?)ñca (?P<v1>{PJ_RE}) (?P<y>\S+?)ñca (?P<v2>{PJ_RE})\.$")
WHO_S = ("အကြင်သူသည်", "ထိုသူသည်")              # yo … so … (as yassa … tassa «အကြင်သူအား … ထိုသူအား»)
OBJ = "ကို"


def pariñña(s):
    m = PJ_Q.match(s)
    if m:
        pre = F.VA_PANA + " " if m["cl"] == "yo vā pana" else ""
        return (f"{pre}{WHO_S[0]} {F.subj(m['x'])}{OBJ} {pj(m['v1'], 'cl')}{C} {WHO_S[1]} {F.subj(m['y'])}{OBJ} "
                f"{pj(m['v2'], 'q')}{END}")
    m = PJ_BUT.match(s)
    if m:
        S, pl = PJ_SUBJ[m["who"]]
        neg2 = pj_parse(m["v2"])[1]
        v2 = pj_not_so(m["v2"], pl) if neg2 else PJ_PRE + F.my_verb("parijān", pj_parse(m["v2"])[0], True, pl=pl)
        return (f"{S}သည် {F.subj(m['x'])}{OBJ} {pj(m['v1'], pl=pl)}{C} {F.BUT} {F.subj(m['y'])}{OBJ} {v2}{END}")
    m = PJ_BOTH.match(s)
    if m:
        S, pl = PJ_SUBJ[m["who"]]
        x, y = F.subj(m["x"] + "ṃ"), F.subj(m["y"] + "ṃ")
        return f"{S}သည် {x}{OBJ}{ALSO} {pj(m['v1'], pl=pl)}{C} {y}{OBJ}{ALSO} {pj(m['v2'], pl=pl)}{END}"
    return None


# ===================================================================================== pavatti sentences and fragments
A_BOTH2 = re.compile(rf"^(?P<who>.+?) (?P<pro>{F.PROR}) (?P<x>\S+?)ñca (?P<v1>{F.VB}),? (?P<y>\S+?)ñca "
                     rf"(?P<v2>{F.VB})\.$")


def pavatti(s):
    r = F.pavatti_sentence(s)
    if r:
        return r
    m = A_BOTH2.match(s)
    if m:
        return F.a_both(m["who"], m["pro"], m["x"] + "ṃ", m["v1"], m["y"] + "ṃ", m["v2"])
    m = A_BOTH3.match(s)
    if m and (m["xc"] == "ñca") != (m["yc"] == "ñca"):
        # source slip: one member of «X ca … Y ca» without «ca» (3-03): that member without «လည်း»
        x = F.subj(m["x"] + "ṃ") + (ALSO if m["xc"] == "ñca" else "")
        y = F.subj(m["y"] + "ṃ") + (ALSO if m["yc"] == "ñca" else "")
        return f"{F.who_my(m['who'], m['pro'])} {x} {F.V(m['v1'])}{C} {y} {F.V(m['v2'])}{END}"
    return None


A_BOTH3 = re.compile(rf"^(?P<who>.+?) (?P<pro>{F.PROR}) (?P<x>\S+?)(?P<xc>ñca|ṃ) (?P<v1>{F.VB}) (?P<y>\S+?)"
                     rf"(?P<yc>ñca|ṃ) (?P<v2>{F.VB})\.$")
CL_KEYS = sorted(F.CL, key=lambda k: -len(k.split()))
FT_KEYS = ["tassa tattha", "tassa", "tattha"]
VBW = re.compile(rf"^{F.VB}$")


def who_try(who, pro):
    try:
        return F.who_my(who, pro)
    except (F.Miss, KeyError, IndexError):
        return None


def before_ft(low, j):
    return any(low[j:j + len(k.split())] == k.split() for k in FT_KEYS)


def frag_pavatti(s, end):
    """Token translation of a pavattivāra piece cut by «…» (no frame fits a cut sentence)."""
    toks = s.split()
    out = []
    i = 0
    verb_seen = flip = in_q = ft_seen = False
    found = None
    if not re.match(r"^(?:[Yy]assa|[Yy]attha|tassa|tattha)\b", s):
        for m in re.finditer(r" (tesaṃ tattha|tesaṃ|tattha)(?= |$)", s):
            who, rest = s[: m.start()], s[m.end():].split()
            if "no ca" in who or (rest and rest[0].lower() in F.PART):
                continue
            w = who_try(who, m[1])
            if w is not None:
                found = (w, len((who + m[0]).split()))
                break
    if found:
        out.append(found[0])
        i = found[1]
    elif all(F._place_form(t) or t.lower() in F.PART or attr_my(t) or t.lower() in ("sabbesaṃ", "itaresaṃ",
                                                                                     "pacchimabhavikānaṃ")
             for t in toks):
        return F.group_my(s) + F.DAT + end
    low = [t.lower().rstrip(",") for t in toks]
    while i < len(toks):
        hit = None
        if i == 0:
            for k in sorted(["yassa vā pana yattha", "yassa yattha", "yassa vā pana", "yattha vā pana", "yassa",
                             "yattha"], key=lambda k: -len(k.split())):
                n = len(k.split())
                if low[i:i + n] == k.split():
                    hit = (k, n)
                    break
            if hit:
                k = hit[0]
                pre = ""
                if " vā pana" in k:
                    pre, k = F.VA_PANA + " ", k.replace(" vā pana", "")
                out.append(pre + F.CL[k][0])
                i += hit[1]
                in_q = True
                continue
        if verb_seen and not ft_seen and not found:
            k = next((k for k in FT_KEYS if low[i:i + len(k.split())] == k.split()), None)
            if k:
                out[-1] += C
                out.append(F.FT[k])
                i += len(k.split())
                ft_seen, verb_seen = True, False
                continue
        if low[i:i + 2] == ["no", "ca"]:
            out.append(F.BUT)
            i += 2
            k = next((k for k in ("tesaṃ tattha", "tesaṃ", "tattha") if low[i:i + len(k.split())] == k.split()), None)
            if k:
                out.append(F.PRO[k])
                i += len(k.split())
            flip, verb_seen = True, False
            continue
        t = toks[i].rstrip(",")
        comma = C if toks[i].endswith(",") else ""
        if t.lower() == "na" and i + 1 < len(toks) and VBW.match(toks[i + 1].rstrip(",")):
            t = "na " + toks[i + 1].rstrip(",")
            comma = C if toks[i + 1].endswith(",") else ""
            i += 1
        if VBW.match(t):
            root, tense, neg = F.pali_verb(t)
            q = bool(re.search(r"(?:īti|āti)$", t))
            if q:
                v = F.my_verb(root, tense, neg, "q")
            elif flip:
                v = F.not_so(root, tense) if neg else F.my_verb(root, tense, True)
            elif (in_q or before_ft(low, i + 1)) and not ft_seen:
                v = F.my_verb(root, tense, neg, "cl")
            else:
                v = F.my_verb(root, tense, neg)
            out.append(v + comma)
            verb_seen, flip = True, False
            i += 1
            continue
        fused = t.endswith("ñca")
        key = t[:-3] + "ṃ" if fused else t
        if key in F.SUBJ:
            if fused and verb_seen and not in_q and not out[-1].endswith(C):
                out[-1] += C
            out.append(F.SUBJ[key] + (ALSO if fused else "") + comma)
            i += 1
            continue
        raise F.Miss(f"fragment token {t!r} in: {s}")
    return " ".join(out) + end


ANS_BARE = {k[:-1]: v[:-1] for k, v in F.ANSWERS.items()}      # «Āmantā» / «No» / «Natthi» without the stop


def sentence(s):
    """A whole sentence (ends in . or ?)."""
    for fn in (pavatti, pariñña, pannatti):
        r = fn(s)
        if r:
            return r
    raise F.Miss("no frame for: " + s)


def fragment(s):
    """A piece next to a «…»: a whole sentence, an answer, or a cut sentence."""
    end = s[-1] if s[-1] in ".?" else ""
    core = s[:-1] if end else s
    if core in ANS_BARE:
        return ANS_BARE[core] + (END if end else "")
    if end:
        for fn in (pavatti, pariñña):
            r = fn(s)
            if r:
                return r
    r = pannatti(s)
    if r:
        return r
    r = pavatti(core + ".")
    if r and re.search(r"(?:no ca|ñca )", core):
        return r[:-1] + (END if end else "")
    return frag_pavatti(core, END if end else "")


SPLIT = F.SPLIT
BRACKET = re.compile(r" \[([^\]]*)\]")


def lead_my(lead):
    """the «.» / «?» that ends a sentence right after a «…»: «။» / «လော။» (the question verb is cut)."""
    p = lead.strip()
    if not p:
        return lead
    if p == ".":
        return END + lead[1:]
    if p == "?":
        return "လော" + END + lead[1:]
    raise F.Miss("lead: " + lead)


def body_ell(text):
    """Text with «…»: the pieces between the ellipses one by one."""
    out = []
    for p in re.split(r"(…)", text):
        if p == "…" or not p.strip():
            out.append(p)
            continue
        mlead = re.match(r"^[.?]?\s*", p)
        lead = mlead[0]
        rest = p[len(lead):]
        trail = re.search(r"\s*$", rest)[0]
        core = rest[: len(rest) - len(trail)]
        piece = lead_my(lead)
        if core:
            piece += " ".join(fragment(x) for x in SPLIT.split(core))
        out.append(piece + trail)
    return "".join(out)


def body_plain(text):
    return " ".join(sentence(x) if x[-1] in ".?" else fragment(x) for x in SPLIT.split(text))


NOTE_RE = re.compile("|".join(re.escape(k) for k in sorted(NOTES, key=len, reverse=True)))


def body(line):
    if line in COLO:
        return COLO[line]
    post = [v for k, v in SLIP_POST.items() if k in line]
    res = body2(unslip(line))
    for a, b in post:
        if a not in res:
            raise F.Miss("slip repair: " + a)
        res = res.replace(a, b, 1)
    return res


def body2(line):
    notes = []

    def keep_note(m):
        notes.append(NOTES[m[0]])
        return f"⟪{len(notes) - 1}⟫"
    line = NOTE_RE.sub(keep_note, line)
    vars_ = []

    def keep(m):
        vars_.append(variants(m[1]))
        return f" ⟦{len(vars_) - 1}⟧"
    line = BRACKET.sub(keep, line)
    line = line.replace("…pe…", PE).replace("…Pe…", PE)
    out = []
    for sg in re.split(r"(⟪\d+⟫)", line):
        mm = re.fullmatch(r"⟪(\d+)⟫", sg)
        if mm:
            out.append(notes[int(mm[1])])
            continue
        if not sg.strip():
            out.append(sg)
            continue
        lead = re.match(r"^\s*", sg)[0]
        trail = re.search(r"\s*$", sg)[0]
        core = sg.strip()
        if core == ".":
            out.append(lead + END + trail)
            continue
        out.append(lead + (body_ell(core) if PE in core else body_plain(core)) + trail)
    res = "".join(out)
    for i, v in enumerate(vars_):
        res = res.replace(f"⟦{i}⟧", v)
    return res


def translate_line(line):
    if not line.strip():
        return ""
    bid = ""
    m = F.ID_RE.search(line)
    if m:
        bid, line = " " + m[1], line[: m.start()]
    h = re.match(r"^(#+) (.*)$", line)
    if h:
        return f"{h[1]} {F.heading(h[2])}{bid}"
    lab = ""
    m = F.LABEL_RE.match(line)
    if m:
        lab, line = F.label(m[1]) + " ", line[m.end():]
    out = lab + body(line) + bid
    left = re.sub(r"\[[^\]]*\]", "", out)
    if re.search(r"[A-Za-zāīūṃṅñṭḍṇḷ⟦⟧⟪⟫⟨⟩]", left.replace(bid, "")):
        raise F.Miss("Pāli left in: " + out)
    return out


def translate_text(text):
    return "\n".join(translate_line(l) for l in text.splitlines()) + "\n"


# ===================================================================================== per-line check (make_sample.py)
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
    out = translate_text(src)
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
            translate_line(l)
        except (F.Miss, KeyError, ValueError, IndexError) as ex:
            n += 1
            print(f"{name}:{i} {type(ex).__name__}: {ex}")
    return n


if __name__ == "__main__":
    sel = [a for a in sys.argv[1:] if not a.startswith("--")]
    names = [n for n in NAMES_OUT if not sel or any(n.startswith(s) for s in sel)]
    if "--misses" in sys.argv:
        print("misses:", sum(misses(n) for n in names))
        sys.exit(0)
    OUT.mkdir(parents=True, exist_ok=True)
    for n in names:
        text, nbad = run(n)
        if nbad:
            sys.exit(f"{n}: {nbad} bad lines, nothing written")
        (OUT / n).write_text(text, encoding="utf-8")
        print(f"{n}: written, {len([l for l in text.splitlines() if l.strip()])} lines")
