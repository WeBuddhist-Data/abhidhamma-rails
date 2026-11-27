"""Burmese zero-shot of pi-3 (Dhātukathā, «ဓာတ်များအကြောင်း ဆွေးနွေးခြင်း»): chapters 3, 4, 5, 6, 8, 9
(Dutiya-, Tatiya-, Catuttha-, Pañcama-, Sattama-, Aṭṭhamanayo).

usage: python3 -I -X utf8 make_ch3-6-8-9.py [chapter ...]
Every line is generated from the Pāli by my3_formulas.translate_line() (read only, imported), extended IN MEMORY
here: the frames of these methods (one rule in F.EXTRA_RULES), the instrumental -> nominative table of the topic
names (the Burmese names themselves come from F.subject(), i.e. the FINAL pi-1 / pi-2 Burmese), the summary verses
(F.FIXED), number words, variant labels. A sentence no frame matches stops the run (F.Miss), nothing is guessed. A
chapter is written only when every line passed. Every new string is logged in notes-ch3-6-8-9.md.

Frames (one per Pāli formula, identical everywhere):
  X-ena ye dhammā        = «Xနှင့်» (chain items joined by «… »; the relative head is said once, after the predicate)
  khandhasaṅgahena (a)saṅgahitā āyatanasaṅgahena … dhātusaṅgahena … =
      «အစုအဝေး အကျုံးဝင်ခြင်းဖြင့် အကျုံး(မ)ဝင်၊ အာရုံခံ နယ်ပယ် အကျုံးဝင်ခြင်းဖြင့် …၊ ဓာတ် အကျုံးဝင်ခြင်းဖြင့် …»
      (= make_ch12-15.py rel_my)
  … ye dhammā sampayuttā / vippayuttā = «… ယှဉ်တွဲ / ကင်းကွာ»
  relative head «ye … dhammā, te dhammā» = «…သော သဘောတရားများ၊ ထိုသဘောတရားများသည်» (pi-1 ^1-1115, ^1-1091)
  tehi dhammehi ye dhammā = «ထိုသဘောတရားတို့နှင့် …သော သဘောတရားများ» (pi-1 ^1-1115, identical Pāli)
  te dhammā katihi … (a)saṅgahitā? = «ထိုသဘောတရားများသည် အစုအဝေး မည်မျှ၊ … ဓာတ် မည်မျှတို့တွင် အကျုံး(မ)ဝင်ကြသနည်း။»
  te dhammā katihi … sampayuttā(ti) / vippayuttā? = «… ဓာတ် မည်မျှတို့နှင့် ယှဉ်တွဲ / ကင်းကွာကြသနည်း။»
  Te dhammā COUNTS (a)saṅgahitā. = «ထိုသဘောတရားများသည် COUNTSတို့တွင် အကျုံးဝင်ကြသည် / အကျုံးမဝင်ကြ။» (F.counts_my)
  Te dhammā COUNTS vippayuttā. = «ထိုသဘောတရားများသည် COUNTSတို့နှင့် ကင်းကွာကြသည်။»; zero run «ကင်းကွာရာ X၊ Y မရှိ»
  ; COUNTS kehici vippayuttā = «၊ COUNTSတို့၏ အချို့နှင့် ကင်းကွာကြသည်»
  Natthi. = «မရှိ။»
"""
import pathlib
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import my3_formulas as F  # noqa: E402

ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-3_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-3-burmese-plain-zeroshot_split_chapters"
NAMES_OUT = ["3-dutiyanayo.md", "4-tatiyanayo.md", "5-catutthanayo.md", "6-pancamanayo.md", "8-sattamanayo.md",
             "9-atthamanayo.md"]

C, END, KH, AY, DH = F.C, F.END, F.KHANDHA, F.AYATANA, F.DHATU

# ===================================================================================== new table entries (in memory)
F.NUM_MY.update({30: "သုံးဆယ်", 47: "လေးဆယ့်ခုနစ်"})          # tiṃsa, sattacattālīsa (verses)
F.TERM_ALIAS.update({"paccupannārammaṇā": "paccuppannārammaṇā",    # pi-3 spelling ^3-210
                     "na hetusahetukā": "na hetū sahetukā"})         # pi-3 compound ^3-213 (variants: na hetū …)
F._add("avijjāpaccayā saṅkhāro", F.tattha("2", "avijjāpaccayā saṅkhāro", "^2-249"), "sg")   # singular, ^3-182 …

# ===================================================================================== frame words (new)
BY = F.NOUN_W["saṅgaho"] + "ဖြင့်"   # khandhasaṅgahena = «အစုအဝေး အကျုံးဝင်ခြင်းဖြင့်» (as make_ch12-15.py)
WITH = "နှင့်"                       # X-ena (sampayuttā / saṅgahitā / vippayuttā) = «Xနှင့်»
REL = f"သော {F.DHP}"                # «ye … dhammā» (pi-1 ^1-1115 «… ယှဉ်တွဲသော သဘောတရားများ၊»)
TE = f"ထို{F.DHP}"                  # te dhammā (pi-1 ^1-1091 «ထိုသဘောတရားများသည်»)
TEHI = f"ထို{F.DH}တို့" + WITH        # tehi dhammehi (pi-1 ^1-1115 «ထိုသဘောတရားတို့နှင့်», identical Pāli)
SV = {"sampayuttā": F.SAMPAYUTTA_V, "vippayuttā": F.VIPPAYUTTA_V}
SOME = "၏ အချို့"                    # kehici (by some): «… တို့၏ အချို့နှင့် ကင်းကွာကြသည်»
NATTHI = "မရှိ"                     # Natthi. (pi-1 ^1-1221 «… မရှိ»)
F.witness("1", "^1-1091", "te dhammā", TE + F.SUBJ_MARK)
F.witness("1", "^1-1115", "Tehi dhammehi ye dhammā sampayuttā", f"{TEHI} {F.SAMPAYUTTA_V}{REL}၊")
F.witness("1", "^1-1221", "Natthi", NATTHI)


def V(neg):
    return F.ASANGAHA_V if neg else F.SANGAHA_V


# ===================================================================================== topic names (instrumental)
INS = {      # instrumental (as in the source, first letter lower case) -> nominative key of F.SUBJ
    "avijjāya": "avijjā", "avijjāpaccayā saṅkhārena": "avijjāpaccayā saṅkhāro",
    "saṅkhārapaccayā viññāṇena": "saṅkhārapaccayā viññāṇaṃ", "viññāṇapaccayā nāmarūpena": "viññāṇapaccayā nāmarūpaṃ",
    "nāmarūpapaccayā saḷāyatanena": "nāmarūpapaccayā saḷāyatanaṃ", "saḷāyatanapaccayā phassena": "saḷāyatanapaccayā phasso",
    "phassapaccayā vedanāya": "phassapaccayā vedanā", "vedanāpaccayā taṇhāya": "vedanāpaccayā taṇhā",
    "taṇhāpaccayā upādānena": "taṇhāpaccayā upādānaṃ",
    "jātiyā": "jāti", "jarāya": "jarā", "maraṇena": "maraṇaṃ", "sokena": "soko", "paridevena": "paridevo",
    "dukkhena": "dukkhaṃ", "domanassena": "domanassaṃ", "upāyāsena": "upāyāso",
    "jhānena": "jhānaṃ", "satipaṭṭhānena": "satipaṭṭhānaṃ", "sammappadhānena": "sammappadhānaṃ",
    "iddhipādena": "iddhipādo", "appamaññāya": "appamaññā", "pañcahi indriyehi": "pañcindriyāni",
    "pañcahi balehi": "pañca balāni", "sattahi bojjhaṅgehi": "satta bojjhaṅgā",
    "ariyena aṭṭhaṅgikena maggena": "ariyo aṭṭhaṅgiko maggo",
    "phassena": "phasso", "vedanāya": "vedanā", "saññāya": "saññā", "cetanāya": "cetanā", "cittena": "cittaṃ",
    "adhimokkhena": "adhimokkho", "manasikārena": "manasikāro",
    "vipākadhammadhammehi": "vipākadhammadhammā", "upādādhammehi": "upādā dhammā",
}
INS_END = [("kkhandhena", "kkhandho"), ("āyatanena", "āyatanaṃ"), ("dhātuyā", "dhātu"), ("ndriyena", "ndriyaṃ"),
           ("saccena", "saccaṃ"), ("bhavena", "bhavo")]
SLIP = {"cittasahabhūmi": "cittasahabhūhi"}      # ^3-189 «Cittasahabhūmi dhammehi» (source slip, read -bhūhi)
SLIPS_SEEN = []


def ins2nom(x):
    k = x[0].lower() + x[1:]
    if k in INS:
        return INS[k]
    for a, b in INS_END:
        if k.endswith(a) and " " not in k:
            return k[:-len(a)] + b
    raise F.Miss("instrumental: " + x)


def adj_nom(x):
    """«sukhāya vedanāya sampayuttehi» / «hetūhi ceva sahetukehi ca» -> nominative plural «… sampayuttā» …."""
    out = []
    for w in x.split():
        lw = w[0].lower() + w[1:] if not out else w
        if lw in SLIP:
            SLIPS_SEEN.append(lw)
            lw = SLIP[lw]
        if lw.endswith("bhūhi"):
            out.append(lw[:-len("bhūhi")] + "bhuno")
        elif lw == "hetūhi":
            out.append("hetū")
        elif lw.endswith("īhi"):
            out.append(lw[:-len("īhi")] + "ino")
        elif lw.endswith("ehi"):
            out.append(lw[:-len("ehi")] + "ā")
        elif lw.endswith("hi"):
            raise F.Miss("adjective: " + x)
        else:
            out.append(lw)
    return " ".join(out)


VAR_KIND = {"upādānapaccayā kammabhavena": F.P1.PATHA, "punareva": F.P1.LEKHANA, "cullantaradukā": F.P1.LEKHANA,
            "tiṃsavidhanti": F.P1.LEKHANA, "dvevīsati": F.P1.PATHA, "na hetū sahetukehi": F.P1.PATHA,
            "na hetūhi sahetukehi": F.P1.PATHA}
VAR_RE = re.compile(r"(?P<t>[^\[\]()]+?) \((?P<s>[^()]+)\)")


def var_my(br):
    """«[na hetū sahetukehi (sī.), na hetūhi sahetukehi (syā. ka.)]» ->
    «[ပါဌ်ကွဲ (Sī.): na hetū sahetukehi၊ (Syā., Ka.): na hetūhi sahetukehi]» (pi-2 ^2-165 pattern)."""
    parts = br[1:-1].split(", ")
    out, kinds = [], []
    for p in parts:
        m = VAR_RE.fullmatch(p)
        if not m or m["t"] not in VAR_KIND:
            raise F.Miss("variant: " + br)
        sig = ", ".join(F.SIGLA[s] for s in m["s"].split())
        kinds.append(VAR_KIND[m["t"]])
        out.append(f"({sig}): {m['t']}")
    if len(set(kinds)) != 1:
        raise F.Miss("variant kinds: " + br)
    return f"[{kinds[0]} " + f"{C} ".join(out) + "]"


BR_RE = re.compile(r" (\[[^\]]+\])")


def item_my(piece, last):
    """One chain item «X ye dhammā» / «Xehi dhammehi ye dhammā» / bare «Saṃyojanehi» -> Burmese."""
    br = BR_RE.search(piece)
    brpos = None
    if br:
        before = piece[:br.start()]
        piece = before + piece[br.end():]
        brpos = len(before.split())
    has_ye = piece.endswith(" ye dhammā")
    x = piece[:-len(" ye dhammā")] if has_ye else piece
    has_dh = x.endswith(" dhammehi")
    if has_dh:
        x = x[:-len(" dhammehi")]
    if last and not has_ye:
        raise F.Miss("chain end without «ye dhammā»: " + piece)
    if has_dh:
        my = F.subject(adj_nom(x) + " dhammā")[0]
        if br:
            if brpos != len(x.split()):
                raise F.Miss("variant position: " + piece)
            my = my[:-len(F.DHP)] + var_my(br[1]) + " " + F.DHP
        return my + WITH if has_ye else my
    if not has_ye:                       # bare «Saṃyojanehi …»: the name without «သဘောတရားများ», no postposition
        my = F.subject(adj_nom(x) + " dhammā")[0]
        if not my.endswith(" " + F.DHP) or br:
            raise F.Miss("bare item: " + piece)
        return my[:-len(" " + F.DHP)]
    my = F.subject(ins2nom(x))[0] + WITH
    if br:
        if brpos != len(x.split()):
            raise F.Miss("variant position: " + piece)
        my += " " + var_my(br[1])
    return my


ELL_RE = re.compile(r"\s*(?:…pe…|…Pe…|…)\s*")


def chain_my(ch):
    pieces = ELL_RE.split(ch.strip())
    if any(not p for p in pieces):
        raise F.Miss("chain: " + ch)
    return f"{F.PE} ".join(item_my(p, i == len(pieces) - 1) for i, p in enumerate(pieces))


# ===================================================================================== predicates, questions, answers
PRED_S = (r"khandhasaṅgahena (?P<a>a?)saṅgahitā āyatanasaṅgahena (?P<b>a?)saṅgahitā "
          r"dhātusaṅgahena (?P<c>a?)saṅgahitā")
PRED_RE = re.compile(rf"{PRED_S}|(?P<sv>sampayuttā|vippayuttā)(?![\w])")


def pred_my(m):
    if m["sv"]:
        return SV[m["sv"]] + REL
    return f"{KH} {BY} {V(m['a'])}{C} {AY} {BY} {V(m['b'])}{C} {DH} {BY} {V(m['c'])}{REL}"


Q_RE = re.compile(r"katihi khandhehi katihāyatanehi katihi dhātūhi "
                  r"(?:(?P<neg>a?)saṅgahitā|(?P<sv>sampayuttā|vippayuttā)(?:ti)?)\?")


def q_my(m):
    if m["sv"]:
        return f"{KH} {F.KATI}{C} {AY} {F.KATI}{C} {DH} {F.KATI}တို့{WITH} {SV[m['sv']]}ကြသနည်း{END}"
    return f"{F.Q1_MY} {F.VERB[not m['neg']]['q']['pl']}{END}"


def counts_sv(cs, sv):
    """Counts with sampayutta / vippayutta: «A n-ပါး၊ B m-ပါးတို့နှင့် ကင်းကွာကြသည်», zero «ကင်းကွာရာ A၊ B မရှိ»."""
    runs = []
    for kind, n in cs:
        z = n == 0
        if runs and runs[-1][0] == z:
            runs[-1][1].append((kind, n))
        else:
            runs.append((z, [(kind, n)]))
    out = []
    for z, r in runs:
        if z:
            out.append(f"{sv}{F.WHERE} " + f"{C} ".join(F.KIND[k] for k, _ in r) + f" {F.ZERO_TAIL}")
        else:
            lst = f"{C} ".join(F.count_my(k, n) for k, n in r)
            post = WITH if len(r) == 1 and r[0][1] == 1 else "တို့" + WITH
            out.append(f"{lst}{post} {sv}ကြသည်")
    return f"{C} ".join(out)


ANS_RE = re.compile(rf"(?P<thap>{F.THAP_P} )?(?P<c>{F.COUNTS_RE.pattern}) "
                    r"(?:(?P<neg>a?)saṅgahitā|(?P<sv>sampayuttā|vippayuttā))"
                    rf"(?:; (?P<c2>{F.COUNTS_RE.pattern}) kehici (?P<sv2>vippayuttā))?\.", re.IGNORECASE)


def answer_my(body):
    """«[asaṅkhataṃ khandhato ṭhapetvā] COUNTS VERB[; COUNTS kehici vippayuttā].» (after «te dhammā»)."""
    m = ANS_RE.fullmatch(body)
    if not m:
        raise F.Miss("answer: " + body)
    cs = F.counts_parse(m["c"].strip())
    parts = [F.THAPETVA] if m["thap"] else []
    if m["sv"]:
        parts.append(counts_sv(cs, SV[m["sv"]]))
    else:
        parts.append(F.counts_my(cs, not m["neg"], "pl"))
    res = " ".join(parts)
    if m["c2"]:
        c2 = F.counts_parse(m["c2"].strip())
        if m["sv2"] != m["sv"] or any(n == 0 for _, n in c2):
            raise F.Miss("kehici: " + body)
        lst = f"{C} ".join(F.count_my(k, n) for k, n in c2)
        post = SOME if len(c2) == 1 and c2[0][1] == 1 else "တို့" + SOME
        res += f"{C} {lst}{post}{WITH} {SV[m['sv2']]}ကြသည်"
    return res + END


ELL1 = r"(?:…pe…|…Pe…|…)"


def sentence(s):
    """One sentence of these methods -> Burmese (None: not of this kind)."""
    if s == "Natthi.":
        return NATTHI + END
    m = re.fullmatch(r"Te dhammā (?P<b>.+)", s)
    if m:
        return f"{TE}{F.SUBJ_MARK} " + answer_my(m["b"])
    m = re.fullmatch(r"(?P<ch>.+ ye dhammā) ?…\.", s)            # a chain line without predicate (^3-192)
    if m and not PRED_RE.search(m["ch"]):
        return chain_my(m["ch"]) + F.PE + END
    m = PRED_RE.search(s)
    if not m or " ye dhammā" not in s[:m.start()]:
        return None
    ch = s[:m.start()].rstrip()
    if not ch.endswith(" ye dhammā"):
        raise F.Miss("predicate position: " + s)
    out = chain_my(ch) + " " + pred_my(m)
    rest = s[m.end():]
    t = re.match(rf"(?P<sep>, | )?tehi dhammehi ye dhammā(?: (?=[sv]|khandha)|(?P<ell>{ELL1}) ?)", rest)
    elided = False
    if t:
        out += (C + " " if t["sep"] == ", " else " ") + TEHI
        rest = rest[t.end():]
        if t["ell"]:
            out += F.PE
            elided = True
        else:
            m2 = PRED_RE.match(rest)
            if not m2:
                raise F.Miss("second predicate: " + s)
            out += " " + pred_my(m2)
            rest = rest[m2.end():]
    q = re.fullmatch(r", te dhammā (?P<q>.+)", rest)
    if q and not elided:
        mq = Q_RE.fullmatch(q["q"])
        if not mq:
            raise F.Miss("question: " + s)
        return out + f"{C} {TE}{F.SUBJ_MARK} " + q_my(mq)
    a = re.fullmatch(rf"(?P<ell>{ELL1})? ?te dhammā (?P<b>.+)", rest)
    if a and (a["ell"] or elided):
        return out + ("" if elided else F.PE) + f" {TE}{F.SUBJ_MARK} " + answer_my(a["b"])
    raise F.Miss("frame: " + s)


def rule(m):
    return sentence(m.group(0))


F.EXTRA_RULES.insert(0, (re.compile(r"(?s).+"), rule))


# ===================================================================================== summary verses (uddāna)
def sg(term):
    """A topic name in the singular (verses: neuter singular «…ṃ»): «… သဘောတရားများ» -> «… သဘောတရား»."""
    my = F.subject(term)[0]
    if not my.endswith(" " + F.DHP):
        raise F.Miss("sg: " + term)
    return my[:-len(F.DHP)] + F.DH


def n_(kind, n):
    return F.count_my(kind, n)


def num(n):
    return F.NUM_MY[n] + F.CL


IND = F.P1.INDRIYA
S = lambda k: F.subject(k)[0]                                       # noqa: E731
CULA, MAHA = F.heads("1", "Cūḷantaradukaṃ"), F.heads("1", "Mahantaradukaṃ")
GOCCHA = "အစု"                       # gocchaka (pi-1 Hetugocchakaṃ «အမြစ်တို့၏ အစု»)
F.witness("1", "^1-M2-6", "Hetugocchakaṃ", GOCCHA)
ANTARA = "ကြားညှပ်"                  # antara (pi-1 Cūḷantaradukaṃ / Mahantaradukaṃ «ကြားညှပ် …»)
PADA = F.PADA                        # pada = «ပုဒ်»
PACCAYAKARA = "အကြောင်းတို့၏ အခြင်းအရာ"     # paccayākāra (new)
PATICCA = S("paṭiccasamuppādo")      # paṭicca(samuppāda) in «paṭiccapadā» / «paṭicca»
UPARI = "ထို့အထက်၌"                  # upari (new)
UDDHAM = "အထက်ပိုင်း၌"               # uddhaṃ (new)
PUNA = "တဖန်"                        # puna / punadeva (new)
LABBH = "မတွေ့ရ"                     # na labbhare / na labbhanti (new)
TIKA_LOC = f"{F.TIKA}တို့တွင်"          # tikesu / tike
VITVIC = S("savitakkasavicārā dhammā").split(" ရှိသော")[0]     # vitakka-vicāra (pi-1 ^1-1000)
assert VITVIC == "စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှု"
V3 = {}
V3["Dasāyatanā sattarasa dhātuyo,"] = f"{n_('a', 10)}{C} {n_('d', 17)}{C}"
V3["Sattindriyā asaññābhavo ekavokārabhavo;"] = f"{IND} {num(7)}{C} {S('asaññābhavo')}{C} {S('ekavokārabhavo')}{C}"
V3["Paridevo sanidassanasappaṭighaṃ,"] = f"{S('paridevo')}{C} {sg('sanidassanasappaṭighā dhammā')}{C}"
V3["Anidassanaṃ punadeva [punareva (pī.)] sappaṭighaṃ upādāti."] = (
    f"{sg('anidassanā dhammā')}{C} {PUNA} {var_my('[punareva (pī.)]')} {sg('sappaṭighā dhammā')}{C} "
    f"{sg('upādā dhammā')}{END}")
V4 = {}
V4["Tayo khandhā tathā saccā, indriyāni ca soḷasa;"] = f"{KH} {num(3)}{C} ထို့အတူ သစ္စာများ{C} {IND} {num(16)}လည်း{C}"
V4["Padāni paccayākāre, cuddasūpari cuddasa."] = f"{PACCAYAKARA}၌ {PADA} {num(14)}{C} {UPARI} {num(14)}{END}"
V4["Samatiṃsa padā honti, gocchakesu dasasvatha;"] = f"{GOCCHA} {num(10)}တို့၌မူ {PADA} {F.NUM_MY[30]} အပြည့် ရှိ၏{C}"
V4["Duve cūḷantaradukā [cullantaradukā (sī.)], aṭṭha honti mahantarāti."] = (
    f"{num(2)}သည် {CULA} {var_my('[cullantaradukā (sī.)]')} ဖြစ်၏{C} {num(8)}သည် {MAHA} ဖြစ်၏{END}")
V5 = {}
V5["Dve saccā pannarasindriyā, ekādasa paṭiccapadā;"] = (
    f"သစ္စာ {num(2)}{C} {IND} {num(15)}{C} {PATICCA}၏ {PADA} {num(11)}{C}")
V5["Uddhaṃ puna ekādasa, gocchakapadamettha tiṃsavidhāti [tiṃsavidhanti (pī.)]."] = (
    f"{UDDHAM} {PUNA} {num(11)}{C} ဤနေရာ၌ {GOCCHA}တို့၏ {PADA}သည် {F.NUM_MY[30]} မျိုး ရှိ၏ "
    f"{var_my('[tiṃsavidhanti (pī.)]')}{END}")
V6 = {}
V6["Rūpañca dhammāyatanaṃ dhammadhātu, itthipumaṃ jīvitaṃ nāmarūpaṃ;"] = (
    f"ရုပ်{C} {S('dhammāyatanaṃ')}{C} {S('dhammadhātu')}{C} မိန်းမ{C} ယောက်ျား{C} အသက်{C} စိတ်ပိုင်းနှင့် ရုပ်ပိုင်း{C}")
V6["Dve bhavā jāti jarā maccurūpaṃ, anārammaṇaṃ no cittaṃ cittena vippayuttaṃ."] = (
    f"ဘဝ {num(2)}{C} {S('jāti')}{C} {S('jarā')}{C} {S('maraṇaṃ')}{C} ရုပ်{C} {sg('anārammaṇā dhammā')}{C} "
    f"{sg('no cittā dhammā')}{C} {sg('cittavippayuttā dhammā')}{END}")
V6["Visaṃsaṭṭhaṃ samuṭṭhāna-sahabhu anuparivatti;"] = (
    f"{sg('cittavisaṃsaṭṭhā dhammā')}{C} {sg('cittasamuṭṭhānā dhammā')}{C} {sg('cittasahabhuno dhammā')}{C} "
    f"{sg('cittānuparivattino dhammā')}{C}")
V6["Bāhiraṃ upādā dve, visayo [dvevīsati (syā.)] esanayo subuddho."] = (
    f"{sg('bāhirā dhammā')}{C} {sg('upādā dhammā')} ဟူသော {num(2)}သည် အပိုင်းအခြား {var_my('[dvevīsati (syā.)]')} "
    f"ဖြစ်၏{C} ဤ{F.NAYA}ကို ကောင်းစွာ နားလည်ပြီ{END}")
V8 = {}
V8["Khandhā caturo āyatanañca mekaṃ;"] = f"{KH} {num(4)}နှင့် {n_('a', 1)}{C}"
V8["Dhātūsu satta dvepi ca indriyato."] = f"{DH}တို့တွင် {num(7)}{C} {IND}တို့မှလည်း {num(2)}{END}"
V8["Tayo paṭicca tathariva phassapañcamā;"] = (
    f"{PATICCA}မှ {num(3)}{C} ထို့အတူ {S('phasso')} စသော {num(5)}{C}")
V8["Adhimuccanā manasi tikesu tīṇi."] = f"{S('adhimokkho')}{C} {S('manasikāro')}{C} {TIKA_LOC} {num(3)}{END}"
V8["Sattantarā dve ca manena yuttā;"] = f"{ANTARA} {F.DUKA}တို့မှ {num(7)}{C} {S('cittaṃ')}နှင့် ယှဉ်သော {num(2)}လည်း{C}"
V8["Vitakkavicāraṇā upekkhakāya cāti."] = (
    f"{VITVIC}{C} {sg('upekkhāsahagatā dhammā')}လည်း{END}")
V9 = {}
V9["Dhammāyatanaṃ dhammadhātu, atha jīvitaṃ nāmarūpaṃ;"] = (
    f"{S('dhammāyatanaṃ')}{C} {S('dhammadhātu')}{C} ထို့နောက် အသက်{C} စိတ်ပိုင်းနှင့် ရုပ်ပိုင်း{C}")
V9["Saḷāyatanaṃ jātijarāmataṃ, dve ca tike na labbhare."] = (
    f"{n_('a', 6)}{C} {S('jāti')}{C} {S('jarā')}{C} {S('maraṇaṃ')}{C} {TIKA_LOC} {num(2)}လည်း {LABBH}{END}")
V9["Paṭhamantare satta ca, gocchake dasa aparante;"] = (
    f"ပထမ {ANTARA} {GOCCHA}တွင် {num(7)}{C} {GOCCHA}တို့တွင် {num(10)}{C} နောက်ပိုင်း {ANTARA} {GOCCHA}တွင်")
V9["Cuddasa cha ca matthake, iccete sattacattālīsa dhammā;"] = (
    f"{num(14)}{C} အဆုံးပိုင်း၌ {num(6)}{C} ဤသို့ ဤ{F.DHP} {num(47)}တို့သည်")
V9["Samucchede na labbhanti, moghapucchakena cāti."] = (
    f"ပိုင်းဖြတ်ခြင်း၌ {LABBH}ကြ{C} မေးခွန်း အချည်းနှီး ဖြစ်သောကြောင့်လည်း{END}")
VERSES = {}
for _d in (V3, V4, V5, V6, V8, V9):
    for _k in _d:
        if _k in F.FIXED:
            raise SystemExit("verse already fixed: " + _k)
    VERSES.update(_d)
F.FIXED.update(VERSES)


# ===================================================================================== writing
def write(name, txt):
    txt = unicodedata.normalize("NFC", txt)
    (OUT / name).write_text(txt, encoding="utf-8")
    print(f"wrote {name}: {sum(1 for l in txt.splitlines() if l)} lines")


def bids(lines):
    bid_of, cur = {}, []
    for i, line in enumerate(lines):
        if line.strip():
            cur.append(i)
            m = F.ID_RE.search(line)
            if m:
                for j in cur:
                    bid_of[j] = m.group(1)
                cur = []
    return bid_of


def render(name):
    lines = (PALI / name).read_text(encoding="utf-8-sig").splitlines()
    bid_of = bids(lines)
    return "\n".join(F.translate_line(l, bid_of.get(i)) for i, l in enumerate(lines)).rstrip("\n") + "\n"


def chapter(name):
    lines = (PALI / name).read_text(encoding="utf-8-sig").splitlines()
    bid_of = bids(lines)
    done = []
    for i, line in enumerate(lines):
        try:
            done.append(F.translate_line(line, bid_of.get(i)))
        except F.Miss as e:
            print(f"STOP {name} line {i + 1}: {e}\n  {line[:200]}")
            return False
    write(name, "\n".join(done).rstrip("\n") + "\n")
    return True


if __name__ == "__main__":
    names = [a for a in sys.argv[1:] if not a.startswith("--")] or NAMES_OUT
    OUT.mkdir(parents=True, exist_ok=True)
    ok = True
    for n in names:
        ok = chapter(n) and ok
    sys.exit(0 if ok else 1)
