"""Burmese zero-shot of pi-4 chapter 5-catukkapuggalapannatti (the fours) «လေးမျိုးတွဲ ပုဂ္ဂိုလ် သတ်မှတ်ချက်».

usage: python3 -I -X utf8 make_ch5.py [--misses]
Model: make_sample.py (approved sample). Every line is generated from the Pāli by my4_formulas.translate_line()
through the frames and tables of my4_formulas.py and make_sample.py (imported read only: make_sample installs the
approved sample tables at import and writes nothing; its __main__ is never run) and the tables of THIS script, which
extends them IN MEMORY only (nothing in my4_formulas.py / make_sample.py / my4-zeroshot-terms.md is changed):
  * NAME5: the group members (clouds, mice, mangoes, pots, ponds, bulls, snakes, trees) as person-type names
    (NAME, one string per type: list of names, question, closing line), ALIAS5 (spellings with a comma);
  * GROUP5: per simile group the object noun, its four member descriptions P (object «Pသော NOUN», person «Pသူ»,
    simile «ထိုNOUNသည် Pသကဲ့သို့»);
  * PRED5: predicates of the «Kathañca puggalo X hoti?» / «Evaṃ puggalo X hoti.» frames that the mātikā (sample
    PRED_M) does not already give;
  * (brackets: my4_formulas.var_my(), the one renderer of the book; harmonise B7);
  * SENT5: the unique sentences, built from shared parts (lists of clauses) so that identical Pāli gets identical
    Burmese; long clauses that pi-1 / pi-2 already have are READ from the FINAL rails text (my4_formulas.FINAL) and
    witnessed (Pāli and Burmese both in the rails segment);
  * RULES5 (my4_formulas.EXTRA_RULES): the frames of the chapter (Kathañca / Evaṃ puggalo, simile, group lines,
    unquoted / slip closing lines, «Yassa puggalassa rāgo appahīno, ayaṃ vuccati …»).
A unit no rule or table matches stops the run (Miss); nothing is guessed. The chapter is written only when every
line passed; --misses lists every unmatched unit and writes nothing. Every SENT5 key must be used (coverage).
"""
import pathlib
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import make_sample as M  # noqa: E402  (installs the approved sample tables; writes nothing at import)

F = M.F
ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-4_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-4-burmese-plain-zeroshot_split_chapters"
NAME_OUT = "5-catukkapuggalapannatti.md"
C, END, PE, N, W = F.C, F.END, F.PE, F.NAME, F.W
PUG, PUG_PL, IDHA, COP, CLP, CL = F.PUGGALA, F.PUG_PL, F.IDHA, F.COP, F.CL_P, F.CL
NEW = {}         # new recurring strings of this chapter (Pāli = Burmese), for notes-ch5.md


def new(pali, my):
    if pali in NEW and NEW[pali] != my:
        raise SystemExit(f"new-term conflict {pali}: {NEW[pali]} / {my}")
    NEW[pali] = my
    return my


def wit(book, bid, pali, my):
    """A value read from / checked against a FINAL rails segment (my4_formulas.witness)."""
    return F.witness(book, bid, pali, my)


def final_sents(book, bid, line=0):
    """The FINAL Burmese line of a rails segment split into its sentences (at «။ »)."""
    m = F.strip_id(F.FINAL.seg(book, bid)[2][line]).strip()
    return [s for s in m.rstrip("။").split("။ ")]


# ===================================================================================== brackets
PATHA, LEKHANA = F.PATHA, F.LEKHANA
MN, AN, DN = F.REF["ma. ni."], F.REF["a. ni."], F.REF["dī. ni."]
# harmonise B7: every bracket of the book is rendered by my4_formulas.var_my() (one renderer: VAR_KIND, REF,
# BR_NOTE / BR_NOTE_END there); the readings, references and notes of this chapter (BR5) were moved there.

# ===================================================================================== person names (in memory)
# group members: (object Pāli in the list «Cattāro X – …», person Pāli (question / names line), Burmese P)
GROUP5 = {}


def group(gkey, head_pali, noun, sim_pali, members):
    GROUP5[gkey] = dict(head=head_pali, noun=noun, sim=sim_pali, members=members)
    for obj, per, p in members:
        F._n(4, per, p + "သူ")


RAIN, THUN = "မိုး ရွာ", "မိုး ချုန်း"
group("valāhakūpamā", "Cattāro valāhakā", "မိုးတိမ်", "so valāhako", [
    ("gajjitā no vassitā", "gajjitā no vassitā", "မိုး ချုန်း၍ မိုး မရွာ"),
    ("vassitā no gajjitā", "vassitā no gajjitā", "မိုး ရွာ၍ မိုး မချုန်း"),
    ("gajjitā ca vassitā ca", "gajjitā ca vassitā ca", "မိုးလည်း ချုန်း၍ မိုးလည်း ရွာ"),
    ("neva gajjitā no vassitā", "neva gajjitā no vassitā", f"မိုးလည်း မချုန်း{C} မိုးလည်း မရွာ")])
group("mūsikūpamā", "Catasso mūsikā", "ကြွက်", "sā mūsikā", [
    ("gādhaṃ kattā no vasitā", "gādhaṃ kattā no vasitā", "တွင်း တူး၍ တွင်း၌ မနေ"),
    ("vasitā no gādhaṃ kattā", "vasitā no gādhaṃ kattā", "တွင်း၌ နေ၍ တွင်း မတူး"),
    ("gādhaṃ kattā ca vasitā ca", "gādhaṃ kattā ca vasitā ca", "တွင်းလည်း တူး၍ တွင်း၌လည်း နေ"),
    ("neva gādhaṃ kattā no vasitā", "neva gādhaṃ kattā no vasitā", f"တွင်းလည်း မတူး{C} တွင်း၌လည်း မနေ")])
group("ambūpamā", "Cattāri ambāni", "သရက်သီး", "taṃ ambaṃ", [
    ("āmaṃ pakkavaṇṇi", "āmo pakkavaṇṇī", "စိမ်း၍ မှည့်သော အဆင်း ရှိ"),
    ("pakkaṃ āmavaṇṇi", "pakko āmavaṇṇī", "မှည့်၍ စိမ်းသော အဆင်း ရှိ"),
    ("āmaṃ āmavaṇṇi", "āmo āmavaṇṇī", "စိမ်း၍ စိမ်းသော အဆင်း ရှိ"),
    ("pakkaṃ pakkavaṇṇi", "pakko pakkavaṇṇī", "မှည့်၍ မှည့်သော အဆင်း ရှိ")])
group("kumbhūpamā", "Cattāro kumbhā", "အိုး", "so kumbho", [
    ("tuccho pihito", "tuccho pihito", "ဗလာ ဖြစ်၍ အဖုံး ပိတ်ထား"),
    ("pūro vivaṭo", "pūro vivaṭo", "ပြည့်၍ အဖုံး ဖွင့်ထား"),
    ("tuccho vivaṭo", "tuccho vivaṭo", "ဗလာ ဖြစ်၍ အဖုံး ဖွင့်ထား"),
    ("pūro pihito", "pūro pihito", "ပြည့်၍ အဖုံး ပိတ်ထား")])
group("udakarahadūpamā", "Cattāro udakarahadā", "ရေကန်", "so udakarahado", [
    ("uttāno gambhīrobhāso", "uttāno gambhīrobhāso", "တိမ်၍ နက်ဟန် ထင်ရ"),
    ("gambhīro uttānobhāso", "gambhīro uttānobhāso", "နက်၍ တိမ်ဟန် ထင်ရ"),
    ("uttāno uttānobhāso", "uttāno uttānobhāso", "တိမ်၍ တိမ်ဟန် ထင်ရ"),
    ("gambhīro gambhīrobhāso", "gambhīro gambhīrobhāso", "နက်၍ နက်ဟန် ထင်ရ")])
SAKA, PARA, FIERCE = "မိမိ အုပ်ရှိ နွားတို့ကို", "သူတစ်ပါး အုပ်ရှိ နွားတို့ကို", "ကြမ်းကြုတ်"
group("balībaddūpamā", "Cattāro balībaddā [balibaddhā (syā.)]", "နွားလား", "so balībaddo", [
    ("sakagavacaṇḍo no paragavacaṇḍo", "sakagavacaṇḍo no paragavacaṇḍo", f"{SAKA} {FIERCE}၍ {PARA} မ{FIERCE}"),
    ("paragavacaṇḍo no sakagavacaṇḍo", "paragavacaṇḍo no sakagavacaṇḍo", f"{PARA} {FIERCE}၍ {SAKA} မ{FIERCE}"),
    ("sakagavacaṇḍo ca paragavacaṇḍo ca", "sakagavacaṇḍo ca paragavacaṇḍo ca",
     f"{SAKA}လည်း {FIERCE}၍ {PARA}လည်း {FIERCE}"),
    ("neva sakagavacaṇḍo no paragavacaṇḍo", "neva sakagavacaṇḍo no paragavacaṇḍo",
     f"{SAKA}လည်း မ{FIERCE}{C} {PARA}လည်း မ{FIERCE}")])
group("āsīvisūpamā", "Cattāro āsīvisā [āsivisā (syā.)]", "မြွေဆိုး", "so āsīviso", [
    ("āgataviso no ghoraviso", "āgataviso no ghoraviso", "အဆိပ် လျင်မြန်စွာ တက်၍ အဆိပ် မပြင်း"),
    ("ghoraviso no āgataviso", "ghoraviso no āgataviso", "အဆိပ် ပြင်း၍ အဆိပ် လျင်မြန်စွာ မတက်"),
    ("āgataviso ca ghoraviso ca", "āgataviso ca ghoraviso ca", "အဆိပ်လည်း လျင်မြန်စွာ တက်၍ အဆိပ်လည်း ပြင်း"),
    ("neva āgataviso no ghoraviso", "neva āgataviso no ghoraviso",
     f"အဆိပ်လည်း လျင်မြန်စွာ မတက်{C} အဆိပ်လည်း မပြင်း")])
group("rukkhūpamā", "Cattāro rukkhā", "သစ်ပင်", "so rukkho", [
    ("pheggu sāraparivāro", "pheggu sāraparivāro", "အကာ ဖြစ်၍ အနှစ် အခြံအရံ ရှိ"),
    ("sāro phegguparivāro", "sāro phegguparivāro", "အနှစ် ဖြစ်၍ အကာ အခြံအရံ ရှိ"),
    ("pheggu phegguparivāro", "pheggu phegguparivāro", "အကာ ဖြစ်၍ အကာ အခြံအရံ ရှိ"),
    ("sāro sāraparivāro", "sāro sāraparivāro", "အနှစ် ဖြစ်၍ အနှစ် အခြံအရံ ရှိ")])
for _g, _d in GROUP5.items():
    new(_d["head"].split(" [")[0].split(" ", 1)[1], _d["noun"])
    for _o, _p, _m in _d["members"]:
        new(_p, _m + "သူ")
ALIAS5 = {"uṭṭhānaphalūpajīvī, no puññaphalūpajīvī": "uṭṭhānaphalūpajīvī no puññaphalūpajīvī"}
for _a, _k in ALIAS5.items():
    assert _k in N
    F.ALIAS[_a] = _k

# ===================================================================================== predicates (PRED5)
PRED5 = {}
_P = F.PRED
_nn = _P["neva attantapo hoti na attaparitāpanānuyogamanuyutto, na parantapo na paraparitāpanānuyogamanuyutto. "
         "So anattantapo aparantapo diṭṭheva dhamme nicchāto nibbuto sītībhūto [sītibhūto (sī. ka.)] "
         "sukhappaṭisaṃvedī brahmabhūtena attanā viharati"]
NEITHER_TAPA, ANATTANTAPA = _nn.split(END + " ", 1)          # the mātikā (25) predicate and its second sentence
ANATTANTAPA = ANATTANTAPA.replace(" ⟦0⟧", "")               # ch5 ^4-177 / ^4-185: the same sentence, no bracket
PRED5["neva attantapo ca hoti na attaparitāpanānuyogamanuyutto, na parantapo na paraparitāpanānuyogamanuyutto"] = (
    NEITHER_TAPA)                                            # «neva attantapo ca hoti»: the «ca» adds nothing
_BT = "bhūtaṃ tacchaṃ kālena"
PRED5[f"neva avaṇṇārahassa avaṇṇaṃ bhāsitā hoti {_BT}, nopi vaṇṇārahassa vaṇṇaṃ bhāsitā hoti {_BT}"] = (
    _P[f"neva avaṇṇārahassa avaṇṇaṃ bhāsitā hoti {_BT}, no ca vaṇṇārahassa vaṇṇaṃ bhāsitā hoti {_BT}"])


def pred5(p):
    """«X hoti …» of the Kathañca / Evaṃ frames -> Burmese predicate (no end mark)."""
    for k in (p, p.replace(", ", "; "), p.replace(" no ", ", no ")):
        if k in PRED5:
            return PRED5[k]
        if k in _P:
            return _P[k]
    k = re.sub(r"(?<=\S) (?:ca )?hoti(?=[ ,]|$)", lambda m: " ca" if m[0].startswith(" ca ") else "", p, count=1)
    k = k.replace(",", "")
    if F.key_of(k):
        return f"{N[F.key_of(k)]} {COP}"
    raise F.Miss("predicate5: " + p)


def qform(s):
    """Predicate -> question form: final «ဖြစ်၏» -> «ဖြစ်သနည်း», final «မဟုတ်» -> «မဟုတ်သနည်း»."""
    if s.endswith(COP):
        return s[:-len(COP)] + "ဖြစ်သနည်း"
    if s.endswith("မဟုတ်"):
        return s + "သနည်း"
    raise F.Miss("question form: " + s)


KATHAM = f"{PUG}သည် အဘယ်သို့ "                     # Kathañca puggalo … ? = «ပုဂ္ဂိုလ်သည် အဘယ်သို့ … နည်း။» (pi-2)
EVAM = f"ဤသို့ {PUG}သည် "                           # Evaṃ puggalo … . = «ဤသို့ ပုဂ္ဂိုလ်သည် …။»
wit("2", "^2-523", "Kathañca bhikkhu abhikkante", "ရဟန်းသည် အဘယ်သို့ ရှေ့သို့ တိုးရာ")
new("Kathañca puggalo X hoti?", f"{KATHAM}X ဖြစ်သနည်း{END}")
new("Evaṃ puggalo X hoti.", f"{EVAM}X ဖြစ်၏{END}")

# ===================================================================================== frames (RULES5)
SANTO = f"{F.LOKE} {F.SANTO_PL}"                    # santo saṃvijjamānā lokasmiṃ (harmonise B2: book-wide form)
new("santo saṃvijjamānā lokasmiṃ", SANTO)
new("Seyyathāpi so X …, tathūpamo ayaṃ puggalo.", F.tathupamo_my("X", "…"))
SIM_OBJ = {}     # simile «Seyyathāpi so valāhako gajjitā no vassitā» object Pāli -> (noun, P)
for _g, _d in GROUP5.items():
    for _o, _p, _m in _d["members"]:
        SIM_OBJ[f"{_d['sim']} {_o}"] = (_d["noun"], _m)


def r_katham(m):
    return f"{KATHAM}{qform(pred5(m['p']))}{END}"


def r_evam(m):
    return f"{EVAM}{pred5(m['p'])}{END}"


def r_katham_pe(m):           # ^4-169 «Kathañca puggalo X hoti…pe… evaṃ puggalo X hoti.»
    if m["a"] != m["b"]:
        raise F.Miss("kathañca …pe…: " + m[0])
    p = pred5(m["a"] + " hoti")
    return f"{KATHAM}{qform(p)}{PE} {EVAM}{p}{END}"


def r_simile(m):
    if m["o"] not in SIM_OBJ:
        raise F.Miss("simile: " + m[0])
    noun, p = SIM_OBJ[m["o"]]
    return F.tathupamo_my(noun, p)                  # harmonise B2: the Pāli comma = «၊» (book-wide frame)


def r_tattha(m):
    return F.tattha_katame_my(4, F.GROUP[m["g"]])  # harmonise B1: «… ဟူသည် အဘယ် ပုဂ္ဂိုလ်တို့နည်း။»


def r_evamevam(m):
    return F.ime_santo_my(F.GROUP[m["g"]], 4, F.LOKE, evam=True)


def r_ime(m):
    return F.ime_santo_my(F.GROUP[m["g"]], 4, F.LOKE)


def r_vuccati_plain(m):       # «Ayaṃ vuccati puggalo X.» without quotes (^4-171, ^4-172, ^4-188)
    return F.VUCCATI_BARE.format(F.name(m["n"]))


def r_vuccati_slip(m):        # «ayaṃ vuccati, puggalo "X".» (^4-155, stray comma) / «… "X"ti.» (^4-190)
    return F.VUCCATI.format(F.name(m["n"]))


UNWHOLE = {"rāgo": "ရာဂ", "doso": "ဒေါသ", "moho": "မောဟ", "māno": "မာန"}


def r_appahino(m):            # ^4-186 «Yassa puggalassa rāgo appahīno, ayaṃ vuccati puggalo "sarāgo".»
    return (f"အကြင် {PUG}၏ {UNWHOLE[m['k']]}ကို မပယ်ရသေး{C} " + F.VUCCATI.format(F.name(m["n"])))


TRUTH = dict(zip(["idaṃ dukkha", "ayaṃ dukkhasamudayo", "ayaṃ dukkhanirodho", "ayaṃ dukkhanirodhagāminī paṭipadā"],
                 [f"ဤသည်ကား {t}" for t in W["dukkha"].split(f"{C} ")]))
TRUTH.update(zip(["ime āsavā", "ayaṃ āsavasamudayo", "ayaṃ āsavanirodho", "ayaṃ āsavanirodhagāminī paṭipadā"],
                 F.ASAVA4))                    # the book-wide forms (my4_formulas, harmonise B2)
for _k in ("ime āsavā", "ayaṃ āsavasamudayo", "ayaṃ āsavanirodho", "ayaṃ āsavanirodhagāminī paṭipadā"):
    new(_k, TRUTH[_k])
KNOW, NOKNOW = F._KNOW, F._KNOW[:-1].replace(" ကွဲပြားစွာ သိ", " ကွဲပြားစွာ မသိ")   # pajānāti / nappajānāti
TR_ITEM = re.compile(r'"(?P<q>[^"]+)"n?ti yathābhūtaṃ (?P<v>pajānāti|nappajānāti)')


def r_truths(m):              # «So "idaṃ dukkha"nti yathābhūtaṃ (n)appajānāti, … .» (also with …pe…)
    body = m["b"]
    out, pos = [], 0
    for it in TR_ITEM.finditer(body):
        sep = body[pos:it.start()]
        if out:
            out.append({", ": f"{C} ", "…pe… ": f"{PE} ", " …pe… ": f"{PE} "}[sep])   # A5: no space before «…»
        elif sep:
            raise F.Miss("truths: " + body)
        out.append(f"“{TRUTH[it['q']]}”ဟု {KNOW if it['v'] == 'pajānāti' else NOKNOW}")
        pos = it.end()
    if pos != len(body):
        raise F.Miss("truths tail: " + body)
    return f"{F.SO} " + "".join(out) + END


RULES5 = [
    (re.compile(r"Kathañca puggalo (?P<a>.+?) hoti…pe… evaṃ puggalo (?P<b>.+?) hoti\."), r_katham_pe),
    (re.compile(r"Kathañca puggalo (?P<p>[^?]+)\?"), r_katham),
    (re.compile(r"Evaṃ puggalo (?P<p>.+)\."), r_evam),
    (re.compile(r"Seyyathāpi (?P<o>.+), tathūpamo ayaṃ puggalo\."), r_simile),
    (re.compile(r"Tattha katame cattāro (?P<g>\S+) puggalā\?"), r_tattha),
    (re.compile(r"Evamevaṃ cattārome (?P<g>\S+) puggalā santo saṃvijjamānā lokasmiṃ\."), r_evamevam),
    (re.compile(r"Ime cattāro (?P<g>\S+) puggalā santo saṃvijjamānā lokasmiṃ\."), r_ime),
    (re.compile(r"Ayaṃ vuccati puggalo (?P<n>[^\"]+)\."), r_vuccati_plain),
    (re.compile(r'ayaṃ vuccati, puggalo "(?P<n>[^"]+)"\.|Ayaṃ vuccati puggalo "(?P<n2>[^"]+)"ti\.'),
     lambda m: r_vuccati_slip({"n": m["n"] or m["n2"]})),
    (re.compile(r'Yassa puggalassa (?P<k>rāgo|doso|moho|māno) appahīno, ayaṃ vuccati puggalo "(?P<n>[^"]+)"\.'),
     r_appahino),
    (re.compile(r"So (?P<b>\"idaṃ dukkha\"nti yathābhūtaṃ .+)\."), r_truths),
]
F.EXTRA_RULES.extend(RULES5)

# ===================================================================================== SENT5: unique sentences
SENT5 = {}


def S(pali, my):
    if pali in SENT5 and SENT5[pali] != my:
        raise SystemExit("SENT5 conflict: " + pali[:80])
    SENT5[pali] = my


SEPM = {", ": f"{C} ", "…pe… ": f"{PE} ", "; ": f"{C} "}


def J(parts, seps):
    """parts = [(pāli, burmese)], seps = separators between them («, » / «…pe… »)."""
    p, m = parts[0]
    for (a, b), s in zip(parts[1:], seps):
        p, m = p + s + a, m + SEPM[s] + b
    return p, m


# ---- ^4-132 … ^4-143: the ten courses of action (pi-2: pāṇātipāta … ; pi-1 anabhijjhā, abyāpāda)
wit("2", "^2-703", "pāṇātipātā veramaṇī", "သူ့အသက်ကို သတ်ခြင်းမှ ကင်းဝေးခြင်း")
wit("2", "^2-703", "adinnādānā veramaṇī", "မပေးသည်ကို ယူခြင်းမှ ကင်းဝေးခြင်း")
wit("2", "^2-703", "kāmesumicchācārā veramaṇī", "ကာမတို့၌ မှားယွင်းစွာ ကျင့်ခြင်းမှ ကင်းဝေးခြင်း")
wit("2", "^2-703", "musāvādā veramaṇī", "မုသား ပြောခြင်းမှ ကင်းဝေးခြင်း")
wit("2", "^2-703", "surāmerayamajjapamādaṭṭhānā veramaṇī", "သေရည် အရက် မူးယစ်ဖွယ်ဟူသော မေ့လျော့ခြင်း၏ အကြောင်းမှ ကင်းဝေးခြင်း")
wit("2", "^2-487", "pisuṇāya vācāya veramaṇī", "ကုန်းတိုက်သော စကားမှ ကင်းဝေးခြင်း")
wit("2", "^2-487", "pharusāya vācāya veramaṇī", "ကြမ်းတမ်းသော စကားမှ ကင်းဝေးခြင်း")
wit("2", "^2-487", "samphappalāpā veramaṇī", "အကျိုးမဲ့ ပြိန်ဖျင်းသော စကားမှ ကင်းဝေးခြင်း")
wit("1", "^1-1140", "abhijjhā kāyagantho", "သူ့ဥစ္စာကို လိုချင်ခြင်း")
wit("1", "^1-32", "anabhijjhā", "သူ့ဥစ္စာကို မလိုချင်ခြင်း")
wit("1", "^1-33", "abyāpādo", "ဖျက်ဆီးလိုစိတ် မရှိခြင်း")
wit("2", "^2-543", "Abyāpannacitto", "ဖျက်ဆီးလိုစိတ် မရှိသော စိတ် ရှိသူ")
wit("2", "^2-830", "micchādiṭṭhikā", "မှားယွင်းသော အယူ")
wit("2", "^2-830", "sammādiṭṭhikā", "မှန်ကန်သော အယူ")
_SURA = "သေရည် အရက် မူးယစ်ဖွယ်ဟူသော မေ့လျော့ခြင်း၏ အကြောင်း"
# key: (agent Pāli, agent Burmese, act Pāli (locative of samādapeti), act Burmese «…၌»)
ACT = {
    "pana": ("pāṇātipātī", "သူ့အသက်ကို သတ်သူ", "pāṇātipāte", "သူ့အသက်ကို သတ်ခြင်း၌"),
    "adin": ("adinnādāyī", "မပေးသည်ကို ယူသူ", "adinnādāne", "မပေးသည်ကို ယူခြင်း၌"),
    "kame": ("kāmesumicchācārī", "ကာမတို့၌ မှားယွင်းစွာ ကျင့်သူ", "kāmesumicchācāre", "ကာမတို့၌ မှားယွင်းစွာ ကျင့်ခြင်း၌"),
    "musa": ("musāvādī", "မုသား ပြောသူ", "musāvāde", "မုသား ပြောခြင်း၌"),
    "sura": ("surāmerayamajjapamādaṭṭhāyī", f"{_SURA}ကို မှီဝဲသူ", "surāmerayamajjapamādaṭṭhāne", f"{_SURA}၌"),
    "pisu": ("pisuṇavāco", "ကုန်းတိုက်သော စကားကို ပြောသူ", "pisuṇāya vācāya", "ကုန်းတိုက်သော စကား၌"),
    "phar": ("pharusavāco", "ကြမ်းတမ်းသော စကားကို ပြောသူ", "pharusāya vācāya", "ကြမ်းတမ်းသော စကား၌"),
    "samp": ("samphappalāpī", "အကျိုးမဲ့ ပြိန်ဖျင်းသော စကားကို ပြောသူ", "samphappalāpe", "အကျိုးမဲ့ ပြိန်ဖျင်းသော စကား၌"),
    "abhi": ("abhijjhālu", "သူ့ဥစ္စာကို လိုချင်သူ", "abhijjhāya", "သူ့ဥစ္စာကို လိုချင်ခြင်း၌"),
    "byap": ("byāpannacitto", "ဖျက်ဆီးလိုစိတ် ရှိသော စိတ် ရှိသူ", "byāpāde", "ဖျက်ဆီးလိုစိတ်၌"),
    "micc": ("micchādiṭṭhi", "မှားယွင်းသော အယူ ရှိသူ", "micchādiṭṭhiyā", "မှားယွင်းသော အယူ၌"),
    "anab": ("anabhijjhālu", "သူ့ဥစ္စာကို မလိုချင်သူ", "anabhijjhāya", "သူ့ဥစ္စာကို မလိုချင်ခြင်း၌"),
    "abya": ("abyāpannacitto", "ဖျက်ဆီးလိုစိတ် မရှိသော စိတ် ရှိသူ", "abyāpāde", "ဖျက်ဆီးလိုစိတ် မရှိခြင်း၌"),
    "samm": ("sammādiṭṭhi", "မှန်ကန်သော အယူ ရှိသူ", "sammādiṭṭhiyā", "မှန်ကန်သော အယူ၌"),
}
# key: (ablative Pāli of «… paṭivirato hoti» / «… veramaṇiyā samādapeti», Burmese «…မှ»)
ABL = {
    "pana": ("pāṇātipātā", "သူ့အသက်ကို သတ်ခြင်းမှ"), "adin": ("adinnādānā", "မပေးသည်ကို ယူခြင်းမှ"),
    "kame": ("kāmesumicchācārā", "ကာမတို့၌ မှားယွင်းစွာ ကျင့်ခြင်းမှ"), "musa": ("musāvādā", "မုသား ပြောခြင်းမှ"),
    "sura": ("surāmerayamajjapamādaṭṭhānā", f"{_SURA}မှ"), "pisu": ("pisuṇāya vācāya", "ကုန်းတိုက်သော စကားမှ"),
    "phar": ("pharusāya vācāya", "ကြမ်းတမ်းသော စကားမှ"), "samp": ("samphappalāpā", "အကျိုးမဲ့ ပြိန်ဖျင်းသော စကားမှ"),
}
ABST = "ရှောင်ကြဉ်သူ"                             # paṭivirato
SAMADAP = "ဆောက်တည်စေ၏"                           # samādapeti
OWN_ALSO, OTH_ALSO = "မိမိကိုယ်တိုင်လည်း", "သူတစ်ပါးကိုလည်း"   # attanā ca / parañca
for _p, _m in (("paṭivirato", ABST), ("samādapeti", SAMADAP), ("attanā ca", OWN_ALSO), ("parañca", OTH_ALSO)):
    new(_p, _m)


def ag(k, br=""):            # «pāṇātipātī hoti» (agent)
    a, am = ACT[k][0], ACT[k][1]
    return (f"{a} {br} hoti" if br else f"{a} hoti"), (f"{am} ⟦*⟧ {COP}" if br else f"{am} {COP}")


def ab(k):                   # «pāṇātipātā paṭivirato hoti»
    return f"{ABL[k][0]} paṭivirato hoti", f"{ABL[k][1]} {ABST} {COP}"


def ag2(k):                  # «attanā ca pāṇātipātī hoti parañca pāṇātipāte samādapeti»
    a, am, l, lm = ACT[k]
    return f"attanā ca {a} hoti parañca {l} samādapeti", f"{OWN_ALSO} {am} {COP}{C} {OTH_ALSO} {lm} {SAMADAP}"


def ab2(k):                  # «attanā ca pāṇātipātā paṭivirato hoti parañca pāṇātipātā veramaṇiyā samādapeti»
    a, am = ABL[k]
    return (f"attanā ca {a} paṭivirato hoti parañca {a} veramaṇiyā samādapeti",
            f"{OWN_ALSO} {am} {ABST} {COP}{C} {OTH_ALSO} {am} ကင်းဝေးခြင်း၌ {SAMADAP}")


def num_ph(p, m):            # renumber «⟦*⟧» placeholders in order
    i = 0
    while "⟦*⟧" in m:
        m = m.replace("⟦*⟧", f"⟦{i}⟧", 1)
        i += 1
    return p, m


def idha(parts, seps):
    p, m = J(parts, seps)
    return num_ph("Idhekacco puggalo " + p, f"{IDHA} " + m)


FIVE, TEN_BAD = ["pana", "adin", "kame", "musa", "sura"], ["pana", "adin", "kame", "musa", "pisu", "phar", "samp",
                                                              "abhi", "byap", "micc"]
GOOD7 = ["pana", "adin", "kame", "musa", "pisu", "phar", "samp"]
S(*idha([ag(k) for k in FIVE], [", "] * 4))                                       # ^4-132
S(*idha([ag2(k) for k in FIVE], [", "] * 4))                                      # ^4-133
S(*idha([ab(k) for k in FIVE], [", "] * 4))                                       # ^4-134
S(*idha([ab2(k) for k in FIVE], [", "] * 4))                                      # ^4-135
_BRS = {"pisu": "[pisuṇāvāco]", "phar": "[pharusāvāco (sī.) dī. ni. 3.115]", "micc": "[micchādiṭṭhī (ka.)]"}
S(*idha([ag(k, _BRS.get(k, "")) for k in TEN_BAD], [", "] * 9))                    # ^4-136
S(*idha([ag2(k) for k in TEN_BAD], [", "] * 9))                                   # ^4-137
_GOOD10 = [ab(k) for k in GOOD7] + [ag("anab"), ag("abya"), ag("samm", "[sammādiṭṭhī (ka.)]")]
S(*idha(_GOOD10, [", "] * 9))                                                    # ^4-138
S(*idha([ab2(k) for k in GOOD7] + [ag2("anab"), ag2("abya"), ag2("samm")], [", "] * 9))   # ^4-139
S(*idha([ag("pana"), ag("adin"), ag("micc")], [", ", "…pe… "]))                  # ^4-140
S(*idha([ag2("pana"), ag2("adin"), ag2("micc")], [", ", "…pe… "]))               # ^4-141
S(*idha([ab("pana"), ab("adin"), ("samādiṭṭhi hoti", ag("samm")[1])], [", ", "…pe… "]))   # ^4-142 (slip samā-)
S(*idha([ab2("pana"), ag2("samm")], ["…pe… "]))                                  # ^4-143

# ---- ^4-144 … ^4-147: blameworthy and blameless action
KAMMA = {"kāya": "ကိုယ်ဖြင့် ပြုသော ကံ", "vacī": "နှုတ်ဖြင့် ပြုသော ကံ", "mano": "မနောဖြင့် ပြုသော ကံ"}
wit("2", "^2-913", "kāyaduccaritaṃ", "ကိုယ်ဖြင့် ပြုသော ဒုစရိုက်")
wit("2", "^2-913", "vacīduccaritaṃ", "နှုတ်ဖြင့် ပြုသော ဒုစရိုက်")
for _k, _m in KAMMA.items():
    new(_k + "kamma", _m)
VAJ, ANAVAJ = "အပြစ် ရှိသော", "အပြစ် မရှိသော"          # sāvajja / anavajja (names sāvajjo «အပြစ် ရှိသူ», anavajjo)
SAMANN = "အပြည့်အဝ ပြည့်စုံသူ"                       # samannāgato (sample)
S(*idha([(f"sāvajjena {k}kammena samannāgato hoti", f"{VAJ} {v}နှင့် {SAMANN} {COP}") for k, v in KAMMA.items()],
        [", "] * 2))
S(*idha([(f"anavajjena {k}kammena samannāgato hoti", f"{ANAVAJ} {v}နှင့် {SAMANN} {COP}") for k, v in KAMMA.items()],
        [", "] * 2))
S(*idha([(f"sāvajjena bahulaṃ {k}kammena samannāgato hoti appaṃ anavajjena",
          f"{VAJ} {v}နှင့် များစွာ {SAMANN} {COP}{C} {ANAVAJ} ကံနှင့်ကား အနည်းငယ်သာ") for k, v in KAMMA.items()],
        [", "] * 2))
S(*idha([(f"anavajjena bahulaṃ {k}kammena samannāgato hoti appaṃ sāvajjena",
          f"{ANAVAJ} {v}နှင့် များစွာ {SAMANN} {COP}{C} {VAJ} ကံနှင့်ကား အနည်းငယ်သာ") for k, v in KAMMA.items()],
        [", "] * 2))

# ---- ^4-148 … ^4-151: the four who understand the teaching
YASSA = f"အကြင် {PUG}၏"                               # yassa puggalassa (sample ^4-9)
ABHISAMAYA = new("dhammābhisamayo", "တရားကို ထိုးဖောက် သိမြင်ခြင်း")
S("Yassa puggalassa saha udāhaṭavelāya dhammābhisamayo hoti",
  f"{YASSA} တရားကို ပြောကြားလိုက်သည့် ခဏနှင့် တပြိုင်နက် {ABHISAMAYA} ဖြစ်၏")
S("Yassa puggalassa saṃkhittena bhāsitassa vitthārena atthe vibhajiyamāne dhammābhisamayo hoti",
  f"{YASSA} အကျဉ်းအားဖြင့် ဟောထားသည်၏ အနက်ကို အကျယ်အားဖြင့် ခွဲခြား ပြသသောအခါ {ABHISAMAYA} ဖြစ်၏")
S("Yassa puggalassa uddesato paripucchato yoniso manasikaroto kalyāṇamitte sevato bhajato payirupāsato evaṃ "
  "anupubbena dhammābhisamayo hoti",
  f"{YASSA} သင်ယူခြင်း၊ မေးမြန်းခြင်း၊ သင့်လျော်စွာ နှလုံးသွင်းခြင်း၊ မိတ်ဆွေကောင်းတို့ကို {F.SEV[:-3]}ခြင်း၊ "
  f"{F.BHAJ[:-3]}ခြင်း၊ {F.PAYIR[:-3]}ခြင်းဖြင့် ဤသို့ အစဉ်အတိုင်း {ABHISAMAYA} ဖြစ်၏")
S("Yassa puggalassa bahumpi suṇato bahumpi bhaṇato bahumpi dhārayato bahumpi vācayato na tāya jātiyā "
  "dhammābhisamayo hoti",
  f"{YASSA} များစွာ ကြားနာသော်လည်း၊ များစွာ ပြောဆိုသော်လည်း၊ များစွာ ဆောင်ထားသော်လည်း၊ များစွာ ပို့ချသော်လည်း "
  f"ထိုဘဝ၌ {ABHISAMAYA} မဖြစ်")
wit("2", "^2-17-4-57-0", "ayoniso manasikāro", "မသင့်လျော်စွာ နှလုံးသွင်းခြင်း")

# ---- ^4-152 … ^4-155: ready and quick answers
PANHA = "ပြဿနာကို မေးမြန်းခံရသောအခါ"                 # pañhaṃ puṭṭho samāno
S("Katamo ca puggalo yuttappaṭibhāno [yuttapaṭibhāṇo (syā.) a. ni. 4.132] no muttappaṭibhāno?",
  f"{N['yuttappaṭibhāno no muttappaṭibhāno']} ⟦0⟧{F.Q_TAIL}")
for _p, _m in (("yuttaṃ vadati no sīghaṃ", f"သင့်လျော်စွာ ဖြေဆို၏{C} လျင်မြန်စွာ မဖြေဆို"),
               ("sīghaṃ vadati no yuttaṃ", f"လျင်မြန်စွာ ဖြေဆို၏{C} သင့်လျော်စွာ မဖြေဆို"),
               ("yuttañca vadati sīghañca", f"သင့်လျော်စွာလည်း ဖြေဆို၏{C} လျင်မြန်စွာလည်း ဖြေဆို၏"),
               ("neva yuttaṃ vadati no sīghaṃ", f"သင့်လျော်စွာလည်း မဖြေဆို{C} လျင်မြန်စွာလည်း မဖြေဆို")):
    S(f"Idhekacco puggalo pañhaṃ puṭṭho samāno {_p}", f"{IDHA} {PANHA} {_m}")

# ---- ^4-156: the four speakers on the teaching
DK = new("dhammakathiko", "တရား ဟောပြောသူ")
SAHITA, ASAHITA = "အနက် ဆက်စပ်သည်", "အနက် မဆက်စပ်သည်"
_PRE = {"i": ("Idhekacco", "ဤလောက၌ အချို့သော"), "p": ("Idha panekacco", f"{F.IDHA_PANA} ဤလောက၌ အချို့သော")}   # B6
_AMT = {"a": ("appañca", "နည်းနည်းလည်း"), "b": ("bahuñca", "များများလည်း")}
_SA = {"n": ("asahitañca", ASAHITA, "na kusalā", "မကျွမ်းကျင်"), "y": ("sahitañca", SAHITA, "kusalā", "ကျွမ်းကျင်၏")}
for _a, _b, _c in ("ian", "pay", "pbn", "pby"):          # the four lines of ^4-156
    (_pre_p, _pre_m), (_amt_p, _amt_m), (_sa_p, _sa_m, _ku_p, _ku_m) = _PRE[_a], _AMT[_b], _SA[_c]
    if True:
        if True:
            S(f"{_pre_p} dhammakathiko {_amt_p} bhāsati {_sa_p}, parisā cassa {_ku_p} hoti sahitāsahitassa.",
              f"{_pre_m} {DK}သည် {_amt_m} ဟောပြော၏{C} {_sa_m}ကိုလည်း ဟောပြော၏{C} ထိုသူ၏ ပရိသတ်သည်လည်း "
              f"{SAHITA}{C} {ASAHITA}ကို ခွဲခြားရာ၌ {_ku_m}{END}")
S("Evarūpo dhammakathiko evarūpāya parisāya dhammakathikotveva saṅkhaṃ gacchati.",
  f"ဤကဲ့သို့သော {DK}သည် ဤကဲ့သို့သော ပရိသတ်၌ {DK}ဟူ၍သာ အမည် ရ၏{END}")
S('Ime cattāro "dhammakathikā puggalā".', f"ဤ{PUG_PL}သည် “{F.GROUP['dhammakathikā']} {PUG}” {F.persons(4)} ဖြစ်ကြ၏{END}")

# ---- ^4-157 … ^4-163, ^4-170: the simile groups (object list, names line)
for _g, _d in GROUP5.items():
    _h = _d["head"]
    _hb = " ⟦0⟧" if "[" in _h else ""
    S(_h, f"{_d['noun']}{_hb} လေးမျိုး")
    _objs = [o for o, p, m in _d["members"]]
    _pers = [p for o, p, m in _d["members"]]
    if _g not in ("ambūpamā", "balībaddūpamā"):
        S(", ".join(_objs) + ".", f"{C} ".join(f"{m}သော {_d['noun']}" for o, p, m in _d["members"]) + END)
    _names = ", ".join(_pers)
    S(_names[0].upper() + _names[1:] + ".", f"{C} ".join(f"{m}သူ" for o, p, m in _d["members"]) + END)
    S("Katame cattāro?", F.katame_n_my(4))
_A = GROUP5["ambūpamā"]["members"]
S("āmaṃ pakkavaṇṇi [pakkavaṇṇī], pakkaṃ āmavaṇṇi [āmavaṇṇī (syā. ka.) a. ni. 4.105], āmaṃ āmavaṇṇi, "
  "pakkaṃ pakkavaṇṇi.",
  f"{_A[0][2]}သော သရက်သီး ⟦0⟧{C} {_A[1][2]}သော သရက်သီး ⟦1⟧{C} {_A[2][2]}သော သရက်သီး{C} {_A[3][2]}သော သရက်သီး{END}")
_B = GROUP5["balībaddūpamā"]["members"]
S("sakagavacaṇḍo [sagavacaṇḍo (ka. sī.) a. ni. 4.108] no paragavacaṇḍo, paragavacaṇḍo no sakagavacaṇḍo, "
  "sakagavacaṇḍo ca paragavacaṇḍo ca, neva sakagavacaṇḍo no paragavacaṇḍo.",
  f"{SAKA} {FIERCE}၍ ⟦0⟧ {PARA} မ{FIERCE}သော နွားလား{C} " +
  f"{C} ".join(f"{m}သော နွားလား" for o, p, m in _B[1:]) + END)

# ---- the persons of the simile groups
SO = "ထိုသူသည်"                                        # So (sample)
IDHA_G = f"{W['idhekacco']} {PUG}၏"                    # idhekaccassa puggalassa
SPEAK, DO = "ပြောဆိုသူ", "ပြုလုပ်သူ"                    # bhāsitā / kattā
S("Idhekacco puggalo bhāsitā hoti, no kattā.", f"{IDHA} {SPEAK} {COP}{C} {DO} မဟုတ်{END}")
S("Idhekacco puggalo kattā hoti, no bhāsitā.", f"{IDHA} {DO} {COP}{C} {SPEAK} မဟုတ်{END}")
S("Idhekacco puggalo bhāsitā ca hoti, kattā ca.", f"{IDHA} {SPEAK}လည်း {COP}{C} {DO}လည်း {COP}{END}")
S("Idhekacco puggalo neva bhāsitā hoti no kattā.", f"{IDHA} {SPEAK}လည်း မဟုတ်{C} {DO}လည်း မဟုတ်{END}")
NAVANGA = wit("2", "^2-724", "suttaṃ geyyaṃ veyyākaraṇaṃ gāthaṃ udānaṃ itivuttakaṃ jātakaṃ abbhutadhammaṃ vedallaṃ",
              "သုတ်၊ ဂေယျ၊ ဝေယျာကရဏ၊ ဂါထာ၊ ဥဒါန်း၊ ဣတိဝုတ်၊ ဇာတ်၊ အဗ္ဘုတဓမ္မ၊ ဝေဒလ္လ")
_NAV_P = "suttaṃ geyyaṃ veyyākaraṇaṃ gāthaṃ udānaṃ itivuttakaṃ jātakaṃ abbhutadhammaṃ vedallaṃ"
S(_NAV_P + ".", NAVANGA + END)
S("Idhekacco puggalo dhammaṃ pariyāpuṇāti", f"{IDHA} တရားကို သင်ယူ၏")
S("Idhekacco puggalo dhammaṃ na pariyāpuṇāti", f"{IDHA} တရားကို မသင်ယူ")
_PAS_P = ("pāsādikaṃ hoti abhikkantaṃ paṭikkantaṃ ālokitaṃ vilokitaṃ samiñjitaṃ{b} pasāritaṃ "
          "saṅghāṭipattacīvaradhāraṇaṃ.")
_PAS_M = ("ရှေ့သို့ တိုးခြင်း၊ နောက်သို့ ဆုတ်ခြင်း၊ ရှေ့သို့ ကြည့်ခြင်း၊ ဘေးသို့ ကြည့်ခြင်း၊ ကွေးခြင်း{b}၊ ဆန့်ခြင်း၊ "
          "ဒုကုဋ်၊ သပိတ်၊ သင်္ကန်းကို ဆောင်ခြင်းသည်")
wit("2", "^2-523", "abhikkante paṭikkante", "ရှေ့သို့ တိုးရာ၊ နောက်သို့ ဆုတ်ရာ")
wit("2", "^2-523", "ālokite vilokite", "ရှေ့သို့ ကြည့်ရာ၊ ဘေးသို့ ကြည့်ရာ")
wit("2", "^2-523", "saṅghāṭipattacīvaradhāraṇe", "ဒုကုဋ်၊ သပိတ်၊ သင်္ကန်းကို ဆောင်ရာ")
PASADIKA = new("pāsādika", "ကြည်ညိုဖွယ်")
S("Idhekaccassa puggalassa " + _PAS_P.format(b=" [sammiñjitaṃ (sī. syā.)]"),
  f"{IDHA_G} {_PAS_M.format(b=' ⟦0⟧')} {PASADIKA} {COP}{END}")
S("Idhekaccassa puggalassa " + _PAS_P.format(b=""), f"{IDHA_G} {_PAS_M.format(b='')} {PASADIKA} {COP}{END}")
S("Idhekaccassa puggalassa na " + _PAS_P.format(b=""), f"{IDHA_G} {_PAS_M.format(b='')} {PASADIKA} မဟုတ်{END}")
OWN_P, OTH_P, SCARE = "မိမိ ပရိသတ်ကို", "သူတစ်ပါး ပရိသတ်ကို", "ထိတ်လန့်စေသူ"     # sakaparisaṃ / paraparisaṃ ubbejitā
S("Idhekacco puggalo sakaparisaṃ ubbejitā hoti, no paraparisaṃ.", f"{IDHA} {OWN_P} {SCARE} {COP}{C} {OTH_P} မဟုတ်{END}")
S("Idhekacco puggalo paraparisaṃ ubbejitā hoti, no sakaparisaṃ.", f"{IDHA} {OTH_P} {SCARE} {COP}{C} {OWN_P} မဟုတ်{END}")
S("Idhekacco puggalo sakaparisañca ubbejitā hoti, paraparisañca.",
  f"{IDHA} {OWN_P}လည်း {SCARE} {COP}{C} {OTH_P}လည်း {SCARE} {COP}{END}")
S("Idhekacco puggalo neva sakaparisaṃ ubbejitā hoti no paraparisaṃ.",
  f"{IDHA} {OWN_P}လည်း {SCARE} မဟုတ်{C} {OTH_P}လည်း မဟုတ်{END}")
KODHA = wit("2", "^2-833", "Kodho ca upanāho", "အမျက်ဒေါသ")
# abhiṇhaṃ kujjhati / So ca khvassa kodho …: the book-wide forms (my4_formulas, harmonise B2; = ch4 ^4-113 … ^4-115)
S("Idhekacco puggalo abhiṇhaṃ kujjhati.", f"{IDHA} {F.OFTEN_ANGRY}{END}")
S("Idhekacco puggalo naheva kho [neva kho (sī.) a. ni. 4.110] abhiṇhaṃ kujjhati.",
  f"{IDHA} {F.NOT_OFTEN_ANGRY} ⟦0⟧{END}")
S("Idhekacco puggalo naheva kho abhiṇhaṃ kujjhati.", f"{IDHA} {F.NOT_OFTEN_ANGRY}{END}")
_LONG = "ကြာမြင့်စွာ ရှည်လျားသော ကာလပတ်လုံး"            # ciraṃ dīgharattaṃ
S("So ca khvassa kodho na ciraṃ dīgharattaṃ anuseti.", F.KODHO_SHORT + END)
S("So ca khvassa kodho ciraṃ dīgharattaṃ anuseti.", F.KODHO_LONG + END)
assert F.KODHO_LONG == f"ထိုသူ၏ ထို{KODHA}သည်ကား {_LONG} ကိန်းအောင်း၏"
DUSS, SILAV = "သီလ ပျက်", "သီလ ရှိ"                      # dussīla (pi-1 ^1-1333) / sīlavā
wit("1", "^1-1333", "dussīlā", "သီလ ပျက်သော")
PAPAD, KALAD = "ယုတ်မာသော သဘော ရှိ", "ကောင်းမွန်သော သဘော ရှိ"   # pāpadhammo / kalyāṇadhammo (names)
assert N["pāpadhammo"] == PAPAD + "သူ" and N["kalyāṇadhammo"] == KALAD + "သူ"
S("Idhekacco puggalo dussīlo hoti pāpadhammo, parisā ca khvassa hoti sīlavatī kalyāṇadhammā.",
  f"{IDHA} {F.DUSS_HOTI}{C} ထိုသူ၏ ပရိသတ်ကား {SILAV}၍ {KALAD}၏{END}")
S("Idhekacco puggalo sīlavā hoti kalyāṇadhammo, parisā ca khvassa hoti dussīlā pāpadhammā.",
  f"{IDHA} {F.SIL_HOTI}{C} ထိုသူ၏ ပရိသတ်ကား {DUSS}၍ {PAPAD}၏{END}")
S("Idhekacco puggalo dussīlo hoti pāpadhammo, parisāpissa hoti dussīlā pāpadhammā.",
  f"{IDHA} {F.DUSS_HOTI}{C} ထိုသူ၏ ပရိသတ်သည်လည်း {DUSS}၍ {PAPAD}၏{END}")
S("Idhekacco puggalo sīlavā hoti kalyāṇadhammo, parisāpissa hoti sīlavatī kalyāṇadhammā.",
  f"{IDHA} {F.SIL_HOTI}{C} ထိုသူ၏ ပရိသတ်သည်လည်း {SILAV}၍ {KALAD}၏{END}")

# ---- ^4-164, ^4-165: praise and blame without / after investigation
WELL_P, BAD_P, WRONG_P, RIGHT_P = "ကောင်းစွာ ကျင့်သော", "ဆိုးစွာ ကျင့်သော", "မှားယွင်းစွာ ကျင့်သော", "မှန်ကန်စွာ ကျင့်သော"
TITTH = f"{BAD_P}{C} {WRONG_P} တိတ္ထိတို့နှင့် တိတ္ထိ တပည့်တို့ကို"
BUDDH = f"{WELL_P}{C} {RIGHT_P} ဘုရားရှင်တို့နှင့် ဘုရားရှင်၏ တပည့်တို့ကို"
PRAISE, BLAME = "ချီးမွမ်း ပြောဆို၏", "ကဲ့ရဲ့ ပြောဆို၏"     # vaṇṇaṃ / avaṇṇaṃ bhāsati (mātikā PR / BL)
Q_GOOD = f"“ကောင်းစွာ ကျင့်သူတို့”ဟူ၍လည်း{C} “မှန်ကန်စွာ ကျင့်သူတို့”ဟူ၍လည်း ပြောဆို၏{END}"
Q_BAD = f"“ဆိုးစွာ ကျင့်သူတို့”ဟူ၍လည်း{C} “မှားယွင်းစွာ ကျင့်သူတို့”ဟူ၍လည်း ပြောဆို၏{END}"
_TP = "duppaṭipannānaṃ micchāpaṭipannānaṃ titthiyānaṃ titthiyasāvakānaṃ"
_BP = "suppaṭipannānaṃ sammāpaṭipannānaṃ buddhānaṃ buddhasāvakānaṃ"
for _w, _wp, _v, _vm in ((_TP, TITTH, "vaṇṇaṃ", PRAISE), (_BP, BUDDH, "avaṇṇaṃ", BLAME),
                         (_TP, TITTH, "avaṇṇaṃ", BLAME), (_BP, BUDDH, "vaṇṇaṃ", PRAISE)):
    S(f"Idhekacco puggalo {_w} {_v} bhāsati", f"{IDHA} {_wp} {_vm}")
S('"suppaṭipannā" itipi, "sammāpaṭipannā" itipīti.', Q_GOOD)
S('"duppaṭipannā" itipi, "micchāpaṭipannā" itipīti.', Q_BAD)
PAT_BAD, PAT_GOOD = "ဆိုးသော ကျင့်စဉ်၊ မှားယွင်းသော ကျင့်စဉ်၌", "ကောင်းသော ကျင့်စဉ်၊ မှန်ကန်သော ကျင့်စဉ်၌"
TRUST, NOTRUST = "ကြည်ညိုမှုကို ဖြစ်စေ၏", "မကြည်ညိုမှုကို ဖြစ်စေ၏"   # pasādaṃ / appasādaṃ janeti
for _w, _wp in (("duppaṭipadāya micchāpaṭipadāya", PAT_BAD), ("suppaṭipadāya sammāpaṭipadāya", PAT_GOOD)):
    for _v, _vm in (("pasādaṃ", TRUST), ("appasādaṃ", NOTRUST)):
        S(f"Idhekacco puggalo {_w} {_v} janeti", f"{IDHA} {_wp} {_vm}")
S('"suppaṭipadā" itipi, "sammāpaṭipadā" itipīti.',
  f"“ကောင်းသော ကျင့်စဉ်”ဟူ၍လည်း{C} “မှန်ကန်သော ကျင့်စဉ်”ဟူ၍လည်း ပြောဆို၏{END}")
S('"duppaṭipadā" itipi, "micchāpaṭipadā" itipīti.',
  f"“ဆိုးသော ကျင့်စဉ်”ဟူ၍လည်း{C} “မှားယွင်းသော ကျင့်စဉ်”ဟူ၍လည်း ပြောဆို၏{END}")

# ---- ^4-166: at the right time
BTK = M.BTK
S("Idhekacco puggalo vaṇṇopi saṃvijjati avaṇṇopi saṃvijjati.",       # harmonise A4: the nominative as written
  f"{IDHA} ချီးမွမ်းဖွယ်လည်း ရှိ၏{C} ကဲ့ရဲ့ဖွယ်လည်း ရှိ၏{END}")
_BL_T, _PR_T = "ထိုသူ၌ ကဲ့ရဲ့ဖွယ် ရှိသမျှကို", "ထိုသူ၌ ချီးမွမ်းဖွယ် ရှိသမျှကို"
_SAY, _NOSAY = f"{BTK} ပြော၏", f"{BTK} မပြော"
_YO = {"avaṇṇo taṃ bhaṇati": f"{_BL_T} {_SAY}", "avaṇṇo taṃ na bhaṇati": f"{_BL_T} {_NOSAY}",
       "vaṇṇo taṃ bhaṇati": f"{_PR_T} {_SAY}", "vaṇṇo taṃ na bhaṇati": f"{_PR_T} {_NOSAY}",
       "vaṇṇo tampi bhaṇati": f"{_PR_T}လည်း {_SAY}", "vaṇṇo tampi na bhaṇati": f"{_PR_T}လည်း {_NOSAY}"}
for _a, _b in (("avaṇṇo taṃ bhaṇati", "vaṇṇo taṃ na bhaṇati"), ("vaṇṇo taṃ bhaṇati", "avaṇṇo taṃ na bhaṇati")):
    S(f"Yo tattha {_a} {_BT}, yo tattha {_b} {_BT}.", f"{_YO[_a]}{C} {_YO[_b]}{END}")
S(f"Yo tattha avaṇṇo taṃ bhaṇati {_BT}, yopi tattha vaṇṇo tampi bhaṇati {_BT}.",
  f"{_YO['avaṇṇo taṃ bhaṇati']}{C} {_YO['vaṇṇo tampi bhaṇati']}{END}")
S(f"Yo tattha avaṇṇo taṃ na bhaṇati {_BT}, yopi tattha vaṇṇo tampi na bhaṇati {_BT}.",
  f"{_YO['avaṇṇo taṃ na bhaṇati']}{C} {_YO['vaṇṇo tampi na bhaṇati']}{END}")
S("Tatra kālaññū hoti tassa pañhassa veyyākaraṇāya.",
  f"ထို၌ ထိုပြဿနာကို ဖြေဆိုရန် သင့်လျော်သော အချိန်ကို သိသူ {COP}{END}")
wit("2", "^2-508", "upekkhako ca viharati sato ca sampajāno", "ဥပေက္ခာ ရှိလျက်လည်း နေ၍၊ သတိ ရှိလျက် ကောင်းစွာ ဆင်ခြင်သိမြင်လျက်")
S("Upekkhako viharati sato sampajāno.", f"ဥပေက္ခာ ရှိလျက်{C} သတိ ရှိလျက်{C} ကောင်းစွာ ဆင်ခြင်သိမြင်လျက် နေ၏{END}")

# ---- ^4-167: living by effort and by merit
UTT, PUN, LIVE, NOLIVE = F.UTT, F.PUN, F.LIVE, F.NOLIVE
_EFF = "ထကြွ၍ ကြိုးပမ်း၍ အားထုတ်၍ နေသော"            # uṭṭhahato ghaṭato vāyamato
AJIVA = new("ājīvo", "အသက်မွေးမှု")
S("Yassa puggalassa uṭṭhahato ghaṭato vāyamato ājīvo abhinibbattati, no puññato",
  f"{_EFF} အကြင် {PUG}၏ {AJIVA}သည် ထိုအားထုတ်မှုကြောင့် ဖြစ်ပေါ်၏{C} ကောင်းမှုကြောင့် မဟုတ်")
S("Yassa puggalassa uṭṭhahato ghaṭato vāyamato ājīvo abhinibbattati puññato ca",
  f"{_EFF} အကြင် {PUG}၏ {AJIVA}သည် ထိုအားထုတ်မှုကြောင့်လည်း{C} ကောင်းမှုကြောင့်လည်း ဖြစ်ပေါ်၏")
wit("2", "^2-1021", "paranimmitavasavattīnaṃ devānaṃ", "ပရနိမ္မိတဝသဝတ္တီ နတ်")
S("Paranimmitavasavattī deve [paranimmitavasavattideve (sī. syā.)] upādāya tatūpari devā puññaphalūpajīvino na "
  "uṭṭhānaphalūpajīvino.",
  f"ပရနိမ္မိတဝသဝတ္တီ နတ်တို့ ⟦0⟧မှ စ၍ ထိုအထက်ရှိ နတ်တို့သည် {PUN} {LIVE}ကြ၏{C} {UTT} {NOLIVE}ကြ{END}")
NERAYIKA = wit("2", "^2-1009", "nerayikānaṃ", "ငရဲသား")
S("Nerayikā neva uṭṭhānaphalūpajīvino no puññaphalūpajīvino.",
  f"{NERAYIKA}တို့သည် {UTT}လည်း {NOLIVE}ကြ{C} {PUN}လည်း {NOLIVE}ကြ{END}")

# ---- ^4-168: darkness and light
REBORN = "ပြန်လည် မွေးဖွားသူ"                          # paccājāto
APAYA = wit("2", "^2-U58", "kāyassa bhedā paraṃ maraṇā apāyaṃ duggatiṃ vinipātaṃ nirayaṃ upapajjati",
            "ခန္ဓာကိုယ် ပြိုကွဲ၍ သေပြီးနောက် အပါယ်၊ ဆိုးသော လားရာ၊ ပျက်စီး ကျရောက်ရာ၊ ငရဲ၌ ပြန်လည် ဖြစ်ပေါ်ရ၏")
SAGGA = (wit("2", "^2-830", "kāyassa bhedā paraṃ maraṇā sugatiṃ saggaṃ lokaṃ",
             "ခန္ဓာကိုယ် ပြိုကွဲ၍ သေပြီးနောက် ကောင်းသော လားရာ၊ နတ်ပြည် လောက") + "၌ ပြန်လည် ဖြစ်ပေါ်၏")
_LOW_P = ("Idhekacco puggalo nīce kule paccājāto hoti", f"{IDHA} နိမ့်ကျသော အမျိုး၌ {REBORN} {COP}")
_LOW2 = ("caṇḍālakule vā nesādakule vā venakule{a} vā rathakārakule vā pukkusakule vā dalidde{b} appannapānabhojane "
         "kasiravuttike, yattha kasirena ghāsacchādo labbhati.")
_LOW2M = ("စဏ္ဍာလ အမျိုး၌ဖြစ်စေ၊ မုဆိုး အမျိုး၌ဖြစ်စေ၊ ဝါးရက်သမား အမျိုး{a}၌ဖြစ်စေ၊ ရထားလုပ်သမား အမျိုး၌ဖြစ်စေ၊ "
          "အမှိုက်သိမ်းသမား အမျိုး၌ဖြစ်စေ၊ ဆင်းရဲသော{b}၊ အစား အသောက် နည်းပါးသော၊ အသက်မွေးရ ခက်ခဲသော၊ "
          "အစာနှင့် အဝတ်ကို ခက်ခဲစွာ ရရသော အမျိုး၌ ဖြစ်၏")
S(_LOW2.format(a=" [veṇakule (sī. syā.)]", b=" [daḷidde (sī.) passa aṅguttaranikāye]"),
  _LOW2M.format(a=" ⟦0⟧", b=" ⟦1⟧") + END)
S(_LOW2.format(a="", b=""), _LOW2M.format(a="", b="") + END)
_HIGH_P = ("Idhekacco puggalo ucce kule paccājāto hoti", f"{IDHA} မြင့်မြတ်သော အမျိုး၌ {REBORN} {COP}")
S(*_LOW_P)
S(*_HIGH_P)
S("khattiyamahāsālakule vā brāhmaṇamahāsālakule vā gahapatimahāsālakule vā aḍḍhe mahaddhane mahābhoge "
  "pahūtajātarūparajate pahūtavittūpakaraṇe pahūtadhanadhaññe.",
  "ကြွယ်ဝသော မင်းမျိုး၌ဖြစ်စေ၊ ကြွယ်ဝသော ပုဏ္ဏားမျိုး၌ဖြစ်စေ၊ ကြွယ်ဝသော သူကြွယ်မျိုး၌ဖြစ်စေ၊ ချမ်းသာသော၊ "
  "ဥစ္စာ များသော၊ စည်းစိမ် များသော၊ ရွှေ ငွေ ပေါများသော၊ ဥစ္စာ အသုံးအဆောင် ပေါများသော၊ ဥစ္စာ စပါး ပေါများသော "
  f"အမျိုး၌ ဖြစ်၏{END}")
wit("2", "^2-1021", "khattiyamahāsālānaṃ", "ကြွယ်ဝသော မင်းမျိုး")
wit("2", "^2-1021", "brāhmaṇamahāsālānaṃ", "ကြွယ်ဝသော ပုဏ္ဏားမျိုး")
wit("2", "^2-1021", "gahapatimahāsālānaṃ", "ကြွယ်ဝသော သူကြွယ်မျိုး")
REQ = "အစာ၊ အဖျော်၊ အဝတ်၊ ယာဉ်၊ ပန်း နံ့သာ နံ့သာပျောင်း၊ အိပ်ရာ နေအိမ် ဆီမီးတို့ကို"   # annassa … padīpeyyassa
S("So ca hoti dubbaṇṇo duddasiko okoṭimako bahvābādho kāṇo vā kuṇī vā khañjo vā pakkhahato vā, na lābhī annassa "
  "pānassa vatthassa yānassa mālāgandhavilepanassa seyyāvasathapadīpeyyassa.",
  f"ထိုသူသည်လည်း အဆင်း ဆိုးသူ၊ ကြည့်ရ ဆိုးသူ၊ ပုကွသူ၊ ရောဂါ များသူ၊ မျက်စိ ကွယ်သူဖြစ်စေ၊ လက် ကောက်သူဖြစ်စေ၊ "
  f"ခြေ ဆွံ့သူဖြစ်စေ၊ လေဖြတ်သူဖြစ်စေ ဖြစ်၏{C} {REQ} ရရှိသူ မဟုတ်{END}")
S("So ca hoti abhirūpo dassanīyo pāsādiko paramāya vaṇṇapokkharatāya samannāgato, lābhī annassa pānassa vatthassa "
  "yānassa mālāgandhavilepanassa seyyāvasathapadīpeyyassa.",
  f"ထိုသူသည်လည်း ရုပ်ချောသူ၊ ရှုချင်ဖွယ် ဖြစ်သူ၊ {PASADIKA} ဖြစ်သူ၊ အလွန် လှပသော အဆင်းနှင့် {SAMANN} ဖြစ်၏{C} "
  f"{REQ} ရရှိသူ {COP}{END}")
wit("2", "^2-830", "suvaṇṇe dubbaṇṇe", "အဆင်း လှသော၊ အဆင်း ဆိုးသော")
wit("2", "^2-894", "kāyena duccaritaṃ caritvā, vācāya duccaritaṃ caritvā, manasā duccaritaṃ caritvā",
    "ကိုယ်ဖြင့် ဒုစရိုက်ကို ကျင့်၍၊ နှုတ်ဖြင့် ဒုစရိုက်ကို ကျင့်၍၊ မနောဖြင့် ဒုစရိုက်ကို ကျင့်၍")
for _c, _cm, _dest in (("duccaritaṃ", "ဒုစရိုက်", APAYA), ("sucaritaṃ", "သုစရိုက်", SAGGA)):
    S(f"So kāyena {_c} carati, vācāya {_c} carati, manasā {_c} carati.",
      f"{SO} ကိုယ်ဖြင့် {_cm}ကို ကျင့်၏{C} နှုတ်ဖြင့် {_cm}ကို ကျင့်၏{C} မနောဖြင့် {_cm}ကို ကျင့်၏{END}")
    _tail = ("apāyaṃ duggatiṃ vinipātaṃ nirayaṃ upapajjati" if _c == "duccaritaṃ" else "sugatiṃ saggaṃ lokaṃ upapajjati")
    S(f"So kāyena {_c} caritvā vācāya {_c} caritvā manasā {_c} caritvā kāyassa bhedā paraṃ maraṇā {_tail}.",
      f"{SO} ကိုယ်ဖြင့် {_cm}ကို ကျင့်၍၊ နှုတ်ဖြင့် {_cm}ကို ကျင့်၍၊ မနောဖြင့် {_cm}ကို ကျင့်၍ {_dest}{END}")
wit("2", "^2-830", "kāyasucaritena", "ကိုယ်ဖြင့် ပြုသော သုစရိုက်")

# ---- ^4-171, ^4-172: the measures of trust
MEASURE = "ထို၌ အတိုင်းအတာ ထား၍ ကြည်ညိုမှုကို ဖြစ်စေ၏"      # tattha pamāṇaṃ gahetvā pasādaṃ janeti
SEE = "မြင်၍"
S("Idhekacco puggalo ārohaṃ vā passitvā pariṇāhaṃ vā passitvā saṇṭhānaṃ vā passitvā pāripūriṃ vā passitvā tattha "
  "pamāṇaṃ gahetvā pasādaṃ janeti.",
  f"{IDHA} အရပ် အမြင့်ကိုဖြစ်စေ {SEE}၊ လုံးပတ်ကိုဖြစ်စေ {SEE}၊ ပုံသဏ္ဌာန်ကိုဖြစ်စေ {SEE}၊ ကိုယ်အင်္ဂါ ပြည့်စုံမှုကိုဖြစ်စေ "
  f"{SEE} {MEASURE}{END}")
S("Idhekacco puggalo paravaṇṇanāya parathomanāya parapasaṃsanāya paravaṇṇahārikāya [paravaṇṇahāriyā (sī.)] tattha "
  "pamāṇaṃ gahetvā pasādaṃ janeti.",
  f"{IDHA} သူတစ်ပါးတို့၏ ချီးမွမ်းစကား၊ ချီးကျူးစကား၊ ထောမနာစကား၊ ဂုဏ်သတင်း ဆောင်ယူချက် ⟦0⟧တို့ကို အကြောင်းပြု၍ "
  f"{MEASURE}{END}")
S("Idhekacco puggalo cīvaralūkhaṃ vā passitvā pattalūkhaṃ vā passitvā senāsanalūkhaṃ vā passitvā vividhaṃ vā "
  "dukkarakārikaṃ passitvā tattha pamāṇaṃ gahetvā pasādaṃ janeti.",
  f"{IDHA} သင်္ကန်း၏ ကြမ်းတမ်းခြင်းကိုဖြစ်စေ {SEE}၊ သပိတ်၏ ကြမ်းတမ်းခြင်းကိုဖြစ်စေ {SEE}၊ အိပ်ရာ နေရာ၏ "
  f"ကြမ်းတမ်းခြင်းကိုဖြစ်စေ {SEE}၊ အမျိုးမျိုးသော ပြုရခက်သော အကျင့်ကိုဖြစ်စေ {SEE} {MEASURE}{END}")
S("Idhekacco puggalo sīlaṃ vā passitvā samādhiṃ vā passitvā paññaṃ vā passitvā tattha pamāṇaṃ gahetvā pasādaṃ "
  "janeti.",
  f"{IDHA} သီလကိုဖြစ်စေ {SEE}၊ သမာဓိကိုဖြစ်စေ {SEE}၊ ပညာကိုဖြစ်စေ {SEE} {MEASURE}{END}")
wit("2", "^2-528", "vivittaṃ senāsanaṃ", "အိပ်ရာ နေရာ")

# ---- ^4-173: one's own good and others' good
SAMP = [("sīla", "သီလ"), ("samādhi", "သမာဓိ"), ("paññā", "ပညာ"), ("vimutti", "လွတ်မြောက်မှု"),
        ("vimuttiñāṇadassana", "လွတ်မြောက်မှုကို သိမြင်သော ဉာဏ်")]
wit("1", "^1-M2-141", "vimutti ca", "လွတ်မြောက်မှု")
wit("1", "^1-M2-136", "sīlasampadā ca", "သီလ ပြည့်စုံခြင်း")
new("vimuttiñāṇadassana", "လွတ်မြောက်မှုကို သိမြင်သော ဉာဏ်")
_OWN, _OTH = "မိမိကိုယ်တိုင်", "သူတစ်ပါးကို"
_FORMS = {   # (own Pāli, own Burmese, other Pāli, other Burmese) with «{s}» / «{m}» for the five
    "a": ("attanā {s}sampanno hoti", f"{_OWN} {{m}} ပြည့်စုံသူ {COP}",
          "no paraṃ {s}sampadāya samādapeti", f"{_OTH} {{m}} ပြည့်စုံခြင်း၌ မ{SAMADAP[:-1]}"),
    "b": ("attanā na {s}sampanno hoti", f"{_OWN} {{m}} ပြည့်စုံသူ မဟုတ်",
          "paraṃ {s}sampadāya samādapeti", f"{_OTH} {{m}} ပြည့်စုံခြင်း၌ {SAMADAP}"),
    "c": ("attanā ca {s}sampanno hoti", f"{OWN_ALSO} {{m}} ပြည့်စုံသူ {COP}",
          "parañca {s}sampadāya samādapeti", f"{OTH_ALSO} {{m}} ပြည့်စုံခြင်း၌ {SAMADAP}"),
    "d": ("attanā na {s}sampanno hoti", f"{_OWN} {{m}} ပြည့်စုံသူ မဟုတ်",
          "no paraṃ {s}sampadāya samādapeti", f"{_OTH} {{m}} ပြည့်စုံခြင်း၌ မ{SAMADAP[:-1]}"),
}
for _f, (_op, _om, _xp, _xm) in _FORMS.items():
    _parts = [(f"{_op.format(s=s)}, {_xp.format(s=s)}", f"{_om.format(m=m)}{C} {_xm.format(m=m)}") for s, m in SAMP]
    _kp, _km = idha(_parts, ["; "] * 4)
    S(_kp + ".", _km + END)
# the Pāli writes «paññāsampanno» / «paññāsampadāya» (ā): fix the keys built with «paññasampanno»
for _k in [k for k in SENT5 if "paññasampa" in k]:
    SENT5[_k.replace("paññasampa", "paññāsampa")] = SENT5.pop(_k)

# ---- ^4-174: tormenting oneself
S("Idhekacco puggalo acelako hoti muttācāro hatthāpalekhano [hatthāvalekhano (syā.)], naehibhaddantiko "
  "natiṭṭhabhaddantiko nābhihaṭaṃ na uddissakataṃ na nimantanaṃ sādiyati, so na kumbhimukhā paṭiggaṇhāti na "
  "kaḷopimukhā [kalopimukhā (sī. syā.) ma. ni. 2.7] paṭiggaṇhāti, na eḷakamantaraṃ na daṇḍamantaraṃ na musalamantaraṃ "
  "na dvinnaṃ bhuñjamānānaṃ na gabbhiniyā na pāyamānāya na purisantaragatāya, na saṅkittīsu na yattha sā upaṭṭhito "
  "hoti na yattha makkhikā saṇḍasaṇḍacārinī, na macchaṃ na maṃsaṃ na suraṃ na merayaṃ na thusodakaṃ pivati.",
  f"{IDHA} အဝတ် မဝတ်သူ {COP}{C} ကျင့်ဝတ်ကို စွန့်လွှတ်သူ၊ လက်ကို လျက်သူ ⟦0⟧ {COP}{C} “အရှင်၊ လာပါ”ဟု ဆိုလျှင် "
  "မလာသူ၊ “အရှင်၊ ရပ်ပါ”ဟု ဆိုလျှင် မရပ်သူ ဖြစ်၏၊ ယူဆောင်လာသော ဆွမ်းကို မသာယာ၊ မိမိအတွက် ရည်ရွယ်၍ ပြုသော "
  "ဆွမ်းကို မသာယာ၊ ပင့်ဖိတ်ခြင်းကို မသာယာ၊ ထိုသူသည် အိုး၏ နှုတ်ခမ်းမှ မခံယူ၊ ဒယ်အိုး၏ နှုတ်ခမ်းမှ ⟦1⟧ မခံယူ၊ "
  "တံခါးခုံကို ကြားခံ၍ မခံယူ၊ တုတ်ကို ကြားခံ၍ မခံယူ၊ ကျည်ပွေ့ကို ကြားခံ၍ မခံယူ၊ အတူ စားနေသော နှစ်ယောက်ထံမှ "
  "မခံယူ၊ ကိုယ်ဝန် ရှိသော မိန်းမထံမှ မခံယူ၊ နို့တိုက်နေသော မိန်းမထံမှ မခံယူ၊ ယောက်ျားနှင့် အတူ ရှိနေသော "
  "မိန်းမထံမှ မခံယူ၊ ငတ်မွတ်ချိန်၌ စုဆောင်းထားသော ဆွမ်းကို မခံယူ၊ ခွေး ရပ်စောင့်နေရာ၌ မခံယူ၊ ယင်ကောင်တို့ "
  "အုပ်လိုက် ပျံဝဲနေရာ၌ မခံယူ၊ ငါးကို မစား၊ အသားကို မစား၊ သေရည်ကို မသောက်၊ အရက်ကို မသောက်၊ ဖွဲရေကို မသောက်"
  f"{END}")
S("So ekāgāriko vā hoti ekālopiko, dvāgāriko vā hoti dvālopiko…pe… sattāgāriko vā hoti sattālopiko; ekissāpi "
  "dattiyā yāpeti, dvīhipi dattīhi yāpeti…pe… sattahipi dattīhi yāpeti; ekāhikampi āhāraṃ āhāreti, dvīhikampi "
  "[dvāhikampi (sī.)] āhāraṃ āhāreti…pe… sattāhikampi āhāraṃ āhāreti.",
  f"{SO} အိမ် တစ်အိမ်သာ ဆွမ်းခံ၍ တစ်လုတ်သာ စားသူ ဖြစ်၏၊ အိမ် နှစ်အိမ်သာ ဆွမ်းခံ၍ နှစ်လုတ်သာ စားသူ ဖြစ်၏{PE} "
  f"အိမ် ခုနစ်အိမ်သာ ဆွမ်းခံ၍ ခုနစ်လုတ်သာ စားသူ ဖြစ်၏၊ ဆွမ်း တစ်ခွက်ဖြင့်လည်း မျှတ၏၊ ဆွမ်း နှစ်ခွက်ဖြင့်လည်း "
  f"မျှတ၏{PE} ဆွမ်း ခုနစ်ခွက်ဖြင့်လည်း မျှတ၏၊ တစ်ရက်ခြားလည်း အစာကို စား၏၊ နှစ်ရက်ခြား ⟦0⟧လည်း အစာကို စား၏{PE} "
  f"ခုနစ်ရက်ခြားလည်း အစာကို စား၏{END}")
S("Iti evarūpaṃ aḍḍhamāsikampi pariyāyabhattabhojanānuyogamanuyutto viharati.",
  f"ဤသို့ ဤကဲ့သို့သော လဝက်ခြား အလှည့်ကျ အစာ စားခြင်း၌လည်း အားထုတ်လျက် နေ၏{END}")
_FOODS = ["ဟင်းရွက်", "ဆပ်", "တောစပါး", "သားရေ အပိုင်းအစ", "ရေညှိ", "ဖွဲနု", "ထမင်းရည်ချ", "နှမ်းဖတ်", "မြက်", "နွားချေး"]
S("So sākabhakkho vā hoti sāmākabhakkho vā hoti nīvārabhakkho vā hoti daddulabhakkho vā hoti haṭabhakkho vā hoti "
  "kaṇabhakkho vā hoti ācāmabhakkho vā hoti piññākabhakkho vā hoti tiṇabhakkho vā hoti gomayabhakkho vā hoti, "
  "vanamūlaphalāhāro yāpeti pavattaphalabhojī.",
  f"{SO} " + f"{C} ".join(f"{x}ကို စားသူဖြစ်စေ" for x in _FOODS) +
  f" {COP}{C} တော၌ ရှိသော အမြစ်နှင့် အသီးကို အစာပြု၍ မျှတ၏၊ ကြွေကျသော အသီးကို စားသူ ဖြစ်၏{END}")
_CLOTH = ["လျှော် အဝတ်", "လျှော် ရောသော အဝတ်", "အလောင်းကို ပတ်သော အဝတ်", "ပံ့သကူ အဝတ်", "သစ်ခေါက် အဝတ်", "သမင်သားရေ",
          "သမင်သားရေ အစ", "ကုသမြက်ဖြင့် ရက်သော အဝတ်", "သစ်ခေါက် အမျှင်ဖြင့် ရက်သော အဝတ်", "ပျဉ်ပြားဖြင့် ပြုသော အဝတ်",
          "လူ့ဆံပင်ဖြင့် ရက်သော ကမ္ဗလာ", "တိရစ္ဆာန် အမွေးဖြင့် ရက်သော ကမ္ဗလာ", "ဇီးကွက် အတောင်"]
S("So sāṇānipi dhāreti masāṇānipi dhāreti chavadussānipi dhāreti paṃsukūlānipi dhāreti tirīṭānipi dhāreti "
  "ajinampi dhāreti ajinakkhipampi dhāreti kusacīrampi dhāreti vākacīrampi dhāreti phalakacīrampi dhāreti "
  "kesakambalampi dhāreti vāḷakambalampi dhāreti ulūkapakkhampi [ulukapakkhampi (sī. syā.)] dhāreti, "
  "kesamassulocakopi hoti kesamassulocanānuyogamanuyutto, ubbhaṭṭhakopi hoti āsanapaṭikkhitto, ukkuṭikopi hoti "
  "ukkuṭikappadhānamanuyutto, kaṇṭakāpassayikopi hoti kaṇṭakāpassaye seyyaṃ kappeti, sāyatatiyakampi "
  "[sāyaṃtatiyakampi (syā. ka.) ma. ni. 2.7] udakorohanānuyogamanuyutto viharati.",
  f"{SO} " + f"{C} ".join(f"{x}ကိုလည်း{' ⟦0⟧' if x == 'ဇီးကွက် အတောင်' else ''} ဝတ်၏" for x in _CLOTH) +
  f"{C} ဆံပင်နှင့် မုတ်ဆိတ်ကို နုတ်သူလည်း ဖြစ်၏၊ ဆံပင်နှင့် မုတ်ဆိတ်ကို နုတ်ခြင်း၌ အားထုတ်သူ ဖြစ်၏၊ မတ်တတ် "
  f"ရပ်သူလည်း ဖြစ်၏၊ ထိုင်ခုံကို ပယ်သူ ဖြစ်၏၊ ခြောင်းကြောင့်ချ ထိုင်သူလည်း ဖြစ်၏၊ ခြောင်းကြောင့်ချ ထိုင်၍ "
  f"ကြိုးစားခြင်း၌ အားထုတ်သူ ဖြစ်၏၊ ဆူးပေါ်၌ လျောင်းသူလည်း ဖြစ်၏၊ ဆူးပေါ်၌ အိပ်ရာ ပြု၏၊ ညနေ အပါအဝင် နေ့စဉ် "
  f"သုံးကြိမ် ⟦1⟧ ရေ ဆင်းခြင်း၌ အားထုတ်လျက် နေ၏{END}")
S("Iti evarūpaṃ anekavihitaṃ kāyassa ātāpanaparitāpanānuyogamanuyutto viharati.",
  f"ဤသို့ ဤကဲ့သို့သော အမျိုးမျိုးသော ကိုယ်ကို ပူလောင်စေခြင်း၊ ပူပန်စေခြင်း၌ အားထုတ်လျက် နေ၏{END}")
wit("2", "^2-829", "anekavihitaṃ pubbenivāsaṃ", "အမျိုးမျိုးသော")

# ---- ^4-175: tormenting others
S("Idhekacco puggalo orabbhiko hoti sūkariko sākuṇiko māgaviko luddo macchaghātako coro coraghātako goghātako "
  "bandhanāgāriko, ye vā panaññepi keci kurūrakammantā.",
  f"{IDHA} သိုး သတ်သူ၊ ဝက် သတ်သူ၊ ငှက် ဖမ်းသူ၊ သားကောင် ဖမ်းသူ၊ မုဆိုး၊ ငါး သတ်သူ၊ သူခိုး၊ သူခိုးကို "
  f"သတ်သူ၊ နွား သတ်သူ၊ ထောင်စောင့် {COP}{C} သို့မဟုတ် ကြမ်းကြုတ်သော အလုပ် ရှိကြသော အခြားသူတို့လည်း ဖြစ်ကြ၏{END}")

# ---- ^4-176: the king's sacrifice (tormenting oneself and others)
SHAVE = "ဆံပင်နှင့် မုတ်ဆိတ်ကို ရိတ်၍"                       # kesamassuṃ ohāretvā
S("Idhekacco puggalo rājā vā hoti khattiyo muddhāvasitto [muddhābhisitto (syā. ka.)] brāhmaṇo vā mahāsālo.",
  f"{IDHA} ဘိသိက်ခံ ⟦0⟧ မင်းမျိုး ဘုရင်ဖြစ်စေ၊ ကြွယ်ဝသော ပုဏ္ဏားဖြစ်စေ {COP}{END}")
S("So puratthimena narassa navaṃ sandhāgāraṃ [santāgāraṃ (syā.), yaññāgāraṃ (sī.)] kārāpetvā kesamassuṃ ohāretvā "
  "kharājinaṃ [khurājinaṃ (syā. ka.)] nivāsetvā sappitelena kāyaṃ abbhañjitvā migavisāṇena piṭṭhiṃ kaṇḍuvamāno "
  "[kaṇḍūyamāno (sī.)] sandhāgāraṃ pavisati saddhiṃ mahesiyā brāhmaṇena ca purohitena.",
  f"{SO} လူ၏ အရှေ့ဘက်၌ အဆောင်သစ် ⟦0⟧ကို ဆောက်စေ၍ {SHAVE} ကြမ်းသော သားရေ ⟦1⟧ကို ဝတ်၍ ထောပတ်နှင့် ဆီဖြင့် "
  f"ကိုယ်ကို လိမ်း၍ သမင်ချိုဖြင့် ကျောကို ကုတ်လျက် ⟦2⟧ မိဖုရားနှင့်လည်းကောင်း၊ ပုဏ္ဏား ပုရောဟိတ်နှင့်လည်းကောင်း "
  f"အတူ ထိုအဆောင်သို့ ဝင်၏{END}")
S("So tattha anantarahitāya bhūmiyā haritupalittāya seyyaṃ kappeti.",
  f"{SO} ထိုအဆောင်၌ အခင်း မခင်းထားသော၊ စိမ်းစိုသော နွားချေးဖြင့် လိမ်းကျံထားသော မြေပေါ်၌ အိပ်ရာ ပြု၏{END}")
S("Ekissā gāviyā sarūpavacchāya yaṃ ekasmiṃ thane khīraṃ hoti tena rājā yāpeti, yaṃ dutiyasmiṃ thane khīraṃ hoti tena "
  "mahesī yāpeti, yaṃ tatiyasmiṃ thane khīraṃ hoti tena brāhmaṇo purohito yāpeti, yaṃ catutthasmiṃ thane khīraṃ hoti "
  "tena aggiṃ juhati, avasesena vacchako yāpeti.",
  "မိခင်နှင့် အဆင်းတူသော နွားသငယ် ရှိသော နွားမ တစ်ကောင်၏ နို့သီး တစ်လုံး၌ ရှိသော နွားနို့ဖြင့် ဘုရင်သည် မျှတ၏၊ "
  "ဒုတိယ နို့သီး၌ ရှိသော နွားနို့ဖြင့် မိဖုရားသည် မျှတ၏၊ တတိယ နို့သီး၌ ရှိသော နွားနို့ဖြင့် ပုဏ္ဏား ပုရောဟိတ်သည် "
  "မျှတ၏၊ စတုတ္ထ နို့သီး၌ ရှိသော နွားနို့ဖြင့် မီးကို ပူဇော်၏၊ ကြွင်းကျန်သော နွားနို့ဖြင့် နွားသငယ်သည် မျှတ၏" + END)
S("So evamāha", f"{SO} ဤသို့ ဆို၏")
_SAC = [("usabhā", "နွားထီး"), ("vacchatarā", "နွားထီးပေါက်"), ("vacchatariyo", "နွားမပေါက်"), ("ajā", "ဆိတ်"),
        ("urabbhā", "သိုး")]
S('"' + ", ".join(f"ettakā {p} haññantu yaññatthāya" for p, m in _SAC) +
  ", (ettakā assā haññantu yaññatthāya) [( ) natthi sīhaḷapotthake. majjhimanikāye kandarakasuttepi evameva] "
  'ettakā rukkhā chijjantu yūpatthāya, ettakā dabbhā lūyantu barihisatthāyā"ti '
  "[parihiṃsatthāyāti (sī. syā. ka.) ma. ni. 2.9].",
  "“" + f"{C} ".join(f"ယဇ်အတွက် {m} ဤမျှကို သတ်ကြစေ" for p, m in _SAC) +
  f"{C} (ယဇ်အတွက် မြင်း ဤမျှကို သတ်ကြစေ) ⟦0⟧ ယဇ်တိုင်အတွက် သစ်ပင် ဤမျှကို ခုတ်ကြစေ{C} ယဇ်ခင်းရန် မြက် ဤမျှကို "
  f"ရိတ်ကြစေ”ဟု ⟦1⟧{END}")
S("Yepissa te honti dāsāti vā pessāti vā kammakarāti vā, tepi daṇḍatajjitā bhayatajjitā assumukhā rudamānā "
  "parikammāni karonti.",
  "ထိုသူ၏ ကျွန်ဟူ၍ဖြစ်စေ၊ စေခိုင်းရသူဟူ၍ဖြစ်စေ၊ အလုပ်သမားဟူ၍ဖြစ်စေ ရှိကြသော သူတို့သည်လည်း ဒဏ်ကြောင့် "
  f"ခြိမ်းခြောက်ခံရလျက်၊ ဘေးကြောင့် ခြိမ်းခြောက်ခံရလျက်၊ မျက်ရည် စီးလျက် ငိုကြွေးလျက် အလုပ်တို့ကို လုပ်ကြ၏{END}")

# ---- ^4-177 … ^4-185: neither tormenting oneself nor others (the going forth and the training)
S("So anattantapo aparantapo diṭṭheva dhamme nicchāto nibbuto sītībhūto sukhappaṭisaṃvedī brahmabhūtena attanā "
  "viharati.", ANATTANTAPA + END)


def plain(s):
    """pi-2 Burmese of the Tathāgata without the honorific (the same Pāli said of a monk here)."""
    return s.replace("တော်မူ၏", "၏").replace("တော်မူသည်", "၏")


TATH = F.TATHAGATA                                  # tathāgato = «မြတ်စွာဘုရား» (pi-2; harmonise B4)
S("Idha tathāgato loke uppajjati arahaṃ sammāsambuddho vijjācaraṇasampanno sugato lokavidū anuttaro "
  "purisadammasārathi satthā devamanussānaṃ buddho bhagavā.",
  f"ဤလောက၌ {TATH}သည် ပွင့်ထွန်းတော်မူ၏၊ ရဟန္တာ၊ {W['sammasambuddha']}၊ {W['vijja']}နှင့် အကျင့် ပြည့်စုံတော်မူသူ၊ "
  "ကောင်းသော လားရာသို့ ကြွတော်မူသူ၊ လောကကို သိတော်မူသူ၊ ဆုံးမထိုက်သော ယောက်ျားတို့ကို ဆုံးမရာ၌ အတုမရှိသူ၊ "
  f"နတ်နှင့် လူတို့၏ ဆရာ၊ သစ္စာတို့ကို သိတော်မူသူ၊ {F.BHAGAVA_EPITHET} ဖြစ်တော်မူ၏{END}")   # bhagavā: the epithet (B4)
SAYAM = wit("2", "^2-831", "sayaṃ abhiññā sacchikatvā", "ကိုယ်တိုင် ထူးကဲစွာ သိ၍ မျက်မှောက်ပြုပြီး")
S("So imaṃ lokaṃ sadevakaṃ samārakaṃ sabrahmakaṃ sassamaṇabrāhmaṇiṃ pajaṃ sadevamanussaṃ sayaṃ abhiññā "
  "sacchikatvā pavedeti.",
  f"ထို{TATH}သည် နတ်နှင့် တကွ၊ မာရ်နှင့် တကွ၊ ဗြဟ္မာနှင့် တကွ ဖြစ်သော ဤလောကကိုလည်းကောင်း၊ ရဟန်း ပုဏ္ဏားနှင့် "
  f"တကွ၊ နတ် လူနှင့် တကွ ဖြစ်သော သတ္တဝါ အပေါင်းကိုလည်းကောင်း {SAYAM} ဟောကြားတော်မူ၏{END}")
BRAHMA = wit("2", "^2-509", "brahmacariye", "မြင့်မြတ်သော အကျင့်")
S("So dhammaṃ deseti ādikalyāṇaṃ majjhekalyāṇaṃ pariyosānakalyāṇaṃ sātthaṃ sabyañjanaṃ, kevalaparipuṇṇaṃ "
  "parisuddhaṃ brahmacariyaṃ pakāseti.",
  f"ထို{TATH}သည် အစ၌ ကောင်းသော၊ အလယ်၌ ကောင်းသော၊ အဆုံး၌ ကောင်းသော၊ အနက် ပြည့်စုံသော၊ သဒ္ဒါ ပြည့်စုံသော "
  f"တရားကို ဟောတော်မူ၏၊ အလုံးစုံ ပြည့်စုံ၍ စင်ကြယ်သော {BRAHMA}ကို ထင်ရှားပြတော်မူ၏{END}")
S("Taṃ dhammaṃ suṇāti gahapati vā gahapatiputto vā aññatarasmiṃ vā kule paccājāto.",
  f"ထိုတရားကို သူကြွယ်ဖြစ်စေ၊ သူကြွယ်၏ သားဖြစ်စေ၊ အခြားသော အမျိုး၌ {REBORN}ဖြစ်စေ ကြားနာ၏{END}")
S("So taṃ dhammaṃ sutvā tathāgate saddhaṃ paṭilabhati.",
  f"{SO} ထိုတရားကို ကြားနာ၍ {TATH}၌ ယုံကြည်မှုကို ရရှိ၏{END}")
S("So tena saddhāpaṭilābhena samannāgato iti paṭisañcikkhati",
  f"{SO} ထိုယုံကြည်မှုကို ရရှိခြင်းနှင့် {SAMANN[:-2]}လျက် ဤသို့ ဆင်ခြင်၏")
GOFORTH = "အိမ်မှ ထွက်၍ အိမ်ရာ မရှိသော ရဟန်းအဖြစ်သို့ ကူး"     # agārasmā anagāriyaṃ pabbajati
ROBE = "ဖန်ရည်စွန်းသော သင်္ကန်းတို့ကို ဝတ်ရုံ၍"               # kāsāyāni vatthāni acchādetvā
new("kesamassuṃ ohāretvā", SHAVE)
new("kāsāyāni vatthāni acchādetvā", ROBE)
new("agārasmā anagāriyaṃ pabbajati", GOFORTH + "၏")
S('"sambādho gharāvāso rajāpatho, abbhokāso pabbajjā.',
  f"“အိမ်ရာ၌ နေခြင်းသည် ကျဉ်းကျပ်၏၊ မြူမှုန် တက်ရာ လမ်း ဖြစ်၏၊ ရဟန်း ပြုခြင်းသည် လွင်တီးခေါင်ကဲ့သို့ ဖြစ်၏{END}")
S("Nayidaṃ sukaraṃ agāraṃ ajjhāvasatā ekantaparipuṇṇaṃ ekantaparisuddhaṃ saṅkhalikhitaṃ brahmacariyaṃ carituṃ.",
  f"အိမ်ရာ၌ နေသူသည် စင်စစ် ပြည့်စုံ၍ စင်စစ် စင်ကြယ်သော၊ ပွတ်ထားသော ခရုသင်းကဲ့သို့ ဖြူစင်သော {BRAHMA}ကို "
  f"ကျင့်ရန် မလွယ်ကူ{END}")
S('Yaṃnūnāhaṃ kesamassuṃ ohāretvā kāsāyāni vatthāni acchādetvā agārasmā anagāriyaṃ pabbajeyya"nti! So aparena '
  "samayena appaṃ vā bhogakkhandhaṃ pahāya mahantaṃ vā bhogakkhandhaṃ pahāya appaṃ vā ñātiparivaṭṭaṃ pahāya mahantaṃ "
  "vā ñātiparivaṭṭaṃ pahāya kesamassuṃ ohāretvā kāsāyāni vatthāni acchādetvā agārasmā anagāriyaṃ pabbajati.",
  f"ငါသည် {SHAVE} {ROBE} {GOFORTH}ရလျှင် ကောင်းလေစွ”ဟု ဆင်ခြင်၏{END} {SO} နောက်ကာလ၌ နည်းသော စည်းစိမ် "
  "အစုကိုဖြစ်စေ ပယ်၍၊ များသော စည်းစိမ် အစုကိုဖြစ်စေ ပယ်၍၊ နည်းသော ဆွေမျိုး အပေါင်းကိုဖြစ်စေ ပယ်၍၊ များသော ဆွေမျိုး "
  f"အပေါင်းကိုဖြစ်စေ ပယ်၍ {SHAVE} {ROBE} {GOFORTH}၏{END}")
HITA = wit("2", "^2-508", "sabbapāṇabhūtahitānukampī", "ခပ်သိမ်းသော သတ္တဝါတို့၏ အကျိုးကို စာနာလျက်")
S("So evaṃ pabbajito samāno bhikkhūnaṃ sikkhāsājīvasamāpanno pāṇātipātaṃ pahāya pāṇātipātā paṭivirato hoti "
  "nihitadaṇḍo nihitasattho lajjī dayāpanno sabbapāṇabhūtahitānukampī viharati.",
  f"{SO} ဤသို့ ရဟန်း ပြုပြီးသည် ဖြစ်၍ ရဟန်းတို့၏ သိက္ခာနှင့် {AJIVA}သို့ ရောက်လျက် သူ့အသက်ကို သတ်ခြင်းကို ပယ်၍ "
  f"{ABL['pana'][1]} {ABST} {COP}{C} တုတ်ကို ချထားသူ၊ လက်နက်ကို ချထားသူ၊ ရှက်တတ်သူ၊ သနားကြင်နာမှု ရှိသူ ဖြစ်လျက် "
  f"{HITA} နေ၏{END}")
S("Adinnādānaṃ pahāya adinnādānā paṭivirato hoti dinnādāyī dinnapāṭikaṅkhī, athenena sucibhūtena attanā viharati.",
  f"မပေးသည်ကို ယူခြင်းကို ပယ်၍ {ABL['adin'][1]} {ABST} {COP}{C} ပေးသည်ကိုသာ ယူသူ၊ ပေးသည်ကိုသာ မျှော်လင့်သူ ဖြစ်၍ "
  f"ခိုးဝှက်ခြင်း မရှိသော၊ စင်ကြယ်သော မိမိကိုယ်ဖြင့် နေ၏{END}")
S("Abrahmacariyaṃ pahāya brahmacārī hoti ārācārī [anācārī (ka.)] paṭivirato methunā gāmadhammā.",
  f"{BRAHMA} မဟုတ်သည်ကို ပယ်၍ {BRAHMA}ကို ကျင့်သူ {COP}{C} ဝေးကွာစွာ ကျင့်သူ ⟦0⟧ ဖြစ်၍ ရွာသားတို့၏ အလေ့ ဖြစ်သော "
  f"မေထုန်မှ {ABST} {COP}{END}")
S("Musāvādaṃ pahāya musāvādā paṭivirato hoti saccavādī saccasandho theto paccayiko avisaṃvādako lokassa.",
  f"မုသား ပြောခြင်းကို ပယ်၍ {ABL['musa'][1]} {ABST} {COP}{C} မှန်သော စကားကို ပြောသူ၊ မှန်ကန်မှုဖြင့် စကားကို "
  f"ဆက်စပ်သူ၊ တည်ကြည်သူ၊ ယုံကြည်ထိုက်သူ၊ လောကကို မလှည့်ဖြားသူ {COP}{END}")
S("Pisuṇaṃ vācaṃ pahāya pisuṇāya vācāya paṭivirato hoti, ito sutvā na amutra akkhātā imesaṃ bhedāya, amutra vā "
  "sutvā na imesaṃ akkhātā amūsaṃ bhedāya.",
  f"ကုန်းတိုက်သော စကားကို ပယ်၍ {ABL['pisu'][1]} {ABST} {COP}{C} ဤသူတို့ကို ကွဲစေရန် ဤနေရာမှ ကြား၍ ထိုနေရာ၌ "
  f"မပြောကြားသူ၊ ထိုသူတို့ကို ကွဲစေရန် ထိုနေရာမှ ကြား၍ ဤသူတို့အား မပြောကြားသူ {COP}{END}")
S("Iti bhinnānaṃ vā sandhātā sahitānaṃ vā anuppadātā samaggārāmo samaggarato samagganandī samaggakaraṇiṃ vācaṃ "
  "bhāsitā hoti.",
  "ဤသို့ ကွဲပြားနေသူတို့ကို ပြန်လည် စည်းလုံးစေသူ၊ စည်းလုံးနေသူတို့ကို အားပေးသူ၊ ညီညွတ်ခြင်း၌ မွေ့လျော်သူ၊ "
  f"ညီညွတ်ခြင်း၌ ပျော်ပိုက်သူ၊ ညီညွတ်ခြင်း၌ နှစ်သက်သူ ဖြစ်၍ ညီညွတ်စေသော စကားကို {SPEAK} {COP}{END}")
S("Pharusaṃ vācaṃ pahāya pharusāya vācāya paṭivirato hoti.",
  f"ကြမ်းတမ်းသော စကားကို ပယ်၍ {ABL['phar'][1]} {ABST} {COP}{END}")
wit("2", "^2-643", "piyaṃ manāpaṃ", "စိတ်နှင့် တွေ့သော")
S("Yā sā vācā nelā kaṇṇasukhā pemanīyā hadayaṅgamā porī bahujanakantā bahujanamanāpā tathārūpiṃ vācaṃ bhāsitā hoti.",
  F.NELA + END)                                     # harmonise B2: pi-1 ^1-1350 (neḷā …), = ch4 ^4-99
S("Samphappalāpaṃ pahāya samphappalāpā paṭivirato hoti, kālavādī bhūtavādī atthavādī dhammavādī vinayavādī "
  "nidhānavatiṃ vācaṃ bhāsitā kālena sāpadesaṃ pariyantavatiṃ atthasaṃhitaṃ.",
  f"အကျိုးမဲ့ ပြိန်ဖျင်းသော စကားကို ပယ်၍ {ABL['samp'][1]} {ABST} {COP}{C} သင့်လျော်သော အချိန်၌ ပြောသူ၊ "
  "အမှန်ကို ပြောသူ၊ အကျိုးကို ပြောသူ၊ တရားကို ပြောသူ၊ ဝိနည်းကို ပြောသူ ဖြစ်၍ သင့်လျော်သော အချိန်၌ မှတ်သားထိုက်သော၊ "
  f"အကြောင်း ပြချက်နှင့် တကွ ဖြစ်သော၊ အပိုင်းအခြား ရှိသော၊ အကျိုးနှင့် စပ်သော စကားကို {SPEAK} {COP}{END}")
S("So bījagāmabhūtagāmasamārambhā paṭivirato hoti, ekabhattiko hoti rattūparato virato vikālabhojanā, "
  "naccagītavāditavisūkadassanā paṭivirato hoti, mālāgandhavilepanadhāraṇamaṇḍanavibhūsanaṭṭhānā paṭivirato hoti, "
  "uccāsayanamahāsayanā paṭivirato hoti, jātarūparajatapaṭiggahaṇā paṭivirato hoti.",
  f"{SO} မျိုးစေ့ အပေါင်း၊ အပင် အပေါင်းကို ဖျက်ဆီးခြင်းမှ {ABST} {COP}{C} တစ်နပ်တည်းသာ စားသူ {COP}{C} ညစာမှ "
  f"{ABST}၊ အချိန်လွန် စားခြင်းမှ ကင်းဝေးသူ {COP}{C} ကခြင်း၊ သီချင်းဆိုခြင်း၊ တီးမှုတ်ခြင်း၊ ကုသိုလ်ကို ဆန့်ကျင်သော "
  f"ပွဲသဘင်ကို ကြည့်ခြင်းမှ {ABST} {COP}{C} ပန်း နံ့သာ နံ့သာပျောင်းတို့ကို ဆောင်ခြင်း၊ အလှပြင်ခြင်း၊ တန်ဆာဆင်ခြင်း၏ "
  f"အကြောင်းမှ {ABST} {COP}{C} မြင့်သော အိပ်ရာ၊ မြတ်သော အိပ်ရာမှ {ABST} {COP}{C} ရွှေ ငွေကို လက်ခံခြင်းမှ "
  f"{ABST} {COP}{END}")
_ACC = [("Āmakadhañña", "စပါး အစိမ်းကို"), ("āmakamaṃsa", "အသား အစိမ်းကို"), ("itthikumārikā", "မိန်းမ၊ မိန်းကလေးကို"),
        ("dāsidāsa", "ကျွန်မ၊ ကျွန်ယောက်ျားကို"), ("ajeḷaka", "ဆိတ်၊ သိုးကို"), ("kukkuṭasūkara", "ကြက်၊ ဝက်ကို"),
        ("hatthigavāssavaḷava", "ဆင်၊ နွား၊ မြင်း၊ မြင်းမကို"), ("khettavatthu", "လယ်၊ မြေကို")]
S(", ".join(f"{p}paṭiggahaṇā paṭivirato hoti" for p, m in _ACC) +
  ", dūteyyapahiṇagamanānuyogā paṭivirato hoti, kayavikkayā paṭivirato hoti, tulākūṭakaṃsakūṭamānakūṭā paṭivirato "
  "hoti, ukkoṭanavañcananikatisāciyogā [… sāviyogā (syā. ka.)] paṭivirato hoti, "
  "chedanavadhabandhanaviparāmosaālopasahasākārā paṭivirato hoti.",
  f"{C} ".join(f"{m} လက်ခံခြင်းမှ {ABST} {COP}" for p, m in _ACC) +
  f"{C} တမန် လုပ်ခြင်း၊ စေခိုင်းရာသို့ သွားခြင်း၌ အားထုတ်ခြင်းမှ {ABST} {COP}{C} ရောင်းဝယ်ခြင်းမှ {ABST} {COP}{C} "
  f"ချိန်ခွင် လိမ်ခြင်း၊ ကြေးခွက် လိမ်ခြင်း၊ အတိုင်းအတာ လိမ်ခြင်းမှ {ABST} {COP}{C} တံစိုး ယူခြင်း၊ လှည့်ဖြားခြင်း၊ "
  f"စဉ်းလဲခြင်း၊ ကောက်ကျစ်သော နည်းလမ်း ⟦0⟧မှ {ABST} {COP}{C} ဖြတ်ခြင်း၊ သတ်ခြင်း၊ နှောင်ဖွဲ့ခြင်း၊ ခိုးဆိုးခြင်း၊ "
  f"လုယက်ခြင်း၊ အနိုင်အထက် ပြုခြင်းမှ {ABST} {COP}{END}")
ROBE_FOOD = "ကိုယ်ကို စောင့်ရှောက်ရုံ သင်္ကန်း၊ ဝမ်းကို မျှတရုံ ဆွမ်းဖြင့် ရောင့်ရဲသူ ဖြစ်၏"
S("So santuṭṭho hoti kāyaparihārikena cīvarena kucchiparihārikena piṇḍapātena.", f"{SO} {ROBE_FOOD}{END}")
S("So yena yeneva pakkamati samādāyeva pakkamati, seyyathāpi nāma pakkhī sakuṇo yena yeneva ḍeti sapattabhārova ḍeti.",
  "ထိုသူသည် ထွက်ခွာရာ အရပ်တိုင်း၌ ယူဆောင်၍သာ ထွက်ခွာ၏၊ ဥပမာအားဖြင့် အတောင် ရှိသော ငှက်သည် ပျံရာ အရပ်တိုင်း၌ "
  f"မိမိ အတောင်တို့ဟူသော ဝန်ကိုသာ ဆောင်၍ ပျံသကဲ့သို့တည်း{END}")
S("Evamevaṃ bhikkhu santuṭṭho hoti kāyaparihārikena cīvarena kucchiparihārikena piṇḍapātena.",
  f"ထို့အတူပင် ရဟန်းသည် {ROBE_FOOD}{END}")
S("So yena yeneva pakkamati samādāyeva pakkamati.", f"ထိုသူသည် ထွက်ခွာရာ အရပ်တိုင်း၌ ယူဆောင်၍သာ ထွက်ခွာ၏{END}")
SILAKH = f"ဤအရိယာ သီလ {F.KH}"                                    # iminā ariyena sīlakkhandhena
INDSAM = f"ဤအရိယာ {W['indriya_sense'].split('တို့၏')[0]} စောင့်စည်းမှု"   # iminā ariyena indriyasaṃvarena
SATISAMP = "ဤအရိယာ သတိနှင့် ကောင်းစွာ ဆင်ခြင်သိမြင်ခြင်း"                 # iminā ariyena satisampajaññena
SANTUTTHI = "ဤအရိယာ ရောင့်ရဲမှု"                                       # imāya ariyāya santuṭṭhiyā
S("So iminā ariyena sīlakkhandhena samannāgato ajjhattaṃ anavajjasukhaṃ paṭisaṃvedeti.",
  f"{SO} {SILAKH}နှင့် {SAMANN[:-2]}လျက် မိမိ၌ အပြစ် မရှိသော သာယာမှုကို ခံစား၏{END}")
# ^4-181: the sense restraint (pi-1 ^1-1354, the same clauses)
_I = final_sents("1", "^1-1354")
assert _I[1].startswith("ဤလောက၌ အချို့သော သူသည် မျက်စိဖြင့်") and _I[3].startswith("နားဖြင့်")
S("So cakkhunā rūpaṃ disvā na nimittaggāhī hoti nānubyañjanaggāhī.",
  f"{SO} " + _I[1][len("ဤလောက၌ အချို့သော သူသည် "):] + END)
S("Yatvādhikaraṇamenaṃ cakkhundriyaṃ asaṃvutaṃ viharantaṃ abhijjhādomanassā pāpakā akusalā dhammā anvāssaveyyuṃ, "
  "tassa saṃvarāya paṭipajjati, rakkhati cakkhundriyaṃ, cakkhundriye saṃvaraṃ āpajjati; sotena saddaṃ sutvā…pe… "
  "ghānena gandhaṃ ghāyitvā…pe… jivhāya rasaṃ sāyitvā…pe… kāyena phoṭṭhabbaṃ phusitvā…pe… manasā dhammaṃ viññāya "
  "na nimittaggāhī hoti nānubyañjanaggāhī.", f"{_I[2]}{C} {_I[3]}{END}")
S("Yatvādhikaraṇamenaṃ manindriyaṃ asaṃvutaṃ viharantaṃ abhijjhādomanassā pāpakā akusalā dhammā anvāssaveyyuṃ, "
  "tassa saṃvarāya paṭipajjati, rakkhati manindriyaṃ, manindriye saṃvaraṃ āpajjati.", _I[4] + END)
S("So iminā ariyena indriyasaṃvarena samannāgato ajjhattaṃ abyāsekasukhaṃ paṭisaṃvedeti.",
  f"{SO} {INDSAM}နှင့် {SAMANN[:-2]}လျက် မိမိ၌ ကိလေသာ မရောနှောသော သာယာမှုကို ခံစား၏{END}")
# ^4-182, ^4-183: clear comprehension, solitude, the hindrances, the jhānas (pi-2 ^2-508, the same clauses)
_J = final_sents("2", "^2-508")
assert _J[1].startswith("ထိုရဟန်းသည် ရှေ့သို့") and _J[9].startswith("ထိုရဟန်းသည် စိတ်ကို ညစ်နွမ်း")
_MONK = "ထိုရဟန်းသည် "
S("So abhikkante paṭikkante sampajānakārī hoti, ālokite vilokite sampajānakārī hoti, samiñjite pasārite "
  "sampajānakārī hoti, saṅghāṭipattacīvaradhāraṇe sampajānakārī hoti, asite pīte khāyite sāyite sampajānakārī hoti, "
  "uccārapassāvakamme sampajānakārī hoti, gate ṭhite nisinne sutte jāgarite bhāsite tuṇhībhāve sampajānakārī hoti.",
  f"{SO} " + _J[1][len(_MONK):].replace(" [စာလုံးပေါင်းကွဲ (Sī., Syā.): sammiñjite]", "") + END)
_e = _J[2].index("ကောက်ရိုးပုံ ဖြစ်သော") + len("ကောက်ရိုးပုံ ဖြစ်သော")
VIVITTA = _J[2][len(_MONK):_e] + " ဆိတ်ငြိမ်သော အိပ်ရာ နေရာကို ဆည်းကပ်၏"
S("So iminā ca ariyena sīlakkhandhena samannāgato iminā ca ariyena indriyasaṃvarena samannāgato iminā ca ariyena "
  "satisampajaññena samannāgato imāya ca ariyāya santuṭṭhiyā samannāgato [passa ma. ni. 2 kandarakasutte; a. ni. 1 "
  "attantapasutte ca] vivittaṃ senāsanaṃ bhajati araññaṃ rukkhamūlaṃ pabbataṃ kandaraṃ giriguhaṃ susānaṃ vanapatthaṃ "
  "abbhokāsaṃ palālapuñjaṃ.",
  f"{SO} " + f"{C} ".join(f"{x}နှင့်လည်း {SAMANN[:-2]}လျက်" for x in (SILAKH, INDSAM, SATISAMP, SANTUTTHI)) +
  f" ⟦0⟧ {VIVITTA}{END}")
S("So pacchābhattaṃ piṇḍapātapaṭikkanto nisīdati pallaṅkaṃ ābhujitvā ujuṃ kāyaṃ paṇidhāya parimukhaṃ satiṃ "
  "upaṭṭhapetvā.",
  f"{SO} ဆွမ်းစားပြီးနောက် ဆွမ်းခံရာမှ ပြန်လာ၍ " + _J[3][_J[3].index("ထက်ဝယ်ဖွဲ့ခွေ၍"):] + END)
S("So abhijjhaṃ loke pahāya vigatābhijjhena cetasā viharati, abhijjhāya cittaṃ parisodheti; byāpādapadosaṃ pahāya "
  "abyāpannacitto viharati sabbapāṇabhūtahitānukampī, byāpādapadosā cittaṃ parisodheti; thinamiddhaṃ "
  "[thīnamiddhaṃ (sī. syā.)] pahāya vigatathinamiddho viharati ālokasaññī sato sampajāno, thinamiddhā cittaṃ "
  "parisodheti; uddhaccakukkuccaṃ pahāya anuddhato viharati ajjhattaṃ vūpasantacitto, uddhaccakukkuccā cittaṃ "
  "parisodheti; vicikicchaṃ pahāya tiṇṇavicikiccho viharati akathaṃkathī kusalesu dhammesu, vicikicchāya cittaṃ "
  "parisodheti.",
  f"{SO} " + _J[4][len(_MONK):] + f"{C} " +
  _J[6].replace("ထိုင်းမှိုင်းမှုနှင့် ငိုက်မျဉ်းမှုကို ပယ်၍", "ထိုင်းမှိုင်းမှုနှင့် ငိုက်မျဉ်းမှုကို ⟦0⟧ ပယ်၍", 1).join(
      [_J[5] + f"{C} ", f"{C} " + f"{C} ".join(_J[7:9])]) + END)
_JH = _J[9][:_J[9].index("၊ ရုပ်ဟု မှတ်သိမှုတို့ကို")]
_JH1, _JH2 = _JH.split(" – ")
S("So ime pañca nīvaraṇe pahāya cetaso upakkilese paññāya dubbalīkaraṇe vivicceva kāmehi vivicca akusalehi "
  "dhammehi savitakkaṃ savicāraṃ vivekajaṃ pītisukhaṃ paṭhamaṃ jhānaṃ upasampajja viharati; vitakkavicārānaṃ "
  "vūpasamā ajjhattaṃ sampasādanaṃ cetaso ekodibhāvaṃ avitakkaṃ avicāraṃ samādhijaṃ pītisukhaṃ dutiyaṃ jhānaṃ "
  "upasampajja viharati; pītiyā ca virāgā upekkhako ca viharati sato ca sampajāno sukhañca kāyena paṭisaṃvedeti, yaṃ "
  "taṃ ariyā ācikkhanti", f"{SO} " + _JH1[len(_MONK):])
S('"upekkhako satimā sukhavihārī"ti tatiyaṃ jhānaṃ upasampajja viharati; sukhassa ca pahānā dukkhassa ca pahānā '
  "pubbeva somanassadomanassānaṃ atthaṅgamā adukkhamasukhaṃ upekkhāsatipārisuddhiṃ catutthaṃ jhānaṃ upasampajja "
  "viharati.", _JH2 + END)
# ^4-183 … ^4-185: the three knowledges (pi-1 ^1-1380 names; pi-2 ^2-829 / ^2-830, without the honorific)
SAMAHITE = F.SAMAHITE                                # (moved to my4_formulas: also ch6 ^4-198, harmonise B2)
_SAM_P = ("So evaṃ samāhite citte parisuddhe pariyodāte anaṅgaṇe vigatūpakkilese mudubhūte kammaniye ṭhite "
          "āneñjappatte {} cittaṃ abhininnāmeti.")
for _p, _bid, _pp, _m in (("pubbenivāsānussatiñāṇāya", "^1-1380", "pubbenivāsānussati ñāṇaṃ",
                           "ရှေးဘဝများကို အဖန်ဖန် အောက်မေ့နိုင်သော ဉာဏ်"),
                          ("sattānaṃ cutūpapātañāṇāya", "^1-1380", "sattānaṃ cutūpapāte ñāṇaṃ",
                           "သတ္တဝါတို့၏ သေခြင်းနှင့် ဖြစ်ပေါ်ခြင်းကို သိသော ဉာဏ်"),
                          ("āsavānaṃ khayañāṇāya", "^1-1380", "āsavānaṃ khaye ñāṇaṃ",
                           "စိတ်အစွန်းအထင်းတို့ ကုန်ခန်းခြင်းကို သိသော ဉာဏ်")):
    S(_SAM_P.format(_p), f"{SO} {SAMAHITE} {wit('1', _bid, _pp, _m)}အတွက် စိတ်ကို ညွတ်စေ၏{END}")
_K = final_sents("2", "^2-829")
_KA, _KB = _K[1].split(" – ")
_KB1, _KB2 = _KB.split(" “", 1)
S("So anekavihitaṃ pubbenivāsaṃ anussarati, seyyathidaṃ",
  f"{SO} " + plain(_KA[len(f"ဤလောက၌ {W['tathagata']}သည် "):]))
S("ekampi jātiṃ dvepi jātiyo tissopi jātiyo catassopi jātiyo pañcapi jātiyo dasapi jātiyo vīsampi jātiyo tiṃsampi "
  "jātiyo cattālīsampi jātiyo paññāsampi jātiyo jātisatampi jātisahassampi jātisatasahassampi anekepi saṃvaṭṭakappe "
  "anekepi vivaṭṭakappe anekepi saṃvaṭṭavivaṭṭakappe", _KB1)
S('"amutrāsiṃ evaṃnāmo evaṃgotto evaṃvaṇṇo evamāhāro evaṃsukhadukkhapaṭisaṃvedī evamāyupariyanto, so tato cuto '
  "amutra udapādiṃ; tatrāpāsiṃ evaṃnāmo evaṃgotto evaṃvaṇṇo evamāhāro evaṃsukhadukkhapaṭisaṃvedī evamāyupariyanto, "
  'so tato cuto idhūpapanno"ti.', "“" + _KB2 + END)
S("Iti sākāraṃ sauddesaṃ anekavihitaṃ pubbenivāsaṃ anussarati.", plain(_K[2]) + END)
_L = final_sents("2", "^2-830")
_LA, _LB = _L[1].split(" – ")
S("So dibbena cakkhunā visuddhena atikkantamānusakena satte passati cavamāne upapajjamāne hīne paṇīte suvaṇṇe "
  "dubbaṇṇe, sugate duggate yathākammūpage satte pajānāti", f"{SO} " + plain(_LA[len(f"ဤလောက၌ {W['tathagata']}သည် "):]))
S('"ime vata bhonto sattā kāyaduccaritena samannāgatā, vacīduccaritena samannāgatā, manoduccaritena samannāgatā, '
  "ariyānaṃ upavādakā, micchādiṭṭhikā micchādiṭṭhikammasamādānā.", _LB + END)
S("Te kāyassa bhedā paraṃ maraṇā apāyaṃ duggatiṃ vinipātaṃ nirayaṃ upapannā.", _L[2] + END)
S("Ime vā pana bhonto sattā kāyasucaritena samannāgatā vacīsucaritena samannāgatā manosucaritena samannāgatā "
  "ariyānaṃ anupavādakā sammādiṭṭhikā sammādiṭṭhikammasamādānā.", _L[3] + END)
S('Te kāyassa bhedā paraṃ maraṇā sugatiṃ saggaṃ lokaṃ upapannā"ti.', _L[4] + END)
S("So iti dibbena cakkhunā visuddhena atikkantamānusakena satte passati cavamāne upapajjamāne hīne paṇīte "
  "suvaṇṇe dubbaṇṇe, sugate duggate yathākammūpage satte pajānāti.", f"{SO} " + plain(_L[5]) + END)
_ASV = {"kāma": "ကာမ", "bhava": "ဘဝ", "avijjā": "အမှန်ကို မသိမှု"}
wit("2", "^2-937", "Kāmāsavo, bhavāsavo, diṭṭhāsavo, avijjāsavo",
    "ကာမ စိတ်အစွန်းအထင်း၊ ဘဝ စိတ်အစွန်းအထင်း၊ အယူ စိတ်အစွန်းအထင်း၊ အမှန်ကို မသိမှု စိတ်အစွန်းအထင်း")
S("Tassa evaṃ jānato evaṃ passato kāmāsavāpi cittaṃ vimuccati, bhavāsavāpi cittaṃ vimuccati, avijjāsavāpi cittaṃ "
  "vimuccati.",
  F.JANATO)
assert F.JANATO == "ဤသို့ သိသော၊ ဤသို့ မြင်သော ထိုသူ၏ စိတ်သည် " + f"{C} ".join(
    f"{m} {W['asava']}မှလည်း လွတ်မြောက်၏" for m in _ASV.values()) + END
S("Vimuttasmiṃ vimuttamiti ñāṇaṃ hoti.", F.VIMUTTASMIM)
JATI = wit("2", "^2-191", "Tattha katamā jāti", "မွေးဖွားခြင်း")
S('"Khīṇā jāti, vusitaṃ brahmacariyaṃ, kataṃ karaṇīyaṃ, nāparaṃ itthattāyā"ti pajānāti.',
  F.KHINA)
assert F.KHINA.startswith(f"“{JATI} ကုန်ပြီ၊ {BRAHMA}ကို ကျင့်ပြီးပြီ၊ ")

# ---- ^4-187: calm and insight
LOKUT = wit("1", "^1-M2-12", "lokuttarā dhammā", "လောကကို ကျော်လွန်သော")
_RA = f"{F._RUPA_SAHA} {F.SAMAP_PL}ကိုဖြစ်စေ{C} {F._ARUPA_SAHA} {F.SAMAP_PL}ကိုဖြစ်စေ"   # (sample ^4-3)
_LM = f"{LOKUT} {W['magga']}ကိုဖြစ်စေ{C} {W['phala']}ကိုဖြစ်စေ"
_RA_P = "rūpasahagatānaṃ vā arūpasahagatānaṃ vā samāpattīnaṃ"
_LM_P = "lokuttaramaggassa vā phalassa vā"
GOT = M.GOT
S(f"Idhekacco puggalo lābhī hoti {_RA_P}, na lābhī {_LM_P}.", f"{IDHA} {_RA} {GOT} {COP}{C} {_LM} {GOT} မဟုတ်{END}")
S(f"Idhekacco puggalo lābhī hoti {_LM_P}, na lābhī {_RA_P}.", f"{IDHA} {_LM} {GOT} {COP}{C} {_RA} {GOT} မဟုတ်{END}")
S(f"Idhekacco puggalo lābhī hoti {_RA_P}, lābhī {_LM_P}.", f"{IDHA} {_RA} {GOT} {COP}{C} {_LM} {GOT} {COP}{END}")
S(f"Idhekacco puggalo neva lābhī hoti {_RA_P}, na lābhī {_LM_P}.",
  f"{IDHA} {_RA} {GOT}လည်း မဟုတ်{C} {_LM} {GOT}လည်း မဟုတ်{END}")

# ---- ^4-188, ^4-190: with the stream and against it; the four ascetics
S("Idhekacco puggalo kāme ca paṭisevati pāpañca kammaṃ karoti.",
  f"{IDHA} ကာမတို့ကိုလည်း မှီဝဲ၏၊ ယုတ်မာသော ကံကိုလည်း ပြု၏{END}")
S("Idhekacco puggalo kāme ca na paṭisevati pāpañca kammaṃ na karoti.",
  f"{IDHA} ကာမတို့ကိုလည်း မမှီဝဲ၊ ယုတ်မာသော ကံကိုလည်း မပြု{END}")
S("So sahāpi dukkhena sahāpi domanassena assumukhenapi rudamāno paripuṇṇaṃ parisuddhaṃ brahmacariyaṃ carati.",
  f"{SO} နာကျင်မှုနှင့် အတူလည်းကောင်း၊ စိတ်ဆင်းရဲမှုနှင့် အတူလည်းကောင်း၊ မျက်ရည် စီးလျက် ငိုကြွေးလျက်လည်းကောင်း "
  f"ပြည့်စုံ၍ စင်ကြယ်သော {BRAHMA}ကို ကျင့်၏{END}")
S("Idhekacco puggalo pañcannaṃ orambhāgiyānaṃ saṃyojanānaṃ parikkhayā opapātiko hoti tattha parinibbāyī "
  "anāvattidhammo tasmā lokā.", F.ANAGAMI + END)
S("Idhekacco puggalo āsavānaṃ khayā anāsavaṃ cetovimuttiṃ paññāvimuttiṃ diṭṭheva dhamme sayaṃ abhiññā sacchikatvā "
  "upasampajja viharati.",
  wit("2", "^2-831", "āsavānaṃ khayā anāsavaṃ", f"{W['asava']}တို့ ကုန်ခန်းခြင်းကြောင့် {W['asava']} မရှိသော") and
  f"{IDHA} {W['asava']}တို့ ကုန်ခန်းခြင်းကြောင့် {W['asava']} မရှိသော {W['cetovimuttim']}ကို {W['ditthe_dhamme']} "
  f"{SAYAM} ဝင်စား၍ နေ၏{END}")
S("Idhekacco puggalo tiṇṇaṃ saṃyojanānaṃ parikkhayā rāgadosamohānaṃ tanuttā sakadāgāmī hoti, sakideva imaṃ lokaṃ "
  "āgantvā dukkhassantaṃ karoti.",
  F.SENT["Idhekacco puggalo tiṇṇaṃ saṃyojanānaṃ parikkhayā rāgadosamohānaṃ tanuttā sakadāgāmī hoti, sakideva imaṃ "
         "lokaṃ āgantvā dukkhassantaṃ karoti"] + END)

# ---- ^4-189: learning
for _q, _qm in (("appakaṃ", "နည်း၏"), ("bahukaṃ", "များ၏")):
    S(f"Idhekaccassa puggalassa {_q} sutaṃ hoti {_NAV_P}.",
      f"{IDHA_G} {F.SUTA} ဖြစ်သော {NAVANGA}သည် {_qm}{END}")
_DHA = "အနက်ကို သိ၍၊ တရားကို သိ၍ တရားနှင့် လျော်သော တရားကို ကျင့်သူ"   # atthamaññāya dhammamaññāya dhammānudhamma…
new("dhammānudhammappaṭipanno", "တရားနှင့် လျော်သော တရားကို ကျင့်သူ")
for _q, _qm in (("appakassa", "နည်းသော"), ("bahukassa", "များသော")):
    S(f"So tassa {_q} sutassa na atthamaññāya dhammamaññāya dhammānudhammappaṭipanno hoti.",
      f"{SO} ထို{_qm} {F.SUTA}၏ {_DHA} မဟုတ်{END}")
    S(f"So tassa {_q} sutassa atthamaññāya dhammamaññāya dhammānudhammappaṭipanno hoti.",
      f"{SO} ထို{_qm} {F.SUTA}၏ {_DHA} {COP}{END}")
S("So tassa appakassa sutassa na atthamaññāya dhammamaññāya dhammānudhammappaṭipanno [na dhammamaññāya na "
  "dhammānudhammapaṭipanno (syā.), na dhammamaññāya dhammānudhammappaṭipanno (ka.)] hoti.",
  f"{SO} ထိုနည်းသော {F.SUTA}၏ {_DHA} ⟦0⟧ မဟုတ်{END}")
del SENT5["So tassa appakassa sutassa na atthamaññāya dhammamaññāya dhammānudhammappaṭipanno hoti."]

# ===================================================================================== install the tables
for _k, _v in SENT5.items():
    if _k in F.SENT and F.SENT[_k] != _v:
        raise SystemExit("table conflict with the sample: " + _k[:80])
    F.SENT[_k] = unicodedata.normalize("NFC", _v)
USED = set()
_unit_sample = F.unit_my


def unit5(u):
    if u in SENT5:
        USED.add(u)
    return _unit_sample(u)


F.EXTRA_RULES.insert(0, (re.compile(r".+"), lambda m: F.fill(F.SENT[m[0]], m[0]) if m[0] in SENT5 else None))
F.unit_my = unit5        # units_my() looks unit_my up at call time (coverage of SENT5, in memory only)


# ===================================================================================== generator
def generate(misses=None):
    lines = (PALI / NAME_OUT).read_text(encoding="utf-8-sig").splitlines()
    done = []
    for i, line in enumerate(lines):
        try:
            done.append(F.translate_line(line))
        except F.Miss as e:
            if misses is None:
                print(f"STOP {NAME_OUT} line {i + 1}: {e}\n  {line[:200]}")
                return None
            misses.append(f"{i + 1}: {e}")
            done.append("")
    return unicodedata.normalize("NFC", "\n".join(done).rstrip("\n") + "\n")


if __name__ == "__main__":
    if "--misses" in sys.argv:
        ms = []
        generate(ms)
        print("\n".join(ms) or "no misses")
        print(f"{len(ms)} misses; unused SENT5 keys: {len(set(SENT5) - USED)}")
        for k in sorted(set(SENT5) - USED):
            print("  unused:", k[:150])
        sys.exit(0)
    txt = generate()
    if txt is None:
        sys.exit(1)
    unused = set(SENT5) - USED
    if unused:
        print(f"STOP: {len(unused)} SENT5 keys unused (coverage):")
        for k in sorted(unused):
            print("  ", k[:150])
        sys.exit(1)
    (OUT / NAME_OUT).write_text(txt, encoding="utf-8")
    print(f"wrote {NAME_OUT}: {sum(1 for l in txt.splitlines() if l)} lines, {len(SENT5)} unique sentences, "
          f"{len(NEW)} new strings")
