"""Burmese zero-shot of pi-6 (Yamaka, «အတွဲလိုက် မေးဖြေခြင်း»), group ch10c: Indriyayamaka 10-10 … 10-13
(paccuppannānāgata- and atītānāgatavāra of the uppāda part, the pariññāvāra, the end of the book).

usage: python3 -I -X utf8 make_ch10c.py [chapter ...] [--misses]
Model: make_sample.py (approved sample); the person-lead and pariññā machinery follows make_ch2-02-4-5.py, the
moment / samaṅgī / «yassa cittassa anantarā» phrases make_ch6-8.py (both READ only, never run or imported).
Imports my6_formulas.py unchanged and only EXTENDS its tables in memory (add_subject / PLACES / PART / H / COLO /
FRAMES; who_my wrapped: the module's own parse is tried first, so every group the sample builds comes out as there).
The 22 faculties are read from the FINAL pi-2 rails (^2-219, the pi-2 order). Every other reused value is read /
checked in the FINAL pi-1 … pi-5 rails texts (F.W = witness: stops the run if the text drifts) or marked NEW here
and in notes-ch10c.md. A sentence that no frame / table entry matches stops the run (Miss): nothing is guessed.
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
NAMES_OUT = ["10-10-indriyayamaka.md", "10-11-indriyayamaka.md", "10-12-indriyayamaka.md", "10-13-indriyayamaka.md"]
W, C, END, PE, AND, DAT = F.W, F.C, F.END, F.PE, F.AND, F.DAT
NEW = {}          # NEW strings of this group (Pāli = Burmese), for the notes / check


def new(pali, my):
    NEW.setdefault(pali, my)
    return my


# ===================================================================================== the 22 faculties (pi-2 ^2-219)
IND_H, IND = F.items("2", "^2-219")          # «စွမ်းရည် နှစ်ဆယ့်နှစ်ပါး», {cakkhundriyaṃ: «မျက်စိ၏ စွမ်းရည်», …}
IND_ORDER = list(IND)                       # the pi-1 / pi-2 order
assert len(IND) == 22 and IND_ORDER[0] == "cakkhundriyaṃ" and IND_ORDER[-1] == "aññātāvindriyaṃ"
for _k, _v in IND.items():
    F.add_subject(_k, _v)
W("1", "^1-161", "saddhindriyaṃ hoti", IND["saddhindriyaṃ"], key="saddhindriyaṃ (pi-1)")   # pi-1 agrees


def ind(tok):
    """a faculty in any surface form (…ṃ, …ñca, …nti, …ti) -> its Burmese name."""
    t = tok.strip()
    t = re.sub(r"ñca$", "ṃ", t)
    t = re.sub(r"nti$", "ṃ", t)
    if t[0].isupper():
        t = t[0].lower() + t[1:]
    if t not in IND:
        raise F.Miss("faculty: " + tok)
    return IND[t]


# ===================================================================================== terms read from pi-1 … pi-5
ITTHI = W("2", "^2-219", "itthindriyaṃ", "မိန်းမ", key="itthī")          # «မိန်းမ၏ စွမ်းရည်»
PURISA = W("2", "^2-219", "purisindriyaṃ", "ယောက်ျား", key="purisa")
SOMANASSA = W("2", "^2-219", "somanassindriyaṃ", "ဝမ်းမြောက်မှု", key="somanassa")
UPEKKHA = W("2", "^2-219", "upekkhindriyaṃ", "ဥပေက္ခာ", key="upekkhā")
SADDHA = W("2", "^2-219", "saddhindriyaṃ", "ယုံကြည်မှု", key="saddhā")
NANA = W("1", "^1-147", "ñāṇavippayuttaṃ", "ဉာဏ်", key="ñāṇa")
NANA_VIPP = W("1", "^1-147", "ñāṇavippayuttaṃ", "ဉာဏ်နှင့် ကင်းကွာသော", key="ñāṇavippayutta")
VIPP = NANA_VIPP[len(NANA):]                 # «နှင့် ကင်းကွာသော» (core style rule)
SAMP = "နှင့် ယှဉ်တွဲသော"                    # -sampayutta (core style rule)
W("1", "^1-M2-58", "cittasampayuttā dhammā", "စိတ်နှင့် ယှဉ်တွဲသော", key="-sampayutta")
SAHAGATA = W("1", "^1-147", "somanassasahagataṃ", "ဝမ်းမြောက်မှုနှင့်အတူ", key="somanassa- (with joy)")
CITTA = F.TOPICS["Citta"]                    # «စိတ်»
PACCHIMA = "နောက်ဆုံး"                       # pacchima (sample «နောက်ဆုံး ဘဝ»; ch2-02-4-5 / ch6-8 «နောက်ဆုံး စိတ်»)
SAMANGI = W("2", "^2-809", "kāyaduccaritasamaṅgī", "နှင့် ပြည့်စုံသူ", key="-samaṅgī")
UPPADAK = W("5", "^5-366", "Uppādakkhaṇe", "ဖြစ်ခြင်း ခဏ၌", key="uppādakkhaṇe")
BHANGAK = W("5", "^5-366", "bhaṅgakkhaṇe", "ပြိုပျက်ခြင်း ခဏ၌", key="bhaṅgakkhaṇe")
MOMENT = {"uppādakkhaṇe": UPPADAK, "bhaṅgakkhaṇe": BHANGAK}
VATTAMANE = W("5", "^5-556", "citte vattamāne", "စိတ် ဖြစ်နေစဉ်", key="citte vattamāne")
ANANTARA = W("5", "^5-687", "anantarā", "၏ ချက်ချင်း နောက်၌", key="X-assa anantarā")
NIRODHA_SAM = W("5", "^5-458", "nirodhaṃ samāpajjantassa", "ချုပ်ငြိမ်းခြင်း သမာပတ်ကို ဝင်စားနေသူ",
                key="nirodhasamāpanna")
PLANE = {"kāmāvacara": W("1", "^1-990", "kāmāvacare", "ကာမဘုံ", key="kāmāvacara (plane)"),
         "rūpāvacara": W("1", "^1-990", "rūpāvacare", "သိမ်မွေ့သော ရုပ်ဘုံ", key="rūpāvacara (plane)"),
         "arūpāvacara": W("1", "^1-990", "arūpāvacare", "ရုပ်မရှိသော ဘုံ", key="arūpāvacara (plane)")}
F.PLACES.update(PLANE)
SA = {"cakkhu": "မျက်စိ", "ghāna": "နှာခေါင်း", "sota": "နား", "jivhā": "လျှာ", "kāya": "ကိုယ်"}
for _k, _i in (("cakkhu", "cakkhundriyaṃ"), ("sota", "sotindriyaṃ"), ("ghāna", "ghānindriyaṃ")):
    W("2", "^2-219", _i, SA[_k], key=_k)
HAVE_WITH = f"{F.HAVE}လျက်"                   # sa-X-ka «X ရှိလျက်» (ch3 / ch2-02-4-5)
NOT_HAVE = f"မ{F.HAVE}ဘဲ"                     # a-X-ka «X မရှိဘဲ»
NOT_BE = f"{F.NEGV[F.BE]}ဘဲ"                  # na itthīnaṃ «မိန်းမ မဟုတ်ဘဲ» (NEW, the a-X-ka pattern)
REBORN_FINISH = "ပြန်လည် ဖြစ်ပေါ်ပြီး ပရိနိဗ္ဗာန် ပြုမည့်"      # upapajjitvā parinibbāyissanti (sample GROUP_ATOMS)
assert F.GROUP_ATOMS["ye arūpaṃ upapajjitvā parinibbāyissanti"].endswith(REBORN_FINISH + F.THEM)
AMONG = "အနက်"                               # «… tesaṃ cavantānaṃ» after a relative: «…သူတို့အနက် စုတေဆဲသူတို့»
#                                             (ch2-02-4-5 / ch3 (majority); ch6-8 has «ထဲမှ»)
PAVATTE = "ဘဝ တည်နေစဉ်"                       # pavatte (ch2-02-4-5)
DUTIYA_CITTE = f"ဒုတိယ {VATTAMANE}"            # dutiye citte vattamāne (ch2-02-4-5 / ch6-8)

# pariññāvāra verbs: (positive stem, negative stem)
PVERB = {"parijān": (W("5", "^5-317", "parijānaṃ", "ပိုင်းခြား သိ", key="parijānāti"), "ပိုင်းခြား မသိ"),
         "pajah": (W("5", "^5-317", "pajahaṃ", "ပယ်", key="pajahati"), "မပယ်"),
         "bhāv": (W("5", "^5-339", "anāgāmimaggaṃ bhāvetīti", "ပွားများ", key="bhāveti"), "မပွားများ"),
         "sacchikar": (W("5", "^5-194", "sacchikaroti", "မျက်မှောက်ပြု", key="sacchikaroti"), "မျက်မှောက် မပြု")}
W("4", "^4-17", "na sotāpattiphalaṃ sacchikaroti", "မျက်မှောက် မပြု", key="na sacchikaroti")
W("2", "^2-1029", "agga", "အမြတ်ဆုံး", key="agga")
MAGGA = W("1", "^1-1039", "maggahetukā", "မဂ်", key="magga")
PHALA = W("1", "^1-996", "maggaphalāni", "ဖိုလ်", key="phala")
AGGA = "အမြတ်ဆုံး"
ARAHA = W("4", "^4-M-7", "Arahā", "ရဟန္တာ", key="arahā")
ANAGAMI = W("4", "^4-M-7", "Anāgāmī", "အနာဂါမ်", key="anāgāmī")
ANAGAMIMAGGA = W("5", "^5-339", "anāgāmimaggaṃ", "အနာဂါမိမဂ်", key="anāgāmimagga")
ATTHAMAKA = W("5", "^5-368", "Aṭṭhamakassa puggalassa", "အဋ္ဌမ ပုဂ္ဂိုလ်", key="aṭṭhamaka")
PUTHUJJANA = W("1", "^1-1007", "puthujjano", "ပုထုဇဉ်", key="puthujjana")
PATILABH = W("2", "^2-974", "paṭilabhati", "ရရှိ", key="paṭilabhati")
PUGGALA = F.PUGGALA
YOKE = W("4", "^4-M-8", "Dve puggalā", "ပုဂ္ဂိုလ် နှစ်ယောက်", key="Dve puggalā")[len(PUGGALA) + 1 + len("နှစ်"):]
NUMBER = {"dve": "နှစ်", "tayo": "သုံး", "cattāro": "လေး", "pañca": "ငါး", "cha": "ခြောက်", "satta": "ခုနစ်",
          "aṭṭha": "ရှစ်"}
YO = ("အကြင်သူသည်", "ထိုသူသည်")            # yo … so … (ch2-02-4-5 / ch6-8)

# ===================================================================================== NEW strings of this group
ETENEVA = new("(ye ca purisā / yā ca itthiyo) eteneva bhāvena katici bhave dassetvā parinibbāyissanti",
              "ဤ အဖြစ်ဖြင့်ပင် ဘဝ အချို့ကို ဖြတ်သန်းပြီး ပရိနိဗ္ဗာန် ပြုမည့်")
new("na itthīnaṃ / na purisānaṃ (+ participle)", f"{ITTHI} {NOT_BE} / {PURISA} {NOT_BE}")
new("somanassena / upekkhāya upapajjitvā", f"{SAHAGATA} / {UPEKKHA}နှင့်အတူ ပြန်လည် ဖြစ်ပေါ်ပြီး")
YAM_CITTA, TAM_CITTA = f"အကြင်{CITTA}", f"ထို{CITTA}"   # yassa cittassa … tassa cittassa (ch. 5 correlative)
W("2", "^2-751", "samanantarā", "ချက်ချင်း နောက်၌", key="anantarā (ch2-02-4-5)")
OWN_MIND = "မိမိ စိတ်"                          # yassa cittassa anantarā (persons): ch6-8 «မိမိ စိတ်၏ ချက်ချင်း နောက်၌ …»
new("Dve / Tayo … puggalā (subject)", f"{PUGGALA} နှစ်{YOKE}တို့ / သုံး{YOKE}တို့ … (as ch7a 7-03)")
new("maggasamaṅgino (counted)", f"{MAGGA}{SAMANGI} N{YOKE}")
new("Yo aggaphalaṃ sacchikaroti so / sacchākāsi so", f"{AGGA} {PHALA}ကို {PVERB['sacchikar'][0]}သူသည် / …ပြုခဲ့သူသည်")
new("Anāgāmimaggasamaṅgī", f"{ANAGAMIMAGGA}{SAMANGI}")

# ===================================================================================== persons (pavatti leads)
PART2 = {"upapajjantānaṃ": F.PART["upapajjantānaṃ"][0], "upapajjantīnaṃ": F.PART["upapajjantānaṃ"][0],
         "cavantānaṃ": F.PART["cavantānaṃ"][0], "cavantīnaṃ": F.PART["cavantānaṃ"][0],
         "parinibbantānaṃ": F.PART["parinibbantānaṃ"][0]}
F.PART["upapajjantīnaṃ"] = F.PART["upapajjantānaṃ"]      # feminine forms: same Burmese
F.PART["cavantīnaṃ"] = F.PART["cavantānaṃ"]
UPPAJJANTA = new("uppajjantānaṃ (slip for upapajjantānaṃ, ^6-10-398 «purisānaṃ uppajjantānaṃ»)",
                 F.VERB["uppajj"] + "ဆဲ")
HEADN = {"itthīnaṃ": ITTHI, "purisānaṃ": PURISA, "itthiyo": ITTHI, "purisā": PURISA}
SA_RE = re.compile(r"^(?P<a>sa|a)(?P<k>cakkhu|ghāna|sota|jivhā|kāya)k(?:ānaṃ|ā)$")
GEN_RE = re.compile(r"^(?:(?P<x>ñāṇa|saddhā|somanassa|upekkhā|paññā)(?P<sv>vippayutta|sampayutta))?(?P<p>pacchima)?"
                    r"cittassa$")
XW = {"ñāṇa": NANA, "saddhā": SADDHA, "somanassa": SOMANASSA, "upekkhā": UPEKKHA}
SAMANGI_RE = re.compile(r"^(?:(?P<x>somanassa|upekkhā)sampayutta)?(?P<p>pacchima)?cittasamaṅgīnaṃ$")


def mind_np(x=None, sv=None, p=None):
    """(somanassa, sampayutta, pacchima) -> «ဝမ်းမြောက်မှုနှင့် ယှဉ်တွဲသော နောက်ဆုံး စိတ်»."""
    pre = f"{XW[x]}{SAMP if sv == 'sampayutta' else VIPP} " if x else ""
    return f"{pre}{PACCHIMA + ' ' if p else ''}{CITTA}"


def sa_attr(t):
    m = SA_RE.match(t)
    if not m:
        return None
    return f"{SA[m['k']]} {HAVE_WITH if m['a'] == 'sa' else NOT_HAVE}"


def _acc_places(toks, j):
    keys = []
    while j < len(toks) and F._place_form(toks[j]) and F._place_form(toks[j])[1] == "acc":
        keys.append(F._place_form(toks[j])[0])
        j += 1
    return keys, j


def moment_at(toks, i):
    """a moment at toks[i] -> (Burmese adverbial «… ခဏ၌» / «… ဖြစ်နေစဉ်», next i) or None."""
    tl = toks
    j, pre = i, []
    if j < len(tl) and tl[j] == "pavatte":
        pre.append(PAVATTE)
        j += 1
    if tl[j:j + 3] == ["dutiye", "citte", "vattamāne"] and not pre:
        return DUTIYA_CITTE, j + 3
    # yassa cittassa anantarā X-pacchimacittaṃ uppajjissati tassa cittassa …kkhaṇe
    if tl[j:j + 3] == ["yassa", "cittassa", "anantarā"] and j + 8 <= len(tl) and tl[j + 5:j + 7] == ["tassa", "cittassa"] \
            and tl[j + 7] in MOMENT:
        m = re.fullmatch(r"(?:(?P<x>somanassa|upekkhā)(?P<sv>sampayutta))?pacchimacittaṃ", tl[j + 3])
        if not m:
            raise F.Miss("next mind: " + tl[j + 3])
        v = F.V(toks[j + 4], "cl")
        x = f"{XW[m['x']]}{SAMP} " if m["x"] else ""
        return (f"{YAM_CITTA}{ANANTARA} {x}{PACCHIMA} {CITTA} {v}{C} {TAM_CITTA}၏ {MOMENT[tl[j + 7]]}", j + 8)
    if j + 1 < len(tl) and tl[j + 1] in MOMENT:
        m = GEN_RE.match(tl[j])
        if m:
            return " ".join(pre + [f"{mind_np(m['x'], m['sv'], m['p'])}၏ {MOMENT[tl[j + 1]]}"]), j + 2
    return None


def rel_at(toks, i):
    """(ye|yā) ca [purisā|itthiyo] [sa-X-kā] [somanassena|upekkhāya|places-acc] upapajjitvā parinibbāyissanti /
    (ye|yā) ca (purisā|itthiyo) eteneva bhāvena katici bhave dassetvā parinibbāyissanti -> (Burmese, next i)."""
    tl = toks
    if tl[i:i + 1] not in (["ye"], ["yā"]) or tl[i + 1:i + 2] != ["ca"]:
        return None
    j = i + 2
    head = F.THEM
    if j < len(tl) and tl[j] in HEADN:
        head = " " + HEADN[tl[j]] + "တို့"
        j += 1
    if tl[j:j + 6] == ["eteneva", "bhāvena", "katici", "bhave", "dassetvā", "parinibbāyissanti"]:
        return f"{ETENEVA}{head}", j + 6
    pre = []
    if j < len(tl) and sa_attr(tl[j]):
        pre.append(sa_attr(tl[j]))
        j += 1
    if j < len(tl) and tl[j] in ("somanassena", "upekkhāya"):
        pre.append(SAHAGATA if tl[j] == "somanassena" else f"{UPEKKHA}နှင့်အတူ")
        j += 1
    keys, j = _acc_places(tl, j)
    if keys:
        pre.append(F._join_places(keys) + F.LOC)
    if tl[j:j + 2] != ["upapajjitvā", "parinibbāyissanti"]:
        raise F.Miss("relative: " + " ".join(toks[i:]))
    return " ".join(pre + [REBORN_FINISH]) + head, j + 2


def person_at(toks, i):
    """one person phrase at toks[i] that the module does not build -> (Burmese «…သူတို့», next i) or None."""
    tl = toks
    t = tl[i]
    if t == "nirodhasamāpannānaṃ":
        return f"{NIRODHA_SAM}တို့", i + 1
    m = SAMANGI_RE.match(t)
    if m:
        return f"{mind_np(m['x'], 'sampayutta' if m['x'] else None, m['p'])}{SAMANGI}တို့", i + 1
    if tl[i:i + 3] == ["yassa", "cittassa", "anantarā"] and i + 5 <= len(tl) and tl[i + 5:i + 6] != ["tassa"]:
        m = re.fullmatch(r"(?:(?P<x>somanassa|upekkhā)(?P<sv>sampayutta))?pacchimacittaṃ", tl[i + 3])
        if not m:
            raise F.Miss("own mind: " + tl[i + 3])
        x = f"{XW[m['x']]}{SAMP} " if m["x"] else ""
        return f"{OWN_MIND}{ANANTARA} {x}{PACCHIMA} {CITTA} {F.V(toks[i + 4], 'attr')}{F.THEM}", i + 5
    r = rel_at(tl, i)
    if r:
        return r
    # pacchimabhavikānaṃ [sa-X-kānaṃ] (itthīnaṃ upapajjantīnaṃ | purisānaṃ upapajjantānaṃ | uppajjantānaṃ)
    if t == "pacchimabhavikānaṃ":
        j, pre = i + 1, ""
        if j < len(tl) and sa_attr(tl[j]):
            pre = sa_attr(tl[j]) + " "
            j += 1
        if tl[j:j + 2] in (["itthīnaṃ", "upapajjantīnaṃ"], ["purisānaṃ", "upapajjantānaṃ"], ["purisānaṃ",
                                                                                               "uppajjantānaṃ"]):
            verb = UPPAJJANTA if tl[j + 1] == "uppajjantānaṃ" else PART2[tl[j + 1]]
            return f"{pre}{verb} {F.PACCHIMA}သော {HEADN[tl[j]]}တို့", j + 2
        if pre and tl[j:j + 1] == ["upapajjantānaṃ"]:
            return f"{pre}{PART2['upapajjantānaṃ']} {F.PACCHIMA}{F.THEM}", j + 1
        return None
    # [na] itthīnaṃ / purisānaṃ / sa-X-kānaṃ / a-X-kānaṃ [places-acc] participle
    j, pre = i, ""
    if t == "na" and i + 1 < len(tl) and tl[i + 1] in HEADN:
        pre = f"{HEADN[tl[i + 1]]} {NOT_BE} "
        j = i + 2
    elif sa_attr(t):
        pre = sa_attr(t) + " "
        j = i + 1
    else:
        return None
    keys, j = _acc_places(tl, j)
    if j < len(tl) and tl[j] in PART2:
        loc = (F._join_places(keys) + F.PART[tl[j]][1] + " ") if keys else ""
        return f"{pre}{loc}{PART2[tl[j]]}{F.THEM}", j + 1
    raise F.Miss("person with attribute: " + " ".join(toks[i:]))


def _is_module_tok(t):
    return t in ("sabbesaṃ", "itaresaṃ", "pacchimabhavikānaṃ") or t in F.PART or bool(F._place_form(t))


def _person_here(toks, j):
    """True when this group's own person phrase starts at toks[j] (it ends a run of module tokens)."""
    try:
        return person_at(toks, j) is not None
    except F.Miss:
        return False


def lead_units(toks):
    """tokens (lower case, no brackets) -> [(kind, Burmese)]: P person, M moment, A flag «sabbesaṃ» before a moment."""
    units, i = [], 0
    while i < len(toks):
        t = toks[i]
        mo = moment_at(toks, i)
        if mo:
            units.append(("M", mo[0]))
            i = mo[1]
            continue
        if t == "sabbesaṃ" and moment_at(toks, i + 1):
            units.append(("A", ""))
            i += 1
            continue
        if t in ("tesaṃ", "tāsaṃ") and i + 1 < len(toks) and toks[i + 1] in PART2 and units and units[-1][0] == "P":
            units[-1] = ("P", units[-1][1] + f"{AMONG} {PART2[toks[i + 1]]}{F.THEM}")
            i += 2
            continue
        r = person_at(toks, i)
        if r:
            units.append(("P", r[0]))
            i = r[1]
            continue
        if _is_module_tok(t):
            j = i + 1
            while j < len(toks) and _is_module_tok(toks[j]) and not moment_at(toks, j) \
                    and not (toks[j] == "sabbesaṃ" and moment_at(toks, j + 1)) and not _person_here(toks, j):
                j += 1
            run = toks[i:j]
            while run:
                units.append(("P", F._one_group(run)))
            i = j
            continue
        raise F.Miss("lead token: " + t + " in " + " ".join(toks))
    return units


def join_units(units):
    """The ch2-02-4-5 / ch. 5 lead style (also the sibling ch. 10 groups ch9-10a / ch10b): a moment is its own
    adverbial unit «M» (units joined with «၊ »), a final one followed by «ထိုသူတို့အား»; sabbesaṃ before a moment
    «သူ အားလုံးတို့၏ M»; a lead that is ONE moment alone «M ရှိသူတို့» (8 / 6-02 usage). Person units are joined as
    the module joins groups («A၊ Bနှင့် C»). -> (Burmese, last kind)."""
    if len(units) == 1 and units[0][0] == "M":
        return f"{units[0][1]} {F.HAS}{F.THEM}", "P"
    segs, run, k, last = [], [], 0, None
    while k < len(units):
        kind, txt = units[k]
        if kind == "P":
            run.append(txt)
            last = "P"
        else:
            if run:
                segs.append(_join_p(run))
                run = []
            if kind == "A":
                k += 1
                txt = f"{ALL_OF_GEN}{units[k][1]}"
            segs.append(txt)
            last = "M"
        k += 1
    if run:
        segs.append(_join_p(run))
    return f"{C} ".join(segs), last


ALL_OF_GEN = f"{F.ALL_OF}၏ "                 # sabbesaṃ before a moment (ch2-02-4-5 / 5-01)


def _join_p(parts):
    return parts[0] if len(parts) == 1 else f"{C} ".join(parts[:-1]) + f"{AND} " + parts[-1]


# identical Pāli in the finished groups with another lead style: their Burmese (6-02, 7 occurrences; 10-11 ^6-10-402 / 403)
F.GROUP_ATOMS["pacchimacittassa bhaṅgakkhaṇe asaññasattānaṃ"] = f"{PACCHIMA} {CITTA}၏ {BHANGAK} {F.HAS}{F.THEM}{AND} " \
                                                               f"{F.SATTA_ASANNA}တို့"
PROR = r"(?:tesaṃ tattha|tāsaṃ tattha|tesaṃ|tāsaṃ|tattha)"
PRO = {"tesaṃ": F.PRO["tesaṃ"], "tāsaṃ": F.PRO["tesaṃ"], "tesaṃ tattha": F.PRO["tesaṃ tattha"],
       "tāsaṃ tattha": F.PRO["tesaṃ tattha"], "tattha": F.PRO["tattha"]}
_who_module = F.who_my


def who_my(who, pro):
    """The module's who_my first (pure person runs / places, identical to the sample); else the lead parser."""
    pro0 = pro.replace("tāsaṃ", "tesaṃ")
    try:
        return _who_module(who, pro0)
    except F.Miss:
        pass
    var = re.findall(r" ?(⟦\d+⟧)", who)
    who = re.sub(r" ?⟦\d+⟧", "", who)
    toks = [t[0].lower() + t[1:] for t in who.replace(",", "").split()]
    if pro0 == "tattha":
        raise F.Miss("lead: tattha after persons: " + who)
    out, last = join_units(lead_units(toks))
    out += DAT if last == "P" else " " + F.PRO["tesaṃ"]
    out += "".join(" " + v for v in var)
    return out + (" " + F.FT["tattha"] if pro0 == "tesaṃ tattha" else "")


F.who_my = who_my

# ===================================================================================== pavatti frames (this group)
VB = F.VB
A_BUT2 = re.compile(rf"^(?P<who>.+?) (?P<pro>{PROR}) (?P<x>\S+) (?P<v1>{VB}),? no ca (?P<pro2>{PROR}) (?P<y>\S+) "
                    rf"(?P<v2>{VB})\.$")
A_BOTH2 = re.compile(rf"^(?P<who>.+?) (?P<pro>{PROR}) (?P<x>\S+?ñca) (?P<v1>{VB}) (?P<y>\S+?ñca) (?P<v2>{VB})\.$")


def a_but2(m):
    root2, tense2, neg2 = F.pali_verb(m["v2"])
    v2m = F.not_so(root2, tense2) if neg2 else F.my_verb(root2, tense2, True)
    return (f"{who_my(m['who'], m['pro'])} {ind(m['x'])} {F.V(m['v1'])}{C} {F.BUT} {PRO[m['pro2']]} {ind(m['y'])} "
            f"{v2m}{END}")


def a_both2(m):
    return f"{who_my(m['who'], m['pro'])} {ind(m['x'])}လည်း {F.V(m['v1'])}{C} {ind(m['y'])}လည်း {F.V(m['v2'])}{END}"


NOTE_RE = re.compile(r"^\((?P<x>\w+?)mūlakaṃ\)(?P<dot>\.?)$")


def note_my(m):
    """(Cakkhundriyamūlakaṃ) = «(မျက်စိ၏ စွမ်းရည်ကို အခြေခံ၍)» (the ch. 3 pattern «(Xကို အခြေခံ၍)»)."""
    x = m["x"][0].lower() + m["x"][1:] + "ṃ"
    return f"({ind(x)}{F.BASED})" + (END if m["dot"] else "")


# ===================================================================================== pariññāvāra
PV_END = [("issanti", "fut", True), ("essanti", "fut", True), ("issati", "fut", False), ("essati", "fut", False),
          ("ittha", "past", None), ("ākāsi", "past", False), ("onti", "pres", True), ("oti", "pres", False),
          ("enti", "pres", True), ("eti", "pres", False), ("anti", "pres", True), ("āti", "pres", False),
          ("ati", "pres", False)]
PVB = r"(?:na |nap|n)?(?:parijān|pajah|ppajah|pajjah|bhāv|bhav|sacchikar|sacchāk)\w*"
PSLIP = {"nappajjahittha": "nappajahittha",          # ^6-10-480 slip (double j)
         "bhavissanti": "bhāvessanti",               # slip: «bhavissanti» (will be) with an object; read bhāvessanti
         "sacchākāsi": "sacchikarākāsi"}             # aorist of sacchikaroti (past)


def pali_pverb(w):
    """'parijānāti' / 'na bhāvitthāti' / 'nappajahissanti' / 'sacchākāsi' -> (root, tense, neg, plural or None)."""
    w = w.strip()
    w = PSLIP.get(w, w)
    neg = False
    if w.startswith("na "):
        neg, w = True, w[3:]
    if w.startswith("nappajah"):
        neg, w = True, w[3:]
    w = PSLIP.get(w, w)
    w = re.sub(r"īti$", "i", w)
    w = re.sub(r"itthāti$", "ittha", w)
    for root in PVERB:
        if w.startswith(root):
            rest = w[len(root):]
            for e, tense, pl in PV_END:
                if rest == e:
                    return root, tense, neg, pl
    raise F.Miss("pali_pverb: " + w)


def p_verb(root, tense, neg=False, form="stmt", pl=False):
    """the four pariññā verbs in every tense / polarity (forms as F.my_verb; the negative stem of each verb)."""
    stem = PVERB[root][1 if neg else 0]
    fut = tense == "fut"
    ko_ = "ကြ" if pl else ""
    v = stem + ((ko_ + F.TENSE_MY[tense]) if fut else (F.TENSE_MY[tense] + ko_))
    if form == "stmt":
        return v if (neg or fut) else v + "သည်"
    if form == "cl":
        return v if (neg or fut) else v + "၏"
    if form == "q":
        return v + ("လော" if fut else "သလော")
    if form == "notso":
        return v + ("" if fut else "သည်") + F.NOT_SO
    if form == "rel":                                   # «… ပြုသူ» / «… ပြုခဲ့သူ» (Yo … so)
        return v + "သူ"
    raise ValueError(form)


def PV(w, form="stmt", pl=False):
    root, tense, neg, p = pali_pverb(w)
    return p_verb(root, tense, neg, form, pl)


def obj(tok):
    return ind(tok) + "ကို"


# pariññā subjects: Pāli (with ⟦n⟧ for a variant bracket) -> (Burmese subject, plural)
_LEAVE = {"aggamaggasamaṅgiñca": f"{AGGA} {MAGGA}{SAMANGI}", "anāgāmimaggasamaṅgiñca": f"{ANAGAMIMAGGA}{SAMANGI}",
          "arahantañca": ARAHA, "aṭṭhamakañca": ATTHAMAKA}
W("5", "^5-546", "arahantānaṃ", "ရဟန္တာ", key="arahanta-")
SINGLE = {"arahā": ARAHA, "aggamaggasamaṅgī": f"{AGGA} {MAGGA}{SAMANGI}",
          "anāgāmimaggasamaṅgī": f"{ANAGAMIMAGGA}{SAMANGI}", "anāgāmimaggasamaṅgi": f"{ANAGAMIMAGGA}{SAMANGI}",
          "aṭṭhamako": ATTHAMAKA, "anāgāmī": ANAGAMI}
GET_PATH = f"{MAGGA}ကို {PATILABH}မည့်"
NOGET_PATH = f"{MAGGA}ကို {F.NEG}{PATILABH}မည့်"


def counted(n, noun):
    return f"{noun} {NUMBER[n.lower()]}{YOKE}"


def p_who(s):
    """a pariññā subject -> (Burmese, plural, variant placeholders); a variant goes after «…သည်» (the sample:
    after «…အား»), in a ṭhapetvā group after «…ကို»."""
    s = s.strip()
    var = " ".join(re.findall(r"⟦\d+⟧", s))
    s0 = re.sub(r" ?⟦\d+⟧", "", s)
    tl = s0[0].lower() + s0[1:]
    if tl in SINGLE:
        return SINGLE[tl], False, var
    m = re.fullmatch(r"(?P<n>dve|tayo|cattāro|pañca|cha|satta|aṭṭha) (?:(?P<p>puggalā)|maggasamaṅgino)", tl)
    if m:
        noun = PUGGALA if m["p"] else f"{MAGGA}{SAMANGI}"
        return counted(m["n"], noun) + "တို့", True, var      # «ပုဂ္ဂိုလ် နှစ်ယောက်တို့သည်» (as ch7a, 7-03)
    m = re.fullmatch(r"ye puthujjanā maggaṃ (?P<na>na )?paṭilabhissanti te", tl)
    if m:
        return f"{NOGET_PATH if m['na'] else GET_PATH} {PUTHUJJANA}တို့", True, var
    m = re.fullmatch(r"yo aggaphalaṃ (?P<v>sacchikaroti|sacchākāsi) so", tl)
    if m:
        return f"{AGGA} {PHALA}ကို {PV(m['v'], 'rel')}", False, var
    m = re.fullmatch(r"(?P<l>.+?) ṭhapetvā avasesā puggalā", tl)
    if m:
        left = m["l"]
        parts = []
        mm = re.fullmatch(r"(?P<n>dve|tayo|cattāro) maggasamaṅgino(?P<ca> ca)?(?: (?P<r>.+))?", left)
        if mm:
            parts.append(counted(mm["n"], f"{MAGGA}{SAMANGI}"))
            rest = (mm["r"] or "").split()
        else:
            rest = left.split()
        for w in rest:
            if w not in _LEAVE:
                raise F.Miss("ṭhapetvā: " + left)
            parts.append(_LEAVE[w])
        lv = f"{AND} ".join(parts)
        return f"{lv}ကို {var + ' ' if var else ''}{F.THAPETVA}{C} {F.AVASESA} {PUGGALA}တို့", True, ""
    raise F.Miss("pariññā person: " + s)


Q_PAR = re.compile(rf"^(?P<vp>[Yy]o vā pana|[Yy]o) (?P<x>\S+) (?P<v1>{PVB}) so (?P<y>\S+) (?P<v2>{PVB})[?.]$")
A_PAR_BUT = re.compile(rf"^(?P<who>.+?) (?P<x>\S+) (?P<v1>{PVB}),? no ca (?P<y>\S+) (?P<v2>{PVB})\.$")
A_PAR_BOTH = re.compile(rf"^(?P<who>.+?) (?P<x>\S+?ñca) (?P<v1>{PVB}) (?P<y>\S+?ñca) (?P<v2>{PVB})\.$")
Q_HALF1 = re.compile(rf"^(?P<vp>[Yy]o vā pana|[Yy]o) (?P<x>\S+) (?P<v1>{PVB})\.$")      # slip ^6-10-477 «… bhāvessati.»
Q_HALF2 = re.compile(rf"^So (?P<y>\S+) (?P<v2>{PVB})\?$")


def but_my(who, x, v1, y, v2):
    W_, pl, var = p_who(who)
    r2, t2, n2, _ = pali_pverb(v2)
    v2m = p_verb(r2, t2, True, "notso" if n2 else "stmt", pl)
    return f"{W_}သည်{' ' + var if var else ''} {obj(x)} {PV(v1, pl=pl)}{C} {F.BUT} {obj(y)} {v2m}{END}"


def both_my(who, x, v1, y, v2):
    W_, pl, var = p_who(who)
    return f"{W_}သည်{' ' + var if var else ''} {obj(x)}လည်း {PV(v1, pl=pl)}{C} {obj(y)}လည်း {PV(v2, pl=pl)}{END}"


def pariñña_sentence(s):
    m = Q_PAR.match(s)
    if m:
        pre = F.VA_PANA + " " if "vā pana" in m["vp"] else ""
        return f"{pre}{YO[0]} {obj(m['x'])} {PV(m['v1'], 'cl')}{C} {YO[1]} {obj(m['y'])} {PV(m['v2'], 'q')}{END}"
    m = Q_HALF1.match(s)
    if m:
        pre = F.VA_PANA + " " if "vā pana" in m["vp"] else ""
        return f"{pre}{YO[0]} {obj(m['x'])} {PV(m['v1'], 'stmt')}{END}"
    m = Q_HALF2.match(s)
    if m:
        return f"{YO[1]} {obj(m['y'])} {PV(m['v2'], 'q')}{END}"
    m = A_PAR_BOTH.match(s)
    if m and re.search(PVB, m["who"]) is None or (m and m["who"].lower().startswith("yo aggaphalaṃ")):
        return both_my(m["who"], m["x"], m["v1"], m["y"], m["v2"])
    m = A_PAR_BUT.match(s)
    if m:
        try:
            return but_my(m["who"], m["x"], m["v1"], m["y"], m["v2"])
        except F.Miss:
            mm = re.fullmatch(rf"^(?P<who>.+? so) (?P<x>\S+) (?P<v1>{PVB}),? no ca (?P<y>\S+) (?P<v2>{PVB})\.$", s)
            if mm:
                return but_my(mm["who"], mm["x"], mm["v1"], mm["y"], mm["v2"])
            raise
    return None


def ch10_sentence(s):
    if s in SENT:
        return SENT[s]
    m = NOTE_RE.match(s)
    if m:
        return note_my(m)
    m = A_BUT2.match(s)
    if m:
        return a_but2(m)
    m = A_BOTH2.match(s)
    if m:
        return a_both2(m)
    if re.search(r"\b(?:yo|Yo|So)\b|parijān|pajah|bhāv|sacchi|sacchā", s):
        return pariñña_sentence(s)
    return None


SENT = {}          # whole sentences that no frame builds (slips), Pāli -> Burmese; filled below
F.FRAMES.insert(0, ch10_sentence)

# ===================================================================================== «…pe…» lines
FR_FIRST = re.compile(rf"^{F.CLR} (?P<x>\S+)(?: (?P<v1>{VB}) (?P<ft>tassa tattha|tassa|tattha) (?P<y>\S+))?$")
FR_LAST = re.compile(rf"^(?P<y>\S+) (?P<v2>{VB})[?.]$")
FR_LAST2 = re.compile(rf"^(?P<x>\S+) (?P<v1>{VB}) (?P<ft>tassa tattha|tassa|tattha) (?P<y>\S+) (?P<v2>{VB})[?.]$")


def fragment(t):
    """one piece of a «…pe…» line."""
    t0 = t.strip()
    if not t0:
        return ""
    if t0 in ("?", "."):
        return END
    parts = F.SPLIT.split(t0)
    if len(parts) > 1:
        return " ".join(fragment(p) for p in parts)
    m = FR_FIRST.match(t0)
    if m:
        c = m["cl"].lower()
        pre = F.VA_PANA + " " if " vā pana" in c else ""
        out = f"{pre}{F.CL[c.replace(' vā pana', '')][0]} {ind(m['x'])}"
        if m["v1"]:
            out += f" {F.V(m['v1'], 'cl')}{C} {F.FT[m['ft']]} {ind(m['y'])}"
        return out
    m = FR_LAST2.match(t0)
    if m:
        return f"{ind(m['x'])} {F.V(m['v1'], 'cl')}{C} {F.FT[m['ft']]} {ind(m['y'])} {F.V(m['v2'], 'q')}{END}"
    m = FR_LAST.match(t0)
    if m:
        return f"{ind(m['y'])} {F.V(m['v2'], 'q')}{END}"
    if re.fullmatch(r"\w+ndriyaṃ|\w+indriyaṃ", t0):
        return ind(t0)
    return F.sentence_my(t0)


def pe_line(s):
    s = s.replace("…pe…", PE).replace("…Pe…", PE)
    out = []
    for p in s.split(PE):
        q = fragment(p)
        lead = " " if p.startswith(" ") and q and q != END else ""
        out.append(lead + q)
    return PE.join(out)


_body_my0 = F.body_my


def body_my(line):
    if line in F.COLO or line in F.LINES:
        return _body_my0(line)
    if "…" in line:
        return pe_line(line)
    return _body_my0(line)


F.body_my = body_my

# ===================================================================================== headings and colophons
PARINNA = W("4", "^4-130", "pariññaṃ", "ပိုင်းခြား သိခြင်း", key="pariññā")
H_NEW = {"Pariññāvāro": F.vara(PARINNA)}
F.H.update(H_NEW)
BOOK = new("Yamakapakaraṇaṃ niṭṭhitaṃ.", f"{F.quoted(F.TITLE)} ကျမ်း ပြီးဆုံးပြီ{END}")
W("2", "^2-1044", "Vibhaṅgapakaraṇaṃ niṭṭhitaṃ", "“ခွဲခြမ်းစိတ်ဖြာခြင်း” ကျမ်း ပြီးဆုံးပြီ။", key="Xpakaraṇaṃ niṭṭhitaṃ.")
COLO_NEW = {
    "Pavattivāro niṭṭhito.": F.finished(F.vara(F.PAVATTI)),        # as 2-02 / 3-06 / 5-03
    "Pariññāvāro.": F.vara(PARINNA) + END,                           # as 2-02 / 5-03
    "Yamakapakaraṇaṃ niṭṭhitaṃ.": BOOK,                              # pi-1 … pi-5 book colophon pattern
}
F.COLO.update(COLO_NEW)


# ===================================================================================== source slips (as written)
SLIP_RAW = {}


def add_slip(pali, parts):
    """pali: a sentence of the source with a missing «.»; parts: the sentences it is read as."""
    SLIP_RAW[pali] = parts


# ^6-10-393 «… na uppajjissati pacchimacittassa bhaṅgakkhaṇe …» (no «.»)
add_slip("Sabbesaṃ cittassa bhaṅgakkhaṇe ñāṇavippayuttacittassa uppādakkhaṇe nirodhasamāpannānaṃ asaññasattānaṃ tesaṃ "
         "paññindriyaṃ na uppajjati, no ca tesaṃ manindriyaṃ na uppajjissati pacchimacittassa bhaṅgakkhaṇe tesaṃ "
         "paññindriyañca na uppajjati manindriyañca na uppajjissati.",
         ["Sabbesaṃ cittassa bhaṅgakkhaṇe ñāṇavippayuttacittassa uppādakkhaṇe nirodhasamāpannānaṃ asaññasattānaṃ "
          "tesaṃ paññindriyaṃ na uppajjati, no ca tesaṃ manindriyaṃ na uppajjissati.",
          "Pacchimacittassa bhaṅgakkhaṇe tesaṃ paññindriyañca na uppajjati manindriyañca na uppajjissati."])


# ^6-10-452 (10-13) «… bhāvessanti no ca … pajahissanti, pañca puggalā … bhavissanti …» (no «.»; «bhavissanti»)
add_slip("Dve puggalā aññindriyaṃ bhāvessanti no ca domanassindriyaṃ pajahissanti, pañca puggalā aññindriyañca "
         "bhavissanti domanassindriyañca pajahissanti.",
         ["Dve puggalā aññindriyaṃ bhāvessanti, no ca domanassindriyaṃ pajahissanti.",
          "Pañca puggalā aññindriyañca bhavissanti domanassindriyañca pajahissanti."])
# ^6-10-468 «… no ca domanassindriyaṃ pajahanti anāgāmimaggasamaṅgi aññindriyañca bhāvessanti, domanassindriyañca …»
add_slip("Cha puggalā aññindriyaṃ bhāvessanti, no ca domanassindriyaṃ pajahanti anāgāmimaggasamaṅgi aññindriyañca "
         "bhāvessanti, domanassindriyañca pajahanti.",
         ["Cha puggalā aññindriyaṃ bhāvessanti, no ca domanassindriyaṃ pajahanti.",
          "Anāgāmimaggasamaṅgi aññindriyañca bhāvessanti domanassindriyañca pajahanti."])


def resolve_slips():
    for k, parts in SLIP_RAW.items():
        SENT[k] = " ".join(F.sentence_my(p) for p in parts)


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
    if not hm and not F.strip_id(m).rstrip().endswith(("။", "…", "။)", ")")) and F.strip_id(p).rstrip()[-1:] in ".?":
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
        except (F.Miss, KeyError, IndexError, AttributeError, TypeError, ValueError) as ex:
            n += 1
            print(f"{name}:{i} {type(ex).__name__} {ex}")
    return n


resolve_slips()

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
