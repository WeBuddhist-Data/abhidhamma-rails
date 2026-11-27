"""Burmese zero-shot of pi-6 ch. 7, second group (Anusayayamaka, «ကိန်းအောင်းခြင်းများကို အတွဲလိုက် မေးဖြေခြင်း»):
7-06 … 7-11 (pajahanavāra paṭiloma, pariññāvāra, pahīnavāra, uppajjanavāra, dhātupucchā- / dhātuvisajjanāvāra).

usage: python3 -I -X utf8 make_ch7b.py [7-06 7-07 …] [--misses]   (no chapter = all six)
Built on make_ch7a.py (the model group 7-01 … 7-05), which is IMPORTED READ-ONLY (its import writes nothing; it only
extends my6_formulas' tables in memory): its TABLES (the seven anusayas, case endings, persons, places, pronouns,
question intros, headings, colophons, notes) are used as they are, so identical Pāli gets identical Burmese. Its
token translator is copied here (sentence_my) and extended for this group: nappajahati (prepared in ch7a, used here),
«na parijānāti», pahīno / appahīno, uppajjati / nuppajjati, «na vattabbo "…"ti vā "…"ti vā», «;», the
«… ṭhapetvā avasesā puggalā» subjects, the dhātupucchā questions and dhātuvisajjanā answers (cuta / upapajjanta, kati,
kassaci, satta / pañca / tayo, satteva, bhaṅgā), notes and variant brackets. A token that no table knows stops the
run (F.Miss): nothing is guessed. Each line is checked against its Pāli (line_check of make_ch7a); a chapter file is
written only when every line passed. --misses lists unmatched lines and writes nothing.
New strings are logged in notes-ch7b.md.
"""
import pathlib
import re
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import make_ch7a as A  # noqa: E402  (read-only model: tables + line_check; nothing written at import)

F = A.F
W = F.W
PALI, OUT = A.PALI, A.OUT
NAMES_OUT = [f"7-{i:02d}-anusayayamaka.md" for i in range(6, 12)]
C, END, PE = F.C, F.END, F.PE
AND, ALSO, OBJ = F.AND, A.ALSO, A.OBJ
P = A.P

# =====================================================================================================================
# NEW / extended tables of this group (every new string is logged in notes-ch7b.md)
# =====================================================================================================================
# --- verbs ------------------------------------------------------------------------------------------------------
F.VERB["parijān"] = "သိ"                       # «ပိုင်းခြား သိ» (as make_ch3.py: the «မ» goes before «သိ»)
PJ_PRE = W("5", "^5-390", "parijānāti", "ပိုင်းခြား သိ", key="parijānāti")[:-len("သိ")]     # «ပိုင်းခြား »
PAHINA = W("4", "^4-65", "pahīno", "ပယ်ပြီး ဖြစ်", key="pahīno")            # «Xကို ပယ်ပြီး ဖြစ်၏» (pi-4)
APPAHINA = W("4", "^4-45", "appahīno", "မပယ်ရသေး", key="appahīno")          # «Xကို မပယ်ရသေး» (pi-4)
W("5", "^5-65", "cuto arūpadhātuṃ upapajjatī", "မှ သေ၍ ရုပ်မရှိသော ဘုံ၌ ပြန်လည် ဖြစ်ပေါ်", key="X-ā cuto Y-aṃ upapajjati")
UPAPAJJ = F.PART["upapajjantānaṃ"][0][:-len("ဆဲ")]                          # «ပြန်လည် ဖြစ်ပေါ်» (upapajjati)
CAVATI = F.PART["cavantānaṃ"][0][:-len("ဆဲ")]                               # «စုတေ» (cavati, sample)
VERB_RE = dict(A.VERB_RE)
VERB_RE.update({
    "pj": re.compile(r"^parijān(?P<pl>ā|an)(?P<q>ti|tīti)$"),                     # parijānāti / -ātīti / -anti
    "pah": re.compile(r"^(?P<neg>ap|)pahīn(?P<pl>o|ā)(?P<q>ti)?$"),               # pahīno / appahīnāti …
    "up": re.compile(r"^(?P<neg>n|)uppajj(?P<pl>a|an)(?P<q>ti|tīti)$"),           # uppajjati / nuppajjatīti
})
ROOT_OF = dict(A.ROOT_OF, up="uppajj")
NEG_W = ("nā", "nira", "nap", "ap", "n")
PL_OF = {"anu": ("nt",), "sa": ("ā",), "pa": ("an", "n"), "pj": ("an",), "pah": ("ā",), "up": ("an",)}

# --- na vattabbo "pahīno"ti vā "appahīno"ti vā -----------------------------------------------------------------
W("2", "^2-641", 'na vattabbā "hetū ceva sahetukā cā"ti', "ဟု ခေါ်ဆို၍ မရ", key="na vattabbā \"…\"ti")
W("5", "^5-386", '"saññā atthī"ti vā "natthī"ti vāti', "”ဟူ၍ဖြစ်စေ၊ “မရှိ”ဟူ၍ဖြစ်စေ", key="\"…\"ti vā \"…\"ti vā")
NOT_CALL = "ခေါ်ဆို၍ မရ"                       # na vattabbo / na vattabbā (pi-2)
TI_VA = "ဟူ၍ဖြစ်စေ"                           # "…"ti vā (pi-5)
QUOTE_W = {"pahīno": "ပယ်ပြီး", "pahīnā": "ပယ်ပြီး", "appahīno": APPAHINA, "appahīnā": APPAHINA}


def vattabba_my(q1, q2):
    """«“ပယ်ပြီး”ဟူ၍ဖြစ်စေ၊ “မပယ်ရသေး”ဟူ၍ဖြစ်စေ ခေါ်ဆို၍ မရ» (the object, if any, is «Xကို»)."""
    return f"“{QUOTE_W[q1]}”{TI_VA}{C} “{QUOTE_W[q2]}”{TI_VA} {NOT_CALL}"


# --- persons ----------------------------------------------------------------------------------------------------
ANAGAMIMAGGA = W("5", "^5-339", "anāgāmimaggaṃ", "အနာဂါမိမဂ်", key="anāgāmimagga")
SAMANGI = W("2", "^2-809", "kāyaduccaritasamaṅgī", "နှင့် ပြည့်စုံသူ", key="-samaṅgī")
ANAGAMI_SAM = f"{ANAGAMIMAGGA}{SAMANGI}"                 # «အနာဂါမိမဂ်နှင့် ပြည့်စုံသူ» (as make_ch10c.py)
MAGGA_SAM = f"{W('1', '^1-M1-16', 'magg', 'မဂ်')}{SAMANGI}"   # maggasamaṅgī «မဂ်နှင့် ပြည့်စုံသူ»
assert A.AGGA_SAM == f"အမြတ်ဆုံး {MAGGA_SAM}"
WHO = dict(A.WHO)
WHO.update({("anāgāmimaggasamaṅgī",): (ANAGAMI_SAM, "nom", False, False)})
# members of «… ṭhapetvā avasesā puggalā» (acc. «-ṃ», acc. + ca «-ñca», gen. pl. «dvinnaṃ maggasamaṅgīnaṃ(ca)»)
LEAVE = {("aggamaggasamaṅgiñca",): A.AGGA_SAM, ("aggamaggasamaṅgiṃ",): A.AGGA_SAM,
         ("anāgāmimaggasamaṅgiñca",): ANAGAMI_SAM, ("anāgāmimaggasamaṅgiṃ",): ANAGAMI_SAM,
         ("aṭṭhamakañca",): A.ATTHAMA,
         ("dvinnaṃ", "maggasamaṅgīnaṃ"): f"{MAGGA_SAM} {A.COUNT[2].split()[-1]}{A.PL}",
         ("dvinnaṃ", "maggasamaṅgīnañca"): f"{MAGGA_SAM} {A.COUNT[2].split()[-1]}{A.PL}"}
REST = f"{F.AVASESA} {A.PUGGALA}{A.PL}"                     # avasesā puggalā «ကြွင်းကျန်သော ပုဂ္ဂိုလ်တို့» (make_ch3.py)


def leave_my(members):
    """«Aနှင့် Bကို ချန်ထား၍၊ ကြွင်းကျန်သော ပုဂ္ဂိုလ်တို့သည်» (make_ch3.py PJ_SUBJ)."""
    return f"{f'{AND} '.join(members)}{OBJ} {F.THAPETVA}{C} {REST}{A.CASE_P['nom']}"


# --- dhātupucchā / dhātuvisajjanā ------------------------------------------------------------------------------
DHATU = {"kāma": A.KAMA, "rūpa": A.RUPA_B, "arūpa": A.ARUPA_B}
NOT_BE = F.NEGV[F.BE]                                       # «မဟုတ်»
BHUMI = "ဘုံ"


def dhatu_my(keys_neg):
    """[('kāma', False)] -> «ကာမဘုံ»; [('kāma', True)] -> «ကာမဘုံ မဟုတ်သော ဘုံ»; [('kāma', True), ('arūpa', True)] ->
    «ကာမဘုံလည်း မဟုတ်၊ ရုပ်မရှိသော ဘုံလည်း မဟုတ်သော ဘုံ» (pi-5 ^5-386 «… ရှိသည်လည်း မဟုတ်၊ … မရှိသည်လည်း မဟုတ်သော»)."""
    if len(keys_neg) == 1:
        k, neg = keys_neg[0]
        return f"{DHATU[k]} {NOT_BE}သော {BHUMI}" if neg else DHATU[k]
    if not all(n for _, n in keys_neg):
        raise F.Miss(f"dhātu {keys_neg}")
    return f"{C} ".join(f"{DHATU[k]}{ALSO} {NOT_BE}" for k, _ in keys_neg) + f"သော {BHUMI}"


W("2", "^2-1007", "kassaci ekādasāyatanāni pātubhavanti", "အချို့အား", key="kassaci")
SOME = "အချို့အား"                                            # kassaci (pi-2 ^2-1007)
SOME_OF = "အချို့"                                            # first kassaci after the person «…သူ အချို့အား»
W("2", "^2-151", "kati kusalā", "မည်မျှ", key="kati")
KATI = "မည်မျှ"                                               # kati (pi-2 ^2-151)
NUM_A = {"satta": W("2", "^2-838", "Satta anusayā", "ခုနစ်ပါး", key="satta (anusayā)"), "pañca": "ငါးပါး",
         "tayo": A.NUM_P["tīsu"]}                            # satta / pañca / tayo anusayā «ကိန်းအောင်းခြင်း N ပါး»
BHANGA = W("5", "^5-366", "bhaṅgakkhaṇe", "ပြိုပျက်", key="bhaṅga")    # bhaṅgā «ပြိုပျက်…» (pi-5 «ပြိုပျက်ခြင်း»)
UPAPATTI = f"{UPAPAJJ}ခြင်း"                                  # upapatti «ပြန်လည် ဖြစ်ပေါ်ခြင်း» (ch2-02-4-5 upapatticitta)
NAMA_NATTHI = f"ဟူ၍ {F.NEGV[F.HAVE]}"                         # «upapatti nāma natthi» «… ဟူ၍ မရှိ» (NEW)
W("1", "^1-1287", "Heṭṭhato", "အောက်၌", key="heṭṭhā")
HETTHA = "အောက်၌"                                             # heṭṭhā (pi-1 ^1-1287 heṭṭhato)
ONE = "သူ"                                                    # the person of a participle «…ဆဲသူ», «စုတေသူ»
ANUSAYA_W = A.ANUSAYA_W                                       # «ကိန်းအောင်းခြင်း»


def anu_v(neg, form):
    return A.verb_my("anu", neg, True, form)                  # anusenti / nānusenti (plural)


# --- headings, colophons, notes ---------------------------------------------------------------------------------
PARINNA = W("2", "^2-1029", "pariññāya", "ပိုင်းခြား သိ", key="pariññā") + "ခြင်း"   # (make_ch3.py)
PAHINA_N = f"{PAHINA}ခြင်း"                                    # pahīna «ပယ်ပြီး ဖြစ်ခြင်း» (NEW)
PUCCHA = W("5", "^5-652", "pucchā", "အမေး", key="pucchā")      # pucchā «အမေး» (pi-5)
VISAJJANA = "အဖြေ"                                            # visajjanā «အဖြေ» (NEW)
DHATU_ABOUT = f"{BHUMI}များအကြောင်း"                            # dhātu- (the three planes) «ဘုံများအကြောင်း» (NEW)
VARA_OF = dict(A.VARA_OF)
VARA_OF.update({"Pariññā": F.vara(PARINNA), "Pahīna": F.vara(PAHINA_N), "Uppajjana": F.vara(F.UPPADA)})
DHATU_P = f"{DHATU_ABOUT} {PUCCHA} {F.VARA}"                    # dhātupucchāvāro «ဘုံများအကြောင်း အမေး ဖော်ပြချက်»
DHATU_V = f"{DHATU_ABOUT} {VISAJJANA} {F.VARA}"                 # dhātuvisajjanāvāro «ဘုံများအကြောင်း အဖြေ ဖော်ပြချက်»
H_NEW = {"Pariññāvāro": VARA_OF["Pariññā"], "Pariññāvāra": VARA_OF["Pariññā"],
         "Pahīnavāro": VARA_OF["Pahīna"], "Pahīnavāra": VARA_OF["Pahīna"],
         "Uppajjanavāro": VARA_OF["Uppajjana"], "dhātupucchāvāro": DHATU_P, "dhātuvisajjanāvāro": DHATU_V}
for _k, _v in H_NEW.items():
    if _k in F.H and F.H[_k] != _v:
        raise F.Miss(f"heading {_k} already {F.H[_k]}")
F.H.update(H_NEW)
COLO = dict(A.COLO)
for _k in ("Pariññā", "Pahīna", "Uppajjana"):
    _v = VARA_OF[_k]
    COLO[f"{_k}vāro."] = f"{_v}{END}"
    COLO[f"{_k}vāre anulomaṃ."] = f"{_v}၌ {F.ANULOMA}{END}"
    COLO[f"{_k}vāre paṭilomaṃ."] = f"{_v}၌ {A.PATILOMA}{END}"
COLO["Dhātupucchāvāro."] = f"{DHATU_P}{END}"
COLO["Dhātuvisajjanāvāro."] = f"{DHATU_V}{END}"
NOTES = dict(A.NOTES)
VITTH = W("5", "^5-839", "vitthāretabb", "အကျယ် ချဲ့", key="vitthāreti") + "ရမည်"   # (make_ch3.py / ch2-02-4-5)
NOTES["(vitthāretabbaṃ)"] = NOTES["(Vitthāretabbaṃ)"] = f"({VITTH})"
DHATU_NOTE = {"Kāmadhātu": [("kāma", False)], "Rūpadhātu": [("rūpa", False)], "Arūpadhātu": [("arūpa", False)],
              "Nakāmadhātu": [("kāma", True)], "Narūpadhātu": [("rūpa", True)], "Naarūpadhātu": [("arūpa", True)],
              "Nakāmanaarūpadhātu": [("kāma", True), ("arūpa", True)],
              "Narūpanaarūpadhātu": [("rūpa", True), ("arūpa", True)],
              "Nakāmanarūpadhātu": [("kāma", True), ("rūpa", True)]}
for _k, _v in DHATU_NOTE.items():   # (Kāmadhātumūlakaṃ) «(ကာမဘုံကို အခြေခံ၍)» (NEW, as the -mūlaka notes of ch7a)
    NOTES[f"({_k}mūlakaṃ)"] = f"({dhatu_my(_v)}{F.BASED})"
VARIANT = {   # whole variant brackets (inner text) -> Burmese (pi-4 ^4-117 «… နှင့်ကား ညီ၏» for «… pana sameti»)
    "pahīno (sī. ka.) anusayavārena pana na sameti":
        f"[{F.VAR_P} (Sī., Ka.): pahīno{C} {VARA_OF['Anusaya']}{AND}ကား မညီ]",
}

# --- source slips (translated as written; read as the evident word) ----------------------------------------------
SLIPS = [
    ("Pajahanāvāre paṭilomaṃ.", "Pajahanavāre paṭilomaṃ."),      # 7-06 ^6-7-197: «Pajahanā-» for Pajahana-
    ("Dhātuvisajjavāro.", "Dhātuvisajjanāvāro."),                # 7-11: «-visajja-» for -visajjanā- (heading)
    ("upapattināma natthi", "upapatti nāma natthi"),             # 7-11 ^6-7-348: «upapattināma» (spacing)
    ("kāmadhātuyā tīsu vedanāsu, apariyāpanne", "kāmadhātuyā tīsu vedanāsu apariyāpanne"),   # 7-08: stray «,»
]


def unslip(s):
    s = A.unslip(s)
    for a, b in SLIPS:
        s = s.replace(a, b)
    return s


# =====================================================================================================================
# the token translator (copied from make_ch7a.sentence_my; extended)
# =====================================================================================================================
TOK = re.compile(r"…|[^\s…]+")


def tokens(s):
    """as make_ch7a.tokens, «;» split off too."""
    out = []
    for m in TOK.finditer(s):
        w, sp = m[0], m.start() > 0 and s[m.start() - 1] == " "
        tail = []
        while w and w[-1] in ",.?;" and w != "…":
            tail.insert(0, w[-1])
            w = w[:-1]
        if w:
            out.append((w, sp))
            sp = False
        for t in tail:
            out.append((t, False))
    return out


def verb_parse(w):
    for fam, rx in VERB_RE.items():
        m = rx.match(w)
        if m:
            neg = m.groupdict().get("neg") in NEG_W
            pl = m["pl"] in PL_OF[fam]
            q = m["q"] in ("īti", "tīti") or (fam in ("sa", "pah") and m["q"] == "ti")
            return fam, neg, pl, q
    return None


def verb_my(fam, neg, pl, form):
    """make_ch7a.verb_my + pj (parijānāti), pah (pahīno), up (uppajjati)."""
    if fam in ("anu", "sa", "pa"):
        return A.verb_my(fam, neg, pl, form)
    if fam == "pah":                                          # pahīna: no «ကြ» (pi-4 ^4-44 plural «… ပယ်ပြီး ဖြစ်၏»)
        if form == "noca":
            return APPAHINA + ("သည်" + F.NOT_SO if neg else "")
        if neg:
            return APPAHINA + ("သလော" if form == "q" else "")
        return PAHINA + {"stmt": "သည်", "cl": "၏", "q": "သလော"}[form]
    root = "parijān" if fam == "pj" else ROOT_OF[fam]
    pre = PJ_PRE if fam == "pj" else ""
    if form == "noca":
        if neg:
            return pre + F.my_verb(root, "pres", True, "stmt", pl) + "သည်" + F.NOT_SO
        return pre + F.my_verb(root, "pres", True, "stmt", pl)
    if form == "wh":
        raise F.Miss("wh " + fam)
    return pre + F.my_verb(root, "pres", neg, form, pl)


match_seq = A.match_seq
PRO, PRO_KEYS, PLACE_PRO, INTRO = A.PRO, A.PRO_KEYS, A.PLACE_PRO, A.INTRO
PRO_T = {tuple(x.split()): x for x in PRO_KEYS}
PLACE_PRO_T = {tuple(x.split()): x for x in PLACE_PRO}


def governor(low, i):
    """the family of the predicate that governs the term at i: the next verb («na» + parijān… included) or «vattabb…»."""
    for j in range(i + 1, len(low)):
        if low[j].startswith("vattabb"):
            return "vat"
        v = verb_parse(low[j])
        if v:
            return v[0]
        if low[j] in (",", ";", ".", "?"):
            return None
    return None


def sentence_my(s):
    """One Pāli sentence (or a piece cut by «…») -> Burmese (make_ch7a.sentence_my, extended)."""
    toks = tokens(s)
    words = [w for w, _ in toks]
    low = [w.lower() for w in words]
    question = "?" in words
    pieces = []
    i = 0
    mode = "a"
    noca = False
    if low and low[0] in ("yassa", "yattha", "yo", "yato", "kattha"):
        k, j, pre = low[0], 1, ""
        if low[1:3] == ["vā", "pana"]:
            pre, j = F.VA_PANA + " ", 3
        if j < len(low) and (k, low[j]) in (("yassa", "yattha"), ("yo", "yato")):
            k, j = f"{k} {low[j]}", j + 1
        pieces.append(P(pre + INTRO[k], "intro", False))
        mode = "wh" if k == "kattha" else "q1"
        i = j
    while i < len(toks):
        w, sp = toks[i]
        lw = low[i]
        if w in (",", ";"):
            pieces[-1].t += C
            pieces[-1].comma = True
            i += 1
            continue
        if w in (".", "?"):
            if question and pieces and pieces[-1].kind in ("gap", "term", "intro"):
                pieces[-1].t += "လော" + END
            else:
                pieces[-1].t += END
            i += 1
            continue
        if w == "…":
            pieces.append(P(PE, "gap", sp))
            i += 1
            continue
        m = re.fullmatch(r"⟦(\d+)⟧", w)
        if m:                                              # a variant bracket: attached to the piece before it
            pieces[-1].t += " " + VAR_HOLD[int(m[1])]
            i += 1
            continue
        if low[i:i + 2] == ["no", "ca"]:
            pieces.append(P(F.BUT, "but", sp))
            noca = True
            i += 2
            k = match_seq(low, i, PRO_T)
            if k:
                pieces.append(P(PRO[" ".join(k)], "pro"))
                i += len(k)
            continue
        if lw in A.ANS and (i + 1 == len(words) or words[i + 1] in (".", "…")):
            pieces.append(P(A.ANS[lw], "ans", sp))
            i += 1
            continue
        if lw == "na" and i + 1 < len(low) and low[i + 1] in ("vattabbo", "vattabbā"):
            if [x.lower() for x in words[i + 3:i + 6:2]] != ["vā", "vā"] or not all(
                    re.fullmatch(r'"\w+"ti', x) for x in words[i + 2:i + 5:2]):
                raise F.Miss("na vattabbo: " + s)
            qs = [x[1:-3] for x in words[i + 2:i + 5:2]]
            pieces.append(P(vattabba_my(*qs), "vat", sp))
            i += 6
            continue
        if lw == "na" and i + 1 < len(low) and verb_parse(low[i + 1]) and verb_parse(low[i + 1])[0] == "pj":
            fam, _n, pl, _q = verb_parse(low[i + 1])
            pieces.append(P(verb_my(fam, True, pl, form_of(mode, noca)), "verb", sp, comma=False))
            noca = False
            i += 2
            continue
        k = match_seq(low, i, LEAVE)
        if k:
            mem, sp0 = [], sp
            while (k := match_seq(low, i, LEAVE)):
                mem.append(LEAVE[k])
                i += len(k)
            if low[i:i + 3] != ["ṭhapetvā", "avasesā", "puggalā"]:
                raise F.Miss("ṭhapetvā: " + s)
            i += 3
            pieces.append(P(leave_my(mem), "who", sp0))
            continue
        k = match_seq(low, i, WHO)
        if k:
            pieces.append(P(A.who_my(*WHO[k]), "who", sp))
            i += len(k)
            continue
        if lw == "sabbattha":
            pieces.append(P(A.SABBATTHA, "place", sp))
            i += 1
            continue
        if match_seq(low, i, A.PLACE):
            keys, sp0 = [], sp
            while (k := match_seq(low, i, A.PLACE)):
                keys.append(k)
                i += len(k)
            kp = match_seq(low, i, PLACE_PRO_T)
            if not kp:
                raise F.Miss("places without ettha / tattha / tato: " + s)
            i += len(kp)
            pieces.append(P(f"{A.places_my(keys)} {A.NAMELY} {A.HERE_P if kp == ('ettha',) else A.THERE_P}", "place",
                            sp0))
            continue
        k = match_seq(low, i, PRO_T)
        if k:
            if mode != "q1" or not pieces or pieces[-1].kind != "verb":
                raise F.Miss(f"pronoun «{' '.join(k)}» out of place: {s}")
            pieces.append(P(PRO[" ".join(k)], "corr", sp))
            mode = "q2"
            i += len(k)
            continue
        m = A.TERM_RE.match(lw)
        if m:
            case, ca = A.ENDING[m[2]]
            if case == "nom" and governor(low, i) in ("pah", "vat"):
                case = "acc"                             # pahīno / na vattabbo: «Xကို ပယ်ပြီး ဖြစ်၏» (pi-4)
            if i + 1 < len(low) and low[i + 1] == "ca":
                ca = True
                i += 1
            pieces.append(P(A.STEM[m[1]] + A.CASE_MY[case] + (ALSO if ca else ""), "term", sp, ca=ca))
            i += 1
            continue
        if lw == "tadekaṭṭhaṃ":
            pieces.append(P(A.TADEKA, "tadeka", sp))
            i += 1
            continue
        v = verb_parse(lw)
        if v:
            fam, neg, pl, _q = v
            pieces.append(P(verb_my(fam, neg, pl, form_of(mode, noca)), "verb", sp, comma=False))
            noca = False
            i += 1
            continue
        raise F.Miss(f"token {w!r} in: {s}")
    for j, p in enumerate(pieces):
        if j:
            q = pieces[j - 1]
            if not getattr(q, "comma", False) and not q.t.endswith((C, END)):
                if q.kind == "term" and q.ca and p.kind == "term":
                    q.t += C
                elif q.kind == "verb" and p.kind in ("term", "corr", "who", "tadeka"):
                    q.t += C
    out = ""
    for j, p in enumerate(pieces):
        out += (" " if (j and p.sp) else "") + p.t
    return out


def form_of(mode, noca):
    return {"q1": "cl", "q2": "q", "wh": "wh"}.get(mode, "noca" if noca else "stmt")


# =====================================================================================================================
# dhātupucchā (7-10) and dhātuvisajjanā (7-11) sentences
# =====================================================================================================================
_DH = r"(?:kāma|rūpa|arūpa)dhātu"
WHO_RE = re.compile(rf"^(?P<from>(?:na )?{_DH}yā(?: na {_DH}yā)?) cutassa "
                    rf"(?P<to>(?:na )?{_DH}ṃ(?: na {_DH}ṃ)?) upapajjantassa (?P<rest>.+)$")
NO_UPA = re.compile(rf"^(?P<from>(?:na )?{_DH}yā(?: na {_DH}yā)?) cutassa "
                    rf"(?P<to>(?:na )?{_DH}yā(?: na {_DH}yā)?) upapatti nāma natthi, heṭṭhā upapajjamāno "
                    rf"kāmadhātuṃyeva upapajjati, (?P<rest>.+)$")


def dh_list(s):
    """'Na kāmadhātuyā na arūpadhātuyā' / 'na rūpadhātuṃ' / 'Kāmadhātuyā' -> [('kāma', True), …]."""
    out = []
    for m in re.finditer(rf"(?:(?P<na>[Nn]a) )?(?P<k>kāma|rūpa|arūpa)dhātu(?:yā|ṃ)", s[0].lower() + s[1:]):
        out.append((m["k"], bool(m["na"])))
    if " ".join(("na " if n else "") + k + "dhātu" for k, n in out) != re.sub(r"(?<=dhātu)(?:yā|ṃ)", "",
                                                                                s[0].lower() + s[1:]):
        raise F.Miss("dhātu phrase: " + s)
    return out


def who_dh(m):
    """«Xမှ စုတေ၍ Y၌ ပြန်လည် ဖြစ်ပေါ်ဆဲသူ» (pi-5 ^5-65 «X မှ သေ၍ Y ၌ ပြန်လည် ဖြစ်ပေါ်»; cavati «စုတေ», sample)."""
    return f"{dhatu_my(dh_list(m['from']))}{F.ABL} {CAVATI}၍ {dhatu_my(dh_list(m['to']))}{F.LOC} {UPAPAJJ}ဆဲ{ONE}"


def ans_clause(c, first, who):
    """'kassaci satta anusayā anusenti' / 'satteva anusayā anusenti' / 'anusayā bhaṅgā natthi'."""
    m = re.fullmatch(r"kassaci (?P<n>satta|pañca|tayo) anusayā anusenti", c)
    if m:
        lead = f"{who} {SOME_OF}{F.DAT}" if first else SOME
        return f"{lead} {ANUSAYA_W} {NUM_A[m['n']]} {anu_v(False, 'stmt')}"
    if c == "satteva anusayā anusenti":
        lead = f"{who}{F.DAT} " if first and who else ""
        return f"{lead}{ANUSAYA_W} {NUM_A['satta']}{A.EVA} {anu_v(False, 'stmt')}"
    if c == "anusayā bhaṅgā natthi":
        return f"{BHANGA}သော {ANUSAYA_W} {F.NEGV[F.HAVE]}"
    raise F.Miss("dhātuvisajjanā clause: " + c)


def dhatu_sentence(s):
    """one dhātupucchā / dhātuvisajjanā sentence -> Burmese, or None."""
    body_, end = s[:-1], s[-1]
    if end not in ".?":
        return None
    body_ = body_[0].lower() + body_[1:]
    m = WHO_RE.match(body_)
    if m:
        who = who_dh(m)
        rest = m["rest"]
        q = re.fullmatch(r"kati anusayā anusenti, kati anusayā nānusenti, kati anusayā bhaṅgā", rest)
        if q:
            k = f"{ANUSAYA_W} {KATI}"
            return (f"{who}{F.DAT} {k} {anu_v(False, 'stmt').removesuffix('သည်')}{A.WH}{C} {k} "
                    f"{anu_v(True, 'stmt')}{A.WH}{C} {k} {BHANGA}ကြ{A.WH}{END}")
        cl = re.split(r", |; ", rest)
        seps = re.findall(r", |; ", rest)
        if seps[-1] != "; " or cl[-1] != "anusayā bhaṅgā natthi":
            raise F.Miss("dhātuvisajjanā: " + s)
        out = [ans_clause(c, j == 0, who) for j, c in enumerate(cl)]
        return f"{C} ".join(out) + END
    m = NO_UPA.match(body_)
    if m:
        frm, to = dhatu_my(dh_list(m["from"])), dhatu_my(dh_list(m["to"]))
        head = (f"{frm}{F.ABL} {CAVATI}{ONE}{F.DAT} {to}{F.LOC} {UPAPATTI} {NAMA_NATTHI}{C} {HETTHA} {UPAPAJJ}ဆဲ{ONE}"
                f"သည် {A.KAMA}{F.LOC}{A.EVA} {UPAPAJJ}သည်")
        cl = re.split(r", |; ", m["rest"])
        return f"{head}{C} " + f"{C} ".join(ans_clause(c, False, "") for c in cl) + END
    return None


# =====================================================================================================================
# lines
# =====================================================================================================================
SPLIT = F.SPLIT
NOTE_RE = re.compile("|".join(re.escape(k) for k in sorted(NOTES, key=len, reverse=True)))
VAR_HOLD = []
VITTH_END = re.compile(r"^(?P<pre>.*?) \((?P<v>[Vv])itthāretabbaṃ\)\.$")


def sentences_my(sg):
    out = []
    for x in SPLIT.split(sg.strip()):
        r = dhatu_sentence(x)
        out.append(r if r is not None else sentence_my(x))
    return " ".join(out)


LINES = {"9": "9"}         # 7-10 ^6-7-311: a bare «9» line (source; kept as the digit)


def body(line):
    if line in COLO:
        return COLO[line]
    if line in LINES:
        return LINES[line]
    line = unslip(line)
    if line in COLO:
        return COLO[line]
    VAR_HOLD.clear()

    def keep_var(m):
        if m[1] not in VARIANT:
            raise F.Miss("variant: " + m[1])
        VAR_HOLD.append(VARIANT[m[1]])
        return f" ⟦{len(VAR_HOLD) - 1}⟧"
    line = re.sub(r" \[([^\]]*)\]", keep_var, line)
    m = VITTH_END.match(line)
    if m:                                  # «… X (vitthāretabbaṃ).» / «… Āmantā. (Vitthāretabbaṃ).»
        pre = m["pre"]
        note = NOTES[f"({m['v']}itthāretabbaṃ)"]
        if pre.endswith("."):
            return f"{body(pre)} {note}{END}"
        return f"{body(pre + '.').removesuffix(END)} {note}{END}"
    notes = []

    def keep_note(m):
        notes.append(NOTES[m[0]])
        return f"⟪{len(notes) - 1}⟫"
    line = NOTE_RE.sub(keep_note, line)
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
        out.append(lead + sentences_my(sg) + trail)
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
    if re.search(r"[A-Za-zāīūṃṅñṭḍṇḷ⟦⟧⟪⟫]", re.sub(r"\[[^\]]*\]", "", out.replace(bid, ""))):
        raise F.Miss("Pāli left in: " + out)
    return out


def translate_text(text):
    return "\n".join(translate_line(l) for l in text.splitlines()) + "\n"


line_check = A.line_check


def run(name):
    src = (PALI / name).read_text(encoding="utf-8-sig")
    out = translate_text(src)
    nbad = 0
    P_ = [l for l in src.splitlines() if l.strip()]
    M_ = [l for l in out.splitlines() if l.strip()]
    if len(P_) != len(M_):
        print(f"{name}: {len(P_)} vs {len(M_)} lines")
        nbad += 1
    for i, (p, m) in enumerate(zip(P_, M_), 1):
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
        except (F.Miss, KeyError, ValueError, IndexError, AttributeError) as ex:
            n += 1
            print(f"{name}:{i} {type(ex).__name__}: {str(ex)[:300]}")
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
