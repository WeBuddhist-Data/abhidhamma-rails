"""Burmese zero-shot of pi-6 ch. 7, first group (Anusayayamaka, «ကိန်းအောင်းခြင်းများကို အတွဲလိုက် မေးဖြေခြင်း»):
7-01 … 7-05 (uppattiṭṭhāna, anusayavāra, sānusayavāra, pajahanavāra anuloma).

usage: python3 -I -X utf8 make_ch7a.py [7-01 7-02 …] [--misses]   (no chapter = all five)
Every line is generated from the Pāli: my6_formulas.py is imported (never edited; its tables are extended IN MEMORY
here only) and the anusaya tables below (TABLES, kept at the top for the agent of 7-06 … 7-11) feed one token
translator (sentence_my). The Pāli order of these frames is the Burmese order (question «yassa X V tassa Y V?»,
answer «WHO PLACES PRO X V, no ca PRO Y V.»), so each Pāli token (or fixed token group) gives one Burmese piece, the
verb form set by its place (first clause of a question, question verb, statement, after «no ca»). Reused values are
read from / checked against the FINAL pi-1 … pi-5 rails texts at import (F.FINAL / F.witness). A token that no table
knows stops the run (F.Miss): nothing is guessed. Each line is checked against its Pāli (line_check, as make_ch3.py);
a chapter file is written only when every line passed. --misses lists unmatched lines and writes nothing.
New strings are logged in notes-ch7a.md.
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
NAMES_OUT = [f"7-0{i}-anusayayamaka.md" for i in range(1, 6)]
C, END, PE = F.C, F.END, F.PE
AND, ALSO, OBJ = F.AND, "လည်း", "ကို"

# =====================================================================================================================
# TABLES (anusaya chapter; the agent of 7-06 … 7-11 imports or copies these)
# =====================================================================================================================
# --- the seven latent tendencies: the pi-2 list (^2-816 «Sattānusayā – …»; also ^2-949) --------------------------------
def _seven():
    f, p, m = F.FINAL.seg("2", "^2-816")
    pl = re.search(r"Sattānusayā – (.+?)\. ", p[0])[1].split(", ")
    mh, ml = re.search(r"(ကိန်းအောင်းခြင်း ခုနစ်ပါး) – (.+?)။", m[0]).groups()
    ml = ml.split(f"{C} ")
    if len(pl) != 7 or len(ml) != 7:
        raise F.Miss("seven anusayas")
    f2, p2, m2 = F.FINAL.seg("2", "^2-949")
    for x, y in zip(pl, ml):
        if x not in " ".join(p2).lower() or y not in " ".join(m2):
            raise F.Miss(f"^2-949 {x} / {y}")
        F.WITNESS.setdefault(x, ("2", "^2-816", y))
    F.WITNESS.setdefault("Sattānusayā", ("2", "^2-816", mh))
    return mh, dict(zip(pl, ml))


ANUSAYA_H, ANUSAYA = _seven()       # «ကိန်းအောင်းခြင်း ခုနစ်ပါး», {kāmarāgānusayo: «ကာမရာဂ ကိန်းအောင်းခြင်း», …}
#   kāmarāgānusayo «ကာမရာဂ ကိန်းအောင်းခြင်း», paṭighānusayo «မုန်းတီးမှု ကိန်းအောင်းခြင်း», mānānusayo «မာန …»,
#   diṭṭhānusayo «အယူ …», vicikicchānusayo «ယုံမှားမှု …», bhavarāgānusayo «ဘဝရာဂ …», avijjānusayo «အမှန်ကို မသိမှု …»
ANUSAYA_W = W("1", "^1-1065", "anusay", "ကိန်းအောင်းခြင်း", key="anusaya")
STEM = {k[:-1]: v for k, v in ANUSAYA.items()}          # 'kāmarāgānusay' -> Burmese
# surface ending -> (case, fused «ca»): nom «X», ins «X» (before sānusaya / niranusaya), acc «Xကို»
ENDING = {"o": ("nom", False), "ena": ("ins", False), "aṃ": ("acc", False), "añca": ("acc", True)}
CASE_MY = {"nom": "", "ins": "", "acc": OBJ}
TERM_RE = re.compile(r"^(" + "|".join(sorted(STEM, key=len, reverse=True)) + r")(" + "|".join(
    sorted(ENDING, key=len, reverse=True)) + r")$")

# --- verbs: anuseti (lie latent), sānusaya / niranusaya (having / free of), pajahati (abandon) -------------------------
F.VERB["anuset"] = W("2", "^2-816", "anuseti", "ကိန်းအောင်း", key="anuseti")        # «… ကိန်းအောင်း၏» (pi-2)
W("4", "^4-114", "na ciraṃ dīgharattaṃ anuseti", "မကိန်းအောင်း", key="nānuseti")     # negative «မကိန်းအောင်း» (pi-4)
F.VERB["pajah"] = W("5", "^5-390", "pajahati", "ပယ်", key="pajahati")                 # «Xကို ပယ်သည်» (pi-5)
SA_N = W("5", "^5-606", "sānusayo", "ကိန်းအောင်းခြင်း ရှိသူ", key="sānusayo")[len(ANUSAYA_W) + 1:]   # «ရှိသူ»
NIR_N = "မ" + SA_N                  # niranusayo «… မရှိသူ» (NEW: nir- = «မရှိ»)
PL_N = "များ"                      # sānusayā / niranusayā (plural predicate noun) «… ရှိသူများ»
VERB_RE = {
    "anu": re.compile(r"^(?P<neg>nā|a)nuse(?P<pl>t|nt)(?P<q>i|īti)$"),          # anuseti / nānusentīti …
    "sa": re.compile(r"^(?P<neg>sā|nira)nusay(?P<pl>o|ā)(?P<q>ti)?$"),         # sānusayo / niranusayoti …
    "pa": re.compile(r"^(?P<neg>nap|)pajah(?P<pl>a|a?n)(?P<q>ti|tīti)$"),       # pajahati / pajahatīti / nappajahati
}
ROOT_OF = {"anu": "anuset", "pa": "pajah"}

# --- persons: Pāli tokens -> (Burmese base, case, plural, eva) -------------------------------------------------------
ANAGAMI = W("4", "^4-M-7", "Anāgāmī", "အနာဂါမ်", key="anāgāmī")
ARAHA = W("4", "^4-M-7", "Arahā", "ရဟန္တာ", key="arahā")
PUTHU = W("1", "^1-1007", "puthujjan", "ပုထုဇဉ်", key="puthujjana")
ATTHAMA = W("5", "^5-368", "Aṭṭhamakassa puggalassa", "အဋ္ဌမ ပုဂ္ဂိုလ်", key="aṭṭhamaka")      # the eighth person
W("2", "^2-1029", "agga", "အမြတ်ဆုံး", key="agga")
W("2", "^2-809", "samaṅgī", "ပြည့်စုံသော", key="samaṅgī")
W("1", "^1-M1-16", "magg", "မဂ်", key="magga")
AGGA_SAM = "အမြတ်ဆုံး မဂ်နှင့် ပြည့်စုံသူ"                    # aggamaggasamaṅgī (as make_ch3.py)
PUGGALA = F.PUGGALA                                         # «ပုဂ္ဂိုလ်»
COUNT = {2: W("4", "^4-M-8", "Dve puggalā", f"{PUGGALA} နှစ်ယောက်", key="dve puggalā"),
         3: W("4", "^4-M-9", "Tayo puggalā", f"{PUGGALA} သုံးယောက်", key="tayo puggalā"),
         4: W("4", "^4-M-10", "Cattāro puggalā", f"{PUGGALA} လေးယောက်", key="cattāro puggalā")}
W("4", "^4-M-8", "Dvinnaṃ puggalānaṃ", f"{PUGGALA} နှစ်ယောက်တို့", key="dvinnaṃ puggalānaṃ")
EVA = W("5", "^5-241", "arahattaṃyeva", "ပင်", key="-eva")
THAT_P = f"ထို{PUGGALA}"                                     # so / te puggala «ထိုပုဂ္ဂိုလ်»
PL = "တို့"
WHO = {   # lower-case Pāli token tuple -> (Burmese base, case 'dat' (anuseti) / 'nom' (sānusaya, pajahati), plural, eva)
    ("anāgāmissa",): (ANAGAMI, "dat", False, False), ("anāgāmī",): (ANAGAMI, "nom", False, False),
    ("arahato",): (ARAHA, "dat", False, False), ("arahā",): (ARAHA, "nom", False, False),
    ("puthujjanassa",): (PUTHU, "dat", False, False), ("puthujjano",): (PUTHU, "nom", False, False),
    ("aṭṭhamakassa",): (ATTHAMA, "dat", False, False), ("aṭṭhamako",): (ATTHAMA, "nom", False, False),
    ("aggamaggasamaṅgissa",): (AGGA_SAM, "dat", False, False), ("aggamaggasamaṅgī",): (AGGA_SAM, "nom", False, False),
    ("dvinnaṃ", "puggalānaṃ"): (COUNT[2], "dat", True, False), ("dve", "puggalā"): (COUNT[2], "nom", True, False),
    ("tiṇṇaṃ", "puggalānaṃ"): (COUNT[3], "dat", True, False), ("tayo", "puggalā"): (COUNT[3], "nom", True, False),
    ("catunnaṃ", "puggalānaṃ"): (COUNT[4], "dat", True, False), ("cattāro", "puggalā"): (COUNT[4], "nom", True, False),
    ("tesaññeva", "puggalānaṃ"): (THAT_P, "dat", True, True), ("tasseva", "puggalassa"): (THAT_P, "dat", False, True),
    ("teva", "puggalā"): (THAT_P, "nom", True, True), ("sveva", "puggalo"): (THAT_P, "nom", False, True),
}
CASE_P = {"dat": F.DAT, "nom": "သည်"}                       # «…အား» / «…သည်»


def who_my(base, case, pl, eva):
    """«ပုဂ္ဂိုလ် သုံးယောက်တို့အား», «ထိုပုဂ္ဂိုလ်တို့အားပင်», «အနာဂါမ်သည်», «ထိုပုဂ္ဂိုလ်သည်ပင်»."""
    return f"{base}{PL if pl else ''}{CASE_P[case]}{EVA if eva else ''}"


# --- places (the planes and feelings where a tendency lies latent): Pāli token tuple -> Burmese noun -----------------
KAMA = W("2", "^2-991", "Kāmadhātuyā", "ကာမဘုံ", key="kāmadhātu (plane)")
RUPA_B = W("2", "^2-993", "Rūpadhātuyā", "သိမ်မွေ့သော ရုပ်ဘုံ", key="rūpadhātu (plane)")
ARUPA_B = W("2", "^2-995", "Arūpadhātuyā", "ရုပ်မရှိသော ဘုံ", key="arūpadhātu (plane)")
VEDANA = F.PT["vedanā"][0]                                     # «ခံစားမှု»
DUKKHA_V = W("1", "^1-M1-2", "dukkhāya vedanāya", f"နာကျင်သော {VEDANA}", key="dukkhā vedanā")
NUM_P = {"dvīsu": W("1", "^1-1441", "dvīsu", "နှစ်ပါး", key="dvīsu"),
         "tīsu": W("1", "^1-1475", "tīsu bhūmīsu", "သုံးပါး", key="tīsu")}
W("1", "^1-1475", "tīsu bhūmīsu", "ဘုံ သုံးပါးရှိ", key="X-loc + noun «Xရှိ …»")       # «ဘုံ သုံးပါးရှိ ကုသိုလ်စိတ်»
APARI = W("1", "^1-M2-96", "apariyāpannā", "ဘဝဘုံတို့၌ အကျုံးမဝင်သော", key="apariyāpanna")
PARI = W("1", "^1-283", "maggapariyāpannaṃ", "၌ အကျုံးဝင်သော", key="-pariyāpanna «… ၌ အကျုံးဝင်သော»")
SAKKAYA = W("1", "^1-1007", "sakkāyadiṭṭhi", "ကိုယ်", key="sakkāya")
SABBA = W("5", "^5-334", "sabbe te", "အားလုံး", key="sabba")
TH = F.THING                                                 # «အရာ»
PLACE = {
    ("kāmadhātuyā", "dvīsu", "vedanāsu"): f"{KAMA}ရှိ {VEDANA} {NUM_P['dvīsu']}",
    ("kāmadhātuyā", "tīsu", "vedanāsu"): f"{KAMA}ရှိ {VEDANA} {NUM_P['tīsu']}",
    ("kāmadhātuyā",): KAMA,
    ("dukkhāya", "vedanāya"): DUKKHA_V,
    ("rūpadhātuyā",): RUPA_B,
    ("arūpadhātuyā",): ARUPA_B,
    ("apariyāpanne",): f"{APARI} {TH}",
    ("sabbasakkāyapariyāpannesu", "dhammesu"): f"{SAKKAYA}{PARI} {F.DHAMMA} {SABBA}",
}
SABBATTHA = "နေရာတိုင်း၌"                                    # sabbattha (as make_ch3.py / make_ch6-8.py notes)
NAMELY = "ဟူသော"                                             # «PLACES ဟူသော ဤနေရာ၌ / ထိုနေရာ၌» (ettha / tattha)
HERE_P, THERE_P = "ဤနေရာ၌", F.FT["tattha"]                   # ettha / tattha, tato (okāsa «နေရာ»)


def places_my(keys):
    """['rūpadhātuyā', 'arūpadhātuyā'] -> «သိမ်မွေ့သော ရုပ်ဘုံနှင့် ရုပ်မရှိသော ဘုံ»; three or more «A၊ Bနှင့် C»."""
    its = [PLACE[k] for k in keys]
    if len(its) == 1:
        return its[0]
    return f"{C} ".join(its[:-1]) + f"{AND} " + its[-1]


# --- pronouns and correlatives (all the same Burmese in questions and after «no ca») ---------------------------------
PRO = {"tassa tattha": F.FT["tassa tattha"], "tesaṃ tattha": F.PRO["tesaṃ tattha"], "so tato": "ထိုသူသည် " + THERE_P,
       "te tato": "ထိုသူတို့သည် " + THERE_P, "tassa": F.FT["tassa"], "tesaṃ": F.PRO["tesaṃ"], "tattha": THERE_P,
       "so": "ထိုသူသည်", "te": "ထိုသူတို့သည်", "tato": THERE_P, "ettha": HERE_P}
PRO_KEYS = sorted(PRO, key=lambda k: -len(k.split()))
PLACE_PRO = {"tassa tattha", "tesaṃ tattha", "so tato", "te tato", "tattha", "tato", "ettha"}
# question intros: yassa / yattha / yo / yato (+ vā pana) (+ yattha / yato); kattha
INTRO = {"yassa": F.CL["yassa"][0], "yattha": F.CL["yattha"][0], "yassa yattha": F.CL["yassa yattha"][0],
         "yo": "အကြင်သူသည်", "yato": F.CL["yattha"][0], "yo yato": "အကြင်သူသည် " + F.CL["yattha"][0],
         "kattha": W("2", "^2-1024", "kattha upapajjanti", "မည်သည့်နေရာ၌", key="kattha")}
WH = "သနည်း"                                                 # kattha … anuseti? «… ကိန်းအောင်းသနည်း»
TADEKA = (W("2", "^2-816", "Tadekaṭṭho", "ထိုအရာနှင့် တစ်နေရာတည်း တည်ရှိ", key="tadekaṭṭha")
          + "သည့် အနေဖြင့်")                                  # tadekaṭṭhaṃ (pajahati) «… တည်ရှိသည့် အနေဖြင့်» (NEW form)

# --- headings, colophons, notes --------------------------------------------------------------------------------------
UPPATTI_T = f"{F.VERB['uppajj']}ရာ {F.OKASA}"                 # uppattiṭṭhāna «ဖြစ်ပေါ်ရာ နေရာ» (NEW)
MAHA = f"{F.VARA}ကြီး"                                        # mahāvāro «ဖော်ပြချက်ကြီး» (NEW)
SANUSAYA_W = f"{ANUSAYA_W} {SA_N}"                            # sānusaya «ကိန်းအောင်းခြင်း ရှိသူ» (pi-5)
PAJAHANA = F.VERB["pajah"] + "ခြင်း"                           # pajahana «ပယ်ခြင်း» (NEW)
PATILOMA = F.PACCANIKA                                        # paṭiloma (Yamaka negated form) = paccanīka (NEW use)
VARA_OF = {"Anusaya": F.vara(ANUSAYA_W), "Sānusaya": F.vara(SANUSAYA_W), "Pajahana": F.vara(PAJAHANA),
           "Uppattiṭṭhāna": F.vara(UPPATTI_T)}
F.H.update({
    "Uppattiṭṭhānavāro": VARA_OF["Uppattiṭṭhāna"],
    "Mahāvāro 1. anusayavāro": f"{MAHA} 1. {VARA_OF['Anusaya']}",
    "Anusayavāra": VARA_OF["Anusaya"], "Anusayavāro": VARA_OF["Anusaya"],
    "Sānusayavāro": VARA_OF["Sānusaya"], "Sānusayavāra": VARA_OF["Sānusaya"],
    "Pajahanavāro": VARA_OF["Pajahana"], "Pajahanavāra": VARA_OF["Pajahana"],
    "paṭilomapuggalo": f"{PUGGALA}{F.ALIKE} {PATILOMA}",
    "paṭilomaokāso": f"{F.OKASA}{F.ALIKE} {PATILOMA}",
    "paṭilomapuggalokāsā": f"{PUGGALA}{AND} {F.OKASA}{F.ALIKE} {PATILOMA}",
})
COLO = dict(F.COLO)
for _k, _v in VARA_OF.items():
    COLO[f"{_k}vāro."] = f"{_v}{END}"                                    # Anusayavāro. «…အလိုက် ဖော်ပြချက်။»
    COLO[f"{_k}vāre anulomaṃ."] = f"{_v}၌ {F.ANULOMA}{END}"               # «… ဖော်ပြချက်၌ အဟုတ်ပြ ပုံစံ။»
    COLO[f"{_k}vāre paṭilomaṃ."] = f"{_v}၌ {PATILOMA}{END}"
    COLO[f"{_k}vāro niṭṭhito."] = F.finished(_v)
NUMW = {"Eka": "တစ်", "Duka": "နှစ်", "Tika": "သုံး", "Catukka": "လေး", "Pañcaka": "ငါး", "Chakka": "ခြောက်"}
NOTES = {}
for _k, _v in NUMW.items():   # (Ekamūlakaṃ) «(တစ်ပါးကို အခြေခံ၍)»: based on one (two …) tendency(-ies) (NEW)
    NOTES[f"({_k}mūlakaṃ)"] = f"({_v}ပါး{F.BASED})"
    NOTES[f"({_k}mūlakaṃ )"] = f"({_v}ပါး{F.BASED} )"                  # source spacing «(Ekamūlakaṃ )» kept
LINES = {   # unique whole lines
    "Sattānusayā – " + ", ".join(ANUSAYA) + ".": f"{ANUSAYA_H} – " + f"{C} ".join(ANUSAYA.values()) + END,
}

# --- source slips (translated as written; read as the evident word) --------------------------------------------------
SLIPS = [
    ("kāmārāgānusayo", "kāmarāgānusayo"),       # 7-01 (two lines): «kāmārāga» for kāmarāga
    ("anusanti", "anusenti"),                   # 7-01 ^6-7-32: «anusanti» for anusenti
    ("vedanāya ariyāpanne", "vedanāya apariyāpanne"),   # 7-04: «ariyāpanne» for apariyāpanne
]


def unslip(s):
    for a, b in SLIPS:
        s = s.replace(a, b)
    return s


# =====================================================================================================================
# the token translator
# =====================================================================================================================
TOK = re.compile(r"…|[^\s…]+")
ANS = {"āmantā": F.YES[:-1], "no": F.NO[:-1], "natthi": F.NATTHI[:-1]}


class P:
    """A Burmese piece: text, kind, space before."""

    def __init__(self, t, kind, sp=True, **kw):
        self.t, self.kind, self.sp = t, kind, sp
        self.__dict__.update(kw)


def tokens(s):
    """'… anuseti, no ca …?' -> [(word, space_before)], «,» «.» «?» split off as their own tokens."""
    out = []
    for m in TOK.finditer(s):
        w, sp = m[0], m.start() > 0 and s[m.start() - 1] == " "
        tail = []
        while w and w[-1] in ",.?" and w != "…":
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
            neg = m["neg"] in ("nā", "nira", "nap")
            pl = m["pl"] in ("nt", "ā", "an", "n")
            return fam, neg, pl, m["q"] in ("īti", "tīti") or (fam == "sa" and m["q"] == "ti")
    return None


def verb_my(fam, neg, pl, form):
    """form: 'cl' (first clause of a question), 'q' (question), 'wh' (kattha question), 'stmt', 'noca' (after «no ca»:
    a positive verb negated, a negative one «… မVသည်ကား မဟုတ်»)."""
    ko = "ကြ" if pl else ""
    if fam == "sa":
        n = (NIR_N if neg else SA_N) + (PL_N if pl else "")
        return {"stmt": f"{n} {F.BE}{ko}သည်", "cl": f"{n} {F.BE}{ko}၏", "q": f"{n} {F.BE}{ko}သလော",
                "noca": f"{n} {F.NEGV[F.BE]}{ko}"}[form]
    root = ROOT_OF[fam]
    if form == "wh":
        return F.my_verb(root, "pres", neg, "stmt", pl).removesuffix("သည်") + WH
    if form == "noca":
        if neg:
            return F.my_verb(root, "pres", True, "stmt", pl) + "သည်" + F.NOT_SO
        return F.my_verb(root, "pres", True, "stmt", pl)
    return F.my_verb(root, "pres", neg, form, pl)


def match_seq(low, i, table):
    for k in sorted(table, key=lambda k: -len(k)):
        if tuple(low[i:i + len(k)]) == k:
            return k
    return None


def sentence_my(s):
    """One Pāli sentence (or a piece cut by «…») -> Burmese."""
    toks = tokens(s)
    words = [w for w, _ in toks]
    low = [w.lower() for w in words]
    question = "?" in words
    pieces = []
    i = 0
    mode = "a"                                   # 'q1' / 'q2' (question before / after the correlative), 'wh', 'a'
    noca = False
    # --- intro of a question
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
        if w in (",",):
            pieces[-1].t += C
            pieces[-1].comma = True
            i += 1
            continue
        if w in (".", "?"):
            if question and pieces and pieces[-1].kind in ("gap", "term", "intro"):
                pieces[-1].t += "လော" + END                 # a question cut before its verb «…လော။»
            else:
                pieces[-1].t += END
            i += 1
            continue
        if w == "…":
            pieces.append(P(PE, "gap", sp))
            i += 1
            continue
        if low[i:i + 2] == ["no", "ca"]:
            pieces.append(P(F.BUT, "but", sp))
            noca = True
            i += 2
            k = match_seq(low, i, {tuple(x.split()): x for x in PRO_KEYS})
            if k:
                pieces.append(P(PRO[" ".join(k)], "pro"))
                i += len(k)
            continue
        if lw in ANS and (i + 1 == len(words) or words[i + 1] in (".", "…")):
            pieces.append(P(ANS[lw], "ans", sp))
            i += 1
            continue
        k = match_seq(low, i, WHO)
        if k:
            pieces.append(P(who_my(*WHO[k]), "who", sp))
            i += len(k)
            continue
        if lw == "sabbattha":
            pieces.append(P(SABBATTHA, "place", sp))
            i += 1
            continue
        if match_seq(low, i, PLACE):
            keys, sp0 = [], sp
            while (k := match_seq(low, i, PLACE)):
                keys.append(k)
                i += len(k)
            kp = match_seq(low, i, {tuple(x.split()): x for x in PLACE_PRO})
            if not kp:
                raise F.Miss("places without ettha / tattha / tato: " + s)
            i += len(kp)
            pieces.append(P(f"{places_my(keys)} {NAMELY} {HERE_P if kp == ('ettha',) else THERE_P}", "place", sp0))
            continue
        k = match_seq(low, i, {tuple(x.split()): x for x in PRO_KEYS})
        if k:
            if mode != "q1" or not pieces or pieces[-1].kind != "verb":
                raise F.Miss(f"pronoun «{' '.join(k)}» out of place: {s}")
            pieces.append(P(PRO[" ".join(k)], "corr", sp))
            mode = "q2"
            i += len(k)
            continue
        m = TERM_RE.match(lw)
        if m:
            case, ca = ENDING[m[2]]
            if i + 1 < len(low) and low[i + 1] == "ca":
                ca = True
                i += 1
            pieces.append(P(STEM[m[1]] + CASE_MY[case] + (ALSO if ca else ""), "term", sp, ca=ca))
            i += 1
            continue
        if lw == "tadekaṭṭhaṃ":
            pieces.append(P(TADEKA, "tadeka", sp))
            i += 1
            continue
        v = verb_parse(lw)
        if v:
            fam, neg, pl, _q = v
            if mode == "q1":
                form = "cl"
            elif mode in ("q2",):
                form = "q"
            elif mode == "wh":
                form = "wh"
            else:
                form = "noca" if noca else "stmt"
            noca = False
            pieces.append(P(verb_my(fam, neg, pl, form), "verb", sp, comma=False))
            i += 1
            continue
        raise F.Miss(f"token {w!r} in: {s}")
    # --- join: list «၊» between «ca» members, clause «၊» after a verb that another clause follows
    out = ""
    for j, p in enumerate(pieces):
        if j:
            q = pieces[j - 1]
            if not getattr(q, "comma", False) and not q.t.endswith((C, END)):
                if q.kind == "term" and q.ca and p.kind == "term":
                    q.t += C
                elif q.kind == "verb" and p.kind in ("term", "corr", "who", "tadeka"):
                    q.t += C
    for j, p in enumerate(pieces):
        out += (" " if (j and p.sp) else "") + p.t
    return out


SPLIT = F.SPLIT
NOTE_RE = re.compile("|".join(re.escape(k) for k in sorted(NOTES, key=len, reverse=True)))


def body(line):
    if line in COLO:
        return COLO[line]
    if line in LINES:
        return LINES[line]
    line = unslip(line)
    if line in LINES:
        return LINES[line]
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
        out.append(lead + " ".join(sentence_my(x) for x in SPLIT.split(sg.strip())) + trail)
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


# ===================================================================================== per-line check (make_ch3.py)
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
        except (F.Miss, KeyError, ValueError, IndexError) as ex:
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
