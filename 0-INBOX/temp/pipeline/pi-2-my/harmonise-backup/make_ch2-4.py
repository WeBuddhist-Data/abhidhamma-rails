"""Burmese zero-shot of pi-2 chapters 2-ayatanavibhango, 3-dhatuvibhango, 4-saccavibhango.

usage: python3 -I -X utf8 make_ch2-4.py [chapter ...]        (default: the three chapters)
       python3 -I -X utf8 make_ch2-4.py --find REGEX [n]     (pi-1 Pāli sentences matching REGEX, with the final
                                                              pi-1 Burmese sentence; read only)
Model: make_sample.py. my2_formulas.py is imported and extended IN MEMORY only (never edited). Every line is
generated sentence by sentence:
  1. a Pāli sentence that also occurs in pi-1 gets pi-1's final Burmese sentence (rails text, read only);
  2. else a whole-sentence frame of this file (SENT) or the clause engine of my2_formulas (with EXTRA rules here);
  3. matter fragments go through the final pi-1 Rūpakaṇḍa engine (F.P1.clauses_my, rails patches applied).
A sentence nothing matches raises Miss; a chapter is written only when every line passed (else the misses are listed).
"""
import pathlib
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import my2_formulas as F  # noqa: E402

ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-2_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-2-burmese-plain-zeroshot_split_chapters"
NAMES_OUT = ["2-ayatanavibhango.md", "3-dhatuvibhango.md", "4-saccavibhango.md"]
P1 = F.P1
T = F.T
C, END, PE = F.C, F.END, F.PE
DH, DHP = F.DH, F.DHP
COP = F.COP
Miss = F.Miss


# ===================================================================================== pi-1 sentences (final)
def psplit(l):
    l = F.ID_RE.sub("", l)
    l = re.sub(r"\[[^\]]*\]", lambda m: m[0].replace(". ", ".\x00"), l)
    return [s.replace("\x00", " ") for s in re.split(r"(?<=[.?])(?:\"|”)? (?=\S)", l) if s]


def bsplit(l):
    l = F.ID_RE.sub("", l)
    return [s for s in re.split(r"(?<=။) ", l) if s]


def _pi1_pairs():
    for p in sorted(F.P1_PALI.glob("*.md")):
        pl = p.read_text(encoding="utf-8-sig").split("\n")
        bl = (F.P1_RAILS / p.name).read_text(encoding="utf-8").split("\n")
        for x, y in zip(pl, bl):
            if not x.strip() or x.startswith("#"):
                continue
            ps, bs = psplit(x), bsplit(y)
            if len(ps) == len(bs):
                for s, t in zip(ps, bs):
                    yield p.name, F.ID_RE.search(x)[1] if F.ID_RE.search(x) else "", s, t


D1 = {}
for _n, _i, _s, _t in _pi1_pairs():
    D1.setdefault(_s.replace("upādinn", "upādiṇṇ"), set()).add(_t)


def p1(pali_sentence):
    """The final pi-1 Burmese of a pi-1 Pāli sentence (must exist and be unique)."""
    v = D1.get(pali_sentence)
    if not v or len(v) != 1:
        raise SystemExit("pi-1 sentence not unique / not found: " + pali_sentence[:80])
    return next(iter(v))


def p1cut(pali_sentence, start, end):
    """A piece of a pi-1 Burmese sentence between two anchors (start inclusive if str, end exclusive)."""
    b = p1(pali_sentence)
    i = b.index(start) if start else 0
    j = b.index(end, i) if end else len(b)
    return b[i:j]


if __name__ == "__main__" and "--find" in sys.argv:
    _pairs = list(_pi1_pairs())
    for _pat in sys.argv[sys.argv.index("--find") + 1:]:
        rx = re.compile(_pat)
        hit = [(n, i, s, t) for n, i, s, t in _pairs if rx.search(s)]
        print(f"#### {_pat}: {len(hit)} hits")
        for n, i, s, t in hit[:1]:
            print(f"== {n} {i}\nPI: {s}\nMY: {t}\n")
    sys.exit()


# ===================================================================================== building blocks
C3 = F.C3
AYAT = C3["AYATANA"]                 # အာရုံခံ နယ်ပယ်
DHATU = C3["DHATU"]                  # ဓာတ်
NUMW = {"eka": "တစ်", "dvi": "နှစ်", "ti": "သုံး", "catu": "လေး", "pañca": "ငါး", "cha": "ခြောက်", "satta": "ခုနစ်",
        "aṭṭha": "ရှစ်", "nava": "ကိုး", "dasa": "ဆယ်", "ekādasa": "ဆယ့်တစ်", "dvādasa": "ဆယ့်နှစ်",
        "pannarasa": "ဆယ့်ငါး", "soḷasa": "ဆယ့်ခြောက်", "sattarasa": "ဆယ့်ခုနစ်", "aṭṭhārasa": "ဆယ့်ရှစ်"}
for _k in ("eka", "dvi", "ti", "catu", "pañca", "cha", "satta", "aṭṭha", "nava", "dasa"):
    assert P1.NUM[_k] == NUMW[_k]
assert C3["NUMW"]["ekādasa"] == NUMW["ekādasa"]
CL = P1.CL                           # ပါး


def count(x, n):
    return f"{x} {NUMW[n]}{CL}"


SACCA = "သစ္စာ"                       # sacca (pi-1 termbase saccaṃ)
ARIYA = "အရိယာ"                       # ariya (pi-1 termbase Ariya)
DUKKHA_T = "ဒုက္ခ"                    # dukkha, the first truth (pi-1 «Dukkhe ñāṇaṃ» = «ဒုက္ခကို သိသော ဉာဏ်»)
SAMUDAYA = "ဖြစ်ပေါ်ခြင်း"            # samudaya (pi-1 termbase)
NIRODHA = "ချုပ်ငြိမ်းခြင်း"           # nirodha (pi-1 termbase)
GAMINI = "ချုပ်ငြိမ်းရာသို့ ရောက်စေသော"   # nirodhagāminī (pi-1 ^1-1050 list «ဒုက္ခ ချုပ်ငြိမ်းရာသို့ ရောက်စေသော ကျင့်စဉ်»)
PATIPADA = P1.PATIPADA               # ကျင့်စဉ်
MAGGA = P1.MAGGA                     # မဂ်

# names (Pāli nominative, case-free first letter -> Burmese)
NM = {}
for _k, _v in C3["NOUN"].items():
    if _k.endswith(("āyatanaṃ", "dhātu")) and not _k.startswith("na "):
        NM[_k] = _v
for _k in ("manāyatanaṃ", "dhammāyatanaṃ", "manoviññāṇadhātu", "dhammadhātu", "vedanākkhandho", "saññākkhandho",
           "saṅkhārakkhandho", "viññāṇakkhandho"):
    NM[_k] = P1.NAMES[_k]
for _s in ("cakkhu", "sota", "ghāna", "jivhā", "kāya"):
    NM[_s + "viññāṇadhātu"] = f"{C3['SENSE'][_s]} {P1.VINNANA} {DHATU}"       # pi-1 ^1-1340
NM["manodhātu"] = f"{P1.MANO} {DHATU}"                                     # pi-1 ^1-1340
NM["rūpakkhandho"] = F.KH["rūpakkhandho"][0]
NM["asaṅkhatā dhātu"] = f"{T['asaṅkhatā']} {DHATU}"                        # pi-1 C3 «asaṅkhatā ca dhātu»
NEW = {}            # group -> [(pāli, burmese)] for the notes


def new(group, table, k, v):
    if k in table and table[k] != v:
        raise SystemExit(f"conflict {k}: {table[k]} / {v}")
    table[k] = v
    NEW.setdefault(group, []).append((k, v))


def nm(p):
    k = p[0].lower() + p[1:]
    if k not in NM:
        raise Miss("name: " + p)
    return NM[k]


# ===================================================================================== variants
SIG = dict(P1.SIGLA)
SIG.update({"sabbattha": "Sabbattha", "?": "ရင်းမြစ် မသေချာ"})      # «(?)» = source uncertain (no «?» in the text)
EVAM_UPARI = "အောက်တွင်လည်း ဤနည်းအတိုင်း"     # evamuparipi (likewise further on)
VKIND = {}          # variant text -> PATHA / LEKHANA


def var_my(br):
    """Any Pāli variant bracket: «[t (s.)]», «[t1 (s.), t2 (s.)]», «[t1 (s.) t2 (s.)]», «[t (s.) evamuparipi]»,
    «[t (s.) dha. sa. 596-599]»."""
    inner = br[1:-1]
    tail = ""
    m = re.fullmatch(r"(?P<a>.+\))(?P<t> evamuparipi| dha\. sa\. [0-9-]+)", inner)
    if m:
        inner, tail = m["a"], m["t"].strip()
    parts = re.findall(r"\s*(?P<t>[^(),]+?) \((?P<s>[^()]+)\),?", inner)
    if "".join(f"{t} ({s})" for t, s in parts).replace(" ", "") != inner.replace(",", "").replace(" ", ""):
        raise Miss("variant: " + br)
    kinds = {VKIND.get(t) or F.VAR_KIND.get(t) for t, _ in parts}
    if None in kinds or len(kinds) != 1:
        raise Miss("variant kind: " + br)
    segs = []
    for i, (t, s) in enumerate(parts):
        sig = ", ".join(SIG[x] for x in s.split())
        segs.append(f"({sig}): {t}")
    out = f"[{kinds.pop()} " + f"{C} ".join(segs)
    if tail == "evamuparipi":
        out += f"{C} {EVAM_UPARI}"
    elif tail:
        out += f"{C} “{P1.TITLE}” {tail.split()[-1]}"
    return out + "]"


for _k, _v in {"cakkhuṃ": F.P1.LEKHANA, "pītaṃ lohitaṃ": F.P1.LEKHANA, "mutiṅgasaddho": F.P1.LEKHANA,
               "lapilakaṃ": F.P1.PATHA, "lampikaṃ": F.P1.PATHA}.items():
    VKIND[_k] = _v
VAR_TOKEN = re.compile(r" ?\[[^\]]+\]")


# ===================================================================================== pi-1 matter engine (final)
def norm_matter(s):
    """Vb spellings -> the pi-1 spellings of the same words (sandhi only)."""
    s = re.sub(r"mpe(taṃ|so|sā)" + F.NA, r"ṃ pe\1", s)
    return s


P1.var_my = var_my                  # in memory: the pi-1 engines (C3 kinds, r_var) use the wider variant reader
F.var_my = var_my
for _k, _v in {"caturassaṃ": "caturaṃsaṃ"}.items():
    C3["COLOUR"][_k] = C3["COLOUR"][_v]
C3["COLOUR_GEN"]["maṇisaṅkhamuttaveḷuriyassa"] = C3["COLOUR_GEN"]["maṇisaṅkhamuttāveḷuriyassa"]
C3["SMELL"]["āmagandho"] = C3["SMELL"]["āmakagandho"]
C3["TASTE"]["lambikaṃ"] = C3["TASTE"]["lambilaṃ"]
for _a, _b in (("caturassaṃ", "caturaṃsaṃ"), ("maṇisaṅkhamuttaveḷuriyassa", "maṇisaṅkhamuttāveḷuriyassa"),
               ("āmagandho", "āmakagandho"), ("lambikaṃ", "lambilaṃ")):
    NEW.setdefault("Spelling of pi-1 list words (same Burmese as pi-1)", []).append((_a, f"as pi-1 {_b}"))


def r_obj_short(m):
    o = {"saddo": "sadda", "gandho": "gandha", "raso": "rasa"}[m["o"]]
    return f"{C3['UPADAYA4']} ဖြစ်သော{C} {C3['A_NS']} {C3['OBJECT'][o]}"


QOPEN = {'"': "“", "‘": "‘"}
QCLOSE = {'"': "”", "‘": "’"}


def name_my(x):
    """A quoted or bare name in «ayaṃ vuccati X»."""
    k = x[0].lower() + x[1:]
    if k in NM:
        return NM[k]
    if k in EXTRA_NAMES:
        return EXTRA_NAMES[k]
    m = re.fullmatch(r"rūpaṃ (?P<p>.+)", k)
    if m:
        return f"{C3['chain_my'](m['p'])} {F.RUPA}"
    raise Miss("vuccati name: " + x)


EXTRA_NAMES = {}


def r_vuccati_q(m):
    pl = m["v"] == "vuccanti"
    o = m["o"]
    pre = m["pre"]
    x = name_my(m["x"]) if not pre else C3["chain_my"](m["x"])
    tail = f" {F.RUPA}" if pre else ""
    dem = "ဤသည်" + ("တို့" if pl else "") + ("လည်း" if m["d"].lower() == "idampi" else "")
    dash = " –" if m["dash"] else ""
    return f"{dem}ကို{dash} {QOPEN[o]}{x}{QCLOSE[o]}{tail}ဟု ခေါ်သည်"


def r_vuccati_bare(m):
    return f"ဤသည်ကို {name_my(m['x'])}ဟု ခေါ်သည်"


VUCC_Q = (r"(?P<d>[Aa]yaṃ|[Ii]daṃ|[Ii]me|[Ii]dampi) (?P<v>vuccati|vuccanti)(?P<dash> –)? (?P<pre>rūpaṃ )?(?P<o>[\"‘])"
          r"(?P<x>[^\"’]+)[\"’]")
VUCC_B = r"(?:[Aa]yaṃ|[Ii]daṃ) vuccati (?P<x>[^\".–;?‘’]+?)(?=\.|$| –)"
CU_MORE = [
    (re.compile(VUCC_Q), r_vuccati_q),
    (re.compile(r"Yo (?P<o>saddo|gandho|raso) catunnaṃ mahābhūtānaṃ upādāya anidassano sappaṭigho(?=…pe…)"),
     r_obj_short),
]
P1.CU_EXTRA_RULES[:0] = CU_MORE
P1.rebuild_cu()


# ===================================================================================== engine extensions (in memory)
HEAD_NEW = {
    "Āyatanavibhaṅgo": f"{AYAT}များကို {F.TITLE}",
    "Dhātuvibhaṅgo": f"{DHATU}များကို {F.TITLE}",
    "Saccavibhaṅgo": f"{SACCA}များကို {F.TITLE}",
}
for _k, _v in HEAD_NEW.items():
    new("Headings and colophons", F.HEAD, _k, _v)
    new("Headings and colophons", F.COLO, _k + " niṭṭhito", f"“{_v}” {F.NITTHITA}")

# pañhāpucchaka subjects: (Burmese, topic noun, plural)
SUBJ_COUNT = {"dvādasa": "dvādasa", "ekādasa": "ekādasa", "dasa": "dasa", "nava": "nava", "cha": "cha",
              "pañca": "pañca", "dvā": "dvi"}
for _p, _n in (("dasāyatanā", "dasa"), ("dvāyatanā", "dvi"), ("pañcāyatanā", "pañca"), ("cattāro āyatanā", "catu"),
               ("ekādasāyatanā", "ekādasa"), ("navāyatanā", "nava"), ("chāyatanā", "cha")):
    new("Subjects (pañhāpucchaka)", F.KH, _p, (count(AYAT, _n), None, True))
for _p in ("manāyatanaṃ", "dhammāyatanaṃ", "rūpāyatanaṃ", "saddāyatanaṃ"):
    F.KH[_p] = (NM[_p], None, False)
F.KH["manāyatanaṃ"] = (NM["manāyatanaṃ"], "manāyatana", False)
F.NOUN["manāyatana"] = dict(my=NM["manāyatanaṃ"], pl=False, forms={"manāyatanaṃ"})
NEW.setdefault("Topic noun of «atthi T» (abhidhamma part)", []).append(("manāyatanaṃ", NM["manāyatanaṃ"]))

# heads of the enumerations «N X – a, b, …» and of «N-annaṃ X-ānaṃ kati …»
COUNT_HEAD = {}
COUNT_AMONG = {}


def r_count_head(m):
    return COUNT_HEAD[m[0]]


def r_count_among(m):
    STATE["pl"] = True
    return COUNT_AMONG[m[0]]


STATE = F.STATE


def r_nv_subj(m):
    """Subject with the neuter «na vattabbaṃ» (the sample rule covers -o / -ā)."""
    if STATE.get("part") != "pan":
        return None
    name, n, pl = F.kh(m["s"])
    STATE["pl"] = pl
    if m["nv"]:
        STATE["nv"] = True
    return f"{name}သည်"


BUT = "သို့သော်"                      # «…, na vattabbā – "X"ti» after siyā clauses (but it cannot be called …)


def r_nv_mid(m):
    STATE["nv"] = True
    return BUT


def r_pred_bare(m):
    return f"{F.term_my(m['t'])} {DH} {COP[False]}"


def r_items_more(m):
    return F.r_itemrun(m)


def install_rules():
    kh_alt = F._alt(F.KH)
    rules = RULES_MORE + [
        (_esc_keys(COUNT_HEAD) + r"(?= – )", r_count_head),
        (_esc_keys(COUNT_AMONG) + r"(?= kati)", r_count_among),
        (VUCC_Q, r_vuccati_q),
        (VUCC_B, r_vuccati_bare),
        (r"(?P<s>" + kh_alt + r")(?P<nv> na vattabb(?:o|ā|aṃ)(?= – ))?(?= )", r_nv_subj),
        (r"siyā na vattabbaṃ(?= – )", F.r_siya_nv),
        (r"na vattabb(?:o|ā|aṃ)(?= – )", r_nv_mid),
        (r"(?P<t>phassasampayuttaṃ)" + F.NA, r_pred_bare),
        (r"(?:" + F._alt(F.ITEM) + r")(?: (?:" + F._alt(F.ITEM) + r"))+(?=…| …)", F.r_itemrun),
        (r"\[[^\]]+\]", lambda m: var_my(m[0])),
        (r"…(?!pe…|Pe…)", lambda m: PE),
    ]
    F.EXTRA_RULES[:] = [(r, f) for r, f in rules]
    F.rebuild()


def _esc_keys(d):
    return "(?:" + "|".join(re.escape(k) for k in sorted(d, key=len, reverse=True)) + ")" if d else "(?!x)x"


RULES_MORE = []          # chapter frames added below


# ===================================================================================== the sentence dispatcher
SENT = []                # (compiled fullmatch regex on a Pāli sentence, function(match) -> Burmese sentence)
SLIPS = {}               # Pāli as written -> Pāli as read (source slips, logged in the notes)


def pre_pan(s):
    """pañhāpucchaka: the joined neuter «Xañca / Xañcā / Xañceva» -> «Xaṃ ca / cā / ceva» (the pi-1 CEVA keys)."""
    s = re.sub(r"(\w)ñceva" + F.NA, r"\1ṃ ceva", s)
    s = re.sub(r"(?<![\wāīūṃṅñṭḍṇḷ])(?![Pp]añc)([\wāīūṃṅñṭḍṇḷ]+?)ñc([aā])(?=[\",.; ]|$)", r"\1ṃ c\2", s)
    return s


def sentence_my(s):
    k = s.replace("upādinn", "upādiṇṇ")
    if k in D1 and len(D1[k]) == 1:
        REUSED.append(s)
        return next(iter(D1[k]))
    for rx, f in SENT:
        m = rx.fullmatch(s)
        if m:
            return f(m)
    for a, b in SLIPS.items():
        s = s.replace(a, b)
    if STATE.get("part") == "pan":
        s = pre_pan(s)
    errs = []
    for eng in (F.clauses_my, P1.clauses_my):
        for kk in ("pl", "nv"):
            STATE.pop(kk, None)
        try:
            return eng(norm_matter(s) if eng is P1.clauses_my else s)
        except Miss as e:
            errs.append(str(e))
    raise Miss(" || ".join(errs))


REUSED = []


def line_my(body):
    body = body.replace("upādinn", "upādiṇṇ")
    if body.startswith("#") or (body.endswith(".") and body[:-1] in F.COLO) or body in F.FIXED or \
            re.fullmatch(r"\(.+\)", body):
        return F.line_my(body)
    return " ".join(sentence_my(x) for x in psplit(body))


def translate_line(line):
    if not line.strip():
        return ""
    m = F.ID_RE.search(line)
    body = line[:m.start()] if m else line
    return line_my(body) + (" " + m.group(1) if m else "")


def sent(pattern):
    def deco(f):
        SENT.append((re.compile(pattern), f))
        return f
    return deco


def rule(pattern):
    def deco(f):
        RULES_MORE.append((pattern, f))
        return f
    return deco


# ===================================================================================== chapter 2: āyatana
COUNT_HEAD["Dvādasāyatanāni"] = count(AYAT, "dvādasa")
COUNT_AMONG["Dvādasannaṃ āyatanānaṃ"] = count(AYAT, "dvādasa") + "တို့အနက်"
assert p1("Dvādasāyatanāni – cakkhāyatanaṃ, rūpāyatanaṃ, sotāyatanaṃ, saddāyatanaṃ, ghānāyatanaṃ, gandhāyatanaṃ, "
          "jivhāyatanaṃ, rasāyatanaṃ, kāyāyatanaṃ, phoṭṭhabbāyatanaṃ, manāyatanaṃ, dhammāyatanaṃ.").startswith(
    COUNT_HEAD["Dvādasāyatanāni"] + " – ")
QUESTION = "ဟူသည် အဘယ်နည်း"
QUESTION_PL = "ဟူသည် အဘယ်တို့နည်း"


@sent(r"Tattha katam(?:o|ā|aṃ) (?P<x>[^?]+)\?")
def s_question(m):
    x = m["x"]
    mm = re.fullmatch(r"rūpaṃ (?P<p>.+)", x)
    if mm:
        return f"ထိုတို့အနက် {C3['chain_my'](mm['p'])} {F.RUPA} {QUESTION}{END}"
    return f"ထိုတို့အနက် {name_my(x)} {QUESTION}{END}"


# «X aniccaṃ dukkhaṃ anattā vipariṇāmadhammaṃ» (the twelve bases, suttanta part)
ANICCA = C3["EKA_NEW"]["aniccaṃ"]                      # မမြဲသော (pi-1 termbase aniccaṃ)
DUKKHA_C = f"{DUKKHA_T} ဖြစ်သော"                        # dukkha (characteristic; as the first truth)
ANATTA = "အတ္တ မဟုတ်သော"                              # anattā (not self)
VIPARINAMA = "ဖောက်ပြန်ပြောင်းလဲတတ်သော သဘော ရှိသော"   # vipariṇāmadhamma (of a nature to change)
for _k, _v in (("aniccaṃ / aniccā / anicco", ANICCA), ("dukkhaṃ / dukkhā / dukkho (characteristic)", DUKKHA_C),
               ("anattā", ANATTA), ("vipariṇāmadhammaṃ / -ā / -o", VIPARINAMA)):
    NEW.setdefault("Characteristics (āyatana suttanta part)", []).append((_k, _v))
TWELVE = {"cakkhuṃ": (C3["SENSE"]["cakkhu"], False), "sotaṃ": (C3["SENSE"]["sota"], False),
          "ghānaṃ": (C3["SENSE"]["ghāna"], False), "jivhā": (C3["SENSE"]["jivhā"], False),
          "kāyo": (C3["SENSE"]["kāya"], False), "mano": (P1.MANO, False),
          "rūpā": (C3["OBJECT"]["rūpa"], True), "saddā": (C3["OBJECT"]["sadda"], True),
          "gandhā": (C3["OBJECT"]["gandha"], True), "rasā": (C3["OBJECT"]["rasa"], True),
          "phoṭṭhabbā": (C3["OBJECT"]["phoṭṭhabba"], True), "dhammā": (DH, True)}


@sent(r"(?P<x>\S+) anicc(?:aṃ|ā|o) dukkh(?:aṃ|ā|o) anattā vipariṇāmadhamm(?:aṃ|ā|o)\.")
def s_anicca(m):
    k = m["x"][0].lower() + m["x"][1:]
    if k not in TWELVE:
        raise Miss("twelve: " + k)
    x, pl = TWELVE[k]
    subj = f"{x}တို့သည်" if pl else f"{x}သည်"
    return f"{subj} {ANICCA}{C} {DUKKHA_C}{C} {ANATTA}{C} {VIPARINAMA} {'အရာများ' if pl else 'အရာ'} {COP[pl]}{END}"


for _k, _v in {"rāgakkhayo": f"{P1.RAGA} {P1.SYN['khayo']}", "dosakkhayo": f"ဒေါသ {P1.SYN['khayo']}",
               "mohakkhayo": f"မောဟ {P1.SYN['khayo']}"}.items():
    new("List items", F.ITEM, _k, _v)
for _k in ("manāyatanaṃ", "dhammāyatanaṃ"):
    F.ITEM.setdefault(_k, NM[_k])
IRREG = {
    "na hetūahetukā": "na hetū ahetukā", "arūpaṃ": "arūpino", "rūpā": "rūpino", "arūpāni": "arūpino",
    "cittena sampayuttaṃ": "cittasampayuttā", "cittena vippayuttaṃ": "cittavippayuttā",
    "cittena saṃsaṭṭhaṃ": "cittasaṃsaṭṭhā", "cittena visaṃsaṭṭhaṃ": "cittavisaṃsaṭṭhā",
    "cittena sampayuttā": "cittasampayuttā", "cittena vippayuttā": "cittavippayuttā",
    "cittena saṃsaṭṭhā": "cittasaṃsaṭṭhā", "cittena visaṃsaṭṭhā": "cittavisaṃsaṭṭhā",
}
for _k, _v in IRREG.items():
    F.TERM_IRREG.setdefault(_k, _v)
SLIPS.update({
    # 2-ayatanavibhango
    "jīvhindriyampetaṃ": "jivhindriyampetaṃ",
    '"saṃyojanañceva saṃyojaniya"ntipi': '"saṃyojanañceva saṃyojaniyañcā"tipi',
    '"upādāniyañceva upādānasampayuttañcā"ti': '"upādānañceva upādānasampayuttañcā"ti',
    "siyā upādānasampayuttaupādāniyā": "siyā upādānavippayuttaupādāniyā",
    "kilesasampayuttā ceva no ca na kilesā": "kilesasampayuttā ceva no ca kilesā",
})


# ===================================================================================== pi-1 synonym lists, item by item
MULTI = ["cittassa āghāto", "cittassa byāpatti", "anattamanatā cittassa", "cetaso abhiniropanā", "cittassa sārāgo",
         "kāyikaṃ sātaṃ", "kāyikaṃ sukhaṃ", "kāyikaṃ asātaṃ", "kāyikaṃ dukkhaṃ", "cetasikaṃ asātaṃ",
         "cetasikaṃ dukkhaṃ", "kāyasamphassajaṃ sātaṃ sukhaṃ vedayitaṃ", "kāyasamphassajā sātā sukhā vedanā",
         "kāyasamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ", "kāyasamphassajā asātā dukkhā vedanā",
         "cetosamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ", "cetosamphassajā asātā dukkhā vedanā",
         "catūhi vacīduccaritehi ārati", "tīhi kāyaduccaritehi ārati", "micchāājīvā ārati"]


def learn(pali_sentence, gen=None):
    """Read the items of a pi-1 synonym list «Yo / Yā / Yaṃ [tasmiṃ samaye] [GEN] A B … – …» and its final pi-1
    Burmese item by item into P1.SYN (new keys only; an existing key must agree)."""
    my = p1(pali_sentence)
    m = re.match(r"(?:Yo|Yā|Yaṃ)(?: evarūpo| evarūpā)?(?: tasmiṃ samaye)? (?P<l>.+?) – ", pali_sentence)
    lst = m["l"]
    if gen:
        lst = lst[len(gen) + 1:]
    b = my.split(" – ")[0]
    for pre in ("ထိုအချိန်၌ ", "ဤသို့ သဘောရှိသော "):
        b = b.removeprefix(pre)
    if gen:
        b = b.split(" ", gen.count(" ") + 1 + GEN_WORDS.get(gen, 0))[-1]
    b = b.removesuffix(" ရှိသမျှ")
    items_b = [re.sub(r" \[[^\]]*\]", "", x) for x in b.split(f"{C} ")]
    toks = re.sub(r" ?\[[^\]]*\]", "", lst).split(" ")
    items_p, i = [], 0
    while i < len(toks):
        for k in range(6, 0, -1):
            ph = " ".join(toks[i:i + k])
            if len(toks[i:i + k]) == k and (k == 1 or ph in MULTI or ph in P1.SYN or ph in P1.NAMES):
                items_p.append(ph)
                i += k
                break
    if len(items_p) != len(items_b):
        raise SystemExit(f"learn: {len(items_p)} Pāli / {len(items_b)} Burmese items: {pali_sentence[:60]}")
    for a, bb in zip(items_p, items_b):
        old = P1.SYN.get(a) or P1.NAMES.get(a)
        if old is not None and old != bb:
            raise SystemExit(f"learn conflict {a}: {old} / {bb}")
        P1.SYN.setdefault(a, bb)
    return items_p


GEN_WORDS = {}
learn("Yaṃ tasmiṃ samaye aññāṇaṃ adassanaṃ anabhisamayo ananubodho asambodho appaṭivedho asaṃgāhanā apariyogāhanā "
      "asamapekkhanā apaccavekkhanā apaccakkhakammaṃ dummejjhaṃ bālyaṃ asampajaññaṃ moho pamoho sammoho avijjā "
      "avijjogho avijjāyogo avijjānusayo avijjāpariyuṭṭhānaṃ avijjālaṅgī moho akusalamūlaṃ – ayaṃ tasmiṃ samaye "
      "moho hoti.")
learn("Yo tasmiṃ samaye takko vitakko saṅkappo appanā byappanā cetaso abhiniropanā micchāsaṅkappo – ayaṃ tasmiṃ "
      "samaye vitakko hoti.")
learn("Yo tasmiṃ samaye takko vitakko saṅkappo appanā byappanā cetaso abhiniropanā sammāsaṅkappo – ayaṃ tasmiṃ "
      "samaye vitakko hoti.")
learn("Yo evarūpo cittassa āghāto paṭighāto paṭighaṃ paṭivirodho kopo pakopo sampakopo doso padoso sampadoso "
      "cittassa byāpatti manopadoso kodho kujjhanā kujjhitattaṃ doso dussanā dussitattaṃ byāpatti byāpajjanā "
      "byāpajjitattaṃ virodho paṭivirodho caṇḍikkaṃ asuropo anattamanatā cittassa – ayaṃ vuccati doso.")
learn("Yo adoso adussanā adussitattaṃ metti mettāyanā mettāyitattaṃ anuddā anuddāyanā anudāyitattaṃ hitesitā "
      "anukampā abyāpādo abyāpajjo adoso kusalamūlaṃ – ayaṃ vuccati adoso.")
GEN_WORDS["tajjākāyaviññāṇadhātusamphassajaṃ"] = 5
learn("Yaṃ tasmiṃ samaye tajjākāyaviññāṇadhātusamphassajaṃ kāyikaṃ sātaṃ kāyikaṃ sukhaṃ kāyasamphassajaṃ sātaṃ sukhaṃ "
      "vedayitaṃ kāyasamphassajā sātā sukhā vedanā – ayaṃ tasmiṃ samaye vedanā hoti.",
      gen="tajjākāyaviññāṇadhātusamphassajaṃ")
learn("Yaṃ tasmiṃ samaye tajjākāyaviññāṇadhātusamphassajaṃ kāyikaṃ asātaṃ kāyikaṃ dukkhaṃ kāyasamphassajaṃ asātaṃ "
      "dukkhaṃ vedayitaṃ kāyasamphassajā asātā dukkhā vedanā – ayaṃ tasmiṃ samaye vedanā hoti…pe….",
      gen="tajjākāyaviññāṇadhātusamphassajaṃ")
GEN_WORDS["tajjāmanoviññāṇadhātusamphassajaṃ"] = 5
learn("Yaṃ tasmiṃ samaye tajjāmanoviññāṇadhātusamphassajaṃ cetasikaṃ asātaṃ cetasikaṃ dukkhaṃ cetosamphassajaṃ asātaṃ "
      "dukkhaṃ vedayitaṃ cetosamphassajā asātā dukkhā vedanā – ayaṃ tasmiṃ samaye vedanā hoti…pe….",
      gen="tajjāmanoviññāṇadhātusamphassajaṃ")
# Vb spellings of the same list words (avijjā list): same Burmese as pi-1
for _a, _b in (("asaṅgāhaṇā", "asaṃgāhanā"), ("apariyogāhaṇā", "apariyogāhanā"), ("apaccavekkhaṇā", "apaccavekkhanā")):
    P1.SYN[_a] = P1.SYN[_b]
    NEW.setdefault("Spelling of pi-1 list words (same Burmese as pi-1)", []).append((_a, f"as pi-1 {_b}"))


# ===================================================================================== chapter 3: dhātu
SEYYATHIDAM = "ဆိုလိုသည်မှာ"                            # seyyathidaṃ (namely, that is)
VA_PANA = "အခြား"                                       # yaṃ vā panaññampi atthi … (pi-1 «… အခြား … ရှိသမျှလည်း»)
REL = "ရှိသမျှ"                                         # Yo / Yaṃ / Yā (pi-1 rails L02)
ARA = "အရာ"
ELEM = {k: C3["NOUN"][k] for k in ("pathavīdhātu", "āpodhātu", "tejodhātu", "vāyodhātu", "ākāsadhātu")}
NEWNAMES = {
    "viññāṇadhātu": f"{P1.VINNANA} {DHATU}",
    "sukhadhātu": f"{P1.SUKHA}မှု {DHATU}", "dukkhadhātu": f"{P1.DUKKHA}မှု {DHATU}",
    "somanassadhātu": f"{P1.SOMANASSA} {DHATU}", "domanassadhātu": f"စိတ်ဆင်းရဲမှု {DHATU}",
    "upekkhādhātu": f"ဥပေက္ခာ {DHATU}", "avijjādhātu": f"{T['avijjā'] if 'avijjā' in T else 'အမှန်ကို မသိမှု'} {DHATU}",
    "kāmadhātu": f"ကာမ {DHATU}", "byāpādadhātu": f"{P1.JH_BYAPADA} {DHATU}", "vihiṃsādhātu": f"ညှဉ်းပန်းမှု {DHATU}",
    "nekkhammadhātu": f"ကာမမှ ထွက်မြောက်ခြင်း {DHATU}", "abyāpādadhātu": f"{P1.NAMES['abyāpādo']} {DHATU}",
    "avihiṃsādhātu": f"ညှဉ်းပန်းမှု မရှိခြင်း {DHATU}",
}
for _k, _v in NEWNAMES.items():
    new("Names (elements)", NM, _k, _v)
for _k, _v in ELEM.items():
    NM[_k] = _v
    new("Names (elements)", NM, "ajjhattikā " + _k, f"{T['ajjhattikā']} {_v}")
    new("Names (elements)", NM, "bāhirā " + _k, f"{T['bāhirā']} {_v}")
for _k in list(NM):
    if " " not in _k:
        if F.ITEM.get(_k, NM[_k]) != NM[_k]:
            raise SystemExit("item conflict " + _k)
        F.ITEM.setdefault(_k, NM[_k])
VKIND.update({"paṭhavīdhātu": P1.LEKHANA, "nahāru": P1.LEKHANA, "aṭṭhimiñjā": P1.LEKHANA, "sajjhu": P1.LEKHANA,
              "lohitaṅgo": P1.LEKHANA, "lohitako": P1.LEKHANA, "kathalaṃ": P1.LEKHANA,
              "sneho snehagataṃ": P1.LEKHANA, "koṭṭhasayā": P1.LEKHANA, "sakalikaggi": P1.PATHA, "rūpaṃ": P1.LEKHANA})
COUNT_HEAD.update({"Cha dhātuyo": count(DHATU, "cha"), "Aparāpi cha dhātuyo": "နောက်ထပ် " + count(DHATU, "cha"),
                   "Aṭṭhārasa dhātuyo": count(DHATU, "aṭṭhārasa")})
COUNT_AMONG["Aṭṭhārasannaṃ dhātūnaṃ"] = count(DHATU, "aṭṭhārasa") + "တို့အနက်"
assert p1("Aṭṭhārasa dhātuyo cakkhudhātu rūpadhātu cakkhuviññāṇadhātu, sotadhātu saddadhātu sotaviññāṇadhātu, "
          "ghānadhātu gandhadhātu ghānaviññāṇadhātu, jivhādhātu rasadhātu jivhāviññāṇadhātu, kāyadhātu "
          "phoṭṭhabbadhātu kāyaviññāṇadhātu, manodhātu dhammadhātu manoviññāṇadhātu.").startswith(
    COUNT_HEAD["Aṭṭhārasa dhātuyo"] + " ")
for _p, _n in (("soḷasa dhātuyo", "soḷasa"), ("dve dhātuyo", "dvi"), ("dasa dhātuyo", "dasa"), ("pañca dhātuyo", "pañca"),
               ("pannarasa dhātuyo", "pannarasa"), ("sattarasa dhātuyo", "sattarasa"), ("cha dhātuyo", "cha"),
               ("nava dhātuyo", "nava"), ("aṭṭha dhātuyo", "aṭṭha"), ("satta dhātuyo", "satta"),
               ("ekādasa dhātuyo", "ekādasa"), ("dvādasa dhātuyo", "dvādasa"), ("tisso dhātuyo", "ti"),
               ("sattadhātuyo", "satta")):
    new("Subjects (pañhāpucchaka)", F.KH, _p, (count(DHATU, _n), None, True))
for _p in ("kāyaviññāṇadhātu", "manoviññāṇadhātu", "dhammadhātu", "manodhātu", "saddadhātu", "rūpadhātu"):
    F.KH[_p] = (NM[_p], None, False)
F.TERM_IRREG.setdefault("uppādinī", "uppādino")

# the qualifiers of the element definitions (pi-1 4-01 list words and Mātikā terms)
EQ = {"ajjhattaṃ": F.DEF["ajjhatt"], "paccattaṃ": F.DEF["paccatt"], "upādinnaṃ": F.DEF["upādiṇṇ"],
      "upādiṇṇaṃ": F.DEF["upādiṇṇ"], "bāhiraṃ": f"{T['bāhirā']} ဖြစ်သော", "bahiddhā": T["bahiddhā"],
      "anupādinnaṃ": T["anupādiṇṇā"], "anupādiṇṇaṃ": T["anupādiṇṇā"]}
for _k, _v in {"kharigataṃ": P1.SYN["kharagataṃ"],
               "asamphuṭṭhaṃ maṃsalohitehi": "အသားနှင့် သွေးတို့နှင့် မထိတွေ့သောအရာ"}.items():
    new("Synonym lists (element definitions)", P1.SYN, _k, _v)
NEW.setdefault("Spelling of pi-1 list words (same Burmese as pi-1)", []).append(("kharigataṃ", "as pi-1 kharagataṃ"))
EXAMPLES = {   # seyyathidaṃ – … (one Pāli item = one Burmese item)
    # internal earth
    "kesā": "ဆံပင်", "lomā": "မွေးညင်း", "nakhā": "ခြေသည်းလက်သည်း", "dantā": "သွား", "taco": "အရေ",
    "maṃsaṃ": "အသား", "nhāru": "အကြော", "aṭṭhi": "အရိုး", "aṭṭhimiñjaṃ": "ရိုးတွင်းခြင်ဆီ", "vakkaṃ": "ကျောက်ကပ်",
    "hadayaṃ": "နှလုံး", "yakanaṃ": "အသည်း", "kilomakaṃ": "အမြှေး", "pihakaṃ": "သရက်ရွက်", "papphāsaṃ": "အဆုတ်",
    "antaṃ": "အူမ", "antaguṇaṃ": "အူသိမ်", "udariyaṃ": "အစာသစ်", "karīsaṃ": "အစာဟောင်း",
    # external earth
    "ayo": "သံ", "lohaṃ": "ကြေး", "tipu": "သံဖြူ", "sīsaṃ": "ခဲ", "sajjhaṃ": "ငွေဖြူ", "muttā": "ပုလဲ",
    "maṇi": "ကျောက်မျက်", "veḷuriyo": "ကြောင်မျက်ရွဲ", "saṅkho": "ခရုသင်း", "silā": "ကျောက်ဖျာ", "pavāḷaṃ": "သန္တာ",
    "rajataṃ": "ငွေ", "jātarūpaṃ": "ရွှေ", "lohitaṅko": "ပတ္တမြား", "masāragallaṃ": "မြ",
    "tiṇaṃ": "မြက်", "kaṭṭhaṃ": "ထင်း", "sakkharā": "ကျောက်စရစ်", "kaṭhalaṃ": "အိုးခြမ်းကွဲ", "bhūmi": "မြေ",
    "pāsāṇo": "ကျောက်တုံး", "pabbato": "တောင်",
    # internal water
    "pittaṃ": "သည်းခြေ", "semhaṃ": "သလိပ်", "pubbo": "ပြည်", "lohitaṃ": "သွေး", "sedo": "ချွေး", "medo": "အဆီခဲ",
    "assu": "မျက်ရည်", "vasā": "အဆီကြည်", "kheḷo": "တံတွေး", "siṅghāṇikā": "နှပ်", "lasikā": "အစေး",
    "muttaṃ": "ကျင်ငယ်",
    # external water (raso = sap here, not taste)
    "mūlaraso": "အမြစ် အရည်", "khandharaso": "ပင်စည် အရည်", "tacaraso": "အခေါက် အရည်", "pattaraso": "အရွက် အရည်",
    "puppharaso": "ပန်း အရည်", "phalaraso": "အသီး အရည်", "khīraṃ": "နို့", "dadhi": "နို့ချဉ်", "sappi": "ထောပတ်ဆီ",
    "navanītaṃ": "ထောပတ်", "telaṃ": "ဆီ", "madhu": "ပျားရည်", "phāṇitaṃ": "တင်လဲ",
    "bhummāni vā udakāni antalikkhāni vā": "မြေပေါ်ရှိ ရေဖြစ်စေ၊ ကောင်းကင်မှ ရေဖြစ်စေ",
    # internal fire
    "yena ca santappati": "အကြင်အရာဖြင့် ကိုယ် ပူနွေးခြင်း", "yena ca jīrīyati": "အကြင်အရာဖြင့် အိုမင်းခြင်း",
    "yena ca pariḍayhati": "အကြင်အရာဖြင့် ကိုယ် ပူလောင်ခြင်း",
    "yena ca asitapītakhāyitasāyitaṃ sammā pariṇāmaṃ gacchati":
        "အကြင်အရာဖြင့် စားထားသော၊ သောက်ထားသော၊ ခဲထားသော၊ လျက်ထားသော အစာ ကောင်းစွာ ကြေကျက်ခြင်း",
    # external fire
    "kaṭṭhaggi": "ထင်း မီး", "palālaggi": "ကောက်ရိုး မီး", "tiṇaggi": "မြက် မီး", "gomayaggi": "နွားချေး မီး",
    "thusaggi": "ဖွဲ မီး", "saṅkāraggi": "အမှိုက် မီး", "indaggi": "မိုးကြိုး မီး", "aggisantāpo": "မီး၏ အပူ",
    "sūriyasantāpo": "နေ၏ အပူ", "kaṭṭhasannicayasantāpo": "ထင်းပုံ၏ အပူ", "tiṇasannicayasantāpo": "မြက်ပုံ၏ အပူ",
    "dhaññasannicayasantāpo": "စပါးပုံ၏ အပူ", "bhaṇḍasannicayasantāpo": "ကုန်ပစ္စည်းပုံ၏ အပူ",
    # internal wind
    "uddhaṅgamā vātā": "အထက်သို့ တက်သော လေ", "adhogamā vātā": "အောက်သို့ ဆင်းသော လေ",
    "kucchisayā vātā": "ဝမ်းတွင်း၌ ရှိသော လေ", "koṭṭhāsayā vātā": "အူတွင်း၌ ရှိသော လေ",
    "aṅgamaṅgānusārino vātā": "ကိုယ်အင်္ဂါ အသီးသီးသို့ လှည့်လည်သွားသော လေ",
    "satthakavātā": "ဓားဖြင့် ထိုးသကဲ့သို့ ဖြစ်သော လေ", "khurakavātā": "သင်တုန်းဓားဖြင့် ရိတ်သကဲ့သို့ ဖြစ်သော လေ",
    "uppalakavātā": "ထိုးဖောက်သကဲ့သို့ ဖြစ်သော လေ", "assāso passāso iti vā": "ဝင်လေ ထွက်လေ ဟူ၍လည်း",
    # external wind
    "puratthimā vātā": "အရှေ့ လေ", "pacchimā vātā": "အနောက် လေ", "uttarā vātā": "မြောက် လေ",
    "dakkhiṇā vātā": "တောင် လေ", "sarajā vātā": "ဖုန်ပါသော လေ", "arajā vātā": "ဖုန်မပါသော လေ",
    "sītā vātā": "အေးသော လေ", "uṇhā vātā": "ပူသော လေ", "parittā vātā": "အားနည်းသော လေ",
    "adhimattā vātā": "ပြင်းထန်သော လေ", "kāḷavātā": "လေမည်း", "verambhavātā": "လေပွေ",
    "pakkhavātā": "အတောင်ခတ်ရာမှ ဖြစ်သော လေ", "supaṇṇavātā": "ဂဠုန် အတောင်ခတ်ရာမှ ဖြစ်သော လေ",
    "tālavaṇṭavātā": "ထန်းလက် ယပ်ဖြင့် ခတ်သော လေ", "vidhūpanavātā": "ယပ်တောင်ဖြင့် ခတ်သော လေ",
    # internal space
    "kaṇṇacchiddaṃ": "နားပေါက်", "nāsacchiddaṃ": "နှာခေါင်းပေါက်", "mukhadvāraṃ": "ခံတွင်းပေါက်",
    "yena ca asitapītakhāyitasāyitaṃ ajjhoharati":
        "အကြင်အရာဖြင့် စားထားသော၊ သောက်ထားသော၊ ခဲထားသော၊ လျက်ထားသော အစာကို မျိုချခြင်း",
    "yattha ca asitapītakhāyitasāyitaṃ santiṭṭhati":
        "အကြင်အရာ၌ စားထားသော၊ သောက်ထားသော၊ ခဲထားသော၊ လျက်ထားသော အစာ တည်နေခြင်း",
    "yena ca asitapītakhāyitasāyitaṃ adhobhāgaṃ nikkhamati":
        "အကြင်အရာဖြင့် စားထားသော၊ သောက်ထားသော၊ ခဲထားသော၊ လျက်ထားသော အစာ အောက်ဘက်သို့ ထွက်ခြင်း",
}
for _k, _v in EXAMPLES.items():
    NEW.setdefault("Examples of the elements (seyyathidaṃ – …)", []).append((_k, _v))
_seen = {}
for _k, _v in EXAMPLES.items():
    if _v in _seen:
        raise SystemExit(f"two examples share {_v}: {_seen[_v]} / {_k}")
    _seen[_v] = _k


def examples_my(text):
    text = re.sub(r"(\S+) (\[[^\]]+\]) (vātā)", r"\1 \3 \2", text)
    toks = re.findall(r"\[[^\]]*\]|[^\s\[,]+|,", text)
    out, i = [], 0
    while i < len(toks):
        t = toks[i]
        if t == ",":
            i += 1
            continue
        if t.startswith("["):
            out[-1] += " " + var_my(t)
            i += 1
            continue
        for k in range(9, 0, -1):
            ph = " ".join(toks[i:i + k])
            if len(toks[i:i + k]) == k and ph in EXAMPLES:
                out.append(EXAMPLES[ph])
                i += k
                break
        else:
            raise Miss("example: " + t)
    return f"{C} ".join(out)


def elem_desc(q1, syn, q2):
    """«Q1 SYN… Q2» of an element definition -> Burmese («… ဖြစ်၍ Q2 …»)."""
    a = f"{C} ".join(EQ[w] for w in q1.split()) if q1 else ""
    items = P1.items_my(P1.list_items(syn))
    b = f"{C} ".join(EQ[w] for w in q2.split())
    return (a + " " if a else "") + items + " ဖြစ်၍ " + b


EDEF = (r"Yaṃ (?P<q1>(?:ajjhattaṃ paccattaṃ|bāhiraṃ)) (?P<syn>.+?) (?P<q2>ajjhattaṃ upādiṇṇaṃ|bahiddhā anupādiṇṇaṃ)"
        r"(?:, seyyathidaṃ – (?P<ex>.+?))?, yaṃ vā panaññampi atthi (?P<o1>(?:ajjhattaṃ paccattaṃ|bāhiraṃ)) "
        r"(?P<osyn>.+?) (?P<o2>ajjhattaṃ upādiṇṇaṃ|bahiddhā anupādiṇṇaṃ) – (?P<v>.+)\.")
EDEF_SHORT = (r"Yaṃ (?P<q1>bāhiraṃ) (?P<syn>.+?) (?P<q2>bahiddhā anupādiṇṇaṃ) – (?P<v>.+)\.")


def _vucc(v):
    m = re.fullmatch(VUCC_Q, v)
    if not m:
        raise Miss("vuccati: " + v)
    return r_vuccati_q(m)


@sent(EDEF)
def s_elem(m):
    if (m["o1"], m["osyn"], m["o2"]) != (m["q1"], VAR_TOKEN.sub("", m["syn"]), m["q2"]):
        raise Miss("element definition: repeat differs")
    d = elem_desc(m["q1"], m["syn"], m["q2"])
    ex = f"{C} {SEYYATHIDAM} – {examples_my(m['ex'])}" if m["ex"] else ""
    d2 = elem_desc(m["o1"], m["osyn"], m["o2"]).removesuffix(" " + EQ[m["o2"].split()[-1]])
    other = d2 + f" {EQ[m['o2'].split()[-1]]} {VA_PANA} {ARA} {REL}လည်း"
    return f"{d} {ARA} {REL}{ex}{C} {other} – {_vucc(m['v'])}{END}"


@sent(EDEF_SHORT)
def s_elem_short(m):
    return f"{elem_desc(m['q1'], m['syn'], m['q2'])} {ARA} {REL} – {_vucc(m['v'])}{END}"


@sent(r"(?P<x>\w+dhātu)dvayaṃ – atthi ajjhattikā, atthi bāhirā\.")
def s_dvaya(m):
    e = name_my(m["x"])
    return f"{e} {NUMW['dvi']}{F.KIND} – {T['ajjhattikā']} {e} {F.HOTI}{C} {T['bāhirā']} {e} {F.HOTI}{END}"


@sent(r"Yā ca ajjhattikā (?P<x>\w+dhātu) yā ca bāhirā (?P=x), tadekajjhaṃ abhisaññūhitvā abhisaṅkhipitvā – (?P<v>.+)\.")
def s_both(m):
    e = name_my(m["x"])
    return (f"{T['ajjhattikā']} {e}လည်းကောင်း{C} {T['bāhirā']} {e}လည်းကောင်း {REL}{C} {F.SUMMARY_END} – "
            f"{_vucc(m['v'])}{END}")


@sent(r"(?:Imā|Ime) cha dhātuyo\.")
def s_ima(m):
    return f"ဤတို့သည် {count(DHATU, 'cha')} {COP[True]}{END}"


@sent(r"Iti imāni tīṇi chakkāni tadekajjhaṃ abhisaññūhitvā abhisaṅkhipitvā aṭṭhārasa dhātuyo honti\.")
def s_iti(m):
    return (f"ဤသို့ ဤ{DHATU} {NUMW['cha']}{CL}တွဲ {NUMW['ti']}စု{C} {F.SUMMARY_END} {count(DHATU, 'aṭṭhārasa')} "
            f"{COP[True]}{END}")


PATISAMYUTTA = "နှင့် စပ်ယှဉ်သော"                   # -paṭisaṃyutta (connected with)
PS = {"Kāma": "ကာမ", "Byāpāda": P1.JH_BYAPADA, "Vihiṃsā": "ညှဉ်းပန်းမှု", "Nekkhamma": "ကာမမှ ထွက်မြောက်ခြင်း",
      "Abyāpāda": P1.NAMES["abyāpādo"], "Avihiṃsā": "ညှဉ်းပန်းမှု မရှိခြင်း"}


@rule(r"(?P<x>Kāma|Byāpāda|Vihiṃsā|Nekkhamma|Abyāpāda|Avihiṃsā)paṭisaṃyutto (?P<l>takko .+?)(?= – )")
def r_patisam(m):
    return f"{PS[m['x']]}{PATISAMYUTTA} {P1.items_my(P1.list_items(m['l']))}"


KAMA_DEF = ("Heṭṭhato avīcinirayaṃ pariyantaṃ karitvā uparito paranimmitavasavattī deve anto karitvā yaṃ etasmiṃ "
            "antare etthāvacarā ettha pariyāpannā khandhadhātuāyatanā rūpā [rūpaṃ (syā.)] vedanā saññā saṅkhārā "
            "viññāṇaṃ")


@rule(re.escape(KAMA_DEF) + r"(?= – )")
def r_kama(m):
    return (f"အောက်ဘက်တွင် အဝီစိ ငရဲကို အဆုံး ပြု၍{C} အထက်ဘက်တွင် ပရနိမ္မိတဝသဝတ္တီ နတ်တို့ကို အတွင်း၌ ထည့်သွင်း၍ "
            f"ဤကြား၌ ကျင်လည်ကြသော{C} ဤကြား၌ အကျုံးဝင်ကြသော {F.KHANDHA}{C} {DHATU}{C} {AYAT}တို့{C} {F.RUPA} "
            f"{var_my('[rūpaṃ (syā.)]')}{C} {P1.FEEL}{C} {P1.SANNA}{C} {P1.SANKHARA}များ{C} {P1.VINNANA} {REL}")


@rule(r"Dasasu vā āghātavatthūsu (?P<l>cittassa āghāto .+?)(?= – )")
def r_aghata(m):
    return f"ရန်ငြိုးဖွဲ့ရာ အကြောင်း {NUMW['dasa']}{CL}တို့၌ဖြစ်စေ {P1.items_my(P1.list_items(m['l']))}"


for _k, _v in {"heṭhanā": "နှိပ်စက်ခြင်း", "viheṭhanā": "ညှဉ်းဆဲခြင်း", "hiṃsanā": "ထိခိုက်နာကျင်စေခြင်း",
               "vihiṃsanā": "ညှဉ်းပန်းခြင်း", "rosanā": "ဒေါသ ထွက်စေခြင်း", "virosanā": "အလွန် ဒေါသ ထွက်စေခြင်း",
               "parūpaghāto": "သူတစ်ပါးကို ထိပါးခြင်း",
               "mettācetovimutti": "မေတ္တာဖြင့် စိတ် လွတ်မြောက်ခြင်း", "karuṇā": "ကရုဏာ",
               "karuṇāyanā": "ကရုဏာ ထားခြင်း", "karuṇāyitattaṃ": "ကရုဏာ ထားသော အဖြစ်",
               "karuṇācetovimutti": "ကရုဏာဖြင့် စိတ် လွတ်မြောက်ခြင်း"}.items():
    new("Synonym lists (vihiṃsā, mettā, karuṇā)", P1.SYN, _k, _v)
IDHEKACCO = p1cut("Idhekacco paṭisanthārako hoti āmisapaṭisanthārena vā dhammapaṭisanthārena vā – ayaṃ vuccati "
                  "paṭisanthāro.", None, " ပစ္စည်းဖြင့်")            # ဤလောက၌ အချို့သော သူသည်


@rule(r"Idhekacco pāṇinā vā leḍḍunā vā daṇḍena vā satthena vā rajjuyā vā aññataraññatarena satte viheṭheti")
def r_idhekacco(m):
    return (f"{IDHEKACCO} လက်ဖြင့်ဖြစ်စေ{C} မြေစိုင်ခဲဖြင့်ဖြစ်စေ{C} တုတ်ဖြင့်ဖြစ်စေ{C} လက်နက်ဖြင့်ဖြစ်စေ{C} "
            f"ကြိုးဖြင့်ဖြစ်စေ{C} တစ်ခုခုသော အရာဖြင့် သတ္တဝါတို့ကို ညှဉ်းဆဲ၏")


@rule(r"yā evarūpā (?P<l>heṭhanā .+?)(?= – )")
def r_evarupa(m):
    return f"ဤသို့ သဘောရှိသော {P1.items_my(P1.list_items(m['l']))} {REL}"


@rule(r"Yā sattesu (?P<l>(?:metti|karuṇā) .+?)(?= – )")
def r_sattesu(m):
    return f"သတ္တဝါတို့အပေါ်၌ {P1.items_my(P1.list_items(m['l']))} {REL}"


@sent(r"Sabbepi kusalā dhammā \"(?P<x>[^\"]+)\"\.")
def s_sabbepi(m):
    return f"{T['kusalā']} {DH} အားလုံးသည်လည်း “{name_my(m['x'])}” {COP[True]}{END}"


# the citta list «cittaṃ mano mānasaṃ … tajjā-X» (pi-1 ^1-6) and the arising clauses of the abhidhamma part
for _s in ("cakkhu", "sota", "ghāna", "jivhā", "kāya"):
    new("Synonym lists (citta)", P1.SYN, f"tajjā{_s}viññāṇadhātu", f"သက်ဆိုင်ရာ {NM[_s + 'viññāṇadhātu']}")
new("Synonym lists (citta)", P1.SYN, "tajjāmanodhātu", f"သက်ဆိုင်ရာ {NM['manodhātu']}")
assert P1.SYN["tajjāmanoviññāṇadhātu"] == f"သက်ဆိုင်ရာ {NM['manoviññāṇadhātu']}"
CITTA_L = r"cittaṃ mano mānasaṃ(?: hadayaṃ paṇḍaraṃ mano manāyatanaṃ manindriyaṃ viññāṇaṃ viññāṇakkhandho|…pe…) tajjā\w+"
UPPAJJATI = "ဖြစ်ပေါ်သည်"
NIRUDDHA = "ဖြစ်ပေါ်ပြီး ချုပ်ပြီးသည့် အခြားမဲ့၌"     # uppajjitvā niruddhasamanantarā (right after … arose and ceased)
PATICCA2 = "ကို မှီ၍"


def citta_l(s):
    return P1.items_my(P1.list_items(s))


@rule(r"(?P<a>\w+?)ñca paṭicca (?P<b>\w+?) ca uppajjati (?P<l>" + CITTA_L + ")")
def r_paticca(m):
    a = {"Cakkhu": "cakkhu", "Sota": "sota", "Ghāna": "ghāna", "Jivha": "jivhā", "Kāya": "kāya", "mana": "mano"}[m["a"]]
    am = C3["SENSE"].get(a, P1.MANO)
    b = {"rūpe": C3["OBJECT"]["rūpa"], "sadde": C3["OBJECT"]["sadda"], "gandhe": C3["OBJECT"]["gandha"],
         "rase": C3["OBJECT"]["rasa"], "phoṭṭhabbe": C3["OBJECT"]["phoṭṭhabba"], "dhamme": DH}[m["b"]]
    return f"{am}ကိုလည်းကောင်း{C} {b}တို့ကိုလည်းကောင်း မှီ၍ {citta_l(m['l'])} {UPPAJJATI}"


DHATUYA = r"(?P<d>[Cc]akkhuviññāṇadhātuyā|sotaviññāṇadhātuyā|ghānaviññāṇadhātuyā|jivhāviññāṇadhātuyā|" \
          r"kāyaviññāṇadhātuyā|manodhātuyā)"


def _dh(d):
    return NM[d[0].lower() + d[1:-2]]                  # X-dhātuyā -> X-dhātu


@rule(DHATUYA + r"(?P<pi>pi)? uppajjitvā niruddhasamanantarā uppajjati (?P<l>manodhātu|" + CITTA_L + ")")
def r_niruddha(m):
    l = NM["manodhātu"] if m["l"] == "manodhātu" else citta_l(m["l"])
    pi = "လည်း" if m["pi"] else ""
    return f"{_dh(m['d'])}{pi} {NIRUDDHA} {l} {UPPAJJATI}"


@rule(DHATUYA + r"(?= ?…pe…)")
def r_dhatuya_pe(m):
    return _dh(m["d"])


@rule(r"sabbadhammesu vā pana paṭhamasamannāhāro uppajjati (?P<l>" + CITTA_L + ")")
def r_samannahara(m):
    return f"{F.VA_OR} {DH} အားလုံးတို့၌ ပထမ နှလုံးသွင်းခြင်း ဖြစ်သော {citta_l(m['l'])} {UPPAJJATI}"


SLIPS.update({
    # 3-dhatuvibhango
    "atthi hetu, atthi ahetu.": "atthi hetu, atthi na hetu.",
    '"parāmāsā ceva parāmaṭṭhā cāti parāmaṭṭhā ceva no ca parāmāsā".':
        '"parāmāsā ceva parāmaṭṭhā cā"ti, "parāmaṭṭhā ceva no ca parāmāsā".',
})


# ===================================================================================== chapter 4: sacca
LOBHA = p1("Yo rāgo sārāgo anunayo anurodho nandī nandīrāgo [nandirāgo (sī.)] cittassa sārāgo icchā mucchā ajjhosānaṃ "
           "gedho paligedho saṅgo paṅko ejā māyā janikā sañjananī sibbinī [sibbanī (sī.)] jālinī saritā visattikā "
           "suttaṃ visaṭā āyūhinī [āyūhanī (sī. syā.)] dutiyā paṇidhi bhavanetti vanaṃ vanatho santhavo sineho apekkhā "
           "paṭibandhu āsā āsisanā āsisitattaṃ [āsiṃsanā āsiṃsitattaṃ (sī. syā.)] rūpāsā saddāsā gandhāsā rasāsā "
           "phoṭṭhabbāsā lābhāsā dhanāsā puttāsā jīvitāsā jappā pajappā abhijappā jappā jappanā jappitattaṃ loluppaṃ "
           "loluppāyanā loluppāyitattaṃ pucchañjikatā [puñcikatā (syā.) pucchikatā (sī.)] sādhukamyatā adhammarāgo "
           "visamalobho nikanti nikāmanā patthanā pihanā sampatthanā kāmataṇhā bhavataṇhā vibhavataṇhā rūpataṇhā "
           "arūpataṇhā nirodhataṇhā rūpataṇhā saddataṇhā gandhataṇhā rasataṇhā phoṭṭhabbataṇhā dhammataṇhā ogho yogo "
           "gantho upādānaṃ āvaraṇaṃ nīvaraṇaṃ chādanaṃ bandhanaṃ upakkileso anusayo pariyuṭṭhānaṃ latā vevicchaṃ "
           "dukkhamūlaṃ dukkhanidānaṃ dukkhappabhavo mārapāso mārabaḷisaṃ māravisayo taṇhānadī taṇhājālaṃ "
           "taṇhāgaddulaṃ taṇhāsamuddo abhijjhā lobho akusalamūlaṃ – ayaṃ vuccati lobho.")
TANHA = "တပ်မက်မှု"                                     # taṇhā (pi-1 termbase)
OBJ6 = {"rūpa": C3["OBJECT"]["rūpa"], "sadda": C3["OBJECT"]["sadda"], "gandha": C3["OBJECT"]["gandha"],
        "rasa": C3["OBJECT"]["rasa"], "phoṭṭhabba": C3["OBJECT"]["phoṭṭhabba"], "dhamma": DH}
P1TANHA = {"kāmataṇhā": f"ကာမကို {TANHA}", "bhavataṇhā": f"ဘဝကို {TANHA}",
           "vibhavataṇhā": f"ဘဝ ပျောက်ကွယ်ခြင်းကို {TANHA}", "nandīrāgo": "နှစ်သက်မှု ရာဂ",
           "abhijjhā": "သူ့ဥစ္စာကို လိုချင်ခြင်း"}
for _o, _m in OBJ6.items():
    P1TANHA[_o + "taṇhā"] = f"{_m}ကို {TANHA}"
for _k, _v in P1TANHA.items():
    assert _v in LOBHA, _k
NAMES4 = {
    "dukkhaṃ ariyasaccaṃ": f"{DUKKHA_T} {ARIYA} {SACCA}",
    "dukkhasamudayaṃ ariyasaccaṃ": f"{DUKKHA_T} {SAMUDAYA} {ARIYA} {SACCA}",
    "dukkhanirodhaṃ ariyasaccaṃ": f"{DUKKHA_T} {NIRODHA} {ARIYA} {SACCA}",
    "dukkhanirodhagāminī paṭipadā ariyasaccaṃ": f"{DUKKHA_T} {GAMINI} {PATIPADA} {ARIYA} {SACCA}",
    "dukkhasamudayo": f"{DUKKHA_T} {SAMUDAYA}", "dukkhanirodho": f"{DUKKHA_T} {NIRODHA}",
    "dukkhanirodhagāminī paṭipadā": f"{DUKKHA_T} {GAMINI} {PATIPADA}",
    "dukkhasaccaṃ": f"{DUKKHA_T} {SACCA}", "samudayasaccaṃ": f"{SAMUDAYA} {SACCA}",
    "nirodhasaccaṃ": f"{NIRODHA} {SACCA}", "maggasaccaṃ": f"{MAGGA} {SACCA}",
    "jāti": "မွေးဖွားခြင်း", "jarā": P1.SYN["jarā"], "maraṇaṃ": "သေခြင်း", "soko": "စိုးရိမ်ခြင်း",
    "paridevo": "ငိုကြွေးခြင်း", "domanassaṃ": "စိတ်ဆင်းရဲမှု", "upāyāso": "ပြင်းစွာ ပူပန်ခြင်း",
    "taṇhā": TANHA,
    "appiyehi sampayogo dukkho": f"မချစ်သော အရာတို့နှင့် ပေါင်းဆုံရခြင်းသည် {DUKKHA_T}",
    "piyehi vippayogo dukkho": f"ချစ်သော အရာတို့နှင့် ကွေကွင်းရခြင်းသည် {DUKKHA_T}",
    "yampicchaṃ na labhati tampi dukkhaṃ": f"အလိုရှိသည်ကို မရခြင်း၊ ထိုသည်လည်း {DUKKHA_T}",
    "saṃkhittena pañcupādānakkhandhā dukkhā": f"အကျဉ်းအားဖြင့် စွဲလမ်းမှု၏ အာရုံ ဖြစ်သော {count(F.KHANDHA, 'pañca')}"
                                              f"တို့သည် {DUKKHA_T}",
    "sammāvācā": P1.SYN.get("sammāvācā") or "မှန်ကန်သော စကား", "sammākammanto": "မှန်ကန်သော အလုပ်",
    "sammāājīvo": "မှန်ကန်သော အသက်မွေးမှု",
}
_P1DEP = p1("Avijjāpaccayā saṅkhārā, saṅkhārapaccayā viññāṇaṃ, viññāṇapaccayā nāmarūpaṃ, nāmarūpapaccayā saḷāyatanaṃ, "
            "saḷāyatanapaccayā phasso, phassapaccayā vedanā, vedanāpaccayā taṇhā, taṇhāpaccayā upādānaṃ, "
            "upādānapaccayā bhavo, bhavapaccayā jāti, jātipaccayā jarāmaraṇaṃ sokaparidevadukkhadomanassupāyāsā "
            "sambhavanti; evametassa kevalassa dukkhakkhandhassa samudayo hotīti.")
SOKA5 = _P1DEP[_P1DEP.index("စိုးရိမ်ခြင်း"):_P1DEP.index("တို့ ဖြစ်ပေါ်ကြသည်")]
for _k in ("jāti", "maraṇaṃ", "soko", "paridevo", "upāyāso", "taṇhā", "jarā"):
    assert NAMES4[_k] in _P1DEP, _k
for _k in ("sammāvācā", "sammākammanto", "sammāājīvo"):
    assert NAMES4[_k] in p1("Yasmiṃ samaye lokuttaraṃ jhānaṃ bhāveti niyyānikaṃ apacayagāmiṃ diṭṭhigatānaṃ pahānāya "
                            "paṭhamāya bhūmiyā pattiyā vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja viharati "
                            "dukkhapaṭipadaṃ dandhābhiññaṃ, tasmiṃ samaye phasso hoti, vedanā hoti, saññā hoti, cetanā "
                            "hoti, cittaṃ hoti, vitakko hoti, vicāro hoti, pīti hoti, sukhaṃ hoti, cittassekaggatā "
                            "hoti, saddhindriyaṃ hoti, vīriyindriyaṃ hoti, satindriyaṃ hoti, samādhindriyaṃ hoti, "
                            "paññindriyaṃ hoti, manindriyaṃ hoti, somanassindriyaṃ hoti, jīvitindriyaṃ hoti, "
                            "anaññātaññassāmītindriyaṃ hoti, sammādiṭṭhi hoti, sammāsaṅkappo hoti, sammāvācā hoti, "
                            "sammākammanto hoti, sammāājīvo hoti, sammāvāyāmo hoti, sammāsati hoti, sammāsamādhi hoti, "
                            "saddhābalaṃ hoti, vīriyabalaṃ hoti, satibalaṃ hoti, samādhibalaṃ hoti, paññābalaṃ hoti, "
                            "hiribalaṃ hoti, ottappabalaṃ hoti, alobho hoti, adoso hoti, amoho hoti, anabhijjhā hoti, "
                            "abyāpādo hoti, sammādiṭṭhi hoti, hirī hoti, ottappaṃ hoti, kāyapassaddhi hoti, "
                            "cittapassaddhi hoti, kāyalahutā hoti, cittalahutā hoti, kāyamudutā hoti, cittamudutā hoti, "
                            "kāyakammaññatā hoti, cittakammaññatā hoti, kāyapāguññatā hoti, cittapāguññatā hoti, "
                            "kāyujukatā hoti, cittujukatā hoti, sati hoti, sampajaññaṃ hoti, samatho hoti, vipassanā "
                            "hoti, paggāho hoti, avikkhepo hoti; ye vā pana tasmiṃ samaye aññepi atthi "
                            "paṭiccasamuppannā arūpino dhammā – ime dhammā kusalā."), _k
for _k in ("sammādiṭṭhi", "sammāsaṅkappo", "sammāvāyāmo", "sammāsati", "sammāsamādhi"):
    NAMES4[_k] = P1.NAMES[_k]
UPK = "စွဲလမ်းမှု၏ အာရုံ ဖြစ်သော"                      # -upādānakkhandha (aggregate as object of clinging)
for _p, _k in (("rūpupādānakkhandho", "rūpakkhandho"), ("vedanupādānakkhandho", "vedanākkhandho"),
               ("saññupādānakkhandho", "saññākkhandho"), ("saṅkhārupādānakkhandho", "saṅkhārakkhandho"),
               ("viññāṇupādānakkhandho", "viññāṇakkhandho")):
    NAMES4[_p] = f"{UPK} {NM[_k]}"
BODILY_DUKKHA = "ကိုယ်ဆင်းရဲခြင်း"                        # dukkha in «sokaparidevadukkhadomanassupāyāsā» (pi-1)
assert BODILY_DUKKHA in SOKA5
for _k, _v in NAMES4.items():
    new("Names (truths, suffering)", NM, _k, _v)
    F.ITEM.setdefault(_k, _v)
COUNT_HEAD.update({"Cattāri ariyasaccāni": f"{ARIYA} {count(SACCA, 'catu')}", "Cattāri saccāni": count(SACCA, "catu")})
COUNT_AMONG["Catunnaṃ ariyasaccānaṃ"] = f"{ARIYA} {count(SACCA, 'catu')}တို့အနက်"
for _k in ("Dukkhasaccaṃ", "Samudayasaccaṃ", "Nirodhasaccaṃ", "Maggasaccaṃ"):
    new("Headings and colophons", F.HEAD, _k, NM[_k.lower()])
for _p in ("samudayasaccaṃ", "maggasaccaṃ", "nirodhasaccaṃ", "dukkhasaccaṃ"):
    F.KH[_p] = (NM[_p], None, False)
for _p, _n in (("dve saccā", "dvi"), ("tīṇi saccāni", "ti")):
    new("Subjects (pañhāpucchaka)", F.KH, _p, (count(SACCA, _n), None, True))
F.TERM_IRREG.setdefault("araṇanti", "araṇā")
P1.NAMES.setdefault("aṭṭhaṅgiko maggo", f"{P1.count_my(P1._ANGA, 'aṭṭha')} ရှိသော {MAGGA}")
assert P1.NAMES["aṭṭhaṅgiko maggo"] in p1("Tasmiṃ kho pana samaye cattāro khandhā honti, dvāyatanāni honti, dve dhātuyo "
    "honti, tayo āhārā honti, navindriyāni honti, pañcaṅgikaṃ jhānaṃ hoti, aṭṭhaṅgiko maggo hoti, satta balāni honti, "
    "tayo hetū honti, eko phasso hoti, ekā vedanā hoti, ekā saññā hoti, ekā cetanā hoti, ekaṃ cittaṃ hoti, eko "
    "vedanākkhandho hoti, eko saññākkhandho hoti, eko saṅkhārakkhandho hoti, eko viññāṇakkhandho hoti, ekaṃ "
    "manāyatanaṃ hoti, ekaṃ manindriyaṃ hoti, ekā manoviññāṇadhātu hoti, ekaṃ dhammāyatanaṃ hoti, ekā dhammadhātu "
    "hoti; ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā – ime dhammā kusalā…pe….")
VKIND.update({"dukkhasamudayo": P1.LEKHANA, "dukkhanirodho": P1.LEKHANA, "lālapo lālapanā lālapitattaṃ": P1.LEKHANA,
              "ponobbhavikā": P1.LEKHANA, "veramaṇi": P1.LEKHANA, "viriyārambho": P1.LEKHANA})


def name_list(text):
    """«A, B [v], C …» -> «A၊ B [v]၊ C …» (a variant inside a name goes after the name)."""
    out = []
    for it in text.split(", "):
        vs = VAR_TOKEN.findall(it)
        base = VAR_TOKEN.sub("", it)
        out.append(name_my(base) + "".join(" " + var_my(v.strip()) for v in vs))
    return f"{C} ".join(out)


@rule(r"(?P<h>Cattāri ariyasaccāni|Cattāri saccāni) – (?P<l>.+?)(?=\.$)")
def r_truths(m):
    return f"{COUNT_HEAD[m['h']]} – {name_list(m['l'])}"


_old_name_my = name_my


def name_my(x):                                        # noqa: F811  (context: dukkha in the suttanta definitions)
    if x == "dukkhaṃ":
        return BODILY_DUKKHA if STATE.get("part") == "sut" else DUKKHA_T
    return _old_name_my(x)


# ---- dukkhasacca (suttanta)
PI_X = {"Jātipi": NM["jāti"], "jarāpi": NM["jarā"], "maraṇampi": NM["maraṇaṃ"]}


@sent(r"Jātipi dukkhā, jarāpi dukkhā, maraṇampi dukkhaṃ, sokaparidevadukkhadomanassupāyāsāpi dukkhā, appiyehi sampayogo "
      r"dukkho, piyehi vippayogo dukkho, yaṃ picchaṃ na labhati tampi dukkhaṃ, saṃkhittena pañcupādānakkhandhā "
      r"dukkhā\.")
def s_dukkha(m):
    d = f"{DUKKHA_T} {COP[False]}"
    dp = f"{DUKKHA_T} {COP[True]}"
    parts = [f"{NM['jāti']}သည်လည်း {d}", f"{NM['jarā']}သည်လည်း {d}", f"{NM['maraṇaṃ']}သည်လည်း {d}",
             f"{SOKA5}တို့သည်လည်း {dp}", f"မချစ်သော အရာတို့နှင့် ပေါင်းဆုံရခြင်းသည် {d}",
             f"ချစ်သော အရာတို့နှင့် ကွေကွင်းရခြင်းသည် {d}", f"အလိုရှိသည်ကို မရခြင်း၊ ထိုသည်လည်း {d}",
             f"အကျဉ်းအားဖြင့် စွဲလမ်းမှု၏ အာရုံ ဖြစ်သော {count(F.KHANDHA, 'pañca')}တို့သည် {dp}"]
    return f"{C} ".join(parts) + END


GEN4 = {"tesaṃ tesaṃ sattānaṃ tamhi tamhi sattanikāye": "ထိုထို သတ္တဝါတို့၏ ထိုထို သတ္တဝါ အပေါင်း၌",
        "tesaṃ tesaṃ sattānaṃ tamhā tamhā sattanikāyā": "ထိုထို သတ္တဝါတို့၏ ထိုထို သတ္တဝါ အပေါင်းမှ"}
assert GEN4["tesaṃ tesaṃ sattānaṃ tamhi tamhi sattanikāye"].startswith(F.YE_GEN["tesaṃ tesaṃ sattānaṃ"])
_rx = p1("Yā rūpassa jarā jīraṇatā khaṇḍiccaṃ pāliccaṃ valittacatā āyuno saṃhāni indriyānaṃ paripāko – idaṃ taṃ "
         "rūpaṃ rūpassa jaratā.")
SYN4 = {
    # jāti
    "jāti": NM["jāti"], "sañjāti": "ကောင်းစွာ မွေးဖွားခြင်း", "okkanti": "သက်ဆင်းခြင်း", "abhinibbatti": "ထင်ရှား ဖြစ်ခြင်း",
    "khandhānaṃ pātubhāvo": f"{F.KHANDHA}တို့ ပေါ်ထွက်ခြင်း", "āyatanānaṃ paṭilābho": f"{AYAT}တို့ကို ရရှိခြင်း",
    # maraṇa
    "cuti": "စုတေခြင်း", "cavanatā": "ရွေ့လျောခြင်း", "maccu": "သေမင်း", "maraṇaṃ": NM["maraṇaṃ"],
    "kālakiriyā": "ကွယ်လွန်ခြင်း", "khandhānaṃ bhedo": f"{F.KHANDHA}တို့၏ {P1.SYN['bhedo']}",
    "kaḷevarassa nikkhepo": "ကိုယ်ခန္ဓာကို စွန့်ပစ်ခြင်း", "jīvitindriyassupacchedo": f"{P1.NAMES['jīvitindriyaṃ']} ပြတ်စဲခြင်း",
    # soka
    "soko": NM["soko"], "socanā": "စိုးရိမ်နေခြင်း", "socitattaṃ": "စိုးရိမ်ထားသော အဖြစ်", "antosoko": "အတွင်း စိုးရိမ်ခြင်း",
    "antoparisoko": "အတွင်း၌ အလွန် စိုးရိမ်ခြင်း", "cetaso parijjhāyanā": "စိတ်၏ လောင်မြိုက်ခြင်း",
    "domanassaṃ": NM["domanassaṃ"], "sokasallaṃ": "စိုးရိမ်ခြင်းဟူသော ငြောင့်",
    # parideva
    "ādevo": "ငိုခြင်း", "paridevo": NM["paridevo"], "ādevanā": "ငိုနေခြင်း", "paridevanā": "ငိုကြွေးနေခြင်း",
    "ādevitattaṃ": "ငိုထားသော အဖြစ်", "paridevitattaṃ": "ငိုကြွေးထားသော အဖြစ်", "vācā": C3["VACA"],
    "palāpo": "ပေါက်ကရ ပြောခြင်း", "vippalāpo": "ကမောက်ကမ ပြောခြင်း", "lālappo": "မြည်တမ်းခြင်း",
    "lālappanā": "မြည်တမ်းနေခြင်း", "lālappitattaṃ": "မြည်တမ်းထားသော အဖြစ်",
    # upāyāsa
    "āyāso": "ပူပန်ခြင်း", "upāyāso": NM["upāyāso"], "āyāsitattaṃ": "ပူပန်ထားသော အဖြစ်",
    "upāyāsitattaṃ": "ပြင်းစွာ ပူပန်ထားသော အဖြစ်",
    # nirodha
    "asesavirāganirodho": "အကြွင်း မရှိ ကင်းပြတ်ချုပ်ငြိမ်းခြင်း", "cāgo": "စွန့်လွှတ်ခြင်း", "paṭinissaggo": "စွန့်ပစ်ခြင်း",
    "mutti": "လွတ်မြောက်ခြင်း", "anālayo": "မတွယ်တာခြင်း",
    # appiya / piya
    "saṅgati": "ဆုံတွေ့ခြင်း", "samāgamo": "ပေါင်းဆုံခြင်း", "samodhānaṃ": "စုဝေးခြင်း", "missībhāvo": "ရောနှောခြင်း",
    "asaṅgati": "မဆုံတွေ့ခြင်း", "asamāgamo": "မပေါင်းဆုံခြင်း", "asamodhānaṃ": "မစုဝေးခြင်း", "amissībhāvo": "မရောနှောခြင်း",
}
for _k, _v in SYN4.items():
    if _k in ("jarā",):
        continue
    new("Synonym lists (truths)", P1.SYN, _k, _v)
JARA_L = "jarā jīraṇatā khaṇḍiccaṃ pāliccaṃ valittacatā āyuno saṃhāni indriyānaṃ paripāko"
for _w in ("jīraṇatā", "khaṇḍiccaṃ", "pāliccaṃ", "valittacatā", "āyuno saṃhāni"):
    assert P1.SYN[_w] in _rx
P1.SYN["indriyānaṃ paripāko"] = _rx.split("ရှိသမျှ")[0].split(f"{C} ")[-1].strip()      # pi-1 final (rails)
assert P1.SYN["indriyānaṃ paripāko"] == "အာရုံခံ အင်္ဂါတို့ ရင့်ရော်ခြင်း"


@rule(r"Yā (?P<g>tesaṃ tesaṃ sattānaṃ (?:tamhi tamhi sattanikāye|tamhā tamhā sattanikāyā)) (?P<l>.+?)(?= – )")
def r_jati(m):
    return f"{GEN4[m['g']]} {P1.items_my(P1.list_items(m['l']))} {REL}"


BYASANA = {"ñāti": "ဆွေမျိုး", "bhoga": "စည်းစိမ်", "roga": "ကျန်းမာရေး", "sīla": "သီလ", "diṭṭhi": "အယူ"}
PHUTTHA = "နှင့် တွေ့ကြုံရသူ၏"                           # (X-byasanena) phuṭṭhassa (afflicted by …)
BY_HEAD = (r"Ñātibyasanena vā phuṭṭhassa bhogabyasanena vā phuṭṭhassa rogabyasanena vā phuṭṭhassa sīlabyasanena vā "
           r"phuṭṭhassa diṭṭhibyasanena vā phuṭṭhassa aññataraññatarena byasanena samannāgatassa aññataraññatarena "
           r"dukkhadhammena phuṭṭhassa")
BY_HEAD_MY = (f"{C} ".join(f"{v} ပျက်စီးခြင်းနှင့်ဖြစ်စေ တွေ့ကြုံရသူ၏" for v in BYASANA.values())
              + f"{C} တစ်ခုခုသော ပျက်စီးခြင်းနှင့် ပြည့်စုံသူ၏{C} တစ်ခုခုသော ဆင်းရဲဖွယ် အကြောင်းနှင့် တွေ့ကြုံရသူ၏")


@rule(BY_HEAD + r" (?P<l>.+?)(?= – )")
def r_byasana(m):
    return f"{BY_HEAD_MY} {P1.items_my(P1.list_items(m['l']))}"


IDHA = p1cut("Saṃviggassa ca yoniso padhānanti – idha bhikkhu anuppannānaṃ pāpakānaṃ akusalānaṃ dhammānaṃ anuppādāya "
             "chandaṃ janeti vāyamati vīriyaṃ ārabhati cittaṃ paggaṇhāti padahati, uppannānaṃ pāpakānaṃ akusalānaṃ "
             "dhammānaṃ pahānāya chandaṃ janeti vāyamati vīriyaṃ ārabhati cittaṃ paggaṇhāti padahati, anuppannānaṃ "
             "kusalānaṃ dhammānaṃ uppādāya chandaṃ janeti vāyamati vīriyaṃ ārabhati cittaṃ paggaṇhāti padahati, "
             "uppannānaṃ kusalānaṃ dhammānaṃ ṭhitiyā asammosāya bhiyyobhāvāya vepullāya bhāvanāya pāripūriyā chandaṃ "
             "janeti vāyamati vīriyaṃ ārabhati cittaṃ paggaṇhāti padahati.", "ဤသာသနာ၌", None)
IDHA_HEAD = IDHA.split(" ရဟန်းသည်")[0]                  # ဤသာသနာ၌ (idha, of a monk / disciple)
IDHA_LOKA = IDHEKACCO.split(" ")[0]                     # ဤလောက၌ (idha, of anyone: pi-1 Idhekacco)
assert IDHA_LOKA == "ဤလောက၌"
BHIKKHU = "ရဟန်းသည်"                                    # bhikkhu (subject)
PADHANA4 = IDHA[len(IDHA_HEAD + " " + BHIKKHU) + 1:].removesuffix(END).split("ကြိုးပမ်း၏၊ ")
PADHANA4 = [x if x.endswith("ကြိုးပမ်း၏") else x + "ကြိုးပမ်း၏" for x in PADHANA4]
assert len(PADHANA4) == 4
PADHANA_PI = ["anuppannānaṃ pāpakānaṃ akusalānaṃ dhammānaṃ anuppādāya", "uppannānaṃ pāpakānaṃ akusalānaṃ dhammānaṃ pahānāya",
              "anuppannānaṃ kusalānaṃ dhammānaṃ uppādāya",
              "uppannānaṃ kusalānaṃ dhammānaṃ ṭhitiyā asammosāya bhiyyobhāvāya vepullāya bhāvanāya pāripūriyā"]
PAD_TAIL = "chandaṃ janeti, vāyamati, vīriyaṃ ārabhati, cittaṃ paggaṇhāti, padahati"


@sent(r"(?P<i>Idha bhikkhu )?(?P<x>[Aa]nuppannānaṃ .+?|[Uu]ppannānaṃ .+?) " + re.escape(PAD_TAIL) + r"\.")
def s_padhana(m):
    x = m["x"][0].lower() + m["x"][1:]
    if x not in PADHANA_PI:
        raise Miss("padhāna: " + x)
    body = PADHANA4[PADHANA_PI.index(x)]
    return (f"{IDHA_HEAD} {BHIKKHU} " if m["i"] else "") + body + END


# ---- samudaya / nirodha (suttanta)
PIYARUPA = "ချစ်ဖွယ် သဘော ရှိသော"                         # piyarūpa
SATARUPA = f"{P1._SATA}သော သဘော ရှိသော"                  # sātarūpa (sāta = pi-1 «နှစ်သက်ဖွယ်ကောင်း»)
LOKE = "လောက၌"
PS_THING = f"{PIYARUPA}{C} {SATARUPA} အရာ"
ARISE = {"uppajjamānā uppajjati": ("ဖြစ်ပေါ်လျှင်", "ဖြစ်ပေါ်သည်"), "nivisamānā nivisati": ("တည်လျှင်", "တည်သည်"),
         "pahīyamānā pahīyati": ("ပျောက်ကင်းလျှင်", "ပျောက်ကင်းသည်"),
         "nirujjhamānā nirujjhati": ("ချုပ်ငြိမ်းလျှင်", "ချုပ်ငြိမ်းသည်")}
ARISE_Q = {k: (a, b.removesuffix("သည်") + "သနည်း") for k, (a, b) in ARISE.items()}
TAN_THIS = f"ဤ{TANHA}သည်"


@sent(r"Yāyaṃ taṇhā ponobhavikā (?P<v>\[[^\]]+\]) nandirāgasahagatā tatratatrābhinandinī, seyyathidaṃ – kāmataṇhā, "
      r"bhavataṇhā, vibhavataṇhā\.")
def s_tanha(m):
    return (f"ဘဝသစ်ကို ဖြစ်စေတတ်သော {var_my(m['v'])}{C} {P1TANHA['nandīrāgo']}နှင့်အတူ ဖြစ်သော{C} ထိုထို ဘဝ၌ အလွန် "
            f"နှစ်သက်တတ်သော {TANHA} {REL}{C} {SEYYATHIDAM} – {P1TANHA['kāmataṇhā']}{C} {P1TANHA['bhavataṇhā']}{C} "
            f"{P1TANHA['vibhavataṇhā']}{END}")


@sent(r"Sā kho panesā taṇhā kattha (?P<a>\w+ \w+), kattha (?P<b>\w+ \w+)\?")
def s_kattha(m):
    a, b = ARISE_Q[m["a"]], ARISE_Q[m["b"]]
    return f"ထို{TANHA}သည် အဘယ်၌ {a[0]} {a[1]}{C} အဘယ်၌ {b[0]} {b[1]}{END}"


def _ettha(a, b, esa=True):
    a, b = ARISE[a], ARISE[b]
    return f"ဤအရာ၌ {TAN_THIS} {a[0]} {a[1]}{C} ဤအရာ၌ {b[0]} {b[1]}"


@sent(r"Yaṃ loke piyarūpaṃ sātarūpaṃ, etthesā taṇhā (?P<a>\w+ \w+), ettha (?P<b>\w+ \w+)\.")
def s_yam_loke(m):
    return f"{LOKE} {PS_THING} {REL}{C} {_ettha(m['a'], m['b'])}{END}"


@sent(r"Etthesā taṇhā (?P<a>\w+ \w+), ettha (?P<b>\w+ \w+)\.")
def s_ettha(m):
    return _ettha(m["a"], m["b"]) + END


@sent(r"Kiñca loke piyarūpaṃ sātarūpaṃ\?")
def s_kinca(m):
    return f"{LOKE} {PS_THING} {QUESTION}{END}"


SIX = {}
for _s, _p in (("cakkhu", "Cakkhuṃ"), ("sota", "sotaṃ"), ("ghāna", "ghānaṃ"), ("jivhā", "jivhā"), ("kāya", "kāyo")):
    SIX[_p.lower()] = C3["SENSE"][_s]
    SIX[_s + "viññāṇaṃ"] = f"{C3['SENSE'][_s]} {P1.VINNANA}"
    SIX[_s + "samphasso"] = f"{C3['SENSE'][_s]}၏ {P1.PHASSA}"
    SIX[_s + "samphassajā vedanā"] = F.ITEM[_s + "samphassajā vedanā"]
SIX["mano"] = P1.MANO
SIX["manoviññāṇaṃ"] = f"{P1.MANO} {P1.VINNANA}"
SIX["manosamphasso"] = f"{P1.MANO}၏ {P1.PHASSA}"
SIX["manosamphassajā vedanā"] = F.ITEM["manosamphassajā vedanā"]
for _o, _m in OBJ6.items():
    SIX[_o[:-1] + "ā"] = _m
    SIX[_o + "saññā"] = f"{_m}ကို {P1.SANNA}"
    SIX[_o + "sañcetanā"] = f"{_m}ကို {P1.CETANA}"
    SIX[_o + "taṇhā"] = P1TANHA[_o + "taṇhā"]
    SIX[_o + "vitakko"] = f"{_m}ကို {P1.VIT}"
    SIX[_o + "vicāro"] = f"{_m}ကို {P1.VIC}"
for _k, _v in SIX.items():
    NEW.setdefault("The sixty items «X loke piyarūpaṃ sātarūpaṃ»", []).append((_k, _v))
SIX_ALT = "(?:" + "|".join(f"[{k[0].upper()}{k[0]}]" + re.escape(k[1:]) for k in sorted(SIX, key=len, reverse=True)) + ")"
PLURAL6 = {"rūpā", "saddā", "gandhā", "rasā", "phoṭṭhabbā", "dhammā"}


def _six(x):
    k = x[0].lower() + x[1:]
    return SIX[k] + ("တို့သည်" if k in PLURAL6 else "သည်")


@rule(r"(?P<x>" + SIX_ALT + r") loke piyarūpaṃ sātarūpaṃ(?=\.)")
def r_six_full(m):
    return f"{_six(m['x'])} {LOKE} {PS_THING} {COP[False]}"


@rule(r"(?P<x>" + SIX_ALT + r") loke(?=…)")
def r_six_pe(m):
    return f"{_six(m['x'])} {LOKE}"


@sent(r"Yo tassāyeva taṇhāya (?P<l>asesavirāganirodho .+?)\.")
def s_nirodha(m):
    return f"ထို{TANHA}၏ပင် {P1.items_my(P1.list_items(m['l']))} {REL}{END}"


# ---- appiya / piya
APPIYA_OBJ = f"{F.DEF['aniṭṭh']}{C} {F.DEF['akant']}{C} {F.DEF['amanāp']}"
PIYA_OBJ = f"{F.DEF['iṭṭh']}{C} {F.DEF['kant']}{C} {F.DEF['manāp']}"
FIVE = f"{C} ".join(OBJ6[o] for o in ("rūpa", "sadda", "gandha", "rasa", "phoṭṭhabba")) + "တို့"
KAMA4 = {"anatthakāmā": "အကျိုး မရှိခြင်းကို လိုလားသူ", "ahitakāmā": "အစီးအပွား မရှိခြင်းကို လိုလားသူ",
         "aphāsukakāmā": "ချမ်းသာ မရှိခြင်းကို လိုလားသူ", "ayogakkhemakāmā": "ဘေးကင်းမှု မရှိခြင်းကို လိုလားသူ",
         "atthakāmā": "အကျိုးကို လိုလားသူ", "hitakāmā": "အစီးအပွားကို လိုလားသူ", "phāsukakāmā": "ချမ်းသာကို လိုလားသူ",
         "yogakkhemakāmā": "ဘေးကင်းမှုကို လိုလားသူ"}
KIN = {"mātā": "မိခင်", "pitā": "ဖခင်", "bhātā": "ညီအစ်ကို", "bhaginī": "ညီအစ်မ", "mittā": "မိတ်ဆွေတို့",
       "amaccā": "အပေါင်းအဖော်တို့", "ñātī": "ဆွေမျိုးတို့", "sālohitā": "သွေးချင်းတို့"}
for _g, _d in (("Wishers (appiya / piya)", KAMA4), ("Relatives (piya)", KIN)):
    NEW.setdefault(_g, []).extend(_d.items())


@rule(r"Idha yassa te honti (?P<a>aniṭṭhā akantā amanāpā|iṭṭhā kantā manāpā) rūpā saddā gandhā rasā phoṭṭhabbā")
def r_yassa(m):
    obj = APPIYA_OBJ if m["a"].startswith("aniṭṭhā") else PIYA_OBJ
    return f"{IDHA_LOKA} အကြင်သူအား {obj} {FIVE} ရှိကြကုန်၏"


@rule(r"ye vā panassa te honti (?P<k>\w+kāmā \w+kāmā \w+kāmā \w+kāmā)(?P<kin> mātā vā pitā vā bhātā vā bhaginī vā "
      r"mittā vā amaccā vā ñātī vā sālohitā vā)?")
def r_ye_va(m):
    k = f"{C} ".join(KAMA4[w] for w in m["k"].split())
    if m["kin"]:
        kin = f"{C} ".join(KIN[w] + " ဖြစ်စေ" for w in m["kin"].split() if w != "vā")
        return f"{F.VA_OR} ထိုသူ၏ {k} ဖြစ်ကြသော {kin} ရှိကြကုန်၏"
    return f"{F.VA_OR} ထိုသူ၏ {k}တို့ ရှိကြကုန်၏"


@rule(r"yā tehi (?P<l>(?:a)?saṅgati .+?)(?= – )")
def r_tehi(m):
    return f"ထိုတို့နှင့် {P1.items_my(P1.list_items(m['l']))} {REL}"


# ---- yampicchaṃ
ICCHA_X = {"jāti": NM["jāti"], "jarā": NM["jarā"], "byādhi": "နာခြင်း", "maraṇa": NM["maraṇaṃ"],
           "sokaparidevadukkhadomanassupāyāsa": SOKA5}
HAVING = "သဘော ရှိသော"


@rule(r"(?P<x>[Jj]āti|[Jj]arā|byādhi|maraṇa|sokaparidevadukkhadomanassupāyāsa)dhammānaṃ sattānaṃ(?P<e> evaṃ icchā "
      r"uppajjati)?(?=…| –)")
def r_dhamma_satta(m):
    x = ICCHA_X[m["x"][0].lower() + m["x"][1:]]
    return f"{x} {HAVING} သတ္တဝါတို့အား" + (" ဤသို့ ဆန္ဒ ဖြစ်ပေါ်၏" if m["e"] else "")


@rule(r"\"aho vata, mayaṃ na (?P<x>jāti|sokaparidevadukkhadomanassupāyāsa)dhammā assāma; na ca, vata, no "
      r"(?P<y>jāti|sokaparidevadukkhadomanassupāyāsā) āgaccheyy(?:ā\"ti|u\"nti)! Na kho panetaṃ icchāya pattabbaṃ")
def r_aho(m):
    x = ICCHA_X[m["x"]]
    y = NM["jāti"] if m["y"] == "jāti" else SOKA5 + "တို့"
    return (f"“အို၊ ငါတို့သည် {x} {HAVING}သူများ မဖြစ်ကြပါစေလင့်၊ ငါတို့ထံသို့ {y} မရောက်လာပါစေလင့်”ဟု၊ "
            f"သို့သော် ဤအရာကို ဆန္ဒဖြင့် ရနိုင်သည် မဟုတ်")


@sent(r"Idampi \"(?P<x>[^\"]+)\"\.")
def s_idampi(m):
    return f"ဤသည်လည်း “{name_my(m['x'])}” {COP[False]}{END}"


@sent(r"Seyyathidaṃ – (?P<l>[^.]+)\.")
def s_seyyathidam(m):
    return f"{SEYYATHIDAM} – {name_list(m['l'])}{END}"


@sent(r"Tattha katame (?P<x>[^?]+)\?")
def s_question_pl(m):
    return f"ထိုတို့အနက် {name_my(m['x'])} {QUESTION_PL}{END}"


# ---- maggasacca (suttanta)
@sent(r"Ayameva ariyo aṭṭhaṅgiko maggo, seyyathidaṃ – (?P<l>[^.]+)\.")
def s_ariyamagga(m):
    return (f"{P1.count_my(P1._ANGA, 'aṭṭha')} ရှိသော ဤ{ARIYA} {MAGGA}ပင် {COP[False]}{C} {SEYYATHIDAM} – "
            f"{name_list(m['l'])}{END}")


FOUR_NANA = p1cut("Dukkhe ñāṇaṃ, dukkhasamudaye ñāṇaṃ, dukkhanirodhe ñāṇaṃ, dukkhanirodhagāminiyā paṭipadāya ñāṇaṃ, "
                  "pubbante ñāṇaṃ, aparante ñāṇaṃ, pubbantāparante ñāṇaṃ, idappaccayatā paṭiccasamuppannesu dhammesu "
                  "ñāṇaṃ, yā evarūpā paññā pajānanā vicayo pavicayo dhammavicayo sallakkhaṇā upalakkhaṇā "
                  "paccupalakkhaṇā paṇḍiccaṃ kosallaṃ nepuññaṃ vebhabyā cintā upaparikkhā bhūrī medhā pariṇāyikā "
                  "vipassanā sampajaññaṃ patodo paññā paññindriyaṃ paññābalaṃ paññāsatthaṃ paññāpāsādo paññāāloko "
                  "paññāobhāso paññāpajjoto paññāratanaṃ amoho dhammavicayo sammādiṭṭhi – ayaṃ vuccati amoho.",
                  None, "၊ အတိတ်ကာလကို")


@rule(r"Dukkhe ñāṇaṃ, dukkhasamudaye ñāṇaṃ, dukkhanirodhe ñāṇaṃ, dukkhanirodhagāminiyā paṭipadāya ñāṇaṃ(?= – )")
def r_four_nana(m):
    return FOUR_NANA


SANKAPPA3 = {"Nekkhammasaṅkappo": f"{PS['Nekkhamma']}ကို {P1.SYN['saṅkappo']}",
             "abyāpādasaṅkappo": f"{PS['Abyāpāda']}ကို {P1.SYN['saṅkappo']}",
             "avihiṃsāsaṅkappo": f"{PS['Avihiṃsā']}ကို {P1.SYN['saṅkappo']}"}
VERAMANI = P1.SYN.get("veramaṇī") or "ကင်းဝေးခြင်း"
ABST = {"Musāvādā": "မုသားစကားမှ", "pisuṇāya vācāya": "ကုန်းချောစကားမှ", "pharusāya vācāya": "ကြမ်းတမ်းသော စကားမှ",
        "samphappalāpā": "အကျိုးမဲ့ စကားမှ", "Pāṇātipātā": "သူ့အသက်ကို သတ်ခြင်းမှ",
        "adinnādānā": "မပေးသည်ကို ယူခြင်းမှ", "kāmesumicchācārā": "ကာမတို့၌ မှားယွင်းစွာ ကျင့်ခြင်းမှ"}
for _g, _d in (("Right intention (suttanta)", SANKAPPA3), ("Abstentions (veramaṇī = pi-1 ကင်းဝေးခြင်း)", ABST)):
    NEW.setdefault(_g, []).extend(_d.items())


@rule(r"Nekkhammasaṅkappo, abyāpādasaṅkappo, avihiṃsāsaṅkappo(?= – )")
def r_sankappa3(m):
    return f"{C} ".join(SANKAPPA3.values())


@rule(r"(?P<l>(?:(?:Musāvādā|pisuṇāya vācāya|pharusāya vācāya|samphappalāpā|Pāṇātipātā|adinnādānā|kāmesumicchācārā) "
      r"veramaṇī(?:, )?)+)(?= – )")
def r_veramani(m):
    items = re.findall(r"(.+?) veramaṇī(?:, |$)", m["l"])
    return f"{C} ".join(f"{ABST[x]} {VERAMANI}" for x in items)


ARIYASAVAKA = f"{ARIYA} တပည့်သည်"                         # ariyasāvako


@rule(r"Idha ariyasāvako micchāājīvaṃ pahāya sammāājīvena jīvikaṃ kappeti")
def r_ajiva(m):
    return f"{IDHA_HEAD} {ARIYASAVAKA} မှားယွင်းသော အသက်မွေးမှုကို ပယ်၍ {NM['sammāājīvo']}ဖြင့် အသက် မွေး၏"


ANUPASSI = "ကို အဖန်ဖန် ရှုလျက်"
SATI_TAIL = (f"အားထုတ်သူ{C} ကောင်းစွာ ဆင်ခြင်သိမြင်သူ{C} {P1.SUT['sati']} ရှိသူ ဖြစ်၍ {LOKE} "
             f"{P1TANHA['abhijjhā']}နှင့် {NM['domanassaṃ']}ကို ပယ်ဖျောက်လျက် နေ၏")
FOUR_BASE = {"kāye kāyānupassī": f"ကိုယ်၌ ကိုယ်{ANUPASSI}", "dhammesu dhammānupassī": f"{DH}တို့၌ {DH}တို့{ANUPASSI}"}


@sent(r"(?P<i>Idha bhikkhu )?(?P<pre>(?:Vedanāsu…pe… citte…pe… ))?(?P<b>kāye kāyānupassī|dhammesu dhammānupassī) viharati "
      r"ātāpī sampajāno satimā, vineyya loke abhijjhādomanassaṃ\.")
def s_sati(m):
    head = f"{IDHA_HEAD} {BHIKKHU} " if m["i"] else ""
    pre = f"{P1.FEEL}တို့၌{PE} {P1.MIND}၌{PE} " if m["pre"] else ""
    return f"{head}{pre}{FOUR_BASE[m['b']]}{C} {SATI_TAIL}{END}"


JH = P1.JH_FORM
ORDJ = {"paṭhamaṃ": P1.ORD["paṭhama"], "dutiyaṃ": P1.ORD["dutiya"], "tatiyaṃ": P1.ORD["tatiya"],
        "catutthaṃ": P1.ORD["catuttha"]}


def jhana_parts(text):
    text = text[0].lower() + text[1:]
    toks = re.findall(r'yaṃ taṃ ariyā ācikkhanti – "upekkhako satimā sukhavihārī"ti|[^\s,]+|,', text)
    out, i = [], 0
    while i < len(toks):
        if toks[i] == ",":
            i += 1
            continue
        for k in range(4, 0, -1):
            ph = " ".join(toks[i:i + k])
            if len(toks[i:i + k]) == k and ph in JH:
                out.append(JH[ph])
                i += k
                break
        else:
            raise Miss("jhāna word: " + toks[i])
    return f"{C} ".join(out)


@sent(r"(?P<i>Idha bhikkhu )?(?P<l>.+?),? (?P<o>paṭhamaṃ|dutiyaṃ|tatiyaṃ|catutthaṃ) jhānaṃ upasampajja viharati\.")
def s_jhana(m):
    head = f"{IDHA_HEAD} {BHIKKHU} " if m["i"] else ""
    return f"{head}{jhana_parts(m['l'])} {ORDJ[m['o']]} {P1.JHANA}ကို ဝင်စား၍ နေ၏{END}"


# ---- abhidhamma part
REMAIN = "ကြွင်းကျန်သော"                                  # avasesa (remaining)
KM3 = f"{P1.SYN['kusalamūlaṃ']} {NUMW['ti']}{CL}"           # tīṇi kusalamūlāni
SAS = T["sāsavā"]
DCLAUSE = {
    "taṇhā": f"{TANHA}လည်း",
    "avasesā ca kilesā": f"{REMAIN} {P1.KIL}တို့လည်း",
    "avasesā ca akusalā dhammā": f"{REMAIN} {T['akusalā']} {DH}တို့လည်း",
    "tīṇi ca kusalamūlāni sāsavāni": f"{SAS} {KM3}တို့လည်း",
    "avasesā ca sāsavā kusalā dhammā": f"{REMAIN} {SAS} {T['kusalā']} {DH}တို့လည်း",
    "sāsavā ca kusalākusalānaṃ dhammānaṃ vipākā": f"{SAS} {T['kusalā']}နှင့် {T['akusalā']} {DH}တို့၏ အကျိုးတို့လည်း",
    "sāsavā kusalākusalānaṃ dhammānaṃ vipākā": f"{SAS} {T['kusalā']}နှင့် {T['akusalā']} {DH}တို့၏ အကျိုးတို့လည်း",
    "ye ca dhammā kiriyā neva kusalā nākusalā na ca kammavipākā":
        C3["FIXED"]["ye ca dhammā kiriyā neva kusalā nākusalā na ca kammavipākā"],
    "sabbañca rūpaṃ": C3["FIXED"]["sabbañca rūpaṃ"],
}
GCLAUSE = {
    "taṇhāya": f"{TANHA}ကိုလည်းကောင်း", "avasesānañca kilesānaṃ": f"{REMAIN} {P1.KIL}တို့ကိုလည်းကောင်း",
    "avasesānañca akusalānaṃ dhammānaṃ": f"{REMAIN} {T['akusalā']} {DH}တို့ကိုလည်းကောင်း",
    "tiṇṇañca kusalamūlānaṃ sāsavānaṃ": f"{SAS} {KM3}တို့ကိုလည်းကောင်း",
    "avasesānañca sāsavānaṃ kusalānaṃ dhammānaṃ": f"{REMAIN} {SAS} {T['kusalā']} {DH}တို့ကိုလည်းကောင်း",
}
for _g, _d in (("Abhidhamma part: what is suffering / its arising", DCLAUSE), ("… and its ceasing", GCLAUSE)):
    NEW.setdefault(_g, []).extend(_d.items())
PAHANA = "ပယ်ခြင်း"


@rule(r"(?P<l>(?:Taṇhā(?![\wāīūṃṅñṭḍṇḷ])|[Aa]vasesā|[Tt]īṇi|[Ss]āsavā|ye ca dhammā kiriyā|sabbañca)[^–]*?)(?= – )")
def r_dclause(m):
    parts = [x.strip() for x in m["l"].split(", ")]
    out = []
    for p in parts:
        p0 = p[0].lower() + p[1:]
        if p0 == "taṇhā ca avasesā ca kilesā":
            out += [DCLAUSE["taṇhā"], DCLAUSE["avasesā ca kilesā"]]
            continue
        if p0 == "taṇhā ca":
            out.append(DCLAUSE["taṇhā"])
            continue
        if p0 == "taṇhā" and len(parts) == 1:
            out.append(TANHA)
            continue
        if p0 not in DCLAUSE:
            return None
        out.append(DCLAUSE[p0])
    return f"{C} ".join(out)


@rule(r"(?P<l>Taṇhāya(?: ca)?(?:, [^–]+?)?) pahānaṃ(?= – )")
def r_gclause(m):
    parts = [x.strip() for x in m["l"].split(", ")]
    if parts == ["Taṇhāya"]:
        return f"{TANHA}ကို {PAHANA}"
    out = []
    for p in parts:
        p0 = (p[0].lower() + p[1:]).removesuffix(" ca")
        if p0 not in GCLAUSE:
            return None
        out.append(GCLAUSE[p0])
    return f"{C} ".join(out) + f" {PAHANA}"


LOKUTTARA_OPEN = p1cut("Yasmiṃ samaye lokuttaraṃ jhānaṃ bhāveti niyyānikaṃ apacayagāmiṃ diṭṭhigatānaṃ pahānāya "
                       "paṭhamāya bhūmiyā pattiyā vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja viharati "
                       "dukkhapaṭipadaṃ dandhābhiññaṃ, tasmiṃ samaye phasso hoti…pe… avikkhepo hoti…pe… ime dhammā "
                       "kusalā.", None, "၊ ထိုအချိန်၌")


def r_lok_open(m):
    return f"{IDHA_HEAD} {BHIKKHU} {LOKUTTARA_OPEN}"


P1.CU_EXTRA_RULES[:0] = [
    (re.compile(r"aṭṭhaṅgiko maggo hoti(?= sammādiṭṭhi…pe…)"),
     lambda m: f"{P1.NAMES['aṭṭhaṅgiko maggo']} {P1.CU_HOTI['sg']}{C}"),      # no punctuation in the Pāli: «၊»
    (re.compile(r"Idha bhikkhu yasmiṃ samaye lokuttaraṃ jhānaṃ bhāveti niyyānikaṃ apacayagāmiṃ diṭṭhigatānaṃ pahānāya "
                r"paṭhamāya bhūmiyā pattiyā,? vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja viharati dukkhapaṭipadaṃ "
                r"dandhābhiññaṃ"), r_lok_open),
]
P1.rebuild_cu()
for _s in (
        "Yā tasmiṃ samaye paññā pajānanā vicayo pavicayo dhammavicayo sallakkhaṇā upalakkhaṇā paccupalakkhaṇā "
        "paṇḍiccaṃ kosallaṃ nepuññaṃ vebhabyā cintā upaparikkhā bhūrī medhā pariṇāyikā vipassanā sampajaññaṃ patodo "
        "paññā paññindriyaṃ paññābalaṃ paññāsatthaṃ paññāpāsādo paññāāloko paññāobhāso paññāpajjoto paññāratanaṃ "
        "amoho dhammavicayo sammādiṭṭhi dhammavicayasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ – idaṃ tasmiṃ samaye "
        "paññindriyaṃ hoti.",
        "Yo tasmiṃ samaye takko vitakko saṅkappo appanā byappanā cetaso abhiniropanā sammāsaṅkappo maggaṅgaṃ "
        "maggapariyāpannaṃ – ayaṃ tasmiṃ samaye vitakko hoti.",
        "Yā tasmiṃ samaye catūhi vacīduccaritehi ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti "
        "velāanatikkamo setughāto sammāvācā maggaṅgaṃ maggapariyāpannaṃ – ayaṃ tasmiṃ samaye sammāvācā hoti.",
        "Yā tasmiṃ samaye tīhi kāyaduccaritehi ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti "
        "velāanatikkamo setughāto sammākammanto maggaṅgaṃ maggapariyāpannaṃ – ayaṃ tasmiṃ samaye sammākammanto hoti.",
        "Yā tasmiṃ samaye micchāājīvā ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti velāanatikkamo "
        "setughāto sammāājīvo maggaṅgaṃ maggapariyāpannaṃ – ayaṃ tasmiṃ samaye sammāājīvo hoti.",
        "Yo tasmiṃ samaye cetasiko vīriyārambho nikkamo parakkamo uyyāmo vāyāmo ussāho ussoḷhī thāmo dhiti "
        "asithilaparakkamatā anikkhittachandatā anikkhittadhuratā dhurasampaggāho vīriyaṃ vīriyindriyaṃ vīriyabalaṃ "
        "sammāvāyāmo vīriyasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ – idaṃ tasmiṃ samaye vīriyindriyaṃ hoti.",
        "Yā tasmiṃ samaye sati anussati paṭissati sati saraṇatā dhāraṇatā apilāpanatā asammussanatā sati satindriyaṃ "
        "satibalaṃ sammāsati satisambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ – idaṃ tasmiṃ samaye satindriyaṃ hoti.",
        "Yā tasmiṃ samaye cittassa ṭhiti saṇṭhiti avaṭṭhiti avisāhāro avikkhepo avisāhaṭamānasatā samatho "
        "samādhindriyaṃ samādhibalaṃ sammāsamādhi samādhisambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ – ayaṃ tasmiṃ "
        "samaye cittassekaggatā hoti."):
    learn(_s)
VERAMANI = P1.SYN["veramaṇī"]
assert VERAMANI == "ကင်းဝေးခြင်း"


@sent(r"Avasesā dhammā dukkhanirodhagāminiyā paṭipadāya sampayuttā\.")
def s_avasesa(m):
    return f"{REMAIN} {DH}တို့သည် {NM['dukkhanirodhagāminī paṭipadā']}{F.SAMP} {DHP} {COP[True]}{END}"


# pañhāpucchaka: «siyā A na B» / bare «na A B»
@rule(r"siyā (?P<a>[^\s,]+) na (?P<b>[^\s,]+)(?=, |\.)")
def r_siya_a_na_b(m):
    pl = STATE.get("pl", False)
    return (f"{F.SIYA} {F.term_my(m['a'])}{C} {P1.no_(F.term_my(m['b']))} {DHP if pl else DH} {COP[pl]}")


@rule(r"na (?P<a>maggārammaṇaṃ) (?P<b>maggahetukaṃ)(?=, )")
def r_na_a_b(m):
    pl = STATE.get("pl", False)
    return f"{P1.no_(F.term_my(m['a']))}{C} {F.term_my(m['b'])} {DHP if pl else DH} {COP[pl]}"


SLIPS.update({
    # 4-saccavibhango
    "Yā micchā ājīvā ārati": "Yā micchāājīvā ārati",
    "Dve saccā nīvaraṇiyā dve saccā anīvaraṇiyā.": "Dve saccā nīvaraṇiyā, dve saccā anīvaraṇiyā.",
    "Dukkhasaccaṃ siyā ajjhattaṃ, siyā bāhiraṃ.": "Dukkhasaccaṃ siyā ajjhattikaṃ, siyā bāhiraṃ.",
    '"upādānañceva upādānasampayuttañcā" tipi': '"upādānañceva upādānasampayuttañcā"tipi',
    '"kileso ceva kilesasampayuttañcā" tipi': '"kileso ceva kilesasampayuttañcā"tipi',
})


# ===================================================================================== output
def write(name, txt):
    txt = unicodedata.normalize("NFC", txt)
    (OUT / name).write_text(txt, encoding="utf-8")
    print(f"wrote {name}: {sum(1 for l in txt.splitlines() if l)} lines")


def chapter(name):
    lines = (PALI / name).read_text(encoding="utf-8-sig").splitlines()
    done, misses = [], []
    STATE.clear()
    for i, line in enumerate(lines):
        try:
            done.append(translate_line(line))
        except Miss as e:
            misses.append(f"line {i + 1}: {str(e)[:300]}")
            done.append("")
    if misses:
        print(f"STOP {name}: {len(misses)} lines missed")
        for x in misses[:int(ARGS.get('max', 12))]:
            print("  " + x)
        return False
    write(name, "\n".join(done).rstrip("\n") + "\n")
    return True


NOTES = HERE / "notes-ch2-4.md"
TERMS_HEAD = "## New terms and strings (generated by make_ch2-4.py)"


def write_terms():
    """Rewrite the generated section of notes-ch2-4.md: every new string, «Pāli = Burmese», one per line."""
    groups = dict(NEW)
    groups["Building blocks"] = [
        ("sacca", SACCA), ("ariya", ARIYA), ("dukkha (truth / characteristic)", DUKKHA_T),
        ("dukkha (bodily pain, suttanta definitions; pi-1 soka… list)", BODILY_DUKKHA), ("samudaya", SAMUDAYA),
        ("nirodha", NIRODHA), ("nirodhagāminī", GAMINI), ("seyyathidaṃ", SEYYATHIDAM),
        ("yaṃ vā panaññampi atthi …", f"… {VA_PANA} … {REL}လည်း"), ("-paṭisaṃyutta", PATISAMYUTTA),
        ("uppajjati (finite)", UPPAJJATI), ("uppajjitvā niruddhasamanantarā", NIRUDDHA),
        ("Xñca paṭicca Y ca uppajjati", f"Xကိုလည်းကောင်း၊ Yတို့ကိုလည်းကောင်း မှီ၍ … {UPPAJJATI}"),
        ("Idha (monk / disciple)", IDHA_HEAD), ("Idha (anyone; pi-1 Idhekacco)", IDHA_LOKA), ("bhikkhu", BHIKKHU),
        ("ariyasāvako", ARIYASAVAKA), ("avasesa", REMAIN), ("pahānaṃ", PAHANA), ("piyarūpaṃ", PIYARUPA),
        ("sātarūpaṃ", SATARUPA), ("loke", LOKE), ("-dhamma (having the nature of)", HAVING),
        ("…, na vattabbā – … (after siyā clauses)", BUT), ("(?) siglum", SIG["?"]),
        ("evamuparipi", EVAM_UPARI), ("dha. sa. N (cross-reference)", f"“{P1.TITLE}” N"),
        ("Imā cha dhātuyo", f"ဤတို့သည် {count(DHATU, 'cha')} {COP[True]}"),
        ("Yā sattesu …", "သတ္တဝါတို့အပေါ်၌ … ရှိသမျှ"),
        ("Dasasu vā āghātavatthūsu", f"ရန်ငြိုးဖွဲ့ရာ အကြောင်း {NUMW['dasa']}{CL}တို့၌ဖြစ်စေ"),
        ("sabbadhammesu vā pana paṭhamasamannāhāro", f"{F.VA_OR} {DH} အားလုံးတို့၌ ပထမ နှလုံးသွင်းခြင်း ဖြစ်သော"),
        ("Avasesā dhammā dukkhanirodhagāminiyā paṭipadāya sampayuttā",
         f"{REMAIN} {DH}တို့သည် {NM['dukkhanirodhagāminī paṭipadā']}{F.SAMP} {DHP} {COP[True]}"),
    ]
    groups["Count heads"] = list(COUNT_HEAD.items()) + list(COUNT_AMONG.items())
    groups["Synonym lists (truths)"] = [(k, v) for k, v in SYN4.items()]
    L = [TERMS_HEAD, "", "One «Pāli = Burmese» per line; pi-1 values marked in the code (asserts against the pi-1 "
         "rails text). my2_formulas.py and my2-zeroshot-terms.md are not changed.", ""]
    for g, items in groups.items():
        L += [f"### {g}", ""]
        seen = set()
        for k, v in items:
            if k in seen:
                continue
            seen.add(k)
            L.append(f"{k} = {v[0] if isinstance(v, tuple) else v}")
        L.append("")
    txt = NOTES.read_text(encoding="utf-8") if NOTES.exists() else ""
    i = txt.find("\n" + TERMS_HEAD + "\n")
    base = (txt[:i + 1] if i >= 0 else txt).rstrip("\n") + "\n\n"
    NOTES.write_text(unicodedata.normalize("NFC", base + "\n".join(L).rstrip("\n") + "\n"), encoding="utf-8")
    print("updated notes-ch2-4.md:", TERMS_HEAD)


ARGS = {}
if __name__ == "__main__":
    names = [a for a in sys.argv[1:] if not a.startswith("--")] or NAMES_OUT
    for a in sys.argv[1:]:
        if a.startswith("--max="):
            ARGS["max"] = a[6:]
    install_rules()
    OUT.mkdir(parents=True, exist_ok=True)
    ok = all([chapter(n) for n in names])
    if ok and "--no-terms" not in sys.argv:
        write_terms()
