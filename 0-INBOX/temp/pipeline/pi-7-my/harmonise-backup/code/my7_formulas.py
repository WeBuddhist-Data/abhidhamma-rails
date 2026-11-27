"""Shared Burmese formulas for pi-7 (Paṭṭhāna, «အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ»), plain audience.

Every pi-7 Burmese generator imports this module, so that identical Pāli gets identical Burmese, within pi-7 and with
the FINAL pi-1 … pi-6 Burmese (the rails texts). It writes no files (no bytecode either). It holds:
  * FINAL: the rails texts of pi-1 … pi-6 aligned with their Pāli by block ID (read only), and W(): every value reused
    from them is CHECKED at import (its Pāli must occur in a Pāli segment and its Burmese in that segment's Burmese);
    WITNESS records (book, block, Burmese) for the terms file and the reuse test of check_sample.py;
  * the book frame, number words, the 24 conditions in every case form (cond()), the triad / dyad term tables
    (TRIADS, from pi-1 final), the noun lexicon (NOUN) and the noun-phrase renderer (np_my());
  * the headings (heading()), colophons, the variant form (variant());
  * the frames: clause() (paṭicca / sahajāta / paccaya / nissaya / saṃsaṭṭha / sampayutta and the pucchāvāra
    «Siyā … uppajjeyya»), panha() («X dhammo Yassa dhammassa Zpaccayena paccayo»), chain() (condition chains and the
    counting frame «Hetuyā tīṇi …»), pairs() («ekaṃ khandhaṃ paṭicca dve khandhā …»), ghatana() («Hetu-…-avigatanti
    tīṇi»);
  * the engine translate(): a unit (sentence, or a part between « – » / «; ») is tried against the SK templates,
    the pañhā frame, the ghaṭanā frame, the pairs frame, and then fragment by fragment (between «…») against SKF,
    the clause frame and the chain. Anything left raises Miss (DEV=True collects it in UNSEEN): nothing is guessed.
Later chapters: import this module, add their own triads / nouns / notes with the add_*() helpers and TRIADS[...]
(then call rebuild()), and put their unique sentence templates into SK / SKF in their own make_*.py.
Never change an existing value without the user's approval.
"""
import pathlib
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]


class Miss(KeyError):
    pass


# ===================================================================================== FINAL: rails texts pi-1 … pi-6
ID_RE = re.compile(r"\s*(\^[0-9A-Za-z-]+)\s*$")
BOOKS = {b: (ROOT / f"AI_translation/pali/pi-{b}_split_chapters",
             ROOT / f"AI_translation/burmese/pi-{b}-burmese-plain-rails_split_chapters") for b in "123456"}


def _blocks(text):
    res, cur = {}, []
    for line in text.splitlines():
        if not line.strip():
            continue
        cur.append(line)
        m = ID_RE.search(line)
        if m:
            res[m.group(1)] = cur
            cur = []
    return res


class _Final:
    """SEG[book][block id] = (file, pāli lines, burmese lines) for pi-1 … pi-6 (rails)."""

    def __init__(self):
        self.SEG = {}
        for book, (pdir, bdir) in BOOKS.items():
            d = {}
            for f in sorted(pdir.glob("*.md")):
                bf = bdir / f.name
                if not bf.exists():
                    continue
                pb = _blocks(f.read_text(encoding="utf-8-sig"))
                bb = _blocks(unicodedata.normalize("NFC", bf.read_text(encoding="utf-8-sig")))
                for k, v in pb.items():
                    if k in bb and len(bb[k]) == len(v):
                        d[k] = (f.name, v, bb[k])
            self.SEG[book] = d


FINAL = _Final()
LAX = False      # True: collect failing witnesses in WFAIL instead of stopping (development only)
WFAIL = []
WITNESS = {}     # Pāli -> (book, block id, Burmese): every value read from / checked against the FINAL rails


def W(pali, my, book=None, bid=None, key=None):
    """A value reused from pi-1 … pi-6: find (or check) a FINAL segment whose Pāli contains «pali» (case-insensitive,
    variants and «…pe…» ignored) and whose Burmese contains «my». Raises Miss if there is none."""
    def norm(s):
        s = re.sub(r"\s*[\[{][^\]}]*[\]}]", "", s)
        return s.replace("…pe…", "…").replace("…Pe…", "…").lower()
    pk = norm(pali)
    books = [book] if book else list(FINAL.SEG)
    for b in books:
        items = [(bid, FINAL.SEG[b][bid])] if bid else FINAL.SEG[b].items()
        for k, (f, p, m) in items:
            if pk in norm(" ".join(p)) and my in " ".join(m):
                WITNESS.setdefault(key or pali, (b, k, my))
                return my
    if LAX:
        WFAIL.append((pali, my, book, bid))
        return my
    raise Miss(f"witness: «{pali}» / «{my}» not found in the FINAL rails")


# ===================================================================================== basics and book frame
C = "၊"                    # list / clause break (Pāli «,» and «;»)
END = "။"                  # end of a statement or question (Pāli «.»)
PE = "…"                   # …pe… / …Pe… = one «…»
NAMO = W("Namo tassa bhagavato arahato sammāsambuddhassa",
         "ထိုမြတ်စွာဘုရား၊ ရဟန္တာ၊ အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရားရှင်အား ရှိခိုးပါ၏", "1")
ABHI = W("Abhidhammapiṭake", "အဘိဓမ္မာပိဋကတွင်", "1", "^0")
TITLE = "အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ"     # Paṭṭhānapāḷi (book title, Burmese only): "how causes and results connect"
DONE = "ပြီးဆုံးပြီ"                         # niṭṭhitaṃ / niṭṭhito / niṭṭhitā (pi-1 … pi-6 colophons)
W("Khandhavibhaṅgo niṭṭhito", "“အစုအဝေးများကို ခွဲခြမ်းစိတ်ဖြာခြင်း” ပြီးဆုံးပြီ။", "2", "^2-153")


def pe(s):
    return s.replace("…pe…", PE).replace("…Pe…", PE)


def finished(name):
    """«X niṭṭhitaṃ.» = «“X” ပြီးဆုံးပြီ။» (pi-1 … pi-6 colophons)."""
    return f"“{name}” {DONE}{END}"


# --- labels (Ka) (Kha) … ---------------------------------------------------------------------------------------------
AKKHARA = {"Ka": "က", "Kha": "ခ", "Ga": "ဂ", "Gha": "ဃ", "Ṅa": "င", "Ca": "စ", "Cha": "ဆ", "Ja": "ဇ"}
W("(Ka) kusalā dhammā", "(က) ကုသိုလ် သဘောတရားများ", "1", "^1-M1-1")
W("(Gha)", "(ဃ)", "2", "^2-793")

# ===================================================================================== numbers
# counts of the saṅkhyāvāra («Hetuyā tīṇi» = «… ၌ သုံးခု»): the number of answers (vāra), classifier «ခု» (NEW)
NUMW = {"eka": "တစ်", "dvi": "နှစ်", "ti": "သုံး", "catu": "လေး", "pañca": "ငါး", "cha": "ခြောက်", "satta": "ခုနစ်",
        "aṭṭha": "ရှစ်", "nava": "ကိုး", "dasa": "ဆယ်"}
COUNT = {"ekaṃ": "တစ်ခု", "dve": "နှစ်ခု", "tīṇi": "သုံးခု", "cattāri": "လေးခု", "pañca": "ငါးခု", "cha": "ခြောက်ခု",
         "satta": "ခုနစ်ခု", "aṭṭha": "ရှစ်ခု", "nava": "ကိုးခု", "dasa": "ဆယ်ခု"}
COUNT_VAL = {"ekaṃ": 1, "dve": 2, "tīṇi": 3, "cattāri": 4, "pañca": 5, "cha": 6, "satta": 7, "aṭṭha": 8, "nava": 9,
             "dasa": 10}
# khandha / mahābhūta counts (pi-2 / pi-3 / pi-5: «အစုအဝေး တစ်ပါး … လေးပါး»)
PAA = {1: "တစ်ပါး", 2: "နှစ်ပါး", 3: "သုံးပါး", 4: "လေးပါး"}
W("tīhi khandhehi", "အစုအဝေး သုံးပါး", "3")
W("cattāro khandhā arūpino", "ရုပ် မဟုတ်သော အစုအဝေး လေးပါးတို့သည်", "5")
W("ekena khandhena", "အစုအဝေး တစ်ပါး", "3")
W("Dve khandhā", "အစုအဝေး နှစ်ပါး", "2")
NP_NUM = {"eko": 1, "ekaṃ": 1, "ekassa": 1, "dve": 2, "dvinnaṃ": 2, "tayo": 3, "tiṇṇaṃ": 3, "cattāro": 4,
          "catunnaṃ": 4}

# ===================================================================================== the 24 conditions
# stem -> N, the bare name. Every case form is built from N (cond()):
#   name (Xpaccayo, headings)            «Nဟူသော အကြောင်း»          neg «Nဟူသော အကြောင်း မဟုတ်ခြင်း»
#   ablative (Xpaccayā)                  «Nဟူသော အကြောင်းကြောင့်»    neg «Nဟူသော အကြောင်းကြောင့် မဟုတ်ဘဲ»
#   counting locative (Xe / Xyā N)       «Nဟူသော အကြောင်း၌»          neg «Nဟူသော အကြောင်း မဟုတ်ခြင်း၌»
#   instrumental (Xpaccayena paccayo)    «Nဟူသော အကြောင်းဖြင့် အကြောင်း ဖြစ်သည်» (pi-5 rails)
#                                         na Xpaccayena paccayo «… အကြောင်း ဖြစ်သည် မဟုတ်»
#   -pi (Xpaccayopi)                     «Nဟူသော အကြောင်းကိုလည်း» (object of vitthāretabbo)
#   bare (ghaṭanā lists)                 «N»
PACCAYA = W("paccayo", "အကြောင်း", "5", "^5-717")
CONDS = [
    ("hetu", W("Hetupaccayena paccayo", "အမြစ်ဟူသော အကြောင်းဖြင့် အကြောင်း", "5", "^5-717") and "အမြစ်"),
    ("ārammaṇa", W("ārammaṇapaccayena paccayo", "အာရုံဟူသော အကြောင်းဖြင့် အကြောင်း", "5") and "အာရုံ"),
    ("adhipati", W("adhipatipaccayena paccayo", "အကြီးအမှူးဟူသော အကြောင်းဖြင့် အကြောင်း", "5") and "အကြီးအမှူး"),
    ("anantara", W("anantarapaccayena paccayo", "ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်းဖြင့် အကြောင်း", "5")
     and "ချက်ချင်း နောက်၌ ဖြစ်စေခြင်း"),
    ("samanantara", W("samanantarapaccayena paccayo",
                      "ကောင်းစွာ ချက်ချင်း နောက်၌ ဖြစ်စေခြင်းဟူသော အကြောင်းဖြင့် အကြောင်း", "5")
     and "ကောင်းစွာ ချက်ချင်း နောက်၌ ဖြစ်စေခြင်း"),
    ("sahajāta", W("sahajātapaccayena paccayo", "အတူ ပေါ်ပေါက်ခြင်းဟူသော အကြောင်းဖြင့် အကြောင်း", "5")
     and "အတူ ပေါ်ပေါက်ခြင်း"),
    ("aññamañña", "အချင်းချင်း ထောက်ပံ့ခြင်း"),        # NEW (pi-5 aññamañña = «အချင်းချင်း»)
    ("nissaya", "အမှီ"),                                # NEW (nissāya «မှီ၍»)
    ("upanissaya", "အားကြီးသော အမှီ"),                  # NEW
    ("purejāta", "ရှေးဦးစွာ ဖြစ်ပေါ်ခြင်း"),            # NEW (pi-2 purejāta «ရှေးဦးစွာ ဖြစ်ပေါ်ပြီးသော»)
    ("pacchājāta", "နောက်မှ ဖြစ်ပေါ်ခြင်း"),            # NEW
    ("āsevana", W("āsevanapaccayena paccayo", "အလေ့အကျင့် ပြုခြင်းဟူသော အကြောင်းဖြင့် အကြောင်း", "5")
     and "အလေ့အကျင့် ပြုခြင်း"),
    ("kamma", "ကံ"),                                    # pi-1 … pi-6 kamma «ကံ»
    ("vipāka", "ကံ၏ အကျိုး"),                           # pi-1 Vipākattika «ကံ၏ အကျိုး»
    ("āhāra", W("āhārapaccayena paccayo", "အာဟာရဟူသော အကြောင်းဖြင့် အကြောင်း", "5") and "အာဟာရ"),
    ("indriya", W("indriyapaccayena paccayo", "စွမ်းရည်ဟူသော အကြောင်းဖြင့် အကြောင်း", "5") and "စွမ်းရည်"),
    ("jhāna", "ဈာန်"),                                  # pi-5 jhāna «ဈာန်»
    ("magga", W("maggapaccayena paccayo", "မဂ်ဟူသော အကြောင်းဖြင့် အကြောင်း", "5") and "မဂ်"),
    ("sampayutta", "ယှဉ်တွဲခြင်း"),                     # NEW (sampayutta «…နှင့် ယှဉ်တွဲသော» pi-1)
    ("vippayutta", "ကင်းကွာခြင်း"),                     # NEW (vippayutta «…နှင့် ကင်းကွာသော» pi-1)
    ("atthi", "ရှိခြင်း"),                              # NEW (pi-5 atthi «ရှိသည်»)
    ("natthi", "မရှိခြင်း"),                            # NEW (pi-5 natthi «မရှိသည်»)
    ("vigata", "ပျောက်ကွယ်ခြင်း"),                      # NEW (pi-1 vibhava «ဘဝ ပျောက်ကွယ်ခြင်း»)
    ("avigata", "မပျောက်ကွယ်ခြင်း"),                    # NEW
]
STEMS = [c[0] for c in CONDS]
N = dict(CONDS)
HUTHO = "ဟူသော"
KYAUNG = "ကြောင့်"
NOT = "မဟုတ်"
LOC2STEM = {"hetuyā": "hetu", "adhipatiyā": "adhipati", "atthiyā": "atthi", "natthiyā": "natthi"}
LOC2STEM.update({s[:-1] + "e": s for s in STEMS if s not in ("hetu", "adhipati", "atthi", "natthi")})
NEG_PREFIX = {s: ("no" if s in ("atthi", "natthi", "vigata", "avigata") else "na") for s in STEMS}


def cname(stem):
    return f"{N[stem]}{HUTHO} {PACCAYA}"


def cond(stem, form, neg=False):
    """form: 'n' name, 'ab' ablative (Xpaccayā), 'loc' counting locative, 'i' instrumental «…ဖြင့်»,
    'pi' Xpaccayopi, 'bare' the bare name, 'obj' name + «ကို» (vitthāretabbo), 'gen' name + «၏»."""
    nm = cname(stem)
    if form == "bare":
        return N[stem]
    if form == "n":
        return f"{nm} {NOT}ခြင်း" if neg else nm
    if form == "gen":
        return (f"{nm} {NOT}ခြင်း" if neg else nm) + "၏"
    if form == "obj":
        return (f"{nm} {NOT}ခြင်း" if neg else nm) + "ကို"
    if form == "pi":
        return (f"{nm} {NOT}ခြင်း" if neg else nm) + "ကိုလည်း"
    if form == "ab":
        return f"{nm}{KYAUNG} {NOT}ဘဲ" if neg else f"{nm}{KYAUNG}"
    if form == "loc":
        return f"{nm} {NOT}ခြင်း၌" if neg else f"{nm}၌"
    if form == "i":
        if neg:
            raise ValueError("a negated instrumental is «na Xpaccayena paccayo» (iframe)")
        return f"{nm}ဖြင့်"
    raise ValueError(form)


IS_COND = f"{PACCAYA} ဖြစ်သည်"          # «… ဖြင့် အကြောင်း ဖြစ်သည်» (pi-5 rails)


def iframe(stem, neg_free=False):
    """«Xpaccayena paccayo» = «Nဟူသော အကြောင်းဖြင့် အကြောင်း ဖြစ်သည်»; «na Xpaccayena paccayo» adds «မဟုတ်»."""
    return f"{cond(stem, 'i')} {IS_COND}" + (f" {NOT}" if neg_free else "")


_STEM_ALT = "|".join(sorted(STEMS, key=len, reverse=True))
WCH = r"[\wāīūṃṅñṭḍṇḷ]"
COND_RE = re.compile(r"(?<![\wāīūṃṅñṭḍṇḷ])(?P<neg>[Nn]a|[Nn]o)?(?P<stem>(?i:" + _STEM_ALT + r"))paccay"
                     r"(?P<end>opi|oti|ena|ā|o|aṃ)(?![\wāīūṃṅñṭḍṇḷ])")
_LOC_ALT = "|".join(sorted(LOC2STEM, key=len, reverse=True))
_CNT_ALT = "|".join(sorted(COUNT, key=len, reverse=True))
COUNT_RE = re.compile(r"(?<![\wāīūṃṅñṭḍṇḷ])(?P<neg>[Nn]a|[Nn]o)?(?P<loc>(?i:" + _LOC_ALT + r")) (?P<num>"
                      + _CNT_ALT + r")(?![\wāīūṃṅñṭḍṇḷ])")


def count_my(stem, neg, num):
    return f"{cond(stem, 'loc', neg)} {COUNT[num]}"


# ===================================================================================== triads and dyads (pi-1 final)
# Each value is the attributive form used before a noun («… သဘောတရား»).
ABY = W("abyākatā dhammā", "ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော သဘောတရား", "1", "^1-M1-1")[:-len(" သဘောတရား")]
TRIADS = {
    "kusala": {"kusal": W("Kusalā dhammā", "ကုသိုလ် သဘောတရား", "1", "^1-M1-1")[:-len(" သဘောတရား")],
               "akusal": W("akusalā dhammā", "အကုသိုလ် သဘောတရား", "1", "^1-M1-1")[:-len(" သဘောတရား")],
               "abyākat": ABY},
    "vedana": {"sukhāya vedanāya sampayutt": W("Sukhāya vedanāya sampayuttā dhammā",
                                               "သာယာသော ခံစားမှုနှင့် ယှဉ်တွဲသော သဘောတရားများ", "1",
                                               "^1-M1-2")[:-len(" သဘောတရားများ")],
               "dukkhāya vedanāya sampayutt": W("dukkhāya vedanāya sampayuttā dhammā",
                                                "နာကျင်သော ခံစားမှုနှင့် ယှဉ်တွဲသော သဘောတရားများ", "1",
                                                "^1-M1-2")[:-len(" သဘောတရားများ")],
               "adukkhamasukhāya vedanāya sampayutt": W("adukkhamasukhāya vedanāya sampayuttā dhammā",
                                                        "မနာကျင် မသာယာသော ခံစားမှုနှင့် ယှဉ်တွဲသော သဘောတရားများ",
                                                        "1", "^1-M1-2")[:-len(" သဘောတရားများ")]},
}
# Pāli endings each triad accepts after its stem (the vedanā phrase is long enough to stand alone)
TRIAD_END = {"kusala": r"(?:aṃ|o|ā|ānaṃ|añca|assa|e|ena|āya)(?![\wāīūṃṅñṭḍṇḷ])", "vedana": r""}
TERM_KEYS = {}
TERM_RE = None


def rebuild():
    """Rebuild the term regex after adding a triad / dyad to TRIADS (and TRIAD_END)."""
    global TERM_RE
    TERM_KEYS.clear()
    alts, i = [], 0
    for tri, tab in TRIADS.items():
        for k in sorted(tab, key=len, reverse=True):
            g = f"t{i}"
            TERM_KEYS[g] = (tri, k)
            pat = f"[{k[0].upper()}{k[0]}]" + re.escape(k[1:])
            alts.append(f"(?P<{g}>{pat}){TRIAD_END[tri]}")
            i += 1
    TERM_RE = re.compile(r"(?<![\wāīūṃṅñṭḍṇḷ])(?:" + "|".join(alts) + ")")


rebuild()


def term_value(m):
    for g, v in m.groupdict().items():
        if v:
            tri, k = TERM_KEYS[g]
            return TRIADS[tri][k]
    raise ValueError(m[0])


# ===================================================================================== nouns and noun phrases
DHAMMA = W("Kusalā dhammā", "သဘောတရား", "1", "^1-M1-1")
KHANDHA = W("Cattāro khandhā", "အစုအဝေး", "2")
# Pāli head-noun form -> (Burmese noun, case, plural). case: n nominative, a accusative, g genitive / dative,
# l locative, i instrumental. Later chapters add with add_noun().
NOUN = {}


def add_noun(my, **forms):
    """add_noun('သဘောတရား', n=['dhammo'], np=['dhammā'], a=['dhammaṃ'], ap=['dhamme'], g=['dhammassa'],
    gp=['dhammānaṃ'] …): register every Pāli form of one Burmese noun (p = plural)."""
    for k, words in forms.items():
        case, pl = k[0], k.endswith("p")
        for w in words:
            NOUN[w] = (my, case, pl)


add_noun(DHAMMA, n=["dhammo"], np=["dhammā"], a=["dhammaṃ"], ap=["dhamme"], g=["dhammassa"], gp=["dhammānaṃ"])
add_noun(KHANDHA, n=["khandho"], np=["khandhā"], a=["khandhaṃ"], ap=["khandhe"], g=["khandhassa"], gp=["khandhānaṃ"])
add_noun(W("rūpānaṃ", "ရုပ်", "1"), gp=["rūpānaṃ"], n=["rūpaṃ"])
add_noun(W("mahābhūtā", "မူလဓာတ်ကြီး", "5"), np=["mahābhūtā"])
add_noun(W("hetū", "အမြစ်", "1"), np=["hetū"])
add_noun("စေ့ဆော်မှု", n=["cetanā"])
add_noun(W("moho", "မောဟ", "1"), n=["moho"])
VATTHU = W("vatthuṃ", "မှီရာ ဝတ္ထု", "5")
add_noun(W("bhojane", "အစားအစာ", "1") and "ရာသီဥတုနှင့် အစားအစာ", n=["utubhojanam"])   # utu (NEW) «ရာသီဥတု»
add_noun(W("puggalo", "ပုဂ္ဂိုလ်", "5"), n=["puggalo"])
add_noun(W("senāsanaṃ", "အိပ်ရာ နေရာ", "2"), n=["senāsanam"])
add_noun(VATTHU, a=["vatthuṃ"])
# qualifiers (attributive, before the noun): Pāli word -> Burmese (already attributive)
QUAL = {}


def add_qual(my, *words):
    for w in words:
        QUAL[w] = my


SAHAGATA = "နှင့်အတူ ဖြစ်သော"   # X-sahagata (pi-1 «Xနှင့်အတူ ဖြစ်သော»)
add_qual(W("dukkhasahagataṃ", "နာကျင်မှုနှင့်အတူ ဖြစ်သော", "1"), "dukkhasahagataṃ", "dukkhasahagatassa")
add_qual(W("sukhasahagatā", "သာယာမှုနှင့်အတူ ဖြစ်သော", "1"), "sukhasahagataṃ", "sukhasahagatassa")
KAYAVINNANA = W("kāyaviññāṇaṃ", "ကိုယ် သိစိတ်", "1")
add_qual(KAYAVINNANA + SAHAGATA, "kāyaviññāṇasahagataṃ")
add_qual("သိစိတ် လေးပါးနှင့်အတူ ဖြစ်သော", "catuviññāṇasahagataṃ")        # NEW (catuviññāṇa)
add_qual(W("vicikicchāsahagato", "ယုံမှားမှုနှင့်အတူ ဖြစ်သော", "1"), "vicikicchāsahagato", "vicikicchāsahagate")
add_qual(W("uddhaccasahagato", "ယောက်ယက်ခတ်မှုနှင့်အတူ ဖြစ်သော", "1"), "uddhaccasahagato", "uddhaccasahagate")
AHETUKA = W("ahetukaṃ", "အမြစ် မရှိသော", "2")
add_qual(AHETUKA, "ahetukaṃ")
VIPAKA_ADJ = "ကံ၏ အကျိုး ဖြစ်သော"      # vipāka- (pi-1 «ကံ၏ အကျိုး ဖြစ်သော သဘောတရားများ»)
W("Vipākā dhammā", VIPAKA_ADJ, "1", "^1-M1-3")
add_qual(VIPAKA_ADJ, "vipāko", "vipākā", "vipākānaṃ")
ARUPA = W("arūpino", "ရုပ် မဟုတ်သော", "5")
POSTQUAL = {"arūpino"}          # adjectives that follow their noun in the Pāli («cattāro khandhā arūpino»)
add_qual(ARUPA, "arūpino", "arūpīnaṃ")
add_qual(W("rūpino dhammā", "ရုပ် ဖြစ်သော", "1"), "rūpino", "rūpīnaṃ")
add_qual("ယှဉ်တွဲသော", "sampayuttakānaṃ", "sampayuttā")
add_qual("ထို", "taṃ")
add_qual("ထိုအရာနှင့် ယှဉ်တွဲသော", "taṃsampayuttakā", "taṃsampayuttakānaṃ")        # NEW (taṃ- «ထိုအရာ»)
add_qual("ထိုအရာမှ ဖြစ်ပေါ်လာသော", "taṃsamuṭṭhānānaṃ")
add_qual(W("cittasamuṭṭhānā", "စိတ်မှ ဖြစ်ပေါ်လာသော", "2"), "cittasamuṭṭhānānaṃ")
add_qual(W("purimā", "ရှေးရှေး", "5"), "purimā purimā")
add_qual(W("pacchimānaṃ", "နောက်နောက်", "5"), "pacchimānaṃ pacchimānaṃ")
CITTACETASIKA = W("cittacetasikā dhammā", "စိတ်နှင့် စိတ်၏ အဖော် သဘောတရား", "1")[:-len(" " + DHAMMA)]
add_qual(CITTACETASIKA, "cittacetasikā", "cittacetasikānaṃ")
add_qual(W("kiriyābyākatā", "ပြုရုံမျှသာ ဖြစ်သော ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော", "5"),
         "kiriyābyākatā", "kiriyābyākatānaṃ")
add_qual("နောက်မှ ဖြစ်ပေါ်သော", "pacchājātā")
add_qual(W("paccuppannā dhammā", "ပစ္စုပ္ပန်", "1"), "paṭuppannānaṃ")
add_qual("ချက်ချင်း ချုပ်ငြိမ်းပြီးသော", "samanantaraniruddhā")              # NEW
add_qual("ချက်ချင်း ပျောက်ကွယ်ပြီးသော", "samanantaravigatā")               # NEW
add_qual("အမြစ်နှင့် ယှဉ်တွဲသော", "hetusampayuttakānaṃ")
for _p, _my in (("chanda", "ဆန္ဒ"), ("vīriya", "ဝီရိယ"), ("citta", "စိတ်"), ("vīmaṃsa", "စုံစမ်းဆင်ခြင်မှု"),
                ("jhāna", "ဈာန်"), ("magga", "မဂ်")):
    add_qual(f"{_my}နှင့် ယှဉ်တွဲသော", f"{_p}sampayuttakānaṃ")
W("chandādhipati sahajātānaṃ", "ဆန္ဒ အကြီးအမှူးသည်", "5")
W("vīmaṃsādhipati", "စုံစမ်းဆင်ခြင်မှု အကြီးအမှူး", "5")
# whole noun phrases that are not built from parts (Pāli -> (Burmese noun phrase, case, plural))
FIXED = {}


def add_fixed(my, case, pl, *words):
    for w in words:
        for v in (w, w[:1].lower() + w[1:]):
            FIXED[v] = (my, case, pl)


# āyatana, dhātu, indriya names (pi-1 / pi-2 final)
_AY = {"rūpāyatanaṃ": "အဆင်းအရောင် အာရုံခံ နယ်ပယ်", "saddāyatanaṃ": "အသံ အာရုံခံ နယ်ပယ်",
       "gandhāyatanaṃ": "အနံ့ အာရုံခံ နယ်ပယ်", "rasāyatanaṃ": "အရသာ အာရုံခံ နယ်ပယ်",
       "phoṭṭhabbāyatanaṃ": "အထိအတွေ့ အာရုံခံ နယ်ပယ်", "cakkhāyatanaṃ": "မျက်စိ အာရုံခံ နယ်ပယ်",
       "sotāyatanaṃ": "နား အာရုံခံ နယ်ပယ်", "ghānāyatanaṃ": "နှာခေါင်း အာရုံခံ နယ်ပယ်",
       "jivhāyatanaṃ": "လျှာ အာရုံခံ နယ်ပယ်", "kāyāyatanaṃ": "ကိုယ် အာရုံခံ နယ်ပယ်"}
for _p, _my in _AY.items():
    add_fixed(W(_p, _my, "1"), "n", False, _p[0].upper() + _p[1:], _p)
_DH = {"cakkhuviññāṇadhātu": "မျက်စိ သိစိတ် ဓာတ်", "sotaviññāṇadhātu": "နား သိစိတ် ဓာတ်",
       "ghānaviññāṇadhātu": "နှာခေါင်း သိစိတ် ဓာတ်", "jivhāviññāṇadhātu": "လျှာ သိစိတ် ဓာတ်",
       "kāyaviññāṇadhātu": "ကိုယ် သိစိတ် ဓာတ်", "manodhātu": "မနော ဓာတ်", "manoviññāṇadhātu": "မနော သိစိတ် ဓာတ်"}
for _p, _my in _DH.items():
    W(_p, _my, "2")
    add_fixed(_my, "n", False, _p, _p[0].upper() + _p[1:])
    add_fixed(_my, "g", False, _p + "yā", _p[0].upper() + _p[1:] + "yā")
add_fixed(_DH["ghānaviññāṇadhātu"], "n", False, "Ghāṇaviññāṇadhātu")      # source slip ṇ (logged)
_IN = {"cakkhundriyaṃ": "မျက်စိ၏ စွမ်းရည်", "sotindriyaṃ": "နား၏ စွမ်းရည်", "ghānindriyaṃ": "နှာခေါင်း၏ စွမ်းရည်",
       "jivhindriyaṃ": "လျှာ၏ စွမ်းရည်", "kāyindriyaṃ": "ကိုယ်၏ စွမ်းရည်"}
for _p, _my in _IN.items():
    add_fixed(W(_p, _my, "2"), "n", False, _p, _p[0].upper() + _p[1:])
add_fixed(W("rūpajīvitindriyaṃ", "ရုပ် အသက်၏ စွမ်းရည်", "2", "^2-1017"), "n", False, "Rūpajīvitindriyaṃ")
add_fixed(W("nāmarūpaṃ", "စိတ်ပိုင်းနှင့် ရုပ်ပိုင်း", "2"), "n", False, "nāmarūpaṃ")
add_fixed(W("kabaḷīkāro āhāro", "လုတ်ပြု၍ စားရသော အာဟာရ", "1"), "n", False, "kabaḷīkāro §V§ āhāro")
add_fixed(W("mahābhūtā upādāyarūpānaṃ", "မူလဓာတ်ကြီးတို့ကို မှီ၍ ဖြစ်သော ရုပ်", "5"), "g", True, "upādārūpānaṃ")
KATATTARUPA = "ကံ ပြုခဲ့သောကြောင့် ဖြစ်သော ရုပ်"          # kaṭattārūpa (NEW; pi-1 «ကံကို ပြုခဲ့၍ … သောကြောင့်»)
add_fixed(KATATTARUPA, "g", True, "kaṭattārūpānaṃ", "kaṭattā ca rūpānaṃ")
add_fixed("ဤကိုယ်", "g", False, "imassa kāyassa")
add_fixed("ရှေးဦးစွာ ဖြစ်ပေါ်ပြီးသော ဤကိုယ်", "g", False, "purejātassa imassa kāyassa")
W("purejātārammaṇā", "ရှေးဦးစွာ ဖြစ်ပေါ်ပြီးသော", "2")
add_fixed(W("kusalākusale", "ကုသိုလ်နှင့် အကုသိုလ်", "5") + " ကံ", "n", False, "kusalākusalaṃ kammaṃ")
add_fixed(f"{ARUPA} အာဟာရ", "n", True, "arūpino āhārā")
add_fixed(f"{ARUPA} စွမ်းရည်", "n", True, "arūpino indriyā")
add_fixed(W("maggaṅgaṃ", "မဂ်၏ အင်္ဂါ", "1"), "n", True, "maggaṅgāni")
add_fixed("ဈာန်၏ အင်္ဂါ", "n", True, "jhānaṅgāni")
add_fixed(f"{DHAMMA} အားလုံး", "n", True, "sabbe dhammā")
for _p, _my in (("chandādhipati", "ဆန္ဒ"), ("vīriyādhipati", "ဝီရိယ"), ("cittādhipati", "စိတ်"),
                ("vīmaṃsādhipati", "စုံစမ်းဆင်ခြင်မှု")):
    add_fixed(f"{_my} {N['adhipati']}", "n", False, _p)
# prefixes (time / place) before a phrase
OKKANTI = "သန္ဓေ သက်ဆင်းသော ခဏ၌"       # okkantikkhaṇe (NEW; pi-2 okkanti «သက်ဆင်းခြင်း»)
PATISANDHI = "ပဋိသန္ဓေ"                  # paṭisandhi (NEW)
PREFIX = {"okkantikkhaṇe": OKKANTI, "paṭisandhikkhaṇe": f"{PATISANDHI} နေသော ခဏ၌",
          "ahetukapaṭisandhikkhaṇe": f"{AHETUKA} {PATISANDHI} နေသော ခဏ၌",
          "arūpe": W("arūpe", "ရုပ်မရှိသော ဘုံ", "2") + "၌"}

CASE = {"n": "သည်", "a": "ကို", "g": "အား", "l": "၌", "i": "ဖြင့်", "": ""}
LAKAUNG = "လည်းကောင်း"            # «Xလည်းကောင်း၊ Yလည်းကောင်း» (X ca Y ca / X Yñca; pi-2 rails)


def _conj(words):
    """Split an NP word list on coordination -> list of conjunct word lists, or None when there is none.
    Pāli «ca» is enclitic: «A ca B ca [rest]» closes a conjunct after each «ca»; a single inner «ca» follows the
    first word of the second conjunct («X Y ca Z» = [X] + [Y Z]); «Wñca» opens a new conjunct with «Wṃ»."""
    n_ca = words.count("ca")
    parts = []
    if n_ca >= 2:
        cur = []
        rest = list(words)
        while "ca" in rest:
            i = rest.index("ca")
            parts.append(rest[:i])
            rest = rest[i + 1:]
        if rest:
            more = _conj(rest)
            parts.extend(more if more else [rest])
    elif n_ca == 1:
        i = words.index("ca")
        if i == len(words) - 1 or i < 1:
            return None
        if i == 1:
            return None
        first, second = words[:i - 1], [words[i - 1]] + words[i + 1:]
        more = _conj(second)
        parts = [first] + (more if more else [second])
    else:
        for i, w in enumerate(words):
            if "\u0002" in w and i > 0:           # a fixed phrase with an inner «ca» («kaṭattā ca rūpānaṃ»)
                more = _conj(words[i + 1:]) if words[i + 1:] else None
                parts = [words[:i], [w] + words[i + 1:]]
                break
            if w.endswith("ñca") and i > 0:
                second = [w[:-3] + "ṃ"] + words[i + 1:]
                more = _conj(second)
                parts = [words[:i]] + (more if more else [second])
                break
    parts = [p for p in parts if p]
    return parts if len(parts) > 1 else None


TERM_TAIL_OK = {"", "aṃ", "o", "ā", "e", "ena", "assa", "āya", "akānaṃ", "ānaṃ", "akā", "āyo"}


def np_parse(words, terms):
    """One conjunct -> (Burmese phrase without case, case, plural, n_terms). terms: iterator of term values."""
    words = [w.replace("\u0002", " ") for w in words]
    if words and words[0].endswith("ñca") and words[0] not in FIXED:      # «Wñca» opening a conjunct
        words = [words[0][:-3] + "ṃ"] + words[1:]
    if len(words) > 1 and words[-1] in POSTQUAL:                         # «cattāro khandhā arūpino»
        words = words[:-2] + [words[-1], words[-2]]
    text = " ".join(words)
    # an asyndetic list of fixed nouns «rūpāyatanaṃ saddāyatanaṃ …» -> «A၊ B၊ … E» (plural)
    if len(words) > 1 and all(w in FIXED for w in words):
        return (C + " ").join(FIXED[w][0] for w in words), FIXED[words[-1]][1], True, 0
    if text in FIXED:
        my, case, pl = FIXED[text]
        return my, case, pl, 0
    # term coordination on one noun: «§T§o ca §T§o ca dhammā», «§T§añca §T§añca dhammaṃ»
    head = words[-1]
    if head in FIXED:
        hmy, case, pl = FIXED[head]
    elif head in NOUN:
        hmy, case, pl = NOUN[head]
    else:
        raise KeyError("noun: " + head)
    mods, num, nt = [], None, 0
    i = 0
    pre = words[:-1]
    while i < len(pre):
        w = pre[i]
        two = " ".join(pre[i:i + 2])
        if two in QUAL:
            mods.append(QUAL[two])
            i += 2
            continue
        if w.startswith("§T§"):
            if w[3:] not in TERM_TAIL_OK:
                raise KeyError("term tail in an NP: " + w)
            mods.append(next(terms))
            nt += 1
        elif w in NP_NUM:
            num = NP_NUM[w]
        elif w in QUAL:
            mods.append(QUAL[w])
        else:
            raise KeyError("np word: " + w)
        i += 1
    if num is not None:
        pl = num > 1
    # «sukhasahagataṃ kāyaviññāṇasahagataṃ»: two qualifiers in a row get «၊» between them
    out = []
    for k, m in enumerate(mods):
        out.append(m + (C if k + 1 < len(mods) and m.endswith(SAHAGATA) and mods[k + 1].endswith(SAHAGATA)
                        else ""))
    phrase = " ".join(out + [hmy]) + (f" {PAA[num]}" if num else "")
    return phrase, case, pl, nt


def np_my(words, terms, role):
    """Render a Pāli NP (list of words; term slots «§T§…») in a role: 'n' subject («…သည်»), 'a' object («…ကို»),
    'g' recipient («…အား»), '' bare (no case: plural «များ» when there is no number).
    Coordination gives «Xလည်းကောင်း၊ Yလည်းကောင်း» (with the case marker inside each conjunct, none for 'n').
    Term coordination on one noun gives «A Nနှင့် B N» / «A N၊ B Nနှင့် C N». Returns (Burmese, plural, n_terms)."""
    words = list(words)
    txt = " ".join(words)
    for k in FIXED:
        if " ca " in k and k in txt:
            txt = txt.replace(k, k.replace(" ", "\u0002"))
    words = txt.split()
    # term coordination: all words before the noun are §T§ terms joined by ca / -ñca
    if all(w.startswith("§T§") or w == "ca" for w in words[:-1]) and sum(w.startswith("§T§") for w in words) > 1:
        head = words[-1]
        hmy, _, pl = NOUN[head]
        n_t = sum(w.startswith("§T§") for w in words)
        vals = [f"{next(terms)} {hmy}" for _ in range(n_t)]
        joined = (C + " ").join(vals[:-1]) + "နှင့် " + vals[-1] if len(vals) > 2 else vals[0] + "နှင့် " + vals[1]
        pl = True if words[-1] in ("dhammā",) else pl
        return joined + _mark(pl, None, role), pl, n_t
    parts = _conj(words)
    if parts:
        out, nt = [], 0
        for p in parts:
            ph, _, pl, k = np_parse(p, terms)
            nt += k
            out.append(ph + _mark(pl, "x", role if role != "n" else "") + LAKAUNG)
        return (C + " ").join(out), True, nt
    ph, _, pl, nt = np_parse(words, terms)
    num = re.search(r" (?:" + "|".join(PAA.values()) + r")$", ph)
    return ph + _mark(pl, num, role), pl, nt


def _mark(pl, num, role):
    case = CASE[role]
    if not pl:
        return case
    if case:
        return "တို့" + case
    return "" if num else "များ"


# ===================================================================================== headings
HEAD = {
    "(Paṭhamo bhāgo)": "(ပထမ အပိုင်း)",
    "Dhammānulome": "သဘောတရား အဟုတ်ပြ ပုံစံ၌",
    "Tikapaṭṭhānaṃ": f"သုံးမျိုးတွဲတို့၏ {TITLE}",
    "Paccayuddeso": "အကြောင်းများ၏ အကျဉ်း ဖော်ပြချက်",
    "Paccayaniddeso": "အကြောင်းများ၏ အကျယ် ဖော်ပြချက်",
    "Pucchāvāro": "အမေးအလိုက် ဖော်ပြချက်",
    "Paccayānulomaṃ": "အကြောင်း အဟုတ်ပြ ပုံစံ",
    "Paccayapaccanīyaṃ": "အကြောင်း အငြင်းပြ ပုံစံ",
    "Paccayānulomapaccanīyaṃ": "အကြောင်း အဟုတ်ပြ အငြင်းပြ ပုံစံ",
    "Paccayapaccanīyānulomaṃ": "အကြောင်း အငြင်းပြ အဟုတ်ပြ ပုံစံ",
    "Ekamūlakaṃ": "အကြောင်း တစ်ခုကို အခြေခံခြင်း",
    "Dumūlakaṃ": "အကြောင်း နှစ်ခုကို အခြေခံခြင်း",
    "Timūlakaṃ": "အကြောင်း သုံးခုကို အခြေခံခြင်း",
    "Catumūlakaṃ": "အကြောင်း လေးခုကို အခြေခံခြင်း",
    "Pañcamūlakaṃ": "အကြောင်း ငါးခုကို အခြေခံခြင်း",
    "Sabbamūlakaṃ": "အကြောင်း အားလုံးကို အခြေခံခြင်း",
    "Dumūlakādi": "အကြောင်း နှစ်ခုကို အခြေခံခြင်း စသည်",
    "Paṭiccavāro": "မှီ၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်",
    "Sahajātavāro": "အတူ ပေါ်ပေါက်ခြင်းအလိုက် ဖော်ပြချက်",
    "Paccayavāro": "အကြောင်းပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်",
    "Nissayavāro": "အမှီပြု၍ ဖြစ်ပေါ်ခြင်းအလိုက် ဖော်ပြချက်",
    "Saṃsaṭṭhavāro": "ရောနှောခြင်းအလိုက် ဖော်ပြချက်",
    "Sampayuttavāro": "ယှဉ်တွဲခြင်းအလိုက် ဖော်ပြချက်",
    "Pañhāvāro": "ပြဿနာအလိုက် ဖော်ပြချက်",
    "Vibhaṅgavāro": "ခွဲခြမ်းစိတ်ဖြာခြင်းအလိုက် ဖော်ပြချက်",
    "Saṅkhyāvāro": "ရေတွက်ခြင်းအလိုက် ဖော်ပြချက်",
    "Suddhaṃ": "ရိုးရိုး",
    "Paccanīyuddhāro": "အငြင်းပြ ပုံစံအတွက် ထုတ်နုတ်ချက်",
    "Ghaṭanā": "ပေါင်းစပ်ချက်",
    "Sāmaññaghaṭanā": "သာမန် ပေါင်းစပ်ချက်",
    "Pakiṇṇakaghaṭanā": "အထွေထွေ ပေါင်းစပ်ချက်",
    "Saindriya-maggaghaṭanā": f"{cname('indriya')}နှင့် {cname('magga')} ပါဝင်သော ပေါင်းစပ်ချက်",
    "Sādhipati-indriya-maggaghaṭanā": f"{cname('adhipati')}၊ {cname('indriya')}နှင့် {cname('magga')} ပါဝင်သော "
                                      "ပေါင်းစပ်ချက်",
}
W("uddeso", "အကျဉ်း ဖော်ပြချက်", "6")
W("niddeso", "အကျယ် ဖော်ပြချက်", "6")
W("anulomaṃ", "အဟုတ်ပြ ပုံစံ", "6", key="anulomaṃ (the positive method; heading)")
W("Suddhakhandhavāro", "ရိုးရိုး အစုအဝေး ဖော်ပြချက်", "6")
TIKA = W("tikaṃ", "သုံးမျိုးတွဲ", "1")            # tika (a mātikā triad; also a counting group of three)
DUKA = W("dukaṃ", "နှစ်မျိုးတွဲ", "1")
PADA = "ပုဒ်"                                      # padaṃ (pi-? termbase «ပုဒ်»)
VARA = "အလိုက် ဖော်ပြချက်"
TIKA_NAME = {"Vedanāttikaṃ": W("Vedanātikaṃ", f"ခံစားမှု {TIKA}", "2", "^2-18-10-2-0"),     # pi-2 spells Vedanātikaṃ
             "Kusalattikaṃ": W("Kusalattikaṃ", f"ကုသိုလ် {TIKA}", "2", "^2-18-10-1-0"),
             "kusalattikassa": f"ကုသိုလ် {TIKA}၏", "kusalattikaṃ": f"ကုသိုလ် {TIKA}ကို"}
W("Vipākattikaṃ", "ကံ၏ အကျိုး သုံးမျိုးတွဲ", "2")
# counting groups (how many conditions are taken together) «X မျိုးတွဲ» (pi-1 / pi-2 / pi-5 «… မျိုးတွဲ»)
GROUP = {"duka": DUKA, "dukāni": f"{DUKA}များ", "tika": TIKA, "catukka": W("catukkaṃ", "လေးမျိုးတွဲ", "2"),
         "pañcaka": "ငါးမျိုးတွဲ", "chakka": "ခြောက်မျိုးတွဲ", "sattaka": "ခုနစ်မျိုးတွဲ", "aṭṭhaka": "ရှစ်မျိုးတွဲ",
         "navaka": "ကိုးမျိုးတွဲ", "dasaka": "ဆယ်မျိုးတွဲ", "tevīsaka": "နှစ်ဆယ့်သုံးမျိုးတွဲ",
         "catuvīsaka": "နှစ်ဆယ့်လေးမျိုးတွဲ"}
ADI = "စသည်"                                      # -ādi (pi-3 / pi-6 «X စသည်»)
SABHAGA = "နှင့် တွဲဖက်သည်များ"                  # X-sabhāgaṃ «Nဟူသော အကြောင်းနှင့် တွဲဖက်သည်များ» (NEW)
MULAKA = "ကို အခြေခံခြင်း"                        # X-mūlakaṃ «Nဟူသော အကြောင်းကို အခြေခံခြင်း»
GHATANA = "ပေါင်းစပ်ချက်"
PAREN = {"saupanissayaṃ": f"{cond('upanissaya', 'n')} ပါဝင်သော", "sakammaṃ": f"{cond('kamma', 'n')} ပါဝင်သော"}


def _cond_word(w):
    """'Nahetu' / 'Hetu' / 'Napacchājāta' -> (stem, neg) or None."""
    lw = w.lower()
    for pre in ("no", "na", ""):
        if lw.startswith(pre) and lw[len(pre):] in STEMS:
            return lw[len(pre):], bool(pre)
    return None


def _adi(w):
    if w.endswith("ādi"):
        base = w[:-3]
        return (base if _cond_word(base) else base + "a"), True
    return w, False


TRIAD_PADA = {"kusal": "ကုသိုလ်", "akusal": "အကုသိုလ်", "abyākat": ABY}


def _split_triad(s):
    s = s.lower()
    out = []
    while s:
        for k, n in (("akusal", 6), ("kusal", 5), ("abyākat", 7), ("ābyākat", 7), ("ākusal", 6)):
            if s.startswith(k):
                out.append({"ābyākat": "abyākat", "ākusal": "akusal"}.get(k, k))
                s = s[n:]
                if s.startswith("a") and not s.startswith(("akusal", "abyākat")):
                    s = s[1:]
                break
        else:
            raise KeyError("triad split: " + s)
    return out


def _join_and(vals):
    if len(vals) == 1:
        return vals[0]
    return (C + " ").join(vals[:-1]) + "နှင့် " + vals[-1]


def heading(text):
    """Translate a heading text (without #, ID). Keeps «*…*», a leading «(n) » / «(n.) », a trailing « (n)» and «.»."""
    star = text.startswith("*") and text.endswith("*")
    t = text[1:-1] if star else text
    dot = ""
    if t.endswith(".") and t not in HEAD:
        t, dot = t[:-1], END
    num = ""
    m = re.match(r"^(\(\d+\.?\) )(.*)$", t)
    if m:
        num, t = m.groups()
    tail = ""
    m = re.match(r"^(.*?)( \(\d+\))$", t)
    if m:
        t, tail = m.group(1), m.group(2)
    paren = ""
    m = re.match(r"^(.*?) \((saupanissayaṃ|sakammaṃ)\)$", t)
    if m:
        t, paren = m.group(1), f" ({PAREN[m.group(2)]})"
    out = num + _heading(t) + paren + tail + dot
    return f"*{out}*" if star else out


def _heading(t):
    if t in HEAD:
        return HEAD[t]
    if t in TIKA_NAME:
        return TIKA_NAME[t]
    m = re.fullmatch(r"(\w+?)padaṃ", t)
    if m:
        return _join_and([TRIAD_PADA[s] for s in _split_triad(m.group(1))]) + " " + PADA
    m = re.fullmatch(r"(\w+?)paccayo", t)
    if m and _cond_word(m.group(1)):
        return cond(*_swap(_cond_word(m.group(1))), )
    m = re.fullmatch(r"(\w+?)paccayādi", t)
    if m and _cond_word(m.group(1)):
        return cond(*_swap(_cond_word(m.group(1)))) + " " + ADI
    m = re.fullmatch(r"(\w+?)-(\w+?)paccayā", t)
    if m and _cond_word(m.group(1)) and _cond_word(m.group(2)):
        return _join_and([cond(*_swap(_cond_word(g))) for g in m.groups()])
    m = re.fullmatch(r"(\w+?)sabhāgaṃ", t)
    if m and _cond_word(_adi(m.group(1))[0]):
        w, adi = _adi(m.group(1))
        return cond(*_swap(_cond_word(w))) + (f" {ADI}တို့" if adi else "") + SABHAGA
    m = re.fullmatch(r"(\w+?)mūlak(aṃ|ādi)", t)
    if m and _cond_word(m.group(1)):
        return cond(*_swap(_cond_word(m.group(1)))) + MULAKA + (" " + ADI if m.group(2) == "ādi" else "")
    m = re.fullmatch(r"(\w+?)ghaṭanā", t)
    if m and _cond_word(m.group(1)):
        return cond(*_swap(_cond_word(m.group(1)))) + "၏ " + GHATANA
    m = re.fullmatch(r"(\w+?)duk(aṃ|āni)", t)
    if m and _cond_word(_adi(m.group(1))[0]):
        w, adi = _adi(m.group(1))
        base = cond(*_swap(_cond_word(w)))
        return (f"{base} {ADI}တို့၏ {GROUP['dukāni']}" if adi else f"{base}၏ {GROUP['duka']}")
    if t.endswith("ṃ") and t.lower()[:-1] in GROUP:
        return GROUP[t.lower()[:-1]]
    raise KeyError("heading: " + t)


def _swap(sn):
    stem, neg = sn
    return stem, "n", neg


# ===================================================================================== variants {x (sī. syā.)}
SIGLA = {"sī.": "Sī.", "syā.": "Syā.", "ka.": "Ka.", "kaṃ.": "Kaṃ.", "pī.": "Pī.", "ma.": "Ma.", "?": "(မသေချာ)"}
VAR_P = W("paṭhamassa jhānassa saddo kaṇḍako", "ပါဌ်ကွဲ (Syā.)", "5")[:-len(" (Syā.)")]              # a word differs (pi-1 … pi-6 «[ပါဌ်ကွဲ (Syā.): …]»)
VAR_L = W("cātumahābhūtiko", "စာလုံးပေါင်းကွဲ (Sī., Syā.)", "2")[:-len(" (Sī., Syā.)")]   # spelling only
# The pi-7 Pāli writes variants in braces «{paccayoti (syā.)}». pi-4-mr/check_marks.py compares the number of «[»
# per line with the Pāli, so the Burmese keeps the braces with the pi-1 label inside: «{ပါဌ်ကွဲ (Syā.): paccayoti}».
VAR_OPEN, VAR_CLOSE = "{", "}"
SPELLING = set()            # inner texts that differ in spelling only; chapters add
EDNOTES = {}                # editorial notes in braces (no siglum): inner Pāli -> Burmese; chapters add
VAR_RE = re.compile(r"\{([^{}]*)\}")


def variant(inner):
    if inner in EDNOTES:
        return VAR_OPEN + EDNOTES[inner] + VAR_CLOSE
    m = re.fullmatch(r"(.*?) \(([^)]*)\)", inner.strip())
    if not m:
        raise Miss("variant / editorial note (add to EDNOTES): " + inner)
    reading, sig = m.groups()
    sig = ", ".join(SIGLA[s] for s in sig.split())
    lab = VAR_L if inner in SPELLING else VAR_P
    return f"{VAR_OPEN}{lab} ({sig}): {reading}{VAR_CLOSE}"


# ===================================================================================== verbs and link words
UP = W("uppajjati", "ဖြစ်ပေါ်သည်", "5")           # uppajjati (pi-2 / pi-5 «ဖြစ်ပေါ်သည်»)
VERB = {
    "uppajjati": "ဖြစ်ပေါ်သည်",
    "uppajjanti": "ဖြစ်ပေါ်ကြသည်",
    "uppajjeyya": "ဖြစ်ပေါ်နိုင်သလော",            # Siyā … uppajjeyya: «… ဖြစ်ပေါ်နိုင်သလော» (NEW)
    "uppajjeyyuṃ": "ဖြစ်ပေါ်နိုင်ကြသလော",
}
W("Cakkhuñca paṭicca rūpe ca uppajjati cittaṃ", "အဆင်းအရောင်တို့ကိုလည်းကောင်း မှီ၍", "2")      # paṭicca «… ကို မှီ၍» (pi-2, pi-5)
W("yaṃ cakkhuṃ nissāya rūpaṃ ārabbha", "ထို မျက်စိကို မှီ၍ အဆင်းအရောင်ကို အာရုံပြု၍", "1")   # nissāya / ārabbha
W("kammena sahajāto kammūpacayo", "ကံနှင့်အတူ ပေါ်ပေါက်သော ကံ၏ စုဆောင်းမှု", "5")              # sahajāto
W("cittasaṃsaṭṭhā", "စိတ်နှင့် ရောနှောသော", "2")                                              # saṃsaṭṭha
# link word -> function(np Burmese (case-less, with plural «တို့» if plural), plural) -> Burmese
LINK = {
    "paṭicca": lambda a: f"{a}ကို မှီ၍",
    "nissāya": lambda a: f"{a}ကို မှီ၍",
    "paccayā": lambda a: f"{a}{KYAUNG}",
    "sahajāto": lambda a: f"{a}နှင့်အတူ ပေါ်ပေါက်သော",
    "saṃsaṭṭho": lambda a: f"{a}နှင့် ရောနှောသော",
    "sampayutto": lambda a: f"{a}နှင့် ယှဉ်တွဲသော",
    "sampayuttā": lambda a: f"{a}နှင့် ယှဉ်တွဲသော",
    "ārabbha": lambda a: f"{a}ကို အာရုံပြု၍",
}
SADISA = "နှင့် တူသည်"            # X-sadisaṃ «… နှင့် တူသည်» (NEW)
PARIPUNNA = f"{PATISANDHI}နှင့်တကွ " + W("paripuṇṇaṃ", "ပြည့်စုံ") + "သည်"   # paripuṇṇaṃ paṭisandhikaṃ
NOTES = {"(saṃkhittaṃ)": "(" + W("saṃkhittaṃ", "အကျဉ်းချုပ်", "6") + ")",
         "(mūlakaṃ saṃkhittaṃ)": "(အခြေခံ အကြောင်းများကို အကျဉ်းချုပ်)",
         "(adhipatiyā paṭisandhi natthi)": f"({cname('adhipati')}၌ {PATISANDHI} မရှိ)",
         "(nādhipati paripuṇṇaṃ paṭisandhikaṃ)": f"({cond('adhipati', 'loc', True)} {PARIPUNNA})",
         "(napacchājātampi naāsevanampi paripuṇṇaṃ paṭisandhikaṃ)":
             f"({cond('pacchājāta', 'loc', True)}လည်း{C} {cond('āsevana', 'loc', True)}လည်း {PARIPUNNA})",
         "(anantarapaccayasadisaṃ)": f"({cname('anantara')}{SADISA})",
         "(aññamaññampi nissayampi sahajātapaccayasadisaṃ)":
             f"({cname('aññamañña')}လည်း{C} {cname('nissaya')}လည်း {cname('sahajāta')}{SADISA})",
         "(anantarasadisaṃ)": f"({N['anantara']}{SADISA})",
         "(nakammapaccayasadisaṃ)": f"({cond('kamma', 'n', True)}{SADISA})",
         '(saddhāpañcamakesu "mānaṃ jappeti, diṭṭhiṃ gaṇhātī"ti kātabbaṃ, avasesesu na kātabbaṃ)':
             "(ယုံကြည်မှု စသော ငါးပါးတို့၌ “မာနကို ဖြစ်ပေါ်စေသည်၊ အယူကို စွဲယူသည်”ဟု ထည့်ရမည်၊ "
             "ကြွင်းသည်တို့၌ မထည့်ရ)"}


# ===================================================================================== slotter and renderer
def slot(unit):
    """Pāli unit -> (skeleton, slots). Slots in Pāli order: V variant, T triad term (Pāli ending kept after «§T§»),
    K count «hetuyā tīṇi», C condition word (ending kept: §C§ā §C§ena §C§o §C§opi §C§oti), D «(n)»."""
    slots = {"V": [], "T": [], "K": [], "C": [], "D": []}

    def sub_v(m):
        slots["V"].append(variant(m.group(1)))
        return "§V§"
    s = VAR_RE.sub(sub_v, unit)

    def sub_t(m):
        slots["T"].append(term_value(m))
        hit = next(v for v in m.groupdict().values() if v)
        return "§T§" + m[0][len(hit):]
    s = TERM_RE.sub(sub_t, s)

    def sub_k(m):
        slots["K"].append((LOC2STEM[m["loc"].lower()], bool(m["neg"]), m["num"]))
        return "§K§"
    s = COUNT_RE.sub(sub_k, s)

    def sub_c(m):
        slots["C"].append((m["stem"].lower(), bool(m["neg"])))
        return "§C§" + m["end"]
    s = COND_RE.sub(sub_c, s)

    def sub_d(m):
        slots["D"].append(m[0])
        return "§D§"
    s = re.sub(r"\(\d+\)", sub_d, s)
    return s, slots


FIELD_RE = re.compile(r"\{(?P<k>[TCKDV])(?P<i>\d+)(?:\.(?P<f>[a-z]+))?\}")


def render(tpl, slots):
    """Fill a template: {T1} term, {C1.ab|loc|n|i|pi|obj|gen|bare|if} condition ('if' = the whole
    «… အကြောင်းဖြင့် အကြောင်း ဖြစ်သည်»), {K1} count, {D1} digits, {V1} variant. Every slot must be used once."""
    if callable(tpl):
        return tpl(slots)
    used = {k: set() for k in slots}

    def f(m):
        k, i, fm = m["k"], int(m["i"]) - 1, m["f"]
        used[k].add(i)
        v = slots[k][i]
        if k == "C":
            stem, neg = v
            if fm in ("if", "ifn"):
                if neg:
                    raise ValueError("negated condition in an instrumental frame")
                return iframe(stem, fm == "ifn")
            return cond(stem, fm or "ab", neg)
        if k == "K":
            return count_my(*v)
        return v
    out = FIELD_RE.sub(f, tpl)
    for k, vals in slots.items():
        if len(used[k]) != len(vals):
            raise ValueError(f"template uses {k} {sorted(used[k])} of {len(vals)}: {tpl}")
    return out


# ===================================================================================== frames
def _chain_tok():
    notes = "|".join(re.escape(k) for k in sorted(NOTES, key=len, reverse=True))
    return re.compile(r"na §C§ena paccayo|§C§ena paccayo|§C§ā|§K§|§D§|§V§|kiñci kāle|" + notes)


KINCI_KALE = "အချို့သော အချိန်၌"      # kiñci kāle (NEW)


def chain(s, slots, ci, ki, di, vi=None):
    """A condition chain / counting fragment, token by token in Pāli order. Between the last ablative and a
    following count a «၊» is put («A-ကြောင့်၊ B-၌ သုံးခု»); «, » between counts becomes «၊ »."""
    out, pos, prev = [], 0, None
    for m in _chain_tok().finditer(s):
        gap = s[pos:m.start()]
        if gap.strip(" ,"):
            raise KeyError("chain gap: " + repr(gap) + " in " + s)
        gap = gap.replace(",", C)
        tok = m[0]
        if tok == "§C§ā":
            stem, neg = slots["C"][ci[0]]
            ci[0] += 1
            my, kind = cond(stem, "ab", neg), "ab"
        elif tok == "§K§":
            my, kind = count_my(*slots["K"][ki[0]]), "K"
            ki[0] += 1
            if prev == "ab" and gap == " ":
                gap = C + " "
        elif tok.endswith("ena paccayo"):
            stem, neg = slots["C"][ci[0]]
            ci[0] += 1
            if neg:
                raise KeyError("negated instrumental")
            my, kind = iframe(stem, tok.startswith("na ")), "i"
        elif tok == "§D§":
            my, kind = slots["D"][di[0]], "D"
            di[0] += 1
        elif tok == "§V§":
            if vi is None:
                raise KeyError("variant in a chain")
            my, kind = slots["V"][vi[0]], "V"
            vi[0] += 1
        elif tok == "kiñci kāle":
            my, kind = KINCI_KALE, "adv"
        else:
            my, kind = NOTES[tok], "note"
        out.append(gap + my)
        prev = kind
        pos = m.end()
    tail = s[pos:]
    if tail.strip(" .,;"):
        raise KeyError("chain tail: " + repr(tail) + " in " + s)
    return "".join(out) + punct(tail)


def punct(t):
    """Pāli end punctuation -> Burmese: «.» «။», «,» / «;» «၊»."""
    return t.replace(".", END).replace(";", C).replace(",", C)


_NOUN_ANY = None
CLAUSE_RE = None


def _clause_re():
    nouns = "|".join(sorted(set(NOUN) | {k.split()[-1] for k in FIXED}, key=len, reverse=True))
    return re.compile(
        r"^(?P<lead>[\s(]*)(?P<siya>[Ss]iyā )?(?:(?P<pre>(?:" + "|".join(PREFIX) + r")) )?"
        r"(?:(?P<a>(?:[^\s…]+ )*?(?:" + nouns + r")) (?P<link>" + "|".join(LINK) + r")(?: |$))?"
        r"(?:(?P<b>(?:[^\s…]+ )*?(?:" + nouns + r")) (?P<v>" + "|".join(VERB) + r")(?: |$))?"
        r"(?P<ch>.*?)(?P<trail>[\s.,;]*)$")


HELD = []      # the verb held back by clause(hold=True), for the last fragment of the sentence


def clause(frag, slots, ti, ci, ki, di, hold=False):
    """One fragment of a paṭicca-type sentence: [siyā] [prefix] [NP-acc LINK] [NP-nom VERB] [condition chain].
    Burmese order: [prefix] [NP LINK] [NP-သည်] [chain] [verb]."""
    m = CLAUSE_RE.match(frag)
    if not m or not (m["a"] or m["b"] or m["ch"].strip()):
        raise KeyError("clause: " + frag)
    if m["siya"] and not m["v"]:
        raise KeyError("siyā without verb: " + frag)
    terms = iter(slots["T"][ti[0]:])
    parts = [m["lead"]]
    if m["pre"]:
        parts.append(PREFIX[m["pre"]] + " ")
    used = 0
    if m["a"]:
        aw = m["a"].split()
        a_my, _, k = np_my(aw, terms, "")
        a_my = re.sub(r"များ$", "တို့", a_my)
        used += k
        parts.append(LINK[m["link"]](a_my))
        parts.append(" " if (m["b"] or m["ch"].strip()) else "")
    if m["b"]:
        bw = m["b"].split()
        role = "n" if (m["ch"].strip() or m["a"]) else ""
        b_my, bpl, k = np_my(bw, terms, "n")
        used += k
        parts.append(b_my + " ")
    ti[0] += used
    ch = m["ch"]
    note = ""
    for k in sorted(NOTES, key=len, reverse=True):
        if ch.endswith(" " + k) and m["v"]:
            ch, note = ch[:-len(k) - 1], k
            break
    if ch.strip():
        parts.append(chain(ch, slots, ci, ki, di))
        if m["v"]:
            parts.append(" ")
    if m["v"]:
        if hold:
            HELD.append(VERB[m["v"]])
            if parts and parts[-1] == " ":
                parts.pop()
        else:
            parts.append(VERB[m["v"]])
    if note:
        parts.append(" " + NOTES[note])
    return "".join(parts).rstrip(" ") + punct(m["trail"])


def pairs(s, slots, ti):
    """«[prefix] NP-acc LINK NP-nom, NP-acc LINK NP-nom» (no verb), pairs separated by «, »."""
    out = []
    for part in s.split(", "):
        pm = re.match(r"^(?P<pre>(?:" + "|".join(map(re.escape, PREFIX)) + r") )?(?P<a>.+?) (?P<link>"
                      + "|".join(LINK) + r") (?P<b>.+)$", part)
        if not pm:
            raise KeyError("pair: " + part)
        terms = iter(slots["T"][ti[0]:])
        aw, bw = pm["a"].split(), pm["b"].split()
        a_my, _, k1 = np_my(aw, terms, "")
        a_my = re.sub(r"များ$", "တို့", a_my)
        b_my, _, k2 = np_my(bw, terms, "")
        ti[0] += k1 + k2
        pre = PREFIX[pm["pre"].strip()] + " " if pm["pre"] else ""
        out.append(pre + LINK[pm["link"]](a_my) + " " + b_my)
    return (C + " ").join(out)


# ------------------------------------------------------------------ the pañhāvāra frame
def _nom_re():
    ks = [k for k, v in NOUN.items() if v[1] == "n"] + [k for k, v in FIXED.items() if v[1] == "n"]
    return "|".join(sorted((re.escape(k) for k in ks), key=len, reverse=True))


def _gen_re():
    ks = [k for k, v in NOUN.items() if v[1] == "g"] + [k for k, v in FIXED.items() if v[1] == "g"]
    return "|".join(sorted((re.escape(k) for k in ks), key=len, reverse=True))


PANHA_RE = None


def _panha_re():
    pre = "|".join(map(re.escape, PREFIX))
    return re.compile(r"^(?P<pre>(?:" + pre + r") )?(?:(?P<a>(?:\S+ )*?(?:" + _nom_re() + r"))(?P<pi>pi)? )?"
                      r"(?:(?P<b>(?:\S+ )*?(?:" + _gen_re() + r"(?:ñca)?))(?P<ks> kesañci)? )?"
                      r"(?P<adv>aññamaññaṃ )?(?P<rest>(?:kiñci kāle (?:§V§ )?)?(?:na )?§C§ena paccayo.*)$")


AMONG_SOME = "တို့အနက် အချို့အား"      # kesañci after a recipient: «… သဘောတရားတို့အနက် အချို့အား» (NEW)
ANNAMANNAM = W("aññamaññapaccayā", "အချင်းချင်း", "5")    # aññamaññaṃ (adverb)
PI = "လည်း"                          # -pi «…သည်လည်း»


def panha(sk, slots):
    """«[prefix] NP-nom [NP-dat [kesañci]] [aññamaññaṃ] [kiñci kāle] [na] Xpaccayena paccayo[…]» =
    «[prefix] NP-သည် [NP-အား] [အချင်းချင်း] … Nဟူသော အကြောင်းဖြင့် အကြောင်း ဖြစ်သည်». Every split point between
    the two noun phrases is tried; the first that renders wins."""
    m = re.search(r"(?:^| )((?:kiñci kāle (?:§V§ )?)?(?:na )?§C§ena paccayo.*)$", sk)
    if not m:
        return None
    rest = m.group(1)
    head = sk[:m.start(1)].strip()
    words = head.split() if head else []
    pre = ""
    if words and words[0] in PREFIX:
        pre = PREFIX[words[0]] + " "
        words = words[1:]
    adv = ""
    if words and words[-1] == "aññamaññaṃ":
        adv = ANNAMANNAM + " "
        words = words[:-1]
    some = False
    if words and words[-1] == "kesañci":
        some = True
        words = words[:-1]
    if not words:
        return None
    nt = len(slots["T"])
    best = None
    for j in range(len(words), -1, -1):
        aw, bw = words[:j], words[j:]
        pi = False
        if aw and aw[-1].endswith("pi") and aw[-1][:-2] in NOUN:
            aw = aw[:-1] + [aw[-1][:-2]]
            pi = True
        terms = iter(slots["T"])
        try:
            a_my, k1 = "", 0
            if aw:
                if not (_case_of(aw) == "n"):
                    continue
                a_my, _, k1 = np_my(aw, terms, "n")
            b_my, k2 = "", 0
            if bw:
                if _case_of(bw) != "g":
                    continue
                b_my, _, k2 = np_my(bw, terms, "g")
        except (KeyError, StopIteration):
            continue
        if k1 + k2 != nt:
            continue
        if some:
            if not b_my.endswith("တို့အား"):
                continue
            b_my = b_my[:-len("တို့အား")] + AMONG_SOME
        best = (a_my + (PI if pi else ""), b_my)
        break
    if best is None or slots["K"]:
        return None
    a_my, b_my = best
    ci, ki, di, vi = [0], [0], [0], [0]
    try:
        r = PE.join(chain(p, slots, ci, ki, di, vi) for p in rest.split(PE))
    except KeyError:
        return None
    if ci[0] != len(slots["C"]) or di[0] != len(slots["D"]) or vi[0] != len(slots["V"]):
        return None
    return pre + (f"{a_my} " if a_my else "") + (f"{b_my} " if b_my else "") + adv + r


def _case_of(words):
    """Case of the last conjunct's head noun of an NP word list ('n', 'g', … or None)."""
    if len(words) > 1 and words[-1] in POSTQUAL:
        words = words[:-1]
    txt = " ".join(words)
    for k, (_, c, _) in FIXED.items():
        if txt.endswith(k):
            return c
    w = words[-1]
    if w in NOUN:
        return NOUN[w][1]
    if w in FIXED:
        return FIXED[w][1]
    return None


# ------------------------------------------------------------------ ghaṭanā lines
GHATANA_RE = None


def segment_conds(compound):
    """'Hetu-sahajātaaññamañña-nissaya' (with source slips: missing hyphens, a space, «sahajātaṃ», sandhi
    «ārammaṇādhipati», «adhipatīti») -> (stems, slips)."""
    slips = []
    c = compound.replace(" -", "-").replace("- ", "-")
    if c != compound:
        slips.append("space at a hyphen")
    out = []
    for part in c.split("-"):
        p = part.lower()
        if p.endswith("ṃ") and p[:-1] in STEMS:
            slips.append(f"«{part}» for «{part[:-1]}»")
            p = p[:-1]
        first = True
        while p:
            for st in sorted(STEMS, key=len, reverse=True):
                cand = [st, st[:-1] + "ā"] if st.endswith(("a", "u")) else [st]
                hit = next((x for x in cand if p.startswith(x)), None)
                if hit:
                    out.append(st)
                    p = p[len(hit):]
                    if hit != st:
                        p = "a" + p
                    elif p:
                        slips.append(f"no hyphen before «{p}»")
                    break
            else:
                raise KeyError("ghaṭanā stem: " + part)
            first = False
    return out, slips


def ghatana_list(stems):
    return f"{(C + ' ').join(cond(st, 'bare') for st in stems)} {HUTHO} {GHATANA}"


def ghatana(s):
    """Every «A-B-…-Znti N» item of a line -> «A၊ B၊ … Z ဟူသော ပေါင်းစပ်ချက်၌ N». Returns (Burmese, slips)."""
    slips = []

    def f(m):
        raw = m["c"]
        if raw.endswith("adhipat"):
            raw += "i"
        stems, sl = segment_conds(raw)
        slips.extend(sl)
        return f"{ghatana_list(stems)}၌ {COUNT[m['n']]}" + punct(m["end"])
    out = GHATANA_RE.sub(f, s)
    return out, slips


# ===================================================================================== the phrase lexicon (LEX)
# For the long pañhāvāra paragraphs (ārammaṇa, adhipati, anantara, upanissaya …) whose word order Burmese shares
# with the Pāli (object before verb, qualifier before noun). Each entry: Pāli phrase (lower case, words split by one
# space; «§T§» words stand for a triad term) -> (Burmese, kind). Kinds:
#   n nominative item, a accusative item, na neuter item (nominative or accusative), g recipient (dative «အား»),
#   G genitive «၏», i instrumental «ဖြင့်», b ablative «မှ», l locative «၌», adj qualifier (no marker),
#   v verb or clause end (a nominative before it stays bare), x fixed text, post (joins the item before it).
# A plural item is given with «+» at the end of its Burmese («အစုအဝေး+»): «…တို့» before a marker, «…များ» bare.
# Item markers: n «သည်» unless the next word is a verb or nothing follows in the fragment; a / na «ကို» unless
# nothing follows (then bare) or a post word follows (it brings its own «ကို»); na before a recipient = n.
LEX = {}
MARK = {"n": "သည်", "a": "ကို", "g": "အား", "G": "၏", "i": "ဖြင့်", "b": "မှ", "l": "၌"}


def add_lex(kind, table):
    for k, v in table.items():
        LEX[k] = (v, kind)


# --- terms of the term tails: «§T§ādhipati» (sukhāya vedanāya sampayuttādhipati) …
TAIL = {"ādhipati": (N["adhipati"], "n"), "acittasamaṅgissa": ("စိတ်နှင့် ပြည့်စုံသူ", "G"),
        "apaṭisandhi": (PATISANDHI, "na")}
add_lex("n", {"ariyā": W("ariyā", "အရိယာ") + "+", "khandhā": KHANDHA + "+", "eko khandho": f"{KHANDHA} {PAA[1]}",
              "dve khandhā": f"{KHANDHA} {PAA[2]}+", "saddhā": W("saddhā", "ယုံကြည်မှု"),
              "cāgo": W("cāgo", "စွန့်လွှတ်ခြင်း"), "paññā": W("paññā", "ပညာ"), "rāgo": W("rāgo", "ရာဂ"),
              "moho": W("moho", "မောဟ"), "māno": W("māno", "မာန"), "diṭṭhi": W("diṭṭhi", "အယူ"),
              "patthanā": W("patthanā", "တောင့်တခြင်း"), "doso": W("doso", "ဒေါသ"),
              "vicikicchā": W("vicikicchā", "ယုံမှားမှု"), "uddhaccaṃ": W("uddhaccaṃ", "ယောက်ယက်ခတ်မှု"),
              "domanassaṃ": W("domanassaṃ", "စိတ်ဆင်းရဲမှု"), "cetanā": "စေ့ဆော်မှု",
              "āvajjanā": "စိတ်ညွတ်ခြင်း", "maggo": W("maggo", "မဂ်"), "gotrabhu": "အနွယ် ပြောင်းခြင်း စိတ်",
              "vipākamanodhātu": W("vipākamanodhātu", "ကံ၏ အကျိုး ဖြစ်သော မနော ဓာတ်"),
              "vipākamanoviññāṇadhātu": "ကံ၏ အကျိုး ဖြစ်သော မနော သိစိတ် ဓာတ်"})
add_lex("na", {"sīlaṃ": W("sīlaṃ", "သီလ"), "sutaṃ": W("sutaṃ", "အကြားအမြင်"),
               "dukkhasahagataṃ kāyaviññāṇaṃ": f"{QUAL['dukkhasahagataṃ']} {KAYAVINNANA}",
               "sukhasahagataṃ kāyaviññāṇaṃ": f"{QUAL['sukhasahagataṃ']} {KAYAVINNANA}",
               "anulomaṃ": "လျော်ညီခြင်း စိတ်", "vodānaṃ": W("vodānaṃ", "စင်ကြယ်ခြင်း") + " စိတ်",
               "phalaṃ": W("phalaṃ", "ဖိုလ်"), "kiriyaṃ": W("kiriyaṃ", "ပြုရုံမျှသာ ဖြစ်သော") + " စိတ်",
               "kusalākusalaṃ": W("kusalākusale", "ကုသိုလ်နှင့် အကုသိုလ်"),
               "cuticittaṃ": W("cuti", "စုတေခြင်း", "2") + " စိတ်", "bhavaṅgaṃ": "ဘဝင် စိတ်",
               "cittaṃ": W("cittaṃ", "စိတ်"),
               "nevasaññānāsaññāyatanaṃ": W("nevasaññānāsaññāyatanaṃ",
                                           "မှတ်သိမှု ရှိသည်လည်း မဟုတ်၊ မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ်"),
               "ākāsānañcāyatanaṃ": W("ākāsānañcāyatanaṃ", "အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ်"),
               "ākiñcaññāyatanaṃ": W("ākiñcaññāyatanaṃ", "ဘာမျှ မရှိသော နယ်ပယ်"), "vatthuṃ": VATTHU})
add_lex("a", {"saddhaṃ": "ယုံကြည်မှု", "cāgaṃ": "စွန့်လွှတ်ခြင်း", "paññaṃ": "ပညာ", "rāgaṃ": "ရာဂ", "mohaṃ": "မောဟ",
              "mānaṃ": "မာန", "diṭṭhiṃ": "အယူ", "patthanaṃ": "တောင့်တခြင်း", "dosaṃ": "ဒေါသ",
              "khandhe": KHANDHA + "+", "taṃ": "ထိုအရာ", "dve khandhe": f"{KHANDHA} {PAA[2]}+",
              "pahīne kilese": "ပယ်ပြီးသော " + W("kilese", "ကိလေသာ") + "+",
              "vikkhambhite kilese": "ခွာထားပြီးသော ကိလေသာ+",
              "pubbe samudāciṇṇe kilese": W("pubbe", "ရှေး") + "က ဖြစ်ခဲ့ဖူးသော ကိလေသာ+"})
add_lex("g", {"saddhāya": "ယုံကြည်မှု", "sīlassa": "သီလ", "sutassa": "အကြားအမြင်", "cāgassa": "စွန့်လွှတ်ခြင်း",
              "paññāya": "ပညာ", "rāgassa": "ရာဂ", "mohassa": "မောဟ", "mānassa": "မာန", "diṭṭhiyā": "အယူ",
              "patthanāya": "တောင့်တခြင်း", "dosassa": "ဒေါသ",
              "dukkhasahagatassa kāyaviññāṇassa": f"{QUAL['dukkhasahagataṃ']} {KAYAVINNANA}",
              "sukhasahagatassa kāyaviññāṇassa": f"{QUAL['sukhasahagataṃ']} {KAYAVINNANA}",
              "khandhānaṃ": KHANDHA + "+", "dvinnaṃ khandhānaṃ": f"{KHANDHA} {PAA[2]}+",
              "sampayuttakānaṃ khandhānaṃ": f"{QUAL['sampayuttakānaṃ']} {KHANDHA}+",
              "ekassa khandhassa": f"{KHANDHA} {PAA[1]}",
              "cetopariyañāṇassa": W("cetopariyāye ñāṇaṃ", "စိတ်ကို ပိုင်းခြား၍ သိသော ဉာဏ်"),
              "pubbenivāsānussatiñāṇassa": W("pubbenivāsānussati ñāṇaṃ", "ရှေးဘဝများကို အဖန်ဖန် အောက်မေ့နိုင်သော ဉာဏ်"),
              "yathākammūpagañāṇassa": "ကံအားလျော်စွာ ဖြစ်ပေါ်ပုံကို သိသော ဉာဏ်",
              "anāgataṃsañāṇassa": "အနာဂတ်ကို သိသော ဉာဏ်",
              "iddhividhañāṇassa": "တန်ခိုး အမျိုးမျိုးကို ပြနိုင်သော ဉာဏ်",
              "āvajjanāya": "စိတ်ညွတ်ခြင်း", "gotrabhussa": "အနွယ် ပြောင်းခြင်း စိတ်",
              "vodānassa": "စင်ကြယ်ခြင်း စိတ်", "maggassa": "မဂ်", "phalassa": "ဖိုလ်",
              "phalasamāpattiyā": "ဖိုလ်သမာပတ်", "vuṭṭhānassa": W("vuṭṭhānaṃ", "ထမြောက်ခြင်း") + " စိတ်",
              "upapatticittassa": W("upapatti", "ပြန်လည် ဖြစ်ပေါ်ခြင်း") + " စိတ်", "bhavaṅgassa": "ဘဝင် စိတ်",
              "vipākamanodhātuyā": "ကံ၏ အကျိုး ဖြစ်သော မနော ဓာတ်",
              "vipākamanoviññāṇadhātuyā": "ကံ၏ အကျိုး ဖြစ်သော မနော သိစိတ် ဓာတ်",
              "kiriyamanoviññāṇadhātuyā": "ပြုရုံမျှသာ ဖြစ်သော မနော သိစိတ် ဓာတ်",
              "viññāṇañcāyatanassa": W("viññāṇañcāyatanassa", "အဆုံး မရှိသော သိစိတ် နယ်ပယ်"),
              "nevasaññānāsaññāyatanassa": "မှတ်သိမှု ရှိသည်လည်း မဟုတ်၊ မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ်",
              "vippaṭisārissa": "နောင်တ ရသူ"})          # pi-4 termbase vippaṭisārī «နောင်တ ရသော»
add_lex("G", {"nirodhā vuṭṭhahantassa": W("nirodhasamāpatti", "ချုပ်ငြိမ်းခြင်း သမာပတ်") + "မှ ထမြောက်နေသူ"})
add_lex("i", {"cittena": "စိတ်", "cetopariyañāṇena": "စိတ်ကို ပိုင်းခြား၍ သိသော ဉာဏ်",
              "duṭṭhena cittena": W("duṭṭhena", "ပြစ်မှားသော") + " စိတ်"})
add_lex("b", {"jhānā": "ဈာန်", "maggā": "မဂ်", "phalā": "ဖိုလ်"})
add_lex("adj", {"vipāko": VIPAKA_ADJ})
GARU = W("ariyaṃ dhammaṃ garuṃ katvā", "လေးစားဖွယ်ရာ ပြု၍", "5")
add_lex("post", {"upanissāya": "ကို အားကြီးစွာ မှီ၍", "ārabbha": "ကို အာရုံပြု၍", "garuṃ katvā": f"ကို {GARU}"})
add_lex("v", {"uppajjati": UP, "uppajjanti": VERB["uppajjanti"], "paccavekkhati": "ပြန်လည် ဆင်ခြင်သည်",
              "paccavekkhanti": "ပြန်လည် ဆင်ခြင်ကြသည်", "jānāti": W("jānāti", "သိသည်"), "jānanti": "သိကြသည်",
              "vipassati": "ထိုးထွင်း၍ ရှုသည်", "assādeti abhinandati": "သာယာ နှစ်သက်သည်",
              "na labbhati": "မတွေ့ရ", "vuṭṭhahitvā": W("vuṭṭhahitvā", "ထ၍")})
add_lex("x", {
    # what is done with a mind (the deeds are pi-5 ^5-… «… ရာ» forms in the present)
    "dānaṃ datvā": W("Dānaṃ datvā", "ပေးလှူခြင်းကို ပြု၍", "2"), "sīlaṃ samādiyitvā": "သီလကို ဆောက်တည်၍",
    "uposathakammaṃ katvā": "ဥပုသ်ကို စောင့်ထိန်း၍",
    "dānaṃ deti": "ပေးလှူခြင်းကို ပြုသည်", "sīlaṃ samādiyati": "သီလကို ဆောက်တည်သည်",
    "uposathakammaṃ karoti": "ဥပုသ်ကို စောင့်ထိန်းသည်", "jhānaṃ uppādeti": "ဈာန်ကို ဖြစ်စေသည်",
    "vipassanaṃ uppādeti": "ထိုးထွင်းသိမြင်ခြင်းကို ဖြစ်စေသည်", "maggaṃ uppādeti": "မဂ်ကို ဖြစ်စေသည်",
    "abhiññaṃ uppādeti": W("abhiññaṃ", "ထူးကဲစွာ သိခြင်း") + "ကို ဖြစ်စေသည်",
    "samāpattiṃ uppādeti": W("samāpatti", "သမာပတ်", "5") + "ကို ဖြစ်စေသည်",
    "mānaṃ jappeti": "မာနကို " + W("mānaṃ jappeti", "ဖြစ်ပေါ်စေ", "2") + "သည်",
    "diṭṭhiṃ gaṇhāti": "အယူကို စွဲယူသည်",
    "pāṇaṃ hanati": W("pāṇaṃ haneyya", "သတ္တဝါကို သတ်", "5") + "သည်",
    "adinnaṃ ādiyati": "မပေးသည်ကို ယူသည်", "musā bhaṇati": "မုသား ပြောသည်",
    "pisuṇaṃ bhaṇati": "ကုန်းတိုက်သော စကားကို ပြောသည်", "pharusaṃ bhaṇati": "ကြမ်းတမ်းသော စကားကို ပြောသည်",
    "samphaṃ palapati": "အကျိုးမဲ့ ပြိန်ဖျင်းသော စကားကို ပြောသည်", "sandhiṃ chindati": "အိမ်ကို ဖောက်ထွင်းသည်",
    "nillopaṃ harati": "ဥစ္စာကို လုယူသည်", "ekāgārikaṃ karoti": "အိမ်တစ်လုံးတည်းကို ဝိုင်း၍ တိုက်သည်",
    "paripanthe tiṭṭhati": "လမ်းခရီး၌ ဓားပြ တိုက်သည်", "paradāraṃ gacchati": "သူတစ်ပါး၏ မယားထံ သွားသည်",
    "gāmaghātaṃ karoti": "ရွာကို ဖျက်ဆီး၍ လုယက်သည်", "nigamaghātaṃ karoti": "နိဂုံးကို ဖျက်ဆီး၍ လုယက်သည်",
    "mātaraṃ jīvitā voropeti": "အမိကို " + W("jīvitā voropeti", "အသက်မှ သတ်", "5") + "သည်",
    "pitaraṃ jīvitā voropeti": "အဖကို အသက်မှ သတ်သည်", "arahantaṃ jīvitā voropeti": "ရဟန္တာကို အသက်မှ သတ်သည်",
    "tathāgatassa lohitaṃ uppādeti": "မြတ်စွာဘုရား၏ " + W("lohitaṃ", "သွေး") + "ကို ထွက်စေသည်",
    "saṅghaṃ bhindati": W("saṅghaṃ", "သံဃာ") + "ကို ဖြိုခွဲသည်",
    "attānaṃ ātāpeti paritāpeti": W("attānaṃ", "မိမိကိုယ်") + "ကို ပူပန်စေ၍ ပြင်းစွာ ပူပန်စေသည်",
    "pariyiṭṭhimūlakaṃ dukkhaṃ paccanubhoti": "ရှာမှီးခြင်းကို အရင်းခံသော ဆင်းရဲကို "
                                              + W("paccanubhonti", "ခံစား") + "သည်",
    "aniccato dukkhato anattato": "မမြဲဟု၊ ဆင်းရဲဟု၊ အတ္တ မဟုတ်ဟု",
    "jhāne parihīne": "ဈာန် " + W("parihīne", "ဆုတ်ယုတ်သွားသော") + "အခါ",
    "sahajātā": "အတူ ပေါ်ပေါက်သည့် ကံ", "nānākkhaṇikā": "ခဏ ကွဲပြားသည့် ကံ",
    "ārammaṇādhipati": f"{N['ārammaṇa']} {N['adhipati']}", "sahajātādhipati": f"အတူ ပေါ်ပေါက်သော {N['adhipati']}",
    "ārammaṇūpanissayo": f"{N['ārammaṇa']}ဖြင့် {N['upanissaya']}",
    "anantarūpanissayo": f"{N['anantara']}ဖြင့် {N['upanissaya']}",
    "pakatūpanissayo": f"ပကတိ {N['upanissaya']}",
})
for _p, _my in PREFIX.items():
    LEX[_p] = (_my, "x")
for _p, _my in (("sukhāya vedanāya", "သာယာသော ခံစားမှု"), ("dukkhāya vedanāya", "နာကျင်သော ခံစားမှု"),
                ("adukkhamasukhāya vedanāya", "မနာကျင် မသာယာသော ခံစားမှု")):     # «X vedanāya…pe…» (pi-5)
    LEX[_p] = (W(_p, _my, "5"), "x")
# vipassati «ထိုးထွင်း၍ ရှုသည်» (vipassanā «ထိုးထွင်းသိမြင်ခြင်း», burmese-style.md)
LEX_SEP = {",": C, ".": END, ";": C}


def _lex_item(my, kind, nxt):
    """Render an item given the kind of the following token (None = nothing follows in the fragment)."""
    pl = my.endswith("+")
    base = my[:-1] if pl else my
    numbered = re.search(r" (?:" + "|".join(PAA.values()) + r")$", base) is not None
    if kind in ("g", "G", "i", "b", "l"):
        mark = MARK[kind]
    elif kind == "n":
        mark = "" if nxt in (None, "v", "sep") else MARK["n"]
    elif kind == "na":
        if nxt in (None, "sep", "post"):
            mark = ""
        elif nxt in ("g", "T-g"):
            mark = MARK["n"]
        else:
            mark = MARK["a"]
    elif kind == "a":
        mark = "" if nxt in (None, "sep", "post") else MARK["a"]
    else:
        return base
    if pl and not numbered:
        return base + ("တို့" + mark if (mark or nxt == "post") else "များ")
    if pl and numbered and mark:
        return base + "တို့" + mark
    return base + mark


def lex(frag, slots, ti, ci, ki, di, vi):
    """Translate one fragment through LEX (longest match), NOTES, the term slots and the condition slots."""
    text = frag.strip()
    lead, trail = frag[:len(frag) - len(frag.lstrip())], ""
    toks = []          # (kind, value) ; value: Burmese or a term index
    pos = 0
    notes = sorted(NOTES, key=len, reverse=True)
    words = text.split(" ")
    i = 0
    while i < len(words):
        rest = " ".join(words[i:])
        hit = next((k for k in notes if rest.startswith(k)), None)
        if hit:
            toks.append(("x", NOTES[hit]))
            n_w = len(hit.split(" "))
            last = words[i + n_w - 1]
            extra = last[last.rindex(hit.split(" ")[-1]) + len(hit.split(" ")[-1]):]
            if extra:
                toks.append(("sep", extra))
            i += n_w
            continue
        w = words[i]
        core = w.rstrip(",.;)")
        punc = w[len(core):]
        if core.startswith("(") and core not in LEX:
            toks.append(("x", "("))
            core = core[1:]
            words[i] = core + punc
            if not core:
                i += 1
                continue
        if core.endswith(")") and core not in LEX:
            pass
        # slot tokens
        if core.startswith("§T§"):
            tail = core[3:]
            toks.append(("T", slots["T"][ti[0]]))
            ti[0] += 1
            if tail in TAIL:
                my, kind = TAIL[tail]
                toks.append((kind, my))
            elif tail not in ("", "aṃ", "o", "ā", "e", "ena", "assa", "āya", "akānaṃ", "ānaṃ"):
                raise KeyError("term tail: " + tail)
            if punc:
                toks.append(("sep", punc))
            i += 1
            continue
        if core == "na" and i + 2 < len(words) and words[i + 1] == "§C§ena" and words[i + 2].rstrip(",.;") == "paccayo":
            stem, neg = slots["C"][ci[0]]
            ci[0] += 1
            toks.append(("v", iframe(stem, True)))
            p2 = words[i + 2][len("paccayo"):]  # noqa
            if p2:
                toks.append(("sep", p2))
            i += 3
            continue
        if core == "§C§ena" and i + 1 < len(words) and words[i + 1].rstrip(",.;") == "paccayo":
            stem, neg = slots["C"][ci[0]]
            ci[0] += 1
            toks.append(("v", iframe(stem)))
            p2 = words[i + 1][len("paccayo"):]
            if p2:
                toks.append(("sep", p2))
            i += 2
            continue
        if core == "§C§ā":
            stem, neg = slots["C"][ci[0]]
            ci[0] += 1
            toks.append(("x", cond(stem, "ab", neg)))
        elif core == "§V§":
            toks.append(("x", slots["V"][vi[0]]))
            vi[0] += 1
        elif core == "§D§":
            toks.append(("x", slots["D"][di[0]]))
            di[0] += 1
        elif core == "§K§":
            toks.append(("x", count_my(*slots["K"][ki[0]])))
            ki[0] += 1
        else:
            for n in range(min(8, len(words) - i), 0, -1):
                ph = words[i:i + n]
                if any(x.rstrip(",.;)") != x for x in ph[:-1]):
                    continue
                key = " ".join(ph[:-1] + [ph[-1].rstrip(",.;)")])
                if key in LEX:
                    my, kind = LEX[key]
                    toks.append((kind, my))
                    punc = ph[-1][len(ph[-1].rstrip(",.;)")):]
                    i += n - 1
                    break
            else:
                raise KeyError("lex: " + core + " in «" + text + "»")
        if punc:
            toks.append(("sep", punc))
        i += 1
    # render
    out = []
    for k, (kind, val) in enumerate(toks):
        nk = toks[k + 1][0] if k + 1 < len(toks) else None
        if kind == "T" and nk is not None:
            pass
        if kind == "sep":
            out.append(punct(val))
            continue
        if kind == "post":
            if not out:
                raise KeyError("post word first")
            pk = toks[k - 1][0] if k else None
            if pk in ("a", "na", "n") or (pk is not None and out[-1].endswith(("များ", "တို့"))):
                out[-1] = out[-1] + val
            else:                                 # «… cittena garuṃ katvā»: the object stands earlier
                out.append(" " + val[len("ကို "):] if val.startswith("ကို ") else " " + val)
            continue
        if kind == "T":
            out.append(" " + val if out and not out[-1].endswith("(") else val)
            continue
        if nk == "T" and k + 2 < len(toks) and toks[k + 2][0] == "g":
            nk = "g"
        my = _lex_item(val, kind, nk)
        out.append((" " if out and not out[-1].endswith("(") else "") + my)
    res = "".join(out)
    return lead + res.replace(" ၊", "၊").replace(" ။", "။")


# ===================================================================================== the engine
SK = {}           # whole-unit skeleton -> template (also fixed lines by their Pāli text)
SKF = {}          # fragment skeleton (text between «…») -> template
HLINES = {}       # whole heading / line Pāli text -> Burmese (chapters add)
DEV = False
UNSEEN, SLIPS, USED = {}, set(), {}


def lc(u):
    """lower-case the first letter (also after a leading «(»): sentence capitals do not change the Burmese."""
    i = 1 if u[:1] == "(" else 0
    return u[:i] + u[i:i + 1].lower() + u[i + 1:] if u[i:i + 1].isupper() else u


def try_sk(u, table):
    sk, slots = slot(lc(u))
    for key in (sk, sk.rstrip(".;,")):
        if key in table:
            out = render(table[key], slots)
            USED[key] = table[key]
            return out + (punct(sk[len(key):]) if key != sk else "")
    return None


def pairs_mr(sk, slots):
    body = sk.rstrip(".;")
    end = punct(sk[len(body):])
    for k, v in NOTES.items():
        if body.endswith(" " + k):
            body, end = body[:-len(k) - 1], " " + v + end
            break
    if not re.search(r" (?:" + "|".join(LINK) + r") ", body):
        return None
    if any(slots[k] for k in "CKVD"):
        return None
    if re.search(r" (?:" + "|".join(VERB) + r")\b", body):
        return None
    try:
        ti = [0]
        out = pairs(body, slots, ti)
    except (KeyError, StopIteration):
        return None
    if ti[0] != len(slots["T"]):
        return None
    return out + end


GH_PRE = re.compile(r"^(?P<lead>\s*)(?P<g>[\wāīūṃṅñṭḍṇḷ]+(?:-[\wāīūṃṅñṭḍṇḷ]+)+)nti (?P<rest>.+)$")


def _pure_chain(fr):
    sk, _ = slot(lc(fr))
    body = sk.strip(" .,;")
    for k in NOTES:
        body = body.replace(k, "")
    return bool(re.fullmatch(r"\s*(?:§C§ā\s*)+", body))


def frags_my(u):
    """Fragment by fragment (between «…»). When a fragment with the verb is followed only by fragments that are
    bare condition chains («… uppajjati Apaccayā… Bpaccayā… Cpaccayā»), the verb moves to the end of the last
    one (Burmese puts the verb last: «… A-ကြောင့်… B-ကြောင့်… C-ကြောင့် ဖြစ်ပေါ်သည်»)."""
    out = []
    frs = u.split(PE)
    hold_idx = None
    empty = [not f.strip(" .,;)") for f in frs]
    for i, fr in enumerate(frs):
        if re.search(r"(?<![\wāīūṃṅñṭḍṇḷ])(?:" + "|".join(VERB) + r")(?![\wāīūṃṅñṭḍṇḷ])", fr):
            later = [j for j in range(i + 1, len(frs)) if not empty[j]]
            if later and all(_pure_chain(frs[j]) for j in later):
                hold_idx = i
    HELD.clear()
    for idx, frag in enumerate(frs):
        if not frag.strip(" .,;)"):
            out.append(punct(frag))
            continue
        gm = GH_PRE.match(frag)
        if gm:
            stems, sl = segment_conds(gm["g"])
            sk, slots = slot(gm["rest"])
            ci, ki, di = [0], [0], [0]
            r = chain(sk, slots, ci, ki, di)
            out.append(f"{gm['lead']}{ghatana_list(stems)}နှင့် {r}")
            continue
        r = try_sk(frag.strip(), SKF)
        if r is not None:
            out.append(frag[:len(frag) - len(frag.lstrip())] + r + punct(frag[len(frag.rstrip()):]))
            continue
        sk, slots = slot(lc(frag))
        r = panha(sk.strip(), slots)
        if r is not None:
            out.append(frag[:len(frag) - len(frag.lstrip())] + r)
            continue
        ti, ci, ki, di = [0], [0], [0], [0]
        try:
            r = clause(sk, slots, ti, ci, ki, di, hold=(idx == hold_idx))
        except (KeyError, StopIteration):
            r = None
        if r is not None and (ti[0], ci[0], ki[0], di[0]) == tuple(len(slots[k]) for k in "TCKD") \
                and not slots["V"]:
            out.append(r)
            continue
        ti, ci, ki, di, vi = [0], [0], [0], [0], [0]
        try:
            r = lex(sk, slots, ti, ci, ki, di, vi)
        except (KeyError, IndexError) as e:
            raise Miss(f"{sk}  [{e}]")
        if (ti[0], ci[0], ki[0], di[0], vi[0]) != tuple(len(slots[k]) for k in "TCKDV"):
            raise Miss(f"{sk}  [lex left slots]")
        out.append(r)
    if HELD:
        j = max(k for k in range(len(out)) if not empty[k])
        t = out[j]
        body = t.rstrip(" ။၊")
        note = re.search(r" \([^()]*\)$", body)
        if note:                                  # the verb goes before a closing note
            body, tail = body[:note.start()], body[note.start():] + t[len(body):]
        else:
            tail = t[len(body):]
        out[j] = body + " " + HELD.pop() + tail
    return PE.join(out)


def unit_my(u):
    if not u.strip():
        return u
    lead = u[:len(u) - len(u.lstrip())]
    u = u.strip()
    out = try_sk(u, SK)
    if out is None:
        sk, slots = slot(lc(u))
        out = panha(sk, slots)
        if out is None and re.search(r"(?:nti|īti) (?:" + _CNT_ALT + r")\b", u):
            try:
                out, slips = ghatana(u)
            except KeyError as e:
                raise Miss(str(e))
            for s in slips:
                SLIPS.add(f"ghaṭanā: {s} («{u[:60]}…»)")
            if re.search(r"[A-Za-zāīūṃṅñṭḍṇḷ]{3,}", out):
                raise Miss("ghaṭanā left Pāli: " + u)
        if out is None:
            out = pairs_mr(sk, slots)
        if out is None:
            try:
                out = frags_my(u)
            except Miss as e:
                raise Miss(f"{sk}\n     frag: {e}")
    return lead + out


SPLIT = re.compile(r"( – |; |(?<=[.?])\s+(?=[^\s)])|(?<=\))\s+(?=\())")
HYPH_RE = re.compile(r"(?<![\wāīūṃṅñṭḍṇḷ])((?:[Nn][ao][\wāīūṃṅñṭḍṇḷ]+-)+)(?=[Nn][ao][\wāīūṃṅñṭḍṇḷ]+paccayā)")


def expand_hyphens(text):
    """«naārammaṇa-naadhipati-…-navippayutta-noatthipaccayā» -> separate words «naārammaṇapaccayā …» (the Pāli
    writes one compound of negated conditions; missing hyphens are source slips, logged)."""
    def f(m):
        words = []
        for part in m.group(1).strip("-").split("-"):
            p = part
            while p:
                for pre in ("na", "no"):
                    if p.lower().startswith(pre):
                        rest = p[2:]
                        st = next((x for x in sorted(STEMS, key=len, reverse=True) if rest.startswith(x)), None)
                        if st:
                            words.append(p[:2] + st + "paccayā")
                            p = rest[len(st):]
                            if p:
                                SLIPS.add(f"no hyphen before «{p}» in a negated compound")
                            break
                else:
                    raise Miss("hyphen compound: " + part)
        return " ".join(words) + " "
    return HYPH_RE.sub(f, text)


def body_my(text):
    text = expand_hyphens(pe(text))
    text = re.sub(r"\{[^{}]*\}", lambda m: m[0].replace(" ", "\u0001"), text)
    parts = [p.replace("\u0001", " ") for p in SPLIT.split(text)]
    out = []
    for p in parts:
        if SPLIT.fullmatch(p):
            out.append(" – " if p.strip() == "–" else (C + " " if p.strip() == ";" else " "))
            continue
        try:
            out.append(unit_my(p))
        except (Miss, KeyError, ValueError, StopIteration) as e:
            if DEV:
                UNSEEN.setdefault(str(e), p)
                out.append("??")
            else:
                raise Miss(f"{e}\n   in: {p}")
    res = "".join(out)
    # «; » became «၊ »: no space-less doubling
    return res.replace("။၊", "။").replace("၊၊", "၊")


def line_my(line):
    m = ID_RE.search(line)
    bid = m.group(1) if m else ""
    text = line[:m.start()] if m else line
    if text.startswith("#"):
        hashes, h = text.split(" ", 1)
        if h in HLINES:
            my = HLINES[h]
        else:
            try:
                my = heading(h)
            except KeyError:
                if DEV:
                    UNSEEN.setdefault("HEADING " + h, h)
                    my = "??"
                else:
                    raise Miss("heading: " + h)
        out = f"{hashes} {my}"
    elif text in HLINES:
        out = HLINES[text]
    else:
        out = body_my(text)
    return out + (" " + bid if bid else "")


def translate(src_text):
    """A whole chapter (Pāli) -> Burmese: one line per line, one blank line between segments."""
    global CLAUSE_RE, PANHA_RE, GHATANA_RE
    CLAUSE_RE, PANHA_RE = _clause_re(), _panha_re()
    GHATANA_RE = re.compile(r"(?P<c>[\wāīūṃṅñṭḍṇḷ][\wāīūṃṅñṭḍṇḷ -]*?)(?:nti|īti) (?P<n>" + _CNT_ALT
                            + r")(?P<end>[. ]|$)")
    out = []
    for line in src_text.splitlines():
        if not line.strip():
            if out and out[-1] != "":
                out.append("")
            continue
        out.append(line_my(line.rstrip()))
    while out and out[-1] == "":
        out.pop()
    return "\n".join(out) + "\n"
