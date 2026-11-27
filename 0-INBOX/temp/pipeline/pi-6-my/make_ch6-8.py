"""Burmese zero-shot of pi-6 (Yamaka, «အတွဲလိုက် မေးဖြေခြင်း»), group ch6-8: 6-01 / 6-02 Saṅkhārayamaka, 8 Cittayamaka.

usage: python3 -I -X utf8 make_ch6-8.py [chapter ...] [--misses]
Model: make_sample.py (approved sample). Imports my6_formulas.py unchanged and only EXTENDS its tables in memory
(add_subject / add_term / PLACES / PART / H / COLO / LINES / FRAMES; group_my / place_my wrapped: the module's own
parse is tried first, so every group the sample builds comes out as in the sample). Every new value is either
read / checked in the FINAL pi-1 … pi-5 rails texts (F.W = witness, stops the run if the text drifts) or marked NEW
here and in notes-ch6-8.md. A sentence that no frame / table entry matches stops the run (Miss): nothing is guessed.
Each line is checked against its Pāli (dashes, «…», «[», item number, label, block ID, heading level, no «?» «।»
«:-», no Latin letters outside variant brackets, final «။»); a chapter is written only when every line passed.
--misses lists the unmatched lines and writes nothing.
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
NAMES_OUT = ["6-01-sankharayamaka.md", "6-02-sankharayamaka.md", "8-cittayamaka.md"]
W, C, END, PE, AND = F.W, F.C, F.END, F.PE, F.AND
NEW = {}          # NEW strings of this group (Pāli = Burmese), for the notes / check


def new(pali, my):
    NEW.setdefault(pali, my)
    return my


# ===================================================================================== terms read from pi-1 … pi-5
KAYA_S = W("5", "^5-458", "kāyasaṅkhāro", "ကိုယ်၏ ပြုပြင်ဖန်တီးမှု")     # same sense (breathing), pi-5 Kathāvatthu
VACI_S = W("5", "^5-458", "vacīsaṅkhāro", "နှုတ်၏ ပြုပြင်ဖန်တီးမှု")     # (pi-2 ^2-226 «ကိုယ် / နှုတ် / စိတ် ပြုပြင်ဖန်တီးမှု»
CITTA_S = W("5", "^5-458", "cittasaṅkhāro", "စိတ်၏ ပြုပြင်ဖန်တီးမှု")    #  = volition sense: explained exception)
SANKHARA = W("1", "^1-40", "saṅkhār", "ပြုပြင်ဖန်တီးမှု", key="saṅkhāro")
KAYA = W("2", "^2-226", "Kāyasañcetanā", "ကိုယ်", key="kāyo")
VACI = W("5", "^5-332", "vacībhedo", "နှုတ်", key="vacī")
CITTA = W("1", "^1-6", "cittaṃ", "စိတ်", key="cittaṃ")
ASSASA = W("5", "^5-333", "assāsapassāsā", "ဝင်လေ ထွက်လေ")
VV = W("5", "^5-332", "Vitakkavicārā vacīsaṅkhārā", "စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှု", key="vitakkavicārā")
VV_GEN = W("1", "^1-161", "vitakkavicārānaṃ", "စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှုတို့", key="vitakkavicārānaṃ")
SANNA_VEDANA = W("5", "^5-333", "saññā ca vedanā ca", "မှတ်သိမှုနှင့် ခံစားမှု")
SAVV = W("1", "^1-M1-6", "savitakkasavicārā dhammā", "စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှု ရှိသော", key="savitakkasavicāra")
AVV = W("1", "^1-1401", "avitakkaavicārā", "စတင်ကြံစည်မှုလည်း မရှိ၊ ဆက်လက်သုံးသပ်မှုလည်း မရှိသော",
        key="avitakkaavicāra")
BHUMI = W("1", "^1-988", "Sukhabhūmiyaṃ", "ရှိရာ အဆင့်၌", key="-bhūmiyaṃ")       # «သာယာမှု ရှိရာ အဆင့်၌»
CITTA_SAMP = W("1", "^1-M2-58", "cittasampayuttā dhammā", "စိတ်နှင့် ယှဉ်တွဲသော", key="cittasampayutta")
W("1", "^1-1308", "Sabbepi kusalā dhammā", "ကုသိုလ် သဘောတရား အားလုံးသည်", key="sabbepi … dhammā")
UPPADAK = W("5", "^5-366", "Uppādakkhaṇe", "ဖြစ်ခြင်း ခဏ၌", key="uppādakkhaṇe")
BHANGAK = W("5", "^5-366", "bhaṅgakkhaṇe", "ပြိုပျက်ခြင်း ခဏ၌", key="bhaṅgakkhaṇe")
KHANA_ACC = {"uppādakkhaṇaṃ": UPPADAK[:-1] + "ကို", "bhaṅgakkhaṇaṃ": BHANGAK[:-1] + "ကို"}   # «… ခဏကို»
VINA = W("5", "^5-227", "vinā rūpena", "မပါဘဲ", key="vinā X-ehi")                # «ရုပ် မပါဘဲ»
SAMANGI = W("2", "^2-809", "kāyaduccaritasamaṅgī", "နှင့် ပြည့်စုံသူ", key="-samaṅgī")
ANANTARA = W("5", "^5-687", "anantarā", "၏ ချက်ချင်း နောက်၌", key="X-assa anantarā")
VATTAMANE = W("5", "^5-556", "citte vattamāne", "စိတ် ဖြစ်နေစဉ်", key="citte vattamāne")
DUTIYA = W("1", "^1-146", "Dutiyaṃ cittaṃ", "ဒုတိယ စိတ်", key="dutiya citta")
UPPANNA = W("1", "^1-1", "cittaṃ uppannaṃ hoti", "ဖြစ်ပေါ်ပြီးသော", key="uppanna")[:-3]   # «ဖြစ်ပေါ်ပြီး»
NIRUDDHA = W("5", "^5-333", "niruddhā hoti", "ချုပ်ငြိမ်းပြီး ဖြစ်သည်", key="niruddha")[:-len(" ဖြစ်သည်")]
MANA = W("5", "^5-366", "vimuccamānanti", "လွတ်မြောက်ဆဲ", key="-māna (participle)")[-2:]   # «ဆဲ»
PARIJANATI = W("5", "^5-390", "parijānāti", "ပိုင်းခြား သိ", key="parijānāti")
PARINNA = W("4", "^4-130", "pariññaṃ", "ပိုင်းခြား သိခြင်း", key="pariññā")
ATIKKANTA = W("2", "^2-609", "atikkanto hoti vītikkanto", "ကျော်လွန်ပြီး ဖြစ်၏၊ လွန်မြောက်ပြီး", key="atikkanta / vītikkanta")
VITIKKANTA_W, ATIKKANTA_W = "လွန်မြောက်", "ကျော်လွန်"
NIRODHA_SAM = W("5", "^5-458", "nirodhaṃ samāpajjantassa", "ချုပ်ငြိမ်းခြင်း သမာပတ်ကို ဝင်စားနေသူ",
                key="nirodhasamāpanna")
SAMAPANNA = W("5", "^5-333", "Tatiyaṃ jhānaṃ samāpannassa", "တတိယ ဈာန်ကို ဝင်စားနေသူ", key="X-jhānaṃ samāpanna")
JHANA = {"paṭhamajjhāna": W("5", "^5-332", "paṭhamaṃ jhānaṃ samāpannassa", "ပထမ ဈာန်", key="paṭhamajjhāna"),
         "dutiyajjhāna": W("5", "^5-333", "Dutiyassa jhānassa", "ဒုတိယ ဈာန်", key="dutiyajjhāna"),
         "tatiyajjhāna": W("5", "^5-333", "Tatiyaṃ jhānaṃ", "တတိယ ဈာန်", key="tatiyajjhāna"),
         "catutthajjhāna": W("5", "^5-333", "catutthaṃ jhānaṃ", "စတုတ္ထ ဈာန်", key="catutthajjhāna")}
PLANE = {"kāmāvacara": W("1", "^1-990", "kāmāvacare", "ကာမဘုံ", key="kāmāvacara (plane)"),
         "rūpāvacara": W("1", "^1-990", "rūpāvacare", "သိမ်မွေ့သော ရုပ်ဘုံ", key="rūpāvacara (plane)"),
         "arūpāvacara": W("1", "^1-990", "arūpāvacare", "ရုပ်မရှိသော ဘုံ", key="arūpāvacara (plane)")}
KAMA_ADJ = W("1", "^1-1", "kāmāvacaraṃ kusalaṃ cittaṃ", "ကာမဘုံနှင့် ဆိုင်သော", key="kāmāvacara (adjective)")
EVA = W("5", "^5-241", "arahattaṃyeva", "ပင်", key="-yeva")
# citta qualifiers (pi-2 ^2-365 cittānupassanā list; pi-1 kusala / akusala citta; pi-1 Mātikā saraṇa / araṇa)
QUAL = {}
for _p, _m in (("sarāgaṃ", "ရာဂ ရှိသော"), ("vītarāgaṃ", "ရာဂ ကင်းသော"), ("sadosaṃ", "ဒေါသ ရှိသော"),
               ("vītadosaṃ", "ဒေါသ ကင်းသော"), ("samohaṃ", "မောဟ ရှိသော"), ("vītamohaṃ", "မောဟ ကင်းသော"),
               ("saṃkhittaṃ", "တွန့်ဆုတ်နေသော"), ("vikkhittaṃ", "ပျံ့လွင့်နေသော"), ("mahaggataṃ", "ကြီးမြတ်သော"),
               ("amahaggataṃ", "မကြီးမြတ်သော"), ("sauttaraṃ", "ထိုထက် သာလွန်သည် ရှိသေးသော"),
               ("anuttaraṃ", "ထိုထက် သာလွန်သည် မရှိသော"), ("samāhitaṃ", "တည်ကြည်သော"), ("asamāhitaṃ", "မတည်ကြည်သော"),
               ("vimuttaṃ", "လွတ်မြောက်သော"), ("avimuttaṃ", "မလွတ်မြောက်သော")):
    QUAL[_p] = W("2", "^2-365", _p, _m + " စိတ်", key=f"{_p} cittaṃ")
QUAL["kusalaṃ"] = W("1", "^1-1", "kusalaṃ cittaṃ", "ကုသိုလ်စိတ်", key="kusalaṃ cittaṃ")
QUAL["akusalaṃ"] = W("1", "^1-365", "akusalaṃ cittaṃ", "အကုသိုလ်စိတ်", key="akusalaṃ cittaṃ")
QUAL["abyākataṃ"] = W("5", "^5-556", "kusalābyākate citte", f"{F.ABY} စိတ်", key="abyākataṃ cittaṃ")
QUAL["sukhāya vedanāya sampayuttaṃ"] = W("1", "^1-988", "sukhāya vedanāya sampayuttā",
                                         "သာယာသော ခံစားမှုနှင့် ယှဉ်တွဲသော", key="sukhāya vedanāya sampayutta") + " စိတ်"
QUAL["araṇaṃ"] = W("1", "^1-M2-100", "araṇā dhammā", "ပဋိပက္ခ မရှိသော", key="araṇa") + " စိတ်"
SARANA = W("1", "^1-M2-100", "saraṇā dhammā", "ပဋိပက္ခ ရှိသော", key="saraṇa")
QUALS = "|".join(sorted(map(re.escape, QUAL), key=len, reverse=True))

# ===================================================================================== NEW strings of this group
PACCHIMA_CITTA = new("pacchimacitta", "နောက်ဆုံး စိတ်")        # pacchima as in the sample «နောက်ဆုံး ဘဝ»
YO, SO = new("yo … so … (pariññāvāra)", "အကြင်သူသည်"), "ထိုသူသည်"
YAM, TAM = new("yaṃ cittaṃ … taṃ cittaṃ", "အကြင်"), "ထို"
OWN_MIND = new("yassa cittassa anantarā", "မိမိ စိတ်")           # «မိမိ စိတ်၏ ချက်ချင်း နောက်၌ …»
SO_Q = new("tassa cittaṃ? ((14) question without a predicate)", "ထိုသို့ ဖြစ်သလော")
# harmonise B4: «အနက်» (ch2-02-4-5 / ch3 / ch10b / ch10c, majority) for the earlier «ထဲမှ»
AMONG = new("tesaṃ cavantānaṃ (after «ye ca …»)", "အနက်")      # «… ပြုမည့်သူတို့အနက် စုတေဆဲသူတို့»
SAMANNA = new("-sāmañña (Suddhacittasāmaññaṃ)", "အထွေထွေ")
ADDITIONAL = new("uppajjamānaṃ / nirujjhamānaṃ khaṇaṃ khaṇaṃ vītikkantaṃ atikkantakālaṃ",
                 "ခဏ ခဏကို လွန်မြောက်ပြီး ကာလ ကျော်လွန်ပြီး")

# ===================================================================================== module tables extended
for p, m in (("kāyasaṅkhāro", KAYA_S), ("vacīsaṅkhāro", VACI_S), ("cittasaṅkhāro", CITTA_S), ("cittaṃ", CITTA)):
    F.add_subject(p, m)
F.add_term("kāyo", KAYA, acc="kāyaṃ")
F.add_term("vacī", VACI, acc="vaciṃ")
F.add_term("cittaṃ", CITTA)
F.add_term("saṅkhāro", SANKHARA)
F.add_term("kāyasaṅkhāro", KAYA_S, acc="kāyasaṅkhāraṃ")
F.add_term("vacīsaṅkhāro", VACI_S, acc="vacīsaṅkhāraṃ")
F.add_term("cittasaṅkhāro", CITTA_S, acc="cittasaṅkhāraṃ")
F.PLACES.update(JHANA)
F.PLACES.update(PLANE)
F.PART["samāpannānaṃ"] = (SAMAPANNA[len("တတိယ ဈာန်ကို "):-len("သူ")], "ကို")   # «… ဈာန်ကို ဝင်စားနေသူတို့»

# ===================================================================================== persons and moments
MOMENT_END = {"uppādakkhaṇe": UPPADAK, "bhaṅgakkhaṇe": BHANGAK}
CMOD = {"pacchima": "နောက်ဆုံး", "savitakkasavicāra": SAVV, "avitakkaavicāra": AVV, "sarāga": "ရာဂ ရှိသော",
        "kusala": "ကုသိုလ်"}
CMOD_RE = re.compile("(" + "|".join(sorted(CMOD, key=len, reverse=True)) + ")")


def citta_np(pre):
    """'' / 'pacchima' / 'sarāgapacchima' / 'pacchimakusala' / 'avitakkaavicāra' … -> «… စိတ်»."""
    mods = []
    while pre:
        m = CMOD_RE.match(pre)
        if not m:
            raise F.Miss("citta modifier: " + pre)
        mods.append(CMOD[m[1]])
        pre = pre[m.end():]
    out = " ".join(mods + [CITTA])
    return out.replace("ကုသိုလ် စိတ်", QUAL["kusalaṃ"])


GEN_RE = re.compile(r"^(?P<pre>\w*?)cittassa$")


def gen_np(t):
    """genitive of a moment: cittassa / pacchimacittassa … / assāsapassāsānaṃ / vitakkavicārānaṃ -> «…၏»."""
    tl = t.lower()
    if tl == "assāsapassāsānaṃ":
        return ASSASA + "တို့၏"
    if tl == "vitakkavicārānaṃ":
        return VV_GEN + "၏"
    m = GEN_RE.match(tl)
    if m:
        return citta_np(m["pre"]) + "၏"
    return None


VINA_OBJ = {"assāsapassāsehi": ASSASA, "vitakkavicārehi": VV}


def moment_at(toks, i):
    """[vinā X-ehi] GEN uppādakkhaṇe / bhaṅgakkhaṇe, or dutiye citte vattamāne -> (adverbial Burmese, next index)."""
    j, pre = i, ""
    if j + 1 < len(toks) and toks[j].lower() == "vinā" and toks[j + 1].lower() in VINA_OBJ:
        pre = f"{VINA_OBJ[toks[j + 1].lower()]} {VINA} "
        j += 2
    if [x.lower() for x in toks[j:j + 3]] == ["dutiye", "citte", "vattamāne"] and not pre:
        return f"{DUTIYA} ဖြစ်နေစဉ်", j + 3
    if j + 1 < len(toks) and toks[j + 1].lower() in MOMENT_END:
        g = gen_np(toks[j])
        if g:
            return f"{pre}{g} {MOMENT_END[toks[j + 1].lower()]}", j + 2
    return None


SAMANGI_RE = re.compile(r"^(?P<pre>\w*?)cittasamaṅgīnaṃ$")
REL_OBJ = {"avitakkaavicāraṃ": AVV, "kāmāvacarānaṃ": KAMA_ADJ}
BHUMI_RE = re.compile(r"^(?P<b>savitakkasavicāra|avitakkaavicāra)bhūmiyaṃ$")
BHUMI_PRE = {"savitakkasavicāra": SAVV[:-len("ရှိသော")], "avitakkaavicāra": AVV[:-len("ရှိသော")]}


def loc_at(toks, i):
    """loc. planes / jhānas / -bhūmiyaṃ (a place before a person or moment) -> (Burmese «…၌», next index)."""
    keys, j = [], i
    while j < len(toks):
        f = F._place_form(toks[j])
        if f and f[1] == "loc":
            keys.append(("p", f[0]))
        elif BHUMI_RE.match(toks[j].lower()):
            keys.append(("b", BHUMI_RE.match(toks[j].lower())["b"]))
        else:
            break
        j += 1
    if not keys:
        return None
    if all(k == "p" for k, _ in keys):
        return F._join_places([v for _, v in keys]) + F.LOC, j
    if len(keys) == 1:
        return f"{BHUMI_PRE[keys[0][1]]}{BHUMI}", j
    raise F.Miss("mixed places: " + " ".join(toks[i:j]))


def person_at(toks, i):
    """this group's own person phrases -> (Burmese «…သူတို့», next index) or None."""
    tl = [x.lower() for x in toks]
    t = tl[i]
    if t == "nirodhasamāpannānaṃ":
        return f"{NIRODHA_SAM}တို့", i + 1
    m = SAMANGI_RE.match(t)
    if m:
        return f"{citta_np(m['pre'])}{SAMANGI}တို့", i + 1
    if t == "itaresaṃ" and loc_at(toks, i + 1) and loc_at(toks, i + 1)[1] == len(toks):
        return f"{loc_at(toks, i + 1)[0]} {F.HAS}သော {F.OTHERS}", len(toks)
    if t == "itaresaṃ" and i + 1 < len(toks) and SAMANGI_RE.match(tl[i + 1]):
        m = SAMANGI_RE.match(tl[i + 1])
        return f"{citta_np(m['pre'])}{SAMANGI[:-len('သူ')]}သော {F.OTHERS}", i + 2
    if tl[i:i + 3] == ["yassa", "cittassa", "anantarā"] and i + 6 <= len(toks) and tl[i + 4] == "pacchimacittaṃ":
        obj = REL_OBJ[tl[i + 3]]
        v = F.V(toks[i + 5], "attr")
        return f"{OWN_MIND}{ANANTARA} {obj} {PACCHIMA_CITTA} {v}{F.THEM}", i + 6
    if tl[i:i + 2] == ["ye", "ca"]:
        j, keys = i + 2, []
        while j < len(toks) and F._place_form(toks[j]) and F._place_form(toks[j])[1] == "acc":
            keys.append(F._place_form(toks[j])[0])
            j += 1
        if tl[j:j + 2] == ["upapajjitvā", "parinibbāyissanti"]:
            out = f"{F._join_places(keys)}{F.LOC} ပြန်လည် ဖြစ်ပေါ်ပြီး ပရိနိဗ္ဗာန် ပြုမည့်{F.THEM}"
            j += 2
            if tl[j:j + 2] == ["tesaṃ", "cavantānaṃ"]:
                out += f"{AMONG} {F.PART['cavantānaṃ'][0]}{F.THEM}"
                j += 2
            return out, j
    return None


FLAGS = {"sabbesaṃ": "all", "itaresaṃ": "other", "tesaṃyeva": "same"}


def items_of(toks):
    """token list -> [(kind, Burmese)], kind P (person), M (moment), L (place before), F (flag before a moment)."""
    out, i = [], 0
    while i < len(toks):
        r = moment_at(toks, i)
        if r:
            out.append(("M", r[0]))
            i = r[1]
            continue
        t = toks[i].lower()
        if t in FLAGS and moment_at(toks, i + 1):
            out.append(("F", FLAGS[t]))
            i += 1
            continue
        r = person_at(toks, i)
        if r:
            if r[0] is None:
                raise F.Miss("relative clause: " + " ".join(toks[i:]))
            out.append(("P", r[0]))
            i = r[1]
            continue
        r = loc_at(toks, i)
        if r and r[1] == len(toks):                           # a place alone before «tesaṃ»: «X၌ ရှိသူတို့»
            out.append(("P", f"{r[0]} {F.HAS}{F.THEM}"))
            i = r[1]
            continue
        if r and r[1] < len(toks) and toks[r[1]].lower() not in F.PART and toks[r[1]].lower() != "pacchimabhavikānaṃ":
            out.append(("L", r[0]))
            i = r[1]
            continue
        rest = list(toks[i:])
        n0 = len(rest)
        out.append(("P", F._one_group(rest)))
        i += n0 - len(rest)
    return out


def units_of(items):
    """harmonise B1 / B6: the ch. 5 lead style (ch2-02-4-5, ch9-10a, ch10b, ch10c): a moment is its own adverbial unit
    (kind M), a person group its own unit (kind P); sabbesaṃ before a moment «သူ အားလုံးတို့၏ M», tesaṃyeva before a
    moment «ထိုသူတို့၏ပင် M» (as the ch. 5 inner «tesaṃ + moment» «ထိုသူတို့၏ M», eva «ပင်» after the case as ch7a
    «ထိုပုဂ္ဂိုလ်တို့အားပင်»), itaresaṃ before a moment the unit «အခြားသူတို့» then M (as ch9-10a «အခြားသူတို့၊ …»);
    a place before (L) is put in front of the next unit. -> [(kind, Burmese)]."""
    units, loc, k = [], "", 0
    while k < len(items):
        kind, s = items[k]
        if kind == "L":
            loc = s + " "
            k += 1
            continue
        if kind == "F":
            adv = items[k + 1][1]
            if s == "other":
                units.append(("P", loc + F.OTHERS))
                units.append(("M", adv))
            else:
                pre = {"all": f"{F.ALL_OF}၏ ", "same": f"{F.THEM.replace('သူ', 'ထိုသူ')}၏{EVA} "}[s]
                units.append(("M", loc + pre + adv))
            k += 2
        else:
            units.append((kind, loc + s))
            k += 1
        loc = ""
    if loc:
        raise F.Miss("place without a person")
    return units


def join_units(units):
    """Consecutive person units joined as the module joins groups («A၊ Bနှင့် C»), the rest with «၊ »; a final moment
    is followed by «ထိုသူတို့» (+ «အား» from the module's who_my), as ch. 5 «… ခဏ၌ ထိုသူတို့အား»."""
    segs, run = [], []
    for kind, txt in units:
        if kind == "P":
            run.append(txt)
            continue
        if run:
            segs.append(run[0] if len(run) == 1 else f"{C} ".join(run[:-1]) + f"{AND} " + run[-1])
            run = []
        segs.append(txt)
    if run:
        segs.append(run[0] if len(run) == 1 else f"{C} ".join(run[:-1]) + f"{AND} " + run[-1])
    out = f"{C} ".join(segs)
    return out + (" " + F.PRO["tesaṃ"][:-len(F.DAT)] if units[-1][0] == "M" else "")


_group_my0, _place_my0 = F.group_my, F.place_my


def group_my(g):
    try:
        return _group_my0(g)
    except F.Miss:
        pass
    toks = g.strip().replace(",", "").split()
    return join_units(units_of(items_of(toks)))


def place_my(g):
    try:
        return _place_my0(g)
    except F.Miss:
        pass
    r = loc_at(g.split(), 0)
    if not r or r[1] != len(g.split()):
        raise F.Miss("place: " + g)
    return r[0]


F.group_my, F.place_my = group_my, place_my

# ===================================================================================== predicates (citta chapter)
PARTICIPLE = {"uppannaṃ": UPPANNA, "uppajjamānaṃ": F.VERB["uppajj"] + MANA,
              "nirujjhamānaṃ": F.VERB["nirujjh"] + MANA, "niruddhaṃ": NIRUDDHA}
PART_ATTR = {"uppannaṃ": UPPANNA + "သော", "uppajjamānaṃ": F.VERB["uppajj"] + MANA,
             "nirujjhamānaṃ": F.VERB["nirujjh"] + MANA, "niruddhaṃ": NIRUDDHA + "သော"}
BE, ISNT = F.BE, F.NEGV[F.BE]


def unquote(w):
    """the «-ti» of a quoted predicate: uppannanti -> uppannaṃ, nirujjhatīti -> nirujjhati, …"""
    if w.endswith("nti") and (w[:-3] + "ṃ") in PARTICIPLE:
        return w[:-3] + "ṃ"
    for a, b in (("īti", "i"), ("āti", "a")):
        if w.endswith(a):
            return w[:-len(a)] + b
    return w


class El:
    """one predicate element: a finite verb (root, tense, neg) or a participle (stem, neg)."""

    def __init__(self, w, neg=False):
        w = unquote(w)
        if w in PARTICIPLE:
            self.kind, self.stem, self.neg = "p", PARTICIPLE[w], neg
        else:
            r, t, n = F.pali_verb(w)
            self.kind, self.root, self.tense, self.neg = "v", r, t, (n or neg)

    def _fin(self, form):
        return F.my_verb(self.root, self.tense, self.neg, form)

    def cl(self):
        return self._fin("cl") if self.kind == "v" else f"{self.stem} {ISNT if self.neg else BE + '၏'}"

    def q(self):
        return self._fin("q") if self.kind == "v" else f"{self.stem} {ISNT if self.neg else BE}သလော"

    def st(self):
        return self._fin("stmt") if self.kind == "v" else f"{self.stem} {ISNT if self.neg else BE + 'သည်'}"

    def butnot(self):
        """after «no ca»: a positive Pāli element is negated, a negative one becomes «… ကား မဟုတ်»."""
        if self.kind == "v":
            return F.not_so(self.root, self.tense) if self.neg else F.my_verb(self.root, self.tense, True)
        return f"{self.stem} {ISNT}သည်{F.NOT_SO}" if self.neg else f"{self.stem} {ISNT}"

    def also(self):
        """«… ceva … ca» / «na ceva … na ca …»: «Vသည်လည်း ဖြစ်» / «Pလည်း ဖြစ်» / «Pလည်း မဟုတ်»."""
        if self.kind == "v":
            v = self._fin("stmt")
            if self.neg and self.tense != "fut":
                v += "သည်"
            return f"{v}လည်း {BE}"
        return f"{self.stem}လည်း {ISNT if self.neg else BE}"

    def conj(self):
        """first verb of «V1 na V2» / «na V1 V2»: «V1သော်လည်း» (fut «V1လိမ့်မည် ဖြစ်သော်လည်း»)."""
        v = self._fin("stmt")
        if self.tense == "fut":
            return f"{v} {BE}သော်လည်း"
        return (v if self.neg else v[:-len("သည်")]) + "သော်လည်း"


def also_join(els):
    s = f"{C} ".join(e.also() for e in els)
    return s + ("သည်" if s.endswith(BE) else "")


class Pred:
    """a predicate: one element, a pair «V1 na V2» (conj), «A ceva B ca» / «na ceva A na ca B» (also), or the
    (14) atikkantakāla pair."""

    def __init__(self, s):
        s = s.strip()
        self.kind = None
        m = re.fullmatch(r"(?P<n1>na )?(?P<a>uppajjamānaṃ|nirujjhamānaṃ) khaṇaṃ khaṇaṃ vītikkantaṃ atikkantakālaṃ, "
                         r"(?P<n2>na )?(?P<b>uppajjamānaṃ|nirujjhamānaṃ) khaṇaṃ khaṇaṃ vītikkantaṃ atikkantakālaṃ", s)
        if m:
            self.kind = "14"
            self.e = [(PARTICIPLE[m["a"]] + " " + ADDITIONAL, bool(m["n1"])),
                      (PARTICIPLE[m["b"]] + " " + ADDITIONAL, bool(m["n2"]))]
            return
        m = re.fullmatch(r"na ceva (?P<a>\S+) na ca (?P<b>\S+)", s)
        if m:
            self.kind, self.e = "also", [El(m["a"], True), El(m["b"], True)]
            return
        m = re.fullmatch(r"(?P<n>na )?(?P<a>\S+?)(?:ñceva| ceva) (?P<b>\S+?)(?:ñca| ca)", s)
        if m:
            a = m["a"] + ("ṃ" if s.split()[0 if not m["n"] else 1].endswith("ñceva") else "")
            b = m["b"] + ("ṃ" if s.endswith("ñca") else "")
            self.kind, self.e = "also", [El(a, bool(m["n"])), El(b)]
            return
        m = re.fullmatch(r"(?P<n1>na )?(?P<a>\S+) (?P<n2>na )?(?P<b>\S+)", s)
        if m and bool(m["n1"]) != bool(m["n2"]):
            self.kind, self.e = "pair", [El(m["a"], bool(m["n1"])), El(m["b"], bool(m["n2"]))]
            if self.e[0].kind != "v" or self.e[1].kind != "v":
                raise F.Miss("pair: " + s)
            return
        m = re.fullmatch(r"(?P<n>na )?(?P<a>\S+)", s)
        if m:
            self.kind, self.e = "one", [El(m["a"], bool(m["n"]))]
            return
        raise F.Miss("predicate: " + s)

    def _14(self, last):
        (a, na), (b, nb) = self.e
        first = f"{a} {ISNT}ဘဲ" if na else f"{a} {BE}၍"
        return first, b, nb

    def cl(self):
        if self.kind == "14":
            first, b, nb = self._14(True)
            return f"{first} {b} {ISNT if nb else BE + '၏'}"
        if self.kind == "pair":
            return f"{self.e[0].conj()} {self.e[1].cl()}"
        if self.kind == "one":
            return self.e[0].cl()
        raise F.Miss("clause of " + self.kind)

    def q(self):
        if self.kind == "pair":
            return f"{self.e[0].conj()} {self.e[1].q()}"
        if self.kind == "one":
            return self.e[0].q()
        raise F.Miss("question of " + self.kind)

    def st(self):
        if self.kind == "pair":
            return f"{self.e[0].conj()} {self.e[1].st()}"
        if self.kind == "one":
            return self.e[0].st()
        if self.kind == "also":
            return also_join(self.e)
        raise F.Miss("statement of " + self.kind)

    def butnot(self):
        if self.kind == "one":
            return self.e[0].butnot()
        raise F.Miss("no ca of " + self.kind)


def subj_c(q, cl=None):
    """the citta subject: «စိတ်» / qualified «ရာဂ ရှိသော စိတ်»; with yaṃ «အကြင်စိတ်», with taṃ «ထိုစိတ်»."""
    base = QUAL[q] if q else CITTA
    if cl == "yaṃ":
        return YAM + (" " if q else "") + base
    if cl == "taṃ":
        return TAM + (" " if q else "") + base
    return base


CLC = r"(?P<cl>[Yy]assa vā pana yaṃ|[Yy]assa yaṃ|[Yy]aṃ vā pana|[Yy]aṃ|[Yy]assa vā pana|[Yy]assa)"
Q_CIT = re.compile(rf"^{CLC} (?:(?P<q1>{QUALS}) )?cittaṃ (?P<p1>.+?)(?: no ca (?P<nc>tassa taṃ|tassa|taṃ) "
                   rf"(?:(?P<q3>{QUALS}) )?cittaṃ (?P<p3>.+?),)? (?P<ft>tassa taṃ|tassa|taṃ) (?:(?P<q2>{QUALS}) )?"
                   rf"(?:cittaṃ|cittanti)(?: (?P<p2>.+?))?[?.]$")


def dat_subj(cl, q, first=True):
    """(clause word, subject) for yassa / yaṃ / yassa yaṃ (first) or tassa / taṃ / tassa taṃ (second)."""
    c = cl.lower().replace(" vā pana", "")
    person = c.startswith(("yassa", "tassa"))
    thing = c.endswith(("yaṃ", "taṃ"))
    pw = (F.CL["yassa"][0] if first else F.FT["tassa"]) if person else ""
    s = subj_c(q, ("yaṃ" if first else "taṃ") if thing else None)
    if not person:
        s += "သည်"              # no dative: the subject takes «သည်»
    return (pw + " " if pw else "") + s


def q_citta(m):
    pre = F.VA_PANA + " " if " vā pana" in m["cl"] else ""
    out = f"{pre}{dat_subj(m['cl'], m['q1'])} {Pred(m['p1']).cl()}{C} "
    if m["nc"]:
        out += f"{F.BUT} {dat_subj(m['nc'], m['q3'], False)} {Pred(m['p3']).butnot()}{C} "
    p2 = Pred(m["p2"]).q() if m["p2"] else SO_Q
    return out + f"{dat_subj(m['ft'], m['q2'], False)} {p2}{END}"


# answers: persons («who tesaṃ …»), phenomena («Subject cittaṃ …») and bare (12) / (13)
DSUBJ = {"Bhaṅgakkhaṇe cittaṃ": f"{BHANGAK} {F.HAS}သော {CITTA}",
         "Uppādakkhaṇe cittaṃ": f"{UPPADAK} {F.HAS}သော {CITTA}",
         "Atītaṃ cittaṃ": f"{F.TIMES['Atīta']} {CITTA}", "Anāgataṃ cittaṃ": f"{F.TIMES['Anāgata']} {CITTA}",
         "Paccuppannaṃ cittaṃ": f"{F.TIMES['Paccuppanna']} {CITTA}",
         "Atītānāgataṃ cittaṃ": f"{F.TIMES['Atīta']} {CITTA}{AND} {F.TIMES['Anāgata']} {CITTA}"}
for _k, _t in (("Bhaṅgakkhaṇe", "anāgata"), ("Bhaṅgakkhaṇe", "atīta"), ("Uppādakkhaṇe", "anāgata")):
    DSUBJ[f"{_k} {_t}ñca cittaṃ"] = (f"{DSUBJ[_k + ' cittaṃ']}{AND} "
                                     f"{F.TIMES[_t[0].upper() + _t[1:]]} {CITTA}")
DSUBJ["Uppādakkhaṇe anāgataṃ cittaṃ"] = DSUBJ["Uppādakkhaṇe anāgatañca cittaṃ"]
DBARE = {"Bhaṅgakkhaṇe": BHANGAK, "Uppādakkhaṇe": UPPADAK}
DS = "|".join(sorted(map(re.escape, DSUBJ), key=len, reverse=True))
A_PER = re.compile(rf"^(?P<who>.+?) tesaṃ (?:(?P<q>{QUALS}) )?cittaṃ (?P<rest>.+)\.$")
A_DHA = re.compile(rf"^(?P<s>{DS}) (?P<rest>.+)\.$")
A_BARE = re.compile(r"^(?P<s>Bhaṅgakkhaṇe|Uppādakkhaṇe) (?P<rest>.+)\.$")
NOCA = re.compile(rf"^(?P<a>.+?), no ca (?:(?P<pro>tesaṃ|tassa taṃ|taṃ) (?:(?P<q>{QUALS}) )?cittaṃ )?(?P<b>.+)$")


def rest_my(rest, pro_my):
    """predicate part of an answer: «A, no ca PRO cittaṃ B» / «A, B» / «A»."""
    m = NOCA.match(rest)
    if m:
        pro = ""
        if m["pro"]:
            pro = {"tesaṃ": F.PRO["tesaṃ"], "tassa taṃ": f"{F.FT['tassa']} {subj_c(m['q'], 'taṃ')}",
                   "taṃ": subj_c(m["q"], "taṃ") + "သည်"}[m["pro"]]
            if m["pro"] == "tesaṃ":
                pro += " " + subj_c(m["q"])
        return f"{Pred(m['a']).st()}{C} {F.BUT} {pro + ' ' if pro else ''}{Pred(m['b']).butnot()}"
    parts = re.split(r", (?=(?:na )?\S+ (?:na |ceva ))", rest)
    return f"{C} ".join(Pred(p).st() for p in parts)


SENT = {}          # whole sentences that no frame builds (hand-written), Pāli -> Burmese


def citta_sentence(s):
    if s in SENT:
        return SENT[s]
    m = Q_CIT.match(s)
    if m:
        return q_citta(m)
    m = A_PER.match(s)
    if m:
        return f"{F.who_my(m['who'], 'tesaṃ')} {subj_c(m['q'])} {rest_my(m['rest'], None)}{END}"
    m = A_DHA.match(s)
    if m:
        return f"{DSUBJ[m['s']]}သည် {rest_my(m['rest'], None)}{END}"
    m = A_BARE.match(s)
    if m:
        return f"{DBARE[m['s']]} {rest_my(m['rest'], None)}{END}"
    m = re.fullmatch(r"(?P<n1>na )?(?P<a>\S+) (?P<n2>na )?(?P<b>\S+?)[?.]", s)
    if m and unquote(m["a"]) in PARTICIPLE and unquote(m["b"]) in PARTICIPLE and bool(m["n1"]) == bool(m["n2"]):
        a, b = unquote(m["a"]), unquote(m["b"])
        if m["n1"]:
            return f"{PARTICIPLE[a]} {ISNT}သော {F.THING}သည် {PARTICIPLE[b]} {ISNT}သလော{END}"
        return f"{PART_ATTR[a]} {F.THING}သည် {PARTICIPLE[b]} {BE}သလော{END}"
    m = re.fullmatch(r"(?P<v>Uppannaṃ)\.", s)
    if m:
        return El("uppannaṃ").st() + END
    return None


# ===================================================================================== saṅkhāra chapter frames
def sankhara_sentence(s):
    # «X na Y, X.» (the sample's P4 with any term as subject)
    m = re.fullmatch(r"(?P<s>\S+) na (?P<b>\S+), (?P<a>\S+)\.", s)
    if m:
        S, A, B = F.term(m["s"]), F.term(m["a"]), F.term(m["b"])
        return f"{S[0]}သည် {F.isnt(B[0], False)}{C} {F.is_(A[0], False)}{END}"
    # pariññāvāra: yo X-aṃ parijānāti so Y-aṃ parijānātīti?
    m = re.fullmatch(r"(?P<yo>[Yy]o vā pana|[Yy]o) (?P<x>\S+) parijānāti so (?P<y>\S+) parijānātīti\?", s)
    if m:
        pre = F.VA_PANA + " " if "vā pana" in m["yo"] else ""
        return f"{pre}{YO} {F.term(m['x'])[0]}ကို {PARIJANATI}၏{C} {SO} {F.term(m['y'])[0]}ကို {PARIJANATI}သလော{END}"
    # the slip ^6-6-121: «… tesaṃ tattha X na nirujjhittha Y ca nirujjhissati.» (translated as written)
    m = re.fullmatch(rf"(?P<who>.+?) (?P<pro>tesaṃ tattha|tesaṃ|tattha) (?P<x>\S+) na (?P<v1>{F.VB[11:]}) "
                     rf"(?P<y>\S+) ca (?P<v2>{F.VB})\.", s)
    if m:
        return (f"{F.who_my(m['who'], m['pro'])} {F.subj(m['x'])} {F.V('na ' + m['v1'])}{C} "
                f"{F.subj(m['y'])}လည်း {F.V(m['v2'])}{END}")
    return None


F.FRAMES.extend([sankhara_sentence, citta_sentence])

# ===================================================================================== «…pe…» lines
FRAG_CL = re.compile(rf"^{F.CLR} (?:(?P<q>{QUALS}) )?(?P<x>\S+) (?P<p>(?:na )?{F.VB[11:]}(?: (?:na )?{F.VB[11:]})?)"
                     r"(?P<ft> tassa)?$")
NOTE = {}          # editorial notes in round brackets, Pāli (with brackets) -> Burmese


def fragment(t):
    """one piece of a «…pe…» line."""
    t0 = t.strip()
    if not t0:
        return ""
    # harmonise B15 (align_check «(Kha) yassa vā pana yattha…pe…?»): a question cut before its verb «…pe…?» =
    # «…လော။» (ch3 / ch2-02-4-5 / ch7a), not «…။»
    if t0[0] in "?." and len(t0) > 1:
        return ("လော" if t0[0] == "?" else "") + END + " " + fragment(t0[1:])
    if t0 in ("?", "."):
        return ("လော" if t0 == "?" else "") + END
    if t0 in NOTE:
        return NOTE[t0]
    parts = F.SPLIT.split(t0)
    if len(parts) > 1 and not t0.startswith("("):
        return " ".join(F.sentence_my(x) for x in parts[:-1]) + " " + fragment(parts[-1])
    if t0 in F.ANSWERS:
        return F.ANSWERS[t0]
    if t0 == "Āmantā":                # «Āmantā …pe….» = «ဟုတ်ပါသည် …။» (ch7a / ch9-10a; harmonise A4: no «။» added)
        return F.YES[: -len(END)]
    m = re.fullmatch(r"(?P<a>.+[.?]) (?P<n>\(.+\)\.?)", t0)
    if m and m["n"] in NOTE:
        return fragment(m["a"]) + " " + NOTE[m["n"]]
    m = re.fullmatch(r"(?P<a>.+?) (?P<n>\(.+\)\.?)", t0)
    if m and m["n"] in NOTE:
        return fragment(m["a"]) + " " + NOTE[m["n"]]
    m = re.fullmatch(r"(?P<cl>[Yy]assa vā pana yattha|[Yy]assa vā pana|[Yy]attha vā pana|[Yy]assa yattha|[Yy]assa|"
                     r"[Yy]attha)(?: (?P<x>\S+))?", t0)
    if m and (not m["x"] or m["x"] in F.SUBJ):
        c = m["cl"].lower()
        pre = F.VA_PANA + " " if " vā pana" in c else ""
        return f"{pre}{F.CL[c.replace(' vā pana', '')][0]}" + (f" {F.subj(m['x'])}" if m["x"] else "")
    m = FRAG_CL.match(t0)
    if m:
        c = m["cl"].lower()
        pre = F.VA_PANA + " " if " vā pana" in c else ""
        x = subj_c(m["q"]) if m["x"] == "cittaṃ" else F.subj(m["x"])
        out = f"{pre}{F.CL[c.replace(' vā pana', '')][0]} {x} {Pred(m['p']).cl()}"
        return out + (f"{C} {F.FT['tassa']}" if m["ft"] else "")
    m = re.fullmatch(r"(?P<who>.+?) (?P<pro>tesaṃ tattha|tesaṃ|tattha)", t0)
    if m:
        return F.who_my(m["who"], m["pro"])
    if t0.endswith(("?", ".")):
        return F.sentence_my(t0)
    raise F.Miss("pe fragment: " + t0)


def pe_line(s):
    s = s.replace("…pe…", PE).replace("…Pe…", PE)
    out = []
    for p in s.split(PE):
        q = fragment(p)
        lead = " " if p.startswith(" ") and q and q != END else ""
        trail = " " if p.endswith(" ") and p.strip() else ""
        out.append(lead + q + trail)
    return PE.join(out)


_body_my0 = F.body_my


def body_my(line):
    if line in F.COLO or line in F.LINES or F.BRACKET.sub("⟦v⟧", line) in F.LINES:
        return _body_my0(line)
    if "…" in line:
        return pe_line(line)
    return _body_my0(line)


F.body_my = body_my

# ===================================================================================== headings and colophons
UPPANNA_N = new("uppanna (heading noun)", f"{UPPANNA}သော {F.THING}")
UPPAJJAMANA_N = new("uppajjamāna (heading noun)", f"{PARTICIPLE['uppajjamānaṃ']} {F.THING}")
NIRUJJHAMANA_N = new("nirujjhamāna (heading noun)", f"{PARTICIPLE['nirujjhamānaṃ']} {F.THING}")
NIRUDDHA_N = new("niruddha (heading noun)", f"{NIRUDDHA}သော {F.THING}")
NA_NIRODHA = new("na-nirodha (heading)", "မ" + F.NIRODHA)
UP_NI = f"{F.UPPADA}{AND} {F.NIRODHA}"
SUTTANTA = W("5", "^5-74", "Attheva suttantoti", "သုတ္တန်", key="suttanta")
H_NEW = {
    "Suddhasaṅkhāravāro": F.vara(f"{F.SUDDHA} {SANKHARA}", False),
    "Nirodhavāro": F.vara(F.NIRODHA),
    "Uppādavāro": F.vara(F.UPPADA),
    "Uppādanirodhavāro": F.vara(UP_NI),
    "Pavatti 3. uppādanirodhavāro": f"{F.PAVATTI} 3. {F.vara(UP_NI)}",
    "Pariññāvāro": F.vara(PARINNA),
    "1-6. Paccuppannavārādi": f"1-6. {F.vara(F.TIMES['Paccuppanna'])} {F.ADI}",
    "paccanīkaokāsā": F.H["paccanīkaokāso"],              # plural spelling of the heading (^6-6-16-5-0)
    "Suddhacittasāmaññaṃ": new("Suddhacittasāmaññaṃ", f"{F.SUDDHA} {CITTA} {SAMANNA}"),
    "Puggalavāro": F.vara(F.PUGGALA),
    "Dhammavāro": F.vara(F.DHAMMA),
    "Puggaladhammavāro": F.vara(f"{F.PUGGALA}{AND} {F.DHAMMA}"),
    "Uppādanirodhakālasambhedavāro": new("Uppādanirodhakālasambhedavāro",
                                         F.vara(f"{UP_NI}၏ ကာလ ရောနှောခြင်း", False)),
    "Uppāduppannavāro": F.vara(f"{F.UPPADA}{AND} {UPPANNA_N}", False),
    "Nirodhuppannavāro": F.vara(f"{F.NIRODHA}{AND} {UPPANNA_N}", False),
    "Uppajjamāna-nanirodhavāro": F.vara(f"{UPPAJJAMANA_N}{AND} {NA_NIRODHA}", False),
    "Uppajjamānuppannavāro": F.vara(f"{UPPAJJAMANA_N}{AND} {UPPANNA_N}", False),
    "Nirujjhamānuppannavāro": F.vara(f"{NIRUJJHAMANA_N}{AND} {UPPANNA_N}", False),
    "Uppannuppādavāro": F.vara(f"{UPPANNA_N}{AND} {F.UPPADA}", False),
    "Uppannuppajjamānavāro": F.vara(f"{UPPANNA_N}{AND} {UPPAJJAMANA_N}", False),
    "Niruddhanirujjhamānavāro": F.vara(f"{NIRUDDHA_N}{AND} {NIRUJJHAMANA_N}", False),
    "Atikkantakālavāro": new("Atikkantakālavāro", F.vara(f"ကာလ {ATIKKANTA_W}ပြီးခြင်း", False)),
    "Suttantacittamissakaviseso": new("Suttantacittamissakaviseso", f"{SUTTANTA}လာ {CITTA}များကို ရောစပ်သော ထူးခြားချက်"),
    "Abhidhammacittamissakaviseso": new("Abhidhammacittamissakaviseso",
                                        f"{F.ABHI[:-len('ပိဋကတွင်')]}လာ {CITTA}များကို ရောစပ်သော ထူးခြားချက်"),
}
H_NEW["Suddhacittasāmañña"] = H_NEW["Suddhacittasāmaññaṃ"]
H_NEW["Uppajjamānananirodhavāro"] = H_NEW["Uppajjamāna-nanirodhavāro"]
F.H.update(H_NEW)
COLO_NEW = {
    "Paṇṇattivāro.": F.vara(F.PANNATTI) + END,
    "Uppādavāro.": F.vara(F.UPPADA) + END,
    "Nirodhavāro.": F.vara(F.NIRODHA) + END,
    "Uppādanirodhavāro.": F.vara(UP_NI) + END,
    "Pariññāvāro.": F.vara(PARINNA) + END,
}
F.COLO.update(COLO_NEW)

# ===================================================================================== unique lines and notes
# harmonise B15 / B16: the note vocabulary of ch3 / ch2-02-4-5 (the majority, also ch7b / ch10b): yassaka / yatthaka /
# yassayatthaka «“အကြင်သူအား” / “အကြင်နေရာ၌” / “အကြင်သူအား အကြင်နေရာ၌” အပိုင်း», sadisaṃ «တူညီသည်», vitthāretabbaṃ
# «အကျယ် ချဲ့ရမည်» (pi-5 ^5-839), vibhajitabbaṃ «ခွဲခြား ပြရမည်», vibhatta «ခွဲခြား ပြထားသကဲ့သို့», pucchā «အမေး»
# (pi-5 ^5-652), ekasadisaṃ «တစ်ထပ်တည်း တူညီ», «X-nti na kātabbaṃ» «“X”ဟု မပြုရ» (ch2-02-4-5)
YASSAKA = new("yassaka (the «yassa» questions)", f"“{F.CL['yassa'][0]}” အပိုင်း")
YATTHAKA = new("yatthaka (the «yattha» questions)", f"“{F.CL['yattha'][0]}” အပိုင်း")
YY = new("yassayatthaka (the «yassa yattha» questions)", f"“{F.CL['yassa yattha'][0]}” အပိုင်း")
SADISA = new("sadisaṃ", "တူညီသည်")
VITTHAR = new("vitthāretabbaṃ", "အကျယ် ချဲ့ရမည်")
VIBHAJ = new("vibhajitabbaṃ / vibhajitabbā", "ခွဲခြား ပြရမည်")
VIBHATTA = "ခွဲခြား ပြထားသကဲ့သို့"
PUCCHA = "အမေး"
NO_DIFF = new("natthi nānākaraṇaṃ", "ကွဲပြားချက် မရှိ")
NIRODHA_Q = f"“{NIRODHA_SAM}တို့{F.DAT}”"
BOTH_SAME = f"{YASSAKA}လည်း{C} {YY}လည်း {SADISA}"     # (yassakampi yassayatthakampi sadisaṃ), as ch2-02-4-5
NOTE.update({
    "(itaresaṃ yatthakānaṃ sadisaṃ).": f"(အခြား {YATTHAKA}တို့နှင့် {SADISA})။",      # itaresaṃ «အခြား» (ch3)
    "(itaresaṃ yatthakānaṃ sadisaṃ)": f"(အခြား {YATTHAKA}တို့နှင့် {SADISA})",
    "(yassakampi yassayatthakampi sadisaṃ).": f"({BOTH_SAME})။",
    "(yassakampi yassayatthakampi sadisaṃ)": f"({BOTH_SAME})",
    "(Yassakampi yassayatthakampi sadisaṃ.)": f"({BOTH_SAME}။)",
})
LINES_CH = {
    "Tayo saṅkhārā – kāyasaṅkhāro, vacīsaṅkhāro, cittasaṅkhāroti. Assāsapassāsā kāyasaṅkhāro, vitakkavicārā "
    "vacīsaṅkhāro, saññā ca vedanā ca cittasaṅkhāro. Ṭhapetvā vitakkavicāre sabbepi cittasampayuttakā dhammā "
    "cittasaṅkhāro.":
        f"{SANKHARA} သုံးပါး – {KAYA_S}{C} {VACI_S}{C} {CITTA_S}{END} {ASSASA}သည် {KAYA_S} {BE}သည်{C} "
        f"{VV}သည် {VACI_S} {BE}သည်{C} {SANNA_VEDANA}သည် {CITTA_S} {BE}သည်{END} {VV}ကို {F.THAPETVA}{C} "
        f"{CITTA_SAMP} {F.DHAMMA} အားလုံးသည် {CITTA_S} {BE}သည်{END}",
    "paccanīkaṃ": F.PACCANIKA,
    "(14) Atikkantakālavāro": f"(14) {H_NEW['Atikkantakālavāro']}",
    "4 (Ṅa) paccanīkaokāso": f"4 {F.label('Ṅa')} {F.H['paccanīkaokāso']}",
    "(Yassakampi yassayatthakampi sadisaṃ.)": NOTE["(Yassakampi yassayatthakampi sadisaṃ.)"],
    "(Yatthakampi sabbattha ekasadisaṃ).": f"({YATTHAKA}လည်း နေရာတိုင်း၌ တစ်ထပ်တည်း {SADISA})။",
    "(Yassakampi yassayatthakampi sadisaṃ vitthāretabbaṃ, yassayatthake nirodhasamāpannānanti na labbhati.)":
        f"({BOTH_SAME}၊ {VITTHAR}၊ {YY}၌ {NIRODHA_Q}ဟူသော စကားကို မရ။)",
    "(Yassakampi yassayatthakampi sadisaṃ, yassayatthake nirodhasamāpannānanti na labbhati).":
        f"({BOTH_SAME}၊ {YY}၌ {NIRODHA_Q}ဟူသော စကားကို မရ)။",
    "(Yassakampi yassayatthakampi sadisaṃ vitthāretabbaṃ, yassayatthake nirodhasamāpannānanti na kātabbaṃ.)":
        f"({BOTH_SAME}၊ {VITTHAR}၊ {YY}၌ {NIRODHA_Q}ဟု မပြုရ။)",
    "(Atītā pucchā uppādavārepi nirodhavārepi uppādanirodhavārepi sadisaṃ vitthāretabbā).":
        f"(အတိတ် {PUCCHA}တို့ကို {F.vara(F.UPPADA)}၌လည်း၊ {F.vara(F.NIRODHA)}၌လည်း၊ {F.vara(UP_NI)}၌လည်း "
        f"တူညီစွာ {VITTHAR})။",
    "(Yathā uppādavāre atītā pucchā yassakampi yassayatthakampi anulomampi paccanīkampi vibhattaṃ evaṃ "
    "nirodhavārepi vibhajitabbaṃ, natthi nānākaraṇaṃ.)":
        f"({F.vara(F.UPPADA)}၌ အတိတ် {PUCCHA}ကို {YASSAKA}ကိုလည်း၊ {YY}ကိုလည်း၊ {F.ANULOMA}ကိုလည်း၊ "
        f"{F.PACCANIKA}ကိုလည်း {VIBHATTA} {F.vara(F.NIRODHA)}၌လည်း {VIBHAJ}၊ {NO_DIFF}။)",
    "(Yathā uppādavāre paccuppannātītā pucchā anulomampi paccanīkampi vibhattā evaṃ uppādavāranirodhavārepi "
    "paccuppannātītā pucchā anulomampi paccanīkampi vibhajitabbā.)":
        f"({F.vara(F.UPPADA)}၌ {F.TIMES['Paccuppanna']}{AND} {F.TIMES['Atīta']} {PUCCHA}တို့ကို {F.ANULOMA}ကိုလည်း၊ "
        f"{F.PACCANIKA}ကိုလည်း {VIBHATTA} {F.vara(F.UPPADA)}{AND} {F.vara(F.NIRODHA)}၌လည်း "
        f"{F.TIMES['Paccuppanna']}{AND} {F.TIMES['Atīta']} {PUCCHA}တို့ကို {F.ANULOMA}ကိုလည်း၊ {F.PACCANIKA}ကိုလည်း "
        f"{VIBHAJ}။)",
    "(Yathā nirodhavāre atītānāgatā pucchā anulomampi paccanīkampi evaṃ uppādanirodhavārepi atītānāgatā pucchā "
    "anulomampi paccanīkampi vibhajitabbaṃ asammohantena nirodhavārena sadisaṃ, natthi nānākaraṇaṃ.)":
        f"({F.vara(F.NIRODHA)}၌ {F.TIMES['Atīta']}{AND} {F.TIMES['Anāgata']} {PUCCHA}တို့ကို {F.ANULOMA}ကိုလည်း၊ "
        f"{F.PACCANIKA}ကိုလည်း ဖော်ပြထားသကဲ့သို့ {F.vara(UP_NI)}၌လည်း {F.TIMES['Atīta']}{AND} "
        f"{F.TIMES['Anāgata']} {PUCCHA}တို့ကို {F.ANULOMA}ကိုလည်း၊ {F.PACCANIKA}ကိုလည်း မရောထွေးစေဘဲ "
        f"{VIBHAJ}၊ {F.vara(F.NIRODHA)}နှင့် {SADISA}၊ {NO_DIFF}။)",
    "(Yathā khandhayamake pariññāvāraṃ vibhattaṃ evaṃ saṅkhārayamakepi pariññāvāraṃ vibhajitabbaṃ.)":
        f"(“{F.H['Khandhayamakaṃ']}”၌ {F.vara(PARINNA)}ကို {VIBHATTA} "
        f"“{F.H['Saṅkhārayamakaṃ']}”၌လည်း {F.vara(PARINNA)}ကို {VIBHAJ}။)",
    "(Etena upāyena yāva saraṇaaraṇā uddharitabbā.)":
        f"(ဤနည်းဖြင့် “{SARANA}” “{QUAL['araṇaṃ'][:-len(' စိတ်')]}” အတွဲ တိုင်အောင် ထုတ်ဖော်ရမည်။)",
    "(Yassa cittake sakabhāvena niddiṭṭhe, yaṃ cittake ca yassa yaṃ cittake ca ekattena niddiṭṭhe.)":
        "(“အကြင်သူအား စိတ်” အပိုင်းကို ၎င်း၏ ကိုယ်ပိုင် ပုံစံဖြင့် ဖော်ပြပြီး၊ “အကြင်စိတ်” အပိုင်းနှင့် "
        "“အကြင်သူအား အကြင်စိတ်” အပိုင်းကိုလည်း တစ်ပေါင်းတည်း ဖော်ပြပြီးသောအခါ။)",
    "(Mūlayamakaṃ cittayamakaṃ dhammayamakanti tīṇi yamakāni yāva saraṇaaraṇā gacchanti.)":
        f"(“{F.H['Mūlayamakaṃ']}”၊ “{F.H['Cittayamakaṃ']}”၊ “{F.H['Dhammayamakaṃ']}” ဟူသော အတွဲလိုက် "
        f"မေးဖြေခြင်း သုံးခုသည် “{SARANA}” “{QUAL['araṇaṃ'][:-len(' စိတ်')]}” အတွဲ တိုင်အောင် ရောက်ကြသည်။)",
}
F.LINES.update(LINES_CH)
SENT.update({
    "Bhaṅgakkhaṇe cittaṃ uppādakkhaṇaṃ vītikkantaṃ bhaṅgakkhaṇaṃ avītikkantaṃ, atītaṃ cittaṃ uppādakkhaṇañca "
    "vītikkantaṃ bhaṅgakkhaṇañca vītikkantaṃ.":
        f"{DSUBJ['Bhaṅgakkhaṇe cittaṃ']}သည် {KHANA_ACC['uppādakkhaṇaṃ']} {VITIKKANTA_W}ပြီး {BE}၍ "
        f"{KHANA_ACC['bhaṅgakkhaṇaṃ']} မ{VITIKKANTA_W}{C} {DSUBJ['Atītaṃ cittaṃ']}သည် {KHANA_ACC['uppādakkhaṇaṃ']}လည်း "
        f"{VITIKKANTA_W}ပြီး {KHANA_ACC['bhaṅgakkhaṇaṃ']}လည်း {VITIKKANTA_W}ပြီး {BE}သည်{END}",
    "Bhaṅgakkhaṇe cittaṃ bhaṅgakkhaṇaṃ avītikkantaṃ no ca uppādakkhaṇaṃ avītikkantaṃ, uppādakkhaṇe anāgatañca "
    "cittaṃ bhaṅgakkhaṇañca avītikkantaṃ uppādakkhaṇañca avītikkantaṃ.":
        f"{DSUBJ['Bhaṅgakkhaṇe cittaṃ']}သည် {KHANA_ACC['bhaṅgakkhaṇaṃ']} မ{VITIKKANTA_W} {F.BUT} "   # A4: no «,»
        f"{KHANA_ACC['uppādakkhaṇaṃ']} မ{VITIKKANTA_W}သည်{F.NOT_SO}{C} {DSUBJ['Uppādakkhaṇe anāgatañca cittaṃ']}သည် "
        f"{KHANA_ACC['bhaṅgakkhaṇaṃ']}လည်း မ{VITIKKANTA_W}{C} {KHANA_ACC['uppādakkhaṇaṃ']}လည်း မ{VITIKKANTA_W}{END}",
    "Atītaṃ cittaṃ.": DSUBJ["Atītaṃ cittaṃ"] + END,
    "Uppādakkhaṇe anāgataṃ cittaṃ.": DSUBJ["Uppādakkhaṇe anāgataṃ cittaṃ"] + END,
})
# the slip «vītakkantaṃ» (^6-8-83) = vītikkantaṃ: same Burmese
_k = next(k for k in SENT if k.startswith("Bhaṅgakkhaṇe cittaṃ uppādakkhaṇaṃ vītikkantaṃ"))
SENT[_k.replace("uppādakkhaṇaṃ vītikkantaṃ", "uppādakkhaṇaṃ vītakkantaṃ", 1)] = SENT[_k]


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
    if not hm and not F.strip_id(m).rstrip().endswith(("။", "…", "။)")) and F.strip_id(p).rstrip()[-1:] in ".?":
        e.append("no final «။»")
    return e


def run(name):
    """-> (Burmese text, number of bad lines); raises Miss on an unmatched sentence."""
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
