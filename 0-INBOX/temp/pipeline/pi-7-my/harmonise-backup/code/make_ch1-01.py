"""Burmese zero-shot of pi-7 1-01-kusalattika («ကုသိုလ် သုံးမျိုးတွဲ»), the full model triad, from the Pāli only.

usage: python3 -I -X utf8 make_ch1-01.py [--dev] [--regress]
  (no flag)  translate the chapter and write AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters/
             1-01-kusalattika.md; stops on the first unmatched sentence (nothing is guessed).
  --dev      do not stop: list every unmatched skeleton with its count in chk-ch1-01/dev.txt (nothing written).
  --regress  regenerate the approved sample (1-00, 1-02) in memory through these frames and compare it with the
             published files (must be byte-identical; nothing written).

Every line goes through my7_formulas.translate() (shared module, read-only) with the sample's templates
(make_sample.py is imported, never run) and this chapter's frames, which setup() registers. The frames are clean
functions of their terms (triad terms, nouns, conditions), so the later triads / dyads can reuse them:

    import importlib.util, pathlib
    spec = importlib.util.spec_from_file_location("ch101", pathlib.Path(__file__).with_name("make_ch1-01.py"))
    K = importlib.util.module_from_spec(spec); spec.loader.exec_module(K)     # setup() runs on import

Every new string is logged in notes-ch1-01.md («Pāli = Burmese»).
"""
import collections
import pathlib
import re
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import my7_formulas as F  # noqa: E402
import make_sample as S  # noqa: E402  (registers the sample's templates; its main() is not run)

ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-7_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters"
NAME = "1-01-kusalattika.md"
CHK = HERE / "chk-ch1-01"
C, END, PE = F.C, F.END, F.PE
W = F.W
ABY = F.ABY

# ===================================================================================== nouns, qualifiers, numbers
MAHABHUTA = F.NOUN["mahābhūtā"][0]                              # «မူလဓာတ်ကြီး» (pi-1 / pi-2 / pi-5)
VIPAKABY = W("vipākābyākatā", "ကံ၏ အကျိုး ဖြစ်သော " + ABY, "5")    # vipākābyākata (pi-5 rails)
KIRIYABY = F.QUAL["kiriyābyākatā"]                               # kiriyābyākata (pi-5 rails)
CITTASAM = F.QUAL["cittasamuṭṭhānānaṃ"]                          # «စိတ်မှ ဖြစ်ပေါ်လာသော» (pi-1 / pi-2)
UPADARUPA = F.FIXED["upādārūpānaṃ"][0]                           # «မူလဓာတ်ကြီးတို့ကို မှီ၍ ဖြစ်သော ရုပ်» (pi-5)
BAHIRA = W("bāhiraṃ", "ပြင်ပ", "1")
UTU = "ရာသီဥတု"                                                  # utu (module «ရာသီဥတုနှင့် အစားအစာ»)
ASANNA = W("Asaññasattānaṃ", "အသညသတ်", "5")                      # asaññasattā (pi-5 «အသညသတ်တို့၌»)
VATTHU = F.VATTHU                                                # «မှီရာ ဝတ္ထု» (pi-5)
CAKKHUVINNANA = {"cakkhu": "မျက်စိ", "sota": "နား", "ghāna": "နှာခေါင်း", "jivhā": "လျှာ", "kāya": "ကိုယ်"}


def setup_nouns():
    F.add_noun(MAHABHUTA, n=["mahābhūtaṃ"], ap=["mahābhūte"], g=["mahābhūtassa"], gp=["mahābhūtānaṃ"])
    F.add_noun(VATTHU, n=["vatthu"], g=["vatthussa"])
    F.add_noun(F.N["āhāra"], np=["āhārā"])
    F.add_noun(F.N["indriya"], np=["indriyā"])
    F.NP_NUM.update({"tiṇṇannaṃ": 3, "tayo": 3})
    F.add_qual(CITTASAM, "cittasamuṭṭhānaṃ")
    F.add_qual(VIPAKABY, "vipākābyākataṃ", "vipākābyākato", "vipākābyākatā", "vipākābyākatānaṃ", "vipākābyākate",
               "vipākābyākatassa")
    F.add_qual(KIRIYABY, "kiriyābyākataṃ", "kiriyābyākato", "kiriyābyākate", "kiriyābyākatassa")
    F.add_qual(BAHIRA, "bāhiraṃ")
    F.add_qual(f"{F.N['āhāra']}မှ ဖြစ်ပေါ်လာသော", "āhārasamuṭṭhānaṃ")       # NEW
    F.add_qual(f"{UTU}မှ ဖြစ်ပေါ်လာသော", "utusamuṭṭhānaṃ")                  # NEW
    F.add_fixed(F.KATATTARUPA, "n", False, "kaṭattārūpaṃ", "kaṭattā ca rūpaṃ")
    F.add_fixed(UPADARUPA, "n", False, "upādārūpaṃ")
    for p, my in CAKKHUVINNANA.items():
        v = W(p + "viññāṇaṃ", my + " သိစိတ်", "1")
        F.add_fixed(v, "n", False, p + "viññāṇaṃ")
        F.add_fixed(v, "g", False, p + "viññāṇassa")
    F.PREFIX["asaññasattānaṃ"] = ASANNA + "တို့၏"                     # NEW (genitive «of the non-percipient beings»)


# ===================================================================================== engine extensions
# Link words (after an accusative NP): the sample's renderings; a coordinated NP («A ca B ca paṭicca») puts the
# link's case marker inside each conjunct («Aကိုလည်းကောင်း၊ Bကိုလည်းကောင်း မှီ၍», as pi-2 «… တို့ကိုလည်းကောင်း မှီ၍»).
ROLE_MARK = {"paṭicca": "ကို", "nissāya": "ကို", "paccayā": "ကြောင့်", "sahajāto": "နှင့်", "sahajātā": "နှင့်",
             "sahajātaṃ": "နှင့်", "saṃsaṭṭho": "နှင့်", "saṃsaṭṭhā": "နှင့်", "sampayutto": "နှင့်",
             "sampayuttā": "နှင့်", "ārabbha": "ကို"}
ROLE_REST = {"paṭicca": "မှီ၍", "nissāya": "မှီ၍", "paccayā": "", "sahajāto": "အတူ ပေါ်ပေါက်သော",
             "sahajātā": "အတူ ပေါ်ပေါက်သော", "sahajātaṃ": "အတူ ပေါ်ပေါက်သော", "saṃsaṭṭho": "ရောနှောသော",
             "saṃsaṭṭhā": "ရောနှောသော", "sampayutto": "ယှဉ်တွဲသော", "sampayuttā": "ယှဉ်တွဲသော",
             "ārabbha": "အာရုံပြု၍"}
_ORIG_NP = F.np_my


def _n_terms(words):
    return sum(1 for w in words if w.startswith("§T§"))


def _conj_render(parts, vals, role):
    """Coordinated NP parts -> «Xလည်းကောင်း၊ Yလည်းကောင်း» (case marker inside each conjunct, none for 'n')."""
    it = iter(vals)
    out = []
    for p in parts:
        ph, _, pl, k = F.np_parse(p, it)
        out.append(ph + F._mark(pl, "x", role if role != "n" else "") + F.LAKAUNG)
    return (C + " ").join(out)


def _chunks(words, vals):
    """Split an asyndetic NP list («cittasamuṭṭhānaṃ rūpaṃ kaṭattārūpaṃ upādārūpaṃ») into parseable chunks
    (each ends at a head noun), left to right, longest first. Returns [(phrase, plural)] or None."""
    out, i, vi = [], 0, 0
    while i < len(words):
        for j in range(len(words), i, -1):
            nt = _n_terms(words[i:j])
            try:
                ph, _, pl, k = F.np_parse(words[i:j], iter(vals[vi:vi + nt]))
            except (KeyError, StopIteration):
                continue
            out.append((ph, pl))
            i, vi = j, vi + nt
            break
        else:
            return None
    return out if len(out) > 1 else None


def expand_nca(words):
    """«Xñca» -> «Xṃ ca» (not for triad terms, not inside fixed phrases), so that the sample's rules for «ca» see
    every conjunct: «kusalaṃ ekaṃ khandhañca vatthuñca» = [kusalaṃ ekaṃ khandhaṃ] [vatthuṃ]."""
    out = []
    for w in words:
        head = w[:-3] + "ṃ"
        if (w.endswith("ñca") and not w.startswith("§T§") and w not in F.FIXED and len(words) > 1
                and (head in F.NOUN or head in F.FIXED) and head not in F.QUAL):
            out += [w[:-3] + "ṃ", "ca"]
        else:
            out.append(w)
    return out


_ORIG_CASE = F._case_of


def case_of2(words):
    words = expand_nca(list(words))
    while len(words) > 1 and words[-1] == "ca":
        words = words[:-1]
    return _ORIG_CASE(words)


def np_my2(words, terms, role):
    """F.np_my plus: commas inside an NP list are dropped; «A B ca» (one closing ca) = «A ca B ca»; an asyndetic
    list of NPs gets «၊» between them; a role «@link» marks each conjunct with the link's case."""
    words = expand_nca([w.rstrip(",") for w in words])
    nt = _n_terms(words)
    vals = [next(terms) for _ in range(nt)]
    mark_role = role[1:] if role.startswith("@") else None
    base_role = "" if mark_role else role
    term_coord = all(w.startswith("§T§") or w == "ca" for w in words[:-1]) and nt > 1
    if mark_role and not term_coord:
        txt = " ".join(words)
        for k in F.FIXED:
            if " ca " in k and k in txt:
                txt = txt.replace(k, k.replace(" ", "\u0002"))
        parts = F._conj(txt.split())
        if parts is None and len(words) >= 3 and words[-1] == "ca" and words.count("ca") == 1:
            parts = [words[:-2], [words[-2]]]
        if parts:
            return _conj_render(parts, vals, role), True, nt
    try:
        return _ORIG_NP(words, iter(vals), base_role)
    except (KeyError, StopIteration):
        pass
    if len(words) >= 3 and words[-1] == "ca" and words.count("ca") == 1:
        return _conj_render([words[:-2], [words[-2]]], vals, base_role), True, nt
    ch = _chunks(words, vals) if nt == 0 else None          # term-free lists only (the sample's are not lists)
    if ch:
        joined = (C + " ").join(ph for ph, _ in ch)
        pl = any(p for _, p in ch)
        return joined + F._mark(pl, None, base_role), pl, nt
    raise KeyError("np: " + " ".join(words))


def link_np(aw, link, terms):
    """«NP-acc LINK» -> Burmese (conjuncts marked inside), consuming the NP's terms. Returns (Burmese, n_terms)."""
    nt = _n_terms(aw)
    vals = [next(terms) for _ in range(nt)]
    r, _, k = np_my2(aw, iter(vals), "@" + link)
    if F.LAKAUNG in r and r.endswith(F.LAKAUNG):
        rest = ROLE_REST[link]
        return r + (" " + rest if rest else ""), k
    a_my, _, k = np_my2(aw, iter(vals), "")
    a_my = re.sub(r"များ$", "တို့", a_my)
    return F.LINK[link](a_my), k


def clause2(frag, slots, ti, ci, ki, di, hold=False):
    """F.clause with the accusative NP rendered by link_np (conjuncts marked inside); otherwise identical."""
    m = F.CLAUSE_RE.match(frag)
    if not m or not (m["a"] or m["b"] or m["ch"].strip()):
        raise KeyError("clause: " + frag)
    if m["siya"] and not m["v"]:
        raise KeyError("siyā without verb: " + frag)
    terms = iter(slots["T"][ti[0]:])
    parts = [m["lead"]]
    if m["pre"]:
        parts.append(F.PREFIX[m["pre"]] + " ")
    used = 0
    if m["a"]:
        a_txt, k = link_np(m["a"].split(), m["link"], terms)
        used += k
        parts.append(a_txt)
        parts.append(" " if (m["b"] or m["ch"].strip()) else "")
    if m["b"]:
        b_my, bpl, k = F.np_my(m["b"].split(), terms, "n")
        used += k
        parts.append(b_my + " ")
    ti[0] += used
    ch = m["ch"]
    note = ""
    for k in sorted(F.NOTES, key=len, reverse=True):
        if ch.endswith(" " + k) and m["v"]:
            ch, note = ch[:-len(k) - 1], k
            break
    if ch.strip():
        parts.append(F.chain(ch, slots, ci, ki, di))
        if m["v"]:
            parts.append(" ")
    if m["v"]:
        if hold:
            F.HELD.append(F.VERB[m["v"]])
            if parts and parts[-1] == " ":
                parts.pop()
        else:
            parts.append(F.VERB[m["v"]])
    if note:
        parts.append(" " + F.NOTES[note])
    return "".join(parts).rstrip(" ") + F.punct(m["trail"])


def pairs2(s, slots, ti):
    """F.pairs with link_np (conjuncts marked inside)."""
    out = []
    for part in s.split(", "):
        pm = re.match(r"^(?P<pre>(?:" + "|".join(map(re.escape, F.PREFIX)) + r") )?(?P<a>.+?) (?P<link>"
                      + "|".join(F.LINK) + r") (?P<b>.+)$", part)
        if not pm:
            raise KeyError("pair: " + part)
        terms = iter(slots["T"][ti[0]:])
        a_txt, k1 = link_np(pm["a"].split(), pm["link"], terms)
        b_my, _, k2 = F.np_my(pm["b"].split(), terms, "")
        ti[0] += k1 + k2
        pre = F.PREFIX[pm["pre"].strip()] + " " if pm["pre"] else ""
        out.append(pre + a_txt + " " + b_my)
    return (C + " ").join(out)


def setup_engine():
    for k in ("sahajātā", "sahajātaṃ"):
        F.LINK[k] = F.LINK["sahajāto"]
    F.LINK["saṃsaṭṭhā"] = F.LINK["saṃsaṭṭho"]
    for k in ROLE_MARK:
        F.CASE["@" + k] = ROLE_MARK[k]
    F.np_my = np_my2
    F.clause = clause2
    F.pairs = pairs2
    F._case_of = case_of2


# ===================================================================================== numbers above ten
# counts «… ၌ Nခု» and counting groups «Nမျိုးတွဲ» (Burmese number words; NEW above ten)
NUM11 = {"ekādasa": (11, "ဆယ့်တစ်"), "dvādasa": (12, "ဆယ့်နှစ်"), "terasa": (13, "ဆယ့်သုံး"),
         "cuddasa": (14, "ဆယ့်လေး"), "pannarasa": (15, "ဆယ့်ငါး"), "soḷasa": (16, "ဆယ့်ခြောက်"),
         "sattarasa": (17, "ဆယ့်ခုနစ်"), "aṭṭhārasa": (18, "ဆယ့်ရှစ်"), "vīsa": (20, "နှစ်ဆယ်"),
         "ekavīsa": (21, "နှစ်ဆယ့်တစ်"), "bāvīsa": (22, "နှစ်ဆယ့်နှစ်")}


def setup_numbers():
    for w, (n, my) in NUM11.items():
        if w in ("vīsa", "ekavīsa", "bāvīsa"):
            continue
        F.COUNT[w] = my + "ခု"
        F.COUNT_VAL[w] = n
    F._CNT_ALT = "|".join(sorted(F.COUNT, key=len, reverse=True))
    F.COUNT_RE = re.compile(r"(?<![\wāīūṃṅñṭḍṇḷ])(?P<neg>[Nn]a|[Nn]o)?(?P<loc>(?i:" + F._LOC_ALT + r")) (?P<num>"
                            + F._CNT_ALT + r")(?![\wāīūṃṅñṭḍṇḷ])")
    for w, (n, my) in NUM11.items():
        F.GROUP[w + "ka"] = my + "မျိုးတွဲ"
    F.GROUP["chakka"] = F.GROUP.get("chakka", "ခြောက်မျိုးတွဲ")


# ===================================================================================== headings
SA_PAREN = {"sāsevanaṃ": "āsevana", "savipākaṃ": "vipāka", "sāhāraṃ": "āhāra", "saindriyaṃ": "indriya",
            "saupanissayaṃ": "upanissaya", "sakammaṃ": "kamma"}
PAAWIN = "ပါဝင်သော"                     # sa-X «Nဟူသော အကြောင်း ပါဝင်သော» (sample PAREN)
NA_PAAWIN = "မပါဝင်သော"                 # a-X «Nဟူသော အကြောင်း မပါဝင်သော» (NEW)
MISSAKA = "ရောစပ်"                      # -missaka (NEW) «… ရောစပ် ပေါင်းစပ်ချက်»
GANANA = S.GANANA                       # gaṇanā «ရေတွက်ချက်» (sample)
MULAKA_ADJ = "ကို အခြေခံသော"            # X-mūlakā (adjective, gaṇanā hetumūlakā) (NEW)


def sa_x(stem, neg=False):
    return f"{F.cname(stem)} {NA_PAAWIN if neg else PAAWIN}"


def _stems_sa(s):
    """'indriya-magga' / 'indriyamagga' / 'hetādhipati-indriya' / 'hetu-adhipati-magga' -> condition stems."""
    stems, _ = F.segment_conds(s.replace("hetādhipati", "hetu-adhipati"))
    return stems


_ORIG_HEADING = F._heading


def heading_core(t):
    """The heading cores the sample module does not know (raises KeyError otherwise)."""
    try:
        return _ORIG_HEADING(t)
    except KeyError:
        pass
    lt = t[0].lower() + t[1:]
    # «Anulomaṃ – hetupaccayo» / «Paccanīyaṃ – nahetupaccayo»
    if " – " in t:
        return " – ".join(heading_core(p) for p in t.split(" – "))
    if t in ("Anulomaṃ",):
        return F.HEAD["Paccayānulomaṃ"].split(" ", 1)[1]                # «အဟုတ်ပြ ပုံစံ» (pi-6)
    if t in ("Paccanīyaṃ",):
        return "အငြင်းပြ ပုံစံ"
    m = re.fullmatch(r"Gaṇanā (\w+?)mūlakā", t)
    if m and F._cond_word(m.group(1)):
        return F.cond(*F._swap(F._cond_word(m.group(1)))) + f"{MULAKA_ADJ} {GANANA}"
    # counting groups and «Tikādi», «Chakkādi», «Namaggatikaṃ», «Atthiādidukādi»
    m = re.fullmatch(r"(\w+?)(ka)ṃ", lt)
    if m and (m.group(1) + "ka") in F.GROUP:
        return F.GROUP[m.group(1) + "ka"]
    m = re.fullmatch(r"(tik|chakk|duk)ādi", lt)
    if m:
        g = {"tik": F.GROUP["tika"], "chakk": F.GROUP["chakka"], "duk": F.GROUP["duka"]}[m.group(1)]
        return f"{g} {F.ADI}"
    m = re.fullmatch(r"(\w+?)tikaṃ", lt)
    if m and F._cond_word(m.group(1)):
        return F.cond(*F._swap(F._cond_word(m.group(1)))) + "၏ " + F.TIKA
    m = re.fullmatch(r"(\w+?)ādidukādi", lt)
    if m and F._cond_word(m.group(1)):
        return F.cond(*F._swap(F._cond_word(m.group(1)))) + f" {F.ADI}တို့၏ {F.DUKA} {F.ADI}"
    # «X-Ydukāni» (two conditions' dyads)
    m = re.fullmatch(r"(\w+?)-(\w+?)dukāni", lt)
    if m and F._cond_word(m.group(1)) and F._cond_word(m.group(2)):
        return F._join_and([F.cond(*F._swap(F._cond_word(g))) for g in m.groups()]) + f"တို့၏ {F.GROUP['dukāni']}"
    # «Xādipaccayā», «Naadhipatyādi»
    m = re.fullmatch(r"(\w+?)ādipaccayā", lt)
    if m:
        for base in (m.group(1), m.group(1) + "a"):
            if F._cond_word(base):
                return F.cond(*F._swap(F._cond_word(base))) + " " + F.ADI
    m = re.fullmatch(r"(\w+?)yādi", lt)
    if m and F._cond_word(m.group(1) + "i"):
        return F.cond(*F._swap(F._cond_word(m.group(1) + "i"))) + " " + F.ADI
    # ghaṭanā kinds
    m = re.fullmatch(r"(\w+?)-?sāmaññaghaṭanā", lt)
    if m and F._cond_word(m.group(1)):
        return F.cond(*F._swap(F._cond_word(m.group(1)))) + "၏ " + F.HEAD["Sāmaññaghaṭanā"]
    m = re.fullmatch(r"(\w+?)missakaghaṭanā", lt)
    if m and F._cond_word(m.group(1)):
        return F.cond(*F._swap(F._cond_word(m.group(1)))) + f"၏ {MISSAKA} {F.GHATANA}"
    m = re.fullmatch(r"(\w+?)pakiṇṇakaghaṭanā", lt)
    if m and F._cond_word(m.group(1)):
        return F.cond(*F._swap(F._cond_word(m.group(1)))) + "၏ " + F.HEAD["Pakiṇṇakaghaṭanā"]
    m = re.fullmatch(r"(sahajāta-?)?(chand|vīriy|citt|vīmaṃs)ādhipatighaṭanā", lt)
    if m:
        adh = F.FIXED[m.group(2) + "ādhipati"][0]
        return (("အတူ ပေါ်ပေါက်သော " if m.group(1) else "") + adh + "၏ " + F.GHATANA)
    m = re.fullmatch(r"s(a|ā)(\w+(?:-\w+)*)ghaṭanā", lt)
    if m:
        cands = [m.group(2)] if m.group(1) == "a" else ["ā" + m.group(2), "a" + m.group(2)]
        for c in cands:
            try:
                stems = _stems_sa(c)
            except KeyError:
                continue
            return f"{F._join_and([F.cname(s) for s in stems])} {PAAWIN} {F.GHATANA}"
    raise KeyError("heading: " + t)


def heading2(text):
    """F.heading plus the sa-X parens «(sāsevanaṃ)» … of this chapter."""
    star = text.startswith("*") and text.endswith("*")
    t = text[1:-1] if star else text
    m = re.match(r"^(.*?) \((sāsevanaṃ|savipākaṃ|sāhāraṃ|saindriyaṃ)\)$", t)
    if m:
        out = F.heading(m.group(1)) + f" ({sa_x(SA_PAREN[m.group(2)])})"
        return f"*{out}*" if star else out
    return _HEADING(text)


_HEADING = F.heading


def setup_headings():
    F._heading = heading_core
    F.heading = heading2


# ===================================================================================== ghaṭanā compounds
_ORIG_SEGMENT = F.segment_conds


def segment_conds2(compound):
    """F.segment_conds plus «…atthīti» / «…natthīti» (the «īti» ending eats the stem's «i») and the ū-sandhi
    «ārammaṇūpanissaya» (ārammaṇa + upanissaya)."""
    c = compound
    if re.search(r"(?i)(?:^|-)n?atth$", c) or re.search(r"(?i)[aā]dhipat$", c):
        c += "i"
    c = re.sub(r"(?i)(ārammaṇ|anantar)ūpanissaya", lambda m: m.group(1) + "a-upanissaya", c)
    return _ORIG_SEGMENT(c)


def setup_ghatana():
    F.segment_conds = segment_conds2


# ===================================================================================== editorial notes
# Words of the notes (NEW unless marked): ṭhitena «… ၌ တည်၍», sabbattha «နေရာတိုင်း၌», pañhā «ပြဿနာ» (sample
# Pañhāvāro «ပြဿနာ»), nānākaraṇaṃ «ကွဲပြားချက်», natthi «မရှိ» (sample NOTES) / atthi «ရှိ», kātabbaṃ «ပြုရမည်»,
# paripuṇṇaṃ «ပြည့်စုံ» (sample), avasesa «ကြွင်းသည်» (sample), ṭhapetvā «ချန်ထား၍» (pi-2), etenupāyena
# «ဤနည်းဖြင့်», sajjhāyantena «သရဇ္ဈာယ်လျက်» (sample sajjhāya «သရဇ္ဈာယ်»), cakka «စက်ဝိုင်း».
VITTH = S.PH["vitthāretabbo"]                 # «အကျယ် ချဲ့ရမည်» (pi-5; sample)
GANETABBA = S.PH["gaṇetabbaṃ"]                # «ရေတွက်ရမည်» (sample)
KATABBA = "ပြုရမည်"
EVAM = S.PH["evaṃ"]                           # «ထိုနည်းတူ» (pi-2; sample)
KAYYA = "ကဲ့သို့"                              # yathā X «Xကဲ့သို့» (sample «(yathā kusalattikaṃ …)»)
SADISA = F.SADISA                             # «နှင့် တူသည်» (sample)
SADISANI = "နှင့် တူကြသည်"                    # -sadisāni (plural subject)
PANHA = F.HEAD["Pañhāvāro"].split("အလိုက်")[0]          # pañhā «ပြဿနာ» (sample heading)
THITA = "၌ တည်၍"
SABBATTHA = "နေရာတိုင်း၌"
NANAKARANA = "ကွဲပြားချက်"
AVASESA = "ကြွင်းသည်"
PARIPUNNA = W("paripuṇṇaṃ", "ပြည့်စုံ")
THAPETVA = W("ṭhapetvā", "ချန်ထား၍", "2")
ETENUPAYENA = "ဤနည်းဖြင့်"
SAJJHAYANTENA = "သရဇ္ဈာယ်လျက်"
NATTHI, ATTHI = "မရှိ", "ရှိ"
VERBS_N = {"vitthāretabbaṃ": VITTH, "vitthāretabbā": VITTH, "vitthāretabbāni": VITTH, "vitthāretabbo": VITTH,
           "gaṇetabbaṃ": GANETABBA, "kātabbaṃ": KATABBA, "kātabbo": KATABBA}
STEM_RX = "|".join(sorted(F.STEMS, key=len, reverse=True))
VARA_OF = {"paṭicca": "Paṭiccavāro", "sahajāta": "Sahajātavāro", "paccaya": "Paccayavāro", "nissaya": "Nissayavāro",
           "saṃsaṭṭha": "Saṃsaṭṭhavāro", "sampayutta": "Sampayuttavāro", "pañhā": "Pañhāvāro"}
ATTA = {k: F.HEAD[v].split("အလိုက်")[0] for k, v in VARA_OF.items() if k != "pañhā"}   # Xattaṃ «X ဖြစ်ခြင်း»
ORDER_N = {"anulomaṃ": "အဟုတ်ပြ ပုံစံ", "paccanīyaṃ": "အငြင်းပြ ပုံစံ", "anulomapaccanīyaṃ": "အဟုတ်ပြ အငြင်းပြ ပုံစံ",
           "paccanīyānulomaṃ": "အငြင်းပြ အဟုတ်ပြ ပုံစံ", "anulomagaṇanā": f"အဟုတ်ပြ ပုံစံ၏ {GANANA}",
           "paccanīyagaṇanā": f"အငြင်းပြ ပုံစံ၏ {GANANA}", "vibhaṅgo": F.HEAD["Vibhaṅgavāro"].split("အလိုက်")[0],
           "paccanīyuddhāro": F.HEAD["Paccanīyuddhāro"]}
ORDER_L = {"anulome": "အဟုတ်ပြ ပုံစံ၌", "paccanīye": "အငြင်းပြ ပုံစံ၌",
           "paccanīyavibhaṅge": f"အငြင်းပြ ပုံစံ၏ {ORDER_N['vibhaṅgo']}၌"}
WORDS_N = {"avasesaṃ": AVASESA, "avasesāni": AVASESA, "sabbaṃ": "အားလုံး", "paṭisandhi": F.PATISANDHI,
           "imāni padāni": f"ဤ {F.PADA}", "sabbāni padāni": f"{F.PADA} အားလုံး",
           "avasesāni padāni": f"ကြွင်းသော {F.PADA}", "abyākataṃ": f"{ABY} {F.DHAMMA}"}
PLURAL_N = {"avasesāni", "imāni padāni", "sabbāni padāni", "avasesāni padāni"}
BARE = {}                     # bare condition words of the notes: «vipākaṃ» name, «kamme» / «hetumhi» place, «-mpi»
for _st in F.STEMS:
    BARE[_st + "ṃ"] = (_st, "n")
    BARE[_st + "mpi"] = (_st, "pi")
    BARE[_st[:-1] + "e" if _st.endswith("a") else _st + "mhi"] = (_st, "loc")


def vara(w):
    return F.HEAD[VARA_OF[w]]


def thing(w):
    """One word (or fixed pair) of an editorial note -> (Burmese, kind): 'n' a name, 'pi' a name + «လည်း», 'l' a
    place («… ၌»), 'g' a counting (gaṇanā: «… အတိုင်း» after yathā, as the sample). Raises KeyError."""
    lw = w[0].lower() + w[1:]
    if lw in WORDS_N:
        return WORDS_N[lw], ("np" if lw in PLURAL_N else "n")
    m = re.fullmatch(r"(na|no)?(" + STEM_RX + r")paccay(aṃ|o|ā|ampi|āpi|opi)", lw)
    if m:
        my = F.cond(m.group(2), "n", bool(m.group(1)))
        return (my + "လည်း", "pi") if m.group(3).endswith("pi") else (my, "n")
    m = re.fullmatch(r"(na|no)?(" + STEM_RX + r")mūlak(aṃ|e|ā)", lw)
    if m:
        my = F.cond(m.group(2), "n", bool(m.group(1))) + F.MULAKA
        return (my + "၌", "l") if m.group(3) == "e" else (my, "n")
    m = re.fullmatch(r"(na|no)?(\w+)", lw)
    if m and m.group(2) in BARE:
        st, form = BARE[m.group(2)]
        neg = bool(m.group(1))
        if form == "loc":
            return F.cond(st, "loc", neg), "l"
        return F.cond(st, "n", neg) + ("လည်း" if form == "pi" else ""), form
    m = re.fullmatch(r"(na|no)?(\w+)yā", lw)           # hetuyā / adhipatiyā … (place)
    if m and m.group(2) + "yā" in F.LOC2STEM:
        return F.cond(F.LOC2STEM[m.group(2) + "yā"], "loc", bool(m.group(1))), "l"
    m = re.fullmatch(r"(paṭicca|sahajāta|paccaya|nissaya|saṃsaṭṭha|sampayutta|pañhā)vār(e|agaṇanā)", lw)
    if m:
        return (vara(m.group(1)) + "၌", "l") if m.group(2) == "e" else (f"{vara(m.group(1))}၏ {GANANA}", "g")
    if lw in ORDER_L:
        return ORDER_L[lw], "l"
    if lw in ORDER_N:
        return ORDER_N[lw], "n"
    raise KeyError("note word: " + w)


def _words(ws):
    """Join the fixed pairs («imāni padāni» …) into one item."""
    out, i = [], 0
    while i < len(ws):
        two = " ".join(ws[i:i + 2])
        if two in WORDS_N:
            out.append(two)
            i += 2
        else:
            out.append(ws[i])
            i += 1
    return out


def things(ws):
    """A run of note words: places / orders first, then names (several names get «၊»).
    -> (Burmese, kind of the last item, number of names)."""
    items = [thing(w) for w in _words(ws)]
    if all(k == "pi" for _, k in items):
        return (C + " ").join(o for o, _ in items), "pi", len(items)
    lead = []
    while items and items[0][1] == "l":
        lead.append(items.pop(0)[0])
    if any(k == "l" for _, k in items):
        raise KeyError("note order: " + " ".join(ws))
    body = (C + " ").join(o for o, _ in items)
    kind = items[-1][1] if items else "l"
    return " ".join(lead + ([body] if body else [])), kind, len(items)


def yatha_obj(ws):
    my, kind, n = things(ws)
    if kind == "l":
        return f"{my} ရှိသည့်အတိုင်း"
    if kind == "g":
        return f"{my}အတိုင်း"
    return my + KAYYA


def _marked(ws, mark):
    my, kind, n = things(ws)
    if kind == "pi":
        return my
    return my + ("တို့" if n > 1 or kind == "np" else "") + mark


def obj(ws):
    return _marked(ws, "ကို")


def subj(ws):
    return _marked(ws, "သည်")


def place(ws):
    my, kind, n = things(ws)
    if kind != "l":
        raise KeyError("place: " + " ".join(ws))
    return my


def sadisa_x(x):
    """The model of a «-sadisaṃ»: «hetupaccaya» / «nahetumūlaka» -> Burmese name."""
    if x.endswith("mūlaka"):
        return thing(x + "ṃ")[0]
    m = re.fullmatch(r"(na|no)?(" + STEM_RX + r")paccaya", x)
    if not m:
        raise KeyError("sadisa: " + x)
    return F.cond(m.group(2), "n", bool(m.group(1)))


V_ALT = "|".join(VERBS_N)


def note_clause(t):
    """One clause of an editorial note (lower case, «,» spaced) -> Burmese (KeyError / None if no frame)."""
    w = t.split()
    # (Yathā A[ vitthārito] [,] evaṃ [B] V)  /  (B yathā A [,] evaṃ V)
    m = re.fullmatch(r"(?:(?P<b>.+?) )?yathā (?P<a>.+?)(?P<vt> vitthārito)?(?: ,)? evaṃ(?: (?P<b2>.+?))? (?P<v>"
                     + V_ALT + r")", t)
    if m and not (m["b"] and m["b2"]):
        aw = m["a"].split()
        v = VERBS_N[m["v"]]
        if m["vt"]:
            return f"{obj(aw)} {S.PH['vitthārito']} {obj(m['b2'].split())} {EVAM} {v}"
        parts = []
        if m["b"]:
            parts.append(obj(m["b"].split()))
        parts += [yatha_obj(aw), EVAM]
        if m["b2"]:
            parts.append(obj(m["b2"].split()))
        return " ".join(parts + [v])
    m = re.fullmatch(r"yathā (?P<a>.+)", t)                       # (yathā A …) without evaṃ
    if m:
        return yatha_obj(m["a"].split())
    # (B yathā A)
    m = re.fullmatch(r"(?P<b>.+?) yathā (?P<a>.+?)", t)
    if m:
        return f"{subj(m['b'].split())} {yatha_obj(m['a'].split())} ဖြစ်သည်"
    # ([B] [L ṭhitena] [paripuṇṇaṃ] X-sadisaṃ / -sadisāni [kātabbaṃ])
    m = re.fullmatch(r"(?:(?P<b>.+?) )?(?:(?P<l>\S+) ṭhitena )?(?P<p>paripuṇṇaṃ )?(?P<x>\S+?)sadis(?P<e>aṃ|āni)"
                     r"(?P<k> kātabbaṃ)?", t)
    if m:
        x = sadisa_x(m["x"])
        th = f"{place([m['l']])[:-1]}{THITA} " if m["l"] else ""
        if m["k"]:
            return (f"{obj(m['b'].split())} " if m["b"] else "") + f"{th}{x}နှင့် တူအောင် {KATABBA}"
        pre = (PARIPUNNA + "စွာ ") if m["p"] else ""
        tu = SADISANI if m["e"] == "āni" else SADISA
        return (f"{subj(m['b'].split())} " if m["b"] else "") + f"{th}{pre}{x}{tu}"
    m = re.fullmatch(r"(?P<t>\S+) ṭhapetvā sabbattha (?P<v>" + V_ALT + ")", t)
    if m:
        return f"{obj([m['t']])} {THAPETVA} {SABBATTHA} {VERBS_N[m['v']]}"
    # (B V)  (Hetumūlakaṃ vitthāretabbaṃ / avasesāni padāni etenupāyena vitthāretabbāni)
    m = re.fullmatch(r"(?P<b>.+?)(?P<e> etenupāyena)?(?P<s> sajjhāyantena)? (?P<v>" + V_ALT + ")", t)
    if m:
        return " ".join(x for x in (obj(m["b"].split()), ETENUPAYENA if m["e"] else "",
                                     SAJJHAYANTENA if m["s"] else "", VERBS_N[m["v"]]) if x)
    # (L [L] X natthi / atthi)  (Navippayutte paṭisandhi natthi; Vipākamūlake āsevanaṃ natthi)
    m = re.fullmatch(r"(?P<l>.+?) (?P<x>\S+) (?P<v>natthi|atthi)", t)
    if m:
        return f"{place(m['l'].split())} {thing(m['x'])[0]} {NATTHI if m['v'] == 'natthi' else ATTHI}"
    # (L idaṃ nānākaraṇaṃ)
    m = re.fullmatch(r"(?P<l>.+?) idaṃ nānākaraṇaṃ", t)
    if m:
        return f"{place(m['l'].split())} ဤသည် {NANAKARANA} ဖြစ်သည်"
    # (Xattaṃ nāma Yattaṃ , Yattaṃ nāma Xattaṃ)
    m = re.fullmatch(r"(\w+?)ttaṃ nāma (\w+?)ttaṃ , (\w+?)ttaṃ nāma (\w+?)ttaṃ", t)
    if m:
        a, b, c, d = (ATTA[g] for g in m.groups())
        return f"{a} ဟူသည် {b} ဖြစ်သည်{C} {c} ဟူသည် {d} ဖြစ်သည်"
    return None


def note_body(b):
    """The text of an editorial note (without its brackets and end marks) -> Burmese, or None. A note of several
    clauses («A-sadisaṃ, B-sadisaṃ») is rendered clause by clause, joined by «၊»."""
    t = " ".join(b.replace(",", " ,").replace(";", " ;").split())
    if t in NOTE_FIXED:
        return NOTE_FIXED[t]
    try:
        r = note_clause(t)
    except KeyError:
        r = None
    if r is not None:
        return r
    parts = re.split(r" [,;] ", t)
    if len(parts) > 1:
        out = []
        for p in parts:
            r = NOTE_FIXED.get(p) or note_clause(p)
            if r is None:
                return None
            out.append(r)
        return (C + " ").join(out)
    return None


def _nf():
    """Hand-written notes (one unique sentence each; built from the shared words)."""
    cn = F.cname
    return {
        "ekekaṃ paccayaṃ mūlakaṃ kātūna sajjhāyantena gaṇetabbāti":
            f"{F.PACCAYA} တစ်ခုစီကို အခြေခံ ပြု၍ {SAJJHAYANTENA} {GANETABBA}",
        "ime tevīsatipaccayā sajjhāyantena vitthāretabbā":
            f"ဤ {F.PACCAYA} နှစ်ဆယ့်သုံးပါးတို့ကို {SAJJHAYANTENA} {VITTH}",
        "cakkaṃ bandhitabbaṃ": "စက်ဝိုင်း ဖွဲ့ရမည်", "cakkaṃ kātabbaṃ": f"စက်ဝိုင်း {KATABBA}",
        "ārammaṇe ṭhitena sabbattha tīṇeva pañhā":
            f"{F.cond('ārammaṇa', 'loc')[:-1]}{THITA} {SABBATTHA} {PANHA} {F.COUNT['tīṇi']}ပင် ရှိသည်",
        "yāvāsevanā sabbaṃ sadisaṃ": f"{cn('āsevana')}အထိ အားလုံး တူသည်",
        "nakamme gaṇite pañca pañhā honti":
            f"{F.cond('kamma', 'n', True)}ကို ရေတွက်သောအခါ {PANHA} {F.COUNT['pañca']} ရှိသည်",
        "naindriyapaccayā kamme satta pañhā":
            f"{F.cond('indriya', 'ab', True)}{C} {F.cond('kamma', 'loc')} {PANHA} {F.COUNT['satta']}",
        "sabbāni padāni vitthāretabbāni": f"{F.PADA} အားလုံးတို့ကို {VITTH}",
        "imāni alikhitesu padesu tīṇi pañhā": f"မရေးထားသော ဤ {F.PADA}တို့၌ {PANHA} {F.COUNT['tīṇi']} ရှိသည်",
        "napurejātamūlake nahetuyā ṭhitena āsevane ca magge ca eko pañho kātabbo":
            (f"{F.cond('purejāta', 'n', True)}{F.MULAKA}၌ {F.cond('hetu', 'loc', True)[:-1]}{THITA} "
             f"{F.cond('āsevana', 'loc')}{F.LAKAUNG}{C} {F.cond('magga', 'loc')}{F.LAKAUNG} {PANHA} "
             f"{F.COUNT['ekaṃ']}ကို {KATABBA}"),
        "saṃsaṭṭhavāre paccanīyavibhaṅge nakamme ca navipāke ca paṭisandhi natthi":
            (f"{vara('saṃsaṭṭha')}၌ {ORDER_L['paccanīyavibhaṅge']} {F.cond('kamma', 'loc', True)}{F.LAKAUNG}{C} "
             f"{F.cond('vipāka', 'loc', True)}{F.LAKAUNG} {F.PATISANDHI} {NATTHI}"),
        "avasesesu sabbattha atthi": f"ကြွင်းသော {SABBATTHA} {ATTHI}",
        "abyākataṃ paripuṇṇaṃ kātabbaṃ": f"{ABY} {F.DHAMMA}ကို {PARIPUNNA}အောင် {KATABBA}",
        "napacchājātapaccayampi naāsevanapaccayampi paripuṇṇaṃ":
            f"{F.cond('pacchājāta', 'n', True)}လည်း{C} {F.cond('āsevana', 'n', True)}လည်း {PARIPUNNA}သည်",
        "sattarasa": F.COUNT["sattarasa"],
        "paripuṇṇaṃ": f"{PARIPUNNA}သည်",
    }


NOTE_FIXED = {}


def note_unit(u):
    """A whole editorial note unit (with or without its brackets: a note may run over several units). A variant in
    braces at the end of the note is rendered after it."""
    var = ""
    m = re.search(r" (\{[^{}]*\})([.)]*)$", u)
    if m:
        var = " " + F.variant(m.group(1)[1:-1])
        u = u[:m.start()] + m.group(2)
        if not u.endswith(")") and u.startswith("("):
            F.SLIPS.add("note without its closing bracket («(yathā nahetumūlakaṃ {…}.»)")
    lead = "(" if u.startswith("(") else ""
    b = u[1:] if lead else u
    m = re.fullmatch(r"(.*?)([.)]*)", b)
    body, tail = m.group(1), m.group(2)
    if not body:
        return None
    body = body[0].lower() + body[1:]
    try:
        r = note_body(body)
    except KeyError:
        return None
    if r is None:
        return None
    if var:
        return lead + r + var + F.punct(tail)
    return lead + r + F.punct(tail)


def setup_notes():
    NOTE_FIXED.update(_nf())
    for st in F.STEMS:
        for neg in (False, True):
            pre = F.NEG_PREFIX[st] if neg else ""
            k = f"({pre}{st}paccayasadisaṃ)"
            if k not in F.NOTES:
                F.NOTES[k] = f"({F.cond(st, 'n', neg)}{SADISA})"
    F.NOTES["(sabbattha ekaṃ)"] = f"({SABBATTHA} {F.COUNT['ekaṃ']})"
    F.NOTES["(kātabbaṃ)"] = f"({KATABBA})"


# ===================================================================================== pieces (fragments of the vibhaṅga)
# A fragment that the sample's clause frame does not take is split at «, » / «; » into pieces, each one of:
#   a count alone («… tīṇi.»), a list of condition kinds («sahajātaṃ, pacchājātaṃ»), a pair
#   «[prefix] NP-acc LINK [NP]», «[NP-nom] NP-acc Xpaccayā …» («khandhā vatthuṃ vippayuttapaccayā»), a bare NP /
#   qualifier / prefix before «…» («bāhiraṃ…», «akusalaṃ dhammaṃ…»: a bare accusative takes the case marker of the
#   unit's link word), or a condition chain. Anything else falls back to the sample's lexicon (lex()).
# Condition kinds (the vibhaṅga of vippayutta / atthi / purejāta …) are named by the bare condition name N
# (as the sample's adhipati / upanissaya kinds «အာရုံ အကြီးအမှူး»); in the kamma section the sample's
# «sahajātā = အတူ ပေါ်ပေါက်သည့် ကံ» stays (CUR["cond"] tells the section).
KIND = {"sahajātaṃ": "sahajāta", "sahajāto": "sahajāta", "sahajātā": "sahajāta", "purejātaṃ": "purejāta",
        "pacchājātaṃ": "pacchājāta", "pacchājātā": "pacchājāta", "āhāraṃ": "āhāra", "indriyaṃ": "indriya"}
KIND_FIXED = {"ārammaṇapurejātaṃ": f"{F.N['ārammaṇa']} {F.N['purejāta']}",
              "vatthupurejātaṃ": f"{VATTHU} {F.N['purejāta']}"}
CUR = {"cond": None, "link": None, "fix": False}
_ORIG_LEX = F.lex
LINK_ALT = None


def kind_word(w):
    lw = w[0].lower() + w[1:]
    if lw in KIND_FIXED:
        return KIND_FIXED[lw]
    if lw in KIND and not (CUR["cond"] == "kamma" and lw == "sahajātā"):
        return F.N[KIND[lw]]
    return None


def _piece(p, slots, ti, ci, vi=None):
    """One piece (no «, »): -> Burmese or None. ti / ci / vi: [index] counters into slots T / C / V."""
    words = p.split()
    if not words:
        return ""
    if len(words) > 2 and words[1] == "§V§" and words[0] in F.PREFIX and vi is not None:   # «arūpe {…} …»
        v = slots["V"][vi[0]]
        r = _piece(" ".join(words[2:]), slots, ti, ci, vi)
        if r is None:
            return None
        vi[0] += 1
        return f"{F.PREFIX[words[0]]} {v} {r}"
    if re.search(r"(?<![\wāīūṃṅñṭḍṇḷ])(?:" + "|".join(F.VERB) + r")(?![\wāīūṃṅñṭḍṇḷ])", p):
        t0, c0 = ti[0], ci[0]
        try:
            r = F.clause(p, slots, ti, ci, [0], [0])
            return r
        except (KeyError, StopIteration, IndexError):
            ti[0], ci[0] = t0, c0
            return None
    m = re.fullmatch(r"(?P<x>.+) (?P<acc>\S+) (?P<ch>§C§ā)", p)          # «pair NP-acc Xpaccayā»
    if m and "§C§" not in m["x"] and re.search(r" (?:" + LINK_ALT + r")(?: |$)", m["x"]):
        t0 = ti[0]
        x = _piece(m["x"], slots, ti, ci, vi)
        if x is not None:
            try:
                a, _, k = np_my2([m["acc"]], iter(slots["T"][ti[0]:]), "a")
            except (KeyError, StopIteration):
                ti[0] = t0
                return None
            ti[0] += k
            st, neg = slots["C"][ci[0]]
            ci[0] += 1
            return f"{x} {a} {F.cond(st, 'ab', neg)}"
        ti[0] = t0
    if len(words) == 1 and words[0] in F.COUNT:
        return F.COUNT[words[0]]
    if len(words) == 1 and kind_word(words[0]):
        return kind_word(words[0])
    if len(words) > 2 and kind_word(words[-1]):                # «A dhammā B dhammassa sahajātaṃ, …»
        nd = nom_dat(words[:-1], slots, ti)
        if nd:
            return nd + " " + kind_word(words[-1])
    # pair «[prefix] A LINK [B]»
    m = re.fullmatch(r"(?:(?P<pre>" + "|".join(map(re.escape, F.PREFIX)) + r") )?(?P<a>.+?) (?P<link>" + LINK_ALT
                     + r")(?: (?P<b>.+))?", p)
    if m and "§C§" not in p and "§K§" not in p:
        try:
            terms = iter(slots["T"][ti[0]:])
            a, k1 = link_np(m["a"].split(), m["link"], terms)
            b, k2 = ("", 0)
            if m["b"]:
                b, _, k2 = np_my2(m["b"].split(), terms, "")
        except (KeyError, StopIteration):
            return None
        ti[0] += k1 + k2
        pre = F.PREFIX[m["pre"]] + " " if m["pre"] else ""
        return pre + a + (" " + b if b else "")
    # «[NP-nom] NP-acc Xpaccayā [Ypaccayā …]»
    m = re.fullmatch(r"(?P<np>.+?) (?P<ch>§C§ā(?: §C§ā)*)", p)
    if m:
        ws = m["np"].split()
        for j in range(len(ws) - 1, -1, -1):
            nom, acc = ws[:j], ws[j:]
            try:
                terms = iter(slots["T"][ti[0]:])
                n_my, k1 = ("", 0)
                if nom:
                    if F._case_of(nom) not in ("n",) and not nom[-1].startswith("§T§"):
                        continue
                    n_my, _, k1 = np_my2(nom, terms, "n")
                a_my, _, k2 = np_my2(acc, terms, "a")
            except (KeyError, StopIteration):
                continue
            ti[0] += k1 + k2
            chs = []
            for _ in m["ch"].split():
                st, neg = slots["C"][ci[0]]
                ci[0] += 1
                chs.append(F.cond(st, "ab", neg))
            return (n_my + " " if n_my else "") + a_my + " " + " ".join(chs)
        return None
    if "§" in p.replace("§T§", ""):
        return None
    # a bare NP / qualifier / prefix; «NP-nom NP-dat» before «…» («saddāyatanaṃ sotaviññāṇassa…»)
    if len(words) > 1:
        nd = nom_dat(words, slots, ti)
        if nd:
            return nd
    if p in F.PREFIX:
        return F.PREFIX[p]
    if p in F.QUAL:
        return F.QUAL[p]
    try:
        terms = iter(slots["T"][ti[0]:])
        r, _, k = np_my2(words, terms, "")
    except (KeyError, StopIteration):
        return None
    ti[0] += k
    case = F._case_of(words)
    if case == "a" and CUR["link"]:
        r = re.sub(r"များ$", "တို့", r) + ROLE_MARK[CUR["link"]]
    elif case == "g":
        r = re.sub(r"များ$", "တို့", r) + F.CASE["g"]
    return r


def nom_dat(words, slots, ti):
    """«NP-nom NP-dat» (no verb) -> «NPသည် NPအား», every split tried as in the sample's pañhā frame."""
    for j in range(len(words) - 1, 0, -1):
        aw, bw = words[:j], words[j:]
        if F._case_of(aw) != "n" or F._case_of(bw) != "g":
            continue
        try:
            terms = iter(slots["T"][ti[0]:])
            a, _, k1 = np_my2(aw, terms, "n")
            b, _, k2 = np_my2(bw, terms, "g")
        except (KeyError, StopIteration):
            continue
        ti[0] += k1 + k2
        return f"{a} {b}"
    return None


GH_ITI = re.compile(r"^(?P<lead>\s*)(?P<g>[\wāīūṃṅñṭḍṇḷ]+(?:-[\wāīūṃṅñṭḍṇḷ]+)+)(?:nti|īti) (?P<rest>.+)$")


def ghatana_frag(sk, slots):
    """«A-B-…-Zīti / -nti naX N, …» (a ghaṭanā with counts; the sample's GH_PRE takes «nti» only)."""
    m = GH_ITI.match(sk)
    if not m:
        return None
    try:
        stems, sl = F.segment_conds(m["g"])
        ci, ki, di = [0], [0], [0]
        r = F.chain(m["rest"], slots, ci, ki, di)
    except KeyError:
        return None
    return f"{m['lead']}{F.ghatana_list(stems)}နှင့် {r}"


def pieces(sk, slots):
    body = sk.strip()
    m = re.fullmatch(r"(.*?)([.,;]*)", body)
    body, trail = m.group(1), m.group(2)
    parts = re.split(r"(, |; )", body)
    ti, ci, vi = [0], [0], [0]
    out = []
    for p in parts:
        if p in (", ", "; "):
            out.append(C + " ")
            continue
        r = _piece(p, slots, ti, ci, vi)
        if r is None:
            return None
        out.append(r)
    if ti[0] != len(slots["T"]) or ci[0] != len(slots["C"]) or vi[0] != len(slots["V"]) or slots["K"] \
            or slots["D"]:
        return None
    lead = sk[:len(sk) - len(sk.lstrip())]
    return lead + "".join(out) + F.punct(trail)


def mark_terms(frag, slots):
    """A bare term «kusalaṃ» used as a noun in the pañhā prose gets its case marker: «… aniccato / assādeti /
    garuṃ katvā» object «Tကို», before a recipient subject «Tသည်» (the sample's lex leaves a term bare)."""
    words = frag.split()
    T = list(slots["T"])
    j = -1
    for i, w in enumerate(words):
        if not w.startswith("§T§"):
            continue
        j += 1
        if w != "§T§aṃ" or i + 1 >= len(words):
            continue
        nxt = words[i + 1].rstrip(",.;")
        if nxt in ("aniccato", "assādeti") or nxt == "garuṃ":
            T[j] = T[j] + "ကို"
            continue
        for n in range(4, 0, -1):
            key = " ".join(words[i + 1:i + 1 + n]).rstrip(",.;")
            if key in F.LEX and F.LEX[key][1] == "g":
                T[j] = T[j] + "သည်"
                break
    if T == slots["T"]:
        return slots
    s2 = dict(slots)
    s2["T"] = T
    return s2


def lex2(frag, slots, ti, ci, ki, di, vi):
    """The sample's lexicon first (its output stays as it is), then the pieces."""
    try:
        return _ORIG_LEX(frag, mark_terms(frag, slots), ti, ci, ki, di, vi)
    except (KeyError, IndexError) as e:
        err = e
    r = ghatana_frag(frag, slots)
    if r is None:
        r = pieces(frag, slots)
    if r is None:
        raise err
    ti[0], ci[0], ki[0], di[0], vi[0] = (len(slots[k]) for k in "TCKDV")
    return r


# ===================================================================================== line hook (context, fixes)
# Source slips normalised before translation (only for this chapter's run; each is logged).
FIXES = []


def _fixes():
    """Built after setup_numbers() (the count words above ten)."""
    return [
    (re.compile(r"(?<![\wāīūṃṅñṭḍṇḷ])([Nn]a|[Nn]o)[ -](?=(?:" + F._LOC_ALT + r") (?:" + F._CNT_ALT
                + r")(?![\wāīūṃṅñṭḍṇḷ]))"), r"\1", "negated count written apart / with a hyphen («na X», «na-X»)"),
    (re.compile(r"(?<![\wāīūṃṅñṭḍṇḷ])([Nn]a|[Nn]o) (?=(?:" + STEM_RX + r")paccayā(?![\wāīūṃṅñṭḍṇḷ]))"), r"\1",
     "negated condition written apart («na Xpaccayā»)"),
    (re.compile(r"(?<![\wāīūṃṅñṭḍṇḷ])Na (?=jhāne idaṃ)"), "Na", "«Na jhāne» for «Najhāne»"),
    (re.compile(r"naṃindriye"), "naindriye", "«naṃindriye» for «naindriye»"),
    (re.compile(r"(?<= )sattaṃ(?=,)"), "satta", "«sattaṃ» for «satta» (a count)"),
    (re.compile(r"Nadhipatipaccayā"), "Naadhipatipaccayā", "«Nadhipatipaccayā» for «Naadhipatipaccayā»"),
    (re.compile(r"naaññamañña-paccayā"), "naaññamaññapaccayā", "«naaññamañña-paccayā» (hyphen)"),
    (re.compile(r"adhipati paccayena"), "adhipatipaccayena", "«adhipati paccayena» written apart"),
    (re.compile(r"vippass(?=a(?:ti|nti))"), "vipass", "«vippassati / -anti» for «vipassati»"),
    (re.compile(r"Avigata āhāra-"), "Avigata-āhāra-", "«Avigata āhāra-» (hyphen missing)"),
    (re.compile(r"(?<=[\wāīūṃṅñṭḍṇḷ]) -(?=[\wāīūṃṅñṭḍṇḷ])|(?<=[\wāīūṃṅñṭḍṇḷ])- (?=[\wāīūṃṅñṭḍṇḷ])"), "-",
     "ghaṭanā: space at a hyphen"),
    (re.compile(r"(?<= )upanissaya(?= (?:dānaṃ|mānaṃ|pāṇaṃ|anuppannaṃ|jhānaṃ))"), "upanissāya",
     "«upanissaya» for «upanissāya» (a gerund)"),
    (re.compile(r"dve khandha nissāya"), "dve khandhe nissāya", "«dve khandha» for «dve khandhe»"),
    ]
_ORIG_LINE = F.line_my
HEAD_COND = re.compile(r"^#+ \*(?:Na|No)?(" + STEM_RX.replace("|", "|") + r")paccayo\*", re.I)


def line_my2(line):
    return _line_my3(line).replace(f"{VIPAKABY} {KIRIYABY}", f"{VIPAKABY}{C} {KIRIYABY}")


def _line_my3(line):
    if line.startswith("#"):
        m = re.match(r"^#+ \*([^*]+)\*", line)
        if m:
            t = m.group(1).lower()
            st = next((s for s in sorted(F.STEMS, key=len, reverse=True)
                       if re.fullmatch(r"(?:na|no)?" + s + r"paccayo", t)), None)
            CUR["cond"] = st if st else (CUR["cond"] if "paccay" not in t else None)
        return _ORIG_LINE(line)
    if CUR["fix"]:
        for rx, rep, why in FIXES:
            new = rx.sub(rep, line)
            if new != line:
                F.SLIPS.add(why)
                line = new
    return _ORIG_LINE(line)


def setup_pieces():
    global LINK_ALT
    FIXES[:] = _fixes()
    LINK_ALT = "|".join(sorted(F.LINK, key=len, reverse=True))
    F.lex = lex2
    F.line_my = line_my2


# ===================================================================================== the pañhāvāra lexicon (LEX)
# New LEX entries of this chapter (kinds as in my7_formulas: n / na / a / g / G / i / b / adj / v / x / post; «+» =
# plural). Every Burmese is logged in notes-ch1-01.md; values reused from pi-1 … pi-6 go through W().
ARAHA = W("arahā", "ရဟန္တာ", "5")
SEKKHA = W("sekkho", "ကျင့်ကြံဆဲသူ", "4")
PUTHUJJANA = W("puthujjano", "ပုထုဇဉ်", "1")
NIBBANA = W("nibbānaṃ", "နိဗ္ဗာန်", "5")
JHANA_N, MAGGA_N = F.N["jhāna"], F.N["magga"]
ORD = {"paṭham": "ပထမ", "dutiy": "ဒုတိယ", "tatiy": "တတိယ", "catutth": "စတုတ္ထ"}       # jhāna / magga ordinals
DIBBACAKKHU = W("dibbacakkhu", "နတ်မျက်စိ", "5")
DIBBASOTA = W("dibbasotaṃ", "နတ်နား", "5") + " ဓာတ်"                # dibbā sotadhātu (dhātu «ဓာတ်»)
KAYIKA = W("kāyikaṃ sukhaṃ", "ကိုယ်ပိုင်းဆိုင်ရာ", "1")
SUKHA, DUKKHA = W("kāyikaṃ sukhaṃ", "သာယာမှု", "1"), W("kāyikaṃ dukkhaṃ", "နာကျင်မှု", "1")
PARIKAMMA = "ကြိုတင် ပြင်ဆင်မှု"                                 # parikamma (the preliminary work; NEW)
CITTASAMANGI = F.TAIL["acittasamaṅgissa"][0]                       # «စိတ်နှင့် ပြည့်စုံသူ» (sample)
ARUPA_AY = {"ākāsānañcāyatana": F.LEX["ākāsānañcāyatanaṃ"][0], "viññāṇañcāyatana": F.LEX["viññāṇañcāyatanassa"][0],
            "ākiñcaññāyatana": F.LEX["ākiñcaññāyatanaṃ"][0],
            "nevasaññānāsaññāyatana": F.LEX["nevasaññānāsaññāyatanaṃ"][0]}
KIRIYA_CITTA = F.LEX["kiriyaṃ"][0]                                  # «ပြုရုံမျှသာ ဖြစ်သော စိတ်» (sample)
CRIME = {   # the deeds (nouns) of the upanissaya paragraphs: Pāli stem -> Burmese (pi-1 / pi-2 / pi-4)
    "pāṇātipāt": W("pāṇātipātā", "သူ့အသက်ကို သတ်ခြင်း", "2"),
    "adinnādān": W("adinnādānā", "မပေးသည်ကို ယူခြင်း", "2"),
    "kāmesumicchācār": W("kāmesumicchācārā", "ကာမတို့၌ မှားယွင်းစွာ ကျင့်ခြင်း", "2"),
    "musāvād": W("musāvādā", "မုသား ပြောခြင်း", "2"),
    "samphappalāp": W("samphappalāpā", "အကျိုးမဲ့ ပြိန်ဖျင်းသော စကား", "2"),
    "byāpād": W("byāpādo", "ဖျက်ဆီးလိုစိတ်", "1"),
}
PISUNA = W("pisuṇāya vācāya", "ကုန်းတိုက်သော စကား", "2")
PHARUSA = W("pharusāya vācāya", "ကြမ်းတမ်းသော စကား", "2")
ABHIJJHA = W("abhijjhā", "သူ့ဥစ္စာကို လိုချင်ခြင်း", "1")
MICCHADITTHI = W("micchādiṭṭhi", "မှားယွင်းသော အယူ", "1")
NIYATA = W("micchādiṭṭhiniyatā", "ကျိန်းသေသော", "1")
KAMMA5 = {"mātughāti": "အမိကို သတ်သော", "pitughāti": "အဖကို သတ်သော", "arahantaghāti": "ရဟန္တာကို သတ်သော",
          "ruhiruppāda": "မြတ်စွာဘုရား၏ သွေးကို ထွက်စေသော", "saṅghabheda": "သံဃာကို ဖြိုခွဲသော"}   # NEW (+ «ကံ»)
PATISAMBHIDA = {"attha": W("atthapaṭisambhidā", "အကျိုးအနက်ကို ပိုင်းခြားသိသော ဉာဏ်", "2"),
                "dhamma": W("dhammapaṭisambhidā", "တရားကို ပိုင်းခြားသိသော ဉာဏ်", "2"),
                "nirutti": W("niruttipaṭisambhidā", "စကားဖြင့် ဖော်ပြမှုကို ပိုင်းခြားသိသော ဉာဏ်", "2"),
                "paṭibhāna": W("paṭibhānapaṭisambhidā", "ဉာဏ်ပေါ်မှုကို ပိုင်းခြားသိသော ဉာဏ်", "2")}
THANATHANA = "ဖြစ်နိုင်ခြင်းနှင့် မဖြစ်နိုင်ခြင်း၌ " + W("kosallaṃ", "ကျွမ်းကျင်ခြင်း", "1")   # ṭhānāṭhānakosalla
NANA = {"cetopariyañāṇ": F.LEX["cetopariyañāṇassa"][0], "pubbenivāsānussatiñāṇ": F.LEX["pubbenivāsānussatiñāṇassa"][0],
        "yathākammūpagañāṇ": F.LEX["yathākammūpagañāṇassa"][0], "anāgataṃsañāṇ": F.LEX["anāgataṃsañāṇassa"][0],
        "iddhividhañāṇ": F.LEX["iddhividhañāṇassa"][0]}
GERUND = {  # the deeds as gerunds («… -tvā»), before «tassa paṭighātatthāya …»
    "pāṇaṃ hantvā": "သတ္တဝါကို သတ်၍", "adinnaṃ ādiyitvā": "မပေးသည်ကို ယူ၍", "musā bhaṇitvā": "မုသား ပြော၍",
    "pisuṇaṃ bhaṇitvā": "ကုန်းတိုက်သော စကားကို ပြော၍", "pharusaṃ bhaṇitvā": "ကြမ်းတမ်းသော စကားကို ပြော၍",
    "samphaṃ palapitvā": "အကျိုးမဲ့ ပြိန်ဖျင်းသော စကားကို ပြော၍", "sandhiṃ chinditvā": "အိမ်ကို ဖောက်ထွင်း၍",
    "nillopaṃ haritvā": "ဥစ္စာကို လုယူ၍", "ekāgārikaṃ karitvā": "အိမ်တစ်လုံးတည်းကို ဝိုင်း၍ တိုက်ပြီး",
    "paripanthe ṭhatvā": "လမ်းခရီး၌ ဓားပြ တိုက်ပြီး", "paradāraṃ gantvā": "သူတစ်ပါး၏ မယားထံ သွား၍",
    "gāmaghātaṃ karitvā": "ရွာကို ဖျက်ဆီး၍ လုယက်ပြီး", "nigamaghātaṃ karitvā": "နိဂုံးကို ဖျက်ဆီး၍ လုယက်ပြီး",
    "mātaraṃ jīvitā voropetvā": "အမိကို အသက်မှ သတ်၍", "pitaraṃ jīvitā voropetvā": "အဖကို အသက်မှ သတ်၍",
    "arahantaṃ jīvitā voropetvā": "ရဟန္တာကို အသက်မှ သတ်၍",
    "duṭṭhena cittena tathāgatassa lohitaṃ uppādetvā": "ပြစ်မှားသော စိတ်ဖြင့် မြတ်စွာဘုရား၏ သွေးကို ထွက်စေ၍",
    "saṅghaṃ bhinditvā": "သံဃာကို ဖြိုခွဲ၍", "tassa paṭighātatthāya": "ထိုအမှုကို ပယ်ဖျက်ရန်အတွက်",
}


def setup_lex():
    F.add_lex("n", {"arahā": ARAHA, "sekkhā": SEKKHA + "+", "maggo": MAGGA_N,
                    "phalasamāpatti": F.LEX["phalasamāpattiyā"][0], "dibbacakkhu": DIBBACAKKHU,
                    "dibbasotadhātu": DIBBASOTA, "abhijjhā": ABHIJJHA, "micchādiṭṭhi": MICCHADITTHI,
                    "niyatamicchādiṭṭhi": f"{NIYATA} {MICCHADITTHI}", "pisuṇavācā": PISUNA,
                    "pharusavācā": PHARUSA,
                    "kusalādhipati": f"{F.TRIADS['kusala']['kusal']} {F.N['adhipati']}",
                    "akusalādhipati": f"{F.TRIADS['kusala']['akusal']} {F.N['adhipati']}",
                    "vipākābyākatakiriyābyākatādhipati": f"{VIPAKABY}{C} {KIRIYABY} {F.N['adhipati']}"})
    for stem, my in CRIME.items():
        F.add_lex("n", {stem + "o": my})
        F.add_lex("a", {stem + "aṃ": my})
        F.add_lex("g", {stem + "assa": my})
    F.add_lex("g", {"pisuṇāya vācāya": PISUNA, "pharusāya vācāya": PHARUSA, "abhijjhāya": ABHIJJHA,
                    "micchādiṭṭhiyā": MICCHADITTHI, "niyatamicchādiṭṭhiyā": f"{NIYATA} {MICCHADITTHI}",
                    "dibbāya sotadhātuyā": DIBBASOTA, "sekkhānaṃ": SEKKHA + "+",
                    "kāyikassa sukhassa": f"{KAYIKA} {SUKHA}", "kāyikassa dukkhassa": f"{KAYIKA} {DUKKHA}",
                    "ṭhānāṭhānakosallassa": THANATHANA, "ākāsānañcāyatanassa": ARUPA_AY["ākāsānañcāyatana"],
                    "ākiñcaññāyatanassa": ARUPA_AY["ākiñcaññāyatana"], "vipākassa": F.N["vipāka"],
                    "kiriyassa": KIRIYA_CITTA})
    for p, my in PATISAMBHIDA.items():
        F.add_lex("g", {p + "ppaṭisambhidāya": my})
    for k, my in KAMMA5.items():
        F.add_lex("n", {k + "kammaṃ": f"{my} {F.N['kamma']}"})
        F.add_lex("g", {k + "kammassa": f"{my} {F.N['kamma']}"})
    for p, my in NANA.items():
        F.add_lex("n", {p + "aṃ": my})
    for o, my in ORD.items():
        F.add_lex("n", {f"{o}aṃ jhānaṃ": f"{my} {JHANA_N}", f"{o}o maggo": f"{my} {MAGGA_N}"})
        F.add_lex("g", {f"{o}assa jhānassa": f"{my} {JHANA_N}", f"{o}assa maggassa": f"{my} {MAGGA_N}"})
    F.add_lex("g", {"dibbassa cakkhussa": DIBBACAKKHU})
    for ay, my in ARUPA_AY.items():
        F.add_lex("n", {ay + "kusalaṃ": f"{my} {F.TRIADS['kusala']['kusal']}",
                        ay + "kiriyaṃ": f"{my} {KIRIYA_CITTA}"})
        F.add_lex("g", {ay + "kusalassa": f"{my} {F.TRIADS['kusala']['kusal']}",
                        ay + "vipākassa": f"{my} {F.N['vipāka']}", ay + "kiriyassa": f"{my} {KIRIYA_CITTA}"})
    F.add_lex("na", {"viññāṇañcāyatanaṃ": ARUPA_AY["viññāṇañcāyatana"], "parikammaṃ": PARIKAMMA, "nibbānaṃ": NIBBANA,
                     "kāyikaṃ sukhaṃ": f"{KAYIKA} {SUKHA}", "kāyikaṃ dukkhaṃ": f"{KAYIKA} {DUKKHA}",
                     "utu": UTU, "utuṃ": UTU, "bhojanaṃ": W("bhojane", "အစားအစာ", "1"),
                     "senāsanaṃ": W("senāsanaṃ", "အိပ်ရာ နေရာ", "2")})
    F.add_lex("a", {"cakkhuṃ": W("cakkhuṃ", "မျက်စိ", "1"), "sotaṃ": W("sotaṃ", "နား", "1"),
                    "ghānaṃ": "နှာခေါင်း", "jivhaṃ": "လျှာ", "kāyaṃ": "ကိုယ်",
                    "rūpe": W("rūpe", "အဆင်းအရောင်", "5") + "+", "sadde": W("sadde", "အသံ", "5") + "+",
                    "gandhe": "အနံ့+", "rase": "အရသာ+", "phoṭṭhabbe": "အထိအတွေ့+",
                    "jhānaṃ": JHANA_N, "maggaṃ": MAGGA_N, "gotrabhuṃ": F.LEX["gotrabhu"][0],
                    "vicikicchaṃ": F.LEX["vicikicchā"][0], "saṅkhāre": W("saṅkhāre", "ပြုပြင်ဖန်တီးမှု", "1") + "+",
                    "pubbe suciṇṇāni": "ရှေးက ကောင်းစွာ ကျင့်ခဲ့ဖူးသော အမှု+"})
    F.add_lex("G", {"arahato": ARAHA, "kusalacittasamaṅgissa": f"{F.TRIADS['kusala']['kusal']} {CITTASAMANGI}",
                    "akusalacittasamaṅgissa": f"{F.TRIADS['kusala']['akusal']} {CITTASAMANGI}",
                    "vipākābyākatakiriyābyākatacittasamaṅgissa": f"{VIPAKABY}{C} {KIRIYABY} {CITTASAMANGI}"})
    F.add_lex("adj", {"sekkhāya": W("sekkhā", "ကျင့်ကြံဆဲသူ၏", "1", key="sekkhāya")})
    F.add_lex("g", {"sekkhāya phalasamāpattiyā": f"{F.LEX['sekkhāya'][0]} {F.LEX['phalasamāpattiyā'][0]}"})
    F.add_lex("i", {"dibbena cakkhunā": DIBBACAKKHU})
    F.add_lex("v", {"vipassanti": "ထိုးထွင်း၍ ရှုကြသည်"})
    F.add_lex("x", {"sekkhā vā puthujjanā vā": f"{SEKKHA}တို့သော်လည်းကောင်း{C} {PUTHUJJANA}တို့သော်လည်းကောင်း",
                    "rūpaṃ passati": "အဆင်းအရောင်ကို မြင်သည်", "rūpaṃ passanti": "အဆင်းအရောင်ကို မြင်ကြသည်",
                    "saddaṃ suṇāti": W("saddaṃ", "အသံ", "1") + "ကို " + W("suṇāti", "ကြားသည်", "1"),
                    "saddaṃ suṇanti": "အသံကို ကြားကြသည်",
                    "dibbāya sotadhātuyā saddaṃ suṇāti": f"{DIBBASOTA}ဖြင့် အသံကို ကြားသည်",
                    "dibbāya sotadhātuyā saddaṃ suṇanti": f"{DIBBASOTA}ဖြင့် အသံကို ကြားကြသည်",
                    "niruddhe vipāko tadārammaṇatā uppajjati":
                        f"ချုပ်ငြိမ်းသောအခါ {F.VIPAKA_ADJ} စိတ်သည် ထိုအာရုံကို အာရုံပြုသည့် အနေဖြင့် {F.UP}",
                    "anuppannaṃ kiriyasamāpattiṃ uppādeti":
                        f"{W('anuppannā', 'မဖြစ်ပေါ်သေးသော', '2')} {KIRIYA_CITTA[:-len(' စိတ်')]} သမာပတ်ကို ဖြစ်စေသည်",
                    "uppannaṃ samāpajjati": "ဖြစ်ပေါ်ပြီးသော သမာပတ်ကို ဝင်စားသည်",
                    "anuppannaṃ samāpattiṃ uppādenti": "မဖြစ်ပေါ်သေးသော သမာပတ်ကို ဖြစ်စေကြသည်",
                    "uppannaṃ samāpajjanti": "ဖြစ်ပေါ်ပြီးသော သမာပတ်ကို ဝင်စားကြသည်",
                    "upanissaya": F.N["upanissaya"]})
    F.add_lex("x", GERUND)
    F.add_qual("ကုသိုလ်", "kusalāni")
    F.add_qual("အကုသိုလ်", "akusalāni")
    F.add_qual(VIPAKABY, "vipākābyākatāni")
    F.add_qual(KIRIYABY, "kiriyābyākatāni")
    F.add_qual(F.AHETUKA, "ahetukā")
    F.add_qual(f"{F.AHETUKA} {VIPAKABY}", "ahetukavipākābyākatā")
    F.add_qual("သိစိတ် ငါးပါးနှင့်အတူ ဖြစ်သော", "pañcaviññāṇasahagataṃ")       # as the sample's catuviññāṇa
    F.add_qual(W("purejātārammaṇā", "ရှေးဦးစွာ ဖြစ်ပေါ်ပြီးသော", "2"), "purejātaṃ")
    F.add_qual(BAHIRA, "bāhire")
    F.add_qual(f"{F.N['āhāra']}မှ ဖြစ်ပေါ်လာသော", "āhārasamuṭṭhāne")
    F.add_qual(f"{UTU}မှ ဖြစ်ပေါ်လာသော", "utusamuṭṭhāne")
    F.add_qual(CITTASAM, "cittasamuṭṭhānañca")
    F.add_fixed(F.FIXED["kabaḷīkāro §V§ āhāro"][0], "n", False, "kabaḷīkāro āhāro")
    F.add_noun(F.N["kamma"], n=["kammaṃ"])
    F.add_noun(F.N["vipāka"], g=["vipākassa"])
    for k in ("kusalādhipati", "akusalādhipati", "vipākābyākatakiriyābyākatādhipati"):
        F.add_fixed(F.LEX[k][0], "n", False, k)
    F.add_lex("a", {"vipākābyākate kiriyābyākate khandhe": f"{VIPAKABY}{C} {KIRIYABY} {F.KHANDHA}+"})
    F.add_lex("x", {"purejātaṃ": F.N["purejāta"]})
    F.add_lex("v", {"assādeti": "သာယာသည်", "abhinandati": "နှစ်သက်သည်"})
    for k, (my, kind) in list(F.LEX.items()):          # «X ca, Y ca» recipients: «Xအားလည်းကောင်း၊ …»
        if kind == "g" and " " not in k[-3:]:
            pl = my.endswith("+")
            F.LEX.setdefault(k + " ca", ((my[:-1] + "တို့" if pl else my) + F.CASE["g"] + F.LAKAUNG, "x"))
    F.EDNOTES["āruppe (sabbattha)"] = f"{F.VAR_P} ({SABBATTHA}): āruppe"
    F.NOTES["(saṃkhittaṃ.)"] = "(" + F.NOTES["(saṃkhittaṃ)"][1:-1] + END + ")"
    F.NOTES["(adhipati paṭisandhikkhaṇe natthi.)"] = f"({F.PREFIX['paṭisandhikkhaṇe']} {F.cname('adhipati')} {NATTHI}{END})"
    for w in F.COUNT:
        F.NOTES.setdefault(f"(sabbattha {w})", f"({SABBATTHA} {F.COUNT[w]})")
    F.NOTES["(naāsevanapaccayamūlakampi nahetumūlakasadisaṃ.)"] = \
        (f"({F.cond('āsevana', 'n', True)}{F.MULAKA}သည်လည်း {F.cond('hetu', 'n', True)}{F.MULAKA}{SADISA}{END})")
    F.NOTES["(imāni tīṇi mūlāni ekasadisāni)"] = f"(ဤ အခြေခံ {F.COUNT['tīṇi']}တို့သည် တူညီကြသည်)"


# the «X parikammaṃ X» sentences of the upanissaya section: «X၏ ကြိုတင် ပြင်ဆင်မှုသည် Xအား …»
PARIKAMMA_RE = re.compile(r"^(?P<a>.+?) parikammaṃ (?P<b>.+?) (?P<r>§C§ena paccayo\.?)$")


def parikamma_unit(s):
    sk, slots = F.slot(F.lc(s))
    m = PARIKAMMA_RE.match(sk)
    if not m or m["a"] not in F.LEX or F.LEX[m["a"]][1] != "g" or m["b"] not in F.LEX:
        return None
    st, neg = slots["C"][0]
    return (f"{F.LEX[m['a']][0]}၏ {PARIKAMMA}သည် {F.LEX[m['b']][0]}အား {F.iframe(st)}"
            + F.punct(m["r"][len("§C§ena paccayo"):]))


# ===================================================================================== unit hook
_ORIG_UNIT = F.unit_my
NOTE_START = re.compile(r"^(\([^()]*\)\.?) (\S.*)$")              # «(note.) rest»
NOTE_END = re.compile(r"^(.*\S) (\((?:[^(){}]|\{[^{}]*\})*\)?\.?)$")                 # «rest… (note).» / «rest… (note.»


def unit_my2(u):
    if not u.strip():
        return u
    lead = u[:len(u) - len(u.lstrip())]
    s = u.strip()
    lk = re.search(r"(?<![\wāīūṃṅñṭḍṇḷ])(" + LINK_ALT + r")(?![\wāīūṃṅñṭḍṇḷ])", s)
    CUR["link"] = lk.group(1) if lk else None
    r = None
    if s.startswith("(") or s.endswith(")") or re.fullmatch(r"[\w\s,;āīūṃṅñṭḍṇḷ]+\.", s):
        r = note_unit(s)
    if r is None:
        r = special_unit(s)
    if r is None:
        r = parikamma_unit(s)
    if r is None:
        m = NOTE_START.match(s)
        if m and note_any(m.group(1)) is not None:
            r = note_any(m.group(1)) + " " + unit_my2(m.group(2))
    if r is None:
        m = re.match(r"^([^()]+\.\)) (\S.*)$", s)                  # «Paripuṇṇaṃ.) Avigate tīṇi.»
        if m and note_any(m.group(1)) is not None:
            r = note_any(m.group(1)) + " " + unit_my2(m.group(2))
    if r is None:
        m = re.match(r"^(.*\S) (\([^()]*\)\.?) ([A-ZĀ].*)$", s)       # «… (saṃkhittaṃ.) Saṅghaṃ bhindati.»
        if m and note_any(m.group(2)) is not None:
            r = unit_my2(m.group(1)) + " " + note_any(m.group(2)) + " " + unit_my2(m.group(3))
    if r is None:
        m = NOTE_END.match(s)
        if m and m.group(2).startswith("(") and note_any(m.group(2)) is not None:
            r = unit_my2(m.group(1)) + " " + note_any(m.group(2))
    if r is not None:
        return lead + r
    return _ORIG_UNIT(u)


def note_any(s):
    r = note_unit(s)
    return r if r is not None else special_unit(s)


def special_unit(s):
    """Lines and fragments of a fixed shape: «Xmūlakaṃ.», «Xvāre anulomaṃ.», «Pañhāvārassa …», «(Savipākaṃ»,
    «5)», «(Saṃkhittaṃ.)»."""
    ls = s[0].lower() + s[1:] if s[:1].isalpha() else s
    if re.fullmatch(r"[\wāīūṃṅñṭḍṇḷ]+", s) and kind_word(s):        # a condition-kind label «Sahajātā –»
        return kind_word(s)
    m = re.fullmatch(r"(na|no)?(" + STEM_RX + r")mūlakaṃ(\.?)", ls)
    if m:
        return F.cond(m.group(2), "n", bool(m.group(1))) + F.MULAKA + F.punct(m.group(3))
    m = re.fullmatch(r"(paṭicca|sahajāta|paccaya|nissaya|saṃsaṭṭha|sampayutta)vāre (\w+)(\.?)", ls)
    if m and m.group(2) in ORDER_N:
        return f"{vara(m.group(1))}၌ {ORDER_N[m.group(2)]}" + F.punct(m.group(3))
    m = re.fullmatch(r"pañhāvārassa (\w+)(\.?)", ls)
    if m and m.group(1) in ORDER_N:
        return f"{vara('pañhā')}၏ {ORDER_N[m.group(1)]}" + F.punct(m.group(2))
    m = re.fullmatch(r"\((s|)(a|ā)(vipāka|sevana|hāra|indriya)ṃ", s.lower())
    if m:
        stem = {"vipāka": "vipāka", "sevana": "āsevana", "hāra": "āhāra", "indriya": "indriya"}[m.group(3)]
        return "(" + sa_x(stem, neg=not m.group(1))
    if re.fullmatch(r"\d+\)", s):
        return s
    if s == "Paccanīyaṃ":
        return "အငြင်းပြ ပုံစံ"
    m = re.fullmatch(r"(\w+) niṭṭhitaṃ\.", s)
    if m and m.group(1) in F.TIKA_NAME:
        return F.finished(F.TIKA_NAME[m.group(1)])
    m = re.fullmatch(r"([A-ZĀ]\w+(?: \w+)?)\.", s)
    if m:
        try:
            return heading_core(m.group(1)) + END
        except KeyError:
            pass
    m = re.fullmatch(r"((?:\S+ ca, )+\S+ ca)", ls)
    if m:
        try:
            return (C + " ").join(thing(p.split()[0])[0] + F.LAKAUNG for p in m.group(1).split(", "))
        except KeyError:
            pass
    m = re.fullmatch(r"(\(?)(saṃkhittaṃ|saṅkhitaṃ)([.)]*)", s.lower())
    if m:
        if m.group(2) == "saṅkhitaṃ":
            F.SLIPS.add("«Saṅkhitaṃ» for «Saṃkhittaṃ» (^7-2-70)")
        return m.group(1) + F.NOTES["(saṃkhittaṃ)"][1:-1] + F.punct(m.group(3))
    return None


def setup_units():
    F.unit_my = unit_my2


setup_nouns()
setup_engine()
setup_numbers()
setup_headings()
setup_ghatana()
setup_notes()
setup_units()
setup_pieces()
setup_lex()


# ===================================================================================== run
class Counting(dict):
    cnt = collections.Counter()

    def setdefault(self, k, v):
        self.cnt[k] += 1
        return super().setdefault(k, v)


def regress():
    bad = 0
    for n in S.NAMES:
        txt = F.translate((PALI / n).read_text(encoding="utf-8-sig"))
        pub = (OUT / n).read_text(encoding="utf-8")
        if txt != pub:
            bad += 1
            for i, (a, b) in enumerate(zip(txt.splitlines(), pub.splitlines()), 1):
                if a != b:
                    print(f"{n}:{i}\n  new {a[:300]}\n  pub {b[:300]}")
                    break
        print(n, "identical" if txt == pub else "DIFFERS")
    return bad


def main():
    if "--regress" in sys.argv:
        sys.exit(1 if regress() else 0)
    F.DEV = "--dev" in sys.argv
    CUR["fix"] = True
    src = (PALI / NAME).read_text(encoding="utf-8-sig")
    if F.DEV:
        F.UNSEEN = Counting()
    txt = F.translate(src)
    if F.DEV:
        rows = sorted(F.UNSEEN.items(), key=lambda kv: -F.UNSEEN.cnt[kv[0]])
        CHK.mkdir(exist_ok=True)
        with open(CHK / "dev.txt", "w", encoding="utf-8") as fh:
            for k, v in rows:
                fh.write(f"[{F.UNSEEN.cnt[k]}] SK: {k}\n    {v}\n")
        (CHK / "dev-out.md").write_text(txt, encoding="utf-8")
        print(len(rows), "unmatched skeletons,", sum(F.UNSEEN.cnt.values()), "occurrences")
    else:
        (OUT / NAME).write_text(txt, encoding="utf-8")
        print(f"wrote {NAME}: {sum(1 for l in txt.splitlines() if l)} lines")
    if F.SLIPS and "--slips" in sys.argv:
        print("slips:", *sorted(F.SLIPS), sep="\n  ")


if __name__ == "__main__":
    main()
