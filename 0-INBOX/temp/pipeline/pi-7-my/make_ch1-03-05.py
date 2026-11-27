"""Burmese zero-shot of pi-7 1-03-vipakattika, 1-04-upadinnattika, 1-05-sankilitthattika («အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ»).

usage: python3 -I -X utf8 make_ch1-03-05.py [chapter ...] [--dev]
Every line goes through my7_formulas.translate() with the approved sample's tables (make_sample.py is IMPORTED for its
tables only: its main block, which writes the sample's files, never runs) and the frames of this script (triads,
nouns, lexicon, templates). my7_formulas.py is never edited: its tables are extended in memory here, and every new
string is logged in notes-ch1-03-05.md. A sentence that no frame matches stops the run; it is never guessed.
--dev lists every unmatched skeleton instead of stopping (nothing is written). Each chapter is written as soon as
it is complete.
"""
import collections
import pathlib
import re
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import my7_formulas as F  # noqa: E402
import make_sample as S  # noqa: E402,F401  (tables only; registers the sample's SK / HLINES / SPELLING)

ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-7_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters"
NAMES = ["1-03-vipakattika.md", "1-04-upadinnattika.md", "1-05-sankilitthattika.md"]
C, END, PE, W = F.C, F.END, F.PE, F.W

# ===================================================================================== the three triads (pi-1 final)
_W = r"[\wāīūṃṅñṭḍṇḷ]"
_TEENW = ["ekādasa", "dvādasa", "terasa", "cuddasa", "pannarasa", "soḷasa", "sattarasa", "aṭṭhārasa", "ekūnavīsati",
          "vīsati", "ekavīsati", "dvāvīsati", "bāvīsati", "tevīsati", "tevīsa", "catuvīsati"]
_NUMS = "|".join(sorted(list(F.COUNT) + _TEENW, key=len, reverse=True))
_END = (r"(?:aṃ|o|ā|ānaṃ|añca|assa|e(?! (?:" + _NUMS + r")(?!" + _W + r")(?! khandh))|āni|āya|ādhipati"
        r"|acittasamaṅgissa)(?!" + _W + r")")


def _tw(pali, my, bid):
    """a pi-1 Mātikā term, read from the FINAL rails (attributive form, without « သဘောတရားများ»)"""
    return W(pali, my + " ", "1", bid)[:-1]


TRIADS_ADD = {
    "vipaka": {
        "vipāk": _tw("vipākā dhammā", "ကံ၏ အကျိုး ဖြစ်သော", "^1-M1-3"),
        "vipākadhammadhamm": _tw("vipākadhammadhammā", "အကျိုး ပေးတတ်သော", "^1-M1-3"),
        "nevavipākanavipākadhammadhamm": _tw("nevavipākanavipākadhammadhammā",
                                             "ကံ၏ အကျိုးလည်း မဟုတ်၊ အကျိုး ပေးတတ်သည်လည်း မဟုတ်သော", "^1-M1-3"),
    },
    "upadinna": {
        "upādinnupādāniy": _tw("upādiṇṇupādāniyā", "ကံကြောင့် ဖြစ်၍ စွဲလမ်းမှု၏ အာရုံလည်း ဖြစ်နိုင်သော", "^1-M1-4"),
        "anupādinnupādāniy": _tw("anupādiṇṇupādāniyā", "ကံကြောင့် မဖြစ်သော်လည်း စွဲလမ်းမှု၏ အာရုံ ဖြစ်နိုင်သော",
                                 "^1-M1-4"),
        "anupādinnaanupādāniy": _tw("anupādiṇṇaanupādāniyā",
                                    "ကံကြောင့်လည်း မဖြစ်၊ စွဲလမ်းမှု၏ အာရုံလည်း မဖြစ်နိုင်သော", "^1-M1-4"),
    },
    "sankilittha": {
        "saṃkiliṭṭhasaṃkilesik": _tw("saṃkiliṭṭhasaṃkilesikā",
                                     "ကိလေသာဖြင့် ညစ်နွမ်း၍ ကိလေသာ၏ အာရုံလည်း ဖြစ်နိုင်သော", "^1-M1-5"),
        "asaṃkiliṭṭhasaṃkilesik": _tw("asaṃkiliṭṭhasaṃkilesikā",
                                      "ကိလေသာဖြင့် မညစ်နွမ်းသော်လည်း ကိလေသာ၏ အာရုံ ဖြစ်နိုင်သော", "^1-M1-5"),
        "asaṃkiliṭṭhaasaṃkilesik": _tw("asaṃkiliṭṭhaasaṃkilesikā",
                                       "ကိလေသာဖြင့်လည်း မညစ်နွမ်း၊ ကိလေသာ၏ အာရုံလည်း မဖြစ်နိုင်သော", "^1-M1-5"),
    },
}
TRIADS_ADD["sankilittha"]["asaṅkiliṭṭhasaṃkilisik"] = TRIADS_ADD["sankilittha"]["asaṃkiliṭṭhasaṃkilesik"]  # slip
# the stand-alone forms split by prep() («vipākadhamma dhammo»): the same Burmese, the noun follows
TRIADS_ADD["vipaka"]["vipākadhamma"] = TRIADS_ADD["vipaka"]["vipākadhammadhamm"]
TRIADS_ADD["vipaka"]["nevavipākanavipākadhamma"] = TRIADS_ADD["vipaka"]["nevavipākanavipākadhammadhamm"]
TRIAD_END_ADD = {"vipaka": r"(?<!kammaṃ vipāk)(?:" + _END + r"|(?<=dhamma)(?= dhamm))", "upadinna": _END,
                 "sankilittha": _END}
F.TRIADS.update(TRIADS_ADD)
F.TRIAD_END.update(TRIAD_END_ADD)
F.rebuild()

# ===================================================================================== Pāli preparation (in memory)
# 1. «vipākadhammadhammo» = vipākadhamma + dhammo: when the term stands alone (no noun follows), the noun «dhamma» is
#    part of the word; it is split off so that the frames see «§T§ dhammo» (pi-1: «အကျိုး ပေးတတ်သော သဘောတရားများ»).
# 2. «khandhañca vatthuñca» = «khandhaṃ ca vatthuṃ ca» (the enclitic written apart, so that the coordination rules of
#    the module apply: «A ca B ca» / «X Y ca Z»); terms are not touched (the module's term coordination).
# 3. source slips written apart / together (logged in SLIPS).
_DD = r"(?<![\wāīūṃṅñṭḍṇḷ])([Vv]ipākadhamma|[Nn]evavipākanavipākadhamma)dhamm(o|aṃ|assa|ā|ānaṃ|e)(?![\wāīūṃṅñṭḍṇḷ])"
_KEEP_NEXT = ("eko", "ekaṃ", "ekassa", "dve", "tayo", "tiṇṇannaṃ", "khandh", "dhamm", "ca", "cetanā", "hetū",
              "āhārā", "indriyā", "jhānaṅg", "maggaṅg", "mahābhūt", "sampayuttak")
NCA = {"vatthuñca", "cittasamuṭṭhānānañca", "cittasamuṭṭhānañca", "khandhañca", "cakkhāyatanañca",
       "rūpajīvitindriyañca", "rūpāyatanañca", "phoṭṭhabbāyatanañca", "kāyāyatanañca", "cakkhundriyañca",
       "cakkhuviññāṇañca", "kāyindriyañca", "kāyaviññāṇañca"}
SLIP_FIX = {"nevavipākanavipākadhamma-dhammo": "nevavipākanavipākadhammadhammo",
            "sappayuttakānaṃ": "sampayuttakānaṃ", "paṭisandhikhaṇe": "paṭisandhikkhaṇe", "tayokhandhā": "tayo khandhā",
            "pakatūnissayo": "pakatūpanissayo", "vippassanti": "vipassanti", "vitthāratabbaṃ": "vitthāretabbaṃ"}
_TERMW = (r"(?:[Vv]ipāk|[Nn]evavipākanavipākadhammadhamm|[Vv]ipākadhammadhamm|(?:[Aa]n)?[Uu]pādinn(?:aanu|u)pādāniy"
          r"|(?:[Aa]s|[Ss])aṃkiliṭṭha(?:a?saṃ)kilesik)")


TOK = "\u0003"


def prep(text):
    for a, b in SLIP_FIX.items():
        if a in text:
            F.SLIPS.add(f"«{a}» read as «{b}»")
            text = text.replace(a, b)

    def dd(m):
        nxt = text[m.end():m.end() + 40].lstrip(" ,.;").replace("…pe…", "").lstrip()
        if nxt.startswith(_KEEP_NEXT):
            return m[0]
        return f"{m[1]} dhamm{m[2]}"
    text = re.sub(_DD, dd, text)
    text = re.sub(r"(?<![\wāīūṃṅñṭḍṇḷ])(\S+)ñca(?![\wāīūṃṅñṭḍṇḷ])",
                  lambda m: f"{m[1]}ṃ ca" if m[0] in NCA else m[0], text)
    # «X-assa ca Y-assa ca» (two terms, the noun left out) = «… dhammassa» (the noun of the frame supplied)
    text = re.sub(r"(?<![\wāīūṃṅñṭḍṇḷ])(" + _TERMW + r"(assa|o|aṃ) ca " + _TERMW + r"(?:assa|o|aṃ) ca)"
                  r"(?= [a-zāīūṃṅñṭḍṇḷ]*paccayena|…)", lambda m: f"{m[1]} dhamm{m[2]}", text)
    # «na adhipatiyā tīṇi» / «na adhipatipaccayā» written apart (source slip) = «naadhipatiyā …»
    def na_apart(m):
        F.SLIPS.add(f"«{m[0]}» written apart, read as «na{m[1]}»")
        return "na" + m[1]
    text = re.sub(r"(?<![\wāīūṃṅñṭḍṇḷ])na ((?:" + F._LOC_ALT + r") (?:" + F._CNT_ALT + r")(?![\wāīūṃṅñṭḍṇḷ]))",
                  na_apart, text)
    text = re.sub(r"(?<![\wāīūṃṅñṭḍṇḷ])na ([a-zāīū]+paccayā)(?![\wāīūṃṅñṭḍṇḷ])", na_apart, text)
    # «tayo khandhā vatthu ca» (one «ca» after the last member) = «tayo khandhā ca vatthu ca»
    text = re.sub(r"(?<= khandhā) (?=vatthu ca(?![\wāīūṃṅñṭḍṇḷ]))", " ca ", text)
    text = re.sub(r"(?<= khandhānaṃ) (?=vatthussa ca(?![\wāīūṃṅñṭḍṇḷ]))", " ca ", text)
    # «vipākādhipati» = «vipāko adhipati» (the term qualifies the noun adhipati: «ကံ၏ အကျိုး ဖြစ်သော အကြီးအမှူး»)
    text = re.sub(r"(?<![\wāīūṃṅñṭḍṇḷ])(" + _TERMW + r")ādhipati(?![\wāīūṃṅñṭḍṇḷ])", r"\1o adhipati", text)
    # one NP token (words joined by U+0003) for «[purejātassa] imassa [terms] kāyassa» and «[terms] kabaḷīkāro
    # āhāro»: the terms qualify the body / the food (rendered by np_my below)
    _tw = r"(?:" + _TERMW + r"[a-zāīūṃ]*(?: ca)? )"
    text = re.sub(r"(?<![\wāīūṃṅñṭḍṇḷ])((?:purejātassa )?(?:imassa )?" + _tw + r"+kāyassa)",
                  lambda m: m[1].replace(" ", TOK), text)
    text = re.sub(r"(?<![\wāīūṃṅñṭḍṇḷ])(" + _tw + r"+kabaḷīkāro āhāro)", lambda m: m[1].replace(" ", TOK), text)
    # the label «Sahajātā –» outside the kamma section (no «cetanā» follows) names the kind of condition
    text = re.sub(r"(?<![\wāīūṃṅñṭḍṇḷ])Sahajātā(?= – (?:(?!cetanā)[^.])*\.)", "SahajātāKIND", text)
    return text


# ===================================================================================== numbers above ten
# pi-1 / pi-2 / pi-3: «ဆယ့်နှစ်ပါး», «ဆယ့်တစ်ပါး», «ဆယ့်ခုနစ်ပါး», «ဆယ့်ခြောက်ပါး», «ဆယ့်ငါးပါး», «ဆယ့်လေးပါး», «နှစ်ဆယ်»
TEEN = {"ekādasa": (11, W("ekādasa cittuppādā", "ဆယ့်တစ်", "1")), "dvādasa": (12, W("Dvādasa akusalacittāni", "ဆယ့်နှစ်", "1")),
        "terasa": (13, "ဆယ့်သုံး"), "cuddasa": (14, W("Cuddasa", "ဆယ့်လေး", "3")),
        "pannarasa": (15, W("Pannarasa dhātuyo", "ဆယ့်ငါး", "2")), "soḷasa": (16, W("Soḷasa dhātuyo", "ဆယ့်ခြောက်", "2")),
        "sattarasa": (17, W("Sattarasa dhātuyo", "ဆယ့်ခုနစ်", "2")), "aṭṭhārasa": (18, "ဆယ့်ရှစ်"),
        "ekūnavīsati": (19, "ဆယ့်ကိုး"), "vīsati": (20, W("Vīsati mahānayā", "နှစ်ဆယ်", "1")),
        "ekavīsati": (21, "နှစ်ဆယ့်တစ်"), "dvāvīsati": (22, "နှစ်ဆယ့်နှစ်"), "bāvīsati": (22, "နှစ်ဆယ့်နှစ်"),
        "tevīsati": (23, "နှစ်ဆယ့်သုံး"), "tevīsa": (23, "နှစ်ဆယ့်သုံး"),
        "catuvīsati": (24, "နှစ်ဆယ့်လေး")}
for _w, (_n, _my) in TEEN.items():
    F.COUNT[_w] = _my + "ခု"
    F.COUNT_VAL[_w] = _n
F._CNT_ALT = "|".join(sorted(F.COUNT, key=len, reverse=True))
F.COUNT_RE = re.compile(r"(?<![\wāīūṃṅñṭḍṇḷ])(?P<neg>[Nn]a|[Nn]o)?(?P<loc>(?i:" + F._LOC_ALT + r")) (?P<num>"
                        + F._CNT_ALT + r")(?![\wāīūṃṅñṭḍṇḷ])")


# ===================================================================================== engine extensions (in memory)
# (a) an asyndetic list of fixed noun phrases of several words («cittasamuṭṭhānaṃ rūpaṃ kaṭattārūpaṃ upādārūpaṃ»)
_np_parse0 = F.np_parse


def _fixed_split(words):
    if not words:
        return []
    for n in range(len(words), 0, -1):
        k = " ".join(words[:n])
        if k in F.FIXED:
            rest = _fixed_split(words[n:])
            if rest is not None:
                return [k] + rest
    return None


def np_parse(words, terms):
    if len(words) == 1 and TOK in words[0]:
        my, case, nt, odd = _tok_my(words[0], terms)
        return my, case, False, nt
    if len(words) == 1 and words[0].startswith("§T§") and words[0][3:] in TERM_CASE:
        # a term standing for «term + dhamma» («X-añca Y-añca dhammaṃ paṭicca Z-o…pe…»): the noun supplied (logged)
        case, pl = TERM_CASE[words[0][3:]]
        return f"{next(terms)} {F.DHAMMA}", case, pl, 1
    w2 = [w.replace("\u0002", " ") for w in words]
    if len(w2) > 1 and " ".join(w2) not in F.FIXED and not any(w.startswith("§T§") for w in w2):
        seg = _fixed_split(" ".join(w2).split())
        if seg and len(seg) > 1:
            return (C + " ").join(F.FIXED[k][0] for k in seg), F.FIXED[seg[-1]][1], True, 0
    return _np_parse0(words, terms)


F.np_parse = np_parse

# (a2) the joined tokens of prep(): «[purejātassa] imassa [T…] kāyassa» (g), «[T…] kabaḷīkāro āhāro» (n)
KAYA = F.FIXED["imassa kāyassa"][0]                       # «ဤကိုယ်»
PUREJATA_Q = F.FIXED["purejātassa imassa kāyassa"][0][:-len(" " + KAYA)]
KABALI = F.FIXED["kabaḷīkāro §V§ āhāro"][0]
F.add_fixed(KABALI, "n", False, "kabaḷīkāro āhāro")


def _tok_my(tok, terms):
    """Burmese of a joined token (without case); returns (Burmese, case, n_terms, odd_ca)"""
    ws = tok.split(TOK)
    vals, nt, n_ca = [], 0, ws.count("ca")
    for w in ws:
        if w.startswith("§T§"):
            vals.append(next(terms))
            nt += 1
    tq = (C + " ").join(vals)
    if ws[-1] == "kāyassa":
        pre = PUREJATA_Q + " " if ws[0] == "purejātassa" else ""
        return pre + (tq + " " if tq else "") + KAYA, "g", nt, (n_ca == 1)
    return (tq + " " if tq else "") + KABALI, "n", nt, False


_np_my0 = F.np_my


def np_my(words, terms, role):
    pre = words[:-1]
    if (len(pre) > 1 and all(w.startswith("§T§") for w in pre)
            and not any(w.endswith(("ñca", "ca")) for w in pre)):
        # terms of two triads stacked on one noun («vipākānaṃ sukhāya vedanāya sampayuttānaṃ khandhānaṃ»): both
        # qualify the noun (no «ca»), so no «…နှင့်» coordination (the sample's QUAL rendering)
        ph, _, pl, nt = F.np_parse(list(words), terms)
        num = re.search(r" (?:" + "|".join(F.PAA.values()) + r")$", ph)
        return ph + F._mark(pl, num, role), pl, nt
    if not words or TOK not in words[-1]:
        return _np_my0(words, terms, role)
    terms = iter(terms)
    lead = words[:-1]
    if not lead:
        my, case, nt, odd = _tok_my(words[-1], terms)
        return my + F.CASE[role], False, nt
    if "ca" in lead:                      # «A ca [token] ca»: the module's coordination (the token is one word)
        return _np_my0(words, terms, role)
    a_my, _, k1 = _np_my0(lead, terms, role)
    b_my, case, k2, odd = _tok_my(words[-1], terms)
    if odd:                               # «tiṇṇannaṃ khandhānaṃ purejātassa imassa X ca kāyassa»
        F.SLIPS.add("«… khandhānaṃ purejātassa imassa X ca kāyassa»: the «ca» read as joining the khandhas and "
                    "the body")
        return f"{a_my}{F.LAKAUNG}{C} {b_my}{F.CASE[role]}{F.LAKAUNG}", True, k1 + k2
    return f"{a_my}{C} {b_my}{F.CASE[role]}", True, k1 + k2


F.np_my = np_my
_case_of0 = F._case_of


TERM_CASE = {"o": ("n", False), "ā": ("n", True), "aṃ": ("a", False), "assa": ("g", False), "ānaṃ": ("g", True),
             "e": ("a", True)}


def _case_of(words):
    while len(words) > 1 and words[-1] == "ca":          # «A ca B ca»: the last member's case
        words = words[:-1]
    if words and TOK in words[-1]:
        return "g" if words[-1].endswith("kāyassa") else "n"
    if len(words) == 1 and words[0].startswith("§T§") and words[0][3:] in TERM_CASE:
        return TERM_CASE[words[0][3:]][0]
    return _case_of0(words)


F._case_of = _case_of

# (a3) a coordinated first member of a pair: the case of the link inside each member, as pi-2 ^2-184 «Cakkhuñca
#      paṭicca rūpe ca …» = «…ကိုလည်းကောင်း၊ …ကိုလည်းကောင်း မှီ၍» («khandhe ca mahābhūte ca paṭicca …»)
LINK_IN = {"paṭicca": ("ကို", " မှီ၍"), "nissāya": ("ကို", " မှီ၍"), "paccayā": (F.KYAUNG, "")}


def _coord_link(words, terms, link):
    txt = " ".join(words)
    for k in F.FIXED:
        if " ca " in k and k in txt:
            txt = txt.replace(k, k.replace(" ", "\u0002"))
    parts = F._conj(txt.split())
    if not parts or link not in LINK_IN:
        return None, 0
    case, tail = LINK_IN[link]
    out, nt = [], 0
    for p in parts:
        ph, _, pl, k = F.np_parse(p, terms)
        nt += k
        num = re.search(r" (?:" + "|".join(F.PAA.values()) + r")$", ph)
        out.append(ph + ("တို့" if pl and not num else "") + case + F.LAKAUNG)
    return (C + " ").join(out) + tail, nt


def pairs(s, slots, ti):
    out = []
    for part in s.split(", "):
        pm = re.match(r"^(?P<pre>(?:" + "|".join(map(re.escape, F.PREFIX)) + r") )?(?P<a>.+?) (?P<link>"
                      + "|".join(F.LINK) + r") (?P<b>.+)$", part)
        if not pm:
            raise KeyError("pair: " + part)
        terms = iter(slots["T"][ti[0]:])
        aw, bw = pm["a"].split(), pm["b"].split()
        a_lk, k1 = _coord_link(aw, terms, pm["link"]) if "ca" in aw else (None, 0)
        if a_lk is None:
            a_my, _, k1 = F.np_my(aw, terms, "")
            a_my = re.sub(r"များ$", "တို့", a_my)
            a_lk = F.LINK[pm["link"]](a_my)
        b_my, _, k2 = F.np_my(bw, terms, "")
        ti[0] += k1 + k2
        pre = F.PREFIX[pm["pre"].strip()] + " " if pm["pre"] else ""
        out.append(pre + a_lk + " " + b_my)
    return (C + " ").join(out)


F.pairs = pairs

# (b) verbless pairs inside a «…» fragment («X ekaṃ khandhaṃ paṭicca tayo khandhā…pe… dve khandhe paṭicca dve khandhā»)
_panha0 = F.panha


def panha(sk, slots):
    r = _panha0(sk, slots)
    if r is None and not any(slots[k] for k in "CKVD"):
        r = F.pairs_mr(sk, slots)
    return r


F.panha = panha

# ===================================================================================== tables of this script
HLINES = {}
SK = {}
SKF = {}
NEW = collections.OrderedDict()     # every new string of this script: Pāli -> Burmese (listed by --new)


def new(pali, my):
    """a NEW string of this script (logged in the notes), returned unchanged"""
    NEW.setdefault(pali, my)
    return my


# --- nouns, qualifiers, fixed phrases (paṭiccavāra … sampayuttavāra) -------------------------------------------------
MAHABHUTA = F.NOUN["mahābhūtā"][0]
F.add_noun(F.VATTHU, n=["vatthu"], g=["vatthussa"])
F.add_noun(MAHABHUTA, a=["mahābhūtaṃ"], ap=["mahābhūte"], gp=["mahābhūtānaṃ"])
CITTASAM = F.QUAL["cittasamuṭṭhānānaṃ"]
F.add_qual(CITTASAM, "cittasamuṭṭhānaṃ")
F.add_qual(F.AHETUKA, "ahetuke", "ahetukā")
F.add_qual(new("pañcaviññāṇasahagataṃ", "သိစိတ် ငါးပါးနှင့်အတူ ဖြစ်သော"), "pañcaviññāṇasahagataṃ")
_VIN = {"cakkhu": "မျက်စိ", "sota": "နား", "ghāna": "နှာခေါင်း", "jivhā": "လျှာ", "kāya": "ကိုယ်"}
for _p, _my in _VIN.items():
    _v = f"{_my} သိစိတ်"
    F.add_fixed(_v, "n", False, f"{_p}viññāṇaṃ")
    F.add_fixed(_v, "g", False, f"{_p}viññāṇassa")
    F.add_qual(_v + F.SAHAGATA, f"{_p}viññāṇasahagataṃ", f"{_p}viññāṇasahagato", f"{_p}viññāṇasahagatānaṃ")
    SKF[_p] = _my                                           # «sota… ghāna… jivhā… kāya…» (elliptic list)
W("kāyaviññāṇaṃ", "ကိုယ် သိစိတ်", "1")
F.add_fixed(f"{CITTASAM} {F.NOUN['rūpaṃ'][0]}", "n", False, "cittasamuṭṭhānaṃ rūpaṃ")
F.add_fixed(F.KATATTARUPA, "n", False, "kaṭattārūpaṃ", "kaṭattā ca rūpaṃ")
UPADARUPA = F.FIXED["upādārūpānaṃ"][0]
F.add_fixed(UPADARUPA, "n", False, "upādārūpaṃ")
F.LINK["sahajātā"] = F.LINK["sahajāto"]
F.LINK["saṃsaṭṭhā"] = F.LINK["saṃsaṭṭho"]
# harmonise H3: asaññasattānaṃ (… mahābhūtaṃ, possessive genitive) «အသညသတ်တို့၏» as 1-01 (one form in the book)
ASANNA = W("asaññasattānaṃ", "အသညသတ်တို့", "6") + "၏"
F.PREFIX["asaññasattānaṃ"] = ASANNA
F.LEX["asaññasattānaṃ"] = (ASANNA, "x")
SKF["asaññasattānaṃ"] = ASANNA
BAHIRA = W("rūpaṃ bāhiraṃ", "ပြင်ပ", "1")
SKF["bāhiraṃ"] = BAHIRA
SKF["āhārasamuṭṭhānaṃ"] = new("āhārasamuṭṭhānaṃ", "အာဟာရမှ ဖြစ်ပေါ်လာသော")
SKF["utusamuṭṭhānaṃ"] = new("utusamuṭṭhānaṃ", "ရာသီဥတုမှ ဖြစ်ပေါ်လာသော")     # utu «ရာသီဥတု» (sample)
SKF["ekaṃ mahābhūtaṃ"] = f"{MAHABHUTA} {F.PAA[1]}"
for _p in ("bāhiraṃ", "āhārasamuṭṭhānaṃ", "utusamuṭṭhānaṃ"):        # «utusamuṭṭhānaṃ ekaṃ mahābhūtaṃ paṭicca …»
    F.add_qual(SKF[_p], _p)
UBHAYA = new("ubhayañca (after X ca)", "နှစ်မျိုးလုံး")
SKF["§T§o ca ubhayañca"] = f"{{T1}} {F.DHAMMA}{F.LAKAUNG}{C} {UBHAYA}{F.LAKAUNG}"
SKF["§T§añca §T§añca"] = f"{{T1}} {F.DHAMMA}နှင့် {{T2}} {F.DHAMMA}"
for _w in F.COUNT:                                          # a bare count after «…»: «…pe… tīṇi.» = «… သုံးခု။»
    SKF[_w] = F.COUNT[_w]

# --- notes -----------------------------------------------------------------------------------------------------------
for _st in F.STEMS:
    F.NOTES[f"({_st}sadisaṃ)"] = f"({F.N[_st]}{F.SADISA})"                       # sample «(anantarasadisaṃ)»
    F.NOTES[f"({_st}paccayasadisaṃ)"] = f"({F.cname(_st)}{F.SADISA})"            # sample «(anantarapaccayasadisaṃ)»
    F.NOTES[f"({F.NEG_PREFIX[_st]}{_st}paccayasadisaṃ)"] = f"({F.cond(_st, 'n', True)}{F.SADISA})"
NANAKARANA = new("nānākaraṇaṃ", "ကွဲပြားချက်")
NANATTA = new("nānattaṃ", "ကွဲပြားခြင်း")
IDAM = "ဤသည်မှာ"
F.NOTES.update({
    "(sahajātaṃ sabbaṃ hetupaccayasadisaṃ)": f"({F.cname('sahajāta')}၌ အားလုံး {F.cname('hetu')}{F.SADISA})",
    "(sahajāte idaṃ nānākaraṇaṃ)": f"({F.cname('sahajāta')}၌ {IDAM} {NANAKARANA} ဖြစ်သည်)",
    "(idaṃ nānattaṃ)": f"({IDAM} {NANATTA} ဖြစ်သည်)",
    "(adhipatiyā paṭisandhikkhaṇe natthi)": f"({F.cname('adhipati')}၌ {F.PATISANDHI} နေသော ခဏ မရှိ)",
    "(hetupaccayasadisā nava)": f"({F.cname('hetu')}{F.SADISA}များ {F.COUNT['nava']})",
    "(vitthārena gaṇetabbaṃ)": "(" + new("vitthārena", "အကျယ်အားဖြင့်") + " " + S.PH["gaṇetabbaṃ"] + ")",
    "(paṭisandhi paripuṇṇaṃ)": f"({F.PATISANDHI} {F.W('paripuṇṇaṃ', 'ပြည့်စုံ')}သည်)",
})
PANHA = new("pañhā", "ပြဿနာ")                       # pañhā (count of questions; sample heading pañhāvāra «ပြဿနာ»)
for _w in ("ekā", "satta", "terasa"):
    _c = F.COUNT["ekaṃ" if _w == "ekā" else _w]
    F.NOTES[f"({_w} pañhā)"] = f"({PANHA} {_c})"

# --- headings and whole lines ---------------------------------------------------------------------------------------
F.TIKA_NAME["Vipākattikaṃ"] = W("Vipākattikaṃ", "ကံ၏ အကျိုး သုံးမျိုးတွဲ", "2")
F.TIKA_NAME["Upādinnattikaṃ"] = W("Upādinnattikaṃ", "ကံကြောင့် ဖြစ်ခြင်း သုံးမျိုးတွဲ", "2")
F.TIKA_NAME["Saṃkiliṭṭhattikaṃ"] = new("Saṃkiliṭṭhattikaṃ", "ကိလေသာဖြင့် ညစ်နွမ်းခြင်း သုံးမျိုးတွဲ")
for _p in ("Vipākattikaṃ", "Upādinnattikaṃ", "Saṃkiliṭṭhattikaṃ"):
    HLINES[f"{_p} niṭṭhitaṃ."] = F.finished(F.TIKA_NAME[_p])
for _w, (_n, _my) in TEEN.items():
    if _w.endswith("a"):
        F.GROUP[_w + "ka"] = _my + "မျိုးတွဲ"            # «Ekādasakaṃ» = «ဆယ့်တစ်မျိုးတွဲ»
F.GROUP["ekādasaka"] = TEEN["ekādasa"][1] + "မျိုးတွဲ"
for _v in ("Sahajātavāro", "Paccayavāro", "Nissayavāro", "Saṃsaṭṭhavāro", "Sampayuttavāro", "Paṭiccavāro"):
    HLINES[_v + "."] = F.HEAD[_v] + END
HLINES["Anulomagaṇanā."] = "အဟုတ်ပြ ပုံစံ၏ ရေတွက်ချက်" + END
# harmonise H1: «Anulomaṃ.» closing the positive order = «အဟုတ်ပြ ပုံစံ။» (1-01, 2-07 … 2-11); the mind moment
# «anulomaṃ» inside a sentence keeps the LEX noun «လျော်ညီခြင်း စိတ်»
HLINES["Anulomaṃ."] = "အဟုတ်ပြ ပုံစံ" + END
HLINES["*1-4. Paccayacatukkaṃ*"] = f"*1-4. {F.PACCAYA} {F.GROUP['catukka']}*"
HLINES["*Natthi-vigatāvigatapaccayā*"] = (f"*{F.cname('natthi')}{C} {F.cname('vigata')}နှင့် "
                                          f"{F.cname('avigata')}*")
HLINES["*Sabhāgaṃ*"] = "*" + new("Sabhāgaṃ", "တွဲဖက်သည်များ") + "*"
HLINES["*Anulomaṃ*"] = "*" + F.WITNESS.get("anulomaṃ (the positive method; heading)", (0, 0, "အဟုတ်ပြ ပုံစံ"))[2] + "*"

# --- the pañhāvāra lexicon (LEX kinds: n na a g G i b x v post; «+» = plural) --------------------------------------
SEKKHA = W("sekkhā", "ကျင့်ကြံဆဲသူ", "4")
PUTHU = W("puthujjanā", "ပုထုဇဉ်", "6")
ARAHA = W("arahā", "ရဟန္တာ", "5")
KAYIKA_S = W("kāyikaṃ sukhaṃ", "ကိုယ်ပိုင်းဆိုင်ရာ သာယာမှု", "1")
KAYIKA_D = W("kāyikaṃ dukkhaṃ", "ကိုယ်ပိုင်းဆိုင်ရာ နာကျင်မှု", "1")
SAMAPATTI = F.WITNESS["samāpatti"][2] if "samāpatti" in F.WITNESS else W("samāpatti", "သမာပတ်", "5")
KIRIYA = F.QUAL["kiriyābyākatā"][:-len(" " + F.ABY)]                  # «ပြုရုံမျှသာ ဖြစ်သော»
ANUPPANNA = W("anuppannā", "မဖြစ်ပေါ်သေးသော", "1")
UPPANNA = W("uppannā", "ဖြစ်ပေါ်ပြီးသော", "1")
PARIKAMMA = new("parikammaṃ", "ကြိုတင် ပြင်ဆင်မှု")
ORD = {"paṭham": "ပထမ", "dutiy": "ဒုတိယ", "tatiy": "တတိယ", "catutth": "စတုတ္ထ"}
NIBBANA = W("nibbānaṃ", "နိဗ္ဗာန်", "2")
AY = {"ākāsānañcāyatana": F.LEX["ākāsānañcāyatanaṃ"][0], "viññāṇañcāyatana": F.LEX["viññāṇañcāyatanassa"][0],
      "ākiñcaññāyatana": F.LEX["ākiñcaññāyatanaṃ"][0], "nevasaññānāsaññāyatana": F.LEX["nevasaññānāsaññāyatanaṃ"][0]}
SAMB = {"attha": W("atthapaṭisambhidā", "အကျိုးအနက်ကို ပိုင်းခြားသိသော ဉာဏ်", "2"),
        "dhamma": W("dhammapaṭisambhidā", "တရားကို ပိုင်းခြားသိသော ဉာဏ်", "2"),
        "nirutti": W("niruttipaṭisambhidā", "စကားဖြင့် ဖော်ပြမှုကို ပိုင်းခြားသိသော ဉာဏ်", "2"),
        "paṭibhāna": W("paṭibhānapaṭisambhidā", "ဉာဏ်ပေါ်မှုကို ပိုင်းခြားသိသော ဉာဏ်", "2")}
THANA = W("ṭhānāṭhānaṃ", "ဖြစ်နိုင်သော အကြောင်းနှင့် မဖြစ်နိုင်သော အကြောင်း", "5")
KOSALLA = new("ṭhānāṭhānakosalla", THANA + "၌ ကျွမ်းကျင်မှု")
DEEDS = {"pāṇātipāt": W("pāṇātipātakammassa", "သူ့အသက်ကို သတ်ခြင်း", "5"),
         "micchādiṭṭhi": W("micchādiṭṭhi", "မှားယွင်းသော အယူ", "1"),
         "mātughātikamm": W("mātughātakammassa", "အမိကို သတ်ခြင်း ကံ", "5"),
         "niyatamicchādiṭṭhi": W("niyatā", "ကျိန်းသေသော", "1") + " မှားယွင်းသော အယူ",
         "saṅghabhedakakamm": W("saṅghabhedakammassa", "သံဃာကို သင်းခွဲခြင်း ကံ", "5")}
F.add_lex("n", {"sekkhā": SEKKHA + "+", "arahā": ARAHA, "puthujjanā": PUTHU + "+", "mahābhūtā": MAHABHUTA + "+",
                "phalasamāpatti": F.LEX["phalasamāpattiyā"][0], "utu": "ရာသီဥတု",
                "pāṇātipāto": DEEDS["pāṇātipāt"], "micchādiṭṭhi": DEEDS["micchādiṭṭhi"],
                "mātughātikammaṃ": DEEDS["mātughātikamm"], "niyatamicchādiṭṭhi": DEEDS["niyatamicchādiṭṭhi"],
                "dhammo": F.DHAMMA, "dhammā": F.DHAMMA + "+", "kusalākusalaṃ kammaṃ": F.FIXED["kusalākusalaṃ kammaṃ"][0],
                "kammaṃ": "ကံ", "āhārā": "အာဟာရ+", "indriyā": "စွမ်းရည်+", "jhānaṅgā": "ဈာန်၏ အင်္ဂါ+",
                "maggaṅgā": F.FIXED["maggaṅgāni"][0] + "+",
                "pañcaviññāṇaṃ": "သိစိတ် " + F.PAA.get(5, "ငါးပါး"), "bhavaṅgaṃ": "ဘဝင် စိတ်",
                "vipākamanodhātu": F.LEX["vipākamanodhātu"][0],
                "vipākamanoviññāṇadhātu": F.LEX["vipākamanoviññāṇadhātu"][0]})
for _o, _my in ORD.items():
    F.add_lex("n", {f"{_o}o maggo": f"{_my} မဂ်", f"{_o}aṃ jhānaṃ": f"{_my} ဈာန်",
                    f"{_o}assa jhānassa parikammaṃ": f"{_my} ဈာန်၏ {PARIKAMMA}",
                    f"{_o}assa maggassa parikammaṃ": f"{_my} မဂ်၏ {PARIKAMMA}"})
    F.add_lex("g", {f"{_o}assa jhānassa": f"{_my} ဈာန်", f"{_o}assa maggassa": f"{_my} မဂ်"})
    F.add_lex("x", {f"{_o}assa": _my})                                  # «… paṭhamassa…pe…» (elliptic)
F.add_lex("n", {"nevasaññānāsaññāyatanassa parikammaṃ": f"{AY['nevasaññānāsaññāyatana']}၏ {PARIKAMMA}"})
for _k, _my in AY.items():
    # harmonise (align): the formless-base minds as 1-01 «<base> ကုသိုလ်», «<base> ပြုရုံမျှသာ ဖြစ်သော စိတ်»,
    # «<base> ကံ၏ အကျိုး» (was «<base>နှင့် ဆိုင်သော …»)
    F.add_lex("n", {f"{_k}kusalaṃ": f"{_my} ကုသိုလ်",
                    f"{_k}kiriyaṃ": f"{_my} {KIRIYA} စိတ်"})
    F.add_lex("g", {f"{_k}kusalassa": f"{_my} ကုသိုလ်",
                    f"{_k}kiriyassa": f"{_my} {KIRIYA} စိတ်",
                    f"{_k}vipākassa": f"{_my} {F.N['vipāka']}"})
F.add_lex("na", {"nibbānaṃ": NIBBANA, "kāyikaṃ sukhaṃ": KAYIKA_S, "kāyikaṃ dukkhaṃ": KAYIKA_D,
                 "bhojanaṃ": F.NOUN["utubhojanam"][0].split("နှင့် ")[1], "senāsanaṃ": F.NOUN["senāsanam"][0]})
F.add_lex("a", {"cakkhuṃ": "မျက်စိ", "sotaṃ": "နား", "ghānaṃ": "နှာခေါင်း", "jivhaṃ": "လျှာ", "kāyaṃ": "ကိုယ်",
                "rūpe": "အဆင်းအရောင်+", "sadde": "အသံ+", "gandhe": "အနံ့+", "rase": "အရသာ+",
                "phoṭṭhabbe": "အထိအတွေ့+", "saṅkhāre": W("saṅkhārā", "ပြုပြင်ဖန်တီးမှု", "1") + "+",
                "maggaṃ": "မဂ်", "jhānaṃ": "ဈာန်", "gotrabhuṃ": "အနွယ် ပြောင်းခြင်း စိတ်", "utuṃ": "ရာသီဥတု",
                "pubbe suciṇṇāni": F.LEX["pubbe samudāciṇṇe kilese"][0].split("က ")[0] + "က "
                                   + new("suciṇṇāni", "ကောင်းစွာ ပြုခဲ့ဖူးသည်") + "+",
                "anuppannaṃ kiriyasamāpattiṃ": f"{ANUPPANNA} {KIRIYA} {SAMAPATTI}",
                "anuppannaṃ kusalasamāpattiṃ": f"{ANUPPANNA} ကုသိုလ် {SAMAPATTI}",
                "anuppannaṃ samāpattiṃ": f"{ANUPPANNA} {SAMAPATTI}", "uppannaṃ": UPPANNA[:-len("သော")] + "သည်",
                "uppannaṃ samāpattiṃ": f"{UPPANNA} {SAMAPATTI}", "phalasamāpattiṃ": F.LEX["phalasamāpattiyā"][0],
                "rūpaṃ": F.FIXED["rūpāyatanaṃ"][0].split(" ")[0], "saddaṃ": "အသံ"})
F.add_lex("g", {"kāyikassa sukhassa": KAYIKA_S, "kāyikassa dukkhassa": KAYIKA_D, "vipākassa": "ကံ၏ အကျိုး",
                "dhammassa": F.DHAMMA, "pāṇātipātassa": DEEDS["pāṇātipāt"], "micchādiṭṭhiyā": DEEDS["micchādiṭṭhi"],
                "byāpādassa": W("byāpādo", "ဖျက်ဆီးလိုစိတ်", "1"), "mātughātikammassa": DEEDS["mātughātikamm"],
                "niyatamicchādiṭṭhiyā": DEEDS["niyatamicchādiṭṭhi"],
                "saṅghabhedakakammassa": DEEDS["saṅghabhedakakamm"], "ṭhānāṭhānakosallassa": KOSALLA,
                "pañcannaṃ viññāṇānaṃ": "သိစိတ် ငါးပါး+", "āvajjanāya": "စိတ်ညွတ်ခြင်း"})
for _k, _my in SAMB.items():
    F.LEX[f"{_k}ppaṭisambhidāya"] = (_my, "g")
F.add_lex("G", {"sekkhānaṃ": SEKKHA + "+", "arahato": ARAHA, "ariyānaṃ": "အရိယာ+"})
F.add_lex("i", {"dibbena cakkhunā": W("dibbena cakkhunā", "နတ်မျက်စိ", "2"),
                "dibbāya sotadhātuyā": W("dibbāya sotadhātuyā", "နတ်နား ဓာတ်", "5")})
F.add_lex("v", {"vipassanti": "ထိုးထွင်း၍ ရှုကြသည်", "assādenti abhinandanti": "သာယာ နှစ်သက်ကြသည်",
                "assādenti abhinandati": "သာယာကြ၍ နှစ်သက်သည်", "assādeti": "သာယာသည်", "assādenti": "သာယာကြသည်",
                "uppādeti": "ဖြစ်စေသည်", "uppādenti": "ဖြစ်စေကြသည်",
                "samāpajjati": W("samāpajjati", "ဝင်စား") + "သည်", "samāpajjanti": "ဝင်စားကြသည်"})
F.add_lex("x", {
    "sekkhā vā puthujjanā vā": f"{SEKKHA}တို့ဖြစ်စေ{C} {PUTHU}တို့ဖြစ်စေ",
    "rūpaṃ passati": "အဆင်းအရောင်ကို " + W("rūpaṃ passati", "မြင်") + "သည်", "rūpaṃ passanti": "အဆင်းအရောင်ကို မြင်ကြသည်",
    "saddaṃ suṇāti": "အသံကို " + W("suṇāti", "ကြားသည်", "1"), "saddaṃ suṇanti": "အသံကို ကြားကြသည်",
    "kusalākusale niruddhe": F.LEX["kusalākusalaṃ"][0] + " " + new("niruddhe", "ချုပ်ငြိမ်းသွားသောအခါ"),
    "niruddhe": "ချုပ်ငြိမ်းသွားသောအခါ",
    "tadārammaṇatā uppajjati": "စိတ်သည် " + new("tadārammaṇatā", "ထိုအာရုံကိုပင် အာရုံပြုသော အဖြစ်ဖြင့်")
                               + " " + F.UP,
    "pāṇaṃ hantvā": "သတ္တဝါကို " + new("hantvā", "သတ်၍"),
    "tassa paṭighātatthāya": new("tassa paṭighātatthāya", "ထိုအမှုကို ချေဖျက်ရန်"),
    "saṅghaṃ bhinditvā": "သံဃာကို " + new("bhinditvā", "ဖြိုခွဲ၍"),
    "sahajātaṃ": F.N["sahajāta"], "purejātaṃ": F.N["purejāta"], "pacchājātaṃ": F.N["pacchājāta"],
    "āhāraṃ": F.N["āhāra"], "indriyaṃ": F.N["indriya"], "sahajāto": F.N["sahajāta"],
    "pacchājātā": F.N["pacchājāta"], "sahajātākind": F.N["sahajāta"],
    "ārammaṇapurejātaṃ": f"{F.N['ārammaṇa']} {F.N['purejāta']}",
    "vatthupurejātaṃ": f"{F.VATTHU} {F.N['purejāta']}",
    "pakatūpanissayo": F.LEX["pakatūpanissayo"][0],
})
F.add_noun("ကံ", n=["kammaṃ"])
F.add_noun("ကံ၏ အကျိုး", g=["vipākassa"])
F.add_noun(F.N["adhipati"], n=["adhipati"])
F.add_noun("စိတ်ညွတ်ခြင်း", n=["āvajjanā"])
F.add_noun("သိစိတ်", gp=["viññāṇānaṃ"])
F.NP_NUM.update({"tiṇṇannaṃ": 3, "pañcannaṃ": 5})
F.PAA[5] = "ငါးပါး"
F.add_qual("အတူ ပေါ်ပေါက်သည့်", "sahajātā")              # as the sample's kamma kinds «… သည့် ကံ»
F.add_qual("ခဏ ကွဲပြားသည့်", "nānākkhaṇikā")
F.add_qual(F.FIXED["kabaḷīkāro §V§ āhāro"][0][:-len(" အာဟာရ")], "kabaḷīkāro")
for _p, _my in (("pañcaviññāṇaṃ", "သိစိတ် ငါးပါး"), ("bhavaṅgaṃ", "ဘဝင် စိတ်"),
                ("vipākamanodhātu", F.LEX["vipākamanodhātu"][0]),
                ("vipākamanoviññāṇadhātu", F.LEX["vipākamanoviññāṇadhātu"][0])):
    F.add_fixed(_my, "n", False, _p)
for _p in ("vipākamanodhātuyā", "vipākamanoviññāṇadhātuyā", "kiriyamanoviññāṇadhātuyā"):
    F.add_fixed(F.LEX[_p][0], "g", False, _p)
F.add_fixed("ဘဝင် စိတ်", "g", False, "bhavaṅgassa")
F.add_fixed("စိတ်ညွတ်ခြင်း", "g", False, "āvajjanāya")
SKF["vatthuṃ khandhā"] = f"{F.VATTHU}ကို မှီ၍ {F.KHANDHA}များ"        # «…, vatthuṃ [paṭicca] khandhā» (logged)
SK["sahajātāKIND"] = F.N["sahajāta"]
F.LEX["sahajātāKIND"] = (F.N["sahajāta"], "x")
KINDS = {"sahajātaṃ", "purejātaṃ", "pacchājātaṃ", "āhāraṃ", "indriyaṃ", "ārammaṇapurejātaṃ", "vatthupurejātaṃ"}
for _p, _my in (("āhārā", "အာဟာရ"), ("indriyā", "စွမ်းရည်"), ("jhānaṅgā", "ဈာန်၏ အင်္ဂါ"),
                ("maggaṅgā", F.FIXED["maggaṅgāni"][0])):
    F.add_noun(_my, np=[_p])
F.add_noun(MAHABHUTA, n=["mahābhūtaṃ"], g=["mahābhūtassa"])
F.add_fixed(f"{CITTASAM} {F.NOUN['rūpānaṃ'][0]}", "g", True, "cittasamuṭṭhānānaṃ rūpānaṃ")
F.add_fixed(F.PAA[3], "g", True, "tiṇṇannaṃ")                     # «… tiṇṇannaṃ…pe…» (elliptic)
SKF["purimā purimā"] = F.QUAL["purimā purimā"]
SKF["rūpāyatanaṃ cakkhuviññāṇassa purejāta"] = (f"{F.FIXED['rūpāyatanaṃ'][0]}သည် {F.FIXED['cakkhuviññāṇassa'][0]}အား "
                                                f"{F.N['purejāta']}")      # «purejāta…pe…» (cut short in the source)
SKF["ekā"] = F.COUNT["ekaṃ"]
SKF["tisso"] = F.COUNT["tīṇi"]
SKF["tīṇi (paṭisandhi kātabbā §V§.)"] = f"{F.COUNT['tīṇi']} ({F.PATISANDHI}ကို ထည့်ရမည် {{V1}}{END})"
SKF["vatthuṃ §C§ā (anantarasadisaṃ"] = f"{F.VATTHU} {{C1.ab}} ({F.N['anantara']}{F.SADISA}"
F.NOTES["(saṃkhittaṃ.)"] = f"({F.NOTES['(saṃkhittaṃ)'][1:-1]}{END})"
F.NOTES["(saṃkhittaṃ."] = f"({F.NOTES['(saṃkhittaṃ)'][1:-1]}{END}"
F.NOTES["=19"] = "=19"
F.NOTES["(saṃkhittaṃ"] = f"({F.NOTES['(saṃkhittaṃ)'][1:-1]}"
F.TERM_TAIL_OK.add("āni")
F.add_fixed(F.PAA[2], "g", True, "dvinnaṃ")                         # «… dvinnaṃ…pe…» (elliptic)
SKF["paccayo"] = F.IS_COND                                         # «purimā purimā…pe… paccayo.»
for _p, _my in _VIN.items():
    SKF[f"{_p}viññāṇasahagato"] = F.QUAL[f"{_p}viññāṇasahagato"]
F.add_lex("n", {"vatthu": F.VATTHU})
F.add_lex("x", {"ārabbha rāgo": "အာရုံပြု၍ " + F.LEX["rāgo"][0]})
SK["(vitthārena gaṇetabbaṃ.)"] = F.NOTES["(vitthārena gaṇetabbaṃ)"][:-1] + END + ")"
HLINES["Paccanīyaṃ"] = "အငြင်းပြ ပုံစံ"                                              # a stray «=19» in the source (kept, logged)
F.add_lex("x", {"tadārammaṇatā": "စိတ်သည် " + NEW["tadārammaṇatā"], "aniccato": "မမြဲဟု",
                "vicikicchaṃ ārabbha": "ယုံမှားမှုကို အာရုံပြု၍", "uddhaccaṃ ārabbha": "ယောက်ယက်ခတ်မှုကို အာရုံပြု၍"})
F.add_lex("a", {"vipassanaṃ": F.LEX["vipassanaṃ uppādeti"][0].split("ကို")[0]})
F.HEAD["Paccanīyaṃ"] = "အငြင်းပြ ပုံစံ"
HLINES["*2-6 Sahajāta-paccaya-nissaya-saṃsaṭṭha-sampayuttavāro*"] = (
    "*2-6 " + (C + " ").join(F.HEAD[v][:-len(F.VARA)] for v in ("Sahajātavāro", "Paccayavāro", "Nissayavāro",
                                                                  "Saṃsaṭṭhavāro"))
    + "နှင့် " + F.HEAD["Sampayuttavāro"] + "*")
HLINES["*Hetusāmaññaghaṭanā (9)*"] = f"*{F.cname('hetu')}၏ {F.HEAD['Sāmaññaghaṭanā']} (9)*"
HLINES["Paṭṭhānapāḷi paṭhamo bhāgo niṭṭhito."] = f"“{F.TITLE}” {F.HEAD['(Paṭhamo bhāgo)'][1:-1]} {F.DONE}{END}"
VARA_P = {v[0].lower() + v[1:] + "pi": F.HEAD[v] for v in ("Paṭiccavāro", "Sahajātavāro", "Paccayavāro",
                                                           "Nissayavāro", "Saṃsaṭṭhavāro", "Sampayuttavāro")}
SADISO = new("sadiso (X-pi Y-pi sadiso)", "တူသည်")
_VPA = "(?:" + "|".join(VARA_P) + ")"
VP_RE = re.compile(r"^\((?P<v>" + _VPA + "(?: " + _VPA + r")*) (?P<e>sadiso|vitthāretabbo)(?P<p>\.?)\)(?P<q>\.?)$")


def varapi(u):
    m = VP_RE.match(F.lc(u))
    if not m:
        return None
    vs = (C + " ").join(VARA_P[w] + "လည်း" for w in m["v"].split())
    e = SADISO if m["e"] == "sadiso" else S.PH["vitthāretabbo"]
    return f"({vs} {e}" + (END if m["p"] else "") + ")" + (END if m["q"] else "")


SAVIPAKA = f"{F.cname('vipāka')} ပါဝင်သော"
SK.update({
    "(avipākaṃ": "(" + new("avipākaṃ (ghaṭanā group)", f"{F.cname('vipāka')} မပါဝင်သော"),
    "(savipākaṃ": "(" + new("savipākaṃ (ghaṭanā group)", SAVIPAKA), "4)": "4)", "5)": "5)",
    "(catuvīsatipaccayā vitthāretabbā, §C§ā.)": f"({F.PACCAYA} {TEEN['catuvīsati'][1]}ပါးကို {S.PH['vitthāretabbo']}{C} "
                                               f"{{C1.ab}}{END})",
    "(ekā pañhā.)": f"({PANHA} {F.COUNT['ekaṃ']}{END})",
    "(natthi-vigataṃ anantarasadisaṃ, avigataṃ atthisadisaṃ.)":
        f"({F.N['natthi']}{C} {F.N['vigata']}သည် {F.N['anantara']}{F.SADISA}{C} {F.N['avigata']}သည် "
        f"{F.N['atthi']}{F.SADISA}{END})",
    "(paṭisandhipi imesaṃ tiṇṇannaṃ kātabbā.)": f"(ဤ {F.COUNT['tīṇi']}တို့၌ {F.PATISANDHI}ကိုလည်း ထည့်ရမည်{END})",
    "kusalattikassa gaṇanato upādinnattike gaṇanā gambhīrā sukhumatarā ca, evaṃ kātūna asammohantena gaṇetabbaṃ.)":
        (f"{S.KT}၏ {S.GANANA}ထက် {F.TIKA_NAME['Upādinnattikaṃ']}၌ {S.GANANA}သည် " + new("gambhīrā sukhumatarā ca",
         "နက်နဲ၍ ပို၍ သိမ်မွေ့သည်") + f"{C} " + new("evaṃ kātūna", "ဤသို့ ပြု၍") + f" {S.PH['asammuyhantena']} "
         f"{S.PH['gaṇetabbaṃ']}{END})"),
    "asammohantena eso sajjhāyamaggo.)": f"ဤသည်မှာ {S.PH['asammuyhantena']} " + new("sajjhāyamaggo",
                                          "သရဇ္ဈာယ်သည့် နည်းလမ်း") + f" ဖြစ်သည်{END})",
})

# --- the instructions «(Yathā kusalattike X Vpp, evaṃ [idhāpi] Y.)» (built from parts; the sample's own wording) -----
KT = S.KT                                                     # kusalattika «ကုသိုလ် သုံးမျိုးတွဲ»
GANANA, GANITA, EVAM = S.GANANA, S.GANITA, S.PH["evaṃ"]
YX = {"gaṇanā": GANANA,
      "paccanīyagaṇanā": S.ORDER["paccanīya"] + " " + GANANA,
      "anulomapaccanīyagaṇanā": S.ORDER["anulomapaccanīya"] + " " + GANANA,
      "paccanīyānulomagaṇanā": S.ORDER["paccanīyānuloma"] + " " + GANANA,
      "anulomagaṇanā": "အဟုတ်ပြ ပုံစံ၏ " + GANANA,
      "paṭiccagaṇanā": F.HEAD["Paṭiccavāro"] + "၏ " + GANANA,
      "pañhāvārassa anulomagaṇanā": F.HEAD["Pañhāvāro"] + "၏ အဟုတ်ပြ ပုံစံ၏ " + GANANA,
      "nahetumūlakaṃ": F.heading("Nahetumūlakaṃ"),
      "paccanīyānulomaṃ": "အငြင်းပြ အဟုတ်ပြ ပုံစံ",
      "paccanīyavāro": "အငြင်းပြ ပုံစံ" + F.VARA,
      "paṭiccavāro": F.HEAD["Paṭiccavāro"]}
VIBHATTA = new("vibhattā / vibhattaṃ (after yathā)", "ခွဲခြမ်းစိတ်ဖြာထားသည့်အတိုင်း")
YV = {"gaṇitā": GANITA, "gaṇitaṃ": GANITA, "vitthāritā": S.PH["vitthārito"], "vitthārito": S.PH["vitthārito"],
      "vitthāritaṃ": S.PH["vitthārito"], "vibhattā": VIBHATTA, "vibhattaṃ": VIBHATTA}
VIBHAJ = new("vibhajitabbaṃ / -bāni", "ခွဲခြမ်းစိတ်ဖြာရမည်")
YEND = {"gaṇetabbaṃ": S.PH["gaṇetabbaṃ"], "gaṇetabbā": S.PH["gaṇetabbaṃ"], "vitthāretabbaṃ": S.PH["vitthāretabbo"],
        "vitthāretabbā": S.PH["vitthāretabbo"], "vitthāretabbo": S.PH["vitthāretabbo"],
        "vitthāratabbaṃ": S.PH["vitthāretabbo"], "vibhajitabbaṃ": VIBHAJ}
YADV = {"idhāpi": new("idhāpi", "ဤနေရာ၌လည်း"), "idaṃ": new("idaṃ (object)", "ဤသည်ကို"), "idampi": S.IDAMPI}
SAJJH = S.PH["sajjhāyamaggena"]
Y_RE = re.compile(r"^(?P<o>\()?[Yy]athā kusalattik(?P<case>e|assa)(?: (?P<x>" + "|".join(sorted(YX, key=len, reverse=True))
                  + r"))?(?P<sj1> sajjhāyamaggena)?(?: (?P<v>" + "|".join(YV) + r"))?,? evaṃ(?: (?P<adv>"
                  + "|".join(YADV) + r"))? (?P<end>" + "|".join(YEND) + r")(?P<p1>\.?)(?P<c>\)?)(?P<p2>\.?)$")


def yatha(u):
    m = Y_RE.match(u)
    if not m:
        return None
    kt = KT + ("၌" if m["case"] == "e" else "၏")
    if m["x"] and m["v"]:
        a = f"{kt} {YX[m['x']]}ကို" + (f" {SAJJH}" if m["sj1"] else "") + f" {YV[m['v']]}"
    elif m["x"]:
        a = f"{kt} {YX[m['x']]}အတိုင်း"
    elif m["v"]:
        a = kt + (f" {SAJJH}" if m["sj1"] else "") + f" {YV[m['v']]}"
    else:
        a = f"{kt}ကဲ့သို့"
    adv = f" {YADV[m['adv']]}" if m["adv"] else ""
    out = (m["o"] or "") + a + adv + f" {EVAM} {YEND[m['end']]}"
    return out + (END if m["p1"] else "") + m["c"] + (END if m["p2"] else "")


# --- other unique sentences (by their Pāli skeleton, lower-case first letter) ----------------------------------------
SAMKHITTA = F.NOTES["(saṃkhittaṃ)"][1:-1]
PADA_ALL = f"{F.PADA} အားလုံးကို"
SK.update({
    "(saṃkhittaṃ.": f"({SAMKHITTA}{END}", "saṃkhittaṃ).": f"{SAMKHITTA}){END}", "saṃkhittaṃ)": f"{SAMKHITTA})",
    "(saṃkhittaṃ.)": f"({SAMKHITTA}{END})",
    "(anantarasadisaṃ.": f"({F.N['anantara']}{F.SADISA}{END}",
    "yathā anulomaṃ sahajātasadisaṃ.)": f"အဟုတ်ပြ ပုံစံကဲ့သို့ {F.N['sahajāta']}{F.SADISA}{END})",
    "sabbāni padāni vitthāretabbāni.)": f"{PADA_ALL} {S.PH['vitthāretabbo']}{END})",
    "(sabbāni padāni vibhajitabbāni.)": f"({PADA_ALL} {VIBHAJ}{END})",
})


# --- engine: units and fragments that the module's frames do not cover ----------------------------------------------
_unit0 = F.unit_my


def bits(sk, slots):
    """(1) «[pre] NP LINK [count]» (a pair whose second member is left out); (2) «[pre] NP [count | note]»;
    (3) «[pre] NP-nom NP-dat» (a pañhā sentence whose condition is left out: «X eko khandho tiṇṇannaṃ khandhānaṃ…»).
    Returns Burmese or None."""
    if any(slots[k] for k in "CKVD"):
        return None
    s = sk.strip()
    end = ""
    m = re.search(r"[.;,]$", s)
    if m:
        s, end = s[:-1], F.punct(m[0])
    note = ""
    for k in sorted(F.NOTES, key=len, reverse=True):
        if s.endswith(" " + k):
            s, note = s[:-len(k) - 1], " " + F.NOTES[k]
            break
    cnt = ""
    m = re.search(r" (" + F._CNT_ALT + r")$", s)
    if m:
        s, cnt = s[:m.start()], " " + F.COUNT[m[1]]
    words = s.split()
    pre = ""
    if words and words[0] in F.PREFIX:
        pre, words = F.PREFIX[words[0]] + " ", words[1:]
    if not words:
        return (pre.rstrip() + (" " if pre and cnt else "") + cnt.strip() + note + end).strip() \
            if (cnt or note or pre) else None
    # a list of condition kinds after the recipient: «X dhammo Yassa dhammassa sahajātaṃ, purejātaṃ.»
    k = len(words)
    while k > 0 and words[k - 1].rstrip(",") in KINDS:
        k -= 1
    if 0 < k < len(words) and all(w.endswith(",") for w in words[k:-1]):
        head = bits(" ".join(words[:k]), slots)
        if head is not None:
            kinds = (C + " ").join(F.LEX[w.rstrip(",")][0] for w in words[k:])
            return pre + head + " " + kinds + cnt + note + end
    if " ".join(words) in SKF:
        return pre + F.render(SKF[" ".join(words)], slots) + cnt + note + end
    try:
        if len(words) > 1 and words[-1] in F.LINK:
            terms = iter(slots["T"])
            a_lk, k = _coord_link(words[:-1], terms, words[-1]) if "ca" in words[:-1] else (None, 0)
            if a_lk is None:
                terms = iter(slots["T"])
                a_my, _, k = F.np_my(words[:-1], terms, "")
                a_lk = F.LINK[words[-1]](re.sub(r"များ$", "တို့", a_my))
            if k != len(slots["T"]):
                return None
            return pre + a_lk + cnt + note + end
        case = F._case_of(words)
        if case == "g":
            # harmonise H11 / H16: «NP-nom NP-dat…» before «…» (the condition left out: «rūpāyatanaṃ cakkhuviññāṇassa…»,
            # «eko khandho ca cakkhāyatanañca tiṇṇannaṃ khandhānaṃ…») is the conditioning / conditioned pair of the
            # pañhā frame, not one list of recipients: try (3) first
            r3 = _nom_dat(sk, slots, end)
            if r3 is not None:
                return r3
        if case in ("n", "a", "g"):
            terms = iter(slots["T"])
            my, _, k = F.np_my(words, terms, {"n": "", "a": "", "g": "g"}[case])
            if k == len(slots["T"]):
                return pre + my + cnt + note + end
    except (KeyError, StopIteration, IndexError, ValueError):
        pass
    return _nom_dat(sk, slots, end)


def _nom_dat(sk, slots, end):
    # (3) NP-nom NP-dat: the pañhā frame with a stand-in condition, then the condition text removed
    sl = dict(slots)
    sl["C"] = [("hetu", False)]
    r = _panha0(sk.strip().rstrip(".;,") + " §C§ena paccayo", sl)
    tail = " " + F.iframe("hetu")
    if r and r.endswith(tail):
        return r[:-len(tail)] + end
    return None


def _sub_slots(parts, slots):
    """split the slots of a skeleton among its comma parts (slots are numbered in Pāli order)"""
    pos = {k: 0 for k in slots}
    out = []
    for p in parts:
        sub = {}
        for k in slots:
            n = p.count(f"§{k}§")
            sub[k] = slots[k][pos[k]:pos[k] + n]
            pos[k] += n
        out.append(sub)
    return out


def part_my(p, sub):
    if p.strip() in SKF:
        return F.render(SKF[p.strip()], sub)
    m = re.match(r"^(.*?)( \([^()]*\))?((?: §C§ā)+)$", p)
    if m and m[1] and "§C§" not in m[1]:        # «… upādārūpaṃ (idaṃ nānattaṃ) Ārammaṇapaccayā»: a chain follows
        h = {k: (v if k != "C" else []) for k, v in sub.items()}
        r = part_my(m[1], h)
        if r is None:
            return None
        note = (" " + F.NOTES[m[2].strip()]) if m[2] else ""
        return r + note + " " + F.chain(m[3].strip(), sub, [0], [0], [0])
    r = None
    if not any(sub[k] for k in "CKVD"):
        r = F.pairs_mr(p, sub)
    return r if r is not None else bits(p, sub)


def pairs2(sk, slots):
    """«A, B, C» where each comma part is a pair, a pair without its second member, or a listed fragment"""
    body = sk.strip()
    end = ""
    if body[-1:] in ".;":
        body, end = body[:-1], F.punct(body[-1])
    parts = body.split(", ")
    if len(parts) < 2:
        return None
    outs = []
    for p, sub in zip(parts, _sub_slots(parts, slots)):
        try:
            r = part_my(p, sub)
        except (KeyError, StopIteration, IndexError, ValueError):
            r = None
        if r is None:
            return None
        outs.append(r)
    return (C + " ").join(outs) + end


def panha(sk, slots):        # noqa: F811  (replaces (b) above: pañhā frame, verbless pairs, bits)
    r = _panha0(sk, slots)
    if r is None and not any(slots[k] for k in "CKVD"):
        r = F.pairs_mr(sk, slots)
    if r is None:
        r = bits(sk, slots)
    if r is None:
        r = pairs2(sk, slots)
    return r


F.panha = panha


NODASH = re.compile(r"^(.* uppajj(?:ati|anti) (?:(?:na|no)?[a-zāīū]+paccayā ?)+) (ahetuk.*)$")


def unit_my(u):
    y = yatha(u.strip()) or varapi(u.strip())
    if y is not None:
        return u[:len(u) - len(u.lstrip())] + y
    m = re.match(r"^(\s*\(\d+\)) (\S.*)$", u) or re.match(r"^(.*?\.\)) (\S.*)$", u)
    if m:                                    # «(1) Vipāko …» / «(saṃkhittaṃ.) Nahetuyā …»: two units on one line
        return unit_my(m[1]) + " " + unit_my(m[2])
    m = NODASH.match(u)
    if m and " – " not in u:                 # «… uppajjati nahetupaccayā ahetukaṃ …» (no dash in the source)
        F.SLIPS.add(f"no dash before «{m[2][:30]}…»: translated as two parts, no dash added")
        return _unit0(m[1]) + " " + _unit0(m[2])
    return _unit0(u)


F.unit_my = unit_my

F.HLINES.update(HLINES)
F.SK.update(SK)
F.SKF.update(SKF)


def chapter(name):
    txt = F.translate(prep((PALI / name).read_text(encoding="utf-8-sig")))
    if not F.DEV:
        (OUT / name).write_text(txt, encoding="utf-8")
        print(f"wrote {name}: {sum(1 for l in txt.splitlines() if l)} lines")


if __name__ == "__main__":
    F.DEV = "--dev" in sys.argv
    if "--out" in sys.argv:                  # write a review copy elsewhere (inside pi-7-my/)
        OUT = pathlib.Path(sys.argv[sys.argv.index("--out") + 1]).resolve()
        del sys.argv[sys.argv.index("--out"):sys.argv.index("--out") + 2]
    names = [a for a in sys.argv[1:] if not a.startswith("--")] or NAMES
    for n in names:
        chapter(n)
    if F.DEV:
        for k, v in F.UNSEEN.items():
            print("SK:", k)
            print("   ", v)
        print(len(F.UNSEEN), "unmatched")
    if F.SLIPS:
        print("slips:", *sorted(F.SLIPS), sep="\n  ")
