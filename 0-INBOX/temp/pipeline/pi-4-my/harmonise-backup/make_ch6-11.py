"""Burmese zero-shot of pi-4 (Puggalapaññatti, «ပုဂ္ဂိုလ်များကို သတ်မှတ်ဖော်ပြခြင်း»), chapters 6 … 11
(Pañcaka … Dasakapuggalapaññatti).

usage: python3 -I -X utf8 make_ch6-11.py [chapter ...] [--misses]
Model: make_sample.py (imported read only: its tables UNIQUE / PRED_M / LINES_M are installed into my4_formulas at
import, nothing is written; its __main__ is never run). Every line is generated from the Pāli by
my4_formulas.translate_line() through the frames and tables of my4_formulas.py and of make_sample.py, plus the
tables and frames of THIS script (extended in memory only; my4_formulas.py is never edited):
  * VAR_KIND additions and an extended variant renderer (several readings in one bracket, the sigla «aṭṭhakathā»,
    the trailing notes «evamuparipi», «evaṃ tīsu ṭhānesupi»);
  * EXTRA_RULES: «Kathañca puggalo X?» / «Evaṃ puggalo X.» (KATHA table), the unquoted «Ayaṃ vuccati puggalo X.»;
  * SENT_6 … SENT_11: the sentences of the chapters, built from frames (the four admonished persons, the five
    warriors and the five monks like warriors, the ascetic practices, the six of the chakka, the definitions of
    ch2 repeated in ch8 / ch10) and hand-written strings for unique prose.
Reused pi-2 / pi-1 final Burmese is checked against the rails text by my4_formulas.witness() (fails at import if it
drifts). A sentence no frame or table entry matches stops the run (my4_formulas.Miss); nothing is guessed. A chapter
is written only when every line passed; on a stop the lines that passed go to scratch/partial-<chapter>.
"""
import pathlib
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import make_sample as M  # noqa: E402  (installs the sample tables into my4_formulas; writes nothing at import)

F = M.F
ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-4_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-4-burmese-plain-zeroshot_split_chapters"
NAMES_OUT = ["6-pancakapuggalapannatti.md", "7-chakkapuggalapannatti.md", "8-sattakapuggalapannatti.md",
             "9-atthakapuggalapannatti.md", "10-navakapuggalapannatti.md", "11-dasakapuggalapannatti.md"]
C, END, N, W, PE = F.C, F.END, F.NAME, F.W, F.PE
IDHA, COP, PUG, PUG_PL, CLP = F.IDHA, F.COP, F.PUGGALA, F.PUG_PL, F.CL_P
NEW = {}         # new recurring strings of these chapters («Pāli = Burmese»), for the notes / checker

# ===================================================================================== variant readings
F.VAR_KIND.update({
    "ārabbhajā": F.LEKHANA, "ayaṃ pana": F.PATHA, "satthambhati": F.LEKHANA, "ussādanaṃyeva": F.PATHA,
    "ussādanaññeva": F.PATHA, "santānetuṃ": F.PATHA, "āvīkatvā": F.LEKHANA, "sāmaṃyeva": F.PATHA,
    "uhasati": F.LEKHANA, "appicchaṃyeva": F.PATHA, "idamaṭṭhitaṃyeva": F.LEKHANA, "mokkho": F.PATHA,
    "nonītaṃ": F.LEKHANA, "dukkhassantaṃ karoti": F.PATHA, "sāhu": F.LEKHANA, "viriyaṃ": F.LEKHANA,
})
SIGLA_X = dict(F.SIGLA, **{"aṭṭhakathā": "အဋ္ဌကထာ"})
F.witness("2", "^2-811", "aṭṭhakathā oloketabbā", "အဋ္ဌကထာ")
NOTE = {"evamuparipi": "နောက်တွင်လည်း ဤနည်းတူ",                 # pi-2 ^2-718 / ^2-796 / ^2-811
        "evaṃ tīsu ṭhānesupi": "နေရာ သုံးခုလုံး၌လည်း ဤနည်းတူ"}
F.witness("2", "^2-796", "evamuparipi", NOTE["evamuparipi"])
_READ = re.compile(r"(?P<t>[^\[\](),\s][^\[\](),]*?) \((?P<s>[^()]+)\)")
_var_my0 = F.var_my


def var_my_x(br):
    """The sample renderer, extended: «[a (sī.), b (syā. ka.) a. ni. 5.141]» -> «[L (Sī.): a၊ (Syā., Ka.): b၊ ref]»
    (pi-2 ^2-832: the label once); sigla «aṭṭhakathā»; a trailing note «evamuparipi» (pi-2 ^2-796)."""
    if all(t in F.SIGLA for x in re.findall(r"\(([^()]+)\)", br) for t in x.split()):
        try:
            return _var_my0(br)
        except F.Miss:
            pass
    body = br[1:-1]
    note = ref = ""
    for k, v in NOTE.items():
        if body.endswith(" " + k):
            body, note = body[:-len(k) - 1], v
    m = re.search(r" (?P<r>[a-z]+\. [a-z]+\.) (?P<n>[\d.]+)$", body)
    if m:
        body, ref = body[:m.start()], f"{F.REF[m['r']]} {m['n']}"
    parts, pos = [], 0
    for rm in _READ.finditer(body):
        if body[pos:rm.start()] not in ("", ", "):
            raise F.Miss("variant: " + br)
        pos = rm.end()
        if rm["t"] not in F.VAR_KIND:
            raise F.Miss("variant kind: " + br)
        sig = ", ".join(SIGLA_X[s] for s in rm["s"].split())
        parts.append((F.VAR_KIND[rm["t"]], sig, rm["t"]))
    if pos != len(body) or not parts:
        raise F.Miss("variant: " + br)
    out = [f"{parts[0][0]} ({parts[0][1]}): {parts[0][2]}"] + [f"({s}): t" .replace(": t", f": {t}")
                                                              for _, s, t in parts[1:]]
    out += [x for x in (ref, note) if x]
    return "[" + f"{C} ".join(out) + "]"


F.var_my = var_my_x

# ===================================================================================== frames: Kathañca / Evaṃ
# «Kathañca puggalo X?» = «ပုဂ္ဂိုလ်သည် အဘယ်သို့ Vသနည်း။»; «Evaṃ puggalo X.» = «ဤသို့ ပုဂ္ဂိုလ်သည် V၏။»
# (V = the mātikā name as a verb phrase; the mātikā strings are checked below)
KATHA = {
    "datvā avajānāti": N["datvā avajānāti"][:-2],
    "saṃvāsena avajānāti": N["saṃvāsena avajānāti"][:-2],
    "ādheyyamukho hoti": f"{N['ādheyyamukho']} ဖြစ်",
    "lolo hoti": f"{N['lolo']} ဖြစ်",
    "mando momūho hoti": f"{N['mando momūho']} ဖြစ်",
    "sakiṃ nimuggo nimuggova hoti": "တစ်ကြိမ် နစ်လျှင် နစ်မြဲ နစ်နေသူ ဖြစ်",
    "ummujjitvā nimujjati": "ပေါ်လာပြီး ပြန်နစ်",
    "ummujjitvā ṭhito hoti": "ပေါ်လာပြီး တည်နေသူ ဖြစ်",
    "ummujjitvā vipassati viloketi": "ပေါ်လာပြီး သေချာစွာ မြင်၍ ပတ်ဝန်းကျင်ကို ကြည့်",
    "ummujjitvā patarati": "ပေါ်လာပြီး ကူးခတ်",
    "ummujjitvā patigādhappatto hoti": "ပေါ်လာပြီး ခြေကုပ်ရာသို့ ရောက်သူ ဖြစ်",
    "ummujjitvā tiṇṇo hoti pāraṅgato thale tiṭṭhati brāhmaṇo":
        f"ပေါ်လာပြီး {N['tiṇṇo pāraṅgato thale tiṭṭhati brāhmaṇo']} ဖြစ်",
}
_MAT5 = F.LINES["Datvā avajānāti, saṃvāsena avajānāti, ādheyyamukho hoti, lolo hoti, mando momūho hoti."]
_MAT7 = [v for k, v in F.LINES.items() if k.startswith("Satta udakūpamā puggalā.")][0]
for _k, _v in KATHA.items():          # the verb phrase = the mātikā item (vipassati viloketi: «၏၊» -> «၍», logged)
    _mv = _v.replace("မြင်၍ ပတ်ဝန်းကျင်ကို", "မြင်၏၊ ပတ်ဝန်းကျင်ကို")
    if _mv + "၏" not in _MAT5 + _MAT7:
        raise SystemExit("KATHA not as the mātikā: " + _k)
Q_HOW = f"{PUG}သည် အဘယ်သို့ {{}}သနည်း{END}"
E_HOW = f"ဤသို့ {PUG}သည် {{}}၏{END}"
NEW["Kathañca puggalo X? … Evaṃ puggalo X."] = Q_HOW.format("V") + " … " + E_HOW.format("V")
KATHA_RE = re.compile(r"Kathañca puggalo (?P<n>.+)\?")
EVAM_RE = re.compile(r"Evaṃ puggalo (?P<n>.+)\.")
VNQ_RE = re.compile(r"Ayaṃ vuccati puggalo (?P<n>[^\"]+)\.")      # ch8 / ch10: the name without quotes
F.EXTRA_RULES += [
    (KATHA_RE, lambda m: Q_HOW.format(KATHA[m["n"]]) if m["n"] in KATHA else None),
    (EVAM_RE, lambda m: E_HOW.format(KATHA[m["n"]]) if m["n"] in KATHA else None),
    (VNQ_RE, lambda m: F.VUCCATI.format(F.name(m["n"])) if F.key_of(m["n"]) else None),
]

# ===================================================================================== shared pieces
TATRA = "ထိုတို့အနက်"                                       # Tatra / Tattha (pi-2 «Tattha katamā … = ထိုတို့အနက် …»)
F.witness("2", "^2-849", "Tattha katamā", TATRA)
Q_PL = f" ဟူသည် အဘယ် {PUG_PL}နည်း{END}"                       # «Tattha katame … puggalā?» (plural of Q_TAIL)
PUNA = F.witness("2", "^2-760", "Puna caparaṃ", "တစ်ဖန်")
SEYY = F.witness("2", "^2-643", "Seyyathāpi nāma", "ဥပမာအားဖြင့်")
EVAMEVA = F.witness("2", "^2-643", "evameva", "ထို့အတူပင်")
BHIKKHU = "ရဟန်း"
IDHA_BH = F.witness("2", "^2-508", "Idha bhikkhu", "ဤသာသနာ၌ ရဟန်းသည်")      # Idha bhikkhu (pi-2)
IDHEK = W["idhekacco"]                                         # idhekacco = «ဤလောက၌ အချို့သော»
SO_BH = "ထိုရဟန်းသည်"                                           # So (the monk; pi-2 ^2-508)
F.witness("2", "^2-508", "So vivittaṃ", SO_BH)
SO = "ထိုသူသည်"                                                 # So (a person / warrior; sample ^4-31)
AYASMA = F.witness("2", "^2-957", "āyasmanto", "အသျှင်")
ASAVA = W["asava"]
ARAMBHAJA = "မှားယွင်းစွာ ပြုမူခြင်းမှ ဖြစ်သော"                 # ārambhaja (ārabhati = «မှားယွင်းစွာ ပြုမူ», sample)
VIPPA_JA = "နောင်တ ပူပန်မှုမှ ဖြစ်သော"                          # vippaṭisāraja (vippaṭisārī = «နောင်တ ပူပန်သူ», sample)
PAHAYA = "ပယ်၍"                                                  # pahāya (pi-2 ^2-508)
F.witness("2", "^2-508", "abhijjhaṃ loke pahāya", "လိုချင်ခြင်းကို ပယ်၍")
SIKKHA_DROP = F.witness("2", "^2-957", "sikkhaṃ paccakkhāya hīnāyāvattitvā", "သိက္ခာကို စွန့်၍ လူဘောင်သို့ ပြန်လည်")
BRAHMA = "မြင့်မြတ်သော အကျင့်"                                   # brahmacariya (pi-1 / pi-2 termbase)
F.witness("2", "^2-957", "sikkhaṃ", "သိက္ခာ")
PAKKAMATI = F.witness("2", "^2-957", "yenakāmaṃ pakkamati", "အလိုရှိရာသို့ ထွက်သွား")
ARANNA = F.witness("2", "^2-534", "Araññagato vā rukkhamūlagato vā suññāgāragato vā",
                   "တောသို့ ရောက်သည်ဖြစ်စေ၊ သစ်ပင်ရင်းသို့ ရောက်သည်ဖြစ်စေ၊ ဆိတ်ငြိမ်ရာ အိမ်သို့ ရောက်သည်ဖြစ်စေ")
SAMANN = "အပြည့်အဝ ပြည့်စုံ"                                     # samannāgata (sample)


def fin(stem):
    """A verb phrase stem -> finite: «… ဝင်နိုင်» -> «…၏»; a negative last verb «မ…» stays (sample «မရောက်»)."""
    last = stem.split(" ")[-1].split("၊")[-1]
    return stem if last.startswith("မ") and not last.startswith(("မြ", "မှ")) else stem + "၏"


SENT = {}


def put(p, my):
    if p in SENT and SENT[p] != my:
        raise SystemExit("SENT conflict: " + p[:80])
    SENT[p] = unicodedata.normalize("NFC", my)


# ===================================================================================== ch6 ^4-191 the four admonished
_A = {   # ārabhati / vippaṭisārī (the mātikā predicates of the sample, the bracket left out)
    "ārabhati ca vippaṭisārī ca hoti": f"မှားယွင်းစွာလည်း ပြုမူ၏{C} {M.REM}လည်း {COP}",
    "ārabhati na vippaṭisārī hoti": f"{M.WRONG}{C} {M.REM}ကား မဟုတ်",
    "na ārabhati vippaṭisārī hoti": f"{M.NOWRONG}{C} {M.REM}ကား {COP}",
    "na ārabhati na vippaṭisārī hoti": f"{M.NOWRONG}{C} {M.REM}လည်း မဟုတ်",
}
_REST = ("tañca cetovimuttiṃ paññāvimuttiṃ yathābhūtaṃ nappajānāti, yatthassa te {}pāpakā akusalā dhammā aparisesā "
         "nirujjhanti")
_UPP = "ဖြစ်ပေါ်ပြီးသော "
assert _UPP in M._NOKNOW
for i, (pa, ma) in enumerate(_A.items()):
    upp = "" if i == 3 else "uppannā "           # source slip: the fourth line has no «uppannā»
    know = M._NOKNOW if upp else M._NOKNOW.replace(_UPP, "")
    put(f"Tatra yvāyaṃ puggalo {pa}, {_REST.format(upp)}, so evamassa vacanīyo",
        f"{TATRA} အကြင် {PUG}သည် {ma}{C} {know}{C} ထို{PUG}ကို ဤသို့ ပြောဆိုသင့်၏")
_EXIST = {"": "ရှိကုန်၏", "na ": "မရှိကုန်"}                         # saṃvijjanti
_GROW = {"": "ပို၍ ပို၍ တိုးပွားကုန်၏", "na": "ပို၍ ပို၍ မတိုးပွားကုန်"}   # pavaḍḍhanti (vaḍḍhanti = «တိုးပွားကုန်၏», sample)
for ne, ng in (("", ""), ("", "na"), ("na ", ""), ("na ", "na")):
    for br, mb in (("", ""), (" [ārabbhajā (ka.) a. ni. 5.142]", " ⟦0⟧")):
        put(f'"āyasmato kho ārambhajā{br} āsavā {ne}saṃvijjanti, vippaṭisārajā āsavā {ng}{"ppa" if ng else "pa"}vaḍḍhanti.',
            f"“{AYASMA}၌ {ARAMBHAJA}{mb} {ASAVA}တို့ {_EXIST[ne]}{C} {VIPPA_JA} {ASAVA}တို့ {_GROW[ng]}{END}")
for p1, p2 in ((True, True), (True, False), (False, True), (False, False)):
    pa = ("ārambhaje āsave pahāya " if p1 else "") + ("vippaṭisāraje āsave paṭivinodetvā " if p2 else "")
    ma = (f"{ARAMBHAJA} {ASAVA}တို့ကို {PAHAYA} " if p1 else "") + (
        f"{VIPPA_JA} {ASAVA}တို့ကို ဖယ်ရှားပြီး " if p2 else "")
    put(f"Sādhu vatāyasmā {pa}cittaṃ paññañca bhāvetu.",
        f"{AYASMA}သည် {ma}စိတ်ကိုလည်း ပညာကိုလည်း ပွားများလျှင် ကောင်းလေစွ{END}")
FIFTH = f"ထို ပဉ္စမ {PUG}"                                            # amunā pañcamena puggalena
put('Evamāyasmā amunā pañcamena puggalena samasamo bhavissatī"ti.',
    f"ဤသို့ဖြင့် {AYASMA}သည် {FIFTH}နှင့် တန်းတူ ဖြစ်လိမ့်မည်”ဟု{END}")
F.witness("2", "^2-957", 'evamāha – "kiṃ', "ဤသို့ ဆို၏ – “")       # «… – “…”ဟု။» (pi-2 quote frame)
put("Ime cattāro puggalā amunā pañcamena puggalena evaṃ ovadiyamānā evaṃ anusāsiyamānā anupubbena āsavānaṃ "
    "khayaṃ pāpuṇanti.",
    f"ဤ{PUG} လေး{CLP}တို့သည် {FIFTH}က ဤသို့ ဆုံးမခံရ၍ ဤသို့ သွန်သင်ခံရသဖြင့် အစဉ်အတိုင်း "
    f"{F.witness('2', '^2-760', 'āsavānaṃ khayaṃ', ASAVA + 'တို့ ကုန်ခန်းခြင်း')}သို့ ရောက်ကြ၏{END}")

# ===================================================================================== ch6 ^4-192 the second five
CIVARA = F.witness("2", "^2-849", "cīvarapiṇḍapātasenāsanagilānappaccayabhesajjaparikkhār",
                   "သင်္ကန်း၊ ဆွမ်း၊ ကျောင်းအိပ်ရာနေရာ၊ သူနာ၏ အထောက်အပံ့ ဖြစ်သော ဆေးအသုံးအဆောင်")
put("Idhekacco puggalo yassa puggalassa deti cīvarapiṇḍapātasenāsanagilānapaccayabhesajjaparikkhāraṃ, tassa evaṃ hoti",
    f"{IDHA} အကြင် {PUG}အား {CIVARA}ကို ပေး၏{C} ထိုသူ၌ ဤသို့ အကြံ ဖြစ်၏")
put('"ahaṃ dammi, ayaṃ [ayaṃ pana (syā. ka.) a. ni. 5.141] paṭiggaṇhātī"ti, tamenaṃ datvā avajānāti.',
    f"“ငါက ပေး၏{C} ဤသူက ⟦0⟧ လက်ခံ၏”ဟု ထိုသူကို {KATHA['datvā avajānāti']}၏{END}")
put("Idhekacco puggalo yena puggalena saddhiṃ saṃvasati dve vā tīṇi vā vassāni, tamenaṃ saṃvāsena avajānāti.",
    f"{IDHA} အကြင် {PUG}နှင့် နှစ်နှစ်ဖြစ်စေ{C} သုံးနှစ်ဖြစ်စေ အတူ နေ၏{C} ထိုသူကို "
    f"{KATHA['saṃvāsena avajānāti']}၏{END}")
put("Idhekacco puggalo parassa vaṇṇe vā avaṇṇe vā bhāsiyamāne khippaññeva adhimuccitā hoti.",
    f"{IDHA} သူတစ်ပါးကို ချီးမွမ်း၍ဖြစ်စေ{C} ကဲ့ရဲ့၍ဖြစ်စေ ပြောဆိုနေစဉ် လျင်မြန်စွာပင် ယုံကြည်လိုက်သူ {COP}{END}")
_ITT = "ခဏတာသာ"                                                # ittara (short-lived)
put("Idhekacco puggalo ittarasaddho hoti ittarabhattī ittarapemo ittarappasādo.",
    f"{IDHA} " + f"{C} ".join(f"{_ITT} {x} ရှိသူ" for x in ("ယုံကြည်မှု", "ကိုးကွယ်ခြင်း", "ချစ်ခင်မှု", "ကြည်ညိုမှု"))
    + f" {COP}{END}")
_NOKNOWS = [f"{x} သဘောတရားတို့ကို မသိ" for x in (
    "ကုသိုလ် အကုသိုလ်", "အပြစ် ရှိသော အပြစ် မရှိသော", "ယုတ်ညံ့သော မွန်မြတ်သော",
    "မည်းနက်သော ဖြူစင်သော ဆန့်ကျင်ဘက် ရှိသော")]
put("Idhekacco puggalo kusalākusale dhamme na jānāti, sāvajjānavajje dhamme na jānāti, hīnappaṇīte dhamme na jānāti, "
    "kaṇhasukkasappaṭibhāge dhamme na jānāti.", f"{IDHA} " + f"{C} ".join(_NOKNOWS) + END)

# ===================================================================================== ch6 ^4-193 … ^4-198 warriors
WAR = "စစ်သည်"                                                  # yodhājīva (GROUP «စစ်သည်နှင့် တူသော», sample)
assert F.GROUP["yodhājīvūpamā"] == WAR + "နှင့် တူသော"
RAJ, DHAJ, USS, SAMP = "ဖုန်လုံး", "အလံဖျား", "ကြွေးကြော်သံ", "ထိပ်တိုက် တိုက်ခိုက်ခြင်း"
VIJAYA = "စစ်ပွဲ၌ အောင်နိုင်ခြင်း"                                # saṅgāmavijaya
SAHATI = "သည်းခံနိုင်၏"
P_STAGE = {1: "rajaggaññeva disvā", 2: "sahati rajaggaṃ, api ca kho dhajaggaññeva disvā",
           3: "sahati rajaggaṃ sahati dhajaggaṃ, api ca kho ussāraṇaññeva{b} sutvā",
           4: "sahati rajaggaṃ sahati dhajaggaṃ sahati ussāraṇaṃ, api ca kho sampahāre haññati byāpajjati",
           5: "sahati rajaggaṃ sahati dhajaggaṃ sahati ussāraṇaṃ sahati sampahāraṃ"}
_S1 = f"{RAJ}ကို {SAHATI}"
_S2 = f"{_S1}{C} {DHAJ}ကို {SAHATI}"
_S3 = f"{_S2}{C} {USS}ကို {SAHATI}"
B_STAGE = {1: f"{RAJ}ကိုပင် မြင်၍", 2: f"{_S1}{C} သို့သော် {DHAJ}ကိုပင် မြင်၍",
           3: f"{_S2}{C} သို့သော် {USS}ကိုပင်{{b}} ကြား၍",
           4: f"{_S3}{C} သို့သော် {SAMP}၌ အသတ်ခံရ၏{C} ဒဏ်ရာ ရ",          # verb stems (4, 5)
           5: f"{_S3}{C} {SAMP}ကို သည်းခံနိုင်"}
P_SINK_W = "saṃsīdati visīdati na santhambhati{b} na sakkoti saṅgāmaṃ otarituṃ"
B_SINK = f"စိတ်ဓာတ် ကျဆင်း၏{C} အားလျော့၏{C} ခိုင်ခိုင်မာမာ မရပ်တည်နိုင်"
B_SINK_W = f"{B_SINK}{{b}}{C} စစ်ပွဲသို့ မဝင်နိုင်"
P_SINK_M = ("saṃsīdati visīdati na santhambhati na sakkoti brahmacariyaṃ sandhāretuṃ{b1}, sikkhādubbalyaṃ "
            "āvikatvā{b2} sikkhaṃ paccakkhāya hīnāyāvattati")
B_SINK_M = (f"{B_SINK}{C} {BRAHMA}ကို ဆက်လက် မထိန်းသိမ်းနိုင်{{b1}}{C} သိက္ခာ၌ အားနည်းချက်ကို ထုတ်ဖော်၍{{b2}} "
            f"{SIKKHA_DROP}")
P_WIN = "So taṃ saṅgāmaṃ abhivijinitvā vijitasaṅgāmo tameva saṅgāmasīsaṃ ajjhāvasati"
B_WIN = f"{SO} ထိုစစ်ပွဲကို အောင်နိုင်၍ စစ်ပွဲကို အောင်ပြီးသူ ဖြစ်ကာ ထိုစစ်ပွဲ၏ ရှေ့တန်းကိုပင် အုပ်စိုး နေ"
ORD = {1: ("paṭhamo", "ပထမ"), 2: ("dutiyo", "ဒုတိယ"), 3: ("tatiyo", "တတိယ"), 4: ("catuttho", "စတုတ္ထ"),
       5: ("pañcamo", "ပဉ္စမ")}
SANTO_L = "လောက၌ ထင်ရှား ရှိနေသော"                              # santo saṃvijjamāno lokasmiṃ
SANTO_B = f"{BHIKKHU}တို့အထဲ၌ ထင်ရှား ရှိနေသော"                    # … bhikkhūsu
NEW["santo saṃvijjamāno lokasmiṃ / bhikkhūsu"] = f"{SANTO_L} / {SANTO_B}"
BR = {"": "", "0": " ⟦0⟧", "1": " ⟦1⟧"}


def stage(k, who_p, who_b, sink_p, sink_b, end=END):
    """«… idhekacco yodhājīvo / bhikkhu STAGE SINK.» -> Burmese (sink = None for the stages 4 and 5)."""
    p = f"{who_p} {P_STAGE[k]}" + (f" {sink_p}" if sink_p else "") + "."
    b = f"{who_b} {B_STAGE[k]}" + (f" {sink_b}" if sink_b else "")
    return p, fin(b) + end


# the five warriors (^4-193)
_br3 = " [ussādanaṃyeva (sī.), ussādanaññeva (syā. ka.) a. ni. 5.141]"
for k in range(1, 6):
    who_p = ("idhekacco" if k == 1 else f"Puna caparaṃ idhekacco") + " yodhājīvo"
    who_b = ("" if k == 1 else f"{PUNA} ") + f"{IDHEK} {WAR}သည်"
    bw = " [satthambhati (sī.) a. ni. 5.141]" if k == 1 else ""
    sp = P_SINK_W.format(b=bw) if k <= 3 else None
    sb = B_SINK_W.format(b=BR["0"] if bw else "") if k <= 3 else None
    p, b = stage(k, who_p, who_b, sp, sb)
    p = p.replace("{b}", _br3 if k == 3 else "")
    b = b.replace("{b}", BR["0"] if k == 3 else "")
    put(p, b)
    o_p, o_b = ORD[k]
    put(f"Ayaṃ {o_p} yodhājīvo santo saṃvijjamāno lokasmiṃ.", f"ဤသူသည် {SANTO_L} {o_b} {WAR} {COP}{END}")
    put(f"Ayaṃ {o_p} yodhājīvūpamo puggalo santo saṃvijjamāno bhikkhūsu.",
        f"ဤသူသည် {SANTO_B} {o_b} {F.GROUP['yodhājīvūpamā']} {PUG} {COP}{END}")
put(P_WIN + ".", fin(B_WIN) + END)
put("Evarūpopi idhekacco yodhājīvo hoti.", f"{IDHEK} {WAR}သည်လည်း ဤသို့ သဘောရှိသူ {COP}{END}")
put("Evarūpopi idhekacco puggalo hoti.", f"{IDHA}လည်း ဤသို့ သဘောရှိသူ {COP}{END}")
put("Ime pañca yodhājīvā santo saṃvijjamānā lokasmiṃ.", f"ဤသူတို့သည် {SANTO_L} {WAR} ငါး{CLP} ဖြစ်ကြ၏{END}")
put("Ime pañca yodhājīvūpamā puggalā santo saṃvijjamānā bhikkhūsu.",
    f"ဤသူတို့သည် {SANTO_B} {F.GROUP['yodhājīvūpamā']} {PUG} ငါး{CLP} ဖြစ်ကြ၏{END}")
put("Tattha katame pañca yodhājīvūpamā puggalā?", f"{TATRA} {F.GROUP['yodhājīvūpamā']} {PUG} ငါး{CLP}{Q_PL}")
put("Pañca yodhājīvā", f"{WAR} ငါး{CLP}")
put("Evamevaṃ pañcime yodhājīvūpamā puggalā santo saṃvijjamānā bhikkhūsu.",
    f"{EVAMEVA} {F.GROUP['yodhājīvūpamā']} ဤ{PUG} ငါး{CLP}တို့သည် {BHIKKHU}တို့အထဲ၌ ထင်ရှား ရှိနေကြ၏{END}")
put("Katame pañca?", f"အဘယ် ငါး{CLP}တို့နည်း{END}")
# the five monks (^4-194 … ^4-198)
for k in range(1, 6):
    who_p = ("Idhekacco" if k == 1 else "Puna caparaṃ idhekacco") + " bhikkhu"
    who_b = ("" if k == 1 else f"{PUNA} ") + f"{IDHEK} {BHIKKHU}သည်"
    if k <= 3:
        b1, b2 = (" [santānetuṃ (sī. syā.) a. ni. 5.75]", " [āvīkatvā (sī.)]") if k == 1 else ("", "")
        sp = P_SINK_M.format(b1=b1, b2=b2)
        sb = B_SINK_M.format(b1=BR["0"] if b1 else "", b2=BR["1"] if b2 else "")
    else:
        sp = sb = None
    p, b = stage(k, who_p, who_b, sp, sb)
    put(p.replace("{b}", ""), b.replace("{b}", ""))
    # the simile «Seyyathāpi so yodhājīvo …, tathūpamo ayaṃ puggalo.»
    tail_p = (f" {P_SINK_W.format(b='')}" if k <= 3 else "") + (f", {P_WIN[0].lower()}{P_WIN[1:]}" if k == 5 else "")
    stem_b = (f"{B_STAGE[k]} {B_SINK_W.format(b='')}" if k <= 3 else B_STAGE[k]).replace("{b}", "")
    if k == 5:
        stem_b = f"{fin(stem_b)}{C} {B_WIN}"
    put(f"Seyyathāpi so yodhājīvo {P_STAGE[k].replace('{b}', '')}{tail_p}, tathūpamo ayaṃ puggalo.",
        f"{SEYY} ထို{WAR}သည် {stem_b}သကဲ့သို့{C} ဤ{PUG}သည် ထို{WAR}နှင့် တူ၏{END}")
for pk, mk in (("rajaggasmiṃ", RAJ), ("dhajaggasmiṃ", DHAJ), ("ussāraṇāya", USS), ("sampahārasmiṃ", SAMP),
               ("saṅgāmavijayasmiṃ", VIJAYA)):
    put(f"Kimassa {pk}?", f"ထို{BHIKKHU}အတွက် {mk} ဟူသည် အဘယ်နည်း{END}")
    put(f"Idamassa {pk}.", f"ဤသည်ကား ထို{BHIKKHU}အတွက် {mk} {COP}{END}")
HEAR_P = ('"asukasmiṃ nāma gāme vā nigame vā itthī vā kumārī vā abhirūpā dassanīyā pāsādikā paramāya '
          'vaṇṇapokkharatāya samannāgatā"ti')
BEAUTY = (f"အဆင်းလှသော{C} ရှုချင်ဖွယ် ကောင်းသော{C} ကြည်ညိုဖွယ် ကောင်းသော{C} အလွန် ကောင်းမွန်သော အသားအရေနှင့် "
          f"{SAMANN}သော")
HEAR_B = (f"“{F.witness('2', '^2-957', 'itthannāmaṃ', 'ဤမည်သော')} ရွာ၌ဖြစ်စေ{C} နိဂုံး၌ဖြစ်စေ {BEAUTY} "
          f"မိန်းမဖြစ်စေ{C} အပျိုဖြစ်စေ ရှိ၏”ဟု")
put("Idha bhikkhu suṇāti", f"{IDHA_BH} ကြား၏")
put("Idha bhikkhu na heva kho suṇāti", f"{IDHA_BH} ကြားသည်ကား မဟုတ်")
put(HEAR_P + ".", HEAR_B + END)
put(HEAR_P + ", api ca kho sāmaṃ [sāmaṃyeva (sī.)] passati itthiṃ vā kumāriṃ vā abhirūpaṃ dassanīyaṃ pāsādikaṃ "
    "paramāya vaṇṇapokkharatāya samannāgataṃ.",
    f"{HEAR_B}{C} သို့သော် {BEAUTY} မိန်းမကိုဖြစ်စေ{C} အပျိုကိုဖြစ်စေ ကိုယ်တိုင် ⟦0⟧ မြင်၏{END}")
put(f"So taṃ sutvā {P_SINK_M.format(b1='', b2='')}.", f"{SO_BH} ထိုအကြောင်းကို ကြား၍ {fin(B_SINK_M.format(b1='', b2=''))}{END}")
put(f"So taṃ disvā {P_SINK_M.format(b1='', b2='')}.", f"{SO_BH} ထိုသူကို မြင်၍ {fin(B_SINK_M.format(b1='', b2=''))}{END}")
MATU = "အမျိုးသမီး"                                              # mātugāma (itthī = «မိန်းမ»)
APPROACH_P = ("Idha bhikkhuṃ araññagataṃ vā rukkhamūlagataṃ vā suññāgāragataṃ vā mātugāmo upasaṅkamitvā ")
APPROACH_B = f"{IDHA_BH} {ARANNA}{C} ထို{BHIKKHU}ထံသို့ {MATU}သည် ချဉ်းကပ်၍ "
USS_ACT = ["ပြုံးရယ်", "စကား ပြောဆို ချော့မော့", "ကျယ်လောင်စွာ ရယ်မော", "ကျီစယ် ပြက်ရယ်ပြု"]
SAMP_ACT = ["အနီး၌ ထိုင်", "အနီး၌ လှဲလျောင်း", "ဖိ၍ အုပ်မိုး"]
put(APPROACH_P + "ūhasati [uhasati (aṭṭhakathā) a. ni. 5.75] ullapati ujjagghati uppaṇḍeti.",
    APPROACH_B + f"{USS_ACT[0]}၏ ⟦0⟧{C} " + f"{C} ".join(x + "၏" for x in USS_ACT[1:]) + END)
put(APPROACH_P + "abhinisīdati abhinipajjati ajjhottharati.", APPROACH_B + f"{C} ".join(x + "၏" for x in SAMP_ACT) + END)
_PASS_U = f"{SO_BH} {MATU}၏ " + f"{C} ".join(x + "ခြင်း" for x in USS_ACT) + "ကို ခံရသောအခါ"
_PASS_S = f"{SO_BH} {MATU}၏ " + f"{C} ".join(x + "ခြင်း" for x in SAMP_ACT) + "ကို ခံရသောအခါ"
put("So mātugāmena ūhasiyamāno ullapiyamāno ujjagghiyamāno uppaṇḍiyamāno "
    f"{P_SINK_M.format(b1='', b2='')}.", f"{_PASS_U} {fin(B_SINK_M.format(b1='', b2=''))}{END}")
_SAMP_P = "So mātugāmena abhinisīdiyamāno abhinipajjiyamāno ajjhotthariyamāno "
put(_SAMP_P + "sikkhaṃ appaccakkhāya dubbalyaṃ anāvikatvā methunaṃ dhammaṃ paṭisevati.",
    f"{_PASS_S} သိက္ခာကို မစွန့်ဘဲ{C} အားနည်းချက်ကို မထုတ်ဖော်ဘဲ မေထုန် အကျင့်ကို မှီဝဲ၏{END}")
put(_SAMP_P + "viniveṭhetvā vinimocetvā yena kāmaṃ pakkamati.",
    f"{_PASS_S} ရုန်းထွက်၍ လွတ်မြောက်အောင် ပြုပြီး {PAKKAMATI}၏{END}")
# ^4-198 lines 2 … 5: the practice up to the destruction of the taints (pi-2 ^2-508 word for word where the Pāli is)
_VIV = F.witness("2", "^2-508", "So vivittaṃ senāsanaṃ bhajati araññaṃ rukkhamūlaṃ pabbataṃ kandaraṃ giriguhaṃ "
                                "susānaṃ vanapatthaṃ abbhokāsaṃ palālapuñjaṃ",
                 f"{SO_BH} တော၊ သစ်ပင်ရင်း၊ တောင်၊ ချောက်၊ တောင်ဂူ၊ သုသာန်၊ တောအုပ်ကြီး၊ လွင်တီးခေါင်၊ ကောက်ရိုးပုံ ဖြစ်သော")
_SEN = F.witness("2", "^2-508", "vivittaṃ senāsanaṃ bhajati", "ဆိတ်ငြိမ်သော အိပ်ရာ နေရာကို ဆည်းကပ်၏")
put("So vivittaṃ senāsanaṃ bhajati araññaṃ rukkhamūlaṃ pabbataṃ kandaraṃ giriguhaṃ susānaṃ vanapatthaṃ abbhokāsaṃ "
    "palālapuñjaṃ.", f"{_VIV} {_SEN}{END}")
_SIT_P = ("So araññagato vā rukkhamūlagato vā suññāgāragato vā nisīdati pallaṅkaṃ ābhujitvā ujuṃ kāyaṃ paṇidhāya "
          "parimukhaṃ satiṃ upaṭṭhapetvā")
put(_SIT_P + ".", F.witness("2", "^2-508", _SIT_P,
                            f"{SO_BH} {ARANNA} ထက်ဝယ်ဖွဲ့ခွေ၍ ကိုယ်ကို ဖြောင့်မတ်စွာ ထား၍ ရှေ့မှောက်၌ သတိကို ထင်စေ၍ "
                            f"ထိုင်၏") + END)
_NIV_P = ["So abhijjhaṃ loke pahāya vigatābhijjhena cetasā viharati, abhijjhāya cittaṃ parisodheti",
          "byāpādapadosaṃ pahāya abyāpannacitto viharati",
          "thinamiddhaṃ pahāya vigatathinamiddho viharati ālokasaññī sato sampajāno, thinamiddhā cittaṃ parisodheti",
          "uddhaccakukkuccaṃ pahāya anuddhato viharati ajjhattaṃ vūpasantacitto, uddhaccakukkuccā cittaṃ parisodheti",
          "vicikicchaṃ pahāya tiṇṇavicikiccho viharati akathaṃkathī kusalesu dhammesu, vicikicchāya cittaṃ parisodheti"]
_NIV_B = [
    f"{SO_BH} လောက၌ သူ့ဥစ္စာကို လိုချင်ခြင်းကို ပယ်၍ သူ့ဥစ္စာကို လိုချင်ခြင်း ကင်းသော စိတ်ဖြင့် နေ၏၊ သူ့ဥစ္စာကို "
    "လိုချင်ခြင်းမှ စိတ်ကို အကြွင်းမဲ့ သန့်စင်စေ၏",
    "ဖျက်ဆီးလိုစိတ်နှင့် အလွန် ဒေါသထွက်ခြင်းကို ပယ်၍ ဖျက်ဆီးလိုစိတ် မရှိသော စိတ် ရှိသူ ဖြစ်လျက် ခပ်သိမ်းသော "
    "သတ္တဝါတို့၏ အကျိုးကို စာနာလျက် နေ၏၊ ဖျက်ဆီးလိုစိတ်နှင့် အလွန် ဒေါသထွက်ခြင်းမှ စိတ်ကို အကြွင်းမဲ့ သန့်စင်စေ၏",
    "ထိုင်းမှိုင်းမှုနှင့် ငိုက်မျဉ်းမှုကို ပယ်၍ ထိုင်းမှိုင်းမှုနှင့် ငိုက်မျဉ်းမှု ကင်းသူ ဖြစ်လျက်၊ အလင်းဟု မှတ်သိလျက်၊ "
    "သတိ ရှိလျက်၊ ကောင်းစွာ ဆင်ခြင်သိမြင်လျက် နေ၏၊ ထိုင်းမှိုင်းမှုနှင့် ငိုက်မျဉ်းမှုမှ စိတ်ကို အကြွင်းမဲ့ သန့်စင်စေ၏",
    "ယောက်ယက်ခတ်မှုနှင့် နောင်တ ပူပန်မှုကို ပယ်၍ မယောက်ယက်ခတ်ဘဲ မိမိ၌ ကောင်းစွာ ငြိမ်သက်ပြီးသော စိတ် ရှိလျက် "
    "နေ၏၊ ယောက်ယက်ခတ်မှုနှင့် နောင်တ ပူပန်မှုမှ စိတ်ကို အကြွင်းမဲ့ သန့်စင်စေ၏",
    "ယုံမှားမှုကို ပယ်၍ ယုံမှားမှုကို ကူးမြောက်လျက်၊ ကုသိုလ် သဘောတရားတို့၌ ‘အဘယ်သို့နည်း’ဟု မတွေးတောဘဲ နေ၏၊ "
    "ယုံမှားမှုမှ စိတ်ကို အကြွင်းမဲ့ သန့်စင်စေ၏"]
for _p, _b in zip(_NIV_P, _NIV_B):
    F.witness("2", "^2-508", _p, _b)
# ch6 has «… viharati, sabbapāṇabhūtahitānukampī byāpādapadosā cittaṃ parisodheti» (pi-2: «viharati
# sabbapāṇabhūtahitānukampī, byāpādapadosā …»): same words, the comma moved; the pi-2 Burmese is kept.
put("So abhijjhaṃ loke pahāya vigatābhijjhena cetasā viharati, abhijjhāya cittaṃ parisodheti; byāpādapadosaṃ pahāya "
    "abyāpannacitto viharati, sabbapāṇabhūtahitānukampī byāpādapadosā cittaṃ parisodheti; " + "; ".join(_NIV_P[2:]) + ".",
    f"{C} ".join(_NIV_B) + END)
_JH1 = F.witness("2", "^2-508", "So ime pañca nīvaraṇe pahāya cetaso upakkilese paññāya dubbalīkaraṇe vivicceva kāmehi "
                                "vivicca akusalehi dhammehi savitakkaṃ savicāraṃ vivekajaṃ pītisukhaṃ paṭhamaṃ jhānaṃ "
                                "upasampajja viharati; vitakkavicārānaṃ vūpasamā",
                 f"{SO_BH} စိတ်ကို ညစ်နွမ်းစေတတ်သော အညစ်အကြေးများ ဖြစ်ကုန်သော၊ ပညာကို အားနည်းစေတတ်ကုန်သော ဤအတားအဆီး "
                 "ငါးပါးတို့ကို ပယ်၍ ကာမတို့မှ ကင်းဆိတ်၍သာ၊ အကုသိုလ် သဘောတရားတို့မှ ကင်းဆိတ်၍၊ စတင်ကြံစည်မှု ရှိသော၊ "
                 "ဆက်လက်သုံးသပ်မှု ရှိသော၊ ကင်းဆိတ်ခြင်းမှ ဖြစ်ပေါ်သော ပီတိနှင့် သာယာမှု ရှိသော ပထမ ဈာန်ကို ဝင်စား၍ နေ၏၊ "
                 "စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှုတို့ ငြိမ်းသွားခြင်းကြောင့်")
for _o in ("ဒုတိယ ဈာန်", "တတိယ ဈာန်", "စတုတ္ထ ဈာန်ကို ဝင်စား၍ နေ၏"):
    F.witness("2", "^2-508", "jhānaṃ upasampajja viharati", _o)
put("So ime pañca nīvaraṇe pahāya cetaso upakkilese paññāya dubbalīkaraṇe vivicceva kāmehi vivicca akusalehi dhammehi "
    "savitakkaṃ savicāraṃ vivekajaṃ pītisukhaṃ paṭhamaṃ jhānaṃ upasampajja viharati; vitakkavicārānaṃ vūpasamā dutiyaṃ "
    "jhānaṃ…pe… tatiyaṃ jhānaṃ…pe… catutthaṃ jhānaṃ upasampajja viharati.",
    f"{_JH1} ဒုတိယ ဈာန်{PE} တတိယ ဈာန်{PE} စတုတ္ထ ဈာန်ကို ဝင်စား၍ နေ၏{END}")
_KHAYA = F.witness("2", "^2-760", "āsavānaṃ khayaṃ", f"{ASAVA}တို့ ကုန်ခန်းခြင်း")
put("So evaṃ samāhite citte parisuddhe pariyodāte anaṅgaṇe vigatūpakkilese mudubhūte kammaniye ṭhite āneñjappatte "
    "āsavānaṃ khayañāṇāya cittaṃ abhininnāmeti.",
    f"{SO_BH} ဤသို့ စိတ် တည်ကြည်၍ စင်ကြယ်ပြီး{C} ဖြူစင်ပြီး{C} အညစ်အကြေး မရှိဘဲ{C} ညစ်နွမ်းမှု ကင်း၍{C} "
    f"နူးညံ့ပြီး{C} အလုပ်ပေးရ လွယ်ကူပြီး{C} တည်တံ့၍ မတုန်လှုပ်သည့် အခြေသို့ ရောက်သောအခါ {_KHAYA}ကို သိသော "
    f"ဉာဏ်အတွက် စိတ်ကို ရှေးရှု ညွှတ်၏{END}")
_KNOW = W["yathabhutam_pajanati"] + "၏"
_AS4 = [f"{ASAVA}တို့", f"{ASAVA} ဖြစ်ပေါ်ခြင်း", f"{ASAVA} ချုပ်ငြိမ်းခြင်း", f"{ASAVA} ချုပ်ငြိမ်းရာသို့ ရောက်စေသော ကျင့်စဉ်"]
put('So "idaṃ dukkha"nti yathābhūtaṃ pajānāti, "ayaṃ dukkhasamudayo"ti yathābhūtaṃ pajānāti, "ayaṃ dukkhanirodho"ti '
    'yathābhūtaṃ pajānāti, "ayaṃ dukkhanirodhagāminī paṭipadā"ti yathābhūtaṃ pajānāti, "ime āsavā"ti yathābhūtaṃ '
    'pajānāti, "ayaṃ āsavasamudayo"ti yathābhūtaṃ pajānāti, "ayaṃ āsavanirodho"ti yathābhūtaṃ pajānāti, "ayaṃ '
    'āsavanirodhagāminī paṭipadā"ti yathābhūtaṃ pajānāti.',
    f"{SO_BH} " + f"{C} ".join(f"“ဤသည်ကား {t}”ဟု {_KNOW}" for t in M.F._TR + _AS4) + END)
put("Tassa evaṃ jānato evaṃ passato kāmāsavāpi cittaṃ vimuccati, bhavāsavāpi cittaṃ vimuccati, avijjāsavāpi cittaṃ "
    "vimuccati.",
    f"ဤသို့ သိ၍ ဤသို့ မြင်သော ထို{BHIKKHU}၏ စိတ်သည် " + f"{C} ".join(
        f"{x} {ASAVA}မှလည်း လွတ်မြောက်၏" for x in ("ကာမ", "ဘဝ", "အမှန်ကို မသိမှု")) + END)
put("Vimuttasmiṃ vimuttamiti ñāṇaṃ hoti.", f"လွတ်မြောက်သောအခါ “လွတ်မြောက်ပြီ”ဟု သိသော ဉာဏ် ဖြစ်၏{END}")
put('"Khīṇā jāti, vusitaṃ brahmacariyaṃ, kataṃ karaṇīyaṃ, nāparaṃ itthattāyā"ti pajānāti.',
    f"“မွေးဖွားခြင်း ကုန်ပြီ{C} {BRAHMA}ကို ကျင့်ပြီးပြီ{C} ပြုဖွယ် ကိစ္စကို ပြုပြီးပြီ{C} ဤအဖြစ်အတွက် နောက်ထပ် "
    f"ပြုဖွယ် မရှိတော့ပြီ”ဟု ကွဲပြားစွာ သိ၏{END}")

# ===================================================================================== ch6 ^4-199 … ^4-201 ascetics
FOUR_P = ("appicchataṃyeva{b0} nissāya santuṭṭhiṃyeva nissāya sallekhaṃyeva nissāya idamatthitaṃyeva{b1} nissāya")
FOUR_B = (f"အလိုနည်းခြင်းကိုသာ{{b0}} မှီ၍{C} ရောင့်ရဲမှုကိုသာ မှီ၍{C} ကိလေသာကို ခြစ်ခွာခြင်းကိုသာ မှီ၍{C} "
          f"ဤမျှဖြင့် လုံလောက်ခြင်းကိုသာ{{b1}} မှီ၍")
F.witness("2", "^2-849", "asantuṭṭhassa", "ရောင့်ရဲမှု")
PAPICCHA = F.witness("2", "^2-865", "pāpiccho icchāpakato", "ယုတ်မာသော အလိုရှိသော၊ အလိုဆန္ဒ နှိပ်စက်ခံရသော")
BEST = f"အမြတ်ဆုံးလည်း{C} အကောင်းဆုံးလည်း{C} အကြီးမှူးလည်း{{b}}{C} အထွတ်အထိပ်လည်း{C} အမွန်မြတ်ဆုံးလည်း {COP}"
NEW["aggo ca seṭṭho ca pāmokkho ca uttamo ca pavaro ca"] = BEST.replace("{b}", "")
PURE = (f"{SEYY} နွားမှ နွားနို့ ဖြစ်၏{C} နွားနို့မှ နို့ချဉ်{C} နို့ချဉ်မှ ထောပတ်{{b}}{C} ထောပတ်မှ ထောပတ်ကြည်{C} "
        f"ထောပတ်ကြည်မှ ထောပတ်ကြည် အနှစ် ဖြစ်၏{C} ထိုတို့အနက် ထောပတ်ကြည် အနှစ်ကို အမြတ်ဆုံးဟု ဆိုကြသကဲ့သို့{C} "
        f"{EVAMEVA}")


def ascetic(stem, my, b0="", b1="", b2="", b3=""):
    """The five piṇḍapātikā / sosānikā (^4-199, ^4-201): stem «piṇḍapātik», my = the group noun (sample)."""
    so, pl, gp = stem + "o", stem + "ā", stem + "ānaṃ"
    m0, m1, m2, m3 = (BR["0"] if b0 else ""), (BR["1"] if b1 else ""), (BR["0"] if b2 else ""), (BR["0"] if b3 else "")
    four_p, four_b = FOUR_P.format(b0=b0, b1=b1), FOUR_B.format(b0=m0, b1=m1)
    four_pn, four_bn = FOUR_P.format(b0="", b1=""), FOUR_B.format(b0="", b1="")
    put(f"Tattha katame pañca {pl}?", f"{TATRA} {my} ငါး{CLP}{Q_PL}")
    put(f'Mandattā momūhattā {so} hoti, pāpiccho icchāpakato {so} hoti, ummādā cittavikkhepā {so} hoti, "vaṇṇitaṃ '
        f'buddhehi buddhasāvakehī"ti {so} hoti, api ca {four_p} {so} hoti.',
        f"ထုံထိုင်းခြင်း{C} အလွန် တွေဝေခြင်းကြောင့် {my} {COP}{C} {PAPICCHA} သူ ဖြစ်၍ {my} {COP}{C} ရူးသွပ်ခြင်း{C} "
        f"စိတ် ပျံ့လွင့်ခြင်းကြောင့် {my} {COP}{C} “ဘုရားရှင်တို့နှင့် ဘုရားရှင်၏ တပည့်တို့ ချီးမွမ်းထားသည်”ဟု {my} "
        f"{COP}{C} ထို့ပြင် {four_b} {my} {COP}{END}")
    put(f"Tatra yvāyaṃ {so} {four_pn} {so}, ayaṃ imesaṃ pañcannaṃ {gp} aggo ca seṭṭho ca pāmokkho{b2} ca uttamo ca "
        f"pavaro ca.",
        f"{TATRA} {four_bn} {my} ဖြစ်သော အကြင်သူ ရှိ၏{C} ဤသူသည် ဤ {my} ငါး{CLP}တို့အနက် {BEST.format(b=m2)}{END}")
    put(f"Seyyathāpi nāma gavā khīraṃ, khīramhā dadhi, dadhimhā navanītaṃ{b3}, navanītamhā sappi, sappimhā "
        f"sappimaṇḍo, sappimaṇḍaṃ tattha aggamakkhāyati; evamevaṃ yvāyaṃ {so} {four_pn} {so} hoti, ayaṃ imesaṃ "
        f"pañcannaṃ {gp} aggo ca seṭṭho ca pāmokkho ca uttamo ca pavaro ca.",
        f"{PURE.format(b=m3)} {four_bn} {my} ဖြစ်သော အကြင်သူ ရှိ၏{C} ဤသူသည် ဤ {my} ငါး{CLP}တို့အနက် "
        f"{BEST.format(b='')}{END}")
    put(f"Ime pañca {pl}.", f"ဤသူတို့သည် {my} ငါး{CLP} ဖြစ်ကြ၏{END}")


ascetic("piṇḍapātik", F.GROUP_NOUN["piṇḍapātikā"], " [appicchaṃyeva (syā.) a. ni. 5.181]",
        " [idamaṭṭhitaṃyeva (sī.)]", " [mokkho (sī.)]", " [nonītaṃ (sī.)]")
ascetic("sosānik", F.GROUP_NOUN["sosānikā"])
_REST9 = ["khalupacchābhattikā", "ekāsanikā", "paṃsukūlikā", "tecīvarikā", "āraññikā", "rukkhamūlikā", "abbhokāsikā",
          "nesajjikā", "yathāsanthatikā"]
put("Tattha katame " + "…pe… ".join(f"pañca {x}" for x in _REST9).replace("rukkhamūlikā…pe…", "rukkhamūlikā …pe…") + "…pe….",
    f"{TATRA} " + f"{PE} ".join(f"{F.GROUP_NOUN[x]} ငါး{CLP}" for x in _REST9) + PE + END)

# ===================================================================================== ch7 ^4-202 the six
_AN = "pubbe ananussutesu dhammesu sāmaṃ saccāni"
_DUK = M._DUK
_DIT = W["ditthe_dhamme"]
SIX = [
    (f"{_AN} abhisambujjhati, tattha ca sabbaññutaṃ pāpuṇāti balesu ca vasībhāvaṃ",
     f"{F.ANANUSSUTA} {F.ABHISAM}{C} ထို၌လည်း {F.SABBANNU} ရောက်၏{C} {F.BALA_VASI}လည်း ရောက်၏",
     "sammāsambuddho tena daṭṭhabbo", N["sammāsambuddho"]),
    (f"{_AN} abhisambujjhati, na ca tattha sabbaññutaṃ pāpuṇāti na ca balesu vasībhāvaṃ",
     F.PRED[f"{_AN} abhisambujjhati, na ca tattha sabbaññutaṃ pāpuṇāti na ca balesu vasībhāvaṃ"],
     "paccekasambuddho tena daṭṭhabbo", N["paccekasambuddho"]),
    (f"{_AN} anabhisambujjhati, diṭṭheva dhamme dukkhassantakaro hoti [dukkhassantaṃ karoti (sī.) evamuparipi], "
     "sāvakapāramiñca pāpuṇāti",
     f"{F.ANANUSSUTA} {F.ANABHISAM}{C} {_DIT} {_DUK} ⟦0⟧ {COP}{C} {M._SAVAKA}သို့လည်း ရောက်၏",
     "sāriputtamoggallānā tena daṭṭhabbā", "သာရိပုတ္တရာနှင့် မောဂ္ဂလ္လာန်တို့"),
    (f"{_AN} anabhisambujjhati, diṭṭheva dhamme dukkhassantakaro hoti, na ca sāvakapāramiṃ pāpuṇāti",
     F.PRED[f"{_AN} anabhisambujjhati, diṭṭheva dhamme dukkhassantakaro hoti, na ca sāvakapāramiṃ pāpuṇāti"],
     "avasesā arahantā tena daṭṭhabbā", f"ကြွင်းကျန်သော {W['araha']}တို့"),
    (f"{_AN} anabhisambujjhati, na ca diṭṭheva dhamme dukkhassantakaro hoti, anāgāmī hoti anāgantā itthattaṃ",
     f"{F.ANANUSSUTA} {F.ANABHISAM}{C} {_DIT} {_DUK}လည်း မဟုတ်{C} {N['anāgāmī']} {COP}{C} ဤဘဝသို့ ပြန်မလာမည့်သူ "
     f"{COP}", "anāgāmī tena daṭṭhabbo", N["anāgāmī"]),
    (f"{_AN} anabhisambujjhati, na ca diṭṭheva dhamme dukkhassantakaro hoti, āgantā itthattaṃ",
     f"{F.ANANUSSUTA} {F.ANABHISAM}{C} {_DIT} {_DUK}လည်း မဟုတ်{C} ဤဘဝသို့ ပြန်လာမည့်သူ {COP}",
     "sotāpannasakadāgāmino tena daṭṭhabbā", f"{N['sotāpanno']}နှင့် {N['sakadāgāmī']}တို့"),
]
TENA = "ကို ထိုသို့ သိမှတ်ရမည်"                                    # X tena daṭṭhabbo
NEW["Tatra yvāyaṃ puggalo P, X tena daṭṭhabbo."] = f"{TATRA} အကြင် {PUG}သည် P{C} X{TENA}{END}"
for _p, _b, _x, _xb in SIX:
    put(f"Tatra yvāyaṃ puggalo {_p}, {_x}.", f"{TATRA} အကြင် {PUG}သည် {_b}{C} {_xb}{TENA}{END}")
assert f"ကြွင်းကျန်သော {PUG_PL}" in M.UNIQUE["Avasesā puggalā aniyatā."]

# ===================================================================================== ch8 ^4-203 … ^4-206
_Q5 = [("saddhā", "ယုံကြည်မှု"), ("hirī", "ဒုစရိုက်ကို ရှက်မှု"), ("ottappaṃ", "ဒုစရိုက်ကို ကြောက်ရွံ့မှု"),
       ("vīriyaṃ", "ဝီရိယ"), ("paññā", "ပညာ")]
F.witness("1", "^1-1166", "kukkuccaṃ", "နောင်တ ပူပန်မှု")      # kukkucca (vippaṭisāra kept apart: sample)
GOOD = "ကောင်း၏"                                                 # sādhu / sāhu
KUS = W["kusalesu"]
_UMM_B = (f"{IDHA} “" + f"{C} ".join(
    f"{KUS} {m}သည်" + (" ⟦1⟧" if p == "vīriyaṃ" else "") + f" {GOOD}" + (" ⟦0⟧" if p == "hirī" else "")
    for p, m in _Q5) + "”ဟု သဘောထား၍ ပေါ်လာ၏" + END)
put('Idhekacco puggalo ummujjati "sāhu saddhā kusalesu dhammesu, sādhu [sāhu (sī. syā.) evaṃ tīsu ṭhānesupi] hirī '
    'kusalesu dhammesu, sādhu ottappaṃ kusalesu dhammesu, sādhu vīriyaṃ [viriyaṃ (sī. syā.)] kusalesu dhammesu, sādhu '
    'paññā kusalesu dhammesū"ti.', _UMM_B)
put('Idhekacco puggalo ummujjati "sāhu saddhā kusalesu dhammesu, sādhu hirī kusalesu dhammesu, sādhu ottappaṃ '
    'kusalesu dhammesu, sādhu vīriyaṃ kusalesu dhammesu, sādhu paññā kusalesu dhammesū"ti.',
    _UMM_B.replace(" ⟦0⟧", "").replace(" ⟦1⟧", ""))
_DEM = {"saddhā": "sā", "hirī": "sā", "ottappaṃ": "taṃ", "vīriyaṃ": "taṃ", "paññā": "sā"}
_FALL = f"မတည်တံ့{C} မတိုးပွား{C} ယုတ်လျော့သာ ယုတ်လျော့၏"          # neva tiṭṭhati no vaḍḍhati hāyatiyeva
_STAY = f"မယုတ်လျော့{C} မတိုးပွား{C} တည်နေ၏"                       # neva hāyati no vaḍḍhati ṭhitā hoti
put(", ".join(f"tassa {_DEM[p]} {p} neva tiṭṭhati no vaḍḍhati hāyatiyeva" for p, m in _Q5).capitalize() + ".",
    f"{C} ".join(f"ထိုသူ၏ ထို{m}သည် {_FALL}" for p, m in _Q5) + END)
put(", ".join(f"tassa {_DEM[p]} {p} neva hāyati no vaḍḍhati {'ṭhitaṃ' if _DEM[p] == 'taṃ' else 'ṭhitā'} hoti"
              for p, m in _Q5).capitalize() + ".",
    f"{C} ".join(f"ထိုသူ၏ ထို{m}သည် {_STAY}" for p, m in _Q5) + END)
put("So tiṇṇaṃ saṃyojanānaṃ parikkhayā sotāpanno hoti avinipātadhammo niyato sambodhiparāyano.",
    f"{SO} {F.STREAM[len(IDHA) + 1:]} {COP}{END}")
assert F.STREAM.startswith(IDHA + " ") and F.ANAGAMI.startswith(IDHA + " ")
put("So tiṇṇaṃ saṃyojanānaṃ parikkhayā rāgadosamohānaṃ tanuttā sakadāgāmī hoti sakideva imaṃ lokaṃ āgantvā "
    "dukkhassantakaro hoti.",
    f"{SO} {W['samyojana']} {F._PARIKKHAYA}၊ ရာဂ၊ ဒေါသ၊ မောဟတို့ ပါးလျခြင်းကြောင့် {N['sakadāgāmī']} {COP}{C} "
    f"ဤလောကသို့ တစ်ကြိမ်သာ ပြန်လာ၍ {_DUK} {COP}{END}")
assert ("ရာဂ၊ ဒေါသ၊ မောဟတို့ ပါးလျခြင်းကြောင့်" in M.UNIQUE[[k for k in M.UNIQUE if "rāgadosamohānaṃ" in k][0]])
put("So pañcannaṃ orambhāgiyānaṃ saṃyojanānaṃ parikkhayā opapātiko hoti tattha parinibbāyī anāvattidhammo tasmā lokā.",
    f"{SO} {F.ANAGAMI[len(IDHA) + 1:]}{END}")
_ARAHATTA = F.witness("2", "^2-831", "āsavānaṃ khayā anāsavaṃ cetovimuttiṃ paññāvimuttiṃ diṭṭheva dhamme sayaṃ abhiññā "
                                     "sacchikatvā upasampajja",
                      f"{ASAVA}တို့ ကုန်ခန်းခြင်းကြောင့် {ASAVA} မရှိသော စိတ်၏ လွတ်မြောက်ခြင်း၊ ပညာဖြင့် လွတ်မြောက်ခြင်းကို "
                      "မျက်မှောက်ဘဝ၌ပင် ကိုယ်တိုင် ထူးကဲစွာ သိ၍ မျက်မှောက်ပြုပြီး ဝင်စား၍ နေ")
put("So āsavānaṃ khayā anāsavaṃ cetovimuttiṃ paññāvimuttiṃ diṭṭheva dhamme sayaṃ abhiññā sacchikatvā upasampajja "
    "viharati.", f"{SO} {_ARAHATTA}၏{END}")      # pi-2 «နေတော်မူ၏» is said of the Tathāgata: «နေ၏» here
put("Idhekacco puggalo samannāgato hoti ekantakāḷakehi akusalehi dhammehi.",
    f"{IDHA} လုံးဝ မည်းနက်သော အကုသိုလ် သဘောတရားတို့နှင့် {SAMANN}သူ {COP}{END}")
# the definitions of ch2 with other punctuation (ch8 ^4-204, ch10)
_U = F.SENT
put("Idhekacco puggalo aṭṭha vimokkhe kāyena phusitvā viharati paññāya cassa disvā āsavā parikkhīṇā honti.",
    _U["Idhekacco puggalo aṭṭha vimokkhe kāyena phusitvā viharati; paññāya cassa disvā āsavā parikkhīṇā honti"] + END)
put("Idhekacco puggalo na heva kho aṭṭha vimokkhe kāyena phusitvā viharati paññāya cassa disvā āsavā parikkhīṇā honti.",
    _U["Idhekacco puggalo na heva kho aṭṭha vimokkhe kāyena phusitvā viharati; paññāya cassa disvā āsavā parikkhīṇā "
       "honti."])
put("Idhekacco puggalo aṭṭha vimokkhe kāyena phusitvā viharati paññāya cassa disvā ekacce āsavā parikkhīṇā honti.",
    _U["Idhekacco puggalo aṭṭha vimokkhe kāyena phusitvā viharati; paññāya cassa disvā ekacce āsavā parikkhīṇā honti."])
put("Katamo ca puggalo paññāvimutto…pe… kāyasakkhī… diṭṭhippatto… saddhāvimutto… dhammānusārī ….",
    f"{N['paññāvimutto']}{F.Q_TAIL[:-1]}{PE} {N['kāyasakkhī']}{PE} {N['diṭṭhippatto']}{PE} {N['saddhāvimutto']}{PE} "
    f"{N['dhammānusārī']}{PE}{END}")
for _f in ("paññi", "saddhi"):
    _k = [k for k in M.UNIQUE if k.startswith("Yassa puggalassa sotāpattiphalasacchikiriyāya paṭipannassa " + _f)][0]
    put(_k + ".", M.UNIQUE[_k] + END)
put("Sotāpattiphalasacchikiriyāya paṭipanno puggalo saddhānusārī, phale ṭhito saddhāvimuttoti.",
    M.UNIQUE["Sotāpattiphalasacchikiriyāya paṭipanno puggalo saddhānusārī phale ṭhito saddhāvimutto."])
put("Sotāpattiphalasacchikiriyāya paṭipanno puggalo dhammānusārī, phale ṭhito diṭṭhippatto.",
    M.UNIQUE["Sotāpattiphalasacchikiriyāya paṭipanno puggalo dhammānusārī phale ṭhito diṭṭhippatto."])

# ===================================================================================== ch9 ^4-207
_MAT8 = F.LINES["Cattāro maggasamaṅgino, cattāro phalasamaṅgino puggalā."][:-1]
put("Tattha katame cattāro maggasamaṅgino, cattāro phalasamaṅgino puggalā?", f"{TATRA} {_MAT8}{Q_PL}")
_PAIRS = [(N["sotāpanno"], N["sotāpattiphalasacchikiriyāya paṭipanno"]),
          (N["sakadāgāmī"], N["sakadāgāmiphalasacchikiriyāya paṭipanno"]),
          (N["anāgāmī"], N["anāgāmiphalasacchikiriyāya paṭipanno"]),
          (N["arahā"], F.LINES["Arahattaphalasacchikiriyāya [arahattāya (sī.)] paṭipanno"])]
_M1, _M2 = _MAT8.split(f"{C} ")
put("Sotāpanno, sotāpattiphalasacchikiriyāya paṭipanno; sakadāgāmī, sakadāgāmiphalasacchikiriyāya paṭipanno; anāgāmī, "
    "anāgāmiphalasacchikiriyāya paṭipanno; arahā, arahattaphalasacchikiriyāya [arahattāya (syā. ka.) a. ni. 8.59] "
    "paṭipanno; ime cattāro maggasamaṅgino, ime cattāro phalasamaṅgino puggalā.",
    f"{C} ".join(f"{a}{C} {b}" for a, b in _PAIRS) + f"{C} ဤသူတို့သည် {_M1} ဖြစ်ကြ၏{C} ဤသူတို့သည် {_M2} ဖြစ်ကြ၏{END}")

# ===================================================================================== ch10 ^4-208
put(f"Idhekacco puggalo {SIX[0][0]}.", f"{IDHA} {SIX[0][1]}{END}")
put(f"Idhekacco puggalo {SIX[1][0]}.", f"{IDHA} {SIX[1][1]}{END}")
assert f"{IDHA} {SIX[0][1]}" == M.UNIQUE[[k for k in M.UNIQUE if k.startswith("Idhekacco puggalo pubbe") and
                                          "na ca" not in k][0]]
_TR4 = [f"“ဤသည်ကား {t}”ဟု {_KNOW}" for t in F._TR]
_TATH = _U["Tathāgatappaveditā cassa dhammā paññāya vodiṭṭhā honti vocaritā."][:-1]
_DP = ('Idhekacco puggalo "idaṃ dukkha"nti yathābhūtaṃ pajānāti…pe… "ayaṃ dukkhanirodhagāminī paṭipadā"ti yathābhūtaṃ '
       'pajānāti, tathāgatappaveditā cassa dhammā paññāya vodiṭṭhā honti vocaritā, paññāya cassa disvā ekacce āsavā '
       'parikkhīṇā honti')
put(_DP + ".", f"{IDHA} {_TR4[0]}{PE} {_TR4[3]}{C} {_TATH}{C} {F.ASAVA_SOME}{END}")
put(_DP + ", no ca kho yathā diṭṭhippattassa.",
    f"{IDHA} {_TR4[0]}{PE} {_TR4[3]}{C} {_TATH}{C} "
    f"{_U['Paññāya cassa disvā ekacce āsavā parikkhīṇā honti, no ca kho yathā diṭṭhippattassa']}{END}")

# ===================================================================================== ch11 ^4-209
_IDHA_N = F.LINES["Pañcannaṃ idha niṭṭhā, pañcannaṃ idha vihāya niṭṭhā."][:-1].split(f"{C} ")
assert _IDHA_N[0].startswith(f"ငါး{CLP}တို့၏ ") and _IDHA_N[0].endswith(" ဖြစ်၏")
put("Katamesaṃ pañcannaṃ idha niṭṭhā?", f"အဘယ် {_IDHA_N[0][:-1]}သနည်း{END}")
put("Katamesaṃ pañcannaṃ idha vihāya niṭṭhā?", f"အဘယ် {_IDHA_N[1][:-1]}သနည်း{END}")
put("Sattakkhattuparamassa kolaṅkolassa ekabījissa sakadāgāmissa yo ca diṭṭheva dhamme arahā",
    f"{C} ".join(N[k] for k in ("sattakkhattuparamo", "kolaṅkolo", "ekabījī")) +
    f"{C} {N['sakadāgāmī']}နှင့် {_DIT} {W['araha']} ဖြစ်သူ")
put("imesaṃ pañcannaṃ idha niṭṭhā.", f"ဤ {_IDHA_N[0]}{END}")
put("Antarāparinibbāyissa upahaccaparinibbāyissa asaṅkhāraparinibbāyissa sasaṅkhāraparinibbāyissa uddhaṃsotassa "
    "akaniṭṭhagāmino",
    f"{C} ".join(N[k] for k in ("antarāparinibbāyī", "upahaccaparinibbāyī", "asaṅkhāraparinibbāyī",
                                 "sasaṅkhāraparinibbāyī", "uddhaṃsoto akaniṭṭhagāmī")))
put("imesaṃ pañcannaṃ idha vihāya niṭṭhāti.", f"ဤ {_IDHA_N[1]}{END}")
put("Ettāvatā puggalānaṃ puggalapaññattīti.", f"ဤမျှသည် {F.gen_my('puggalānaṃ')} {F.pannatti_my('puggala')} ဖြစ်သည်{END}")
# «ettāvatā … paññatti» = «ဤမျှသည် … သတ်မှတ်ချက် ဖြစ်သည်» (my4_formulas.yavata_my, ch1 ^4-M-2 … ^4-M-5)

# ===================================================================================== install
for _k, _v in SENT.items():
    if _k in F.SENT and F.SENT[_k] != _v:
        raise SystemExit("table conflict: " + _k[:80])
    F.SENT[_k] = _v


# ===================================================================================== generator (as make_sample)
def write(name, txt):
    txt = unicodedata.normalize("NFC", txt)
    (OUT / name).write_text(txt, encoding="utf-8")
    print(f"wrote {name}: {sum(1 for l in txt.splitlines() if l)} lines")


def chapter(name, misses=None):
    lines = (PALI / name).read_text(encoding="utf-8-sig").splitlines()
    done = []
    for i, line in enumerate(lines):
        try:
            done.append(F.translate_line(line))
        except F.Miss as e:
            if misses is not None:
                misses.append(f"{name}:{i + 1}: {e}")
                done.append("")
                continue
            part = HERE / "scratch" / ("partial-" + name)
            part.parent.mkdir(exist_ok=True)
            part.write_text("\n".join(done) + "\n", encoding="utf-8")
            print(f"STOP {name} line {i + 1}: {e}\n  {line[:200]}\n  ({len(done)} lines kept in {part})")
            return False
    if misses is not None:
        return not misses
    write(name, "\n".join(done).rstrip("\n") + "\n")
    return True


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    names = args or NAMES_OUT
    if "--misses" in sys.argv:
        ms = []
        for n in names:
            chapter(n, ms)
        print("\n".join(ms) or "no misses")
        print(f"{len(ms)} misses")
        sys.exit(0)
    ok = True
    for n in names:
        ok = chapter(n) and ok
    sys.exit(0 if ok else 1)
