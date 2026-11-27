"""Burmese zero-shot of pi-6 ch. 10 (Indriyayamaka, «စွမ်းရည်များကို အတွဲလိုက် မေးဖြေခြင်း»), group ch10b:
10-05 … 10-09-indriyayamaka (pavattivāra, uppādavāra: atīta, anāgata, paccuppannātīta, paccuppannānāgata).

usage: python3 -I -X utf8 make_ch10b.py [10-05 10-06 …] [--misses] [--who]   (no chapter = all five)
Imports my6_formulas (READ ONLY: its tables are extended IN MEMORY here, never edited on disk). Models: make_sample.py,
make_ch3.py (attributes «X ရှိလျက် / X မရှိဘဲ», the «…pe…» fragment engine, notes), make_ch2-02-4-5.py (the lead
parser: person groups, moments, relative clauses; units joined «၊ », a final moment + «ထိုသူတို့အား») and
make_ch6-8.py (a lead that is one moment alone: «… ခဏ၌ ရှိသူတို့အား», 8-cittayamaka); functions copied, never run.
Every line comes from the Pāli through the module frames plus the tables / frames of this script:
  * the 22 faculties: pi-2 ^2-219 list (F.items, read at import), «X၏ စွမ်းရည်»;
  * persons: sa-/a-X-ka (ch. 3), sahetuka, ñāṇasampayutta, somanassena / upekkhāya, itthī / purisa as the head noun,
    na itthīnaṃ / na purisānaṃ, upapajjantīnaṃ, itarāsaṃ, tāsaṃ, relative clauses «ye / yā (ca) …
    parinibbāyissanti», named persons (pacchimacittasamaṅgī, nirodhasamāpanna), moments (… cittassa
    uppāda- / bhaṅgakkhaṇe, the «yassa cittassa anantarā … tassa cittassa …» correlative), places;
  * the pavatti frames with «tāsaṃ» and «X-ñca … Y-ñca …»; the «…pe…» fragments; the notes «(Xmūlakaṃ)».
A sentence that nothing matches raises F.Miss: nothing is guessed. A chapter is written only when every line passes
line_check. --misses lists unmatched lines and writes nothing; --who lists the leads with their Burmese.
New strings: NEW (logged in notes-ch10b.md).
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
NAMES_OUT = [f"10-0{i}-indriyayamaka.md" for i in range(5, 10)]
W = F.W
C, END, PE, AND, DAT = F.C, F.END, F.PE, F.AND, F.DAT
ALSO = "လည်း"
NEW = {}          # every new string of this script: Pāli -> Burmese (for the notes and the check)


def new(pali, my):
    NEW.setdefault(pali, my)
    return my


# ===================================================================================== the 22 faculties (pi-2 ^2-219)
IND_H, IND = F.items("2", "^2-219")         # «စွမ်းရည် နှစ်ဆယ့်နှစ်ပါး», {cakkhundriyaṃ: «မျက်စိ၏ စွမ်းရည်», …}
INDRIYA = W("1", "^1-1", "indriy", "စွမ်းရည်", key="indriya")
if len(IND) != 22:
    raise SystemExit("faculty list: %d" % len(IND))
for k, v in IND.items():
    F.add_subject(k, v)                       # pavattivāra subjects (Pāli nominative, pi-2 spelling)
# the source spelling of the faculties used in the Yamaka must be the pi-2 spelling (checked: every faculty word of my
# chapters is a key of IND; see faculty_words() in check_ch10b.py)

# ===================================================================================== places and persons
F.PLACES["kāmāvacara"] = "ကာမဘုံ"                     # as ch. 3 (style core plane names)
F.PLACES["rūpāvacara"] = "သိမ်မွေ့သော ရုပ်ဘုံ"
F.PLACES["arūpāvacara"] = F.PLACES["arūpa"]
W("1", "^1-M2-93", "kāmāvacarā", "ကာမဘုံ", key="kāmāvacara (place)")
W("1", "^1-M2-94", "rūpāvacarā", "သိမ်မွေ့သော ရုပ်ဘုံ", key="rūpāvacara (place)")
W("1", "^1-M2-95", "arūpāvacarā", "ရုပ်မရှိသော ဘုံ", key="arūpāvacara (place)")
F.PART["upapajjantīnaṃ"] = F.PART["upapajjantānaṃ"]   # feminine participle (itthīnaṃ … upapajjantīnaṃ): same Burmese

CITTA = W("1", "^1-6", "cittaṃ", "စိတ်", key="citta")
SOMANASSA = W("1", "^1-1", "somanassasahagataṃ", "ဝမ်းမြောက်မှု", key="somanassa")
UPEKKHA = W("2", "^2-767", "Upekkhāsampayuttā", "ဥပေက္ခာ", key="upekkhā")
SADDHA = W("2", "^2-219", "saddhindriyaṃ", "ယုံကြည်မှု", key="saddhā")
NANA = W("1", "^1-1", "ñāṇasampayuttaṃ", "ဉာဏ်", key="ñāṇa")
SAMP = W("1", "^1-1", "ñāṇasampayuttaṃ", "ဉာဏ်နှင့် ယှဉ်တွဲသော", key="-sampayutta")[len(NANA):]   # «နှင့် ယှဉ်တွဲသော»
VIPP = W("2", "^2-767", "upekkhāvippayuttā", "ဥပေက္ခာနှင့် ကင်းကွာသော", key="-vippayutta")[len(UPEKKHA):]
ITTHI = W("2", "^2-219", "itthindriyaṃ", "မိန်းမ", key="itthī")
PURISA = W("2", "^2-219", "purisindriyaṃ", "ယောက်ျား", key="purisa")
HETU_R = W("1", "^1-M2-2", "sahetukā dhammā", "အမြစ်", key="hetu (in sahetuka)")
WITH, WITHOUT = "ရှိလျက်", "မရှိဘဲ"           # sa-X-ka / a-X-ka (ch. 3)
# somanassena / upekkhāya upapajjati (reborn «together with» joy / equanimity): «…နှင့်အတူ» (pi-1 sahagata
# «ဝမ်းမြောက်မှုနှင့်အတူ ဖြစ်သော» ^1-1, «ဥပေက္ခာနှင့်အတူ ဖြစ်သော» ^1-M1-7; as the 10-01 … 10-04 and 10-10 … 10-13 agents)
INSTR = W("1", "^1-1", "somanassasahagataṃ", "ဝမ်းမြောက်မှုနှင့်အတူ", key="somanassena (with joy)")[len(SOMANASSA):]
W("1", "^1-M1-7", "upekkhāsahagatā", UPEKKHA + INSTR, key="upekkhāya (with equanimity)")
NOT_BEING = "မဟုတ်ဘဲ"                         # na itthīnaṃ «မိန်းမ မဟုတ်ဘဲ»
QUAL = {"somanassa": SOMANASSA, "upekkhā": UPEKKHA, "saddhā": SADDHA, "ñāṇa": NANA}
# person attributes (gen. pl. / instr.) before the place and the participle -> Burmese phrase
ATTR = {
    "sacakkhukānaṃ": new("sacakkhuka", f"မျက်စိ {WITH}"), "acakkhukānaṃ": new("acakkhuka", f"မျက်စိ {WITHOUT}"),
    "sasotakānaṃ": f"နား {WITH}", "asotakānaṃ": f"နား {WITHOUT}",
    "saghānakānaṃ": new("saghānaka", f"နှာခေါင်း {WITH}"), "aghānakānaṃ": new("aghānaka", f"နှာခေါင်း {WITHOUT}"),
    "sahetukānaṃ": new("sahetukānaṃ (persons)", f"{HETU_R} {WITH}"),
    "ahetukānaṃ": new("ahetukānaṃ (persons)", f"{HETU_R} {WITHOUT}"),
    "ñāṇasampayuttānaṃ": new("ñāṇasampayuttānaṃ (persons)", f"{NANA}{SAMP[:-len('သော')]}လျက်"),
    "ñāṇavippayuttānaṃ": new("ñāṇavippayuttānaṃ (persons)", f"{NANA}{VIPP[:-len('သော')]}လျက်"),
    "somanassena": new("somanassena (reborn with joy)", f"{SOMANASSA}{INSTR}"),
    "upekkhāya": new("upekkhāya (reborn with equanimity)", f"{UPEKKHA}{INSTR}"),
}
W("2", "^2-154", "cakkhāyatanaṃ", "မျက်စိ", key="cakkhu «မျက်စိ»")
W("2", "^2-154", "ghānāyatanaṃ", "နှာခေါင်း", key="ghāna «နှာခေါင်း»")
NEG_NOUN = {"itthīnaṃ": new("na itthīnaṃ (persons)", f"{ITTHI} {NOT_BEING}"),
            "purisānaṃ": new("na purisānaṃ (persons)", f"{PURISA} {NOT_BEING}")}
NOUN = {"itthīnaṃ": ITTHI, "purisānaṃ": PURISA}      # head noun: «… ပြန်လည် ဖြစ်ပေါ်ဆဲ မိန်းမတို့»
PL = "တို့"
OTHER_ADJ = "အခြား"                               # itaresaṃ / itarāsaṃ + noun: «… အခြား မိန်းမတို့»
PACCHIMA_ADJ = f"{F.PACCHIMA}သော"                 # pacchimabhavika + noun: «… နောက်ဆုံး ဘဝ ရှိသော မိန်းမတို့»
_ORIG_ONE_GROUP = F._one_group


def _is_attr(toks, j):
    t = toks[j].lower() if j < len(toks) else ""
    if t in ATTR or t in NOUN:
        return True
    return t == "na" and j + 1 < len(toks) and toks[j + 1].lower() in NEG_NOUN


def one_group(toks):
    """F._one_group plus the attributes (ch. 3 «X ရှိလျက် / X မရှိဘဲ» and this chapter's) and the head nouns
    itthī / purisa, before place and participle."""
    j = 0
    while j < len(toks) and toks[j].lower() in ("sabbesaṃ", "itaresaṃ", "itarāsaṃ", "pacchimabhavikānaṃ"):
        j += 1
    if not (j < len(toks) and _is_attr(toks, j)):
        return _ORIG_ONE_GROUP(toks)
    allf = othf = pac = False
    while toks[0].lower() in ("sabbesaṃ", "itaresaṃ", "itarāsaṃ", "pacchimabhavikānaṃ"):
        w = toks.pop(0).lower()
        allf |= w == "sabbesaṃ"
        othf |= w in ("itaresaṃ", "itarāsaṃ")
        pac |= w == "pacchimabhavikānaṃ"
    attrs, noun = [], None
    while toks and _is_attr(toks, 0):
        w = toks.pop(0).lower()
        if w == "na":
            attrs.append(NEG_NOUN[toks.pop(0).lower()])
        elif w in NOUN:
            if noun:
                raise F.Miss("two head nouns")
            noun = NOUN[w]
        else:
            attrs.append(ATTR[w])
    places, case = [], None
    while toks and F._place_form(toks[0]) and F._place_form(toks[0])[1] in ("acc", "abl") \
            and case in (None, F._place_form(toks[0])[1]):
        k, case = F._place_form(toks.pop(0))
        places.append(k)
    if not toks or toks[0].lower() not in ("upapajjantānaṃ", "upapajjantīnaṃ", "cavantānaṃ"):
        raise F.Miss("attribute without participle: " + " ".join(toks))
    head = toks.pop(0).lower()
    verb, cw = F.PART[head]
    if case and case != {"upapajjantānaṃ": "acc", "upapajjantīnaṃ": "acc", "cavantānaṃ": "abl"}[head]:
        raise F.Miss("place case")
    loc = (F._join_places(places) + cw + " ") if places else ""
    a = (" ".join(attrs) + " ") if attrs else ""
    if noun:
        pre = (OTHER_ADJ + " " if othf else "") + (PACCHIMA_ADJ + " " if pac else "")
        if allf:
            raise F.Miss("sabbesaṃ + noun")
        return f"{a}{loc}{verb} {pre}{noun}{PL}"
    if pac:
        if othf or allf:
            raise F.Miss("pacchimabhavika + itara")
        return f"{a}{loc}{verb} {F.PACCHIMA}{F.THEM}"
    if othf:
        return f"{a}{loc}{verb} {F.OTHERS}"
    return f"{a}{loc}{verb}{F.ALL_OF if allf else F.THEM}"


F._one_group = one_group

# --- relative clauses: «ye / yā (ca) [purisā | itthiyo | sacakkhukā …] [eteneva bhāvena katici bhave dassetvā]
#     [somanassena | upekkhāya] [places-acc] [upapajjitvā] parinibbāyissanti»
REL_HEAD = {"purisā": f" {PURISA}{PL}", "itthiyo": f" {ITTHI}{PL}"}
REL_ATTR = {"sacakkhukā": ATTR["sacakkhukānaṃ"], "saghānakā": ATTR["saghānakānaṃ"]}
BHAVA = new("eteneva bhāvena katici bhave dassetvā", "ဤ အဖြစ်ဖြင့်ပင် ဘဝ အချို့ကို ဖြတ်သန်းပြီး")
REBORN_THEN = "ပြန်လည် ဖြစ်ပေါ်ပြီး"         # upapajjitvā (sample GROUP_ATOMS)
PARINIB_FUT = "ပရိနိဗ္ဗာန် ပြုမည့်"            # parinibbāyissanti (relative; sample GROUP_ATOMS)
assert F.GROUP_ATOMS["ye arūpaṃ upapajjitvā parinibbāyissanti"] == \
    f"{F.PLACES['arūpa']}{F.LOC} {REBORN_THEN} {PARINIB_FUT}{F.THEM}"


def rel_at(toks, i):
    """A relative clause at toks[i] (lower case) -> (Burmese person phrase, next i) or None."""
    if i >= len(toks) or toks[i] not in ("ye", "yā"):
        return None
    j = i + 1
    if j < len(toks) and toks[j] == "ca":
        j += 1
    head, parts = F.THEM, []
    if j < len(toks) and toks[j] in REL_HEAD:
        head = REL_HEAD[toks[j]]
        j += 1
    elif j < len(toks) and toks[j] in REL_ATTR:
        parts.append(REL_ATTR[toks[j]])
        j += 1
    if toks[j:j + 5] == ["eteneva", "bhāvena", "katici", "bhave", "dassetvā"]:
        parts.append(BHAVA)
        j += 5
    if j < len(toks) and toks[j] in ("somanassena", "upekkhāya"):
        parts.append(ATTR[toks[j]])
        j += 1
    places = []
    while j < len(toks) and F._place_form(toks[j]) and F._place_form(toks[j])[1] == "acc":
        places.append(F._place_form(toks[j])[0])
        j += 1
    if places:
        parts.append(F._join_places(places) + F.LOC)
    if j < len(toks) and toks[j] == "upapajjitvā":
        parts.append(REBORN_THEN)
        j += 1
    elif places:
        raise F.Miss("relative: places without upapajjitvā")
    if j >= len(toks) or toks[j] != "parinibbāyissanti":
        raise F.Miss("relative clause: " + " ".join(toks[i:]))
    parts.append(PARINIB_FUT)
    return " ".join(parts) + head, j + 1


# --- moments (make_ch2-02-4-5.py _moment_at, extended)
KHANA = W("5", "^5-366", "Uppādakkhaṇe vimuttaṃ, bhaṅgakkhaṇe", "ဖြစ်ခြင်း ခဏ၌", key="uppādakkhaṇe")
MOMENT = {"uppādakkhaṇe": KHANA,
          "bhaṅgakkhaṇe": W("5", "^5-366", "bhaṅgakkhaṇe", "ပြိုပျက်ခြင်း ခဏ၌")}
PACCHIMA_CITTA = f"နောက်ဆုံး {CITTA}"                       # pacchimacitta (ch. 5 / ch. 6-8)
GEN = {   # genitive of a moment phrase -> Burmese (before «၏»)
    "cittassa": CITTA,
    "pacchimacittassa": PACCHIMA_CITTA,
    "upapatticittassa": f"{F.PART['upapajjantānaṃ'][0][:-2]}ခြင်း {CITTA}",   # ch. 5 «ပြန်လည် ဖြစ်ပေါ်ခြင်း စိတ်»
}
for q, qm in QUAL.items():
    GEN[f"{q}sampayuttacittassa"] = new(f"{q}sampayuttacitta", f"{qm}{SAMP} {CITTA}")
    GEN[f"{q}vippayuttacittassa"] = new(f"{q}vippayuttacitta", f"{qm}{VIPP} {CITTA}")
    GEN[f"{q}sampayuttapacchimacittassa"] = new(f"{q}sampayuttapacchimacitta", f"{qm}{SAMP} {PACCHIMA_CITTA}")
ACC_CITTA = {f"{q}sampayuttapacchimacittaṃ": GEN[f"{q}sampayuttapacchimacittassa"] for q in QUAL}
PAVATTE = "ဘဝ တည်နေစဉ်"                                     # pavatte (ch. 5)
VATTAMANE = W("5", "^5-556", "citte vattamāne", "စိတ် ဖြစ်နေစဉ်", key="citte vattamāne")
CITTE = {"dutiye citte": f"ဒုတိယ {VATTAMANE}"}             # ch. 5 «ဒုတိယ စိတ် ဖြစ်နေစဉ်»
ANANTARA = W("2", "^2-751", "samanantarā", "ချက်ချင်း နောက်၌", key="anantarā")
OWN_CITTA = f"မိမိ {CITTA}၏"                                 # yassa cittassa anantarā … (persons; ch. 6-8)
YASSA_CITTA = ("အကြင်" + CITTA + "၏", "ထို" + CITTA + "၏")    # yassa cittassa … tassa cittassa (ch. 5)
SAMANGI = W("1", "^1-1039", "Ariyamaggasamaṅgissa", "နှင့် ပြည့်စုံသူ", key="-samaṅgī")
NAMED = {   # named persons (gen. pl.) -> Burmese person phrase (ch. 5 / ch. 6-8)
    "pacchimacittasamaṅgīnaṃ": f"{PACCHIMA_CITTA}{SAMANGI}{PL}",
    "nirodhasamāpannānaṃ": "ချုပ်ငြိမ်းခြင်း သမာပတ်ကို ဝင်စားနေ" + F.THEM,
}


def _moment_at(toks, i):
    """A moment phrase at toks[i]: [places-loc] [pavatte] GEN (uppāda|bhaṅga)kkhaṇe | dutiye citte vattamāne |
    yassa cittassa anantarā X uppajjissati tassa cittassa …kkhaṇe -> (Burmese, next i) or None."""
    j, pre = i, []
    places = []
    while j < len(toks) and F._place_form(toks[j]) and F._place_form(toks[j])[1] == "loc":
        places.append(F._place_form(toks[j])[0])
        j += 1
    if places:
        pre.append(F._join_places(places) + F.LOC)
    if j < len(toks) and toks[j] == "pavatte":
        pre.append(PAVATTE)
        j += 1
    if toks[j:j + 3] == ["yassa", "cittassa", "anantarā"] and j + 7 < len(toks) and toks[j + 3] in ACC_CITTA:
        v = toks[j + 4]
        if toks[j + 5:j + 7] != ["tassa", "cittassa"] or toks[j + 7] not in MOMENT:
            raise F.Miss("yassa cittassa anantarā …: " + " ".join(toks[j:]))
        my = (f"{YASSA_CITTA[0]} {ANANTARA} {ACC_CITTA[toks[j + 3]]} {F.V(v, 'cl')}{C} "
              f"{YASSA_CITTA[1]} {MOMENT[toks[j + 7]]}")
        new(f"yassa cittassa anantarā {toks[j + 3]} {v} tassa cittassa {toks[j + 7]}", my)
        return " ".join(pre + [my]), j + 8
    g = toks[j] if j < len(toks) else ""
    if g in GEN and j + 1 < len(toks) and toks[j + 1] in MOMENT:
        return " ".join(pre + [f"{GEN[g]}၏ {MOMENT[toks[j + 1]]}"]), j + 2
    for n in (2,):
        g = " ".join(toks[j:j + n])
        if g in CITTE and j + n < len(toks) and toks[j + n] == "vattamāne":
            return " ".join(pre + [CITTE[g]]), j + n + 1
    return None


PERSON_TOK = ("sabbesaṃ", "itaresaṃ", "itarāsaṃ", "pacchimabhavikānaṃ", "na")


def _is_person_tok(t):
    return t in PERSON_TOK or t in F.PART or t in ATTR or t in NOUN or bool(F._place_form(t))


SLIPS_LEAD = {"pacchimacittasamaṅgīna": "pacchimacittasamaṅgīnaṃ",     # 10-06 (missing ṃ)
              "cavantāna": "cavantānaṃ"}                               # (missing ṃ)


def lead_units(who):
    """A person / moment / place lead -> [(kind, Burmese)]: P person, M moment, L place (ch. 5 lead parser)."""
    toks = []
    for t in who.replace(",", "").split():
        t = t[0].lower() + t[1:]
        toks.append(SLIPS_LEAD.get(t, t))
    units, i, prefix = [], 0, ""
    while i < len(toks):
        t = toks[i]
        mo = _moment_at(toks, i)
        if mo:
            units.append(["M", prefix + mo[0]])
            prefix = ""
            i = mo[1]
            continue
        if t == "sabbesaṃ" and _moment_at(toks, i + 1):
            prefix = f"{F.ALL_OF}၏ "                                 # ch. 5 «သူ အားလုံးတို့၏ …»
            i += 1
            continue
        if t in ("tesaṃ", "tāsaṃ"):                                 # inner «tesaṃ» after a relative clause
            if i + 1 < len(toks) and toks[i + 1] in F.PART and units and units[-1][0] == "P" \
                    and units[-1][1].endswith(PL):
                verb = F.PART[toks[i + 1]][0]
                units[-1][1] += "အနက် " + verb + F.THEM            # ch. 3 / ch. 5 «…သူတို့အနက် …ဆဲသူတို့»
                i += 2
                continue
            raise F.Miss("lead: inner tesaṃ")
        if toks[i:i + 3] == ["yassa", "cittassa", "anantarā"] and i + 4 < len(toks) and toks[i + 3] in ACC_CITTA:
            v = toks[i + 4]
            my = new(f"yassa cittassa anantarā {toks[i + 3]} {v} (persons)",
                     f"{OWN_CITTA} {ANANTARA} {ACC_CITTA[toks[i + 3]]} {F.V(v, 'attr')}{F.THEM}")
            units.append(["P", my])
            i += 5
            continue
        r = rel_at(toks, i)
        if r:
            units.append(["P", r[0]])
            i = r[1]
            continue
        if t in NAMED:
            units.append(["P", NAMED[t]])
            i += 1
            continue
        if _is_person_tok(t):
            j = i
            while j < len(toks) and _is_person_tok(toks[j]) and not (j > i and _moment_at(toks, j)) \
                    and not (toks[j] == "sabbesaṃ" and _moment_at(toks, j + 1)) and toks[j] not in NAMED:
                j += 1
            run = toks[i:j]
            if all(F._place_form(x) and F._place_form(x)[1] == "loc" for x in run):
                units.append(["L", F.place_my(" ".join(run))])
            else:
                while run:
                    units.append(["P", F._one_group(run)])
            i = j
            continue
        raise F.Miss("lead token: " + t + " in " + " ".join(toks))
    if prefix:
        raise F.Miss("lead: dangling prefix")
    return [tuple(u) for u in units]


def _join_p(parts):
    return parts[0] if len(parts) == 1 else f"{C} ".join(parts[:-1]) + f"{AND} " + parts[-1]


def join_lead(units):
    """Consecutive person units joined as the module joins groups («A၊ Bနှင့် C»), the rest with «၊ » (ch. 5)."""
    segs, run = [], []
    for kind, txt in units:
        if kind == "P":
            run.append(txt)
            continue
        if run:
            segs.append(_join_p(run))
            run = []
        segs.append(txt)
    if run:
        segs.append(_join_p(run))
    return f"{C} ".join(segs)


# harmonise B1: a lead that is one moment alone has the ch. 5 form «M ထိုသူတို့အား» (no «M ရှိသူတို့အား» any more)
# harmonise B3: tāsaṃ (fem., after itthīnaṃ …) = «ထိုမိန်းမတို့» (as ch9-10a), tesaṃ «ထိုသူတို့»
THEY_F = "ထိုမိန်းမတို့"
_who_module = F.who_my


def who_my(who, pro):
    """The module's who_my first (person runs / places, identical to the sample and ch. 3); else the lead parser."""
    fem = pro.startswith("tāsaṃ")
    pro = pro.replace("tāsaṃ", "tesaṃ")                 # the lead itself as with tesaṃ; the pronoun «ထိုမိန်းမတို့»
    try:
        return _who_module(who, pro)
    except (F.Miss, KeyError, IndexError):
        pass
    units = lead_units(who)
    if pro == "tattha":
        if any(k != "L" for k, _ in units):
            raise F.Miss("lead: tattha after persons")
        return join_lead(units)
    last = units[-1][0]
    if last == "P":
        out = join_lead(units) + DAT
    elif last == "M":
        out = join_lead(units) + " " + (THEY_F + DAT if fem else F.PRO["tesaṃ"])
    else:
        raise F.Miss("lead: place before tesaṃ")
    return out + (" " + F.FT["tattha"] if pro == "tesaṃ tattha" else "")


F.who_my = who_my

# ===================================================================================== pavatti sentences
VB = F.VB
PROR = r"(?:tesaṃ tattha|tāsaṃ tattha|tattha|tesaṃ|tāsaṃ)"
F.PRO.update({"tāsaṃ": THEY_F + DAT, "tāsaṃ tattha": THEY_F + DAT + " " + F.FT["tattha"]})   # harmonise B3
A_BUT = re.compile(rf"^(?P<who>.+?) (?P<pro>{PROR}) (?P<x>\S+) (?P<v1>{VB}),? no ca (?P<pro2>{PROR}) (?P<y>\S+) "
                   rf"(?P<v2>{VB})\.$")
A_BOTH = re.compile(rf"^(?P<who>.+?) (?P<pro>{PROR}) (?P<x>\S+?)(?P<c1>ñca| ca)? (?P<v1>{VB}),? (?P<y>\S+?)"
                    rf"(?P<c2>ñca| ca)? (?P<v2>{VB})\.$")


def subj_ca(x, c):
    return F.subj(x + "ṃ" if c == "ñca" else x)


A_ONE = re.compile(rf"^(?P<who>.+?) (?P<pro>{PROR}) (?P<x>\S+?)ñca (?P<v1>{VB})\.$")
S_ONE = re.compile(rf"^(?P<x>\S+?)ñca (?P<v1>{VB})\.$")


def pavatti(s):
    r = F.pavatti_sentence(s)
    if r:
        return r
    m = A_ONE.match(s)          # slip: «… tesaṃ tattha Xñca V. Yñca V.» (one «ca … ca» sentence cut by «.»)
    if m:
        return f"{F.who_my(m['who'], m['pro'])} {F.subj(m['x'] + 'ṃ')}{ALSO} {F.V(m['v1'])}{END}"
    m = S_ONE.match(s)
    if m:
        return f"{F.subj(m['x'][0].lower() + m['x'][1:] + 'ṃ')}{ALSO} {F.V(m['v1'])}{END}"
    m = A_BUT.match(s)
    if m:
        r = F.a_but(m["who"], m["pro"], m["x"], m["v1"], m["pro2"], m["y"], m["v2"])   # harmonise B3
        if ", no ca " not in s:           # harmonise A4: ^6-10-318 «… na uppajjissati no ca …»: no «၊» (no Pāli «,»)
            r = r.replace(f"{C} {F.BUT} ", f" {F.BUT} ", 1)
        return r
    m = A_BOTH.match(s)
    if m and (m["c1"] or m["c2"]):
        X, Y = subj_ca(m["x"], m["c1"]), subj_ca(m["y"], m["c2"])
        return (f"{F.who_my(m['who'], m['pro'])} {X}{ALSO if m['c1'] else ''} {F.V(m['v1'])}{C} "
                f"{Y}{ALSO if m['c2'] else ''} {F.V(m['v2'])}{END}")
    return None


# ===================================================================================== notes and slips
NOTES = {"(Sadisaṃ )": new("(Sadisaṃ) (note)", "(တူညီသည်)")}     # sadisaṃ «တူညီသည်» (ch. 5); stray space dropped
for k, v in IND.items():
    NOTES[f"({k[0].upper()}{k[1:-1]}mūlakaṃ)"] = f"({v}{F.BASED})"   # (Cakkhundriyamūlakaṃ) = «(မျက်စိ၏ စွမ်းရည်ကို အခြေခံ၍)»
NOTES["(Ghānandriyamūlakaṃ)"] = NOTES["(Ghānindriyamūlakaṃ)"]       # 10-08 slip «Ghānandriya-»
NOTE_RE = re.compile("|".join(re.escape(k) for k in sorted(NOTES, key=len, reverse=True)))
SLIPS = [   # (Pāli as written, reading used) - logged in notes-ch10b.md
    ("manindriyaṃ ca uppajj", "manindriyañca uppajj"),              # «manindriyaṃ ca» for manindriyañca
    ("somanassindriyaṃ na upapajjissati", "somanassindriyaṃ na uppajjissati"),   # 10-06 upapajj- for uppajj-
    ("uppajjissati, tassa purisindriyaṃ", "uppajjissati tassa purisindriyaṃ"),  # 10-09 stray comma (Burmese «၊» anyway)
]


def unslip(s):
    for a, b in SLIPS:
        s = s.replace(a, b)
    return s


# ===================================================================================== «…pe…» fragments (make_ch3.py)
VBW = re.compile(rf"^{VB}$")
FT_KEYS = ["tassa tattha", "tassa", "tattha"]
ANS_BARE = {k[:-1]: v[:-1] for k, v in F.ANSWERS.items()}      # «Āmantā» / «No» / «Natthi» without the stop


def who_try(who, pro):
    try:
        return F.who_my(who, pro)
    except (F.Miss, KeyError, IndexError):
        return None


def before_ft(low, j):
    return any(low[j:j + len(k.split())] == k.split() for k in FT_KEYS)


def frag_pavatti(s, end):
    """Token translation of a pavattivāra piece cut by «…» (no frame fits a cut sentence) (make_ch3.py)."""
    toks = s.split()
    out = []
    i = 0
    verb_seen = flip = in_q = ft_seen = False
    found = None
    if not re.match(r"^(?:[Yy]assa|[Yy]attha|tassa|tattha)\b", s):
        for m in re.finditer(rf" ({PROR})(?= |$)", s):
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
            k = next((k for k in ("tesaṃ tattha", "tāsaṃ tattha", "tesaṃ", "tāsaṃ", "tattha")
                      if low[i:i + len(k.split())] == k.split()), None)
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


def sentence(s):
    r = pavatti(s)
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
        r = pavatti(s)
        if r:
            return r
    if VBW.match(core) and end == ".":
        return F.V(core) + END                       # «Uppajjittha.» after «…»
    return frag_pavatti(core, END if end else "")


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
    """Text with «…»: the pieces between the ellipses one by one (make_ch3.py)."""
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
            piece += " ".join(fragment(x) for x in F.SPLIT.split(core))
        out.append(piece + trail)
    return "".join(out)


def body_plain(text):
    return " ".join(sentence(x) if x[-1] in ".?" else fragment(x) for x in F.SPLIT.split(text))


def body(line):
    if line in F.COLO:
        return F.COLO[line]
    line = unslip(line)
    notes = []

    def keep_note(m):
        notes.append(NOTES[m[0]])
        return f"⟪{len(notes) - 1}⟫"
    line = NOTE_RE.sub(keep_note, line)
    if "[" in line:
        raise F.Miss("variant bracket (none expected): " + line)
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
    return "".join(out)


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
    if re.search(r"[A-Za-zāīūṃṅñṭḍṇḷ⟦⟧⟪⟫]", out.replace(bid, "")):
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


LEAD_RE = re.compile(rf"^(?P<who>.+?) (?P<pro>{PROR}) \S+ (?:ca )?(?:{VB})")


def who_list(names):
    """--who: every distinct lead of the answers with its Burmese."""
    import collections
    c = collections.Counter()
    for n in names:
        for l in (PALI / n).read_text(encoding="utf-8-sig").splitlines():
            for s in F.SPLIT.split(F.strip_id(l)):
                m = LEAD_RE.match(s)
                if m and not re.match(r"^\(\w+\) ", s) and not s.lower().startswith(("yassa", "yattha")):
                    c[(m["who"], m["pro"])] += 1
    for (w, p), v in sorted(c.items()):
        print(v, w, "|", p, "=>", F.who_my(w, p))


if __name__ == "__main__":
    sel = [a for a in sys.argv[1:] if not a.startswith("--")]
    names = [n for n in NAMES_OUT if not sel or any(n.startswith(s) for s in sel)]
    if "--who" in sys.argv:
        who_list(names)
        sys.exit(0)
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
